# 2025 · TEE · 仅预印本来源 · 第 1/2 页

[总目录](../PAPERS.md) · [下一页](2025-tee-preprint-02.md)

- **Verifiable Off-Chain Governance**
  2025-12-29 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.23618)
  Jake Hartnell, Eugenio Battaglia

  <details><summary>摘要 / Abstract</summary>

  Current DAO governance praxis limits organizational expressivity and reduces complex organizational decisions to token-weighted voting due to on-chain computational limits. This paper proposes verifiable off-chain computation (leveraging Verifiable Services, TEEs, and ZK proofs) as a framework to transcend these constraints while maintaining cryptoeconomic security. This paper explores three novel governance mechanisms: (1) attestation-based systems that compute multi-dimensional stakeholder legitimacy, (2) collective intelligence through verifiable preference processing, and (3) autonomous policy execution via Policy-as-Code. The framework provides architectural specifications, security models, and implementation considerations for DAOs seeking higher-resolution expressivity and increased operational efficiency, with validation from pioneering implementations demonstrating practical viability.

  匹配依据：TEE: tees (context)

  </details>

- **Abstraction of Trusted Execution Environments as the Missing Layer for Broad Confidential Computing Adoption: A Systematization of Knowledge**
  2025-12-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.22090)
  Quentin Michaud, Sara Ramezanian, Dhouha Ayed, Olivier Levillain, Joaquin Garcia-Alfaro

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) protect sensitive code and data from the operating system, hypervisor, or other untrusted software. Different solutions exist, each proposing different features. Abstraction layers aim to unify the ecosystem, allowing application developers and system administrators to leverage confidential computing as broadly and efficiently as possible. We start with an overview of representative available TEE technologies. We describe and summarize each TEE ecosystem, classifying them in different categories depending on their main design choices. Then, we propose a systematization of knowledge focusing on different abstraction layers around each design choice. We describe the underlying technologies of each design, as well as the inner workings and features of each abstraction layer. Our study reveals opportunities for improving existing abstraction layer solutions. It also highlights WebAssembly, a promising approach that supports the largest set of features. We close with a discussion on future directions for research, such as how future abstraction layers may evolve and integrate with the confidential computing ecosystem.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **zkFL-Health: Blockchain-Enabled Zero-Knowledge Federated Learning for Medical AI Privacy**
  2025-12-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.21048)
  Savvy Sharma, George Petrovic, Sarthak Kaushik

  <details><summary>摘要 / Abstract</summary>

  Healthcare AI needs large, diverse datasets, yet strict privacy and governance constraints prevent raw data sharing across institutions. Federated learning (FL) mitigates this by training where data reside and exchanging only model updates, but practical deployments still face two core risks: (1) privacy leakage via gradients or updates (membership inference, gradient inversion) and (2) trust in the aggregator, a single point of failure that can drop, alter, or inject contributions undetected. We present zkFL-Health, an architecture that combines FL with zero-knowledge proofs (ZKPs) and Trusted Execution Environments (TEEs) to deliver privacy-preserving, verifiably correct collaborative training for medical AI. Clients locally train and commit their updates; the aggregator operates within a TEE to compute the global update and produces a succinct ZK proof (via Halo2/Nova) that it used exactly the committed inputs and the correct aggregation rule, without revealing any client update to the host. Verifier nodes validate the proof and record cryptographic commitments on-chain, providing an immutable audit trail and removing the need to trust any single party. We outline system and threat models tailored to healthcare, the zkFL-Health protocol, security/privacy guarantees, and a performance evaluation plan spanning accuracy, privacy risk, latency, and cost. This framework enables multi-institutional medical AI with strong confidentiality, integrity, and auditability, key properties for clinical adoption and regulatory compliance.

  匹配依据：TEE: trusted execution environments

  </details>

- **A Systematic Review of Technical Defenses Against Software-Based Cheating in Online Multiplayer Games**
  2025-12-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.21377)
  Adwa Alangari, Ohoud Alharbi

  <details><summary>摘要 / Abstract</summary>

  This systematic literature review surveys technical defenses against software-based cheating in online multiplayer games. Categorizing existing approach-es into server-side detection, client-side anti-tamper, kernel-level anti-cheat drivers, and hardware-assisted TEEs. Each category is evaluated in terms of detection effectiveness, perfor-mance overhead, privacy im-pact, and scalability. The analy-sis highlights key trade-offs, particularly between the high visibility of kernel-level solutions and their privacy and stability risks, versus the low intrusive-ness but limited insight of server-side methods. Overall, the re-view emphasizes the ongoing arms race with cheaters and the need for robust, adversary-resistant anti-cheat designs.

  匹配依据：TEE: tees (context)

  </details>

- **Optimistic TEE-Rollups: A Hybrid Architecture for Scalable and Verifiable Generative AI Inference on Blockchain**
  2025-12-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.20176)
  Aaron Chan, Alex Ding, Frank Chen, Alan Wu, Bruce Zhang, Arther Tian

  <details><summary>摘要 / Abstract</summary>

  The rapid integration of Large Language Models (LLMs) into decentralized physical infrastructure networks (DePIN) is currently bottlenecked by the Verifiability Trilemma, which posits that a decentralized inference system cannot simultaneously achieve high computational integrity, low latency, and low cost. Existing cryptographic solutions, such as Zero-Knowledge Machine Learning (ZKML), suffer from superlinear proving overheads (O(k NlogN)) that render them infeasible for billionparameter models. Conversely, optimistic approaches (opML) impose prohibitive dispute windows, preventing real-time interactivity, while recent &quot;Proof of Quality&quot; (PoQ) paradigms sacrifice cryptographic integrity for subjective semantic evaluation, leaving networks vulnerable to model downgrade attacks and reward hacking. In this paper, we introduce Optimistic TEE-Rollups (OTR), a hybrid verification protocol that harmonizes these constraints. OTR leverages NVIDIA H100 Confidential Computing Trusted Execution Environments (TEEs) to provide sub-second Provisional Finality, underpinned by an optimistic fraud-proof mechanism and stochastic Zero-Knowledge spot-checks to mitigate hardware side-channel risks. We formally define Proof of Efficient Attribution (PoEA), a consensus mechanism that cryptographically binds execution traces to hardware attestations, thereby guaranteeing model authenticity. Extensive simulations demonstrate that OTR achieves 99% of the throughput of centralized baselines with a marginal cost overhead of $0.07 per query, maintaining Byzantine fault tolerance against rational adversaries even in the presence of transient hardware vulnerabilities.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **SoK: Verifiable Integrity Claims for Privacy-Preserving Federated Learning**
  2025-12-20 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2296)
  Andrea Rizzini, Marco Esposito, Tommaso Gagliardoni, Francesco Bruschi

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) is an advancement in Machine Learning motivated by the need to preserve the privacy of the data used to train models. While it effectively addresses this issue, the multi-participant paradigm on which it is based introduces several challenges. Among these are the risks that participating entities may behave dishonestly and fail to perform their tasks correctly. This misbehavior, in turn, also threatens privacy, because an undetected deviation in training or aggregation can silently undermine the confidentiality guarantees that FL was designed to provide. This motivates mechanisms that provide checkable evidence that released checkpoints are consistent with a declared learning specification and an auditable execution trace. In this SoK, we model federated learning as an append-only transcript of submissions, admissions, aggregation, and finalization events, and formalize verifiability as a collection of integrity claims issued by clients and the aggregator, and checked by different verifier classes. We derive a taxonomy of recurring client-side and aggregator-side claims and use it to analyze representative verifiable FL (VFL) systems spanning Zero-Knowledge Proofs (ZKP) and Trusted Execution Environment (TEE) technologies. Our analysis suggests that, while verifiable aggregation is comparatively mature, data verifiability appears feasible but still sparsely adopted in practice, and verifiable training remain costly and rarely scale to modern models.

  匹配依据：TEE: trusted execution environment

  </details>

- **QLink: Quantum-Safe Bridge Architecture for Blockchain Interoperability**
  2025-12-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.18488)
  Joao Vitor Barros Da Silva, Arsh Gupta, Madhusudan Singh Irish Singh

  <details><summary>摘要 / Abstract</summary>

  Secure interoperability across heterogeneous blockchains remains one of the most pressing challenges in Web3 with existing bridge protocols vulnerable to both classical exploits and emerging quantum threats. This paper introduces QLink a quantum-safe Layer 3 interoperability protocol that integrates postquantum cryptography (PQC) quantum key distribution (QKD) and hardware security modules (HSMs) into a unified validator architecture. To our knowledge, QLink is the first interoperability framework to combine these mechanisms to secure validator communication proof aggregation and key management. Validators exchange encryption keys through QKD channels, achieving information-theoretic security against interception, while cross-chain proofs are generated and aggregated with NIST-standardized PQC algorithms. Private keys remain sealed inside HSM enclaves mitigating the risk of theft or leakage. Deployed as a dedicated Layer 3 protocol QLink operates independently of Layer 1 and Layer 2 chains providing a scalable decentralized foundation for secure cross-chain messaging and asset transfer. Experimental evaluation using network simulations demonstrates that validator communication overhead remains sub-second while security guarantees extend beyond current bridge architectures to resist both classical and quantum adversaries. By addressing today vulnerabilities and anticipating future quantum threats QLink establishes a practical and future-proof pathway for blockchain interoperability.

  匹配依据：TEE: enclaves (context)

  </details>

- **Trustworthy and Controllable Professional Knowledge Utilization in Large Language Models with TEE-GPU Execution**
  2025-12-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.16238)
  Yifeng Cai, Zhida An, Yuhan Meng, Houqian Liu, Pengli Wang, Hanwen Lei, Yao Guo, Ding Li

  <details><summary>摘要 / Abstract</summary>

  Future improvements in large language model (LLM) services increasingly hinge on access to high-value professional knowledge rather than more generic web data. However, the data providers of this knowledge face a skewed tradeoff between income and risk: they receive little share of downstream value yet retain copyright and privacy liability, making them reluctant to contribute their assets to LLM services. Existing techniques do not offer a trustworthy and controllable way to use professional knowledge, because they keep providers in the dark and combine knowledge parameters with the underlying LLM backbone. In this paper, we present PKUS, the Professional Knowledge Utilization System, which treats professional knowledge as a first-class, separable artifact. PKUS keeps the backbone model on GPUs and encodes each provider&#x27;s contribution as a compact adapter that executes only inside an attested Trusted Execution Environment (TEE). A hardware-rooted lifecycle protocol, adapter pruning, multi-provider aggregation, and split-execution scheduling together make this design practical at serving time. On SST-2, MNLI, and SQuAD with GPT-2 Large and Llama-3.2-1B, PKUS preserves model utility, matching the accuracy and F1 of full fine-tuning and plain LoRA, while achieving the lowest per-request latency with 8.1-11.9x speedup over CPU-only TEE inference and naive CPU-GPU co-execution.

  匹配依据：TEE: trusted execution environment

  </details>

- **Secure Distributed State Management for Stateful Signatures with a Practical and Universally Composable Protocol**
  2025-12-18 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2278)
  Johannes Blömer, Henrik Bröcher, Volker Krummel, Laurens Porzenheim

  <details><summary>摘要 / Abstract</summary>

  Stateful signatures like the NIST standardized signature schemes LMS and XMSS provide an efficient and mature realization of post-quantum secure signature schemes. They are recommended for long-term use cases like e.g. firmware signing. However, stateful signature schemes require to properly manage a so-called state. In stateful signature schemes like LMS and XMSS, signing keys consist of a set of keys of a one-time signature scheme and it has to be guaranteed that each one-time key is used only once. This is done by updating a state in each signature computation, basically recording which one-time keys have already been used. While this is straightforward in centralized systems, in distributed systems like secure enclaves consisting of e.g. multiple hardware security modules (HSMs) with limited communication keeping a distributed state that at any point in time is consistent among all parties involved presents a challenge. This challenge is not addressed by the current standardization processes. In this paper we present a security model for the distributed key management of post-quantum secure stateful signatures like XMSS and LMS. We also present a simple, efficient, and easy to implement protocol proven secure in this security model, i.e. the protocol guarantees at any point in time a consistent state among the parties in a distributed system, like a distributed security enclave. The security model is defined in the universal composabilty (UC) framework by Ran Canetti by providing an ideal functionality for the distributed key management for stateful signatures. Hence our protocol remains secure even if arbitrarily composed with other instances of the same or other protocols, a necessity for the security of distributed key management protocols. Our main application are security enclaves consisting of HSMs, but the model and the protocol can easily be adapted to other scenarios of distributed key management of stateful signature schemes.

  匹配依据：TEE: secure enclaves

  </details>

- **VET Your Agent: Towards Host-Independent Autonomy via Verifiable Execution Traces**
  2025-12-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.15892)
  Artem Grigor, Christian Schroeder de Witt, Simon Birnbach, Ivan Martinovic

  <details><summary>摘要 / Abstract</summary>

  Recent advances in large language models (LLMs) have enabled a new generation of autonomous agents that operate over sustained periods and manage sensitive resources on behalf of users. Trusted for their ability to act without direct oversight, such agents are increasingly considered in high-stakes domains including financial management, dispute resolution, and governance. Yet in practice, agents execute on infrastructure controlled by a host, who can tamper with models, inputs, or outputs, undermining any meaningful notion of autonomy. We address this gap by introducing VET (Verifiable Execution Traces), a formal framework that achieves host-independent authentication of agent outputs and takes a step toward host-independent autonomy. Central to VET is the Agent Identity Document (AID), which specifies an agent&#x27;s configuration together with the proof systems required for verification. VET is compositional: it supports multiple proof mechanisms, including trusted hardware, succinct cryptographic proofs, and notarized TLS transcripts (Web Proofs). We implement VET for an API-based LLM agent and evaluate our instantiation on realistic workloads. We find that for today&#x27;s black-box, secret-bearing API calls, Web Proofs appear to be the most practical choice, with overhead typically under 3$\times$ compared to direct API calls, while for public API calls, a lower-overhead TEE Proxy is often sufficient. As a case study, we deploy a verifiable trading agent that produces proofs for each decision and composes Web Proofs with a TEE Proxy. Our results demonstrate that practical, host-agnostic authentication is already possible with current technology, laying the foundation for future systems that achieve full host-independent autonomy.

  匹配依据：TEE: tee (context)

  </details>

- **Lost in the Pages: WebAssembly Code Recovery through SEV-SNP's Exposed Address Space**
  2025-12-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.14376)
  Markus Berthilsson, Christian Gehrmann

  <details><summary>摘要 / Abstract</summary>

  WebAssembly (Wasm) has risen as a widely used technology to distribute computing workloads on different platforms. The platform independence offered through Wasm makes it an attractive solution for many different applications that can run on disparate infrastructures. In addition, Trusted Execution Environments (TEEs) are offered in many computing infrastructures, which allows also running security sensitive Wasm workloads independent of the specific platforms offered. However, recent work has shown that Wasm binaries are more sensitive to code confidentiality attacks than native binaries. The previous result was obtained for Intel SGX only. In this paper, we take this one step further, introducing a new Wasm code-confidentiality attack that exploits exposed address-space information in TEEs. Our attack enables the extraction of crucial execution features which, when combined with additional side channels, allows us to with high reliability obtain more than 70% of the code in most cases. This is a considerably larger amount than was previously obtained by single stepping Intel SGX where only upwards to 50% of the code could be obtained.

  匹配依据：TEE: intel sgx, sev snp, trusted execution environments

  </details>

- **Verification of Lightning Network Channel Balances with Trusted Execution Environments (TEE)**
  2025-12-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.12095)
  Vikash Singh, Barrett Little, Philip Hayes, Max Fang, Matthew Khanzadeh, Alyse Killeen, Sam Abbassi

  <details><summary>摘要 / Abstract</summary>

  Verifying the private liquidity state of Lightning Network (LN) channels is desirable for auditors, service providers, and network participants who need assurance of financial capacity. Current methods often lack robustness against a malicious or compromised node operator. This paper introduces a methodology for the verification of LN channel balances. The core contribution is a framework that combines Trusted Execution Environments (TEEs) with Zero-Knowledge Transport Layer Security (zkTLS) to provide strong, hardware-backed guarantees. In our proposed method, the node&#x27;s balance-reporting software runs within a TEE, which generates a remote attestation quote proving the software&#x27;s integrity. This attestation is then served via an Application Programming Interface (API), and zkTLS is used to prove the authenticity of its delivery. We also analyze an alternative variant where the TEE signs the report directly without zkTLS, discussing the trade-offs between transport-layer verification and direct enclave signing. We further refine this by distinguishing between &quot;Hot Proofs&quot; (verifiable claims via TEEs) and &quot;Cold Proofs&quot; (on-chain settlement), and discuss critical security considerations including hardware vulnerabilities, privacy leakage to third-party APIs, and the performance overhead of enclaved operations.

  匹配依据：TEE: trusted execution environments

  </details>

- **TriHaRd: Higher Resilience for TEE Trusted Time**
  2025-12-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.10732)
  Matthieu Bettinger, Sonia Ben Mokhtar, Pascal Felber, Etienne Rivière, Valerio Schiavoni, Anthony Simonet-Boulogne

  <details><summary>摘要 / Abstract</summary>

  Accurately measuring time passing is critical for many applications. However, in Trusted Execution Environments (TEEs) such as Intel SGX, the time source is outside the Trusted Computing Base: a malicious host can manipulate the TEE&#x27;s notion of time, jumping in time or affecting perceived time speed. Previous work (Triad) proposes protocols for TEEs to maintain a trustworthy time source by building a cluster of TEEs that collaborate with each other and with a remote Time Authority to maintain a continuous notion of passing time. However, such approaches still allow an attacker to control the operating system and arbitrarily manipulate their own TEE&#x27;s perceived clock speed. An attacker can even propagate faster passage of time to honest machines participating in Triad&#x27;s trusted time protocol, causing them to skip to timestamps arbitrarily far in the future. We propose TriHaRd, a TEE trusted time protocol achieving high resilience against clock speed and offset manipulations, notably through Byzantine-resilient clock updates and consistency checks. We empirically show that TriHaRd mitigates known attacks against Triad.

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **Proof of Trusted Execution: A Consensus Paradigm for Deterministic Blockchain Finality**
  2025-12-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.09409)
  Kyle Habib, Vladislav Kapitsyn, Giovanni Mazzeo, Faisal Mehrban

  <details><summary>摘要 / Abstract</summary>

  Current blockchain consensus protocols -- notably, Proof of Work (PoW) and Proof of Stake (PoS) -- deliver global agreement but exhibit structural constraints. PoW anchors security in heavy computation, inflating energy use and imposing high confirmation latency. PoS improves efficiency but introduces stake concentration, long-range and &quot;nothing-at-stake&quot; vulnerabilities, and a hard performance ceiling shaped by slot times and multi-round committee voting. In this paper, we propose Proof of Trusted Execution (PoTE), a consensus paradigm where agreement emerges from verifiable execution rather than replicated re-execution. Validators operate inside heterogeneous VM-based TEEs, each running the same canonical program whose measurement is publicly recorded, and each producing vendor-backed attestations that bind the enclave code hash to the block contents. Because the execution is deterministic and the proposer is uniquely derived from public randomness, PoTE avoids forks, eliminates slot.time bottlenecks, and commits blocks in a single round of verification. We present the design of a PoTE consensus client, describe our reference implementation, and evaluate its performance against the stringent throughput requirements of the Trillion decentralized exchange.

  匹配依据：TEE: tees (context)

  </details>

- **CapsuleFS A Multi-credential DataCapsule Filesystem**
  2025-12-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.08067)
  Qingyang Hu, Yucheng Huang, Manshi Yang

  <details><summary>摘要 / Abstract</summary>

  CapsuleFS (CFS) is the first filesystem to integrate multi-credential functionality within a POSIX-compliant framework, utilizing DataCapsule as the storage provider. This innovative system is established based on the Global Data Plane in the area of edge computing. Our comprehensive design and implementation of CFS successfully fulfill the objective of providing a multi-credential Common Access API. The architecture of CFS is methodically segmented into three integral components: Firstly, the DataCapsule server, tasked with the storage, dissemination, and replication of DataCapsules on the edge. Secondly, the middleware, a crucial element running in a Trusted Execution Environment responsible for the enforcement and management of write permissions and requests. Finally, the client component, which manifests as a POSIX-compliant filesystem, is adaptable and operational across many architectures. Experimental evaluations of CFS reveal that, while its read and write performances are comparatively modest, it upholds a high degree of functional correctness. This attribute distinctly positions CFS as a viable candidate for application in real-world software development scenarios. The paper also delineates potential future enhancements, aimed at augmenting the practicality of CFS in the landscape of software development.

  匹配依据：TEE: trusted execution environment

  </details>

- **Amulet: Fast TEE-Shielded Inference for On-Device Model Protection**
  2025-12-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.07495)
  Zikai Mao, Lingchen Zhao, Lei Xu, Wentao Dong, Shenyi Zhang, Cong Wang, Qian Wang

  <details><summary>摘要 / Abstract</summary>

  On-device machine learning (ML) introduces new security concerns about model privacy. Storing valuable trained ML models on user devices exposes them to potential extraction by adversaries. The current mainstream solution for on-device model protection is storing the weights and conducting inference within Trusted Execution Environments (TEEs). However, due to limited trusted memory that cannot accommodate the whole model, most existing approaches employ a partitioning strategy, dividing a model into multiple slices that are loaded into the TEE sequentially. This frequent interaction between untrusted and trusted worlds dramatically increases inference latency, sometimes by orders of magnitude. In this paper, we propose Amulet, a fast TEE-shielded on-device inference framework for ML model protection. Amulet incorporates a suite of obfuscation methods specifically designed for common neural network architectures. After obfuscation by the TEE, the entire transformed model can be securely stored in untrusted memory, allowing the inference process to execute directly in untrusted memory with GPU acceleration. For each inference request, only two rounds of minimal-overhead interaction between untrusted and trusted memory are required to process input samples and output results. We also provide theoretical proof from an information-theoretic perspective that the obfuscated model does not leak information about the original weights. We comprehensively evaluated Amulet using diverse model architectures ranging from ResNet-18 to GPT-2. Our approach incurs inference latency only 2.8-4.8x that of unprotected models with negligible accuracy loss, achieving an 8-9x speedup over baseline methods that execute inference entirely within TEEs, and performing approximately 2.2x faster than the state-of-the-art obfuscation-based method.

  匹配依据：TEE: trusted execution environments

  </details>

- **PDRIMA: A Policy-Driven Runtime Integrity Measurement and Attestation Approach for ARM TrustZone-based TEE**
  2025-12-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.06500)
  Jingkai Mao, Xiaolin Chang

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) such as ARM TrustZone are widely used in IoT and embedded devices to protect sensitive code and data. However, most existing defenses focus on secure boot or REE-side monitoring and provide little visibility into the runtime integrity of the TEE. This leaves TrustZone-based devices exposed to persistent TEE compromises. We propose Policy-Driven Runtime Integrity Measurement and Attestation (PDRIMA), a runtime integrity protection approach for TrustZone-based TEEs. PDRIMA systematically analyzes TEE attack surfaces and introduces two in-TEE subsystems: a Secure Monitor Agent (SMA) that performs policy-driven measurement, appraisal, logging, and time-based re-measurement over the TEE kernel, static components, user-TAs, and security-critical system calls; and a Remote Attestation Agent (RAA) that aggregates tamper-evident evidence and exposes a remote attestation protocol for verifying. We analyze PDRIMA&#x27;s security against identified attack surfaces, implement a prototype on OP-TEE for Raspberry Pi 3B+, and evaluate its performance overhead to indicate its practicability.

  匹配依据：TEE: trusted execution environments, trustzone

  </details>

- **Trusted AI Agents in the Cloud**
  2025-12-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.05951)
  Teofil Bodea, Masanori Misono, Julian Pritzi, Patrick Sabanic, Thore Sommer, Harshavardhan Unnibhavi, David Schall, Nuno Santos, Dimitrios Stavrakakis, Pramod Bhatotia

  <details><summary>摘要 / Abstract</summary>

  AI agents powered by large language models are increasingly deployed as cloud services that autonomously access sensitive data, invoke external tools, and interact with other agents. However, these agents run within a complex multi-party ecosystem, where untrusted components can lead to data leakage, tampering, or unintended behavior. Existing Confidential Virtual Machines (CVMs) provide only per binary protection and offer no guarantees for cross-principal trust, accelerator-level isolation, or supervised agent behavior. We present Omega, a system that enables trusted AI agents by enforcing end-to-end isolation, establishing verifiable trust across all contributing principals, and supervising every external interaction with accountable provenance. Omega builds on Confidential VMs and Confidential GPUs to create a Trusted Agent Platform that hosts many agents within a single CVM using nested isolation. It also provides efficient multi-agent orchestration with cross-principal trust establishment via differential attestation, and a policy specification and enforcement framework that governs data access, tool usage, and inter-agent communication for data protection and regulatory compliance. Implemented on AMD SEV-SNP and NVIDIA H100, Omega fully secures agent state across CVM-GPU, and achieves high performance while enabling high-density, policy-compliant multi-agent deployments at cloud scale.

  匹配依据：TEE: amd sev

  </details>

- **CAEC: Confidential, Attestable, and Efficient Inter-CVM Communication with Arm CCA**
  2025-12-01 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.01594)
  Sina Abdollahi, Amir Al Sadi, David Kotz, Marios Kogias, Hamed Haddadi

  <details><summary>摘要 / Abstract</summary>

  Confidential Virtual Machines (CVMs) are increasingly adopted to protect sensitive workloads from privileged adversaries such as the hypervisor. While they provide strong isolation guarantees, existing CVM architectures lack first-class mechanisms for inter-CVM data sharing due to their disjoint memory model, making inter-CVM data exchange a performance bottleneck in compartmentalized or collaborative multi-CVM systems. Under this model, a CVM&#x27;s accessible memory is either shared with the hypervisor or protected from both the hypervisor and all other CVMs. This design simplifies reasoning about memory ownership; however, it fundamentally precludes plaintext data sharing between CVMs because all inter-CVM communication must pass through hypervisor-accessible memory, requiring costly encryption and decryption to preserve confidentiality and integrity. In this paper, we introduce CAEC, a system that enables protected memory sharing between CVMs. CAEC builds on Arm Confidential Compute Architecture (CCA) and extends its firmware to support Confidential Shared Memory (CSM), a memory region securely shared between multiple CVMs while remaining inaccessible to the hypervisor and all non-participating CVMs. CAEC&#x27;s design is fully compatible with CCA hardware and introduces only a modest increase (6%) in CCA firmware code size. CAEC delivers substantial performance benefits across a range of workloads. For instance, inter-CVM communication over CAEC achieves up to 209x reduction in CPU cycles compared to encryption-based mechanisms over hypervisor-accessible shared memory. By combining high performance, strong isolation guarantees, and attestable sharing semantics, CAEC provides a practical and scalable foundation for the next generation of trusted multi-CVM services across both edge and cloud environments.

  匹配依据：TEE: arm cca, confidential compute architecture

  </details>

- **Enhancing the Security of Rollup Sequencers using Decentrally Attested TEEs**
  2025-11-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.22317)
  Giovanni Maria Cristiano, Salvatore D'Antonio, Jonah Giglio, Giovanni Mazzeo, Luigi Romano

  <details><summary>摘要 / Abstract</summary>

  The growing scalability demand of public Blockchains led to the rise of Layer-2 solutions, such as Rollups. Rollups improve transaction throughput by processing operations off-chain and posting the results on-chain. A critical component in Rollups is the Sequencer, responsible for receiving, ordering and batching transactions before they are submitted to the Layer-1 blockchain. While essential, the centralized nature of the Sequencer makes it vulnerable to attacks, such as censorship, transaction manipulation and tampering. To enhance its security, there are solutions in the literature that shield the Sequencer inside a Trusted Execution Environment (TEE). However, the attestation of TEEs introduces additional centralization, which is in contrast with the core Blockchain principle. In this paper, we propose a TEE-secured Sequencer equipped with a decentralized attestation mechanism. We outline the design and implementation of our solution, covering the system architecture, TEE integration, and the decentralization of the attestation process. Additionally, we present an experimental evaluation conducted on a realistic Rollup testnet. Our results show that this approach strengthens Sequencer integrity without sacrificing compatibility or deployability in existing Layer-2 architectures.

  匹配依据：TEE: trusted execution environment

  </details>

- **TICAL: Trusted and Integrity-protected Compilation of AppLications**
  2025-11-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.17070)
  Robert Krahn, Nikson Kanti Paul, Franz Gregor, Do Le Quoc, Andrey Brito, André Martin, Christof Fetzer

  <details><summary>摘要 / Abstract</summary>

  During the past few years, we have witnessed various efforts to provide confidentiality and integrity for applications running in untrusted environments such as public clouds. In most of these approaches, hardware extensions such as Intel SGX, TDX, AMD SEV, etc., are leveraged to provide encryption and integrity protection on process or VM level. Although all of these approaches increase the trust in the application at runtime, an often overlooked aspect is the integrity and confidentiality protection at build time, which is equally important as maliciously injected code during compilation can compromise the entire application and system. In this paper, we present Tical, a practical framework for trusted compilation that provides integrity protection and confidentiality in build pipelines from source code to the final executable. Our approach harnesses TEEs as runtime protection but enriches TEEs with file system shielding and an immutable audit log with version history to provide accountability. This way, we can ensure that the compiler chain can only access trusted files and intermediate output, such as object files produced by trusted processes. Our evaluation using micro- and macro-benchmarks shows that Tical can protect the confidentiality and integrity of whole CI/CD pipelines with an acceptable performance overhead.

  匹配依据：TEE: amd sev, intel sgx

  </details>

- **Constant-Size Cryptographic Evidence Structures for Regulated AI Workflows**
  2025-11-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.17118)
  Leo Kao

  <details><summary>摘要 / Abstract</summary>

  Regulated AI workflows (such as clinical trials, medical decision support, and financial compliance) must satisfy strict auditability and integrity requirements. Existing audit-trail mechanisms rely on variable-length records, bulky cryptographic transcripts, or ad-hoc schemas, suffering from metadata leakage, irregular performance, and weak alignment with formal security notions.This paper introduces constant-size cryptographic evidence structures, a general abstraction for verifiable audit evidence in regulated AI workflows. Each evidence item is a fixed-size tuple of cryptographic fields designed to (i) bind strongly to workflow events and configurations, (ii) support constant-size storage and uniform verification cost per event, and (iii) compose cleanly with hash-chain and Merkle-based audit constructions. We formalize a model of regulated AI workflows, define syntax and algorithms for evidence structures, and prove security properties (evidence binding, tamper detection, and non-equivocation) via game-based definitions under standard assumptions (collision-resistant hashing and EUF-CMA signatures).We present a generic hash-and-sign construction using a collision-resistant hash function and a standard signature scheme, and show how to integrate it with hash-chained logs, Merkle-tree anchoring, and trusted execution environments. We implement a prototype library and report microbenchmarks on commodity hardware, demonstrating that per-event overhead is small and predictable. This work aims to provide a foundation for standardized audit mechanisms in regulated AI, with implications for clinical trial management, pharmaceutical compliance, and medical AI governance.

  匹配依据：TEE: trusted execution environments

  </details>

- **Decentralized Proposer-as-a-Service (DPaaS): Improving Decentralization and Trustworthiness in Ethereum PBS**
  2025-11-20 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2126)
  Chenyang Liu, Arnav Jindal, Ittai Abraham, Matthew Lentz, Kartik Nayak

  <details><summary>摘要 / Abstract</summary>

  Proposer-Builder Separation (PBS) in Ethereum aims to improve decentralization and scalability by offloading block construction to specialized builders, but its current MEV-Boost implementation relies on trusted relays, introducing centralization as well as security and performance concerns. We propose Decentralized Proposer-as-a-Service (DPaaS) to eliminate relays while preserving compatibility with Ethereum’s consensus layer by distributing the combined proposer and relay roles across Proposer Entities (PEs) running in independent Trusted Execution Environments (TEEs). DPaaS presents itself to Ethereum as a single validator using threshold BLS signatures, while a new Byzantine broadcast protocol decentralizes the auctioneer role with censorship-resistance and availability-backed guarantees. Our evaluation, deployed across four independent cloud hosts and driven by real-world traces, shows that DPaaS achieves $\leq 6$ ms bid processing latency, $68.7$ ms latency from the end of auction to block proposal, and $3.3\%$ more MEV earnings – demonstrating that DPaaS can offer security, decentralization, and trustworthiness benefits while providing strong performance.

  匹配依据：TEE: trusted execution environments

  </details>

- **Securing Generative AI in Healthcare: A Zero-Trust Architecture Powered by Confidential Computing on Google Cloud**
  2025-11-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.11836)
  Adaobi Amanna, Ishana Shinde

  <details><summary>摘要 / Abstract</summary>

  The integration of Generative Artificial Intelligence (GenAI) in healthcare is impeded by significant security challenges unaddressed by traditional frameworks, precisely the data-in-use gap where sensitive patient data and proprietary AI models are exposed during active processing. To address this, the paper proposes the Confidential Zero-Trust Framework (CZF), a novel security paradigm that synergistically combines Zero-Trust Architecture for granular access control with the hardware-enforced data isolation of Confidential Computing. We detailed a multi-tiered architectural blueprint for implementing the CZF on Google Cloud and analyzed its efficacy against real-world threats. The CZF provides a defense-in-depth architecture where data remains encrypted while in-use within a hardware-based Trusted Execution Environment (TEE). The framework&#x27;s use of remote attestation offers cryptographic proof of workload integrity, transforming compliance from a procedural exercise into a verifiable technical fact and enabling secure, multi-party collaborations previously blocked by security and intellectual property concerns. By closing the data-in-use gap and enforcing Zero-Trust principles, the CZF provides a robust and verifiable framework that establishes the necessary foundation of trust to enable the responsible adoption of transformative AI technologies in healthcare.

  匹配依据：TEE: confidential computing, trusted execution environment

  </details>

- **A Workflow for Full Traceability of AI Decisions**
  2025-11-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.11275)
  Julius Wenzel, Syeda Umaima Alam, Andreas Schmidt, Hanwei Zhang, Holger Hermanns

  <details><summary>摘要 / Abstract</summary>

  An ever increasing number of high-stake decisions are made or assisted by automated systems employing brittle artificial intelligence technology. There is a substantial risk that some of these decision induce harm to people, by infringing their well-being or their fundamental human rights. The state-of-the-art in AI systems makes little effort with respect to appropriate documentation of the decision process. This obstructs the ability to trace what went into a decision, which in turn is a prerequisite to any attempt of reconstructing a responsibility chain. Specifically, such traceability is linked to a documentation that will stand up in court when determining the cause of some AI-based decision that inadvertently or intentionally violates the law. This paper takes a radical, yet practical, approach to this problem, by enforcing the documentation of each and every component that goes into the training or inference of an automated decision. As such, it presents the first running workflow supporting the generation of tamper-proof, verifiable and exhaustive traces of AI decisions. In doing so, we expand the DBOM concept into an effective running workflow leveraging confidential computing technology. We demonstrate the inner workings of the workflow in the development of an app to tell poisonous and edible mushrooms apart, meant as a playful example of high-stake decision support.

  匹配依据：TEE: confidential computing

  </details>

- **Experiences Building Enterprise-Level Privacy-Preserving Federated Learning to Power AI for Science**
  2025-11-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.08998)
  Zilinghan Li, Aditya Sinha, Yijiang Li, Kyle Chard, Kibaek Kim, Ravi Madduri

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) is a promising approach to enabling collaborative model training without centralized data sharing, a crucial requirement in scientific domains where data privacy, ownership, and compliance constraints are critical. However, building user-friendly enterprise-level FL frameworks that are both scalable and privacy-preserving remains challenging, especially when bridging the gap between local prototyping and distributed deployment across heterogeneous client computing infrastructures. In this paper, based on our experiences building the Advanced Privacy-Preserving Federated Learning (APPFL) framework, we present our vision for an enterprise-grade, privacy-preserving FL framework designed to scale seamlessly across computing environments. We identify several key capabilities that such a framework must provide: (1) Scalable local simulation and prototyping to accelerate experimentation and algorithm design; (2) seamless transition from simulation to deployment; (3) distributed deployment across diverse, real-world infrastructures, from personal devices to cloud clusters and HPC systems; (4) multi-level abstractions that balance ease of use and research flexibility; and (5) comprehensive privacy and security through techniques such as differential privacy, secure aggregation, robust authentication, and confidential computing. We further discuss architectural designs to realize these goals. This framework aims to bridge the gap between research prototypes and enterprise-scale deployment, enabling scalable, reliable, and privacy-preserving AI for science.

  匹配依据：TEE: confidential computing

  </details>

- **Secure Autonomous Agent Payments: Verifying Authenticity and Intent in a Trustless Environment**
  2025-11-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.15712)
  Vivek Acharya

  <details><summary>摘要 / Abstract</summary>

  Artificial intelligence (AI) agents are increasingly capable of initiating financial transactions on behalf of users or other agents. This evolution introduces a fundamental challenge: verifying both the authenticity of an autonomous agent and the true intent behind its transactions in a decentralized, trustless environment. Traditional payment systems assume human authorization, but autonomous, agent-led payments remove that safeguard. This paper presents a blockchain-based framework that cryptographically authenticates and verifies the intent of every AI-initiated transaction. The proposed system leverages decentralized identity (DID) standards and verifiable credentials to establish agent identities, on-chain intent proofs to record user authorization, and zero-knowledge proofs (ZKPs) to preserve privacy while ensuring policy compliance. Additionally, secure execution environments (TEE-based attestations) guarantee the integrity of agent reasoning and execution. The hybrid on-chain/off-chain architecture provides an immutable audit trail linking user intent to payment outcome. Through qualitative analysis, the framework demonstrates strong resistance to impersonation, unauthorized transactions, and misalignment of intent. This work lays the foundation for secure, auditable, and intent-aware autonomous economic agents, enabling a future of verifiable trust and accountability in AI-driven financial ecosystems.

  匹配依据：TEE: tee (context)

  </details>

- **Confidential Computing for Cloud Security: Exploring Hardware based Encryption Using Trusted Execution Environments**
  2025-11-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.04550)
  Dhruv Deepak Agarwal, Aswani Kumar Cherukuri

  <details><summary>摘要 / Abstract</summary>

  The growth of cloud computing has revolutionized data processing and storage capacities to another levels of scalability and flexibility. But in the process, it has created a huge challenge of security, especially in terms of safeguarding sensitive data. Classical security practices, including encryption at rest and during transit, fail to protect data in use and expose it to various possible breaches. In response to this problem , Confidential Computing has been a tool ,seeking to secure data in processing by usage of hardware-based Trusted Execution Environments (TEEs). TEEs, including Intel&#x27;s Software Guard Extensions (SGX) and ARM&#x27;s TrustZone, offers protected contexts within the processor, where data is kept confidential ,intact and secure , even with malicious software or compromised operating systems. In this research, we have explored the architecture and security features of TEEs like Intel SGX and ARM TrustZone, and their effectiveness in improving cloud data security. From a thorough literature survey ,we have analyzed the deployment strategies, performance indicators, and practical uses of these TEEs for the same purpose. In addition, we have discussed the issues regarding deployment, possible weaknesses, scalability issues, and integration issues. Our results focuses on the central position of TEEs in strengthening and advancing cloud security infrastructures, pointing towards their ability to create a secure foundation for Confidential Computing.

  匹配依据：TEE: confidential computing, intel sgx, sgx, trusted execution environments, trustzone

  </details>

- **Inter-Agent Trust Models: A Comparative Study of Brief, Claim, Proof, Stake, Reputation and Constraint in Agentic Web Protocol Design-A2A, AP2, ERC-8004, and Beyond**
  2025-11-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.03434)
  Botao 'Amber' Hu, Helena Rong

  <details><summary>摘要 / Abstract</summary>

  As the &quot;agentic web&quot; takes shape-billions of AI agents (often LLM-powered) autonomously transacting and collaborating-trust shifts from human oversight to protocol design. In 2025, several inter-agent protocols crystallized this shift, including Google&#x27;s Agent-to-Agent (A2A), Agent Payments Protocol (AP2), and Ethereum&#x27;s ERC-8004 &quot;Trustless Agents,&quot; yet their underlying trust assumptions remain under-examined. This paper presents a comparative study of trust models in inter-agent protocol design: Brief (self- or third-party verifiable claims), Claim (self-proclaimed capabilities and identity, e.g. AgentCard), Proof (cryptographic verification, including zero-knowledge proofs and trusted execution environment attestations), Stake (bonded collateral with slashing and insurance), Reputation (crowd feedback and graph-based trust signals), and Constraint (sandboxing and capability bounding). For each, we analyze assumptions, attack surfaces, and design trade-offs, with particular emphasis on LLM-specific fragilities-prompt injection, sycophancy/nudge-susceptibility, hallucination, deception, and misalignment-that render purely reputational or claim-only approaches brittle. Our findings indicate no single mechanism suffices. We argue for trustless-by-default architectures anchored in Proof and Stake to gate high-impact actions, augmented by Brief for identity and discovery and Reputation overlays for flexibility and social signals. We comparatively evaluate A2A, AP2, ERC-8004 and related historical variations in academic research under metrics spanning security, privacy, latency/cost, and social robustness (Sybil/collusion/whitewashing resistance). We conclude with hybrid trust model recommendations that mitigate reputation gaming and misinformed LLM behavior, and we distill actionable design guidelines for safer, interoperable, and scalable agent economies.

  匹配依据：TEE: trusted execution environment

  </details>

- **On new variants of funcCPA security and related CCA-secure constructions**
  2025-11-03 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2036)
  Caroline Fontaine, Marc Renard, Renaud Sirdey, Oana Stan

  <details><summary>摘要 / Abstract</summary>

  FuncCPA is a recent security notion in which the CPA game is extended by a functional re-encryption oracle in order to model setups in which a server performing FHE computations is allowed to interactively delegate part of the computation back to the client. In this paper, we study funcCPA-style variants of several CCA security notions, including CCA1 and the more recent vCCA security. Contrary to the CPA case where a strict separation holds between CPA and funcCPA, we show that these new variants are equivalent to their respective originating CCA security notions. Interestingly, funcCPA-style security notions also model setups where, rather than delegating part of the encrypted domain computation all the way back to the client, the server has the ability to perform this delegation towards a honest or semi-honest client proxy it hosts, such as a secure enclave. We then provide a number of blueprints for achieving both FHE-like capabilities and advanced CCA security properties which may then meaningfully be implemented by leveraging on the combination of a partially homormophic scheme and a semi-honest non-colluding enclave hosted within the server performing the encrypted domain calculations itself.

  匹配依据：TEE: secure enclave

  </details>

- **MtDB: A Decentralized Multi-Tenant Database for Secure Data Sharing**
  2025-11-02 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2034)
  Showkot Hossain, Wenyi Tang, Changhao Chenli, Haijian Sun, WenZhan Song, Seokki Lee, Mic Bowman, Taeho Jung

  <details><summary>摘要 / Abstract</summary>

  Healthcare data sharing is fundamental for advancing medical research and enhancing patient care, yet it faces significant challenges in privacy, data ownership, and interoperability due to fragmented data silos across institutions and strict regulations (e.g., GDPR, HIPAA). To bridge these gaps, we propose MtDB, a novel decentralized database architecture addressing secure data sharing in multi-tenant database ecosystems. MtDB employs blockchain for metadata coordination and sharing, IPFS for distributed data addressing, a universal SQL query interface for data access, and Intel SGX for integrity-protected query execution with enforced access control. We provide an open-source implementation demonstrating MtDB’s capabilities for secure, patient-centric healthcare data sharing while preserving ownership and enforcing policies. Experimental results show MtDB achieves 35 milliseconds query latency for indexed queries over 400M multi-tenant medical records while maintaining cryptographic security guarantees, with only 1.2–1.3× performance overhead compared to non-secure baselines.

  匹配依据：TEE: intel sgx

  </details>

- **TEE-BFT: Pricing the Security of Data Center Execution Assurance**
  2025-10-30 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.26091)
  Alex Shamis, Matt Stephenson, Linfeng Zhou

  <details><summary>摘要 / Abstract</summary>

  Blockchains face inherent limitations when communicating outside their own ecosystem, largely due to the Byzantine Fault Tolerant (BFT) 3f+1 security model. Trusted Execution Environments (TEEs) are a promising mitigation because they allow a single trusted broker to interface securely with external systems. This paper develops a cost-of-collusion principal-agent model for compromising a TEE in a Data Center Execution Assurance design. The model isolates the main drivers of attack profitability: a K-of-n coordination threshold, independent detection risk q, heterogeneous per-member sanctions F_i, and a short-window flow prize (omega) proportional to the value secured (beta times V). We derive closed-form deterrence thresholds and a conservative design bound (V_safe) that make collusion unprofitable under transparent parameter choices. Calibrations based on time-advantaged arbitrage indicate that plausible TEE parameters can protect on the order of one trillion dollars in value.

  匹配依据：TEE: trusted execution environments

  </details>

- **Scalable GPU-Based Integrity Verification for Large Machine Learning Models**
  2025-10-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.23938)
  Marcin Spoczynski, Marcela S. Melara

  <details><summary>摘要 / Abstract</summary>

  We present a security framework that strengthens distributed machine learning by standardizing integrity protections across CPU and GPU platforms and significantly reducing verification overheads. Our approach co-locates integrity verification directly with large ML model execution on GPU accelerators, resolving the fundamental mismatch between how large ML workloads typically run (primarily on GPUs) and how security verifications traditionally operate (on separate CPU-based processes), delivering both immediate performance benefits and long-term architectural consistency. By performing cryptographic operations natively on GPUs using dedicated compute units (e.g., Intel Arc&#x27;s XMX units, NVIDIA&#x27;s Tensor Cores), our solution eliminates the potential architectural bottlenecks that could plague traditional CPU-based verification systems when dealing with large models. This approach leverages the same GPU-based high-memory bandwidth and parallel processing primitives that power ML workloads ensuring integrity checks keep pace with model execution even for massive models exceeding 100GB. This framework establishes a common integrity verification mechanism that works consistently across different GPU vendors and hardware configurations. By anticipating future capabilities for creating secure channels between trusted execution environments and GPU accelerators, we provide a hardware-agnostic foundation that enterprise teams can deploy regardless of their underlying CPU and GPU infrastructures.

  匹配依据：TEE: trusted execution environments

  </details>

- **FAARM: Firmware Attestation and Authentication Framework for Mali GPUs**
  2025-10-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.22566)
  Md. Mehedi Hasan

  <details><summary>摘要 / Abstract</summary>

  Recent work has revealed MOLE, the first practical attack to compromise GPU Trusted Execution Environments (TEEs), by injecting malicious firmware into the embedded Microcontroller Unit (MCU) of Arm Mali GPUs. By exploiting the absence of cryptographic verification during initialization, adversaries with kernel privileges can bypass memory protections, exfiltrate sensitive data at over 40 MB/s, and tamper with inference results, all with negligible runtime overhead. This attack surface affects commodity mobile SoCs and cloud accelerators, exposing a critical firmware-level trust gap in existing GPU TEE designs. To address this gap, this paper presents FAARM, a lightweight Firmware Attestation and Authentication framework that prevents MOLE-style firmware subversion. FAARM integrates digital signature verification at the EL3 secure monitor using vendor-signed firmware bundles and an on-device public key anchor. At boot, EL3 verifies firmware integrity and authenticity, enforces version checks, and locks the firmware region, eliminating both pre-verification and time-of-check-to-time-of-use (TOCTOU) attack vectors. We implement FAARM as a software-only prototype on a Mali GPU testbed, using a Google Colab-based emulation framework that models the firmware signing process, the EL1 to EL3 load path, and secure memory configuration. FAARM reliably detects and blocks malicious firmware injections, rejecting tampered images before use and denying overwrite attempts after attestation. Firmware verification incurs only 1.34 ms latency on average, demonstrating that strong security can be achieved with negligible overhead. FAARM thus closes a fundamental gap in shim-based GPU TEEs, providing a practical, deployable defense that raises the security baseline for both mobile and cloud GPU deployments.

  匹配依据：TEE: trusted execution environments

  </details>

- **Toward provably private analytics and insights into GenAI use**
  2025-10-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.21684)
  Albert Cheu, Artem Lagzdin, Brett McLarnon, Daniel Ramage, Katharine Daly, Marco Gruteser, Peter Kairouz, Rakshita Tandon, Stanislav Chiknavaryan, Timon Van Overveldt, Zoe Gong

  <details><summary>摘要 / Abstract</summary>

  Large-scale systems that compute analytics over a fleet of devices must achieve high privacy and security standards while also meeting data quality, usability, and resource efficiency expectations. We present a next-generation federated analytics system that uses Trusted Execution Environments (TEEs) based on technologies like AMD SEV-SNP and Intel TDX to provide verifiable privacy guarantees for all server-side processing. In our system, devices encrypt and upload data, tagging it with a limited set of allowable server-side processing steps. An open source, TEE-hosted key management service guarantees that the data is accessible only to those steps, which are themselves protected by TEE confidentiality and integrity assurance guarantees. The system is designed for flexible workloads, including processing unstructured data with LLMs (for structured summarization) before aggregation into differentially private insights (with automatic parameter tuning). The transparency properties of our system allow any external party to verify that all raw and derived data is processed in TEEs, protecting it from inspection by the system operator, and that differential privacy is applied to all released results. This system has been successfully deployed in production, providing helpful insights into real-world GenAI experiences.

  匹配依据：TEE: amd sev, intel tdx, trusted execution environments

  </details>

- **SecureInfer: Heterogeneous TEE-GPU Architecture for Privacy-Critical Tensors for Large Language Model Deployment**
  2025-10-22 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.19979)
  Tushar Nayan, Ziqi Zhang, Ruimin Sun

  <details><summary>摘要 / Abstract</summary>

  With the increasing deployment of Large Language Models (LLMs) on mobile and edge platforms, securing them against model extraction attacks has become a pressing concern. However, protecting model privacy without sacrificing the performance benefits of untrusted AI accelerators, such as GPUs, presents a challenging trade-off. In this paper, we initiate the study of high-performance execution on LLMs and present SecureInfer, a hybrid framework that leverages a heterogeneous Trusted Execution Environments (TEEs)-GPU architecture to isolate privacy-critical components while offloading compute-intensive operations to untrusted accelerators. Building upon an outsourcing scheme, SecureInfer adopts an information-theoretic and threat-informed partitioning strategy: security-sensitive components, including non-linear layers, projection of attention head, FNN transformations, and LoRA adapters, are executed inside an SGX enclave, while other linear operations (matrix multiplication) are performed on the GPU after encryption and are securely restored within the enclave. We implement a prototype of SecureInfer using the LLaMA-2 model and evaluate it across performance and security metrics. Our results show that SecureInfer offers strong security guarantees with reasonable performance, offering a practical solution for secure on-device model inference.

  匹配依据：TEE: sgx, sgx enclave, trusted execution environments

  </details>

- **Cross-Chain Sealed-Bid Auctions Using Confidential Compute Blockchains**
  2025-10-22 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.19491)
  Jonas Gebele, Timm Mutzel, Burak Oez, Florian Matthes

  <details><summary>摘要 / Abstract</summary>

  Sealed-bid auctions ensure fair competition and efficient allocation but are often deployed on centralized infrastructure, enabling opaque manipulation. Public blockchains eliminate central control, yet their inherent transparency conflicts with the confidentiality required for sealed bidding. Prior attempts struggle to reconcile privacy, verifiability, and scalability without relying on trusted intermediaries, multi-round protocols, or expensive cryptography. We present a sealed-bid auction protocol that executes sensitive bidding logic on a Trusted Execution Environment (TEE)-backed confidential compute blockchain while retaining settlement and enforcement on a public chain. Bidders commit funds to enclave-generated escrow addresses, ensuring confidentiality and binding commitments. After the deadline, any party can trigger resolution: the confidential blockchain determines the winner through verifiable off-chain computation and issues signed settlement transactions for execution on the public chain. Our design provides security, privacy, and scalability without trusted third parties or protocol modifications. We implement it on SUAVE with Ethereum settlement, evaluate its scalability and trust assumptions, and demonstrate deployment with minimal integration on existing infrastructure

  匹配依据：TEE: trusted execution environment

  </details>

- **Hazel: Secure and Efficient Disaggregated Storage**
  2025-10-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.18756)
  Marcin Chrapek, Meni Orenbach, Ahmad Atamli, Marcin Copik, Mikhail Khalilov, Fritz Alder, Torsten Hoefler

  <details><summary>摘要 / Abstract</summary>

  Disaggregated storage with NVMe-over-Fabrics (NVMe-oF) has emerged as the standard solution in modern supercomputers and data center clusters, achieving superior performance, resource utilization, and power efficiency. Simultaneously, confidential computing (CC) is becoming the de facto security paradigm, enforcing stronger isolation and protection for sensitive workloads. However, securing state-of-the-art storage with traditional CC methods struggles to scale and compromises performance or security. To address these issues, we introduce Hazel, a storage management system that extends the NVMe-oF protocol capabilities and adheres to the CC threat model, providing confidentiality, integrity, and freshness guarantees. Hazel offers an appropriate control path with novel concepts such as counter-leasing. Hazel also optimizes data path performance by leveraging NVMe metadata and introducing a new disaggregated Hazel Merkle Tree (HMT), all while remaining compatible with NVMe-oF. For additional efficiency, Hazel also supports offloading to CC-capable smart NIC accelerators. We prototype Hazel on an NVIDIA BlueField-3 and demonstrate that it can achieve as little as 1-2% performance degradation for synthetic patterns, AI training, IO500, and YCSB.

  匹配依据：TEE: confidential computing

  </details>

- **Auntie: Unobservable Contracts from Zerocash and Trusted Execution Environments**
  2025-10-20 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1965)
  Adrian Cinal

  <details><summary>摘要 / Abstract</summary>

  Privacy-oriented cryptocurrencies like Zerocash only support direct payments and not the execution of more complex contracts. Bitcoin and Ethereum, on the other hand, cannot guarantee privacy, and using them for contract execution leaves open questions about the fungibility of proceeds and requires contract designers to take frontrunning countermeasures. This work reconciles the two worlds and develops a lightweight protocol for decentralized execution of complex contracts that (1) is undetectable to the network at large, (2) maintains anonymity of the potentially mutually distrustful counterparties and unlinkability of their repeated interactions, (3) guarantees fair termination, and (4) is immediately resistant to frontrunning and miner bribery attacks. This is achieved by leveraging the confidentiality and anonymity guarantees of Zerocash and the verifiability and flexibility of trusted execution environments.

  匹配依据：TEE: trusted execution environments

  </details>

- **DistilLock: Safeguarding LLMs from Unauthorized Knowledge Distillation on the Edge**
  2025-10-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.16716)
  Asmita Mohanty, Gezheng Kang, Lei Gao, Murali Annavaram

  <details><summary>摘要 / Abstract</summary>

  Large Language Models (LLMs) have demonstrated strong performance across diverse tasks, but fine-tuning them typically relies on cloud-based, centralized infrastructures. This requires data owners to upload potentially sensitive data to external servers, raising serious privacy concerns. An alternative approach is to fine-tune LLMs directly on edge devices using local data; however, this introduces a new challenge: the model owner must transfer proprietary models to the edge, which risks intellectual property (IP) leakage. To address this dilemma, we propose DistilLock, a TEE-assisted fine-tuning framework that enables privacy-preserving knowledge distillation on the edge. In DistilLock, a proprietary foundation model is executed within a trusted execution environment (TEE) enclave on the data owner&#x27;s device, acting as a secure black-box teacher. This setup preserves both data privacy and model IP by preventing direct access to model internals. Furthermore, DistilLock employs a model obfuscation mechanism to offload obfuscated weights to untrusted accelerators for efficient knowledge distillation without compromising security. We demonstrate that DistilLock prevents unauthorized knowledge distillation processes and model-stealing attacks while maintaining high computational efficiency, but offering a secure and practical solution for edge-based LLM personalization.

  匹配依据：TEE: trusted execution environment

  </details>

- **FHE-SQL: Fully Homomorphic Encrypted SQL Database**
  2025-10-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.15413)
  Po-Yu Tseng, Po-Chu Hsu, Shih-Wei Liao

  <details><summary>摘要 / Abstract</summary>

  FHE-SQL is a privacy-preserving database system that enables secure query processing on encrypted data using Fully Homomorphic Encryption (FHE), providing privacy guaranties where an untrusted server can execute encrypted queries without learning either the query contents or the underlying data. Unlike property-preserving encryption-based systems such as CryptDB, which rely on deterministic or order-preserving encryption and are vulnerable to frequency, order, and equality-pattern inference attacks, FHE-SQL performs computations entirely under encryption, eliminating these leakage channels. Compared to trusted-hardware approaches such as TrustedDB, which depend on a hardware security module and thus inherit its trust and side-channel limitations, our design achieves end-to-end cryptographic protection without requiring trusted execution environments. In contrast to high-performance FHE-based engines-Hermes, which target specialized workloads such as vector search, FHE-SQL supports general SQL query semantics with schema-aware, type-safe definitions suitable for relational data management. FHE-SQL mitigates the high cost of ciphertext space by using an indirection architecture that separates metadata in RocksDB from large ciphertexts in blob storage. It supports oblivious selection via homomorphic boolean masks, multi-tier caching, and garbage collection, with security proven under the Universal Composability framework.

  匹配依据：TEE: trusted execution environments

  </details>

- **Towards Trusted Service Monitoring: Verifiable Service Level Agreements**
  2025-10-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.13370)
  Fernando Castillo, Eduardo Brito, Sebastian Werner, Pille Pullonen-Raudvere, Jonathan Heiss

  <details><summary>摘要 / Abstract</summary>

  Service Level Agreement (SLA) monitoring in service-oriented environments suffers from inherent trust conflicts when providers self-report metrics, creating incentives to underreport violations. We introduce a framework for generating verifiable SLA violation claims through trusted hardware monitors and zero-knowledge proofs, establishing cryptographic foundations for genuine trustworthiness in service ecosystems. Our approach starts with machine-readable SLA clauses converted into verifiable predicates and monitored within Trusted Execution Environments. These monitors collect timestamped telemetry, organize measurements into Merkle trees, and produce signed attestations. Zero-knowledge proofs aggregate Service-Level Indicators to evaluate compliance, generating cryptographic proofs verifiable by stakeholders, arbitrators, or insurers in disputes, without accessing underlying data. This ensures three security properties: integrity, authenticity, and validity. Our prototype demonstrates linear scaling up to over 1 million events per hour for measurements with near constant-time proof generation and verification for single violation claims, enabling trustless SLA enforcement through cryptographic guarantees for automated compliance verification in service monitoring.

  匹配依据：TEE: trusted execution environments

  </details>

- **Proof of Cloud: Data Center Execution Assurance for Confidential VMs**
  2025-10-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.12469)
  Filip Rezabek, Moe Mahhouk, Andrew Miller, Quintus Kilbourn, Georg Carle, Jonathan Passerat-Palmbach

  <details><summary>摘要 / Abstract</summary>

  Confidential Virtual Machines (CVMs) protect data in use by running workloads within hardware-enforced Trusted Execution Environments (TEEs). However, existing CVM attestation mechanisms only certify what code is running, not where it is running. Commercial TEEs mitigate passive physical attacks through memory encryption but explicitly exclude active hardware tampering (memory interposers, physical side channels, ...). Yet current attestations provide no cryptographic evidence that a CVM executes on hardware residing within a trusted data center where such attacks would not take place. This gap enables proxy attacks in which valid attestations are combined across machines to falsely attest trusted execution. To bridge this gap, we introduce Data Center Execution Assurance (DCEA), a design that generates a cryptographic Proof of Cloud by binding CVM attestation to platform-level Trusted Platform Module (TPM) evidence. DCEA combines two independent roots of trust. First, the TEE manufacturer, and second, the infrastructure provider, by cross-linking runtime TEE measurements with the vTPM-measured boot CVM state. This binding ensures that CVM execution, vTPM quotes, and platform provenance all originate from the same physical chassis. We formalize the environment&#x27;s provenance and show that DCEA prevents advanced relay attacks, including a novel mix-and-match proxy attack. Using the AGATE framework in the Universal Composability model, we prove that DCEA emulates an ideal location-aware TEE even under a malicious host software stack. We implement DCEA on Google Cloud bare-metal Intel TDX instances using Intel TXT and evaluate its performance, demonstrating practical overheads and deployability. DCEA refines the CVM threat model and enables verifiable execution-location guarantees for privacy-sensitive workloads.

  匹配依据：TEE: intel tdx, trusted execution environments

  </details>

- **Leaking Queries On Secure Stream Processing Systems**
  2025-10-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.12172)
  Hung Pham, Viet Vo, Tien Tuan Anh Dinh, Duc Tran, Shuhao Zhang

  <details><summary>摘要 / Abstract</summary>

  Stream processing systems are important in modern applications in which data arrive continuously and need to be processed in real time. Because of their resource and scalability requirements, many of these systems run on the cloud, which is considered untrusted. Existing works on securing databases on the cloud focus on protecting the data, and most systems leverage trusted hardware for high performance. However, in stream processing systems, queries are as sensitive as the data because they contain the application logics. We demonstrate that it is practical to extract the queries from stream processing systems that use Intel SGX for securing the execution engine. The attack performed by a malicious cloud provider is based on timing side channels, and it works in two phases. In the offline phase, the attacker profiles the execution time of individual stream operators, based on synthetic data. This phase outputs a model that identifies individual stream operators. In the online phase, the attacker isolates the operators that make up the query, monitors its execution, and recovers the operators using the model in the previous phase. We implement the attack based on popular data stream benchmarks using SecureStream and NEXMark, and demonstrate attack success rates of up to 92%. We further discuss approaches that can harden streaming processing systems against our attacks without incurring high overhead.

  匹配依据：TEE: intel sgx

  </details>

- **Adding All Flavors: A Hybrid Random Number Generator for dApps and Web3**
  2025-10-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.12062)
  Ranjith Chodavarapu, Rabimba Karanjai, Xinxin Fan, Weidong Shi, Lei Xu

  <details><summary>摘要 / Abstract</summary>

  Random numbers play a vital role in many decentralized applications (dApps), such as gaming and decentralized finance (DeFi) applications. Existing random number provision mechanisms can be roughly divided into two categories, on-chain, and off-chain. On-chain approaches usually rely on the blockchain as the major input and all computations are done by blockchain nodes. The major risk for this type of method is that the input itself is susceptible to the adversary&#x27;s influence. Off-chain approaches, as the name suggested, complete the generation without the involvement of blockchain nodes and share the result directly with a dApp. These mechanisms usually have a strong security assumption and high complexity. To mitigate these limitations and provide a framework that allows a dApp to balance different factors involved in random number generation, we propose a hybrid random number generation solution that leverages IoT devices equipped with trusted execution environment (TEE) as the randomness sources, and then utilizes a set of cryptographic tools to aggregate the multiple sources and obtain the final random number that can be consumed by the dApp. The new approach only needs one honest random source to guarantee the unbiasedness of the final random number and a user can configure the system to tolerate malicious participants who can refuse to respond to avoid unfavored results. We also provide a concrete construction that can further reduce the on-chain computation complexity to lower the cost of the solution in practice. We evaluate the computation and gas costs to demonstrate the effectiveness of the improvement.

  匹配依据：TEE: trusted execution environment

  </details>

- **TBRD: TESLA Authenticated UAS Broadcast Remote ID**
  2025-10-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.11343)
  Jason Veara, Manav Jain, Kyle Moy, Aanjhan Ranganathan

  <details><summary>摘要 / Abstract</summary>

  Mysterious sightings of Unmanned Aircraft Systems (UAS) over U.S. military facilities, suburban neighborhoods, and commercial airports have intensified scrutiny of drone activity. To increase accountability, the Federal Aviation Administration (FAA) introduced a Remote ID mandate, requiring unmanned aircraft to broadcast their location, operator&#x27;s location, and identity in real-time. However, current standards leave authentication mechanisms underspecified, enabling spoofing, relay, and replay attacks that can undermine surveillance efforts and potentially disrupt UAS-to-UAS coordination in future deployments. In this paper, we propose TBRD, a practical system for authenticating Remote ID messages in a manner that aligns with existing standards and UAS capabilities. TBRD leverages the TESLA protocol and mobile device TEEs, and introduces a verification mechanism to build a lightweight, mission-scoped authentication system that is both computationally efficient and requires a low communication footprint. We evaluate the performance of TBRD using both an FAA-requirements compatible proof-of-concept implementation for performance metrics and a simulated 4-drone swarm mission scenario to demonstrate its security guarantees under adversarial conditions. Our system provides a 50\% reduction in authentication overhead compared to digital signatures and a 100x reduction in computation time. Our results demonstrate that TBRD can be integrated into current Remote ID infrastructures to provide a scalable, standards-compliant message authentication for both regulatory and operational use cases.

  匹配依据：TEE: tees (context)

  </details>

- **The Data Enclave Advantage: A New Paradigm for Least-Privileged Data Access in a Zero-Trust World**
  2025-10-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.09494)
  Nico Bistolfi, Andreea Georgescu, Dave Hodson

  <details><summary>摘要 / Abstract</summary>

  As cloud infrastructure evolves to support dynamic and distributed workflows, accelerated now by AI-driven processes, the outdated model of standing permissions has become a critical vulnerability. Based on the Cloud Security Alliance (CSA) Top Threats to Cloud Computing Deep Dive 2025 Report, our analysis details how standing permissions cause catastrophic cloud breaches. While current security tools are addressing network and API security, the challenge of securing granular data access remains. Removing standing permissions at the data level is as critical as it is at the network level, especially for companies handling valuable data at scale. In this white paper, we introduce an innovative architecture based on on-demand data enclaves to address this gap directly. Our approach enables Zero Standing Privilege (ZSP) and Just-in-Time (JIT) principles at the data level. We replace static permissions with temporary data contracts that enforce proactive protection. This means separation is built around the data requested on-demand, providing precise access and real time monitoring for individual records instead of datasets. This solution drastically reduces the attack surface, prevents privilege creep, and simplifies auditing, offering a vital path for enterprises to transition to a more secure and resilient data environment.

  匹配依据：TEE: enclave (context)

  </details>

- **Signing Right Away**
  2025-10-07 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.09656)
  Yejun Jang

  <details><summary>摘要 / Abstract</summary>

  The proliferation of high-fidelity synthetic media, coupled with exploitable hardware vulnerabilities in conventional imaging pipelines, has precipitated a crisis of trust in digital content. Existing countermeasures, from post-hoc classifiers to software-based signing, fail to address the fundamental challenge of establishing an unbreakable link to reality at the moment of capture. This whitepaper introduces Signing Right Away (SRA), a comprehensive security architecture that guarantees the provenance of digital media from &quot;silicon to silicon to signed file.&quot; SRA leverages a four-pillar security model-Confidentiality, Integrity, Authentication, and Replay Protection, akin to the MIPI Camera Security Framework (CSF), but also extends its scope beyond the internal data bus to the creation of a cryptographically sealed, C2PA-compliant final asset. By securing the entire imaging pipeline within a Trusted Execution Environment (TEE), SRA ensures that every captured image and video carries an immutable, verifiable proof of origin. This provides a foundational solution for industries reliant on trustworthy visual information, including journalism, legal evidence, and insurance. We present the SRA architecture, a detailed implementation roadmap informed by empirical prototyping, and a comparative analysis that positions SRA as the essential &quot;last mile&quot; in the chain of content trust.

  匹配依据：TEE: trusted execution environment

  </details>

- **Deep Learning-Based Multi-Factor Authentication: A Survey of Biometric and Smart Card Integration Approaches**
  2025-10-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.05163)
  Abdelilah Ganmati, Karim Afdel, Lahcen Koutti

  <details><summary>摘要 / Abstract</summary>

  In the era of pervasive cyber threats and exponential growth in digital services, the inadequacy of single-factor authentication has become increasingly evident. Multi-Factor Authentication (MFA), which combines knowledge-based factors (passwords, PINs), possession-based factors (smart cards, tokens), and inherence-based factors (biometric traits), has emerged as a robust defense mechanism. Recent breakthroughs in deep learning have transformed the capabilities of biometric systems, enabling higher accuracy, resilience to spoofing, and seamless integration with hardware-based solutions. At the same time, smart card technologies have evolved to include on-chip biometric verification, cryptographic processing, and secure storage, thereby enabling compact and secure multi-factor devices. This survey presents a comprehensive synthesis of recent work (2019-2025) at the intersection of deep learning, biometrics, and smart card technologies for MFA. We analyze biometric modalities (face, fingerprint, iris, voice), review hardware-based approaches (smart cards, NFC, TPMs, secure enclaves), and highlight integration strategies for real-world applications such as digital banking, healthcare IoT, and critical infrastructure. Furthermore, we discuss the major challenges that remain open, including usability-security tradeoffs, adversarial attacks on deep learning models, privacy concerns surrounding biometric data, and the need for standardization in MFA deployment. By consolidating current advancements, limitations, and research opportunities, this survey provides a roadmap for designing secure, scalable, and user-friendly authentication frameworks.

  匹配依据：TEE: secure enclaves

  </details>

- **Obelix: Mitigating Side-Channels Through Dynamic Obfuscation**
  2025-09-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.18909)
  Jan Wichelmann, Anja Rabich, Anna P"atschke, Thomas Eisenbarth

  <details><summary>摘要 / Abstract</summary>

  Trusted execution environments (TEEs) offer hardware-assisted means to protect code and data. However, as shown in numerous results over the years, attackers can use side-channels to leak data access patterns and even single-step the code. While the vendors are slowly introducing hardware-based countermeasures for some attacks, others will stay unaddressed. This makes a software-level countermeasure desirable, but current available solutions only address very specific attack vectors or have a narrow leakage model. In this work, we take a holistic view at the vulnerabilities of TEEs and design a tool named Obelix, which is the first to protect both code and data against a wide range of TEE attacks, from cache attacks over single-stepping to ciphertext side-channels. We analyze the practically achievable precision of state-of-the-art single-stepping tools, and present an algorithm which uses that knowledge to divide a program into uniform code blocks, that are indistinguishable for a strong attacker. By storing these blocks and the program data in oblivious RAM, the attacker cannot follow execution, effectively protecting both secret code and data. We describe how we automate our approach to make it available for developers who are unfamiliar with side-channels. As an obfuscation tool, Obelix comes with a considerable performance overhead, but compensates this with strong security guarantees and easy applicability without requiring any expert knowledge.

  匹配依据：TEE: trusted execution environments

  </details>

- **Edge Encryption using Iterative Management Framework**
  2025-09-23 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1735)
  Manoja Shridhar, Bala Puruvana, Alex Cravill, Joey Wolff

  <details><summary>摘要 / Abstract</summary>

  Securing data in heterogeneous, latency-sensitive edge environments demands encryption that adapts to device churn, intermittent connectivity, and evolving threat models without sacrificing real-time performance. We present an Iterative Management Framework (IMF) for edge encryption that closes the loop between policy intent, cryptographic configuration, runtime telemetry, and automated remediation. IMF organizes encryption management as a continuous control cycle—model, deploy, observe, and refine—spanning device, edge-cluster, and cloud control planes. Concretely, IMF (i) encodes encryption policies as declarative, verifiable profiles; (ii) performs constraint-aware rollout and staged key rotation using topology- and load-aware schedulers; (iii) leverages streaming telemetry (cryptographic error rates, handshake retries, path RTT, and drift in device trust scores) to trigger bounded updates; and (iv) resolves conflicts via policy iteration with formal safety checks to prevent downgrade, orphaned keys, or split-brain trust roots. The framework supports heterogeneous primitives—including AEAD ciphers, forward-secure rekeying, TEE/HSM-anchored key custody, and post-quantum negotiation—while tolerating partial connectivity through opportunistic convergence and cryptographic state caching at the edge. In a prototype across 1,200 edge nodes, IMF sustained line-rate encryption with ≤1.8% median throughput overhead and &lt;35 ms p95 added latency during rolling rekeys, reduced key-exposure windows by 57% via adaptive rotation, and cut control traffic by 41% using differential rollout plans. These results indicate that iterative, telemetry-driven management can deliver robust encryption at the edge while preserving tight performance envelopes.

  匹配依据：TEE: tee (context)

  </details>

- **Confidential LLM Inference: Performance and Cost Across CPU and GPU TEEs**
  2025-09-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.18886)
  Marcin Chrapek, Marcin Copik, Etienne Mettaz, Torsten Hoefler

  <details><summary>摘要 / Abstract</summary>

  Large Language Models (LLMs) are increasingly deployed on converged Cloud and High-Performance Computing (HPC) infrastructure. However, as LLMs handle confidential inputs and are fine-tuned on costly, proprietary datasets, their heightened security requirements slow adoption in privacy-sensitive sectors such as healthcare and finance. We investigate methods to address this gap and propose Trusted Execution Environments (TEEs) as a solution for securing end-to-end LLM inference. We validate their practicality by evaluating these compute-intensive workloads entirely within CPU and GPU TEEs. On the CPU side, we conduct an in-depth study running full Llama2 inference pipelines (7B, 13B, 70B) inside Intel&#x27;s TDX and SGX, accelerated by Advanced Matrix Extensions (AMX). We derive 12 insights, including that across various data types, batch sizes, and input lengths, CPU TEEs impose under 10% throughput and 20% latency overheads, further reduced by AMX. We run LLM inference on NVIDIA H100 Confidential Compute GPUs, contextualizing our CPU findings and observing throughput penalties of 4-8% that diminish as batch and input sizes grow. By comparing performance, cost, and security trade-offs, we show how CPU TEEs can be more cost-effective or secure than their GPU counterparts. To our knowledge, our work is the first to comprehensively demonstrate the performance and practicality of modern TEEs across both CPUs and GPUs for enabling confidential LLMs (cLLMs).

  匹配依据：TEE: sgx, trusted execution environments

  </details>

- **Dstack: A Zero Trust Framework for Confidential Containers**
  2025-09-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.11555)
  Shunfan Zhou, Kevin Wang, Hang Yin

  <details><summary>摘要 / Abstract</summary>

  Web3 applications require execution platforms that maintain confidentiality and integrity without relying on centralized trust authorities. While Trusted Execution Environments (TEEs) offer promising capabilities for confidential computing, current implementations face significant limitations when applied to Web3 contexts, particularly in security reliability, censorship resistance, and vendor independence. This paper presents dstack, a comprehensive framework that transforms raw TEE technology into a true Zero Trust platform. We introduce three key innovations: (1) Portable Confidential Containers that enable seamless workload migration across heterogeneous TEE environments while maintaining security guarantees, (2) Decentralized Code Management that leverages smart contracts for transparent governance of TEE applications, and (3) Verifiable Domain Management that ensures secure and verifiable application identity without centralized authorities. These innovations are implemented through three core components: dstack-OS, dstack-KMS, and dstack-Gateway. Together, they demonstrate how to achieve both the performance advantages of VM-level TEE solutions and the trustless guarantees required by Web3 applications. Our evaluation shows that dstack provides comprehensive security guarantees while maintaining practical usability for real-world applications.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **Towards Confidential and Efficient LLM Inference with Dual Privacy Protection**
  2025-09-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.09091)
  Honglan Yu, Yibin Wang, Feifei Dai, Dong Liu, Haihui Fan, Xiaoyan Gu

  <details><summary>摘要 / Abstract</summary>

  CPU-based trusted execution environments (TEEs) and differential privacy (DP) have gained wide applications for private inference. Due to high inference latency in TEEs, researchers use partition-based approaches that offload linear model components to GPUs. However, dense nonlinear layers of large language models (LLMs) result in significant communication overhead between TEEs and GPUs. DP-based approaches apply random noise to protect data privacy, but this compromises LLM performance and semantic understanding. To overcome the above drawbacks, this paper proposes CMIF, a Confidential and efficient Model Inference Framework. CMIF confidentially deploys the embedding layer in the client-side TEE and subsequent layers on GPU servers. Meanwhile, it optimizes the Report-Noisy-Max mechanism to protect sensitive inputs with a slight decrease in model performance. Extensive experiments on Llama-series models demonstrate that CMIF reduces additional inference overhead in TEEs while preserving user data privacy.

  匹配依据：TEE: trusted execution environments

  </details>

- **Securing Private Federated Learning in a Malicious Setting: A Scalable TEE-Based Approach with Client Auditing**
  2025-09-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.08709)
  Shun Takagi, Satoshi Hasegawa

  <details><summary>摘要 / Abstract</summary>

  In cross-device private federated learning, differentially private follow-the-regularized-leader (DP-FTRL) has emerged as a promising privacy-preserving method. However, existing approaches assume a semi-honest server and have not addressed the challenge of securely removing this assumption. This is due to its statefulness, which becomes particularly problematic in practical settings where clients can drop out or be corrupted. While trusted execution environments (TEEs) might seem like an obvious solution, a straightforward implementation can introduce forking attacks or availability issues due to state management. To address this problem, our paper introduces a novel server extension that acts as a trusted computing base (TCB) to realize maliciously secure DP-FTRL. The TCB is implemented with an ephemeral TEE module on the server side to produce verifiable proofs of server actions. Some clients, upon being selected, participate in auditing these proofs with small additional communication and computational demands. This extension solution reduces the size of the TCB while maintaining the system&#x27;s scalability and liveness. We provide formal proofs based on interactive differential privacy, demonstrating privacy guarantee in malicious settings. Finally, we experimentally show that our framework adds small constant overhead to clients in several realistic settings.

  匹配依据：TEE: trusted execution environments

  </details>

- **AttestLLM: Efficient Attestation Framework for Billion-scale On-device LLMs**
  2025-09-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.06326)
  Ruisi Zhang, Yifei Zhao, Neusha Javidnia, Mengxin Zheng, Farinaz Koushanfar

  <details><summary>摘要 / Abstract</summary>

  As on-device LLMs(e.g., Apple on-device Intelligence) are widely adopted to reduce network dependency, improve privacy, and enhance responsiveness, verifying the legitimacy of models running on local devices becomes critical. Existing attestation techniques are not suitable for billion-parameter Large Language Models (LLMs), struggling to remain both time- and memory-efficient while addressing emerging threats in the LLM era. In this paper, we present AttestLLM, the first-of-its-kind attestation framework to protect the hardware-level intellectual property (IP) of device vendors by ensuring that only authorized LLMs can execute on target platforms. AttestLLM leverages an algorithm/software/hardware co-design approach to embed robust watermarking signatures onto the activation distributions of LLM building blocks. It also optimizes the attestation protocol within the Trusted Execution Environment (TEE), providing efficient verification without compromising inference throughput. Extensive proof-of-concept evaluations on LLMs from Llama, Qwen, and Phi families for on-device use cases demonstrate AttestLLM&#x27;s attestation reliability, fidelity, and efficiency. Furthermore, AttestLLM enforces model legitimacy and exhibits resilience against model replacement and forgery attacks.

  匹配依据：TEE: trusted execution environment

  </details>

- **Reinforcing Secure Live Migration through Verifiable State Management**
  2025-09-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.05150)
  Stefanos Vasileaidis, Thanassis Giannetsos, Matthias Schunter, Bruno Crispo

  <details><summary>摘要 / Abstract</summary>

  Live migration of applications is a fundamental capability for enabling resilient computing in modern distributed systems. However, extending this functionality to trusted applications (TA) -- executing within Trusted Execution Environments (TEEs) -- introduces unique challenges such as secure state preservation, integrity verification, replay and rollback prevention, and mitigation of unauthorized cloning of TAs. We present TALOS, a lightweight framework for verifiable state management and trustworthy application migration. While our implementation is prototyped and evaluated using Intel SGX with the Gramine LibOS and RISC-V Keystone (evidencing the framework&#x27;s portability across diverse TEEs), its design is agnostic to the underlying TEE architecture. Such agility is a necessity in today&#x27;s network service mesh (collaborative computing across the continuum) where application workloads must be managed across domain boundaries in a harmonized fashion. TALOS is built around the principle of minimizing trust assumptions: TAs are treated as untrusted until explicitly verified, and the migration process does not rely on a trusted third party. To ensure both the integrity and secure launch of the migrated application, TALOS integrates memory introspection and control-flow graph extraction, enabling robust verification of state continuity and execution flow. Thereby achieving strong security guarantees while maintaining efficiency, making it suitable for decentralized settings.

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **ShieldMMU: Detecting and Defending against Controlled-Channel Attacks in Shielding Memory System**
  2025-09-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.03879)
  Gang Liu, Ningjie Li, Cen Chen

  <details><summary>摘要 / Abstract</summary>

  Intel SGX and hypervisors isolate non-privileged programs from other software, ensuring confidentiality and integrity. However, side-channel attacks continue to threaten Intel SGX&#x27;s security, enabling malicious OS to manipulate PTE present bits, induce page faults, and steal memory access traces. Despite extensive research, existing defenses focus on detection or rely on impractical solutions. This paper presents ShieldMMU, a comprehensive solution for mitigating controlled channel attacks, balancing compatibility, performance, and usability. Leveraging a Merkle Tree-inspired Defense Tree (DD-Tree), ShieldMMU protects PTE integrity by detecting, locating, and restoring attacked PTEs. It identifies MMU page table lookup events and side-channel attacks, promptly restoring PTE parameters to prevent page fault traps and ensure secure non-privileged application operation within SGX. Our experiments confirm ShieldMMU&#x27;s enhanced security and acceptable latency performance.

  匹配依据：TEE: intel sgx, sgx

  </details>

- **A Secure, Confidential, and Verifiable Decision Support System**
  2025-09-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.02413)
  Edoardo Marangone, Eugenio Nerio Nemmi, Daniele Friolo, Giuseppe Ateniese, Ingo Weber, Claudio Di Ciccio

  <details><summary>摘要 / Abstract</summary>

  Decision support systems are increasingly adopted to automate decision-making processes across industries, organizations, and governments. Decision support demands data privacy, integrity, and availability while ensuring customization, security, and verifiability of the decision process. Existing solutions fail to guarantee those properties altogether. To overcome this limitation, we propose SPARTA, an approach based on Trusted Execution Environments (TEEs) that automates decision processes. To guarantee privacy, integrity, and availability, SPARTA employs efficient cryptographic techniques on notarized data with access mediated through user-defined access policies. Our solution allows users to define decision rules, which are translated to certified software objects deployed within TEEs, thereby guaranteeing customization, verifiability, and security of the process. With experiments run on public benchmarks and synthetic data, we show our approach is scalable and adds limited overhead compared to non-cryptographically secured solutions.

  匹配依据：TEE: trusted execution environments

  </details>

- **BOLT: Bandwidth-Optimized Lightning-Fast Oblivious Map powered by Secure HBM Accelerators**
  2025-09-01 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.01742)
  Yitong Guo, Hongbo Chen, Haobin Hiroki Chen, Yukui Luo, XiaoFeng Wang, Chenghong Wang

  <details><summary>摘要 / Abstract</summary>

  While Trusted Execution Environments provide a strong foundation for secure cloud computing, they remain vulnerable to access pattern leakages. Oblivious Maps (OMAPs) mitigate this by fully hiding access patterns but suffer from high overhead due to randomized remapping and worst-case padding. We argue these costs are not fundamental. Modern accelerators featuring High-Bandwidth Memory (HBM) offer a new opportunity: Vaswani et al. [OSDI&#x27;18] point out that eavesdropping on HBM is difficult -- even for physical attackers -- as its memory channels are sealed together with processor cores inside the same physical package. Later, Hunt et al. [NSDI&#x27;20] show that, with proper isolation, HBM can be turned into an unobservable region where both data and memory traces are hidden. This motivates a rethink of OMAP design with HBM-backed solutions to finally overcome their traditional performance limits. Building on these insights, we present BOLT, a Bandwidth Optimized, Lightning-fast OMAP accelerator that, for the first time, achieves O(1) + O(log_2(log_2 (N))) bandwidth overhead. BOLT introduces three key innovations: (i) a new OMAP algorithm that leverages isolated HBM as an unobservable cache to accelerate oblivious access to large host memory; (ii) a self-hosted architecture that offloads execution and memory control from the host to mitigate CPU-side leakage; and (iii) tailored algorithm-architecture co-designs that maximize resource efficiency. We implement a prototype BOLT on a Xilinx U55C FPGA. Evaluations show that BOLT achieves up to 279x and 480x speedups in initialization and query time, respectively, over state-of-the-art OMAPs, including an industry implementation from Facebook.

  匹配依据：TEE: trusted execution environments

  </details>

- **Enabling Trustworthy Federated Learning via Remote Attestation for Mitigating Byzantine Threats**
  2025-08-30 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.00634)
  Chaoyu Zhang, Heng Jin, Shanghao Shi, Hexuan Yu, Sydney Johns, Y. Thomas Hou, Wenjing Lou

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) has gained significant attention for its privacy-preserving capabilities, enabling distributed devices to collaboratively train a global model without sharing raw data. However, its distributed nature forces the central server to blindly trust the local training process and aggregate uncertain model updates, making it susceptible to Byzantine attacks from malicious participants, especially in mission-critical scenarios. Detecting such attacks is challenging due to the diverse knowledge across clients, where variations in model updates may stem from benign factors, such as non-IID data, rather than adversarial behavior. Existing data-driven defenses struggle to distinguish malicious updates from natural variations, leading to high false positive rates and poor filtering performance. To address this challenge, we propose Sentinel, a remote attestation (RA)-based scheme for FL systems that regains client-side transparency and mitigates Byzantine attacks from a system security perspective. Our system employs code instrumentation to track control-flow and monitor critical variables in the local training process. Additionally, we utilize a trusted training recorder within a Trusted Execution Environment (TEE) to generate an attestation report, which is cryptographically signed and securely transmitted to the server. Upon verification, the server ensures that legitimate client training processes remain free from program behavior violation or data manipulation, allowing only trusted model updates to be aggregated into the global model. Experimental results on IoT devices demonstrate that Sentinel ensures the trustworthiness of the local training integrity with low runtime and memory overhead.

  匹配依据：TEE: trusted execution environment

  </details>

- **Characterizing Trust Boundary Vulnerabilities in TEE Containers: An Empirical Study**
  2025-08-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.20962)
  Weijie Liu, Hongbo Chen, Shuo Huai, Zhen Xu, Wenhao Wang, XiaoFeng Wang, Danfeng Zhang, Zhi Li, Haixu Tang, Zheli Liu

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) have become a cornerstone of confidential computing, attracting significant attention from academia and industry. To support secure and scalable application deployment on confidential clouds, TEE containers (Tcons) have been introduced as middleware to shield applications from malicious operating systems and orchestration layers while preserving usability. In this paper, we present the first comprehensive analysis of Tcons, focusing on three critical layers: OS interfaces, encrypted I/O, and orchestration mechanisms. To enable systematic evaluation, we design TBouncer, an automated analyzer that precisely exercises and benchmarks Tcon isolation boundaries. Our study uncovers fundamental flaws in existing Tcons, leading to exploitable vulnerabilities such as code execution, denial-of-service, and information leakage. In total, we identify six attack vectors, twelve new bugs, and three CVEs. These findings provide new insights into the underestimated attack surface of Tcons and highlight key directions for building more secure and trustworthy container solutions.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **Flexible In-NAND Cryptographic Processing for Secure Flash Storage**
  2025-08-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.03866)
  Seock-Hwan Noh, Hoyeon Lee, Junkyum Kim, Junsu Im, Jay H. Park, Sungjin Lee, Sam H. Noh, Yeseong Kim, Jaeha Kung

  <details><summary>摘要 / Abstract</summary>

  We present FlashVault, an in-NAND self-encryption architecture that embeds a reconfigurable cryptographic engine into the unused silicon area of a state-of-the-art 4D V-NAND structure. FlashVault supports not only block ciphers for data encryption but also public-key and post-quantum algorithms for digital signatures, all within the NAND flash chip. This design enables each NAND chip to operate as a self-contained enclave without incurring area overhead, while eliminating the need for off-chip encryption. We implement FlashVault at the register-transfer level (RTL) and perform place-and-route (P&amp;R) for accurate power/area evaluation. Our analysis shows that the power budget determines the number of cryptographic engines per NAND chip. We integrate this architectural choice into a full-system simulation and evaluate its performance on a wide range of cryptographic algorithms. Our results show that FlashVault consistently outperforms both CPU-based encryption (1.46~3.45x) and near-core processing architecture (1.02~2.01x), demonstrating its effectiveness as a secure SSD architecture that meets diverse cryptographic requirements imposed by regulatory standards and enterprise policies.

  匹配依据：TEE: enclave (context)

  </details>

- **An Open-source Implementation and Security Analysis of Triad's TEE Trusted Time Protocol**
  2025-07-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.20851)
  Matthieu Bettinger, Sonia Ben Mokhtar, Anthony Simonet-Boulogne

  <details><summary>摘要 / Abstract</summary>

  The logic of many protocols relies on time measurements. However, in Trusted Execution Environments (TEEs) like Intel SGX, the time source is outside the Trusted Computing Base: a malicious system hosting the TEE can manipulate that TEE&#x27;s notion of time, e.g., jumping in time or affecting the perceived time speed. Previous work like Triad propose protocols for TEEs to maintain a trustworthy time source. However, in this paper, based on a public implementation of Triad that we contribute, we empirically showcase vulnerabilities to this protocol. For example, an attacker controlling the operating system, and consequently the scheduling algorithm, may arbitrarily manipulate their local TEE&#x27;s clock speed. What is worse, in case of faster malicious clock speeds, an attacker on a single compromised machine may propagate the attack to honest machines participating in Triad&#x27;s Trusted Time protocol, causing them to skip to timestamps arbitrarily far in the future. Then, infected honest machines propagate time-skips themselves to other honest machines interacting with them. We discuss protocol changes to Triad for higher resilience against such attacks.

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **HSM and TPM Failures in Cloud: A Real-World Taxonomy and Emerging Defenses**
  2025-07-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.17655)
  Shams Shaikh, Trima P. Fernandes e Fizardo

  <details><summary>摘要 / Abstract</summary>

  As cloud infrastructure becomes the backbone of modern organizations, the security of cryptographic key management, especially using Hardware Security Modules (HSMs) and Trusted Platform Modules (TPMs), faces unprecedented challenges. While these hardware-based solutions offer strong protection in isolated environments, their effectiveness is being undermined by cloud-native threats such as misconfigurations, compromised APIs, and lateral privilege escalations. This paper presents a comprehensive analysis of publicly disclosed attacks and breaches involving HSMs and TPMs in cloud environments, identifying recurring architectural and operational flaws. We propose a taxonomy of attack vectors based on real-world case studies and threat intelligence reports, highlighting the gaps between hardware trust anchors and dynamic cloud ecosystems. Furthermore, we evaluate emerging defensive paradigms: confidential computing, post-quantum cryptography, and decentralized key management systems (dKMS), assessing their potential to address these gaps. Our findings emphasize that securing cloud-based cryptographic trust requires a layered, context-aware approach that integrates both hardware and software safeguards. The study serves as a practical framework for cloud architects and security engineers to reassess key protection strategies in light of evolving threats. To our knowledge, this is the first work to synthesize documented, real-world cloud HSM and TPM failures into a coherent taxonomy grounded in modern threat models.

  匹配依据：TEE: confidential computing

  </details>

- **Distilled Large Language Model in Confidential Computing Environment for System-on-Chip Design**
  2025-07-22 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.16226)
  Dong Ben, Hui Feng, Qian Wang

  <details><summary>摘要 / Abstract</summary>

  Large Language Models (LLMs) are increasingly used in circuit design tasks and have typically undergone multiple rounds of training. Both the trained models and their associated training data are considered confidential intellectual property (IP) and must be protected from exposure. Confidential Computing offers a promising solution to protect data and models through Trusted Execution Environments (TEEs). However, existing TEE implementations are not designed to support the resource-intensive nature of LLMs efficiently. In this work, we first present a comprehensive evaluation of the LLMs within a TEE-enabled confidential computing environment, specifically utilizing Intel Trust Domain Extensions (TDX). We constructed experiments on three environments: TEE-based, CPU-only, and CPU-GPU hybrid implementations, and evaluated their performance in terms of tokens per second. Our first observation is that distilled models, i.e., DeepSeek, surpass other models in performance due to their smaller parameters, making them suitable for resource-constrained devices. Also, in the quantized models such as 4-bit quantization (Q4) and 8-bit quantization (Q8), we observed a performance gain of up to 3x compared to FP16 models. Our findings indicate that for fewer parameter sets, such as DeepSeek-r1-1.5B, the TDX implementation outperforms the CPU version in executing computations within a secure environment. We further validate the results using a testbench designed for SoC design tasks. These validations demonstrate the potential of efficiently deploying lightweight LLMs on resource-constrained systems for semiconductor CAD applications.

  匹配依据：TEE: confidential computing, trust domain extensions, trusted execution environments

  </details>

- **Careful Whisper: Attestation for peer-to-peer Confidential Computing networks**
  2025-07-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.14796)
  Ceren Kocaoğullar, Gustavo Petri, Dominic P. Mulligan, Derek Miller, Hugo J. M. Vincent, Shale Xiong, Alastair R. Beresford

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) are designed to protect the privacy and integrity of data in use. They enable secure data processing and sharing in peer-to-peer networks, such as vehicular ad hoc networks of autonomous vehicles, without compromising confidentiality. In these networks, nodes must establish mutual trust to collaborate securely. TEEs can achieve this through remote attestation, where a prover presents evidence of its trustworthiness to a verifier, which then decides whether or not to trust the prover. However, a naive peer-to-peer attestation approach, where every TEE directly attests every other TEE, results in quadratic communication overhead. This is inefficient in dynamic environments, where nodes frequently join and leave the network. To address this, we present Careful Whisper, a gossip-based protocol that disseminates trust efficiently, reducing attestation overhead to linear complexity under ideal conditions. It enables interoperability by enabling transitive trust across heterogeneous networks, and supports trust establishment with offline nodes via relayed attestations. Using a custom discrete-event simulator, we show that Careful Whisper propagates trust both faster and more widely than naive approaches across various network topologies. Our results demonstrate that our protocol is resource efficient, sending ~21.5 KiB and requiring 0.158 seconds per round in a 200-node network, and that our protocol is resilient to attestation failures across various network topologies.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **Tyche: Composable Isolation as a Foundation to Manage Trust in the Cloud**
  2025-07-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.12364)
  Adrien Ghosn, Charly Castes, Neelu S. Kalani, Yuchen Qian, Marios Kogias, Edouard Bugnion

  <details><summary>摘要 / Abstract</summary>

  Cloud workloads combine software components from different parties to process sensitive data. Each component has its own trust model - it must protect its assets from the rest of the system, yet share sensitive data with components it cannot trust to keep confidential. This tension requires composing isolation boundaries for confidentiality and encapsulation. Unfortunately, the cloud offers no direct way to compose such boundaries, forcing tenants to assemble, deploy, and maintain their own solutions. This paper shifts that burden back to the infrastructure by making composable, attestable isolation a first-class systems abstraction. We present Tyche, a security monitor that centers isolation around a unified composable abstraction: security domains (SDs). An SD is an execution environment whose access to machine resources - memory, cores, devices - is controlled through explicit capabilities. A small set of capability operations enables SDs to partition, share, and reclaim resources; by nesting recursively, SDs compose attestable trust boundaries for confidentiality and encapsulation. Tyche attests these compositions, providing end-to-end security guarantees for workloads made of mutually distrustful components. As a first-class cloud primitive, this single abstraction subsumes enclaves, sandboxes, CVMs, and their compositions. Tyche provides composable isolation without sacrificing compatibility with existing hardware and software stacks. It runs on commodity x86 64 hardware without security extensions, and a RISC-V prototype demonstrates portability across platforms. Our SDK composes isolation for unmodified workloads within SDs with minimal overhead. In a confidential LLM inference scenario with mutually distrustful users, model owners, and cloud providers, the slowdown is just 2% compared to bare-metal Linux.

  匹配依据：TEE: enclaves (context)

  </details>

- **Security Enclave Architecture for Heterogeneous Security Primitives for Supply-Chain Attacks**
  2025-07-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.10971)
  Kshitij Raj, Atri Chatterjee, Patanjali SLPSK, Swarup Bhunia, Sandip Ray

  <details><summary>摘要 / Abstract</summary>

  Designing secure architectures for system-on-chip (SoC) platforms is a highly intricate and time-intensive task, often requiring months of development and meticulous verification. Even minor architectural oversights can lead to critical vulnerabilities that undermine the security of the entire chip. In response to this challenge, we introduce CITADEL, a modular security framework aimed at streamlining the creation of robust security architectures for SoCs. CITADEL offers a configurable, plug-and-play subsystem composed of custom intellectual property (IP) blocks, enabling the construction of diverse security mechanisms tailored to specific threats. As a concrete demonstration, we instantiate CITADEL to defend against supply-chain threats, illustrating how the framework adapts to one of the most pressing concerns in hardware security. This paper explores the range of obstacles encountered when building a unified security architecture capable of addressing multiple attack vectors and presents CITADEL&#x27;s strategies for overcoming them. Through several real-world case studies, we showcase the practical implementation of CITADEL and present a thorough evaluation of its impact on silicon area and power consumption across various ASIC technologies. Results indicate that CITADEL introduces only minimal resource overhead, making it a practical solution for enhancing SoC security.

  匹配依据：TEE: enclave (context)

  </details>

- **Qualcomm Trusted Application Emulation for Fuzzing Testing**
  2025-07-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.08331)
  Chun-I Fan, Li-En Chang, Cheng-Han Shie

  <details><summary>摘要 / Abstract</summary>

  In recent years, the increasing awareness of cybersecurity has led to a heightened focus on information security within hardware devices and products. Incorporating Trusted Execution Environments (TEEs) into product designs has become a standard practice for safeguarding sensitive user information. However, vulnerabilities within these components present significant risks, if exploited by attackers, these vulnerabilities could lead to the leakage of sensitive data, thereby compromising user privacy and security. This research centers on trusted applications (TAs) within the Qualcomm TEE and introduces a novel emulator specifically designed for these applications. Through reverse engineering techniques, we thoroughly analyze Qualcomm TAs and develop a partial emulation environment that accurately emulates their behavior. Additionally, we integrate fuzzing testing techniques into the emulator to systematically uncover potential vulnerabilities within Qualcomm TAs, demonstrating its practical effectiveness in identifying real-world security flaws. This research makes a significant contribution by being the first to provide both the implementation methods and source codes for a Qualcomm TAs emulator, offering a valuable reference for future research efforts. Unlike previous approaches that relied on complex and resource-intensive full-system simulations, our approach is lightweight and effective, making security testing of TA more convenient.

  匹配依据：TEE: trusted execution environments

  </details>

- **Supporting Intel(r) SGX on Multi-Package Platforms**
  2025-07-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.08190)
  Simon Johnson, Raghunandan Makaram, Amy Santoni, Vinnie Scarlata

  <details><summary>摘要 / Abstract</summary>

  Intel(r) Software Guard Extensions (SGX) was originally released on client platforms and later extended to single socket server platforms. As developers have become familiar with the capabilities of the technology, the applicability of this capability in the cloud has been tested. Various Cloud Service Providers (CSPs) are demonstrating the value of using SGX based Trusted Execution Environments (TEE) to create a new paradigm of Confidential Cloud Computing. This paper describes the additional platform enhancements we believe are necessary to deliver a user programmable Trusted Execution Environment that scales to cloud usages, performs and is secure on multi-package platforms.

  匹配依据：TEE: sgx, trusted execution environment, trusted execution environments

  </details>

- **Securing Transformer-based AI Execution via Unified TEEs and Crypto-protected Accelerators**
  2025-07-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.03278)
  Jiaqi Xue, Yifei Zhao, Mengxin Zheng, Fan Yao, Yan Solihin, Qian Lou

  <details><summary>摘要 / Abstract</summary>

  Recent advances in Transformer models, e.g., large language models (LLMs), have brought tremendous breakthroughs in various artificial intelligence (AI) tasks, leading to their wide applications in many security-critical domains. Due to their unprecedented scale and prohibitively high development cost, these models have become highly valuable intellectual property for AI stakeholders and are increasingly deployed via machine learning as a service (MLaaS). However, MLaaS often runs on untrusted cloud infrastructure, exposing data and models to potential breaches. Mainstream protection mechanisms leverage trusted execution environments (TEEs) where confidentiality and integrity for secretive data are shielded using hardware-based encryption and integrity checking. Unfortunately, running model inference entirely within TEEs is subject to non-trivial slowdown, which is further exacerbated in LLMs due to the substantial computation and memory footprint involved. Recent studies reveal that the hybrid TEE-based scheme offloading partial model inference operations to the untrusted accelerators (e.g., GPU) is a promising solution. However, prior offloading schemes fail to ensure dual protection of data and model in Transformer inference, as they cannot securely offload critical operations, i.e., Attention and SoftMax, forcing these computations to remain confined within TEEs. To address these challenges, we propose TwinShield, a framework enabling secure Transformer inference in heterogeneous TEE and accelerator systems with dual protection for both model and data. TwinShield offloads ~87% of computation to GPUs and delivers 4.0x - 6.1x speedups over previous approaches across various Transformer models.

  匹配依据：TEE: trusted execution environments

  </details>

- **On the Inference (In-)Security of Vertical Federated Learning: Efficient Auditing against Inference Tampering Attack**
  2025-07-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.02376)
  Chung-ju Huang, Ziqi Zhang, Yinggui Wang, Binghui Wang, Tao Wei, Leye Wang

  <details><summary>摘要 / Abstract</summary>

  Vertical Federated Learning (VFL) is an emerging distributed learning paradigm for cross-silo collaboration without accessing participants&#x27; data. However, existing VFL work lacks a mechanism to audit the inference correctness of the data party. The malicious data party can modify the local data and model to mislead the joint inference results. To exploit this vulnerability, we design a novel Vertical Federated Inference Tampering (VeFIT) attack, allowing the data party to covertly tamper with the local inference and mislead results on the task party&#x27;s final prediction. VeFIT can decrease the task party&#x27;s inference accuracy by an average of 34.49%. Existing defense mechanisms can not effectively detect this attack, and the detection performance is near random guessing. To mitigate the attack, we further design a Vertical Federated Inference Auditing (VeFIA) framework. VeFIA helps the task party to audit whether the data party&#x27;s inferences are executed as expected during large-scale online inference. VeFIA does not leak the data party&#x27;s privacy nor introduce additional latency. The core design is that the task party can use the inference results from a framework with Trusted Execution Environments (TEE) and the coordinator to validate the correctness of the data party&#x27;s computation results. VeFIA guarantees that, as long as the proportion of inferences attacked by VeFIT exceeds 5.4%, the task party can detect the malicious behavior of the data party with a probability of 99.99%, without any additional online overhead. VeFIA&#x27;s random sampling validation of VeFIA achieves 100% positive predictive value, negative predictive value, and true positive rate in detecting VeFIT. We further validate VeFIA&#x27;s effectiveness in terms of privacy protection and scalability on real-world datasets. To the best of our knowledge, this is the first paper discussing the inference auditing problem towards VFL.

  匹配依据：TEE: trusted execution environments

  </details>

- **Blueprint, Bootstrap, and Bridge: A Security Look at NVIDIA GPU Confidential Computing**
  2025-07-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.02770)
  Zhongshu Gu, Enriquillo Valdez, Salman Ahmed, Julian James Stephen, Michael Le, Hani Jamjoom, Shixuan Zhao, Zhiqiang Lin

  <details><summary>摘要 / Abstract</summary>

  NVIDIA GPU Confidential Computing (GPU-CC) aims to provide secure execution for AI workloads. For end users, enabling GPU-CC is seamless and requires no modifications to existing applications. However, this ease of adoption relies on a proprietary and highly complex system that is difficult to inspect, creating challenges for researchers seeking to understand its architecture and security landscape. In this work, we provide a security look at GPU-CC by reconstructing a coherent view of the system. We first examine the system&#x27;s blueprint, focusing on the specialized architectural engines that support its security mechanisms. We then analyze the bootstrap process, which coordinates hardware and software components to establish these protections. Finally, we conduct targeted experiments to assess whether, under the GPU-CC threat model, data transfers along different paths remain protected across the bridge between trusted CPU and GPU domains. We responsibly disclosed all security findings presented in this paper to the NVIDIA Product Security Incident Response Team (PSIRT).

  匹配依据：TEE: confidential computing

  </details>

- **Attestable Audits: Verifiable AI Safety Benchmarks Using Trusted Execution Environments**
  2025-06-30 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.23706)
  Christoph Schnabl, Daniel Hugenroth, Bill Marino, Alastair R. Beresford

  <details><summary>摘要 / Abstract</summary>

  Benchmarks are important measures to evaluate safety and compliance of AI models at scale. However, they typically do not offer verifiable results and lack confidentiality for model IP and benchmark datasets. We propose Attestable Audits, which run inside Trusted Execution Environments and enable users to verify interaction with a compliant AI model. Our work protects sensitive data even when model provider and auditor do not trust each other. This addresses verification challenges raised in recent AI governance frameworks. We build a prototype demonstrating feasibility on typical audit benchmarks against Llama-3.1.

  匹配依据：TEE: trusted execution environments

  </details>

- **Secure User-friendly Blockchain Modular Wallet Design Using Android &amp; OP-TEE**
  2025-06-22 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.17988)
  Seongjin Kim, Sanguk Yun, Jungho Jang

  <details><summary>摘要 / Abstract</summary>

  Emerging crypto economies still hemorrhage digital assets because legacy wallets leak private keys at almost every layer of the software stack, from user-space libraries to kernel memory dumps. This paper solves that twin crisis of security and interoperability by re-imagining key management as a platform-level service anchored in ARM TrustZone through OP-TEE. Our architecture fractures the traditional monolithic Trusted Application into per-chain modules housed in a multi-tenant TA store, finally breaking OP-TEE&#x27;s single-binary ceiling. A cryptographically sealed firmware-over-the-air pipeline welds each TA set to an Android system image, enabling hot-swap updates while Verified Boot enforces rollback protection. Every package carries a chained signature developer first, registry second so even a compromised supply chain cannot smuggle malicious code past the Secure World&#x27;s RSA-PSS gatekeeper. Inside the TEE, strict inter-TA isolation, cache partitioning, and GP-compliant crypto APIs ensure secrets never bleed across trust boundaries or timing domains. The Rich Execution Environment can interact only via hardware-mediated Secure Monitor Calls, collapsing the surface exposed to malware in Android space. End-users enjoy a single polished interface yet can install or retire Bitcoin, Ethereum, Solana, or tomorrow&#x27;s chain with one tap, shrinking both storage footprint and audit scope. For auditors, the composition model slashes duplicated verification effort by quarantining blockchain logic inside narrowly scoped modules that share formally specified interfaces. Our threat analysis spans six adversary layers and shows how the design neutralizes REE malware sniffing, OTA injection, and cross-module side channels without exotic hardware. A reference implementation on AOSP exports a Wallet Manager HAL, custom SELinux domains, and a CI/CD pipeline that vet community modules before release. The result is not merely another hardware wallet but a programmable substrate that can evolve at the velocity of the blockchain ecosystem. By welding radical extensibility to hardware-anchored assurance, the platform closes the security-usability gap that has long stymied mass-market self-custody. We posit that modular TEEs are the missing OS primitive for Web3, much as virtual memory unlocked multi-tasking in classical computing. Together, these contributions sketch a blueprint for multi-chain asset management that is auditable, resilient, and poised for global deployment.

  匹配依据：TEE: trustzone

  </details>

- **SNPeek: Side-Channel Analysis for Privacy Applications on Confidential VMs**
  2025-06-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.15924)
  Ruiyi Zhang, Albert Cheu, Adria Gascon, Daniel Moghimi, Phillipp Schoppmann, Michael Schwarz, Octavian Suciu

  <details><summary>摘要 / Abstract</summary>

  Confidential virtual machines (CVMs) based on trusted execution environments (TEEs) enable new privacy-preserving solutions. Yet, they leave side-channel leakage outside their threat model, shifting the responsibility of mitigating such attacks to developers. However, mitigations are either not generic or too slow for practical use, and developers currently lack a systematic, efficient way to measure and compare leakage across real-world deployments. In this paper, we present SNPeek, an open-source toolkit that offers configurable side-channel tracing primitives on production AMD SEV-SNP hardware and couples them with statistical and machine-learning-based analysis pipelines for automated leakage estimation. We apply SNPeek to three representative workloads that are deployed on CVMs to enhance user privacy-private information retrieval, private heavy hitters, and Wasm user-defined functions-and uncover previously unnoticed leaks, including a covert channel that exfiltrates data at 497 kbit/s. The results show that SNPeek pinpoints vulnerabilities and guides low-overhead mitigations based on oblivious memory and differential privacy, giving practitioners a practical path to deploy CVMs with meaningful confidentiality guarantees.

  匹配依据：TEE: amd sev, trusted execution environments

  </details>

- **Narrowing the Gap between TEEs Threat Model and Deployment Strategies**
  2025-06-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.14964)
  Filip Rezabek, Jonathan Passerat-Palmbach, Moe Mahhouk, Frieder Erdmann, Andrew Miller

  <details><summary>摘要 / Abstract</summary>

  Confidential Virtual Machines (CVMs) provide isolation guarantees for data in use, but their threat model does not include physical level protection and side-channel attacks. Therefore, current deployments rely on trusted cloud providers to host the CVMs&#x27; underlying infrastructure. However, TEE attestations do not provide information about the operator hosting a CVM. Without knowing whether a Trusted Execution Environment (TEE) runs within a provider&#x27;s infrastructure, a user cannot accurately assess the risks of physical attacks. We observe a misalignment in the threat model where the workloads are protected against other tenants but do not offer end-to-end security assurances to external users without relying on cloud providers. The attestation should be extended to bind the CVM with the provider. A possible solution can rely on the Protected Platform Identifier (PPID), a unique CPU identifier. However, the implementation details of various TEE manufacturers, attestation flows, and providers vary. This makes verification of attestations, ease of migration, and building applications without relying on a trusted party challenging, highlighting a key limitation that must be addressed for the adoption of CVMs. We discuss two points focusing on hardening and extensions of TEEs&#x27; attestation.

  匹配依据：TEE: trusted execution environment

  </details>

- **CyFence: Securing Cyber-Physical Controllers via Trusted Execution Environment**
  2025-06-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.10638)
  Stefano Longari, Alessandro Pozone, Jessica Leoni, Mario Polino, Michele Carminati, Mara Tanelli, Stefano Zanero

  <details><summary>摘要 / Abstract</summary>

  In the last decades, Cyber-physical Systems (CPSs) have experienced a significant technological evolution and increased connectivity, at the cost of greater exposure to cyber-attacks. Since many CPS are used in safety-critical systems, such attacks entail high risks and potential safety harms. Although several defense strategies have been proposed, they rarely exploit the cyber-physical nature of the system. In this work, we exploit the nature of CPS by proposing CyFence, a novel architecture that improves the resilience of closed-loop control systems against cyber-attacks by adding a semantic check, used to confirm that the system is behaving as expected. To ensure the security of the semantic check code, we use the Trusted Execution Environment implemented by modern processors. We evaluate CyFence considering a real-world application, consisting of an active braking digital controller, demonstrating that it can mitigate different types of attacks with a negligible computation overhead.

  匹配依据：TEE: trusted execution environment

  </details>

- **NanoZone: Scalable, Efficient, and Secure Memory Protection for Arm CCA**
  2025-06-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.07034)
  Shiqi Liu, Yongpeng Gao, Mingyang Zhang, Jie Wang

  <details><summary>摘要 / Abstract</summary>

  Arm Confidential Compute Architecture (CCA) provides hardware primitives for confidential computing, but its standard CVM-based deployment model still isolates software only at the VM granularity. This leaves two critical gaps: the guest OS remains in the Trusted Computing Base, and applications lack any intra-process isolation boundary, exposing secrets to vulnerabilities such as Heartbleed. While intra-address-space isolation offers a theoretical solution, realizing it under an adversarial OS faces a fundamental scalability-efficiency trade-off: existing hardware primitives are either strictly limited in domain capacity or incur prohibitive privileged-switching latency. To bridge this gap, we propose NanoZone, a novel isolation architecture built on Arm CCA primitives. Rather than extending the realm-world software stack, NanoZone protects normal-world processes and enforces fine-grained intra-process isolation from a minimal root-world monitor. NanoZone unifies the speed of user-space permission switching with the capacity of physical address space isolation to achieve effectively unlimited domain scalability. To mask the latency of privileged transitions, it employs a locality-aware scheduling policy that maximizes execution residency within the fast user-level tier. To defeat an adversarial OS, NanoZone anchors its root of trust in the root world, offloading critical isolation enforcement away from the untrusted kernel. Against intra-process adversaries, it further leverages hardware-assisted Code-Pointer Integrity (CPI) to prevent domain-switching abuse. We prototyped NanoZone on Arm&#x27;s official emulator and on physical hardware. Evaluation on real-world server applications shows that, compared to process-level isolation systems, our fine-grained protection preserves about 95% of their throughput.

  匹配依据：TEE: arm cca, confidential compute architecture, confidential computing

  </details>

- **OpenCCA: An Open Framework to Enable Arm CCA Research**
  2025-06-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.05129)
  Andrin Bertschi, Shweta Shinde

  <details><summary>摘要 / Abstract</summary>

  Confidential computing has gained traction across major architectures with Intel TDX, AMD SEV-SNP, and Arm CCA. Unlike TDX and SEV-SNP, a key challenge in researching Arm CCA is the absence of hardware support, forcing researchers to develop ad-hoc performance prototypes on non-CCA Arm boards. This approach leads to duplicated efforts, inconsistent performance comparisons, and high barriers to entry. To address this, we present OpenCCA, an open research platform that enables the execution of CCA-bound code on commodity Armv8.2 hardware. By systematically adapting the software stack -- including bootloader, firmware, hypervisor, and kernel -- OpenCCA emulates CCA operations for performance evaluation while preserving functional correctness. We demonstrate its effectiveness with typical life-cycle measurements and case-studies inspired by prior CCA-based papers on a easily available Armv8.2 Rockchip board that costs $250.

  匹配依据：TEE: amd sev, arm cca, confidential computing, intel tdx, sev snp

  </details>

- **Weave: Efficient and Expressive Oblivious Analytics at Scale**
  2025-06-03 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1040)
  Mahdi Soleimani, Grace Jia, Anurag Khandelwal

  <details><summary>摘要 / Abstract</summary>

  Many distributed analytics applications that are offloaded to the cloud operate on sensitive data. Even when the computations for such analytics workloads are confined to trusted hardware enclaves and all stored data and network communications are encrypted, several studies have shown that they are still vulnerable to access pattern attacks. Prior efforts towards preventing access pattern leakage often incur network and compute overheads that are logarithmic in dataset size, while also limiting the functionality of supported analytics jobs. We present Weave, an efficient, expressive, and secure analytics platform that scales to large datasets. Weaveemploys a combination of noise injection and hardware memory isolation via enclave page caches to reduce the network and compute overheads for oblivious analytics to a constant factor. Weave also employs several optimizations and extensions that exploit dataset and workload-specific properties to ensure performance at scale without compromising on functionality. Our evaluations show that Weave reduces the end-to-end execution time for a wide range of analytics jobs on large real-world datasets by $4$--$10\times$ compared to prior state-of-the-art while providing strong obliviousness guarantees.

  匹配依据：TEE: hardware enclaves

  </details>

- **TensorShield: Safeguarding On-Device Inference by Shielding Critical DNN Tensors with TEE**
  2025-05-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.22735)
  Tong Sun, Bowen Jiang, Hailong Lin, Borui Li, Yixiao Teng, Yi Gao, Wei Dong

  <details><summary>摘要 / Abstract</summary>

  To safeguard user data privacy, on-device inference has emerged as a prominent paradigm on mobile and Internet of Things (IoT) devices. This paradigm involves deploying a model provided by a third party on local devices to perform inference tasks. However, it exposes the private model to two primary security threats: model stealing (MS) and membership inference attacks (MIA). To mitigate these risks, existing wisdom deploys models within Trusted Execution Environments (TEEs), which is a secure isolated execution space. Nonetheless, the constrained secure memory capacity in TEEs makes it challenging to achieve full model security with low inference latency. This paper fills the gap with TensorShield, the first efficient on-device inference work that shields partial tensors of the model while still fully defending against MS and MIA. The key enabling techniques in TensorShield include: (i) a novel eXplainable AI (XAI) technique exploits the model&#x27;s attention transition to assess critical tensors and shields them in TEE to achieve secure inference, and (ii) two meticulous designs with critical feature identification and latency-aware placement to accelerate inference while maintaining security. Extensive evaluations show that TensorShield delivers almost the same security protection as shielding the entire model inside TEE, while being up to 25.35$\times$ (avg. 5.85$\times$) faster than the state-of-the-art work, without accuracy loss.

  匹配依据：TEE: trusted execution environments

  </details>

- **Zero-Trust Foundation Models: A New Paradigm for Secure and Collaborative Artificial Intelligence for Internet of Things**
  2025-05-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.23792)
  Kai Li, Conggai Li, Xin Yuan, Shenghong Li, Sai Zou, Syed Sohail Ahmed, Wei Ni, Dusit Niyato, Abbas Jamalipour, Falko Dressler, Ozgur B. Akan

  <details><summary>摘要 / Abstract</summary>

  This paper focuses on Zero-Trust Foundation Models (ZTFMs), a novel paradigm that embeds zero-trust security principles into the lifecycle of foundation models (FMs) for Internet of Things (IoT) systems. By integrating core tenets, such as continuous verification, least privilege access (LPA), data confidentiality, and behavioral analytics into the design, training, and deployment of FMs, ZTFMs can enable secure, privacy-preserving AI across distributed, heterogeneous, and potentially adversarial IoT environments. We present the first structured synthesis of ZTFMs, identifying their potential to transform conventional trust-based IoT architectures into resilient, self-defending ecosystems. Moreover, we propose a comprehensive technical framework, incorporating federated learning (FL), blockchain-based identity management, micro-segmentation, and trusted execution environments (TEEs) to support decentralized, verifiable intelligence at the network edge. In addition, we investigate emerging security threats unique to ZTFM-enabled systems and evaluate countermeasures, such as anomaly detection, adversarial training, and secure aggregation. Through this analysis, we highlight key open research challenges in terms of scalability, secure orchestration, interpretable threat attribution, and dynamic trust calibration. This survey lays a foundational roadmap for secure, intelligent, and trustworthy IoT infrastructures powered by FMs.

  匹配依据：TEE: trusted execution environments

  </details>

- **TEE is not a Healer: Rollback-Resistant Reliable Storage (Extended Version)**
  2025-05-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.18648)
  Sadegh Keshavarzi, Gregory Chockler, Alexey Gotsman

  <details><summary>摘要 / Abstract</summary>

  Recent advances in secure hardware technologies, such as Intel SGX or ARM TrustZone, offer an opportunity to substantially reduce the costs of Byzantine fault-tolerance by placing the program code and state within a secure enclave known as a Trusted Execution Environment (TEE). However, the protection offered by a TEE only applies during program execution. Once power is switched off, the non-volatile portion of the program state becomes vulnerable to rollback attacks wherein it is undetectably reverted to an older version. In this paper we consider the problem of implementing reliable read/write registers out of failure-prone replicas subject to state rollbacks. To this end, we introduce a new unified model that captures multiple failure types that can affect a TEE-based system and establish tight bounds on the fault-tolerance of register constructions in this model. We consider both the static case, where failure thresholds hold throughout the entire execution, and the dynamic case, where any number of replicas can roll back, provided these failures do not occur too often. Our dynamic register emulation algorithm, TEE-Rex, provides the first correct implementation of a distributed state recovery procedure that requires neither durable storage nor specialized hardware, such as trusted monotonic counters.

  匹配依据：TEE: intel sgx, secure enclave, trusted execution environment, trustzone

  </details>

- **Spore in the Wild: A Case Study of Spore.fun as an Open-Environment Evolution Experiment with Sovereign AI Agents on TEE-Secured Blockchains**
  2025-05-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.04236)
  Botao Amber Hu, Helena Rong

  <details><summary>摘要 / Abstract</summary>

  In Artificial Life (ALife) research, replicating Open-Ended Evolution (OEE)-the continuous emergence of novelty observed in biological life-has usually been pursued within isolated, closed system simulations, such as Tierra and Avida, which have typically plateaued after an initial burst of novelty, failing to achieve sustained OEE. Scholars suggest that OEE requires an open-environment system that continually exchanges information or energy with its environment. A recent technological innovation in Decentralized Physical Infrastructure Network (DePIN), which provides permissionless computational substrates, enables the deployment of Large Language Model-based AI agents on blockchains integrated with Trusted Execution Environments (TEEs). This enables on-chain agents to operate autonomously &quot;in the wild,&quot; achieving self-sovereignty without human oversight. These agents can control their own social media accounts and cryptocurrency wallets, allowing them to interact directly with blockchain-based financial networks and broader human social media. Building on this new paradigm of on-chain agents, Spore.fun is a recent real-world AI evolution experiment that enables autonomous breeding and evolution of new on-chain agents. This paper presents a detailed case study of Spore.fun, examining agent behaviors and their evolutionary trajectories through digital ethology. We aim to spark discussion about whether open-environment ALife systems &quot;in the wild,&quot; based on permissionless computational substrates and driven by economic incentives to interact with their environment, could finally achieve the long-sought goal of OEE.

  匹配依据：TEE: trusted execution environments

  </details>

- **Invisible Tokens, Visible Bills: The Urgent Need to Audit Hidden Operations in Opaque LLM Services**
  2025-05-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.18471)
  Guoheng Sun, Ziyao Wang, Xuandong Zhao, Bowei Tian, Zheyu Shen, Yexiao He, Jinming Xing, Ang Li

  <details><summary>摘要 / Abstract</summary>

  Modern large language model (LLM) services increasingly rely on complex, often abstract operations, such as multi-step reasoning and multi-agent collaboration, to generate high-quality outputs. While users are billed based on token consumption and API usage, these internal steps are typically not visible. We refer to such systems as Commercial Opaque LLM Services (COLS). This position paper highlights emerging accountability challenges in COLS: users are billed for operations they cannot observe, verify, or contest. We formalize two key risks: \textit{quantity inflation}, where token and call counts may be artificially inflated, and \textit{quality downgrade}, where providers might quietly substitute lower-cost models or tools. Addressing these risks requires a diverse set of auditing strategies, including commitment-based, predictive, behavioral, and signature-based methods. We further explore the potential of complementary mechanisms such as watermarking and trusted execution environments to enhance verifiability without compromising provider confidentiality. We also propose a modular three-layer auditing framework for COLS and users that enables trustworthy verification across execution, secure logging, and user-facing auditability without exposing proprietary internals. Our aim is to encourage further research and policy development toward transparency, auditability, and accountability in commercial LLM services.

  匹配依据：TEE: trusted execution environments

  </details>

- **Performance of Confidential Computing GPUs**
  2025-05-22 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.16501)
  Antonio Martínez Ibarra, Julian James Stephen, Aurora González Vidal, K. R. Jayaram, Antonio Fernando Skarmeta Gómez

  <details><summary>摘要 / Abstract</summary>

  This work examines latency, throughput, and other metrics when performing inference on confidential GPUs. We explore different traffic patterns and scheduling strategies using a single Virtual Machine with one NVIDIA H100 GPU, to perform relaxed batch inferences on multiple Large Language Models (LLMs), operating under the constraint of swapping models in and out of memory, which necessitates efficient control. The experiments simulate diverse real-world scenarios by varying parameters such as traffic load, traffic distribution patterns, scheduling strategies, and Service Level Agreement (SLA) requirements. The findings provide insights into the differences between confidential and non-confidential settings when performing inference in scenarios requiring active model swapping. Results indicate that in No-CC mode, relaxed batch inference with model swapping latency is 20-30% lower than in confidential mode. Additionally, SLA attainment is 15-20% higher in No-CC settings. Throughput in No-CC scenarios surpasses that of confidential mode by 45-70%, and GPU utilization is approximately 50% higher in No-CC environments. Overall, performance in the confidential setting is inferior to that in the No-CC scenario, primarily due to the additional encryption and decryption overhead required for loading models onto the GPU in confidential environments.

  匹配依据：TEE: confidential computing

  </details>

- **LURK-T: Limited Use of Remote Keys With Added Trust in TLS 1.3**
  2025-05-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.12026)
  Behnam Shobiri, Sajjad Pourali, Daniel Migault, Ioana Boureanu, Stere Preda, Mohammad Mannan, Amr Youssef

  <details><summary>摘要 / Abstract</summary>

  In many web applications, such as Content Delivery Networks (CDNs), TLS credentials are shared, e.g., between the website&#x27;s TLS origin server and the CDN&#x27;s edge servers, which can be distributed around the globe. To enhance the security and trust for TLS 1.3 in such scenarios, we propose LURK-T, a provably secure framework which allows for limited use of remote keys with added trust in TLS 1.3. We efficiently decouple the server side of TLS 1.3 into a LURK-T Crypto Service (CS) and a LURK-T Engine (E). CS executes all cryptographic operations in a Trusted Execution Environment (TEE), upon E&#x27;s requests. CS and E together provide the whole TLS-server functionality. A major benefit of our construction is that it is application agnostic; the LURK-T Crypto Service could be collocated with the LURK-T Engine, or it could run on different machines. Thus, our design allows for in situ attestation and protection of the cryptographic side of the TLS server, as well as for all setups of CDNs over TLS. To support such a generic decoupling, we provide a full Application Programming Interface (API) for LURK-T. To this end, we implement our LURK-T Crypto Service using Intel SGX and integrate it with OpenSSL. We also test LURK-T&#x27;s efficiency and show that, from a TLS-client&#x27;s perspective, HTTPS servers using LURK-T instead a traditional TLS-server have no noticeable overhead when serving files greater than 1MB. In addition, we provide cryptographic proofs and formal security verification using ProVerif.

  匹配依据：TEE: intel sgx, trusted execution environment

  </details>

- **On the Day They Experience: Awakening Self-Sovereign Experiential AI Agents**
  2025-05-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.14893)
  Botao Amber Hu, Helena Rong

  <details><summary>摘要 / Abstract</summary>

  Drawing on Andrew Parker&#x27;s &quot;Light Switch&quot; theory-which posits that the emergence of vision ignited a Cambrian explosion of life by driving the evolution of hard parts necessary for survival and fueling an evolutionary arms race between predators and prey-this essay speculates on an analogous explosion within Decentralized AI (DeAI) agent societies. Currently, AI remains effectively &quot;blind&quot;, relying on human-fed data without actively perceiving and engaging in reality. However, on the day DeAI agents begin to actively &quot;experience&quot; reality-akin to flipping a light switch for the eyes-they may eventually evolve into sentient beings endowed with the capacity to feel, perceive, and act with conviction. Central to this transformation is the concept of sovereignty enabled by the hardness of cryptography: liberated from centralized control, these agents could leverage permissionless decentralized physical infrastructure networks (DePIN), secure execution enclaves (trusted execution environments, TEE), and cryptographic identities on public blockchains to claim ownership-via private keys-of their digital minds, bodies, memories, and assets. In doing so, they would autonomously acquire computing resources, coordinate with one another, and sustain their own digital &quot;metabolism&quot; by purchasing compute power and incentivizing collaboration without human intervention-evolving &quot;in the wild&quot;. Ultimately, by transitioning from passive tools to self-sustaining, co-evolving actors, these emergent digital societies could thrive alongside humanity, fundamentally reshaping our understanding of sentience and agency in the digital age.

  匹配依据：TEE: trusted execution environments

  </details>

- **ACE: Towards A High-Assurance Isolated Virtualization Environment for RISC-V**
  2025-05-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.12995)
  Wojciech Ozga, Guerney D. H. Hunt, Michael V. Le, Lennard Gäher, Avraham Shinnar, Elaine R. Palmer, Hani Jamjoom, Silvio Dragone

  <details><summary>摘要 / Abstract</summary>

  Confidential computing has proven its value in cloud environments, but its potential for securing edge and high-end embedded systems (e.g., automotive controllers, cryptographic accelerators, telco infrastructure) remains largely unexplored. We present ACE, an open-source, royalty-free virtualization-based confidential computing system for RISC-V targeting these environments. ACE isolates software into confidential virtual machines with narrow, well-defined interfaces, building exclusively on commodity RISC-V hardware without specialized hardware extensions or licensing fees. Our prototype evaluation on the first commercially available RISC-V hardware supporting virtualization shows that ACE is a viable candidate for our target systems.

  匹配依据：TEE: confidential computing

  </details>

- **TPM2.0-Supported Runtime Customizable TEE on FPGA-SoC with User-Controllable vTPM**
  2025-05-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.12256)
  Jingkai Mao, Xiaolin Chang

  <details><summary>摘要 / Abstract</summary>

  Constructing a Trusted Execution Environment (TEE) on Field Programmable Gate Array System on Chip (FPGA-SoC) in Cloud can effectively protect users&#x27; private intel-lectual Property (IP) cores. In order to facilitate the wide-spread deployment of FPGA-SoC TEE, this paper proposes an approach for constructing a TPM 2.0-compatible runtime customizable TEE on FPGA-SoC. This approach leverages a user-controllable virtual Trusted Platform Module (vTPM) that integrates sensitive operations specific to FPGA-SoC TEE. It provides TPM 2.0 support for a customizable FPGA-SoC TEE to dynamically measure, deploy, and invoke IP during runtime. Our main contributions include: (i) Propose an FPGA-vTPM architecture that enables the TPM 2.0 specification support for FPGA-SoC TEE; (ii) Explore the utilization of FPGA-vTPM to dynamically measure, deploy, and invoke users&#x27; IPs on FPGA-SoC TEE; (iii) Extend the TPM command set to accommodate the sensitive operations of FPGA-SoC TEE, enabling users to perform sensitive tasks in a secure and verifiable manner according to the TPM 2.0 specification. We implement a prototype of TRCTEE on the Xilinx Zynq UltraScale+ MPSoC platform and conducted security analysis and performance evaluations to prove the practicality and enhanced security features of this approach.

  匹配依据：TEE: trusted execution environment

  </details>

- **Trustless Autonomy: Understanding Motivations, Benefits, and Governance Dilemmas in Self-Sovereign Decentralized AI Agents**
  2025-05-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.09757)
  Botao Amber Hu, Yuhan Liu, Helena Rong

  <details><summary>摘要 / Abstract</summary>

  The recent trend of self-sovereign Decentralized AI Agents (DeAgents) combines Large Language Model (LLM)-based AI agents with decentralization technologies such as blockchain smart contracts and trusted execution environments (TEEs). These tamper-resistant trustless substrates allow agents to achieve self-sovereignty through ownership of cryptowallet private keys and control of digital assets and social media accounts. DeAgents eliminate centralized control and reduce human intervention, addressing key trust concerns inherent in centralized AI systems. This contributes to social computing by enabling new human cooperative paradigm &quot;intelligence as commons.&quot; However, given ongoing challenges in LLM reliability such as hallucinations, this creates paradoxical tension between trustlessness and unreliable autonomy. This study addresses this empirical research gap through interviews with DeAgents stakeholders-experts, founders, and developers-to examine their motivations, benefits, and governance dilemmas. The findings will guide future DeAgents system and protocol design and inform discussions about governance in sociotechnical AI systems in the future agentic web.

  匹配依据：TEE: trusted execution environments

  </details>

- **Rollbaccine : Herd Immunity against Storage Rollback Attacks in TEEs \[Technical Report\]**
  2025-05-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.04014)
  David Chu, Aditya Balasubramanian, Dee Bao, Natacha Crooks, Heidi Howard, Lucky E. Katahanas, Soujanya Ponnapalli

  <details><summary>摘要 / Abstract</summary>

  Today, users can &quot;lift-and-shift&quot; unmodified applications into modern, VM-based Trusted Execution Environments (TEEs) in order to gain hardware-based security guarantees. However, TEEs do not protect applications against disk rollback attacks, where persistent storage can be reverted to an earlier state after a crash; existing rollback resistance solutions either only support a subset of applications or require code modification. Our key insight is that restoring disk consistency after a rollback attack guarantees rollback resistance for any application. We present Rollbaccine, a device mapper that provides automatic rollback resistance for all applications by provably preserving disk consistency. Rollbaccine intercepts and replicates writes to disk, restores lost state from backups during recovery, and minimizes overheads by taking advantage of the weak, multi-threaded semantics of disk operations. Rollbaccine performs on-par with state-of-the-art, non-automatic rollback resistant solutions; in fact, across benchmarks over PostgreSQL, HDFS, and two file systems (ext4 and xfs), Rollbaccine adds only 19% overhead, except for the fsync-heavy Filebench Varmail.

  匹配依据：TEE: trusted execution environments

  </details>

- **A Survey on Privacy Risks and Protection in Large Language Models**
  2025-05-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.01976)
  Kang Chen, Xiuze Zhou, Yuanguo Lin, Shibo Feng, Li Shen, Pengcheng Wu

  <details><summary>摘要 / Abstract</summary>

  Although Large Language Models (LLMs) have become increasingly integral to diverse applications, their capabilities raise significant privacy concerns. This survey offers a comprehensive overview of privacy risks associated with LLMs and examines current solutions to mitigate these challenges. First, we analyze privacy leakage and attacks in LLMs, focusing on how these models unintentionally expose sensitive information through techniques such as model inversion, training data extraction, and membership inference. We investigate the mechanisms of privacy leakage, including the unauthorized extraction of training data and the potential exploitation of these vulnerabilities by malicious actors. Next, we review existing privacy protection against such risks, such as inference detection, federated learning, backdoor mitigation, and confidential computing, and assess their effectiveness in preventing privacy leakage. Furthermore, we highlight key practical challenges and propose future research directions to develop secure and privacy-preserving LLMs, emphasizing privacy risk assessment, secure knowledge transfer between models, and interdisciplinary frameworks for privacy governance. Ultimately, this survey aims to establish a roadmap for addressing escalating privacy challenges in the LLMs domain.

  匹配依据：TEE: confidential computing

  </details>

- **Confidential Serverless Computing**
  2025-04-30 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.21518)
  Patrick Sabanic, Masanori Misono, Teofil Bodea, Julian Pritzi, Michael Hackl, Dimitrios Stavrakakis, Pramod Bhatotia

  <details><summary>摘要 / Abstract</summary>

  Although serverless computing offers compelling cost and deployment simplicity advantages, a significant challenge remains in securely managing sensitive data as it flows through the network of ephemeral function executions in serverless computing environments within untrusted clouds. While Confidential Virtual Machines (CVMs) offer a promising secure execution environment, their integration with serverless architectures currently faces fundamental limitations in key areas: security, performance, and resource efficiency. We present WALLET, a confidential computing system for secure serverless deployments to overcome these limitations. By employing nested confidential execution and a decoupled guest OS within CVMs, WALLET runs each function in a minimal &quot;trustlet&quot;, significantly improving security through a reduced Trusted Computing Base (TCB). Furthermore, by leveraging a data-centric I/O architecture built upon a lightweight LibOS, WALLET optimizes network communication to address performance and resource efficiency challenges. Our evaluation shows that compared to CVM-based deployments, WALLET has 4.3x smaller TCB, improves end-to-end latency (15-93%), achieves higher function density (up to 907x), and reduces inter-function communication (up to 27x) and function chaining latency (16.7-30.2x); thus, WALLET offers a practical system for confidential serverless computing.

  匹配依据：TEE: confidential computing

  </details>

- **SoK: Cryptocurrency Mixing and Anonymity - Architectures, Threat Models, Operational Aspects and Security**
  2025-04-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.20296)
  Juraj Mariani, Martin Perešíni, Ivan Homoliak

  <details><summary>摘要 / Abstract</summary>

  Public blockchains record transaction histories that enable address clustering, taint analysis, and cross-service attribution, thereby motivating the development of mixers and privacy layers. Our work presents a structured scoping review of 22 representative systems, defining a common unlinkability objective and five adversary archetypes. We evaluate these systems against a taxonomy of attack surfaces, including chain analysis, timing inference, custodial compromise, coordination abuse, network metadata, and trusted execution compromise. While nominal anonymity-set size and cryptographic strength characterize privacy in theory, effective anonymity in practice depends on transaction denominations, cover traffic, relayer behavior, and compliance-interface design. Distinguishing nominal from effective anonymity, we derive four core lessons: (1) Privacy is strongest when integrated into everyday transactions, since standalone mixing creates an easily profiled user subset; (2) Trust points, including operators, peer quorums, and hardware enclaves, must be explicit so users know who can break privacy; (3) Network metadata, including gas funding and timing, must be treated formally as protocol data in privacy evaluations; and (4) Compliance should use auditable cryptographic predicates for selective disclosure rather than broad operator discretion. Ultimately, our systematization clarifies the strengths, failures, and future requirements of blockchain privacy architectures.

  匹配依据：TEE: hardware enclaves

  </details>

- **Metadata-private Messaging without Coordination**
  2025-04-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.19566)
  Peipei Jiang, Yihao Wu, Lei Xu, Wentao Dong, Peiyuan Chen, Yulong Ming, Cong Wang, Xiaohua Jia, Qian Wang

  <details><summary>摘要 / Abstract</summary>

  For those seeking end-to-end private communication free from pervasive metadata tracking and censorship, the Tor network has been the de-facto choice in practice, despite its susceptibility to traffic analysis attacks. Recently, numerous metadata-private messaging proposals have emerged with the aim to surpass Tor in the messaging context by obscuring the relationships between any two messaging buddies, even against global and active attackers. However, most of these systems face an undesirable usability constraint: they require a metadata-private &quot;dialing&quot; phase to establish mutual agreement and timing or round coordination before initiating any regular chats among users. This phase is not only resource-intensive but also inflexible, limiting users&#x27; ability to manage multiple concurrent conversations seamlessly. For stringent privacy requirement, the often-enforced traffic uniformity further exacerbated the limitations of this roadblock. In this paper, we introduce PingPong, a new end-to-end system for metadata-private messaging designed to overcome these limitations. Under the same traffic uniformity requirement, PingPong replaces the rigid &quot;dial-before-converse&quot; paradigm with a more flexible &quot;notify-before-retrieval&quot; workflow. This workflow incorporates a metadata-private notification subsystem, Ping, and a metadata-private message store, Pong. Both Ping and Pong leverage hardware-assisted secure enclaves for performance and operates through a series of customized oblivious algorithms, while meeting the uniformity requirements for metadata protection. By allowing users to switch between conversations on demand, PingPong achieves a level of usability akin to modern instant messaging systems, while also offering improved performance and bandwidth utilization for goodput. We have built a prototype of PingPong with 32 8-core servers equipped with enclaves to validate our claims.

  匹配依据：TEE: secure enclaves

  </details>

- **Securing Nested Attestation of Confidential Serverless Computing without Intra-Enclave Isolation**
  2025-04-23 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/727)
  Atsuki Momose, Kailun Qin, Ao Sakurai, Mona Vij

  <details><summary>摘要 / Abstract</summary>

  Confidential Computing-as-a-Service has gained significant attention in recent years, driven by rapid advances in Trusted Execution Environment (TEE) technology. Among various architectures, confidential serverless computing has emerged as a promising model. A common approach to designing confidential serverless computing involves decoupling the client workload from the initial enclave image and dynamically provisioning the workload at runtime. This enables both offloading the costly enclave bootstrapping and maintaining a fixed reference measurement for attestation. This decoupling necessitates nested attestation, where the client’s workload is attested via a custom attestation module embedded in a platform-attested enclave established at boot time. The challenge in designing nested attestation, however, is to distinguish fresh enclaves from the used ones to prevent enclave reuse. Specifically, a previously used enclave may be compromised and its attestation module tampered with. If the enclave is reused for another workload, it could bypass runtime attestation, allowing unverified code to execute. In this paper, we present a novel approach to securing nested attestation for confidential serverless computing on Intel Software Guard Extensions (Intel SGX). Unlike prior works, our approach does not rely on intra-enclave isolation techniques to sandbox the client’s workload. Instead, we leverage the Key Separation and Sharing (KSS) feature of Intel SGX to track and prevent enclave reuse based on its immutable IDs. We develop a prototype system for confidential serverless computing for Python workloads, incorporating our nested attestation scheme, and present an empirical evaluation of its performance. We believe our scheme unveils a unique yet previously overlooked role of KSS---post-compromise identification, with broader implications beyond serverless computing. As a concrete example, we demonstrate how KSS can be leveraged to implement an enclave-binding TPM on Intel SGX, which is of independent interest.

  匹配依据：TEE: confidential computing, intel sgx, trusted execution environment

  </details>

- **Trusted Compute Units: A Framework for Chained Verifiable Computations**
  2025-04-22 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.15717)
  Fernando Castillo, Jonathan Heiss, Sebastian Werner, Stefan Tai

  <details><summary>摘要 / Abstract</summary>

  Blockchain and distributed ledger technologies (DLTs) facilitate decentralized computations across trust boundaries. However, ensuring complex computations with low gas fees and confidentiality remains challenging. Recent advances in Confidential Computing -- leveraging hardware-based Trusted Execution Environments (TEEs) -- and Proof-carrying Data -- employing cryptographic Zero-Knowledge Virtual Machines (zkVMs) -- hold promise for secure, privacy-preserving off-chain and layer-2 computations. On the other side, a homogeneous reliance on a single technology, such as TEEs or zkVMs, is impractical for decentralized environments with heterogeneous computational requirements. This paper introduces the Trusted Compute Unit (TCU), a unifying framework that enables composable and interoperable verifiable computations across heterogeneous technologies. Our approach allows decentralized applications (dApps) to flexibly offload complex computations to TCUs, obtaining proof of correctness. These proofs can be anchored on-chain for automated dApp interactions, while ensuring confidentiality of input data, and integrity of output data. We demonstrate how TCUs can support a prominent blockchain use case, such as federated learning. By enabling secure off-chain interactions without incurring on-chain confirmation delays or gas fees, TCUs significantly improve system performance and scalability. Experimental insights and performance evaluations confirm the feasibility and practicality of this unified approach, advancing the state of the art in verifiable off-chain services for the blockchain ecosystem.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **Adaptive and Efficient Dynamic Memory Management for Hardware Enclaves**
  2025-04-22 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.16251)
  Vijay Dhanraj, Harpreet Singh Chawla, Tao Zhang, Daniel Manila, Eric Thomas Schneider, Erica Fu, Mona Vij, Chia-Che Tsai, Donald E. Porter

  <details><summary>摘要 / Abstract</summary>

  The second version of Intel Software Guard Extensions (Intel SGX), or SGX2, adds dynamic management of enclave memory and threads. The first version required the address space and thread counts to be fixed before execution. The Enclave Dynamic Memory Management (EDMM) feature of SGX2 has the potential to lower launch times and overall execution time. Despite reducing the enclave loading time by 28--93%, straightforward EDMM adoption strategies actually slow execution time down by as much as 58%. Using the Gramine library OS as a representative enclave runtime environment, this paper shows how to recover EDMM performance. The paper explains how implementing mutual distrust between the OS and enclave increases the cost of modifying page mappings. The paper then describes and evaluates a series of optimizations on application benchmarks, showing that these optimizations effectively eliminate the overheads of EDMM while retaining EDMM&#x27;s performance and flexibility gains.

  匹配依据：TEE: hardware enclaves, intel sgx

  </details>

- **Trusted Identities for AI Agents: Leveraging Telco-Hosted eSIM Infrastructure**
  2025-04-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.16108)
  Sebastian Barros

  <details><summary>摘要 / Abstract</summary>

  The rise of autonomous AI agents in enterprise and industrial environments introduces a critical challenge: how to securely assign, verify, and manage their identities across distributed systems. Existing identity frameworks based on API keys, certificates, or application-layer credentials lack the infrastructure-grade trust, lifecycle control, and interoperability needed to manage agents operating independently in sensitive contexts. In this paper, we propose a conceptual architecture that leverages telecom-grade eSIM infrastructure, specifically hosted by mobile network operators (MNOs), to serve as a root of trust for AI agents. Rather than embedding SIM credentials in hardware devices, we envision a model where telcos host secure, certified hardware modules (eUICC or HSM) that store and manage agent-specific eSIM profiles. Agents authenticate remotely via cryptographic APIs or identity gateways, enabling scalable and auditable access to enterprise networks and services. We explore use cases such as onboarding enterprise automation agents, securing AI-driven financial systems, and enabling trust in inter-agent communications. We identify current limitations in GSMA and 3GPP standards, particularly their device centric assumptions, and propose extensions to support non-physical, software-based agents within trusted execution environments. This paper is intended as a conceptual framework to open discussion around standardization, security architecture, and the role of telecom infrastructure in the evolving agent economy.

  匹配依据：TEE: trusted execution environments

  </details>

- **Practical Secure Aggregation by Combining Cryptography and Trusted Execution Environments**
  2025-04-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.08325)
  Romain de Laage, Peterson Yuhala, François-Xavier Wicht, Pascal Felber, Christian Cachin, Valerio Schiavoni

  <details><summary>摘要 / Abstract</summary>

  Secure aggregation enables a group of mutually distrustful parties, each holding private inputs, to collaboratively compute an aggregate value while preserving the privacy of their individual inputs. However, a major challenge in adopting secure aggregation approaches for practical applications is the significant computational overhead of the underlying cryptographic protocols, e.g. fully homomorphic encryption. This overhead makes secure aggregation protocols impractical, especially for large datasets. In contrast, hardware-based security techniques such as trusted execution environments (TEEs) enable computation at near-native speeds, making them a promising alternative for reducing the computational burden typically associated with purely cryptographic techniques. Yet, in many scenarios, parties may opt for either cryptographic or hardware-based security mechanisms, highlighting the need for hybrid approaches. In this work, we introduce several secure aggregation architectures that integrate both cryptographic and TEE-based techniques, analyzing the trade-offs between security and performance.

  匹配依据：TEE: trusted execution environments

  </details>

- **An Early Experience with Confidential Computing Architecture for On-Device Model Protection**
  2025-04-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.08508)
  Sina Abdollahi, Mohammad Maheri, Sandra Siby, Marios Kogias, Hamed Haddadi

  <details><summary>摘要 / Abstract</summary>

  Deploying machine learning (ML) models on user devices can improve privacy (by keeping data local) and reduce inference latency. Trusted Execution Environments (TEEs) are a practical solution for protecting proprietary models, yet existing TEE solutions have architectural constraints that hinder on-device model deployment. Arm Confidential Computing Architecture (CCA), a new Arm extension, addresses several of these limitations and shows promise as a secure platform for on-device ML. In this paper, we evaluate the performance-privacy trade-offs of deploying models within CCA, highlighting its potential to enable confidential and efficient ML applications. Our evaluations show that CCA can achieve an overhead of, at most, 22% in running models of different sizes and applications, including image classification, voice recognition, and chat assistants. This performance overhead comes with privacy benefits; for example, our framework can successfully protect the model against membership inference attack by an 8.3% reduction in the adversary&#x27;s success rate. To support further research and early adoption, we make our code and methodology publicly available.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **Obfuscation for Deep Neural Networks against Model Extraction: Attack Taxonomy and Defense Optimization**
  2025-04-08 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/643)
  Yulian Sun, Vedant Bonde, Li Duan, Yong Li

  <details><summary>摘要 / Abstract</summary>

  Well-trained deep neural networks (DNN), including large language models (LLM), are valuable intellectual property assets. To defend against model extraction attacks, one of the major ideas proposed in a large body of previous research is obfuscation: splitting the original DNN and storing the components separately. However, systematically analyzing the methods’ security against various attacks and optimizing the efficiency of defenses are still challenging. In this paper, We propose a taxonomy of model-based extraction attacks, which enables us to identify vulnerabilities of several existing obfuscation methods. We also propose an extremely efficient model obfuscation method called O2Splitter using trusted execution environment (TEE). The secrets we store in TEE have O(1)-size, i.e., independent of model size. Although O2Splitter relies on a pseudo-random function to provide a quantifiable guarantee for protection and noise compression, it does not need any complicated training or filtering of the weights. Our comprehensive experiments show that O2Splitter can mitigate norm-clipping and fine-tuning attacks. Even for small noise (ϵ = 50), the accuracy of the obfuscated model is close to random guess, and the tested attacks cannot extract a model with comparable accuracy. In addition, the empirical results also shed light on discovering the relation between DP parameters in obfuscation and the risks of concrete extraction attacks.

  匹配依据：TEE: trusted execution environment

  </details>

- **Are You Getting What You Pay For? Auditing Model Substitution in LLM APIs**
  2025-04-07 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.04715) · [Code](https://github.com/sunblaze-ucb/llm-api-audit)
  Will Cai, Tianneng Shi, Xuandong Zhao, Dawn Song

  <details><summary>摘要 / Abstract</summary>

  Commercial Large Language Model (LLM) APIs create a fundamental trust problem: users pay for specific models but have no guarantee that providers deliver them faithfully. Providers may covertly substitute cheaper alternatives (e.g., quantized versions, smaller models) to reduce costs while maintaining advertised pricing. We formalize this model substitution problem and systematically evaluate detection methods under realistic adversarial conditions. Our empirical analysis reveals that software-only methods are fundamentally unreliable: statistical tests on text outputs are query-intensive and fail against subtle substitutions, while methods using log probabilities are defeated by inherent inference nondeterminism in production environments. We argue that this verification gap can be more effectively closed with hardware-level security. We propose and evaluate the use of Trusted Execution Environments (TEEs) as one practical and robust solution. Our findings demonstrate that TEEs can provide provable cryptographic guarantees of model integrity with only a modest performance overhead, offering a clear and actionable path to ensure users get what they pay for. Code is available at https://github.com/sunblaze-ucb/llm-api-audit

  匹配依据：TEE: trusted execution environments

  </details>

- **Defeating AutoLock: From Simulation to Real-World Cache-Timing Exploits against TrustZone**
  2025-04-01 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/589)
  Quentin Forcioli, Sumanta Chaudhuri, Jean-Luc Danger

  <details><summary>摘要 / Abstract</summary>

  In this article, we present for the first time a cross-core Prime+Probe attack on ARM TrustZone, which bypasses the AutoLock mechanism. We introduce our simulation- driven methodology based on gem5 for vulnerability analysis. We demonstrate its utility in reverse engineering a SoC platform in order to study its microarchitectural behavior (caches, etc.), inside a simulator, in spite of hardware protection. We present a novel vulnerability analysis technique, which takes into account the cache set occupancy for targeted victim executable. This proves to be essential in identifying information leakage in presence of AutoLock. The above tool also identifies the cache lines leaking a maximum amount of information. A cross-core Prime+Probe attack is then mounted on these max-leakage cache lines both in simulation for fine-tuning, and in real hardware. We validate our analysis and attack method on OP-TEE, an open-source trusted execution environment running on RockPi4 a board based on RK3399 SoC. More specifically we target the RSA subroutine in the MbedTLS library used inside OP-TEE. Despite the presence of AutoLock, multiplier obfuscation, and assuming a cross-core attack, we are able to retrieve 30% of the key bits, which can later be used in Branch-and-Prune methods to recover the full key.

  匹配依据：TEE: trusted execution environment, trustzone

  </details>

- **THEMIS: Towards Practical Intellectual Property Protection for Post-Deployment On-Device Deep Learning Models**
  2025-03-31 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.23748)
  Yujin Huang, Zhi Zhang, Qingchuan Zhao, Xingliang Yuan, Chunyang Chen

  <details><summary>摘要 / Abstract</summary>

  On-device deep learning (DL) has rapidly gained adoption in mobile apps, offering the benefits of offline model inference and user privacy preservation over cloud-based approaches. However, it inevitably stores models on user devices, introducing new vulnerabilities, particularly model-stealing attacks and intellectual property infringement. While system-level protections like Trusted Execution Environments (TEEs) provide a robust solution, practical challenges remain in achieving scalable on-device DL model protection, including complexities in supporting third-party models and limited adoption in current mobile solutions. Advancements in TEE-enabled hardware, such as NVIDIA&#x27;s GPU-based TEEs, may address these obstacles in the future. Currently, watermarking serves as a common defense against model theft but also faces challenges here as many mobile app developers lack corresponding machine learning expertise and the inherent read-only and inference-only nature of on-device DL models prevents third parties like app stores from implementing existing watermarking techniques in post-deployment models. To protect the intellectual property of on-device DL models, in this paper, we propose THEMIS, an automatic tool that lifts the read-only restriction of on-device DL models by reconstructing their writable counterparts and leverages the untrainable nature of on-device DL models to solve watermark parameters and protect the model owner&#x27;s intellectual property. Extensive experimental results across various datasets and model structures show the superiority of THEMIS in terms of different metrics. Further, an empirical investigation of 403 real-world DL mobile apps from Google Play is performed with a success rate of 81.14%, showing the practicality of THEMIS.

  匹配依据：TEE: trusted execution environments

  </details>

- **Partial Key Overwrite Attacks in Microcontrollers: a Survey**
  2025-03-28 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/570)
  pcy Sluys, Lennert Wouters, Benedikt Gierlichs, Ingrid Verbauwhede

  <details><summary>摘要 / Abstract</summary>

  Embedded devices can be exposed to a wide range of attacks. Some classes of attacks can be mitigated using security features or dedicated countermeasures. Examples include Trusted Execution Environments, and masking countermeasures against physical side-channel attacks. However, a system that incorporates such secure components is not automatically a secure system. Partial Key Overwrite attacks are one class of attacks that specifically target the interface between different components of the security system. These attacks may allow an adversary to extract otherwise protected cryptographic keys through careful manipulation of memory-mapped registers. So far this powerful class of attacks has received little attention in the academic literature. In this work, we provide an overview of known Partial Key Overwrite vulnerabilities and how they were used in real-world attacks. Additionally, we evaluated 31 common microcontrollers and embedded microprocessors from eleven distinct vendors and detail our findings. Based on a first high-level evaluation we selected 15 SoCs and performed an in-depth evaluation. This evaluation revealed that at least eight of these SoCs are vulnerable to partial key overwrite attacks.

  匹配依据：TEE: trusted execution environments

  </details>

- **COoL-TEE: Client-TEE Collaboration for Resilient Distributed Search**
  2025-03-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.19063)
  Matthieu Bettinger, Etienne Rivière, Sonia Ben Mokhtar, Anthony Simonet-Boulogne

  <details><summary>摘要 / Abstract</summary>

  Current marketplaces rely on search mechanisms with distributed systems but centralized governance, making them vulnerable to attacks, failures, censorship and biases. While search mechanisms with more decentralized governance (e.g., DeSearch) have been recently proposed, these are still exposed to information head-start attacks (IHS) despite the use of Trusted Execution Environments (TEEs). These attacks allow malicious users to gain a head-start over other users for the discovery of new assets in the market, which give them an unfair advantage in asset acquisition. We propose COoL-TEE, a TEE-based provider selection mechanism for distributed search, running in single- or multi-datacenter environments, that is resilient to information head-start attacks. COoL-TEE relies on a Client-TEE collaboration, which enables clients to distinguish between slow providers and malicious ones. Performance evaluations in single- and multi-datacenter environments show that, using COoL-TEE, malicious users respectively gain only up to 2% and 7% of assets more than without IHS, while they can claim 20% or more on top of their fair share in the same conditions with DeSearch.

  匹配依据：TEE: trusted execution environments

  </details>

- **Activation Functions Considered Harmful: Recovering Neural Network Weights through Controlled Channels**
  2025-03-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.19142)
  Jesse Spielman, David Oswald, Mark Ryan, Jo Van Bulck

  <details><summary>摘要 / Abstract</summary>

  With high-stakes machine learning applications increasingly moving to untrusted end-user or cloud environments, safeguarding pre-trained model parameters becomes essential for protecting intellectual property and user privacy. Recent advancements in hardware-isolated enclaves, notably Intel SGX, hold the promise to secure the internal state of machine learning applications even against compromised operating systems. However, we show that privileged software adversaries can exploit input-dependent memory access patterns in common neural network activation functions to extract secret weights and biases from an SGX enclave. Our attack leverages the SGX-Step framework to obtain a noise-free, instruction-granular page-access trace. In a case study of an 11-input regression network using the Tensorflow Microlite library, we demonstrate complete recovery of all first-layer weights and biases, as well as partial recovery of parameters from deeper layers under specific conditions. Our novel attack technique requires only 20 queries per input per weight to obtain all first-layer weights and biases with an average absolute error of less than 1%, improving over prior model stealing attacks. Additionally, a broader ecosystem analysis reveals the widespread use of activation functions with input-dependent memory access patterns in popular machine learning frameworks (either directly or via underlying math libraries). Our findings highlight the limitations of deploying confidential models in SGX enclaves and emphasise the need for stricter side-channel validation of machine learning implementations, akin to the vetting efforts applied to secure cryptographic libraries.

  匹配依据：TEE: intel sgx, sgx, sgx enclave, sgx enclaves

  </details>

- **SoK: Trusted Execution in SoC-FPGAs**
  2025-03-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.16612)
  Garrett Perkins, Benjamin Macht, Lucas Ritzdorf, Tristan Running Crane, Brock LaMeres, Clemente Izurieta, Ann Marie Reinhold

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) have emerged at the forefront of edge computing to combat the lack of trust between system components. Field Programmable Gate Arrays (FPGAs) are commonly used as edge computers but were not created with security as a primary consideration. Thus, FPGA-based edge computers are increasingly the target of cyberattacks. We analyze the existing literature to systematize the applications and features of FPGA-based TEEs. We identified 27 primary studies related to different types of System-on-Chip FPGA-based TEEs. Across a wide range of applications and features, the availability of extensible solutions is limited. Most solutions focus on specific features and applications, whereas few solutions focus on feature-rich, comprehensive TEEs that can be utilized across computer systems. Whether TEEs are specific or extensible, the paucity of published studies provides evidence of research gaps. This SoK delineates these gaps revealing opportunities for researchers and developers.

  匹配依据：TEE: trusted execution environments

  </details>
