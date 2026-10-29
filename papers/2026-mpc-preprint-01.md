# 2026 · MPC · 仅预印本来源 · 第 1/6 页

[总目录](../PAPERS.md) · [下一页](2026-mpc-preprint-02.md)

- **Rerandomizable Garbling Beyond BHHO-KMHE and a Construction from LWE**
  2026-10-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2664)
  Raphael Heitjohann, Jonas von der Heyden, Tibor Jager

  <details><summary>摘要 / Abstract</summary>

  Rerandomizable garbling schemes (RGS) are a fundamental primitive enabling advanced cryptographic constructions such as multi-hop homomorphic encryption (Gentry, Halevi, Vaikuntanathan, CRYPTO 2010), iO-combiners (Ananth, Jain, Naor, Sahai, Yogev, CRYPTO 2016), and YOSO-style MPC (Acharya, Hazay, Kolesnikov, Prabhakaran, TCC 2022 and CRYPTO 2024). All known RGS instantiations rely on discrete-logarithm-type assumptions, concretely via the BHHO scheme (Boneh, Halevi, Hamburg, Ostrovsky, CRYPTO 2008) and its recent pairing-based variant (Heitjohann, von der Heyden, Jager, CRYPTO 2025). This reliance stems from the use of key-and-message homomorphic encryption (KMHE) that supports rerandomization and strong &quot;key-privacy under leakage&quot;, which hides the applied homomorphic transformations and is currently only achievable using BHHO-style bitwise encryption in combination with permutation-based homomorphisms. Our first main contribution is a new garbling technique that shifts the burden of hiding homomorphic transformations from the encryption scheme to the garbling itself. This allows us to construct RGS from KMHE schemes with substantially weaker properties, avoiding the need for bitwise encryption and permutation-based homomorphisms, and enabling the construction of RGS from KMHE with other homomorphisms, such as additively-homomorphic ones. As a second contribution, we give a concrete lattice-based instantiation of the required KMHE primitive, based on LWE. This construction is a variant of the GSW FHE scheme (Gentry, Sahai, Waters, CRYPTO 2013), which uses new techniques for rerandomization and is tailored to the requirements of our new garbling scheme by supporting a &quot;homomorphic&quot;/&quot;lossy&quot; mode. This yields the first RGS construction that does not rely on discrete-logarithm assumptions and may provide post-quantum security.

  匹配依据：MPC: garbling scheme, garbling schemes

  </details>

- **OblivDGL: Oblivious Deep Graph Learning Made Practical**
  2026-10-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2655)
  Yiming Qin, Xiaoning Liu, Shangqi Lai, Joseph K. Liu, Xingliang Yuan

  <details><summary>摘要 / Abstract</summary>

  The rapid deployment of Graph Neural Networks (GNNs) within Machine Learning as a Service (MLaaS) has opened up new privacy concerns. Both sensitive graph data and proprietary GNN models are submitted to and processed in third-party MLaaS platform for training and inference. To alleviate those concerns, recent efforts have been made to design tailored secure computation protocols for GNNs. Unfortunately, existing designs cannot accomplish security, functionality, and scalability simultaneously. They leak a certain degree of graph information, offer limited support on secure training of GNNs, and can hardly scale to large graphs. In this paper, we design and implement OblivDGL, an oblivious deep graph learning framework for secure GNN inference and training. Our design is inspired by Deep Graph Library (DGL), an industrial practice for graph learning. At its core, we distill the secure computational patterns of GNNs into a generalized form, and empower both secure GNN training and inference through a novel oblivious message passing paradigm. To realize such a paradigm, we design a new oblivious graph representation, and realize it by function secret sharing (FSS), a lightweight secure computation technique with low latency. Compared to prior secure GNN systems, OblivDGL achieves the most stringent privacy guarantees, i.e., revealing no private information except for the total number of edges and nodes. One standout feature of OblivDGL is the scalability of processing encrypted graphs by carefully tailored parallelization designs. Extensive evaluations on four benchmark graph datasets demonstrate that, compared to state-of-the-art secure GNN frameworks, OblivDGL reduces communication cost by up to 1024x and achieves up to 14.3x speedup in runtime during secure training. For secure inference, OblivDGL achieves up to 754x lower communication and a 4.19x speedup.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Asynchronous Verifiable and Complete Secret Sharing: From Design Patterns to System-Level Trade-offs**
  2026-10-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.37234)
  Joachim Bruneau-Queyreix, Martin Zivojinovic, Leo Mendiboure, Tom Claudel, Laurent Réveillère

  <details><summary>摘要 / Abstract</summary>

  Modern secret sharing protocols promise robust secret sharing in fully asynchronous Byzantine systems, but their practical costs remain difficult to compare across papers, assumptions, and workloads. The difficulty is not merely experimental: protocols with similar asymptotic guarantees often place very different work on the critical path through their choices of dissemination, verification, batching, and recovery. This paper turns that fragmented research landscape into a corpus-backed designspace analysis and systems evaluation of asynchronous verifiable and complete secret sharing. We derive a design sieve, select seven representative protocols, and implement them in a common Rust framework. In our experiments on the Grid&#x27;5000 platform, we evaluate honest-dealer and faulty-dealer stress executions using latency, throughput, message count, bandwidth, and aggregate CPU-time. The results show that message complexity alone poorly predicts latency, that optimistic paths can be dominated by recovery cost, and that batching or packing helps only when verification stays off the critical path. These findings turn protocol-by-protocol comparisons into design-to-cost guidance for choosing, implementing, and extending asynchronous verifiable and complete sharing protocols.

  匹配依据：MPC: secret sharing

  </details>

- **Reverse Substitution in Secret Sharing: The Critical One-Half Threshold and a Route to Superpolynomial Lower Bounds**
  2026-10-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2652)
  Shahram Khazaei

  <details><summary>摘要 / Abstract</summary>

  The contribution vector (convec) of a secret-sharing scheme is the vector of its normalized share sizes. The average and maximum coordinates of a convec give, respectively, the average and maximum information ratios of the scheme. Obtaining superlinear lower bounds on these quantities for unrestricted perfect secret sharing has remained a challenging open problem for about four decades. In this paper, we study substitution, a natural way to build complicated access structures from simpler ones: one participant of an outer access structure is replaced by an inner access structure. Given secret-sharing schemes for the two factors, the standard forward construction composes them into a scheme for the composite access structure. We study the converse question. Given an arbitrary scheme for the composite access structure, we ask to what extent its convec admits a reverse factorization into convecs for the outer and inner factors, up to a common multiplicative loss. Exact reversal is false: we give a counterexample whose optimal reverse factor is \(8/9\), with a composite scheme that is scalar-linear over every finite field. On the positive side, we prove that a factor \(1/2\) is always attainable, and that every fixed instance admits a strictly larger factor. For a recursive family built from Csirmaz’s classical access structure \(\mathcal C_k\), whose distinguished set has size \(k\), we identify a critical reverse factor that determines when the resulting lower bound becomes superlinear. This critical factor exceeds one half by only an amount of order \((\log k)/k\). Crossing it yields superlinear lower bounds, while any fixed positive excess above one half gives a route to superpolynomial lower bounds. Using only Shannon inequalities, the corresponding recursive factor cannot cross the critical value. Thus any improvement sufficient to pass this threshold must exploit constraints beyond the Shannon inequalities.

  匹配依据：MPC: secret sharing

  </details>

- **Minimality of Binary Codes From Weight Layers and Graph Cut Spaces**
  2026-10-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.35372)
  Xianhong Xie, Mengni Wang, Tingting Wu

  <details><summary>摘要 / Abstract</summary>

  Minimal binary linear codes play an important role in secret-sharing schemes and in the structural study of linear codes. We study the minimality of three classes of known constructions: codes from a single complete Hamming-weight layer, codes from arbitrary unions of such layers and graph cut-space codes. For the previously studied single-layer codes C, we give a complete minimality classification: C is minimal if and only if t is even. For t = 4, we determine the minimum and maximum weights, and show that the family strictly violates the binary Ashikhmin Barg sufficient condition for every k. We also calculate the minimum distance of the dual code. For arbitrary unions of complete Hamming-weight layers, we obtain an if-and-only-if classification of minimality and uniform criteria for evenness, self-orthogonality, the doubly even property and hull dimension. We further analyze the family for odd k. Finally, using the classical bond characterization of cuts, we translate minimality of graph cut space codes into a graph-theoretic condition: a nonempty simple graph has a minimal cut code precisely when it has one edge-containing component and that component is complete. We also give a graph-function realization of the known binary tetrahedron code and explicitly identify the resulting code equivalence.

  匹配依据：MPC: secret sharing

  </details>

- **Information-Theoretic Secure Aggregation With Heterogeneous Client Quantization**
  2026-10-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.35833)
  Shreya Meel, Sennur Ulukus, Itzhak Tamo

  <details><summary>摘要 / Abstract</summary>

  In federated learning (FL), secure aggregation enables a server to compute the sum of local model updates of $N$ clients, without revealing any information on the individual model updates to the server, beyond their sum. Different clients may be subject to heterogeneous bandwidth constraints, and consequently may choose different numbers of quantization levels to represent the information they send. Most secure aggregation works require the clients to project the values of their update parameters to a common finite group (or field), which does not directly accommodate heterogeneous precision constraints on their transmitted masked updates. Existing approaches of secure aggregation with heterogeneous quantization levels reveal partial aggregates of model-updates, and can reveal segments of individual model updates, under certain dropout and client-server collusion patterns. To prevent this privacy breach, we propose an information-theoretic secure aggregation scheme that tolerates client drop-outs, and up to $T$ semi-honest clients that collude with each other and with the server, under heterogeneous quantization at clients. Our protocol utilizes the $(T+1, N)$ threshold black-box secret sharing construction, where secret shares of the client updates, despite belonging to distinct algebraic groups owing to different quantization, are generated from identical linear integer systems.

  匹配依据：MPC: secret sharing

  </details>

- **HELLO, GOODBYE: Concurrent General Composition From Super-Rushing Security**
  2026-10-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2651)
  Anirudh Chandramouli

  <details><summary>摘要 / Abstract</summary>

  Kushilevitz, Lindell, and Rabin (STOC `06, SIAM Journal on Computing `10), in their seminal result, showed that any standalone-secure synchronous multiparty computation (MPC) protocol can be compiled into one secure under concurrent general composition, by adding a synchronisation step after every round; thereby, at least doubling the round complexity. We show that for protocols that are secure against super-rushing adversaries, introduced by Asharov, Chandramouli, Cohen, and Ishai (EuroCrypt `25), two synchronisation rounds suffice. Specifically, for an $R$-round protocol that is secure against super-rushing adversaries with a black-box, straight-line simulator, adding a round of start synchronisation (saying ``HELLO&#x27;&#x27;) and a round of end synchronisation (saying ``GOODBYE&#x27;&#x27;) yields security under concurrent general composition with selective abort in $R+2$ rounds. If the end synchronisation is over a broadcast channel, the security is upgraded to unanimous abort. Both compilers incur no loss in the security reduction and preserve the flavour of security (perfect, statistical, or computational) of the underlying synchronous protocol. Moreover, combining with the sufficient conditions of Asharov et al. for perfect security, and the round-preserving super-rushing compilers of Ciampi, Ravi, and Zou (Cryptology ePrint Archive 2026/1745) for statistical and computational security, yields compilers from rushing security to security under concurrent general composition, with an additive overhead of at most $2$ rounds. We further extend our compilers to protocols with a trusted setup, such as a common reference string or a public-key infrastructure, which is necessary in the dishonest majority setting. We require two conditions. First, every execution of the protocol uses its own stateless copy of the setup, whose responses to the adversary do not depend on the interactions of the honest parties. In particular, this rules out setups that are shared across executions, such as a global common reference string or a single public-key infrastructure used by every execution. Second, the underlying protocol is secure against super-rushing adversaries with adaptive inputs, that is, even when the inputs are chosen after interacting with the setup. Under these conditions, the same compilers yield security under concurrent general composition. We also show that adaptive inputs cannot be relaxed to the usual notion of security in the setup-hybrid model. Specifically, we give a protocol that is statistically secure against super-rushing adversaries with guaranteed output delivery under the standard hybrid model, but is insecure under concurrent general composition after adding start and end synchronisation, even with selective abort.

  匹配依据：MPC: multiparty computation

  </details>

- **HNSecW: A Logarithmic-Time MPC Protocol for Approximate Nearest Neighbor Search**
  2026-10-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.34248)
  Fahong Zhang, Weijie Jin, Lixu Wang, Ning Luo, Xiao Wang, Wei Dong

  <details><summary>摘要 / Abstract</summary>

  As a core component of modern RAG systems, approximate nearest neighbor (ANN) search has been extensively studied for decades. In practice, deploying ANN often requires symmetric privacy, where the querier&#x27;s query and the database owner&#x27;s data must remain hidden from each other, necessitating a secure multi-party computation (MPC) solution. So far, most MPC-based ANN protocols follow a cluster-based approach: they evaluate distances for the query over a large candidate set and rely on heavyweight primitives such as distributed ORAM to hide access patterns. As a result, each search typically requires $O(\sqrt{N})$ time. We propose HNSecW, a novel MPC protocol for ANN search that achieves the $O(\log N)$ search time for the first time. We first study the single-query setting. Starting from HNSW, the state-of-the-art ANN algorithm, we redesign its control flow and data structures to achieve fully data-independent execution. To further achieve logarithmic search time, we employ offline reshuffling and partial database duplication. Furthermore, we extend our protocol to support multiple sequential queries by introducing a &quot;double visited&quot; caching structure that eliminates redundant cross-query memory accesses, thereby avoiding per-query online shuffling. In addition, we develop a batch-query protocol that exploits higher parallelism to reduce both round complexity and the circuit&#x27;s critical path. Our experiments show that HNSecW preserves the high accuracy of plaintext HNSW ($\geq 90\%$ recall) and delivers over a $20\times$ efficiency improvement over prior work on million-scale datasets.

  匹配依据：MPC: secure multi party computation

  </details>

- **Tritone: Pairwise Garbled Disputes for Multi-Party Proof Verification on Bitcoin**
  2026-10-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2612)
  Oleksii Avramenko, Alessandro Baccarini, Torben Poguntke

  <details><summary>摘要 / Abstract</summary>

  Bitcoin Script lacks native pairing operations for efficient direct verification of Groth16 proofs. Conventional federated bridges instead authorize withdrawals through a signing quorum, whose collusion can release funds without valid evidence. We present the Tritone protocol, which lets Bitcoin enforce the outcome of verifying a Groth16 proof for an NP relation fixed in a one-time trusted setup, with the locked funds secure as long as one of a fixed set of $N$ operators is honest. Verification is optimistic and off-chain, and every transaction is standard under current relay policy, so Tritone runs on Bitcoin today without consensus changes. Tritone generalizes the two-party BABE protocol to a fixed committee of $N$ operators, with one dispute instance per ordered pair. Cut-and-choose protects against malicious garblers, while Feldman verifiable secret sharing correlates input keys across candidates. Our new Lamport-adaptor gadget forces a challenging verifier to disclose the shares selected by the prover&#x27;s committed proof element, providing the transaction-level binding left unspecified by BABE. A single set of disclosed shares then unlocks all retained candidates. We formalize the multi-party primitive, prove the protocol secure against up to $N-1$ statically corrupted operators, and specify its complete pre-signed transaction graph. We implement Tritone in Rust. On Bitcoin mainnet, when one verifier disputes a claim at every stage, the prover-candidate posts 9,607 vB and the verifier 18,160 vB of protocol transactions. In local benchmarks at 40-bit statistical security, the prover-candidate of each dispute instance retains as little as 112.83 MiB. Tritone thus replaces trust in a signing quorum with a single-honest-operator assumption wherever locked bitcoin is released to an operator against a Groth16 proof, with Bitcoin bridges as our showcase.

  匹配依据：MPC: secret sharing

  </details>

- **Traceable Quantum Secret Sharing**
  2026-10-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.32218)
  Mengyan Qiao, Jian Long, Yu Li, Zhu Cao

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing protects distributed quantum information against unauthorized reconstruction, yet existing schemes provide no intrinsic accountability when shares are leaked or forged. This missing capability is particularly relevant in realistic distributed settings, where compromised participants may either expose valid shares or maliciously interfere with reconstruction. Here we establish a framework for traceable quantum secret sharing under these two threat models. We introduce leakage-verifiable and traceable quantum secret sharing (LVT-QSS), which attributes leaked shares through an explicit leakage verification mechanism, and malicious-traceable and accountable quantum secret sharing (MTA-QSS), which identifies participants who submit forged shares during reconstruction. We formulate security definitions for both settings and prove that the proposed protocols satisfy the corresponding guarantees against the relevant adversaries. Numerical simulations under per-share depolarizing noise further quantify the robustness of the proposed schemes and identify verification as the dominant noise sensitive stage. These results incorporate accountability into quantum secret sharing and provide a foundation for traceable distributed quantum cryptography.

  匹配依据：MPC: secret sharing

  </details>

- **Smaller Share Size for Evolving Secret Sharing: General Thresholds and Threshold Three**
  2026-10-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2619)
  Xiaozheng Wang

  <details><summary>摘要 / Abstract</summary>

  Evolving secret sharing allows participants to join indefinitely without modifying previously distributed shares. We study the share size of perfectly secure evolving threshold secret sharing schemes and obtain two improvements. For general thresholds, we introduce a polynomial sharing method that shares two secrets with adjacent reconstruction thresholds using one polynomial. Combining this method with the evolving scheme of Cheng et al.\ (ASIACRYPT 2025), we obtain an evolving $k$-threshold scheme whose $t$-th share has size \[ \left\lfloor \frac{k}{2} \right\rfloor \log_2 t + O_k\!\left(\ell+\log_2\log_2 t\right) \] bits for an $\ell$-bit secret. This reduces the leading coefficient of their general construction from $k-1$ to $\lfloor k/2\rfloor$. For threshold three, we give a separate construction that reduces the lower-order terms of the scheme of Cheng et al. We mask the short shares in all generations with the same random $\ell$-bit value $R$, which is shared through an evolving $2$-threshold scheme, we obtain \[ \log_2 t+(2+o(1))\log_2\log_2 t \] bits per share for fixed $\ell$. Both constructions satisfy correctness and perfect information-theoretic security.

  匹配依据：MPC: secret sharing

  </details>

- **Quantum Secret Sharing from CSS qLDPC Codes: Computable Access Structures, Accessible Logical Dimension, and Topology-Aware Network Cost**
  2026-10-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.32428)
  Malik Mouaji, Saif Al-Kuwari

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) schemes can be constructed from quantum error-correcting codes, but characterizing their access structures and implementation costs becomes challenging for finite-length, high-rate quantum low-density parity-check (qLDPC) codes. We develop an exact computational framework for QSS induced by CSS qLDPC codes. The framework characterizes authorized, forbidden, and intermediate coalitions using restricted parity-check matrices and binary linear algebra, and introduces the accessible logical dimension \(κ(A)\), defined through the symplectic rank of locally supported logical classes, to refine the characterization of intermediate coalitions. We further incorporate physical network constraints through separate Tanner-incidence, Steiner-routing, and scheduling-depth costs, and treat the partitioning of physical qubits into participants as an explicit design variable. Numerical experiments on four CSS qLDPC codes verify the predicted complement duality and monotonicity properties and show substantial variation in access transitions and network costs. For the codes studied, the bivariate bicycle instance exhibits the sharpest transition, while network embedding costs vary by more than an order of magnitude across physical topologies. We also show that participant partitioning can substantially improve block-level security and reconstruction thresholds. These results provide a practical bridge between the algebraic structure of CSS qLDPC codes, the graded accessibility of quantum secrets, and the physical constraints of networked QSS implementations.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Federated Loss Exploration for Vision-Based Perception under Non-IID Data**
  2026-10-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.32626)
  Nergiz Yuca, Christian Internò, Nikolay Matyunin, Markus Olhofer, Barbara Hammer, Stefan Katzenbeisser

  <details><summary>摘要 / Abstract</summary>

  Vision-based image classification models benefit from Federated Learning (FL) across vehicles, however learning accurate models from distributed vehicular cameras is challenging due to data heterogeneity and privacy concerns. To improve performance on non-IID data, advanced FL optimization approaches have emerged that share auxiliary insights, such as client gradient behaviors. While these gradient-guided optimized FL methods improve the model accuracy, their reliance on sharing additional gradient information introduces a previously unexplored privacy vulnerability. In our empirical privacy-leakage experiment, we show that a malicious server can infer clients&#x27; label sets from shared guidance matrices under heterogeneous client label distributions (simulated via Dirichlet-based label partitions), between 50% and 84% accuracy. To address this privacy leakage, we propose PPFLex that replaces the central server with three Secure Multi-Party Computation (MPC) servers to securely compute the global guidance matrix and perform federated averaging under semi-honest and malicious MPC server assumptions. We evaluate PPFLex on widely used traffic-sign classification datasets (e.g., GTSRB and BTSC) as representative autonomous vehicle perception benchmarks, comparing against baselines. Our results show that PPFLex achieves accuracy comparable to the plain-text FedLEx pipeline while preventing privacy leakage, incurring acceptable MPC overhead.

  匹配依据：MPC: secure multi party computation

  </details>

- **The Entire Quantum Computer on a Classical Leash**
  2026-10-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.31775)
  Yael Tauman Kalai, Dakshita Khurana, Justin Raizes

  <details><summary>摘要 / Abstract</summary>

  We show that a classical client with no quantum hardware can use a single untrusted and potentially malicious quantum server as if it were its own trusted quantum computer. Through the server, the client can privately choose and run quantum computations, prepare quantum states, and process quantum states supplied by other parties. It can also keep quantum memory on the server, hidden from the server itself, and use that memory in later computations so its quantum state persists across rounds of interaction. Together, these capabilities let a purely classical party act as a quantum party in a variety of interactive protocols. We expect this virtual quantum computer to be a broadly useful tool. As immediate applications, we resolve two known open problems: (1) classical verification of quantum sampling with negligible computational soundness error, and (2) remote state preparation of arbitrary efficiently preparable quantum states. Underlying all of these results is a general-purpose, maliciously secure two-party computation protocol between a classical client and a quantum server, which we construct assuming only the post-quantum hardness of learning with errors.

  匹配依据：MPC: secure two party computation

  </details>

- **SILMARILS-MV: Information-Theoretically Secure Multi-Verifier Signatures with Dealer-Free Key Issuance and Linear Aggregation for Permissioned Blockchains**
  2026-10-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.31814)
  Khadijeh Bagheri, Hassan Khodaiemehr, Chen Feng

  <details><summary>摘要 / Abstract</summary>

  Permissioned blockchains authenticate transactions, votes and quorum certificates with computationally secure signatures, and post-quantum replacements inflate consensus traffic by orders of magnitude. Information-theoretic alternatives have required a trusted authority, quantum channels, per-signature interaction, or single-use keys with bounded transfer. We present SILMARILS-MV, a multi-verifier unconditionally secure signature in which a signature is the vector $α= A\,e(m)$ and each verifier holds a secret functional $c_i = Γ^T λ(x_i)$ derived from virtual anchors $Γ$ that nobody learns. Against unbounded adversaries corrupting up to $ω$ verifiers and any signers, and observing every decision, an honest verifier accepts a forged or invalid signature with probability at most $Q/q + 1/(q-1)$, a bound that is tight in its leading term. The scheme is strongly unforgeable, non-repudiable, transferable across unboundedly many hops, and linearly aggregatable. Keys are issued by the validators through perfectly secure MPC for $t &lt; n/3$, without broadcast. To scale, we let the committee itself sign: in threshold notarization, finality certificates have constant size $32(ω+1)$ bytes and per-validator issuance cost no longer depends on $n$. Arbiter-verified keys give clients 32-byte signatures, robust redistribution supports membership changes and share refresh, and verifiers can be enrolled retroactively. A certificate verifies in 2.4 microseconds. In an analytic normal-case model at 1000 validators, threshold notarization needs 71 KiB of authentication traffic per validator per block, 22x less than ML-DSA-44 for admitted verifiers. In a Rust HotStuff prototype with 100 validators, SILMARILS-MV commits 2.8x more transactions per second than ML-DSA-44 with 67x less cryptographic CPU, and Monte-Carlo attacks match the bounds.

  匹配依据：MPC: mpc (context)

  </details>

- **Integer Coordinate Families and Threshold RSA Signatures for Any Prime Exponent**
  2026-10-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2601)
  Shivansh Jaiswal, Somitra Sanadhya

  <details><summary>摘要 / Abstract</summary>

  At CT-RSA 2026, Ng and Lau introduced $(t,n)$-integer coordinate families for threshold RSA signatures with $e=3$, and found some families by heuristic search for $2\le t \le n \le 9$. They asked whether such families always exist and, if so, can they be constructed efficiently. We answer both of these questions positively. We prove that a $(t,n)$-integer coordinate family is also a $(t+1,n)$-integer coordinate family. We construct such families for $t=2$, and $2\le n &lt; 19$, using a polynomial time algorithm in $n$ and its output bit length. Answering another question raised in the Ng-Lau work, we prove super-polynomial lower bounds on coordinates of pairwise families. We also find the minimum families for $n \le 9$. Ng and Lau proposed a threshold signature scheme based on integer coordinate families. We show that the Ng-Lau scheme admits trivial forgeries, and has a flawed proof. We give a repaired scheme $\mathrm{PiIC}$ which does not suffer from these issues. Finally, we propose an integer secret-sharing scheme $\mathrm{PiZ}$ that works for every prime $e$ and every $(t,n)$, without relying on any special coordinate family. We prove that both the schemes $\mathrm{PiIC}$ and $\mathrm{PiZ}$ are TS-UF-CMA secure under the standard RSA assumption.

  匹配依据：MPC: secret sharing

  </details>

- **Efficient Laconic Oblivious Transfer with Malicious Security**
  2026-10-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2593)
  Yijian Zhang, Zuoxia Yu, Rupeng Yang, Willy Susilo

  <details><summary>摘要 / Abstract</summary>

  Laconic Oblivious Transfer (OT) enables a receiver to compress a large database into a short digest, allowing a sender to generate a succinct ciphertext that reveals only a single indexed message. While prior works achieve efficient constructions in the semi-honest model, known solutions for malicious security rely on inherently heavy non-black-box techniques, such as garbled circuits or succinct arguments, resulting in impractical schemes. In this work, we present the first construction of maliciously secure laconic OT that makes fully black-box use of its underlying primitives. Our construction is based on a simple and widely used paradigm combining vector commitments with witness encryption, previously known to yield efficient semi-honest protocols. We show that this approach can in fact achieve malicious security by introducing two minimal yet powerful enhancements: equivocal vector commitments and maliciously secure witness encryption. We prove that these properties suffice to obtain laconic OT with security against malicious senders in the universal composability model and against malicious receivers in the context model. We instantiate our framework from standard assumptions, including LWE and bilinear Diffie-Hellman variants, obtaining schemes in the standard model. Notably, our constructions avoid heavy non-black-box tools mentioned before, and therefore achieve efficiency comparable to the state-of-the-art black-box constructions with merely semi-honest security. In particular, in certain settings, we obtain malicious security at essentially no additional asymptotic cost. Our results resolve a central question on the feasibility of practical, maliciously secure laconic OT, and provide a unifying pathway for efficiently achieving malicious security in laconic cryptography.

  匹配依据：MPC: garbled circuits, oblivious transfer

  </details>

- **Semantic-Aware Update Admission and Adaptive Byzantine Redundancy for Secure Computation Offloading in COIN-Enabled Metaverse Systems**
  2026-10-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.29592)
  Ibrahim Aliyu, Jaehyung Park, Jinsul Kim

  <details><summary>摘要 / Abstract</summary>

  Computing in the network (COIN) supports latency-sensitive Metaverse services, but blockchain commitment of persistent shared-state updates competes with application execution for limited resources. We consider the joint problem of deciding which updates to commit, how much Byzantine redundancy to provision, and where to execute Metaverse application tasks. We formulate this problem under resource, latency, and practical Byzantine fault tolerance (PBFT) constraints, accounting for update persistence and semantic significance. We develop a hierarchical redundancy-aware PBFT (R-PBFT) approach that decomposes the decision process into slot-wise computation offloading and sequential update-admission and redundancy control. We formulate the former as an identical-interest game and address the latter using a feasibility-filtered double deep Q-network (DDQN). Analytical downlink allocation accounts for the energy and delivery-feasibility effects of consensus latency. For fixed slot state and redundancy, we establish the game&#x27;s exact-potential property and finite termination of strict sequential improvements. Feasible-action filtering enforces configured Byzantine redundancy and blockchain-budget constraints independently of learning. Numerical results show relative improvements of up to $46.7\%$ in reward averaged across tested user loads and seeds over Minimum Secure, the strongest baseline on average. At the highest tested Byzantine bound, the secure timely-update ratio improves by $62.3\%$ over the same baseline. Ablations assess the contributions of feasibility filtering and adaptive deferral.

  匹配依据：MPC: secure computation

  </details>

- **Rerandomizable Garbling for Arithmetic Circuits**
  2026-10-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2590)
  Anasuya Acharya, Pierre Meyer, Claudio Orlandi, Lawrence Roy

  <details><summary>摘要 / Abstract</summary>

  Rerandomizable garbling is a powerful extension of Yao’s garbled circuits that allows a garbled circuit to be refreshed without changing its functionality, while preserving privacy as long as at least one rerandomization step is honest. Existing constructions, however, are limited to Boolean circuits and incur significant communication overhead. In this work, we initiate the study of rerandomizable garbling for arithmetic circuits. We present the first rerandomizable arithmetic garbling scheme, based on techniques inspired by recent advances in garbling from homomorphic secret sharing. Our construction departs fundamentally from previous approaches and achieves communication complexity $O(|\mathbf{C}|\log B)$ for circuits $\mathbf{C}$ with $B$-bounded computation. Concretely, our scheme requires 17 group elements per multiplication gate, while addition gates are free. Our scheme can be instantiated under standard subgroup-indistinguishability assumptions, including the Decisional Composite Residuosity (DCR) assumption and assumptions over class groups.

  匹配依据：MPC: garbled circuit, garbled circuits, garbling scheme, secret sharing

  </details>

- **Regular Syndrome Decoding Is Easier Than Previously Estimated**
  2026-10-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.29175) · [IACR ePrint](https://eprint.iacr.org/2026/2563)
  Jiseung Kim, Minkyu Kim, Changmin Lee, Hochang Lee

  <details><summary>摘要 / Abstract</summary>

  The Regular Syndrome Decoding (RSD) problem is a structured variant of classical Syndrome Decoding and underlies a growing number of efficient cryptographic constructions, including zero knowledge protocols, pseudorandom correlation generators, and MPC in the Head signatures. Although RSD is generally believed to be computationally hard, recent works have shown that algebraic attacks can outperform information set decoding on important RSD parameter regimes. Building on this line of work, we revisit the concrete hardness of RSD and show that many widely used parameter sets are substantially easier to solve than previously estimated. This improvement stems from a refined hybrid algebraic attack that exposes and removes a previously overlooked source of concrete complexity: the joint blockwise placement of zero coordinate guesses and syndrome based variable eliminations. Rather than treating the two guessing stages and linear elimination as largely separate choices, our method coordinates them across all regular blocks so that the guessing penalty is balanced while sufficient equations are retained for linearization. This gives a systematic block balancing principle for the entire guess reduce solve pipeline. We reassess several RSD based applications, including Ferret, Wolverine, and committed VOLE. Our estimates place at least one parameter set per application below its 128 bit target, with losses approaching 67 bits. On PCG benchmarks, we improve previous best attack costs by up to 29.77 and 25.91 bits over non binary and binary fields, respectively. Moreover, for the revised 128 bit PCG parameter sets of Liu et al. evaluated here, estimated attack costs are all below $2^{111}$ field operations. These results substantially revise the concrete security landscape of RSD and indicate that several existing parameter choices overestimate the hardness of their underlying RSD instances.

  匹配依据：MPC: mpc (context)

  </details>

- **GhostFaceMPC: Privacy-Preserving Face Recognition with Multi-Party Computation**
  2026-10-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.29987) · [IACR ePrint](https://eprint.iacr.org/2026/2499) · [Code](https://github.com/crypto-unict/GhostFaceMPC)
  Davide Carnemolla, Dario Catalano, Mario Di Raimondo

  <details><summary>摘要 / Abstract</summary>

  Facial recognition has become central to modern authentication systems, security frameworks, and personalized services. However, its widespread adoption is hindered by severe privacy risks, particularly surrounding unauthorized access to sensitive biometric data. To address these challenges, this paper presents GhostFaceMPC, the first end-to-end, privacy-preserving face recognition system to evaluate a deep convolutional neural network extractor and matching under secure multi-party computation. GhostFaceMPC enables secure processing of facial data across all stages of a face recognition process, from feature extraction and storage to matching, without exposing raw images or biometric embeddings at any stage. We introduce a multi-party computation-friendly quantization of the GhostFaceNet model and circuit optimizations that make face recognition under multi-party computation practical. The code is available at https://github.com/crypto-unict/GhostFaceMPC.

  匹配依据：MPC: multi party computation, secure multi party computation

  </details>

- **Eras MPC: Granular Preprocessing and Abort Recovery with Dynamic Committees**
  2026-10-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2588)
  Ivan Damgard, Bernardo David, Rahul Satish

  <details><summary>摘要 / Abstract</summary>

  MPC with dynamic committees achieves scalability by having small committees execute each round of the computation, instead of involving all parties in the entire execution. However, achieving Guaranteed Output Delivery in efficient information theoretical protocols requires larger honest majority committees, limiting scalability. Moreover, using preprocessed correlated randomness to speed up the computation is prohibitively expensive due to the cost of transferring such randomness to parties that have not yet joined the execution. We propose Eras MPC, a model where small dishonest majority computation committees execute one or more rounds of the computation with the help of honest majority preprocessing and checkpointing committees. The computation is carried out in &quot;Eras&quot;, which are sets of shorter epochs. In the beginning of each Era&#x27;s first epoch, a preprocessing committee generates correlated randomness for the computation epochs to be executed by different computation committees. In the end of an Era, checkpoint committees verify the current state of the computation, save this state if it is valid and provide the latest valid state to the next Era. We show an Eras MPC protocol where the preprocessing is carried out using an honest majority MPC protocol to generate authenticated Beaver triples, requiring only enough rounds of interaction to perform two subsequent batches of multiplications. The computation is done via the SPDZ online phase executed in each epoch by a small dishonest majority committee. Finally, intermediate state is checkpointed by verifying the validity of wire shares and saving wire values in $4$ rounds, each executed by a different honest majority checkpoint committee.

  匹配依据：MPC: mpc (context)

  </details>

- **Privacy-Preserving Robustness-Guided Testing**
  2026-10-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.27441)
  Charles Koll, Houssam Abbas, Mike Rosulek

  <details><summary>摘要 / Abstract</summary>

  In industries like semi-conductors and aerospace, it is common for the design company to contract out part of the testing process to a Testing-as-a-Service (TaaS) company. In such a setup, both parties want to keep their intellectual property private (i.e. unknown to the other party): namely the design and its output traces for the designer, and the detailed correctness specifications for the tester. We demonstrate a practical way for conducting provably private TaaS using a cryptographically secure multi-party computation protocol. We do so for the common setup where the specification is in Signal Temporal Logic, and testing is done using robustness-guided falsification. Our implementation carefully separates the steps of falsification, and manages to be $\textit{maximally secure}$, in the sense that the parties learn the absolutely minimum necessary for falsification. For up to a 100-dimensional input search space, the generation of one test takes less than 80 msec, and the overhead of the privacy-preserving protocol is less than 6x. These numbers mean that privacy-preserving TaaS is practical, thus enabling TaaS in security-sensitive industries.

  匹配依据：MPC: secure multi party computation

  </details>

- **Interflow: Breaking the Offline-Online Barrier for Private AI at the Edge**
  2026-10-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.27431)
  Hanieh Totonchi Asl, Ebrahim Nouri, Zhuoran Li, Danella Zhao

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving machine learning (PPML) offers a promising path toward bringing powerful AI services to the edge without exposing sensitive user data. However, its practical deployment remains constrained by the high communication, computation, and data-movement costs of secure multi-party computation (MPC), particularly during nonlinear inference. Existing MPC systems typically decouple input-independent correlated randomness generation from online execution, creating substantial memory pressure to buffer single-use cryptographic data. Moreover, limited storage can force a stop-and-refill execution pattern that repeatedly stalls the pipeline to replenish these buffers, bringing randomness generation back onto the critical path. We propose Interflow, an algorithm-hardware co-design that rethinks this separation by batch-wise processing and pipelining correlated-randomness generation with online execution: while the current batch consumes pre-generated randomness to execute secure nonlinear operations, correlation generation proceeds concurrently for the next batch. By leveraging interleaved execution, efficient data movement, and hardware acceleration, the design transforms preprocessing from a serialized, storage-intensive offline phase into a continuously overlapped pipeline that generates correlated randomness closer to the point of consumption, reducing memory footprint and data movement overhead. Implemented on the Zynq UltraScale+ ZCU102, Interflow improves nonlinear evaluation throughput by up to 1.55x for CNN operators and 1.48x for transformer operators. It achieves up to 1.26x speedup for ResNet-50 and up to 1.21x speedup for BERT-base, and reduces memory footprint by up to 37%, compared with baseline frameworks.

  匹配依据：MPC: secure multi party computation

  </details>

- **Big Secrets Small Shares: Revisiting Secure Multi-Party Computation**
  2026-10-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.27609)
  Wilton Kim, Van Long Phuoc Pham, Stanislav Kruglik, Han Mao Kiah

  <details><summary>摘要 / Abstract</summary>

  At CRYPTO 2007, Damgård and Nielsen introduced a preprocessing approach to multi-party computation (MPC) to achieve linear communication complexity. Another approach to reduce communication complexity was proposed by Cramer, Damgård, and de Haan at EUROCRYPT 2007, which involved using ramp-secret sharing schemes to jointly share base-field components of secrets from the extension field. In this paper, we combine these two ideas to achieve a non-asymptotic reduction of communication cost in a multi-phase MPC setup. We introduce a new modification of the ramp secret sharing scheme, called compact sharing, and tailor the MPC protocol to accommodate this modification. Compact sharing masks the polynomial coefficients that would otherwise leak during degree reduction. The protocol provides perfect security against static semi-honest adversaries under an explicit tradeoff between the corruption threshold and the extension degree. When the extension degree scales linearly with the number of parties, the gate-evaluation core achieves constant communication overhead relative to an extension-field element, amortized over full preprocessing batches; input and output communication is counted separately.

  匹配依据：MPC: multi party computation, secret sharing, secure multi party computation

  </details>

- **A Spectral Theory of Local-to-Global Leakage**
  2026-10-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2571)
  Rei Ueno

  <details><summary>摘要 / Abstract</summary>

  This paper studies how local leakages characterize the global leakage in additive secret sharing over a finite abelian group, which is a special case of linear secret sharing and side-channel masking. Our main finding is structural: local-to-global leakage is governed by two disjoint components---the magnitude of local leakage and its spectral alignment across shares, while existing literature attempted to characterize the global leakage only by local mutual information (MI). We first give an exact decomposition of leakage in additive secret sharing. The decomposition reveals a structural parameter invisible to MI, while previous literature conjectured that the local MI alone suffices to characterize global leakage. We then show that this missing parameter is indispensable: two leakage channels with identical local MI can induce exponentially different global leakage. Our exact decomposition identifies the missing structural quantity and completely characterizes this phenomenon. We then show the separation theorem with its realizability---local MI, despite governing the classical leakage bounds, does not even determine the exponential rate at which leakage vanishes under homomorphic composition. More strongly, we establish a universal separation theorem: even when all permutation-invariant scalar measures of local leakage agree, the global leakage can exhibit exponentially different decay rates. We further provide the characterization of the spectral alignment factor and derive its lower bound through character-order multiplicity and Möbius inversion. We then extend the framework to automorphism-weighted sharing. We establish that automorphism-weighted sharing can achieve perfect leakage cancellation with finitely many shares, even for non-trivial full-support local leakage channels. In sharp contrast, such perfect cancellation is impossible for ordinary additive sharing with non-trivial i.i.d local leakage channels and finitely many shares. Consequently, local leakage magnitudes correctly measure the average amount of local leakage, but discard the compatibility structure needed for composition. Magnitude-only bounds must optimize over structural alignments that the actual leakage channel does not realize.

  匹配依据：MPC: secret sharing

  </details>

- **PPGA: A Framework for Privacy-Preserving Graph Algorithms using the Prepare/Propagate/Gather/Apply Paradigm**
  2026-10-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2550)
  Andreas Brüggemann, Simon Brunnauer, Thomas Schneider

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving graph computation enables the secure analysis of graphs modeling social interactions and networks, financial transactions, etc., while keeping the graph private. One approach is to use secure multiparty computation (MPC), allowing different clients to contribute parts of a graph without need of disclosure, and multiple MPC protocols have been proposed for running message-passing-based graph analysis. Yet, existing public implementations are prototypes for fixed analysis functions that require substantial MPC expertise to modify and extend. We present PPGA, a practical framework based on the MultiCent protocol (PETS&#x27;25). PPGA lets users define their custom message-passing graph algorithms with a high-level interface, clients input parts of the graph, and then runs the algorithm in MPC. It significantly improves performance compared to MultiCent&#x27;s implementation, running BFS on a graph of size |V|+|E|=30 million in 23 minutes without leaking the graph topology.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Off-Key: Inconsistent MAC Keys Compromise Privacy in SPDZ-Family MPC**
  2026-10-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2533)
  Marcel Keller, Sela Navot, Nirvan Tyagi

  <details><summary>摘要 / Abstract</summary>

  SPDZ-family protocols for maliciously secure multi-party computation protect secret-shared values with message authentication codes (MACs) under a secret-shared global key. Their security requires that all values and preprocessing used together be authenticated under the same key. We present Off-Key, a privacy attack that exploits violations of this requirement. Depending on which specific MAC check protocol is used, a corrupted party can either recover the value of a shared secret from a single authentication check or test a guess through selective failure by modifying a MAC share and observing whether a masked check succeeds. While this attack does not compromise the theoretical security guarantees of the protocols, we demonstrate this key-consistency vulnerability in evaluated versions of MP-SPDZ, SCALE-MAMBA, and FANNG-MPC, which allow a corrupted party to use different keys across batches, threads, or process runs. To help implementations avoid this class of attacks, we identify the state that enforces key consistency in representative preprocessing protocols and show how preserving and reusing it prevents the attack.

  匹配依据：MPC: secure multi party computation

  </details>

- **Enjoy FAEST on Hardware: Efficient and Novel Hardware Acceleration of Emerging Post-Quantum Digital Signature Scheme FAEST**
  2026-10-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2525)
  Brendan Funk, Jiafeng Xie

  <details><summary>摘要 / Abstract</summary>

  The National Institute of Standards and Technology (NIST) Post-Quantum Cryptography (PQC) standardization process has drawn significant attention from the research community recently, especially regarding these PQC schemes&#x27; hardware acceleration. Nevertheless, related research on the emerging schemes, e.g., those currently under consideration by the NIST additional digital signature scheme standardization, still needs further exploration. With this background, this paper presents an efficient and novel hardware acceleration for FAEST, one of the promising signatures in the NIST Round 3 additional scheme competition. Overall, we have presented several layers of innovative efforts to obtain the proposed acceleration. First of all, we have conducted detailed algorithmic analysis on the major computationally intensive operations within FAEST and proposed novel design strategies and algorithms for their efficient hardware implementation. Next, we have proposed novel design efforts to construct these major operations into efficient building blocks to finalize the overall accelerator, along with the help of optimized operational phase workflow. The dedicated extension to build the L1-EM-fast accelerator is also given. Finally, we have provided a detailed and thorough evaluation process to showcase the superior performance of the proposed design over the existing complete, Sign part, and single security level MPC-in-the-head signature acceleration works. For instance, at the same security level, the proposed fast variant has at least 98\% less equivalent Area-Delay Product (eADP) than the recent complete SDitH design. To the authors&#x27; best knowledge, this is the first hardware acceleration work for FAEST, and we hope the outcome of this research will facilitate the ongoing PQC standardization process.

  匹配依据：MPC: mpc (context)

  </details>

- **QuarkShard: Decomposing Cross-Shard Requests into Single-Input Transactions**
  2026-10-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.23014)
  Changyu Duan, Zhixuan Fang

  <details><summary>摘要 / Abstract</summary>

  Sharding blockchains enhance scalability by distributing the workload across multiple shards. Within sharding blockchains, securely and efficiently processing cross-shard user requests remains a pivotal challenge. Traditional sharding blockchain protocols execute cross-shard requests under a processing paradigm that treats each user request as a monolithic entity to preserve its atomicity, inherently introducing significant intra-shard BFT execution overhead and cross-shard communication overhead. We propose QuarkShard, a sharding protocol that breaks away from this traditional paradigm to achieve intra-shard and cross-shard overheads below the lower bounds imposed by conventional approaches. QuarkShard decomposes cross-shard requests into single-input-shard transactions, where each transaction requires consensus and processing within only a single shard, thereby substantially reducing total request processing overhead. Meanwhile, through a carefully designed request decomposition algorithm, QuarkShard guarantees fund atomicity or location atomicity during request execution. QuarkShard also enhances the security of blockchain sharding systems against MEV attacks and flooding attacks. Empirical evaluation across a wide-area network spanning four AWS regions demonstrates that QuarkShard achieves superior performance, attaining a peak throughput of $1024$k requests per second with sub-$4$-second latency. Benchmark comparisons show that QuarkShard achieves up to $210.7\%$ and $314.8\%$ of the maximum throughputs of Kronos and 2PC, respectively.

  匹配依据：MPC: 2pc (context)

  </details>

- **Structural Cryptanalysis of the Eevee AEAD Family**
  2026-10-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2496)
  Shuping Mao, Peng Wang, Jiadong Han, Tingting Guo, Yan Jia, Ying Chen

  <details><summary>摘要 / Abstract</summary>

  Eevee is a family of three AEAD modes, Umbreon, Jolteon, and Espeon, proposed at CCS 2023 for IoT-to-cloud secure computation. We analyze structural flaws in the algorithms of the supplied full-version specification and the proof steps underlying their online authenticated-encryption claims. An AD-free, two-encryption prefix distinguisher has advantage $1-2^{-n}$ in the ideal-forkcipher model, contradicting the specified online ideal object. Independently, the separable associated-data transform yields a four-encryption nonce-misuse distinguisher with advantage $1-2^{-n}$, a deterministic AD-only forgery, and nonempty-message forgeries obtained from cross-domain state differences. These attacks contradict the advertised nonce-misuse bounds of Umbreon and Espeon. With nonce-respecting encryption queries, one two-block Jolteon encryption permits a fresh one-block forgery with the same tag, while Espeon&#x27;s short-message path permits arbitrary AD substitution. We trace these counterexamples to failures of online-prefix consistency, conditional transcript distributions, domain separation, and checksum freshness in the original proof. The authenticity attacks follow from deterministic identities, and the privacy counterexamples persist with an ideal forkcipher. We derive corresponding requirements for AD processing and message finalization, and briefly summarize supporting checks of the published C routines. The central failures concern the mode design and cannot be resolved solely by correcting implementation encodings.

  匹配依据：MPC: secure computation

  </details>

- **SMT-Boosted Security Types and Correctness for Low-Level MPC**
  2026-10-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.22047)
  Christian Skalka, Steven Baldasty, Yeonhee Yeh, Felix Walberg, Joseph P. Near

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation (MPC) is an important enabling technology for data privacy in modern distributed applications. We develop a new Hoare logic and type theory to automatically enforce correctness, confidentiality, and integrity properties of protocols written in the Prelude/Overture language framework. Both definition and automation of our analyses leverages SMT verification, supporting precision and efficiency. Our approach is compositional, scalable, and generalizes to arbitrary prime fields and secret sharing schemes.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Robust ECDSA Threshold Signing at Scale**
  2026-10-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2493)
  Carsten Baum, Anders Dalskov

  <details><summary>摘要 / Abstract</summary>

  This work presents an efficient, scalable, and robust threshold ECDSA signing protocol for the $t\leq (n-1)/3$ scenario, making it suitable for e.g., bridging consensus from one Blockchain to another. Our construction allows to batch-compute pre-processing material for efficient online signing. While our protocol is based on established ideas for (Verifiable) Secret Sharing, we optimize it to scale efficiently both in terms of computation and communication with a large number of signers. We therefore combine efficient batching techniques for sharing (Fitzi &amp; Hirt, PODC 2006), randomness extraction (Beerliova-Trubiniova &amp; Hirt, TCC 2008) and share opening (Damgård &amp; Nielsen, CRYPTO 2007) with recent advances in efficient Zero-Knowledge proofs (Attema &amp; Cramer, CRYPTO 2020). We implement and evaluate the protocol experimentally and show that it is practical for large number of parties $n$.

  匹配依据：MPC: secret sharing

  </details>

- **On the Complexity of Symmetric Boolean Functions in Multiparty Private Simultaneous Messages**
  2026-10-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.21216)
  Marshall Ball, Peter Crawford-Kahrl, Vladimir Podolskii, Morgan Prior

  <details><summary>摘要 / Abstract</summary>

  Multiparty Private Simultaneous Messages (PSM), also known as Decomposable Randomized Encoding (DRE) or information-theoretic garbling, is a model for non-interactive secure computation. Each party encodes its input using shared randomness and sends a message to an evaluator who does not know that randomness. The evaluator must recover the function output without learning anything else about the inputs. Perfect privacy requires identical transcript distributions on inputs with the same output. We also study the weaker notion of support privacy, which requires only that these distributions have the same support. We study the communication complexity of symmetric Boolean functions when each of the $n$ parties holds one input bit. Lower bounds. We prove a superlinear lower bound for support-private PSM protocols computing $OR_n$. Our technique gives $Ω(n\log n)$ lower bounds for $MAJ_n$ and $EMAJ_n$ (with even $n$), and an $Ω(n\log q)$ lower bound for $MOD_q$ when $q\leq(1-c)n$ for a fixed constant $c&gt;0$. Upper bounds. We construct perfectly private PSM protocols of total communication $\widetilde{O}(n^{3/2})$ for every symmetric Boolean function, improving on the known quadratic bound. For $MAJ_n$, known branching-program constructions yield an upper bound of $O(n\log^3 n\log\log n)$. For $EMAJ_n$ and $MOD_q$ with prime $q$, the lower bounds are tight up to constant factors in the stated regimes. Under support privacy, we obtain $\widetilde{O}(n)$ communication for every symmetric Boolean function. Earlier lower-bound techniques of Ball et al. (ITCS 2020) yield only trivial linear bounds for symmetric Boolean functions. Concurrent and independent work by Holmgren and Wu proves a $ω(n)$ lower bound for $OR_n$ using the same combinatorial core. Both works used AI assistance.

  匹配依据：MPC: secure computation

  </details>

- **NOMAI: Scalable Federated Learning with Private Weights**
  2026-10-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.21059)
  Yiyi Sun, Mushtari Sadia, Amrita Roy Chowdhury

  <details><summary>摘要 / Abstract</summary>

  The twin goals of privacy-preserving federated learning (FL) -- harnessing distributed data while protecting the parties who contribute it -- demands three properties: model privacy, data privacy, and integrity. Achieving all three in a realistic deployment -- with a single coordinator and millions of users -- remains an open challenge that prior work has yet to fully resolve. We present NOMAI, the first scalable MPC-based FL system to provide all three guarantees simultaneously. NOMAI operates under an honest-majority assumption in the semi-honest model, with an extension to the malicious-with-abort setting. At its core, NOMAI combines a multi-committee MPC architecture with packed Shamir secret sharing, enabling SIMD-style secure computation that scales far beyond what monolithic n-party protocols can support. We further introduce ML-aware optimizations and new cryptographic primitives that substantially reduce per-user overhead. Our evaluation shows NOMAI is practically deployable at unprecedented scale: it reduces per-user computation to just &lt;350 ms (semi-honest) and &lt;700 ms (malicious) for per iteration of training MNIST, achieving three orders-of-magnitude improvements over prior work while seamlessly supporting populations of over 106 users. This demonstrates, for the first time, that MPC-based FL can meet the scale demands of real-world systems without compromising on privacy or integrity.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Coefficient choice in Galois-ring lifts of APN permutations: sharp unit-direction spectra and one-term optimal lifts**
  2026-10-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.21178)
  Hiroki Fukui

  <details><summary>摘要 / Abstract</summary>

  Permutation polynomials over the Galois ring $\mathrm{GR}(2^k,m)$ are nonlinear components for symmetric primitives that add keys in the ring, as in secure computation modulo $2^k$. Rønjom and Sandrib showed that their differential uniformity is at least $2q^{k-1}$, where $q=2^m$. For the class studied here it is attained on top-layer differences, while almost all differences are units. We ask how small the difference table can be on unit differences when the residue permutation is fixed and only higher coefficient digits of its lift are chosen. Let $m\ge5$ be odd, $k\ge3$, and let $p$ be a reduced quadratic almost perfect nonlinear (APN) permutation of $\mathbb{F}_q$ whose derivative is nowhere zero and two-to-one. Over all lifts of $p$, the least possible maximum on unit differences is $q$ or $2q$, decided by two invariants of $p$ and the level $k$. We describe every lift attaining it and show that the coefficients modulo $8$ decide optimality at every level. For every odd $m\ge5$, residue permutations with at most $16$ monomials attain $q$ after one $2$-adic digit of one coefficient of the natural lift is changed. For an explicit infinite family, one added monomial lowers the maximum on unit differences from $4q$, or from at least $q^2$, to $2q$ at every level without raising the degree. Under a uniform starting state and independent uniform round keys, valuation preservation yields layerwise bounds for characteristics and two-round differentials that distinguish lifts with the same global uniformity. Core results are formalized in Lean 4.

  匹配依据：MPC: secure computation

  </details>

- **Secret Sharing from Non-Extractable Randomness**
  2026-10-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.20173) · [IACR ePrint](https://eprint.iacr.org/2026/2477)
  Divesh Aggarwal

  <details><summary>摘要 / Abstract</summary>

  Bosley and Dodis (TCC 2007) proved that a class of imperfect randomness sources that suffices for information-theoretic encryption of messages longer than the logarithm of the key length must admit deterministic extraction of nearly uniform bits, and asked whether the same is true of two-out-of-two secret sharing. Aggarwal, Chung, Obremski, and Ribeiro (TCC 2022) gave a positive answer for schemes that are in addition leakage-resilient or non-malleable; the original question remained open. We answer it in the negative. For every $b\ge2$ we construct a class of flat sources on $\{0,1\}^{b+2}$, each of min-entropy at least $b$, together with a perfectly correct and perfectly private two-out-of-two scheme that shares a $b$-bit secret into two $(b+1)$-bit shares using any source in the class, and we show that every deterministic map from $\{0,1\}^{b+2}$ to $\{0,1\}$ is at statistical distance at least $1/6$ from uniform on some source in the class. This implies that sharing a long enough secret does not require extractable randomness. The proof is a short parity argument. The idea of the construction extends to other thresholds: for two-out-of-$n$ and $r$-out-of-$r$ sharing we give perfect schemes with $(b+1)$-bit shares, private for classes of flat sources from which no single bit can be extracted with error below $1/(4n-2)$ and $1/(2(2^r-1))$, respectively.

  匹配依据：MPC: secret sharing

  </details>

- **Heterogeneous CPU–NPU Implementation of the AIMer Post-Quantum Signature for Low Latency on a Mobile SoC**
  2026-10-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2486)
  Myoungsu Shin, Jihoon Jang, Hanbeom Shin, Insung Kim, Dongjae Lee, Donggeun Kwon

  <details><summary>摘要 / Abstract</summary>

  Signatures in the MPC-in-the-head paradigm rest only on a symmetric primitive, but their signing is slow, because it computes hash functions and a linear map for every simulated party of every repetition. We show that the Hexagon NPU of Snapdragon SoCs shortens one complete signing operation of AIMer, the MPC-in- the-head signature that the Korean post-quantum cryptography competition selected. Prior work speeds up such signatures on one CPU core, accelerates post-quantum arithmetic on GPUs for batches of operations, and reports only single post-quantum functions for mobile NPUs. Our implementation divides each signing operation along its dependency graph. The NPU computes the hashing and the per-party linear map of the last repetitions, which need no secret key, and the CPU keeps the secret key and the two hashes that absorb the repetitions in index order. A fast AArch64 implementation serves both as the CPU part and as the baseline, and it signs 4.5 to 6.1 times faster than the reference implementation on one core. On a Snapdragon 8 Gen 3 tablet, one core with the NPU signs 1.30 to 1.42 times faster than two cores and 1.74 to 1.97 times faster than one core for the three short-signature parameter sets. The same configuration uses 13 to 27 % less energy per signing operation than two cores. On Snapdragon 8 Elite and 8 Gen 2 phones, one core with the NPU signs 1.28 to 1.35 and 1.74 to 1.82 times faster than two cores.

  匹配依据：MPC: mpc (context)

  </details>

- **Edabits Generation with Quasi-Linear Communication Complexity**
  2026-10-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2482)
  Alexander Bienstock, Daniel Escudero, Qijia Fan, Fengrun Liu, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  The work of (Escudero et al., CRYPTO 2020) introduces the so-called edabits, which are defined as a secret sharing of an integer over an arithmetic domain, together with its bit decomposition secret shared over a binary domain. In the same work, it is shown how edabits can be used to securely evaluate advanced primitives such as comparison, bit decomposition, and truncation, which are essential building blocks in more complex applications such as privacy-preserving machine learning and beyond. Edabits are general and can be defined over any secret-sharing scheme or corruption model. Such flexibility, coupled with their wide range of applications, makes edabits a powerful target correlation. Escudero et al.~introduced a protocol to generate edabits that works in the arithmetic black-box (ABB) model, that is, it is agnostic to the concrete secret-sharing scheme and even works both for fields $\mathbb{F}_p$ and rings $\mathbb{Z}_{2^\ell}$, as well as both for honest majority $t 0$. This includes the honest majority case $t&lt;n/2$, but also dishonest majority with an (arbitrarily small) constant fraction of honest parties. Our result is achieved via novel applications of randomness extraction methods, as well as better edabit aggregation for the binary components. Along the way and of independent interest, we improve the communication complexity of dabit generation (dabits are bits shared in both binary and arithmetic domains) from $\Omega(n^2\ell)$ bits achieved in (Rotaru and Wood, INDOCRYPT 2019), to linear $O(n\ell)$ bits.

  匹配依据：MPC: secret sharing

  </details>

- **On Secure Sorting and Its Application to Privacy-Preserving Graph Pattern Matching**
  2026-10-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2457)
  Marcel Keller

  <details><summary>摘要 / Abstract</summary>

  Sorting in secure computation has been studied almost as long as there have been implementations of multi-party computation (Wang et al., AsiaCCS&#x27;10). More recent advances include completely secure implementations (revealing nothing other than the list size) that have used Quicksort (Araki et al., CCS&#x27;21) and radix sort (Asharov et al., CCS&#x27;22). For the first time, we extensively compare the two variants across a range of parameters and for both honest- and dishonest-majority computation. We then apply secure sorting to improve sparse matrix multiplication without oblivious RAM based on recent work by Damie et al. (CODASPY&#x27;26). Our main contribution here is to produce an output in the same format as the inputs to the multiplication. This is needed for repeated multiplication of graph adjacency matrices, which we use to find cycles in graphs. Such cycles have been associated with money laundering, and this also applies to another graph pattern dubbed scatter-gather, which we can detect with the same approach. Our work therefore can be applied to privacy-preserving anti-money laundering detection.

  匹配依据：MPC: multi party computation, secure computation

  </details>

- **Local Leakage Resilience of Shamir Secret Sharing: Below Half Threshold Rate**
  2026-10-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.17711) · [IACR ePrint](https://eprint.iacr.org/2026/2454)
  Hai H. Nguyen

  <details><summary>摘要 / Abstract</summary>

  We study the local leakage resilience of Shamir secret sharing, where an adversary leaks a bounded number of bits from every share. For $n$ parties and reconstruction threshold $k$ over a prime field $\mathbb{F}_p$ with $p&gt;n$, we prove the following. (1) There is an absolute constant $c_{\mathrm{bh}} 0$ and $k\ge cn$, Shamir sharing is resilient to quadratic-residue leakage and to almost all local leakage functions of up to $η_c\log_2 p$ bits, for a constant $η_c&gt;0$. All three results follow from one analytic framework, which we develop for generalized Reed--Solomon codes: local leakage from a uniform codeword is statistically close to the same leakage from independent uniform field elements. The framework expresses the leakage distance as the norm of a function on the leakage outputs. The Efron--Stein decomposition splits this function into orthogonal components indexed by supports of dual codewords. Two tools bound the components: list recovery of the dual code, which is ordinary list decoding for one-bit leakage, and a generalized von Neumann inequality for MDS systems of linear forms that retains linearly many Gowers norms. The first tool gives the result above half, the second gives the constant-rate result, and applying both to different ranges of supports in the same decomposition gives the result below half.

  匹配依据：MPC: secret sharing

  </details>

- **HULK: An Efficient Algorithm for Enabling Fast Bulk Bitwise Operations on Homomorphically Encrypted Data**
  2026-10-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.18391)
  Mayank Kabra, Phillip Widdowson, Harshita Gupta, Rakesh Nadig, Nisa Bostancı, Eirini Tzermpou, Rakesh Kumar, Spiros Galanopoulos, Ataberk Olgun, Abdullah Giray Yağlıkçı, Mohammad Sadrosadati, Onur Mutlu

  <details><summary>摘要 / Abstract</summary>

  A wide range of important cloud applications, e.g., database analytics, graph analytics, and genome analysis, spend a considerable amount of time performing bulk bitwise operations (e.g., AND, OR, XOR). These applications often operate on highly sensitive data, making data privacy a critical concern. Homomorphic encryption (HE) enables secure computation on encrypted data without requiring decryption, ensuring privacy in untrusted and shared environments. We analyze 13 end-to-end applications across three domains (healthcare, graph, and database analytics) and observe that bulk bitwise operations take 62-100% of the execution time of the healthcare and graph workloads. The key problem is that existing HE approaches perform them with high-latency homomorphic operations (e.g., multiplication or lookup tables) and significantly increase the data size. Our goal is to enable fast bulk bitwise operations on homomorphically encrypted data by designing an efficient HE algorithm that reduces the use of these costly operations. To this end, we propose HULK, which performs two key steps: (1) it constructs bulk bitwise operations using low-cost homomorphic additions, which compute the Hamming weight of the encrypted operand bits in every slot of a packed ciphertext without any homomorphic multiplication, and (2) it decodes the result of an AND, OR, or XOR from the Hamming weight with a single indicator polynomial, keeping the result in the standard encoding. Across 13 end-to-end applications in healthcare, graph, and database analytics, HULK improves performance over the arithmetic approach used by prior works by up to 7.26x (CPU) and 6.65x (GPU), and on average by 2.32x/1.78x/1.45x (CPU) and 2.08x/1.70x/1.51x (GPU) for healthcare/graph/database analytics. When we increase the reduction depth in a representative application, HULK&#x27;s speedup grows to 10.10x over the state-of-the-art GPU baseline.

  匹配依据：MPC: secure computation

  </details>

- **Think Locally Before Computing Jointly: Efficient Secure Multi-Party Computation via Maximizing Local Processing**
  2026-10-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.17072)
  Mingfei Yu, Chenglu Jin, Giovanni De Micheli

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) lets parties evaluate a function over private inputs without revealing them. In garbled-circuit (GC) protocols, prior optimization has largely treated the number of non-linear gates, especially AND gates, as a proxy for cryptographic cost, and has focused on minimizing multiplicative complexity. We identify an orthogonal source of savings: a gate need not be garbled when one party knows or can locally compute its inputs; that party can evaluate it outside the secure protocol, even when the gate is non-linear. We introduce ownership-aware optimization for GC-based MPC, which minimizes non-linear gates requiring joint evaluation rather than total non-linear gates. We formalize this objective in a cost model and implement a compiler-integrated, gate-level framework that restructures Boolean circuits to increase party-local computation while preserving secure-computation semantics. The method is automated and general-purpose, and composes with existing multiplicative-complexity optimization. Experiments show that it reduces jointly evaluated computation and improves end-to-end GC performance on circuits with party-local structure, revealing protocol-cost savings missed by conventional GC cost models.

  匹配依据：MPC: garbled circuit, secure computation, secure multi party computation

  </details>

- **Modulus Operandi: Round-Optimal Modulus Conversion for MPC and Threshold FHE**
  2026-10-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2450)
  Ivan Damgård, Sebastian Hasler, Sebastian Kolby, Stanislas Pawlak

  <details><summary>摘要 / Abstract</summary>

  In secure multiparty computation (MPC), modulus conversion turns a sharing of a value $x$ modulo $q$ into a sharing of the same value modulo $t$, without leaking anything about $x$. One important application of modulus conversion is in threshold decryption for lattice-based cryptosystems, where a sharing modulo the ciphertext modulus has to be moved to the plaintext modulus before it can be opened. The most efficient protocols so far (Damgård et al., Asiacrypt 2026) are in the preprocessing model, assume $x$ is bounded away from $q$ by a constant factor and take two rounds for a prime target modulus, three rounds for arbitrary moduli, and one round when all moduli are 2-powers. We improve upon this by constructing three new modulus conversion protocols in the preprocessing model: - Our first conversion protocol takes a single round for arbitrary moduli, consisting of just one opening. - Our second conversion protocol is a variant of the first protocol, where in the preprocessing most of the secure multiplications are replaced by private inputs, which are checked in a batch using fully linear interactive oracle proofs (FLIOPs). This makes the preprocessing cheaper (amortized over a batch of conversions) when the number $N$ of parties is small. This comes at the cost of making the bound on $x$ a factor $N$ stronger. - Our third conversion protocol avoids the bound on $x$ altogether but takes two rounds. All our protocols are stated in the arithmetic black box (ABB) model, so they can run on top of a wide variety of MPC protocols, inheriting their corruption threshold and security model. To allow the third conversion protocol to run in two rounds, we construct the first one-round comparison protocol in the ABB model for comparing a bitwise shared $n$-bit value against a public threshold with polynomial-size preprocessing. Concretely, the preprocessing size is $\mathcal O(n^2)$ in general, and $\mathcal O(n^2 / \log n)$ in our case where the secret value is fixed in preprocessing. We also construct constant-round ABB protocols without preprocessing for computing symmetric functions and comparisons of values shared bitwise modulo powers of arbitrary primes (e.g., $2^k$), at communication quasi-linear in the number of input bits. Previously, this required either a sufficiently large prime or polynomially larger communication. Finally, we give an impossibility result for non-interactive modulus conversion, demonstrating that a single round is optimal: unless $t$ divides $q$, every non-interactive conversion for inputs $x &lt; q/\beta$ is incorrect with probability at least $\approx 1/(4\beta)$.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Verifiable Computation on Encrypted Data from Homomorphic Encryption over Random Encodings**
  2026-10-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2422)
  Jiayi Kang, Erik Pohle, Jannik Spiessens

  <details><summary>摘要 / Abstract</summary>

  Verifiable Computation on Encrypted Data (vCOED) enables clients to outsource computation while providing both privacy and integrity. A promising vCOED paradigm is blind proofs, which use homomorphic encryption (HE) to evaluate verifiable computation (VC) proofs on encrypted data. Despite their efficiency, blind proofs do not provide strong client privacy: a malicious server can exploit reaction attacks to learn information about the client&#x27;s inputs, intermediate values or final outputs. Our work addresses this limitation by introducing Homomorphic Encryption over Random Encodings (HERE). We formalize a new security notion, indistinguishability under chosen-plaintext attacks in the presence of an equality oracle over encodings (IND-CPA-E). We prove that combining IND-CPA-E-secure HERE schemes with blind proofs that verify computation over the encodings yields vCOED protocols with strong client privacy. We then instantiate a HERE scheme for functions of bounded degree $d$, using Shamir secret sharing at $(d+1)$ evaluation points under $(d+1)$ distinct HE keys. Finally, we demonstrate the concrete efficiency of our approach through an application to matrix-vector multiplication (MVM), a linear computation corresponding to $d=1$. The proof overhead (i.e. the ratio of the vCOED prover runtime to the homomorphic MVM runtime) in our combined vCOED protocol is as low as $2\times$, as demonstrated in our prototype implementation.

  匹配依据：MPC: secret sharing

  </details>

- **Lattice Bingo: Asynchrony and One-Shot Adaptivity in Verifiable Secret Sharing via Erasure Code Commitments**
  2026-10-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2432)
  Ittai Abraham, Aniket Kate, Aditi Partap, Ertem Nusret Tas

  <details><summary>摘要 / Abstract</summary>

  Asynchronous verifiable secret sharing (AVSS) allows a dealer to distribute a secret among parties while preserving privacy and consistent reconstruction, despite Byzantine faults and arbitrary message delays. It is a fundamental building block for Byzantine agreement, distributed key generation, and secure multiparty computation. Packed AVSS protocols share many secrets together to reduce communication per secret. The best known AVSS protocols achieve quadratic communication while sharing linearly many secrets. In particular, Bingo (Abraham et al., CRYPTO 2023) shares a batch of $\Theta(k)$ secrets among $k$ parties using $O(\lambda k^2)$ words of communication, while also achieving adaptive security, but relies on assumptions that are not post-quantum secure. Known post-quantum alternatives have higher worst-case communication for comparable batch sizes or require substantially larger batches to achieve linear amortized communication. We present Lattice Bingo, a lattice-based packed AVSS protocol with quadratic communication and linear packing. For every constant $\epsilon&gt;0$, it shares $\Theta(k)$ secrets among $k\geq(3+\epsilon)f$ parties, tolerates $f$ Byzantine parties, and uses $O(k^2\operatorname{poly}(\lambda))$ words of communication. It additionally achieves one-shot adaptive secrecy: the adversary may adaptively choose its corruption and reconstruction requests based on the public transcript observed so far, but must submit these requests together in a single batch. Our main technical contribution is a commitment scheme for two-dimensional linear codes based on the PowerBASIS assumption. We combine PowerBASIS commitments with the linear code based secret sharing of Applebaum, Nir, and Pinkas, replacing the Reed–Solomon encoding and KZG commitments used in Bingo. Our commitment supports proof interpolation, enabling parties to recover missing shares and their opening proofs. It additionally achieves a notion that we call one-shot simulation hiding. Together, these properties allow us to adapt Bingo’s framework to obtain Lattice Bingo with the same efficiency and one-shot adaptive security.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **The Power of Multislices in Monotone Computation**
  2026-10-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2415)
  Amos Beimel, Oded Nir

  <details><summary>摘要 / Abstract</summary>

  Motivated by recent constructions and barriers in secret sharing, we study multislice functions. These functions, parametrized by a width parameter $w$, take the value 0 on inputs of Hamming weight below a base value $k$, 1 on inputs of weight above $k+w$, and are monotone in between. We first investigate formulas over multislice gates, which generalize the formulas over slices model (Applebaum et al., TOCT 2026). We prove that, although multislices compute complicated functions, they do not help in computing the worst-case function when $w\ll n$; that is, there is an explicit monotone function such that for every $w$, every formula over multislice gates of width $w$ that computes it, regardless of its depth and gate fan-in, has size $2^{\Omega\left(n/((w+1)\log^2 n)\right)}$. Our lower bound is based on a randomized Karchmer-Wigderson protocol for multislices that can be amortized across the formula. As a complementary result, we show how to realize multislices using slice gates, i.e., multislice gates of width 0; the construction uses a simple peeling recursion. Consequently, every width-$w$ multislice on $n$ variables has a formula over slice gates of size at most $2n^{w+1}$ and depth $(w+1)$. The same construction allows to compute multislices with small monotone real formulas and circuits, two models introduced by Pudl\&#x27;ak (J. Symb. Log., 1997) in the context of proof complexity. This result also has an application to secret sharing: it yields, for sufficiently long secrets, multilinear secret-sharing schemes for width-$w$ multislices with maximal information ratio $n^{O(w+1)}$, which is polynomial for every fixed $w$. In addition, we prove that an explicit access structure requires shares of size $2^{\Omega(n)}$ in every secret-sharing scheme from a family of schemes that captures all currently known constructions for general access structures with share size $2^{cn+o(n)}$, for $c&lt;1$. Our proof goes through an exponential lower bound on the size of formulas over so-called CDS gates and ideal linear gates.

  匹配依据：MPC: secret sharing

  </details>

- **Mercury: Fuzzy Private Set Intersection with Communication and Computation Logarithmic in the Threshold**
  2026-10-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2409)
  Qi Liu, Kang Yang, Binwu Xiang, Xiaojie Guo, Cheng Hong, Yu Yu

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection (PSI) allows two mutually distrusting parties to compute the intersection of their sets without revealing any additional information and has found numerous applications. The approximate matching required by various applications has led to the development of Fuzzy PSI (FPSI), a variant of PSI that identifies approximate intersection elements under a public distance threshold \(\delta\). Reducing computation and communication costs remains an important challenge for FPSI. In this paper, we present a new FPSI protocol, called Mercury, which achieves logarithmic computation and communication complexity with respect to threshold \(\delta\). Our protocol exploits the correlation of the intersection and the point pairs held by the parties, and efficiently identifies the neighboring point pairs by a mixed protocol from homomorphic encryption and secure two-party computation using a &quot;mask-then-compare&quot; technique. We implemented Mercury and evaluated both its sender-private and standard FPSI variants. For balanced two-dimensional inputs, Mercury-SP achieves \(9.0\sim63.9\times\) runtime speedups and reduces communication by a factor of \(8.7\sim26.1\) across the evaluated thresholds and set sizes in the LAN setting, compared to the FPSI protocol by Dang et al. (CCS&#x27;25). In the completed unbalanced experiments, Mercury-SP achieves \(55.7\sim132.4\times\) WAN runtime speedups compared to the FPSI protocol by Piske et al. (CCS&#x27;25).

  匹配依据：MPC: private set intersection, secure two party computation

  </details>

- **Individual Cryptography from Iterated Squaring**
  2026-10-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2418)
  Georg Fuchsbauer, Christoph U. Günther, Charlotte Hoffmann, Krzysztof Pietrzak, Fabian Regen

  <details><summary>摘要 / Abstract</summary>

  Individual cryptography (Dziembowski et al. Crypto&#x27;23) and complete knowledge (Kelkar et al. CCS&#x27;24) aim at constructing protocols that ensure that some individual party must know a secret value in the clear, and so the computation cannot have been “outsourced” to an MPC computation. Two central primitives are proofs of complete (or individual) knowledge, which enforce that some party actually knows the secret witness, and secret sharing with snitching, which enforces that whenever the secret is reconstructed, some party must learn a certificate of this fact. The instantiations proposed by both papers (Crypto&#x27;23 and CCS&#x27;24) ensure that to compute a proof or reconstruct the shared secret, a large number of hash function evaluations is necessary. Thus, at least one party must compute many of these “in the clear” (and not via MPC) and from the hash function inputs one can extract the secret (in the random oracle model). In practice, they suggest using Bitcoin mining hardware. Sequential proofs of complete knowledge have recently been proposed, which use proofs of sequential work to enforce that the hashes are performed sequentially. As a consequence, it suffices to require a much smaller number of hashes, and thus such primitives can be implemented on standard hardware. Unfortunately, this approach does not work for primitives like secret sharing, as one would need to efficiently sample the challenge for the sequential computation together with its solution. In this work, we leverage ideas from time-lock puzzles to overcome this issue. We construct secret sharing with snitching and encryption with self-incriminating proofs where reconstruction/decryption is sequential. The security of our scheme relies on a new knowledge assumption, which informally states that whenever parties that hold secret shares of an RSA modulus N=pq jointly compute 2^2^T N for some large T (too large to perform a sequential computation of length T in MPC), then at least one of them must have learned a multiple of N.

  匹配依据：MPC: secret sharing

  </details>

- **Improved Local Leakage Resilience of Shamir Secret Sharing and Worst-Case Optimal Polynomial Intersection**
  2026-10-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.12357)
  Yihang Sun, Mary Wootters

  <details><summary>摘要 / Abstract</summary>

  We study two problems: Local Leakage Resilience (LLR) for Shamir secret sharing, and worst-case Optimal Polynomial Intersection (OPI). Both problems concern polynomials $Q(X)$ of degree less than $k$, over a prime-order finite field $\mathbb{F}_p$. In LLR for Shamir secret sharing, one asks how much one can learn about $Q(0)$ given a few bits leaked from each of $Q(α_1), \ldots, Q(α_n)$, for distinct non-zero evaluation points $α_i \in \mathbb{F}_p$. In OPI, one is given input list $S_1, \ldots, S_n \subset \mathbb{F}_p$, and wants to find a polynomial $Q(X)$ of degree less than $k$ so that $Q(α_i) \in S_i$ for as many $i$ as possible. Leveraging recent connection between these two problems due to (Sun, Wootters 2026), we improve the state-of-the-art for both problems. For LLR, we show that there is some constant $δ&gt; 0$ so that, as long as $R := k/n \geq 1/2 - δ$, Shamir secret-sharing is one-bit locally leakage resilient (meaning that one can learn only a negligible amount about $Q(0)$). This is the first result to break the so-called &quot;one-half barrier&quot; for LLR, and improves over the previous best known result, requiring $R \geq 0.668$ (Kasser, 2025). For OPI, we give a quantum algorithm that finds a polynomial $Q(X)$ that agrees with at least a $\mathsf{SCL}_ρ(R)-\varepsilon$ fraction of the lists in expectation, for every fixed $\varepsilon&gt;0$, where $\mathsf{SCL}_ρ$ is the \emph{semicircle law} of (Jordan et al., 2025). This improves previous algorithmic (and existential) results of (Jo, 2026) and (Horinaga, Yamakawa, 2026). We also give further improved existential results. We also adapt the hardness result of (Yamakawa, Zhandry, 2024) to apply to OPI (rather than a folded version); over large fields, this gives an unconditional separation between the quantum and classical hardness of OPI relative to a membership oracle.

  匹配依据：MPC: secret sharing

  </details>

- **The Price of Privacy: Randomness Complexity of Graph-Based Multi-Secret Sharing**
  2026-10-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.10002) · [IACR ePrint](https://eprint.iacr.org/2026/2395)
  Piotr Marszalik

  <details><summary>摘要 / Abstract</summary>

  We study the randomness required to share possibly correlated secret bits among parties connected by a graph. A dealer places shares on the edges so that each party can recover its own secret from its incident shares and learn nothing about the others beyond what its own secret reveals. Anilkumar et al. completely determined the minimum randomness required for three binary secrets. We extend this study to four secrets and obtain results for arbitrary numbers of secrets on general graphs. For four parties on a complete graph, we determine the minimum number of random states for every set of permitted secret combinations: the possible values are one, two, three and four. We also characterize when one random bit suffices on an arbitrary graph.

  匹配依据：MPC: secret sharing

  </details>

- **The Geometry of Collusion Leakage in Inner-Product Functional Encryption**
  2026-10-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2404)
  Ferdinando Zullo

  <details><summary>摘要 / Abstract</summary>

  Inner-product functional encryption (IPFE) allows the holder of a functional key for a vector $y$ to learn $\langle x,y\rangle$ from an encryption of $x$, and nothing more. Keys, however, accumulate: a coalition holding sufficiently many independent keys recovers the plaintext. We model each institution by the span $W_i\leq\F_q^n$ of its authorized key vectors and show that a coalition $I$ determines the plaintext exactly modulo $(\sum_{i\in I}W_i)^\perp$; for a uniform plaintext it learns exactly $\dim\sum_{i\in I}W_i$ field symbols. The resulting leakage function is a representable and entropic polymatroid. We then study authorization spaces of dimension $r$ whose pairwise intersections have dimension at most $h$. We prove that some coalition of size $c\geq2$ always learns at least $\min\{n,2r-h+c-2\}$ dimensions, and we give a Vandermonde-type construction in which every coalition of size $c$ learns exactly this amount, for all $c$ simultaneously. Hence the largest achievable reconstruction threshold is $n-2r+h+2$, which gives an exact tradeoff between functional diversity and collusion resistance. The optimal configuration is a sunflower, an equidistant subspace code and a generalized arc; its orthogonal complements form a generalized dual arc, and for $r=1$ it reduces to Reed--Solomon secret sharing.

  匹配依据：MPC: secret sharing

  </details>

- **Round Optimal MPC With Provable Cheater Identification**
  2026-10-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2393)
  Yashvanth Kondi, Divya Ravi, Jure Sternad, Sophia Yakoubov

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation with provable identifiable selective abort (PISA), introduced by Kondi and Ravi (CCS 2025), guarantees that every honest party either obtains the computation output or a certificate that convinces any external auditor that a specific party cheated. Crucially, honest parties need not agree: some may get output while others receive evidence of cheating. In contrast, secure computation with identifiable abort (IA) requires just such unanimity; however, in the event that an honest party doesn&#x27;t get output, it need merely be able to point to a cheater - not to prove their guilt. Secure computation with IA classically requires broadcast. Kondi and Ravi demonstrated that secure computation with PISA, on the other hand, can be built over point-to-point channels alone. While PISA is feasible exactly when guaranteed output delivery is, i.e. for $t &lt; n / 2$, the best known construction over point-to-point channels requires six rounds. We settle the round complexity of PISA for all but a narrow band of thresholds. We prove that two rounds are impossible for $t \geq n /3$, even with arbitrary setup and computational assumptions; we give a three-round protocol for any $t &lt; n/2$, which is therefore round-optimal for $n / 3 \leq t &lt; n/2$; and we give a two-round protocol for $t &lt; n/4$. The two-round protocol introduces a new primitive called one-or-nothing secret sharing with omissions.

  匹配依据：MPC: secret sharing, secure computation, secure multiparty computation

  </details>

- **Practical and Efficient MPC from FHE, without ZKPoKs**
  2026-10-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2403)
  Kelong Cong, Nigel P. Smart, Titouan Tanguy, MIchael Walter

  <details><summary>摘要 / Abstract</summary>

  Fully Homomorphic Encryption (FHE) enables one to implement low-round and low-communication complexity Multi-Party Computation (MPC) which is secure in the static malicious corruption model. By expanding on an idea presented in the full version of the FHE-based MPC protocol of Smart (IMA, 2023), we show how to completely remove the need for Zero-Knowledge Proofs-of-Knowledge in that protocol. This simplification makes the final security proof of the MPC protocol much simpler, and more modular. The new protocol makes use of an FHE scheme with an encrypted PRF functionality, and in addition to our main result we formalize the security of such encrypted PRFs and prove the construction of Deo et al. (CCS 2025) secure in this model.

  匹配依据：MPC: multi party computation

  </details>

- **Mixed States in Quantum Rabin Oblivious Transfer**
  2026-10-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.09796)
  James T. Peat, Lara Stroh, Kenny Campbell, Erika Andersson

  <details><summary>摘要 / Abstract</summary>

  Oblivious transfer (OT) is a fundamental cryptographic primitive that is useful for realizing any two-party computation. Since information-theoretically secure perfect OT is impossible classically and quantumly, research has focused on imperfect protocols, exploring how close to perfect one can get against unbounded dishonest parties. While current approaches often make use of pure quantum states, recent work suggests that mixed quantum states may improve performance. In this paper, we investigate the use of mixed quantum states in Rabin oblivious transfer, where a sender holds one bit and a receiver learns its value with a certain probability while the sender remains ignorant of whether the receiver learned it. We present three mixed-state protocols constructed with two distinct methods, extending an existing pure-state scheme and employing a probabilistic approach, and demonstrate improved performance compared to classical and quantum pure-state protocols across varying parameters.

  匹配依据：MPC: oblivious transfer, two party computation

  </details>

- **Fair and Efficient Helper-Aided MPC with Cheater Identification**
  2026-10-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2392)
  Maximilian Kamps, Protik Paul, Divya Ravi

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) enables privacy-preserving tasks such as auctions and voting. In practice, more than half of the parties may collude, making security against a dishonest majority desirable. Unfortunately, dishonest-majority MPC suffers from high communication and can achieve only abort security. For instance, in an auction, an adversary may abort after learning the outcome and rerun the protocol with a higher bid. Helper-aided MPC mitigates these limitations by introducing a semi-honest, non-colluding helper, a model that naturally fits settings with a central governing or coordinating entity and provides strong guarantees even when up to $n-1$ parties are malicious. The model assumes that the adversary can either semi-honestly corrupt the helper or maliciously corrupt up to $n-1$ parties (excluding the helper). While existing helper-aided protocols are fair i.e. either all parties receive the output or none do; they still allow the adversary to abort without any penalty and deny output to all parties. This behavior is undesirable in practice, as parties may incur the cost of computation without receiving the output. In this work, we design efficient helper-aided MPC protocols that achieve identifiable fairness: either all parties obtain the output, or—if an abort occurs—no party receives the output, and the honest parties identify at least one common cheater. We propose two protocols, $\mathsf{Alhena}$ for synchronous networks and $\mathsf{Wasat}$ for asynchronous networks which provide the stronger guarantee of identifiable fairness compared to the state-of-the-art fair protocols $\mathsf{Asterisk}$ (Kamarkar et al. IEEE S&amp;P 2024) and $\mathsf{Castor}$ (Kamarkar et al. IEEE S&amp;P 2026) in the respective network settings. Our experiments show that, in the online phase, $\mathsf{Alhena}$ and $\mathsf{Wasat}$ achieves speedups of $4-12.5\times$ and $2.5-5\times$ over $\mathsf{Asterisk}$ and $\mathsf{Castor}$ respectively. Furthermore, in the preprocessing phase, $\mathsf{Wasat}$ exhibits speedup of $\approx 3\times$ over $\mathsf{Castor}$. Notably, our protocols are designed in such a way that the online performance remains unaffected by active misbehaviour.

  匹配依据：MPC: secure multi party computation

  </details>

- **Collusion-Secure Semi-Quantum Secret Sharing Scheme using a Quantum Third Party**
  2026-10-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.10176)
  Santanu Majhi, Nirupam Basak

  <details><summary>摘要 / Abstract</summary>

  The security of a secret sharing protocol is compromised if one or more dishonest participants can reconstruct the secret by deviating from the prescribed protocol, particularly when such malicious behavior remains undetected. Semi-Quantum Secret Sharing (SQSS) is a variant of secret sharing in which the participants possess only classical capabilities, such as preparing and measuring qubits in the computational ($Z$) basis, while a quantum-capable third party assists the dealer in generating and distributing quantum shares of a classical secret. The limited quantum capabilities of the participants in SQSS protocols may introduce vulnerabilities to collusion attacks, enabling an assisting quantum third party, in collaboration with a dishonest classical participant, to jointly recover the secret even without detection. In this work, we propose a novel SQSS protocol that eliminates this vulnerability and achieves information-theoretic security against collusion attacks. We further prove that the proposed protocol is secure against a broad class of external and internal attacks. Finally, a comparative analysis demonstrates that our construction advances existing SQSS protocols by simultaneously optimizing qubit efficiency, involves a classical dealer, and resilience against DCNA attacks using basic Bell states.

  匹配依据：MPC: secret sharing

  </details>

- **Truffle: Maliciously Secure Three-Party Shuffles with Applications to Parsing**
  2026-10-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2376)
  Nidhish Bhimrajka, Yashvanth Kondi, Daniel Noble, Bhavish Raj Gopal

  <details><summary>摘要 / Abstract</summary>

  Deploying Secure Multiparty Computation (MPC) to operate on data from real world sources requires many connective elements that have not received much attention in the literature. One prominent example is that MPC protocols typically assume conveniently structured data, whereas data in the real world comes in formats that are meant to be handled by string parsing engines. In this work, we give a new constant round protocol for securely parsing secret shared strings into an MPC-friendly format, built upon secure shuffle as a key primitive. Secure shuffle applies a permutation to a list while keeping both the permutation and the underlying data secret-shared at all times. While highly efficient protocols exist in the semi-honest setting, achieving malicious security has incurred significant overhead in both rounds and communication. We present Truffle, a new three-party shuffle protocol that is secure against one active corruption to bridge this gap. Truffle achieves an amortised round complexity that for the first time matches the state-of-the-art semi-honest protocol, while incurring only sublinear communication overhead. The core technique that underlies Truffle is a novel distributed verifier zero-knowledge proof that checks the correctness of a putative shuffle. We implement Truffle and show via benchmarks that it is performant enough to handle real application data. Beyond parsing secret shared data, secure shuffle finds applications in graph analytics, anonymous communication, Distributed Oblivious RAM, aggregate statistics, and secure sorting, each of which stand to benefit from the improvement that Truffle provides.

  匹配依据：MPC: secure multiparty computation

  </details>

- **The Post-Quantum Cost of Garbled-Circuit Bitcoin Bridges**
  2026-10-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2383)
  Mukesh Tiwari, Aaron Feickert

  <details><summary>摘要 / Abstract</summary>

  Recent Bitcoin bridge designs rely on verification of succinct proofs to process withdrawals. This requires off-chain garbled circuit evaluation of a succinct proof, the input labels for which must be encoded on chain in a manner compatible with malicious security. We assess the post-quantum vulnerability of these cryptographic components, and examine the costs of secure alternatives. Circuit sizes for post-quantum proving systems can be made smaller than the current pairing-based baseline, but at the cost of significantly higher proof sizes that incur greater cost and require multiple Bitcoin blocks to encode. We suggest avenues of future research to improve efficiency of proofs, circuit representations, and input encodings.

  匹配依据：MPC: garbled circuit

  </details>

- **Runaway Reaction: When Benign Skills Compose into Malicious Behavior**
  2026-10-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.05943)
  Zunlong Zhou, Ziyuan Yang, Mengyu Sun, Yi Zhang

  <details><summary>摘要 / Abstract</summary>

  Agent skills package task-specific knowledge and procedures that can be composed to support complex agent tasks, while public marketplaces provide a growing pool of reusable skills. Existing security vetting, however, largely evaluates skills in isolation, leaving composition-induced risks underexplored. Such risks arise because composing benign skills expands the agent&#x27;s capability space, enabling behaviors unavailable to any skill alone. Interestingly, we find that directly composing benign skills can already induce malicious behaviors, even when every individual skill passes security vetting. We further find that some target malicious behaviors remain difficult to realize through direct composition, even when the selected skills collectively provide the required capabilities. To systematically instantiate these attacks, we present Compositional Risk Induction via Multi skill Execution (CRIME). CRIME first uses the Malicious Plot Casting (MPC) module to decompose a target malicious behavior into complementary requirements and identify suitable benign skill compositions from public skill repositories. For compositions that cannot directly realize the target behavior, the Runaway Reaction Steering (RRS) module uses execution feedback to iteratively refine the selected skills toward the target while requiring each skill to remain benign under standalone vetting. The resulting composition is then passed to the Skill Reaction Chamber (SRC) module, where the skill pair is executed in a sandbox and the resulting environmental consequences are examined to determine whether the target behavior has occurred. Unsuccessful cases are returned to RRS for further refinement. Furthermore, we construct a benchmark of 4,000 public skills across eight cybersecurity behaviors for systematic evaluation of composition-induced vulnerabilities.

  匹配依据：MPC: mpc (context)

  </details>

- **Quantum Leakage from Shamir Sharing with Correlated Resources**
  2026-10-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.06350)
  Isaac Barouch Essayag, Aryeh Lev Zabokritskiy

  <details><summary>摘要 / Abstract</summary>

  We study leakage from Shamir secret sharing when each device uses its share to produce one qubit from an initial quantum resource independent of the secret and sharing randomness. We prove exponentially small trace distance between the leakage states of any two secrets, when reconstruction requires a sufficiently large fraction of the shares, for fixed stationary chains satisfying an upper operator mixing condition and for resources generated by fixed finite quantum memories with primitive transfer channels. These guarantees permit arbitrary extensions of the device marginal as adversary side information and hold uniformly over prime fields larger than the number of shares. For independent device--reference pairs, which provide the quantitative input to the argument, we determine the optimal exponential base when reconstruction requires all shares: $2\sqrt2/π$ for a qubit and $2/π$ for a classical bit, in both cases allowing arbitrary finite references. A comparison of selected marginals with product states converts the bounds for independent device--reference pairs into security guarantees for the correlated resources.

  匹配依据：MPC: secret sharing

  </details>

- **One-Round Threshold XMSS and SPHINCS+ from Fully Homomorphic Encryption**
  2026-10-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2360)
  Jung Hee Cheon, Kevin Choi, Hyeoncheol Joo, Taeseong Kim

  <details><summary>摘要 / Abstract</summary>

  While hash-based signatures such as XMSS and SPHINCS$^+$ are well-established and play a key role in post-quantum cryptography, thresholdizing them to enable use in distributed systems remains a challenge. In particular, their lack of exploitable structure prevents any algebraic attempts that are otherwise possible in the context of classical signatures such as ECDSA, Schnorr, RSA, or BLS, whereas general-purpose MPC techniques are costly in round complexity. In this work, we construct and implement the first one-round threshold protocol for XMSS and SPHINCS$^+$, with concrete parameters yielding full backward compatibility. At a high level, the secret key is shared among the signing parties while the signing algorithm is evaluated homomorphically using a threshold fully homomorphic encryption scheme. Any $t$-of-$n$ parties, via threshold decryption, can collaboratively derive the signature, which is accepted by the unmodified RFC 8391 or FIPS 205 verifier. At a technical level, we develop efficient homomorphic SHAKE evaluation over discrete CKKS for varying batch sizes. Analyzing XMSS and SPHINCS$^+$ signing reveals parallel hash computations and data-dependent selections, which we handle through batching and homomorphic lookup to obtain end-to-end circuits. Our implementation amortizes SHAKE256/256 evaluation to $3.4\,\text{ms}$ per hash and completes online threshold XMSS signing in $0.69\,\text{s}$. Threshold SPHINCS$^+$ has roughly two orders of magnitude higher signing latency but over an order of magnitude lower setup latency than XMSS.

  匹配依据：MPC: mpc (context)

  </details>

- **Cryptanalysis of a Class of Ideal Secret Sharing Schemes Based on the CRT for Polynomial Rings**
  2026-10-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.06312)
  Jian Ding, Zhiyuan Guo, Hongju Li, Yuying Man

  <details><summary>摘要 / Abstract</summary>

  Based on the CRT for polynomial rings, Yang, Zhu, Fu and Xia (ISIT 2026) proposed a compartmented secret sharing scheme for the compartmented access structure with lower bounds, claiming it can be ideal. We exhibit three families of unauthorized subsets that reconstruct the secret. The scheme is therefore insecure, except for a degenerate choice of parameters in which the only authorized subset is the whole participant set. The flaw in the security analysis is that it does not take all published polynomials into account. Similar flaws appear in the same first author&#x27;s hierarchical schemes (ISIT 2024, 2026).

  匹配依据：MPC: secret sharing

  </details>

- **Secure D2D Coded Caching under Radius-Limited Connectivity via Lifting**
  2026-10-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.05065)
  Han Fang, Nan Liu, Wei Kang

  <details><summary>摘要 / Abstract</summary>

  Secure device-to-device (D2D) caching requires users to generate delivery signals from their own caches and to recover their requested files without learning the other files. We construct schemes that meet both requirements when communication is limited to nearby users. The network consists of $K$ users on a cycle, a library of $N$ independent files, and a reception radius $r$. Delivery uses one round of noiseless orthogonal local broadcasts, with no server transmission. Each user&#x27;s cache has capacity $M$ file units. An outer secret-sharing code assigns file shares to senders, and a secure local caching scheme at each sender delivers the requested shares. The cache budget includes the sender&#x27;s library representation, random state, and delivery keys. We prove that each receiver&#x27;s cache and all audible broadcasts jointly reveal no information about nonrequested files, despite the dependence between the outer shares. The converse counts transmissions crossing a contiguous user block and uses secrecy to remove one user&#x27;s observation from the entropy bound. Let $h=2r$ and $K\ge h+1$. The private coded caching (PCC) instantiation attains the minimum peak sum load $K/h$ for every $M\ge Nh$ when $N&gt;1$. For $N\ge K$, its memory-sharing envelope is within a factor $15$ of the optimum throughout $M\in[N/h+2,Nh]$. We also apply lifting without secrecy constraints, achieving the optimal load on $M\in[hN/(h+1),N]$ and a factor-$9/2$ guarantee on $M\in[N/(h+1),N]$ when $N\ge K$.

  匹配依据：MPC: secret sharing

  </details>

- **Understanding Sigma Protocols via MPC-in-the-Head**
  2026-10-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2322)
  Haiyang Xue

  <details><summary>摘要 / Abstract</summary>

  In this paper, we propose an understanding of classical Sigma protocols (as denoted by $\Sigma$-protocols in the literature) through the lens of the MPC-in-the-head (MPCitH) paradigm. We seek not to construct new schemes, but to build a formal bridge connecting these two foundational areas. While many elegant yet foundational Sigma-protocols were introduced decades ago as standalone algebraic or combinatorial interactive proofs, reconsidering them via the modern aspect of (extended) MPCitH significantly enhances our cryptographic insight into their underlying structures. We present a formal mapping that translates classical commitment-challenge-and-response into the internal views of virtual parties, communicating via private point-to-point or public broadcast channels, secret-sharing schemes, commitments, and MPC consistency/correctness checks. By deconstructing algebraic schemes as linear secret-sharing protocols over public channels and combinatorial schemes as discrete threshold MPC instances over private/public channels, we isolate the exact structural reasons why their soundness and efficiency characteristics diverge. The protocols include: - Algebraic schemes: Schnorr, Okamoto, Chaum-Pedersen, Guillou-Quisquater, GMR for QR and discrete log over an unknown-order group. - Combinatorial schemes: Stern, GMW for Graph 3-Coloring, and Graph Isomorphism, among others. Although reinterpreting these already elegant, classic proofs using a heavy-weight machinery like MPCitH might seem redundant, it deepens our understanding of their underlying design principles.

  匹配依据：MPC: secret sharing

  </details>

- **Trusted Hardware Acceleration for Malicious-Secure Function Secret Sharing**
  2026-10-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.04818)
  Yujie Xue, Yijing Peng, Lin Liu, Shaojing Fu, Shaoqing Li, Yaohua Wang, Rongmao Chen, Yang Guo

  <details><summary>摘要 / Abstract</summary>

  Function secret sharing (FSS) underlies two-party private inference and private information retrieval, with cost dominated by generating, moving and evaluating distributed point function (DPF) keys. A trusted GPU-integrated distributed function accelerator (DFA) removed key movement by generating and consuming keys locally, but tolerates only semi-honest adversaries. A malicious host or GPU can tamper with shares, replay one-time material, swap buffers after checking, request early outputs, or abuse the accelerator as a forgery oracle, while malicious FSS ships large authenticated keys or multiplies DPF work. We present VIGOR-DFA, protecting the chain from authorized input to authorized output release with three mechanisms: a fresh authentication epilogue using three field multiplications per DPF output, 3.8-4.0 times faster per gate than per-lane DPF tag trees; a freeze-before-challenge check of every opening with t = 3 independent MAC lanes over F_{2^61-1}; and a role-bound one-time resource ledger with a release guard, in a protected datapath beside the GPU L2 cache. We prove stand-alone static malicious security with abort in a protected-module model, with statistical error Q(2/p)^t approximately 2^-148 for Q less than or equal to 2^32 checked batches. Our DFA-calibrated model shows that, against dealer-based malicious FSS modeled after the protocol family of Shark, VIGOR-DFA removes 21.8-563 GB of per-query offline authenticated material and, mainly by generating it in-module, lowers LAN latency by 10.1-14.0 times (1.5-1.8 times excluding offline distribution) and energy by 3.0-3.9 times. Malicious security costs 2.5-3.5 times LAN latency over semi-honest DFA and 0.145 mm^2 at 7 nm. We have completed the verification of specifications and the functional CPU reference model, including GPU/RTL conformance verification, protected runtime evaluation, and deployment-related tests.

  匹配依据：MPC: secret sharing

  </details>

- **Quantum-State Oblivious Transfer over Quantum Erasure Channels**
  2026-10-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.04667)
  Remi A. Chou

  <details><summary>摘要 / Abstract</summary>

  We study quantum-state oblivious transfer over the quantum erasure channel under information-theoretic security guarantees. Specifically, Alice holds two quantum systems, Bob wishes to recover one of them, and the parties have access to independent channel uses and authenticated public classical communication, with no initial shared entanglement. We consider both honest-but-curious and malicious behavior. We establish finite-blocklength converse and achievability bounds, which match in the honest-but-curious setting. The malicious setting construction combines interactive hashing with tests of whether Bob received selected channel outputs, and distributes each input across several qubits so that erasures conceal an entire input from a dishonest receiver, even when the inputs are entangled with an external reference. We also derive fixed-error asymptotic expansions and show that both malicious and honest-but-curious settings have the same capacity.

  匹配依据：MPC: oblivious transfer

  </details>

- **Multiparty Homomorphic Secret Sharing From Distributed Discrete Logarithm**
  2026-10-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2308)
  Pierre Meyer, Claudio Orlandi, Lawrence Roy, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  Homomorphic secret sharing (HSS) enables non-interactive distributed evaluation of functions on secret-shared inputs. While two-party HSS is well understood, multiparty constructions remain limited in expressiveness and efficiency. We present a general framework for constructing multiparty HSS from two-party semi-private HSS (which in turn can be instantiated using distributed discrete logarithms) via a new party virtualization paradigm. In a semi-private HSS, some designated inputs may be fully known to specific servers, while the remaining inputs remain hidden. Starting from two-party semi-private schemes, we obtain $N$-party semi-private HSS supporting compositions of polynomial computations and restricted multiplication straight-line programs, for $N = O(\log \lambda / \log \log \lambda)$. We further upgrade semi-private HSS to fully private HSS for functions of polynomial degree and polynomially bounded Waring rank. As a consequence, we obtain multiparty distributed point functions with key size polynomial in $\lambda$ and $\log |D|$, for a domain $D$ of superpolynomial size. When the underlying two-party scheme supports offline/online sharing, the resulting multiparty DPFs are programmable. Our framework admits instantiations under standard assumptions including DCR and class-group assumptions.

  匹配依据：MPC: secret sharing

  </details>

- **Breaking the $n^2$ Barrier: Information-Theoretic MPC with Sub-Quadratic Communication**
  2026-10-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2311)
  Alexander Bienstock, Yuval Efron, Kevin Yeo

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) considers the problem of securely computing a function across $n$ parties such that no adversary controlling $t$ corrupted parties may learn any additional information beyond the function output. For information-theoretic security in the honest majority setting, recent works have made tremendous progress in reducing the MPC communication costs for large circuits obtaining as low as $\tilde{O}(|C|)$ total communication. To date, all information-theoretic MPC protocols require an additive $\tilde{\Omega}(n^2)$ communication independent of the circuit size that becomes the dominant cost for small circuits. In this work, we consider the problem of building more efficient information-theoretic MPC protocols with $o(n^2)$ communication for small circuits. For corruption threshold $t&lt; (1/2-\epsilon)\cdot n$, we present an information-theoretic MPC protocol secure against adaptive and malicious adversaries with subquadratic communication for a wide range of circuits, including those in which the number of input parties $I$ satisfies $|I| = o(n)$, circuit size $|C| = o(n^{1.5}/|I|)$, and circuit depth $\mathsf{depth}(C) = o(n)$; for example, $|C| = o(n^{3/4})$ and $|I| = o(n^{3/4})$ input parties. To our knowledge, this is the first information-theoretic MPC protocol with $o(n^2)$ communication for a wide-range of circuit classes. Furthermore, we note the requirement of sublinear input parties $|I| = o(n)$ is necessary to obtain $o(n^2)$ communication due to the $\Omega(|I| \cdot n)$ lower bound by Damgård {\em et al.} [EUROCRYPT&#x27;16]. To obtain our new MPC protocol, we develop new techniques for key MPC subroutines including randomness generation, player virtualization and output reconstruction with $o(n^2)$ communication leveraging the sublinear number of input parties, $|I| = o(n)$, and randomized output distribution with unpredictable communication patterns. Finally, we also prove a separation showing that $o(n^2)$ communication MPC is impossible for adversaries with stronger than standard adaptive rushing capabilities even for constant-size circuits.

  匹配依据：MPC: secure multi party computation

  </details>

- **An Input-Fed AES-Round Family for Fixed-Length Hashing**
  2026-10-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2314)
  Peter Rindal

  <details><summary>摘要 / Abstract</summary>

  Secure computation often hashes high-entropy fixed-length values in inner loops. A public permutation with terminal Davies--Meyer feed-forward can expose the permutation value when an application applies another feed-forward step. We study an input-fed alternative that injects the input after every AES round. The base construction, $H_{128}:\{0,1\}^{128}\to\{0,1\}^{128}$, uses ten full AESENC-style rounds with keys $x+c_i$ and no AES key expansion. Its concrete analysis adapts differential, collision, linear, integral, and meet-in-he-middle (MITM) methods to this shared-input round-key interface. We prove a three-round integral distinguisher and give a five-round anchored MITM attack candidate with estimated time $2^{120}$; the remaining results provide reduced-round evidence rather than a proof of random-function behavior. On an AMD Ryzen 9 7950X, measured scalar and eight-lane AES-NI costs are within one percent of fixed-key AES-128; a sixteen-block VAES kernel is 2.3\% slower. Two extensions use the same input-fed principle. The tweakable construction $H_{128}^{\mathsf{tw}}$ splits a 72-bit public counter into an eight-bit tweak and a 64-bit epoch. One public schedule serves 256 consecutive positions, and consecutive fixed-key AES outputs under a published key supply the epoch schedules. Within one epoch, a pair with different tweaks can cancel at most one complete boundary injection. The construction also admits an exact 256-query two-round integral distinguisher. The wide construction $H_{256}$ maps 256 bits to 256 bits. It uses two AES lanes and adopts the column permutation and round constants of Haraka-256 v2 [KLMR16]. We analyze the differential, integral, collision, slide, rebound, and MITM mechanisms introduced by these extensions. A supporting ideal-permutation analysis shows that affine wrappers with one or two permutation calls fail generically. For three calls with independently uniform public constants, it gives a birthday-order bound when the distinguisher completes its primitive queries before querying the target. Finally, we define checkable punctured vectors and prove a GM-style protocol secure against static semi-honest corruptions in the ideal-OT and random-oracle model.

  匹配依据：MPC: secure computation

  </details>

- **Robust and leakage-resilient device-independent oblivious transfer in MiniQCrypt**
  2026-10-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.01421)
  Zhili Chen, Rahul Jain, YaoNan Zhang

  <details><summary>摘要 / Abstract</summary>

  Assuming post-quantum one-way functions, we construct device-independent (DI) oblivious transfer (OT) and bit commitment: honest parties use only trusted classical computation to operate untrusted quantum devices, which may share arbitrary entanglement and behave non-IID. Security is simulation-based against quantum polynomial-time adversaries and composes sequentially with efficient simulators. One protocol skeleton serves both, in two regimes. With isolated laboratories and coordinate-local measurements in the honest receiver&#x27;s device, it tolerates a constant rate of honest-device faults. With polylogarithmically many qubits of adaptive leakage between the laboratories and arbitrary joint measurements, it tolerates an inverse-polylogarithmic rate. Each elementary DI call uses a fresh, isolated batch of polylogarithmically many device coordinates, and total device use in the compiled OT protocol is polynomial. The commitment has efficient simulators against both parties and yields DI coin tossing with abort. Because OT is complete for secure computation, the construction yields a DI protocol, with abort, for every efficiently computable classical functionality on a fixed number of parties, secure against static corruption of any proper subset of them. The commitment&#x27;s extractor changes a public parity relation through classical equivocation and leaves the device execution, hence its leakage, unchanged. A commit-and-prove functionality, disjoint audits, and an affine consistency check link the certified correlations to ideal OT. Sender security rests on a selector-aware parallel-repetition bound for the Magic Square game, which we derive from the two-round threshold theorem of Kundu and Tan.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **Pseudorandom Correlation Generators for Matrix Triples**
  2026-10-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2298)
  Maxime Bombar, Geoffroy Couteau, Nikolas Melissaris, Anuja Modi

  <details><summary>摘要 / Abstract</summary>

  We introduce new pseudorandom correlation generators (PCGs) for matrix triples: shares of triples $(A,B,A\cdot B)$ where $A,B$ are random matrices over $\mathbb{F}^{n\times n}$ for a field $\mathbb{F}$ and an integer $n$. Matrix triples are consumed in a wide variety of secure computation protocols that involve matrix arithmetic, which occurs commonly in settings such as privacy-preserving machine-learning and statistics, threshold cryptography, secure linear algebra, and more. Previous PCGs for matrix triples are inefficient: their seed grows at least linearly in the matrix dimension, and their expansion is slow. In this work, we introduce two new PCGs with improved performances: 1. Our first construction, inspired by the recent work of (Gentry and Lee, Crypto 2026) on FHE for matrix arithmetic, relies on the quasi-abelian syndrome decoding (QASD) assumption introduced in (Bombar et al., Crypto 2023), an assumption which has since received a significant amount of attention. Our PCG generates $N$ matrix triples over $\mathbb{F}^{n\times n}$ from a seed of size $poly(\lambda,\log n,\log N)$ using $\Theta(n^3\log(n^3N))$ field operations per triple, removing the linear dependency on $n$ from the seed compared to previous works. 2. Our second construction is more mathematically involved, and builds upon an elegant and surprising connection with the Weyl-Pauli twisted algebra, a mathematical structure originally studied in (Weyl, Zeitschrift für Physik, 1927) in the context of quantum kinematics. Our PCG relies on a new variant of the QASD assumption over the Weyl-Pauli twisted group algebra and exhibits impressive performances: it has the same seed size as our first construction and generates $N$ matrix triples at a cost only a small constant time larger than the cost of computing $N$ matrix triples in the clear. We complement our results with an in-depth study of our new twisted QASD assumption and demonstrate the benefits of our PCGs in concrete applications such as privacy-preserving machine learning and threshold MAYO.

  匹配依据：MPC: secure computation

  </details>

- **Non-Interactive Black-Box Witness-Indistinguishable Commit-and-Prove via Targeted Hitting-Set Generators**
  2026-10-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2286)
  Susumu Kiyoshima

  <details><summary>摘要 / Abstract</summary>

  Targeted hitting-set generators (HSGs) are primitives that have recently attracted attention in the study of pseudorandomness and derandomization. Recent works have shown that sufficiently strong targeted HSGs can be used to soundly instantiate the Fiat--Shamir transformation, yielding non-interactive protocols against uniform PPT adversaries in the plain model (i.e., without any setup phase for selecting a cryptographic hash function). In particular, Chen et al. (STOC 2025) combined this paradigm with the MPC-in-the-head technique to construct a non-interactive witness-indistinguishable argument for NP from a non-interactive commitment scheme and a targeted HSG. Inspired by these results, we explore other cryptographic applications of this paradigm. Our main result is a black-box construction of a non-interactive witness-indistinguishable commit-and-prove scheme against uniform PPT adversaries in the plain model. Following Chen et al., we obtain our construction by combining the MPC-in-the-head technique with the targeted-HSG-based Fiat--Shamir paradigm. The construction relies on an injective one-way function with efficiently recognizable range and a sufficiently strong targeted HSG. The latter is the same targeted HSG used by Chen et al. and can be instantiated under a very strong but plausible complexity-theoretic assumption.

  匹配依据：MPC: mpc (context)

  </details>

- **Kettle: Short Post-Quantum Threshold Signatures from the HAWK Signature Scheme**
  2026-10-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2288)
  Calvin Abou Haidar, Daniel Escudero, Thomas Espitau, Clément Hoffmann, Kaoru Takemure, Mehdi Tibouchi, Hernán Darío Vanegas Madrigal

  <details><summary>摘要 / Abstract</summary>

  HAWK is a lattice-based hash-and-sign signature scheme that was a third round candidate in the NIST additional call for post-quantum signatures. It has short signatures and keys, as well as fast and portable signing and verification. However, in response to a highly-publicized AI-driven cryptanalytic result that reduced its security (roughly doubling the required dimension to achieve a given security level), the authors de- cided to withdraw from the competition. The need to increase parameters was seen as limiting the size advantage of HAWK compared to the already selected lattice schemes ML-DSA and Falcon, which was one of its primary selling points along- side speed and the lack of floating-point arithmetic. In this paper, we identify another attractive aspect of the HAWK design that is not affected by the AI attack and has been overlooked so far: its surprising friendliness to multi- party computation (MPC). Indeed, HAWK signing can be achieved in a generic way from a small collection of basic composable MPC functionalities (like integer multiplication, uniform random generation, etc.) in such a way that instanti- ating those functionalities using MPC protocols with given security properties (semi-honest vs. malicious, honest vs. dis- honest majority, etc.) yields a secure protocol for MPC signing with those same properties. As a result, we obtain Kettle, a UC-secure threshold signa- ture protocol that outputs specification-compliant HAWK sig- natures and scales to an arbitrary number of parties. It offers essentially the shortest signature size so far for a lattice-based threshold signature, while achieving significantly lower round complexity and online communication cost than other thresh- old protocols built from pre-existing, non-threshold lattice- based signatures (like ML-DSA and Falcon): as low as 2 online rounds (a dozen rounds total) and 2 kB online com- munication per party, depending on the specific setting and optimization choices. We also provide a proof-of-concept implementation of our approach in the MP-SPDZ framework, which can be instanti- ated with any number of parties, any threshold, and a variety of security properties.

  匹配依据：MPC: multi party computation

  </details>

- **Homomorphic Advantage Operator: Stabilizing Reinforcement Learning Under Fully Homomorphic Encryption Constraints**
  2026-10-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.02074)
  Abid Mohamed Nadhir, Ahmad Al Hanbali, Beggas Mounir

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving machine learning presents significant deployment challenges on the cloud for intelligent systems with confidential data. Fully Homomorphic Encryption (FHE) offers a compelling solution for secure computation, preserving data confidentiality of cloud computations. However, applying FHE to reinforcement learning (RL) requires replacing non-linear operations with polynomial approximations, which diverge catastrophically due to a unique recursive error phenomenon known as the Bellman drift. This article introduces the Homomorphic Advantage Operator (HAO), a stabilization framework designed to prevent polynomial approximation divergence in FHE-based deep RL. HAO adapts the zero-mean centering projection from advantage-based value estimation directly to temporal-difference (TD) targets. This linear projection annihilates the uniform state-value baseline that drives the Bellman drift, maintaining per-state action rankings while requiring zero additional non-linear multiplicative depth and avoiding expensive ciphertext bootstrapping. The proposed HAO framework was evaluated using a three-tier experimental methodology, including a tabular Markov Decision Process (MDP), an encrypted CartPole environment using real CKKS cryptographic operations, and a 20-node logistics routing benchmark with dense continuous features. The results demonstrate that the proposed HAO strictly bounds network pre-activations within the safe polynomial approximation domain. The proposed HAO RL agents achieved 0% boundary breaches across all random seeds used, whereas regularization alone (L2 weight decay and gradient clipping) breached the bound on 3 of 5 seeds and the unstabilized baseline did so in 83.8% of episodes. Finally, HAO agents improve optimal policy accuracy by 18.0 percentage points in tabular domains and remain stable when DP-SGD-style Gaussian noise is added to the clipped gradients.

  匹配依据：MPC: secure computation

  </details>

- **DuraShare: BIP39-native secret sharing with full manual fallback**
  2026-10-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2300)
  Jeroen van de Graaf, Renato Schiavinato Lopez

  <details><summary>摘要 / Abstract</summary>

  BIP39 is a Bitcoin standard that turns a wallet&#x27;s random seed of size between 128 and 256 bits into a human-readable sequence of 12 to 24 words, taken from a fixed 2048-word list. Each word corresponds to an index in that list. DuraShare allows the holder of this sequence to split it among $n$ Sharekeepers, each of whom receives one share. Any subset of $k$ Sharekeepers can combine their shares and reconstruct the original sequence, whereas $k-1$ colluding Sharekeepers obtain no (Shannon) information. For everyday convenience we adopt a software-assisted model, while ensuring that a full manual fallback remains feasible for recovery, requiring nothing beyond paper, a calculator, and specific instructions. This matters because Sharekeepers may be family members or lawyers unfamiliar with crypto-technology, called upon only decades later, when no specific vendor, software, or hardware can be assumed to still exist. DuraShare combines three existing, well-established cryptographic techniques: (1) Shamir Secret Sharing over $\mathbb{F}_{2053}$, the smallest prime larger than 2048; (2) 2D error detection, applying row and column checksums to each share to protect the data against transcription errors and physical damage; and (3) a simple affine inner-product MAC over $\mathbb{F}_{2053}$ to authenticate each share, preventing a Sharekeeper from tampering without being detected.

  匹配依据：MPC: secret sharing

  </details>

- **Deniable Secret Sharing: Towards Practical Faking**
  2026-10-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2294)
  Ignacio Amores, Tamar Ben David, Matteo Campanelli, Sebastian Kolby, Eran Omri, Anat Paskin-Cherniavsky, Sophia Yakoubov

  <details><summary>摘要 / Abstract</summary>

  Deniable secret sharing (DSS; Canetti et al, TCC 2025) is designed for a scenario where an adversary is able to bribe or coerce all shareholders to divulge their shares of a secret. A deniable secret sharing scheme is equipped with a faking function that enables shareholders to produce fake shares that look like real shares, but do not actually reveal any additional information about the secret. Existing DSS constructions require the fakers to jointly compute on their shares, without considering how this computation might be realized. In this paper, we investigate two crucial properties of such computations: the extent to which the fakers themselves learn information about the secret (privacy against fakers), and the number of messages they need to exchange (message complexity). Message complexity can be seen as a measure of faking conspicuousness, if the adversary is able to observe network traffic. We prove that to obtain the strongest notion of DSS, any information-theoretic construction requires the fakers to exchange a non-zero number of messages, which could be large (depending on the access structure). We describe a general construction that matches this lower bound in many cases, e.g. for threshold access structures. Furthermore, for linear secret sharing schemes, we prove that certain unqualified sets must learn the secret as a result of faking. Moving to the computational setting, we describe two constructions which require no interaction beyond the knowledge of who the fakers are. This implies that both inconspicuousness and privacy against fakers are achieved. The first construction requires the share size to be exponential in the number of shareholders, but assumes only a PRG. The second construction has small shares, but assumes virtual black-box obfuscation. We see the latter construction as a stepping stone for a future iO-based instantiation. All of our lower bounds and constructions consider general access structures.

  匹配依据：MPC: secret sharing

  </details>

- **Randomized Early-Stopping Byzantine Agreement with Applications to Round-Efficient MPC**
  2026-09-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2284)
  Michele Ciampi, Pouyan Forghani, Yun Lu, Vassilis Zikas

  <details><summary>摘要 / Abstract</summary>

  We consider two main classes of synchronous round-efficient Byzantine Agreement (BA) protocols: \emph{expected constant rounds} and \emph{early-stopping}. Randomized protocols can terminate in expected constant rounds, and early-stopping protocols&#x27; worst-case round complexity depends on the actual number of corrupted parties $f\le t$, with $\min(t+1, f+2)$ being optimal. In this work, we combine the benefits of both classes, proposing a protocol that has constant round-complexity in expectation and $O(f)$ in the worst case. We present our protocol in the form of a compiler that can lift a broad class of expected-constant-round BA protocols, including Feldman--Micali and Katz--Koo, to {\em also} achieve near-optimal $O(f)$ worst-case complexity. This yields the {\em first} treatment of perfectly secure BA protocols for $t&lt;n/3$ that is both expected constant-round and near-optimal ($O(f)$) early stopping. Assuming a PKI, we show a variant of the compiler with a better round complexity, tolerating $t&lt;n/2$ corruptions. We also extend our results to parallel broadcast, also known as interactive consistency (IC). We give a compiler that runs $N$ Byzantine agreement instances in parallel while preserving both guarantees, expected constant rounds and $O(f)$ rounds in the worst case. Parallel broadcast then follows with one extra round for $t&lt;n/2$. To the best of our knowledge, this is the first compiler of its kind, and the first IC protocol with such expected and worse round-complexity. Finally, by combining our protocol with standard (fast) sequential composition techniques, we obtain a valid candidate to execute \emph{multi-party computation protocols} that require broadcast as their hybrid. By running existing MPC constructions using our broadcast protocol, we obtain the first MPC protocol that requires constant rounds of P2P communication in expectation and $O(f)$ rounds in the worst case.

  匹配依据：MPC: multi party computation

  </details>

- **Quantum Secret Sharing and Error Correction vs No-Cloning**
  2026-09-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2610.00441)
  Steven Chien, Ishani Mukherjee, Mark Zhandry

  <details><summary>摘要 / Abstract</summary>

  Secret sharing is ubiquitous throughout cryptography. All possible access structures are classically feasible, and in the case of threshold access structures, the protocols are even very efficient. However, when moving to the quantum setting, the no-cloning theorem shows that many access structures are impossible. In fact, no-cloning exactly characterizes feasibility: for thresholds, quantum secret sharing is possible if and only if the threshold $t$ is strictly more than $n/2$. In this work, we propose a variant of quantum secret sharing (QSS) where two or more identical copies of the input state are provided, but the output is only required to recover one copy. This notion circumvents the simple one-copy no-cloning obstruction, though the natural $k$-copy generalization still gives much milder obstructions. For thresholds using $k$ copies, no-cloning implies that QSS is impossible whenever $t\leq n/(k+1)$. It is tempting to hypothesize that no-cloning continues to exactly characterize the many-copy case. However, we show that this is not the case. We give positive results showing that multiple copies allow for going slightly beyond the single-copy obstruction: for thresholds, we construct QSS whenever $t&gt;(n-k+1)/2$. On the other hand, we give a novel obstruction we call the Clique Path obstruction, which applies to arbitrary access structures. For thresholds, it shows that QSS is impossible whenever $t\leq (n-1)/k$. Our upper and lower bounds exactly match for $k=2$. Both our results leverage connections to the $k$-colorability of certain graphs derived from the access structure. We leave closing the gap for $k\geq 3$ copies as a fascinating direction for future work. Secret sharing is closely related to error correction, which can also be considered in the many-copy setting. Our results imply similar obstructions for quantum error correction for erasure channels.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy Foundations for Multi-Institutional Scientific Artificial Intelligence**
  2026-09-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.39787)
  Olivera Kotevska, Sumit Jha, Aur'elien Bellet, Rui Hu, Nathaniel D. Bastian, Rafael Ferreira da Silva, Ravi Madduri, Kibaek Kim

  <details><summary>摘要 / Abstract</summary>

  Scientific artificial intelligence (AI), spanning foundation models (FMs) to federated data-analysis pipelines, is becoming shared infrastructure across national laboratories, universities, hospitals, and industrial partners. This collaboration creates privacy risks whose natural unit is often an institution&#x27;s participation, research strategy, or technical capability rather than a single record. Differential privacy (DP), federated learning (FL), secure computation, trusted execution, and provenance each protect parts of the stack, but their guarantees rarely compose across mixed-trust institutions, access tiers, and autonomous agents. This perspective recasts privacy for scientific AI as an assurance problem defined by six elements: protected asset, observer, channel, permitted disclosure, guarantee, and evidence. We demonstrate the framing through a claim register for a composite cross-institutional scenario and use it to assess the model lifecycle. Two of the resulting gaps are specific to leadership-class facilities: scheduler, allocation, and telemetry metadata expose an institution&#x27;s resource posture, and instrument-attached control loops leak research strategy through timing and contention on shared accelerators. We identify six research priorities: institution-level guarantees, agent-communication privacy, cross-tier information flow, privacy-compatible reproducibility, leadership-scale accounting, and instrument side channels. The contribution is a common form for stating, comparing, and auditing claims whose guarantees otherwise remain fragmented across the scientific AI stack.

  匹配依据：MPC: secure computation

  </details>

- **Natural Barriers to Quantum Extraction: On the Post-Quantum (In)security of (O)EKE and Masny-Rindal OT**
  2026-09-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.39844) · [IACR ePrint](https://eprint.iacr.org/2026/2280)
  James Bartusek, Jake Januzelli

  <details><summary>摘要 / Abstract</summary>

  Encrypted key exchange (EKE), introduced by Bellovin and Merritt (IEEE S\&amp;P 1992), and Masny-Rindal OT, introduced by Masny and Rindal (ACM CCS 2019), are highly-efficient methods for compiling essentially any KEM into advanced cryptographic protocols, namely password-authenticated key exchange (PAKE) and oblivious transfer (OT), by relying only on idealized symmetric-key primitives. They have become leading candidates for practically-implementable PAKE and OT due to (1) their simplicity, (2) their plug-and-play nature, allowing for flexibility in the choice of KEM, and (3) existing proofs of UC-security (in the classical adversarial model). Due to point (2) above, these compilers yield attractive candidates for efficient post-quantum PAKE and OT, especially given the recent post-quantum KEM standardization efforts. This motivates the question of whether the (UC-)security of these compilers translates to the quantum adversarial model. In this work, we show that it does not. In particular, we prove that a general family of (O)EKE protocols, as well as Masny-Rindal OT, are not UC-secure against quantum polynomial-time adversaries, even when instantiated with a post-quantum KEM. To establish UC-insecurity, we devise an adversarial strategy that provably thwarts any attempt by the simulator to extract its input (the password in the case of PAKE, and the receiver&#x27;s choice bit in the case of OT). These are the first naturally-occurring/non-contrived cryptographic protocols that are known to be secure in the (classical) ROM but provably insecure in the QROM. To complement these negative results, we establish that both compilers yield certain notions of game-based security. In the PAKE setting, we consider OEKE instantiated with the ``2-Feistel&#x27;&#x27; cipher, and prove its stand-alone game-based security in the quantum random oracle model. We view these results as a proof of concept that security of (O)EKE and Masny-Rindal OT can yet be redeemed in the quantum setting, though we caution that the situation will be more subtle than in the classical setting due to the breakdown of simulation-based security. Along the way, we establish a novel ``advantage-tight&#x27;&#x27; one-way to hiding lemma that may be of independent interest.

  匹配依据：MPC: oblivious transfer

  </details>

- **Quantum Secure Non-Interactive Reductions**
  2026-09-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.38452)
  Maxwell Gold, Sarah Hagen, Daniel Alabi, Eric Chitambar

  <details><summary>摘要 / Abstract</summary>

  Efficient models for secure computation often rely on offline preprocessed correlations, which subsequently enable private online computation from minimal assumptions. Within these models, the study of secure non-interactive reductions (SNIR) formalizes when one classical correlation can be non-interactively transformed into another, while guaranteeing information-theoretic simulation-based privacy. In this work, we introduce quantum secure non-interactive reductions (QSNIR), a natural extension of SNIR, in which the source and target resource are each a bipartite quantum state. Specifically, when the target resource is classical, our framework enables us to analyze the problem of disseminating private correlations from entanglement, in addition to classical resources. Our primary technical result is that QSNIR privacy in this context can be computed exactly via a semidefinite program (SDP) pair that quantifies an error operationally rooted in a simulation-based cheating advantage. We prove that QSNIR privacy is lower-bounded by a decision problem related to minimum-error state discrimination (MED), and use both definitions to compute exact one-shot privacy errors for universal two-party computation (2PC) preprocessing correlations.

  匹配依据：MPC: secure computation, two party computation

  </details>

- **Quantum Leakage Resilience of Shamir Secret Sharing**
  2026-09-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.37276)
  Rishabh Batra, Fuyuki Kitagawa, Ryo Nishimaki, Takashi Yamakawa

  <details><summary>摘要 / Abstract</summary>

  We initiate the study of quantum leakage resilience of unmodified Shamir secret sharing over prime fields. A well-studied leakage model for Shamir&#x27;s secret sharing classically is single-bit local leakage from each share. We consider its quantum analogue where, for each party, a local leakage channel takes as input the party&#x27;s share and outputs a leaked qubit. Without preshared entanglement, we show that the distinguishing advantage is $2^{-Ω(n)}$ when the threshold rate $t/n=τ$ exceeds $τ_\star\approx0.73339$ by a fixed positive margin. More generally, we allow disjoint entangled blocks of any fixed maximum size where there is no entanglement between different blocks or with the adversary, and each block emits at most a fixed number of qubits. Security holds when the threshold rate is high enough (sufficiently close to one). We then allow a specified set of devices to share entanglement with the adversary. We show that security holds even when a linear number of devices ($αn$ for small $α&gt;0$) share entanglement with each other and with the adversary for a large enough threshold rate. As a complementary negative result, we also show that even classical single-bit leakage makes Shamir scheme insecure if we allow arbitrarily large entanglement between the leakage devices. A GHZ state shared by exactly $t$ leakage devices makes even classical one-bit leakage insecure, without any entanglement with the adversary. In this attack, each participating device emits only one classical bit, and their joint parity distinguishes any chosen pair of secrets with a constant advantage. Thus, for fixed threshold rates above $τ_\star$, the maximum number of devices that may share arbitrary entanglement with one another and with the adversary while preserving security is linear in $n$ up to constant factors, although the optimal support fraction remains open.

  匹配依据：MPC: secret sharing

  </details>

- **PQMZ: Formally Verified Falcon-PKR for Post-Quantum Cryptographic Migration in Zcash**
  2026-09-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2260)
  Hannes Hacker, Shekoufeh Neisarian, Sara Zain, Elif Bilge Kavun

  <details><summary>摘要 / Abstract</summary>

  Migrating blockchain systems to Post-Quantum Cryptography (PQC) requires not only replacing classical primitives, but also analysing transformations that change how signatures are represented and verified. We study Falcon-PKR, a public-key-recovery variant of Falcon, motivated by Zcash-like transparent transaction workflows. Falcon-PKR replaces explicit storage of the full Falcon public key with a compact stored digest and reconstructs a candidate public key from the signature during verification. In our construction, this reduces the combined representation size of public key and signature by approximately 15%, but it also introduces a distinct security case in which verification depends on a reconstructed key derived from adversarially supplied signature data. We address this with a machine-checked EasyCrypt formalisation in the Random Oracle Model (ROM). We mechanically verify an EUF-CMA reduction showing that the security of Falcon-PKR is bounded by the security of standard Falcon together with collision resistance of a domain-separated public-key hash. The analysis therefore treats both assumptions explicitly and does not claim a proof of Falcon itself. We also machine-check correctness for honest signing under an abstract Falcon signing interface. We implement Falcon-PKR for Falcon-512 and Falcon-1024 in Python and C, and evaluate runtime and size against ECDSA and selected Post-Quantum (PQ) alternatives, exposing explicit verification and storage trade-offs. As a complementary case study, we implement and analyse an extended SECUER-based Multi-Party Computation (MPC) ceremony architecture. Together, the two case studies address both transaction-signature and ceremony-infrastructure layers of PQ blockchain migration.

  匹配依据：MPC: multi party computation

  </details>

- **OPFL: Optimistic Verification of Federated Learning via Empirical Boundary**
  2026-09-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.37011)
  Hongxu Su, Jianzhu Yao, Xuechao Wang, Pramod Viswanath

  <details><summary>摘要 / Abstract</summary>

  Federated learning enables multiple clients to collaboratively train models without sharing their private data. However, the lack of visibility into local training makes it difficult to verify whether clients follow the prescribed training procedure or submit malicious updates, such as model poisoning. A natural approach is to replay client training for verification. However, privacy-preserving replay produces numerical results that cannot be directly matched with local client execution because the two run in different environments. We present OPFL, an optimistic verification framework for privacy-preserving federated learning. To protect data privacy, OPFL performs replay inside secure multi-party computation (MPC). Although gradients computed on MPC and local GPUs are not bitwise identical, we observe that their absolute differences are stable and bounded. OPFL therefore calibrates an empirical boundary offline and uses it to distinguish benign numerical deviations from malicious manipulation. To reduce the cost of expensive MPC replay, OPFL adopts optimistic verification by post auditing only sampled training steps. Experiments on LeNet, BERT, and Qwen show that the boundary generalizes across datasets, input lengths, and GPUs, while achieving $0$\% ASR against model poisoning and PGD-based attacks. On a LeNet workload, at $p=0.01$, OPFL is approximately $98.6\times$ faster than full MPC-based FL and $625.5\times$ faster than ZK-based approach.

  匹配依据：MPC: secure multi party computation

  </details>

- **TPOKÉ: Threshold Public-Key Encryption from POKÉ via Isogeny Sharing**
  2026-09-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2243)
  Toshiki Takatera, Hiroshi Onuki, Tsuyoshi Takagi

  <details><summary>摘要 / Abstract</summary>

  POKÉ, introduced by Basso and Maino, is one of the most efficient isogeny-based public-key encryption schemes. The generic parallel-encryption approach yields a $(t,n)$-threshold variant by running $n$ independent POKÉ instances and secret-sharing the message, but this multiplies the public-key and ciphertext sizes by roughly $n$. We present S-TPOKÉ, a POKÉ-based $(t,n)$-threshold construction for every $1\le t\le n$, and Ch-TPOKÉ, an $(n,n)$ variant that arranges the parties&#x27; secret isogenies differently. Both schemes avoid repeating part of the isogeny computation that appears in every independent POKÉ instance. Compared with the trivial construction, they reduce the number of degree-$3^{b}$ isogenies computed during encryption from $2n$ to $n+1$ and reduce the ciphertext size by about a factor of two when $n$ is large. The two schemes differ in how the parties&#x27; secret isogenies are arranged. S-TPOKÉ is our main construction: the dealer samples $n$ independent secret isogenies, while encryption samples one sender-side secret isogeny and shares it across the parties. Ch-TPOKÉ instead arranges the parties&#x27; secret isogenies into a chain. For S-TPOKÉ, we prove SIM-CPA security under static corruption in the random oracle model from the $(k,n)$-S-C-POKE assumptions for all $1\le k\le t$, which extend C-POKE to the threshold setting. For Ch-TPOKÉ, we prove only SIM-CPA security under static maximal corruption from the $(j,n)$-Ch-D-POKE assumptions for all $j\in\{1,\ldots,n\}$, which extend D-POKE to a chain-based threshold setting. This guarantee is strictly weaker than SIM-CPA security under static corruption. We also give asymptotic parameter choices targeting $\lambda$-bit security and derive closed-form expressions for the public-key, ciphertext, and partial-decryption sizes in terms of $\lambda$ and $n$.

  匹配依据：MPC: secret sharing

  </details>

- **Batch Decryption from New Standard Assumptions**
  2026-09-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2252)
  Nico Döttling, Bernardo Magri, Benjamin Marsh, Mahesh Sreekumar Rajasree

  <details><summary>摘要 / Abstract</summary>

  Batch decryption allows an authority to release a short key that enables public decryption of a selected batch of ciphertexts. Motivated by encrypted mempools, we study this capability through two constructions with different authorization semantics and assumptions. First, we provide a simple and compact epochless construction in an RSA group based on Fiat&#x27;s Batch RSA [CRYPTO&#x27;89]. Its batch-decryption hint is just one group element, and its keys and ciphertexts have size independent of the batch size, with no batch bound fixed at setup. We prove adaptive security under the strong RSA assumption in the random-oracle model. The scheme permits repeated releases for overlapping batches, with each release authorizing decryption of the selected ciphertexts. Second, we give an adaptively secure generic construction of identity-based encryption with batch decryption in the epoch-based model, which permits at most one batch-key query for the challenge epoch. The construction combines deferred encryption via garbled circuits, non-inclusion secure registration-based encryption, and weak receiver non-committing IBE. We construct the latter primitive from ordinary IBE and pseudorandom functions, obtaining an instantiation of the epoch-based construction from the computational Diffie--Hellman assumption.

  匹配依据：MPC: garbled circuits

  </details>

- **Adaptively UC-Secure Oblivious Transfer from Group Actions**
  2026-09-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2251)
  Olivier Blazy, Céline Chevalier, Saqib Kakvi, Lola-Baie Mallordy

  <details><summary>摘要 / Abstract</summary>

  Oblivious Transfer (OT) is a fundamental building block for secure computation, in which a sender holds two messages and a receiver learns exactly one of them, without revealing which one was chosen and without learning the other. While generic constructions for Universally Composable (UC) OT exist, instantiating them from post-quantum assumptions remains challenging, particularly under adaptive corruption. In this work, we present the first adaptively UC-secure OT protocol based on Group Actions, specifically assuming weakly pseudorandom Effective Group Actions (EGA) like CSIDH. We adhere to the framework of [BC15], which derives an adaptively UC-secure OT protocol from SPHF-friendly extractable and equivocable (E²) commitment schemes. The central challenge in instantiating this construction from group actions is the lack of SPHF-friendly IND-CCA encryption. Classical CCA transformations such as Fujisaki-Okamoto destroy the algebraic structure required for building SPHFs over ciphertexts, while known group action-based schemes offer no native mechanism to prove ciphertext validity. To overcome this obstacle, we construct from group actions an IND-CCA encryption scheme with enough algebraic structure to efficiently recognize valid ciphertexts. Our contributions are threefold: (1) a verifiable chameleon hash function with perfect soundness in the standard model, (2) an SPHF-friendly, publicly verifiable IND-CCA encryption scheme in the random oracle model, and (3) we combine these to build an SPHF-friendly E² commitment scheme and derive a fully adaptively secure OT protocol in the UC framework. This is the first construction of its kind under group action assumptions, enabling post-quantum secure OT with adaptive security guarantees. These building blocks may also be of independent interest e.g., to obtain digital signatures, non-malleable commitment schemes, or verifiable encryption.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **Threshold Signatures with Identifiable Abort from One-way Functions**
  2026-09-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2238)
  Mojtaba Fadavi, David Jao, Samuel Jaques

  <details><summary>摘要 / Abstract</summary>

  A $(T,N)$-threshold signature scheme distributes a signing key among $N$ participants so that any $T$ participants can jointly generate a valid signature, while fewer than $T$ cannot. In this work, we first introduce a threshold one-time signature scheme with \emph{identifiable abort} based on a variant of Lamport one-time signature and Shamir secret sharing, enabling authorized participants to jointly reconstruct signatures from partial signatures. We then extend the scheme to support multiple messages using multi-layer Merkle trees. One-time signatures introduce specific coordination challenges: participants must agree on both the message and the one-time key index to avoid unsafe key reuse. We address this using a bulletin-board mechanism for consensus. Under this framework, our construction produces signatures with one message from the bulletin board to each signer and one response message from each signer, while the bulletin board may require additional communication to reach agreement. With a simple majority-vote bulletin board, the scheme signs in four rounds. Subject to this coordination constraint, the construction inherits the guarantees of the underlying threshold framework: Universal Composability (UC) unforgeability with identifiable abort, non-UC robustness, and a bulletin-board mechanism that is UC-secure with an honest super-majority and robust when the central aggregator is honest.

  匹配依据：MPC: secret sharing

  </details>

- **Local Rewriting under Assumed Erasure**
  2026-09-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2229)
  Napassorn Litchiowong

  <details><summary>摘要 / Abstract</summary>

  We study local rewriting after an assumed erasure step in an ideal oblivious-transfer protocol. Bob transforms his retained record while Alice&#x27;s actual record remains fixed. Exact rewriting between shared-source and independent-source records is possible in both directions precisely when the retained records of the shared source are independent. For balanced deterministic maps retaining $k$ and $\ell$ bits from an $n$-bit source, the optimal error over the maps is $\max\{0,1-2^{n-k-\ell}\}$. For fixed full-row-rank linear maps, it is $1-2^{-d}$, where $d$ is their row-space intersection dimension. A nonlinear example shows that an optimal approximate rewrite may change Bob&#x27;s marginal distribution.

  匹配依据：MPC: oblivious transfer

  </details>

- **Threshold Key Encapsulation Mechanisms via MPC: ML-KEM Compatibility and Optimization**
  2026-09-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2220)
  The-Anh Ta, Dongxi Liu, Sid Chau, Jiafan Wang

  <details><summary>摘要 / Abstract</summary>

  There is currently a strong interest in designing standard-compatible threshold cryptographic primitives, a trend bolstered by NIST&#x27;s Call for Multi-Party Threshold Schemes (NIST IR 8214C). While Multi-Party Computation (MPC) can be applied to the construction of threshold Key Encapsulation Mechanism (KEM) from NIST standard ML-KEM scheme to preserve the compatibility with ML-KEM, such a direct construction yields a high number of threshold decapsulation rounds as many as 384 for MK-KEM-512. In this paper, we optimise the round complexity of MPC-based threshold ML-KEM decapsulation. Our first construction (Scheme A) uses masked predicates, parallel coin expansion and global scheduling methods to improve the round complexity of MPC-based ML-KEM decapsulation, while maintaining ML-KEM encapsulation, public key and ciphertext formats. For ML-KEM-512, 768 and 1024, our construction improves the round complexity to 145, 218, and 290, respectively. We also introduce a variant (Scheme B) that uses an MPC-friendly variant of Kyber KEM and KangarooTwelve hash to further improve the round complexity to $35$ at the security level of ML-KEM-512, without full ML-KEM compatibility. In the semi-honest MPC model, we prove Scheme A security by exact composition with ML-KEM, and Scheme B IND-CCA security in the QROM from Module-LWE and negligible decryption failure.

  匹配依据：MPC: multi party computation

  </details>

- **The planted tensor problem over finite fields: algorithms and cryptography**
  2026-09-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.31256)
  Yuxuan Liu, Youming Qiao, Gang Tang, Chuanqi Zhang

  <details><summary>摘要 / Abstract</summary>

  Inspired by the planted clique problem for random graphs, we introduce the planted totally-isotropic space problem for random tensors as follows. Let $U\cong \mathbb{F}_q^n$ and $W\cong \mathbb{F}_q^m$ be finite-dimensional vector spaces over a finite field $\mathbb{F}_q$. Given $d\in \mathbb{N}$, choose a random \(d\)-dimensional subspace \(V\leq U\), and construct a random alternating bilinear map $φ:U\times U\to W$ subject to the constraint \(φ(V,V)=0\). Such a $V$ is known as a totally-isotropic space of $φ$, and the goal is to recover $V$. Building on the recent probabilistic analysis of random tensors (Pham--Qiao--Wigderson--Wigderson, \emph{in progress}), we initiate the study of the algorithmic hardness of this problem. Setting $m=\lceil n/\log n\rceil$, we show that this problem admits an average-case polynomial-time algorithm for $d\geq n/2$, by leveraging recent advances on the non-commutative rank problem. We also show that this problem admits a $q^{O(n\log n)}$-time algorithm. We carry out algorithmic experiments using polynomial-system solving. From these results, we conjecture that the planted totally-isotropic space problem for $d=\lceil n/C\rceil$ with some constant $C\geq 3$ is exponentially hard. Based on this evidence of computational hardness, we explore cryptographic applications of the planted totally-isotropic space problem and related planted tensor problems. We present private simultaneous messages and secret sharing protocols based on planted tensor problems, following the protocols based on planted subgraphs in (Abram--Beimel--Ishai--Kushilevitz--Narayanan, \emph{TCC}&#x27;23). At the same security level, the public information size of protocols based on planted subgraphs is (moderately) exponential in that of protocols based on planted tensors, while the communication costs of these protocols are polynomially related.

  匹配依据：MPC: secret sharing

  </details>

- **Practical Attacks Against EALPN Using Belief Propagation**
  2026-09-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2213)
  Pierre Galissant, Guilhem Jazeron, Léo Perrin

  <details><summary>摘要 / Abstract</summary>

  Weak and shallow pseudo random functions form a new class of symmetric primitives that is seeing a growing relevance, from their use in the initialization phase of some MPC protocols to the internals of some FHE-based protocols. However, their security is hard to ensure: &quot;weak&quot; means that chosen plaintext attacks are irrelevant, and &quot;shallow&quot; means that their construction cannot be round-based: in this exotic setting, how can we define secure PRFs? In this paper, we investigate EALPN, a recent proposal of this type. We identify critical blind spots in the initial asymptotic analysis of the designers: the role of l, one of its parameters, turns out to be crucial. Indeed, we present a key recovery attack with a complexity that is polynomial in all other parameters, and whose complexity grows exponentially but still slowly with l. As a consequence, some parametrizations intended to provide 128 bits of security only offer 37 bits. Our attack is based on novel use of the belief propagation algorithm. Our analysis of its efficiency in our specific setting can be of independent interest.

  匹配依据：MPC: mpc (context)

  </details>

- **Incrementally Verifiable Computation without Extraction**
  2026-09-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2219)
  Abhishek Jain, Surya Mathialagan, Brent Waters

  <details><summary>摘要 / Abstract</summary>

  Incrementally verifiable computation (IVC) [Valiant, TCC &#x27;08] allows one to iteratively prove that a configuration $x_0$ reaches a configuration $x_T$ via $T$ repeated applications of a (possibly non-deterministic) machine $\mathcal{M}$. An IVC scheme is fully succinct if the proof size is independent of both $T$ and the size of the intermediate configurations. In this work, we develop a new indistinguishability obfuscation ($i\mathcal{O}$)-based approach to IVC that avoids the extraction-based security analyses central to prior constructions. Assuming subexponential hardness of $i\mathcal{O}$ and one-way functions, we construct an adaptively sound fully succinct IVC scheme for deterministic computations. This yields the first IVC for deterministic computations that does not rely on algebraic assumptions. Under the same assumptions, we further obtain a fully succinct two-hop IVC scheme for $\mathsf{NP}$ with non-adaptive soundness, allowing one to prove that $x_0$ reaches $x_2$ via an intermediate configuration $x_1$. This is the first IVC scheme for $\mathsf{NP}$ achieving full succinctness. Our constructions are based on a new connection between IVC and secret sharing for $s$-$t$ connectivity in graphs.

  匹配依据：MPC: secret sharing

  </details>

- **Beyond Incentive Compatibility: Rational Harm-Proof Transaction Fee Mechanisms**
  2026-09-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.32005) · [IACR ePrint](https://eprint.iacr.org/2025/2247)
  Forest Zhang, Elain Park, Ke Wu

  <details><summary>摘要 / Abstract</summary>

  Transaction fee mechanisms (TFMs) allocate scarce block space in blockchains. Prior work focuses on incentive compatibility (IC): honest behavior maximizes the payoff of each strategic player. We introduce rational-harm proofness (RHP), which rules out deviations that harm honest participants without reducing the deviator&#x27;s utility relative to honest behavior. IC alone does not exclude such costless harm: in a second-price auction, a losing bidder can raise the winner&#x27;s payment without changing its own payoff. For finite block capacity k, we characterize TFMs satisfying RHP alongside user incentive compatibility (UIC) and miner incentive compatibility (MIC). In the plain model, where a single miner implements the auction, we prove a tight tetrilemma: no TFM simultaneously achieves positive miner revenue, UIC, MIC, and RHP against miner-user coalitions, while any three are jointly achievable. In the MPC-assisted model, where a committee of miners implements the auction using multi-party computation, we construct a randomized TFM with positive miner revenue satisfying UIC, MIC, and RHP against users, miners, and miner-user coalitions containing at most k users. Randomness is necessary to confirm transactions under congestion: any deterministic TFM satisfying UIC and user RHP in this model confirms no transactions when the number of submitted bids exceeds k. Finally, IC and RHP are incomparable for every strategic role in both models: mechanisms can satisfy either property without satisfying the other. These results extend transaction fee mechanism design beyond incentives to protection against costless harm.

  匹配依据：MPC: multi party computation

  </details>

- **A Three-Party W-State Quantum Secret Sharing Protocol with X-Gate Encoding and Forbidden-Outcome Detection**
  2026-09-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.31472)
  Timur R. Teregulov, Elena R. Loubenets

  <details><summary>摘要 / Abstract</summary>

  We develop a new three-party quantum secret-sharing (QSS) protocol based on a three-qubit W state. This protocol encodes the secret-sequence bits using X gates and employs randomly selected Hadamard operations and measurement bases to generate information and security-test rounds. We evaluate the efficiency of the proposed protocol and analyze its security against an internal adversary performing intercept-and-resend and entangle-and-measure attacks, deriving the corresponding detection probabilities. The analysis of the entangle-and-measure attack shows that extracting information through an ancillary system leads to a nonzero probability of forbidden outcomes in the test rounds, thereby enabling the detection of the attack. The proposed protocol is implemented in Python using the Qsikit framework and executed on quantum processors. Its performance is evaluated in terms of the quantum bit error rate (QBER) for information rounds under different secret-bit encoding configurations. The experimental results demonstrate that the QBER depends noticeably on the quantum processor used.

  匹配依据：MPC: secret sharing

  </details>

- **On the Power of Slicing and Dicing: Linear Garbling Beyond Two-Input Gates**
  2026-09-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2200)
  Tianren Liu, Luojian Wei

  <details><summary>摘要 / Abstract</summary>

  Communication is a central efficiency bottleneck in garbled circuits. Rosulek and Roy (CRYPTO 2021) introduced \emph{slicing} and \emph{dicing}, obtaining a garbling scheme in which XOR gates require no communication and each two-input AND gate costs \(1.5\lambda + 5\) bits, where \(\lambda\) is the security parameter. In this work, we investigate the power of these techniques for garbling gates of larger fan-in. We develop a linear-algebraic framework that yields concrete constructions and asymptotic bounds. For three- and four-input gates, we obtain constructions with communication costs $7\lambda/3 + 35$ and $15\lambda/4 + O(1)$ bits, respectively. For arbitrary fan-in \(n\), we give a construction for any single-output gate with communication cost bounded by \(22 \cdot 2^n\lambda/n + 2^n\) bits. Our constructions are compatible with free-XOR, and all hash queries within each gate are nonadaptive. We prove security of the framework in the random-oracle model and under a circular correlation robustness (CCR) condition for any number of slices. We also evaluate simple uses of the three-input construction against the best two-input circuits collected in our experiments, finding evidence of communication savings on control circuits.

  匹配依据：MPC: garbled circuits, garbling scheme

  </details>

- **Fully Anonymous Perfect Threshold Secret Sharing: Explicit One-Bit Construction and Rate Amplification**
  2026-09-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2202)
  Chongxu Ren, Hongbo Yu

  <details><summary>摘要 / Abstract</summary>

  Secret sharing distributes a secret among participants so that only sufficiently large groups can recover it. Fully anonymous secret sharing also allows recovery from share values alone, without participant identities. Below the reconstruction threshold, the shares must look exactly like independent uniform random values, revealing neither the secret nor their holders&#x27; identities. Con, Li, and Mazor established that such schemes with error-free recovery exist for every threshold, leaving an efficient general construction open. We give efficient constructions for every threshold 2 ≤ t ≤ n among n participants. For an L-bit secret, each share has L + O(t² log² n) bits. Sharing runs in expected polynomial time, and reconstruction runs in deterministic polynomial time. Our approach combines an efficient one-bit construction with a general transformation that uses it to protect a short message needed for anonymous reconstruction of a long secret. The additional share length has an upper bound depending only on the number of participants and the threshold. For a fixed participant count and threshold, the rate approaches one as secrets grow longer, while anonymity remains exact and recovery never errs.

  匹配依据：MPC: secret sharing

  </details>

- **SPRUCE: Scalable Multiparty Private Set Union in Constant Rounds**
  2026-09-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2188)
  Zhengwei Tong, Saba Eskandarian, Jonathan Katz, Kartik Nayak

  <details><summary>摘要 / Abstract</summary>

  Multiparty private set union (MPSU) enables a group of mutually distrusting parties, each holding a private set, to learn the union of their sets without revealing additional information. MPSU is a fundamental primitive with applications to privacy-preserving tasks such as cyber-risk assessment and private record matching. State-of-the-art MPSU protocols require parties to sequentially shuffle encrypted values in order to hide which party contributed which inputs to the final result. We introduce a new paradigm for semi-honest MPSU that eliminates the need for such shuffling. This allows the protocol to run in constant rounds regardless of how many parties are involved. The resulting protocol also benefits from improved parallelism, an information-theoretic online phase, and native support for unbalanced input sizes, a situation most prior works must handle by padding inputs to hide individual input sizes. We implement and evaluate our protocol across a range of party counts, input sizes, and network conditions. In the unbalanced setting, where parties hold unequal-sized inputs, our protocol significantly outperforms the state-of-the-art schemes PULSE (CCS ’25) and DZBC25 (USENIX Security ’25). In the balanced setting, it achieves an order-of-magnitude improvement over PULSE in most settings and outperforms DZBC25 in WAN deployments with 100ms latency.

  匹配依据：MPC: private set union

  </details>

- **Physalia: Redistribution-Resistant Content Protection for Decentralized Storage**
  2026-09-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.28277)
  Giacomo Giuliari, Karl Wüst

  <details><summary>摘要 / Abstract</summary>

  In decentralized storage systems, access control is often implemented by encrypting the data before upload and sharing the decryption key with authorized parties. A leaked key, however, makes the data publicly accessible, which lowers the barrier to content piracy below that of traditional systems, where piracy requires redistributing the full data. We present Physalia, an end-to-end access-control system for decentralized storage that secret-shares the data itself, instead of just the key, across multiple servers. Leaking the data then requires transmitting it in full: We formalize this intuition and introduce the redistribution bandwidth an adversary must pay to leak protected content and show that Physalia raises it to the size of the data. Sharing across untrusted servers requires robustness against corrupted shares. We develop a robustness transform that turns any computational secret sharing scheme into a robust one and which is of independent interest. In contrast to existing schemes that rely on error correction, it uses signatures with ephemeral keys and adds only constant-size metadata per share. We show that this transform is secure and evaluate Physalia end-to-end on the Walrus decentralized storage system with an on-chain access policy.

  匹配依据：MPC: secret sharing

  </details>

- **Credible AUctions via MPC Gadgets: Bounding Information Leakage Under Abort**
  2026-09-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.27402)
  Matheus Venturyne Xavier Ferreira

  <details><summary>摘要 / Abstract</summary>

  The design of credible auctions---mechanisms where a revenue-maximizing auctioneer has no incentive to deviate from the protocol---faces a fundamental cryptographic barrier when the auctioneer controls shill bidders. While a natural approach is to use Secure Multi-Party Computation (MPC) to remove the trusted auctioneer, the impossibility of fair coin flipping of Cleve (1986) implies that monolithic MPC protocols grant the auctioneer a &quot;free option&quot;: they can learn the auction&#x27;s outcome and unilaterally abort if the revenue is unsatisfactory. Cryptographic commitments with ex-ante penalties mitigate this abort asymmetry, but no finite penalty suffices for heavy-tailed distributions. We circumvent this barrier by introducing the MPC Decomposition Principle. Rather than encrypting the entire mechanism, we use MPC strictly as an information-restriction tool. We isolate the winner determination problem into a minimal MPC gadget that computes and reveals the winner&#x27;s identity but no payment information. This qualitative restriction mathematically bounds the information leaked upon an abort. By combining this gadget with sequential revelation and finite economic penalties, we design the Sequential Revelation Auction (SRA). We prove that bounding the information leakage strictly bounds the value of the free option, showing that a penalty of $k \geq \sum_{i=1}^n Rev(F_i)$ is sufficient for credibility, and tight: for equal-revenue distributions, every smaller penalty admits a profitable deviation. Using constant-round MPC, the SRA resolves an open question of Akbarpour and Li (2020) and Ferreira and Weinberg (2020) by providing a constant-round, incentive-compatible, revenue-optimal credible auction for all product distributions with vanishing revenue tails

  匹配依据：MPC: secure multi party computation

  </details>

- **Budgeted Threshold Signatures: Protocol-Native Spending Limits with Zero On-Chain Footprint**
  2026-09-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2176)
  Huaifeng Chen, Yuchang Zhang, Yu Cheng

  <details><summary>摘要 / Abstract</summary>

  Spending limits are the workhorse of custody policy, yet in every deployed threshold-signing stack they live outside the signing protocol—in centralized policy engines, on-chain covenants, or hardware co-signers—where they leak budget state, bind to a single chain, or add a trusted bypass surface. The workload is compounding: agent payments passed one hundred million transfers on a single chain in under a year. We initiate the study of protocol-native spending limits: per-epoch budgets secret-shared among the signers and enforced inside the signing session, with unchanged on-chain verification. We first show that the natural approach fails: gating a threshold signature with a passively secure MPC comparison admits a deterministic bypass. For the class of linear gatein-combination protocols we prove that every member signs over-budget transactions with probability one, disguised against any transcript auditor up to the statistical masking bound. We then construct BTS, a budgeted threshold Schnorr scheme with a formal budget-soundness definition for honest-majority configurations. The gap is closed with an authenticated gate: in implementation, every attack attempt is caught before a signature is produced, at a measured cost of 3.4–3.7× multiplications and five extra rounds. Batched over k=20 payments, enforcement amortizes to about one network round trip per payment in our WANmodeled prototype.

  匹配依据：MPC: mpc (context)

  </details>

- **Argo: Leaking a Secret from an Invalid Groth16 Proof**
  2026-09-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2165)
  Liam Eagen, Ying Tong Lai

  <details><summary>摘要 / Abstract</summary>

  We present Argo, a randomized encoding scheme for the invalidity of pairing-based SNARKs like Groth16. Argo allows an encoder to encode a proof such that a decoder can derive a secret if the proof is invalid. We prove the selective security of invalidity Argo, as well as the adaptive security of validity Argo, under DDH in one source group of a bilinear pairing in the standard model, a standard assumption that holds in the generic group model used to analyze Groth16. We show how to couple invalidity Argo with a projective garbling scheme like Argo MAC or Duty-Free Bits to construct a garbled circuit for Groth16 invalidity as a function of the proof bits, and how to use it with BitVM to construct a permissionless, optimistic Groth16 verifier for Bitcoin: a decoder proves a proof invalid by publishing a secret, and the decoder can be anyone, not necessarily known in advance. When instantiated with BN254, Argo has an offline encoding size of about 21 kB, a thousand times smaller than the projective garbling scheme, and an end-to-end protocol size more than three orders of magnitude smaller than existing Yao-based approaches. Generating an Argo + Argo MAC garbled circuit takes tens of milliseconds on a laptop, compared to minutes for a Yao GC. Argo is the first protocol that makes permissionless, optimistic SNARK verification on Bitcoin practical.

  匹配依据：MPC: garbled circuit, garbling scheme

  </details>

- **I Prove, Therefore I Am: Spatiotemporal Multi-Party Computation**
  2026-09-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.26448) · [IACR ePrint](https://eprint.iacr.org/2026/2118)
  Ziqing Guo, Fuyuki Kitagawa, Xiao Liang

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) enables mutually distrustful parties to compute on private digital inputs. We initiate the study of spatiotemporal MPC, extending this paradigm to functionalities whose inputs additionally depend on physical facts such as the parties&#x27; locations, times, or trajectories. Such protocols must simultaneously hide spatiotemporal information and ensure its physical consistency: a malicious party should not be able to make the functionality operate on a spatiotemporal input inconsistent with its actual physical state. The main conceptual challenge is to formulate extraction of spatiotemporal information within the simulation-based security framework. We introduce arguments of spatiotemporal knowledge, following the principle &quot;I prove, therefore I am:&quot; rather than defining physical presence directly through a mathematical relation, we define it operationally through the ability to complete a sound spatiotemporal verification protocol. Accordingly, an extractor recovers a spatiotemporal point from a successful prover and certifies its physical validity by using the extracted prover to succeed in an auxiliary spatiotemporal verification protocol. Building on this notion, we define universally composable (UC) security for spatiotemporal MPC, capturing privacy, physical consistency, and composability. We provide constructions achieving this new MPC notion. We first construct UC-secure commit-and-prove of spatiotemporal knowledge: in the CRS model under LWE against quantum provers without pre-shared entanglement, and in the QROM against quantum provers with unbounded pre-shared entanglement. Using these protocols, we obtain UC-secure spatiotemporal MPC from semi-honest post-quantum MPC. We also extend our framework to support quantum functionalities with classical spatiotemporal input.

  匹配依据：MPC: multi party computation, secure multiparty computation

  </details>

- **Fully Anonymous Perfect Secret-Sharing**
  2026-09-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2145)
  Roni Con, Ray Li, Noam Mazor

  <details><summary>摘要 / Abstract</summary>

  Fully anonymous secret-sharing schemes ensure two properties at once: for any fixed secret, the combined shares of every unauthorized set of participants are uniformly random, and every authorized set can reconstruct the secret exactly using only the share values, without needing to know which participant holds which share or in what order the shares appear. It was previously open whether such schemes exist for nontrivial exact-threshold parameters 2 &lt; t &lt; n. For the smallest previously open threshold, t= 3, we give, for every n≥4, an explicit fully anonymous scheme for one-bit secrets, with 2⌈log n⌉-bit shares and a perfect reconstruction algorithm running in poly(log n) time. The next result, found by ChatGPT, shows that for every 1 ≤t ≤n there exists a fully anonymous perfect (t,n) threshold secret-sharing scheme for one-bit secrets, in which each share has length O(tlog n) bits. The proof is purely existential and does not provide an efficient construction. Moreover, ChatGPT identified a simple construction of a fully anonymous perfect scheme for every access structure A; if A contains ℓ authorized sets, then each share consists of ℓ2 bits. The authors subsequently verified and streamlined the proofs on their own and take full responsibility for their correctness.

  匹配依据：MPC: secret sharing

  </details>

- **Cryptographic Security Is Not Enough: Privacy Gaps in the Renegade Decentralized Dark Pool**
  2026-09-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.27100)
  Prerna Arote, Adrian Saiz, Oriol Saguillo, Lucianna Kiffer

  <details><summary>摘要 / Abstract</summary>

  Dark pools are designed to provide pre-trade privacy, liveness, and post-trade confidentiality - concealing order flow before execution and limiting information leakage after. Decentralized dark pools, such as Renegade, aim to replicate these properties without custodial risk, using secure multi-party computation (MPC) and zero-knowledge proofs for private order matching and verifiable settlement. We show that Renegade&#x27;s cryptographic guarantees do not deliver these dark pool properties in practice. MPC-with-abort ensures correctness but not fairness: a party may learn the match result and abort without penalty, breaking pre-trade privacy. We demonstrate that the protocol&#x27;s discovery layer further leaks trading intent before MPC even begins, and that sustained probing via selective abort can probabilistically reconstruct counterparty order history, threatening post-trade confidentiality. We also show that the absence of input-consistency checks prior to MPC execution enables a griefing attack using invalid state commitments requiring no real token holdings that continuously locks honest users&#x27; wallets and wastes compute, breaking liveness under sustained conditions. We further analyze over 700,000 Renegade transactions on Base and probe the P2P layer, finding that the network is effectively centralized: 88% of traffic routes through a handful of relayers, with only four nodes sustaining the P2P layer. Since relayers hold their users&#x27; wallet state in plaintext, this concentration means the system operates as a centralized orderbook in practice - reproducing off-chain the information asymmetry that dark pools are designed to eliminate. Together, our results show that cryptographic privacy does not imply dark pool security: pre-trade privacy, liveness, and post-trade confidentiality each require additional protocol-level guarantees beyond MPC correctness.

  匹配依据：MPC: secure multi party computation

  </details>
