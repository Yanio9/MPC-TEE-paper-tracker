# MPC & TEE Paper Tracker

安全多方计算（MPC）与可信执行环境（TEE）论文。通过 DBLP 追踪 **2020 年起正式发表于会议或期刊**的相关论文，每日北京时间 **09:17** 自动更新。

**[完整论文单页：浏览、搜索与摘要](https://yanio9.github.io/MPC-TEE-paper-tracker/)** · [使用与收录说明](GUIDE.md) · [最近更新状态](reports/latest-run.md) · [Actions](https://github.com/Yanio9/MPC-TEE-paper-tracker/actions)

下方直接列出论文。若 GitHub 未显示完整列表，请打开上方的完整论文单页。

论文按会议、期刊名称归类，组内按年份倒序；MPC、TEE 与交叉方向显示为标签。arXiv 和 IACR ePrint 不再独立抓取，已发表论文附带的预印本链接保留为全文入口。普通联邦学习论文不会单独收录；ChinaCrypt 暂列补充关注来源，尚未接入自动逐篇采集。

本项目参考 [FL-paper-update-tracker](https://github.com/youngfish42/FL-paper-update-tracker) 的工作流程，经 [Yanio9 的 fork](https://github.com/Yanio9/FL-paper-update-tracker) 改造；保留原作者 Yuwen Yang 的 [MIT License](LICENSE)。这是独立个人版本，不向原仓库同步或提交 PR。

<!-- PAPERS:START -->

共 **704** 篇去重论文，均已关联会议或期刊发表记录。

按会议、期刊分组，组内按年份倒序；MPC / TEE 为方向标签。已发表论文附带的 arXiv / ePrint 链接作为全文入口保留。

**会议与期刊**：[CRYPTO（75）](#venue-crypto) · [EUROCRYPT（75）](#venue-eurocrypt) · [ASIACRYPT（46）](#venue-asiacrypt) · [TCC（57）](#venue-tcc) · [PKC（15）](#venue-pkc) · [Journal of Cryptology（29）](#venue-journal-of-cryptology) · [TCHES（11）](#venue-tches) · [IEEE S&amp;P（43）](#venue-ieee-s-p) · [ACM CCS（47）](#venue-acm-ccs) · [USENIX Security（60）](#venue-usenix-security) · [NDSS（25）](#venue-ndss) · [PoPETs（34）](#venue-popets) · [TIFS（54）](#venue-tifs) · [TDSC（57）](#venue-tdsc) · [OSDI（2）](#venue-osdi) · [EuroSys（8）](#venue-eurosys) · [NSDI（2）](#venue-nsdi) · [ISCA（7）](#venue-isca) · [MICRO（5）](#venue-micro) · [HPCA（3）](#venue-hpca) · [ASPLOS（11）](#venue-asplos) · [SIGMOD（3）](#venue-sigmod) · [PACMMOD / SIGMOD（3）](#venue-pacmmod-sigmod) · [PVLDB（6）](#venue-pvldb) · [ICDE（3）](#venue-icde) · [TPDS（3）](#venue-tpds) · [FOCS（4）](#venue-focs) · [STOC（4）](#venue-stoc) · [ICML（4）](#venue-icml) · [NeurIPS（4）](#venue-neurips) · [ICLR（2）](#venue-iclr) · [conf/woot（2）](#venue-conf-woot)

<a id="venue-crypto"></a>

## CRYPTO（75）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| Unconditionally Secure MPC for Boolean Circuits with Constant Communication. | CRYPTO | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-35418-1_1) · [ePrint](https://eprint.iacr.org/2026/1194) |
| Statistically Secure Asynchronous MPC with Linear Communication and 풪(n5) Additive Overhead. | CRYPTO | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-35418-1_2) |
| Secure Computation Against NC1 Leakage Without Secure Hardware. | CRYPTO | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-35415-0_10) |
| Multiparty Computation with Minimal Overhead Without Circuit Transformation. | CRYPTO | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-35418-1_5) |
| Just-in-Time-OPRFs and a Modular Framework for Fast Private Set Intersection. | CRYPTO | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-35418-1_12) · [ePrint](https://eprint.iacr.org/2026/1532) |
| Dishonest-Majority Secure Computation via PIR-Authenticated Multiplication Triples. | CRYPTO | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-35418-1_15) · [ePrint](https://eprint.iacr.org/2026/257) |
| Breaking the $\\varOmega (\|C\|\\kappa )$ Barrier on Garbled Circuit Size in the Random Oracle Model. | CRYPTO | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-35418-1_18) |
| Actively Secure MPC with O(\|C\|) Computation and Communication via CRT. | CRYPTO | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-35418-1_7) · [ePrint](https://eprint.iacr.org/2026/1270) |
| ømega (1/λ )-Rate Boolean Garbling Scheme from Generic Groups. | CRYPTO | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-032-01884-7_16) |
| The Round Complexity of Black-Box Post-quantum Secure Computation. | CRYPTO | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-032-01884-7_1) · [arXiv](https://arxiv.org/abs/2502.13830) · [ePrint](https://eprint.iacr.org/2025/250) |
| Strong Secret Sharing with Snitching. | CRYPTO | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-032-01884-7_10) · [ePrint](https://eprint.iacr.org/2025/1119) |
| Silent Circuit Relinearisation: Sublinear-Size (Boolean and Arithmetic) Garbled Circuits from DCR. | CRYPTO | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-032-01884-7_14) · [ePrint](https://eprint.iacr.org/2025/245) |
| NIZK Amplification via Leakage-Resilient Secure Computation. | CRYPTO | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-032-01907-3_15) · [ePrint](https://eprint.iacr.org/2025/995) |
| Lower Bounds for Garbled Circuits from Shannon-Type Information Inequalities. | CRYPTO | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-032-01884-7_19) · [ePrint](https://eprint.iacr.org/2025/876) |
| How to Make Any Computational Secret Sharing Scheme Adaptively Secure. | CRYPTO | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-032-01884-7_11) · [ePrint](https://eprint.iacr.org/2025/1014) |
| Fully Anonymous Secret Sharing. | CRYPTO | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-032-01884-7_12) · [ePrint](https://eprint.iacr.org/2025/1984) |
| Computationally Differentially Private Inner-Product Protocols Imply Oblivious Transfer. | CRYPTO | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-032-01884-7_6) · [arXiv](https://arxiv.org/abs/2502.15629) |
| Bitwise Garbling Schemes - A Model with 32λ\\documentclass\[12pt\]{minimal} \\usepackage{amsmath} \\usepackage{wasysym} \\usepackage{amsfonts} \\usepackage{amssymb} \\usepackage{amsbsy} \\usepackage{mathrsfs} \\usepackage{upgreek} \\setlength{\\oddsidemargin}{-69pt} \\begin{document}$$\\frac{3}{2}\\lambda $$\\end{document}-Bit Lower Bound of Ciphertexts. | CRYPTO | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-032-01884-7_15) |
| Authenticated BitGC for Actively Secure Rate-One 2PC. | CRYPTO | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-032-01884-7_21) · [ePrint](https://eprint.iacr.org/2025/232) |
| Actively Secure MPC in the Dishonest Majority Setting: Achieving Constant Complexity in Online Communication, Computation Per Gate, Rounds, and Private Input Size. | CRYPTO | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-032-01884-7_4) · [ePrint](https://eprint.iacr.org/2025/810) |
| A Unified Framework for Succinct Garbling from Homomorphic Secret Sharing. | CRYPTO | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-032-01884-7_13) · [ePrint](https://eprint.iacr.org/2025/442) |
| Traceable Secret Sharing: Strong Security and Efficient Constructions. | CRYPTO | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-68388-6_9) · [ePrint](https://eprint.iacr.org/2024/405) |
| Towards Breaking the Half-Barrier of Local Leakage-Resilient Shamir's Secret Sharing. | CRYPTO | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-68388-6_10) |
| Stochastic Secret Sharing with 1-Bit Shares and Applications to MPC. | CRYPTO | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-68388-6_11) · [ePrint](https://eprint.iacr.org/2024/1053) |
| Secure Multiparty Computation with Identifiable Abort via Vindicating Release. | CRYPTO | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-68397-8_2) |
| Secret Sharing with Certified Deletion. | CRYPTO | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-68394-7_7) · [arXiv](https://arxiv.org/abs/2405.08117) · [ePrint](https://eprint.iacr.org/2024/736) |
| Scalable Multiparty Computation from Non-linear Secret Sharing. | CRYPTO | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-68397-8_12) · [ePrint](https://eprint.iacr.org/2025/1007) |
| Linear-Communication Asynchronous Complete Secret Sharing with Optimal Resilience. | CRYPTO | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-68397-8_13) · [ePrint](https://eprint.iacr.org/2024/245) |
| Fully Secure MPC and zk-FLIOP over Rings: New Constructions, Improvements and Extensions. | CRYPTO | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-68397-8_5) · [ePrint](https://eprint.iacr.org/2024/837) |
| Doubly Efficient Cryptography: Commitments, Arguments and RAM MPC. | CRYPTO | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-68397-8_8) · [ePrint](https://eprint.iacr.org/2025/235) |
| Computation Efficient Structure-Aware PSI from Incremental Function Secret Sharing. | CRYPTO | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-68397-8_10) · [ePrint](https://eprint.iacr.org/2024/842) |
| 10-Party Sublinear Secure Computation from Standard Assumptions. | CRYPTO | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-68400-5_2) · [ePrint](https://eprint.iacr.org/2025/269) |
| Secure Multiparty Computation from Threshold Encryption Based on Class Groups. | CRYPTO | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-38557-5_20) · [ePrint](https://eprint.iacr.org/2022/1437) |
| Secure Computation with Shared EPR Pairs (Or: How to Teleport in Zero-Knowledge). | CRYPTO | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-38554-4_8) · [arXiv](https://arxiv.org/abs/2304.10480) · [ePrint](https://eprint.iacr.org/2023/564) |
| Reusable Secure Computation in the Plain Model. | CRYPTO | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-38557-5_14) · [ePrint](https://eprint.iacr.org/2023/1006) |
| New Bounds on the Local Leakage Resilience of Shamir's Secret Sharing Scheme. | CRYPTO | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-38557-5_5) · [ePrint](https://eprint.iacr.org/2023/805) |
| Network-Agnostic Security Comes (Almost) for Free in DKG and MPC. | CRYPTO | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-38557-5_3) · [ePrint](https://eprint.iacr.org/2022/1369) |
| Multi-party Homomorphic Secret Sharing and Sublinear MPC from Sparse LPN. | CRYPTO | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-38545-2_11) · [ePrint](https://eprint.iacr.org/2023/1593) |
| Malicious Secure, Structure-Aware Private Set Intersection. | CRYPTO | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-38557-5_19) · [ePrint](https://eprint.iacr.org/2023/1166) |
| List Oblivious Transfer and Applications to Round-Optimal Black-Box Multiparty Coin Tossing. | CRYPTO | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-38557-5_15) · [ePrint](https://eprint.iacr.org/2023/1512) |
| Cryptography with Weights: MPC, Encryption and Signatures. | CRYPTO | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-38557-5_10) · [ePrint](https://eprint.iacr.org/2022/1632) |
| Bingo: Adaptivity and Asynchrony in Verifiable Secret Sharing and Distributed Key Generation. | CRYPTO | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-38557-5_2) · [ePrint](https://eprint.iacr.org/2022/1759) |
| Two-Round MPC Without Round Collapsing Revisited - Towards Efficient Malicious Protocols. | CRYPTO | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-15802-5_13) · [ePrint](https://eprint.iacr.org/2022/944) |
| Tight Bounds on the Randomness Complexity of Secure Multiparty Computation. | CRYPTO | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-15985-5_17) · [ePrint](https://eprint.iacr.org/2022/799) |
| Structure-Aware Private Set Intersection, with Applications to Fuzzy Matching. | CRYPTO | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-15802-5_12) · [ePrint](https://eprint.iacr.org/2022/1011) |
| Short Leakage Resilient and Non-malleable Secret Sharing Schemes. | CRYPTO | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-15802-5_7) · [ePrint](https://eprint.iacr.org/2022/216) |
| Sharing Transformation and Dishonest Majority MPC with Packed Secret Sharing. | CRYPTO | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-15985-5_1) · [ePrint](https://eprint.iacr.org/2022/831) |
| More Efficient Dishonest Majority Secure Computation over $\\mathbb {Z}\_{2^k}$ via Galois Rings. | CRYPTO | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-15802-5_14) · [ePrint](https://eprint.iacr.org/2022/815) |
| YOSO: You Only Speak Once - Secure MPC with Stateless Ephemeral Roles. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84245-1_3) · [ePrint](https://eprint.iacr.org/2021/210) |
| Upslices, Downslices, and Secret-Sharing with Complexity of 1.5n. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84252-9_21) |
| Traceable Secret Sharing and Applications. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84252-9_24) · [ePrint](https://eprint.iacr.org/2021/871) |
| Three-Round Secure Multiparty Computation from Black-Box Two-Round Oblivious Transfer. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84245-1_7) · [ePrint](https://eprint.iacr.org/2021/957) |
| Three Halves Make a Whole? Beating the Half-Gates Lower Bound for Garbled Circuits. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84242-0_5) · [ePrint](https://eprint.iacr.org/2021/749) |
| Silver: Silent VOLE and Oblivious Transfer from Hardness of Decoding Structured LDPC Codes. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84252-9_17) · [ePrint](https://eprint.iacr.org/2021/1150) |
| Secure Computation from One-Way Noisy Communication, or: Anti-correlation via Anti-concentration. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84245-1_5) |
| Quadratic Secret Sharing and Conditional Disclosure of Secrets. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84252-9_25) · [ePrint](https://eprint.iacr.org/2021/285) |
| One-Way Functions Imply Secure Computation in a Quantum World. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84242-0_17) · [arXiv](https://arxiv.org/abs/2011.13486) · [ePrint](https://eprint.iacr.org/2020/1487) |
| On the Round Complexity of Black-Box Secure MPC. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84245-1_8) · [ePrint](https://eprint.iacr.org/2021/1467) |
| Oblivious Key-Value Stores and Amplification for Private Set Intersection. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84245-1_14) · [ePrint](https://eprint.iacr.org/2021/883) |
| Non-interactive Secure Multiparty Computation for Symmetric Functions, Revisited: More Efficient Constructions and Extensions. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84245-1_11) |
| MPC-Friendly Symmetric Cryptography from Alternating Moduli: Candidates, Protocols, and Applications. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84259-8_18) · [ePrint](https://eprint.iacr.org/2021/885) |
| Large Message Homomorphic Secret Sharing from DCR and Applications. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84252-9_23) · [ePrint](https://eprint.iacr.org/2021/274) |
| Fluid MPC: Secure Multiparty Computation with Dynamic Participants. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84245-1_4) · [ePrint](https://eprint.iacr.org/2020/754) |
| Efficient Information-Theoretic Multi-party Computation over Non-commutative Rings. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84245-1_12) · [ePrint](https://eprint.iacr.org/2021/1025) |
| Constructing Locally Leakage-Resilient Linear Secret-Sharing Schemes. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84252-9_26) · [ePrint](https://eprint.iacr.org/2020/1517) |
| Broadcast-Optimal Two Round MPC with an Honest Majority. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84245-1_6) · [ePrint](https://eprint.iacr.org/2020/1254) |
| Asymptotically-Good Arithmetic Secret Sharing over $\\mathbb {Z}/p^{\\ell }\\mathbb {Z}$ with Strong Multiplication and Its Applications to Efficient MPC. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84252-9_22) |
| Adaptive Extractors and Their Application to Leakage Resilient Secret Sharing. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84252-9_20) · [ePrint](https://eprint.iacr.org/2020/1252) |
| ATLAS: Efficient and Scalable MPC in the Honest Majority Setting. | CRYPTO | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-84245-1_9) · [ePrint](https://eprint.iacr.org/2021/833) |
| Stacked Garbling - Garbled Circuit Proportional to Longest Execution Path. | CRYPTO | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-56880-1_27) · [ePrint](https://eprint.iacr.org/2020/973) |
| Private Set Intersection in the Internet Setting from Lightweight Oblivious PRF. | CRYPTO | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-56877-1_2) · [ePrint](https://eprint.iacr.org/2020/729) |
| Non-malleable Secret Sharing Against Bounded Joint-Tampering Attacks in the Plain Model. | CRYPTO | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-56877-1_5) · [ePrint](https://eprint.iacr.org/2020/725) |
| Nearly Optimal Robust Secret Sharing Against Rushing Adversaries. | CRYPTO | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-56877-1_6) |
| Guaranteed Output Delivery Comes Free in Honest Majority MPC. | CRYPTO | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-56880-1_22) · [ePrint](https://eprint.iacr.org/2020/189) |
| Always Have a Backup Plan: Fully Secure Synchronous MPC with Asynchronous Fallback. | CRYPTO | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-56880-1_25) · [ePrint](https://eprint.iacr.org/2020/740) |

<a id="venue-eurocrypt"></a>

## EUROCRYPT（75）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| Updatable Private Set Intersection from Symmetric-Key Techniques. | EUROCRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-25317-0_13) · [ePrint](https://eprint.iacr.org/2026/438) |
| Traceable Secret Sharing Schemes for General Access Structures. | EUROCRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-25324-8_1) · [ePrint](https://eprint.iacr.org/2025/1120) |
| Traceable Secret Sharing Revisited. | EUROCRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-25324-8_2) · [ePrint](https://eprint.iacr.org/2025/1980) |
| Succinct Garbled Circuits with Low-Depth Garbling Algorithms. | EUROCRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-25324-8_9) · [ePrint](https://eprint.iacr.org/2025/2308) |
| Simultaneous-Message and Succinct Secure Computation: Reusable and Multiparty Protocols. | EUROCRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-25324-8_4) · [ePrint](https://eprint.iacr.org/2026/1425) |
| Perfectly Secure Network-Agnostic MPC Comes for Free. | EUROCRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-25324-8_12) · [ePrint](https://eprint.iacr.org/2026/377) |
| PUFF: Maximally Proactive Security for Free in Perfectly Secure MPC with Guaranteed Output Delivery. | EUROCRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-25324-8_18) · [ePrint](https://eprint.iacr.org/2026/509) |
| On the Security of Linear Secret Sharing with General Noisy Side-Channel Leakage. | EUROCRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-25336-1_17) · [ePrint](https://eprint.iacr.org/2025/1809) |
| On Succinct Non-interactive Secure Computation with Malicious Security. | EUROCRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-25324-8_20) · [ePrint](https://eprint.iacr.org/2026/909) |
| Non-interactive Secure Computation with Constant Communication Overhead. | EUROCRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-25324-8_5) · [ePrint](https://eprint.iacr.org/2026/1555) |
| New Upper and Lower Bounds for Perfectly Secure MPC. | EUROCRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-25324-8_13) · [ePrint](https://eprint.iacr.org/2025/1206) |
| Malicious Private Set Union with Two-Sided Output. | EUROCRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-25317-0_14) · [ePrint](https://eprint.iacr.org/2026/204) |
| Maintaining Sublinear Locality Over Time: Adaptively Secure MPC on a Reusable Hidden Graph. | EUROCRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-25324-8_19) · [ePrint](https://eprint.iacr.org/2026/905) |
| Fast and Efficient Perfectly Secure Network-Agnostic Secure Computation. | EUROCRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-25324-8_7) · [ePrint](https://eprint.iacr.org/2026/655) |
| Client-Server Homomorphic Secret Sharing in the CRS Model. | EUROCRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-25324-8_3) |
| TinyLabels: How to Compress Garbled Circuit Input Labels, Efficiently. | EUROCRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-91095-1_9) · [ePrint](https://eprint.iacr.org/2024/2048) |
| Simultaneous-Message and Succinct Secure Computation. | EUROCRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-91092-0_8) · [ePrint](https://eprint.iacr.org/2025/096) |
| Secret Sharing with Publicly Verifiable Deletion. | EUROCRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-91131-6_10) · [ePrint](https://eprint.iacr.org/2024/1596) |
| Round-Optimal Black-Box Multiparty Computation from Polynomial-Time Assumptions. | EUROCRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-91092-0_12) · [ePrint](https://eprint.iacr.org/2023/1742) |
| Physical-Bit Leakage Resilience of Linear Code-Based Secret Sharing. | EUROCRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-91101-9_3) |
| On the Adaptive Security of Free-XOR-Based Garbling Schemes in the Plain Model. | EUROCRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-91095-1_8) · [ePrint](https://eprint.iacr.org/2025/326) |
| Multi-Key Homomorphic Secret Sharing. | EUROCRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-91092-0_1) · [ePrint](https://eprint.iacr.org/2025/094) |
| Leap: A Fast, Lattice-Based OPRF with Application to Private Set Intersection. | EUROCRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-91098-2_10) · [ePrint](https://eprint.iacr.org/2025/333) |
| Honest Majority MPC with Õ(\|C\|) Communication in Minicrypt. | EUROCRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-91092-0_16) |
| Efficient Mixed Garbling from Homomorphic Secret Sharing and GGM-Tree. | EUROCRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-91095-1_6) · [ePrint](https://eprint.iacr.org/2025/207) |
| Disincentivize Collusion in Verifiable Secret Sharing. | EUROCRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-91092-0_2) · [ePrint](https://eprint.iacr.org/2025/446) |
| Black-Box Constant-Round Secure 2PC with Succinct Communication. | EUROCRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-91092-0_13) · [ePrint](https://eprint.iacr.org/2025/474) |
| BitGC: Garbled Circuits with 1 Bit per Gate. | EUROCRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-91098-2_16) · [ePrint](https://eprint.iacr.org/2024/1988) |
| Two-Round Maliciously-Secure Oblivious Transfer with Optimal Rate. | EUROCRYPT | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-58751-1_10) · [ePrint](https://eprint.iacr.org/2024/372) |
| Toward Malicious Constant-Rate 2PC via Arithmetic Garbling. | EUROCRYPT | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-58740-5_14) · [ePrint](https://eprint.iacr.org/2024/283) |
| Succinct Homomorphic Secret Sharing. | EUROCRYPT | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-58751-1_11) · [ePrint](https://eprint.iacr.org/2024/814) |
| Publicly Verifiable Secret Sharing Over Class Groups and Applications to DKG and YOSO. | EUROCRYPT | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-58740-5_8) · [ePrint](https://eprint.iacr.org/2023/1651) |
| Garbled Circuit Lookup Tables with Logarithmic Number of Ciphertexts. | EUROCRYPT | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-58740-5_7) · [ePrint](https://eprint.iacr.org/2024/369) |
| Fuzzy Private Set Intersection with Large Hyperballs. | EUROCRYPT | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-58740-5_12) · [ePrint](https://eprint.iacr.org/2024/330) |
| Efficient Arithmetic in Garbled Circuits. | EUROCRYPT | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-58740-5_1) · [ePrint](https://eprint.iacr.org/2024/139) |
| Constructing Leakage-Resilient Shamir's Secret Sharing: Over Composite Order Fields. | EUROCRYPT | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-58737-5_11) |
| Connecting Leakage-Resilient Secret Sharing to Practice: Scaling Trends and Physical Dependencies of Prime Field Masking. | EUROCRYPT | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-58737-5_12) · [ePrint](https://eprint.iacr.org/2024/377) |
| Sublinear-Communication Secure Multiparty Computation Does Not Require FHE. | EUROCRYPT | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-30617-4_6) · [ePrint](https://eprint.iacr.org/2023/1802) |
| Reverse Firewalls for Oblivious Transfer Extension and Applications to Zero-Knowledge. | EUROCRYPT | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-30545-0_9) · [ePrint](https://eprint.iacr.org/2022/1535) |
| Oblivious Transfer with Constant Computational Overhead. | EUROCRYPT | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-30545-0_10) · [ePrint](https://eprint.iacr.org/2023/817) |
| Endemic Oblivious Transfer via Random Oracles, Revisited. | EUROCRYPT | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-30545-0_11) · [ePrint](https://eprint.iacr.org/2022/1525) |
| Detect, Pack and Batch: Perfectly-Secure MPC with Linear Communication and Constant Expected Time. | EUROCRYPT | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-30617-4_9) · [ePrint](https://eprint.iacr.org/2023/557) |
| Constrained Pseudorandom Functions from Homomorphic Secret Sharing. | EUROCRYPT | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-30620-4_7) · [ePrint](https://eprint.iacr.org/2023/387) |
| A New Framework for Quantum Oblivious Transfer. | EUROCRYPT | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-30545-0_13) · [arXiv](https://arxiv.org/abs/2209.04520) · [ePrint](https://eprint.iacr.org/2022/1191) |
| Secure Multiparty Computation with Sublinear Preprocessing. | EUROCRYPT | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-06944-4_15) |
| Secure Multiparty Computation with Free Branching. | EUROCRYPT | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-06944-4_14) · [ePrint](https://eprint.iacr.org/2023/901) |
| Round-Optimal and Communication-Efficient Multiparty Computation. | EUROCRYPT | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-06944-4_3) · [ePrint](https://eprint.iacr.org/2020/1437) |
| Round-Optimal Multi-party Computation with Identifiable Abort. | EUROCRYPT | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-06944-4_12) · [ePrint](https://eprint.iacr.org/2022/645) |
| Practical Non-interactive Publicly Verifiable Secret Sharing with Thousands of Parties. | EUROCRYPT | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-06944-4_16) · [ePrint](https://eprint.iacr.org/2021/1397) |
| Lightweight, Maliciously Secure Verifiable Function Secret Sharing. | EUROCRYPT | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-06944-4_6) · [ePrint](https://eprint.iacr.org/2021/580) |
| Garbled Circuits with Sublinear Evaluator. | EUROCRYPT | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-06944-4_2) · [ePrint](https://eprint.iacr.org/2022/797) |
| Adaptively Secure Computation for RAM Programs. | EUROCRYPT | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-07085-3_7) |
| Unbounded Multi-party Computation from Learning with Errors. | EUROCRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-77886-6_26) · [ePrint](https://eprint.iacr.org/2021/431) |
| Threshold Garbled Circuits and Ad Hoc Secure Computation. | EUROCRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-77883-5_3) · [ePrint](https://eprint.iacr.org/2021/308) |
| The Rise of Paillier: Homomorphic Secret Sharing and Public-Key Silent OT. | EUROCRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-77870-5_24) · [ePrint](https://eprint.iacr.org/2021/262) |
| Post-Quantum Multi-Party Computation. | EUROCRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-77870-5_16) · [arXiv](https://arxiv.org/abs/2005.12904) · [ePrint](https://eprint.iacr.org/2020/1395) |
| Order-C Secure Multiparty Computation for Highly Repetitive Circuits. | EUROCRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-77886-6_23) · [ePrint](https://eprint.iacr.org/2021/500) |
| Oblivious Transfer Is in MiniQCrypt. | EUROCRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-77886-6_18) · [arXiv](https://arxiv.org/abs/2011.14980) · [ePrint](https://eprint.iacr.org/2020/1500) |
| Multiparty Reusable Non-interactive Secure Computation from LWE. | EUROCRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-77886-6_25) · [ePrint](https://eprint.iacr.org/2021/378) |
| Leakage-Resilience of the Shamir Secret-Sharing Scheme Against Physical-Bit Leakages. | EUROCRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-77886-6_12) · [ePrint](https://eprint.iacr.org/2021/186) |
| Large Scale, Actively Secure Computation from LPN and Free-XOR Garbled Circuits. | EUROCRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-77883-5_2) · [ePrint](https://eprint.iacr.org/2021/120) |
| Generic Compiler for Publicly Verifiable Covert Multi-Party Computation. | EUROCRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-77886-6_27) · [ePrint](https://eprint.iacr.org/2021/251) |
| Function Secret Sharing for Mixed-Mode and Fixed-Point Secure Computation. | EUROCRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-77886-6_30) · [ePrint](https://eprint.iacr.org/2020/1392) |
| Constant-Overhead Unconditionally Secure Multiparty Computation Over Binary Fields. | EUROCRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-77886-6_28) · [ePrint](https://eprint.iacr.org/2020/1412) |
| Compact, Efficient and UC-Secure Isogeny-Based Oblivious Transfer. | EUROCRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-77870-5_8) · [ePrint](https://eprint.iacr.org/2020/1012) |
| Breaking the Circuit Size Barrier for Secure Computation Under Quasi-Polynomial LPN. | EUROCRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-77886-6_29) · [ePrint](https://eprint.iacr.org/2021/943) |
| Two-Round Oblivious Transfer from CDH or LPN. | EUROCRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-45724-2_26) |
| Succinct Non-interactive Secure Computation. | EUROCRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-45724-2_8) |
| Statistical Zaps and New Oblivious Transfer Protocols. | EUROCRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-45727-3_23) · [ePrint](https://eprint.iacr.org/2020/235) |
| Resource-Restricted Cryptography: Revisiting MPC Bounds in the Proof-of-Work Era. | EUROCRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-45724-2_5) |
| PSI from PaXoS: Fast, Malicious Private Set Intersection. | EUROCRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-45724-2_25) · [ePrint](https://eprint.iacr.org/2020/193) |
| Lower Bounds for Leakage-Resilient Secret Sharing. | EUROCRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-45721-1_20) |
| Evolving Ramp Secret Sharing with a Small Gap. | EUROCRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-45721-1_19) |
| Efficient Constructions for Almost-Everywhere Secure Computation. | EUROCRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-45724-2_6) |
| Blackbox Secret Sharing Revisited: A Coding-Theoretic Approach with Application to Expansionless Near-Threshold Schemes. | EUROCRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-45721-1_18) |

<a id="venue-asiacrypt"></a>

## ASIACRYPT（46）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| Towards Scalable YOSO MPC via Packed Secret-Sharing. | ASIACRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-981-95-5116-3_3) · [ePrint](https://eprint.iacr.org/2025/635) |
| Threshold Homomorphic Secret Sharing: Definitions and Constructions. | ASIACRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-981-95-5119-4_18) |
| Taming Adaptive Security and New Access Structures in Evolving Secret Sharing. | ASIACRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-981-95-5125-5_3) |
| Succinct Line-Point Zero-Knowledge Arguments from Homomorphic Secret Sharing. | ASIACRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-981-95-5116-3_19) · [ePrint](https://eprint.iacr.org/2025/1866) |
| Succinct Computational Secret Sharing for Monotone Circuits. | ASIACRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-981-95-5125-5_4) · [ePrint](https://eprint.iacr.org/2025/850) |
| Randomized Agreement, Verifiable Secret Sharing and Multi-party Computation in Granular Synchrony. | ASIACRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-981-95-5116-3_1) · [ePrint](https://eprint.iacr.org/2025/1327) |
| New Framework for Structure-Aware PSI From Distributed Function Secret Sharing. | ASIACRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-981-95-5116-3_10) · [ePrint](https://eprint.iacr.org/2025/907) |
| Fuzzy Private Set Intersection from VOLE. | ASIACRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-981-95-5116-3_11) · [ePrint](https://eprint.iacr.org/2025/911) |
| Broadcast-Optimal Secure Computation from Black-Box Oblivious Transfer. | ASIACRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-981-95-5116-3_5) · [ePrint](https://eprint.iacr.org/2025/1614) |
| A Construction of Evolving k-Threshold Secret Sharing Scheme over A Polynomial Ring. | ASIACRYPT | 2026 | MPC | [论文](https://doi.org/10.1007/978-981-95-5125-5_1) · [arXiv](https://arxiv.org/abs/2402.01144) · [ePrint](https://eprint.iacr.org/2025/1499) |
| Verifiable Secret Sharing from Symmetric Key Cryptography with Improved Optimistic Complexity. | ASIACRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-981-96-0941-3_4) · [ePrint](https://eprint.iacr.org/2024/838) |
| Updatable Private Set Intersection Revisited: Extended Functionalities, Deletion, and Worst-Case Complexity. | ASIACRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-981-96-0938-3_7) · [ePrint](https://eprint.iacr.org/2024/1446) |
| Unclonable Secret Sharing. | ASIACRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-981-96-0947-5_5) · [arXiv](https://arxiv.org/abs/2406.11008) · [ePrint](https://eprint.iacr.org/2024/716) |
| Timed Secret Sharing. | ASIACRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-981-96-0941-3_5) · [ePrint](https://eprint.iacr.org/2023/1024) |
| The Concrete Security of Two-Party Computation: Simple Definitions, and Tight Proofs for PSI and OPRFs. | ASIACRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-981-96-0938-3_11) · [ePrint](https://eprint.iacr.org/2024/1476) |
| QuietOT: Lightweight Oblivious Transfer with a Public-Key Setup. | ASIACRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-981-96-0888-1_7) · [ePrint](https://eprint.iacr.org/2024/1079) |
| Perfectly-Secure Multiparty Computation with Linear Communication Complexity over Any Modulus. | ASIACRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-981-96-0938-3_4) · [ePrint](https://eprint.iacr.org/2024/370) |
| Honest Majority GOD MPC with O(sfdepth(C)) Rounds and Low Online Communication. | ASIACRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-981-96-0938-3_8) |
| FOLEAGE: $\\mathbb {F}\_{\\scriptstyle 4}$OLE-Based Multi-party Computation for Boolean Circuits. | ASIACRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-981-96-0938-3_3) |
| Evolving Secret Sharing Made Short. | ASIACRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-981-96-0941-3_3) · [ePrint](https://eprint.iacr.org/2023/1534) |
| Efficient Fuzzy Private Set Intersection from Fuzzy Mapping. | ASIACRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-981-96-0938-3_2) · [ePrint](https://eprint.iacr.org/2024/1462) |
| Dishonest Majority Multiparty Computation over Matrix Rings. | ASIACRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-981-96-0938-3_10) · [ePrint](https://eprint.iacr.org/2023/1912) |
| Compute, but Verify: Efficient Multiparty Computation over Authenticated Inputs. | ASIACRYPT | 2025 | MPC | [论文](https://doi.org/10.1007/978-981-96-0938-3_5) · [ePrint](https://eprint.iacr.org/2022/1648) |
| Unconditionally Secure Multiparty Computation for Symmetric Functions with Low Bottleneck Complexity. | ASIACRYPT | 2023 | MPC | [论文](https://doi.org/10.1007/978-981-99-8721-4_11) · [ePrint](https://eprint.iacr.org/2023/662) |
| Threshold Linear Secret Sharing to the Rescue of MPC-in-the-Head. | ASIACRYPT | 2023 | MPC | [论文](https://doi.org/10.1007/978-981-99-8721-4_14) · [ePrint](https://eprint.iacr.org/2022/1407) |
| Sigma Protocols from Verifiable Secret Sharing and Their Applications. | ASIACRYPT | 2023 | MPC | [论文](https://doi.org/10.1007/978-981-99-8724-5_7) · [ePrint](https://eprint.iacr.org/2023/1388) |
| Scalable Multi-party Private Set Union from Multi-query Secret-Shared Private Membership Test. | ASIACRYPT | 2023 | MPC | [论文](https://doi.org/10.1007/978-981-99-8721-4_8) · [ePrint](https://eprint.iacr.org/2023/1413) |
| Practically Efficient Private Set Intersection from Trusted Hardware with Side-Channels. | ASIACRYPT | 2023 | MPC | [论文](https://doi.org/10.1007/978-981-99-8730-6_9) |
| Oblivious Transfer from Zero-Knowledge Proofs - Or How to Achieve Round-Optimal Quantum Oblivious Transfer and Zero-Knowledge Proofs on Quantum States. | ASIACRYPT | 2023 | MPC | [论文](https://doi.org/10.1007/978-981-99-8742-9_1) · [arXiv](https://arxiv.org/abs/2303.01476) · [ePrint](https://eprint.iacr.org/2023/311) |
| Adaptive Distributional Security for Garbling Schemes with 𝒪(\|x\|) Online Complexity. | ASIACRYPT | 2023 | MPC | [论文](https://doi.org/10.1007/978-981-99-8721-4_5) |
| YOLO YOSO: Fast and Simple Encryption and Secret Sharing in the YOSO Model. | ASIACRYPT | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-22963-3_22) · [ePrint](https://eprint.iacr.org/2022/242) |
| Non-interactive Secure Computation of Inner-Product from LPN and LWE. | ASIACRYPT | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-22963-3_16) · [ePrint](https://eprint.iacr.org/2023/072) |
| Concurrently Composable Non-interactive Secure Computation. | ASIACRYPT | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-22963-3_18) · [ePrint](https://eprint.iacr.org/2021/1562) |
| Two-Round Adaptively Secure MPC from Isogenies, LPN, or CDH. | ASIACRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-92075-3_11) · [ePrint](https://eprint.iacr.org/2023/1170) |
| Reverse Firewalls for Adaptively Secure MPC Without Setup. | ASIACRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-92075-3_12) · [ePrint](https://eprint.iacr.org/2021/1262) |
| Homomorphic Secret Sharing for Multipartite and General Adversary Structures Supporting Parallel Evaluation of Low-Degree Polynomials. | ASIACRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-92075-3_7) · [ePrint](https://eprint.iacr.org/2021/1395) |
| Better Security-Efficiency Trade-Offs in Permutation-Based Two-Party Computation. | ASIACRYPT | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-92075-3_10) · [ePrint](https://eprint.iacr.org/2022/080) |
| Simpler Statistically Sender Private Oblivious Transfer from Ideals of Cyclotomic Integers. | ASIACRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64834-3_13) · [ePrint](https://eprint.iacr.org/2020/1413) |
| Secure MPC: Laziness Leads to GOD. | ASIACRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64840-4_5) |
| On the Exact Round Complexity of Best-of-Both-Worlds Multi-party Computation. | ASIACRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64840-4_3) · [ePrint](https://eprint.iacr.org/2020/1050) |
| MPC with Synchronous Security and Asynchronous Responsiveness. | ASIACRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64840-4_4) |
| Efficient and Round-Optimal Oblivious Transfer and Commitment with Adaptive Security. | ASIACRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64840-4_10) · [ePrint](https://eprint.iacr.org/2020/545) |
| Efficient Fully Secure Computation via Distributed Zero-Knowledge Proofs. | ASIACRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64840-4_9) · [ePrint](https://eprint.iacr.org/2020/1451) |
| Crowd Verifiable Zero-Knowledge and End-to-End Verifiable Multiparty Computation. | ASIACRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64840-4_24) · [ePrint](https://eprint.iacr.org/2020/711) |
| Circuit Amortization Friendly Encodingsand Their Application to Statistically Secure Multiparty Computation. | ASIACRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64840-4_8) |
| ALBATROSS: Publicly AttestabLe BATched Randomness Based On Secret Sharing. | ASIACRYPT | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64840-4_11) · [ePrint](https://eprint.iacr.org/2020/644) |

<a id="venue-tcc"></a>

## TCC（57）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| Simplified PIR and CDS Protocols and Improved Linear Secret-Sharing Schemes. | TCC | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-12293-3_12) · [ePrint](https://eprint.iacr.org/2024/1599) |
| Pseudorandom Correlation Functions for Garbled Circuits. | TCC | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-12293-3_15) · [ePrint](https://eprint.iacr.org/2025/2325) |
| Polynomial Secret Sharing Schemes and Algebraic Matroids. | TCC | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-12293-3_14) · [ePrint](https://eprint.iacr.org/2025/368) |
| Multiparty Homomorphic Secret Sharing and More from LPN and MQ. | TCC | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-12293-3_16) · [ePrint](https://eprint.iacr.org/2025/966) |
| Honest Majority Constant-Round MPC with Linear Communication from One-Way Functions. | TCC | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-12287-2_1) · [ePrint](https://eprint.iacr.org/2025/1676) |
| Deniable Secret Sharing. | TCC | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-12293-3_13) · [ePrint](https://eprint.iacr.org/2025/525) |
| Split-State Non-malleable Codes and Secret Sharing Schemes for Quantum Messages. | TCC | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-78017-2_3) · [arXiv](https://arxiv.org/abs/2308.06466) · [ePrint](https://eprint.iacr.org/2024/335) |
| Secure Computation with Parallel Calls to 2-Ary Functions. | TCC | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-78023-3_8) · [ePrint](https://eprint.iacr.org/2024/1701) |
| Secret-Sharing Schemes for High Slices. | TCC | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-78023-3_19) · [ePrint](https://eprint.iacr.org/2024/602) |
| Reducing the Share Size of Weighted Threshold Secret Sharing Schemes via Chow Parameters Approximation. | TCC | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-78023-3_17) · [ePrint](https://eprint.iacr.org/2024/772) |
| Rate-1 Arithmetic Garbling From Homomorphic Secret Sharing. | TCC | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-78023-3_3) · [ePrint](https://eprint.iacr.org/2024/820) |
| Perfectly-Secure MPC with Constant Online Communication Complexity. | TCC | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-78023-3_11) · [ePrint](https://eprint.iacr.org/2024/242) |
| New Upper Bounds for Evolving Secret Sharing via Infinite Branching Programs. | TCC | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-78023-3_18) · [ePrint](https://eprint.iacr.org/2024/419) |
| Homomorphic Secret Sharing with Verifiable Evaluation. | TCC | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-78023-3_20) · [ePrint](https://eprint.iacr.org/2025/1491) |
| General Adversary Structures in Byzantine Agreement and Multi-party Computation with Active and Omission Corruption. | TCC | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-78023-3_7) · [ePrint](https://eprint.iacr.org/2024/209) |
| An Improvement Upon the Bounds for the Local Leakage Resilience of Shamir's Secret Sharing Scheme. | TCC | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-78023-3_13) |
| Adaptive Security, Erasures, and Network Assumptions in Communication-Local MPC. | TCC | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-78023-3_10) · [ePrint](https://eprint.iacr.org/2024/1489) |
| A Note on Low-Communication Secure Multiparty Computation via Circuit Depth-Reduction. | TCC | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-78023-3_6) · [ePrint](https://eprint.iacr.org/2024/1473) |
| Towards Topology-Hiding Computation from Oblivious Transfer. | TCC | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-48615-9_13) · [ePrint](https://eprint.iacr.org/2023/849) |
| Three Party Secure Computation with Friends and Foes. | TCC | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-48618-0_6) · [ePrint](https://eprint.iacr.org/2023/1605) |
| Proactive Secret Sharing with Constant Communication. | TCC | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-48618-0_12) · [ePrint](https://eprint.iacr.org/2023/942) |
| On the Round Complexity of Fully Secure Solitary MPC with Honest Majority. | TCC | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-48618-0_5) · [ePrint](https://eprint.iacr.org/2021/241) |
| On Secure Computation of Solitary Output Functionalities with and Without Broadcast. | TCC | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-48618-0_4) · [ePrint](https://eprint.iacr.org/2022/934) |
| Network Agnostic MPC with Statistical Security. | TCC | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-48618-0_3) · [arXiv](https://arxiv.org/abs/2306.01401) · [ePrint](https://eprint.iacr.org/2023/820) |
| Improved Polynomial Secret-Sharing Schemes. | TCC | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-48618-0_13) · [ePrint](https://eprint.iacr.org/2023/1158) |
| DORAM Revisited: Maliciously Secure RAM-MPC with Logarithmic Overhead. | TCC | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-48615-9_16) · [ePrint](https://eprint.iacr.org/2023/578) |
| 3-Party Secure Computation for RAMs: Optimal and Concretely Efficient. | TCC | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-48615-9_17) · [ePrint](https://eprint.iacr.org/2023/516) |
| Sublinear Secure Computation from New Assumptions. | TCC | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-22365-5_5) · [ePrint](https://eprint.iacr.org/2023/513) |
| Statistical Security in Two-Party Computation Revisited. | TCC | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-22365-5_7) · [ePrint](https://eprint.iacr.org/2022/1190) |
| Round-Optimal Honest-Majority MPC in Minicrypt and with Everlasting Security - (Extended Abstract). | TCC | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-22365-5_4) |
| Round-Optimal Black-Box Secure Computation from Two-Round Malicious OT. | TCC | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-22365-5_16) · [ePrint](https://eprint.iacr.org/2022/1288) |
| On Secret Sharing, Randomness, and Random-less Reductions for Secret Sharing. | TCC | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-22318-1_12) · [ePrint](https://eprint.iacr.org/2021/802) |
| On Perfectly Secure Two-Party Computation for Symmetric Functionalities with Correlated Randomness. | TCC | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-22365-5_19) · [ePrint](https://eprint.iacr.org/2022/1504) |
| Oblivious-Transfer Complexity of Noisy Coin-Toss via Secure Zero Communication Reductions. | TCC | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-22368-6_4) · [ePrint](https://eprint.iacr.org/2022/1539) |
| Leakage-resilient Linear Secret-sharing Against Arbitrary Bounded-size Leakage Family. | TCC | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-22318-1_13) |
| Fully-Secure MPC with Minimal Trust. | TCC | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-031-22365-5_17) · [ePrint](https://eprint.iacr.org/2022/1248) |
| Two-Round Maliciously Secure Computation with Super-Polynomial Simulation. | TCC | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-90459-3_22) · [ePrint](https://eprint.iacr.org/2021/1230) |
| Round-Efficient Byzantine Agreement and Multi-party Computation with Asynchronous Fallback. | TCC | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-90459-3_21) · [ePrint](https://eprint.iacr.org/2021/1141) |
| On Communication-Efficient Asynchronous MPC with Adaptive Security. | TCC | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-90453-1_2) · [ePrint](https://eprint.iacr.org/2021/1174) |
| On Communication Models and Best-Achievable Security in Two-Round MPC. | TCC | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-90453-1_4) · [ePrint](https://eprint.iacr.org/2021/690) |
| On Actively-Secure Elementary MPC Reductions. | TCC | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-90459-3_24) · [ePrint](https://eprint.iacr.org/2021/1208) |
| Oblivious Transfer from Trapdoor Permutations in Minimal Rounds. | TCC | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-90453-1_18) · [ePrint](https://eprint.iacr.org/2021/1433) |
| Laconic Private Set Intersection and Applications. | TCC | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-90456-2_4) · [ePrint](https://eprint.iacr.org/2021/728) |
| Information-Theoretically Secure MPC Against Mixed Dynamic Adversaries. | TCC | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-90459-3_20) · [ePrint](https://eprint.iacr.org/2021/1163) |
| Generalized Pseudorandom Secret Sharing and Efficient Straggler-Resilient Secure Computation. | TCC | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-90453-1_5) · [ePrint](https://eprint.iacr.org/2021/1223) |
| Environmentally Friendly Composable Multi-party Computation in the Plain Model from Standard (Timed) Assumptions. | TCC | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-90459-3_25) · [ePrint](https://eprint.iacr.org/2021/843) |
| Continuously Non-malleable Secret Sharing: Joint Tampering, Plain Model and Capacity. | TCC | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-90453-1_12) · [ePrint](https://eprint.iacr.org/2021/1128) |
| Towards Multiparty Computation Withstanding Coercion of All Parties. | TCC | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64378-2_15) · [ePrint](https://eprint.iacr.org/2020/1434) |
| The Share Size of Secret-Sharing Schemes for Almost All Access Structures and Graphs. | TCC | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64381-2_18) · [ePrint](https://eprint.iacr.org/2020/664) |
| Round Optimal Secure Multiparty Computation from Minimal Assumptions. | TCC | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64378-2_11) |
| Robust Secret Sharing with Almost Optimal Share Size and Security Against Rushing Adversaries. | TCC | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64381-2_17) |
| On the Complexity of Arithmetic Secret Sharing. | TCC | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64381-2_16) |
| On Statistical Security in Two-Party Computation. | TCC | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64378-2_19) · [ePrint](https://eprint.iacr.org/2020/1428) |
| Non-malleable Codes, Extractors and Secret Sharing for Interleaved Tampering and Composition of Tampering. | TCC | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64381-2_21) |
| Mr NISC: Multiparty Reusable Non-Interactive Secure Computation. | TCC | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64378-2_13) |
| Information-Theoretic 2-Round MPC Without Round Collapsing: Adaptive Security, and More. | TCC | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64378-2_18) · [ePrint](https://eprint.iacr.org/2020/1431) |
| A Secret-Sharing Based MPC Protocol for Boolean Circuits with Good Amortized Complexity. | TCC | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-64378-2_23) · [ePrint](https://eprint.iacr.org/2020/162) |

<a id="venue-pkc"></a>

## PKC（15）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| Scaling Fully Secure MPC via Robust Recursive Search and Gap Amplification. | PKC | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-26734-4_10) · [ePrint](https://eprint.iacr.org/2026/475) |
| On the Power of Sumcheck in Secure Multiparty Computation. | PKC | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-26734-4_9) · [ePrint](https://eprint.iacr.org/2025/177) |
| Malicious Homomorphic Secret Sharing with Applications to DV-NIZK and More. | PKC | 2026 | MPC | [论文](https://doi.org/10.1007/978-3-032-26740-5_7) · [ePrint](https://eprint.iacr.org/2025/2077) |
| Π: A Unified Framework for Computational Verifiable Secret Sharing. | PKC | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-91829-2_4) |
| Efficient Permutation Correlations and Batched Random Access for Two-Party Computation. | PKC | 2025 | MPC | [论文](https://doi.org/10.1007/978-3-031-91829-2_3) · [ePrint](https://eprint.iacr.org/2024/547) |
| On Sigma-Protocols and (Packed) Black-Box Secret Sharing Schemes. | PKC | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-57722-2_14) · [ePrint](https://eprint.iacr.org/2023/1652) |
| On Information-Theoretic Secure Multiparty Computation with Local Repairability. | PKC | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-57722-2_7) · [ePrint](https://eprint.iacr.org/2024/391) |
| Network-Agnostic Multi-party Computation Revisited (Extended Abstract). | PKC | 2024 | MPC | [论文](https://doi.org/10.1007/978-3-031-57722-2_6) |
| Threshold Private Set Intersection with Better Communication Complexity. | PKC | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-31371-4_9) · [ePrint](https://eprint.iacr.org/2023/919) |
| Round-Optimal Oblivious Transfer and MPC from Computational CSIDH. | PKC | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-31368-4_14) · [ePrint](https://eprint.iacr.org/2022/1511) |
| On Homomorphic Secret Sharing from Polynomial-Modulus LWE. | PKC | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-31371-4_1) · [ePrint](https://eprint.iacr.org/2023/382) |
| Improved Private Set Intersection for Sets with Small Entries. | PKC | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-031-31371-4_7) · [ePrint](https://eprint.iacr.org/2022/334) |
| Multi-party Threshold Private Set Intersection with Sublinear Communication. | PKC | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-75248-4_13) · [ePrint](https://eprint.iacr.org/2020/600) |
| A Geometric Approach to Homomorphic Secret Sharing. | PKC | 2021 | MPC | [论文](https://doi.org/10.1007/978-3-030-75248-4_4) · [ePrint](https://eprint.iacr.org/2021/260) |
| Mon$\\mathbb {Z}\_{2^{k}}$a: Fast Maliciously Secure Two Party Computation on $\\mathbb {Z}\_{2^{k}}$. | PKC | 2020 | MPC | [论文](https://doi.org/10.1007/978-3-030-45388-6_13) |

<a id="venue-journal-of-cryptology"></a>

## Journal of Cryptology（29）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| Universally Composable Almost-Everywhere Secure Computation. | Journal of Cryptology | 2026 | MPC | [论文](https://doi.org/10.1007/S00145-025-09565-2) · [ePrint](https://eprint.iacr.org/2021/1398) |
| Protecting Distributed Primitives Against Leakage: Equivocal Secret Sharing and more. | Journal of Cryptology | 2025 | MPC | [论文](https://doi.org/10.1007/S00145-024-09524-3) · [ePrint](https://eprint.iacr.org/2022/497) |
| Improved Universal Thresholdizer from Iterative Shamir Secret Sharing. | Journal of Cryptology | 2025 | MPC | [论文](https://doi.org/10.1007/S00145-024-09536-Z) · [ePrint](https://eprint.iacr.org/2023/545) |
| Randomness Recoverable Secret Sharing Schemes. | Journal of Cryptology | 2024 | MPC | [论文](https://doi.org/10.1007/S00145-024-09515-4) · [ePrint](https://eprint.iacr.org/2023/959) |
| Lightweight Asynchronous Verifiable Secret Sharing with Optimal Resilience. | Journal of Cryptology | 2024 | MPC | [论文](https://doi.org/10.1007/S00145-024-09505-6) · [ePrint](https://eprint.iacr.org/2023/536) |
| On the Power of an Honest Majority in Three-Party Computation Without Broadcast. | Journal of Cryptology / TCC | 2023 | MPC | [论文](https://doi.org/10.1007/978-3-030-64378-2_22) · [论文](https://doi.org/10.1007/S00145-023-09456-4) · [ePrint](https://eprint.iacr.org/2020/1170) |
| On the Communication Efficiency of Statistically Secure Asynchronous MPC with Optimal Resilience. | Journal of Cryptology | 2023 | MPC | [论文](https://doi.org/10.1007/S00145-023-09451-9) · [ePrint](https://eprint.iacr.org/2022/913) |
| Manticore: A Framework for Efficient Multiparty Computation Supporting Real Number and Boolean Arithmetic. | Journal of Cryptology | 2023 | MPC | [论文](https://doi.org/10.1007/S00145-023-09464-4) |
| High-Throughput Secure Three-Party Computation with an Honest Majority. | Journal of Cryptology | 2023 | MPC | [论文](https://doi.org/10.1007/S00145-023-09461-7) |
| Fast Large-Scale Honest-Majority MPC for Malicious Adversaries. | Journal of Cryptology | 2023 | MPC | [论文](https://doi.org/10.1007/S00145-023-09453-7) |
| Breaking and Fixing Garbled Circuits When a Gate has Duplicate Input Wires. | Journal of Cryptology | 2023 | MPC | [论文](https://doi.org/10.1007/S00145-023-09472-4) · [ePrint](https://eprint.iacr.org/2023/530) |
| Adaptively Secure MPC with Sublinear Communication Complexity. | Journal of Cryptology | 2023 | MPC | [论文](https://doi.org/10.1007/S00145-023-09446-6) |
| Actively Secure Garbled Circuits with Constant Communication Overhead in the Plain Model. | Journal of Cryptology | 2023 | MPC | [论文](https://doi.org/10.1007/S00145-023-09465-3) |
| ZK-PCPs from Leakage-Resilient Secret Sharing. | Journal of Cryptology | 2022 | MPC | [论文](https://doi.org/10.1007/S00145-022-09433-3) · [ePrint](https://eprint.iacr.org/2021/606) |
| TinyKeys: A New Approach to Efficient Multi-Party Computation. | Journal of Cryptology | 2022 | MPC | [论文](https://doi.org/10.1007/S00145-022-09423-5) |
| From Fairness to Full Security in Multiparty Computation. | Journal of Cryptology | 2022 | MPC | [论文](https://doi.org/10.1007/S00145-021-09415-X) · [arXiv](https://arxiv.org/abs/2105.00962) |
| Efficient Perfectly Secure Computation with Optimal Resilience. | Journal of Cryptology / TCC | 2022 | MPC | [论文](https://doi.org/10.1007/978-3-030-90453-1_3) · [论文](https://doi.org/10.1007/S00145-022-09434-2) · [ePrint](https://eprint.iacr.org/2021/1206) |
| Correction to: Unconditionally Secure Computation Against Low-Complexity Leakage. | Journal of Cryptology | 2022 | MPC | [论文](https://doi.org/10.1007/S00145-021-09412-0) · [论文](https://doi.org/10.1007/S00145-021-09417-9) |
| Unconditionally Secure Computation Against Low-Complexity Leakage. | Journal of Cryptology | 2021 | MPC | [论文](https://doi.org/10.1007/S00145-021-09402-2) |
| Round-Optimal Secure Multi-party Computation. | Journal of Cryptology | 2021 | MPC | [论文](https://doi.org/10.1007/S00145-021-09382-3) |
| On the Local Leakage Resilience of Linear Secret Sharing Schemes. | Journal of Cryptology | 2021 | MPC | [论文](https://doi.org/10.1007/S00145-021-09375-2) |
| On the Exact Round Complexity of Secure Three-Party Computation. | Journal of Cryptology | 2021 | MPC | [论文](https://doi.org/10.1007/S00145-021-09404-0) |
| On Abelian and Homomorphic Secret Sharing Schemes. | Journal of Cryptology | 2021 | MPC | [论文](https://doi.org/10.1007/S00145-021-09410-2) |
| High-Performance Multi-party Computation for Binary Circuits Based on Oblivious Transfer. | Journal of Cryptology | 2021 | MPC | [论文](https://doi.org/10.1007/S00145-021-09403-1) |
| On the Power of Secure Two-Party Computation. | Journal of Cryptology | 2020 | MPC | [论文](https://doi.org/10.1007/S00145-019-09314-2) |
| Low Cost Constant Round MPC Combining BMR and Oblivious Transfer. | Journal of Cryptology | 2020 | MPC | [论文](https://doi.org/10.1007/S00145-020-09355-Y) |
| Feasibility and Infeasibility of Secure Computation with Malicious PUFs. | Journal of Cryptology | 2020 | MPC | [论文](https://doi.org/10.1007/S00145-019-09329-9) |
| An Optimal Distributed Discrete Log Protocol with Applications to Homomorphic Secret Sharing. | Journal of Cryptology | 2020 | MPC | [论文](https://doi.org/10.1007/S00145-019-09330-2) |
| 1/p-Secure Multiparty Computation without an Honest Majority and the Best of Both Worlds. | Journal of Cryptology | 2020 | MPC | [论文](https://doi.org/10.1007/S00145-020-09354-Z) |

<a id="venue-tches"></a>

## TCHES（11）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| Loricae: Upgrading and Optimizing Multi-Party Computation Protocols with Filmy Hardware Enclaves. | TCHES | 2026 | MPC + TEE | [论文](https://doi.org/10.46586/TCHES.V2026.I2.73-105) |
| It's TEEtime: Secure Interrupt Isolation for Normal-world Enclaves on Arm. | TCHES | 2026 | TEE | [论文](https://doi.org/10.46586/TCHES.V2026.I1.135-160) |
| Secure and efficient transciphering for FHE-based MPC. | TCHES | 2025 | MPC | [论文](https://doi.org/10.46586/TCHES.V2025.I3.745-780) · [ePrint](https://eprint.iacr.org/2024/1702) |
| POTA: A Pipelined Oblivious Transfer Acceleration Architecture for Secure Multi-Party Computation. | TCHES | 2025 | MPC | [论文](https://doi.org/10.46586/TCHES.V2025.I3.262-292) |
| Dash: Accelerating Distributed Private Convolutional Neural Network Inference with Arithmetic Garbled Circuits. | TCHES | 2025 | MPC | [论文](https://doi.org/10.46586/TCHES.V2025.I1.420-449) · [arXiv](https://arxiv.org/abs/2302.06361) |
| All-You-Can-Compute: Packed Secret Sharing for Combined Resilience. | TCHES | 2025 | MPC | [论文](https://doi.org/10.46586/TCHES.V2025.I2.420-459) · [ePrint](https://eprint.iacr.org/2025/035) |
| SEV-Step A Single-Stepping Framework for AMD-SEV. | TCHES | 2024 | TEE | [论文](https://doi.org/10.46586/TCHES.V2024.I1.180-206) · [arXiv](https://arxiv.org/abs/2307.14757) |
| Garbled Circuits from an SCA Perspective Free XOR can be Quite Expensive. . . | TCHES | 2023 | MPC | [论文](https://doi.org/10.46586/TCHES.V2023.I2.54-79) · [ePrint](https://eprint.iacr.org/2022/901) |
| Composite Enclaves: Towards Disaggregated Trusted Execution. | TCHES | 2022 | TEE | [论文](https://doi.org/10.46586/TCHES.V2022.I1.630-656) · [arXiv](https://arxiv.org/abs/2010.10416) |
| ROTed: Random Oblivious Transfer for embedded devices. | TCHES | 2021 | MPC | [论文](https://doi.org/10.46586/TCHES.V2021.I4.215-238) · [ePrint](https://eprint.iacr.org/2021/935) |
| Bluethunder: A 2-level Directional Predictor Based Side-Channel Attack against SGX. | TCHES | 2020 | TEE | [论文](https://doi.org/10.13154/TCHES.V2020.I1.321-347) |

<a id="venue-ieee-s-p"></a>

## IEEE S&amp;P（43）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| TEE.Fail: Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition. | IEEE S&amp;P | 2026 | TEE | [论文](https://doi.org/10.1109/SP63933.2026.00101) |
| TDXRay: Microarchitectural Side-Channel Analysis of Intel TDX for Real-World Workloads. | IEEE S&amp;P | 2026 | TEE | [论文](https://doi.org/10.1109/SP63933.2026.00170) |
| Practical Multi-Party Private Set Intersection with Reducible Zero-Sharing. | IEEE S&amp;P | 2026 | MPC | [论文](https://doi.org/10.1109/SP63933.2026.00006) · [ePrint](https://eprint.iacr.org/2025/2019) |
| Optimistic Asynchronous Dynamic-Committee Proactive Secret Sharing. | IEEE S&amp;P | 2026 | MPC | [论文](https://doi.org/10.1109/SP63933.2026.00243) · [ePrint](https://eprint.iacr.org/2025/880) |
| GoSSamer: Lightweight and Linear-Communication Asynchronous (Dynamic Proactive) Secret Sharing and the Applications. | IEEE S&amp;P | 2026 | MPC | [论文](https://doi.org/10.1109/SP63933.2026.00185) · [ePrint](https://eprint.iacr.org/2025/1516) |
| Efficient Fuzzy Private Set Intersection from Secret-Shared OPRF. | IEEE S&amp;P | 2026 | MPC | [论文](https://doi.org/10.1109/SP63933.2026.00172) · [arXiv](https://arxiv.org/abs/2604.14909) |
| Decor: Delegated Computation on Randomness for Secure Evaluation of Nonlinear Functions. | IEEE S&amp;P | 2026 | MPC | [论文](https://doi.org/10.1109/SP63933.2026.00256) |
| Concretely-Efficient Multi-Key Homomorphic Secret Sharing and Applications. | IEEE S&amp;P | 2026 | MPC | [论文](https://doi.org/10.1109/SP63933.2026.00004) · [ePrint](https://eprint.iacr.org/2025/1803) |
| BreakFAST: Confused Deputy Attack on Infinity Fabric to Break AMD SEV-SNP. | IEEE S&amp;P | 2026 | TEE | [论文](https://doi.org/10.1109/SP63933.2026.00259) |
| Battering RAM: Low-Cost Interposer Attacks on Confidential Computing via Dynamic Memory Aliasing. | IEEE S&amp;P | 2026 | TEE | [论文](https://doi.org/10.1109/SP63933.2026.00052) |
| AEX-NStep: Probabilistic Interrupt Counting Attacks on Intel SGX. | IEEE S&amp;P | 2026 | TEE | [论文](https://doi.org/10.1109/SP63933.2026.00035) · [arXiv](https://arxiv.org/abs/2510.14675) |
| Verifiable Secret Sharing Simplified. | IEEE S&amp;P | 2025 | MPC | [论文](https://doi.org/10.1109/SP61157.2025.00046) · [ePrint](https://eprint.iacr.org/2023/1196) |
| Towards Efficient and Practical Multi-party Computation under Inconsistent Trust in TEEs. | IEEE S&amp;P | 2025 | MPC | [论文](https://doi.org/10.1109/SP61157.2025.00185) |
| SHARK: Actively Secure Inference Using Function Secret Sharing. | IEEE S&amp;P | 2025 | MPC | [论文](https://doi.org/10.1109/SP61157.2025.00175) · [ePrint](https://eprint.iacr.org/2025/716) |
| Rushing at SPDZ: On the Practical Security of Malicious MPC Implementations. | IEEE S&amp;P | 2025 | MPC | [论文](https://doi.org/10.1109/SP61157.2025.00176) · [ePrint](https://eprint.iacr.org/2025/789) |
| Portal: Fast and Secure Device Access with Arm CCA for Modern Arm Mobile System-on-Chips (SoCs). | IEEE S&amp;P | 2025 | TEE | [论文](https://doi.org/10.1109/SP61157.2025.00013) |
| Is MPC Secure? Leveraging Neural Network Classifiers to Detect Data Leakage Vulnerabilities in MPC Implementations. | IEEE S&amp;P | 2025 | MPC | [论文](https://doi.org/10.1109/SP61157.2025.00181) |
| Highly Efficient Actively Secure Two-Party Computation with One-Bit Advantage Bound. | IEEE S&amp;P | 2025 | MPC | [论文](https://doi.org/10.1109/SP61157.2025.00183) · [ePrint](https://eprint.iacr.org/2025/614) |
| BadRAM: Practical Memory Aliasing Attacks on Trusted Execution Environments. | IEEE S&amp;P | 2025 | TEE | [论文](https://doi.org/10.1109/SP61157.2025.00104) |
| WeSee: Using Malicious \#VC Interrupts to Break AMD SEV-SNP. | IEEE S&amp;P | 2024 | TEE | [论文](https://doi.org/10.1109/SP54263.2024.00262) · [arXiv](https://arxiv.org/abs/2404.03526) |
| SoK: SGX.Fail: How Stuff Gets eXposed. | IEEE S&amp;P | 2024 | TEE | [论文](https://doi.org/10.1109/SP54263.2024.00260) |
| Pandora: Principled Symbolic Validation of Intel SGX Enclave Runtimes. | IEEE S&amp;P | 2024 | TEE | [论文](https://doi.org/10.1109/SP54263.2024.00090) |
| On (the Lack of) Code Confidentiality in Trusted Execution Environments. | IEEE S&amp;P | 2024 | TEE | [论文](https://doi.org/10.1109/SP54263.2024.00259) · [arXiv](https://arxiv.org/abs/2212.07899) |
| NodeGuard: A Highly Efficient Two-Party Computation Framework for Training Large-Scale Gradient Boosting Decision Tree. | IEEE S&amp;P | 2024 | MPC | [论文](https://doi.org/10.1109/SPW63631.2024.00015) · [ePrint](https://eprint.iacr.org/2024/535) |
| No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML. | IEEE S&amp;P | 2024 | TEE | [论文](https://doi.org/10.1109/SP54263.2024.00052) · [arXiv](https://arxiv.org/abs/2310.07152) |
| MPC-in-the-Head Framework without Repetition and its Applications to the Lattice-based Cryptography. | IEEE S&amp;P | 2024 | MPC | [论文](https://doi.org/10.1109/SP54263.2024.00157) · [ePrint](https://eprint.iacr.org/2024/1591) |
| GAuV: A Graph-Based Automated Verification Framework for Perfect Semi-Honest Security of Multiparty Computation Protocols. | IEEE S&amp;P | 2024 | MPC | [论文](https://doi.org/10.1109/SP54263.2024.00131) · [ePrint](https://eprint.iacr.org/2024/1078) |
| Efficient Actively Secure DPF and RAM-based 2PC with One-Bit Leakage. | IEEE S&amp;P | 2024 | MPC | [论文](https://doi.org/10.1109/SP54263.2024.00205) · [ePrint](https://eprint.iacr.org/2024/426) |
| Don't Eject the Impostor: Fast Three-Party Computation With a Known Cheater. | IEEE S&amp;P | 2024 | MPC | [论文](https://doi.org/10.1109/SP54263.2024.00164) |
| Private Access Control for Function Secret Sharing. | IEEE S&amp;P | 2023 | MPC | [论文](https://doi.org/10.1109/SP46215.2023.10179295) · [ePrint](https://eprint.iacr.org/2022/1707) |
| vSGX: Virtualizing SGX Enclaves on AMD SEV. | IEEE S&amp;P | 2022 | TEE | [论文](https://doi.org/10.1109/SP46214.2022.9833694) |
| Waldo: A Private Time-Series Database from Function Secret Sharing. | IEEE S&amp;P | 2022 | MPC | [论文](https://doi.org/10.1109/SP46214.2022.9833611) · [ePrint](https://eprint.iacr.org/2021/1661) |
| Smile: Secure Memory Introspection for Live Enclave. | IEEE S&amp;P | 2022 | TEE | [论文](https://doi.org/10.1109/SP46214.2022.9833714) |
| SecFloat: Accurate Floating-Point meets Secure 2-Party Computation. | IEEE S&amp;P | 2022 | MPC | [论文](https://doi.org/10.1109/SP46214.2022.9833697) · [ePrint](https://eprint.iacr.org/2022/322) |
| RT-TEE: Real-time System Availability for Cyber-physical Systems using ARM TrustZone. | IEEE S&amp;P | 2022 | TEE | [论文](https://doi.org/10.1109/SP46214.2022.9833604) |
| Publicly Accountable Robust Multi-Party Computation. | IEEE S&amp;P | 2022 | MPC | [论文](https://doi.org/10.1109/SP46214.2022.9833608) · [ePrint](https://eprint.iacr.org/2022/436) |
| COBRA: Dynamic Proactive Secret Sharing for Confidential BFT Services. | IEEE S&amp;P | 2022 | MPC | [论文](https://doi.org/10.1109/SP46214.2022.9833658) |
| Abusing Trust: Mobile Kernel Subversion via TrustZone Rootkits. | IEEE S&amp;P | 2022 | TEE | [论文](https://doi.org/10.1109/SPW54247.2022.9833891) |
| A Systematic Look at Ciphertext Side Channels on AMD SEV-SNP. | IEEE S&amp;P | 2022 | TEE | [论文](https://doi.org/10.1109/SP46214.2022.9833768) |
| SoK: Understanding the Prevailing Security Vulnerabilities in TrustZone-assisted TEE Systems. | IEEE S&amp;P | 2020 | TEE | [论文](https://doi.org/10.1109/SP40000.2020.00061) |
| Plundervolt: Software-based Fault Injection Attacks against Intel SGX. | IEEE S&amp;P | 2020 | TEE | [论文](https://doi.org/10.1109/SP40000.2020.00057) |
| Enabling Rack-scale Confidential Computing using Heterogeneous Trusted Execution Environment. | IEEE S&amp;P | 2020 | TEE | [论文](https://doi.org/10.1109/SP40000.2020.00054) |
| Efficient and Secure Multiparty Computation from Fixed-Key Block Ciphers. | IEEE S&amp;P | 2020 | MPC | [论文](https://doi.org/10.1109/SP40000.2020.00016) |

<a id="venue-acm-ccs"></a>

## ACM CCS（47）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| WireTap: Breaking Server SGX via DRAM Bus Interposition. | ACM CCS | 2025 | TEE | [论文](https://doi.org/10.1145/3719027.3765204) |
| Velox: Scalable Fair Asynchronous MPC from Lightweight Cryptography. | ACM CCS | 2025 | MPC | [论文](https://doi.org/10.1145/3719027.3765114) · [ePrint](https://eprint.iacr.org/2025/1630) |
| RMPocalypse: How a Catch-22 Breaks AMD SEV-SNP. | ACM CCS | 2025 | TEE | [论文](https://doi.org/10.1145/3719027.3765233) |
| PULSE: Parallel Private Set Union for Large-Scale Entities. | ACM CCS | 2025 | MPC | [论文](https://doi.org/10.1145/3719027.3765108) · [ePrint](https://eprint.iacr.org/2025/790) |
| Heracles: Chosen Plaintext Attack on AMD SEV-SNP. | ACM CCS | 2025 | TEE | [论文](https://doi.org/10.1145/3719027.3765209) |
| GPU Travelling: Efficient Confidential Collaborative Training with TEE-Enabled GPUs. | ACM CCS | 2025 | TEE | [论文](https://doi.org/10.1145/3719027.3765029) |
| Attestable Builds: Compiling Verifiable Binaries on Untrusted Systems using Trusted Execution Environments. | ACM CCS | 2025 | TEE | [论文](https://doi.org/10.1145/3719027.3765128) · [arXiv](https://arxiv.org/abs/2505.02521) |
| A System Framework to Symbolically Explore Intel TDX Module Execution. | ACM CCS | 2025 | TEE | [论文](https://doi.org/10.1145/3719027.3765212) |
| Unbalanced Private Set Union with Reduced Computation and Communication. | ACM CCS | 2024 | MPC | [论文](https://doi.org/10.1145/3658644.3690308) · [ePrint](https://eprint.iacr.org/2024/1340) |
| Trusted Execution Environments for Quantum Computers. | ACM CCS | 2024 | TEE | [论文](https://doi.org/10.1145/3658644.3690855) |
| TDXdown: Single-Stepping and Instruction Counting Attacks against Intel TDX. | ACM CCS | 2024 | TEE | [论文](https://doi.org/10.1145/3658644.3690230) |
| Specification and Verification of Strong Timing Isolation of Hardware Enclaves. | ACM CCS | 2024 | TEE | [论文](https://doi.org/10.1145/3658644.3690203) |
| Secure Sorting and Selection via Function Secret Sharing. | ACM CCS | 2024 | MPC | [论文](https://doi.org/10.1145/3658644.3690359) |
| Secure Multiparty Computation with Lazy Sharing. | ACM CCS | 2024 | MPC | [论文](https://doi.org/10.1145/3658644.3690207) · [ePrint](https://eprint.iacr.org/2024/1347) |
| Secret Sharing with Snitching. | ACM CCS | 2024 | MPC | [论文](https://doi.org/10.1145/3658644.3690296) · [ePrint](https://eprint.iacr.org/2024/1610) |
| Poster: Multiparty Private Set Intersection from Multiparty Homomorphic Encryption. | ACM CCS | 2024 | MPC | [论文](https://doi.org/10.1145/3658644.3691405) |
| Poster: A Secure Multiparty Computation Platform for Squeaky-Clean Data Rooms. | ACM CCS | 2024 | MPC | [论文](https://doi.org/10.1145/3658644.3691371) |
| Gramine-TDX: A Lightweight OS Kernel for Confidential VMs. | ACM CCS | 2024 | TEE | [论文](https://doi.org/10.1145/3658644.3690323) |
| Efficient Secret Sharing for Large-Scale Applications. | ACM CCS | 2024 | MPC | [论文](https://doi.org/10.1145/3658644.3670379) · [ePrint](https://eprint.iacr.org/2024/1045) |
| Efficient Scalable Multi-Party Private Set Intersection(-Variants) from Bicentric Zero-Sharing. | ACM CCS | 2024 | MPC | [论文](https://doi.org/10.1145/3658644.3690245) |
| Coral: Maliciously Secure Computation Framework for Packed and Mixed Circuits. | ACM CCS | 2024 | MPC | [论文](https://doi.org/10.1145/3658644.3690223) · [ePrint](https://eprint.iacr.org/2024/1372) |
| Actively Secure Private Set Intersection in the Client-Server Setting. | ACM CCS | 2024 | MPC | [论文](https://doi.org/10.1145/3658644.3690349) · [ePrint](https://eprint.iacr.org/2024/570) |
| AITIA: Efficient Secure Computation of Bivariate Causal Discovery. | ACM CCS | 2024 | MPC | [论文](https://doi.org/10.1145/3658644.3670337) · [ePrint](https://eprint.iacr.org/2024/1065) |
| SymGX: Detecting Cross-boundary Pointer Vulnerabilities of SGX Applications via Static Symbolic Execution. | ACM CCS | 2023 | TEE | [论文](https://doi.org/10.1145/3576915.3623213) |
| Ramen: Souper Fast Three-Party Computation for RAM Programs. | ACM CCS | 2023 | MPC | [论文](https://doi.org/10.1145/3576915.3623115) · [ePrint](https://eprint.iacr.org/2023/310) |
| Linear Communication in Malicious Majority MPC. | ACM CCS | 2023 | MPC | [论文](https://doi.org/10.1145/3576915.3623162) · [ePrint](https://eprint.iacr.org/2022/781) |
| Let's Go Eevee! A Friendly and Suitable Family of AEAD Modes for IoT-to-Cloud Secure Computation. | ACM CCS | 2023 | MPC | [论文](https://doi.org/10.1145/3576915.3623091) · [ePrint](https://eprint.iacr.org/2023/1361) |
| Fast Unbalanced Private Set Union from Fully Homomorphic Encryption. | ACM CCS | 2023 | MPC | [论文](https://doi.org/10.1145/3576915.3623064) · [ePrint](https://eprint.iacr.org/2022/653) |
| Efficient Multiparty Probabilistic Threshold Private Set Intersection. | ACM CCS | 2023 | MPC | [论文](https://doi.org/10.1145/3576915.3623158) |
| COMBINE: COMpilation and Backend-INdependent vEctorization for Multi-Party Computation. | ACM CCS | 2023 | MPC | [论文](https://doi.org/10.1145/3576915.3623181) · [ePrint](https://eprint.iacr.org/2023/089) |
| TurboPack: Honest Majority MPC with Constant Online Communication. | ACM CCS | 2022 | MPC | [论文](https://doi.org/10.1145/3548606.3560633) · [ePrint](https://eprint.iacr.org/2022/1316) |
| STAR: Secret Sharing for Private Threshold Aggregation Reporting. | ACM CCS | 2022 | MPC | [论文](https://doi.org/10.1145/3548606.3560631) · [arXiv](https://arxiv.org/abs/2109.10074) |
| Laconic Private Set-Intersection From Pairings. | ACM CCS | 2022 | MPC | [论文](https://doi.org/10.1145/3548606.3560642) · [ePrint](https://eprint.iacr.org/2022/529) |
| Fast Fully Secure Multi-Party Computation over Any Ring with Two-Thirds Honest Majority. | ACM CCS | 2022 | MPC | [论文](https://doi.org/10.1145/3548606.3559389) · [ePrint](https://eprint.iacr.org/2022/623) |
| Cerberus: A Formal Approach to Secure and Efficient Enclave Memory Sharing. | ACM CCS | 2022 | TEE | [论文](https://doi.org/10.1145/3548606.3560595) · [arXiv](https://arxiv.org/abs/2209.15253) |
| SmashEx: Smashing SGX Enclaves Using Exceptions. | ACM CCS | 2021 | TEE | [论文](https://doi.org/10.1145/3460120.3484821) · [arXiv](https://arxiv.org/abs/2110.06657) |
| Simple, Fast Malicious Multiparty Private Set Intersection. | ACM CCS | 2021 | MPC | [论文](https://doi.org/10.1145/3460120.3484772) · [ePrint](https://eprint.iacr.org/2021/1221) |
| Secure Multi-party Computation of Differentially Private Heavy Hitters. | ACM CCS | 2021 | MPC | [论文](https://doi.org/10.1145/3460120.3484557) |
| One Glitch to Rule Them All: Fault Injection Attacks Against AMD's Secure Encrypted Virtualization. | ACM CCS | 2021 | TEE | [论文](https://doi.org/10.1145/3460120.3484779) · [arXiv](https://arxiv.org/abs/2108.04575) |
| Machine-checked ZKP for NP relations: Formally Verified Security Proofs and Implementations of MPC-in-the-Head. | ACM CCS | 2021 | MPC | [论文](https://doi.org/10.1145/3460120.3484771) · [arXiv](https://arxiv.org/abs/2104.05516) · [ePrint](https://eprint.iacr.org/2021/1149) |
| MPC-Friendly Commitments for Publicly Verifiable Covert Security. | ACM CCS | 2021 | MPC | [论文](https://doi.org/10.1145/3460120.3485375) · [arXiv](https://arxiv.org/abs/2109.07461) · [ePrint](https://eprint.iacr.org/2022/102) |
| CrossLine: Breaking "Security-by-Crash" based Memory Isolation in AMD SEV. | ACM CCS | 2021 | TEE | [论文](https://doi.org/10.1145/3460120.3485253) · [arXiv](https://arxiv.org/abs/2008.00146) |
| Compact and Malicious Private Set Intersection for Small Sets. | ACM CCS | 2021 | MPC | [论文](https://doi.org/10.1145/3460120.3484778) · [ePrint](https://eprint.iacr.org/2021/1159) |
| TRUSTORE: Side-Channel Resistant Storage for SGX using Intel Hybrid CPU-FPGA. | ACM CCS | 2020 | TEE | [论文](https://doi.org/10.1145/3372297.3417265) |
| More Efficient MPC from Improved Triple Generation and Authenticated Garbling. | ACM CCS | 2020 | MPC | [论文](https://doi.org/10.1145/3372297.3417285) |
| MP-SPDZ: A Versatile Framework for Multi-Party Computation. | ACM CCS | 2020 | MPC | [论文](https://doi.org/10.1145/3372297.3417872) · [ePrint](https://eprint.iacr.org/2020/521) |
| Is the Classical GMW Paradigm Practical? The Case of Non-Interactive Actively Secure 2PC. | ACM CCS | 2020 | MPC | [论文](https://doi.org/10.1145/3372297.3423366) |

<a id="venue-usenix-security"></a>

## USENIX Security（60）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| Transparent Attested DNS for Confidential Computing Services. | USENIX Security | 2025 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity25/presentation/delignat-lavaud) · [arXiv](https://arxiv.org/abs/2503.14611) |
| TLBlur: Compiler-Assisted Automated Hardening against Controlled Channels on Off-the-Shelf Intel SGX Platforms. | USENIX Security | 2025 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity25/presentation/vanoverloop) |
| TDXploit: Novel Techniques for Single-Stepping and Cache Attacks on Intel TDX. | USENIX Security | 2025 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity25/presentation/rauscher) |
| SEAF: Secure Evaluation on Activation Functions with Dynamic Precision for Secure Two-Party Inference. | USENIX Security | 2025 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity25/presentation/guo-hao-seaf) · [ePrint](https://eprint.iacr.org/2025/1111) |
| Private Set Intersection and other Set Operations in the Third Party Setting. | USENIX Security | 2025 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity25/presentation/yeo) · [ePrint](https://eprint.iacr.org/2025/1328) |
| Improved Secure Two-party Computation from a Geometric Perspective. | USENIX Security | 2025 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity25/presentation/guo-hao-improved) · [ePrint](https://eprint.iacr.org/2025/200) |
| Game of Arrows: On the (In-)Security of Weight Obfuscation for On-Device TEE-Shielded LLM Partition Algorithms. | USENIX Security | 2025 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-pengli) |
| Fast Enhanced Private Set Union in the Balanced and Unbalanced Scenarios. | USENIX Security | 2025 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity25/presentation/tu) · [ePrint](https://eprint.iacr.org/2025/827) |
| Enabling Low-Cost Secure Computing on Untrusted In-Memory Architectures. | USENIX Security | 2025 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity25/presentation/ghinani) · [arXiv](https://arxiv.org/abs/2501.17292) |
| Efficient Multi-Party Private Set Union Without Non-Collusion Assumptions. | USENIX Security | 2025 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity25/presentation/dong-minglang) · [ePrint](https://eprint.iacr.org/2024/1146) |
| Efficient 2PC for Constant Round Secure Equality Testing and Comparison. | USENIX Security | 2025 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity25/presentation/lu) · [ePrint](https://eprint.iacr.org/2024/949) |
| Dorami: Privilege Separating Security Monitor on RISC-V TEEs. | USENIX Security | 2025 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity25/presentation/kuhne) · [arXiv](https://arxiv.org/abs/2410.03653) |
| Scalable Private Set Union, with Stronger Security. | USENIX Security | 2024 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity24/presentation/jia-yanxue) · [ePrint](https://eprint.iacr.org/2024/922) |
| Scalable Multi-Party Computation Protocols for Machine Learning in the Honest-Majority Setting. | USENIX Security | 2024 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity24/presentation/liu-fengrun) |
| PEPSI: Practically Efficient Private Set Intersection in the Unbalanced Setting. | USENIX Security | 2024 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity24/presentation/mahdavi) · [arXiv](https://arxiv.org/abs/2310.14565) |
| O-Ring and K-Star: Efficient Multi-party Private Set Intersection. | USENIX Security | 2024 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity24/presentation/wu-mingli) |
| GlobalConfusion: TrustZone Trusted Application 0-Days by Design. | USENIX Security | 2024 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity24/presentation/busch-globalconfusion) |
| Fast RS-IOP Multivariate Polynomial Commitments and Verifiable Secret Sharing. | USENIX Security | 2024 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity24/presentation/zhang-zongyang) |
| Abuse Reporting for Metadata-Hiding Communication Based on Secret Sharing. | USENIX Security | 2024 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity24/presentation/eskandarian) · [ePrint](https://eprint.iacr.org/2023/1144) |
| ACAI: Protecting Accelerator Execution with Arm Confidential Computing Architecture. | USENIX Security | 2024 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity24/presentation/sridhara) · [arXiv](https://arxiv.org/abs/2305.15986) |
| TVA: A multi-party computation system for secure and expressive time series analytics. | USENIX Security | 2023 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity23/presentation/faisal) · [ePrint](https://eprint.iacr.org/2023/1120) |
| Squirrel: A Scalable Secure Two-Party Computation Framework for Training Gradient Boosting Decision Tree. | USENIX Security | 2023 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity23/presentation/lu) · [ePrint](https://eprint.iacr.org/2023/527) |
| SHELTER: Extending Arm CCA with Isolation in User Space. | USENIX Security | 2023 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity23/presentation/zhang-yiming) |
| Reusable Enclaves for Confidential Serverless Computing. | USENIX Security | 2023 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity23/presentation/zhao-shixuan) |
| Oops..! I Glitched It Again! How to Multi-Glitch the Glitching-Protections on ARM TrustZone-M. | USENIX Security | 2023 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity23/presentation/sass) · [arXiv](https://arxiv.org/abs/2302.06932) |
| Linear Private Set Union from Multi-Query Reverse Private Membership Test. | USENIX Security | 2023 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity23/presentation/zhang-cong) · [ePrint](https://eprint.iacr.org/2022/358) |
| EnigMap: External-Memory Oblivious Map for Secure Enclaves. | USENIX Security | 2023 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity23/presentation/tinoco) · [ePrint](https://eprint.iacr.org/2022/1083) |
| Efficient Unbalanced Private Set Intersection Cardinality and User-friendly Privacy-preserving Contact Tracing. | USENIX Security | 2023 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity23/presentation/wu-mingli) |
| Efficient 3PC for Binary Circuits with Application to Maliciously-Secure DNN Inference. | USENIX Security | 2023 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity23/presentation/li-yun) · [ePrint](https://eprint.iacr.org/2023/909) |
| Distance-Aware Private Set Intersection. | USENIX Security | 2023 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity23/presentation/chakraborti-intersection) · [arXiv](https://arxiv.org/abs/2112.14737) |
| AEX-Notify: Thwarting Precise Single-Stepping Attacks through Interrupt Awareness for Intel SGX Enclaves. | USENIX Security | 2023 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity23/presentation/constable) |
| A Verified Confidential Computing as a Service Framework for Privacy Preservation. | USENIX Security | 2023 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity23/presentation/chen-hongbo) |
| Trust Dies in Darkness: Shedding Light on Samsung's TrustZone Keymaster Design. | USENIX Security | 2022 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity22/presentation/shakevsky) · [ePrint](https://eprint.iacr.org/2022/208) |
| Shuffle-based Private Set Union: Faster and More Secure. | USENIX Security | 2022 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity22/presentation/jia) · [ePrint](https://eprint.iacr.org/2022/157) |
| SGXLock: Towards Efficiently Establishing Mutual Distrust Between Host Application and Enclave for SGX. | USENIX Security | 2022 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity22/presentation/chen-yuan) |
| SGXFuzz: Efficiently Synthesizing Nested Structures for SGX Enclave Fuzzing. | USENIX Security | 2022 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity22/presentation/cloosters) |
| Repurposing Segmentation as a Practical LVI-NULL Mitigation in SGX. | USENIX Security | 2022 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity22/presentation/giner) |
| ReZone: Disarming TrustZone with TEE Privilege Reduction. | USENIX Security | 2022 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity22/presentation/cerdeira) · [arXiv](https://arxiv.org/abs/2203.01025) |
| Piranha: A GPU Platform for Secure Computation. | USENIX Security | 2022 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity22/presentation/watson) · [ePrint](https://eprint.iacr.org/2022/892) · [Code](https://github.com/ucbrise/piranha) |
| Minefield: A Software-only Protection for SGX Enclaves against DVFS Attacks. | USENIX Security | 2022 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity22/presentation/kogler-minefield) |
| MAGE: Mutual Attestation for a Group of Enclaves without Trusted Third Parties. | USENIX Security | 2022 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity22/presentation/chen-guoxing) · [arXiv](https://arxiv.org/abs/2008.09501) |
| Estimating Incidental Collection in Foreign Intelligence Surveillance: Large-Scale Multiparty Private Set Intersection with Union and Sum. | USENIX Security | 2022 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity22/presentation/kulshrestha) |
| Composable Cachelets: Protecting Enclaves from Cache Side-Channel Attacks. | USENIX Security | 2022 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity22/presentation/townley) |
| A Hardware-Software Co-design for Efficient Intra-Enclave Isolation. | USENIX Security | 2022 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity22/presentation/gu-jinyu) |
| VoltPillager: Hardware-based fault injection attacks against Intel SGX Enclaves using the SVID voltage scaling interface. | USENIX Security | 2021 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity21/presentation/chen-zitai) |
| Senate: A Maliciously-Secure MPC Platform for Collaborative Analytics. | USENIX Security | 2021 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity21/presentation/poddar) · [arXiv](https://arxiv.org/abs/2010.13752) · [ePrint](https://eprint.iacr.org/2020/1350) |
| Fuzzy Labeled Private Set Intersection with Applications to Private Real-Time Biometric Search. | USENIX Security | 2021 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity21/presentation/uzun) |
| Frontal Attack: Leaking Control-Flow in SGX via the CPU Frontend. | USENIX Security | 2021 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity21/presentation/puddu) · [arXiv](https://arxiv.org/abs/2005.11516) |
| Fantastic Four: Honest-Majority Four-Party Secure Computation With Malicious Security. | USENIX Security | 2021 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity21/presentation/dalskov) · [ePrint](https://eprint.iacr.org/2020/1330) |
| CURE: A Security Architecture with CUstomizable and Resilient Enclaves. | USENIX Security | 2021 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity21/presentation/bahmani) · [arXiv](https://arxiv.org/abs/2010.15866) |
| CIPHERLEAKS: Breaking Constant-time Cryptography on AMD SEV via the Ciphertext Side Channel. | USENIX Security | 2021 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity21/presentation/li-mengyuan) |
| ABY2.0: Improved Mixed-Protocol Secure Two-Party Computation. | USENIX Security | 2021 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity21/presentation/patra) · [ePrint](https://eprint.iacr.org/2020/1225) |
| Unearthing the TrustedCore: A Critical Review on Huawei's Trusted Execution Environment. | USENIX Security | 2020 | TEE | [论文](https://www.usenix.org/conference/woot20/presentation/busch) |
| TeeRex: Discovery and Exploitation of Memory Corruption Vulnerabilities in SGX Enclaves. | USENIX Security | 2020 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity20/presentation/cloosters) · [arXiv](https://arxiv.org/abs/2007.07586) |
| Secure Multi-party Computation of Differentially Private Median. | USENIX Security | 2020 | MPC | [论文](https://www.usenix.org/conference/usenixsecurity20/presentation/boehler) |
| SENG, the SGX-Enforcing Network Gateway: Authorizing Communication from Shielded Clients. | USENIX Security | 2020 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity20/presentation/schwarz) |
| PARTEMU: Enabling Dynamic Analysis of Real-World TrustZone Software Using Emulation. | USENIX Security | 2020 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity20/presentation/harrison) |
| HybCache: Hybrid Side-Channel-Resilient Caches for Trusted Execution Environments. | USENIX Security | 2020 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity20/presentation/dessouky) |
| Civet: An Efficient Java Partitioning Framework for Hardware Enclaves. | USENIX Security | 2020 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity20/presentation/tsai) |
| An Off-Chip Attack on Hardware Enclaves via the Memory Bus. | USENIX Security | 2020 | TEE | [论文](https://www.usenix.org/conference/usenixsecurity20/presentation/lee-dayeol) |

<a id="venue-ndss"></a>

## NDSS（25）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| cwPSU: Efficient Unbalanced Private Set Union via Constant-weight Codes. | NDSS | 2026 | MPC | [论文](https://www.ndss-symposium.org/ndss-paper/cwpsu-efficient-unbalanced-private-set-union-via-constant-weight-codes/) |
| UIEE: Secure and Efficient User-space Isolated Execution Environment for Embedded TEE Systems. | NDSS | 2026 | TEE | [论文](https://www.ndss-symposium.org/ndss-paper/uiee-secure-and-efficient-user-space-isolated-execution-environment-for-embedded-tee-systems/) |
| RoundRole: Unlocking the Efficiency of Multi-party Computation with Bandwidth-aware Execution. | NDSS | 2026 | MPC | [论文](https://www.ndss-symposium.org/ndss-paper/roundrole-unlocking-the-efficiency-of-multi-party-computation-with-bandwidth-aware-execution/) |
| Practical Traceable Over-Threshold Multi-Party Private Set Intersection. | NDSS | 2026 | MPC | [论文](https://www.ndss-symposium.org/ndss-paper/practical-traceable-over-threshold-multi-party-private-set-intersection/) · [arXiv](https://arxiv.org/abs/2512.24652) |
| MinBucket MPSI: Breaking the Max-Size Bottleneck in Multi-Party Private Set Intersection. | NDSS | 2026 | MPC | [论文](https://www.ndss-symposium.org/ndss-paper/minbucket-mpsi-breaking-the-max-size-bottleneck-in-multi-party-private-set-intersection/) |
| Faster Than Ever: A New Lightweight Private Set Intersection and Its Variants. | NDSS | 2026 | MPC | [论文](https://www.ndss-symposium.org/ndss-paper/faster-than-ever-a-new-lightweight-private-set-intersection-and-its-variants/) |
| EXIA: Trusted Transitions for Enclaves via External-Input Attestation. | NDSS | 2026 | TEE | [论文](https://www.ndss-symposium.org/ndss-paper/exia-trusted-transitions-for-enclaves-via-external-input-attestation/) |
| DNN Latency Sequencing: Extracting DNN Architectures from Intel SGX Enclaves with Single-Stepping Attacks. | NDSS | 2026 | TEE | [论文](https://www.ndss-symposium.org/ndss-paper/dnn-latency-sequencing-extracting-dnn-architectures-from-intel-sgx-enclaves-with-single-stepping-attacks/) |
| The Road to Trust: Building Enclaves within Confidential VMs. | NDSS | 2025 | TEE | [论文](https://www.ndss-symposium.org/ndss-paper/the-road-to-trust-building-enclaves-within-confidential-vms/) · [arXiv](https://arxiv.org/abs/2402.11438) |
| SCRUTINIZER: Towards Secure Forensics on Compromised TrustZone. | NDSS | 2025 | TEE | [论文](https://www.ndss-symposium.org/ndss-paper/scrutinizer-towards-secure-forensics-on-compromised-trustzone/) |
| Recurrent Private Set Intersection for Unbalanced Databases with Cuckoo Hashing and Leveled FHE. | NDSS | 2025 | MPC | [论文](https://www.ndss-symposium.org/ndss-paper/recurrent-private-set-intersection-for-unbalanced-databases-with-cuckoo-hashing-and-leveled-fhe/) |
| RContainer: A Secure Container Architecture through Extending ARM CCA Hardware Primitives. | NDSS | 2025 | TEE | [论文](https://www.ndss-symposium.org/ndss-paper/rcontainer-a-secure-container-architecture-through-extending-arm-cca-hardware-primitives/) |
| Distributed Function Secret Sharing and Applications. | NDSS | 2025 | MPC | [论文](https://www.ndss-symposium.org/ndss-paper/distributed-function-secret-sharing-and-applications/) |
| CounterSEVeillance: Performance-Counter Attacks on AMD SEV-SNP. | NDSS | 2025 | TEE | [论文](https://www.ndss-symposium.org/ndss-paper/counterseveillance-performance-counter-attacks-on-amd-sev-snp/) |
| ASGARD: Protecting On-Device Deep Neural Networks with Virtualization-Based Trusted Execution Environments. | NDSS | 2025 | TEE | [论文](https://www.ndss-symposium.org/ndss-paper/asgard-protecting-on-device-deep-neural-networks-with-virtualization-based-trusted-execution-environments/) |
| Secure Multiparty Computation of Threshold Signatures Made More Efficient. | NDSS | 2024 | MPC | [论文](https://www.ndss-symposium.org/ndss-paper/secure-multiparty-computation-of-threshold-signatures-made-more-efficient/) |
| LDR: Secure and Efficient Linux Driver Runtime for Embedded TEE Systems. | NDSS | 2024 | TEE | [论文](https://www.ndss-symposium.org/ndss-paper/ldr-secure-and-efficient-linux-driver-runtime-for-embedded-tee-systems/) |
| Faults in Our Bus: Novel Bus Fault Attack to Break ARM TrustZone. | NDSS | 2024 | TEE | [论文](https://www.ndss-symposium.org/ndss-paper/faults-in-our-bus-novel-bus-fault-attack-to-break-arm-trustzone/) |
| EnclaveFuzz: Finding Vulnerabilities in SGX Applications. | NDSS | 2024 | TEE | [论文](https://www.ndss-symposium.org/ndss-paper/enclavefuzz-finding-vulnerabilities-in-sgx-applications/) |
| CAGE: Complementing Arm CCA with GPU Extensions. | NDSS | 2024 | TEE | [论文](https://www.ndss-symposium.org/ndss-paper/cage-complementing-arm-cca-with-gpu-extensions/) |
| MyTEE: Own the Trusted Execution Environment on Embedded Devices. | NDSS | 2023 | TEE | [论文](https://www.ndss-symposium.org/ndss-paper/mytee-own-the-trusted-execution-environment-on-embedded-devices/) |
| Faster Secure Comparisons with Offline Phase for Efficient Private Set Intersection. | NDSS | 2023 | MPC | [论文](https://www.ndss-symposium.org/ndss-paper/faster-secure-comparisons-with-offline-phase-for-efficient-private-set-intersection/) · [arXiv](https://arxiv.org/abs/2209.13913) |
| Hybrid Trust Multi-party Computation with Trusted Execution Environment. | NDSS | 2022 | MPC + TEE | [论文](https://www.ndss-symposium.org/ndss-paper/auto-draft-222/) |
| Binary Search in Secure Computation. | NDSS | 2022 | MPC | [论文](https://www.ndss-symposium.org/ndss-paper/auto-draft-224/) · [ePrint](https://eprint.iacr.org/2021/1049) |
| More than a Fair Share: Network Data Remanence Attacks against Secret Sharing-based Schemes. | NDSS | 2021 | MPC | [论文](https://www.ndss-symposium.org/ndss-paper/more-than-a-fair-share-network-data-remanence-attacks-against-secret-sharing-based-schemes/) |

<a id="venue-popets"></a>

## PoPETs（34）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| SEED: A Minimal‑Footprint TEE Framework for Verifiable, Confidential Microservice Deployment. | PoPETs | 2026 | TEE | [论文](https://doi.org/10.56553/POPETS-2026-0021) |
| Oblivis: A Framework for Delegated and Efficient Oblivious Transfer. | PoPETs | 2026 | MPC | [论文](https://doi.org/10.56553/POPETS-2026-0104) · [arXiv](https://arxiv.org/abs/2603.14492) |
| Beyond the Output: Inference Attacks on Private Set Union and Multi-Key Private Matching. | PoPETs | 2026 | MPC | [论文](https://doi.org/10.56553/POPETS-2026-0155) |
| ZIPNet: Low-bandwidth anonymous broadcast from (dis)Trusted Execution Environments. | PoPETs | 2025 | TEE | [论文](https://doi.org/10.56553/POPETS-2025-0058) · [ePrint](https://eprint.iacr.org/2024/1227) |
| Wave Hello to Privacy: Efficient Mixed-Mode MPC using Wavelet Transforms. | PoPETs | 2025 | MPC | [论文](https://doi.org/10.56553/POPETS-2025-0083) · [ePrint](https://eprint.iacr.org/2025/013) |
| TEEMS: A Trusted Execution Environment based Metadata-protected Messaging System. | PoPETs | 2025 | TEE | [论文](https://doi.org/10.56553/POPETS-2025-0119) · [ePrint](https://eprint.iacr.org/2025/1102) |
| SoK: Computational and Distributed Differential Privacy for MPC. | PoPETs | 2025 | MPC | [论文](https://doi.org/10.56553/POPETS-2025-0023) · [ePrint](https://eprint.iacr.org/2024/1290) |
| Re-visiting Authorized Private Set Intersection: A New Privacy-Preserving Variant and Two Protocols. | PoPETs | 2025 | MPC | [论文](https://doi.org/10.56553/POPETS-2025-0041) · [ePrint](https://eprint.iacr.org/2024/1579) |
| PIGEON: A High Throughput Framework for Private Inference of Neural Networks using Secure Multiparty Computation. | PoPETs | 2025 | MPC | [论文](https://doi.org/10.56553/POPETS-2025-0090) · [ePrint](https://eprint.iacr.org/2024/1371) |
| Maliciously Secure Circuit Private Set Intersection via SPDZ-Compatible Oblivious PRF. | PoPETs | 2025 | MPC | [论文](https://doi.org/10.56553/POPETS-2025-0082) · [ePrint](https://eprint.iacr.org/2024/789) |
| High-Throughput Secure Multiparty Computation with an Honest Majority in Various Network Settings. | PoPETs | 2025 | MPC | [论文](https://doi.org/10.56553/POPETS-2025-0015) · [arXiv](https://arxiv.org/abs/2206.03776) · [ePrint](https://eprint.iacr.org/2024/386) |
| Toward A Practical Multi-party Private Set Union. | PoPETs | 2024 | MPC | [论文](https://doi.org/10.56553/POPETS-2024-0133) · [ePrint](https://eprint.iacr.org/2023/1930) |
| SIGMA: Secure GPT Inference with Function Secret Sharing. | PoPETs | 2024 | MPC | [论文](https://doi.org/10.56553/POPETS-2024-0107) · [ePrint](https://eprint.iacr.org/2023/1269) |
| PrivDNN: A Secure Multi-Party Computation Framework for Deep Learning using Partial DNN Encryption. | PoPETs | 2024 | MPC | [论文](https://doi.org/10.56553/POPETS-2024-0089) · [arXiv](https://arxiv.org/abs/2607.21895) · [Code](https://github.com/LiangqinRen/PrivDNN) |
| Multiparty Private Set Intersection Cardinality and Its Applications. | PoPETs | 2024 | MPC | [论文](https://doi.org/10.56553/POPETS-2024-0041) · [ePrint](https://eprint.iacr.org/2022/735) |
| Efficiently Compiling Secure Computation Protocols From Passive to Active Security: Beyond Arithmetic Circuits. | PoPETs | 2024 | MPC | [论文](https://doi.org/10.56553/POPETS-2024-0006) |
| Compact: Approximating Complex Activation Functions for Secure Computation. | PoPETs | 2024 | MPC | [论文](https://doi.org/10.56553/POPETS-2024-0065) · [arXiv](https://arxiv.org/abs/2309.04664) |
| Trust TEE?: Exploring the Impact of Trusted Execution Environments on Smart Home Privacy Norms. | PoPETs | 2023 | TEE | [论文](https://doi.org/10.56553/POPETS-2023-0067) |
| Trifecta: Faster High-Throughput Three-Party Computation over WAN Using Multi-Fan-In Logic Gates. | PoPETs | 2023 | MPC | [论文](https://doi.org/10.56553/POPETS-2023-0107) |
| Multi-Party Replicated Secret Sharing over a Ring with Applications to Privacy-Preserving Machine Learning. | PoPETs | 2023 | MPC | [论文](https://doi.org/10.56553/POPETS-2023-0035) · [ePrint](https://eprint.iacr.org/2020/1577) |
| Funshade: Function Secret Sharing for Two-Party Secure Thresholded Distance Evaluation. | PoPETs | 2023 | MPC | [论文](https://doi.org/10.56553/POPETS-2023-0096) · [ePrint](https://eprint.iacr.org/2022/1688) |
| Efficient decision tree training with new data structure for secure multi-party computation. | PoPETs | 2023 | MPC | [论文](https://doi.org/10.56553/POPETS-2023-0021) · [arXiv](https://arxiv.org/abs/2112.12906) |
| Convolutions in Overdrive: Maliciously Secure Convolutions for MPC. | PoPETs | 2023 | MPC | [论文](https://doi.org/10.56553/POPETS-2023-0084) · [ePrint](https://eprint.iacr.org/2023/359) |
| XORBoost: Tree Boosting in the Multiparty Computation Setting. | PoPETs | 2022 | MPC | [论文](https://doi.org/10.56553/POPETS-2022-0099) · [ePrint](https://eprint.iacr.org/2021/432) |
| Updatable Private Set Intersection. | PoPETs | 2022 | MPC | [论文](https://doi.org/10.2478/POPETS-2022-0051) · [ePrint](https://eprint.iacr.org/2021/1349) |
| SoK: TEE-Assisted Confidential Smart Contract. | PoPETs | 2022 | TEE | [论文](https://doi.org/10.56553/POPETS-2022-0093) · [arXiv](https://arxiv.org/abs/2203.08548) |
| Polymath: Low-Latency MPC via Secure Polynomial Evaluations and Its Applications. | PoPETs | 2022 | MPC | [论文](https://doi.org/10.2478/POPETS-2022-0020) · [ePrint](https://eprint.iacr.org/2021/978) |
| Pika: Secure Computation using Function Secret Sharing over Rings. | PoPETs | 2022 | MPC | [论文](https://doi.org/10.56553/POPETS-2022-0113) · [ePrint](https://eprint.iacr.org/2022/826) |
| Fully Secure PSI via MPC-in-the-Head. | PoPETs | 2022 | MPC | [论文](https://doi.org/10.56553/POPETS-2022-0073) · [ePrint](https://eprint.iacr.org/2022/379) |
| AriaNN: Low-Interaction Privacy-Preserving Deep Learning via Function Secret Sharing. | PoPETs | 2022 | MPC | [论文](https://doi.org/10.2478/POPETS-2022-0015) · [arXiv](https://arxiv.org/abs/2006.04593) |
| SGX-MR: Regulating Dataflows for Protecting Access Patterns of Data-Intensive SGX Applications. | PoPETs | 2021 | TEE | [论文](https://doi.org/10.2478/POPETS-2021-0002) · [arXiv](https://arxiv.org/abs/2009.03518) |
| Fortified Multi-Party Computation: Taking Advantage of Simple Secure Hardware Modules. | PoPETs | 2021 | MPC | [论文](https://doi.org/10.2478/POPETS-2021-0072) |
| Reimagining Secret Sharing: Creating a Safer and More Versatile Primitive by Adding Authenticity, Correcting Errors, and Reducing Randomness Requirements. | PoPETs | 2020 | MPC | [论文](https://doi.org/10.2478/POPETS-2020-0082) · [ePrint](https://eprint.iacr.org/2020/800) |
| Mind the Gap: Ceremonies for Applied Secret Sharing. | PoPETs | 2020 | MPC | [论文](https://doi.org/10.2478/POPETS-2020-0033) |

<a id="venue-tifs"></a>

## TIFS（54）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| Updatable Multi-Party Private Set Intersection for Real-Time Collaborative Threat Intelligence. | TIFS | 2026 | MPC | [论文](https://doi.org/10.1109/TIFS.2026.3707440) |
| UFOs: An Ultra-Fast Toolkit for Multiparty Computation on Small Elements. | TIFS | 2026 | MPC | [论文](https://doi.org/10.1109/TIFS.2026.3734714) |
| TrustSearch: Toward Secure and Efficient Reverse Image Search via SGX. | TIFS | 2026 | TEE | [论文](https://doi.org/10.1109/TIFS.2026.3696201) |
| Secure Computation Over Gaussian Multiple-Access Wiretap Channels With Feedback. | TIFS | 2026 | MPC | [论文](https://doi.org/10.1109/TIFS.2026.3715114) |
| Secret Sharing Schemes From Correlated Random Variables and Rate-Limited Public Communication. | TIFS | 2026 | MPC | [论文](https://doi.org/10.1109/TIFS.2026.3657030) · [arXiv](https://arxiv.org/abs/2505.04076) |
| Practical Private Set Operation via Secret Sharing for Lightweight Clients. | TIFS | 2026 | MPC | [论文](https://doi.org/10.1109/TIFS.2026.3684841) |
| Optimal Access Structure Partition Methods for Image Secret Sharing. | TIFS | 2026 | MPC | [论文](https://doi.org/10.1109/TIFS.2025.3645631) |
| On the Attribute Hiding Security of Privacy Preserving Secret-Sharing-Based Outsourced Decision Tree Classification. | TIFS | 2026 | MPC | [论文](https://doi.org/10.1109/TIFS.2026.3714143) |
| Efficient Privacy-Preserving User Tracking From Threshold Multi-Party Private Set Intersection. | TIFS | 2026 | MPC | [论文](https://doi.org/10.1109/TIFS.2026.3705319) |
| Efficient Malicious Multiparty Private Set Intersection Supporting Cardinality, Sharing, and Batching. | TIFS | 2026 | MPC | [论文](https://doi.org/10.1109/TIFS.2026.3671114) |
| DisT-FL: Enhancing Security for TEE-Based Aggregation in Federated Learning. | TIFS | 2026 | TEE | [论文](https://doi.org/10.1109/TIFS.2026.3715108) · [arXiv](https://arxiv.org/abs/2606.04899) |
| DMPF-PSI: Enabling High-Frequency Updatable Private Set Intersection on Dynamic Data. | TIFS | 2026 | MPC | [论文](https://doi.org/10.1109/TIFS.2026.3705330) |
| Cryptanalysis of "Multi-Party Private Set Intersection With One-Round Online Interaction". | TIFS | 2026 | MPC | [论文](https://doi.org/10.1109/TIFS.2026.3666890) |
| CROSS-TEE: A Distributed Trusted Execution Environment Architecture for Cross-Module Automotive Security. | TIFS | 2026 | TEE | [论文](https://doi.org/10.1109/TIFS.2026.3714115) |
| Multi-Party Private Set Intersection With One-Round Online Interaction. | TIFS | 2025 | MPC | [论文](https://doi.org/10.1109/TIFS.2025.3574993) |
| More Granular, Less Trust: Enforcing Intra-Process Isolation With Arm CCA in an Untrusted Management Environment. | TIFS | 2025 | TEE | [论文](https://doi.org/10.1109/TIFS.2025.3634981) · [arXiv](https://arxiv.org/abs/2608.20584) |
| More Efficient, Privacy-Enhanced, and Powerful Privacy-Preserving Feature Retrieval Private Set Intersection. | TIFS | 2025 | MPC | [论文](https://doi.org/10.1109/TIFS.2025.3562695) |
| Microft: Exploring and Mitigating Cross-State Control-Flow Hijacking Attacks on ARM Cortex-M TrustZone. | TIFS | 2025 | TEE | [论文](https://doi.org/10.1109/TIFS.2025.3625394) |
| Labeled Private Set Intersection From Distributed Point Function. | TIFS | 2025 | MPC | [论文](https://doi.org/10.1109/TIFS.2025.3550059) |
| EoTMP: Efficient Over-Threshold Multi-Party Private Set Intersection. | TIFS | 2025 | MPC | [论文](https://doi.org/10.1109/TIFS.2025.3639987) |
| Efficient and Privacy-Preserving Feature Selection Based on Multiparty Computation. | TIFS | 2025 | MPC | [论文](https://doi.org/10.1109/TIFS.2025.3546843) |
| Efficient Three-Party ECDSA Signature Based on Replicated Secret Sharing With Identifiable Abort. | TIFS | 2025 | MPC | [论文](https://doi.org/10.1109/TIFS.2025.3607264) |
| Efficient Collaborative Data Cleaning Using Private Set Intersection and Encoding for Unbalanced Datasets. | TIFS | 2025 | MPC | [论文](https://doi.org/10.1109/TIFS.2025.3594871) |
| Charge Your Clients: Payable Secure Computation and Its Applications. | TIFS | 2025 | MPC | [论文](https://doi.org/10.1109/TIFS.2025.3559456) · [ePrint](https://eprint.iacr.org/2025/630) |
| Updatable Private Set Intersection With Forward Privacy. | TIFS | 2024 | MPC | [论文](https://doi.org/10.1109/TIFS.2024.3461475) |
| The Capacity Region of Distributed Multi-User Secret Sharing Under Perfect Secrecy. | TIFS | 2024 | MPC | [论文](https://doi.org/10.1109/TIFS.2024.3484666) |
| Sparsity and Privacy in Secret Sharing: A Fundamental Trade-Off. | TIFS | 2024 | MPC | [论文](https://doi.org/10.1109/TIFS.2024.3394256) · [arXiv](https://arxiv.org/abs/2308.06413) |
| Secure and Efficient Federated Learning via Novel Authenticable Multi-Party Computation and Compressed Sensing. | TIFS | 2024 | MPC | [论文](https://doi.org/10.1109/TIFS.2024.3486611) |
| Secure Similarity Queries Over Vertically Distributed Data via TEE-Enhanced Cloud Computing. | TIFS | 2024 | TEE | [论文](https://doi.org/10.1109/TIFS.2024.3413630) |
| Secret Cracking and Security Enhancement for the Image Application of CRT-Based Secret Sharing. | TIFS | 2024 | MPC | [论文](https://doi.org/10.1109/TIFS.2024.3477265) |
| P²FRPSI: Privacy-Preserving Feature Retrieved Private Set Intersection. | TIFS | 2024 | MPC | [论文](https://doi.org/10.1109/TIFS.2023.3343973) |
| Fast Evaluation of S-Boxes With Garbled Circuits. | TIFS | 2024 | MPC | [论文](https://doi.org/10.1109/TIFS.2024.3402145) · [arXiv](https://arxiv.org/abs/2405.20713) · [ePrint](https://eprint.iacr.org/2022/1278) |
| FSS-DBSCAN: Outsourced Private Density-Based Clustering via Function Secret Sharing. | TIFS | 2024 | MPC | [论文](https://doi.org/10.1109/TIFS.2024.3446233) |
| Enabling Threshold Functionality for Private Set Intersection Protocols in Cloud Computing. | TIFS | 2024 | MPC | [论文](https://doi.org/10.1109/TIFS.2024.3402355) |
| Efficient Coded Multi-Party Computation at Edge Networks. | TIFS | 2024 | MPC | [论文](https://doi.org/10.1109/TIFS.2023.3326970) · [arXiv](https://arxiv.org/abs/2305.07142) |
| Dual-Cloud Multi-Secret Sharing Architecture for Privacy Preserving Persistent Computation. | TIFS | 2024 | MPC | [论文](https://doi.org/10.1109/TIFS.2024.3436662) |
| DeCloak: Enable Secure and Cheap Multi-Party Transactions on Legacy Blockchains by a Minimally Trusted TEE Network. | TIFS | 2024 | MPC + TEE | [论文](https://doi.org/10.1109/TIFS.2023.3318935) · [arXiv](https://arxiv.org/abs/2202.10206) |
| Communication-Efficient Privacy-Preserving Neural Network Inference via Arithmetic Secret Sharing. | TIFS | 2024 | MPC | [论文](https://doi.org/10.1109/TIFS.2024.3420216) |
| Collusion-Resilient and Maliciously Secure Cloud- Assisted Two-Party Computation Scheme in Mobile Cloud Computing. | TIFS | 2024 | MPC | [论文](https://doi.org/10.1109/TIFS.2024.3428410) |
| A New Shift-Add Secret Sharing Scheme for Partial Data Protection With Parallel Zigzag Decoding. | TIFS | 2024 | MPC | [论文](https://doi.org/10.1109/TIFS.2024.3488498) |
| Publicly Verifiable Homomorphic Secret Sharing for Polynomial Evaluation. | TIFS | 2023 | MPC | [论文](https://doi.org/10.1109/TIFS.2023.3298258) |
| Privacy of Federated QR Decomposition Using Additive Secure Multiparty Computation. | TIFS | 2023 | MPC | [论文](https://doi.org/10.1109/TIFS.2023.3301710) · [arXiv](https://arxiv.org/abs/2210.06163) |
| Low Communication Secure Computation From Semi-Trusted Hardware. | TIFS | 2023 | MPC | [论文](https://doi.org/10.1109/TIFS.2023.3282134) |
| Rphx: Result Pattern Hiding Conjunctive Query Over Private Compressed Index Using Intel SGX. | TIFS | 2022 | TEE | [论文](https://doi.org/10.1109/TIFS.2022.3144877) |
| Practical Multi-Party Private Set Intersection Protocols. | TIFS | 2022 | MPC | [论文](https://doi.org/10.1109/TIFS.2021.3118879) |
| Fast Privacy-Preserving Text Classification Based on Secure Multiparty Computation. | TIFS | 2022 | MPC | [论文](https://doi.org/10.1109/TIFS.2022.3144007) · [arXiv](https://arxiv.org/abs/2101.07365) · [ePrint](https://eprint.iacr.org/2021/069) |
| Differentially Private Set Intersection for Asymmetrical ID Alignment. | TIFS | 2022 | MPC | [论文](https://doi.org/10.1109/TIFS.2022.3207911) |
| Analog Secret Sharing With Applications to Private Distributed Learning. | TIFS | 2022 | MPC | [论文](https://doi.org/10.1109/TIFS.2022.3173417) |
| Utilizing and Extending Trusted Execution Environment in Heterogeneous SoCs for a Pay-Per-Device IP Licensing Scheme. | TIFS | 2021 | TEE | [论文](https://doi.org/10.1109/TIFS.2021.3058777) |
| Private Set Intersection With Authorization Over Outsourced Encrypted Datasets. | TIFS | 2021 | MPC | [论文](https://doi.org/10.1109/TIFS.2021.3101059) |
| Framing in Secret Sharing. | TIFS | 2021 | MPC | [论文](https://doi.org/10.1109/TIFS.2021.3067468) |
| SecGrid: A Secure and Efficient SGX-Enabled Smart Grid System With Rich Functionalities. | TIFS | 2020 | TEE | [论文](https://doi.org/10.1109/TIFS.2019.2938875) |
| Reversible Image Secret Sharing. | TIFS | 2020 | MPC | [论文](https://doi.org/10.1109/TIFS.2020.3001735) |
| Establishing Trusted I/O Paths for SGX Client Systems With Aurora. | TIFS | 2020 | TEE | [论文](https://doi.org/10.1109/TIFS.2019.2945621) |

<a id="venue-tdsc"></a>

## TDSC（57）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| kvTZ: TrustZone Virtualization for Commodity Arm-Based Platforms. | TDSC | 2026 | TEE | [论文](https://doi.org/10.1109/TDSC.2025.3605807) |
| Toward Secure and Efficient Driver Support for Embedded TEE Systems. | TDSC | 2026 | TEE | [论文](https://doi.org/10.1109/TDSC.2026.3693739) |
| Teamwork Makes TEE Work: Open and Resilient Remote Attestation on Decentralized Trust. | TDSC | 2026 | TEE | [论文](https://doi.org/10.1109/TDSC.2025.3636884) · [arXiv](https://arxiv.org/abs/2402.08908) |
| SecOIR: Enhancing Privacy and Accuracy in Outsourced Image Retrieval via Function Secret Sharing and Deep Hashing. | TDSC | 2026 | MPC | [论文](https://doi.org/10.1109/TDSC.2025.3628356) |
| SXGB: Secure and Efficient Vertical Federated XGBoost via Trusted Execution Environments. | TDSC | 2026 | TEE | [论文](https://doi.org/10.1109/TDSC.2025.3626379) |
| Privacy-Preserving Continuous Authentication of Smartphone Users via Secret Sharing. | TDSC | 2026 | MPC | [论文](https://doi.org/10.1109/TDSC.2026.3680150) |
| PriFFT: Privacy-Preserving Federated Fine-Tuning of Large Language Models via Hybrid Secret Sharing. | TDSC | 2026 | MPC | [论文](https://doi.org/10.1109/TDSC.2026.3661572) · [arXiv](https://arxiv.org/abs/2503.03146) |
| Palladium: Guarding Neural Network Training With Confidential Computing. | TDSC | 2026 | TEE | [论文](https://doi.org/10.1109/TDSC.2026.3694706) |
| FESCAT: Function Secret Sharing Based Efficient Secure Collaborative Analysis of Time Series Data. | TDSC | 2026 | MPC | [论文](https://doi.org/10.1109/TDSC.2025.3632891) |
| Enabling Confidential VMs Across Diverse ARM Platforms by Retrofitting TrustZone. | TDSC | 2026 | TEE | [论文](https://doi.org/10.1109/TDSC.2026.3657770) |
| Complementing Confidential Computing Environment for Applications on Arm CCA. | TDSC | 2026 | TEE | [论文](https://doi.org/10.1109/TDSC.2025.3604008) |
| Building Confidential Accelerator Computing Environment for Arm CCA. | TDSC | 2026 | TEE | [论文](https://doi.org/10.1109/TDSC.2025.3615787) |
| Approx-PSI: Efficient Differentially Private Set Intersection-Based Analysis. | TDSC | 2026 | MPC | [论文](https://doi.org/10.1109/TDSC.2025.3629820) |
| Anonymous Integrity Auditing Scheme Based on Trusted Execution Environment for Distributed Edge Computing. | TDSC | 2026 | TEE | [论文](https://doi.org/10.1109/TDSC.2026.3670134) |
| Ultra-Fast Private Set Intersection From Efficient Oblivious Key-Value Stores. | TDSC | 2025 | MPC | [论文](https://doi.org/10.1109/TDSC.2025.3557963) |
| Tacco: A Framework for Ensuring the Security of Real-World TEEs via Formal Verification. | TDSC | 2025 | TEE | [论文](https://doi.org/10.1109/TDSC.2025.3594594) |
| Revisiting SGX-Based Encrypted Deduplication via PoW-Before-Encryption and Eliminating Redundant Computations. | TDSC | 2025 | TEE | [论文](https://doi.org/10.1109/TDSC.2024.3476288) |
| Reversible Data Hiding in Encrypted Images With Secret Sharing and Multivariate Linear Equation. | TDSC | 2025 | MPC | [论文](https://doi.org/10.1109/TDSC.2025.3590551) |
| Privacy-Preserving Authorized Set Matching via Dishonest Majority Multiparty Computation. | TDSC | 2025 | MPC | [论文](https://doi.org/10.1109/TDSC.2025.3599183) |
| PM-ABE: Puncturable Bilateral Fine-Grained Access Control From Lattices for Secret Sharing. | TDSC | 2025 | MPC | [论文](https://doi.org/10.1109/TDSC.2024.3431035) |
| OPSA: Efficient and Verifiable One-Pass Secure Aggregation With TEE for Federated Learning. | TDSC | 2025 | TEE | [论文](https://doi.org/10.1109/TDSC.2025.3565640) · [ePrint](https://eprint.iacr.org/2024/476) |
| Multiparty Delegated Private Set Union With Efficient Updates on Outsourced Datasets. | TDSC | 2025 | MPC | [论文](https://doi.org/10.1109/TDSC.2024.3419576) |
| MuEOC: Efficient SGX-Based Multi-Key Homomorphic Outsourcing Computation for E-Health System. | TDSC | 2025 | TEE | [论文](https://doi.org/10.1109/TDSC.2024.3476483) |
| MaTEE: Efficiently Bridging the Semantic Gap in TrustZone via Arm Pointer Authentication. | TDSC | 2025 | TEE | [论文](https://doi.org/10.1109/TDSC.2024.3445296) · [arXiv](https://arxiv.org/abs/2608.20583) |
| Increasing the Resilience of Secure Multiparty Computation Using Security Modules. | TDSC | 2025 | MPC | [论文](https://doi.org/10.1109/TDSC.2025.3552670) |
| Formal Security Analysis of the AMD SEV-SNP Software Interface. | TDSC | 2025 | TEE | [论文](https://doi.org/10.1109/TDSC.2025.3528737) · [arXiv](https://arxiv.org/abs/2403.10296) |
| Enabling Two-Party Secure Computation on Set Intersection. | TDSC | 2025 | MPC | [论文](https://doi.org/10.1109/TDSC.2025.3561472) · [ePrint](https://eprint.iacr.org/2023/609) |
| A Scheme of Robust Privacy-Preserving Multi-Party Computation via Public Verification. | TDSC | 2025 | MPC | [论文](https://doi.org/10.1109/TDSC.2025.3555284) |
| SGXFault: An Efficient Page Fault Handling Mechanism for SGX Enclaves. | TDSC | 2024 | TEE | [论文](https://doi.org/10.1109/TDSC.2023.3268169) |
| Maliciously Secure MPC From Semi-Honest 2PC in the Server-Aided Model. | TDSC | 2024 | MPC | [论文](https://doi.org/10.1109/TDSC.2023.3322397) |
| Ensuring State Continuity for Confidential Computing: A Blockchain-Based Approach. | TDSC | 2024 | TEE | [论文](https://doi.org/10.1109/TDSC.2024.3381973) |
| Building a Lightweight Trusted Execution Environment for Arm GPUs. | TDSC | 2024 | TEE | [论文](https://doi.org/10.1109/TDSC.2023.3334277) |
| Bounds and Protocols for Graph-Based Distributed Secret Sharing. | TDSC | 2024 | MPC | [论文](https://doi.org/10.1109/TDSC.2023.3261239) |
| Application of Randomness for Security and Privacy in Multi-Party Computation. | TDSC | 2024 | MPC | [论文](https://doi.org/10.1109/TDSC.2024.3381959) |
| A Secure Computing System With Hardware-Efficient Lazy Bonsai Merkle Tree for FPGA-Attached Embedded Memory. | TDSC | 2024 | MPC | [论文](https://doi.org/10.1109/TDSC.2023.3324935) |
| A Comprehensive Trusted Runtime for WebAssembly With Intel SGX. | TDSC | 2024 | TEE | [论文](https://doi.org/10.1109/TDSC.2023.3334516) · [arXiv](https://arxiv.org/abs/2312.09087) |
| Verifiable Homomorphic Secret Sharing for Low Degree Polynomials. | TDSC | 2023 | MPC | [论文](https://doi.org/10.1109/TDSC.2022.3194321) |
| Trust Beyond Border: Lightweight, Verifiable User Isolation for Protecting In-Enclave Services. | TDSC | 2023 | TEE | [论文](https://doi.org/10.1109/TDSC.2021.3138427) |
| T-Counter: Trustworthy and Efficient CPU Resource Measurement Using SGX in the Cloud. | TDSC | 2023 | TEE | [论文](https://doi.org/10.1109/TDSC.2022.3145814) |
| Shielding Graph for eXact Analytics With SGX. | TDSC | 2023 | TEE | [论文](https://doi.org/10.1109/TDSC.2023.3241164) |
| On the Security of a Lattice-Based Multi-Stage Secret Sharing Scheme. | TDSC | 2023 | MPC | [论文](https://doi.org/10.1109/TDSC.2022.3209011) |
| Matrix-Based Secret Sharing for Reversible Data Hiding in Encrypted Images. | TDSC | 2023 | MPC | [论文](https://doi.org/10.1109/TDSC.2022.3218570) |
| Maliciously Secure and Efficient Large-Scale Genome-Wide Association Study With Multi-Party Computation. | TDSC | 2023 | MPC | [论文](https://doi.org/10.1109/TDSC.2022.3152498) |
| Improved Protocols for Distributed Secret Sharing. | TDSC | 2023 | MPC | [论文](https://doi.org/10.1109/TDSC.2022.3213790) |
| Efficient Noise Generation Protocols for Differentially Private Multiparty Computation. | TDSC | 2023 | MPC | [论文](https://doi.org/10.1109/TDSC.2022.3227568) · [ePrint](https://eprint.iacr.org/2022/1391) |
| ESMAC: Efficient and Secure Multi-Owner Access Control With TEE in Multi-Level Data Processing. | TDSC | 2023 | TEE | [论文](https://doi.org/10.1109/TDSC.2022.3215977) |
| ENCIDER: Detecting Timing and Cache Side Channels in SGX Enclaves and Cryptographic APIs. | TDSC | 2023 | TEE | [论文](https://doi.org/10.1109/TDSC.2022.3160346) |
| Circuit-Free General-Purpose Multi-Party Computation via Co-Utile Unlinkable Outsourcing. | TDSC | 2023 | MPC | [论文](https://doi.org/10.1109/TDSC.2021.3138826) · [arXiv](https://arxiv.org/abs/2112.15001) |
| CVTEE: A Compatible Verified TEE Architecture With Enhanced Security. | TDSC | 2023 | TEE | [论文](https://doi.org/10.1109/TDSC.2021.3133576) |
| Self-Stabilizing Secure Computation. | TDSC | 2022 | MPC | [论文](https://doi.org/10.1109/TDSC.2020.2986751) |
| Secret Sharing Based Reversible Data Hiding in Encrypted Images With Multiple Data-Hiders. | TDSC | 2022 | MPC | [论文](https://doi.org/10.1109/TDSC.2020.3011923) |
| SGXTuner: Performance Enhancement of Intel SGX Applications Via Stochastic Optimization. | TDSC | 2022 | TEE | [论文](https://doi.org/10.1109/TDSC.2021.3064391) |
| Malware in the SGX Supply Chain: Be Careful When Signing Enclaves! | TDSC | 2022 | TEE | [论文](https://doi.org/10.1109/TDSC.2020.3024562) |
| Differentially Oblivious Data Analysis With Intel SGX: Design, Optimization, and Evaluation. | TDSC | 2022 | TEE | [论文](https://doi.org/10.1109/TDSC.2021.3106317) |
| Secure Secret Sharing Enabled b-band Mini Vaults Bio-Cryptosystem for Vectorial Biometrics. | TDSC | 2021 | MPC | [论文](https://doi.org/10.1109/TDSC.2018.2874245) |
| Secure Computing Enclaves Using FPGAs. | TDSC | 2021 | MPC + TEE | [论文](https://doi.org/10.1109/TDSC.2019.2933214) |
| Efficient Server-Aided Secure Two-Party Computation in Heterogeneous Mobile Cloud Computing. | TDSC | 2021 | MPC | [论文](https://doi.org/10.1109/TDSC.2020.2966632) |

<a id="venue-osdi"></a>

## OSDI（2）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| Design and Verification of the Arm Confidential Compute Architecture. | OSDI | 2022 | TEE | [论文](https://www.usenix.org/conference/osdi22/presentation/li) |
| MAGE: Nearly Zero-Cost Virtual Memory for Secure Computation. | OSDI | 2021 | MPC | [论文](https://www.usenix.org/conference/osdi21/presentation/kumar) · [arXiv](https://arxiv.org/abs/2106.14651) |

<a id="venue-eurosys"></a>

## EuroSys（8）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| TZ-LLM: Protecting On-Device Large Language Models with Arm TrustZone. | EuroSys | 2026 | TEE | [论文](https://doi.org/10.1145/3767295.3769334) · [arXiv](https://arxiv.org/abs/2511.13717) |
| Rakis: Secure Fast I/O Primitives Across Trust Boundaries on Intel SGX. | EuroSys | 2025 | TEE | [论文](https://doi.org/10.1145/3689031.3696090) |
| Safe and Practical GPU Computation in TrustZone. | EuroSys | 2023 | TEE | [论文](https://doi.org/10.1145/3552326.3567483) |
| Minimum viable device drivers for ARM trustzone. | EuroSys | 2022 | TEE | [论文](https://doi.org/10.1145/3492321.3519565) · [arXiv](https://arxiv.org/abs/2110.08303) |
| Confidential computing for OpenPOWER. | EuroSys | 2021 | TEE | [论文](https://doi.org/10.1145/3447786.3456243) |
| Oblivious coopetitive analytics using hardware enclaves. | EuroSys | 2020 | TEE | [论文](https://doi.org/10.1145/3342195.3387552) |
| MPTEE: bringing flexible and efficient memory protection to Intel SGX. | EuroSys | 2020 | TEE | [论文](https://doi.org/10.1145/3342195.3387536) |
| Keystone: an open framework for architecting trusted execution environments. | EuroSys | 2020 | TEE | [论文](https://doi.org/10.1145/3342195.3387532) |

<a id="venue-nsdi"></a>

## NSDI（2）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| Over-Threshold Multiparty Private Set Intersection for Collaborative Network Intrusion Detection. | NSDI | 2026 | MPC | [论文](https://www.usenix.org/conference/nsdi26/presentation/arpaci) · [arXiv](https://arxiv.org/abs/2510.12045) |
| Telekine: Secure Computing with Cloud GPUs. | NSDI | 2020 | MPC | [论文](https://www.usenix.org/conference/nsdi20/presentation/hunt) |

<a id="venue-isca"></a>

## ISCA（7）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| LÆGIS: Pinpointing and Addressing Performance Overheads of GPU-Based Confidential Computing. | ISCA | 2026 | TEE | [论文](https://doi.org/10.1109/ISCA66397.2026.00046) |
| sNPU: Trusted Execution Environments on Integrated NPUs. | ISCA | 2024 | TEE | [论文](https://doi.org/10.1109/ISCA59077.2024.00057) |
| TEESec: Pre-Silicon Vulnerability Discovery for Trusted Execution Environments. | ISCA | 2023 | TEE | [论文](https://doi.org/10.1145/3579371.3589070) |
| HAAC: A Hardware-Software Co-Design to Accelerate Garbled Circuits. | ISCA | 2023 | MPC + TEE | [论文](https://doi.org/10.1145/3579371.3589045) · [arXiv](https://arxiv.org/abs/2211.13324) |
| PPMLAC: high performance chipset architecture for secure multi-party computation. | ISCA | 2022 | MPC | [论文](https://doi.org/10.1145/3470496.3527392) |
| Confidential Serverless Made Efficient with Plug-In Enclaves. | ISCA | 2021 | TEE | [论文](https://doi.org/10.1109/ISCA52012.2021.00032) |
| Nested Enclave: Supporting Fine-grained Hierarchical Isolation with SGX. | ISCA | 2020 | TEE | [论文](https://doi.org/10.1109/ISCA45697.2020.00069) |

<a id="venue-micro"></a>

## MICRO（5）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| Ironman: Accelerating Oblivious Transfer Extension for Privacy-Preserving AI with Near-Memory Processing. | MICRO | 2025 | MPC | [论文](https://doi.org/10.1145/3725843.3756025) · [arXiv](https://arxiv.org/abs/2507.16391) |
| HyperTEE: A Decoupled TEE Architecture with Secure Enclave Management. | MICRO | 2024 | TEE | [论文](https://doi.org/10.1109/MICRO61859.2024.00018) |
| Accelerating Extra Dimensional Page Walks for Confidential Computing. | MICRO | 2023 | TEE | [论文](https://doi.org/10.1145/3613424.3614293) |
| CRONUS: Fault-isolated, Secure and High-performance Heterogeneous Computing for Trusted Execution Environment. | MICRO | 2022 | TEE | [论文](https://doi.org/10.1109/MICRO56248.2022.00019) |
| IceClave: A Trusted Execution Environment for In-Storage Computing. | MICRO | 2021 | TEE | [论文](https://doi.org/10.1145/3466752.3480109) · [arXiv](https://arxiv.org/abs/2109.03373) |

<a id="venue-hpca"></a>

## HPCA（3）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| Data Enclave: A Data-Centric Trusted Execution Environment. | HPCA | 2024 | TEE | [论文](https://doi.org/10.1109/HPCA57654.2024.00026) |
| A Quantum Computer Trusted Execution Environment. | HPCA | 2024 | TEE | [论文](https://doi.org/10.1109/HPCA57654.2024.00051) |
| Root Crash Consistency of SGX-style Integrity Trees in Secure Non-Volatile Memory Systems. | HPCA | 2023 | TEE | [论文](https://doi.org/10.1109/HPCA56546.2023.10071003) |

<a id="venue-asplos"></a>

## ASPLOS（11）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| WorksetEnclave: Towards Optimizing Cold Starts in Confidential Serverless with Workset-Based Enclave Restore. | ASPLOS | 2026 | TEE | [论文](https://doi.org/10.1145/3779212.3790249) |
| Trust-V: Toward Secure and Reliable Storage for Trusted Execution Environments. | ASPLOS | 2026 | TEE | [论文](https://doi.org/10.1145/3779212.3790242) |
| TEEM³: Core-Independent and Cooperating Trusted Execution Environments. | ASPLOS | 2026 | TEE | [论文](https://doi.org/10.1145/3779212.3790232) |
| Detecting Inconsistencies in Arm CCA's Formally Verified Specification. | ASPLOS | 2026 | TEE | [论文](https://doi.org/10.1145/3779212.3790152) |
| Reload+Reload: Exploiting Cache and Memory Contention Side Channel on AMD SEV. | ASPLOS | 2025 | TEE | [论文](https://doi.org/10.1145/3676641.3716017) |
| MDPeek: Breaking Balanced Branches in SGX with Memory Disambiguation Unit Side Channels. | ASPLOS | 2025 | TEE | [论文](https://doi.org/10.1145/3676641.3716004) |
| TensorTEE: Unifying Heterogeneous TEE Granularity for Efficient Secure Collaborative Tensor Computing. | ASPLOS | 2024 | TEE | [论文](https://doi.org/10.1145/3622781.3674168) · [arXiv](https://arxiv.org/abs/2407.08903) |
| Salus: A Practical Trusted Execution Environment for CPU-FPGA Heterogeneous Cloud Platforms. | ASPLOS | 2024 | TEE | [论文](https://doi.org/10.1145/3622781.3674169) |
| MPC-Pipe: an Efficient Pipeline Scheme for Semi-honest MPC Machine Learning. | ASPLOS | 2024 | MPC | [论文](https://doi.org/10.1145/3622781.3674175) |
| Occlum: Secure and Efficient Multitasking Inside a Single Enclave of Intel SGX. | ASPLOS | 2020 | TEE | [论文](https://doi.org/10.1145/3373376.3378469) · [arXiv](https://arxiv.org/abs/2001.07450) |
| COIN Attacks: On Insecurity of Enclave Untrusted Interfaces in SGX. | ASPLOS | 2020 | TEE | [论文](https://doi.org/10.1145/3373376.3378486) |

<a id="venue-sigmod"></a>

## SIGMOD（3）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| TeeBench: Seamless Benchmarking in Trusted Execution Environments. | SIGMOD | 2023 | TEE | [论文](https://doi.org/10.1145/3555041.3589726) |
| IncShrink: Architecting Efficient Outsourced Databases using Incremental MPC and Differential Privacy. | SIGMOD | 2022 | MPC | [论文](https://doi.org/10.1145/3514221.3526151) · [arXiv](https://arxiv.org/abs/2203.05084) |
| VeriDB: An SGX-based Verifiable Database. | SIGMOD | 2021 | TEE | [论文](https://doi.org/10.1145/3448016.3457308) |

<a id="venue-pacmmod-sigmod"></a>

## PACMMOD / SIGMOD（3）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| Scalable Privacy-Preserving Shortest Path Distance Computation via 2-Hop Labeling in MPC. | PACMMOD / SIGMOD | 2026 | MPC | [论文](https://doi.org/10.1145/3786695) |
| OBIR-tree: An Efficient Oblivious Index for Spatial Keyword Queries on Secure Enclaves. | PACMMOD / SIGMOD | 2025 | TEE | [论文](https://doi.org/10.1145/3709708) |
| TEE-based General-purpose Computational Backend for Secure Delegated Data Processing. | PACMMOD / SIGMOD | 2023 | TEE | [论文](https://doi.org/10.1145/3626757) |

<a id="venue-pvldb"></a>

## PVLDB（6）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| LETIndex: A Secure Learned Index with TEE. | PVLDB | 2025 | TEE | [论文](https://doi.org/10.14778/3750601.3750682) |
| Olive: Oblivious Federated Learning on Trusted Execution Environment Against the Risk of Sparsification. | PVLDB | 2023 | TEE | [论文](https://doi.org/10.14778/3603581.3603583) · [arXiv](https://arxiv.org/abs/2202.07165) |
| Longshot: Indexing Growing Databases using MPC and Differential Privacy. | PVLDB | 2023 | MPC | [论文](https://doi.org/10.14778/3594512.3594529) |
| Enabling Secure and Efficient Data Analytics Pipeline Evolution with Trusted Execution Environment. | PVLDB | 2023 | TEE | [论文](https://doi.org/10.14778/3603581.3603589) |
| Cracking-Like Join for Trusted Execution Environments. | PVLDB | 2023 | TEE | [论文](https://doi.org/10.14778/3598581.3598602) |
| What Is the Price for Joining Securely? Benchmarking Equi-Joins in Trusted Execution Environments. | PVLDB | 2021 | TEE | [论文](https://doi.org/10.14778/3494124.3494146) |

<a id="venue-icde"></a>

## ICDE（3）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| BiTDB: Constructing A Built-in TEE Secure Database for Embedded Systems (Extended Abstract). | ICDE | 2025 | TEE | [论文](https://doi.org/10.1109/ICDE65448.2025.00393) |
| SEFrame: An SGX-enhanced Smart Contract Execution Framework for Permissioned Blockchain. | ICDE | 2022 | TEE | [论文](https://doi.org/10.1109/ICDE53745.2022.00289) |
| High-Performance Smart Contracts Concurrent Execution for Permissioned Blockchain Using SGX. | ICDE | 2021 | TEE | [论文](https://doi.org/10.1109/ICDE51399.2021.00175) |

<a id="venue-tpds"></a>

## TPDS（3）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| TSC-VEE: A TrustZone-Based Smart Contract Virtual Execution Environment. | TPDS | 2023 | TEE | [论文](https://doi.org/10.1109/TPDS.2023.3263882) |
| Pistis: Issuing Trusted and Authorized Certificates With Distributed Ledger and TEE. | TPDS | 2022 | TEE | [论文](https://doi.org/10.1109/TPDS.2021.3121562) |
| QShield: Protecting Outsourced Cloud Data Queries With Multi-User Access Control Based on SGX. | TPDS | 2021 | TEE | [论文](https://doi.org/10.1109/TPDS.2020.3024880) |

<a id="venue-focs"></a>

## FOCS（4）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| Secure Computation Meets Distributed Universal Optimality. | FOCS | 2023 | MPC | [论文](https://doi.org/10.1109/FOCS57990.2023.00144) |
| Geometry of Secure Two-party Computation. | FOCS | 2022 | MPC | [论文](https://doi.org/10.1109/FOCS54457.2022.00101) |
| The Round Complexity of Perfect MPC with Active Security and Optimal Resiliency. | FOCS | 2020 | MPC | [论文](https://doi.org/10.1109/FOCS46700.2020.00121) · [ePrint](https://eprint.iacr.org/2020/581) |
| Extractors and Secret Sharing Against Bounded Collusion Protocols. | FOCS | 2020 | MPC | [论文](https://doi.org/10.1109/FOCS46700.2020.00117) |

<a id="venue-stoc"></a>

## STOC（4）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| The Meta-complexity of Secret Sharing. | STOC | 2025 | MPC | [论文](https://doi.org/10.1145/3717823.3718161) · [ePrint](https://eprint.iacr.org/2025/046) |
| Succinct Computational Secret Sharing. | STOC | 2023 | MPC | [论文](https://doi.org/10.1145/3564246.3585127) · [ePrint](https://eprint.iacr.org/2023/955) |
| Quantum garbled circuits. | STOC | 2022 | MPC | [论文](https://doi.org/10.1145/3519935.3520073) · [arXiv](https://arxiv.org/abs/2006.01085) · [ePrint](https://eprint.iacr.org/2020/1401) |
| Better secret sharing via robust conditional disclosure of secrets. | STOC | 2020 | MPC | [论文](https://doi.org/10.1145/3357713.3384293) · [ePrint](https://eprint.iacr.org/2020/080) |

<a id="venue-icml"></a>

## ICML（4）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| GroupCover: A Secure, Efficient and Scalable Inference Framework for On-device Model Protection based on TEEs. | ICML | 2024 | TEE | [论文](https://proceedings.mlr.press/v235/zhang24bn.html) |
| Ditto: Quantization-aware Secure Inference of Transformers upon MPC. | ICML | 2024 | MPC | [论文](https://proceedings.mlr.press/v235/wu24d.html) · [arXiv](https://arxiv.org/abs/2405.05525) |
| Privacy-Preserving Feature Selection with Secure Multiparty Computation. | ICML | 2021 | MPC | [论文](http://proceedings.mlr.press/v139/li21e.html) · [arXiv](https://arxiv.org/abs/2102.03517) · [ePrint](https://eprint.iacr.org/2021/132) |
| Differentially Private Set Union. | ICML | 2020 | MPC | [论文](http://proceedings.mlr.press/v119/gopi20a.html) · [arXiv](https://arxiv.org/abs/2002.09745) |

<a id="venue-neurips"></a>

## NeurIPS（4）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| Private Set Union with Multiple Contributions. | NeurIPS | 2025 | MPC | [论文](http://papers.nips.cc/paper_files/paper/2025/hash/81a4bde3b5c6665dbd780b1fd577851f-Abstract-Conference.html) |
| LoRO: Real-Time on-Device Secure Inference for LLMs via TEE-Based Low Rank Obfuscation. | NeurIPS | 2025 | TEE | [论文](http://papers.nips.cc/paper_files/paper/2025/hash/1b86cf4b15cd83b6520d851eb7298228-Abstract-Conference.html) |
| AegisGuard: RL-Guided Adapter Tuning for TEE-Based Efficient &amp; Secure On-Device Inference. | NeurIPS | 2025 | TEE | [论文](http://papers.nips.cc/paper_files/paper/2025/hash/f308b5f207348484552997c536375654-Abstract-Conference.html) |
| CrypTen: Secure Multi-Party Computation Meets Machine Learning. | NeurIPS | 2021 | MPC | [论文](https://proceedings.neurips.cc/paper/2021/hash/2754518221cfbc8d25c13a06a4cb8421-Abstract.html) · [arXiv](https://arxiv.org/abs/2109.00984) |

<a id="venue-iclr"></a>

## ICLR（2）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| SecP-Tuning: Efficient Privacy-Preserving Prompt Tuning for Large Language Models via MPC. | ICLR | 2026 | MPC | [论文](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7f2e5d16c2c5ac161ce7aa44af35c0fe-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2506.15307) |
| SelectFormer in Data Markets: Privacy-Preserving and Efficient Data Selection for Transformers with Multi-Party Computation. | ICLR | 2025 | MPC | [论文](https://openreview.net/forum?id=2cF3f9t31y) |

<a id="venue-conf-woot"></a>

## conf/woot（2）

| 论文标题 | 会议 / 期刊 / 来源 | 年份 | 方向 | 资源链接 |
|---|---|---|---|---|
| PowerHooK: Enabling Software-Based Power Side Channels Against AMD SEV Technologies via Transient-Execution Replay. | conf/woot | 2026 | TEE | [论文](https://www.usenix.org/conference/woot26/presentation/oberhuber) |
| DisARMed: Attacking ARM TrustZone from Userspace with Memory Aliasing. | conf/woot | 2026 | TEE | [论文](https://www.usenix.org/conference/woot26/presentation/henes) |

<!-- PAPERS:END -->
