# MPC & TEE 论文目录

覆盖安全多方计算、相关密码协议、可信执行环境及机密计算。

[最近运行状态](reports/latest-run.md) · [项目说明](README.md)

自动筛选结果，建议按匹配依据人工复核；arXiv 和 IACR ePrint 是预印本来源。

共 **634** 篇去重论文。

## MPC + TEE（2）

### 2026

- **SENTRA:Privacy-Preserving Training in Outsourced Cloud Environments**
  2026-07-15 · MPC / TEE · [IACR ePrint](https://eprint.iacr.org/2026/1443)
  Maryam Zarezadeh, Jana Eisoldt, Bhavish Mohee, Stefan Köpsell, Behzad Abdolmaleki

  <details><summary>摘要 / Abstract</summary>

  Training machine learning models in untrusted clouds requires strong guarantees of confidentiality, integrity, and correctness, while remaining scalable and resilient to node churn. These challenges are further amplified in emerging agentic AI systems, where autonomous and distributed learning components require trustworthy coordination and secure state management across heterogeneous cloud environments. Existing Trusted Execution Environments (TEEs) lack scalability and remain vulnerable to side-channel attacks for large workloads, while pure secure multi-party computation (MPC) approaches incur prohibitive overhead in practice. SENTRA (Secure ENclave-based TRaining Architecture) addresses these challenges through a hybrid architecture that combines TEEs, secret sharing, and communication-efficient MPC with system level mechanisms that secure the entire training lifecycle. SENTRA introduces a scalable collective attestation protocol that verifies all participating enclaves and enforces hardware exclusivity before any node may store or process secret shares. Training data and model parameters are stored as secret shares in a versioned enclave-backed key–value store (KVS), providing rollback protection and consistent state under adversarial conditions. SENTRA further supports dynamic, fault tolerant membership through Dynamic Proactive Secret Sharing (DPSS)-based resharing, safe packed-MPC computation under degree bounds, and adaptive handling of node failures. Evaluation of a prototype implementation shows that SENTRA achieves up to 8.89 samples/s throughput and 1.29× faster training than the CrypTen baseline in software-only mode. In hardware-enclave mode, SENTRA incurs only an 8.3% performance overhead while providing memory-isolated confidentiality, fault-tolerant membership management, rollback protection, and recovery from node failures in approximately 8 seconds.

  匹配依据：MPC: secret sharing, secure multi party computation; TEE: hardware enclave, secure enclave, trusted execution environments

  </details>

- **Loricae: Upgrading and Optimizing Multi-Party Computation Protocols with Filmy Hardware Enclaves.**
  2026 · MPC / TEE · [TCHES](https://doi.org/10.46586/TCHES.V2026.I2.73-105)
  Xiaoyu Fan, Mingyu Gao, Yifan Song, Xiang Li, Weijie Liu, Baiting Jiang

## MPC（480）

### 2026

- **Rerandomizable Garbling Beyond BHHO-KMHE and a Construction from LWE**
  2026-10-28 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2664)
  Raphael Heitjohann, Jonas von der Heyden, Tibor Jager

  <details><summary>摘要 / Abstract</summary>

  Rerandomizable garbling schemes (RGS) are a fundamental primitive enabling advanced cryptographic constructions such as multi-hop homomorphic encryption (Gentry, Halevi, Vaikuntanathan, CRYPTO 2010), iO-combiners (Ananth, Jain, Naor, Sahai, Yogev, CRYPTO 2016), and YOSO-style MPC (Acharya, Hazay, Kolesnikov, Prabhakaran, TCC 2022 and CRYPTO 2024). All known RGS instantiations rely on discrete-logarithm-type assumptions, concretely via the BHHO scheme (Boneh, Halevi, Hamburg, Ostrovsky, CRYPTO 2008) and its recent pairing-based variant (Heitjohann, von der Heyden, Jager, CRYPTO 2025). This reliance stems from the use of key-and-message homomorphic encryption (KMHE) that supports rerandomization and strong &quot;key-privacy under leakage&quot;, which hides the applied homomorphic transformations and is currently only achievable using BHHO-style bitwise encryption in combination with permutation-based homomorphisms. Our first main contribution is a new garbling technique that shifts the burden of hiding homomorphic transformations from the encryption scheme to the garbling itself. This allows us to construct RGS from KMHE schemes with substantially weaker properties, avoiding the need for bitwise encryption and permutation-based homomorphisms, and enabling the construction of RGS from KMHE with other homomorphisms, such as additively-homomorphic ones. As a second contribution, we give a concrete lattice-based instantiation of the required KMHE primitive, based on LWE. This construction is a variant of the GSW FHE scheme (Gentry, Sahai, Waters, CRYPTO 2013), which uses new techniques for rerandomization and is tailored to the requirements of our new garbling scheme by supporting a &quot;homomorphic&quot;/&quot;lossy&quot; mode. This yields the first RGS construction that does not rely on discrete-logarithm assumptions and may provide post-quantum security.

  匹配依据：MPC: garbling scheme, garbling schemes

  </details>

- **OblivDGL: Oblivious Deep Graph Learning Made Practical**
  2026-10-27 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2655)
  Yiming Qin, Xiaoning Liu, Shangqi Lai, Joseph K. Liu, Xingliang Yuan

  <details><summary>摘要 / Abstract</summary>

  The rapid deployment of Graph Neural Networks (GNNs) within Machine Learning as a Service (MLaaS) has opened up new privacy concerns. Both sensitive graph data and proprietary GNN models are submitted to and processed in third-party MLaaS platform for training and inference. To alleviate those concerns, recent efforts have been made to design tailored secure computation protocols for GNNs. Unfortunately, existing designs cannot accomplish security, functionality, and scalability simultaneously. They leak a certain degree of graph information, offer limited support on secure training of GNNs, and can hardly scale to large graphs. In this paper, we design and implement OblivDGL, an oblivious deep graph learning framework for secure GNN inference and training. Our design is inspired by Deep Graph Library (DGL), an industrial practice for graph learning. At its core, we distill the secure computational patterns of GNNs into a generalized form, and empower both secure GNN training and inference through a novel oblivious message passing paradigm. To realize such a paradigm, we design a new oblivious graph representation, and realize it by function secret sharing (FSS), a lightweight secure computation technique with low latency. Compared to prior secure GNN systems, OblivDGL achieves the most stringent privacy guarantees, i.e., revealing no private information except for the total number of edges and nodes. One standout feature of OblivDGL is the scalability of processing encrypted graphs by carefully tailored parallelization designs. Extensive evaluations on four benchmark graph datasets demonstrate that, compared to state-of-the-art secure GNN frameworks, OblivDGL reduces communication cost by up to 1024x and achieves up to 14.3x speedup in runtime during secure training. For secure inference, OblivDGL achieves up to 754x lower communication and a 4.19x speedup.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Asynchronous Verifiable and Complete Secret Sharing: From Design Patterns to System-Level Trade-offs**
  2026-10-27 · MPC · [arXiv](https://arxiv.org/abs/2610.37234)
  Joachim Bruneau-Queyreix, Martin Zivojinovic, Leo Mendiboure, Tom Claudel, Laurent Réveillère

  <details><summary>摘要 / Abstract</summary>

  Modern secret sharing protocols promise robust secret sharing in fully asynchronous Byzantine systems, but their practical costs remain difficult to compare across papers, assumptions, and workloads. The difficulty is not merely experimental: protocols with similar asymptotic guarantees often place very different work on the critical path through their choices of dissemination, verification, batching, and recovery. This paper turns that fragmented research landscape into a corpus-backed designspace analysis and systems evaluation of asynchronous verifiable and complete secret sharing. We derive a design sieve, select seven representative protocols, and implement them in a common Rust framework. In our experiments on the Grid&#x27;5000 platform, we evaluate honest-dealer and faulty-dealer stress executions using latency, throughput, message count, bandwidth, and aggregate CPU-time. The results show that message complexity alone poorly predicts latency, that optimistic paths can be dominated by recovery cost, and that batching or packing helps only when verification stays off the critical path. These findings turn protocol-by-protocol comparisons into design-to-cost guidance for choosing, implementing, and extending asynchronous verifiable and complete sharing protocols.

  匹配依据：MPC: secret sharing

  </details>

- **Reverse Substitution in Secret Sharing: The Critical One-Half Threshold and a Route to Superpolynomial Lower Bounds**
  2026-10-26 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2652)
  Shahram Khazaei

  <details><summary>摘要 / Abstract</summary>

  The contribution vector (convec) of a secret-sharing scheme is the vector of its normalized share sizes. The average and maximum coordinates of a convec give, respectively, the average and maximum information ratios of the scheme. Obtaining superlinear lower bounds on these quantities for unrestricted perfect secret sharing has remained a challenging open problem for about four decades. In this paper, we study substitution, a natural way to build complicated access structures from simpler ones: one participant of an outer access structure is replaced by an inner access structure. Given secret-sharing schemes for the two factors, the standard forward construction composes them into a scheme for the composite access structure. We study the converse question. Given an arbitrary scheme for the composite access structure, we ask to what extent its convec admits a reverse factorization into convecs for the outer and inner factors, up to a common multiplicative loss. Exact reversal is false: we give a counterexample whose optimal reverse factor is \(8/9\), with a composite scheme that is scalar-linear over every finite field. On the positive side, we prove that a factor \(1/2\) is always attainable, and that every fixed instance admits a strictly larger factor. For a recursive family built from Csirmaz’s classical access structure \(\mathcal C_k\), whose distinguished set has size \(k\), we identify a critical reverse factor that determines when the resulting lower bound becomes superlinear. This critical factor exceeds one half by only an amount of order \((\log k)/k\). Crossing it yields superlinear lower bounds, while any fixed positive excess above one half gives a route to superpolynomial lower bounds. Using only Shannon inequalities, the corresponding recursive factor cannot cross the critical value. Thus any improvement sufficient to pass this threshold must exploit constraints beyond the Shannon inequalities.

  匹配依据：MPC: secret sharing

  </details>

- **Minimality of Binary Codes From Weight Layers and Graph Cut Spaces**
  2026-10-26 · MPC · [arXiv](https://arxiv.org/abs/2610.35372)
  Xianhong Xie, Mengni Wang, Tingting Wu

  <details><summary>摘要 / Abstract</summary>

  Minimal binary linear codes play an important role in secret-sharing schemes and in the structural study of linear codes. We study the minimality of three classes of known constructions: codes from a single complete Hamming-weight layer, codes from arbitrary unions of such layers and graph cut-space codes. For the previously studied single-layer codes C, we give a complete minimality classification: C is minimal if and only if t is even. For t = 4, we determine the minimum and maximum weights, and show that the family strictly violates the binary Ashikhmin Barg sufficient condition for every k. We also calculate the minimum distance of the dual code. For arbitrary unions of complete Hamming-weight layers, we obtain an if-and-only-if classification of minimality and uniform criteria for evenness, self-orthogonality, the doubly even property and hull dimension. We further analyze the family for odd k. Finally, using the classical bond characterization of cuts, we translate minimality of graph cut space codes into a graph-theoretic condition: a nonempty simple graph has a minimal cut code precisely when it has one edge-containing component and that component is complete. We also give a graph-function realization of the known binary tetrahedron code and explicitly identify the resulting code equivalence.

  匹配依据：MPC: secret sharing

  </details>

- **Information-Theoretic Secure Aggregation With Heterogeneous Client Quantization**
  2026-10-26 · MPC · [arXiv](https://arxiv.org/abs/2610.35833)
  Shreya Meel, Sennur Ulukus, Itzhak Tamo

  <details><summary>摘要 / Abstract</summary>

  In federated learning (FL), secure aggregation enables a server to compute the sum of local model updates of $N$ clients, without revealing any information on the individual model updates to the server, beyond their sum. Different clients may be subject to heterogeneous bandwidth constraints, and consequently may choose different numbers of quantization levels to represent the information they send. Most secure aggregation works require the clients to project the values of their update parameters to a common finite group (or field), which does not directly accommodate heterogeneous precision constraints on their transmitted masked updates. Existing approaches of secure aggregation with heterogeneous quantization levels reveal partial aggregates of model-updates, and can reveal segments of individual model updates, under certain dropout and client-server collusion patterns. To prevent this privacy breach, we propose an information-theoretic secure aggregation scheme that tolerates client drop-outs, and up to $T$ semi-honest clients that collude with each other and with the server, under heterogeneous quantization at clients. Our protocol utilizes the $(T+1, N)$ threshold black-box secret sharing construction, where secret shares of the client updates, despite belonging to distinct algebraic groups owing to different quantization, are generated from identical linear integer systems.

  匹配依据：MPC: secret sharing

  </details>

- **HELLO, GOODBYE: Concurrent General Composition From Super-Rushing Security**
  2026-10-26 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2651)
  Anirudh Chandramouli

  <details><summary>摘要 / Abstract</summary>

  Kushilevitz, Lindell, and Rabin (STOC `06, SIAM Journal on Computing `10), in their seminal result, showed that any standalone-secure synchronous multiparty computation (MPC) protocol can be compiled into one secure under concurrent general composition, by adding a synchronisation step after every round; thereby, at least doubling the round complexity. We show that for protocols that are secure against super-rushing adversaries, introduced by Asharov, Chandramouli, Cohen, and Ishai (EuroCrypt `25), two synchronisation rounds suffice. Specifically, for an $R$-round protocol that is secure against super-rushing adversaries with a black-box, straight-line simulator, adding a round of start synchronisation (saying ``HELLO&#x27;&#x27;) and a round of end synchronisation (saying ``GOODBYE&#x27;&#x27;) yields security under concurrent general composition with selective abort in $R+2$ rounds. If the end synchronisation is over a broadcast channel, the security is upgraded to unanimous abort. Both compilers incur no loss in the security reduction and preserve the flavour of security (perfect, statistical, or computational) of the underlying synchronous protocol. Moreover, combining with the sufficient conditions of Asharov et al. for perfect security, and the round-preserving super-rushing compilers of Ciampi, Ravi, and Zou (Cryptology ePrint Archive 2026/1745) for statistical and computational security, yields compilers from rushing security to security under concurrent general composition, with an additive overhead of at most $2$ rounds. We further extend our compilers to protocols with a trusted setup, such as a common reference string or a public-key infrastructure, which is necessary in the dishonest majority setting. We require two conditions. First, every execution of the protocol uses its own stateless copy of the setup, whose responses to the adversary do not depend on the interactions of the honest parties. In particular, this rules out setups that are shared across executions, such as a global common reference string or a single public-key infrastructure used by every execution. Second, the underlying protocol is secure against super-rushing adversaries with adaptive inputs, that is, even when the inputs are chosen after interacting with the setup. Under these conditions, the same compilers yield security under concurrent general composition. We also show that adaptive inputs cannot be relaxed to the usual notion of security in the setup-hybrid model. Specifically, we give a protocol that is statistically secure against super-rushing adversaries with guaranteed output delivery under the standard hybrid model, but is insecure under concurrent general composition after adding start and end synchronisation, even with selective abort.

  匹配依据：MPC: multiparty computation

  </details>

- **HNSecW: A Logarithmic-Time MPC Protocol for Approximate Nearest Neighbor Search**
  2026-10-25 · MPC · [arXiv](https://arxiv.org/abs/2610.34248)
  Fahong Zhang, Weijie Jin, Lixu Wang, Ning Luo, Xiao Wang, Wei Dong

  <details><summary>摘要 / Abstract</summary>

  As a core component of modern RAG systems, approximate nearest neighbor (ANN) search has been extensively studied for decades. In practice, deploying ANN often requires symmetric privacy, where the querier&#x27;s query and the database owner&#x27;s data must remain hidden from each other, necessitating a secure multi-party computation (MPC) solution. So far, most MPC-based ANN protocols follow a cluster-based approach: they evaluate distances for the query over a large candidate set and rely on heavyweight primitives such as distributed ORAM to hide access patterns. As a result, each search typically requires $O(\sqrt{N})$ time. We propose HNSecW, a novel MPC protocol for ANN search that achieves the $O(\log N)$ search time for the first time. We first study the single-query setting. Starting from HNSW, the state-of-the-art ANN algorithm, we redesign its control flow and data structures to achieve fully data-independent execution. To further achieve logarithmic search time, we employ offline reshuffling and partial database duplication. Furthermore, we extend our protocol to support multiple sequential queries by introducing a &quot;double visited&quot; caching structure that eliminates redundant cross-query memory accesses, thereby avoiding per-query online shuffling. In addition, we develop a batch-query protocol that exploits higher parallelism to reduce both round complexity and the circuit&#x27;s critical path. Our experiments show that HNSecW preserves the high accuracy of plaintext HNSW ($\geq 90\%$ recall) and delivers over a $20\times$ efficiency improvement over prior work on million-scale datasets.

  匹配依据：MPC: secure multi party computation

  </details>

- **Tritone: Pairwise Garbled Disputes for Multi-Party Proof Verification on Bitcoin**
  2026-10-23 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2612)
  Oleksii Avramenko, Alessandro Baccarini, Torben Poguntke

  <details><summary>摘要 / Abstract</summary>

  Bitcoin Script lacks native pairing operations for efficient direct verification of Groth16 proofs. Conventional federated bridges instead authorize withdrawals through a signing quorum, whose collusion can release funds without valid evidence. We present the Tritone protocol, which lets Bitcoin enforce the outcome of verifying a Groth16 proof for an NP relation fixed in a one-time trusted setup, with the locked funds secure as long as one of a fixed set of $N$ operators is honest. Verification is optimistic and off-chain, and every transaction is standard under current relay policy, so Tritone runs on Bitcoin today without consensus changes. Tritone generalizes the two-party BABE protocol to a fixed committee of $N$ operators, with one dispute instance per ordered pair. Cut-and-choose protects against malicious garblers, while Feldman verifiable secret sharing correlates input keys across candidates. Our new Lamport-adaptor gadget forces a challenging verifier to disclose the shares selected by the prover&#x27;s committed proof element, providing the transaction-level binding left unspecified by BABE. A single set of disclosed shares then unlocks all retained candidates. We formalize the multi-party primitive, prove the protocol secure against up to $N-1$ statically corrupted operators, and specify its complete pre-signed transaction graph. We implement Tritone in Rust. On Bitcoin mainnet, when one verifier disputes a claim at every stage, the prover-candidate posts 9,607 vB and the verifier 18,160 vB of protocol transactions. In local benchmarks at 40-bit statistical security, the prover-candidate of each dispute instance retains as little as 112.83 MiB. Tritone thus replaces trust in a signing quorum with a single-honest-operator assumption wherever locked bitcoin is released to an operator against a Groth16 proof, with Bitcoin bridges as our showcase.

  匹配依据：MPC: secret sharing

  </details>

- **Traceable Quantum Secret Sharing**
  2026-10-23 · MPC · [arXiv](https://arxiv.org/abs/2610.32218)
  Mengyan Qiao, Jian Long, Yu Li, Zhu Cao

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing protects distributed quantum information against unauthorized reconstruction, yet existing schemes provide no intrinsic accountability when shares are leaked or forged. This missing capability is particularly relevant in realistic distributed settings, where compromised participants may either expose valid shares or maliciously interfere with reconstruction. Here we establish a framework for traceable quantum secret sharing under these two threat models. We introduce leakage-verifiable and traceable quantum secret sharing (LVT-QSS), which attributes leaked shares through an explicit leakage verification mechanism, and malicious-traceable and accountable quantum secret sharing (MTA-QSS), which identifies participants who submit forged shares during reconstruction. We formulate security definitions for both settings and prove that the proposed protocols satisfy the corresponding guarantees against the relevant adversaries. Numerical simulations under per-share depolarizing noise further quantify the robustness of the proposed schemes and identify verification as the dominant noise sensitive stage. These results incorporate accountability into quantum secret sharing and provide a foundation for traceable distributed quantum cryptography.

  匹配依据：MPC: secret sharing

  </details>

- **Smaller Share Size for Evolving Secret Sharing: General Thresholds and Threshold Three**
  2026-10-23 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2619)
  Xiaozheng Wang

  <details><summary>摘要 / Abstract</summary>

  Evolving secret sharing allows participants to join indefinitely without modifying previously distributed shares. We study the share size of perfectly secure evolving threshold secret sharing schemes and obtain two improvements. For general thresholds, we introduce a polynomial sharing method that shares two secrets with adjacent reconstruction thresholds using one polynomial. Combining this method with the evolving scheme of Cheng et al.\ (ASIACRYPT 2025), we obtain an evolving $k$-threshold scheme whose $t$-th share has size \[ \left\lfloor \frac{k}{2} \right\rfloor \log_2 t + O_k\!\left(\ell+\log_2\log_2 t\right) \] bits for an $\ell$-bit secret. This reduces the leading coefficient of their general construction from $k-1$ to $\lfloor k/2\rfloor$. For threshold three, we give a separate construction that reduces the lower-order terms of the scheme of Cheng et al. We mask the short shares in all generations with the same random $\ell$-bit value $R$, which is shared through an evolving $2$-threshold scheme, we obtain \[ \log_2 t+(2+o(1))\log_2\log_2 t \] bits per share for fixed $\ell$. Both constructions satisfy correctness and perfect information-theoretic security.

  匹配依据：MPC: secret sharing

  </details>

- **Quantum Secret Sharing from CSS qLDPC Codes: Computable Access Structures, Accessible Logical Dimension, and Topology-Aware Network Cost**
  2026-10-23 · MPC · [arXiv](https://arxiv.org/abs/2610.32428)
  Malik Mouaji, Saif Al-Kuwari

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) schemes can be constructed from quantum error-correcting codes, but characterizing their access structures and implementation costs becomes challenging for finite-length, high-rate quantum low-density parity-check (qLDPC) codes. We develop an exact computational framework for QSS induced by CSS qLDPC codes. The framework characterizes authorized, forbidden, and intermediate coalitions using restricted parity-check matrices and binary linear algebra, and introduces the accessible logical dimension \(κ(A)\), defined through the symplectic rank of locally supported logical classes, to refine the characterization of intermediate coalitions. We further incorporate physical network constraints through separate Tanner-incidence, Steiner-routing, and scheduling-depth costs, and treat the partitioning of physical qubits into participants as an explicit design variable. Numerical experiments on four CSS qLDPC codes verify the predicted complement duality and monotonicity properties and show substantial variation in access transitions and network costs. For the codes studied, the bivariate bicycle instance exhibits the sharpest transition, while network embedding costs vary by more than an order of magnitude across physical topologies. We also show that participant partitioning can substantially improve block-level security and reconstruction thresholds. These results provide a practical bridge between the algebraic structure of CSS qLDPC codes, the graded accessibility of quantum secrets, and the physical constraints of networked QSS implementations.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Federated Loss Exploration for Vision-Based Perception under Non-IID Data**
  2026-10-23 · MPC · [arXiv](https://arxiv.org/abs/2610.32626)
  Nergiz Yuca, Christian Internò, Nikolay Matyunin, Markus Olhofer, Barbara Hammer, Stefan Katzenbeisser

  <details><summary>摘要 / Abstract</summary>

  Vision-based image classification models benefit from Federated Learning (FL) across vehicles, however learning accurate models from distributed vehicular cameras is challenging due to data heterogeneity and privacy concerns. To improve performance on non-IID data, advanced FL optimization approaches have emerged that share auxiliary insights, such as client gradient behaviors. While these gradient-guided optimized FL methods improve the model accuracy, their reliance on sharing additional gradient information introduces a previously unexplored privacy vulnerability. In our empirical privacy-leakage experiment, we show that a malicious server can infer clients&#x27; label sets from shared guidance matrices under heterogeneous client label distributions (simulated via Dirichlet-based label partitions), between 50% and 84% accuracy. To address this privacy leakage, we propose PPFLex that replaces the central server with three Secure Multi-Party Computation (MPC) servers to securely compute the global guidance matrix and perform federated averaging under semi-honest and malicious MPC server assumptions. We evaluate PPFLex on widely used traffic-sign classification datasets (e.g., GTSRB and BTSC) as representative autonomous vehicle perception benchmarks, comparing against baselines. Our results show that PPFLex achieves accuracy comparable to the plain-text FedLEx pipeline while preventing privacy leakage, incurring acceptable MPC overhead.

  匹配依据：MPC: secure multi party computation

  </details>

- **The Entire Quantum Computer on a Classical Leash**
  2026-10-22 · MPC · [arXiv](https://arxiv.org/abs/2610.31775)
  Yael Tauman Kalai, Dakshita Khurana, Justin Raizes

  <details><summary>摘要 / Abstract</summary>

  We show that a classical client with no quantum hardware can use a single untrusted and potentially malicious quantum server as if it were its own trusted quantum computer. Through the server, the client can privately choose and run quantum computations, prepare quantum states, and process quantum states supplied by other parties. It can also keep quantum memory on the server, hidden from the server itself, and use that memory in later computations so its quantum state persists across rounds of interaction. Together, these capabilities let a purely classical party act as a quantum party in a variety of interactive protocols. We expect this virtual quantum computer to be a broadly useful tool. As immediate applications, we resolve two known open problems: (1) classical verification of quantum sampling with negligible computational soundness error, and (2) remote state preparation of arbitrary efficiently preparable quantum states. Underlying all of these results is a general-purpose, maliciously secure two-party computation protocol between a classical client and a quantum server, which we construct assuming only the post-quantum hardness of learning with errors.

  匹配依据：MPC: secure two party computation

  </details>

- **SILMARILS-MV: Information-Theoretically Secure Multi-Verifier Signatures with Dealer-Free Key Issuance and Linear Aggregation for Permissioned Blockchains**
  2026-10-22 · MPC · [arXiv](https://arxiv.org/abs/2610.31814)
  Khadijeh Bagheri, Hassan Khodaiemehr, Chen Feng

  <details><summary>摘要 / Abstract</summary>

  Permissioned blockchains authenticate transactions, votes and quorum certificates with computationally secure signatures, and post-quantum replacements inflate consensus traffic by orders of magnitude. Information-theoretic alternatives have required a trusted authority, quantum channels, per-signature interaction, or single-use keys with bounded transfer. We present SILMARILS-MV, a multi-verifier unconditionally secure signature in which a signature is the vector $α= A\,e(m)$ and each verifier holds a secret functional $c_i = Γ^T λ(x_i)$ derived from virtual anchors $Γ$ that nobody learns. Against unbounded adversaries corrupting up to $ω$ verifiers and any signers, and observing every decision, an honest verifier accepts a forged or invalid signature with probability at most $Q/q + 1/(q-1)$, a bound that is tight in its leading term. The scheme is strongly unforgeable, non-repudiable, transferable across unboundedly many hops, and linearly aggregatable. Keys are issued by the validators through perfectly secure MPC for $t &lt; n/3$, without broadcast. To scale, we let the committee itself sign: in threshold notarization, finality certificates have constant size $32(ω+1)$ bytes and per-validator issuance cost no longer depends on $n$. Arbiter-verified keys give clients 32-byte signatures, robust redistribution supports membership changes and share refresh, and verifiers can be enrolled retroactively. A certificate verifies in 2.4 microseconds. In an analytic normal-case model at 1000 validators, threshold notarization needs 71 KiB of authentication traffic per validator per block, 22x less than ML-DSA-44 for admitted verifiers. In a Rust HotStuff prototype with 100 validators, SILMARILS-MV commits 2.8x more transactions per second than ML-DSA-44 with 67x less cryptographic CPU, and Monte-Carlo attacks match the bounds.

  匹配依据：MPC: mpc (context)

  </details>

- **Integer Coordinate Families and Threshold RSA Signatures for Any Prime Exponent**
  2026-10-22 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2601)
  Shivansh Jaiswal, Somitra Sanadhya

  <details><summary>摘要 / Abstract</summary>

  At CT-RSA 2026, Ng and Lau introduced $(t,n)$-integer coordinate families for threshold RSA signatures with $e=3$, and found some families by heuristic search for $2\le t \le n \le 9$. They asked whether such families always exist and, if so, can they be constructed efficiently. We answer both of these questions positively. We prove that a $(t,n)$-integer coordinate family is also a $(t+1,n)$-integer coordinate family. We construct such families for $t=2$, and $2\le n &lt; 19$, using a polynomial time algorithm in $n$ and its output bit length. Answering another question raised in the Ng-Lau work, we prove super-polynomial lower bounds on coordinates of pairwise families. We also find the minimum families for $n \le 9$. Ng and Lau proposed a threshold signature scheme based on integer coordinate families. We show that the Ng-Lau scheme admits trivial forgeries, and has a flawed proof. We give a repaired scheme $\mathrm{PiIC}$ which does not suffer from these issues. Finally, we propose an integer secret-sharing scheme $\mathrm{PiZ}$ that works for every prime $e$ and every $(t,n)$, without relying on any special coordinate family. We prove that both the schemes $\mathrm{PiIC}$ and $\mathrm{PiZ}$ are TS-UF-CMA secure under the standard RSA assumption.

  匹配依据：MPC: secret sharing

  </details>

- **Efficient Laconic Oblivious Transfer with Malicious Security**
  2026-10-22 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2593)
  Yijian Zhang, Zuoxia Yu, Rupeng Yang, Willy Susilo

  <details><summary>摘要 / Abstract</summary>

  Laconic Oblivious Transfer (OT) enables a receiver to compress a large database into a short digest, allowing a sender to generate a succinct ciphertext that reveals only a single indexed message. While prior works achieve efficient constructions in the semi-honest model, known solutions for malicious security rely on inherently heavy non-black-box techniques, such as garbled circuits or succinct arguments, resulting in impractical schemes. In this work, we present the first construction of maliciously secure laconic OT that makes fully black-box use of its underlying primitives. Our construction is based on a simple and widely used paradigm combining vector commitments with witness encryption, previously known to yield efficient semi-honest protocols. We show that this approach can in fact achieve malicious security by introducing two minimal yet powerful enhancements: equivocal vector commitments and maliciously secure witness encryption. We prove that these properties suffice to obtain laconic OT with security against malicious senders in the universal composability model and against malicious receivers in the context model. We instantiate our framework from standard assumptions, including LWE and bilinear Diffie-Hellman variants, obtaining schemes in the standard model. Notably, our constructions avoid heavy non-black-box tools mentioned before, and therefore achieve efficiency comparable to the state-of-the-art black-box constructions with merely semi-honest security. In particular, in certain settings, we obtain malicious security at essentially no additional asymptotic cost. Our results resolve a central question on the feasibility of practical, maliciously secure laconic OT, and provide a unifying pathway for efficiently achieving malicious security in laconic cryptography.

  匹配依据：MPC: garbled circuits, oblivious transfer

  </details>

- **Semantic-Aware Update Admission and Adaptive Byzantine Redundancy for Secure Computation Offloading in COIN-Enabled Metaverse Systems**
  2026-10-21 · MPC · [arXiv](https://arxiv.org/abs/2610.29592)
  Ibrahim Aliyu, Jaehyung Park, Jinsul Kim

  <details><summary>摘要 / Abstract</summary>

  Computing in the network (COIN) supports latency-sensitive Metaverse services, but blockchain commitment of persistent shared-state updates competes with application execution for limited resources. We consider the joint problem of deciding which updates to commit, how much Byzantine redundancy to provision, and where to execute Metaverse application tasks. We formulate this problem under resource, latency, and practical Byzantine fault tolerance (PBFT) constraints, accounting for update persistence and semantic significance. We develop a hierarchical redundancy-aware PBFT (R-PBFT) approach that decomposes the decision process into slot-wise computation offloading and sequential update-admission and redundancy control. We formulate the former as an identical-interest game and address the latter using a feasibility-filtered double deep Q-network (DDQN). Analytical downlink allocation accounts for the energy and delivery-feasibility effects of consensus latency. For fixed slot state and redundancy, we establish the game&#x27;s exact-potential property and finite termination of strict sequential improvements. Feasible-action filtering enforces configured Byzantine redundancy and blockchain-budget constraints independently of learning. Numerical results show relative improvements of up to $46.7\%$ in reward averaged across tested user loads and seeds over Minimum Secure, the strongest baseline on average. At the highest tested Byzantine bound, the secure timely-update ratio improves by $62.3\%$ over the same baseline. Ablations assess the contributions of feasibility filtering and adaptive deferral.

  匹配依据：MPC: secure computation

  </details>

- **Rerandomizable Garbling for Arithmetic Circuits**
  2026-10-21 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2590)
  Anasuya Acharya, Pierre Meyer, Claudio Orlandi, Lawrence Roy

  <details><summary>摘要 / Abstract</summary>

  Rerandomizable garbling is a powerful extension of Yao’s garbled circuits that allows a garbled circuit to be refreshed without changing its functionality, while preserving privacy as long as at least one rerandomization step is honest. Existing constructions, however, are limited to Boolean circuits and incur significant communication overhead. In this work, we initiate the study of rerandomizable garbling for arithmetic circuits. We present the first rerandomizable arithmetic garbling scheme, based on techniques inspired by recent advances in garbling from homomorphic secret sharing. Our construction departs fundamentally from previous approaches and achieves communication complexity $O(|\mathbf{C}|\log B)$ for circuits $\mathbf{C}$ with $B$-bounded computation. Concretely, our scheme requires 17 group elements per multiplication gate, while addition gates are free. Our scheme can be instantiated under standard subgroup-indistinguishability assumptions, including the Decisional Composite Residuosity (DCR) assumption and assumptions over class groups.

  匹配依据：MPC: garbled circuit, garbled circuits, garbling scheme, secret sharing

  </details>

- **Regular Syndrome Decoding Is Easier Than Previously Estimated**
  2026-10-21 · MPC · [arXiv](https://arxiv.org/abs/2610.29175) · [IACR ePrint](https://eprint.iacr.org/2026/2563)
  Jiseung Kim, Minkyu Kim, Changmin Lee, Hochang Lee

  <details><summary>摘要 / Abstract</summary>

  The Regular Syndrome Decoding (RSD) problem is a structured variant of classical Syndrome Decoding and underlies a growing number of efficient cryptographic constructions, including zero knowledge protocols, pseudorandom correlation generators, and MPC in the Head signatures. Although RSD is generally believed to be computationally hard, recent works have shown that algebraic attacks can outperform information set decoding on important RSD parameter regimes. Building on this line of work, we revisit the concrete hardness of RSD and show that many widely used parameter sets are substantially easier to solve than previously estimated. This improvement stems from a refined hybrid algebraic attack that exposes and removes a previously overlooked source of concrete complexity: the joint blockwise placement of zero coordinate guesses and syndrome based variable eliminations. Rather than treating the two guessing stages and linear elimination as largely separate choices, our method coordinates them across all regular blocks so that the guessing penalty is balanced while sufficient equations are retained for linearization. This gives a systematic block balancing principle for the entire guess reduce solve pipeline. We reassess several RSD based applications, including Ferret, Wolverine, and committed VOLE. Our estimates place at least one parameter set per application below its 128 bit target, with losses approaching 67 bits. On PCG benchmarks, we improve previous best attack costs by up to 29.77 and 25.91 bits over non binary and binary fields, respectively. Moreover, for the revised 128 bit PCG parameter sets of Liu et al. evaluated here, estimated attack costs are all below $2^{111}$ field operations. These results substantially revise the concrete security landscape of RSD and indicate that several existing parameter choices overestimate the hardness of their underlying RSD instances.

  匹配依据：MPC: mpc (context)

  </details>

- **GhostFaceMPC: Privacy-Preserving Face Recognition with Multi-Party Computation**
  2026-10-21 · MPC · [arXiv](https://arxiv.org/abs/2610.29987) · [IACR ePrint](https://eprint.iacr.org/2026/2499) · [Code](https://github.com/crypto-unict/GhostFaceMPC)
  Davide Carnemolla, Dario Catalano, Mario Di Raimondo

  <details><summary>摘要 / Abstract</summary>

  Facial recognition has become central to modern authentication systems, security frameworks, and personalized services. However, its widespread adoption is hindered by severe privacy risks, particularly surrounding unauthorized access to sensitive biometric data. To address these challenges, this paper presents GhostFaceMPC, the first end-to-end, privacy-preserving face recognition system to evaluate a deep convolutional neural network extractor and matching under secure multi-party computation. GhostFaceMPC enables secure processing of facial data across all stages of a face recognition process, from feature extraction and storage to matching, without exposing raw images or biometric embeddings at any stage. We introduce a multi-party computation-friendly quantization of the GhostFaceNet model and circuit optimizations that make face recognition under multi-party computation practical. The code is available at https://github.com/crypto-unict/GhostFaceMPC.

  匹配依据：MPC: multi party computation, secure multi party computation

  </details>

- **Eras MPC: Granular Preprocessing and Abort Recovery with Dynamic Committees**
  2026-10-21 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2588)
  Ivan Damgard, Bernardo David, Rahul Satish

  <details><summary>摘要 / Abstract</summary>

  MPC with dynamic committees achieves scalability by having small committees execute each round of the computation, instead of involving all parties in the entire execution. However, achieving Guaranteed Output Delivery in efficient information theoretical protocols requires larger honest majority committees, limiting scalability. Moreover, using preprocessed correlated randomness to speed up the computation is prohibitively expensive due to the cost of transferring such randomness to parties that have not yet joined the execution. We propose Eras MPC, a model where small dishonest majority computation committees execute one or more rounds of the computation with the help of honest majority preprocessing and checkpointing committees. The computation is carried out in &quot;Eras&quot;, which are sets of shorter epochs. In the beginning of each Era&#x27;s first epoch, a preprocessing committee generates correlated randomness for the computation epochs to be executed by different computation committees. In the end of an Era, checkpoint committees verify the current state of the computation, save this state if it is valid and provide the latest valid state to the next Era. We show an Eras MPC protocol where the preprocessing is carried out using an honest majority MPC protocol to generate authenticated Beaver triples, requiring only enough rounds of interaction to perform two subsequent batches of multiplications. The computation is done via the SPDZ online phase executed in each epoch by a small dishonest majority committee. Finally, intermediate state is checkpointed by verifying the validity of wire shares and saving wire values in $4$ rounds, each executed by a different honest majority checkpoint committee.

  匹配依据：MPC: mpc (context)

  </details>

- **Privacy-Preserving Robustness-Guided Testing**
  2026-10-20 · MPC · [arXiv](https://arxiv.org/abs/2610.27441)
  Charles Koll, Houssam Abbas, Mike Rosulek

  <details><summary>摘要 / Abstract</summary>

  In industries like semi-conductors and aerospace, it is common for the design company to contract out part of the testing process to a Testing-as-a-Service (TaaS) company. In such a setup, both parties want to keep their intellectual property private (i.e. unknown to the other party): namely the design and its output traces for the designer, and the detailed correctness specifications for the tester. We demonstrate a practical way for conducting provably private TaaS using a cryptographically secure multi-party computation protocol. We do so for the common setup where the specification is in Signal Temporal Logic, and testing is done using robustness-guided falsification. Our implementation carefully separates the steps of falsification, and manages to be $\textit{maximally secure}$, in the sense that the parties learn the absolutely minimum necessary for falsification. For up to a 100-dimensional input search space, the generation of one test takes less than 80 msec, and the overhead of the privacy-preserving protocol is less than 6x. These numbers mean that privacy-preserving TaaS is practical, thus enabling TaaS in security-sensitive industries.

  匹配依据：MPC: secure multi party computation

  </details>

- **Interflow: Breaking the Offline-Online Barrier for Private AI at the Edge**
  2026-10-20 · MPC · [arXiv](https://arxiv.org/abs/2610.27431)
  Hanieh Totonchi Asl, Ebrahim Nouri, Zhuoran Li, Danella Zhao

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving machine learning (PPML) offers a promising path toward bringing powerful AI services to the edge without exposing sensitive user data. However, its practical deployment remains constrained by the high communication, computation, and data-movement costs of secure multi-party computation (MPC), particularly during nonlinear inference. Existing MPC systems typically decouple input-independent correlated randomness generation from online execution, creating substantial memory pressure to buffer single-use cryptographic data. Moreover, limited storage can force a stop-and-refill execution pattern that repeatedly stalls the pipeline to replenish these buffers, bringing randomness generation back onto the critical path. We propose Interflow, an algorithm-hardware co-design that rethinks this separation by batch-wise processing and pipelining correlated-randomness generation with online execution: while the current batch consumes pre-generated randomness to execute secure nonlinear operations, correlation generation proceeds concurrently for the next batch. By leveraging interleaved execution, efficient data movement, and hardware acceleration, the design transforms preprocessing from a serialized, storage-intensive offline phase into a continuously overlapped pipeline that generates correlated randomness closer to the point of consumption, reducing memory footprint and data movement overhead. Implemented on the Zynq UltraScale+ ZCU102, Interflow improves nonlinear evaluation throughput by up to 1.55x for CNN operators and 1.48x for transformer operators. It achieves up to 1.26x speedup for ResNet-50 and up to 1.21x speedup for BERT-base, and reduces memory footprint by up to 37%, compared with baseline frameworks.

  匹配依据：MPC: secure multi party computation

  </details>

- **Big Secrets Small Shares: Revisiting Secure Multi-Party Computation**
  2026-10-20 · MPC · [arXiv](https://arxiv.org/abs/2610.27609)
  Wilton Kim, Van Long Phuoc Pham, Stanislav Kruglik, Han Mao Kiah

  <details><summary>摘要 / Abstract</summary>

  At CRYPTO 2007, Damgård and Nielsen introduced a preprocessing approach to multi-party computation (MPC) to achieve linear communication complexity. Another approach to reduce communication complexity was proposed by Cramer, Damgård, and de Haan at EUROCRYPT 2007, which involved using ramp-secret sharing schemes to jointly share base-field components of secrets from the extension field. In this paper, we combine these two ideas to achieve a non-asymptotic reduction of communication cost in a multi-phase MPC setup. We introduce a new modification of the ramp secret sharing scheme, called compact sharing, and tailor the MPC protocol to accommodate this modification. Compact sharing masks the polynomial coefficients that would otherwise leak during degree reduction. The protocol provides perfect security against static semi-honest adversaries under an explicit tradeoff between the corruption threshold and the extension degree. When the extension degree scales linearly with the number of parties, the gate-evaluation core achieves constant communication overhead relative to an extension-field element, amortized over full preprocessing batches; input and output communication is counted separately.

  匹配依据：MPC: multi party computation, secret sharing, secure multi party computation

  </details>

- **A Spectral Theory of Local-to-Global Leakage**
  2026-10-20 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2571)
  Rei Ueno

  <details><summary>摘要 / Abstract</summary>

  This paper studies how local leakages characterize the global leakage in additive secret sharing over a finite abelian group, which is a special case of linear secret sharing and side-channel masking. Our main finding is structural: local-to-global leakage is governed by two disjoint components---the magnitude of local leakage and its spectral alignment across shares, while existing literature attempted to characterize the global leakage only by local mutual information (MI). We first give an exact decomposition of leakage in additive secret sharing. The decomposition reveals a structural parameter invisible to MI, while previous literature conjectured that the local MI alone suffices to characterize global leakage. We then show that this missing parameter is indispensable: two leakage channels with identical local MI can induce exponentially different global leakage. Our exact decomposition identifies the missing structural quantity and completely characterizes this phenomenon. We then show the separation theorem with its realizability---local MI, despite governing the classical leakage bounds, does not even determine the exponential rate at which leakage vanishes under homomorphic composition. More strongly, we establish a universal separation theorem: even when all permutation-invariant scalar measures of local leakage agree, the global leakage can exhibit exponentially different decay rates. We further provide the characterization of the spectral alignment factor and derive its lower bound through character-order multiplicity and Möbius inversion. We then extend the framework to automorphism-weighted sharing. We establish that automorphism-weighted sharing can achieve perfect leakage cancellation with finitely many shares, even for non-trivial full-support local leakage channels. In sharp contrast, such perfect cancellation is impossible for ordinary additive sharing with non-trivial i.i.d local leakage channels and finitely many shares. Consequently, local leakage magnitudes correctly measure the average amount of local leakage, but discard the compatibility structure needed for composition. Magnitude-only bounds must optimize over structural alignments that the actual leakage channel does not realize.

  匹配依据：MPC: secret sharing

  </details>

- **PPGA: A Framework for Privacy-Preserving Graph Algorithms using the Prepare/Propagate/Gather/Apply Paradigm**
  2026-10-19 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2550)
  Andreas Brüggemann, Simon Brunnauer, Thomas Schneider

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving graph computation enables the secure analysis of graphs modeling social interactions and networks, financial transactions, etc., while keeping the graph private. One approach is to use secure multiparty computation (MPC), allowing different clients to contribute parts of a graph without need of disclosure, and multiple MPC protocols have been proposed for running message-passing-based graph analysis. Yet, existing public implementations are prototypes for fixed analysis functions that require substantial MPC expertise to modify and extend. We present PPGA, a practical framework based on the MultiCent protocol (PETS&#x27;25). PPGA lets users define their custom message-passing graph algorithms with a high-level interface, clients input parts of the graph, and then runs the algorithm in MPC. It significantly improves performance compared to MultiCent&#x27;s implementation, running BFS on a graph of size |V|+|E|=30 million in 23 minutes without leaking the graph topology.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Off-Key: Inconsistent MAC Keys Compromise Privacy in SPDZ-Family MPC**
  2026-10-19 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2533)
  Marcel Keller, Sela Navot, Nirvan Tyagi

  <details><summary>摘要 / Abstract</summary>

  SPDZ-family protocols for maliciously secure multi-party computation protect secret-shared values with message authentication codes (MACs) under a secret-shared global key. Their security requires that all values and preprocessing used together be authenticated under the same key. We present Off-Key, a privacy attack that exploits violations of this requirement. Depending on which specific MAC check protocol is used, a corrupted party can either recover the value of a shared secret from a single authentication check or test a guess through selective failure by modifying a MAC share and observing whether a masked check succeeds. While this attack does not compromise the theoretical security guarantees of the protocols, we demonstrate this key-consistency vulnerability in evaluated versions of MP-SPDZ, SCALE-MAMBA, and FANNG-MPC, which allow a corrupted party to use different keys across batches, threads, or process runs. To help implementations avoid this class of attacks, we identify the state that enforces key consistency in representative preprocessing protocols and show how preserving and reusing it prevents the attack.

  匹配依据：MPC: secure multi party computation

  </details>

- **Enjoy FAEST on Hardware: Efficient and Novel Hardware Acceleration of Emerging Post-Quantum Digital Signature Scheme FAEST**
  2026-10-18 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2525)
  Brendan Funk, Jiafeng Xie

  <details><summary>摘要 / Abstract</summary>

  The National Institute of Standards and Technology (NIST) Post-Quantum Cryptography (PQC) standardization process has drawn significant attention from the research community recently, especially regarding these PQC schemes&#x27; hardware acceleration. Nevertheless, related research on the emerging schemes, e.g., those currently under consideration by the NIST additional digital signature scheme standardization, still needs further exploration. With this background, this paper presents an efficient and novel hardware acceleration for FAEST, one of the promising signatures in the NIST Round 3 additional scheme competition. Overall, we have presented several layers of innovative efforts to obtain the proposed acceleration. First of all, we have conducted detailed algorithmic analysis on the major computationally intensive operations within FAEST and proposed novel design strategies and algorithms for their efficient hardware implementation. Next, we have proposed novel design efforts to construct these major operations into efficient building blocks to finalize the overall accelerator, along with the help of optimized operational phase workflow. The dedicated extension to build the L1-EM-fast accelerator is also given. Finally, we have provided a detailed and thorough evaluation process to showcase the superior performance of the proposed design over the existing complete, Sign part, and single security level MPC-in-the-head signature acceleration works. For instance, at the same security level, the proposed fast variant has at least 98\% less equivalent Area-Delay Product (eADP) than the recent complete SDitH design. To the authors&#x27; best knowledge, this is the first hardware acceleration work for FAEST, and we hope the outcome of this research will facilitate the ongoing PQC standardization process.

  匹配依据：MPC: mpc (context)

  </details>

- **QuarkShard: Decomposing Cross-Shard Requests into Single-Input Transactions**
  2026-10-16 · MPC · [arXiv](https://arxiv.org/abs/2610.23014)
  Changyu Duan, Zhixuan Fang

  <details><summary>摘要 / Abstract</summary>

  Sharding blockchains enhance scalability by distributing the workload across multiple shards. Within sharding blockchains, securely and efficiently processing cross-shard user requests remains a pivotal challenge. Traditional sharding blockchain protocols execute cross-shard requests under a processing paradigm that treats each user request as a monolithic entity to preserve its atomicity, inherently introducing significant intra-shard BFT execution overhead and cross-shard communication overhead. We propose QuarkShard, a sharding protocol that breaks away from this traditional paradigm to achieve intra-shard and cross-shard overheads below the lower bounds imposed by conventional approaches. QuarkShard decomposes cross-shard requests into single-input-shard transactions, where each transaction requires consensus and processing within only a single shard, thereby substantially reducing total request processing overhead. Meanwhile, through a carefully designed request decomposition algorithm, QuarkShard guarantees fund atomicity or location atomicity during request execution. QuarkShard also enhances the security of blockchain sharding systems against MEV attacks and flooding attacks. Empirical evaluation across a wide-area network spanning four AWS regions demonstrates that QuarkShard achieves superior performance, attaining a peak throughput of $1024$k requests per second with sub-$4$-second latency. Benchmark comparisons show that QuarkShard achieves up to $210.7\%$ and $314.8\%$ of the maximum throughputs of Kronos and 2PC, respectively.

  匹配依据：MPC: 2pc (context)

  </details>

- **Structural Cryptanalysis of the Eevee AEAD Family**
  2026-10-15 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2496)
  Shuping Mao, Peng Wang, Jiadong Han, Tingting Guo, Yan Jia, Ying Chen

  <details><summary>摘要 / Abstract</summary>

  Eevee is a family of three AEAD modes, Umbreon, Jolteon, and Espeon, proposed at CCS 2023 for IoT-to-cloud secure computation. We analyze structural flaws in the algorithms of the supplied full-version specification and the proof steps underlying their online authenticated-encryption claims. An AD-free, two-encryption prefix distinguisher has advantage $1-2^{-n}$ in the ideal-forkcipher model, contradicting the specified online ideal object. Independently, the separable associated-data transform yields a four-encryption nonce-misuse distinguisher with advantage $1-2^{-n}$, a deterministic AD-only forgery, and nonempty-message forgeries obtained from cross-domain state differences. These attacks contradict the advertised nonce-misuse bounds of Umbreon and Espeon. With nonce-respecting encryption queries, one two-block Jolteon encryption permits a fresh one-block forgery with the same tag, while Espeon&#x27;s short-message path permits arbitrary AD substitution. We trace these counterexamples to failures of online-prefix consistency, conditional transcript distributions, domain separation, and checksum freshness in the original proof. The authenticity attacks follow from deterministic identities, and the privacy counterexamples persist with an ideal forkcipher. We derive corresponding requirements for AD processing and message finalization, and briefly summarize supporting checks of the published C routines. The central failures concern the mode design and cannot be resolved solely by correcting implementation encodings.

  匹配依据：MPC: secure computation

  </details>

- **SMT-Boosted Security Types and Correctness for Low-Level MPC**
  2026-10-15 · MPC · [arXiv](https://arxiv.org/abs/2610.22047)
  Christian Skalka, Steven Baldasty, Yeonhee Yeh, Felix Walberg, Joseph P. Near

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation (MPC) is an important enabling technology for data privacy in modern distributed applications. We develop a new Hoare logic and type theory to automatically enforce correctness, confidentiality, and integrity properties of protocols written in the Prelude/Overture language framework. Both definition and automation of our analyses leverages SMT verification, supporting precision and efficiency. Our approach is compositional, scalable, and generalizes to arbitrary prime fields and secret sharing schemes.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Robust ECDSA Threshold Signing at Scale**
  2026-10-15 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2493)
  Carsten Baum, Anders Dalskov

  <details><summary>摘要 / Abstract</summary>

  This work presents an efficient, scalable, and robust threshold ECDSA signing protocol for the $t\leq (n-1)/3$ scenario, making it suitable for e.g., bridging consensus from one Blockchain to another. Our construction allows to batch-compute pre-processing material for efficient online signing. While our protocol is based on established ideas for (Verifiable) Secret Sharing, we optimize it to scale efficiently both in terms of computation and communication with a large number of signers. We therefore combine efficient batching techniques for sharing (Fitzi &amp; Hirt, PODC 2006), randomness extraction (Beerliova-Trubiniova &amp; Hirt, TCC 2008) and share opening (Damgård &amp; Nielsen, CRYPTO 2007) with recent advances in efficient Zero-Knowledge proofs (Attema &amp; Cramer, CRYPTO 2020). We implement and evaluate the protocol experimentally and show that it is practical for large number of parties $n$.

  匹配依据：MPC: secret sharing

  </details>

- **On the Complexity of Symmetric Boolean Functions in Multiparty Private Simultaneous Messages**
  2026-10-15 · MPC · [arXiv](https://arxiv.org/abs/2610.21216)
  Marshall Ball, Peter Crawford-Kahrl, Vladimir Podolskii, Morgan Prior

  <details><summary>摘要 / Abstract</summary>

  Multiparty Private Simultaneous Messages (PSM), also known as Decomposable Randomized Encoding (DRE) or information-theoretic garbling, is a model for non-interactive secure computation. Each party encodes its input using shared randomness and sends a message to an evaluator who does not know that randomness. The evaluator must recover the function output without learning anything else about the inputs. Perfect privacy requires identical transcript distributions on inputs with the same output. We also study the weaker notion of support privacy, which requires only that these distributions have the same support. We study the communication complexity of symmetric Boolean functions when each of the $n$ parties holds one input bit. Lower bounds. We prove a superlinear lower bound for support-private PSM protocols computing $OR_n$. Our technique gives $Ω(n\log n)$ lower bounds for $MAJ_n$ and $EMAJ_n$ (with even $n$), and an $Ω(n\log q)$ lower bound for $MOD_q$ when $q\leq(1-c)n$ for a fixed constant $c&gt;0$. Upper bounds. We construct perfectly private PSM protocols of total communication $\widetilde{O}(n^{3/2})$ for every symmetric Boolean function, improving on the known quadratic bound. For $MAJ_n$, known branching-program constructions yield an upper bound of $O(n\log^3 n\log\log n)$. For $EMAJ_n$ and $MOD_q$ with prime $q$, the lower bounds are tight up to constant factors in the stated regimes. Under support privacy, we obtain $\widetilde{O}(n)$ communication for every symmetric Boolean function. Earlier lower-bound techniques of Ball et al. (ITCS 2020) yield only trivial linear bounds for symmetric Boolean functions. Concurrent and independent work by Holmgren and Wu proves a $ω(n)$ lower bound for $OR_n$ using the same combinatorial core. Both works used AI assistance.

  匹配依据：MPC: secure computation

  </details>

- **NOMAI: Scalable Federated Learning with Private Weights**
  2026-10-15 · MPC · [arXiv](https://arxiv.org/abs/2610.21059)
  Yiyi Sun, Mushtari Sadia, Amrita Roy Chowdhury

  <details><summary>摘要 / Abstract</summary>

  The twin goals of privacy-preserving federated learning (FL) -- harnessing distributed data while protecting the parties who contribute it -- demands three properties: model privacy, data privacy, and integrity. Achieving all three in a realistic deployment -- with a single coordinator and millions of users -- remains an open challenge that prior work has yet to fully resolve. We present NOMAI, the first scalable MPC-based FL system to provide all three guarantees simultaneously. NOMAI operates under an honest-majority assumption in the semi-honest model, with an extension to the malicious-with-abort setting. At its core, NOMAI combines a multi-committee MPC architecture with packed Shamir secret sharing, enabling SIMD-style secure computation that scales far beyond what monolithic n-party protocols can support. We further introduce ML-aware optimizations and new cryptographic primitives that substantially reduce per-user overhead. Our evaluation shows NOMAI is practically deployable at unprecedented scale: it reduces per-user computation to just &lt;350 ms (semi-honest) and &lt;700 ms (malicious) for per iteration of training MNIST, achieving three orders-of-magnitude improvements over prior work while seamlessly supporting populations of over 106 users. This demonstrates, for the first time, that MPC-based FL can meet the scale demands of real-world systems without compromising on privacy or integrity.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Coefficient choice in Galois-ring lifts of APN permutations: sharp unit-direction spectra and one-term optimal lifts**
  2026-10-15 · MPC · [arXiv](https://arxiv.org/abs/2610.21178)
  Hiroki Fukui

  <details><summary>摘要 / Abstract</summary>

  Permutation polynomials over the Galois ring $\mathrm{GR}(2^k,m)$ are nonlinear components for symmetric primitives that add keys in the ring, as in secure computation modulo $2^k$. Rønjom and Sandrib showed that their differential uniformity is at least $2q^{k-1}$, where $q=2^m$. For the class studied here it is attained on top-layer differences, while almost all differences are units. We ask how small the difference table can be on unit differences when the residue permutation is fixed and only higher coefficient digits of its lift are chosen. Let $m\ge5$ be odd, $k\ge3$, and let $p$ be a reduced quadratic almost perfect nonlinear (APN) permutation of $\mathbb{F}_q$ whose derivative is nowhere zero and two-to-one. Over all lifts of $p$, the least possible maximum on unit differences is $q$ or $2q$, decided by two invariants of $p$ and the level $k$. We describe every lift attaining it and show that the coefficients modulo $8$ decide optimality at every level. For every odd $m\ge5$, residue permutations with at most $16$ monomials attain $q$ after one $2$-adic digit of one coefficient of the natural lift is changed. For an explicit infinite family, one added monomial lowers the maximum on unit differences from $4q$, or from at least $q^2$, to $2q$ at every level without raising the degree. Under a uniform starting state and independent uniform round keys, valuation preservation yields layerwise bounds for characteristics and two-round differentials that distinguish lifts with the same global uniformity. Core results are formalized in Lean 4.

  匹配依据：MPC: secure computation

  </details>

- **Secret Sharing from Non-Extractable Randomness**
  2026-10-14 · MPC · [arXiv](https://arxiv.org/abs/2610.20173) · [IACR ePrint](https://eprint.iacr.org/2026/2477)
  Divesh Aggarwal

  <details><summary>摘要 / Abstract</summary>

  Bosley and Dodis (TCC 2007) proved that a class of imperfect randomness sources that suffices for information-theoretic encryption of messages longer than the logarithm of the key length must admit deterministic extraction of nearly uniform bits, and asked whether the same is true of two-out-of-two secret sharing. Aggarwal, Chung, Obremski, and Ribeiro (TCC 2022) gave a positive answer for schemes that are in addition leakage-resilient or non-malleable; the original question remained open. We answer it in the negative. For every $b\ge2$ we construct a class of flat sources on $\{0,1\}^{b+2}$, each of min-entropy at least $b$, together with a perfectly correct and perfectly private two-out-of-two scheme that shares a $b$-bit secret into two $(b+1)$-bit shares using any source in the class, and we show that every deterministic map from $\{0,1\}^{b+2}$ to $\{0,1\}$ is at statistical distance at least $1/6$ from uniform on some source in the class. This implies that sharing a long enough secret does not require extractable randomness. The proof is a short parity argument. The idea of the construction extends to other thresholds: for two-out-of-$n$ and $r$-out-of-$r$ sharing we give perfect schemes with $(b+1)$-bit shares, private for classes of flat sources from which no single bit can be extracted with error below $1/(4n-2)$ and $1/(2(2^r-1))$, respectively.

  匹配依据：MPC: secret sharing

  </details>

- **Heterogeneous CPU–NPU Implementation of the AIMer Post-Quantum Signature for Low Latency on a Mobile SoC**
  2026-10-14 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2486)
  Myoungsu Shin, Jihoon Jang, Hanbeom Shin, Insung Kim, Dongjae Lee, Donggeun Kwon

  <details><summary>摘要 / Abstract</summary>

  Signatures in the MPC-in-the-head paradigm rest only on a symmetric primitive, but their signing is slow, because it computes hash functions and a linear map for every simulated party of every repetition. We show that the Hexagon NPU of Snapdragon SoCs shortens one complete signing operation of AIMer, the MPC-in- the-head signature that the Korean post-quantum cryptography competition selected. Prior work speeds up such signatures on one CPU core, accelerates post-quantum arithmetic on GPUs for batches of operations, and reports only single post-quantum functions for mobile NPUs. Our implementation divides each signing operation along its dependency graph. The NPU computes the hashing and the per-party linear map of the last repetitions, which need no secret key, and the CPU keeps the secret key and the two hashes that absorb the repetitions in index order. A fast AArch64 implementation serves both as the CPU part and as the baseline, and it signs 4.5 to 6.1 times faster than the reference implementation on one core. On a Snapdragon 8 Gen 3 tablet, one core with the NPU signs 1.30 to 1.42 times faster than two cores and 1.74 to 1.97 times faster than one core for the three short-signature parameter sets. The same configuration uses 13 to 27 % less energy per signing operation than two cores. On Snapdragon 8 Elite and 8 Gen 2 phones, one core with the NPU signs 1.28 to 1.35 and 1.74 to 1.82 times faster than two cores.

  匹配依据：MPC: mpc (context)

  </details>

- **Edabits Generation with Quasi-Linear Communication Complexity**
  2026-10-14 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2482)
  Alexander Bienstock, Daniel Escudero, Qijia Fan, Fengrun Liu, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  The work of (Escudero et al., CRYPTO 2020) introduces the so-called edabits, which are defined as a secret sharing of an integer over an arithmetic domain, together with its bit decomposition secret shared over a binary domain. In the same work, it is shown how edabits can be used to securely evaluate advanced primitives such as comparison, bit decomposition, and truncation, which are essential building blocks in more complex applications such as privacy-preserving machine learning and beyond. Edabits are general and can be defined over any secret-sharing scheme or corruption model. Such flexibility, coupled with their wide range of applications, makes edabits a powerful target correlation. Escudero et al.~introduced a protocol to generate edabits that works in the arithmetic black-box (ABB) model, that is, it is agnostic to the concrete secret-sharing scheme and even works both for fields $\mathbb{F}_p$ and rings $\mathbb{Z}_{2^\ell}$, as well as both for honest majority $t 0$. This includes the honest majority case $t&lt;n/2$, but also dishonest majority with an (arbitrarily small) constant fraction of honest parties. Our result is achieved via novel applications of randomness extraction methods, as well as better edabit aggregation for the binary components. Along the way and of independent interest, we improve the communication complexity of dabit generation (dabits are bits shared in both binary and arithmetic domains) from $\Omega(n^2\ell)$ bits achieved in (Rotaru and Wood, INDOCRYPT 2019), to linear $O(n\ell)$ bits.

  匹配依据：MPC: secret sharing

  </details>

- **On Secure Sorting and Its Application to Privacy-Preserving Graph Pattern Matching**
  2026-10-13 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2457)
  Marcel Keller

  <details><summary>摘要 / Abstract</summary>

  Sorting in secure computation has been studied almost as long as there have been implementations of multi-party computation (Wang et al., AsiaCCS&#x27;10). More recent advances include completely secure implementations (revealing nothing other than the list size) that have used Quicksort (Araki et al., CCS&#x27;21) and radix sort (Asharov et al., CCS&#x27;22). For the first time, we extensively compare the two variants across a range of parameters and for both honest- and dishonest-majority computation. We then apply secure sorting to improve sparse matrix multiplication without oblivious RAM based on recent work by Damie et al. (CODASPY&#x27;26). Our main contribution here is to produce an output in the same format as the inputs to the multiplication. This is needed for repeated multiplication of graph adjacency matrices, which we use to find cycles in graphs. Such cycles have been associated with money laundering, and this also applies to another graph pattern dubbed scatter-gather, which we can detect with the same approach. Our work therefore can be applied to privacy-preserving anti-money laundering detection.

  匹配依据：MPC: multi party computation, secure computation

  </details>

- **Local Leakage Resilience of Shamir Secret Sharing: Below Half Threshold Rate**
  2026-10-13 · MPC · [arXiv](https://arxiv.org/abs/2610.17711) · [IACR ePrint](https://eprint.iacr.org/2026/2454)
  Hai H. Nguyen

  <details><summary>摘要 / Abstract</summary>

  We study the local leakage resilience of Shamir secret sharing, where an adversary leaks a bounded number of bits from every share. For $n$ parties and reconstruction threshold $k$ over a prime field $\mathbb{F}_p$ with $p&gt;n$, we prove the following. (1) There is an absolute constant $c_{\mathrm{bh}} 0$ and $k\ge cn$, Shamir sharing is resilient to quadratic-residue leakage and to almost all local leakage functions of up to $η_c\log_2 p$ bits, for a constant $η_c&gt;0$. All three results follow from one analytic framework, which we develop for generalized Reed--Solomon codes: local leakage from a uniform codeword is statistically close to the same leakage from independent uniform field elements. The framework expresses the leakage distance as the norm of a function on the leakage outputs. The Efron--Stein decomposition splits this function into orthogonal components indexed by supports of dual codewords. Two tools bound the components: list recovery of the dual code, which is ordinary list decoding for one-bit leakage, and a generalized von Neumann inequality for MDS systems of linear forms that retains linearly many Gowers norms. The first tool gives the result above half, the second gives the constant-rate result, and applying both to different ranges of supports in the same decomposition gives the result below half.

  匹配依据：MPC: secret sharing

  </details>

- **HULK: An Efficient Algorithm for Enabling Fast Bulk Bitwise Operations on Homomorphically Encrypted Data**
  2026-10-13 · MPC · [arXiv](https://arxiv.org/abs/2610.18391)
  Mayank Kabra, Phillip Widdowson, Harshita Gupta, Rakesh Nadig, Nisa Bostancı, Eirini Tzermpou, Rakesh Kumar, Spiros Galanopoulos, Ataberk Olgun, Abdullah Giray Yağlıkçı, Mohammad Sadrosadati, Onur Mutlu

  <details><summary>摘要 / Abstract</summary>

  A wide range of important cloud applications, e.g., database analytics, graph analytics, and genome analysis, spend a considerable amount of time performing bulk bitwise operations (e.g., AND, OR, XOR). These applications often operate on highly sensitive data, making data privacy a critical concern. Homomorphic encryption (HE) enables secure computation on encrypted data without requiring decryption, ensuring privacy in untrusted and shared environments. We analyze 13 end-to-end applications across three domains (healthcare, graph, and database analytics) and observe that bulk bitwise operations take 62-100% of the execution time of the healthcare and graph workloads. The key problem is that existing HE approaches perform them with high-latency homomorphic operations (e.g., multiplication or lookup tables) and significantly increase the data size. Our goal is to enable fast bulk bitwise operations on homomorphically encrypted data by designing an efficient HE algorithm that reduces the use of these costly operations. To this end, we propose HULK, which performs two key steps: (1) it constructs bulk bitwise operations using low-cost homomorphic additions, which compute the Hamming weight of the encrypted operand bits in every slot of a packed ciphertext without any homomorphic multiplication, and (2) it decodes the result of an AND, OR, or XOR from the Hamming weight with a single indicator polynomial, keeping the result in the standard encoding. Across 13 end-to-end applications in healthcare, graph, and database analytics, HULK improves performance over the arithmetic approach used by prior works by up to 7.26x (CPU) and 6.65x (GPU), and on average by 2.32x/1.78x/1.45x (CPU) and 2.08x/1.70x/1.51x (GPU) for healthcare/graph/database analytics. When we increase the reduction depth in a representative application, HULK&#x27;s speedup grows to 10.10x over the state-of-the-art GPU baseline.

  匹配依据：MPC: secure computation

  </details>

- **Think Locally Before Computing Jointly: Efficient Secure Multi-Party Computation via Maximizing Local Processing**
  2026-10-12 · MPC · [arXiv](https://arxiv.org/abs/2610.17072)
  Mingfei Yu, Chenglu Jin, Giovanni De Micheli

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) lets parties evaluate a function over private inputs without revealing them. In garbled-circuit (GC) protocols, prior optimization has largely treated the number of non-linear gates, especially AND gates, as a proxy for cryptographic cost, and has focused on minimizing multiplicative complexity. We identify an orthogonal source of savings: a gate need not be garbled when one party knows or can locally compute its inputs; that party can evaluate it outside the secure protocol, even when the gate is non-linear. We introduce ownership-aware optimization for GC-based MPC, which minimizes non-linear gates requiring joint evaluation rather than total non-linear gates. We formalize this objective in a cost model and implement a compiler-integrated, gate-level framework that restructures Boolean circuits to increase party-local computation while preserving secure-computation semantics. The method is automated and general-purpose, and composes with existing multiplicative-complexity optimization. Experiments show that it reduces jointly evaluated computation and improves end-to-end GC performance on circuits with party-local structure, revealing protocol-cost savings missed by conventional GC cost models.

  匹配依据：MPC: garbled circuit, secure computation, secure multi party computation

  </details>

- **Modulus Operandi: Round-Optimal Modulus Conversion for MPC and Threshold FHE**
  2026-10-12 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2450)
  Ivan Damgård, Sebastian Hasler, Sebastian Kolby, Stanislas Pawlak

  <details><summary>摘要 / Abstract</summary>

  In secure multiparty computation (MPC), modulus conversion turns a sharing of a value $x$ modulo $q$ into a sharing of the same value modulo $t$, without leaking anything about $x$. One important application of modulus conversion is in threshold decryption for lattice-based cryptosystems, where a sharing modulo the ciphertext modulus has to be moved to the plaintext modulus before it can be opened. The most efficient protocols so far (Damgård et al., Asiacrypt 2026) are in the preprocessing model, assume $x$ is bounded away from $q$ by a constant factor and take two rounds for a prime target modulus, three rounds for arbitrary moduli, and one round when all moduli are 2-powers. We improve upon this by constructing three new modulus conversion protocols in the preprocessing model: - Our first conversion protocol takes a single round for arbitrary moduli, consisting of just one opening. - Our second conversion protocol is a variant of the first protocol, where in the preprocessing most of the secure multiplications are replaced by private inputs, which are checked in a batch using fully linear interactive oracle proofs (FLIOPs). This makes the preprocessing cheaper (amortized over a batch of conversions) when the number $N$ of parties is small. This comes at the cost of making the bound on $x$ a factor $N$ stronger. - Our third conversion protocol avoids the bound on $x$ altogether but takes two rounds. All our protocols are stated in the arithmetic black box (ABB) model, so they can run on top of a wide variety of MPC protocols, inheriting their corruption threshold and security model. To allow the third conversion protocol to run in two rounds, we construct the first one-round comparison protocol in the ABB model for comparing a bitwise shared $n$-bit value against a public threshold with polynomial-size preprocessing. Concretely, the preprocessing size is $\mathcal O(n^2)$ in general, and $\mathcal O(n^2 / \log n)$ in our case where the secret value is fixed in preprocessing. We also construct constant-round ABB protocols without preprocessing for computing symmetric functions and comparisons of values shared bitwise modulo powers of arbitrary primes (e.g., $2^k$), at communication quasi-linear in the number of input bits. Previously, this required either a sufficiently large prime or polynomially larger communication. Finally, we give an impossibility result for non-interactive modulus conversion, demonstrating that a single round is optimal: unless $t$ divides $q$, every non-interactive conversion for inputs $x &lt; q/\beta$ is incorrect with probability at least $\approx 1/(4\beta)$.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Verifiable Computation on Encrypted Data from Homomorphic Encryption over Random Encodings**
  2026-10-09 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2422)
  Jiayi Kang, Erik Pohle, Jannik Spiessens

  <details><summary>摘要 / Abstract</summary>

  Verifiable Computation on Encrypted Data (vCOED) enables clients to outsource computation while providing both privacy and integrity. A promising vCOED paradigm is blind proofs, which use homomorphic encryption (HE) to evaluate verifiable computation (VC) proofs on encrypted data. Despite their efficiency, blind proofs do not provide strong client privacy: a malicious server can exploit reaction attacks to learn information about the client&#x27;s inputs, intermediate values or final outputs. Our work addresses this limitation by introducing Homomorphic Encryption over Random Encodings (HERE). We formalize a new security notion, indistinguishability under chosen-plaintext attacks in the presence of an equality oracle over encodings (IND-CPA-E). We prove that combining IND-CPA-E-secure HERE schemes with blind proofs that verify computation over the encodings yields vCOED protocols with strong client privacy. We then instantiate a HERE scheme for functions of bounded degree $d$, using Shamir secret sharing at $(d+1)$ evaluation points under $(d+1)$ distinct HE keys. Finally, we demonstrate the concrete efficiency of our approach through an application to matrix-vector multiplication (MVM), a linear computation corresponding to $d=1$. The proof overhead (i.e. the ratio of the vCOED prover runtime to the homomorphic MVM runtime) in our combined vCOED protocol is as low as $2\times$, as demonstrated in our prototype implementation.

  匹配依据：MPC: secret sharing

  </details>

- **Lattice Bingo: Asynchrony and One-Shot Adaptivity in Verifiable Secret Sharing via Erasure Code Commitments**
  2026-10-09 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2432)
  Ittai Abraham, Aniket Kate, Aditi Partap, Ertem Nusret Tas

  <details><summary>摘要 / Abstract</summary>

  Asynchronous verifiable secret sharing (AVSS) allows a dealer to distribute a secret among parties while preserving privacy and consistent reconstruction, despite Byzantine faults and arbitrary message delays. It is a fundamental building block for Byzantine agreement, distributed key generation, and secure multiparty computation. Packed AVSS protocols share many secrets together to reduce communication per secret. The best known AVSS protocols achieve quadratic communication while sharing linearly many secrets. In particular, Bingo (Abraham et al., CRYPTO 2023) shares a batch of $\Theta(k)$ secrets among $k$ parties using $O(\lambda k^2)$ words of communication, while also achieving adaptive security, but relies on assumptions that are not post-quantum secure. Known post-quantum alternatives have higher worst-case communication for comparable batch sizes or require substantially larger batches to achieve linear amortized communication. We present Lattice Bingo, a lattice-based packed AVSS protocol with quadratic communication and linear packing. For every constant $\epsilon&gt;0$, it shares $\Theta(k)$ secrets among $k\geq(3+\epsilon)f$ parties, tolerates $f$ Byzantine parties, and uses $O(k^2\operatorname{poly}(\lambda))$ words of communication. It additionally achieves one-shot adaptive secrecy: the adversary may adaptively choose its corruption and reconstruction requests based on the public transcript observed so far, but must submit these requests together in a single batch. Our main technical contribution is a commitment scheme for two-dimensional linear codes based on the PowerBASIS assumption. We combine PowerBASIS commitments with the linear code based secret sharing of Applebaum, Nir, and Pinkas, replacing the Reed–Solomon encoding and KZG commitments used in Bingo. Our commitment supports proof interpolation, enabling parties to recover missing shares and their opening proofs. It additionally achieves a notion that we call one-shot simulation hiding. Together, these properties allow us to adapt Bingo’s framework to obtain Lattice Bingo with the same efficiency and one-shot adaptive security.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **The Power of Multislices in Monotone Computation**
  2026-10-08 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2415)
  Amos Beimel, Oded Nir

  <details><summary>摘要 / Abstract</summary>

  Motivated by recent constructions and barriers in secret sharing, we study multislice functions. These functions, parametrized by a width parameter $w$, take the value 0 on inputs of Hamming weight below a base value $k$, 1 on inputs of weight above $k+w$, and are monotone in between. We first investigate formulas over multislice gates, which generalize the formulas over slices model (Applebaum et al., TOCT 2026). We prove that, although multislices compute complicated functions, they do not help in computing the worst-case function when $w\ll n$; that is, there is an explicit monotone function such that for every $w$, every formula over multislice gates of width $w$ that computes it, regardless of its depth and gate fan-in, has size $2^{\Omega\left(n/((w+1)\log^2 n)\right)}$. Our lower bound is based on a randomized Karchmer-Wigderson protocol for multislices that can be amortized across the formula. As a complementary result, we show how to realize multislices using slice gates, i.e., multislice gates of width 0; the construction uses a simple peeling recursion. Consequently, every width-$w$ multislice on $n$ variables has a formula over slice gates of size at most $2n^{w+1}$ and depth $(w+1)$. The same construction allows to compute multislices with small monotone real formulas and circuits, two models introduced by Pudl\&#x27;ak (J. Symb. Log., 1997) in the context of proof complexity. This result also has an application to secret sharing: it yields, for sufficiently long secrets, multilinear secret-sharing schemes for width-$w$ multislices with maximal information ratio $n^{O(w+1)}$, which is polynomial for every fixed $w$. In addition, we prove that an explicit access structure requires shares of size $2^{\Omega(n)}$ in every secret-sharing scheme from a family of schemes that captures all currently known constructions for general access structures with share size $2^{cn+o(n)}$, for $c&lt;1$. Our proof goes through an exponential lower bound on the size of formulas over so-called CDS gates and ideal linear gates.

  匹配依据：MPC: secret sharing

  </details>

- **Mercury: Fuzzy Private Set Intersection with Communication and Computation Logarithmic in the Threshold**
  2026-10-08 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2409)
  Qi Liu, Kang Yang, Binwu Xiang, Xiaojie Guo, Cheng Hong, Yu Yu

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection (PSI) allows two mutually distrusting parties to compute the intersection of their sets without revealing any additional information and has found numerous applications. The approximate matching required by various applications has led to the development of Fuzzy PSI (FPSI), a variant of PSI that identifies approximate intersection elements under a public distance threshold \(\delta\). Reducing computation and communication costs remains an important challenge for FPSI. In this paper, we present a new FPSI protocol, called Mercury, which achieves logarithmic computation and communication complexity with respect to threshold \(\delta\). Our protocol exploits the correlation of the intersection and the point pairs held by the parties, and efficiently identifies the neighboring point pairs by a mixed protocol from homomorphic encryption and secure two-party computation using a &quot;mask-then-compare&quot; technique. We implemented Mercury and evaluated both its sender-private and standard FPSI variants. For balanced two-dimensional inputs, Mercury-SP achieves \(9.0\sim63.9\times\) runtime speedups and reduces communication by a factor of \(8.7\sim26.1\) across the evaluated thresholds and set sizes in the LAN setting, compared to the FPSI protocol by Dang et al. (CCS&#x27;25). In the completed unbalanced experiments, Mercury-SP achieves \(55.7\sim132.4\times\) WAN runtime speedups compared to the FPSI protocol by Piske et al. (CCS&#x27;25).

  匹配依据：MPC: private set intersection, secure two party computation

  </details>

- **Individual Cryptography from Iterated Squaring**
  2026-10-08 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2418)
  Georg Fuchsbauer, Christoph U. Günther, Charlotte Hoffmann, Krzysztof Pietrzak, Fabian Regen

  <details><summary>摘要 / Abstract</summary>

  Individual cryptography (Dziembowski et al. Crypto&#x27;23) and complete knowledge (Kelkar et al. CCS&#x27;24) aim at constructing protocols that ensure that some individual party must know a secret value in the clear, and so the computation cannot have been “outsourced” to an MPC computation. Two central primitives are proofs of complete (or individual) knowledge, which enforce that some party actually knows the secret witness, and secret sharing with snitching, which enforces that whenever the secret is reconstructed, some party must learn a certificate of this fact. The instantiations proposed by both papers (Crypto&#x27;23 and CCS&#x27;24) ensure that to compute a proof or reconstruct the shared secret, a large number of hash function evaluations is necessary. Thus, at least one party must compute many of these “in the clear” (and not via MPC) and from the hash function inputs one can extract the secret (in the random oracle model). In practice, they suggest using Bitcoin mining hardware. Sequential proofs of complete knowledge have recently been proposed, which use proofs of sequential work to enforce that the hashes are performed sequentially. As a consequence, it suffices to require a much smaller number of hashes, and thus such primitives can be implemented on standard hardware. Unfortunately, this approach does not work for primitives like secret sharing, as one would need to efficiently sample the challenge for the sequential computation together with its solution. In this work, we leverage ideas from time-lock puzzles to overcome this issue. We construct secret sharing with snitching and encryption with self-incriminating proofs where reconstruction/decryption is sequential. The security of our scheme relies on a new knowledge assumption, which informally states that whenever parties that hold secret shares of an RSA modulus N=pq jointly compute 2^2^T N for some large T (too large to perform a sequential computation of length T in MPC), then at least one of them must have learned a multiple of N.

  匹配依据：MPC: secret sharing

  </details>

- **Improved Local Leakage Resilience of Shamir Secret Sharing and Worst-Case Optimal Polynomial Intersection**
  2026-10-08 · MPC · [arXiv](https://arxiv.org/abs/2610.12357)
  Yihang Sun, Mary Wootters

  <details><summary>摘要 / Abstract</summary>

  We study two problems: Local Leakage Resilience (LLR) for Shamir secret sharing, and worst-case Optimal Polynomial Intersection (OPI). Both problems concern polynomials $Q(X)$ of degree less than $k$, over a prime-order finite field $\mathbb{F}_p$. In LLR for Shamir secret sharing, one asks how much one can learn about $Q(0)$ given a few bits leaked from each of $Q(α_1), \ldots, Q(α_n)$, for distinct non-zero evaluation points $α_i \in \mathbb{F}_p$. In OPI, one is given input list $S_1, \ldots, S_n \subset \mathbb{F}_p$, and wants to find a polynomial $Q(X)$ of degree less than $k$ so that $Q(α_i) \in S_i$ for as many $i$ as possible. Leveraging recent connection between these two problems due to (Sun, Wootters 2026), we improve the state-of-the-art for both problems. For LLR, we show that there is some constant $δ&gt; 0$ so that, as long as $R := k/n \geq 1/2 - δ$, Shamir secret-sharing is one-bit locally leakage resilient (meaning that one can learn only a negligible amount about $Q(0)$). This is the first result to break the so-called &quot;one-half barrier&quot; for LLR, and improves over the previous best known result, requiring $R \geq 0.668$ (Kasser, 2025). For OPI, we give a quantum algorithm that finds a polynomial $Q(X)$ that agrees with at least a $\mathsf{SCL}_ρ(R)-\varepsilon$ fraction of the lists in expectation, for every fixed $\varepsilon&gt;0$, where $\mathsf{SCL}_ρ$ is the \emph{semicircle law} of (Jordan et al., 2025). This improves previous algorithmic (and existential) results of (Jo, 2026) and (Horinaga, Yamakawa, 2026). We also give further improved existential results. We also adapt the hardness result of (Yamakawa, Zhandry, 2024) to apply to OPI (rather than a folded version); over large fields, this gives an unconditional separation between the quantum and classical hardness of OPI relative to a membership oracle.

  匹配依据：MPC: secret sharing

  </details>

- **The Price of Privacy: Randomness Complexity of Graph-Based Multi-Secret Sharing**
  2026-10-07 · MPC · [arXiv](https://arxiv.org/abs/2610.10002) · [IACR ePrint](https://eprint.iacr.org/2026/2395)
  Piotr Marszalik

  <details><summary>摘要 / Abstract</summary>

  We study the randomness required to share possibly correlated secret bits among parties connected by a graph. A dealer places shares on the edges so that each party can recover its own secret from its incident shares and learn nothing about the others beyond what its own secret reveals. Anilkumar et al. completely determined the minimum randomness required for three binary secrets. We extend this study to four secrets and obtain results for arbitrary numbers of secrets on general graphs. For four parties on a complete graph, we determine the minimum number of random states for every set of permitted secret combinations: the possible values are one, two, three and four. We also characterize when one random bit suffices on an arbitrary graph.

  匹配依据：MPC: secret sharing

  </details>

- **The Geometry of Collusion Leakage in Inner-Product Functional Encryption**
  2026-10-07 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2404)
  Ferdinando Zullo

  <details><summary>摘要 / Abstract</summary>

  Inner-product functional encryption (IPFE) allows the holder of a functional key for a vector $y$ to learn $\langle x,y\rangle$ from an encryption of $x$, and nothing more. Keys, however, accumulate: a coalition holding sufficiently many independent keys recovers the plaintext. We model each institution by the span $W_i\leq\F_q^n$ of its authorized key vectors and show that a coalition $I$ determines the plaintext exactly modulo $(\sum_{i\in I}W_i)^\perp$; for a uniform plaintext it learns exactly $\dim\sum_{i\in I}W_i$ field symbols. The resulting leakage function is a representable and entropic polymatroid. We then study authorization spaces of dimension $r$ whose pairwise intersections have dimension at most $h$. We prove that some coalition of size $c\geq2$ always learns at least $\min\{n,2r-h+c-2\}$ dimensions, and we give a Vandermonde-type construction in which every coalition of size $c$ learns exactly this amount, for all $c$ simultaneously. Hence the largest achievable reconstruction threshold is $n-2r+h+2$, which gives an exact tradeoff between functional diversity and collusion resistance. The optimal configuration is a sunflower, an equidistant subspace code and a generalized arc; its orthogonal complements form a generalized dual arc, and for $r=1$ it reduces to Reed--Solomon secret sharing.

  匹配依据：MPC: secret sharing

  </details>

- **Round Optimal MPC With Provable Cheater Identification**
  2026-10-07 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2393)
  Yashvanth Kondi, Divya Ravi, Jure Sternad, Sophia Yakoubov

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation with provable identifiable selective abort (PISA), introduced by Kondi and Ravi (CCS 2025), guarantees that every honest party either obtains the computation output or a certificate that convinces any external auditor that a specific party cheated. Crucially, honest parties need not agree: some may get output while others receive evidence of cheating. In contrast, secure computation with identifiable abort (IA) requires just such unanimity; however, in the event that an honest party doesn&#x27;t get output, it need merely be able to point to a cheater - not to prove their guilt. Secure computation with IA classically requires broadcast. Kondi and Ravi demonstrated that secure computation with PISA, on the other hand, can be built over point-to-point channels alone. While PISA is feasible exactly when guaranteed output delivery is, i.e. for $t &lt; n / 2$, the best known construction over point-to-point channels requires six rounds. We settle the round complexity of PISA for all but a narrow band of thresholds. We prove that two rounds are impossible for $t \geq n /3$, even with arbitrary setup and computational assumptions; we give a three-round protocol for any $t &lt; n/2$, which is therefore round-optimal for $n / 3 \leq t &lt; n/2$; and we give a two-round protocol for $t &lt; n/4$. The two-round protocol introduces a new primitive called one-or-nothing secret sharing with omissions.

  匹配依据：MPC: secret sharing, secure computation, secure multiparty computation

  </details>

- **Practical and Efficient MPC from FHE, without ZKPoKs**
  2026-10-07 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2403)
  Kelong Cong, Nigel P. Smart, Titouan Tanguy, MIchael Walter

  <details><summary>摘要 / Abstract</summary>

  Fully Homomorphic Encryption (FHE) enables one to implement low-round and low-communication complexity Multi-Party Computation (MPC) which is secure in the static malicious corruption model. By expanding on an idea presented in the full version of the FHE-based MPC protocol of Smart (IMA, 2023), we show how to completely remove the need for Zero-Knowledge Proofs-of-Knowledge in that protocol. This simplification makes the final security proof of the MPC protocol much simpler, and more modular. The new protocol makes use of an FHE scheme with an encrypted PRF functionality, and in addition to our main result we formalize the security of such encrypted PRFs and prove the construction of Deo et al. (CCS 2025) secure in this model.

  匹配依据：MPC: multi party computation

  </details>

- **Mixed States in Quantum Rabin Oblivious Transfer**
  2026-10-07 · MPC · [arXiv](https://arxiv.org/abs/2610.09796)
  James T. Peat, Lara Stroh, Kenny Campbell, Erika Andersson

  <details><summary>摘要 / Abstract</summary>

  Oblivious transfer (OT) is a fundamental cryptographic primitive that is useful for realizing any two-party computation. Since information-theoretically secure perfect OT is impossible classically and quantumly, research has focused on imperfect protocols, exploring how close to perfect one can get against unbounded dishonest parties. While current approaches often make use of pure quantum states, recent work suggests that mixed quantum states may improve performance. In this paper, we investigate the use of mixed quantum states in Rabin oblivious transfer, where a sender holds one bit and a receiver learns its value with a certain probability while the sender remains ignorant of whether the receiver learned it. We present three mixed-state protocols constructed with two distinct methods, extending an existing pure-state scheme and employing a probabilistic approach, and demonstrate improved performance compared to classical and quantum pure-state protocols across varying parameters.

  匹配依据：MPC: oblivious transfer, two party computation

  </details>

- **Fair and Efficient Helper-Aided MPC with Cheater Identification**
  2026-10-07 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2392)
  Maximilian Kamps, Protik Paul, Divya Ravi

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) enables privacy-preserving tasks such as auctions and voting. In practice, more than half of the parties may collude, making security against a dishonest majority desirable. Unfortunately, dishonest-majority MPC suffers from high communication and can achieve only abort security. For instance, in an auction, an adversary may abort after learning the outcome and rerun the protocol with a higher bid. Helper-aided MPC mitigates these limitations by introducing a semi-honest, non-colluding helper, a model that naturally fits settings with a central governing or coordinating entity and provides strong guarantees even when up to $n-1$ parties are malicious. The model assumes that the adversary can either semi-honestly corrupt the helper or maliciously corrupt up to $n-1$ parties (excluding the helper). While existing helper-aided protocols are fair i.e. either all parties receive the output or none do; they still allow the adversary to abort without any penalty and deny output to all parties. This behavior is undesirable in practice, as parties may incur the cost of computation without receiving the output. In this work, we design efficient helper-aided MPC protocols that achieve identifiable fairness: either all parties obtain the output, or—if an abort occurs—no party receives the output, and the honest parties identify at least one common cheater. We propose two protocols, $\mathsf{Alhena}$ for synchronous networks and $\mathsf{Wasat}$ for asynchronous networks which provide the stronger guarantee of identifiable fairness compared to the state-of-the-art fair protocols $\mathsf{Asterisk}$ (Kamarkar et al. IEEE S&amp;P 2024) and $\mathsf{Castor}$ (Kamarkar et al. IEEE S&amp;P 2026) in the respective network settings. Our experiments show that, in the online phase, $\mathsf{Alhena}$ and $\mathsf{Wasat}$ achieves speedups of $4-12.5\times$ and $2.5-5\times$ over $\mathsf{Asterisk}$ and $\mathsf{Castor}$ respectively. Furthermore, in the preprocessing phase, $\mathsf{Wasat}$ exhibits speedup of $\approx 3\times$ over $\mathsf{Castor}$. Notably, our protocols are designed in such a way that the online performance remains unaffected by active misbehaviour.

  匹配依据：MPC: secure multi party computation

  </details>

- **Collusion-Secure Semi-Quantum Secret Sharing Scheme using a Quantum Third Party**
  2026-10-07 · MPC · [arXiv](https://arxiv.org/abs/2610.10176)
  Santanu Majhi, Nirupam Basak

  <details><summary>摘要 / Abstract</summary>

  The security of a secret sharing protocol is compromised if one or more dishonest participants can reconstruct the secret by deviating from the prescribed protocol, particularly when such malicious behavior remains undetected. Semi-Quantum Secret Sharing (SQSS) is a variant of secret sharing in which the participants possess only classical capabilities, such as preparing and measuring qubits in the computational ($Z$) basis, while a quantum-capable third party assists the dealer in generating and distributing quantum shares of a classical secret. The limited quantum capabilities of the participants in SQSS protocols may introduce vulnerabilities to collusion attacks, enabling an assisting quantum third party, in collaboration with a dishonest classical participant, to jointly recover the secret even without detection. In this work, we propose a novel SQSS protocol that eliminates this vulnerability and achieves information-theoretic security against collusion attacks. We further prove that the proposed protocol is secure against a broad class of external and internal attacks. Finally, a comparative analysis demonstrates that our construction advances existing SQSS protocols by simultaneously optimizing qubit efficiency, involves a classical dealer, and resilience against DCNA attacks using basic Bell states.

  匹配依据：MPC: secret sharing

  </details>

- **Truffle: Maliciously Secure Three-Party Shuffles with Applications to Parsing**
  2026-10-06 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2376)
  Nidhish Bhimrajka, Yashvanth Kondi, Daniel Noble, Bhavish Raj Gopal

  <details><summary>摘要 / Abstract</summary>

  Deploying Secure Multiparty Computation (MPC) to operate on data from real world sources requires many connective elements that have not received much attention in the literature. One prominent example is that MPC protocols typically assume conveniently structured data, whereas data in the real world comes in formats that are meant to be handled by string parsing engines. In this work, we give a new constant round protocol for securely parsing secret shared strings into an MPC-friendly format, built upon secure shuffle as a key primitive. Secure shuffle applies a permutation to a list while keeping both the permutation and the underlying data secret-shared at all times. While highly efficient protocols exist in the semi-honest setting, achieving malicious security has incurred significant overhead in both rounds and communication. We present Truffle, a new three-party shuffle protocol that is secure against one active corruption to bridge this gap. Truffle achieves an amortised round complexity that for the first time matches the state-of-the-art semi-honest protocol, while incurring only sublinear communication overhead. The core technique that underlies Truffle is a novel distributed verifier zero-knowledge proof that checks the correctness of a putative shuffle. We implement Truffle and show via benchmarks that it is performant enough to handle real application data. Beyond parsing secret shared data, secure shuffle finds applications in graph analytics, anonymous communication, Distributed Oblivious RAM, aggregate statistics, and secure sorting, each of which stand to benefit from the improvement that Truffle provides.

  匹配依据：MPC: secure multiparty computation

  </details>

- **The Post-Quantum Cost of Garbled-Circuit Bitcoin Bridges**
  2026-10-06 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2383)
  Mukesh Tiwari, Aaron Feickert

  <details><summary>摘要 / Abstract</summary>

  Recent Bitcoin bridge designs rely on verification of succinct proofs to process withdrawals. This requires off-chain garbled circuit evaluation of a succinct proof, the input labels for which must be encoded on chain in a manner compatible with malicious security. We assess the post-quantum vulnerability of these cryptographic components, and examine the costs of secure alternatives. Circuit sizes for post-quantum proving systems can be made smaller than the current pairing-based baseline, but at the cost of significantly higher proof sizes that incur greater cost and require multiple Bitcoin blocks to encode. We suggest avenues of future research to improve efficiency of proofs, circuit representations, and input encodings.

  匹配依据：MPC: garbled circuit

  </details>

- **Runaway Reaction: When Benign Skills Compose into Malicious Behavior**
  2026-10-05 · MPC · [arXiv](https://arxiv.org/abs/2610.05943)
  Zunlong Zhou, Ziyuan Yang, Mengyu Sun, Yi Zhang

  <details><summary>摘要 / Abstract</summary>

  Agent skills package task-specific knowledge and procedures that can be composed to support complex agent tasks, while public marketplaces provide a growing pool of reusable skills. Existing security vetting, however, largely evaluates skills in isolation, leaving composition-induced risks underexplored. Such risks arise because composing benign skills expands the agent&#x27;s capability space, enabling behaviors unavailable to any skill alone. Interestingly, we find that directly composing benign skills can already induce malicious behaviors, even when every individual skill passes security vetting. We further find that some target malicious behaviors remain difficult to realize through direct composition, even when the selected skills collectively provide the required capabilities. To systematically instantiate these attacks, we present Compositional Risk Induction via Multi skill Execution (CRIME). CRIME first uses the Malicious Plot Casting (MPC) module to decompose a target malicious behavior into complementary requirements and identify suitable benign skill compositions from public skill repositories. For compositions that cannot directly realize the target behavior, the Runaway Reaction Steering (RRS) module uses execution feedback to iteratively refine the selected skills toward the target while requiring each skill to remain benign under standalone vetting. The resulting composition is then passed to the Skill Reaction Chamber (SRC) module, where the skill pair is executed in a sandbox and the resulting environmental consequences are examined to determine whether the target behavior has occurred. Unsuccessful cases are returned to RRS for further refinement. Furthermore, we construct a benchmark of 4,000 public skills across eight cybersecurity behaviors for systematic evaluation of composition-induced vulnerabilities.

  匹配依据：MPC: mpc (context)

  </details>

- **Quantum Leakage from Shamir Sharing with Correlated Resources**
  2026-10-05 · MPC · [arXiv](https://arxiv.org/abs/2610.06350)
  Isaac Barouch Essayag, Aryeh Lev Zabokritskiy

  <details><summary>摘要 / Abstract</summary>

  We study leakage from Shamir secret sharing when each device uses its share to produce one qubit from an initial quantum resource independent of the secret and sharing randomness. We prove exponentially small trace distance between the leakage states of any two secrets, when reconstruction requires a sufficiently large fraction of the shares, for fixed stationary chains satisfying an upper operator mixing condition and for resources generated by fixed finite quantum memories with primitive transfer channels. These guarantees permit arbitrary extensions of the device marginal as adversary side information and hold uniformly over prime fields larger than the number of shares. For independent device--reference pairs, which provide the quantitative input to the argument, we determine the optimal exponential base when reconstruction requires all shares: $2\sqrt2/π$ for a qubit and $2/π$ for a classical bit, in both cases allowing arbitrary finite references. A comparison of selected marginals with product states converts the bounds for independent device--reference pairs into security guarantees for the correlated resources.

  匹配依据：MPC: secret sharing

  </details>

- **One-Round Threshold XMSS and SPHINCS+ from Fully Homomorphic Encryption**
  2026-10-05 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2360)
  Jung Hee Cheon, Kevin Choi, Hyeoncheol Joo, Taeseong Kim

  <details><summary>摘要 / Abstract</summary>

  While hash-based signatures such as XMSS and SPHINCS$^+$ are well-established and play a key role in post-quantum cryptography, thresholdizing them to enable use in distributed systems remains a challenge. In particular, their lack of exploitable structure prevents any algebraic attempts that are otherwise possible in the context of classical signatures such as ECDSA, Schnorr, RSA, or BLS, whereas general-purpose MPC techniques are costly in round complexity. In this work, we construct and implement the first one-round threshold protocol for XMSS and SPHINCS$^+$, with concrete parameters yielding full backward compatibility. At a high level, the secret key is shared among the signing parties while the signing algorithm is evaluated homomorphically using a threshold fully homomorphic encryption scheme. Any $t$-of-$n$ parties, via threshold decryption, can collaboratively derive the signature, which is accepted by the unmodified RFC 8391 or FIPS 205 verifier. At a technical level, we develop efficient homomorphic SHAKE evaluation over discrete CKKS for varying batch sizes. Analyzing XMSS and SPHINCS$^+$ signing reveals parallel hash computations and data-dependent selections, which we handle through batching and homomorphic lookup to obtain end-to-end circuits. Our implementation amortizes SHAKE256/256 evaluation to $3.4\,\text{ms}$ per hash and completes online threshold XMSS signing in $0.69\,\text{s}$. Threshold SPHINCS$^+$ has roughly two orders of magnitude higher signing latency but over an order of magnitude lower setup latency than XMSS.

  匹配依据：MPC: mpc (context)

  </details>

- **Cryptanalysis of a Class of Ideal Secret Sharing Schemes Based on the CRT for Polynomial Rings**
  2026-10-05 · MPC · [arXiv](https://arxiv.org/abs/2610.06312)
  Jian Ding, Zhiyuan Guo, Hongju Li, Yuying Man

  <details><summary>摘要 / Abstract</summary>

  Based on the CRT for polynomial rings, Yang, Zhu, Fu and Xia (ISIT 2026) proposed a compartmented secret sharing scheme for the compartmented access structure with lower bounds, claiming it can be ideal. We exhibit three families of unauthorized subsets that reconstruct the secret. The scheme is therefore insecure, except for a degenerate choice of parameters in which the only authorized subset is the whole participant set. The flaw in the security analysis is that it does not take all published polynomials into account. Similar flaws appear in the same first author&#x27;s hierarchical schemes (ISIT 2024, 2026).

  匹配依据：MPC: secret sharing

  </details>

- **Secure D2D Coded Caching under Radius-Limited Connectivity via Lifting**
  2026-10-04 · MPC · [arXiv](https://arxiv.org/abs/2610.05065)
  Han Fang, Nan Liu, Wei Kang

  <details><summary>摘要 / Abstract</summary>

  Secure device-to-device (D2D) caching requires users to generate delivery signals from their own caches and to recover their requested files without learning the other files. We construct schemes that meet both requirements when communication is limited to nearby users. The network consists of $K$ users on a cycle, a library of $N$ independent files, and a reception radius $r$. Delivery uses one round of noiseless orthogonal local broadcasts, with no server transmission. Each user&#x27;s cache has capacity $M$ file units. An outer secret-sharing code assigns file shares to senders, and a secure local caching scheme at each sender delivers the requested shares. The cache budget includes the sender&#x27;s library representation, random state, and delivery keys. We prove that each receiver&#x27;s cache and all audible broadcasts jointly reveal no information about nonrequested files, despite the dependence between the outer shares. The converse counts transmissions crossing a contiguous user block and uses secrecy to remove one user&#x27;s observation from the entropy bound. Let $h=2r$ and $K\ge h+1$. The private coded caching (PCC) instantiation attains the minimum peak sum load $K/h$ for every $M\ge Nh$ when $N&gt;1$. For $N\ge K$, its memory-sharing envelope is within a factor $15$ of the optimum throughout $M\in[N/h+2,Nh]$. We also apply lifting without secrecy constraints, achieving the optimal load on $M\in[hN/(h+1),N]$ and a factor-$9/2$ guarantee on $M\in[N/(h+1),N]$ when $N\ge K$.

  匹配依据：MPC: secret sharing

  </details>

- **Understanding Sigma Protocols via MPC-in-the-Head**
  2026-10-03 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2322)
  Haiyang Xue

  <details><summary>摘要 / Abstract</summary>

  In this paper, we propose an understanding of classical Sigma protocols (as denoted by $\Sigma$-protocols in the literature) through the lens of the MPC-in-the-head (MPCitH) paradigm. We seek not to construct new schemes, but to build a formal bridge connecting these two foundational areas. While many elegant yet foundational Sigma-protocols were introduced decades ago as standalone algebraic or combinatorial interactive proofs, reconsidering them via the modern aspect of (extended) MPCitH significantly enhances our cryptographic insight into their underlying structures. We present a formal mapping that translates classical commitment-challenge-and-response into the internal views of virtual parties, communicating via private point-to-point or public broadcast channels, secret-sharing schemes, commitments, and MPC consistency/correctness checks. By deconstructing algebraic schemes as linear secret-sharing protocols over public channels and combinatorial schemes as discrete threshold MPC instances over private/public channels, we isolate the exact structural reasons why their soundness and efficiency characteristics diverge. The protocols include: - Algebraic schemes: Schnorr, Okamoto, Chaum-Pedersen, Guillou-Quisquater, GMR for QR and discrete log over an unknown-order group. - Combinatorial schemes: Stern, GMW for Graph 3-Coloring, and Graph Isomorphism, among others. Although reinterpreting these already elegant, classic proofs using a heavy-weight machinery like MPCitH might seem redundant, it deepens our understanding of their underlying design principles.

  匹配依据：MPC: secret sharing

  </details>

- **Trusted Hardware Acceleration for Malicious-Secure Function Secret Sharing**
  2026-10-03 · MPC · [arXiv](https://arxiv.org/abs/2610.04818)
  Yujie Xue, Yijing Peng, Lin Liu, Shaojing Fu, Shaoqing Li, Yaohua Wang, Rongmao Chen, Yang Guo

  <details><summary>摘要 / Abstract</summary>

  Function secret sharing (FSS) underlies two-party private inference and private information retrieval, with cost dominated by generating, moving and evaluating distributed point function (DPF) keys. A trusted GPU-integrated distributed function accelerator (DFA) removed key movement by generating and consuming keys locally, but tolerates only semi-honest adversaries. A malicious host or GPU can tamper with shares, replay one-time material, swap buffers after checking, request early outputs, or abuse the accelerator as a forgery oracle, while malicious FSS ships large authenticated keys or multiplies DPF work. We present VIGOR-DFA, protecting the chain from authorized input to authorized output release with three mechanisms: a fresh authentication epilogue using three field multiplications per DPF output, 3.8-4.0 times faster per gate than per-lane DPF tag trees; a freeze-before-challenge check of every opening with t = 3 independent MAC lanes over F_{2^61-1}; and a role-bound one-time resource ledger with a release guard, in a protected datapath beside the GPU L2 cache. We prove stand-alone static malicious security with abort in a protected-module model, with statistical error Q(2/p)^t approximately 2^-148 for Q less than or equal to 2^32 checked batches. Our DFA-calibrated model shows that, against dealer-based malicious FSS modeled after the protocol family of Shark, VIGOR-DFA removes 21.8-563 GB of per-query offline authenticated material and, mainly by generating it in-module, lowers LAN latency by 10.1-14.0 times (1.5-1.8 times excluding offline distribution) and energy by 3.0-3.9 times. Malicious security costs 2.5-3.5 times LAN latency over semi-honest DFA and 0.145 mm^2 at 7 nm. We have completed the verification of specifications and the functional CPU reference model, including GPU/RTL conformance verification, protected runtime evaluation, and deployment-related tests.

  匹配依据：MPC: secret sharing

  </details>

- **Quantum-State Oblivious Transfer over Quantum Erasure Channels**
  2026-10-03 · MPC · [arXiv](https://arxiv.org/abs/2610.04667)
  Remi A. Chou

  <details><summary>摘要 / Abstract</summary>

  We study quantum-state oblivious transfer over the quantum erasure channel under information-theoretic security guarantees. Specifically, Alice holds two quantum systems, Bob wishes to recover one of them, and the parties have access to independent channel uses and authenticated public classical communication, with no initial shared entanglement. We consider both honest-but-curious and malicious behavior. We establish finite-blocklength converse and achievability bounds, which match in the honest-but-curious setting. The malicious setting construction combines interactive hashing with tests of whether Bob received selected channel outputs, and distributes each input across several qubits so that erasures conceal an entire input from a dishonest receiver, even when the inputs are entangled with an external reference. We also derive fixed-error asymptotic expansions and show that both malicious and honest-but-curious settings have the same capacity.

  匹配依据：MPC: oblivious transfer

  </details>

- **Multiparty Homomorphic Secret Sharing From Distributed Discrete Logarithm**
  2026-10-02 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2308)
  Pierre Meyer, Claudio Orlandi, Lawrence Roy, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  Homomorphic secret sharing (HSS) enables non-interactive distributed evaluation of functions on secret-shared inputs. While two-party HSS is well understood, multiparty constructions remain limited in expressiveness and efficiency. We present a general framework for constructing multiparty HSS from two-party semi-private HSS (which in turn can be instantiated using distributed discrete logarithms) via a new party virtualization paradigm. In a semi-private HSS, some designated inputs may be fully known to specific servers, while the remaining inputs remain hidden. Starting from two-party semi-private schemes, we obtain $N$-party semi-private HSS supporting compositions of polynomial computations and restricted multiplication straight-line programs, for $N = O(\log \lambda / \log \log \lambda)$. We further upgrade semi-private HSS to fully private HSS for functions of polynomial degree and polynomially bounded Waring rank. As a consequence, we obtain multiparty distributed point functions with key size polynomial in $\lambda$ and $\log |D|$, for a domain $D$ of superpolynomial size. When the underlying two-party scheme supports offline/online sharing, the resulting multiparty DPFs are programmable. Our framework admits instantiations under standard assumptions including DCR and class-group assumptions.

  匹配依据：MPC: secret sharing

  </details>

- **Breaking the $n^2$ Barrier: Information-Theoretic MPC with Sub-Quadratic Communication**
  2026-10-02 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2311)
  Alexander Bienstock, Yuval Efron, Kevin Yeo

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) considers the problem of securely computing a function across $n$ parties such that no adversary controlling $t$ corrupted parties may learn any additional information beyond the function output. For information-theoretic security in the honest majority setting, recent works have made tremendous progress in reducing the MPC communication costs for large circuits obtaining as low as $\tilde{O}(|C|)$ total communication. To date, all information-theoretic MPC protocols require an additive $\tilde{\Omega}(n^2)$ communication independent of the circuit size that becomes the dominant cost for small circuits. In this work, we consider the problem of building more efficient information-theoretic MPC protocols with $o(n^2)$ communication for small circuits. For corruption threshold $t&lt; (1/2-\epsilon)\cdot n$, we present an information-theoretic MPC protocol secure against adaptive and malicious adversaries with subquadratic communication for a wide range of circuits, including those in which the number of input parties $I$ satisfies $|I| = o(n)$, circuit size $|C| = o(n^{1.5}/|I|)$, and circuit depth $\mathsf{depth}(C) = o(n)$; for example, $|C| = o(n^{3/4})$ and $|I| = o(n^{3/4})$ input parties. To our knowledge, this is the first information-theoretic MPC protocol with $o(n^2)$ communication for a wide-range of circuit classes. Furthermore, we note the requirement of sublinear input parties $|I| = o(n)$ is necessary to obtain $o(n^2)$ communication due to the $\Omega(|I| \cdot n)$ lower bound by Damgård {\em et al.} [EUROCRYPT&#x27;16]. To obtain our new MPC protocol, we develop new techniques for key MPC subroutines including randomness generation, player virtualization and output reconstruction with $o(n^2)$ communication leveraging the sublinear number of input parties, $|I| = o(n)$, and randomized output distribution with unpredictable communication patterns. Finally, we also prove a separation showing that $o(n^2)$ communication MPC is impossible for adversaries with stronger than standard adaptive rushing capabilities even for constant-size circuits.

  匹配依据：MPC: secure multi party computation

  </details>

- **An Input-Fed AES-Round Family for Fixed-Length Hashing**
  2026-10-02 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2314)
  Peter Rindal

  <details><summary>摘要 / Abstract</summary>

  Secure computation often hashes high-entropy fixed-length values in inner loops. A public permutation with terminal Davies--Meyer feed-forward can expose the permutation value when an application applies another feed-forward step. We study an input-fed alternative that injects the input after every AES round. The base construction, $H_{128}:\{0,1\}^{128}\to\{0,1\}^{128}$, uses ten full AESENC-style rounds with keys $x+c_i$ and no AES key expansion. Its concrete analysis adapts differential, collision, linear, integral, and meet-in-he-middle (MITM) methods to this shared-input round-key interface. We prove a three-round integral distinguisher and give a five-round anchored MITM attack candidate with estimated time $2^{120}$; the remaining results provide reduced-round evidence rather than a proof of random-function behavior. On an AMD Ryzen 9 7950X, measured scalar and eight-lane AES-NI costs are within one percent of fixed-key AES-128; a sixteen-block VAES kernel is 2.3\% slower. Two extensions use the same input-fed principle. The tweakable construction $H_{128}^{\mathsf{tw}}$ splits a 72-bit public counter into an eight-bit tweak and a 64-bit epoch. One public schedule serves 256 consecutive positions, and consecutive fixed-key AES outputs under a published key supply the epoch schedules. Within one epoch, a pair with different tweaks can cancel at most one complete boundary injection. The construction also admits an exact 256-query two-round integral distinguisher. The wide construction $H_{256}$ maps 256 bits to 256 bits. It uses two AES lanes and adopts the column permutation and round constants of Haraka-256 v2 [KLMR16]. We analyze the differential, integral, collision, slide, rebound, and MITM mechanisms introduced by these extensions. A supporting ideal-permutation analysis shows that affine wrappers with one or two permutation calls fail generically. For three calls with independently uniform public constants, it gives a birthday-order bound when the distinguisher completes its primitive queries before querying the target. Finally, we define checkable punctured vectors and prove a GM-style protocol secure against static semi-honest corruptions in the ideal-OT and random-oracle model.

  匹配依据：MPC: secure computation

  </details>

- **Robust and leakage-resilient device-independent oblivious transfer in MiniQCrypt**
  2026-10-01 · MPC · [arXiv](https://arxiv.org/abs/2610.01421)
  Zhili Chen, Rahul Jain, YaoNan Zhang

  <details><summary>摘要 / Abstract</summary>

  Assuming post-quantum one-way functions, we construct device-independent (DI) oblivious transfer (OT) and bit commitment: honest parties use only trusted classical computation to operate untrusted quantum devices, which may share arbitrary entanglement and behave non-IID. Security is simulation-based against quantum polynomial-time adversaries and composes sequentially with efficient simulators. One protocol skeleton serves both, in two regimes. With isolated laboratories and coordinate-local measurements in the honest receiver&#x27;s device, it tolerates a constant rate of honest-device faults. With polylogarithmically many qubits of adaptive leakage between the laboratories and arbitrary joint measurements, it tolerates an inverse-polylogarithmic rate. Each elementary DI call uses a fresh, isolated batch of polylogarithmically many device coordinates, and total device use in the compiled OT protocol is polynomial. The commitment has efficient simulators against both parties and yields DI coin tossing with abort. Because OT is complete for secure computation, the construction yields a DI protocol, with abort, for every efficiently computable classical functionality on a fixed number of parties, secure against static corruption of any proper subset of them. The commitment&#x27;s extractor changes a public parity relation through classical equivocation and leaves the device execution, hence its leakage, unchanged. A commit-and-prove functionality, disjoint audits, and an affine consistency check link the certified correlations to ideal OT. Sender security rests on a selector-aware parallel-repetition bound for the Magic Square game, which we derive from the two-round threshold theorem of Kundu and Tan.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **Pseudorandom Correlation Generators for Matrix Triples**
  2026-10-01 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2298)
  Maxime Bombar, Geoffroy Couteau, Nikolas Melissaris, Anuja Modi

  <details><summary>摘要 / Abstract</summary>

  We introduce new pseudorandom correlation generators (PCGs) for matrix triples: shares of triples $(A,B,A\cdot B)$ where $A,B$ are random matrices over $\mathbb{F}^{n\times n}$ for a field $\mathbb{F}$ and an integer $n$. Matrix triples are consumed in a wide variety of secure computation protocols that involve matrix arithmetic, which occurs commonly in settings such as privacy-preserving machine-learning and statistics, threshold cryptography, secure linear algebra, and more. Previous PCGs for matrix triples are inefficient: their seed grows at least linearly in the matrix dimension, and their expansion is slow. In this work, we introduce two new PCGs with improved performances: 1. Our first construction, inspired by the recent work of (Gentry and Lee, Crypto 2026) on FHE for matrix arithmetic, relies on the quasi-abelian syndrome decoding (QASD) assumption introduced in (Bombar et al., Crypto 2023), an assumption which has since received a significant amount of attention. Our PCG generates $N$ matrix triples over $\mathbb{F}^{n\times n}$ from a seed of size $poly(\lambda,\log n,\log N)$ using $\Theta(n^3\log(n^3N))$ field operations per triple, removing the linear dependency on $n$ from the seed compared to previous works. 2. Our second construction is more mathematically involved, and builds upon an elegant and surprising connection with the Weyl-Pauli twisted algebra, a mathematical structure originally studied in (Weyl, Zeitschrift für Physik, 1927) in the context of quantum kinematics. Our PCG relies on a new variant of the QASD assumption over the Weyl-Pauli twisted group algebra and exhibits impressive performances: it has the same seed size as our first construction and generates $N$ matrix triples at a cost only a small constant time larger than the cost of computing $N$ matrix triples in the clear. We complement our results with an in-depth study of our new twisted QASD assumption and demonstrate the benefits of our PCGs in concrete applications such as privacy-preserving machine learning and threshold MAYO.

  匹配依据：MPC: secure computation

  </details>

- **Non-Interactive Black-Box Witness-Indistinguishable Commit-and-Prove via Targeted Hitting-Set Generators**
  2026-10-01 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2286)
  Susumu Kiyoshima

  <details><summary>摘要 / Abstract</summary>

  Targeted hitting-set generators (HSGs) are primitives that have recently attracted attention in the study of pseudorandomness and derandomization. Recent works have shown that sufficiently strong targeted HSGs can be used to soundly instantiate the Fiat--Shamir transformation, yielding non-interactive protocols against uniform PPT adversaries in the plain model (i.e., without any setup phase for selecting a cryptographic hash function). In particular, Chen et al. (STOC 2025) combined this paradigm with the MPC-in-the-head technique to construct a non-interactive witness-indistinguishable argument for NP from a non-interactive commitment scheme and a targeted HSG. Inspired by these results, we explore other cryptographic applications of this paradigm. Our main result is a black-box construction of a non-interactive witness-indistinguishable commit-and-prove scheme against uniform PPT adversaries in the plain model. Following Chen et al., we obtain our construction by combining the MPC-in-the-head technique with the targeted-HSG-based Fiat--Shamir paradigm. The construction relies on an injective one-way function with efficiently recognizable range and a sufficiently strong targeted HSG. The latter is the same targeted HSG used by Chen et al. and can be instantiated under a very strong but plausible complexity-theoretic assumption.

  匹配依据：MPC: mpc (context)

  </details>

- **Kettle: Short Post-Quantum Threshold Signatures from the HAWK Signature Scheme**
  2026-10-01 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2288)
  Calvin Abou Haidar, Daniel Escudero, Thomas Espitau, Clément Hoffmann, Kaoru Takemure, Mehdi Tibouchi, Hernán Darío Vanegas Madrigal

  <details><summary>摘要 / Abstract</summary>

  HAWK is a lattice-based hash-and-sign signature scheme that was a third round candidate in the NIST additional call for post-quantum signatures. It has short signatures and keys, as well as fast and portable signing and verification. However, in response to a highly-publicized AI-driven cryptanalytic result that reduced its security (roughly doubling the required dimension to achieve a given security level), the authors de- cided to withdraw from the competition. The need to increase parameters was seen as limiting the size advantage of HAWK compared to the already selected lattice schemes ML-DSA and Falcon, which was one of its primary selling points along- side speed and the lack of floating-point arithmetic. In this paper, we identify another attractive aspect of the HAWK design that is not affected by the AI attack and has been overlooked so far: its surprising friendliness to multi- party computation (MPC). Indeed, HAWK signing can be achieved in a generic way from a small collection of basic composable MPC functionalities (like integer multiplication, uniform random generation, etc.) in such a way that instanti- ating those functionalities using MPC protocols with given security properties (semi-honest vs. malicious, honest vs. dis- honest majority, etc.) yields a secure protocol for MPC signing with those same properties. As a result, we obtain Kettle, a UC-secure threshold signa- ture protocol that outputs specification-compliant HAWK sig- natures and scales to an arbitrary number of parties. It offers essentially the shortest signature size so far for a lattice-based threshold signature, while achieving significantly lower round complexity and online communication cost than other thresh- old protocols built from pre-existing, non-threshold lattice- based signatures (like ML-DSA and Falcon): as low as 2 online rounds (a dozen rounds total) and 2 kB online com- munication per party, depending on the specific setting and optimization choices. We also provide a proof-of-concept implementation of our approach in the MP-SPDZ framework, which can be instanti- ated with any number of parties, any threshold, and a variety of security properties.

  匹配依据：MPC: multi party computation

  </details>

- **Homomorphic Advantage Operator: Stabilizing Reinforcement Learning Under Fully Homomorphic Encryption Constraints**
  2026-10-01 · MPC · [arXiv](https://arxiv.org/abs/2610.02074)
  Abid Mohamed Nadhir, Ahmad Al Hanbali, Beggas Mounir

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving machine learning presents significant deployment challenges on the cloud for intelligent systems with confidential data. Fully Homomorphic Encryption (FHE) offers a compelling solution for secure computation, preserving data confidentiality of cloud computations. However, applying FHE to reinforcement learning (RL) requires replacing non-linear operations with polynomial approximations, which diverge catastrophically due to a unique recursive error phenomenon known as the Bellman drift. This article introduces the Homomorphic Advantage Operator (HAO), a stabilization framework designed to prevent polynomial approximation divergence in FHE-based deep RL. HAO adapts the zero-mean centering projection from advantage-based value estimation directly to temporal-difference (TD) targets. This linear projection annihilates the uniform state-value baseline that drives the Bellman drift, maintaining per-state action rankings while requiring zero additional non-linear multiplicative depth and avoiding expensive ciphertext bootstrapping. The proposed HAO framework was evaluated using a three-tier experimental methodology, including a tabular Markov Decision Process (MDP), an encrypted CartPole environment using real CKKS cryptographic operations, and a 20-node logistics routing benchmark with dense continuous features. The results demonstrate that the proposed HAO strictly bounds network pre-activations within the safe polynomial approximation domain. The proposed HAO RL agents achieved 0% boundary breaches across all random seeds used, whereas regularization alone (L2 weight decay and gradient clipping) breached the bound on 3 of 5 seeds and the unstabilized baseline did so in 83.8% of episodes. Finally, HAO agents improve optimal policy accuracy by 18.0 percentage points in tabular domains and remain stable when DP-SGD-style Gaussian noise is added to the clipped gradients.

  匹配依据：MPC: secure computation

  </details>

- **DuraShare: BIP39-native secret sharing with full manual fallback**
  2026-10-01 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2300)
  Jeroen van de Graaf, Renato Schiavinato Lopez

  <details><summary>摘要 / Abstract</summary>

  BIP39 is a Bitcoin standard that turns a wallet&#x27;s random seed of size between 128 and 256 bits into a human-readable sequence of 12 to 24 words, taken from a fixed 2048-word list. Each word corresponds to an index in that list. DuraShare allows the holder of this sequence to split it among $n$ Sharekeepers, each of whom receives one share. Any subset of $k$ Sharekeepers can combine their shares and reconstruct the original sequence, whereas $k-1$ colluding Sharekeepers obtain no (Shannon) information. For everyday convenience we adopt a software-assisted model, while ensuring that a full manual fallback remains feasible for recovery, requiring nothing beyond paper, a calculator, and specific instructions. This matters because Sharekeepers may be family members or lawyers unfamiliar with crypto-technology, called upon only decades later, when no specific vendor, software, or hardware can be assumed to still exist. DuraShare combines three existing, well-established cryptographic techniques: (1) Shamir Secret Sharing over $\mathbb{F}_{2053}$, the smallest prime larger than 2048; (2) 2D error detection, applying row and column checksums to each share to protect the data against transcription errors and physical damage; and (3) a simple affine inner-product MAC over $\mathbb{F}_{2053}$ to authenticate each share, preventing a Sharekeeper from tampering without being detected.

  匹配依据：MPC: secret sharing

  </details>

- **Deniable Secret Sharing: Towards Practical Faking**
  2026-10-01 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2294)
  Ignacio Amores, Tamar Ben David, Matteo Campanelli, Sebastian Kolby, Eran Omri, Anat Paskin-Cherniavsky, Sophia Yakoubov

  <details><summary>摘要 / Abstract</summary>

  Deniable secret sharing (DSS; Canetti et al, TCC 2025) is designed for a scenario where an adversary is able to bribe or coerce all shareholders to divulge their shares of a secret. A deniable secret sharing scheme is equipped with a faking function that enables shareholders to produce fake shares that look like real shares, but do not actually reveal any additional information about the secret. Existing DSS constructions require the fakers to jointly compute on their shares, without considering how this computation might be realized. In this paper, we investigate two crucial properties of such computations: the extent to which the fakers themselves learn information about the secret (privacy against fakers), and the number of messages they need to exchange (message complexity). Message complexity can be seen as a measure of faking conspicuousness, if the adversary is able to observe network traffic. We prove that to obtain the strongest notion of DSS, any information-theoretic construction requires the fakers to exchange a non-zero number of messages, which could be large (depending on the access structure). We describe a general construction that matches this lower bound in many cases, e.g. for threshold access structures. Furthermore, for linear secret sharing schemes, we prove that certain unqualified sets must learn the secret as a result of faking. Moving to the computational setting, we describe two constructions which require no interaction beyond the knowledge of who the fakers are. This implies that both inconspicuousness and privacy against fakers are achieved. The first construction requires the share size to be exponential in the number of shareholders, but assumes only a PRG. The second construction has small shares, but assumes virtual black-box obfuscation. We see the latter construction as a stepping stone for a future iO-based instantiation. All of our lower bounds and constructions consider general access structures.

  匹配依据：MPC: secret sharing

  </details>

- **Randomized Early-Stopping Byzantine Agreement with Applications to Round-Efficient MPC**
  2026-09-30 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2284)
  Michele Ciampi, Pouyan Forghani, Yun Lu, Vassilis Zikas

  <details><summary>摘要 / Abstract</summary>

  We consider two main classes of synchronous round-efficient Byzantine Agreement (BA) protocols: \emph{expected constant rounds} and \emph{early-stopping}. Randomized protocols can terminate in expected constant rounds, and early-stopping protocols&#x27; worst-case round complexity depends on the actual number of corrupted parties $f\le t$, with $\min(t+1, f+2)$ being optimal. In this work, we combine the benefits of both classes, proposing a protocol that has constant round-complexity in expectation and $O(f)$ in the worst case. We present our protocol in the form of a compiler that can lift a broad class of expected-constant-round BA protocols, including Feldman--Micali and Katz--Koo, to {\em also} achieve near-optimal $O(f)$ worst-case complexity. This yields the {\em first} treatment of perfectly secure BA protocols for $t&lt;n/3$ that is both expected constant-round and near-optimal ($O(f)$) early stopping. Assuming a PKI, we show a variant of the compiler with a better round complexity, tolerating $t&lt;n/2$ corruptions. We also extend our results to parallel broadcast, also known as interactive consistency (IC). We give a compiler that runs $N$ Byzantine agreement instances in parallel while preserving both guarantees, expected constant rounds and $O(f)$ rounds in the worst case. Parallel broadcast then follows with one extra round for $t&lt;n/2$. To the best of our knowledge, this is the first compiler of its kind, and the first IC protocol with such expected and worse round-complexity. Finally, by combining our protocol with standard (fast) sequential composition techniques, we obtain a valid candidate to execute \emph{multi-party computation protocols} that require broadcast as their hybrid. By running existing MPC constructions using our broadcast protocol, we obtain the first MPC protocol that requires constant rounds of P2P communication in expectation and $O(f)$ rounds in the worst case.

  匹配依据：MPC: multi party computation

  </details>

- **Quantum Secret Sharing and Error Correction vs No-Cloning**
  2026-09-30 · MPC · [arXiv](https://arxiv.org/abs/2610.00441)
  Steven Chien, Ishani Mukherjee, Mark Zhandry

  <details><summary>摘要 / Abstract</summary>

  Secret sharing is ubiquitous throughout cryptography. All possible access structures are classically feasible, and in the case of threshold access structures, the protocols are even very efficient. However, when moving to the quantum setting, the no-cloning theorem shows that many access structures are impossible. In fact, no-cloning exactly characterizes feasibility: for thresholds, quantum secret sharing is possible if and only if the threshold $t$ is strictly more than $n/2$. In this work, we propose a variant of quantum secret sharing (QSS) where two or more identical copies of the input state are provided, but the output is only required to recover one copy. This notion circumvents the simple one-copy no-cloning obstruction, though the natural $k$-copy generalization still gives much milder obstructions. For thresholds using $k$ copies, no-cloning implies that QSS is impossible whenever $t\leq n/(k+1)$. It is tempting to hypothesize that no-cloning continues to exactly characterize the many-copy case. However, we show that this is not the case. We give positive results showing that multiple copies allow for going slightly beyond the single-copy obstruction: for thresholds, we construct QSS whenever $t&gt;(n-k+1)/2$. On the other hand, we give a novel obstruction we call the Clique Path obstruction, which applies to arbitrary access structures. For thresholds, it shows that QSS is impossible whenever $t\leq (n-1)/k$. Our upper and lower bounds exactly match for $k=2$. Both our results leverage connections to the $k$-colorability of certain graphs derived from the access structure. We leave closing the gap for $k\geq 3$ copies as a fascinating direction for future work. Secret sharing is closely related to error correction, which can also be considered in the many-copy setting. Our results imply similar obstructions for quantum error correction for erasure channels.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy Foundations for Multi-Institutional Scientific Artificial Intelligence**
  2026-09-30 · MPC · [arXiv](https://arxiv.org/abs/2609.39787)
  Olivera Kotevska, Sumit Jha, Aur'elien Bellet, Rui Hu, Nathaniel D. Bastian, Rafael Ferreira da Silva, Ravi Madduri, Kibaek Kim

  <details><summary>摘要 / Abstract</summary>

  Scientific artificial intelligence (AI), spanning foundation models (FMs) to federated data-analysis pipelines, is becoming shared infrastructure across national laboratories, universities, hospitals, and industrial partners. This collaboration creates privacy risks whose natural unit is often an institution&#x27;s participation, research strategy, or technical capability rather than a single record. Differential privacy (DP), federated learning (FL), secure computation, trusted execution, and provenance each protect parts of the stack, but their guarantees rarely compose across mixed-trust institutions, access tiers, and autonomous agents. This perspective recasts privacy for scientific AI as an assurance problem defined by six elements: protected asset, observer, channel, permitted disclosure, guarantee, and evidence. We demonstrate the framing through a claim register for a composite cross-institutional scenario and use it to assess the model lifecycle. Two of the resulting gaps are specific to leadership-class facilities: scheduler, allocation, and telemetry metadata expose an institution&#x27;s resource posture, and instrument-attached control loops leak research strategy through timing and contention on shared accelerators. We identify six research priorities: institution-level guarantees, agent-communication privacy, cross-tier information flow, privacy-compatible reproducibility, leadership-scale accounting, and instrument side channels. The contribution is a common form for stating, comparing, and auditing claims whose guarantees otherwise remain fragmented across the scientific AI stack.

  匹配依据：MPC: secure computation

  </details>

- **Natural Barriers to Quantum Extraction: On the Post-Quantum (In)security of (O)EKE and Masny-Rindal OT**
  2026-09-30 · MPC · [arXiv](https://arxiv.org/abs/2609.39844) · [IACR ePrint](https://eprint.iacr.org/2026/2280)
  James Bartusek, Jake Januzelli

  <details><summary>摘要 / Abstract</summary>

  Encrypted key exchange (EKE), introduced by Bellovin and Merritt (IEEE S\&amp;P 1992), and Masny-Rindal OT, introduced by Masny and Rindal (ACM CCS 2019), are highly-efficient methods for compiling essentially any KEM into advanced cryptographic protocols, namely password-authenticated key exchange (PAKE) and oblivious transfer (OT), by relying only on idealized symmetric-key primitives. They have become leading candidates for practically-implementable PAKE and OT due to (1) their simplicity, (2) their plug-and-play nature, allowing for flexibility in the choice of KEM, and (3) existing proofs of UC-security (in the classical adversarial model). Due to point (2) above, these compilers yield attractive candidates for efficient post-quantum PAKE and OT, especially given the recent post-quantum KEM standardization efforts. This motivates the question of whether the (UC-)security of these compilers translates to the quantum adversarial model. In this work, we show that it does not. In particular, we prove that a general family of (O)EKE protocols, as well as Masny-Rindal OT, are not UC-secure against quantum polynomial-time adversaries, even when instantiated with a post-quantum KEM. To establish UC-insecurity, we devise an adversarial strategy that provably thwarts any attempt by the simulator to extract its input (the password in the case of PAKE, and the receiver&#x27;s choice bit in the case of OT). These are the first naturally-occurring/non-contrived cryptographic protocols that are known to be secure in the (classical) ROM but provably insecure in the QROM. To complement these negative results, we establish that both compilers yield certain notions of game-based security. In the PAKE setting, we consider OEKE instantiated with the ``2-Feistel&#x27;&#x27; cipher, and prove its stand-alone game-based security in the quantum random oracle model. We view these results as a proof of concept that security of (O)EKE and Masny-Rindal OT can yet be redeemed in the quantum setting, though we caution that the situation will be more subtle than in the classical setting due to the breakdown of simulation-based security. Along the way, we establish a novel ``advantage-tight&#x27;&#x27; one-way to hiding lemma that may be of independent interest.

  匹配依据：MPC: oblivious transfer

  </details>

- **Quantum Secure Non-Interactive Reductions**
  2026-09-29 · MPC · [arXiv](https://arxiv.org/abs/2609.38452)
  Maxwell Gold, Sarah Hagen, Daniel Alabi, Eric Chitambar

  <details><summary>摘要 / Abstract</summary>

  Efficient models for secure computation often rely on offline preprocessed correlations, which subsequently enable private online computation from minimal assumptions. Within these models, the study of secure non-interactive reductions (SNIR) formalizes when one classical correlation can be non-interactively transformed into another, while guaranteeing information-theoretic simulation-based privacy. In this work, we introduce quantum secure non-interactive reductions (QSNIR), a natural extension of SNIR, in which the source and target resource are each a bipartite quantum state. Specifically, when the target resource is classical, our framework enables us to analyze the problem of disseminating private correlations from entanglement, in addition to classical resources. Our primary technical result is that QSNIR privacy in this context can be computed exactly via a semidefinite program (SDP) pair that quantifies an error operationally rooted in a simulation-based cheating advantage. We prove that QSNIR privacy is lower-bounded by a decision problem related to minimum-error state discrimination (MED), and use both definitions to compute exact one-shot privacy errors for universal two-party computation (2PC) preprocessing correlations.

  匹配依据：MPC: secure computation, two party computation

  </details>

- **Quantum Leakage Resilience of Shamir Secret Sharing**
  2026-09-29 · MPC · [arXiv](https://arxiv.org/abs/2609.37276)
  Rishabh Batra, Fuyuki Kitagawa, Ryo Nishimaki, Takashi Yamakawa

  <details><summary>摘要 / Abstract</summary>

  We initiate the study of quantum leakage resilience of unmodified Shamir secret sharing over prime fields. A well-studied leakage model for Shamir&#x27;s secret sharing classically is single-bit local leakage from each share. We consider its quantum analogue where, for each party, a local leakage channel takes as input the party&#x27;s share and outputs a leaked qubit. Without preshared entanglement, we show that the distinguishing advantage is $2^{-Ω(n)}$ when the threshold rate $t/n=τ$ exceeds $τ_\star\approx0.73339$ by a fixed positive margin. More generally, we allow disjoint entangled blocks of any fixed maximum size where there is no entanglement between different blocks or with the adversary, and each block emits at most a fixed number of qubits. Security holds when the threshold rate is high enough (sufficiently close to one). We then allow a specified set of devices to share entanglement with the adversary. We show that security holds even when a linear number of devices ($αn$ for small $α&gt;0$) share entanglement with each other and with the adversary for a large enough threshold rate. As a complementary negative result, we also show that even classical single-bit leakage makes Shamir scheme insecure if we allow arbitrarily large entanglement between the leakage devices. A GHZ state shared by exactly $t$ leakage devices makes even classical one-bit leakage insecure, without any entanglement with the adversary. In this attack, each participating device emits only one classical bit, and their joint parity distinguishes any chosen pair of secrets with a constant advantage. Thus, for fixed threshold rates above $τ_\star$, the maximum number of devices that may share arbitrary entanglement with one another and with the adversary while preserving security is linear in $n$ up to constant factors, although the optimal support fraction remains open.

  匹配依据：MPC: secret sharing

  </details>

- **PQMZ: Formally Verified Falcon-PKR for Post-Quantum Cryptographic Migration in Zcash**
  2026-09-29 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2260)
  Hannes Hacker, Shekoufeh Neisarian, Sara Zain, Elif Bilge Kavun

  <details><summary>摘要 / Abstract</summary>

  Migrating blockchain systems to Post-Quantum Cryptography (PQC) requires not only replacing classical primitives, but also analysing transformations that change how signatures are represented and verified. We study Falcon-PKR, a public-key-recovery variant of Falcon, motivated by Zcash-like transparent transaction workflows. Falcon-PKR replaces explicit storage of the full Falcon public key with a compact stored digest and reconstructs a candidate public key from the signature during verification. In our construction, this reduces the combined representation size of public key and signature by approximately 15%, but it also introduces a distinct security case in which verification depends on a reconstructed key derived from adversarially supplied signature data. We address this with a machine-checked EasyCrypt formalisation in the Random Oracle Model (ROM). We mechanically verify an EUF-CMA reduction showing that the security of Falcon-PKR is bounded by the security of standard Falcon together with collision resistance of a domain-separated public-key hash. The analysis therefore treats both assumptions explicitly and does not claim a proof of Falcon itself. We also machine-check correctness for honest signing under an abstract Falcon signing interface. We implement Falcon-PKR for Falcon-512 and Falcon-1024 in Python and C, and evaluate runtime and size against ECDSA and selected Post-Quantum (PQ) alternatives, exposing explicit verification and storage trade-offs. As a complementary case study, we implement and analyse an extended SECUER-based Multi-Party Computation (MPC) ceremony architecture. Together, the two case studies address both transaction-signature and ceremony-infrastructure layers of PQ blockchain migration.

  匹配依据：MPC: multi party computation

  </details>

- **OPFL: Optimistic Verification of Federated Learning via Empirical Boundary**
  2026-09-29 · MPC · [arXiv](https://arxiv.org/abs/2609.37011)
  Hongxu Su, Jianzhu Yao, Xuechao Wang, Pramod Viswanath

  <details><summary>摘要 / Abstract</summary>

  Federated learning enables multiple clients to collaboratively train models without sharing their private data. However, the lack of visibility into local training makes it difficult to verify whether clients follow the prescribed training procedure or submit malicious updates, such as model poisoning. A natural approach is to replay client training for verification. However, privacy-preserving replay produces numerical results that cannot be directly matched with local client execution because the two run in different environments. We present OPFL, an optimistic verification framework for privacy-preserving federated learning. To protect data privacy, OPFL performs replay inside secure multi-party computation (MPC). Although gradients computed on MPC and local GPUs are not bitwise identical, we observe that their absolute differences are stable and bounded. OPFL therefore calibrates an empirical boundary offline and uses it to distinguish benign numerical deviations from malicious manipulation. To reduce the cost of expensive MPC replay, OPFL adopts optimistic verification by post auditing only sampled training steps. Experiments on LeNet, BERT, and Qwen show that the boundary generalizes across datasets, input lengths, and GPUs, while achieving $0$\% ASR against model poisoning and PGD-based attacks. On a LeNet workload, at $p=0.01$, OPFL is approximately $98.6\times$ faster than full MPC-based FL and $625.5\times$ faster than ZK-based approach.

  匹配依据：MPC: secure multi party computation

  </details>

- **TPOKÉ: Threshold Public-Key Encryption from POKÉ via Isogeny Sharing**
  2026-09-28 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2243)
  Toshiki Takatera, Hiroshi Onuki, Tsuyoshi Takagi

  <details><summary>摘要 / Abstract</summary>

  POKÉ, introduced by Basso and Maino, is one of the most efficient isogeny-based public-key encryption schemes. The generic parallel-encryption approach yields a $(t,n)$-threshold variant by running $n$ independent POKÉ instances and secret-sharing the message, but this multiplies the public-key and ciphertext sizes by roughly $n$. We present S-TPOKÉ, a POKÉ-based $(t,n)$-threshold construction for every $1\le t\le n$, and Ch-TPOKÉ, an $(n,n)$ variant that arranges the parties&#x27; secret isogenies differently. Both schemes avoid repeating part of the isogeny computation that appears in every independent POKÉ instance. Compared with the trivial construction, they reduce the number of degree-$3^{b}$ isogenies computed during encryption from $2n$ to $n+1$ and reduce the ciphertext size by about a factor of two when $n$ is large. The two schemes differ in how the parties&#x27; secret isogenies are arranged. S-TPOKÉ is our main construction: the dealer samples $n$ independent secret isogenies, while encryption samples one sender-side secret isogeny and shares it across the parties. Ch-TPOKÉ instead arranges the parties&#x27; secret isogenies into a chain. For S-TPOKÉ, we prove SIM-CPA security under static corruption in the random oracle model from the $(k,n)$-S-C-POKE assumptions for all $1\le k\le t$, which extend C-POKE to the threshold setting. For Ch-TPOKÉ, we prove only SIM-CPA security under static maximal corruption from the $(j,n)$-Ch-D-POKE assumptions for all $j\in\{1,\ldots,n\}$, which extend D-POKE to a chain-based threshold setting. This guarantee is strictly weaker than SIM-CPA security under static corruption. We also give asymptotic parameter choices targeting $\lambda$-bit security and derive closed-form expressions for the public-key, ciphertext, and partial-decryption sizes in terms of $\lambda$ and $n$.

  匹配依据：MPC: secret sharing

  </details>

- **Batch Decryption from New Standard Assumptions**
  2026-09-28 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2252)
  Nico Döttling, Bernardo Magri, Benjamin Marsh, Mahesh Sreekumar Rajasree

  <details><summary>摘要 / Abstract</summary>

  Batch decryption allows an authority to release a short key that enables public decryption of a selected batch of ciphertexts. Motivated by encrypted mempools, we study this capability through two constructions with different authorization semantics and assumptions. First, we provide a simple and compact epochless construction in an RSA group based on Fiat&#x27;s Batch RSA [CRYPTO&#x27;89]. Its batch-decryption hint is just one group element, and its keys and ciphertexts have size independent of the batch size, with no batch bound fixed at setup. We prove adaptive security under the strong RSA assumption in the random-oracle model. The scheme permits repeated releases for overlapping batches, with each release authorizing decryption of the selected ciphertexts. Second, we give an adaptively secure generic construction of identity-based encryption with batch decryption in the epoch-based model, which permits at most one batch-key query for the challenge epoch. The construction combines deferred encryption via garbled circuits, non-inclusion secure registration-based encryption, and weak receiver non-committing IBE. We construct the latter primitive from ordinary IBE and pseudorandom functions, obtaining an instantiation of the epoch-based construction from the computational Diffie--Hellman assumption.

  匹配依据：MPC: garbled circuits

  </details>

- **Adaptively UC-Secure Oblivious Transfer from Group Actions**
  2026-09-28 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2251)
  Olivier Blazy, Céline Chevalier, Saqib Kakvi, Lola-Baie Mallordy

  <details><summary>摘要 / Abstract</summary>

  Oblivious Transfer (OT) is a fundamental building block for secure computation, in which a sender holds two messages and a receiver learns exactly one of them, without revealing which one was chosen and without learning the other. While generic constructions for Universally Composable (UC) OT exist, instantiating them from post-quantum assumptions remains challenging, particularly under adaptive corruption. In this work, we present the first adaptively UC-secure OT protocol based on Group Actions, specifically assuming weakly pseudorandom Effective Group Actions (EGA) like CSIDH. We adhere to the framework of [BC15], which derives an adaptively UC-secure OT protocol from SPHF-friendly extractable and equivocable (E²) commitment schemes. The central challenge in instantiating this construction from group actions is the lack of SPHF-friendly IND-CCA encryption. Classical CCA transformations such as Fujisaki-Okamoto destroy the algebraic structure required for building SPHFs over ciphertexts, while known group action-based schemes offer no native mechanism to prove ciphertext validity. To overcome this obstacle, we construct from group actions an IND-CCA encryption scheme with enough algebraic structure to efficiently recognize valid ciphertexts. Our contributions are threefold: (1) a verifiable chameleon hash function with perfect soundness in the standard model, (2) an SPHF-friendly, publicly verifiable IND-CCA encryption scheme in the random oracle model, and (3) we combine these to build an SPHF-friendly E² commitment scheme and derive a fully adaptively secure OT protocol in the UC framework. This is the first construction of its kind under group action assumptions, enabling post-quantum secure OT with adaptive security guarantees. These building blocks may also be of independent interest e.g., to obtain digital signatures, non-malleable commitment schemes, or verifiable encryption.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **Incrementally Verifiable Computation without Extraction**
  2026-09-25 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2219)
  Abhishek Jain, Surya Mathialagan, Brent Waters

  <details><summary>摘要 / Abstract</summary>

  Incrementally verifiable computation (IVC) [Valiant, TCC &#x27;08] allows one to iteratively prove that a configuration $x_0$ reaches a configuration $x_T$ via $T$ repeated applications of a (possibly non-deterministic) machine $\mathcal{M}$. An IVC scheme is fully succinct if the proof size is independent of both $T$ and the size of the intermediate configurations. In this work, we develop a new indistinguishability obfuscation ($i\mathcal{O}$)-based approach to IVC that avoids the extraction-based security analyses central to prior constructions. Assuming subexponential hardness of $i\mathcal{O}$ and one-way functions, we construct an adaptively sound fully succinct IVC scheme for deterministic computations. This yields the first IVC for deterministic computations that does not rely on algebraic assumptions. Under the same assumptions, we further obtain a fully succinct two-hop IVC scheme for $\mathsf{NP}$ with non-adaptive soundness, allowing one to prove that $x_0$ reaches $x_2$ via an intermediate configuration $x_1$. This is the first IVC scheme for $\mathsf{NP}$ achieving full succinctness. Our constructions are based on a new connection between IVC and secret sharing for $s$-$t$ connectivity in graphs.

  匹配依据：MPC: secret sharing

  </details>

- **Fully Anonymous Perfect Threshold Secret Sharing: Explicit One-Bit Construction and Rate Amplification**
  2026-09-24 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2202)
  Chongxu Ren, Hongbo Yu

  <details><summary>摘要 / Abstract</summary>

  Secret sharing distributes a secret among participants so that only sufficiently large groups can recover it. Fully anonymous secret sharing also allows recovery from share values alone, without participant identities. Below the reconstruction threshold, the shares must look exactly like independent uniform random values, revealing neither the secret nor their holders&#x27; identities. Con, Li, and Mazor established that such schemes with error-free recovery exist for every threshold, leaving an efficient general construction open. We give efficient constructions for every threshold 2 ≤ t ≤ n among n participants. For an L-bit secret, each share has L + O(t² log² n) bits. Sharing runs in expected polynomial time, and reconstruction runs in deterministic polynomial time. Our approach combines an efficient one-bit construction with a general transformation that uses it to protect a short message needed for anonymous reconstruction of a long secret. The additional share length has an upper bound depending only on the number of participants and the threshold. For a fixed participant count and threshold, the rate approaches one as secrets grow longer, while anonymity remains exact and recovery never errs.

  匹配依据：MPC: secret sharing

  </details>

- **Argo: Leaking a Secret from an Invalid Groth16 Proof**
  2026-09-23 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2165)
  Liam Eagen, Ying Tong Lai

  <details><summary>摘要 / Abstract</summary>

  We present Argo, a randomized encoding scheme for the invalidity of pairing-based SNARKs like Groth16. Argo allows an encoder to encode a proof such that a decoder can derive a secret if the proof is invalid. We prove the selective security of invalidity Argo, as well as the adaptive security of validity Argo, under DDH in one source group of a bilinear pairing in the standard model, a standard assumption that holds in the generic group model used to analyze Groth16. We show how to couple invalidity Argo with a projective garbling scheme like Argo MAC or Duty-Free Bits to construct a garbled circuit for Groth16 invalidity as a function of the proof bits, and how to use it with BitVM to construct a permissionless, optimistic Groth16 verifier for Bitcoin: a decoder proves a proof invalid by publishing a secret, and the decoder can be anyone, not necessarily known in advance. When instantiated with BN254, Argo has an offline encoding size of about 21 kB, a thousand times smaller than the projective garbling scheme, and an end-to-end protocol size more than three orders of magnitude smaller than existing Yao-based approaches. Generating an Argo + Argo MAC garbled circuit takes tens of milliseconds on a laptop, compared to minutes for a Yao GC. Argo is the first protocol that makes permissionless, optimistic SNARK verification on Bitcoin practical.

  匹配依据：MPC: garbled circuit, garbling scheme

  </details>

- **Fully Anonymous Perfect Secret-Sharing**
  2026-09-22 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2145)
  Roni Con, Ray Li, Noam Mazor

  <details><summary>摘要 / Abstract</summary>

  Fully anonymous secret-sharing schemes ensure two properties at once: for any fixed secret, the combined shares of every unauthorized set of participants are uniformly random, and every authorized set can reconstruct the secret exactly using only the share values, without needing to know which participant holds which share or in what order the shares appear. It was previously open whether such schemes exist for nontrivial exact-threshold parameters 2 &lt; t &lt; n. For the smallest previously open threshold, t= 3, we give, for every n≥4, an explicit fully anonymous scheme for one-bit secrets, with 2⌈log n⌉-bit shares and a perfect reconstruction algorithm running in poly(log n) time. The next result, found by ChatGPT, shows that for every 1 ≤t ≤n there exists a fully anonymous perfect (t,n) threshold secret-sharing scheme for one-bit secrets, in which each share has length O(tlog n) bits. The proof is purely existential and does not provide an efficient construction. Moreover, ChatGPT identified a simple construction of a fully anonymous perfect scheme for every access structure A; if A contains ℓ authorized sets, then each share consists of ℓ2 bits. The authors subsequently verified and streamlined the proofs on their own and take full responsibility for their correctness.

  匹配依据：MPC: secret sharing

  </details>

- **Weighted Batch Threshold Encryption with Efficient DKG**
  2026-09-15 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2053)
  Alexander Frolov, Aditi Partap, Max Resnick, Ertem Nusret Tas

  <details><summary>摘要 / Abstract</summary>

  Batch threshold encryption allows a committee to decrypt a selected batch of ciphertexts using one short pre-decryption key per party, while ciphertexts outside the batch remain private. This makes batch threshold encryption attractive for building encrypted mempools for blockchains, where validators reveal transactions selected for a block while pending transactions remain private. However, in proof-of-stake systems like Solana or Ethereum, authorization depends on each validator&#x27;s stake, which motivates a weighted version of batch threshold encryption. Naive approaches to weighting existing batch threshold encryption schemes lead to communication costs proportional to the weight assigned to each party. Existing schemes that avoid this cost either associate every ciphertext with a batch label or an encryption-time index. We present the first weighted batch threshold encryption schemes that require neither batch/epoch labels nor encryption-time ciphertext indices, while keeping each party&#x27;s communication independent of its weight. We obtain two constructions by virtualizing prior schemes: the BTX construction of Agarwal et al. and the partial-fraction construction of Boneh et al. In both schemes&#x27; decryption procedures, each party communicates a single group element for an entire batch, regardless of its assigned weight. We prove correctness, robustness, and security under weighted variants of the original schemes&#x27; assumptions, and analyze the assumptions in generic bilinear groups. For the BTX-based construction, we also give a specialized distributed key generation protocol that avoids the general purpose MPC-based setup required by the previous state-of-the-art schemes. Finally, we implement our schemes to demonstrate their practical performance at parameter sizes relevant to blockchains.

  匹配依据：MPC: mpc (context)

  </details>

- **It's Not Just a Phase: Understanding Function Dependence in MPC Preprocessing (Extended Version)**
  2026-09-14 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/2029)
  Andreas Brüggemann, Kasra Edalatnejad, Jan Filipp, Philipp Kusterer, Thomas Schneider

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) is a key enabling technology for privacy-preserving applications. To achieve low latency after inputs are provided, many efficient protocols utilize preprocessing, and the landscape of preprocessing approaches is growing and diverse. Some recent works use variants of function-dependent preprocessing, leveraging additional knowledge on the function to be computed for even better performance. While the existing literature primarily focuses on performance, it is mostly overlooked that there exist different kinds of function dependence and what practical implications they have. We systematize the different flavors of function dependence, relating them to practical requirements beyond efficiency.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Spruce: Scalable Private Outsourced Retrieval Using Compact Embeddings**
  2026-09-03 · MPC · [arXiv](https://arxiv.org/abs/2609.03376)
  Peichun Hua, Yunming Xiao

  <details><summary>摘要 / Abstract</summary>

  Retrieval-Augmented Generation (RAG) has made dense retrieval over large document collections a standard building block. Organizations increasingly outsource vector indexes to untrusted clouds, exposing proprietary corpora and user queries. Cryptographic protection is challenging because each query searches corpus-scale state, causing computation, correlated randomness, and communication to grow with the corpus. At million-document scale, a naive secure implementation takes minutes and about 90 GB of communication per query. Even recent optimized systems require 10--22 seconds. We propose Spruce (Scalable Private Outsourced Retrieval Using Compact Embeddings), which co-designs representations with the cryptographic protocol. Spruce learns compact binary codes that preserve candidates for full-precision reranking, replacing corpus-wide embedding scoring with efficient Hamming-distance computation under two-server multi-party computation (MPC). A corpus-calibrated fixed-radius protocol avoids multi-round candidate selection while preserving retrieval quality. Spruce also provides private cluster pruning, which trades minor quality loss for substantially less computation, and a one-core owner-operated dealer that removes cloud OT preprocessing bottlenecks. Across four corpora containing 383K--5.42M documents, Spruce preserves the original search quality with median candidate sets of only 382--1,952. At 10 Gbps inter-server bandwidth, full scans take 0.21--2.97 seconds, $4.8$--$6.7\times$ faster than the closest measured prior work. Private pruning takes 0.06--1.09 seconds, achieves $13.1$--$22.9\times$ speedups, and retains $93.9\%$--$97.3\%$ of full-float NDCG. On the largest corpus, pruning and the dealer jointly improve sustained throughput by $31.5\times$ at 1 Gbps per link.

  匹配依据：MPC: multi party computation

  </details>

- **Card-Based Computation in the Virtual Player Simulation Model**
  2026-09-02 · MPC · [arXiv](https://arxiv.org/abs/2609.02716)
  Suthee Ruangwises

  <details><summary>摘要 / Abstract</summary>

  Player simulation has recently emerged as a new direction in card-based cryptography, with protocols developed for simulating virtual players in physical card games such as Old Maid, UNO, and President. Unlike conventional card-based secure computation, player simulation imposes additional constraints: the cards represent a persistent game state, the remaining cards in a virtual player&#x27;s hand must be preserved after each action, and it is desirable to represent each card in the game by a single physical card. In this paper, we study generic card-based computation in the virtual player simulation model. We focus on games whose cards admit a publicly known ranking and propose two fundamental protocols. First, we present the Play-Minimum protocol, which securely selects and plays the minimum-value card from a virtual player&#x27;s hand when all cards in the deck have distinct values. By symmetry, the protocol can also be used to play the maximum-value card. Second, we present the Sorting protocol, which securely arranges a virtual player&#x27;s hand in nondecreasing order and remains applicable when multiple cards have the same value. These protocols provide generic computational primitives independent of any particular card game and constitute a step toward understanding the computational capabilities of the virtual player simulation model.

  匹配依据：MPC: secure computation

  </details>

- **Fully-Succinct Multi-Key FHE &amp; Rate-1 Simulatable Threshold Decryption from LWE**
  2026-08-13 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/1683)
  Abtin Afshar, Rishab Goyal

  <details><summary>摘要 / Abstract</summary>

  We construct the first multi-key fully homomorphic encryption (MKFHE) scheme where the ciphertext size, public key size, and secret key size remain independent of the number of users, $N$. Our construction is leveled and relies on the standard Learning with Errors (LWE) assumption. All prior MKFHE schemes incur at least linear growth in ciphertext size with the number of users ($|\mathsf{ct}| \propto N$), a limitation that has persisted across more than a decade of research. Our results provide the first evidence that MKFHE with constant ciphertext size is achievable under standard assumptions and paves the way for many interesting applications. We also describe a single-round distributed decryption protocol for multi-key ciphertexts in our fully-succinct MKFHE scheme. More remarkably, we show that our MKFHE scheme simultaneously satisfies the following properties: (1) the size of each user&#x27;s partial decryption share is identically equal to the plaintext length (i.e., partial decryption shares are truly rate-1), and (2) an honest user&#x27;s partial decryption can be simulated. To the best of our knowledge prior to this work, we did not have any MKFHE with one-round distributed decryption from standard assumptions that simultaneously satisfied both these properties. We show that our MKFHE is significantly useful in designing various forms of multi-party computation (MPC) protocols with asymptotically optimal communication complexity.

  匹配依据：MPC: multi party computation

  </details>

- **Silent Distributed Cryptography for DNFs and Threshold Policies from Lattices**
  2026-07-29 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/1547)
  Abtin Afshar, Rishab Goyal, Saikumar Yadugiri

  <details><summary>摘要 / Abstract</summary>

  We study two central problems in threshold cryptography from lattices: (1) threshold encryption with silent setup for general thresholds $t \geq 2$, where no post-quantum constructions were previously known, and (2) threshold fully homomorphic encryption (TFHE) with sublinear parameters, an open problem since the work of [Boneh et al.; CRYPTO&#x27;18]. We introduce $\textit{$(\alpha,\beta)$-Scaled Linear Secret Sharing Schemes}$ (LSSS), a relaxation of standard LSSS in which each authorized set $S$ reconstructs a scaled version of the secret, $\gamma_S \cdot k$, where both the reconstruction coefficients and the set-dependent scaling factor $\gamma_S$ are bounded over the integers. Unlike prior approaches based on bit decomposition, this preserves the uniform distribution of unauthorized shares. Building on this, we obtain: 1. $\textbf{Silent Threshold and Distributed monotone-policy encryption.}$ We provide the first post-quantum construction supporting: (i) threshold policies with ciphertexts growing as $\tau^{16} \cdot \mathsf{poly}(\lambda, \log N)$, where $\tau = \min(t^2,N{-}t)$, and (ii) DNF formulas with fully compact parameters. Our constructions are proven secure under the decomposed LWE assumption in the random oracle model. If we additionally rely on a common reference string, then the ciphertext size for our threshold policy scheme can be reduced to $\tau^4 \cdot \mathsf{poly}(\lambda, \log N)$ under the Succinct LWE assumption. 2. $\textbf{Decentralized TFHE with silent setup.}$ We provide the first $\textit{decentralized}$ TFHE, for threshold policies and DNFs, from the decomposed LWE assumption. Our construction supports homomorphic evaluation of arbitrary circuits, one-round distributed decryption, and silent setup. This was left as an open problem by [Boneh et al.; CRYPTO&#x27;18] and, prior to this work, we did not have any non-trivial construction for decentralized TFHE from any assumption. 3. $\textbf{Sublinear centralized TFHE from LWE.}$ We also extend our techniques to $\textit{centralized}$ TFHE. We provide a TFHE scheme under the standard LWE assumption, where all parameters are simultaneously sublinear in $N$ for any threshold $t$ as long as $\min(t^2,N{-}t)=o(N^{1/6})$. This breaks the $\omega(N)$ barrier that has persisted in the TFHE literature since 2018.

  匹配依据：MPC: secret sharing

  </details>

- **Batched Oblivious Transfer with Square-Root Communication**
  2026-07-28 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/1541)
  Yicheng Li, Claudio Orlandi, Lawrence Roy, Yizhou Yao

  <details><summary>摘要 / Abstract</summary>

  Oblivious Transfer (OT) is a fundamental cryptographic primitive and a core building block for many multiparty cryptographic protocols. While existing OT extension techniques achieve excellent asymptotic efficiency for very large batches, their performance degrades when the total number of OTs is only moderate, since the cost of generating the required base OTs is no longer effectively amortized. In this work, we close this gap by presenting OT constructions that achieve square-root communication complexity for batched OT generation. Concretely, our most efficient protocol generates ell random OTs using O(lambda sqrt(ell)) bits of communication, where lambda is the security parameter. Our constructions are inspired by recent advances in homomorphic secret sharing and techniques for distributed discrete logarithm computation, and explore complementary points in the design space. The first construction is based on the Damgård-Jurik cryptosystem and standard assumptions, at the cost of a one-time trusted setup. The second eliminates the need for trusted setup, relying instead on a power-DDH assumption over prime-order groups. For 128-bit security, our schemes require approximately 2.6 KiB and 1.25 KiB of communication, respectively, to generate 128 random OTs, including the hash key in the power-DDH construction. Our best construction outperforms existing OT extension techniques for batch sizes of up to 32,768 OTs.

  匹配依据：MPC: oblivious transfer, secret sharing

  </details>

- **IBE and PIR from Isogenies**
  2026-07-17 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/1457)
  Shweta Agrawal, Andrea Basso, Sikhar Patranabis

  <details><summary>摘要 / Abstract</summary>

  We significantly expand the reach of isogeny-based cryptography by constructing, for the first time, two fundamental primitives that have long remained out of reach from isogenies: identity-based encryption (IBE) and semi-honest single-server private information retrieval (PIR) with communication polylogarithmic in the database size. Our IBE additionally achieves anonymity, which means that the ciphertexts hide both the message and the recipient identity. Our results are enabled by new techniques for constructing cryptographic primitives from structured isogeny computations, centered around the first construction of blind batch encryption from isogenies. To establish its security, we introduce a new hardness assumption, CDH with Mismatched Torsion (CDHwMT), which informally captures the hardness of a CDH-like problem in the presence of structured auxiliary isogeny information. We provide evidence for its plausibility by showing that, in the Algebraic Isogeny Model, CDHwMT reduces to well-studied isogeny assumptions. The same techniques yield further cryptographic applications: the first isogeny-based hierarchical IBE, laconic oblivious transfer, and public-key encryption simultaneously achieving high-rate leakage resilience and key-dependent-message/circular security. All of our constructions can be conjectured to be post-quantum secure. Beyond these individual primitives, our results demonstrate that isogenies can support substantially richer cryptographic functionality than previously known, and provide new tools toward building advanced post-quantum cryptography.

  匹配依据：MPC: oblivious transfer

  </details>

- **Combinatorial aspects of holographic quantum secret sharing**
  2026-07-17 · MPC · [arXiv](https://arxiv.org/abs/2607.16110)
  Ning Bao, Keiichiro Furuya, Jacob March

  <details><summary>摘要 / Abstract</summary>

  We introduce combinatorial holographic quantum secret sharing (CHQSS) for a bulk subregion in AdS$_3$/CFT$_2$ to study how logical information of the bulk subregion is encoded in the boundary and protected from erasures of boundary subregions. We introduce a distance, a reconstruction threshold, and a secret threshold to characterize CHQSS schemes. We present the phase transitions of multipartite entanglement wedges in a symmetric setup and observe multiple distinct phase transition points. The distance and thresholds depend on the holographic phase and the choice of bulk subregion. We derive the maximum distance. Moreover, we derive the relations between the distance and the thresholds. We construct a family of CHQSS schemes in the symmetric setting that includes perfect threshold CHQSS and perfect non-threshold CHQSS.

  匹配依据：MPC: secret sharing

  </details>

- **MPC with Weighted and Fluid Participation**
  2026-07-04 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/1375)
  Ghada Almashaqbeh, Sumedh Ghude

  <details><summary>摘要 / Abstract</summary>

  Most existing multiparty computation (MPC) protocols assume static and equal participation. All computing parties can dedicate resources and stay online for the entire computation, and they have equal influence on computation correctness and security (i.e., they are equally hard to corrupt). Supporting dynamic participation, so parties can join/leave at will, and associating weights to these parties reflecting their trust level, are essential to enable MPC in contemporary emerging applications. Existing solutions addressed these issues separately at varying security levels, and attempting to combine them while addressing malicious security raises several challenges and open questions. In this paper, we close this gap and develop maliciously-secure MPC protocols that support weighted participation in both static and dynamic (or fluid) settings. In particular, we extend prior work on weighted ramp secret sharing (WRSS) to support verifiability and proactivity, which could be of independent interest. Then, we show how to perform arithmetic operations over weighted shares in a verifiable way, thus enabling maliciously-secure weighted MPC with guaranteed output delivery under static participation. Utilizing the proactivity feature of our secret sharing scheme, we develop a state handover protocol and employ it to support dynamic participation in committee-based MPC with the same security guarantees. Both protocols are synchronous and assume honest majority. To the best of our knowledge, our work is the first to support both weighted and dynamic participation in MPC.

  匹配依据：MPC: multiparty computation, secret sharing

  </details>

- **On the generic structures of the protocols for quantum auction and quantum summation and their relation**
  2026-06-26 · MPC · [arXiv](https://arxiv.org/abs/2606.27693)
  Kabir Sandhu, Sandeep Mishra, Anirban Pathak

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (SMC) addresses the problem of jointly computing global functions of private inputs while revealing minimal information about individual data. Two prominent examples of SMC tasks are sealed-bid auction and secure multi-party summation. Existing schemes for quantum auction and quantum summation have largely been developed independently, motivated by distinct applications and employing different computational primitives. In this work, mutual reductions between the two tasks are established for single-item sealed-bid auctions with first-price payment. In one direction, an auction used as a black box computes a secure sum: each party bids a private random key drawn from its input, so the clearing price depends on the inputs only through their sum $S$. The reduction is perfectly private against colluding semi-honest parties and uses $O(S^2\log(1/δ))$ auction rounds, which is optimal, or $O(S\log(1/δ))$ under coherent access. It can be instantiated with an existing auctioneer-free quantum auction after a one-line change to its disjunction subroutine, which as published leaks occupancy counts. In the other direction, summation with randomized inputs yields threshold disjunctions, and a single search over composite keys locates the highest bid and a winner, revealing nothing else. Because each query consumes the bidders&#x27; encodings, a bidder can adapt its effective bid undetected, while a fixed query set restores sealed bidding. Combinatorial auctions and general payment rules lie outside this framework. On a superconducting processor, one instance of each direction is executed, recovering the winner for four-bidder instances with ties and the sum of private inputs from repeated auctions.

  匹配依据：MPC: secure multi party computation

  </details>

- **Discrepancy for Random Linear Codes**
  2026-06-23 · MPC · [arXiv](https://arxiv.org/abs/2606.24471)
  Dean Doron, Tal Leonov, Jonathan Mosheiff, Henrique Navas, Nicolas Resch, João Ribeiro

  <details><summary>摘要 / Abstract</summary>

  We show that random linear codes (RLCs) possess nearly optimal discrepancy-type properties in a broad range of settings. Our main results are two general discrepancy theorems: one controls all translates of a fixed test, and the other controls large families of Fourier-pseudorandom tests. Two motivating examples follow: First, RLCs behave essentially like unstructured random codes for list-decoding from errors above capacity. More precisely, an RLC $C\subseteq \mathbb{F}_q^n$ of rate $1 - \frac{1}{n}\log_q|B_ρ| + \varepsilon$, where $|B_ρ|$ is the volume of a radius-$ρ$ Hamming ball in $\mathbb{F}_q^n$, satisfies $|C \cap B| = (1\pm o(1)) \frac{|C|\cdot |B|}{q^n}$ simultaneously for all radius-$ρ$ Hamming balls $B$ with high probability. This vastly generalizes the previously best known fact that RLCs of this rate have covering radius at most $ρn$ with high probability (Blinovsky, 1987). Second, over prime fields, RLCs behave essentially like unstructured random codes for zero-error list-recovery, and list-recovery from erasures, above capacity. More precisely, for a prime $q&gt;2$ and input list size $2\leq \ell\leq q-1$, an RLC $C\subseteq \mathbb{F}_q^n$ of rate $1-\log_q \ell+\varepsilon$ will satisfy $|C \cap S| = (1\pm o(1)) \frac{|C|\cdot \ell^n}{q^n}$ simultaneously for all combinatorial rectangles $S=S_1\times S_2\times\cdots\times S_n$, where $|S_i|=\ell$ for all $i$, with high probability. An analogous result also holds when we can bound $|S_i|$ only for some of the $i$&#x27;s. We use this to show the abundance of locally leakage-resilient $n$-party linear ramp secret sharing schemes with any linear reconstruction threshold and sublinear threshold gap $O(n/\log n)$ over fields of polynomial size $q=Θ(n^γ)$ for a constant $γ\in(0,1/5)$. Prior work was stuck at reconstruction thresholds above $n/2$ for both threshold and ramp schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Secret key-distribution over networks with node-based adversarial errors**
  2026-06-17 · MPC · [arXiv](https://arxiv.org/abs/2606.19305)
  Reza Sayyari, Michael Langberg

  <details><summary>摘要 / Abstract</summary>

  We study the multiple key-cast problem in network coding under active node-based adversaries. In multiple key-cast, a source generates independent secret keys to be securely and reliably delivered to designated terminal subsets. The network adversary can observe \(\ell_o\) nodes, inject additive or overwrite errors into \(\ell_e\) nodes, and simultaneously observe and corrupt \(\ell_{oe}\) nodes, while having full knowledge of the topology and coding operations. Adversarial models of similar nature, however, where corruption and eavesdropping is done on edges instead of nodes, have seen previous studies in the context of secure multicast network-coding. The work at hand builds on and extends these studies to address the challenges in node-based adversaries in the context of (multiple) key distribution. For single-source networks where every node is d-vertex connected from the source, we show that perfectly secure multiple key-cast under additive and overwrite error models is asymptotically achievable at the key-capacity of \(d-\ell_o-\ell_e-2\ell_{oe}\). We then extend our analysis to networks where only terminal nodes satisfy this connectivity requirement, while intermediate nodes may be only partially connected. For these topologies, we develop coding schemes that achieve secure and reliable multiple key-cast capacities determined by the source vertex-connectivity and additional structural properties of the network. Finally, we show that our results generalize to multi-source settings, ensuring perfect secrecy even if the adversary observes all but one source node, and establish that our constructions apply directly to secure multicast network coding and to network secret-sharing scenarios. As part of our studies, we improve the security guarantee of a central scheme in [Zhang et al., IEEE Trans. Comm., 2023] addressing parallel-edge networks, from weak-security to perfect-security.

  匹配依据：MPC: secret sharing

  </details>

- **Giskard : Byzantine Robust and Private Aggregation for Large-Scale Decentralized Learning**
  2026-06-17 · MPC · [arXiv](https://arxiv.org/abs/2606.19129)
  Ousmane Touat, César Sabater, Mohamed Maouche, Sonia Ben Mokhtar

  <details><summary>摘要 / Abstract</summary>

  In decentralized learning, clients train a machine learning model while keeping their data locally and share their model parameters or gradients with a set of neighbors, making it vulnerable to both privacy attacks and model poisoning attacks. Jointly addressing privacy and Byzantine behavior in decentralized learning is challenging. Indeed, Differential Privacy (DP) applied on the client side is known to increase the variance of honest model updates, which weakens Byzantine-robust aggregation against poisoning attacks. Distributed DP can mitigate this issue by adding noise after aggregation, but implementing it without a trusted curator requires both confidential and Byzantine-resilient computation. Recent work addresses this challenge using secure multi-party computation (MPC) to implement robust aggregation while preserving input confidentiality. However, these solutions scale badly: they either require all-to-all communication between participants or delegate the entire computation to a small subset of parties whose computational and communication cost grows with network size. In this paper, we present Giskard, a scalable protocol for private and Byzantine-robust decentralized aggregation. Giskard organizes $n$ parties into a tree of committees of size $O(\log n)$ and evaluates a differentially private coordinate-wise approximate median via a committee-adapted secure quantile search over the value domain, using MPC within each committee. We assess Giskard both theoretically by proving its security and privacy properties and empirically through extensive experiments involving up to one million participants. Compared to its closest competitors, Giskard reduces per-party communication complexity by close to three orders of magnitude over the closest competitor while exhibiting comparable robustness under up to $n/4$ Byzantine parties.

  匹配依据：MPC: secure multi party computation

  </details>

- **Efficient Private Set Intersection and Searchable Encryption using Homomorphic Bloom Filters**
  2026-06-16 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/1267)
  Anil Kumar Pradhan, Killari Nandini, Harsh Kasyap, Sayantan Mukherjee

  <details><summary>摘要 / Abstract</summary>

  Existing encrypted search and private set intersection (PSI) protocols struggle to reconcile post-quantum security with practical efficiency, often leaking search and access patterns or requiring prohibitively deep fully homomorphic encryption (FHE) circuits. We address these limitations by introducing a new Homomorphic Bloom Filters (HBF) framework, a quantum-resilient framework that embeds length-$m$ Bloom filters directly into the plaintext space of an RLWE-based FHE scheme, enabling shallow homomorphic evaluation and matching without structural leakage. Building on HBF, we construct a searchable encryption (SE) scheme and a private set intersection (PSI) protocol, both based on a depth-1 homomorphic missing-bit circuit. The SE scheme requires no rotations or bootstrapping at server side and incurs no additional computational cost as the number of query keywords increases. The PSI protocol reduces each packed Bloom-filter comparison to a single ciphertext--plaintext multiplication, with cost depending on the Bloom-filter length rather than direct element-wise comparisons with the responder&#x27;s set. This framework confines leakage to benign dataset dimensions, tunable false-positive rates, and other public metadata, thereby eliminating explicit pattern leakage.

  匹配依据：MPC: private set intersection

  </details>

- **A Billion Hard CRYSTALS: Automated Design Space Exploration of Mixed-Domain Masking for PQC in Hardware**
  2026-06-16 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/1265)
  Fabian Buschkowski, Niklas Höher, Pascal Sasdrich, Tim Güneysu

  <details><summary>摘要 / Abstract</summary>

  Lattice-based post-quantum cryptographic schemes such as ML-KEM or ML-DSA combine bitwise operations, which are most efficiently masked using Boolean secret sharing, with arithmetic operations modulo q, which are cheaper to mask using an additive sharing in the respective field or ring. Previous work has automated the generation of Boolean-masked hardware circuits as well as the design space exploration process, but to the best of our knowledge, no similar generic framework exists for hardware designs requiring mixed masking domains. Such designs pose three additional challenges. First, share-wise arithmetic requires no registers to be secure, leading to long critical paths without deliberate pipelining. Second, the conversions required at domain boundaries increase both complexity and susceptibility to human error. Finally, generation of masking randomness from a traditional PRNG requires post-processing, e.g., via rejection sampling, to achieve uniformity modulo q, which results in a variable output rate. We solve these issues and integrate our scheme-agnostic solutions into the masking and design space exploration framework HADES. An efficient pre-synthesis critical path estimation, which is around 60 times faster than synthesis with traditional timing analysis, enables effective exploration of mixed-domain masked circuits without compromising the maximum clock frequency. Our adapted gadget-based masking procedure tracks masking domains and inserts pipelined conversions at domain boundaries automatically, or lets the template developer place resource-shared conversions manually. Lastly, a Markov-chain model of probabilistic masking randomness generation and buffering yields cost-minimal design configurations that guarantee stall-free masked operation except for a user-defined failure probability. We evaluate our methodology for multiple relevant moduli and implement an arbitrary-order masked ML-KEM decapsulation core as a case study for our open-source framework. Its area-optimized configurations represent, to the best of our knowledge, the most compact reported ML-KEM designs, with 54.1 kGE unmasked and 125.4 kGE at first order using the NanGate45 library. Jointly optimizing for area and critical path yields competitive clock frequencies of 325–429 MHz for at most 31% more area, which is still smaller than all previous designs. Practical side-channel security at both first and second masking order is validated through FPGA-based TVLA measurements of the full decapsulation routine using 10 million traces each.

  匹配依据：MPC: secret sharing

  </details>

- **Magic Secret Sharing: Threshold Control of Quantum Computational Power via GHZ Entanglement**
  2026-05-15 · MPC · [arXiv](https://arxiv.org/abs/2605.16614)
  Soumyojyoti Dutta, Tushar

  <details><summary>摘要 / Abstract</summary>

  We introduce Magic Secret Sharing (MSS), a quantum cryptographic primitive in which the secret is the computational capability of a quantum state rather than its classical description. In the resource theory of magic, non-stabilizer states fuel universal quantum computation via non-Clifford gates; MSS distributes this resource with an (n-1,n) threshold structure using a pre-shared GHZ state and a single local phase gate P(phi) = diag(1, exp(i*phi)). Any individual party holds the maximally mixed state I/2, with Wigner distance C(I/2) = 0, so no local operation can yield non-Clifford computational advantage regardless of what operations are applied or what noise acts on the device. The authorised coalition reconstructs magic content C(phi) = (|sin(phi)| + |cos(phi)| - 1)/2 exactly, enabling a logical T gate via gate teleportation in multi-server blind quantum computation (BQC). Among diagonal parametric gates, phase gates are the unique class satisfying the security condition, characterised via an exact column-sum condition. The protocol is elevated to a one-sided device-independent (1SDI) setting via a steering inequality: the assemblage produced on the recipient&#x27;s side certifies magic delivery without trusting the coalition&#x27;s devices. We demonstrate the (2,3) instance on ibm_marrakesh (156-qubit IBM Heron): security (C(rho_Bob) &lt; 10^-6, the linear-programming solver tolerance) holds in every run and is independently reproduced on a second qubit assignment, and state fidelity reaches 0.959-0.973 for the authorised party, with faithfulness confirmed for all four test values of phi to within 0.025 in magic content, a residual that depolarising noise alone accounts for.

  匹配依据：MPC: secret sharing

  </details>

- **LogVOLE: Succinct and Efficient Chosen-Input VOLE for ZK and Beyond**
  2026-05-11 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/925)
  Lucien K. L. Ng, Peter Rindal, Akash Shah

  <details><summary>摘要 / Abstract</summary>

  Random Vector Oblivious Linear Evaluation (VOLE) correlations can be generated efficiently for zero-knowledge proofs and secure computation. Applications that need correlations on the receiver’s actual input typically derandomize random VOLE by sending a linear-size vector, a main communication bottleneck. We study chosen-input VOLE (CI-VOLE), where the receiver privately chooses a large vector \(\mathbf{x}\), the sender fixes \(\Delta\), and the parties obtain shares of \(\mathbf{x}\cdot\Delta\) without communicating a linear-size object. This work presents LogVOLE, a concretely efficient CI-VOLE protocol with polylogarithmic end-to-end communication under Ring-LWE. The construction uses a recursive shrink/expand design: it authenticates short digests of the chosen input and then uses a succinct telescope to expand those relations back to the full vector. The protocol has \(O(\lambda\log^2(|\mathbf{x}|+m_{\mathsf{msg}}))\) one-time setup and query communication and \(O(|\mathbf{x}|/n)\) ring operations. Here, \(n\) is the underlying ring degree, \(\lambda\) is the computational security parameter, and \(m_{\mathsf{msg}}\) is the size of the shares. LogVOLE also supports a public-key non-interactive mode: for a fixed \(\Delta\), the sender publishes reusable parameters, and a receiver sends one compact \(\mathbf{x}\)-dependent message to obtain the matching VOLE shares. This gives a route to non-interactive VOLE-based ZK with polylogarithmic communication for arbitrary circuits. We also give a malicious-security extension in the random oracle model. Using LogVOLE, we construct the first concretely efficient VOLE-based designated-verifier ZK protocol for arbitrary circuits with polylogarithmic communication. At 128-bit computational and 40-bit statistical security, our implementation achieves online throughput of 13.9 million \(\mathbb{Z}_p\) correlations/s and 12.9 million ZK multiplication gates/s using 16 CPU cores per party. With golden-seed optimization and reusable setup, our GPU implementation processes 532.3 million \(\mathbb{Z}_p\) correlations/s and 451.7 million ZK multiplication gates/s online on an H200 GPU. With one CPU thread per party, our implementation proves \(1024\times1024\) matrix multiplication in about 4 seconds online, with 226 kB of online communication.

  匹配依据：MPC: secure computation

  </details>

- **BitVM3: Efficient Bitcoin Bridges via Garbled Circuits**
  2026-05-11 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/933)
  Robin Linus Woll, Ioannis Alexopoulos, Lukas Aumayr, Zeta Avarikioti, Matteo Maffei, David Tse

  <details><summary>摘要 / Abstract</summary>

  Bitcoin bridges, protocols that lock BTC on Bitcoin and represent it on a secondary system, underpin much of Bitcoin&#x27;s application layer, yet remain poorly secured. Deployed bridges rely on federated custody with honest-majority assumptions, while BitVM2, the state of the art in trust-minimized bridging, incurs worst-case dispute costs of approximately \$16,000, requiring large operator bonds and deposits that restrict participation to well-capitalized parties. We present BitVM3-BRIDGE, a trust-minimized bridge architecture from Bitcoin to (i) chains with finality certificates, such as Ethereum, and (ii) Bitcoin rollups. Our main contribution is an end-to-end bridge construction that makes trust-minimized Bitcoin bridging practical at scale. The bridge is powered by BitVM3-CORE, a modular abstraction for permissionless off-chain computation on Bitcoin using garbled circuits. In BitVM3-CORE, a challenger evaluates a garbled circuit entirely off-chain and obtains a fraud-proof witness if and only if the operator&#x27;s claim is incorrect. This paradigm reduces total on-chain costs to approximately \$9, with the challenge transaction itself costing just \$0.20. This nearly 1000× cost reduction enables smaller bonds, broader operator participation, and smaller deposit sizes. Beyond the bridge itself, we make two additional contributions. First, we formalize BitVM3-CORE as a sound and complete on-chain proof system under standard cryptographic assumptions. Prior GC-based proposals typically provide either informal security arguments or construction-specific formalizations. By contrast, our framework captures existing constructions within a uniform model and gives a generic treatment based on axiomatized security and functional assumptions. Second, we introduce an on-chain Bitcoin light client secure in the variable-difficulty setting, enabling permissionless chain introspection on Bitcoin and thereby the rollup variant of BitVM3-BRIDGE.

  匹配依据：MPC: garbled circuit, garbled circuits

  </details>

- **On the Common Bias of Majorities: Poly-Time Attacks on THR-XOR PRGs**
  2026-05-05 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/880)
  Antonio Giulio D’Antona, Pierrick Méaux, Akin Ünal

  <details><summary>摘要 / Abstract</summary>

  Pseudorandom Generators (PRGs) based on Threshold-XOR predicates with large locality and high stretches have recently gained traction, since they lend themselves as shallow weak Pseudorandom Functions (PRFs) to fast multiparty computation protocols. In this work, we present novel fast attacks on such PRGs that achieve substantial advantages. Concretely, we break the security levels of most parameters collected by Boura, Couteau, Perrin and Rotella (ToSC&#x27;25), as well as those proposed by Fu, Li, Lyu and Liu (EC&#x27;26). On the asymptotic side, we prove that our attacks achieve an advantage of $n^{-n/a}$ where $n$ denotes the seed length and $a$ the locality of threshold predicates. As a consequence, when $a \in \Theta(n)$, we get poly-time attacks with noticeable advantage. These results close current gaps on the theoretical study of THR-XOR based Goldreich PRGs. Additionally, we demonstrate how the attack advantage can be amplified for PRGs with large output lengths (which are common in the context of weak PRFs). Finally, we discuss alternative predicates for Goldreich PRGs that resist all currently known attacks.

  匹配依据：MPC: multiparty computation

  </details>

- **Federated Generation of Synthetic RNA-seq Data**
  2026-04-30 · MPC · [arXiv](https://arxiv.org/abs/2604.27456)
  Daniil Filienko, Martine De Cock, Sikha Pentyala

  <details><summary>摘要 / Abstract</summary>

  Access to genomic data is highly regulated due to its sensitive nature. While safeguards are essential, cumbersome data access processes pose a significant barrier to the development of AI methods for genomics. Synthetic data generation can mitigate this tension by enabling broader data sharing without exposing sensitive information. Synthetic genomic data are produced by training generative models on real data and subsequently sampling artificial data that preserves relevant statistics while limiting disclosures about the underlying individuals. In some settings, a single data holder may have sufficient data to train such generative models; however, in many applications data must be combined across multiple sites to achieve adequate scale. This need arises, e.g., in rare disease studies, where individual hospitals typically hold data for only a small number of patients. The solution we present in this paper enables multiple data holders to jointly train a synthetic data generator without revealing their raw data. Our approach combines secure multiparty computation (MPC) to ensure input privacy, so that no party ever discloses its data in unencrypted form, with differential privacy (DP) to provide output privacy by mitigating information leakage from the released synthetic data. We empirically demonstrate the effectiveness of the proposed method by generating high-utility synthetic datasets from multiple real RNA-seq cohorts in federated settings, showing that our approach enables privacy-preserving data synthesis even when data are distributed across institutions.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Practical Post-Quantum Secure Publicly Verifiable Secret Sharing and Applications**
  2026-04-24 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/813)
  Aniket Kate, Pratyay Mukherjee, Hamza Saleem, Pratik Sarkar, Rohit Sinha

  <details><summary>摘要 / Abstract</summary>

  We present a new framework for constructing practically efficient publicly verifiable secret sharing (PVSS) with $non-interactive$ $dealers$, in that the dealer may go offline after sending a single message, and is not involved in the share verification process. We use identity-based encryption (IBE) and commitments as the main ingredients and avoid expensive zero-knowledge proofs. By instantiating them with post-quantum secure schemes, a lattice-based IBE and a hash-based commitment, we obtain our first construction: a post-quantum secure PVSS with non-interactive dealers that outperforms the prior lattice-based practical construction by Gentry et al. [Eurocrypt 2022]. However, to enable the aggregation of PVSS transcripts (which facilitates many additional applications such as secure voting), we propose our second construction by replacing hash-based commitments with Pedersen&#x27;s homomorphic commitments. While this does not achieve full-fledged post-quantum security (as Pedersen&#x27;s scheme is not quantum safe), it still provides privacy against a post-quantum adversary. We prove the security of this construction in a new model, which we call long-lasting security. This model guarantees that the protocol is secure in the present (pre-quantum era) while maintaining privacy in the long term (post-quantum era). This new model is of independent interest for constructing efficient schemes that are resilient to the harvest-now-decrypt-later line of attacks. In this model, we propose a blockchain-compatible secure voting scheme using our PVSS scheme. Our PVSS schemes demonstrate practical efficiency: our post-quantum PVSS shares a secret among $1024$ receivers in $667$~ms and verifies the dealing in $&lt;5$ ms, and communicates $4.4$MB, overall whereas the state of the art [Gentry et al., Eurocrypt 2022] communicates $251$MB and requires $2060$s for dealing the secret.

  匹配依据：MPC: secret sharing

  </details>

- **Towards Formal Security Proofs of MQOM**
  2026-03-31 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/629)
  Haruhisa Kosuge, Keita Xagawa

  <details><summary>摘要 / Abstract</summary>

  Recent MPC-in-the-Head (MPCitH) signatures increasingly rely on aggressive GGM-tree optimizations to reduce signature size and computational cost, culminating in __secret-key-root correlated GGM trees__ as used in SBC (Huth and Joux, CRYPTO 2024), MQOM (NIST PQC Standardization for Additional Signature Round-2, 2024), and rBN++ (Kim, Lee, and Son, EUROCRYPT 2025). While this technique yields substantial compression, it introduces a dependency loop in the proof (Kosuge and Xagawa, CiC 2026(3)). We analyze MQOM and resolve this circularity by providing EUF-CMA security proofs for a slightly modified variant. The modifications consist of incorporating a salt into the input of a hash function and modifying the evaluation domain to ensure that all evaluation points are nonzero. For the resulting variant of MQOM, we prove EUF-CMA security for the GF(2) parameter sets in the random-oracle plus ideal-cipher model, assuming EUF-NMA security, standard one-wayness, and a heuristic conjecture on matrices. Our proof combines the H-coefficient technique with one-wayness, which may be of independent interest. We also prove EUF-CMA security in the (quantum) random-oracle model, where block-cipher-based hash functions are modeled as random oracles. The proof relies on EUF-NMA security and partial-guessing one-wayness (Feneuil and Rivain, ASIACRYPT 2026), which can be reduced classically to partial-domain one-wayness.

  匹配依据：MPC: mpc (context)

  </details>

- **Post-Quantum Cryptography from Quantum Stabilizer Decoding**
  2026-03-19 · MPC · [arXiv](https://arxiv.org/abs/2603.19110) · [IACR ePrint](https://eprint.iacr.org/2026/548)
  Jonathan Z. Lu, Alexander Poremba, Yihui Quek, Akshar Ramkumar

  <details><summary>摘要 / Abstract</summary>

  Post-quantum cryptography currently rests on a small number of hardness assumptions, posing significant risks should any one of them be compromised. This vulnerability motivates the search for new and cryptographically versatile assumptions that make a convincing case for quantum hardness. In this work, we argue that decoding random quantum stabilizer codes -- a quantum analog of the well-studied LPN problem -- is an excellent candidate. This task occupies a unique middle ground: it is inherently native to quantum computation, yet admits an equivalent formulation with purely classical input and output, as recently shown by Khesin et al. (STOC &#x27;26). We prove that the average-case hardness of quantum stabilizer decoding implies the core primitives of classical Cryptomania, including public-key encryption (PKE) and oblivious transfer (OT), as well as one-way functions. Our constructions are moreover practical: our PKE scheme achieves essentially the same efficiency as state-of-the-art LPN-based PKE, and our OT is round-optimal. We also provide substantial evidence that stabilizer decoding does not reduce to LPN, suggesting that the former problem constitutes a genuinely new post-quantum assumption. Our primary technical contributions are twofold. First, we give a reduction from random quantum stabilizer decoding to an average-case problem closely resembling LPN, but which is equipped with additional symplectic algebraic structure. While this structure is essential to the quantum nature of the problem, it raises significant barriers to cryptographic security reductions. Second, we develop a new suit of scrambling techniques for such structured linear spaces, and use them to produce rigorous security proofs for all of our constructions.

  匹配依据：MPC: oblivious transfer

  </details>

- **Duty-Free Bits: Projectivizing Garbling Schemes**
  2026-03-08 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/476)
  Nakul Khambhati, Anwesh Bhattacharya, David Heath

  <details><summary>摘要 / Abstract</summary>

  Garbling schemes are powerful primitives that enable secure computation between a mutually untrusting garbler and evaluator. A projective garbling scheme is one that encodes the evaluator&#x27;s input in a simple bit-by-bit manner. Projective schemes, such as the seminal scheme of Yao, are versatile, as they are naturally compatible with other simple tools, such as $1$-out-of-$2$ oblivious transfer (OT). There exist garbling schemes that naturally operate over large finite fields, some of which require only efficient information-theoretic (IT) techniques. However, here the evaluator&#x27;s input is encoded via an affine function over a large field, so these schemes are not naturally projective, reducing their versatility. We provide a transformation that efficiently projectivizes such schemes. Consider an arithmetic garbling scheme where the evaluator&#x27;s input consists of elements from a large prime field. Our symmetric-key-based garbling techniques give a mechanism to translate from Yao-style garbled labels to IT-style garbled labels at cost proportional to the input and output labels: crossing the border is duty-free! We apply our technique to two problems. (1) Recent works show that projective garbling schemes solve a problem central to trust-minimized bridges for the Bitcoin blockchain. BABE (Garg et al., 2026) and Argo MAC (Eagen and Lai, 2026) give two different approaches. Both works implicitly construct an efficient IT garbling scheme, then use naive bit-decomposition to achieve projectivity. We construct and implement drop-in replacements for both; we improve BABE&#x27;s encoding size by $51\times$, and Argo MAC&#x27;s by $23\times$. (2) Our technique implies a non-interactive reduction from vector oblivious linear evaluations (VOLEs) over $\mathbb{F}_p$ to $1$-out-of-$2$ OTs. To our knowledge, ours is the state-of-the-art Minicrypt (plus base OTs) protocol for large field VOLE secure against a malicious receiver. It costs only $O((\lambda + n) \lg p)$ bits.

  匹配依据：MPC: garbling scheme, garbling schemes, oblivious transfer, secure computation

  </details>

- **Putting the OPTI in Round Optimal IA-MPC in the Plain Model**
  2026-02-27 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/406)
  Yashvanth Kondi, Divya Ravi, Jure Sternad, Sophia Yakoubov

  <details><summary>摘要 / Abstract</summary>

  We advance the study of best-possible security guarantees of two-round secure multiparty computation in the plain model. While Goel et al. (TCC &#x27;21) showed the infeasibility of Identifiable Abort in two rounds in the plain model with a standard honest majority (i.e. $t &lt; n/2$), the effect of relaxing the setting to an honest supermajority has not been established. In this work, we close this gap. When $t &lt; n/3$, we show that two rounds are sufficient to achieve identifiable abort. Notably, ours is the first two-round general-purpose MPC construction in the plain model tolerating more than one corruption that achieves a guarantee stronger than unanimous abort. We obtain our construction via a new compiler that lifts any protocol with unanimous abort to one that achieves identifiable abort. A core building block for our compiler is Oblivious Public Transfer with Intermediaries (OPTI), a new primitive that we introduce which may be of independent interest.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Perfectly Secure Network-Agnostic MPC Comes for Free.**
  2026-02-24 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_12) · [IACR ePrint](https://eprint.iacr.org/2026/377)
  Xiaoyu Ji, Chen-Da Liu-Zhang, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) allows a set of parties to jointly compute a function while keeping their inputs private. Classical MPC protocols assume either a synchronous or an asynchronous network. Synchronous protocols tolerate more corrupted parties but rely on a timing bound, while asynchronous protocols make no timing assumptions but handle fewer corruptions. The network-agnostic model aims to combine the advantages of both. It requires security without knowing in advance whether the network is synchronous or asynchronous, guaranteeing resilience against up to $t_s$ corruptions in the synchronous case and $t_a$ corruptions in the asynchronous case. The optimal corruption threshold for perfect security has been established as $n = 2\max(t_s, t_a) + \max(2t_a, t_s) + 1$, but prior work either falls short of this threshold or requires exponential local computation. In this work, we present the first perfectly secure network-agnostic MPC protocol with polynomial communication and computation complexity under the optimal threshold. Our protocol achieves expected communication complexity $\mathcal{O}((|C|n + (D+C_I)n^2 + n^6)\log n)$ bits for a circuit of size $|C|$ over a finite field $\mathbb{F}$ of size $\mathcal{O}(n)$, depth $D$, and input size $C_I$. Our main technical contribution is a compiler that generates Beaver triples in the network-agnostic setting using synchronous and asynchronous triple-generation protocols in a black-box way. Beyond the cost of the underlying protocols, it only requires $\mathcal{O}(n^2)$ instances of network-agnostic Byzantine agreement.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Statistically Secure Asynchronous MPC with Linear Communication and $\\mathcal{O}(n^5)$ Additive Overhead**
  2026-02-19 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/320)
  Xiaoyu Ji, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) allows distrusted parties to jointly evaluate a common function while keeping their inputs private. In this work, we focus on improving the communication complexity of information-theoretic asynchronous MPC with optimal resilience ($t &lt; n/3$). The current state-of-the-art work in this setting by Goyal, Liu-Zhang, and Song [Crypto’24] achieves amortized linear communication per gate with $\Omega(n^{14})$ elements additive overhead. In comparison, the best-known result in the synchronous setting by Goyal, Song, and Zhu [Crypto’20] achieves the amortized linear communication per gate with only $\mathcal{O}(n^{6})$ elements additive overhead, revealing a significant gap that we aim to close. This work closes this gap and goes further. We present the first statistically secure asynchronous MPC protocol achieving amortized linear communication per gate with only $\mathcal{O}(n^{5})$ elements additive overhead assuming a functionality for Agreement on Common Set (ACS). With the best-known instantiation for ACS, we obtain an asynchronous MPC protocol in the plain model with additive overhead $\mathcal{O}((\kappa+n)n^4\log\kappa)$ elements in expectation, where $\kappa$ is the security parameter. In the setting of statistical security with optimal resilience, this even surpasses the best synchronous result when $n\geq\sqrt{\kappa\log\kappa}$. Technically, our contributions include (i) a new protocol for generating Beaver triples with linear communication per triple and $\mathcal{O}(n^3)$ elements additive overhead assuming functionalities for generating random degree-$t$ Shamir sharings and ACS, and (ii) a new protocol for generating random degree-$t$ Shamir sharings with linear communication per sharing and $\mathcal{O}(n^{5})$ elements additive overhead assuming a functionality for ACS.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Multi-key Fully Homomorphic Encryption with Non-Interactive Setup in the Plain Model**
  2026-02-19 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/322)
  Seonhong Min, Jeongeun Park, Yongsoo Song

  <details><summary>摘要 / Abstract</summary>

  Multi-key fully homomorphic encryption (MKFHE) enables computation over encrypted data under multiple different keys. Constructing MKFHE without any trusted or interactive setup remains an open problem. In the context of MKFHE, a trusted setup is often assumed to mean the use of a common random string (CRS). In this paper, we present the first MKFHE scheme in the plain model (i.e., without any trusted or interactive setup) based on the RLWE assumption. Specifically, we construct a multi-key somewhat homomorphic encryption based on the RLWE assumption and extend it to a multi-key variant of the Gentry-Sahai-Waters (GSW) scheme with a circular security assumption. Our design yields a 2-round multi-party computation (MPC) in the plain model against semi-honest adversaries. Moreover, it can be applied to transform existing FHE schemes that rely on RGSW in their construction into a multi-key variant. We also provide concrete conversions for widely-used FHE schemes, including BGV, BFV, CKKS, FHEW, TFHE, and Carousel. Finally, we implement our scheme and present experimental results for the expansion algorithm from a single-key ciphertext to a multi-key ciphertext and the multi-key homomorphic multiplication algorithm.

  匹配依据：MPC: multi party computation

  </details>

- **Fuzzy Private Set Intersection under Density-Bounded Assumptions**
  2026-02-14 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/262)
  Seunghun Paik, Jae Hong Seo

  <details><summary>摘要 / Abstract</summary>

  This paper presents a new fuzzy private set intersection (FPSI) protocol, a two-party protocol to securely identify similar items across private sets. Our design departs from the prevailing separation-based paradigm---e.g., ``apart by $2\delta$&#x27;&#x27; or the disjoint projection assumption---which either incurs exponential overhead in dimensionality or requires high dimensionality to justify the assumption. Instead, we address this tension by explicitly allowing collisions within $\delta$-balls, but requiring that their multiplicity be bounded per axis. We formalize this new structural property as $C$-max collision. We theoretically analyze its plausibility on several common distributions, e.g., the uniform distribution, and real datasets, and provide an efficient algorithm to verify this assumption. Under the $C$-max collision property, we propose an efficient FPSI protocol for $\ell_{\infty}$ distance that supports both low- and high-dimensional regimes. Our construction is based on a novel abstraction that views FPSI as an oblivious intersection of membership tags, which natively handles axis-wise matching multiplicity. We capture its requirements through a new functionality called oblivious selected set intersection, along with its instantiation based on symmetric key techniques. Assuming the $C$-max collision property on the receiver&#x27;s set, our protocol achieves computation/communication complexities scaling linearly with both parties&#x27; set sizes for a fixed $C$. We implement our protocol and conduct extensive evaluation. While a direct comparison is infeasible, ours achieves online efficiency comparable to state-of-the-art separation-based FPSI protocols in both low- and high-dimensional regimes.

  匹配依据：MPC: private set intersection

  </details>

- **ECHO: Efficient Covertly-Secure Three-party Computation with Applications to Private Machine Learning**
  2026-02-10 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/216)
  Yufei Duan, Yun Li, Zhicong Huang, Cheng Hong, Tao Wei, Chao Zhang

  <details><summary>摘要 / Abstract</summary>

  Secure three-party computation with an honest majority is among the most efficient secure computation settings and is widely used in practice. However, achieving malicious security incurs significant overhead, often an order of magnitude higher than semi-honest protocols. Covert security provides a security–efficiency trade-off by detecting malicious behavior with a certain probability (e.g., $50\%$), deterring rational adversaries. Existing covert protocols mainly target two-party or dishonest-majority settings, with little work on efficient honest-majority three-party solutions. We present $\mathsf{ECHO}$, a family of concretely efficient protocols for covertly secure honest-majority three-party computation. We explore the design space of cheating detection and identification, and develop optimized protocols for both arithmetic and Boolean circuits, targeting different performance goals such as low latency and reduced communication. For arithmetic circuits over rings, our asymmetric-MAC-based protocol achieves an online phase only $1.26\times$ slower than the semi-honest baseline and over $5.59\times$ faster than malicious security. For Boolean circuits, our method improves over the best malicious protocol by $5\times$. We also applied $\mathsf{ECHO}$ on practical PPML tasks. $\mathsf{ECHO}$ approaches semi-honest performance while providing up to $8\times$ speedup over malicious security.

  匹配依据：MPC: secure computation, secure three party computation, three party computation

  </details>

- **BABE: Verifying Proofs on Bitcoin Made 1000x Cheaper**
  2026-01-16 · MPC · [IACR ePrint](https://eprint.iacr.org/2026/065)
  Sanjam Garg, Dimitris Kolonelos, Mikhail Sergeevitch, Srivatsan Sridhar, David Tse

  <details><summary>摘要 / Abstract</summary>

  Endowing Bitcoin with the ability to verify succinct proofs has been a longstanding problem with important applications such as scaling Bitcoin and allowing the Bitcoin asset to be used in other blockchains trustlessly. It is a challenging problem due to the lack of expressiveness in the Bitcoin scripting language and the small Bitcoin block space. BitVM2 is the state-of-the-art verification protocol for Bitcoin used in several mainnets and testnets, but it suffers from very high on-chain Bitcoin transaction fees in the unhappy path (over $14,000 in a recent experiment). Recent research BitVM3 dramatically reduces this on-chain cost by using a garbled SNARK verifier circuit to shift most of the verification off-chain, but each garbled circuit is 42 Gibytes in size, so the off-chain storage and setup costs are huge. This paper introduces BABE, a new proof verification protocol on Bitcoin, which preserves BitVM3&#x27;s savings of on-chain costs but reduces its off-chain storage and setup costs by three orders of magnitude. BABE uses a witness encryption scheme for linear pairing relations to verify Groth16 proofs. Since Groth16 verification involves non-linear pairings, this witness encryption scheme is augmented with a secure two-party computation protocol implemented using a very efficient garbled circuit for scalar multiplication on elliptic curves. The design of this garbled circuit builds on a recent work, Argo MAC, which gives an efficient garbling scheme to compute homomorphic MACs on such curves.

  匹配依据：MPC: garbled circuit, garbling scheme, secure two party computation

  </details>

- **cwPSU: Efficient Unbalanced Private Set Union via Constant-weight Codes.**
  2026 · MPC · [NDSS](https://www.ndss-symposium.org/ndss-paper/cwpsu-efficient-unbalanced-private-set-union-via-constant-weight-codes/)
  Song Bian, Hui Li, Qingwen Li

- **Updatable Private Set Intersection from Symmetric-Key Techniques.**
  2026 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25317-0_13)
  Junxin Liu, Xinyi Shi, Peihan Miao, Jifeng Wang, Mike Rosulek

- **Updatable Multi-Party Private Set Intersection for Real-Time Collaborative Threat Intelligence.**
  2026 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2026.3707440)
  Zhongming Wang, Biwen Chen, Xiaoguo Li, Ze Jiang, Di Zhang, Xiaofeng Liao, Tao Xiang

- **Universally Composable Almost-Everywhere Secure Computation.**
  2026 · MPC · [Journal of Cryptology](https://doi.org/10.1007/S00145-025-09565-2)
  Juan A. Garay, Rutvik Patel, Pouyan Forghani, Nishanth Chandran, Rafail Ostrovsky, Vassilis Zikas

- **Unconditionally Secure MPC for Boolean Circuits with Constant Communication.**
  2026 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-032-35418-1_1)
  Yubo Zeng, Kang Yang, Min Zhang, Dengguo Feng

- **UFOs: An Ultra-Fast Toolkit for Multiparty Computation on Small Elements.**
  2026 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2026.3734714)
  Yuan Zhang, Moyang Xie, Sheng Zhong, Jiacheng Gao

- **Traceable Secret Sharing Schemes for General Access Structures.**
  2026 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_1)
  Miquel Guiot, Oriol Farràs

- **Traceable Secret Sharing Revisited.**
  2026 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_2)
  Abhishek Jain, Vipul Goyal, Aditi Partap

- **Towards Scalable YOSO MPC via Packed Secret-Sharing.**
  2026 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-95-5116-3_3)
  Daniel Escudero, Elisaweta Masserova, Antigoni Polychroniadou

- **Threshold Homomorphic Secret Sharing: Definitions and Constructions.**
  2026 · MPC · [series/lncs](https://doi.org/10.1007/978-981-95-5119-4_18)
  Junqing Gong, Rupeng Yang, Shifeng Sun, Xinzhou Wang, Yuan Luo, Dawu Gu

- **Taming Adaptive Security and New Access Structures in Evolving Secret Sharing.**
  2026 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-95-5125-5_3)
  Sara Giammusso, Danilo Francati, Daniele Venturi

- **Succinct Line-Point Zero-Knowledge Arguments from Homomorphic Secret Sharing.**
  2026 · MPC · [series/lncs](https://doi.org/10.1007/978-981-95-5116-3_19)
  Zhe Li, Mengmeng Zhou, Yizhou Yao, Chaoping Xing, Chen Yuan

- **Succinct Garbled Circuits with Low-Depth Garbling Algorithms.**
  2026 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_9)
  Huijia Lin, Hanjun Li, George Lu

- **Succinct Computational Secret Sharing for Monotone Circuits.**
  2026 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-95-5125-5_4)
  Shafik Nassar, George Lu, Brent Waters

- **Statistically Secure Asynchronous MPC with Linear Communication and 풪(n5) Additive Overhead.**
  2026 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-032-35418-1_2)
  Yifan Song, Xiaoyu Ji

- **Simultaneous-Message and Succinct Secure Computation: Reusable and Multiparty Protocols.**
  2026 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_4)
  Akshayaram Srinivasan, Abhishek Jain, David J. Wu, Siddharth Agarwal

- **Simplified PIR and CDS Protocols and Improved Linear Secret-Sharing Schemes.**
  2026 · MPC · [TCC](https://doi.org/10.1007/978-3-032-12293-3_12)
  Bar Alon, Or Lasri, Amos Beimel

- **Secure Computation Over Gaussian Multiple-Access Wiretap Channels With Feedback.**
  2026 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2026.3715114)
  Han Deng, Bin Dai, Yuhan Yang, Fan Cheng, Haoheng Yuan, Chao Qi

- **Secure Computation Against NC1 Leakage Without Secure Hardware.**
  2026 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-032-35415-0_10)
  Yuyu Wang

- **Secret Sharing Schemes From Correlated Random Variables and Rate-Limited Public Communication.**
  2026 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2026.3657030)
  Rumia Sultana, Remi A. Chou

- **SecP-Tuning: Efficient Privacy-Preserving Prompt Tuning for Large Language Models via MPC.**
  2026 · MPC · [ICLR](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7f2e5d16c2c5ac161ce7aa44af35c0fe-Abstract-Conference.html)
  Zhuo Zhang, Xun Zhou, Yehong Zhang, Shiyu Liu, Jinglong Luo, Ye Dong, Hui Wang, Zenglin Xu, Yue Yu

- **SecOIR: Enhancing Privacy and Accuracy in Outsourced Image Retrieval via Function Secret Sharing and Deep Hashing.**
  2026 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2025.3628356)
  Zhi Li, Hao Wang, Xiaochao Wei, Ye Su, Lei Wu, Wenying Zhang

- **Scaling Fully Secure MPC via Robust Recursive Search and Gap Amplification.**
  2026 · MPC · [PKC](https://doi.org/10.1007/978-3-032-26734-4_10)
  Matan Hamilis, Ariel Nof

- **Scalable Privacy-Preserving Shortest Path Distance Computation via 2-Hop Labeling in MPC.**
  2026 · MPC · [PACMMOD / SIGMOD](https://doi.org/10.1145/3786695)
  Huizhong Wang, Kun Chen, Chenhao Ma, Yuanyuan Zeng, Wei Dong

- **RoundRole: Unlocking the Efficiency of Multi-party Computation with Bandwidth-aware Execution.**
  2026 · MPC · [NDSS](https://www.ndss-symposium.org/ndss-paper/roundrole-unlocking-the-efficiency-of-multi-party-computation-with-bandwidth-aware-execution/)
  Kun Chen, Wei Xu, Jiping Yu, Yunyi Chen, Xiaoyu Fan, Xin Liu

- **Randomized Agreement, Verifiable Secret Sharing and Multi-party Computation in Granular Synchrony.**
  2026 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-95-5116-3_1)
  David Heath, Ananya Appan, Ling Ren

- **Pseudorandom Correlation Functions for Garbled Circuits.**
  2026 · MPC · [TCC](https://doi.org/10.1007/978-3-032-12293-3_15)
  Srini Devadas, Geoffroy Couteau, Sacha Servan-Schreiber, Alexander Koch

- **Privacy-Preserving Continuous Authentication of Smartphone Users via Secret Sharing.**
  2026 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2026.3680150)
  Mingming Hu, Ding Wang, Daojun Han, Bibo Tu, Jingtao Guo

- **PriFFT: Privacy-Preserving Federated Fine-Tuning of Large Language Models via Hybrid Secret Sharing.**
  2026 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2026.3661572)
  Ke Cheng, Qiang Qu, Zhichao You, Jiaxuan Fu, Xutong Mu, Shiyang Ma, Yulong Shen, Xuewen Dong

- **Practical Traceable Over-Threshold Multi-Party Private Set Intersection.**
  2026 · MPC · [NDSS](https://www.ndss-symposium.org/ndss-paper/practical-traceable-over-threshold-multi-party-private-set-intersection/)
  Kailiang Ji, Weijing You, Huiyang He, Le Yang, Jingqiang Lin

- **Practical Private Set Operation via Secret Sharing for Lightweight Clients.**
  2026 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2026.3684841)
  Ziyu Niu, Yumei Li, Yudi Zhang, Willy Susilo, Hao Wang, Ye Su

- **Practical Multi-Party Private Set Intersection with Reducible Zero-Sharing.**
  2026 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00006)
  Jin Tan, Zhenyu Guan, Hua Guo, Yewei Guan, Jiarong Huo, Man Ho Au

- **Polynomial Secret Sharing Schemes and Algebraic Matroids.**
  2026 · MPC · [series/lncs](https://doi.org/10.1007/978-3-032-12293-3_14)
  Oriol Farràs, Amos Beimel, Adriana Moya

- **PUFF: Maximally Proactive Security for Free in Perfectly Secure MPC with Guaranteed Output Delivery.**
  2026 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_18)
  Jiarui Li, Mengzhen Zou, Guoyan Zhang, Guidong Li, Chen Qian

- **Over-Threshold Multiparty Private Set Intersection for Collaborative Network Intrusion Detection.**
  2026 · MPC · [NSDI](https://www.usenix.org/conference/nsdi26/presentation/arpaci)
  Florian Kerschbaum, Raouf Boutaba, Onur Eren Arpaci

- **Optimistic Asynchronous Dynamic-Committee Proactive Secret Sharing.**
  2026 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00243)
  Zhuolun Xiang, Qiang Tang, Bin Hu, Zhenliang Lu, Zongyang Zhang, Jianwei Liu

- **Optimal Access Structure Partition Methods for Image Secret Sharing.**
  2026 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2025.3645631)
  Li Tang, Ching-Nung Yang, Wei Qi Yan, Zhihua Xia, Xiaotian Wu

- **On the Security of Linear Secret Sharing with General Noisy Side-Channel Leakage.**
  2026 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25336-1_17)
  Hessam Mahdavifar, Utkarsh Gupta

- **On the Power of Sumcheck in Secure Multiparty Computation.**
  2026 · MPC · [PKC](https://doi.org/10.1007/978-3-032-26734-4_9)
  Zhe Li, Yizhou Yao, Chen Yuan, Chaoping Xing

- **On the Attribute Hiding Security of Privacy Preserving Secret-Sharing-Based Outsourced Decision Tree Classification.**
  2026 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2026.3714143)
  Yu-Chi Chen, Chang-Ching Hung, Tsung-Chen Hsieh, Srinivas Shekar

- **On Succinct Non-interactive Secure Computation with Malicious Security.**
  2026 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_20)
  Arka Rai Choudhuri, Omer Paneth, Abhishek Jain, Maya Farber Brodsky

- **Oblivis: A Framework for Delegated and Efficient Oblivious Transfer.**
  2026 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2026-0104)
  Aydin Abadi, Yvo Desmedt

- **Non-interactive Secure Computation with Constant Communication Overhead.**
  2026 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_5)
  Naty Peter, Yuval Ishai, Akshayaram Srinivasan, Ziyang Jin

- **New Upper and Lower Bounds for Perfectly Secure MPC.**
  2026 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_13)
  Lawrence Roy, Shravani Patil, Arpita Patra, Ivan Damgård

- **New Framework for Structure-Aware PSI From Distributed Function Secret Sharing.**
  2026 · MPC · [series/lncs](https://doi.org/10.1007/978-981-95-5116-3_10)
  Peihan Miao, Dung Bui, Gayathri Garimella, Phuoc Pham Van Long

- **Multiparty Homomorphic Secret Sharing and More from LPN and MQ.**
  2026 · MPC · [TCC](https://doi.org/10.1007/978-3-032-12293-3_16)
  Geoffroy Couteau, Naman Kumar, Xiaxi Ye

- **Multiparty Computation with Minimal Overhead Without Circuit Transformation.**
  2026 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-032-35418-1_5)
  Aditya Hegde, Mingyuan Wang, Phuoc Pham Van Long

- **MinBucket MPSI: Breaking the Max-Size Bottleneck in Multi-Party Private Set Intersection.**
  2026 · MPC · [NDSS](https://www.ndss-symposium.org/ndss-paper/minbucket-mpsi-breaking-the-max-size-bottleneck-in-multi-party-private-set-intersection/)
  Yang Cao, Binbin Tu, Yu Chen, Boyudong Zhu

- **Malicious Private Set Union with Two-Sided Output.**
  2026 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25317-0_14)
  Ni Trieu, Sihang Pu, Jiahui Gao

- **Malicious Homomorphic Secret Sharing with Applications to DV-NIZK and More.**
  2026 · MPC · [PKC](https://doi.org/10.1007/978-3-032-26740-5_7)
  Lisa Kohl, Zhe Li, Pedro Capitão, Hila Dahari-Garbian

- **Maintaining Sublinear Locality Over Time: Adaptively Secure MPC on a Reusable Hidden Graph.**
  2026 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_19)
  Elette Boyle, Ran Cohen, Pierre Meyer

- **Just-in-Time-OPRFs and a Modular Framework for Fast Private Set Intersection.**
  2026 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-032-35418-1_12)
  Rishabh Ranjan, Doreen Riepel, Mihir Bellare

- **Honest Majority Constant-Round MPC with Linear Communication from One-Way Functions.**
  2026 · MPC · [series/lncs](https://doi.org/10.1007/978-3-032-12287-2_1)
  Junru Li, Yifan Song

- **GoSSamer: Lightweight and Linear-Communication Asynchronous (Dynamic Proactive) Secret Sharing and the Applications.**
  2026 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00185)
  Bin Hu, Yuan Lu, Xinxin Xing, Yizhong Liu, Boyang Liao, Jianwei Liu, Xun Lin, Tianwei Zhang

- **Fuzzy Private Set Intersection from VOLE.**
  2026 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-95-5116-3_11)
  Sihang Pu, Aron van Baarsen

- **Faster Than Ever: A New Lightweight Private Set Intersection and Its Variants.**
  2026 · MPC · [NDSS](https://www.ndss-symposium.org/ndss-paper/faster-than-ever-a-new-lightweight-private-set-intersection-and-its-variants/)
  Liyao Xiang, Jinyong Shan, Weidong Qiu, Guowei Ling, Peng Tang

- **Fast and Efficient Perfectly Secure Network-Agnostic Secure Computation.**
  2026 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_7)
  Gilad Stern, Gilad Asharov, Fatima Elsheimy

- **FESCAT: Function Secret Sharing Based Efficient Secure Collaborative Analysis of Time Series Data.**
  2026 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2025.3632891)
  David S. L. Wei, Jingcheng Zhao, Qibin Sun, Bin Zhu, Kaiping Xue, Jun Lu

- **Efficient Privacy-Preserving User Tracking From Threshold Multi-Party Private Set Intersection.**
  2026 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2026.3705319)
  Jianting Ning, Haining Yang, Jing Qin, Bo Zhao, Jixin Ma

- **Efficient Malicious Multiparty Private Set Intersection Supporting Cardinality, Sharing, and Batching.**
  2026 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2026.3671114)
  Kim-Kwang Raymond Choo, Zhenfu Cao, Xiyuan Han, Jun Zhou, Xiaolei Dong

- **Efficient Fuzzy Private Set Intersection from Secret-Shared OPRF.**
  2026 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00172)
  Meng Hao, Yonggang Wen, Xinpeng Yang, Chenkai Weng, Robert H. Deng, Tianwei Zhang

- **Dishonest-Majority Secure Computation via PIR-Authenticated Multiplication Triples.**
  2026 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-032-35418-1_15)
  Matan Hamilis, Yuval Ishai, Ariel Nof, Elette Boyle, Niv Gilboa

- **Deniable Secret Sharing.**
  2026 · MPC · [series/lncs](https://doi.org/10.1007/978-3-032-12293-3_13)
  Sophia Yakoubov, Sebastian Kolby, Divya Ravi, Ran Canetti, Ivan Damgård

- **Decor: Delegated Computation on Randomness for Secure Evaluation of Nonlinear Functions.**
  2026 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00256)
  Hyunghoon Cho, Haris Smajlovic, Ruzica Piskac, Kyle Sheng, Timos Antonopoulos

- **DMPF-PSI: Enabling High-Frequency Updatable Private Set Intersection on Dynamic Data.**
  2026 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2026.3705330)
  Zhi Li, Debiao He, Hao Wang, Jiadi Zhang, Ye Su

- **Cryptanalysis of "Multi-Party Private Set Intersection With One-Round Online Interaction".**
  2026 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2026.3666890)
  Yewei Guan, Jiarong Huo, Ye Yuan, Hua Guo, Jin Tan

- **Concretely-Efficient Multi-Key Homomorphic Secret Sharing and Applications.**
  2026 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00004)
  Srini Devadas, Geoffroy Couteau, Kaiwen He, Sacha Servan-Schreiber

- **Client-Server Homomorphic Secret Sharing in the CRS Model.**
  2026 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_3)
  Geoffroy Couteau, Aditya Hegde, Lawrence Roy, Lalita Devadas, Abhishek Jain, Damiano Abram, Sacha Servan-Schreiber

- **Broadcast-Optimal Secure Computation from Black-Box Oblivious Transfer.**
  2026 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-95-5116-3_5)
  Luisa Siniscalchi, Michele Ciampi, Divya Ravi, Yu Xia

- **Breaking the $\\varOmega (\|C\|\\kappa )$ Barrier on Garbled Circuit Size in the Random Oracle Model.**
  2026 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-032-35418-1_18)
  Junru Li, Yifan Song

- **Beyond the Output: Inference Attacks on Private Set Union and Multi-Key Private Matching.**
  2026 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2026-0155)
  Francesca Falzon, Tianxin Tang, Kenneth G. Paterson, Andrea Raguso

- **Approx-PSI: Efficient Differentially Private Set Intersection-Based Analysis.**
  2026 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2025.3629820)
  Jian Long, Ziyuan Liang, Zhan Qin, Chao Li, Fan Zhang

- **Actively Secure MPC with O(\|C\|) Computation and Communication via CRT.**
  2026 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-032-35418-1_7)
  Daniel Escudero, Alexander Bienstock, Antigoni Polychroniadou

- **A Construction of Evolving k-Threshold Secret Sharing Scheme over A Polynomial Ring.**
  2026 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-95-5125-5_1)
  Sian-Jheng Lin, Xianhong Xie, Hongru Cao, Qi Cheng, Nenghai Yu, Yunghsiang Sam Han

### 2025

- **A New Approach to Large Party Beaver-Style MPC with Small Computational Overhead**
  2025-12-22 · MPC · [IACR ePrint](https://eprint.iacr.org/2025/2305)
  Aayush Jain, Huijia Lin, Nuozhou Sun

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) enables $N$ parties to jointly evaluate any function over their private inputs while preserving confidentiality. While decades of research have produced concretely efficient protocols for small to moderate numbers of participants, scaling MPC to thousands of parties remains a central challenge. Most of the existing approaches either incur per-party costs linear in $N$, due to pairwise computations, or rely on heavy cryptographic tools such as homomorphic encryption, which introduces prohibitive overheads when evaluating Boolean circuits. In this work, we introduce a new lightweight approach to designing semi-honest MPC protocols with per-party, per-gate computation and communication costs that are independent of $N$. Our construction leverages the Sparse Learning Parity with Noise (Sparse LPN) assumption in the random oracle model to achieve per-gate costs of $O(k^2 \cdot c(\lambda))$ computation and $O(c(\lambda))$ communication, where $k$ is the sparsity parameter for the Sparse LPN assumption and $c(\lambda)$ is an arbitrarily small super-constant in the security parameter $\lambda$. Assuming Sparse LPN remains hard for any super-constant sparsity, this yields the first semi-honest MPC protocol in the dishonest-majority setting with per-party, per-gate costs bounded by an arbitrarily small super-constant overhead in $\lambda$. Structurally, our MPC instantiates a Beaver-style MPC with the required correlations generated efficiently. Departing from prior approaches that generate Beaver triples either silently (Boyle et al., 2019; 2020; 2022) or through homomorphic computation (Damgård et al., 2012), our focus is on efficiently generating a weaker correlation. In particular, using Sparse LPN we show that if we relax the correctness requirement in generating random Beaver triples to permit a tunably small inverse-polynomial error probability, such triples can be silently generated with arbitrarily small super-constant per-party computation. We then show that such correlations can be used in an efficient online phase similar to Beaver&#x27;s protocol (with a tiny super-constant factor blow-up in communication).

  匹配依据：MPC: secure multi party computation

  </details>

- **Linear codes over a mixed-alphabet ring and their Gray images with applications to projective and locally repairable codes**
  2025-12-08 · MPC · [arXiv](https://arxiv.org/abs/2512.07343)
  Leijo Jose, Lavanya G., Anuradha Sharma

  <details><summary>摘要 / Abstract</summary>

  Let $m \geq 2$ be an integer, and let $\mathbb{F}_q$ be the finite field of prime power order $q.$ Let $\mathcal{R}=\frac{\mathbb{F}_q[u]}{\langle u^2 \rangle}\times \mathbb{F}_q$ be the mixed-alphabet ring, where $\frac{\mathbb{F}_q[u]}{\langle u^2 \rangle}$ is the quasi-Galois ring with maximal ideal $\langle u\rangle$ of nilpotency index $2$ and residue field $\mathbb{F}_q.$ In this paper, we construct four infinite families of linear codes over the ring $\frac{\mathbb{F}_q[u]}{\langle u^2 \rangle}$ whose defining sets are certain non-empty subsets of $\mathcal{R}^m$ associated with three simplicial complexes of $\mathbb{F}_q^m,$ each possessing a single maximal element. We explicitly determine the parameters and Lee weight distributions of these codes. We also study their Gray images and identify several infinite families of few-weight codes over $\mathbb{F}_q,$ as well as an infinite family of minimal, near-Griesmer and distance-optimal codes over $\mathbb{F}_q.$ We also observe that their Gray images are self-orthogonal codes for $q=2$ or $3.$ We determine spanning matrices of these codes. Leveraging this result, we provide two constructions of infinite families of projective few-weight codes over $\mathbb{F}_q$ with new parameters. As an application of our newly constructed minimal codes over $\mathbb{F}_q,$ we examine the minimal access structures of Masseys secret sharing schemes based on their duals and determine the number of dictatorial participants in these schemes. Finally, we investigate the locality properties of our newly constructed projective codes and show that these codes have locality either $2$ or $3.$ As a consequence, we obtain four infinite families of $q$-ary locally repairable codes (LRCs) with locality $2,$ and two infinite families of binary LRCs with locality $3.$

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Fully Distributed Gaussian Process Regression**
  2025-12-05 · MPC · [arXiv](https://arxiv.org/abs/2512.05473)
  Yeongjun Jang, Kaoru Teranishi, Jihoon Suh, Takashi Tanaka

  <details><summary>摘要 / Abstract</summary>

  Although distributed Gaussian process regression (GPR) enables multiple agents to jointly learn a model of the target function, its collaborative nature poses a risk of private data leakage. To address this, we propose a privacy-preserving fully distributed GPR protocol based on secure multi-party computation, which hides each agent&#x27;s individual contribution from semi-honest coalitions of bounded size, beyond what is implied by the aggregated value. Building upon a secure distributed average consensus algorithm, it guarantees that each agent&#x27;s local model practically converges to the same global model obtained by the standard distributed GPR. Formal privacy guarantees are established within the simulation based security paradigm. The protocol is further extended to privacy-preserving optimization of kernel hyperparameters, which is critical yet often overlooked in the literature. Experimental results demonstrate the effectiveness and practical applicability of the proposed method.

  匹配依据：MPC: secure multi party computation

  </details>

- **Game-Theoretically Fair Distributed Coin Tossing With Private Preferences**
  2025-12-02 · MPC · [IACR ePrint](https://eprint.iacr.org/2025/2190)
  Pedro Branco, Pratik Soni, Sri AravindaKrishnan Thyagarajan, Ke Wu

  <details><summary>摘要 / Abstract</summary>

  Secure coin-tossing is typically modeled as an input-less functionality, where parties with no private inputs jointly generate a fair coin. In the dishonest majority setting, however, a strongly fair coin-tossing protocol is impossible. To circumvent this barrier, recent work has adopted the weaker notion of game-theoretic fairness, where adversaries are rational parties with preferences for specific outcomes, seeking to bias the coin in their favor. Yet these preferences may encode secret information, making prior protocols that assume preferences are public, fundamentally incompatible with privacy. We initiate a comprehensive study of privacy-preserving game-theoretically fair coin-tossing, where the preferences of honest parties remain private. We propose a simulation-based security framework and a new ideal functionality that reconciles both preference-privacy and game-theoretic fairness. A key ingredient is a certifying authority that authenticates each party’s preference and publishes only aggregate statistics, preventing misreporting while hiding parties&#x27; preferences. The functionality guarantees that every honest party receives an output: either a uniform coin; or, if an adversary deviates, a coin that strictly decreases the adversarial coalition&#x27;s expected utility. Within this framework, we construct a protocol realizing our ideal functionality under standard cryptographic assumptions that works for both binary and general $m$-sided coin-tossing. Our schemes tolerate the same optimal (or nearly optimal) corruption thresholds as the best known protocols with public preferences (Wu-Asharov-Shi, EUROCRYPT &#x27;22; Thyagarajan-Wu-Soni, CRYPTO &#x27;24). Technically, our protocols combine authenticated preferences with an anonymous communication layer that decouples identities from preference-dependent actions, together with a deviation-penalty mechanism that enforces game-theoretic fairness. Our work is the first to reconcile game-theoretic fairness with preference privacy, offering new definitional tools and efficient protocols for rational multi-party computation in dishonest majority settings.

  匹配依据：MPC: multi party computation

  </details>

- **Improved Robust Secret-Sharing for Honest-Majority Preprocessing-MPC**
  2025-11-21 · MPC · [IACR ePrint](https://eprint.iacr.org/2025/2135)
  Charanjit S. Jutla, Nathan Manohar, Arnab Roy

  <details><summary>摘要 / Abstract</summary>

  We design a novel robust secret-sharing scheme in the honest-majority setting for $n$ parties that allows constant communication per opening per party when amortized over $\Theta(n)$ simultaneous openings. We attain this scheme by a novel application of list decoding of folded Reed-Solomon codes. This was stated as an open problem by Escudero and Fehr (2023), who could obtain this amortized complexity only for $\Theta(n^2)$ simultaneous openings. Additionally, the dealing of such shares for a random value in a finite field $\mathbb{F}$ can itself be done using an honest-majority MPC protocol using only $O(n^2)$ multiplications between Shamir-shared values. This allows us to build an offline-online fully-secure (GOD) honest-majority MPC protocol, which has a fast online stage with amortized communication cost only $O(n)$ per multiplication gate (assuming the circuit has width $\Omega(n)$) and with no additional overhead, and an offline preprocessing stage with incremental communication cost only $O(n^3)$ per multiplication gate. This improves the previous best protocol in this setting by Escudero and Fehr (2023), which required the circuit to have width $\Omega(n^2)$. Further, the earlier scheme had an incremental preprocessing cost of $O(n^4)$ per multiplication gate. Due to requiring non-responsive rounds, the online stage of these protocols may still be concretely far less efficient than the online stage of the offline-online BGW protocol. Since the BGW protocol only provides security against fewer than $n/3$ malicious parties, we also devise a novel MPC protocol that boosts the BGW protocol&#x27;s correctness threshold to $n/2$, while maintaining privacy and robustness thresholds at $n/3$, and with minimal online overhead. This is useful in applications, such as elections and auctions, where certification of a correct result is paramount. To achieve this correctness against fewer than $n/2$ malicious parties and to keep the pre-processing cost low, we use our novel robust honest-majority secret-sharing scheme, but only once during a final SPDZ-style attestation.

  匹配依据：MPC: secret sharing

  </details>

- **Batched and Packed (Publicly) Verifiable Secret Sharing: A Unified Framework and Applications**
  2025-10-30 · MPC · [IACR ePrint](https://eprint.iacr.org/2025/2018)
  Shahla Atapoor, Karim Baghery, Georgio Nicolas, Robi Pedersen, Jannik Spiessens

  <details><summary>摘要 / Abstract</summary>

  Verifiable Secret Sharing (VSS) allows a dealer to distribute a secret among $n$ parties so that each can verify their share&#x27;s validity, and any qualified subset can reconstruct the secret. Publicly Verifiable Secret Sharing (PVSS) extends VSS by enabling anyone to verify the correctness of distributed shares. Both VSS and PVSS schemes are core building blocks in many cryptographic applications. We introduce a $k$-batched and $l$-packed extension of $\Pi$, a unified framework from PKC 2025 for Shamir-based computational VSS in the synchronous setting with optimal resilience. Our framework enables the sharing and verification of $l\times k$ secrets in a single protocol execution, offering a tunable trade-off between efficiency and robustness: the $k$-batched, non-packed variant ($l=1$) improves performance while maintaining optimal resilience, whereas the $k$-batched, $l$-packed variant achieves even greater efficiency at the cost of slightly reduced fault tolerance. Using this framework, we construct several Batched and Packed (BP) VSS and PVSS schemes that significantly reduce both computational and communication costs for the dealer and parties. When sharing many secrets, two of our VSS schemes and our PVSS scheme perform almost as efficiently as plain Shamir sharing. For example, when sharing more than 100 secrets, the overhead of our hash-based BP-VSS is below 3%, for our BP-VSS with information-theoretic privacy it remains around 8%, and for our BP-PVSS it is under 1%. These results show that verifiability in Shamir secret sharing can be achieved in post-quantum and large-scale settings with negligible overhead for the dealer. Our proposed BP-PVSS scheme is the first that can achieve these properties and outperforms existing state-of-the-art protocols. We discuss several applications and, as a concrete case study, use our BP-PVSS scheme to revisit the ALBATROSS randomness generation protocol from ASIACRYPT 2020, yielding a more efficient variant.

  匹配依据：MPC: secret sharing

  </details>

- **Single-Shuffle Full-Open Card-Based Secure Computation Protocols for Any Function**
  2025-10-20 · MPC · [arXiv](https://arxiv.org/abs/2510.17308)
  Reo Eriguchi, Kazumasa Shinagawa

  <details><summary>摘要 / Abstract</summary>

  A card-based secure computation protocol is a method for $n$ parties to compute a function $f$ on their private inputs $(x_1,\ldots,x_n)$ using physical playing cards, in such a way that the suits of revealed cards leak no information beyond the value of $f(x_1,\ldots,x_n)$. A \textit{single-shuffle full-open} protocol is a minimal model of card-based secure computation in which, after the parties place face-down cards representing their inputs, a single shuffle operation is performed and then all cards are opened to derive the output. Despite the simplicity of this model, the class of functions known to admit single-shuffle full-open protocols has been limited to a few small examples. In this work, we prove for the first time that every function admits a single-shuffle full-open protocol. We present two constructions that offer a trade-off between the number of cards and the complexity of the shuffle operation. These feasibility results are derived from a novel connection between single-shuffle full-open protocols and a cryptographic primitive known as \textit{Private Simultaneous Messages} protocols, which has rarely been studied in the context of card-based cryptography. We also present variants of single-shuffle protocols in which only a subset of cards are revealed. These protocols reduce the complexity of the shuffle operation compared to existing protocols in the same setting.

  匹配依据：MPC: secure computation

  </details>

- **Authenticated Garbling with Tensor Gates**
  2025-10-04 · MPC · [IACR ePrint](https://eprint.iacr.org/2025/1831)
  Nakul Khambhati, Turan Vural, David Heath, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  Authenticated garbling (Wang et al., CCS&#x27;17) is the leading framework for achieving constant-round maliciously secure 2PC, achieving total communication comparable to protocols in the semi-honest setting. In the semi-honest setting, the one-hot garbling scheme of Heath and Kolesnikov (CCS&#x27;21) supports tensor gates $\vec x \otimes \vec y$, for $\vec x \in \{0,1\}^n$ and $\vec y \in \{0,1\}^m$, in $O(n+m)\kappa$ bits, versus $O(nm)\kappa$ for an AND-gate-based garbling. Extending this improvement to the malicious setting has remained open. We present two authenticated garbling protocols that efficiently handle tensor gates. Our first protocol minimizes garbled circuit size, matching the size of semi-honest one-hot garbling; all additional overhead is confined to preprocessing. We also design a custom preprocessing protocol for efficiently generating random authenticated tensor triples, proved secure assuming only a circular correlation robust hash function and base OTs. Our second protocol minimizes total communication via compressed (PCG-style) preprocessing. We construct an authenticated variant of one-hot garbling where the additional overhead in garbled-circuit size as compared to the semi-honest garbling scales with tensor-gate input length rather than output length. As in the semi-honest case, tensor gates are restricted to inputs of length $O(\log \kappa)$ and arbitrary-length tensor products are handled by tiling multiple short input gates. This yields an $O(\log \kappa)$ factor reduction in communication for general tensor products compared to previous state-of-the-art authenticated garbling protocols, with concrete improvements in communication and runtime for practical workloads such as integer and matrix multiplication within an authenticated garbled circuit.

  匹配依据：MPC: garbled circuit, garbling protocols, garbling scheme

  </details>

- **Going Faster: Privacy-Preserving Shortest paths from Start to End (Extended Version)**
  2025-10-01 · MPC · [IACR ePrint](https://eprint.iacr.org/2025/1794)
  Vincent Ehrmanntraut, Ulrike Meyer

  <details><summary>摘要 / Abstract</summary>

  Finding shortest paths in graphs is a fundamental combinatorial optimization problem with numerous applications, e.g., in graph centrality measures, computational biology, and business process analysis. To address privacy constraints in such applications, Secure Multi-Party Computation (SMPC) protocols can compute the lengths of shortest paths on secret-shared graphs. Many such protocols have been proposed in the past, but they only compute the lengths of the shortest paths and not the paths themselves. In this paper, we close this gap by proposing two SMPC protocols that output secret-shared shortest paths. The first composes sub-protocols to calculate predecessors, to follow them, and to reorder wrongly positioned padding. Our second protocol optimizes the predecessor-following by decomposing it into sub-functionalities and proposing new sub-protocols for each. Further, the padding-reorder is replaced by a graph transformation. We evaluate our protocols across multiple network and security settings. Our optimized predecessor-following is up to 23 times faster than prior art, and our graph transformation is orders of magnitude faster than the padding-reorder. Overall, our second protocol is 5% to 49% faster than the first protocol due to the predecessor-calculation dominating the runtime on large graphs. Finally, we introduce a novel demultiplex protocol that, in fast networks, outperforms prior protocols on vector sizes up to 500, and on all evaluated vector sizes in slow networks. Due to the ubiquity of demultiplexes, this protocol is of independent interest.

  匹配依据：MPC: secure multi party computation

  </details>

- **WISCH: Efficient data signing via correlated signatures**
  2025-09-12 · MPC · [IACR ePrint](https://eprint.iacr.org/2025/1650)
  Ariel Futoransky, Ramses Fernandez, Emilio Garcia, Gabriel Larotonda, Sergio Demian Lerner

  <details><summary>摘要 / Abstract</summary>

  We present WISCH, a commit-reveal protocol that combines compact aggregate signatures with hash-based commitments to enable selective disclosure of correlated data in multiparty computation. The protocol separates an on-chain verification core from off chain preparation, so that verification cost depends only on the number of openings, not on the size of the underlying message space. This yields asymptotic efficiency: on-chain cost grows linearly in the number of revealed items and is independent of the ambient domain, while the per-byte overhead decreases with the message granularity. Security is established via a simulation-based proof in a UC framework with an ideal ledger functionality, in the algebraic group and global random-oracle models, under standard assumptions for discrete-log-based signatures and hash-based commitments. Thus WISCH provides selectively verifiable revelation with succinct on-chain checks and provable security guarantees.

  匹配依据：MPC: multiparty computation

  </details>

- **Succinct Oblivious Tensor Evaluation and Applications: Adaptively-Secure Laconic Function Evaluation and Trapdoor Hashing for All Circuits**
  2025-08-13 · MPC · [arXiv](https://arxiv.org/abs/2508.09673)
  Damiano Abram, Giulio Malavolta, Lawrence Roy

  <details><summary>摘要 / Abstract</summary>

  We propose the notion of succinct oblivious tensor evaluation (OTE), where two parties compute an additive secret sharing of a tensor product of two vectors $\mathbf{x} \otimes \mathbf{y}$, exchanging two simultaneous messages. Crucially, the size of both messages and of the CRS is independent of the dimension of $\mathbf{x}$. We present a construction of OTE with optimal complexity from the standard learning with errors (LWE) problem. Then we show how this new technical tool enables a host of cryptographic primitives, all with security reducible to LWE, such as: * Adaptively secure laconic function evaluation for depth-$D$ functions $f:\{0, 1\}^m\rightarrow\{0, 1\}^\ell$ with communication $m+\ell+D\cdot \mathrm{poly}(λ)$. * A trapdoor hash function for all functions. * An (optimally) succinct homomorphic secret sharing for all functions. * A rate-$1/2$ laconic oblivious transfer for batch messages, which is best possible. In particular, we obtain the first laconic function evaluation scheme that is adaptively secure from the standard LWE assumption, improving upon Quach, Wee, and Wichs (FOCS 2018). As a key technical ingredient, we introduce a new notion of \emph{adaptive lattice encodings}, which may be of independent interest.

  匹配依据：MPC: oblivious transfer, secret sharing

  </details>

- **TLShare: Private Authenticated MPC and FHE Inputs Over TLS**
  2025-08-06 · MPC · [IACR ePrint](https://eprint.iacr.org/2025/1434)
  Manuel B. Santos, Dimitris Mouris, Xiang Xie, Miguel de Vega, Andrei Lapets

  <details><summary>摘要 / Abstract</summary>

  Transport Layer Security (TLS) is the backbone of the web, allowing clients to establish secure and private channels with servers. DECO (CCS&#x27;20) and follow-up works proposed protocols that enable proving the provenance of a TLS response, i.e., that a payload came from a particular server, without needing server-side modifications. Unfortunately, these works are limited to proving Boolean statements over the payload (e.g., age $\ge$ 18) and cannot combine payloads from multiple clients. We introduce TLShare, a framework that extracts authenticated data from a TLS connection and imports it into secure multiparty computation (MPC) or fully homomorphic encryption (FHE), without requiring server-side changes or exposing client credentials. Unlike prior work, TLShare allows the payload itself, not just a predicate about it, to serve as private input to secure downstream computation. TLShare supports combining verifiable inputs across multiple clients and servers, enabling new applications such as privacy-preserving financial risk assessment and collaborative analytics. We design three protocols for TLShare: one for MPC using verifiable secret sharing, and two for FHE using interactive and non-interactive zero-knowledge proofs, each ensuring input authenticity, integrity, and end-to-end privacy. We evaluate all three protocols of TLShare over both LAN and WAN settings, comparing their trade-offs and demonstrating their practicality.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Collusion-Safe Proxy Re-Encryption**
  2025-08-05 · MPC · [IACR ePrint](https://eprint.iacr.org/2025/1423)
  Haotian Yin, Jie Zhang, Wanxin Li, Yuji Dong, Eng Gee Lim, Dominik Wojtczak

  <details><summary>摘要 / Abstract</summary>

  Proxy re-encryption is a cryptographic scheme enabling a delegator (user $i$) to delegate its decryption right to a valid delegatee (user $j$) through a proxy, who cannot extract any information about the message during the procedure. An important security notion is the security against collusion between the proxy and the delegatee. In this case, the adversary has the secret key of the delegatee, $\mathsf{sk}_j$, and the re-encryption key, $\mathsf{rk}_{i\to j}$. The master secret security is first formalised by Ateniese et al. (NDSS&#x27;05) to capture the secrecy of $i$&#x27;s secret key during collusion. This notion was further formalised by Zhou et al. (ASIACRYPT&#x27;23) as the indistinguishability of re-encrypted ciphertext against chosen-message attacks, called collusion safety, which implies the master secret security. In this paper, we find that a PRE scheme is not master secret secure as they claimed, and many other schemes were not master secret secure. Then, we propose a generic construction to achieve collusion safety at the cost of doubling the key size from the IND-CPA secure PRE, enjoying a much better generality and efficiency than the existing technique by secret sharing.

  匹配依据：MPC: secret sharing

  </details>

- **The Matrix Subcode Equivalence problem and its application to signature with MPC-in-the-Head**
  2025-07-21 · MPC · [arXiv](https://arxiv.org/abs/2507.15377)
  Magali Bardet, Charles Brion, Philippe Gaborit, Mercedes Haiech, Romaric Neveu

  <details><summary>摘要 / Abstract</summary>

  Nowadays, equivalence problems are widely used in cryptography, most notably to establish cryptosystems such as digital signatures, with MEDS, LESS, PERK as the most recent ones. However, in the context of matrix codes, only the code equivalence problem has been studied, while the subcode equivalence is well-defined in the Hamming metric. In this work, we introduce two new problems: the Matrix Subcode Equivalence Problem and the Matrix Code Permuted Kernel Problem, to which we apply the MPCitH paradigm to build a signature scheme. These new problems, closely related to the Matrix Code Equivalence problem, ask to find an isometry given a code $C$ and a subcode $D$. Furthermore, we prove that the Matrix Subcode Equivalence problem reduces to the Hamming Subcode Equivalence problem, which is known to be NP-Complete, thus introducing the matrix code version of the Permuted Kernel Problem. We also adapt the combinatorial and algebraic algorithms for the Matrix Code Equivalence problem to the subcode case, and we analyze their complexities. We find with this analysis that the algorithms perform much worse than in the code equivalence case, which is the same as what happens in the Hamming metric. Finally, our analysis of the attacks allows us to take parameters much smaller than in the Matrix Code Equivalence case. Coupled with the effectiveness of \textit{Threshold-Computation-in-the-Head} or \textit{VOLE-in-the-Head}, we obtain a signature size of $\approx$ 4 800 Bytes, with a public key of $\approx$ 275 Bytes. We thus obtain a reasonable signature size, which brings diversity in the landscape of post-quantum signature schemes, by relying on a new hard problem. In particular, this new signature scheme performs better than SPHINCS+, with a smaller size of public key + signature. Our signature compares also well with other signature schemes: compared to MEDS, the signature is smaller, and we reduced the size of the sum of signature and public key by a factor close to 5. We also obtain a signature size that is almost half the size of the CROSS signature scheme.

  匹配依据：MPC: mpc (context)

  </details>

- **Topological Mixed States: Phases of Matter from Axiomatic Approaches**
  2025-06-04 · MPC · [arXiv](https://arxiv.org/abs/2506.04221)
  Tai-Hsuan Yang, Bowen Shi, Jong Yeon Lee

  <details><summary>摘要 / Abstract</summary>

  For closed quantum systems, topological orders are understood through the equivalence classes of ground states of gapped local Hamiltonians. The generalization of this conceptual paradigm to open quantum systems, however, remains elusive, often relying on operational definitions without fundamental principles. Here, we fill this gap by proposing an approach based on three axioms: ($i$) local recoverability, ($ii$) absence of long-range correlations, and ($iii$) spatial uniformity. States that satisfy these axioms are fixed points; requiring the axioms only after coarse-graining promotes each fixed point to an equivalence class, i.e., a phase, presenting the first step towards the axiomatic classification of mixed-state phases of matter: mixed-state bootstrap program. From these axioms, a rich set of topological data naturally emerges; importantly, these data are robust under relaxation of axioms. For example, each topological mixed state supports locally indistinguishable classical and/or quantum logical memories with distinct responses to topological operations. These data label distinct mixed-state phases, allowing one to distinguish them. We further uncover a hierarchy of secret-sharing constraints: in non-Abelian phases, reliable recovery-even of information that looks purely classical-demands a specific coordination among spatial subregions, a requirement different across non-Abelian classes. This originates from non-Abelian fusion rules that can stay robust under decoherence. Finally, we performed large-scale numerical simulations to corroborate stability: weakly decohered fixed points respect the axioms once coarse-grained. These results lay the foundation for a systematic classification of topological states in open quantum systems.

  匹配依据：MPC: secret sharing

  </details>

- **An Efficient Framework for Collusion Resistant Multiparty FHE**
  2025-05-27 · MPC · [IACR ePrint](https://eprint.iacr.org/2025/965)
  Robin Jadoul, Barry van Leeuwen, Oliver Zajonc

  <details><summary>摘要 / Abstract</summary>

  Multiparty fully homomorphic encryption (MPFHE) is a generalization of (multi-key) fully homomorphic encryption ((MK)FHE) that lives on the cusp between multiparty computation (MPC) and FHE, enabling a computation over encrypted data using multiple keys. However, contrary to MKFHE, it seeks to reduce the noise inflation based on the number of parties by allowing the parties to first compute shared data in MPC before executing the computation in FHE. However, many works use specific constructions, e.g. Chang-Li, Koirala et. al., and Ma et. al., reliant on the behaviour of a particular scheme and do not consider security against colluding servers and parties, e.g. Passelègue-Stehlé, Okada-Takagi, and Mouchet et. al. In this work we present a new framework that is secure against collusion between servers and parties and allows the use of a broad spectrum of MPC and FHE protocols, while eliminating the noise inflation based on the participating number of parties. We then show a case study of this using the FINAL scheme and show that we reduce the required key material by 60­–99.9% compared to the MKFHE FINAL scheme, FINALLY, and 65–70% compared to the Park-Rovira scheme in all cases, and by up to 71% compared to the AKÖ scheme when there are 4 or more parties. Moreover, we reduce the bootstrapping time for the AKÖ, Park-Rovira, and KMS schemes by 75–99.7%.

  匹配依据：MPC: multiparty computation

  </details>

- **Optimistic, Signature-Free Reliable Broadcast and Its Applications**
  2025-05-05 · MPC · [arXiv](https://arxiv.org/abs/2505.02761)
  Nibesh Shrestha, Qianyu Yu, Aniket Kate, Giuliano Losa, Kartik Nayak, Xuechao Wang

  <details><summary>摘要 / Abstract</summary>

  Reliable broadcast (RBC) is a key primitive in fault-tolerant distributed systems, and improving its efficiency can benefit a wide range of applications. This work focuses on signature-free RBC protocols, which are particularly attractive due to their computational efficiency. Existing protocols in this setting incur an optimal 3 steps to reach a decision while tolerating up to $f &lt; n/3$ Byzantine faults, where $n$ is the number of parties. In this work, we propose an optimistic RBC protocol that maintains the $f &lt; n/3$ fault tolerance but achieves termination in just 2 steps under certain optimistic conditions--when at least $\lceil \frac{n+2f-2}{2} \rceil$ non-broadcaster parties behave honestly. We also prove a matching lower bound on the number of honest parties required for 2-step termination. We show that our latency-reduction technique generalizes beyond RBC and applies to other primitives such as asynchronous verifiable secret sharing (AVSS) and asynchronous verifiable information dispersal (AVID), enabling them to complete in 2 steps under similar optimistic conditions. To highlight the practical impact of our RBC protocol, we integrate it into Sailfish++, a new signature-free, post-quantum secure DAG-based Byzantine fault-tolerant (BFT) consensus protocol. Under optimistic conditions, this protocol achieves a commit latency of 3 steps--matching the performance of the best signature-based protocols. Our experimental evaluation shows that our protocol significantly outperforms existing post-quantum secure and signature-based protocols, even on machines with limited CPU resources. In contrast, signature-based protocols require high CPU capacity to achieve comparable performance. We have open-sourced our Rust implementation of Sailfish++ to facilitate reproducible results.

  匹配依据：MPC: secret sharing

  </details>

- **AuthOr: Lower Cost Privacy-Free Garbling of Arbitrary Boolean Circuits**
  2025-04-30 · MPC · [arXiv](https://arxiv.org/abs/2501.18387) · [IACR ePrint](https://eprint.iacr.org/2025/775)
  Osman Biçer, Ali Ajorian

  <details><summary>摘要 / Abstract</summary>

  Privacy-free garbling schemes of Frederiksen et al. (Eurocrypt ’15) are designed to satisfy only the authenticity criterion of Bellare et al. (ACM CCS ’12) and to be more efficient than full-fledged garbling schemes. In this work, we improve the state-of-the-art privacy-free version of half-gates (HG) garbling of Zahur et al. (Crypto ’15) by allowing an AND gate to be garbled with zero ciphertexts whenever at least one of its input wires is freely settable by the garbler. Our full solution, AuthOr, then combines the ideas from the information-theoretic garbling of Kondi and Patra (Crypto ’17) with the improved HG-based scheme we obtain. AuthOr has a lower communication cost (i.e., garbled-circuit size) than HG garbling without any additional security assumptions. Theoretically, AuthOr’s garbled-circuit size reduction over HG garbling ranges from 0% to 100%, with the exact improvement depending on the circuit structure. We have implemented our scheme and evaluated it on various circuits constructed by independent researchers. Our experimental results show that, in practice, the garbled-circuit size reduction can reach roughly 98%.

  匹配依据：MPC: garbled circuit, garbling schemes

  </details>

- **One-Step Schnorr Threshold Identification**
  2025-04-22 · MPC · [IACR ePrint](https://eprint.iacr.org/2025/722)
  Foteinos Mergoupis-Anagnou

  <details><summary>摘要 / Abstract</summary>

  Threshold cryptographic primitives have not been widely adopted in real-world distributed systems (i.e., beyond the closed committee model) presumably due to state-synchronization overhead and complex certification processes for the shareholders. These are both aspects of their overreliance on infrastructure, an assumption that is usually glossed over in their design. In this work, we propose OSST, a real-time threshold identification protocol that achieves non-interactivity and non-reliance on public shares by means of direct proof interpolation. Given a Shamir $(n, t)$-shared secret $x$, the proposed scheme allows any $t^* \ge t$ (but no less) shareholders to prove over designated communication channels that their key shares interpolate to $x$ without revealing any information beyond that. Provers do not engage in distributed computations, sending their packets to the verifier asynchronously; conversely, verifiers need only know the combined public key $y \equiv g ^ x$, without need to pre-validate and register the individual member identities. The protocol is intended for use in permissionless or unmanaged meshes that lack both overlay networks and trust infrastructure or governance, a use case space that has been tacitly neglected as &#x27;&#x27;niche&#x27;&#x27; by the current mainstream. No publicly verifiable setup is required beyond distributing $x$ according to Shamir&#x27;s secret sharing (or equivalent distributed key generation scheme) and advertising its public counterpart; in particular, the protocol is intended to be secure against impersonation without relying on the auditability of any advertised public shares. We provide evidence that this has good chances to hold true by giving a reasonably restricted security proof in the random oracle model under the one-more discrete-logarithm (OMDL) hardness assumption.

  匹配依据：MPC: secret sharing

  </details>

- **On the (In)security of Approximate Computation Protocols from CKKS**
  2025-03-03 · MPC · [IACR ePrint](https://eprint.iacr.org/2025/395)
  Intak Hwang, Yisol Hwang, Miran Kim, Dongwon Lee, Yongsoo Song

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation (MPC) enables collaborative and privacy-preserving computation over private inputs. Recent advances in Homomorphic Encryption (HE), particularly the CKKS scheme, have significantly improved the practicality of secure computation, making it suitable for real-world applications involving approximate arithmetic. However, the inherent errors introduced by CKKS pose substantial challenges in the design and analysis of CKKS-based secure computation protocols. In this work, we investigate the correctness and security of existing CKKS-based MPC protocols. Most prior constructions rely on the noise smudging technique, in which each party independently adds exponentially large noise to the output to guarantee the security of the protocol. However, we show that this approach does not achieve standard simulation-based security for MPC. To address this limitation, we apply an alternative method, called collaborative sampling, in which all participating parties jointly generate additive shares of the smudging noise. We consider both asymmetric two-party protocols between a client and a server, and symmetric multiparty protocols among mutually distrusting parties. For each setting, we present concrete protocol constructions based on collaborative sampling, explicitly define the corresponding ideal functionalities, and provide formal security proofs. We further provide concrete constructions and implementations of collaborative sampling protocols. As an alternative perspective, we show that existing protocols, despite failing to achieve standard simulation-based security, still satisfy a weaker security notion called liberal security for approximate MPC protocols.

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **Accountable Verifiable Secret Sharing and Applications**
  2025-02-21 · MPC · [IACR ePrint](https://eprint.iacr.org/2025/318)
  Karim Baghery, Ehsan Ebrahimi, Omid Mirzamohammadi, Mahdi Sedaghat

  <details><summary>摘要 / Abstract</summary>

  Verifiable Secret Sharing (VSS) ensures consistent sharing and correct reconstruction, but does not identify the shareholders involved. Traceable Secret Sharing (TSS) expands secret sharing with two guarantees: $\textit{traceability}$, which identifies the makers of a reconstruction box through black-box queries; and $\textit{non-imputability}$, which prevents false accusations against honest shareholders. However, full traceability is practically expensive: existing Shamir-based schemes require multiple carefully chosen queries to a $\textit{stateless}$ reconstruction box. Moreover, Goyal et al. (ePrint 2025/1980) show that the strongest form of black-box tracing is incompatible with simultaneously achieving non-imputability and tracer secrecy. We introduce $\textit{Accountable VSS}$ (Acc-VSS), a practical extension of VSS that achieves the next-best goal: $\textit{accountability}$, a strict relaxation of traceability requiring that (i) the contributors to every accepted reconstruction be publicly identifiable from its transcript with a $\textit{single}$ query, and (ii) no honest shareholder be falsely accused, even by an adversary holding all other shares. Accountability thus replaces black-box, multi-query tracing with a transcript check executable by any external verifier or smart-contract judge. In this paper, (i) we give a generic transformation from any computationally secure Shamir-based VSS to Acc-VSS, adding only one field element per share; it uses a long-term identity secret to each share and a conjunctive NIZK to bind partial reconstructions to the shareholder and the dealer&#x27;s commitments; (ii) we instantiate it with Feldman and Pedersen VSS and prove the security of both schemes; (iii) we prove a self-contained $\textit{single-query}$ impossibility lemma motivating our relaxation; and (iv) we show how Acc-VSS uniformly yields accountable threshold ElGamal decryption, Schnorr/FROST signing, and distributed key generation. For the benchmarked VSS-based threshold-decryption protocol, accountability adds at most $20.3\%$ end-to-end overhead for $n=20$ and less than $6\%$ for $n=100$. Encrypted mempools, end-to-end-verifiable e-voting tallies, and validator-slashing in proof-of-stake systems all reduce to this framework.

  匹配依据：MPC: secret sharing

  </details>

- **Π: A Unified Framework for Computational Verifiable Secret Sharing.**
  2025 · MPC · [PKC](https://doi.org/10.1007/978-3-031-91829-2_4)
  Karim Baghery

- **ømega (1/λ )-Rate Boolean Garbling Scheme from Generic Groups.**
  2025 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-032-01884-7_16)
  Geoffroy Couteau, Aditya Hegde, Naman Kumar, Carmit Hazay

- **Wave Hello to Privacy: Efficient Mixed-Mode MPC using Wavelet Transforms.**
  2025 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2025-0083)
  Sameer Wagh, Mehmet Ugurbil, Miguel de Vega, José Reis, Ryan Henry

- **Verifiable Secret Sharing from Symmetric Key Cryptography with Improved Optimistic Complexity.**
  2025 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-96-0941-3_4)
  Ignacio Cascudo, Daniele Cozzo, Emanuele Giunta

- **Verifiable Secret Sharing Simplified.**
  2025 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SP61157.2025.00046)
  Alin Tomescu, Zhuolun Xiang, Alexander Spiegelman, Sourav Das, Ling Ren, Benny Pinkas

- **Velox: Scalable Fair Asynchronous MPC from Lightweight Cryptography.**
  2025 · MPC · [ACM CCS](https://doi.org/10.1145/3719027.3765114)
  Chen-Da Liu-Zhang, Aniket Kate, Akhil Bandarupalli, Yifan Song, Daniel Pöllmann, Xiaoyu Ji

- **Updatable Private Set Intersection Revisited: Extended Functionalities, Deletion, and Worst-Case Complexity.**
  2025 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-96-0938-3_7)
  Saikrishna Badrinarayanan, Peihan Miao, Xinyi Shi, Ruida Zeng, Max Tromanhauser

- **Unclonable Secret Sharing.**
  2025 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-96-0947-5_5)
  Vipul Goyal, Prabhanjan Vijendra Ananth, Jiahui Liu, Qipeng Liu

- **Ultra-Fast Private Set Intersection From Efficient Oblivious Key-Value Stores.**
  2025 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2025.3557963)
  Shifeng Sun, Peng Tang, Weidong Qiu, Shouling Ji, Fei Tang, Guowei Ling

- **Towards Efficient and Practical Multi-party Computation under Inconsistent Trust in TEEs.**
  2025 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SP61157.2025.00185)
  Qi Wang, Xuanwei Hu, Rujia Li, Yi Liu

- **TinyLabels: How to Compress Garbled Circuit Input Labels, Efficiently.**
  2025 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-031-91095-1_9)
  Hanjun Li, Marian Dietz, Huijia Lin

- **Timed Secret Sharing.**
  2025 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-96-0941-3_5)
  Philipp Jovanovic, Aydin Abadi, Alireza Kavousi

- **The Round Complexity of Black-Box Post-quantum Secure Computation.**
  2025 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-032-01884-7_1)
  Rohit Chatterjee, Takashi Yamakawa, Xiao Liang, Omkant Pandey

- **The Meta-complexity of Secret Sharing.**
  2025 · MPC · [STOC](https://doi.org/10.1145/3717823.3718161)
  Oded Nir, Benny Applebaum

- **The Concrete Security of Two-Party Computation: Simple Definitions, and Tight Proofs for PSI and OPRFs.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-981-96-0938-3_11)
  Rishabh Ranjan, Doreen Riepel, Ali Aldakheel, Mihir Bellare

- **Strong Secret Sharing with Snitching.**
  2025 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-032-01884-7_10)
  Tomasz Lizurej, Jan Bormet, Marcin Mielniczuk, Stefan Dziembowski, Sebastian Faust

- **Split-State Non-malleable Codes and Secret Sharing Schemes for Quantum Messages.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-78017-2_3)
  Naresh Goud Boddu, João Ribeiro, Vipul Goyal, Rahul Jain

- **SoK: Computational and Distributed Differential Privacy for MPC.**
  2025 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2025-0023)
  Fredrik Meisingseth, Christian Rechberger

- **Simultaneous-Message and Succinct Secure Computation.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-91092-0_8)
  Elette Boyle, Akshayaram Srinivasan, Sacha Servan-Schreiber, Abhishek Jain

- **Silent Circuit Relinearisation: Sublinear-Size (Boolean and Arithmetic) Garbled Circuits from DCR.**
  2025 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-032-01884-7_14)
  Peter Scholl, Lawrence Roy, Pierre Meyer, Claudio Orlandi

- **SelectFormer in Data Markets: Privacy-Preserving and Efficient Data Selection for Transformers with Multi-Party Computation.**
  2025 · MPC · [ICLR](https://openreview.net/forum?id=2cF3f9t31y)
  Felix Xiaozhu Lin, Xu Ouyang, Yangfeng Ji

- **Secure and efficient transciphering for FHE-based MPC.**
  2025 · MPC · [TCHES](https://doi.org/10.46586/TCHES.V2025.I3.745-780)
  Pierrick Méaux, Clément Hoffmann, Antonio Guimarães, Diego F. Aranha

- **Secure Computation with Parallel Calls to 2-Ary Functions.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-78023-3_8)
  Akshayaram Srinivasan, Varun Narayanan, Shubham Vivek Pawar

- **Secret-Sharing Schemes for High Slices.**
  2025 · MPC · [TCC](https://doi.org/10.1007/978-3-031-78023-3_19)
  Or Lasri, Oriol Farràs, Oded Nir, Amos Beimel

- **Secret Sharing with Publicly Verifiable Deletion.**
  2025 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-031-91131-6_10)
  Benjamin Sela, Jonathan Katz

- **SHARK: Actively Secure Inference Using Function Secret Sharing.**
  2025 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SP61157.2025.00175)
  Rahul Sharma, Kanav Gupta, Nishanth Chandran, Divya Gupta, Jonathan Katz

- **SEAF: Secure Evaluation on Activation Functions with Dynamic Precision for Secure Two-Party Inference.**
  2025 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/guo-hao-seaf)
  Ximing Fu, Zhusen Liu, Zhaoqian Liu, Hao Guo

- **Rushing at SPDZ: On the Practical Security of Malicious MPC Implementations.**
  2025 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SP61157.2025.00176)
  Sabine Oechsner, Peter Scholl, Frederik Huss Nielsen, Alexander Kyster

- **Round-Optimal Black-Box Multiparty Computation from Polynomial-Time Assumptions.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-91092-0_12)
  Michele Ciampi, Luisa Siniscalchi, Hendrik Waldner, Rafail Ostrovsky

- **Reversible Data Hiding in Encrypted Images With Secret Sharing and Multivariate Linear Equation.**
  2025 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2025.3590551)
  Xianquan Zhang, Chunqiang Yu, Peng Liu, Xinpeng Zhang, Guoxiang Li, Zhenjun Tang

- **Reducing the Share Size of Weighted Threshold Secret Sharing Schemes via Chow Parameters Approximation.**
  2025 · MPC · [TCC](https://doi.org/10.1007/978-3-031-78023-3_17)
  Miquel Guiot, Oriol Farràs

- **Recurrent Private Set Intersection for Unbalanced Databases with Cuckoo Hashing and Leveled FHE.**
  2025 · MPC · [NDSS](https://www.ndss-symposium.org/ndss-paper/recurrent-private-set-intersection-for-unbalanced-databases-with-cuckoo-hashing-and-leveled-fhe/)
  Eduardo Chielle, Michail Maniatakos

- **Re-visiting Authorized Private Set Intersection: A New Privacy-Preserving Variant and Two Protocols.**
  2025 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2025-0041)
  Evangelia Anna Markatou, Francesca Falzon

- **Rate-1 Arithmetic Garbling From Homomorphic Secret Sharing.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-78023-3_3)
  Lawrence Roy, Peter Scholl, Pierre Meyer, Claudio Orlandi

- **QuietOT: Lightweight Oblivious Transfer with a Public-Key Setup.**
  2025 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-96-0888-1_7)
  Geoffroy Couteau, Srini Devadas, Lalita Devadas, Sacha Servan-Schreiber, Alexander Koch

- **Protecting Distributed Primitives Against Leakage: Equivocal Secret Sharing and more.**
  2025 · MPC · [Journal of Cryptology](https://doi.org/10.1007/S00145-024-09524-3)
  Mor Weiss, Muthuramakrishnan Venkitasubramaniam, Carmit Hazay

- **Private Set Union with Multiple Contributions.**
  2025 · MPC · [NeurIPS](http://papers.nips.cc/paper_files/paper/2025/hash/81a4bde3b5c6665dbd780b1fd577851f-Abstract-Conference.html)
  Ananda Theertha Suresh, Uri Stemmer, Travis Dick, Ziteng Sun, Alex Kulesza, Haim Kaplan

- **Private Set Intersection and other Set Operations in the Third Party Setting.**
  2025 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/yeo)
  Jason H. M. Ying, Foo Yee Yeo

- **Privacy-Preserving Authorized Set Matching via Dishonest Majority Multiparty Computation.**
  2025 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2025.3599183)
  Weidong Qiu, Liyao Xiang, Jinyong Shan, Fei Tang, Guowei Ling, Peng Tang, Shifeng Sun

- **Physical-Bit Leakage Resilience of Linear Code-Based Secret Sharing.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-91101-9_3)
  Hai H. Nguyen

- **Perfectly-Secure Multiparty Computation with Linear Communication Complexity over Any Modulus.**
  2025 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-96-0938-3_4)
  Daniel Escudero, Wenhao Wang, Yifan Song

- **Perfectly-Secure MPC with Constant Online Communication Complexity.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-78023-3_11)
  Xiaxi Ye, Yifan Song

- **PULSE: Parallel Private Set Union for Large-Scale Entities.**
  2025 · MPC · [ACM CCS](https://doi.org/10.1145/3719027.3765108)
  Ni Trieu, Jiahui Gao, Marina Blanton, Son Nguyen

- **POTA: A Pipelined Oblivious Transfer Acceleration Architecture for Secure Multi-Party Computation.**
  2025 · MPC · [TCHES](https://doi.org/10.46586/TCHES.V2025.I3.262-292)
  Yong Liu, Ninghui Sun, Qinfen Hao, Xiaolin Li, Yong Zhang, Hongwei Liu, Wei Yan

- **PM-ABE: Puncturable Bilateral Fine-Grained Access Control From Lattices for Secret Sharing.**
  2025 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2024.3431035)
  Debiao He, Mengxue Yang, Huaqun Wang

- **PIGEON: A High Throughput Framework for Private Inference of Neural Networks using Secure Multiparty Computation.**
  2025 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2025-0090)
  Murali Annavaram, Christopher Harth-Kitzerow, Rachit Rajat, Yongqin Wang, Georg Carle

- **On the Adaptive Security of Free-XOR-Based Garbling Schemes in the Plain Model.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-91095-1_8)
  Karen Azari, Chethan Kamath, Anasuya Acharya

- **New Upper Bounds for Evolving Secret Sharing via Infinite Branching Programs.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-78023-3_18)
  Bar Alon, Tamar Ben David, Eran Omri, Anat Paskin-Cherniavsky, Amos Beimel

- **NIZK Amplification via Leakage-Resilient Secure Computation.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-032-01907-3_15)
  Eliran Kachlon, Benny Applebaum

- **Multiparty Delegated Private Set Union With Efficient Updates on Outsourced Datasets.**
  2025 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2024.3419576)
  Heewon Chung, Myungsun Kim, Patrick Chulsoon Yang

- **Multi-Party Private Set Intersection With One-Round Online Interaction.**
  2025 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2025.3574993)
  Shengnan Zhao, Chuan Zhao, Qiuliang Xu, Yu Meng, Shan Jing, Shimeng Lu, Zhenxiang Chen

- **Multi-Key Homomorphic Secret Sharing.**
  2025 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-031-91092-0_1)
  Aditya Hegde, Geoffroy Couteau, Lalita Devadas, Sacha Servan-Schreiber, Abhishek Jain

- **More Efficient, Privacy-Enhanced, and Powerful Privacy-Preserving Feature Retrieval Private Set Intersection.**
  2025 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2025.3562695)
  Guowei Ling, Fei Tang, Peng Tang, Weidong Qiu, Jinyong Shan

- **Maliciously Secure Circuit Private Set Intersection via SPDZ-Compatible Oblivious PRF.**
  2025 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2025-0082)
  Changyu Dong, Linting Huang, Xiaojian Liang, Yaxi Yang, Hongyu Ren, Xiangfu Song, Jianying Zhou, Ye Dong

- **Lower Bounds for Garbled Circuits from Shannon-Type Information Inequalities.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-032-01884-7_19)
  Lawrence Roy, Jake Januzelli, Mike Rosulek

- **Leap: A Fast, Lattice-Based OPRF with Application to Private Set Intersection.**
  2025 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-031-91098-2_10)
  Daniel Kales, Omid Mir, Sebastian Ramacher, Lena Heimberger, Riccardo Lolato, Christian Rechberger

- **Labeled Private Set Intersection From Distributed Point Function.**
  2025 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2025.3550059)
  Kang Yang, Yu Yu, Qi Liu, Xiaojie Guo

- **Is MPC Secure? Leveraging Neural Network Classifiers to Detect Data Leakage Vulnerabilities in MPC Implementations.**
  2025 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SP61157.2025.00181)
  Wenjing Fang, Jin Tan, Lei Wang, Junming Ma, Lushan Song, Guopeng Lin, Weili Han, Xiaoning Du

- **Ironman: Accelerating Oblivious Transfer Extension for Privacy-Preserving AI with Near-Memory Processing.**
  2025 · MPC · [MICRO](https://doi.org/10.1145/3725843.3756025)
  Tianshi Xu, Runsheng Wang, Chenqi Lin, Zhaohui Chen, Kang Yang, Meng Li, Ling Liang, Mingyu Gao, Yufei Wang

- **Increasing the Resilience of Secure Multiparty Computation Using Security Modules.**
  2025 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2025.3552670)
  Lamya Abdullah, Felix C. Freiling, Dominique Schröder

- **Improved Universal Thresholdizer from Iterative Shamir Secret Sharing.**
  2025 · MPC · [Journal of Cryptology](https://doi.org/10.1007/S00145-024-09536-Z)
  Wonhee Cho, Jiseung Kim, Jung Hee Cheon

- **Improved Secure Two-party Computation from a Geometric Perspective.**
  2025 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/guo-hao-improved)
  Liqiang Peng, Lei Hu, Haiyang Xue, Weiran Liu, Hao Guo, Zhe Liu, Li Peng

- **How to Make Any Computational Secret Sharing Scheme Adaptively Secure.**
  2025 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-032-01884-7_11)
  George Lu, Brent Waters

- **Honest Majority MPC with Õ(\|C\|) Communication in Minicrypt.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-91092-0_16)
  Xiaxi Ye, Yifan Song

- **Honest Majority GOD MPC with O(sfdepth(C)) Rounds and Low Online Communication.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-981-96-0938-3_8)
  Daniel Escudero, Alexander Bienstock, Amit Agarwal, Ivan Damgård

- **Homomorphic Secret Sharing with Verifiable Evaluation.**
  2025 · MPC · [TCC](https://doi.org/10.1007/978-3-031-78023-3_20)
  Aarushi Goel, Arka Rai Choudhuri, Aditya Hegde, Abhishek Jain

- **Highly Efficient Actively Secure Two-Party Computation with One-Bit Advantage Bound.**
  2025 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SP61157.2025.00183)
  Junzuo Lai, Qi Wang, Anjia Yang, Yi Liu, Siu-Ming Yiu, Peng Yang, Jian Weng

- **High-Throughput Secure Multiparty Computation with an Honest Majority in Various Network Settings.**
  2025 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2025-0015)
  Ajith Suresh, Murali Annavaram, Christopher Harth-Kitzerow, Yongqin Wang, Hossein Yalame, Georg Carle

- **General Adversary Structures in Byzantine Agreement and Multi-party Computation with Active and Omission Corruption.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-78023-3_7)
  Konstantinos Brazitikos, Vassilis Zikas

- **Fully Anonymous Secret Sharing.**
  2025 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-032-01884-7_12)
  Paul Lou, Yuval Ishai, Abhishek Jain, Allison Bishop, Matthew Green

- **Fast Enhanced Private Set Union in the Balanced and Unbalanced Scenarios.**
  2025 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/tu)
  Cong Zhang, Yujie Bai, Yang Cao, Binbin Tu, Yu Chen

- **FOLEAGE: $\\mathbb {F}\_{\\scriptstyle 4}$OLE-Based Multi-party Computation for Boolean Circuits.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-981-96-0938-3_3)
  Geoffroy Couteau, Dung Bui, Clément Ducros, Sacha Servan-Schreiber, Maxime Bombar, Alain Couvreur

- **Evolving Secret Sharing Made Short.**
  2025 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-96-0941-3_3)
  Danilo Francati, Daniele Venturi

- **EoTMP: Efficient Over-Threshold Multi-Party Private Set Intersection.**
  2025 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2025.3639987)
  Xiaoguang Li, Hui Li, Xingwen Zhao, Song Bian, Qingwen Li

- **Enabling Two-Party Secure Computation on Set Intersection.**
  2025 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2025.3561472)
  Alptekin Küpçü, Ferhat Karakoç

- **Enabling Low-Cost Secure Computing on Untrusted In-Memory Architectures.**
  2025 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/ghinani)
  Elaheh Sadredini, Jingyao Zhang, Sahar Ghoflsaz Ghinani

- **Efficient and Privacy-Preserving Feature Selection Based on Multiparty Computation.**
  2025 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2025.3546843)
  Hao Guo, Lu Zhou, Luyao Wang, Weibin Wu

- **Efficient Three-Party ECDSA Signature Based on Replicated Secret Sharing With Identifiable Abort.**
  2025 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2025.3607264)
  Chenkai Zeng, Min Luo, Yu Peng, Wenjing Cheng, Qi Feng, Qingcai Luo, Xiaolin Yang

- **Efficient Permutation Correlations and Batched Random Access for Two-Party Computation.**
  2025 · MPC · [PKC](https://doi.org/10.1007/978-3-031-91829-2_3)
  Srinivasan Raghuraman, Peter Rindal, Harshal Shah, Stanislav Peceny

- **Efficient Multi-Party Private Set Union Without Non-Collusion Assumptions.**
  2025 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/dong-minglang)
  Cong Zhang, Yujie Bai, Minglang Dong, Yu Chen

- **Efficient Mixed Garbling from Homomorphic Secret Sharing and GGM-Tree.**
  2025 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-031-91095-1_6)
  Wenjie Nan, Jian Guo

- **Efficient Fuzzy Private Set Intersection from Fuzzy Mapping.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-981-96-0938-3_2)
  Ying Gao, Xiang Liu, Longxin Wang, Yuanchao Luo, Lin Qi

- **Efficient Collaborative Data Cleaning Using Private Set Intersection and Encoding for Unbalanced Datasets.**
  2025 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2025.3594871)
  Fagen Li, Wenyi Li, Yu Zhou, Xiaojun Zhang, Jingting Xue, Wenzheng Zhang

- **Efficient 2PC for Constant Round Secure Equality Testing and Comparison.**
  2025 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/lu)
  Xin Kang, Chun Chen, Xiaoyuan Zhang, Kui Ren, Tianpei Lu, Yang Liu, Zhuo Ma, Bingsheng Zhang

- **Distributed Function Secret Sharing and Applications.**
  2025 · MPC · [NDSS](https://www.ndss-symposium.org/ndss-paper/distributed-function-secret-sharing-and-applications/)
  Dongxiao Liu, Meng Hao, Hanxiao Chen, Pengzhi Xing, Hongwei Li, Jia Hu

- **Disincentivize Collusion in Verifiable Secret Sharing.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-91092-0_2)
  Hai H. Nguyen, Aniket Kate, Tiantian Gong, Hemanta K. Maji

- **Dishonest Majority Multiparty Computation over Matrix Rings.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-981-96-0938-3_10)
  Hongqing Liu, Taoxu Zou, Chen Yuan, Chaoping Xing

- **Dash: Accelerating Distributed Private Convolutional Neural Network Inference with Arithmetic Garbled Circuits.**
  2025 · MPC · [TCHES](https://doi.org/10.46586/TCHES.V2025.I1.420-449)
  Sebastian Berndt, Ida Bruhns, Jonas Sander, Thomas Eisenbarth

- **Compute, but Verify: Efficient Multiparty Computation over Authenticated Inputs.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-981-96-0938-3_5) · [IACR ePrint](https://eprint.iacr.org/2022/1648)
  Moumita Dutta, Chaya Ganesh, Sikhar Patranabis, Nitin Singh

  <details><summary>摘要 / Abstract</summary>

  Traditional notions of secure multiparty computation (MPC) allow mutually distrusting parties to jointly compute a function over their private inputs, but typically do not specify how these inputs are chosen. Motivated by real-world applications where corrupt inputs could adversely impact privacy and operational legitimacy, we consider a notion of authenticated MPC where the inputs are authenticated, e.g., signed using a digital signature by some certification authority. We propose a generic and efficient compiler that transforms any linear secret sharing based honest-majority MPC protocol into one with input authentication. Our compiler incurs significantly lower computational costs and competitive communication overheads when compared to the best existing solutions, while entirely avoiding the (potentially expensive) protocol-specific techniques and pre-processing requirements that are inherent to these solutions. For $n$-party honest majority MPC protocols with abort security where each party has $\ell$ inputs, our compiler incurs $O(n\log \ell)$ communication overall and a computational overhead of $O(\ell)$ group exponentiations per party (the corresponding overheads for the most efficient existing solution are $O(n^2)$ and $O(\ell n)$). Finally, for a corruption threshold $t&lt;n/3$, our compiler preserves the stronger identifiable abort security of the underlying MPC protocol. No existing solution for authenticated MPC achieves this regardless of the corruption threshold. Along the way, we make several technical contributions that are of independent interest. This includes the notion of distributed proofs of knowledge and concrete realizations of the same for several relations of interest, such as proving knowledge of many popularly used digital signature schemes, and proving knowledge of opening of a Pedersen commitment.

  匹配依据：MPC: multiparty computation, secret sharing, secure multiparty computation

  </details>

- **Computationally Differentially Private Inner-Product Protocols Imply Oblivious Transfer.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-032-01884-7_6)
  Eliad Tsfadia, Jad Silbak, Iftach Haitner, Noam Mazor, Chao Yan

- **Charge Your Clients: Payable Secure Computation and Its Applications.**
  2025 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2025.3559456)
  Meng Hao, Weiran Liu, Cong Zhang, Liqiang Peng, Shuaishuai Li, Dongdai Lin, Lei Zhang

- **Black-Box Constant-Round Secure 2PC with Succinct Communication.**
  2025 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-031-91092-0_13)
  Michele Ciampi, Akash Shah, Ankit Kumar Misra, Rafail Ostrovsky

- **Bitwise Garbling Schemes - A Model with 32λ\\documentclass\[12pt\]{minimal} \\usepackage{amsmath} \\usepackage{wasysym} \\usepackage{amsfonts} \\usepackage{amssymb} \\usepackage{amsbsy} \\usepackage{mathrsfs} \\usepackage{upgreek} \\setlength{\\oddsidemargin}{-69pt} \\begin{document}$$\\frac{3}{2}\\lambda $$\\end{document}-Bit Lower Bound of Ciphertexts.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-032-01884-7_15)
  Honggang Hu, Changhong Xu, Fei Xu

- **BitGC: Garbled Circuits with 1 Bit per Gate.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-91098-2_16)
  Xiao Wang, Hanlin Liu, Yu Yu, Kang Yang

- **Authenticated BitGC for Actively Secure Rate-One 2PC.**
  2025 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-032-01884-7_21)
  Hanlin Liu, Xiao Wang, Yu Yu, Kang Yang

- **An Improvement Upon the Bounds for the Local Leakage Resilience of Shamir's Secret Sharing Scheme.**
  2025 · MPC · [TCC](https://doi.org/10.1007/978-3-031-78023-3_13)
  Dustin Kasser

- **All-You-Can-Compute: Packed Secret Sharing for Combined Resilience.**
  2025 · MPC · [TCHES](https://doi.org/10.46586/TCHES.V2025.I2.420-459)
  Maximilian Orlt, Liang Zhao, Sebastian Faust, Kathrin Wirschem

- **Adaptive Security, Erasures, and Network Assumptions in Communication-Local MPC.**
  2025 · MPC · [TCC](https://doi.org/10.1007/978-3-031-78023-3_10)
  Juan A. Garay, Ankit Kumar Misra, Nishanth Chandran, Vassilis Zikas, Rafail Ostrovsky

- **Actively Secure MPC in the Dishonest Majority Setting: Achieving Constant Complexity in Online Communication, Computation Per Gate, Rounds, and Private Input Size.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-032-01884-7_4)
  Jaesang Noh, Dohyuk Kim, Seung-Hwan Lee, Dong-Joon Shin, Taejeong Kim

- **A Unified Framework for Succinct Garbling from Homomorphic Secret Sharing.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-032-01884-7_13)
  Yuval Ishai, Hanjun Li, Huijia Lin

- **A Scheme of Robust Privacy-Preserving Multi-Party Computation via Public Verification.**
  2025 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2025.3555284)
  Keke Gai, Jing Yu, Weizhi Meng, Dongjue Wang, Liehuang Zhu

- **A Note on Low-Communication Secure Multiparty Computation via Circuit Depth-Reduction.**
  2025 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-78023-3_6)
  Geoffroy Couteau, Pierre Charbit, Pierre Meyer, Reza Naserasr

### 2024

- **Succinct Homomorphic MACs from Groups and Applications**
  2024-12-24 · MPC · [IACR ePrint](https://eprint.iacr.org/2024/2073)
  Yuval Ishai, Hanjun Li, Huijia Lin

  <details><summary>摘要 / Abstract</summary>

  Homomorphic message authentication codes (HMACs) allow users to authenticate data using a shared secret key, while supporting computation over authenticated data. Given data $(m_1, \ldots, m_n)$ and their tags $(\sigma_1, \ldots, \sigma_n)$, anyone can evaluate a circuit $C$ on the data and tags to produce a succinct tag authenticating the output $C(m_1, \ldots, m_n)$. Importantly, tags remain succinc -- of size polynomial in the security parameter $\lambda$ -- regardless of the size of $C$. This work introduces an enhanced variant of HMACs called algebraic HMAC (aHMAC), in which all tags (input and output) take the form $\Delta \cdot m + K$, as in standard information-theoretic MACs. We construct an aHMAC from group-based assumptions, including variants of the DDH and DCR assumptions, and use it to obtain group-based constructions of several cryptographic primitives: - Succinct CDS for circuits. For any $P: [N]^k \to [N]$ represented by circuit, we obtain a Conditional Disclosure of Secrets protocol with poly$(\lambda, k, \log N )$ communication. - Succinct PSM for simple programs. For any $P:[N]^k \to [N]$ represented by a truth-table or shallow branching program, we obtain a Private Simultaneous Messages protocol or a garbling scheme with poly$(\lambda, k, \log N )$ communication. - Constrained PRFs for circuits. We obtain the first group-based constrained pseudorandom functions for general circuits, improving over a previous construction for NC1 circuits. Prior to our work, these applications could only be obtained from lattice assumptions or indistinguishability obfuscation.

  匹配依据：MPC: garbling scheme

  </details>

- **Anonymous Shamir's Secret Sharing via Reed-Solomon Codes Against Permutations, Insertions, and Deletions**
  2024-12-22 · MPC · [arXiv](https://arxiv.org/abs/2412.17003)
  Roni Con

  <details><summary>摘要 / Abstract</summary>

  In this work, we study the performance of Reed-Solomon codes against an adversary that first permutes the symbols of the codeword and then performs insertions and deletions. This adversarial model is motivated by the recent interest in fully anonymous secret-sharing schemes [EBG+24],[BGI+24]. A fully anonymous secret-sharing scheme has two key properties: (1) the identities of the participants are not revealed before the secret is reconstructed, and (2) the shares of any unauthorized set of participants are uniform and independent. In particular, the shares of any unauthorized subset reveal no information about the identity of the participants who hold them. In this work, we first make the following observation: Reed-Solomon codes that are robust against an adversary that permutes the codeword and then deletes symbols from the permuted codeword can be used to construct ramp threshold secret-sharing schemes that are fully anonymous. Then, we show that over large enough fields of size, there are $[n,k]$ Reed-Solomon codes that are robust against an adversary that arbitrary permutes the codeword and then performs $n-2k+1$ insertions and deletions to the permuted codeword. This implies the existence of a $(k-1, 2k-1, n)$ ramp secret sharing scheme that is fully anonymous. That is, any $k-1$ shares reveal nothing about the secret, and, moreover, this set of shares reveals no information about the identities of the players who hold them. On the other hand, any $2k-1$ shares can reconstruct the secret without revealing their identities. We also provide explicit constructions of such schemes based on previous works on Reed-Solomon codes correcting insertions and deletions. The constructions in this paper give the first gap threshold secret-sharing schemes that satisfy the strongest notion of anonymity together with perfect reconstruction.

  匹配依据：MPC: secret sharing

  </details>

- **MULTISS: Long-Term Secure Distributed Storage over Remote QKD Networks**
  2024-11-25 · MPC · [IACR ePrint](https://eprint.iacr.org/2024/1915)
  Thomas Prévost, Olivier Alibart, Anne Marin, Marc Kaplan, Pascal Lafourcade, Charles Olivier-Anclin

  <details><summary>摘要 / Abstract</summary>

  We introduce MULTISS, a distributed storage protocol over multiple remote Quantum Key Distribution (QKD) networks that ensures long-term data confidentiality. MULTISS is designed to combine several QKD networks, as QKD links are inherently limited in range, and to connect these networks through classical cryptographic channels. It relies on a hierarchical secret sharing scheme that makes certain shares mandatory for the reconstruction of the original secret. Hence, MULTISS offers a secure distributed storage solution in a scenario that is compatible with the current deployment of quantum networks. We prove that MULTISS preserves the confidentiality of stored data even if an adversary (i) gains full access to all nodes of a subset of the QKD networks, or (ii) records all classical communications between distant QKD networks and compromises them at a later stage. We show that it provides strictly stronger security guarantees than existing QKD-storage protocols. Our protocol also includes a procedure to update the shares without reconstructing the original data. In addition, we provide a recovery mechanism that tolerates the complete compromise of some QKD networks. We further introduce a variant of the protocol, called the local-mode, that minimizes the communication overhead of the recovery procedure when deployed over specific network topologies.

  匹配依据：MPC: secret sharing

  </details>

- **Efficient Pairing-Free Adaptable k-out-of-N Oblivious Transfer Protocols**
  2024-10-07 · MPC · [IACR ePrint](https://eprint.iacr.org/2024/1583)
  Keykhosro Khosravani, Taraneh Eghlidos, Mohammad reza Aref

  <details><summary>摘要 / Abstract</summary>

  Oblivious Transfer (OT) is one of the fundamental building blocks in cryptography that enables various privacy-preserving applications. Constructing efficient OT schemes has been an active research area. This paper presents three efficient two-round pairing-free k-out-of-n oblivious transfer protocols with standard security. Our constructions follow the minimal communication pattern: the receiver sends k messages to the sender, who responds with n+k messages, achieving the lowest data transmission among pairing-free k-out-of-n OT schemes. Furthermore, our protocols support adaptivity and enable the sender to encrypt the n messages offline, independent of the receiver’s variables, offering significant performance advantages in one-sender-multiple-receiver scenarios. We provide security proofs under the Computational Diffie-Hellman (CDH) and RSA assumptions, without relying on the Random Oracle Model. Our protocols combine minimal communication rounds, adaptivity, offline encryption capability, and provable security, making them well-suited for privacy-preserving applications requiring efficient oblivious transfer.

  匹配依据：MPC: oblivious transfer

  </details>

- **Updatable Private Set Intersection With Forward Privacy.**
  2024 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2024.3461475)
  Xiaolei Dong, Zhenfu Cao, Jun Zhou, Ruochen Wang, Kim-Kwang Raymond Choo

- **Unbalanced Private Set Union with Reduced Computation and Communication.**
  2024 · MPC · [ACM CCS](https://doi.org/10.1145/3658644.3690308)
  Cong Zhang, Meng Hao, Anyu Wang, Liqiang Peng, Weiran Liu, Xiaoyun Wang, Yu Chen

- **Two-Round Maliciously-Secure Oblivious Transfer with Optimal Rate.**
  2024 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-031-58751-1_10)
  Akshayaram Srinivasan, Pedro Branco, Nico Döttling

- **Traceable Secret Sharing: Strong Security and Efficient Constructions.**
  2024 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-031-68388-6_9)
  Lior Rotem, Aditi Partap, Dan Boneh

- **Towards Breaking the Half-Barrier of Local Leakage-Resilient Shamir's Secret Sharing.**
  2024 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-031-68388-6_10)
  Hai H. Nguyen

- **Toward Malicious Constant-Rate 2PC via Arithmetic Garbling.**
  2024 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-031-58740-5_14)
  Yibin Yang, Carmit Hazay

- **Toward A Practical Multi-party Private Set Union.**
  2024 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2024-0133)
  Ni Trieu, Jiahui Gao, Son Nguyen

- **The Capacity Region of Distributed Multi-User Secret Sharing Under Perfect Secrecy.**
  2024 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2024.3484666)
  Jiahong Wu, Wei Kang, Nan Liu

- **Succinct Homomorphic Secret Sharing.**
  2024 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-031-58751-1_11)
  Lawrence Roy, Peter Scholl, Damiano Abram

- **Stochastic Secret Sharing with 1-Bit Shares and Applications to MPC.**
  2024 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-68388-6_11)
  Eliran Kachlon, Benny Applebaum

- **Sparsity and Privacy in Secret Sharing: A Fundamental Trade-Off.**
  2024 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2024.3394256)
  Maximilian Egger, Marvin Xhemrishi, Rawad Bitar, Antonia Wachter-Zeh

- **Secure and Efficient Federated Learning via Novel Authenticable Multi-Party Computation and Compressed Sensing.**
  2024 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2024.3486611)
  Di Xiao, Yushu Zhang, Xiangli Xiao, Lvjun Chen

- **Secure Sorting and Selection via Function Secret Sharing.**
  2024 · MPC · [ACM CCS](https://doi.org/10.1145/3658644.3690359)
  Yuval Ishai, Elette Boyle, Mahimna Kelkar, Yiping Ma, Amit Agarwal, Divya Gupta, Nishanth Chandran, Niv Gilboa

- **Secure Multiparty Computation with Lazy Sharing.**
  2024 · MPC · [ACM CCS](https://doi.org/10.1145/3658644.3690207)
  Cong Zhang, Shuaishuai Li, Dongdai Lin

- **Secure Multiparty Computation with Identifiable Abort via Vindicating Release.**
  2024 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-031-68397-8_2)
  Yashvanth Kondi, Ran Cohen, Jack Doerner, Abhi Shelat

- **Secure Multiparty Computation of Threshold Signatures Made More Efficient.**
  2024 · MPC · [NDSS](https://www.ndss-symposium.org/ndss-paper/secure-multiparty-computation-of-threshold-signatures-made-more-efficient/)
  Harry W. H. Wong, Jack P. K. Ma, Sherman S. M. Chow

- **Secret Sharing with Snitching.**
  2024 · MPC · [ACM CCS](https://doi.org/10.1145/3658644.3690296)
  Tomasz Lizurej, Marcin Mielniczuk, Stefan Dziembowski, Sebastian Faust

- **Secret Sharing with Certified Deletion.**
  2024 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-031-68394-7_7)
  James Bartusek, Justin Raizes

- **Secret Cracking and Security Enhancement for the Image Application of CRT-Based Secret Sharing.**
  2024 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2024.3477265)
  Rui Wang, Xuehu Yan, Guozheng Yang, Wei Yan, Longlong Li

- **Scalable Private Set Union, with Stronger Security.**
  2024 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity24/presentation/jia-yanxue)
  Shifeng Sun, Yanxue Jia, Hong-Sheng Zhou, Dawu Gu

- **Scalable Multiparty Computation from Non-linear Secret Sharing.**
  2024 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-031-68397-8_12)
  Pratyay Mukherjee, Abhishek Jain, Sanjam Garg, Mingyuan Wang

- **Scalable Multi-Party Computation Protocols for Machine Learning in the Honest-Majority Setting.**
  2024 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity24/presentation/liu-fengrun)
  Xiang Xie, Yu Yu, Fengrun Liu

- **SIGMA: Secure GPT Inference with Function Secret Sharing.**
  2024 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2024-0107)
  Ashish Panwar, Rahul Sharma, Ananta Mukherjee, Neha Jawalkar, Kanav Gupta, Divya Gupta, Nishanth Chandran

- **Randomness Recoverable Secret Sharing Schemes.**
  2024 · MPC · [Journal of Cryptology](https://doi.org/10.1007/S00145-024-09515-4)
  Behzad Vahdani, Shahram Khazaei, Mohammad Hajiabadi

- **P²FRPSI: Privacy-Preserving Feature Retrieved Private Set Intersection.**
  2024 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2023.3343973)
  Chaochao Cai, Weidong Qiu, Haiyang Xue, Guowei Ling, Jinyong Shan, Wulu Li, Peng Tang, Xinyi Huang, Fei Tang

- **Publicly Verifiable Secret Sharing Over Class Groups and Applications to DKG and YOSO.**
  2024 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-031-58740-5_8)
  Bernardo Machado David, Ignacio Cascudo

- **PrivDNN: A Secure Multi-Party Computation Framework for Deep Learning using Partial DNN Encryption.**
  2024 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2024-0089)
  Kaitai Liang, Zhu Li, Liangqin Ren, Zeyan Liu, Fengjun Li, Bo Luo

- **Poster: Multiparty Private Set Intersection from Multiparty Homomorphic Encryption.**
  2024 · MPC · [ACM CCS](https://doi.org/10.1145/3658644.3691405)
  Wouter Lueks, Christian Mouchet, Lea Nürnberger, Sylvain Chatel

- **Poster: A Secure Multiparty Computation Platform for Squeaky-Clean Data Rooms.**
  2024 · MPC · [ACM CCS](https://doi.org/10.1145/3658644.3691371)
  Sikhar Patranabis, Vinayaka Pandit, Abhishek Singh, Nitin Singh, Pankaj Dayama

- **PEPSI: Practically Efficient Private Set Intersection in the Unbalanced Setting.**
  2024 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity24/presentation/mahdavi)
  Ehsan Amjadian, Simon Oya, Florian Kerschbaum, Thomas Humphries, Faezeh Ebrahimianghazani, Bailey Kacsmar, Xinda Li, Nils Lukas, John A. Premkumar, Rasoul Akhavan Mahdavi

- **On Sigma-Protocols and (Packed) Black-Box Secret Sharing Schemes.**
  2024 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-57722-2_14)
  Ignacio Cascudo, Claudia Bartoli

- **On Information-Theoretic Secure Multiparty Computation with Local Repairability.**
  2024 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-57722-2_7)
  Daniel Escudero, Ivan Tjuawinata, Chaoping Xing

- **O-Ring and K-Star: Efficient Multi-party Private Set Intersection.**
  2024 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity24/presentation/wu-mingli)
  Tsz Hon Yuen, Kwan Yin Chan, Mingli Wu

- **NodeGuard: A Highly Efficient Two-Party Computation Framework for Training Large-Scale Gradient Boosting Decision Tree.**
  2024 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SPW63631.2024.00015)
  Yufan Jiang, Tianxiang Dai, Fei Mei, Yong Li

- **Network-Agnostic Multi-party Computation Revisited (Extended Abstract).**
  2024 · MPC · [PKC](https://doi.org/10.1007/978-3-031-57722-2_6)
  Supreeth Varadarajan, Nidhish Bhimrajka, Ashish Choudhury

- **Multiparty Private Set Intersection Cardinality and Its Applications.**
  2024 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2024-0041)
  Ni Trieu, Avishay Yanai, Jiahui Gao

- **Maliciously Secure MPC From Semi-Honest 2PC in the Server-Aided Model.**
  2024 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2023.3322397)
  Yibiao Lu, Kui Ren, Bingsheng Zhang

- **MPC-in-the-Head Framework without Repetition and its Applications to the Lattice-based Cryptography.**
  2024 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00157)
  Qianwen Gao, Long Chen, Zhenfeng Zhang, Weihao Bai

- **MPC-Pipe: an Efficient Pipeline Scheme for Semi-honest MPC Machine Learning.**
  2024 · MPC · [ASPLOS](https://doi.org/10.1145/3622781.3674175)
  Murali Annavaram, Rachit Rajat, Yongqin Wang

- **Linear-Communication Asynchronous Complete Secret Sharing with Optimal Resilience.**
  2024 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-68397-8_13)
  Junru Li, Yifan Song, Xiaoyu Ji

- **Lightweight Asynchronous Verifiable Secret Sharing with Optimal Resilience.**
  2024 · MPC · [Journal of Cryptology](https://doi.org/10.1007/S00145-024-09505-6)
  Victor Shoup, Nigel P. Smart

- **Garbled Circuit Lookup Tables with Logarithmic Number of Ciphertexts.**
  2024 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-031-58740-5_7)
  David Heath, Lucien K. L. Ng, Vladimir Kolesnikov

- **GAuV: A Graph-Based Automated Verification Framework for Perfect Semi-Honest Security of Multiparty Computation Protocols.**
  2024 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00131)
  Wei Zhang, Shizhen Xu, Xingyu Xie, Tuowei Wang, Yifei Li, Jun Zhu, Yifan Song

- **Fuzzy Private Set Intersection with Large Hyperballs.**
  2024 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-58740-5_12)
  Sihang Pu, Aron van Baarsen

- **Fully Secure MPC and zk-FLIOP over Rings: New Constructions, Improvements and Extensions.**
  2024 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-031-68397-8_5)
  Ariel Nof, Anders P. K. Dalskov, Daniel Escudero

- **Fast RS-IOP Multivariate Polynomial Commitments and Verifiable Secret Sharing.**
  2024 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity24/presentation/zhang-zongyang)
  Kexin Shi, Ximeng Liu, Weihan Li, Jin Dong, Yanpei Guo, Zongyang Zhang, Sherman S. M. Chow

- **Fast Evaluation of S-Boxes With Garbled Circuits.**
  2024 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2024.3402145)
  Aysajan Abidin, Erik Pohle, Bart Preneel

- **FSS-DBSCAN: Outsourced Private Density-Based Clustering via Function Secret Sharing.**
  2024 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2024.3446233)
  Yulong Shen, Zhao Chang, Jiaxuan Fu, Yuheng Xia, Anxiao Song, Ke Cheng

- **Enabling Threshold Functionality for Private Set Intersection Protocols in Cloud Computing.**
  2024 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2024.3402355)
  Yongjun Zhao, Khin Mi Mi Aung, Benjamin Hong Meng Tan, Huaxiong Wang, Jingwei Hu

- **Efficiently Compiling Secure Computation Protocols From Passive to Active Security: Beyond Arithmetic Circuits.**
  2024 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2024-0006)
  Dennis Murphy, Marina Blanton, Chen Yuan

- **Efficient Secret Sharing for Large-Scale Applications.**
  2024 · MPC · [ACM CCS](https://doi.org/10.1145/3658644.3670379)
  Sarvar Patel, Kevin Yeo, Joon Young Seo, Giuseppe Persiano

- **Efficient Scalable Multi-Party Private Set Intersection(-Variants) from Bicentric Zero-Sharing.**
  2024 · MPC · [ACM CCS](https://doi.org/10.1145/3658644.3690245)
  Ying Gao, Mengmeng Zhou, Wei Wang, Longxin Wang, Xiang Liu, Yuanchao Luo, Lin Qi

- **Efficient Coded Multi-Party Computation at Edge Networks.**
  2024 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2023.3326970)
  Hulya Seferoglu, Elahe Vedadi, Yasaman Keshtkarjahromi

- **Efficient Arithmetic in Garbled Circuits.**
  2024 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-58740-5_1)
  David Heath

- **Efficient Actively Secure DPF and RAM-based 2PC with One-Bit Leakage.**
  2024 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00205)
  Ruiyu Zhu, Xiao Wang, Yu Yu, Xiaojie Guo, Wenhao Zhang, Kang Yang

- **Dual-Cloud Multi-Secret Sharing Architecture for Privacy Preserving Persistent Computation.**
  2024 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2024.3436662)
  Jhe-Kai Yang, Hsin-Chan Yen, Pei-Wen Lin, Yu-Chi Chen

- **Doubly Efficient Cryptography: Commitments, Arguments and RAM MPC.**
  2024 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-031-68397-8_8)
  Wei-Kai Lin, Ethan Mook, Daniel Wichs

- **Don't Eject the Impostor: Fast Three-Party Computation With a Known Cheater.**
  2024 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00164)
  Ajith Suresh, Thomas Schneider, Oliver Schick, Hossein Yalame, Andreas Brüggemann

- **Ditto: Quantization-aware Secure Inference of Transformers upon MPC.**
  2024 · MPC · [ICML](https://proceedings.mlr.press/v235/wu24d.html)
  Lei Wang, Junming Ma, Wenjing Fang, Jin Tan, Yancheng Zheng, Haoqi Wu

- **Coral: Maliciously Secure Computation Framework for Packed and Mixed Circuits.**
  2024 · MPC · [ACM CCS](https://doi.org/10.1145/3658644.3690223)
  Zhicong Huang, Wen-jie Lu, Wenguang Chen, Yuchen Wang, Tao Wei, Cheng Hong

- **Constructing Leakage-Resilient Shamir's Secret Sharing: Over Composite Order Fields.**
  2024 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-031-58737-5_11)
  Hai H. Nguyen, Xiuyu Ye, Anat Paskin-Cherniavsky, Hemanta K. Maji

- **Connecting Leakage-Resilient Secret Sharing to Practice: Scaling Trends and Physical Dependencies of Prime Field Masking.**
  2024 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-031-58737-5_12)
  Elena Micheli, François-Xavier Standaert, Maximilian Orlt, Loïc Masure, Sebastian Faust

- **Computation Efficient Structure-Aware PSI from Incremental Function Secret Sharing.**
  2024 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-68397-8_10)
  Peihan Miao, Gayathri Garimella, Benjamin Goff

- **Compact: Approximating Complex Activation Functions for Secure Computation.**
  2024 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2024-0065)
  Rahul Chatterjee, Peter Rindal, Sunpreet S. Arora, Maliheh Shirvanian, Mazharul Islam

- **Communication-Efficient Privacy-Preserving Neural Network Inference via Arithmetic Secret Sharing.**
  2024 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2024.3420216)
  Jianting Ning, Yan Zhang, Changqing Luo, Jinbo Xiong, Ximeng Liu, Youliang Tian, Renwan Bi

- **Collusion-Resilient and Maliciously Secure Cloud- Assisted Two-Party Computation Scheme in Mobile Cloud Computing.**
  2024 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2024.3428410)
  Zhenfu Cao, Zhe Liu, Nan Min, Zhusen Liu, Weizheng Wang, Lu Zhou, Yutong Ye

- **Bounds and Protocols for Graph-Based Distributed Secret Sharing.**
  2024 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2023.3261239)
  Alfredo De Santis, Roberto De Prisco, Francesco Palmieri

- **Application of Randomness for Security and Privacy in Multi-Party Computation.**
  2024 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2024.3381959)
  William J. Buchanan, Rahul Saha, Gulshan Kumar, G. Geetha, Mauro Conti

- **Actively Secure Private Set Intersection in the Client-Server Setting.**
  2024 · MPC · [ACM CCS](https://doi.org/10.1145/3658644.3690349)
  Mariana Raykova, Phillipp Schoppmann, Xiao Wang, Yunqing Sun, Jonathan Katz

- **Abuse Reporting for Metadata-Hiding Communication Based on Secret Sharing.**
  2024 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity24/presentation/eskandarian)
  Saba Eskandarian

- **AITIA: Efficient Secure Computation of Bivariate Causal Discovery.**
  2024 · MPC · [ACM CCS](https://doi.org/10.1145/3658644.3670337)
  Lun Wang, Ni Trieu, Truong Son Nguyen, Evgenios M. Kornaropoulos

- **A Secure Computing System With Hardware-Efficient Lazy Bonsai Merkle Tree for FPGA-Attached Embedded Memory.**
  2024 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2023.3324935)
  Yu Zou, Rakin Muhammad Shadab, Sanjay Gandham, Mingjie Lin, Amro Awad

- **A New Shift-Add Secret Sharing Scheme for Partial Data Protection With Parallel Zigzag Decoding.**
  2024 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2024.3488498)
  Chi Wan Sung, Yichen Shen, Jiajun Chen

- **10-Party Sublinear Secure Computation from Standard Assumptions.**
  2024 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-68400-5_2)
  Geoffroy Couteau, Naman Kumar

### 2023

- **Verifiable Homomorphic Secret Sharing for Low Degree Polynomials.**
  2023 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2022.3194321)
  Liang Feng Zhang, Xin Chen, Jing Liu

- **Unconditionally Secure Multiparty Computation for Symmetric Functions with Low Bottleneck Complexity.**
  2023 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-99-8721-4_11)
  Reo Eriguchi

- **Trifecta: Faster High-Throughput Three-Party Computation over WAN Using Multi-Fan-In Logic Gates.**
  2023 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2023-0107)
  Sina Faraji, Florian Kerschbaum

- **Towards Topology-Hiding Computation from Oblivious Transfer.**
  2023 · MPC · [TCC](https://doi.org/10.1007/978-3-031-48615-9_13)
  Lisa Kohl, Marshall Ball, Alexander Bienstock, Pierre Meyer

- **Threshold Private Set Intersection with Better Communication Complexity.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-31371-4_9)
  Satrajit Ghosh, Mark Simkin

- **Threshold Linear Secret Sharing to the Rescue of MPC-in-the-Head.**
  2023 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-99-8721-4_14)
  Matthieu Rivain, Thibauld Feneuil

- **Three Party Secure Computation with Friends and Foes.**
  2023 · MPC · [TCC](https://doi.org/10.1007/978-3-031-48618-0_6)
  Bar Alon, Amos Beimel, Eran Omri

- **TVA: A multi-party computation system for secure and expressive time series analytics.**
  2023 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/faisal)
  Vasiliki Kalavri, Mayank Varia, John Liagouris, Muhammad Faisal, Jerry Zhang

- **Succinct Computational Secret Sharing.**
  2023 · MPC · [STOC](https://doi.org/10.1145/3564246.3585127)
  Tianren Liu, Yuval Ishai, Benny Applebaum, Vinod Vaikuntanathan, Eyal Kushilevitz, Amos Beimel

- **Sublinear-Communication Secure Multiparty Computation Does Not Require FHE.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-30617-4_6)
  Elette Boyle, Geoffroy Couteau, Pierre Meyer

- **Squirrel: A Scalable Secure Two-Party Computation Framework for Training Gradient Boosting Decision Tree.**
  2023 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/lu)
  Zhicong Huang, Qizhi Zhang, Wen-jie Lu, Yuchen Wang, Cheng Hong

- **Sigma Protocols from Verifiable Secret Sharing and Their Applications.**
  2023 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-99-8724-5_7)
  Zhichao Wang, Chuanzhou Yao, Yu Chen, Min Zhang

- **Secure Multiparty Computation from Threshold Encryption Based on Class Groups.**
  2023 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-031-38557-5_20)
  Lennart Braun, Ivan Damgård, Claudio Orlandi

- **Secure Computation with Shared EPR Pairs (Or: How to Teleport in Zero-Knowledge).**
  2023 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-031-38554-4_8)
  Akshayaram Srinivasan, James Bartusek, Dakshita Khurana

- **Secure Computation Meets Distributed Universal Optimality.**
  2023 · MPC · [FOCS](https://doi.org/10.1109/FOCS57990.2023.00144)
  Merav Parter

- **Scalable Multi-party Private Set Union from Multi-query Secret-Shared Private Membership Test.**
  2023 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-99-8721-4_8)
  Ying Gao, Xiang Liu

- **Round-Optimal Oblivious Transfer and MPC from Computational CSIDH.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-31368-4_14)
  Daniel Masny, Pratyay Mukherjee, Saikrishna Badrinarayanan, Pratik Sarkar, Srinivasan Raghuraman, Sikhar Patranabis

- **Reverse Firewalls for Oblivious Transfer Extension and Applications to Zero-Knowledge.**
  2023 · MPC · [EUROCRYPT](https://doi.org/10.1007/978-3-031-30545-0_9)
  Suvradip Chakraborty, Pratik Sarkar, Chaya Ganesh

- **Reusable Secure Computation in the Plain Model.**
  2023 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-031-38557-5_14)
  Akshayaram Srinivasan, Mingyuan Wang, Vipul Goyal

- **Ramen: Souper Fast Three-Party Computation for RAM Programs.**
  2023 · MPC · [ACM CCS](https://doi.org/10.1145/3576915.3623115)
  Mahak Pancholi, Lennart Braun, Rahul Rachuri, Mark Simkin

- **Publicly Verifiable Homomorphic Secret Sharing for Polynomial Evaluation.**
  2023 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2023.3298258)
  Xin Chen, Liang Feng Zhang

- **Proactive Secret Sharing with Constant Communication.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-48618-0_12)
  Daniel Noble, Brett Hemenway, Tal Rabin

- **Private Access Control for Function Secret Sharing.**
  2023 · MPC · [IEEE S&amp;P](https://doi.org/10.1109/SP46215.2023.10179295)
  Simon Beyzerov, Eli Yablon, Hyojae Park, Sacha Servan-Schreiber

- **Privacy of Federated QR Decomposition Using Additive Secure Multiparty Computation.**
  2023 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2023.3301710)
  Anne Hartebrodt, Richard Röttger

- **Practically Efficient Private Set Intersection from Trusted Hardware with Side-Channels.**
  2023 · MPC · [ASIACRYPT](https://doi.org/10.1007/978-981-99-8730-6_9)
  Jeremias Mechler, Felix Dörre, Jörn Müller-Quade

- **On the Security of a Lattice-Based Multi-Stage Secret Sharing Scheme.**
  2023 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2022.3209011)
  Longjiang Qu, Debiao He, Jianqiao Xu, Zhichao Yang

- **On the Round Complexity of Fully Secure Solitary MPC with Honest Majority.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-48618-0_5)
  Saikrishna Badrinarayanan, Peihan Miao, Pratyay Mukherjee, Divya Ravi

- **On the Power of an Honest Majority in Three-Party Computation Without Broadcast.**
  2023 · MPC · [Journal of Cryptology](https://doi.org/10.1007/S00145-023-09456-4)
  Ran Cohen, Bar Alon, Tom Suad, Eran Omri

- **On the Communication Efficiency of Statistically Secure Asynchronous MPC with Optimal Resilience.**
  2023 · MPC · [Journal of Cryptology](https://doi.org/10.1007/S00145-023-09451-9)
  Ashish Choudhury, Arpita Patra

- **On Secure Computation of Solitary Output Functionalities with and Without Broadcast.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-48618-0_4)
  Bar Alon, Eran Omri

- **On Homomorphic Secret Sharing from Polynomial-Modulus LWE.**
  2023 · MPC · [PKC](https://doi.org/10.1007/978-3-031-31371-4_1)
  Lisa Kohl, Thomas Attema, Pedro Capitão

- **Oblivious Transfer with Constant Computational Overhead.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-30545-0_10)
  Lisa Kohl, Elette Boyle, Peter Scholl, Yuval Ishai, Geoffroy Couteau, Nicolas Resch, Niv Gilboa

- **Oblivious Transfer from Zero-Knowledge Proofs - Or How to Achieve Round-Optimal Quantum Oblivious Transfer and Zero-Knowledge Proofs on Quantum States.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-981-99-8742-9_1)
  Léo Colisson Palais, Garazi Muguruza, Florian Speelman

- **New Bounds on the Local Leakage Resilience of Shamir's Secret Sharing Scheme.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-38557-5_5)
  Ohad Klein, Ilan Komargodski

- **Network-Agnostic Security Comes (Almost) for Free in DKG and MPC.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-38557-5_3)
  Julian Loss, Chen-Da Liu-Zhang, Renas Bacho, Daniel Collins

- **Network Agnostic MPC with Statistical Security.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-48618-0_3)
  Ananya Appan, Ashish Choudhury

- **Multi-party Homomorphic Secret Sharing and Sublinear MPC from Sparse LPN.**
  2023 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-031-38545-2_11)
  Yuval Ishai, Aayush Jain, Quang Dao, Huijia Lin

- **Multi-Party Replicated Secret Sharing over a Ring with Applications to Privacy-Preserving Machine Learning.**
  2023 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2023-0035)
  Alessandro N. Baccarini, Chen Yuan, Marina Blanton

- **Matrix-Based Secret Sharing for Reversible Data Hiding in Encrypted Images.**
  2023 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2022.3218570)
  Xinpeng Zhang, Yongyong Chen, Zhongyun Hua, Shuang Yi, Yanxiang Wang, Yifeng Zheng, Xingyu Liu

- **Manticore: A Framework for Efficient Multiparty Computation Supporting Real Number and Boolean Arithmetic.**
  2023 · MPC · [Journal of Cryptology](https://doi.org/10.1007/S00145-023-09464-4)
  Mariya Georgieva, Iraklis Leontiadis, Dimitar Jetchev, Abson Sae-Tang, Marius Vuille, Kevin Deforth, Mohsen Mohammadi, Jonathan Katz, Nicolas Gama, Sergiu Carpov

- **Maliciously Secure and Efficient Large-Scale Genome-Wide Association Study With Multi-Party Computation.**
  2023 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2022.3152498)
  Jianfeng Ma, Zhiquan Liu, Anjia Yang, Jia-Nan Liu, Yaxi Yang, Caiqin Dong, Jian Weng

- **Malicious Secure, Structure-Aware Private Set Intersection.**
  2023 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-031-38557-5_19)
  Jaspal Singh, Gayathri Garimella, Mike Rosulek

- **Low Communication Secure Computation From Semi-Trusted Hardware.**
  2023 · MPC · [TIFS](https://doi.org/10.1109/TIFS.2023.3282134)
  Kui Ren, Bingsheng Zhang, Yibiao Lu

- **Longshot: Indexing Growing Databases using MPC and Differential Privacy.**
  2023 · MPC · [PVLDB](https://doi.org/10.14778/3594512.3594529)
  Johes Bater, Kartik Nayak, Yanping Zhang, Ashwin Machanavajjhala

- **List Oblivious Transfer and Applications to Round-Optimal Black-Box Multiparty Coin Tossing.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-38557-5_15)
  Michele Ciampi, Luisa Siniscalchi, Hendrik Waldner, Rafail Ostrovsky

- **Linear Private Set Union from Multi-Query Reverse Private Membership Test.**
  2023 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/zhang-cong)
  Cong Zhang, Weiran Liu, Min Zhang, Dongdai Lin, Yu Chen

- **Linear Communication in Malicious Majority MPC.**
  2023 · MPC · [ACM CCS](https://doi.org/10.1145/3576915.3623162)
  Daniel McVicker, Phi Hung Le, S. Dov Gordon

- **Let's Go Eevee! A Friendly and Suitable Family of AEAD Modes for IoT-to-Cloud Secure Computation.**
  2023 · MPC · [ACM CCS](https://doi.org/10.1145/3576915.3623091)
  Aysajan Abidin, Erik Pohle, Amit Singh Bhati, Elena Andreeva, Bart Preneel

- **Improved Protocols for Distributed Secret Sharing.**
  2023 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2022.3213790)
  Roberto De Prisco, Francesco Palmieri, Alfredo De Santis

- **Improved Private Set Intersection for Sets with Small Entries.**
  2023 · MPC · [PKC](https://doi.org/10.1007/978-3-031-31371-4_7)
  Dung Bui, Geoffroy Couteau

- **Improved Polynomial Secret-Sharing Schemes.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-48618-0_13)
  Or Lasri, Oriol Farràs, Amos Beimel

- **High-Throughput Secure Three-Party Computation with an Honest Majority.**
  2023 · MPC · [Journal of Cryptology](https://doi.org/10.1007/S00145-023-09461-7)
  Or Weinstein, Ariel Nof, Jun Furukawa, Yehuda Lindell

- **HAAC: A Hardware-Software Co-Design to Accelerate Garbled Circuits.**
  2023 · MPC · [ISCA](https://doi.org/10.1145/3579371.3589045)
  Brandon Reagen, Jianqiao Mo, Jayanth Gopinath

- **Garbled Circuits from an SCA Perspective Free XOR can be Quite Expensive. . .**
  2023 · MPC · [CHES](https://doi.org/10.46586/TCHES.V2023.I2.54-79)
  Itamar Levi, Carmit Hazay

- **Funshade: Function Secret Sharing for Two-Party Secure Thresholded Distance Evaluation.**
  2023 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2023-0096)
  Alberto Ibarrondo, Melek Önen, Hervé Chabanne

- **Faster Secure Comparisons with Offline Phase for Efficient Private Set Intersection.**
  2023 · MPC · [NDSS](https://www.ndss-symposium.org/ndss-paper/faster-secure-comparisons-with-offline-phase-for-efficient-private-set-intersection/)
  Erik-Oliver Blass, Rasoul Akhavan Mahdavi, Florian Kerschbaum

- **Fast Unbalanced Private Set Union from Fully Homomorphic Encryption.**
  2023 · MPC · [ACM CCS](https://doi.org/10.1145/3576915.3623064)
  Cong Zhang, Binbin Tu, Qi Liu, Yu Chen

- **Fast Large-Scale Honest-Majority MPC for Malicious Adversaries.**
  2023 · MPC · [Journal of Cryptology](https://doi.org/10.1007/S00145-023-09453-7)
  Ariel Nof, Yehuda Lindell, Koki Hamada, Ryo Kikuchi, Koji Chida, Dai Ikarashi, Daniel Genkin

- **Endemic Oblivious Transfer via Random Oracles, Revisited.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-30545-0_11)
  Kui Ren, Hong-Sheng Zhou, Zhelei Zhou, Bingsheng Zhang

- **Efficient decision tree training with new data structure for secure multi-party computation.**
  2023 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2023-0021)
  Koji Chida, Ryo Kikuchi, Koki Hamada, Dai Ikarashi

- **Efficient Unbalanced Private Set Intersection Cardinality and User-friendly Privacy-preserving Contact Tracing.**
  2023 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/wu-mingli)
  Tsz Hon Yuen, Mingli Wu

- **Efficient Noise Generation Protocols for Differentially Private Multiparty Computation.**
  2023 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2022.3227568)
  Noboru Kunihiro, Reo Eriguchi, Atsunori Ichikawa, Koji Nuida

- **Efficient Multiparty Probabilistic Threshold Private Set Intersection.**
  2023 · MPC · [ACM CCS](https://doi.org/10.1145/3576915.3623158)
  En Zhang, Leiyong Qin, Feng-Hao Liu

- **Efficient 3PC for Binary Circuits with Application to Maliciously-Secure DNN Inference.**
  2023 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/li-yun)
  Zhicong Huang, Yufei Duan, Yifan Song, Yun Li, Chao Zhang, Cheng Hong

- **Distance-Aware Private Set Intersection.**
  2023 · MPC · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/chakraborti-intersection)
  Anrin Chakraborti, Giulia Fanti, Michael K. Reiter

- **Detect, Pack and Batch: Perfectly-Secure MPC with Linear Communication and Constant Expected Time.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-30617-4_9)
  Ittai Abraham, Gilad Asharov, Shravani Patil, Arpita Patra

- **DORAM Revisited: Maliciously Secure RAM-MPC with Logarithmic Overhead.**
  2023 · MPC · [TCC](https://doi.org/10.1007/978-3-031-48615-9_16)
  Brett Hemenway, Daniel Noble, Jacob Zhang, Matan Shtepel, Rafail Ostrovsky

- **Cryptography with Weights: MPC, Encryption and Signatures.**
  2023 · MPC · [CRYPTO](https://doi.org/10.1007/978-3-031-38557-5_10)
  Rohit Sinha, Pratyay Mukherjee, Mingyuan Wang, Sanjam Garg, Abhishek Jain, Yinuo Zhang

- **Convolutions in Overdrive: Maliciously Secure Convolutions for MPC.**
  2023 · MPC · [PoPETs](https://doi.org/10.56553/POPETS-2023-0084)
  Marc Rivinius, Sebastian Hasler, Pascal Reisert, Ralf Küsters

- **Constrained Pseudorandom Functions from Homomorphic Secret Sharing.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-30620-4_7)
  Alain Passelègue, Geoffroy Couteau, Mahshid Riahinia, Pierre Meyer

- **Circuit-Free General-Purpose Multi-Party Computation via Co-Utile Unlinkable Outsourcing.**
  2023 · MPC · [TDSC](https://doi.org/10.1109/TDSC.2021.3138826)
  Jesús A. Manjón, Josep Domingo-Ferrer

- **COMBINE: COMpilation and Backend-INdependent vEctorization for Multi-Party Computation.**
  2023 · MPC · [ACM CCS](https://doi.org/10.1145/3576915.3623181)
  Muhammad Ishaq, Benjamin Sherman, Lindsey Kennard, Ana L. Milanova, Benjamin Levy, Vassilis Zikas

- **Breaking and Fixing Garbled Circuits When a Gate has Duplicate Input Wires.**
  2023 · MPC · [Journal of Cryptology](https://doi.org/10.1007/S00145-023-09472-4)
  Thomas Schneider, Raine Nieminen

- **Bingo: Adaptivity and Asynchrony in Verifiable Secret Sharing and Distributed Key Generation.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-38557-5_2)
  Philipp Jovanovic, Mary Maller, Ittai Abraham, Gilad Stern, Sarah Meiklejohn

- **Adaptively Secure MPC with Sublinear Communication Complexity.**
  2023 · MPC · [Journal of Cryptology](https://doi.org/10.1007/S00145-023-09446-6)
  Ran Cohen, Daniel Wichs, Abhi Shelat

- **Adaptive Distributional Security for Garbling Schemes with 𝒪(\|x\|) Online Complexity.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-981-99-8721-4_5)
  Estuardo Alpirez Bock, Sabine Oechsner, Kirthivaasan Puniamurthy, Pihla Karanko, Christopher Brzuska

- **Actively Secure Garbled Circuits with Constant Communication Overhead in the Plain Model.**
  2023 · MPC · [Journal of Cryptology](https://doi.org/10.1007/S00145-023-09465-3)
  Yuval Ishai, Carmit Hazay, Muthuramakrishnan Venkitasubramaniam

- **A New Framework for Quantum Oblivious Transfer.**
  2023 · MPC · [series/lncs](https://doi.org/10.1007/978-3-031-30545-0_13)
  James Bartusek, Amit Agarwal, Nishant Kumar, Dakshita Khurana

- **3-Party Secure Computation for RAMs: Optimal and Concretely Efficient.**
  2023 · MPC · [TCC](https://doi.org/10.1007/978-3-031-48615-9_17)
  Atsunori Ichikawa, Ilan Komargodski, Ryo Kikuchi, Koki Hamada, Dai Ikarashi

### 2022

- **Programmable Distributed Point Functions**
  2022-08-15 · MPC · [IACR ePrint](https://eprint.iacr.org/2022/1060)
  Elette Boyle, Niv Gilboa, Yuval Ishai, Victor I. Kolobov

  <details><summary>摘要 / Abstract</summary>

  A distributed point function (DPF) is a cryptographic primitive that enables compressed additive sharing of a secret unit vector across two or more parties. Despite growing ubiquity within applications and notable research efforts, the best 2-party DPF construction to date remains the tree-based construction from (Boyle et al, CCS&#x27;16), with no significantly new approaches since. We present a new framework for 2-party DPF construction, which applies in the setting of feasible (polynomial-size) domains. This captures in particular all DPF applications in which the keys are expanded to the full domain. Our approach is motivated by a strengthened notion we put forth, of programmable DPF (PDPF): in which a short, input-independent &quot;offline&quot; key can be reused for sharing many point functions. * PDPF from OWF: We construct a PDPF for feasible domains from the minimal assumption that one-way functions exist, where the second &quot;online&quot; key size is polylogarithmic in the domain size $N$. Our approach offers multiple new efficiency features and applications: * Privately puncturable PRFs: Our PDPF gives the first OWF-based privately puncturable PRFs (for feasible domains) with sublinear keys. * $O(1)$-round distributed DPF Gen: We obtain a (standard) DPF with polylog-size keys that admits an analog of Doerner-shelat (CCS&#x27;17) distributed key generation, requiring only $O(1)$ rounds (versus $\log N$). * PCG with 1 short key: Compressing useful correlations for secure computation, where one key is of minimal size. This provides up to exponential communication savings in some application scenarios.

  匹配依据：MPC: secure computation

  </details>

### 2019

- **Revisiting Shared Data Protection Against Key Exposure**
  2019-01-23 · MPC · [arXiv](https://arxiv.org/abs/1901.08083)
  Katarzyna Kapusta, Gerard Memmi, Matthieu Rambaud

  <details><summary>摘要 / Abstract</summary>

  This paper puts a new light on secure data storage inside distributed systems. Specifically, it revisits computational secret sharing in a situation where the encryption key is exposed to an attacker. It comes with several contributions: First, it defines a security model for encryption schemes, where we ask for additional resilience against exposure of the encryption key. Precisely we ask for (1) indistinguishability of plaintexts under full ciphertext knowledge, (2) indistinguishability for an adversary who learns: the encryption key, plus all but one share of the ciphertext. (2) relaxes the &quot;all-or-nothing&quot; property to a more realistic setting, where the ciphertext is transformed into a number of shares, such that the adversary can&#x27;t access one of them. (1) asks that, unless the user&#x27;s key is disclosed, noone else than the user can retrieve information about the plaintext. Second, it introduces a new computationally secure encryption-then-sharing scheme, that protects the data in the previously defined attacker model. It consists in data encryption followed by a linear transformation of the ciphertext, then its fragmentation into shares, along with secret sharing of the randomness used for encryption. The computational overhead in addition to data encryption is reduced by half with respect to state of the art. Third, it provides for the first time cryptographic proofs in this context of key exposure. It emphasizes that the security of our scheme relies only on a simple cryptanalysis resilience assumption for blockciphers in public key mode: indistinguishability from random, of the sequence of diferentials of a random value. Fourth, it provides an alternative scheme relying on the more theoretical random permutation model. It consists in encrypting with sponge functions in duplex mode then, as before, secret-sharing the randomness.

  匹配依据：MPC: secret sharing

  </details>

## TEE（152）

### 2026

- **LLMs in Cloud: A Discussion on Architecture, Orchestration, and Inference**
  2026-10-24 · TEE · [arXiv](https://arxiv.org/abs/2610.33475)
  Jannatun Noor, Athar Noor Mohammad Rafee, Md. Sadman Haque, Sreezon Das Gupta, Atiar Osman, Md. Abu Obaida Zishan

  <details><summary>摘要 / Abstract</summary>

  The widespread deployment of foundational Large Language Models (LLM) across cloud datacenters marks a fundamental paradigm shift from stateless deep learning toward distributed, memory-intensive generative workloads. However, serving massive foundation models under stringent Service Level Objectives (SLO) exposes critical physical and system bottlenecks. These challenges include the persistent High Bandwidth Memory (HBM) wall, operational asymmetry between compute-bound prefilling and memory-bandwidth-bound decoding, explosive Key-Value (KV) cache expansion, prohibitive serverless cold starts, and hardware reliability vulnerabilities. Existing literature reviews remain layer-siloed, decoupling low-level accelerator virtualization from cluster orchestration and runtime inference, while largely overlooking defining advancements from 2024 to 2026. To address these limitations, this study presents a comprehensive, cross-layer systematic review guided by the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) 2020 framework. We synthesize a holistic taxonomy unifying hardware virtualization, cluster-level scheduling, and runtime inference optimizations, including iteration-level continuous batching, prefill-decoding disaggregation, and hierarchical KV cache offloading. Furthermore, we evaluate resilient cloud-native service architectures, examining scale-to-zero serverless paradigms, fault-tolerant checkpointing against silent data corruption, and hardware-enforced Trusted Execution Environments (TEEs) for multi-tenant isolation. Finally, we formalize the multi-dimensional Pareto trade-offs governing throughput, latency, monetary cost, and confidentiality, outlining a forward-looking research roadmap spanning Compute Express Link (CXL) memory pooling, in-memory computing, and autonomous multi-agent control planes to guide future cloud LLM infrastructure.

  匹配依据：TEE: trusted execution environments

  </details>

- **KNOX: Hardware-assisted Regulatory Sandbox for Generative Models**
  2026-10-20 · TEE · [arXiv](https://arxiv.org/abs/2610.27543)
  Vasisht Duddu, Adam Caulfield, Xi He

  <details><summary>摘要 / Abstract</summary>

  Regulations require companies to run AI models in a regulatory sandbox, an isolated environment that enables monitoring model behavior by regulators, prior to deployment. But, they do not spell out the technical mechanisms to design such a sandbox. Ideally, a regulatory sandbox should show (i) compliance (checks against regulations, and deviations from intended behavior, i.e., unauthorized tool and system calls); (ii) confidentiality (protects model weights from regulators); (iii) attestability (produces tamper-resistant evidence of model behavior for monitoring); and (iv) scalability (evidence is verifiable by multiple regulators). Several prior works (information-flow control, prompt-injection defenses, control-flow integrity, and traditional sandboxing) address specific compliance aspects but lack confidentiality, attestability, and scalability. TEEs meet some of these requirements, but simply running models inside a TEE is insufficient as we need compliance mechanisms. We present KNOX, the first regulatory sandbox, built by running AI workloads inside TEEs. We demonstrate KNOX using agentic workloads. For compliance, we derive an attested policy manifest (with the applicable regulations, the expected tool calls, and the permitted system calls) for a given user prompt. Before an executor performs an action, an attested reference monitor compares it against the attested policy manifest and allows it only if it matches. Every action and verdict is recorded in an attested execution graph, enabling regulators to verify the model&#x27;s execution and its compliance. We show that KNOX meets all requirements, and can check for compliance with regulations and deviations from intended behavior (e.g., due to prompt injection); and incurs low overhead (&lt;1%).

  匹配依据：TEE: tees (context)

  </details>

- **DISCO\*: DIstributed and SCalable Oblivious Joins and Oblivious Primitives**
  2026-10-20 · TEE · [IACR ePrint](https://eprint.iacr.org/2026/2572)
  Apostolos Mavrogiannakis, Xian Wang, Ioannis Demertzis, Dimitrios Papadopoulos, Minos Garofalakis

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) let clients outsource computation to untrusted clouds, but they remain vulnerable to side-channel and leakage-abuse attacks. Recent work closes this gap by combining hardware enclaves with oblivious computation, which offers strong security guarantees yet struggles to meet the performance and scalability demands of real-world deployments. In this work, we present DISCO, the first scalable, distributed, and fully oblivious database system that seamlessly combines hardware enclaves with cutting-edge oblivious primitives and novel optimizations that significantly reduce inter-server communication overheads. What distinguishes DISCO from prior work is a suite of distributed frameworks that unlock parallel computation and fundamentally shift the design paradigm of distributed oblivious systems, enabling practical deployment at scales that were unattainable with previous solutions. We provide a thorough evaluation of the performance of our system on both synthetic and real-world datasets. Our evaluation demonstrates that our design significantly reduces the gap between theory and practice, achieving 88× speedup over Jodes and 180× over SODA on non-foreign key joins with N = 2²⁵ elements. Most importantly, we report, for the first time, results for computations at the terabyte scale.

  匹配依据：TEE: hardware enclaves, trusted execution environments

  </details>

- **Pangolin: Efficient DAG-based BFT State-Machine Replication with TEE-Accelerated Commitment**
  2026-10-19 · TEE · [arXiv](https://arxiv.org/abs/2610.26295)
  Paul Franke-Bergmann, Maya Kuhlmann, Alexander Heß, Marc Leinweber, Rüdiger Kapitza, Hannes Hartenstein, Franz J. Hauck, Christian Berger

  <details><summary>摘要 / Abstract</summary>

  Currently many Byzantine fault-tolerant (BFT) protocols use directed acyclic graphs (DAGs) to let replicas propose blocks of requests in parallel for improved throughput. Yet, the existing DAG-based designs mainly consider the atomic-broadcast layer: They typically do not describe an efficient client interaction layer, their garbage collection is either unspecified or relies on trusted external storage, and the lowest-latency designs rely on timing assumptions that may be violated in geo-distributed deployments. In this paper, we propose the Pangolin protocol: It introduces a novel low-latency DAG-based atomic broadcast layer and completes it into an efficient state-machine replication (SMR) framework. To preserve system throughput, clients issue requests to a single replica and verify replies efficiently via compact execution proofs. Furthermore, Pangolin introduces a new garbage-collection scheme for DAGs which bounds memory usage even under full asynchrony. Pangolin leverages trusted execution environments to tolerate f Byzantine faults with only n &gt;= 2f + 1 replicas and accelerates vertex commitments significantly: Broadcasting certified vertices requires only a single communication step, and commit rules are refined to commit both frequently and early without revealing the coin-elected anchor. This way, Pangolin overtakes the fastest partially synchronous DAG protocols while being live under asynchrony: In our evaluation, Pangolin achieves an average 1.27x (up to 1.52x) latency speedup over Mysticeti.

  匹配依据：TEE: trusted execution environments

  </details>

- **Empirical Analysis of TEE-Enabled Rollup Designs**
  2026-10-16 · TEE · [arXiv](https://arxiv.org/abs/2610.24284)
  Claudiu-Nicu Bărbieru, Corentin Libert, Peterson Yuhala, Andrei Arusoaie, Matthieu Bettinger, Oana-Otilia Captarencu, Pascal Felber, Emanuel Onica, Etienne Rivière, Valerio Schiavoni

  <details><summary>摘要 / Abstract</summary>

  Layer 2 (L2) rollups have become the dominant scaling solution in Ethereum. At the core of these systems lies the rollup sequencer, a component that orders, executes, and submits L2 transaction blocks to the main Ethereum blockchain. The centralization of this sequencer introduces security risks, including censorship and malicious manipulation of transactions to extract maximum extractable value (MEV). Trusted execution environments (TEEs) provide strong hardware-enforced confidentiality and integrity guarantees for code and data. TEEs are strong candidates for strengthening security and ensuring verifiable neutrality in rollup sequencer operations, but multiple TEE-based designs are possible, offering different trade-offs among modularity, performance, and security guarantees. Among them, the separation of proposer and builder logic (PBS) into independent services is a strong contender against the monolithic approach that bundles all sequencer logic. Despite several proposed theoretical frameworks, there is a lack of experimental evaluation of the practicality and security trade-offs of integrating TEEs into rollup sequencers. This work addresses this gap through a comprehensive empirical study of TEE-enabled rollup designs under both PBS and monolithic sequencer models. Our experimental evaluations show that the impact of TEEs on rollup performance is small and that PBS does not significantly amplify it. We also show that PBS can lead to significant performance improvements by enabling more specialized, efficient builder logic implementations.

  匹配依据：TEE: trusted execution environments

  </details>

- **When Rotation Bounds Nothing: Streaming Image Classifiers to Field Nodes Under Physical Capture**
  2026-10-15 · TEE · [arXiv](https://arxiv.org/abs/2610.21276)
  Daniel Gilkarov, Ran Dubin

  <details><summary>摘要 / Abstract</summary>

  Field nodes run image classifiers locally, exposing a first-class asset, the trained model, to theft. Trusted-execution enclaves, collaborative-inference splits, and encrypted storage assume the device owner is the adversary from deployment. Here the operator owns the node, and an adversary seizing it reads only what cold-boot capture finds resident. One answer stores nothing: a chunkable multi-exit model streams into volatile memory, rotating to bound residency. We characterise the capture envelope on real LTE traces across two victims of one architecture, against passive and adaptive adversaries. Neither survives a capable adversary; recovery cost alone differs. Against a from-scratch victim the uncaptured stages must be learned: the adaptive adversary gains most at shallow seizures, ends the CIFAR-10 envelope at every rotation, and stays rotation-bounded on CIFAR100, from 42.6% of usable seizures at 5 s to 86.8% at 30 s. Against the same architecture sliced from a public pretrained backbone, the adversary downloads those stages, recovering at least 90% of maximum accuracy at all depths, taking usable CIFAR-100 seizures from 0.0% to 97.3% at 5 s, given the victim&#x27;s full labelled training set. Delivery-side secrecy raises a seizure&#x27;s price; a public copy of the withheld stages erases it.

  匹配依据：TEE: enclaves (context)

  </details>

- **BiShield-TEE: On the (In-)Security of Unilateral Weight Obfuscation in On-Device TEE-Shielded LLM Partition**
  2026-10-15 · TEE · [arXiv](https://arxiv.org/abs/2610.21565) · [Code](https://github.com/laduiw/BiShield-TEE)
  Zhiyuan Wang, Yuezhi Zhou, Ziqi Zhang, Zhu Zhang, Zhixing Tan, Yongheng Deng

  <details><summary>摘要 / Abstract</summary>

  On-device deployment of large language models (LLMs) is increasingly adopted due to latency and privacy requirements, but exposes proprietary models to reverse engineering and intellectual property theft. Trusted Execution Environments (TEEs) provide hardware-enforced isolation for on-device inference, yet most TEE-based parameter obfuscation relies on unilateral matrix transformations that obfuscate only the output side. We identify a vulnerability in this design, termed the Solution Determinacy Property (SDP): the obfuscation secret is uniquely determined, exposing the structure of the true key and enabling attackers to break the protection. Under our attacks, representative methods GroupCover and ArrowCloak are reduced to negligible protection, with attack accuracy reaching over 2.4 times the full-shielding black-box baseline and recovering near-complete model functionality. To address this vulnerability, we propose BiShield-TEE, a bilateral framework that induces Ambiguous Solutions through joint obfuscation of input and output dimensions, hiding the true key among many equally valid candidates. Experiments across diverse models and datasets show that BiShield-TEE confines attack accuracy to the full-shielding black-box baseline, while achieving higher inference efficiency than prior methods on real hardware. Our code is available at https://github.com/laduiw/BiShield-TEE.

  匹配依据：TEE: trusted execution environments

  </details>

- **Snapshots of TEE-Based Encrypted Databases Leak Plaintext Histograms via Dendrochronology**
  2026-10-13 · TEE · [IACR ePrint](https://eprint.iacr.org/2026/2465)
  Zachary Espiritu

  <details><summary>摘要 / Abstract</summary>

  Arborists use dendrochronology, or the study of tree &quot;growth rings&quot; (as in, the plant), to infer past environmental events. We identify an analogous, exploitable phenomenon in the indexes used by several encrypted databases (EDBs) based on trusted execution environments (TEEs). Such EDBs have been shown to leak the order of indexed values, but not the histogram (or frequency of each value), with respect to a weaker class of snapshot adversaries. This order-only leakage substantially reduces the impact of possible inference attacks. We show, in fact, frequency is recoverable in the snapshot model from many TEE-based EDBs, even if the TEE itself is &quot;secure&quot;. Our insight is simple: practical storage engines impose a strict total order on indexed keys by augmenting each key with a unique tie-breaker. If the adversary learns information about the tie-breakers, they can recover the frequencies of plaintext keys. We show this enables stronger inference attacks on several TEE-based EDBs (including Microsoft SQL Server’s Always Encrypted, StealthDB, and HeDB) to demonstrate this vulnerability’s ubiquity and point to broader lessons for TEE applications designed around legacy code.

  匹配依据：TEE: trusted execution environments

  </details>

- **FLAI Protocol: Decentralized Federated Learning with On-Chain Rewards and sPEG-Based Contribution Scoring**
  2026-10-13 · TEE · [arXiv](https://arxiv.org/abs/2610.17546)
  Eli Yune, Mahesh Balan

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) enables collaborative model training without data centralization but struggles with incentive alignment, accountability, and robustness under heterogeneous non-IID data. Existing decentralized FL (DeFL) systems leverage blockchains for coordination yet face high on-chain overhead, unverifiable self-reports, and weak fairness guarantees. We present the FLAI Protocol, a trusted execution environment (TEE)-backed DeFL framework that integrates enclave-validated aggregation, sparse Peer Evaluation Graph (sPEG) scoring, and on-chain settlement. sPEG incorporates peer-based quality, class coverage, promptness, effort, and reputation into composite contribution scores. The protocol formalizes contribution evaluation and tokenized incentive distribution, ensuring verifiable fairness and resilience against free-riding and collusion. We evaluate FLAI on image, text, and healthcare datasets and demonstrate parity with FedAvg in utility while improving fairness and accountability. A case study in consumer eHealth (aggregating wearable and electronic health record data for real-world evidence generation) illustrates the protocol&#x27;s applicability to privacy-critical domains where equitable rewards, auditability, and data sovereignty are essential.

  匹配依据：TEE: trusted execution environment

  </details>

- **Resource-constrained Remote Attestation of Smart Meters Using Merkle Trees in a Trusted Execution Environment**
  2026-10-12 · TEE · [arXiv](https://arxiv.org/abs/2610.16373)
  Amirhossein Shakiba, Hamid Reza Ghaeini, Sadegh Dorri Nogoorani

  <details><summary>摘要 / Abstract</summary>

  Smart meters are pivotal to the functioning of smart grids, as they measure and transmit energy consumption data that includes sensitive information about household energy usage patterns. While this data offers significant financial benefits, it can also reveal detailed insights into residents&#x27; daily routines, making the security of smart meters a critical concern. This paper introduces a novel remote attestation method for smart meters that ensures the integrity and privacy of data exchanged between smart meters and central servers while detecting unauthorized tampering. Our approach structures the communication data into a Merkle Tree-a hash data structure that facilitates efficient data integrity and authenticity verification. All operations involved in constructing the Merkle root and hashing critical data are executed in the secure environment of a Trusted Execution Environment (TEE) using OP-TEE, thereby maintaining the integrity and security of the smart meter&#x27;s data. Comparing our experimental results with the related works highlights the superiority of our method in terms of resource efficiency, security robustness, and the feasibility of implementation on smart meters and resource-constrained devices, thereby enhancing the overall security and reliability of smart grid systems.

  匹配依据：TEE: trusted execution environment

  </details>

- **A methodology to derive security specifications for complex electronic systems**
  2026-10-12 · TEE · [IACR ePrint](https://eprint.iacr.org/2026/2447)
  Sylvain Guilley, Ritu Ranjan Shrivstwa, Ville Yli-Mäyry

  <details><summary>摘要 / Abstract</summary>

  Modern electronic systems are becoming increas- ingly complex and must satisfy demanding performance, power, and area (PPA) constraints. Consider for instance artificial intelligence chips, aiming at datacenters running LLMs or at automotive perception, which manipulate massive data streams. Beyond performance considerations, these systems must also provide increasingly strong security and dependability guaran- tees. Indeed, when electronic systems are based on chiplets, for instance, the supply chain gets longer and therefore brings a larger number of threats. Also, those systems are very versatile, in that they can run varied multi-tenant applications. Therefore, defining what security features are required in this context with numerous stakes is not trivial. Existing scholarly research is very relevant when the security problem is well defined. The resulting scientific papers accord- ingly dig very deep: this modus operandi has proved productive in exploring new problems, and actually allowed to come up with innovative solutions. For instance, in the field of side-channel attacks, varied mitigations alongside with metrics to evaluate them have been devised. Increasing sophistication resulted from this research, as external considerations have been injected into the problem (typically, aspects such as attack order, impact of combinatorial glitches, etc.). Therefore, we face today the question of selecting the most suitable technology amongst the proliferation of state-of-the-art techniques. In addition, in complex systems, we encounter another prob- lem, namely that of defining the security problem(s). A fruitful approach in this respect is a risk based approach. Specifically, the application of a risk-oriented methodology allows to reason on the security rationale. It proceeds as follows. First, the system missions are listed. Then for each of them, the necessary assets are deduced. A threat analysis allows to identify how assets are threatened, and eventually, security requirements can be enunciated. At this stage, the task of matching relevant countermeasures becomes straightforward. This paper illustrates the methodology by deriving security specifications for datacenter and automotive chiplets. The considered missions are (secure) provisioning, trimming, debugging, booting, and remote attestation.

  匹配依据：TEE: tees (context)

  </details>

- **ARMOR: Adversary Cost Amplification via a Schema-Preserving Password-Hardening Retrofit for Resource-Constrained Systems**
  2026-10-09 · TEE · [arXiv](https://arxiv.org/abs/2610.14300)
  Avinash Srinivasan

  <details><summary>摘要 / Abstract</summary>

  Credential-database disclosure exposes Internet of Things gateways, edge servers and legacy verifiers to offline password guessing. Memory-hard key derivation functions (KDFs) are preferred but can exceed constrained-device budgets. ARMOR addresses this deployment gap with a schema-preserving verifier-side transform for database-only compromise, assuming an isolated Chain Registry. The registry holds secret per-account chains of injective operations; fixed terminal escape encoding preserves distinct pre-hash values under each chain while moving outputs outside printable ASCII. This disrupts evaluated stock tools&#x27; candidate coverage, but chain-aware attackers can generate the transformed bytes directly. We therefore evaluate a bounded chain-aware attack on $1{,}000$ paired salted-MD5 targets: it executes $89.35\times$ the plain arm&#x27;s counted salted checks, reproduced on A6000 and A100. All target passwords are in the bounded pool; same-target ambiguity enumeration and simulated login trials recover every original password. These results describe the implemented attack, not minimum attacker cost. Bare-metal transforms take microseconds, while protected storage dominates the measured TrustZone-M components; these are component measurements, not complete authentication times. ARMOR thus provides bounded chain uncertainty under registry isolation with low transform cost, although an isolated high-entropy pepper remains cryptographically stronger. ARMOR composes as KDF(ARMOR(password)) when resources permit and the KDF accepts the complete transformed output.

  匹配依据：TEE: trustzone

  </details>

- **Protecting CPU AI On Edge TEEs: WebAssembly's Promise and Practical Challenges**
  2026-10-08 · TEE · [arXiv](https://arxiv.org/abs/2610.12050)
  Friedrich Vandenberghe, Lachlan J. Gunn, Bruno Volckaert, Merlijn Sebrechts

  <details><summary>摘要 / Abstract</summary>

  AI models on edge hardware contain important intellectual property (IP), but an adversary can steal it when they achieve root access. Trusted Execution Environments (TEE) like Arm TrustZone protect against these Operating System (OS) level attacks. However, they are challenging to use. More precisely, it is difficult to run unaltered applications inside a TEE. This work presents a solution that allows the execution of unaltered AI models, compiled to WebAssembly, on the WebAssembly Micro Runtime (WAMR) in OP-TEE for Arm TrustZone. Additionally, this work provides an AI model distributor that encrypts the WebAssembly binary and places the encryption key in one of the device&#x27;s fuses. This way, only the WAMR Trusted Application (TA) in OP-TEE can decrypt and execute the AI model. A thorough evaluation of our solution shows that it incurs an additional overhead of 22% in comparison to an application manually ported to OP-TEE, while also facilitating the execution of unaltered AI models with an additional inference latency of 6% without significant porting effort. Overall, there is a pressing need to safeguard the IP of AI models and this work shows that there is a real promise in WebAssembly, but there remain some practical challenges.

  匹配依据：TEE: trusted execution environments, trustzone

  </details>

- **Optimal Statistical Oblivious RAM and Search Tree in the External-Memory Model**
  2026-10-08 · TEE · [IACR ePrint](https://eprint.iacr.org/2026/2419)
  Andrew Krapivin, Elaine Shi

  <details><summary>摘要 / Abstract</summary>

  Oblivious RAM (ORAM) allows a trusted client to access (encrypted) data stored in untrusted memory, such that the access patterns reveal nothing about the data or the queries. It is well-known that any ORAM scheme must suffer from a logarithmic overhead. More precisely stated, each request must incur $\Omega(\log_B N)$ block transfers on average, where $N$ is the size of the logical memory and $B$ is the block size of the oblivious implementation. Moreover, the same lower bound extends to oblivious Search Trees (ST). For upper bounds, however, we have been long stuck with a $(\log_B N)^2$ curse on two fronts: (1) Log-squared curse for statistically secure ORAMs: although optimality is known for computationally secure ORAMs for $B = \Theta(1)$ or $B \geq \log^{1+\epsilon} N$ (where $\epsilon &gt; 0$ is an arbitrarily small constant), progress has been stagnant when it comes to statistical security. (2) Log-squared curse for oblivious search trees: for search trees, we do not know how to overcome the log-squared curse even when allowing computational assumptions. In this paper, we break this long-standing log-squared curse for both oblivious search trees and statistically secure ORAM on broad parameter regimes: (1) Our first result gives an optimal, statistically secure ORAM with $O(\log_B N)$ cost as long as $B \geq \log^{1+\epsilon} N$. (2) Our second result gives an optimal, statistically secure oblivious search tree with $O(\log_B N)$ cost when $B \geq \log^{2+\epsilon} N$, matching the performance of the best known non-oblivious search trees in this parameter region. Notably, this means that for search trees, we can get obliviousness for free! The assumptions on $B$ required to achieve optimality are standard and mild. They not only coincide with the standard wide cache-line assumption prevalent in the classical algorithms literature, but also align well with the hardware-enclave architectures that employ oblivious algorithms in practice, such as the implementations of Signal and Meta.

  匹配依据：TEE: hardware enclave

  </details>

- **Enabling Extended SGX Enclaves inside Confidential Virtual Machines**
  2026-10-08 · TEE · [arXiv](https://arxiv.org/abs/2610.12695)
  Pamenas Kariuki, Dong Yiliang, Quoc Do Le, Christof Fetzer

  <details><summary>摘要 / Abstract</summary>

  Confidential Virtual Machines (CVMs), such as AMD SEV-SNP, and process enclaves, such as Intel SGX, provide workload protection against cloud threats. However, they strongly differ in TCB, deployment cost and speed, peer workload protection, resource sharing, fine-grained isolation and attestation, and programming capabilities. Nesting process enclaves within CVMs offers an optimal solution and an opportunity to address long-standing SGX limitations: lack of intra-enclave protection, expensive transitions and exception paths, slow enclave cloning, and a restricted programming model that limits Library Operating Systems (LibOS). This paper introduces TEEVisor, a CVM-resident architecture consisting of a security monitor and a kernel driver that leverages AMD SEV-SNP Virtual Machine Privilege Levels (VMPLs) to build hardware-protected, process-level enclaves inside a guest CVM with two modes: (1) an SGX binary compatibility mode to run unmodified SGX applications; and (2) a novel extended SGX~(eSGX) mode optimizing slow execution paths and offering richer enclave programming capabilities. On commercial AMD EPYC hardware, against native CVM execution, TEEVisor incurs under 5% overhead on compute- and memory-bound workloads, around 12% on I/O-heavy applications, and accelerates enclave cloning to a rate of 93~$μ$s/MB of enclave size, demonstrating that eSGX semantics inside a CVM are practical for production use.

  匹配依据：TEE: amd sev, intel sgx, sgx, sgx enclaves

  </details>

- **Hashing Beats Trees: Practical Oblivious Dictionaries in SGX**
  2026-10-07 · TEE · [IACR ePrint](https://eprint.iacr.org/2026/2397)
  Erik-Oliver Blass, Travis Mayberry

  <details><summary>摘要 / Abstract</summary>

  Oblivious RAM (ORAM) is a powerful cryptographic primitive that hides both the contents of outsourced data and the access pattern to the data. However, it offers only a restrictive array-based interface. A principal obstacle to its deployment is building an efficient oblivious dictionary upon it. To build such a dictionary, the state-of-the-art layers an oblivious AVL tree over ORAM, avoids an expensive local position map, but forces every operation to traverse a full root-to-leaf path, costing $\Theta(\log n)$ ORAM accesses. We show this trade-off to be suboptimal, particularly when deployed in a common setup within a trusted execution environment like SGX. There, a small amount of client memory can reduce the position map recursion depth to three levels or less, rendering its overhead relatively small. With low position map cost, probabilistic hash tables prevail as dictionary data structures due to their small, constant number of accesses compared to $\Theta(\log n)$ path traversal of a tree. We implement and analyze oblivious, probabilistic hash tables over Path ORAM, including several different strategies: chaining, power-of-two-choices, stash-less cuckoo, and de-amortized cuckoo hashing. Execution of these algorithms within a secure enclave requires &quot;double obliviousness&quot;, which in turn needs strict concrete maximum cost limits for each access that current literature does not provide. We derive these concrete padding parameters bounding the hash table rebuild probability to $\le 2^{-40}$ via large-scale simulation. In an SGX deployment, our constructions outperform oblivious trees by up to $20\times$ for $\mathsf{lookup}$s and $12\times$ for $\mathsf{insert}$s.

  匹配依据：TEE: secure enclave, sgx, trusted execution environment

  </details>

- **PRA-TLS: Attestation of a Client Application for TEE**
  2026-10-05 · TEE · [arXiv](https://arxiv.org/abs/2610.06061)
  Reina Sasaki, Yutaka Ishikawa, Atsuko Takefusa, Masato Oguchi

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) are secure foundations for protecting sensitive information and executing computations over confidential data. Processing in an isolated execution environment (enclave) is invoked by an untrusted application in the Rich Execution Environment (REE). Then the enclave returns the execution results to the untrusted application. Even if the enclave has been attested, the boundary between the enclave and the untrusted application poses risks, such as tampering with input arguments or return values and manipulating the order in which the application invokes functions. Therefore, it is necessary to establish the authenticity and integrity of not only the enclave itself but also the application and its execution environment. In this study, we propose an attestation protocol, Portable Remote Attestation TLS (PRA-TLS), for a client application that invokes an enclave. We introduce a daemon that acts as an attester. PRA-TLS uses a trusted Attester Daemon to measure the state of the host environment and application code at runtime, providing these measurements as attestation evidence for verification by a remote Verifier. This mechanism allows the enclave to proceed only when the software environment is in the expected state and the application code is verified as legitimate. We define attack models and security requirements for the proposed protocol and formally evaluate its security using the Tamarin Prover. Furthermore, we implement a prototype of PRA-TLS using Intel SGX and evaluate its performance.

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **Attestable Audit: Property-Based Attestation for Proprietary Workloads without Artifact Disclosure**
  2026-10-03 · TEE · [arXiv](https://arxiv.org/abs/2610.04480)
  Takuma Imamura

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) prove the integrity of code and data to a remote peer through remote attestation: the TEE issues an attestation report by signing, with a hardware-bound key, its configuration information, including measurements (cryptographic digests) of the code loaded inside it. A verifier appraises the report by matching these measurements against reference values. When the measured artifact is proprietary, however, the verifier cannot derive the reference values itself: it can only confirm that something with a given measurement is running inside the TEE---not that the program behaves as expected---forcing full trust in the reference value provider. We propose an architecture that closes this gap without disclosing the artifact, composing two TEE workloads: attestable build (Hugenroth et al., 2025), which binds a source code digest to a build artifact measurement, and attestable audit (proposed in this paper), which binds the same source code digest to the verdicts of automated audits---fuzzing, static analysis, AI code auditing, formal methods---executed inside a TEE. Both are instances of Confidential Computing Proofs: TEE attestation viewed as a hardware-backed zero-knowledge proof. Chaining the two certificates lets the verifier conclude that the running artifact was built from source code satisfying the audited properties, without disclosing either the source code or the build artifact. A proof-of-concept implementation on Intel SGX with the Gramine Library OS, running the Bandit security analyzer on Python code, demonstrates the practicality of the approach.

  匹配依据：TEE: confidential computing, intel sgx, trusted execution environments

  </details>

- **Extending eBPF observability to Non-standard execution environments**
  2026-09-30 · TEE · [arXiv](https://arxiv.org/abs/2609.39530)
  Pamenas Kariuk, André Martin, Christof Fetzer

  <details><summary>摘要 / Abstract</summary>

  eBPF observability of non-standard execution environments (NEEs) like TEEs or LibOSes is hindered by their unconventional exception-handling and memory-access mechanisms that limit standard Linux tooling. This work introduces two mechanisms that enable eBPF-based observability for NEEs: (1) kernel memory extensions for safely accessing NEE memory from eBPF programs, and (2) a lightweight flexible probe performance measurement unit (LWFP PMU) that provides flexible and generic probing, for NEEs, through the following LWFP: simple (SLWFP), enclave (ELWFP) and extended (ExLWFP) probes. We demonstrate the practicality of these extensions by developing tooling for tracing, stack sampling with Flame Graphs, dynamic instrumentation, timing analysis, and USDT support for Intel SGX enclaves and LibOSes. Performance measurements show that SLWFP probes achieve a latency of 394 ns, outperforming uprobes, which exhibit 25% higher latency, while ELWFP probes incur a latency ~2.8 microseconds, which is practical for enclave observability. The addition of SLWFP introduces negligible overhead to existing uprobe performance. Taken together, this work lays the foundation for closing the long-standing gap between NEE tooling and Linux observability tooling by enabling generic and reusable eBPF tooling for diverse NEE hardware and software architectures.

  匹配依据：TEE: intel sgx, sgx enclaves

  </details>

- **TEE Anchor: Cross-TEE Organizational Endorsement for Mitigating TEE Physical Attacks**
  2026-09-28 · TEE · [arXiv](https://arxiv.org/abs/2609.35919)
  Ao Sakurai

  <details><summary>摘要 / Abstract</summary>

  In 2025, practical physical-access attacks against TEEs, such as TEE.fail and Battering RAM, were disclosed, posing a serious threat to current TEEs. The more strictly the target machine is guarded, the harder such attacks are to mount. Residing under trusted management has therefore emerged as a new security requirement. Yet existing attestation cannot prove a machine&#x27;s organizational affiliation. This leaves room for an attacker to pass off a physically accessible machine under their control as one operated in a legitimate environment. We propose TEE Anchor, a mechanism that mitigates physical attacks by proving which organization manages a machine. TEE Anchor is a lightweight, X.509-based design that needs no additional root of trust such as a (v)TPM. The organization issues a certificate over the Chip ID, a unique per-CPU identifier, forming its own PKI. A Verifier then proves affiliation by matching the Chip ID in the attestation evidence against that certificate. This outperforms (v)TPM-based prior work in operational cost and deployability, applies across major TEEs without vendor lock-in, and lets any organization assert affiliation independently of TEE vendors. We implemented a prototype and confirmed that all operations, including provisioning and verification, complete within a few milliseconds.

  匹配依据：TEE: tee (context)

  </details>

- **INTCC: A Framework for Interactive Confidential Computing**
  2026-09-28 · TEE · [arXiv](https://arxiv.org/abs/2609.35552)
  Qingzhe Bing, Kaiyuan Zhang, Yinqian Zhang

  <details><summary>摘要 / Abstract</summary>

  Confidential computing leverages Trusted Execution Environments (TEEs) to ensure the confidentiality and integrity of data in use. However, TEEs rely on remote attestation to guarantee the integrity of their initial memory state. This model is fundamentally at odds with interactive development workflows. In scenarios like LLM fine-tuning and exploratory data analysis, data processors need human-in-the-loop capabilities, including dynamic code injection, intermediate state inspection, and hyperparameter tuning, all of which inherently violate the static, one-time integrity guarantees of traditional remote attestation. To reconcile this tension, we propose the interactive confidential computing paradigm, a system architecture enabling untrusted data processors to execute dynamic, non-deterministic operations within TEEs without compromising data confidentiality. Driven by the insight that inherently unmeasurable human interaction must be excluded from the Trusted Computing Base (TCB), we logically partition the TEE into an interactive controller and a verifiable runtime. To realize this paradigm, we present INTCC, a framework featuring three key mechanisms: (1) a proxy-based dispatch system to preserve the native development experience; (2) a fine-grained information flow control mechanism based on a security lattice to prevent data leakage; and (3) a privacy-preserving verifiable execution mechanism to guarantee the runtime compliance of dynamic workflows. We implement INTCC on AMD SEV-SNP using Confidential Containers and evaluate it across diverse real-world workloads. Our experiments demonstrate that INTCC effectively balances security and interactivity, incurring a practical overhead of less than 5% for LLM fine-tuning and under 17% for data analysis relative to baseline execution.

  匹配依据：TEE: amd sev, confidential computing, trusted execution environments

  </details>

- **Toward provably private learning from federated data**
  2026-09-25 · TEE · [arXiv](https://arxiv.org/abs/2609.31494)
  Katharine Daly, Yu Xiao, Zachary Garrett, Brett McLarnon, Jianpeng Hou, Arun Ganesh, Yanxiang Zhang, Noriyuki Takahashi, Haicheng Sun, Yuanbo Zhang, Timon Van Overveldt, Daniel Ramage

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) allows devices with private data to collaborate in training a shared model. We present a next-generation FL system based on Trusted Execution Environments (TEEs) that addresses operational challenges associated with earlier systems and provides externally verifiable central Differential Privacy (DP) guarantees for the first time while offering a better privacy-utility tradeoff. In our system, devices upload data encrypted with keys managed by a TEE-hosted Key Management Service (KMS). The uploaded data is cryptographically tied to a policy limiting the set of Python programs that may later process the data in server-side TEEs. External parties may inspect public transparency logs to observe the set of workloads allowed by these policies. Our experimental results show that the new system improves device coverage and favorably shifts privacy-utility curves by enabling collected data to be integrated into the server-side workload at a schedule that optimizes DP guarantees and is unaffected by device availability. Our new system has been productionized, enabling models for the Android Keyboard (Gboard) to be trained faster and achieve better accuracy under smaller, now externally verifiable privacy budgets in comparison to models trained using the prior system.

  匹配依据：TEE: trusted execution environments

  </details>

- **SpliTEE: Fast and Private LLM Inference by Coupling GPU-Assisted Trusted Execution Environments with Differential Privacy**
  2026-09-14 · TEE · [arXiv](https://arxiv.org/abs/2609.15039)
  Shashie Dilhara Batan Arachchige, Robin Carpentier, Hassan Jameel Asghar, Dali Kaafar

  <details><summary>摘要 / Abstract</summary>

  User prompts provided to large language models (LLMs) may contain private information. One way to protect them is to execute the LLM inside a trusted execution environment (TEE). However, this results in slow inference times as current TEEs are significantly slower than GPUs for LLM inference. To circumvent this, Tramèr and Boneh (2019) proposed Slalom which splits neural network inference between a TEE and an untrusted GPU. They encrypt inputs to computations outsourced to the GPU. In this paper, we extend this split-inference architecture to LLM inference and instead protect intermediate inputs using differential privacy (DP). We first demonstrate that masking intermediate representations is necessary by showing an 80% accuracy on a prompt-reconstruction attack from these representations. Our main contribution is a global sensitivity analysis of key functions in LLM inference, which bounds the required scale of DP noise. Unlike encryption, DP avoids quantization, allowing the LLM to remain in the floating-point domain. We also derive an upper bound on the floating-point error from masking and subsequent noise cancellation as a function of the privacy parameter epsilon, keeping the same quality of the LLM response. We implement our architecture using the Intel TDX TEE and two LLMs: Llama-3.2-3B and Qwen3-4B. Our split execution is nearly twice as fast as fully TDX-based inference. Moreover, it is at most 43% faster than Slalom while achieving higher accuracy. Finally, we demonstrate that prompt reconstruction, even with knowledge of the DP mechanism, cannot recover more information than is contained in an unrelated prompt.

  匹配依据：TEE: intel tdx, trusted execution environment, trusted execution environments

  </details>

- **Breaking Fault Lines: Unifying TEE-Assisted BFT Consensus in Partially Trusted Worlds**
  2026-09-09 · TEE · [arXiv](https://arxiv.org/abs/2609.09742)
  Xiaoqing Wen, Tong Liu, Jianyu Niu, Jialin Li, Cong Wang, Yinqian Zhang, Chen Feng

  <details><summary>摘要 / Abstract</summary>

  This paper revisits TEE-assisted BFT under a universal partial-TEE model, where an arbitrary subset of replicas execute inside TEEs while the remaining replicas operate without hardware trust guarantees. We show that heterogeneous trust changes the structure of quorum formation and fault tolerance. In particular, we derive a tight resilience bound f &lt; max {n/3, m/2}, where n is the total number of replicas and m is the number of TEE-enabled replicas. The result reveals a sharp threshold phenomenon: TEEs improve fault tolerance only once they exceed two-thirds of the deployment. Guided by this characterization, we introduce two protocol principles: (1) a dual-quorum construction that safely combines TEE-only and mixed quorums, and (2) a TEE-leader fast path that leverages hardware-enforced non-equivocation to reduce both consensus and view-change latency. We realize these ideas in Raftel, which is, to our knowledge, the first HotStuff-style BFT protocol designed explicitly for arbitrary partial-TEE deployments, and in chained-Raftel, a pipelined variant that further accelerates mixed-trust execution. We implement both protocols atop Intel SGX and evaluate them in LAN and WAN environments. Our results show that Raftel achieves up to 625 TPS with sub-670 ms latency in WAN settings, outperforming HotStuff by up to 308 TPS in throughput while approaching the performance of fully TEE-assisted protocols.

  匹配依据：TEE: intel sgx

  </details>

- **Bootstrapping Mutual Attestation with Kleene's Second Recursion Theorem**
  2026-08-21 · TEE · [arXiv](https://arxiv.org/abs/2608.20671)
  Takuma Imamura

  <details><summary>摘要 / Abstract</summary>

  Remote attestation is a procedure by which a system (such as a Trusted Execution Environment) proves its own configuration to a remote peer. Here, the configuration includes the measurements (hash digests) of software components. When multiple nodes perform mutual attestation, each node must maintain the reference values for its peers&#x27; measurements. We refer to this as the reference-value bootstrapping problem for mutual attestation. In this paper, we formulate the problem as a fixed-point equation and solve it directly using Kleene&#x27;s second recursion theorem. In our approach, nodes can reconstruct one another&#x27;s source code, thereby allowing each node to derive the reference values at runtime. When a source code itself is deployed, as with a Python script, a node derives the peer&#x27;s reference value directly from its reconstructed source. When a build artifact is deployed, as with AWS Nitro Enclaves, a node instead reproducibly builds the peer&#x27;s artifact from its reconstructed source and derives the reference value from it. As a proof of concept, we develop transpilers in Python and Nix to generate mutually referencing programs. Using these transpilers, we demonstrate the mutual derivation of reference values for the two deployment models mentioned above. Our solution is architecture-independent, requires no trusted third party, and works with existing attestation stacks without modification.

  匹配依据：TEE: trusted execution environment

  </details>

- **WaveCommitments: Private and Verifiable Speech-Agent Marketplaces**
  2026-07-16 · TEE · [arXiv](https://arxiv.org/abs/2610.26867)
  Oguzhan Baser, Kaan Kale, Sriram Vishwanath, Sandeep Chinchali

  <details><summary>摘要 / Abstract</summary>

  Modern speech systems are evolving into ecosystems of autonomous speech agents that interact, negotiate, and trade assets such as embeddings, spectrograms, or raw data. In such markets, sellers cannot reveal assets for evaluation due to privacy constraints, and buyers cannot price what they cannot test. Thus, we introduce WaveCommitments, an end-to-end design that couples multivariate polynomial commitments with confidential asset valuation via Data Shapley inside a trusted execution environment. It enables selective openings and tamper-evident provenance to prove that a delivered asset matches the valuation while hiding everything else. Our extensive experiments across three standard datasets and various tasks with state-of-the-art encoders, including Whisper, reveal that we speed up the strongest baselines by up to 18.1x while reducing their proof sizes by up to 43.2x. We also analyze how a speaker&#x27;s value shifts across tasks and encoders, revealing agent-level market prices.

  匹配依据：TEE: trusted execution environment

  </details>

- **Evidence-Bound Gateway-Path Provenance for Third-Party LLM Inference**
  2026-06-21 · TEE · [arXiv](https://arxiv.org/abs/2606.22560)
  Fei Wang, Zebai Tian

  <details><summary>摘要 / Abstract</summary>

  Third-party LLM gateways select providers, models, endpoints, and fallback paths while also authoring the records used to explain and bill those decisions. We present evidence-bound gateway-path provenance, which makes these decisions subject to client-verifiable request contracts. An attested mediation runtime intersects a signed service policy with the client&#x27;s authorization, constructs provider-facing calls, and protects streamed responses. The contract distinguishes initial routes from fallback destinations and admits each transition only after an authorized failure. A signed close-out binds the execution trace, provider-reported usage, authorized pricing, and complete response. We formalize the protocol state machine and establish authorization preservation, execution and stream binding, charge integrity, and channel confidentiality relative to the public receipt metadata. The analysis also characterizes replay, runtime replacement, and the information disclosed by public payload commitments. Controlled software-path measurements show 0.442 ms paired p95 latency overhead at concurrency one, peak throughput of 10.65 thousand requests/s, and stream close-out below 0.4 ms p95. An AWS Nitro Enclaves prototype completed 30 live single-route streaming requests with attestation-bound session and signing keys. The design separates gateway administration from payload processing and supplies a verifiable account of each confirmed execution.

  匹配依据：TEE: enclaves (context)

  </details>

- **OTRO: Oblivious Tokenization Path with Square-Root ORAM**
  2026-06-15 · TEE · [arXiv](https://arxiv.org/abs/2606.17358)
  Jonghyun Lee, Yongqin Wang, Rachit Rajat, Daniel Wong, Mengyuan Li, Murali Annavaram

  <details><summary>摘要 / Abstract</summary>

  The CPU-side large language model (LLM) tokenizer is a critical security gap in LLM serving through a confidential computing stack with CPU and GPU trusted execution environments (TEEs). Tokenizers converts the prompts through table-driven lookups, and the resulting memory access patterns are a powerful source of side-channel leakage. Recent work demonstrates end-to-end recovery of user prompts from tokenizer access pattern on production Intel TDX. However, a drop-in use of the popular tree-based Oblivious RAMs (e.g., PathORAM) to prevent access-pattern leakage introduces $\sim$13$\times$ tokenizer slowdown, resulting in 10-58% higher time-to-first-token (TTFT). In this paper, we present OTRO, an efficient, oblivious tokenization path tailored to latency-critical LLM serving. OTRO relies on square-root ORAM for fast single-access lookups, but avoids its prohibitive $O(N\log^2N$) rebuild cost every $\sqrt{N}$ accesses through three key innovations. First, OTRO provides a pool of replicated square-root ORAM instances that utilize the read-only nature of tokenizer table. Second, an epoch-based rotation policy decouples accesses from rebuilds and pads each epoch with dummy accesses to its boundaries, minimizing observable information. Lastly, chunked KV-cache-aware tokenization further overlaps rebuilds with GPU prefill and minimizes the instance count. Implemented as modules in HuggingFace Tokenizers and nano-vLLM, running within a TDX-enabled CVM with an NVIDIA H100 GPU, OTRO limits TTFT overhead to at most 4.5%, keeps tokenizer-induced latency under 10\% of total TTFT, and adds less than 0.5 GB of memory overhead while reducing the tokenizer&#x27;s observable leakage across various model families and sizes.

  匹配依据：TEE: confidential computing, intel tdx, trusted execution environments

  </details>

- **TENNOR: Trustworthy Execution for Neural Networks through Obliviousness and Retrievals**
  2026-05-08 · TEE · [arXiv](https://arxiv.org/abs/2605.07160)
  Zifan Qu, Vasileios P. Kemerlis, Giuseppe Ateniese, Evgenios M. Kornaropoulos

  <details><summary>摘要 / Abstract</summary>

  Training neural networks on sensitive data in untrusted cloud environments requires simultaneously achieving computational efficiency and rigorous privacy guarantees. Sparsification techniques, essential for scalable training of wide layers, expose input-dependent memory-access patterns that are visible and can be exploited by a host OS/hypervisor, even when computation is protected by a Trusted Execution Environment. We present TENNOR, a system that resolves this tension by co-designing the neural network training pipeline with doubly oblivious primitives, eliminating value-dependent neural network access-pattern leakage while also utilizing adaptive sparsification. TENNOR recasts sparse neuron activation as a locality-sensitive hashing (LSH) retrieval problem, reducing secure sparsification to doubly oblivious accesses over an LSH data structure. To eliminate the prohibitive storage cost of &quot;multi-table&quot; LSH, we introduce Multi-Probe Winner-Take-All (MP-WTA): the first multi-probe scheme for rank-based LSH, achieving a $50\times$ reduction in (hash table) memory while preserving model accuracy. We evaluate TENNOR on multi-label classification benchmarks, with output layers of up to hundreds of thousands of neurons under different batch sizes inside an Intel TDX Trusted Domain, achieving per-batch training speedups of $13\times$-$470\times$ over a Path ORAM baseline and reducing a 208-hour run to about 26 minutes.

  匹配依据：TEE: intel tdx, trusted execution environment

  </details>

- **Sharing is caring: Attestable and Trusted Workflows out of Distrustful Components**
  2026-03-03 · TEE · [arXiv](https://arxiv.org/abs/2603.03403)
  Amir Al Sadi, Sina Abdollahi, Adrien Ghosn, Hamed Haddadi, Marios Kogias

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) protect private memory and attest initial code and configuration, but neither constrain nor attest shared channels between TEEs or with the untrusted host. Confidentiality thus depends on the functional correctness of all in-TEE code accessing these channels: a single misuse can leak data and compromise a pipeline. This assumption is increasingly untenable for agentic applications that generate code at runtime and cloud pipelines of mutually distrustful components. We present MICA, a confidential-computing firmware extension that decouples confidentiality from trust in in-TEE code. MICA lets tenants define, restrict, and attest channel constraints between TEEs and with the untrusted host, including transitive constraints spanning a pipeline. It extends attestation to groups of communicating TEEs, letting external parties verify the confidentiality properties induced by these constraints across a pipeline. We implement MICA on Arm CCA by extending the Realm Management Monitor with a small policy language, requiring no hardware changes and minor QEMU and KVM changes. Our evaluation demonstrates support for confidential agentic applications and pipeline computations without trusting the functional correctness of in-TEE code. MICA increases the TCB by 7% and incurs infrequent setup costs: 2-4% boot-time overhead, approximately 1.5 s for policy upload, and 246-598 ms for group attestation. Once established, Realm communication is direct, uses protected memory, and requires no MICA intervention or software encryption, yielding up to 14.5 times lower cross-TEE message latency than encrypted communication over untrusted memory.

  匹配依据：TEE: arm cca, confidential computing, trusted execution environments

  </details>

- **kvTZ: TrustZone Virtualization for Commodity Arm-Based Platforms.**
  2026 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2025.3605807)
  Shih-Wei Li, Chun-Yen Lin

- **WorksetEnclave: Towards Optimizing Cold Starts in Confidential Serverless with Workset-Based Enclave Restore.**
  2026 · TEE · [ASPLOS](https://doi.org/10.1145/3779212.3790249)
  Xiaolong Yan, Weijuan Zhang, Qihang Zhou, Xiaoqi Jia, Feifan Qian, Zisen Wan, Wentao Yao

- **UIEE: Secure and Efficient User-space Isolated Execution Environment for Embedded TEE Systems.**
  2026 · TEE · [NDSS](https://www.ndss-symposium.org/ndss-paper/uiee-secure-and-efficient-user-space-isolated-execution-environment-for-embedded-tee-systems/)
  Xinhui Shao, Haobo Li, Huaiyu Yan, Yier Jin, Ping Jiang, Xuandong Chen, Ming Yang, Junzhou Luo, Zhen Ling

- **TrustSearch: Toward Secure and Efficient Reverse Image Search via SGX.**
  2026 · TEE · [TIFS](https://doi.org/10.1109/TIFS.2026.3696201)
  Dayan Wu, Xiong Li, Hongwei Li, Jingwei Li, Xiaosong Zhang, Fang Zou, Ting Chen, Jia Zhang

- **Trust-V: Toward Secure and Reliable Storage for Trusted Execution Environments.**
  2026 · TEE · [ASPLOS](https://doi.org/10.1145/3779212.3790242)
  Seung-Kyun Han, Jin Soo Jang, Jiyeon Yang

- **Toward Secure and Efficient Driver Support for Embedded TEE Systems.**
  2026 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2026.3693739)
  Zhen Ling, Huaiyu Yan, Ming Yang, Xinhui Shao, Junzhou Luo, Ping Jiang, Xinwen Fu

- **Teamwork Makes TEE Work: Open and Resilient Remote Attestation on Decentralized Trust.**
  2026 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2025.3636884)
  Dawu Gu, Chi Zhang, Shipei Qu, Xiaolin Zhang, Kailun Qin, Tengfei Wang

- **TZ-LLM: Protecting On-Device Large Language Models with Arm TrustZone.**
  2026 · TEE · [EuroSys](https://doi.org/10.1145/3767295.3769334)
  Jiacheng Shi, Zhichao Hua, Jinyu Gu, Zihan Zhao, Yang Yu, Xunjie Wang

- **TEEM³: Core-Independent and Cooperating Trusted Execution Environments.**
  2026 · TEE · [ASPLOS](https://doi.org/10.1145/3779212.3790232)
  Nils Asmussen, Friedrich Pauls, Carsten Weinhold, Sebastian Haas, Michael Roitzsch, Nilanjana Das, Nicholas Gordon, Stephan Gerhold

- **TEE.Fail: Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition.**
  2026 · TEE · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00101)
  Christina Garman, Stephan van Schaik, Alexander Seto, Jalen Chuang, Daniel Genkin, Nicolás Berrios

- **TDXRay: Microarchitectural Side-Channel Analysis of Intel TDX for Real-World Workloads.**
  2026 · TEE · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00170)
  Lukas Gerlach, Ruiyi Zhang, Phillipp Schoppmann, Michael Schwarz, Albert Cheu, Hosein Yavarzadeh, Daniel Moghimi, Adrià Gascón, Tristan Hornetz

- **SXGB: Secure and Efficient Vertical Federated XGBoost via Trusted Execution Environments.**
  2026 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2025.3626379)
  Hui Zhu, Rongxing Lu, Hui Li, Jiaqi Zhao, Fengwei Wang

- **SEED: A Minimal‑Footprint TEE Framework for Verifiable, Confidential Microservice Deployment.**
  2026 · TEE · [PoPETs](https://doi.org/10.56553/POPETS-2026-0021)
  Md. Redowan Mahmud, Omar Jarkas, Ryan Kok Leong Ko, Naipeng Dong

- **PowerHooK: Enabling Software-Based Power Side Channels Against AMD SEV Technologies via Transient-Execution Replay.**
  2026 · TEE · [conf/woot](https://www.usenix.org/conference/woot26/presentation/oberhuber)
  Martin Unterguggenberger, Rishub Nagpal, Andreas Kogler, Mathias Oberhuber, Stefan Mangard, Martin Wistauder

- **Palladium: Guarding Neural Network Training With Confidential Computing.**
  2026 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2026.3694706)
  Juan Wang, Wenzhe Yi, Xiaoyang Xu, Hongxin Hu, Ziang Li, Mengda Yang

- **LÆGIS: Pinpointing and Addressing Performance Overheads of GPU-Based Confidential Computing.**
  2026 · TEE · [ISCA](https://doi.org/10.1109/ISCA66397.2026.00046)
  Adwait Jog, Yang Yang

- **It's TEEtime: Secure Interrupt Isolation for Normal-world Enclaves on Arm.**
  2026 · TEE · [TCHES](https://doi.org/10.46586/TCHES.V2026.I1.135-160)
  Ivan Puddu, Shweta Shinde, Moritz Schneider, Friederike Groschupp, Mark Kuhne, Srdjan Capkun

- **Enabling Confidential VMs Across Diverse ARM Platforms by Retrofitting TrustZone.**
  2026 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2026.3657770)
  Zeyu Mi, Haibo Chen, Yicong Wang

- **EXIA: Trusted Transitions for Enclaves via External-Input Attestation.**
  2026 · TEE · [NDSS](https://www.ndss-symposium.org/ndss-paper/exia-trusted-transitions-for-enclaves-via-external-input-attestation/)
  Guoxing Chen, Sanchuan Chen, Yidi Kao, Haojin Zhu, Zhen Huang, Yan Meng

- **DisT-FL: Enhancing Security for TEE-Based Aggregation in Federated Learning.**
  2026 · TEE · [TIFS](https://doi.org/10.1109/TIFS.2026.3715108)
  Guoxing Chen, Jianzong Wang, Jianyu Niu, Zhen Huang, Guanlong Wu, Ju Yang, Yinqian Zhang

- **DisARMed: Attacking ARM TrustZone from Userspace with Memory Aliasing.**
  2026 · TEE · [conf/woot](https://www.usenix.org/conference/woot26/presentation/henes)
  Mihai Ordean, Jacqueline Henes, David Oswald, Matthew Bowden

- **Detecting Inconsistencies in Arm CCA's Formally Verified Specification.**
  2026 · TEE · [ASPLOS](https://doi.org/10.1145/3779212.3790152)
  Xiang Cheng, Taesoo Kim, Changho Choi, Bokdeuk Jeong

- **DNN Latency Sequencing: Extracting DNN Architectures from Intel SGX Enclaves with Single-Stepping Attacks.**
  2026 · TEE · [NDSS](https://www.ndss-symposium.org/ndss-paper/dnn-latency-sequencing-extracting-dnn-architectures-from-intel-sgx-enclaves-with-single-stepping-attacks/)
  Chung Hwan Kim, Z. Berkay Celik, Minkyung Park, Zelun Kong, DaveTian

- **Complementing Confidential Computing Environment for Applications on Arm CCA.**
  2026 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2025.3604008)
  Xiapu Luo, Zhenyu Ning, Fengwei Zhang, Shoumeng Yan, Haoyang Huang, Yuxin Hu, Zhengyu He, Yiming Zhang

- **CROSS-TEE: A Distributed Trusted Execution Environment Architecture for Cross-Module Automotive Security.**
  2026 · TEE · [TIFS](https://doi.org/10.1109/TIFS.2026.3714115)
  Kui Ren, Shoumeng Yan, Kun Yang, Sisi Li, Hongliang Tian

- **Building Confidential Accelerator Computing Environment for Arm CCA.**
  2026 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2025.3615787)
  Tao Wei, Jiannong Cao, Zhengyu He, Fengwei Zhang, Chenxu Wang, Kevin Leach, Shoumeng Yan, Kun Lu, Zhenyu Ning, Yunjie Deng

- **BreakFAST: Confused Deputy Attack on Infinity Fabric to Break AMD SEV-SNP.**
  2026 · TEE · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00259)
  Shweta Shinde, Benedict Schlüter, Philipp Giersfeld

- **Battering RAM: Low-Cost Interposer Attacks on Confidential Computing via Dynamic Memory Aliasing.**
  2026 · TEE · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00052)
  Jo Van Bulck, David F. Oswald, Jesse De Meulemeester, Ingrid Verbauwhede

- **Anonymous Integrity Auditing Scheme Based on Trusted Execution Environment for Distributed Edge Computing.**
  2026 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2026.3670134)
  Jie Cui, Junjie Liu, Qingyang Zhang, Fengqun Wang, Jiaxin Li, Hong Zhong

- **AEX-NStep: Probabilistic Interrupt Counting Attacks on Intel SGX.**
  2026 · TEE · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00035)
  Ivan Puddu, Nicolas Dutly, Friederike Groschupp, Kari Kostiainen, Srdjan Capkun

### 2025

- **Decentralized Proposer-as-a-Service (DPaaS): Improving Decentralization and Trustworthiness in Ethereum PBS**
  2025-11-20 · TEE · [IACR ePrint](https://eprint.iacr.org/2025/2126)
  Chenyang Liu, Arnav Jindal, Ittai Abraham, Matthew Lentz, Kartik Nayak

  <details><summary>摘要 / Abstract</summary>

  Proposer-Builder Separation (PBS) in Ethereum aims to improve decentralization and scalability by offloading block construction to specialized builders, but its current MEV-Boost implementation relies on trusted relays, introducing centralization as well as security and performance concerns. We propose Decentralized Proposer-as-a-Service (DPaaS) to eliminate relays while preserving compatibility with Ethereum’s consensus layer by distributing the combined proposer and relay roles across Proposer Entities (PEs) running in independent Trusted Execution Environments (TEEs). DPaaS presents itself to Ethereum as a single validator using threshold BLS signatures, while a new Byzantine broadcast protocol decentralizes the auctioneer role with censorship-resistance and availability-backed guarantees. Our evaluation, deployed across four independent cloud hosts and driven by real-world traces, shows that DPaaS achieves $\leq 6$ ms bid processing latency, $68.7$ ms latency from the end of auction to block proposal, and $3.3\%$ more MEV earnings – demonstrating that DPaaS can offer security, decentralization, and trustworthiness benefits while providing strong performance.

  匹配依据：TEE: trusted execution environments

  </details>

- **SoK: Cryptocurrency Mixing and Anonymity - Architectures, Threat Models, Operational Aspects and Security**
  2025-04-28 · TEE · [arXiv](https://arxiv.org/abs/2504.20296)
  Juraj Mariani, Martin Perešíni, Ivan Homoliak

  <details><summary>摘要 / Abstract</summary>

  Public blockchains record transaction histories that enable address clustering, taint analysis, and cross-service attribution, thereby motivating the development of mixers and privacy layers. Our work presents a structured scoping review of 22 representative systems, defining a common unlinkability objective and five adversary archetypes. We evaluate these systems against a taxonomy of attack surfaces, including chain analysis, timing inference, custodial compromise, coordination abuse, network metadata, and trusted execution compromise. While nominal anonymity-set size and cryptographic strength characterize privacy in theory, effective anonymity in practice depends on transaction denominations, cover traffic, relayer behavior, and compliance-interface design. Distinguishing nominal from effective anonymity, we derive four core lessons: (1) Privacy is strongest when integrated into everyday transactions, since standalone mixing creates an easily profiled user subset; (2) Trust points, including operators, peer quorums, and hardware enclaves, must be explicit so users know who can break privacy; (3) Network metadata, including gas funding and timing, must be treated formally as protocol data in privacy evaluations; and (4) Compliance should use auditable cryptographic predicates for selective disclosure rather than broad operator discretion. Ultimately, our systematization clarifies the strengths, failures, and future requirements of blockchain privacy architectures.

  匹配依据：TEE: hardware enclaves

  </details>

- **ZIPNet: Low-bandwidth anonymous broadcast from (dis)Trusted Execution Environments.**
  2025 · TEE · [PoPETs](https://doi.org/10.56553/POPETS-2025-0058)
  Rui Wang, Ian Miers, Michael Rosenberg, Maurice Shih, Zhenyu Zhao, Fan Zhang

- **WireTap: Breaking Server SGX via DRAM Bus Interposition.**
  2025 · TEE · [ACM CCS](https://doi.org/10.1145/3719027.3765204)
  Christina Garman, Stephan van Schaik, Jalen Chuang, Alexander Seto, Samy Amer, Daniel Genkin, Oytun Kuday Duran

- **Transparent Attested DNS for Confidential Computing Services.**
  2025 · TEE · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/delignat-lavaud)
  Antoine Delignat-Lavaud, Sylvan Clebsch, Christoph M. Wintersteiger, Manuel Costa, Kapil Vaswani, Cédric Fournet

- **The Road to Trust: Building Enclaves within Confidential VMs.**
  2025 · TEE · [NDSS](https://www.ndss-symposium.org/ndss-paper/the-road-to-trust-building-enclaves-within-confidential-vms/)
  Shijun Zhao, XiaoFeng Wang, Shoumeng Yan, Dan Meng, Linke Song, Benshan Mei, Shuang Liu, Wenhao Wang, Rui Hou

- **Tacco: A Framework for Ensuring the Security of Real-World TEEs via Formal Verification.**
  2025 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2025.3594594)
  Kui Ren, Jilin Hu, Yongwang Zhao, Shuangquan Pan, Zuohua Ding

- **TLBlur: Compiler-Assisted Automated Hardening against Controlled Channels on Off-the-Shelf Intel SGX Platforms.**
  2025 · TEE · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/vanoverloop)
  Jo Van Bulck, Mathias Payer, Andrés Sánchez, Frank Piessens, Flavio Toffalini, Daan Vanoverloop

- **TEEMS: A Trusted Execution Environment based Metadata-protected Messaging System.**
  2025 · TEE · [PoPETs](https://doi.org/10.56553/POPETS-2025-0119)
  Ian Goldberg, Sajin Sasy, Aaron Johnson

- **TDXploit: Novel Techniques for Single-Stepping and Cache Attacks on Intel TDX.**
  2025 · TEE · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/rauscher)
  Daniel Gruss, Luca Wilke, Fabian Rauscher, Hannes Weissteiner, Thomas Eisenbarth

- **SCRUTINIZER: Towards Secure Forensics on Compromised TrustZone.**
  2025 · TEE · [NDSS](https://www.ndss-symposium.org/ndss-paper/scrutinizer-towards-secure-forensics-on-compromised-trustzone/)
  Shoumeng Yan, Fengwei Zhang, Xiapu Luo, Zhenkai Liang, Xuhua Ding, Tao Wei, Zhengyu He, Rui Hou, Yiming Zhang

- **Revisiting SGX-Based Encrypted Deduplication via PoW-Before-Encryption and Eliminating Redundant Computations.**
  2025 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2024.3476288)
  Xiaowei Ge, Guanxiong Ha, Zhen Su, Chunfu Jia, Yuchen Chen

- **Reload+Reload: Exploiting Cache and Memory Contention Side Channel on AMD SEV.**
  2025 · TEE · [ASPLOS](https://doi.org/10.1145/3676641.3716017)
  Shih-Wei Li, Li-Chung Chiang

- **Rakis: Secure Fast I/O Primitives Across Trust Boundaries on Intel SGX.**
  2025 · TEE · [EuroSys](https://doi.org/10.1145/3689031.3696090)
  Dmitrii Kuvaiskii, Fan Sang, Taesoo Kim, Mansour Alharthi, Mona Vij

- **RMPocalypse: How a Catch-22 Breaks AMD SEV-SNP.**
  2025 · TEE · [ACM CCS](https://doi.org/10.1145/3719027.3765233)
  Shweta Shinde, Benedict Schlüter

- **RContainer: A Secure Container Architecture through Extending ARM CCA Hardware Primitives.**
  2025 · TEE · [NDSS](https://www.ndss-symposium.org/ndss-paper/rcontainer-a-secure-container-architecture-through-extending-arm-cca-hardware-primitives/)
  Jiayun Chen, Zhenyu Song, Shaowen Xu, Qihang Zhou, Peng Liu, Wenzhuo Cao, Xiaoqi Jia, Shengzhi Zhang

- **Portal: Fast and Secure Device Access with Arm CCA for Modern Arm Mobile System-on-Chips (SoCs).**
  2025 · TEE · [IEEE S&amp;P](https://doi.org/10.1109/SP61157.2025.00013)
  Jaehyuk Lee, Xiaokuan Zhang, Fan Sang, Taesoo Kim

- **OPSA: Efficient and Verifiable One-Pass Secure Aggregation With TEE for Federated Learning.**
  2025 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2025.3565640)
  Jinsong Han, Zhiguo Wan, Zhangshuang Guan, Yulin Zhao

- **OBIR-tree: An Efficient Oblivious Index for Spatial Keyword Queries on Secure Enclaves.**
  2025 · TEE · [PACMMOD / SIGMOD](https://doi.org/10.1145/3709708)
  Xiangyu Wang, Jianfeng Ma, Zesen Liu, Zikai Ye, Dan Zhu

- **MuEOC: Efficient SGX-Based Multi-Key Homomorphic Outsourcing Computation for E-Health System.**
  2025 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2024.3476483)
  Zhenfu Cao, Jun Zhou, Yisong Wang, Kim-Kwang Raymond Choo, Xiaolei Dong

- **More Granular, Less Trust: Enforcing Intra-Process Isolation With Arm CCA in an Untrusted Management Environment.**
  2025 · TEE · [TIFS](https://doi.org/10.1109/TIFS.2025.3634981)
  Kun Sun, Zhouqi Jiang, Zhaohui Chen, Jie Wang, Wei Zhou, Shiqi Liu, Yulai Xie

- **Microft: Exploring and Mitigating Cross-State Control-Flow Hijacking Attacks on ARM Cortex-M TrustZone.**
  2025 · TEE · [TIFS](https://doi.org/10.1109/TIFS.2025.3625394)
  Zheyuan Ma, Lukasz Ziarek, Xi Tan, Ziming Zhao, Shambhu J. Upadhyaya, Hongxin Hu, Ning Zhang

- **MaTEE: Efficiently Bridging the Semantic Gap in TrustZone via Arm Pointer Authentication.**
  2025 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2024.3445296)
  Yongpeng Gao, Xiang Li, Jie Wang, Jiajin Hu, Shiqi Liu

- **MDPeek: Breaking Balanced Branches in SGX with Memory Disambiguation Unit Side Channels.**
  2025 · TEE · [ASPLOS](https://doi.org/10.1145/3676641.3716004)
  Wenjian He, Dongsheng Wang, Trevor E. Carlson, Chang Liu, Shuaihu Feng, Yuan Li, Yongqiang Lyu

- **LoRO: Real-Time on-Device Secure Inference for LLMs via TEE-Based Low Rank Obfuscation.**
  2025 · TEE · [NeurIPS](http://papers.nips.cc/paper_files/paper/2025/hash/1b86cf4b15cd83b6520d851eb7298228-Abstract-Conference.html)
  Jianhua Liu, Gaojian Xiong, Jianwei Liu, Yu Sun, Jian Cui

- **LETIndex: A Secure Learned Index with TEE.**
  2025 · TEE · [VLDB](https://doi.org/10.14778/3750601.3750682)
  Shuting Cao, Zeping Niu, Guoliang Li

- **Heracles: Chosen Plaintext Attack on AMD SEV-SNP.**
  2025 · TEE · [ACM CCS](https://doi.org/10.1145/3719027.3765209)
  Shweta Shinde, Benedict Schlüter, Christoph Wech

- **Game of Arrows: On the (In-)Security of Weight Obfuscation for On-Device TEE-Shielded LLM Partition Algorithms.**
  2025 · TEE · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-pengli)
  Zheng Zhang, Yifeng Cai, Bingyou Dong, Huanran Xue, Pengli Wang, Junlin Liu, Yao Zhang, Ye Wu, Ziqi Zhang

- **GPU Travelling: Efficient Confidential Collaborative Training with TEE-Enabled GPUs.**
  2025 · TEE · [ACM CCS](https://doi.org/10.1145/3719027.3765029)
  Enriquillo Valdez, Shixuan Zhao, Hani Jamjoom, Salman Ahmed, Zhongshu Gu, Zhiqiang Lin

- **Formal Security Analysis of the AMD SEV-SNP Software Interface.**
  2025 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2025.3528737)
  Petar Paradzik, Marko Horvat, Ante Derek

- **Dorami: Privilege Separating Security Monitor on RISC-V TEEs.**
  2025 · TEE · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/kuhne)
  Shweta Shinde, Mark Kuhne, Stavros Volos

- **CounterSEVeillance: Performance-Counter Attacks on AMD SEV-SNP.**
  2025 · TEE · [NDSS](https://www.ndss-symposium.org/ndss-paper/counterseveillance-performance-counter-attacks-on-amd-sev-snp/)
  Daniel Gruss, Stefan Gast, Robin Leander Schröder, Hannes Weissteiner

- **BiTDB: Constructing A Built-in TEE Secure Database for Embedded Systems (Extended Abstract).**
  2025 · TEE · [ICDE](https://doi.org/10.1109/ICDE65448.2025.00393)
  Jianfeng Ma, Chengyan Ma, Di Lu, Ning Xi, Chaoyue Lv, Xiaohong Jiang, Yulong Shen

- **BadRAM: Practical Memory Aliasing Attacks on Trusted Execution Environments.**
  2025 · TEE · [IEEE S&amp;P](https://doi.org/10.1109/SP61157.2025.00104)
  David F. Oswald, Jo Van Bulck, Jesse De Meulemeester, Luca Wilke, Thomas Eisenbarth, Ingrid Verbauwhede

- **Attestable Builds: Compiling Verifiable Binaries on Untrusted Systems using Trusted Execution Environments.**
  2025 · TEE · [ACM CCS](https://doi.org/10.1145/3719027.3765128)
  Alastair R. Beresford, Daniel Hugenroth, Mario Lins, René Mayrhofer

- **AegisGuard: RL-Guided Adapter Tuning for TEE-Based Efficient &amp; Secure On-Device Inference.**
  2025 · TEE · [NeurIPS](http://papers.nips.cc/paper_files/paper/2025/hash/f308b5f207348484552997c536375654-Abstract-Conference.html)
  Che Wang, Yinggui Wang, Yurong Hao, Tiantong Wang, Wei Yang Bryan Lim, Yang Cao, Zhong Chen, Ziqi Zhang, Jianbo Gao, Tao Wei

- **ASGARD: Protecting On-Device Deep Neural Networks with Virtualization-Based Trusted Execution Environments.**
  2025 · TEE · [NDSS](https://www.ndss-symposium.org/ndss-paper/asgard-protecting-on-device-deep-neural-networks-with-virtualization-based-trusted-execution-environments/)
  Dokyung Song, Minhee Kim, Joonkyo Jung, Myungsuk Moon

- **A System Framework to Symbolically Explore Intel TDX Module Execution.**
  2025 · TEE · [ACM CCS](https://doi.org/10.1145/3719027.3765212)
  Pansilu Pitigalaarachchi, Xuhua Ding

### 2024

- **sNPU: Trusted Execution Environments on Integrated NPUs.**
  2024 · TEE · [ISCA](https://doi.org/10.1109/ISCA59077.2024.00057)
  Yubin Xia, Erhu Feng, Haibo Chen, Dahu Feng, Dong Du

- **WeSee: Using Malicious \#VC Interrupts to Break AMD SEV-SNP.**
  2024 · TEE · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00262)
  Shweta Shinde, Benedict Schlüter, Supraja Sridhara, Andrin Bertschi

- **Trusted Execution Environments for Quantum Computers.**
  2024 · TEE · [ACM CCS](https://doi.org/10.1145/3658644.3690855)
  Theodoros Trochatos

- **TensorTEE: Unifying Heterogeneous TEE Granularity for Efficient Secure Collaborative Tensor Computing.**
  2024 · TEE · [ASPLOS](https://doi.org/10.1145/3622781.3674168)
  Yifan Hao, Xiaqing Li, Yuanbo Wen, Erhu Feng, Jianan Mu, Pengwei Jin, Tianyun Ma, Xinkai Song, Husheng Han, Zidong Du, Ling Liang, Xinyao Zheng, Qi Guo, Xing Hu

- **TDXdown: Single-Stepping and Instruction Counting Attacks against Intel TDX.**
  2024 · TEE · [ACM CCS](https://doi.org/10.1145/3658644.3690230)
  Luca Wilke, Florian Sieck, Thomas Eisenbarth

- **Specification and Verification of Strong Timing Isolation of Hardware Enclaves.**
  2024 · TEE · [ACM CCS](https://doi.org/10.1145/3658644.3690203)
  Clément Pit-Claudel, Thomas Bourgeat, Stella Lau, Adam Chlipala

- **SoK: SGX.Fail: How Stuff Gets eXposed.**
  2024 · TEE · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00260)
  Christina Garman, Stephan van Schaik, Eyal Ronen, Alexander Seto, Thomas Yurek, Bader AlBassam, Daniel Genkin, Yuval Yarom, Andrew Miller, Adam Batori

- **Secure Similarity Queries Over Vertically Distributed Data via TEE-Enhanced Cloud Computing.**
  2024 · TEE · [TIFS](https://doi.org/10.1109/TIFS.2024.3413630)
  Hui Zhu, Jun Shao, Yunguo Guan, Rongxing Lu, Fengwei Wang, Songnian Zhang, Hui Li, Yandong Zheng

- **Salus: A Practical Trusted Execution Environment for CPU-FPGA Heterogeneous Cloud Platforms.**
  2024 · TEE · [ASPLOS](https://doi.org/10.1145/3622781.3674169)
  Zhen Gu, Yiran Li, Le Su, Yijin Guan, Yanheng Lu, Dimin Niu, Sheng Wang, Yu Zou, Mingyu Gao, Feifei Li, Yuan Xie

- **SGXFault: An Efficient Page Fault Handling Mechanism for SGX Enclaves.**
  2024 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2023.3268169)
  Omais Shafi Pandith

- **SEV-Step A Single-Stepping Framework for AMD-SEV.**
  2024 · TEE · [TCHES](https://doi.org/10.46586/TCHES.V2024.I1.180-206)
  Anja Rabich, Luca Wilke, Jan Wichelmann, Thomas Eisenbarth

- **Pandora: Principled Symbolic Validation of Intel SGX Enclave Runtimes.**
  2024 · TEE · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00090)
  David F. Oswald, Jo Van Bulck, Lesly-Ann Daniel, Fritz Alder, Frank Piessens

- **On (the Lack of) Code Confidentiality in Trusted Execution Environments.**
  2024 · TEE · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00259)
  Daniele Lain, Ivan Puddu, Moritz Schneider, Stefano Boschetto, Srdjan Capkun

- **No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML.**
  2024 · TEE · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00052)
  Yao Guo, Bingyan Liu, Yifeng Cai, Chen Gong, Yuanyuan Yuan, Xiangqun Chen, Ding Li, Ziqi Zhang

- **LDR: Secure and Efficient Linux Driver Runtime for Embedded TEE Systems.**
  2024 · TEE · [NDSS](https://www.ndss-symposium.org/ndss-paper/ldr-secure-and-efficient-linux-driver-runtime-for-embedded-tee-systems/)
  Haobo Li, Lan Luo, Xinhui Shao, Huaiyu Yan, Ping Jiang, Ming Yang, Kai Dong, Xinwen Fu, Junzhou Luo, Zhen Ling

- **HyperTEE: A Decoupled TEE Architecture with Secure Enclave Management.**
  2024 · TEE · [MICRO](https://doi.org/10.1109/MICRO61859.2024.00018)
  Shijun Zhao, Dan Meng, Fengwei Zhang, Peinan Li, Yubiao Huang, Lutan Zhao, Yunkai Bai, Rui Hou, Michael C. Huang

- **GroupCover: A Secure, Efficient and Scalable Inference Framework for On-device Model Protection based on TEEs.**
  2024 · TEE · [series/jmlr](https://proceedings.mlr.press/v235/zhang24bn.html)
  Tianyi Zhang, Zheng Zhang, Jianwei Liu, Yao Zhang, Ye Wu, Na Wang, Ziqi Zhang

- **Gramine-TDX: A Lightweight OS Kernel for Confidential VMs.**
  2024 · TEE · [ACM CCS](https://doi.org/10.1145/3658644.3690323)
  Dmitrii Kuvaiskii, Dimitrios Stavrakakis, Cedric Xing, Kailun Qin, Pramod Bhatotia, Mona Vij

- **GlobalConfusion: TrustZone Trusted Application 0-Days by Design.**
  2024 · TEE · [USENIX Security](https://www.usenix.org/conference/usenixsecurity24/presentation/busch-globalconfusion)
  Marcel Busch, Philipp Mao, Mathias Payer

- **Faults in Our Bus: Novel Bus Fault Attack to Break ARM TrustZone.**
  2024 · TEE · [NDSS](https://www.ndss-symposium.org/ndss-paper/faults-in-our-bus-novel-bus-fault-attack-to-break-arm-trustzone/)
  Nimish Mishra, Debdeep Mukhopadhyay, Anirban Chakraborty

- **Ensuring State Continuity for Confidential Computing: A Blockchain-Based Approach.**
  2024 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2024.3381973)
  Yinqian Zhang, Jianyu Niu, Xiang Li, Wei Peng, Xiaokuan Zhang

- **EnclaveFuzz: Finding Vulnerabilities in SGX Applications.**
  2024 · TEE · [NDSS](https://www.ndss-symposium.org/ndss-paper/enclavefuzz-finding-vulnerabilities-in-sgx-applications/)
  Liheng Chen, Baojian Chen, Zheyu Ma, Chao Zhang, Yuan Li, Zheming Li

- **DeCloak: Enable Secure and Cheap Multi-Party Transactions on Legacy Blockchains by a Minimally Trusted TEE Network.**
  2024 · TEE · [TIFS](https://doi.org/10.1109/TIFS.2023.3318935)
  Yuchen Wu, Lei Wang, Hong Lei, Bangdao Chen, Yue Li, Qian Ren, Yingjun Wu

- **Data Enclave: A Data-Centric Trusted Execution Environment.**
  2024 · TEE · [HPCA](https://doi.org/10.1109/HPCA57654.2024.00026)
  Yan Solihin, James Pangia, Xipeng Shen, Yuanchao Xu, Chencheng Ye

- **CAGE: Complementing Arm CCA with GPU Extensions.**
  2024 · TEE · [NDSS](https://www.ndss-symposium.org/ndss-paper/cage-complementing-arm-cca-with-gpu-extensions/)
  Kevin Leach, Chenxu Wang, Shoumeng Yan, Fengwei Zhang, Yunjie Deng, Jiannong Cao, Zhenyu Ning, Zhengyu He

- **Building a Lightweight Trusted Execution Environment for Arm GPUs.**
  2024 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2023.3334277)
  Kevin Leach, Shoumeng Yan, Fengwei Zhang, Zhengyu He, Chenxu Wang, Zhenyu Ning, Jin Li, Yunjie Deng, Jiannong Cao

- **ACAI: Protecting Accelerator Execution with Arm Confidential Computing Architecture.**
  2024 · TEE · [USENIX Security](https://www.usenix.org/conference/usenixsecurity24/presentation/sridhara)
  Shweta Shinde, Supraja Sridhara, Mark Kuhne, Benedict Schlüter, Andrin Bertschi, Fabio Aliberti

- **A Quantum Computer Trusted Execution Environment.**
  2024 · TEE · [HPCA](https://doi.org/10.1109/HPCA57654.2024.00051)
  Sanjay Deshpande, Chuanqi Xu, Yao Lu, Theodoros Trochatos, Yongshan Ding, Jakub Szefer

- **A Comprehensive Trusted Runtime for WebAssembly With Intel SGX.**
  2024 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2023.3334516)
  Marcelo Pasin, Giovanni Mazzeo, Darshan Vaydia, Valerio Schiavoni, Arne Hollum, Jämes Ménétrey, Pascal Felber

### 2023

- **Trust TEE?: Exploring the Impact of Trusted Execution Environments on Smart Home Privacy Norms.**
  2023 · TEE · [PoPETs](https://doi.org/10.56553/POPETS-2023-0067)
  Pratik Musale, Adam Lee

- **Trust Beyond Border: Lightweight, Verifiable User Isolation for Protecting In-Enclave Services.**
  2023 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2021.3138427)
  XiaoFeng Wang, Dongdai Lin, Hongliang Tian, Hongbo Chen, Wenhao Wang, Weijie Liu

- **TeeBench: Seamless Benchmarking in Trusted Execution Environments.**
  2023 · TEE · [SIGMOD](https://doi.org/10.1145/3555041.3589726)
  Jorge-Arnulfo Quiané-Ruiz, Tilman Dietzel, Kajetan Jeremi Maliszewski, Volker Markl

- **TSC-VEE: A TrustZone-Based Smart Contract Virtual Execution Environment.**
  2023 · TEE · [TPDS](https://doi.org/10.1109/TPDS.2023.3263882)
  Tao Li, Youyang Qiao, Zhiyuan Zhou, Ye Lu, Yaozheng Fang, Xueshuo Xie, Zhaolong Jian, Dayi Yang

- **TEESec: Pre-Silicon Vulnerability Discovery for Trusted Execution Environments.**
  2023 · TEE · [ISCA](https://doi.org/10.1145/3579371.3589070)
  Yuan Xiao, Radu Teodorescu, Kristin Barber, Moein Ghaniyoun, Yinqian Zhang

- **TEE-based General-purpose Computational Backend for Secure Delegated Data Processing.**
  2023 · TEE · [SIGMOD](https://doi.org/10.1145/3626757)
  Sheng Wang, Jialin Li, Feifei Li, Kian-Lee Tan, Mo Sha

- **T-Counter: Trustworthy and Efficient CPU Resource Measurement Using SGX in the Cloud.**
  2023 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2022.3145814)
  Chuntao Dong, Qingni Shen, Zhonghai Wu, Daoqing Yu, Xuhua Ding, Pengfei Wu, Wu Luo

- **SymGX: Detecting Cross-boundary Pointer Vulnerabilities of SGX Applications via Static Symbolic Execution.**
  2023 · TEE · [ACM CCS](https://doi.org/10.1145/3576915.3623213)
  Shengjian Guo, Yuanpeng Wang, Yao Guo, Qinkun Bao, Ningyu He, Zhineng Zhong, Xiangqun Chen, Ziqi Zhang, Ding Li

- **Shielding Graph for eXact Analytics With SGX.**
  2023 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2023.3241164)
  Lingchen Zhao, Qian Wang, Minxin Du, Peipei Jiang, Sherman S. M. Chow

- **Safe and Practical GPU Computation in TrustZone.**
  2023 · TEE · [EuroSys](https://doi.org/10.1145/3552326.3567483)
  Felix Xiaozhu Lin, Heejin Park

- **SHELTER: Extending Arm CCA with Isolation in User Space.**
  2023 · TEE · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/zhang-yiming)
  Yuxin Hu, Shoumeng Yan, Fengwei Zhang, Haoyang Huang, Yiming Zhang, Zhengyu He, Zhenyu Ning, Xiapu Luo

- **Root Crash Consistency of SGX-style Integrity Trees in Secure Non-Volatile Memory Systems.**
  2023 · TEE · [HPCA](https://doi.org/10.1109/HPCA56546.2023.10071003)
  Jianming Huang, Yu Hua

- **Reusable Enclaves for Confidential Serverless Computing.**
  2023 · TEE · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/zhao-shixuan)
  Guoxing Chen, Mengya Zhang, Shixuan Zhao, Pinshen Xu, Yinqian Zhang, Zhiqiang Lin

- **Oops..! I Glitched It Again! How to Multi-Glitch the Glitching-Protections on ARM TrustZone-M.**
  2023 · TEE · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/sass)
  Xhani Marvin Saß, Richard Mitev, Ahmad-Reza Sadeghi

- **Olive: Oblivious Federated Learning on Trusted Execution Environment Against the Risk of Sparsification.**
  2023 · TEE · [VLDB](https://doi.org/10.14778/3603581.3603583)
  Yang Cao, Fumiyuki Kato, Masatoshi Yoshikawa

- **MyTEE: Own the Trusted Execution Environment on Embedded Devices.**
  2023 · TEE · [NDSS](https://www.ndss-symposium.org/ndss-paper/mytee-own-the-trusted-execution-environment-on-embedded-devices/)
  Seung-Kyun Han, Jin Soo Jang

- **EnigMap: External-Memory Oblivious Map for Secure Enclaves.**
  2023 · TEE · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/tinoco)
  Sixiang Gao, Afonso Tinoco, Elaine Shi

- **Enabling Secure and Efficient Data Analytics Pipeline Evolution with Trusted Execution Environment.**
  2023 · TEE · [PVLDB](https://doi.org/10.14778/3603581.3603589)
  Cong Yue, Zhiyong Huang, Haotian Gao, Tien Tuan Anh Dinh, Beng Chin Ooi

- **ESMAC: Efficient and Secure Multi-Owner Access Control With TEE in Multi-Level Data Processing.**
  2023 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2022.3215977)
  Wenxiu Ding, Zheng Yan, Yaxing Chen, Zhiguo Wan, Yuxuan Cai, Dan Liu

- **ENCIDER: Detecting Timing and Cache Side Channels in SGX Enclaves and Cryptographic APIs.**
  2023 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2022.3160346)
  Kevin R. B. Butler, Grant Hernandez, Tuba Yavuz, Jing (Dave) Tian, Farhaan Fowze, Ken Yihang Bai

- **Cracking-Like Join for Trusted Execution Environments.**
  2023 · TEE · [PVLDB](https://doi.org/10.14778/3598581.3598602)
  Jorge-Arnulfo Quiané-Ruiz, Kajetan Jeremi Maliszewski, Volker Markl

- **CVTEE: A Compatible Verified TEE Architecture With Enhanced Security.**
  2023 · TEE · [TDSC](https://doi.org/10.1109/TDSC.2021.3133576)
  Rui Chang, Xinliang Miao, Jianhong Zhao, Kui Ren, Shuang Cao, Liehui Jiang, Tao Wei, Yongwang Zhao

- **Accelerating Extra Dimensional Page Walks for Confidential Computing.**
  2023 · TEE · [MICRO](https://doi.org/10.1145/3613424.3614293)
  Yubin Xia, Bicheng Yang, Haibo Chen, Dong Du

- **AEX-Notify: Thwarting Precise Single-Stepping Attacks through Interrupt Awareness for Intel SGX Enclaves.**
  2023 · TEE · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/constable)
  Yuan Xiao, Ilya Alexandrovich, Jo Van Bulck, Taesoo Kim, Xiang Cheng, Scott Constable, Cedric Xing, Mona Vij, Frank Piessens, Mark Silberstein

- **A Verified Confidential Computing as a Service Framework for Privacy Preservation.**
  2023 · TEE · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/chen-hongbo)
  Kang Li, Mingshen Sun, XiaoFeng Wang, Haobin Hiroki Chen, Hongbo Chen, Zhaofeng Chen
