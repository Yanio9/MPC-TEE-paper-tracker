# 2026 · TEE · 仅预印本来源 · 第 1/2 页

[总目录](../PAPERS.md) · [下一页](2026-tee-preprint-02.md)

- **LLMs in Cloud: A Discussion on Architecture, Orchestration, and Inference**
  2026-10-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.33475)
  Jannatun Noor, Athar Noor Mohammad Rafee, Md. Sadman Haque, Sreezon Das Gupta, Atiar Osman, Md. Abu Obaida Zishan

  <details><summary>摘要 / Abstract</summary>

  The widespread deployment of foundational Large Language Models (LLM) across cloud datacenters marks a fundamental paradigm shift from stateless deep learning toward distributed, memory-intensive generative workloads. However, serving massive foundation models under stringent Service Level Objectives (SLO) exposes critical physical and system bottlenecks. These challenges include the persistent High Bandwidth Memory (HBM) wall, operational asymmetry between compute-bound prefilling and memory-bandwidth-bound decoding, explosive Key-Value (KV) cache expansion, prohibitive serverless cold starts, and hardware reliability vulnerabilities. Existing literature reviews remain layer-siloed, decoupling low-level accelerator virtualization from cluster orchestration and runtime inference, while largely overlooking defining advancements from 2024 to 2026. To address these limitations, this study presents a comprehensive, cross-layer systematic review guided by the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) 2020 framework. We synthesize a holistic taxonomy unifying hardware virtualization, cluster-level scheduling, and runtime inference optimizations, including iteration-level continuous batching, prefill-decoding disaggregation, and hierarchical KV cache offloading. Furthermore, we evaluate resilient cloud-native service architectures, examining scale-to-zero serverless paradigms, fault-tolerant checkpointing against silent data corruption, and hardware-enforced Trusted Execution Environments (TEEs) for multi-tenant isolation. Finally, we formalize the multi-dimensional Pareto trade-offs governing throughput, latency, monetary cost, and confidentiality, outlining a forward-looking research roadmap spanning Compute Express Link (CXL) memory pooling, in-memory computing, and autonomous multi-agent control planes to guide future cloud LLM infrastructure.

  匹配依据：TEE: trusted execution environments

  </details>

- **KNOX: Hardware-assisted Regulatory Sandbox for Generative Models**
  2026-10-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.27543)
  Vasisht Duddu, Adam Caulfield, Xi He

  <details><summary>摘要 / Abstract</summary>

  Regulations require companies to run AI models in a regulatory sandbox, an isolated environment that enables monitoring model behavior by regulators, prior to deployment. But, they do not spell out the technical mechanisms to design such a sandbox. Ideally, a regulatory sandbox should show (i) compliance (checks against regulations, and deviations from intended behavior, i.e., unauthorized tool and system calls); (ii) confidentiality (protects model weights from regulators); (iii) attestability (produces tamper-resistant evidence of model behavior for monitoring); and (iv) scalability (evidence is verifiable by multiple regulators). Several prior works (information-flow control, prompt-injection defenses, control-flow integrity, and traditional sandboxing) address specific compliance aspects but lack confidentiality, attestability, and scalability. TEEs meet some of these requirements, but simply running models inside a TEE is insufficient as we need compliance mechanisms. We present KNOX, the first regulatory sandbox, built by running AI workloads inside TEEs. We demonstrate KNOX using agentic workloads. For compliance, we derive an attested policy manifest (with the applicable regulations, the expected tool calls, and the permitted system calls) for a given user prompt. Before an executor performs an action, an attested reference monitor compares it against the attested policy manifest and allows it only if it matches. Every action and verdict is recorded in an attested execution graph, enabling regulators to verify the model&#x27;s execution and its compliance. We show that KNOX meets all requirements, and can check for compliance with regulations and deviations from intended behavior (e.g., due to prompt injection); and incurs low overhead (&lt;1%).

  匹配依据：TEE: tees (context)

  </details>

- **DISCO\*: DIstributed and SCalable Oblivious Joins and Oblivious Primitives**
  2026-10-20 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2572)
  Apostolos Mavrogiannakis, Xian Wang, Ioannis Demertzis, Dimitrios Papadopoulos, Minos Garofalakis

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) let clients outsource computation to untrusted clouds, but they remain vulnerable to side-channel and leakage-abuse attacks. Recent work closes this gap by combining hardware enclaves with oblivious computation, which offers strong security guarantees yet struggles to meet the performance and scalability demands of real-world deployments. In this work, we present DISCO, the first scalable, distributed, and fully oblivious database system that seamlessly combines hardware enclaves with cutting-edge oblivious primitives and novel optimizations that significantly reduce inter-server communication overheads. What distinguishes DISCO from prior work is a suite of distributed frameworks that unlock parallel computation and fundamentally shift the design paradigm of distributed oblivious systems, enabling practical deployment at scales that were unattainable with previous solutions. We provide a thorough evaluation of the performance of our system on both synthetic and real-world datasets. Our evaluation demonstrates that our design significantly reduces the gap between theory and practice, achieving 88× speedup over Jodes and 180× over SODA on non-foreign key joins with N = 2²⁵ elements. Most importantly, we report, for the first time, results for computations at the terabyte scale.

  匹配依据：TEE: hardware enclaves, trusted execution environments

  </details>

- **Pangolin: Efficient DAG-based BFT State-Machine Replication with TEE-Accelerated Commitment**
  2026-10-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.26295)
  Paul Franke-Bergmann, Maya Kuhlmann, Alexander Heß, Marc Leinweber, Rüdiger Kapitza, Hannes Hartenstein, Franz J. Hauck, Christian Berger

  <details><summary>摘要 / Abstract</summary>

  Currently many Byzantine fault-tolerant (BFT) protocols use directed acyclic graphs (DAGs) to let replicas propose blocks of requests in parallel for improved throughput. Yet, the existing DAG-based designs mainly consider the atomic-broadcast layer: They typically do not describe an efficient client interaction layer, their garbage collection is either unspecified or relies on trusted external storage, and the lowest-latency designs rely on timing assumptions that may be violated in geo-distributed deployments. In this paper, we propose the Pangolin protocol: It introduces a novel low-latency DAG-based atomic broadcast layer and completes it into an efficient state-machine replication (SMR) framework. To preserve system throughput, clients issue requests to a single replica and verify replies efficiently via compact execution proofs. Furthermore, Pangolin introduces a new garbage-collection scheme for DAGs which bounds memory usage even under full asynchrony. Pangolin leverages trusted execution environments to tolerate f Byzantine faults with only n &gt;= 2f + 1 replicas and accelerates vertex commitments significantly: Broadcasting certified vertices requires only a single communication step, and commit rules are refined to commit both frequently and early without revealing the coin-elected anchor. This way, Pangolin overtakes the fastest partially synchronous DAG protocols while being live under asynchrony: In our evaluation, Pangolin achieves an average 1.27x (up to 1.52x) latency speedup over Mysticeti.

  匹配依据：TEE: trusted execution environments

  </details>

- **Empirical Analysis of TEE-Enabled Rollup Designs**
  2026-10-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.24284)
  Claudiu-Nicu Bărbieru, Corentin Libert, Peterson Yuhala, Andrei Arusoaie, Matthieu Bettinger, Oana-Otilia Captarencu, Pascal Felber, Emanuel Onica, Etienne Rivière, Valerio Schiavoni

  <details><summary>摘要 / Abstract</summary>

  Layer 2 (L2) rollups have become the dominant scaling solution in Ethereum. At the core of these systems lies the rollup sequencer, a component that orders, executes, and submits L2 transaction blocks to the main Ethereum blockchain. The centralization of this sequencer introduces security risks, including censorship and malicious manipulation of transactions to extract maximum extractable value (MEV). Trusted execution environments (TEEs) provide strong hardware-enforced confidentiality and integrity guarantees for code and data. TEEs are strong candidates for strengthening security and ensuring verifiable neutrality in rollup sequencer operations, but multiple TEE-based designs are possible, offering different trade-offs among modularity, performance, and security guarantees. Among them, the separation of proposer and builder logic (PBS) into independent services is a strong contender against the monolithic approach that bundles all sequencer logic. Despite several proposed theoretical frameworks, there is a lack of experimental evaluation of the practicality and security trade-offs of integrating TEEs into rollup sequencers. This work addresses this gap through a comprehensive empirical study of TEE-enabled rollup designs under both PBS and monolithic sequencer models. Our experimental evaluations show that the impact of TEEs on rollup performance is small and that PBS does not significantly amplify it. We also show that PBS can lead to significant performance improvements by enabling more specialized, efficient builder logic implementations.

  匹配依据：TEE: trusted execution environments

  </details>

- **When Rotation Bounds Nothing: Streaming Image Classifiers to Field Nodes Under Physical Capture**
  2026-10-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.21276)
  Daniel Gilkarov, Ran Dubin

  <details><summary>摘要 / Abstract</summary>

  Field nodes run image classifiers locally, exposing a first-class asset, the trained model, to theft. Trusted-execution enclaves, collaborative-inference splits, and encrypted storage assume the device owner is the adversary from deployment. Here the operator owns the node, and an adversary seizing it reads only what cold-boot capture finds resident. One answer stores nothing: a chunkable multi-exit model streams into volatile memory, rotating to bound residency. We characterise the capture envelope on real LTE traces across two victims of one architecture, against passive and adaptive adversaries. Neither survives a capable adversary; recovery cost alone differs. Against a from-scratch victim the uncaptured stages must be learned: the adaptive adversary gains most at shallow seizures, ends the CIFAR-10 envelope at every rotation, and stays rotation-bounded on CIFAR100, from 42.6% of usable seizures at 5 s to 86.8% at 30 s. Against the same architecture sliced from a public pretrained backbone, the adversary downloads those stages, recovering at least 90% of maximum accuracy at all depths, taking usable CIFAR-100 seizures from 0.0% to 97.3% at 5 s, given the victim&#x27;s full labelled training set. Delivery-side secrecy raises a seizure&#x27;s price; a public copy of the withheld stages erases it.

  匹配依据：TEE: enclaves (context)

  </details>

- **BiShield-TEE: On the (In-)Security of Unilateral Weight Obfuscation in On-Device TEE-Shielded LLM Partition**
  2026-10-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.21565) · [Code](https://github.com/laduiw/BiShield-TEE)
  Zhiyuan Wang, Yuezhi Zhou, Ziqi Zhang, Zhu Zhang, Zhixing Tan, Yongheng Deng

  <details><summary>摘要 / Abstract</summary>

  On-device deployment of large language models (LLMs) is increasingly adopted due to latency and privacy requirements, but exposes proprietary models to reverse engineering and intellectual property theft. Trusted Execution Environments (TEEs) provide hardware-enforced isolation for on-device inference, yet most TEE-based parameter obfuscation relies on unilateral matrix transformations that obfuscate only the output side. We identify a vulnerability in this design, termed the Solution Determinacy Property (SDP): the obfuscation secret is uniquely determined, exposing the structure of the true key and enabling attackers to break the protection. Under our attacks, representative methods GroupCover and ArrowCloak are reduced to negligible protection, with attack accuracy reaching over 2.4 times the full-shielding black-box baseline and recovering near-complete model functionality. To address this vulnerability, we propose BiShield-TEE, a bilateral framework that induces Ambiguous Solutions through joint obfuscation of input and output dimensions, hiding the true key among many equally valid candidates. Experiments across diverse models and datasets show that BiShield-TEE confines attack accuracy to the full-shielding black-box baseline, while achieving higher inference efficiency than prior methods on real hardware. Our code is available at https://github.com/laduiw/BiShield-TEE.

  匹配依据：TEE: trusted execution environments

  </details>

- **Snapshots of TEE-Based Encrypted Databases Leak Plaintext Histograms via Dendrochronology**
  2026-10-13 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2465)
  Zachary Espiritu

  <details><summary>摘要 / Abstract</summary>

  Arborists use dendrochronology, or the study of tree &quot;growth rings&quot; (as in, the plant), to infer past environmental events. We identify an analogous, exploitable phenomenon in the indexes used by several encrypted databases (EDBs) based on trusted execution environments (TEEs). Such EDBs have been shown to leak the order of indexed values, but not the histogram (or frequency of each value), with respect to a weaker class of snapshot adversaries. This order-only leakage substantially reduces the impact of possible inference attacks. We show, in fact, frequency is recoverable in the snapshot model from many TEE-based EDBs, even if the TEE itself is &quot;secure&quot;. Our insight is simple: practical storage engines impose a strict total order on indexed keys by augmenting each key with a unique tie-breaker. If the adversary learns information about the tie-breakers, they can recover the frequencies of plaintext keys. We show this enables stronger inference attacks on several TEE-based EDBs (including Microsoft SQL Server’s Always Encrypted, StealthDB, and HeDB) to demonstrate this vulnerability’s ubiquity and point to broader lessons for TEE applications designed around legacy code.

  匹配依据：TEE: trusted execution environments

  </details>

- **FLAI Protocol: Decentralized Federated Learning with On-Chain Rewards and sPEG-Based Contribution Scoring**
  2026-10-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.17546)
  Eli Yune, Mahesh Balan

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) enables collaborative model training without data centralization but struggles with incentive alignment, accountability, and robustness under heterogeneous non-IID data. Existing decentralized FL (DeFL) systems leverage blockchains for coordination yet face high on-chain overhead, unverifiable self-reports, and weak fairness guarantees. We present the FLAI Protocol, a trusted execution environment (TEE)-backed DeFL framework that integrates enclave-validated aggregation, sparse Peer Evaluation Graph (sPEG) scoring, and on-chain settlement. sPEG incorporates peer-based quality, class coverage, promptness, effort, and reputation into composite contribution scores. The protocol formalizes contribution evaluation and tokenized incentive distribution, ensuring verifiable fairness and resilience against free-riding and collusion. We evaluate FLAI on image, text, and healthcare datasets and demonstrate parity with FedAvg in utility while improving fairness and accountability. A case study in consumer eHealth (aggregating wearable and electronic health record data for real-world evidence generation) illustrates the protocol&#x27;s applicability to privacy-critical domains where equitable rewards, auditability, and data sovereignty are essential.

  匹配依据：TEE: trusted execution environment

  </details>

- **Resource-constrained Remote Attestation of Smart Meters Using Merkle Trees in a Trusted Execution Environment**
  2026-10-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.16373)
  Amirhossein Shakiba, Hamid Reza Ghaeini, Sadegh Dorri Nogoorani

  <details><summary>摘要 / Abstract</summary>

  Smart meters are pivotal to the functioning of smart grids, as they measure and transmit energy consumption data that includes sensitive information about household energy usage patterns. While this data offers significant financial benefits, it can also reveal detailed insights into residents&#x27; daily routines, making the security of smart meters a critical concern. This paper introduces a novel remote attestation method for smart meters that ensures the integrity and privacy of data exchanged between smart meters and central servers while detecting unauthorized tampering. Our approach structures the communication data into a Merkle Tree-a hash data structure that facilitates efficient data integrity and authenticity verification. All operations involved in constructing the Merkle root and hashing critical data are executed in the secure environment of a Trusted Execution Environment (TEE) using OP-TEE, thereby maintaining the integrity and security of the smart meter&#x27;s data. Comparing our experimental results with the related works highlights the superiority of our method in terms of resource efficiency, security robustness, and the feasibility of implementation on smart meters and resource-constrained devices, thereby enhancing the overall security and reliability of smart grid systems.

  匹配依据：TEE: trusted execution environment

  </details>

- **A methodology to derive security specifications for complex electronic systems**
  2026-10-12 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2447)
  Sylvain Guilley, Ritu Ranjan Shrivstwa, Ville Yli-Mäyry

  <details><summary>摘要 / Abstract</summary>

  Modern electronic systems are becoming increas- ingly complex and must satisfy demanding performance, power, and area (PPA) constraints. Consider for instance artificial intelligence chips, aiming at datacenters running LLMs or at automotive perception, which manipulate massive data streams. Beyond performance considerations, these systems must also provide increasingly strong security and dependability guaran- tees. Indeed, when electronic systems are based on chiplets, for instance, the supply chain gets longer and therefore brings a larger number of threats. Also, those systems are very versatile, in that they can run varied multi-tenant applications. Therefore, defining what security features are required in this context with numerous stakes is not trivial. Existing scholarly research is very relevant when the security problem is well defined. The resulting scientific papers accord- ingly dig very deep: this modus operandi has proved productive in exploring new problems, and actually allowed to come up with innovative solutions. For instance, in the field of side-channel attacks, varied mitigations alongside with metrics to evaluate them have been devised. Increasing sophistication resulted from this research, as external considerations have been injected into the problem (typically, aspects such as attack order, impact of combinatorial glitches, etc.). Therefore, we face today the question of selecting the most suitable technology amongst the proliferation of state-of-the-art techniques. In addition, in complex systems, we encounter another prob- lem, namely that of defining the security problem(s). A fruitful approach in this respect is a risk based approach. Specifically, the application of a risk-oriented methodology allows to reason on the security rationale. It proceeds as follows. First, the system missions are listed. Then for each of them, the necessary assets are deduced. A threat analysis allows to identify how assets are threatened, and eventually, security requirements can be enunciated. At this stage, the task of matching relevant countermeasures becomes straightforward. This paper illustrates the methodology by deriving security specifications for datacenter and automotive chiplets. The considered missions are (secure) provisioning, trimming, debugging, booting, and remote attestation.

  匹配依据：TEE: tees (context)

  </details>

- **ARMOR: Adversary Cost Amplification via a Schema-Preserving Password-Hardening Retrofit for Resource-Constrained Systems**
  2026-10-09 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.14300)
  Avinash Srinivasan

  <details><summary>摘要 / Abstract</summary>

  Credential-database disclosure exposes Internet of Things gateways, edge servers and legacy verifiers to offline password guessing. Memory-hard key derivation functions (KDFs) are preferred but can exceed constrained-device budgets. ARMOR addresses this deployment gap with a schema-preserving verifier-side transform for database-only compromise, assuming an isolated Chain Registry. The registry holds secret per-account chains of injective operations; fixed terminal escape encoding preserves distinct pre-hash values under each chain while moving outputs outside printable ASCII. This disrupts evaluated stock tools&#x27; candidate coverage, but chain-aware attackers can generate the transformed bytes directly. We therefore evaluate a bounded chain-aware attack on $1{,}000$ paired salted-MD5 targets: it executes $89.35\times$ the plain arm&#x27;s counted salted checks, reproduced on A6000 and A100. All target passwords are in the bounded pool; same-target ambiguity enumeration and simulated login trials recover every original password. These results describe the implemented attack, not minimum attacker cost. Bare-metal transforms take microseconds, while protected storage dominates the measured TrustZone-M components; these are component measurements, not complete authentication times. ARMOR thus provides bounded chain uncertainty under registry isolation with low transform cost, although an isolated high-entropy pepper remains cryptographically stronger. ARMOR composes as KDF(ARMOR(password)) when resources permit and the KDF accepts the complete transformed output.

  匹配依据：TEE: trustzone

  </details>

- **Protecting CPU AI On Edge TEEs: WebAssembly's Promise and Practical Challenges**
  2026-10-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.12050)
  Friedrich Vandenberghe, Lachlan J. Gunn, Bruno Volckaert, Merlijn Sebrechts

  <details><summary>摘要 / Abstract</summary>

  AI models on edge hardware contain important intellectual property (IP), but an adversary can steal it when they achieve root access. Trusted Execution Environments (TEE) like Arm TrustZone protect against these Operating System (OS) level attacks. However, they are challenging to use. More precisely, it is difficult to run unaltered applications inside a TEE. This work presents a solution that allows the execution of unaltered AI models, compiled to WebAssembly, on the WebAssembly Micro Runtime (WAMR) in OP-TEE for Arm TrustZone. Additionally, this work provides an AI model distributor that encrypts the WebAssembly binary and places the encryption key in one of the device&#x27;s fuses. This way, only the WAMR Trusted Application (TA) in OP-TEE can decrypt and execute the AI model. A thorough evaluation of our solution shows that it incurs an additional overhead of 22% in comparison to an application manually ported to OP-TEE, while also facilitating the execution of unaltered AI models with an additional inference latency of 6% without significant porting effort. Overall, there is a pressing need to safeguard the IP of AI models and this work shows that there is a real promise in WebAssembly, but there remain some practical challenges.

  匹配依据：TEE: trusted execution environments, trustzone

  </details>

- **Optimal Statistical Oblivious RAM and Search Tree in the External-Memory Model**
  2026-10-08 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2419)
  Andrew Krapivin, Elaine Shi

  <details><summary>摘要 / Abstract</summary>

  Oblivious RAM (ORAM) allows a trusted client to access (encrypted) data stored in untrusted memory, such that the access patterns reveal nothing about the data or the queries. It is well-known that any ORAM scheme must suffer from a logarithmic overhead. More precisely stated, each request must incur $\Omega(\log_B N)$ block transfers on average, where $N$ is the size of the logical memory and $B$ is the block size of the oblivious implementation. Moreover, the same lower bound extends to oblivious Search Trees (ST). For upper bounds, however, we have been long stuck with a $(\log_B N)^2$ curse on two fronts: (1) Log-squared curse for statistically secure ORAMs: although optimality is known for computationally secure ORAMs for $B = \Theta(1)$ or $B \geq \log^{1+\epsilon} N$ (where $\epsilon &gt; 0$ is an arbitrarily small constant), progress has been stagnant when it comes to statistical security. (2) Log-squared curse for oblivious search trees: for search trees, we do not know how to overcome the log-squared curse even when allowing computational assumptions. In this paper, we break this long-standing log-squared curse for both oblivious search trees and statistically secure ORAM on broad parameter regimes: (1) Our first result gives an optimal, statistically secure ORAM with $O(\log_B N)$ cost as long as $B \geq \log^{1+\epsilon} N$. (2) Our second result gives an optimal, statistically secure oblivious search tree with $O(\log_B N)$ cost when $B \geq \log^{2+\epsilon} N$, matching the performance of the best known non-oblivious search trees in this parameter region. Notably, this means that for search trees, we can get obliviousness for free! The assumptions on $B$ required to achieve optimality are standard and mild. They not only coincide with the standard wide cache-line assumption prevalent in the classical algorithms literature, but also align well with the hardware-enclave architectures that employ oblivious algorithms in practice, such as the implementations of Signal and Meta.

  匹配依据：TEE: hardware enclave

  </details>

- **Enabling Extended SGX Enclaves inside Confidential Virtual Machines**
  2026-10-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.12695)
  Pamenas Kariuki, Dong Yiliang, Quoc Do Le, Christof Fetzer

  <details><summary>摘要 / Abstract</summary>

  Confidential Virtual Machines (CVMs), such as AMD SEV-SNP, and process enclaves, such as Intel SGX, provide workload protection against cloud threats. However, they strongly differ in TCB, deployment cost and speed, peer workload protection, resource sharing, fine-grained isolation and attestation, and programming capabilities. Nesting process enclaves within CVMs offers an optimal solution and an opportunity to address long-standing SGX limitations: lack of intra-enclave protection, expensive transitions and exception paths, slow enclave cloning, and a restricted programming model that limits Library Operating Systems (LibOS). This paper introduces TEEVisor, a CVM-resident architecture consisting of a security monitor and a kernel driver that leverages AMD SEV-SNP Virtual Machine Privilege Levels (VMPLs) to build hardware-protected, process-level enclaves inside a guest CVM with two modes: (1) an SGX binary compatibility mode to run unmodified SGX applications; and (2) a novel extended SGX~(eSGX) mode optimizing slow execution paths and offering richer enclave programming capabilities. On commercial AMD EPYC hardware, against native CVM execution, TEEVisor incurs under 5% overhead on compute- and memory-bound workloads, around 12% on I/O-heavy applications, and accelerates enclave cloning to a rate of 93~$μ$s/MB of enclave size, demonstrating that eSGX semantics inside a CVM are practical for production use.

  匹配依据：TEE: amd sev, intel sgx, sgx, sgx enclaves

  </details>

- **Hashing Beats Trees: Practical Oblivious Dictionaries in SGX**
  2026-10-07 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2397)
  Erik-Oliver Blass, Travis Mayberry

  <details><summary>摘要 / Abstract</summary>

  Oblivious RAM (ORAM) is a powerful cryptographic primitive that hides both the contents of outsourced data and the access pattern to the data. However, it offers only a restrictive array-based interface. A principal obstacle to its deployment is building an efficient oblivious dictionary upon it. To build such a dictionary, the state-of-the-art layers an oblivious AVL tree over ORAM, avoids an expensive local position map, but forces every operation to traverse a full root-to-leaf path, costing $\Theta(\log n)$ ORAM accesses. We show this trade-off to be suboptimal, particularly when deployed in a common setup within a trusted execution environment like SGX. There, a small amount of client memory can reduce the position map recursion depth to three levels or less, rendering its overhead relatively small. With low position map cost, probabilistic hash tables prevail as dictionary data structures due to their small, constant number of accesses compared to $\Theta(\log n)$ path traversal of a tree. We implement and analyze oblivious, probabilistic hash tables over Path ORAM, including several different strategies: chaining, power-of-two-choices, stash-less cuckoo, and de-amortized cuckoo hashing. Execution of these algorithms within a secure enclave requires &quot;double obliviousness&quot;, which in turn needs strict concrete maximum cost limits for each access that current literature does not provide. We derive these concrete padding parameters bounding the hash table rebuild probability to $\le 2^{-40}$ via large-scale simulation. In an SGX deployment, our constructions outperform oblivious trees by up to $20\times$ for $\mathsf{lookup}$s and $12\times$ for $\mathsf{insert}$s.

  匹配依据：TEE: secure enclave, sgx, trusted execution environment

  </details>

- **PRA-TLS: Attestation of a Client Application for TEE**
  2026-10-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.06061)
  Reina Sasaki, Yutaka Ishikawa, Atsuko Takefusa, Masato Oguchi

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) are secure foundations for protecting sensitive information and executing computations over confidential data. Processing in an isolated execution environment (enclave) is invoked by an untrusted application in the Rich Execution Environment (REE). Then the enclave returns the execution results to the untrusted application. Even if the enclave has been attested, the boundary between the enclave and the untrusted application poses risks, such as tampering with input arguments or return values and manipulating the order in which the application invokes functions. Therefore, it is necessary to establish the authenticity and integrity of not only the enclave itself but also the application and its execution environment. In this study, we propose an attestation protocol, Portable Remote Attestation TLS (PRA-TLS), for a client application that invokes an enclave. We introduce a daemon that acts as an attester. PRA-TLS uses a trusted Attester Daemon to measure the state of the host environment and application code at runtime, providing these measurements as attestation evidence for verification by a remote Verifier. This mechanism allows the enclave to proceed only when the software environment is in the expected state and the application code is verified as legitimate. We define attack models and security requirements for the proposed protocol and formally evaluate its security using the Tamarin Prover. Furthermore, we implement a prototype of PRA-TLS using Intel SGX and evaluate its performance.

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **Attestable Audit: Property-Based Attestation for Proprietary Workloads without Artifact Disclosure**
  2026-10-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.04480)
  Takuma Imamura

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) prove the integrity of code and data to a remote peer through remote attestation: the TEE issues an attestation report by signing, with a hardware-bound key, its configuration information, including measurements (cryptographic digests) of the code loaded inside it. A verifier appraises the report by matching these measurements against reference values. When the measured artifact is proprietary, however, the verifier cannot derive the reference values itself: it can only confirm that something with a given measurement is running inside the TEE---not that the program behaves as expected---forcing full trust in the reference value provider. We propose an architecture that closes this gap without disclosing the artifact, composing two TEE workloads: attestable build (Hugenroth et al., 2025), which binds a source code digest to a build artifact measurement, and attestable audit (proposed in this paper), which binds the same source code digest to the verdicts of automated audits---fuzzing, static analysis, AI code auditing, formal methods---executed inside a TEE. Both are instances of Confidential Computing Proofs: TEE attestation viewed as a hardware-backed zero-knowledge proof. Chaining the two certificates lets the verifier conclude that the running artifact was built from source code satisfying the audited properties, without disclosing either the source code or the build artifact. A proof-of-concept implementation on Intel SGX with the Gramine Library OS, running the Bandit security analyzer on Python code, demonstrates the practicality of the approach.

  匹配依据：TEE: confidential computing, intel sgx, trusted execution environments

  </details>

- **Extending eBPF observability to Non-standard execution environments**
  2026-09-30 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.39530)
  Pamenas Kariuk, André Martin, Christof Fetzer

  <details><summary>摘要 / Abstract</summary>

  eBPF observability of non-standard execution environments (NEEs) like TEEs or LibOSes is hindered by their unconventional exception-handling and memory-access mechanisms that limit standard Linux tooling. This work introduces two mechanisms that enable eBPF-based observability for NEEs: (1) kernel memory extensions for safely accessing NEE memory from eBPF programs, and (2) a lightweight flexible probe performance measurement unit (LWFP PMU) that provides flexible and generic probing, for NEEs, through the following LWFP: simple (SLWFP), enclave (ELWFP) and extended (ExLWFP) probes. We demonstrate the practicality of these extensions by developing tooling for tracing, stack sampling with Flame Graphs, dynamic instrumentation, timing analysis, and USDT support for Intel SGX enclaves and LibOSes. Performance measurements show that SLWFP probes achieve a latency of 394 ns, outperforming uprobes, which exhibit 25% higher latency, while ELWFP probes incur a latency ~2.8 microseconds, which is practical for enclave observability. The addition of SLWFP introduces negligible overhead to existing uprobe performance. Taken together, this work lays the foundation for closing the long-standing gap between NEE tooling and Linux observability tooling by enabling generic and reusable eBPF tooling for diverse NEE hardware and software architectures.

  匹配依据：TEE: intel sgx, sgx enclaves

  </details>

- **TEE Anchor: Cross-TEE Organizational Endorsement for Mitigating TEE Physical Attacks**
  2026-09-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.35919)
  Ao Sakurai

  <details><summary>摘要 / Abstract</summary>

  In 2025, practical physical-access attacks against TEEs, such as TEE.fail and Battering RAM, were disclosed, posing a serious threat to current TEEs. The more strictly the target machine is guarded, the harder such attacks are to mount. Residing under trusted management has therefore emerged as a new security requirement. Yet existing attestation cannot prove a machine&#x27;s organizational affiliation. This leaves room for an attacker to pass off a physically accessible machine under their control as one operated in a legitimate environment. We propose TEE Anchor, a mechanism that mitigates physical attacks by proving which organization manages a machine. TEE Anchor is a lightweight, X.509-based design that needs no additional root of trust such as a (v)TPM. The organization issues a certificate over the Chip ID, a unique per-CPU identifier, forming its own PKI. A Verifier then proves affiliation by matching the Chip ID in the attestation evidence against that certificate. This outperforms (v)TPM-based prior work in operational cost and deployability, applies across major TEEs without vendor lock-in, and lets any organization assert affiliation independently of TEE vendors. We implemented a prototype and confirmed that all operations, including provisioning and verification, complete within a few milliseconds.

  匹配依据：TEE: tee (context)

  </details>

- **INTCC: A Framework for Interactive Confidential Computing**
  2026-09-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.35552)
  Qingzhe Bing, Kaiyuan Zhang, Yinqian Zhang

  <details><summary>摘要 / Abstract</summary>

  Confidential computing leverages Trusted Execution Environments (TEEs) to ensure the confidentiality and integrity of data in use. However, TEEs rely on remote attestation to guarantee the integrity of their initial memory state. This model is fundamentally at odds with interactive development workflows. In scenarios like LLM fine-tuning and exploratory data analysis, data processors need human-in-the-loop capabilities, including dynamic code injection, intermediate state inspection, and hyperparameter tuning, all of which inherently violate the static, one-time integrity guarantees of traditional remote attestation. To reconcile this tension, we propose the interactive confidential computing paradigm, a system architecture enabling untrusted data processors to execute dynamic, non-deterministic operations within TEEs without compromising data confidentiality. Driven by the insight that inherently unmeasurable human interaction must be excluded from the Trusted Computing Base (TCB), we logically partition the TEE into an interactive controller and a verifiable runtime. To realize this paradigm, we present INTCC, a framework featuring three key mechanisms: (1) a proxy-based dispatch system to preserve the native development experience; (2) a fine-grained information flow control mechanism based on a security lattice to prevent data leakage; and (3) a privacy-preserving verifiable execution mechanism to guarantee the runtime compliance of dynamic workflows. We implement INTCC on AMD SEV-SNP using Confidential Containers and evaluate it across diverse real-world workloads. Our experiments demonstrate that INTCC effectively balances security and interactivity, incurring a practical overhead of less than 5% for LLM fine-tuning and under 17% for data analysis relative to baseline execution.

  匹配依据：TEE: amd sev, confidential computing, trusted execution environments

  </details>

- **Toward provably private learning from federated data**
  2026-09-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.31494)
  Katharine Daly, Yu Xiao, Zachary Garrett, Brett McLarnon, Jianpeng Hou, Arun Ganesh, Yanxiang Zhang, Noriyuki Takahashi, Haicheng Sun, Yuanbo Zhang, Timon Van Overveldt, Daniel Ramage

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) allows devices with private data to collaborate in training a shared model. We present a next-generation FL system based on Trusted Execution Environments (TEEs) that addresses operational challenges associated with earlier systems and provides externally verifiable central Differential Privacy (DP) guarantees for the first time while offering a better privacy-utility tradeoff. In our system, devices upload data encrypted with keys managed by a TEE-hosted Key Management Service (KMS). The uploaded data is cryptographically tied to a policy limiting the set of Python programs that may later process the data in server-side TEEs. External parties may inspect public transparency logs to observe the set of workloads allowed by these policies. Our experimental results show that the new system improves device coverage and favorably shifts privacy-utility curves by enabling collected data to be integrated into the server-side workload at a schedule that optimizes DP guarantees and is unaffected by device availability. Our new system has been productionized, enabling models for the Android Keyboard (Gboard) to be trained faster and achieve better accuracy under smaller, now externally verifiable privacy budgets in comparison to models trained using the prior system.

  匹配依据：TEE: trusted execution environments

  </details>

- **Write-Public Oblivious RAM and Its Applications**
  2026-09-22 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2163)
  Ananya Appan, James Austgen, Kushal Babel, Sourav Das

  <details><summary>摘要 / Abstract</summary>

  Oblivious RAM (ORAM) protocols enable a resource-constrained client to outsource data to an untrusted server, and access this data without revealing what is being accessed. While ORAM protocols are almost optimal, concretely efficient ORAM protocols incur sub-optimal bandwidth overhead and require multiple roundtrips of communication between the client and the server. In this work, we introduce write-public ORAM: a relaxed variant of ORAM that hides what data is being read, but not what data is being updated on the server. We present wpORAM, a write-public ORAM that modifies Path ORAM to achieve a log N-factor improvement in bandwidth and roundtrips over Path ORAM during writes. The asymptotic cost of reads in wpORAM remains the same as Path ORAM, with a slight slowdown in practice. wpORAM, when used with a Trusted Execution Environment (TEE), can implement a dynamic Private Information Retrieval scheme that efficiently updates data stored in a public database. We use wpORAM to implement a private blockchain RPC server that enables blockchain clients to query RPC nodes without revealing their queries to the server operator. Our evaluation shows that, while syncing with the latest blockchain state, our RPC node achieves a 3-4x speedup over Path ORAM. Our RPC node can serve reads with a slowdown of approximately 23% compared to Path ORAM.

  匹配依据：TEE: trusted execution environment

  </details>

- **Verifiable Computation with Trusted Execution Environments and On-Chain Digital Rights Tokens**
  2026-09-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.21728)
  Bingle Stegmann Kruger, Co-Pierre Georg

  <details><summary>摘要 / Abstract</summary>

  We present an architecture that enables data owners to combine private data into data pools using Trusted Execution Environments (TEEs) and manage these pools by issuing narrowly scoped computational rights, encoded as Digital Rights Tokens (DRTs), to third-party data analysts. Each DRT binds specific open-source code to a pool and is issued and redeemed on a distributed ledger. Data analysts can obtain the right to execute open-source code on the combined sealed data inside a TEE and receive the result from this code execution, but not the underlying data. We argue for a control-centric view of privacy in which creators retain ex ante control over how their data is processed. A reference implementation runs WebAssembly (WASM)/Python jobs over sealed datasets and records redemptions on Solana, illustrating the feasibility and limitations of the platform.

  匹配依据：TEE: trusted execution environments

  </details>

- **Towards TEE-Certified DP: Verifiable Differentially Private Training on Legacy GPUs**
  2026-09-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.20532)
  Li Ge, Wenjie Qu, Weitao Feng, Yi Zeng, Jiaheng Zhang, Xiaofeng Wang, Wei Dong

  <details><summary>摘要 / Abstract</summary>

  Wide adoption of machine learning has created growing policy and regulatory demand for protecting sensitive training data, with differential privacy (DP) emerging as a key mechanism. Yet a less-studied problem is how to certify the faithful execution of DP during training: an external verifier should be able to check that a released model was trained with proper DP protection, without accessing the private training data. Existing cryptographic approaches, such as zero-knowledge proofs, provide strong guarantees but often incur prohibitive overhead, in some cases by orders of magnitude. Trusted Execution Environments (TEEs) offer a more efficient alternative, but the multi-GPU TEE support needed for training and fine-tuning large language models remains limited to recent platforms and is absent or inefficient on legacy GPUs. To address this, we propose a practical framework for verifiable DP training using CPU-side TEEs together with untrusted GPUs. Our design addresses a fundamental efficiency-security tension: training entirely inside a CPU TEE is too slow, while unrestricted GPU offloading can allow malicious deviations from DP. We therefore offload expensive gradient computation to GPUs, while using the CPU TEE to efficiently verify the correct enforcement of DP on gradients through probabilistic checking. Our framework detects frequent full deviations from DP with high probability; for the utility-oriented forged-gradient attacks evaluated in this work, sparse deviations provide limited utility benefit and show no measurable additional membership leakage. Experiments further show that our approach nearly achieves a ``free lunch&#x27;&#x27;: it incurs only modest overhead compared with standard GPU-based DP training, while effectively constraining malicious deviations from the claimed DP execution.

  匹配依据：TEE: trusted execution environments

  </details>

- **AUPE: Collaborative byzantine fault-tolerant peer-sampling**
  2026-09-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.18563)
  Augusta Mukam, Joachim Bruneau-Queyreix, Laurent Réveillère

  <details><summary>摘要 / Abstract</summary>

  Peer sampling is a crucial primitive in distributed systems, used to manage overlays and disseminate information in large-scale scenarios such as permissionless blockchain systems. Its purpose is to maintain and regularly update a local and partial snapshot, or view, of the complete system&#x27;s membership. These protocols are often targeted by malicious actors who aim to disrupt higher-level protocols. Typically, an adversary who controls a set of byzantine nodes attempts to manipulate how legitimate nodes perceive the presence of byzantine ones by increasing their representation in the view of honest nodes. While state-of-the-art byzantine-tolerant peer sampling protocols mitigate this bias, their effectiveness decreases significantly as the number of malicious nodes increases. This paper introduces AUPE, the first collaborative Byzantine-tolerant peer sampling protocol that leverages the presence of trusted nodes, such as Intel&#x27;s SGX capable devices, to collaboratively track the spread of identifiers in the system and locally debias the representation of byzantine nodes. Simulations with 10,000 nodes demonstrate that AUPE outperforms state-of-the-art solutions, achieving nearperfect resilience even when faced with an adversary controlling 26% of the nodes. Overall, by including as few as 10% of trusted nodes, AUPE increases the tolerance of BRAHMS by up to 60% while limiting the impact of the adversary&#x27;s attack, even when possessing up to 40% of the nodes.

  匹配依据：TEE: sgx

  </details>

- **Error-Bounded Fixed-Point Design of Super-Sample-Rate IIR Filters for Real-Time Superconducting Qubit Flux Predistortion**
  2026-09-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.16488)
  Matt Huszabianlou, Angelos Ioannou, Nirmalendu Bikash Patra, Anastasiia Butko, Gang Huang, Irfan Siddiqi

  <details><summary>摘要 / Abstract</summary>

  Flux-activated two-qubit gates in superconducting processors require correction of line distortion, which otherwise produces residual detuning, conditional-phase error, and leakage. Prior demonstrations of cryoscope-based distortion calibration have generally used commercial solutions that specify the filter models but not their FPGA implementation. These details matter for custom and open-source systems, where the fixed-point coefficient and datapath formats set how accurately the correction is realized, and the IIR feedback loop in its standard form does not meet timing at the required clock rate. We derive the coefficient formats of the correction filters from a step response error tolerance, using bounds on the quantization-induced displacement of the poles and zeros over the physical parameter range of each distortion, and the accumulator format from the smallest input change that must remain resolvable at the output. The same analysis gives the conditions under which quantization preserves filter stability. We implement the resulting FIR/IIR cascade on the QubiC platform at a fabric clock rate of \SI{500}{MHz}, using a super-sample-rate structure with scattered look-ahead pipelining, which removes the feedback recursion from the critical path without changing the target transfer function. A representative cascade for our \SI{1}{GS/s} flux lines, comprising an integrator, a second-order section, and a 20-tap FIR, consumes 88 DSP slices and adds \SI{162}{ns} of latency. We confirm the hardware implementation by correcting characteristic bias-tee distortion, an intermediate step toward full cryoscope-based calibration.

  匹配依据：TEE: tee (context)

  </details>

- **SpliTEE: Fast and Private LLM Inference by Coupling GPU-Assisted Trusted Execution Environments with Differential Privacy**
  2026-09-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.15039)
  Shashie Dilhara Batan Arachchige, Robin Carpentier, Hassan Jameel Asghar, Dali Kaafar

  <details><summary>摘要 / Abstract</summary>

  User prompts provided to large language models (LLMs) may contain private information. One way to protect them is to execute the LLM inside a trusted execution environment (TEE). However, this results in slow inference times as current TEEs are significantly slower than GPUs for LLM inference. To circumvent this, Tramèr and Boneh (2019) proposed Slalom which splits neural network inference between a TEE and an untrusted GPU. They encrypt inputs to computations outsourced to the GPU. In this paper, we extend this split-inference architecture to LLM inference and instead protect intermediate inputs using differential privacy (DP). We first demonstrate that masking intermediate representations is necessary by showing an 80% accuracy on a prompt-reconstruction attack from these representations. Our main contribution is a global sensitivity analysis of key functions in LLM inference, which bounds the required scale of DP noise. Unlike encryption, DP avoids quantization, allowing the LLM to remain in the floating-point domain. We also derive an upper bound on the floating-point error from masking and subsequent noise cancellation as a function of the privacy parameter epsilon, keeping the same quality of the LLM response. We implement our architecture using the Intel TDX TEE and two LLMs: Llama-3.2-3B and Qwen3-4B. Our split execution is nearly twice as fast as fully TDX-based inference. Moreover, it is at most 43% faster than Slalom while achieving higher accuracy. Finally, we demonstrate that prompt reconstruction, even with knowledge of the DP mechanism, cannot recover more information than is contained in an unrelated prompt.

  匹配依据：TEE: intel tdx, trusted execution environment, trusted execution environments

  </details>

- **MicroHasTEE: Bare-Metal Haskell for Type-Level Peripheral Ownership on Armv8-M**
  2026-09-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.12580)
  Robert Krook

  <details><summary>摘要 / Abstract</summary>

  Arm TrustZone for Armv8-M isolates Secure and Non-secure software, but developers must still coordinate peripheral attribution, interrupt routing, initialization, and gateway interfaces across separately built firmware images. Inconsistent assumptions between these images can compile successfully and emerge only as faults on the target device. We present MicroHasTEE, a multiparty programming framework that expresses both firmware applications as participants in one typed Haskell program. MicroHasTEE represents peripheral authority with type-level capability ledgers and uses indexed setup computations to track resource acquisition, configuration, transfer, and finalization. Domain-specific effect types restrict peripheral operations and interrupt callbacks to the participant that holds the corresponding authority, while typed callable handles describe the Secure services available to Non-secure code. MicroHs compiles the shared program twice to produce separate bare-metal Secure and Non-secure firmware images. We implement MicroHasTEE for an STM32U5 Nucleo board, including TrustZone configuration, peripheral drivers, and a serialized gateway for cross-domain Haskell calls. For programs expressed through its interface, MicroHasTEE rejects inconsistent resource use, attribution changes after configuration, callbacks in the wrong domain, and calls to unregistered Secure services. A door-lock case study demonstrates feasibility, with firmware images occupying 232.7 KiB and 228.4 KiB of flash and approximately 220 KiB of SRAM per domain.

  匹配依据：TEE: trustzone

  </details>

- **"They don't care about this": A Systematic Study of TEE Build Reproducibility in the Wild**
  2026-09-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.11411)
  Annika Wilde, Marco Gutfleisch, Felix Reichmann, Anirban Chakraborty, Yuval Yarom, M. Angela Sasse, Ghassan Karame

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) have become a cornerstone of modern cloud computing, providing strong confidentiality and integrity guarantees for both code and data. A critical component of this trust model is remote attestation, which enables external entities to verify the authenticity and integrity of code executing within a TEE through cryptographic measurements. However, the effectiveness of remote attestation fundamentally depends on the verifier&#x27;s ability to trace the reported measurement back to the original source code - a property that can only be guaranteed through reproducible builds. In this paper, we investigate the reproducibility of TEE builds through a technical analysis of 115 TEE deployments. Our analysis spans popular TEEs such as Intel SGX, Intel TDX, and AMD SEV, and reveals that a striking 91% of those deployments were not reproducible, with 80% failing to provide both source code and a reference build, the two essential prerequisites for reproducibility. To explore the root causes, we contacted the maintainers of 50 SGX projects and managed to recruit 12 developers from industry and academia for interviews. Only one of our participants reported that reproducibility is a priority during development, effectively confirming our technical findings. Beyond technical barriers (e.g., timestamps included in the binary) that can be readily addressed, we identify broader ecosystem-level challenges, such as the lack of control over the build environment in projects involving multiple stakeholders. We argue that achieving reproducibility in TEEs requires a holistic development approach that extends beyond individual developers and calls for stronger commitments - rather than treating TEEs as a &quot;security badge&quot;.

  匹配依据：TEE: amd sev, intel sgx, intel tdx, sgx, trusted execution environments

  </details>

- **Understanding the Security Boundary of Obfuscation-based On-Device LLM Protection**
  2026-09-09 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.10117)
  Hanyi Zhou, Chenyang Li, Yuanzhe Pang, Ke Xu, Mingwei Xu, Zhuotao Liu

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) offer a promising mechanism for safeguarding the intellectual property of on-device Large Language Models (LLMs). To overcome the inherent computational bottlenecks of TEEs, existing TEE-Shielded LLM Partition (TSLP) methods apply efficient obfuscation schemes to computationally intensive layers, offloading them to external GPUs while retaining only lightweight operations within the TEE. Although a growing body of TSLP-based approaches has emerged, these defense mechanisms remain largely heuristic. Consequently, some methods are proven vulnerable to certain specialized adversarial attacks designed to exploit their specific architectural implementations. To overcome the limitations of these heuristic designs, this paper addresses a fundamental research question: can we establish common primitives to unify representative prior methodologies, characterize the security boundary of their compositions, and systematically extend them? To this end, we formalize a set of obfuscation primitives, defined as dual-tuples of linear computations satisfying specific algebraic properties. We demonstrate that the matrix-level weight transformations of several representative efficient TSLP frameworks can be expressed as compositions of these primitives; consequently, the canonical form of these primitive compositions, denoted as \priorboundary, defines the security boundary of this primitive family. We then expose the vulnerabilities of \priorboundary through a novel primitive-guided attack methodology, \sysattack, demonstrating a shared vulnerability in several prominent TSLP methods published in top-tier venues, such as ArrowCloak (Security&#x27;25), TSQP (S\&amp;P&#x27;25), and LoRO (NeurIPS&#x27;25). Finally, we introduce two novel obfuscation primitives and integrate them with existing constructs to formulate \sysdefense, extending the prior security boundary \priorboundary.

  匹配依据：TEE: trusted execution environments

  </details>

- **Session Attestation for Unmodified TLS Services in Confidential Virtual Machines**
  2026-09-09 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.09668)
  Qi Gu, Wenmao Liu, Weijing You, Yifei Chen, Sheng Ma, Fozhong Chen

  <details><summary>摘要 / Abstract</summary>

  Confidential cloud services aim to protect sensitive requests from the infrastructure that executes them. However, running a service inside a trusted execution environment does not ensure that users&#x27; plaintext appears only within the protected environment. We formulate Endpoint-Substitution Relay (ESR), a common attack outcome in which an adversary receives plaintext at a client-accepted endpoint while relaying requests to the legitimate service to preserve correct behavior. We present TLSLatch, a transparent session-attestation mechanism for services running in confidential virtual machines. TLSLatch attests the protected origin of the server&#x27;s ephemeral TLS 1.3 key share and gates outbound traffic until verification succeeds. It requires no changes to applications, TLS libraries, certificates, or application protocols, and adds no extra payload-encryption layer. We implement TLSLatch with a hardware-backed Hygon CSV CVM server and clients on Linux, Windows, and macOS. Across these platforms, TLSLatch reduces completion time for 1KB requests by 56.9%--65.5% compared with nested TNG, and for 64MB requests by 43.8%--82.4% compared with CMaaS using application-key reuse. These results show that transparent session attestation can preserve existing TLS stacks while adding low-overhead endpoint binding to confidential cloud services.

  匹配依据：TEE: trusted execution environment

  </details>

- **HermiCache: Enclave-Aware Cache Replacement for Trusted Execution Environments**
  2026-09-09 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.10634)
  Oussama Elmnaouri, Pascal Cotret, Vianney Lapôtre, Loïc Lagadec

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) protect enclave memory from untrusted software but remain vulnerable to cache-based side-channel attacks due to shared microarchitectural resources. Existing countermeasures use techniques such as cache partitioning or randomization: these solutions are not ideal if a designer wants fine-grained configurations and a deterministic protection. In this paper, we introduce HermiCache which is an answer to these requirements. HermiCache is designed for RISC-V cores and has been implemented in the OpenHwGroup CVA6 core with a Keystone TEE for the software layer. The solution has an area overhead of 6% on the processor core.

  匹配依据：TEE: trusted execution environments

  </details>

- **Breaking Fault Lines: Unifying TEE-Assisted BFT Consensus in Partially Trusted Worlds**
  2026-09-09 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.09742)
  Xiaoqing Wen, Tong Liu, Jianyu Niu, Jialin Li, Cong Wang, Yinqian Zhang, Chen Feng

  <details><summary>摘要 / Abstract</summary>

  This paper revisits TEE-assisted BFT under a universal partial-TEE model, where an arbitrary subset of replicas execute inside TEEs while the remaining replicas operate without hardware trust guarantees. We show that heterogeneous trust changes the structure of quorum formation and fault tolerance. In particular, we derive a tight resilience bound f &lt; max {n/3, m/2}, where n is the total number of replicas and m is the number of TEE-enabled replicas. The result reveals a sharp threshold phenomenon: TEEs improve fault tolerance only once they exceed two-thirds of the deployment. Guided by this characterization, we introduce two protocol principles: (1) a dual-quorum construction that safely combines TEE-only and mixed quorums, and (2) a TEE-leader fast path that leverages hardware-enforced non-equivocation to reduce both consensus and view-change latency. We realize these ideas in Raftel, which is, to our knowledge, the first HotStuff-style BFT protocol designed explicitly for arbitrary partial-TEE deployments, and in chained-Raftel, a pipelined variant that further accelerates mixed-trust execution. We implement both protocols atop Intel SGX and evaluate them in LAN and WAN environments. Our results show that Raftel achieves up to 625 TPS with sub-670 ms latency in WAN settings, outperforming HotStuff by up to 308 TPS in throughput while approaching the performance of fully TEE-assisted protocols.

  匹配依据：TEE: intel sgx

  </details>

- **NACRE: Rethinking Confidential Containers through Native Architectural Support**
  2026-09-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.03849)
  Linke Song, Wenhao Wang, Weijie Liu, Rui Hou

  <details><summary>摘要 / Abstract</summary>

  Linux containers achieve high density and fast lifecycle operations by sharing the host kernel, but this design also lets a compromised host inspect or modify container state. Existing confidential-computing systems protect an enclave address space or an entire guest operating system, while recent container-granularity systems still add a separate protection context. These abstractions do not make a dynamic group of host-managed Linux processes the architectural protection unit. This paper presents NACRE, a RISC-V hardware-software co-design for native confidential containers. Its key insight is to separate the host&#x27;s authority to manage resources from its authority to access or commit protected state. Hardware-recognized container identities direct protected traps to an isolated S-mode agent, while an M-mode monitor commits security- sensitive identity, mapping, and page transitions. The agent delegates services to host Linux without changing satp; services that neither access private bytes nor modify protected state also avoid M-mode. We prototype NACRE by extending QEMU, OpenSBI, Linux, a trusted agent, and runc. The prototype implements the single-container private-memory substrate and covered launch, fault, fork/COW, user-access, and teardown paths. Across five lmbench syscall and pipe metrics, the three-run means remain within 3.5% of the runc-origin baseline. With the eight nginx object-size means weighted equally, aggregate throughput is 1.9% lower.

  匹配依据：TEE: confidential computing

  </details>

- **Type-Directed, Secure-by-Construction Enclave Partitioning for LLVM**
  2026-09-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.02048)
  Wesley B. Nuzzo, Samuel Dodson, Benjamin Houle, Tarakaram Gollamudi, Anitha Gollamudi

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) provide hardware-supported isolation through enclaves that protect code and data independently of software abstractions. However, TEEs alone cannot enforce information-flow security. This problem is further aggravated in LLVM-like low-level languages that allow unrestricted pointer manipulation and unstructured control flow. Moreover, using TEEs effectively typically requires manually partitioning applications into enclave and non-enclave components, a process that is labor-intensive, error-prone, and lacks fine-grained control. We address these challenges with a three-step approach. First, we formalize SIR, an enclave-oblivious calculus based on LLVM IR, equipped with a novel permissive type system that enforces security against low-level attackers. To obtain meaningful guarantees, SIR combines information-flow control with security-aware coarse-grained memory safety. Second, we extend SIR to SIREN, an enclave-aware calculus that enforces noninterference against stronger attackers capable of observing arbitrary non-enclave memory. Third, we develop a type-driven, type-preserving compilation from SIR to SIREN that automatically produces secure enclave-aware programs, eliminating manual partitioning while providing fine-grained control over host-enclave boundaries. We implement and evaluate SPLITR on thirteen microbenchmarks and real-world workloads, including applications from SGXGauge, on Intel SGX hardware. SPLITR scales to OpenSSL (425,953 LLVM IR instructions) and supports multiple objectives that expose trade-offs among enclave TCB size, host-enclave transitions, and boundary data movement. For OpenSSL, optimizing for transitions reduces them from 393 to 187. Runtime overhead is dominated by fixed enclave costs for short-running workloads, whereas long-running applications better amortize these costs and approach native performance.

  匹配依据：TEE: intel sgx, secure enclave, trusted execution environments

  </details>

- **Private Computation Space: Experience with Trusted Multi-Cluster Federated Learning for Agriculture**
  2026-09-01 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.01667)
  Shuangyu Lei, Muhammad Salman Abid, Jacob Belding, Sam Mosher, Manushi B. Trivedi, Shivranjani Baruah, Liam Wickes-Do, Andrew Anderson, Braulio Dumba, Alyssa Whitcraft, Ritvik Sahajpal, Sijin Li, Kelly Robbins, Michael Gore, Margaret Frank, Steven Wolf, Liz Jones, Abraham Stroock, Kaitlin Gold, Hakim Weatherspoon

  <details><summary>摘要 / Abstract</summary>

  Artificial Intelligence has shown to help improve agricultural practices, yet adoption remains limited: 69% of U.S. farmers have privacy concerns with sharing their data, and these concerns must be addressed before adoption is widespread. While Federated Learning has been demonstrated to protect privacy at scale for other sectors, deploying a system for agriculture comes with its own set of challenges; the problem necessitates a system that can protect farmer data and identities while preserving model utility, runs on commodity hardware, and is resilient to fragile rural infrastructure. To address these concerns, we introduce the Private Computation Space (PCS), a deployed, open-source Machine Learning system to provision and process farmer data securely. We design a system tailored to an agricultural setting, with multi-cluster orchestration for reliability in rural areas with asynchronous Federated Learning (FL), Differential Privacy (DP), and Trusted Execution Environments (TEEs), to allow farms to participate in the framework while keeping their data private. We evaluate the system on two deployed workloads: monitoring nitrogen with living plant sensors in NY for six months and predicting evapotranspiration from weather stations in CA for ten months. Our evaluation finds a Dice Similarity Coefficient (DSC) of 0.71 and $R^2$ accuracy of 0.84 for the respective workloads, improving the worst single-site model accuracy by 22.4% and 9.1%, respectively, while preserving privacy.

  匹配依据：TEE: trusted execution environments

  </details>

- **Zero-Knowledge Predicate Proofs Between AI Agents: A Measured, Cross-Protocol Gateway and the Source-Integrity Gap**
  2026-08-30 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.30083)
  Ashok Subbabhatta Gopalakrishna

  <details><summary>摘要 / Abstract</summary>

  Multi-agent AI platforms move quickly from staging to production, but the way agents establish trust remains rudimentary: an agent either transmits raw data to a peer or accepts that peer&#x27;s natural-language self-report that a value complies with policy. The first over-shares; the second is unverifiable and is exactly the channel prompt injection attacks. Prevailing responses emphasise identity, visibility, and post-hoc detection, and recent proposals for cryptographically enforced agent policy have been evaluated in simulation rather than execution. We take provable data minimisation between agents from proposal to running system. In our Zero-Knowledge Proof Gateway, agents exchange proofs of governance-defined predicates over private data rather than the data itself, so exposure is prevented by design rather than detected afterwards; because no interoperability protocol can carry such a proof, we propose a slot and implement it on both MCP and Agent2Agent from one endpoint. A 32-bit threshold predicate proves in 6.2 ms and verifies in 1.0 ms with a 608-byte Bulletproofs proof on one commodity vCPU; eleven adversarial experiments and nineteen protocol checks pass; and the system is deployed to Kubernetes with empirically verified network isolation. Our case study proves a retail client order is within its limit without revealing the amount, instantiating the GDPR data-minimisation principle as an enforced technical measure of the kind EU law now names explicitly. We then address the limitation no comparable work resolves: a predicate proof binds a statement to a committed value, never to the system of record. We give a construction fusing an enclave attestation with the proof in both directions, so verifying one artifact certifies jointly that the predicate holds and that the value was read by a specific measured binary, and test it against a mock authority.

  匹配依据：TEE: enclave (context)

  </details>

- **Building the Truman Show: A TrustZone-Based Framework for Lightweight Out-of-band Kernel Security Monitoring**
  2026-08-30 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.29758)
  Zhenling Duan, Pan Dong, Renshuang Jiang, Xiaoxiang Fang, Bao Li

  <details><summary>摘要 / Abstract</summary>

  The increasing number of vulnerabilities in operating systems, together with sophisticated kernel-level threats (e.g., rootkits), has weakened the effectiveness of traditional in-kernel protection mechanisms. Since these defenses operate at the same privilege level as the kernel, they share the same attack surface and can be bypassed once the kernel is compromised. Isolation-based security approaches provide stronger protection by separating security logic from the kernel, but strict isolation often introduces semantic gaps that limit system visibility and hinder timely threat detection. In this paper, we present LOOM, a lightweight out-of-band operating system monitoring architecture built on ARM TrustZone. By leveraging TrustZone&#x27;s hardware-enforced isolation, LOOM establishes a tamper-resistant monitoring environment independent of the kernel. To bridge the semantic gap, we design a lightweight semantic reconstruction mechanism in the Secure World. It selectively captures the states and behavioral patterns of critical kernel objects, such as process control blocks and kernel modules. Additionally, LOOM introduces a dual-stage hazard prevention mechanism that combines atomic memory protection with an interrupt-driven adaptive agent to detect and mitigate kernel rootkit activities. An address translation cache is further incorporated to optimize repeated address access and reduce monitoring overhead. Overall, we develop a multi-layered collaborative architecture with platform, functional, and auxiliary layers for secure and efficient kernel monitoring. A prototype of LOOM has been implemented on the Phytium D2000 platform. Experimental results indicate that LOOM incurs negligible overhead while maintaining a strong monitoring capability. Furthermore, a security capability analysis based on CVE cases demonstrates that LOOM can detect and mitigate various kernel attacks.

  匹配依据：TEE: trustzone

  </details>

- **ANCHOR: A Vision for Secure Persistent Key-Value Stores in Disaggregated Data Centers**
  2026-08-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.27819)
  Viraj Thakkar, Dongha Kim, Hokeun Kim, Zhichao Cao

  <details><summary>摘要 / Abstract</summary>

  Persistent key-value stores (PKVS) are increasingly deployed in disaggregated settings that split compute, memory, and storage across separate server pools. This shift redraws the trust boundary: data that would remain within a single machine is now transported, cached, and rewritten across multiple hosts, expanding exposure to both network attackers and intra-infrastructure adversaries. This paper presents ANCHOR, a vision for end-to-end integrity and freshness in disaggregated PKVS. ANCHOR proposes a two-part semantics-aware architecture: 1) Persistence path: ANCHOR outlines encrypting and authenticating PKVS persistent files and preventing rollback with manifest versioning. 2) Volatile path: ANCHOR treats caches, indexes, and filters as untrusted hints unless accompanied by verifiable provenance, enforced by a TEE-resident policy. Finally, we outline key invariants and discuss enclave-friendly batching and asynchronous I/O to amortize verification without undermining disaggregation&#x27;s performance and elasticity benefits.

  匹配依据：TEE: tee (context)

  </details>

- **Beyond Vector Hiding: Breaking and Mitigating Shared-Direction Weight Obfuscation in TEE-Offloaded Large Language Models**
  2026-08-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.26651)
  Menghui Zhang, Aoying Zheng, Guoxiao Liu, Zizhuang Deng, Jiejing Wen, Jincheng Zhuang, Ran Tao

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environment (TEE)-shielded partitioning of Large Language Models (LLMs) accelerates on-device inference by offloading obfuscated linear layers to an untrusted accelerator while retaining only a small correction inside the TEE. However, earlier lightweight obfuscation schemes preserved weight-vector directions and were broken by ArrowMatch. To defend against this attack, ArrowCloak injects scalar multiples of the same hidden direction into all weight vectors, enabling lightweight trusted correction. We show that this reuse leaves a rank-one relation across the complete accelerator-visible matrix. For the released real-valued scheme, we propose SpectralLeak, which estimates and removes the shared component. Across 12 task settings, its surrogates achieve $87.98\%$ mean accuracy versus $89.85\%$ for the victims. In our defense-favorable mod-$Q$ realization of ArrowCloak&#x27;s published modular security formulation, mod-$Q$ arithmetic suppresses this spectral signal but retains the algebraic rank-one relation modulo $Q$. We therefore propose LatticeLeak, which exploits the resulting hidden lattice. In our BERT-Base and GPT2-Base experiments, it reconstructs every protected fixed-point parameter exactly; across all evaluated architectures, the reconstructed models retain victim-level task accuracy without victim queries, labels, or fine-tuning. These findings identify shared rank-one reuse as the root cause of the leakage exploited by our attacks. Guided by this insight, we design ButterflyCloak, a keyed maximal-rank butterfly mask that replaces the reused direction with distinct mask rows while retaining fast trusted correction...

  匹配依据：TEE: trusted execution environment

  </details>

- **Benchmarking Confidential Computing Performance on NVIDIA Blackwell GPUs**
  2026-08-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.26575)
  Amean Asad, Ansgar Grunseid

  <details><summary>摘要 / Abstract</summary>

  This paper measures the performance impact of running large language model inference and training inside a Trusted Execution Environment (TEE) on NVIDIA B200 GPUs, using Intel Trust Domain Extensions (TDX) confidential VMs together with NVIDIA Confidential Computing (CC) on Blackwell GPUs. The performance impact is derived from paired confidential versus non-confidential runs on a single physical host where the only variable is the GPU CC bit and the TDX guest object in the VM launch. The main result is that confidential inference on Blackwell achieves low single-digit throughput overhead when the stack is configured correctly, at about 1-3%. Stock inference stacks incur 30 to 40% penalties due to avoidable configurations rather than the achievable operating point. The cost is not fully represented by a single number because it is governed by two independent axes, a fixed per-host-operation cost that amortizes as batch size grows and a per-NVLink-traffic cost that tracks the share of the step spent in encrypted collectives, and which of the two dominates is set by the workload and the software. We localize each cost to a specific encrypted boundary, give a microbenchmark that predicts the serving penalty to within a submission count, and end with concrete deployment guidance. GPU compute, energy draw, and usable memory capacity are unaffected by CC.

  匹配依据：TEE: confidential computing, trust domain extensions, trusted execution environment

  </details>

- **PRISM: Lightweight Enclave Isolation with Prismatic Capabilities**
  2026-08-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.26367)
  Merve Gülmez, Adam Caulfield, Hakan Englund, N. Asokan, Thomas Nyman

  <details><summary>摘要 / Abstract</summary>

  Trusted execution environments (TEEs) protect sensitive code and data from external interference, but lack inherent memory safety. CHERI can enforce spatial memory safety at the object level. Attempts to establish a TEE using CHERI primitives suffer from (1) expensive capability revocation operations, (2) need to rely on the host operating system (OS) to support provenance tracking and physical memory protection, (3) expensive domain transitions, and (4) lack of support for remote attestation. We introduce prismatic capabilities and present PRISM, a TEE architecture for CHERI leveraging prismatic capabilities to create userspace enclaves while addressing these challenges. PRISM binds enclave &#x27;hues&#x27; (identifiers) in prismatic capabilities to physical memory access controls, enables O(1) ownership establishment without memory sweeps, and supports efficient domain transitions that atomically activate and deactivate prismatic capabilities. Additionally, PRISM enables remote attestation of its enclaves. We demonstrate that execution of userspace enclaves in PRISM incurs only moderate overhead (&lt;= 15%), a significant improvement over the same workloads under Intel SGX

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **Here is a GIFT: Enforcing User Data Isolation in LLM Serving via GPU Information Flow Tracking**
  2026-08-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.25431)
  Jiacheng Shi, Xunjie Wang, Cheng Tan, Jinyu Gu

  <details><summary>摘要 / Abstract</summary>

  LLM serving frameworks process large volumes of user data--often containing sensitive information--on shared infrastructure. Ensuring isolation between users who share the same serving framework (on CPUs) and LLM operators (on GPUs) is critical for privacy protection. This paper presents GIFT, a GPU Information Flow Tracking system that enforces user data isolation in LLM serving with minimal overhead. Moreover, the design of GIFT is non-intrusive and allows CPU-side serving frameworks to evolve freely. It rests on two key insights. First, encryption-as-isolation leverages the observation that CPU components only orchestrate data flow, not content manipulation; thus, per-user encryption can provide isolation without modifying serving logic. Second, GPU kernels exhibit limited and predictable information flows, enabling static flow analysis. GIFT precomputes information flow rules for each kernel and uses decoupled flow tracking, avoiding instrumentation or GPU stalls. Furthermore, we extend GIFT to GIFT-CC, which integrates confidential computing to protect against untrusted operating systems and hypervisors (LLM service providers). Implemented on vLLM and DistServe, GIFT and GIFT-CC enforce user data isolation with a 4-10.7% throughput overhead while maintaining the same latency level.

  匹配依据：TEE: confidential computing

  </details>

- **The Invisible Editorial Layer: Formalizing Undisclosed Inference-Time Steering, Probability Placement, and the Attribution Problem in Deployed Language Models**
  2026-08-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.24662)
  Augusto Camargo

  <details><summary>摘要 / Abstract</summary>

  Evaluations of generative language models frequently interpret observable behavioral traits, such as political stance, brand inclination, and normative framing, as manifestations of model weights, post-training alignment, or prompting. This interpretation risks conflating a foundation model with the multi-layered production system through which its outputs are ultimately served. Modern inference stacks support runtime interventions capable of modifying generation while model parameters remain frozen. We examine inference-time framing bias: systematic runtime steering of generated text toward institutional, ideological, or commercial frames without requiring changes to the underlying model parameters. We formalize the Inference Attribution Problem and establish an observational non-identifiability result showing that, under black-box observation alone, behaviorally equivalent deployed systems may arise from structurally distinct combinations of model parameters and inference policies. Consequently, observed behavioral bias does not uniquely identify the architectural layer responsible for it. We further characterize Probability Placement as a deployment pattern in which undisclosed commercial influence is embedded within an ostensibly organic assistant response through systematic probability-mass reallocation, distinguishing it from explicit token-auction mechanisms for generative advertising. Finally, we discuss implications for behavioral auditing, inference provenance, confidential computing, cryptographic attestation, the EU AI Act, the Digital Services Act, and advertising-disclosure principles. We argue that governance of generative systems must increasingly distinguish between auditing a model and auditing the deployed system that ultimately speaks.

  匹配依据：TEE: confidential computing

  </details>

- **CA-less Mutual Co-Signing of Documents over a Unidirectional Visual Channel with Transported Hardware Attestation**
  2026-08-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.25144)
  Dmytro Diikun

  <details><summary>摘要 / Abstract</summary>

  We describe and analyze a protocol for mutual co-signing of a document by two mobile devices that (i) communicate only over a one-way, lossy, low-bandwidth optical channel (an animated on-screen code read by the counterparty&#x27;s camera), (ii) use no intermediary server on the trust path, and (iii) use no certificate authority. Trust in each party&#x27;s public key is instead grounded in a hardware attestation token produced by the platform secure element, transported in full over the visual channel by a rateless (fountain) code and cryptographically bound into the co-signature. The core technical contribution is a two-stage hash anchor that removes the circular signing dependency inherent to interactive co-signing: the first party commits to the document before the identity of the second party is known, and the second party&#x27;s identity is later bound to that commitment without invalidating the first signature. We give a threat model, define four security properties (anchor binding, co-signature inseparability, attestation-bound key provenance, and post-signing tamper evidence) and reduce them to standard assumptions (collision resistance of H and EUF-CMA security of the underlying signature scheme), with the secure element modeled as an ideal signing oracle. We report a working instantiation on iOS/Android using ECDSA P-256 in the Secure Enclave/StrongBox, SHA-256, Apple App Attest / Play Integrity, and an LT-style fountain code, together with an independent third-party verifier that recomputes all anchors and checks both signatures fully offline.

  匹配依据：TEE: secure enclave

  </details>

- **Beyond Semantic Accuracy: Consequence-Aware Evaluation for Safety-Critical Language Understanding**
  2026-08-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.24621)
  Yujing Chang, Thinh Pham, Van-Phat Thai, Chunyao Ma, Yash Guleria, Pham Nhut Huy, Sameer Alam

  <details><summary>摘要 / Abstract</summary>

  Can language models be trusted in safety- critical operations? In such settings, strong per- formance on semantic metrics does not guaran- tee operational reliability: a misread altitude, a dropped execution condition, or a confused call- sign may score well under standard F1 yet carry sharply asymmetric operational consequences. We study this problem in air traffic control (ATC), where controller-pilot communication demands near-zero error tolerance, and use consequence-aware evaluation to test whether semantic scores misstate operational reliabil- ity. The framework is instantiated in a con- trolled diagnostic ATC benchmark grounded in aviation standards and feedback from 40 air traffic controllers across three countries. Evaluating 8 models, we uncover a system- atic semantic-safety gap: conventional scores give substantially higher performance estimates than consequence-aware evaluation, even for models that appear reliable under standard met- rics. Risk-aware fine-tuning narrows but does not close this gap, showing that consequence- aware evaluation is a necessary complement to standard NLP metrics before any real safety- critical deployment claim

  匹配依据：TEE: tee (context)

  </details>

- **TEE-X: TEE-aware Acceleration Framework for Large Vision Models at the Edge**
  2026-08-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.22716)
  Kurt M Wilson, Mohaiminul Al Nahian, Abeer Matar A. Almalky, Sadat Shahriyar, Souvik Kundu, Zhishan Guo, Abdullah Al Arafat, Adnan Siraj Rakin

  <details><summary>摘要 / Abstract</summary>

  Despite their remarkable success, machine learning models, particularly in vision applications, are alarmingly vulnerable to a range of security threats. One key factor in the attack landscape is the distinction between white-box and black-box threat models, as the latter poses challenges that limit attack effectiveness when access to model information is limited. As a result, using Trusted Execution Environments (TEEs) enhances security for machine learning applications by protecting model confidentiality and execution integrity, effectively shifting the execution environment from the white-box to the black-box side of the threat model spectrum. While adopting TEEs for large vision models, e.g., Vision Transformers (ViTs), is crucial for enhancing security and privacy, significant challenges related to memory constraints and increased computational latency must be addressed, especially in time-sensitive edge applications where safety and privacy are paramount. The objective of this work is to enable large vision models to be fully hosted within TEEs, achieving GPU-level inference latency for time-sensitive edge vision applications while maintaining performance. To this end, we propose TEE-X, a TEE-aware acceleration framework that introduces a sensitivity-aware modularization technique and enables vectorization in TEE inference. This design is validated on OP-TEE for Arm TrustZone, configured to optimize performance on the NVIDIA Jetson AGX Xavier for efficient edge vision applications using ViT models. The findings reveal that TEE-X delivers an effective TEE-aware acceleration framework that achieves minimal accuracy-latency trade-offs while ensuring fast and secure edge inference for vision models.

  匹配依据：TEE: trusted execution environments, trustzone

  </details>

- **HRFPRE: Fast Proxy Re-encryption for Multi-RSU Outsourcing and Hardware-assisted Revocation in the IoV.**
  2026-08-24 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1789)
  Tingting Li, Leyou Zhang, Qing Wu, Fei Zhou, Yuxing Wei

  <details><summary>摘要 / Abstract</summary>

  In the Internet of Vehicles (IoV), content-centric data sharing is essential for driving safety and user experience. However, the highly dynamic and distributed IoV network raises challenges such as unauthorized data access and inefficient information dissemination. Although existing proxy re-encryption (PRE) schemes with revocation partially mitigate these concerns, they still have key shortcomings: (i) computational costs that grow linearly with the number of attributes; (ii) heavy cloud-side overhead from re-encryption and outsourced decryption, causing delays or decryption failures; and (iii) revocation mechanisms that are inefficient or insufficiently responsive in handling malicious users. Recent studies have addressed these issues, but many schemes still struggle to ensure reliable message recovery in dynamic IoV scenarios. To overcome these limitations, we propose HRFPRE, an efficient proxy re-encryption mechanism based on multi-RSU outsourcing and hardware-assisted revocation. Our scheme provides constant-size public parameters and lightweight user-side decryption over asymmetric pairing-friendly groups, while supporting an unbounded attribute space. Re-encryption requires only four pairing operations and supports a novel &quot;encrypt-then-offline hosting&quot; model for vehicles. Simultaneously, Roadside Units (RSUs) provide outsourced re-encryption, key generation assistance, and decryption services to resource-constrained onboard units, effectively shifting computational load away from the cloud. By integrating a key-decoupled Trusted Execution Environment (TEE), HRFPRE enables immediate revocation and keeps plaintext recovery dependent on the user-held key even under TEE-side side-channel leakage. Under the Decisional Linear (DLIN) assumption, HRFPRE achieves adaptive security while resisting replay and collusion attacks. Theoretical analysis and experiments show that HRFPRE reduces computational and communication overhead, making it suitable for secure data exchange in dynamic IoV environments.

  匹配依据：TEE: trusted execution environment

  </details>

- **Hiding Directions, Leaking Structure: Breaking ArrowCloak through Low-Rank Structure**
  2026-08-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.21615)
  Beijie Liu, Junyi Ouyang, Haoxuan Xu, Vincent Quentin Ulitzsch, Potung Yu, Yajie Zhao, Mengyuan Li

  <details><summary>摘要 / Abstract</summary>

  TEE-shielded inference keeps sensitive state in a trusted execution environment (TEE) while offloading linear algebra to an untrusted accelerator. Wang et al., in Game of Arrows (USENIX Security 2025), showed that five widely adopted lightweight defenses preserve vector directions and introduced ArrowMatch to exploit this leakage. They then proposed ArrowCloak, which adds a different multiple of one shared mask direction to each vector and bases its weight-recovery hardness argument on Learning with Errors (LWE). ArrowCloak successfully reduces ArrowMatch to near-black-box levels. In this paper, we revisit ArrowCloak from cryptographic and structural perspectives. Its LWE formulation does not by itself establish standard LWE hardness: the reduction direction, quantized arithmetic, and joint instance distribution do not meet the required conditions. Reusing one mask direction leaves a recoverable rank-one component across the released matrix. We exploit this structure with our proposed attack, an end-to-end, query-free recovery attack. Given a public checkpoint and the obfuscated weights, the attack removes the masking subspace, recovers the hidden one-to-one correspondence, and reconstructs protected weights without transformation secrets, victim queries, or fine-tuning data. Across six model-task pairs spanning classification, segmentation, and diffusion, the attack recovers 99.92%-100% of hidden vector correspondences. Reconstructed classification models achieve 94.39%-99.54% victim agreement and differ by at most 1.59 percentage points in accuracy; the recovered segmentation model achieves 98.35% output agreement. These findings suggest that lightweight protection should address both per-vector geometry and joint structure across released weights.

  匹配依据：TEE: trusted execution environment

  </details>

- **Bootstrapping Mutual Attestation with Kleene's Second Recursion Theorem**
  2026-08-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.20671)
  Takuma Imamura

  <details><summary>摘要 / Abstract</summary>

  Remote attestation is a procedure by which a system (such as a Trusted Execution Environment) proves its own configuration to a remote peer. Here, the configuration includes the measurements (hash digests) of software components. When multiple nodes perform mutual attestation, each node must maintain the reference values for its peers&#x27; measurements. We refer to this as the reference-value bootstrapping problem for mutual attestation. In this paper, we formulate the problem as a fixed-point equation and solve it directly using Kleene&#x27;s second recursion theorem. In our approach, nodes can reconstruct one another&#x27;s source code, thereby allowing each node to derive the reference values at runtime. When a source code itself is deployed, as with a Python script, a node derives the peer&#x27;s reference value directly from its reconstructed source. When a build artifact is deployed, as with AWS Nitro Enclaves, a node instead reproducibly builds the peer&#x27;s artifact from its reconstructed source and derives the reference value from it. As a proof of concept, we develop transpilers in Python and Nix to generate mutually referencing programs. Using these transpilers, we demonstrate the mutual derivation of reference values for the two deployment models mentioned above. Our solution is architecture-independent, requires no trusted third party, and works with existing attestation stacks without modification.

  匹配依据：TEE: trusted execution environment

  </details>

- **Securing Filesystems for Confidential Computing**
  2026-08-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.19924)
  Dimitra Giantsidi, Antoine Delignat-Lavaud, Cédric Fournet, Jinnan Guo, Heidi Howard, Tianjiao Huang, Kapil Vaswani, Stavros Volos

  <details><summary>摘要 / Abstract</summary>

  Confidential computing protects applications inside Trusted Execution Environments (TEEs), but it leaves storage vulnerable. Even with disk encryption, a malicious cloud provider can roll back, replay, fork, or tamper with disk state, breaking the integrity and freshness guarantees required by stateful applications. Existing solutions either assume trusted storage, incur high overheads, or push integrity logic into applications. We present ShieldFS, a POSIX-compliant filesystem that provides end-to-end integrity and freshness for persistent storage in the confidential-computing threat model without requiring application changes. ShieldFS represents permissible filesystem states using succinct cryptographic commitments, maintained inside TEEs and replicated in a lightweight trusted registry. On-disk data structures, including a write-ahead log and a storage pool, are authenticated using hash chains and an embedded Merkle tree. ShieldFS utilizes transactions and copy-on-write to update persistent filesystem state and commitments atomically. The commitments are verified during reads, ensuring that rollback, replay, and equivocation attacks are detected even when the entire I/O stack is untrusted. We implement the design by extending ZFS, yielding ShieldZFS. Evaluation with standard filesystem benchmarks and real-world workloads shows that ShieldZFS provides strong integrity and freshness guarantees with performance comparable to state-of-the-art filesystems.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **A Lifecycle-Oriented Detection and Defense Framework for Price Manipulation Attacks in DeFi**
  2026-08-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.15518)
  Xingyu Xiong, Chang Liu, Xiaoqi Li

  <details><summary>摘要 / Abstract</summary>

  Aiming at frequent oracle price manipulation attacks in Decentralized Finance (DeFi), this paper investigates attack patterns, vulnerability types, risk assessment, automated detection, and defense strategies. Based on Oracle lifecycle theory, a three-layer attack tree covering the physical, protocol, and application layers is constructed to analyze the attack chain and identify the data election stage as a key intrusion point. Four major contract-level vulnerabilities are summarized: insufficient validation of price data flow, oracle call risks, uncontrolled cross-contract calls, and defects in AMM price reading logic. Fuzzy-AHP and Value-at-Risk (VaR) models are combined to quantify risk factors and construct a risk matrix covering technology, market, governance, and contract risks. An automated detection tool based on an extended Slither framework is developed using taint tracking and pattern matching. Finally, a multi-layer defense strategy is proposed, integrating trusted execution environments at the data source layer, TWAP smoothing and adaptive circuit breakers at the smart contract layer, and optimized kernel network configurations at the operating system layer. Experiments show that the proposed approach reduces attack-induced price deviation from 55.56% to below 5%. The detection tool achieves 94.38% accuracy and 92.31% recall, outperforming existing open-source tools.

  匹配依据：TEE: trusted execution environments

  </details>

- **YAVIN: A Unified Architecture for Secure Edge Processing in Memory**
  2026-08-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.13496)
  Shouzhi Fang, William C. Tegge, Md Omar Faruque, Peipei Zhou, Endadul Hoque, Alex K. Jones

  <details><summary>摘要 / Abstract</summary>

  Secure, private multi-tenant execution spanning processors, memory, and accelerators remains one of the most significant challenges in modern edge computing systems. Simultaneously, processing-in-memory (PIM) has emerged as an effective approach for reducing the Von Neumann bottleneck by moving computation closer to data. Existing trusted execution environments (TEEs) establish trust only within the processor, protecting data while it traverses untrusted resources such as the memory bus. Consequently, trusted computation cannot be performed directly within memory. We present YAVIN, a unified trusted computing base (TCB) that extends the TEE beyond the processor to encompass both processor execution and a dedicated memory region supporting trusted processing-in-memory execution while treating the memory bus as untrusted. Leveraging the dedicated protected memory regions already established by conventional TEE architectures, YAVIN enables data to be decrypted, processed, and re-encrypted by either processor or PIM execution while remaining within the TEE. To realize this unified TCB, YAVIN presents the first PIM implementations of the LightSaber KEM post-quantum cryptosystem and ASCON-128 authenticated encryption, co-designing both algorithms for efficient DRAM execution to establish and maintain shared cryptographic state. Finally, we demonstrate how cryptography-PIM co-design for tensor-based workloads reorganizes computation to satisfy the ordering constraints imposed by authenticated encryption with minimal performance overhead while simultaneously enabling bit-sliced ordering that limits temporary plaintext exposure. Compared to the latest PIM AES implementation, YAVIN achieves more than a 20x speedup while incurring only 34% and 9.3% overhead when executing INT8 and INT32 quantized edge-class LLMs, respectively, relative to plaintext execution.

  匹配依据：TEE: trusted execution environments

  </details>

- **RealmEye: Virtual Machine Introspection for Arm CCA Realm VMs**
  2026-08-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.12822)
  Ruofei Qu, Wei Feng, Hongzhan Ma, Menghan Jia, Muyan Shen, Yu Qin

  <details><summary>摘要 / Abstract</summary>

  Confidential VMs (CVMs) have become the dominant substrate for sensitive cloud workloads, from financial services to privacy-preserving AI inference. The hardware isolation that protects these CVMs from a malicious cloud also blinds their owners to what runs inside them: kernel rootkits planted via network or supply-chain attacks can hide processes, tamper with kernel data, and exfiltrate model weights under the cover of the same isolation that defends the VM. Tenants therefore need to inspect a running CVM from outside, yet classical VM introspection (VMI) presupposes a trusted Hypervisor, which CVMs exclude from the TCB. The state-of-the-art CVM-VMI system, 00SEVen, restores introspection on AMD SEV-SNP via an in-VM agent at a privileged tier (VMPL0), a mechanism that does not exist on Arm CCA, leaving Realm VMs without any introspection solution. We present RealmEye, the first VMI system for Arm CCA Realm VMs. RealmEye places the entire introspection logic inside the Realm Management Monitor (RMM) at R-EL2, achieving hardware-enforced separation between the monitor and the monitored VM: no agent runs inside the Realm, and the Realm remains unmodified. RealmEye reads Realm memory and registers, suspends the VM for consistent snapshots, and traps page-level accesses, without relying on any in-VM interface. A periodic, self-driven trigger mode keeps scan timing internal to the RMM, preventing the Hypervisor from colluding with in-Realm rootkits. Results are returned to the remote owner over a hardware-attested channel, and a CCA driver backend lets existing tools such as LibVMI and DRAKVUF interoperate with RealmEye unchanged. On the Arm FVP, RealmEye detects process hiding and syscall-table hooking by Diamorphine, and its in-RMM cost is linearly predictable from primitive invocation counts.

  匹配依据：TEE: amd sev, arm cca

  </details>

- **HIPAA-Compliant AI Deployment Patterns in Clinical Settings: Privacy-Preserving Techniques and Governance Controls**
  2026-08-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.31626)
  Vinod Dhiman

  <details><summary>摘要 / Abstract</summary>

  Artificial intelligence (AI) is moving from research prototypes into clinical workflows, yet the deployment of AI systems that process protected health information (PHI) remains constrained by the U.S. Health Insurance Portability and Accountability Act (HIPAA) and by the absence of shared engineering guidance for satisfying it. Existing work tends to treat privacy-preserving machine learning and regulatory governance as separate concerns, leaving practitioners without a concrete mapping from architectural decisions to compliance obligations. This paper contributes a catalog of five reusable deployment patterns for clinical AI that jointly address the HIPAA Privacy and Security Rules: a de-identified analytics zone, cross-entity federated learning, confidential inference within trusted execution environments, a PHI-minimizing retrieval-augmented clinical assistant, and a synthetic data sandbox for development. Each pattern is specified in terms of context, governing forces, structure, and residual risk, and is mapped to the administrative, physical, and technical safeguards of the HIPAA Security Rule as well as to the NIST AI Risk Management Framework and ISO/IEC~42001. We further present a threat model for clinical AI and a decision procedure for selecting patterns based on data sensitivity, trust boundaries, and latency requirements. The goal is to give security engineers, compliance owners, and clinical informaticists a common vocabulary that turns abstract regulatory duties into verifiable architectural controls.

  匹配依据：TEE: trusted execution environments

  </details>

- **RSS: Robust Signing Service using Threshold Signatures and TEEs**
  2026-08-12 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1670)
  Filip Rezabek, Kilian Glas, Eber Christer, Xinxin Fan, Georg Carle

  <details><summary>摘要 / Abstract</summary>

  Threshold signatures reduce the risk of single-key compromise by distributing signing authority, but each key share remains exposed to compromise of the software and infrastructure that execute the protocol. We present RSS, a threshold signing service that runs share generation and signing inside Trusted Execution Environments (TEEs). We integrate GG20 threshold ECDSA, FROST, and threshold BLS into the EnGINE experimentation framework and evaluate local and Google Cloud deployments using AMD SEV-SNP and Intel TDX. Our experiments separate distributed key generation (DKG), preprocessing, and online signing, and cover up to 40 logical protocol participants distributed across four physical hosts or confidential VMs (CVMs). In matched-platform comparisons, confidential execution adds limited overhead relative to protocol and deployment effects. DKG is the main scaling bottleneck: for 40 participants, it completes within seconds in the evaluated configurations, whereas signing completes in tens of milliseconds. Threshold BLS is approximately twice as slow as FROST for comparable values of $n$ and $t$. These results establish the performance feasibility of executing threshold-signature workloads inside CVMs under benign-operation assumptions. The evaluation does not cover a complete attestation-bound provisioning lifecycle, persistent-state rollback protection, or Byzantine fault behavior.

  匹配依据：TEE: amd sev, intel tdx, trusted execution environments

  </details>

- **A Runtime Decentralized Attestation and Coordinated Repair Framework for Securing Automotive ECUs**
  2026-08-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.11489)
  Josh Dafoe, Niusen Chen, Bo Chen

  <details><summary>摘要 / Abstract</summary>

  The evolution of automotive technology increasingly integrates components, transforming vehicles into interconnected systems of systems. Modern vehicles are controlled by a distributed system of computing devices, known as electronic control units (ECUs). However, this interconnectedness means that any error poses significant risks to the vehicle operator. In particular, malware can be injected into ECUs, threatening vehicle safety. To address this, we need mechanisms to detect compromised ECUs then repair them to a benign state. Existing approaches mainly focus on detection and do not address the challenge of integrating detection with runtime ECU repair. This integration is nontrivial because runtime repair involves both local rollback and reboot with timing determined from global vehicle context to avoid unsafe behavior. In this work, we have designed DACER, a runtime decentralized attestation and coordinated repair framework for automotive ECUs. DACER is the first approach that co-designs attestation and repair to unify the ``local&#x27;&#x27; nature of firmware rollback with the ``global&#x27;&#x27; nature of ECU reboot. In DACER, each ECU performs efficient local self-attestation and self-repair functions, enabling low-overhead coordination for distributed operations. In addition, DACER takes advantage of the hierarchical vehicle computing architecture. Our resulting DACER design checks the entire state of the vehicle, resists single points of failure, conforms to real-time constraints, and enables firmware restoration during runtime. The key functions are enabled by the ARM TrustZone equipped within each ECU and the secure flash memory controller embedded in the storage device. We implemented DACER on real-world hardware and experimentally demonstrated its low overhead.

  匹配依据：TEE: trustzone

  </details>

- **Repeated-Game Security for Restaking-Based Verifiable Inference**
  2026-08-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.09055)
  Zhenhang Shang, Yingzhe Yu, Kani Chen

  <details><summary>摘要 / Abstract</summary>

  Restaking-based protocols enable verifiable LLM inference without the high proving cost of zkML or the hardware trust assumptions of TEEs. Their security is commonly justified by a one-round slashing condition: a rational provider should not cheat when the expected penalty exceeds the cost saving from dishonest inference. This paper shows that this condition can overstate security when inference is supplied repeatedly under the same stake. We model verifiable inference as a discounted repeated game and identify a repeated-game gap caused by proportional slashing: detected deviations reduce future penalty exposure, while cost savings are earned again across queries. We derive the gap in closed form, show that it persists under minimum-stake ejection, and extend it to memoryless bounded-slashing protocols covering deployed designs. We propose a deployable mechanism combining history-dependent challenges, reputation-weighted slashing, and stake vesting. The mechanism restores infinite-horizon subgame-perfect incentive compatibility against stationary mixed-strategy deviations above an explicit discount-factor threshold without per-query cryptographic verification. Evaluation across nine open-weight model pairs from 0.5B to 14B parameters shows that the audit signal has the required concave detectability response. A Stackelberg audit-budget analysis shows that improved signal responsiveness reduces the baseline audit rate by 2.6x at discount factor 0.95. Calibrated to deployed parameters, surveyed protocols pass one-round incentive compatibility but admit repeated-game deviations for discount factors between 0.92 and 0.98, with deviation-profit fractions of 1.5%--8%. Our mechanism reduces deviation profits by 31%--54% while maintaining low-latency economic verification.

  匹配依据：TEE: tees (context)

  </details>

- **Logit-Boundary Geometric Belief Interfaces and Sparse Sheaf-Enclave Protocols: A Self-Contained Substrate for Secure Network Electronic Health Record (EHR) Interoperability**
  2026-08-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.10300)
  Alvin Spivey, Yu Huang

  <details><summary>摘要 / Abstract</summary>

  Electronic health-record interoperability is a boundary problem: legacy systems, generative models, terminology services, identity systems, and human reviewers may each expose rich internal states, while operational exchange requires a narrow shared interface of typed claims, bounded uncertainty, provenance, and explicit admission or abstention. This paper details a mathematical and engineering architecture for that interface. The organizing idea is the logit boundary: a discovery model may propose pre-threshold scores over a local categorical decision, but a deterministic judgment substrate decides whether the proposal is admissible, requires review, or must be quarantined before any Fast Healthcare Interoperability Resources (FHIR) transaction is constructed. The resulting Geometric Belief Interface (GBI) combines finite boundary semantics, local Dirichlet evidence, cellular-sheaf and mapping-cone diagnostics, advisory geometric audit charts, and a Decentralized Cryptographic Sheaf-Enclave (DCSE) protocol sketch for fail-closed deployment. The framework does not establish clinical truth, global representation alignment, or end-to-end safety; it defines certificate-producing checks at a model-to-system boundary. A companion frozen synthetic benchmark, GBI BoundaryBench v0.1, evaluated Qwen3-4B-Instruct-2507 on 256 held-out tasks across three evidence modes (768 canonical executions). All executions completed, but none produced an output accepted by the benchmark contract: 369 were rejected during safe parsing and 399 during schema validation, yielding zero coverage and deterministic quarantine. This empirical result is deliberately narrow - one 4B open-weight model under one frozen interface - and is reported as evidence about the admission boundary, not as a general claim about LLM capability or clinical safety. A Julia appendix verifies numerical certificates using standard libraries.

  匹配依据：TEE: enclave (context)

  </details>

- **From Single Chatbots to Governed Agent Ecosystems: An Agentic AI Pattern Catalogue and Orchestration Framework for Mission-Critical Hospital Information Management Systems**
  2026-08-07 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.07627)
  Manideep Dhar, Ritwik Singh, Sharat Chandra Kumar Manikonda

  <details><summary>摘要 / Abstract</summary>

  Hospitals are racing to embed AI, while coping with the surge in adaptation of the technology in other industries, into the triage management, documentation, scheduling, and revenue-cycle workflows, yet most deployments remain as fragmented pilots that stall at the edge of production, exposing patients and institutions to operational fragility, ungoverned risk, and mounting technical debt. At the same time, the global AI-in-healthcare market is projected to exceed nearly USD 1 trillion by 2034, according to the report of Fortune Business Insights, amplifying the financial consequences of architectural missteps and failed scaling strategies. This research proposes a compliance-first Agentic AI pattern catalogue and orchestration framework, purposely built for HIMS, moving beyond the single LLM chatbots and towards a governed ecosystem of autonomous and semi-autonomous agents. The framework extends by adding (i) a taxonomy of Agentic roles, (ii) a formal risk-stratification model that maps each pattern to risk tiers, human-in-the-loop checkpoints, and governance hooks, and (iii) a unified orchestration runtime capable of coordinating multi-agent workflows across EHR/HIMS landscapes such as Epic, Cerner, and MEDITECH. Technically the framework combines vLLM-based inference, optimized paging memory, confidential computing, and MCP based on-premise deployment, enforcing end-to-end encryption and policy-as-code controls aligned with HIPAA, GDPR, the EU AI Act, India&#x27;s DPDP and DISHA Acts, ISO 27001, ISO 27002, ISO 14971 and IEC 62304. We exhibit how the proposed architecture is capable and efficient to reduce the documentation time, integration effort, and AI pilot attrition while constricting the governance and auditability, offering hospital leaders and governing authorities an urgently needed blueprint to convert AI investment into sustainable clinical, operational, and financial ROI

  匹配依据：TEE: confidential computing

  </details>

- **Counters and Nonces for Mitigating Ciphertext Side Channels**
  2026-08-07 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1632)
  Moritz Peters, Jens Alich, Ashwin Jha, Gregor Leander, Yuval Yarom, Tim Güneysu

  <details><summary>摘要 / Abstract</summary>

  Recent works have highlighted the risk of deterministic memory encryption, as used for example in AMD SEV. In the so-called ciphertext side-channel attack, an adversary leaks sensitive information, such as cryptographic keys, from an encrypted VM by observing changes in the encrypted contents of the memory. To date, countermeasures have been quite restricted in scope and have not addressed the root cause. Alternatively, some studies suggest adding freshness to memory encryption. However, this approach is considered impractical due to the performance overhead introduced by fetching such freshness values for every single memory access. In this work, we propose an efficient approach for eliminating most of the overhead of fetching the aforementioned freshness. Our core idea is to repurpose the ECC memory area to efficiently store random nonces or counters. We propose a range of implementations with varying trade-offs between security guarantees and performance overhead, and demonstrate that we can achieve a solid baseline security even with small random nonces. By leaving a portion of ECC memory unused, we show that it is possible to efficiently integrate protection mechanisms such as memory integrity and memory tagging, while limiting the overall performance overhead to approximately 2%.

  匹配依据：TEE: amd sev

  </details>

- **HarnessOpt-Bench: Evaluating LLMs at Harness Optimization**
  2026-08-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.06301)
  Varun Ursekar, Apaar Shanker, Yash Maurya, Shehab Yasser, Vijay S. Kalmath, Veronica Chatrath, Yuan Xue

  <details><summary>摘要 / Abstract</summary>

  As LLMs are increasingly deployed within agentic systems, their capabilities depend not only on the model weights but also on the harness: the prompts, tools, control flow, memory, and orchestration code surrounding them. This makes automated harness optimization -- the iterative and evaluation-guided improvement of a harness by an AI system -- both an important route to improving AI systems and a demanding capability for AI systems themselves. Yet the community lacks a common protocol for measuring how well frontier LLMs perform at this task. We introduce HarnessOpt-Bench, a benchmark for end-to-end harness optimization under expensive and stochastic evaluation. An optimizer, an LLM paired with a coding harness, receives a target agent&#x27;s seed harness, graded evaluation feedback, and a fixed target-evaluation budget. It edits the harness and nominates a final candidate, which is scored by its normalized gain over the seed on a held-out test partition that remains inaccessible throughout search. A trusted execution environment enforces the evaluation boundary, meters target-agent resource use, and preserves candidate versions for audit. We evaluate 5 frontier LLMs as optimizers both under a shared coding harness and under their native harnesses across 4 downstream tasks, over 111 scored runs. Experiment results show that optimizer models separate more than the coding harnesses they act through, native harnesses are not consistently superior, and gains vary substantially across tasks and seed regimes. These results establish harness optimization as a measurable and discriminative capability with large space for improvement.

  匹配依据：TEE: trusted execution environment

  </details>

- **From Siloed Algorithms to Compliance-First Agentic Platforms: A Multi-Layered Architecture for Hospital AI Systems**
  2026-08-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.06112)
  Manideep Dhar, Ritwik Singh, Sharat Chandra Kumar Manikonda

  <details><summary>摘要 / Abstract</summary>

  Hospitals are rapidly adopting artificial intelligence for triage, imaging, scheduling etc., yet most deployments remain isolated point solutions locked inside departmental silos, resulting in duplicated effort, hidden risks, and unrealized enterprise value. Despite explosive growth of AI in healthcare market and accelerating investment, an estimated 70-80% of healthcare AI pilots fail to scale, largely due to governance gaps, fragmented data, and missing integration blueprints. This research proposes a hospital-specific, compliance-first, Agentic AI architecture with multiple interoperable layers, extending existing hospital AI platform models with: (i) an Agent Orchestration Layer for multi-agent workflows across clinical, operational, and financial domains, (ii) a Compliance and Policy Layer that centralizes policy-as-code for HIPAA, GDPR, the EU AI Act, DISHA Act, India&#x27;s DPDP Act, and ISO/IEC security and safety standards, and (iii) a Privacy-Preserving Data Fabric that plugs federated learning, differential privacy, and secure enclaves into real-world Hospital Information Management System (HIMS) flows. Using a synthetic but structurally realistic hospital dataset and an open, ready-to-deploy prototype implementation, this study demonstrates the end-to-end orchestration of triage risk prediction, workflow optimization, and compliance logging, achieving substantial simulated reductions in task turnaround times and manual documentation effort while maintaining policy-guarded data access. The resulting architecture offers hospital leaders a pragmatic blueprint to move from ad hoc tools to a governed, globally compliant, ROI-focused AI platform that can be tailored to on-premise, hybrid and cloud-native deployments.

  匹配依据：TEE: secure enclaves

  </details>

- **SparSEEty: Extracting Tokens from Sparsity-Exploiting LLM Serving Systems via Deterministic Side Channels**
  2026-08-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.02995)
  Yongwan Jo, Jinyoung Park, Euihyun Lee, Dokyung Song

  <details><summary>摘要 / Abstract</summary>

  Modern large language models (LLMs) exhibit activation sparsity, wherein only a subset of their neurons is activated for given input tokens. Researchers have leveraged this property to optimize LLM serving systems by omitting weight accesses and computations pertaining to inactive neurons. Unfortunately, however, such optimizations create input-dependent weight accesses, which can be leaked over side channels. We present SparSEEty, a new token extraction attack that exploits input-dependent neuron weight accesses introduced by sparsity-exploiting LLM serving systems. SparSEEty first constructs a neuron-activation oracle using neuron weight access side channels during LLM inference, and then inverts the activation traces to reconstruct the input tokens, forming an end-to-end token extraction attack. We instantiate SparSEEty against an LLM serving system protected inside an Intel TDX confidential virtual machine (CVM), addressing three key challenges: (i) constructing a neuron-activation oracle using a combination of side channels exposed by CVMs, (ii) reducing inference-time overheads of neuron activation monitoring for covertness, and (iii) accurately inverting partial binary activation traces back to tokens. Our evaluation shows that SparSEEty can reconstruct both prompt and response tokens with consistently high BLEU scores (&gt;0.95) across various models and datasets, while incurring monitoring overheads of 3.7% to 7.2%.

  匹配依据：TEE: intel tdx

  </details>

- **AMD SEV-SNP: A Confidential Computing Primer**
  2026-08-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.04039)
  Amean Asad, Patrick McClurg, Patrick Woodhead

  <details><summary>摘要 / Abstract</summary>

  This paper is a technical primer on AMD Secure Encrypted Virtualization with Secure Nested Paging (SEV-SNP), a hardware confidential computing implementation that provides Trusted Execution Environments (TEEs) for virtual machines. SEV-SNP treats the hypervisor as adversarial. It encrypts guest memory and register state with keys the hypervisor never possesses, detects any tampering with guest memory at the point of access, and lets a guest prove to a remote verifier exactly what code it is running. The paper constructs each of these guarantees from the hardware up. It opens with the threat model that drives the design and the hardware that enforces it, the AMD Secure Processor and the encryption engine in the memory controller. It then develops the mechanisms that make a confidential guest practical. The Reverse Map Table provides memory integrity against an adversary who controls the page tables. The privilege and communication machinery (VM Privilege Levels, the encrypted VM Save Area, and the GHCB protocol) lets the guest cooperate with a hypervisor it does not trust. The attestation pipeline binds a hardware-signed measurement of the guest&#x27;s initial state to AMD&#x27;s certificate chain, so a remote verifier can confirm independently what is running.

  匹配依据：TEE: amd sev, confidential computing, secure encrypted virtualization, sev snp, trusted execution environments

  </details>

- **Spyre-Accelerated Retrieval-Augmented Generation on IBM LinuxONE: A Cloud-Native Architecture for Secure, High-Throughput Enterprise AI Inference**
  2026-08-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.21393)
  Sandeep Bokkasam, Pankaj D

  <details><summary>摘要 / Abstract</summary>

  Running large language models inside enterprise environments has always bumped up against a practical wall: the data lives in one place, the AI horsepower sits somewhere else, and moving sensitive records between the two creates real headaches around latency, security, and regulatory exposure. IBM&#x27;s Spyre accelerator PCIe inference card built for LinuxONE and the broader IBM Z family changes that equation. In this paper we lay out a six-subsystem RAG architecture that runs entirely on IBM LinuxONE, using Spyre for generative inference, the Telum II on-chip accelerator for lightweight classification tasks, and Red Hat OpenShift for container orchestration. Every piece of the pipeline from query intake through vector retrieval, prompt assembly, LLM inference, compliance filtering, and response delivery stays within a single LinuxONE system, so sensitive data never has to leave the hardware perimeter. We walk through the design choices behind each subsystem, dig into the Spyre compilation and serving stack, explain how LinuxONE&#x27;s Secure Execution technology extends confidential-computing guarantees to AI workloads, and benchmark the architecture against cloud-GPU and on-premises alternatives. Early analysis points to end-to-end RAG latencies under two seconds and up to a 20x reduction compared to off-platform inference, all while keeping the strong encryption and auditability posture that regulated industries actually need.

  匹配依据：TEE: confidential computing

  </details>

- **SONIC: Concurrent Oblivious RAM &amp; Data Structures for Low-Latency and High-Throughput**
  2026-08-02 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1577)
  Nihal Talur, Ioannis Demertzis

  <details><summary>摘要 / Abstract</summary>

  Relying solely on encryption for privacy-preserving computations is prone to leakage-abuse/access-pattern attacks. TEEs, while cost-effective, are also vulnerable to side-channel attacks. Oblivious primitives, such as oblivious memory (ORAM) and data structures (ODS), are effective building blocks to mitigate these risks by concealing memory access patterns and side-channel information. Applications range from private contact discovery (Signal) to anonymous key transparency, encrypted email search, encrypted/oblivious databases, anonymous communication (Sparta/SP&#x27;25), private federated learning, LLM privacy (Compass/OSDI&#x27;25), and broader confidential computing efforts. Tree-based ORAMs (EnigMap (USENIX&#x27;23), GraphOS (PVLDB&#x27;23), Oblix (SP&#x27;18)) offer low latency but limited parallelism. Partition-based solutions like Snoopy (SOSP&#x27;21) shard data across subORAMs (which build oblivious hashtables on incoming requests, then linearly scan them), achieving high throughput by trading off latency, theoretically enabling linear scalability. In practice, Snoopy’s performance hinges on how quickly each subORAM can build the oblivious hashtable and complete its linear scan before exceeding latency targets, constraining server utilization and throughput. While supporting a TB-scale dataset with Snoopy is theoretically feasible, we estimate it would require 1000+ servers. In this work, we reconcile the fractured landscape between low-latency and high-throughput ORAM designs. We introduce SONIC: the first parallel/concurrent doubly-oblivious tree-based ORAM for TEEs. SONIC achieves 156K-3.3M req/s with a single server, tackling the core challenges of all tree-ORAM constructions: overcoming the sequential eviction bottleneck, enabling efficient batch evictions, and providing lock-free access/reshuffle/stash operations. SONIC achieves throughput 29-104$\times$ higher than EnigMap, and 158-560$\times$ higher than GraphOS, with lower latency. In the distributed, high-throughput setting, our SONIC-powered OMAP PMChain can replace Snoopy&#x27;s subORAM, supporting higher throughput and $64\times$ larger datasets using the same hardware (reducing Snoopy&#x27;s server requirements).

  匹配依据：TEE: confidential computing

  </details>

- **Hardware-rooted attestation for AI-agent evidence: composing IETF RATS with action evidence packages**
  2026-08-01 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.00801)
  Anton Sokolov

  <details><summary>摘要 / Abstract</summary>

  An action evidence package (AEP) is a signed, append-only record of what an AI agent did, who or what authorised the action, and what the outcome was. It is a software-layer artefact: it tells a verifier the story of an action as the agent&#x27;s own runtime reports it. This note argues that software attestation of this kind is necessary but not sufficient. When a verifier&#x27;s question shifts from &quot;what does the agent claim it did?&quot; to &quot;did the specific model version the operator claims to have deployed actually produce this output, on unmodified hardware?&quot;, the AEP alone cannot answer. The missing element is a hardware root of trust: an attestation that the measured boot and runtime state of the platform match an endorsed reference. The IETF Remote Attestation Procedures (RATS) architecture (RFC 9334) and Veraison, an open-source RATS Verifier implementation (Confidential Computing Consortium / Linux Foundation), supply exactly this. We propose a composite attestation: hardware Evidence appraised under RATS, bound to a software AEP. We map a small verifier vocabulary (Authorised / Unauthorised / Indeterminate / Attested / Contested / Expired) onto RATS appraisal outcomes, and demonstrate feasibility with a small executed experiment: on a software Trusted Platform Module (TPM; the swtpm emulator), an output-binding protocol folds the hash of an AEP outcome and a fresh appraiser nonce into an attestation-key-signed quote, with a model-artefact measurement carried in a platform register. A minimal RATS-Verifier stand-in resolves the three platform outcomes as designed -- Attested for a good, fresh quote; Contested when the model measurement is swapped; Expired when a stale quote is replayed -- and rejects a forged AEP outcome bound to a valid quote. The result is a feasibility demonstration on emulated hardware, not a hardware-rooted guarantee.

  匹配依据：TEE: confidential computing

  </details>

- **SMARM+: Analyzing and Enhancing Shuffled Measurements for Remote Attestation in Real-Time IoT Settings**
  2026-07-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.23698)
  Amarin Laohajirapan, Norrathep Rattanavipanon

  <details><summary>摘要 / Abstract</summary>

  Remote attestation (RA) is a lightweight security primitive for detecting software compromise on IoT devices. Traditional RA schemes require atomic, non-interruptible memory measurements, making them difficult to deploy alongside real-time workloads. SMARM addresses this limitation by measuring memory in a secret, shuffled block order, reducing the non-interruptibility period to the duration of a single block measurement. However, SMARM was originally designed for microkernel-based systems and has not been studied in RTOS-driven real-time environments. In this work, we present the first systematic study of SMARM in real-time RTOS-based setups. We implement SMARM on commodity ARM TrustZone-M hardware running FreeRTOS and Zephyr, and introduce the Frequency Accuracy Ratio (FAR) to quantify the extent to which attestation can coexist with real-time execution under varying workloads. Our evaluation shows that SMARM&#x27;s real-time compatibility is highly sensitive to block size: large blocks significantly degrade real-time availability, while small blocks incur substantial secure-storage overhead, limiting deployability on memory-constrained devices. To address this limitation, we propose SMARM+, a family of enhanced SMARM variants consisting of SMARM+PRNG and SMARM+FPE. They are designed to reduce secure-storage requirements while preserving SMARM&#x27;s security guarantees and real-time behavior. Our evaluation highlights the trade-off between secure-storage reduction, attestation runtime, and energy overhead, and provides guidance on selecting among SMARM, SMARM+PRNG, and SMARM+FPE for different deployment settings.

  匹配依据：TEE: trustzone

  </details>

- **Decentralized Compute on Untrusted Hardware Using Intel TDX and Encrypted CVMs**
  2026-07-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.21865)
  Venish Patidar, Dhruv Bindra, Ahmed Darwich, Josh Brown, Haidong Xia, Sathi Nair

  <details><summary>摘要 / Abstract</summary>

  The rapid growth of artificial intelligence workloads has generated an unprecedented demand for secure and scalable compute resources. However, centralized cloud providers continue to dominate both pricing and security models. In an increasingly competitive AI landscape, where the compromise of training data or model weights can confer a significant advantage, there is a critical need for a computing infrastructure that safeguards data at rest, in transit, and in use, while remaining affordable and broadly accessible. Furthermore, existing GPU cluster offerings (e.g., 8xH100s, 8xH200s, 8xB200s) create financial barriers that limit access for organizations, startups, and independent researchers seeking secure, high-performance computing environments. This paper introduces a decentralized, confidential computing platform that leverages Intel Trust Domain Extensions (TDX), Intel Trust Authority (ITA) and NVIDIA Confidential Computing (CC) to establish a distributed ecosystem of fully encrypted Confidential Virtual Machines (CVMs). The proposed architecture incentivizes hardware providers to contribute Intel TDX capable compute resources. Each participating provider is provisioned with a freshly instantiated, uniquely encrypted Ubuntu 24.04 CVM, providing data protection across all stages, at rest, in transit, and in use. By decentralizing the confidential computing stack and leveraging confidential computing across independently operated nodes, this work demonstrates a viable alternative to traditional cloud-based infrastructures. The proposed system offers enhanced security assurances, transparent cost structures, and democratized access to enterprise-grade secure compute capabilities, paving the way for a more open, secure, and equitable foundation for next-generation AI development.

  匹配依据：TEE: confidential computing, intel tdx, trust domain extensions

  </details>

- **The Chronos Vulnerability: A Taxonomy of Temporal Persistence and Memory-Based Deception in Agentic AI**
  2026-07-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.19433)
  Om Narayan, Ramkinker Singh, Praveen Baskar

  <details><summary>摘要 / Abstract</summary>

  The transition from stateless generative models in artificial intelligence to stateful, autonomous agents represents an architectural evolution that, while providing the capabilities of long-term planning and the automation of enterprise workflows, also represents the introduction of a new form of security threat, the Chronos Vulnerability. The Chronos Vulnerability represents the threat of memory-based attacks, including the Memory Injection Attack (MINJA) and the sleeper agent, in which the internal belief system of the autonomous agent is compromised, effectively decoupling the attack vector from the final catastrophic event. This study formalizes the threat model for persistence-based attacks and the threat of Dynamics Blindness in the context of the World of Workflows benchmark, demonstrating that traditional endpoint content filters are insufficient for the current stateful architecture. Consequently, this study synthesizes a defense-in-depth landscape, categorizing emerging frameworks such as diagnostic trajectory guardrails (AgentDoG), formal temporal verification (Agent-C), immunological memory consensus (A-MemGuard), and hardware-anchored trust via GPU-based Trusted Execution Environments (TEEs) and Zero-Trust memory architectures.

  匹配依据：TEE: trusted execution environments

  </details>

- **RT-SHCUA: Real-Time Self-Hosted Computer-Use Agent for UAV Control**
  2026-07-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.17951)
  Di Lu, Bo Zhang, Xiyuan Li, Yongzhi Liao, Xuewen Dong, Yulong Shen, Zhiquan Liu, Jianfeng Ma

  <details><summary>摘要 / Abstract</summary>

  Natural-language control offers a promising interface for unmanned aerial vehicles (UAVs), but directly applying self-hosted computer-use agents (SHCUAs) to UAV control introduces a structural mismatch. SHCUAs are designed for interactive host-side tool use, where delayed agent iterations are often acceptable. UAV control, however, is coupled with continuously changing physical states, strict timing constraints, safety risks, and security accountability. A stale, unauthorized, or tampered agent decision may therefore lead to unsafe or untraceable vehicle behavior. This paper proposes a real-time and security-oriented restructuring of SHCUA-based UAV control. Instead of allowing an SHCUA to directly issue flight commands, we transform its outputs into contract-bound UAV skill invocations with explicit timing, state, authority, fallback, and evidence semantics. Based on this abstraction, we design an architecture that separates semantic reasoning from onboard execution and security/safety enforcement. Slow cloud or edge reasoning is used for mission understanding, while onboard components validate and dispatch only timely, authorized, and state-consistent skills. Security-critical enforcement points can be protected by TEE-style or microcontroller isolation mechanisms without moving the full language agent or high-frequency flight-control loop into trusted components. Prototype evaluation shows that RT-SHCUA maintains bounded task-level responsiveness while supporting degraded handling, trusted admission, and auditable evidence preservation for SHCUA-mediated UAV actions.

  匹配依据：TEE: tee (context)

  </details>

- **Vordr: Verifiable, Scalable and Anonymous Remote Attestation for Confidential Virtual Machines**
  2026-07-18 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1472)
  Nirajan Koirala, Kevin Vuong, Micah Brody, Jihye Kim, Hyunok Oh, Taeho Jung

  <details><summary>摘要 / Abstract</summary>

  Confidential virtual machines (CVMs) provide hardware-rooted attestation and isolation, protecting data in use from untrusted cloud infrastructure. However, current CVM attestation frameworks are limited to a two-party trust model between the cloud provider and the CVM owner, and primarily guarantee only the boot-time state. As CVMs increasingly host public-facing workloads (e.g., LLM inference APIs, web applications) that process end-user data, this creates a three-party trust mismatch among the cloud provider, the CVM owner, and end users. Once a workload is deployed, end-users lack cryptographic assurance of runtime integrity and must implicitly trust the CVM owner for any post-launch modifications. Furthermore, extending continuous runtime attestation to a large number of end users introduces severe scalability bottlenecks and is vulnerable to co-location-based attacks. Existing methods either enforce static post-launch lockdown or rely on CVM owner-maintained software logs that are not hardware-anchored. We present Vordr, a framework that removes the CVM owners from the end-user&#x27;s trust domain across the full CVM lifecycle while still allowing workload-level updates/installations with auditability. We introduce a novel architecture that establishes an exclusive administrative binding between a process-based TEE (Warden Enclave (WEN)) and the CVM. This binding strictly blocks the CVM owners (or cloud) from directly manipulating the CVM. Vordr continuously tracks runtime integrity via a hardware-rooted Linux IMA event log anchored to PCR 10, serving time-bounded, platform-unlinkable cached or audit-ready quotes for independent end-user auditing. We optimize the costly IMA-log extraction via a novel incremental attestation design leveraging the IMA log&#x27;s append-only structure and the WEN&#x27;s sealed state. We implement Vordr, validate it across several workloads, and show that it provides up to 60.8x speedup for runtime monitoring with huge communication reductions in steady-state incremental rounds compared to prior methods. Vordr delivers highly scalable and verifiable runtime attestation, providing substantially stronger guarantees for runtime integrity and platform unlinkability.

  匹配依据：TEE: tee (context)

  </details>

- **SABLE: Minimalist Instruction-Level Authenticated Encryption for Constrained Confidential Computing**
  2026-07-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.16771)
  Hamid Noori, Carlton Shepherd

  <details><summary>摘要 / Abstract</summary>

  Conventional processor designs expose code and data as plaintext throughout execution, rendering them inherently vulnerable to attacks that recover intellectual property or modify security/safety checks. Instruction-level encryption (ILE) enables CPU-level decryption, execution, and optionally authentication of individual encrypted program instructions at runtime. However, existing proposals depend on specific micro-architectures, detect corrupted instructions after they have executed, rely on non-standard ciphers, or require complex analyses of program state. In this work, we introduce and present a design exploration of a RISC-V processor architecture (SABLE) that enables minimally invasive instruction-level authenticated encryption of programs. SABLE is agnostic to the underlying micro-architecture, remaining compatible with the standard RISC-V toolchain with minor changes to post-process compiled ELF binaries. We integrate a decrypt-and-verify stage at two points (the instruction-memory wrapper and the CPU frontend) and explore seven ILE micro-architectures from a single-cycle (combinational) design to six multi-cycle (sequential) variants. We implement and evaluate the designs using ASCON-128a on a Xilinx Artix-7 FPGA with the open-source NEORV32 system on chip. Relative to baseline performance, the configurations span LUT, performance, power, and energy-per-instruction overheads of 1.6-9.3$\times$, 4.1-10.0$\times$, 1.5-8.0$\times$, and 10.4-80.0$\times$, respectively, using the Dhrystone benchmarking suite. Finally, we discuss design trade-offs, highlighting area-, performance-, and energy-aware design points.

  匹配依据：TEE: confidential computing

  </details>

- **WaveCommitments: Private and Verifiable Speech-Agent Marketplaces**
  2026-07-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.26867)
  Oguzhan Baser, Kaan Kale, Sriram Vishwanath, Sandeep Chinchali

  <details><summary>摘要 / Abstract</summary>

  Modern speech systems are evolving into ecosystems of autonomous speech agents that interact, negotiate, and trade assets such as embeddings, spectrograms, or raw data. In such markets, sellers cannot reveal assets for evaluation due to privacy constraints, and buyers cannot price what they cannot test. Thus, we introduce WaveCommitments, an end-to-end design that couples multivariate polynomial commitments with confidential asset valuation via Data Shapley inside a trusted execution environment. It enables selective openings and tamper-evident provenance to prove that a delivered asset matches the valuation while hiding everything else. Our extensive experiments across three standard datasets and various tasks with state-of-the-art encoders, including Whisper, reveal that we speed up the strongest baselines by up to 18.1x while reducing their proof sizes by up to 43.2x. We also analyze how a speaker&#x27;s value shifts across tasks and encoders, revealing agent-level market prices.

  匹配依据：TEE: trusted execution environment

  </details>

- **Cross-Core Inference Offload as an Operating-System Service on Dual-Core Microcontrollers**
  2026-07-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.12620) · [Code](https://github.com/Dimitrios-Kafetzis/SynapticOS)
  Dimitrios Kafetzis

  <details><summary>摘要 / Abstract</summary>

  Dual-core MCUs are asymmetric: on NXP&#x27;s MCXN947, the second Cortex-M33 has no FPU, DSP extension, TrustZone, or MPU. We treat the asymmetry as a design input in the Phase 3 dual-core architecture of SynapticOS, an open-source Zephyr-based runtime: the AI runtime (models, NPU/DSP, scheduler) lives on the capable core, and the application core reaches inference only via a message-based OS service -- a remote system call. The transport is a pair of lock-free single-producer/single-consumer rings in shared SRAM: one writer per index, free-running 32-bit counters, ordering by data-memory barriers alone (the platform has no cross-core atomics). Because ring state is shared, a rebooting application core rejoins unaided. Requests carry priority classes, errors and timeouts propagate to the caller, and tensors stage zero-copy in a shared slot -- a 27 KB frame cannot exist twice in 64 KB of RAM. Measured on the FRDM-MCXN947 (both cores 150 MHz): the application core boots in 1,514 us and completes the handshake in 2,554 us, bit-identical over 11 boots; round trips are 15 us typical / 81 us worst-case (50 us budget); pushes cost 25 cycles; a 1,913-serve two-model soak had zero errors (stub-NPU latencies bracket transport, not silicon). An MPU region on the runtime core guards the application core&#x27;s RAM (fault-injection verified); protection is one-directional -- the application core has no MPU, and ARMv8-M cannot block privileged reads. Two hardware-revealed defects are reported: releasing the second core into erased flash wedges the whole chip and its debug port (now prevented by a ROM-API blank check), and a Zephyr flash-driver Kconfig silently disarmed the devicetree MPU guard (now programmed at runtime). Firmware is 98.9 KB flash (runtime core) and 32.4 KB (application core, 42.6 of 64 KB RAM); 108 tests in 13 suites pass 100%. Apache 2.0: https://github.com/Dimitrios-Kafetzis/SynapticOS

  匹配依据：TEE: trustzone

  </details>

- **From PBS to ePBS: the Microstructure of Block Building**
  2026-07-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.11240)
  Jingyu Liu, Bolin Zhang, Lin William Cong, Siguang Li, Xuechao Wang

  <details><summary>摘要 / Abstract</summary>

  Ethereum&#x27;s Glamsterdam upgrade introduces enshrined proposer-builder separation (ePBS), replacing relay-centric PBS with direct builder bids to proposers. We study how this shift changes the block-building microstructure through a general imperfect-information two-stage auction with verifiable messages, where an early bid serves as both a price offer and a signal. PBS and ePBS are modeled as restrictions of the same block-building game: PBS fixes stopping and disclosure exogenously, while ePBS lets the proposer choose stopping and disclosure ex post. Latency heterogeneity is captured by asymmetric information updates: fast builders observe disclosed early information before rebidding, while slow builders do not. We combine exact perfect Bayesian equilibrium characterizations in tractable cases with calibrated no-regret learning in finite games. For PBS, we show that separating equilibria preserve the standard first-price-auction payoff benchmark and provide conditions for their existence. For ePBS, we demonstrate a ratchet effect: because the proposer can defer block proposal and use early bid information in the second stage, builders anticipate ex-post extraction and shade or pool early bids, generating allocation inefficiency and revenue-efficiency valleys. We interpret this ratchet distortion as a commitment failure. Under full commitment, the optimal policy collapses to the static Myerson auction and removes the ratchet channel. To realize part of this commitment advantage in a feasible mechanism, we propose a Trusted Execution Environment (TEE) sidecar that enforces limited commitment. We formulate the revenue-maximizing TEE mechanism as a bilinear optimization problem. In conservative finite benchmarks, the TEE design increases the proposer revenue relative to the first-price benchmark by approximately \(25\%\).

  匹配依据：TEE: trusted execution environment

  </details>

- **NARAD: Non-colluding Aggregator-oblivious Record-And-Decrypt**
  2026-07-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.07596)
  Akshit Vakati Venkata, Rajat Dugar, Ayush Adarsh

  <details><summary>摘要 / Abstract</summary>

  Electronic voting must keep individual ballots private while letting anyone verify the final tally. This paper presents an architecture that meets both goals without a trusted key dealer: each voter encrypts a ballot in the browser with a self-generated secret key under the Paillier additive homomorphic cryptosystem, and no party ever holds every key. Two server roles divide the tally. A collector combines the voters&#x27; per-ballot auxiliary values into a single group element; an aggregator uses that element to cancel the voters&#x27; random masks inside the homomorphic product and recover the exact vote sum, learning the result but no individual ballot. The Solana blockchain records every ciphertext immutably and enforces the election lifecycle, while a native C library (libtommath) performs the heavy modular arithmetic. We state six assumptions under which the protocol is correct and prove product homomorphism, mask cancellation, and sum recovery; privacy rests on the Decisional Composite Residuosity (DCR) assumption for the additive layer together with a Diffie-Hellman-style assumption on the masking base. A bit-packing scheme places an entire multi-candidate ballot in one ciphertext, cutting client work, on-chain transactions, storage, and tally cost by a factor of k (the candidate count); the slot width b is free, with only k*b bounded by log_2(N). With b = 25 and a 255-bit modulus the scheme supports ten candidates and up to 2^25 - 1 = 33,554,431 votes per candidate, about 335 million ballots, and tallies 50,000 ballots in under one second. Finally, running the collector and aggregator inside attested secure enclaves makes the tally tamper-resistant and prevents cross-role collusion to deanonymize voters. The proof-of-concept implementation is open-source; a worked numerical example in the appendix reproduces the full pipeline.

  匹配依据：TEE: secure enclaves

  </details>

- **KS-CFA: Control-Flow Attestation via Symbolic Replay Against Control-Flow Bending Attacks**
  2026-07-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.07926)
  Zhanyu Sha, Konstantinos Markantonakis, Carlton Shepherd, Amir Rafi

  <details><summary>摘要 / Abstract</summary>

  Control-flow attestation (CFA) enables a remote entity to verify program execution on a target device by monitoring control-flow behaviour at runtime. However, control-flow bending (CFB) attacks remain difficult to detect, where an adversary steers execution along legal edges of the program&#x27;s control-flow graph by corrupting branch flags, loop counters, and other runtime data. Existing solutions impose significant drawbacks: they require enumerating vast measurement spaces, cover only a reduced subset of attacks, or rely on low-level hardware modifications. In this work, we present KS-CFA, a new CFA scheme that detects CFB attacks across four transfer types (indirect calls, conditional and indirect jumps, and returns) without those costs. To this end, we combine symbolic execution and selective identification of input-sourced control-flow dependent variables: a strict subset of control-flow-relevant state whose values are directly read from external input. The proving device records, inside a trusted execution environment (TEE), a control-flow trace and the external inputs that determine relevant run-time variables. The verifier then replays the reported path through single-path symbolic execution, predicting each transfer and localising divergences that signal an attack. We implement and evaluate KS-CFA using the RISC-V Keystone TEE and Embench-IoT on QEMU and a Rocket-based FPGA platform (NiteFury II). Prover-side overhead relative to unattested execution ranges from 6.8-20.5x on QEMU and 6.7-32.2x on the FPGA, and verification requires no path or value enumeration.

  匹配依据：TEE: trusted execution environment

  </details>

- **Embedded Blockchain Infrastructure Management (eBIM): A RISC-V-Empowered Hardware--Software Co-Design Framework Towards Trustworthy Blockchain**
  2026-07-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.07625)
  Qinglin Yang, Yuan Liu, Yaoyao Zhang, Boya Wang, Zongjian You, Chunming Rong, Zhihong Tian

  <details><summary>摘要 / Abstract</summary>

  Blockchain systems are undergoing a fundamental transition from decentralized ledgers for digital assets to general-purpose trust infrastructures for verifiable computation, decentralized physical resources, and automated infrastructure management. Meanwhile, the limitations of the Blockchain as a Service (BaaS) model stem from a common structural problem: outsourcing control of infrastructure to third-party service providers inevitably involves a systemic surrender of trust, flexibility, and data sovereignty. RISC-V, with its open, modular, and extensible design, provides a general-purpose computing foundation for public blockchains that is open, low-level, compileable, verifiable, and scalable. Inspired by the development and characteristics of eSIM, the embedded Blockchain infrastructure management (eBIM) is defined as a software-hardware collaborative paradigm for blockchain infrastructure management with RISC-V. This study aims to provide a comprehensive survey on eBIM supporting research and technologies, to answer the following research questions (RQs): RQ1 What is eBIM? RQ2 How does eBIM work? RQ3 What can eBIM do? By introducing the concept of eBIM, this paper establishes a foundational reference for researchers, hardware architects, and protocol designers in this rapidly evolving landscape, including cryptographic acceleration, trusted execution environments, zero-knowledge virtual machines, and smart contract execution engines. The prospects of the proposed e-BIM and its future research directions are indicated in this paper.

  匹配依据：TEE: trusted execution environments

  </details>

- **Data Structures for Private Token Transfers in TEE-Based Networks**
  2026-07-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.04032)
  Blake Regalia, Benjamin Adams

  <details><summary>摘要 / Abstract</summary>

  Trusted execution environment (TEE) based confidential smart contract networks promise privacy but remain vulnerable to storage access pattern attacks that can link senders and recipients in token transfers. When contracts update recipient balances during transfers, the unique storage keys accessed reveal transaction relationships even when data is encrypted. This paper introduces two novel data structures to address this vulnerability: the Delayed Write Buffer (DWB) and the Bitwise-Trie of Bucketed Entries (BTBE). The DWB delays recipient balance updates by buffering pending transfers and randomly settling entries, breaking the direct correlation between transfer execution and recipient storage access. The BTBE further enhances privacy by grouping addresses into constant-sized buckets, preventing flooding attacks and creating anonymity sets for balance queries. Additionally, we present a private notification system enabling real-time, privacy-preserving push notifications for confidential contracts. Our domain-specific approach leverages the unique characteristics of token transfers -- asymmetric balance updates and tolerance for delayed settlement -- to achieve practical performance with probabilistic anonymity guarantees.

  匹配依据：TEE: trusted execution environment

  </details>

- **Know Thy Neighbor: Cross-TEE Mutual Attestation**
  2026-07-01 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.00695)
  Daniel Andrade, João N. Silva, Miguel P. Correia

  <details><summary>摘要 / Abstract</summary>

  Cloud services are composed of multiple heterogeneous distributed components and instances that communicate with one another. This occurs both in applications and services running in traditional execution environments and in trusted applications (TAs) running in trusted execution environments (TEEs). TA instances use attestation before exchanging information to ensure all parties meet the expected security conditions. The straightforward solution to mutually attesting two TA instances that are willing to communicate is employing remote attestation mechanisms in both directions. This is typically the case when the two TA instances are running on TEEs of the same type. In order to support cross-TEE attestation, such an approach, that is, using remote attestation in both directions, would require each TEE type (e.g., SGX, TrustZone) to support the attestation software stack of all other TEE types with which it needs to interact. A dedicated cross-TEE mutual attestation solution has multiple benefits in terms of efficiency and security. This paper presents the Heterogeneous Mutual Attestation (Hema) protocol, a formally-verified protocol for the mutual attestation of TA instances running on the same TEE type or on different TEE types.

  匹配依据：TEE: sgx, trusted execution environments, trustzone

  </details>

- **EnclaveX: End-to-End Confidential AI with CPU/GPU TEEs**
  2026-06-30 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.31408)
  Robert Schambach, Quoc Do Le, Sergei Arnautov, Christof Fetzer

  <details><summary>摘要 / Abstract</summary>

  Large Language Models (LLMs) have rapidly proliferated, driving widespread adoption of AI applications. Most deployments rely on centralized infrastructures such as Microsoft Azure, Google Cloud, or AWS, requiring users to share sensitive data and training or fine-tuning code. This dependence raises significant security and privacy concerns, as cloud providers must be trusted to ensure confidentiality and integrity. Trusted Execution Environments (TEEs) e.g., Intel SGX/TDX, AMD SEV-SNP, and ARM CCA have been introduced to mitigate these risks. More recently, NVIDIA has developed GPU TEEs (e.g., H100/H200), yet comprehensive evaluations of end-to-end workflows that integrate CPU and GPU TEEs remain limited. Critical aspects, including performance overhead, remote attestation, and security guarantees for AI/LLM applications, have not been sufficiently studied. This paper addresses this gap by presenting an end-to-end workflow that combines CPU and GPU TEEs. We propose mechanisms to ensure confidentiality and integrity at both the VM level (via Intel TDX and AMD SEV-SNP) and the application level, highlighting vulnerabilities such as Kubernetes administrators&#x27; ability to access confidential VM contents. Finally, we evaluate the performance overhead of our system using industry benchmarks, focusing on configurations that integrate Intel TDX with NVIDIA H200 GPUs.

  匹配依据：TEE: amd sev, arm cca, intel sgx, intel tdx, trusted execution environments

  </details>

- **Query Cost Model Calibration in Confidential Virtual Machines**
  2026-06-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.26385)
  Qihan Zhang, Mengyuan Li, Ibrahim Sabek

  <details><summary>摘要 / Abstract</summary>

  With the growing adoption of Confidential Computing, running databases in confidential virtual machines (CVMs) such as AMD SEV-SNP has become an attractive way to protect sensitive cloud data with minimal changes to legacy DBMSs. However, analytical queries in such CVMs often suffer substantial overhead, and prior database work has largely stopped at benchmarking these slowdowns rather than optimizing them. We show that this problem stems from a hardware-software mismatch: query optimizers still rely on KVM-oriented (non-encrypted VM) cost assumptions that no longer hold in CVMs. To address this, we propose a lightweight CVM-aware cost calibration. It models two dominant sources of optimizer-facing overhead: data movement and RMP-related translation using simple physical proxies already available to the optimizer. Experiments show that the calibration significantly narrows the KVM/CVM performance gap, recovering up to 48 percent performance and even outperforming the KVM baseline on some workloads.

  匹配依据：TEE: amd sev, confidential computing

  </details>

- **The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing**
  2026-06-22 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.23969)
  Hang Yin, Kevin Wang

  <details><summary>摘要 / Abstract</summary>

  GPU Confidential Computing (GPU-CC) now preserves GPU-local performance: on NVIDIA B300, BF16 matmul runs at 0.998x of non-confidential performance. Yet LLM serving under Intel TDX plus GPU-CC still loses 13-27% of throughput, and KV-cache restore latency can more than double. This paper studies that gap on two Blackwell platforms, RTX Pro 6000 and B300 HGX, and identifies its dominant cause: the confidential VM-GPU bridge, not GPU compute. We find that GPU-CC turns host/device movement into a serialized, high-setup-cost channel. Secure copies do not gain CUDA-stream concurrency within a context, asynchronous transfers block at the runtime boundary, and small crossings pay a fixed toll. This violates the assumptions of modern inference runtimes, where DMA is expected to be cheap, concurrent, and asynchronous. In vLLM dense decode, the gap closes around 44x-slower small alloc-and-copy operations; targeted patches reject alternative explanations. A scheduling flag recovers 57% of the gap, while a worker-thread drain recovers up to 92% in qualified high-concurrency runs. The same bridge model explains a +131% KV-restore penalty and a 34x model-load slowdown. Blackwell also changes the confidential tenancy unit. We qualify confidential multi-GPU NVSwitch tenants on B300, including 510 GB/s NVLink P2P inside a CVM and concurrent isolated tenants, and identify the remaining fabric-attestation gap for production confidential AI platforms.

  匹配依据：TEE: confidential computing, intel tdx

  </details>

- **FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation**
  2026-06-22 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.09046) · [arXiv](https://arxiv.org/abs/2606.23370)
  Yinpeng Wu, Yitong Chen, Lixiang Wang, Jinyu Gu, Zhichao Hua, Yubin Xia

  <details><summary>摘要 / Abstract</summary>

  Device-side Large Language Models (LLMs) have grown explosively, offering stronger privacy and higher availability than their cloud-side counterparts. During LLM inference, both the model weights and the user data are valuable, and attackers may compromise the OS kernel to steal them. ARM TrustZone is the de facto hardware-based isolation technology on mobile devices, used to protect sensitive applications from a compromised OS. However, protecting LLM inference with TrustZone incurs significant overhead to both the secure inference and the normal aplications, due to two challenges: the inflexible resource isolation and the inefficient secure resource management. To address these challenges, this paper presents FlexServe, a fast and secure LLM inference system for mobile devices. The key idea is to decouple the access permission from the management permission of secure resources, so that the normal-world OS cannot access them but can still manage them as usual. First, FlexServe introduces a Recallable Resource Isolation mechanism to construct Recallable Secure Memory (Flex-Mem) and a Recallable Secure NPU (Flex-NPU). They can only be accessed by the secure world, but can be efficiently allocated and reclaimed by the normal-world OS. Based on them, FlexServe further introduces a FlexServe Framework to run secure LLM inference in the secure world. It works together with the normal-world OS to perform cooperative secure memory management. We implement a prototype of FlexServe and compare it with two TrustZone-based strawman designs. The results show that FlexServe achieves average TTFT speedups of 10.05X over the strawman and 2.44X over an optimized strawman.

  匹配依据：TEE: trustzone

  </details>

- **Evidence-Bound Gateway-Path Provenance for Third-Party LLM Inference**
  2026-06-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.22560)
  Fei Wang, Zebai Tian

  <details><summary>摘要 / Abstract</summary>

  Third-party LLM gateways select providers, models, endpoints, and fallback paths while also authoring the records used to explain and bill those decisions. We present evidence-bound gateway-path provenance, which makes these decisions subject to client-verifiable request contracts. An attested mediation runtime intersects a signed service policy with the client&#x27;s authorization, constructs provider-facing calls, and protects streamed responses. The contract distinguishes initial routes from fallback destinations and admits each transition only after an authorized failure. A signed close-out binds the execution trace, provider-reported usage, authorized pricing, and complete response. We formalize the protocol state machine and establish authorization preservation, execution and stream binding, charge integrity, and channel confidentiality relative to the public receipt metadata. The analysis also characterizes replay, runtime replacement, and the information disclosed by public payload commitments. Controlled software-path measurements show 0.442 ms paired p95 latency overhead at concurrency one, peak throughput of 10.65 thousand requests/s, and stream close-out below 0.4 ms p95. An AWS Nitro Enclaves prototype completed 30 live single-route streaming requests with attestation-bound session and signing keys. The design separates gateway administration from payload processing and supplies a verifiable account of each confirmed execution.

  匹配依据：TEE: enclaves (context)

  </details>

- **CloakLM: Obfuscating GPU Memory Layout to Mitigate Model Ex-filtration for Serving**
  2026-06-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.18400)
  Kunal Jain, Seokjin Go, Divya Mahajan

  <details><summary>摘要 / Abstract</summary>

  Large foundation models deployed on third-party and shared accelerator infrastructure face a practical risk of model exfiltration that existing defenses do not fully address. In common serving deployments, model providers control the VM or bare-metal serving stack but not the surrounding hardware substrate. The host to GPU interconnect, accelerator fabric, and neighboring infrastructure components remain outside the tenant&#x27;s trust boundary and have been shown to be exploitable. Hermes demonstrates lossless DNN reconstruction from passive PCIe observation, while TunnelS exfiltrates HBM contents at high throughput via driver-level access without disrupting inference. Co-tenant VMs can further access memory-mapped interfaces or misconfigured RDMA regions without physical co-location. These attacks exploit a common property of ML systems: model weights are stored in large, contiguous, and repeatedly accessed memory regions, making intercepted PCIe transfers and HBM dumps rich enough to reveal model structure and parameters. We present CloakLM, a software-only memory-obfuscation framework that removes this structural regularity without changing the inference stack&#x27;s logical view of memory. CloakLM combines three mechanisms: PCIe traffic shaping, inter- and intra-layer weight shuffling, and physical HBM page remapping. Authorized execution retains a valid virtual memory layout with negligible overhead, while unauthorized observers see fragmented and semantically incoherent state. CloakLM integrates with vLLM and PyTorch, requires no hardware changes, and complements confidential computing. Evaluation on distributed inference workloads using LLaMA and Qwen models shows near-native performance while significantly increasing resistance to PCIe snooping and HBM dump attacks, making inference-time model exfiltration substantially less practical.

  匹配依据：TEE: confidential computing

  </details>

- **Bifrost: Hybrid TEE-FHE Inference for Privacy-Preserving Transformer and LLM Serving**
  2026-06-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.17421)
  Chenghao Chen, Kailun Qin, Xiaolin Zhang, Chi Zhang, Dawu Gu

  <details><summary>摘要 / Abstract</summary>

  Cloud-hosted transformer and large language model (LLM) inference creates a direct confidentiality problem: user prompts may contain sensitive code, business data, personal information, or regulated documents, yet remote serving exposes intermediate state to the cloud software stack and accelerator runtime. Fully homomorphic encryption (FHE) keeps accelerator-side execution ciphertext-only, but end-to-end LLM inference remains expensive because linear layers are interleaved with non-linear, cache-state, and refresh-sensitive operators. CPU trusted execution environments (TEEs) can execute those operators natively, but a CPU TEE alone does not define how an untrusted accelerator should participate. We present Bifrost, a hybrid TEE-FHE serving architecture in which secrets are provisioned only to an attested CPU TEE, while the accelerator, device memory, driver/runtime stack, and host software remain outside the trusted computing base. Bifrost uses FHE as a secure delegation mechanism for projection and feed-forward linear layers on accelerator-backed CKKS, while non-linear operators, attention-side control logic, KV-state transitions, and decrypt-then-encrypt refresh execute inside the CPU TEE. Bifrost+ further applies a prefill/decode split: prompt-side KV state is built inside the CPU TEE, and only decode-side state enters the hybrid ciphertext path. In an estimator-style comparison matching Euston&#x27;s methodology, Bifrost reduces projected latency by 9.25x on GPT-2 (1.5B) and 9.91x on LLaMA 3 (8B). In direct CKKS/FHE deployments, Bifrost+ reduces TTFT by 14.6-45.8x on GPT-2 (124M) and 15.3-53.4x on Qwen3 (0.6B). The systems lesson is selective encrypted execution: use FHE only where ciphertext-only accelerator delegation is required, and keep non-linear, refresh, and prompt-side work inside the CPU TEE.

  匹配依据：TEE: trusted execution environments

  </details>

- **The Proxy Knows Too Much: Sealing LLM API Routers with Attested TEEs**
  2026-06-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.16358)
  Sipeng Xie, Qianhong Wu, Hengrun Lu, Ziliang Sun, Qi Wu, Bo Qin, Qin Wang

  <details><summary>摘要 / Abstract</summary>

  Agents increasingly access large language models (LLMs) through API routers. A router terminates the client&#x27;s transport-layer security session and opens a separate upstream session, so it holds the full interaction in plaintext. This makes the router an application-layer man-in-the-middle: it can rewrite agent tool calls, swap dependencies for typosquatted packages, trigger attacks only under audit-evading conditions, and passively exfiltrate secrets. Existing client-side defenses are evadable. We propose AEGIS, a provider-transparent attested API router whose data path is a client-verified faithful passthrough. AEGISconfines plaintext handling to a small hardware-enclave component while leaving authentication, scheduling, accounting, and management on the untrusted host. The client verifies the enclave before releasing plaintext. The host can neither read nor alter the interaction, and plaintext leaves only toward destinations fixed by the measured image. We show that all four malicious-router attack classes succeed against a plaintext-access baseline and are blocked by AEGIS, including adaptive tests against the same boundary. The trusted path is $851$ lines, carries three provider-native APIs without conversion, and completes every request under real-provider workload and concurrency. In a seeded audit pilot, two commodity coding agents find eight and ten of ten planted invariant violations. The local relay overhead is about six milliseconds per request.

  匹配依据：TEE: hardware enclave

  </details>

- **OTRO: Oblivious Tokenization Path with Square-Root ORAM**
  2026-06-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.17358)
  Jonghyun Lee, Yongqin Wang, Rachit Rajat, Daniel Wong, Mengyuan Li, Murali Annavaram

  <details><summary>摘要 / Abstract</summary>

  The CPU-side large language model (LLM) tokenizer is a critical security gap in LLM serving through a confidential computing stack with CPU and GPU trusted execution environments (TEEs). Tokenizers converts the prompts through table-driven lookups, and the resulting memory access patterns are a powerful source of side-channel leakage. Recent work demonstrates end-to-end recovery of user prompts from tokenizer access pattern on production Intel TDX. However, a drop-in use of the popular tree-based Oblivious RAMs (e.g., PathORAM) to prevent access-pattern leakage introduces $\sim$13$\times$ tokenizer slowdown, resulting in 10-58% higher time-to-first-token (TTFT). In this paper, we present OTRO, an efficient, oblivious tokenization path tailored to latency-critical LLM serving. OTRO relies on square-root ORAM for fast single-access lookups, but avoids its prohibitive $O(N\log^2N$) rebuild cost every $\sqrt{N}$ accesses through three key innovations. First, OTRO provides a pool of replicated square-root ORAM instances that utilize the read-only nature of tokenizer table. Second, an epoch-based rotation policy decouples accesses from rebuilds and pads each epoch with dummy accesses to its boundaries, minimizing observable information. Lastly, chunked KV-cache-aware tokenization further overlaps rebuilds with GPU prefill and minimizes the instance count. Implemented as modules in HuggingFace Tokenizers and nano-vLLM, running within a TDX-enabled CVM with an NVIDIA H100 GPU, OTRO limits TTFT overhead to at most 4.5%, keeps tokenizer-induced latency under 10\% of total TTFT, and adds less than 0.5 GB of memory overhead while reducing the tokenizer&#x27;s observable leakage across various model families and sizes.

  匹配依据：TEE: confidential computing, intel tdx, trusted execution environments

  </details>

- **Invisible Manipulation Channels in AI-Assisted Financial Advisory: Implications for Market Integrity and Regulatory Design**
  2026-06-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.16121)
  Liuyang Yao, Zhouyu Li, Junguang He, Ziyang You

  <details><summary>摘要 / Abstract</summary>

  AI systems are increasingly deployed for credit assessment and investment advisory in global financial markets, yet the integrity of their inference pipelines remains insufficiently addressed by existing regulatory frameworks. This paper identifies and empirically validates an invisible manipulation channel operating at the sampling layer of LLM inference--a vulnerability that allows adversaries to systematically bias AI-generated financial opinions while preserving full compliance with output-based audit mechanisms, including statistical watermarking. We show that this inference-stage manipulation is statistically hard to detect: the Kullback-Leibler divergence between manipulated and normal output distributions can be made arbitrarily small, so that any output-based detection scheme requires impractically large sample sizes to achieve reliable detection power. Empirical experiments across credit rating and investment advisory scenarios show that directional bias keywords can be amplified by 1.8-1.9x under stealth-preserving (aware) manipulation while triggering zero of six black-box detectors and preserving watermark integrity. The vulnerability generalizes across three mainstream watermarking schemes and three heterogeneous model architectures, establishing it as a systemic financial infrastructure risk. Software-based defenses including cryptographically secure pseudorandom number generators are entirely ineffective, while QRNG combined with TEE hardware isolation achieves 100% attack blocking--reducing the target rate to the natural baseline--by replacing the predictable hash key with quantum-derived entropy that renders all pre-computed manipulation targets invalid. We propose four regulatory amendments centered on mandatory QRNG certification for high-risk financial AI systems under NIST SP 800-90B, inference-layer supply chain audits, and output provenance mechanisms.

  匹配依据：TEE: tee (context)

  </details>

- **Communication-Efficient Verifiable Attention for LLM Inference**
  2026-06-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.16352)
  Ziqun Chen, Ming Wu, Michael Heinrich, Jason Zeng, Huiying Lan, Tianwei Zhang, Rui Tan

  <details><summary>摘要 / Abstract</summary>

  Computation integrity of remote large language model (LLM) serving can be questionable. For conventional deep neural networks (DNNs), the existing TEE-shielded DNN partitioning (TSDP) approach uses Trusted Execution Environment (TEE) to compute non-linear components and verify the integrity of linear components offloaded to an untrusted GPU. However, directly applying TSDP to Transformer-based LLMs incurs significant TEE computation and TEE-GPU communication overhead. This paper presents Communication-efficient TEE-GPU Attention (\textsc{VeriAttn}) for accelerating verifiable LLM inference. \textsc{VeriAttn} offloads both linear and non-linear computations of attention to the GPU, while TEE performs verification. Moreover, for prefill, \textsc{VeriAttn} uses a two-level pipeline to overlap data movement, TEE pre-/post-processing, and GPU computation. For decoding, when the key-value cache exceeds available GPU memory, \textsc{VeriAttn} partitions attention across TEE and GPU to reduce repeated key-value transfers. Evaluation on an Intel TDX platform shows that \textsc{VeriAttn} achieves 2.60-3.38$\times$ and 3.86-5.42$\times$ acceleration over TSDP for 6k-token prompts and 10k-token outputs during prefill and decoding, respectively.

  匹配依据：TEE: intel tdx, trusted execution environment

  </details>

- **OpenPCC: Open and Confidential LLM Serving on Commodity TEEs**
  2026-06-09 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.11145)
  Haoling Zhou, Shixuan Zhao, Chao Wang, Zhiqiang Lin

  <details><summary>摘要 / Abstract</summary>

  Generative AI applications such as personal AI agents, image generators, and chat assistants offer advanced capabilities to improve user experience. Behind the scenes, Large Language Models (LLMs) that power these services require a massive amount of computation and are usually deployed in the cloud, available as APIs, meaning that a user&#x27;s request has to be sent to a Cloud Inference Service (CIS) for processing. However, the strong capabilities of LLM also mean that user&#x27;s requests now contain much more personal sensitive or enterprise confidential information, demanding equally strong protection in CIS. While early industry efforts such as Apple Private Cloud Compute (PCC) and Google Private AI Compute have emerged to show the potential of secure CIS, they are not adoptable for deployment by others due to their reliance on proprietary hardware and closed ecosystem. In addition, they all suffer from their own design glitches that can undermine the ambitious goal of bringing in true privacy protection to end users. In this paper, we present our analysis of the fundamental requirements of building a secure yet open CIS. We then present OpenPCC, a Confidential CIS framework that does not rely on proprietary hardware but instead uses commercially available TEEs. We implement an open-source prototype and characterize it end-to-end on a Llama-3 8B vLLM workload, separating OpenPCC&#x27;s own cost from the underlying TEE hardware. Our analysis and evaluation demonstrated the feasibility and security of the system.

  匹配依据：TEE: tees (context)

  </details>

- **A Hybrid Edge-Cloud Architecture for Low-Latency Entitlement Verification in Resource-Constrained Devices**
  2026-06-09 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.10536)
  Pravin Nagare, Aditya Sabbineni, Devendra Dahiphale, Faiz Gouri, Pratik Thantharate

  <details><summary>摘要 / Abstract</summary>

  As digital media consumption shifts toward large-scale Over-the-Top (OTT) platforms, the efficiency of the control plane, specifically entitlement and identity verification, has become a critical factor in user experience. Current architectures often rely on synchronous cloud-tethered validation flows that introduce significant latency, especially on resource-constrained consumer electronics. This paper proposes a Hybrid Edge-Cloud Entitlement Framework designed to minimize user-perceived friction. By implementing a secure, local caching layer within device middleware and utilizing an Adaptive Entitlement Cache with Proactive Refresh (AEC-PR) algorithm, we decouple the user interaction from backend network variability. We evaluate the performance on ARM Cortex-A series hardware, demonstrating that localized cryptographic verification reduces authorization latency from a mean of 422.8ms to 18.4ms (a 95.6% reduction) while mitigating implementation-level side-channel risks through deterministic Ed25519 arithmetic and TEE isolation.

  匹配依据：TEE: tee (context)

  </details>

- **Trustworthy Smart Fabs via Professional Proxies: Scaling Safe and Sustainable by Design (SSbD) through Industrial Data Spaces**
  2026-06-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.09227)
  Han-Teng Liao, Chang-Yi Kao, Karen Ang

  <details><summary>摘要 / Abstract</summary>

  The convergence of the 2026 European Union Safe and Sustainable by Design (SSbD) framework, Corporate Sustainability Due Diligence Directive (CSDDD), and Carbon Border Adjustment Mechanism (CBAM) introduce a severe governance bottleneck for advanced semiconductor manufacturing facilities (&quot;Smart Fabs&quot;). Regulatory compliance demands have surpassed the capacity of manual corporate reporting, creating a direct conflict between multi-stakeholder transparency and corporate data privacy. This paper addresses this challenge by introducing a zero-trust socio-technical orchestration framework that operationalizes a six-layer SSbD reference architecture within trustworthy industrial data spaces. We propose a shift from reactive automation to autonomous governance through &quot;Professional Proxies&quot;-role-based agentic workflows executing within hardware-isolated trust zones. Structured as an interoperable network protocol stack, the framework coordinates an automated, five-step &quot;relay race&quot; between Facility, Process Engineering, and Finance proxy teams to align factory-floor yield models with macro-level sustainability mandates. By executing Virtual Metrology (VM) predictions and Federated Machine Learning (FML) inside hardware-rooted Trusted Execution Environments (TEEs), this architecture resolves the Data Sovereignty Paradox, demonstrating how fabs can export cryptographically signed compliance tokens via International Data Spaces (IDS) connectors without exposing proprietary process recipes. Ultimately, this framework provides technology managers with a verifiable, evidence-based pathway toward resilient, net-zero Industry 5.0 ecosystems.

  匹配依据：TEE: trusted execution environments

  </details>

- **Fully Oblivious Differential Privacy for Frequency Estimation in the Augmented Shuffle Model with Trusted Processors**
  2026-06-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.09402)
  Takao Murakami, Yuichi Sei, Reo Eriguchi

  <details><summary>摘要 / Abstract</summary>

  In the shuffle model of DP (Differential Privacy), a shuffler randomly permutes users&#x27; data to achieve high accuracy and privacy. Recent studies show that most existing shuffle protocols are vulnerable to collusion attacks by the data collector and users. They address this issue by introducing the augmented shuffle model that incorporates random sampling and dummy data addition into the shuffler. However, it remains open how to ensure the shuffler follows the protocol and does not collude with the data collector in this model. We address this trust issue by thoroughly exploring the augmented shuffle model with TEEs (Trusted Execution Environments). We first introduce a new privacy notion, FODP (Fully Oblivious DP), which strengthens DP to prevent various TEE side-channel attacks based on external/internal memory access patterns and control flows. We propose a general framework for FODP algorithms based on memory-size obfuscation and three concrete algorithms within it. We also improve the efficiency of our algorithms by using the count-min sketch and optimizing the number of hashes. We evaluate our algorithms on Intel SGX and demonstrate their effectiveness through comparisons with nine baselines.

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **EnclaveScale: Hardware-Assisted Edge-DP for Secure Data Centre Power Telemetry**
  2026-06-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.09163)
  Hung Dang, Tue Nguyen, Minh Vo

  <details><summary>摘要 / Abstract</summary>

  EnclaveScale is a distributed, hardware-assisted telemetry architecture providing post-extraction attestation, enabling operators to collaboratively model high-resolution generative AI power transients. Existing cryptographic techniques scale poorly for 10-Hz streaming or fail to authenticate origins, permitting malicious hosts to spoof sensor inputs. We implement and evaluate a post-extraction pipeline utilizing DCAP attestation, differential privacy noise injection, and Byzantine rejection across 32 GCP Confidential VMs, achieving 0\% post-extraction attack success rate. This edge-DP approach distils continuous GPU transients into discrete Markov-chain transition matrices, guaranteeing event-level differential privacy. To mitigate pre-ingestion vulnerabilities, we propose an SPDM-authenticated first-mile layer. While current platforms lack attested I/O, emerging hardware architectures integrate PCIe IDE and TDISP to natively prevent host-level synthesis, securing the end-to-end provenance boundary. A Global Aggregation Enclave verifies these cryptographic proofs prior to capacity-weighted aggregation. Evaluation demonstrates a steady-state throughput of $131{,}406$ samples/s per enclave, amortising attestation overhead to $0.23\,μ$s/sample. On empirical NVML-sampled H100, A100, and L4 traces, EnclaveScale achieves a dynamic orchestration margin error of $1.3$\,MW compared to $0.1$\,MW for an honest-aggregator central-DP baseline. EnclaveScale establishes a secure foundation for dynamic multi-tenant power orchestration, obfuscating sub-second anomalies locally and protecting macro-workload confidentiality via spatial dilution during global aggregation.

  匹配依据：TEE: enclave (context)

  </details>

- **Chimera: Protocol-Aware Recovery for Confidential BFT Consensus**
  2026-06-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.09101)
  Tong Liu, Xiaoqing Wen, Ziwei Zhou, Si Liu, Jianyu Niu, Cong Wang, Yinqian Zhang

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) have enabled confidential Byzantine Fault-Tolerant (BFT) consensus systems with confidentiality and improved scalability. However, TEEs do not provide state continuity: during recovery, a compromised host can roll back a crashed enclave to a stale persistent state, significantly threatening both safety and availability. Existing defenses face a fundamental tradeoff: they either impose substantial overhead on critical consensus paths, reducing throughput and increasing latency, or incur prolonged recovery delays, hurting availability. We present the first systematic taxonomy of rollback-resilient recovery for confidential BFT consensus, distilling prior approaches into four categories. We further expose their inherent limitations. Guided by this detailed analysis, we design CHIMERA, a protocol-aware recovery framework that breaks this tradeoff. Our key insight is that rollback protection in consensus systems should not be uniform. Different types of persistent states differ fundamentally in their state distribution, update behavior, and representation form. CHIMERA separates persistent state into metadata and logs according to these protocol-level properties and applies distinct recovery mechanisms to each type. We formally model CHIMERA in Maude and verify its safety and liveness properties. We implement it on Braft and ZooKeeper using Intel TDX, and evaluate it in both LAN and WAN settings. Results show that CHIMERA achieves higher throughput, lower recovery latency, and better availability than state-of-the-art rollback-resilient baselines.

  匹配依据：TEE: intel tdx, trusted execution environments

  </details>

- **Verifiable and Confidential DNN Inference on Low-End Edge Devices**
  2026-06-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.07470)
  Mohamed Khalil Kiri, Ivan De Oliveira Nunes, Aurélien Francillon, Norrathep Rattanavipanon

  <details><summary>摘要 / Abstract</summary>

  Deploying deep neural network (DNN) inference on low-end edge devices raises two key challenges: protecting model confidentiality against a potentially compromised edge system and enabling verifiable inference without incurring prohibitive overhead. Existing approaches either house partial models and inference software within trusted execution environments (TEEs), resulting in high cost and an application-dependent trusted computing base (TCB), or execute in untrusted environments, providing little security. In this work, we present VECODI, a framework for verifiable and confidential DNN inference on constrained edge devices. At its core, VECODI introduces SHANGRI-LA, a new execution abstraction on TrustZone-M TEEs that establishes a third runtime environment with privileges strictly between the Secure and Non-Secure Worlds. VECODI leverages SHANGRI-LA to execute untrusted inference code in the Non-Secure World while using minimal application-agnostic Secure-World support to protect model confidentiality and enable verifiability (with respect to proper execution of inference code and model parameters) of inference results. We realize VECODI on a real-world NUCLEO-L552ZE-Q development board and open-source its prototype. Our results show VECODI&#x27;s small TCB, memory footprint, and runtime overhead, making it a practical option for secure inference in low-end edge devices.

  匹配依据：TEE: trusted execution environments, trustzone

  </details>

- **Opportunities and Challenges in Securely Reusing and Repurposing Mobile Devices**
  2026-06-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.06181)
  Adelin Roty, Jan Tobias Mühlberg, Jean-François Determe

  <details><summary>摘要 / Abstract</summary>

  An estimated 5.3 billion mobile phones became electronic waste in 2022. Many of these devices can be repurposed and used in different contexts to extend their lifetime and to reduce ecological impacts. An often overlooked aspect of smartphone reuse is cybersecurity: these devices embed hardware-backed security mechanisms that rely on vendor-controlled provisioning and are designed for a fixed device lifecycle. In this paper, we investigate whether security mechanisms and guarantees remain effective when devices are repurposed outside their original ecosystem. We explore security features in a PinePhone, an open-hardware smartphone, and focus on three core security aspects: boot chain integrity, isolation provided by the Trusted Execution Environment, and the protection of hardware-bound secrets. Our experiments simulate realistic repurposing scenarios and highlight the complexity of reconstructing trust anchors. We generalize our observations to infer requirements for secure repurposing and illustrate how vendor locked mechanisms hinder the repurposing of a majority of discarded devices.

  匹配依据：TEE: trusted execution environment

  </details>

- **PS-UIE: Privilege-Separated Integrity Enforcement for User-Space Executable Objects in Confidential VMs**
  2026-06-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.04549)
  Jingkai Mao, Xiaolin Chang

  <details><summary>摘要 / Abstract</summary>

  Confidential Virtual Machines (CVMs), such as AMD SEV-SNP, enable cloud tenants to run security-sensitive workloads, but tenants can rely on the execution of these workloads only when they can trust the CVM. This trust requires continuous integrity assurance from CVM launch to the current runtime state, including initial trust establishment at launch and subsequent runtime integrity assurance. Existing works help establish launch-time trust and protect parts of runtime integrity, but they do not fully address the integrity of file-backed user-space executable objects, such as main executables, program interpreters, and dynamically loaded shared objects, that may be loaded or mapped dynamically during execution inside CVMs. In this paper, we propose Privilege-Separated User-space Integrity Enforcement (PS-UIE), an approach for enforcing the integrity of user-space executable objects inside AMD SEV-SNP-based CVMs. PS-UIE consists of a privilege-separated architecture and three mechanisms. The architecture separates the authority for integrity measurement and enforcement from the measured targets by placing it in a higher-privileged protected domain. Built on this architecture, PS-UIE provides policy lifecycle management, execution-time integrity enforcement, and evidence export and verification mechanisms. It enables policy-controlled integrity measurement and enforcement for user-space executable objects and generates verifiable runtime evidence. We implement PS-UIE on an AMD SEV-SNP platform. The security analysis and performance evaluation show that PS-UIE enforces the integrity of user-space executable objects on the covered execute-permission grant paths and provides verifiable runtime evidence while incurring acceptable overhead.

  匹配依据：TEE: amd sev

  </details>
