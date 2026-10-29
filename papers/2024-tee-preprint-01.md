# 2024 · TEE · 仅预印本来源 · 第 1/2 页

[总目录](../PAPERS.md) · [下一页](2024-tee-preprint-02.md)

- **Swarm Contract: A Multi-Sovereign Agent Consensus Mechanism**
  2024-12-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.19256)
  Haowei Yang

  <details><summary>摘要 / Abstract</summary>

  Traditional smart contracts on blockchains excel at on-chain, deterministic logic. However, they have inherent limitations when dealing with large-scale off-chain data, dynamic multi-step workflows, and scenarios requiring high flexibility or iterative updates. In this paper, we propose the concept of a &quot;Swarm Contract&quot; (Swarm), a multi-agent mechanism wherein several digital life forms (DLF) or Sovereign Agents (SA) collectively handle complex tasks in Trusted Execution Environments (TEE). These digital entities are defined as autonomous software agents that own their code, state, and possibly on-chain assets, while operating free from centralized control. By leveraging a simple multi-signature wallet on-chain, Swarm moves most of the logic off-chain, achieving trust minimization through multi-agent consensus rather than a single monolithic on-chain contract. We illustrate these ideas with a lightweight off-chain auction example - minting and selling 10,000 identical NFTs - to showcase how off-chain coordination can determine a clearing price and finalize distribution, with each step performed collectively by multiple agents in TEE. This approach broadens the scope of trustless and decentralized solutions, potentially benefiting DAO governance, multi-modal data processing, and cross-chain interoperability.

  匹配依据：TEE: trusted execution environments

  </details>

- **VaulTor: Putting the TEE in Tor**
  2024-12-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.16064)
  Humza Ikram, Rumaisa Habib, Muaz Ali, Zartash Afzal Uzmi

  <details><summary>摘要 / Abstract</summary>

  Online services that desire to operate anonymously routinely host themselves as &#x27;Hidden Services&#x27; in the Tor network. However, these services are frequently threatened by deanonymization attacks, whereby their IP address and location may be inferred by the authorities. We present VaulTor, a novel architecture for the Tor network to ensure an extra layer of security for the Hidden Services against deanonymization attacks. In this new architecture, a volunteer (vault) is incentivized to host the web application content on behalf of the Hidden Service. The vault runs the hosted application in a Trusted Execution Environment (TEE) and becomes the point of contact for interested clients. This setup can substantially reduce the uptime requirement of the original Hidden Service provider and hence significantly decrease the chance of deanonymization attacks against them. We also show that the VaulTor architecture does not cause any noticeable performance degradation in accessing the hosted content (the performance degradation ranges from 2.6-5.5%).

  匹配依据：TEE: trusted execution environment

  </details>

- **T-Edge: Trusted Heterogeneous Edge Computing**
  2024-12-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.13905)
  Jiamin Shen, Yao Chen, Weng-Fai Wong, Ee-Chien Chang

  <details><summary>摘要 / Abstract</summary>

  Heterogeneous computing, which incorporates GPUs, NPUs, and FPGAs, is increasingly utilized to improve the efficiency of computer systems. However, this shift has given rise to significant security and privacy concerns, especially when the execution platform is remote. One way to tackle these challenges is to establish a trusted and isolated environment for remote program execution, while maintaining minimal overhead and flexibility. While CPU-based trusted execution has been extensively explored and found commercial success, extension to heterogeneous computing systems remains a challenge. This paper proposes a practical trusted execution environment design for ARM/FPGA System-on-Chip platforms, leveraging TrustZone&#x27;s unique characteristics. The design features a dedicated security controller within the ARM TrustZone, overseeing FPGA reconfiguration and managing communication between CPU cores and FPGA fabrics. This design involves a provisioning service that enables application users to establish trust in the FPGA fabric within cloud-based computing resources provided by the platform owner, running applications developed by third-party developers and hardware manufactured by the device manufacturer. To ensure the security of our proposed system, we employ an automated protocol verifier, ProVerif, to validate its compliance with essential security requirements. Furthermore, we demonstrate the practicality of our system model by implementing a prototype application on the Xilinx MPSoC development board.

  匹配依据：TEE: trusted execution environment, trustzone

  </details>

- **C-FedRAG: A Confidential Federated Retrieval-Augmented Generation System**
  2024-12-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.13163)
  Parker Addison, Minh-Tuan H. Nguyen, Tomislav Medan, Jinali Shah, Mohammad T. Manzari, Brendan McElrone, Laksh Lalwani, Aboli More, Smita Sharma, Holger R. Roth, Isaac Yang, Chester Chen, Daguang Xu, Yan Cheng, Andrew Feng, Ziyue Xu

  <details><summary>摘要 / Abstract</summary>

  Organizations seeking to utilize Large Language Models (LLMs) for knowledge querying and analysis often encounter challenges in maintaining an LLM fine-tuned on targeted, up-to-date information that keeps answers relevant and grounded. Retrieval Augmented Generation (RAG) has quickly become a feasible solution for organizations looking to overcome the challenges of maintaining proprietary models and to help reduce LLM hallucinations in their query responses. However, RAG comes with its own issues regarding scaling data pipelines across tiered-access and disparate data sources. In many scenarios, it is necessary to query beyond a single data silo to provide richer and more relevant context for an LLM. Analyzing data sources within and across organizational trust boundaries is often limited by complex data-sharing policies that prohibit centralized data storage, therefore, inhibit the fast and effective setup and scaling of RAG solutions. In this paper, we introduce Confidential Computing (CC) techniques as a solution for secure Federated Retrieval Augmented Generation (FedRAG). Our proposed Confidential FedRAG system (C-FedRAG) enables secure connection and scaling of a RAG workflows across a decentralized network of data providers by ensuring context confidentiality. We also demonstrate how to implement a C-FedRAG system using the NVIDIA FLARE SDK and assess its performance using the MedRAG toolkit and MIRAGE benchmarking dataset.

  匹配依据：TEE: confidential computing

  </details>

- **SeSeMI: Secure Serverless Model Inference on Sensitive Data**
  2024-12-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.11640)
  Guoyu Hu, Yuncheng Wu, Gang Chen, Tien Tuan Anh Dinh, Beng Chin Ooi

  <details><summary>摘要 / Abstract</summary>

  Model inference systems are essential for implementing end-to-end data analytics pipelines that deliver the benefits of machine learning models to users. Existing cloud-based model inference systems are costly, not easy to scale, and must be trusted in handling the models and user request data. Serverless computing presents a new opportunity, as it provides elasticity and fine-grained pricing. Our goal is to design a serverless model inference system that protects models and user request data from untrusted cloud providers. It offers high performance and low cost, while requiring no intrusive changes to the current serverless platforms. To realize our goal, we leverage trusted hardware. We identify and address three challenges in using trusted hardware for serverless model inference. These challenges arise from the high-level abstraction of serverless computing, the performance overhead of trusted hardware, and the characteristics of model inference workloads. We present SeSeMI, a secure, efficient, and cost-effective serverless model inference system. It adds three novel features non-intrusively to the existing serverless infrastructure and nothing else.The first feature is a key service that establishes secure channels between the user and the serverless instances, which also provides access control to models and users&#x27; data. The second is an enclave runtime that allows one enclave to process multiple concurrent requests. The final feature is a model packer that allows multiple models to be executed by one serverless instance. We build SeSeMI on top of Apache OpenWhisk, and conduct extensive experiments with three popular machine learning models. The results show that SeSeMI achieves low latency and low cost at scale for realistic workloads.

  匹配依据：TEE: enclave (context)

  </details>

- **VerifiableFL: Verifiable Claims for Federated Learning using Exclaves**
  2024-12-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.10537)
  Jinnan Guo, Kapil Vaswani, Andrew Paverd, Peter Pietzuch

  <details><summary>摘要 / Abstract</summary>

  In federated learning (FL), data providers jointly train a machine learning model without sharing their training data. This makes it challenging to provide verifiable claims about the trained FL model, e.g., related to the employed training data, any data sanitization, or the correct training algorithm-a malicious data provider can simply deviate from the correct training protocol without detection. While prior FL training systems have explored the use of trusted execution environments (TEEs) to protect the training computation, such approaches rely on the confidentiality and integrity of TEEs. The confidentiality guarantees of TEEs, however, have been shown to be vulnerable to a wide range of attacks, such as side-channel attacks. We describe VerifiableFL, a system for training FL models that establishes verifiable claims about trained FL models with the help of fine-grained runtime attestation proofs. Since these runtime attestation proofs only require integrity protection, VerifiableFL generates them using the new abstraction of exclaves. Exclaves are integrity-only execution environments, which do not contain software-managed secrets and thus are immune to data leakage attacks. VerifiableFL uses exclaves to attest individual data transformations during FL training without relying on confidentiality guarantees. The runtime attestation proofs then form an attested dataflow graph of the entire FL model training computation. The graph is checked by an auditor to ensure that the trained FL model satisfies its claims, such as the use of data sanitization by data providers or correct aggregation by the model provider. VerifiableFL extends NVFlare FL framework to use exclaves. We show that VerifiableFL introduces less than 12% overhead compared to unprotected FL training.

  匹配依据：TEE: trusted execution environments

  </details>

- **Building a Privacy Web with SPIDEr -- Secure Pipeline for Information De-Identification with End-to-End Encryption**
  2024-12-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.09222)
  Novoneel Chakraborty, Anshoo Tandon, Kailash Reddy, Kaushal Kirpekar, Bryan Paul Robert, Hari Dilip Kumar, Abhilash Venkatesh, Abhay Sharma

  <details><summary>摘要 / Abstract</summary>

  Data de-identification makes it possible to glean insights from data while preserving user privacy. The use of Trusted Execution Environments (TEEs) allow for the execution of de-identification applications on the cloud without the need for a user to trust the third-party application provider. In this paper, we present \textit{SPIDEr - Secure Pipeline for Information De-Identification with End-to-End Encryption}, our implementation of an end-to-end encrypted data de-identification pipeline. SPIDEr supports classical anonymisation techniques such as suppression, pseudonymisation, generalisation, and aggregation, as well as techniques that offer a formal privacy guarantee such as k-anonymisation and differential privacy. To enable scalability and improve performance on constrained TEE hardware, we enable batch processing of data for differential privacy computations. We present our design of the control flows for end-to-end secure execution of de-identification operations within a TEE. As part of the control flow for running SPIDEr within the TEE, we perform attestation, a process that verifies that the software binaries were properly instantiated on a known, trusted platform.

  匹配依据：TEE: trusted execution environments

  </details>

- **Protecting Confidentiality, Privacy and Integrity in Collaborative Learning**
  2024-12-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.08534)
  Dong Chen, Alice Dethise, Istemi Ekin Akkus, Ivica Rimac, Klaus Satzke, Antti Koskela, Marco Canini, Wei Wang, Ruichuan Chen

  <details><summary>摘要 / Abstract</summary>

  A collaboration between dataset owners and model owners is needed to facilitate effective machine learning (ML) training. During this collaboration, however, dataset owners and model owners want to protect the confidentiality of their respective assets (i.e., datasets, models and training code), with the dataset owners also caring about the privacy of individual users whose data is in their datasets. Existing solutions either provide limited confidentiality for models and training code, or suffer from privacy issues due to collusion. We present Citadel++, a collaborative ML training system designed to simultaneously protect the confidentiality of datasets, models and training code as well as the privacy of individual users. Citadel++ enhances differential privacy mechanisms to safeguard the privacy of individual user data while maintaining model utility. By employing Virtual Machine-level Trusted Execution Environments (TEEs) as well as the improved sandboxing and integrity mechanisms through OS-level techniques, Citadel++ effectively preserves the confidentiality of datasets, models and training code, and enforces our privacy mechanisms even when the models and training code have been maliciously designed. Our experiments show that Citadel++ provides model utility and performance while adhering to the confidentiality and privacy requirements of dataset owners and model owners, outperforming the state-of-the-art privacy-preserving training systems by up to 543x on CPU and 113x on GPU TEEs.

  匹配依据：TEE: trusted execution environments

  </details>

- **Privacy-Preserving Large Language Models: Mechanisms, Applications, and Future Directions**
  2024-12-09 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.06113)
  Guoshenghui Zhao, Eric Song

  <details><summary>摘要 / Abstract</summary>

  The rapid advancement of large language models (LLMs) has revolutionized natural language processing, enabling applications in diverse domains such as healthcare, finance and education. However, the growing reliance on extensive data for training and inference has raised significant privacy concerns, ranging from data leakage to adversarial attacks. This survey comprehensively explores the landscape of privacy-preserving mechanisms tailored for LLMs, including differential privacy, federated learning, cryptographic protocols, and trusted execution environments. We examine their efficacy in addressing key privacy challenges, such as membership inference and model inversion attacks, while balancing trade-offs between privacy and model utility. Furthermore, we analyze privacy-preserving applications of LLMs in privacy-sensitive domains, highlighting successful implementations and inherent limitations. Finally, this survey identifies emerging research directions, emphasizing the need for novel frameworks that integrate privacy by design into the lifecycle of LLMs. By synthesizing state-of-the-art approaches and future trends, this paper provides a foundation for developing robust, privacy-preserving large language models that safeguard sensitive information without compromising performance.

  匹配依据：TEE: trusted execution environments

  </details>

- **NebulaFL: Effective Asynchronous Federated Learning for JointCloud Computing**
  2024-12-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.04868)
  Fei Gao, Ming Hu, Zhiyu Xie, Peichang Shi, Xiaofei Xie, Guodong Yi, Huaimin Wang

  <details><summary>摘要 / Abstract</summary>

  With advancements in AI infrastructure and Trusted Execution Environment (TEE) technology, Federated Learning as a Service (FLaaS) through JointCloud Computing (JCC) is promising to break through the resource constraints caused by heterogeneous edge devices in the traditional Federated Learning (FL) paradigm. Specifically, with the protection from TEE, data owners can achieve efficient model training with high-performance AI services in the cloud. By providing additional FL services, cloud service providers can achieve collaborative learning among data owners. However, FLaaS still faces three challenges, i.e., i) low training performance caused by heterogeneous data among data owners, ii) high communication overhead among different clouds (i.e., data centers), and iii) lack of efficient resource scheduling strategies to balance training time and cost. To address these challenges, this paper presents a novel asynchronous FL approach named NebulaFL for collaborative model training among multiple clouds. To address data heterogeneity issues, NebulaFL adopts a version control-based asynchronous FL training scheme in each data center to balance training time among data owners. To reduce communication overhead, NebulaFL adopts a decentralized model rotation mechanism to achieve effective knowledge sharing among data centers. To balance training time and cost, NebulaFL integrates a reward-guided strategy for data owners selection and resource scheduling. The experimental results demonstrate that, compared to the state-of-the-art FL methods, NebulaFL can achieve up to 5.71\% accuracy improvement. In addition, NebulaFL can reduce up to 50% communication overhead and 61.94% costs under a target accuracy.

  匹配依据：TEE: trusted execution environment

  </details>

- **CCxTrust: Confidential Computing Platform Based on TEE and TPM Collaborative Trust**
  2024-12-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.03842)
  Ketong Shang, Jiangnan Lin, Yu Qin, Muyan Shen, Hongzhan Ma, Wei Feng, Dengguo Feng

  <details><summary>摘要 / Abstract</summary>

  Confidential Computing has emerged to address data security challenges in cloud-centric deployments by protecting data in use through hardware-level isolation. However, reliance on a single hardware root of trust (RoT) limits user confidence in cloud platforms, especially for high-performance AI services, where end-to-end protection of sensitive models and data is critical. Furthermore, the lack of interoperability and a unified trust model in multi-cloud environments prevents the establishment of a cross-platform, cross-cloud chain of trust, creating a significant trust gap for users with high privacy requirements. To address the challenges mentioned above, this paper proposes CCxTrust (Confidential Computing with Trust), a confidential computing platform leveraging collaborative roots of trust from TEE and TPM. CCxTrust combines the black-box RoT embedded in the CPU-TEE with the flexible white-box RoT of TPM to establish a collaborative trust framework. The platform implements independent Roots of Trust for Measurement (RTM) for TEE and TPM, and a collaborative Root of Trust for Report (RTR) for composite attestation. The Root of Trust for Storage (RTS) is solely supported by TPM. We also present the design and implementation of a confidential TPM supporting multiple modes for secure use within confidential virtual machines. Additionally, we propose a composite attestation protocol integrating TEE and TPM to enhance security and attestation efficiency, which is proven secure under the PCL protocol security model. We implemented a prototype of CCxTrust on a confidential computing server with AMD SEV-SNP and TPM chips, requiring minimal modifications to the TPM and guest Linux kernel. The composite attestation efficiency improved by 24% without significant overhead, while Confidential TPM performance showed a 16.47% reduction compared to standard TPM.

  匹配依据：TEE: amd sev, confidential computing

  </details>

- **PAPAYA Federated Analytics Stack: Engineering Privacy, Scalability and Practicality**
  2024-12-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.02340)
  Harish Srinivas, Graham Cormode, Mehrdad Honarkhah, Samuel Lurye, Jonathan Hehir, Lunwen He, George Hong, Ahmed Magdy, Dzmitry Huba, Kaikai Wang, Shen Guo, Shoubhik Bhattacharya

  <details><summary>摘要 / Abstract</summary>

  Cross-device Federated Analytics (FA) is a distributed computation paradigm designed to answer analytics queries about and derive insights from data held locally on users&#x27; devices. On-device computations combined with other privacy and security measures ensure that only minimal data is transmitted off-device, achieving a high standard of data protection. Despite FA&#x27;s broad relevance, the applicability of existing FA systems is limited by compromised accuracy; lack of flexibility for data analytics; and an inability to scale effectively. In this paper, we describe our approach to combine privacy, scalability, and practicality to build and deploy a system that overcomes these limitations. Our FA system leverages trusted execution environments (TEEs) and optimizes the use of on-device computing resources to facilitate federated data processing across large fleets of devices, while ensuring robust, defensible, and verifiable privacy safeguards. We focus on federated analytics (statistics and monitoring), in contrast to systems for federated learning (ML workloads), and we flag the key differences.

  匹配依据：TEE: trusted execution environments

  </details>

- **Liquefaction: Privately Liquefying Blockchain Assets**
  2024-12-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.02634)
  James Austgen, Andrés Fábrega, Mahimna Kelkar, Dani Vilardell, Sarah Allen, Kushal Babel, Jay Yu, Ari Juels

  <details><summary>摘要 / Abstract</summary>

  Inherent in the world of cryptocurrency systems and their security models is the notion that private keys, and thus assets, are controlled by individuals or individual entities. We present Liquefaction, a wallet platform that demonstrates the dangerous fragility of this foundational assumption by systemically breaking it. Liquefaction uses trusted execution environments (TEEs) to encumber private keys, i.e., attach rich, multi-user policies to their use. In this way, it enables the cryptocurrency credentials and assets of a single end-user address to be freely rented, shared, or pooled. It accomplishes these things privately, with no direct on-chain traces. Liquefaction demonstrates the sweeping consequences of TEE-based key encumbrance for the cryptocurrency landscape. Liquefaction can undermine the security and economic models of many applications and resources, such as locked tokens, DAO voting, airdrops, loyalty points, soulbound tokens, and quadratic voting. It can do so with no on-chain and minimal off-chain visibility. Conversely, we also discuss beneficial applications of Liquefaction, such as privacy-preserving, cost-efficient DAOs and a countermeasure to dusting attacks. Importantly, we describe an existing TEE-based tool that applications can use as a countermeasure to Liquefaction. Our work prompts a wholesale rethinking of existing models and enforcement of key and asset ownership in the cryptocurrency ecosystem.

  匹配依据：TEE: trusted execution environments

  </details>

- **Blindfold: Confidential Memory Management by Untrusted Operating System**
  2024-12-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.01059)
  Caihua Li, Seung-seob Lee, Lin Zhong

  <details><summary>摘要 / Abstract</summary>

  Confidential Computing (CC) has received increasing attention in recent years as a mechanism to protect user data from untrusted operating systems (OSes). Existing CC solutions hide confidential memory from the OS and/or encrypt it to achieve confidentiality. In doing so, they render OS memory optimization unusable or complicate the trusted computing base (TCB) required for optimization. This paper presents our results toward overcoming these limitations, synthesized in a CC design named Blindfold. Like many other CC solutions, Blindfold relies on a small trusted software component running at a higher privilege level than the kernel, called Guardian. It features three techniques that can enhance existing CC solutions. First, instead of nesting page tables, Guardian mediates how the OS accesses memory and handles exceptions by switching page and interrupt tables. Second, Blindfold employs a lightweight capability system to regulate the kernel semantic access to user memory, unifying case-by-case approaches in previous work. Finally, Blindfold provides carefully designed secure ABI for confidential memory management without encryption. We report an implementation of Blindfold that works on ARMv8-A/Linux. Using Blindfold prototype, we are able to evaluate the cost of enabling confidential memory management by the untrusted Linux kernel. We show Blindfold has a smaller runtime TCB than related systems and enjoys competitive performance. More importantly, we show that the Linux kernel, including all of its memory optimizations except memory compression, can function properly for confidential memory. This requires only about 400 lines of kernel modifications.

  匹配依据：TEE: confidential computing

  </details>

- **The Forking Way: When TEEs Meet Consensus**
  2024-12-01 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.00706)
  Annika Wilde, Tim Niklas Gruel, Claudio Soriente, Ghassan Karame

  <details><summary>摘要 / Abstract</summary>

  An increasing number of distributed platforms combine Trusted Execution Environments (TEEs) with blockchains. Indeed, many hail the combination of TEEs and blockchains a good &quot;marriage&quot;: TEEs bring confidential computing to the blockchain while the consensus layer could help defend TEEs from forking attacks. In this paper, we systemize how current blockchain solutions integrate TEEs and to what extent they are secure against forking attacks. To do so, we thoroughly analyze 29 proposals for TEE-based blockchains, ranging from academic proposals to production-ready platforms. We uncover a lack of consensus in the community on how to combine TEEs and blockchains. In particular, we identify four broad means to interconnect TEEs with consensus, analyze their limitations, and discuss possible remedies. Our analysis also reveals previously undocumented forking attacks on three production-ready TEE-based blockchains: Ten, Phala, and the Secret Network. We leverage our analysis to propose effective countermeasures against those vulnerabilities; we responsibly disclosed our findings to the developers of each affected platform.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **Asynchronous Byzantine Consensus with Trusted Monotonic Counters**
  2024-11-29 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1937)
  Yackolley Amoussou-Guenou, Maurice Herlihy, Maria Potop Butucaru

  <details><summary>摘要 / Abstract</summary>

  The paper promotes a new design paradigm for Byzantine tolerant distributed algorithms using trusted abstractions (oracles) specified in a functional manner. The contribution of the paper is conceptual. The objective here is to design distributed fundamental algorithms such as reliable broadcast and asynchronous byzantine consensus using trusted execution environments and to help designers to compare various solutions on a common ground. In this framework we revisit the Bracha&#x27;s seminal work on Asynchronous Byzantine Consensus. Our solution uses trusted monotonic counters abstraction and tolerates $t$ Byzantine processes in a system with $n$ processes, $n \geq 2t+1$. The keystone of our construction is a novel and elegant Byzantine Reliable Broadcast algorithm resilient to $t&lt;n$ Byzantine processes that uses an unique trusted monotonic counter (at the initiator).

  匹配依据：TEE: trusted execution environments

  </details>

- **RISecure-PUF: Multipurpose PUF-Driven Security Extensions with Lookaside Buffer in RISC-V**
  2024-11-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.14025)
  Chenghao Chen, Xiaolin Zhang, Kailun Qin, Tengfei Wang, Yipeng Shi, Tianyi Huang, Chi Zhang, Dawu Gu

  <details><summary>摘要 / Abstract</summary>

  RISC-V&#x27;s limited security features hinder its use in confidential computing and heterogeneous platforms. This paper introduces RISecure-PUF, a security extension utilizing existing Physical Unclonable Functions for key generation and secure protocol purposes. A one-way hash function is integrated to ensure provable security against modeling attacks, while a lookaside buffer accelerates batch sampling and minimizes reliance on error correction codes. Implemented on the Genesys 2 FPGA, RISecure-PUF improves at least $2.72\times$ in batch scenarios with negligible hardware overhead and a maximum performance reduction of $10.7\%$, enabled by reusing the hash function module in integrated environments such as cryptographic engines.

  匹配依据：TEE: confidential computing

  </details>

- **TEEMATE: Fast and Efficient Confidential Container using Shared Enclave**
  2024-11-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.11423)
  Chulmin Lee, Jaewon Hur, Sangho Lee, Byoungyoung Lee

  <details><summary>摘要 / Abstract</summary>

  Confidential container is becoming increasingly popular as it meets both needs for efficient resource management by cloud providers, and data protection by cloud users. Specifically, confidential containers integrate the container and the enclave, aiming to inherit the design-wise advantages of both (i.e., resource management and data protection). However, current confidential containers suffer from large performance overheads caused by i) a larger startup latency due to the enclave creation, and ii) a larger memory footprint due to the non-shareable characteristics of enclave memory. This paper explores a design conundrum of confidential container, examining why the confidential containers impose such large performance overheads. Surprisingly, we found there is a universal misconception that an enclave can only be used by a single (containerized) process that created it. However, an enclave can be shared across multiple processes, because an enclave is merely a set of physical resources while the process is an abstraction constructed by the host kernel. To this end, we introduce TeeMate, a new approach to utilize the enclaves on the host system. Especially, TeeMate designs the primitives to i) share the enclave memory between processes, thus preserving memory abstraction, and ii) assign the threads in enclave between processes, thus preserving thread abstraction. We concretized TeeMate on Intel SGX, and implemented confidential serverless computing and confidential database on top of TeeMate based confidential containers. The evaluation clearly demonstrated the strong practical impact of TeeMate by achieving at least 4.5 times lower latency and 2.8 times lower memory usage compared to the applications built on the conventional confidential containers.

  匹配依据：TEE: intel sgx

  </details>

- **GNN-Based Code Annotation Logic for Establishing Security Boundaries in C Code**
  2024-11-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.11567)
  Varun Gadey, Raphael Goetz, Christoph Sendner, Sampo Sovio, Alexandra Dmitrienko

  <details><summary>摘要 / Abstract</summary>

  Securing sensitive operations in today&#x27;s interconnected software landscape is crucial yet challenging. Modern platforms rely on Trusted Execution Environments (TEEs), such as Intel SGX and ARM TrustZone, to isolate security sensitive code from the main system, reducing the Trusted Computing Base (TCB) and providing stronger assurances. However, identifying which code should reside in TEEs is complex and requires specialized expertise, which is not supported by current automated tools. Existing solutions often migrate entire applications to TEEs, leading to suboptimal use and an increased TCB. To address this gap, we propose Code Annotation Logic (CAL), a pioneering tool that automatically identifies security sensitive components for TEE isolation. CAL analyzes codebases, leveraging a graph-based approach with novel feature construction and employing a custom graph neural network model to accurately determine which parts of the code should be isolated. CAL effectively optimizes TCB, reducing the burden of manual analysis and enhancing overall security. Our contributions include the definition of security sensitive code, the construction and labeling of a comprehensive dataset of source files, a feature rich graph based data preparation pipeline, and the CAL model for TEE integration. Evaluation results demonstrate CAL&#x27;s efficacy in identifying sensitive code with a recall of 86.05%, an F1 score of 81.56%, and an identification rate of 91.59% for security sensitive functions. By enabling efficient code isolation, CAL advances the secure development of applications using TEEs, offering a practical solution for developers to reduce attack vectors.

  匹配依据：TEE: intel sgx, trusted execution environments, trustzone

  </details>

- **TEESlice: Protecting Sensitive Neural Network Models in Trusted Execution Environments When Attackers have Pre-Trained Models**
  2024-11-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.09945)
  Ding Li, Ziqi Zhang, Mengyu Yao, Yifeng Cai, Yao Guo, Xiangqun Chen

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEE) are used to safeguard on-device models. However, directly employing TEEs to secure the entire DNN model is challenging due to the limited computational speed. Utilizing GPU can accelerate DNN&#x27;s computation speed but commercial widely-available GPUs usually lack security protection. To this end, scholars introduce TSDP, a method that protects privacy-sensitive weights within TEEs and offloads insensitive weights to GPUs. Nevertheless, current methods do not consider the presence of a knowledgeable adversary who can access abundant publicly available pre-trained models and datasets. This paper investigates the security of existing methods against such a knowledgeable adversary and reveals their inability to fulfill their security promises. Consequently, we introduce a novel partition before training strategy, which effectively separates privacy-sensitive weights from other components of the model. Our evaluation demonstrates that our approach can offer full model protection with a computational cost reduced by a factor of 10. In addition to traditional CNN models, we also demonstrate the scalability to large language models. Our approach can compress the private functionalities of the large language model to lightweight slices and achieve the same level of protection as the shielding-whole-model baseline.

  匹配依据：TEE: trusted execution environments

  </details>

- **Obfuscation as Instruction Decorrelation**
  2024-11-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.05570)
  Ali Ajorian, Erick Lavoie, Christian Tschudin

  <details><summary>摘要 / Abstract</summary>

  Obfuscation of computer programs has historically been approached either as a practical but \textit{ad hoc} craft to make reverse engineering subjectively difficult, or as a sound theoretical investigation unfortunately detached from the numerous existing constraints of engineering practical systems. In this paper, we propose \textit{instruction decorrelation} as a new approach that makes the instructions of a set of real-world programs appear independent from one another. We contribute: a formal definition of \textit{instruction independence} with multiple instantiations for various aspects of programs; a combination of program transformations that meet the corresponding instances of instruction independence against an honest-but-curious adversary, specifically random interleaving and memory access obfuscation; and an implementation of an interpreter that uses a trusted execution environment (TEE) only to perform memory address translation and memory shuffling, leaving instructions execution outside the TEE. These first steps highlight the practicality of our approach. Combined with additional techniques to protect the content of memory and to hopefully lower the requirements on TEEs, this work could potentially lead to more secure obfuscation techniques that could execute on commonly available hardware.

  匹配依据：TEE: trusted execution environment

  </details>

- **PipeLLM: Fast and Confidential Large Language Model Services with Speculative Pipelined Encryption**
  2024-11-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.03357)
  Yifan Tan, Cheng Tan, Zeyu Mi, Haibo Chen

  <details><summary>摘要 / Abstract</summary>

  Confidential computing on GPUs, like NVIDIA H100, mitigates the security risks of outsourced Large Language Models (LLMs) by implementing strong isolation and data encryption. Nonetheless, this encryption incurs a significant performance overhead, reaching up to 52.8 percent and 88.2 percent throughput drop when serving OPT-30B and OPT-66B, respectively. To address this challenge, we introduce PipeLLM, a user-transparent runtime system. PipeLLM removes the overhead by overlapping the encryption and GPU computation through pipelining - an idea inspired by the CPU instruction pipelining - thereby effectively concealing the latency increase caused by encryption. The primary technical challenge is that, unlike CPUs, the encryption module lacks prior knowledge of the specific data needing encryption until it is requested by the GPUs. To this end, we propose speculative pipelined encryption to predict the data requiring encryption by analyzing the serving patterns of LLMs. Further, we have developed an efficient, low-cost pipeline relinquishing approach for instances of incorrect predictions. Our experiments on NVIDIA H100 GPU show that compared with vanilla systems without confidential computing (e.g., vLLM, PEFT, and FlexGen), PipeLLM incurs modest overhead (less than 19.6 percent in throughput) across various LLM sizes, from 13B to 175B.

  匹配依据：TEE: confidential computing

  </details>

- **BlindexTEE: A Blind Index Approach towards TEE-supported End-to-end Encrypted DBMS**
  2024-11-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.02084)
  Louis Vialar, Jämes Ménétrey, Valerio Schiavoni, Pascal Felber

  <details><summary>摘要 / Abstract</summary>

  Using cloud-based applications comes with privacy implications, as the end-user looses control over their data. While encrypting all data on the client is possible, it largely reduces the usefulness of database management systems (DBMS) that are typically built to efficiently query large quantities of data. We present BlindexTEE, a new component that sits between the application business-logic and the database. BlindexTEE is shielded from malicious users or compromised environments by executing inside an SEV-SNP confidential VM, AMD&#x27;s trusted execution environment (TEE). BlindexTEE is in charge of end-to-end encryption of user data while preserving the ability of the DBMS to efficiently filter data. By decrypting and re-encrypting data, it builds blind indices, used later on to efficiently query the DBMS. We demonstrate the practicality of BlindexTEE with MySQL in several micro- and macro-benchmarks, achieving overheads between 36.1% and 462% over direct database access depending on the usage scenario.

  匹配依据：TEE: sev snp, trusted execution environment

  </details>

- **RA-WEBs: Remote Attestation for WEB services**
  2024-11-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.01340)
  Kosei Akama, Yoshimichi Nakatsuka, Korry Luke, Masaaki Sato, Keisuke Uehara

  <details><summary>摘要 / Abstract</summary>

  Data theft and leakage, caused by external adversaries and insiders, demonstrate the need for protecting user data. Trusted Execution Environments (TEEs) offer a promising solution by creating secure environments that protect data and code from such threats. The rise of confidential computing on cloud platforms facilitates the deployment of TEE-enabled server applications, which are expected to be widely adopted in web services such as privacy-preserving LLM inference and secure data logging. One key feature is Remote Attestation (RA), which enables integrity verification of a TEE. However, $\textit{compatibility}$ issues with RA verification arise as no browsers natively support this feature, making prior solutions cumbersome and risky. To address these challenges, we propose $\texttt{RA-WEBs}$ ($\textbf{R}$emote $\textbf{A}$ttestation for $\textbf{Web}$ $\textbf{s}$ervices), a novel RA protocol designed for high compatibility with the current web ecosystem. $\texttt{RA-WEBs}$ leverages established web mechanisms for immediate deployability, enabling RA verification on existing browsers. We conduct a comprehensive security analysis, demonstrating $\texttt{RA-WEBs}$&#x27;s resilience against various threats. Our contributions include the $\texttt{RA-WEBs}$ proposal, a proof-of-concept implementation, an in-depth security analysis, and publicly available code for reproducible research.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **Differentially Private Learned Indexes**
  2024-10-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.21164)
  Jianzhang Du, Tilak Mudgal, Rutvi Rahul Gadre, Yukui Luo, Chenghong Wang

  <details><summary>摘要 / Abstract</summary>

  In this paper, we address the problem of efficiently answering predicate queries on encrypted databases, those secured by Trusted Execution Environments (TEEs), which enable untrusted providers to process encrypted user data without revealing its contents. A common strategy in modern databases to accelerate predicate queries is the use of indexes, which map attribute values (keys) to their corresponding positions in a sorted data array. This allows for fast lookup and retrieval of data subsets that satisfy specific predicates. Unfortunately, indexes cannot be directly applied to encrypted databases due to strong data dependent leakages. Recent approaches apply differential privacy (DP) to construct noisy indexes that enable faster access to encrypted data while maintaining provable privacy guarantees. However, these methods often suffer from large storage costs, with index sizes typically scaling linearly with the key space. To address this challenge, we propose leveraging learned indexes, a trending technique that repurposes machine learning models as indexing structures, to build more compact DP indexes.

  匹配依据：TEE: trusted execution environments

  </details>

- **Lightweight, Secure and Stateful Serverless Computing with PSL**
  2024-10-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.20004)
  Alexander Thomas, Shubham Mishra, Kaiyuan Chen, John Kubiatowicz

  <details><summary>摘要 / Abstract</summary>

  We present PSL, a lightweight, secure and stateful Function-as-a-Serivce (FaaS) framework for Trusted Execution Environments (TEEs). The framework provides rich programming language support on heterogeneous TEE hardware for statically compiled binaries and/or WebAssembly (WASM) bytecodes, with a familiar Key-Value Store (KVS) interface to secure, performant, network-embedded storage. It achieves near-native execution speeds by utilizing the dynamic memory mapping capabilities of Intel SGX2 to create an in-enclave WASM runtime with Just-In-Time (JIT) compilation. PSL is designed to efficiently operate within an asynchronous environment with a distributed tamper-proof confidential storage system, assuming minority failures. The system exchanges eventually-consistent state updates across nodes while utilizing release-consistent locking mechanisms to enhance transactional capabilities. The execution of PSL is up to 3.7x faster than the state-of-the-art SGX WASM runtime. PSL reaches 95k ops/s with YCSB 100% read workload and 89k ops/s with 50% read/write workload. We demonstrate the scalability and adaptivity of PSL through a case study of secure and distributed training of deep neural networks.

  匹配依据：TEE: sgx, trusted execution environments

  </details>

- **MVVM: Deploy Your AI Agents-Securely, Efficiently, Everywhere**
  2024-10-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.15894)
  Yiwei Yang, Aibo Hu, Yusheng Zheng, Brian Zhao, Xinqi Zhang, Dawei Xiang, Kexin Chu, Wei Zhang, Andi Quinn

  <details><summary>摘要 / Abstract</summary>

  The rise of AI agents powered by Large Language Models (LLMs) presents critical challenges: how to securely execute and migrate these agents across heterogeneous environments while protecting sensitive user data, maintaining availability during network failures, minimizing response latency for time-critical decisions, and ensuring output safety in mission-critical applications. We present MVVM, a WebAssembly-based secure container framework that enables transparent live migration of LLM agent workspaces between edge devices and cloud servers with end-to-end privacy guarantees, resilient multi-tier replication, speculative execution for latency optimization, and integrated validation for safety assurance. MVVM introduces two key innovations: (1) a two-way sandboxing framework leveraging hardware enclaves and accelerator extensions that protects both the agent from malicious hosts and the host from compromised agents; (2) an efficient cross platform migration mechanism using WebAssembly and WASI&#x27;s platform-agnostic design, enabling seamless movement across ARM phones, RISC-V MCUs, x86 servers, and heterogeneous accelerators; and three astonishing use cases: (1) privacy-aware daemon that automatically determines whether to execute locally or remotely based on data sensitivity and resource availability; (2) multi-tier replication with intelligent quality degradation that maintains service availability despite network failures or resource constraints; (3) a comprehensive execution framework combining speculative execution for 10x latency reduction with parallel validation that ensures output safety without compromising responsiveness. Our evaluation demonstrates that MVVM is validated on three separate devices across 18 workloads.

  匹配依据：TEE: hardware enclaves

  </details>

- **Fastrack: Fast IO for Secure ML using GPU TEEs**
  2024-10-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.15240)
  Yongqin Wang, Rachit Rajat, Jonghyun Lee, Tingting Tang, Murali Annavaram

  <details><summary>摘要 / Abstract</summary>

  As cloud-based ML expands, ensuring data security during training and inference is critical. GPU-based Trusted Execution Environments (TEEs) offer secure, high-performance solutions, with CPU TEEs managing data movement and GPU TEEs handling authentication and computation. However, CPU-to-GPU communication overheads significantly hinder performance, as data must be encrypted, authenticated, decrypted, and verified, increasing costs by 12.69 to 33.53 times. This results in GPU TEE inference becoming 54.12% to 903.9% slower and training 10% to 455% slower than non-TEE systems, undermining GPU TEE advantages in latency-sensitive applications. This paper analyzes Nvidia H100 TEE protocols and identifies three key overheads: 1) redundant CPU re-encryption, 2) limited authentication parallelism, and 3) unnecessary operation serialization. We propose Fastrack, optimizing with 1) direct GPU TEE communication, 2) parallelized authentication, and 3) overlapping decryption with PCI-e transmission. These optimizations cut communication costs and reduce inference/training runtime by up to 84.6%, with minimal overhead compared to non-TEE systems.

  匹配依据：TEE: trusted execution environments

  </details>

- **HADES: Range-Filtered Private Aggregation on Public Data**
  2024-10-18 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1699)
  Xiaoyuan Liu, Ni Trieu, Trinabh Gupta, Ishtiyaque Ahmad, Dawn Song

  <details><summary>摘要 / Abstract</summary>

  In aggregation queries, predicate parameters often reveal user intent. Protecting these parameters is critical for user privacy, regardless of whether the database is public or private. While most existing works focus on private data settings, we address a public data setting where the server has access to the database. Current solutions for this setting either require additional setups (e.g., noncolluding servers, hardware enclaves) or are inefficient for practical workloads. Furthermore, they often do not support range predicates or boolean combinations commonly seen in real-world use cases. To address these limitations, we built HADES, a fully homomorphic encryption (FHE) based private aggregation system for public data that supports point, range predicates, and boolean combinations. Our one-round HADES protocol efficiently generates predicate indicators by leveraging the plaintext form of public data records. It introduces a novel elementwise-mapping operation and an optimized reduction algorithm, achieving latency efficiency within a limited noise budget. Our highly scalable, multi-threaded implementation improves performance over previous one-round FHE solutions by 204x to 6574x on end-to-end TPC-H queries, reducing aggregation time on 1M records from 15 hours to 38 seconds

  匹配依据：TEE: hardware enclaves

  </details>

- **Privacy-Preserving Decentralized AI with Confidential Computing**
  2024-10-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.13752)
  Dayeol Lee, Jorge António, Hisham Khan

  <details><summary>摘要 / Abstract</summary>

  This paper addresses privacy protection in decentralized Artificial Intelligence (AI) using Confidential Computing (CC) within the Atoma Network, a decentralized AI platform designed for the Web3 domain. Decentralized AI distributes AI services among multiple entities without centralized oversight, fostering transparency and robustness. However, this structure introduces significant privacy challenges, as sensitive assets such as proprietary models and personal data may be exposed to untrusted participants. Cryptography-based privacy protection techniques such as zero-knowledge machine learning (zkML) suffers prohibitive computational overhead. To address the limitation, we propose leveraging Confidential Computing (CC). Confidential Computing leverages hardware-based Trusted Execution Environments (TEEs) to provide isolation for processing sensitive data, ensuring that both model parameters and user data remain secure, even in decentralized, potentially untrusted environments. While TEEs face a few limitations, we believe they can bridge the privacy gap in decentralized AI. We explore how we can integrate TEEs into Atoma&#x27;s decentralized framework.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **ZONIA: a Zero-Trust Oracle System for Blockchain IoT Applications**
  2024-10-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.10532)
  Lorenzo Gigli, Ivan Zyrianoff, Federico Montori, Luca Sciullo, Carlos Kamienski, Marco Di Felice

  <details><summary>摘要 / Abstract</summary>

  The rapid expansion of the Internet of Things (IoT) has led to significant data reliability and system transparency challenges, aggravated by the centralized nature of existing IoT architectures. This centralization often results in siloed data ecosystems, where interoperability issues and opaque data handling practices compromise both the utility and trustworthiness of IoT applications. To address these issues, we introduce ZONIA (Zero-trust Oracle Network for IoT Applications), a novel blockchain oracle system designed to enhance data integrity and decentralization in IoT environments. Unlike traditional approaches that rely on Trusted Execution Environments and centralized data sources, ZONIA utilizes a decentralized, zero-trust model that allows for anonymous participation and integrates multiple data sources to ensure fairness and reliability. This paper outlines ZONIA&#x27;s architecture, which supports semantic and geospatial queries, details its data reliability mechanisms, and presents a comprehensive evaluation demonstrating its scalability and resilience against data falsification and collusion attacks. Both analytical and experimental results demonstrate ZONIA&#x27;s scalability, showcasing its feasibility to handle an increasing number of nodes in the system under different system conditions and workloads. Furthermore, the implemented reputation mechanism significantly enhances data accuracy, maintaining high reliability even when 40\% of nodes exhibit malicious behavior.

  匹配依据：TEE: trusted execution environments

  </details>

- **Sharing without Showing: Secure Cloud Analytics with Trusted Execution Environments**
  2024-10-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.10574)
  Marcus Birgersson, Cyrille Artho, Musard Balliu

  <details><summary>摘要 / Abstract</summary>

  Many applications benefit from computations over the data of multiple users while preserving confidentiality. We present a solution where multiple mutually distrusting users&#x27; data can be aggregated with an acceptable overhead, while allowing users to be added to the system at any time without re-encrypting data. Our solution to this problem is to use a Trusted Execution Environment (Intel SGX) for the computation, while the confidential data is encrypted with the data owner&#x27;s key and can be stored anywhere, without trust in the service provider. We do not require the user to be online during the computation phase and do not require a trusted party to store data in plain text. Still, the computation can only be carried out if the data owner explicitly has given permission. Experiments using common functions such as the sum, least square fit, histogram, and SVM classification, exhibit an average overhead of $1.6 \times$. In addition to these performance experiments, we present a use case for computing the distributions of taxis in a city without revealing the position of any other taxi to the other parties.

  匹配依据：TEE: intel sgx, trusted execution environment, trusted execution environments

  </details>

- **Quantum Operating System Support for Quantum Trusted Execution Environments**
  2024-10-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.08486)
  Theodoros Trochatos, Jakub Szefer

  <details><summary>摘要 / Abstract</summary>

  With the growing reliance on cloud-based quantum computing, ensuring the confidentiality and integrity of quantum computations is paramount. Quantum Trusted Execution Environments (QTEEs) have been proposed to protect users&#x27; quantum circuits when they are submitted to remote cloud-based quantum computers. However, deployment of QTEEs necessitates a Quantum Operating Systems (QOS) that can support QTEEs hardware and operation. This work introduces the first architecture for a QOS to support and enable essential steps required for secure quantum task execution on cloud platforms.

  匹配依据：TEE: trusted execution environments

  </details>

- **Federated Learning in Practice: Reflections and Projections**
  2024-10-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.08892)
  Katharine Daly, Hubert Eichner, Peter Kairouz, H. Brendan McMahan, Daniel Ramage, Zheng Xu

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) is a machine learning technique that enables multiple entities to collaboratively learn a shared model without exchanging their local data. Over the past decade, FL systems have achieved substantial progress, scaling to millions of devices across various learning domains while offering meaningful differential privacy (DP) guarantees. Production systems from organizations like Google, Apple, and Meta demonstrate the real-world applicability of FL. However, key challenges remain, including verifying server-side DP guarantees and coordinating training across heterogeneous devices, limiting broader adoption. Additionally, emerging trends such as large (multi-modal) models and blurred lines between training, inference, and personalization challenge traditional FL frameworks. In response, we propose a redefined FL framework that prioritizes privacy principles rather than rigid definitions. We also chart a path forward by leveraging trusted execution environments and open-source ecosystems to address these challenges and facilitate future advancements in FL.

  匹配依据：TEE: trusted execution environments

  </details>

- **Fortify Your Foundations: Practical Privacy and Security for Foundation Model Deployments In The Cloud**
  2024-10-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.05930)
  Marcin Chrapek, Anjo Vahldiek-Oberwagner, Marcin Spoczynski, Scott Constable, Mona Vij, Torsten Hoefler

  <details><summary>摘要 / Abstract</summary>

  Foundation Models (FMs) display exceptional performance in tasks such as natural language processing and are being applied across a growing range of disciplines. Although typically trained on large public datasets, FMs are often fine-tuned or integrated into Retrieval-Augmented Generation (RAG) systems, which rely on private data. This access, along with their size and costly training, heightens the risk of intellectual property theft. Moreover, multimodal FMs may expose sensitive information. In this work, we examine the FM threat model and discuss the practicality and comprehensiveness of various approaches for securing against them, such as ML-based methods and trusted execution environments (TEEs). We demonstrate that TEEs offer an effective balance between strong security properties, usability, and performance. Specifically, we present a solution achieving less than 10\% overhead versus bare metal for the full Llama2 7B and 13B inference pipelines running inside \intel\ SGX and \intel\ TDX. We also share our configuration files and insights from our implementation. To our knowledge, our work is the first to show the practicality of TEEs for securing FMs.

  匹配依据：TEE: intel sgx, intel tdx, trusted execution environments

  </details>

- **CONFINE: Preserving Data Secrecy in Decentralized Process Mining**
  2024-10-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.04453)
  Valerio Goretti, Davide Basile, Luca Barbaro, Claudio Di Ciccio

  <details><summary>摘要 / Abstract</summary>

  In the contemporary business landscape, collaboration across multiple organizations offers a multitude of opportunities, including reduced operational costs, enhanced performance, and accelerated technological advancement. The application of process mining techniques in an inter-organizational setting, exploiting the recorded process event data, enables the coordination of joint effort and allows for a deeper understanding of the business. Nevertheless, considerable concerns pertaining to data confidentiality emerge, as organizations frequently demonstrate a reluctance to expose sensitive data demanded for process mining, due to concerns related to privacy and security risks. The presence of conflicting interests among the parties involved can impede the practice of open data sharing. To address these challenges, we propose our approach and toolset named CONFINE, which we developed with the intent of enabling process mining on process event data from multiple providers while preserving the confidentiality and integrity of the original records. To ensure that the presented interaction protocol steps are secure and that the processed information is hidden from both involved and external actors, our approach is based on a decentralized architecture and consists of trusted applications running in Trusted Execution Environments (TEE). In this demo paper, we provide an overview of the core components and functionalities as well as the specific details of its application.

  匹配依据：TEE: trusted execution environments

  </details>

- **OML: Open, Monetizable, and Loyal AI**
  2024-10-05 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1573)
  Zerui Cheng, Edoardo Contente, Ben Finch, Oleg Golev, Jonathan Hayase, Andrew Miller, Niusha Moshrefi, Anshul Nasery, Sandeep Nailwal, Sewoong Oh, Himanshu Tyagi, Pramod Viswanath

  <details><summary>摘要 / Abstract</summary>

  Artificial Intelligence (AI) has steadily improved across a wide range of tasks, and a significant breakthrough towards general intelligence was achieved with the rise of generative deep models, which have garnered worldwide attention. However, the development and deployment of AI are almost entirely controlled by a few powerful organizations and individuals who are racing to create Artificial General Intelligence (AGI). These centralized entities make decisions with little public oversight, shaping the future of humanity, often with unforeseen consequences. In this paper, we propose OML, which stands for Open, Monetizable, and Loyal AI, an approach designed to democratize AI development and shift control away from these monopolistic actors. OML is realized through an interdisciplinary framework spanning AI, blockchain, and cryptography. We present several ideas for constructing OML systems using technologies such as Trusted Execution Environments (TEE), traditional cryptographic primitives like fully homomorphic encryption and functional encryption, obfuscation, and AI-native solutions rooted in the sample complexity and intrinsic hardness of AI tasks. A key innovation of our work is the introduction of a new scientific field: AI-native cryptography, which leverages cryptographic primitives tailored to AI applications. Unlike conventional cryptography, which focuses on discrete data and binary security guarantees, AI-native cryptography exploits the continuous nature of AI data representations and their low-dimensional manifolds, focusing on improving approximate performance. One core idea is to transform AI attack methods, such as data poisoning, into security tools. This novel approach serves as a foundation for OML 1.0, an implemented system that demonstrates the practical viability of AI-native cryptographic techniques. At the heart of OML 1.0 is the concept of model fingerprinting, a novel AI-native cryptographic primitive that helps protect the integrity and ownership of AI models. The spirit of OML is to establish a decentralized, open, and transparent platform for AI development, enabling the community to contribute, monetize, and take ownership of AI models. By decentralizing control and ensuring transparency through blockchain technology, OML prevents the concentration of power and provides accountability in AI development that has not been possible before. To the best of our knowledge, this paper is the first to: • Identify the monopolization and lack of transparency challenges in AI deployment today and formulate the challenge as OML (Open, Monetizable, Loyal). • Provide an interdisciplinary approach to solving the OML challenge, incorporating ideas from AI, blockchain, and cryptography. • Introduce and formally define the new scientific field of AI-native cryptography. • Develop novel AI-native cryptographic primitives and implement them in OML 1.0, analyzing their security and effectiveness. • Leverage blockchain technology to host OML solutions, ensuring transparency, decentralization, and alignment with the goals of democratized AI development. Through OML, we aim to provide a decentralized framework for AI development that prioritizes open collaboration, ownership rights, and transparency, ultimately fostering a more inclusive AI ecosystem.

  匹配依据：TEE: trusted execution environments

  </details>

- **An Edge-Computing based Industrial Gateway for Industry 4.0 using ARM TrustZone Technology**
  2024-10-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.02529)
  Sandeep Gupta

  <details><summary>摘要 / Abstract</summary>

  Secure and efficient communication to establish a seamless nexus between the five levels of a typical automation pyramid is paramount to Industry 4.0. Specifically, vertical and horizontal integration of these levels is an overarching requirement to accelerate productivity and improve operational activities. Vertical integration can improve visibility, flexibility, and productivity by connecting systems and applications. Horizontal integration can provide better collaboration and adaptability by connecting internal production facilities, multi-site operations, and third-party partners in a supply chain. In this paper, we propose an Edge-computing-based Industrial Gateway for interfacing information technology and operational technology that can enable Industry 4.0 vertical and horizontal integration. Subsequently, we design and develop a working prototype to demonstrate a remote production-line maintenance use case with a strong focus on security aspects and the edge paradigm to bring computational resources and data storage closer to data sources.

  匹配依据：TEE: trustzone

  </details>

- **KeyVisor -- A Lightweight ISA Extension for Protected Key Handles with CPU-enforced Usage Policies**
  2024-10-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.01777)
  Fabian Schwarz, Jan Philipp Thoma, Christian Rossow, Tim Güneysu

  <details><summary>摘要 / Abstract</summary>

  The confidentiality of cryptographic keys is essential for the security of protection schemes used for communication, file encryption, and outsourced computation. Beyond cryptanalytic attacks, adversaries can steal keys from memory via software exploits or side channels, enabling them to, e.g., tamper with secrets or impersonate key owners. Therefore, existing defenses protect keys in dedicated devices or isolated memory, or store them only in encrypted form. However, these designs often provide unfavorable tradeoffs, sacrificing performance, fine-grained access control, or deployability. In this paper, we present KeyVisor, a lightweight ISA extension that securely offloads the handling of cryptographic keys to the CPU. KeyVisor provides CPU instructions that enable applications to request protected key handles and perform AEAD cipher operations on them. The underlying keys are accessible only by KeyVisor, and thus never leak to memory. KeyVisor&#x27;s direct CPU integration enables fast crypto operations and hardware-enforced key usage restrictions, e.g., keys usable only for de-/encryption, with a limited lifetime, or with a process binding. Furthermore, privileged software, e.g., the monitor firmware of TEEs, can revoke keys or bind them to a specific process/TEE. We implement KeyVisor for RISC-V based on Rocket Chip, evaluate its performance, and demonstrate real-world use cases, including key-value databases, automotive feature licensing, and a read-only network middlebox.

  匹配依据：TEE: tees (context)

  </details>

- **TRACES: TEE-based Runtime Auditing for Commodity Embedded Systems**
  2024-09-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.19125)
  Adam Caulfield, Antonio Joia Neto, Norrathep Rattanavipanon, Ivan De Oliveira Nunes

  <details><summary>摘要 / Abstract</summary>

  Control Flow Attestation (CFA) offers a means to detect control flow hijacking attacks on remote devices, enabling verification of their runtime trustworthiness. CFA generates a trace (CFLog) containing the destination of all branching instructions executed. This allows a remote Verifier (Vrf) to inspect the execution control flow on a potentially compromised Prover (Prv) before trusting that a value/action was correctly produced/performed by Prv. However, while CFA can be used to detect runtime compromises, it cannot guarantee the eventual delivery of the execution evidence (CFLog) to Vrf. In turn, a compromised Prv may refuse to send CFLog to Vrf, preventing its analysis to determine the exploit&#x27;s root cause and appropriate remediation actions. In this work, we propose TRACES: TEE-based Runtime Auditing for Commodity Embedded Systems. TRACES guarantees reliable delivery of periodic runtime reports even when Prv is compromised. This enables secure runtime auditing in addition to best-effort delivery of evidence in CFA. TRACES also supports a guaranteed remediation phase, triggered upon compromise detection to ensure that identified runtime vulnerabilities can be reliably patched. To the best of our knowledge, TRACES is the first system to provide this functionality on commodity devices (i.e., without requiring custom hardware modifications). To that end, TRACES leverages support from the ARM TrustZone-M Trusted Execution Environment (TEE). To assess practicality, we implement and evaluate a fully functional (open-source) prototype of TRACES atop the commodity ARM Cortex-M33 micro-controller unit.

  匹配依据：TEE: trusted execution environment, trustzone

  </details>

- **SpecCFA: Enhancing Control Flow Attestation/Auditing via Application-Aware Sub-Path Speculation**
  2024-09-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.18403)
  Adam Caulfield, Liam Tyler, Ivan De Oliveira Nunes

  <details><summary>摘要 / Abstract</summary>

  At the edge of modern cyber-physical systems, Micro-Controller Units (MCUs) are responsible for safety-critical sensing/actuation. However, MCU cost constraints rule out the usual security mechanisms of general-purpose computers. Thus, various low-cost security architectures have been proposed to remotely verify MCU software integrity. Control Flow Attestation (CFA) enables a Verifier (Vrf) to remotely assess the run-time behavior of a prover MCU (Prv), generating an authenticated trace of all of Prv control flow transfers (CFLog). Further, Control Flow Auditing architectures augment CFA by guaranteeing the delivery of evidence to Vrf. Unfortunately, a limitation of existing CFA lies in the cost to store and transmit CFLog, as even simple MCU software may generate large traces. Given these issues, prior work has proposed static (context-insensitive) optimizations. However, they do not support configurable program-specific optimizations. In this work, we note that programs may produce unique predictable control flow sub-paths and argue that program-specific predictability can be leveraged to dynamically optimize CFA while retaining all security guarantees. Therefore, we propose SpecCFA: an approach for dynamic sub-path speculation in CFA. SpecCFA allows Vrf to securely speculate on likely control flow sub-paths for each attested program. At run-time, when a sub-path in CFLog matches a pre-defined speculation, the entire sub-path is replaced by a reserved symbol. SpecCFA can speculate on multiple variable-length control flow sub-paths simultaneously. We implement SpecCFA atop two open-source control flow auditing architectures: one based on a custom hardware design and one based on a commodity Trusted Execution Environment (ARM TrustZone-M). In both cases, SpecCFA significantly lowers storage/performance costs that are critical to resource-constrained MCUs.

  匹配依据：TEE: trusted execution environment, trustzone

  </details>

- **Confidential Prompting: Privacy-preserving LLM Inference on Cloud**
  2024-09-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.19134)
  Caihua Li, In Gim, Lin Zhong

  <details><summary>摘要 / Abstract</summary>

  This paper introduces a vision of confidential prompting: securing user prompts from an untrusted, cloud-hosted large language model (LLM) while preserving model confidentiality, output invariance, and compute efficiency. As a first step toward this vision, we present Petridish, a system built on top of confidential computing and its core contribution, a novel technology called Secure Partitioned Decoding (SPD). Petridish runs the LLM service inside a confidential virtual machine (CVM), which protects the secrets, i.e., the LLM parameters and user prompts, from adversaries outside the CVM. Importantly, it splits the LLM service for a user into two processes, using SPD: a per-user process performs prefill with the user prompts and computes attention scores during decoding; a service process, shared by all users, batches the attention scores from per-user processes and generates output tokens for all users. Both the LLM provider and the users trust Petridish&#x27;s CVM and its operating system, which guarantees isolation between processes and limits their outbound network capabilities to control information flow. The CVM&#x27;s attestation capability and its open-source software stack enable Petridish to provide auditable protection of both user prompt and LLM confidentiality. Together, Petridish maintains full utility of LLM service and enables practical, privacy-preserving cloud-hosted LLM inference for sensitive applications, such as processing personal data, clinical records, and financial documents.

  匹配依据：TEE: confidential computing

  </details>

- **TeeRollup: Efficient Rollup Design Using Heterogeneous TEE**
  2024-09-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.14647)
  Xiaoqing Wen, Quanbi Feng, Hanzheng Lyu, Jianyu Niu, Yinqian Zhang, Chen Feng

  <details><summary>摘要 / Abstract</summary>

  Rollups have emerged as a promising approach to improving blockchains&#x27; scalability by offloading transactions execution off-chain. Existing rollup solutions either leverage complex zero-knowledge proofs or optimistically assume execution correctness unless challenged. However, these solutions suffer from high gas costs and significant withdrawal delays, hindering their adoption in decentralized applications. This paper introduces TEERollup, an efficient rollup protocol that leverages Trusted Execution Environments (TEEs) to achieve both low gas costs and short withdrawal delays. Sequencers (system participants) execute transactions within TEEs and upload signed execution results to the blockchain with confidential keys of TEEs. Unlike most TEE-assisted blockchain designs, TEERollup adopts a practical threat model where the integrity and availability of TEEs may be compromised. To address these issues, we first introduce a distributed system of sequencers with heterogeneous TEEs, ensuring system security even if a certain proportion of TEEs are compromised. Second, we propose a challenge mechanism to solve the redeemability issue caused by TEE unavailability. Furthermore, TEERollup incorporates Data Availability Providers (DAPs) to reduce on-chain storage overhead and uses a laziness penalty mechanism to regulate DAP behavior. We implement a prototype of TEERollup in Golang, using the Ethereum test network, Sepolia. Our experimental results indicate that TEERollup outperforms zero-knowledge rollups (ZK-rollups), reducing on-chain verification costs by approximately 86% and withdrawal delays to a few minutes.

  匹配依据：TEE: trusted execution environments

  </details>

- **MECURY: Practical Cross-Chain Exchange via Trusted Hardware**
  2024-09-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.14640)
  Xiaoqing Wen, Quanbi Feng, Jianyu Niu, Yinqian Zhang, Chen Feng

  <details><summary>摘要 / Abstract</summary>

  The proliferation of blockchain-backed cryptocurrencies has sparked the need for cross-chain exchanges of diverse digital assets. Unfortunately, current exchanges suffer from high on-chain verification costs, weak threat models of central trusted parties, or synchronous requirements, making them impractical for currency trading applications. In this paper, we present MERCURY, a practical cryptocurrency exchange that is trust-minimized and efficient without online-client requirements. MERCURY leverages Trusted Execution Environments (TEEs) to shield participants from malicious behaviors, eliminating the reliance on trusted participants and making on-chain verification efficient. Despite the simple idea, building a practical TEE-assisted cross-chain exchange is challenging due to the security and unavailability issues of TEEs. MERCURY tackles the unavailability problem of TEEs by implementing an efficient challenge-response mechanism executed on smart contracts. Furthermore, MERCURY utilizes a lightweight transaction verification mechanism and adopts multiple optimizations to reduce on-chain costs. Comparative evaluations with XClaim, ZK-bridge, and Tesseract demonstrate that MERCURY significantly reduces on-chain costs by approximately 67.87%, 45.01%, and 47.70%, respectively.

  匹配依据：TEE: trusted execution environments

  </details>

- **Ditto: Elastic Confidential VMs with Secure and Dynamic CPU Scaling**
  2024-09-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.15542)
  Shixuan Zhao, Mengyuan Li, Mengjia Yan, Zhiqiang Lin

  <details><summary>摘要 / Abstract</summary>

  Confidential Virtual Machines (CVMs) are a type of VMbased Trusted Execution Environments (TEEs) designed to enhance the security of cloud-based VMs, safeguarding them even from malicious hypervisors. Although CVMs have been widely adopted by major cloud service providers, current CVM designs face significant challenges in runtime resource management due to their fixed capacities and lack of transparency. These limitations hamper efficient cloud resource management, leading to increased operational costs and reduced agility in responding to fluctuating workloads. This paper introduces a dynamic CPU resource management approach, featuring the novel concept of &quot;Elastic CVM. This approach allows for hypervisor-assisted runtime adjustment of CPU resources using a specialized vCPU type, termed Worker vCPU. This new approach enhances CPU resource adaptability and operational efficiency without compromising security. Additionally, we introduce a Worker vCPU Abstraction Layer to simplify Worker vCPU deployment and management. To demonstrate the effectiveness of our approach, we have designed and implemented a serverless computing prototype platform, called Ditto. We show that Ditto significantly improves performance and efficiency through finergrain resource management. The concept of &quot;Elastic CVM&quot; and the Worker vCPU design not only optimize cloud resource utilization but also pave the way for more flexible and cost-effective confidential computing environments.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **Unlocking the Power of Environment Assumptions for Unit Proofs**
  2024-09-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.12269)
  Siddharth Priya, Temesghen Kahsai, Arie Gurfinkel

  <details><summary>摘要 / Abstract</summary>

  Clearly articulating the assumptions of the execution environment is crucial for the successful application of code-level formal verification. The process of specifying a model for the environment can be both laborious and error-prone, often requiring domain experts. In contrast, when engineers write unit tests, they frequently employ mocks (tMocks) to define the expected behavior of the environment in which the function under test operates. These tMocks describe how the environment behaves, e.g., the return types of an external API call (stateless behaviour) or the correct sequence of function calls (stateful behaviour). Mocking frameworks have proven to be highly effective tools for crafting unit tests. In our work, we draw inspiration from tMocks and introduce their counterpart in the realm of formal verification, which we term vMocks. vMocks offer an intuitive framework for specifying a plausible environment when conducting code-level formal verification. We implement a vMock library for the verification of C programs called SEAMOCK. We investigate the practicality of vMocks by, first, comparing specifications styles in the communication layer of the Android Trusty Trusted Execution Environment (TEE) open source project, and second, in the verification of mbedTLS, a widely used open source C library that provides secure communication protocols and cryptography primitives for embedded systems. Based on our experience, we conclude that vMocks complement other forms of environment models. We believe that vMocks ease adoption of code-level formal verification among developers already familiar with tMocks.

  匹配依据：TEE: trusted execution environment

  </details>

- **H$\_2$O$\_2$RAM: A High-Performance Hierarchical Doubly Oblivious RAM**
  2024-09-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.07167)
  Leqian Zheng, Zheng Zhang, Wentao Dong, Yao Zhang, Ye Wu, Cong Wang

  <details><summary>摘要 / Abstract</summary>

  The combination of Oblivious RAM (ORAM) with Trusted Execution Environments (TEE) has found numerous real-world applications due to their complementary nature. TEEs alleviate the performance bottlenecks of ORAM, such as network bandwidth and roundtrip latency, and ORAM provides general-purpose protection for TEE applications against attacks exploiting memory access patterns. The defining property of this combination, which sets it apart from traditional ORAM designs, is its ability to ensure that memory accesses, both inside and outside of TEEs, are made oblivious, thus termed doubly oblivious RAM (O$_2$RAM). Efforts to develop O$_2$RAM with enhanced performance are ongoing. In this work, we propose H$_2$O$_2$RAM, a high-performance doubly oblivious RAM construction. The distinguishing feature of our approach, compared to the existing tree-based doubly oblivious designs, is its first adoption of the hierarchical framework that enjoys inherently better data locality and parallelization. While the latest hierarchical solution, FutORAMa, achieves concrete efficiency in the classic client-server model by leveraging a relaxed assumption of sublinear-sized client-side private memory, adapting it to our scenario poses challenges due to the conflict between this relaxed assumption and our doubly oblivious requirement. To this end, we introduce several new efficient oblivious components to build a high-performance hierarchical O$_2$RAM (H$_2$O$_2$RAM). We implement our design and evaluate it on various scenarios. The results indicate that H$_2$O$_2$RAM reduces execution time by up to $\sim 10^3$ times and saves memory usage by $5\sim44$ times compared to state-of-the-art solutions.

  匹配依据：TEE: trusted execution environments

  </details>

- **Ciphertext Policy Attribute Based Encryption with Intel SGX**
  2024-09-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.07149)
  Vivek Suryawanshi, Shamik Sural

  <details><summary>摘要 / Abstract</summary>

  Modern computing environments demand robust security measures to protect sensitive data and resources. Ciphertext-Policy Attribute-Based Encryption (CP-ABE) is a well-established encryption technique known for its fine-grained access control capabilities. However, as the digital landscape evolves, there is a growing need to enhance the security of CP-ABE operations. We propose an approach that utilizes CP-ABE with Intel SGX. It allows data to be encrypted and decrypted securely within the SGX enclave based on the rules in policy by ensuring that only authorized users gain access. We evaluate its performance through different experiments by focusing on key parameters such as the number of rules, attributes and file size. Our results demonstrate the performance and scalability of integrating SGX with CP-ABE in enhancing data security with only minimal increase in execution time due to enclave overhead.

  匹配依据：TEE: intel sgx, sgx, sgx enclave

  </details>

- **The HitchHiker's Guide to High-Assurance System Observability Protection with Efficient Permission Switches**
  2024-09-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.04484)
  Chuqi Zhang, Jun Zeng, Yiming Zhang, Adil Ahmad, Fengwei Zhang, Hai Jin, Zhenkai Liang

  <details><summary>摘要 / Abstract</summary>

  Protecting system observability records (logs) from compromised OSs has gained significant traction in recent times, with several note-worthy approaches proposed. Unfortunately, none of the proposed approaches achieve high performance with tiny log protection delays. They also leverage risky environments for protection (\eg many use general-purpose hypervisors or TrustZone, which have large TCB and attack surfaces). HitchHiker is an attempt to rectify this problem. The system is designed to ensure (a) in-memory protection of batched logs within a short and configurable real-time deadline by efficient hardware permission switching, and (b) an end-to-end high-assurance environment built upon hardware protection primitives with debloating strategies for secure log protection, persistence, and management. Security evaluations and validations show that HitchHiker reduces log protection delay by 93.3--99.3% compared to the state-of-the-art, while reducing TCB by 9.4--26.9X. Performance evaluations show HitchHiker incurs a geometric mean of less than 6% overhead on diverse real-world programs, improving on the state-of-the-art approach by 61.9--77.5%.

  匹配依据：TEE: trustzone

  </details>

- **Confidential Computing on NVIDIA Hopper GPUs: A Performance Benchmark Study**
  2024-09-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.03992)
  Jianwei Zhu, Hang Yin, Peng Deng, Aline Almeida, Shunfan Zhou

  <details><summary>摘要 / Abstract</summary>

  This report evaluates the performance impact of enabling Trusted Execution Environments (TEE) on NVIDIA Hopper GPUs for large language model (LLM) inference tasks. We benchmark the overhead introduced by TEE mode across various LLMs and token lengths, with a particular focus on the bottleneck caused by CPU-GPU data transfers via PCIe. Our results indicate that while there is minimal computational overhead within the GPU, the overall performance penalty is primarily attributable to data transfer. For the majority of typical LLM queries, the overhead remains below 7%, with larger models and longer sequences experiencing nearly zero overhead.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **A First Look At Efficient And Secure On-Device LLM Inference Against KV Leakage**
  2024-09-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.04040)
  Huan Yang, Deyu Zhang, Yudong Zhao, Yuanchun Li, Yunxin Liu

  <details><summary>摘要 / Abstract</summary>

  Running LLMs on end devices has garnered significant attention recently due to their advantages in privacy preservation. With the advent of lightweight LLM models and specially designed GPUs, on-device LLM inference has achieved the necessary accuracy and performance metrics. However, we have identified that LLM inference on GPUs can leak privacy-sensitive intermediate information, specifically the KV pairs. An attacker could exploit these KV pairs to reconstruct the entire user conversation, leading to significant vulnerabilities. Existing solutions, such as Fully Homomorphic Encryption (FHE) and Trusted Execution Environments (TEE), are either too computation-intensive or resource-limited. To address these issues, we designed KV-Shield, which operates in two phases. In the initialization phase, it permutes the weight matrices so that all KV pairs are correspondingly permuted. During the runtime phase, the attention vector is inversely permuted to ensure the correctness of the layer output. All permutation-related operations are executed within the TEE, ensuring that insecure GPUs cannot access the original KV pairs, thus preventing conversation reconstruction. Finally, we theoretically analyze the correctness of KV-Shield, along with its advantages and overhead.

  匹配依据：TEE: trusted execution environments

  </details>

- **A Confidential Computing Transparency Framework for a Comprehensive Trust Chain**
  2024-09-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.03720)
  Ceren Kocaoğullar, Tina Marjanov, Ivan Petrov, Ben Laurie, Al Cutter, Christoph Kern, Alice Hutchings, Alastair R. Beresford

  <details><summary>摘要 / Abstract</summary>

  Confidential Computing enhances privacy of data in-use through hardware-based Trusted Execution Environments (TEEs) that use attestation to verify their integrity, authenticity, and certain runtime properties, along with those of the binaries they execute. However, TEEs require user trust, as attestation alone cannot guarantee the absence of vulnerabilities or backdoors. Enhanced transparency can mitigate the reliance on naive trust. Some organisations currently employ various transparency measures, including open-source firmware, publishing technical documentation, or undergoing external audits, but these require investments with unclear returns. This may discourage the adoption of transparency, leaving users with limited visibility into system privacy measures. Additionally, the lack of standardisation complicates meaningful comparisons between implementations. To address these challenges, we propose a three-level conceptual framework providing organisations with a practical pathway to incrementally improve Confidential Computing transparency. To evaluate whether our transparency framework contributes to an increase in end-user trust, we conducted an empirical study with over 800 non-expert participants. The results indicate that greater transparency improves user comfort, with participants willing to share various types of personal data across different levels of transparency. The study also reveals misconceptions about transparency, highlighting the need for clear communication and user education.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **VECA: Reliable and Confidential Resource Clustering for Volunteer Edge-Cloud Computing**
  2024-09-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.03057)
  Hemanth Sai Yeddulapalli, Mauro Lemus Alarcon, Upasana Roy, Roshan Lal Neupane, Durbek Gafurov, Motahare Mounesan, Saptarshi Debroy, Prasad Calyam

  <details><summary>摘要 / Abstract</summary>

  Volunteer Edge-Cloud (VEC) computing has a significant potential to support scientific workflows in user communities contributing volunteer edge nodes. However, managing heterogeneous and intermittent resources to support machine/deep learning (ML/DL) based workflows poses challenges in resource governance for reliability, and confidentiality for model/data privacy protection. There is a need for approaches to handle the volatility of volunteer edge node availability, and also to scale the confidential data-intensive workflow execution across a large number of VEC nodes. In this paper, we present VECA, a reliable and confidential VEC resource clustering solution featuring three-fold methods tailored for executing ML/DL-based scientific workflows on VEC resources. Firstly, a capacity-based clustering approach enhances system reliability and minimizes VEC node search latency. Secondly, a novel two-phase, globally distributed scheduling scheme optimizes job allocation based on node attributes and using time-series-based Recurrent Neural Networks. Lastly, the integration of confidential computing ensures privacy preservation of the scientific workflows, where model and data information are not shared with VEC resources providers. We evaluate VECA in a Function-as-a-Service (FaaS) cloud testbed that features OpenFaaS and MicroK8S to support two ML/DL-based scientific workflows viz., G2P-Deep (bioinformatics) and PAS-ML (health informatics). Results from tested experiments demonstrate that our proposed VECA approach outperforms state-of-the-art methods; especially VECA exhibits a two-fold reduction in VEC node search latency and over 20% improvement in productivity rates following execution failures compared to the next best method.

  匹配依据：TEE: confidential computing

  </details>

- **Obsidian: Cooperative State-Space Exploration for Performant Inference on Secure ML Accelerators**
  2024-09-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.02817)
  Sarbartha Banerjee, Shijia Wei, Prakash Ramrakhyani, Mohit Tiwari

  <details><summary>摘要 / Abstract</summary>

  Trusted execution environments (TEEs) for machine learning accelerators are indispensable in secure and efficient ML inference. Optimizing workloads through state-space exploration for the accelerator architectures improves performance and energy consumption. However, such explorations are expensive and slow due to the large search space. Current research has to use fast analytical models that forego critical hardware details and cross-layer opportunities unique to the hardware security primitives. While cycle-accurate models can theoretically reach better designs, their high runtime cost restricts them to a smaller state space. We present Obsidian, an optimization framework for finding the optimal mapping from ML kernels to a secure ML accelerator. Obsidian addresses the above challenge by exploring the state space using analytical and cycle-accurate models cooperatively. The two main exploration components include: (1) A secure accelerator analytical model, that includes the effect of secure hardware while traversing the large mapping state space and produce the best m model mappings; (2) A compiler profiling step on a cycle-accurate model, that captures runtime bottlenecks to further improve execution runtime, energy and resource utilization and find the optimal model mapping. We compare our results to a baseline secure accelerator, comprising of the state-of-the-art security schemes obtained from guardnn [ 33 ] and sesame [11]. The analytical model reduces the inference latency by 20.5% for a cloud and 8.4% for an edge deployment with an energy improvement of 24% and 19% respectively. The cycle-accurate model, further reduces the latency by 9.1% for a cloud and 12.2% for an edge with an energy improvement of 13.8% and 13.1%.

  匹配依据：TEE: trusted execution environments

  </details>

- **Privacy-Preserving Multimedia Mobile Cloud Computing Using Protective Perturbation**
  2024-09-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.01710)
  Zhongze Tang, Mengmei Ye, Yao Liu, Sheng Wei

  <details><summary>摘要 / Abstract</summary>

  Mobile cloud computing has been adopted in many multimedia applications, where the resource-constrained mobile device sends multimedia data (e.g., images) to remote cloud servers to request computation-intensive multimedia services (e.g., image recognition). While significantly improving the performance of the mobile applications, the cloud-based mechanism often causes privacy concerns as the multimedia data and services are offloaded from the trusted user device to untrusted cloud servers. Several recent studies have proposed perturbation-based privacy preserving mechanisms, which obfuscate the offloaded multimedia data to eliminate privacy exposures without affecting the functionality of the remote multimedia services. However, the existing privacy protection approaches require the deployment of computation-intensive perturbation generation on the resource-constrained mobile devices. Also, the obfuscated images are typically not compliant with the standard image compression algorithms and suffer from significant bandwidth consumption. In this paper, we develop a novel privacy-preserving multimedia mobile cloud computing framework, namely $PMC^2$, to address the resource and bandwidth challenges. $PMC^2$ employs secure confidential computing in the cloud to deploy the perturbation generator, which addresses the resource challenge while maintaining the privacy. Furthermore, we develop a neural compressor specifically trained to compress the perturbed images in order to address the bandwidth challenge. We implement $PMC^2$ in an end-to-end mobile cloud computing system, based on which our evaluations demonstrate superior latency, power efficiency, and bandwidth consumption achieved by $PMC^2$ while maintaining high accuracy in the target multimedia service.

  匹配依据：TEE: confidential computing

  </details>

- **AGATE: Augmented Global Attested Trusted Execution in the Universal Composability framework**
  2024-08-30 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1369)
  Lorenzo Martinico, Markulf Kohlweiss

  <details><summary>摘要 / Abstract</summary>

  A Trusted Execution Environment (TEE) is a security technology, implemented by CPU manufacturers, which guarantees integrity and confidentiality on a restricted execution environment to any remote verifier through attestation. TEEs are deployed on various consumer and commercial hardware platforms, and have been widely adopted as a component in the design of cryptographic protocols both theoretical and practical. Within the provable security community, the use of TEEs as a setup assumption has converged to a standard ideal definition in the Universal Composability setting ($G_{\mathsf{att}}$, defined by Pass et al., Eurocrypt &#x27;17). However, it is unclear whether any real TEE design can actually realise such a level of security, or whether the diverse capabilities of today&#x27;s TEE implementations will in fact converge to a single standard. Therefore, it is necessary for cryptographers and protocol designers to specify what assumptions are necessary for the TEE they are using to support the correctness and security of their protocol. To this end, this paper provides a more careful treatment of trusted execution than the existing literature, focusing on the capabilities of enclaves and adversaries. Our goal is to provide meaningful patterns for comparing different classes of TEEs, particularly how a weaker TEE functionality can implement a stronger one given an appropriate mechanism to bridge the two. We introduce a new, &quot;modular&quot; definition of TEEs that captures a broad range of pre-existing functionalities defined in the literature while maintaining their high level of abstraction. While our goal is not directly to model implementations of specific commercial TEE providers, our modular definition provides a way to capture more meaningful and realistic hardware capabilities. We propose to characterise TEE capabilities along the following terms: - the set of trusted features available to the enclave; - the set of possible attacks on an enclave; - the content of attestation signatures. We then define various possible ideal modular $G_{\mathsf{att}}$ functionality instantiations that capture existing variants in the literature. Finally, we conclude the paper by constructing a protocol template to realise stronger $G_{\mathsf{att}}$ setups from weaker ones, and provide an example of removing an attack.

  匹配依据：TEE: trusted execution environment

  </details>

- **Rorqual: Speeding up Narwhal with TEEs**
  2024-08-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.14099)
  Luciano Freitas, Shashank Motepalli, Matej Pavlovic, Benjamin Livshits

  <details><summary>摘要 / Abstract</summary>

  In this paper, we introduce Rorqual, a protocol designed to enhance the performance of the Narwhal Mempool by integrating Trusted Execution Environments (TEEs). Both Narwhal and Roqual are protocols based on a Directed Acyclic Graph (DAG). Compared to Narwhal, Rorqual achieves significant reductions in latency and increases throughput by streamlining the steps required to include a vertex in the DAG. The use of TEEs also reduces the communication complexity of the protocol while maintaining low computational costs. Through rigorous analysis, we demonstrate the protocol&#x27;s robustness under both normal and adversarial conditions, highlighting its improvements in throughput, latency, and security.

  匹配依据：TEE: trusted execution environments

  </details>

- **ParTEETor: A System for Partial Deployments of TEEs within Tor**
  2024-08-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.14646)
  Rachel King, Quinn Burke, Yohan Beugin, Blaine Hoak, Kunyang Li, Eric Pauley, Ryan Sheatsley, Patrick McDaniel

  <details><summary>摘要 / Abstract</summary>

  The Tor anonymity network allows users such as political activists and those under repressive governments to protect their privacy when communicating over the internet. At the same time, Tor has been demonstrated to be vulnerable to several classes of deanonymizing attacks that expose user behavior and identities. Prior work has shown that these threats can be mitigated by leveraging trusted execution environments (TEEs). However, previous proposals assume that all relays in the network will be TEE-based-which as a practical matter is unrealistic. In this work, we introduce ParTEETor, a Tor-variant system, which leverages partial deployments of TEEs to thwart known attacks. We study two modes of operation: non-policy and policy. Non-policy mode uses the existing Tor relay selection algorithm to provide users incident security. Policy mode extends the relay selection algorithm to address the classes of attacks by enforcing a specific TEE circuit configuration. We evaluate ParTEETor for security, performance, and privacy. Our evaluation demonstrates that at even a small TEE penetration (e.g., 10% of relays are TEE-based), users can reach performance of Tor today while enforcing a security policy to guarantee protection from at least two classes of attacks. Overall, we find that partial deployments of TEEs can substantially improve the security of Tor, without a significant impact on performance or privacy.

  匹配依据：TEE: trusted execution environments

  </details>

- **Confidential Computing on Heterogeneous CPU-GPU Systems: Survey and Future Directions**
  2024-08-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.11601)
  Qifan Wang, David Oswald

  <details><summary>摘要 / Abstract</summary>

  In recent years, the widespread informatization and rapid data explosion have increased the demand for high-performance heterogeneous systems that integrate multiple computing cores such as CPUs, Graphics Processing Units (GPUs), Application Specific Integrated Circuits (ASICs), and Field Programmable Gate Arrays (FPGAs). The combination of CPU and GPU is particularly popular due to its versatility. However, these heterogeneous systems face significant security and privacy risks. Advances in privacy-preserving techniques, especially hardware-based Trusted Execution Environments (TEEs), offer effective protection for GPU applications. Nonetheless, the potential security risks involved in extending TEEs to GPUs in heterogeneous systems remain uncertain and need further investigation. To investigate these risks in depth, we study the existing popular GPU TEE designs and summarize and compare their key implications. Additionally, we review existing powerful attacks on GPUs and traditional TEEs deployed on CPUs, along with the efforts to mitigate these threats. We identify potential attack surfaces introduced by GPU TEEs and provide insights into key considerations for designing secure GPU TEEs. This survey is timely as new TEEs for heterogeneous systems, particularly GPUs, are being developed, highlighting the need to understand potential security threats and build both efficient and secure systems.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **Universal Composable Transaction Serialization with Order Fairness**
  2024-08-19 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1296)
  Michele Ciampi, Aggelos Kiayias, Yu Shen

  <details><summary>摘要 / Abstract</summary>

  Order fairness in the context of distributed ledgers has received recently significant attention due to a range of attacks that exploit the reordering and adaptive injection of transactions (violating what is known as &quot;input causality&quot;). To address such concerns an array of definitions for order fairness has been put forth together with impossibility and feasibility results highlighting the difficulty and multifaceted nature of fairness in transaction serialization. Motivated by this we present a comprehensive modeling of order fairness capitalizing on the universal composition (UC) setting. Our results capture the different flavors of sender order fairness and input causality (which is arguably one of the most critical aspects of ledger transaction processing with respect to serialization attacks) and we parametrically illustrate what are the limits of feasibility for realistic constructions via an impossibility result. Our positive result, a novel distributed ledger protocol utilizing trusted enclaves, complements tightly our impossibility result, hence providing an optimal sender order fairness ledger construction that is also eminently practical.

  匹配依据：TEE: trusted enclaves

  </details>

- **Privacy Technologies for Financial Intelligence**
  2024-08-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.09935)
  Yang Li, Thilina Ranbaduge, Kee Siong Ng

  <details><summary>摘要 / Abstract</summary>

  Financial crimes like money laundering and terrorism financing can have significant impacts on society, including loss of trust in the integrity of the financial system, misuse and mismanagement of public funds, increase in societal problems like drug trafficking and illicit gambling, and loss of innocent lives due to terrorism activities. Effective detection of complex financial crimes remains a formidable challenge for regulators and financial institutions because the critical data needed to establish patterns and criminality are often dispersed across multiple organisations and cannot be linked due to privacy constraints around large-scale data matching. Recent advances in privacy and confidential computing technologies, which enable private and secure data analysis across organisations, offer a promising opportunity for regulators and the financial industry to come together to enhance their collaborative risk detection while maintaining privacy standards. This paper, through a survey of the financial intelligence ecosystem, seeks to identify opportunities for the utilisation of privacy technologies to improve the state-of-the-art in financial-crime detection.

  匹配依据：TEE: confidential computing

  </details>

- **SeeWasm: An Efficient and Fully-Functional Symbolic Execution Engine for WebAssembly Binaries**
  2024-08-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.08537)
  Ningyu He, Zhehao Zhao, Hanqin Guan, Jikai Wang, Shuo Peng, Ding Li, Haoyu Wang, Xiangqun Chen, Yao Guo

  <details><summary>摘要 / Abstract</summary>

  WebAssembly (Wasm), as a compact, fast, and isolation-guaranteed binary format, can be compiled from more than 40 high-level programming languages. However, vulnerabilities in Wasm binaries could lead to sensitive data leakage and even threaten their hosting environments. To identify them, symbolic execution is widely adopted due to its soundness and the ability to automatically generate exploitations. However, existing symbolic executors for Wasm binaries are typically platform-specific, which means that they cannot support all Wasm features. They may also require significant manual interventions to complete the analysis and suffer from efficiency issues as well. In this paper, we propose an efficient and fully-functional symbolic execution engine, named SeeWasm. Compared with existing tools, we demonstrate that SeeWasm supports full-featured Wasm binaries without further manual intervention, while accelerating the analysis by 2 to 6 times. SeeWasm has been adopted by existing works to identify more than 30 0-day vulnerabilities or security issues in well-known C, Go, and SGX applications after compiling them to Wasm binaries.

  匹配依据：TEE: sgx

  </details>

- **Reliable Communication in Hybrid Authentication and Trust Models**
  2024-08-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.08060)
  Rowdy Chotkan, Bart Cox, Vincent Rahli, Jérémie Decouchant

  <details><summary>摘要 / Abstract</summary>

  Reliable communication is a fundamental distributed communication abstraction that allows any two nodes of a network to communicate with each other. It is necessary for more powerful communication primitives, such as broadcast and consensus. Using different authentication models, two classical protocols implement reliable communication in unknown and sufficiently connected networks. In the first one, network links are authenticated, and processes rely on dissemination paths to authenticate messages. In the second one, processes generate digital signatures that are flooded in the network. This work considers the hybrid system model that combines authenticated links and authenticated processes. We additionally aim to leverage the possible presence of trusted nodes and trusted components in networks, which have been assumed in the scientific literature and in practice. We first extend the two classical reliable communication protocols to leverage trusted nodes. We then propose DualRC, a novel algorithm that enables reliable communication in the hybrid authentication model by manipulating both dissemination paths and digital signatures, and leverages the possible presence of trusted nodes (e.g., network gateways) and trusted components (e.g., Intel SGX enclaves). We provide correctness verification algorithms to assess whether our algorithms implement reliable communication for all nodes on a given network.

  匹配依据：TEE: intel sgx, sgx enclaves

  </details>

- **Voltran: Unlocking Trust and Confidentiality in Decentralized Federated Learning Aggregation**
  2024-08-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.06885)
  Hao Wang, Yichen Cai, Jun Wang, Chuan Ma, Chunpeng Ge, Xiangmou Qu, Lu Zhou

  <details><summary>摘要 / Abstract</summary>

  The decentralized Federated Learning (FL) paradigm built upon blockchain architectures leverages distributed node clusters to replace the single server for executing FL model aggregation. This paradigm tackles the vulnerability of the centralized malicious server in vanilla FL and inherits the trustfulness and robustness offered by blockchain. However, existing blockchain-enabled schemes face challenges related to inadequate confidentiality on models and limited computational resources of blockchains to perform large-scale FL computations. In this paper, we present Voltran, an innovative hybrid platform designed to achieve trust, confidentiality, and robustness for FL based on the combination of the Trusted Execution Environment (TEE) and blockchain technology. We offload the FL aggregation computation into TEE to provide an isolated, trusted and customizable off-chain execution, and then guarantee the authenticity and verifiability of aggregation results on the blockchain. Moreover, we provide strong scalability on multiple FL scenarios by introducing a multi-SGX parallel execution strategy to amortize the large-scale FL workload. We implement a prototype of Voltran and conduct a comprehensive performance evaluation. Extensive experimental results demonstrate that Voltran incurs minimal additional overhead while guaranteeing trust, confidentiality, and authenticity, and it significantly brings a significant speed-up compared to state-of-the-art ciphertext aggregation schemes.

  匹配依据：TEE: sgx, trusted execution environment

  </details>

- **CRISP: Confidentiality, Rollback, and Integrity Storage Protection for Confidential Cloud-Native Computing**
  2024-08-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.06822)
  Ardhi Putra Pratama Hartono, Andrey Brito, Christof Fetzer

  <details><summary>摘要 / Abstract</summary>

  Trusted execution environments (TEEs) protect the integrity and confidentiality of running code and its associated data. Nevertheless, TEEs&#x27; integrity protection does not extend to the state saved on disk. Furthermore, modern cloud-native applications heavily rely on orchestration (e.g., through systems such as Kubernetes) and, thus, have their services frequently restarted. During restarts, attackers can revert the state of confidential services to a previous version that may aid their malicious intent. This paper presents CRISP, a rollback protection mechanism that uses an existing runtime for Intel SGX and transparently prevents rollback. Our approach can constrain the attack window to a fixed and short period or give developers the tools to avoid the vulnerability window altogether. Finally, experiments show that applying CRISP in a critical stateful cloud-native application may incur a resource increase but only a minor performance penalty.

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **Devlore: Device Interrupt Protection for Confidential VMs**
  2024-08-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.05835)
  Andrin Bertschi, Supraja Sridhara, Mark Kuhne, Benedict Schlüter, Friederike Groschupp, Clément Thorens, Nicolas Dutly, Srdjan Capkun, Shweta Shinde

  <details><summary>摘要 / Abstract</summary>

  Modern confidential computing executes sensitive computation in an abstraction called confidential VMs and protects from the hypervisor, host OS, and other co-resident VMs. It has been shown that an attacker can inject malicious interrupts to break the confidentiality and integrity of confidential VMs. We present Devlore, a device interrupt isolation mechanism that protects confidential VMs from interrupt manipulation attacks. Our design employs a delegate-but-check strategy by offloading interrupt management to the hypervisor, but adds correctness checks in the trusted software. We prototype our design on Arm Confidential Computing Architecture (CCA). We evaluate it on Arm FVP to demonstrate four diverse devices attached to confidential VMs and report costs on a Rock5b board. Our case studies show the feasibility of real-world use cases and that Devlore incurs minimal overheads of 0.06% for typical integrated GPU applications.

  匹配依据：TEE: confidential computing

  </details>

- **Demystifying AMD SEV Performance Penalty for NFV Deployment**
  2024-08-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.02212)
  Syafiq Al Atiiq, Aris Cahyadi Risdianto

  <details><summary>摘要 / Abstract</summary>

  Network Function Virtualization (NFV) has shifted communication networks towards more adaptable software solutions, but this transition raises new security concerns, particularly in public cloud deployments. While Intel&#x27;s Software Guard Extensions (SGX) offers a potential remedy, it requires complex application adaptations. This paper investigates AMD&#x27;s Secure Encrypted Virtualization (SEV) as an alternative approach for securing NFV. SEV encrypts virtual machine (VM) memory, protecting it from threats, including those at the hypervisor level, without requiring application modifications. We explore the practicality and performance implications of executing native network function (NF) implementations in AMD SEV-SNP, the latest iteration of SEV. Our study focuses on running an unmodified Snort NF within SEV. Results show an average performance penalty of approximately 20% across various traffic and packet configurations, demonstrating a trade-off between security and performance that may be acceptable for many NFV deployments.

  匹配依据：TEE: amd sev, secure encrypted virtualization, sgx

  </details>

- **An Experimental Evaluation of TEE technology Evolution: Benchmarking Transparent Approaches based on SGX, SEV, and TDX**
  2024-08-01 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.00443)
  Luigi Coppolino, Salvatore D'Antonio, Davide Iasio, Giovanni Mazzeo, Luigi Romano

  <details><summary>摘要 / Abstract</summary>

  Protection of data-in-use is a key priority, for which Trusted Execution Environment (TEE) technology has unarguably emerged as a, possibly the most, promising solution. Multiple server-side TEE offerings have been released over the years, exhibiting substantial differences with respect to several aspects. The first comer was Intel SGX, which featured Process-based TEE protection, an efficient yet difficult to use approach. Some SGX limitations were (partially) overcome by runtimes, notably: Gramine, Scone, and Occlum. A major paradigm shift was later brought by AMD SEV, with VM-based TEE protection, which enabled lift-and-shift deployment of legacy applications. This new paradigm has been implemented by Intel only recently, in TDX. While the threat model of the aforementioned TEE solutions has been widely discussed, a thorough performance comparison is still lacking in the literature. This paper provides a comparative evaluation of TDX, SEV, Gramine-SGX, and Occlum-SGX. We study computational overhead and resource usage, under different operational scenarios and using a diverse suite of legacy applications. By doing so, we provide a reliable performance assessment under realistic conditions. We explicitly emphasize that, at the time of writing, TDX was not yet available to the public. Thus, the evaluation of TDX is a unique feature of this study.

  匹配依据：TEE: amd sev, intel sgx, sgx, trusted execution environment

  </details>

- **Model Agnostic Hybrid Sharding For Heterogeneous Distributed Inference**
  2024-07-29 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.19775)
  Claudio Angione, Yue Zhao, Harry Yang, Ahmad Farhan, Fielding Johnston, James Buban, Patrick Colangelo

  <details><summary>摘要 / Abstract</summary>

  The rapid growth of large-scale AI models, particularly large language models has brought significant challenges in data privacy, computational resources, and accessibility. Traditional centralized architectures often struggle to meet required data security and scalability needs which hinders the democratization of AI systems. Nesa introduces a model-agnostic sharding framework designed for decentralized AI inference. Our framework uses blockchain-based sequential deep neural network sharding to distribute computational tasks across a diverse network of nodes based on a personalised heuristic and routing mechanism. This enables efficient distributed training and inference for recent large-scale models even on consumer-grade hardware. We use compression techniques like dynamic blockwise quantization and mixed matrix decomposition to reduce data transfer and memory needs. We also integrate robust security measures, including hardware-based trusted execution environments to ensure data integrity and confidentiality. Evaluating our system across various natural language processing and vision tasks shows that these compression strategies do not compromise model accuracy. Our results highlight the potential to democratize access to cutting-edge AI technologies by enabling secure and efficient inference on a decentralized network.

  匹配依据：TEE: trusted execution environments

  </details>

- **Towards Secure and Private AI: A Framework for Decentralized Inference**
  2024-07-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.19401)
  Hongyang Zhang, Yue Zhao, Claudio Angione, Harry Yang, James Buban, Ahmad Farhan, Fielding Johnston, Patrick Colangelo

  <details><summary>摘要 / Abstract</summary>

  The rapid advancement of ML models in critical sectors such as healthcare, finance, and security has intensified the need for robust data security, model integrity, and reliable outputs. Large multimodal foundational models, while crucial for complex tasks, present challenges in scalability, reliability, and potential misuse. Decentralized systems offer a solution by distributing workload and mitigating central points of failure, but they introduce risks of unauthorized access to sensitive data across nodes. We address these challenges with a comprehensive framework designed for responsible AI development. Our approach incorporates: 1) Zero-knowledge proofs for secure model verification, enhancing trust without compromising privacy. 2) Consensus-based verification checks to ensure consistent outputs across nodes, mitigating hallucinations and maintaining model integrity. 3) Split Learning techniques that segment models across different nodes, preserving data privacy by preventing full data access at any point. 4) Hardware-based security through trusted execution environments (TEEs) to protect data and computations. This framework aims to enhance security and privacy and improve the reliability and fairness of multimodal AI systems. Promoting efficient resource utilization contributes to more sustainable AI development. Our state-of-the-art proofs and principles demonstrate the framework&#x27;s effectiveness in responsibly democratizing artificial intelligence, offering a promising approach for building secure and private foundational models.

  匹配依据：TEE: trusted execution environments

  </details>

- **Applying Post-Quantum Cryptography Algorithms to a DLT-Based CBDC Infrastructure: Comparative and Feasibility Analysis**
  2024-07-26 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1206)
  Daniel de Haro Moraes, Joao Paulo Aragao Pereira, Bruno Estolano Grossi, Gustavo Mirapalheta, George Marcel Monteiro Arcuri Smetana, Wesley Rodrigues, Courtnay Nery Guimarães Jr., Bruno Domingues, Fábio Saito, Marcos Simplício

  <details><summary>摘要 / Abstract</summary>

  This article presents an innovative project for a Central Bank Digital Currency (CBDC) infrastructure. Focusing on security and reliability, the proposed architecture: (1) employs post-quantum cryptography (PQC) algorithms for long-term security, even against attackers with access to cryptographically-relevant quantum computers; (2) can be integrated with a Trusted Execution Environment (TEE) to safeguard the confidentiality of transaction contents as they are processed by third-parties; and (3) uses Distributed Ledger Technology (DLT) to promote a high level of transparency and tamper resistance for all transactions registered in the system. Besides providing a theoretical discussion on the benefits of this architecture, we experimentally evaluate its components. Namely, as PQC algorithms, we consider three signature schemes being standardized by the National Institute of Standards and Technology (NIST), CRYSTALS-Dilithium, Falcon, and SPHINCS+. Those algorithms are integrated into the Hyperledger Besu (DLT) and executed both inside and outside an Intel SGX TEE environment. According to our results, CRYSTALS-Dilithium-2 combined with classical secp256k1 signatures leads to the shortest execution times when signing blocks in the DLT, reaching 1.68ms without the TEE, and 2.09ms with TEE. The same combination also displays the best results for signature verifications, achieving 0.5ms without a TEE and 1.98ms with a TEE. We also describe the main aspects of the evaluation methodology and the next steps in validating the proposed infrastructure. The conclusions drawn from our experiments is that the combination of PQC and TEE promises highly secure and effective DLT-based CBDC scenarios, ready to face the challenges of the digital financial future and potential quantum threats.

  匹配依据：TEE: intel sgx, trusted execution environment

  </details>

- **CrudiTEE: A Stick-and-Carrot Approach to Building Trustworthy Cryptocurrency Wallets with TEEs**
  2024-07-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.16473)
  Lulu Zhou, Zeyu Liu, Fan Zhang, Michael K. Reiter

  <details><summary>摘要 / Abstract</summary>

  Cryptocurrency introduces usability challenges by requiring users to manage signing keys. Popular signing key management services (e.g., custodial wallets), however, either introduce a trusted party or burden users with managing signing key shares, posing the same usability challenges. TEEs (Trusted Execution Environments) are a promising technology to avoid both, but practical implementations of TEEs suffer from various side-channel attacks that have proven hard to eliminate. This paper explores a new approach to side-channel mitigation through economic incentives for TEE-based cryptocurrency wallet solutions. By taking the cost and profit of side-channel attacks into consideration, we designed a Stick-and-Carrot-based cryptocurrency wallet, CrudiTEE, that leverages penalties (the stick) and rewards (the carrot) to disincentivize attackers from exfiltrating signing keys in the first place. We model the attacker&#x27;s behavior using a Markov Decision Process (MDP) to evaluate the effectiveness of the bounty and enable the service provider to adjust the parameters of the bounty&#x27;s reward function accordingly.

  匹配依据：TEE: trusted execution environments

  </details>

- **Aster: Fixing the Android TEE Ecosystem with Arm CCA**
  2024-07-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.16694)
  Mark Kuhne, Supraja Sridhara, Andrin Bertschi, Nicolas Dutly, Srdjan Capkun, Shweta Shinde

  <details><summary>摘要 / Abstract</summary>

  The Android ecosystem relies on either TrustZone (e.g., OP-TEE, QTEE, Trusty) or trusted hypervisors (pKVM, Gunyah) to isolate security-sensitive services from malicious apps and Android bugs. TrustZone allows any secure world code to access the normal world that runs Android. Similarly, a trusted hypervisor has full access to Android running in one VM and security services in other VMs. In this paper, we motivate the need for mutual isolation, wherein Android, hypervisors, and the secure world are isolated from each other. Then, we propose a sandboxed service abstraction, such that a sandboxed execution cannot access any other sandbox, Android, hypervisor, or secure world memory. We present Aster which achieves these goals while ensuring that sandboxed execution can still communicate with Android to get inputs and provide outputs securely. Our main insight is to leverage the hardware isolation offered by Arm Confidential Computing Architecture (CCA). However, since CCA does not satisfy our sandboxing and mutual isolation requirements, Aster repurposes its hardware enforcement to meet its goals while addressing challenges such as secure interfaces, virtio, and protection against interrupts. We implement Aster to demonstrate its feasibility and assess its compatibility. We take three case studies, including one currently deployed on Android phones and insufficiently secured using a trusted hypervisor, to demonstrate that they can be protected by Aster.

  匹配依据：TEE: arm cca, confidential computing, trustzone

  </details>

- **Agora: Trust Less and Open More in Verification for Confidential Computing**
  2024-07-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.15062)
  Hongbo Chen, Quan Zhou, Sen Yang, Xing Han, Fan Zhang, Danfeng Zhang, Xiaofeng Wang

  <details><summary>摘要 / Abstract</summary>

  Binary verification plays a pivotal role in software security, yet building a verification service that is both open and trustworthy poses a formidable challenge. In this paper, we introduce a novel binary verification service, AGORA, scrupulously designed to overcome the challenge. At the heart of this approach lies a strategic insight: certain tasks can be delegated to untrusted entities, while the corresponding validators are securely housed within the trusted computing base (TCB). AGORA can validate untrusted assertions generated for versatile policies. Through a novel blockchain-based bounty task manager, it also utilizes crowdsourcing to remove trust in theorem provers. These synergistic techniques successfully ameliorate the TCB size burden associated with two procedures: binary analysis and theorem proving. The design of AGORA allows untrusted parties to participate in these complex processes. Moreover, based on running the optimized TCB within trusted execution environments and recording the verification process on a blockchain, the public can audit the correctness of verification results. By implementing verification workflows for software-based fault isolation policy and side-channel mitigation, our evaluation demonstrates the efficacy of AGORA.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **SecScale: A Scalable and Secure Trusted Execution Environment for Servers**
  2024-07-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.13572)
  Ani Sunny, Nivedita Shrivastava, Smruti R. Sarangi

  <details><summary>摘要 / Abstract</summary>

  Trusted execution environments (TEEs) are an integral part of modern secure processors. They ensure that their application and code pages are confidential, tamper proof and immune to diverse types of attacks. In 2021, Intel suddenly announced its plans to deprecate its most trustworthy enclave, SGX, on its 11th and 12th generation processors. The reasons stemmed from the fact that it was difficult to scale the enclaves (sandboxes) beyond 256 MB as the hardware overheads outweighed the benefits. Competing solutions by Intel and other vendors are much more scalable, but do not provide many key security guarantees that SGX used to provide notably replay attack protection. In the last three years, no proposal from industry or academia has been able to provide both scalability (with a modest slowdown) as well as replay-protection on generic hardware (to the best of our knowledge). We solve this problem by proposing SecScale that uses some new ideas centered around speculative execution (read first, verify later), creating a forest of MACs (instead of a tree of counters) and providing complete memory encryption (no generic unsecure regions). We show that we are 10% faster than the nearest competing alternative.

  匹配依据：TEE: sgx, trusted execution environment, trusted execution environments

  </details>

- **LSKV: A Confidential Distributed Datastore to Protect Critical Data in the Cloud**
  2024-07-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.12623)
  Andrew Jeffery, Julien Maffre, Heidi Howard, Richard Mortier

  <details><summary>摘要 / Abstract</summary>

  Software services are increasingly migrating to the cloud, requiring trust in actors with direct access to the hardware, software and data comprising the service. A distributed datastore storing critical data sits at the core of many services; a prime example being etcd in Kubernetes. Trusted execution environments can secure this data from cloud providers during execution, but it is complex to build trustworthy data storage systems using such mechanisms. We present the design and evaluation of the Ledger-backed Secure Key-Value datastore (LSKV), a distributed datastore that provides an etcd-like API but can use trusted execution mechanisms to keep cloud providers outside the trust boundary. LSKV provides a path to transition traditional systems towards confidential execution, provides competitive performance compared to etcd, and helps clients to gain trust in intermediary services. LSKV forms a foundational core, lowering the barriers to building more trustworthy systems.

  匹配依据：TEE: trusted execution environments

  </details>

- **Cabin: Confining Untrusted Programs within Confidential VMs**
  2024-07-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.12334)
  Benshan Mei, Saisai Xia, Wenhao Wang, Dongdai Lin

  <details><summary>摘要 / Abstract</summary>

  Confidential computing safeguards sensitive computations from untrusted clouds, with Confidential Virtual Machines (CVMs) providing a secure environment for guest OS. However, CVMs often come with large and vulnerable operating system kernels, making them susceptible to attacks exploiting kernel weaknesses. The imprecise control over the read/write access in the page table has allowed attackers to exploit vulnerabilities. The lack of security hierarchy leads to insufficient separation between untrusted applications and guest OS, making the kernel susceptible to direct threats from untrusted programs. This study proposes Cabin, an isolated execution framework within guest VM utilizing the latest AMD SEV-SNP technology. Cabin shields untrusted processes to the user space of a lower virtual machine privilege level (VMPL) by introducing a proxy-kernel between the confined processes and the guest OS. Furthermore, we propose execution protection mechanisms based on fine-gained control of VMPL privilege for vulnerable programs and the proxy-kernel to minimize the attack surface. We introduce asynchronous forwarding mechanism and anonymous memory management to reduce the performance impact. The evaluation results show that the Cabin framework incurs a modest overhead (5% on average) on Nbench and WolfSSL benchmarks.

  匹配依据：TEE: amd sev, confidential computing

  </details>

- **Ascend-CC: Confidential Computing on Heterogeneous NPU for Emerging Generative AI Workloads**
  2024-07-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.11888)
  Aritra Dhar, Clément Thorens, Lara Magdalena Lazier, Lukas Cavigelli

  <details><summary>摘要 / Abstract</summary>

  Cloud workloads have dominated generative AI based on large language models (LLM). Specialized hardware accelerators, such as GPUs, NPUs, and TPUs, play a key role in AI adoption due to their superior performance over general-purpose CPUs. The AI models and the data are often highly sensitive and come from mutually distrusting parties. Existing CPU-based TEEs such as Intel SGX or AMD SEV do not provide sufficient protection. Device-centric TEEs like Nvidia-CC only address tightly coupled CPU-GPU systems with a proprietary solution requiring TEE on the host CPU side. On the other hand, existing academic proposals are tailored toward specific CPU-TEE platforms. To address this gap, we propose Ascend-CC, a confidential computing architecture based on discrete NPU devices that requires no trust in the host system. Ascend-CC provides strong security by ensuring data and model encryption that protects not only the data but also the model parameters and operator binaries. Ascend-CC uses delegation-based memory semantics to ensure isolation from the host software stack, and task attestation provides strong model integrity guarantees. Our Ascend-CC implementation and evaluation with state-of-the-art LLMs such as Llama2 and Llama3 shows that Ascend-CC introduces minimal overhead with no changes in the AI software stack.

  匹配依据：TEE: amd sev, confidential computing, intel sgx

  </details>

- **Anonymous Outsourced Statekeeping with Reduced Server Storage**
  2024-07-12 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1139)
  Dana Dachman-Soled, Esha Ghosh, Mingyu Liang, Ian Miers, Michael Rosenberg

  <details><summary>摘要 / Abstract</summary>

  Strike-lists are a common technique for rollback and replay prevention in protocols that require that clients remain anonymous or that their current position in a state machine remain confidential. Strike-lists are heavily used in anonymous credentials, e-cash schemes, and trusted execution environments, and are widely deployed on the web in the form of Privacy Pass (PoPETS &#x27;18) and Google Private State Tokens. In such protocols, clients submit pseudorandom tokens associated with each action (e.g., a page view in Privacy Pass) or state transition, and the token is added to a server-side list to prevent reuse. Unfortunately, the size of a strike-list, and hence the storage required by the server, is proportional to the total number of issued tokens, $N \cdot t$, where $N$ is the number of clients and $t$ is the maximum number of tickets per client. In this work, we ask whether it is possible to realize a strike-list-like functionality, which we call the anonymous tickets functionality, with storage requirements proportional to $N \log(t)$. For the anonymous tickets functionality we construct a secure protocol from standard assumptions that achieves server storage of $O(N)$ ciphertexts, where each ciphertext encrypts a message of length $O(\log(t))$. We also consider an extension of the strike-list functionality where the server stores an arbitrary state for each client and clients advance their state with some function $s_i\gets f(s_{i-1},\mathsf{auxinput})$, which we call the anonymous outsourced state-keeping functionality. In this setting, malicious clients are prevented from rolling back their state, while honest clients are guaranteed anonymity and confidentiality against a malicious server. We achieve analogous results in this setting for two different classes of functions. Our results rely on a new technique to preserve client anonymity in the face of selective failure attacks by a malicious server. Specifically, our protocol guarantees that misbehavior of the server either (1) does not prevent the honest client from redeeming a ticket or (2) provides the honest client with an escape hatch that can be used to simulate a redeem in a way that is indistinguishable to the server.

  匹配依据：TEE: trusted execution environments

  </details>

- **ProxyGPT: Enabling User Anonymity in LLM Chatbots via (Un)Trustworthy Volunteer Proxies**
  2024-07-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.08792)
  Dzung Pham, Jade Sheffey, Chau Minh Pham, Amir Houmansadr

  <details><summary>摘要 / Abstract</summary>

  Popular large language model (LLM) chatbots such as ChatGPT and Claude require users to create an account with an email or a phone number before allowing full access to their services. This practice ties users&#x27; personally identifiable information (PII) to their sensitive conversational data, thus posing significant privacy risks. Unfortunately, existing private LLM solutions based on cryptography or trusted execution environments (TEEs) remain unpopular due to their prohibitive computational expense and platform restrictions. To enable practical user anonymity in LLM chatbots, we propose ProxyGPT, a privacy-enhancing system that leverages browser interaction proxies to submit user queries on their behalf. Unlike traditional proxy systems, ProxyGPT operates at the &quot;user&quot; layer by proxying user interactions with the browser in identity-required environments, thus easily supporting a wide range of chatbot services. We prevent malicious proxies by performing regular integrity audits using modern web proof protocols for TLS data provenance. We further utilize state-of-the-art LLM prompt guards on the proxy&#x27;s side to mitigate unwanted user requests. Additionally, we incorporate a give-and-take economy based on Chaum&#x27;s blind-signature e-cash to incentivize ProxyGPT users to proxy for others. Our system evaluation and user study demonstrate the practicality of our approach, as each chat request only takes a few additional seconds on average to fully complete. To the best of our knowledge, ProxyGPT is the first comprehensive proxy-based solution for privacy-preserving AI chatbots.

  匹配依据：TEE: trusted execution environments

  </details>

- **Enabling Performant and Secure EDA as a Service in Public Clouds Using Confidential Containers**
  2024-07-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.06040)
  Mengmei Ye, Derren Dunn, Daniele Buono, Angelo Ruocco, Claudio Carvalho, Tobin Feldman-fitzthum, Hubertus Franke, James Bottomley

  <details><summary>摘要 / Abstract</summary>

  Increasingly, business opportunities available to fabless design teams in the semiconductor industry far exceed those addressable with on-prem compute resources. An attractive option to capture these electronic design automation (EDA) design opportunities is through public cloud bursting. However, security concerns with public cloud bursting arise from having to protect process design kits, third party intellectual property, and new design data for semiconductor devices and chips. One way to address security concerns for public cloud bursting is to leverage confidential containers for EDA workloads. Confidential containers add zero trust computing elements to significantly reduce the probability of intellectual property escapes. A key concern that often follows security discussions is whether EDA workload performance will suffer with confidential computing. In this work we demonstrate a full set of EDA confidential containers and their deployment and characterize performance impacts of confidential elements of the flow including storage and networking. A complete end-to-end confidential container-based EDA workload exhibits 7.13% and 2.05% performance overheads over bare-metal container and VM based solutions, respectively.

  匹配依据：TEE: confidential computing

  </details>

- **SRAS: Self-governed Remote Attestation Scheme for Multi-party Collaboration**
  2024-07-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.03745)
  Linan Tian, Yunke Shen, Zhiqiang Li

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs), such as Intel Software Guard Extensions (SGX), ensure the confidentiality and integrity of user applications when using cloud computing resources. However, in the multi-party cloud computing scenario, how to select a Relying Party to verify the TEE of each party and avoid leaking sensitive data to each other remains an open question. In this paper, we propose SRAS, an open self-governed remote attestation scheme with attestation and verification functions for verifying the trustworthiness of TEEs and computing assets, achieving decentralized unified trusted attestation and verification platform for multi-party cloud users. In SRAS, we design a Relying Party enclave, which can form a virtual verifiable network, capable of local verification on behalf of other participants relying parties without leaking sensitive data to others. We provide an open-source prototype implementation of SRAS to facilitate the adoption of this technology by cloud users or developers.

  匹配依据：TEE: sgx, trusted execution environments

  </details>

- **ObfuscaTune: Obfuscated Offsite Fine-tuning and Inference of Proprietary LLMs on Private Datasets**
  2024-07-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.02960)
  Ahmed Frikha, Nassim Walha, Ricardo Mendes, Krishna Kanth Nakka, Xue Jiang, Xuebing Zhou

  <details><summary>摘要 / Abstract</summary>

  This work addresses the timely yet underexplored problem of performing inference and finetuning of a proprietary LLM owned by a model provider entity on the confidential/private data of another data owner entity, in a way that ensures the confidentiality of both the model and the data. Hereby, the finetuning is conducted offsite, i.e., on the computation infrastructure of a third-party cloud provider. We tackle this problem by proposing ObfuscaTune, a novel, efficient and fully utility-preserving approach that combines a simple yet effective obfuscation technique with an efficient usage of confidential computing (only 5% of the model parameters are placed on TEE). We empirically demonstrate the effectiveness of ObfuscaTune by validating it on GPT-2 models with different sizes on four NLP benchmark datasets. Finally, we compare to a naïve version of our approach to highlight the necessity of using random matrices with low condition numbers in our approach to reduce errors induced by the obfuscation.

  匹配依据：TEE: confidential computing

  </details>

- **Laminator: Verifiable ML Property Cards using Hardware-assisted Attestations**
  2024-06-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2406.17548)
  Vasisht Duddu, Oskari Järvinen, Lachlan J Gunn, N Asokan

  <details><summary>摘要 / Abstract</summary>

  Regulations increasingly call for various assurances from machine learning (ML) model providers about their training data, training process, and model behavior. For better transparency, industry (e.g., Huggingface and Google) has adopted model cards and datasheets to describe various properties of training datasets and models. In the same vein, we introduce the notion of inference cards to describe the properties of a given inference (e.g., binding of the output to the model and its corresponding input). We coin the term ML property cards to collectively refer to these various types of cards. To prevent a malicious model provider from including false information in ML property cards, they need to be verifiable. We show how to construct verifiable ML property cards using property attestation, technical mechanisms by which a prover (e.g., a model provider) can attest to various ML properties to a verifier (e.g., an auditor). Since prior attestation mechanisms based purely on cryptography are often narrowly focused (lacking versatility) and inefficient, we need an efficient mechanism to attest different types of properties across the entire ML model pipeline. Emerging widespread support for confidential computing has made it possible to run and even train models inside hardware-assisted trusted execution environments (TEEs), which provide highly efficient attestation mechanisms. We propose Laminator, which uses TEEs to provide the first framework for verifiable ML property cards via hardware-assisted ML property attestations. Laminator is efficient in terms of overhead, scalable to large numbers of verifiers, and versatile with respect to the properties it can prove during training or inference.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **Context-Aware Trust Verification for Identity-Based Software Signing**
  2024-06-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2406.15596)
  Chinenye Okafor, James C. Davis, Santiago Torres-Arias

  <details><summary>摘要 / Abstract</summary>

  Modern software release infrastructure uses identity-based software signing to associate software artifacts with a known identity. For example, registries such as npm and Docker Hub rely on Sigstore&#x27;s identity-based software signing in their artifact provenance workflows. However, existing verification procedures only provide evidence of a signer&#x27;s identity, but not the conditions under which signing occurred. As a result, compromised credentials, identity providers, or signing tools can still produce signatures that pass verification. This gap prevents software engineering tools (e.g., package registries, dependency analysis tools, deployment systems, and CI/CD verification stages) from enforcing verifiable context-aware trust policies for software signing. We present DiVerify, a framework for automated verification of software signing conditions. A DiVerify signature binds identity claims from multiple independent scope providers, signing-environment attestation from a TEE-isolated daemon, and the signing key into a single verifiable object. A machine-checkable policy language specifies the identity, authentication, and environment conditions required for accepting a signature. We formally analyze DiVerify and show that it is sound, prototype it across three deployment modes, and demonstrate overhead under 400ms, with storage overhead of less than 1.6% of average PyPI package size. Case study integrations with existing systems confirm DiVerify composes well.

  匹配依据：TEE: tee (context)

  </details>

- **FACOS: Enabling Privacy Protection Through Fine-Grained Access Control with On-chain and Off-chain System**
  2024-06-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2406.03695)
  Chao Liu, Cankun Hou, Tianyu Jiang, Jianting Ning, Hui Qiao, Yusen Wu

  <details><summary>摘要 / Abstract</summary>

  Data-driven landscape across finance, government, and healthcare, the continuous generation of information demands robust solutions for secure storage, efficient dissemination, and fine-grained access control. Blockchain technology emerges as a significant tool, offering decentralized storage while upholding the tenets of data security and accessibility. However, on-chain and off-chain strategies are still confronted with issues such as untrusted off-chain data storage, absence of data ownership, limited access control policy for clients, and a deficiency in data privacy and auditability. To solve these challenges, we propose a permissioned blockchain-based privacy-preserving fine-grained access control on-chain and off-chain system, namely FACOS. We applied three fine-grained access control solutions and comprehensively analyzed them in different aspects, which provides an intuitive perspective for system designers and clients to choose the appropriate access control method for their systems. Compared to similar work that only stores encrypted data in centralized or non-fault-tolerant IPFS systems, we enhanced off-chain data storage security and robustness by utilizing a highly efficient and secure asynchronous Byzantine fault tolerance (BFT) protocol in the off-chain environment. As each of the clients needs to be verified and authorized before accessing the data, we involved the Trusted Execution Environment (TEE)-based solution to verify the credentials of clients. Additionally, our evaluation results demonstrated that our system offers better scalability and practicality than other state-of-the-art designs.

  匹配依据：TEE: trusted execution environment

  </details>

- **Verifying components of Arm(R) Confidential Computing Architecture with ESBMC**
  2024-06-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2406.04375)
  Tong Wu, Shale Xiong, Edoardo Manino, Gareth Stockwell, Lucas C. Cordeiro

  <details><summary>摘要 / Abstract</summary>

  Realm Management Monitor (RMM) is an essential firmware component within the recent Arm Confidential Computing Architecture (Arm CCA). Previous work applies formal techniques to verify the specification and prototype reference implementation of RMM. However, relying solely on a single verification tool may lead to the oversight of certain bugs or vulnerabilities. This paper discusses the application of ESBMC, a state-of-the-art Satisfiability Modulo Theories (SMT)-based software model checker, to further enhance RRM verification. We demonstrate ESBMC&#x27;s ability to precisely parse the source code and identify specification failures within a reasonable time frame. Moreover, we propose potential improvements for ESBMC to enhance its efficiency for industry engineers. This work contributes to exploring the capabilities of formal verification techniques in real-world scenarios and suggests avenues for further improvements to better meet industrial verification needs.

  匹配依据：TEE: arm cca, confidential computing

  </details>

- **A Survey of Unikernel Security: Insights and Trends from a Quantitative Analysis**
  2024-06-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2406.01872)
  Alex Wollman, John Hastings

  <details><summary>摘要 / Abstract</summary>

  Unikernels, an evolution of LibOSs, are emerging as a virtualization technology to rival those currently used by cloud providers. Unikernels combine the user and kernel space into one &quot;uni&quot;fied memory space and omit functionality that is not necessary for its application to run, thus drastically reducing the required resources. The removed functionality however is far-reaching and includes components that have become common security technologies such as Address Space Layout Randomization (ASLR), Data Execution Prevention (DEP), and Non-executable bits (NX bits). This raises questions about the real-world security of unikernels. This research presents a quantitative methodology using TF-IDF to analyze the focus of security discussions within unikernel research literature. Based on a corpus of 33 unikernel-related papers spanning 2013-2023, our analysis found that Memory Protection Extensions and Data Execution Prevention were the least frequently occurring topics, while SGX was the most frequent topic. The findings quantify priorities and assumptions in unikernel security research, bringing to light potential risks from underexplored attack surfaces. The quantitative approach is broadly applicable for revealing trends and gaps in niche security domains.

  匹配依据：TEE: sgx

  </details>

- **Secret Key Recovery in a Global-Scale End-to-End Encryption System**
  2024-06-03 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/887)
  Graeme Connell, Vivian Fang, Rolfe Schmidt, Emma Dauterman, Raluca Ada Popa

  <details><summary>摘要 / Abstract</summary>

  End-to-end encrypted messaging applications ensure that an attacker cannot read a user&#x27;s message history without their decryption keys. While this provides strong privacy, it creates a usability problem: if a user loses their devices and cannot access their decryption keys, they can no longer access their account. To solve this usability problem, users should be able to back up their account information with the messaging provider. For privacy, this backup should be encrypted and the provider should not have access to users&#x27; decryption keys. To solve this problem, we present Secure Value Recovery 3 (SVR3), a secret key recovery system that distributes trust across different types of hardware enclaves run by different cloud providers in order to protect users&#x27; decryption keys. SVR3 is the first deployed secret key recovery system to split trust across heterogeneous enclaves managed by different cloud providers: this design ensures that a single type of enclave does not become a central point of attack. SVR3 protects decryption keys via rollback protection and fault tolerance techniques tailored to the enclaves&#x27; security guarantees. SVR3 costs \$0.0025/user/year and takes 365ms for a user to recover their key, which is a rare operation. A part of SVR3 has been rolled out to millions of real users in a deployment with capacity for over 500 million users, demonstrating the ability to operate at scale.

  匹配依据：TEE: hardware enclaves

  </details>

- **SNPGuard: Remote Attestation of SEV-SNP VMs Using Open Source Tools**
  2024-06-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2406.01186)
  Luca Wilke, Gianluca Scopelliti

  <details><summary>摘要 / Abstract</summary>

  Cloud computing is a ubiquitous solution to handle today&#x27;s complex computing demands. However, it comes with data privacy concerns, as the cloud service provider has complete access to code and data running on their infrastructure. VM-based Trusted Execution Environments (TEEs) are a promising solution to solve this issue. They provide strong isolation guarantees to lock out the cloud service provider, as well as an attestation mechanism to enable the end user to verify their trustworthiness. Attesting the whole boot chain of a VM is a challenging task that requires modifications to several software components. While there are open source solutions for the individual components, the tooling and documentation for properly integrating them remains scarce. In this paper, we try to fill this gap by elaborating on two common boot workflows and providing open source tooling to perform them with low manual effort. The first workflow assumes that the VM image does only require integrity but not confidentiality, allowing for an uninterrupted boot process. The second workflow covers booting a VM with an encrypted root filesystem, requiring secure provisioning of the decryption key during early boot. While our tooling targets AMD Secure Encrypted Virtualization (SEV) VMs, the concepts also apply to other VM-based TEEs such as Intel Trusted Domain Extensions (TDX).

  匹配依据：TEE: secure encrypted virtualization, sev snp, trusted execution environments

  </details>

- **A Privacy-Preserving Graph Encryption Scheme Based on Oblivious RAM**
  2024-05-29 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2405.19259)
  Seyni Kane, Anis Bkakria

  <details><summary>摘要 / Abstract</summary>

  Graph encryption schemes play a crucial role in facilitating secure queries on encrypted graphs hosted on untrusted servers. With applications spanning navigation systems, network topology, and social networks, the need to safeguard sensitive data becomes paramount. Existing graph encryption methods, however, exhibit vulnerabilities by inadvertently revealing aspects of the graph structure and query patterns, posing threats to security and privacy. In response, we propose a novel graph encryption scheme designed to mitigate access pattern and query pattern leakage through the integration of oblivious RAM and trusted execution environment techniques, exemplified by a Trusted Execution Environment (TEE). Our solution establishes two key security objectives: (1) ensuring that adversaries, when presented with an encrypted graph, remain oblivious to any information regarding the underlying graph, and (2) achieving query indistinguishability by concealing access patterns. Additionally, we conducted experimentation to evaluate the efficiency of the proposed schemes when dealing with real-world location navigation services.

  匹配依据：TEE: trusted execution environment

  </details>

- **Do Not Trust Power Management: A Survey on Internal Energy-based Attacks Circumventing Trusted Execution Environments Security Properties**
  2024-05-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2405.15537)
  Gwenn Le Gonidec, Maria Méndez Real, Guillaume Bouffard, Jean-Christophe Prévotet

  <details><summary>摘要 / Abstract</summary>

  Over the past few years, several research groups have introduced innovative hardware designs for Trusted Execution Environments (TEEs), aiming to secure applications against potentially compromised privileged software, including the kernel. Since 2015, a new class of software-enabled hardware attacks leveraging energy management mechanisms has emerged. These internal energy-based attacks comprise fault, side-channel and covert channel attacks. Their aim is to bypass TEE security guarantees and expose sensitive information such as cryptographic keys. They have increased in prevalence in the past few years. Popular TEE implementations, such as ARM TrustZone and Intel SGX, incorporate countermeasures against these attacks. However, these countermeasures either hinder the capabilities of the power management mechanisms or have been shown to provide insufficient system protection. This article presents the first comprehensive knowledge survey of these attacks, along with an evaluation of literature countermeasures. We believe that this study will spur further community efforts towards this increasingly important type of attacks.

  匹配依据：TEE: intel sgx, trusted execution environments, trustzone

  </details>

- **Establishing Trust in the Beyond-5G Core Network using Trusted Execution Environments**
  2024-05-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2405.12177)
  Marinos Vomvas, Norbert Ludant, Guevara Noubir

  <details><summary>摘要 / Abstract</summary>

  The fifth generation (5G) of cellular networks starts a paradigm shift from the traditional monolithic system design to a Service Based Architecture, that fits modern performance requirements and scales efficiently to new services. This paradigm will be the foundation of future cellular core networks beyond 5G. The new architecture splits network functionalities into smaller logical entities that can be disaggregated logically, physically, and geographically. This affords interoperability between the mobile network operators and commercial software and hardware vendors or cloud providers. By making use of commodity services and products, this system construct inherits the vulnerabilities in those underlying technologies, thereby increasing its attack surface and requiring a rigorous security analysis. In this work, we review the security implications introduced in B5G networks, and the security mechanisms that are supported by the 5G standard. We emphasize on the support of Zero Trust Architecture in 5G and its relevance in decentralized deployments. We revisit the definition of trust in modern enterprise network operations and identify important Zero Trust properties that are weakened by the nature of cloud deployments. To that end, we propose a vertical extension of Zero Trust, namely, Zero Trust Execution, to model untrusted execution environments, and we provide an analysis on how to establish trust in Beyond-5G network architectures using Trusted Execution Environments. Our analysis shows how our model architecture handles the increased attack surface and reinforces the Zero Trust Architecture principles in the 5G Core, without any changes to the 5G standard. Finally, we provide experimental results over a 5G testbed using Open5GS and UERANSIM that demonstrate minimal performance overhead, and a monetary cost evaluation.

  匹配依据：TEE: trusted execution environments

  </details>

- **DuckDB-SGX2: The Good, The Bad and The Ugly within Confidential Analytical Query Processing**
  2024-05-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2405.11988)
  Ilaria Battiston, Lotte Felius, Sam Ansmink, Laurens Kuiper, Peter Boncz

  <details><summary>摘要 / Abstract</summary>

  We provide an evaluation of an analytical workload in a confidential computing environment, combining DuckDB with two technologies: modular columnar encryption in Parquet files (data at rest) and the newest version of the Intel SGX Trusted Execution Environment (TEE), providing a hardware enclave where data in flight can be (more) securely decrypted and processed. One finding is that the &quot;performance tax&quot; for such confidential analytical processing is acceptable compared to not using these technologies. We eventually manage to run TPC-H SF30 with under 2x overhead compared to non-encrypted, non-enclave execution; we show that, specifically, columnar compression and encryption are a good combination. Our second finding consists of dos and don&#x27;ts to tune DuckDB to work effectively in this environment. There are various performance hazards: potentially 5x higher cache miss costs due to memory encryption inside the enclave, NUMA penalties, and highly elevated cost of swapping pages in and out of the enclave -- which is also triggered indirectly by using a non-SGX-aware malloc library.

  匹配依据：TEE: confidential computing, hardware enclave, intel sgx, sgx, trusted execution environment

  </details>

- **Byzantine Reliable Broadcast with One Trusted Monotonic Counter**
  2024-05-20 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/774)
  Yackolley Amoussou-Guenou, Lionel Beltrando, Maurice Herlihy, Maria Potop-Butucaru

  <details><summary>摘要 / Abstract</summary>

  Byzantine Reliable Broadcast is one of the most popular communication primitives in distributed systems. Byzantine reliable broadcast ensures that processes agree to deliver a message from an initiator even if some processes (perhaps including the initiator) are Byzantine. In asynchronous settings it is known since the prominent work of Bracha [Bracha87] that Byzantine reliable broadcast can be implemented deterministically if $n \geq 3t+1$ where $t$ is an upper bound on the number of Byzantine processes. Here, we study Byzantine Reliable Broadcast when processes are equipped with trusted execution environments (TEEs), special software or hardware designed to prevent equivocation. Our contribution is twofold. First, we show that, despite common belief, when each process is equipped with a TEE, Bracha&#x27;s algorithm still needs $n \geq 3t+1$. Second, we present a novel algorithm that uses a single TEE (at the initiator) that implements Byzantine Reliable Asynchronous Broadcast with $n \geq 2t+1$.

  匹配依据：TEE: trusted execution environments

  </details>

- **TBNet: A Neural Architectural Defense Framework Facilitating DNN Model Protection in Trusted Execution Environments**
  2024-05-07 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2405.03974)
  Ziyu Liu, Tong Zhou, Yukui Luo, Xiaolin Xu

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) have become a promising solution to secure DNN models on edge devices. However, the existing solutions either provide inadequate protection or introduce large performance overhead. Taking both security and performance into consideration, this paper presents TBNet, a TEE-based defense framework that protects DNN model from a neural architectural perspective. Specifically, TBNet generates a novel Two-Branch substitution model, to respectively exploit (1) the computational resources in the untrusted Rich Execution Environment (REE) for latency reduction and (2) the physically-isolated TEE for model protection. Experimental results on a Raspberry Pi across diverse DNN model architectures and datasets demonstrate that TBNet achieves efficient model protection at a low cost.

  匹配依据：TEE: trusted execution environments

  </details>

- **Towards Trust Proof for Secure Confidential Virtual Machines**
  2024-05-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2405.01030)
  Jingkai Mao, Haoran Zhu, Junchao Fan, Lin Li, Xiaolin Chang

  <details><summary>摘要 / Abstract</summary>

  The Virtual Machine (VM)-based Trusted-Execution-Environment (TEE) technology, like AMD Secure-Encrypted-Virtualization (SEV), enables the establishment of Confidential VMs (CVMs) to protect data privacy. But CVM lacks ways to provide the trust proof of its running state, degrading the user confidence of using CVM. The technology of virtual Trusted Platform Module (vTPM) can be used to generate trust proof for CVM. However, the existing vTPM-based approaches have the weaknesses like lack of a well-defined root-of-trust, lack of vTPM protection, and lack of vTPM&#x27;s trust proof. These weaknesses prevent the generation of the trust proof of the CVM. This paper proposes an approach to generate the trust proof for AMD SEV-based CVM so as to ensure its security by using a secure vTPM to construct Trusted Complete Chain for the CVM (T3CVM). T3CVM consists of three components: 1) TR-Manager, as the well-defined root-of-trust, helps to build complete trust chains for CVMs; 2) CN-TPMCVM, a special CVM provides secure vTPMs; 3) CN-CDriver, an enhanced TPM driver. Our approach overcomes the weaknesses of existing approaches and enables trusted computing-based applications to run seamlessly in the trusted CVM. We perform a formal security analysis of T3CVM, and implement a prototype system to evaluate its performance.

  匹配依据：TEE: amd sev, secure encrypted virtualization, trusted execution environment

  </details>

- **A New Hash-based Enhanced Privacy ID Signature Scheme**
  2024-04-28 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/651)
  Liqun Chen, Changyu Dong, Nada El Kassem, Christopher J.P. Newton, Yalan Wang

  <details><summary>摘要 / Abstract</summary>

  The elliptic curve-based Enhanced Privacy ID (EPID) signature scheme is broadly used for hardware enclave attestation by many platforms that implement Intel Software Guard Extensions (SGX) and other devices. This scheme has also been included in the Trusted Platform Module (TPM) specifications and ISO/IEC standards. However, it is insecure against quantum attackers. While research into quantum-resistant EPID has resulted in several lattice-based schemes, Boneh et al. have initiated the study of EPID signature schemes built only from symmetric primitives. We observe that for this line of research, there is still room for improvement. In this paper, we propose a new hash-based EPID scheme, which includes a novel and efficient signature revocation scheme. In addition, our scheme can handle a large group size (up to $2^{60}$ group members), which meets the requirements of rapidly developing hardware enclave attestation applications. The security of our scheme is proved under the Universal Composability (UC) model. Finally, we have implemented our EPID scheme, which, to our best knowledge, is the first implementation of EPID from symmetric primitives.

  匹配依据：TEE: hardware enclave, sgx

  </details>

- **GraphOS: Towards Oblivious Graph Processing**
  2024-04-26 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/642)
  Javad Ghareh Chamani, Ioannis Demertzis, Dimitrios Papadopoulos, Charalampos Papamanthou, Rasool Jalili

  <details><summary>摘要 / Abstract</summary>

  We propose GraphOS, a system that allows a client that owns a graph database to outsource it to an untrusted server for storage and querying. It relies on doubly-oblivious primitives and trusted hardware to achieve a very strong privacy and efficiency notion which we call oblivious graph processing: the server learns nothing besides the number of graph vertexes and edges, and for each query its type and response size. At a technical level, GraphOS stores the graph on a doubly-oblivious data structure, so that all vertex/edge accesses are indistinguishable. For this purpose, we propose Omix++, a novel doubly-oblivious map that outperforms the previous state of the art by up to 34×, and may be of independent interest. Moreover, to avoid any leakage from CPU instruction fetching during query evaluation, we propose algorithms for four fundamental graph queries (BFS/DFS traversal, minimum spanning tree, and single-source shortest paths) that have a fixed execution trace, i.e., the sequence of executed operations is independent of the input. By combining these techniques, we eliminate all information that a hardware adversary observing the memory access pattern within the protected enclave can infer. We benchmarked GraphOS against the best existing solution, based on oblivious relational DBMS(translating graph queries to relational operators). GraphOS is not only significantly more performant (by up to two orders of magnitude for our tested graphs) but it eliminates leakage related to the graph topology that is practically inherent when a relational DBMS is used unless all operations are “padded” to the worst case.

  匹配依据：TEE: enclave (context)

  </details>

- **Distributed &amp; Scalable Oblivious Sorting and Shuffling**
  2024-04-24 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/627)
  Nicholas Ngai, Ioannis Demertzis, Javad Ghareh Chamani, Dimitrios Papadopoulos

  <details><summary>摘要 / Abstract</summary>

  Existing oblivious systems offer robust security by concealing memory access patterns, but they encounter significant scalability and performance challenges. Recent efforts to enhance the practicality of these systems involve embedding oblivious computation, e.g., oblivious sorting and shuffling, within Trusted Execution Environments (TEEs). For instance, oblivious sort has been heavily utilized: in Oblix (S&amp;P&#x27;18), when oblivious indexes are created and accessed; in Snoopy&#x27;s high-throughput oblivious key-value (SOSP&#x27;21) during initialization and when the input requests are deduplicated and prepared for delivery; in Opaque (NSDI&#x27;17) for all the proposed oblivious SQL operators; in the state-of-the-art non-foreign key oblivious join approach (PVLDB&#x27;20). Additionally, oblivious sort/shuffle find applications in Signal&#x27;s commercial solution for contact discovery, anonymous Google&#x27;s Key Transparency, Searchable Encryption, software monitoring, and differentially private federated learning with user privacy. In this work, we address the scalability bottleneck of oblivious sort and shuffle by re-designing these approaches to achieve high efficiency in distributed multi-enclave environments. First, we propose a multi-threaded bitonic sort optimized for the distributed setting, making it the most performant oblivious sort for small number of enclaves (up to 4). For larger numbers of enclaves, we propose a novel oblivious bucket sort, which improves data locality and network consumption and outperforms our optimized distributed bitonic-sort by up to 5-6x. To the best of our knowledge, these are the first distributed oblivious TEE-based sorting solutions. For reference, we are able to sort 2 GiB of data in 1 second and 128 GiB in 53.4 seconds in a multi-enclave test. A fundamental building block of our oblivious bucket-sort is an oblivious shuffle that improves the prior state-of-the-art result (CCS&#x27;22) by up to 9.5x in the distributed multi-enclave setting---interestingly it is better by 10% even in the single-enclave/multi-thread setting.

  匹配依据：TEE: trusted execution environments

  </details>

- **SIGY: Breaking Intel SGX Enclaves with Malicious Exceptions &amp; Signals**
  2024-04-22 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.13998)
  Supraja Sridhara, Andrin Bertschi, Benedict Schlüter, Shweta Shinde

  <details><summary>摘要 / Abstract</summary>

  User programs recover from hardware exceptions and respond to signals by executing custom handlers that they register specifically for such events. We present SIGY attack, which abuses this programming model on Intel SGX to break the confidentiality and integrity guarantees of enclaves. SIGY uses the untrusted OS to deliver fake hardware events and injects fake signals in an enclave at any point. Such unintended execution of benign program-defined handlers in an enclave corrupts its state and violates execution integrity. 7 runtimes and library OSes (OpenEnclave, Gramine, Scone, Asylo, Teaclave, Occlum, EnclaveOS) are vulnerable to SIGY. 8 languages supported in Intel SGX have programming constructs that are vulnerable to SIGY. We use SIGY to demonstrate 4 proof of concept exploits on webservers (Nginx, Node.js) to leak secrets and data analytics workloads in different languages (C and Java) to break execution integrity.

  匹配依据：TEE: intel sgx, sgx enclaves

  </details>

- **FedMPQ: Secure and Communication-Efficient Federated Learning with Multi-codebook Product Quantization**
  2024-04-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.13575)
  Xu Yang, Jiapeng Zhang, Qifeng Zhang, Zhuo Tang

  <details><summary>摘要 / Abstract</summary>

  In federated learning, particularly in cross-device scenarios, secure aggregation has recently gained popularity as it effectively defends against inference attacks by malicious aggregators. However, secure aggregation often requires additional communication overhead and can impede the convergence rate of the global model, which is particularly challenging in wireless network environments with extremely limited bandwidth. Therefore, achieving efficient communication compression under the premise of secure aggregation presents a highly challenging and valuable problem. In this work, we propose a novel uplink communication compression method for federated learning, named FedMPQ, which is based on multi shared codebook product quantization.Specifically, we utilize updates from the previous round to generate sufficiently robust codebooks. Secure aggregation is then achieved through trusted execution environments (TEE) or a trusted third party (TTP).In contrast to previous works, our approach exhibits greater robustness in scenarios where data is not independently and identically distributed (non-IID) and there is a lack of sufficient public data. The experiments conducted on the LEAF dataset demonstrate that our proposed method achieves 99% of the baseline&#x27;s final accuracy, while reducing uplink communications by 90-95%

  匹配依据：TEE: trusted execution environments

  </details>

- **TransLinkGuard: Safeguarding Transformer Models Against Model Stealing in Edge Deployment**
  2024-04-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.11121)
  Qinfeng Li, Zhiqiang Shen, Zhenghan Qin, Yangfan Xie, Xuhong Zhang, Tianyu Du, Jianwei Yin

  <details><summary>摘要 / Abstract</summary>

  Proprietary large language models (LLMs) have been widely applied in various scenarios. Additionally, deploying LLMs on edge devices is trending for efficiency and privacy reasons. However, edge deployment of proprietary LLMs introduces new security challenges: edge-deployed models are exposed as white-box accessible to users, enabling adversaries to conduct effective model stealing (MS) attacks. Unfortunately, existing defense mechanisms fail to provide effective protection. Specifically, we identify four critical protection properties that existing methods fail to simultaneously satisfy: (1) maintaining protection after a model is physically copied; (2) authorizing model access at request level; (3) safeguarding runtime reverse engineering; (4) achieving high security with negligible runtime overhead. To address the above issues, we propose TransLinkGuard, a plug-and-play model protection approach against model stealing on edge devices. The core part of TransLinkGuard is a lightweight authorization module residing in a secure environment, e.g., TEE. The authorization module can freshly authorize each request based on its input. Extensive experiments show that TransLinkGuard achieves the same security protection as the black-box security guarantees with negligible overhead.

  匹配依据：TEE: tee (context)

  </details>

- **Dynamic Frequency-Based Fingerprinting Attacks against Modern Sandbox Environments**
  2024-04-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.10715)
  Debopriya Roy Dipta, Thore Tiemann, Berk Gulmezoglu, Eduard Marin, Thomas Eisenbarth

  <details><summary>摘要 / Abstract</summary>

  The cloud computing landscape has evolved significantly in recent years, embracing various sandboxes to meet the diverse demands of modern cloud applications. These sandboxes encompass container-based technologies like Docker and gVisor, microVM-based solutions like Firecracker, and security-centric sandboxes relying on Trusted Execution Environments (TEEs) such as Intel SGX and AMD SEV. However, the practice of placing multiple tenants on shared physical hardware raises security and privacy concerns, most notably side-channel attacks. In this paper, we investigate the possibility of fingerprinting containers through CPU frequency reporting sensors in Intel and AMD CPUs. One key enabler of our attack is that the current CPU frequency information can be accessed by user-space attackers. We demonstrate that Docker images exhibit a unique frequency signature, enabling the distinction of different containers with up to 84.5% accuracy even when multiple containers are running simultaneously in different cores. Additionally, we assess the effectiveness of our attack when performed against several sandboxes deployed in cloud environments, including Google&#x27;s gVisor, AWS&#x27; Firecracker, and TEE-based platforms like Gramine (utilizing Intel SGX) and AMD SEV. Our empirical results show that these attacks can also be carried out successfully against all of these sandboxes in less than 40 seconds, with an accuracy of over 70% in all cases. Finally, we propose a noise injection-based countermeasure to mitigate the proposed attack on cloud environments.

  匹配依据：TEE: amd sev, intel sgx, trusted execution environments

  </details>

- **Privacy preserving layer partitioning for Deep Neural Network models**
  2024-04-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.07437)
  Kishore Rajasekar, Randolph Loh, Kar Wai Fok, Vrizlynn L. L. Thing

  <details><summary>摘要 / Abstract</summary>

  MLaaS (Machine Learning as a Service) has become popular in the cloud computing domain, allowing users to leverage cloud resources for running private inference of ML models on their data. However, ensuring user input privacy and secure inference execution is essential. One of the approaches to protect data privacy and integrity is to use Trusted Execution Environments (TEEs) by enabling execution of programs in secure hardware enclave. Using TEEs can introduce significant performance overhead due to the additional layers of encryption, decryption, security and integrity checks. This can lead to slower inference times compared to running on unprotected hardware. In our work, we enhance the runtime performance of ML models by introducing layer partitioning technique and offloading computations to GPU. The technique comprises two distinct partitions: one executed within the TEE, and the other carried out using a GPU accelerator. Layer partitioning exposes intermediate feature maps in the clear which can lead to reconstruction attacks to recover the input. We conduct experiments to demonstrate the effectiveness of our approach in protecting against input reconstruction attacks developed using trained conditional Generative Adversarial Network(c-GAN). The evaluation is performed on widely used models such as VGG-16, ResNet-50, and EfficientNetB0, using two datasets: ImageNet for Image classification and TON IoT dataset for cybersecurity attack detection.

  匹配依据：TEE: hardware enclave, trusted execution environments

  </details>

- **Menhir: An Oblivious Database with Protection against Access and Volume Pattern Leakage**
  2024-04-10 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/556)
  Leonie Reichert, Gowri R Chandran, Phillipp Schoppmann, Thomas Schneider, Björn Scheuermann

  <details><summary>摘要 / Abstract</summary>

  Analyzing user data while protecting the privacy of individuals remains a big challenge. Trusted execution environments (TEEs) are a possible solution as they protect processes and Virtual Machines (VMs) against malicious hosts. However, TEEs can leak access patterns to code and to the data being processed. Furthermore, when data is stored in a TEE database, the data volume required to answer a query is another unwanted side channel that contains sensitive information. Both types of information leaks, access patterns and volume patterns, allow for database reconstruction attacks. In this paper, we present Menhir, an oblivious TEE database that hides access patterns with ORAM guarantees and volume patterns through differential privacy. The database allows range and point queries with SQL-like WHERE-clauses. It builds on the state-of-the-art oblivious AVL tree construction Oblix (S&amp;P&#x27;18), which by itself does not protect against volume leakage. We show how volume leakage can be exploited in range queries and improve the construction to mitigate this type of attack. We prove the correctness and obliviousness of Menhir. Our evaluation shows that our approach is feasible and scales well with the number of rows and columns in the database.

  匹配依据：TEE: trusted execution environments

  </details>

- **Enc2DB: A Hybrid and Adaptive Encrypted Query Processing Framework**
  2024-04-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.06819)
  Hui Li, Jingwen Shi, Qi Tian, Zheng Li, Yan Fu, Bingqing Shen, Yaofeng Tu

  <details><summary>摘要 / Abstract</summary>

  As cloud computing gains traction, data owners are outsourcing their data to cloud service providers (CSPs) for Database Service (DBaaS), bringing in a deviation of data ownership and usage, and intensifying privacy concerns, especially with potential breaches by hackers or CSP insiders. To address that, encrypted database services propose encrypting every tuple and query statement before submitting to the CSP, ensuring data confidentiality when the CSP is honest-but-curious, or even compromised. Existing solutions either employ property preserving cryptography schemes, which can perform certain operations over ciphertext without decrypting the data over the CSP, or utilize trusted execution environment (TEE) to safeguard data and computations from the CSP. Based on these efforts, we introduce Enc2DB, a novel secure database system, following a hybrid strategy on PostgreSQL and openGauss. We present a micro-benchmarking test and self-adaptive mode switch strategy that can dynamically choose the best execution path (cryptography or TEE) to answer a given query. Besides, we also design and implement a ciphertext index compatible with native cost model and query optimizers to accelerate query processing. Empirical study over TPC-C test justifies that Enc2DB outperforms pure TEE and cryptography solutions, and our ciphertext index implementation also outperforms the state-of-the-art cryptographic-based system.

  匹配依据：TEE: trusted execution environment

  </details>

- **R5Detect: Detecting Control-Flow Attacks from Standard RISC-V Enclaves**
  2024-04-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.03771)
  Davide Bove, Lukas Panzer

  <details><summary>摘要 / Abstract</summary>

  Embedded and Internet-of-Things (IoT) devices are ubiquitous today, and the uprising of several botnets based on them (e.g., Mirai, Ripple20) raises issues about the security of such devices. Especially low-power devices often lack support for modern system security measures, such as stack integrity, Non-eXecutable bits or strong cryptography. In this work, we present R5Detect, a security monitoring software that detects and prevents control-flow attacks on unmodified RISC-V standard architectures. With a novel combination of different protection techniques, it can run on embedded and low-power IoT devices, which may lack proper security features. R5Detect implements a memory-protected shadow stack to prevent runtime modifications, as well as a heuristics detection based on Hardware Performance Counters to detect control-flow integrity violations. Our results indicate that regular software can be protected against different degrees of control-flow manipulations with an average performance overhead of below 5 %. We implement and evaluate R5Detect on standard low-power RISC-V devices and show that such security features can be effectively used with minimal hardware support.

  匹配依据：TEE: enclaves (context)

  </details>

- **Heckler: Breaking Confidential VMs with Malicious Interrupts**
  2024-04-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.03387)
  Benedict Schlüter, Supraja Sridhara, Mark Kuhne, Andrin Bertschi, Shweta Shinde

  <details><summary>摘要 / Abstract</summary>

  Hardware-based Trusted execution environments (TEEs) offer an isolation granularity of virtual machine abstraction. They provide confidential VMs (CVMs) that host security-sensitive code and data. AMD SEV-SNP and Intel TDX enable CVMs and are now available on popular cloud platforms. The untrusted hypervisor in these settings is in control of several resource management and configuration tasks, including interrupts. We present Heckler, a new attack wherein the hypervisor injects malicious non-timer interrupts to break the confidentiality and integrity of CVMs. Our insight is to use the interrupt handlers that have global effects, such that we can manipulate a CVM&#x27;s register states to change the data and control flow. With AMD SEV-SNP and Intel TDX, we demonstrate Heckler on OpenSSH and sudo to bypass authentication. On AMD SEV-SNP we break execution integrity of C, Java, and Julia applications that perform statistical and text analysis. We explain the gaps in current defenses and outline guidelines for future defenses.

  匹配依据：TEE: amd sev, intel tdx, trusted execution environments

  </details>

- **GuaranTEE: Towards Attestable and Private ML with CCA**
  2024-03-29 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.00190)
  Sandra Siby, Sina Abdollahi, Mohammad Maheri, Marios Kogias, Hamed Haddadi

  <details><summary>摘要 / Abstract</summary>

  Machine-learning (ML) models are increasingly being deployed on edge devices to provide a variety of services. However, their deployment is accompanied by challenges in model privacy and auditability. Model providers want to ensure that (i) their proprietary models are not exposed to third parties; and (ii) be able to get attestations that their genuine models are operating on edge devices in accordance with the service agreement with the user. Existing measures to address these challenges have been hindered by issues such as high overheads and limited capability (processing/secure memory) on edge devices. In this work, we propose GuaranTEE, a framework to provide attestable private machine learning on the edge. GuaranTEE uses Confidential Computing Architecture (CCA), Arm&#x27;s latest architectural extension that allows for the creation and deployment of dynamic Trusted Execution Environments (TEEs) within which models can be executed. We evaluate CCA&#x27;s feasibility to deploy ML models by developing, evaluating, and openly releasing a prototype. We also suggest improvements to CCA to facilitate its use in protecting the entire ML deployment pipeline on edge devices.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **SecGraph: Towards SGX-based Efficient and Confidentiality-Preserving Graph Search**
  2024-03-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.19531)
  Qiuhao Wang, Xu Yang, Saiyu Qi, Yong Qi

  <details><summary>摘要 / Abstract</summary>

  Graphs have more expressive power and are widely researched in various search demand scenarios, compared with traditional relational and XML models. Today, many graph search services have been deployed on a third-party server, which can alleviate users from the burdens of maintaining large-scale graphs and huge computation costs. Nevertheless, outsourcing graph search services to the third-party server may invade users&#x27; privacy. PeGraph was recently proposed to achieve the encrypted search over the social graph. The main idea of PeGraph is to maintain two data structures XSet and TSet motivated by the OXT technology to support encrypted conductive search. However, PeGraph still has some limitations. First, PeGraph suffers from high communication and computation costs in search operations. Second, PeGraph cannot support encrypted search over dynamic graphs. In this paper, we propose an SGX-based efficient and confidentiality-preserving graph search scheme SecGraph that can support insertion and deletion operations. We first design a new proxy-token generation method to reduce the communication cost. Then, we design an LDCF-encoded XSet based on the Logarithmic Dynamic Cuckoo Filter to reduce the computation cost. Finally, we design a new dynamic version of TSet named Twin-TSet to enable encrypted search over dynamic graphs. We have demonstrated the confidentiality preservation property of SecGraph through rigorous security analysis. Experiment results show that SecGraph yields up to 208x improvement in search time compared with PeGraph and the communication cost in PeGraph is up to 540x larger than that in SecGraph.

  匹配依据：TEE: sgx

  </details>

- **Your Trust, Your Terms: A General Paradigm for Near-Instant Cross-Chain Transfer**
  2024-03-22 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.15191)
  Di Wu, Jingyu Liu, Xuechao Wang, Jian Liu, Yingjie Xue, Kui Ren, Chun Chen

  <details><summary>摘要 / Abstract</summary>

  Cross-chain transactions today remain slow, costly, and fragmented. Existing custodial exchanges expose users to counterparty and centralization risks, while non-custodial liquidity bridges suffer from capital inefficiency and slow settlement; critically, neither approach guarantees users a unilateral path to recover assets if the infrastructure fails. We introduce the Delegated Ownership Transfer (DOT) paradigm, which decouples key ownership from value ownership to enable secure, high-performance cross-chain payments. In DOT, a user deposits funds into a sandboxed on-chain Temporary Account (TA) (value ownership) while delegating its private key (key ownership) to an abstract Trusted Entity (TE). Payments and swaps are thus reframed as near-instant, off-chain ownership handoffs. Security follows from dual guarantees: the TE&#x27;s exclusive control prevents double-spending, while a pre-signed, unilateral recovery transaction ensures users retain ultimate authority over their assets. Building on this foundation, we design a novel off-chain atomic swap that executes optimistically in near real time and remains fair even if the TE fails. We formalize the security of DOT in the Universal Composability framework and present two concrete instantiations: a high-performance design based on Trusted Execution Environments (TEEs) and a cryptographically robust variant leveraging threshold cryptography. Our geo-distributed prototype shows that cross-chain payments complete in under 16.70 ms and atomic swaps in under 33.09 ms, with costs fully decoupled from Layer-1 gas fees. These results provide a practical blueprint for building secure, efficient, and interoperable cross-chain payment systems.

  匹配依据：TEE: trusted execution environments

  </details>

- **Memory-Efficient and Secure DNN Inference on TrustZone-enabled Consumer IoT Devices**
  2024-03-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.12568)
  Xueshuo Xie, Haoxu Wang, Zhaolong Jian, Tao Li, Wei Wang, Zhiwei Xu, Guiling Wang

  <details><summary>摘要 / Abstract</summary>

  Edge intelligence enables resource-demanding Deep Neural Network (DNN) inference without transferring original data, addressing concerns about data privacy in consumer Internet of Things (IoT) devices. For privacy-sensitive applications, deploying models in hardware-isolated trusted execution environments (TEEs) becomes essential. However, the limited secure memory in TEEs poses challenges for deploying DNN inference, and alternative techniques like model partitioning and offloading introduce performance degradation and security issues. In this paper, we present a novel approach for advanced model deployment in TrustZone that ensures comprehensive privacy preservation during model inference. We design a memory-efficient management method to support memory-demanding inference in TEEs. By adjusting the memory priority, we effectively mitigate memory leakage risks and memory overlap conflicts, resulting in 32 lines of code alterations in the trusted operating system. Additionally, we leverage two tiny libraries: S-Tinylib (2,538 LoCs), a tiny deep learning library, and Tinylibm (827 LoCs), a tiny math library, to support efficient inference in TEEs. We implemented a prototype on Raspberry Pi 3B+ and evaluated it using three well-known lightweight DNN models. The experimental results demonstrate that our design significantly improves inference speed by 3.13 times and reduces power consumption by over 66.5% compared to non-memory optimization method in TEEs.

  匹配依据：TEE: trusted execution environments, trustzone

  </details>

- **Benchmarking Analytical Query Processing in Intel SGXv2**
  2024-03-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.11874)
  Adrian Lutsch, Muhammad El-Hindi, Matthias Heinrich, Daniel Ritter, Zsolt István, Carsten Binnig

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs), such as Intel&#x27;s Software Guard Extensions (SGX), are increasingly being adopted to address trust and compliance issues in the public cloud. Intel SGX&#x27;s second generation (SGXv2) addresses many limitations of its predecessor (SGXv1), offering the potential for secure and efficient analytical cloud DBMSs. We assess this potential and conduct the first in-depth evaluation study of analytical query processing algorithms inside SGXv2. Our study reveals that, unlike SGXv1, state-of-the-art algorithms like radix joins and SIMD-based scans are a good starting point for achieving high-performance query processing inside SGXv2. However, subtle hardware and software differences still influence code execution inside SGX enclaves and cause substantial overheads. We investigate these differences and propose new optimizations to bring the performance inside enclaves on par with native code execution outside enclaves.

  匹配依据：TEE: intel sgx, sgx, sgx enclaves, trusted execution environments

  </details>
