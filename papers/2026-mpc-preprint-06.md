# 2026 · MPC · 仅预印本来源 · 第 6/6 页

[总目录](../PAPERS.md) · [上一页](2026-mpc-preprint-05.md)

- **Implementation of Oblivious Transfer over Binary-Input AWGN Channels by Polar Codes**
  2026-01-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.10682)
  Pin-Hsun Lin, Hadi Aghaee, Christian Deppe, Eduard A. Jorswieck, Holger Boche

  <details><summary>摘要 / Abstract</summary>

  We develop a one-out-of-two oblivious transfer protocol over the binary-input additive white Gaussian noise (BI-AWGN) channel using polar codes. The scheme uses two decoder views linked by automorphisms of the polar transform and publicly draws the encoder at random from the corresponding automorphism group. This yields perfect secrecy for Bob at any blocklength. Secrecy for Alice is obtained asymptotically via channel polarization combined with privacy amplification. Because the construction deliberately injects randomness into selected bad bit-channels, we derive a relaxed reliability criterion, which is empirically certified via Monte-Carlo simulations. We also evaluate finite-blocklength performance. Finally, we characterize the polar-transform automorphisms as bit-level permutations of bit-channel indices, and exploit this structure to derive and optimize an achievable finite-blocklength rate.

  匹配依据：MPC: oblivious transfer

  </details>

- **$L$ for the Price of One: On the Benefits of Using more than $t+1$ Parties in Threshold Signing**
  2026-01-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/061)
  Daniel Escudero, Yashvanth Kondi, Yifan Song, Hernán Vanegas

  <details><summary>摘要 / Abstract</summary>

  In threshold ECDSA a committee of $N$ parties holds---say, Shamir---shares of degree $t$ of a secret key, where typically $N\gg t$ for operational purposes (e.g. redundancy to prevent losing the key). At signing time, $t+1$ parties can execute a protocol to produce a signature on a given message without leaking anything about the secret key. In this work we show that if we use $n=t+2(\ell-1) + 1$ parties for signing instead, we can compute $\ell$ signatures without increasing at all the communication costs per party, essentially getting $\ell\times$ more signatures almost for free in a dishonest majority. Our result is achieved by making use of packed secret-sharing to distribute multiple secrets with no communication penalty. This introduces several challenges not present in the non-packed domain, which leads us to introduce two primitives that may be of independent interest: we show how to prove that a sharing contains small elements efficiently, and its use in distributing consistent sharings of the same secret modulo two different integers. We also show how to generate degree-$2$ preprocessing material with constant communication via an adaptation of the virtual parties idea by Bracha from 1987. We compare the communication of our protocol to sign $\ell$ messages with respect to the state-of-the-art in $t+1$-party ECDSA signing by (Doerner et al, S&amp;P&#x27;24), which needs to be repeated $\ell$ times. Our results show that, for appropriate regimes of $(t,n,\ell)$, our protocol can achieve 5x less communication (and even a larger factor) than theirs while adding only a few extra parties for the computation.

  匹配依据：MPC: secret sharing

  </details>

- **SoK: Enhancing Cryptographic Collaborative Learning with Differential Privacy**
  2026-01-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.09460)
  Francesco Capano, Jonas Böhler, Benjamin Weggenmann

  <details><summary>摘要 / Abstract</summary>

  In collaborative learning (CL), multiple parties jointly train a machine learning model on their private datasets. However, data can not be shared directly due to privacy concerns. To ensure input confidentiality, cryptographic techniques, e.g., multi-party computation (MPC), enable training on encrypted data. Yet, even securely trained models are vulnerable to inference attacks aiming to extract memorized data from model outputs. To ensure output privacy and mitigate inference attacks, differential privacy (DP) injects calibrated noise during training. While cryptography and DP offer complementary guarantees, combining them efficiently for cryptographic and differentially private CL (CPCL) is challenging. Cryptography incurs performance overheads, while DP degrades accuracy, creating a privacy-accuracy-performance trade-off that needs careful design considerations. This work systematizes the CPCL landscape. We introduce a unified framework that generalizes common phases across CPCL paradigms, and identify secure noise sampling as the foundational phase to achieve CPCL. We analyze trade-offs of different secure noise sampling techniques, noise types, and DP mechanisms discussing their implementation challenges and evaluating their accuracy and cryptographic overhead across CPCL paradigms. Additionally, we implement identified secure noise sampling options in MPC and evaluate their computation and communication costs in WAN and LAN. Finally, we propose future research directions based on identified key observations, gaps and possible enhancements in the literature.

  匹配依据：MPC: multi party computation

  </details>

- **Secret sharing with additive access structures from correlated random variables**
  2026-01-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.09640)
  David Miller, Rémi A. Chou

  <details><summary>摘要 / Abstract</summary>

  We generalize secret-sharing models that rely on correlated randomness and public communication, originally designed for a fixed access structure, to support a sequence of dynamic access structures, which we term an Additive Access Structure. Specifically, the access structure is allowed to monotonically grow by having any subset of participants added to it at a given time step, and the dealer only learns of these changes to the access structure on the time step that they occur. For this model, we prove the existence of a secret sharing strategy that achieves the same secret rate at each time step as the best known strategy for the fixed access structure version of this model. We also prove that there exists a strategy that is capacity-achieving at any time step where the access structure is a threshold access structure.

  匹配依据：MPC: secret sharing

  </details>

- **Learning-Augmented Perfectly Secure Collaborative Matrix Multiplication**
  2026-01-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.09916)
  Zixuan He, Mohammad Reza Deylam Salehi, Derya Malak, Photios A. Stavrou

  <details><summary>摘要 / Abstract</summary>

  This paper presents a perfectly secure matrix multiplication (PSMM) protocol for multiparty computation (MPC) of $\mathrm{A}^{\top}\mathrm{B}$ over finite fields. The proposed scheme guarantees correctness and information-theoretic privacy against threshold-bounded, semi-honest colluding agents, under explicit local storage constraints. Our scheme encodes submatrices as evaluations of sparse masking polynomials and combines coefficient alignment with Beaver-style randomness to ensure perfect secrecy. We demonstrate that any colluding set of parties below the security threshold observes uniformly random shares, and that the recovery threshold is optimal, matching existing information-theoretic limits. Building on this framework, we introduce a learning-augmented extension that integrates tensor-decomposition-based local block multiplication, capturing both classical and learned low-rank methods. We demonstrate that the proposed learning-based PSMM preserves privacy and recovery guarantees for MPC, while providing scalable computational efficiency gains (up to $80\%$) as the matrix dimensions grow.

  匹配依据：MPC: multiparty computation

  </details>

- **Kilobyte-Bandwidth Subliminal Channels in FIPS 204 ML-DSA via Packed-Commitment Embedding**
  2026-01-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/053)
  Mounir IDRASSI

  <details><summary>摘要 / Abstract</summary>

  Galteland and Gjøsteen observe that Dilithium-family signatures admit broadband subliminal channels in a secret-key-assisted setting where the receiver can reconstruct the signer’s hidden commitment from a public signature. This note gives a standards-specific instantiation for FIPS 204 ML-DSA. We do not claim a new subliminal-channel technique: our goal is to make the FIPS 204 patch point and byte-level embedding interface explicit and to list the resulting capacities for the approved parameter sets. Two FIPS 204 facts drive the construction: for any accepted signature, the commitment vector \(y\) is recoverable from \((c, z)\) given \(s_1\), and the standardized \(\gamma_1\) values make the packing/unpacking mapping a bijection on its fixed-length byte input. We embed an \(L\)-byte payload by XOR-masking a pseudorandom packed container and decoding it with the standard unpacking routine: the resulting signatures verify under unmodified verifiers. We implemented the patch in the mldsa-native C library and validated round-trip extraction, abort-rate statistics, and distribution sanity checks for all three parameter sets. Changes, scripts, and artifacts are available in the mldsa-native-sublime fork on GitHub. The per-signature covert capacity is \(32\ell w - 32\) bytes, where \(w = \log_2(2\gamma_1)\), namely 2,272 bytes for ML-DSA-44, 3,168 bytes for ML-DSA-65, and 4,448 bytes for ML-DSA-87. As in prior work, extraction requires \(s_1\), so the relevant setting is kleptographic/ASA-style secret sharing rather than public tagging.

  匹配依据：MPC: secret sharing

  </details>

- **Argo MAC: Garbling with Elliptic Curve MACs**
  2026-01-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/049)
  Liam Eagen, Ying Tong Lai

  <details><summary>摘要 / Abstract</summary>

  Off-chain cryptography enables more expressive smart contracts for Bitcoin. Recent work, including BitVM, use SNARKs to prove arbitrary computation, and garbled circuits to verifiably move proof verification off-chain. We define a new garbling primitive, Argo MAC, that enables over $1000\times$ more efficient garbled SNARK verifiers. Argo MAC efficiently translates from an encoding of the bit decomposition of a curve point to a homomorphic MAC of that point. These homomorphic MACs enable much more efficient garbling. In subsequent work, we will describe how to use Argo MAC to construct garbled SNARK verifiers for pairing-based SNARKs.

  匹配依据：MPC: garbled circuits

  </details>

- **LINEture: novel signature cryptosystem**
  2026-01-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.07071)
  Gennady Khalimov, Yevgen Kotukh

  <details><summary>摘要 / Abstract</summary>

  We propose a novel digital signature cryptosystem that exploits the concept of the brute-force problem. To ensure the security of the cryptosystem, we employed several mechanisms: sharing a common secret for factorable permutations, associating permutations with the message being signed, and confirming knowledge of the shared secret using a zero-knowledge proof. We developed a secret-sharing theory based on homomorphic matrix transformations for factorized permutations. The inverse matrix transformation for computing the shared secret is determined by secret parameters, which results in incompletely defined functionality and gives rise to a brute-force cryptanalysis problem. Randomization of session keys using a message hash and random parameters guarantees the uniqueness of each signature, even for identical messages. We employed a zero-knowledge authentication protocol to confirm knowledge of the shared secret, thereby protecting the verifier against unauthorized signature imposition. The LINEture cryptosystem is built on linear matrix algebra and does not rely on a computationally hard problem. High security is achieved through the appropriate selection of matrix transformation dimensions. Matrix computations potentially offer low operational costs for signature generation and verification.

  匹配依据：MPC: secret sharing

  </details>

- **High-capacity dual degrees of freedom quantum secret sharing protocol beyond the linear rate-distance bound**
  2026-01-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.06919)
  Meng-Dong Zhu, Cheng Zhang, Shi-Pu Gu, Xing-Fu Wang, Ming-Ming Du, Wei Zhong, Lan Zhou, Yu-Bo Sheng

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) is the multipartite cryptographic primitive. Most of existing QSS protocols are limited by the linear rate-distance bound, and cannot realize the long-distance and high-capacity multipartite key distribution. This paper proposes a polarization (Pol) and phase (Ph) dual degrees of freedom (dual-DOF) QSS protocol based on the weak coherent pulse (WCP) sources. Our protocol combines the single-photon interference, two-photon interference and non-interference principles, and can resist the internal attack from the dishonest player. We develop simulation method to estimate its performance under the beam splitting attack. The simulation results show that our protocol can surpass the linear bound. Comparing with the differential-phase-shift twin-field QSS and WCP-Ph-QSS protocols, our protocol has stronger resistance against the beam splitting attack, and thus has longer maximal communication distance and higher key rate. By using the WCPs with high average photon number ($μ$ = 1.5), our protocol achieves a key rate about 5.4 times of that in WCP-Ph-QSS protocol. Its maximal communication distance (441.7 km) is about 7.9% longer than that of the WCP-Ph-QSS. Our protocol is highly feasible with current experimental technology and offers a promising approach for long-distance and high-capacity quantum networks.

  匹配依据：MPC: secret sharing

  </details>

- **Scalable Honest-majority MPC for Machine Learning from Mixed Secret Sharings**
  2026-01-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/038)
  Meilin Li, Meng Hao, Yu Chen

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) provides a promising approach for privacy-preserving machine learning (ML). Existing solutions generally fall into two categories but face scalability and efficiency limitations. Protocols based on Shamir secret sharing (SS) incur high communication costs, while those relying on packed Shamir secret sharing (PS) remain largely theoretical and often require costly secret routing, especially for complex ML tasks. In this work, we propose a mixed secret sharing strategy that leverages PS sharing for non-linear layers with repeated and independent operations, and SS sharing for linear layers such as matrix multiplications. To efficiently support alternating linear and non-linear computations, we design generic conversions between SS and PS sharings and further integrate them into the corresponding ML protocols, thereby eliminating additional communication and computation overhead. Moreover, we develop efficient PS sharing-based protocols for primitive non-linear building blocks, which enable multiple non-linear operations to be executed with essentially the same communication cost as a single operation. We implement our framework for secure multi-party ML inference and conduct extensive experiments. Compared to the SOTA work LXY24 (USENIX Security &#x27;24), our approach reduces communication by $3.6$-$6.1 \times$, while achieving $1.5$-$4.3 \times$ runtime improvement in the WAN setting and comparable or up to $2.3 \times$ better performance in the LAN setting.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **On Threshold Fully Homomorphic Encryption with Synchronized Decryptors**
  2026-01-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/031)
  François Colin de Verdière, Alain Passelègue, Damien Stehlé

  <details><summary>摘要 / Abstract</summary>

  We study t-out-of-n threshold fully homomorphic encryption (ThFHE) in the synchronous setting, i.e., when the set of t decryptors is known at the outset of the decryption protocol. It has been observed in various works that the synchronous setting assumption enables to efficiently circumvent one of the major difficulties of ThFHE, namely hiding noise terms whose gigantic magnitude is incurred by the reconstruction coefficients of Shamir secret sharing. Yet, prior to this work, ThFHE in the synchronous setting had not even been properly defined. As a first contribution, we provide a clear syntax for ThFHE in the synchronous setting, as well as two security models: a weak model in which designating the set of decryptors is only viewed as an enabler of efficient decryption and it is fine for non-designated parties to be able to decrypt as long as there are sufficiently many of them; and a much stronger model where a set of decryptors which does not exactly match the designated set should not learn anything. Then, we show that the main existing schemes (Mouchet et al., Journal of Cryptology, 2023; Mouchet et al., ACM CCS, 2024) are insecure, even in the weak model, by describing efficient key-recovery attacks. Finally, we propose a simple and efficient construction which achieves security in the strong security model, by masking the partial decryption shares with pseudorandom functions.

  匹配依据：MPC: secret sharing

  </details>

- **JAGUAR: Efficient and Secure Unbalanced PSI under Malicious Adversaries in the Client-Server Setting**
  2026-01-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/025)
  Weizhan Jing, Xiaojun Chen, Xudong Chen, Ye Dong, Qiang Liu, Tingyu Fan

  <details><summary>摘要 / Abstract</summary>

  In many unbalanced private set intersection (uPSI) applications of the client-server setting, the server needs to perform uPSI with multiple clients. Cong \textit{et al.} (ACM CCS&#x27;21) proposed a state-of-the-art (SOTA) uPSI protocol based on fully homomorphic encryption (FHE), achieving malicious security by employing an oblivious pseudorandom function (OPRF) in the pre-processing phase. However, re-executing existing uPSI protocols with each client imposes significant computational overhead for the server. In this paper, we present JAGUAR, a maliciously secure and efficient uPSI protocol designed for this setting. JAGUAR reduces online computation through a Divide-and-Combine optimization, requiring only $\mathcal{O}(\sqrt{|X|})$ homomorphic multiplications. Furthermore, it employs a novel fixed VOLE-based OPRF that enables reusable and lightweight pre-processing across multiple clients. Experimental results demonstrate that JAGUAR achieves up to $2.7\times$ improvement in online runtime compared to the SOTA protocol in LAN. In multi-client scenarios, JAGUAR further outperforms existing protocols by a wide margin in terms of scalability and overall performance.

  匹配依据：MPC: private set intersection

  </details>

- **IND-CCA Lattice Threshold KEM under 30 KiB**
  2026-01-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/021)
  Katharina Boudgoust, Oleksandra Lapiha, Rafaël del Pino, Thomas Prest

  <details><summary>摘要 / Abstract</summary>

  At Asiacrypt&#x27;25, Lapiha and Prest proposed a lattice-based IND-CCA threshold key-encapsulation mechanism (TKEM) obtained from a threshold identity-based encryption (TIBE) and a signature scheme. Their construction relies on a variant of the Boneh-Canetti-Halevi-Katz (BCHK) transform, instantiated with a lattice-based TIBE. However it suffers from large ciphertexts at 540 KiB for $\kappa = 128$ bits of security. We present substantial improvements to their TIBE, resulting in the first concretely efficient lattice-based IND-CCA TKEM, with ciphertexts just under 30 KiB for a threshold $T = 32$, $Q = 2^{45}$ queries, and the same $\kappa$. Our design simplifies the original framework by leveraging the power of random oracles already present in their construction. We further enhance efficiency by adopting approximate computations where appropriate and by replacing module-NTRU trapdoors with NTRU trapdoors, achieving a remarkable eighteenfold reduction in ciphertext size. Finally, leveraging recent developments in secret sharing, we ensure the verifiability of key-extraction shares even in the presence of malicious parties.

  匹配依据：MPC: secret sharing

  </details>

- **FlexProofs: A Vector Commitment with Flexible Linear Time for Computing All Proofs**
  2026-01-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.03031)
  Jing Liu, Liang Feng Zhang

  <details><summary>摘要 / Abstract</summary>

  In this paper, we introduce FlexProofs, a new vector commitment (VC) scheme that achieves two key properties: (1) the prover can generate all individual opening proofs for a vector of size $N$ in optimal time ${\cal O}(N)$, and there is a flexible batch size parameter $b$ that can be increased to further reduce the time to generate all proofs; and (2) the scheme is directly compatible with a family of zkSNARKs that encode their input as a multi-linear polynomial. As a critical building block, we propose the first functional commitment (FC) scheme for multi-exponentiations with batch opening. Compared with HydraProofs, the only existing VC scheme that computes all proofs in optimal time ${\cal O}(N)$ and is directly compatible with zkSNARKs, FlexProofs may speed up the process of generating all proofs, if the parameter $b$ is properly chosen. Our experiments show that for $N=2^{16}$ and $b=\log^2 N$, FlexProofs can be $6\times$ faster than HydraProofs. Moreover, when combined with suitable zkSNARKs, FlexProofs enable practical applications such as verifiable secret sharing and verifiable robust aggregation.

  匹配依据：MPC: secret sharing

  </details>

- **MOZAIK: A Privacy-Preserving Analytics Platform for IoT Data Using MPC and FHE**
  2026-01-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.02245)
  Michiel Van Kenhove, Erik Pohle, Leonard Schild, Martin Zbudila, Merlijn Sebrechts, Filip De Turck, Bruno Volckaert, Aysajan Abidin

  <details><summary>摘要 / Abstract</summary>

  The rapid increase of Internet of Things (IoT) systems across several domains has led to the generation of vast volumes of sensitive data, presenting significant challenges in terms of storage and data analytics. Cloud-assisted IoT solutions offer storage, scalability, and computational resources, but introduce new security and privacy risks that conventional trust-based approaches fail to adequately mitigate. To address these challenges, this paper presents MOZAIK, a novel end-to-end privacy-preserving confidential data storage and distributed processing architecture tailored for IoT-to-cloud scenarios. MOZAIK ensures that data remains encrypted throughout its lifecycle, including during transmission, storage, and processing. This is achieved by employing a cryptographic privacy-enhancing technology known as computing on encrypted data (COED). Two distinct COED techniques are explored, specifically secure multi-party computation (MPC) and fully homomorphic encryption (FHE). The paper includes a comprehensive analysis of the MOZAIK architecture, including a proof-of-concept implementation and performance evaluations. The evaluation results demonstrate the feasibility of the MOZAIK system and indicate the cost of an end-to-end privacy-preserving system compared to regular plaintext alternatives. All components of the MOZAIK platform are released as open-source software alongside this publication, with the aim of advancing secure and privacy-preserving data processing practices.

  匹配依据：MPC: secure multi party computation

  </details>

- **Efficient Threshold ML-DSA**
  2026-01-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/013)
  Sofía Celi, Rafaël del Pino, Thomas Espitau, Guilhem Niot, Thomas Prest

  <details><summary>摘要 / Abstract</summary>

  Threshold signature schemes allow a group of users to jointly generate a digital signature, providing resilience against faults and enhancing decentralization. With the advent of post-quantum cryptography, lattice-based threshold signatures have gained attention as viable PQ-threshold solutions. Nevertheless, existing constructions are limited in terms of their scalability, robustness. Worse, none is compatible with standardized schemes, particularly with the NIST-selected and standardized Module-Lattice-based Digital Signature Algorithm (ML-DSA) algorithm. In this work, we present the first threshold signature scheme that is fully compatible with ML-DSA, supporting secure and efficient signing for a small number of parties, with an average communication per party upper bounded by 1 MB up to 6 parties. Our construction leverages advanced short secret sharing techniques and integrates optimized rejection sampling to achieve a favorable balance between communication efficiency and correctness in distributed environments. We implement our construction in Go and evaluate its performance across local, LAN, and WAN network settings. Our benchmarks demonstrate that our threshold ML-DSA scheme is not only practically deployable but also well-suited for real-world applications, including multi-device cryptocurrency wallets, threshold-based TLS authentication, and for Tor&#x27;s directory authorities.

  匹配依据：MPC: secret sharing

  </details>

- **Analogs of absolutely maximally entangled states in nonlocal correlations via the sheaf-theoretic framework and its applications**
  2026-01-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.02009)
  Nripendra Majumdar, S. Aravinda

  <details><summary>摘要 / Abstract</summary>

  The foundational work by Bell led to an interest in understanding non-local correlations that arise from entangled states shared between distinct, spacelike-separated parties, which formed a foundation for the theory of quantum information processing. We investigate the question of maximal correlations analogous to the maximally entangled states defined in the entanglement theory of multipartite systems. In this work, we define the maximality of nonlocal correlation as being analogous to the absolutely maximally entangled state. To formalize this, we employ the sheaf-theoretic framework for contextuality, which generalizes non-locality. This provides a metric for correlations called contextual fraction (CF), which ranges from $0$ (non-contextual) to $1$ (maximally contextual). Using this, we have defined the absolutely maximal contextual correlations (AMCC), which are maximally contextual and have maximal marginals. The Popescu-Rohrlich (PR) box serves as the bipartite example, and we construct various extensions of such correlations in the tripartite case. An infinite family of various forms of AMCC is constructed using the parity check and the constraint satisfiability problem (CSP) construction. We also demonstrate the existence of maximally contextual correlations, which do not exhibit maximal marginals, and refer to them as non-AMCC. Furthermore, we showed that GHZ correlations in the $(n,2,2)$ setting give rise to AMCCs for the particular choice of measurement settings. The results are further applied to secret sharing and randomness extraction using AMCCs.

  匹配依据：MPC: secret sharing

  </details>

- **Secure, Verifiable, and Scalable Multi-Client Data Sharing via Consensus-Based Privacy-Preserving Data Distribution**
  2026-01-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.00418)
  Prajwal Panth, Sahaj Raj Malla

  <details><summary>摘要 / Abstract</summary>

  We propose the Consensus-Based Privacy-Preserving Data Distribution (CPPDD) framework, a lightweight and post-setup autonomous protocol for secure multi-client data aggregation. The framework enforces unanimous-release confidentiality through a dual-layer protection mechanism that combines per-client affine masking with priority-driven sequential consensus locking. Decentralized integrity is verified via step (sigma_S) and data (sigma_D) checksums, facilitating autonomous malicious deviation detection and atomic abort without requiring persistent coordination. The design supports scalar, vector, and matrix payloads with O(N*D) computation and communication complexity, optional edge-server offloading, and resistance to collusion under N-1 corruptions. Formal analysis proves correctness, Consensus-Dependent Integrity and Fairness (CDIF) with overwhelming-probability abort on deviation, and IND-CPA security assuming a pseudorandom function family. Empirical evaluations on MNIST-derived vectors demonstrate linear scalability up to N = 500 with sub-millisecond per-client computation times. The framework achieves 100% malicious deviation detection, exact data recovery, and three-to-four orders of magnitude lower FLOPs compared to MPC and HE baselines. CPPDD enables atomic collaboration in secure voting, consortium federated learning, blockchain escrows, and geo-information capacity building, addressing critical gaps in scalability, trust minimization, and verifiable multi-party computation for regulated and resource-constrained environments.

  匹配依据：MPC: multi party computation

  </details>

- **Applications of Secure Multi-Party Computation in Financial Services**
  2026-01-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.00334)
  Brahim Khalil Sedraoui, Abdelmadjid Benmachiche, Amina Makhlouf, Chaouki Chemam

  <details><summary>摘要 / Abstract</summary>

  The concept of Secure Multi-Party Computation (SMPC) is a cryptographic service that allows generating analysis of sensitive data related to finance under the collaboration of all stakeholders without violating the privacy of the research participants. This article shows the increasing significance of privacy protection in the contemporary financial services, where various stakeholders should comply with stringent security and regulatory standards. It discusses the main issues of scalability, computational efficiency, and working with very large datasets, and it identifies the directions of future research to make SMPC protocols more practical and efficient. The results highlight the possibility of SMPC to facilitate safe, transparent, and trustful financial transactions in an ecosystem that is becoming more digital.

  匹配依据：MPC: secure multi party computation

  </details>
