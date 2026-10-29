"""Direct paper lists, complete single-page website, digests and source reports."""
from __future__ import annotations

import html
import re
from collections import Counter
from pathlib import Path

from .core import write_json, publication_allowed
from .catalog import (escaped, safe_link, paper_date, has_publication_record,
                      render_library, render_tables, render_site, update_readme)


def paper_lines(paper: dict, include_abstract: bool = False) -> list[str]:
    links = []
    for record in paper["records"]:
        url = safe_link(record.get("url", ""))
        if url:
            label = record["venue"] if record["source"] == "dblp" else {"arxiv": "arXiv", "eprint": "IACR ePrint"}[record["source"]]
            links.append(f"[{escaped(label)}]({url})")
    links += [f"[Code]({safe_link(url)})" for url in paper.get("code_links", []) if safe_link(url)]
    status = "含会议/期刊记录" if has_publication_record(paper) else "仅预印本来源"
    lines = [f"- **{escaped(paper['title'])}**", f"  {paper_date(paper)} · {' / '.join(paper['topics'])} · {status} · {' · '.join(links)}"]
    if paper.get("authors"):
        lines.append("  " + escaped(", ".join(paper["authors"])))
    if include_abstract and paper.get("abstract"):
        lines += ["", "  <details><summary>摘要 / Abstract</summary>", "", "  " + html.escape(paper["abstract"]), ""]
        if paper.get("abstract_cn"):
            lines += ["  " + html.escape(paper["abstract_cn"]), ""]
        evidence = "; ".join(f"{topic}: {', '.join(words)}" for topic, words in paper.get("matched_terms", {}).items())
        lines += ["  匹配依据：" + escaped(evidence), "", "  </details>"]
    lines.append("")
    return lines


def render_digest(papers: dict, identifiers: list[str], repository: str, limit: int) -> str:
    lines = [f"本次新增 **{len(identifiers)}** 篇 MPC / TEE 相关论文。", "",
             f"[完整论文目录](https://github.com/{repository}/blob/main/PAPERS.md) · "
             f"[来源状态](https://github.com/{repository}/blob/main/reports/latest-run.md)", ""]
    for identifier in identifiers[:limit]:
        block = paper_lines(papers[identifier])
        if len("\n".join(lines + block)) > 45000:
            lines += ["其余条目请查看完整目录。", ""]
            break
        lines += block
    if len(identifiers) > limit:
        lines += [f"其余 {len(identifiers) - limit} 篇请查看完整目录。", ""]
    return "\n".join(lines)


def write_outputs(root: Path, papers: dict, state: dict, report: dict, config: dict) -> None:
    papers = {identifier: paper for identifier, paper in papers.items() if publication_allowed(paper, config)}
    (root / "reports").mkdir(parents=True, exist_ok=True)
    update_readme(root / "README.md", render_tables(papers, config))
    (root / "PAPERS.md").write_text(render_library(papers, report, config), encoding="utf-8", newline="\n")
    site = root / "docs"
    site.mkdir(parents=True, exist_ok=True)
    (site / "index.html").write_text(render_site(papers, config), encoding="utf-8", newline="\n")
    (site / ".nojekyll").write_text("", encoding="utf-8")
    # Remove only obsolete generated pagination files, preserving personal notes.
    archive = root / "papers"
    if archive.exists():
        for path in archive.glob("*.md"):
            if re.fullmatch(r"(?:\d{4}|unknown)-(?:mpc|tee|mpc-tee)(?:-(?:published|preprint))?-\d+\.md", path.name):
                if not path.resolve().is_relative_to(archive.resolve()):
                    raise ValueError("Generated archive cleanup escaped the papers directory")
                path.unlink()
    lines = ["# 最近运行状态", "", f"运行时间：{report['started_at']}", "",
             "| 来源 | 状态 | 相关记录 | 说明 |", "|---|---|---:|---|"]
    for source, status in report["sources"].items():
        lines.append(f"| {source} | {status['status']} | {status.get('matched', 0)} | {escaped(status.get('message', ''))} |")
    counts = Counter(topic for paper in papers.values() for topic in paper["topics"])
    identifiers = [identifier for identifier in state.get("pending", []) if identifier in papers]
    lines += ["", f"去重论文：{len(papers)}；MPC 标签：{counts['MPC']}；TEE 标签：{counts['TEE']}。", "",
              f"待发送新增论文：{len(identifiers)}。", "",
              "首次成功扫描各来源时建立基线；扫描失败不会推进该来源的成功时间。", ""]
    if report.get("enrichment_errors"):
        lines += ["摘要补全/翻译未完成：", ""] + [f"- {escaped(x)}" for x in report["enrichment_errors"]] + [""]
    (root / "reports" / "latest-run.md").write_text("\n".join(lines), encoding="utf-8")
    write_json(root / "reports" / "latest-run.json", report)
    digest = render_digest(papers, identifiers, config["project"]["repository"], config["notifications"]["max_papers_per_issue"])
    (root / "reports" / "pending-digest.md").write_text(digest, encoding="utf-8")
