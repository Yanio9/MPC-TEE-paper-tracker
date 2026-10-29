"""Readable paper library, daily digest and source-health report."""
from __future__ import annotations

import html
import re
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


def has_publication_record(paper: dict) -> bool:
    return any(record["source"] == "dblp" for record in paper["records"])


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


def render_library(papers: dict, report: dict) -> str:
    lines = ["# MPC & TEE 论文目录", "", "覆盖安全多方计算、相关密码协议、可信执行环境及机密计算。", "",
             "[最近运行状态](reports/latest-run.md) · [项目说明](README.md)", "",
             "自动筛选结果，建议按匹配依据人工复核；仅预印本来源表示尚未关联正式发表记录，不代表论文一定尚未发表。", "",
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


def archive_pages(selected: list[dict], prefix: str, title: str) -> tuple[dict[str, str], str]:
    chunks, current, current_bytes = [], [], 0
    for paper in selected:
        block = "\n".join(paper_lines(paper, include_abstract=True))
        size = len(block.encode("utf-8"))
        if current and (current_bytes + size > 200_000 or len(current) >= 150):
            chunks.append(current)
            current, current_bytes = [], 0
        current.append(block)
        current_bytes += size
    if current:
        chunks.append(current)
    files = {}
    names = [f"{prefix}-{page:02d}.md" for page in range(1, len(chunks) + 1)]
    for page, blocks in enumerate(chunks):
        navigation = ["[总目录](../PAPERS.md)"]
        if page:
            navigation.append(f"[上一页]({names[page - 1]})")
        if page + 1 < len(chunks):
            navigation.append(f"[下一页]({names[page + 1]})")
        heading = [f"# {title} · 第 {page + 1}/{len(chunks)} 页", "", " · ".join(navigation), ""]
        files[names[page]] = "\n".join(heading + blocks).rstrip() + "\n"
    links = " · ".join(f"[第 {page + 1} 页](papers/{name})" for page, name in enumerate(names))
    return files, f"{len(selected)} 篇" + ("：" + links if links else "")


def library_files(papers: dict, report: dict) -> tuple[str, dict[str, str]]:
    """Keep large historical libraries readable as bounded Markdown pages."""
    full = render_library(papers, report)
    if len(full.encode("utf-8")) <= 400_000:
        return full, {}
    groups = {}
    labels = {"mpc-tee": "MPC + TEE", "mpc": "MPC", "tee": "TEE"}
    for paper in papers.values():
        year = paper_date(paper)[:4]
        year = year if re.fullmatch(r"\d{4}", year) else "unknown"
        topic = "mpc-tee" if len(paper["topics"]) == 2 else paper["topics"][0].lower()
        groups.setdefault((year, topic), []).append(paper)
    index = ["# MPC & TEE 论文目录", "", f"共 **{len(papers)}** 篇去重论文，按年份和方向分页保存摘要与来源链接。", "",
             "[最近运行状态](reports/latest-run.md) · [项目说明与收录范围](README.md)", "",
             "仅预印本来源表示尚未关联正式发表记录，不代表论文一定尚未发表；每篇论文保留全部已关联的来源。", "",
             f"含会议/期刊记录：**{sum(has_publication_record(paper) for paper in papers.values())}** 篇；"
             f"仅预印本来源：**{sum(not has_publication_record(paper) for paper in papers.values())}** 篇。", "",
             "| 年份 | 方向 | 篇数 | 含会议/期刊记录 | 仅预印本来源 |", "|---|---|---:|---|---|"]
    files = {}
    for (year, topic), selected in sorted(groups.items(), key=lambda item: (-int(item[0][0]) if item[0][0].isdigit() else 0, list(labels).index(item[0][1]))):
        selected.sort(key=lambda p: (paper_date(p), p["title"]), reverse=True)
        columns = []
        for published, suffix, label in ((True, "published", "含会议/期刊记录"), (False, "preprint", "仅预印本来源")):
            subset = [paper for paper in selected if has_publication_record(paper) == published]
            pages, links = archive_pages(subset, f"{year}-{topic}-{suffix}", f"{year} · {labels[topic]} · {label}")
            files.update(pages)
            columns.append(links)
        index.append(f"| {year} | {labels[topic]} | {len(selected)} | {columns[0]} | {columns[1]} |")
    return "\n".join(index) + "\n", files


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
    index, pages = library_files(papers, report)
    archive = root / "papers"
    archive.mkdir(parents=True, exist_ok=True)
    for name, content in pages.items():
        (archive / name).write_text(content, encoding="utf-8")
    for path in archive.glob("*.md"):
        if path.name not in pages and re.fullmatch(r"(?:\d{4}|unknown)-(?:mpc|tee|mpc-tee)(?:-(?:published|preprint))?-\d+\.md", path.name):
            if not path.resolve().is_relative_to(archive.resolve()):
                raise ValueError("Generated archive cleanup escaped the papers directory")
            path.unlink()
    (root / "PAPERS.md").write_text(index, encoding="utf-8")
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
