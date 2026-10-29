# 2026 · TEE · 含会议/期刊记录 · 第 1/1 页

[总目录](../PAPERS.md)

- **More Granular, Less Trust: Enforcing Intra-Process Isolation With Arm CCA in an Untrusted Management Environment.**
  2026-08-20 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2608.20584) · [TIFS](https://doi.org/10.1109/TIFS.2025.3634981)
  Kun Sun, Zhouqi Jiang, Zhaohui Chen, Jie Wang, Wei Zhou, Shiqi Liu, Yulai Xie

  <details><summary>摘要 / Abstract</summary>

  With the increasing adoption of confidential computing, security-sensitive applications are often deployed in confidential virtual machines (CVMs), which reduce reliance on third-party cloud providers. However, privilege attacks originating from the OS remain a significant threat in these environments. Existing finer-grained isolation schemes, such as SHELTER, provide process-level protection but are still vulnerable to intraprocess attacks and potential collusion between the OS and intra-process adversaries. Many current intra-process isolation techniques continue to depend on the OS to manage and enforce isolation domains, leading to a large Trusted Computing Base (TCB). This gap highlights the need for more granular, less trust-dependent confidential computing solutions. In this paper, we present CCAegis, a system that extends the Arm Confidential Compute Architecture (CCA) to enforce intra-process isolation of sensitive data and operations, safeguarding them from both intraprocess adversaries and the OS. We employ static analysis to track the flow of sensitive data and identify functions that handle such data. Permission-switching instructions are inserted at the function call and return points, adjusting permissions via the Granule Protection Table (GPT) to ensure that only designated functions can access the isolated data. Notably, CCAegis places trust solely in the Secure Monitor, which configures the GPTs and manages domain switching, thereby minimizing the TCB. We implemented CCAegis on both an official emulator and a real development board to assess its performance. Our experimental results show that CCAegis effectively isolates sensitive data and operations, with performance overheads ranging from 1.01x to 1.43x compared to the original version across real-world cryptographic workloads.

  匹配依据：TEE: arm cca, confidential compute architecture, confidential computing

  </details>

- **MaTEE: Efficiently Bridging the Semantic Gap in TrustZone via Arm Pointer Authentication.**
  2026-08-20 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2608.20583) · [TDSC](https://doi.org/10.1109/TDSC.2024.3445296)
  Yongpeng Gao, Xiang Li, Jie Wang, Jiajin Hu, Shiqi Liu

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) employ hardware-based isolation mechanisms to safeguard the confidentiality and integrity of sensitive code and data. One such prevalent implementation is Arm TrustZone, which partitions the system into the secure and normal (non-secure) worlds. However, this partitioning results in the secure world having very limited visibility into the operating information of the normal world, creating a semantic gap between these two worlds. Specifically, the secure world lacks an effective user identity authentication when receiving data requests from the normal world. Consequently, malicious Client Applications (CAs) in the normal world can deceive Trusted Applications (TAs) in the secure world by utilizing elaborate request parameters, compromising the sensitive data stored by other CAs. We systematically classify these Semantic Gap Vulnerabilities (SGVs) and propose a mate system for the TEE called MATEE to defend against SGVs. MATEE utilizes Arm Pointer Authentication (PA) to bind each request to the corresponding CA&#x27;s identity and then verifies the identity when the CA accesses sensitive data, thereby preventing malicious request forgery. In particular, MATEE isolates sensitive data of different CAs without modifying existing CAs and TAs. Our evaluation demonstrates that MATEE successfully defends against SGVs with a minimal runtime overhead (2.19%).

  匹配依据：TEE: trusted execution environments, trustzone

  </details>

- **DisT-FL: Enhancing Security for TEE-Based Aggregation in Federated Learning.**
  2026-06-03 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2606.04899) · [TIFS](https://doi.org/10.1109/TIFS.2026.3715108)
  Guoxing Chen, Jianzong Wang, Jianyu Niu, Zhen Huang, Guanlong Wu, Ju Yang, Yinqian Zhang

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs)-aided federated learning protocols emerge as promising solutions to counter server-side adversaries and ensure the trustworthiness of the server. In this paper, we dissect existing protocols and demonstrate that server-side adversaries can still manipulate client selection and replay aggregation to compromise system robustness and privacy, by exploiting TEE limitations, i.e., state rollback and I/O manipulation. To this end, we present DIST-FL, a distributed system of servers guarded by multiple TEEs forming an append-only ledger for privacy-preserved, robust FL aggregation. Specifically, DIST-FL ensures operation linearizability to thwart state rollback attacks and incorporates inputs from reliable servers to mitigate I/O manipulation threats. We implement DIST-FL and conduct evaluations in WAN settings. Experimental results demonstrate that DIST-FL can effectively counter the proposed attacks and match the single-TEE&#x27;s performance while offering a 6x throughput boost over its counterparts, leveraging TEE&#x27;s computational advantages.

  匹配依据：TEE: trusted execution environments

  </details>

- **kvTZ: TrustZone Virtualization for Commodity Arm-Based Platforms.**
  2026 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2025.3605807)
  Shih-Wei Li, Chun-Yen Lin

- **WorksetEnclave: Towards Optimizing Cold Starts in Confidential Serverless with Workset-Based Enclave Restore.**
  2026 · TEE · 含会议/期刊记录 · [ASPLOS](https://doi.org/10.1145/3779212.3790249)
  Xiaolong Yan, Weijuan Zhang, Qihang Zhou, Xiaoqi Jia, Feifan Qian, Zisen Wan, Wentao Yao

- **UIEE: Secure and Efficient User-space Isolated Execution Environment for Embedded TEE Systems.**
  2026 · TEE · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/uiee-secure-and-efficient-user-space-isolated-execution-environment-for-embedded-tee-systems/)
  Xinhui Shao, Haobo Li, Huaiyu Yan, Yier Jin, Ping Jiang, Xuandong Chen, Ming Yang, Junzhou Luo, Zhen Ling

- **TrustSearch: Toward Secure and Efficient Reverse Image Search via SGX.**
  2026 · TEE · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2026.3696201)
  Dayan Wu, Xiong Li, Hongwei Li, Jingwei Li, Xiaosong Zhang, Fang Zou, Ting Chen, Jia Zhang

- **Trust-V: Toward Secure and Reliable Storage for Trusted Execution Environments.**
  2026 · TEE · 含会议/期刊记录 · [ASPLOS](https://doi.org/10.1145/3779212.3790242)
  Seung-Kyun Han, Jin Soo Jang, Jiyeon Yang

- **Toward Secure and Efficient Driver Support for Embedded TEE Systems.**
  2026 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2026.3693739)
  Zhen Ling, Huaiyu Yan, Ming Yang, Xinhui Shao, Junzhou Luo, Ping Jiang, Xinwen Fu

- **Teamwork Makes TEE Work: Open and Resilient Remote Attestation on Decentralized Trust.**
  2026 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2402.08908) · [TDSC](https://doi.org/10.1109/TDSC.2025.3636884)
  Dawu Gu, Chi Zhang, Shipei Qu, Xiaolin Zhang, Kailun Qin, Tengfei Wang

  <details><summary>摘要 / Abstract</summary>

  Remote Attestation (RA) enables the integrity and authenticity of applications in Trusted Execution Environment (TEE) to be verified. Existing TEE RA designs employ a centralized trust model where they rely on a single provisioned secret key and a centralized verifier to establish trust for remote parties. This model is however brittle and can be untrusted under advanced attacks nowadays. Besides, most designs only have fixed procedures once deployed, making them hard to adapt to different emerging situations and provide resilient functionalities. Therefore, we propose JANUS, an open and resilient TEE RA scheme. To decentralize trust, we, on one hand, introduce Physically Unclonable Function (PUF) as an intrinsic root of trust (RoT) in TEE to directly provide physical trusted measurements. On the other hand, we design novel decentralized verification functions on smart contract with result audits and RA session snapshot. Furthermore, we design an automated switch mechanism that allows JANUS to remain resilient and offer flexible RA services under various situations. We provide a UC-based security proof and demonstrate the scalability and generality of JANUS by implementing an complete prototype.

  匹配依据：TEE: trusted execution environment

  </details>

- **TZ-LLM: Protecting On-Device Large Language Models with Arm TrustZone.**
  2026 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2511.13717) · [EuroSys](https://doi.org/10.1145/3767295.3769334)
  Jiacheng Shi, Zhichao Hua, Jinyu Gu, Zihan Zhao, Yang Yu, Xunjie Wang

  <details><summary>摘要 / Abstract</summary>

  Large Language Models (LLMs) deployed on mobile devices offer benefits like user privacy and reduced network latency, but introduce a significant security risk: the leakage of proprietary models to end users. To mitigate this risk, we propose a system design for protecting on-device LLMs using Arm Trusted Execution Environment (TEE), TrustZone. Our system addresses two primary challenges: (1) The dilemma between memory efficiency and fast inference (caching model parameters within TEE memory). (2) The lack of efficient and secure Neural Processing Unit (NPU) time-sharing between Rich Execution Environment (REE) and TEE. Our approach incorporates two key innovations. First, we employ pipelined restoration, leveraging the deterministic memory access patterns of LLM inference to prefetch parameters on demand, hiding memory allocation, I/O and decryption latency under computation time. Second, we introduce a co-driver design, creating a minimal data plane NPU driver in the TEE that collaborates with the full-fledged REE driver. This reduces the TEE TCB size and eliminates control plane reinitialization overhead during NPU world switches. We implemented our system on the emerging OpenHarmony OS and the llama.cpp inference framework, and evaluated it with various LLMs on an Arm Rockchip device. Compared to a strawman TEE baseline lacking our optimizations, our system reduces TTFT by up to 90.9% and increases decoding speed by up to 23.2%.

  匹配依据：TEE: trusted execution environment, trustzone

  </details>

- **TEEM³: Core-Independent and Cooperating Trusted Execution Environments.**
  2026 · TEE · 含会议/期刊记录 · [ASPLOS](https://doi.org/10.1145/3779212.3790232)
  Nils Asmussen, Friedrich Pauls, Carsten Weinhold, Sebastian Haas, Michael Roitzsch, Nilanjana Das, Nicholas Gordon, Stephan Gerhold

- **TEE.Fail: Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition.**
  2026 · TEE · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00101)
  Christina Garman, Stephan van Schaik, Alexander Seto, Jalen Chuang, Daniel Genkin, Nicolás Berrios

- **TDXRay: Microarchitectural Side-Channel Analysis of Intel TDX for Real-World Workloads.**
  2026 · TEE · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00170)
  Lukas Gerlach, Ruiyi Zhang, Phillipp Schoppmann, Michael Schwarz, Albert Cheu, Hosein Yavarzadeh, Daniel Moghimi, Adrià Gascón, Tristan Hornetz

- **SXGB: Secure and Efficient Vertical Federated XGBoost via Trusted Execution Environments.**
  2026 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2025.3626379)
  Hui Zhu, Rongxing Lu, Hui Li, Jiaqi Zhao, Fengwei Wang

- **SEED: A Minimal‑Footprint TEE Framework for Verifiable, Confidential Microservice Deployment.**
  2026 · TEE · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2026-0021)
  Md. Redowan Mahmud, Omar Jarkas, Ryan Kok Leong Ko, Naipeng Dong

- **PowerHooK: Enabling Software-Based Power Side Channels Against AMD SEV Technologies via Transient-Execution Replay.**
  2026 · TEE · 含会议/期刊记录 · [conf/woot](https://www.usenix.org/conference/woot26/presentation/oberhuber)
  Martin Unterguggenberger, Rishub Nagpal, Andreas Kogler, Mathias Oberhuber, Stefan Mangard, Martin Wistauder

- **Palladium: Guarding Neural Network Training With Confidential Computing.**
  2026 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2026.3694706)
  Juan Wang, Wenzhe Yi, Xiaoyang Xu, Hongxin Hu, Ziang Li, Mengda Yang

- **LÆGIS: Pinpointing and Addressing Performance Overheads of GPU-Based Confidential Computing.**
  2026 · TEE · 含会议/期刊记录 · [ISCA](https://doi.org/10.1109/ISCA66397.2026.00046)
  Adwait Jog, Yang Yang

- **It's TEEtime: Secure Interrupt Isolation for Normal-world Enclaves on Arm.**
  2026 · TEE · 含会议/期刊记录 · [TCHES](https://doi.org/10.46586/TCHES.V2026.I1.135-160)
  Ivan Puddu, Shweta Shinde, Moritz Schneider, Friederike Groschupp, Mark Kuhne, Srdjan Capkun

- **Enabling Confidential VMs Across Diverse ARM Platforms by Retrofitting TrustZone.**
  2026 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2026.3657770)
  Zeyu Mi, Haibo Chen, Yicong Wang

- **EXIA: Trusted Transitions for Enclaves via External-Input Attestation.**
  2026 · TEE · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/exia-trusted-transitions-for-enclaves-via-external-input-attestation/)
  Guoxing Chen, Sanchuan Chen, Yidi Kao, Haojin Zhu, Zhen Huang, Yan Meng

- **DisARMed: Attacking ARM TrustZone from Userspace with Memory Aliasing.**
  2026 · TEE · 含会议/期刊记录 · [conf/woot](https://www.usenix.org/conference/woot26/presentation/henes)
  Mihai Ordean, Jacqueline Henes, David Oswald, Matthew Bowden

- **Detecting Inconsistencies in Arm CCA's Formally Verified Specification.**
  2026 · TEE · 含会议/期刊记录 · [ASPLOS](https://doi.org/10.1145/3779212.3790152)
  Xiang Cheng, Taesoo Kim, Changho Choi, Bokdeuk Jeong

- **DNN Latency Sequencing: Extracting DNN Architectures from Intel SGX Enclaves with Single-Stepping Attacks.**
  2026 · TEE · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/dnn-latency-sequencing-extracting-dnn-architectures-from-intel-sgx-enclaves-with-single-stepping-attacks/)
  Chung Hwan Kim, Z. Berkay Celik, Minkyung Park, Zelun Kong, DaveTian

- **Complementing Confidential Computing Environment for Applications on Arm CCA.**
  2026 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2025.3604008)
  Xiapu Luo, Zhenyu Ning, Fengwei Zhang, Shoumeng Yan, Haoyang Huang, Yuxin Hu, Zhengyu He, Yiming Zhang

- **CROSS-TEE: A Distributed Trusted Execution Environment Architecture for Cross-Module Automotive Security.**
  2026 · TEE · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2026.3714115)
  Kui Ren, Shoumeng Yan, Kun Yang, Sisi Li, Hongliang Tian

- **Building Confidential Accelerator Computing Environment for Arm CCA.**
  2026 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2025.3615787)
  Tao Wei, Jiannong Cao, Zhengyu He, Fengwei Zhang, Chenxu Wang, Kevin Leach, Shoumeng Yan, Kun Lu, Zhenyu Ning, Yunjie Deng

- **BreakFAST: Confused Deputy Attack on Infinity Fabric to Break AMD SEV-SNP.**
  2026 · TEE · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00259)
  Shweta Shinde, Benedict Schlüter, Philipp Giersfeld

- **Battering RAM: Low-Cost Interposer Attacks on Confidential Computing via Dynamic Memory Aliasing.**
  2026 · TEE · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00052)
  Jo Van Bulck, David F. Oswald, Jesse De Meulemeester, Ingrid Verbauwhede

- **Anonymous Integrity Auditing Scheme Based on Trusted Execution Environment for Distributed Edge Computing.**
  2026 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2026.3670134)
  Jie Cui, Junjie Liu, Qingyang Zhang, Fengqun Wang, Jiaxin Li, Hong Zhong

- **AEX-NStep: Probabilistic Interrupt Counting Attacks on Intel SGX.**
  2026 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2510.14675) · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00035)
  Ivan Puddu, Nicolas Dutly, Friederike Groschupp, Kari Kostiainen, Srdjan Capkun

  <details><summary>摘要 / Abstract</summary>

  To mitigate interrupt-based stepping attacks (notably using SGX-Step), Intel introduced AEX-Notify, an ISA extension to Intel SGX that aims to prevent deterministic single-stepping. In this work, we introduce AEX-NStep, the first interrupt counting attack on AEX-Notify-enabled Enclaves. We show that deterministic single-stepping is not required for interrupt counting attacks to be practical and that, therefore, AEX-Notify does not entirely prevent such attacks. We specifically show that one of AEX-Notify&#x27;s security guarantees, obfuscated forward progress, does not hold, and we introduce two new probabilistic interrupt counting attacks. We use these attacks to construct a practical ECDSA key leakage attack on an AEX-Notify-enabled SGX enclave. Our results extend the original security analysis of AEX-Notify and inform the design of future mitigations.

  匹配依据：TEE: intel sgx, sgx, sgx enclave

  </details>
