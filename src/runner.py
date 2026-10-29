"""Run every enabled source independently; keep source checkpoints transactional."""
from __future__ import annotations

import copy
import logging
import os
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import yaml

from .core import PaperStore, classify, read_json, write_json
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
    for key in ("years_back", "years_ahead", "overlap_days", "initial_lookback_days"):
        if not isinstance(config["tracking"][key], int) or config["tracking"][key] < 0:
            raise ValueError(f"tracking.{key} must be a nonnegative integer")
    return config


def run(root: Path, config: dict, selected: list[str] | None = None, since: date | None = None,
        dry_run: bool = False, now: datetime | None = None, collectors=None, client_factory=HttpClient,
        no_enrich: bool = False) -> dict:
    now = now or datetime.now(timezone.utc)
    stamp = now.isoformat(timespec="seconds")
    today = now.date()
    cache = read_json(root / "data" / "papers.json", {"schema_version": 1, "papers": {}})
    state = read_json(root / "data" / "state.json", {"schema_version": 1, "sources": {}, "pending": []})
    if cache.get("schema_version") != 1 or state.get("schema_version") != 1:
        raise ValueError("Unsupported cache schema; refusing to overwrite")
    store = PaperStore(cache["papers"])
    pending = set(state.get("pending", []))
    report = {"started_at": stamp, "sources": {}, "enrichment_errors": []}
    collectors = collectors or COLLECTORS
    # Reapply user exclusions after config edits, without migrating unrelated FL cache.
    for identifier, paper in list(store.papers.items()):
        matched = classify(paper, config)
        if not matched:
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
        if previous.get("last_success", "")[:10] == today.isoformat() and since is None:
            report["sources"][name] = {"status": "cached", "message": "Already completed today (UTC)"}
            continue
        if name == "eprint" and previous.get("last_success", "")[:10] == today.isoformat():
            report["sources"][name] = {"status": "cached", "message": "ePrint is refreshed at most once per day"}
            continue
        lower_bound = since or (date.fromisoformat(previous["last_success"][:10]) - timedelta(days=config["tracking"]["overlap_days"])
                                if previous.get("last_success") else today - timedelta(days=config["tracking"]["initial_lookback_days"]))
        staged = PaperStore(store.papers)
        staged_pending = set(pending)
        received = matched_count = new_count = 0
        LOG.info("Scanning %s since %s", name, lower_bound)
        try:
            client = client_factory(name, source_cfg["interval_seconds"], config["project"].get("contact_email", ""))
            for paper in collectors[name](config, client, today, lower_bound):
                received += 1
                if not paper.get("title") or not paper.get("records"):
                    raise ValueError(f"{name} returned an incomplete record")
                if name == "dblp":
                    year = int(paper["records"][0]["year"])
                    if not today.year - config["tracking"]["years_back"] <= year <= today.year + config["tracking"]["years_ahead"]:
                        continue
                matched = classify(paper, config)
                if not matched:
                    continue
                paper["topics"], paper["matched_terms"] = sorted(matched), matched
                matched_count += 1
                identifier, is_new = staged.add(paper, stamp)
                new_count += int(is_new)
                if is_new and (previous.get("last_success") or config["notifications"]["notify_on_first_run"]):
                    staged_pending.add(identifier)
            store = staged
            pending = {store.resolve(identifier) for identifier in staged_pending}
            state["sources"][name] = {"last_success": stamp, "last_attempt": stamp, "status": "ok"}
            report["sources"][name] = {"status": "ok", "received": received, "matched": matched_count,
                                       "new": new_count, "baseline": not bool(previous.get("last_success")), "since": lower_bound.isoformat()}
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
