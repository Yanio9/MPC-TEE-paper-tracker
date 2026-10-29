# 2025 · MPC + TEE · 仅预印本来源 · 第 1/1 页

[总目录](../PAPERS.md)

- **What You Trust Is Insecure: Demystifying How Developers (Mis)Use Trusted Execution Environments in Practice**
  2025-12-19 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.17363)
  Yuqing Niu, Jieke Shi, Ruidong Han, Ye Liu, Chengyan Ma, Yunbo Lyu, David Lo

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs), such as Intel SGX and ARM TrustZone, provide isolated regions of CPU and memory for secure computation and are increasingly used to protect sensitive data and code across diverse application domains. However, little is known about how developers actually use TEEs in practice. This paper presents the first large-scale empirical study of real-world TEE applications. We collected and analyzed 241 open-source projects from GitHub that utilize the two most widely-adopted TEEs, Intel SGX and ARM TrustZone. By combining manual inspection with customized static analysis scripts, we examined their adoption contexts, usage patterns, and development practices across three phases. First, we categorized the projects into 8 application domains and identified trends in TEE adoption over time. We found that the dominant use case is IoT device security (30%), which contrasts sharply with prior academic focus on blockchain and cryptographic systems (7%), while AI model protection (12%) is rapidly emerging as a growing domain. Second, we analyzed how TEEs are integrated into software and observed that 32.4% of the projects reimplement cryptographic functionalities instead of using official SDK APIs, suggesting that current SDKs may have limited usability and portability to meet developers&#x27; practical needs. Third, we examined security practices through manual inspection and found that 25.3% (61 of 241) of the projects exhibit insecure coding behaviors when using TEEs, such as hardcoded secrets and missing input validation, which undermine their intended security guarantees. Our findings have important implications for improving the usability of TEE SDKs and supporting developers in trusted software development.

  匹配依据：MPC: secure computation; TEE: intel sgx, trusted execution environments, trustzone

  </details>

- **HOT Protocol**
  2025-12-01 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.02287)
  Peter Volnov, Georgii Kuksa, Andrey Zhevlakov

  <details><summary>摘要 / Abstract</summary>

  HOT Protocol provides the infrastructure that allows smart contracts to securely own and manage private keys. The Multi-Party Computation (MPC) Network manages signing keys. By running an MPC node inside a Trusted Execution Environment (TEE), the protocol achieves stronger security guarantees while lowering economic requirements for participants. The NEAR Protocol provides a decentralized and efficient state layer. Key management can be integrated with any smart contract across Stellar, TON, Solana, and EVM-compatible networks.

  匹配依据：MPC: multi party computation; TEE: trusted execution environment

  </details>

- **DEXO: A Secure and Fair Exchange Mechanism for Decentralized IoT Data Markets**
  2025-11-23 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.18498)
  Yue Li, Ifteher Alom, Wenhai Sun, Yang Xiao

  <details><summary>摘要 / Abstract</summary>

  Opening up data produced by the Internet of Things (IoT) and mobile devices for public utilization can maximize their economic value. Challenges remain in the trustworthiness of the data sources and the security of the trading process, particularly when there is no trust between the data providers and consumers. In this paper, we propose DEXO, a decentralized data exchange mechanism that facilitates secure and fair data exchange between data consumers and distributed IoT/mobile data providers at scale, allowing the consumer to verify the data generation process and the providers to be compensated for providing authentic data, with correctness guarantees from the exchange platform. To realize this, DEXO extends the decentralized oracle network model that has been successful in the blockchain applications domain to incorporate novel hardware-cryptographic co-design that harmonizes trusted execution environment, secret sharing, and smart contract-assisted fair exchange. For the first time, DEXO ensures end-to-end data confidentiality, source verifiability, and fairness of the exchange process with strong resilience against participant collusion. We implemented a prototype of the DEXO system to demonstrate feasibility. The evaluation shows a moderate deployment cost and significantly improved blockchain operation efficiency compared to a popular data exchange mechanism.

  匹配依据：MPC: secret sharing; TEE: trusted execution environment

  </details>

- **Emerging Paradigms for Securing Federated Learning Systems**
  2025-09-25 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.21147)
  Amr Akmal Abouelmagd, Amr Hilal

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) facilitates collaborative model training while keeping raw data decentralized, making it a conduit for leveraging the power of IoT devices while maintaining privacy of the locally collected data. However, existing privacy- preserving techniques present notable hurdles. Methods such as Multi-Party Computation (MPC), Homomorphic Encryption (HE), and Differential Privacy (DP) often incur high compu- tational costs and suffer from limited scalability. This survey examines emerging approaches that hold promise for enhancing both privacy and efficiency in FL, including Trusted Execution Environments (TEEs), Physical Unclonable Functions (PUFs), Quantum Computing (QC), Chaos-Based Encryption (CBE), Neuromorphic Computing (NC), and Swarm Intelligence (SI). For each paradigm, we assess its relevance to the FL pipeline, outlining its strengths, limitations, and practical considerations. We conclude by highlighting open challenges and prospective research avenues, offering a detailed roadmap for advancing secure and scalable FL systems.

  匹配依据：MPC: multi party computation; TEE: trusted execution environments

  </details>

- **Private, Verifiable, and Auditable AI Systems**
  2025-08-27 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.00085)
  Tobin South

  <details><summary>摘要 / Abstract</summary>

  The growing societal reliance on artificial intelligence necessitates robust frameworks for ensuring its security, accountability, and trustworthiness. This thesis addresses the complex interplay between privacy, verifiability, and auditability in modern AI, particularly in foundation models. It argues that technical solutions that integrate these elements are critical for responsible AI innovation. Drawing from international policy contributions and technical research to identify key risks in the AI pipeline, this work introduces novel technical solutions for critical privacy and verifiability challenges. Specifically, the research introduces techniques for enabling verifiable and auditable claims about AI systems using zero-knowledge cryptography; utilizing secure multi-party computation and trusted execution environments for auditable, confidential deployment of large language models and information retrieval; and implementing enhanced delegation mechanisms, credentialing systems, and access controls to secure interactions with autonomous and multi-agent AI systems. Synthesizing these technical advancements, this dissertation presents a cohesive perspective on balancing privacy, verifiability, and auditability in foundation model-based AI systems, offering practical blueprints for system designers and informing policy discussions on AI safety and governance.

  匹配依据：MPC: secure multi party computation; TEE: trusted execution environments

  </details>

- **Silentflow: Leveraging Trusted Execution for Resource-Limited MPC via Hardware-Algorithm Co-design**
  2025-08-18 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.13357)
  Zhuoran Li, Hanieh Totonchi Asl, Ebrahim Nouri, Yifei Cai, Danella Zhao

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation (MPC) offers a practical foundation for privacy-preserving machine learning at the edge, with MPC commonly employed to support nonlinear operations. These MPC protocols fundamentally rely on Oblivious Transfer (OT), particularly Correlated OT (COT), to generate correlated randomness essential for secure computation. Although COT generation is efficient in conventional two-party settings with resource-rich participants, it becomes a critical bottleneck in real-world inference on resource-constrained devices (e.g., IoT sensors and wearables), due to both communication latency and limited computational capacity. To enable real-time secure inference, we introduce Silentflow, a highly efficient Trusted Execution Environment (TEE)-assisted protocol that eliminates communication in COT generation. We tackle the core performance bottleneck-low computational intensity-through structured algorithmic decomposition: kernel fusion for parallelism, Blocked On-chip eXpansion (BOX) to improve memory access patterns, and vectorized batch operations to maximize memory bandwidth utilization. Through design space exploration, we balance end-to-end latency and resource demands, achieving up to 39.51x speedup over state-of-the-art protocols. By offloading COT computations to a Zynq-7000 SoC, SilentFlow accelerates PPMLaaS inference on the ImageNet dataset under resource constraints, achieving a 4.62x and 3.95x speedup over Cryptflow2 and Cheetah, respectively.

  匹配依据：MPC: oblivious transfer, secure computation, secure multi party computation; TEE: trusted execution environment

  </details>

- **Policy-Driven AI in Dataspaces: Taxonomy, Explainability, and Pathways for Compliant Innovation**
  2025-07-26 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.20014)
  Joydeep Chandra, Satyam Kumar Navneet

  <details><summary>摘要 / Abstract</summary>

  As AI-driven dataspaces become integral to data sharing and collaborative analytics, ensuring privacy, performance, and policy compliance presents significant challenges. This paper provides a comprehensive review of privacy-preserving and policy-aware AI techniques, including Federated Learning, Differential Privacy, Trusted Execution Environments, Homomorphic Encryption, and Secure Multi-Party Computation, alongside strategies for aligning AI with regulatory frameworks such as GDPR and the EU AI Act. We propose a novel taxonomy to classify these techniques based on privacy levels, performance impacts, and compliance complexity, offering a clear framework for practitioners and researchers to navigate trade-offs. Key performance metrics -- latency, throughput, cost overhead, model utility, fairness, and explainability -- are analyzed to highlight the multi-dimensional optimization required in dataspaces. The paper identifies critical research gaps, including the lack of standardized privacy-performance KPIs, challenges in explainable AI for federated ecosystems, and semantic policy enforcement amidst regulatory fragmentation. Future directions are outlined, proposing a conceptual framework for policy-driven alignment, automated compliance validation, standardized benchmarking, and integration with European initiatives like GAIA-X, IDS, and Eclipse EDC. By synthesizing technical, ethical, and regulatory perspectives, this work lays the groundwork for developing trustworthy, efficient, and compliant AI systems in dataspaces, fostering innovation in secure and responsible data-driven ecosystems.

  匹配依据：MPC: secure multi party computation; TEE: trusted execution environments

  </details>

- **A User-Centric, Privacy-Preserving, and Verifiable Ecosystem for Personal Data Management and Utilization**
  2025-06-27 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.22606)
  Osama Zafar, Mina Namazi, Yuqiao Xu, Youngjin Yoo, Erman Ayday

  <details><summary>摘要 / Abstract</summary>

  In the current paradigm of digital personalized services, the centralized management of personal data raises significant privacy concerns, security vulnerabilities, and diminished individual autonomy over sensitive information. Despite their efficiency, traditional centralized architectures frequently fail to satisfy rigorous privacy requirements and expose users to data breaches and unauthorized access risks. This pressing challenge calls for a fundamental paradigm shift in methodologies for collecting, storing, and utilizing personal data across diverse sectors, including education, healthcare, and finance. This paper introduces a novel decentralized, privacy-preserving architecture that handles heterogeneous personal information, ranging from educational credentials to health records and financial data. Unlike traditional models, our system grants users complete data ownership and control, allowing them to selectively share information without compromising privacy. The architecture&#x27;s foundation comprises advanced privacy-enhancing technologies, including secure enclaves and federated learning, enabling secure computation, verification, and data sharing. The system supports diverse functionalities, including local computation, model training, and privacy-preserving data sharing, while ensuring data credibility and robust user privacy.

  匹配依据：MPC: secure computation; TEE: secure enclaves

  </details>

- **Private Signaling Secure Against Actively Corrupted Servers**
  2025-06-06 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1056)
  Haotian Chu, Xiao Wang, Yanxue Jia

  <details><summary>摘要 / Abstract</summary>

  Private signaling allows servers to identify a recipient&#x27;s messages on a public bulletin board without knowing the recipient&#x27;s metadata. It is a central tool for systems like privacy-preserving blockchains and anonymous messaging. However, unless with TEE, current constructions all assume that the servers are only passively corrupted, which significantly limits their practical relevance. In this work, we present a TEE-free simulation-secure private signaling protocol assuming two non-colluding servers, either of which can be actively corrupted. Crucially, we convert signal retrieval into a problem similar to private set intersection and use custom-built zero-knowledge proofs to ensure consistency with the public bulletin board. As a result, our protocol achieves lower server-to-server communication overhead and a much smaller digest compared to state-of-the-art semi-honest protocol. For example, for a board size of $2^{19}$ messages, the resulting digest size is only 33.57KB. Our protocol is also computationally efficient: retrieving private signals only takes about 2 minutes, using 16 threads and a LAN network.

  匹配依据：MPC: private set intersection; TEE: tee (context)

  </details>

- **Towards a DSL for hybrid secure computation**
  2025-05-27 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.20912)
  Romain de Laage

  <details><summary>摘要 / Abstract</summary>

  Fully homomorphic encryption (FHE) and trusted execution environments (TEE) are two approaches to provide confidentiality during data processing. Each approach has its own strengths and weaknesses. In certain scenarios, computations can be carried out in a hybrid environment, using both FHE and TEE. However, processing data in such hybrid settings presents challenges, as it requires to adapt and rewrite the algorithms for the chosen technique. We propose a domain-specific language (DSL) for secure computation that allows to express the computations to perform and execute them using a backend that leverages either FHE or TEE, depending on what is available.

  匹配依据：MPC: secure computation; TEE: trusted execution environments

  </details>

- **TERRA : Trojan-Resilient Reverse-Firewall for Cryptographic Applications**
  2025-04-29 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/761)
  Chandan Kumar, Nimish Mishra, Suvradip Chakraborty, Satrajit Ghosh, Debdeep Mukhopadhyay

  <details><summary>摘要 / Abstract</summary>

  Reverse firewalls (RFs), introduced by Mironov and Stephens Davidowitz at Eurocrypt 2015, provide a defence mechanism for cryptographic protocols against subversion attacks. In a subversion setting, an adversary compromises the machines of honest parties, enabling the leakage of their secrets through the protocol transcript. Previous research in this area has established robust guarantees, including resistance against data exfiltration for an RF. In this work, we present a new perspective focused on the implementation specifics of RFs. The inherently untrusted nature of RFs exposes their real-world implementations to the risk of Trojan insertion — an especially pressing issue in today’s outsourced supply chain ecosystem. We argue how Trojan-affected RF implementations can compromise their core exfiltration resistance property, leading to a complete breakdown of the RF’s security guarantees. Building on this perspective, we propose an enhanced definition for ``Trojan-resilient Reverse Firewalls&#x27;&#x27; (Tr-RF), incorporating an additional Trojan resilience property. We then present concrete instantiations of Tr-RFs for Coin Tossing (CT) and Oblivious Transfer (OT) protocols, utilizing techniques from Private Circuit III (CCS&#x27;16) to convert legacy RFs into Tr-RFs. We also give simulation-based proofs to claim the enhanced security guarantees of our Tr-RF instantiations. Additionally, we offer concrete implementations of our Tr-RF based CT and OT protocols utilizing the Open-Portable Trusted Execution Environment (OP-TEE). Through OP-TEE, we practically realize assumptions made in Private Circuit III that are critical to ensuring Tr-RF security, bridging the gap between theoretical models and real-world applications. To the best of our knowledge, this provides the first practical implementation of reverse firewalls for any cryptographic functionality. Our work emphasizes the importance of evaluating protocol specifications within implementation-specific contexts.

  匹配依据：MPC: oblivious transfer; TEE: trusted execution environment

  </details>

- **TFHE-Coder: Evaluating LLM-agentic Fully Homomorphic Encryption Code Generation**
  2025-03-15 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.12217)
  Mayank Kumar, Jiaqi Xue, Mengxin Zheng, Qian Lou

  <details><summary>摘要 / Abstract</summary>

  Fully Homomorphic Encryption over the torus (TFHE) enables computation on encrypted data without decryption, making it a cornerstone of secure and confidential computing. Despite its potential in privacy preserving machine learning, secure multi party computation, private blockchain transactions, and secure medical diagnostics, its adoption remains limited due to cryptographic complexity and usability challenges. While various TFHE libraries and compilers exist, practical code generation remains a hurdle. We propose a compiler integrated framework to evaluate LLM inference and agentic optimization for TFHE code generation, focusing on logic gates and ReLU activation. Our methodology assesses error rates, compilability, and structural similarity across open and closedsource LLMs. Results highlight significant limitations in off-the-shelf models, while agentic optimizations such as retrieval augmented generation (RAG) and few-shot prompting reduce errors and enhance code fidelity. This work establishes the first benchmark for TFHE code generation, demonstrating how LLMs, when augmented with domain-specific feedback, can bridge the expertise gap in FHE code generation.

  匹配依据：MPC: secure multi party computation; TEE: confidential computing

  </details>

- **IBE-IBE: Intent-Based Execution through Identity-Based Encryption and Auctions**
  2025-02-15 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/241)
  Peyman Momeni, Fig Smith

  <details><summary>摘要 / Abstract</summary>

  This paper introduces a decentralized and leaderless sealed bid auction model for dynamic pricing of intents across blockchain networks. We leverage Multi-Party Computation (MPC) and Identity-Based Encryption (IBE) to improve pricing while ensuring fairness and decentralization. By addressing the vulnerabilities of current centralized or static pricing mechanisms, our approach fosters transparent, secure, and competitive price discovery. We further enhance the confidentiality of intents through Multi-Party Computation (MPC), Fully Homomorphic Encryption (FHE), and Trusted Execution Environments (TEE). Our novel methodology mitigates the risks of frontrunning and centralization while preserving the rapid settlement times essential to decentralized finance (DeFi).

  匹配依据：MPC: multi party computation; TEE: trusted execution environments

  </details>

- **Individual Confidential Computing of Polynomials over Non-Uniform Information**
  2025-01-26 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.15645)
  Saar Tarnopolsky, Zirui, Deng, Vinayak Ramkumar, Netanel Raviv, Alejandro Cohen

  <details><summary>摘要 / Abstract</summary>

  In this paper, we address the problem of secure distributed computation in scenarios where user data is not uniformly distributed, extending existing frameworks that assume uniformity, an assumption that is challenging to enforce in data for computation. Motivated by the pervasive reliance on single service providers for data storage and computation, we propose a privacy-preserving scheme that achieves information-theoretic security guarantees for computing polynomials over non-uniform data distributions. Our framework builds upon the concept of perfect subset privacy and employs linear hashing techniques to transform non-uniform data into approximately uniform distributions, enabling robust and secure computation. We derive leakage bounds and demonstrate that information leakage of any subset of user data to untrusted service providers, i.e., not only to colluding workers but also (and more importantly) to the admin, remains negligible under the proposed scheme.

  匹配依据：MPC: secure computation; TEE: confidential computing

  </details>

- **Characterization of GPU TEE Overheads in Distributed Data Parallel ML Training**
  2025-01-20 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.11771)
  Jonghyun Lee, Yongqin Wang, Rachit Rajat, Murali Annavaram

  <details><summary>摘要 / Abstract</summary>

  Confidential computing (CC) or trusted execution enclaves (TEEs) is now the most common approach to enable secure computing in the cloud. The recent introduction of GPU TEEs by NVIDIA enables machine learning (ML) models to be trained without leaking model weights or data to the cloud provider. However, the potential performance implications of using GPU TEEs for ML training are not well characterized. In this work, we present an in-depth characterization study on performance overhead associated with running distributed data parallel (DDP) ML training with GPU Trusted Execution Environments (TEE). Our study reveals the performance challenges in DDP training within GPU TEEs. DDP uses ring-all-reduce, a well-known approach, to aggregate gradients from multiple devices. Ring all-reduce consists of multiple scatter-reduce and all-gather operations. In GPU TEEs only the GPU package (GPU and HBM memory) is trusted. Hence, any data communicated outside the GPU packages must be encrypted and authenticated for confidentiality and integrity verification. Hence, each phase of the ring-all-reduce requires encryption and message authentication code (MAC) generation from the sender, and decryption and MAC authentication on the receiver. As the number of GPUs participating in DDP increases, the overhead of secure inter-GPU communication during ring-all-reduce grows proportionally. Additionally, larger models lead to more asynchronous all-reduce operations, exacerbating the communication cost. Our results show that with four GPU TEEs, depending on the model that is being trained, the runtime per training iteration increases by an average of 8x and up to a maximum of 41.6x compared to DDP training without TEE.

  匹配依据：MPC: secure computing; TEE: confidential computing, trusted execution environments

  </details>

- **Exploring side-channels in Intel Trust Domain Extensions**
  2025-01-18 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/079)
  Upasana Mandal, Shubhi Shukla, Nimish Mishra, Sarani Bhattacharya, Paritosh Saxena, Debdeep Mukhopadhyay

  <details><summary>摘要 / Abstract</summary>

  Intel Trust Domain Extensions (TDX) has emerged as a crucial technology aimed at strengthening the isolation and security guarantees of virtual machines, especially as the demand for secure computation is growing largely. Despite the protections offered by TDX, in this work, we dig deep into the security claims and uncover an intricate observation in TDX. These findings undermine TDX&#x27;s core security guarantees by breaching the isolation between the Virtual Machine Manager (VMM) and Trust Domains (TDs). In this work for the first time, we show through a series of experiments that these performance counters can also be exploited by the VMM to differentiate between activities of an idle and active TD. The root cause of this leakage is core contention. This occurs when the VMM itself, or a process executed by the VMM, runs on the same core as the TD. Due to resource contention on the core, the effects of the TD&#x27;s computations become observable in the performance monitors collected by the VMM. This finding underscore the critical need for enhanced protections to bridge these gaps within these advanced virtualized environments.

  匹配依据：MPC: secure computation; TEE: trust domain extensions

  </details>

- **ABLE: Optimizing Mixed Arithmetic and Boolean Garbled Circuit**
  2025-01-13 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/048)
  Jianqiao Cambridge Mo, Karthik Garimella, Austin Ebel, Brandon Reagen

  <details><summary>摘要 / Abstract</summary>

  Privacy and security have become critical priorities in many scenarios. Privacy-preserving computation (PPC) is a powerful solution that allows functions to be computed directly on encrypted data. Garbled circuit (GC) is a key PPC technology that enables secure, confidential computing. GC comes in two forms: Boolean GC supports all operations by expressing functions as logic circuits; arithmetic GC is a newer technique to efficiently compute a set of arithmetic operations like addition and multiplication. Mixed GC combines both Boolean and arithmetic GC, in an attempt to optimize performance by computing each function in its most natural form. However, this introduces additional costly conversions between the two forms and it remains unclear if and when the efficiency gains of arithmetic GC outweigh these conversion costs. In this paper, we present Arithmetic Boolean Logic Exchange for Garbled Circuit, the first real implementation of mixed GC. ABLE profiles the performance of Boolean and arithmetic GC operations along with their conversions. We assess not only communication but also computation latency, a crucial factor in evaluating the end-to-end runtime of GC. Based on these insights, we propose a method to determine whether it is more efficient to use general Boolean GC or mixed GC for a given application. Rather than implementing both approaches to identify the better solution for each unique case, our method enables users to select the most suitable GC realization early in the design process. This method evaluates whether the benefits of transitioning operations from Boolean to arithmetic GC offset the associated conversion costs. We apply this approach to a neural network task as a case study. We propose an optimization to reduce the number of primes in arithmetic GC, cutting communication and compute latency by up to 14.1% and 15.7%, respectively. Additionally, we optimize mixed GC conversions with a row reduction technique, achieving a 48.6%reduction in garbled table size for bit-decomposition and a 50%reduction for bit-composition operation. Our code is open-sourced for community use.

  匹配依据：MPC: garbled circuit; TEE: confidential computing

  </details>
