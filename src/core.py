"""Topic matching and persistent, cross-source paper identity."""
from __future__ import annotations

import copy
import hashlib
import html
import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlparse


def year_bounds(config: dict, today) -> tuple[int, int]:
    tracking = config["tracking"]
    first = tracking["start_year"] if "start_year" in tracking else today.year - tracking.get("years_back", 3)
    return first, today.year + tracking["years_ahead"]


def in_year_range(paper: dict, first: int, last: int) -> bool:
    return any(str(record.get("year", "")).isdigit() and first <= int(record["year"]) <= last
               for record in paper.get("records", []))


def has_publication_record(paper: dict) -> bool:
    return any(record["source"] == "dblp" for record in paper.get("records", []))


def publication_allowed(paper: dict, config: dict) -> bool:
    return not config.get("tracking", {}).get("publication_only", False) or has_publication_record(paper)


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]*>", " ", str(value or "")))).strip()


def normalized_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", clean_text(value)).casefold()
    return re.sub(r"[^\w]+", " ", value).strip()


def classify(paper: dict, config: dict) -> dict[str, list[str]]:
    """Require an explicit topic phrase or a contextualized acronym, never FL alone."""
    text = normalized_text(paper.get("title", "") + " " + paper.get("abstract", ""))
    if config["tracking"].get("exclude_federated_learning") and re.search(r"\bfederated\s+(?:machine\s+)?learning\b", text):
        return {}
    matches = {}
    for topic, rules in config["topics"].items():
        evidence = sorted({m.group(0) for pattern in rules["patterns"] for m in re.finditer(pattern, text)})
        if not evidence and not any(normalized_text(x) in text for x in rules.get("acronym_exclusions", [])):
            acronym = re.search(rules["acronym_pattern"], text)
            if acronym and re.search(rules["context_pattern"], text):
                evidence.append(acronym.group(0) + " (context)")
        if evidence:
            matches[topic] = evidence
    return matches


def canonical_doi(value: str) -> str:
    value = unquote(str(value or "")).strip().lower()
    value = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", value)
    return value.rstrip(" .") if re.match(r"^10\.\d{4,9}/\S+$", value) else ""


def canonical_arxiv(value: str) -> str:
    value = re.sub(r"^https?://(?:export\.)?arxiv\.org/(?:abs|pdf)/", "", value)
    value = re.sub(r"\.pdf$", "", value)
    return re.sub(r"v\d+$", "", value).strip()


def identity_keys(paper: dict) -> set[str]:
    keys = set(paper.get("aliases", []))
    title = normalized_text(paper.get("title", ""))
    if title:
        keys.add("title:" + title)
    for record in paper.get("records", []):
        if record.get("id"):
            identifier = canonical_arxiv(record["id"]) if record["source"] == "arxiv" else record["id"]
            keys.add(record["source"] + ":" + identifier)
        doi = canonical_doi(record.get("doi", ""))
        if doi:
            keys.add("doi:" + doi)
            if doi.startswith("10.48550/arxiv."):
                keys.add("arxiv:" + canonical_arxiv(doi.split("arxiv.", 1)[1]))
        for field in ("url", "pdf_url"):
            value = record.get(field, "")
            parsed = urlparse(value)
            if parsed.hostname in {"arxiv.org", "export.arxiv.org"} and re.match(r"^/(abs|pdf)/", parsed.path):
                keys.add("arxiv:" + canonical_arxiv(value))
            elif parsed.hostname == "eprint.iacr.org":
                match = re.match(r"/(\d{4}/\d+)", parsed.path)
                if match:
                    keys.add("eprint:" + match.group(1))
            elif parsed.hostname in {"doi.org", "dx.doi.org"}:
                doi = canonical_doi(value)
                if doi:
                    keys.add("doi:" + doi)
    return keys


def extract_code_links(abstract: str) -> list[str]:
    return sorted({url.rstrip(".,;:)") for url in re.findall(r"https://github\.com/[\w.-]+/[\w.-]+", abstract)})


class PaperStore:
    def __init__(self, papers: dict | None = None):
        self.papers = copy.deepcopy(papers or {})
        self.index = {}
        self.redirects = {}
        for identifier, paper in self.papers.items():
            for key in identity_keys(paper):
                self.index[key] = identifier

    def resolve(self, identifier: str) -> str:
        while identifier in self.redirects:
            identifier = self.redirects[identifier]
        return identifier

    @staticmethod
    def merge(target: dict, incoming: dict) -> None:
        target["aliases"] = sorted(identity_keys(target) | identity_keys(incoming))
        # Keep the newest metadata for each stable source ID; never erase existing fields.
        records = {(r["source"], r["id"]): r for r in target.get("records", [])}
        for new in incoming.get("records", []):
            key = (new["source"], new["id"])
            old = records.get(key, {})
            if new.get("updated", "") >= old.get("updated", ""):
                records[key] = {**old, **{k: v for k, v in new.items() if v}}
        target["records"] = sorted(records.values(), key=lambda r: (r["source"], r["id"]))
        target["authors"] = list(dict.fromkeys(target.get("authors", []) + incoming.get("authors", [])))
        target["topics"] = sorted(set(target.get("topics", [])) | set(incoming.get("topics", [])))
        for topic, evidence in incoming.get("matched_terms", {}).items():
            target.setdefault("matched_terms", {})[topic] = sorted(set(target.get("matched_terms", {}).get(topic, [])) | set(evidence))
        if incoming.get("abstract"):
            old_date = target.get("abstract_updated", "")
            new_date = incoming.get("abstract_updated", "")
            if not target.get("abstract") or new_date >= old_date:
                if target.get("abstract") != incoming["abstract"]:
                    target.pop("abstract_cn", None)
                target["abstract"] = incoming["abstract"]
                target["abstract_updated"] = new_date
        if incoming.get("abstract_cn") and not target.get("abstract_cn"):
            target["abstract_cn"] = incoming["abstract_cn"]
        target["code_links"] = sorted(set(target.get("code_links", [])) | set(incoming.get("code_links", [])))
        for field in ("first_seen",):
            values = [x for x in [target.get(field), incoming.get(field)] if x]
            if values:
                target[field] = min(values)
        target["last_seen"] = max(target.get("last_seen", ""), incoming.get("last_seen", ""))

    def add(self, paper: dict, now: str) -> tuple[str, bool]:
        paper = copy.deepcopy(paper)
        for record in paper.get("records", []):
            if record["source"] == "arxiv":
                record["id"] = canonical_arxiv(record["id"])
        paper.setdefault("first_seen", now)
        paper["last_seen"] = now
        paper["code_links"] = extract_code_links(paper.get("abstract", ""))
        keys = identity_keys(paper)
        existing = sorted({self.resolve(self.index[k]) for k in keys if k in self.index})
        is_new = not existing
        if existing:
            identifier = existing[0]
            target = self.papers[identifier]
            for duplicate in existing[1:]:
                self.merge(target, self.papers.pop(duplicate))
                self.redirects[duplicate] = identifier
            self.merge(target, paper)
            # A newer version can change the title without becoming a new paper.
            target["title"] = paper["title"]
        else:
            identifier = hashlib.sha256(sorted(keys)[0].encode("utf-8")).hexdigest()[:20]
            self.papers[identifier] = paper
            paper["aliases"] = sorted(keys)
        for key in identity_keys(self.papers[identifier]):
            self.index[key] = identifier
        return identifier, is_new


def read_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return copy.deepcopy(default)
    with path.open(encoding="utf-8") as handle:
        result = json.load(handle)
    if not isinstance(result, dict):
        raise ValueError(f"Invalid cache object: {path}")
    return result


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(path)
