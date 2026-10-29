# 2026 · MPC · 仅预印本来源 · 第 5/6 页

[总目录](../PAPERS.md) · [上一页](2026-mpc-preprint-04.md) · [下一页](2026-mpc-preprint-06.md)

- **On the Security of MPC-in-the-Head Signatures with Correlated GGM Trees**
  2026-03-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/615)
  Thibauld Feneuil, Matthieu Rivain

  <details><summary>摘要 / Abstract</summary>

  Recent MPC-in-the-Head techniques enable the construction of signature schemes with compact signature sizes from various hardness assumptions. These techniques rely on commitments based on GGM trees, which have been optimized to further reduce the signature size with the so-called one-tree or correlated tree optimizations. While the one-tree technique has no incidence on the security of the scheme, this is not obvious for the correlated tree technique, and a formal security analysis of this technique has been missing in the literature. In this work, we fill this gap and provide the first formal security analysis of MPC-in-the-Head signature schemes based on correlated trees. We first exhibit a potential security flaw of this technique which rules out any hope for a security reduction to the underlying hardness assumption. In particular, we show that recovering the first $\lambda$ bits of the secret witness is sufficient to achieve a full key recovery (where $\lambda$ is the security level). The underlying assumption should hence be such that recovering these $\lambda$ bits is as hard as recovering the full witness. Some state-of-the-art schemes do not satisfy this condition, which prevents a direct application of the correlated tree technique. We then provide a formal security proof for signature schemes based on the correlated tree technique under this degraded hardness assumption. Our proof comes in several variants, in the random oracle mode or in the ideal cipher model, depending on the specific correlated tree construction. We also introduce a tweak for the instantiation of the leaf seed expansion in the ideal cipher model, which allows us to achieve a tighter security reduction. Our result shows that MPC-in-the-Head signatures based on correlated trees can achieve strong security guarantees and provides the first formal security proof for the MQOM v2 signature scheme, the on-going candidate in the NIST post-quantum standardization process with the shortest signature size in the MPC-in-the-Head family.

  匹配依据：MPC: mpc (context)

  </details>

- **Can Adaptive Communication Graphs Lower the Bottleneck Complexity of (Secure) Multiparty Computation?**
  2026-03-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/608)
  Lisa Kohl, Pierre Meyer, Divya Ravi, Nicolas Resch

  <details><summary>摘要 / Abstract</summary>

  The bottleneck complexity of a (secure) multiparty computation protocol is one measure of its communication-efficiency. It captures how well the communication load is balanced, and is defined as the maximum communication complexity required by any one party within the protocol execution. Prior works on this topic restricted attention to protocols with fixed communication graphs, i.e. whether or not a given party communicates to another only depends on the round number. We demonstrate the power of adaptively choosing communication graphs by developing various bottleneck-efficient protocols, both with and without security. Done naÏvely, protocols with adaptive communication graphs can exploit unnatural tricks, such as &quot;communicating with silence.&quot; To ensure our protocols are meaningful, we additionally stipulate that they should run correctly even in asynchronous networks (where we make no assumption on the adversarial message-delays other than being finite). [Bottleneck complexity of arbitrary functions.] With fixed communication graphs, Boyle, Jain, Prabhakaran, and Yu (ICALP&#x27;18) established the existence of a function $f\colon\{0,1\}^n\to\{0,1\}$ requiring $\Omega(n)$-bit bottleneck complexity, which is matched by the trivial protocol of having all parties send their inputs to one party. By adaptively choosing communication graphs, we show that any function $f\colon\{0,1\}^n\to\{0,1\}$ can be computed (securely) with bottleneck $O(n/\log n)$ (which we prove is essentially optimal), even in \emph{asynchronous} networks. [Bottleneck complexity of symmetric functions.] Prior works have demonstrated that special classes of symmetric functions, such as additive [Eriguchi, Asiacrypt&#x27;23] or abelian [Keller, Orlandi, Paskin-Cherniavsky, Ravi, ITC&#x27;23] functions can be computed bottleneck-efficiently with fixed communication graphs. We both expand the class of symmetric functions achievable with low bottleneck complexity, as well as show how input-adaptive communication graphs can be leveraged to further reduce the bottleneck complexity of some of our protocols.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Secure Two-Party Matrix Multiplication from Lattices and Its Application to Encrypted Control**
  2026-03-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.22857)
  Kaoru Teranishi

  <details><summary>摘要 / Abstract</summary>

  In this study, we propose a two-party computation protocol for approximate matrix multiplication of fixed-point numbers. The proposed protocol is provably secure under standard lattice-based cryptographic assumptions and enables matrix multiplication at a desired approximation level within a single round of communication. We demonstrate the feasibility of the protocol by applying it to the secure implementation of a linear control law. Our evaluation reveals that the client achieves lower online computational complexity compared to the original controller computation, while ensuring the privacy of controller inputs, outputs, and parameters. Furthermore, a numerical example confirms that the proposed method maintains sufficient precision of control inputs even in the presence of approximation and quantization errors.

  匹配依据：MPC: two party computation

  </details>

- **Privacy-Preserving EHR Data Transformation via Geometric Operators: A Human-AI Co-Design Technical Report**
  2026-03-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.22954)
  Maolin Wang, Beining Bao, Gan Yuan, Hongyu Chen, Bingkun Zhao, Baoshuo Kan, Jiming Xu, Qi Shi, Yinggong Zhao, Yao Wang, Wei Ying Ma, Jun Yan

  <details><summary>摘要 / Abstract</summary>

  Electronic health records (EHRs) and other real-world clinical data are essential for clinical research, medical artificial intelligence, and life science, but their sharing is severely limited by privacy, governance, and interoperability constraints. These barriers create persistent data silos that hinder multi-center studies, large-scale model development, and broader biomedical discovery. Existing privacy-preserving approaches, including multi-party computation and related cryptographic techniques, provide strong protection but often introduce substantial computational overhead, reducing the efficiency of large-scale machine learning and foundation-model training. In addition, many such methods make data usable for restricted computation while leaving them effectively invisible to clinicians and researchers, limiting their value in workflows that still require direct inspection, exploratory analysis, and human interpretation. We propose a real-world-data transformation framework for privacy-preserving sharing of structured clinical records. Instead of converting data into opaque representations, our approach constructs transformed numeric views that preserve medical semantics and major statistical properties while, under a clearly specified threat model, provably breaking direct linkage between those views and protected patient-level attributes. Through collaboration between computer scientists and the AI agent \textbf{SciencePal}, acting as a constrained tool inventor under human guidance, we design three transformation operators that are non-reversible within this threat model, together with an additional mixing strategy for high-risk scenarios, supported by theoretical analysis and empirical evaluation under reconstruction, record linkage, membership inference, and attribute inference attacks.

  匹配依据：MPC: multi party computation

  </details>

- **TALUS: FIPS-204-Exact Threshold ML-DSA via Boundary Clearance**
  2026-03-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.22109)
  Leo Kao, Raymond Chang

  <details><summary>摘要 / Abstract</summary>

  We present TALUS, a threshold signing protocol for ML-DSA (FIPS 204) that supports an arbitrary number of parties, emits signatures accepted by any unmodified ML-DSA verifier, and reduces, for a bounded number of signatures per key, to ML-DSA&#x27;s own assumptions (Module-LWE and SelfTargetMSIS). Its core is the Boundary Clearance Condition (BCC): for a constant fraction of nonces (31.7% at ML-DSA-65), the secret vector s2 provably cannot cross a rounding boundary, so the s2-dependent rejection check can be enforced offline on preprocessed nonces. This removes the interaction that forces multi-round signing in prior schemes, yielding a TEE-assisted one-round profile and a fully distributed honest-majority MPC profile with two online rounds, both built on a Carry Elimination Framework that computes the shared commitment w1 = HighBits(Ay) on secret shares, a step we show is unavoidable. We prove a lower bound: any FIPS-204-exact threshold scheme revealing a summed (Irwin-Hall) nonce admits an efficient key-recovery attack after about 2^30 signatures under one key (at ML-DSA-65), so no q_s-independent unforgeability is possible for this class. Complementing it, a q_s-bounded analysis certifies over 105 bits at the operational signing cap for the external view, with insider ceilings disclosed per view and a mandatory key rotation capping each key&#x27;s signing lifetime. A Rust implementation across all three FIPS 204 levels demonstrates practicality.

  匹配依据：MPC: mpc (context)

  </details>

- **PRIVADA: Private user-centric Data Aggregation**
  2026-03-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/579)
  Betul Askin Ozdemir, Beyza Bozdemir, Ionut Groza, Melek Önen

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving data aggregation has become a fundamental tool for large-scale analytics in AI-driven and cloud-based systems. While existing solutions provide the default privacy guarantee, i.e., input confidentiality, most assure a semi-honest adversary model and fail to simultaneously ensure user anonymity, selective disclosure, and result privacy in the multiple data customers environment. In this work, we introduce PRIVADA, a maliciously secure data aggregation solution that uses MPC in the SPDZ framework. Unlike prior data aggregation schemes using MPC with/without SPDZ, PRIVADA supports multiple data customers while preventing inference of user participation and resisting collusions in real-world data aggregation applications. Moreover, our work guarantees user privacy and result privacy, in addition to input privacy. PRIVADA outperforms the state-of-the-art solutions by providing security against participating parties, including malicious data owners, aggregators, and data customers. Our proof-of-concept implementation also supports the new privacy-preserving data aggregation by combining malicious security, being available for multiple data customers, and ensuring strong privacy guarantees in large-scale deployments. The aggregation operation on the aggregator side becomes simpler with PRIVADA, and experimental results show a 12–15 times speedup compared to the state-of-the-art. This confirms that malicious security and strong privacy guarantees can be achievable without sacrificing practicality.

  匹配依据：MPC: mpc (context)

  </details>

- **Asymptotically Ideal Hierarchical Secret Sharing Based on CRT for Integer Ring**
  2026-03-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.22011)
  Jian Ding, Cheng Wang, Hongju Li, Cheng Shu, Haifeng Yu

  <details><summary>摘要 / Abstract</summary>

  In Shamir&#x27;s secret sharing scheme, all participants possess equal privileges. However, in many practical scenarios, it is often necessary to assign different levels of authority to different participants. To address this requirement, Hierarchical Secret Sharing (HSS) schemes were developed, which partitioned all participants into multiple subsets and assigned a distinct privilege level to each. Existing Chinese Remainder Theorem (CRT)-based HSS schemes benefit from flexible share sizes, but either exhibit security flaws or have an information rate less than $\frac{1}{2}$. In this work, we propose a disjunctive HSS scheme and a conjunctive HSS scheme by using the CRT for integer ring and one-way functions. Both schemes are asymptotically ideal and are proven to be secure.

  匹配依据：MPC: secret sharing

  </details>

- **Asymptotically Ideal Conjunctive Hierarchical Secret Sharing Scheme Based on CRT for Polynomial Ring**
  2026-03-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.22001)
  Jian Ding, Cheng Wang, Hongju Li, Cheng Shu, Haifeng Yu

  <details><summary>摘要 / Abstract</summary>

  Conjunctive Hierarchical Secret Sharing (CHSS) is a type of secret sharing that divides participants into multiple distinct hierarchical levels, with each level having a specific threshold. An authorized subset must simultaneously meet the threshold of all levels. Existing Chinese Remainder Theorem (CRT)-based CHSS schemes either have security vulnerabilities or have an information rate lower than $\frac{1}{2}$. In this work, we utilize the CRT for polynomial ring and one-way functions to construct an asymptotically perfect CHSS scheme. It has computational security, and permits flexible share sizes. Notably, when all shares are of equal size, our scheme is an asymptotically ideal CHSS scheme with an information rate one.

  匹配依据：MPC: secret sharing

  </details>

- **Secret-Shared Shuffle from Authenticated Correlations**
  2026-03-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/566)
  Xiangfu Song, Xiaojian Liang, Ye Dong, Jianli Bai, Pu Duan, Changyu Dong, Tianwei Zhang, Ee-Chien Chang

  <details><summary>摘要 / Abstract</summary>

  Shuffle is a basic primitive for secure computation. Secret-shared shuffle refers to oblivious permutation over secret-shared data, which has broad applications in secret-sharing-based secure computation. Since shuffle is typically used in highly sensitive applications, malicious security is often necessary to provide realistic security guarantees. This paper proposes a new family of two-party maliciously secure secret-shared shuffle protocols with linear communication/computation cost and constant-round communication. Achieving this goal has been proven non-trivial by several recent attempts. We answer this question by proposing a new and simple shuffle paradigm based on authenticated correlations. We start by proposing a simple and efficient protocol template based on authenticated correlations with linear cost and constant-round communication. The protocol can be enhanced to be fully authenticated against a malicious sender, which avoids selective-failure attacks that incur the main overhead in existing solutions. However, our roadmap introduces a consistency issue from a malicious receiver, and the challenge is how to resolve the issue while preserving the expected efficiency property. To this end, we propose new efficiency-preserving consistency checks, enabled by a set of new techniques, optimizations, and analyses. Combining the consistency checks with our framework based on authenticated correlations, we propose two maliciously secure secret-shared shuffle protocols with linear cost and constant-round communication. We have implemented our protocols. Performance evaluation shows that our protocols are faster with lower communication than the state-of-the-art.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **SynCirc: Efficient Synthesis of Depth-Optimized Circuits from High-Level Languages (Extended Version)**
  2026-03-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/561)
  Arpita Patra, Joachim Schmidt, Thomas Schneider, Ajith Suresh, Hossein Yalame

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation (MPC) enables secure computation on private data. Many of today&#x27;s efficient MPC protocols need a representation of the evaluated function as circuit composed of Boolean or Lookup Tables (LUTs). To improve the practicality of MPC, we present SynCirc, a hardware synthesis framework optimized for MPC applications. Built on Verilog and the open-source tool Yosys-ABC, SynCirc introduces custom libraries and constraints for multi-input AND gates, achieving up to $3\times$ reduction in multiplicative depth and online rounds compared to TinyGMW (Demmler et al., CCS&#x27;15). SynCirc also offers an expanded library of efficient building blocks like comparison, multiplexers, equality checks and incorporates Boolean and LUT circuits. For these building blocks, we achieve improvements in multiplicative depth/online rounds between $22.3\%$ and $66.7\%$ over ShallowCC (Büscher et al., ESORICS&#x27;16). Our evaluation using the FLUTE framework (Brüggemann et al., IEEE S&amp;P’23) shows that SynCirc has $116\times$ less online communication than the multi-input AND gate protocol of Trifecta (Faraji and Kerschbaum, PETS&#x27;23). SynCirc introduces novel capabilities, including enhanced support for High-Level Synthesis (HLS) with the XLS tool, enabling developers to create secure functions in C/C++ without the need for expertise in hardware definition languages like Verilog. SynCirc is an open-source toolchain that democratizes secure computation, simplifies circuit synthesis and makes advanced privacy-preserving technologies more accessible.

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **Sharing The Secret: Distributed Privacy-Preserving Monitoring**
  2026-03-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.20107)
  Mahyar Karimi, K. S. Thejaswini, Roderick Bloem, Thomas A. Henzinger

  <details><summary>摘要 / Abstract</summary>

  In traditional runtime verification, a system is typically observed by a monolithic monitor. Enforcing privacy in such settings is computationally expensive, as it necessitates heavy cryptographic primitives. Therefore, privacy-preserving monitoring remains impractical for real-time applications. In this work, we address this scalability challenge by distributing the monitor across multiple parties -- at least one of which is honest. This architecture enables the use of efficient secret-sharing schemes instead of computationally intensive cryptography, dramatically reducing over-head while maintaining strong privacy guarantees. While existing secret-sharing approaches are typically limited to one-shot executions which do not maintain an internal state, we introduce a protocol tailored for continuous monitoring that supports repeated evaluations over an evolving internal state (kept secret from the system and the monitoring entities). We implement our approach using the MP-SPDZ framework. Our experiments demonstrate that, under these architectural assumptions, our protocol is significantly more scalable than existing alternatives.

  匹配依据：MPC: secret sharing

  </details>

- **PrivaLean: Low-Latency and High-Accuracy System for Secure 2PC Inference**
  2026-03-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/554)
  Jinghao Zhao, Hongwei Yang, Bobo Wang, Lichunxi Yang, Juncheng Li, Xiangrui Zeng, Meng Hao, Desheng Wang, Hui He, Weizhe Zhang

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation offers a powerful paradigm for protecting private information. However, its significant computational overhead and high communication latency limit its further application. To address these challenges, we present PrivaLean, an innovative framework designed for low-round and high-accuracy secure two-party inference under the semi-honest model. The core design of PrivaLean focuses on two main dimensions. First, for linear layer evaluation, we propose two distinct optimizations: a local random ciphertext generation mechanism that avoids massive offline interactions to drastically reduce communication rounds, and an intermediate encoding method that significantly minimizes memory overhead for low-memory devices. Second, to conquer non-linear evaluation bottlenecks, we design a co-optimized scheme featuring a novel trigonometric activation protocol and a data-distribution-aware training strategy. The activation requires only a single communication round and avoids expensive online truncation, while the training strategy can adapt to the precise data distribution and mitigate overfitting through knowledge distillation. The final accuracy is even higher than that of the ReLU-based baseline. Comprehensive evaluations on large-scale networks (e.g., MiniONN, ResNet-32/-50) demonstrate that in a Wide Area Network setting, PrivaLean completes a single ResNet-50 inference in 125.02 seconds. Compared to the state-of-the-art system Cheetah, PrivaLean achieves significantly fewer communication rounds and a 50.5% reduction in inference latency.

  匹配依据：MPC: secure multi party computation

  </details>

- **Graph-based Asynchrony with Quasilinear Complexity for Any Linear Verifiable Secret Sharing Scheme**
  2026-03-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/553)
  Hugo Delavenne, Lola-Baie Mallordy

  <details><summary>摘要 / Abstract</summary>

  Verifiable Secret Sharing (VSS) schemes usually consider synchronous communication, which cannot always be the case on real networks where packets can be lost or parties arbitrarily delayed. Allowing asynchrony adds a large overhead complexity cost: the dealer and communication complexity is in $O(n^2\log n)$ in state of the art $n$-parties Asynchronous VSS (AVSS) schemes [ABDM25], whereas there are synchronous schemes with only linear communications. To ensure that all honest parties agree on the same secret and are ready for reconstruction, AVSS schemes essentially perform a protocol similar to Bracha&#x27;s broadcast [Bra87]. While this immediately bounds the overall communication complexity of the protocol to be at least in $O(n^2)$, this method enables to reach the maximum threshold of malicious parties of $t=n/3$. However, a smaller threshold $t$ may be sufficient for some use cases, and one may want to take advantage of this. We consider a statistical scheme, meaning that the correctness and termination properties are only guaranteed with good probability. We propose a new method to transform any linear VSS scheme into a statistical AVSS. We build a statistical AVSS protocol Bonneval-on-Arc where each party only communicates with $d$ neighbours, a situation that we model by a $d$-regular graph. We obtain quasilinear communication complexity for the dealer, and sublinear complexity for each party, and a corruption threshold $t &lt; n/(d+2)$ as a tradeoff.

  匹配依据：MPC: secret sharing

  </details>

- **Post-Quantum Cryptography from Quantum Stabilizer Decoding**
  2026-03-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.19110) · [IACR ePrint](https://eprint.iacr.org/2026/548)
  Jonathan Z. Lu, Alexander Poremba, Yihui Quek, Akshar Ramkumar

  <details><summary>摘要 / Abstract</summary>

  Post-quantum cryptography currently rests on a small number of hardness assumptions, posing significant risks should any one of them be compromised. This vulnerability motivates the search for new and cryptographically versatile assumptions that make a convincing case for quantum hardness. In this work, we argue that decoding random quantum stabilizer codes -- a quantum analog of the well-studied LPN problem -- is an excellent candidate. This task occupies a unique middle ground: it is inherently native to quantum computation, yet admits an equivalent formulation with purely classical input and output, as recently shown by Khesin et al. (STOC &#x27;26). We prove that the average-case hardness of quantum stabilizer decoding implies the core primitives of classical Cryptomania, including public-key encryption (PKE) and oblivious transfer (OT), as well as one-way functions. Our constructions are moreover practical: our PKE scheme achieves essentially the same efficiency as state-of-the-art LPN-based PKE, and our OT is round-optimal. We also provide substantial evidence that stabilizer decoding does not reduce to LPN, suggesting that the former problem constitutes a genuinely new post-quantum assumption. Our primary technical contributions are twofold. First, we give a reduction from random quantum stabilizer decoding to an average-case problem closely resembling LPN, but which is equipped with additional symplectic algebraic structure. While this structure is essential to the quantum nature of the problem, it raises significant barriers to cryptographic security reductions. Second, we develop a new suit of scrambling techniques for such structured linear spaces, and use them to produce rigorous security proofs for all of our constructions.

  匹配依据：MPC: oblivious transfer

  </details>

- **NI-DKG: Non-Interactive Distributed Key Generation Using Blockchain and Zero-Knowledge Proofs**
  2026-03-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/552)
  Alex Kampa, Pau Escrich, Marta Bellés-Muñoz, Roger Baig

  <details><summary>摘要 / Abstract</summary>

  We present a non-interactive DKG protocol that eliminates complaint procedures through the systematic use of ZK proofs. The protocol requires a timed public bulletin board with adjoined computing capacity as its coordination layer, a capability realized in practice by smart-contract-enabled blockchains. Existing smart-contract DKGs detect invalid contributions only after submission, requiring dispute phases that introduce timing constraints and attack surfaces. In our protocol, each participant submits a single zk-SNARK proving the correctness of their contribution: polynomial commitment consistency, Feldman verification equations, and correct share encryption. The smart contract rejects any invalid proof, simplifying the protocol to non-interactive phases delimited by block numbers. The protocol relies on standard primitives: Shamir&#x27;s secret sharing, Feldman commitments, hashed ElGamal encryption, and Chaum-Pedersen discrete-log equality proofs, with on-chain verification via zk-SNARKs. We provide an implementation outline for EVM-compatible chains, including circuit specifications for key generation, threshold decryption, and optional secret key disclosure. We also discuss EVM verifier constraints on the number of public inputs and sketch approaches to address them.

  匹配依据：MPC: secret sharing

  </details>

- **A Complexity Hierarchy of Shuffles in Card-Based Protocols**
  2026-03-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.18608)
  Tomoki Ono, Suthee Ruangwises

  <details><summary>摘要 / Abstract</summary>

  Card-based cryptography uses physical playing cards to construct protocols for secure multi-party computation. Existing card-based protocols employ various types of shuffles, some of which are easy to implement in practice while others are considerably more complex. In this paper, we classify shuffle operations into several levels according to their implementation complexity. We motivate this hierarchy from both practical and theoretical perspectives, and prove separation results between several levels by showing that certain shuffles cannot be realized using only operations from lower levels. Finally, we propose a new complexity measure for evaluating card-based protocols based on this hierarchy.

  匹配依据：MPC: secure multi party computation

  </details>

- **DDH-based schemes for multi-party Function Secret Sharing**
  2026-03-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.17453) · [IACR ePrint](https://eprint.iacr.org/2025/1805)
  Marc Damie, Florian Hahn, Andreas Peter, Jan Ramon

  <details><summary>摘要 / Abstract</summary>

  Function Secret Sharing (FSS) schemes enable sharing efficiently secret functions. Schemes dedicated to point functions, referred to as Distributed Point Functions (DPFs), are the center of FSS literature thanks to their numerous applications including private information retrieval, anonymous communications, and machine learning. While two-party DPFs benefit from schemes with logarithmic key sizes, multi-party DPFs have seen limited advancements: $O(\sqrt{N})$ key sizes (with $N$, the function domain size) and/or exponential factors in the key size. We propose a DDH-based technique reducing the key size of existing multi-party schemes. In particular, we build an honest-majority DPF with $O(\sqrt[3]{N})$ key size. Our benchmark highlights key sizes up to $10\times$ smaller (on realistic problem sizes) than state-of-the-art schemes. Finally, we extend our technique to schemes supporting comparison functions.

  匹配依据：MPC: secret sharing

  </details>

- **Asymptotically ideal Disjunctive Hierarchical Secret Sharing Scheme with an Explicit Construction**
  2026-03-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.17257)
  Jian Ding, Cheng Wang, Haifeng Yu, Hongju Li, Cheng Shu

  <details><summary>摘要 / Abstract</summary>

  Disjunctive Hierarchical Secret Sharing (DHSS) scheme is a secret sharing scheme in which the set of all participants is partitioned into disjoint subsets. Each disjoint subset is said to be a level, and different levels have different degrees of trust and different thresholds. If the number of cooperating participants from a given level falls to meet its threshold, the shortfall can be compensated by participants from higher levels. Many ideal DHSS schemes have been proposed, but they often suffer from big share sizes. Conversely, existing non-ideal DHSS schemes achieve small share sizes, yet they fail to be both secure and asymptotically ideal simultaneously. In this work, we present an explicit construct of an asymptotically ideal DHSS scheme by using a polynomial, multiple linear homogeneous recurrence relations and one-way functions. Although our scheme has computational security and many public values, it has a small share size and the dealer is required polynomial time.

  匹配依据：MPC: secret sharing

  </details>

- **Novel CRT-based Asymptotically Ideal Disjunctive Hierarchical Secret Sharing Scheme**
  2026-03-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.16267)
  Hongju Li, Jian Ding, Fuyou Miao, Cheng Wang, Cheng Shu

  <details><summary>摘要 / Abstract</summary>

  Disjunctive Hierarchical Secret Sharing (DHSS)} scheme is a type of secret sharing scheme in which the set of all participants is partitioned into disjoint subsets, and each subset is said to be a level with different degrees of trust and different thresholds. In this work, we focus on the Chinese Remainder Theorem (CRT)-based DHSS schemes due to their ability to accommodate flexible share sizes. We point out that the ideal DHSS scheme of Yang et al. (ISIT, 2024) and the asymptotically ideal DHSS scheme of Tiplea et al. (IET Information Security, 2021) are insecure. Consequently, existing CRT-based DHSS schemes either exhibit security flaws or have an information rate less than $\frac{1}{2}$. To address these limitations, we propose a CRT-based asymptotically perfect DHSS scheme that supports flexible share sizes. Notably, our scheme is asymptotically ideal when all shares are equal in size. Its information rate achieves one and it has computational security.

  匹配依据：MPC: secret sharing

  </details>

- **NanoZK: Privacy-Preserving Verifiable Inference for Large Language Models via Layerwise Zero-Knowledge Proofs**
  2026-03-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.18046)
  Zhaohui Wang

  <details><summary>摘要 / Abstract</summary>

  We present NanoZK, a zero-knowledge proof system for verifiable LLM inference: clients and third-party auditors check that a provider executed the advertised model on a committed input without learning weights or activations. NanoZK introduces a layerwise proof framework that decomposes transformer inference into independently provable layers linked by a SHA-256 commitment chain, yielding constant-size sub-circuit proofs (3.5-3.7 KB; about 83 KB total at L=12), comparable in total size to and substantially more parallelizable than prior ZKML&#x27;s monolithic 101-126 KB proofs. We prove compositional soundness and zero-knowledge under standard assumptions, design 16-bit lookup-table approximations for softmax, GELU, and normalization with measured perplexity degradation below 1e-4 across six model/dataset combinations, and add a Fisher-information-guided audit-budget triage as an efficiency tool (full soundness still requires verifying every layer). On CPU the MLP sub-circuit proves in about 6.3 s prove-only (about 43 s setup plus prove) with about 22 ms verification at any width; attention prove-only time scales from 0.9 s (d=16) to 184 s (d=256); full-block end-to-end proofs are measured to d=128, with a projected GPU time of about 68 s per block at d=768 from measured O(d^2) MSM scaling and a conservative 15-30x GPU-MSM speedup range based on Icicle&#x27;s published 30x result for n &gt;= 2^20 and extrapolated to the smaller-n regime. Privacy scope: NanoZK hides weights and activations from verifiers and auditors but does not hide the prompt from the prover; this is complementary to HE/MPC.

  匹配依据：MPC: mpc (context)

  </details>

- **Dataflow-Oriented Classification and Performance Analysis of GPU-Accelerated Homomorphic Encryption**
  2026-03-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.16692)
  Ai Nozaki, Takuya Kojima, Hideki Takase, Hiroshi Nakamura

  <details><summary>摘要 / Abstract</summary>

  Fully Homomorphic Encryption (FHE) enables secure computation over encrypted data, but its computational cost remains a major obstacle to practical deployment. To mitigate this overhead, many studies have explored GPU acceleration for the CKKS scheme, which is widely used for approximate arithmetic. In CKKS, CKKS parameters are configured for each workload by balancing multiplicative depth, security requirements, and performance. These parameters significantly affect ciphertext size, thereby determining how the memory footprint fits within the GPU memory hierarchy. Nevertheless, prior studies typically apply their proposed optimization methods uniformly, without considering differences in CKKS parameter configurations. In this work, we demonstrate that the optimal GPU optimization strategy for CKKS depends on the CKKS parameter configuration. We first classify prior optimizations by two aspects of dataflows which affect memory footprint and then conduct both qualitative and quantitative performance analyses. Our analysis shows that even on the same GPU architecture, the optimal strategy varies with CKKS parameters with performance differences of up to 1.98 $\times$ between strategies, and that the criteria for selecting an appropriate strategy differ across GPU architectures.

  匹配依据：MPC: secure computation

  </details>

- **P$^2$RAG: Efficient Privacy-Preserving RAG Service Supporting Arbitrary Top-$k$ Retrieval**
  2026-03-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.14778)
  Yulong Ming, Mingyue Wang, Jijia Yang, Jie Xu, Zihan Wu, Cong Wang, Xiaohua Jia

  <details><summary>摘要 / Abstract</summary>

  Retrieval-Augmented Generation (RAG) enables large language models to use external knowledge, but outsourcing the RAG service raises privacy concerns for both data owners and users. Privacy-preserving RAG systems address these concerns by performing secure top-$k$ retrieval, which is typically implemented using secure sorting to identify relevant documents. However, existing systems face challenges supporting arbitrary $k$ due to their inability to change $k$, new security issues, and in particular, efficiency degradation with large $k$. This is a significant limitation because applications such as finance, law, and healthcare require a $k$ that is large enough to cause huge overhead for existing systems. Also, modern long-context models generally achieve higher accuracy with larger retrieval sets. We propose P$^2$RAG, an efficient privacy-preserving RAG service that supports arbitrary top-$k$ retrieval. Unlike existing systems, P$^2$RAG avoids sorting candidate documents. Instead, it uses an interactive bisection method to determine the set of top-$k$ documents. For security, P$^2$RAG uses secret sharing on two semi-honest non-colluding servers to protect the data owner&#x27;s database and the user&#x27;s prompt. It enforces restrictions and verification to defend against malicious users and tightly bounds the information leakage of the database. The experiments show that P$^2$RAG is 3--300$\times$ faster than the state-of-the-art PRAG for $k = 16$--$1024$.

  匹配依据：MPC: secret sharing

  </details>

- **A Maliciously-Secure Post-Quantum OPRF from Crypto Dark Matter**
  2026-03-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/533)
  Diego F. Aranha, Aron van Baarsen, Adam Blatchley Hansen, Kent Nielsen, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  We construct protocols for oblivious pseudorandom functions (OPRFs) based on alternating moduli assumptions in the &quot;Crypto Dark Matter&quot; paradigm (Boneh et al, TCC 2016). Prior OPRFs based on this type of assumption were only secure against a semi-honest adversary. We show how to obtain maliciously secure protocols, by leveraging new cut-and-choose techniques for generating correlated randomness based on vector oblivious linear evaluation (VOLE), which allow efficient conversions between different moduli in zero-knowledge and secure two-party computation. Compared with the state-of-the-art GOLD OPRF (Yang et al, S&amp;P 2025), our construction has a faster online phase in all settings, as well as overall better efficiency in the small-batch setting. Furthermore, our construction supports obtaining a secret-shared output, and can be extended to handle secret-shared inputs. This opens up additional applications in variants of private set intersection and secure database operations.

  匹配依据：MPC: private set intersection, secure two party computation

  </details>

- **On secret sharing from extended norm-trace curves**
  2026-03-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.14009)
  Olav Geil

  <details><summary>摘要 / Abstract</summary>

  In [4] Camps-Moreno et al. treated (relative) generalized Hamming weights of codes from extended norm-trace curves and they gave examples of resulting good asymmetric quantum error-correcting codes employing information on the relative distances. In the present paper we study ramp secret sharing schemes which are objects that require an analysis of higher relative weights and we show that not only do schemes defined from one-point algebraic geometric codes from extended norm-trace curves have good parameters, they also posses a second layer of security along the lines of [11]. It is left undecided in [4, page 2889] if the ``footprint-like approach&#x27;&#x27; as employed by Camps-Moreno herein is strictly better for codes related to extended norm-trace codes than the general approach for treating one-point algebraic geometric codes and their likes as presented in [12]. We demonstrate that the method used in [4] to estimate (relative) generalized Hamming weights of codes from extended norm-trace curves can be viewed as a clever application of the enhanced Goppa bound in [12] rather than a competing approach.

  匹配依据：MPC: secret sharing

  </details>

- **Secure Multi-party Matrix Invertibility Testing over Small Finite Fields**
  2026-03-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/514)
  Seungwoo Han, Jooyoung Lee, Seungmin Park, Mincheol Son

  <details><summary>摘要 / Abstract</summary>

  Multi-party matrix invertibility testing over finite fields of small order or characteristic is a pivotal operation for thresholdizing multivariate quadratic~(MQ) signature schemes. However, achieving perfect privacy in a constant number of rounds remains a challenge: existing solutions either suffer from information leakage, failing to provide perfect privacy, or require high computational and communication overhead, in particular, when $p\leq n$, where $p$ and $n$ denote the characteristic of the underlying field and the matrix size, respectively. To address this limitation, we propose two protocols for multi-party testing of matrix invertibility. The first protocol extends the Cramer-Damg{\aa}rd protocol to fields of small order by employing the field lifting technique. The second protocol is based on multi-party computation of the Samuelson-Berkowitz algorithm, specifically designed for fields of small characteristic. Both protocols are formalized in the arithmetic black-box~(ABB) model with Shamir&#x27;s secret sharing scheme. We show that both protocols achieve perfect privacy while allowing for a tradeoff between input-independent offline rounds and input-dependent online rounds, where the input corresponds to the shared matrices. Specifically, the first protocol runs in $7$ offline rounds with communication complexity $O(Nn^4)$ and in $3$ online rounds with communication complexity $O(n^4)$, and the second protocol runs in $3$ offline rounds with communication complexity $O(n^4)$ and in $9$ online rounds with communication complexity $O(n^4)$, where $n$ is the matrix size and $N$ is the number of parties.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Privacy-Preserving Machine Learning for IoT: A Cross-Paradigm Survey and Future Roadmap**
  2026-03-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.13570)
  Zakia Zaman, Praveen Gauravaram, Mahbub Hassan, Sanjay Jha, Wen Hu

  <details><summary>摘要 / Abstract</summary>

  The rapid proliferation of the Internet of Things has intensified demand for robust privacy-preserving machine learning mechanisms to safeguard sensitive data generated by large-scale, heterogeneous, and resource-constrained devices. Unlike centralized environments, IoT ecosystems are inherently decentralized, bandwidth-limited, and latency-sensitive, exposing privacy risks across sensing, communication, and distributed training pipelines. These characteristics render conventional anonymization and centralized protection strategies insufficient for practical deployments. This survey presents a comprehensive IoT-centric, cross-paradigm analysis of privacy-preserving machine learning. We introduce a structured taxonomy spanning perturbation-based mechanisms such as differential privacy, distributed paradigms such as federated learning, cryptographic approaches including homomorphic encryption and secure multiparty computation, and generative synthesis techniques based on generative adversarial networks. For each paradigm, we examine formal privacy guarantees, computational and communication complexity, scalability under heterogeneous device participation, and resilience against threats including membership inference, model inversion, gradient leakage, and adversarial manipulation. We further analyze deployment constraints in wireless IoT environments, highlighting trade-offs between privacy, communication overhead, model convergence, and system efficiency within next-generation mobile architectures. We also consolidate evaluation methodologies, summarize representative datasets and open-source frameworks, and identify open challenges including hybrid privacy integration, energy-aware learning, privacy-preserving large language models, and quantum-resilient machine learning.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Almost-Free Queue Jumping for Prior Inputs in Private Neural Inference**
  2026-03-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.12946)
  Qiao Zhang, Minghui Xu, Tingchuang Zhang, Xiuzhen Cheng

  <details><summary>摘要 / Abstract</summary>

  Privacy-Preserving Machine Learning as a Service (PP-MLaaS) enables secure neural network inference by integrating cryptographic primitives such as homomorphic encryption (HE) and multi-party computation (MPC), protecting both client data and server models. Recent mixed-primitive frameworks have significantly improved inference efficiency, yet they process batched inputs sequentially, offering little flexibility for prioritizing urgent requests. Naïve queue jumping introduces considerable computational and communication overhead, increasing non-negligible latency for in-queue inputs. We initiate the study of privacy-preserving queue jumping in batched inference and propose PrivQJ, a novel framework that enables efficient priority handling without degrading overall system performance. PrivQJ exploits shared computation across inputs via in-processing slot recycling, allowing prior inputs to be piggybacked onto ongoing batch computation with almost no additional cryptographic cost. Both theoretical analysis and experimental results demonstrate over an order-of-magnitude reduction in overhead compared to state-of-the-art PP-MLaaS systems.

  匹配依据：MPC: multi party computation

  </details>

- **Practically Efficient Linear-Time Server-Aided Private Set Union and Third Party Private Set Operations**
  2026-03-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/507)
  Foo Yee Yeo, Jason H. M. Ying

  <details><summary>摘要 / Abstract</summary>

  We present protocols for server-aided private set union (PSU), third-party private set difference (TP-PSD) and third-party private symmetric difference (TP-PSymD), offering both information-theoretically secure and cryptographically secure versions. In addition, we introduce variants of our TP-PSD and TP-PSymD protocols that are designed for practical deployment in settings when certain parties are resource-constrained. In a third-party setting, the receiver who obtains the output is an external inputless party with two other participating input parties. Our protocols for third-party private set operations significantly outperform those of Yeo and Ying (USENIX ’25), improving both asymptotic computational complexity and practical performance. Experimental results demonstrate substantial efficiency gains, including greatly reduced running times and scalability to much larger set sizes. Moreover, our server-aided private set union protocol is several times faster than existing state-of-the-art two-party private set union protocols.

  匹配依据：MPC: private set union

  </details>

- **FHorgEt: A Cryptographic Solution for Secure Machine Unlearning**
  2026-03-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/510)
  David Balbás, Dario Fiore, Georgios Raikos, Damien Robissout, Claudio Soriente

  <details><summary>摘要 / Abstract</summary>

  Data regulations grant users the right to be forgotten, empowering them to control if and when their data is used in applications such as machine learning training. Machine unlearning offers a promising mechanism to enforce this right by enabling the removal of specific training data from models. Existing machine unlearning approaches, however, assume an honest server that correctly executes all unlearning requests. In practice, this assumption is too strong: nothing prevents a server from falsely claiming to have performed unlearning while secretly retaining the original model or continuing to use the data for training. Such behaviours remain possible even when unlearning requests are verifiable---for example, via zero-knowledge proofs---because the server may still keep copies of the data or model. In this work, we argue that a security model for machine unlearning should capture data confidentiality throughout the lifecycle of a model, including training, inference, and unlearning. We introduce such a formalism and then present the first machine learning framework that provides cryptographic guarantees that unlearning requests are properly executed and that users&#x27; data is forgotten. We implement our framework using fully-homomorphic encryption (FHE) and secure multi-party computation (MPC), within a distributed setting where training, unlearning and inference requests are handled by a group of servers. Our constructions are secure in the honest-but-curious model if at least one of the servers is honest, and can be lifted against actively malicious servers following standard techniques. We also show, via a proof-of-concept implementation, that such a system does not add a significant overhead on top of FHE-based training.

  匹配依据：MPC: secure multi party computation

  </details>

- **Verified delegated quantum computation requires techniques beyond cut-and-choose**
  2026-03-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.09368)
  Fabian Wiesner, Anna Pappa

  <details><summary>摘要 / Abstract</summary>

  Delegated quantum computation enables a client with limited quantum capabilities to outsource computations to a more powerful quantum server while preserving correctness and privacy. Verification is crucial in this setting to ensure that the untrusted quantum server performs the computation honestly and returns correct results. A common verification method is the quantum cut-and-choose technique. Inspired by classical verification methods for two-party computation, the client uses the majority of the delegated rounds to test the server&#x27;s honesty, while keeping the remaining ones for the actual computation. Combining this technique with other methods, such as quantum error correction, could help achieve negligible cheating probabilities for the server; however, such methods can impose significant overheads making implementations unfeasible for the near-term future. In this work, we investigate whether cut-and-choose can yield efficient and secure verifiable quantum computation without additional costly techniques. We find that verifiable delegated quantum computation protocols relying solely on cut-and-choose techniques cannot be secure and efficient at the same time.

  匹配依据：MPC: two party computation

  </details>

- **Threshold Oblivious Pseudorandom Functions from Isogeny Group Actions**
  2026-03-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/489)
  Robi Pedersen

  <details><summary>摘要 / Abstract</summary>

  We present a new verifiable oblivious pseudorandom function (VOPRF) from isogeny group actions. Our construction is twice as fast as the previous state of the art of Delpech de Saint Guilhem and Pedersen at a slightly higher communication cost. One major contribution is the realization of a new proof protocol that is integrated as a two-party computation into the OPRF protocol, making the output verifiable. The main design choice behind our construction and this new proof system is to enable an easy transformation into a threshold protocol, something previous designs have not achieved. To this end, we present our VOPRF in a modular way based on different subroutines. We show how to replace these subroutines with their threshold counterparts, using simulation-based arguments. This results in the first threshold VOPRF from isogenies and one of the first threshold VOPRFs in the post-quantum literature. In contrast to other post-quantum threshold VOPRF designs, our construction has input and output size independent of the number of server parties and furthermore is robust, while other designs rely on aborts in the presence of malicious parties.

  匹配依据：MPC: two party computation

  </details>

- **The Landscape of Reusable Garbling**
  2026-03-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/492)
  Anasuya Acharya, Carmit Hazay, Rahul Satish

  <details><summary>摘要 / Abstract</summary>

  Reusability is a recurring theme in cryptography, appearing in various contexts where a one-time setup produces an encoded program that can be applied to multiple inputs. Prominent examples include indistinguishability obfuscation (iO), functional encryption (FE), laconic function evaluation (LFE), homomorphic secret-sharing (HSS), and function secret-sharing (FSS), each offering different trade-offs in efficiency and functionality. A particularly clean setting for reusability arises in garbling schemes: a garbler publishes a garbled circuit that can be evaluated on multiple inputs chosen by an evaluator. While one-time garbling has become a central and widely applicable primitive, its reusable variant has received comparatively little attention, typically studied only as a consequence of FE. In this work, we revisit the foundations of reusable garbling and develop a framework that clarifies its relationship to other reusable primitives. We first show that reusable garbling is equivalent to a single-key private-key variant of FE, capturing exactly the guarantees required for reusability and isolating it as a primitive in its own right. This equivalence further implies a black-box separation between reusable garbling and public-key FE, establishing that reusability can be realized entirely within the private-key setting without invoking public-key mechanisms. Building on this perspective, we demonstrate direct constructions from several inherently reusable primitives, including LFE, iO, HSS, and FSS, broadening the foundations of reusable garbling and revealing how reusability naturally emerges across diverse cryptographic paradigms.

  匹配依据：MPC: garbled circuit, garbling schemes, secret sharing

  </details>

- **SIMD HSS and aHMAC from Interval Encoding with Application to One-Bit-Per-Gate Garbling**
  2026-03-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/485)
  Jaehyung Kim, Hanjun Li, Huijia Lin, Zeyu Liu

  <details><summary>摘要 / Abstract</summary>

  Primitives enabling homomorphic computation over secret-shared values--Homomorphic Secret Sharing (HSS) and algebraic Homomorphic MACs (aHMAC)--have recently emerged as efficient alternatives to ciphertext-based primitives such as fully homomorphic encryption (FHE) and attribute-based encryption (ABE). Leveraging the distributed nature of secret sharing, direct constructions of HSS and aHMAC are simple, lightweight, avoid costly bootstrapping, and have many applications including one-bit-per-gate garbled circuits. Despite encouraging progress, all existing direct schemes still lack one key feature: efficient Single Instruction Multiple Data (SIMD) evaluation, a capability that has been critical to the efficiency of FHE. This gap leaves the potential of substantial efficiency improvements untapped. We present the first SIMD evaluation techniques for HSS and aHMAC, based on variants of the RLWE assumption. Using a new interval coefficient encoding, our approach embeds $\sqrt{n}$ integer-valued slots per ring element and supports $\sqrt{n}$-fold batch addition and multiplication in just $O(\log n)$ ring operations, achieving a multiplicative $\tilde O(\sqrt{n})$ improvement in amortized efficiency over prior direct constructions. Building on top of these improvements, we show a streamlined one-bit-per-gate SIMD garbling scheme with similar efficiency gains in the online phase. Our efficiency gains are concrete. Concrete operation counts and microbenchmark based estimates show $6\times$--$10\times$ improvements in amortized multiplication cost over prior non-SIMD constructions, with up to $25\times$--$50\times$ speedups for aggregation-heavy workloads such as matrix--vector multiplication. These results demonstrate the practical potential of SIMD techniques for secret-sharing-based homomorphic computation.

  匹配依据：MPC: garbled circuits, garbling scheme, secret sharing

  </details>

- **Duty-Free Bits: Projectivizing Garbling Schemes**
  2026-03-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/476)
  Nakul Khambhati, Anwesh Bhattacharya, David Heath

  <details><summary>摘要 / Abstract</summary>

  Garbling schemes are powerful primitives that enable secure computation between a mutually untrusting garbler and evaluator. A projective garbling scheme is one that encodes the evaluator&#x27;s input in a simple bit-by-bit manner. Projective schemes, such as the seminal scheme of Yao, are versatile, as they are naturally compatible with other simple tools, such as $1$-out-of-$2$ oblivious transfer (OT). There exist garbling schemes that naturally operate over large finite fields, some of which require only efficient information-theoretic (IT) techniques. However, here the evaluator&#x27;s input is encoded via an affine function over a large field, so these schemes are not naturally projective, reducing their versatility. We provide a transformation that efficiently projectivizes such schemes. Consider an arithmetic garbling scheme where the evaluator&#x27;s input consists of elements from a large prime field. Our symmetric-key-based garbling techniques give a mechanism to translate from Yao-style garbled labels to IT-style garbled labels at cost proportional to the input and output labels: crossing the border is duty-free! We apply our technique to two problems. (1) Recent works show that projective garbling schemes solve a problem central to trust-minimized bridges for the Bitcoin blockchain. BABE (Garg et al., 2026) and Argo MAC (Eagen and Lai, 2026) give two different approaches. Both works implicitly construct an efficient IT garbling scheme, then use naive bit-decomposition to achieve projectivity. We construct and implement drop-in replacements for both; we improve BABE&#x27;s encoding size by $51\times$, and Argo MAC&#x27;s by $23\times$. (2) Our technique implies a non-interactive reduction from vector oblivious linear evaluations (VOLEs) over $\mathbb{F}_p$ to $1$-out-of-$2$ OTs. To our knowledge, ours is the state-of-the-art Minicrypt (plus base OTs) protocol for large field VOLE secure against a malicious receiver. It costs only $O((\lambda + n) \lg p)$ bits.

  匹配依据：MPC: garbling scheme, garbling schemes, oblivious transfer, secure computation

  </details>

- **A Note on \`\`Linear-Communication ACSS with Guaranteed Termination and Lower Amortized Bound''**
  2026-03-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/469)
  Xiaoyu Ji, Junru Li, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  In this note, we demonstrate that the construction of asynchronous complete secret sharing (ACSS) proposed in the recent work by Qin et al., accepted at Eurocrypt 2026, is insecure. In particular, we identify several issues affecting the liveness of their protocol and present attacks that compromise its correctness.

  匹配依据：MPC: secret sharing

  </details>

- **Icefish: Practical zk-SNARKs for Verifiable Genomics**
  2026-03-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/463)
  Alexander Frolov, Maurice Shih, Rob Patro, Ian Miers

  <details><summary>摘要 / Abstract</summary>

  Individual genomic data is a uniquely sensitive type of user data. While many papers have considered using Multi-Party Computation (MPC) or Fully Homomorphic Encryption (FHE) to allow collaborators to study combined genomic datasets they cannot share, few have considered verifying the results of genomic computations, either in research studies or in the emerging area of personalized genetic therapies. In this paper, we initiate the first systematic study of zero-knowledge proofs for verifiable genomics, providing both building blocks for verifying common operations in computational genomics, such as sequence alignment, and exploring two end-to-end applications: Verifiable Genome-Wide Association Studies: A Genome-Wide Association Study (GWAS) study operates over a repository of genomic data, identifying statistical correlations between genetic variations and observed traits or medical conditions. Our system enables third parties to verify that research was honestly computed over an authenticated, untampered database, ensuring both the integrity of the underlying data set and the correctness of the resulting science. We achieve practical performance (&lt;40 minutes proving time) for studies of sizes equal to those in the existing genomics literature. Verifiable CRISPR eligibility: We propose using zk-SNARKs in the context of gene engineering (e.g. CRISPR). To our knowledge, this is a new use case for zk-SNARKs. We implement and optimize models for detecting ``on-target&#x27;&#x27; and ``off-target&#x27;&#x27; sites for a CRISPR probe in zk-SNARKs, so users can, for example, demonstrate eligibility for a therapy or trial without having to reveal their own DNA sequence. In support of these applications, we develop new building blocks, like zero-knowledge proofs of sequence alignment that are 30x faster than the prior state of the art, and storage-efficient indexes for Merkle trees for large scale genomic data that asymptotically reduce storage costs.

  匹配依据：MPC: multi party computation

  </details>

- **Good-Enough LLM Obfuscation (GELO)**
  2026-03-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.05035)
  Anatoly Belikov, Ilya Fedotov

  <details><summary>摘要 / Abstract</summary>

  Large Language Models (LLMs) are increasingly served on shared accelerators where an adversary with read access to device memory can observe KV caches and hidden states, threatening prompt privacy for open-source models. Cryptographic protections such as MPC and FHE offer strong guarantees but remain one to two orders of magnitude too slow for interactive inference, while static obfuscation schemes break under multi-run statistical attacks once the model is known. We present GELO (Good-Enough LLM Obfuscation), a lightweight protocol for privacy-preserving inference that limits information leakage from untrusted accelerator observations by hiding hidden states with fresh, per-batch invertible mixing. For each offloaded projection, the TEE samples a random matrix $A$, forms $U = AH$, offloads $U$ and weights W to the accelerator, and then applies $A^{-1}$ on return, so that $A^{-1}((AH)W ) = HW$ and outputs are unchanged. Because mixing is never reused across batches, the attacker faces only a single-batch blind source separation problem. We analyse information leakage and introduce two practical defences: (i) non-orthogonal mixing to mask Gram matrices, and (ii) orthogonal mixing augmented with a small fraction of high-energy &quot;shield&quot; vectors that pollute higher-order statistics. On Llama-2 7B, GELO preserves float32 outputs exactly, closely matches low-precision baselines, and shows about $20$--$30\%$ compute-side overhead in a controlled offload microbenchmark; an unoptimized remote prototype is dominated by transport overhead, motivating deeper serving-engine integration. GELO resists ICA/BSS and anchor-assisted attacks; a 60M-parameter transformer-based unmixing attack also fails under strong mixing and shielding.

  匹配依据：MPC: mpc (context)

  </details>

- **Fuzzy Private Set Intersection for Real-World Datasets**
  2026-03-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/441)
  Satvinder Singh, Yanxue Jia, Aniket Kate

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection (PSI) allows two mutually distrusting parties to compute the intersection of their private sets without revealing any additional information. Fuzzy PSI, an approximate variant of PSI, allows the receiver to learn points of the sender that are ``close&quot; to its points. More formally, the receiver learns all $y$ in the sender&#x27;s set that satisfy $dist(x,y)&lt; \delta$ for some element $x$ in the receiver&#x27;s set and threshold parameter $\delta$. Recently, there has been significant progress on Fuzzy PSI, as it allows us to realize several important applications such as password matching, facial recognition, and contact tracing in a privacy-preserving manner. However, existing Fuzzy PSI constructions make strong assumptions on the input sets, such as receiver set disjointedness or projected disjointedness. In this work, we analyze those strong assumptions from a practical viewpoint and observe a gap between theory and practice, i.e., real-world data sets do not abide to those assumptions. To bridge the gap, we first define a new relaxed and weaker assumption based on the low density of sets, demonstrate the assumption to be practical, and build a compiler that converts constructions under the strong assumption to those under the new, practical assumption. At the core of our transformation is a novel idea involving higher-dimensional lifting and coloring. Combining our transformation with current Fuzzy PSI protocols under the strong assumption yields efficient and practical Fuzzy PSI protocols. We also concretely analyze the run-time and overhead of our transformed protocols for parameters for illustrative applications, such as password matching.

  匹配依据：MPC: private set intersection

  </details>

- **Asynchronous MPC with Abort**
  2026-03-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/455)
  Ananya Appan, David Heath, Ling Ren

  <details><summary>摘要 / Abstract</summary>

  Most prior works on secure Multi-Party Computation (MPC) in asynchronous networks study Guaranteed Output Delivery (GOD), meaning that all parties learn the function output. Asynchronous MPC protocols with GOD necessarily tolerate only t &lt; n/3 corruptions, and they necessarily allow the adversary to exclude the inputs of up to t honest parties from the computation, a phenomenon referred to as input loss. Seeking improvements to threshold/input loss, we consider weakening GOD to security with abort, a standard notion studied in the context of synchronous networks. Unfortunately we show that, when these standard notions are applied in asynchrony, it is not possible to improve the corruption threshold or the input loss. We therefore study relaxations of these standard notions under which protocols can be improved. In particular, we propose a relaxation of the standard notion of correctness for asynchronous MPC protocols. Our relaxed notion requires only that parties obtain the correct output when all parties are honest and when at most a threshold A of the parties are asynchronous. We present several impossibility and feasibility results that completely characterize what is possible in the context of our relaxed correctness. For instance, it is possible to achieve selective abort even when t &lt; n parties are corrupt if (and only if) A &lt; (n-t)/2, but it is impossible to achieve unanimous abort unless t &lt; n/3, even when A=0. We additionally propose a new notion of identifiable abort for asynchronous networks (aIA), and we show that we can achieve fair MPC with aIA and min(A,t) input loss.

  匹配依据：MPC: secure multi party computation

  </details>

- **Toward multi-purpose quantum communication networks: from theory to protocol implementation**
  2026-03-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.02923)
  Lucas Hanouz, Marc Kaplan, Jean-Sébastien Kersaint Tournebize, Chin-te Liao, Anne Marin

  <details><summary>摘要 / Abstract</summary>

  Most quantum communication networks around the world are used for a single task: quantum key distribution. In order to initiate the transition to multi-purpose quantum communication networks, we demonstrate the implementation of two different tasks on the same quantum key distribution hardware. Specifically, we focus on quantum oblivious transfer and quantum tokens. Our main contribution is to establish a methodology that greatly simplifies the expertise required to achieve the deployment, assess its performance, and evaluate its feasibility at a large scale. The implementation that we present is full-stack. It is based on a development framework that allows running user-defined applications both with simulated or real quantum communication backend. The hardware used for the implementation is VeriQloud&#x27;s Qline. The simulation backend reproduces exactly the inputs and outputs of the real hardware, but also its losses and errors. It can therefore be used to validate the implementation before running it on the real hardware. The sources of the software that we use are fully open, making our research reproducible. The security of the implementations on real hardware are discussed with respect to security bounds previously known in the literature. We also discuss the engineering choices that we made in order to make the implementations feasible. By establishing a methodology to evaluate the performance and security of quantum communication protocols, we take a significant step towards industrializing and deploying large-scale, multi-purpose quantum communication networks.

  匹配依据：MPC: oblivious transfer

  </details>

- **Information-Theoretic Strong Traceable Secret Sharing Schemes**
  2026-03-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/435)
  Oriol Farràs, Miquel Guiot

  <details><summary>摘要 / Abstract</summary>

  Traceable secret sharing complements traditional schemes by enabling the identification of parties who sell their shares. Recently, two independent works extended traceable secret sharing to general access structures. Goyal, Jain, and Partap [EC&#x27;26] introduced a model in which a reconstruction box is augmented with a label $I \subseteq [n]$ and is only required to distinguish between two secrets when queried with the shares of parties in $I$. Based on how this label relates to the corrupted set $J$ that built the box, they defined two notions of traceability. If $I \cap J = \emptyset$, the model is called $\emptyset$-strong traceability, for which they presented a construction based on indistinguishability obfuscation (iO). Otherwise, their model is calledstrong traceability, for which they proved an impossibility result. Farràs and Guiot [EC&#x27;26] proposed a different model, which we call hiding traceability, where the reconstruction box has no label and the access structure is hidden from the parties. In this work, we improve traceable secret sharing for general access structures in three directions. First, we present a fully information-theoretic scheme for the $\emptyset$-strong traceability model, eliminating the need for strong cryptographic assumptions. This resolves an open question posed by Goyal, Jain, and Partap, who asked what are the minimal assumptions needed in the $\emptyset$-strong traceability model. Second, motivated by the impossibility of strong traceability, we introduce a relaxed notion calledhidden mildly strong traceability. This model is relevant in practice and bridges the strong and hidden models. For this setting, we present an information-theoretic scheme for general access structures. Finally, we consider the more general model of stateful traceability, where reconstruction boxes may keep state across queries, and we prove an impossibility result for this setting.

  匹配依据：MPC: secret sharing

  </details>

- **Hermine: An Efficient Lattice-based FROST-like Threshold Signature**
  2026-03-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/419)
  Giacomo Borin, Sofía Celi, Rafael del Pino, Thomas Espitau, Shuichi Katsumata, Guilhem Niot, Thomas Prest, Kaoru Takemure

  <details><summary>摘要 / Abstract</summary>

  Threshold signatures have regained a strong interest recently, driven by applications in cryptocurrencies and NIST&#x27;s ongoing call for threshold schemes. Among them, FROST - a classical threshold Schnorr signature scheme already in real-world deployment - stands out. Its appeal lies in three core features: partially non-interactive signing, non-interactive identifiable abort (IA), and proactive security. In contrast, while post-quantum (PQ) threshold signatures have seen significant advances in recent years, no existing scheme simultaneously provides even two of these features. Considering the imminent need to migrate to PQ cryptography, this state-of-the-art remains unsatisfactory. In this work, we propose Hermine, a lattice-based threshold signature that offers the full feature set of FROST under standard lattice assumptions. Hermine is designed to efficiently support the Medium scale of parties ($N \le 64$) as defined in the NIST threshold call, producing a small \Raccoon signature of size $11$ KB. Our main technical contribution is introducing an everywhere-short secret sharing, which splits a short secret vector $\mathbf{s} \in R_q^\ell$ into short shares and admits a short linear reconstruction algorithm. While the resulting construction appears intuitive, its security proof requires a non-trivial, fine-grained analysis of the information on $\mathbf{s}$ that is inherently leaked by the short shares. Furthermore, we formalize game-based unforgeability and IA definitions with proactive security, which may be of independent interest.

  匹配依据：MPC: secret sharing

  </details>

- **An Ultra-Robust Privacy Preserving Scheme for Federated Learning using Distributed Homomorphic Encryption**
  2026-03-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/416)
  Ikhlas Mastour, Layth Sliman, Boussad Ait Salem, Balthazar Bauer, Raoudha Ben Djemaa, Kamel Barkaoui

  <details><summary>摘要 / Abstract</summary>

  Federated Learning is an emerging machine learning paradigm that enables distributed model training directly at data sources and transmitting only model updates, thereby reducing communication bottlenecks and mitigating risks associated with raw data exposure. Despite these advantages, recent advances have demonstrated that privacy in federated learning remains limited and subject to inference attacks that exploit shared model updates to extract sensitive information. To address this limitation, we propose Robust and Resilient Federated Learning using Distributed Homomorphic Encryption (RRFL-DHE), a privacy-preserving federated learning framework that combines a distributed homomorphic encryption scheme with threshold linear secret sharing. The framework enables clients to encrypt their model updates to allow secure aggregation without exposing individual contributions. To maintain resilience against client dropouts, RRFL-DHE incorporates a dropout management protocol, maintaining training continuity and accurate global model reconstruction. To assess our framework, we provide a rigorous security proof against a semi-honest server model and evaluate RRFL-DHE on non-IID MNIST and Fashion MNIST datasets using SVM and CNN models. The results show that RRFL-DHE preserves model utility with less than 1% deviation compared to the FedAvg approach, while outperforming the xMK-CKKS approach by approximately 15% in accuracy. These findings highlight the importance of RRFL-DHE as a promising solution for distributed computing, while preserving privacy, maintaining utility, and ensuring resilience against dropouts.

  匹配依据：MPC: secret sharing

  </details>

- **Accurate, private, secure, federated U-statistics with higher degree**
  2026-03-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.01986)
  Quentin Sinh, Jan Ramon

  <details><summary>摘要 / Abstract</summary>

  We study the problem of computing a U-statistic with a kernel function f of degree k $\ge$ 2, i.e., the average of some function f over all k-tuples of instances, in a federated learning setting. Ustatistics of degree 2 include several useful statistics such as Kendall&#x27;s $τ$ coefficient, the Area under the Receiver-Operator Curve and the Gini mean difference. Existing methods provide solutions only under the lower-utility local differential privacy model and/or scale poorly in the size of the domain discretization. In this work, we propose a protocol that securely computes U-statistics of degree k $\ge$ 2 under central differential privacy by leveraging Multi Party Computation (MPC). Our method substantially improves accuracy when compared to prior solutions. We provide a detailed theoretical analysis of its accuracy, communication and computational properties. We evaluate its performance empirically, obtaining favorable results, e.g., for Kendall&#x27;s $τ$ coefficient, our approach reduces the Mean Squared Error by up to four orders of magnitude over existing baselines.

  匹配依据：MPC: multi party computation

  </details>

- **Putting the OPTI in Round Optimal IA-MPC in the Plain Model**
  2026-02-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/406)
  Yashvanth Kondi, Divya Ravi, Jure Sternad, Sophia Yakoubov

  <details><summary>摘要 / Abstract</summary>

  We advance the study of best-possible security guarantees of two-round secure multiparty computation in the plain model. While Goel et al. (TCC &#x27;21) showed the infeasibility of Identifiable Abort in two rounds in the plain model with a standard honest majority (i.e. $t &lt; n/2$), the effect of relaxing the setting to an honest supermajority has not been established. In this work, we close this gap. When $t &lt; n/3$, we show that two rounds are sufficient to achieve identifiable abort. Notably, ours is the first two-round general-purpose MPC construction in the plain model tolerating more than one corruption that achieves a guarantee stronger than unanimous abort. We obtain our construction via a new compiler that lifts any protocol with unanimous abort to one that achieves identifiable abort. A core building block for our compiler is Oblivious Public Transfer with Intermediaries (OPTI), a new primitive that we introduce which may be of independent interest.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Privacy-Preserving Local Energy Trading Considering Network Fees**
  2026-02-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.23698)
  Eman Alqahtani, Mustafa A. Mustafa

  <details><summary>摘要 / Abstract</summary>

  Driven by the widespread deployment of distributed energy resources, local energy markets (LEMs) have emerged as a promising approach for enabling direct trades among prosumers and consumers to balance intermittent generation and demand locally. However, LEMs involve processing sensitive participant data, which, if not protected, poses privacy risks. At the same time, since electricity is exchanged over the physical power network, market mechanisms should consider physical constraints and network-related costs. Existing work typically addresses these issues separately, either by incorporating grid-related aspects or by providing privacy protection. To address this gap, we propose a privacy-preserving protocol for LEMs, with consideration of network fees that can incite participants to respect physical limits. The protocol is based on a double-auction mechanism adapted from prior work to enable more efficient application of our privacy-preserving approach. To protect participants&#x27; data, we use secure multiparty computation. In addition, Schnorr&#x27;s identification protocol is employed with multiparty verification to ensure authenticated participation without compromising privacy. We further optimise the protocol to reduce communication and round complexity. We prove that the protocol meets its security requirements and show through experimentation its feasibility at a typical LEM scale: a market with 5,000 participants can be cleared in 4.17 minutes.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Bittersweet Signatures: Bringing LWR to a Picnic for Hardware-Friendly MPC-in-the-Head**
  2026-02-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/397)
  Brieuc Balon, Gianluca Brian, Sebastian Faust, Carmit Hazay, Elena Micheli, François-Xavier Standaert

  <details><summary>摘要 / Abstract</summary>

  Post-quantum signature schemes are becoming increasingly important due to the threat of quantum computers to classical cryptographic schemes. Among the approaches considered in the literature, the MPC-in-the-head paradigm introduced by Ishai et al. (STOC&#x27;07) provides an innovative solution for constructing zero-knowledge proofs by exploiting Multi-Party Computation (MPC). This technique has proven to be a versatile tool in order to design efficient cryptographic schemes, including post-quantum signatures. Building on the MPC-in-the-head paradigm, we introduce Bittersweet signatures, a new class of signature schemes based on the Learning With Rounding (LWR) assumption. Their main advantage is conceptual simplicity: by exploiting (almost) key-homomorphic pseudorandom functions (PRFs), a cryptographic object that preserves pseudorandomness while allowing linear operations on keys, we obtain a very regular design offering nice opportunities for parallel implementations. Theoretically, analyzing Bittersweet signatures requires addressing significant challenges related to the (carry) leakage that almost key-homomorphic operations lead to. Concretely, Bittersweet signatures natively lead to competitive signature sizes, trading moderate software performance overheads for hardware performance gains when compared to state-of-the-art MPC-in-the-head schemes (e.g., relying on code-based assumptions), while admittedly lagging a bit behind recent algorithms based on the VOLE-in-the-head or Threshold-Computation-in-the-head frameworks. Besides, their scalability and algebraic structure makes them promising candidates for leakage-resilient implementations. The new abstractions we introduce additionally suggest interesting research directions towards further optimization and generalization.

  匹配依据：MPC: multi party computation

  </details>

- **Necessary and Sufficient Conditions for the Existence of Ideal Linear Secret Sharing Schemes for Arbitrary Access Structures**
  2026-02-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/388)
  Zheng Chen, Qiuxia Xu, Chunming Tang

  <details><summary>摘要 / Abstract</summary>

  Determining whether an arbitrary access structure can be realized by an ideal linear secret sharing scheme is an important research topic. we use linear codes as the main tool to construct matrices $H$ and $G$ over a finite field $\mathbb{F}_q$ for a given access structure $\Gamma_{\min}$, and show that a necessary and sufficient condition for the existence of an ideal linear secret sharing scheme realizing $\Gamma_{\min}$ is that the equation $GH^{\mathsf{T}}=0$ has a solution. If this equation has a solution, then $H$ serves as the parity-check matrix of a linear code that realizes $\Gamma_{\min}$, and $G$ is the corresponding generator matrix. Furthermore, we prove that the result is equivalent to the following statement: there exists an ideal linear code for realizing the $\Gamma_{\min}$ if and only if it is the port of a matroid that is representable over $\mathbb{F}_q$.

  匹配依据：MPC: secret sharing

  </details>

- **Multi-Committee MPC: From Unanimous to Identifiable Abort**
  2026-02-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/381)
  Lichun Li, Hongqing Liu, Jiawei Ni, Chaoping Xing, Chen Yuan

  <details><summary>摘要 / Abstract</summary>

  In this work, we consider dishonest majority MPC protocols with $(1-\epsilon)n$ corrupted parties for some constant $\epsilon\in (0,1/2)$. In this setting, there exist MPC protocols with unanimous abort that achieve constant communication in both online and offline phases via a packed secret sharing scheme. Departing from their approaches, we revisit the &#x27;&#x27;committee-based&#x27;&#x27; approach to design an efficient MPC protocol with constant online and offline communication complexity. To balance the communication load of each party, our protocol adopts multiple committees, each of constant size. The computation of circuit $C$ is then divided into layers, each assigned to one committee. To securely transmit messages between committees, we introduce the handoff gates, incurring only a slight communication overhead. Furthermore, we leverage circuit-dependent preprocessing and incremental checking to improve the online efficiency. Compared to other MPC protocols in the same corruption setting, our protocol achieves the smallest concrete total communication complexity. Building upon our multi-committee unanimous-abort protocol, we upgrade it to identifiable abort by adapting a technique from (Rivinius, EUROCRYPT 2025). To integrate this technique into our setting, we adjust the verification timing and introduce a king party to reduce the communication complexity of openings. This yields the first identifiable-abort MPC protocol with constant communication complexity in the sub-optimal dishonest majority setting.

  匹配依据：MPC: secret sharing

  </details>

- **Is PSI Really Faster Than PSU? Achieving Efficient PSU with Invertible Bloom Filters**
  2026-02-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/376)
  Lucas Piske, Ni Trieu

  <details><summary>摘要 / Abstract</summary>

  Private Set Union (PSU) enables two parties to compute the union of their private sets without revealing anything beyond the union itself. Existing PSU protocols remain much slower than private set intersection (PSI), often by a factor of around $30\times$. In this work, we present the first PSU protocol based on Invertible Bloom Lookup Tables (IBLTs), introducing a fundamentally new framework that departs from traditional, inefficient approaches. Our protocol exploits structural invariants between each party’s IBLTs and their union to compute the union efficiently without explicitly constructing a combined IBLT. Central to our approach is the notion of union peelability, which allows union elements to be recovered directly from the original IBLTs. We securely implement this functionality using only Oblivious Transfer (OT) and Oblivious Pseudorandom Function (OPRF) for equality checks, ensuring no information beyond the union is leaked. As a result, for set sizes ranging from $2^{14}$ to $2^{20}$, our protocol achieves a runtime of $0.08$ to $2.95$ seconds in the LAN setting, which is comparable to state-of-the-art PSI. We also show substantial speedups over prior PSU work—up to $10\times$ faster in LAN settings and consistently faster in WAN scenarios—while maintaining linear computation and communication complexity with small constants.

  匹配依据：MPC: oblivious transfer, private set intersection, private set union

  </details>

- **Efficient Multi-Party Secure Comparison over Different Domains with Preprocessing Assistance**
  2026-02-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.19604)
  Kaiwen Wang, Xiaolin Chang, Yuehan Dong, Ruichen Zhang

  <details><summary>摘要 / Abstract</summary>

  Secure comparison is a fundamental primitive in multi-party computation, supporting privacy-preserving applications such as machine learning and data analytics. A critical performance bottleneck in comparison protocols is their preprocessing phase, primarily due to the high cost of generating the necessary correlated randomness. Recent frameworks introduce a passive, non-colluding dealer to accelerate preprocessing. However, two key issues still remain. First, existing dealer-assisted approaches treat the dealer as a drop-in replacement for conventional preprocessing without redesigning the comparison protocol to optimize the online phase. Second, most protocols are specialized for particular algebraic domains, adversary models, or party configurations, lacking broad generality. In this work, we present the first dealer-assisted $n$-party LTBits (Less-Than-Bits) and MSB (Most Significant Bit) extraction protocols over both $\mathbb{F}_p$ and $\mathbb{Z}_{2^k}$, achieving perfect security at the protocol level. By fully exploiting the dealer&#x27;s capability to generate rich correlated randomness, our $\mathbb{F}_p$ construction achieves constant-round online complexity and our $\mathbb{Z}_{2^k}$ construction achieves $O(\log_n k)$ rounds with tunable branching factor. All protocols are formulated as black-box constructions via an extended ABB model, ensuring portability across MPC backends and adversary models. Experimental results demonstrate $1.79\times$ to $19.4\times$ speedups over state-of-the-art MPC frameworks, highlighting the practicality of our protocols for comparison-intensive MPC applications.

  匹配依据：MPC: multi party computation

  </details>

- **Additions, Multiplications, and the Interaction In-Between: Optimizing MPC Protocols via Leveled Linear Secret Sharing (Full Version)**
  2026-02-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/368)
  Andreas Brüggemann, Thomas Schneider, Maximilian Stillger

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) enables distrusting parties in a distributed system to compute on their private inputs without compromising their privacy. For many secret-sharing-based approaches, including some of today&#x27;s most efficient MPC protocols, there is a pattern where two shared values are locally multiplied into some intermediate representation that is immediately and interactively translated back into sharings of the product. The intermediate representation is often still a full-fledged but different secret sharing scheme. This has been used to efficiently compute dot products by computing the sum of all intermediate products and then interactively translating only the sum instead of translating each individual product. Beyond that, the intermediate representation or secret sharing scheme has mostly been seen only as a necessary interim step, leaving most of its potential untapped. We change that by proposing the paradigm of leveled linear secret sharing, which allows dynamic switching between the original secret sharing and the previously only intermediate one more freely, while enabling arbitrary linear computations in any of the domains. Prior multiplications are split into a non-interactive multiplication that switches from one to the other secret sharing, and an interactive upgrade back to the original secret sharing domain. The upgrade now does not necessarily follow each multiplication immediately, but just needs to be placed somewhere before the next multiplication is computed, possibly upgrading the linear aggregation of many multiplications&#x27; results. We apply this idea to improve three-party computation on replicated sharings (CCS&#x27;16), n-party BGW-style protocols (STOC&#x27;88), and masked secret sharing protocols such as ABY2.0 (USENIX Security&#x27;21). We build a novel optimizer that optimally selects which gate of a circuit is evaluated in which domain. With that, we improve communication by 10-37% for many circuits. Furthermore, we implement our generalization for replicated sharing, measure run time improvements of mostly 10-26% in a LAN, and make a full implementation of the protocol and our novel optimizer publicly available.

  匹配依据：MPC: secret sharing, secure multiparty computation, three party computation

  </details>

- **UFO: Unlocking Ultra-Efficient Quantized Private Inference with Protocol and Algorithm Co-Optimization**
  2026-02-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.18758)
  Wenxuan Zeng, Chao Yang, Tianshi Xu, Bo Zhang, Changrui Ren, Jin Dong, Meng Li

  <details><summary>摘要 / Abstract</summary>

  Private convolutional neural network (CNN) inference based on secure two-party computation (2PC) suffers from high communication and latency overhead, especially from convolution layers. In this paper, we propose UFO, a quantized 2PC inference framework that jointly optimizes the 2PC protocols and quantization algorithm. UFO features a novel 2PC protocol that systematically combines the efficient Winograd convolution algorithm with quantization to improve inference efficiency. However, we observe that naively combining quantization and Winograd convolution faces the following challenges: 1) From the inference perspective, Winograd transformations introduce extensive additions and require frequent bit width conversions to avoid inference overflow, leading to non-negligible communication overhead; 2) From the training perspective, Winograd transformations introduce weight outliers that make quantization-aware training (QAT) difficult, resulting in inferior model accuracy. To address these challenges, we co-optimize both protocol and algorithm. 1) At the protocol level, we propose a series of graph-level optimizations for 2PC inference to minimize the communication. 2) At the algorithm level, we develop a mixed-precision QAT algorithm based on layer sensitivity to optimize model accuracy given communication constraints. To accommodate the outliers, we further introduce a 2PC-friendly bit re-weighting algorithm to increase the representation range without explicitly increasing bit widths. With extensive experiments, UFO demonstrates 11.7x, 3.6x, and 6.3x communication reduction with 1.29%, 1.16%, and 1.29% higher accuracy compared to state-of-the-art frameworks SiRNN, COINN, and CoPriv, respectively.

  匹配依据：MPC: secure two party computation

  </details>

- **PrivacyBench: Privacy Isn't Free in Hybrid Privacy-Preserving Vision Systems**
  2026-02-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.18900)
  Nnaemeka Obiefuna, Samuel Oyeneye, Similoluwa Odunaiya, Iremide Oyelaja, Steven Kolawole

  <details><summary>摘要 / Abstract</summary>

  Privacy preserving machine learning deployments in sensitive deep learning applications; from medical imaging to autonomous systems; increasingly require combining multiple techniques. Yet, practitioners lack systematic guidance to assess the synergistic and non-additive interactions of these hybrid configurations, relying instead on isolated technique analysis that misses critical system level interactions. We introduce PrivacyBench, a benchmarking framework that reveals striking failures in privacy technique combinations with severe deployment implications. Through systematic evaluation across ResNet18 and ViT models on medical datasets, we uncover that FL + DP combinations exhibit severe convergence failure, with accuracy dropping from 98% to 13% while compute costs and energy consumption substantially increase. In contrast, FL + SMPC maintains near-baseline performance with modest overhead. Our framework provides the first systematic platform for evaluating privacy-utility-cost trade-offs through automated YAML configuration, resource monitoring, and reproducible experimental protocols. PrivacyBench enables practitioners to identify problematic technique interactions before deployment, moving privacy-preserving computer vision from ad-hoc evaluation toward principled systems design. These findings demonstrate that privacy techniques cannot be composed arbitrarily and provide critical guidance for robust deployment in resource-constrained environments.

  匹配依据：MPC: smpc (context)

  </details>

- **Zebra: Arithmetic Garbled RAM for Large Words from DCR**
  2026-02-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/345)
  Tianyao Gu, Ashrujit Ghoshal, Elaine Shi

  <details><summary>摘要 / Abstract</summary>

  Garbled RAM is a promising technique for scaling secure two-party computation to large datasets. It features an efficient two-round protocol and supports each memory access with polylogarithmic overhead, thereby avoiding the prohibitive cost of RAM-to-circuit conversion. While earlier works on Garbled RAM primarily focused on establishing theoretical feasibility, recent research has increasingly emphasized concrete efficiency, culminating in constructions that achieve approximately $O(\lambda T W \log N)$ bandwidth cost (up to super-constant factors) for garbling a RAM with running time $T$, memory size $N$, and word size $W$. We ask whether it is possible to further improve the bandwidth cost of Garbled RAM. In contrast, the Garbled Circuit literature has developed a rich set of techniques that remove the bandwidth&#x27;s dependence on the security parameter $\lambda$, leading to constant-rate or even sub-constant-rate garbling schemes. However, no comparable methods are currently known for Garbled RAM. We propose a new garbling scheme for arithmetic RAM, called Zebra (short for ``Zero Exposure B-bounded Random Accesses&#x27;&#x27;). Specifically, we show that when the word size $W$ is suitably large, we can eliminate the $\lambda$-factor dependence and achieve a bandwidth cost of $O(T W \log N)$. In this sense, our scheme can also be viewed as the RAM analogue of ``constant-rate garbling for arithmetic circuits&#x27;&#x27;. Further, we show how to extend our techniques to support the garbling of boolean RAMs, achieving a bandwidth cost of $O(T W (\log N + \lambda))$ when the word size is suitably large. We implemented Zebra and released our code through open source. Our evaluation shows a $10.1\times$ concrete improvement in bandwidth and a $3.5\times$ improvement in end-to-end time relative to the state-of-the-art Garbled RAM schemes on a 256MB database with 4kB entries.

  匹配依据：MPC: garbled circuit, garbling scheme, garbling schemes, secure two party computation

  </details>

- **Efficient, UC-secure and Publicly Auditable MPC from OLE &amp; VOLE-in-the-head**
  2026-02-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/337)
  Carsten Baum, Chiara-Marie Zok

  <details><summary>摘要 / Abstract</summary>

  Secure Multiparty Computation (MPC) computes on private input data, but generally does not guarantee correctness of the output towards third parties. This property, also called public auditability, was first studied explicitly by Baum et al. (SCN 2014). Their work and its follow-ups generate a Non-Interactive Zero-Knowledge proof of correctness of the MPC outcome during the MPC protocol, ensuring validity of the output even if all parties are corrupted. In this work, we revisit and improve the MPC with Public Auditability blueprint. While the original work uses a version of the SPDZ MPC protocol with expensive lattice-based preprocessing, our construction combines any generic OLE-based preprocessing with a publicly verifiable somewhat linearly homomorphic commitment scheme from VOLE-in-the-head in a non-trivial way. Our commitment scheme relies solely on random oracle calls instead of previously used linearly homomorphic commitments based on structured Public-Key assumptions.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Statistically Secure Asynchronous MPC with Linear Communication and $\\mathcal{O}(n^5)$ Additive Overhead**
  2026-02-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/320)
  Xiaoyu Ji, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) allows distrusted parties to jointly evaluate a common function while keeping their inputs private. In this work, we focus on improving the communication complexity of information-theoretic asynchronous MPC with optimal resilience ($t &lt; n/3$). The current state-of-the-art work in this setting by Goyal, Liu-Zhang, and Song [Crypto’24] achieves amortized linear communication per gate with $\Omega(n^{14})$ elements additive overhead. In comparison, the best-known result in the synchronous setting by Goyal, Song, and Zhu [Crypto’20] achieves the amortized linear communication per gate with only $\mathcal{O}(n^{6})$ elements additive overhead, revealing a significant gap that we aim to close. This work closes this gap and goes further. We present the first statistically secure asynchronous MPC protocol achieving amortized linear communication per gate with only $\mathcal{O}(n^{5})$ elements additive overhead assuming a functionality for Agreement on Common Set (ACS). With the best-known instantiation for ACS, we obtain an asynchronous MPC protocol in the plain model with additive overhead $\mathcal{O}((\kappa+n)n^4\log\kappa)$ elements in expectation, where $\kappa$ is the security parameter. In the setting of statistical security with optimal resilience, this even surpasses the best synchronous result when $n\geq\sqrt{\kappa\log\kappa}$. Technically, our contributions include (i) a new protocol for generating Beaver triples with linear communication per triple and $\mathcal{O}(n^3)$ elements additive overhead assuming functionalities for generating random degree-$t$ Shamir sharings and ACS, and (ii) a new protocol for generating random degree-$t$ Shamir sharings with linear communication per sharing and $\mathcal{O}(n^{5})$ elements additive overhead assuming a functionality for ACS.

  匹配依据：MPC: secure multiparty computation

  </details>

- **New Techniques for Information-Theoretic Asynchronous MPC with Abort**
  2026-02-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/319)
  Xiaoyu Ji, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  We study the communication complexity of information-theoretic asynchronous multiparty computation (AMPC) with optimal resilience $n=3t+1$ and malicious security. In this setting, the only known result with linear communication per gate is due to Goyal, Liu-Zhang, and Song [CRYPTO ’24]. However, their construction incurs a large communication overhead of $\Omega(n^{14})$ elements that is independent of the circuit size, rendering their result only of theoretical interest. By additionally assuming a random oracle, Bandarupalli et al. [CCS ’25] reduce the communication overhead to $\mathcal{O}(n^3)$ while maintaining the linear communication per gate, at the cost of only achieving malicious security with fairness. In this work, we remove the random oracle assumption and design an information-theoretic AMPC protocol that achieves malicious security with abort. The communication complexity of our construction is $\mathcal{O}(|C|n + Dn^2 + n^3)$ field elements for an arithmetic circuit of size $|C|$ and depth $D$, assuming a functionality for Agreement on Common Set (ACS). Our main technical contribution is a novel verification mechanism with the following guarantee: whenever verification succeeds, there exists a subset of at least $t+1$ honest parties whose local computations are mutually consistent, and the final output is correct with respect to their computation. In contrast to prior approaches that require all honest parties to hold consistent states and execute identical computations before verification, our mechanism tolerates inconsistencies among honest parties while still ensuring that the verified computation is correct for at least one such honest subset, if the verification succeeds.

  匹配依据：MPC: multiparty computation

  </details>

- **Multi-key Fully Homomorphic Encryption with Non-Interactive Setup in the Plain Model**
  2026-02-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/322)
  Seonhong Min, Jeongeun Park, Yongsoo Song

  <details><summary>摘要 / Abstract</summary>

  Multi-key fully homomorphic encryption (MKFHE) enables computation over encrypted data under multiple different keys. Constructing MKFHE without any trusted or interactive setup remains an open problem. In the context of MKFHE, a trusted setup is often assumed to mean the use of a common random string (CRS). In this paper, we present the first MKFHE scheme in the plain model (i.e., without any trusted or interactive setup) based on the RLWE assumption. Specifically, we construct a multi-key somewhat homomorphic encryption based on the RLWE assumption and extend it to a multi-key variant of the Gentry-Sahai-Waters (GSW) scheme with a circular security assumption. Our design yields a 2-round multi-party computation (MPC) in the plain model against semi-honest adversaries. Moreover, it can be applied to transform existing FHE schemes that rely on RGSW in their construction into a multi-key variant. We also provide concrete conversions for widely-used FHE schemes, including BGV, BFV, CKKS, FHEW, TFHE, and Carousel. Finally, we implement our scheme and present experimental results for the expansion algorithm from a single-key ciphertext to a multi-key ciphertext and the multi-key homomorphic multiplication algorithm.

  匹配依据：MPC: multi party computation

  </details>

- **FLiPD: Privacy-Preserving Federated Learning via Multi-Party Computation and Differential Privacy**
  2026-02-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/324)
  Gowri R Chandran, Melek Önen, Thomas Schneider

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) is a collaborative Machine Learning (ML) process where clients locally train an ML model on their private inputs, and send it to a server that aggregates the local model updates to obtain a global model update. FL is widely used in applications where the training data is distributed among several clients, e.g., for next word prediction in Google keyboard (Gboard). Nevertheless, FL faces several challenges concerning privacy and security. 1) Client privacy needs to be preserved by employing defenses against inference attacks using Secure Aggregation (SA) protocols. 2) The security of the model has to be defended against poisoning and backdoor attacks, e.g., by using clustering or filtering algorithms. In this work, we present FLiPD, an optimised SA protocol for FL that protects against several attacks via a combination of Multi-Party Computation (MPC) and Differential Privacy (DP) mechanisms. We provide defenses against both inference and backdoor attacks. Moreover, by applying distributed DP noise generation, we show that our protocol is secure even when the majority of the clients collude with a server. As opposed to existing solutions, in FLiPD, the client-server communication cost is essentially the same as in unprotected FL, which sends plaintext updates. Furthermore, the server-server communication cost is slightly lower (by 11%) than the state-of-the-art Prio+ (Addanki et al., SCN&#x27;22). In addition, we examine the accuracy of FLiPD both in the presence and absence of attacks. We achieve 87% accuracy for a Linear Regression model trained on the HAR dataset, and 90% for a Convolution Neural Network trained on the MNIST dataset.

  匹配依据：MPC: multi party computation

  </details>

- **Quantum One Time Programs: Less Assumptions, More Feasibility and One Message 2PC**
  2026-02-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/300)
  Prabhanjan Ananth, Divyanshu Bhardwaj

  <details><summary>摘要 / Abstract</summary>

  Quantum one-time programs, introduced by Broadbent, Gutowski, and Stebila [CRYPTO 2013], is a compiler that takes as input a program $f$ and converts it into a quantum state $\sigma_f$ such that given $\sigma_f$, it is possible to only obtain the output of $f$ on a single input. Our goal is to investigate the class of functionalities for which we can design one-time programs in the plain model. We show the following: 1. We show that, assuming learning with errors, one-time programs for (randomized) pseudorandom functionalities exist in the plain model. In contrast, the result by Gupte, Liu, Raizes, Roberts, and Vaikuntanathan [STOC 2025] relied upon indistinguishability obfuscation. 2. We show that, assuming indistinguishability obfuscation, one-time programs for any class of randomized functionalities exist in the plain model, as long as the class of functionalities satisfy a natural security notion called constrained security. Additionally, we give constructions of one-time encryption and one-time message authentication codes based on learning with errors. Finally, we show that a novel variant of one-time programs imply one-message secure two-party computation protocols for non-trivial functionalities in the CRS model.

  匹配依据：MPC: secure two party computation

  </details>

- **Non Interactive MPC, (Quantumly) Revisited**
  2026-02-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/302)
  Prabhanjan Ananth, Divyanshu Bhardwaj, Aparna Gupte

  <details><summary>摘要 / Abstract</summary>

  Classical non-interactive secure computation, despite being extensively studied, suffers from an inherent barrier: adversaries can learn the entire residual function via resetting attacks. We investigate whether quantum resources can circumvent this barrier and restrict adversarial leakage. Our results are as follows: 1. $\textbf{Definitions}$: We introduce new security definitions for the one-message MPC and 2PC settings that restrict the amount of adversarial leakage compared to prior classical definitions. 2. $\textbf{MPC}$: There exist information-theoretically secure one-message multi-party computation protocols in the oracle model in both the quantum pre-processing and classical pre-processing settings. 3. $\textbf{2PC}$: There exist semi-honest secure one-message two-party computation for (randomized) pseudorandom functionalities in the plain model based on LWE and maliciously secure one-message two-party computation for (randomized) constrained functionalities in the CRS model based on iO. Prior work by [Gupte, Liu, Raizes, Roberts and, Vaikuntanathan STOC 2025] achieved semi-honest security based on iO. Our results demonstrate the power of quantum information to circumvent barriers in classical secure computation.

  匹配依据：MPC: multi party computation, secure computation, two party computation

  </details>

- **Malicious Security Comes Free in SPDZ**
  2026-02-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/283)
  Junru Li, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  We study the communication complexity of SPDZ-type MPC protocols in the dishonest majority setting with maximum corruption, where $t=n-1$ out of $n$ parties can be corrupted. In the semi-honest setting, the state-of-the-art SPDZ protocol achieves an amortized communication cost of $4n$ field elements per multiplication gate, assuming a pseudorandom correlation generator (PCG) that prepares random Beaver triples silently in the offline phase. However, achieving security against malicious adversaries typically incurs a substantial overhead. Existing works either blow up the communication by incurring $10n$ field elements per gate or an additional overhead of $O(\sqrt{|C|}\cdot n^3)$, or additionally require an additively homomorphic encryption scheme. In this work, we construct a maliciously secure SPDZ-type protocol with the same amortized communication complexity as the semi-honest variant, i.e., $4n$ field elements per multiplication gate, assuming a PCG for \emph{tensor-product} correlations. We note that the tensor-product correlations come free in communication as by-products from almost all existing constructions of PCGs for random Beaver triples, although additional local computation is required. These by-products allow us to construct an efficient preprocessing phase and a recursive check protocol, which enables an online evaluation of the circuit without authenticating all the wire values. The recursive check requires sublinear communication in $|C|$, though it incurs an $O(k)$ overhead on the online computational cost compared to the semi-honest baseline.

  匹配依据：MPC: mpc (context)

  </details>

- **Weighted Cryptography with Weight-Independent Complexity**
  2026-02-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/273)
  Aarushi Goel, Swagata Sasmal, Mingyuan Wang

  <details><summary>摘要 / Abstract</summary>

  Cryptographic primitives involving multiple participants, such as secure multiparty computation (MPC), threshold signatures, and threshold encryption, are typically designed under the assumption that at least a threshold number of participants remain honest and non-colluding. However, many real-world applications require more expressive access structures beyond simple thresholds. A prominent example is the weighted threshold access structure, where each party is assigned a weight and security holds as long as the total weight of corrupted parties does not exceed a specified threshold. Despite the practical relevance of such access structures, our understanding of efficient constructions supporting them remains limited. For instance, existing approaches for weighted MPC and weighted threshold encryption incur costs that scale with the total assigned weights to all parties or rely on non-black-box use of cryptography. In this work, we present the first black-box constructions of the following weighted cryptosystems with weight-independent complexity in the trusted setup model: (i) a weighted MPC protocol with guaranteed output delivery, (ii) a semi-honest weighted threshold encryption scheme and (iii) a semi-honest weighted threshold Schnorr signature scheme. At the heart of our constructions is a new succinct computational secret sharing scheme with linear homomorphism for weighted threshold access structures. We provide two concrete instantiations of this primitive, based on the Decisional Composite Residuosity (DCR) assumption and the Learning With Errors (LWE) assumption, respectively. Furthermore, our constructions extend to any general access structure that can be represented efficiently as a monotone Boolean circuit.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **LRD-MPC: Efficient MPC Inference through Low-rank Decomposition**
  2026-02-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.14397)
  Tingting Tang, Yongqin Wang, Murali Annavaram

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-party Computation (MPC) enables untrusted parties to jointly compute a function without revealing their inputs. Its application to machine learning (ML) has gained significant attention, particularly for secure inference services deployed across multiple cloud virtual machines (VMs), where each VM acts as an MPC party. Model providers secret-share model weights, and users secret-share inputs, ensuring that each server operates only on random shares. While MPC provides strong cryptographic guarantees, it incurs substantial computational and communication overhead. Deep neural networks rely heavily on convolutional and fully connected layers, which require costly matrix multiplications in MPC. To reduce this cost, we propose leveraging low-rank decomposition (LRD) for linear layers, replacing one large matrix multiplication with two smaller ones. Each matrix multiplication in MPC incurs a round of communication, meaning decomposing one matrix multiplication into two leads to an additional communication round. Second, the added matrix multiplication requires an additional truncation step to maintain numerical precision. Since truncation itself requires communication and computation, these overheads can offset the gains from decomposition. To address this, we introduce two complementary optimizations: truncation skipping and efficient linear layer concatenation. Truncation skipping removes the extra truncation induced by LRD, while linear layer concatenation pipelines operations to hide the additional communication round. Together, these techniques mitigate the main overheads of LRD in MPC and improve overall efficiency. Our approach is broadly applicable across MPC protocols. Experiments show up to 25% speedup in n-PC and 33% in 3-PC protocols over full-rank baselines, along with up to 52% GPU energy savings and 88% reduction in offline-phase latency.

  匹配依据：MPC: secure multi party computation

  </details>

- **Constructions of linear codes from vectorial plateaued functions and their subfield codes with applications to quantum CSS codes**
  2026-02-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.14832)
  Virginio Fratianni, Sihem Mesnager

  <details><summary>摘要 / Abstract</summary>

  Linear codes over finite fields parameterized by functions have proven to be a powerful tool in coding theory, yielding optimal and few-weight codes with significant applications in secret sharing, authentication codes, and association schemes. In 2023, Xu et al. introduced a construction framework for 3-dimensional linear codes parameterized by two functions, which has demonstrated considerable success in generating infinite families of optimal linear codes. Motivated by this approach, we propose a construction that extends the framework to three functions, thereby enhancing the flexibility of the parameters. Additionally, we introduce a vectorial setting by allowing vector-valued functions, expanding the construction space and the set of achievable structural properties. We analyze both scalar and vectorial frameworks, employing Bent and s-Plateaued functions, including Almost Bent, to define the code generators. By exploiting the properties of the Walsh transform, we determine the explicit parameters and weight distributions of these codes and their punctured versions. A key result of this study is that the constructed codes have few weights, and their duals are distance and dimensionally optimal with respect to both the Sphere Packing and Griesmer bounds. Furthermore, we establish a theoretical connection between our vectorial approach and the classical first generic construction of linear codes, providing sufficient conditions for the resulting codes to be minimal and self-orthogonal. Finally, we investigate applications to quantum coding theory within the Calderbank-Shor-Steane framework.

  匹配依据：MPC: secret sharing

  </details>

- **Beyond the Linear Barrier: Secret Sharing for Evolving (Weighted) Threshold Access Structures with Poly-logarithmic Share Size**
  2026-02-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/267)
  Danilo Francati, Sara Giammusso, Daniele Venturi

  <details><summary>摘要 / Abstract</summary>

  Evolving secret sharing allows a dealer to share a secret message between a growing number of $n$ parties. Crucially, the dealer does not know an upper bound on $n$, neither it knows the access structure before party $n$ arrives; furthermore, the dealer is not allowed to update the shares of old parties. We construct new secret sharing schemes for so-called evolving (weighted) threshold access, in which the arrival of party $n$ determines the number of parties $t_n \le n$ that are required in order to reconstruct the secret. We also consider the more general case in which party $n$ has associated a weight $w_n$ with logarithmic size, and the authorized subsets of parties are those for which the sum of the corresponding weights exceeds the current threshold $t_n$. In particular, we obtain: - A secret sharing scheme for evolving threshold access structures with adaptive privacy in the plain model, and with share size $\mathsf{poly}(\lambda,\log n)$. This construction requires one-way functions (OWFs) and indistinguishability obfuscation (iO) for Turing machines. - A secret sharing scheme for evolving weighted threshold access structures with adaptive privacy in the plain model, and with share size $\mathsf{poly}(\lambda,\log W_n)$ where $W_n$ is the sum of the weights up to party $n$. This construction requires OWFs and iO for Turing machines, and additionally assumes that the weights are fixed (i.e., cannot change over time). - A secret sharing scheme for evolving weighted threshold access structures with static privacy in the plain model, and with share size $\mathsf{poly}(\lambda,\log W_n)$. This construction allows the weight of old parties to change over time, but it requires somewhere statistically binding hash functions and achieves only static privacy. Previous constructions of secret sharing schemes for evolving (weighted) threshold access structures achieved (much worse) share sizes linear in $W_n$ (and in the security parameter) and, when considering adaptive privacy, they require the random oracle model.

  匹配依据：MPC: secret sharing

  </details>

- **Logarithmic-Depth Pseudorandom Functions from Well-Founded Code-Based Assumptions**
  2026-02-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/261)
  Youlong Ding, Aayush Jain, Ilan Komargodski

  <details><summary>摘要 / Abstract</summary>

  We give the first $\mathsf{NC}^1$-computable Pseudorandom Function (PRF) constructions from well-founded (non-ad-hoc) code-based assumptions. Specifically, we give two constructions based on two different classical variants of the learning parity with noise (LPN) assumption: (1) An $\mathsf{NC}^1$-computable PRF from hardness of Sparse-LPN [Alekhnovich, FOCS~&#x27;03] (with respect to a sublinear-depth expander graph family). This PRF is also key-homomorphic. (2) An $\mathsf{NC}^1$-computable PRF from hardness of Ring-LPN [Heyse et al., FSE~&#x27;12]. Both of these assumptions have been studied for many years in cryptography and average-case complexity. Ring-LPN has been used in the context of silent preprocessing for MPC and has a stable cryptanalysis. The study of counterexamples for Sparse-LPN is an active area of research. Notably, within the range of parameters that we need, none of these assumptions is known to imply collision-resistant hashing, and the first is not known to imply public-key encryption. Prior constructions of code-based PRFs (let alone key-homomorphic) are either super-logarithmic depth, or rely on newly introduced assumptions. As a bonus, we give a similar result relying on the \emph{classical} LPN assumption, albeit with quasi-polynomial hardness: -A key-homomorphic $\mathsf{NC}^1$-computable PRF from quasi-polynomial hardness of the classical LPN [Blum et al., CRYPTO~&#x27;93]. Technically, all of our results are obtained via a refinement and substantial extension of the recent ideas of [Ding, Jain, and Komargodski, STOC~&#x27;25].

  匹配依据：MPC: mpc (context)

  </details>

- **Fuzzy Private Set Intersection under Density-Bounded Assumptions**
  2026-02-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/262)
  Seunghun Paik, Jae Hong Seo

  <details><summary>摘要 / Abstract</summary>

  This paper presents a new fuzzy private set intersection (FPSI) protocol, a two-party protocol to securely identify similar items across private sets. Our design departs from the prevailing separation-based paradigm---e.g., ``apart by $2\delta$&#x27;&#x27; or the disjoint projection assumption---which either incurs exponential overhead in dimensionality or requires high dimensionality to justify the assumption. Instead, we address this tension by explicitly allowing collisions within $\delta$-balls, but requiring that their multiplicity be bounded per axis. We formalize this new structural property as $C$-max collision. We theoretically analyze its plausibility on several common distributions, e.g., the uniform distribution, and real datasets, and provide an efficient algorithm to verify this assumption. Under the $C$-max collision property, we propose an efficient FPSI protocol for $\ell_{\infty}$ distance that supports both low- and high-dimensional regimes. Our construction is based on a novel abstraction that views FPSI as an oblivious intersection of membership tags, which natively handles axis-wise matching multiplicity. We capture its requirements through a new functionality called oblivious selected set intersection, along with its instantiation based on symmetric key techniques. Assuming the $C$-max collision property on the receiver&#x27;s set, our protocol achieves computation/communication complexities scaling linearly with both parties&#x27; set sizes for a fixed $C$. We implement our protocol and conduct extensive evaluation. While a direct comparison is infeasible, ours achieves online efficiency comparable to state-of-the-art separation-based FPSI protocols in both low- and high-dimensional regimes.

  匹配依据：MPC: private set intersection

  </details>

- **On Compressing Linearly Shared Correlations**
  2026-02-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/255)
  Geoffroy Couteau, Alexander Koch, Nikolas Melissaris, Peter Scholl, Sacha Servan-Schreiber, Xiaxi Ye

  <details><summary>摘要 / Abstract</summary>

  Compressing correlated randomness is a key component of secure computation protocols in the silent preprocessing model and has received significant attention in recent years. Most existing constructions target additive correlations, where the parties receive additive shares of a relation. Beyond additive correlations, much less is known: more general linear correlations can be compressed using pseudorandom secret sharing, generic constructions for richer linear-output correlations can be obtained by combining LWE-based multiparty HSS with share conversion, in regimes where the share-conversion overhead is efficient, and general correlations can be compressed using indistinguishability obfuscation. In this work, we advance the study of compression for useful forms of correlated randomness beyond additive output sharing (concretely, linear-output correlations, together with a constrained variant capturing random permutations), without resorting to $iO$, introducing new techniques, new feasibility results, and relying on more diverse assumptions. We provide several constructions for pseudorandom correlation generators and functions using direct HSS- and LPN/MQ-based techniques. Concretely, we focus on two types of correlations in this work. First, we introduce pseudorandom permutation functions, where each party obtains a portion of a pseudorandom permutation $\pi$ over the set $\set{1,\dots, n}$, such that a single party learns nothing about the full permutation beyond its own output. We give a three-party construction of a pseudorandom correlation function (PCF) for permutations from homomorphic secret sharing satisfying a special share programmability property. This construction can be instantiated from a variety of standard assumptions and can even be concretely efficient (generating pseudorandom permutations in a fraction of a second). We describe two applications of pseudorandom permutation functions: one in anonymous broadcast and the other in single secret leader election. Second, we introduce pseudorandom correlation generators for classical correlations (such as Beaver triples) where additive secret sharing is replaced with threshold secret sharing. We obtain pseudorandom correlation functions for degree-$1$ Shamir shares of $\mathsf{NC}^1$ correlations from a variety of standard assumptions. We also introduce two new PCG constructions for threshold-shared constant-degree correlations in the regimes where either the privacy threshold $t$ or $n-t$ is a constant. These constructions rely on the conjunction of the LPN and MQ assumptions.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **When Trying to Catch Cheaters Breaks the MPC: Breaking and Fixing Delayed Consistency Checks in Trident, Fantastic Four, SWIFT, and Quad (Full Version)**
  2026-02-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/234)
  Andreas Brüggemann, Thomas Schneider

  <details><summary>摘要 / Abstract</summary>

  Actively secure multi-party computation in the honest-majority setting often relies on multiple parties computing the same message to be sent. This additional redundancy allows to detect when a party deviates from the protocol. Many works utilize this for efficient protocol design, with some protocols delaying and batching consistency checks to further boost efficiency. In this paper, we show multiple cases where such batched consistency checks render the protocols insecure. Our concrete attacks derive additional knowledge from the batched consistency checks, reconstructing values on intermediate wires. Specifically, we show concrete attacks on Trident (NDSS&#x27;20), Fantastic Four (USENIX Security&#x27;21) including its implementation in the popular MP-SPDZ framework (CCS&#x27;20), and Quad (PoPETS&#x27;25). Furthermore, we find how an imprecise specification of SWIFT (USENIX Security&#x27;21) can enable a similar attack and reveal a gap in their security proof. Finally, we propose a fix for all protocols with a small performance overhead. Our provably secure fix uses a generic, joint consistency check that replaces the former, insecure consistency checks.

  匹配依据：MPC: secure multi party computation

  </details>

- **Sharing a Secret Anamorphically: Secret Shares Dressed Up as Signatures**
  2026-02-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/236)
  Gennaro Avitabile, Vincenzo Botta, Daniele Friolo

  <details><summary>摘要 / Abstract</summary>

  Anamorphic Encryption (Persiano, Phan and Yung, Eurocrypt &#x27;22) allows private communication in a challenging setting where encryption is severely controlled by a central authority (henceforth the dictator) who can demand the users to surrender their secret keys. Anamorphic Signatures (AS) (Kutylowski, Persiano, Phan, Yung, Zawada, Crypto &#x27;23) face the even more restrictive world where only authentication is allowed but users still want to send secret messages despite the repressive control of the dictator holding their signing key. Several constructions have been proposed so far, but they all come with some limitations. We propose a new flexible setting where digital signatures are used to covertly embed secret shares which $t$ out of $N$ designated receivers can combine to recover a covert secret. We formalize this new primitive called Anamorphic Secret Sharing Signatures (ASSS) together with new robustness, forward secrecy, and private unforgeability notions and we give a construction for Schnorr-like signatures overcoming the limitations of previous constructions. ASSS additionally imply (regular single-receiver) AS, but two signatures (instead of one) are needed to recover the covert message.

  匹配依据：MPC: secret sharing

  </details>

- **ECHO: Efficient Covertly-Secure Three-party Computation with Applications to Private Machine Learning**
  2026-02-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/216)
  Yufei Duan, Yun Li, Zhicong Huang, Cheng Hong, Tao Wei, Chao Zhang

  <details><summary>摘要 / Abstract</summary>

  Secure three-party computation with an honest majority is among the most efficient secure computation settings and is widely used in practice. However, achieving malicious security incurs significant overhead, often an order of magnitude higher than semi-honest protocols. Covert security provides a security–efficiency trade-off by detecting malicious behavior with a certain probability (e.g., $50\%$), deterring rational adversaries. Existing covert protocols mainly target two-party or dishonest-majority settings, with little work on efficient honest-majority three-party solutions. We present $\mathsf{ECHO}$, a family of concretely efficient protocols for covertly secure honest-majority three-party computation. We explore the design space of cheating detection and identification, and develop optimized protocols for both arithmetic and Boolean circuits, targeting different performance goals such as low latency and reduced communication. For arithmetic circuits over rings, our asymmetric-MAC-based protocol achieves an online phase only $1.26\times$ slower than the semi-honest baseline and over $5.59\times$ faster than malicious security. For Boolean circuits, our method improves over the best malicious protocol by $5\times$. We also applied $\mathsf{ECHO}$ on practical PPML tasks. $\mathsf{ECHO}$ approaches semi-honest performance while providing up to $8\times$ speedup over malicious security.

  匹配依据：MPC: secure computation, secure three party computation, three party computation

  </details>

- **Cavern: Efficient Honest-Majority Maliciously Secure $(2+1)$-PC for $\\mathbb{Z}\_{2^n}$ via DPF**
  2026-02-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/214)
  Yang Liu, Liang Feng Zhang

  <details><summary>摘要 / Abstract</summary>

  We introduce Cavern, a new maliciously secure $(2+1)$-PC protocol for efficient piecewise polynomial (i.e., spline) evaluation on additively secret shared inputs over the ring $\mathbb{Z}_{2^n}$ in the preprocessing model, where parties obtain input-independent correlated randomness in an offline phase, which they then use to run an efficient protocol in the input-dependent online phase. This $(2+1)$ party structure can alternatively be instantiated between two parties with the aid of a (possibly untrusted) dealer. At the technical level, we introduce a new primitive called verifiable incremental distributed point function (VIDPF) and build on a novel combination of the VIDPF and authenticated secret sharing, providing an efficient method to detect the malicious behavior of the dealer or one of the parties. We implement and benchmark our protocol against the state-of-the-art semi-honest protocol Grotto (CCS 2023), and the trusted-dealer-based maliciously secure 2PC protocol Shark (S&amp;P 2025). The results indicate that Cavern only imposes a constant factor overhead on the top of Grotto and Shark, while providing stronger security guarantees.

  匹配依据：MPC: secret sharing

  </details>

- **The Finite Geometry of Breaking Quantum Secrets**
  2026-02-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.08410)
  Péter Lévay, Metod Saniga

  <details><summary>摘要 / Abstract</summary>

  Using a finite geometric framework for studying the pentagon and heptagon codes we show that the concepts of quantum secret sharing and contextuality can be studied in a nice and unified manner. The basic idea is a careful study of the respective $2+3$ and $3+4$ tensorial factorizations of the elements of the stabilizer groups of these codes. It is demonstrated in detail how finite geometric structures entailing a specific three-qubit (resp. four-qubit) embedding of binary symplectic polar spaces of rank two (resp. three), corresponding to these factorizations, govern issues of contextuality and entanglement needed for a geometric understanding of quantum secret sharing. Using these results for the $(3,5)$ and $(4,7)$ threshold schemes explicit secret breaking protocols are derived. Our results hint at a novel geometric way of looking at contextual configurations.

  匹配依据：MPC: secret sharing

  </details>

- **MPSpeed: Implementing and Optimizing MPC-in-the-Head Digital Signatures in Hardware**
  2026-02-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/206)
  Stelios Manasidis, Quinten Norga, Suparna Kundu, Ingrid Verbauwhede

  <details><summary>摘要 / Abstract</summary>

  The Multi-Party Computation (MPC)-in-the-Head (MPCitH) framework enables the construction of post-quantum Digital Signature Algorithms (DSAs), offering competitive public key sizes. However, this comes at a cost of high computational complexity, resulting in high signature generation and verification times. In this work, we propose a compact and efficient hardware accelerator for Mirath, an MPCitH-based DSA and candidate in the ongoing NIST PQC standardization effort. We propose a series of algorithmic and hardware-level optimizations, focusing on Mirath&#x27;s most critical operations: GGM tree-based polynomial commitments and MPC arithmetic. Firstly, we observe Mirath greatly relies on symmetric primitives (SHA3 &amp; AES) during the GGM tree expansion and typically requires a large amount of memory to store the derived tree nodes. We propose an on-the-fly scheduling for generating and computing the GGM tree, such that a minimal amount of GGM tree nodes are stored in memory and their computations can be performed in parallel. Our methodology enables temporarily storing a minimal (and configurable) set of parent nodes in local buffers, from which the low-level tree nodes can be efficiently derived instead of repeatedly doing so from the root seed. This is achieved through a novel, hardware-friendly tree node indexing scheme, which enables efficient traversal through GGM tree nodes using only left and right shifts to find their closest previously computed ancestor. Secondly, we analyze the MPC arithmetic in Mirath and propose massively parallel and yet area-efficient arithmetic units, capable of exploiting algorithm-level parallelism in the MPCitH operations. This is achieved by analyzing Mirath&#x27;s proposed parameter sets and identifying the most hardware-friendly parameters, for which we design highly fine-tuned modules. Finally, we implement our unified design, which supports all Mirath operations, on an Artix-7 FPGA and compare its performance against Mirath&#x27;s AVX2 optimized implementation and state-of-the-art PQC DSA hardware implementations. Compared to an implementation of the MPCitH-based SDitH scheme (TCHES 2024), we reduce on-chip BRAM by up to $81.6\%$ and improve the area-time-product by a factor of $52.7\times$ to $64.8\times$. Overall, we demonstrate that modern MPCitH constructions can be significantly accelerated in hardware through a combination of algorithmic, architectural and low-level hardware optimizations, in line with real-world performance requirements.

  匹配依据：MPC: multi party computation

  </details>

- **CryptoGen: Secure Transformer Generation with Encrypted KV-Cache Reuse**
  2026-02-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.08798)
  Hedong Zhang, Neusha Javidnia, Shweta Pardeshi, Qian Lou, Farinaz Koushanfar

  <details><summary>摘要 / Abstract</summary>

  The widespread deployment of cloud-hosted generative models raises a fundamental challenge: enabling efficient autoregressive generation while preserving the privacy of both user prompts and model parameters in untrusted environments. We address this challenge in a client-server setting where an untrusted server hosts an autoregressive Transformer and the client requires cryptographic protection for both inputs and inference. We present CryptoGen, the first system to enable scalable privacy-preserving neural generation with persistent encrypted key-value (KV) cache reuse. Discriminative-task secure inference systems incur quadratic latency and memory growth when adapted to autoregressive decoding due to the lack of native encrypted KV-cache support. In contrast, CryptoGen achieves near-linear scaling by securely reusing and updating encrypted KV caches throughout generation. CryptoGen integrates homomorphic encryption and secret sharing to support both prefilling and generation. Key techniques include a unified encrypted KV-cache framework, heterogeneous SIMD encodings for different phases, optimized cipher-cipher matrix-matrix and matrix-vector operations, and efficient noise refresh and ciphertext concatenation mechanisms. Evaluation on generative Transformer models trained on WikiText-2, PTB, and LAMBADA shows that for input lengths of 128-512 tokens, CryptoGen achieves 4.4x-7.6x lower per-token latency than state-of-the-art discriminative secure inference systems, while maintaining near-linear latency and memory scaling, with advantages increasing for longer sequences. CryptoGen is released as an open-source library.

  匹配依据：MPC: secret sharing

  </details>

- **Network function computation with vector linear target function and security function**
  2026-02-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.07316)
  Min Xu, Qian Chen, Gennian Ge

  <details><summary>摘要 / Abstract</summary>

  In this paper, we study the problem of securely computing a function over a network, where both the target function and the security function are vector linear. The network is modeled as a directed acyclic graph. A sink node wishes to compute a function of messages generated by multiple distributed sources, while an eavesdropper can access exactly one wiretap set from a given collection. The eavesdropper must be prevented from obtaining any information about a specified security function of the source messages. The secure computing capacity is the maximum average number of times that the target function can be securely computed with zero error at the sink node with the given collection of wiretap sets and security function for one use of the network. We establish two upper bounds on this capacity, which hold for arbitrary network topologies and for any vector linear target and security functions. These bounds generalize existing results and also lead to a new upper bound when the target function is the sum over a finite field. For the lower bound, when the target function is the sum, we extend an existing method, which transforms a non-secure network code into a secure one, to the case where the security function is vector linear. Furthermore, for a particular class of networks and a vector linear target function, we characterize the required properties of the global encoding matrix to construct a secure vector linear network code.

  匹配依据：MPC: secure computing

  </details>

- **Faster Pseudorandom Correlation Generators via Walsh-Hadamard Transform**
  2026-02-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/196)
  Zhe Li, Hongqing Liu, Chaoping Xing, Yizhou Yao, Chen Yuan

  <details><summary>摘要 / Abstract</summary>

  The past few years have witnessed the growing importance of pseudorandom correlation generators (PCGs) for generating correlated randomness with sublinear communication. To date, quasi-linear time PCGs for oblivious linear evaluation (OLE) over arbitrary finite fields have been constructed under either Ring-LPN or Quasi-Abelian syndrome decoding (QA-SD) assumptions, with a throughput of millions of OLEs per second demonstrated, in particular, for binary field. However, many modern MPC protocols deal with large prime fields, in which existing PCGs suffer from a significant efficiency gap due to a quasi-linear number of {\em multiplications} involved in FFT (Fast Fourier Transform) algorithms. Moreover, FFT typically relies on FFT-friendly fields that contain large smooth multiplicative subgroups, and therefore are not well suited to popular fields, such as Mersenne prime fields. In this work, we close the gap by leveraging the well-known Walsh-Hadamard transform (WHT) in the context of QA-SD based PCGs. Although WHT is still a quasi-linear time algorithm as normal FFTs, no multiplication is needed — addition and subtraction suffice. Since multiplications over a prime field $\mathbb{F}_p$ typically incur an $O(\log{p})$ overhead over additions, our scheme that avoids a large number of multiplications perfectly fits the large prime field setting. Experimental results show that WHT is at least one magnitude faster than FFT over a $64$-bit smooth prime field. Consequently, our PCG achieves $27,000$ OLE per second over a $64$-bit prime field. This is the first full implementation of PCG for OLE over arbitrary large prime fields that we are aware of. We then build PCG for vector-OLE over arbitrary large prime fields from QA-SD assumptions, and fully implement it using the $\mathsf{libOTe}$ library. We achieve a throughput of over $5$ million vector-OLEs per second over a $64$-bit prime field, roughly four times faster than state-of-the-art PCGs from either expand-accumulate (EA) codes (Boyle et al., CRYPTO 2022), or expand-convolute (EC) codes (Raghuraman et al., CRYPTO 2023).

  匹配依据：MPC: mpc (context)

  </details>

- **Private Sum Computation: Trade-Offs between Communication, Randomness, and Privacy**
  2026-02-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.06238)
  Remi A. Chou, Joerg Kliewer, Aylin Yener

  <details><summary>摘要 / Abstract</summary>

  Consider multiple users and a fusion center. Each user possesses a sequence of bits and can communicate with the fusion center through a one-way public channel. The fusion center&#x27;s task is to compute the sum of all the sequences under the privacy requirement that a set of colluding users, along with the fusion center, cannot gain more than a predetermined amount $δ$ of information, measured through mutual information, about the sequences of other users. Our first contribution is to characterize the minimum amount of necessary communication between the users and the fusion center, as well as the minimum amount of necessary randomness at the users. Our second contribution is to establish a connection between private sum computation and secret sharing by showing that secret sharing is necessary to generate the local randomness needed for private sum computation, and prove that it holds true for any $δ\geq 0$.

  匹配依据：MPC: secret sharing

  </details>

- **Towards Public Tracing: Collaborative Traceable Secret Sharing**
  2026-02-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/181)
  Pousali Dey, Rittwik Hajra, Subha Kar, Soumit Pal

  <details><summary>摘要 / Abstract</summary>

  In a $(t,n)$-threshold secret sharing scheme, secrecy holds as long as fewer than $t$ servers collude. If $f &lt; t$ parties are corrupt and they sell their shares, there is no mechanism to hold them accountable in classical secret sharing schemes. Goyal–Song–Srinivasan [CRYPTO&#x27;21] introduced Traceable Secret Sharing ($\mathsf{TSS}$) and later Boneh–Partap–Rotem [CRYPTO&#x27;24] made it practical: $f&lt;t$ corrupt servers produce a reconstruction box $\mathcal{R}$ that, given $t-f$ extra shares, outputs the secret. The task is to trace $\mathcal{R}$ back to the corrupted servers, given black-box access to $\mathcal{R}$. Prior works on $\mathsf{TSS}$ rely on a designated tracer with private trace keys for tracing and/or verification. We remove the dependence on any designated tracer and propose Collaborative Traceable Secret Sharing ($\mathsf{CTSS}$), which eliminates the private trace key and the private verification key. Instead, tracing requires collaboration from a threshold number of parties, and verification is fully public. We define the $\mathsf{CTSS}$ framework, along with its security notions, and present two efficient collaborative traceable secret sharing schemes based on the classical Shamir and Blakley schemes. Both achieve secrecy, traceability, and non-imputability, with minimal share size overhead and polynomial-time tracing effectively eliminating the need for a designated tracing authority.

  匹配依据：MPC: secret sharing

  </details>

- **Nudge: A Private Recommendations Engine**
  2026-02-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/179)
  Alexandra Henzinger, Emma Dauterman, Henry Corrigan-Gibbs, Dan Boneh

  <details><summary>摘要 / Abstract</summary>

  Nudge is a recommender system with cryptographic privacy. A Nudge deployment consists of three infrastructure servers and many users, who retrieve/rate items from a large data set (e.g., videos, posts, businesses). Periodically, the Nudge servers collect ratings from users in secret-shared form, then run a three-party computation to train a lightweight recommender model on users’ private ratings. Finally, the servers deliver personalized recommendations to each user. At every step, Nudge reveals nothing to the servers about any user’s preferences beyond the aggregate model itself. User privacy holds against an adversary that compromises the entire secret state of one server. The technical core of Nudge is a new, three-party protocol for matrix factorization. On the Netflix data set with half a million users and ten thousand items, Nudge (running on three 192-core servers on a local-area network) privately learns a recommender model in 50 mins with 40 GB of server-to-server communication. On a standard quality benchmark (nDCG@20), Nudge scores 0.29 out of 1.0, on par with non-private matrix factorization and just shy of non-private neural recommenders, which score 0.31.

  匹配依据：MPC: three party computation

  </details>

- **Benchmarking Secure Multiparty Computation Frameworks for Real-World Workloads in Diverse Network Settings**
  2026-02-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/183)
  Christopher Harth-Kitzerow, Jonas Schiller, Nina Schwanke, Thomas Prantl, Georg Carle

  <details><summary>摘要 / Abstract</summary>

  Secure Multiparty Computation (MPC) enables distributed parties to jointly evaluate functions on their combined datasets while preserving individual data confidentiality. Although MPC protocols and frameworks have achieved significant performance improvements in recent years, particularly for complex workloads like secure neural network inference, systematic standardization and benchmarking of these frameworks remain underexplored. This work comprehensively analyzes over 50 MPC applications to identify the core algorithmic structure most common in real-world MPC applications. From this analysis, we derive six reference use cases and implement these across four state-of-the-art MPC frameworks: HPMPC, MPyC, MP-SPDZ, and MOTION. We develop an open-source benchmarking framework that evaluates these implementations under varying network conditions, including bandwidth constraints, latency, packet loss, and input sizes. Our work presents the first systematic cross-framework evaluation of MPC performance based on real-world use cases across diverse network conditions and MPC security models. Thus, our comprehensive analysis yields novel insights into practical MPC performance and provides evidence-based recommendations for framework selection across different operational contexts.

  匹配依据：MPC: secure multiparty computation

  </details>

- **On (Im)possibility of Network Oblivious Transfer via Noisy Channels and Non-Signaling Correlations**
  2026-02-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.03421)
  Hadi Aghaee, Christian Deppe, Holger Boche

  <details><summary>摘要 / Abstract</summary>

  This work investigates the fundamental limits of implementing network oblivious transfer via noisy multiple access channels and broadcast channels between honest-but-curious parties when the parties have access to general tripartite non-signaling correlations. By modeling the shared resource as an arbitrary tripartite non-signaling box, we obtain a unified perspective on both the channel behavior and the resulting correlations. Our main result demonstrates that perfect oblivious transfer is impossible. In the asymptotic regime, we further show that even negligible leakage cannot be achieved, as repeated use of the resource amplifies the receiver(s)&#x27;s ability to distinguish messages that were not intended for him/them. In contrast, the receiver(s)&#x27;s own privacy is not subject to a universal impossibility limitation.

  匹配依据：MPC: oblivious transfer

  </details>

- **gcVM: Publicly Auditable MPC via Garbled Circuits with Applications to Private EVM-Compatible Computation**
  2026-02-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/170)
  Avishay Yana, Meital Levy, Mike Rosulek, Hila Dahari-Garbian

  <details><summary>摘要 / Abstract</summary>

  Blockchains have achieved substantial progress in scalability and fault tolerance, yet they remain fundamentally limited in confidentiality, hindering adoption by businesses, communities, and individuals who require privacy-preserving computations. Existing zero-knowledge (ZK) solutions provide partial privacy guarantees but struggle with performance and composability, especially for multi-party computations over shared private state. In this work, we introduce gcVM, a novel extension to the Ethereum Virtual Machine (EVM) that integrates garbled-circuit-based secure multi-party computation to enable general-purpose, privacy-preserving computation on-chain. gcVM allows transactional interactions between untrusted parties while balancing the transparency of public blockchains with strong confidentiality. Our implementation demonstrates up to 83 confidential transactions per second (cTPS) on standard cloud instances, with projected enhancements expected to scale throughput to approximately 500 cTPS—two to three orders of magnitude faster than comparable FHE-based solutions. gcVM is compatible with existing EVM tooling, provides public auditability, and requires no trusted hardware, offering a practical and efficient platform for privacy-centric blockchain applications across finance, governance, and decentralized services.

  匹配依据：MPC: garbled circuit, garbled circuits, secure multi party computation

  </details>

- **When Feasibility of Fairness Audits Relies on Willingness to Share Data: Examining User Acceptance of Multi-Party Computation Protocols for Fairness Monitoring**
  2026-02-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.01846)
  Changyang He, Parnian Jahangirirad, Lin Kyi, Asia J. Biega

  <details><summary>摘要 / Abstract</summary>

  Fairness monitoring is critical for detecting algorithmic bias, as mandated by the EU AI Act. Since such monitoring requires sensitive user data (e.g., ethnicity), the AI Act permits its processing only with strict privacy measures, such as multi-party computation (MPC), in compliance with the GDPR. However, the effectiveness of such secure monitoring protocols ultimately depends on people&#x27;s willingness to share their data. Little is known about how different MPC protocol designs shape user acceptance. To address this, we conducted an online survey with 833 participants in Europe, examining user acceptance of various MPC protocol designs for fairness monitoring. Findings suggest that users prioritized risk-related attributes (e.g., privacy protection mechanism) in direct evaluation but benefit-related attributes (e.g., fairness objective) in simulated choices, with acceptance shaped by their fairness and privacy orientations. We derive implications for deploying and communicating privacy-preserving protocols in ways that foster informed consent and align with user expectations.

  匹配依据：MPC: multi party computation

  </details>

- **Co-designing for Compliance: Multi-party Computation Protocols for Post-Market Fairness Monitoring in Algorithmic Hiring**
  2026-02-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.01837)
  Changyang He, Nina Baranowska, Josu Andoni Eguiluz Castaneira, Guillem Escriba, Matthias Juentgen, Anna Via, Frederik Zuiderveen Borgesius, Asia Biega

  <details><summary>摘要 / Abstract</summary>

  Post-market fairness monitoring is now mandated to ensure fairness and accountability for high-risk employment AI systems under emerging regulations such as the EU AI Act. However, effective fairness monitoring often requires access to sensitive personal data, which is subject to strict legal protections under data protection law. Multi-party computation (MPC) offers a promising technical foundation for compliant post-market fairness monitoring, enabling the secure computation of fairness metrics without revealing sensitive attributes. Despite growing technical interest, the operationalization of MPC-based fairness monitoring in real-world hiring contexts under concrete legal, industrial, and usability constraints remains unknown. This work addresses this gap through a co-design approach integrating technical, legal, and industrial expertise. We identify practical design requirements for MPC-based fairness monitoring, develop an end-to-end, legally compliant protocol spanning the full data lifecycle, and empirically validate it in a large-scale industrial setting. Our findings provide actionable design insights as well as legal and industrial implications for deploying MPC-based post-market fairness monitoring in algorithmic hiring systems.

  匹配依据：MPC: multi party computation, secure computation

  </details>

- **AI for Sustainable Data Protection and Fair Algorithmic Management in Environmental Regulation**
  2026-02-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.07021)
  Sahibpreet Singh, Saksham Sharma

  <details><summary>摘要 / Abstract</summary>

  Integration of AI into environmental regulation represents a significant advancement in data management. It offers promising results in both data protection plus algorithmic fairness. This research addresses the critical need for sustainable data protection in the era of ever evolving cyber threats. Traditional encryption methods face limitations in handling the dynamic nature of environmental data. This necessitates the exploration of advanced cryptographic techniques. The objective of this study is to evaluate how AI can enhance these techniques to ensure robust data protection while facilitating fair algorithmic management. The methodology involves a comprehensive review of current advancements in AI-enhanced homomorphic encryption (HE) and multi-party computation (MPC). It is coupled with an analysis of how these techniques can be applied to environmental data regulation. Key findings indicate that AI-driven dynamic key management, adaptive encryption schemes, and optimized computational efficiency in HE, alongside AI-enhanced protocol optimization and fault mitigation in MPC, significantly improve the security of environmental data processing. These findings highlight a crucial research gap in the intersection of AI, cyber laws, and environmental regulation, particularly in terms of addressing algorithmic bias, transparency, and accountability. The implications of this research underscore the need for stricter cyber laws. Also, the development of comprehensive regulations to safeguard sensitive environmental data. Future efforts should focus on refining AI systems to balance security with privacy and ensuring that regulatory frameworks can adapt to technological advancements. This study provides a foundation for future research aimed at achieving secure sustainable environmental data management through AI innovations.

  匹配依据：MPC: multi party computation

  </details>

- **Fuzzy Enhanced Private Set Union in Hamming and Minkowski Spaces**
  2026-02-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/166)
  Qiang Liu, JaeYoung Bae, Hyung Tae Lee, Joon-Woo Lee

  <details><summary>摘要 / Abstract</summary>

  Private Set Union (PSU) enables two parties holding private sets $X$ and $Y$ to compute their union $X\cup Y$ without revealing anything else. Enhanced PSU (ePSU) further eliminates during-execution leakage, but existing constructions are limited to exact matching. This restriction is inadequate for many real-world applications involving noisy data, approximate representations, or feature embeddings, where similarity is naturally defined via distance metric rather than strict equality. In this work, we introduce fuzzy ePSU, a new cryptographic primitive that supports distance-based union while preserving the no during-execution leakage guarantee of ePSU. Given a distance metric $\mathsf{dist}(\cdot,\cdot)$ and a threshold $\delta$, fuzzy ePSU allows the receiver to learn exactly those sender items whose distance to all receiver items exceeds $\delta$, thereby computing a fuzzy union of the two sets. We present two concrete fuzzy ePSU constructions instantiated over different metric spaces. For the Hamming space, we design a protocol based on a new primitive called Fuzzy Oblivious Non-Membership Conditional Randomness Generation (FOnMCRG), achieving linear complexity in the input set sizes and $\delta$. For the Minkowski space, we introduce Fuzzy Permuted Non-Membership Conditional Randomness Generation (FpnMCRG), which combines fuzzy mapping with hashing-to-bin techniques and achieves (quasi-)linear complexity in the input sizes and dimension. We implement our protocols and evaluate their performance in both metric spaces. For input sets of size $2^{12}$, our Hamming-space protocol incurs about 79.990~MB of communication and 70.686~s of runtime with $\delta=4$. In the Minkowski space with $\{1,2,\infty\}$-norm, dimension $d=10$, and $\delta=30$, it incurs 388.137--689.889~MB of communication and 347.082--483.328~s of runtime.

  匹配依据：MPC: private set union

  </details>

- **Bifrost: A Much Simpler Secure Two-Party Data Join Protocol for Secure Data Analytics**
  2026-02-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.01225)
  Shuyu Chen, Mingxun Zhou, Haoyu Niu, Guopeng Lin, Weili Han

  <details><summary>摘要 / Abstract</summary>

  Secure data join enables two parties with vertically distributed data to securely compute the joined table, allowing the parties to perform downstream Secure multi-party computation-based Data Analytics (SDA), such as training machine learning models, based on the joined table. While Circuit-based Private Set Intersection (CPSI) can be used for secure data join, it introduces redundant dummy rows in the joined table, which results in high overhead in the downstream SDA tasks. iPrivJoin addresses this issue but introduces significant communication overhead in the redundancy removal process, as it relies on the cryptographic primitive OPPRF for data encoding and multiple rounds of oblivious shuffles. In this paper, we propose a much simpler secure data join protocol, Bifrost, which outputs (the secret shares of) a redundancy-free joined table. The highlight of Bifrost lies in its simplicity: it builds upon two conceptually simple building blocks, an ECDH-PSI protocol and a two-party oblivious shuffle protocol. The lightweight protocol design allows Bifrost to avoid the need for OPPRF. We also proposed a simple optimization named \textit{dual mapping} that reduces the rounds of oblivious shuffle needed from two to one. Experiments on datasets of up to 100 GB show that Bifrost achieves $2.54 \sim 22.32\times$ speedup and reduces the communication by $84.15\% \sim 88.97\%$ compared to the SOTA redundancy-free secure data join protocol iPrivJoin. Notably, the communication size of Bifrost is nearly equal to the size of the input data. In the two-step SDA pipeline evaluation (secure join and SDA), the redundancy-free property of Bifrost not only avoids the catastrophic error rate blowup in the downstream tasks caused by the dummy rows in the joined table (as introduced in CPSI), but also shows up to $2.80\times$ speed-up in the SDA process with up to $73.15\%$ communication reduction.

  匹配依据：MPC: private set intersection, secure multi party computation

  </details>

- **Fuzzy Private Set Union via Oblivious Key Homomorphic Encryption Retrieval**
  2026-01-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.20400)
  Jean-Guillaume Dumas, Aude Maignan, Luiza Soezima

  <details><summary>摘要 / Abstract</summary>

  Private Set Multi-Party Computations are protocols that allow parties to jointly and securely compute functions: apart from what is deducible from the output of the function, the input sets are kept private. Then, a Private Set Union (PSU), resp. Intersection (PSI), is a protocol that allows parties to jointly compute the union, resp. the intersection, between their private sets. Now a structured PSI, is a PSI where some structure of the sets can allow for more efficient protocols. For instance in Fuzzy PSI, elements only need to be close enough, instead of equal, to be part of the intersection. We present in this paper, Fuzzy PSU protocols (FPSU), able to efficiently take into account approximations in the union. For this, we introduce a new efficient sub-protocol, called Oblivious Key Homomorphic Encryption Retrieval (OKHER), improving on Oblivious Key-Value Retrieval (OKVR) techniques in our setting. In the fuzzy context, the receiver set $X=\{x_i\}_{1..n}$ is replaced by ${\mathcal B}_δ(X)$, the union of $n$ balls of dimension $d$ with radius $δ$, centered at the $x_i$. The sender set is just its $m$ points of dimension $d$. Then the FPSU functionality corresponds to $X \sqcup \{y \in Y, y \notin {\mathcal B}_δ(X)\}$. Thus, we formally define the FPSU functionality and security properties, and propose several protocols tuned to the patterns of the balls using the $l_\infty$ distance. Using our OKHER routine and homomorphic encryption, we are for instance able to obtain a FPSU protocols with an asymptotic communication volume bound ranging from $O(dm\log(δ{n}))$ to $O(d^2m\log(δ^2n))$, depending on the receiver data set structure.

  匹配依据：MPC: private set union

  </details>

- **From Arithmetic to Shamir: Secure and Efficient Masking Gadgets for Multiplications - Applications to the Post-Quantum Signature Scheme MQOM**
  2026-01-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/138)
  Vladimir Sarde, Nicolas Debande, Louis Goubin

  <details><summary>摘要 / Abstract</summary>

  Efficiently masking multiplications in software is a long standing and extensively studied problem. A variety of gadgets have been proposed to perform these multiplications, each offering different trade-offs between efficiency and security. However, almost all existing solutions rely on arithmetic masking, in which multiplications cannot be naturally protected. In this work, we introduce two novel gadgets, named A2S and S2A, that enable conversions between arithmetic masking and Shamir’s Secret Sharing (SSS)-based masking. With this approach, multiplications can be performed naturally and securely in a sharewise manner. We prove that our gadgets achieve SNI security, which provides security guarantees and straightforward composability. Moreover, we demonstrate that composing them with multiplication yields PINI security. We then provide a detailed complexity analysis and discuss the contexts where our gadgets are most relevant. As a case study, we apply them to the MQOM post-quantum signature scheme, a candidate in the second round of the NIST additional post-quantum digital signature standardization process. When computing the sensitive multiplications in MQOM, for masking order t = 1, our approach reduces the number of multiplications, additions, and randomness requirements by 31%, 71%, and 60%, respectively, compared to the state of the art, while incurring only small additional memory overhead. We further show that these gains not only hold but actually increase as the masking order grows. Our results demonstrate that arithmetic-to-SSS conversions provide an effective and scalable path toward efficient masked implementations, making them particularly attractive for postquantum cryptography.

  匹配依据：MPC: secret sharing

  </details>

- **ARES: Online-Friendly Robust Threshold ECDSA with Amortized Costs**
  2026-01-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/130)
  Guofeng Tang, Tian Qiu, Bowen Jiang, Haiyang Xue, Meng Hao, Guomin Yang, Robert H. Deng

  <details><summary>摘要 / Abstract</summary>

  Threshold ECDSA has been an active research topic in recent years, driven by its wide-ranging applications, particularly in blockchain domains. In these real-world applications, robustness is a critical requirement. It ensures that a signature is successfully generated as long as $t+1$ honest parties are present, regardless of malicious behavior from others. Existing robust constructions generally fall into two categories: those based on threshold linearly homomorphic encryption (TLHE) and those leveraging the Multiplicative-to-Additive (MtA) paradigm. The TLHE-based approach (e.g., WMC24 in NDSS&#x27;24) achieves constant sending communication per party but incurs an expensive online phase. In contrast, the MtA-based approach (e.g., TX25 in S\&amp;P&#x27;25) is online-friendly, requiring only elliptic-curve group operations during the online phase. However, it has the drawback of requiring $O(n)$ sending communication per party when $n$ parties are involved. In this work, we propose ARES, a robust threshold ECDSA scheme designed to reduce both communication and computational overhead within the online-friendly MtA framework. To improve the communication efficiency of TX25, we propose verifiable non-interactive multiplication (VNIM), a new primitive which endows standard non-interactive multiplication with public verifiability. Simultaneously, we leverage super-invertible matrices and packed secret sharing to amortize the overall costs. Specifically, when setting the packing parameter of packed secret sharing to $\ell = 1$ (i.e., without secret packing), ARES exhibits linear communication complexity while already achieving an approximately $50\%$ improvement over TX25. When configuring $\ell = t/3$ with $t \ge 12$, ARES achieves lower communication overhead than WMC24, requiring a constant $\approx 4.5\text{ KB}$ per party. Furthermore, setting $\ell = t/2$ reduces the amortized communication cost to roughly $3\text{ KB}$ per party. On the other hand, amortizing across $\ell$ signatures incurs a trade-off by increasing the required party size by $\ell$.

  匹配依据：MPC: secret sharing

  </details>

- **Private Iris Recognition with High-Performance FHE**
  2026-01-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.17561)
  Jincheol Ha, Guillaume Hanrot, Taeyeong Noh, Jung Hee Cheon, Jung Woo Kim, Damien Stehlé

  <details><summary>摘要 / Abstract</summary>

  Among biometric verification systems, irises stand out because they offer high accuracy even in large-scale databases. For example, the World ID project aims to provide authentication to all humans via iris recognition, with millions already registered. Storing such biometric data raises privacy concerns, which can be addressed using privacy-enhancing techniques. Bloemen et al. describe a solution based on 2-out-of-3 Secret-Sharing Multiparty Computation (SS-MPC), for the World ID setup. In terms of security, unless an adversary corrupts 2~servers, the iris codes remain confidential and nothing leaks beyond the result of the computation. Their solution is able to match~$32$ users against a database of~$2^{22}$ iris codes in~$\approx 2$s , using~24 H100 GPUs, more than 40~communication rounds and $81$GB/party of data transferred (the timing assumes a network speed above~3Tb/s). In the present work, we explore the use of Threshold Fully Homomorphic Encryption (ThFHE) for the same task. The ThFHE solution brings a number of security advantages: no trusted setup, the encrypted database and queries can be public, the secret can be distributed among many parties, and active security can be added without significant performance degradation. Our proof-of-concept implementation of the computation phase handles $32$~eyes against a database of $7\cdot 2^{14}$ iris codes in~$\approx 1.8$s ($\approx 0.33s$ for 4 eyes against the same database), using 8 RTX-5090 GPUs. To this, one should add~2 to 3 rounds of communication (depending on deployment choice). We perform the matching using the CKKS (Th)FHE scheme. Our main technical ingredients are the use of recent progress on FHE-based linear algebra boosted using int8 GPU operations, and the introduction of a technique reducing the number of ciphertexts to be processed as early as possible.

  匹配依据：MPC: multiparty computation, secret sharing

  </details>

- **How to Steal Oblivious Transfer from Minicrypt**
  2026-01-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/113)
  Cruz Barnum, David Heath

  <details><summary>摘要 / Abstract</summary>

  The celebrated work of Impagliazzo and Rudich (STOC&#x27;89) provides an oracle separation between those primitives implied by a random oracle (RO) and those that imply key agreement and public-key cryptography. For the last 36 years, this result seemed to cleanly separate two worlds: Minicrypt, which is often described as what can be achieved from only ROs, and Cryptomania, which is a world where public-key cryptography exists. This work presents a natural primitive, called an oblivious interactive hash function (OIHF), and shows the following: (1) OIHFs can be constructed from ROs. (2) OIHFs can be constructed from oblivious transfer (OT), and hence they are implied by various well-studied public-key-style assumptions. (3) The existence of an OIHF implies OT, via a non-black-box reduction. Point (1) places the primitive into Minicrypt, point (2) implies that numerous well-studied standard-model complexity assumptions imply that OIHFs exist, and point (3) shows that this primitive circumvents the barrier imposed by Impagliazzo and Rudich. Our results show that a protocol constructible in Minicrypt implies OT. However, this *does not* imply that OT can be constructed from RO; indeed, Impagliazzo/Rudich shows this is impossible. Our non-black-box reduction is well-defined only for standard-model OIHFs, i.e. ones that do not use RO, and at present we can only construct standard-model OIHF in Cryptomania. This is to say that we do not propose an OT protocol that can be constructed from a cryptographic hash function. Rather, our results call into question the value of the random oracle model as an idealization of Minicrypt, and they question where the boundaries of Minicrypt lie.

  匹配依据：MPC: oblivious transfer

  </details>

- **Emerging Threats and Countermeasures in Neuromorphic Systems: A Survey**
  2026-01-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.16589)
  Pablo Sorrentino, Stjepan Picek, Ihsen Alouani, Nikolaos Athanasios Anagnostopoulos, Francesco Regazzoni, Lejla Batina, Tamalika Banerjee, Fatih Turkmen

  <details><summary>摘要 / Abstract</summary>

  Neuromorphic computing mimics brain-inspired mechanisms through spiking neurons and energy-efficient processing, offering a pathway to efficient in-memory computing (IMC). However, these advancements raise critical security and privacy concerns. As the adoption of bio-inspired architectures and memristive devices increases, so does the urgency to assess the vulnerability of these emerging technologies to hardware and software attacks. Emerging architectures introduce new attack surfaces, particularly due to asynchronous, event-driven processing and stochastic device behavior. The integration of memristors into neuromorphic hardware and software implementations in spiking neural networks offers diverse possibilities for advanced computing architectures, including their role in security-aware applications. This survey systematically analyzes the security landscape of neuromorphic systems, covering attack methodologies, side-channel vulnerabilities, and countermeasures. We focus on both hardware and software concerns relevant to spiking neural networks (SNNs) and hardware primitives, such as Physical Unclonable Functions (PUFs) and True Random Number Generators (TRNGs) for cryptographic and secure computation applications. We approach this analysis from diverse perspectives, from attack methodologies to countermeasure strategies that integrate efficiency and protection in brain-inspired hardware. This review not only maps the current landscape of security threats but provides a foundation for developing secure and trustworthy neuromorphic architectures.

  匹配依据：MPC: secure computation

  </details>

- **Secure Computation for Fixed-point and Floating-point Arithmetic**
  2026-01-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/102)
  Tianpei Lu, Bingsheng Zhang, Yuyang Feng, Kui Ren

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation (MPC) protocols naturally operate over rings/fields, and they are less efficient for real-number arithmetics, which are commonly needed in AI-powered applications. State-of-the-art solutions are hindered by the high cost of fixed-point and floating-point operations. This work addresses these bottlenecks by proposing a series of novel MPC protocols. Compared to SOTA, our fixed-point multiplication protocol reduces the online communication cost by about $75\%$. For scenarios where higher precision is required, we present the first constant-round floating-point arithmetic protocol for addition and multiplication in the three-party computation (3PC) setting, reducing the communication overhead of SOTA by approximately $95\%$. The experimental results demonstrate that our fixed-point multiplication protocol is more than $3\times$ faster than all mainstream solutions (such as ABY3, Falcon, Orca, etc.). Our floating-point addition and multiplication protocols are over $3\times$ and $5\times$, respectively, faster than SOTA, SecFloat [S&amp;P 23].

  匹配依据：MPC: secure computation, secure multi party computation, three party computation

  </details>

- **Deal out oblivious correlations: 2-depth HSS circuit for silent V-OLE generation**
  2026-01-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/104)
  Davide Cerutti, Stelvio Cimato

  <details><summary>摘要 / Abstract</summary>

  We analyzed in depth the Homomorphic Secret Sharing construction applied for Pseudorandom Correlation Function, and we obtained interesting results for various applications. In this paper, we discuss how the PCF can be achieved using the Damgard-Jurik HSS schema by solving the distance function over a ciphertext parametric space of \(\mathbb{Z}^{*}_{n^{\zeta + 1}}\), performing the distributed multiplication protocol as the base building block for our PCF. We created a weak PCF for Vector-OLE via 1-depth HSS circuit, furthermore, via what we called pre-computation with RO-less, we achieved a strong PCF for V-OLE between two parties correct against anhonest-but-curious adversary \(\mathcal{A}_{\mathsf{hbc}}\) and fail-safe secure against an active adversary \(\mathcal{A}_{\mathsf{poly}}\). We also extended our main construction by describing a silent approach in two different ways described as semi-silent by a pre-sampling assumption between the parties and a true-silent protocol execution exploiting the generation of seeds by a PRF. As a last step, we discussed how to build a \(n \times\)OLE generator via our pre-computation session to craft an arbitrary amount of OLE correlation. Our entire paper is further verified by the implementation of a complete and exhaustive library covering all HSS operations, publicly accessible and usable via \(\textit{pip install obliviouspy-HSS}\) and importing \(\textit{import oblivious}\).

  匹配依据：MPC: secret sharing

  </details>

- **Tropical cryptography IV: Digital signatures and secret sharing with arbitrary access structure**
  2026-01-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/095)
  Dima Grigoriev, Chris Monico, Vladimir Shpilrain

  <details><summary>摘要 / Abstract</summary>

  We use tropical algebras as platforms for a very efficient digital signature protocol. Security relies on computational hardness of factoring a given tropical matrix in a product of two matrices of given dimensions; this problem is known to be NP-complete. We also offer a secret sharing scheme with an arbitrary access structure where security of the shared secret is based on computational hardness of the same problem.

  匹配依据：MPC: secret sharing

  </details>

- **High-Throughput and Scalable Secure Inference Protocols for Deep Learning with Packed Secret Sharing**
  2026-01-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.13041)
  Qinghui Zhang, Xiaojun Chen, Yansong Zhang, Xudong Chen

  <details><summary>摘要 / Abstract</summary>

  Most existing secure neural network inference protocols based on secure multi-party computation (MPC) typically support at most four participants, demonstrating severely limited scalability. Liu et al. (USENIX Security&#x27;24) presented the first relatively practical approach by utilizing Shamir secret sharing with Mersenne prime fields. However, when processing deeper neural networks such as VGG16, their protocols incur substantial communication overhead, resulting in particularly significant latency in wide-area network (WAN) environments. In this paper, we propose a high-throughput and scalable MPC protocol for neural network inference against semi-honest adversaries in the honest-majority setting. The core of our approach lies in leveraging packed Shamir secret sharing (PSS) to enable parallel computation and reduce communication complexity. The main contributions are three-fold: i) We present a communication-efficient protocol for vector-matrix multiplication, based on our newly defined notion of vector-matrix multiplication-friendly random share tuples. ii) We design the filter packing approach that enables parallel convolution. iii) We further extend all non-linear protocols based on Shamir secret sharing to the PSS-based protocols for achieving parallel non-linear operations. Extensive experiments across various datasets and neural networks demonstrate the superiority of our approach in WAN. Compared to Liu et al. (USENIX Security&#x27;24), our scheme reduces the communication upto 5.85x, 11.17x, and 6.83x in offline, online and total communication overhead, respectively. In addition, our scheme is upto 1.59x, 2.61x, and 1.75x faster in offline, online and total running time, respectively.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **HYPERSHIELD: Protecting the Hypercube MPC-in-the-Head Framework Against Differential Probing Adversaries without Masking**
  2026-01-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/081)
  Linda Pirker, Quinten Norga, Suparna Kundu, Anindya Ganguly, Barry van Leeuwen, Angshuman Karmakar, Ingrid Verbauwhede

  <details><summary>摘要 / Abstract</summary>

  Post-quantum secure digital signatures based on the MPC-in-the-Head (MPCitH) paradigm, a zero-knowledge (ZK) proof-based construction, are becoming increasingly popular due to their small public key size. However, the development of techniques for protecting MPCitH-based schemes against side-channel attacks remains slow, despite them being critical for real-world deployment. In this work, we adapt the Hypercube-MPCitH framework exploiting its native use of additive secret sharing to enable inherent protection against first- and high-order differential power analysis (DPA). We first perform a sensitivity analysis of the Hypercube Syndrome Decoding in the Head (SDitH) digital signature scheme with respect to both simple and differential power analysis. Based on the insight into its side-channel sensitivity, we then propose a tweak to the signature scheme to increase its inherent resistance against DPAs by design, eliminating the need to explicitly mask large parts of the signing procedure. More specifically, this is achieved through the novel (k+1)-Hypercube ZK Protocol: the proposed tweak increases the number of hidden shares an adversary must probe to recover the secret key from one to k+1, thus achieving inherent masking order k. Typically, increasing the amount of hidden shares results in a degradation of soundness in the zero-knowledge proof and as a result increases the signature size to a point where the scheme becomes of limited practical interest. To address this, we propose a technique to select the hidden shares in a more structured and optimal fashion, by exploiting the GGM tree structure in the Hypercube-MPCitH framework. As a result, the amount of revealed seeds is reduced, thus resulting in a smaller signature size even compared to the original hypercube protocol. Finally, we implement and benchmark the proposed Hypercube-SDitH signature scheme, comparing it against the cost of traditional masking. We propose different parameter sets that explore a trade-off between computational overhead and signature size. For 3rd-order protection, our tweaked signature scheme only incurs a 35-50% overhead in computational cost, compared to an estimated overhead of 300% for a fully masked implementation, while the overhead in signature size stays relatively low (52%). Overall, we demonstrate that the proposed (k+1)-Hypercube ZK Protocol can be used to construct efficient, DPA-resistant MPCitH-based digital signatures.

  匹配依据：MPC: secret sharing

  </details>

- **Function Recovery Attacks in Gate-Hiding Garbled Circuits using SAT Solving**
  2026-01-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.13271)
  Chao Yin, Zunchen Huang, Chenglu Jin, Marten van Dijk, Fabio Massacci

  <details><summary>摘要 / Abstract</summary>

  Semi-Private Function Evaluation (SPFE) enables joint computation while protecting both input data and the function itself. A practical instantiation is gate-hiding garbled circuits, which conceal gate functionalities while revealing circuit topology. Existing security definitions intentionally exclude leakage through topology, leaving its concrete impact on function privacy largely unexplored. We present a SAT-based function-recovery attack that reconstructs hidden gate operations from a circuit&#x27;s public topology under two attacker knowledge models. Our approach combines topology-preserving simplification theorems with a decomposition of the recovery task into smaller SAT queries, thereby reducing the candidate gate-type assignment space and improving recovery performance. We evaluate the attack on ISCAS benchmarks, representative secure computation circuits, and fault-tolerant sensor fusion circuits under a 24-hour recovery budget. Compared to a baseline attack, the optimized version substantially reduces recovery time and, in some cases, completes recovery within the evaluation budget where the baseline does not. Our results show that revealing circuit topology can materially assist recovery of hidden gate functionality, identifying topology as a security-relevant leakage channel in gate-hiding garbled circuits.

  匹配依据：MPC: garbled circuits, secure computation

  </details>

- **2PC Memory-Manipulating Programs with Constant Overhead**
  2026-01-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/086)
  David Heath

  <details><summary>摘要 / Abstract</summary>

  General-purpose secure multiparty computation (MPC) remains bottlenecked in large part by a lack of efficient techniques for handling memory access. We demonstrate a remarkably simple and efficient 2PC instantiation of random access memory (RAM), based on distributed point functions (DPFs, Gilboa and Ishai, Eurocrypt&#x27;14). Our semi-honest 2PC protocol can be achieved from oblivious transfer (OT) and a black-box pseudorandom generator (PRG). For a memory storing large enough data words, our 2PC RAM incurs constant communication overhead per access. Like prior works using DPFs to achieve memory access, our work incurs linear computation per access, but per-access communication is lean. Our 2PC RAM is built on top of an obliviousness-friendly model of computation called the single access machine model (SAM, Appan et al., CCS&#x27;24). In the SAM model, each memory slot can be read at most once. We present a simple 2PC SAM protocol, where each single-access memory operation incurs at most $O(w + \lambda \lg n)$ bits of communication, where $w$ is the word size, $n$ is the number of memory words, and $\lambda$ is a security parameter. Of this cost, only $2w + 2\lg n$ bits are incurred in the online phase. There are now many oblivious algorithms that compile directly to SAM more efficiently than via a compilation to RAM, and our 2PC SAM can instantiate these algorithms. As one example, we can use our 2PC SAM to implement privacy-preserving graph traversal (DFS or BFS) over a secret-shared size-$n$ graph while revealing nothing beyond the runtime of the SAM program. Our construction achieves online communication $O(n \lg n)$ bits, asymptotically matching the number of bits touched in a corresponding cleartext graph traversal.

  匹配依据：MPC: oblivious transfer, secure multiparty computation

  </details>

- **SoK: Outsourced Private Set Intersection**
  2026-01-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/080)
  Sophie Hawkes, Christian Weinert

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) protocols are an essential privacy-enhancing technology for many real-world use cases, ranging from mobile contact discovery to fraud detection. However, PSI executed directly between input parties can result in unreasonable performance overhead. This motivates the study of outsourced PSI, where clients delegate the heavy PSI operations to an untrusted (cloud) server. In this SoK, we introduce a framework of 12 distinct properties that characterize outsourced PSI protocols based on security, functionality, and efficiency. By analyzing 20 protocols through this framework, we provide a valuable resource and an interactive tool for researchers and practitioners to select the most suitable protocols for their specific requirements. Finally, we discuss research gaps between trends in regular PSI and the current state of outsourced PSI, identifying promising avenues for future work.

  匹配依据：MPC: private set intersection

  </details>

- **Privacy-Preserving Federated Learning with Verifiable Fairness Guarantees**
  2026-01-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.12447)
  Mohammed Himayath Ali, Mohammed Aqib Abdullah, Syed Muneer Hussain, Mohammed Mudassir Uddin, Shahnawaz Alam

  <details><summary>摘要 / Abstract</summary>

  Federated learning enables collaborative model training across distributed institutions without centralizing sensitive data; however, ensuring algorithmic fairness across heterogeneous data distributions while preserving privacy remains fundamentally unresolved. This paper introduces CryptoFair-FL, a novel cryptographic framework providing the first verifiable fairness guarantees for federated learning systems under formal security definitions. The proposed approach combines additively homomorphic encryption with secure multi-party computation to enable privacy-preserving verification of demographic parity and equalized odds metrics without revealing protected attribute distributions or individual predictions. A novel batched verification protocol reduces computational complexity from BigO(n^2) to BigO(n \log n) while maintaining (\dparam, \deltap)-differential privacy with dparam = 0.5 and deltap = 10^{-6}. Theoretical analysis establishes information-theoretic lower bounds on the privacy cost of fairness verification, demonstrating that the proposed protocol achieves near-optimal privacy-fairness tradeoffs. Comprehensive experiments across four benchmark datasets (MIMIC-IV healthcare records, Adult Income, CelebA, and a novel FedFair-100 benchmark) demonstrate that CryptoFair-FL reduces fairness violations from 0.231 to 0.031 demographic parity difference while incurring only 2.3 times computational overhead compared to standard federated averaging. The framework successfully defends against attribute inference attacks, maintaining adversarial success probability below 0.05 across all tested configurations. These results establish a practical pathway for deploying fairness-aware federated learning in regulated industries requiring both privacy protection and algorithmic accountability.

  匹配依据：MPC: secure multi party computation

  </details>

- **InterPUF: Distributed Authentication via Physically Unclonable Functions and Multi-party Computation for Reconfigurable Interposers**
  2026-01-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.11368)
  Ishraq Tashdid, Tasnuva Farheen, Sazadur Rahman

  <details><summary>摘要 / Abstract</summary>

  Modern system-in-package (SiP) platforms increasingly adopt reconfigurable interposers to enable plug-and-play chiplet integration across heterogeneous multi-vendor ecosystems. However, this flexibility introduces severe trust challenges, as traditional authentication schemes fail to scale or adapt in decentralized, post-fabrication programmable environments. This paper presents InterPUF, a compact and scalable authentication framework that transforms the interposer into a distributed root of trust. InterPUF embeds a route-based differential delay physically unclonable function (PUF) across the reconfigurable interconnect and secures authentication using multi-party computation (MPC), ensuring raw PUF signatures are never exposed. Our hardware evaluation shows only 0.23% area and 0.072% power overhead across diverse chiplets while preserving authentication latency within tens of nanoseconds. Simulation results using pyPUF confirm strong uniqueness, reliability, and modeling resistance under process, voltage, and temperature variations. By combining interposer-resident PUF primitives with cryptographic hashing and collaborative verification, InterPUF enforces a minimal-trust authentication model without relying on a centralized anchor.

  匹配依据：MPC: multi party computation

  </details>

- **BABE: Verifying Proofs on Bitcoin Made 1000x Cheaper**
  2026-01-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/065)
  Sanjam Garg, Dimitris Kolonelos, Mikhail Sergeevitch, Srivatsan Sridhar, David Tse

  <details><summary>摘要 / Abstract</summary>

  Endowing Bitcoin with the ability to verify succinct proofs has been a longstanding problem with important applications such as scaling Bitcoin and allowing the Bitcoin asset to be used in other blockchains trustlessly. It is a challenging problem due to the lack of expressiveness in the Bitcoin scripting language and the small Bitcoin block space. BitVM2 is the state-of-the-art verification protocol for Bitcoin used in several mainnets and testnets, but it suffers from very high on-chain Bitcoin transaction fees in the unhappy path (over $14,000 in a recent experiment). Recent research BitVM3 dramatically reduces this on-chain cost by using a garbled SNARK verifier circuit to shift most of the verification off-chain, but each garbled circuit is 42 Gibytes in size, so the off-chain storage and setup costs are huge. This paper introduces BABE, a new proof verification protocol on Bitcoin, which preserves BitVM3&#x27;s savings of on-chain costs but reduces its off-chain storage and setup costs by three orders of magnitude. BABE uses a witness encryption scheme for linear pairing relations to verify Groth16 proofs. Since Groth16 verification involves non-linear pairings, this witness encryption scheme is augmented with a secure two-party computation protocol implemented using a very efficient garbled circuit for scalar multiplication on elliptic curves. The design of this garbled circuit builds on a recent work, Argo MAC, which gives an efficient garbling scheme to compute homomorphic MACs on such curves.

  匹配依据：MPC: garbled circuit, garbling scheme, secure two party computation

  </details>

- **PADER: Paillier-based Secure Decentralized Social Recommendation**
  2026-01-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.10212) · [Code](https://github.com/GarminQ/PADER)
  Chaochao Chen, Jiaming Qian, Fei Zheng, Yachuan Liu

  <details><summary>摘要 / Abstract</summary>

  The prevalence of recommendation systems also brings privacy concerns to both the users and the sellers, as centralized platforms collect as much data as possible from them. To keep the data private, we propose PADER: a Paillier-based secure decentralized social recommendation system. In this system, the users and the sellers are nodes in a decentralized network. The training and inference of the recommendation model are carried out securely in a decentralized manner, without the involvement of a centralized platform. To this end, we apply the Paillier cryptosystem to the SoReg (Social Regularization) model, which exploits both user&#x27;s ratings and social relations. We view the SoReg model as a two-party secure polynomial evaluation problem and observe that the simple bipartite computation may result in poor efficiency. To improve efficiency, we design secure addition and multiplication protocols to support secure computation on any arithmetic circuit, along with an optimal data packing scheme that is suitable for the polynomial computations of real values. Experiment results show that our method only takes about one second to iterate through one user with hundreds of ratings, and training with ~500K ratings for one epoch only takes &lt;3 hours, which shows that the method is practical in real applications. The code is available at https://github.com/GarminQ/PADER.

  匹配依据：MPC: secure computation

  </details>
