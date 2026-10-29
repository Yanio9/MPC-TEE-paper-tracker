# MPC & TEE Paper Tracker

Yanio9 的个人论文追踪器：**安全多方计算（MPC）与可信执行环境（TEE）**。

[论文目录](PAPERS.md) · [最近运行状态](reports/latest-run.md) · [运行与配置说明](TECHNICAL.md) · [Actions](https://github.com/Yanio9/MPC-TEE-paper-tracker/actions)

## 追踪范围

- **MPC**：安全多方/两方/三方计算、混淆电路、不经意传输、私有集合求交/并集、秘密共享。
- **TEE**：可信执行环境、机密计算、Intel SGX/TDX、AMD SEV/SNP、TrustZone、ARM CCA，以及相关安全与远程证明研究。
- 同时匹配的论文归入 **MPC + TEE**；匹配依据保存在数据与摘要展开栏中。

**不会泛抓联邦学习论文。** `federate`、`FedAvg` 等原有检索条件已移除。联邦学习论文只有在标题或摘要符合 MPC/TEE 规则时才收录，例如“用 MPC 做隐私保护聚合”或“在 SGX 内执行联邦训练”。普通 FedAvg、非 IID、客户端选择等论文不会仅因涉及 FL 就被收录。

若希望连交叉论文也排除，将 `config.yaml` 的 `tracking.exclude_federated_learning` 设为 `true`。该选项排除标题/已取得摘要中明确提到 federated learning 的论文，不能识别未明示的 FL 应用。

## 数据来源

| 来源 | 获取方式 | 默认范围 |
|---|---|---|
| DBLP | 官方 SPARQL API，按关键词、年份和会议/期刊分页查询 | 固定从 **2020 年**到当前年份 +1；密码学、安全、系统、数据库及相关 ML 会议 |
| arXiv | 官方 Atom API，在标题和摘要中检索 | 首次从 **2020-01-01** 回补，此后从上次成功时间向前重叠 3 天 |
| IACR ePrint | 官方 OAI-PMH，支持日期范围和续传令牌 | 首次从 **2020-01-01** 回补，此后增量扫描并重叠 3 天 |

DBLP 包括 CRYPTO、EUROCRYPT、ASIACRYPT、TCC、PKC、Journal of Cryptology、ToSC/TCHES，以及 S&P、CCS、USENIX Security、NDSS、PoPETs、OSDI、SOSP、EuroSys、ASPLOS 等，完整可编辑列表见 `config.yaml`。

三个来源独立执行。没有“第一个关键词有新论文，才扫描其余关键词”的限制。通过来源 ID、规范化 DOI、arXiv ID、ePrint ID 和规范化标题合并重复记录，保留不同来源链接。标题差异很大且无共享标识符的版本仍可能重复，需要人工核对。

## 自动更新与通知

- 每天 **北京时间 09:17** 计划运行（GitHub 调度可能延迟）。
- 首次成功扫描各来源时只建立基线，避免历史论文刷屏；后续新增论文创建汇总 Issue。
- 点击本仓库 **Watch → Custom → Issues** 订阅论文提醒；GitHub 的邮件通知取决于你的账户通知设置。
- 在 **Actions → Track MPC and TEE papers → Run workflow** 手动运行。填 `since: 2020-01-01` 可安静回补历史论文，不发送补录提醒；DBLP 固定起点由 `tracking.start_year` 控制。
- 同一天已经成功的来源默认不重复抓取。ePrint 每天至多刷新一次近期窗口；明确请求的历史回补只查询更早的区间。失败来源保留原成功时间，下次继续补抓。
- 来源失败会写入运行报告，并让工作流显示失败；其他成功来源仍保存结果。反爬验证页不会被当成零篇论文。

无需付费 API key 即可采集。arXiv/ePrint 摘要随元数据获取；DBLP 的缺失摘要可选用 Crossref 补充。若需要中文翻译，在本仓库 **Settings → Secrets and variables → Actions** 添加自己的 `DASHSCOPE_API_KEY`；翻译会使用你账户的 Qwen-MT-plus 配额。默认未提供 key 时跳过翻译，不影响采集。

## 本地运行

要求 Python 3.11 或更高版本。

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m src.main
```

只检查两个预印本来源：

```bash
python -m src.main --sources arxiv,eprint --no-enrich
```

试运行不写入缓存或文件：

```bash
python -m src.main --dry-run --no-enrich
```

采集程序只更新本地文件。GitHub Actions 在**本仓库**提交结果并发布 Issue，不创建 PR，不同步或写入原作者仓库。

## 局限与可调参数

这是基于元数据和规则的论文发现工具，不保证查全率或精确率。DBLP 通常没有摘要，标题未明确提到相关技术时可能漏检；预印本可能只在相关工作中提到 MPC/TEE 而被命中。缩写必须带安全/密码学上下文，避免将控制领域 MPC、医学 TEE 等误收录。

增删 `topics.*.dblp_terms` / `arxiv_terms` 可以调整发现范围；修改 `topics.*.patterns` 和缩写上下文规则可调整筛选标准。新增会议仅修改 DBLP 的 `venues`，不会因为缺少硬编码分类映射而在输出时丢失论文。

发表年份起点固定为 `tracking.start_year: 2020`，不会随当前年份向后滚动。预印本以首次提交年份判断是否在范围内，早于 2020 年、仅在近期修订的预印本不会单独收录。历史 arXiv 查询按提交年份分段，减少单次查询过大造成的截断。

## 来源与许可

本项目基于 [youngfish42/FL-paper-update-tracker](https://github.com/youngfish42/FL-paper-update-tracker) 的工作流程思路改造，经 [Yanio9 的 fork](https://github.com/Yanio9/FL-paper-update-tracker) 获取，参考版本为 `90930fad44e2f177e85cb4f975a081523bd66277`。原项目基于 [beiyuouo/dblp-watcher](https://github.com/beiyuouo/dblp-watcher)。保留原作者 Yuwen Yang 的 [MIT License](LICENSE)。本仓库为独立个人版本，与原项目不存在自动合并关系。

接口说明：[DBLP SPARQL](https://blog.dblp.org/2024/09/09/introducing-our-public-sparql-query-service/)、[DBLP 搜索 API](https://dblp.org/faq/How+to+use+the+dblp+search+API.html)、[arXiv](https://info.arxiv.org/help/api/user-manual.html)、[IACR ePrint](https://eprint.iacr.org/rss/)。预印本摘要与元数据来自各来源；论文全文遵循各自许可，本仓库不下载全文 PDF。
