# 2025 · MPC · 仅预印本来源 · 第 4/5 页

[总目录](../PAPERS.md) · [上一页](2025-mpc-preprint-03.md) · [下一页](2025-mpc-preprint-05.md)

- **Pura: An Efficient Privacy-Preserving Solution for Face Recognition**
  2025-05-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.15476)
  Guotao Xu, Bowen Zhao, Yang Xiao, Yantao Zhong, Liang Zhai, Qingqi Pei

  <details><summary>摘要 / Abstract</summary>

  Face recognition is an effective technology for identifying a target person by facial images. However, sensitive facial images raises privacy concerns. Although privacy-preserving face recognition is one of potential solutions, this solution neither fully addresses the privacy concerns nor is efficient enough. To this end, we propose an efficient privacy-preserving solution for face recognition, named Pura, which sufficiently protects facial privacy and supports face recognition over encrypted data efficiently. Specifically, we propose a privacy-preserving and non-interactive architecture for face recognition through the threshold Paillier cryptosystem. Additionally, we carefully design a suite of underlying secure computing protocols to enable efficient operations of face recognition over encrypted data directly. Furthermore, we introduce a parallel computing mechanism to enhance the performance of the proposed secure computing protocols. Privacy analysis demonstrates that Pura fully safeguards personal facial privacy. Experimental evaluations demonstrate that Pura achieves recognition speeds up to 16 times faster than the state-of-the-art.

  匹配依据：MPC: secure computing

  </details>

- **Monitoring in the Dark: Privacy-Preserving Runtime Verification of Cyber-Physical Systems**
  2025-05-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.16059)
  Charles Koll, Preston Tan Hang, Mike Rosulek, Houssam Abbas

  <details><summary>摘要 / Abstract</summary>

  In distributed Cyber-Physical Systems and Internet-of-Things applications, the nodes of the system send measurements to a monitor that checks whether these measurements satisfy given formal specifications. For instance in Urban Air Mobility, a local traffic authority will be monitoring drone traffic to evaluate its flow and detect emerging problematic patterns. Certain applications require both the specification and the measurements to be private -- i.e. known only to their owners. Examples include traffic monitoring, testing of integrated circuit designs, and medical monitoring by wearable or implanted devices. In this paper we propose a protocol that enables privacy-preserving robustness monitoring. By following our protocol, both system (e.g. drone) and monitor (e.g. traffic authority) only learn the robustness of the measured trace w.r.t. the specification. But the system learns nothing about the formula, and the monitor learns nothing about the signal monitored. We do this using garbled circuits, for specifications in Signal Temporal Logic interpreted over timed state sequences. We analyze the runtime and memory overhead of privacy preservation, the size of the circuits, and their practicality for three different usage scenarios: design testing, offline monitoring, and online monitoring of Cyber-Physical Systems.

  匹配依据：MPC: garbled circuits

  </details>

- **Covert Attacks on Machine Learning Training in Passively Secure MPC**
  2025-05-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.17092) · [IACR ePrint](https://eprint.iacr.org/2025/906)
  Matthew Jagielski, Daniel Escudero, Rahul Rachuri, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) allows data owners to train machine learning models on combined data while keeping the underlying training data private. The MPC threat model either considers an adversary who passively corrupts some parties without affecting their overall behavior, or an adversary who actively modifies the behavior of corrupt parties. It has been argued that in some settings, active security is not a major concern, partly because of the potential risk of reputation loss if a party is detected cheating. In this work we show explicit, simple, and effective attacks that an active adversary can run on existing passively secure MPC training protocols, while keeping essentially zero risk of the attack being detected. The attacks we show can compromise both the integrity and privacy of the model, including attacks reconstructing exact training data. Our results challenge the belief that a threat model that does not include malicious behavior by the involved parties may be reasonable in the context of PPML, motivating the use of actively secure protocols for training.

  匹配依据：MPC: secure multiparty computation

  </details>

- **A Survey On Secure Machine Learning**
  2025-05-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.15124)
  Taobo Liao, Taoran Li, Prathamesh Nadkarni

  <details><summary>摘要 / Abstract</summary>

  In this survey, we will explore the interaction between secure multiparty computation and the area of machine learning. Recent advances in secure multiparty computation (MPC) have significantly improved its applicability in the realm of machine learning (ML), offering robust solutions for privacy-preserving collaborative learning. This review explores key contributions that leverage MPC to enable multiple parties to engage in ML tasks without compromising the privacy of their data. The integration of MPC with ML frameworks facilitates the training and evaluation of models on combined datasets from various sources, ensuring that sensitive information remains encrypted throughout the process. Innovations such as specialized software frameworks and domain-specific languages streamline the adoption of MPC in ML, optimizing performance and broadening its usage. These frameworks address both semi-honest and malicious threat models, incorporating features such as automated optimizations and cryptographic auditing to ensure compliance and data integrity. The collective insights from these studies highlight MPC&#x27;s potential in fostering collaborative yet confidential data analysis, marking a significant stride towards the realization of secure and efficient computational solutions in privacy-sensitive industries. This paper investigates a spectrum of SecureML libraries that includes cryptographic protocols, federated learning frameworks, and privacy-preserving algorithms. By surveying the existing literature, this paper aims to examine the efficacy of these libraries in preserving data privacy, ensuring model confidentiality, and fortifying ML systems against adversarial attacks. Additionally, the study explores an innovative application domain for SecureML techniques: the integration of these methodologies in gaming environments utilizing ML.

  匹配依据：MPC: secure multiparty computation

  </details>

- **A Generic Framework for Practical Lattice-Based Non-interactive Publicly Verifiable Secret Sharing**
  2025-05-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/901)
  Behzad Abdolmaleki, John Clark, Mohammad Foroutani, Shahram Khazaei, Sajjad Nasirzadeh

  <details><summary>摘要 / Abstract</summary>

  Non-interactive publicly verifiable secret sharing (PVSS) schemes enable the decentralized (re-)sharing of secrets in adversarial environments, allowing anyone to verify the correctness of distributed shares. Such schemes are essential for large-scale decentralized applications, including committee-based systems that require both transparency and robustness. However, existing PVSS schemes rely on group-based cryptography, making them vulnerable to quantum attacks and limiting their suitability for post-quantum applications. In this work, we propose the first practical, fully lattice-based, non-interactive PVSS scheme, grounded on standard lattice assumptions for post-quantum security. At the heart of our design lies a generic framework that transforms vector commitments and linear encryption schemes into practical PVSS protocols. We enhance vector commitments by incorporating proof of smallness, ensuring that encrypted shares are both verifiable and privacy-preserving. Our construction introduces two tailored lattice-based encryption schemes, each supporting efficient proofs of decryption correctness. This framework provides strong verifiability guarantees while maintaining low proof sizes and computational efficiency.

  匹配依据：MPC: secret sharing

  </details>

- **Blinding Post-Quantum Hash-and-Sign Signatures**
  2025-05-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/895)
  Charles Bouillaguet, Thibauld Feneuil, Jules Maire, Matthieu Rivain, Julia Sauvage, Damien Vergnaud

  <details><summary>摘要 / Abstract</summary>

  Blind signature schemes are essential for privacy-preserving applications such as electronic voting, digital currencies or anonymous credentials. In this paper, we revisit Fischlin&#x27;s framework for round-optimal blind signature schemes and its recent efficient lattice-based instantiations. Our proposed framework compiles any post-quantum hash-and-sign signature scheme into a blind signature scheme. The resulting scheme ensures blindness by design and achieves one-more unforgeability, relying solely on the unforgeability of the underlying signature scheme and the random oracle model. To achieve this we introduce the notion of commit-append-and-prove (CAP) systems, which generalizes traditional commit-and-prove system by making their commitments updatable before proving. This building block allows us to unlock the technical challenges encountered when generalizing previous variants of the Fischlin&#x27;s framework to any hash-and-sign signature scheme. We provide efficient CAP system instantiations based on recent MPC-in-the-Head techniques. We showcase our framework by constructing blind versions of UOV and Wave, thereby introducing the first practical blind signatures based on multivariate cryptography and code-based cryptography. Our blind UOV signatures range from 3.8 KB to 11 KB, significantly outperforming previous post-quantum blind signatures, such as the 22 KB lattice-based blind signatures, which were the most compact until now.

  匹配依据：MPC: mpc (context)

  </details>

- **Fast Fuzzy PSI from Symmetric-Key Techniques**
  2025-05-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/885)
  Cong Zhang, Yu Chen, Yang Cao, Yujie Bai, Shuaishuai Li, Juntong Lin, Anyu Wang, Xiaoyun Wang

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) enables a sender holding a set $Q$ and a receiver holding a set $W$ to securely compute the intersection $Q\cap W$. Fuzzy PSI (FPSI) is a PSI variant where the receiver learns the items $q\in Q$ for which there exists $w\in W$ such that $\dist(q, w) \leq \delta$ with respect to some distance metric. Recently, Gao et al. (ASIACRYPT 2024) proposed the first FPSI protocols for $L_\infty$ and $L_{p\in[1,\infty)}$ distance with linear complexity. They summarized their FPSI construction into two steps: fuzzy mapping and fuzzy matching. However, their realizations of the two steps heavily rely on public key operations, namely the DH-key exchange and additively homomorphic encryption, resulting in low efficiency. In this work, we propose new FPSI protocols for $L_\infty$ and $L_{p\in[1,\infty)}$ distances, primarily leveraging symmetric-key primitives. We revisit the definition of fuzzy mapping and rigorously redefine it as a cryptographic scheme. We further introduce consistency for fuzzy mapping scheme, which could simplify the fuzzy matching step into plain PSI. We then demonstrate how to execute fuzzy mapping step satisfying consistency. We also propose several new technologies to completely avoid the extensive use of computationally expensive public-key operations burden inherent in existing solutions. We implement our FPSI protocols and compare them with the state-of-the-art FPSI protocols. Experiments show that our protocols perform better than state-of-the-art under all the parameters we tested. Specifically, our protocols achieve a $2.2-83.9 \times $ speedup in running time and $1.5-11.5 \times$ shrinking in communication cost, depending on set sizes, dimension and distance threshold.

  匹配依据：MPC: private set intersection

  </details>

- **One-Way Homomorphic Encryption: A Composite Group Approach**
  2025-05-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/881)
  Mahdi Mahdavi, Helena Rifà-Pous

  <details><summary>摘要 / Abstract</summary>

  Homomorphic Encryption (HE) is a fundamental Privacy-Enhancing Technology (PET) that enables computations on encrypted data without decryption. Despite its utility, designing an efficient and secure HE scheme is highly complex, requiring sophisticated cryptographic techniques. This paper introduces a novel approach to achieving homomorphic properties—supporting either one addition or one multiplication—within composite groups. While the proposed technique exhibits one-wayness, it has a good potential to serve as a foundational building block for constructing indistinguishable cryptosystems. This work contributes to the advancement of homomorphic encryption by providing a new perspective on secure computation within structured algebraic settings.

  匹配依据：MPC: secure computation

  </details>

- **UltraProofs: Scalable Reed-Solomon Code Commitment**
  2025-05-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/865)
  Yanpei Guo, Alex Luoyuan Xiong, Wenjie Qu, Jiaheng Zhang

  <details><summary>摘要 / Abstract</summary>

  Reed–Solomon (RS) codes underpin a wide range of cryptographic protocols, from verifiable secret sharing (VSS) to blockchain data availability (DA). An RS code commitment enables a prover to distribute codeword fragments among many parties while allowing each recipient to verify that its fragment is consistent with a RS code. Existing constructions either rely on homomorphic polynomial commitments, which incur redundant commitments and expensive group operations, or use FRI-based interactive proofs, which achieve fast proving but suffer from prohibitively large communication. We present UltraProofs, a new RS code commitment framework that achieves linear-time proof generation while remaining compatible with any multilinear polynomial commitment. Our key technical contribution is an evaluation-consolidation protocol that reduces $n$ evaluation proofs at distinct RS points to a single randomized evaluation, eliminating redundant commitments and removing the need for homomorphic structure. We further design a tailored multilinear PCS, LightLigero, which achieves $O(\lambda \log n)$ proof size and maintains $O(n \log n)$ prover time. UltraProofs attains asymptotically optimal prover complexity with concrete speedups in practice: in VSS, it reduces prover time by $2.4\times$ and proof size by $4\times$ compared to HydraProofs (S&amp;P&#x27;25); in DA, it cuts per-node communication by up to $2{\sim}5\times$ relative to FRIDA (Crypto&#x27;24) while retaining similar prover cost. By decoupling verifiable RS encoding from any specific PCS instantiation, UltraProofs provides a flexible, efficient, and modular foundation for large-scale verifiable storage and distributed cryptographic systems.

  匹配依据：MPC: secret sharing

  </details>

- **High-efficient long-distance device-independent quantum secret sharing based on single-photon sources**
  2025-05-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.10797)
  Qi Zhang, Cheng Zhang, Wei Zhong, Ming-Ming Du, Lan Zhou, Yu-Bo Sheng

  <details><summary>摘要 / Abstract</summary>

  Device-independent quantum secret sharing (DI QSS) relaxes security assumptions of experimental devices to provide the highest security level for QSS. Previous DI QSS protocols require to generate multi-partite entangled states and then implement the long-distance entanglement distribution. The extremely low generation probability of current multi-partite entanglement source and photon transmission loss largely limit DI QSS&#x27;s practical key generation rate and secure photon transmission distance. In the paper, we propose a high-efficient long-distance DI QSS protocol based on practical nearly on-demand single-photon sources (SPSs), which adopts the single photons and heralded architecture to construct long-distance multi-partite entanglement channels. Our SPS DI QSS protocol can automatically eliminate the negative influence from photon transmission loss and largely increase the secure photon transmission distance. Moreover, we adopt active improvement strategies such as random key generation basis, postselection, and advanced postselection to further increase the practical key generation rate and lower the experimental requirement. Comparing with previous DI QSS protocols based on entanglement sources, our SPS DI QSS protocol can increase the practical communication efficiency by six orders of magnitude, and increase the secure photon transmission distance by at least 151 times. This SPS DI QSS protocol is feasible with the current experimental technologies. Our protocol makes it possible to realize high-efficient long-distance DI network in the near future.

  匹配依据：MPC: secret sharing

  </details>

- **Delegated PSI from Homomorphic Encryptions**
  2025-05-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/868)
  Sicheng Wei, Jingwei Hu

  <details><summary>摘要 / Abstract</summary>

  This paper presents an efficient protocol for private set intersection in a setting with multiple set owners and a semi-honest cloud server. The core idea is to reduce the intersection computation to secure operations over Bloom filters, enabling both scalability and efficiency. By leveraging this transformation, our protocols achieve strong privacy guarantees while minimizing computation and communication overhead.

  匹配依据：MPC: private set intersection

  </details>

- **Blockchain-Enabled Decentralized Privacy-Preserving Group Purchasing for Energy Plans**
  2025-05-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.11094)
  Sid Chi-Kin Chau, Yue Zhou

  <details><summary>摘要 / Abstract</summary>

  Retail energy markets are increasingly consumer-oriented, thanks to a growing number of energy plans offered by a plethora of energy suppliers, retailers and intermediaries. To maximize the benefits of competitive retail energy markets, group purchasing is an emerging paradigm that aggregates consumers&#x27; purchasing power by coordinating switch decisions to specific energy providers for discounted energy plans. Traditionally, group purchasing is mediated by a trusted third-party, which suffers from the lack of privacy and transparency. In this paper, we introduce a novel paradigm of decentralized privacy-preserving group purchasing, empowered by privacy-preserving blockchain and secure multi-party computation, to enable users to form a coalition for coordinated switch decisions in a decentralized manner, without a trusted third-party. The coordinated switch decisions are determined by a competitive online algorithm, based on users&#x27; private consumption data and current energy plan tariffs. Remarkably, no private user consumption data will be revealed to others in the online decision-making process, which is carried out in a transparently verifiable manner to eliminate frauds from dishonest users and supports fair mutual compensations by sharing the switching costs to incentivize group purchasing. We implemented our decentralized group purchasing solution as a smart contract on Solidity-supported blockchain platform (e.g., Ethereum), and provide extensive empirical evaluation.

  匹配依据：MPC: secure multi party computation

  </details>

- **Private Transformer Inference in MLaaS: A Survey**
  2025-05-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.10315)
  Yang Li, Xinyu Zhou, Yitong Wang, Liangxin Qian, Jun Zhao

  <details><summary>摘要 / Abstract</summary>

  Transformer models have revolutionized AI, powering applications like content generation and sentiment analysis. However, their deployment in Machine Learning as a Service (MLaaS) raises significant privacy concerns, primarily due to the centralized processing of sensitive user data. Private Transformer Inference (PTI) offers a solution by utilizing cryptographic techniques such as secure multi-party computation and homomorphic encryption, enabling inference while preserving both user data and model privacy. This paper reviews recent PTI advancements, highlighting state-of-the-art solutions and challenges. We also introduce a structured taxonomy and evaluation framework for PTI, focusing on balancing resource efficiency with privacy and bridging the gap between high-performance inference and data privacy.

  匹配依据：MPC: secure multi party computation

  </details>

- **Multiplication triples from entangled quantum resources**
  2025-05-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.10385)
  Maxwell Gold, Eric Chitambar

  <details><summary>摘要 / Abstract</summary>

  An efficient paradigm for multi-party computation (MPC) are protocols structured around access to shared pre-processed computational resources. In this model, certain forms of correlated randomness are distributed to the participants prior to their computation. The shared randomness is then consumed in a computation phase that involves public communication with efficient round complexity, and the computation is secure in this second phase provided the initial correlations were distributed securely. Usually the latter requires some strong setup assumptions, such as a trusted dealer and private channels. We present a novel approach for generating these correlations from entangled quantum graph states and yield information-theoretic privacy guarantees that hold against a malicious adversary, with limited assumptions. Our primary contribution is a tripartite resource state and measurement-based protocol for extracting a binary multiplication triple, a special form of shared randomness that enables the private multiplication of a bit conjunction. Here, we employ a third party as a Referee and demand only an honest pair among the three parties. The role of this Referee is weaker than that of a Dealer, as the Referee learns nothing about the underlying shared randomness that is disseminated. We prove perfect privacy for our protocol, assuming access to an ideal copy of the resource state, an assumption that is based on the existence of graph state verification protocols. Finally, we demonstrate its application as a primitive for more complex Boolean functionalities such as 1-out-of-2 oblivious transfer (OT) and MPC for an arbitrary $N$-party Boolean function, assuming access to the proper broadcasting channel.

  匹配依据：MPC: multi party computation, oblivious transfer

  </details>

- **Encrypted Matrix-Vector Products from Secret Dual Codes**
  2025-05-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/858)
  Fabrice Benhamouda, Caicai Chen, Shai Halevi, Yuval Ishai, Hugo Krawczyk, Tamer Mour, Tal Rabin, Alon Rosen

  <details><summary>摘要 / Abstract</summary>

  Motivated by applications to efficient secure computation, we consider the following problem of encrypted matrix–vector product (EMVP). Let $\mathbb F$ be a finite field. In an offline phase, a client uploads an encryption of a matrix $M \in \mathbb F^{m\times \ell}$ to a server, keeping only a short secret key. The server stores the encrypted matrix \(\hat{M}\). In the online phase, the client may repeatedly send encryptions \(\hat{ q}_i\) of query vectors \(q_i \in \mathbb F^\ell\), which enables the client and the server to locally compute compact shares of the matrix–vector product \(Mq_i\). The server learns nothing about \(M\) or \(q_i\). The shared output can either be revealed to the client or processed by another protocol. We present efficient EMVP protocols based on variants of the learning parity with noise (LPN) assumption and the related learning subspace with noise (LSN) assumption. Our EMVP protocols are field-agnostic in the sense that the parties only perform arithmetic operations over \(\mathbb F\), and are close to optimal with respect to both communication and computation. In fact, for sufficiently large \(\ell\) (typically a few hundreds), the online computation and communication costs of our LSN-based EMVP can be \emph{less than twice} the costs of computing \(Mq_i\) in the clear. Combined with suitable secure post-processing protocols on the secret-shared output, our EMVP protocols are useful for a variety of secure computation tasks, including encrypted fuzzy search and secure ML. Our technical approach builds on recent techniques for private information retrieval in the secret-key setting. The core idea is to encode the matrix \(M\) and the queries \(q_i\) using a pair of secret dual linear codes, while defeating algebraic attacks by adding noise.

  匹配依据：MPC: secure computation

  </details>

- **Towards the ideals of Self-Recovery and Metadata Privacy in Social Vault Recovery with Apollo**
  2025-05-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.19484)
  Shailesh Mishra, Simone Colombo, Pasindu Tennage, Martin Burkhart, Bryan Ford

  <details><summary>摘要 / Abstract</summary>

  Social recovery enables users to enlist trusted contacts, or trustees, to help recover lost access to end-to-end-encrypted repositories or vaults. However, existing recovery mechanisms often make strong memorability assumptions about what users will remember. Weakening these memorability assumptions to increase the robustness of recovery is possible, but may leak sensitive metadata about the user and/or trustees if done naively. This paper&#x27;s first contribution is to draw attention to and formalize this basic tension between memorability and metadata privacy in social vault recovery. Our second contribution is Apollo, a social recovery mechanism that aims to avoid any memorability assumptions while strongly protecting recovery metadata privacy. Apollo approximates the ideal of self-recovery by relying only on a threshold of social reconnection events, which may be initiated either by the user or the user&#x27;s contacts. Apollo thereby has a chance of succeeding in vault recovery even in a worst-case scenario where the user has forgotten all metadata, including even the vault&#x27;s existence. To protect the metadata&#x27;s privacy, Apollo distributes either real or fake (chaff) data to all of a user&#x27;s contacts, not just the user&#x27;s trustees, thus systematically anonymizing the trustees among the larger set of contacts. To make this anonymity set scalable, Apollo uses a novel multi-layered secret sharing scheme to mitigate the computational overhead of recovery in this setting, which would otherwise be exponential in the recovery threshold. Finally, we evaluate a prototype implementation of Apollo. Apollo reduces the probability of malicious recovery to under 0.1% for an adversary capable of obtaining shares from every 1-out-of-2 contacts. After reconnecting with 30 contacts, the multi-layered design shows an improvement of 5 orders in computation time, compared to a single-layered approach.

  匹配依据：MPC: secret sharing

  </details>

- **Quantum ($t$,$n$) Threshold Multi-Secret Sharing based on Cluster States**
  2025-05-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.09317)
  Rui-Hai Ma, Hui-Nan Chen, Bin-Bin Cai, Song Lin, Xiao-Chen Zhang

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing is an encryption technique based on quantum mechanics, which utilizes uncertainty principle to achieve security in transmission. Most protocols focus on the study of quantum ($n,n$) or ($t,n$) threshold single secret sharing. In this paper, the first quantum ($t,n$) threshold multi-secret sharing protocol based on Lagrangian interpolation and cluster states is proposed, which requires only $t$ instead of $n$ participants to reconstruct multiple quantum secrets. The protocol exploits the security properties of the cluster state to transmit shared information in two parts, quantum and classical, where the shares remain private after reconstructing quantum secrets. Meanwhile, extending the new measurement basis in cluster states enables participants to transmit quantum information without preparing particles. In the presented protocol, the dealer can be offline after sending secrets. And required quantum operations are all common quantum operations, thus the protocol is practical under the current technical conditions. It is proven to be theoretically secure against external and internal attacks by analyzing the protocol under several common external attacks and internal attacks. In addition, experiments on IMB Q prove that the protocol satisfies correctness and feasibility.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Runtime Verification**
  2025-05-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.09276)
  Thomas A. Henzinger, Mahyar Karimi, K. S. Thejaswini

  <details><summary>摘要 / Abstract</summary>

  Runtime verification offers scalable solutions to improve the safety and reliability of systems. However, systems that require verification or monitoring by a third party to ensure compliance with a specification might contain sensitive information, causing privacy concerns when usual runtime verification approaches are used. Privacy is compromised if protected information about the system, or sensitive data that is processed by the system, is revealed. In addition, revealing the specification being monitored may undermine the essence of third-party verification. In this work, we propose two novel protocols for the privacy-preserving runtime verification of systems against formal sequential specifications. In our first protocol, the monitor verifies whether the system satisfies the specification without learning anything else, though both parties are aware of the specification. Our second protocol ensures that the system remains oblivious to the monitored specification, while the monitor learns only whether the system satisfies the specification and nothing more. Our protocols adapt and improve existing techniques used in cryptography, and more specifically, multi-party computation. The sequential specification defines the observation step of the monitor, whose granularity depends on the situation (e.g., banks may be monitored on a daily basis). Our protocols exchange a single message per observation step, after an initialisation phase. This design minimises communication overhead, enabling relatively lightweight privacy-preserving monitoring. We implement our approach for monitoring specifications described by register automata and evaluate it experimentally.

  匹配依据：MPC: multi party computation

  </details>

- **SAFE-SiP: Secure Authentication Framework for System-in-Package Using Multi-party Computation**
  2025-05-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.09002)
  Ishraq Tashdid, Tasnuva Farheen, Sazadur Rahman

  <details><summary>摘要 / Abstract</summary>

  The emergence of chiplet-based heterogeneous integration is transforming the semiconductor, AI, and high-performance computing industries by enabling modular designs and improved scalability. However, assembling chiplets from multiple vendors after fabrication introduces a complex supply chain that raises serious security concerns, including counterfeiting, overproduction, and unauthorized access. Current solutions often depend on dedicated security chiplets or changes to the timing flow, which assume a trusted SiP integrator. This assumption can expose chiplet signatures to other vendors and create new attack surfaces. This work addresses those vulnerabilities using Multi-party Computation (MPC), which enables zero-trust authentication without disclosing sensitive information to any party. We present SAFE-SiP, a scalable authentication framework that garbles chiplet signatures and uses MPC for verifying integrity, effectively blocking unauthorized access and adversarial inference. SAFE-SiP removes the need for a dedicated security chiplet and ensures secure authentication, even in untrusted integration scenarios. We evaluated SAFE-SiP on five RISC-V-based System-in-Package (SiP) designs. Experimental results show that SAFE-SiP incurs minimal power overhead, an average area overhead of only 3.05%, and maintains a computational complexity of 2^192, offering a highly efficient and scalable security solution.

  匹配依据：MPC: multi party computation

  </details>

- **Privacy-Preserving Analytics for Smart Meter (AMI) Data: A Hybrid Approach to Comply with CPUC Privacy Regulations**
  2025-05-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.08237)
  Benjamin Westrich

  <details><summary>摘要 / Abstract</summary>

  Advanced Metering Infrastructure (AMI) data from smart electric and gas meters enables valuable insights for utilities and consumers, but also raises significant privacy concerns. In California, regulatory decisions (CPUC D.11-07-056 and D.11-08-045) mandate strict privacy protections for customer energy usage data, guided by the Fair Information Practice Principles (FIPPs). We comprehensively explore solutions drawn from data anonymization, privacy-preserving machine learning (differential privacy and federated learning), synthetic data generation, and cryptographic techniques (secure multiparty computation, homomorphic encryption). This allows advanced analytics, including machine learning models, statistical and econometric analysis on energy consumption data, to be performed without compromising individual privacy. We evaluate each technique&#x27;s theoretical foundations, effectiveness, and trade-offs in the context of utility data analytics, and we propose an integrated architecture that combines these methods to meet real-world needs. The proposed hybrid architecture is designed to ensure compliance with California&#x27;s privacy rules and FIPPs while enabling useful analytics, from forecasting and personalized insights to academic research and econometrics, while strictly protecting individual privacy. Mathematical definitions and derivations are provided where appropriate to demonstrate privacy guarantees and utility implications rigorously. We include comparative evaluations of the techniques, an architecture diagram, and flowcharts to illustrate how they work together in practice. The result is a blueprint for utility data scientists and engineers to implement privacy-by-design in AMI data handling, supporting both data-driven innovation and strict regulatory compliance.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Rerandomizable Garbling, Revisited**
  2025-05-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/843)
  Raphael Heitjohann, Jonas von der Heyden, Tibor Jager

  <details><summary>摘要 / Abstract</summary>

  In key-and-message homomorphic encryption (KMHE), the key space is a subset of the message space, allowing encryption of secret keys such that the same homomorphism can be applied to both the key and the message of a given ciphertext. KMHE with suitable security properties is the main building block for constructing rerandomizable garbling schemes (RGS, Gentry et al., CRYPTO 2010), which enable advanced cryptographic applications like multi-hop homomorphic encryption, the YOSO-like MPC protocol SCALES (Acharya et al., TCC 2022 and CRYPTO 2024), and more. The BHHO scheme (Boneh et al., CRYPTO 2008) is currently the only known KMHE scheme suitable for constructing RGS. An encryption of a secret key consists of $\mathcal{O}(\lambda^{2})$ group elements, where $\lambda$ is the security parameter, which incurs a significant bandwidth and computational overhead that makes the scheme itself, and the RGS protocols building upon it, impractical. We present a new, more efficient KMHE scheme with linear-size ciphertexts. Despite using heavier cryptographic tools (pairings instead of plain DDH-hard groups), the concrete ciphertext size and computational costs are very significantly reduced. We are able to shrink the ciphertext by 97.83 % (from 16.68 MB to 360 kB) and reduce the estimated computations for encryption by 99.996 % (from 4 minutes to 0.01 seconds) in comparison to BHHO. Additionally, we introduce gate KMHE as a new tool to build more efficient RGS. Our RGS construction shrinks the size of a garbled gate by 98.99 % (from 133.43 MB to 1.35 MB) and decreases the estimated cost of garbling by 99.998 % (from 17 minutes to 0.02 seconds per gate) in comparison to Acharya et al. In summary, our work shows for the first time that RGS and the SCALES protocol (and hence YOSO-like MPC) are practically feasible for simple circuits.

  匹配依据：MPC: garbling schemes

  </details>

- **Post-Quantum Secure Decentralized Random Number Generation Protocol with Two Rounds of Communication in the Standard Model**
  2025-05-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.07536)
  Pham Nhat Minh, Khuong Nguyen-An

  <details><summary>摘要 / Abstract</summary>

  Randomness plays a vital role in numerous applications, including simulation, cryptography, distributed systems, and gaming. Consequently, extensive research has been conducted to generate randomness. One such method is to design a decentralized random number generator (DRNG), a protocol that enables multiple participants to collaboratively generate random outputs that must be publicly verifiable. However, existing DRNGs are either not secure against quantum computers or depend on the random oracle model (ROM) to achieve security. In this paper, we design a DRNG based on lattice-based publicly verifiable secret sharing (PVSS) that is post-quantum secure and proven secure in the standard model. Additionally, our DRNG requires only two rounds of communication to generate a single (pseudo)random value and can tolerate up to any t &lt; n/2 dishonest participants. To our knowledge, the proposed DRNG construction is the first to achieve all these properties.

  匹配依据：MPC: secret sharing

  </details>

- **Comet: Accelerating Private Inference for Large Language Model by Predicting Activation Sparsity**
  2025-05-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.07239)
  Guang Yan, Yuhui Zhang, Zimu Guo, Lutan Zhao, Xiaojun Chen, Chen Wang, Wenhao Wang, Dan Meng, Rui Hou

  <details><summary>摘要 / Abstract</summary>

  With the growing use of large language models (LLMs) hosted on cloud platforms to offer inference services, privacy concerns about the potential leakage of sensitive information are escalating. Secure multi-party computation (MPC) is a promising solution to protect the privacy in LLM inference. However, MPC requires frequent inter-server communication, causing high performance overhead. Inspired by the prevalent activation sparsity of LLMs, where most neuron are not activated after non-linear activation functions, we propose an efficient private inference system, Comet. This system employs an accurate and fast predictor to predict the sparsity distribution of activation function output. Additionally, we introduce a new private inference protocol. It efficiently and securely avoids computations involving zero values by exploiting the spatial locality of the predicted sparse distribution. While this computation-avoidance approach impacts the spatiotemporal continuity of KV cache entries, we address this challenge with a low-communication overhead cache refilling strategy that merges miss requests and incorporates a prefetching mechanism. Finally, we evaluate Comet on four common LLMs and compare it with six state-of-the-art private inference systems. Comet achieves a 1.87x-2.63x speedup and a 1.94x-2.64x communication reduction.

  匹配依据：MPC: secure multi party computation

  </details>

- **Standing Firm in 5G: A Single-Round, Dropout-Resilient Secure Aggregation for Federated Learning**
  2025-05-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.07148)
  Yiwei Zhang, Rouzbeh Behnia, Imtiaz Karim, Attila A. Yavuz, Elisa Bertino

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) is well-suited to 5G networks, where many mobile devices generate sensitive edge data. Secure aggregation protocols enhance privacy in FL by ensuring that individual user updates reveal no information about the underlying client data. However, the dynamic and large-scale nature of 5G-marked by high mobility and frequent dropouts-poses significant challenges to the effective adoption of these protocols. Existing protocols often require multi-round communication or rely on fixed infrastructure, limiting their practicality. We propose a lightweight, single-round secure aggregation protocol designed for 5G environments. By leveraging base stations for assisted computation and incorporating precomputation, key-homomorphic pseudorandom functions, and t-out-of-k secret sharing, our protocol ensures efficiency, robustness, and privacy. Experiments show strong security guarantees and significant gains in communication and computation efficiency, making the approach well-suited for real-world 5G FL deployments.

  匹配依据：MPC: secret sharing

  </details>

- **Row Reduction Techniques for $n$-Party Garbling**
  2025-05-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/829)
  Kelong Cong, Emmanuela Orsini, Erik Pohle, Oliver Zajonc

  <details><summary>摘要 / Abstract</summary>

  Recent advancements in maliciously secure garbling have significantly improved the efficiency of constant-round multi-party computation. Research in the field has primarily focused on reducing communication complexity through row reduction techniques and improvements to the preprocessing phase with the use of simpler correlations. In this work, we present two contributions to reduce the communication complexity of state of the art multi-party garbling with an arbitrary number of corruptions. First, we show how to achieve full row reduction for $n$-party garbled circuits in HSS17-style protocols (Hazay et al., Asiacrypt&#x27;17 &amp; JC&#x27;20) and authenticated garbling (Yang et al., CCS&#x27;20), reducing the size of the garbled circuit by 25% from $4n\kappa$ to $3n\kappa$ and from $(4n-6)\kappa$ to $3(n-1)\kappa$ bits per AND gate, respectively. Achieving row reduction in multi-party garbling has been an open problem which was partly addressed by the work of Yang et al. for authenticated garbling. In our work, we show a full row reduction for both garbling approaches, thus addressing this open problem completely. Second, drawing inspiration from the work of Dittmer et al. (Crypto 2022), we propose a new preprocessing protocol to obtain the required materials for the garbling phase using large field triples that can be generated with sublinear communication. The new preprocessing significantly reduces the communication overhead of garbled circuits. Our optimizations result in up to a $6\times$ reduction in communication compared to HSS17 and a $2.2\times$ reduction over the state of the art authenticated garbling of Yang et al. for 3 parties in a circuit with 10 million AND gates.

  匹配依据：MPC: garbled circuit, garbled circuits, multi party computation

  </details>

- **SoK: Dlog-based Distributed Key Generation**
  2025-05-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/819)
  Renas Bacho, Alireza Kavousi

  <details><summary>摘要 / Abstract</summary>

  Distributed Key Generation (DKG) protocols are fundamental components of threshold cryptography, enabling key generation in a trustless manner for a range of cryptographic operations such as threshold encryption and signing. Of particular widespread use are DKG protocols for discrete-logarithm based cryptosystems. In this Systematization of Knowledge (SoK), we present a comprehensive analysis of existing DKG protocols in the discrete-logarithm setting, with the goal of identifying cryptographic techniques and design principles that facilitate the development of secure and resilient protocols. To offer a structured overview of the literature, we adopt a modular approach and classify DKG protocols based on their underlying network assumption and cryptographic tools. These two factors determine how DKG protocols manage secret sharing and reach consensus as their essential building blocks. We also highlight various insights and suggest future research directions that could drive further advancements in this area.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy Challenges In Image Processing Applications**
  2025-05-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.04181)
  Maneesha, Bharat Gupta, Rishabh Sethi, Charvi Adita Das

  <details><summary>摘要 / Abstract</summary>

  As image processing systems proliferate, privacy concerns intensify given the sensitive personal information contained in images. This paper examines privacy challenges in image processing and surveys emerging privacy-preserving techniques including differential privacy, secure multiparty computation, homomorphic encryption, and anonymization. Key applications with heightened privacy risks include healthcare, where medical images contain patient health data, and surveillance systems that can enable unwarranted tracking. Differential privacy offers rigorous privacy guarantees by injecting controlled noise, while MPC facilitates collaborative analytics without exposing raw data inputs. Homomorphic encryption enables computations on encrypted data and anonymization directly removes identifying elements. However, balancing privacy protections and utility remains an open challenge. Promising future directions identified include quantum-resilient cryptography, federated learning, dedicated hardware, and conceptual innovations like privacy by design. Ultimately, a holistic effort combining technological innovations, ethical considerations, and policy frameworks is necessary to uphold the fundamental right to privacy as image processing capabilities continue advancing rapidly.

  匹配依据：MPC: secure multiparty computation

  </details>

- **HydraProofs: Optimally Computing All Proofs in a Vector Commitment (with applications to efficient zkSNARKs over data from multiple users)**
  2025-05-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/813)
  Christodoulos Pappas, Dimitris Papadopoulos, Charalampos Papamanthou

  <details><summary>摘要 / Abstract</summary>

  In this work, we introduce HydraProofs, the first vector commitment (VC) scheme that achieves the following two properties. (i) The prover can produce all the opening proofs for different elements (or consecutive sub-arrays) for a vector of size N in optimal time O(N). (ii) It is directly compatible with a family of zkSNARKs that encode their input as a multi-linear polynomial, i.e., our VC can be directly used when running the zkSNARK on its pre-image, without the need to open&#x27;&#x27; the entire vector pre-image inside the zkSNARK. To the best of our knowledge, all prior VC schemes either achieve (i) but are not efficiently pluggable&#x27;&#x27; into zkSNARKs (e.g., a Merkle tree commitment that requires re-computing the entire hash tree inside the circuit), or achieve (ii) but take (NlogN) time. We then combine HydraProofs with the seminal GKR protocol and apply the resulting zkSNARK in a setting where multiple users participate in a computation executed by an untrusted server and each user wants to ensure the correctness of the result and that her data was included. Our experimental evaluation shows our approach outperforms prior ones by 4-16x for prover times on general circuits. Finally, we consider two concrete application use cases, verifiable secret sharing and verifiable robust aggregation. For the former, our construction achieves the first scheme for Shamir&#x27;s secret sharing with linear time prover (lower than the time needed for the dealer computation). For the second we propose a scheme that works against misbehaving aggregators and our experiments show it can be reasonably deployed in existing schemes with minimal slow-downs.

  匹配依据：MPC: secret sharing

  </details>

- **Empc: Effective Path Prioritization for Symbolic Execution with Path Cover**
  2025-05-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.03555)
  Shuangjie Yao, Dongdong She

  <details><summary>摘要 / Abstract</summary>

  Symbolic execution is a powerful program analysis technique that can formally reason the correctness of program behaviors and detect software bugs. It can systematically explore the execution paths of the tested program. But it suffers from an inherent limitation: path explosion. Path explosion occurs when symbolic execution encounters an overwhelming number (exponential to the program size) of paths that need to be symbolically reasoned. It severely impacts the scalability and performance of symbolic execution. To tackle this problem, previous works leverage various heuristics to prioritize paths for symbolic execution. They rank the exponential number of paths using static rules or heuristics and explore the paths with the highest rank. However, in practice, these works often fail to generalize to diverse programs. In this work, we propose a novel and effective path prioritization technique with path cover, named Empc. Our key insight is that not all paths need to be symbolically reasoned. Unlike traditional path prioritization, our approach leverages a small subset of paths as a minimum path cover (MPC) that can cover all code regions of the tested programs. To encourage diversity in path prioritization, we compute multiple MPCs. We then guide the search for symbolic execution on the small number of paths inside multiple MPCs rather than the exponential number of paths. We implement our technique Empc based on KLEE. We conduct a comprehensive evaluation of Empc to investigate its performance in code coverage, bug findings, and runtime overhead. The evaluation shows that Empc can cover 19.6% more basic blocks than KLEE&#x27;s best search strategy and 24.4% more lines compared to the state-of-the-art work cgs. Empc also finds 24 more security violations than KLEE&#x27;s best search strategy. Meanwhile, Empc can significantly reduce the memory usage of KLEE by up to 93.5%.

  匹配依据：MPC: mpc (context)

  </details>

- **Optimistic, Signature-Free Reliable Broadcast and Its Applications**
  2025-05-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.02761)
  Nibesh Shrestha, Qianyu Yu, Aniket Kate, Giuliano Losa, Kartik Nayak, Xuechao Wang

  <details><summary>摘要 / Abstract</summary>

  Reliable broadcast (RBC) is a key primitive in fault-tolerant distributed systems, and improving its efficiency can benefit a wide range of applications. This work focuses on signature-free RBC protocols, which are particularly attractive due to their computational efficiency. Existing protocols in this setting incur an optimal 3 steps to reach a decision while tolerating up to $f &lt; n/3$ Byzantine faults, where $n$ is the number of parties. In this work, we propose an optimistic RBC protocol that maintains the $f &lt; n/3$ fault tolerance but achieves termination in just 2 steps under certain optimistic conditions--when at least $\lceil \frac{n+2f-2}{2} \rceil$ non-broadcaster parties behave honestly. We also prove a matching lower bound on the number of honest parties required for 2-step termination. We show that our latency-reduction technique generalizes beyond RBC and applies to other primitives such as asynchronous verifiable secret sharing (AVSS) and asynchronous verifiable information dispersal (AVID), enabling them to complete in 2 steps under similar optimistic conditions. To highlight the practical impact of our RBC protocol, we integrate it into Sailfish++, a new signature-free, post-quantum secure DAG-based Byzantine fault-tolerant (BFT) consensus protocol. Under optimistic conditions, this protocol achieves a commit latency of 3 steps--matching the performance of the best signature-based protocols. Our experimental evaluation shows that our protocol significantly outperforms existing post-quantum secure and signature-based protocols, even on machines with limited CPU resources. In contrast, signature-based protocols require high CPU capacity to achieve comparable performance. We have open-sourced our Rust implementation of Sailfish++ to facilitate reproducible results.

  匹配依据：MPC: secret sharing

  </details>

- **Accelerating Multiparty Noise Generation Using Lookups**
  2025-05-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/805)
  Fredrik Meisingseth, Christian Rechberger, Fabian Schmid

  <details><summary>摘要 / Abstract</summary>

  We propose a novel method for using lookup tables (LUTs) in multiparty noise sampling which allows using smaller and/or fewer LUTs compared to previous work (Franzese et al., CCS&#x27;25, and Kii et al., PETS&#x27;25), leading to efficiency improvements of several orders of magnitude. This is primarily achieved by not evaluating the LUTs at uniformly random indices but rather using a non-uniform index distribution that can be sampled efficiently. Our method is largely distribution-agnostic, and we demonstrate its flexibility by approximating the discrete Laplace and Gaussian distributions (for a wide range of parameters) to a negligible statistical distance. Our concrete implementation, based on 3-party replicated secret sharing, achieves sub-kilobyte communication and millisecond-level computation. Amortized over 1000 discrete Laplace or Gaussian ($\sigma \leq 1000$) samples, we require just 619 bytes of communication (constituting over two orders of magnitude less communication than all previous work) and under 2 ms per party in the semi-honest setting, in all considered network configurations. With recently proposed batched multiplication checks, the malicious setting adds less than 1 byte and 5 ms per sample (amortized). Offering potential independent value, our open-source implementation also extends LUT communication trade-offs (Morita et al., USENIX&#x27;25), thus enabling more efficient evaluation of larger LUTs. Further, the merits of our sampling method are not contingent on the above MPC setting and we give analytical performance estimations for use with other MPC machinery, which indicate that it widely is a competitive alternative, especially for somewhat concentrated distributions.

  匹配依据：MPC: secret sharing

  </details>

- **Scrutinizing the Security of AES-based Hashing and One-way Functions**
  2025-05-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/792)
  Shiyao Chen, Jian Guo, Eik List, Danping Shi, Tianyu Zhang

  <details><summary>摘要 / Abstract</summary>

  AES has cemented its position as the primary symmetric-key primitive for a wide range of cryptographic applications, which motivates the analysis on the concrete security of AES in practical instantiations, for instance, the collision resistance of AES-based hashing, the key commitment security of AES-based authenticated encryption schemes, and the one-wayness of AES-based one-way functions in MPC/ZK protocols. In this work, we further advance the meet-in-the-middle (MITM) attack framework on AES-like constructions. We introduce single-color initial structure (SCIS), which leverages new structural insights to reduce the complexity of neutral word generation, a critical bottleneck in MITM attacks. As a result, we yield a series of improved results on AES over the state-of-the-art, including the first classical one-block collision attack on 7-round AES-MMO/MP, marking the first round advancement in over a decade and matching the best attack round in the quantum setting, as well as the first one-block collision attack on 4-round AES-128-DM, bridging the gap highlighted by Taiyama et al. at Asiacrypt 2024 from a non-differential-based approach. Additionally, we provide a comprehensive list of new results on the security margins of AES-192, AES-256, Rijndael-192, and Rijndael-256 in multiple attack settings.

  匹配依据：MPC: mpc (context)

  </details>

- **Preprocessing for Life: Dishonest-Majority MPC with a Trusted or Untrusted Dealer**
  2025-05-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/787)
  Elette Boyle, Niv Gilboa, Matan Hamilis, Yuval Ishai, Ariel Nof

  <details><summary>摘要 / Abstract</summary>

  We put forth a new paradigm for practical secure multiparty computation (MPC) in the preprocessing model, where a feasible one-time setup can enable a lifetime of efficient online secure computations. Our protocols match the security guarantees and low costs of the cheapest category of MPC solutions, namely 3-party protocols (3PC) secure against a single malicious party, with the qualitative advantages that one party communicates data sublinear in the circuit size, and can go offline after its initial messages. This &quot;2+1&quot;-party structure can alternatively be instantiated between 2 parties with the aid of a (possibly untrusted) dealer. Within such existing protocols, we provide comparable online performance while improving the storage and offline dealer-to-party communication requirements by more than 3 orders of magnitude. At the technical level, we build on a novel combination of the Fully Linear Interactive Oracle Proof (FLIOP)-based protocol design of Boyle et al. (CRYPTO 2021) and pseudorandom correlation generators. We provide an extensive assortment of algorithmic and implementation-level optimizations, design efficient distributed proofs of well-formedness of complex FLIOP correlations, and make them circuit-independent. We implement and benchmark our end-to-end system against the state of the art in the $(2+1)$ regime, a dealer-aided variant of SPDZ for Boolean circuits. We additionally extend our techniques to the $(n+1)$ party setting, where a dealer aids general dishonest-majority MPC, and provide a variant of the protocol which further achieves security with identifiable abort.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Publicly Auditable Garbled Circuit**
  2025-04-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/772)
  San Ling, Chan Nam Ngo, Khai Hanh Tang, Huaxiong Wang

  <details><summary>摘要 / Abstract</summary>

  Advanced cryptographic primitives such as zero-knowledge proofs (ZKPs) have seen an emerging trend in adoption by blockchain applications. However, ZKPs only allow a single prover to convince a verifier of a correct evaluation of a computation over the prover&#x27;s secret input. This is insufficient if the applications require shared private state from more than one party. In this case, one can adopt secure multiparty computation (MPC), which allows a set of mutually distrustful parties to jointly compute a global function while keeping their respective inputs private. Generic MPC, including secret-sharing and garbled-circuit techniques that allow the participants, without deep expertise in cryptography, to define the computation as a circuit, is an important tool in privacy-preserving protocols. Yet, generic MPC mostly focuses on malicious security in which the computed result is verifiable only among the computing parties, but not publicly verifiable. In blockchain applications, public verifiability is important, as the consensus protocol is not just among the computing parties but also public verifiers. Several works have attempted to bridge this gap, albeit not in the blockchain realm, i.e., publicly auditable MPC. Nevertheless, they are non-constant round protocols and only for secret-sharing MPC, i.e., round complexity scales linearly with the circuit multiplicative depth, while round latency is an important cost metric for blockchains. We address this problem by providing a Publicly Auditable Garbled Circuit protocol that is maliciously secure, publicly auditable, and constant-round. Our protocol is efficient, with minimal overhead in terms of the number of rounds, communication, and public transcript size.

  匹配依据：MPC: garbled circuit, secret sharing, secure multiparty computation

  </details>

- **Exploring Adversarial Attacks on the MaSTer Truncation Protocol**
  2025-04-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/773)
  Martin Zbudila, Aysajan Abidin, Bart Preneel

  <details><summary>摘要 / Abstract</summary>

  At CANS 2024, Zbudila et al. presented MaSTer, a maliciously secure multi-party computation protocol for truncation. It allows adversaries to manipulate outputs with a bounded additive error while avoiding detection with a certain probability. In this work, we analyse the broader implications of adversarial exploitation in probabilistic truncation protocols, specifically in relation to MaSTer. We propose three attack strategies aimed at inducing misclassification in deep neural network (DNN) inference. Our empirical evaluation across multiple datasets demonstrates that while adversarial influence remains negligible under realistic constraints, certain configurations and network architectures exhibit increased vulnerability. By improving the understanding of the risks associated with probabilistic truncation protocols in privacy-preserving machine learning, our work demonstrates that the MaSTer protocol is robust in realistic settings.

  匹配依据：MPC: secure multi party computation

  </details>

- **AuthOr: Lower Cost Privacy-Free Garbling of Arbitrary Boolean Circuits**
  2025-04-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.18387) · [IACR ePrint](https://eprint.iacr.org/2025/775)
  Osman Biçer, Ali Ajorian

  <details><summary>摘要 / Abstract</summary>

  Privacy-free garbling schemes of Frederiksen et al. (Eurocrypt ’15) are designed to satisfy only the authenticity criterion of Bellare et al. (ACM CCS ’12) and to be more efficient than full-fledged garbling schemes. In this work, we improve the state-of-the-art privacy-free version of half-gates (HG) garbling of Zahur et al. (Crypto ’15) by allowing an AND gate to be garbled with zero ciphertexts whenever at least one of its input wires is freely settable by the garbler. Our full solution, AuthOr, then combines the ideas from the information-theoretic garbling of Kondi and Patra (Crypto ’17) with the improved HG-based scheme we obtain. AuthOr has a lower communication cost (i.e., garbled-circuit size) than HG garbling without any additional security assumptions. Theoretically, AuthOr’s garbled-circuit size reduction over HG garbling ranges from 0% to 100%, with the exact improvement depending on the circuit structure. We have implemented our scheme and evaluated it on various circuits constructed by independent researchers. Our experimental results show that, in practice, the garbled-circuit size reduction can reach roughly 98%.

  匹配依据：MPC: garbled circuit, garbling schemes

  </details>

- **Security of a secret sharing protocol on the Qline**
  2025-04-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.19702) · [IACR ePrint](https://eprint.iacr.org/2025/764)
  Alex B. Grilo, Lucas Hanouz, Anne Marin

  <details><summary>摘要 / Abstract</summary>

  Secret sharing is a fundamental primitive in cryptography, and it can be achieved even with perfect security. However, the distribution of shares requires computational assumptions, which can compromise the overall security of the protocol. While traditional Quantum Key Distribution (QKD) can maintain security, its widespread deployment in general networks would incur prohibitive costs. In this work, we present a quantum protocol for distributing additive secret sharing of 0, which we prove to be composably secure within the Abstract Cryptography framework. Moreover, our protocol targets the Qline, a recently proposed quantum network architecture designed to simplify and reduce the cost of quantum communication. Once the shares are distributed, they can be used to securely perform a wide range of cryptographic tasks, including standard additive secret sharing, anonymous veto, and symmetric key establishment.

  匹配依据：MPC: secret sharing

  </details>

- **Federated One-Shot Learning with Data Privacy and Objective-Hiding**
  2025-04-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.21182)
  Maximilian Egger, Rüdiger Urbanke, Rawad Bitar

  <details><summary>摘要 / Abstract</summary>

  Privacy in federated learning is crucial, encompassing two key aspects: safeguarding the privacy of clients&#x27; data and maintaining the privacy of the federator&#x27;s objective from the clients. While the first aspect has been extensively studied, the second has received much less attention. We present a novel approach that addresses both concerns simultaneously, drawing inspiration from techniques in knowledge distillation and private information retrieval to provide strong information-theoretic privacy guarantees. Traditional private function computation methods could be used here; however, they are typically limited to linear or polynomial functions. To overcome these constraints, our approach unfolds in three stages. In stage 0, clients perform the necessary computations locally. In stage 1, these results are shared among the clients, and in stage 2, the federator retrieves its desired objective without compromising the privacy of the clients&#x27; data. The crux of the method is a carefully designed protocol that combines secret-sharing-based multi-party computation and a graph-based private information retrieval scheme. We show that our method outperforms existing tools from the literature when properly adapted to this setting.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Differentially Private Secure Multiplication with Erasures and Adversaries**
  2025-04-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.21178)
  Haoyang Hu, Viveck R. Cadambe

  <details><summary>摘要 / Abstract</summary>

  We consider a private distributed multiplication problem involving N computation nodes and T colluding nodes. Shamir&#x27;s secret sharing algorithm provides perfect information-theoretic privacy, while requiring an honest majority, i.e., N \ge 2T + 1. Recent work has investigated approximate computation and characterized privacy-accuracy trade-offs for the honest minority setting N \le 2T for real-valued data, quantifying privacy leakage via the differential privacy (DP) framework and accuracy via the mean squared error. However, it does not incorporate the error correction capabilities of Shamir&#x27;s secret-sharing algorithm. This paper develops a new polynomial-based coding scheme for secure multiplication with an honest minority, and characterizes its achievable privacy-utility tradeoff, showing that the tradeoff can approach the converse bound as closely as desired. Unlike previous schemes, the proposed scheme inherits the capability of the Reed-Solomon (RS) code to tolerate erasures and adversaries. We utilize a modified Berlekamp-Welch algorithm over the real number field to detect adversarial nodes.

  匹配依据：MPC: secret sharing

  </details>

- **Threshold Niederreiter: Chosen-Ciphertext Security and Improved Distributed Decoding**
  2025-04-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/757)
  Pascal Giorgi, Fabien Laguillaumie, Lucas Ottow, Damien Vergnaud

  <details><summary>摘要 / Abstract</summary>

  Threshold public-key encryption securely distributes private key shares among multiple participants, requiring a minimum number of them to decrypt messages. We introduce a quantum-resistant threshold public-key encryption scheme based on the code-based Niederreiter cryptosystem that achieves security against chosen ciphertext attacks. A previous attempt was made recently by Takahashi, Hashimoto, and Ogata (published at DCC in 2023) but we show that it contains a critical security flaw that allow adversaries to exploit malformed ciphertexts to gain information about the secret key. In this work, we formalize a generic conversion enhancing security of (classical) public-key encryption from one-wayness against passive attacks to indistinguishability against chosen-ciphertext attacks. The conversion uses a non-interactive zero-knowledge argument with strong security properties to ensure ciphertext well-formedness. We then provide an instantiation for Niederreiter encryption based on recent techniques introduced in the &quot;MPC-in-the-head&quot; paradigm. The publicly verifiable validity of ciphertexts makes this scheme suitable for threshold public-key encryption and prevents an attack similar to the one on Takahashi-Hashimoto-Ogata scheme. To improve the multi-party computation protocol for decryption (involving secure computations on polynomials), we introduce a field-switching technique that allows to significantly reduce the shared secret key size and computational overhead.

  匹配依据：MPC: multi party computation

  </details>

- **Secret Sharing for DNA Probability Vectors**
  2025-04-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.18970)
  Wenkai Zhang, Zhiying Wang

  <details><summary>摘要 / Abstract</summary>

  Emerging DNA storage technologies use composite DNA letters, where information is represented by a probability vector, leading to higher information density and lower synthesis costs. However, it faces the problem of information leakage in sharing the DNA vessels among untrusted vendors. This paper introduces an asymptotic ramp secret sharing scheme (ARSSS) for secret information storage using composite DNA letters. This innovative scheme, inspired by secret sharing methods over finite fields and enhanced with a modified matrix-vector multiplication operation for probability vectors, achieves asymptotic information-theoretic data security for a large alphabet size. Moreover, this scheme reduces the number of reading operations for DNA samples compared to traditional schemes, and therefore lowers the complexity and the cost of DNA-based secret sharing. We further explore the construction of the scheme, starting with a proof of the existence of a suitable generator, followed by practical examples. Finally, we demonstrate efficient constructions to support large information sizes, which utilize multiple vessels for each secret share rather than a single vessel.

  匹配依据：MPC: secret sharing

  </details>

- **Secret Sharing in the Rank Metric**
  2025-04-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.18294)
  Johan Vester Dinesen, Eimear Byrne, Ragnar Freij-Hollanti, Camilla Hollanti

  <details><summary>摘要 / Abstract</summary>

  The connection between secret sharing and matroid theory is well established. In this paper, we generalize the concepts of secret sharing and matroid ports to $q$-polymatroids. Specifically, we introduce the notion of an access structure on a vector space, and consider properties related to duality, minors, and the relationship to $q$-polymatroids. Finally, we show how rank-metric codes give rise to secret sharing schemes within this framework.

  匹配依据：MPC: secret sharing

  </details>

- **Anti-adversarial Learning: Desensitizing Prompts for Large Language Models**
  2025-04-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.01273)
  Xuan Li, Zhe Yin, Xiaodong Gu, Beijun Shen

  <details><summary>摘要 / Abstract</summary>

  With the widespread use of LLMs, preserving privacy in user prompts has become crucial, as prompts risk exposing privacy and sensitive data to the cloud LLMs. Traditional techniques like homomorphic encryption, secure multi-party computation, and federated learning face challenges due to heavy computational costs and user participation requirements, limiting their applicability in LLM scenarios. In this paper, we propose PromptObfus, a novel method for desensitizing LLM prompts. The core idea of PromptObfus is &quot;anti-adversarial&quot; learning, which perturbs privacy words in the prompt to obscure sensitive information while retaining the stability of model predictions. Specifically, PromptObfus frames prompt desensitization as a masked language modeling task, replacing privacy-sensitive terms with a [MASK] token. A desensitization model is trained to generate candidate replacements for each masked position. These candidates are subsequently selected based on gradient feedback from a surrogate model, ensuring minimal disruption to the task output. We demonstrate the effectiveness of our approach on three NLP tasks. Results show that PromptObfus effectively prevents privacy inference from remote LLMs while preserving task performance.

  匹配依据：MPC: secure multi party computation

  </details>

- **Silenzio: Secure Non-Interactive Outsourced MLP Training**
  2025-04-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.17785)
  Jonas Sander, Thomas Eisenbarth

  <details><summary>摘要 / Abstract</summary>

  Outsourcing ML training to cloud-service-providers presents a compelling opportunity for resource constrained clients, while it simultaneously bears inherent privacy risks. We introduce Silenuio, the first fully non-interactive outsourcing scheme for the training of MLPs that achieves 128bit security using FHE (precisely TFHE). Unlike traditional MPC-based protocols that necessitate interactive communication between the client and server(s) or non-collusion assumptions among multiple servers, Silenzio enables the &quot;fire-and-forget&quot; paradigm without such assumptions. In this approach, the client encrypts the training data once, and the server performs the training without any further interaction. Silenzio operates entirely over low-bitwidth integer to mitigate the computational overhead inherent to FHE. Our approach features a novel low-bitwidth matrix multiplication gadget that leverages input-dependent residue number systems, ensuring that no intermediate value overflows 8bit. Starting from an RNS-to-MRNS conversion process, we propose an efficient block-scaling mechanism, which approximately shifts encrypted tensor values to their user-specified most significant bits. To instantiate the backpropagation of the error, Silenzio introduces a low-bitwidth gradient computation for the cross-entropy loss. We evaluate Silenzio on standard MLP training tasks regarding runtime as well as model performance and achieve similar classification accuracy as MLPs trained using PyTorch with 32bit floating-point computations. Our open-source implementation of Silenzio represents a significant advancement in privacy-preserving ML, providing a new baseline for secure and non-interactive outsourced MLP training.

  匹配依据：MPC: mpc (context)

  </details>

- **Secure Network Function Computation for Linear Functions, Part II: Target-Function Security**
  2025-04-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.17514)
  Yang Bai, Xuan Guang, Raymond W. Yeung

  <details><summary>摘要 / Abstract</summary>

  In this Part II of a two-part paper, we put forward secure network function computation, where in a directed acyclic network, a sink node is required to compute a target function of which the inputs are generated as source messages at multiple source nodes, while a wiretapper, who can access any one but not more than one wiretap set in a given collection of wiretap sets, is not allowed to obtain any information about a security function of the source messages. In Part I of the two-part paper, we have investigated securely computing linear functions with the wiretapper who can eavesdrop any edge subset up to a certain size r, referred to as the security level, where the security function is the identity function. The notion of this security is called source security. In the current paper, we consider another interesting model which is the same as the above one except that the security function is identical to the target function, i.e., we need to protect the information on the target function from being leaked to the wiretapper. The notion of this security is called target-function security. We first prove a non-trivial upper bound on the secure computing capacity, which is applicable to arbitrary network topologies and arbitrary security levels. In particular, when the security level r is equal to 0, the upper bound reduces to the computing capacity without security consideration. Further, from an algebraic point of view, we prove two equivalent conditions for target-function security and source security for the existence of the corresponding linear function-computing secure network codes. With them, for any linear function over a given finite field, we develop a code construction of linear secure network codes for target-function security and thus obtain a lower bound on the secure computing capacity; and also generalize the code construction developed in Part I for source security.

  匹配依据：MPC: secure computing

  </details>

- **Resource Reduction in Multiparty Quantum Secret Sharing of both Classical and Quantum Information under Noisy Scenario**
  2025-04-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.16709)
  Nirupam Basak, Goutam Paul

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) enables secure distribution of information among multiple parties but remains vulnerable to noise. We analyze the effects of bit-flip, phase-flip, and amplitude damping noise on the multiparty QSS for classical message (QSSCM) and secret sharing of quantum information (SSQI) protocols proposed by Zhang et al. (Phys. Rev. A, 71:044301, 2005). To scale down these effects, we introduce an efficient quantum error correction (QEC) scheme based on a simplified version of Shor&#x27;s code. Leveraging the specific structure of the QSS protocols, we reduce the qubit overhead from the standard 9 of Shor&#x27;s code to as few as 3 while still achieving lower average error rates than existing QEC methods. Thus, our approach can also be adopted for other single-qubit-based quantum protocols. Simulations demonstrate that our approach significantly enhances the protocols&#x27; resilience, improving their practicality for real-world deployment.

  匹配依据：MPC: secret sharing

  </details>

- **One-Step Schnorr Threshold Identification**
  2025-04-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/722)
  Foteinos Mergoupis-Anagnou

  <details><summary>摘要 / Abstract</summary>

  Threshold cryptographic primitives have not been widely adopted in real-world distributed systems (i.e., beyond the closed committee model) presumably due to state-synchronization overhead and complex certification processes for the shareholders. These are both aspects of their overreliance on infrastructure, an assumption that is usually glossed over in their design. In this work, we propose OSST, a real-time threshold identification protocol that achieves non-interactivity and non-reliance on public shares by means of direct proof interpolation. Given a Shamir $(n, t)$-shared secret $x$, the proposed scheme allows any $t^* \ge t$ (but no less) shareholders to prove over designated communication channels that their key shares interpolate to $x$ without revealing any information beyond that. Provers do not engage in distributed computations, sending their packets to the verifier asynchronously; conversely, verifiers need only know the combined public key $y \equiv g ^ x$, without need to pre-validate and register the individual member identities. The protocol is intended for use in permissionless or unmanaged meshes that lack both overlay networks and trust infrastructure or governance, a use case space that has been tacitly neglected as &#x27;&#x27;niche&#x27;&#x27; by the current mainstream. No publicly verifiable setup is required beyond distributing $x$ according to Shamir&#x27;s secret sharing (or equivalent distributed key generation scheme) and advertising its public counterpart; in particular, the protocol is intended to be secure against impersonation without relying on the auditability of any advertised public shares. We provide evidence that this has good chances to hold true by giving a reasonably restricted security proof in the random oracle model under the one-more discrete-logarithm (OMDL) hardness assumption.

  匹配依据：MPC: secret sharing

  </details>

- **Kronecker states: a powerful source of multipartite maximally entangled states in quantum information**
  2025-04-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.16256)
  Walther Gonzalez

  <details><summary>摘要 / Abstract</summary>

  In quantum information theory, maximally entangled states, specifically locally maximally entangled (LME) states, are essential for quantum protocols. While many focus on bipartite entanglement, applications such as quantum error correction and multiparty secret sharing rely on multipartite entanglement. These LME states naturally appear in the invariant subspaces of tensor products of irreducible representations of the symmetric group $S_n$, called Kronecker subspaces, whose dimensions are the Kronecker coefficients. A Kronecker subspace is a space of multipartite LME states that entangle high-dimensional Hilbert spaces. Although these states can be derived from Clebsch-Gordan coefficients of $S_n$, known methods are inefficient even for small $n$. A quantum-information-based alternative comes from entanglement concentration protocols, where Kronecker subspaces arise in the isotypic decomposition of multiple copies of entangled states. Closed forms have been found for the multiqubit $W$-class states, but not in general. This thesis extends that approach to any multiqubit system. We first propose a graphical construction called W-state Stitching, where multiqubit entangled states are represented as tensor networks built from $W$ states. By analyzing the isotypic decomposition of copies of these graph states, corresponding graph Kronecker states can be constructed. In particular, graph states of generic multiqubit systems can generate any Kronecker subspace. We explicitly construct bases for three- and four-qubit systems and show that the W-stitching technique also serves as a valuable tool for multiqubit entanglement classification. These results may open new directions in multipartite entanglement resource theories, with bipartite and tripartite $W$ states as foundational elements, and asymptotic analysis based on Kronecker states.

  匹配依据：MPC: secret sharing

  </details>

- **Publicly Verifiable Secret Sharing: Generic Constructions and Lattice-Based Instantiations in the Standard Model**
  2025-04-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.14381)
  Pham Nhat Minh, Khoa Nguyen, Willy Susilo, Khuong Nguyen-An

  <details><summary>摘要 / Abstract</summary>

  Publicly verifiable secret sharing (PVSS) allows a dealer to share a secret among a set of shareholders so that the secret can be reconstructed later from any set of qualified participants. In addition, any public verifier should be able to check the correctness of the sharing and reconstruction process. PVSS has been demonstrated to yield various applications, such as e-voting, distributed key generation, decentralized random number generation protocols, and multi-party computation. Although many concrete PVSS protocols have been proposed, their security is either proven in the random oracle model or relies on quantum-vulnerable assumptions such as factoring or discrete logarithm. In this work, we put forward a generic construction for PVSS that can be instantiated in the standard model under the Learning With Errors (LWE) assumption. Our instantiation provides the first post-quantum PVSS in the standard model, with a reasonable level of asymptotic efficiency.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Two Party Secret Shared Joins**
  2025-04-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/702)
  Srinivasan Raghuraman, Peter Rindal, Harshal Shah

  <details><summary>摘要 / Abstract</summary>

  We present concrete techniques for adapting the protocols of Mohassel et al (CCS 2020) and Badrinarayanan et al (CCS 2022) for compute SQL-like querying operations on secret shared database tables to the two party setting. The afore mentioned protocols are presented in a generic setting with access to certain idealized functionalities, e.g. secret shared permutations. However, they only instantiate their protocols in the honest majority three party setting due to other settings being considered too inefficient. We show that this is no longer the case. In particular, the recent work of Peceny et al. (eprint 2024) gives a concretely efficient two party permutation protocol. Additionally, we give a new and highly efficient protocol for evaluating the strong PRF recently proposed by Alamati et al. (Crypto 2024). Building on these advancements, along with a variety of protocol improvements and significant cryptographic engineering, our open source implementation demonstrate concretely efficient two party SQL-like querying functionality on secret shared data. We focus on the two party setting with secret shared input and output tables. The first protocol $\Pi_\textsf{Join-OO}$ is designed for the setting where the join keys are unique, similar to Private Set Intersection (PSI) except that the inputs and output are secret shared. This protocol is constant round and $O(n)$ running time. The secret protocol $\Pi_\textsf{Join-OM}$ allows one of the tables to contain repeating join keys. Our instantiations achieves $O(n\log n)$ running time and $O(\log n)$ rounds of interaction.

  匹配依据：MPC: private set intersection

  </details>

- **Documentation on Encrypted Dynamic Control Simulation Code using Ring-LWE based Cryptosystems**
  2025-04-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.13403) · [Code](https://github.com/CDSL-EncryptedControl/CDSL)
  Yeongjun Jang, Joowon Lee, Junsoo Kim

  <details><summary>摘要 / Abstract</summary>

  Encrypted controllers offer secure computation by employing modern cryptosystems to execute control operations directly over encrypted data without decryption. However, incorporating cryptosystems into dynamic controllers significantly increases the computational load. This paper aims to provide an accessible guideline for running encrypted controllers using an open-source library Lattigo, which supports an efficient implementation of Ring-Learing With Errors (LWE) based encrypted controllers, and our explanations are assisted with example codes that are fully available at https://github.com/CDSL-EncryptedControl/CDSL.

  匹配依据：MPC: secure computation

  </details>

- **Threshold (Fully) Homomorphic Encryption**
  2025-04-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/699)
  Carl Bootland, Kelong Cong, Daniel Demmler, Tore Kasper Frederiksen, Benoit Libert, Jean-Baptiste Orfila, Dragos Rotaru, Nigel P. Smart, Titouan Tanguy, Samuel Tap, Michael Walter

  <details><summary>摘要 / Abstract</summary>

  This document is a preliminary version of what is intended to be submitted to NIST by Zama as part of their threshold call. The document also serves as partial documentation of the protocols used in the Zama MPC system for threshold TFHE. However, note that the Zama software includes many optimizations built on top of the simple specifications given here. In particular the TFHE parameters given here are larger than those used by the Zama software. This is because the Zama TFHE library contains optimizations which are beyond the scope of this document. Thus the parameters given in this document are compatible with the description of TFHE given here, and take no account of the extra optimizations in the Zama software. Also note that we describe more protocols than that provided in the Zama software. In particular this document describes BGV and BFV threshold implementations, MPC-in-the-Head based proofs of correct encryption. We present mechanisms to perform robust threshold key generation and decryption for Fully Homomorphic Encryption schemes such as BGV, BFV and TFHE, in the case of super honest majority, t &lt; n/3, or t &lt; n/4, in the presence of malicious adversaries. The main mechanism for threshold decryptions follow the noise flooding principle, which we argue is sufficient for BGV and BFV. For TFHE a more subtle technique is needed to apply noise flooding, since TFHE parameters are small. To deal with all three FHE scheme, and obtain a unified framework for all such schemes, we are led to consider secret sharing over Galois Rings and not just finite fields. We consider two sets of threshold profiles, depending on whether binomial(n,t) is big or small. In the small case we obtain for all schemes an asynchronous protocol for robust threshold decryption, and we obtain a robust synchronous protocol for threshold key generation; both with t &lt; n/3. For the large case we only support TFHE, and our protocols require an “offline phase” which requires synchronous networks and can “only” tolerate t &lt; n/4. The threshold key generation operation, and the above mentioned offline phase, require access to a generic offline MPC functionality over arbitrary Galois Rings. This functionality is fully specified here. Finally, we present Zero-Knowledge proof techniques for proving the valid encryption of an FHE ciphertext. These proofs are important in a number of application contexts.

  匹配依据：MPC: secret sharing

  </details>

- **Fherret: Proof of FHE Correct-and-Honest Evaluation with Circuit Privacy from MPCitH**
  2025-04-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/700)
  Janik Huth, Antoine Joux, Giacomo Santato

  <details><summary>摘要 / Abstract</summary>

  The major Fully Homomorphic Encryption (FHE) schemes guarantee the privacy of the encrypted message only in the honest-but-curious setting, when the server follows the protocol without deviating. However, various attacks in the literature show that an actively malicious server can recover sensitive information by executing incorrect functions, tampering with ciphertexts, or observing the client’s reaction during decryption. Existing integrity solutions for FHE schemes either fail to guarantee circuit privacy, exposing the server&#x27;s computations to the client, or introduce significant computational overhead on the prover by requiring proofs of FHE operations on ciphertexts. In this work, we present Fherret, a novel scheme leveraging the MPC-in-the-Head (MPCitH) paradigm to provide a proof of correct-and-honest homomorphic evaluation while preserving circuit privacy. This proof guarantees that the client can safely decrypt the ciphertext obtained from the server without being susceptible to reaction-based attacks, such as verification and decryption oracle attacks. Additionally, this proof guarantees that the server’s evaluation maintains correctness, thereby protecting the client from $\mathsf{IND}\text{-}\mathsf{CPA}^{\mathsf{D}}$-style attacks. Our solution achieves a prover overhead of $4\lambda$ homomorphic evaluations of random functions from the function space $\mathcal{F}$, while retaining a competitive verifier overhead of $2 \lambda$ homomorphic evaluations and a communication size proportional to $\sqrt{2\lambda}$ times the size of a function from $\mathcal{F}$. Furthermore, Fherret is inherently parallelizable, achieving a parallel computation overhead similar to a homomorphic evaluation of a random function from $\mathcal{F}$ for both the prover and the verifier.

  匹配依据：MPC: mpc (context)

  </details>

- **Consecutive Measurement Tradeoffs in Quantum Cryptography**
  2025-04-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.12754)
  Chen-Xun Weng, Minglong Qin, Yanglin Hu, Marco Tomamichel

  <details><summary>摘要 / Abstract</summary>

  Measuring a quantum system can reveal information while disturbing its state. Consequently, the probabilities of obtaining desired outcomes in individual measurements constrain the probability of obtaining them in sequence. This interplay arises naturally in mistrustful quantum cryptography, where a dishonest participant may perform sequential measurements to extract more information than the protocol allows. We develop consecutive measurement theorems (CMTs) to quantify this constraint, relating the average success probability of a single measurement to that of an ordered pair of distinct measurements. For measurements on a common state, we derive the optimal lower bound on consecutive-measurement success as a function of single-measurement success and provide matching constructions over the entire parameter range. We also establish the first robust CMTs for measurements on different but nearby states, with closeness quantified by fidelity or trace distance. We use these results to strengthen sum-binding guarantees for relativistic bit commitment and soundness bounds for relativistic zero-knowledge proofs, and to obtain improved no-go results for quantum oblivious transfer and quantum private query. Our results establish CMTs as a versatile tool for translating consecutive-measurement constraints into concrete cryptographic bounds and suggest applications in other quantum-information settings.

  匹配依据：MPC: oblivious transfer

  </details>

- **Trilithium: Efficient and Universally Composable Distributed ML-DSA Signing**
  2025-04-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/675)
  Antonín Dufka, Semjon Kravtšenko, Peeter Laud, Nikita Snetkov

  <details><summary>摘要 / Abstract</summary>

  In this paper, we present Trilithium: a protocol for distributed key generation and signing compliant with FIPS 204 (ML-DSA). Our protocol allows two parties, ``server&#x27;&#x27; and ``phone&#x27;&#x27; with assistance of correlated randomness provider (CRP) to produce a standard ML-DSA signature. We prove our protocol to be secure against a malicious server or phone in the universal composability model, introducing some novel techniques to argue the security of two-party secure computation protocols with active security against one party, but only active privacy against the other. We provide an implementation of our protocol in Rust and benchmark it, showing the practicality of the protocol. As additional contribution, we propose an actively secure generalization of Attrapadung et al. (ASIA CCS ’22) comparison protocol and a new rounding protocol for fractions with private numerator.

  匹配依据：MPC: secure computation

  </details>

- **Optimal Graph Stretching for Distributed Averaging**
  2025-04-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.10289)
  Florine W. Dekker, Zekeriya Erkin, Mauro Conti

  <details><summary>摘要 / Abstract</summary>

  The performance of distributed averaging depends heavily on the underlying topology. In various fields, including compressed sensing, multi-party computation, and abstract graph theory, graphs may be expected to be free of short cycles, i.e. to have high girth. Though extensive analyses and heuristics exist for optimising the performance of distributed averaging in general networks, these studies do not consider girth. As such, it is not clear what happens to convergence time when a graph is stretched to a higher girth. In this work, we introduce the optimal graph stretching problem, wherein we are interested in finding the set of edges for a particular graph that ensures optimal convergence time under constraint of a minimal girth. We compare various methods for choosing which edges to remove, and use various convergence heuristics to speed up the searching process. We generate many graphs with varying parameters, stretch and optimise them, and measure the duration of distributed averaging. We find that stretching by itself significantly increases convergence time. This decrease can be counteracted with a subsequent repair phase, guided by a convergence time heuristic. Existing heuristics are capable, but may be suboptimal.

  匹配依据：MPC: multi party computation

  </details>

- **Lightweight Trustworthy Distributed Clustering**
  2025-04-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.10109)
  Hongyang Li, Caesar Wu, Mohammed Chadli, Said Mammar, Pascal Bouvry

  <details><summary>摘要 / Abstract</summary>

  Ensuring data trustworthiness within individual edge nodes while facilitating collaborative data processing poses a critical challenge in edge computing systems (ECS), particularly in resource-constrained scenarios such as autonomous systems sensor networks, industrial IoT, and smart cities. This paper presents a lightweight, fully distributed k-means clustering algorithm specifically adapted for edge environments, leveraging a distributed averaging approach with additive secret sharing, a secure multiparty computation technique, during the cluster center update phase to ensure the accuracy and trustworthiness of data across nodes.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Publicly Verifiable Generalized Secret Sharing Schemes and Their Applications**
  2025-04-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/664)
  Liang Zhang, Dongliang Cai, Tao Liu, Xingyu Wu, Haibin Kan, Jiheng Zhang, Moti Yung

  <details><summary>摘要 / Abstract</summary>

  Secret sharing under expressive access structures and public verifiability have largely been developed in separate lines of work. Generalized secret sharing (GSS) supports arbitrary monotone access structures, but relies on private channels and gives no public evidence that the dealer distributed a consistent sharing. Publicly verifiable secret sharing (PVSS), in contrast, supports public verification over insecure channels, but is fundamentally tailored to threshold policies. We introduce publicly verifiable generalized secret sharing (PVGSS), a primitive that combines arbitrary monotone access structures with non-interactive public verification of both encrypted shares and decrypted reconstruction shares. Our construction encrypts only the leaf shares of an underlying GSS instance and proves, via Schnorr-type NIZK proofs, that all ciphertexts are globally consistent with a single secret. The key technical ingredient is a GSS testing procedure that checks this global consistency from proof responses, without revealing the shares. We instantiate PVGSS from recursive Shamir secret sharing and from linear secret sharing schemes, obtaining verification complexity linear in the number of leaves of the access structure. We formalize correctness, encrypted-share verifiability, share-decryption verifiability, and IND1-secrecy, and prove security in the random oracle model under DDH, knowledge soundness of the proof systems, and privacy of the underlying GSS-on-group sharing. As an application, we show how PVGSS enables publicly accountable secret release in a decentralized exchange protocol.

  匹配依据：MPC: secret sharing

  </details>

- **Attribute-Based Publicly Verifiable Secret Sharing**
  2025-04-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/662)
  Liang Zhang, Xingyu Wu, Qiuling Yue, Haibin Kan, Jiheng Zhang

  <details><summary>摘要 / Abstract</summary>

  Can a dealer share a secret without knowing the shareholders? We provide a positive answer to this question by introducing the concept of an attribute-based secret sharing (AB-SS) scheme. With AB-SS, a dealer can distribute a secret based on attributes rather than specific individuals or shareholders. Only authorized users whose attributes satisfy a given access structure can recover the secret. Furthermore, we introduce the concept of attribute-based publicly verifiable secret sharing (AB-PVSS). An AB-PVSS scheme allows external users to verify the correctness of all broadcast messages from the dealer and shareholders, similar to a traditional PVSS scheme. Additionally, AB-SS (or AB-PVSS) distinguishes itself from traditional SS (or PVSS) by enabling a dealer to generate shares according to an arbitrary monotone access structure. To construct an AB-PVSS scheme, we first implement a decentralized ciphertext-policy attribute-based encryption (CP-ABE) scheme. The proposed CP-ABE scheme offers a smaller ciphertext size and requires fewer computational operations, although it is not fully-fledged as a trade-off. We then incorporate non-interactive zero-knowledge (NIZK) proofs to enable public verification of the CP-ABE ciphertext. Based on the CP-ABE and NIZK proofs, we construct an AB-PVSS primitive. Furthermore, we present an intuitive implementation of optimistic fair exchange based on the AB-PVSS scheme. Finally, we conduct security analysis and comprehensive experiments on the proposed CP-ABE and AB-PVSS schemes. The results demonstrate that both schemes exhibit plausible performance compared to related works.

  匹配依据：MPC: secret sharing

  </details>

- **Scalable and Fine-Tuned Privacy Pass from Group Verifiable Random Functions**
  2025-04-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/659)
  Dennis Faut, Julia Hesse, Lisa Kohl, Andy Rupp

  <details><summary>摘要 / Abstract</summary>

  Abstract—Anonymous token schemes are cryptographic protocols for limiting the access to online resources to credible users. The resource provider issues a set of access tokens to the credible user that they can later redeem anonymously, i.e., without the provider being able to link their redemptions. When combined with credibility tests such as CAPTCHAs, anonymous token schemes can significantly increase user experience and provider security, without exposing user access patterns to providers. Current anonymous token schemes such as the Privacy Pass protocol by Davidson et al. rely on oblivious pseudorandom functions (OPRFs), which let server and user jointly compute randomly looking access tokens. For those protocols, token issuing costs are linear in the number of requested tokens. In this work, we propose a new approach for building anonymous token schemes. Instead of relying on two-party computation to realize a privacy-preserving pseudorandom function evaluation, we propose to offload token generation to the user by using group verifiable random functions (GVRFs). GVRFs are a new cryptographic primitive that allow users to produce verifiable pseudorandomness. Opposed to standard VRFs, verification is anonymous within the group of credible users. We give a construction of group VRFs from the Dodis-Yampolskiy VRF and Equivalence- Class Signatures, based on pairings and a new Diffie- Hellman inversion assumption that we analyze in the Generic Group Model. Our construction enjoys compact public keys and proofs, while evaluation and verification costs are only slightly increased compared to the Dodis-Yampolskiy VRF. By deploying a group VRF instead of a OPRF, we obtain an anonymous token scheme where communication as well as server-side computation during the issuing phase is constant and independent of the number of tokens a user requests. Moreover, by means of our new concept of updatable token policies, the number of unspent tokens in circulation can retrospectively (i.e., even after the credibility check) be decreased or increased in order to react to the current or expected network situation. Our tokens are further countable and publicly verifiable. This comes at the cost of higher computational efforts for token redemption and verification as well as somewhat weaker unlinkability guarantees compared to Privacy Pass.

  匹配依据：MPC: two party computation

  </details>

- **Privacy-Preserving Vertical K-Means Clustering**
  2025-04-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.07578)
  Federico Mazzone, Trevor Brown, Florian Kerschbaum, Kevin H. Wilson, Maarten Everts, Florian Hahn, Andreas Peter

  <details><summary>摘要 / Abstract</summary>

  Clustering is a fundamental data processing task used for grouping records based on one or more features. In the vertically partitioned setting, data is distributed among entities, with each holding only a subset of those features. A key challenge in this scenario is that computing distances between records requires access to all distributed features, which may be privacy-sensitive and cannot be directly shared with other parties. The goal is to compute the joint clusters while preserving the privacy of each entity&#x27;s dataset. Existing solutions using secret sharing or garbled circuits implement privacy-preserving variants of Lloyd&#x27;s algorithm but incur high communication costs, scaling as O(nkt), where n is the number of data points, k the number of clusters, and t the number of rounds. These methods become impractical for large datasets or several parties, limiting their use to LAN settings only. On the other hand, a different line of solutions rely on differential privacy (DP) to outsource the local features of the parties to a central server. However, they often significantly degrade the utility of the clustering outcome due to excessive noise. In this work, we propose a novel solution based on homomorphic encryption and DP, reducing communication complexity to O(n+kt). In our method, parties securely outsource their features once, allowing a computing party to perform clustering operations under encryption. DP is applied only to the clusters&#x27; centroids, ensuring privacy with minimal impact on utility. Our solution clusters 100,000 two-dimensional points into five clusters using only 73MB of communication, compared to 101GB for existing works, and completes in just under 3 minutes on a 100Mbps network, whereas existing works take over 1 day. This makes our solution practical even for WAN deployments, all while maintaining accuracy comparable to plaintext k-means algorithms.

  匹配依据：MPC: garbled circuits, secret sharing

  </details>

- **Multi-Party Private Set Operations from Predicative Zero-Sharing**
  2025-04-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.20050) · [IACR ePrint](https://eprint.iacr.org/2025/640)
  Minglang Dong, Yu Chen, Cong Zhang, Yujie Bai, Yang Cao

  <details><summary>摘要 / Abstract</summary>

  Typical protocols in the multi-party private set operations (MPSO) setting enable $m &gt; 2$ parties to perform certain secure computation on the intersection or union of their private sets, realizing a very limited range of MPSO functionalities. Most works in this field focus on just one or two specific functionalities, resulting in a large variety of isolated schemes and a lack of a unified framework in MPSO research. In this work, we present an MPSO framework, which allows $m$ parties, each holding a set, to securely compute any set formulas (arbitrary compositions of a finite number of binary set operations, including intersection, union and difference) on their private sets. Our framework is highly versatile and can be instantiated to accommodate a broad spectrum of MPSO functionalities. To the best of our knowledge, this is the first framework to achieve such a level of flexibility and generality in MPSO, without relying on generic secure multi-party computation (MPC) techniques. Our framework exhibits favorable theoretical and practical performance. With computation and communication complexity scaling linearly with the set size $n$, it achieves optimal complexity that is on par with the naive solution for widely used functionalities, such as multi-party private set intersection (MPSI), MPSI with cardinality output (MPSI-card), and MPSI with cardinality and sum (MPSI-card-sum), for the first time in the standard semi-honest model. Furthermore, the instantiations of our framework, which primarily rely on symmetric-key techniques, provide efficient protocols for MPSI, MPSI-card, MPSI-card-sum, and multi-party private set union (MPSU), with online performance that either surpasses or matches the state of the art in standard semi-honest model. At the technical core of our framework is a newly introduced primitive called predicative zero-sharing. This primitive captures the universality of a number of MPC protocols and is composable. We believe it may be of independent interest.

  匹配依据：MPC: private set intersection, private set union, secure computation, secure multi party computation

  </details>

- **MultiCent: Secure and Scalable Computation of Centrality Measures on Multilayer Graphs**
  2025-04-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/652)
  Andreas Brüggemann, Nishat Koti, Varsha Bhat Kukkala, Thomas Schneider

  <details><summary>摘要 / Abstract</summary>

  As real-world networks such as social networks and computer networks are often complex and distributed, modeling them as multilayer graphs is gaining popularity. For instance, when studying social interactions across platforms like LinkedIn, Facebook, TikTok, and Bluesky, users may be connected on several of these platforms. To identify important nodes/users, the platforms might wish to analyze user interactions using, e.g., centrality measures when accounting for connections across all platforms. This raises the challenge for platforms to perform such computation while simultaneously protecting their user data to shelter their own business as well as uphold data protection laws. Hence, it necessitates designing solutions that allow for performing secure computation on a multilayer graph which is distributed among mutually distrusting parties while keeping each party&#x27;s data hidden. The work of Asharov et al. (WWW&#x27;17) addresses this problem by designing secure solutions for centrality measures that involve computing the truncated Katz score and reach score on multilayer graphs. However, we identify several limitations in that work which render the solution inefficient or even unfeasible for realistic networks with significantly more than $10$k nodes. We address these limitations by designing secure solutions that are significantly more efficient and scalable. In more detail, given that real-world graphs are known to be sparse, our solutions move away from an expensive matrix-based representation to a more efficient list-based representation. We design novel, secure, and efficient solutions for computing centrality measures and prove their correctness. Our solutions drastically reduce the asymptotic complexity from the prohibitive $\mathcal{O}(|\mathsf{V}|^2)$ even for the fastest solution by Asharov et al. down to $\mathcal{O}(|\mathsf{V}|\log |\mathsf{V}|)$, for $|\mathsf{V}|$ nodes. To design our solutions, we extend upon the secure graph computation framework of Koti et al. (CCS&#x27;24), providing a novel framework with improved capabilities in multiple directions. Finally, we provide an end-to-end implementation of our secure graph analysis framework and establish concrete efficiency improvements over prior work, observing several orders of magnitude improvement.

  匹配依据：MPC: secure computation

  </details>

- **Guaranteed Termination Asynchronous Complete Secret Sharing with Lower Communication and Optimal Resilience**
  2025-04-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/649)
  Ying Cai, Chengyi Qin, Mingqiang Wang

  <details><summary>摘要 / Abstract</summary>

  Asynchronous Complete Secret Sharing (ACSS) is a foundational module for asynchronous networks, playing a critical role in cryptography. It is essential for Asynchronous Secure Multi-Party Computation (AMPC) and, with termination, is widely applied in Validated Asynchronous Byzantine Agreement (VABA) and Asynchronous Distributed Key Generation (ADKG) to support secure distributed systems. Currently, there are relatively few statistical secure ACSS protocols that can guarantee termination, and their communication complexity is relatively high. To reduce communication complexity, we propose a new multi-receiver signature scheme, ARICP, which supports linear operations on signatures. Leveraging the ARICP scheme and the properties of symmetric polynomials, we propose an ACSS protocol that ensures termination and optimal resilience ($t &lt; n / 3$) with $\mathcal{O}(n^{2}\kappa$) bits per sharing. Compared with the best-known result of ACSS protocols that guarantee termination [CP23], the amortized communication complexity of our protocol is reduced by a factor of $\mathcal{O}(n)$.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Fission: Distributed Privacy-Preserving Large Language Model Inference**
  2025-04-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/653)
  Mehmet Ugurbil, Dimitris Mouris, Manuel B. Santos, José Cabrero-Holgueras, Miguel de Vega, Shubho Sengupta

  <details><summary>摘要 / Abstract</summary>

  The increased popularity of large language models (LLMs) raises serious privacy concerns, where users&#x27; private queries are sent to untrusted servers. Many cryptographic techniques have been proposed to provide privacy, such as secure multiparty computation (MPC), which enables the evaluation of LLMs directly on private data. However, cryptographic techniques have been deemed impractical as they introduce large communication and computation. On the other hand, many obfuscation techniques have been proposed, such as split inference, where part of the model is evaluated on edge devices to hide the input data from untrusted servers, but these methods provide limited privacy guarantees. We propose Fission, a privacy-preserving framework that improves latency while providing strong privacy guarantees. Fission utilizes an MPC network for linear computations, while nonlinearities are computed on a separate evaluator network that receives shuffled values in the clear and returns nonlinear functions evaluated at these values back to the MPC network. As a result, each evaluator only gets access to parts of the shuffled data, while the model weights remain private. We evaluate fission on a wide set of LLMs and compare it against prior works. Fission results in up to eight times faster inference and eight times reduced bandwidth compared to prior works while retaining high accuracy. Finally, we construct an attack on obfuscation techniques from related works that show significant information leakage, and we demonstrate how Fission enhances privacy.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Laconic Cryptography with Preprocessing**
  2025-04-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/605)
  Rishabh Bhadauria, Nico Döttling, Carmit Hazay, Chuanwei Lin

  <details><summary>摘要 / Abstract</summary>

  Laconic cryptography focuses on designing two-message protocols that allow secure computation on large datasets while minimizing communication costs. While laconic cryptography protocols achieve asymptotically optimal communication complexity for many tasks, their concrete efficiency is prohibitively expensive due to the heavy use of public-key techniques or the non-black-box of cryptographic primitives. In this work, we initiate the study of &quot;laconic cryptography with preprocessing&quot;, introducing a model that includes an offline phase to generate database-dependent correlations, which are then used in a lightweight online phase. These correlations are conceptually simple, relying on linear-algebraic techniques. This enables us to develop a protocol for private laconic vector oblivious linear evaluation (plvOLE). In such a protocol, the receiver holds a large database $\mathsf{DB}$, and the sender has two messages $v$ and $w$, along with an index $i$. The receiver learns the value $v \cdot \mathsf{DB}_i + w$ without revealing other information. Our protocol, which draws from ideas developed in the context of private information retrieval with preprocessing, serves as the backbone for two applications of interest: laconic private set intersection (lPSI) for large universes and laconic function evaluation for RAM-programs (RAM-LFE). Based our plvOLE protocol, we provide efficient instantiations of these two primitives in the preprocessing model.

  匹配依据：MPC: private set intersection, secure computation

  </details>

- **Towards Resilient Federated Learning in CyberEdge Networks: Recent Advances and Future Trends**
  2025-04-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.01240)
  Kai Li, Zhengyang Zhang, Azadeh Pourkabirian, Wei Ni, Falko Dressler, Ozgur B. Akan

  <details><summary>摘要 / Abstract</summary>

  In this survey, we investigate the most recent techniques of resilient federated learning (ResFL) in CyberEdge networks, focusing on joint training with agglomerative deduction and feature-oriented security mechanisms. We explore adaptive hierarchical learning strategies to tackle non-IID data challenges, improving scalability and reducing communication overhead. Fault tolerance techniques and agglomerative deduction mechanisms are studied to detect unreliable devices, refine model updates, and enhance convergence stability. Unlike existing FL security research, we comprehensively analyze feature-oriented threats, such as poisoning, inference, and reconstruction attacks that exploit model features. Moreover, we examine resilient aggregation techniques, anomaly detection, and cryptographic defenses, including differential privacy and secure multi-party computation, to strengthen FL security. In addition, we discuss the integration of 6G, large language models (LLMs), and interoperable learning frameworks to enhance privacy-preserving and decentralized cross-domain training. These advancements offer ultra-low latency, artificial intelligence (AI)-driven network management, and improved resilience against adversarial attacks, fostering the deployment of secure ResFL in CyberEdge networks.

  匹配依据：MPC: secure multi party computation

  </details>

- **$\\mathsf{GraSP}$: Secure Collaborative Graph Processing Made Scalable**
  2025-04-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/590)
  Siddharth Kapoor, Nishat Koti, Varsha Bhat Kukkala, Arpita Patra, Bhavish Raj Gopal

  <details><summary>摘要 / Abstract</summary>

  Secure graph processing enables computing on graphs while hiding the graph topology as well as the associated node/edge data. This facilitates collaborative analysis among multiple data owners, who may only hold a private, partial view of the global graph. Several works address this problem using the technique of secure multiparty computation (MPC) in the presence of 2 or 3 parties. However, when moving to the multiparty setting, as required for collaborative analysis among multiple data owners, the existing solutions are no longer scalable. Specifically, the runtime of the state-of-the-art scales linearly with the number of parties. Additionally, it has an expensive initialisation phase, which requires secure sorting operations known to be expensive in MPC. Thus, we propose $\mathsf{GraSP}$, a generic framework for secure graph processing that improves efficiency and scalability for the multiparty setting. Further, $\mathsf{GraSP}$ is designed to have a lightweight initialisation, which eliminates the need for secure sorting. Unlike any of the prior works, achieving a round complexity in MPC that is independent of the number of parties is what makes $\mathsf{GraSP}$ scalable. Finally, we implement and benchmark the performance of $\mathsf{GraSP}$ for the application of PageRank computation and showcase its efficiency and scalability improvements over the state-of-the-art. Concretely, we witness improvements of up to $78\times$ in runtime in comparison to the state-of-the-art. Further, we observe that $\mathsf{GraSP}$ takes under a minute to perform 10 iterations of PageRank on a graph of size $10^6$ that is distributed among $25$ data owners, making it highly practical for secure graph processing in the multiparty setting.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Pre-Constructed Publicly Verifiable Secret Sharing and Applications**
  2025-03-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/576)
  Karim Baghery, Noah Knapen, Georgio Nicolas, Mahdi Rahimi

  <details><summary>摘要 / Abstract</summary>

  Conventional Publicly Verifiable Secret Sharing (PVSS) protocols allow a dealer to share a secret among $n$ parties without interaction, ensuring that any $t + 1$ parties (where $t+1 \le n$) can recover the secret, while anyone can publicly verify the validity of both the individual shares and the reconstructed secret. PVSS schemes are shown to be a key tool in a wide range of practical applications. In this paper, we introduce Pre-constructed PVSS (PPVSS), an extension of standard PVSS schemes, highlighting its enhanced utility and efficiency in various protocols. Unlike standard PVSS, PPVSS requires the dealer to publish a commitment or encryption of the main secret and incorporates a novel secret reconstruction method. We show that these refinements make PPVSS more practical and versatile than conventional PVSS schemes. To build a PPVSS scheme, we first point out that the well-known PVSS scheme by Schoenmakers (CRYPTO&#x27;99) and its pairing-based variant presented by Heidarvand and Villar (SAC&#x27;08) can be seen as special cases of PPVSS, where the dealer also publishes a commitment to the main secret. However, these protocols are not practical for many applications due to efficiency limitations and are less flexible compared to a standard PPVSS scheme. To address this, we propose a general strategy for transforming a Shamir-based PVSS scheme into a PPVSS scheme. Using this strategy, we construct two practical PPVSS schemes in both the Random Oracle (RO) and plain models, grounded in state-of-the-art PVSS designs. Leveraging the new RO-based PPVSS scheme, we revisit some applications and present more efficient variants. Notably, we propose a new universally verifiable e-voting protocol that improves on the alternative scheme by Schoenmakers (CRYPTO&#x27;99), reducing the verification complexity with $m$ voters from $O(n^2m)$ to $O(nm)$ exponentiations--a previously unattainable goal with standard PVSS schemes. Our implementation results demonstrate that both our proposed PPVSS schemes and the new universally verifiable e-voting protocol significantly outperform existing alternatives in terms of efficiency.

  匹配依据：MPC: secret sharing

  </details>

- **Efficient Garbled Pseudorandom Functions and Lookup Tables from Minimal Assumption**
  2025-03-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/578)
  Wei-Kai Lin, Zhenghao Lu, Hong-Sheng Zhou

  <details><summary>摘要 / Abstract</summary>

  Yao&#x27;s garbled circuits have received huge attention in both theory and practice. While garbled circuits can be constructed using minimal assumption (i.e., the existence of pseudorandom functions or one-way functions), the state-of-the-art constructions (e.g., Rosulek-Roy, Crypto 2021) are based on stronger assumptions. In particular, the ``Free-XOR&#x27;&#x27; technique (Kolesnikov-Schneider, ICALP 2008) is essential in these state-of-the-art constructions, and their security can only be proven in the random oracle model, or rely on the ``circular-correlation robust hash&#x27;&#x27; assumption. In this paper, we aim to develop new techniques to construct efficient garbling schemes using minimal assumptions. Instead of generically replacing the Free-XOR technique, we focus on garbling schemes for specific functionalities. We successfully eliminated the need for Free-XOR in several state-of-the-art schemes, including the one-hot garbling (Heath and Kolesnikov, CCS 2021) and the garbled pseudorandom functions, and the garbled lookup tables (Heath, Kolesnikov and Ng, Eurocrypt 2024). Our schemes are based on minimal assumptions, i.e., standard pseudorandom functions (PRFs)---we resolved the need for circular security. The performance of our scheme is almost as efficient as the best results except for a small constant factor. Namely, for any lookup table $\{0,1\}^n \to \{0,1\}^m$, our scheme takes $n + (5n+9)m\lambda + 2^n \cdot m$ bits of communication, where $\lambda$ is the security parameter of PRF.

  匹配依据：MPC: garbled circuits, garbling schemes

  </details>

- **Reflex: Faster Secure Collaborative Analytics via Controlled Intermediate Result Size Disclosure**
  2025-03-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.20932)
  Long Gu, Shaza Zeitouni, Carsten Binnig, Zsolt István

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation (MPC) enables collaborative analytics without exposing private data. However, OLAP queries under MPC remain prohibitively slow due to oblivious execution and padding of intermediate results with filler tuples. We present Reflex, the first framework that enables configurable trimming of intermediate results across different query operators -- joins, selections, and aggregations -- within full query plans. At its core is the Resizer operator, which can be inserted between any oblivious operators to selectively remove filler tuples under MPC using user-defined probabilistic strategies. To make privacy trade-offs interpretable, we introduce a new metric that quantifies the number of observations an attacker would need to infer the true intermediate result sizes. Reflex thus makes the performance-privacy space of secure analytics navigable, allowing users to balance efficiency and protection. Experiments show substantial runtime reductions while maintaining quantifiable privacy guarantees.

  匹配依据：MPC: secure multi party computation

  </details>

- **Efficient hyperentanglement-based quantum secret sharing protocol**
  2025-03-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.20216)
  Cheng Zhang, Fu-Le Hao, Shi-Pu Gu, Xing-Fu Wang, Lan Zhou, Yu-Bo Sheng

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) is a typical multipartite cryptographic primitive, which is an important part of quantum communication network. Existing QSS protocols generally require basis selection and matching, which would increase the quantum resource consumption and classical communication round, and also face weak random security vulnerabilities. We propose an efficient hyperentanglement-based QSS protocol without the basis selection, in which the dealer and partners share a polarization-momentum hyperentangled Greenberger-Horne-Zeilinger (GHZ) state and encode keys in the polarization degree of freedom (DOF). The dealer decodes the transmitted keys relying on the nonlocal hyperentanglement-assisted polarization GHZ state analysis. Our QSS protocol is unconditionally secure in theory. We develop simulation method to estimate its performance in practical environment. Compared with the QSS based on the GHZ state, our protocol has several advantages. First, it does not require basis selection and can completely distinguish eight polarization GHZ states, which can improve the utilization rate of entanglement resources to 100$\%$ and increase the key generation rate by an order of magnitude. Second, it only requires one round of classical communication, and thus can reduce key generation time by 69.4$\%$. Third, it can eliminate the weak random security vulnerabilities associated with the basis selection. Finally, our protocol only uses linear optical elements, which makes it practically feasible. Our QSS protocol has potential application in future quantum communication network.

  匹配依据：MPC: secret sharing

  </details>

- **Black Box Crypto is Useless for Doubly Efficient PIR**
  2025-03-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/552)
  Wei-Kai Lin, Ethan Mook, Daniel Wichs

  <details><summary>摘要 / Abstract</summary>

  A (single server) private information retrieval (PIR) allows a client to read data from a public database held on a remote server, without revealing to the server which locations she is reading. In a doubly efficient PIR (DEPIR), the database is first preprocessed offline into a data structure, which then allows the server to answer any client query efficiently in sub-linear online time. Constructing DEPIR is a notoriously difficult problem, and this difficulty even extends to a weaker notion secret-key DEPIR (SK-DEPIR), where the database is preprocessed using secret randomness and the client is given a secret key for making queries. We currently only have constructions of SK-DEPIR from the Ring LWE assumption or from non-standard code-based assumptions. We show that the black-box use of essentially all generic cryptographic primitives (e.g., key agreement, oblivious transfer, indistinguishability obfuscation, etc.), including idealized primitives (e.g., random oracles, generic multilinear groups, virtual black-box obfuscation, etc.) is essentially useless for constructing SK-DEPIR. In particular, in any such SK-DEPIR construction, we can replace all black-box use of these primitives with just a black-box use of one-way functions. While we conjecture that SK-DEPIR cannot be constructed using black-box one-way functions alone, we are unable to show this in its full generality. However, we do show this for 2-round schemes with a passive server that simply outputs requested locations in the preprocessed data structure, which is the format of all known schemes. Overall, this shows that the black-box use of essentially all crypto primitives is insufficient for constructing 2-round passive-server SK-DEPIR, and does not provide any benefit beyond black-box one-way functions for constructing general SK-DEPIR.

  匹配依据：MPC: oblivious transfer

  </details>

- **ANARKey: A New Approach to (Socially) Recover Keys**
  2025-03-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/551)
  Aniket Kate, Pratyay Mukherjee, Hamza Saleem, Pratik Sarkar, Bhaskar Roberts

  <details><summary>摘要 / Abstract</summary>

  In a social key recovery scheme, users back up their secret keys (typically using Shamir&#x27;s secret sharing) with their social connections, known as a set of guardians. This places a heavy burden on the guardians, as they must manage their shares both securely and reliably. Finding and managing such a set of guardians may not be easy, especially when the consequences of losing a key are significant. We take an alternative approach of social recovery within a community, where each member already holds a secret key (with possibly an associated public key) and uses other community members as their guardians forming a mutual dependency among themselves. Potentially, each member acts as a guardian for upto $(n-1)$ other community members. Therefore, in this setting, using standard Shamir&#x27;s sharing leads to a linear ($O(n)$) blow-up in the internal secret storage of the guardian for each key recovery. Our solution avoids this linear blowup in internal secret storage by relying on a novel secret-sharing scheme, leveraging the fact that each member already manages a secret key. In fact, our scheme does not require guardians to store anything beyond their own secret keys. We propose the first formal definition of a social key recovery scheme for general access structures in the community setting. We prove that our scheme is secure against any malicious and adaptive adversary that may corrupt up to $t$ parties. As a main technical tool, we use a new notion of secret sharing, that enables $(t+1)$ out of $n$ sharing of a secret even when the shares are generated independently -- we formalize this as bottom-up secret sharing (BUSS), which may be of independent interest. Finally, we provide an implementation benchmarking varying the number of guardians both in a regional, and geo-distributed setting. For instance, for 8 guardians, our backup protocol takes around 146-149 ms in a geo-distributed WAN setting, and 4.9-5.9 ms in the LAN setting; for recovery protocol, the timings are approximately the same for the WAN setting (as network latency dominates), and 1.2-1.4 ms for the LAN setting.

  匹配依据：MPC: secret sharing

  </details>

- **Launching Insights: A Pilot Study on Leveraging Real-World Observational Data from the Mayo Clinic Platform to Advance Clinical Research**
  2025-03-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.16090)
  Yue Yu, Xinyue Hu, Sivaraman Rajaganapathy, Jingna Feng, Ahmed Abdelhameed, Xiaodi Li, Jianfu Li, Ken Liu, Liu Yang, Nilufer Taner, Phil Fiero, Soulmaz Boroumand, Richard Larsen, Maneesh Goyal, Clark Otley, Nansu Zong, John Halamka, Cui Tao

  <details><summary>摘要 / Abstract</summary>

  Backgrounds: Artificial intelligence (AI) is transforming healthcare, yet translating AI models from theoretical frameworks to real-world clinical applications remains challenging. The Mayo Clinic Platform (MCP) was established to address these challenges by providing a scalable ecosystem that integrates real-world multiple modalities data from multiple institutions, advanced analytical tools, and secure computing environments to support clinical research and AI development. Methods: In this study, we conducted four research projects leveraging MCP&#x27;s data infrastructure and analytical capabilities to demonstrate its potential in facilitating real-world evidence generation and AI-driven clinical insights. Utilizing MCP&#x27;s tools and environment, we facilitated efficient cohort identification, data extraction, and subsequent statistical or AI-powered analyses. Results: The results underscore MCP&#x27;s role in accelerating translational research by offering de-identified, standardized real-world data and facilitating AI model validation across diverse healthcare settings. Compared to Mayo&#x27;s internal Electronic Health Record (EHR) data, MCP provides broader accessibility, enhanced data standardization, and multi-institutional integration, making it a valuable resource for both internal and external researchers. Conclusion: Looking ahead, MCP is well-positioned to transform clinical research through its scalable ecosystem, effectively bridging the divide between AI innovation and clinical deployment. Future investigations will build upon this foundation, further exploring MCP&#x27;s capacity to advance precision medicine and enhance patient outcomes.

  匹配依据：MPC: secure computing

  </details>

- **Empirical Analysis of Privacy-Fairness-Accuracy Trade-offs in Federated Learning: A Step Towards Responsible AI**
  2025-03-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.16233)
  Dawood Wasif, Dian Chen, Sindhuja Madabushi, Nithin Alluru, Terrence J. Moore, Jin-Hee Cho

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) enables collaborative model training while preserving data privacy; however, balancing privacy preservation (PP) and fairness poses significant challenges. In this paper, we present the first unified large-scale empirical study of privacy-fairness-utility trade-offs in FL, advancing toward responsible AI deployment. Specifically, we systematically compare Differential Privacy (DP), Homomorphic Encryption (HE), and Secure Multi-Party Computation (SMC) with fairness-aware optimizers including q-FedAvg, q-MAML, Ditto, evaluating their performance under IID and non-IID scenarios using benchmark (MNIST, Fashion-MNIST) and real-world datasets (Alzheimer&#x27;s MRI, credit-card fraud detection). Our analysis reveals HE and SMC significantly outperform DP in achieving equitable outcomes under data skew, although at higher computational costs. Remarkably, we uncover unexpected interactions: DP mechanisms can negatively impact fairness, and fairness-aware optimizers can inadvertently reduce privacy effectiveness. We conclude with practical guidelines for designing robust FL systems that deliver equitable, privacy-preserving, and accurate outcomes.

  匹配依据：MPC: secure multi party computation

  </details>

- **Secret-Sharing Schemes for General Access Structures: An Introduction**
  2025-03-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/518)
  Amos Beimel

  <details><summary>摘要 / Abstract</summary>

  A secret-sharing scheme is a method by which a dealer distributes shares to parties such that only authorized subsets of parties can reconstruct the secret. Secret-sharing schemes are an important tool in cryptography and they are used as a building block in many secure protocols, e.g., secure multiparty computation protocols for arbitrary functionalities, Byzantine agreement, threshold cryptography, access control, attribute-based encryption, and weighted cryptography (e.g., stake-based blockchains). The collection of authorized sets that should be able to reconstruct the secret is called an access structure. The main goal in secret sharing is to minimize the share size in a scheme realizing an access structure. In most of this monograph, we will consider secret-sharing schemes with information-theoretic security, i.e., schemes in which unauthorized sets cannot deduce any information on the secret even when the set has unbounded computational power. Although research on secret-sharing schemes has been conducted for nearly 40 years, we still do not know what the optimal share size required to realize an arbitrary 𝑛-party access structure is; there is an exponential gap between the best known upper bounds and the best known lower bounds on the share size. In this monograph, we review the most important topics on secret sharing. We start by discussing threshold secret-sharing schemes in which the authorized sets are all sets whose size is at least some threshold 𝑡; these are the most useful secret-sharing schemes. We then describe efficient constructions of secret-sharing schemes for general access structures; in particular, we describe constructions of linear secret-sharing schemes from monotone formulas and monotone span programs and provide a simple construction for arbitrary 𝑛-party access structures with share size 2^0.5𝑛. To demonstrate the importance of secret-sharing schemes, we show how they are used to construct secure multi-party computation protocols for arbitrary functions. We next discuss the main problem with known secret-sharing schemes – the large share size, which is exponential in the number of parties. We present the known lower bounds on the share size. These lower bounds are fairly weak, and there is a big gap between the lower and upper bounds. For linear secret-sharing schemes, which are a class of schemes based on linear algebra that contains most known schemes, exponential lower bounds on the share size are known. We then turn to study ideal secret-sharing schemes in which the share size of each party is the same as the size of the secret; these schemes are the most efficient secret-sharing schemes. We describe a characterization of the access structures that have ideal schemes via matroids. Finally, we discuss computational secret-sharing schemes, i.e., secret-sharing schemes that are secure only against polynomial-time adversaries. We show computational schemes for monotone and non-monotone circuits; these constructions are more efficient than the best known schemes with information-theoretic security.

  匹配依据：MPC: secret sharing, secure multi party computation, secure multiparty computation

  </details>

- **New Techniques for Analyzing Fully Secure Protocols: A Case Study of Solitary Output Secure Computation**
  2025-03-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/522)
  Bar Alon, Benjamin Saldman, Eran Omri

  <details><summary>摘要 / Abstract</summary>

  Solitary output secure computation allows a set of mutually distrustful parties to compute a function of their inputs such that only a designated party obtains the output. Such computations should satisfy various security properties such as correctness, privacy, independence of inputs, and even guaranteed output delivery. We are interested in full security, which captures all of these properties. Solitary output secure computation has been the study of many papers in recent years, as it captures many real-world scenarios. A systematic study of fully secure solitary output computation was initiated by Halevi et al. [TCC 2019]. They showed several positive and negative results, however, they did not characterize what functions can be computed with full security. Alon et al. [EUROCRYPT 2024] considered the special, yet important case, of three parties with Boolean output, where the output-receiving party has no input. They completely characterized the set of such functionalities that can be computed with full security. Interestingly, they also showed a possible connection with the seemingly unrelated notion of fairness, where either all parties obtain the output or none of them do. We continue this line of investigation and study the set of three-party solitary output Boolean functionalities where all parties hold private inputs. Our main contribution is defining and analyzing a family of ``special-round&#x27;&#x27; protocols, which generalizes the set of previously proposed protocols. Our techniques allow us to identify which special-round protocols securely compute a given functionality (if such exists). Interestingly, our analysis can also be applied in the two-party setting (where fairness is an issue). Thus, we believe that our techniques may prove useful in additional settings and deepen our understanding of the connections between the various settings.

  匹配依据：MPC: secure computation

  </details>

- **Masking-Friendly Post-Quantum Signatures in the Threshold-Computation-in-the-Head Framework**
  2025-03-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/520)
  Thibauld Feneuil, Matthieu Rivain, Auguste Warmé-Janville

  <details><summary>摘要 / Abstract</summary>

  Side-channel attacks pose significant threats to cryptographic implementations, which require the inclusion of countermeasures to mitigate these attacks. In this work, we study the masking of state-of-the-art post-quantum signatures based on the MPC-in-the-head paradigm. More precisely, we focus on the recent threshold-computation-in-the-head (TCitH) framework that applies to some NIST candidates of the post-quantum standardization process. We first provide an analysis of side-channel attack paths in the signature algorithms based on the TCitH framework. We then explain how to apply standard masking to achieve a $d$-probing secure implementation of such schemes, with performance scaling in $O(d^{2})$, for $d$ the masking order. Our main contribution is to introduce different ways to tweak those signature schemes towards their masking friendliness. While the TCitH framework comes in two variants, the GGM variant and the Merkle tree variant, we introduce a specific tweak for each of these variants. These tweaks allow us to achieve complexities of $O(d)$ and $O(d \log d)$ at the cost of non-constant signature size, caused by the inclusion of additional seeds in the signature. We also propose a third tweak that takes advantage of the threshold secret sharing used in TCitH. With the right choice of parameters, we show how, by design, some parts of the TCitH algorithms satisfy probing security without additional countermeasures. While this approach can substantially reduce the cost of masking in some part of the signature algorithm, it degrades the soundness of the core zero-knowledge proof, hence slightly increasing the size of the signature. We analyze the complexity of the masked implementations of our tweaked TCitH signatures and provide benchmarks on a RISC-V platform with built-in hash accelerator. We use a modular benchmarking approach, allowing to estimate the performance of diverse signature instances with different tweaks and parameters. Our results illustrate how the different variants scale for an increasing masking order. For instance, for a masking order $d = 3$, we obtain signatures of around $14$ kB that run in $0.67$ second on a the target RISC-V CPU with a $250$MHz frequency. This is to be compared with the $4.7$ seconds required by the original signature scheme masked at the same order on the same platform. For a masking order $d=7$, we obtain a signature of $17.5$ kB running in $1.75$ second, to be compared with $16$ seconds for the stardard masked signature. Finally, we discuss the extension of our techniques to signature schemes based on the VOLE-in-the-Head framework, which shares similarities with the GGM variant of TCitH. One key takeaway of our work is that the Merkle tree variant of TCitH is inherently more amenable to efficient masking than frameworks based on GGM trees, such as TCitH-GGM or VOLE-in-the-Head.

  匹配依据：MPC: secret sharing

  </details>

- **Designated-Verifier SNARGs with One Group Element**
  2025-03-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/517)
  Gal Arnon, Jesko Dujmovic, Yuval Ishai

  <details><summary>摘要 / Abstract</summary>

  We revisit the question of minimizing the proof length of designated-verifier succinct non-interactive arguments (dv-SNARGs) in the generic group model. Barta et al. (Crypto 2020) constructed such dv-SNARGs with inverse-polynomial soundness in which the proof consists of only two group elements. For negligible soundness, all previous constructions required a super-constant number of group elements. We show that one group element suffices for negligible soundness. Concretely, we obtain dv-SNARGs (in fact, dv-SNARKs) with $2^{-\tau}$ soundness where proofs consist of one element of a generic group $\mathbb G$ and $O(\tau)$ additional bits. In particular, the proof length in group elements is constant even with $1/|\mathbb G|$ soundness error. In more concrete terms, compared to the best known SNARGs using bilinear groups, we get dv-SNARGs with roughly $2$x shorter proofs (with $2^{-80}$ soundness at a $128$-bit security level). We are not aware of any practically feasible proof systems that achieve similar succinctness, even fully interactive or heuristic ones. Our technical approach is based on a novel combination of techniques for trapdoor hash functions and group-based homomorphic secret sharing with linear multi-prover interactive proofs.

  匹配依据：MPC: secret sharing

  </details>

- **Absolutely Maximal Entanglement in Continuous Variables**
  2025-03-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.15698)
  James I. Kwon, Anthony J. Brady, Victor V. Albert

  <details><summary>摘要 / Abstract</summary>

  We explore absolutely maximal entanglement (AME) and k-uniformity in continuous-variable (CV) quantum systems, and show that-unlike in qudit systems-such entanglement is readily realizable in both Gaussian and non-Gaussian quantum states of multiple modes. We demonstrate that Gaussian CV cluster states are generically AME, rederiving the results of [Phys. Rev. Lett. 103, 070501 (2009)] from a generalized stabilizer formalism, and provide explicit constructions based on Cauchy, Vandermonde, totally positive, and real-block-code generator matrices. We further extend AME properties to a family of non-Gaussian states constructed from discrete Zak basis states that incorporate grid states (a.k.a., Gottesman-Kitaev-Preskill states) as non-Gaussian resources. Realizations of CV AME states enable open-destination multi-party CV teleportation, CV quantum secret sharing, CV majority-agreed key distribution, perfect-tensor networks on arbitrary geometries, and multi-unitary circuits. Our extension to non-Gaussian AME states may further provide robustness to Gaussian noise and benefits to quantum CV information processing.

  匹配依据：MPC: secret sharing

  </details>

- **Towards Building Scalable Constant-Round MPC from Minimal Assumptions via Round Collapsing**
  2025-03-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/508)
  Vipul Goyal, Junru Li, Rafail Ostrovsky, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  In this work, we study the communication complexity of constant-round secure multiparty computation (MPC) against a fully malicious adversary and consider both the honest majority setting and the dishonest majority setting. In the (strong) honest majority setting (where $t=(1/2-\epsilon)n$ for a constant $\epsilon$), the best-known result without relying on FHE is given by Beck et al. (CCS 2023) based on the LPN assumption that achieves $O(|C|\kappa)$ communication, where $\kappa$ is the security parameter and the achieved communication complexity is independent of the number of participants. In the dishonest majority setting, the best-known result is achieved by Goyal et al. (ASIACRYPT 2024), which requires $O(|C|n\kappa)$ bits of communication and is based on the DDH and LPN assumptions. In this work, we achieve the following results: (1) For any constant $\epsilon&lt;1$, we give the first constant-round MPC in the dishonest majority setting for corruption threshold $t&lt;(1-\epsilon)n$ with $O(|C|\kappa+D (n+\kappa)^2\kappa+n^3)$ communication assuming random oracles and oblivious transfers, where $D$ is the circuit depth. (2) We give the first constant-round MPC in the standard honest majority setting (where $t=(n-1)/2$) with $O(|C|\kappa+D (n+\kappa)^2\kappa+n^3)$ communication only assuming random oracles. Unlike most of the previous constructions of constant-round MPCs that are based on multiparty garbling, we achieve our result by letting each party garble his local computation in a non-constant-round MPC that meets certain requirements. We first design a constant-round MPC that achieves $O(|C|\kappa + Dn^2\kappa)$ communication assuming random oracles in the strong honest majority setting of $t=n/4$. Then, we combine the party virtualization technique and the idea of MPC-in-the-head to boost the corruption threshold to $t&lt;(1-\epsilon)n$ for any constant $\epsilon&lt;1$ assuming oblivious transfers to achieve our first result. Finally, our second result is obtained by instantiating oblivious transfers using a general honest-majority MPC and the OT extension technique built on random oracles.

  匹配依据：MPC: secure multiparty computation

  </details>

- **The probabilistic combinatorial attacks on atmospheric continuous-variable quantum secret sharing**
  2025-03-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.12729)
  Fangli Yang, Liang Chang, Minghua Pan

  <details><summary>摘要 / Abstract</summary>

  The combination of quantum secret sharing (QSS) and continuous-variable quantum key distribution (CV-QKD) has demonstrated clear advantages and has undergone significant development in recent years. However, research on the practical security of CV-QSS remains limited, particularly in the context of free-space channels, which exhibit considerable flexibility. In this paper, we study the practical security of free-space CV-QSS, innovatively propose an attack strategy that probabilistically combines two-point distribution attack (TDA) and uniform distribution attack (UDA). We also establish channel parameter models, especially a channel noise model based on local local oscillators (LLO), to further evaluate the key rate. In principle, the analysis can be extended to any number of probabilistic combinations of channel manipulation attacks. The numerical results demonstrate that the probabilistic combination attacks reduce the real key rate of CV-QSS under moderate intensity turbulence, but still enable secure QSS at a distance of 8 km on a scale of hundreds. However, it should be noted that the probabilistic combination attacks will make the deviation between the estimated key rate and the real key rate, i.e., the key rate is overestimated, which may pose a security risk.

  匹配依据：MPC: secret sharing

  </details>

- **Ideal Compartmented Secret Sharing Scheme Based on the Chinese Remainder Theorem for Polynomial Rings**
  2025-03-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/504)
  Alexandru-Valentin Basaga, Sorin Iftene

  <details><summary>摘要 / Abstract</summary>

  A secret sharing scheme starts with a secret and then derives from it certain shares (or shadows) which are distributed to users. The secret may be recovered only by certain predetermined groups. In case of compartmented secret sharing, the set of users is partitioned into compartments and the secret can be recovered only if the number of participants from any compartment is greater than or equal to a fixed compartment threshold and the total number of participants is greater than or equal to a global threshold. In this paper we use the Chinese Remainder Theorem for Polynomial Rings in order to construct an ideal compartmented secret sharing scheme, inspired by the work from [20].

  匹配依据：MPC: secret sharing

  </details>

- **SecurED: Secure Multiparty Edit Distance for Genomic Sequences**
  2025-03-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/500)
  Jiahui Gao, Yagaagowtham Palanikuma, Dimitris Mouris, Duong Tung Nguyen, Ni Trieu

  <details><summary>摘要 / Abstract</summary>

  DNA edit distance (ED) measures the minimum number of single nucleotide insertions, substitutions, or deletions required to convert a DNA sequence into another. ED has broad applications in healthcare such as sequence alignment, genome assembly, functional annotation, and drug discovery. Privacy-preserving computation is essential in this context to protect sensitive genomic data. Nonetheless, the existing secure DNA edit distance solutions lack efficiency when handling large data sequences or resort to approximations and fail to accurately compute the metric. In this work, we introduce secureED, a protocol that tackles these limitations, resulting in a significant performance enhancement of approximately $2-24\times$ compared to existing methods. Our protocol computes a secure ED between two genomes, each comprising $1,000$ letters, in just a few seconds. The underlying technique of our protocol is a novel approach that transforms the established approximate matching technique (i.e., the Ukkonen algorithm) into exact matching, exploiting the inherent similarity in human DNA to achieve cost-effectiveness. Furthermore, we introduce various optimizations tailored for secure computation in scenarios with a limited input domain, such as DNA sequences composed solely of the four nucleotide letters.

  匹配依据：MPC: secure computation

  </details>

- **Tighter Concrete Security for the Simplest OT**
  2025-03-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/493)
  Iftach Haitner, Gil Segev

  <details><summary>摘要 / Abstract</summary>

  The Chou-Orlandi batch oblivious transfer (OT) protocol is a particularly attractive OT protocol that bridges the gap between practical efficiency and strong security guarantees and is especially notable due to its simplicity. The security analysis provided by Chou and Orlandi bases the security of their protocol on the hardness of the computational Diffie-Hellman ($\mathsf{CDH}$) problem in prime-order groups. Concretely, in groups in which no better-than-generic algorithms are known for the $\mathsf{CDH}$ problem, their security analysis yields that an attacker running in time $t$ and issuing $q$ random-oracle queries breaks the security of their protocol with probability at most $\epsilon \leq q^2 \cdot t / 2^{\kappa/2}$, where $\kappa$ is the bit-length of the group&#x27;s order. This concrete bound, however, is somewhat insufficient for 256-bit groups (e.g., for $\kappa = 256$, it does not provide any guarantee already for $t = 2^{48}$ and $q = 2^{40}$). In this work, we establish a tighter concrete security bound for the Chou-Orlandi protocol. First, we introduce the list square Diffie-Hellman ($\ell\text{-}\mathsf{sqDH}$) problem and present a tight reduction from the security of the protocol to the hardness of solving $\ell\text{-}\mathsf{sqDH}$. That is, we completely shift the task of analyzing the concrete security of the protocol to that of analyzing the concrete hardness of the $\ell\text{-}\mathsf{sqDH}$ problem. Second, we reduce the hardness of the $\ell\text{-}\mathsf{sqDH}$ problem to that of the decisional Diffie-Hellman ($\mathsf{DDH}$) problem without incurring a multiplicative loss. Our key observation is that although $\mathsf{CDH}$ and $\mathsf{DDH}$ have the same assumed concrete hardness, relying on the hardness of $\mathsf{DDH}$ enables our reduction to efficiently test the correctness of the solutions it produces. Concretely, in groups in which no better-than-generic algorithms are known for the $\mathsf{DDH}$ problem, our analysis yields that an attacker running in time $t$ and issuing $q \leq t$ random-oracle queries breaks the security of the Chou-Orlandi protocol with probability at most $\epsilon \leq t / 2^{\kappa/2}$ (i.e., we eliminate the above multiplicative $q^2$ term). We prove our results within the standard real-vs-ideal framework considering static corruptions by malicious adversaries, and provide a concrete security treatment by accounting for the statistical distance between a real-model execution and an ideal-model execution.

  匹配依据：MPC: oblivious transfer

  </details>

- **webSPDZ: Versatile MPC on the Web**
  2025-03-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/487)
  Thomas Buchsteiner, Karl W. Koch, Dragos Rotaru, Christian Rechberger

  <details><summary>摘要 / Abstract</summary>

  Multi-party computation (MPC) has become increasingly practical in the last two decades, solving privacy and security issues in various domains, such as healthcare, finance, and machine learning. One big caveat is that MPC sometimes lacks usability since the knowledge barrier for regular users can be high. Users have to deal with, e.g., various CLI tools, private networks, and sometimes even must install many dependencies, which are often hardware-dependent. A solution to improve the usability of MPC is to build browser-based MPC engines where each party runs within a browser window. Two examples of such an MPC web engine are JIFF and the web variant of MPyC. Both support an honest majority with passive corruptions. $\texttt{webSPDZ}$: Our work brings one of the most performant and versatile general-purpose MPC engines, MP-SPDZ, to the web. MP-SPDZ supports ≥40 MPC protocols with different security models, enabling many security models on the web. To port MP-SPDZ to the web, we use Emscripten to compile MP-SPDZ’s C++ BackEnd to WebAssembly and upgrade the party communication for the browser (WebRTC or WebSockets). We call the new MPC web engine webSPDZ. As with the native versions of the mentioned MPC web engines, MPyC-Web and JIFF, webSPDZ outperforms them in our end-to-end experiments. We believe that webSPDZ brings forth many interesting and practically relevant use cases. Thus, webSPDZ pushes the boundaries of practical MPC: making MPC more usable and enabling it for a broader community.

  匹配依据：MPC: multi party computation

  </details>

- **Free-space Continuous-variable Quantum Secret Sharing**
  2025-03-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.11263)
  Fangli Yang, Liang Chang, Daowen Qiu, Minghua Pan, Wanjun Xiong

  <details><summary>摘要 / Abstract</summary>

  Free-space quantum cryptography has the potential to enable global quantum communication. However, most existing continuous-variable quantum secret sharing (CV-QSS) schemes rely on fiber channels. In this paper, we present a CV-QSS protocol designed for free-space transmission and construct models of crucial parameters, including channel transmittance, excess noise, and interruption probability, thus deriving the bound of the secret key rate. In particular, we provide a multi-source excess noise model for free-space CV-QSS based on the local local oscillator (LLO) scheme and a straightforward optimization of the noise. Furthermore, our research considers the impact of atmospheric turbulence on the protocol. Simulation results demonstrate that the intensification of atmospheric turbulence adversely affects the aforementioned crucial parameters, leading to a significant reduction in the key rate. However, our protocol shows its capability to securely share secrets over a distance of exceeding $60$ km among five participants in the presence of turbulence with $C^2_n=1\times 10^{-15}m^{-2/3}$, while maintaining a high key rate of approximately $0.55$ bit/pulse over a distance of $10$ km across twenty participants. These findings suggest that efficient CV-QSS in free space is indeed achievable. This research may serve as a reference for the design and optimization of the practical CV-QSS system.

  匹配依据：MPC: secret sharing

  </details>

- **Paths Not Taken: A Secure Computing Tutorial**
  2025-03-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2504.16088)
  William Earl Boebert

  <details><summary>摘要 / Abstract</summary>

  This paper is a tutorial on the proven but currently under-appreciated security mechanisms associated with &quot;tagged&quot; or &quot;descriptor&quot; architectures. The tutorial shows how the principles behind such architectures can be applied to mitigate or eliminate vulnerabilities. The tutorial incorporates systems engineering practices by presenting the mechanisms in an informal model of an integrated artifact in its operational environment. The artifact is a special-purpose hardware/software system called a &quot;Guard&quot; which robustly hosts defensive software. It is hoped that this tutorial may encourage teachers to include significant past work in their curricula and students who are self-teaching to add that work to their exploration of secure computing.

  匹配依据：MPC: secure computing

  </details>

- **Multi-Party Computation in Corporate Data Processing: Legal and Technical Insights**
  2025-03-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/463)
  Sebastian Becker, Christoph Bösch, Benjamin Hettwer, Thomas Hoeren, Merlin Rombach, Sven Trieflinger, Hossein Yalame

  <details><summary>摘要 / Abstract</summary>

  This paper examines the deployment of Multi-Party Computation (MPC) in corporate data processing environments, focusing on its legal and technical implications under the European Union’s General Data Protection Regulation (GDPR). By combining expertise in cryptography and legal analysis, we address critical questions necessary for assessing the suitability of MPC for real-world applications. Our legal evaluation explores the conditions under which MPC qualifies as an anonymizing approach under GDPR, emphasizing the architectural requirements, such as the distribution of control among compute parties, to minimize re-identification risks effectively. The assertions put forth in the legal opinion are validated by two distinct assessments conducted independently. We systematically answer key regulatory questions, demonstrating that a structured legal assessment is indispensable for organizations aiming to adopt MPC while ensuring compliance with privacy laws. In addition, we complement this analysis with a practical implementation of privacy-preserving analytics using Carbyne Stack, a cloud-native open-source platform for scalable MPC applications, which integrates the MP-SPDZ framework as its backend. We benchmark SQL queries under various security models to evaluate scalability and efficiency.

  匹配依据：MPC: multi party computation

  </details>

- **Faithful and Privacy-Preserving Implementation of Average Consensus**
  2025-03-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.09381)
  Kaoru Teranishi, Kiminao Kogiso, Takashi Tanaka

  <details><summary>摘要 / Abstract</summary>

  We propose a protocol based on mechanism design theory and encrypted control to solve average consensus problems among rational and strategic agents while preserving their privacy. The proposed protocol provides a mechanism that incentivizes the agents to faithfully implement the intended behavior specified in the protocol. Furthermore, the protocol runs over encrypted data using homomorphic encryption and secret sharing to protect the privacy of agents. We also analyze the security of the proposed protocol using a simulation paradigm in secure multi-party computation. The proposed protocol demonstrates that mechanism design and encrypted control can complement each other to achieve security under rational adversaries.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **CIPHERMATCH: Accelerating Homomorphic Encryption-Based String Matching via Memory-Efficient Data Packing and In-Flash Processing**
  2025-03-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.08968)
  Mayank Kabra, Rakesh Nadig, Harshita Gupta, Rahul Bera, Manos Frouzakis, Vamanan Arulchelvan, Yu Liang, Haiyu Mao, Mohammad Sadrosadati, Onur Mutlu

  <details><summary>摘要 / Abstract</summary>

  Homomorphic encryption (HE) allows secure computation on encrypted data without revealing the original data, providing significant benefits for privacy-sensitive applications. Many cloud computing applications (e.g., DNA read mapping, biometric matching, web search) use exact string matching as a key operation. However, prior string matching algorithms that use homomorphic encryption are limited by high computational latency caused by the use of complex operations and data movement bottlenecks due to the large encrypted data size. In this work, we provide an efficient algorithm-hardware codesign to accelerate HE-based secure exact string matching. We propose CIPHERMATCH, which (i) reduces the increase in memory footprint after encryption using an optimized software-based data packing scheme, (ii) eliminates the use of costly homomorphic operations (e.g., multiplication and rotation), and (iii) reduces data movement by designing a new in-flash processing (IFP) architecture. We demonstrate the benefits of CIPHERMATCH using two case studies: (1) Exact DNA string matching and (2) encrypted database search. Our pure software-based CIPHERMATCH implementation that uses our memory-efficient data packing scheme improves performance and reduces energy consumption by 42.9X and 17.6X, respectively, compared to the state-of-the-art software baseline. Integrating CIPHERMATCH with IFP improves performance and reduces energy consumption by 136.9X and 256.4X, respectively, compared to the software-based CIPHERMATCH implementation.

  匹配依据：MPC: secure computation

  </details>

- **Verifiable Secret Sharing Based on Fully Batchable Polynomial Commitment for Privacy-Preserving Distributed Computation**
  2025-03-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/453)
  Xiangyu Kong, Min Zhang, Yu Chen

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving distributed computation enables a resource-limited client to securely delegate computations on sensitive data to multiple servers by distributing shares of the data. In such systems, verifiable secret sharing (VSS) is a fundamental component, ensuring secure data distribution and directly impacting the overall performance. The most practical approach to construct VSS is through polynomial commitment (PC), with two main research directions to improve the VSS efficiency. The first focuses on improving the dealer time by designing PC that supports batch evaluation, i.e., generating multiple evaluation$\&amp;$proof pairs in one shot. The second aims to reduce the broadcast cost by designing PC that supports batch opening, i.e., producing a compact proof for multiple evaluations. Recently, Zhang et al. (Usenix Security 2022) proposed a transparent PC that supports batch evaluation and obtained a transparent VSS with optimal dealer time. However, their scheme does not support batch opening, leading to high broadcast costs in VSS. To the best of our knowledge, no transparent PC currently supports both batch evaluation and batch opening, thus limiting the performance of existing VSS schemes. In this paper, we propose a transparent fully batchable polynomial commitment (TFB-PC), that simultaneously supports batch evaluation and batch opening. Leveraging TFB-PC, we present a VSS scheme with optimal complexity: $O(n\log n)$ dealer time, $O(n)$ participant time and $O(n)$ communication cost. Furthermore, we implement our VSS scheme and compare its performance with Zhang et al.’s VSS (the naive approach). Results show that our scheme achieves $954\text{-}27,595\times$ reduction in communication cost and a $1,028\text{-}1,155,106\times$ speed up in participant time for $2^{11}$-$2^{21}$ parties.

  匹配依据：MPC: secret sharing

  </details>

- **Achieving Data Reconstruction Hardness and Efficient Computation in Multiparty Minimax Training**
  2025-03-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/460)
  Truong Son Nguyen, Yi Ren, Guangyu Nie, Ni Trieu

  <details><summary>摘要 / Abstract</summary>

  Generative models have achieved remarkable success in a wide range of applications. Training such models using proprietary data from multiple parties has been studied in the realm of federated learning. Yet recent studies showed that reconstruction of authentic training data can be achieved in such settings. On the other hand, multiparty computation (MPC) guarantees standard data privacy, yet scales poorly for training generative models. In this paper, we focus on improving reconstruction hardness during Generative Adversarial Network (GAN) training while keeping the training cost tractable. To this end, we explore two training protocols that use a public generator and an MPC discriminator: Protocol 1 (P1) uses a fully private discriminator, while Protocol 2 (P2) privatizes the first three discriminator layers. We prove reconstruction hardness for P1 and P2 by showing that (1) a public generator does not allow recovery of authentic training data, as long as the first two layers of the discriminator are private; and through an existing approximation hardness result on ReLU networks, (2) a discriminator with at least three private layers does not allow authentic data reconstruction with algorithms polynomial in network depth and size. We show empirically that compared with fully MPC training, P1 reduces the training time by $2\times$ and P2 further by $4-16\times$.

  匹配依据：MPC: multiparty computation

  </details>

- **A Democratic Distributed Post-Quantum Certificateless Encryption Scheme**
  2025-03-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/456)
  Thomas Prévost, Bruno Martin, Olivier Alibart

  <details><summary>摘要 / Abstract</summary>

  We propose a post-quantum certificateless encryption scheme based on a web of trust instead of a centralized Key Generation Center. Our scheme allows nodes to communicate securely. It is the nodes already present in the network that vote on the acceptance of new nodes, and agree on the shared key. The threshold required for the acceptance of a new node is configurable. Our protocol thus allows to completely operate without the Key Generation Center (or Key Distribution Center). Our scheme is based on Quasi-Cyclic Moderate Density Parity Check Code McEliece, which is resistant to quantum computer attacks. The voting system uses Shamir secret sharing, coupled with the Kabatianskii-Krouk-Smeets signature scheme, both are also resistant to quantum computer attacks. We provide a security analysis of our protocol, as well as a formal verification and a proof of concept code.

  匹配依据：MPC: secret sharing

  </details>

- **Concretely Efficient Correlated Oblivious Permutation**
  2025-03-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/449)
  Feng Han, Xiao Lan, Weiran Liu, Lei Zhang, Hao Ren, Lin Qu, Yuan Hong

  <details><summary>摘要 / Abstract</summary>

  Oblivious permutation (OP) enables two parties, a sender with a private data vector $x$ and a receiver with a private permutation π, to securely obtain the shares of π(x). OP has been used to construct many important MPC primitives and applications such as secret shuffle, oblivious sorting, private set operations, secure database analysis, and privacy-preserving machine learning. Due to its high complexity, OP has become a performance bottleneck in several practical applications, and many efforts have been devoted to enhancing its concrete efficiency. Chase et al. (Asiacrypt&#x27;20) proposed an offline-online OP paradigm leveraging a pre-computable resource termed Share Translation. While this paradigm significantly reduces online costs, the substantial offline cost of generating Share Translation remains an area for further investigation. In this work, we redefine the pre-computable resource as a cryptographic primitive known as Correlated Oblivious Permutation (COP) and conduct in-depth analyses and optimizations of the two COP generation solutions: network-based solution and matrix-based solution. The optimizations for the network-based solution halve the communication/computation cost of constructing a switch (the basic unit of the permutation network) and reduce the number of switches in the permutation network. The optimizations for the matrix-based solution halve the communication cost of small-size COP generation and reduce the cost of large-size COP generation with in-outside permutation decomposition. We implement our two COP generation protocols and conduct comprehensive evaluations. Taking commonly used 128-bit input data as an example, our network-based and matrix-based solutions are up to 1.7x and 1.6x faster than baseline protocols, respectively. We further facilitate the state-of-the-art (SOTA) PSU protocols with our optimized COP, achieving over 25% reduction in communication cost and 35% decrease in execution time. This shows that our COP optimizations bring significant improvements for real-world MPC primitives.

  匹配依据：MPC: mpc (context)

  </details>

- **A Failure-Free and Efficient Discrete Laplace Distribution for Differential Privacy in MPC**
  2025-03-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.07048)
  Ivan Tjuawinata, Jiabo Wang, Mengmeng Yang, Shanxiang Lyu, Huaxiong Wang, Kwok-Yan Lam

  <details><summary>摘要 / Abstract</summary>

  In an MPC-protected distributed computation, although the use of MPC assures data privacy during computation, sensitive information may still be inferred by curious MPC participants from the computation output. This can be observed, for instance, in the inference attacks on either federated learning or a more standard statistical computation with distributed inputs. In this work, we address this output privacy issue by proposing a discrete and bounded Laplace-inspired perturbation mechanism along with a secure realization of this mechanism using MPC. The proposed mechanism strictly adheres to a zero failure probability, overcoming the limitation encountered on other existing bounded and discrete variants of Laplace perturbation. We provide analyses of the proposed differential privacy (DP) perturbation in terms of its privacy and utility. Additionally, we designed MPC protocols to implement this mechanism and presented performance benchmarks based on our experimental setup. The MPC realization of the proposed mechanism exhibits a complexity similar to the state-of-the-art discrete Gaussian mechanism, which can be considered an alternative with comparable efficiency while providing stronger differential privacy guarantee. Moreover, efficiency of the proposed scheme can be further enhanced by performing the noise generation offline while leaving the perturbation phase online.

  匹配依据：MPC: mpc (context)

  </details>

- **The Beginner's Textbook for Fully Homomorphic Encryption**
  2025-03-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.05136)
  Ronny Ko

  <details><summary>摘要 / Abstract</summary>

  Fully Homomorphic Encryption (FHE) is a cryptographic scheme that enables computations to be performed directly on encrypted data, as if the data were in plaintext. After all computations are performed on the encrypted data, it can be decrypted to reveal the result. The decrypted value matches the result that would have been obtained if the same computations were applied to the plaintext data. FHE supports basic operations such as addition and multiplication on encrypted numbers. Using these fundamental operations, more complex computations can be constructed, including subtraction, division, logic gates (e.g., AND, OR, XOR, NAND, MUX), and even advanced mathematical functions such as ReLU, sigmoid, and trigonometric functions (e.g., sin, cos). These functions can be implemented either as exact formulas or as approximations, depending on the trade-off between computational efficiency and accuracy. FHE enables privacy-preserving machine learning by allowing a server to process the client&#x27;s data in its encrypted form through an ML model. With FHE, the server learns neither the plaintext version of the input features nor the inference results. Only the client, using their secret key, can decrypt and access the results at the end of the service protocol. FHE can also be applied to confidential blockchain services, ensuring that sensitive data in smart contracts remains encrypted and confidential while maintaining the transparency and integrity of the execution process. Other applications of FHE include secure outsourcing of data analytics, encrypted database queries, privacy-preserving searches, efficient multi-party computation for digital signatures, and more. A dynamic website version is available at (https://fhetextbook.github.io). Please report any bugs or errors to the Github issues board.

  匹配依据：MPC: multi party computation

  </details>

- **Multiparty Garbling from OT with Linear Scaling and RAM Support**
  2025-03-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/444)
  David Heath, Vladimir Kolesnikov, Varun Narayanan, Rafail Ostrovsky, Akash Shah

  <details><summary>摘要 / Abstract</summary>

  State-of-the-art protocols that achieve constant-round secure multiparty computation currently present a trade-off: either consume an amount of communication that scales quadratically in the number of parties, or achieve better asymptotics at the cost of high constant factors (e.g. schemes based on LPN or DDH). We construct a constant-round MPC protocol where communication scales linearly in the number of parties n. Our construction relies only on OT and RO, and it leverages packed secret sharing. Due to building on simple primitives, our protocol offers concrete improvement over asymptotically-efficient LPN-based schemes. We consider security in the presence of a dishonest majority where the malicious (with abort) adversary corrupts an arbitrary constant fraction of parties. By leveraging tri-state circuits (Heath et al. Crypto 2023), we extend our protocol to the RAM model of computation. For a RAM program that halts within $T$ steps, our maliciously-secure protocol communicates $O(n \cdot T \log^3 T \log \log T \cdot \kappa)$ total bits, where $\kappa$ is a security parameter.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Private Computation on Common Fuzzy Records**
  2025-03-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/422)
  Kyoohyung Han, Seongkwang Kim, Yongha Son

  <details><summary>摘要 / Abstract</summary>

  Private computation on common records refers to analyze data from two databases containing shared records without revealing personal information. As a basic requirement for private computation, the databases involved essentially need to be aligned by a common identification system. However, it is hard to expect such common identifiers in real world scenario. For this reason, multiple quasi-identifiers can be used to identify common records. As some quasi-identifiers might be missing or have typos, it is important to support fuzzy records setting. Identifying common records using quasi-identifiers requires manipulation of highly sensitive information, which could be privacy concerns. This work studies the problem of enabling such data analysis on the fuzzy records of quasi-identifiers. To this end, we propose ordered threshold-one (OTO) matching which can be efficiently realized by circuit-based private set intersection (CPSI) protocols and some multiparty computation (MPC) techniques. Furthermore, we introduce some generic encoding techniques from traditional matching rules to the OTO matching. Finally, we achieve a secure efficient private computation protocol which supports various matching rules which have already been widely used. We also demonstrate the superiority of our proposal with experimental validation. First, we empirically check that our encoding to OTO matching does not affect accuracy a lot for the benchmark datasets found in the fuzzy record matching literature. Second, we implement our protocol and achieve significantly faster performance at the cost of communication overhead compared to previous privacy-preserving record linkage (PPRL) protocols. In the case of 100K records for each dataset, our work shows 147.58MB communication cost, 10.71s setup time, and 1.97s online time, which is 7.78 times faster compared to the previous work (50.12 times faster when considering online time only).

  匹配依据：MPC: multiparty computation, private set intersection

  </details>

- **Matchmaker: Fast Secure Inference across Deployment Scenarios**
  2025-03-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/424)
  Neha Jawalkar, Nishanth Chandran, Divya Gupta, Rahul Sharma, Arkaprava Basu

  <details><summary>摘要 / Abstract</summary>

  Secure Two-Party Computation (2PC) enables secure inference with cryptographic guarantees that protect the privacy of the model owner and client. However, it adds significant performance overhead. In this work, we make 2PC-based secure inference efficient while considering important deployment scenarios. We observe that the hitherto unconsidered latency of fetching keys from storage significantly impacts performance, as does network speed. We design a Linear Secret Sharing (LSS)-based system $LSS^M$ and a Function Secret Sharing (FSS)-based system $FSS^M$ for secure inference, optimized for small key size and communication, respectively. Notably, our highly-optimized and hardware-aware CPU-based $LSS^M$ outperforms prior GPU-based LSS systems by up to $50\times$. We then show that the best choice between $LSS^M$ and $FSS^M$ depends on the deployment scenario. In fact, under certain deployments, a combination of $LSS^M$ and $FSS^M$ can leverage heterogeneous processing across CPU and GPU. Such protocol-system co-design lets us outperform state-of-the-art secure inference systems by up to $21\times$ (geomean $3.25\times$).

  匹配依据：MPC: secret sharing, secure two party computation

  </details>

- **A Note on the Blindness of the Scheme from ePrint 2025/397**
  2025-03-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/425)
  Lucjan Hanzlik

  <details><summary>摘要 / Abstract</summary>

  This note demonstrates that the blind signature scheme based on cryptographic group actions, as proposed in ePrint paper 2025/397, fails to ensure blindness. Specifically, we construct an adversary that achieves a $1/8$ advantage in the blindness experiment. The attack leverages selective abort techniques (also known as selective failure attacks), a well-known strategy in the MPC literature.

  匹配依据：MPC: mpc (context)

  </details>

- **Low Communication Threshold FHE from Standard (Module-)LWE**
  2025-03-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/409)
  Hiroki Okada, Tsuyoshi Takagi

  <details><summary>摘要 / Abstract</summary>

  Threshold fully homomorphic encryption (ThFHE) is a multi-party extension of FHE; any subset of at least $T$ out of $N$ parties can decrypt the ciphertexts by combining their decryption shares. Recently, Passelègue and Stehlé (Asiacrypt 2024) presented a ThFHE scheme with polynomially short decryption shares from the ``known-norm&#x27;&#x27; variant of learning with errors (LWE) assumption, in which the norm of the secret key is leaked to the adversary. While known-norm LWE is reduced from standard LWE, its module extension, known-covariance module-LWE (MLWE), lacks a known reduction from standard MLWE. Hence, extending their ThFHE scheme to the MLWE-based construction remains an open question. In this paper, we address this open problem: We construct a ThFHE scheme with polynomially small decryption shares from standard LWE/MLWE. Our core technique, which we call noise padding, eliminates the need of known-norm variants of LWE. We distribute shares of a padding noise and use them to adjust the distribution of decryption noise so that no information about the secret key is leaked. Furthermore, our ThFHE efficiently realizes arbitrary $T$-out-of-$N$ threshold decryption via simple Shamir secret sharing instead of $\{0,1\}$-linear secret sharing. Hence, the sizes of the keys, ciphertexts and decryption shares in our scheme are compact: they are $O(1)$ w.r.t. the number of parties $N$.

  匹配依据：MPC: secret sharing

  </details>

- **Garblet: Multi-party Computation for Protecting Chiplet-based Systems**
  2025-03-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/413)
  Mohammad Hashemi, Shahin Tajik, Fatemeh Ganji

  <details><summary>摘要 / Abstract</summary>

  The introduction of shared computation architectures assembled from heterogeneous chiplets introduces new security threats. Due to the shared logical and physical resources, an untrusted chiplet can act maliciously to surreptitiously probe the data communication between chiplets or sense the computation shared between them. This paper presents Garblet, the first framework to leverage the flexibility offered by chiplet technology and Garbled Circuits (GC)-based MPC to enable efficient, secure computation even in the presence of potentially compromised chiplets. Our approach integrates a customized hardware Oblivious Transfer (OT) module and an optimized evaluator engine into chiplet-based platforms. This configuration distributes the tasks of garbling and evaluating circuits across two chiplets, reducing communication costs and enhancing computation speed. We implement this framework on an AMD/Xilinx UltraScale+ multi-chip module and demonstrate its effectiveness using benchmark functions. Additionally, we introduce a novel circuit decomposition technique that allows for parallel processing across multiple chiplets to further improve computational efficiency. Our results highlight the potential of chiplet systems for accelerating GC (e.g., the time complexity of garbled AES is 0.0226ms) in order to guarantee the security and privacy of the computation on chiplets.

  匹配依据：MPC: garbled circuits, multi party computation, oblivious transfer, secure computation

  </details>

- **Client-Aided Secure Two-Party Computation of Dynamic Controllers**
  2025-03-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2503.02176)
  Kaoru Teranishi, Takashi Tanaka

  <details><summary>摘要 / Abstract</summary>

  In this paper, we propose a secure two-party computation protocol for dynamic controllers using a secret sharing scheme. The proposed protocol realizes outsourcing of controller computation to two servers, while controller parameters, states, inputs, and outputs are kept secret against the servers. Unlike previous encrypted controls in a single-server setting, the proposed method can operate a dynamic controller for an infinite time horizon without controller state decryption or input re-encryption. We show that the control performance achievable by the proposed protocol can be made arbitrarily close to that attained by the unencrypted controller. Furthermore, system-theoretic and cryptographic modifications of the protocol are presented to improve the communication complexity. The feasibility of the protocol is demonstrated through numerical examples of PID and observer-based controls.

  匹配依据：MPC: secret sharing, secure two party computation

  </details>

- **Re-Randomize and Extract: A Novel Commitment Construction Framework Based on Group Actions**
  2025-03-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/400)
  Kaijie Jiang, Anyu Wang, Hengyi Luo, Guoxiao Liu, Tang Gang, Yanbin Pan, Xiaoyun Wang

  <details><summary>摘要 / Abstract</summary>

  Cryptographic group actions have attracted growing attention as a useful tool for constructing cryptographic schemes. Among their applications, commitment schemes are particularly interesting as fundamental primitives, playing a crucial role in protocols such as zero-knowledge proofs, multi-party computation, and more. In this paper, we introduce a novel framework to construct commitment schemes based on cryptographic group actions. Specifically, we propose two key techniques for general group actions: re-randomization and randomness extraction. Roughly speaking, a re-randomization algorithm introduces randomness within an orbit for any input element, while a randomness extractor maps this randomness to uniformity over the message space. We demonstrate that these techniques can significantly facilitate the construction of commitment schemes, providing a flexible framework for constructing either perfectly hiding or perfectly binding commitments, depending on the type of extractor involved. Moreover, we extend our framework to support the construction of commitments with additional desirable properties beyond hiding and binding, such as dual-mode commitments and enhanced linkable commitments. These extensions are achieved by further adapting the extractor to satisfy trapdoor or homomorphic properties. Finally, we instantiate all our proposed commitment schemes using lattices, specifically leveraging the lattice isomorphism problem (LIP) and the lattice automorphism problem (LAP) as underlying cryptographic assumptions. To the best of our knowledge, this is the first commitment scheme construction based on LIP/LAP. Additionally, we use LIP to provide a repair and improvement to the tensor isomorphism-based non-interactive commitment scheme proposed by D&#x27;Alconzo, Flamini, and Gangemi (ASIACRYPT 2023), which was recently shown to be insecure by an attack from Gilchrist, Marco, Petit, and Tang (CRYPTO 2024).

  匹配依据：MPC: multi party computation

  </details>

- **PEGASIS: Practical Effective Class Group Action using 4-Dimensional Isogenies**
  2025-03-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/401)
  Pierrick Dartois, Jonathan Komada Eriksen, Tako Boris Fouotsa, Arthur Herlédan Le Merdy, Riccardo Invernizzi, Damien Robert, Ryan Rueger, Frederik Vercauteren, Benjamin Wesolowski

  <details><summary>摘要 / Abstract</summary>

  In this paper, we present the first practical algorithm to compute an effective group action of the class group of any imaginary quadratic order $\mathcal{O}$ on a set of supersingular elliptic curves primitively oriented by $\mathcal{O}$. Effective means that we can act with any element of the class group directly, and are not restricted to acting by products of ideals of small norm, as for instance in CSIDH. Such restricted effective group actions often hamper cryptographic constructions, e.g. in signature or MPC protocols. Our algorithm is a refinement of the Clapoti approach by Page and Robert, and uses $4$-dimensional isogenies. As such, it runs in polynomial time, does not require the computation of the structure of the class group, nor expensive lattice reductions, and our refinements allows it to be instantiated with the orientation given by the Frobenius endomorphism. This makes the algorithm practical even at security levels as high as CSIDH-4096. Our implementation in SageMath takes 1.5s to compute a group action at the CSIDH-512 security level, 21s at CSIDH-2048 level and around 2 minutes at the CSIDH-4096 level. This marks the first instantiation of an effective cryptographic group action at such high security levels. For comparison, the recent KLaPoTi approach requires around 200s at the CSIDH-512 level in SageMath and 2.5s in Rust.

  匹配依据：MPC: mpc (context)

  </details>

- **On the (In)security of Approximate Computation Protocols from CKKS**
  2025-03-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/395)
  Intak Hwang, Yisol Hwang, Miran Kim, Dongwon Lee, Yongsoo Song

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation (MPC) enables collaborative and privacy-preserving computation over private inputs. Recent advances in Homomorphic Encryption (HE), particularly the CKKS scheme, have significantly improved the practicality of secure computation, making it suitable for real-world applications involving approximate arithmetic. However, the inherent errors introduced by CKKS pose substantial challenges in the design and analysis of CKKS-based secure computation protocols. In this work, we investigate the correctness and security of existing CKKS-based MPC protocols. Most prior constructions rely on the noise smudging technique, in which each party independently adds exponentially large noise to the output to guarantee the security of the protocol. However, we show that this approach does not achieve standard simulation-based security for MPC. To address this limitation, we apply an alternative method, called collaborative sampling, in which all participating parties jointly generate additive shares of the smudging noise. We consider both asymmetric two-party protocols between a client and a server, and symmetric multiparty protocols among mutually distrusting parties. For each setting, we present concrete protocol constructions based on collaborative sampling, explicitly define the corresponding ideal functionalities, and provide formal security proofs. We further provide concrete constructions and implementations of collaborative sampling protocols. As an alternative perspective, we show that existing protocols, despite failing to achieve standard simulation-based security, still satisfy a weaker security notion called liberal security for approximate MPC protocols.

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **Computational Quantum Anamorphic Encryption and Anamorphic Secret Sharing**
  2025-03-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/399)
  SAYANTAN GANGULY, Shion Samadder Chaudhury

  <details><summary>摘要 / Abstract</summary>

  The concept of anamorphic encryption, first formally introduced by Persiano et al. in their influential 2022 paper titled ``Anamorphic Encryption: Private Communication Against a Dictator,&#x27;&#x27; enables embedding covert messages within ciphertexts. One of the key distinctions between a ciphertext embedding a covert message and an original ciphertext, compared to an anamorphic ciphertext, lies in the indistinguishability between the original ciphertext and the anamorphic ciphertext. This encryption procedure has been defined based on a public-key cryptosystem. Initially, we present a quantum analogue of the classical anamorphic encryption definition that is based on public-key encryption. Additionally, we introduce a definition of quantum anamorphic encryption that relies on symmetric key encryption. Furthermore, we provide a detailed generalized construction of quantum anamorphic symmetric key encryption within a general framework, which involves taking any two quantum density matrices of any different dimensions and constructing a single quantum density matrix, which is the quantum anamorphic ciphertext containing ciphertexts of both of them. Subsequently, we introduce a definition of computational anamorphic secret-sharing and extend the work of \c{C}akan et al. on computational quantum secret-sharing to computational quantum anamorphic secret-sharing, specifically addressing scenarios with multiple messages, multiple keys, and a single share function. This proposed secret-sharing scheme demonstrates impeccable security measures against quantum adversaries.

  匹配依据：MPC: secret sharing

  </details>
