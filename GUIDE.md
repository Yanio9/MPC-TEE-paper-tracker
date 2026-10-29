# 使用与收录说明

Yanio9 的个人论文追踪器：**安全多方计算（MPC）与可信执行环境（TEE）**。

[论文目录](PAPERS.md) · [最近运行状态](reports/latest-run.md) · [运行与配置说明](TECHNICAL.md) · [Actions](https://github.com/Yanio9/MPC-TEE-paper-tracker/actions)

## 追踪范围

- **MPC**：安全多方/两方/三方计算、混淆电路、不经意传输、私有集合求交/并集、秘密共享。
- **TEE**：可信执行环境、机密计算、Intel SGX/TDX、AMD SEV/SNP、TrustZone、ARM CCA，以及相关安全与远程证明研究。
- 论文按 **CRYPTO、EUROCRYPT、ASIACRYPT、TCC、PKC、Journal of Cryptology、S&P、CCS 等会议和期刊名称**分别归类，每组按年份倒序。分组顺序沿用配置中的会议/期刊顺序。
- MPC、TEE 与 **MPC + TEE** 作为每篇论文的方向标签；匹配依据保存在论文数据中。
- 仓库首页和 `PAPERS.md` 直接展示全部论文表格：标题、会议/期刊/来源、年份、方向、论文及代码链接。完整网页可搜索标题、作者和摘要，并按会议/期刊、方向、年份及发表记录筛选。
- 每篇去重论文只展示一次：有多个正式发表版本时，按最新正式发表记录归类；仅有预印本来源时，分别归入 IACR ePrint 或 arXiv，同时收录于两者的优先归入 ePrint，保留全部来源链接。
- 目录区分“含会议/期刊记录”与“仅预印本来源”；后者表示本工具尚未关联到正式发表记录，不代表论文一定尚未发表。
- 已关联正式发表记录的论文，表格年份优先使用会议/期刊年份，避免被较晚上传的预印本年份覆盖。

**不会泛抓联邦学习论文。** `federate`、`FedAvg` 等原有检索条件已移除。联邦学习论文只有在标题或摘要符合 MPC/TEE 规则时才收录，例如“用 MPC 做隐私保护聚合”或“在 SGX 内执行联邦训练”。普通 FedAvg、非 IID、客户端选择等论文不会仅因涉及 FL 就被收录。

若希望连交叉论文也排除，将 `config.yaml` 的 `tracking.exclude_federated_learning` 设为 `true`。该选项排除标题/已取得摘要中明确提到 federated learning 的论文，不能识别未明示的 FL 应用。

## 数据来源

| 来源 | 获取方式 | 默认范围 |
|---|---|---|
| DBLP | 官方 SPARQL API，按关键词、年份和会议/期刊分页查询 | 固定从 **2020 年**到当前年份 +1；密码学、安全、系统、数据库及相关 ML 会议 |
| arXiv | 官方 Atom API，在标题和摘要中检索 | 首次从 **2020-01-01** 回补，此后从上次成功时间向前重叠 3 天 |
| IACR ePrint | 官方 OAI-PMH，支持日期范围和续传令牌 | 首次从 **2020-01-01** 回补，此后增量扫描并重叠 3 天 |

DBLP 包括 CRYPTO、EUROCRYPT、ASIACRYPT、TCC、PKC、Journal of Cryptology、ToSC/TCHES，以及 S&P、CCS、USENIX Security、NDSS、PoPETs、OSDI、SOSP、EuroSys、ASPLOS 等，完整可编辑列表见 `config.yaml`。

### 会议等级与领域重点

正式发表来源采用精选白名单，综合通用等级与本领域的重要性，不设置统一的“仅 CCF A”门槛。密码学来源维护参考 [中国密码学会 CACR 目录（2025 年）](https://www.cacrnet.org.cn/site/content/1675.html)，不会把来源等级当成单篇论文的质量判断。无论来自哪个会议或期刊，都必须满足 MPC / TEE 主题筛选。

- MPC 重点：CRYPTO（美密）、EUROCRYPT（欧密）、ASIACRYPT（亚密）、TCC、PKC、Journal of Cryptology，以及相关密码协议、隐私与实现领域来源。
- TEE 重点：S&P、CCS、USENIX Security、NDSS，以及 OSDI、SOSP、EuroSys、ASPLOS 等系统与体系结构来源。
- arXiv / IACR ePrint：独立保留早期发现渠道，不赋予会议等级；发现正式发表记录后合并链接。
- ChinaCrypt（全国密码学术会议 / 中国密码学会年会）：列为个人重点补充关注来源，**当前尚未接入自动逐篇采集**，不计入已覆盖的 DBLP 来源。其 [2025 年官方征文通知](https://www.cacrnet.org.cn/site/content/1633.html) 区分未正式出版的会议交流资料与已在其他顶会顶刊发表的交流论文；后者应保留原发表出处，不能重复算作新的 ChinaCrypt 论文。

三个来源独立执行。没有“第一个关键词有新论文，才扫描其余关键词”的限制。通过来源 ID、规范化 DOI、arXiv ID、ePrint ID 和规范化标题合并重复记录，保留不同来源链接。标题差异很大且无共享标识符的版本仍可能重复，需要人工核对。

## 自动更新与通知

- 每天 **北京时间 09:17** 计划运行（GitHub 调度可能延迟）。
- 首次成功扫描各来源时只建立基线，避免历史论文刷屏；后续新增论文创建汇总 Issue。
- 点击本仓库 **Watch → Custom → Issues** 订阅论文提醒；GitHub 的邮件通知取决于你的账户通知设置。
- 在 **Actions → Track MPC and TEE papers → Run workflow** 手动运行。填 `since: 2020-01-01` 可安静回补历史论文，不发送补录提醒；DBLP 固定起点由 `tracking.start_year` 控制。
- 同一天已经成功的来源默认不重复抓取。需要立即重查时，在手动运行中勾选 `refresh`，或本地运行 `python -m src.main --refresh`；它保留历史覆盖、去重与请求间隔，重新查询当前增量窗口。
- 默认 ePrint 每天只刷新一次近期窗口；未勾选 `refresh` 的历史回补只查询更早区间。失败来源保留原成功时间，下次继续补抓。
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
