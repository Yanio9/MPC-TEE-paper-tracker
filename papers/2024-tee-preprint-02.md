# 2024 · TEE · 仅预印本来源 · 第 2/2 页

[总目录](../PAPERS.md) · [上一页](2024-tee-preprint-01.md)

- **On Practicality of Using ARM TrustZone Trusted Execution Environment for Securing Programmable Logic Controllers**
  2024-03-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.05448)
  Zhiang Li, Daisuke Mashima, Wen Shei Ong, Ertem Esiner, Zbigniew Kalbarczyk, Ee-Chien Chang

  <details><summary>摘要 / Abstract</summary>

  Programmable logic controllers (PLCs) are crucial devices for implementing automated control in various industrial control systems (ICS), such as smart power grids, water treatment systems, manufacturing, and transportation systems. Owing to their importance, PLCs are often the target of cyber attackers that are aiming at disrupting the operation of ICS, including the nation&#x27;s critical infrastructure, by compromising the integrity of control logic execution. While a wide range of cybersecurity solutions for ICS have been proposed, they cannot counter strong adversaries with a foothold on the PLC devices, which could manipulate memory, I/O interface, or PLC logic itself. These days, many ICS devices in the market, including PLCs, run on ARM-based processors, and there is a promising security technology called ARM TrustZone, to offer a Trusted Execution Environment (TEE) on embedded devices. Envisioning that such a hardware-assisted security feature becomes available for ICS devices in the near future, this paper investigates the application of the ARM TrustZone TEE technology for enhancing the security of PLC. Our aim is to evaluate the feasibility and practicality of the TEE-based PLCs through the proof-of-concept design and implementation using open-source software such as OP-TEE and OpenPLC. Our evaluation assesses the performance and resource consumption in real-world ICS configurations, and based on the results, we discuss bottlenecks in the OP-TEE secure OS towards a large-scale ICS and desired changes for its application on ICS devices. Our implementation is made available to public for further study and research.

  匹配依据：TEE: trusted execution environment, trustzone

  </details>

- **Secure Information Embedding in Forensic 3D Fingerprinting**
  2024-03-07 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.04918)
  Canran Wang, Jinwen Wang, Mi Zhou, Vinh Pham, Senyue Hao, Chao Zhou, Ning Zhang, Netanel Raviv

  <details><summary>摘要 / Abstract</summary>

  Printer fingerprinting techniques have long played a critical role in forensic applications, including the tracking of counterfeiters and the safeguarding of confidential information. The rise of 3D printing technology introduces significant risks to public safety, enabling individuals with internet access and consumer-grade 3D printers to produce untraceable firearms, counterfeit products, and more. This growing threat calls for a better mechanism to track the production of 3D-printed parts. Inspired by the success of fingerprinting on traditional 2D printers, we introduce SIDE (\textbf{S}ecure \textbf{I}nformation Embe\textbf{D}ding and \textbf{E}xtraction), a novel fingerprinting framework tailored for 3D printing. SIDE addresses the adversarial challenges of 3D print forensics by offering both secure information embedding and extraction. First, through novel coding-theoretic techniques, SIDE is both~\emph{break-resilient} and~\emph{loss-tolerant}, enabling fingerprint recovery even if the adversary breaks the print into fragments and conceals a portion of them. Second, SIDE further leverages Trusted Execution Environments (TEE) to secure the fingerprint embedding process.

  匹配依据：TEE: trusted execution environments

  </details>

- **Bridge the Future: High-Performance Networks in Confidential VMs without Trusted I/O devices**
  2024-03-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.03360)
  Mengyuan Li, Shashvat Srivastava, Mengjia Yan

  <details><summary>摘要 / Abstract</summary>

  Trusted I/O (TIO) is an appealing solution to improve I/O performance for confidential VMs (CVMs), with the potential to eliminate broad sources of I/O overhead. However, this paper emphasizes that not all types of I/O can derive substantial benefits from TIO, particularly network I/O. Given the obligatory use of encryption protocols for network traffic in CVM&#x27;s threat model, TIO&#x27;s approach of I/O encryption over the PCIe bus becomes redundant. Furthermore, TIO solutions need to expand the Trusted Computing Base (TCB) to include TIO devices and are commercially unavailable. Motivated by these insights, the goal of this paper is to propose a software solution that helps CVMs immediately benefit from high-performance networks, while confining trust only to the on-chip CVM. We present FOLIO, a software solution crafted from a secure and efficient Data Plane Development Kit (DPDK) extension compatible with the latest version of AMD Secure Encrypted Virtualization (SEV), a.k.a., Secure Nested Paging (SNP). Our design is informed by a thorough analysis of all possible factors that impact SNP VM&#x27;s network performance. By extensively removing overhead sources, we arrive at a design that approaches the efficiency of an optimal TIO-based configuration. Evaluation shows that FOLIO has a performance dip less than 6% relative to the optimal TIO configuration, while only relying on off-the-shelf CPUs.

  匹配依据：TEE: secure encrypted virtualization

  </details>

- **TRUCE: Private Benchmarking to Prevent Contamination and Improve Comparative Evaluation of LLMs**
  2024-03-01 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.00393)
  Tanmay Rajore, Nishanth Chandran, Sunayana Sitaram, Divya Gupta, Rahul Sharma, Kashish Mittal, Manohar Swaminathan

  <details><summary>摘要 / Abstract</summary>

  Benchmarking is the de-facto standard for evaluating LLMs, due to its speed, replicability and low cost. However, recent work has pointed out that the majority of the open source benchmarks available today have been contaminated or leaked into LLMs, meaning that LLMs have access to test data during pretraining and/or fine-tuning. This raises serious concerns about the validity of benchmarking studies conducted so far and the future of evaluation using benchmarks. To solve this problem, we propose Private Benchmarking, a solution where test datasets are kept private and models are evaluated without revealing the test data to the model. We describe various scenarios (depending on the trust placed on model owners or dataset owners), and present solutions to avoid data contamination using private benchmarking. For scenarios where the model weights need to be kept private, we describe solutions from confidential computing and cryptography that can aid in private benchmarking. We build an end-to-end system, TRUCE, that enables such private benchmarking showing that the overheads introduced to protect models and benchmark are negligible (in the case of confidential computing) and tractable (when cryptographic security is required). Finally, we also discuss solutions to the problem of benchmark dataset auditing, to ensure that private benchmarks are of sufficiently high quality.

  匹配依据：TEE: confidential computing

  </details>

- **State-of-the-Art Approaches to Enhancing Privacy Preservation of Machine Learning Datasets: A Survey**
  2024-02-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.16847)
  Chaoyu Zhang, Shaoyu Li

  <details><summary>摘要 / Abstract</summary>

  This paper examines the evolving landscape of machine learning (ML) and its profound impact across various sectors, with a special focus on the emerging field of Privacy-preserving Machine Learning (PPML). As ML applications become increasingly integral to industries like telecommunications, financial technology, and surveillance, they raise significant privacy concerns, necessitating the development of PPML strategies. The paper highlights the unique challenges in safeguarding privacy within ML frameworks, which stem from the diverse capabilities of potential adversaries, including their ability to infer sensitive information from model outputs or training data. We delve into the spectrum of threat models that characterize adversarial intentions, ranging from membership and attribute inference to data reconstruction. The paper emphasizes the importance of maintaining the confidentiality and integrity of training data, outlining current research efforts that focus on refining training data to minimize privacy-sensitive information and enhancing data processing techniques to uphold privacy. Through a comprehensive analysis of privacy leakage risks and countermeasures in both centralized and collaborative learning settings, this paper aims to provide a thorough understanding of effective strategies for protecting ML training data against privacy intrusions. It explores the balance between data privacy and model utility, shedding light on privacy-preserving techniques that leverage cryptographic methods, Differential Privacy, and Trusted Execution Environments. The discussion extends to the application of these techniques in sensitive domains, underscoring the critical role of PPML in ensuring the privacy and security of ML systems.

  匹配依据：TEE: trusted execution environments

  </details>

- **Trustworthy confidential virtual machines for the masses**
  2024-02-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.15277)
  Anna Galanou, Khushboo Bindlish, Luca Preibsch, Yvonne-Anne Pignolet, Christof Fetzer, Rüdiger Kapitza

  <details><summary>摘要 / Abstract</summary>

  Confidential computing alleviates the concerns of distrustful customers by removing the cloud provider from their trusted computing base and resolves their disincentive to migrate their workloads to the cloud. This is facilitated by new hardware extensions, like AMD&#x27;s SEV Secure Nested Paging (SEV-SNP), which can run a whole virtual machine with confidentiality and integrity protection against a potentially malicious hypervisor owned by an untrusted cloud provider. However, the assurance of such protection to either the service providers deploying sensitive workloads or the end-users passing sensitive data to services requires sending proof to the interested parties. Service providers can retrieve such proof by performing remote attestation while end-users have typically no means to acquire this proof or validate its correctness and therefore have to rely on the trustworthiness of the service providers. In this paper, we present Revelio, an approach that features two main contributions: i) it allows confidential virtual machine (VM)-based workloads to be designed and deployed in a way that disallows any tampering even by the service providers and ii) it empowers users to easily validate their integrity. In particular, we focus on web-facing workloads, protect them leveraging SEV-SNP, and enable end-users to remotely attest them seamlessly each time a new web session is established. To highlight the benefits of Revelio, we discuss how a standalone stateful VM that hosts an open-source collaboration office suite can be secured and present a replicated protocol proxy that enables commodity users to securely access the Internet Computer, a decentralized blockchain infrastructure.

  匹配依据：TEE: confidential computing, sev snp

  </details>

- **Prime+Retouch: When Cache is Locked and Leaked**
  2024-02-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.15425)
  Jaehyuk Lee, Fan Sang, Taesoo Kim

  <details><summary>摘要 / Abstract</summary>

  Caches on the modern commodity CPUs have become one of the major sources of side-channel leakages and been abused as a new attack vector. To thwart the cache-based side-channel attacks, two types of countermeasures have been proposed: detection-based ones that limit the amount of microarchitectural traces an attacker can leave, and cache prefetching-and-locking techniques that claim to prevent such leakage by disallowing evictions on sensitive data. In this paper, we present the Prime+Retouch attack that completely bypasses these defense schemes by accurately inferring the cache activities with the metadata of the cache replacement policy. Prime+Retouch has three noticeable properties: 1) it incurs no eviction on the victim&#x27;s data, allowing us to bypass the two known mitigation schemes, 2) it requires minimal synchronization of only one memory access to the attacker&#x27;s pre-primed cache lines, and 3) it leaks data via non-shared memory, yet because underlying eviction metadata is shared. We demonstrate Prime+Retouch in two architectures: predominant Intel x86 and emerging Apple M1. We elucidate how Prime+Retouch can break the T-table implementation of AES with robust cache side-channel mitigations such as Cloak, under both normal and SGX-protected environments. We also manifest feasibility of the Prime+Retouch attack on the M1 platform imposing more restrictions where the precise measurement tools such as core clock cycle timer and performance counters are inaccessible to the attacker. Furthermore, we first demystify undisclosed cache architecture and its eviction policy of L1 data cache on Apple M1 architecture. We also devise a user-space noise-free cache monitoring tool by repurposing Intel TSX.

  匹配依据：TEE: sgx

  </details>

- **Privacy-Enhancing Collaborative Information Sharing through Federated Learning -- A Case of the Insurance Industry**
  2024-02-22 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.14983)
  Panyi Dong, Zhiyu Quan, Brandon Edwards, Shih-han Wang, Runhuan Feng, Tianyang Wang, Patrick Foley, Prashant Shah

  <details><summary>摘要 / Abstract</summary>

  The report demonstrates the benefits (in terms of improved claims loss modeling) of harnessing the value of Federated Learning (FL) to learn a single model across multiple insurance industry datasets without requiring the datasets themselves to be shared from one company to another. The application of FL addresses two of the most pressing concerns: limited data volume and data variety, which are caused by privacy concerns, the rarity of claim events, the lack of informative rating factors, etc.. During each round of FL, collaborators compute improvements on the model using their local private data, and these insights are combined to update a global model. Such aggregation of insights allows for an increase to the effectiveness in forecasting claims losses compared to models individually trained at each collaborator. Critically, this approach enables machine learning collaboration without the need for raw data to leave the compute infrastructure of each respective data owner. Additionally, the open-source framework, OpenFL, that is used in our experiments is designed so that it can be run using confidential computing as well as with additional algorithmic protections against leakage of information via the shared model updates. In such a way, FL is implemented as a privacy-enhancing collaborative learning technique that addresses the challenges posed by the sensitivity and privacy of data in traditional machine learning solutions. This paper&#x27;s application of FL can also be expanded to other areas including fraud detection, catastrophe modeling, etc., that have a similar need to incorporate data privacy into machine learning collaborations. Our framework and empirical results provide a foundation for future collaborations among insurers, regulators, academic researchers, and InsurTech experts.

  匹配依据：TEE: confidential computing

  </details>

- **Exploiting RPMB authentication in a closed source TEE implementation**
  2024-02-06 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/180)
  Aya Fukami, Richard Buurke, Zeno Geradts

  <details><summary>摘要 / Abstract</summary>

  Embedded Multimedia Cards (eMMCs) provide a protected memory area called the Replay Protected Memory Block (RPMB). eMMCs are commonly used as storage media in modern smartphones. In order to protect these devices from unauthorized access, important data is stored in the RPMB area in an authenticated manner. Modification of the RPMB data requires a pre-shared authentication key. An unauthorized user cannot change the stored data. On modern devices, this pre-shared key is generated and used exclusively within a Trusted Execution Environment (TEE) preventing attackers from access. In this paper, we investigate how the authentication key for RPMB is programmed on the eMMC. We found that this key can be extracted directly from the target memory chip. Once obtained, the authentication key can be used to manipulate stored data. In addition, poor implementation of certain security features, aimed at preventing replay attacks using RPMB on the host system can be broken by an attacker. We show how the authentication key can be extracted and how it can be used to break the anti-rollback protection to enable data restoration even after a data wipe operation has been completed. Our findings show that non-secure RPMB implementations can enable forensic investigators to break security features implemented on modern smartphones.

  匹配依据：TEE: trusted execution environment

  </details>

- **Cryptographically Assured Information Flow: Assured Remote Execution**
  2024-02-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.02630)
  Scott L. Dyer, Christian A. Femrite, Joshua D. Guttman, Julian P. Lanson, Moses D. Liskov

  <details><summary>摘要 / Abstract</summary>

  Assured Remote Execution on a device is the ability of suitably authorized parties to construct secure channels with known processes -- i.e. processes executing known code -- running on it. Assured Remote Execution requires a hardware basis including cryptographic primitives. In this paper, we show that a simple hardware-level mechanism called Cryptographically Assured Information Flow (CAIF) enables Assured Remote Execution. CAIF is akin to some operations in existing Trusted Execution Environments, but securely implements an ideal functionality defined in terms of logging and confidential escrow. We show how to achieve Assured Remote Execution for a wide variety of processes on a CAIF device. Cryptographic protocol analysis demonstrates our security goals are achieved even against a strong adversary that may modify our programs and execute unauthorized programs on the device. Assured Remote Execution enables useful functionality such as trustworthy remote attestation, and provides some of the support needed for secure remote reprogramming.

  匹配依据：TEE: trusted execution environments

  </details>

- **Elephants Do Not Forget: Differential Privacy with State Continuity for Privacy Budget**
  2024-01-31 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.17628)
  Jiankai Jin, Chitchanok Chuengsatiansup, Toby Murray, Benjamin I. P. Rubinstein, Yuval Yarom, Olga Ohrimenko

  <details><summary>摘要 / Abstract</summary>

  Current implementations of differentially-private (DP) systems either lack support to track the global privacy budget consumed on a dataset, or fail to faithfully maintain the state continuity of this budget. We show that failure to maintain a privacy budget enables an adversary to mount replay, rollback and fork attacks - obtaining answers to many more queries than what a secure system would allow. As a result the attacker can reconstruct secret data that DP aims to protect - even if DP code runs in a Trusted Execution Environment (TEE). We propose ElephantDP, a system that aims to provide the same guarantees as a trusted curator in the global DP model would, albeit set in an untrusted environment. Our system relies on a state continuity module to provide protection for the privacy budget and a TEE to faithfully execute DP code and update the budget. To provide security, our protocol makes several design choices including the content of the persistent state and the order between budget updates and query answers. We prove that ElephantDP provides liveness (i.e., the protocol can restart from a correct state and respond to queries as long as the budget is not exceeded) and DP confidentiality (i.e., an attacker learns about a dataset as much as it would from interacting with a trusted curator). Our implementation and evaluation of the protocol use Intel SGX as a TEE to run the DP code and a network of TEEs to maintain state continuity. Compared to an insecure baseline, we observe 1.1-3.2$\times$ overheads and lower relative overheads for complex DP queries.

  匹配依据：TEE: intel sgx, trusted execution environment

  </details>

- **Data-Oblivious ML Accelerators using Hardware Security Extensions**
  2024-01-29 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.16583)
  Hossam ElAtali, John Z. Jekel, Lachlan J. Gunn, N. Asokan

  <details><summary>摘要 / Abstract</summary>

  Outsourced computation can put client data confidentiality at risk. Existing solutions are either inefficient or insufficiently secure: cryptographic techniques like fully-homomorphic encryption incur significant overheads, even with hardware assistance, while the complexity of hardware-assisted trusted execution environments has been exploited to leak secret data. Recent proposals such as BliMe and OISA show how dynamic information flow tracking (DIFT) enforced in hardware can protect client data efficiently. They are designed to protect CPU-only workloads. However, many outsourced computing applications, like machine learning, make extensive use of accelerators. We address this gap with Dolma, which applies DIFT to the Gemmini matrix multiplication accelerator, efficiently guaranteeing client data confidentiality, even in the presence of malicious/vulnerable software and side channel attacks on the server. We show that accelerators can allow DIFT logic optimizations that significantly reduce area overhead compared with general-purpose processor architectures. Dolma is integrated with the BliMe framework to achieve end-to-end security guarantees. We evaluate Dolma on an FPGA using a ResNet-50 DNN model and show that it incurs low overheads for large configurations ($4.4\%$, $16.7\%$, $16.5\%$ for performance, resource usage and power, respectively, with a 32x32 configuration).

  匹配依据：TEE: trusted execution environments

  </details>

- **Fuzzy Extractors are Practical: Cryptographic Strength Key Derivation from the Iris**
  2024-01-22 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/100)
  Amey Shukla, Luke Demarest, Benjamin Fuller, Sohaib Ahmad, Caleb Manicke, Alexander Russell, Sixia Chen

  <details><summary>摘要 / Abstract</summary>

  Despite decades of effort, a persistent chasm has existed between the theory and practice of device-level biometric authentication. Theoretical constructions can, in principle, provide biometric authentication with cryptographically secure public enrollment data. However, concrete implementations of these techniques have failed to provide security with real-world parameters. The result is that deployed authentication algorithms rely on data that overtly leaks private information about the biometric; thus systems rely on externalized security measures such as trusted execution environments. We close this chasm. We introduce a key derivation system with $105$ bits of entropy and a $92%$ true accept rate (TAR) for the iris. Our system advances 1) the feature extraction from the iris and 2) the fuzzy extractor used to derive keys. The fuzzy extractor builds on sample-then-lock (Canetti et al., Journal of Cryptology 2021). We (1) Introduce a new sampling method with a better trade-off between TAR and entropy when features have different quality, (2) Correct Canetti et al.&#x27;s main security proof, showing the minimum of min-entropy over subsets is the relevant security measure, and (3) Tighten Canetti et al.&#x27;s concrete analysis, nearly doubling security under reasonable assumptions. Our final feature extractor incorporates ideas from the new sampling method to produce features optimized for the sample-then-lock construction. The only statistical assumption needed to show security of our system is necessary: the accuracy of min-entropy estimation. At $105$ bits, our quantitative level of security is well above prior work. Simhadri et al. (ISC, 2019) report $32$ bits on the iris, but they have a bug in their analysis that reduces their strength. Zhang et al.&#x27;s (ePrint 2021/1559) system achieves $45$ bits on the face but assumes independence between biometrics and the used error-correcting code, an assumption that cannot be easily verified.

  匹配依据：TEE: trusted execution environments

  </details>

- **Tempo: Confidentiality Preservation in Cloud-Based Neural Network Training**
  2024-01-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.11531)
  Rongwu Xu, Zhixuan Fang

  <details><summary>摘要 / Abstract</summary>

  Cloud deep learning platforms provide cost-effective deep neural network (DNN) training for customers who lack computation resources. However, cloud systems are often untrustworthy and vulnerable to attackers, leading to growing concerns about model privacy. Recently, researchers have sought to protect data privacy in deep learning by leveraging CPU trusted execution environments (TEEs), which minimize the use of cryptography, but existing works failed to simultaneously utilize the computational resources of GPUs to assist in training and prevent model leakage. This paper presents Tempo, the first cloud-based deep learning system that cooperates with TEE and distributed GPUs for efficient DNN training with model confidentiality preserved. To tackle the challenge of preserving privacy while offloading linear algebraic operations from TEE to GPUs for efficient batch computation, we introduce a customized permutation-based obfuscation algorithm to blind both inputs and model parameters. An optimization mechanism that reduces encryption operations is proposed for faster weight updates during backpropagation to speed up training. We implement Tempo and evaluate it with both training and inference for two prevalent DNNs. Empirical results indicate that Tempo outperforms baselines and offers sufficient privacy protection.

  匹配依据：TEE: trusted execution environments

  </details>

- **A Fast, Performant, Secure Distributed Training Framework For Large Language Model**
  2024-01-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.09796)
  Wei Huang, Yinggui Wang, Anda Cheng, Aihui Zhou, Chaofan Yu, Lei Wang

  <details><summary>摘要 / Abstract</summary>

  The distributed (federated) LLM is an important method for co-training the domain-specific LLM using siloed data. However, maliciously stealing model parameters and data from the server or client side has become an urgent problem to be solved. In this paper, we propose a secure distributed LLM based on model slicing. In this case, we deploy the Trusted Execution Environment (TEE) on both the client and server side, and put the fine-tuned structure (LoRA or embedding of P-tuning v2) into the TEE. Then, secure communication is executed in the TEE and general environments through lightweight encryption. In order to further reduce the equipment cost as well as increase the model performance and accuracy, we propose a split fine-tuning scheme. In particular, we split the LLM by layers and place the latter layers in a server-side TEE (the client does not need a TEE). We then combine the proposed Sparsification Parameter Fine-tuning (SPF) with the LoRA part to improve the accuracy of the downstream task. Numerous experiments have shown that our method guarantees accuracy while maintaining security.

  匹配依据：TEE: trusted execution environment

  </details>

- **HasTEE+ : Confidential Cloud Computing and Analytics with Haskell**
  2024-01-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.08901)
  Abhiroop Sarkar, Alejandro Russo

  <details><summary>摘要 / Abstract</summary>

  Confidential computing is a security paradigm that enables the protection of confidential code and data in a co-tenanted cloud deployment using specialized hardware isolation units called Trusted Execution Environments (TEEs). By integrating TEEs with a Remote Attestation protocol, confidential computing allows a third party to establish the integrity of an \textit{enclave} hosted within an untrusted cloud. However, TEE solutions, such as Intel SGX and ARM TrustZone, offer low-level C/C++-based toolchains that are susceptible to inherent memory safety vulnerabilities and lack language constructs to monitor explicit and implicit information-flow leaks. Moreover, the toolchains involve complex multi-project hierarchies and the deployment of hand-written attestation protocols for verifying \textit{enclave} integrity. We address the above with HasTEE+, a domain-specific language (DSL) embedded in Haskell that enables programming TEEs in a high-level language with strong type-safety. HasTEE+ assists in multi-tier cloud application development by (1) introducing a \textit{tierless} programming model for expressing distributed client-server interactions as a single program, (2) integrating a general remote-attestation architecture that removes the necessity to write application-specific cross-cutting attestation code, and (3) employing a dynamic information flow control mechanism to prevent explicit as well as implicit data leaks. We demonstrate the practicality of HasTEE+ through a case study on confidential data analytics, presenting a data-sharing pattern applicable to mutually distrustful participants and providing overall performance metrics.

  匹配依据：TEE: confidential computing, intel sgx, trusted execution environments, trustzone

  </details>
