# 运行与配置

## 文件

- `config.yaml`：领域关键词、匹配规则、来源、会议、时间范围、摘要与通知设置。
- `src/sources.py`：DBLP、arXiv、IACR ePrint 采集与分页；HTTP 超时、限速、重试。
- `src/core.py`：缩写消歧、相关性筛选、跨来源去重、缓存读写。
- `src/runner.py`：独立来源扫描、成功时间、首轮基线、待发送队列。
- `src/enrichment.py`：可选 Crossref 摘要补全与 Qwen 中文翻译。
- `src/catalog.py`：按会议/期刊名称生成直接论文表格及完整单页网页，组内按年份倒序；MPC / TEE / MPC + TEE 作为方向标签与筛选项。
- `src/output.py`：更新 README 自动生成区、完整论文列表、网页和运行报告。
- `scripts/publish_digest.py`：只向配置指定的当前仓库发送 Issue，并检测已发送的论文 ID。
- `data/papers.json`：符合收录规则的去重论文；当前仅保留有 DBLP 发表记录的论文。`records` 保留已关联预印本的元数据与链接，`aliases` 记录旧标题和 ID。
- `data/state.json`：各来源成功时间、错误状态、待发送论文 ID。
- `README.md`：仓库首页直接展示论文表格；每日仅替换 `<!-- PAPERS:START -->` 与 `<!-- PAPERS:END -->` 之间的内容，保留其余手写说明。
- `PAPERS.md`：同一批全部论文的直接列表，不再按页数分流。
- `GUIDE.md`：完整的使用、收录范围与来源许可说明。
- `docs/index.html`：全部收录论文的独立单页网页，保留作者与摘要，可按会议/期刊、关键词、年份、方向筛选。无需外部脚本或服务。
- `reports/`：最近运行摘要、结构化报告和待发送摘要。

## 扫描范围

当前 `tracking.publication_only: true`，只收录具有 DBLP 会议/期刊记录的论文。arXiv 与 ePrint 的 `enabled` 均为 `false`；即使误启用这两个开关，正式发表模式仍会阻止独立预印本扫描。已有缓存和待发送队列同步按此规则清理，展示生成器和通知发布器也会再次筛选。正式发表论文的预印本链接、摘要和去重标识保留。

该模式清除两个预印本来源的扫描检查点，避免移除旧条目后仍声称完整保留了历史覆盖。以后若关闭 `publication_only` 并重新启用预印本来源，将从 2020 年建立安静基线。DBLP 检查点和正式发表论文的通知状态保留。

DBLP 默认使用官方 SPARQL API（`https://sparql.dblp.org/sparql`），完整扫描配置中的关键词、年份范围与会议/期刊集合。`dblp_terms` 中空格表示 AND、`|` 表示 OR、`$` 表示词尾精确匹配；这些条件被转换为标题候选筛选，再经过本地相关性规则确认。每页先选定 500 个独立论文 ID，再获取作者和链接，避免多作者导致分页截断。保留官方搜索 API 后端（`sources.dblp.backend: search`），但它当前可能返回反爬验证页；程序不会绕过验证。原来的 FL 缓存没有导入。

可选的 arXiv 采集器（当前关闭）按标题/摘要检索和最近更新排序，直到翻过时间边界。每篇保留最早提交时间和版本更新时间；版本 ID 去除 `vN` 后去重。可选的 IACR ePrint 采集器（当前关闭）使用 OAI-PMH `from` / `until` 和 `resumptionToken`，可以回补较长中断期间的记录。超出页数上限会报错而非静默截断。

所有来源采用固定的 `tracking.start_year: 2020`，不会随当前年份滚动。预印本首次从 2020-01-01 回补，之后从该来源上次成功日期减去 3 天开始，缓解索引与时区边界延迟；停机多日后不会仅检查最近一天。首次成功扫描某来源不发送历史条目；显式 `--since` 历史回补也不将补录条目加入通知队列。

`python -m src.main --refresh` 或手动工作流的 `refresh: true` 会重新访问已启用且符合收录模式的来源（当前仅 DBLP），跳过当天成功扫描的缓存判断。默认扫描仍保留每天一次的限制。立即刷新不重置历史起点与成功时间，不提高请求频率，不改变去重与通知规则；只有完整扫描成功才推进该来源状态。

arXiv 历史回补按提交年份拆分查询，每页最多 500 条；正常增量查询每页 100 条，按更新时间停止。只收录首次提交年份在配置范围内的预印本。ePrint 在同一天已完成近期扫描时，历史回补结束于最近扫描重叠窗口之前，避免重新刷新近期窗口。`coverage_start` 记录已完成的历史起点，同日重复提交已覆盖的回补请求会跳过。

## 状态与故障

单个来源的扫描在内存中暂存，所有分页成功后才合并到持久化论文库并推进成功时间。失败来源保留旧数据与旧时间；其他已启用来源继续运行。HTTP 429/5xx 使用退避和 Retry-After，DBLP 保持 6 秒加随机间隔，可选 arXiv/ePrint 请求间隔至少约 3 秒。HTML/反爬页作为来源错误处理，不尝试绕过。

写入顺序是论文、状态、展示文件。自动工作流先提交待发送队列，再发 Issue，再提交发送结果。若发 Issue 后提交失败，下次从 Issue 中的论文标记恢复，避免重复提醒。仅将论文标题等外部文本作为数据处理，不拼接进 shell 指令。

所有推送均为普通 `git push origin HEAD:main`。冲突时工作流失败，保留报告供检查，不强制覆盖远端。并发运行通过 Actions concurrency 排队。

## 配置示例

完全排除明确提到联邦学习的论文：

```yaml
tracking:
  exclude_federated_learning: true
```

固定的发表年份起点：

```yaml
tracking:
  start_year: 2020
```

显式历史回补（安静补录，不发送历史论文提醒）：

```bash
python -m src.main --since 2020-01-01
```

在独立目录验证，不修改正式缓存：

```bash
python -m src.main --sources dblp --output-dir .local-preview --no-enrich
```

若要从零开始，将 `data/papers.json` 和 `data/state.json` 备份后一起移出目录，再运行。只移除一个文件会造成论文数据与通知状态不一致，不推荐。

## 通知及可见性

仓库为公开仓库，提交的论文目录、摘要、状态与 Issue 也公开。`DASHSCOPE_API_KEY` 仅通过 GitHub Actions Secret 或本地环境变量提供；不提交 `.env`。程序不读取原作者邮箱、不向原作者仓库写入。改仓库名时需同步 `project.repository` 和 `watch.yml` 的仓库校验条件。

GitHub cron 使用 UTC，`17 1 * * *` 对应北京时间 09:17。公开仓库长时间没有活动可能被 GitHub 暂停定时工作流，可在 Actions 中重新启用。实际执行情况以最近运行报告和 Actions 结果为准。

## 首页与完整网页

按用户要求采用 Awesome-FL 的直接论文列表样式。GitHub 对 README 超过 500 KiB 的内容会截断，因此首页同时链接完整单页，生成器不会因此省略任何论文。旧 `papers/` 分页文件由生成器按严格文件名规则清理，其他笔记保留。

GitHub Pages 使用自定义 Actions 工作流，发布目录为 `docs/`。`pages.yml` 既监听人工提交的页面变化，也通过 `workflow_run` 监听论文抓取完成，保证 GITHUB_TOKEN 提交的数据更新也会部署网页。部署仅使用主分支内容，不执行论文元数据中的代码。
