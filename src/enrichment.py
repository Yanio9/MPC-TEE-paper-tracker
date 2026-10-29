"""Optional abstract enrichment and translation; tracking works without paid keys."""
import logging
import os
import time
from datetime import datetime, timedelta, timezone
from urllib.parse import quote

import requests

from .core import canonical_doi, clean_text, extract_code_links
from .sources import HttpClient

LOG = logging.getLogger(__name__)


def enrich(papers: dict, config: dict) -> list[str]:
    cfg = config.get("enrichment", {})
    errors = []
    client = HttpClient("crossref", 3.1, config["project"].get("contact_email", ""))
    if cfg.get("fetch_missing_abstracts"):
        attempted = 0
        now = datetime.now(timezone.utc)
        retry_before = (now - timedelta(days=7)).isoformat()
        for paper in sorted(papers.values(), key=lambda p: p.get("first_seen", ""), reverse=True):
            if paper.get("abstract") or attempted >= cfg.get("max_abstracts_per_run", 20):
                continue
            if paper.get("abstract_checked_at", "") > retry_before:
                continue
            doi = next((canonical_doi(r.get("doi", "")) for r in paper["records"] if canonical_doi(r.get("doi", ""))), "")
            if not doi:
                continue
            attempted += 1
            paper["abstract_checked_at"] = now.isoformat()
            try:
                params = {"mailto": config["project"]["contact_email"]} if config["project"].get("contact_email") else {}
                data = client.get("https://api.crossref.org/works/" + quote(doi, safe=""), params).json()
                paper["abstract"] = clean_text(data.get("message", {}).get("abstract", ""))
                paper["code_links"] = sorted(set(paper.get("code_links", [])) | set(extract_code_links(paper["abstract"])))
            except Exception as error:
                LOG.warning("Crossref enrichment failed: %s", error)
                errors.append(f"Crossref {doi}: {type(error).__name__}")
    api_key = os.getenv("DASHSCOPE_API_KEY", "")
    if cfg.get("translate_to_chinese") and api_key:
        attempted = 0
        for paper in sorted(papers.values(), key=lambda p: p.get("first_seen", ""), reverse=True):
            if not paper.get("abstract") or paper.get("abstract_cn") or attempted >= cfg.get("max_translations_per_run", 20):
                continue
            attempted += 1
            try:
                response = requests.post(cfg["translation_url"], headers={"Authorization": "Bearer " + api_key},
                                         json={"model": cfg["translation_model"], "messages": [{"role": "user", "content": paper["abstract"]}],
                                               "translation_options": {"source_lang": "English", "target_lang": "Chinese"}}, timeout=45)
                response.raise_for_status()
                paper["abstract_cn"] = response.json()["choices"][0]["message"]["content"].strip()
                time.sleep(1)
            except Exception as error:
                errors.append("Translation: " + type(error).__name__)
                LOG.warning("Translation failed; stopping translations this run (%s)", type(error).__name__)
                break
    return errors
