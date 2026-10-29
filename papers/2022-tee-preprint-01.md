# 2022 · TEE · 仅预印本来源 · 第 1/1 页

[总目录](../PAPERS.md)

- **Efficiently Hardening SGX Enclaves against Memory Access Pattern Attacks via Dynamic Program Partitioning**
  2022-12-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2212.12656)
  Yuzhe Tang, Kai Li, Yibo Wang, Jiaqi Chen, Cheng Xu

  <details><summary>摘要 / Abstract</summary>

  Intel SGX is known to be vulnerable to a class of practical attacks exploiting memory access pattern side-channels, notably page-fault attacks and cache timing attacks. A promising hardening scheme is to wrap applications in hardware transactions, enabled by Intel TSX, that return control to the software upon unexpected cache misses and interruptions so that the existing side-channel attacks exploiting these micro-architectural events can be detected and mitigated. However, existing hardening schemes scale only to small-data computation, with a typical working set smaller than one or few times (e.g., $8$ times) of a CPU data cache. This work tackles the data scalability and performance efficiency of security hardening schemes of Intel SGX enclaves against memory-access pattern side channels. The key insight is that the size of TSX transactions in the target computation is critical, both performance- and security-wise. Unlike the existing designs, this work dynamically partitions target computations to enlarge transactions while avoiding aborts, leading to lower performance overhead and improved side-channel security. We materialize the dynamic partitioning scheme and build a C++ library to monitor and model cache utilization at runtime. We further build a data analytical system using the library and implement various external oblivious algorithms. Performance evaluation shows that our work can effectively increase transaction size and reduce the execution time by up to two orders of magnitude compared with the state-of-the-art solutions.

  匹配依据：TEE: intel sgx, sgx, sgx enclaves

  </details>

- **HyperEnclave: An Open and Cross-platform Trusted Execution Environment**
  2022-12-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2212.04197)
  Yuekai Jia, Shuang Liu, Wenhao Wang, Yu Chen, Zhengde Zhai, Shoumeng Yan, Zhengyu He

  <details><summary>摘要 / Abstract</summary>

  A number of trusted execution environments (TEEs) have been proposed by both academia and industry. However, most of them require specific hardware or firmware changes and are bound to specific hardware vendors (such as Intel, AMD, ARM, and IBM). In this paper, we propose HyperEnclave, an open and cross-platform process-based TEE that relies on the widely-available virtualization extension to create the isolated execution environment. In particular, HyperEnclave is designed to support the flexible enclave operation modes to fulfill the security and performance demands under various enclave workloads. We provide the enclave SDK to run existing SGX programs on HyperEnclave with little or no source code changes. We have implemented HyperEnclave on commodity AMD servers and deployed the system in a world-leading FinTech company to support real-world privacy-preserving computations. The evaluation on both micro-benchmarks and application benchmarks shows the design of HyperEnclave introduces only a small overhead.

  匹配依据：TEE: sgx, trusted execution environment, trusted execution environments

  </details>

- **TokenWeaver: Privacy Preserving and Post-Compromise Secure Attestation**
  2022-12-06 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1691)
  Cas Cremers, Gal Horowitz, Charlie Jacomme, Eyal Ronen

  <details><summary>摘要 / Abstract</summary>

  Modern attestation based on Trusted Execution Environments (TEEs) can significantly reduce the risk of secret compromise, allowing users to securely perform sensitive computations such as running cryptographic protocols for authentication across security critical services. However, this has also made TEEs a high-value attack target, driving an arms race between novel compromise attacks and continuous TEEs updates. Ideally, we want to achieve Post-Compromise Security (PCS): even after a TEE compromise, we can update it back into a secure state. However, at the same time, we would like to guarantee the privacy of users, in particular preventing providers (such as Intel, Google, or Samsung) or services from tracking users across services. This requires unlinkability, which seems incompatible with standard PCS healing mechanisms. In this work, we develop TokenWeaver, the first privacy-preserving post-compromise secure attestation method with automated formal proofs for its core properties. We base our construction on weaving together two types of token chains, one of which is linkable and the other is unlinkable. We provide the full formal models based on the Tamarin and DeepSec provers, including protocol, security properties, and proofs for reproducibility, as well as a proof-of-concept implementation in python that shows the simplicity and applicability of our solution.

  匹配依据：TEE: trusted execution environments

  </details>

- **Confidential High-Performance Computing in the Public Cloud**
  2022-12-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2212.02378)
  Keke Chen

  <details><summary>摘要 / Abstract</summary>

  High-Performance Computing (HPC) in the public cloud democratizes the supercomputing power that most users cannot afford to purchase and maintain. Researchers have studied its viability, performance, and usability. However, HPC in the cloud has a unique feature -- users have to export data and computation to somewhat untrusted cloud platforms. Users will either fully trust cloud providers to protect from all kinds of attacks or keep sensitive assets in-house instead. With the recent deployment of the Trusted Execution Environment (TEE) in the cloud, confidential computing for HPC in the cloud is becoming practical for addressing users&#x27; privacy concerns. This paper discusses the threat models, unique challenges, possible solutions, and significant gaps, focusing on TEE-based confidential HPC computing. We hope this discussion will improve the understanding of this new topic for HPC in the cloud and promote new research directions.

  匹配依据：TEE: confidential computing, trusted execution environment

  </details>

- **Trusted Hart for Mobile RISC-V Security**
  2022-11-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.10299)
  Vladimir Ushakov, Sampo Sovio, Qingchao Qi, Vijayanand Nayani, Valentin Manea, Philip Ginzboorg, Jan Erik Ekberg

  <details><summary>摘要 / Abstract</summary>

  The majority of mobile devices today are based on Arm architecture that supports the hosting of trusted applications in Trusted Execution Environment (TEE). RISC-V is a relatively new open-source instruction set architecture that was engineered to fit many uses. In one potential RISC-V usage scenario, mobile devices could be based on RISC-V hardware. We consider the implications of porting the mobile security stack on top of a RISC-V system on a chip, identify the gaps in the open-source Keystone framework for building custom TEEs, and propose a security architecture that, among other things, supports the GlobalPlatform TEE API specification for trusted applications. In addition to Keystone enclaves the architecture includes a Trusted Hart -- a normal core that runs a trusted operating system and is dedicated for security functions, like control of the device&#x27;s keystore and the management of secure peripherals. The proposed security architecture for RISC-V platform is verified experimentally using the HiFive Unleashed RISC-V development board.

  匹配依据：TEE: trusted execution environment

  </details>

- **Securing Access to Untrusted Services From TEEs with GateKeeper**
  2022-11-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.07185)
  Meni Orenbach, Bar Raveh, Alon Berkenstadt, Yan Michalevsky, Shachar Itzhaky, Mark Silberstein

  <details><summary>摘要 / Abstract</summary>

  Applications running in Trusted Execution Environments (TEEs) commonly use untrusted external services such as host File System. Adversaries may maliciously alter the normal service behavior to trigger subtle application bugs that would have never occurred under correct service operation, causing data leaks and integrity violations. Unfortunately, existing manual protections are incomplete and ad-hoc, whereas formally-verified ones require special expertise. We introduce GateKeeper, a framework to develop mitigations and vulnerability checkers for such attacks by leveraging lightweight formal models of untrusted services. With the attack seen as a violation of a services&#x27; functional correctness, GateKeeper takes a novel approach to develop a comprehensive model of a service without requiring formal methods expertise. We harness available testing suites routinely used in service development to tighten the model to known correct service implementation. GateKeeper uses the resulting model to automatically generate (1) a correct-by-construction runtime service validator in C that is linked with a trusted application and guards each service invocation to conform to the model; and (2) a targeted model-driven vulnerability checker for analyzing black-box applications. We evaluate GateKeeper on Intel SGX enclaves. We develop comprehensive models of a POSIX file system and OS synchronization primitives while using thousands of existing test suites to tighten their models to the actual Linux implementations. We generate the validator and integrate it with Graphene-SGX, and successfully protect unmodified Memcached and SQLite with negligible overheads. The generated vulnerability checker detects novel vulnerabilities in the Graphene-SGX protection layer and production applications.

  匹配依据：TEE: intel sgx, sgx, sgx enclaves, trusted execution environments

  </details>

- **It's TEEtime: A New Architecture Bringing Sovereignty to Smartphones**
  2022-11-09 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.05206)
  Friederike Groschupp, Mark Kuhne, Moritz Schneider, Ivan Puddu, Shweta Shinde, Srdjan Capkun

  <details><summary>摘要 / Abstract</summary>

  Modern smartphones are complex systems in which control over phone resources is exercised by phone manufacturers, OS vendors, and users. These stakeholders have diverse and often competing interests. Barring some exceptions, users entrust their security and privacy to OS vendors (Android and iOS) and need to accept their constraints. Manufacturers protect their firmware and peripherals from the OS by executing in the highest privilege and leveraging dedicated CPUs and TEEs. OS vendors need to trust the highest privileged code deployed by manufacturers. This division of control over the phone is not ideal for OS vendors and is even more disadvantageous for the users. Users are generally limited in what applications they can install on their devices, in the privacy model and trust assumptions of the existing applications, and in the functionalities that applications can have. We propose TEEtime, a new smartphone architecture based on trusted execution allowing to balance the control different stakeholders exert over phones. More leveled control over the phone means that no stakeholder is more privileged than the others. In particular, TEEtime makes users sovereign over their phones: It enables them to install sensitive applications in isolated domains with protected access to selected peripherals alongside an OS. TEEtime achieves this while maintaining compatibility with the existing smartphone ecosystem and without relying on virtualization; it only assumes trust in a phone&#x27;s firmware. TEEtime is the first TEE architecture that allows isolated execution domains to gain protected and direct access to peripherals. TEEtime is based on Armv8-A and achieves peripheral isolation using a novel mechanism based on memory and interrupt controller protection. We demonstrate the feasibility of our design by implementing a prototype of TEEtime, and by running exemplary sensitive applications.

  匹配依据：TEE: tees (context)

  </details>

- **Verifying RISC-V Physical Memory Protection**
  2022-11-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.02179)
  Kevin Cheang, Cameron Rasmussen, Dayeol Lee, David W. Kohlbrenner, Krste Asanović, Sanjit A. Seshia

  <details><summary>摘要 / Abstract</summary>

  We formally verify an open-source hardware implementation of physical memory protection (PMP) in RISC-V, which is a standard feature used for memory isolation in security critical systems such as the Keystone trusted execution environment. PMP provides per-hardware-thread machine-mode control registers that specify the access privileges for physical memory regions. We first formalize the functional property of the PMP rules based on the RISC-V ISA manual. Then, we use the LIME tool to translate an open-source implementation of the PMP hardware module written in Chisel to the UCLID5 formal verification language. We encode the formal specification in UCLID5 and verify the functional correctness of the hardware. This is an initial effort towards verifying the Keystone framework, where the trusted computing base (TCB) relies on PMP to provide security guarantees such as integrity and confidentiality.

  匹配依据：TEE: trusted execution environment

  </details>

- **Empowering Data Centers for Next Generation Trusted Computing**
  2022-11-01 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.00306)
  Aritra Dhar, Supraja Sridhara, Shweta Shinde, Srdjan Capkun, Renzo Andri

  <details><summary>摘要 / Abstract</summary>

  Modern data centers have grown beyond CPU nodes to provide domain-specific accelerators such as GPUs and FPGAs to their customers. From a security standpoint, cloud customers want to protect their data. They are willing to pay additional costs for trusted execution environments such as enclaves provided by Intel SGX and AMD SEV. Unfortunately, the customers have to make a critical choice -- either use domain-specific accelerators for speed or use CPU-based confidential computing solutions. To bridge this gap, we aim to enable data-center scale confidential computing that expands across CPUs and accelerators. We argue that having wide-scale TEE-support for accelerators presents a technically easier solution, but is far away from being a reality. Instead, our hybrid design provides enclaved execution guarantees for computation distributed over multiple CPU nodes and devices with/without TEE support. Our solution scales gracefully in two dimensions -- it can handle a large number of heterogeneous nodes and it can accommodate TEE-enabled devices as and when they are available in the future. We observe marginal overheads of $0.42$--$8\%$ on real-world AI data center workloads that are independent of the number of nodes in the data center. We add custom TEE support to two accelerators (AI and storage) and integrate it into our solution, thus demonstrating that it can cater to future TEE devices.

  匹配依据：TEE: amd sev, confidential computing, intel sgx, trusted execution environments

  </details>

- **uBFT: Microsecond-scale BFT using Disaggregated Memory \[Extended Version\]**
  2022-10-31 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.17174)
  Marcos K. Aguilera, Naama Ben-David, Rachid Guerraoui, Antoine Murat, Athanasios Xygkis, Igor Zablotchi

  <details><summary>摘要 / Abstract</summary>

  We propose uBFT, the first State-Machine Replication (SMR) system to achieve microsecond-scale latency in data centers, while using only $2f{+}1$ replicas to tolerate $f$ Byzantine failures. The Byzantine Fault Tolerance (BFT) provided by uBFT is essential as pure crashes appear to be a mere illusion with real-life systems reportedly failing in many unexpected ways. uBFT relies on a small non-tailored trusted computing base -- disaggregated memory -- and consumes a practically bounded amount of memory (both local and disaggregated). uBFT is based on a novel abstraction called Consistent Tail Broadcast, which we use to prevent equivocation while bounding memory. We implement uBFT using RDMA-based disaggregated memory and obtain an end-to-end latency of as little as 10us. This is at least 50$\times$ faster than MinBFT , a state of the art $2f{+}1$ BFT SMR based on Intel&#x27;s SGX. We use uBFT to replicate two key-value stores (Memcached and Redis), as well as a financial order matching engine (Liquibook). These applications have low latency (up to 20us) and become Byzantine tolerant with as little as 10us more. The price for uBFT is a small amount of reliable disaggregated memory (less than 1 MiB), which in our prototype consists of a small number of memory servers connected through RDMA and replicated for fault tolerance.

  匹配依据：TEE: sgx

  </details>

- **Hardware-Supported Cryptographic Protection of Random Access Memory**
  2022-10-27 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1472)
  Roberto Avanzi, Ionut Mihalcea, David Schall, Héctor Montaner, Andreas Sandberg

  <details><summary>摘要 / Abstract</summary>

  Confidential Computing is the protection of data in use from access or modification by any unauthorized agent, including privileged software. For example, in Intel SGX (Client and Scalable versions) and TDX, AMD SEV, Arm CCA, and IBM Ultravisor this protection is implemented via access control policies. Some of these architectures also include memory protection schemes relying on cryptography, to protect against physical attacks. We review and classify such schemes, from academia and industry, according to protection levels corresponding of adversaries with varying capabilities, budget, and strategy. The building blocks of all memory protection schemes are encryption and integrity primitives and modes of operation, as well as anti-replay structures. We review these building blocks, consider their possible combinations, and evaluate the performance impact of the resulting schemes. We present a framework for performance evaluation in a simulated system. To understand the best and worst case overhead, systems with varying load levels are considered. We propose new solutions to further reduce the performance and memory overheads of such technologies. Advanced counter compression techniques make it viable to store counters used for replay protection in a physically protected memory. By additionally repurposing some ECC bits to store integrity tags, we can provide the highest levels of confidentiality, integrity, and replay protection at a hitherto unattained performance penalty, namely 3.32%, even under extreme load and at costs that make them reasonable in data centers. Combinations of technologies that are suitable for client devices are also discussed.

  匹配依据：TEE: amd sev, arm cca, confidential computing, intel sgx

  </details>

- **Cipherfix: Mitigating Ciphertext Side-Channel Attacks in Software**
  2022-10-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.13124)
  Jan Wichelmann, Anna Pätschke, Luca Wilke, Thomas Eisenbarth

  <details><summary>摘要 / Abstract</summary>

  Trusted execution environments (TEEs) provide an environment for running workloads in the cloud without having to trust cloud service providers, by offering additional hardware-assisted security guarantees. However, main memory encryption as a key mechanism to protect against system-level attackers trying to read the TEE&#x27;s content and physical, off-chip attackers, is insufficient. The recent Cipherleaks attacks infer secret data from TEE-protected implementations by analyzing ciphertext patterns exhibited due to deterministic memory encryption. The underlying vulnerability, dubbed the ciphertext side-channel, is neither protected by state-of-the-art countermeasures like constant-time code nor by hardware fixes. Thus, in this paper, we present a software-based, drop-in solution that can harden existing binaries such that they can be safely executed under TEEs vulnerable to ciphertext side-channels, without requiring recompilation. We combine taint tracking with both static and dynamic binary instrumentation to find sensitive memory locations, and mitigate the leakage by masking secret data before it gets written to memory. This way, although the memory encryption remains deterministic, we destroy any secret-dependent patterns in encrypted memory. We show that our proof-of-concept implementation protects various constant-time implementations against ciphertext side-channels with reasonable overhead.

  匹配依据：TEE: trusted execution environments

  </details>

- **Partially Trusting the Service Mesh Control Plane**
  2022-10-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.12610)
  Constantin Adam, Abdulhamid Adebayo, Hubertus Franke, Edward Snible, Tobin Feldman-Fitzthum, James Cadden, Nerla Jean-Louis

  <details><summary>摘要 / Abstract</summary>

  Zero Trust is a novel cybersecurity model that focuses on continually evaluating trust to prevent the initiation and horizontal spreading of attacks. A cloud-native Service Mesh is an example of Zero Trust Architecture that can filter out external threats. However, the Service Mesh does not shield the Application Owner from internal threats, such as a rogue administrator of the cluster where their application is deployed. In this work, we are enhancing the Service Mesh to allow the definition and reinforcement of a Verifiable Configuration that is defined and signed off by the Application Owner. Backed by automated digital signing solutions and confidential computing technologies, the Verifiable Configuration allows changing the trust model of the Service Mesh, from the data plane fully trusting the control plane to partially trusting it. This lets the application benefit from all the functions provided by the Service Mesh (resource discovery, traffic management, mutual authentication, access control, observability), while ensuring that the Cluster Administrator cannot change the state of the application in a way that was not intended by the Application Owner.

  匹配依据：TEE: confidential computing

  </details>

- **DOT-M: A Dual Offline Transaction Scheme of Central Bank Digital Currency for Trusted Mobile Devices**
  2022-10-22 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1443)
  Bo Yang, Yanchao Zhang, Dong Tong

  <details><summary>摘要 / Abstract</summary>

  In recent years, many major economies have paid close attention to central bank digital currency (CBDC). As an optional attribute of CBDC, dual offline transaction is considered to have great practical value under the circumstances for payment without network connection. However, there is no public report or paper on how to securely design or implement the dual offline transaction function specifically for CBDC. In this paper, we propose DOT-M, a practical dual offline transaction scheme designed for the mobile device user as either a payer or a payee. Precisely, adopting secure element (SE) and trusted execution environment (TEE), the architecture of trusted mobile device is constructed to protect security-sensitive keys and execution of the transaction protocol. According to the trusted architecture, the data structure for offline transaction is designed as well. On this basis, we describe the core procedures of DOT-M in detail, including registration, account synchronization, dual offline transaction, and online data updating. We also enumerate the exceptional situations that may occur during the dual offline transaction, and give specific handling methods for each situation. Moreover, six security properties of the scheme are analyzed under realistic assumptions. A prototype system is implemented and finally tested with possible parameters. The security analysis and experimental results indicate that our scheme could meet the practical requirement of CBDC offline transaction for mobile users from both aspects of security and efficiency.

  匹配依据：TEE: trusted execution environment

  </details>

- **SCL: A Secure Concurrency Layer For Paranoid Stateful Lambdas**
  2022-10-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.11703)
  Kaiyuan Chen, Alexander Thomas, Hanming Lu, William Mullen, Jeffery Ichnowski, Rahul Arya, Nivedha Krishnakumar, Ryan Teoh, Willis Wang, Anthony Joseph, John Kubiatowicz

  <details><summary>摘要 / Abstract</summary>

  We propose a federated Function-as-a-Service (FaaS) execution model that provides secure and stateful execution in both Cloud and Edge environments. The FaaS workers, called Paranoid Stateful Lambdas (PSLs), collaborate with one another to perform large parallel computations. We exploit cryptographically hardened and mobile bundles of data, called DataCapsules, to provide persistent state for our PSLs, whose execution is protected using hardware-secured TEEs. To make PSLs easy to program and performant, we build the familiar Key-Value Store interface on top of DataCapsules in a way that allows amortization of cryptographic operations. We demonstrate PSLs functioning in an edge environment running on a group of Intel NUCs with SGXv2. As described, our Secure Concurrency Layer (SCL), provides eventually-consistent semantics over written values using untrusted and unordered multicast. All SCL communication is encrypted, unforgeable, and private. For durability, updates are recorded in replicated DataCapsules, which are append-only cryptographically-hardened blockchain with confidentiality, integrity, and provenance guarantees. Values for inactive keys are stored in a log-structured merge-tree (LSM) in the same DataCapsule. SCL features a variety of communication optimizations, such as an efficient message passing framework that reduces the latency up to 44x from the Intel SGX SDK, and an actor-based cryptographic processing architecture that batches cryptographic operations and increases throughput by 81x.

  匹配依据：TEE: intel sgx

  </details>

- **Proof of Unlearning: Definitions and Instantiation**
  2022-10-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.11334)
  Jiasi Weng, Shenglong Yao, Yuefeng Du, Junjie Huang, Jian Weng, Cong Wang

  <details><summary>摘要 / Abstract</summary>

  The &quot;Right to be Forgotten&quot; rule in machine learning (ML) practice enables some individual data to be deleted from a trained model, as pursued by recently developed machine unlearning techniques. To truly comply with the rule, a natural and necessary step is to verify if the individual data are indeed deleted after unlearning. Yet, previous parameter-space verification metrics may be easily evaded by a distrustful model trainer. Thus, Thudi et al. recently present a call to action on algorithm-level verification in USENIX Security&#x27;22. We respond to the call, by reconsidering the unlearning problem in the scenario of machine learning as a service (MLaaS), and proposing a new definition framework for Proof of Unlearning (PoUL) on algorithm level. Specifically, our PoUL definitions (i) enforce correctness properties on both the pre and post phases of unlearning, so as to prevent the state-of-the-art forging attacks; (ii) highlight proper practicality requirements of both the prover and verifier sides with minimal invasiveness to the off-the-shelf service pipeline and computational workloads. Under the definition framework, we subsequently present a trusted hardware-empowered instantiation using SGX enclave, by logically incorporating an authentication layer for tracing the data lineage with a proving layer for supporting the audit of learning. We customize authenticated data structures to support large out-of-enclave storage with simple operation logic, and meanwhile, enable proving complex unlearning logic with affordable memory footprints in the enclave. We finally validate the feasibility of the proposed instantiation with a proof-of-concept implementation and multi-dimensional performance evaluation.

  匹配依据：TEE: sgx, sgx enclave

  </details>

- **Efficient Privacy-Preserving Machine Learning with Lightweight Trusted Hardware**
  2022-10-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.10133)
  Pengzhi Huang, Thang Hoang, Yueying Li, Elaine Shi, G. Edward Suh

  <details><summary>摘要 / Abstract</summary>

  In this paper, we propose a new secure machine learning inference platform assisted by a small dedicated security processor, which will be easier to protect and deploy compared to today&#x27;s TEEs integrated into high-performance processors. Our platform provides three main advantages over the state-of-the-art: (i) We achieve significant performance improvements compared to state-of-the-art distributed Privacy-Preserving Machine Learning (PPML) protocols, with only a small security processor that is comparable to a discrete security chip such as the Trusted Platform Module (TPM) or on-chip security subsystems in SoCs similar to the Apple enclave processor. In the semi-honest setting with WAN/GPU, our scheme is 4X-63X faster than Falcon (PoPETs&#x27;21) and AriaNN (PoPETs&#x27;22) and 3.8X-12X more communication efficient. We achieve even higher performance improvements in the malicious setting. (ii) Our platform guarantees security with abort against malicious adversaries under honest majority assumption. (iii) Our technique is not limited by the size of secure memory in a TEE and can support high-capacity modern neural networks like ResNet18 and Transformer. While previous work investigated the use of high-performance TEEs in PPML, this work represents the first to show that even tiny secure hardware with really limited performance can be leveraged to significantly speed-up distributed PPML protocols if the protocol can be carefully designed for lightweight trusted hardware.

  匹配依据：TEE: tees (context)

  </details>

- **CrowdGuard: Federated Backdoor Detection in Federated Learning**
  2022-10-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.07714)
  Phillip Rieger, Torsten Krauß, Markus Miettinen, Alexandra Dmitrienko, Ahmad-Reza Sadeghi

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) is a promising approach enabling multiple clients to train Deep Neural Networks (DNNs) collaboratively without sharing their local training data. However, FL is susceptible to backdoor (or targeted poisoning) attacks. These attacks are initiated by malicious clients who seek to compromise the learning process by introducing specific behaviors into the learned model that can be triggered by carefully crafted inputs. Existing FL safeguards have various limitations: They are restricted to specific data distributions or reduce the global model accuracy due to excluding benign models or adding noise, are vulnerable to adaptive defense-aware adversaries, or require the server to access local models, allowing data inference attacks. This paper presents a novel defense mechanism, CrowdGuard, that effectively mitigates backdoor attacks in FL and overcomes the deficiencies of existing techniques. It leverages clients&#x27; feedback on individual models, analyzes the behavior of neurons in hidden layers, and eliminates poisoned models through an iterative pruning scheme. CrowdGuard employs a server-located stacked clustering scheme to enhance its resilience to rogue client feedback. The evaluation results demonstrate that CrowdGuard achieves a 100% True-Positive-Rate and True-Negative-Rate across various scenarios, including IID and non-IID data distributions. Additionally, CrowdGuard withstands adaptive adversaries while preserving the original performance of protected models. To ensure confidentiality, CrowdGuard uses a secure and privacy-preserving architecture leveraging Trusted Execution Environments (TEEs) on both client and server sides.

  匹配依据：TEE: trusted execution environments

  </details>

- **SoK: How Not to Architect Your Next-Generation TEE Malware?**
  2022-10-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.06792)
  Kubilay Ahmet Küçük, Steve Moyle, Andrew Martin, Alexandru Mereacre, Nicholas Allott

  <details><summary>摘要 / Abstract</summary>

  Besides Intel&#x27;s SGX technology, there are long-running discussions on how trusted computing technologies can be used to cloak malware. Past research showed example methods of malicious activities utilising Flicker, Trusted Platform Module, and recently integrating with enclaves. We observe two ambiguous methodologies of malware development being associated with SGX, and it is crucial to systematise their details. One methodology is to use the core SGX ecosystem to cloak malware; potentially affecting a large number of systems. The second methodology is to create a custom enclave not adhering to base assumptions of SGX, creating a demonstration code of malware behaviour with these incorrect assumptions; remaining local without any impact. We examine what malware aims to do in real-world scenarios and state-of-art techniques in malware evasion. We present multiple limitations of maintaining the SGX-assisted malware and evading it from anti-malware mechanisms. The limitations make SGX enclaves a poor choice for achieving a successful malware campaign. We systematise twelve misconceptions (myths) outlining how an overfit-malware using SGX weakens malware&#x27;s existing abilities. We find the differences by comparing SGX assistance for malware with non-SGX malware (i.e., malware in the wild in our paper). We conclude that the use of hardware enclaves does not increase the preexisting attack surface, enables no new infection vector, and does not contribute any new methods to the stealthiness of malware.

  匹配依据：TEE: hardware enclaves, sgx, sgx enclaves

  </details>

- **POSE: Practical Off-chain Smart Contract Execution**
  2022-10-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.07110)
  Tommaso Frassetto, Patrick Jauernig, David Koisser, David Kretzler, Benjamin Schlosser, Sebastian Faust, Ahmad-Reza Sadeghi

  <details><summary>摘要 / Abstract</summary>

  Smart contracts enable users to execute payments depending on complex program logic. Ethereum is the most notable example of a blockchain that supports smart contracts leveraged for countless applications including games, auctions and financial products. Unfortunately, the traditional method of running contract code on-chain is very expensive, for instance, on the Ethereum platform, fees have dramatically increased, rendering the system unsuitable for complex applications. A prominent solution to address this problem is to execute code off-chain and only use the blockchain as a trust anchor. While there has been significant progress in developing off-chain systems over the last years, current off-chain solutions suffer from various drawbacks including costly blockchain interactions, lack of data privacy, huge capital costs from locked collateral, or supporting only a restricted set of applications. In this paper, we present POSE -- a practical off-chain protocol for smart contracts that addresses the aforementioned shortcomings of existing solutions. POSE leverages a pool of Trusted Execution Environments (TEEs) to execute the computation efficiently and to swiftly recover from accidental or malicious failures. We show that POSE provides strong security guarantees even if a large subset of parties is corrupted. We evaluate our proof-of-concept implementation with respect to its efficiency and effectiveness.

  匹配依据：TEE: trusted execution environments

  </details>

- **Aergia: Leveraging Heterogeneity in Federated Learning Systems**
  2022-10-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.06154)
  Bart Cox, Lydia Y. Chen, Jérémie Decouchant

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) is a popular approach for distributed deep learning that prevents the pooling of large amounts of data in a central server. FL relies on clients to update a global model using their local datasets. Classical FL algorithms use a central federator that, for each training round, waits for all clients to send their model updates before aggregating them. In practical deployments, clients might have different computing powers and network capabilities, which might lead slow clients to become performance bottlenecks. Previous works have suggested to use a deadline for each learning round so that the federator ignores the late updates of slow clients, or so that clients send partially trained models before the deadline. To speed up the training process, we instead propose Aergia, a novel approach where slow clients (i) freeze the part of their model that is the most computationally intensive to train; (ii) train the unfrozen part of their model; and (iii) offload the training of the frozen part of their model to a faster client that trains it using its own dataset. The offloading decisions are orchestrated by the federator based on the training speed that clients report and on the similarities between their datasets, which are privately evaluated thanks to a trusted execution environment. We show through extensive experiments that Aergia maintains high accuracy and significantly reduces the training time under heterogeneous settings by up to 27% and 53% compared to FedAvg and TiFL, respectively.

  匹配依据：TEE: trusted execution environment

  </details>

- **Fast Fully Oblivious Compaction and Shuffling**
  2022-10-06 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1333)
  Sajin Sasy, Aaron Johnson, Ian Goldberg

  <details><summary>摘要 / Abstract</summary>

  Several privacy-preserving analytics frameworks have been proposed that use trusted execution environments (TEEs) like Intel SGX. Such frameworks often use compaction and shuffling as core primitives. However, due to advances in TEE side-channel attacks, these primitives, and the applications that use them, should be _fully oblivious_; that is, perform instruction sequences and memory accesses that do not depend on the secret inputs. Such obliviousness would eliminate the threat of leaking private information through memory or timing side channels, but achieving it naively can result in a significant performance cost. In this work, we present fast, fully oblivious algorithms for compaction and shuffling. We implement and evaluate our designs to show that they are practical and outperform the state of the art. Our oblivious compaction algorithm, ORCompact, is always faster than the best alternative and can yield up to a 5x performance improvement. For oblivious shuffling, we provide two novel algorithms: ORShuffle and BORPStream. ORShuffle outperforms prior fully oblivious shuffles in all experiments, and it provides the largest speed increases—up to 1.8x—when shuffling a large number of small items. BORPStream outperforms all other algorithms when shuffling a large number of large items, with a speedup of up to 1.4x in such cases. It can obtain even larger performance improvements in application settings where the items to shuffle arrive incrementally over time, obtaining a speedup of as much as 4.2x. We additionally give parallel versions of all of our algorithms, prove that they have low parallel step complexity, and experimentally show a 5–6x speedup on an 8-core processor. Finally, ours is the first work with the explicit goal of ensuring full obliviousness of complex functionalities down to the implementation level. To this end, we design Fully Oblivious Assembly Verifier (FOAV), a tool that verifies the binary has no secret-dependent conditional branches.

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **Bao-Enclave: Virtualization-based Enclaves for Arm**
  2022-09-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2209.05572)
  Samuel Pereira, Joao Sousa, Sandro Pinto, José Martins, David Cerdeira

  <details><summary>摘要 / Abstract</summary>

  General-purpose operating systems (GPOS), such as Linux, encompass several million lines of code. Statistically, a larger code base inevitably leads to a higher number of potential vulnerabilities and inherently a more vulnerable system. To minimize the impact of vulnerabilities in GPOS, it has become common to implement security-sensitive programs outside the domain of the GPOS, i.e., in a Trusted Execution Environment (TEE). Arm TrustZone is the de-facto technology for implementing TEEs in Arm devices. However, over the last decade, TEEs have been successfully attacked hundreds of times. Unfortunately, these attacks have been possible due to the presence of several architectural and implementation flaws in TrustZone-based TEEs. In this paper, we propose Bao-Enclave, a virtualization-based solution that enables OEMs to remove security functionality from the TEE and move them into normal world isolated environments, protected from potentially malicious OSes, in the form of lightweight virtual machines (VMs). We evaluate Bao-Enclave on real hardware platforms and find out that Bao-Enclave may improve the performance of security-sensitive workloads by up to 4.8x, while significantly simplifying the TEE software TCB.

  匹配依据：TEE: trusted execution environment, trustzone

  </details>

- **InviCloak: An End-to-End Approach to Privacy and Performance in Web Content Distribution**
  2022-09-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2209.01541)
  Shihan Lin, Rui Xin, Aayush Goel, Xiaowei Yang

  <details><summary>摘要 / Abstract</summary>

  In today&#x27;s web ecosystem, a website that uses a Content Delivery Network (CDN) shares its Transport Layer Security (TLS) private key or session key with the CDN. In this paper, we present the design and implementation of InviCloak, a system that protects the confidentiality and integrity of a user and a website&#x27;s private communications without changing TLS or upgrading a CDN. InviCloak builds a lightweight but secure and practical key distribution mechanism using the existing DNS infrastructure to distribute a new public key associated with a website&#x27;s domain name. A web client and a website can use the new key pair to build an encryption channel inside TLS. InviCloak accommodates the current web ecosystem. A website can deploy InviCloak unilaterally without a client&#x27;s involvement to prevent a passive attacker inside a CDN from eavesdropping on their communications. If a client also installs InviCloak&#x27;s browser extension, the client and the website can achieve end-to-end confidential and untampered communications in the presence of an active attacker inside a CDN. Our evaluation shows that InviCloak increases the median page load times (PLTs) of realistic web pages from 2.0s to 2.1s, which is smaller than the median PLTs (2.8s) of a state-of-the-art TEE-based solution.

  匹配依据：TEE: tee (context)

  </details>

- **Secure and Distributed Assessment of Privacy-Preserving Releases of GWAS**
  2022-08-31 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.14947)
  Túlio Pascoal, Jérémie Decouchant, Marcus Völp

  <details><summary>摘要 / Abstract</summary>

  Genome-wide association studies (GWAS) identify correlations between the genetic variants and an observable characteristic such as a disease. Previous works presented privacy-preserving distributed algorithms for a federation of genome data holders that spans multiple institutional and legislative domains to securely compute GWAS results. However, these algorithms have limited applicability, since they still require a centralized instance to decide whether GWAS results can be safely disclosed, which is in violation to privacy regulations, such as GDPR. In this work, we introduce GenDPR, a distributed middleware that leverages Trusted Execution Environments (TEEs) to securely determine a subset of the potential GWAS statistics that can be safely released. GenDPR achieves the same accuracy as centralized solutions, but requires transferring significantly less data because TEEs only exchange intermediary results but no genomes. Additionally, GenDPR can be configured to tolerate all-but-one honest-but-curious federation members colluding with the aim to expose genomes of correct members.

  匹配依据：TEE: trusted execution environments

  </details>

- **Machine Learning with Confidential Computing: A Systematization of Knowledge**
  2022-08-22 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.10134)
  Fan Mo, Zahra Tarkhani, Hamed Haddadi

  <details><summary>摘要 / Abstract</summary>

  Privacy and security challenges in Machine Learning (ML) have become increasingly severe, along with ML&#x27;s pervasive development and the recent demonstration of large attack surfaces. As a mature system-oriented approach, Confidential Computing has been utilized in both academia and industry to mitigate privacy and security issues in various ML scenarios. In this paper, the conjunction between ML and Confidential Computing is investigated. We systematize the prior work on Confidential Computing-assisted ML techniques that provide i) confidentiality guarantees and ii) integrity assurances, and discuss their advanced features and drawbacks. Key challenges are further identified, and we provide dedicated analyses of the limitations in existing Trusted Execution Environment (TEE) systems for ML use cases. Finally, prospective works are discussed, including grounded privacy definitions for closed-loop protection, partitioned executions of efficient ML, dedicated TEE-assisted designs for ML, TEE-aware ML, and ML full pipeline guarantees. By providing these potential solutions in our systematization of knowledge, we aim to build the bridge to help achieve a much stronger TEE-enabled ML for privacy guarantees without introducing computation and system costs.

  匹配依据：TEE: confidential computing, trusted execution environment

  </details>

- **Shielding Federated Learning Systems against Inference Attacks with ARM TrustZone**
  2022-08-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.05895)
  Aghiles Ait Messaoud, Sonia Ben Mokhtar, Vlad Nitu, Valerio Schiavoni

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) opens new perspectives for training machine learning models while keeping personal data on the users premises. Specifically, in FL, models are trained on the users devices and only model updates (i.e., gradients) are sent to a central server for aggregation purposes. However, the long list of inference attacks that leak private data from gradients, published in the recent years, have emphasized the need of devising effective protection mechanisms to incentivize the adoption of FL at scale. While there exist solutions to mitigate these attacks on the server side, little has been done to protect users from attacks performed on the client side. In this context, the use of Trusted Execution Environments (TEEs) on the client side are among the most proposing solutions. However, existing frameworks (e.g., DarkneTZ) require statically putting a large portion of the machine learning model into the TEE to effectively protect against complex attacks or a combination of attacks. We present GradSec, a solution that allows protecting in a TEE only sensitive layers of a machine learning model, either statically or dynamically, hence reducing both the TCB size and the overall training time by up to 30% and 56%, respectively compared to state-of-the-art competitors.

  匹配依据：TEE: trusted execution environments, trustzone

  </details>

- **STELLA: Sparse Taint Analysis for Enclave Leakage Detection**
  2022-08-09 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.04719)
  Yang Chen, Jianfeng Jiang, Shoumeng Yan, Hui Xu

  <details><summary>摘要 / Abstract</summary>

  Intel SGX (Software Guard Extension) is a promising TEE (trusted execution environment) technique that can protect programs running in user space from being maliciously accessed by the host operating system. Although it provides hardware access control and memory encryption, the actual effectiveness also depends on the quality of the software. In particular, improper implementation of a code snippet running inside the enclave may still leak private data due to the invalid use of pointers. This paper serves as a first attempt to study the privacy leakage issues of enclave code and proposes a novel static sparse taint analysis approach to detect them. We first summarize five common patterns of leakage code. Based on these patterns, our approach performs forward analysis to recognize all taint sinks and then employs a backward approach to detect leakages. Finally, we have conducted experiments with several open-source enclave programs and found 78 vulnerabilities previously unknown in 13 projects.

  匹配依据：TEE: intel sgx, trusted execution environment

  </details>

- **An Enclave-based TEE for SE-in-SoC in RISC-V Industry**
  2022-08-07 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.03631)
  Xuanle Ren, Xiaoxia Cui

  <details><summary>摘要 / Abstract</summary>

  Secure Element (SE) in SoC sees an increasing adoption in industry. Many applications in IoT devices are bound to the SE because it provides strong cryptographic functions and physical protection. Though SE-in-SoC provides strong proven isolation for software programs, it also brings more design complexity and higher cost to PCB board building. More, SE-in-SoC may still have security concerns, such as malware installation and user impersonation. In this work, we employ TEE, a hardware-backed security technique, for protecting SE-in-SoC and RISCV. In particular, we construct various enclaves for isolating applications and manipulating the SE, with the inherently-secure primitives provided by RISC-V. Using hardware and software co-design, the solution ensures trusted execution and secure communication among applications. The security of SE is further protected by enforcing the SE to be controlled by a trusted enclave and making the RISC-V core resilient to side-channel attacks.

  匹配依据：TEE: trusted enclave

  </details>

- **Mixed Fault Tolerance Protocols with Trusted Execution Environment**
  2022-08-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.01946)
  Mingyuan Gao, Hung Dang, Ee-Chien Chang, Jialin Li

  <details><summary>摘要 / Abstract</summary>

  Blockchain systems are designed, built and operated in the presence of failures. There are two dominant failure models, namely crash fault and Byzantine fault. Byzantine fault tolerance (BFT) protocols offer stronger security guarantees, and thus are widely used in blockchain systems. However, their security guarantees come at a dear cost to their performance and scalability. Several works have improved BFT protocols, and Trusted Execution Environment (TEE) has been shown to be an effective solution. However, existing such works typically assume that each participating node is equipped with TEE. For blockchain systems wherein participants typically have different hardware configurations, i.e., some nodes feature TEE while others do not, existing TEE-based BFT protocols are not applicable. This work studies the setting wherein not all participating nodes feature TEE, under which we propose a new fault model called mixed fault. We explore a new approach to designing efficient distributed fault-tolerant protocols under the mixed fault model. In general, mixed fault tolerance (MFT) protocols assume a network of $n$ nodes, among which up to $f = \frac{n-2}{3}$ can be subject to mixed faults. We identify two key principles for designing efficient MFT protocols, namely, (i) prioritizing non-equivocating nodes in leading the protocol, and (ii) advocating the use of public-key cryptographic primitives that allow authenticated messages to be aggregated. We showcase these design principles by prescribing an MFT protocol, namely MRaft. We implemented a prototype of MRaft using Intel SGX, integrated it into the CCF blockchain framework, conducted experiments, and showed that MFT protocols can obtain the same security guarantees as their BFT counterparts while still providing better performance (both transaction throughput and latency) and scalability.

  匹配依据：TEE: intel sgx, trusted execution environment

  </details>

- **Entanglement Universality of TGX States in Qubit-Qutrit Systems**
  2022-08-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.04745)
  Samuel R. Hedemann

  <details><summary>摘要 / Abstract</summary>

  We prove that all states (mixed or pure) of qubit-qutrit ($2\times 3$) systems have entanglement-preserving unitary (EPU) equivalence to a compact subset of true-generalized X (TGX) states called EPU-minimal TGX states which we give explicitly. Thus, for any spectrum-entanglement combination achievable by general states, there exists an EPU-minimal TGX state of the same spectrum and entanglement. We use I-concurrence to measure entanglement and give an explicit formula for it for all $2\times 3$ minimal TGX states (a more general set than EPU-minimal TGX states) whether mixed or pure, yielding its minimum average value over all decompositions. We also give a computable I-concurrence formula for a more general family called minimal super-generalized X (SGX) states, and give optimal decompositions for minimal SGX states and all of their subsets.

  匹配依据：TEE: sgx

  </details>

- **AGAPECert: An Auditable, Generalized, Automated, Privacy-Enabling Certification Framework with Oblivious Smart Contracts**
  2022-07-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.12482)
  Servio Palacios, Aaron Ault, James V. Krogmeier, Bharat Bhargava, Christopher G. Brinton

  <details><summary>摘要 / Abstract</summary>

  This paper introduces AGAPECert, an Auditable, Generalized, Automated, Privacy-Enabling, Certification framework capable of performing auditable computation on private data and reporting real-time aggregate certification status without disclosing underlying private data. AGAPECert utilizes a novel mix of trusted execution environments, blockchain technologies, and a real-time graph-based API standard to provide automated, oblivious, and auditable certification. Our technique allows a privacy-conscious data owner to run pre-approved Oblivious Smart Contract code in their own environment on their own private data to produce Private Automated Certifications. These certifications are verifiable, purely functional transformations of the available data, enabling a third party to trust that the private data must have the necessary properties to produce the resulting certification. Recently, a multitude of solutions for certification and traceability in supply chains have been proposed. These often suffer from significant privacy issues because they tend to take a&quot; shared, replicated database&quot; approach: every node in the network has access to a copy of all relevant data and contract code to guarantee the integrity and reach consensus, even in the presence of malicious nodes. In these contexts of certifications that require global coordination, AGAPECert can include a blockchain to guarantee ordering of events, while keeping a core privacy model where private data is not shared outside of the data owner&#x27;s own platform. AGAPECert contributes an open-source certification framework that can be adopted in any regulated environment to keep sensitive data private while enabling a trusted automated workflow.

  匹配依据：TEE: trusted execution environments

  </details>

- **PMUSpill: The Counters in Performance Monitor Unit that Leak SGX-Protected Secrets**
  2022-07-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.11689)
  Pengfei Qiu, Yongqiang Lyu, Haixia Wang, Dongsheng Wang, Chang Liu, Qiang Gao, Chunlu Wang, Rihui Sun, Gang Qu

  <details><summary>摘要 / Abstract</summary>

  Performance Monitor Unit (PMU) is a significant hardware module on the current processors, which counts the events launched by processor into a set of PMU counters. Ideally, the events triggered by instructions that are executed but the results are not successfully committed (transient execution) should not be recorded. However, in this study, we discover that some PMU events triggered by the transient execution instructions will actually be recorded by PMU. Based on this, we propose the PMUSpill attack, which enables attackers to maliciously leak the secret data that are loaded during transient executions. The biggest challenge is how to encode the secret data into PMU events. We construct an instruction gadget to solve this challenge, whose execution path that can be identified by PMU counters represents what values the secret data are. We successfully implement the PMUSpill attack to leak the secret data stored in Intel Software Guard Extensions (SGX) (a Trusted Execution Environment (TEE) in the Intel&#x27;s processors) through real experiments. Besides, we locate the vulnerable PMU counters and their trigger instructions by iterating all the valid PMU counters and instructions. The experiment results demonstrate that there are up to 20 PMU counters available to implement the PMUSpill attack. We also provide some possible hardware and software-based countermeasures for addressing the PMUSpill attack, which can be utilized to enhance the security of processors in future.

  匹配依据：TEE: sgx, trusted execution environment

  </details>

- **Blindfold: Keeping Private Keys in PKIs and CDNs out of Sight**
  2022-07-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.09335)
  Hisham Galal, Mohammad Mannan, Amr Youssef

  <details><summary>摘要 / Abstract</summary>

  Public key infrastructure (PKI) is a certificate-based technology that helps in authenticating systems identities. HTTPS/TLS relies mainly on PKI to minimize fraud over the Internet. Nowadays, websites utilize CDNs to improve user experience, performance, and resilience against cyber attacks. However, combining HTTPS/TLS with CDNs has raised new security challenges. In any PKI system, keeping private keys private is of utmost importance. However, it has become the norm for CDN-powered websites to violate that fundamental assumption. Several solutions have been proposed to make HTTPS CDN-friendly. However, protection of private keys from the very instance of generation; and how they can be made secure against exposure by malicious (CDN) administrators and malware remain unexplored. We utilize trusted execution environments to protect private keys by never exposing them to human operators or untrusted software. We design Blindfold to protect private keys in HTTPS/TLS infrastructures, including CAs, website on-premise servers, and CDNs. We implemented a prototype to assess Blindfold&#x27;s performance and performed several experiments on both the micro and macro levels. We found that Blindfold slightly outperforms SoftHSM in key generation by 1% while lagging by 0.01% for certificate issuance operations.

  匹配依据：TEE: trusted execution environments

  </details>

- **Wink: Deniable Secure Messaging**
  2022-07-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.08891)
  Anrin Chakraborti, Darius Suciu, Radu Sion

  <details><summary>摘要 / Abstract</summary>

  End-to-end encrypted (E2EE) messaging is an essential first step in providing message confidentiality. Unfortunately, all security guarantees of end-to-end encryption are lost when keys or plaintext are disclosed, either due to device compromise or (sometimes lawful) coercion by powerful adversaries. This work introduces Wink, the first plausibly-deniable messaging system protecting message confidentiality from partial device compromise and compelled key disclosure. Wink can surreptitiously inject hidden messages in standard random coins (e.g., salts, IVs) used by existing E2EE protocols. It does so as part of legitimate secure cryptographic functionality deployed inside the widely-available trusted execution environment (TEE) TrustZone. This results in hidden communication using virtually unchanged existing E2EE messaging apps, as well as strong plausible deniability. Wink has been demonstrated with multiple existing E2EE applications (including Telegram and Signal) with minimal (external) instrumentation, negligible overheads, and crucially, without changing on-wire message formats.

  匹配依据：TEE: trusted execution environment, trustzone

  </details>

- **Horizontal Federated Learning and Secure Distributed Training for Recommendation System with Intel SGX**
  2022-07-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.05079)
  Siyuan Hui, Yuqiu Zhang, Albert Hu, Edmund Song

  <details><summary>摘要 / Abstract</summary>

  With the advent of big data era and the development of artificial intelligence and other technologies, data security and privacy protection have become more important. Recommendation systems have many applications in our society, but the model construction of recommendation systems is often inseparable from users&#x27; data. Especially for deep learning-based recommendation systems, due to the complexity of the model and the characteristics of deep learning itself, its training process not only requires long training time and abundant computational resources but also needs to use a large amount of user data, which poses a considerable challenge in terms of data security and privacy protection. How to train a distributed recommendation system while ensuring data security has become an urgent problem to be solved. In this paper, we implement two schemes, Horizontal Federated Learning and Secure Distributed Training, based on Intel SGX(Software Guard Extensions), an implementation of a trusted execution environment, and TensorFlow framework, to achieve secure, distributed recommendation system-based learning schemes in different scenarios. We experiment on the classical Deep Learning Recommendation Model (DLRM), which is a neural network-based machine learning model designed for personalization and recommendation, and the results show that our implementation introduces approximately no loss in model performance. The training speed is within acceptable limits.

  匹配依据：TEE: intel sgx, trusted execution environment

  </details>

- **DarKnight: An Accelerated Framework for Privacy and Integrity Preserving Deep Learning Using Trusted Hardware**
  2022-06-30 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.00083)
  Hanieh Hashemi, Yongqin Wang, Murali Annavaram

  <details><summary>摘要 / Abstract</summary>

  Privacy and security-related concerns are growing as machine learning reaches diverse application domains. The data holders want to train or infer with private data while exploiting accelerators, such as GPUs, that are hosted in the cloud. Cloud systems are vulnerable to attackers that compromise the privacy of data and integrity of computations. Tackling such a challenge requires unifying theoretical privacy algorithms with hardware security capabilities. This paper presents DarKnight, a framework for large DNN training while protecting input privacy and computation integrity. DarKnight relies on cooperative execution between trusted execution environments (TEE) and accelerators, where the TEE provides privacy and integrity verification, while accelerators perform the bulk of the linear algebraic computation to optimize the performance. In particular, DarKnight uses a customized data encoding strategy based on matrix masking to create input obfuscation within a TEE. The obfuscated data is then offloaded to GPUs for fast linear algebraic computation. DarKnight&#x27;s data obfuscation strategy provides provable data privacy and computation integrity in the cloud servers. While prior works tackle inference privacy and cannot be utilized for training, DarKnight&#x27;s encoding scheme is designed to support both training and inference.

  匹配依据：TEE: trusted execution environments

  </details>

- **WebAssembly as a Common Layer for the Cloud-edge Continuum**
  2022-06-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.12888)
  Jämes Ménétrey, Marcelo Pasin, Pascal Felber, Valerio Schiavoni

  <details><summary>摘要 / Abstract</summary>

  Over the last decade, the cloud computing landscape has transformed from a centralised architecture made of large data centres to a distributed and heterogeneous architecture embracing edge and IoT units. This shift has created the so-called cloud-edge continuum, which closes the gap between large data centres and end-user devices. Existing solutions for programming the continuum are, however, dominated by proprietary silos and incompatible technologies, built around dedicated devices and run-time stacks. In this position paper, we motivate the need for an interoperable environment that would run seamlessly across hardware devices and software stacks, while achieving good performance and a high level of security -- a critical requirement when processing data off-premises. We argue that the technology provided by WebAssembly running on modern virtual machines and shielded within trusted execution environments, combined with a core set of services and support libraries, allows us to meet both goals. We also present preliminary results from a prototype deployed on the cloud-edge continuum.

  匹配依据：TEE: trusted execution environments

  </details>

- **WaTZ: A Trusted WebAssembly Runtime Environment with Remote Attestation for TrustZone**
  2022-06-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.08722)
  Jämes Ménétrey, Marcelo Pasin, Pascal Felber, Valerio Schiavoni

  <details><summary>摘要 / Abstract</summary>

  WebAssembly (Wasm) is a novel low-level bytecode format that swiftly gained popularity for its efficiency, versatility and security, with near-native performance. Besides, trusted execution environments (TEEs) shield critical software assets against compromised infrastructures. However, TEEs do not guarantee the code to be trustworthy or that it was not tampered with. Instead, one relies on remote attestation to assess the code before execution. This paper describes WaTZ, which is (i) an efficient and secure runtime for trusted execution of Wasm code for Arm&#x27;s TrustZone TEE, and (ii) a lightweight remote attestation system optimised for Wasm applications running in TrustZone, as it lacks built-in mechanisms for attestation. The remote attestation protocol is formally verified using a state-of-the-art analyser and model checker. Our extensive evaluation of Arm-based hardware uses synthetic and real-world benchmarks, illustrating typical tasks IoT devices achieve. WaTZ&#x27;s execution speed is on par with Wasm runtimes in the normal world and reaches roughly half the speed of native execution, which is compensated by the additional security guarantees and the interoperability offered by Wasm. WaTZ is open-source and available on GitHub along with instructions to reproduce our experiments.

  匹配依据：TEE: trusted execution environments, trustzone

  </details>

- **Designing a Provenance Analysis for SGX Enclaves**
  2022-06-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.07418)
  Flavio Toffalini, Mathias Payer, Jianying Zhou, Lorenzo Cavallaro

  <details><summary>摘要 / Abstract</summary>

  Intel SGX enables memory isolation and static integrity verification of code and data stored in user-space memory regions called enclaves. SGX effectively shields the execution of enclaves from the underlying untrusted OS. Attackers cannot tamper nor examine enclaves&#x27; content. However, these properties equally challenge defenders as they are precluded from any provenance analysis to infer intrusions inside SGX enclaves. In this work, we propose SgxMonitor, a novel provenance analysis to monitor and identify anomalous executions of enclave code. To this end, we design a technique to extract contextual runtime information from an enclave and propose a novel model to represent enclaves&#x27; intrusions. Our experiments show that not only SgxMonitor incurs an overhead comparable to traditional provenance tools, but it also exhibits macro-benchmarks&#x27; overheads and slowdowns that marginally affect real use cases deployment. Our evaluation shows SgxMonitor successfully identifies enclave intrusions carried out by the state of the art attacks while reporting no false positives and negatives during normal enclaves executions, thus supporting the use of SgxMonitor in realistic scenarios.

  匹配依据：TEE: intel sgx, sgx, sgx enclaves

  </details>

- **Nitriding: A tool kit for building scalable, networked, secure enclaves**
  2022-06-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.04123)
  Philipp Winter, Ralph Giles, Moritz Schafhuber, Hamed Haddadi

  <details><summary>摘要 / Abstract</summary>

  Enclave deployments often fail to simultaneously be secure (e.g., resistant to side channel attacks), powerful (i.e., as fast as an off-the-shelf server), and flexible (i.e., unconstrained by development hurdles). In this paper, we present nitriding, an open tool kit that enables the development of enclave applications that satisfy all three properties. We build nitriding on top of the recently-proposed AWS Nitro Enclaves whose architecture prevents side channel attacks by design, making nitriding more secure than comparable frameworks. We abstract away the constrained development model of Nitro Enclaves, making it possible to run unmodified applications inside an enclave that have seamless and secure Internet connectivity, all while making our code user-verifiable. To demonstrate nitriding&#x27;s flexibility, we design three enclave applications, each a research contribution in its own right: (i) we run a Tor bridge inside an enclave, making it resistant to protocol-level deanonymization attacks; (ii) we built a service for securely revealing infrastructure configuration, empowering users to verify privacy promises like the discarding of IP addresses at the edge; (iii) and we move a Chromium browser into an enclave, thereby isolating its attack surface from the user&#x27;s system. We find that nitriding enables rapid prototyping and alleviates the deployment of production-quality systems, paving the way toward usable and secure enclaves.

  匹配依据：TEE: secure enclaves

  </details>

- **Attestation Mechanisms for Trusted Execution Environments Demystified**
  2022-06-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.03780)
  Jämes Ménétrey, Christian Göttel, Anum Khurshid, Marcelo Pasin, Pascal Felber, Valerio Schiavoni, Shahid Raza

  <details><summary>摘要 / Abstract</summary>

  Attestation is a fundamental building block to establish trust over software systems. When used in conjunction with trusted execution environments, it guarantees the genuineness of the code executed against powerful attackers and threats, paving the way for adoption in several sensitive application domains. This paper reviews remote attestation principles and explains how the modern and industrially well-established trusted execution environments Intel SGX, Arm TrustZone and AMD SEV, as well as emerging RISC-V solutions, leverage these mechanisms.

  匹配依据：TEE: amd sev, intel sgx, trusted execution environments, trustzone

  </details>

- **End-to-End Security for Distributed Event-Driven Enclave Applications on Heterogeneous TEEs**
  2022-06-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.01041)
  Gianluca Scopelliti, Sepideh Pouyanrad, Job Noorman, Fritz Alder, Christoph Baumann, Frank Piessens, Jan Tobias Mühlberg

  <details><summary>摘要 / Abstract</summary>

  This paper presents an approach to provide strong assurance of the secure execution of distributed event-driven applications on shared infrastructures, while relying on a small Trusted Computing Base. We build upon and extend security primitives provided by Trusted Execution Environments (TEEs) to guarantee authenticity and integrity properties of applications, and to secure control of input and output devices. More specifically, we guarantee that if an output is produced by the application, it was allowed to be produced by the application&#x27;s source code based on an authentic trace of inputs. We present an integrated open-source framework to develop, deploy, and use such applications across heterogeneous TEEs. Beyond authenticity and integrity, our framework optionally provides confidentiality and a notion of availability, and facilitates software development at a high level of abstraction over the platform-specific TEE layer. We support event-driven programming to develop distributed enclave applications in Rust and C for heterogeneous TEE, including Intel SGX, ARM TrustZone and Sancus. In this article we discuss the workings of our approach, the extensions we made to the Sancus processor, and the integration of our development model with commercial TEEs. Our evaluation of security and performance aspects show that TEEs, together with our programming model, form a basis for powerful security architectures for dependable systems in domains such as Industrial Control Systems and the Internet of Things, illustrating our framework&#x27;s unique suitability for a broad range of use cases which combine cloud processing, mobile and edge devices, and lightweight sensing and actuation.

  匹配依据：TEE: intel sgx, trusted execution environments, trustzone

  </details>

- **CTR: Checkpoint, Transfer, and Restore for Secure Enclaves**
  2022-05-30 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.15359)
  Yoshimichi Nakatsuka, Ercan Ozturk, Alex Shamis, Andrew Paverd, Peter Pietzuch

  <details><summary>摘要 / Abstract</summary>

  Hardware-based Trusted Execution Environments (TEEs) are becoming increasingly prevalent in cloud computing, forming the basis for confidential computing. However, the security goals of TEEs sometimes conflict with existing cloud functionality, such as VM or process migration, because TEE memory cannot be read by the hypervisor, OS, or other software on the platform. Whilst some newer TEE architectures support migration of entire protected VMs, there is currently no practical solution for migrating individual processes containing in-process TEEs. The inability to migrate such processes leads to operational inefficiencies or even data loss if the host platform must be urgently restarted. We present CTR, a software-only design to retrofit migration functionality into existing TEE architectures, whilst maintaining their expected security guarantees. Our design allows TEEs to be interrupted and migrated at arbitrary points in their execution, thus maintaining compatibility with existing VM and process migration techniques. By cooperatively involving the TEE in the migration process, our design also allows application developers to specify stateful migration-related policies, such as limiting the number of times a particular TEE may be migrated. Our prototype implementation for Intel SGX demonstrates that migration latency increases linearly with the size of the TEE memory and is dominated by TEE system operations.

  匹配依据：TEE: confidential computing, intel sgx, secure enclaves, trusted execution environments

  </details>

- **SoK: Hardware-supported Trusted Execution Environments**
  2022-05-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.12742)
  Moritz Schneider, Ramya Jayaram Masti, Shweta Shinde, Srdjan Capkun, Ronald Perez

  <details><summary>摘要 / Abstract</summary>

  The growing complexity of modern computing platforms and the need for strong isolation protections among their software components has led to the increased adoption of Trusted Execution Environments (TEEs). While several commercial and academic TEE architectures have emerged in recent times, they remain hard to compare and contrast. More generally, existing TEEs have not been subject to a holistic systematization to understand the available design alternatives for various aspects of TEE design and their corresponding pros-and-cons. Therefore, in this work, we analyze the design of existing TEEs and systematize the mechanisms that TEEs implement to achieve their security goals, namely, verifiable launch, run-time isolation, trusted IO, and secure storage. More specifically, we analyze the typical architectural building blocks underlying TEE solutions, design alternatives for each of these components and the trade-offs that they entail. We focus on hardware-assisted TEEs and cover a wide range of TEE proposals from academia and the industry. Our analysis shows that although TEEs are diverse in terms of their goals, usage models, and instruction set architectures, they all share many common building blocks in terms of their design.

  匹配依据：TEE: trusted execution environments

  </details>

- **Dialektos: Privacy-preserving Smart Contracts**
  2022-05-24 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/640)
  Tadas Vaitiekūnas

  <details><summary>摘要 / Abstract</summary>

  Digital ledger technologies supporting smart contracts usually does not ensure any privacy for user transactions or state. Most solutions to this problem either use private network setups, centralized parties, hardware enclaves, or cryptographic primitives, which are novel, complex, and computationally expensive. This paper looks into an alternative way of implementing smart contracts. Our construction of a protocol for smart contracts employs an overlay protocol design pattern for decentralized applications, which separates transaction ordering from transaction validation. This enables consensus on application state while revealing only encrypted versions of transactions to public consensus protocol network. UTXO-based smart contract model allows partitioning state of distributed ledger in a way that participants would need to decrypt and reach consensus only on those transactions, which are relevant to them. We present security analysis, which shows that, assuming presence of a secure consensus protocol, our construction achieves consensus on UTXO-based transactions, while hiding most of transaction details from all protocol parties, except a limited subset of parties, which need particular transactions for construction of their state.

  匹配依据：TEE: hardware enclaves

  </details>

- **Protecting File Activities via Deception for ARM TrustZone**
  2022-05-22 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.10963)
  Liwei Guo, Kaiyang Zhao, Yiying Zhang, Felix Xiaozhu Lin

  <details><summary>摘要 / Abstract</summary>

  A TrustZone TEE often invokes an external filesystem. While filedata can be encrypted, the revealed file activities can leak secrets. To hide the file activities from the filesystem and its OS, we propose Enigma, a deception-based defense injecting sybil file activities as the cover of the actual file activities. Enigma contributes three new designs. (1) To make the deception credible, the TEE generates sybil calls by replaying file calls from the TEE code under protection. (2) To make sybil activities cheap, the TEE requests the OS to run K filesystem images simultaneously. Concealing the disk, the TEE backs only one image with the actual disk while backing other images by only storing their metadata. (3) To protect filesystem image identities, the TEE shuffles the images frequently, preventing the OS from observing any image for long. Enigma works with unmodified filesystems shipped withLinux. On a low-cost Arm SoC with EXT4 and F2FS, our system can concurrently run as many as 50 filesystem images with 1% of disk overhead per additional image. Compared to common obfuscation for hiding addresses in a flat space, Enigma hides file activities with richer semantics. Its cost is lower by one order of magnitude while achieving the same level of probabilistic security guarantees.

  匹配依据：TEE: trustzone

  </details>

- **SplitBFT: Improving Byzantine Fault Tolerance Safety Using Trusted Compartments**
  2022-05-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.08938)
  Ines Messadi, Markus Horst Becker, Kai Bleeke, Leander Jehl, Sonia Ben Mokhtar, Rüdiger Kapitza

  <details><summary>摘要 / Abstract</summary>

  Byzantine fault-tolerant agreement (BFT) in a partially synchronous system usually requires 3f + 1 nodes to tolerate f faulty replicas. Due to their high throughput and finality property BFT algorithms build the core of recent permissioned blockchains. As a complex and resource-demanding infrastructure, multiple cloud providers have started offering Blockchain-as-a-Service. This eases the deployment of permissioned blockchains but places the cloud provider in a central controlling position, thereby questioning blockchains&#x27; fault tolerance and decentralization properties and their underlying BFT algorithm. This paper presents SplitBFT, a new way to utilize trusted execution technology (TEEs), such as Intel SGX, to harden the safety and confidentiality guarantees of BFT systems thereby strengthening the trust in could-based deployments of permissioned blockchains. Deviating from standard assumptions, SplitBFT acknowledges that code protected by trusted execution may fail. We address this by splitting and isolating the core logic of BFT protocols into multiple compartments resulting in a more resilient architecture. We apply SplitBFT to the traditional practical byzantine fault tolerance algorithm (PBFT) and evaluate it using SGX. Our results show that SplitBFT adds only a reasonable overhead compared to the non-compartmentalized variant.

  匹配依据：TEE: intel sgx, sgx

  </details>

- **Confidential Machine Learning within Graphcore IPUs**
  2022-05-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.09005)
  Kapil Vaswani, Stavros Volos, Cédric Fournet, Antonio Nino Diaz, Ken Gordon, Balaji Vembu, Sam Webster, David Chisnall, Saurabh Kulkarni, Graham Cunningham, Richard Osborne, Dan Wilkinson

  <details><summary>摘要 / Abstract</summary>

  We present IPU Trusted Extensions (ITX), a set of experimental hardware extensions that enable trusted execution environments in Graphcore&#x27;s AI accelerators. ITX enables the execution of AI workloads with strong confidentiality and integrity guarantees at low performance overheads. ITX isolates workloads from untrusted hosts, and ensures their data and models remain encrypted at all times except within the IPU. ITX includes a hardware root-of-trust that provides attestation capabilities and orchestrates trusted execution, and on-chip programmable cryptographic engines for authenticated encryption of code and data at PCIe bandwidth. We also present software for ITX in the form of compiler and runtime extensions that support multi-party training without requiring a CPU-based TEE. Experimental support for ITX is included in Graphcore&#x27;s GC200 IPU taped out at TSMC&#x27;s 7nm technology node. Its evaluation on a development board using standard DNN training workloads suggests that ITX adds less than 5% performance overhead, and delivers up to 17x better performance compared to CPU-based confidential computing systems relying on AMD SEV-SNP.

  匹配依据：TEE: amd sev, confidential computing, trusted execution environments

  </details>

- **A Comprehensive Benchmark Suite for Intel SGX**
  2022-05-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.06415)
  Sandeep Kumar, Abhisek Panda, Smruti R. Sarangi

  <details><summary>摘要 / Abstract</summary>

  Trusted execution environments (TEEs) such as \intelsgx facilitate the secure execution of an application on untrusted machines. Sadly, such environments suffer from serious limitations and performance overheads in terms of writing back data to the main memory, their interaction with the OS, and the ability to issue I/O instructions. There is thus a plethora of work that focuses on improving the performance of such environments -- this necessitates the need for a standard, widely accepted benchmark suite (something similar to SPEC and PARSEC). To the best of our knowledge, such a suite does not exist. Our suite, SGXGauge, contains a diverse set of workloads such as blockchain codes, secure machine learning algorithms, lightweight web servers, secure key-value stores, etc. We thoroughly characterizes the behavior of the benchmark suite on a native platform and on a platform that uses a library OS-based shimming layer (GrapheneSGX). We observe that the most important metrics of interest are performance counters related to paging, memory, and TLB accesses. There is an abrupt change in performance when the memory footprint starts to exceed the size of the EPC size in Intel SGX, and the library OS does not add a significant overhead (~ +- 10%).

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **Building A Trusted Execution Environment for In-Storage Computing**
  2022-05-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.06361)
  Yuqi Xue, Luyi Kang, Weiwei Jia, Xiaohao Wang, Jongryool Kim, Changhwan Youn, Myeong Joon Kang, Hyung Jin Lim, Bruce Jacob, Jian Huang

  <details><summary>摘要 / Abstract</summary>

  In-storage computing with modern solid-state drives (SSDs) enables developers to offload programs from the host to the SSD. It has been proven to be an effective approach to alleviating the I/O bottleneck. To facilitate in-storage computing, many frameworks have been proposed. However, few of them consider security as the priority for in-storage computing. Specifically, since modern SSD controllers do not have a trusted execution environment, an offloaded (malicious) program could steal, modify, and even destroy the data stored in the SSD. In this paper, we first investigate the attacks that could be conducted by offloaded in-storage programs. To defend against these attacks, we build IceClave, a lightweight trusted execution environment for in-storage computing. IceClave enables security isolation between in-storage programs and flash management functions. IceClave also achieves security isolation between in-storage programs and enforces memory encryption and integrity verification of in-storage DRAM with low overhead. To protect data loaded from flash chips, IceClave develops a lightweight data encryption/decryption mechanism in flash controllers. We develop IceClave with a full system simulator and evaluate IceClave with a variety of data-intensive applications. Compared to state-of-the-art in-storage computing approaches, IceClave introduces only 7.6% performance overhead, while enforcing security isolation in the SSD controller with minimal hardware cost. IceClave still keeps the performance benefit of in-storage computing by delivering up to 2.31$\times$ better performance than the conventional host-based trusted computing approach.

  匹配依据：TEE: trusted execution environment

  </details>

- **Trusted Container Extensions for Container-based Confidential Computing**
  2022-05-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.05747)
  Ferdinand Brasser, Patrick Jauernig, Frederik Pustelnik, Ahmad-Reza Sadeghi, Emmanuel Stapf

  <details><summary>摘要 / Abstract</summary>

  Cloud computing has emerged as a corner stone of today&#x27;s computing landscape. More and more customers who outsource their infrastructure benefit from the manageability, scalability and cost saving that come with cloud computing. Those benefits get amplified by the trend towards microservices. Instead of renting and maintaining full VMs, customers increasingly leverage container technologies, which come with a much more lightweight resource footprint while also removing the need to emulate complete systems and their devices. However, privacy concerns hamper many customers from moving to the cloud and leveraging its benefits. Furthermore, regulatory requirements prevent the adaption of cloud computing in many industries, such as health care or finance. Standard software isolation mechanisms have been proven to be insufficient if the host system is not fully trusted, e.g., when the cloud infrastructure gets compromised by malicious third-party actors. Consequently, confidential computing is gaining increasing relevance in the cloud computing field. We present Trusted Container Extensions (TCX), a novel container security architecture, which combines the manageability and agility of standard containers with the strong protection guarantees of hardware-enforced Trusted Execution Environments (TEEs) to enable confidential computing for container workloads. TCX provides significant performance advantages compared to existing approaches while protecting container workloads and the data processed by them. Our implementation, based on AMD Secure Encrypted Virtualization (SEV), ensures integrity and confidentiality of data and services during deployment, and allows secure interaction between protected containers as well as to external entities. Our evaluation shows that our implementation induces a low performance overhead of 5.77% on the standard SPEC2017 benchmark suite.

  匹配依据：TEE: confidential computing, secure encrypted virtualization, trusted execution environments

  </details>

- **Private delegated computations using strong isolation**
  2022-05-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.03322)
  Mathias Brossard, Guilhem Bryant, Basma El Gaabouri, Xinxin Fan, Alexandre Ferreira, Edmund Grimley-Evans, Christopher Haster, Evan Johnson, Derek Miller, Fan Mo, Dominic P. Mulligan, Nick Spinale, Eric van Hensbergen, Hugo J. M. Vincent, Shale Xiong

  <details><summary>摘要 / Abstract</summary>

  Sensitive computations are now routinely delegated to third-parties. In response, Confidential Computing technologies are being introduced to microprocessors, offering a protected processing environment, which we generically call an isolate, providing confidentiality and integrity guarantees to code and data hosted within -- even in the face of a privileged attacker. Isolates, with an attestation protocol, permit remote third-parties to establish a trusted &quot;beachhead&quot; containing known code and data on an otherwise untrusted machine. Yet, the rise of these technologies introduces many new problems, including: how to ease provisioning of computations safely into isolates; how to develop distributed systems spanning multiple classes of isolate; and what to do about the billions of &quot;legacy&quot; devices without support for Confidential Computing? Tackling the problems above, we introduce Veracruz, a framework that eases the design and implementation of complex privacy-preserving, collaborative, delegated computations among a group of mutually mistrusting principals. Veracruz supports multiple isolation technologies and provides a common programming model and attestation protocol across all of them, smoothing deployment of delegated computations over supported technologies. We demonstrate Veracruz in operation, on private in-cloud object detection on encrypted video streaming from a video camera. In addition to supporting hardware-backed isolates -- like AWS Nitro Enclaves and Arm Confidential Computing Architecture Realms -- Veracruz also provides pragmatic &quot;software isolates&quot; on Armv8-A devices without hardware Confidential Computing capability, using the high-assurance seL4 microkernel and our IceCap framework.

  匹配依据：TEE: confidential computing

  </details>

- **HTTPA/2: a Trusted End-to-End Protocol for Web Services**
  2022-05-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.01052)
  Gordon King, Hans Wang

  <details><summary>摘要 / Abstract</summary>

  With the advent of cloud computing and the Internet, the commercialized website becomes capable of providing more web services, such as software as a service (SaaS) or function as a service (FaaS), for great user experiences. Undoubtedly, web services have been thriving in popularity that will continue growing to serve modern human life. As expected, there came the ineluctable need for preserving privacy, enhancing security, and building trust. However, HTTPS alone cannot provide a remote attestation for building trust with web services, which remains lacking in trust. At the same time, cloud computing is actively adopting the use of TEEs and will demand a web-based protocol for remote attestation with ease of use. Here, we propose HTTPA/2 as an upgraded version of HTTP-Attestable (HTTPA) by augmenting existing HTTP to enable end-to-end trusted communication between endpoints at layer 7 (L7). HTTPA/2 allows for L7 message protection without relying on TLS. In practice, HTTPA/2 is designed to be compatible with the in-network processing of the modern cloud infrastructure, including L7 gateway, L7 load balancer, caching, etc. We envision that \acs{httpa}/2 will further enable trustworthy web services and trustworthy AI applications in the future, accelerating the transformation of the web-based digital world to be more trustworthy.

  匹配依据：TEE: tees (context)

  </details>

- **PRETRUST: A Framework for Fast Payments in Blockchain Systems**
  2022-04-29 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.13827)
  Huapeng Li, Baocheng Wang

  <details><summary>摘要 / Abstract</summary>

  In this study, we propose PRETRUST, a new framework to address the problem of the efficiency of payment process based on blockchain systems. PRETRUST is based on the thoughts of consortium chains, supporting fast payments. To make parties address transactions efficiently and scale out the capacity, the main strategy is based on the guarantee mechanism and shard technology with a random arrangement of transactions and consensus groups. In PRETRUST, the guarantee process replaces the verification of a transaction on-chain to realize the optimization of efficiency. And the model of a trusted execution environment is utilized in the interactions between PRETRUST and public systems. Throughout the paper, we discuss several transaction scenarios and analyze the security, which shows that PRETRUST can guarantee security.

  匹配依据：TEE: trusted execution environment

  </details>

- **Investigating Black-Box Function Recognition Using Hardware Performance Counters**
  2022-04-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.11639)
  Carlton Shepherd, Benjamin Semal, Konstantinos Markantonakis

  <details><summary>摘要 / Abstract</summary>

  This paper presents new methods and results for recognising black-box program functions using hardware performance counters (HPC), where an investigator can invoke and measure function calls. Important use cases include analysing compiled libraries, e.g. static and dynamic link libraries, and trusted execution environment (TEE) applications. We develop a generic approach to classify a comprehensive set of hardware events, e.g. branch mis-predictions and instruction retirements, to recognise standard benchmarking and cryptographic library functions. This includes various signing, verification and hash functions, and ciphers in numerous modes of operation. Three architectures are evaluated using off-the-shelf Intel/X86-64, ARM, and RISC-V CPUs. Next, we show that several known CVE-numbered OpenSSL vulnerabilities can be detected using HPC differences between patched and unpatched library versions. Further, we demonstrate that standardised cryptographic functions within ARM TrustZone TEE applications can be recognised using non-secure world HPC measurements, applying to platforms that insecurely perturb the performance monitoring unit (PMU) during TEE execution. High accuracy was achieved in all cases (86.22-99.83%) depending on the application, architectural, and compilation assumptions. Lastly, we discuss mitigations, outstanding challenges, and directions for future research.

  匹配依据：TEE: trusted execution environment, trustzone

  </details>

- **Using SGX for Meta-Transactions Support in Ethereum DApps**
  2022-04-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.09864)
  Emanuel Onica, Ciprian Amariei

  <details><summary>摘要 / Abstract</summary>

  Decentralized applications (DApps) gained traction in the context of the blockchain technology. Ethereum is currently the public blockchain that backs the largest amount of the existing DApps. Onboarding new users to Ethereum DApps is a notoriously hard issue to solve. This is mainly caused by lack of cryptocurrency ownership, needed for transaction fees. Several meta-transaction patterns emerged for decoupling users from paying these fees. However, such solutions are mostly offered via off-chain, often paid relayer services and do not fully address the security issues present in the meta-transaction path. In this paper, we introduce a new meta-transaction architecture that makes use of the Intel Software Guard Extensions (SGX). Unlike other solutions, our approach would offer the possibility to deploy a fee-free Ethereum DApp on a web server that can directly relay meta-transactions to the Ethereum network while having essential security guarantees integrated by design.

  匹配依据：TEE: sgx

  </details>

- **BliMe: Verifiably Secure Outsourced Computation with Hardware-Enforced Taint Tracking**
  2022-04-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.09649)
  Hossam ElAtali, Lachlan J. Gunn, Hans Liljestrand, N. Asokan

  <details><summary>摘要 / Abstract</summary>

  Outsourced computing is widely used today. However, current approaches for protecting client data in outsourced computing fall short: use of cryptographic techniques like fully-homomorphic encryption incurs substantial costs, whereas use of hardware-assisted trusted execution environments has been shown to be vulnerable to run-time and side-channel attacks. We present Blinded Memory (BliMe), an architecture to realize efficient and secure outsourced computation. BliMe consists of a novel and minimal set of instruction set architecture (ISA) extensions implementing a taint-tracking policy to ensure the confidentiality of client data even in the presence of server vulnerabilities. To secure outsourced computation, the BliMe extensions can be used together with an attestable, fixed-function hardware security module (HSM) and an encryption engine that provides atomic decrypt-and-taint and encrypt-and-untaint operations. Clients rely on remote attestation and key agreement with the HSM to ensure that their data can be transferred securely to and from the encryption engine and will always be protected by BliMe&#x27;s taint-tracking policy while at the server. We provide an RTL implementation BliMe-BOOM based on the BOOM RISC-V core. BliMe-BOOM requires no reduction in clock frequency relative to unmodified BOOM, and has minimal power ($&lt;\!1.5\%$) and FPGA resource ($\leq\!9.0\%$) overheads. Various implementations of BliMe incur only moderate performance overhead ($8--25\%$). We also provide a machine-checked security proof of a simplified model ISA with BliMe extensions.

  匹配依据：TEE: trusted execution environments

  </details>

- **An Exploratory Study of Attestation Mechanisms for Trusted Execution Environments**
  2022-04-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.06790)
  Jämes Ménétrey, Christian Göttel, Marcelo Pasin, Pascal Felber, Valerio Schiavoni

  <details><summary>摘要 / Abstract</summary>

  Attestation is a fundamental building block to establish trust over software systems. When used in conjunction with trusted execution environments, it guarantees that genuine code is executed even when facing strong attackers, paving the way for adoption in several sensitive application domains. This paper reviews existing remote attestation principles and compares the functionalities of current trusted execution environments as Intel SGX, Arm TrustZone and AMD SEV, as well as emerging RISC-V solutions.

  匹配依据：TEE: amd sev, intel sgx, trusted execution environments, trustzone

  </details>

- **Lessons Learned from Blockchain Applications of Trusted Execution Environments and Implications for Future Research**
  2022-03-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.12724)
  Rabimba Karanjai, Lei Xu, Lin Chen, Fengwei Zhang, Zhimin Gao, Weidong Shi

  <details><summary>摘要 / Abstract</summary>

  Modern computer systems tend to rely on large trusted computing bases (TCBs) for operations. To address the TCB bloating problem, hardware vendors have developed mechanisms to enable or facilitate the creation of a trusted execution environment (TEE) in which critical software applications can execute securely in an isolated environment. Even under the circumstance that a host OS is compromised by an adversary, key security properties such as confidentiality and integrity of the software inside the TEEs can be guaranteed. The promise of integrity and security has driven developers to adopt it for use cases involving access control, PKS, IoT among other things. Among these applications include blockchain-related use cases. The usage of the TEEs doesn&#x27;t come without its own implementation challenges and potential pitfalls. In this paper, we examine the assumptions, security models, and operational environments of the proposed TEE use cases of blockchain-based applications. The exercise and analysis help the hardware TEE research community to identify some open challenges and opportunities for research and rethink the design of hardware TEEs in general.

  匹配依据：TEE: trusted execution environment, trusted execution environments

  </details>

- **Minimizing Trust with Exclusively-Used Physically-Isolated Hardware**
  2022-03-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.08284)
  Zhihao Yao, Seyed Mohammadjavad Seyed Talebi, Mingyi Chen, Ardalan Amiri Sani, Thomas Anderson

  <details><summary>摘要 / Abstract</summary>

  Smartphone owners often need to run security-critical programs on the same device as other untrusted and potentially malicious programs. This requires users to trust hardware and system software to correctly sandbox malicious programs, trust that is often misplaced. Our goal is to minimize the number and complexity of hardware and software components that a smartphone owner needs to trust to withstand adversarial inputs. We present a multi-domain hardware design composed of statically-partitioned, physically-isolated trust domains. We introduce a few simple, formally-verified hardware components to enable a program to gain provably exclusive and simultaneous access to both computation and I/O on a temporary basis. To manage this hardware, we present OctopOS, an OS composed of mutually distrustful subsystems. We present a prototype of this machine (hardware and OS) on a CPU-FPGA board and show that it incurs a small hardware cost compared to modern SoCs. For security-critical programs, we show that this machine significantly reduces the required trust compared to mainstream TEEs while achieving decent performance. For normal programs, performance is similar to a legacy machine.

  匹配依据：TEE: tees (context)

  </details>

- **RAPTEE: Leveraging trusted execution environments for Byzantine-tolerant peer sampling services**
  2022-03-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.04258)
  Matthieu Pigaglio, Joachim Bruneau-Queyreix, David Bromberg, Davide Frey, Etienne Rivière, Laurent Réveillère

  <details><summary>摘要 / Abstract</summary>

  Peer sampling is a first-class abstraction used in distributed systems for overlay management and information dissemination. The goal of peer sampling is to continuously build and refresh a partial and local view of the full membership of a dynamic, large-scale distributed system. Malicious nodes under the control of an adversary may aim at being over-represented in the views of correct nodes, increasing their impact on the proper operation of protocols built over peer sampling. State-of-the-art Byzantine resilient peer sampling protocols reduce this bias as long as Byzantines are not overly present. This paper studies the benefits brought to the resilience of peer sampling services when considering that a small portion of trusted nodes can run code whose authenticity and integrity can be assessed within a trusted execution environment, and specifically Intel&#x27;s software guard extensions technology (SGX). We present RAPTEE, a protocol that builds and leverages trusted gossip-based communications to hamper an adversary&#x27;s ability to increase its system-wide representation in the views of all nodes. We apply RAPTEE to BRAHMS, the most resilient peer sampling protocol to date. Experiments with 10,000 nodes show that with only 1% of SGX-capable devices, RAPTEE can reduce the proportion of Byzantine IDs in the view of honest nodes by up to 17% when the system contains 10% of Byzantine nodes. In addition, the security guarantees of RAPTEE hold even in the presence of a powerful attacker attempting to identify trusted nodes and injecting view-poisoned trusted nodes.

  匹配依据：TEE: sgx, trusted execution environment, trusted execution environments

  </details>

- **Building Your Own Trusted Execution Environments Using FPGA**
  2022-03-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.04214)
  Md Armanuzzaman, Ahmad-Reza Sadeghi, Ziming Zhao

  <details><summary>摘要 / Abstract</summary>

  In recent years, we have witnessed unprecedented growth in using hardware-assisted Trusted Execution Environments (TEE) or enclaves to protect sensitive code and data on commodity devices thanks to new hardware security features, such as Intel SGX and Arm TrustZone. Even though the proprietary TEEs bring many benefits, they have been criticized for lack of transparency, vulnerabilities, and various restrictions. For example, existing TEEs only provide a static and fixed hardware Trusted Computing Base (TCB), which cannot be customized for different applications. Existing TEEs time-share a processor core with the Rich Execution Environment (REE), making execution less efficient and vulnerable to cache side-channel attacks. Moreover, TrustZone lacks hardware support for multiple TEEs, remote attestation, and memory encryption. In this paper, we present BYOTee (Build Your Own Trusted Execution Environments), which is an easy-to-use infrastructure for building multiple equally secure enclaves by utilizing commodity Field Programmable Gate Arrays (FPGA) devices. BYOTee creates enclaves with customized hardware TCBs, which include softcore CPUs, block RAMs, and peripheral connections, in FPGA on demand. Additionally, BYOTee provides mechanisms to attest the integrity of the customized enclaves&#x27; hardware and software stacks, including bitstream, firmware, and the Security-Sensitive Applications (SSA) along with their inputs and outputs to remote verifiers. We implement a BYOTee system for the Xilinx System-on-Chip (SoC) FPGA. The evaluations on the low-end Zynq-7000 system for four SSAs and 12 benchmark applications demonstrate the usage, security, effectiveness, and performance of the BYOTee framework.

  匹配依据：TEE: intel sgx, secure enclaves, trusted execution environments, trustzone

  </details>

- **EnclaveTree: Privacy-preserving Data Stream Training and Inference Using TEE**
  2022-03-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.01438)
  Qifan Wang, Shujie Cui, Lei Zhou, Ocean Wu, Yonghua Zhu, Giovanni Russello

  <details><summary>摘要 / Abstract</summary>

  The classification service over a stream of data is becoming an important offering for cloud providers, but users may encounter obstacles in providing sensitive data due to privacy concerns. While Trusted Execution Environments (TEEs) are promising solutions for protecting private data, they remain vulnerable to side-channel attacks induced by data-dependent access patterns. We propose a Privacy-preserving Data Stream Training and Inference scheme, called EnclaveTree, that provides confidentiality for user&#x27;s data and the target models against a compromised cloud service provider. We design a matrix-based training and inference procedure to train the Hoeffding Tree (HT) model and perform inference with the trained model inside the trusted area of TEEs, which provably prevent the exploitation of access-pattern-based attacks. The performance evaluation shows that EnclaveTree is practical for processing the data streams with small or medium number of features. When there are less than 63 binary features, EnclaveTree is up to ${\thicksim}10{\times}$ and ${\thicksim}9{\times}$ faster than naïve oblivious solution on training and inference, respectively.

  匹配依据：TEE: trusted execution environments

  </details>

- **Computation offloading to hardware accelerators in Intel SGX and Gramine Library OS**
  2022-03-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.01813)
  Dmitrii Kuvaiskii, Gaurav Kumar, Mona Vij

  <details><summary>摘要 / Abstract</summary>

  The Intel Software Guard Extensions (SGX) technology enables applications to run in an isolated SGX enclave environment, with elevated confidentiality and integrity guarantees. Gramine Library OS facilitates execution of existing unmodified applications in SGX enclaves, requiring only an accompanying manifest file that describes the application&#x27;s security posture and configuration. However, Intel SGX is a CPU-only technology, thus Gramine currently supports CPU-only workloads. To enable a broader class of applications that offload computations to hardware accelerators - GPU offload, NIC offload, FPGA offload, TPM communications - Gramine must be augmented with device-backed mmap support and generic ioctl support. In this paper, we describe the design and implementation of this newly added support, the corresponding changes to the manifest-file syntax and the requisite deep copy algorithm. We evaluate our implementation on Intel Media SDK workloads and discuss the encountered caveats and limitations. Finally, we outline a use case for the presented mmap/ioctl support beyond mere device communication, namely the mechanism to slice the application into the trusted enclave part (where the core application executes) and the untrusted shared-memory part (where insecure shared libraries execute).

  匹配依据：TEE: intel sgx, sgx, sgx enclave, sgx enclaves, trusted enclave

  </details>

- **TEE-based decentralized recommender systems: The raw data sharing redemption**
  2022-02-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.11655)
  Akash Dhasade, Nevena Dresevic, Anne-Marie Kermarrec, Rafael Pires

  <details><summary>摘要 / Abstract</summary>

  Recommenders are central in many applications today. The most effective recommendation schemes, such as those based on collaborative filtering (CF), exploit similarities between user profiles to make recommendations, but potentially expose private data. Federated learning and decentralized learning systems address this by letting the data stay on user&#x27;s machines to preserve privacy: each user performs the training on local data and only the model parameters are shared. However, sharing the model parameters across the network may still yield privacy breaches. In this paper, we present REX, the first enclave-based decentralized CF recommender. REX exploits Trusted execution environments (TEE), such as Intel software guard extensions (SGX), that provide shielded environments within the processor to improve convergence while preserving privacy. Firstly, REX enables raw data sharing, which ultimately speeds up convergence and reduces the network load. Secondly, REX fully preserves privacy. We analyze the impact of raw data sharing in both deep neural network (DNN) and matrix factorization (MF) recommenders and showcase the benefits of trusted environments in a full-fledged implementation of REX. Our experimental results demonstrate that through raw data sharing, REX significantly decreases the training time by 18.3x and the network load by 2 orders of magnitude over standard decentralized approaches that share only parameters, while fully protecting privacy by leveraging trustworthy hardware enclaves with very little overhead.

  匹配依据：TEE: hardware enclaves, sgx, trusted execution environments

  </details>

- **GuaranTEE: Introducing Control-Flow Attestation for Trusted Execution Environments**
  2022-02-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.07380)
  Mathias Morbitzer, Benedikt Kopf, Philipp Zieris

  <details><summary>摘要 / Abstract</summary>

  The majority of cloud providers offers users the possibility to deploy Trusted Execution Environments (TEEs) to protect their data and processes from high privileged adversaries. This offer is intended to address concerns of users when moving critical tasks into the cloud. However, TEEs only allow to attest the integrity of the environment at launch-time. To also enable the attestation of a TEE&#x27;s integrity at run-time, we present GuaranTEE. GuaranTEE uses control-flow attestation to ensure the integrity of a service running within a TEE. By additionally placing all components of GuaranTEE in TEEs, we are able to not only detect a compromised target, but are also able to protect ourselves from malicious administrators. We show the practicability of GuaranTEE by providing a detailed performance and security evaluation of our prototype based on Intel SGX in Microsoft Azure. Our evaluation shows that the need to transfer information between TEEs and the additional verification process add considerable overhead under high CPU load. Yet, we are able to reduce this overhead by securely caching collected information and by performing the analysis in parallel to executing the application. In summary, our results show that GuaranTEE provides a practical solution for cloud users focused on protecting the integrity of their data and processes at run-time.

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **Twilight: A Differentially Private Payment Channel Network**
  2022-02-09 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/136)
  Maya Dotan, Saar Tochner, Aviv Zohar, Yossi Gilad

  <details><summary>摘要 / Abstract</summary>

  Payment channel networks (PCNs) provide a faster and cheaper alternative to transactions recorded on the blockchain. Clients can trustlessly establish payment channels with relays by locking coins and then send signed payments that shift coin balances over the network&#x27;s channels. Although payments are never published, anyone can track a client&#x27;s payment by monitoring changes in coin balances over the network&#x27;s channels. We present Twilight, the first PCN that provides a rigorous differential privacy guarantee to its users. Relays in Twilight run a noisy payment processing mechanism that hides the payments they carry. This mechanism increases the relay&#x27;s cost, so Twilight combats selfish relays that wish to avoid it using a trusted execution environment (TEE) that ensures they follow its protocol. The TEE does not store the channel&#x27;s state, which minimizes the trusted computing base. Crucially, Twilight ensures that even if a relay breaks the TEE&#x27;s security, it cannot break the integrity of the PCN. We analyze Twilight in terms of privacy and cost and study the trade-off between them. We implement Twilight using Intel&#x27;s SGX framework and evaluate its performance using relays deployed on two continents. We show that a route consisting of 4 relays handles 820 payments/sec.

  匹配依据：TEE: sgx, trusted execution environment

  </details>

- **CVA6's Data cache: Structure and Behavior**
  2022-02-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.03749)
  Valentin Martinoli, Yannick Teglia, Abdellah Bouagoun, Régis Leveugle

  <details><summary>摘要 / Abstract</summary>

  Since Spectre and Meltdown&#x27;s disclosure in 2018, a new category of attacks has been identified and characterized by the scientific community. The Foreshadow attack, which was the first one to target Intel&#x27;s secure enclave technology (namely SGX) has been developed shortly after. It opened the way to micro architectural attacks on Intel&#x27;s architecture, and led to the quick development of micro architectural attacks until today. While Spectre and Meltdown are often considered as the first micro architectural attacks, one can argue that cache attacks, as introduced by Osvik et al. in 2006, can be seen as the first types of micro architectural attacks that were developed. Now, even though there are many variants, they are still the most prominent type of micro architectural attacks. One example of cache micro architectural covert-channel is the Prime+Probe. Lately targeting the Intel architecture, the micro architectural attacks are now challenging a wider variety of CPUs. Recently, CPUs running the RISC-V Instruction Set Architecture have been targeted. One famous and widely used RISC-V CPU is the ETH Zurich&#x27;s CVA6 (formerly Ariane) core. CVA6 is a 6-stage, single issue, in-order CPU. To the best of our knowledge, there is no existing document presenting very detailed aspects of the CVA6&#x27;s micro architecture, especially with respect to the data cache. Such information is mandatory to deeply understand any architectural or micro architectural study successfully, such as the replication of the Prime+Probe attack on the CVA6 CPU proposed by Nils Wistoff. This paper presents the implementation of the Data cache in the CVA6 CPU from OpenHW Group by focusing on its memory structure and explaining through several examples what happens when a request for memory allocation occurs.

  匹配依据：TEE: secure enclave, sgx

  </details>

- **Towards a trustworthy, secure and reliable enclave for machine learning in a hospital setting: The Essen Medical Computing Platform (EMCP)**
  2022-01-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2201.04816)
  Hendrik F. R. Schmidt, Jörg Schlötterer, Marcel Bargull, Enrico Nasca, Ryan Aydelott, Christin Seifert, Folker Meyer

  <details><summary>摘要 / Abstract</summary>

  AI/Computing at scale is a difficult problem, especially in a health care setting. We outline the requirements, planning and implementation choices as well as the guiding principles that led to the implementation of our secure research computing enclave, the Essen Medical Computing Platform (EMCP), affiliated with a major German hospital. Compliance, data privacy and usability were the immutable requirements of the system. We will discuss the features of our computing enclave and we will provide our recipe for groups wishing to adopt a similar setup.

  匹配依据：TEE: enclave (context)

  </details>

- **Secure Remote Attestation with Strong Key Insulation Guarantees**
  2022-01-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2201.01834)
  Deniz Gurevin, Chenglu Jin, Phuong Ha Nguyen, Omer Khan, Marten van Dijk

  <details><summary>摘要 / Abstract</summary>

  Recent years have witnessed a trend of secure processor design in both academia and industry. Secure processors with hardware-enforced isolation can be a solid foundation of cloud computation in the future. However, due to recent side-channel attacks, the commercial secure processors failed to deliver the promises of a secure isolated execution environment. Sensitive information inside the secure execution environment always gets leaked via side channels. This work considers the most powerful software-based side-channel attackers, i.e., an All Digital State Observing (ADSO) adversary who can observe all digital states, including all digital states in secure enclaves. Traditional signature schemes are not secure in ADSO adversarial model. We introduce a new cryptographic primitive called One-Time Signature with Secret Key Exposure (OTS-SKE), which ensures no one can forge a valid signature of a new message or nonce even if all secret session keys are leaked. OTS-SKE enables us to sign attestation reports securely under the ADSO adversary. We also minimize the trusted computing base by introducing a secure co-processor into the system, and the interaction between the secure co-processor and the attestation processor is unidirectional. That is, the co-processor takes no inputs from the processor and only generates secret keys for the processor to fetch. Our experimental results show that the signing of OTS-SKE is faster than that of Elliptic Curve Digital Signature Algorithm (ECDSA) used in Intel SGX.

  匹配依据：TEE: intel sgx, secure enclaves

  </details>
