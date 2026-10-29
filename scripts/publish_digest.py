"""Publish the durable pending queue to this repository only; retries are idempotent."""
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.core import read_json, write_json, publication_allowed
from src.output import render_digest
from src.runner import load_config


def publish(root: Path, config: dict, session) -> int:
    repository = config["project"]["repository"]
    if os.getenv("GITHUB_REPOSITORY") != repository:
        raise RuntimeError(f"Refusing to publish outside configured repository {repository}")
    state_path = root / "data" / "state.json"
    state = read_json(state_path, {"schema_version": 1, "sources": {}, "pending": []})
    papers = read_json(root / "data" / "papers.json", {"papers": {}})["papers"]
    pending = [identifier for identifier in state.get("pending", []) if identifier in papers and publication_allowed(papers[identifier], config)]
    if not pending:
        if state.get("pending"):
            state["pending"] = []
            write_json(state_path, state)
        print("No new papers to notify.")
        return 0
    base = f"https://api.github.com/repos/{repository}/issues"
    sent = set()
    page = 1
    # A previously created Issue may have survived a failed state commit. Recover its paper IDs.
    while True:
        response = session.get(base, params={"state": "all", "per_page": 100, "page": page}, timeout=30)
        response.raise_for_status()
        issues = response.json()
        for issue in issues:
            if "pull_request" in issue:
                continue
            for marker in re.findall(r"<!-- mpc-tee-papers:([a-f0-9,]+) -->", issue.get("body") or ""):
                sent.update(marker.split(","))
        if len(issues) < 100:
            break
        page += 1
    remaining = [identifier for identifier in pending if identifier not in sent]
    batch = remaining[:500]
    if batch:
        digest = render_digest(papers, batch, repository, config["notifications"]["max_papers_per_issue"])
        marker = "\n\n<!-- mpc-tee-papers:" + ",".join(batch) + " -->"
        day = datetime.now(ZoneInfo(config["project"]["timezone"])).strftime("%Y-%m-%d")
        payload = {"title": f"MPC / TEE 论文更新 · {day} · +{len(batch)}", "body": digest + marker}
        response = session.post(base, json=payload, timeout=30)
        response.raise_for_status()
        print("Published " + response.json()["html_url"])
        sent.update(batch)
    state["pending"] = [identifier for identifier in pending if identifier not in sent]
    write_json(state_path, state)
    return len(batch)


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    session = requests.Session()
    session.headers.update({"Authorization": "Bearer " + os.environ["GH_TOKEN"], "Accept": "application/vnd.github+json",
                            "X-GitHub-Api-Version": "2022-11-28"})
    publish(root, load_config(root / "config.yaml"), session)
