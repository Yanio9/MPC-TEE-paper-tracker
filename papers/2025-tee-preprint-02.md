# 2025 · TEE · 仅预印本来源 · 第 2/2 页

[总目录](../PAPERS.md) · [上一页](2025-tee-preprint-01.md)

- **Acurast: Decentralized Serverless Cloud**
  2025-03-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.15654)
  Christian Killer, Alessandro De Carli, Pascal Brun, Amadeo Victor Charlé, Mike Godenzi, Simon Wehrli

  <details><summary>摘要 / Abstract</summary>

  Centralized trust is ubiquitous in today&#x27;s interconnected world, from computational resources to data storage and its underlying infrastructure. The monopolization of cloud computing resembles a feudalistic system, causing a loss of privacy and data ownership. Cloud Computing and the Internet in general face widely recognized challenges, such as (1) the centralization of trust in auxiliary systems (e.g., centralized cloud providers), (2) the seamless and permissionless interoperability of fragmented ecosystems and (2) the effectiveness, verifiability, and confidentiality of the computation. Acurast is a decentralized serverless cloud that addresses all these shortcomings, following the call for a global-scale cloud founded on the principles of the open-source movement. In Acurast, a purpose-built orchestrator, a reputation engine, and an attestation service are enshrined in the consensus layer. Developers can off-load their computations and verify executions cryptographically. Furthermore, Acurast offers a modular execution layer, taking advantage of secure hardware and trusted execution environments, removing the trust required in third parties, and reducing them to cryptographic hardness assumptions. With this modular architecture, Acurast serves as a decentralized and serverless cloud, allowing confidential and verifiable compute backed by the hardware of security and performance mobile devices.

  匹配依据：TEE: trusted execution environments

  </details>

- **ProDiF: Protecting Domain-Invariant Features to Secure Pre-Trained Models Against Extraction**
  2025-03-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.13224)
  Tong Zhou, Shijin Duan, Gaowen Liu, Charles Fleming, Ramana Rao Kompella, Shaolei Ren, Xiaolin Xu

  <details><summary>摘要 / Abstract</summary>

  Pre-trained models are valuable intellectual property, capturing both domain-specific and domain-invariant features within their weight spaces. However, model extraction attacks threaten these assets by enabling unauthorized source-domain inference and facilitating cross-domain transfer via the exploitation of domain-invariant features. In this work, we introduce **ProDiF**, a novel framework that leverages targeted weight space manipulation to secure pre-trained models against extraction attacks. **ProDiF** quantifies the transferability of filters and perturbs the weights of critical filters in unsecured memory, while preserving actual critical weights in a Trusted Execution Environment (TEE) for authorized users. A bi-level optimization further ensures resilience against adaptive fine-tuning attacks. Experimental results show that **ProDiF** reduces source-domain accuracy to near-random levels and decreases cross-domain transferability by 74.65\%, providing robust protection for pre-trained models. This work offers comprehensive protection for pre-trained DNN models and highlights the potential of weight space manipulation as a novel approach to model security.

  匹配依据：TEE: trusted execution environment

  </details>

- **Verifiable, Efficient and Confidentiality-Preserving Graph Search with Transparency**
  2025-03-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.10171)
  Qiuhao Wang, Xu Yang, Yiwei Liu, Saiyu Qi, Hongguang Zhao, Ke Li, Yong Qi

  <details><summary>摘要 / Abstract</summary>

  Graph databases have garnered extensive attention and research due to their ability to manage relationships between entities efficiently. Today, many graph search services have been outsourced to a third-party server to facilitate storage and computational support. Nevertheless, the outsourcing paradigm may invade the privacy of graphs. PeGraph is the latest scheme achieving encrypted search over social graphs to address the privacy leakage, which maintains two data structures XSet and TSet motivated by the OXT technology to support encrypted conjunctive search. However, PeGraph still exhibits limitations inherent to the underlying OXT. It does not provide transparent search capabilities, suffers from expensive computation and result pattern leakages, and it fails to support search over dynamic encrypted graph database and results verification. In this paper, we propose SecGraph to address the first two limitations, which adopts a novel system architecture that leverages an SGX-enabled cloud server to provide users with secure and transparent search services since the secret key protection and computational overhead have been offloaded to the cloud server. Besides, we design an LDCF-encoded XSet based on the Logarithmic Dynamic Cuckoo Filter to facilitate efficient plaintext computation in trusted memory, effectively mitigating the risks of result pattern leakage and performance degradation due to exceeding the limited trusted memory capacity. Finally, we design a new dynamic version of TSet named Twin-TSet to enable conjunctive search over dynamic encrypted graph database. In order to support verifiable search, we further propose VSecGraph, which utilizes a procedure-oriented verification method to verify all data structures loaded into the trusted memory, thus bypassing the computational overhead associated with the client&#x27;s local verification.

  匹配依据：TEE: sgx

  </details>

- **RaceTEE: Enabling Interoperability of Confidential Smart Contracts**
  2025-03-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.09317)
  Keyu Zhang, Andrew Martin

  <details><summary>摘要 / Abstract</summary>

  Decentralized smart contracts enable trustless collaboration but suffer from limited privacy and scalability, which hinders broader adoption. Trusted Execution Environment (TEE) based off-chain execution frameworks offer a promising solution to both issues. Although TEE-based frameworks have made significant progress, prior work has yet to fully explore contract interoperability, a critical foundation for building complex real-world decentralized applications. This paper identifies the key challenges impeding such interoperability and presents practical solutions. Based on these insights, we introduce RaceTEE, a novel framework that leverages off-chain TEE-enabled nodes to efficiently execute confidential, long-lived smart contracts with interactions of arbitrary complexity among contracts. We implement a RaceTEE prototype using Intel SGX, integrate it with Ethereum, and release it as open source. Evaluation across diverse use cases demonstrates its practicality and effectiveness.

  匹配依据：TEE: intel sgx, trusted execution environment

  </details>

- **SoK: A cloudy view on trust relationships of CVMs -- How Confidential Virtual Machines are falling short in Public Cloud**
  2025-03-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.08256)
  Jana Eisoldt, Anna Galanou, Andrey Ruzhanskiy, Nils Küchenmeister, Yewgenij Baburkin, Tianxiang Dai, Ivan Gudymenko, Stefan Köpsell, Rüdiger Kapitza

  <details><summary>摘要 / Abstract</summary>

  Confidential computing in the public cloud intends to safeguard workload privacy while outsourcing infrastructure management to a cloud provider. This is achieved by executing customer workloads within so called Trusted Execution Environments (TEEs), such as Confidential Virtual Machines (CVMs), which protect them from unauthorized access by cloud administrators and privileged system software. At the core of confidential computing lies remote attestation -- a mechanism that enables workload owners to verify the initial state of their workload and furthermore authenticate the underlying hardware. hile this represents a significant advancement in cloud security, this SoK critically examines the confidential computing offerings of market-leading cloud providers to assess whether they genuinely adhere to its core principles. We develop a taxonomy based on carefully selected criteria to systematically evaluate these offerings, enabling us to analyse the components responsible for remote attestation, the evidence provided at each stage, the extent of cloud provider influence and whether this undermines the threat model of confidential computing. Specifically, we investigate how CVMs are deployed in the public cloud infrastructures, the extent to which customers can request and verify attestation evidence, and their ability to define and enforce configuration and attestation requirements. This analysis provides insight into whether confidential computing guarantees -- namely confidentiality and integrity -- are genuinely upheld. Our findings reveal that all major cloud providers retain control over critical parts of the trusted software stack and, in some cases, intervene in the standard remote attestation process. This directly contradicts their claims of delivering confidential computing, as the model fundamentally excludes the cloud provider from the set of trusted entities.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **GOD model: Privacy Preserved AI School for Personal Assistant**
  2025-02-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2502.18527) · [Code](https://github.com/PIN-AI/God-Model)
  PIN AI Team, Bill Sun, Gavin Guo, Regan Peng, Boliang Zhang, Shouqiao Wang, Laura Florescu, Xi Wang, Davide Crapis, Ben Wu

  <details><summary>摘要 / Abstract</summary>

  Personal AI assistants (e.g., Apple Intelligence, Meta AI) offer proactive recommendations that simplify everyday tasks, but their reliance on sensitive user data raises concerns about privacy and trust. To address these challenges, we introduce the Guardian of Data (GOD), a secure, privacy-preserving framework for training and evaluating AI assistants directly on-device. Unlike traditional benchmarks, the GOD model measures how well assistants can anticipate user needs-such as suggesting gifts-while protecting user data and autonomy. Functioning like an AI school, it addresses the cold start problem by simulating user queries and employing a curriculum-based approach to refine the performance of each assistant. Running within a Trusted Execution Environment (TEE), it safeguards user data while applying reinforcement and imitation learning to refine AI recommendations. A token-based incentive system encourages users to share data securely, creating a data flywheel that drives continuous improvement. Specifically, users mine with their data, and the mining rate is determined by GOD&#x27;s evaluation of how well their AI assistant understands them across categories such as shopping, social interactions, productivity, trading, and Web3. By integrating privacy, personalization, and trust, the GOD model provides a scalable, responsible path for advancing personal AI assistants. For community collaboration, part of the framework is open-sourced at https://github.com/PIN-AI/God-Model.

  匹配依据：TEE: trusted execution environment

  </details>

- **Formally-verified Security against Forgery of Remote Attestation using SSProve**
  2025-02-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2502.17653)
  Sara Zain, Jannik Mähn, Stefan Köpsell, Sebastian Ertel

  <details><summary>摘要 / Abstract</summary>

  Remote attestation (RA) is the foundation for trusted execution environments in the cloud and trusted device driver onboarding in operating systems. However, RA misses a rigorous mechanized definition of its security properties in one of the strongest models, i.e., the semantic model. Such a mechanization requires the concept of StateSeparating Proofs (SSP). However, SSP was only recently implemented as a foundational framework in the Rocq Prover. Based on this framework, this paper presents the first mechanized formalization of the fundamental security properties of RA. Our Rocq Prover development first defines digital signatures and formally verifies security against forgery in the strong existential attack model. Based on these results, we define RA and reduce the security of RA to the security of digital signatures. Our development provides evidence that the RA protocol is secure against forgery. Additionally, we extend our reasoning to the primitives of RA and reduce their security to the security of the primitives of the digital signatures.

  匹配依据：TEE: trusted execution environments

  </details>

- **DITING: A Static Analyzer for Identifying Bad Partitioning Issues in TEE Applications**
  2025-02-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2502.15281)
  Chengyan Ma, Ruidong Han, Jieke Shi, Ye Liu, Yuqing Niu, Di Lu, Chuang Tian, Jianfeng Ma, Debin Gao, David Lo

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environment (TEE) enhances the security of mobile applications and cloud services by isolating sensitive code in the secure world from the non-secure normal world. However, TEE applications are still confronted with vulnerabilities stemming from bad partitioning. Bad partitioning can lead to critical security problems of TEE, such as leaking sensitive data to the normal world or being adversely affected by malicious inputs from the normal world. To address this, we propose an approach to detect partitioning issues in TEE applications. First, we conducted a survey of TEE vulnerabilities caused by bad partitioning and found that the parameters exchanged between the secure and normal worlds often contain insecure usage with bad partitioning implementation. Second, we developed a tool named DITING that can analyze data-flows of these parameters and identify their violations of security rules we defined to find bad partitioning issues. Different from existing research that only focuses on malicious input to TEE, we assess the partitioning issues more comprehensively through input/output and shared memory. Finally, we created the first benchmark targeting bad partitioning, consisting of 110 test cases. Experiments demonstrate that DITING achieves an F1 score of 0.90 in identifying bad partitioning issues.

  匹配依据：TEE: trusted execution environment

  </details>

- **Graph in the Vault: Protecting Edge GNN Inference with Trusted Execution Environment**
  2025-02-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2502.15012)
  Ruyi Ding, Tianhong Xu, Aidong Adam Ding, Yunsi Fei

  <details><summary>摘要 / Abstract</summary>

  Wide deployment of machine learning models on edge devices has rendered the model intellectual property (IP) and data privacy vulnerable. We propose GNNVault, the first secure Graph Neural Network (GNN) deployment strategy based on Trusted Execution Environment (TEE). GNNVault follows the design of &#x27;partition-before-training&#x27; and includes a private GNN rectifier to complement with a public backbone model. This way, both critical GNN model parameters and the private graph used during inference are protected within secure TEE compartments. Real-world implementations with Intel SGX demonstrate that GNNVault safeguards GNN inference against state-of-the-art link stealing attacks with negligible accuracy degradation (&lt;2%).

  匹配依据：TEE: intel sgx, trusted execution environment

  </details>

- **CipherGuard: Compiler-aided Mitigation against Ciphertext Side-channel Attacks**
  2025-02-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2502.13401)
  Ke Jiang, Sen Deng, Yinshuai Li, Shuai Wang, Tianwei Zhang, Yinqian Zhang

  <details><summary>摘要 / Abstract</summary>

  Recently, the new ciphertext side channels resulting from the deterministic memory encryption in Trusted Execution Environments (TEEs), enable ciphertexts to manifest identifiable patterns when being sequentially written to the same memory address. Attackers with read access to encrypted memory in TEEs can potentially deduce plaintexts by analyzing these changing ciphertext patterns. In this paper, we design CipherGuard, a compiler-based mitigation tool to counteract ciphertext side channels with high efficiency and security guarantees. CipherGuard is based on the LLVM ecosystem, and encompasses multiple defense strategies, including software-assisted probabilistic encryption, secret-aware register allocation, and diversion-based obfuscation. The design of CipherGuard demonstrates that compiler techniques are highly effective for fine-grained control over mitigation code generation and assisted component management. Through a comprehensive evaluation, it demonstrates that CipherGuard can strengthen the security of various cryptographic implementations more efficiently than existing state-of-the-art defense, i.e., CipherFix. In its most efficient strategy, CipherGuard incurs an average performance overhead of only 1.41X, with a maximum of 1.95X.

  匹配依据：TEE: trusted execution environments

  </details>

- **Automated TEE Adaptation with LLMs: Identifying, Transforming, and Porting Sensitive Functions in Programs**
  2025-02-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2502.13379)
  Ruidong Han, Zhou Yang, Chengyan Ma, Ye Liu, Yuqing Niu, Siqi Ma, Debin Gao, David Lo

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) isolate a special space within a device memory that is not accessible to the normal world (also known as the untrusted environment), even when the device is compromised. Therefore, developers can utilize TEEs to provide robust security guarantees for their programs, protecting sensitive operations, such as encrypted data storage, fingerprint verification, and remote attestation, from software-based attacks. Despite the robust protections offered by TEEs, adapting existing programs to leverage such security guarantees is challenging, often requiring extensive domain knowledge and manual intervention, which makes TEEs less accessible to developers. This motivates us to design AUTOTEE, the first Large Language Model (LLM) enabled approach that can automatically identify, transform, and port functions containing sensitive operations into TEEs with minimal developer intervention. By manually reviewing 68 repositories, we constructed a benchmark dataset consisting of 385 sensitive functions eligible for transformation, on which AUTOTEE achieves a F1 score of 0.94 on Java and 0.87 on Python. AUTOTEE effectively transforms these sensitive functions into TEE-compatible versions, achieving success rates of 91.8% and 84.3% for Java and Python, respectively, when using GPT-4o.

  匹配依据：TEE: trusted execution environments

  </details>

- **Evaluating the Performance of the DeepSeek Model in Confidential Computing Environment**
  2025-02-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2502.11347)
  Ben Dong, Qian Wang

  <details><summary>摘要 / Abstract</summary>

  The increasing adoption of Large Language Models (LLMs) in cloud environments raises critical security concerns, particularly regarding model confidentiality and data privacy. Confidential computing, enabled by Trusted Execution Environments (TEEs), offers a promising solution to mitigate these risks. However, existing TEE implementations, primarily CPU-based, struggle to efficiently support the resource-intensive nature of LLM inference and training. In this work, we present the first evaluation of the DeepSeek model within a TEE-enabled confidential computing environment, specifically utilizing Intel Trust Domain Extensions (TDX). Our study benchmarks DeepSeek&#x27;s performance across CPU-only, CPU-GPU hybrid, and TEE-based implementations. For smaller parameter sets, such as DeepSeek-R1-1.5B, the TDX implementation outperforms the CPU version in executing computations within a secure environment. It highlights the potential for efficiently deploying LLM models on resource-constrained systems while ensuring security. The overall GPU-to-CPU performance ratio averages 12 across different model sizes, with smaller models exhibiting a lower ratio. Additionally, we provide foundational insights and guidance on optimizing CPU-GPU confidential computing solutions for scalable and secure AI deployments. Our findings contribute to the advancement of privacy-preserving AI, paving the way for efficient and secure LLM inference in confidential computing environments.

  匹配依据：TEE: confidential computing, trust domain extensions, trusted execution environments

  </details>

- **PMU-Data: Data Traces Could be Distinguished**
  2025-02-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2502.10722)
  Zhouyang Li, Pengfei Qiu, Yu Qing, Chunlu Wang, Dongsheng Wang, Xiao Zhang, Gang Qu

  <details><summary>摘要 / Abstract</summary>

  Modern processors widely equip the Performance Monitoring Unit (PMU) to collect various architecture and microarchitecture events. Software developers often utilize the PMU to enhance program&#x27;s performance, but the potential side effects that arise from its activation are often disregarded. In this paper, we find that the PMU can be employed to retrieve instruction operands. Based on this discovery, we introduce PMU-Data, a novel category of side-channel attacks aimed at leaking secret by identifying instruction operands with PMU. To achieve the PMU-Data attack, we develop five gadgets to encode the confidential data into distinct data-related traces while maintaining the control-flow unchanged. We then measure all documented PMU events on three physical machines with different processors while those gadgets are performing. We successfully identify two types of vulnerable gadgets caused by DIV and MOV instructions. Additionally, we discover 40 vulnerable PMU events that can be used to carry out the PMU-Data attack. We through real experiments to demonstrate the perniciousness of the PMU-Data attack by implementing three attack goals: (1) leaking the kernel data illegally combined with the transient execution vulnerabilities including Meltdown, Spectre, and Zombieload; (2) building a covert-channel to secretly transfer data; (3) extracting the secret data protected by the Trusted Execution Environment (TEE) combined with the Zombieload vulnerability.

  匹配依据：TEE: trusted execution environment

  </details>

- **Recipe: Hardware-Accelerated Replication Protocols**
  2025-02-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2502.09251)
  Dimitra Giantsidi, Emmanouil Giortamis, Julian Pritzi, Maurice Bailleu, Manos Kapritsos, Pramod Bhatotia

  <details><summary>摘要 / Abstract</summary>

  Replication protocols are essential for distributed systems, ensuring consistency, reliability, and fault tolerance. Traditional Crash Fault Tolerant (CFT) protocols, which assume a fail-stop model, are inadequate for untrusted cloud environments where adversaries or software bugs can cause Byzantine behavior. Byzantine Fault Tolerant (BFT) protocols address these threats but face significant performance, resource overheads, and scalability challenges. This paper introduces Recipe, a novel approach to transforming CFT protocols to operate securely in Byzantine settings without altering their core logic. Recipe rethinks CFT protocols in the context of modern cloud hardware, including many-core servers, RDMA-capable networks, and Trusted Execution Environments (TEEs). The approach leverages these advancements to enhance the security and performance of replication protocols in untrusted cloud environments. Recipe implements two practical security mechanisms, i.e., transferable authentication and non-equivocation, using TEEs and high-performance networking stacks (e.g., RDMA, DPDK). These mechanisms ensure that any CFT protocol can be transformed into a BFT protocol, guaranteeing authenticity and non-equivocation. The Recipe protocol consists of five key components: transferable authentication, initialization, normal operation, view change, and recovery phases. The protocol&#x27;s correctness is formally verified using Tamarin, a symbolic model checker. Recipe is implemented as a library and applied to transform four widely used CFT protocols-Raft, Chain Replication, ABD, and AllConcur-into Byzantine settings. The results demonstrate up to 24x higher throughput compared to PBFT and 5.9x better performance than state-of-the-art BFT protocols. Additionally, Recipe requires fewer replicas and offers confidentiality, a feature absent in traditional BFT protocols.

  匹配依据：TEE: trusted execution environments

  </details>

- **NDAI Agreements**
  2025-02-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2502.07924)
  Matthew Stephenson, Andrew Miller, Xyn Sun, Bhargav Annem, Rohan Parikh

  <details><summary>摘要 / Abstract</summary>

  We study a fundamental challenge in the economics of innovation: an inventor must reveal details of a new idea to secure compensation or funding, yet such disclosure risks expropriation. We present a model in which a seller (inventor) and buyer (investor) bargain over an information good under the threat of hold-up. In the classical setting, the seller withholds disclosure to avoid misappropriation, leading to inefficiency. We show that trusted execution environments (TEEs) combined with AI agents can mitigate and even fully eliminate this hold-up problem. By delegating the disclosure and payment decisions to tamper-proof programs, the seller can safely reveal the invention without risking expropriation, achieving full disclosure and an efficient ex post transfer. Moreover, even if the invention&#x27;s value exceeds a threshold that TEEs can fully secure, partial disclosure still improves outcomes compared to no disclosure. Recognizing that real AI agents are imperfect, we model &quot;agent errors&quot; in payments or disclosures and demonstrate that budget caps and acceptance thresholds suffice to preserve most of the efficiency gains. Our results imply that cryptographic or hardware-based solutions can function as an &quot;ironclad NDA,&quot; substantially mitigating the fundamental disclosure-appropriation paradox first identified by Arrow (1962) and Nelson (1959). This has far-reaching policy implications for fostering R&amp;D, technology transfer, and collaboration.

  匹配依据：TEE: trusted execution environments

  </details>

- **Automatic ISA analysis for Secure Context Switching**
  2025-02-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2502.06609)
  Neelu S. Kalani, Thomas Bourgeat, Guerney D. H. Hunt, Wojciech Ozga

  <details><summary>摘要 / Abstract</summary>

  Instruction set architectures are complex, with hundreds of registers and instructions that can modify dozens of them during execution, variably on each instance. Prose-style ISA specifications struggle to capture these intricacies of the ISAs, where often the important details about a single register are spread out across hundreds of pages of documentation. Ensuring that all ISA-state is swapped in context switch implementations of privileged software requires meticulous examination of these pages. This manual process is tedious and error-prone. We propose a tool called Sailor that leverages machine-readable ISA specifications written in Sail to automate this task. Sailor determines the ISA-state necessary to swap during the context switch using the data collected from Sail and a novel algorithm to classify ISA-state as security-sensitive. Using Sailor&#x27;s output, we identify three different classes of mishandled ISA-state across four open-source confidential computing systems. We further reveal five distinct security vulnerabilities that can be exploited using the mishandled ISA-state. This research exposes an often overlooked attack surface that stems from mishandled ISA-state, enabling unprivileged adversaries to exploit system vulnerabilities.

  匹配依据：TEE: confidential computing

  </details>

- **TNIC: A Trusted NIC Architecture**
  2025-02-07 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2502.05338)
  Dimitra Giantsidi, Julian Pritzi, Felix Gust, Antonios Katsarakis, Atsushi Koshiba, Pramod Bhatotia

  <details><summary>摘要 / Abstract</summary>

  We introduce TNIC, a trusted NIC architecture for building trustworthy distributed systems deployed in heterogeneous, untrusted (Byzantine) cloud environments. TNIC builds a minimal, formally verified, silicon root-of-trust at the network interface level. We strive for three primary design goals: (1) a host CPU-agnostic unified security architecture by providing trustworthy network-level isolation; (2) a minimalistic and verifiable TCB based on a silicon root-of-trust by providing two core properties of transferable authentication and non-equivocation; and (3) a hardware-accelerated trustworthy network stack leveraging SmartNICs. Based on the TNIC architecture and associated network stack, we present a generic set of programming APIs and a recipe for building high-performance, trustworthy, distributed systems for Byzantine settings. We formally verify the safety and security properties of our TNIC while demonstrating its use by building four trustworthy distributed systems. Our evaluation of TNIC shows up to 6x performance improvement compared to CPU-centric TEE systems.

  匹配依据：TEE: tee (context)

  </details>

- **LATTEO: A Framework to Support Learning Asynchronously Tempered with Trusted Execution and Obfuscation**
  2025-02-07 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2502.04601)
  Abhinav Kumar, George Torres, Noah Guzinski, Gaurav Panwar, Reza Tourani, Satyajayant Misra, Marcin Spoczynski, Mona Vij, Nageen Himayat

  <details><summary>摘要 / Abstract</summary>

  The privacy vulnerabilities of the federated learning (FL) paradigm, primarily caused by gradient leakage, have prompted the development of various defensive measures. Nonetheless, these solutions have predominantly been crafted for and assessed in the context of synchronous FL systems, with minimal focus on asynchronous FL. This gap arises in part due to the unique challenges posed by the asynchronous setting, such as the lack of coordinated updates, increased variability in client participation, and the potential for more severe privacy risks. These concerns have stymied the adoption of asynchronous FL. In this work, we first demonstrate the privacy vulnerabilities of asynchronous FL through a novel data reconstruction attack that exploits gradient updates to recover sensitive client data. To address these vulnerabilities, we propose a privacy-preserving framework that combines a gradient obfuscation mechanism with Trusted Execution Environments (TEEs) for secure asynchronous FL aggregation at the network edge. To overcome the limitations of conventional enclave attestation, we introduce a novel data-centric attestation mechanism based on Multi-Authority Attribute-Based Encryption. This mechanism enables clients to implicitly verify TEE-based aggregation services, effectively handle on-demand client participation, and scale seamlessly with an increasing number of asynchronous connections. Our gradient obfuscation mechanism reduces the structural similarity index of data reconstruction by 85% and increases reconstruction error by 400%, while our framework improves attestation efficiency by lowering average latency by up to 1500% compared to RA-TLS, without additional overhead.

  匹配依据：TEE: trusted execution environments

  </details>

- **Trustformer: A Trusted Federated Transformer**
  2025-01-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.11706)
  Ali Abbasi Tadi, Dima Alhadidi, Luis Rueda

  <details><summary>摘要 / Abstract</summary>

  Transformers, a cornerstone of deep-learning architectures for sequential data, have achieved state-of-the-art results in tasks like Natural Language Processing (NLP). Models such as BERT and GPT-3 exemplify their success and have driven the rise of large language models (LLMs). However, a critical challenge persists: safeguarding the privacy of data used in LLM training. Privacy-preserving techniques like Federated Learning (FL) offer potential solutions, but practical limitations hinder their effectiveness for Transformer training. Two primary issues are (I) the risk of sensitive information leakage due to aggregation methods like FedAvg or FedSGD, and (II) the high communication overhead caused by the large size of Transformer models. This paper introduces a novel FL method that reduces communication overhead while maintaining competitive utility. Our approach avoids sharing full model weights by simulating a global model locally. We apply k-means clustering to each Transformer layer, compute centroids locally, and transmit only these centroids to the server instead of full weights or gradients. To enhance security, we leverage Intel SGX for secure transmission of centroids. Evaluated on a translation task, our method achieves utility comparable to state-of-the-art baselines while significantly reducing communication costs. This provides a more efficient and privacy-preserving FL solution for Transformer models.

  匹配依据：TEE: intel sgx

  </details>

- **ENOLA: Linear-Space and Low-Overhead Control-Flow Attestation for Microcontroller-based Systems**
  2025-01-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.11207)
  Md Armanuzzaman, Engin Kirda, Ziming Zhao

  <details><summary>摘要 / Abstract</summary>

  Control-Flow Attestation (CFA) aims to precisely verify execution paths to a remote verifier. However, existing solutions are fundamentally incompatible with resource-constrained, microcontroller-based systems due to the following reasons: (1) the overhead of transmitting measurement and trace data scales poorly (i.e., often exponentially) with the number of basic blocks or linearly with the length of execution traces, making such approaches impractical even on high-end microprocessor-based systems and entirely infeasible on microcontrollers; (2) cryptographic keys and measurement data are typically stored in memory, rendering them vulnerable to cold boot and memory corruption attacks, which is a serious threat for field-deployed devices; and (3) reliance on software-based measurements, combined with frequent context switches between the Rich Execution Environment (REE) and the Trusted Execution Environment (TEE), introduces significant performance overhead. In this paper, we present ENOLA, a linear-space and low-overhead control-flow attestation solution for microcontroller-based systems. ENOLA achieves linear transmission complexity with basic blocks, guaranteeing its scalability for larger programs. Moreover, ENOLA uses hardware-assisted measurement computation present in off-the-shelf devices, and avoids key storage in memory. ENOLA also allocates general-purpose registers for measurements to thwart memory corruption attacks. ENOLA significantly reduces context switching overhead by eliminating transitions from REE to TEE for backward-edge measurements. We developed the ENOLA compiler using LLVM passes and a custom attestation engine targeting the ARMv8.1-M architecture. Our evaluation shows that ENOLA reduces data transmission overhead by an average of 52x on the Embench, while maintaining performance comparable to (or exceeding) that of existing approaches.

  匹配依据：TEE: trusted execution environment

  </details>

- **A performance analysis of VM-based Trusted Execution Environments for Confidential Federated Learning**
  2025-01-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.11558)
  Bruno Casella

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) is a distributed machine learning approach that has emerged as an effective way to address recent privacy concerns. However, FL introduces the need for additional security measures as FL alone is still subject to vulnerabilities such as model and data poisoning and inference attacks. Confidential Computing (CC) is a paradigm that, by leveraging hardware-based trusted execution environments (TEEs), protects the confidentiality and integrity of ML models and data, thus resulting in a powerful ally of FL applications. Typical TEEs offer an application-isolation level but suffer many drawbacks, such as limited available memory and debugging and coding difficulties. The new generation of TEEs offers a virtual machine (VM)-based isolation level, thus reducing the porting effort for existing applications. In this work, we compare the performance of VM-based and application-isolation level TEEs for confidential FL (CFL) applications. In particular, we evaluate the impact of TEEs and additional security mechanisms such as TLS (for securing the communication channel). The results, obtained across three datasets and two deep learning models, demonstrate that the new VM-based TEEs introduce a limited overhead (at most 1.5x), thus paving the way to leverage public and untrusted computing environments, such as HPC facilities or public cloud, without detriment to performance.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **Not eXactly Byzantine: Efficient and Resilient TEE-Based State Machine Replication**
  2025-01-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.11051)
  Marc Leinweber, Hannes Hartenstein

  <details><summary>摘要 / Abstract</summary>

  We propose, implement, and evaluate NxBFT, a resilient and efficient State Machine Replication protocol using Trusted Execution Environments (TEEs). NxBFT focuses on a &quot;Not eXactly Byzantine&quot; (NxB) operating model as a middle ground between crash and Byzantine fault tolerance. NxBFT&#x27;s consensus layer is asynchronous, graph-based, leaderless, and optimized for the NxB operating model, enabling load-balancing of requests between replicas and, in fault-free cases, two network round trips between decisions. We identify fundamental issues with crash recovery due the use of TEEs in asynchrony that only can be circumvented by relying on synchrony for liveness. We provide a throughput-latency trade-off analysis of NxBFT, Chained-Damysus (rotating leader), and MinBFT (static leader) for up to 40 replicas and network round trip latencies up to 150 ms. NxBFT achieves the highest throughput in all scenarios. When small latencies are required, MinBFT and Damysus are at an advantage with Damysus benefiting from the NxB model in terms of throughput for small deployments. In contrast to leader-based approaches, NxBFT&#x27;s performance is almost not impacted when actual crash faults occur.

  匹配依据：TEE: trusted execution environments

  </details>

- **Picachv: Formally Verified Data Use Policy Enforcement for Secure Data Analytics**
  2025-01-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.10560)
  Haobin Hiroki Chen, Hongbo Chen, Mingshen Sun, Chenghong Wang, XiaoFeng Wang

  <details><summary>摘要 / Abstract</summary>

  Ensuring the proper use of sensitive data in analytics under complex privacy policies is an increasingly critical challenge. Many existing approaches lack portability, verifiability, and scalability across diverse data processing frameworks. We introduce Picachv, a novel security monitor that automatically enforces data use policies. It works on relational algebra as an abstraction for program semantics, enabling policy enforcement on query plans generated by programs during execution. This approach simplifies analysis across diverse analytical operations and supports various front-end query languages. By formalizing both data use policies and relational algebra semantics in Coq, we prove that Picachv correctly enforces policies. Picachv also leverages Trusted Execution Environments (TEEs) to enhance trust in runtime, providing provable policy compliance to stakeholders that the analytical tasks comply with their data use policies. We integrated Picachv into Polars, a state-of-the-art data analytics framework, and evaluate its performance using the TPC-H benchmark. We also apply our approach to real-world use cases. Our work demonstrates the practical application of formal methods in securing data analytics, addressing key challenges.

  匹配依据：TEE: trusted execution environments

  </details>

- **Jodes: Efficient Oblivious Join in the Distributed Setting**
  2025-01-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.09334)
  Yilei Wang, Xiangdong Zeng, Sheng Wang, Feifei Li

  <details><summary>摘要 / Abstract</summary>

  Trusted execution environment (TEE) has provided an isolated and secure environment for building cloud-based analytic systems, but it still suffers from access pattern leakages caused by side-channel attacks. To better secure the data, computation inside TEE enclave should be made oblivious, which introduces significant overhead and severely slows down the computation. A natural way to speed up is to build the analytic system with multiple servers in the distributed setting. However, this setting raises a new security concern -- the volumes of the transmissions among these servers can leak sensitive information to a network adversary. Existing works have designed specialized algorithms to address this concern, but their supports for equi-join, one of the most important but non-trivial database operators, are either inefficient, limited, or under a weak security assumption. In this paper, we present Jodes, an efficient oblivious join algorithm in the distributed setting. Jodes prevents the leakage on both the network and enclave sides, supports a general equi-join operation, and provides a high security level protection that only publicizes the input sizes and the output size. Meanwhile, it achieves both communication cost and computation cost asymptotically superior to existing algorithms. To demonstrate the practicality of Jodes, we conduct experiments in the distributed setting comprising 16 servers. Empirical results show that Jodes achieves up to a sixfold performance improvement over state-of-the-art join algorithms.

  匹配依据：TEE: trusted execution environment

  </details>

- **Privacy-Preserving Data Quality Assessment for Time-Series IoT Sensors**
  2025-01-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.07154)
  Novoneel Chakraborty, Abhay Sharma, Jyotirmoy Dutta, Hari Dilip Kumar

  <details><summary>摘要 / Abstract</summary>

  Data from Internet of Things (IoT) sensors has emerged as a key contributor to decision-making processes in various domains. However, the quality of the data is crucial to the effectiveness of applications built on it, and assessment of the data quality is heavily context-dependent. Further, preserving the privacy of the data during quality assessment is critical in domains where sensitive data is prevalent. This paper proposes a novel framework for automated, objective, and privacy-preserving data quality assessment of time-series data from IoT sensors deployed in smart cities. We leverage custom, autonomously computable metrics that parameterise the temporal performance and adherence to a declarative schema document to achieve objectivity. Additionally, we utilise a trusted execution environment to create a &quot;data-blind&quot; model that ensures individual privacy, eliminates assessee bias, and enhances adaptability across data types. This paper describes this data quality assessment methodology for IoT sensors, emphasising its relevance within the smart-city context while addressing the growing need for privacy in the face of extensive data collection practices.

  匹配依据：TEE: trusted execution environment

  </details>

- **Validation of GPU Computation in Decentralized, Trustless Networks**
  2025-01-09 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.05374)
  Eric Boniardi, Stanley Bishop, Alison Haire

  <details><summary>摘要 / Abstract</summary>

  Verifying computational processes in decentralized networks poses a fundamental challenge, particularly for Graphics Processing Unit (GPU) computations. Our investigation reveals significant limitations in existing approaches: exact recomputation fails due to computational non-determinism across GPU nodes, Trusted Execution Environments (TEEs) require specialized hardware, and Fully Homomorphic Encryption (FHE) faces prohibitive computational costs. To address these challenges, we explore three verification methodologies adapted from adjacent technical domains: model fingerprinting techniques, semantic similarity analysis, and GPU profiling. Through systematic exploration of these approaches, we develop novel probabilistic verification frameworks, including a binary reference model with trusted node verification and a ternary consensus framework that eliminates trust requirements. These methodologies establish a foundation for ensuring computational integrity across untrusted networks while addressing the inherent challenges of non-deterministic execution in GPU-accelerated workloads.

  匹配依据：TEE: trusted execution environments

  </details>

- **SHARE: Optimizing Secure Hub Allocation and Routing Efficiency in Payment Channel Networks**
  2025-01-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.04236)
  Lingxiao Yang, Xuewen Dong, Wei Wang, Yong Yu, Sheng Gao, Qiang Qu, Yulong Shen

  <details><summary>摘要 / Abstract</summary>

  Payment channel hub (PCH), by leveraging a powerful hub to reliably provide off-chain payment services, offers an effective enhancement to payment channel networks (PCNs). However, existing approaches typically rely on a single hub to relay transactions and provide relationship anonymity between participants. This design lacks flexibility under high-frequency transaction scenarios and fail to adequately balance the security of off-chain payments with PCH efficiency. Moreover, current PCNs often adopt source routing, where each transaction path is predetermined without considering the dynamic distribution of large-scale payment requests, leading to load imbalance and even transaction deadlocks. To address these issues, we propose SHARE, a multi-PCH distributed routing scheme based on trusted execution environments (TEE), designed to optimize secure hub allocation and routing efficiency in PCNs. For the multi-hub allocation problem, SHARE balances the management and synchronization costs among participants, and employs mixed-integer linear programming along with supermodular optimization techniques to transform the NP-hard problem into a solvable form, enabling optimal or approximate solutions across various PCN scales. At the routing layer, SHARE integrates global network state with local sender requests to design a TEE-assisted, privacy-preserving distributed routing protocol that dynamically adjusts multipath flow rates, achieving high-throughput and deadlock-free transaction forwarding. We formally prove the security of the SHARE protocol under the universally composable framework. Experimental results demonstrate that SHARE achieves a 43.6% improvement in transaction success ratio and an over 181.5% enhancement in system throughput compared to state-of-the-art PCN solutions, effectively realizing a secure extension of PCNs.

  匹配依据：TEE: trusted execution environments

  </details>

- **TEE-based Key-Value Stores: a Survey**
  2025-01-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.03118)
  Aghiles Ait Messaoud, Sonia Ben Mokhtar, Anthony Simonet-Boulogne

  <details><summary>摘要 / Abstract</summary>

  Key-Value Stores (KVSs) are No-SQL databases that store data as key-value pairs and have gained popularity due to their simplicity, scalability, and fast retrieval capabilities. However, storing sensitive data in KVSs requires strong security properties to prevent data leakage and unauthorized tampering. While software (SW)-based encryption techniques are commonly used to maintain data confidentiality and integrity, they suffer from several drawbacks. They strongly assume trust in the hosting system stack and do not secure data during processing unless using performance-heavy techniques (e.g., homomorphic encryption). Alternatively, Trusted Execution Environments (TEEs) provide a solution that enforces the confidentiality and integrity of code and data at the CPU level, allowing users to build trusted applications in an untrusted environment. They also secure data in use by providing an encapsulated processing environment called enclave. Nevertheless, TEEs come with their own set of drawbacks, including performance issues due to memory size limitations and CPU context switching. This paper examines the state of the art in TEE-based confidential KVSs and highlights common design strategies used in KVSs to leverage TEE security features while overcoming their inherent limitations. This work aims to provide a comprehensive understanding of the use of TEEs in KVSs and to identify research directions for future work.

  匹配依据：TEE: trusted execution environments

  </details>

- **Privacy-Preserving Smart Contracts for Permissioned Blockchains: A zk-SNARK-Based Recipe Part-1**
  2025-01-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.03391)
  Aldenio Burgos, Eduardo Alchieri

  <details><summary>摘要 / Abstract</summary>

  The Bitcoin white paper introduced blockchain technology, enabling trustful transactions without intermediaries. Smart contracts emerged with Ethereum and blockchains expanded beyond cryptocurrency, applying to auctions, crowdfunding and electronic voting. However, blockchain&#x27;s transparency raised privacy concerns and initial anonymity measures proved ineffective. Smart contract privacy solutions employed zero-knowledge proofs, homomorphic encryption and trusted execution environments. These approaches have practical drawbacks, such as limited functionality, high computation times and trust on third parties requirements, being not fully decentralized. This work proposes a solution utilizing zk-SNARKs to provide privacy in smart contracts and blockchains. The solution supports both fungible and nonfungible tokens. Additionally, the proposal includes a new type of transactions, called delegated transactions, which enable use cases like Delivery vs Payment (DvP).

  匹配依据：TEE: trusted execution environments

  </details>

- **PM-Dedup: Secure Deduplication with Partial Migration from Cloud to Edge Servers**
  2025-01-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.02350)
  Zhaokang Ke, Haoyu Gong, David H. C. Du

  <details><summary>摘要 / Abstract</summary>

  Currently, an increasing number of users and enterprises are storing their data in the cloud but do not fully trust cloud providers with their data in plaintext form. To address this concern, they encrypt their data before uploading it to the cloud. However, encryption with different keys means that even identical data will become different ciphertexts, making deduplication less effective. Encrypted deduplication avoids this issue by ensuring that identical data chunks generate the same ciphertext with content-based keys, enabling the cloud to efficiently identify and remove duplicates even in encrypted form. Current encrypted data deduplication work can be classified into two types: target-based and source-based. Target-based encrypted deduplication requires clients to upload all encrypted chunks (the basic unit of deduplication) to the cloud with high network bandwidth overhead. Source-based deduplication involves clients uploading fingerprints (hashes) of encrypted chunks for duplicate checking and only uploading unique encrypted chunks, which reduces network transfer but introduces high latency and potential side-channel attacks, which need to be mitigated by Proof of Ownership (PoW), and high computing overhead of the cloud. So, reducing the latency and the overheads of network and cloud while ensuring security has become a significant challenge for secure data deduplication in cloud storage. In response to this challenge, we present PM-Dedup, a novel secure source-based deduplication approach that relocates a portion of the deduplication checking process and PoW tasks from the cloud to the trusted execution environments (TEEs) in the client-side edge servers. We also propose various designs to enhance the security and efficiency of data deduplication.

  匹配依据：TEE: trusted execution environments

  </details>

- **Fides: Secure and Scalable Asynchronous DAG Consensus via Trusted Components**
  2025-01-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.01062)
  Shaokang Xie, Dakai Kang, Hanzheng Lyu, Jianyu Niu, Mohammad Sadoghi

  <details><summary>摘要 / Abstract</summary>

  DAG-based BFT consensus has attracted growing interest in distributed data management systems for consistent replication in untrusted settings due to its high throughput and resilience to asynchrony. However, existing protocols still suffer from high communication overhead and long commit latency. In parallel, introducing minimal hardware trust has proven effective in reducing the complexity of BFT consensus. Inspired by these works, we present Fides, an asynchronous DAG-based BFT consensus protocol that, to our knowledge, is among the first to leverage TEEs to enhance both scalability and efficiency. Fides tolerates a minority of Byzantine replicas and achieves $O(κn^2 + n^3)$ metadata communication complexity through a customized TEE-assisted Reliable Broadcast (T-RBC) primitive with linear communication complexity in one-step broadcast. Building on T-RBC, Fides redefines the DAG construction rules by reducing the reference requirement from $2f+1$ to $f+1$ between consecutive vertices. This new structure weakens DAG connectivity and invalidates traditional commit rules, so we formally abstract the problem and derive new theoretical bounds of liveness. We further propose a four-round commit rule that achieves the theoretically minimal commit latency. Besides, we design two additional primitives, T-RoundCert and T-Coin, to efficiently certify DAG references and replace the costly cryptographic common coin used in prior protocols. Comprehensive evaluations on geo-distributed and local testbeds show that Fides substantially outperforms state-of-the-art protocols, including Tusk, Bullshark, Mysticeti, RCC, Damysus, Achilles and HybridSet, achieving lower latency and higher throughput while preserving strong safety and liveness guarantees.

  匹配依据：TEE: tees (context)

  </details>
