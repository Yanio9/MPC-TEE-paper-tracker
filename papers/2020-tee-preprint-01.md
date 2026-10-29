# 2020 · TEE · 仅预印本来源 · 第 1/1 页

[总目录](../PAPERS.md)

- **TEEMon: A continuous performance monitoring framework for TEEs**
  2020-12-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2012.06554)
  Robert Krahn, Donald Dragoti, Franz Gregor, Do Le Quoc, Valerio Schiavoni, Pascal Felber, Clenimar Souza, Andrey Brito, Christof Fetzer

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs), such as Intel Software Guard eXtensions (SGX), are considered as a promising approach to resolve security challenges in clouds. TEEs protect the confidentiality and integrity of application code and data even against privileged attackers with root and physical access by providing an isolated secure memory area, i.e., enclaves. The security guarantees are provided by the CPU, thus even if system software is compromised, the attacker can never access the enclave&#x27;s content. While this approach ensures strong security guarantees for applications, it also introduces a considerable runtime overhead in part by the limited availability of protected memory (enclave page cache). Currently, only a limited number of performance measurement tools for TEE-based applications exist and none offer performance monitoring and analysis during runtime. This paper presents TEEMon, the first continuous performance monitoring and analysis tool for TEE-based applications. TEEMon provides not only fine-grained performance metrics during runtime, but also assists the analysis of identifying causes of performance bottlenecks, e.g., excessive system calls. Our approach smoothly integrates with existing open-source tools (e.g., Prometheus or Grafana) towards a holistic monitoring solution, particularly optimized for systems deployed through Docker containers or Kubernetes and offers several dedicated metrics and visualizations. Our evaluation shows that TEEMon&#x27;s overhead ranges from 5% to 17%.

  匹配依据：TEE: sgx, trusted execution environments

  </details>

- **RouTEE: A Secure Payment Network Routing Hub using Trusted Execution Environments**
  2020-12-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2012.04254)
  Junmo Lee, Seongjun Kim, Sanghyeon Park, Soo-Mook Moon

  <details><summary>摘要 / Abstract</summary>

  Cryptocurrencies such as Bitcoin and Ethereum have made payment transactions possible without a trusted third party, but they have a scalability issue due to their consensus mechanisms. Payment networks have emerged to overcome this limitation by executing transactions outside of the blockchain, which is why these are referred to as off-chain transactions. In order to establish a payment channel between two users, the users lock their deposits in the blockchain, and then they can pay each other through the channel. Furthermore, payment networks support multi-hop payments that allow users to transfer their balances to other users who are connected to them via multiple channels. However, multi-hop payments are hard to be accomplished, as they are heavily dependent on routing users on a payment path from a sender to a receiver. Although routing hubs can make multi-hop payments more practical and efficient, they need a lot of collateral locked for a long period and have privacy issues in terms of payment history. We propose RouTEE, a secure payment routing hub that is fully feasible without the hub&#x27;s deposit. Unlike existing payment networks, RouTEE provides high balance liquidity, and details about payments are concealed from hosts by leveraging trusted execution environments (TEEs). RouTEE is designed to make rational hosts behave honestly, by introducing a new routing fee scheme and a secure settlement method. Moreover, users do not need to monitor the blockchain in real-time or run full nodes. They can participate in RouTEE by simply verifying block headers through light clients; furthermore, having only one channel with RouTEE is sufficient to interact with other users. Our implementation demonstrates that RouTEE is highly efficient and outperforms Lightning Network that is the state-of-the-art payment network.

  匹配依据：TEE: trusted execution environments

  </details>

- **On the Challenges of Detecting Side-Channel Attacks in SGX**
  2020-11-30 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.14599)
  Jianyu Jiang, Claudio Soriente, Ghassan Karame

  <details><summary>摘要 / Abstract</summary>

  Existing tools to detect side-channel attacks on Intel SGX are grounded on the observation that attacks affect the performance of the victim application. As such, all detection tools monitor the potential victim and raise an alarm if the witnessed performance (in terms of runtime, enclave interruptions, cache misses, etc.) is out of the ordinary. In this paper, we show that monitoring the performance of enclaves to detect side-channel attacks may not be effective. Our core intuition is that all monitoring tools are geared towards an adversary that interferes with the victim&#x27;s execution in order to extract the most number of secret bits (e.g., the entire secret) in one or few runs. They cannot, however, detect an adversary that leaks smaller portions of the secret - as small as a single bit - at each execution of the victim. In particular, by minimizing the information leaked at each run, the impact of any side-channel attack on the application&#x27;s performance is significantly lowered - ensuring that the detection tool does not detect an attack. By repeating the attack multiple times, each time on a different part of the secret, the adversary can recover the whole secret and remain undetected. Based on this intuition, we adapt known attacks leveraging page-tables and L3 cache to bypass existing detection mechanisms. We show experimentally how an attacker can successfully exfiltrate the secret key used in an enclave running various cryptographic routines of libgcrypt. Beyond cryptographic libraries, we also show how to compromise the predictions of enclaves running decision-tree routines of OpenCV. Our evaluation results suggest that performance-based detection tools do not deter side-channel attacks on SGX enclaves and that effective detection mechanisms are yet to be designed.

  匹配依据：TEE: intel sgx, sgx, sgx enclaves

  </details>

- **CommiTEE: An Efficient and Secure Commit-Chain Protocol using TEEs**
  2020-11-29 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1486)
  Andreas Erwig, Sebastian Faust, Siavash Riahi, Tobias Stöckert

  <details><summary>摘要 / Abstract</summary>

  Permissionless blockchain systems such as Bitcoin or Ethereum are slow and expensive, since transactions are processed in a distributed network by a large set of parties. To improve on these shortcomings, a prominent approach is given by so-called 2nd-layer protocols. In these protocols parties process transactions off-chain directly between each other, thereby drastically reducing the costly and slow interaction with the blockchain. In particular, in the optimistic case, when parties behave honestly, no interaction with the blockchain is needed. One of the most popular off-chain solutions are Plasma protocols (often also called commit-chains). These protocols are orchestrated by a so-called operator that maintains the system and processes transactions between parties. Importantly, the operator is trustless, i.e., even if it is malicious users of the system are guaranteed to not lose funds. To achieve this guarantee, Plasma protocols are highly complex and require involved and expensive dispute resolution processes. This has significantly slowed down development and deployment of these systems. In this work we propose CommiTEE-- a simple and efficient Plasma system leveraging the power of trusted execution environments (TEE). Besides its simplicity, our protocol requires minimal interaction with the blockchain, thereby drastically reducing costs and improving efficiency. An additional benefit of our solution is that it allows for switching between operators, in case the main operator goes offline due to system failure, or behaving maliciously. We implemented and evaluated our system over Ethereum and show that it is at least $2$ times (and in some cases more than $16$ times) cheaper in terms of communication complexity when compared to existing Plasma implementations. Moreover, for protocols using zero-knowledge proofs (like NOCUST-ZKP), CommiTEE decreases the on-chain gas cost by a factor $\approx 19$ compared to prior solution.

  匹配依据：TEE: trusted execution environments

  </details>

- **Subversion-Resilient Enhanced Privacy ID**
  2020-11-19 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1450)
  Antonio Faonio, Dario Fiore, Luca Nizzardo, Claudio Soriente

  <details><summary>摘要 / Abstract</summary>

  Anonymous attestation for secure hardware platforms leverages tailored group signature schemes and assumes the hardware to be trusted. Yet, there is an ever increasing concern on the trustworthiness of hardware components and embedded systems. A subverted hardware may, for example, use its signatures to exfiltrate identifying information or even the signing key. In this paper we focus on Enhanced Privacy ID (EPID)---a popular anonymous attestation scheme used in commodity secure hardware platforms like Intel SGX. We define and instantiate a \emph{subversion resilient} EPID scheme (or SR-EPID). In a nutshell, SR-EPID provides the same functionality and security guarantees of the original EPID, despite potentially subverted hardware. In our design, a ``sanitizer&#x27;&#x27; ensures no covert channel between the hardware and the outside world both during enrollment and during attestation (i.e., when signatures are produced). We design a practical SR-EPID scheme secure against adaptive corruptions and based on a novel combination of malleable NIZKs and hash functions modeled as random oracles. Our approach has a number of advantages over alternative designs. Namely, the sanitizer bears no secret information---hence, a memory leak does not erode security. Further, the role of sanitizer may be distributed in a cascade fashion among several parties so that sanitization becomes effective as long as one of the parties has access to a good source of randomness. Also, we keep the signing protocol non-interactive, thereby minimizing latency during signature generation.

  匹配依据：TEE: intel sgx

  </details>

- **Golden Grain: Building a Secure and Decentralized Model Marketplace for MLaaS**
  2020-11-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.06458)
  Jiasi Weng, Jian Weng, Chengjun Cai, Hongwei Huang, Cong Wang

  <details><summary>摘要 / Abstract</summary>

  ML-as-a-service (MLaaS) becomes increasingly popular and revolutionizes the lives of people. A natural requirement for MLaaS is, however, to provide highly accurate prediction services. To achieve this, current MLaaS systems integrate and combine multiple well-trained models in their services. Yet, in reality, there is no easy way for MLaaS providers, especially for startups, to collect sufficiently well-trained models from individual developers, due to the lack of incentives. In this paper, we aim to fill this gap by building up a model marketplace, called as Golden Grain, to facilitate model sharing, which enforces the fair model-money swapping process between individual developers and MLaaS providers. Specifically, we deploy the swapping process on the blockchain, and further introduce a blockchain-empowered model benchmarking process for transparently determining the model prices according to their authentic performances, so as to motivate the faithful contributions of well-trained models. Especially, to ease the blockchain overhead for model benchmarking, our marketplace carefully offloads the heavy computation and designs a secure off-chain on-chain interaction protocol based on a trusted execution environment (TEE), for ensuring both the integrity and authenticity of benchmarking. We implement a prototype of our Golden Grain on the Ethereum blockchain, and conduct extensive experiments using standard benchmark datasets to demonstrate the practically affordable performance of our design.

  匹配依据：TEE: trusted execution environment

  </details>

- **Customizing Trusted AI Accelerators for Efficient Privacy-Preserving Machine Learning**
  2020-11-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.06376)
  Peichen Xie, Xuanle Ren, Guangyu Sun

  <details><summary>摘要 / Abstract</summary>

  The use of trusted hardware has become a promising solution to enable privacy-preserving machine learning. In particular, users can upload their private data and models to a hardware-enforced trusted execution environment (e.g. an enclave in Intel SGX-enabled CPUs) and run machine learning tasks in it with confidentiality and integrity guaranteed. To improve performance, AI accelerators have been widely employed for modern machine learning tasks. However, how to protect privacy on an AI accelerator remains an open question. To address this question, we propose a solution for efficient privacy-preserving machine learning based on an unmodified trusted CPU and a customized trusted AI accelerator. We carefully leverage cryptographic primitives to establish trust and protect the channel between the CPU and the accelerator. As a case study, we demonstrate our solution based on the open-source versatile tensor accelerator. The result of evaluation shows that the proposed solution provides efficient privacy-preserving machine learning at a small design cost and moderate performance overhead.

  匹配依据：TEE: intel sgx, trusted execution environment

  </details>

- **ShadowNet: A Secure and Efficient On-device Model Inference System for Convolutional Neural Networks**
  2020-11-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.05905)
  Zhichuang Sun, Ruimin Sun, Changming Liu, Amrita Roy Chowdhury, Long Lu, Somesh Jha

  <details><summary>摘要 / Abstract</summary>

  With the increased usage of AI accelerators on mobile and edge devices, on-device machine learning (ML) is gaining popularity. Thousands of proprietary ML models are being deployed today on billions of untrusted devices. This raises serious security concerns about model privacy. However, protecting model privacy without losing access to the untrusted AI accelerators is a challenging problem. In this paper, we present a novel on-device model inference system, ShadowNet. ShadowNet protects the model privacy with Trusted Execution Environment (TEE) while securely outsourcing the heavy linear layers of the model to the untrusted hardware accelerators. ShadowNet achieves this by transforming the weights of the linear layers before outsourcing them and restoring the results inside the TEE. The non-linear layers are also kept secure inside the TEE. ShadowNet&#x27;s design ensures efficient transformation of the weights and the subsequent restoration of the results. We build a ShadowNet prototype based on TensorFlow Lite and evaluate it on five popular CNNs, namely, MobileNet, ResNet-44, MiniVGG, ResNet-404, and YOLOv4-tiny. Our evaluation shows that ShadowNet achieves strong security guarantees with reasonable performance, offering a practical solution for secure on-device model inference.

  匹配依据：TEE: trusted execution environment

  </details>

- **Tokoin: A Coin-Based Accountable Access Control Scheme for Internet of Things**
  2020-11-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.04919)
  Chunchi Liu, Minghui Xu, Hechuan Guo, Xiuzhen Cheng, Yinhao Xiao, Dongxiao Yu, Bei Gong, Arkady Yerukhimovich, Shengling Wang, Weifeng Lv

  <details><summary>摘要 / Abstract</summary>

  With the prevalence of Internet of Things (IoT) applications, IoT devices interact closely with our surrounding environments, bringing us unparalleled smartness and convenience. However, the development of secure IoT solutions is getting a long way lagged behind, making us exposed to common unauthorized accesses that may bring malicious attacks and unprecedented danger to our daily life. Overprivilege attack, a widely reported phenomenon in IoT that accesses unauthorized or excessive resources, is notoriously hard to prevent, trace and mitigate. To tackle this challenge, we propose Tokoin-Based Access Control (TBAC), an accountable access control model enabled by blockchain and Trusted Execution Environment (TEE) technologies, to offer fine-graininess, strong auditability, and access procedure control for IoT. TBAC materializes the virtual access power into a definite-amount and secure cryptographic coin termed &quot;tokoin&quot; (token+coin), and manages it using atomic and accountable state-transition functions in a blockchain. We also realize access procedure control by mandating every tokoin a fine-grained access policy defining who is allowed to do what at when in where by how. The tokoin is peer-to-peer transferable, and can be modified only by the resource owner when necessary. We fully implement TBAC with well-studied cryptographic primitives and blockchain platforms and present a readily available APP for regular users. We also present a case study to demonstrate how TBAC is employed to enable autonomous in-home cargo delivery while guaranteeing the access policy compliance and home owner&#x27;s physical security by regulating the physical behaviors of the deliveryman.

  匹配依据：TEE: trusted execution environment

  </details>

- **Mitigating Leakage in Federated Learning with Trusted Hardware**
  2020-11-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.04948)
  Javad Ghareh Chamani, Dimitrios Papadopoulos

  <details><summary>摘要 / Abstract</summary>

  In federated learning, multiple parties collaborate in order to train a global model over their respective datasets. Even though cryptographic primitives (e.g., homomorphic encryption) can help achieve data privacy in this setting, some partial information may still be leaked across parties if this is done non-judiciously. In this work, we study the federated learning framework of SecureBoost [Cheng et al., FL@IJCAI&#x27;19] as a specific such example, demonstrate a leakage-abuse attack based on its leakage profile, and experimentally evaluate the effectiveness of our attack. We then propose two secure versions relying on trusted execution environments. We implement and benchmark our protocols to demonstrate that they are 1.2-5.4X faster in computation and need 5-49X less communication than SecureBoost.

  匹配依据：TEE: trusted execution environments

  </details>

- **ELM : A Low-Latency and Scalable Memory Encryption Scheme**
  2020-11-10 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1374)
  Akiko Inoue, Kazuhiko Minematsu, Maya Oda, Rei Ueno, Naofumi Homma

  <details><summary>摘要 / Abstract</summary>

  Memory encryption with an authentication tree has received significant attentions due to the increasing threats of active attacks and the widespread use of non-volatile memories. It is also gradually deployed to real-world systems, as shown by SGX available in Intel processors. The topic of memory encryption has been recently extensively studied, most actively from the viewpoint of system architecture. In this paper, we study the topic from the viewpoint of provable secure symmetric-key designs, with a primal focus on latency which is an important criterion for memory. A progress in such a direction can be observed in the memory encryption scheme inside SGX (SGX integrity tree or SIT). It uses dedicated, low-latency symmetric-key components, i.e., a message authentication code (MAC) and an authenticated encryption (AE) scheme based on AES-GCM. SIT has an excellent latency, however, it has a scalability issue for its on-chip memory size. By carefully examining the required behavior of MAC and AE schemes and their interactions in the tree operations, we develop a new memory encryption scheme called ELM. It consists of fully-parallelizable, low-latency MAC and AE schemes and utilizes an incremental property of the MAC. Our AE scheme is similar to OCB, however it improves OCB in terms of decryption latency. To showcase the effectiveness, we consider instantiations of ELM using the same cryptographic cores as SIT, and show that ELM has significantly lower latency than SIT for large memories. We also conducted preliminary hardware implementations to show that the total implementation size is comparable to SIT.

  匹配依据：TEE: sgx

  </details>

- **On the Root of Trust Identification Problem**
  2020-10-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.13858)
  Ivan De Oliveira Nunes, Xuhua Ding, Gene Tsudik

  <details><summary>摘要 / Abstract</summary>

  Root of Trust Identification (RTI) refers to determining whether a given security service or task is being performed by the particular root of trust (e.g., a TEE) within a specific physical device. Despite its importance, this problem has been mostly overlooked. We formalize the RTI problem and argue that security of RTI protocols is especially challenging due to local adversaries, cuckoo adversaries, and the combination thereof. To cope with this problem we propose a simple and effective protocol based on biometrics. Unlike biometric-based user authentication, our approach is not concerned with verifying user identity, and requires neither pre-enrollment nor persistent storage for biometric templates. Instead, it takes advantage of the difficulty of cloning a biometric in real-time to securely identify the root of trust of a given physical device, by using the biometric as a challenge. Security of the proposed protocol is analyzed in the combined Local and Cuckoo adversarial model. Also, a prototype implementation is used to demonstrate the protocol&#x27;s feasibility and practicality. We further propose a Proxy RTI protocol, wherein a previously identified RoT assists a remote verifier in identifying new RoTs.

  匹配依据：TEE: tee (context)

  </details>

- **Performance Analysis of Scientific Computing Workloads on Trusted Execution Environments**
  2020-10-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.13216)
  Ayaz Akram, Anna Giannakou, Venkatesh Akella, Jason Lowe-Power, Sean Peisert

  <details><summary>摘要 / Abstract</summary>

  Scientific computing sometimes involves computation on sensitive data. Depending on the data and the execution environment, the HPC (high-performance computing) user or data provider may require confidentiality and/or integrity guarantees. To study the applicability of hardware-based trusted execution environments (TEEs) to enable secure scientific computing, we deeply analyze the performance impact of AMD SEV and Intel SGX for diverse HPC benchmarks including traditional scientific computing, machine learning, graph analytics, and emerging scientific computing workloads. We observe three main findings: 1) SEV requires careful memory placement on large scale NUMA machines (1$\times$$-$3.4$\times$ slowdown without and 1$\times$$-$1.15$\times$ slowdown with NUMA aware placement), 2) virtualization$-$a prerequisite for SEV$-$results in performance degradation for workloads with irregular memory accesses and large working sets (1$\times$$-$4$\times$ slowdown compared to native execution for graph applications) and 3) SGX is inappropriate for HPC given its limited secure memory size and inflexible programming model (1.2$\times$$-$126$\times$ slowdown over unsecure execution). Finally, we discuss forthcoming new TEE designs and their potential impact on scientific computing.

  匹配依据：TEE: amd sev, intel sgx, sgx, trusted execution environments

  </details>

- **Towards Efficiently Establishing Mutual Distrust Between Host Application and Enclave for SGX**
  2020-10-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.12400)
  Yuan Chen, Jiaqi Li, Guorui Xu, Yajin Zhou, Zhi Wang, Cong Wang, Kui Ren

  <details><summary>摘要 / Abstract</summary>

  Since its debut, SGX has been used in many applications, e.g., secure data processing. However, previous systems usually assume a trusted enclave and ignore the security issues caused by an untrusted enclave. For instance, a vulnerable (or even malicious) third-party enclave can be exploited to attack the host application and the rest of the system. In this paper, we propose an efficient mechanism to confine an untrusted enclave&#x27;s behaviors. The threats of an untrusted enclave come from the enclave-host asymmetries. They can be abused to access arbitrary memory regions of its host application, jump to any code location after leaving the enclave and forge the stack register to manipulate the saved context. Our solution breaks such asymmetries and establishes mutual distrust between the host application and the enclave. It leverages Intel MPK for efficient memory isolation and the x86 single-step debugging mechanism to capture the event when an enclave is existing. It then performs the integrity check for the jump target and the stack pointer. We have solved two practical challenges and implemented a prototype system. The evaluation with multiple micro-benchmarks and representative real-world applications demonstrated the efficiency of our system, with less than 4% performance overhead.

  匹配依据：TEE: sgx, trusted enclave

  </details>

- **DuetSGX: Differential Privacy with Secure Hardware**
  2020-10-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.10664)
  Phillip Nguyen, Alex Silence, David Darais, Joseph P. Near

  <details><summary>摘要 / Abstract</summary>

  Differential privacy offers a formal privacy guarantee for individuals, but many deployments of differentially private systems require a trusted third party (the data curator). We propose DuetSGX, a system that uses secure hardware (Intel&#x27;s SGX) to eliminate the need for a trusted data curator. Data owners submit encrypted data that can be decrypted only within a secure enclave running the DuetSGX system, ensuring that sensitive data is never available to the data curator. Analysts submit queries written in the Duet language, which is specifically designed for verifying that programs satisfy differential privacy; DuetSGX uses the Duet typechecker to verify that each query satisfies differential privacy before running it. DuetSGX therefore provides the benefits of local differential privacy and central differential privacy simultaneously: noise is only added to final results, and there is no trusted third party. We have implemented a proof-of-concept implementation of DuetSGX and we release it as open-source.

  匹配依据：TEE: secure enclave, sgx

  </details>

- **GOAT: GPU Outsourcing of Deep Learning Training With Asynchronous Probabilistic Integrity Verification Inside Trusted Execution Environment**
  2020-10-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.08855)
  Aref Asvadishirehjini, Murat Kantarcioglu, Bradley Malin

  <details><summary>摘要 / Abstract</summary>

  Machine learning models based on Deep Neural Networks (DNNs) are increasingly deployed in a wide range of applications ranging from self-driving cars to COVID-19 treatment discovery. To support the computational power necessary to learn a DNN, cloud environments with dedicated hardware support have emerged as critical infrastructure. However, there are many integrity challenges associated with outsourcing computation. Various approaches have been developed to address these challenges, building on trusted execution environments (TEE). Yet, no existing approach scales up to support realistic integrity-preserving DNN model training for heavy workloads (deep architectures and millions of training examples) without sustaining a significant performance hit. To mitigate the time gap between pure TEE (full integrity) and pure GPU (no integrity), we combine random verification of selected computation steps with systematic adjustments of DNN hyper-parameters (e.g., a narrow gradient clipping range), hence limiting the attacker&#x27;s ability to shift the model parameters significantly provided that the step is not selected for verification during its training phase. Experimental results show the new approach achieves 2X to 20X performance improvement over pure TEE based solution while guaranteeing a very high probability of integrity (e.g., 0.999) with respect to state-of-the-art DNN backdoor attacks.

  匹配依据：TEE: trusted execution environment, trusted execution environments

  </details>

- **Elasticlave: An Efficient Memory Model for Enclaves**
  2020-10-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.08440)
  Zhijingcheng Yu, Shweta Shinde, Trevor E. Carlson, Prateek Saxena

  <details><summary>摘要 / Abstract</summary>

  Trusted-execution environments (TEE), like Intel SGX, isolate user-space applications into secure enclaves without trusting the OS. Thus, TEEs reduce the trusted computing base, but add one to two orders of magnitude slow-down. The performance cost stems from a strict memory model, which we call the spatial isolation model, where enclaves cannot share memory regions with each other. In this work, we present Elasticlave---a new TEE memory model that allows enclaves to selectively and temporarily share memory with other enclaves and the OS. Elasticlave eliminates the need for expensive data copy operations, while offering the same level of application-desired security as possible with the spatial model. We prototype Elasticlave design on an RTL-designed cycle-level RISC-V core and observe 1 to 2 orders of magnitude performance improvements over the spatial model implemented with the same processor configuration. Elasticlave has a small TCB. We find that its performance characteristics and hardware area footprint scale well with the number of shared memory regions it is configured to support.

  匹配依据：TEE: intel sgx, secure enclaves, trusted execution environments

  </details>

- **Secure and Fault Tolerant Decentralized Learning**
  2020-10-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.07541)
  Saurav Prakash, Hanieh Hashemi, Yongqin Wang, Murali Annavaram, Salman Avestimehr

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) is a promising paradigm for training a global model over data distributed across multiple data owners without centralizing clients&#x27; raw data. However, sharing of local model updates can also reveal information of clients&#x27; local datasets. Trusted execution environments (TEEs) within the FL server have been recently deployed by companies like Meta for secure aggregation. However, secure aggregation can suffer from error-prone local updates sent by clients that become faulty during training due to underlying device malfunctions. Also, data heterogeneity across clients makes fault mitigation challenging, as even updates from normal clients are dissimilar. Thus, most of the prior fault tolerant methods, which treat any local update differing from the majority of other updates as faulty, perform poorly. We propose DiverseFL to make model aggregation secure as well as robust to faults. In DiverseFL, any client whose local model update diverges from its associated guiding update is tagged as being faulty. To implement our novel per-client criteria for fault mitigation, DiverseFL creates a TEE-based secure enclave within the FL server, which in addition to performing secure aggregation for carrying out the global model update step, securely receives a small representative sample of local data from each client only once before training, and computes guiding updates for each participating client during training. Thus, DiverseFL provides security against privacy leakage as well as robustness against faulty clients. In experiments, DiverseFL consistently achieves significant improvements in absolute test accuracy over prior fault mitigation benchmarks. DiverseFL also performs closely to OracleSGD, where server combines updates only from the normal clients. We also analyze the convergence rate of DiverseFL under non-IID data and standard convexity assumptions.

  匹配依据：TEE: secure enclave, trusted execution environments

  </details>

- **Exploiting Interfaces of Secure Encrypted Virtual Machines**
  2020-10-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.07094)
  Martin Radev, Mathias Morbitzer

  <details><summary>摘要 / Abstract</summary>

  Cloud computing is a convenient model for processing data remotely. However, users must trust their cloud provider with the confidentiality and integrity of the stored and processed data. To increase the protection of virtual machines, AMD introduced SEV, a hardware feature which aims to protect code and data in a virtual machine. This allows to store and process sensitive data in cloud environments without the need to trust the cloud provider or the underlying software. However, the virtual machine still depends on the hypervisor for performing certain activities, such as the emulation of special CPU instructions, or the emulation of devices. Yet, most code that runs in virtual machines was not written with an attacker model which considers the hypervisor as malicious. In this work, we introduce a new class of attacks in which a malicious hypervisor manipulates external interfaces of an SEV or SEV-ES virtual machine to make it act against its own interests. We start by showing how we can make use of virtual devices to extract encryption keys and secret data of a virtual machine. We then show how we can reduce the entropy of probabilistic kernel defenses in the virtual machine by carefully manipulating the results of the CPUID and RDTSC instructions. We continue by showing an approach for secret data exfiltration and code injection based on the forgery of MMIO regions over the VM&#x27;s address space. Finally, we show another attack which forces decryption of the VM&#x27;s stack and uses Return Oriented Programming to execute arbitrary code inside the VM. While our approach is also applicable to traditional virtualization environments, its severity significantly increases with the attacker model of SEV-ES, which aims to protect a virtual machine from a benign but vulnerable hypervisor.

  匹配依据：TEE: sev (context)

  </details>

- **S3ML: A Secure Serving System for Machine Learning Inference**
  2020-10-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.06212)
  Junming Ma, Chaofan Yu, Aihui Zhou, Bingzhe Wu, Xibin Wu, Xingyu Chen, Xiangqun Chen, Lei Wang, Donggang Cao

  <details><summary>摘要 / Abstract</summary>

  We present S3ML, a secure serving system for machine learning inference in this paper. S3ML runs machine learning models in Intel SGX enclaves to protect users&#x27; privacy. S3ML designs a secure key management service to construct flexible privacy-preserving server clusters and proposes novel SGX-aware load balancing and scaling methods to satisfy users&#x27; Service-Level Objectives. We have implemented S3ML based on Kubernetes as a low-overhead, high-available, and scalable system. We demonstrate the system performance and effectiveness of S3ML through extensive experiments on a series of widely-used models.

  匹配依据：TEE: intel sgx, sgx, sgx enclaves

  </details>

- **Verifiable Functional Encryption using Intel SGX**
  2020-10-06 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1221)
  Tatsuya Suzuki, Keita Emura, Toshihiro Ohigashi, Kazumasa Omote

  <details><summary>摘要 / Abstract</summary>

  Most functional encryption schemes implicitly assume that inputs to decryption algorithms, i.e., secret keys and ciphertexts, are generated honestly. However, they may be tampered by malicious adversaries. Thus, verifiable functional encryption (VFE) was proposed by Badrinarayanan et al. in ASIACRYPT 2016 where anyone can publicly check the validity of secret keys and ciphertexts. They employed indistinguishability-based (IND-based) security due to an impossibility result of simulation-based (SIM-based) VFE even though SIM-based security is more desirable. In this paper, we propose a SIM-based VFE scheme. To bypass the impossibility result, we introduce a trusted setup assumption. Although it appears to be a strong assumption, we demonstrate that it is reasonable in a hardware-based construction, e.g., Fisch et al. in ACM CCS 2017. Our construction is based on a verifiable public-key encryption scheme (Nieto et al. in SCN 2012), a signature scheme, and a secure hardware scheme, which we refer to as VFE-HW. Finally, we discuss an our implementation of VFE-HW using Intel Software Guard Extensions (Intel SGX).

  匹配依据：TEE: intel sgx

  </details>

- **Secure Collaborative Training and Inference for XGBoost**
  2020-10-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.02524)
  Andrew Law, Chester Leung, Rishabh Poddar, Raluca Ada Popa, Chenyu Shi, Octavian Sima, Chaofan Yu, Xingmeng Zhang, Wenting Zheng

  <details><summary>摘要 / Abstract</summary>

  In recent years, gradient boosted decision tree learning has proven to be an effective method of training robust models. Moreover, collaborative learning among multiple parties has the potential to greatly benefit all parties involved, but organizations have also encountered obstacles in sharing sensitive data due to business, regulatory, and liability concerns. We propose Secure XGBoost, a privacy-preserving system that enables multiparty training and inference of XGBoost models. Secure XGBoost protects the privacy of each party&#x27;s data as well as the integrity of the computation with the help of hardware enclaves. Crucially, Secure XGBoost augments the security of the enclaves using novel data-oblivious algorithms that prevent access side-channel attacks on enclaves induced via access pattern leakage.

  匹配依据：TEE: hardware enclaves

  </details>

- **Timing Cache Accesses to Eliminate Side Channels in Shared Software**
  2020-09-30 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.14732)
  Divya Ojha, Sandhya Dwarkadas

  <details><summary>摘要 / Abstract</summary>

  Timing side channels have been used to extract cryptographic keys and sensitive documents, even from trusted enclaves. In this paper, we focus on cache side channels created by access to shared code or data in the memory hierarchy. This vulnerability is exploited by several known attacks, e.g, evict+reload for recovering an RSA key and Spectre variants for data leaked due to speculative accesses. The key insight in this paper is the importance of the first access to the shared data after a victim brings the data into the cache. To eliminate the timing side channel, we ensure that the first access by a process to any cache line loaded by another process results in a miss. We accomplish this goal by using a combination of timestamps and a novel hardware design to allow efficient parallel comparisons of the timestamps. The solution works at all the cache levels and defends against an attacker process running on another core, same core, or another hyperthread. Our design retains the benefits of a shared cache: allowing processes to utilize the entire cache for their execution and retaining a single copy of shared code and data (data deduplication). Our implementation in the GEM5 simulator demonstrates that the system is able to defend against RSA key extraction. We evaluate performance using SPECCPU2006 and observe overhead due to first access delay to be 2.17%. The overhead due to the security context bookkeeping is of the order of 0.3%.

  匹配依据：TEE: trusted enclaves

  </details>

- **Bypassing Isolated Execution on RISC-V with Fault Injection**
  2020-09-30 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1193)
  Shoei Nashimoto, Daisuke Suzuki, Rei Ueno, Naofumi Homma

  <details><summary>摘要 / Abstract</summary>

  RISC-V is equipped with physical memory protection (PMP) to prevent malicious software from accessing protected memory regions. One of the main objectives of PMP is to provide a trusted execution environment (TEE) that isolates secure and insecure applications. In this study, we propose a fault injection attack to bypass the isolation based on PMP. The proposed attack scheme involves extracting successful glitch parameters for fault injection under the assumption of a black-box environment. We implement a proof-of-concept TEE compatible with PMP in RISC-V, and we verify the feasibility and effectiveness of the proposed attack through some experiments conducted in the TEE. The results show that an attacker can bypass the isolation of the TEE and read data from the protected memory region.

  匹配依据：TEE: trusted execution environment

  </details>

- **Oblivious Sampling Algorithms for Private Data Analysis**
  2020-09-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.13689)
  Sajin Sasy, Olga Ohrimenko

  <details><summary>摘要 / Abstract</summary>

  We study secure and privacy-preserving data analysis based on queries executed on samples from a dataset. Trusted execution environments (TEEs) can be used to protect the content of the data during query computation, while supporting differential-private (DP) queries in TEEs provides record privacy when query output is revealed. Support for sample-based queries is attractive due to \emph{privacy amplification} since not all dataset is used to answer a query but only a small subset. However, extracting data samples with TEEs while proving strong DP guarantees is not trivial as secrecy of sample indices has to be preserved. To this end, we design efficient secure variants of common sampling algorithms. Experimentally we show that accuracy of models trained with shuffling and sampling is the same for differentially private models for MNIST and CIFAR-10, while sampling provides stronger privacy guarantees than shuffling.

  匹配依据：TEE: trusted execution environments

  </details>

- **Secure Internal Communication of a Trustzone-Enabled Heterogeneous Soc Lightweight Encryption**
  2020-09-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.06896)
  El Mehdi Benhani, Cuauhtemoc Mancillas Lopez, Lilian Bossuet

  <details><summary>摘要 / Abstract</summary>

  Security in TrustZone-enabled heterogeneous system-on-chip (SoC) is gaining increasing attention for several years. Mainly because this type of SoC can be found in more and more applications in servers or in the cloud. The inside-SoC communication layer is one of the main element of heterogeneous SoC; indeed all the data goes through it. Monitoring and controlling inside-SoC communications enables to fend off attacks before system corruption. In this article, we study the feasibility of encrypted data exchange between the secure software executed in a trusted execution environment (TEE) and the secure logic part of an heterogeneous SoC. Experiment are done with a Xilinx Zynq-7010 SoC and two lightweight stream ciphers. We show that using lightweight stream ciphers is an efficient solution without excessive overheads.

  匹配依据：TEE: trusted execution environment, trustzone

  </details>

- **Light Can Hack Your Face! Black-box Backdoor Attack on Face Recognition Systems**
  2020-09-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.06996)
  Haoliang Li, Yufei Wang, Xiaofei Xie, Yang Liu, Shiqi Wang, Renjie Wan, Lap-Pui Chau, Alex C. Kot

  <details><summary>摘要 / Abstract</summary>

  Deep neural networks (DNN) have shown great success in many computer vision applications. However, they are also known to be susceptible to backdoor attacks. When conducting backdoor attacks, most of the existing approaches assume that the targeted DNN is always available, and an attacker can always inject a specific pattern to the training data to further fine-tune the DNN model. However, in practice, such attack may not be feasible as the DNN model is encrypted and only available to the secure enclave. In this paper, we propose a novel black-box backdoor attack technique on face recognition systems, which can be conducted without the knowledge of the targeted DNN model. To be specific, we propose a backdoor attack with a novel color stripe pattern trigger, which can be generated by modulating LED in a specialized waveform. We also use an evolutionary computing strategy to optimize the waveform for backdoor attack. Our backdoor attack can be conducted in a very mild condition: 1) the adversary cannot manipulate the input in an unnatural way (e.g., injecting adversarial noise); 2) the adversary cannot access the training database; 3) the adversary has no knowledge of the training model as well as the training set used by the victim party. We show that the backdoor trigger can be quite effective, where the attack success rate can be up to $88\%$ based on our simulation study and up to $40\%$ based on our physical-domain study by considering the task of face recognition and verification based on at most three-time attempts during authentication. Finally, we evaluate several state-of-the-art potential defenses towards backdoor attacks, and find that our attack can still be effective. We highlight that our study revealed a new physical backdoor attack, which calls for the attention of the security issue of the existing face recognition/verification techniques.

  匹配依据：TEE: secure enclave

  </details>

- **Simplex: Repurposing Intel Memory Protection Extensions for Information Hiding**
  2020-09-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.06490)
  Matthew Cole, Aravind Prakash

  <details><summary>摘要 / Abstract</summary>

  With the rapid increase in software exploits, the last few decades have seen several hardware-level features to enhance security (e.g., Intel MPX, ARM TrustZone, Intel SGX, Intel CET). Due to security, performance and/or usability issues these features have attracted steady criticism. One such feature is the Intel Memory Protection Extensions (MPX), an instruction set architecture extension promising spatial memory safety at a lower performance cost due to hardware-accelerated bounds checking. However, recent investigations into MPX have found that is neither as performant, accurate, nor precise as cutting-edge software-based spatial memory safety. As a direct consequence, compiler and operating system support for MPX is dying, and Intel has begun to manufacture desktop CPUs without MPX. Nonetheless, given how ubiquitous MPX is, it provides an excellent yet under-utilized hardware resource that can be aptly salvaged for security purposes. In this paper, we propose Simplex, a library framework that re-purposes MPX registers as general purpose registers. Using Simplex, we demonstrate how MPX registers can be used to store sensitive information (e.g., encryption keys) directly on the hardware. We evaluate Simplex for performance and find that its overhead is small enough to permit its deployment in all but the most performance-intensive code. We refactored the string.h buffer manipulation functions and found a geometric mean 0.9% performance overhead. We also modified the deepsjeng and lbm SPEC CPU2017 benchmarks to use Simplex and found a 1% and 0.98% performance overhead respectively. Finally, we investigate the behavior of the MPX context with regards to multi-process and multi-thread programs.

  匹配依据：TEE: intel sgx, trustzone

  </details>

- **HECTOR-V: A Heterogeneous CPU Architecture for a Secure RISC-V Execution Environment**
  2020-09-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.05262)
  Pascal Nasahl, Robert Schilling, Mario Werner, Stefan Mangard

  <details><summary>摘要 / Abstract</summary>

  To ensure secure and trustworthy execution of applications, vendors frequently embed trusted execution environments into their systems. Here, applications are protected from adversaries, including a malicious operating system. TEEs are usually built by integrating protection mechanisms directly into the processor or by using dedicated external secure elements. However, both of these approaches only cover a narrow threat model resulting in limited security guarantees. Enclaves in the application processor typically provide weak isolation between the secure and non-secure domain, especially when considering side-channel attacks. Although secure elements do provide strong isolation, the slow communication interface to the application processor is exposed to adversaries and restricts the use cases. Independently of the used implementation approach, TEEs often lack the possibility to establish secure communication to external peripherals, and most operating systems executed inside TEEs do not provide state-of-the-art defense strategies, making them vulnerable against various attacks. We argue that TEEs implemented on the main application processor are insecure, especially when considering side-channel attacks. We demonstrate how a heterogeneous architecture can be utilized to realize a secure TEE design. We directly embed a processor into our architecture to provide strong isolation between the secure and non-secure domain. The tight coupling of TEE and REE enables HECTOR-V to provide mechanisms for establishing secure communication channels. We further introduce RISC-V Secure Co-Processor, a security-hardened processor tailored for TEEs. To secure applications executed inside the TEE, RVSCP provides control-flow integrity, rigorously restricts I/O accesses to certain execution states, and provides operating system services directly in hardware.

  匹配依据：TEE: trusted execution environments

  </details>

- **Privacy-Preserving Machine Learning in Untrusted Clouds Made Simple**
  2020-09-09 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.04390)
  Dayeol Lee, Dmitrii Kuvaiskii, Anjo Vahldiek-Oberwagner, Mona Vij

  <details><summary>摘要 / Abstract</summary>

  We present a practical framework to deploy privacy-preserving machine learning (PPML) applications in untrusted clouds based on a trusted execution environment (TEE). Specifically, we shield unmodified PyTorch ML applications by running them in Intel SGX enclaves with encrypted model parameters and encrypted input data to protect the confidentiality and integrity of these secrets at rest and during runtime. We use the open-source Graphene library OS with transparent file encryption and SGX-based remote attestation to minimize porting effort and seamlessly provide file protection and attestation. Our approach is completely transparent to the machine learning application: the developer and the end-user do not need to modify the ML application in any way.

  匹配依据：TEE: intel sgx, sgx, sgx enclaves, trusted execution environment

  </details>

- **Enclave-Aware Compartmentalization and Secure Sharing with Sirius**
  2020-09-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.01869)
  Zahra Tarkhani, Anil Madhavapeddy

  <details><summary>摘要 / Abstract</summary>

  Hardware-assisted trusted execution environments (TEEs) are critical building blocks of many modern applications. However, they have a one-way isolation model that introduces a semantic gap between a TEE and its outside world. This lack of information causes an ever-increasing set of attacks on TEE-enabled applications that exploit various insecure interactions with the host OSs, applications, or other enclaves. We introduce Sirius, the first compartmentalization framework that achieves strong isolation and secure sharing in TEE-assisted applications by controlling the dataflows within primary kernel objects (e.g. threads, processes, address spaces, files, sockets, pipes) in both the secure and normal worlds. Sirius replaces ad-hoc interactions in current TEE systems with a principled approach that adds strong inter- and intra-address space isolation and effectively eliminates a wide range of attacks. We evaluate Sirius on ARM platforms and find that it is lightweight ($\approx 15K$ LoC) and only adds $\approx 10.8\%$ overhead to enable TEE support on applications such as httpd, and improves the performance of existing TEE-enabled applications such as the Darknet ML framework and ARM&#x27;s LibDDSSec by $0.05\%-5.6\%$.

  匹配依据：TEE: trusted execution environments

  </details>

- **Binary Compatibility For SGX Enclaves**
  2020-09-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.01144)
  Shweta Shinde, Jinhua Cui, Satyaki Sen, Pinghai Yuan, Prateek Saxena

  <details><summary>摘要 / Abstract</summary>

  Enclaves, such as those enabled by Intel SGX, offer a powerful hardware isolation primitive for application partitioning. To become universally usable on future commodity OSes, enclave designs should offer compatibility with existing software. In this paper, we draw attention to 5 design decisions in SGX that create incompatibility with existing software. These represent concrete starting points, we hope, for improvements in future TEEs. Further, while many prior works have offered partial forms of compatibility, we present the first attempt to offer binary compatibility with existing software on SGX. We present Ratel, a system that enables a dynamic binary translation engine inside SGX enclaves on Linux. Through the lens of Ratel, we expose the fundamental trade-offs between performance and complete mediation on the OS-enclave interface, which are rooted in the aforementioned 5 SGX design restrictions. We report on an extensive evaluation of Ratel on over 200 programs, including micro-benchmarks and real applications such as Linux utilities.

  匹配依据：TEE: intel sgx, sgx, sgx enclaves

  </details>

- **Attacking Threshold Wallets**
  2020-09-01 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1052)
  Jean-Philippe Aumasson, Omer Shlomovits

  <details><summary>摘要 / Abstract</summary>

  Threshold wallets leverage threshold signature schemes (TSS) to distribute signing rights across multiple parties when issuing blockchain transactions. These provide greater assurance against insider fraud, and are sometimes seen as an alternative to methods using a trusted execution environment to issue the signature. This new class of applications motivated researchers to discover better protocols, entrepreneurs to create start-up companies, and large organizations to deploy TSS-based solutions. For example, the leading cryptocurrency exchange (in transaction volume) adopted TSS to protect some of its wallets. Although the TSS concept is not new, this is the first time that so many TSS implementations are written and deployed in such a critical context, where all liquidity reserves could be lost in a minute if the crypto fails. Furthermore, TSS schemes are sometimes extended or tweaked to best adapt to their target use case---what could go wrong? This paper, based on the authors&#x27; experience with building and analyzing TSS technology, describes three different attacks on TSS implementations used by leading organizations. Unlike security analyses of on-paper protocols, this work targets TSS as deployed in real applications, and exploits logical vulnerabilities enabled by the extra layers of complexity added by TSS software. The attacks have concrete applications, and could for example have been exploited to empty an organization&#x27;s cold wallet (typically worth at least an 8-digit dollar figure). Indeed, one of our targets is the cold wallet system of the biggest cryptocurrency exchange (which has been fixed after our disclosure).

  匹配依据：TEE: trusted execution environment

  </details>

- **TZ4Fabric: Executing Smart Contracts with ARM TrustZone**
  2020-08-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.11601)
  Christina Müller, Marcus Brandenburger, Christian Cachin, Pascal Felber, Christian Göttel, Valerio Schiavoni

  <details><summary>摘要 / Abstract</summary>

  Blockchain technology promises to revolutionize manufacturing industries. For example, several supply-chain use-cases may benefit from transparent asset tracking and automated processes using smart contracts. Several real-world deployments exist where the transparency aspect of a blockchain is both an advantage and a disadvantage at the same time. The exposure of assets and business interaction represent critical risks. However, there are typically no confidentiality guarantees to protect the smart contract logic as well as the processed data. Trusted execution environments (TEE) are an emerging technology available in both edge or mobile-grade processors (e.g., Arm TrustZone) and server-grade processors (e.g., Intel SGX). TEEs shield both code and data from malicious attackers. This practical experience report presents TZ4Fabric, an extension of Hyperledger Fabric to leverage Arm TrustZone for the secure execution of smart contracts. Our design minimizes the trusted computing base executed by avoiding the execution of a whole Hyperledger Fabric node inside the TEE, which continues to run in untrusted environment. Instead, we restrict it to the execution of only the smart contract. The TZ4Fabric prototype exploits the open-source OP-TEE framework, as it supports deployments on cheap low-end devices (e.g., Raspberry Pis). Our experimental results highlight the performance trade-off due to the additional security guarantees provided by Arm TrustZone. TZ4Fabric will be released as open-source.

  匹配依据：TEE: intel sgx, trusted execution environments, trustzone

  </details>

- **Attribute-Based Symmetric Searchable Encryption**
  2020-08-18 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/999)
  Hai-Van Dang, Amjad Ullah, Alexandros Bakas, Antonis Michalas

  <details><summary>摘要 / Abstract</summary>

  Symmetric Searchable Encryption (SSE) is an encryption technique that allows users to search directly on their outsourced encrypted data while preserving the privacy of both the files and the queries. Unfortunately, majority of the SSE schemes allows users to either decrypt the whole ciphertext or nothing at all. In this paper, we propose a novel scheme based on traditional symmetric primitives, that allows data owners to bind parts of their ciphertexts with specific policies. Inspired by the concept of Attribute-Based Encryption (ABE) in the public setting, we design a scheme through which users can recover only certain parts of an encrypted document if and only if they retain a set of attributes that satisfy a policy. Our construction satisfies the important notion of forward privacy while at the same time supports the multi-client model by leveraging SGX functionality for the synchronization of users. To prove the correctness of our approach, we provide a detailed simulation-based security analysis coupled with an extensive experimental evaluation that shows the effectiveness of our scheme.

  匹配依据：TEE: sgx

  </details>

- **Trustworthy AI Inference Systems: An Industry Research View**
  2020-08-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.04449)
  Rosario Cammarota, Matthias Schunter, Anand Rajan, Fabian Boemer, Ágnes Kiss, Amos Treiber, Christian Weinert, Thomas Schneider, Emmanuel Stapf, Ahmad-Reza Sadeghi, Daniel Demmler, Joshua Stock, Huili Chen, Siam Umar Hussain, Sadegh Riazi, Farinaz Koushanfar, Saransh Gupta, Tajan Simunic Rosing, Kamalika Chaudhuri, Hamid Nejatollahi, Nikil Dutt, Mohsen Imani, Kim Laine, Anuj Dubey, Aydin Aysu, Fateme Sadat Hosseini, Chengmo Yang, Eric Wallace, Pamela Norton

  <details><summary>摘要 / Abstract</summary>

  In this work, we provide an industry research view for approaching the design, deployment, and operation of trustworthy Artificial Intelligence (AI) inference systems. Such systems provide customers with timely, informed, and customized inferences to aid their decision, while at the same time utilizing appropriate security protection mechanisms for AI models. Additionally, such systems should also use Privacy-Enhancing Technologies (PETs) to protect customers&#x27; data at any time. To approach the subject, we start by introducing current trends in AI inference systems. We continue by elaborating on the relationship between Intellectual Property (IP) and private data protection in such systems. Regarding the protection mechanisms, we survey the security and privacy building blocks instrumental in designing, building, deploying, and operating private AI inference systems. For example, we highlight opportunities and challenges in AI systems using trusted execution environments combined with more recent advances in cryptographic techniques to protect data in use. Finally, we outline areas of further development that require the global collective attention of industry, academia, and government researchers to sustain the operation of trustworthy AI inference systems.

  匹配依据：TEE: trusted execution environments

  </details>

- **Secure IoT Data Analytics in Cloud via Intel SGX**
  2020-08-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.05286)
  Md Shihabul Islam, Mustafa Safa Ozdayi, Latifur Khan, Murat Kantarcioglu

  <details><summary>摘要 / Abstract</summary>

  The growing adoption of IoT devices in our daily life is engendering a data deluge, mostly private information that needs careful maintenance and secure storage system to ensure data integrity and protection. Also, the prodigious IoT ecosystem has provided users with opportunities to automate systems by interconnecting their devices and other services with rule-based programs. The cloud services that are used to store and process sensitive IoT data turn out to be vulnerable to outside threats. Hence, sensitive IoT data and rule-based programs need to be protected against cyberattacks. To address this important challenge, in this paper, we propose a framework to maintain confidentiality and integrity of IoT data and rule-based program execution. We design the framework to preserve data privacy utilizing Trusted Execution Environment (TEE) such as Intel SGX, and end-to-end data encryption mechanism. We evaluate the framework by executing rule-based programs in the SGX securely with both simulated and real IoT device data.

  匹配依据：TEE: intel sgx, sgx, trusted execution environment

  </details>

- **Data Oblivious Algorithms for Multicores**
  2020-08-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.00332) · [IACR ePrint](https://eprint.iacr.org/2020/947)
  Vijaya Ramachandran, Elaine Shi

  <details><summary>摘要 / Abstract</summary>

  As secure processors such as Intel SGX (with hyperthreading) become widely adopted, there is a growing appetite for private analytics on big data. Most prior works on data-oblivious algorithms adopt the classical PRAM model to capture parallelism. However, it is widely understood that PRAM does not best capture realistic multicore processors, nor does it reflect parallel programming models adopted in practice. In this paper, we initiate the study of parallel data oblivious algorithms on realistic multicores, best captured by the binary fork-join model of computation. We first show that data-oblivious sorting can be accomplished by a binary fork-join algorithm with optimal total work and optimal (cache-oblivious) cache complexity, and in O(log n log log n) span (i.e., parallel time) that matches the best-known insecure algorithm. Using our sorting algorithm as a core primitive, we show how to data-obliviously simulate general PRAM algorithms in the binary fork-join model with non-trivial efficiency. We also present results for several applications including list ranking, Euler tour, tree contraction, connected components, and minimum spanning forest. For a subset of these applications, our data-oblivious algorithms asymptotically outperform the best known insecure algorithms. For other applications, we show data oblivious algorithms whose performance bounds match the best known insecure algorithms. Complementing these asymptotically efficient results, we present a practical variant of our sorting algorithm that is self-contained and potentially implementable. It has optimal caching cost, and it is only a log log n factor off from optimal work and about a log n factor off in terms of span; moreover, it achieves small constant factors in its bounds.

  匹配依据：TEE: intel sgx

  </details>

- **MQT-TZ: Hardening IoT Brokers Using ARM TrustZone**
  2020-07-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.12442)
  Carlos Segarra, Ricard Delgado-Gonzalo, Valerio Schiavoni

  <details><summary>摘要 / Abstract</summary>

  The publish-subscribe paradigm is an efficient communication scheme with strong decoupling between the nodes, that is especially fit for large-scale deployments. It adapts natively to very dynamic settings and it is used in a diversity of real-world scenarios, including finance, smart cities, medical environments, or IoT sensors. Several of the mentioned application scenarios require increasingly stringent security guarantees due to the sensitive nature of the exchanged messages as well as the privacy demands of the clients/stakeholders/receivers. MQTT is a lightweight topic-based publish-subscribe protocol popular in edge and IoT settings, a de-facto standard widely adopted nowadays by the industry and researchers. However, MQTT brokers must process data in clear, hence exposing a large attack surface. This paper presents MQT-TZ, a secure MQTT broker leveraging Arm TrustZone, a trusted execution environment (TEE) commonly found even on inexpensive devices largely available on the market (such as Raspberry Pi units). We define a mutual TLS-based handshake and a two-layer encryption for end-to-end security using the TEE as a trusted proxy. The experimental evaluation of our fully implemented prototype with micro-, macro-benchmarks, as well as with real-world industrial workloads from a MedTech use-case, highlights several trade-offs using TrustZone TEE. We report several lessons learned while building and evaluating our system. We release MQT-TZ as open-source.

  匹配依据：TEE: trusted execution environment, trustzone

  </details>

- **Confidential Attestation: Efficient in-Enclave Verification of Privacy Policy Compliance**
  2020-07-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.10513)
  Weijie Liu, Wenhao Wang, Xiaofeng Wang, Xiaozhu Meng, Yaosong Lu, Hongbo Chen, Xinyu Wang, Qingtao Shen, Kai Chen, Haixu Tang, Yi Chen, Luyi Xing

  <details><summary>摘要 / Abstract</summary>

  A trusted execution environment (TEE) such as Intel Software Guard Extension (SGX) runs a remote attestation to prove to a data owner the integrity of the initial state of an enclave, including the program to operate on her data. For this purpose, the data-processing program is supposed to be open to the owner, so its functionality can be evaluated before trust can be established. However, increasingly there are application scenarios in which the program itself needs to be protected. So its compliance with privacy policies as expected by the data owner should be verified without exposing its code. To this end, this paper presents CAT, a new model for TEE-based confidential attestation. Our model is inspired by Proof-Carrying Code, where a code generator produces proof together with the code and a code consumer verifies the proof against the code on its compliance with security policies. Given that the conventional solutions do not work well under the resource-limited and TCB-frugal TEE, we propose a new design that allows an untrusted out-enclave generator to analyze the source code of a program when compiling it into binary and a trusted in-enclave consumer efficiently verifies the correctness of the instrumentation and the presence of other protection before running the binary. Our design strategically moves most of the workload to the code generator, which is responsible for producing well-formatted and easy-to-check code, while keeping the consumer simple. Also, the whole consumer can be made public and verified through a conventional attestation. We implemented this model on Intel SGX and demonstrate that it introduces a very small part of TCB. We also thoroughly evaluated its performance on micro- and macro- benchmarks and real-world applications, showing that the new design only incurs a small overhead when enforcing several categories of security policies.

  匹配依据：TEE: intel sgx, sgx, trusted execution environment

  </details>

- **CACTI: Captcha Avoidance via Client-side TEE Integration**
  2020-07-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.10397)
  Yoshimichi Nakatsuka, Ercan Ozturk, Andrew Paverd, Gene Tsudik

  <details><summary>摘要 / Abstract</summary>

  Preventing abuse of web services by bots is an increasingly important problem, as abusive activities grow in both volume and variety. CAPTCHAs are the most common way for thwarting bot activities. However, they are often ineffective against bots and frustrating for humans. In addition, some recent CAPTCHA techniques diminish user privacy. Meanwhile, client-side Trusted Execution Environments (TEEs) are becoming increasingly widespread (notably, ARM TrustZone and Intel SGX), allowing establishment of trust in a small part (trust anchor or TCB) of client-side hardware. This prompts the question: can a TEE help reduce (or remove entirely) user burden of solving CAPTCHAs? In this paper, we design CACTI: CAPTCHA Avoidance via Client-side TEE Integration. Using client-side TEEs, CACTI allows legitimate clients to generate unforgeable rate-proofs demonstrating how frequently they have performed specific actions. These rate-proofs can be sent to web servers in lieu of solving CAPTCHAs. CACTI provides strong client privacy guarantees, since the information is only sent to the visited website and authenticated using a group signature scheme. Our evaluations show that overall latency of generating and verifying a CACTI rate-proof is less than 0.25 sec, while CACTI&#x27;s bandwidth overhead is over 98% lower than that of current CAPTCHA systems.

  匹配依据：TEE: intel sgx, trusted execution environments, trustzone

  </details>

- **Denial-of-Service Vulnerability of Hash-based Transaction Sharding: Attack and Countermeasure**
  2020-07-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.08600)
  Truc Nguyen, My T. Thai

  <details><summary>摘要 / Abstract</summary>

  Since 2016, sharding has become an auspicious solution to tackle the scalability issue in legacy blockchain systems. Despite its potential to strongly boost the blockchain throughput, sharding comes with its own security issues. To ease the process of deciding which shard to place transactions, existing sharding protocols use a hash-based transaction sharding in which the hash value of a transaction determines its output shard. Unfortunately, we show that this mechanism opens up a loophole that could be exploited to conduct a single-shard flooding attack, a type of Denial-of-Service (DoS) attack, to overwhelm a single shard that ends up reducing the performance of the system as a whole. To counter the single-shard flooding attack, we propose a countermeasure that essentially eliminates the loophole by rejecting the use of hash-based transaction sharding. The countermeasure leverages the Trusted Execution Environment (TEE) to let blockchain&#x27;s validators securely execute a transaction sharding algorithm with a negligible overhead. We provide a formal specification for the countermeasure and analyze its security properties in the Universal Composability (UC) framework. Finally, a proof-of-concept is developed to demonstrate the feasibility and practicality of our solution.

  匹配依据：TEE: trusted execution environment

  </details>

- **SESAME: Software defined Enclaves to Secure Inference Accelerators with Multi-tenant Execution**
  2020-07-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.06751)
  Sarbartha Banerjee, Prakash Ramrakhyani, Shijia Wei, Mohit Tiwari

  <details><summary>摘要 / Abstract</summary>

  Hardware-enclaves that target complex CPU designs compromise both security and performance. Programs have little control over micro-architecture, which leads to side-channel leaks, and then have to be transformed to have worst-case control- and data-flow behaviors and thus incur considerable slowdown. We propose to address these security and performance problems by bringing enclaves into the realm of accelerator-rich architectures. The key idea is to construct software-defined enclaves (SDEs) where the protections and slowdown are tied to an application-defined threat model and tuned by a compiler for the accelerator&#x27;s specific domain. This vertically integrated approach requires new hardware data-structures to partition, clear, and shape the utilization of hardware resources; and a compiler that instantiates and schedules these data-structures to create multi-tenant enclaves on accelerators. We demonstrate our ideas with a comprehensive prototype -- Sesame -- that includes modifications to compiler, ISA, and microarchitecture to a decoupled access execute (DAE) accelerator framework for deep learning models. Our security evaluation shows that classifiers that could distinguish different layers in VGG, ResNet, and AlexNet, fail to do so when run using Sesame. Our synthesizable hardware prototype (on a Xilinx Pynq board) demonstrates how the compiler and micro-architecture enables threat-model-specific trade-offs in code size increase ranging from 3-7 $\%$ and run-time performance overhead for specific defenses ranging from 3.96$\%$ to 34.87$\%$ (across confidential inputs and models and single vs. multi-tenant systems).

  匹配依据：TEE: hardware enclaves

  </details>

- **BDTF: A Blockchain-Based Data Trading Framework with Trusted Execution Environment**
  2020-07-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.06813)
  Guoxiong Su, Wenyuan Yang, Zhengding Luo, Yinghong Zhang, Zhiqiang Bai, Yuesheng Zhu

  <details><summary>摘要 / Abstract</summary>

  The need for data trading promotes the emergence of data market. However, in conventional data markets, both data buyers and data sellers have to use a centralized trading platform which might be dishonest. A dishonest centralized trading platform may steal and resell the data seller&#x27;s data, or may refuse to send data after receiving payment from the data buyer. It seriously affects the fair data transaction and harm the interests of both parties to the transaction. To address this issue, we propose a novel blockchain-based data trading framework with Trusted Execution Environment (TEE) to provide a trusted decentralized platform for fair data trading. In our design, a blockchain network is proposed to realize the payments from data buyers to data sellers, and a trusted exchange is built by using a TEE for the first time to achieve fair data transmission. With these help, data buyers and data sellers can conduct transactions directly. We implement our proposed framework on Ethereum and Intel SGX, security analysis and experimental results have demonstrated that the framework proposed can effectively guarantee the fair completion of data tradings.

  匹配依据：TEE: intel sgx, trusted execution environment

  </details>

- **On Runtime Software Security of TrustZone-M based IoT Devices**
  2020-07-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.05876)
  Lan Luo, Yue Zhang, Cliff C. Zou, Xinhui Shao, Zhen Ling, Xinwen Fu

  <details><summary>摘要 / Abstract</summary>

  Internet of Things (IoT) devices have been increasingly integrated into our daily life. However, such smart devices suffer a broad attack surface. Particularly, attacks targeting the device software at runtime are challenging to defend against if IoT devices use resource-constrained microcontrollers (MCUs). TrustZone-M, a TrustZone extension for MCUs, is an emerging security technique fortifying MCU based IoT devices. This paper presents the first security analysis of potential software security issues in TrustZone-M enabled MCUs. We explore the stack-based buffer overflow (BOF) attack for code injection, return-oriented programming (ROP) attack, heap-based BOF attack, format string attack, and attacks against Non-secure Callable (NSC) functions in the context of TrustZone-M. We validate these attacks using the TrustZone-M enabled SAM L11 MCU. Strategies to mitigate these software attacks are also discussed.

  匹配依据：TEE: trustzone

  </details>

- **An Exploratory Analysis of Microcode as a Building Block for System Defenses**
  2020-07-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.03549)
  Benjamin Kollenda, Philipp Koppe, Marc Fyrbiak, Christian Kison, Christof Paar, Thorsten Holz

  <details><summary>摘要 / Abstract</summary>

  Microcode is an abstraction layer used by modern x86 processors that interprets user-visible CISC instructions to hardware-internal RISC instructions. The capability to update x86 microcode enables a vendor to modify CPU behavior in-field, and thus patch erroneous microarchitectural processes or even implement new features. Most prominently, the recent Spectre and Meltdown vulnerabilities were mitigated by Intel via microcode updates. Unfortunately, microcode is proprietary and closed source, and there is little publicly available information on its inner workings. In this paper, we present new reverse engineering results that extend and complement the public knowledge of proprietary microcode. Based on these novel insights, we show how modern system defenses and tools can be realized in microcode on a commercial, off-the-shelf AMD x86 CPU. We demonstrate how well-established system security defenses such as timing attack mitigations, hardware-assisted address sanitization, and instruction set randomization can be realized in microcode. We also present a proof-of-concept implementation of a microcode-assisted instrumentation framework. Finally, we show how a secure microcode update mechanism and enclave functionality can be implemented in microcode to realize a small trusted execution environment. All microcode programs and the whole infrastructure needed to reproduce and extend our results are publicly available.

  匹配依据：TEE: trusted execution environment

  </details>

- **Offline Model Guard: Secure and Private ML on Mobile Devices**
  2020-07-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.02351)
  Sebastian P. Bayerl, Tommaso Frassetto, Patrick Jauernig, Korbinian Riedhammer, Ahmad-Reza Sadeghi, Thomas Schneider, Emmanuel Stapf, Christian Weinert

  <details><summary>摘要 / Abstract</summary>

  Performing machine learning tasks in mobile applications yields a challenging conflict of interest: highly sensitive client information (e.g., speech data) should remain private while also the intellectual property of service providers (e.g., model parameters) must be protected. Cryptographic techniques offer secure solutions for this, but have an unacceptable overhead and moreover require frequent network interaction. In this work, we design a practically efficient hardware-based solution. Specifically, we build Offline Model Guard (OMG) to enable privacy-preserving machine learning on the predominant mobile computing platform ARM - even in offline scenarios. By leveraging a trusted execution environment for strict hardware-enforced isolation from other system components, OMG guarantees privacy of client data, secrecy of provided models, and integrity of processing algorithms. Our prototype implementation on an ARM HiKey 960 development board performs privacy-preserving keyword recognition using TensorFlow Lite for Microcontrollers in real time.

  匹配依据：TEE: trusted execution environment

  </details>

- **MQT-TZ: Secure MQTT Broker for Biomedical Signal Processing on the Edge**
  2020-07-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.01555)
  Carlos Segarra, Ricard Delgado-Gonzalo, Valerio Schiavoni

  <details><summary>摘要 / Abstract</summary>

  Physical health records belong to healthcare providers, but the information contained within belongs to each patient. In an increasing manner, more health-related data is being acquired by wearables and other IoT devices following the ever-increasing trend of the &quot;Quantified Self&quot;. Even though data protection regulations (e.g., GDPR) encourage the usage of privacy-preserving processing techniques, most of the current IoT infrastructure was not originally conceived for such purposes. One of the most used communication protocols, MQTT, is a lightweight publish-subscribe protocol commonly used in the Edge and IoT applications. In MQTT, the broker must process data on clear text, hence exposing a large attack surface for a malicious agent to steal/tamper with this health-related data. In this paper, we introduce MQT-TZ, a secure MQTT broker leveraging Arm TrustZone, a popular Trusted Execution Environment (TEE). We define a mutual TLS-based handshake and a two-layer encryption for end-to-end security using the TEE as a trusted proxy. We provide quantitative evaluation of our open-source PoC on streaming ECGs in real time and highlight the trade-offs.

  匹配依据：TEE: trusted execution environment, trustzone

  </details>

- **Confidential Computing for Privacy-Preserving Contact Tracing**
  2020-06-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2006.14235)
  David Sturzenegger, Aetienne Sardon, Stefan Deml, Thomas Hardjono

  <details><summary>摘要 / Abstract</summary>

  Contact tracing is paramount to fighting the pandemic but it comes with legitimate privacy concerns. This paper proposes a system enabling both, contact tracing and data privacy. We propose the use of the Intel SGX trusted execution environment to build a privacy-preserving contact tracing backend. While the concept of a confidential computing backend proposed in this paper can be combined with any existing contact tracing smartphone application, we describe a full contact tracing system for demonstration purposes. A prototype of a privacy-preserving contact tracing system based on SGX has been implemented by the authors in a hackathon.

  匹配依据：TEE: confidential computing, intel sgx, sgx, trusted execution environment

  </details>

- **A Survey of Published Attacks on Intel SGX**
  2020-06-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2006.13598)
  Alexander Nilsson, Pegah Nikbakht Bideh, Joakim Brorsson

  <details><summary>摘要 / Abstract</summary>

  Intel Software Guard Extensions (SGX) provides a trusted execution environment (TEE) to run code and operate sensitive data. SGX provides runtime hardware protection where both code and data are protected even if other code components are malicious. However, recently many attacks targeting SGX have been identified and introduced that can thwart the hardware defence provided by SGX. In this paper we present a survey of all attacks specifically targeting Intel SGX that are known to the authors, to date. We categorized the attacks based on their implementation details into 7 different categories. We also look into the available defence mechanisms against identified attacks and categorize the available types of mitigations for each presented attack.

  匹配依据：TEE: intel sgx, sgx, trusted execution environment

  </details>

- **CacheOut: Leaking Data on Intel CPUs via Cache Evictions**
  2020-06-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2006.13353)
  Stephan van Schaik, Marina Minkin, Andrew Kwong, Daniel Genkin, Yuval Yarom

  <details><summary>摘要 / Abstract</summary>

  Recent transient-execution attacks, such as RIDL, Fallout, and ZombieLoad, demonstrated that attackers can leak information while it transits through microarchitectural buffers. Named Microarchitectural Data Sampling (MDS) by Intel, these attacks are likened to &quot;drinking from the firehose&quot;, as the attacker has little control over what data is observed and from what origin. Unable to prevent the buffers from leaking, Intel issued countermeasures via microcode updates that overwrite the buffers when the CPU changes security domains. In this work we present CacheOut, a new microarchitectural attack that is capable of bypassing Intel&#x27;s buffer overwrite countermeasures. We observe that as data is being evicted from the CPU&#x27;s L1 cache, it is often transferred back to the leaky CPU buffers where it can be recovered by the attacker. CacheOut improves over previous MDS attacks by allowing the attacker to choose which data to leak from the CPU&#x27;s L1 cache, as well as which part of a cache line to leak. We demonstrate that CacheOut can leak information across multiple security boundaries, including those between processes, virtual machines, user and kernel space, and from SGX enclaves.

  匹配依据：TEE: sgx, sgx enclaves

  </details>

- **Visor: Privacy-Preserving Video Analytics as a Cloud Service**
  2020-06-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2006.09628)
  Rishabh Poddar, Ganesh Ananthanarayanan, Srinath Setty, Stavros Volos, Raluca Ada Popa

  <details><summary>摘要 / Abstract</summary>

  Video-analytics-as-a-service is becoming an important offering for cloud providers. A key concern in such services is privacy of the videos being analyzed. While trusted execution environments (TEEs) are promising options for preventing the direct leakage of private video content, they remain vulnerable to side-channel attacks. We present Visor, a system that provides confidentiality for the user&#x27;s video stream as well as the ML models in the presence of a compromised cloud platform and untrusted co-tenants. Visor executes video pipelines in a hybrid TEE that spans both the CPU and GPU. It protects the pipeline against side-channel attacks induced by data-dependent access patterns of video modules, and also addresses leakage in the CPU-GPU communication channel. Visor is up to $1000\times$ faster than naïve oblivious solutions, and its overheads relative to a non-oblivious baseline are limited to $2\times$--$6\times$.

  匹配依据：TEE: trusted execution environments

  </details>

- **The Ritva Blockchain: Enabling Confidential Transactions at Scale**
  2020-06-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2006.01758) · [IACR ePrint](https://eprint.iacr.org/2020/642)
  Henri Aare, Peter Vitols

  <details><summary>摘要 / Abstract</summary>

  The distributed ledger technology has been widely hailed as the break- through technology. It has realised a great number of application scenarios, and improved workflow of many domains. Nonetheless, there remain a few major concerns in adopting and deploying the distributed ledger technology at scale. In this white paper, we tackle two of them, namely the throughput scalability and confidentiality protection for transactions. We learn from the existing body of research, and build a scale-out blockchain plat- form that champions privacy called RVChain. RVChain takes advantage of trusted execution environment to offer confidentiality protection for transactions, and scale the throughput of the network in proportion with the number of network participants by supporting parallel shadow chains.

  匹配依据：TEE: trusted execution environment

  </details>

- **DarKnight: A Data Privacy Scheme for Training and Inference of Deep Neural Networks**
  2020-06-01 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2006.01300)
  Hanieh Hashemi, Yongqin Wang, Murali Annavaram

  <details><summary>摘要 / Abstract</summary>

  Protecting the privacy of input data is of growing importance as machine learning methods reach new application domains. In this paper, we provide a unified training and inference framework for large DNNs while protecting input privacy and computation integrity. Our approach called DarKnight uses a novel data blinding strategy using matrix masking to create input obfuscation within a trusted execution environment (TEE). Our rigorous mathematical proof demonstrates that our blinding process provides information-theoretic privacy guarantee by bounding information leakage. The obfuscated data can then be offloaded to any GPU for accelerating linear operations on blinded data. The results from linear operations on blinded data are decoded before performing non-linear operations within the TEE. This cooperative execution allows DarKnight to exploit the computational power of GPUs to perform linear operations while exploiting TEEs to protect input privacy. We implement DarKnight on an Intel SGX TEE augmented with a GPU to evaluate its performance.

  匹配依据：TEE: intel sgx, trusted execution environment

  </details>

- **AQUAREUM: Non-Equivocating Censorship-Evident Centralized Ledger with EVM-Based Verifiable Execution using Trusted Computing and Blockchain**
  2020-05-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.13339)
  Ivan Homoliak, Mario Larangeira, Martin Peresini, Pawel Szalachowski

  <details><summary>摘要 / Abstract</summary>

  Distributed ledger systems (i.e., blockchains) have received a lot of attention. They promise to enable mutually untrusted participants to execute transactions while providing the immutability of the data and censorship resistance. Although decentralized ledgers are a disruptive innovation, as of today, they suffer from scalability, privacy, or governance issues. Therefore, they are inapplicable for many important use cases, where interestingly, centralized ledger systems might gain adoption. Unfortunately, centralized ledgers have also drawbacks, e.g., a lack of efficient verifiability or a higher risk of censorship and equivocation. In this paper, we present AQUAREUM, a novel framework for centralized ledgers removing their main limitations. By a unique combination of a trusted execution environment (TEE) with a public blockchain, AQUAREUM provides publicly verifiable non-equivocating censorship-evident private and high-performance ledgers. AQUAREUM is integrated with a Turing-complete virtual machine (e.g., EVM), allowing arbitrary transaction processing logic, such as transfers or client-specified smart contracts. AQUAREUM is fully implemented and can process over 400 transactions per second on a commodity PC. Furthermore, we modeled AQUAREUM using the Universal Composability framework and proved its security.

  匹配依据：TEE: trusted execution environment

  </details>

- **The Lazarus Effect: Healing Compromised Devices in the Internet of Small Things**
  2020-05-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.09714)
  Manuel Huber, Stefan Hristozov, Simon Ott, Vasil Sarafov, Marcus Peinado

  <details><summary>摘要 / Abstract</summary>

  We live in a time when billions of IoT devices are being deployed and increasingly relied upon. This makes ensuring their availability and recoverability in case of a compromise a paramount goal. The large and rapidly growing number of deployed IoT devices make manual recovery impractical, especially if the devices are dispersed over a large area. Thus, there is a need for a reliable and scalable remote recovery mechanism that works even after attackers have taken full control over devices, possibly misusing them or trying to render them useless. To tackle this problem, we present Lazarus, a system that enables the remote recovery of compromised IoT devices. With Lazarus, an IoT administrator can remotely control the code running on IoT devices unconditionally and within a guaranteed time bound. This makes recovery possible even in case of severe corruption of the devices&#x27; software stack. We impose only minimal hardware requirements, making Lazarus applicable even for low-end constrained off-the-shelf IoT devices. We isolate Lazarus&#x27;s minimal recovery trusted computing base from untrusted software both in time and by using a trusted execution environment. The temporal isolation prevents secrets from being leaked through side-channels to untrusted software. Inside the trusted execution environment, we place minimal functionality that constrains untrusted software at runtime. We implement Lazarus on an ARM Cortex-M33-based microcontroller in a full setup with an IoT hub, device provisioning and secure update functionality. Our prototype can recover compromised embedded OSs and bare-metal applications and prevents attackers from bricking devices, for example, through flash wear out. We show this at the example of FreeRTOS, which requires no modifications but only a single additional task. Our evaluation shows negligible runtime performance impact and moderate memory requirements.

  匹配依据：TEE: trusted execution environment

  </details>

- **Towards Memory Safe Python Enclave for Security Sensitive Computation**
  2020-05-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.05996)
  Huibo Wang, Mingshen Sun, Qian Feng, Pei Wang, Tongxin Li, Yu Ding

  <details><summary>摘要 / Abstract</summary>

  Intel SGX Guard eXtensions (SGX), a hardware-supported trusted execution environment (TEE), is designed to protect security-sensitive applications. However, since enclave applications are developed with memory unsafe languages such as C/C++, traditional memory corruption is not eliminated in SGX. Rust-SGX is the first toolkit providing enclave developers with a memory-language. However, Rust is considered a Systems language and has become the right choice for concurrent applications and web browsers. Many application domains such as Big Data, Machine Learning, Robotics, Computer Vision are more commonly developed in the python programming language. Therefore, Python application developers cannot benefit from secure enclaves like Intel SGX and rust-SGX. To fill this gap, we propose Python-SGX, which is a memory-safe SGX SDK providing enclave developers a memory-safe Python development environment. The key idea is to enable memory-safe Python language in SGX by solving the following key challenges: (1) defining a memory-safe Python interpreter (2)replacing unsafe elements of Python interpreter with safe ones,(3) achieving comparable performance to non-enclave Python applications, and (4) not introducing any unsafe new code or libraries into SGX. We propose to build Python-SGX with PyPy, a Python interpreter written by RPython, which is a subset of Python, and tame unsafe parts in PyPy by formal verification, security hardening, and memory safe language. We have implemented python-SGX and tested it with a series of benchmarks programs. Our evaluation results show that Python-SGX does not cause significant overhead.

  匹配依据：TEE: intel sgx, secure enclaves, sgx, trusted execution environment

  </details>

- **Serdab: An IoT Framework for Partitioning Neural Networks Computation across Multiple Enclaves**
  2020-05-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.06043)
  Tarek Elgamal, Klara Nahrstedt

  <details><summary>摘要 / Abstract</summary>

  Recent advances in Deep Neural Networks (DNN) and Edge Computing have made it possible to automatically analyze streams of videos from home/security cameras over hierarchical clusters that include edge devices, close to the video source, as well as remote cloud compute resources. However, preserving the privacy and confidentiality of users&#x27; sensitive data as it passes through different devices remains a concern to most users. Private user data is subject to attacks by malicious attackers or misuse by internal administrators who may use the data in activities that are not explicitly approved by the user. To address this challenge, we present Serdab, a distributed orchestration framework for deploying deep neural network computation across multiple secure enclaves (e.g., Intel SGX). Secure enclaves provide a guarantee on the privacy of the data/code deployed inside it. However, their limited hardware resources make them inefficient when solely running an entire deep neural network. To bridge this gap, Serdab presents a DNN partitioning strategy to distribute the layers of the neural network across multiple enclave devices or across an enclave device and other hardware accelerators. Our partitioning strategy achieves up to 4.7x speedup compared to executing the entire neural network in one enclave.

  匹配依据：TEE: intel sgx, secure enclaves

  </details>

- **Manifestation of the divergence between antisymmetrized-molecular-dynamics and container pictures of $^{9}$Be via ${}^{9}$Be($p,pn$)${}^{8}$Be knockout reaction**
  2020-05-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.04582)
  Nguyen Tri Toan Phuc, Mengjiao Lyu, Yohei Chiba, Kazuyuki Ogata

  <details><summary>摘要 / Abstract</summary>

  We propose a new approach to probe the spatial extension of the valence neutron orbital in the $^{9}$Be nucleus via the ${}^{9}$Be($p,pn$)${}^{8}$Be knockout reaction. This property of the nuclear molecular orbital has not been established in previous experimental studies and divergence exists between the theoretical descriptions of ${}^{9}$Be from different perspectives, \textit{i.e.}, the antisymmetrized molecular dynamics and the container pictures of cluster dynamics. These pictures are represented by two different well-proven microscopic models, the antisymmetrized molecular dynamics (AMD) and Tohsaki-Horiuchi-Schuck-Röpke (THSR) wave functions. The corresponding reduced width amplitudes (RWAs) in the $^{8}$Be$+n$ channel are extracted from both the AMD and THSR wave functions, and they are found to describe drastically different valence-nucleon motion, which shows the theoretical ambiguity in describing the $π$-orbitals in $^{9}$Be. Using the RWAs as input, the physical observables of the ${}^{9}$Be($p,pn$)${}^{8}$Be knockout reaction are predicted by the distorted-wave impulse approximation (DWIA) framework. The magnitudes of the triple-differential cross sections (TDX) are found to be highly sensitive to the RWA input. It is concluded that the ${}^{9}$Be($p,pn$)${}^{8}$Be knockout reaction could provide a feasible probing for the subtle differences between several structure models manifesting through the spatial extension of the $π$-orbital in the $^{9}$Be nucleus.

  匹配依据：TEE: tdx (context)

  </details>

- **Building and Maintaining a Third-Party Library Supply Chain for Productive and Secure SGX Enclave Development**
  2020-05-09 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.04367)
  Pei Wang, Yu Ding, Mingshen Sun, Huibo Wang, Tongxin Li, Rundong Zhou, Zhaofeng Chen, Yiming Jing

  <details><summary>摘要 / Abstract</summary>

  The big data industry is facing new challenges as concerns about privacy leakage soar. One of the remedies to privacy breach incidents is to encapsulate computations over sensitive data within hardware-assisted Trusted Execution Environments (TEE). Such TEE-powered software is called secure enclaves. Secure enclaves hold various advantages against competing for privacy-preserving computation solutions. However, enclaves are much more challenging to build compared with ordinary software. The reason is that the development of TEE software must follow a restrictive programming model to make effective use of strong memory encryption and segregation enforced by hardware. These constraints transitively apply to all third-party dependencies of the software. If these dependencies do not officially support TEE hardware, TEE developers have to spend additional engineering effort in porting them. High development and maintenance cost is one of the major obstacles against adopting TEE-based privacy protection solutions in production. In this paper, we present our experience and achievements with regard to constructing and continuously maintaining a third-party library supply chain for TEE developers. In particular, we port a large collection of Rust third-party libraries into Intel SGX, one of the most mature trusted computing platforms. Our supply chain accepts upstream patches in a timely manner with SGX-specific security auditing. We have been able to maintain the SGX ports of 159 open-source Rust libraries with reasonable operational costs. Our work can effectively reduce the engineering cost of developing SGX enclaves for privacy-preserving data processing and exchange.

  匹配依据：TEE: intel sgx, secure enclaves, sgx, sgx enclave, sgx enclaves, trusted execution environments

  </details>

- **SGX-SSD: A Policy-based Versioning SSD with Intel SGX**
  2020-04-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.13354)
  Jinwoo Ahn, Seungjin Lee, Jinhoon Lee, Yungwoo Ko, Donghyun Min, Junghee Lee, Youngjae Kim

  <details><summary>摘要 / Abstract</summary>

  This paper demonstrates that SSDs, which perform device-level versioning, can be exposed to data tampering attacks when the retention time of data is less than the malware&#x27;s dwell time. To deal with that threat, we propose SGX-SSD, a SGX-based versioning SSD which selectively preserves file history based on the given policy. The proposed system adopts Intel SGX to implement the version policy management system that is safe from high-privileged malware. Based on the policy, only the necessary data is selectively preserved in SSD that prevents files with less priority from wasting space and also ensures the integrity of important files.

  匹配依据：TEE: intel sgx, sgx

  </details>

- **Dedicated Security Chips in the Age of Secure Enclaves**
  2020-04-24 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/469)
  Kari Kostiainen, Aritra Dhar, Srdjan Capkun

  <details><summary>摘要 / Abstract</summary>

  Secure enclave architectures have become prevalent in modern CPUs and enclaves provide a flexible way to implement various hardware-assisted security services. But special-purpose security chips can still have advantages. Interestingly, dedicated security chips can also assist enclaves and improve their security.

  匹配依据：TEE: secure enclave, secure enclaves

  </details>

- **SEVurity: No Security Without Integrity -- Breaking Integrity-Free Memory Encryption with Minimal Assumptions**
  2020-04-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.11071)
  Luca Wilke, Jan Wichelmann, Mathias Morbitzer, Thomas Eisenbarth

  <details><summary>摘要 / Abstract</summary>

  One reason for not adopting cloud services is the required trust in the cloud provider: As they control the hypervisor, any data processed in the system is accessible to them. Full memory encryption for Virtual Machines (VM) protects against curious cloud providers as well as otherwise compromised hypervisors. AMD Secure Encrypted Virtualization (SEV) is the most prevalent hardware-based full memory encryption for VMs. Its newest extension, SEV-ES, also protects the entire VM state during context switches, aiming to ensure that the host neither learns anything about the data that is processed inside the VM, nor is able to modify its execution state. Several previous works have analyzed the security of SEV and have shown that, by controlling I/O, it is possible to exfiltrate data or even gain control over the VM&#x27;s execution. In this work, we introduce two new methods that allow us to inject arbitrary code into SEV-ES secured virtual machines. Due to the lack of proper integrity protection, it is sufficient to reuse existing ciphertext to build a high-speed encryption oracle. As a result, our attack no longer depends on control over the I/O, which is needed by prior attacks. As I/O manipulation is highly detectable, our attacks are stealthier. In addition, we reverse-engineer the previously unknown, improved Xor-Encrypt-Xor (XEX) based encryption mode, that AMD is using on updated processors, and show, for the first time, how it can be overcome by our new attacks.

  匹配依据：TEE: secure encrypted virtualization

  </details>

- **BAHULAM: Distributed Data Analytics on Secure Enclaves**
  2020-04-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.07597)
  Srinivasa Rao Aravilli

  <details><summary>摘要 / Abstract</summary>

  This is a survey of some of the currently available frameworks (opensource/commercial) in order to run distributed data applications(Hadoop, Spark) on secure enclaves. Intel, AMD, Amazon support secure enclaves on their systems Intel-SGX, AMD Memory Encryption, AWS Nitro Enclaves respectively. Keystone is an open-source framework for architecting Trusted Execution Environments and isolation.

  匹配依据：TEE: intel sgx, secure enclaves, trusted execution environments

  </details>

- **DarkneTZ: Towards Model Privacy at the Edge using Trusted Execution Environments**
  2020-04-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.05703)
  Fan Mo, Ali Shahin Shamsabadi, Kleomenis Katevas, Soteris Demetriou, Ilias Leontiadis, Andrea Cavallaro, Hamed Haddadi

  <details><summary>摘要 / Abstract</summary>

  We present DarkneTZ, a framework that uses an edge device&#x27;s Trusted Execution Environment (TEE) in conjunction with model partitioning to limit the attack surface against Deep Neural Networks (DNNs). Increasingly, edge devices (smartphones and consumer IoT devices) are equipped with pre-trained DNNs for a variety of applications. This trend comes with privacy risks as models can leak information about their training data through effective membership inference attacks (MIAs). We evaluate the performance of DarkneTZ, including CPU execution time, memory usage, and accurate power consumption, using two small and six large image classification models. Due to the limited memory of the edge device&#x27;s TEE, we partition model layers into more sensitive layers (to be executed inside the device TEE), and a set of layers to be executed in the untrusted part of the operating system. Our results show that even if a single layer is hidden, we can provide reliable model privacy and defend against state of the art MIAs, with only 3% performance overhead. When fully utilizing the TEE, DarkneTZ provides model protections with up to 10% overhead.

  匹配依据：TEE: trusted execution environment, trusted execution environments

  </details>

- **The Paradox of Information Access: Growing Isolation in the Age of Sharing**
  2020-04-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.01967)
  Tarek Abdelzaher, Heng Ji, Jinyang Li, Chaoqi Yang, John Dellaverson, Lixia Zhang, Chao Xu, Boleslaw K. Szymanski

  <details><summary>摘要 / Abstract</summary>

  Modern online media, such as Twitter, Instagram, and YouTube, enable anyone to become an information producer and to offer online content for potentially global consumption. By increasing the amount of globally accessible real-time information, today&#x27;s ubiquitous producers contribute to a world, where an individual consumes vanishingly smaller fractions of all produced content. In general, consumers preferentially select information that closely matches their individual views and values. The bias inherent in such selection is further magnified by today&#x27;s information curation services that maximize user engagement (and thus service revenue) by filtering new content in accordance with observed consumer preferences. Consequently, individuals get exposed to increasingly narrower bands of the ideology spectrum. Societies get fragmented into increasingly ideologically isolated enclaves. These enclaves (or echo-chambers) then become vulnerable to misinformation spread, which in turn further magnifies polarization and bias. We call this dynamic the paradox of information access; a growing ideological fragmentation in the age of sharing. This article describes the technical, economic, and socio-cognitive contributors to this paradox, and explores research directions towards its mitigation.

  匹配依据：TEE: enclaves (context)

  </details>

- **Building secure distributed applications the DECENT way**
  2020-04-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.02020)
  Haofan Zheng, Owen Arden

  <details><summary>摘要 / Abstract</summary>

  Remote attestation (RA) authenticates code running in trusted execution environments (TEEs), allowing trusted code to be deployed even on untrusted hosts. However, trust relationships established by one component in a distributed application may impact the security of other components, making it difficult to reason about the security of the application as a whole. Furthermore, traditional RA approaches interact badly with modern web service design, which tends to employ small interacting microservices, short session lifetimes, and little or no state. This paper presents the Decent Application Platform, a framework for building secure decentralized applications. Decent applications authenticate and authorize distributed enclave components using a protocol based on self-attestation certificates, a reusable credential based on RA and verifiable by a third party. Components mutually authenticate each other not only based on their code, but also based on the other components they trust, ensuring that no transitively-connected components receive unauthorized information. While some other TEE frameworks support mutual authentication in some form, Decent is the only system that supports mutual authentication without requiring an additional trusted third party besides the trusted hardware&#x27;s manufacturer. We have verified the secrecy and authenticity of Decent application data in ProVerif, and implemented two applications to evaluate Decent&#x27;s expressiveness and performance: DecentRide, a ride-sharing service, and DecentHT, a distributed hash table. On the YCSB benchmark, we show that DecentHT achieves 7.5x higher throughput and 3.67x lower latency compared to a non-Decent implementation.

  匹配依据：TEE: trusted execution environments

  </details>

- **Trust Management as a Service: Enabling Trusted Execution in the Face of Byzantine Stakeholders**
  2020-03-31 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2003.14099)
  Franz Gregor, Wojciech Ozga, Sébastien Vaucher, Rafael Pires, Do Le Quoc, Sergei Arnautov, André Martin, Valerio Schiavoni, Pascal Felber, Christof Fetzer

  <details><summary>摘要 / Abstract</summary>

  Trust is arguably the most important challenge for critical services both deployed as well as accessed remotely over the network. These systems are exposed to a wide diversity of threats, ranging from bugs to exploits, active attacks, rogue operators, or simply careless administrators. To protect such applications, one needs to guarantee that they are properly configured and securely provisioned with the &quot;secrets&quot; (e.g., encryption keys) necessary to preserve not only the confidentiality, integrity and freshness of their data but also their code. Furthermore, these secrets should not be kept under the control of a single stakeholder - which might be compromised and would represent a single point of failure - and they must be protected across software versions in the sense that attackers cannot get access to them via malicious updates. Traditional approaches for solving these challenges often use ad hoc techniques and ultimately rely on a hardware security module (HSM) as root of trust. We propose a more powerful and generic approach to trust management that instead relies on trusted execution environments (TEEs) and a set of stakeholders as root of trust. Our system, PALAEMON, can operate as a managed service deployed in an untrusted environment, i.e., one can delegate its operations to an untrusted cloud provider with the guarantee that data will remain confidential despite not trusting any individual human (even with root access) nor system software. PALAEMON addresses in a secure, efficient and cost-effective way five main challenges faced when developing trusted networked applications and services. Our evaluation on a range of benchmarks and real applications shows that PALAEMON performs efficiently and can protect secrets of services without any change to their source code.

  匹配依据：TEE: trusted execution environments

  </details>

- **Secure Cloud Storage with Client-Side Encryption Using a Trusted Execution Environment**
  2020-03-09 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2003.04163)
  Marciano da Rocha, Dalton Cézane Gomes Valadares, Angelo Perkusich, Kyller Costa Gorgonio, Rodrigo Tomaz Pagno, Newton Carlos Will

  <details><summary>摘要 / Abstract</summary>

  With the evolution of computer systems, the amount of sensitive data to be stored as well as the number of threats on these data grow up, making the data confidentiality increasingly important to computer users. Currently, with devices always connected to the Internet, the use of cloud data storage services has become practical and common, allowing quick access to such data wherever the user is. Such practicality brings with it a concern, precisely the confidentiality of the data which is delivered to third parties for storage. In the home environment, disk encryption tools have gained special attention from users, being used on personal computers and also having native options in some smartphone operating systems. The present work uses the data sealing, feature provided by the Intel Software Guard Extensions (Intel SGX) technology, for file encryption. A virtual file system is created in which applications can store their data, keeping the security guarantees provided by the Intel SGX technology, before send the data to a storage provider. This way, even if the storage provider is compromised, the data are safe. To validate the proposal, the Cryptomator software, which is a free client-side encryption tool for cloud files, was integrated with an Intel SGX application (enclave) for data sealing. The results demonstrate that the solution is feasible, in terms of performance and security, and can be expanded and refined for practical use and integration with cloud synchronization services.

  匹配依据：TEE: intel sgx, trusted execution environment

  </details>

- **CopyCat: Controlled Instruction-Level Attacks on Enclaves**
  2020-02-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.08437)
  Daniel Moghimi, Jo Van Bulck, Nadia Heninger, Frank Piessens, Berk Sunar

  <details><summary>摘要 / Abstract</summary>

  The adversarial model presented by trusted execution environments (TEEs) has prompted researchers to investigate unusual attack vectors. One particularly powerful class of controlled-channel attacks abuses page-table modifications to reliably track enclave memory accesses at a page-level granularity. In contrast to noisy microarchitectural timing leakage, this line of deterministic controlled-channel attacks abuses indispensable architectural interfaces and hence cannot be mitigated by tweaking microarchitectural resources. We propose an innovative controlled-channel attack, named CopyCat, that deterministically counts the number of instructions executed within a single enclave code page. We show that combining the instruction counts harvested by CopyCat with traditional, coarse-grained page-level leakage allows the accurate reconstruction of enclave control flow at a maximal instruction-level granularity. CopyCat can identify intra-page and intra-cache line branch decisions that ultimately may only differ in a single instruction, underscoring that even extremely subtle control flow deviations can be deterministically leaked from secure enclaves. We demonstrate the improved resolution and practicality of CopyCat on Intel SGX in an extensive study of single-trace and deterministic attacks against cryptographic implementations, and give novel algorithmic attacks to perform single-trace key extraction that exploit subtle vulnerabilities in the latest versions of widely-used cryptographic libraries. Our findings highlight the importance of stricter verification of cryptographic implementations, especially in the context of TEEs.

  匹配依据：TEE: intel sgx, secure enclaves, trusted execution environments

  </details>

- **A &gt;100 Gbps Inline AES-GCM Hardware Engine and Protected DMA Transfers between SGX Enclave and FPGA Accelerator Device**
  2020-02-14 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/178)
  Santosh Ghosh, Luis S Kida, Soham Jayesh Desai, Reshma Lal

  <details><summary>摘要 / Abstract</summary>

  This paper proposes a method to protect DMA data transfer that can be used to offload computation to an accelerator. The proposal minimizes changes in the hardware platform and to the application and SW stack. The paper de-scribes the end-to-end scheme to protect communication between an appli-cation running inside a SGX enclave and a FPGA accelerator optimized for bandwidth and latency and details the implementation of AES-GCM hard-ware engines with high bandwidth and low latency.

  匹配依据：TEE: sgx, sgx enclave

  </details>

- **EncDBDB: Searchable Encrypted, Fast, Compressed, In-Memory Database using Enclaves**
  2020-02-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.05097)
  Benny Fuhry, Jayanth Jain H A, Florian Kerschbaum

  <details><summary>摘要 / Abstract</summary>

  Data confidentiality is an important requirement for clients when outsourcing databases to the cloud. Trusted execution environments, such as Intel SGX, offer an efficient, hardware-based solution to this cryptographic problem. Existing solutions are not optimized for column-oriented, in-memory databases and pose impractical memory requirements on the enclave. We present EncDBDB, a novel approach for client-controlled encryption of a column-oriented, in-memory databases allowing range searches using an enclave. EncDBDB offers nine encrypted dictionaries, which provide different security, performance and storage efficiency tradeoffs for the data. It is especially suited for complex, read-oriented, analytic queries, e.g., as present in data warehouses. The computational overhead compared to plaintext processing is within a millisecond even for databases with millions of entries and the leakage is limited. Compressed encrypted data requires less space than a corresponding plaintext column. Furthermore, the resulting code - and data - in the enclave is very small reducing the potential for security-relevant implementation errors and side-channel leakages.

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **GhostKnight: Breaching Data Integrity via Speculative Execution**
  2020-02-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.00524)
  Zhi Zhang, Yueqiang Cheng, Surya Nepal

  <details><summary>摘要 / Abstract</summary>

  Existing speculative execution attacks are limited to breaching confidentiality of data beyond privilege boundary, the so-called spectre-type attacks. All of them utilize the changes in microarchitectural buffers made by the speculative execution to leak data. We show that the speculative execution can be abused to break data integrity. We observe that the speculative execution not only leaves traces in the microarchitectural buffers but also induces side effects within DRAM, that is, the speculative execution can trigger an access to an illegitimate address in DRAM. If the access to DRAM is frequent enough, then architectural changes (i.e., permanent bit flips in DRAM) will occur, which we term GhostKnight. With the power of of GhostKnight, an attacker is essentially able to cross different privilege boundaries and write exploitable bits to other privilege domains. In our future work, we will develop a GhostKnight-based exploit to cross a trusted execution environment, defeat a 1024-bit RSA exponentiation implementation and obtain a controllable signature.

  匹配依据：TEE: trusted execution environment

  </details>

- **Provably Secure Isolation for Interruptible Enclaved Execution on Small Microprocessors: Extended Version**
  2020-01-29 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2001.10881)
  Matteo Busi, Job Noorman, Jo Van Bulck, Letterio Galletta, Pierpaolo Degano, Jan Tobias Mühlberg, Frank Piessens

  <details><summary>摘要 / Abstract</summary>

  Computer systems often provide hardware support for isolation mechanisms like privilege levels, virtual memory, or enclaved execution. Over the past years, several successful software-based side-channel attacks have been developed that break, or at least significantly weaken the isolation that these mechanisms offer. Extending a processor with new architectural or micro-architectural features, brings a risk of introducing new such side-channel attacks. This paper studies the problem of extending a processor with new features without weakening the security of the isolation mechanisms that the processor offers. We propose to use full abstraction as a formal criterion for the security of a processor extension, and we instantiate that criterion to the concrete case of extending a microprocessor that supports enclaved execution with secure interruptibility of these enclaves. This is a very relevant instantiation as several recent papers have shown that interruptibility of enclaves leads to a variety of software-based side-channel attacks. We propose a design for interruptible enclaves, and prove that it satisfies our security criterion. We also implement the design on an open-source enclave-enabled microprocessor, and evaluate the cost of our design in terms of performance and hardware size.

  匹配依据：TEE: enclaves (context)

  </details>

- **Distributed systems and trusted execution environments: Trade-offs and challenges**
  2020-01-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2001.09670)
  Rafael Pereira Pires

  <details><summary>摘要 / Abstract</summary>

  Security and privacy concerns in computer systems have grown in importance with the ubiquity of connected devices. TEEs provide security guarantees based on cryptographic constructs built in hardware. Intel software guard extensions (SGX), in particular, implements powerful mechanisms that can shield sensitive data even from privileged users with full control of system software. In this work, we essentially explore some of the challenges of designing secure distributed systems by using Intel SGX as cornerstone. We do so by designing and experimentally evaluating several elementary systems ranging from communication and processing middleware to a peer-to-peer privacy-preserving solution. We start with support systems that naturally fit cloud deployment scenarios, namely content-based routing, batching and stream processing frameworks. We implement prototypes and use them to analyse the manifested memory usage issues intrinsic to SGX. Next, we aim at protecting very sensitive data: cryptographic keys. By leveraging TEEs, we design protocols for group data sharing that have lower computational complexity than legacy methods. As a bonus, our proposals allow large savings on metadata volume and processing time of cryptographic operations, all with equivalent security guarantees. Finally, we propose privacy-preserving systems against established services like web-search engines. Our evaluation shows that we propose the most robust system in comparison to existing solutions with regard to user re-identification rates and results accuracy in a scalable way. Overall, this thesis proposes new mechanisms that take advantage of TEEs for distributed system architectures. We show through an empirical approach on top of Intel SGX what are the trade-offs of distinct designs applied to distributed communication and processing, cryptographic protocols and private web search.

  匹配依据：TEE: intel sgx, sgx, trusted execution environments

  </details>

- **SeCloak: ARM Trustzone-based Mobile Peripheral Control**
  2020-01-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2001.08840)
  Matthew Lentz, Rijurekha Sen, Peter Druschel, Bobby Bhattacharjee

  <details><summary>摘要 / Abstract</summary>

  Reliable on-off control of peripherals on smart devices is a key to security and privacy in many scenarios. Journalists want to reliably turn off radios to protect their sources during investigative reporting. Users wish to ensure cameras and microphones are reliably off during private meetings. In this paper, we present SeCloak, an ARM TrustZone-based solution that ensures reliable on-off control of peripherals even when the platform software is compromised. We design a secure kernel that co-exists with software running on mobile devices (e.g., Android and Linux) without requiring any code modifications. An Android prototype demonstrates that mobile peripherals like radios, cameras, and microphones can be controlled reliably with a very small trusted computing base and with minimal performance overhead.

  匹配依据：TEE: trustzone

  </details>

- **When one vulnerable primitive turns viral: Novel single-trace attacks on ECDSA and RSA**
  2020-01-20 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/055)
  Alejandro Cabrera Aldaya, Billy Bob Brumley

  <details><summary>摘要 / Abstract</summary>

  Microarchitecture based side-channel attacks are common threats nowadays. Intel SGX technology provides a strong isolation from an adversarial OS, however, does not guarantee protection against side-channel attacks. In this paper, we analyze the security of the mbedTLS binary GCD algorithm, an implementation that offers interesting challenges when compared for example with OpenSSL, due to the usage of very tight loops in the former. Using practical experiments we demonstrate the mbedTLS binary GCD implementation is vulnerable to side-channel analysis using the SGX-Step framework against mbedTLS based SGX enclaves. We analyze the security of some use cases of this algorithm in this library, resulting in the discovery of a new vulnerability in the ECDSA code path that allows a single-trace attack against this implementation. This vulnerability is three-fold interesting: * It resides in the implementation of a countermeasure which makes it more dangerous due to the false state of security the countermeasure currently offers. * It reduces mbedTLS ECDSA security to an integer factorization problem. * An unexpected GCD call inside the ECDSA code path compromises the countermeasure. We also cover an orthogonal use case, this time inside the mbedTLS RSA code path during the computation of a CRT parameter when loading a private key. The attack also exploits the binary GCD implementation threat, showing how a single vulnerable primitive leads to multiple vulnerabilities. We demonstrate both security threats with end-to-end attacks using 1000 trials each, showing in both cases single-trace attacks can be achieved with success rates very close to 100%.

  匹配依据：TEE: intel sgx, sgx, sgx enclaves

  </details>

- **Accelerating Forward and Backward Private Searchable Encryption Using Trusted Execution**
  2020-01-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2001.03743)
  Viet Vo, Shangqi Lai, Xingliang Yuan, Shi-Feng Sun, Surya Nepal, Joseph K. Liu

  <details><summary>摘要 / Abstract</summary>

  Searchable encryption (SE) is one of the key enablers for building encrypted databases. It allows a cloud server to search over encrypted data without decryption. Dynamic SE additionally includes data addition and deletion operations to enrich the functions of encrypted databases. Recent attacks exploiting the leakage in dynamic operations drive rapid development of new SE schemes revealing less information while performing updates; they are also known as forward and backward private SE. Newly added data is no longer linkable to queries issued before, and deleted data is no longer searchable in queries issued later. However, those advanced SE schemes reduce the efficiency of SE, especially in the communication cost between the client and server. In this paper, we resort to the hardware-assisted solution, aka Intel SGX, to ease the above bottleneck. Our key idea is to leverage SGX to take over the most tasks of the client, i.e., tracking keyword states along with data addition and caching deleted data. However, handling large datasets is non-trivial due to the I/O and memory constraints of the SGX enclave. We further develop batch data processing and state compression technique to reduce the communication overhead between the SGX and untrusted server, and minimise the memory footprint in the enclave. We conduct a comprehensive set of evaluations on both synthetic and real-world datasets, which confirm that our designs outperform the prior art.

  匹配依据：TEE: intel sgx, sgx, sgx enclave

  </details>

- **Blockchain-based Smart-IoT Trust Zone Measurement Architecture**
  2020-01-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2001.03002)
  Jawad Ali, Toqeer Ali, Yazed Alsaawy, Ahmad Shahrafidz Khalid, Shahrulniza Musa

  <details><summary>摘要 / Abstract</summary>

  With a rapid growth in the IT industry, Internet of Things (IoT) has gained a tremendous attention and become a central aspect of our environment. In IoT the things (devices) communicate and exchange the data without the act of human intervention. Such autonomy and proliferation of IoT ecosystem make the devices more vulnerable to attacks. In this paper, we propose a behavior monitor in IoT-Blockchain setup which can provide trust-confidence to outside networks. Behavior monitor extracts the activity of each device and analyzes the behavior using deep auto-encoders. In addition, we also incorporate Trusted Execution Technology (Intel SGX) in order to provide a secure execution environment for applications and data on blockchain. Finally, in evaluation we analyze three IoT devices data that is infected by mirai attack. The evaluation results demonstrate the ability of our proposed method in terms of accuracy and time required for detection.

  匹配依据：TEE: intel sgx

  </details>

- **Towards a secure behavior modeling for IoT networks using Blockchain**
  2020-01-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2001.01841)
  Jawad Ali, Ahmad Shahrafidz Khalid, Eiad Yafi, Shahrulniza Musa, Waqas Ahmed

  <details><summary>摘要 / Abstract</summary>

  Internet of Things (IoT) occupies a vital aspect of our everyday lives. IoT networks composed of smart-devices which communicate and transfer the information without the physical intervention of humans. Due to such proliferation and autonomous nature of IoT systems make these devices threatened and prone to a severe kind of threats. In this paper, we introduces a behavior capturing, and verification procedures in blockchain supported smart-IoT systems that can be able to show the trust-level confidence to outside networks. We defined a custom \emph{Behavior Monitor} and implement on a selected node that can extract the activity of each device and analyzes the behavior using deep machine learning strategy. Besides, we deploy Trusted Execution Technology (TEE) which can be used to provide a secure execution environment (enclave) for sensitive application code and data on the blockchain. Finally, in the evaluation phase we analyze various IoT devices data that is infected by Mirai attack. The evaluation results show the strength of our proposed method in terms of accuracy and time required for detection.

  匹配依据：TEE: tee (context)

  </details>
