# 2025 · TEE · 含会议/期刊记录 · 第 1/1 页

[总目录](../PAPERS.md)

- **TEEMS: A Trusted Execution Environment based Metadata-protected Messaging System**
  2025-06-12 · TEE · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2025-0119) · [IACR ePrint](https://eprint.iacr.org/2025/1102)
  Ian Goldberg, Sajin Sasy, Aaron Johnson

  <details><summary>摘要 / Abstract</summary>

  Ensuring privacy of online messaging remains a challenge. While the contents or data of online communications are often protected by end-to-end encryption, the metadata of communications are not. Metadata such as who is communicating with whom, how much, and how often, are leaked by popular messaging systems today. In the last four decades we have witnessed a rich literature of designs towards metadata-protecting communications systems (MPCS). While recent MPCS works often target metadata-protected messaging systems, no existing construction simultaneously attains four desirable properties for messaging systems, namely (i) low latency, (ii) high throughput, (iii) horizontal scalability, and (iv) asynchronicity. Existing designs often capture disjoint subsets of these properties. For example, PIR-based approaches achieve low latency and asynchronicity but have low throughput and lack horizontal scalability, mixnet-based approaches achieve high throughput and horizontal scalability but lack asynchronicity, and approaches based on trusted execution environments (TEEs) achieve high throughput and asynchronicity but lack horizontal scalability. In this work, we present TEEMS, the first MPCS designed for metadata-protected messaging that simultaneously achieves all four desirable properties. Our distributed TEE-based system uses an oblivious mailbox design to provide metadata-protected messaging. TEEMS presents novel oblivious routing protocols that adapt prior work on oblivious distributed sorting. Moreover, we introduce the notion of ID and token channels to circumvent shortcomings of prior designs. We empirically demonstrate TEEMS&#x27; ability to support $2^{20}$ clients engaged in metadata-protected conversations in under 1 s, with 205 cores, achieving an 18× improvement over prior work for latency and throughput, while supporting significantly better scalability and asynchronicity properties.

  匹配依据：TEE: trusted execution environment, trusted execution environments

  </details>

- **Attestable Builds: Compiling Verifiable Binaries on Untrusted Systems using Trusted Execution Environments**
  2025-05-05 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2505.02521) · [ACM CCS](https://doi.org/10.1145/3719027.3765128)
  Alastair R. Beresford, Daniel Hugenroth, Mario Lins, René Mayrhofer, Alastair Beresford

  <details><summary>摘要 / Abstract</summary>

  In this paper we present attestable builds, a new paradigm to provide strong source-to-binary correspondence in software artifacts. We tackle the challenge of opaque build pipelines that disconnect the trust between source code, which can be understood and audited, and the final binary artifact which is difficult to inspect. Our system uses modern trusted execution environments (TEEs) and sandboxed build containers to provide strong guarantees that a given artifact was correctly built from a specific source code snapshot. As such it complements existing approaches like reproducible builds which typically require time-intensive modifications to existing build configurations and dependencies, and require independent parties to continuously build and verify artifacts. In comparison, an attestable build requires only minimal changes to an existing project, and offers nearly instantaneous verification of the correspondence between a given binary and the source code and build pipeline used to construct it. We evaluate it by building open-source software libraries - focusing on projects which are important to the trust chain and have proven difficult to be built deterministically. The overhead (42 seconds start-up latency and 14% increase in build duration) is small in comparison to the overall build time. Importantly, our prototype can build complex projects such as LLVM Clang without requiring any modifications to their source code and build scripts. Finally, we formally model and verify the attestable build design to demonstrate its security against well-resourced adversaries.

  匹配依据：TEE: trusted execution environments

  </details>

- **Transparent Attested DNS for Confidential Computing Services**
  2025-03-18 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2503.14611) · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/delignat-lavaud)
  Antoine Delignat-Lavaud, Sylvan Clebsch, Christoph M. Wintersteiger, Manuel Costa, Kapil Vaswani, Cédric Fournet

  <details><summary>摘要 / Abstract</summary>

  Confidential services running in hardware-protected Trusted Execution Environments (TEEs) can provide higher security assurance, but this requires custom clients and protocols to distribute, update, and verify their attestation evidence. Compared with classic Internet security, built upon universal abstractions such as domain names, origins, and certificates, this puts a significant burden on service users and providers. In particular, Web browsers and other legacy clients do not get the same security guaranties as custom clients. We present a new approach for users to establish trust in confidential services. We propose attested DNS (aDNS): a name service that securely binds the attested implementation of confidential services to their domain names. ADNS enforces policies for all names in its zone of authority: any TEE that runs a service must present hardware attestation that complies with the domain-specific policy before registering keys and obtaining certificates for any name in this domain. ADNS provides protocols for zone delegation, TEE registration, and certificate issuance. ADNS builds on standards such as DNSSEC, DANE, ACME and Certificate Transparency. ADNS provides DNS transparency by keeping all records, policies, and attestations in a public append-only log, thereby enabling auditing and preventing targeted attacks. We implement aDNS as a confidential service using a fault-tolerant network of TEEs. We evaluate it using sample confidential services that illustrate various TEE platforms. On the client side, we provide a generic browser extension that queries and verifies attestation records before opening TLS connections, with negligible performance overhead, and we show that, with aDNS, even legacy Web clients benefit from confidential computing as long as some enlightened clients verify attestations to deter or blame malicious actors.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **ZIPNet: Low-bandwidth anonymous broadcast from (dis)Trusted Execution Environments**
  2025 · TEE · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2025-0058) · [IACR ePrint](https://eprint.iacr.org/2024/1227)
  Rui Wang, Ian Miers, Michael Rosenberg, Maurice Shih, Zhenyu Zhao, Fan Zhang

  <details><summary>摘要 / Abstract</summary>

  Anonymous Broadcast Channels (ABCs) allow a group of clients to announce messages without revealing the exact author. Modern ABCs operate in a client-server model, where anonymity depends on some threshold (e.g., 1 of 2) of servers being honest. ABCs are an important application in their own right, e.g., for activism and whistleblowing. Recent work on ABCs (Riposte, Blinder) has focused on minimizing the bandwidth cost to clients and servers when supporting large broadcast channels for such applications. But, particularly for low bandwidth settings, they impose large costs on servers, make cover traffic costly, and make volunteer operators unlikely. In this paper, we describe the design, implementation, and evaluation of ZIPNet, an anonymous broadcast channel that 1) scales to hundreds of anytrust servers by minimizing the computational costs of each server, 2) substantially reduces the servers’ bandwidth costs by outsourcing the aggregation of client messages to untrusted (for privacy) infrastructure, and 3) supports cover traffic that is both cheap for clients to produce and for servers to handle.

  匹配依据：TEE: trusted execution environments

  </details>

- **WireTap: Breaking Server SGX via DRAM Bus Interposition.**
  2025 · TEE · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3719027.3765204)
  Christina Garman, Stephan van Schaik, Jalen Chuang, Alexander Seto, Samy Amer, Daniel Genkin, Oytun Kuday Duran

- **The Road to Trust: Building Enclaves within Confidential VMs**
  2025 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2402.11438) · [NDSS](https://www.ndss-symposium.org/ndss-paper/the-road-to-trust-building-enclaves-within-confidential-vms/)
  Shijun Zhao, XiaoFeng Wang, Shoumeng Yan, Dan Meng, Linke Song, Benshan Mei, Shuang Liu, Wenhao Wang, Rui Hou

  <details><summary>摘要 / Abstract</summary>

  Integrity is critical for maintaining system security, as it ensures that only genuine software is loaded onto a machine. Although confidential virtual machines (CVMs) function within isolated environments separate from the host, it is important to recognize that users still encounter challenges in maintaining control over the integrity of the code running within the trusted execution environments (TEEs). The presence of a sophisticated operating system (OS) raises the possibility of dynamically creating and executing any code, making user applications within TEEs vulnerable to interference or tampering if the guest OS is compromised. To address this issue, this paper introduces NestedSGX, a framework which leverages virtual machine privilege level (VMPL), a recent hardware feature available on AMD SEV-SNP to enable the creation of hardware enclaves within the guest VM. Similar to Intel SGX, NestedSGX considers the guest OS untrusted for loading potentially malicious code. It ensures that only trusted and measured code executed within the enclave can be remotely attested. To seamlessly protect existing applications, NestedSGX aims for compatibility with Intel SGX by simulating SGX leaf functions. We have also ported the SGX SDK and the Occlum library OS to NestedSGX, enabling the use of existing SGX toolchains and applications in the system. Performance evaluations show that context switches in NestedSGX take about 32,000 -- 34,000 cycles, approximately $1.9\times$ -- $2.1\times$ higher than that of Intel SGX. NestedSGX incurs minimal overhead in most real-world applications, with an average overhead below 2% for computation and memory intensive workloads and below 15.68% for I/O intensive workloads.

  匹配依据：TEE: amd sev, hardware enclaves, intel sgx, sgx, trusted execution environments

  </details>

- **Tacco: A Framework for Ensuring the Security of Real-World TEEs via Formal Verification.**
  2025 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2025.3594594)
  Kui Ren, Jilin Hu, Yongwang Zhao, Shuangquan Pan, Zuohua Ding

- **TLBlur: Compiler-Assisted Automated Hardening against Controlled Channels on Off-the-Shelf Intel SGX Platforms.**
  2025 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/vanoverloop)
  Jo Van Bulck, Mathias Payer, Andrés Sánchez, Frank Piessens, Flavio Toffalini, Daan Vanoverloop

- **TDXploit: Novel Techniques for Single-Stepping and Cache Attacks on Intel TDX.**
  2025 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/rauscher)
  Daniel Gruss, Luca Wilke, Fabian Rauscher, Hannes Weissteiner, Thomas Eisenbarth

- **SCRUTINIZER: Towards Secure Forensics on Compromised TrustZone.**
  2025 · TEE · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/scrutinizer-towards-secure-forensics-on-compromised-trustzone/)
  Shoumeng Yan, Fengwei Zhang, Xiapu Luo, Zhenkai Liang, Xuhua Ding, Tao Wei, Zhengyu He, Rui Hou, Yiming Zhang

- **Revisiting SGX-Based Encrypted Deduplication via PoW-Before-Encryption and Eliminating Redundant Computations.**
  2025 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2024.3476288)
  Xiaowei Ge, Guanxiong Ha, Zhen Su, Chunfu Jia, Yuchen Chen

- **Reload+Reload: Exploiting Cache and Memory Contention Side Channel on AMD SEV.**
  2025 · TEE · 含会议/期刊记录 · [ASPLOS](https://doi.org/10.1145/3676641.3716017)
  Shih-Wei Li, Li-Chung Chiang

- **Rakis: Secure Fast I/O Primitives Across Trust Boundaries on Intel SGX.**
  2025 · TEE · 含会议/期刊记录 · [EuroSys](https://doi.org/10.1145/3689031.3696090)
  Dmitrii Kuvaiskii, Fan Sang, Taesoo Kim, Mansour Alharthi, Mona Vij

- **RMPocalypse: How a Catch-22 Breaks AMD SEV-SNP.**
  2025 · TEE · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3719027.3765233)
  Shweta Shinde, Benedict Schlüter

- **RContainer: A Secure Container Architecture through Extending ARM CCA Hardware Primitives.**
  2025 · TEE · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/rcontainer-a-secure-container-architecture-through-extending-arm-cca-hardware-primitives/)
  Jiayun Chen, Zhenyu Song, Shaowen Xu, Qihang Zhou, Peng Liu, Wenzhuo Cao, Xiaoqi Jia, Shengzhi Zhang

- **Portal: Fast and Secure Device Access with Arm CCA for Modern Arm Mobile System-on-Chips (SoCs).**
  2025 · TEE · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP61157.2025.00013)
  Jaehyuk Lee, Xiaokuan Zhang, Fan Sang, Taesoo Kim

- **OPSA: Efficient and Verifiable One-Pass Secure Aggregation with TEE for Federated Learning**
  2025 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2025.3565640) · [IACR ePrint](https://eprint.iacr.org/2024/476)
  Jinsong Han, Zhiguo Wan, Zhangshuang Guan, Yulin Zhao

  <details><summary>摘要 / Abstract</summary>

  Federated learning enables collaborative model training while preserving data privacy by keeping data local. To protect user privacy during model aggregation, secure aggregation (SA) protocols are widely adopted to mask models. However, existing SA protocols require at least three round trips per aggregation and lack mechanisms to verify aggregation results. Verifiable SA addresses the verification gap but incurs high communication costs. TEE-based SA minimizes round trips but faces computational bottlenecks due to TEE&#x27;s limited physical memory, especially when handling larger models or numerous clients. In this work, we introduce OPSA, an efficient and verifiable one-pass SA protocol based on TEE. By handling client dropouts via server-side TEE, OPSA enables the server to aggregate masked models in a single pass, significantly reducing round trips. To mitigate TEE&#x27;s limitations, OPSA offloads tasks like model aggregation and mask elimination outside TEE, with only shared keys processed within TEE. Building on this design, we propose KhPRF-OPSA (single masking) and POT-OPSA (double masking) protocols, both incorporating novel cryptographic primitives. Furthermore, OPSA integrates commitment and signature mechanisms to ensure result verifiability with only $O(1)$ additional communication overhead per client. Compared to state-of-the-art schemes, OPSA achieves a 2$\sim$10$\times$ speedup in multi-round aggregation while guaranteeing result verification.

  匹配依据：TEE: tee (context)

  </details>

- **OBIR-tree: An Efficient Oblivious Index for Spatial Keyword Queries on Secure Enclaves.**
  2025 · TEE · 含会议/期刊记录 · [PACMMOD / SIGMOD](https://doi.org/10.1145/3709708)
  Xiangyu Wang, Jianfeng Ma, Zesen Liu, Zikai Ye, Dan Zhu

- **MuEOC: Efficient SGX-Based Multi-Key Homomorphic Outsourcing Computation for E-Health System.**
  2025 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2024.3476483)
  Zhenfu Cao, Jun Zhou, Yisong Wang, Kim-Kwang Raymond Choo, Xiaolei Dong

- **Microft: Exploring and Mitigating Cross-State Control-Flow Hijacking Attacks on ARM Cortex-M TrustZone.**
  2025 · TEE · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2025.3625394)
  Zheyuan Ma, Lukasz Ziarek, Xi Tan, Ziming Zhao, Shambhu J. Upadhyaya, Hongxin Hu, Ning Zhang

- **MDPeek: Breaking Balanced Branches in SGX with Memory Disambiguation Unit Side Channels.**
  2025 · TEE · 含会议/期刊记录 · [ASPLOS](https://doi.org/10.1145/3676641.3716004)
  Wenjian He, Dongsheng Wang, Trevor E. Carlson, Chang Liu, Shuaihu Feng, Yuan Li, Yongqiang Lyu

- **LoRO: Real-Time on-Device Secure Inference for LLMs via TEE-Based Low Rank Obfuscation.**
  2025 · TEE · 含会议/期刊记录 · [NeurIPS](http://papers.nips.cc/paper_files/paper/2025/hash/1b86cf4b15cd83b6520d851eb7298228-Abstract-Conference.html)
  Jianhua Liu, Gaojian Xiong, Jianwei Liu, Yu Sun, Jian Cui

- **LETIndex: A Secure Learned Index with TEE.**
  2025 · TEE · 含会议/期刊记录 · [PVLDB](https://doi.org/10.14778/3750601.3750682)
  Shuting Cao, Zeping Niu, Guoliang Li

- **Heracles: Chosen Plaintext Attack on AMD SEV-SNP.**
  2025 · TEE · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3719027.3765209)
  Shweta Shinde, Benedict Schlüter, Christoph Wech

- **Game of Arrows: On the (In-)Security of Weight Obfuscation for On-Device TEE-Shielded LLM Partition Algorithms.**
  2025 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-pengli)
  Zheng Zhang, Yifeng Cai, Bingyou Dong, Huanran Xue, Pengli Wang, Junlin Liu, Yao Zhang, Ye Wu, Ziqi Zhang

- **GPU Travelling: Efficient Confidential Collaborative Training with TEE-Enabled GPUs.**
  2025 · TEE · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3719027.3765029)
  Enriquillo Valdez, Shixuan Zhao, Hani Jamjoom, Salman Ahmed, Zhongshu Gu, Zhiqiang Lin

- **Formal Security Analysis of the AMD SEV-SNP Software Interface**
  2025 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2403.10296) · [TDSC](https://doi.org/10.1109/TDSC.2025.3528737)
  Petar Paradzik, Marko Horvat, Ante Derek, Petar Paradžik

  <details><summary>摘要 / Abstract</summary>

  AMD Secure Encrypted Virtualization technologies enable confidential computing by protecting virtual machines from highly privileged software such as hypervisors. In this work, we develop the first, comprehensive symbolic model of the software interface of the latest SEV iteration called SEV Secure Nested Paging (SEV-SNP). Our model covers remote attestation, key derivation, page swap and live migration. We analyze the security of the software interface of SEV-SNP and formally prove that most critical secrecy, authentication, attestation and freshness properties do indeed hold in the model. Furthermore, we find that the platform-agnostic nature of messages exchanged between SNP guests and the AMD Secure Processor firmware presents a potential weakness in the design. We show how this weakness leads to formal attacks on multiple security properties, including the partial compromise of attestation report integrity, and discuss possible impacts and mitigations.

  匹配依据：TEE: amd sev, confidential computing, secure encrypted virtualization, sev snp

  </details>

- **Dorami: Privilege Separating Security Monitor on RISC-V TEEs**
  2025 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2410.03653) · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/kuhne)
  Shweta Shinde, Mark Kuhne, Stavros Volos

  <details><summary>摘要 / Abstract</summary>

  TEE implementations on RISC-V offer an enclave abstraction by introducing a trusted component called the security monitor (SM). The SM performs critical tasks such as isolating enclaves from each other as well as from the OS by using privileged ISA instructions that enforce the physical memory protection. However, the SM executes at the highest privilege layer on the platform (machine-mode) along side firmware that is not only large in size but also includes third-party vendor code specific to the platform. In this paper, we present Dorami - a privilege separation approach that isolates the SM from the firmware thus reducing the attack surface on TEEs. Dorami re-purposes existing ISA features to enforce its isolation and achieves its goals without large overheads.

  匹配依据：TEE: tees (context)

  </details>

- **CounterSEVeillance: Performance-Counter Attacks on AMD SEV-SNP.**
  2025 · TEE · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/counterseveillance-performance-counter-attacks-on-amd-sev-snp/)
  Daniel Gruss, Stefan Gast, Robin Leander Schröder, Hannes Weissteiner

- **BiTDB: Constructing A Built-in TEE Secure Database for Embedded Systems (Extended Abstract).**
  2025 · TEE · 含会议/期刊记录 · [ICDE](https://doi.org/10.1109/ICDE65448.2025.00393)
  Jianfeng Ma, Chengyan Ma, Di Lu, Ning Xi, Chaoyue Lv, Xiaohong Jiang, Yulong Shen

- **BadRAM: Practical Memory Aliasing Attacks on Trusted Execution Environments.**
  2025 · TEE · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP61157.2025.00104)
  David F. Oswald, Jo Van Bulck, Jesse De Meulemeester, Luca Wilke, Thomas Eisenbarth, Ingrid Verbauwhede

- **AegisGuard: RL-Guided Adapter Tuning for TEE-Based Efficient &amp; Secure On-Device Inference.**
  2025 · TEE · 含会议/期刊记录 · [NeurIPS](http://papers.nips.cc/paper_files/paper/2025/hash/f308b5f207348484552997c536375654-Abstract-Conference.html)
  Che Wang, Yinggui Wang, Yurong Hao, Tiantong Wang, Wei Yang Bryan Lim, Yang Cao, Zhong Chen, Ziqi Zhang, Jianbo Gao, Tao Wei

- **ASGARD: Protecting On-Device Deep Neural Networks with Virtualization-Based Trusted Execution Environments.**
  2025 · TEE · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/asgard-protecting-on-device-deep-neural-networks-with-virtualization-based-trusted-execution-environments/)
  Dokyung Song, Minhee Kim, Joonkyo Jung, Myungsuk Moon

- **A System Framework to Symbolically Explore Intel TDX Module Execution.**
  2025 · TEE · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3719027.3765212)
  Pansilu Pitigalaarachchi, Xuhua Ding
