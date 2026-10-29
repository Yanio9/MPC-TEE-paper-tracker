"""Readable paper library, daily digest and source-health report."""
from __future__ import annotations

import html
from collections import Counter
from pathlib import Path

from .core import write_json


def escaped(value: str) -> str:
    value = html.escape(str(value), quote=False).replace("\n", " ")
    for character in ("\\", "[", "]", "*", "_", "`", "|", "#"):
        value = value.replace(character, "\\" + character)
    return value


def safe_link(url: str) -> str:
    if not url.startswith(("https://", "http://")):
        return ""
    return url.replace("(", "%28").replace(")", "%29").replace(" ", "%20").replace("<", "%3C").replace(">", "%3E").replace('"', "%22")


def paper_date(paper: dict) -> str:
    return max((r.get("published") or r.get("year", "") for r in paper["records"]), default="")[:10]


def paper_lines(paper: dict, include_abstract: bool = False) -> list[str]:
    links = []
    for record in paper["records"]:
        url = safe_link(record.get("url", ""))
        if url:
            label = record["venue"] if record["source"] == "dblp" else {"arxiv": "arXiv", "eprint": "IACR ePrint"}[record["source"]]
            links.append(f"[{escaped(label)}]({url})")
    links += [f"[Code]({safe_link(url)})" for url in paper.get("code_links", []) if safe_link(url)]
    lines = [f"- **{escaped(paper['title'])}**", f"  {paper_date(paper)} · {' / '.join(paper['topics'])} · {' · '.join(links)}"]
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


def render_library(papers: dict, report: dict) -> str:
    lines = ["# MPC & TEE 论文目录", "", "覆盖安全多方计算、相关密码协议、可信执行环境及机密计算。", "",
             "[最近运行状态](reports/latest-run.md) · [项目说明](README.md)", "",
             "自动筛选结果，建议按匹配依据人工复核；arXiv 和 IACR ePrint 是预印本来源。", "",
             f"共 **{len(papers)}** 篇去重论文。", ""]
    groups = [("MPC + TEE", lambda p: "MPC" in p["topics"] and "TEE" in p["topics"]),
              ("MPC", lambda p: p["topics"] == ["MPC"]), ("TEE", lambda p: p["topics"] == ["TEE"])]
    for label, predicate in groups:
        selected = sorted((p for p in papers.values() if predicate(p)), key=lambda p: (paper_date(p), p["title"]), reverse=True)
        lines += [f"## {label}（{len(selected)}）", ""]
        previous_year = None
        for paper in selected:
            year = paper_date(paper)[:4] or "Unknown year"
            if year != previous_year:
                lines += [f"### {year}", ""]
                previous_year = year
            lines += paper_lines(paper, include_abstract=True)
    return "\n".join(lines).rstrip() + "\n"


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
    (root / "reports").mkdir(parents=True, exist_ok=True)
    (root / "PAPERS.md").write_text(render_library(papers, report), encoding="utf-8")
    lines = ["# 最近运行状态", "", f"运行时间：{report['started_at']}", "",
             "| 来源 | 状态 | 相关记录 | 说明 |", "|---|---|---:|---|"]
    for source, status in report["sources"].items():
        lines.append(f"| {source} | {status['status']} | {status.get('matched', 0)} | {escaped(status.get('message', ''))} |")
    counts = Counter(topic for paper in papers.values() for topic in paper["topics"])
    lines += ["", f"去重论文：{len(papers)}；MPC 标签：{counts['MPC']}；TEE 标签：{counts['TEE']}。", "",
              f"待发送新增论文：{len(state.get('pending', []))}。", "",
              "首次成功扫描各来源时建立基线；扫描失败不会推进该来源的成功时间。", ""]
    if report.get("enrichment_errors"):
        lines += ["摘要补全/翻译未完成：", ""] + [f"- {escaped(x)}" for x in report["enrichment_errors"]] + [""]
    (root / "reports" / "latest-run.md").write_text("\n".join(lines), encoding="utf-8")
    write_json(root / "reports" / "latest-run.json", report)
    identifiers = [identifier for identifier in state.get("pending", []) if identifier in papers]
    digest = render_digest(papers, identifiers, config["project"]["repository"], config["notifications"]["max_papers_per_issue"])
    (root / "reports" / "pending-digest.md").write_text(digest, encoding="utf-8")
