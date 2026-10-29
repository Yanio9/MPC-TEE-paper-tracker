"""Direct paper tables for the repository README and its complete single-page view."""
from __future__ import annotations

import html
from pathlib import Path

START = "<!-- PAPERS:START -->"
END = "<!-- PAPERS:END -->"
TOPICS = (("mpc", "MPC", ["MPC"]), ("tee", "TEE", ["TEE"]), ("mpc-tee", "MPC + TEE", ["MPC", "TEE"]))


def escaped(value: str) -> str:
    value = html.escape(str(value), quote=False).replace("\n", " ").replace("\r", " ")
    for character in ("\\", "[", "]", "*", "_", "`", "|", "#"):
        value = value.replace(character, "\\" + character)
    return value


def safe_link(url: str) -> str:
    if not url.startswith(("https://", "http://")):
        return ""
    for old, new in (("(", "%28"), (")", "%29"), (" ", "%20"), ("<", "%3C"), (">", "%3E"), ('"', "%22"), ("|", "%7C"), ("\n", "%0A"), ("\r", "%0D")):
        url = url.replace(old, new)
    return url


def paper_date(paper: dict) -> str:
    published = [record for record in paper["records"] if record["source"] == "dblp"]
    records = published or paper["records"]
    return max((str(r.get("published") or r.get("year", "")) for r in records), default="")[:10]


def has_publication_record(paper: dict) -> bool:
    return any(record["source"] == "dblp" for record in paper["records"])


def material_links(paper: dict) -> list[tuple[str, str]]:
    links = []
    seen = set()
    for record in sorted(paper["records"], key=lambda r: (r["source"] != "dblp", r["source"], r["id"])):
        url = safe_link(record.get("url", ""))
        if url and url not in seen:
            label = {"dblp": "论文", "arxiv": "arXiv", "eprint": "ePrint"}.get(record["source"], record["source"])
            links.append((label, url))
            seen.add(url)
    for value in paper.get("code_links", []):
        url = safe_link(value)
        if url and url not in seen:
            links.append(("Code", url))
            seen.add(url)
    return links


def venue_label(paper: dict) -> str:
    venues = sorted({r["venue"] for r in paper["records"] if r["source"] == "dblp"})
    if not venues:
        venues = sorted({{"arxiv": "arXiv", "eprint": "IACR ePrint"}.get(r["source"], r["source"]) for r in paper["records"]})
    return " / ".join(venues)


def paper_groups(papers: dict):
    for published, kind in ((True, "published"), (False, "preprint")):
        for slug, label, topics in TOPICS:
            selected = [(identifier, paper) for identifier, paper in papers.items()
                        if sorted(paper["topics"]) == topics and has_publication_record(paper) == published]
            selected.sort(key=lambda item: (paper_date(item[1]), item[1]["title"], item[0]), reverse=True)
            yield f"{slug}-{kind}", label, published, selected


def render_tables(papers: dict) -> str:
    published_count = sum(has_publication_record(paper) for paper in papers.values())
    lines = [f"共 **{len(papers)}** 篇去重论文：会议/期刊记录 **{published_count}** 篇，"
             f"仅预印本来源 **{len(papers) - published_count}** 篇。", "",
             "预印本单独列出；尚未关联会议/期刊记录，不代表论文一定尚未发表。", "",
             "会议/期刊：[MPC](#mpc-published) · [TEE](#tee-published) · [MPC + TEE](#mpc-tee-published)", "",
             "预印本：[MPC](#mpc-preprint) · [TEE](#tee-preprint) · [MPC + TEE](#mpc-tee-preprint)", ""]
    for slug, label, published, selected in paper_groups(papers):
        kind = "会议与期刊" if published else "预印本"
        lines += [f'<a id="{slug}"></a>', "", f"## {label} · {kind}（{len(selected)}）", "",
                  "| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 资源链接 |", "|---|---|---|---|"]
        for _, paper in selected:
            links = " · ".join(f"[{escaped(label)}]({url})" for label, url in material_links(paper))
            lines.append(f"| {escaped(paper['title'])} | {escaped(venue_label(paper))} | {escaped(paper_date(paper)[:4])} | {links} |")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_library(papers: dict, report: dict) -> str:
    return "# MPC & TEE 论文列表\n\n[仓库首页](README.md) · [运行与收录说明](GUIDE.md)\n\n" + render_tables(papers)


def update_readme(path: Path, table: str) -> None:
    current = path.read_text(encoding="utf-8") if path.exists() else "# MPC & TEE Paper Tracker\n"
    if START in current or END in current:
        if current.count(START) != 1 or current.count(END) != 1 or current.index(START) > current.index(END):
            raise ValueError("Invalid README paper markers; refusing to overwrite hand-written content")
        before, tail = current.split(START, 1)
        _, after = tail.split(END, 1)
        content = before + START + "\n\n" + table.rstrip() + "\n\n" + END + after
    else:
        content = current.rstrip() + "\n\n" + START + "\n\n" + table.rstrip() + "\n\n" + END + "\n"
    path.write_text(content, encoding="utf-8", newline="\n")


STYLE = """
:root{color-scheme:light dark;--bg:#f7f8fa;--surface:#fff;--text:#172033;--muted:#536077;--line:#dce2eb;--accent:#1754a1}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:15px/1.6 system-ui,-apple-system,'Segoe UI',sans-serif}
main{max-width:1440px;margin:auto;padding:36px 24px 80px}h1{font-size:32px;margin:0 0 8px}h2{font-size:22px;margin:40px 0 14px}a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.lead,.note{color:var(--muted)}.links{display:flex;flex-wrap:wrap;gap:18px}.filters{display:flex;flex-wrap:wrap;gap:12px;padding:18px 0;align-items:end}
label{display:flex;flex-direction:column;gap:4px;font-size:13px;color:var(--muted)}input,select{font:inherit;color:var(--text);background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:9px 12px}
input{width:min(420px,85vw)}#result-count{margin-left:auto;color:var(--muted)}.table-wrap{overflow-x:auto;background:var(--surface);border:1px solid var(--line);border-radius:8px}
table{width:100%;border-collapse:collapse;text-align:left}th{background:var(--bg);white-space:nowrap}th,td{padding:13px 16px;vertical-align:top;border-bottom:1px solid var(--line)}tbody tr:last-child td{border-bottom:0}
.title{min-width:300px;width:58%;font-weight:600}.venue{min-width:125px}.year{white-space:nowrap}.materials{min-width:130px}.materials a{display:inline-block;margin:0 9px 5px 0}
details{font-weight:400;color:var(--muted);font-size:14px;margin-top:6px}summary{cursor:pointer}details p{white-space:pre-wrap}tr:target{background:#fff4cb}footer{margin-top:40px;color:var(--muted)}[hidden]{display:none!important}
@media(prefers-color-scheme:dark){:root{--bg:#111827;--surface:#182235;--text:#e3eaf5;--muted:#afbdd1;--line:#334058;--accent:#8ec1ff}tr:target{background:#3f3616}}
@media(max-width:650px){main{padding:24px 12px}h1{font-size:26px}th,td{padding:10px}.title{min-width:240px}#result-count{margin-left:0;width:100%}}
"""

SCRIPT = """
const rows = Array.from(document.querySelectorAll('tbody tr')).map(row => ({row, text: row.textContent.toLocaleLowerCase()}));
const search = document.getElementById('search');
const year = document.getElementById('year');
const topic = document.getElementById('topic');
const kind = document.getElementById('kind');
function filterPapers(){
  const words = search.value.trim().toLocaleLowerCase().split(/\\s+/).filter(Boolean);
  let shown = 0;
  for(const item of rows){
    const row = item.row;
    const matches = words.every(word => item.text.includes(word)) && (!year.value || row.dataset.year === year.value) && (!topic.value || row.dataset.topic === topic.value) && (!kind.value || row.dataset.kind === kind.value);
    row.hidden = !matches;
    if(matches) shown++;
  }
  for(const section of document.querySelectorAll('section')) section.hidden = !section.querySelector('tbody tr:not([hidden])');
  document.getElementById('result-count').textContent = `显示 ${shown} / ${rows.length} 篇`;
}
let pending;
search.addEventListener('input', () => {clearTimeout(pending);pending=setTimeout(filterPapers,150);});
for(const element of [year,topic,kind]) element.addEventListener('change',filterPapers);
"""


def render_site(papers: dict, config: dict) -> str:
    repository = html.escape(config["project"]["repository"], quote=True)
    base = f"https://github.com/{repository}"
    years = sorted({paper_date(paper)[:4] for paper in papers.values()}, reverse=True)
    options = "".join(f'<option value="{html.escape(year, quote=True)}">{html.escape(year)}</option>' for year in years)
    parts = ['<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width,initial-scale=1">',
             '<title>MPC &amp; TEE 论文列表</title>', f'<style>{STYLE}</style></head><body><main>',
             '<h1>MPC &amp; TEE 论文列表</h1>',
             f'<p class="lead">从 2020 年起追踪安全多方计算与可信执行环境。共 {len(papers)} 篇去重论文，全部在本页直接列出。</p>',
             f'<nav class="links"><a href="{base}">GitHub 仓库</a><a href="{base}/blob/main/GUIDE.md">收录与运行说明</a><a href="{base}/blob/main/reports/latest-run.md">最近更新状态</a></nav>',
             '<div class="filters"><label>搜索标题、作者、摘要<input id="search" type="search" placeholder="例如：oblivious transfer、SGX"></label>',
             f'<label>年份<select id="year"><option value="">全部年份</option>{options}</select></label>',
             '<label>方向<select id="topic"><option value="">全部方向</option><option value="mpc">MPC</option><option value="tee">TEE</option><option value="mpc-tee">MPC + TEE</option></select></label>',
             '<label>发表记录<select id="kind"><option value="">全部来源</option><option value="published">会议 / 期刊</option><option value="preprint">仅预印本来源</option></select></label>',
             f'<span id="result-count" role="status">显示 {len(papers)} / {len(papers)} 篇</span></div>',
             '<p class="note">仅预印本来源表示尚未关联会议或期刊记录，不代表论文一定尚未发表。点击“作者与摘要”展开详情。</p>']
    for slug, label, published, selected in paper_groups(papers):
        if not selected:
            continue
        kind = "published" if published else "preprint"
        topic = slug.removesuffix("-" + kind)
        title = f'{label} · {"会议与期刊" if published else "预印本"}（{len(selected)}）'
        parts += [f'<section id="{slug}"><h2>{html.escape(title)}</h2><div class="table-wrap"><table>',
                  '<thead><tr><th scope="col">论文标题</th><th scope="col">会议 / 期刊 / 来源</th><th scope="col">年份</th><th scope="col">资源链接</th></tr></thead><tbody>']
        for identifier, paper in selected:
            year = html.escape(paper_date(paper)[:4], quote=True)
            links = " ".join(f'<a href="{html.escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">{html.escape(label)}</a>' for label, url in material_links(paper))
            authors = html.escape(", ".join(paper.get("authors", [])))
            abstract = html.escape(paper.get("abstract", ""))
            translated = html.escape(paper.get("abstract_cn", ""))
            detail = f'<details><summary>作者与摘要</summary><p>{authors}</p>'
            if abstract:
                detail += f'<p>{abstract}</p>'
            if translated:
                detail += f'<p>{translated}</p>'
            detail += '</details>'
            parts.append(f'<tr id="paper-{html.escape(identifier, quote=True)}" data-year="{year}" data-topic="{topic}" data-kind="{kind}"><td class="title">{html.escape(paper["title"])}{detail}</td><td class="venue">{html.escape(venue_label(paper))}</td><td class="year">{year}</td><td class="materials">{links}</td></tr>')
        parts.append('</tbody></table></div></section>')
    parts += [f'<footer>自动更新 · <a href="{base}/blob/main/LICENSE">MIT License</a> · <a href="{base}/blob/main/GUIDE.md#来源与许可">项目来源与论文许可</a></footer>',
              f'</main><script>{SCRIPT}</script></body></html>']
    return "\n".join(parts) + "\n"
