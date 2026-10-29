# 2026 · MPC · 仅预印本来源 · 第 2/6 页

[总目录](../PAPERS.md) · [上一页](2026-mpc-preprint-01.md) · [下一页](2026-mpc-preprint-03.md)

- **Batch IT-MAC: Program the Randomness in Succinct VOLE**
  2026-09-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2159)
  Liqiang Liu, Tianren Liu

  <details><summary>摘要 / Abstract</summary>

  Many cryptographic protocols rely on affine message authentication tags of the form \({\boldsymbol\sigma}=\Delta{\boldsymbol x}+{\boldsymbol k}\), the batch version of information-theoretic MAC. Generating the tags for a long message vector typically requires communication linear in its length. Recent chosen-input VOLE protocols achieve succinct communication, but do not allow the authenticator’s key $k$ to be fixed in advance. We introduce $\mathit{batch\text{-}MAC}$, a primitive that authenticates a chosen message vector in two messages while allowing the authenticator’s key vector to be generated beforehand from a short seed. For a vector of length \(m\), we construct batch-MACs with \(O(m^{2/3}\lambda)\) communication under the decisional composite residuosity (DCR) assumption and \(\operatorname{poly}(\log m,\lambda)\) communication under the learning with errors assumption. Both constructions require a common reference string (CRS). We find applications in constrained pseudorandom functions, 2-message 2PC, and succinct zero-knowledge arguments.

  匹配依据：MPC: 2pc (context)

  </details>

- **United: Shuffle-Free Multiparty PSU via Oblivious Invertible Sketches**
  2026-09-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2132)
  Truong Son Nguyen, Lucas Piske, Ni Trieu

  <details><summary>摘要 / Abstract</summary>

  Multiparty Private Set Union (MPSU) allows multiple parties to compute the union of their private sets while revealing no additional information beyond the prescribed output. Existing practical MPSU protocols typically manipulate individual elements and rely on a distributed shuffle to hide element ownership, introducing an $O(n)$ round-complexity bottleneck. We present United, a shuffle-free MPSU framework based on a new data-structure abstraction, Oblivious Insert-Only Invertible Sketches (OIIS). Rather than anonymizing an element-wise intermediate representation, the parties directly construct a protected symmetric sketch of the union. Conditional oblivious insertion ensures that each distinct union element is inserted exactly once while hiding the insertion condition and modified locations. We provide two realizations of OIIS. Our HE-based construction instantiates OIIS with a standard Invertible Bloom Lookup Table protected by multi-key partially homomorphic encryption, while our MPC-based construction uses additive secret sharing and introduces a new row-local power-sum OIIS technique for efficient conditional insertion. We implement and evaluate both constructions. Across the evaluated configurations, our MPC-based construction achieves up to $3.10\times$ lower runtime in LAN settings, while our HE-based construction achieves up to $2.73\times$ lower runtime in WAN settings compared with prior MPSU protocols.

  匹配依据：MPC: private set union, secret sharing

  </details>

- **Continuum: Concretely Efficient Asynchronous Dynamic MPC with Guaranteed Output Delivery**
  2026-09-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2122)
  Wenxuan Yu, Minghui Xu, Yuan Lu, Yingzi Gao, Xiuzhen Cheng

  <details><summary>摘要 / Abstract</summary>

  Traditional secure multiparty computation (MPC) protocols assume a fixed set of participants throughout the computation. Dynamic MPC (DMPC) relaxes this assumption by permitting parties to join or leave during the process. However, practical deployment of DMPC in Internet settings favors tolerating asynchrony and achieving guaranteed output delivery (GOD). Recently, AD-MPC [CCS 2025] introduced an asynchronous DMPC (ADMPC) achieving this goal, but its reliance on per-epoch preprocessing and masking randomness incurs substantial concrete overhead. In this paper, we present Continuum, a concretely efficient ADMPC protocol with GOD. We introduce an aggregated hand-off protocol that ensures transfer consistency across epochs while eliminating per-epoch masking randomness, and a batch multiplication protocol based on the BGW paradigm that defers degree reduction to the hand-off phase and aggregates verification for all multiplications into succinct proofs. Together, these protocols enable a non-interactive computation phase with interaction concentrated in an efficient hand-off phase, overcoming the primary concrete inefficiencies of prior ADMPC designs. We implement Continuum and evaluate its performance on up to 128 geographically distributed servers. In experiments on 22 servers with circuits of depth 6 and width 100, Continuum reduces linear-gate transfer latency from 76.60s to 15.13s (80% reduction) and multiplication-gate evaluation time from 476.62s to 35.67s (93% reduction), compared with AD-MPC, while preserving strong security guarantees.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Post-Quantum PKE and More from a Noisy Unstructured Linear Algebraic Assumption: Beyond LWE and LPN**
  2026-09-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2113)
  Riddhi Ghosal, Paul Lou, Amit Sahai

  <details><summary>摘要 / Abstract</summary>

  Noisy linear algebraic assumptions (NLAs), such as $\mathsf{LWE}$ and Alekhnovich’s $\mathsf{LPN}$, have long served as the most reliable sources of post-quantum hardness. However, a series of recent classical attacks on assumptions once believed to be quantum-secure, coupled with the rapid progress in quantum technology, underscores the urgent need for assumptions that are plausibly hard even if both $\mathsf{LWE}$ and $\mathsf{LPN}$ turn out to be broken. A fascinating recent work of Ghosal et al. (Eurocrypt 2025) takes an important first step in this direction, constructing a PKE scheme by combining two NLAs that remain plausibly secure even if $\mathsf{LWE}$ and Alekhnovich’s parameter regime for $\mathsf{LPN}$ were to be polynomially broken. A critical weakness of their work, however, is that it is still $\mathsf{LPN}$-broken: namely, an oracle that breaks $\mathsf{LPN}$ with $n^{-\delta}$ noise rate can break their NLA, for some $\delta&gt;0$. We ask: can this barrier be overcome? We answer this question positively, by introducing an NLA that is plausibly hard given an oracle that breaks even constant noise rate $\mathsf{LPN}$, while still being plausibly hard given an oracle that breaks $\mathsf{LWE}$. Along the way, we improve upon the work of Ghosal et al. significantly in several dimensions. Specifically, we introduce a single new natural NLA and provide constructions of (i) public-key encryption and (ii) two-round maliciously secure oblivious transfer protocol from this single assumption. We also construct a one-time circular-secure secret-key encryption from a binary variant of this assumption. Our assumption takes the form $(\mathbf{A}, \mathbf{A}\mathbf{s} + \mathbf{e})$, where $\mathbf{A}$ is a random unstructured square matrix, the secret $\mathbf{s}$ has short and sparse entries, and the error $\mathbf{e}$ is a mixture of two components: a small-but-dense error combined with a large-but-sparse error. We provide a comprehensive initial cryptanalysis, ruling out (1) efficient combinatorial attacks that exploit sparsity such as information set decoding, (2) dimension reduction attacks, and (3) dual lattice attacks. We also prove, via a reduction, that our assumption, and its binary variant, is at-least as hard as $\mathsf{LWE}$. Additionally, we show that for a broad range of parameters including those used by our constructions, our assumption does not appear to fall within the class of “lattice” assumptions, that is, there seems to be no reduction to approximate shortest vector problem solvers, and, crucially, it is plausibly hard even given an oracle that breaks $\mathsf{LPN}$ for any noise density parameter.

  匹配依据：MPC: oblivious transfer

  </details>

- **Actively Secure PPML with Soft-Boundary Overflow Detection**
  2026-09-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2105)
  Yuntian Chen, Tianpei Lu, Keyu Ji, Zhiyuan Ning, Zhanyong Tang, Cong Wang

  <details><summary>摘要 / Abstract</summary>

  MPC-based privacy-preserving machine learning (PPML) typically operates over finite rings rather than floating-point arithmetic, making arithmetic overflow an inherent risk. Existing overflow-detection techniques generally require the evaluation of nonlinear functions, resulting in substantial computation and communication overhead. We propose Soft Boundary Detection, which reduces boundary verification to probabilistic functions over partitioned intervals, with a cost comparable to that of linear computation. Building on this abstraction, we develop an efficient mechanism for detecting arithmetic overflow in PPML workloads. Moreover, we show that Soft Boundary Detection naturally extends to the malicious-adversary setting. In ring-based computation, it further avoids the need to choose a ring space substantially larger than the actual data range to ensure soundness against malicious behavior. Our framework provides two key benefits: (1) highly efficient arithmetic overflow detection, and (2) active security without requiring ring extension or enlarging the underlying ring space. Experimental results demonstrate that our approach substantially strengthens security while retaining high efficiency, providing a practical solution for robust and actively secure PPML.

  匹配依据：MPC: mpc (context)

  </details>

- **Period-Aligned Secure Cosine Evaluation Based on Two-Party Computation**
  2026-09-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2079)
  Qingyu Mo

  <details><summary>摘要 / Abstract</summary>

  The cosine function is widely used in machine-learning applications, but evaluating it on secret-shared data is difficult. Conventional approaches use polynomial approximations or lookup tables, whose costs grow substantially over large input domains. More recent protocols first reduce the private input modulo the cosine period, but securely performing this modular reduction also incurs significant cost. We present a period-aligned two-party cosine protocol. Based on the cosine addition rule, it rescales each share so that a wrap of the input modulus corresponds to a full $2\pi$ period and therefore does not change the recombined cosine. Each party evaluates sine and cosine locally on its share, while the secure computation uses only two cross-party products and one fixed-point output conversion. We evaluate the protocol directly on synthetic inputs and within private RFF-based RBF-SVM prediction. Comparisons with the protocol of Xing et al. (NDSS 2025) and Guo et al. (USENIX Security 2026) demonstrate better efficiency of our proposed protocol.

  匹配依据：MPC: secure computation, two party computation

  </details>

- **Is it safe to lie? Revisiting Incoercible Multi-Party Computation in the Universal Composability Framework**
  2026-09-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2089)
  Saskia Bayreuther, Robin Berger, Eva Hetzel, Jörn Müller-Quade

  <details><summary>摘要 / Abstract</summary>

  In a multi-party protocol, incoercibility aims to protect protocol participants by allowing them to use their honest inputs even in the presence of a coercer. A coercer is an adversary who pressures protocol parties into deviating from the protocol. One goal of an incoercible protocol is that the coercer cannot distinguish if the coerced party obeys their command or is deceiving: The coerced party should be able to plausibly deny their deception to ensure their safety. In the past, several attempts at modeling incoercibility in the Universal Composability framework have been made. In Alwen, Ostrovsky, Zhou, and Zikas’ model (CRYPTO 2015), the deception is modeled as a mapping of protocol messages that are sent and received by the coerced party beyond the reach of the coercer. Similar to proofs in plain UC, in order to prove the incoercibility of a protocol, one shows the indistinguishability of ideal and real worlds. Alwen et al.’s incoercibility definition makes use of four worlds: In both the ideal and the real worlds either coercion or deception takes place. If the environment can neither distinguish between the two coercion worlds nor between the two deception worlds for all ideal deception strategies, the protocol incoercibly UC-realizes the ideal functionality. While this shows that it is always possible for a coerced party to deviate from the coercer’s instructions and deceive them, it does not cover if this deception can be detected by the coercer. In this paper, we tackle the question how the perceived difference between deception and coercion can be modeled in UC. In particular, we make the following contributions. First, we refine the incoercibility notion by Alwen et al. by limiting the deception strategies to ones that allow the coerced party to plausibly deny the deception. We propose a multi-party computation protocol, derived from the one presented by Alwen et al., that fulfills this notion. The protocol uses hardware tokens to make UC-protocols, now including reactive functionalities, incoercible, where coerced parties can deceive the coercer about inputs as well as outputs. Secondly, we define a notion for plausible deniability, which we call Γ-deniability, and show that when the evaluated function is a differentially private mechanism, the deceiving party can plausibly deny their actions.

  匹配依据：MPC: multi party computation

  </details>

- **Garbling Groth16 with Native Group Operations**
  2026-09-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2100)
  Nakul Khambhati, Aaron Feickert, Christian Lewe, Mukesh Tiwari

  <details><summary>摘要 / Abstract</summary>

  The Groth16 verification equation has a compact algebraic description, yet garbling its Boolean implementation can require tens of gigabytes. We show how to garble this computation using native elliptic-curve group operations. Motivated by proof verification in trust-minimized Bitcoin bridges, we construct a projective partial garbling scheme for conditional disclosure on invalid Groth16 proofs. For a fixed verification key and public statement, evaluation reveals a garbler-held secret when the supplied proof is invalid and hides the secret when it is valid. The proof itself remains public. The main technical challenge is handling a pairing whose two arguments are supplied by the evaluator. We introduce a rekeying gadget that resolves this using a single private scalar multiplication. Building on Argo MAC (Eagen and Lai, 2026), BABE (Garg et al., 2026), and Duty-Free Bits (Khambhati et al., 2026), we prove a composition theorem for partial garbling across input representations and apply it to transform group encodings into bitwise projective encodings. This requires extending the projectivization technique of Duty-Free Bits to quadratic extension fields. The resulting garbled program has size $O(\lambda^2)$ bits, where $\lambda$ is the computational security parameter. We prove privacy under the decisional Diffie-Hellman assumption, in the random oracle model. Our BN254 implementation produces a 2.4 MiB garbled program, including projectivization, compared with the 48 GB reported for Boolean garbling of Groth16. Thus, we improve over prior state of the art in Groth16 garbling by over four orders of magnitude.

  匹配依据：MPC: garbling scheme

  </details>

- **Dynamic Participant Updates to Access and Adversary Structures for Ideal Secret Sharing Schemes Based on Linear Codes**
  2026-09-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2086)
  Xu Qiuxia, Tang Chunming, Yi Zongxiang

  <details><summary>摘要 / Abstract</summary>

  The paper investigates secret sharing schemes based on linear codes, focusing primarily on the access structures and adversary structures arising from dynamic participant updates, as well as on whether such access structures can be realized by ideal linear secret sharing schemes. First, we characterize the maximal adversary structure corresponding to the access structure obtained by adding new participants to every authorized subsets of a given access structure.Second, we prove that the original access structure can be realized by a linear code $C(n+1)[n+1,k;q]$ if and only if the access structure obtained after adding $\ell$ new participants can be realized by a linear code $C(n+\ell+1)[n+\ell+1,k+\ell;q]$. In addition, we establish the correspondence between the codewords of these two linear codes. Furthermore, We prove that the original access structure can be realized by an ideal secret sharing scheme if and only if the expanded access structure can be realized by one as well. Finally, we demonstrate that every linear secret sharing scheme realizing a disjoint access structure is ideal. We also prove that access structures whose any two minimal authorized subsets share all but one participant can be realized by an ideal linear secret sharing scheme. In addition, we determine the adversary structure corresponding to this class of access structures. More generally, we obtain the maximal adversary structure when new participants are added to merely part of the minimal authorized subsets.

  匹配依据：MPC: secret sharing

  </details>

- **Critical sets of Latin squares based on autoparatopisms**
  2026-09-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.21532)
  Manuel González-Regadera, Raúl M. Falcón, María Dolores Frau

  <details><summary>摘要 / Abstract</summary>

  In cryptography, critical sets of Latin squares have particularly been implemented to design secret sharing schemes. A main problem in these cryptographic protocols arises from absent holders of pieces of information that are common to different critical sets, because they become indispensable to recover the secret. This paper solves this problem by making use of the orbits of entries described by the autoparatopism group of the Latin square under consideration. To this end, we introduce the more general problem of computing critical sets of Latin squares having a given paratopism in their autoparatopism group. These critical sets depend only on the conjugacy class of the autoparatopism and the main class of the Latin square under consideration. Based on this fact, as an illustrative example, we determine the smallest and largest sizes of critical sets associated with autoparatopisms of Latin squares of order up to six. We implement this approach in the design of a new secret sharing scheme.

  匹配依据：MPC: secret sharing

  </details>

- **On the Leakage of Massey Secret Sharing Schemes under Linear Computations**
  2026-09-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.19929)
  Nadja Aoutouf, Daniel Augot

  <details><summary>摘要 / Abstract</summary>

  Leakage attacks on secret sharing schemes exploit partial information about individual shares to recover the underlying secret. In coding theory, linear exact repair schemes (LERSs) enable the recovery of one codeword symbol from a small amount of information obtained from the remaining symbols, provided that the code has sufficiently low rate. This can be interpreted as recovering the secret from partial information, namely subfield symbols, of the shares. Recently, a randomized construction based on subfield subcodes was proposed for constructing LERS-derived leakage attacks against Massey secret sharing schemes based on general linear codes. We extend this framework to multiple shared secrets whose corresponding shares are related through linear computations, with leakage also allowed on the computation outcomes. More precisely, we consider N secrets, of which K $\le$ N are linearly independent input values and the remaining N -K secrets are determined by linear computations on these inputs. We analyse the existence of LERS-derived leakage that exploits this structure. We first study the case of addition and then generalize our construction to arbitrary linear computations. Our analysis applies to general linear codes of length n+1 and dimension k over F\_{q^m} with k $\le$ N n/(Km), and supports arbitrary linear computations, whereas the previous subfield subcode construction only applies to k $\le$ n/m -1. Consequently, exploiting the linear relations enables LERS based leakage which extend the range of code parameters vulnerable to such attacks. Finally, identical leakage functions can arise for certain linear relations, making this a more realistic yet still potentially powerful attack model. Finally, simulations indicate that identical leakage functions can be used for certain linear relations, yielding a more realistic attack model.

  匹配依据：MPC: secret sharing

  </details>

- **Observation of multiphoton entanglement in resonance fluoresce**
  2026-09-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.19808)
  Xiao-Long Zhou, Jian Wang, Ze-Min Shen, Dong-Yu Huang, Si-Jian He, Qi-Yang Huang, Yi-Jia Liu, Yu-Shu Chen, Quan Jiang, Chuan-Feng Li, Guang-Can Guo

  <details><summary>摘要 / Abstract</summary>

  Resonance fluorescence, the process in which a single two-level quantum emitter interacts with a near-resonant coherent light, is a cornerstone of quantum optics as a paradigmatic light-matter interaction. Quantum phenomena in resonance fluorescence have been accounted for in terms of one- and two-photon processes; however, the physical processes arising from the interaction of a single two-level atom with higher photon numbers remain unexplored experimentally. Here we experimentally reveal the multiphoton scattering nature of resonance fluorescence, which intrinsically gives rise to multiphoton entanglement. By accessing quantum fluctuations in the field emitted from a cavity-quantum electrodynamics system, we resolve third- and fourth-order photon scattering events from a single two-level atom. In the three-photon component, the scattered photons are shown to be genuinely energy-time entangled, as verified by a violation of Svetlichny&#x27;s inequality. As a demonstration of an application, a quantum secret sharing protocol (QSS) is implemented using this entangled photon source. Our study refines the descriptive framework of resonance fluorescence and broadens the scope of its investigation. It also establishes a fundamentally simple route for generating multiphoton entangled states for quantum information processing and quantum metrology.

  匹配依据：MPC: secret sharing

  </details>

- **SEEK: Secure and Efficient Encrypted Keyword Search For Privacy-Preserving Messaging Protocols**
  2026-09-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.18459)
  Soumyadyuti Ghosh, Michail Maniatakos

  <details><summary>摘要 / Abstract</summary>

  Encrypted communication protects sensitive user data but can facilitate harmful or unlawful exchanges, creating a trade-off between detecting dangerous messages and preserving end-user privacy. To address this, we propose SEEK, a practical and efficient encrypted keyword-search protocol for privacy-preserving messaging that combines homomorphic encryption with secure two-party computation (2PC). SEEK first partitions messages into ciphertext fragments with the minimum sufficient overlap, then homomorphically correlates them using encrypted keyword trapdoors. For long messages, this design can reduce sender-side encryption and upload overhead by up to two orders of magnitude over state-of-the-art baselines. It supports ASCII case-insensitive matching with one fixed-size encrypted trapdoor and one homomorphic multiplication per fragment, yielding up to 5.47x faster correlation computation than the strongest fragmentation-based baselines. SEEK then invokes 2PC-based selected decoding, blinded zero testing, and secure aggregation, revealing only the keyword presence-or-absence bit while hiding the keyword, its length, message contents, match counts, and locations. SEEK achieves 100% accuracy under case variations that result in exact-matching failures, without requiring additional trapdoors or online communication. We further realize SEEK as an end-to-end web and cross-platform mobile application. Prototype evaluation on a weekly messaging history yields an online computation time of 1.92 s per search, demonstrating the practical feasibility and efficiency of SEEK.

  匹配依据：MPC: secure two party computation

  </details>

- **On Aborts in Differential Privacy**
  2026-09-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2059)
  Fredrik Meisingseth

  <details><summary>摘要 / Abstract</summary>

  There is a growing literature on differential privacy (DP) in multiparty protocols, enabling use in distributed settings and reduced trust assumptions. A largely overlooked aspect of such protocols is the extent to which an adversary can undermine the DP guarantees by making the protocol abort. Another is the DP properties of the honest parties&#x27; outputs. We initiate the study of both these issues. First, we propose an idealized model of aborts, where an aborter is leaked some information about a DP mechanism execution and then chooses whether or not to let an independent malicious analyst learn the mechanism output. We bound the effects of aborts according to what information (the database, randomness, output, or any combination of these) is leaked. These bounds are not only applicable to multiparty DP via general-purpose multiparty computation (MPC) but may also be used in the analysis of other methods to certify DP properties of a protocol. Second, we apply these bounds to analyze ideal protocol executions in MPC. We show, for the first time, that the ideal execution with fairness gives strictly stronger DP guarantees than that for security-with-abort, for the outputs to the honest parties. Further, solitary-output functionalities satisfy guarantees similar to those of the execution with fairness. Finally, we analyze multiparty protocols with respect to the way in which they realize the respective ideal functionalities. We show that partially fair and fully fair protocols have very similar DP guarantees. Since partial fairness, as opposed to full fairness, can be achieved in dishonest-majority settings, and in particular the two-party setting, this opens up for enhanced DP guarantees in two-party computation.

  匹配依据：MPC: multiparty computation, two party computation

  </details>

- **Improved lower bounds for decomposable randomized encoding**
  2026-09-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.18020)
  Justin Holmgren, Kewen Wu

  <details><summary>摘要 / Abstract</summary>

  A decomposable randomized encoding (DRE) for a function $f$ allows $n$ parties, using shared randomness, to encode their individual inputs locally so that the collection of encodings reveals $f(x_1,\ldots,x_n)$ and nothing else. DREs are widely used in efficient multiparty computation. Their main complexity measure is size, the total bit length of the local encodings. Yet the optimal DRE size remains poorly understood even for the $n$-bit OR function. We prove the first superlinear lower bound for OR and, more generally, for every non-periodic symmetric function. Under an additional symmetry assumption, we prove a sharp $Ω(n\log n)$ lower bound for OR, matching the classic construction of Feige, Kilian, and Naor (STOC 1994). We also prove the first $Ω(n^2)$ lower bound on DRE size for non-explicit Boolean functions.

  匹配依据：MPC: multiparty computation

  </details>

- **Differential Trust: Dynamic Multi-Authority Anonymous Credentials with Epoch-Weighted Updates**
  2026-09-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.18811)
  Chen Li, Jianting Ning, Xiulong Liu, Yulin Liu

  <details><summary>摘要 / Abstract</summary>

  Anonymous credentials (ACs) are fundamental to privacy-preserving authentication, allowing users to prove possession of attributes without revealing their identities. State-of-the-art ACs distribute credential issuance across multiple authorities, typically employing techniques such as Shamir&#x27;s secret sharing or aggregate signatures. While this approach enhances system robustness and eliminates a single point of failure, it treats all authorities equally in the credential issuance phase. This uniform treatment disregards the varying levels of trustworthiness or stake held by different authorities. Such a limitation has become particularly problematic in modern decentralized systems like Proof-of-Stake networks, where the inherent trust differentiation among nodes cannot be leveraged in the credential issuance process. To address this limitation, we propose the notion of Multi-Authority Anonymous Credentials with Epoch-Based Weights (MA-ACEW), the first Multi-Authority Anonymous Credential (MA-AC) model that considers authorities&#x27; weight distribution in credential issuance. Crucially, MA-ACEW enables efficient credential updates when authority weight distributions change across epochs. The core of MA-ACEW is our novel Epoch-Bound Pointcheval-Sanders Signature (EB-PS) primitive, which binds signatures to specific time epochs. This temporal binding enables both weight-based credential issuance within epochs and efficient non-interactive credential updates across epochs. We formalize the EUF-eCMA unforgeability requirement for EB-PS and prove our construction satisfies it under a novel STB-GPS assumption. We then prove that our MA-ACEW construction achieves unforgeability, anonymity, and blindness. Finally, we present benchmarks demonstrating the efficiency of EB-PS and MA-ACEW. Remarkably, presenting a credential aggregated from 128 partial ones takes only 10.68 ms on average.

  匹配依据：MPC: secret sharing

  </details>

- **Weighted Batch Threshold Encryption with Efficient DKG**
  2026-09-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2053)
  Alexander Frolov, Aditi Partap, Max Resnick, Ertem Nusret Tas

  <details><summary>摘要 / Abstract</summary>

  Batch threshold encryption allows a committee to decrypt a selected batch of ciphertexts using one short pre-decryption key per party, while ciphertexts outside the batch remain private. This makes batch threshold encryption attractive for building encrypted mempools for blockchains, where validators reveal transactions selected for a block while pending transactions remain private. However, in proof-of-stake systems like Solana or Ethereum, authorization depends on each validator&#x27;s stake, which motivates a weighted version of batch threshold encryption. Naive approaches to weighting existing batch threshold encryption schemes lead to communication costs proportional to the weight assigned to each party. Existing schemes that avoid this cost either associate every ciphertext with a batch label or an encryption-time index. We present the first weighted batch threshold encryption schemes that require neither batch/epoch labels nor encryption-time ciphertext indices, while keeping each party&#x27;s communication independent of its weight. We obtain two constructions by virtualizing prior schemes: the BTX construction of Agarwal et al. and the partial-fraction construction of Boneh et al. In both schemes&#x27; decryption procedures, each party communicates a single group element for an entire batch, regardless of its assigned weight. We prove correctness, robustness, and security under weighted variants of the original schemes&#x27; assumptions, and analyze the assumptions in generic bilinear groups. For the BTX-based construction, we also give a specialized distributed key generation protocol that avoids the general purpose MPC-based setup required by the previous state-of-the-art schemes. Finally, we implement our schemes to demonstrate their practical performance at parameter sizes relevant to blockchains.

  匹配依据：MPC: mpc (context)

  </details>

- **OptiPrime: Optimizing Private Inference through Protocol-Hardware Co-design**
  2026-09-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.16898)
  Jiangrui Yu, Ye Yu, Si Chen, Chenqi Lin, Wenxuan Zeng, Junfeng Fan, Mingyu Gao, Meng Li

  <details><summary>摘要 / Abstract</summary>

  Private deep neural network (DNN) inference based on hybrid homomorphic encryption (HE) and multi-party computation (MPC) can protect user data with a formal guarantee, but at the cost of significant latency overhead due to HE. Customized HE accelerators have been proposed and have achieved orders-of-magnitude speedup for individual HE operations. However, when directly applying a commercial HE accelerator to state-of-the-art HE-MPC frameworks, we observe only limited end-to-end performance gain. This is because HE-MPC frameworks often require wireless transmission of input and output ciphertexts for each HE operation, leading to a severe network communication bottleneck. To overcome this challenge, we introduce OptiPrime, a protocol-hardware co-optimization framework for efficient private DNN inference. OptiPrime features a novel HE protocol for convolutions that substantially reduces the number of transmitted output ciphertexts and mitigates the network communication bottleneck. Meanwhile, as the new protocol introduces complex computation for fewer output ciphertext, we observe new memory access challenges due to a high volume of weight plaintexts and intermediate ciphertexts. Hence, we further propose a lightweight compression system for the weight plaintexts, reducing memory traffic by 10 times, as well as a specialized dataflow to maximize on-chip data reuse of intermediate ciphertexts. Extensive experiments show that our framework outperforms the Cheetah baseline by at most 5.7 times on CPUs and 4.2 times with an accelerator.

  匹配依据：MPC: multi party computation

  </details>

- **Maliciously Secure Shuffled Distributed OPRF with Applications to Private Set Operations**
  2026-09-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2035)
  Aron van Baarsen, Aarushi Goel, Lisa Kohl, Peihan Miao, Phuoc Van Long Pham, Peter Scholl, Satvinder Singh

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection (PSI) enables two parties to compute the intersection of their private sets without revealing any additional information. For plain PSI, there exist extremely efficient solutions based on symmetric-key techniques for both the semi-honest and malicious settings. However, for more enriched set operations such as PSI-Cardinality, PSI-Sum, Circuit-PSI, and Private Set Union, the efficiency gap between the semi-honest and malicious settings is significant, often spanning orders of magnitude. A key bottleneck underlying these protocols is the need for a shuffled distributed oblivious pseudorandom function (SH-DOPRF) with malicious security. Existing constructions for this primitive are asympotically suboptimal and/or concretely inefficient. In this work, we present a new protocol for SH-DOPRF with malicious security that achieves linear computation and communication complexity. We present two instantiations: a DDH-based construction using the Dodis-Yampolskiy PRF (PKC 2005), and a plausibly post-quantum secure construction based on a variant of the Dark-Matter PRF (Aranha et al., S&amp;P 2026). Our approach is almost entirely based on symmetric-key techniques, with public-key operations used only for evaluating PRF outputs. This primitive yields maliciously secure protocols for multi-query reverse private membership test (Zhang et al., USENIX Security 2023), which in turn can be used to realize the aforementioned private set operations. These protocols provide two-sided outputs while only additionally leaking the cardinality of the intersection. We implement and evaluate our construction to demonstrate concrete efficiency. Our DDH-based maliciously-secure SH-DOPRF achieves a 2--3 orders of magnitude improvement in total running time compared to the state-of-the-art (Miao et al., CRYPTO 2020 &amp; Yang et al., PoPETs 2025), leading to a similar improvement for PSI-Cardinality. The resulting protocols for various other private set operations also achieve significant improvements over prior work; for example, our PSI-Sum and Circuit-PSI protocols are 1--2 orders of magnitude more efficient.

  匹配依据：MPC: private set intersection, private set union

  </details>

- **Universally Composable Reverse Firewalls for Oblivious Linear Evaluation and Applications**
  2026-09-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2012)
  Suvradip Chakraborty, Kiran Deep Ghosh, Satrajit Ghosh, Subha Kar, Divyam Katiyar, Sougata Mandal, Soumit Pal, Amlan Sinha

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) traditionally assumes that parties execute protocols on trustworthy machines. This assumption fails under machine subversion, where compromised devices may leak sensitive information through manipulated protocol transcripts. Reverse Firewalls (RFs), introduced by Mironov and Stephens-Davidowitz, counter this threat by externally sanitizing messages in a functionality-preserving manner, without trusting the internal execution environment. Prior RF constructions are limited to Boolean-circuit-based MPC using oblivious transfer (OT) and garbled circuits (GC). In contrast, many high-performance MPC protocols are predominantly arithmetic, relying on Oblivious Linear Evaluation (OLE) as a core primitive. Achieving subversion resilience in this setting requires sanitizing OLE, a problem that has remained open. We initiate a systematic study of subversion-resilient arithmetic MPC in the universally composable (UC) framework against semi-honest adversaries. We formalize a sanitizable OLE functionality \FsOLE, prove a two-round impossibility for a natural class of additive homomorphic encryption (AHE)-based protocols, and present a UC-secure three-round construction from key-malleable AHE. To recover the full expressiveness of plain OLE, we further introduce wrapped sanitizing OLE under a covert adversary model, yielding an efficient UC-secure two-round protocol. Both constructions are instantiated using a key-malleable AHE scheme from class groups that we construct. Using OLE as a black box, we obtain the first subversion-resilient UC-secure protocols for Oblivious Polynomial Evaluation (OPE), Oblivious Polynomial Addition (OPA), and Private Set Intersection (PSI), achieving optimal communication for PSI. A full end-to-end implementation demonstrates that RF protection incurs only a 1.5--3X overhead, showing that practical subversion-resilient MPC is attainable.

  匹配依据：MPC: garbled circuits, oblivious transfer, private set intersection, secure multi party computation

  </details>

- **Silk: Computation-Efficient and Post-Quantum-Friendly Randomness Beacon**
  2026-09-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2021)
  Binyang Hou, Jiamian Yan, Liang Zhang, Borui Chen, Haibin Kan

  <details><summary>摘要 / Abstract</summary>

  Distributed randomness beacons enable mutually distrustful parties to jointly generate public randomness. Several existing beacons built from secret sharing use costly pairings or group operations to verify shares. Their underlying discrete-logarithm assumptions are also vulnerable to quantum attacks. Moreover, running a separate Byzantine fault-tolerant (BFT) consensus instance for each output incurs repeated computation and communication costs, even when secrets are shared in batches. We present Silk, a computation-efficient, post-quantum-friendly and deterministic randomness beacon under partial synchrony. Silk&#x27;s sharing protocol, Mulberry, realizes batched asynchronous verifiable secret sharing with partial output (bAVSS-PO), using hash-based share verification to reduce computation cost. Silk further amortizes BFT consensus across a batch of outputs, requiring only one BFT instance per batch. We establish Mulberry&#x27;s bAVSS-PO properties and Silk&#x27;s beacon properties under static corruption and the stated security assumptions. We implement Silk and Mulberry in Rust and evaluate their computation and communication costs. In WAN experiments with 121 replicas across eight AWS regions, Silk achieves a throughput of 5.414 outputs/s, 1.53× that of Rondo [NDSS&#x27;25] and 4.18× that of Spurt [IEEE S&amp;P&#x27;22].

  匹配依据：MPC: secret sharing

  </details>

- **On the (Im)possibility of Asynchronous Proactive Secret Sharing**
  2026-09-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2018)
  Erica Blum, Yingzi Gao, Julian Loss, Yuan Lu, Zhenliang Lu, Qiang Tang

  <details><summary>摘要 / Abstract</summary>

  In this paper, we systematically study the (im)possibilities of proactive secret sharing (PSS) in fully asynchronous authenticated networks. To reflect the subtleties arising from the absence of a global clock, we first formalize a hierarchy of natural mobile adversary models for asynchronous PSS (APSS), capturing different adversarial capabilities over corrupted parties and distinct ways of accounting for mobile corruption in asynchrony. Under these models, we then (i) establish new impossibility results by exhibiting generic attacks on APSS, thereby deriving the corresponding resilience upper bounds, and (ii) demonstrate the tightness of these bounds via explicit APSS protocols achieving optimal resilience in each model.

  匹配依据：MPC: secret sharing

  </details>

- **New Pseudorandom Correlation Functions and Exponent VRFs from DCR**
  2026-09-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2030)
  Archisman Dutta, Lisa Kohl, Lawrence Roy, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  Pseudorandom correlation functions (PCFs) allow two parties to expand short correlated keys into an unbounded, locally evaluatable source of correlated randomness. In this paper, we give the first constructions of PCFs for correlated oblivious transfer (COT) and vector oblivious linear evaluation (VOLE) correlations over $\mathbb{Z}_M$ for an arbitrary modulus $M$, with reasonable concrete efficiency. Our construction comes with a lightweight, two-round distributed setup protocol, and relies solely on the decisional composite residuosity (DCR) assumption. As part of our security analysis, we introduce a new family of extended power DDH problems over subgroup indistinguishability groups, and give a novel master theorem showing that this is implied by standard DCR. This suffices to prove security of our PCF based on DCR, and also implies that prior constructions relying on related power-DDH style assumptions in composite groups can be based on DCR alone. We further extend our construction to obtain a PCF for oblivious linear evaluation (OLE) and general degree-two correlations over $\mathbb{F}_2$. As an application of our PCF for VOLE, we derive a designated-verifier exponent-verifiable random function (eVRF), where the publicly verifiable output is the VRF output in the exponent. As an independent contribution, we additionally give a publicly verifiable eVRF from an offline/online variant of homomorphic secret sharing. Both of these constructions have much shorter proof sizes than prior work.

  匹配依据：MPC: oblivious transfer, secret sharing

  </details>

- **Leopard: A High-Performance Framework for Updatable Private Set Intersection**
  2026-09-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2027)
  Xiaowei Li, Shi-Feng Sun, Yanxue Jia, Hao Li, Dawu Gu

  <details><summary>摘要 / Abstract</summary>

  Updatable Private Set Intersection (UPSI) extends conventional PSI protocols to dynamic scenarios, where input sets evolve over time. A straightforward approach is to rerun the entire PSI protocol after each update, incurring redundant computational and communication overhead. Although several UPSI schemes have been proposed to enable updates without full protocol re-execution, existing constructions remain impractical. Building on the high efficiency of unbalanced PSI designs, this work introduces Leopard---a general framework that leverages unbalanced PSI to realize UPSI without complete re-execution, while handling both insertions and deletions. Leopard is compatible with any unbalanced PSI protocol and achieves further performance gains by reusing internal data structures across updates. Specifically, we observe that certain data structures in unbalanced PSI can be incrementally updated instead of fully rebuilt. We provide an FHE-based instantiation of Leopard that demonstrates substantial performance improvements through such data structure reuse. Through comprehensive experiments, we evaluate Leopard&#x27;s performance. Compared to Badrinarayanan et al. (ASIACRYPT 2024) and Alborch et al. (ACNS 2026), our instantiations reduce computational cost by up to 111.28× and at least 1.48×, and communication cost by up to 118.97× and up to 522.01×, respectively.

  匹配依据：MPC: private set intersection

  </details>

- **It's Not Just a Phase: Understanding Function Dependence in MPC Preprocessing (Extended Version)**
  2026-09-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2029)
  Andreas Brüggemann, Kasra Edalatnejad, Jan Filipp, Philipp Kusterer, Thomas Schneider

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) is a key enabling technology for privacy-preserving applications. To achieve low latency after inputs are provided, many efficient protocols utilize preprocessing, and the landscape of preprocessing approaches is growing and diverse. Some recent works use variants of function-dependent preprocessing, leveraging additional knowledge on the function to be computed for even better performance. While the existing literature primarily focuses on performance, it is mostly overlooked that there exist different kinds of function dependence and what practical implications they have. We systematize the different flavors of function dependence, relating them to practical requirements beyond efficiency.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Trinqet: Private Triangle and Quadrangle Counting over Distributed Graphs**
  2026-09-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.14737)
  Mushtari Sadia, Amrita Roy Chowdhury

  <details><summary>摘要 / Abstract</summary>

  Triangle and quadrangle counts are core statistics in graph analysis. Yet many real-world graphs are distributed across multiple parties and encode highly sensitive relationships, precluding direct data sharing. Secure multi-party computation (MPC) provides a principled alternative, but introduces a fundamental tension: the protocol must hide the graph&#x27;s topology, forcing fully data-oblivious operations over all potential edges--while real-world graphs are extremely sparse, making most of this work wasted. We propose Trinqet, a system that resolves this tension through new MPC-friendly algorithms for private triangle and quadrangle detection. Trinqet safely exploits sparsity using a suite of novel techniques that eliminate vast numbers of unnecessary operations while preserving strong security in the malicious threat model. Trinqet supports both counting and enumeration and, in our evaluation, outperforms all five baselines by up to 10^5 in runtime.

  匹配依据：MPC: secure multi party computation

  </details>

- **On Succinct Obfuscation via Propositional Proofs**
  2026-09-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2009)
  Abhishek Jain, Zhengzhong Jin, Surya Mathialagan, Omer Paneth

  <details><summary>摘要 / Abstract</summary>

  A central line of inquiry in the study of indistinguishability obfuscation (IO) is to minimize the size of the obfuscation. Today we know how to obfuscate programs represented as Turing machines, where the size of the obfuscation grows only with the input size and not with the machine&#x27;s running time. Jain and Jin [FOCS 2022] showed how to remove the dependency on the input size for functionally equivalent programs where equivalence can be proven in Cook&#x27;s theory PV. In this work we investigate the limits of the pursuit of succinct obfuscation. We consider the task of obfuscating a program with a large description, most of which can be made public while some portion of the description is secret. We put forth a new notion of fully succinct IO where the size of the obfuscated program only grows with the size of the program&#x27;s secret part and not with the public part or with the input size. Starting with input-succinct IO for PV-equivalent machines, which is known from super-polynomially hard IO for circuits and LWE, we construct fully succinct IO for the same class of programs. We refer to such an obfuscation as fully succinct pv-IO. Next, we show how to bootstrap our fully succinct pv-IO to achieve full IO security. Our bootstrapping theorems are based on succinct cryptographic primitives with seemingly weaker functionality: either succinct witness encryption or SNARGs for NP with unique proofs. We also require that the correctness of these primitives can be proven in theory PV. We show that these assumptions are sufficient and necessary. We demonstrate several applications of fully succinct IO and pv-IO: (i) We give the first IO construction where the size of the obfuscated program is less than twice the size of the original program for a large class of useful programs. (ii) We show how to avoid padding the program before obfuscating it—a step often necessitated by security analysis—by replacing the padding with a public random string. (iii) We give the first construction of succinct computational secret sharing for access structures represented by polynomial-size monotone circuits where the share size does not grow with the size of the access structure.

  匹配依据：MPC: secret sharing

  </details>

- **New Imperfect High Threshold and Slice Secret Sharing Schemes**
  2026-09-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2008)
  Andrej Bogdanov, Yanbo Chen

  <details><summary>摘要 / Abstract</summary>

  We present new constructions of (n - t + 1)-out-of-n threshold and slice secret sharing schemes for short secrets with imperfect secrecy for constant t and growing n. Our main results are 1. an ε-differentially secret, (n - t + 1)-out-of-n bit secret sharing scheme with share alphabet size Õ_t(1/ε^2). In contrast, perfect secrecy requires share alphabet size n - t + 1 (Bogdanov, Guo, and Komargodski, ToC 2020). For t &gt; 3, the security of our scheme relies on a conjecture about factorizations of univariate polynomials in finite fields. 2. an ε-statistically secret bit secret sharing scheme for every (n-2)-out-of-n slice with share size O(log n log 1/ε). Previous constructions with comparable parameters achieved only computational security (Beimel, Farràs, Lasri, and Nir, TCC 2024). Variants of our first construction produce plain and anonymous (n-1)-out-of-n weak bit secret sharing schemes with optimal share size. We discuss the relevance of these schemes to secret sharing duality.

  匹配依据：MPC: secret sharing

  </details>

- **Beyond DCR: HSS and PCFs from Subgroup Indistinguishability**
  2026-09-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/2006)
  Sebastian Hasler

  <details><summary>摘要 / Abstract</summary>

  We construct homomorphic secret sharing (HSS) and pseudorandom correlation functions (PCFs) in a general group-theoretic framework, with security based on the subgroup indistinguishability (SgI) assumption introduced by Brakerski and Goldwasser (Crypto 2010). Under certain instantiations of this framework, SgI corresponds to decisional composite residuosity (DCR), but other instantiations are possible as well. Hence, our work expands the set of assumptions that imply HSS and PCFs. Our constructions crucially rely on the existence of an efficient distributed discrete logarithm (DDLog) algorithm for the utilized group. We construct a new DDLog algorithm that works in general groups as long as the order $t$ of the base is smooth. In particular, our DDLog supports the prime-power case, which was previously an open problem. Moreover, we apply a divide-and-conquer optimization that significantly improves the performance from $\mathcal O(\log^2 t / \log \log t)$ group operations (Abram et al., Crypto 2022) to $\mathcal O(\log t \log \log t)$. Toward constructing PCFs, we introduce a new notion of public-coin subgroup indistinguishability (PC-SgI). We show that, in certain instantiations, SgI implies PC-SgI, so no new assumption is required. We then obtain PCFs for VOLE, OT, OLE, and degree-two correlations, all generically under PC-SgI. Our PCFs for OLE and degree-two correlations additionally rely on the sparse LPN assumption. Along the way, we discover and patch two security issues in prior work: first, an attack on decisional Diffie–Hellman (DDH) in the Joye–Libert instantiation by Abram et al. (Crypto 2022), and second, a flaw in the security proofs of optimized variants of the IKNP OT extension protocol and of many silent OT extension protocols.

  匹配依据：MPC: secret sharing

  </details>

- **Transparent Identity Verification Approach Using MPC and Efficient Credential Status Handling**
  2026-09-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.14195)
  Istiaque Ahmed, Shoji Kasahara, Kentaroh Toyoda, Tadashi Nakano, Thi Hong Tran

  <details><summary>摘要 / Abstract</summary>

  A secure and privacy-preserving identity verification process is essential for digital ecosys- tems. Current eKYC frameworks that rely on Zero-Knowledge Proofs (ZKPs) face high computational cost, rigid circuit design, complex integration, and expensive on-chain verification. The W3C 2021 BitString- based credential status mechanism also suffers from inefficient updates and poor scalability in large- scale deployments. We propose a transparent and cost-effective identity verification framework based on Multi-Party Computation (MPC). It enables private off-chain code execution and produces runtime proofs anchored to a blockchain. The framework introduces a multidimensional bit-matrix model with efficient compression. Using ZSTD, the credential data is reduced to 76 bytes compared to 140 bytes with GZIP, cutting storage and bandwidth costs. The system also supports fine-grained status updates and Layer-2 blockchain anchoring for tamper-evident, low-cost verification. The system employs reusable verifiable presentations (VPs) with unique access tokens, enabling cost-free verification and stronger access control. Selective disclosure preserves user control and strengthens privacy. Finally, the system integrates SHA3 hashing and Falcon post-quantum signatures. This guarantees robustness against quantum attacks, transparency, and scalability. It is a future-proof solution for national-scale identity verification, as demonstrated by experimental findings and security studies that validate its robustness and applicability.

  匹配依据：MPC: multi party computation

  </details>

- **PixCrypt: Fast Fine-Grained FHE with Range-Aware Caching**
  2026-09-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.14137)
  Chao Wang, Shubing Yang, Xiaoyan Sun, Yan Bai, Jun Dai, Dongfang Zhao

  <details><summary>摘要 / Abstract</summary>

  Many analytics tasks require secure computation over encrypted data. In particular, fine-grained data such as pixel-level images require higher precision, as every pixel can directly affect outcomes in tasks like tumor segmentation and anomaly detection. While Multi-Party Computation (MPC) is interactive, Differential Privacy (DP) protects only aggregate values, and Partially Homomorphic Encryption (PHE) lacks multiplicative support, none of them can efficiently handle fine-grained data analytics. Fully Homomorphic Encryption (FHE) uniquely enables arbitrary operations on encrypted pixels but remains computationally expensive, posing significant challenges for both software and hardware accelerators. We present PixCrypt, a caching-based acceleration mechanism for fine-grained fully homomorphic encryption. PixCrypt replaces expensive fresh ciphertext generation with cache retrieval and coefficient-level operations across CKKS, BFV, and BGV, while randomized reconstruction ensures that ciphertexts do not repeat. Its linear noise growth reduces the need for bootstrapping and lowers NTT load, improving hardware accelerator efficiency. This design yields up to 35x faster fine-grained encryption and maintains IND-CPA (Indistinguishability under Chosen Plaintext Attack) security. Experiments on five real-world pixel-level image processing tasks show that PixCrypt significantly improves the practicality of FHE for privacy-preserving analytics.

  匹配依据：MPC: multi party computation, secure computation

  </details>

- **Network-Agnostic VSS with Quadratic Communication in Computational Setting**
  2026-09-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1993)
  Yusong Yao, Qi Feng, Cong Peng, Min Luo, Debiao He

  <details><summary>摘要 / Abstract</summary>

  Verifiable secret sharing (VSS) is a core primitive in multiparty computation (MPC). Bhimrajka et al. [PKC&#x27;24, TIT&#x27;26] proposed the first computationally network-agnostic VSS and VSS-based MPC, which seamlessly accommodate both synchronous and asynchronous network models. However, their VSS requires Byzantine Agreement (BA) and incurs $O(n^5)$ bits of communication per sharing among $n$ parties, and their MPC requires honest participation from nearly all parties. We revisit the network-agnostic VSS architecture and propose a more efficient and general network-agnostic VSS structure. Our key technique is a new virtual-party strategy, which introduces more parties for reconstruction. With this technique, network-agnostic VSS is BA-free and performs as efficiently as synchronous VSS. Specifically, in terms of communication, our VSS costs $O(n^2)$ bits in the one-shot case and $O(n)$ bits in the round-by-round case with the dispute-control technique, yielding the first computationally network-agnostic VSS protocols with amortized linear communication complexity. Besides, we further address a series of subtle yet necessary hurdles in adapting existing results to network-agnostic models, including the erasure coding techniques in Reliable Broadcast (RBC), packed secret sharing techniques in VSS, and the correlated polynomial techniques in MPC.

  匹配依据：MPC: multiparty computation, secret sharing

  </details>

- **A Low-Communication Garbled RAM from Homomorphic Secret Sharing**
  2026-09-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1998)
  Chase Fickes, Jinye He, Wei-Kai Lin

  <details><summary>摘要 / Abstract</summary>

  Garbled circuits are fundamental in modern cryptography and secure two- or multi-party computation. For real-world programs that are naturally expressed in the Random-Access Machine (RAM) model, garbled RAM is the RAM counterpart of garbled circuits: they avoid the cost of compiling the entire program into a circuit, with communication complexity serving as the primary efficiency metric. We study the setting in which the RAM program is public, while the input data and memory contents remain secret except for the prescribed output. We construct a garbled RAM for programs running in time $T$ over memory consisting of $N$ words of $W$ bits each, the scheme achieves \[ O(T \cdot (W + \lambda) \cdot \log N) + \mathrm{poly} (\lambda) \] bits in communication, where $\lambda$ is the security parameter. For sufficiently large word size $W\ge \lambda$ and running time $T\ge\mathrm{poly}(\lambda)$, the communication becomes $O(T W \log N)$, asymptotically matching the bandwidth of an optimal oblivious RAM. Since any secure garbled RAM must hide memory accesses as in oblivious RAMs, our construction can be viewed as compiling an oblivious RAM into a non-interactive analogue, without incurring additional asymptotic communication cost. Technically, our garbled RAM builds on the recent succinct garbled circuits of Ishai, Li, and Lin (Crypto&#x27;25) and Li, Lin, and Lu (Eurocrypt&#x27;26), which are in turn based on homomorphic secret sharing. Accordingly, we inherit their circular-power variants of the Decisional Diffie-Hellman or Ring Learning-With-Errors assumptions. We also use techniques from the recent work on garbled arithmetic RAM, called Zebra, by Gu, Ghoshal, and Shi (Eurocrypt&#x27;26). Compared to Zebra, which achieves the same $O(TW\log N)$ communication for *arithmetic* RAM programs that only perform arithmetic over large and bounded integers, our work focuses on the standard *boolean* RAM model. Compared to the best garbled RAM in the random oracle model, due to Liu, Liu, Luo, and Heath (ACM CCS&#x27;26), we remove a multiplicative factor $\lambda$ in communication.

  匹配依据：MPC: garbled circuits, multi party computation, secret sharing

  </details>

- **Post-Quantum Private Set Intersection for Small Sets**
  2026-09-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1985)
  Junxin Liu, Mike Rosulek, Ni Trieu

  <details><summary>摘要 / Abstract</summary>

  Are private set intersection (PSI) protocols ready for the post-quantum future? We focus on the PSI protocol of Rosulek \&amp; Trieu (``RT21&#x27;&#x27;, ACM CCS 2021), which is the current state-of-the-art for PSI on small sets (less than a thousand items). The RT21 protocol presents some fundamental barriers to post-quantum security. First, although it is written in terms of an arbitrary KEM, it requires certain properties of Diffie-Hellman KEM that simply are not satisfied by any post-quantum candidates. Second, even if adapted to post-quantum KEMs, it would require an ideal permutation with blocklength larger than any known viable candidate. We show how to modify the RT21 to make it compatible with post-quantum KEM candidates like ML-KEM. We also describe a direct domain-extension construction for ideal permutations, showing how to construct a huge-block ideal permutation directly from one with smaller blocklength, such as the Keccak permutation family. Along the way, we also introduce new abstractions for \emph{oblivious key-value stores} (Garimella et al., Crypto 2021) that make the analysis of these kinds of PSI protocols more modular. We implemented our protocol and evaluated its performance across different network settings and instantiations. We achieve PSI from standardized post-quantum primitives with latency as low as $0.25$ ms/item and communication as low as $1.67$ KiB/item. We find that the performance penalty for post-quantum security ranges from 1.25$\times$ to 5.92$\times$ in latency and is 16.7$\times$ in communication, depending on the instantiation.

  匹配依据：MPC: private set intersection

  </details>

- **High-rate multipartite quantum secret sharing with composable security**
  2026-09-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.13367)
  Russell M. J. Brooks, Joseph Ho, Joseph Niblo, Janka Memmen, Anna Pappa, Jens Eisert, Nathan Walk, Alessandro Fedrizzi

  <details><summary>摘要 / Abstract</summary>

  Future quantum communication networks will conceivably support cryptographic tasks that require entanglement among more than two users. Quantum secret sharing is a prime example where entanglement provides a direct means to coordinate untrusted parties with security from eavesdropping in a multi-party setting. However, the canonical GHZ-based protocols can be vulnerable to participant attacks, in which untrusted parties try to learn the secret without collaborating. Here, we experimentally evaluate a discrete-variable $(n,n)$-threshold quantum secret-sharing protocol whose finite-key analysis provides composable security against general attacks, including participant attacks. Using two domain-engineered entangled photon pair sources, we generate 4-qubit GHZ states at rates above $5\times10^3$ fourfold events per second and a maximum asymptotic secret key rate of $750 \pm 10$ bits per second. We then distribute the state through a 4-arm star network comprising 20km of fibre in total. From the measured event rates and error statistics, we infer that a randomised 24-hour execution with the optimised basis probability would yield a composable finite-key lower bound of 8.7 Mbits, under the assumption that the measured source and device statistics remain stationary.

  匹配依据：MPC: secret sharing

  </details>

- **Three-Round Weak Non-Malleable Zero-Knowledge Argument**
  2026-09-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1964)
  Xinxuan Zhang, Yuanju Wei, Zhichao Wang, Zhongliang Zhang, Ming Yang, Ruida Wang, Yi Deng, Hailong Wang

  <details><summary>摘要 / Abstract</summary>

  Non-malleable zero-knowledge argument(NMZK) is a strong notion of zero-knowledge argument that ensures security against man-in-the-middle(MIM) attacks. While three-round constructions exist for various weak zero-knowledge arguments under standard assumptions, all known (weak) NMZK protocols in the plain model have required at least four rounds. In this work, we construct the \emph{first three-round weak non-malleable zero-knowledge argument} under standard cryptographic assumptions. Our protocol satisfies weak zero-knowledge and $\epsilon$-non-malleability, where the latter allows an $\epsilon$ probability gap between the MIM experiment and the stand-alone experiment for any polynomial inverse $\epsilon$. Our construction relies only on well-established primitives, such as the existence of two-message oblivious transfer protocols and delayed-input WI arguments, non-interactive commitments, and circuit-privacy fully homomorphic encryptions.

  匹配依据：MPC: oblivious transfer

  </details>

- **PHAT: PHotonic Accelerator for TFHE**
  2026-09-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.11613)
  Guowei Yang, Farbin Fayza, Beren Aydoğan, Carlos A. Ríos Ocampo, Ayse K. Coskun, Ajay Joshi

  <details><summary>摘要 / Abstract</summary>

  Fully Homomorphic Encryption (FHE) enables secure computation on encrypted data, making it a promising solution for privacy-preserving applications in the cloud. Among various FHE schemes, FHE over the Torus (TFHE) stands out due to its support for arbitrary operations. However, its high computation and communication overhead, particularly in the Fast Fourier Transform (FFT) operations required during bootstrapping, limits its practicality for real-world applications. Conventional electronic accelerators struggle to achieve sufficient throughput due to the limitations of technology scaling and the memory-wall problem. To address these challenges, we propose PHAT, a PHotonic Accelerator for TFHE leveraging Optically-addressed Phase-Change Memory (OPCM). OPCM-based processing-in-memory systems offer high computation and communication throughput, making them well-suited for accelerating FFT operations in TFHE. However, directly mapping FFT to OPCM presents challenges such as high-precision analog computation and the high latency and energy cost of programming OPCM cells. To overcome these challenges, we introduce a novel electro-photonic accelerator architecture optimized for TFHE, featuring OPCM-based FFT units, a twiddle-stationary dataflow tailored for OPCM, and a scheduling mechanism to maximize the utilization of the FFT units. PHAT delivers $2.14\times$--$5.10\times$ speedup across four real-world TFHE workloads against the state-of-the-art ASIC accelerator. Our approach significantly enhances the performance of TFHE applications, paving the way for practical and efficient homomorphic encryption in cloud computing.

  匹配依据：MPC: secure computation

  </details>

- **Lattice-based Threshold Traitor Tracing with Public Traceability**
  2026-09-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1965)
  Sébastien Canard, Nathan Papon, Duong Hieu Phan

  <details><summary>摘要 / Abstract</summary>

  Since the introduction of Threshold Traitor Tracing by Boneh, Partap and Rotem at CRYPTO &#x27;24, several works have extended the functionalities within the framework or improved the parameters. However, most of the existing solution fall short in providing post quantum security guarantees. The only lattice-based construction, due to Das et al. from EUROCRYPT &#x27;26, achieves post-quantum security but is limited to private tracing: a dedicated tracing authority holds a secret tracing key. In a threshold system, where the fundamental goal is to distribute trust, such a single point of failure is undesirable. In this work, we construct the first threshold traitor tracing scheme that simultaneously achieves post-quantum security and public traceability, where anyone can trace a pirate decoder without any secret tracing key. Our core building block is a Q-Partite Threshold Public Key Encryption (QTPKE) scheme, which is known to imply threshold traitor tracing when combined with a robust IPP code: we build QTPKE from plain Learning With Errors (LWE) using a key-shifting mechanism on top of Regev&#x27;s encryption scheme thresholdised via {0,1}-Linear Secret Sharing. We finally prove the security of our scheme in the standard model under standard lattice assumptions.

  匹配依据：MPC: secret sharing

  </details>

- **Component-Dual Compression and the Exact Characteristic-Two Contribution Region of the Relaxed Non-Fano Port**
  2026-09-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1971)
  Shahram Khazaei, Maghsood Parviz

  <details><summary>摘要 / Abstract</summary>

  Jafari and Khazaei (Journal of Cryptology, 2021) introduced a kernel-based lower-bound method for linear secret-sharing schemes by fixing one minimal qualified coalition and comparing its participant components with those arising from auxiliary minimal qualified coalitions. These comparisons form a star. We extend the same mechanism from stars to coalition-labelled trees and obtain new characteristic-two inequalities for the relaxed-line non-Fano port $\widehat N$. For this access structure, the tree method is strictly stronger than the star method, yielding facet inequalities not implied by the star inequalities. We also show that the tree method does not determine the full contribution region. To complete the analysis of $\widehat N$, we introduce component-dual compression (CDC). CDC replaces each share by the span of the components selected from minimal reconstructions and realizes the duals of these compressed spaces in a common coordinate system indexed by the original minimal coalitions. This yields the remaining lower-bound inequalities. Together with matching constructions, the star, tree, and CDC bounds determine the complete characteristic-two linear contribution region of $\widehat N$, with maximum and average linear information ratios $5/4$.

  匹配依据：MPC: secret sharing

  </details>

- **Verifiable Weighted Secret Sharing based on Chinese Remainder Theorem**
  2026-09-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1949)
  Xinyu Zhang, Weiping Ji, Tsz Hon Yuen, Ron Steinfeld, Joseph K. Liu, Shujie Cui

  <details><summary>摘要 / Abstract</summary>

  In this work, we present the first practical verifiable weighted secret sharing (VWSS) scheme based on the Chinese Remainder Theorem (CRT). Classical secret sharing schemes, such as Shamir’s, assume participants with equal weights, which is inadequate for emerging applications like stake-based DAO voting and proof-of-stake blockchains, where parties naturally have unequal voting power or stakes. While prior work (e.g., Garg et al., Crypto&#x27;23) demonstrated that CRT-based (ramp) secret sharing can support weighted access structures more efficiently than linear secret sharing schemes, existing constructions only guarantee security against honest-but-curious dealers. In contrast to traditional linear secret sharing schemes, extending verifiability to CRT-based weighted secret sharing remains challenging, as current approaches either fail to support weighted access structures or incur prohibitive computational overhead on the dealer, limiting their practicality. To address this gap, we develop novel $\Sigma$-protocols for the \emph{unbounded} proof-of-mod (UPoM) relation using integer commitments in groups of unknown order, which may be of independent interest. Combining our UPoM protocols and new observations on the structural properties of CRT-based secret sharing, we construct a VWSS scheme in which the dealer broadcasts only $O(|A|)$ commitments to secret shares, where $A$ is a subset of parties whose total weight meets the reconstruction threshold $T$. This improves upon the closest prior CRT-based VWSS scheme (Shehata et al., CVC&#x27;25), which requires the dealer to broadcast commitments to the secret shares of all parties. Concretely, for a system with four participants and total weight $524$, our scheme generates VWSS proofs in around $0.2$ seconds, \emph{orders of magnitude faster} than the construction of CVC&#x27;25, highlighting its practicality for real-world applications.

  匹配依据：MPC: secret sharing

  </details>

- **Robust Additive Randomized Encodings With Transparent Setup**
  2026-09-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1937)
  Sapir Bekerman Freizeit, Nir Bitansky

  <details><summary>摘要 / Abstract</summary>

  Additive randomized encodings (AREs) reduce the computation of an m-party function f(x1, . . . , xm) to independently encoding each input and adding the resulting encodings in an Abelian group, so that their sum reveals nothing but the output. Robust AREs (RAREs) additionally protect against collusions between the evaluator and some of the parties, guaranteeing that even if some of the input encodings are completely controlled by the adversary, the partial sum of the remaining (honest) input encodings leaks no more than the residual function f(x_H, ·) obtained by fixing the honest inputs x_H. Much of the appeal of RAREs come from the fact that they imply robust non-interactive secure computation in the shuffle model, where parties send messages to the evaluator through anonymous communication channels. Existing constructions of general-purpose RARE either assume ideal obfuscation or rely on structured public parameters generated using secret randomness that must remain hidden. We construct general-purpose RARE with transparent setup. Assuming indistinguishability obfuscation (which is necessary) and LWE, both with subexponential security, we show that every efficient function admits an efficient RARE in the common random string model. We also show how to eliminate public parameters altogether in the honest-majority setting. The main technical observation behind our construction is that non-robust ARE, which exist assuming only one-way functions, can be leveraged to protect from spoofing of honest party encodings.

  匹配依据：MPC: secure computation

  </details>

- **Quantum Evolving Secret Sharing - revisited**
  2026-09-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1946)
  Efrat Cohen, Anat Paskin-Cherniavsky

  <details><summary>摘要 / Abstract</summary>

  In evolving secret sharing, introduced by Komargodski et al., an infinite set of parties share a secret according to an infinite access structure (where minimal qualified sets are finite). In such schemes, par- ties arrive one by one, and and are given a share by the dealer. There is no additional communication incurred to a given party until the time of reconstruction, where share holders who show up combine their shares to reconstruct the secret if they form a qualified set. In this work, we revisit the notion of quantum evolving secret sharing schemes, we dub QESS, where a quantum secret is shared. Smoothly generalizing the above setting runs into difficulties due to the no-cloning theorem. In particular, values handed to previously arriving parties can not be copied by the dealer and used in the evaluation of future parties’ shares, as often done in evolving secret sharing schemes from the liter- ature. Indeed, attempts to formalize quantum evolving secret sharing, such as that on Chaudhury for the so called dynamic threshold setting and by Cohen et al. for general evolving access structures fell short from adhering to the minimally interactive communication pattern above. In this paper, we take a different approach, and consider a setting where several (possibly infinitely many) copies of a secret (known to the dealer) are generated by need. This approach has been used by Cakan et al. for (finite) quantum secret sharing (QSSS), allowing to circumvent the im- possibility of devising QSSS for monotone access structures which are not no-cloning - those that have disjoint pair of qualified sets. This setting is plausible in many applications, where the secret is known to the dealer at sharing time. Cakan et al. demonstrate that at most n copies of the secret prepared by the dealer, suffice to implement any monotone access structure. In the evolving setting, it is not clear how to devise QESS even for evolving no-cloning access structures. Introducing multiple copies of the secret allows to define QESS with a communication pattern similar to the classical setting, in which arbitrary (not necessarily no cloning) evolving access structures can be implemented. using c(t) ≤ t copies of the secret used to generate the shares of the first t parties - similarly to the finite setting. We study the copy number landscape for various evolving access struc- tures. For general access structures, c(t) ≤ t copies of the secret suffice to generate the shares of the first t parties - similarly to the finite setting. On the lower bound side, the no-cloning theorem implies c(t) = t is nec- essary for QESS. The main question we leave open is whether a single copy suffices for no-cloning evolving access structures, while 1 is the ex- act number of the finite setting. We prove that every no-cloning evolving access structure has a QESS with a finite copy number c(t) ≤ C, where the constant C depends on the particular access structure. Furthermore, for every T0, there exists a QESS as above with c(t) ≤ 1 for t ≤ T0. Our techniques generalize the hybrid technique of Cakan et al. abstract- ing their implicit approach of treating the access structure as a union of no-cloning access structures, and implementing each via exiting quantum erasure codes (QECC), which provide not privacy. Then, a copy of the secret, masked by a classical random key (via QOTP) is encoded by each of these codes. The classical keys are then classically shared via each of the access structure to provide privacy. While they rely on a union of no-cloning threshold access structures, we use arbitrary ones. This often reduces the resulting copy number already in the finite setting. Special care is required to share the QOTP keys for each access structure in the union, while keeping every party’s share finite.

  匹配依据：MPC: secret sharing

  </details>

- **Honest Majority MPC Achieving GOD with $O(\|C\|)$ Communication From Pairwise Random OLE Correlations**
  2026-09-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1948)
  Zonghang Du, Yifan Song, Xiaxi Ye

  <details><summary>摘要 / Abstract</summary>

  In this work, we study the communication complexity of information-theoretic MPC with guaranteed output delivery (GOD) in the honest majority setting $(t&lt;n/2)$. The recent work by Song and Ye (EUROCRYPT 2025) gives an honest majority MPC in the random oblivious linear evaluation (OLE) preprocessing model that computes an arithmetic circuit of size $|C|$ with malicious security with abort at the cost of $O(|C|)$ of both communication in field elements and total number of random OLE correlations. We explore the possibility of deriving a similar result for the stronger security notion of GOD. Specifically, we ask the question: `` Is it possible to construct an information-theoretic honest majority MPC in the random OLE preprocessing model that computes an arithmetic circuit of size $|C|$ and achieves GOD with $O(|C|)$ field elements of communication and $O(|C|)$ amount of random OLE correlations in total? &#x27;&#x27; We resolve the above question in the affirmative by providing a concrete construction. To achieve our result, we mainly rely on two techniques. First, we propose a new secret sharing scheme which we refer to as detectable secret sharing. It is a packed secret sharing scheme with an authentication mechanism. Second, to efficiently verify the computation and locate an error when faults occur, we extensively make use of the virtual transcript technique introduced in the work by Goyal, Song, and Zhu (CRYPTO 2020). Our construction is in the random OLE preprocessing model where we assume random OLEs between each pair of parties. By instantiating the random OLEs from various assumptions, we obtain three honest majority MPC protocols with GOD with the following security and communication: (1) the first one achieves information-theoretic security with offline communication of $O(|C|n)$ elements and online communication of $O(|C|)$ elements, (2) the second one achieves computational security with $\tilde{O}(|C|)$ elements of communication only from a random oracle, and (3) the third one achieves computational security with $O(|C|)$ elements of communication from pseudorandom correlation generators (PCG).

  匹配依据：MPC: secret sharing

  </details>

- **High-throughput Verifiable Distributed OPRF from Gold PRF**
  2026-09-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1953)
  Nan Cheng, Yohei Watanabe, Yugo Kasashima, Ioannis Katis, Aikaterini Mitrokotsa

  <details><summary>摘要 / Abstract</summary>

  An oblivious pseudorandom function (OPRF) is a two-party protocol that enables a client to obtain $F_k(x)$ on an input $x$ without learning the server-held key $k$, while the server learns nothing about $x$. OPRF is a fundamental building block in a wide range of privacy-preserving applications, including password-authenticated key exchange (PAKE), private set intersection (PSI), and distributed function secret sharing. In this work, we present the first concrete, high-throughput, post-quantum secure, verifiable distributed OPRF (dOPRF) tolerating $t &lt; n/2$ malicious servers and a malicious client over replicated secret sharing, extending the recently introduced Gold OPRF of Yang et al. (IEEE S&amp;P 2025) to a threshold setting. We adopt an offline-online paradigm and introduce new protocol designs for both phases. (i) In the offline phase, we develop efficient protocols for batched generation of replicated secret sharing of $\alpha^e$ whose cost is independent of $e$. We present two complementary approaches, each designed for different parameter regimes: the first leverages a degenerate additive encoding under which exponentiation commutes with secret sharing; the second employs $t+1$ designated dealers that prove dual-share consistency via non-interactive zero-knowledge proofs, instantiated using both VOLE-in-the-Head and Ligero, yielding post-quantum security based solely on collision-resistant hashing. (ii) In the online phase, we propose a constant-round protocol that tightly integrates secure multiplication-and-opening with distributed zero-knowledge proof (DZKP) verification, reducing communication in every setting we evaluate and computation in all but the largest batched setting, compared to naively using the standard DZKP framework. (iii) We give a verifiable input protocol that enforces a possibly-malicious client providing well-formed inputs; its well-formedness check is absorbed into a hash exchange the online protocol already performs, and it lowers the client&#x27;s upload from a full replicated share to one field element per server per input. Our end-to-end benchmarks show that the construction substantially outperforms the state-of-the-art Legendre-PRF dOPRF of Kaluđerović et al. (ESORICS 2025) in terms of communication across all evaluated settings, and remains practical up to $(n,t)=(9,4)$, a regime where prior approaches become bandwidth- or memory-prohibitive.

  匹配依据：MPC: private set intersection, secret sharing

  </details>

- **Extendable Weighted Evolving Threshold Secret Sharing Schemes over Polynomial Quotient Rings**
  2026-09-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1939)
  Qi Cheng, Guang Hu, Hongru Cao, Sian-Jheng Lin, Yunghsiang S. Han

  <details><summary>摘要 / Abstract</summary>

  In conventional $(k,n)$ secret sharing schemes, a dealer distributes shares of a secret among $n$ participants such that any subset of at least $k$ participants can reconstruct the secret. While such schemes often fail to accommodate practical scenarios in which participants have different management permissions over the secret. To address this problem, weighted $(t,n)$ secret sharing was introduced. In this case, each participant is assigned a specific weight, and the dealer distributes a share to each participant according to their weight, so that any subset of participants whose sum of weights is at least $t$ can recover the secret. However, in weighted $(t,n)$ secret sharing schemes, the number of participants $n$ is known in advance. When $n$ is uncertain and even grows over time, traditional weighted $(t,n)$ secret sharing schemes remain inadequate in such dynamic environments. To solve the problem, we propose the concept of a weighted evolving $t$-threshold secret sharing. Based on the prefix codes, we first propose a construction of a weighted evolving $3$-threshold scheme over the polynomial quotient ring for an $\ell$-bit secret. And then we extend the framework to a general weighted evolving $t$-threshold scheme for any $t\geq 3$. Moreover, we prove the correctness and security of the proposed scheme by leveraging the properties of the polynomial quotient ring and prefix codes. Finally, we analyze the corresponding share size. The result shows that for the $m$-th participant with the weight $w_m$ satisfying $1\leq w_m\leq t-1$, the size of the corresponding share is $w_m(t-1-\frac{w_m-1}{2})(\ell_m-1)+w_m\ell$ bits, where $\ell_m$ denotes the length of a binary prefix code of encoding integer $m$. In contrast, a baseline scheme that allocates $w_m$ independent full evolving shares to this participant would require $w_m(t-1)(\ell_m-1)+w_m\ell$ bits. Our proposed scheme saves $\frac{(w_m-1)w_m}{2}(\ell_m-1)$ bits, thereby achieving a smaller share size.

  匹配依据：MPC: secret sharing

  </details>

- **Efficient Pseudorandom Correlation Generators over Binary Extension Fields and More**
  2026-09-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1940)
  Zhe Li, Hongqing Liu, Chaoping Xing, Yizhou Yao, Chen Yuan

  <details><summary>摘要 / Abstract</summary>

  In this work, we construct highly efficient pseudorandom correlation generators (PCGs) over binary extension fields. PCGs allow for the distribution of a great amount of correlated randomness by having each party locally expand a short seed, enabling efficient multi-party computation (MPC) protocols with silent and sublinear preprocessing. Our PCGs achieve nearly linear time, both asymptotically and concretely, where expanding $N$ VOLEs (vector oblivious linear evaluations) over $\mathbb{F}_{2^k}$ consists of $O(N)$ PRG calls, $O(N)$ multiplications in $\mathbb{F}_{2^k}$ and $O(kN\log{N})$ binary XORs. In fact, the $O(kN\log{N})$ XORs are insignificant in practical parameter regimes where $N\approx 2^{20}$. Concretely, we achieve a throughput of $\approx 5,000,000$ VOLEs per second over $\mathbb{F}_{2^{128}}$, which is at least $4.7$x, $1.9$x and $1.6$x faster than the state-of-the-art PCGs of Expand-Accumulate (EA), Block-Accumulate (BA) and Expand-Convolute (EC) codes, respectively. For oblivious linear evaluations (OLEs), expanding $N$ instances requires $O(\lambda N)$ PRG calls, $O(N)$ multiplications in $\mathbb{F}_{2^k}$ and $O(kN\log{N})$ binary XORs, where $\lambda$ is the security parameter. Based on the $\mathsf{libOTe}$ library, we also give the first full implementation of PCGs for OLEs over extension fields, which shows a throughput of $\approx 42,000$ OLEs per second over $\mathbb{F}_{2^{128}}$. At the heart of our technical contribution is an efficient multivariate FFT algorithm. It evaluates any $n$-variate polynomial $f(x_1,\ldots,x_n)$ over $\mathbb{F}_{2^k}$ of individual degree$\le2$ using exactly $\frac{5}{6}kN\log_3{N}$ additions and $\frac{1}{6}kN\log_3{N}$ multiplications in $\mathbb{F}_4$, where $N=3^n$ and $k$ is an arbitrary even integer. Note that this is considerably faster than normal FFT algorithms that require $O(N\log{N})$ multiplications in the underlying field $\mathbb{F}_{2^k}$. Along the way, we generalize our approach to work over a degree-$k$ Galois extension of $\mathbb{Z}_{2^{\ell}}$, denoted by $\mathbb{GR}(2^{\ell},k)$. Similarly, our algorithm takes only $\frac{7}{6}kN\log_3{N}$ additions and $\frac{1}{6}kN\log_3{N}$ multiplications in $\mathbb{GR}(2^{\ell},2)$ to evaluate $f(x_1,\ldots,x_n)\in\mathbb{GR}(2^{\ell},k)[x_1,\ldots,x_n]_{\leq 2}$. This implies practically efficient PCGs for (V)OLE over Galois rings. As a side contribution of independent interest, we derive fast encoding algorithms for a family of Quasi-Abelian codes, which are even concretely $1.66$x faster than Repeat-Accumulate-Accumulate (RAA) codes over $\mathbb{F}_{2^{128}}$, whose encoding only involves a linear number of additions and two random permutations. As Quasi-Abelian codes have been proven to attain concretely large minimum distance in a recent work of Li et al. (CRYPTO 2026), this opens a door to building more efficient succinct arguments over extension fields.

  匹配依据：MPC: multi party computation

  </details>

- **A size/fan-in trade-off for circuits**
  2026-09-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1896)
  Pierre Meyer

  <details><summary>摘要 / Abstract</summary>

  We consider (boolean or arithmetic) circuits in which every gate may compute an arbitrary function of its input gates. We show a novel tradeoff between a circuit&#x27;s size and its fan-in: \begin{quote} Any function which may be computed using $s$ fan-in $2$ gates can alternatively be computed using $s/3\ (1+O(1/\sqrt{k}))$ fan-in $k$ gates. \end{quote} This asymptotically improves the previous bound of $2s/5\ (1+O(1/k))$ by Charbit, Couteau, Meyer, and Naserasr [TCC&#x27;24]. Among other applications, this improves the communication complexity of secure multiparty computation in the correlated randomness model. \emph{Any} $n$-input $m$-output circuit with $s$ internal gates (over arbitrary binary gates) can be securely computed in the correlated randomness model with per party communication $s/3 + n + m$ and computation $\widetilde{O}(s)$. Our paper stands at the intersection of cryptography, complexity theory, and graph theory, but our main technical contribution is one to extremal combinatorics: we establish that every order-$n$ $2$-degenerate graph admits a planarising set of size at most $\lfloor n/3 \rfloor$. Our main conceptual contribution is to relate the existence of sublinear-size (directed) $k$-path transversals to well-studied graph parameters. Along the way, we uncover a recurringly overstated lemma throughout the literature on sublinear-size vertex-separators and hyperfinite graphs. According to this lemma, any monotone graph class admitting sublinear-size balanced vertex separators should be weakly hyperfinite. However, this is contradicted by a graph class put forward by [Moshkovitz and Shapira, Random Structures \&amp; Algorithms&#x27;15]. Unfortunately, the lemma appears in highly influencial works such as [Henzinger, Klein, Rao, and Subramanian, STOC&#x27;94 \&amp; JCSS&#x27;97], or the textbook of Nešetřil and Ossona de Mendez [\emph{Sparsity}, Springer&#x27;12], and in turn it is used in a significant number of papers. Thankfully a slightly weaker version of this lemma is true, with a caveat on how sublinear the vertex separators needs to be, and we provide the correction as a service to the community.

  匹配依据：MPC: secure multiparty computation

  </details>

- **The Native-Signature Boundary in Post-Quantum Distributed Authorization**
  2026-09-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.03547)
  Dariia Porechna

  <details><summary>摘要 / Abstract</summary>

  Post-quantum signature migration poses a distinct systems problem when authorization is distributed among multiple parties. In native threshold signing, the signature algorithm may determine key generation, share state, preprocessing, interaction, combination, refresh, and recovery. Architectures that evaluate threshold policy outside the native signing relation can reduce this coupling, but their authorization evidence is not accepted by an unchanged native verifier unless a trusted complete-key signer translates approval into a native signature. This paper organizes that design boundary through three properties: native-signature compatibility, unilateral-signing resistance, and threshold-layer agility. We classify specialized threshold signatures, generic MPC signing, distributed hash-based constructions, programmable multisignature and dual-gate authorization, and threshold-authorized HSM signing. A migration impact surface identifies which components change with the signature algorithm. Across the surveyed families, no design simultaneously provides native output, unilateral-signing resistance, and threshold-layer agility. This is an architectural tension, not an impossibility claim, and it clarifies why a replaceable API alone does not make distributed authorization cryptographically agile.

  匹配依据：MPC: mpc (context)

  </details>

- **Spruce: Scalable Private Outsourced Retrieval Using Compact Embeddings**
  2026-09-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.03376)
  Peichun Hua, Yunming Xiao

  <details><summary>摘要 / Abstract</summary>

  Retrieval-Augmented Generation (RAG) has made dense retrieval over large document collections a standard building block. Organizations increasingly outsource vector indexes to untrusted clouds, exposing proprietary corpora and user queries. Cryptographic protection is challenging because each query searches corpus-scale state, causing computation, correlated randomness, and communication to grow with the corpus. At million-document scale, a naive secure implementation takes minutes and about 90 GB of communication per query. Even recent optimized systems require 10--22 seconds. We propose Spruce (Scalable Private Outsourced Retrieval Using Compact Embeddings), which co-designs representations with the cryptographic protocol. Spruce learns compact binary codes that preserve candidates for full-precision reranking, replacing corpus-wide embedding scoring with efficient Hamming-distance computation under two-server multi-party computation (MPC). A corpus-calibrated fixed-radius protocol avoids multi-round candidate selection while preserving retrieval quality. Spruce also provides private cluster pruning, which trades minor quality loss for substantially less computation, and a one-core owner-operated dealer that removes cloud OT preprocessing bottlenecks. Across four corpora containing 383K--5.42M documents, Spruce preserves the original search quality with median candidate sets of only 382--1,952. At 10 Gbps inter-server bandwidth, full scans take 0.21--2.97 seconds, $4.8$--$6.7\times$ faster than the closest measured prior work. Private pruning takes 0.06--1.09 seconds, achieves $13.1$--$22.9\times$ speedups, and retains $93.9\%$--$97.3\%$ of full-float NDCG. On the largest corpus, pruning and the dealer jointly improve sustained throughput by $31.5\times$ at 1 Gbps per link.

  匹配依据：MPC: multi party computation

  </details>

- **Private Quantised Neural Network Inference**
  2026-09-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1880)
  Hendrik Eerikson, Sven Laur, Pille Pullonen-Raudvere

  <details><summary>摘要 / Abstract</summary>

  Neural networks based machine learning models are used in many classification problems yet privacy issues in model usage are mostly unresolved. When a model owner provides their model to other parties for inference, either the model owner has to share the parameters of the model or the model user must share their query and result with the model owner. Depending on the usage scenario, the user’s query or query result could contain sensitive information that the model provider should not see. And on the other hand, the model parameters themselves could be a valuable business secret or leak private training data. In such cases, neural network inference must be performed in a privacy preserving manner, for example, using secure multi-party computation (MPC). We propose protocols for the private inference of neural networks and evaluate them within the Sharemind MPC secure computation framework. Our protocols are based on the per-tensor quantisation scheme in PyTorch which maps floating point model parameters to 8-bit integer values. Quantisation improves the efficiency of our protocols and our protocols are interoperable with models trained using PyTorch. We extend constant round integer convolution and matrix multiplication protocols for quantised model weights, propose constant round protocols for re-quantising values and analyse the optimal secret share bit width for efficient re-quantisation. The resulting protocols are used to evaluate the VGG16 image classification network with an amortised throughput of 24.3 s per image classification in a LAN setting.

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **Subring VOLE over Galois Rings with Applications to ZK over $\\mathbb{Z}\_{p^k}$**
  2026-09-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1864)
  Ignacio Cascudo, Xiang Liu

  <details><summary>摘要 / Abstract</summary>

  Vector oblivious linear evaluation (VOLE) is a type of correlation that is widely used in multiparty computation (MPC) and zero-knowledge (ZK) proofs. Recently, the generation of VOLE correlation has become very efficient due to the pseudorandom correlation generator (PCGs) paradigm (Boyle et al. CCS 2018) and SoftSpokenOT (Roy Crypto 2022). This has driven a line of research on VOLE-based ZK, which enjoys linear prover time, low memory cost and post-quantum security. However, most existing works build VOLE and VOLE-based ZK over finite fields, whereas the constructions over integer rings are less satisfactory, especially in terms of communication and public verifiability. In this work, we address some of these problems using a newly introduced primitive called subring VOLE (srVOLE), which is a generalization of subfield VOLE to Galois rings. Specifically, (1) We propose two maliciously secure srVOLE protocols. One is a PCG-like protocol that achieves extremely low amortized communication. The other is a SoftSpoken-like protocol, which is compatible with the VOLE-in-the-head (VOLEitH) technique and thus can be used to construct publicly verifiable VOLE-based ZK. (2) We find that the VOLE correlation over $\mathbb{Z}_{2^k}$ used in Moz$\mathbb{Z}_{2^k}$arella (Baum et al. Crypto 2022) is a special case of our srVOLE. Therefore, based on our construction, their designated-verifier ZK protocol can be made publicly verifiable. (3) We adapt the QuickSilver (Yang et al. CCS 2021) protocols to any Galois ring and compare with existing VOLE-based ZK protocols over rings. For circuit satisfiability, our protocol only communicates 1 subring element per multiplication gate, reducing the communication by more than half. For polynomial satisfiability, our protocol supports arbitrary low-degree relations, overcoming the restrictions of existing work on degree-2 relations.

  匹配依据：MPC: multiparty computation

  </details>

- **Card-Based Computation in the Virtual Player Simulation Model**
  2026-09-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.02716)
  Suthee Ruangwises

  <details><summary>摘要 / Abstract</summary>

  Player simulation has recently emerged as a new direction in card-based cryptography, with protocols developed for simulating virtual players in physical card games such as Old Maid, UNO, and President. Unlike conventional card-based secure computation, player simulation imposes additional constraints: the cards represent a persistent game state, the remaining cards in a virtual player&#x27;s hand must be preserved after each action, and it is desirable to represent each card in the game by a single physical card. In this paper, we study generic card-based computation in the virtual player simulation model. We focus on games whose cards admit a publicly known ranking and propose two fundamental protocols. First, we present the Play-Minimum protocol, which securely selects and plays the minimum-value card from a virtual player&#x27;s hand when all cards in the deck have distinct values. By symmetry, the protocol can also be used to play the maximum-value card. Second, we present the Sorting protocol, which securely arranges a virtual player&#x27;s hand in nondecreasing order and remains applicable when multiple cards have the same value. These protocols provide generic computational primitives independent of any particular card game and constitute a step toward understanding the computational capabilities of the virtual player simulation model.

  匹配依据：MPC: secure computation

  </details>

- **(Im)possibility of Asynchronous MPC with Honest Majority over Blockchains**
  2026-09-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1860)
  Ashish Choudhury, Sannidhi V Hebbar, Aniket Kate, Pabitra Mandal, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  This work studies asynchronous verifiable secret sharing (AVSS) and asynchronous multi-party computation (AMPC) in the blockchain-hybrid model, where parties have black-box access to an ideal (asynchronous) blockchain functionality providing only persistence and eventual liveness. Motivated by the practical deployment of MPC in blockchain applications such as privacy-preserving payments and threshold wallets, we investigate whether blockchain access can improve the classical resilience bound of $n &gt; 3t$, where $n$ is the total number of parties, and $t$ is the number of parties that can be compromised by an adversary. In particular, in the blockchain-hybrid model, we provide a comprehensive set of lower and upper bounds across three cryptographic settings: (i) no trusted setup, (ii) trusted setup with Minicrypt assumptions, (iii) trusted setup with public-key assumptions. 1. We show that without a trusted setup, or under Minicrypt assumptions, even with a setup, the classical resilience bound for AMPC is inherent: AMPC is impossible for $n \leq 3t$, even against weaker fail-stop or omission adversaries. 2. We establish separations between AVSS and AMPC in the intermediate regime $2t 2t$ without any setup. Moreover, against a Byzantine adversary, again unlike AMPC, AVSS is possible for $n&gt;2t$ under Minicrypt assumptions with a setup. 3. In contrast, under public-key assumptions with trusted setup, we construct an AMPC protocol tolerating Byzantine adversaries whenever $n&gt;2t$. Our protocol leverages threshold homomorphic encryption, threshold signatures, commitments, and zero-knowledge proofs to minimize on-chain communication, achieving blockchain communication complexity independent of the circuit size. In the process, we define an efficient agreement on a common subset primitive for large messages in the blockchain-hybrid model, which can be of independent interest for secure distributed computing systems.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Distributed Key Generation for NTRU**
  2026-09-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1854)
  Patrick Hough, Jérôme Nguyen, Caroline Sandsbråten, Tjerand Silde

  <details><summary>摘要 / Abstract</summary>

  NTRU-based encryption enjoys compact keys and ciphertexts and admits non-interactive distributed decryption, making it an attractive basis for threshold encryption with applications to threshold FHE, threshold signatures, and electronic voting. All known protocols, however, assume a secret key shared by a trusted dealer. The public NTRU key $h = f^{-1}g$ is a nonlinear function of the secret, so distributed key generation (DKG) techniques for LWE-based schemes do not apply, and generic MPC is prohibitively expensive. We present the first dedicated DKG protocol for NTRU. Each party publishes an NTRU sample, defining a joint public key whose secret key is shared multiplicatively, and a multiplicative-to-additive (MtA) conversion yields the additive sharing required for non-interactive decryption. The protocol runs in few rounds and is actively secure with abort. At the heart of our DKG lies the MtA conversion, for which we give two efficient lattice-based certified constructions; one from additively homomorphic NTRU encryption and one from homomorphic secret sharing, both of which may be of independent interest. We demonstrate the protocol by building a threshold variant of NTRU-Encrypt, which we prove secure and instantiate with concrete parameters.

  匹配依据：MPC: secret sharing

  </details>

- **CRSF: Collusion-Resilient Privacy-Preserving Sensor Fusion with Byzantine-Robust Participation**
  2026-09-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.01096)
  Chao Yin, Haihong Tian, Zheng Yang, Haibin Zhang, Fabio Massacci, Chenglu Jin

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving sensor fusion enables an untrusted server to compute an aggregate result over distributed sensor measurements without learning either individual inputs or the final output. Recent garbled-circuit-based protocols provide an efficient realization of this functionality in a sensor--server--client architecture, but remain vulnerable to sensor--server collusion and Byzantine manipulation of sensor participation. These weaknesses can compromise honest-sensor privacy, incorrectly exclude honest sensors, and corrupt the computed fusion result, thereby undermining the security guarantees expected from the protocol. We present CRSF, a collusion-resilient sensor-fusion protocol that addresses these weaknesses while providing privacy, correctness with explicit abort, and liveness. CRSF introduces a Practical Byzantine Fault Tolerance (PBFT)-based agreement phase for sensor submissions and uses server-specific, status-dependent label release with threshold protection of circuit-input labels. This design prevents any Byzantine server from unilaterally manipulating sensor participation and prevents any admissible sensor-server coalition from obtaining enough secret material to compromise honest-sensor privacy. We implement CRSF and compare its online execution time with the most relevant state-of-the-art baseline. Our Google Cloud evaluation measures the total computation and communication cost of the online protocol under fault-free and representative faulty executions. Across a range of fault-tolerant fusion circuits and up to 261 sensors, CRSF demonstrates a highly practical trade-off between robust security and protocol performance.

  匹配依据：MPC: garbled circuit

  </details>

- **A Code-Based $(k,n)$-Threshold Secret Sharing Scheme with Integrity Verification**
  2026-09-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1850)
  Sapna Jyoti Patel, Sumit Kumar Debnath

  <details><summary>摘要 / Abstract</summary>

  Threshold secret sharing schemes (TSSS) enable a dealer to distribute a secret among multiple participants such that only authorized subsets can reconstruct the secret while unauthorized subsets obtain no information. Existing secret sharing schemes (SSS) are often constrained by limited secret size, non-threshold access structures, or the absence of mechanisms for verifying the authenticity of shares and the integrity of the reconstructed secret. In this paper, we propose a novel $(k,n)$-threshold secret sharing scheme based on linear Maximum Distance Separable (MDS) codes. The proposed construction supports the sharing of comparatively larger secrets by representing the secret as a matrix over a finite field and exploits the linearity of MDS codes to achieve efficient share generation and reconstruction. To strengthen reliability, the scheme incorporates cryptographic hash functions for share authentication and integrity verification of the reconstructed secret. We prove that the proposed scheme satisfies correctness and perfect secrecy, thereby providing unconditional security against unauthorized coalitions. Experimental evaluation demonstrates that the proposed construction achieves efficient share generation and reconstruction while outperforming existing code-based secret sharing schemes in terms of supported secret size, scalability, and practical runtime.

  匹配依据：MPC: secret sharing

  </details>

- **Quantum Secret Sharing with a Helper and Programmable Access Structures**
  2026-08-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.00220)
  Eric Chitambar, Sarah Hagen, David W. Kribs, Mike I. Nelson, Andrew Nemec

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) is a process in which the state of a quantum system is partitioned into multiple shares, allowing only specific subsets of shareholders to reconstruct the state, while others gain no information about its identity. In this work, we propose a variant of QSS, called ``helper QSS,&#x27;&#x27; which designates a special shareholder whose participation with any other group of parties is sufficient for recovering the state. We present different families of helper codes that function for an arbitrary number of parties and system sizes. As an application, we introduce the idea of a programmable access structure in QSS, which allows for a third-party programmer to independently choose the access structure of the code even after the shares are delivered to all the shareholders. This choice is made blindly, meaning that the programmer has no information about the secret being encoded, and it is implemented using the nonlocal process of quantum steering.

  匹配依据：MPC: secret sharing

  </details>

- **KORD: Breaking the Key-Generation Bottleneck in Dealerless FSS via Protocol--Hardware Co-Design**
  2026-08-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.30379)
  Yijing Peng, Lin Liu, Yujie Xue, Shaojing Fu, Shaoqing Li, Yaohua Wang, Rongmao Chen, Yang Guo

  <details><summary>摘要 / Abstract</summary>

  Function secret sharing (FSS) has become a core primitive in privacy-preserving computation. However, each FSS invocation requires a fresh pair of function keys generated by a trusted dealer , expands the system&#x27;s trust boundary and hinders practical deployment. Existing dealerless protocols eliminate this dependency, but incur substantial communication and a number of interaction rounds that grows linearly with the input bit-width, making key generation a major bottleneck. This paper present KORD, a protocol--hardware co-design that dramatically reduces the cost of dealerless FSS key generation. At its core is a pair of special-purpose chips that establish a common root of trust through mutual attestation and, within it, reconstruct FSS keys---eliminating the need for a dealer. This root of trust further forms a security boundary within which KORD restructures the generation protocol, collapsing the interaction of prior dealerless protocols into a single round, independent of GGM depth. A cross-key scheduling scheme then interleaves independent GGM-tree traversals, sustaining high computational throughput. KORD reduces per-key-generation communication by 7,633--70,274$\times$ over the state-of-the-art distributed FSS protocol across a comprehensive suite of FSS building blocks. Post-route analysis projects 12.75 million 32-bit DPF keys per second at 204 MHz using 21.5K LUTs, with 99.8% AES lane utilization. On private ResNet-18 inference, KORD cuts the share of end-to-end time spent on key generation from over 96% to 11.9%.

  匹配依据：MPC: secret sharing

  </details>

- **Codes for Quantum Secret Sharing with a Helper**
  2026-08-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.00234)
  Eric Chitambar, Sarah Hagen, David W. Kribs, Zhao Ma, Mike I. Nelson, Andrew Nemec

  <details><summary>摘要 / Abstract</summary>

  Helper quantum secret sharing is a form of secret sharing defined by its unique access structure. One special fixed party, called the helper, can work together with any other party to fully decode the secret. A blind helper is one who can provide this assistance while not holding any local information about the encoded secret. In this work, we analyze the general structure of QSS helper codes and present new code constructions. We fully characterize the structure of blind helper stabilizer codes and show that for the encoding of a single qubit, recovery is always possible using one-way local operations and classical communication (LOCC) from the helper to the targeted party. Furthermore, we demonstrate how such codes also allow for the helper to target larger subsets of parties by one-way LOCC, enabling them to be authorized to recover the secret. Finally, when each party only holds a qubit, we identify the general form of all helper codes (including non-stabilizer codes) and find that LOCC recovery is only possible in special cases.

  匹配依据：MPC: secret sharing

  </details>

- **Thresholding Post-Quantum Signatures**
  2026-08-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.26792)
  Francesco De Sclavis, Matteo Nardelli, Marco Pedicini

  <details><summary>摘要 / Abstract</summary>

  Threshold signature schemes distribute the signing process among $T$ parties out of $N$. They enable a variety of applications and their research is also motivated by a recent NIST call. However, applications are dominated by pre-quantum signatures, which are more efficient but not secure in the post-quantum setting. This paper investigates existing post-quantum signatures, based on a variety of paradigms: lattice problems, one-way (hash) functions, cryptographic group actions, isogenies and multivariate systems. We propose a classification (divided by paradigm) of existing tools that are used to build $T$-out-of-$N$ schemes from digital signatures. We also include general approaches based on FHE, MPC or ZKP.

  匹配依据：MPC: mpc (context)

  </details>

- **SLIDE: Shuffle Shamir Secret Shares Uniformly with Linear Online Communication and Guaranteed Output Delivery**
  2026-08-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.27129)
  Jiacheng Gao, Moyang Xie, Yuan Zhang, Sheng Zhong

  <details><summary>摘要 / Abstract</summary>

  We revisit shuffle protocols for Shamir secret sharing. Existing constructions either produce non-uniform shuffles or incur high communication and round complexity, sometimes exponential in the number of parties. We propose two new shuffle protocols that achieve uniform shuffling with communication complexity $O((k+l)n^2m\log m/\log k)$ for an $m$-by-$l$ matrix shared among $n$ parties, where $k\leq m$ is a tunable parameter. The first protocol is concretely efficient, while the second achieves the best-known $O(nml)$ online communication and $O(n)$ rounds. Experiments show significant improvements in online efficiency and total cost over prior work. Our key technical ingredient is a novel permutation sharing technique that represents permutations using smaller permutation matrices, making their application significantly more efficient. The first protocol applies independent secret permutations sequentially, while the second builds on shuffle correlation to achieve optimal online complexity. We further extend shuffle correlation to support guaranteed output delivery with linear online communication, yielding SLIDE, the first protocol to achieve both $O(nml)$ online communication and guaranteed output delivery. Our constructions rely only on basic Shamir secret sharing over any field of size greater than $n$. As shuffling is a fundamental primitive for MPC tasks such as sorting and oblivious data structures, our results enable more efficient and scalable secure computation in practice.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Revisiting Continuous Noise Sampling for Multi-Party Differential Privacy**
  2026-08-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.27766)
  Yucheng Fu, Tianhao Wang

  <details><summary>摘要 / Abstract</summary>

  Combining secure multi-party computation (MPC) with differential privacy (DP) enables multiple parties to release aggregate statistics without a trusted curator, and the core primitive is the protocol to sample noise from a continuous distribution under finite-precision arithmetic. In this paper, we revisit the continuous noise sampling protocols and present several improvements in both security and efficiency. We start by identifying a vulnerability in widely used sample-and-scale constructions. We demonstrate that the scaling operation in arithmetic circuits confines the noise to a sparse, publicly known set of values, so that an adversary can observe the released noisy queries and decide which dataset produced them. As concrete demonstrations, we instantiate attacks on two systems employing such ``flawed&#x27;&#x27; sampling protocols: Orchard (OSDI&#x27;20) for DP secure aggregation and DP-BREM$^+$ (USENIX Sec&#x27;25) for DP federated learning. We report a near-$100\%$ attack success rate on both systems, under any noise scaler $s\geq 2$ used in practice. The leakage we reveal is intrinsic to the scaling operation, and direct repairs either substantially sacrifice utility or add significant precision bits to make the sampling more expensive. To address the security and efficiency issues together, we turn to discrete sampling at the granularity of individual biased bits. We make several optimizations to the sampler and prove its security. Our implementation achieves $4\times \sim 612\times$ speedup over existing secure discrete samplers and orders-of-magnitude speedup over the insecure sample-and-scale paradigm, with negligible utility loss compared to the ideal continuous mechanism.

  匹配依据：MPC: secure multi party computation

  </details>

- **Entirely nonlocal quantum magic without entanglement**
  2026-08-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.25950)
  Fuchuan Wei, Ruixia Wang, Yujia Zhang, Huihui Li, Junfeng Li, Fei Yan, Zi-Wen Liu

  <details><summary>摘要 / Abstract</summary>

  Nonstabilizerness, or magic, is an archetypal \emph{quantum} resource that is necessary for quantum computational advantage. Here we uncover a phenomenon seemingly at odds with the quantum nature of magic: entirely nonlocal magic (ENM)---magic present only in correlations and absent from each party&#x27;s marginal---can live without entanglement. We systematically study this separation and show it is universal and operationally reversible: every magical state or channel can be encoded into and recovered from a separable ENM realization using only local stabilizer processing and classical communication. We leverage this mechanism to devise an activation key protocol in which a classical key controls access to non-Clifford operations. We further formulate magic secret sharing, in which computational power inaccessible to any party alone becomes accessible through cooperation. On a superconducting quantum processor, we experimentally demonstrate activation key and network computing primitives, together with separable ENM state preparation and extraction protocols. Together, our results establish that magic can be classically activated, localized, and secret-shared without entanglement, providing new resource-control primitives for distributed quantum computation.

  匹配依据：MPC: secret sharing

  </details>

- **Dealing Haystack: Towards Trustless Haystack in the Optimistic Setting**
  2026-08-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1804)
  Isabel Muñoz, Isaac Agudo, Marco López, Daniel Morales

  <details><summary>摘要 / Abstract</summary>

  Hash-based constructions occupy a distinctive position among post-quantum signatures: their security reduces to well-tested properties of hash functions rather than to newer assumptions such as lattices or isogenies. This work focuses on stateful schemes instead of stateless, because the former are considerably more efficient. However, they have the problem of state handling, since reusing a one-time key twice enables signature forgeries. Despite threshold signatures mitigate this problem by spreading trust among a set of disjoint parties, building them from hash-based schemes is difficult, since these lack the homomorphic structure needed to recombine partial signatures, and generic multiparty computation can be expensive for hash-based constructions. Kelsey, Lang and Lucks recently proposed Haystack, the first threshold scheme for hash-based signatures producing standard LMS or XMSS signatures, at the cost of a fully trusted setup and a large common reference value. We analyze Haystack along two dimensions: performance and security. First, as Haystack lacks an implementation and realistic benchmarking, we implement the protocol in Java and produce a network-aware evaluation of its viability in real deployments, concluding that it performs comparably to other post-quantum threshold schemes. Second, we relax the trust placed in the dealer. For that, we introduce a variant of the setup built on an optimistic, lightweight MPC-based partial-DKG. It does not remove the dealer&#x27;s ability to forge, but it prevents it from impersonating trustees within the signing protocol, while preserving the standard signature format. Also, an optional succinct-argument layer provides public auditability. We further consider a full-DKG setting with no dealer and where the trustees run the entire setup under MPC. Both variants are implemented in MP-SPDZ and their costs have been analyzed.

  匹配依据：MPC: multiparty computation

  </details>

- **Ideal Secret Sharing Schemes over Small Domains**
  2026-08-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1794)
  Amos Beimel, Aner Ben-Efraim, Oriol Farràs, Adriana Moya

  <details><summary>摘要 / Abstract</summary>

  In any secret sharing scheme, the size of each share must be at least as large as the size of the secret. Schemes that attain this lower bound are called $k$-ideal, where $k$ is the size of the domain of the secrets and shares, or simply ideal if they are $k$-ideal for some $k$. An access structure is called $k$-ideal if it admits a $k$-ideal secret sharing scheme. The characterization of ideal access structures is a longstanding open problem at the intersection of cryptography, matroid theory, and information theory, previously solved only for $k=2$ and $k=3$. In this work, we solve this problem for $k=4$ and $k=6$. Our results exploit the connections between ideal secret sharing schemes and matroids and new techniques based on latin squares. For $k=4$, we show that an access structure is $4$-ideal if and only if it admits a $\mathbb{F}_4$-linear ideal secret sharing scheme, i.e., a scheme where the shares and the secret are elements of $\mathbb{F}_4$ and the sharing and reconstruction functions are linear. To prove this result, we show that the class of matroids determined by ideal $\mathbb{F}_4$-linear schemes coincides with those determined by $4$-ideal schemes. For $k=6$, we prove that an access structure admits a $6$-ideal scheme if and only if it admits a $k$-ideal scheme for every $k\geq 2$. This result shows that domains of size $k=6$ are the most restrictive domains for constructing ideal secret sharing schemes, and that $6$-ideal schemes can be essentially built by combining ideal $\mathbb{F}_2$-linear schemes with ideal $\mathbb{F}_3$-linear schemes via the Chinese Remainder Theorem. Beyond these characterizations, our main technical contributions are the introduction of new techniques for analyzing ideal secret sharing schemes, extending the connections between ideal threshold schemes and latin squares to the general case, and the classification of the values of $k$ for which some relevant matroids are $k$-entropic.

  匹配依据：MPC: secret sharing

  </details>

- **The Limits of $t$-Private Share Conversion**
  2026-08-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1780)
  Bar Alon

  <details><summary>摘要 / Abstract</summary>

  Private information retrieval (PIR) protocols allow a user to retrieve an entry from a database held by several servers without revealing any information about the index to any individual server. State-of-the-art information-theoretic PIR protocols are based on a combination of matching vectors over the ring $\mathbb{Z}_m$ and decoding polynomials (Efremenko, SICOMP 2012; Dvir and Gopi, STOC 2015; Ghasemi, Kopparty, and Sudan, STOC 2025). Decoding polynomials are sparse polynomials over a field $\mathbb{F}_q$, where $q$ is a prime power coprime to $m$, that evaluate to a nonzero value at $1$ and to $0$ on a certain set of inputs determined by $m$. The properties of decoding polynomials were abstracted by Beimel, Ishai, Kushilevitz, and Orlov (CCC 2012) through the notion of share conversions. Share conversions allow a set of parties to locally convert a secret shared under one scheme into a related secret shared under another scheme. They constructed a share conversion from $\mathbb{Z}_m$ to $\mathbb{F}_{q}$ for various values of $m$ and prime-powers $q$. More recent PIR protocols by Dvir and Gopi and by Ghasemi et al. were abstracted by Alon, Beimel, and Lasri (TCC 2025). The share conversion they considered transforms shares from the ring $\mathbb{Z}_m$ to a finite field $\mathbb{F}_q$, where $q$ is a prime-power coprime to $m$. We observe that if the initial conversion is based on a $t$-private secret-sharing scheme, then the resulting PIR protocol of Alon et al. is also $t$-private: no set of $t$ servers learns any information about the user&#x27;s index. We call such share conversions $t$-private share conversions. Moreover, the resulting PIR protocol could potentially achieve communication complexity better than that of the best-known $t$-private PIR protocols, due to Woodruff and Yekhanin (CCC 2005) and Barkol, Ishai, and Weinreb (APPROX-RANDOM 2007). This raises the natural question of whether $t$-private share conversions exist. We show that there is no $t$-private share conversion from $\mathbb{Z}_m$ to $\mathbb{F}_q$ when $t\geq 2$ and $q$ is coprime to $m$. As a result, the PIR framework of Alon et al. cannot be instantiated in a way that yields a $t$-private PIR protocol. We further generalize the result to conversions whose output is in the ring $\mathbb{Z}_{m&#x27;}$.

  匹配依据：MPC: secret sharing

  </details>

- **Inclusion-Minimal local indistinguishability: a weak form of nonlocality**
  2026-08-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.22393)
  Mao-Sheng Li, Zong-Xing Xiong, Zhu-Jun Zheng, Yan-Ling Wang

  <details><summary>摘要 / Abstract</summary>

  Local discrimination of quantum states is a fundamental task in distributed quantum information processing and underlies applications such as quantum communication, data hiding, and secret sharing. Here we investigate a weak form of local indistinguishability by asking how easily it can disappear when the candidate set is reduced or an additional copy of the unknown state is supplied. We introduce inclusion-minimal locally indistinguishable sets, namely, locally indistinguishable sets for which every proper subset is perfectly distinguishable by local operations and classical communication (LOCC), and show that every finite locally indistinguishable set contains such a subset. We further find that any inclusion-minimal locally indistinguishable sets becomes perfectly distinguishable by LOCC when two identical copies are available, although a single copy is insufficient. Fininally, We construct explicit inclusion-minimal locally indistinguishable product-state sets in $(\mathbb C^d)^{\otimes n}$ for every odd $d=2k+1$ and $n\ge2$. These results show that local indistinguishability can be nontrivial at the single-copy level yet fragile under either the removal of candidate states or a modest increase in copy resources, providing a complementary perspective on the structure of quantum nonlocality.

  匹配依据：MPC: secret sharing

  </details>

- **Efficient Additive Randomized Encodings for String Oblivious Transfer: A Core Primitive for General Functions**
  2026-08-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1781)
  Masaya Yoshimura, Kyoichi Asano, Yugo Kasashima, Mitsugu Iwamoto, Yohei Watanabe

  <details><summary>摘要 / Abstract</summary>

  Additive Randomized Encodings (AREs) provide a lightweight route to non-interactive secure computation: each party locally produces a randomized encoding of its input, and an evaluator learns only the function value from the sum of these encodings. Prior frameworks for constructing AREs for general functions ultimately hinge on an efficient ARE for string oblivious transfer (SOT), making SOT the core efficiency bottleneck. We revisit this final step and present improved ARE constructions for SOT. First, we streamline the recent PKE-based approach by directly constructing the required one-sided ARE (OSARE) for SOT. This yields a perfectly correct, statistically one-sided secure OSARE for SOT of size $\mathcal{O}(\lambda)$, improving the intermediate overhead and, consequently, the overall size of the resulting PKE-based ARE. Second, we give a pairing-free ARE for SOT under the Squaring DDH assumption. Our construction is compatible with Halevi et al.&#x27;s efficient equality-to-SOT methodology: we build an ARE for Rabin-OT that embeds a message in the equality-checking procedure and then transform it to SOT while incurring only constant-factor communication overhead and no additional correctness error. The resulting ARE for SOT has size $\mathcal{O}(\lambda)$ and negligible correctness error.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **Multi-Party Private Set Intersection with Optimal Online Round Complexity and Updatability**
  2026-08-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1774)
  Jiadi Zhang, Hao Wang, Ye Su, Xiaochao Wei, Lei Wu, Zhi Li

  <details><summary>摘要 / Abstract</summary>

  Multi-party private set intersection (MPSI) enables multiple parties to securely compute the intersection of their private datasets without revealing any information beyond the intersection itself. However, as the number of participants scales, the performance of multi-party PSI protocols is significantly influenced, with the number of interaction rounds emerging as a critical bottleneck. In this paper, we propose a novel MPSI protocol and its updatable extension based on function secret sharing and oblivious key-value stores, achieving optimal one-pass online interaction. Our construction guarantees security in the semi-honest model, resisting collusion among any $n-1$ parties when the Leader is honest, and among any $n-2$ parties when the Leader is corrupted—an assumption that aligns well with many practical deployment scenarios. Furthermore, our multi-party updatable PSI (MUPSI) protocol allows parties to efficiently compute the intersection over dynamically updated sets. Our MUPSI protocol achieves collusion resistance against any $n-1$ participants, assuming an honest Leader. It ensures that both computational and communication complexities scale exclusively with the size of the updates rather than the entire datasets, exhibiting superior performance particularly when handling unbalanced sets and large participant cohorts. All proposed protocols exhibit strong scalability with respect to participant count. We demonstrate the superiority of our protocols through implementation and comparison with state-of-the-art MPSI protocols. Experiments show that when the number of participants ranges from $20$ to $140$ and the set size ranges from $2^{12}$ to $2^{20}$, our MPSI protocol is competitive. Notably, in the WAN setting with $140$ participants and a set size of $2^{20}$, the running time is reduced by $49.1\times$ compared with GLW+24. Our MUPSI protocol avoids PSI operations on entire sets, achieving a reduction in running time by an order of magnitude.

  匹配依据：MPC: private set intersection, secret sharing

  </details>

- **Multi-PGBF: Efficient Oblivious Key-Value Store and Application to Private Set Intersection**
  2026-08-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1772)
  Mingli Wu, Tsz Hon Yuen, Man Ho Au, Siu-Ming Yiu

  <details><summary>摘要 / Abstract</summary>

  An oblivious key-value store is a data structure that can encode and decode $n$ key-value pairs in a table of size $m$ obliviously. After encoding, one cannot distinguish the encoded key-value pairs from other key-value pairs in the input domain. In this paper, we first propose a data structure called Peelable Garbled Bloom Filter (PGBF), which encodes the key-value pairs in a similar way to peeling and unpeeling an \emph{onion}. Specifically, it can divide the key-value pair set (i.e., onion) as multiple subsets (i.e., peels) and order them from the outermost peel to the innermost peel by using a counting Bloom filter. However, using a small expansion rate (i.e., $\eta=m/n$) in PGBF will result in a non-empty core issue with non-negligible probability. To handle this issue, we propose Multi-PGBF by combining multiple PGBFs to do the peelings and unpeelings recursively. In addition, we propose a variant C-Multi-PGBF by clustering a large set into small sets to achieve faster encoding efficiency. Our experiments show that Multi-PGBF and C-Multi-PGBF obtain the best encoding and decoding efficiency. Multi-PGBF improves the encoding time of RR (CCS’22) by $65.1\%\sim 77.6\%$, while C-Multi-PGBF improves the encoding time of the clustered RR variant by $60.2\%\sim 64.7\%$. For decoding, Multi-PGBF is $28.6\%\sim 62.4\%$ faster than RR (CCS&#x27;22) and $89.7\%\sim 96.3\%$ faster than RB-OKVS (Usenix&#x27;23). When integrated into the state-of-the-art two-party and multi-party private set intersection protocols (Eurocrypt&#x27;21, Usenix&#x27;24), Multi-PGBF and C-Multi-PGBF lead to faster protocols than those using existing OKVS constructions in most settings.

  匹配依据：MPC: private set intersection

  </details>

- **Rank Measures and Exponential Lower Bounds for Multilinear Secret Sharing**
  2026-08-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1769)
  Shahram Khazaei

  <details><summary>摘要 / Abstract</summary>

  Multilinear secret sharing can amortize share size over a vector secret, so scalar linear lower bounds need not survive normalization by the secret dimension. We prove that the Razborov–G´al rank measure does survive this amortization: every multi-target monotone span program satisfies a rank inequality in which the target dimension appears multiplicatively. Combined with the characteristic-separated witnesses of Pitassi and Robere, this gives an explicit family of access structures whose average and maximum multilinear information ratios are exponential over every finite field, settling the worst-case order at $2^{\Theta(n)}$. We also study arbitrary sharing algorithms with affine-linear reconstruction under non-perfect security notions, including the pairwise statistical security of Beimel–Othman–Peter and the partial privacy of Jafari–Khazaei. Combining these affine-reconstruction results with the degree-reduction theorem of Beimel–Othman–Peter gives corresponding fixed-degree lower bounds under both security notions, in particular for subexponential secret dimension.

  匹配依据：MPC: secret sharing

  </details>

- **Constant-round MPC protocols with Fall-back Security**
  2026-08-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1768)
  Anasuya Acharya, Aditya Patankar, Arpita Patra, Divya Ravi, Raghavendra Vernekar

  <details><summary>摘要 / Abstract</summary>

  The notion of Best-of-Both-Worlds introduced in the work of Ishai et al. (CRYPTO 2006) investigated whether an MPC protocol can simultaneously provide two incomparable security guarantees depending on the number of corrupted parties. As a special case of this, Chaum et al. initiated the study of protocols that tolerate unbounded corruption within a certain adversary structure and PPT corruption of any number of parties beyond that. More recently, Acharya et al. (CRYPTO 2023) formalized this notion as MPC with fall-back security. Although the feasibility of such protocols has now been thoroughly studied in prior works, most of the existing protocols require round complexity linear in the number of parties and the computation size. In this work, we study the round complexity of MPC with fall-back security in the threshold corruption setting, presenting constant-round protocols for optimal thresholds. We present a semi-honest fall-back secure protocol for $t &lt; \frac{n}{2}$ with 3 rounds, in the plain model, whereas the best known protocol in the same setting takes at least 11 rounds. In the CRS model, we present a maliciously fall-back secure protocol for the same threshold with 4 rounds, satisfying unanimous abort (UA). Finally, we extend this to a 5-round protocol that satisfies fairness in the presence of unbounded adversaries for $t &lt; \frac{n}{2}$ corruptions and UA tolerating PPT adversaries for arbitrary corruption beyond that. In the malicious setting, we construct the first constant-round fall-back secure protocols.

  匹配依据：MPC: mpc (context)

  </details>

- **TrustRAG: Blockchain-Enhanced RAG via Committee-Based Credibility Scoring**
  2026-08-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.20097)
  Baixiang Liu, Haotian Che, Yuan Li

  <details><summary>摘要 / Abstract</summary>

  Retrieval-Augmented Generation (RAG) lets Large Language Models (LLMs) pull in up-to-date, domain-specific information instead of relying only on what they were trained on. Yet most RAG systems still draw from centralized databases with limited oversight, making it difficult to verify where a document came from, whether it has been tampered with, or whether it should be trusted at all. This is a serious problem in domains where both the timeliness and accuracy of retrieved content are critical, such as healthcare, finance, logistics, and legal case law, where a wrong or manipulated document can directly lead to bad decisions. We present TrustRAG, a committee-based, blockchain-backed RAG system: before a document is used, it is certified by a committee of domain experts through a zero-knowledge protocol, and the committee&#x27;s hidden scores are combined via secure multi-party computation into a trust score that any client can verify. These scores, along with the underlying document data, are maintained jointly across chains through hash commitments, so no document or score can be silently altered or dropped, and every ranking can be independently replayed and checked.

  匹配依据：MPC: secure multi party computation

  </details>

- **Round-Preserving Compilers for Super-Rushing Secure MPC**
  2026-08-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1745)
  Michele Ciampi, Divya Ravi, Mingrui Zou

  <details><summary>摘要 / Abstract</summary>

  Practical implementations of synchronous MPC protocols typically require each party to advance to the next round as soon as they have received all expected messages. This deviates from the theoretical synchronous round-based model, where instead each party advances in the next round after a timeout. To capture this gap between theory and practice, Asharov, Chandramouli, Cohen and Ishai in Eurocrypt 2025 proposed a new model where the adversary is super-rushing. In this, the adversary can see future messages of some honest parties before delivering current-round messages to slower ones. In this work, we study super-rushing security in both the computational and statistical settings, and design round-preserving compilers that transform standard synchronous MPC protocols into ones secure against super-rushing adversaries. Ours is the first work to investigate the security of computational MPC protocols against a super-rushing adversary.

  匹配依据：MPC: mpc (context)

  </details>

- **Privacy-Preserving Detection of Rare Disease-Associated Cell Subsets via Secure Multi-Party Computation**
  2026-08-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.20118)
  Ş. Selcan Magara, Esther Havemann, Debora Jutz, Ali Burak Ünal, Mete Akgün

  <details><summary>摘要 / Abstract</summary>

  The detection of rare disease-associated cell subsets from high-dimensional single-cell measurements is critical for understanding diseases such as leukaemia and viral infections. CellCnn, a convolutional neural network (CNN) designed for this task, has demonstrated the ability to identify phenotype-associated cell populations at frequencies as low as 0.01\%. Training such models reliably requires patient cohorts that are larger and more diverse than any single institution can typically assemble, and the underlying single-cell data is too sensitive to share across institutional boundaries under existing privacy regulations. We propose a secure multi-party computation (MPC) framework that enables the training and inference of CellCnn entirely on secret-shared data. This ensures that neither the participants nor the computing servers ever observe raw patient data or intermediate values. Evaluated on benchmark single-cell datasets for cytomegalovirus infection (CMV) and acute myeloid leukaemia (AML), our implementation preserves accuracy close to its plaintext counterpart while outperforming the prior privacy-preserving baseline. In contrast to earlier privacy-preserving approaches that removed components such as ReLU activations and bias terms, our method retains these key parts of the CellCnn architecture and supports accurate analysis without exposing raw patient data.

  匹配依据：MPC: secure multi party computation

  </details>

- **Jamming Extensions of Quantum Correlations Lead to Hidden Superluminal Signaling**
  2026-08-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.20247)
  Ravishankar Ramanathan, Xie Sicheng, Michał Eckstein, Paweł Horodecki

  <details><summary>摘要 / Abstract</summary>

  Relativistic causality in certain spacetime configurations permits jamming - superluminal causal influences that nevertheless do not enable superluminal signaling. We fully characterize the correlations compatible with relativistic causality (RC) by extending the operator framework of PRL 104, 140404. When the underlying state is required to be quantum, we prove that any nontrivial jamming - whether state-independent or state-dependent - necessarily leads to hidden superluminal signaling. Thus, the only consistent possibilities are standard quantum correlations without jamming or the full relativistically causal correlation set, with intermediate jamming extensions of quantum correlations leading to signaling. As an application of our characterization, we investigate the security of device-independent (DI) cryptographic primitives against adversaries constrained only by relativistic causality. We construct explicit RC attacks that break DI bit commitment and DI secret sharing in jamming geometries, even when these protocols remain secure against no-signaling adversaries. Our results show that security against relativistic adversaries requires behaviors to be specified together with the spacetime locations of their measurement events; input-output statistics alone are insufficient.

  匹配依据：MPC: secret sharing

  </details>

- **One Proof to Rule Them All: Practical, Sublinear Verification for Actively Secure MPC on $\\mathbb{Z}\_{2^k}$ with Dishonest Majority and a Dealer (Full Version)**
  2026-08-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1741)
  Andreas Brüggemann, Ariel Nof, Thomas Schneider

  <details><summary>摘要 / Abstract</summary>

  Towards bridging the gap between passively and actively secure multiparty computation (MPC), the use of sublinear distributed zero-knowledge (DZK) proofs gained popularity. Such proofs enable extending a passively secure protocol by adding a verification step whose communication is sublinear in the circuit size. For arbitrarily many parties and a dishonest majority, adding a trusted dealer enables efficient computation, as recently shown by Asterisk (IEEE S&amp;P&#x27;24) without requiring DZK. This setting is also compatible with DZK, as shown by Boyle et al. (CRYPTO&#x27;21). Unfortunately, their approach is not tailored to computation over a ring $\mathbb{Z}_{2^k}$, often favored for concrete efficiency and practicality, resulting in high computational overhead. In the honest majority setting with few parties, Li et al. (CCS&#x27;24) optimized DZK to rings, achieving significant performance improvements. In this work, we propose the first sublinear verification protocol that is both, designed for the $n$-party dishonest majority setting with a dealer, and tailored to computation over a ring $\mathbb{Z}_{2^k}$, combining and improving upon both approaches above. Previous approaches used $n$ DZK proofs to check correct behavior for each individual party. Instead, we show how to verify in a single, novel DZK proof that all parties together behave correctly. This decreases the communication complexity for verification from $\mathcal{O}(n \cdot \log m)$ to $\mathcal{O}(n + \log m)$ ring elements per party for $m$ multiplications. Hence, for the first time, active security using DZK scales well with the number of parties $n$. We provide the first public implementation for DZK with arbitrary $n$ and a dealer and show its practical efficiency. For $m=10^6$ multiplications across 30 layers, communication increases by only 0.7% over the passively secure base protocol with only moderate computation overhead. This becomes especially useful in a WAN setting, where we achieve active security at only 34% run time overhead over the passive variant. Compared to Asterisk (IEEE S&amp;P&#x27;24), our protocol has 1.8x better communication and improves run time by 2.5x in WAN and 11.9x in LAN.

  匹配依据：MPC: secure multiparty computation

  </details>

- **FESC: Remodeling Long-Context Private Inference with Encrypted State-Space Models**
  2026-08-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.17442)
  Yufan Zhu, Chao Jin, Khin Mi Mi Aung, Xiaokui Xiao

  <details><summary>摘要 / Abstract</summary>

  Processing long, sensitive documents with machine-learning models requires efficient, privacy-preserving long-context inference. Prior private inference systems optimize or distribute encrypted Transformer attention, but its quadratic token-pair work remains the bottleneck as sequence length grows. Selective state-space models (SSMs) offer linear-time recurrence, yet direct encrypted implementation incurs linear multiplicative depth, sequence-wide state residency, or dense FHE-MPC conversion. We present Factorized Encrypted Scan-Contract (FESC), a hybrid FHE-MPC system for private long-context selective SSM inference. Its factorized scan-contract keeps input-dependent transitions compact across conversion boundaries, composes them without dense expansion, streams state chunks on demand, and contracts outputs before conversion. We demonstrate interface compatibility of the scan-contract implementation across invariant and selective SSM architectures. For our Mamba-2 instantiation, we design GPU-optimized CKKS kernels for linear computations, MPC protocols for SiLU, softplus, exponential, and RMSNorm, with approximation-aware fine-tuning. To our knowledge, FESC is the first private long-document inference system to complete native end-to-end execution at $L \geq 1{,}024$ on a single GPU. At $L = 2{,}048$, a 12-layer Mamba-base model completes inference in 77.3 minutes on one A100 GPU with a peak memory footprint of 32.7 GB, while maintaining near-plaintext accuracy on the evaluated long-document tasks.

  匹配依据：MPC: mpc (context)

  </details>

- **Efficient Private Set Union from Multi-Query Oblivious Membership Transfer**
  2026-08-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1721)
  Yewei Guan, Hua Guo, Man Ho Au, Jiarong Huo, Renheng Wang

  <details><summary>摘要 / Abstract</summary>

  Private Set Union (PSU) allows two parties to compute the union of their private sets while revealing nothing beyond the union. Existing PSU protocols mainly follow two paradigms: reverse private membership test (RPMT) and invertible Bloom lookup table (IBLT). IBLT-based protocols achieve linear complexity using lightweight symmetric-key operations and offer excellent concrete efficiency. RPMT, on the other hand, provides a more general membership-testing functionality that can serve as a reusable building block for PSU and other private-set computations. However, existing RPMT-based protocols either rely on costly building blocks, such as public-key operations and generic secure two-party computation, or incur super-linear complexity. This raises a natural question: can the generality of the RPMT paradigm be retained while matching the asymptotic and concrete efficiency of IBLT-based PSU? In this work, we answer this question affirmatively by introducing a lightweight mechanism for multi-query membership testing. Our mechanism yields a concretely efficient multi-query RPMT (mqRPMT) protocol that is useful beyond PSU and may be of independent interest. Building on this protocol, we construct a PSU protocol with linear computation and communication complexity. Our construction avoids expensive public-key operations and generic secure two-party computation, relying instead on efficient symmetric-key primitives. We extensively evaluate our protocol against state-of-the-art PSU protocols from both the RPMT and IBLT paradigms. Compared with the leading RPMT-based PSU protocol from PKC 2024, our construction is $41.7\times$ $-$ $48.9\times$ faster in the LAN setting and up to $4.5\times$ faster in WAN settings. Compared with the leading IBLT-based PSU protocol from EUROCRYPT 2026, our protocol achieves competitive and, in several metrics, superior performance: it is $1.9\times$ $-$ $2.5\times$ faster in LAN settings and reduces communication by up to $1.4\times$. These results demonstrate that the broader applicability of the RPMT abstraction need not come at the cost of asymptotic or concrete efficiency.

  匹配依据：MPC: private set union, secure two party computation

  </details>

- **Efficient Fuzzy PSI under One-Sided Assumptions**
  2026-08-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.17770)
  Xinpeng Yang, Meng Hao, Yanxue Jia, Chenkai Weng, Yonggang Wen, Tianwei Zhang

  <details><summary>摘要 / Abstract</summary>

  Fuzzy private set intersection (PSI) enables two parties to identify approximately matching elements between their input sets, where two elements are considered a match if their distance is at most a threshold $δ$ under a given metric. Although substantial progress has been made, existing constructions for general Minkowski distances either rely on strong two-sided geometric separation assumptions or incur substantial overhead under one-sided assumptions. In this work, we present the first concretely efficient fuzzy PSI protocols for general $L_{p\in[1,\infty]}$ distances under one-sided assumptions, relying solely on lightweight symmetric-key primitives. Our constructions support both sender-sided and receiver-sided settings. We further study sparser input distributions and present more efficient protocols tailored to this case. To reduce the overhead scaling with $δ$, we non-trivially incorporate prefix trie techniques into our protocols, achieving $O(\logδ)$ complexity for general $L_{p\in[1,\infty]}$ distances for the first time, improving upon $O((\logδ)^d)$ or $O(δ)$ complexities of prior works. Extensive experiments, across a wide range of parameter settings, show that our protocols significantly outperform prior works under the same assumptions. Specifically, against van Baarsen and Pu (EUROCRYPT&#x27;24), our protocols achieve up to $248\times$ faster computation and up to $20\times$ lower communication. Against Dang et al. (CCS&#x27;25), we achieve up to $568\times$ speedup and up to $63\times$ communication reduction. Against Bui et al. (ASIACRYPT&#x27;25), we achieve up to $4978\times$ faster computation and up to $282\times$ lower communication.

  匹配依据：MPC: private set intersection

  </details>

- **CryptDough: A Unified Analytics Engine for Secure Multiparty Computation**
  2026-08-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.17529)
  Muhammad Faisal, Alessandra Lanz, Sam Buxbaum, Adam Godel, Vasiliki Kalavri, Mayank Varia, John Liagouris

  <details><summary>摘要 / Abstract</summary>

  We present CryptDough, a unified analytics engine for secure multiparty computation (MPC). CryptDough enables multiple distrusting parties to jointly execute a data analysis pipeline on their private inputs and learn nothing beyond the result (e.g., aggregate statistics). Unlike existing MPC solutions that support a single threat model or workload type, CryptDough provides built-in support for cross-domain analytics (relational, time series, ML inference) under various threat models, all within the same system runtime. CryptDough contributes (i) a hierarchical system design that facilitates modularity and extensibility through progressive lowering of abstractions, and (ii) the concept of virtual vectors that enable users to write single-threaded code across all layers of the software stack, while pushing the complexity of communication, parallelization, and memory management down to the execution engine. We show that CryptDough generalizes the functionality of state-of-the-art MPC systems and remains competitive on the analytics they support, often outperforming them by more than $2\times$.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Trusted Hardware Acceleration for Function Secret Sharing**
  2026-08-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.16223)
  Pengzhi Huang, Kiwan Maeng, G. Edward Suh

  <details><summary>摘要 / Abstract</summary>

  Function secret sharing (FSS) is a core building block for privacy-preserving systems such as secure inference and private information retrieval (PIR), but incurs significant overhead in key generation, communication, and data movement.We present the distributed function accelerator (DFA), a hardware accelerator that targets the dominant primitive in FSS: distributed point function (DPF) generation and evaluation. DFA combines a high-throughput fixed-function engine for AES-based pseudorandom number generation with a lightweight programmable unit for protocol-specific logic. In untrusted mode, DFA serves as a pure accelerator for DPF evaluation, improving throughput and energy efficiency without changing the protocol. In trusted mode, it further enables local, on-the-fly key generation, eliminating key distribution, and reducing storage and data movement overheads. Across representative workloads, DFA achieves a reduction of 10X end-to-end latency, a reduction of up to 20X communication and more than 5X energy savings for secure inference; and an improvement of 5X throughput and 10X energy reduction for PIR, with modest hardware cost.

  匹配依据：MPC: secret sharing

  </details>

- **Silent Threshold Encryption from Lattices**
  2026-08-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1716)
  Jeffrey Champion, David J. Wu, Shota Yamada

  <details><summary>摘要 / Abstract</summary>

  Silent threshold encryption is a generalization of threshold encryption where the public encryption key associated with a group of users is a deterministic function of their individual public keys. The main efficiency requirement is that the ciphertext size should be sublinear in (and ideally, independent of) the size of the decryption quorum $N$. Existing constructions of silent threshold encryption for arbitrary threshold policies have either relied on bilinear maps or on heavyweight tools such as witness encryption and indistinguishability obfuscation. Recently, several works have shown how to support constant thresholds from the decomposed learning with errors (LWE) problem. In this work, we show how to construct a silent threshold encryption scheme from the decomposed LWE assumption where the ciphertext size for encrypting a single bit is $\tilde{O}(T) + \mathsf{poly}(\lambda, \log N)$. Here, $N$ is the total number of users, $T$ is the threshold, and $\lambda$ is the security parameter. Our scheme achieves non-trivial succinctness for all thresholds $T = N^\varepsilon$ for any constant $\varepsilon &lt; 1$. More generally, our scheme extends beyond threshold policies to any monotone policy family that has a succinct (computational) secret sharing scheme; the ciphertext in this case scales with the maximum number of corrupted shares. The core building block in our work is a new bounded-collusion registered functional encryption (FE) scheme with succinct ciphertexts. Specifically, for $N$ users and a collusion bound $Q$, we obtain a registered FE scheme that supports depth-$d$ Boolean circuits on $\ell$-bit inputs and single-bit output with ciphertext size $Q \cdot \tilde{O}(d) + \ell \cdot \mathsf{poly}(\lambda, d, \log N)$. Security relies on the decomposed LWE assumption in the random oracle model. Previously, bounded-collusion registered FE for general circuits was known only from bilinear maps, evasive LWE, or indistinguishability obfuscation.

  匹配依据：MPC: secret sharing

  </details>

- **Secret Sharing at the Shannon Ceiling**
  2026-08-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.17047)
  Christopher Williamson

  <details><summary>摘要 / Abstract</summary>

  For every $n\geq 9$ that is a multiple of 3, we construct an explicit access structure on $n$ participants. In every perfect secret-sharing scheme realising this access structure, if $S$ denotes the random secret, then the sum of the share entropies is at least $\left(\frac{n^2}{9}+\frac{2n}{3}\right)H(S)$, and some participant has share entropy at least $\left(\frac{n}{6}+\frac12\right)H(S)$. After normalisation by $H(S)$, these are respectively $Ω(n^2)$ and $Ω(n)$ lower bounds and also give the same asymptotic lower bounds on the total and largest expected binary lengths of the shares. This improves by a logarithmic factor the longstanding general lower bounds of $Ω(n^2/\log n)$ for total share size and $Ω(n/\log n)$ for maximum share size due to Csirmaz. The proof uses only elementary Shannon inequalities, together with some averaging arguments. The Shannon-information method has universal $O(n^2)$ and $O(n)$ ceilings for the total and maximum normalised entropy lower bounds it can certify, so our construction reaches both ceilings up to constant factors.

  匹配依据：MPC: secret sharing

  </details>

- **A decrementally-improved algorithm for Boolean MQ**
  2026-08-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1704)
  Charles Bouillaguet, Julia Sauvage

  <details><summary>摘要 / Abstract</summary>

  The MQOM signature scheme is currently a third-round candidate in the NIST competition for additional signatures. It is based on the ``MPC-in-the-Head&#x27;&#x27; paradigm and relies on the hardness of the MQ problem. Some of its parameter sets expose a Boolean quadratic system in the public key. While the situation for MQ over larger fields has been relatively quiescent over the last decade, Boolean MQ has seen active progress, culminating with Dinur&#x27;s algorithms at SODA 2021 and Eurocrypt 2021. We propose yet another algorithm for Boolean MQ. It is a hybrid between the ``polynomial-method&#x27;&#x27; of Lokshtanov, Paturi, Tamaki, Williams and Yu from SODA 2017 and Dinur&#x27;s ``second algorithm&#x27;&#x27; from Eurocrypt 2021. We remove some machinery from the latter to obtain a modest improvement of 1--4 bits in performance for MQOM parameters (``decremental improvement&#x27;&#x27;). MQOM optionally uses the ``correlated GGM trees&#x27;&#x27; technique to shorten signatures; in that case, its security also relies on the hardness of the ``Partial-Guessing One-Wayness&#x27;&#x27; problem for MQ (PGOW-MQ): given an MQ system supposed to offer $\lambda$ bits of security, the adversary has to find the first $\lambda$ bits of a solution, and they have access to an oracle that enables them to check candidate prefixes. The designers of MQOM implicitly assumed that PGOW-MQ is as hard as MQ itself. Our algorithm can exploit the availability of the solution-testing oracle to solve PGOW-MQ 2 to 4 times faster than it solves MQ, thus showing that the two problems are marginally different. This yields attacks against MQOM that are 3--4 bits below the expected security level, but that suffer from huge memory complexities. Lastly, we survey old and new techniques to find an invertible linear change of variables that puts a few arbitrary polynomials in UOV shape. This leads to a small acceleration of our algorithm, and also incidentally improves upon the Thomae-Wolf and Furue-Nakamura-Takagi algorithms to solve underdetermined Boolean systems. A new idea based on matrix pencils was used to solve the largest underdetermined Boolean Fukuoka MQ challenges and may be of independent interest.

  匹配依据：MPC: mpc (context)

  </details>

- **On the Impossibility of Robust Combiners for Cryptographic Groups**
  2026-08-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1695)
  Cong Zhang, Wenli Wang, Taiyu Wang, Hong-Sheng Zhou, Pengfei Chen, Zhihong Jia, Jian Liu, Jinfei Liu, Moti Yung, Kui Ren

  <details><summary>摘要 / Abstract</summary>

  A $(k,n)$-robust combiner for a primitive $\mathcal{P}$ combines $n$ candidate instantiations of $\mathcal{P}$ into a single scheme that remains secure as long as at least $k$ of them remain secure. Robust combiners have been extensively studied for primitives such as hash functions, public-key encryption, and oblivious transfer, but much less is known in the setting of cryptographic groups. In this work, we initiate the study of robust combiners for cryptographic groups in Maurer&#x27;s generic group model (GGM), where algorithms access group elements only through abstract algebraic operations. We ask whether one can combine $n$ candidate groups into a single group that remains secure provided that at least $k$ of the underlying groups remain secure. A natural baseline is the direct-product construction, which preserves search hardness but fails for decisional assumptions and incurs substantial representation overhead. We show that these limitations are in fact inherent. Our first result is a complete impossibility for the decisional Diffie--Hellman assumption: for every polynomially bounded $n$ and $k$ with $k&lt;n$, there is no generic $(k,n)$-robust combiner for cryptographic groups that preserves DDH security. Our second result gives a tight threshold for search assumptions in the regime where $n$ and $k$ are fixed constants. For the discrete logarithm problem, robust generic combination is possible when the combined group order is large enough to encode the secrets of $n-k+1$ components; concretely, if $\log N \ge (n-k+1)\lambda$, where the component groups have distinct $\lambda$-bit prime order, then a robust combiner exists. Conversely, if $\log N \le (n-k)\lambda$, then no generic $(k,n)$-robust DLog-secure combiner exists. These results identify a fundamental limitation of robust hedging at the group level. Decisional assumptions such as DDH cannot be robustly combined in the GGM, while search assumptions admit robustness only at essentially optimal representation cost. Consequently, robustness for group-based cryptography must in general be achieved at higher layers, such as protocol design or key derivation.

  匹配依据：MPC: oblivious transfer

  </details>

- **DumboMix: Robust Asynchronous Anonymous Broadcast Made Practical**
  2026-08-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1699)
  Wei Tang, Hanwen Feng, Jiliang Li, Yuan Lu, Qiang Tang

  <details><summary>摘要 / Abstract</summary>

  We present a practical framework $\mathsf{DumboMix}$ for asynchronous anonymous broadcasts with guaranteed output delivery (G.O.D., a.k.a. robustness), enabling a set of $n$ servers to privately solicit $N$ messages from distinct clients, such that these messages remain secret until they are revealed in uniform random order. Here, asynchronous G.O.D. ensures that all messages are eventually randomly mixed despite (i) arbitrary malicious behaviors by up to $\lfloor (n-1)/3 \rfloor$ Byzantine servers and (ii) unpredictable network delays and jitters. At the core of $\mathsf{DumboMix}$, we first propose a couple of practical mixing methods $\mathsf{DumboMix1}$ and $\mathsf{DumboMix2}$ for Shamir-secret-shared multi-party computation (MPC) over $\mathbb{Z}_p$, along with their server-optimized variants. When randomly mixing $N$ messages, their online phases require only $\mathcal{O}(1)$ multiplicative depth, expected $\mathcal{O}(N^2)$ scalar multiplications (between public and shared values), and up to $\mathcal{O}(N)$ MPC multiplications (between shared values). Moreover, assuming a robust underlying MPC framework, they guarantee that all revealed inputs are uniformly shuffled. In contrast, existing techniques fail to achieve all these performance and functionality features: The DC-net variant $\mathsf{Blinder}$ (CCS’20) may reveal a non-negligible fraction of inputs without shuffling them; Butterfly switching networks in secret-shared MPC (CCS’19) incur $\mathcal{O}(\log^2 N)$ multiplicative depth; RabbitMix (Security’24) requires $\mathcal{O}(N^2)$ MPC multiplications; and PowerMix (CCS’19) incurs $N^{3}/2$ scalar multiplications. We finally implement our new mixing methods within $\mathsf{DumboMPC\text{++}}$, our computation-optimized implementation of the state-of-the-art robust AMPC framework $\mathsf{DumboMPC}$ (Security’25), which provides more concretely efficient offline preprocessing while preserving asynchronous G.O.D. and optimal resilience. We then conduct extensive evaluations with $n=4$ to $31$ servers under varying network settings, revealing that our new mixing methods achieve 44.8--65.9× (resp. 37.1--52.7×), 4.8--7.1× (resp. 3.9--5.5×), and 2.7--4.0× (resp. 5.1--7.2×) speedups over RabbitMix, PowerMix, and the butterfly switching network, respectively, when shuffling 1024 messages in LAN (resp. WAN).

  匹配依据：MPC: multi party computation

  </details>

- **Actively Secure Two-Party Function Secret Sharing with Dynamic Cross-Phase Verification**
  2026-08-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1697)
  Yujie Xue, Lin Liu, Rongmao Chen, Yizhen Jiang, Yuchuan Luo, Bing Sun, Shaojing Fu

  <details><summary>摘要 / Abstract</summary>

  Function secret sharing (FSS) gives two parties succinct keys whose local evaluations add up to a hidden function value. Removing the dealer is the natural next step for preprocessing-based secure computation, but malicious security then requires more than checking a finished key: the generation transcript, the function the key actually computes, and every released evaluation share must all be bound to one execution. We call this the cross-phase binding problem, and we solve it. We present VeriFSS, a dealer-free two-party FSS scheme with active security, proved in the standard simulation-based framework against one static malicious corruption. The construction rests on a two-plane key: the distributed generator produces a key for the paired function $x\mapsto(f_\theta(x),\Lambda f_\theta(x))$, where $\Lambda$ is a secret global authentication scalar. The second plane makes every local evaluation an authenticated sharing for free, which yields online report binding without vector commitments, extractable hashing, or per-point interaction. It also supplies the ingredient the audit was missing: we prove a moment-fidelity lemma showing that a corrupted party cannot misreport the full-domain moments of its own sealed key except with probability $3/|E|$ over the challenge set $E$, and a shape-identification lemma showing that three moment equations pin a point function down exactly, with error $2n/|E|$ over any field. The proof isolates the coefficient of the square monomial in the support polynomial and is therefore characteristic-free; in characteristic two an odd-size equal-weight support defeats the support equation on its own, and we show the position equation takes over. A discrete-derivative reduction carries both lemmas to comparison functions, and a Galois-ring variant covers fixed-point payloads over $\mathbb{Z}_{2^k}$ by a $2$-adic valuation argument, so no non-additive lift into a binary field is ever needed. Generation costs two rounds and five field elements per party per level; certification adds $O(n)$ elements with no dependence on the domain size, and a dynamic cross-domain aggregation certifies arbitrarily many heterogeneous instances under one challenge and a constant number of rounds. We then lift the general-purpose FSS gates of Boyle et al. (EUROCRYPT 2021): every gate that is a public affine post-processing of a constant number of DPF/DCF evaluations---interval containment, splines, ReLU, arithmetic shift, bit decomposition, zero test, table lookup---inherits active security at no additional online cost. We evaluate our construction using a C++ implementation that certifies keys over $\mathbb{F}_{p^2}$ ($p=2^{61}-1$) and $\mathrm{GF}(2^{128})$, realises the gate layer, and agrees bit‑for‑bit on every exported test vector. A certified DPF key at $n=16$ takes $5.7$ ms to generate and $3.3$ ms to certify. Certified DPF keys are $5.4\%$ larger than the semi-honest dealer-free baseline at $n=16$, and aggregated certification traffic converges to $1{,}282$ bytes per instance while the round count stays constant. Replaying the certified execution between two processes over TCP shows what that constancy is worth: at a $50$ ms round trip a session takes $1.15$ s, and the figure is unchanged whether one key or sixty-four are certified together, so wide-area certification of a whole preprocessing session is latency-bound by a single key. A campaign of $1{,}400$ injected generation deviations plus shape, moment and release forgeries is rejected without exception in six of seven deviation classes; the seventh is rejected in exactly the $105$ of $200$ trials in which the attacked index bit is one, which is a quantitatively exact confirmation of the single-bit selective-failure predicate that we model explicitly in the ideal functionality, matching the leakage profile of the best known actively secure distributed DPF.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **SparseMPC: Secure Sparse Operations using Multi-Party Computation**
  2026-08-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1675)
  Marc Damie

  <details><summary>摘要 / Abstract</summary>

  Multi-party computation (MPC) enables multiple parties to jointly process sensitive data without revealing their inputs. However, existing MPC protocols remain inefficient for high-dimensional sparse data. In plaintext, sparse linear algebra algorithms address this problem using two fundamental primitives, Scatter and Gather. We propose SparseMPC, an outsourced MPC protocol that securely implements Scatter and Gather and uses them to perform sparse matrix multiplication. Our protocol supports an arbitrary number of data owners and provides a low memory footprint, constant round complexity, and low communication cost. Beyond sparse matrix multiplication, SparseMPC provides a foundation for efficiently realizing a broader class of sparse computations in outsourced MPC.

  匹配依据：MPC: multi party computation

  </details>

- **Simple and Efficient SKL-IBE with Classical Revocation from LWE**
  2026-08-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1676)
  Ho Nguyen Pham, Duong Hieu Phan, Quoc-Huy Vu, Weiqiang Wen

  <details><summary>摘要 / Abstract</summary>

  Secure key leasing (SKL) is a quantum cryptographic primitive that enables the leasing of decryption keys to delegated users with the guarantee that, once revoked, the lessees irreversibly lose decryption capability. A key feature that makes SKL practically relevant is classical revocation: the ability to revoke keys at any time and from anywhere, without relying on a quantum channel. In this work, we revisit SKL schemes for public-key encryption (PKE) and identity-based encryption (IBE), and present a new approach for concrete efficiency under the standard Learning With Errors (LWE) assumption. First, we refine the security analysis of the Dual-Regev SKL-PKE scheme with classical revocation from [Ananth, Poremba, and Vaikuntanathan, TCC 2023; Ananth, Hu, and Huang, TCC 2024], establishing security under the polynomial hardness of LWE with polynomial modulus. Together with the resource efficiency of the Dual-Regev-based construction, our analysis shows that this approach yields the most quantum-efficient known SKL-PKE scheme. Second, we present a simple and efficient construction of selectively secure SKL-IBE with classical revocation from standard LWE. Our approach directly extends the Dual-Regev SKL-PKE within the IBE framework of [Agrawal, Boneh, and Boyen, Eurocrypt 2010], avoiding garbled circuits and obfuscation-based assumptions and achieving improved concrete efficiency over prior generic approaches.

  匹配依据：MPC: garbled circuits

  </details>

- **Non-Interactive Translation of Winternitz Signatures to Lamport Signatures via Secret Sharing**
  2026-08-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1684)
  Mikhail Sergeevitch, Konrad Staniec, David Tse, Nikhil Vanjani, Robin Linus Woll

  <details><summary>摘要 / Abstract</summary>

  BitVM2 brought arbitrary program execution to Bitcoin, yielding the first light-client-based bridge to its second layers and reducing the trust required at setup to a single honest participant. Its successors, BitVM3 and BABE, move the disputed computation off-chain into Garbled Circuits (GCs), cutting worst-case on-chain dispute costs by roughly three orders of magnitude and so opening participation beyond well-capitalized operators; BABE in turn cuts the off-chain storage and setup costs of BitVM3&#x27;s garbled circuits by a comparable factor. What still reaches the chain, however, is bulkier than it need be. BitVM2 commits its data with compact Winternitz one-time signatures (WOTS), whereas BitVM3 and BABE must reveal GC input labels on-chain and so fall back on far bulkier Lamport signatures, which play two roles at once: GC input labels and Bitcoin-verifiable commitments. WOTS cannot simply be substituted, because its hash chains are monotonic---an evaluator holding one state&#x27;s preimage can hash forward and obtain several active labels on a single input wire, destroying the circuit&#x27;s privacy. Recovering BitVM2&#x27;s compactness therefore calls for a practical GC whose input labels are WOTS signatures---a construction that has remained out of reach. We close this gap with a non-interactive \emph{WOTS-to-Lamport translation gadget}: the garbler commits on-chain using compact WOTS chains, and the evaluator expands them off-chain into exactly the orthogonal Lamport labels the GC consumes, learning nothing about the mutually exclusive ones. A naive translation table that enumerated messages would be exponentially large. Two symmetries bring it down to quadratic: reconstruction from a Shamir sharing depends only on \emph{how many} shares are held and not on \emph{which}, which collapses the exponentially many messages onto the single checksum weight WOTS already computes; and monotonicity, the very property that made WOTS unusable, orders an evaluator&#x27;s access by inclusion. We model the gadget as a garbling scheme and prove it adaptively private. Applied to BABE, it restores WOTS-scale commitments to a GC-based protocol, cutting total on-chain script size by more than $3\times$ and bringing dispute transactions within Bitcoin&#x27;s standardness limit.

  匹配依据：MPC: garbled circuits, garbling scheme, secret sharing

  </details>

- **Linearly Homomorphic Secret Sharing and Multi-Party Computation with Unanimously Verifiable Deletion**
  2026-08-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1673)
  Yilei Chen, Liheng Ji, Han Luo

  <details><summary>摘要 / Abstract</summary>

  Certified deletion enables a party to prove that it has erased the sensitive information contained in a quantum state. Bartusek and Raizes (CRYPTO 2024) gave the first secret-sharing scheme with privately verifiable deletion. Subsequently, Katz and Sela (EUROCRYPT 2025) constructed secret-sharing schemes with publicly verifiable deletion under computational assumptions. Constructing such a publicly verifiable scheme without cryptographic assumptions remains open. In this work, we introduce an intermediate notion called unanimously verifiable deletion. While private verification relies on the dealer and public verification allows any third party to verify deletion, unanimous verification assigns the verification responsibility to the parties in the secret-sharing scheme themselves. We construct an information-theoretically secure linearly homomorphic threshold secret-sharing batch scheme with adaptive unanimously verifiable deletion. In particular, to obtain its linear-homomorphic property, we exploit a linearly homomorphic structure of BB84-type states that enables linear transformations on encoded values while preserving certified deletion. More generally, this structure can be used to upgrade certain primitives with certified deletion to their linearly homomorphic counterparts. As another major contribution, we demonstrate an application of this batch scheme by constructing outsourced multi-party computation (MPC) protocols for arbitrary arithmetic circuits. Our outsourced MPC has semi-honest classical clients and malicious quantum servers, achieves adaptive unanimously verifiable deletion security in the trusted-preprocessing and security-with-abort setting against a rushing adversary, and supports public output reconstruction. The adversary may adaptively corrupt up to $n-1$ clients. For the servers, during the online execution, at most $t$ corrupted servers may remain undeleted and at least $t+1$ honest servers must remain undeleted, for any $t&lt;n/2$. After successful finalization, all servers may be corrupted without revealing additional information about the remaining clients&#x27; inputs beyond the public output and the corrupted clients&#x27; inputs.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Fully-Succinct Multi-Key FHE &amp; Rate-1 Simulatable Threshold Decryption from LWE**
  2026-08-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1683)
  Abtin Afshar, Rishab Goyal

  <details><summary>摘要 / Abstract</summary>

  We construct the first multi-key fully homomorphic encryption (MKFHE) scheme where the ciphertext size, public key size, and secret key size remain independent of the number of users, $N$. Our construction is leveled and relies on the standard Learning with Errors (LWE) assumption. All prior MKFHE schemes incur at least linear growth in ciphertext size with the number of users ($|\mathsf{ct}| \propto N$), a limitation that has persisted across more than a decade of research. Our results provide the first evidence that MKFHE with constant ciphertext size is achievable under standard assumptions and paves the way for many interesting applications. We also describe a single-round distributed decryption protocol for multi-key ciphertexts in our fully-succinct MKFHE scheme. More remarkably, we show that our MKFHE scheme simultaneously satisfies the following properties: (1) the size of each user&#x27;s partial decryption share is identically equal to the plaintext length (i.e., partial decryption shares are truly rate-1), and (2) an honest user&#x27;s partial decryption can be simulated. To the best of our knowledge prior to this work, we did not have any MKFHE with one-round distributed decryption from standard assumptions that simultaneously satisfied both these properties. We show that our MKFHE is significantly useful in designing various forms of multi-party computation (MPC) protocols with asymptotically optimal communication complexity.

  匹配依据：MPC: multi party computation

  </details>

- **Towards Scalable Fuzzy PSI via Efficient Fuzzy Matching**
  2026-08-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.11526)
  Meng Hao, Xinpeng Yang, Hanxiao Chen, Tianwei Zhang, Haiyang Xue, Guomin Yang, Hongwei Li, Robert H. Deng

  <details><summary>摘要 / Abstract</summary>

  In this paper, we present scalable fuzzy PSI protocols for general $L_{p \in [1, \infty]}$ distance, supporting both low- and high-dimensional sets. The core technique is two efficient fuzzy matching protocols. The first is built from a role-reversed oblivious PRF (OPRF) and realizes $O(d\log δ)$ overhead, compared to $O((\log δ)^d)$ in previous works. The second leverages customized oblivious transfer (OT) with $O(d\ell)$ overhead, where $\ell$ is the bit length of inputs, which is particularly suitable for short inputs. With these new techniques, we further propose a new dual-layer hashing framework for fuzzy PSI over low-dimensional sets, instantiated with our OT-based fuzzy matching and enhanced with a domain reduction optimization. The protocols achieve an overhead linear with $n, m, \log δ, 2^d$, without the $O((\log δ)^d)$ or $O(δ)$ factors present in prior works. {For high-dimensional sets, we construct fuzzy PSI protocols based on our OPRF- and OT-based fuzzy matching, which achieve an asymptotic overhead linear with $n, m, d$, and $\log δ$ but rely on the strong globally disjoint assumption.} Extensive evaluations demonstrate that our protocols achieve up to a $145\times$ speedup in running time and a $20\times$ reduction in communication cost compared to van Baarsen and Pu~(ASIACRYPT&#x27;25), and achieve up to a $25\times$ speedup in running time and up to a $17\times$ reduction in communication cost compared to Piske et al.~(CCS&#x27;25).

  匹配依据：MPC: oblivious transfer

  </details>

- **Resolving the Worst-Case Complexity of Linear Secret Sharing**
  2026-08-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1667)
  Oded Nir

  <details><summary>摘要 / Abstract</summary>

  A secret-sharing scheme allows a dealer to distribute a secret among $n$ parties such that only predefined “authorized” sets of parties can reconstruct the secret, and all other “unauthorized” sets learn nothing about it. Families of authorized sets are called access structures, and a scheme is called linear if its sharing map is linear in the secret and the dealer’s randomness. We show that every $n$-party access structure can be realized by a linear secret-sharing scheme over every finite field with at most $2^{\lceil n/2\rceil-1}+1$ field elements per share. Taking the field to be $\mathbb{F}_2$ yields the same bound in bits for one-bit secrets. A known counting lower bound for monotone span programs shows that for every fixed finite field, almost all access structures require share size $2^{n/2-o(n)}$ in every linear scheme, which makes our upper bound tight. Our scheme is considerably simpler than previous schemes that obtained share size $2^{cn+o(n)}$ with $1/2\leq c&lt;1$. We also present a variant of this linear construction that is tailored for monotone k-DNF access structures (also known as $k$-upslices). Then, by combining it with existing non-linear schemes, we derive a scheme for all access structures with share size $2^{0.494n+o(n)}$. This improves the previous upper bound of $2^{0.585n+o(n)}$ by Applebaum and Nir (CRYPTO 2021), and establishes a separation between the worst-case non-linear and linear exponents. Additionally, we prove that almost all monotone functions require monotone span programs of size $2^{n/2-o(n)}$ simultaneously over all fields, finite or infinite, improving the previous bound of $2^{n/3-o(n)}$ for this setting. In particular, almost all access structures require information ratio $2^{n/2-o(n)}$ in linear schemes over every finite field, including fields whose size depend on $n$. Some of the constructions and proofs were discovered in conversations prompted by the author with GPT-5.6 Sol and Claude Fable 5.

  匹配依据：MPC: secret sharing

  </details>

- **Renaming or Tightness: Enforcing Disjunctive Information Flow Policies**
  2026-08-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.09120)
  Xin Xu, Siru Tao, Kaizhen Tan

  <details><summary>摘要 / Abstract</summary>

  A disjunctive policy allows a value to depend on at most one of two secrets and never on both: an analyst may consult one client&#x27;s file or the other&#x27;s, a share of a split secret may be released but not its sibling. Such policies are not lattice-shaped, and Hunt and Sands introduced the quantale of information to give them a semantics, leaving the enforcement layer open. We build the flow-sensitive type system family that the quantale calls for, and show that the object which makes such families useful, the universal type object from which every member specialises, splits in two, with a consequence for enforcement. Over the free commutative quantale on the program variables the whole mechanism survives for every policy: monotone renaming, canonical derivations, principal typings, internal completeness. Over the free object with idempotent generators the certified bound is strictly more precise and still sound, because it records that two reads of one source honour one disjunct. The gap cannot be closed from inside the independent-attribute family: no mechanism of that shape whose labelling maps support monotone renaming certifies a bound more precise than the first, and for principal typings under generator-exact homomorphic specialisation the two coincide. Under the ethical-wall and secret-sharing labels the second read of a disjunctive source therefore drives every such certificate to no guarantee, and programs that satisfy the policy are rejected. The literal transcription of the lattice-era object is no escape either: it is a further quotient that loses branch disjunction. Precision is recovered by deferring specialisation to the judgement level, and the resulting read-out map is the least sound join-preserving one.

  匹配依据：MPC: secret sharing

  </details>

- **Information-Theoretic SFE and PFE with Reduced Communication**
  2026-08-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1647)
  Shuaishuai Li, Cong Zhang, Juntong Lin, Anyu Wang, Xiaoyun Wang

  <details><summary>摘要 / Abstract</summary>

  Secure function evaluation (SFE) and private function evaluation (PFE) are fundamental primitives in multiparty computation. In SFE, multiple parties jointly compute a \textit{public} function over private inputs while revealing nothing beyond the output, whereas in PFE the function itself is \textit{private} and known only to a designated party. In this work, we focus on the semi-honest setting and present more efficient information-theoretic constructions for both SFE and PFE. For SFE, the classical BGW protocol incurs $O(n^2)$ communication per multiplication gate. The DN protocol (Damg\aa rd and Nielsen, Crypto 2007) reduces the amortized communication to linear but still require an additional $O(n^2)$ term, yielding $O(m^* n + n^2)$ communication for $m^*$ multiplication gates. This becomes suboptimal in the regime $m^*= o(n)$. We introduce a simple technique that removes this quadratic overhead, achieving strictly linear $O(m^* n)$ communication. For PFE, the only existing information-theoretic approach relies on universal circuits, which results in $O(m^5n+n^2)$ complexity for arithmetic circuits. We develop new techniques that avoid universal circuits entirely. Combined with our SFE improvements, this yields an honest-majority PFE protocol achieving $O(m^2n)$ communication for circuit size $m$. We further obtain improved efficiency in special cases, including a three-party protocol with $O(m^{4/3})$ communication, and an $n$-party protocol tolerating one corruption with $O(m^{(2n-2)/(2n-3)}n)$ communication.

  匹配依据：MPC: multiparty computation, secure function evaluation

  </details>

- **General versus linear secret sharing under statistical security**
  2026-08-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1646)
  Shahram Khazaei

  <details><summary>摘要 / Abstract</summary>

  How few participants are needed before general secret-sharing schemes can outperform linear ones under a fixed security notion? Under statistical security, we show that the answer is five participants; under perfect security, the corresponding threshold remains unknown. It is known that the \(157\) connected access structures on five participants split into \(140\) Shannon-exact cases and seventeen exceptional cases. For the former, linear schemes attain the Shannon polymatroid region; for each of the latter, the exact linear contribution region is the all-pairs one-common-information region and is strictly smaller than the Shannon region. We investigate the statistical contribution regions of these seventeen exceptional structures. For fifteen of them, we construct a partial scheme whose contribution vector lies outside the exact linear region; Jafari--Khazaei&#x27;s partial-to-statistical transfer then gives a statistically secure family with the same asymptotic vector. One dual pair remains open. For \(\Gamma_{30}\), we further show that the maximum information ratio under statistical security lies in \([14/9,1.6502)\), improving both previously established bounds; moreover, \(1.6502&lt;5/3\), where \(5/3\) is the optimum for linear schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Recursive Common Information for Group-Characterizable Random Variables**
  2026-08-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1644)
  Shahram Khazaei

  <details><summary>摘要 / Abstract</summary>

  Common information (CI) is useful in entropy-based lower bounds for secret sharing. We study CI for group-characterizable (GC) random variables. Building on the sufficient condition of Kaboli--Khazaei--Parviz, we prove an exact pair criterion: two coset random variables $X_H$ and $X_K$ have common information if and only if the subgroups $H$ and $K$ permute, that is, $HK=KH$. Consequently, a GC tuple is $1$-CI exactly when every pair of subgroups in the meet closure of its labels permutes, whereas it is recursively CI exactly when every pair in the generated subgroup sublattice permutes. This also gives a finite algorithm for deciding recursive CI, and we exhibit a GC tuple over $S_3\times S_3$ that is $1$-CI but not $2$-CI. Since normal subgroups satisfy the recursive criterion, homomorphic random variables are recursively CI. For the twelve-participant disjoint Fano--non-Fano access structure, the Shannon lower-bound method with all separate $1$-CI extensions still gives maximum and average optima equal to one. Two depth-two recursive CI extensions instead give the lower bounds $43/41$ and $54089/51756\approx1.04508$ for the maximum and average information ratios of perfect homomorphic schemes. The same bounds hold for Abelian schemes; the exact mixed-linear and linear values are already known.

  匹配依据：MPC: secret sharing

  </details>

- **From Noise to Meaning: Meaningful Secret Sharing with Tamper Detection for Facial Recognition**
  2026-08-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.08924)
  Ajnas Muhammed, Iurii Medvedev, Nuno Gonçalves

  <details><summary>摘要 / Abstract</summary>

  Popularity of AI-based face recognition system directly demands protection of sensitive biometric data used for training. Visual secret sharing is an interesting idea, as it splits facial images into secret shares that look random and spread across many institutions. However, these shares look like noise and can easily spark suspicion and recognized as encrypted content. This makes them open to targeted collection and harvest-now-decrypt-later attacks. Additionally, visual secret sharing does not detect tampering, allowing attackers to modify shares and threaten the integrity of reconstruction. In this paper, we introduce a new method that turns distracting noise-like secret shares into visually appealing cover images with additional cryptographic tamper detection. The proposed technique works with visual secret sharing and introduces cover images to embed the shares using adaptive least significant bit steganography. Here, cover images with perceptual transparency are used to store secret shares while guaranteeing complete privacy. A two layer authentication using strong digital watermarking and cryptographic hashing is used to protect the integrity of shares. The proposed technique shows high resilience in stopping bit-flipping, cropping, and substitution attacks. Extensive experiments on multiple public face datasets show that the technique shows better FR accuracy, while eliminating share conspicuousness and guaranteeing integrity. The proposed framework sets a new standard for protecting facial data in such a way that privacy, security, and integrity are protected.

  匹配依据：MPC: secret sharing

  </details>

- **How to use Polynomially-Hard iO: Turing Machine Obfuscation and More**
  2026-08-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1636)
  Jesko Dujmovic, Yao-Ching Hsieh, Abhishek Jain, Willy Quach

  <details><summary>摘要 / Abstract</summary>

  We revisit the notion of PViO [Jain-Jin, FOCS’22] – an indistinguishability obfuscation (iO) scheme for Turing machines with unbounded input length that guarantees security for pairs of machines whose equivalence can be proven in Cook’s Theory PV. Known constructions of PViO require subexponentially-hard iO for circuits. We give the first construction based on polynomially-hard iO and other standard assumptions. We further show how to replace iO with EFiO – an efficiently falsifiable variant, thus obtaining a construction based on efficiently falsifiable assumptions. Central to our result is a new twist to the celebrated punctured programming technique [Sahai-Waters, STOC’14], where one can program an obfuscated probabilistic function on its entire input domain in one shot instead of an input-by-input manner. Our key ingredient is the notion of function secret sharing [Boyle-Gilboa-Ishai, EUROCRYPT’15]. We further show the versatility of our technique by removing the use of complexity-leveraging in two applications of iO: unleveled fully homomorphic encryption, and adaptively-sound succinct non-interactive arguments for “trapdoor” languages.

  匹配依据：MPC: secret sharing

  </details>
