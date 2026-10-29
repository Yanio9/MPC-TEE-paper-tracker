"""Run every enabled source independently; keep source checkpoints transactional."""
from __future__ import annotations

import copy
import logging
import os
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import yaml

from .core import PaperStore, classify, read_json, write_json, year_bounds, in_year_range
from .enrichment import enrich
from .output import write_outputs
from .sources import COLLECTORS, HttpClient

LOG = logging.getLogger(__name__)


def load_config(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    if set(config["topics"]) != {"MPC", "TEE"}:
        raise ValueError("Expected independent MPC and TEE topics")
    if not re.fullmatch(r"[\w.-]+/[\w.-]+", config["project"]["repository"]):
        raise ValueError("Invalid repository owner/name")
    for topic in config["topics"].values():
        for pattern in topic["patterns"] + [topic["acronym_pattern"], topic["context_pattern"]]:
            re.compile(pattern)
    for key in ("years_ahead", "overlap_days", "years_back", "initial_lookback_days"):
        if key in config["tracking"] and (type(config["tracking"][key]) is not int or config["tracking"][key] < 0):
            raise ValueError(f"tracking.{key} must be a nonnegative integer")
    first_year = config["tracking"].get("start_year")
    if first_year is not None and (type(first_year) is not int or not 1000 <= first_year <= date.today().year):
        raise ValueError("tracking.start_year must be a valid publication year, no later than this year")
    return config


def run(root: Path, config: dict, selected: list[str] | None = None, since: date | None = None,
        dry_run: bool = False, now: datetime | None = None, collectors=None, client_factory=HttpClient,
        no_enrich: bool = False, refresh: bool = False) -> dict:
    now = now or datetime.now(timezone.utc)
    stamp = now.isoformat(timespec="seconds")
    today = now.date()
    first_year, last_year = year_bounds(config, today)
    first_date = date(first_year, 1, 1)
    backfill = since is not None
    cache = read_json(root / "data" / "papers.json", {"schema_version": 1, "papers": {}})
    state = read_json(root / "data" / "state.json", {"schema_version": 1, "sources": {}, "pending": []})
    if cache.get("schema_version") != 1 or state.get("schema_version") != 1:
        raise ValueError("Unsupported cache schema; refusing to overwrite")
    store = PaperStore(cache["papers"])
    pending = set(state.get("pending", []))
    report = {"started_at": stamp, "start_year": first_year, "backfill": backfill, "refresh": refresh, "sources": {}, "enrichment_errors": []}
    collectors = collectors or COLLECTORS
    # Reapply user exclusions after config edits, without migrating unrelated FL cache.
    for identifier, paper in list(store.papers.items()):
        matched = classify(paper, config)
        if not matched or not in_year_range(paper, first_year, last_year):
            del store.papers[identifier]
            pending.discard(identifier)
        else:
            paper["topics"] = sorted(matched)
            paper["matched_terms"] = matched
    store = PaperStore(store.papers)
    for name, source_cfg in config["sources"].items():
        if not source_cfg["enabled"] or (selected and name not in selected):
            report["sources"][name] = {"status": "disabled" if not source_cfg["enabled"] else "not selected"}
            continue
        previous = state["sources"].get(name, {})
        if not refresh and previous.get("last_success", "")[:10] == today.isoformat() and since is None:
            report["sources"][name] = {"status": "cached", "message": "Already completed today (UTC)"}
            continue
        lower_bound = since or (date.fromisoformat(previous["last_success"][:10]) - timedelta(days=config["tracking"]["overlap_days"])
                                if previous.get("last_success") else first_date)
        lower_bound = max(first_date, lower_bound)
        if not refresh and backfill and previous.get("last_success", "")[:10] == today.isoformat() and previous.get("coverage_start", "9999-12-31") <= lower_bound.isoformat():
            report["sources"][name] = {"status": "cached", "message": "Requested historical interval already completed today"}
            continue
        upper_bound = today
        if not refresh and name == "eprint" and previous.get("last_success", "")[:10] == today.isoformat():
            # A requested historical backfill is a different, older OAI interval; do not
            # refresh the recently scanned daily window a second time today.
            upper_bound = today - timedelta(days=config["tracking"]["overlap_days"] + 1)
            if not backfill or lower_bound > upper_bound:
                report["sources"][name] = {"status": "cached", "message": "ePrint daily window already scanned; no older backfill interval"}
                continue
        staged = PaperStore(store.papers)
        staged_pending = set(pending)
        received = matched_count = new_count = 0
        LOG.info("Scanning %s since %s", name, lower_bound)
        try:
            client = client_factory(name, source_cfg["interval_seconds"], config["project"].get("contact_email", ""))
            for paper in collectors[name](config, client, upper_bound, lower_bound):
                received += 1
                if not paper.get("title") or not paper.get("records"):
                    raise ValueError(f"{name} returned an incomplete record")
                if not in_year_range(paper, first_year, last_year):
                    continue
                matched = classify(paper, config)
                if not matched:
                    continue
                paper["topics"], paper["matched_terms"] = sorted(matched), matched
                matched_count += 1
                identifier, is_new = staged.add(paper, stamp)
                new_count += int(is_new)
                if is_new and not backfill and (previous.get("last_success") or config["notifications"]["notify_on_first_run"]):
                    staged_pending.add(identifier)
            store = staged
            pending = {store.resolve(identifier) for identifier in staged_pending}
            covered_from = first_date if name == "dblp" else lower_bound
            coverage_start = min(previous.get("coverage_start", covered_from.isoformat()), covered_from.isoformat())
            state["sources"][name] = {"last_success": stamp, "last_attempt": stamp, "status": "ok", "coverage_start": coverage_start}
            report["sources"][name] = {"status": "ok", "received": received, "matched": matched_count,
                                       "new": new_count, "baseline": backfill or not bool(previous.get("last_success")),
                                       "since": lower_bound.isoformat(), "until": upper_bound.isoformat()}
        except Exception as error:
            # Commit nothing from an incomplete source scan; retry the same window later.
            message = str(error)[:700]
            LOG.error("%s failed: %s", name, message)
            state["sources"][name] = {**previous, "last_attempt": stamp, "status": "error", "error": message}
            report["sources"][name] = {"status": "error", "message": message, "received_before_failure": received}
    if not no_enrich and not dry_run:
        report["enrichment_errors"] = enrich(store.papers, config)
    # Enrichment can reveal a second topic; reclassify to keep labels and explicit FL exclusions consistent.
    for identifier, paper in list(store.papers.items()):
        matched = classify(paper, config)
        if matched:
            paper["topics"], paper["matched_terms"] = sorted(matched), matched
        else:
            del store.papers[identifier]
    state["pending"] = sorted(identifier for identifier in pending if identifier in store.papers)
    report["total_papers"] = len(store.papers)
    report["pending"] = len(state["pending"])
    report["failed_sources"] = [name for name, status in report["sources"].items() if status["status"] == "error"]
    if not dry_run:
        # Papers before state: a crash never advances a checkpoint before its data is saved.
        write_json(root / "data" / "papers.json", {"schema_version": 1, "papers": store.papers})
        write_json(root / "data" / "state.json", state)
        write_outputs(root, store.papers, state, report, config)
    if os.getenv("GITHUB_OUTPUT") and not dry_run:
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as handle:
            handle.write(f"pending={report['pending']}\n")
            handle.write(f"failed_sources={','.join(report['failed_sources'])}\n")
    return report
