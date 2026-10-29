# 2025 · MPC · 含会议/期刊记录 · 第 1/1 页

[总目录](../PAPERS.md)

- **Fully Anonymous Secret Sharing.**
  2025-10-23 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-032-01884-7_12) · [IACR ePrint](https://eprint.iacr.org/2025/1984)
  Paul Lou, Yuval Ishai, Abhishek Jain, Allison Bishop, Matthew Green

  <details><summary>摘要 / Abstract</summary>

  In a secret sharing scheme for a monotone access structure $\mathcal{A}:\{0,1\}^n\rightarrow \{0,1\}$, a dealer can share a secret $s$ to $n$ parties such that any authorized subset of parties $A\in\mathcal{A}$ can recover $s$ while all other subsets learn nothing about $s$. In this work, we study fully anonymous secret sharing (FASS), which strengthens standard secret sharing by requiring the following properties: - Share Anonymity. The shares belonging to any unauthorized set of parties not only hide the secret, but also all identifiable information such as party identities and whether or not the shares were generated together. In particular, it suffices that such shares be uniform and independent. - Anonymous Reconstruction. The reconstruction algorithm does not need to know the reconstructing set of parties. Efficient FASS exists for threshold access structures. For general access structures, the only known construction relies on a monotone DNF representation of $\mathcal{A}$ and has per-party share size $\Omega(\ell n)$ where $\ell$ is the number of minterms of $\mathcal{A}$. This leaves an exponential gap between standard secret sharing and FASS even for simple access structures. Moreover, even in the threshold case, known schemes could not achieve optimal robust reconstruction when mixing shares of multiple secrets. Motivated by a recent work of Eldridge et al. [USENIX&#x27;24], who demonstrated an application of FASS to stalker detection, we initiate a systematic study of FASS, obtaining the following main results. - Near-Optimal Information-Theoretic FASS. We obtain strong lower bounds, showing that the dependence on the DNF size is generally inherent. In particular, the share size can be exponential in the number of parties or even in the minimum CNF size. This stands in sharp contrast to standard secret sharing, where no super-polynomial lower bounds are known, and where the share size is upper bounded by the CNF size. For DNF with $\ell$ small minterms, we improve the previous upper bound to $\tilde O(\ell)$, matching our lower bound up to a polylogarithmic factor. - Computational FASS. We show that the above negative results can be circumvented in the computational setting, obtaining FASS schemes with succinct shares. Under the learning with errors (LWE) assumption, we present a general compiler from standard secret sharing to FASS that preserves the share size of the underlying scheme. For natural graph access structures, we directly construct succinct FASS from either one-way functions or bilinear maps. - Robust FASS. We show that simple modifications of our computational FASS schemes can allow for robust reconstruction of a polynomially unbounded number of secrets from any mixture of their authorized shares.

  匹配依据：MPC: secret sharing

  </details>

- **Velox: Scalable Fair Asynchronous MPC from Lightweight Cryptography.**
  2025-09-10 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3719027.3765114) · [IACR ePrint](https://eprint.iacr.org/2025/1630)
  Chen-Da Liu-Zhang, Aniket Kate, Akhil Bandarupalli, Yifan Song, Daniel Pöllmann, Xiaoyu Ji

  <details><summary>摘要 / Abstract</summary>

  Multi-party computation (MPC) enables a set of mutually $n$ distrusting parties to compute any function on their private inputs. Mainly, MPC facilitates agreement on the function’s output while preserving the secrecy of honest inputs, even against a subset of $t$ parties controlled by an adversary. With applications spanning from anonymous broadcast to private auctions, MPC is considered a cornerstone of distributed cryptography, and significant research efforts have been aimed at making MPC practical in the last decade. However, most libraries either make strong assumptions like the network being bounded synchronous, or incur high computation overhead from the extensive use of expensive public-key operations that prevent them from scaling beyond a few dozen parties. This work presents Velox, an asynchronous MPC protocol that offers fairness against an optimal adversary corrupting up to $t&lt;\frac{n}{3}$ parties. Velox significantly enhances practicality by leveraging lightweight cryptographic primitives - such as symmetric-key encryption and hash functions - which are 2-3 orders of magnitude faster than public-key operations, resulting in substantial computational efficiency. Moreover, Velox is highly communication-efficient, with linear amortized communication relative to circuit size and only $\mathcal{O}(n^3)$ field elements of additive overhead. Concretely, Velox requires just $9.33$ field elements per party per multiplication gate, more than $10\times$ reduction compared to the state of the art. Moreover, Velox also offers Post-Quantum Security as lightweight cryptographic primitives retain their security against a quantum adversary. We implement Velox comprehensively, covering both offline and online phases, and evaluate its performance on a geographically distributed testbed through a real-world application: anonymous broadcast. Our implementation securely shuffles a batch of $k=256$ messages in $4$ seconds with $n=16$ parties and $18$ seconds with $n=64$ parties, a $36\times$ and $28.6\times$ reduction in latency compared to the prior best work. At scale with $n=112$ parties, Velox is able to shuffle the same batch of messages in under $50$ seconds from end to end, illustrating its effectiveness and scalability. Overall, our work removes significant barriers faced by prior asynchronous MPC solutions, making asynchronous MPC practical and efficient for large-scale deployments involving $100$s of parties.

  匹配依据：MPC: multi party computation

  </details>

- **Homomorphic Secret Sharing with Verifiable Evaluation.**
  2025-08-18 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-78023-3_20) · [IACR ePrint](https://eprint.iacr.org/2025/1491)
  Aarushi Goel, Arka Rai Choudhuri, Aditya Hegde, Abhishek Jain

  <details><summary>摘要 / Abstract</summary>

  A homomorphic secret sharing (HSS) scheme allows a client to delegate a computation to a group of untrusted servers while achieving input privacy as long as at least one server is honest. In recent years, many HSS schemes have been constructed that have, in turn, found numerous applications to cryptography. Prior work on HSS focuses on the setting where the servers are semi-honest. In this work we study HSS in the setting of malicious evaluators. We propose the notion of HSS with verifiable evaluation (ve-HSS) that guarantees correctness of output even when all the servers are corrupted. ve-HSS retains all the attractive features of HSS and adds the new feature of succinct public verification of output. We present black-box constructions of ve-HSS by devising generic transformations for semi-honest HSS schemes (with negligible error). This provides a new non-interactive method for verifiable and private outsourcing of computation.

  匹配依据：MPC: secret sharing

  </details>

- **Ironman: Accelerating Oblivious Transfer Extension for Privacy-Preserving AI with Near-Memory Processing.**
  2025-07-22 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2507.16391) · [MICRO](https://doi.org/10.1145/3725843.3756025)
  Tianshi Xu, Runsheng Wang, Chenqi Lin, Zhaohui Chen, Kang Yang, Meng Li, Ling Liang, Mingyu Gao, Yufei Wang

  <details><summary>摘要 / Abstract</summary>

  With the wide application of machine learning (ML), privacy concerns arise with user data as they may contain sensitive information. Privacy-preserving ML (PPML) based on cryptographic primitives has emerged as a promising solution in which an ML model is directly computed on the encrypted data to provide a formal privacy guarantee. However, PPML frameworks heavily rely on the oblivious transfer (OT) primitive to compute nonlinear functions. OT mainly involves the computation of single-point correlated OT (SPCOT) and learning parity with noise (LPN) operations. As OT is still computed extensively on general-purpose CPUs, it becomes the latency bottleneck of modern PPML frameworks. In this paper, we propose a novel OT accelerator, dubbed Ironman, to significantly increase the efficiency of OT and the overall PPML framework. We observe that SPCOT is computation-bounded, and thus propose a hardware-friendly SPCOT algorithm with a customized accelerator to improve SPCOT computation throughput. In contrast, LPN is memory-bandwidth-bounded due to irregular memory access patterns. Hence, we further leverage the near-memory processing (NMP) architecture equipped with memory-side cache and index sorting to improve effective memory bandwidth. With extensive experiments, we demonstrate Ironman achieves a 39.2-237.4 times improvement in OT throughput across different NMP configurations compared to the full-thread CPU implementation. For different PPML frameworks, Ironman demonstrates a 2.1-3.4 times reduction in end-to-end latency for both CNN and Transformer models.

  匹配依据：MPC: oblivious transfer

  </details>

- **Private Set Intersection and other Set Operations in the Third Party Setting.**
  2025-07-21 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/yeo) · [IACR ePrint](https://eprint.iacr.org/2025/1328)
  Jason H. M. Ying, Foo Yee Yeo

  <details><summary>摘要 / Abstract</summary>

  We present a collection of protocols to perform privacy-preserving set operations in the third-party private set intersection (PSI) setting. This includes several protocols for multi-party third party PSI. In this model, there are multiple input parties (or clients) each holding a private set of elements and the receiver is an external party (termed as third-party) with no inputs. Multi-party third party PSI enables the receiver to learn only the intersection result of all input clients&#x27; private sets while revealing nothing else to the clients and the receiver. Our solutions include constructions that are provably secure against an arbitrary number of colluding parties in the semi-honest model. Additionally, we present protocols for third-party private set difference and private symmetric difference, whereby the learned output by the inputless third-party is the set difference and symmetric difference respectively of two other input parties, while preserving the same privacy guarantees. The motivation in the design of these protocols stems from their utilities in numerous real-world applications. We implemented our protocols and conducted experiments across various input and output set sizes.

  匹配依据：MPC: private set intersection

  </details>

- **Strong Secret Sharing with Snitching.**
  2025-06-13 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-032-01884-7_10) · [IACR ePrint](https://eprint.iacr.org/2025/1119)
  Tomasz Lizurej, Jan Bormet, Marcin Mielniczuk, Stefan Dziembowski, Sebastian Faust

  <details><summary>摘要 / Abstract</summary>

  One of the main shortcomings of classical distributed cryptography is its reliance on a certain fraction of participants remaining honest. Typically, honest parties are assumed to follow the protocol and not leak any information, even if behaving dishonestly would benefit them economically. More realistic models used in blockchain consensus rely on weaker assumptions, namely that no large coalition of corrupt parties exists, although every party can act selfishly. This is feasible since, in a consensus protocol, active misbehavior can be detected and &quot;punished&quot; by other parties. However, &quot;information leakage&quot;, where an adversary reveals sensitive information via, e.g., a subliminal channel, is often impossible to detect and, hence, much more challenging to handle. A recent approach to address this problem was proposed by Dziembowski, Faust, Lizurej, and Mielniczuk (ACM CCS 2024), who introduced a new notion called secret sharing with snitching. This primitive guarantees that as long as no large coalition of mutually trusting parties exists, every leakage of the shared secret produces a &quot;snitching proof&quot; indicating that some party participated in the illegal secret reconstruction. This holds in a very strong model, where mutually distrusting parties use an MPC protocol to reconstruct any information about the shared secret. Such a &quot;snitching proof&quot; can be sent to a smart contract (modeled as a &quot;judge&quot;) deployed on the blockchain, which punishes the aving party financially. In this paper, we extend the results from the work of CCS&#x27;24 by addressing its two main shortcomings. Firstly, we significantly strengthen the attack model by considering the case when mutually distrusting parties can also rely on a trusted third party (e.g., a smart contract). We call this new primitive strong secret sharing with snitching (SSSS). We present an SSSS protocol that is secure in this model. Secondly, unlike in the construction from CCS&#x27;24, our protocol does not require the honest parties to perform any MPC computations on hash functions. Besides its theoretical interest, this improvement is of practical importance, as it allows the construction of SSSS from any (even very &quot;MPC-unfriendly&quot;) hash function.

  匹配依据：MPC: secret sharing

  </details>

- **SEAF: Secure Evaluation on Activation Functions with Dynamic Precision for Secure Two-Party Inference.**
  2025-06-13 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/guo-hao-seaf) · [IACR ePrint](https://eprint.iacr.org/2025/1111)
  Ximing Fu, Zhusen Liu, Zhaoqian Liu, Hao Guo

  <details><summary>摘要 / Abstract</summary>

  Secure evaluation of non-linear functions is one of the most expensive operations in secure two-party computation, particularly for activation functions in privacy preserving machine learning (PPML). This work introduces SEAF, a novel framework for efficient Secure Evaluation on Activation Functions. SEAF is based on the linear approximation approach, but enhances it by introducing two key innovations: Trun-Eq based interval test protocols and linear approximation with dynamic precision, which have the potential for broader applicability. Furthermore, we classify common activation functions into several categories, and present specialized methods to evaluate them using our enhanced techniques. Our implementation of SEAF demonstrates $3.5 \times$ to $5.9 \times$ speedup on activation functions $\mathsf{Tanh}$ and $\mathsf{Sigmoid}$ compared to SirNN (S\&amp;P&#x27;21). When applied on $\mathsf{GELU}$, SEAF outperforms Iron (NeurIPS&#x27;22) by more than $10 \times$ and Bolt (S\&amp;P&#x27;24) by up to $3.4 \times$. For end-to-end secure inference on BERT, the original $\mathsf{GELU}$ accounts for $31.3 \%$ and $22.5 \%$ of the total runtime in Iron and Bolt, respectively. In contrast, our optimized $\mathsf{GELU}$ reduces these proportions to $4.3 \%$ and $9.8 \%$, eliminating $\mathsf{GELU}$ as a bottleneck in secure inference.

  匹配依据：MPC: secure evaluation, secure two party computation

  </details>

- **How to Make Any Computational Secret Sharing Scheme Adaptively Secure.**
  2025-06-02 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-032-01884-7_11) · [IACR ePrint](https://eprint.iacr.org/2025/1014)
  George Lu, Brent Waters

  <details><summary>摘要 / Abstract</summary>

  Secret sharing (SS) is a foundational cryptographic primitive with diverse applications, including secure multiparty computation and conditional disclosure of secrets. While traditional schemes have primarily emphasized information-theoretic security, recent advancements have increasingly leveraged computational assumptions to achieve more efficient constructions and support broader access policies. Despite these successes, most existing computational secret sharing (CSS) schemes are limited to a static security model, where adversaries must commit to their choice of corrupted participants at the outset. A critical challenge in CSS lies in achieving adaptive security, where adversaries can dynamically select participants to corrupt, better reflecting real-world threat models. In this paper, we present a novel transformation that converts any statically secure CSS scheme into an adaptively secure one while preserving the original access policy and computational assumptions, providing a framework for bridging the gap between static and adaptive security. Our construction introduces a multiplicative share size overhead of $O(n^2)$ where $n$ is the number of parties. Additionally, we explore trade-offs in efficiency and security, offering more efficient adaptive CSS constructions for specific, restricted policy classes. This work addresses key limitations in the current landscape of CSS and paves the way for broader adoption of adaptively secure secret sharing in cryptographic applications.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Scalable Multiparty Computation from Non-linear Secret Sharing.**
  2025-05-31 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-68397-8_12) · [IACR ePrint](https://eprint.iacr.org/2025/1007)
  Pratyay Mukherjee, Abhishek Jain, Sanjam Garg, Mingyuan Wang

  <details><summary>摘要 / Abstract</summary>

  A long line of work has investigated the design of scalable secure multiparty computation (MPC) protocols with computational and communication complexity independent of the number of parties (beyond any dependence on the circuit size). We present the first unconditionally-secure MPC protocols for arithmetic circuits over {\em large fields} with total computation $\mathcal{O}(|C|\log|F|)$, where $|C|$ and $|F|$ denote the circuit and field size, respectively. Prior work could either achieve similar complexity only in {\em communication}, or required highly structured circuits, or expensive circuit transformations. To obtain our results, we depart from the prior approach of share packing in linear secret-sharing schemes; instead, we use an ``unpacking&#x27;&#x27; approach via {\em non-linear} secret sharing.

  匹配依据：MPC: multiparty computation, secret sharing, secure multiparty computation

  </details>

- **NIZK Amplification via Leakage-Resilient Secure Computation.**
  2025-05-29 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-032-01907-3_15) · [IACR ePrint](https://eprint.iacr.org/2025/995)
  Eliran Kachlon, Benny Applebaum

  <details><summary>摘要 / Abstract</summary>

  Suppose that we are given a weak \emph{Non-Interactive Zero-Knowledge} (NIZK) proof system for NP with non-negligible soundness and zero-knowledge errors, denoted by $\alpha$ and $\beta$, respectively. Is it possible to to reduce these errors to a negligible level? This problem, known as NIZK amplification, was introduced by Goyal, Jain, and Sahai (Crypto&#x27;19) and was further studied by Bitansky and Geier (Crypto&#x27;24). The latter work provides amplification theorems for proofs and arguments, assuming the existence of one-way functions and public-key encryption, respectively. Unfortunately, their results only apply when the security level, $1 - (\alpha + \beta)$, is a constant bounded away from zero. Amplifying NIZK with an inverse polynomial security level remains an open problem and was stated as the main open question in both works. In this work, we resolve the NIZK amplification problem and show how to amplify any non-trivial NIZK proof system that has a noticeable, inverse-polynomial level of security. As in previous works, we amplify proofs and arguments assuming the existence of one-way functions and public-key encryption, respectively. Furthermore, assuming the existence of collision-resistant hash functions, we preserve, for the first time, properties such as statistical zero-knowledge and proof succinctness. Our main technical contribution is a new \emph{leakage-resilient secure multiparty} protocol that computes any public-output functionality with information-theoretic security against an adversary that corrupts an arbitrary subset of parties and obtains bounded leakage from each honest party. Our protocol operates in the pairwise correlated randomness model. Previous works relied on stronger setup assumptions in the form of $n$-wise correlations and either supported a smaller corruption threshold or suffered from an exponential dependency on the number of parties. To transform our protocol into a NIZK amplifier, we introduce a new intermediate notion of \emph{leakage-resilient NP secret sharing}, that may be of independent interest.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Lower Bounds for Garbled Circuits from Shannon-Type Information Inequalities.**
  2025-05-16 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-032-01884-7_19) · [IACR ePrint](https://eprint.iacr.org/2025/876)
  Lawrence Roy, Jake Januzelli, Mike Rosulek

  <details><summary>摘要 / Abstract</summary>

  We establish new lower bounds on the size of practical garbled circuits, which hold against any scheme satisfying the following simple properties: (1) Its security is based on symmetric-key cryptography only. More formally, security holds in Minicrypt, a model in which a random oracle is the only available source of cryptography. (2) The evaluation algorithm makes non-adaptive queries to the random oracle. (3) The evaluation algorithm &quot;knows&quot; which of its oracle queries are made by which other input combinations. These restrictions are reasonable for garbling single gates. In particular, unlike prior attempts at lower bounds, we make no assumptions about the internal behavior of the garbling algorithms --- i.e., how it uses random oracle outputs and wire labels to compute the garbled gate, etc. We prove separate lower bounds depending on whether the scheme uses the free-XOR technique (Kolesnikov &amp; Schneider, ICALP 2008). In the free-XOR case, we prove that a garbled AND-gate requires $1.5\lambda$ bits; thus, the garbling scheme of Rosulek &amp; Roy (Crypto 2022) is optimal. In the non-free-XOR case, we prove that a garbled AND-gate requires $2\lambda$ bits and a garbled XOR-gate requires $\lambda$ bits; thus, the garbling scheme of Gueron, Lindell, Nof, and Pinkas (CCS 2015) is optimal. We prove our lower bounds using tools from information theory. A garbling scheme can be characterized as a joint distribution over various quantities: wire labels, garbled gate information, random oracle responses. We show that different properties of a garbling scheme imply certain Shannon-type information inequalities about this distribution. We then use an automated theorem prover for Shannon-type inequalities to prove that our inequalities imply lower bounds on the entropy---hence, size---of the garbled gate information.

  匹配依据：MPC: garbled circuits, garbling scheme

  </details>

- **Fast Enhanced Private Set Union in the Balanced and Unbalanced Scenarios.**
  2025-05-09 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/tu) · [IACR ePrint](https://eprint.iacr.org/2025/827)
  Cong Zhang, Yujie Bai, Yang Cao, Binbin Tu, Yu Chen

  <details><summary>摘要 / Abstract</summary>

  Private set union (PSU) allows two parties to compute the union of their sets without revealing anything else. It can be categorized into balanced and unbalanced scenarios depending on the size of the set on both sides. Recently, Jia et al. (USENIX Security 2024) highlight that existing scalable PSU solutions suffer from during-execution leakage and propose a PSU with enhanced security for the balanced setting. However, their protocol&#x27;s complexity is superlinear with the size of the set. Thus, the problem of constructing a linear enhanced PSU remains open, and no unbalanced enhanced PSU exists. In this work, we address these two open problems: -Balanced case: We propose the first linear enhanced PSU. Compared to the state-of-the-art enhanced PSU (Jia et al., USENIX Security 2024), our protocol achieves a $2.2 - 8.8\times$ reduction in communication cost and a $1.2 - 8.6\times$ speedup in running time, depending on set sizes and network environments. -Unbalanced case: We present the first unbalanced enhanced PSU, which achieves sublinear communication complexity in the size of the large set. Experimental results demonstrate that the larger the difference between the two set sizes, the better our protocol performs. For unbalanced set sizes $(2^{10},2^{20})$ with single thread in $1$Mbps bandwidth, our protocol requires only $2.322$ MB of communication. Compared with the state-of-the-art enhanced PSU, there is $38.1\times$ shrink in communication and roughly $17.6\times$ speedup in the running time.

  匹配依据：MPC: private set union

  </details>

- **Actively Secure MPC in the Dishonest Majority Setting: Achieving Constant Complexity in Online Communication, Computation Per Gate, Rounds, and Private Input Size.**
  2025-05-06 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-032-01884-7_4) · [IACR ePrint](https://eprint.iacr.org/2025/810)
  Jaesang Noh, Dohyuk Kim, Seung-Hwan Lee, Dong-Joon Shin, Taejeong Kim, Seunghwan Lee

  <details><summary>摘要 / Abstract</summary>

  SPDZ-style and BMR-style protocols are widely known as practical MPC protocols that achieve active security in the dishonest majority setting. However, to date, SPDZ-style protocols have not achieved constant rounds, and BMR-style protocols have struggled to achieve scalable communication or computation. Additionally, there exists fully homomorphic encryption (FHE)-based MPC protocols that achieve both constant rounds and scalable communication, but they face challenges in achieving active security in the dishonest majority setting and are considered impractical due to computational inefficiencies. In this work, we propose an MPC framework that constructs an efficient and scalable FHE-based MPC protocol by integrating a linear secret sharing scheme (LSSS)-based MPC and FHE. The resulting FHE-based MPC protocol achieves active security in the dishonest majority setting and constant complexity in online communication, computation per gate, rounds, and private input size. Notably, when instantiated with the SPDZ protocol and gate FHE for the framework, the resulting FHE-based MPC protocol efficiently achieves active security in the dishonest majority setting by using SPDZ-style MAC and ensures the computation per gate time within 3 ms. Moreover, its offline phase achieves scalable communication and computation, both of which grow linearly with the number of parties $n$. In other words, the proposed FHE-based MPC preserves the key advantages of existing FHE-based MPCs and simultaneously overcomes the weaknesses of them. As a result, the proposed FHE-based MPC is a highly practical and secure like SPDZ-style and BMR-style protocols. For the first time, we introduce the concept of circuit-privacy, which ensures that external adversaries who eavesdrop on communications do not obtain information about the circuit. We rigorously prove that our construction inherently satisfy circuit- privacy, thereby establishing a novel security option for MPC.

  匹配依据：MPC: secret sharing

  </details>

- **Rushing at SPDZ: On the Practical Security of Malicious MPC Implementations.**
  2025-05-03 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP61157.2025.00176) · [IACR ePrint](https://eprint.iacr.org/2025/789)
  Sabine Oechsner, Peter Scholl, Frederik Huss Nielsen, Alexander Kyster

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) enables parties to compute a function over private inputs while maintaining confidentiality. Although MPC has advanced significantly and attracts a growing industry interest, open-source implementations are still at an early stage, with no production-ready code and a poor understanding of their actual security guarantees. In this work, we study the real-world security of modern MPC implementations, focusing on the SPDZ protocol (Damgård et al., CRYPTO 2012, ESORICS 2013), which provides security against malicious adversaries when all-but-one of the participants may be corrupted. We identify a novel type of MAC key leakage in the MAC check protocol of SPDZ, which can be exploited in concurrent, multi-threaded settings, compromising output integrity and, in some cases, input privacy. In our analysis of three SPDZ implementations (MP-SPDZ, SCALE-MAMBA, and FRESCO), two are vulnerable to this attack, while we also uncover further issues and vulnerabilities with all implementations. We propose mitigation strategies and some recommendations for researchers, developers and users, which we hope can bring more awareness to these issues and avoid them reoccurring in future.

  匹配依据：MPC: secure multi party computation

  </details>

- **PULSE: Parallel Private Set Union for Large-Scale Entities.**
  2025-05-03 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3719027.3765108) · [IACR ePrint](https://eprint.iacr.org/2025/790)
  Ni Trieu, Jiahui Gao, Marina Blanton, Son Nguyen

  <details><summary>摘要 / Abstract</summary>

  Multi-party private set union (mPSU) allows multiple parties to compute the union of their private input sets without revealing any additional information. Existing efficient mPSU protocols can be categorized into symmetric key encryption (SKE)-based and public key encryption (PKE)-based approaches. However, neither type of mPSU protocol scales efficiently to a large number of parties, as they fail to fully utilize available computational resources, leaving participants idle during various stages of the protocol execution. This work examines the limitation of existing protocols and proposes a unified framework for designing efficient mPSU protocols. We then introduce an efficient Parallel mPSU for Large-Scale Entities (PULSE) that enables parallel computation, allowing all parties/entities to perform computations without idle time, leading to significant efficiency improvements, particularly as the number of parties increases. Our protocol is based on PKE and secure even when up to $n-1$ semi-honest parties are corrupted. We implemented PULSE and compared it to state-of-the-art mPSU protocols under different settings, showing a speedup of $1.91$ to $3.57\times$ for $n=8$ parties for various set sizes.

  匹配依据：MPC: private set union

  </details>

- **SHARK: Actively Secure Inference Using Function Secret Sharing.**
  2025-04-21 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP61157.2025.00175) · [IACR ePrint](https://eprint.iacr.org/2025/716)
  Rahul Sharma, Kanav Gupta, Nishanth Chandran, Divya Gupta, Jonathan Katz

  <details><summary>摘要 / Abstract</summary>

  We consider the problem of actively secure two-party machine-learning inference in the preprocessing model, where the parties obtain (input-independent) correlated randomness in an offline phase that they can then use to run an efficient protocol in the (input-dependent) online phase. In this setting, the state-of-the-art is the work of Escudero et al. (Crypto 2020); unfortunately, that protocol requires a large amount of correlated randomness, extensive communication, and many rounds of interaction, which leads to poor performance. In this work, we show protocols for this setting based on function secret sharing (FSS) that beat the state-of-the-art in all parameters: they use less correlated randomness and fewer rounds, and require lower communication and computation. We achieve this in part by allowing for a mix of boolean and arithmetic values in FSS-based protocols (something not done in prior work), as well as by relying on “interactive FSS,” a generalization of FSS we introduce. To demonstrate the effectiveness of our approach we build SHARK—the first FSS- based system for actively secure inference—which outperforms the state-of-the-art by up to 2300×.

  匹配依据：MPC: secret sharing

  </details>

- **Charge Your Clients: Payable Secure Computation and Its Applications.**
  2025-04-07 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2025.3559456) · [IACR ePrint](https://eprint.iacr.org/2025/630)
  Meng Hao, Weiran Liu, Cong Zhang, Liqiang Peng, Shuaishuai Li, Dongdai Lin, Lei Zhang

  <details><summary>摘要 / Abstract</summary>

  The online realm has witnessed a surge in the buying and selling of data, prompting the emergence of dedicated data marketplaces. These platforms cater to servers (sellers), enabling them to set prices for access to their data, and clients (buyers), who can subsequently purchase these data, thereby streamlining and facilitating such transactions. However, the current data market is primarily confronted with the following issues. Firstly, they fail to protect client privacy, presupposing that clients submit their queries in plaintext. Secondly, these models are susceptible to being impacted by malicious client behavior, for example, enabling clients to potentially engage in arbitrage activities. To address the aforementioned issues, we propose payable secure computation, a novel secure computation paradigm specifically designed for data pricing scenarios. It grants the server the ability to securely procure essential pricing information while protecting the privacy of client queries. Additionally, it fortifies the server&#x27;s privacy against potential malicious client activities. As specific applications, we have devised customized payable protocols for two distinct secure computation scenarios: Keyword Private Information Retrieval (KPIR) and Private Set Intersection (PSI). We implement our two payable protocols and compare them with the state-of-the-art related protocols that do not support pricing as a baseline. Since our payable protocols are more powerful in the data pricing setting, the experiment results show that they do not introduce much overhead over the baseline protocols. Our payable KPIR achieves the same online cost as baseline, while the setup is about $1.3-1.6\times$ slower than it. Our payable PSI needs about $2\times$ more communication cost than that of baseline protocol, while the runtime is $1.5-3.2\times$ slower than it depending on the network setting.

  匹配依据：MPC: private set intersection, secure computation

  </details>

- **Highly Efficient Actively Secure Two-Party Computation with One-Bit Advantage Bound.**
  2025-04-04 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP61157.2025.00183) · [IACR ePrint](https://eprint.iacr.org/2025/614)
  Junzuo Lai, Qi Wang, Anjia Yang, Yi Liu, Siu-Ming Yiu, Peng Yang, Jian Weng

  <details><summary>摘要 / Abstract</summary>

  Secure two-party computation (2PC) enables two parties to jointly evaluate a function while maintaining input privacy. Despite recent significant progress, a notable efficiency gap remains between actively secure and passively secure protocols. In S\&amp;P&#x27;12, Huang, Katz, and Evans formalized the notion of \emph{active security with one-bit leakage}, providing a promising approach to bridging this gap. Protocols derived from this notion have become foundational in designing highly efficient actively secure 2PC protocols. However, a critical challenge identified by Huang, Katz, and Evans remains unexplored: these protocols face significant weaknesses in ensuring fairness for honest parties when employed in standalone settings rather than as components within larger protocols. While the authors proposed two potential solutions to mitigate this issue, both approaches are prohibitively expensive and lack formalization of security guarantees. In this paper, we first formally define an enhanced notion called \emph{active security with one-bit-advantage bound}, in which the adversaries&#x27; advantages are strictly bounded to at most one bit beyond what honest parties obtain. This bound is enforced through a \emph{progressive revelation} mechanism, where the evaluation result is disclosed incrementally bit by bit. In addition, we propose a novel approach leveraging label structures within garbled circuits to design a highly efficient constant-round 2PC protocol that achieves active security with one-bit advantage bound. Our protocol demonstrates \emph{runtime performance nearly identical to that of passively secure garbled-circuit counterparts} in duplex networks (\eg $1.033\times$ for the {\tt SHA256} circuit in LAN), with \emph{low overhead} for output progressive revelation (only $80$ communicated bytes per bit release). With its strengthened security guarantees and minimal overhead, our protocol is highly suitable for practical 2PC applications.

  匹配依据：MPC: garbled circuit, garbled circuits, secure two party computation

  </details>

- **Black-Box Constant-Round Secure 2PC with Succinct Communication.**
  2025-03-12 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-91092-0_13) · [IACR ePrint](https://eprint.iacr.org/2025/474)
  Michele Ciampi, Akash Shah, Ankit Kumar Misra, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  The most fundamental performance metrics of secure multi-party computation (MPC) protocols are related to the number of messages the parties exchange (i.e., round complexity), the size of these messages (i.e., communication complexity), and the overall computational resources required to execute the protocol (i.e., computational complexity). Another quality metric of MPC protocols is related to the black-box or non-black-box use of the underlying cryptographic primitives. Indeed, the design of black-box MPC protocols, other than being of theoretical interest, usually can lead to protocols that have better computational complexity. In this work, we aim to optimize the round and communication complexity of black-box secure multi-party computation in the plain model, by designing a constant-round two-party computation protocol in the malicious setting, whose communication complexity is only polylogarithmic in the size of the function being evaluated. We successfully design such a protocol, having only black-box access to fully homomorphic encryption, trapdoor permutations, and hash functions. To the best of our knowledge, our protocol is the first to make black-box use of standard cryptographic primitives while achieving almost asymptotically optimal communication and round complexity.

  匹配依据：MPC: secure multi party computation, two party computation

  </details>

- **Disincentivize Collusion in Verifiable Secret Sharing.**
  2025-03-09 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-031-91092-0_2) · [IACR ePrint](https://eprint.iacr.org/2025/446)
  Hai H. Nguyen, Aniket Kate, Tiantian Gong, Hemanta K. Maji

  <details><summary>摘要 / Abstract</summary>

  In verifiable secret sharing (VSS), a dealer shares a secret input among several parties, ensuring each share is verifiable. Motivated by its applications in the blockchain space, we focus on a VSS where parties holding shares are not allowed to reconstruct the dealer&#x27;s secret (even partially) on their own terms, which we address as privacy-targeted collusion if attempted. In this context, our work investigates mechanisms deterring such collusion in VSS among rational and malicious parties. For this problem, we make both algorithmic and combinatorial contributions: 1. We provide two collusion-deterrent mechanisms to discourage parties from colluding and recovering the dealer&#x27;s secret. Notably, when it is desired to achieve fairness---where non-colluding parties are not at a loss---while allowing for the best achievable malicious fault tolerance, we define ``trackable access structures&#x27;&#x27; (TAS) and design a deterrence mechanism tailored for VSS on these structures. 2. We estimate the size of the optimal TAS, construct them from Steiner systems, provide highly robust TAS using partial Steiner systems, and present efficient secret sharing schemes for the latter close-to-optimal TAS for various parameter regimes. 3. We demonstrate that trackability in access structures is connected to combinatorial objects like (partial) Steiner systems, uniform subsets with restricted intersections, and appropriate binary codes. The robustness of access structures is equivalent to the minimum vertex cover of hypergraphs. We believe these connections between cryptography, game theory, and discrete mathematics will be of broader interest.

  匹配依据：MPC: secret sharing

  </details>

- **A Unified Framework for Succinct Garbling from Homomorphic Secret Sharing.**
  2025-03-07 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-032-01884-7_13) · [IACR ePrint](https://eprint.iacr.org/2025/442)
  Yuval Ishai, Hanjun Li, Huijia Lin

  <details><summary>摘要 / Abstract</summary>

  A major challenge in cryptography is the construction of succinct garbling schemes that have asymptotically smaller size than Yao’s garbled circuit construction. We present a new framework for succinct garbling that replaces the heavy machinery of most previous constructions by lighter-weight homomorphic secret sharing techniques. Concretely, we achieve 1-bit-per-gate (amortized) garbling size for Boolean circuits under circular variants of standard assumptions in composite-order or prime-order groups, as well as a lattice-based instantiation. We further extend these ideas to layered circuits, improving the per-gate cost below 1 bit, and to arithmetic circuits, eliminating the typical Ω(λ)-factor overhead for garbling mod-p computations. Our constructions also feature “leveled” variants that remove circular-security requirements at the cost of adding a depth-dependent term to the garbling size. Our framework significantly extends a recent technique of Liu, Wang, Yang, and Yu (Eurocrypt 2025) for lattice-based succinct garbling, and opens new avenues toward practical succinct garbling. For moderately large circuits with a few million gates, our garbled circuits can be two orders of magnitude smaller than Yao-style garbling. While our garbling and evaluation algorithms are much slower, they are still practically feasible, unlike previous fully succinct garbling schemes that rely on expensive tools such as iO or a non-black-box combination of FHE and ABE. This trade-off can make our framework appealing when a garbled circuit is used as a functional ciphertext that is broadcast or stored in multiple locations (e.g., on a blockchain), in which case communication and storage may dominate computational cost.

  匹配依据：MPC: garbled circuit, garbled circuits, garbling schemes, secret sharing

  </details>

- **Leap: A Fast, Lattice-Based OPRF with Application to Private Set Intersection.**
  2025-02-24 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-031-91098-2_10) · [IACR ePrint](https://eprint.iacr.org/2025/333)
  Daniel Kales, Omid Mir, Sebastian Ramacher, Lena Heimberger, Riccardo Lolato, Christian Rechberger

  <details><summary>摘要 / Abstract</summary>

  Oblivious pseudorandom functions (OPRFs) are an important primitive in privacy-preserving cryptographic protocols. The growing interest in OPRFs, both in theory and practice, has led to the development of numerous constructions and variations. However, most of these constructions rely on classical assumptions. Potential future quantum attacks may limit the practicality of those OPRFs for real-world applications. To close this gap, we introduce Leap, a novel OPRF based on heuristic lattice assumptions. Fundamentally, Leap builds upon the Spring [BBL+15] pseudorandom function (PRF), which relies on the learning with rounding assumption, and integrates techniques from multi-party computation, specifically Oblivious Transfer (OT) and Oblivious Linear Evaluation (OLE). With this combination of oblivious protocols, we construct an OPRF that evaluates in less than a millisecond on a modern computer. Efficiency-wise, our prototype implementation achieves computation times of just 11 microseconds for the client and 750 microseconds for the server, excluding some base OT preprocessing overhead. Moreover, Leap requires an online communication cost of 23 kB per evaluation, where the client only has to send around 380 bytes online. To demonstrate the practical applicability of Leap, we present an efficient private set intersection (PSI) protocol built on top of Leap. This application highlights the potential for the integration of Leap into various privacy-preserving applications: We can compute an unbalanced set intersection with set sizes of 2^24 and 2^15 in under a minute of online time and just over two minutes overall.

  匹配依据：MPC: multi party computation, oblivious transfer, private set intersection

  </details>

- **On the Adaptive Security of Free-XOR-Based Garbling Schemes in the Plain Model.**
  2025-02-23 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-031-91095-1_8) · [IACR ePrint](https://eprint.iacr.org/2025/326)
  Karen Azari, Chethan Kamath, Anasuya Acharya

  <details><summary>摘要 / Abstract</summary>

  A Garbling Scheme is a fundamental cryptographic primitive, with numerous theoretical and practical applications. Since its inception by Yao (FOCS&#x27;82, &#x27;86), optimizing the communication and computation complexities of securely garbling circuits has been an area of active research. One such optimization, and perhaps the most fundamental, is the `Free-XOR&#x27; technique (Kolesnikov and Schneider, ICALP&#x27;08) which allows XOR gates in a function garbling to not require representation, and therefore communication. Since then, several works have designed and analysed the security of schemes that adopt the Free-XOR optimisation. In particular: (1) Applebaum (JoC&#x27;16) proved that this can be securely instantiated assuming symmetric-key encryption satisfying a notion called RK-KDM security; and (2) Zahur, Rosulek and Evans (Eurocrypt&#x27;15) proposed the so-called `Half Gates&#x27; scheme, and proved that it can be instantiated assuming hash functions satisfying a notion called CCR security. Although both schemes have been proven selectively secure, prior work leaves it open to analyze whether they satisfy a stronger security notion -- adaptive security -- in the plain model. In this work, we formally show that the selective security of these two schemes cannot be lifted to adaptive security under the same assumptions. To establish these barriers, we adopt techniques from the work of Kamath et al (Crypto&#x27;21), who proved similar negative results for Yao&#x27;s garbling. We use that as a starting point and introduce new techniques tailored towards addressing Free-XOR-based schemes.

  匹配依据：MPC: garbling circuits, garbling scheme, garbling schemes

  </details>

- **Computationally Differentially Private Inner-Product Protocols Imply Oblivious Transfer.**
  2025-02-21 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2502.15629) · [series/lncs](https://doi.org/10.1007/978-3-032-01884-7_6)
  Eliad Tsfadia, Jad Silbak, Iftach Haitner, Noam Mazor, Chao Yan

  <details><summary>摘要 / Abstract</summary>

  In distributed differential privacy, multiple parties collaborate to analyze their combined data while each party protects the confidentiality of its data from the others. Interestingly, for certain fundamental two-party functions, such as the inner product and Hamming distance, the accuracy of distributed solutions significantly lags behind what can be achieved in the centralized model. For computational differential privacy, however, these limitations can be circumvented using oblivious transfer (used to implement secure multi-party computation). Yet, no results show that oblivious transfer is indeed necessary for accurately estimating a non-Boolean functionality. In particular, for the inner-product functionality, it was previously unknown whether oblivious transfer is necessary even for the best possible constant additive error. In this work, we prove that any computationally differentially private protocol that estimates the inner product over $\{-1,1\}^n \times \{-1,1\}^n$ up to an additive error of $O(n^{1/6})$, can be used to construct oblivious transfer. In particular, our result implies that protocols with sub-polynomial accuracy are equivalent to oblivious transfer. In this accuracy regime, our result improves upon Haitner, Mazor, Silbak, and Tsfadia [STOC &#x27;22], who showed that a key-agreement protocol is necessary.

  匹配依据：MPC: oblivious transfer, secure multi party computation

  </details>

- **The Round Complexity of Black-Box Post-quantum Secure Computation.**
  2025-02-19 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2502.13830) · [series/lncs](https://doi.org/10.1007/978-3-032-01884-7_1) · [IACR ePrint](https://eprint.iacr.org/2025/250)
  Rohit Chatterjee, Takashi Yamakawa, Xiao Liang, Omkant Pandey

  <details><summary>摘要 / Abstract</summary>

  We study the round-complexity of secure multi-party computation (MPC) in the post-quantum regime where honest parties and communication channels are classical but the adversary can be a quantum machine. Our focus is on the $\mathit{fully}$ black-box setting where both the construction as well as the security reduction are black-box in nature. In this context, Chia, Chung, Liu, and Yamakawa [FOCS&#x27;22] demonstrated the infeasibility of achieving standard simulation-based security within constant rounds, unless $\mathbf{NP} \subseteq \mathbf{BQP}$. This outcome leaves crucial feasibility questions unresolved. Specifically, it remains unknown whether black-box constructions are achievable within polynomial rounds; additionally, the existence of constant-round constructions with respect to $\epsilon$-$\mathit{simulation}$, a relaxed yet useful alternative to the standard simulation notion, remains unestablished. This work provides positive answers to the aforementioned questions. We introduce the first black-box construction for post-quantum MPC in polynomial rounds, from the minimal assumption of post-quantum semi-honest oblivious transfers. In the two-party scenario, our construction requires only $\omega(1)$ rounds. These results have already found application in the oracle separation between classical-communication quantum MPC and $\mathbf{P} = \mathbf{NP}$ in the recent work of Kretschmer, Qian, and Tal [STOC&#x27;25]. As for $\epsilon$-simulation, Chia, Chung, Liang, and Yamakawa [CRYPTO&#x27;22] resolved the issue for the two-party setting, leaving the general multi-party setting as an open question. We complete the picture by presenting the first black-box and constant-round construction in the multi-party setting. Our construction can be instantiated using various standard post-quantum primitives including lossy public-key encryption, linearly homomorphic public-key encryption, or dense cryptosystems. En route, we obtain a black-box and constant-round post-quantum commitment that achieves a weaker version of the standard 1-many non-malleability, from the minimal assumption of post-quantum one-way functions. Besides its utility in our post-quantum MPC construction, this commitment scheme also reduces the assumption used in the lower bound of quantum parallel repetition recently established by Bostanci, Qian, Spooner, and Yuen [STOC&#x27;24]. We anticipate that it will find more applications in the future.

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **10-Party Sublinear Secure Computation from Standard Assumptions.**
  2025-02-18 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-68400-5_2) · [IACR ePrint](https://eprint.iacr.org/2025/269)
  Geoffroy Couteau, Naman Kumar

  <details><summary>摘要 / Abstract</summary>

  Secure computation enables mutually distrusting parties to jointly compute a function on their secret inputs, while revealing nothing beyond the function output. A long-running challenge is understanding the required communication complexity of such protocols – in particular, when communication can be sublinear in the circuit representation size of the desired function. While several techniques have demonstrated the viability of sublinear secure computation in the two-party setting, known methods for the corresponding multi-party setting rely either on fully homomorphic encryption, non-standard hardness assumptions, or are limited to a small number of parties. In this work, we expand the study of multi-party sublinear secure computation by demonstrating sublinear-communication 10-party computation from various combinations of standard hardness assumptions. In particular, our contributions show: – 8-party homomorphic secret sharing under the hardness of (DDH or DCR), the superpolynomial hardness of LPN, and the existence of constant-depth pseudorandom generators; – A general framework for achieving (N + M )-party sublinear secure computation using M-party homomorphic secret sharing for NC1 and correlated symmetric PIR. Together, our constructions imply the existence of a 10-party MPC protocol with sublinear computation. At the core of our techniques lies a novel series of computational approaches based on homomorphic secret sharing.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Silent Circuit Relinearisation: Sublinear-Size (Boolean and Arithmetic) Garbled Circuits from DCR.**
  2025-02-16 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-032-01884-7_14) · [IACR ePrint](https://eprint.iacr.org/2025/245)
  Peter Scholl, Lawrence Roy, Pierre Meyer, Claudio Orlandi

  <details><summary>摘要 / Abstract</summary>

  We introduce a general template for building garbled circuits with low communication, assuming decisional composite residuosity (DCR) and a circular security assumption. For the case of layered Boolean circuits, we can garble a circuit of size $s$ with communication proportional to $O(s/\log\log s)$ bits, plus an additive factor that is polynomial in the security parameter. For layered arithmetic circuits with $B$-bounded integer computation, we obtain a similar result: the garbled arithmetic circuit has size $O(s/\log\log s) \cdot (\lambda + \log B)$ bits, where $\lambda$ is the security parameter. In both cases, we can remove the circular security assumption by adding a term proportional to the circuit depth. These are the first constructions of general-purpose, garbled circuits with sublinear size, without relying on heavy tools like indistinguishability obfuscation or attribute-based and fully homomorphic encryption. To achieve these results, our main technical tool is a new construction of a form of homomorphic secret sharing (HSS) where some of the inputs are semi-private, that is, known to one of the evaluating parties. Through a new relinearisation technique that allows performing arbitrary additions and multiplications on semi-private shares, we build such an HSS scheme that supports evaluating any function of the form $C(x) \cdot C&#x27;(y)$, where $C$ is any polynomially-sized circuit applied to the semi-private input $x$, and $C&#x27;$ is a restricted-multiplication (or, NC1) circuit applied to the private input $y$. This significantly broadens the expressiveness of known HSS constructions.

  匹配依据：MPC: garbled circuits, secret sharing

  </details>

- **Doubly Efficient Cryptography: Commitments, Arguments and RAM MPC.**
  2025-02-14 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-68397-8_8) · [IACR ePrint](https://eprint.iacr.org/2025/235)
  Wei-Kai Lin, Ethan Mook, Daniel Wichs

  <details><summary>摘要 / Abstract</summary>

  Can a sender commit to a long input without even reading all of it? Can a prover convince a verifier that an NP statement holds without even reading the entire witness? Can a set of parties run a multiparty computation (MPC) protocol in the RAM model, without necessarily even reading their entire inputs? We show how to construct such &quot;doubly efficient&quot; schemes in a setting where parties can preprocess their input offline, but subsequently they can engage in many different protocol executions over this input in sublinear online time. We do so in the plain model, without any common setup. Our constructions rely on doubly efficient private information retrieval (DEPIR) as a building block and can be instantiated based on Ring LWE. In more detail, we begin by constructing doubly efficient (interactive) commitments, where the sender preprocesses the input offline, and can later commit to this input to arbitrary receivers in sublinear online time. Moreover, the sender can open individual bits of the committed input in sublinear time. We then use these commitments to implement doubly succinct (interactive) arguments, where the prover preprocesses the statement/witness offline, and can subsequently run many proof protocols to convince arbitrary verifiers of the statement&#x27;s validity in sublinear online time. Furthermore, we augment these to get a doubly efficient &quot;commit, prove and locally open&quot; protocol, where the prover can commit to a long preprocessed input, prove that it satisfies some global property, and locally open individual bits, all in sublinear time. Finally, we leverage these tools to construct a RAM-MPC with malicious security in the plain model. Each party individually preprocesses its input offline, and can then run arbitrary MPC executions over this input with arbitrary other parties. The online run-time of each MPC execution is only proportional to the RAM run-time of the underlying program, that can be sublinear in the input size.

  匹配依据：MPC: multiparty computation

  </details>

- **Authenticated BitGC for Actively Secure Rate-One 2PC.**
  2025-02-14 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-032-01884-7_21) · [IACR ePrint](https://eprint.iacr.org/2025/232)
  Hanlin Liu, Xiao Wang, Yu Yu, Kang Yang

  <details><summary>摘要 / Abstract</summary>

  In this paper, we present a constant-round actively secure two-party computation protocol with small communication based on the ring learning with errors (RLWE) assumption with key-dependent message security. Our result builds on the recent BitGC protocol by Liu, Wang, Yang, and Yu (Eurocrypt 2025) with communication of one bit per gate for semi-honest security. First, we achieve a different manner of distributed garbling, where the global correlation is secret-shared among the two parties. The garbler always and only holds the garbled labels corresponding to the wire values when all inputs are zero, while the evaluator holds the labels corresponding to the real evaluation. In the second phase, we run an authentication protocol that requires some extra communication, which allows two parties to check the correct computation of each gate by treating the ciphertext as commitments, now that the global key is distributed. For layered circuits, the extra communication for authentication is $o(1)$ bits per gate, resulting in total communication of $1+o(1)$ bits per gate. For generic circuits, the extra communication cost can be $1$ bit per gate in the worst case, and thus, the total communication cost would be 2 bits per gate.

  匹配依据：MPC: secure two party computation

  </details>

- **Improved Secure Two-party Computation from a Geometric Perspective.**
  2025-02-11 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/guo-hao-improved) · [IACR ePrint](https://eprint.iacr.org/2025/200)
  Liqiang Peng, Lei Hu, Haiyang Xue, Weiran Liu, Hao Guo, Zhe Liu, Li Peng

  <details><summary>摘要 / Abstract</summary>

  Multiplication and other non-linear operations are widely recognized as the most costly components of secure two-party computation (2PC) based on linear secret sharing. Multiplication and non-linear operations are well known to be the most expensive protocols in secure two-party computation (2PC). Moreover, the comparison protocol (or $\mathsf{Wrap}$ protocol) is essential for various operations such as truncation, signed extension, and signed non-uniform multiplication. This paper aims to optimize these protocols by avoiding invoking the costly comparison protocol, thereby improving their efficiency. We propose a novel approach to study 2PC from a geometric perspective. Specifically, we interpret the two shares of a secret as the horizontal and vertical coordinates of a point in a Cartesian coordinate system, with the secret itself represented as the corresponding point. This reformulation allows us to address the comparison problem by determining the region where the point lies. Furthermore, we identify scenarios where the costly comparison protocol can be replaced by more efficient evaluating AND gate protocols within a constrained range. Using this method, we improve protocols for truncation, signed extension and signed non-uniform multiplication, all of which are fundamental to 2PC. In particular, for the one-bit error truncation protocol and signed extension protocols, we reduce the state-of-the-art communication complexities of Cheetah (USENIX’22) and SirNN (S\&amp;P’21) from $\approx \lambda (l + 1)$ to $\approx \lambda$ in two rounds, where $l$ is the input length and $\lambda$ is the security parameter. For signed multiplication with non-uniform bit-width, we reduce the communication cost of SirNN&#x27;s by 40\% to 60\%.

  匹配依据：MPC: secret sharing, secure two party computation

  </details>

- **Efficient Mixed Garbling from Homomorphic Secret Sharing and GGM-Tree.**
  2025-02-11 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-031-91095-1_6) · [IACR ePrint](https://eprint.iacr.org/2025/207)
  Wenjie Nan, Jian Guo

  <details><summary>摘要 / Abstract</summary>

  We present new techniques for garbling mixed arithmetic and boolean circuits, utilizing the homomorphic secret sharing scheme introduced by Roy \&amp; Singh (Crypto 2021), along with the half-tree protocol developed by Guo et al (Eurocrypt 2023). Compared to some two-party interactive protocols, our mixed garbling only requires several times $(&lt;10)$ more communication cost. We construct the bit decomposition/composition gadgets with communication cost $O((\lambda+\lambda_{\text{DCR}}/k)b)$ for integers in the range $(-2^{b-1}, 2^{b-1})$, requiring $O(2^k)$ computations for the GGM-tree. Our approach is compatible with constant-rate multiplication protocols, and the cost decreases as $k$ increases. Even for a small $k=8$, the concrete efficiency ranges from $6\lambda b$ ($b \geq 1000$ bits) to $9\lambda b$ ($b \sim 100$ bits) per decomposition/composition. In addition, we develop the efficient gadgets for mod $q$ and unsigned truncation based on bit decomposition and composition. We construct efficient arithmetic gadgets over various domains. For bound integers, we improve the multiplication rate in the work of Meyer et al. (TCC 2024) from $\textstyle\frac{\zeta-2}{\zeta+1}$ to $\frac{\zeta-2}{\zeta}$. We propose new garbling schemes over other domains through bounded integers with our modular and truncation gadgets, which is more efficient than previous constructions. For $\mathbb{Z}_{2^b}$, additions and multiplication can be garbled with a communication cost comparable to our bit decomposition. For general finite field $\mathbb{F}_{p^n}$, particularly for large values of $p$ and $n$, we garble the addition and multiplication at the cost of $O((\lambda+\lambda_{\text{DCR}}/k)b)$, where $b = n\lceil \log p \rceil$. For applications to real numbers, we introduce an ``error-based&#x27;&#x27; truncation that makes the cost of multiplication dependent solely on the desired precision.

  匹配依据：MPC: garbling schemes, secret sharing

  </details>

- **Enabling Low-Cost Secure Computing on Untrusted In-Memory Architectures.**
  2025-01-28 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2501.17292) · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/ghinani)
  Elaheh Sadredini, Jingyao Zhang, Sahar Ghoflsaz Ghinani

  <details><summary>摘要 / Abstract</summary>

  Modern computing systems are limited in performance by the memory bandwidth available to processors, a problem known as the memory wall. Processing-in-Memory (PIM) promises to substantially improve this problem by moving processing closer to the data, improving effective data bandwidth, and leading to superior performance on memory-intensive workloads. However, integrating PIM modules within a secure computing system raises an interesting challenge: unencrypted data has to move off-chip to the PIM, exposing the data to attackers and breaking assumptions on Trusted Computing Bases (TCBs). To tackle this challenge, this paper leverages multi-party computation (MPC) techniques, specifically arithmetic secret sharing and Yao&#x27;s garbled circuits, to outsource bandwidth-intensive computation securely to PIM. Additionally, we leverage precomputation optimization to prevent the CPU&#x27;s portion of the MPC from becoming a bottleneck. We evaluate our approach using the UPMEM PIM system over various applications such as Deep Learning Recommendation Model inference and Logistic Regression. Our evaluations demonstrate up to a $14.66\times$ speedup compared to a secure CPU configuration while maintaining data confidentiality and integrity when outsourcing linear and/or nonlinear computation.

  匹配依据：MPC: garbled circuits, multi party computation, secret sharing, secure computing

  </details>

- **Simultaneous-Message and Succinct Secure Computation.**
  2025-01-21 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-031-91092-0_8) · [IACR ePrint](https://eprint.iacr.org/2025/096)
  Elette Boyle, Akshayaram Srinivasan, Sacha Servan-Schreiber, Abhishek Jain

  <details><summary>摘要 / Abstract</summary>

  We put forth and instantiate a new primitive we call simultaneous-message and succinct (SMS) secure computation. An SMS scheme enables a minimal communication pattern for secure computation in the following scenario: Alice has a large private input X, Bob has a small private input y, and Charlie wants to learn $f(X, y)$ for some public function $f$. Given a common reference string (CRS) setup phase, an SMS scheme for a function f is instantiated with two parties holding inputs $X$ and $y$, and has the following structure: - The parties simultaneously exchange a single message. - Communication is succinct, scaling sublinearly in the size of $X$ and the output $f(X, y)$. - Without further interaction, the parties can locally derive additive secret shares of $f(X, y)$. Indeed, Alice and Bob simultaneously send each other a message using the CRS and their private inputs. Using the transcript and their private state, the parties locally derive additive secret shares of $f(X, y)$, which they can send to Charlie. As such, an SMS scheme incurs a communication cost to Charlie that is only twice that of the function output length. Importantly, the size of Alice’s message does not grow with the size of her input $X$, and both Alice’s and Bob’s first-round messages grow sublinearly in the size of the output. Additionally, Alice’s or Bob’s view provides no information about the other party’s input besides the output of $f(X, y)$, even if colluding with Charlie. We obtain the following results: - Assuming Learning With Errors (LWE), we build an SMS scheme supporting evaluation of depth-$d$ circuits, where Alice&#x27;s message is of size $|f(X, y)|^{(2/3)}$· poly(λ, d), Bob&#x27;s message is of size $(|y| + |f(X, y)|^{(2/3)})$ · poly(λ, d), and λ is the security parameter. We can further extend this to support all functions by assuming the circular security of LWE. - Assuming sub-exponentially secure indistinguishability obfuscation, in conjunction with other standard assumptions, we build an SMS scheme supporting arbitrary polynomial-sized batch functions of the form $(f(x_1, y), ..., f(x_L, y))$, for $X = (x_1, ..., x_L)$. The size of Alice&#x27;s and Bob&#x27;s messages in this construction is poly(λ) and poly(λ, |f|, log L), respectively. We show that SMS schemes have several immediate applications. An SMS scheme gives: - A direct construction of trapdoor hash functions (TDH) (Döttling et al., Crypto&#x27;19) for the same class of functions as the one supported by the SMS scheme. - A simple and generic compiler for obtaining compact, rate-1 fully homomorphic encryption (FHE) from any non-compact FHE scheme. - A simple and generic compiler for obtaining correlation-intractable (CI) hash functions that are secure against all efficiently-searchable relations. In turn, under the LWE assumption, we obtain the first construction of TDH for all functions and generic approaches for obtaining rate-1 FHE and CI hashing. We also show that our iO-based construction gives an alternative approach for two-round secure computation with communication succinctness in the output length (Hubáček and Wichs, ITCS&#x27;15).

  匹配依据：MPC: secure computation

  </details>

- **Multi-Key Homomorphic Secret Sharing.**
  2025-01-21 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-91092-0_1) · [IACR ePrint](https://eprint.iacr.org/2025/094)
  Aditya Hegde, Geoffroy Couteau, Lalita Devadas, Sacha Servan-Schreiber, Abhishek Jain

  <details><summary>摘要 / Abstract</summary>

  Homomorphic secret sharing (HSS) is a distributed analogue of fully homomorphic encryption (FHE) where following an input-sharing phase, two or more parties can locally compute a function over their private inputs to obtain shares of the function output. Over the last decade, HSS schemes have been constructed from an array of different assumptions. However, all existing HSS schemes, except ones based on assumptions known to imply multi-key FHE, require a public-key infrastructure (PKI) or a correlated setup between parties. This limitation carries over to many applications of HSS. In this work, we construct multi-key homomorphic secret sharing (MKHSS), where given only a common reference string (CRS), two parties can secret share their inputs to each other and then perform local computations as in HSS. We present the first MKHSS schemes supporting all NC1 computations from either the decisional Diffie-Hellman (DDH), decisional composite residuosity (DCR), or class group assumptions. Our constructions imply the following applications in the CRS model: - Succinct two-round secure computation. Under the same assumptions as our MKHSS schemes, we construct succinct, two-round secure two-party computation for NC1 circuits. Previously, such a result was only known from the learning with errors assumption. - Attribute-based NIKE. Under DCR or class group assumptions, we construct non-interactive key exchange (NIKE) protocols where two parties agree on a key if and only if their secret attributes satisfy a public NC1 predicate. This significantly generalizes the existing notion of password-based NIKE. - Public-key PCFs. Under DCR or class group assumptions, we construct public-key pseudorandom correlation functions (PCFs) for any NC1 correlation. This yields the first public-key PCFs for Beaver triples (and more) from non-lattice assumptions. - Silent MPC. Under DCR or class group assumptions, we construct a p-party secure computation protocol in the silent preprocessing model where the preprocessing phase has communication O(p), ignoring polynomial factors. All prior protocols that do not rely on spooky encryption require $Ω(p^2)$ communication.

  匹配依据：MPC: secret sharing, secure computation, secure two party computation

  </details>

- **The Meta-complexity of Secret Sharing.**
  2025-01-12 · MPC · 含会议/期刊记录 · [STOC](https://doi.org/10.1145/3717823.3718161) · [IACR ePrint](https://eprint.iacr.org/2025/046)
  Oded Nir, Benny Applebaum

  <details><summary>摘要 / Abstract</summary>

  A secret-sharing scheme allows the distribution of a secret $s$ among $n$ parties, such that only certain predefined “authorized” sets of parties can reconstruct the secret, while all other “unauthorized” sets learn nothing about $s$. The collection of authorized/unauthorized sets is defined by a monotone function $f: \{0,1\}^n \rightarrow \{0,1\}$. It is known that any monotone function can be realized by a secret-sharing scheme; thus, the smallest achievable \emph{total share size}, $S(f)$, serves as a natural complexity measure. In this paper, we initiate the study of the following meta-complexity question: Given a monotone function $f$, is it possible to efficiently distinguish between cases where the secret-sharing complexity of $f$ is small versus large? We examine this question across several computational models, yielding the following main results. (Hardness for formulas and circuits): Given a monotone formula $f$ of size $L$, it is coNP-hard to distinguish between ``cheap&#x27;&#x27; functions, where the maximum share size is 1 bit and the total share size is $O(L^{0.01})$, and ``expensive&#x27;&#x27; functions, where the maximum share size is $\Omega(\sqrt{L})$ and the total share size is $\Omega(L/\log L)$. This latter bound nearly matches known secret-sharing constructions yielding a total share size of $L$ bits. For monotone circuits, we strengthen the bound on the expensive case to a maximum share size of $\Omega(L/\log L)$ and a total share size of $\Omega(L^2/\log L)$. These results rule out the existence of instance-optimal compilers that map a formula $f$ to a secret-sharing scheme with complexity polynomially related to $S(f)$. (Hardness for truth tables): Under cryptographic assumptions, either (1) every $n$-bit slice function can be realized by a $\text{poly}(n)$-size secret-sharing scheme, or (2) given a truth-table representation of $f$ of size $N = 2^n$, it is computationally infeasible to distinguish in time $\text{poly}(N)$ between cases where $S(f) = \text{poly}(n)$ and $S(f) = n^{\omega(1)}$. Option (1) would be considered a breakthrough result, as the best-known construction for slices has a sub-exponential complexity of $2^{\tilde{O}(\sqrt{n})}$ (Liu, Vaikuntanathan, and Wee; Eurocrypt 2018). Our proof introduces a new worst-case-to-average-case reduction for slices, which may be of independent interest. (Hardness for graphs): We examine the simple case where $f$ is given as a 2-DNF, represented by a graph $G$ whose edges correspond to 2-terms, and ask whether it is possible to distinguish between cases where the share size is constant and those where the share size is large, say $\Omega(\log n)$. We establish several connections between this question and questions in communication complexity. For instance, we show that graphs admitting constant-cost secret sharing form a subclass of graphs with constant randomized communication complexity and constant-size adjacency sketches (Harms, Wild, and Zamaraev; STOC 2022). We leverage these connections to establish new lower bounds for specific graph families, derive a combinatorial characterization of graphs with constant-size linear secret-sharing schemes, and show that a natural class of myopic algorithms fails to distinguish cheap graphs from expensive ones.

  匹配依据：MPC: secret sharing

  </details>

- **All-You-Can-Compute: Packed Secret Sharing for Combined Resilience.**
  2025-01-09 · MPC · 含会议/期刊记录 · [TCHES](https://doi.org/10.46586/TCHES.V2025.I2.420-459) · [IACR ePrint](https://eprint.iacr.org/2025/035)
  Maximilian Orlt, Liang Zhao, Sebastian Faust, Kathrin Wirschem

  <details><summary>摘要 / Abstract</summary>

  Unprotected cryptographic implementations are vulnerable to implementation attacks, such as passive side-channel attacks and active fault injection attacks. Recently, countermeasures like polynomial masking and duplicated masking have been introduced to protect implementations against combined attacks that exploit leakage and faults simultaneously. While duplicated masking requires $O(t * e)$ shares to resist an adversary capable of probing $t$ values and faulting $e$ values, polynomial masking requires only $O(t + e)$ shares, which is particularly beneficial for affine computation. At CHES&#x27;$24$, Arnold et al. showed how to further improve the efficiency of polynomial masking in the presence of combined attacks by embedding two secrets into one polynomial sharing. This essentially reduces the complexity of previous constructions by half. The authors also observed that using techniques from packed secret sharing (Grosso et al., CHES&#x27;$13$) cannot easily achieve combined resilience to encode an arbitrary number of secrets in one polynomial encoding. In this work, we resolve these challenges and show that it is possible to embed an arbitrary number of secrets in one encoding and propose gadgets that are secure against combined attacks. We present two constructions that are generic and significantly improve the computational and randomness complexity of existing compilers, such as the laOla compiler presented by Berndt et al. at CRYPTO&#x27;$23$ and its improvement by Arnold et al. For example, for an AES evaluation that protects against $t$ probes and $e$ faults, we improve the randomness complexity of the state-of-the-art construction when $t+e&gt;3$, leading to an improvement of up to a factor of $2.41$.

  匹配依据：MPC: secret sharing

  </details>

- **Wave Hello to Privacy: Efficient Mixed-Mode MPC using Wavelet Transforms.**
  2025-01-03 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2025-0083) · [IACR ePrint](https://eprint.iacr.org/2025/013)
  Sameer Wagh, Mehmet Ugurbil, Miguel de Vega, José Reis, Ryan Henry

  <details><summary>摘要 / Abstract</summary>

  This paper introduces new protocols for secure multiparty computation (MPC) leveraging Discrete Wavelet Transforms (DWTs) for computing nonlinear functions over large domains. By employing DWTs, the protocols significantly reduce the overhead typically associated with Lookup Table-style (LUT) evaluations in MPC. We state and prove foundational results for DWT-compressed LUTs in MPC, present protocols for 9 of the most common activation functions used in ML, and experimentally evaluate the performance of our protocols for large domain sizes in the LAN and WAN settings. Our protocols are extremely fast -- for instance, when considering 64-bit inputs, computing 1000 parallel instances of the sigmoid function, with an error less than $2^{-24}$ takes only a few hundred milliseconds incurs just 29\,KiB of online communication (40 bytes per evaluation).

  匹配依据：MPC: secure multiparty computation

  </details>

- **Π: A Unified Framework for Computational Verifiable Secret Sharing.**
  2025 · MPC · 含会议/期刊记录 · [PKC](https://doi.org/10.1007/978-3-031-91829-2_4)
  Karim Baghery

- **ømega (1/λ )-Rate Boolean Garbling Scheme from Generic Groups.**
  2025 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-032-01884-7_16)
  Geoffroy Couteau, Aditya Hegde, Naman Kumar, Carmit Hazay

- **Verifiable Secret Sharing from Symmetric Key Cryptography with Improved Optimistic Complexity.**
  2025 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-981-96-0941-3_4) · [IACR ePrint](https://eprint.iacr.org/2024/838)
  Ignacio Cascudo, Daniele Cozzo, Emanuele Giunta

  <details><summary>摘要 / Abstract</summary>

  In this paper we propose verifiable secret sharing (VSS) schemes secure for any honest majority in the synchronous model, and that only use symmetric-key cryptographic tools, therefore having plausibly post-quantum security. Compared to the state-of-the-art scheme with these features (Atapoor et al., Asiacrypt `23), our main improvement lies on the complexity of the ``optimistic&#x27;&#x27; scenario where the dealer and all but a small number of receivers behave honestly in the sharing phase: in this case, the running time and download complexity (amount of information read) of each honest verifier is polylogarithmic and the total amount of broadcast information by the dealer is logarithmic; all these complexities were linear in the aforementioned work by Atapoor et al. At the same time, we preserve these complexities with respect to the previous work for the ``pessimistic&#x27;&#x27; case where the dealer or $O(n)$ receivers cheat actively. The new VSS protocol is of interest in multiparty computations where each party runs one VSS as a dealer, such as distributed key generation protocols. Our main technical handle is a distributed zero-knowledge proof of low degreeness of a polynomial, in the model of Boneh et al. (Crypto `19) where the statement (in this case the evaluations of the witness polynomial) is distributed among several verifiers, each knowing one evaluation. Using folding techniques similar to FRI (Ben-Sasson et al., ICALP `18) we construct such a proof where each verifier receives polylogarithmic information and runs in polylogarithmic time.

  匹配依据：MPC: secret sharing

  </details>

- **Verifiable Secret Sharing Simplified.**
  2025 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP61157.2025.00046) · [IACR ePrint](https://eprint.iacr.org/2023/1196)
  Alin Tomescu, Zhuolun Xiang, Alexander Spiegelman, Sourav Das, Ling Ren, Benny Pinkas

  <details><summary>摘要 / Abstract</summary>

  Verifiable Secret Sharing (VSS) is a fundamental building block in cryptography. Despite its importance and extensive studies, existing VSS protocols are often complex and inefficient. Many of them do not support dual thresholds, are not publicly verifiable, or do not properly terminate in asynchronous networks. This paper presents a new and simple approach for designing VSS protocols in synchronous and asynchronous networks. Our VSS protocols are optimally fault-tolerant, i.e., they tolerate a $1/2$ and a $1/3$ fraction of malicious nodes in synchronous and asynchronous networks, respectively. They only require a public key infrastructure and the hardness of discrete logarithms. Our protocols support dual thresholds, and their transcripts are publicly verifiable. We implement our VSS protocols and evaluate them in a geo-distributed setting with up to 256 nodes. The evaluation demonstrates that our protocols offer asynchronous termination and public verifiability with performance that is comparable to that of existing schemes that lack these features. Compared to the existing schemes with similar guarantees, our approach lowers the bandwidth usage and latency by up to 90%.

  匹配依据：MPC: secret sharing

  </details>

- **Updatable Private Set Intersection Revisited: Extended Functionalities, Deletion, and Worst-Case Complexity.**
  2025 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-981-96-0938-3_7) · [IACR ePrint](https://eprint.iacr.org/2024/1446)
  Saikrishna Badrinarayanan, Peihan Miao, Xinyi Shi, Ruida Zeng, Max Tromanhauser

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) allows two mutually distrusting parties each holding a private set of elements, to learn the intersection of their sets without revealing anything beyond the intersection. Recent work (Badrinarayanan et al., PoPETS&#x27;22) initiates the study of updatable PSI (UPSI), which allows the two parties to compute PSI on a regular basis with sets that constantly get updated, where both the computation and communication complexity only grow with the size of the small updates and not the large entire sets. However, there are several limitations of their presented protocols. First, they can only be used to compute the plain PSI functionality and do not support extended functionalities such as PSI-Cardinality and PSI-Sum. Second, they only allow parties to add new elements to their existing set and do not support arbitrary deletion of elements. Finally, their addition-only protocols either require both parties to learn the output or only achieve low complexity in an amortized sense and incur linear worst-case complexity. In this work, we address all the above limitations. In particular, we study UPSI with semi-honest security in both the addition-only and addition-deletion settings. We present new protocols for both settings that support plain PSI as well as extended functionalities including PSI-Cardinality and PSI-Sum, achieving one-sided output (which implies two-sided output). In the addition-only setting, we also present a protocol for a more general functionality Circuit-PSI that outputs secret shares of the intersection. All of our protocols have worst-case computation and communication complexity that only grow with the set updates instead of the entire sets (except for a polylogarithmic factor). We implement our new UPSI protocols and compare with the state-of-the-art protocols for PSI and extended functionalities. Our protocols compare favorably when the total set sizes are sufficiently large, the new updates are sufficiently small, or in networks with low bandwidth.

  匹配依据：MPC: private set intersection

  </details>

- **Unclonable Secret Sharing.**
  2025 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2406.11008) · [ASIACRYPT](https://doi.org/10.1007/978-981-96-0947-5_5) · [IACR ePrint](https://eprint.iacr.org/2024/716)
  Vipul Goyal, Prabhanjan Vijendra Ananth, Jiahui Liu, Qipeng Liu, Prabhanjan Ananth

  <details><summary>摘要 / Abstract</summary>

  Unclonable cryptography utilizes the principles of quantum mechanics to addresses cryptographic tasks that are impossible classically. We introduce a novel unclonable primitive in the context of secret sharing, called unclonable secret sharing (USS). In a USS scheme, there are $n$ shareholders, each holding a share of a classical secret represented as a quantum state. They can recover the secret once all parties (or at least $t$ parties) come together with their shares. Importantly, it should be infeasible to copy their own shares and send the copies to two non-communicating parties, enabling both of them to recover the secret. Our work initiates a formal investigation into the realm of unclonable secret sharing, shedding light on its implications, constructions, and inherent limitations. ** Connections: We explore the connections between USS and other quantum cryptographic primitives such as unclonable encryption and position verification, showing the difficulties to achieve USS in different scenarios. **Limited Entanglement: In the case where the adversarial shareholders do not share any entanglement or limited entanglement, we demonstrate information-theoretic constructions for USS. **Large Entanglement: If we allow the adversarial shareholders to have unbounded entanglement resources (and unbounded computation), we prove that unclonable secret sharing is impossible. On the other hand, in the quantum random oracle model where the adversary can only make a bounded polynomial number of queries, we show a construction secure even with unbounded entanglement. Furthermore, even when these adversaries possess only a polynomial amount of entanglement resources, we establish that any unclonable secret sharing scheme with a reconstruction function implementable using Cliffords and logarithmically many T-gates is also unattainable.

  匹配依据：MPC: secret sharing

  </details>

- **Ultra-Fast Private Set Intersection From Efficient Oblivious Key-Value Stores.**
  2025 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2025.3557963)
  Shifeng Sun, Peng Tang, Weidong Qiu, Shouling Ji, Fei Tang, Guowei Ling

- **Towards Efficient and Practical Multi-party Computation under Inconsistent Trust in TEEs.**
  2025 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP61157.2025.00185)
  Qi Wang, Xuanwei Hu, Rujia Li, Yi Liu

- **TinyLabels: How to Compress Garbled Circuit Input Labels, Efficiently.**
  2025 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-91095-1_9) · [IACR ePrint](https://eprint.iacr.org/2024/2048)
  Hanjun Li, Marian Dietz, Huijia Lin

  <details><summary>摘要 / Abstract</summary>

  Garbled circuits are a foundational primitive in both theory and practice of cryptography. Given $(\hat{C}, K[x])$, where $\hat{C}$ is the garbling of a circuit C and $K[x] = \{K[i, x_i]\}$ are the input labels for an input $x$, anyone can recover $C(x)$, but nothing else about the input $x$. Most research efforts focus on minimizing the size of the garbled circuit $\hat{C}$. In contrast, the work by Applebaum, Ishai, Kushilevitz, and Waters (CRYPTO&#x27; 13) initiated the study of minimizing the cost for transferring the input labels $K[x]$. Later improved in a follow-up by Applebaum et al. (STOC&#x27; 23), the state-of-the-art techniques allow compressing the input labels to the optimal rate of $1 + o(1)$. That is, each input label can be transferred by essentially sending 1 bit. However, existing solutions are computationally expensive, requiring large numbers of public-key operations (such as RSA exponentiation). In this work, we present an efficient input label compression technique based on Ring-LWE. We achieve the same optimal rate of $1 + o(1)$, by making use of additional communication in an offline stage (before the input $x$ becomes known), a paradigm that has already been explored in prior works. A novel feature of the offline communication in our scheme is that the information sent is either reusable or compressible using a random oracle, leading to small amortized offline cost $o(|x|)$. We further demonstrate concrete efficiency through an implementation whose online latency out-performs the naive baseline (which sends all of $K[x]$ in the online phase) in a realistic network with a bandwidth of up to 45Mbps. This break-even point could be pushed even further by leveraging the large potential for parallelization of computation. Finally, we apply our techniques to construct maliciously-secure two-party computation protocols with succinct online communication: The online phase starts once the circuit C becomes known, and requires exchanging only $poly(\lambda)$ bits (independent of $|C|$). After inputs $x_A$, $x_B$ arrive, an additional $|x_A| + |x_B | + poly(\lambda)$ bits need to be sent.

  匹配依据：MPC: garbled circuit, garbled circuits, secure two party computation

  </details>

- **Timed Secret Sharing.**
  2025 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-981-96-0941-3_5) · [IACR ePrint](https://eprint.iacr.org/2023/1024)
  Philipp Jovanovic, Aydin Abadi, Alireza Kavousi

  <details><summary>摘要 / Abstract</summary>

  This paper introduces the notion of timed secret sharing (TSS), which establishes lower and upper time bounds for secret reconstruction in a threshold secret sharing scheme. Such time bounds are particularly useful in scenarios where an early or late reconstruction of a secret matters. We propose several new constructions that offer different security properties and show how they can be instantiated efficiently using novel techniques. We highlight how our ideas can be used to break the public goods game, which is an issue inherent to threshold secret sharing-based systems, without relying on incentive mechanism. We achieve this through an upper time bound that can be implemented either via short-lived proofs, or the gradual release of additional shares, establishing a trade-off between time and fault tolerance. The latter independently provides robustness in the event of dropout by some portion of shareholders.

  匹配依据：MPC: secret sharing

  </details>

- **The Concrete Security of Two-Party Computation: Simple Definitions, and Tight Proofs for PSI and OPRFs.**
  2025 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-981-96-0938-3_11) · [IACR ePrint](https://eprint.iacr.org/2024/1476)
  Rishabh Ranjan, Doreen Riepel, Ali Aldakheel, Mihir Bellare

  <details><summary>摘要 / Abstract</summary>

  This paper initiates a concrete-security treatment of two-party secure computation. The first step is to propose, as target, a simple, indistinguishability-based definition that we call InI. This could be considered a poor choice if it were weaker than standard simulation-based definitions, but it is not; we show that for functionalities satisfying a condition called invertibility, that we define and show is met by functionalities of practical interest like PSI and its variants, the two definitions are equivalent. Based on this, we move forward to study the concrete security of a canonical OPRF-based construction of PSI, giving a tight proof of InI security of the constructed PSI protocol based on the security of the OPRF. This leads us to the concrete security of OPRFs, where we show how different DH-style assumptions on the underlying group yield proofs of different degrees of tightness, including some that are tight, for the well-known and efficient 2H-DH OPRF, and thus for the corresponding DH PSI protocol. We then give a new PSI protocol, called salted-DH PSI, that is as efficient as DH-PSI, yet enjoys tighter proofs.

  匹配依据：MPC: secure computation, two party computation

  </details>

- **Split-State Non-malleable Codes and Secret Sharing Schemes for Quantum Messages.**
  2025 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2308.06466) · [TCC](https://doi.org/10.1007/978-3-031-78017-2_3) · [IACR ePrint](https://eprint.iacr.org/2024/335)
  Naresh Goud Boddu, João Ribeiro, Vipul Goyal, Rahul Jain

  <details><summary>摘要 / Abstract</summary>

  Non-malleable codes are fundamental objects at the intersection of cryptography and coding theory. These codes provide security guarantees even in settings where error correction and detection are impossible, and have found applications to several other cryptographic tasks. One of the strongest and most well-studied adversarial tampering models is $2$-split-state tampering. Here, a codeword is split into two parts and the adversary can then independently tamper with each part using arbitrary functions. This model can be naturally extended to the secret sharing setting with several parties by having the adversary independently tamper with each share. Previous works on non-malleable coding and secret sharing in the split-state tampering model only considered the encoding of \emph{classical} messages. Furthermore, until recent work by Aggarwal, Boddu, and Jain (IEEE Trans.\ Inf.\ Theory 2024), adversaries with quantum capabilities and \emph{shared entanglement} had not been considered, and it is a priori not clear whether previous schemes remain secure in this model. In this work, we introduce the notions of split-state non-malleable codes and secret sharing schemes for quantum messages secure against quantum adversaries with shared entanglement. Then, we present explicit constructions of such schemes that achieve low-error non-malleability. More precisely, we construct efficiently encodable and decodable split-state non-malleable codes and secret sharing schemes for quantum messages preserving entanglement with external systems and achieving security against quantum adversaries having shared entanglement with codeword length $n$, any message length at most $n^{Ω(1)}$, and error $ε=2^{-{n^{Ω(1)}}}$. In the easier setting of \emph{average-case} non-malleability, we achieve efficient non-malleable coding with rate close to $1/11$.

  匹配依据：MPC: secret sharing

  </details>

- **SoK: Computational and Distributed Differential Privacy for MPC.**
  2025 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2025-0023) · [IACR ePrint](https://eprint.iacr.org/2024/1290)
  Fredrik Meisingseth, Christian Rechberger

  <details><summary>摘要 / Abstract</summary>

  In the last fifteen years, there has been a steady stream of works combining differential privacy with various other cryptographic disciplines, particularly that of multi-party computation, yielding both practical and theoretical unification. As a part of that unification, due to the rich definitional nature of both fields, there have been many proposed definitions of differential privacy adapted to the given use cases and cryptographic tools at hand, resulting in computational and/or distributed versions of differential privacy. In this work, we offer a systemization of such definitions, with a focus on definitions that are both computational and tailored for a multi-party setting. We order the definitions according to the distribution model and computational perspective and propose a viewpoint on when given definitions should be seen as instantiations of the same generalised notion. The ordering highlights a clear, and sometimes strict, hierarchy between the definitions, where utility (accuracy) can be traded for stronger privacy guarantees or lesser trust assumptions. Further, we survey theoretical results relating the definitions to each other and extend some such results. We also discuss the state of well-known open questions and suggest new open problems to study. Finally, we consider aspects of the practical use of the different notions, hopefully giving guidance also to future applied work.

  匹配依据：MPC: multi party computation

  </details>

- **SelectFormer in Data Markets: Privacy-Preserving and Efficient Data Selection for Transformers with Multi-Party Computation.**
  2025 · MPC · 含会议/期刊记录 · [ICLR](https://openreview.net/forum?id=2cF3f9t31y)
  Felix Xiaozhu Lin, Xu Ouyang, Yangfeng Ji

- **Secure and efficient transciphering for FHE-based MPC.**
  2025 · MPC · 含会议/期刊记录 · [TCHES](https://doi.org/10.46586/TCHES.V2025.I3.745-780) · [IACR ePrint](https://eprint.iacr.org/2024/1702)
  Pierrick Méaux, Clément Hoffmann, Antonio Guimarães, Diego F. Aranha

  <details><summary>摘要 / Abstract</summary>

  Transciphering (or Hybrid-Homomorphic Encryption, HHE) is an es- tablished technique for avoiding ciphertext expansion in HE applications, saving communication and storage resources. Recently, it has also been shown to be a fundamental component in the practical construction of HE-based multi-party computation (MPC) protocols, being used both for input data and intermediary results (Smart, IMACC 2023). In these protocols, however, ciphers are used with keys that are jointly generated by multiple (possibly malicious) parties, which may require additional security assumptions that have been so far overlooked in the HHE literature. In this paper, we formalize this issue as a security against related-key attacks (RKA) problem and provide efficient solutions for it. We start by presenting an efficient method for homomorphically evaluating Mixed-Filter-Permutator (MFP) ciphers in leveled mode, enabling speedups of up to thousands of times compared to previous literature. For the multi-party scenario, we focus specifically on the Margrethe cipher (Hoffmann et al., INDOCRYPT 2023). We show that, contrary to other commonly used HHE ciphers (e.g. FLIP), Margrethe is out-of-the-box secure for any protocols that allow malicious parties to learn up to two related key streams, enabling security for the vast majority of static MPC protocols. For other cases, we quantify the loss of security based on the number of related key streams (which often depends on the number of malicious parties and specific protocol). Performance-wise, our implementation of Margrethe takes just 3.9 ms to transcipher 4 bit messages, being significantly faster than the state of the art in terms of latency.

  匹配依据：MPC: multi party computation

  </details>

- **Secure Computation with Parallel Calls to 2-Ary Functions.**
  2025 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-78023-3_8) · [IACR ePrint](https://eprint.iacr.org/2024/1701)
  Akshayaram Srinivasan, Varun Narayanan, Shubham Vivek Pawar

  <details><summary>摘要 / Abstract</summary>

  Reductions are the workhorses of cryptography. They allow constructions of complex cryptographic primitives from simple building blocks. A prominent example is the non-interactive reduction from securely computing a ``complex&quot; function $f$ to securely computing a ``simple&quot; function $g$ via randomized encodings. Prior work equated simplicity with functions of small degree. In this work, we consider a different notion of simplicity where we require $g$ to only take inputs from a small number of parties. In other words, we want the arity of $g$ to be as small as possible. In more detail, we consider the problem of reducing secure computation of arbitrary functions to secure computation of functions with arity two (two is the minimal arity required to compute non-trivial functions). Specifically, we want to compute a function $f$ via a protocol that makes parallel calls to 2-ary functions. We want this protocol to be secure against malicious adversaries that could corrupt an arbitrary number of parties. We obtain the following results: - Negative Result: We show that there exists a degree-2 polynomial $p$ such that no protocol that makes parallel calls to 2-ary functions can compute $p$ with statistical security with abort. - Positive Results: We give two ways to bypass the above impossibility result. 1. Weakening the Security Notion. We show that every degree-2 polynomial can be computed with statistical privacy with knowledge of outputs (PwKO) by making parallel calls to 2-ary functions. Privacy with knowledge of outputs is weaker than security with abort. 2. Computational Security. We prove that for every function $f$, there exists a protocol for computing $f$ that makes parallel calls to 2-ary functions and achieves security with abort against computationally-bounded adversaries. The security of this protocol relies on the existence of semi-honest secure oblivious transfer. - Applications: We give connections between this problem and the task of reducing the encoding complexity of Multiparty Randomized Encodings (MPRE) (Applebaum, Brakerski, and Tsabary, TCC 2018). Specifically, we show that under standard computational assumptions, there exists an MPRE where the encoder can be implemented by an $\mathrm{NC}^0$ circuit with constant fan-out. - Extensions: We explore this problem in the honest majority setting and give similar results assuming one-way functions. We also show that if the parties have access to 3-ary functions then we can construct a computationally secure protocol in the dishonest majority setting assuming one-way functions.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **Secret-Sharing Schemes for High Slices.**
  2025 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-78023-3_19) · [IACR ePrint](https://eprint.iacr.org/2024/602)
  Or Lasri, Oriol Farràs, Oded Nir, Amos Beimel

  <details><summary>摘要 / Abstract</summary>

  In a secret-sharing scheme, a secret is shared among $n$ parties such that the secret can be recovered by authorized coalitions, while it should be kept hidden from unauthorized coalitions. In this work we study secret-sharing for $k$-slice access structures, in which coalitions of size $k$ are either authorized or not, larger coalitions are authorized and smaller are unauthorized. Known schemes for these access structures had smaller shares for small $k$&#x27;s than for large ones; hence our focus is on &quot;high&quot; $(n-k)$-slices where $k$ is small. Our work is inspired by several motivations: 1) Obtaining efficient schemes (with perfect or computational security) for natural families of access structures; 2) Making progress in the search for better schemes for general access structures, which are often based on schemes for slice access structures; 3) Proving or disproving the conjecture by Csirmaz (J. Math. Cryptol., 2020) that an access structures and its dual can be realized by secret-sharing schemes with the same share size. The main results of this work are: - Perfect schemes for high slices. We present a scheme for $(n-k)$-slices with information-theoretic security and share size $kn\cdot 2^{\tilde{O}(\sqrt{k \log n})}$. Using a different scheme with slightly larger shares, we prove that the ratio between the optimal share size of $k$-slices and that of their dual $(n-k)$-slices is bounded by $n$. - Computational schemes for high slices. We present a scheme for $(n-k)$-slices with computational security and share size $O(k^2 \lambda \log n)$ based on the existence of one-way functions. Our scheme makes use of a non-standard view point on Shamir secret-sharing that allows to share many secrets with different thresholds with low cost. - Multislice access structures. $(a:b)$-multislices are access structures that behave similarly to slices, but are unconstrained on coalitions in a wider range of cardinalities between $a$ and $b$. We use our new schemes for high slices to realize multislices with the same share sizes that their duals have today. This solves an open question raised by Applebaum and Nir (Crypto, 2021), and allows to realize hypergraph access structures that are chosen uniformly at random under a natural set of distributions with share size $2^{0.491n+o(n)}$ compared to the previous result of $2^{0.5n+o(n)}$.

  匹配依据：MPC: secret sharing

  </details>

- **Secret Sharing with Publicly Verifiable Deletion.**
  2025 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-91131-6_10) · [IACR ePrint](https://eprint.iacr.org/2024/1596)
  Benjamin Sela, Jonathan Katz, Ben Sela

  <details><summary>摘要 / Abstract</summary>

  Certified deletion, an inherently quantum capability, allows a party holding a quantum state to prove that they have deleted the information contained in that state. Bartusek and Raizes (Crypto 2024) recently studied certified deletion in the context of secret sharing schemes, and showed constructions with privately verifiable proofs of deletion that can be verified only by the dealer who generated the shares. We give two constructions of secret sharing schemes with publicly verifiable certified deletion. Our first construction is based on the post-quantum security of the LWE problem, and each share requires a number of qubits that is linear in the size of an underlying classical secret sharing scheme for the same set of authorized parties. Our second construction is based on a more general assumption—the existence of post quantum one-way functions— but requires an asymptotically larger number of qubits relative to the share size of the underlying classical scheme.

  匹配依据：MPC: secret sharing

  </details>

- **Round-Optimal Black-Box Multiparty Computation from Polynomial-Time Assumptions.**
  2025 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-031-91092-0_12) · [IACR ePrint](https://eprint.iacr.org/2023/1742)
  Michele Ciampi, Luisa Siniscalchi, Hendrik Waldner, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  A central direction of research in secure multiparty computation with dishonest majority has been to achieve three main goals: 1. reduce the total number of rounds of communication (to four, which is optimal); 2. use only polynomial-time hardness assumptions, and 3. rely solely on cryptographic assumptions in a black-box manner. This is especially challenging when we do not allow a trusted setup assumption of any kind. While protocols achieving two out of three goals in this setting have been designed in recent literature, achieving all three simultaneously remained an elusive open question. Specifically, it was answered positively only for a restricted class of functionalities. In this paper, we completely resolve this long-standing open question. Specifically, we present a protocol for all polynomial-time computable functions that does not require any trusted setup assumptions and achieves all three of the above goals simultaneously.

  匹配依据：MPC: multiparty computation, secure multiparty computation

  </details>

- **Reversible Data Hiding in Encrypted Images With Secret Sharing and Multivariate Linear Equation.**
  2025 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2025.3590551)
  Xianquan Zhang, Chunqiang Yu, Peng Liu, Xinpeng Zhang, Guoxiang Li, Zhenjun Tang

- **Reducing the Share Size of Weighted Threshold Secret Sharing Schemes via Chow Parameters Approximation.**
  2025 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-78023-3_17) · [IACR ePrint](https://eprint.iacr.org/2024/772)
  Miquel Guiot, Oriol Farràs

  <details><summary>摘要 / Abstract</summary>

  A secret sharing scheme is a cryptographic primitive that allows a dealer to share a secret among a set of parties, so that only authorized subsets of them can recover it. The access structure of the scheme is the family of authorized subsets. In a weighted threshold access structure, each party is assigned a weight according to its importance, and the authorized subsets are those in which the sum of their weights is at least the threshold value. For these access structures, the share size of the best known secret sharing schemes is either linear on the weights or quasipolynomial on the number of parties, which leads to long shares, in general. In certain settings, a way to circumvent this efficiency problem is to approximate the access structure by another one that admits more efficient schemes. This work is dedicated to the open problem posed by this strategy: Finding secret sharing schemes with a good tradeoff between the efficiency and the accuracy of the approximation. We present a method to approximate weighted threshold access structures by others that admit schemes with small shares. This method is based on the techniques for the approximation of the Chow parameters developed by De et al. [Journal of the ACM, 2014]. Our method provides secret sharing schemes with share size $n^{1+o(1)}$, where $n$ is the number of parties, and whose access structure is close to the original one. Namely, in this approximation the condition of being authorized or not is preserved for almost all subsets of parties. In addition, we apply the recent results on computational secret sharing schemes by Applebaum et al. [STOC, 2023] to construct computational secret sharing schemes whose share size is polylogarithmic in the number of parties.

  匹配依据：MPC: secret sharing

  </details>

- **Recurrent Private Set Intersection for Unbalanced Databases with Cuckoo Hashing and Leveled FHE.**
  2025 · MPC · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/recurrent-private-set-intersection-for-unbalanced-databases-with-cuckoo-hashing-and-leveled-fhe/)
  Eduardo Chielle, Michail Maniatakos

- **Re-visiting Authorized Private Set Intersection: A New Privacy-Preserving Variant and Two Protocols.**
  2025 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2025-0041) · [IACR ePrint](https://eprint.iacr.org/2024/1579)
  Evangelia Anna Markatou, Francesca Falzon

  <details><summary>摘要 / Abstract</summary>

  We revisit the problem of Authorized Private Set Intersection (APSI), which allows mutually untrusting parties to authorize their items using a trusted third-party judge before privately computing the intersection. We also initiate the study of Partial-APSI, a novel privacy-preserving generalization of APSI in which the client only reveals a subset of their items to a third-party semi-honest judge for authorization. Partial-APSI allows for partial verification of the set, preserving the privacy of the party whose items are being verified. Both APSI and Partial-APSI have a number of applications, including genome matching, ad conversion, and compliance with privacy policies such as the GDPR. We present two protocols based on bilinear pairings with linear communication. The first realizes the APSI functionality, is secure against a malicious client, and requires only one round of communication during the online phase. Our second protocol realizes the Partial-APSI functionality and is secure against a client that may maliciously inject elements into its input set, but who follows the protocol semi-honestly otherwise. We formally prove correctness and security of these protocols and provide an experimental evaluation to demonstrate their practicality. Our protocols can be efficiently run on commodity hardware. We also show that our protocols are massively parallelizable by running our experiments on a compute grid across 50 cores.

  匹配依据：MPC: private set intersection

  </details>

- **Rate-1 Arithmetic Garbling From Homomorphic Secret Sharing.**
  2025 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-78023-3_3) · [IACR ePrint](https://eprint.iacr.org/2024/820)
  Lawrence Roy, Peter Scholl, Pierre Meyer, Claudio Orlandi

  <details><summary>摘要 / Abstract</summary>

  We present a new approach to garbling arithmetic circuits using techniques from homomorphic secret sharing, obtaining constructions with high rate that support free addition gates. In particular, we build upon non-interactive protocols for computing distributed discrete logarithms in groups with an easy discrete-log subgroup, further demonstrating the versatility of tools from homomorphic secret sharing. Relying on distributed discrete log for the Damgård-Jurik cryptosystem (Roy and Singh, Crypto `21), whose security follows from the decisional composite residuosity assumption (DCR), we get the following main results: [**Two ciphertexts per multiplication, from IND-CPA security of Damgård-Jurik.**] Assuming the Damgård-Jurik cryptosystem is semantically secure (which follows from DCR), there is a garbling scheme for circuits with $B$-bounded integer arithmetic using only two ciphertexts per multiplication. The total bit-size of the resulting garbled circuit is: $$(n + 2s_\times+2D_\times)\cdot (\zeta + 1) \cdot \log N$$ where $n$ is the number of inputs, $s_\times$ is the number of multiplications, $D_\times$ is the multiplicative depth of the circuit, $N$ is an RSA modulus and $N^{\zeta-1}$ is a rough bound on the magnitude of wire values in the computation. [**One ciphertext per multiplication, from KDM security of Damgård-Jurik.**] Assuming the Damgård-Jurik encryption scheme remains secure given encryption of the key and its inverse, the construction achieves rate-$1$. The total bit-size of the resulting garbled circuit is: $$(n + s_\times + 1) \cdot (\zeta + 1) \cdot \log N$$ where the parameters are as above, except $N^{\zeta-2}$ is the magnitude bound. As a side result, we show that our scheme based on IND-CPA security achieves rate $3/5$ for levelled circuits.

  匹配依据：MPC: garbled circuit, garbling scheme, secret sharing

  </details>

- **QuietOT: Lightweight Oblivious Transfer with a Public-Key Setup.**
  2025 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-981-96-0888-1_7) · [IACR ePrint](https://eprint.iacr.org/2024/1079)
  Geoffroy Couteau, Srini Devadas, Lalita Devadas, Sacha Servan-Schreiber, Alexander Koch, Srinivas Devadas

  <details><summary>摘要 / Abstract</summary>

  Oblivious Transfer (OT) is at the heart of secure computation and is a foundation for many applications in cryptography. Over two decades of work have led to extremely efficient protocols for evaluating OT instances in the preprocessing model, through a paradigm called OT extension. A few OT instances generated in an offline phase can be used to perform many OTs in an online phase efficiently, i.e., with very low communication and computational overheads. Specifically, traditional OT extension protocols use a small number of “base” OTs, generated using any black-box OT protocol, and convert them into many OT instances using only lightweight symmetric-key primitives. Recently, a new paradigm of OT with a *public-key setup* has emerged, which replaces the base OTs with a non-interactive setup: Using only the public key of the other party, two parties can efficiently compute a virtually unbounded number of OT instances on-the-fly. In this paper, we put forth a novel framework for OT extension with a public-key setup and concretely efficient instantiations. An implementation of our framework is 30-100 times faster when compared to the previous state-of-the-art public-key OT protocols, and remains competitive even when compared to OT protocols that *do not* offer a public-key setup. Additionally, our instantiations result in the first public-key schemes with plausible post-quantum security. In summary, this paper contributes: - QuietOT: A framework for OT extension with a public-key setup that uses fast, symmetric-key primitives to generate OT instances following a one-time public-key setup, and offering additional features such as precomputability. - A public-key setup for QuietOT from the RingLWE assumption, resulting in the first post-quantum construction of OT extension with a public-key setup. - An optimized, open-source implementation of our construction that can generate up to 1M OT extensions per second on commodity hardware. In contrast, the state-of-the-art public-key OT protocol is limited to approximately 20K OTs per second. - The first formal treatment of the security of OT with a public-key setup in a multi-party setting, which addresses several subtleties that were overlooked in prior work.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **Protecting Distributed Primitives Against Leakage: Equivocal Secret Sharing and more.**
  2025 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-024-09524-3) · [IACR ePrint](https://eprint.iacr.org/2022/497)
  Mor Weiss, Muthuramakrishnan Venkitasubramaniam, Carmit Hazay

  <details><summary>摘要 / Abstract</summary>

  Leakage-resilient cryptography aims to protect cryptographic primitives from so-called &quot;side channel attacks&quot; that exploit their physical implementation to learn their input or secret state. Starting from the works of Ishai, Sahai and Wagner (CRYPTO`03) and Micali and Reyzin (TCC`04), most works on leakage-resilient cryptography either focus on protecting general computations, such as circuits or multiparty computation protocols, or on specific non-interactive primitives such as storage, encryption and signatures. This work focuses on leakage-resilience for the middle ground, namely for distributed and interactive cryptographic primitives. Our main technical contribution is designing the first secret-sharing scheme that is equivocal, resists adaptive probing of a constant fraction of bits from each share, while incurring only a constant blowup in share size. Equivocation is a strong leakage-resilience guarantee, recently introduced by Hazay et al. (ITC`21). Our construction is obtained via a general compiler which we introduce, that transforms any secret-sharing scheme into an equivocal scheme against adaptive leakage. An attractive feature of our compiler is that it respects additive reconstruction, namely, if the original scheme has additive reconstruction, then the transformed scheme has linear reconstruction. We extend our compiler to a general paradigm for protecting distributed primitives against leakage, and show its applicability to various primitives, including secret sharing, verifiable secret sharing, function secret sharing, distributed encryption and signatures, and distributed zero-knowledge proofs. For each of these primitives, our paradigm transforms any construction of the primitive into a scheme that resists adaptive party corruptions, as well as adaptive probing leakage of a constant fraction of bits in each share when the share is stored in memory (but not when it is used in computations). Moreover, the transformation incurs only a constant blowup in the share size, and respects additive reconstruction - an important feature for several of these primitives, such as function secret sharing and distributed encryption.

  匹配依据：MPC: multiparty computation, secret sharing

  </details>

- **Private Set Union with Multiple Contributions.**
  2025 · MPC · 含会议/期刊记录 · [NeurIPS](http://papers.nips.cc/paper_files/paper/2025/hash/81a4bde3b5c6665dbd780b1fd577851f-Abstract-Conference.html)
  Ananda Theertha Suresh, Uri Stemmer, Travis Dick, Ziteng Sun, Alex Kulesza, Haim Kaplan

- **Privacy-Preserving Authorized Set Matching via Dishonest Majority Multiparty Computation.**
  2025 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2025.3599183)
  Weidong Qiu, Liyao Xiang, Jinyong Shan, Fei Tang, Guowei Ling, Peng Tang, Shifeng Sun

- **Physical-Bit Leakage Resilience of Linear Code-Based Secret Sharing.**
  2025 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-031-91101-9_3)
  Hai H. Nguyen

- **Perfectly-Secure Multiparty Computation with Linear Communication Complexity over Any Modulus.**
  2025 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-981-96-0938-3_4) · [IACR ePrint](https://eprint.iacr.org/2024/370)
  Daniel Escudero, Wenhao Wang, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  Consider the task of secure multiparty computation (MPC) among $n$ parties with perfect security and guaranteed output delivery, supporting $t&lt;n/3$ active corruptions. Suppose the arithmetic circuit $C$ to be computed is defined over a finite ring $\mathbb{Z}/q\mathbb{Z}$, for an arbitrary $q\in\mathbb{Z}$. It is known that this type of MPC over such ring is possible, with communication that scales as $O(n|C|)$, assuming that $q$ scales as $\Omega(n)$. However, for constant-size rings $\mathbb{Z}/q\mathbb{Z}$ where $q = O(1)$, the communication is actually $O(n\log n|C|)$ due to the need of the so-called ring extensions. In most natural settings, the number of parties is variable but the &quot;datatypes&quot; used for the computation are fixed (e.g. 64-bit integers). In this regime, no protocol with linear communication exists. In this work we provide an MPC protocol in this setting: perfect security, G.O.D. and $t&lt;n/3$ active corruptions, that enjoys linear communication $O(n|C|)$, even for constant-size rings $\mathbb{Z}/q\mathbb{Z}$. This includes as important particular cases small fields such as $\mathbb{F}_2$, and also the ring $\mathbb{Z}/2^k\mathbb{Z}$. The main difficulty in achieving this result is that widely used techniques such as linear secret-sharing cannot work over constant-size rings, and instead, one must make use of ring extensions that add $\Omega(\log n)$ overhead, while packing $\Omega(\log n)$ ring elements in each extension element in order to amortize this cost. We make use of reverse multiplication-friendly embeddings (RMFEs) for this packing, and adapt recent techniques in network routing (Goyal et al. CRYPTO&#x27;22) to ensure this can be efficiently used for non-SIMD circuits. Unfortunately, doing this naively results in a restriction on the minimum width of the circuit, which leads to an extra additive term in communication of $\mathsf{poly}(n)\cdot\mathsf{depth}(C)$. One of our biggest technical contributions lies in designing novel techniques to overcome this limitation by packing elements that are distributed across different layers. To the best of our knowledge, all works that have a notion of packing (e.g. RMFE or packed secret-sharing) group gates across the same layer, and not doing so, as in our work, leads to a unique set of challenges and complications.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Perfectly-Secure MPC with Constant Online Communication Complexity.**
  2025 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-78023-3_11) · [IACR ePrint](https://eprint.iacr.org/2024/242)
  Xiaxi Ye, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  In this work, we study the communication complexity of perfectly secure MPC protocol with guaranteed output delivery against $t=(n-1)/3$ corruptions. The previously best-known result in this setting is due to Goyal, Liu, and Song (CRYPTO, 2019) which achieves $O(n)$ communication per gate, where $n$ is the number of parties. On the other hand, in the honest majority setting, a recent trend in designing efficient MPC protocol is to rely on packed Shamir sharings to speed up the online phase. In particular, the work by Escudero et al. (CCS 2022) gives the first semi-honest protocol that achieves a constant communication overhead per gate across all parties in the online phase while maintaining overall $O(n)$ communication per gate. We thus ask the following question: ``Is it possible to construct a perfectly secure MPC protocol with GOD such that the online communication per gate is $O(1)$ while maintaining overall $O(n)$ communication per gate?&#x27;&#x27; In this work, we give an affirmative answer by providing an MPC protocol for computing an arithmetic circuit $C$ over a finite field of size at least $2n$ with communication complexity $O(|C|+\mathsf{Depth}\cdot n+n^5 \cdot \log n)$ elements for the online phase, and $O(|C|\cdot n+\mathsf{Depth}\cdot n^2 + n^5 \cdot \log n)$ elements for the preprocessing phase, where $|C|$ is the circuit size and $\mathsf{Depth}$ is the circuit depth.

  匹配依据：MPC: mpc (context)

  </details>

- **POTA: A Pipelined Oblivious Transfer Acceleration Architecture for Secure Multi-Party Computation.**
  2025 · MPC · 含会议/期刊记录 · [TCHES](https://doi.org/10.46586/TCHES.V2025.I3.262-292)
  Yong Liu, Ninghui Sun, Qinfen Hao, Xiaolin Li, Yong Zhang, Hongwei Liu, Wei Yan

- **PM-ABE: Puncturable Bilateral Fine-Grained Access Control From Lattices for Secret Sharing.**
  2025 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2024.3431035)
  Debiao He, Mengxue Yang, Huaqun Wang

- **PIGEON: A High Throughput Framework for Private Inference of Neural Networks using Secure Multiparty Computation.**
  2025 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2025-0090) · [IACR ePrint](https://eprint.iacr.org/2024/1371)
  Murali Annavaram, Christopher Harth-Kitzerow, Rachit Rajat, Yongqin Wang, Georg Carle

  <details><summary>摘要 / Abstract</summary>

  Privacy-Preserving Machine Learning (PPML) is one of the most relevant use cases for Secure Multiparty Computation (MPC). While private training of large neural networks such as VGG-16 or ResNet-50 on state-of-the-art datasets such as ImageNet is still out of reach, given the performance overhead of MPC, GPU-based MPC frameworks are starting to achieve practical runtimes for private inference. However, we show that, unlike plaintext machine learning, using GPU acceleration for both linear (e.g., convolutions) and nonlinear neural network layers (e.g., ReLU) is actually counterproductive in PPML. While GPUs effectively accelerate linear layers compared to CPU-based MPC implementations, the MPC circuits required to evaluate nonlinear layers introduce memory overhead and frequent data movement between the GPU and the CPU to handle network communication. This results in slow ReLU performance and high GPU memory requirements in state-of-the-art GPU-based PPML frameworks, hindering them from scaling to multiple images per second inference throughput and more than eight images per batch on ImageNet. To overcome these limitations, we propose PIGEON, an open-source framework for Private Inference of Neural Networks. PIGEON employs a novel ABG programming model that switches between Arithmetic Vectorization and Bitslicing on the CPU for nonlinear layers depending on the MPC-specific computation required while offloading linear layers to the GPU. Compared to the state-of-the-art PPML framework Piranha, PIGEON improves ReLU throughput by two orders of magnitude, reduces peak GPU memory utilization by one order of magnitude, and scales better with large batch sizes. This translates to one to two orders of magnitude improvements in throughput for large ImageNet batch sizes (e.g., 192) and more than 70% saturation of a 25 Gbit/s network.

  匹配依据：MPC: secure multiparty computation

  </details>

- **New Upper Bounds for Evolving Secret Sharing via Infinite Branching Programs.**
  2025 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-78023-3_18) · [IACR ePrint](https://eprint.iacr.org/2024/419)
  Bar Alon, Tamar Ben David, Eran Omri, Anat Paskin-Cherniavsky, Amos Beimel

  <details><summary>摘要 / Abstract</summary>

  Evolving secret-sharing schemes, defined by Komargodski, Naor, and Yogev [TCC 2016B, IEEE Trans. on Info. Theory 2018], are secret-sharing schemes in which there is no a-priory bound on the number of parties. In such schemes, parties arrive one by one; when a party arrives, the dealer gives it a share and cannot update this share in later stages. The requirement is that some predefined sets (called authorized sets) should be able to reconstruct the secret, while other sets should learn no information on the secret. The collection of authorized sets that can reconstruct the secret is called an evolving access structure. The challenge of the dealer is to be able to give short shares to the the current parties without knowing how many parties will arrive in the future. The requirement that the dealer cannot update shares is designed to prevent expensive updates. Komargodski et al. constructed an evolving secret-sharing scheme for every monotone evolving access structure; the share size of the $t^{\text{th}}$ party in this scheme is $2^{t-1}$. Recently, Mazor [ITC 2023] proved that evolving secret-sharing schemes require exponentially-long shares for some evolving access structure, namely shares of size $2^{t-o(t)}$.In light of these results, our goal is to construct evolving secret-sharing schemes with non-trivial share size for wide classes of evolving access structures; e.g., schemes with share size $2^{ct}$ for $c 0$, which is comparable to the best-known share size of $2^{\tilde{O}((\log t)^{1/2}))}$ for finite $2$-slice and 3-slice access structures. -We prove lower bounds on the share size of evolving secret-sharing schemes for infinite $k$-hypergraph access structures and for infinite directed st-connectivity access structures. As a by-product of the lower bounds, we provide the first non-trivial lower bound for finite directed st-connectivity access structures for general secret-sharing schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Multiparty Delegated Private Set Union With Efficient Updates on Outsourced Datasets.**
  2025 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2024.3419576)
  Heewon Chung, Myungsun Kim, Patrick Chulsoon Yang

- **Multi-Party Private Set Intersection With One-Round Online Interaction.**
  2025 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2025.3574993)
  Shengnan Zhao, Chuan Zhao, Qiuliang Xu, Yu Meng, Shan Jing, Shimeng Lu, Zhenxiang Chen

- **More Efficient, Privacy-Enhanced, and Powerful Privacy-Preserving Feature Retrieval Private Set Intersection.**
  2025 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2025.3562695)
  Guowei Ling, Fei Tang, Peng Tang, Weidong Qiu, Jinyong Shan

- **Maliciously Secure Circuit Private Set Intersection via SPDZ-Compatible Oblivious PRF.**
  2025 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2025-0082) · [IACR ePrint](https://eprint.iacr.org/2024/789)
  Changyu Dong, Linting Huang, Xiaojian Liang, Yaxi Yang, Hongyu Ren, Xiangfu Song, Jianying Zhou, Ye Dong

  <details><summary>摘要 / Abstract</summary>

  Circuit Private Set Intersection (Circuit-PSI) allows two parties to compute a function $f$ on items in the intersection of their input sets without revealing items in the intersection set. It is a well-known variant of PSI and has numerous practical applications. However, existing Circuit-PSI protocols only provide security against \textit{semi-honest} adversaries. A straightforward approach to constructing a maliciously secure Circuit-PSI is to extend a pure garbled-circuit-based PSI (NDSS&#x27;12 \cite{huang2012private}) to a maliciously secure circuit-PSI, but it will not be concretely efficient. Another is converting state-of-the-art semi-honest Circuit-PSI protocols (EUROCRYPT&#x27;21 \cite{rindal2021vole}; PoPETS&#x27;22 \cite{chandran2022circuit}) to be secure in the malicious setting. However, it will come across \textit{the consistency issue} (EUROCRYPT&#x27;11 \cite{shelat2011two}) since parties can not guarantee the inputs of the function $f$ stay unchanged as obtained from the last step. This paper tackles the previously mentioned issue by presenting the first maliciously secure Circuit-PSI protocol. Our key innovation, the Distributed Dual-key Oblivious Pseudorandom Function (DDOPRF), enables the oblivious evaluation of secret-shared inputs using dual keys within the SPDZ MPC framework. Notably, this construction seamlessly ensures fairness within the Circuit-PSI. Compared to the state-of-the-art semi-honest Circuit-PSI protocol (PoPETS&#x27;22), experimental results demonstrate that our malicious Circuit-PSI protocol not only reduces around $5$x communication costs but also enhances efficiency, particularly for modest input sets ($\le 2^{14}$) in the case of the WAN setting with high latency and limited bandwidth.

  匹配依据：MPC: garbled circuit, private set intersection

  </details>

- **Labeled Private Set Intersection From Distributed Point Function.**
  2025 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2025.3550059)
  Kang Yang, Yu Yu, Qi Liu, Xiaojie Guo

- **Is MPC Secure? Leveraging Neural Network Classifiers to Detect Data Leakage Vulnerabilities in MPC Implementations.**
  2025 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP61157.2025.00181)
  Wenjing Fang, Jin Tan, Lei Wang, Junming Ma, Lushan Song, Guopeng Lin, Weili Han, Xiaoning Du

- **Increasing the Resilience of Secure Multiparty Computation Using Security Modules.**
  2025 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2025.3552670)
  Lamya Abdullah, Felix C. Freiling, Dominique Schröder

- **Improved Universal Thresholdizer from Iterative Shamir Secret Sharing.**
  2025 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-024-09536-Z) · [IACR ePrint](https://eprint.iacr.org/2023/545)
  Wonhee Cho, Jiseung Kim, Jung Hee Cheon

  <details><summary>摘要 / Abstract</summary>

  The universal thresholdizer, introduced at CRYPTO&#x27;18, is a cryptographic scheme that transforms any cryptosystem into a threshold variant, thereby enhancing its applicability in threshold cryptography. It enables black-box construction of one-round threshold signature schemes based on the Learning with Errors problem, and similarly, facilitates one-round threshold ciphertext-attack secure public key encryption when integrated with non-threshold schemes. Current constructions of universal thresholdizer are fundamentally built upon linear secret sharing schemes. One approach employs Shamir&#x27;s secret sharing, which lacks compactness and results in ciphertext sizes of $O(N \log N)$, and another approach uses $\{0,1\}$-linear secret sharing scheme ($\{0,1\}$-LSSS), which is compact but induces high communication costs due to requiring $O(N^{5.3})$ secret shares. In this work, we introduce a communication-efficient universal thresholdizer by revising the linear secret sharing scheme. We propose a specialized linear secret sharing scheme, called TreeSSS, which reduces the number of required secret shares $O(N^{3+o(1)})$ while maintaining the compactness of the universal thresholdizer. TreeSSS can also serve as a subroutine for constructing lattice based $t$-out-of-$N$ threshold cryptographic primitives such as threshold fully homomorphic encryptions and threshold signatures. In this context, TreeSSS offers the advantage of lower communication overhead due to the reduced number of secret shares involved.

  匹配依据：MPC: secret sharing

  </details>

- **Honest Majority MPC with Õ(\|C\|) Communication in Minicrypt.**
  2025 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-031-91092-0_16)
  Xiaxi Ye, Yifan Song

- **Honest Majority GOD MPC with O(sfdepth(C)) Rounds and Low Online Communication.**
  2025 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-981-96-0938-3_8)
  Daniel Escudero, Alexander Bienstock, Amit Agarwal, Ivan Damgård

- **High-Throughput Secure Multiparty Computation with an Honest Majority in Various Network Settings.**
  2025 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2206.03776) · [PoPETs](https://doi.org/10.56553/POPETS-2025-0015) · [IACR ePrint](https://eprint.iacr.org/2024/386)
  Ajith Suresh, Murali Annavaram, Christopher Harth-Kitzerow, Yongqin Wang, Hossein Yalame, Georg Carle

  <details><summary>摘要 / Abstract</summary>

  In this work, we present novel protocols over rings for semi-honest secure three-party computation (3PC) and malicious four-party computation (4PC) with one corruption. While most existing works focus on improving total communication complexity, challenges such as network heterogeneity and computational complexity, which impact MPC performance in practice, remain underexplored. Our protocols address these issues by tolerating multiple arbitrarily weak network links between parties without any substantial decrease in performance. Additionally, they significantly reduce computational complexity by requiring up to half the number of basic instructions per gate compared to related work. These improvements lead to up to twice the throughput of state-of-the-art protocols in homogeneous network settings and up to eight times higher throughput in real-world heterogeneous settings. These advantages come at no additional cost: Our protocols maintain the best-known total communication complexity per multiplication, requiring 3 elements for 3PC and 5 elements for 4PC. We implemented our protocols alongside several state-of-the-art protocols (Replicated 3PC, ASTRA, Fantastic Four, Tetrad) in a novel open-source C++ framework optimized for high throughput. Five out of six implemented 3PC and 4PC protocols achieve more than one billion 32-bit multiplications or over 32 billion AND gates per second using our implementation in a 25 Gbit/s LAN environment. This represents the highest throughput achieved in 3PC and 4PC so far, outperforming existing frameworks like MP-SPDZ, ABY3, MPyC, and MOTION by two to three orders of magnitude.

  匹配依据：MPC: secure multiparty computation, secure three party computation

  </details>

- **General Adversary Structures in Byzantine Agreement and Multi-party Computation with Active and Omission Corruption.**
  2025 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-78023-3_7) · [IACR ePrint](https://eprint.iacr.org/2024/209)
  Konstantinos Brazitikos, Vassilis Zikas

  <details><summary>摘要 / Abstract</summary>

  Typical results in multi-party computation (in short, MPC) capture faulty parties by assuming a threshold adversary corrupting parties actively and/or fail-corrupting. These corruption types are, however, inadequate for capturing correct parties that might suffer temporary network failures and/or localized faults - these are particularly relevant for MPC over large, global scale networks. Omission faults and general adversary structures have been proposed as more suitable alternatives. However, to date, there is no characterization of the feasibility landscape combining the above ramifications of fault types and patterns. In this work we provide a tight characterization of feasibility of MPC in the presence of general adversaries - characterized by an adversary structure - that combine omission and active corruption. To this front we first provide a tight characterization of feasibility for Byzantine agreement (BA), a key tool in MPC protocols - this BA result can be of its own separate significance. Subsequently, we demonstrate that the common techniques employed in the threshold MPC literature to deal with omission corruptions do not work in the general adversary setting, not even for proving bounds that would appear straightforward, e.g, sufficiency of the well known $Q^3$ condition on omission-only general adversaries. Nevertheless we provide a new protocol that implements general adversary MPC under a surprisingly complex, yet tight as we prove, bound. All our results are for the classical synchronous model of computation. As a contribution of independent interest, our work puts forth, for the first time, a formal treatment of general-adversary MPC with (active and) omission corruptions in Canetti&#x27;s universal composition framework.

  匹配依据：MPC: multi party computation

  </details>

- **FOLEAGE: $\\mathbb {F}\_{\\scriptstyle 4}$OLE-Based Multi-party Computation for Boolean Circuits.**
  2025 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-981-96-0938-3_3)
  Geoffroy Couteau, Dung Bui, Clément Ducros, Sacha Servan-Schreiber, Maxime Bombar, Alain Couvreur

- **Evolving Secret Sharing Made Short.**
  2025 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-981-96-0941-3_3) · [IACR ePrint](https://eprint.iacr.org/2023/1534)
  Danilo Francati, Daniele Venturi

  <details><summary>摘要 / Abstract</summary>

  Evolving secret sharing (Komargodski, Naor, and Yogev, TCC’16) generalizes the notion of secret sharing to the setting of evolving access structures, in which the share holders are added to the system in an online manner, and where the dealer does not know neither the access structure nor the maximum number of parties in advance. Here, the main difficulty is to distribute shares to the new players without updating the shares of old players; moreover, one would like to minimize the share size as a function of the number of players. In this paper, we initiate a systematic study of evolving secret sharing in the computational setting, where the maximum number of parties is polynomial in the security parameter, but the dealer still does not know this value, neither it knows the access structure in advance. Moreover, the privacy guarantee only holds against computationally bounded adversaries corrupting an unauthorized subset of the players. Our main result is that for many interesting, and practically relevant, evolving access structures (including graphs access structures, DNF and CNF formulas access structures, monotone circuits access structures, and threshold access structures), under standard hardness assumptions, there exist efficient secret sharing schemes with computational privacy and in which the shares are succinct (i.e., much smaller compared to the size of a natural computational representation of the evolving access structure).

  匹配依据：MPC: secret sharing

  </details>

- **EoTMP: Efficient Over-Threshold Multi-Party Private Set Intersection.**
  2025 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2025.3639987)
  Xiaoguang Li, Hui Li, Xingwen Zhao, Song Bian, Qingwen Li

- **Enabling Two-Party Secure Computation on Set Intersection.**
  2025 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2025.3561472) · [IACR ePrint](https://eprint.iacr.org/2023/609)
  Alptekin Küpçü, Ferhat Karakoç

  <details><summary>摘要 / Abstract</summary>

  In this paper, we propose the first linear two-party secure-computation private set intersection (PSI) protocol, in the semi-honest adversary model, computing the following functionality. One of the parties ($P_X$) inputs a set of items $X = \{x_j \mid 1 \le j \le n_X\}$, whereas the other party ($P_Y$) inputs a set of items $Y = \{y_i \mid 1\le i \le n_Y \}$ and a set of corresponding data pairs $D_Y = \{ (d_i^0,d_i^1) \mid 1 \le i \le n_Y\}$ having the same cardinality with $Y$. While $P_Y$ outputs nothing, $P_X$ outputs a set of data $D_X = \{ d_i^{b_i} \mid b_i = 1 \text{ if } y_i \in X, b_i = 0 \text{ otherwise}\}$. This functionality is generally required when the PSI protocol is used as a part of a larger secure two-party computation such as threshold PSI or any function of the intersection in general. In literature, there are linear circuit and secure-computation PSI proposals, such as Pinkas et al. PSI protocol (Eurocrypt 2019), our PSI protocol (CANS 2020) and Chandran et al. PSI protocol (PETS 2022), for similar functionalities but having a cuckoo table mapping in the functionality, which complicates the application of different secure computation techniques on top of the output of the PSI protocol. We also show that the idea in the construction of our secure-computation PSI protocol having the functionality mentioned above can be utilized to convert the existing circuit PSI and secure-computation PSI protocols into the protocols realizing the functionality not having the cuckoo table mapping. We provide this conversion method as a separate protocol, which is one of the main contributions of this work. While creating the protocol, as a side contribution, we provide a one-time batch oblivious programmable pseudo-random function based on garbled Bloom filters.

  匹配依据：MPC: private set intersection, secure computation, secure two party computation

  </details>

- **Efficient and Privacy-Preserving Feature Selection Based on Multiparty Computation.**
  2025 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2025.3546843)
  Hao Guo, Lu Zhou, Luyao Wang, Weibin Wu

- **Efficient Three-Party ECDSA Signature Based on Replicated Secret Sharing With Identifiable Abort.**
  2025 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2025.3607264)
  Chenkai Zeng, Min Luo, Yu Peng, Wenjing Cheng, Qi Feng, Qingcai Luo, Xiaolin Yang

- **Efficient Permutation Correlations and Batched Random Access for Two-Party Computation.**
  2025 · MPC · 含会议/期刊记录 · [PKC](https://doi.org/10.1007/978-3-031-91829-2_3) · [IACR ePrint](https://eprint.iacr.org/2024/547)
  Srinivasan Raghuraman, Peter Rindal, Harshal Shah, Stanislav Peceny

  <details><summary>摘要 / Abstract</summary>

  In this work we formalize the notion of a two-party permutation correlation $(A, B), (C, \pi)$ s.t. $\pi(A)=B+C$ for a random permutation $\pi$ of $n$ elements and vectors $A,B,C\in \mathbb{F}^n$. This correlation can be viewed as an abstraction and generalization of the Chase et al. (Asiacrypt 2020) share translation protocol. We give a systematization of knowledge for how such a permutation correlation can be derandomized to allow the parties to perform a wide range of oblivious permutations of secret-shared data. This systematization immediately enables the translation of various popular honest-majority protocols to be efficiently instantiated in the two-party setting, e.g. collaborative filtering, sorting, database joins, graph algorithms, and many more. We give two novel protocols for efficiently generating a random permutation correlation. The first uses MPC-friendly PRFs to generate a correlation of $n$ elements, each of size $\ell=\log|\mathbb{F}|$ bits, with $O(n\ell)$ bit-OTs, time, communication, and only 3 rounds including setup. Similar asymptotics previously required relatively expensive public-key cryptography, e.g. Paillier or LWE. Our protocol implementation for $n=2^{20},\ell=128$ requires just 7 seconds &amp; $\sim2\ell n$ OTs for communication, a respective 40 &amp; $1.1\times$ improvement on the LWE solution of Juvekar at al. (CCS 2018). The second protocol is based on pseudo-random correlation generators and achieves an overhead that is sublinear in the string length $\ell$, i.e. the communication and number of OTs is $O(n\log \ell)$. The overhead of the latter protocol has larger hidden constants, and therefore is more efficient only when long strings are permuted, e.g. in graph algorithms. Finally, we present a suite of highly efficient protocols based on permutations for performing various batched random access operations. These include the ability to extract a hidden subset of a secret-shared list. More generally, we give ORAM-like protocols for obliviously reading and writing from a list in a batched manner. We argue that this suite of batched random access protocols should be a first class primitive in the MPC practitioner&#x27;s toolbox.

  匹配依据：MPC: two party computation

  </details>

- **Efficient Multi-Party Private Set Union Without Non-Collusion Assumptions.**
  2025 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/dong-minglang) · [IACR ePrint](https://eprint.iacr.org/2024/1146)
  Cong Zhang, Yujie Bai, Minglang Dong, Yu Chen

  <details><summary>摘要 / Abstract</summary>

  Multi-party private set union (MPSU) protocol enables $m$ $(m &gt; 2)$ parties, each holding a set, to collectively compute the union of their sets without revealing any additional information to other parties. There are two main categories of multi-party private set union (MPSU) protocols: The first category builds on public-key techniques, where existing works require a super-linear number of public-key operations, resulting in poor practical efficiency. The second category builds on oblivious transfer and symmetric-key techniques. The only work in this category, proposed by Liu and Gao (ASIACRYPT 2023), features the best concrete performance among all existing protocols, but still has super-linear computation and communication. Moreover, it does not achieve the standard semi-honest security, as it inherently relies on a non-collusion assumption, which is unlikely to hold in practice. There remain two significant open problems so far: no MPSU protocol achieves semi-honest security based on oblivious transfer and symmetric-key techniques; no MPSU protocol achieves both linear computation and linear communication complexity. In this work, we resolve both of them. - We propose the first MPSU protocol based on oblivious transfer and symmetric-key techniques in the standard semi-honest model. This protocol&#x27;s online performance is $3.9-10.0 \times$ faster than Liu and Gao in the LAN setting. Concretely, our protocol requires only $4.4$ seconds in online phase for $3$ parties with sets of $2^{20}$ items each. - We propose the first MPSU protocol achieving linear computation and linear communication complexity, based on public-key operations. This protocol has the best total performance in the WAN settings, due to a factor of $3.0-36.5\times$ improvement in terms of overall communication compared to Liu and Gao. Concretely, on slow network ($50$ Mbps), their protocol takes $6.6$ hours to run for $9$ parties with sets of $2^{18}$ items each, whereas ours only takes $47$ minutes. We implement our protocols and conduct extensive experiments to compare the performance of our protocols and the state-of-the-art. To the best of our knowledge, our code is the first correct and secure implementation of MPSU that reports on large-size experiments.

  匹配依据：MPC: oblivious transfer, private set union

  </details>

- **Efficient Fuzzy Private Set Intersection from Fuzzy Mapping.**
  2025 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-981-96-0938-3_2) · [IACR ePrint](https://eprint.iacr.org/2024/1462)
  Ying Gao, Xiang Liu, Longxin Wang, Yuanchao Luo, Lin Qi

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) allows Sender holding a set \(X\) and Receiver holding a set \(Y\) to compute only the intersection \(X\cap Y\) for Receiver. We focus on a variant of PSI, called fuzzy PSI (FPSI), where Receiver only gets points in \(X\) that are at the distance not greater than a threshold from some points in \(Y\). Most current FPSI approaches first pick out pairs of points that are potentially close and then determine whether the distance of each selected pair is indeed small enough to yield FPSI result. Their complexity bottlenecks stem from the excessive number of point pairs selected by the first picking process. Regarding this process, we consider a more general notion, called fuzzy mapping (Fmap), which can map each point of two parties to a set of identifiers, with closely located points having a same identifier, which forms the selected point pairs. We initiate the formal study on Fmap and show novel Fmap instances for Hamming and \(L_\infty\) distances to reduce the number of selected pairs. We demonstrate the powerful capability of Fmap with some superior properties in constructing FPSI variants and provide a generic construction from Fmap to FPSI. Our new Fmap instances lead to the fastest semi-honest secure FPSI protocols in high-dimensional space to date, for both Hamming and general \(L_{\mathsf p\in [1, \infty]}\) distances. For Hamming distance, our protocol is the first one that achieves strictly linear complexity with input sizes. For \(L_{\mathsf p\in [1, \infty]}\) distance, our protocol is the first one that achieves linear complexity with input sizes, dimension, and threshold.

  匹配依据：MPC: private set intersection

  </details>

- **Efficient Collaborative Data Cleaning Using Private Set Intersection and Encoding for Unbalanced Datasets.**
  2025 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2025.3594871)
  Fagen Li, Wenyi Li, Yu Zhou, Xiaojun Zhang, Jingting Xue, Wenzheng Zhang

- **Efficient 2PC for Constant Round Secure Equality Testing and Comparison.**
  2025 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity25/presentation/lu) · [IACR ePrint](https://eprint.iacr.org/2024/949)
  Xin Kang, Chun Chen, Xiaoyuan Zhang, Kui Ren, Tianpei Lu, Yang Liu, Zhuo Ma, Bingsheng Zhang

  <details><summary>摘要 / Abstract</summary>

  Secure equality testing and comparison are two important primitives widely used in many secure computation scenarios, such as privacy-preserving machine learning, private set intersection, and secure data mining, etc. This work proposes new constant-round two-party computation (2PC) protocols for secure equality testing and comparison. Our protocols are designed in the online/offline paradigm. For 32-bit inputs, the online communication cost of our equality testing protocol and secure comparison protocol are as low as 76 bits (1\% of ABY) and 384 bits (5\% of ABY) , respectively. Our benchmarks show that (i) for 32-bit equality testing, our scheme performs $9 \times$ faster than the Guo \emph{et al.} (EUROCRYPT 2023) and $15 \times$ of the garbled circuit (GC) with the half-gate optimization (CRYPTO 2015). (ii) for 32-bit secure comparison, our scheme performs $3 \times$ faster than Guo \emph{et al.} (EUROCRYPT 2023), $6 \times$ faster than both Rathee \emph{et al.} (CCS 2020) and GC with the half-gate optimization.

  匹配依据：MPC: garbled circuit, private set intersection, secure computation, two party computation

  </details>

- **Distributed Function Secret Sharing and Applications.**
  2025 · MPC · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/distributed-function-secret-sharing-and-applications/)
  Dongxiao Liu, Meng Hao, Hanxiao Chen, Pengzhi Xing, Hongwei Li, Jia Hu

- **Dishonest Majority Multiparty Computation over Matrix Rings.**
  2025 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-981-96-0938-3_10) · [IACR ePrint](https://eprint.iacr.org/2023/1912)
  Hongqing Liu, Taoxu Zou, Chen Yuan, Chaoping Xing

  <details><summary>摘要 / Abstract</summary>

  The privacy-preserving machine learning (PPML) has gained growing importance over the last few years. One of the biggest challenges is to improve the efficiency of PPML so that the communication and computation costs of PPML are affordable for large machine learning models such as deep learning. As we know, linear algebra such as matrix multiplication occupies a significant part of the computation in deep learning such as deep convolutional neural networks (CNN). Thus, it is desirable to propose the MPC protocol specialized for the matrix operations. In this work, we propose a dishonest majority MPC protocol over matrix rings which supports matrix multiplication and addition. Our MPC protocol can be seen as a variant of SPDZ protocol, i.e., the MAC and global key of our protocol are vectors of length $m$ and the secret of our protocol is an $m\times m$ matrix. Compared to the classic SPDZ protocol, our MPC protocol reduces the communication complexity by at least $m$ times to securely compute a matrix multiplication. We also show that the communication complexity of our MPC protocol is asymptotically as good as [16] which also presented a dishonest majority MPC protocol specialized for matrix operations, i.e., the communication complexity of securely computing a multiplication gate is $O(m^2n^2\log q)$ in the preprocessing phase and $O(m^2n\log q)$ in the online phase. The share size and the number of multiplications of our protocol are reduced by around $50\%$ and $40\%$ of [16], respectively. However, we take a completely different approach. The protocol in [16] uses a variant of BFV scheme to embed a whole matrix into a single ciphertext and then treats the matrix operation as the entry-wise operation in the ciphertext while our approach resorts to a variant of vector linear oblivious evaluation (VOLE) called the subfield VOLE [33] which can securely compute the additive sharing of $v {\bf x}$ for $v\in \mathbb{F}_{q^b}, {\bf x}\in \mathbb{F}_q^a$ with sublinear communication complexity. Finally, we note that our MPC protocol can be easily extended to small fields.

  匹配依据：MPC: multiparty computation

  </details>

- **Dash: Accelerating Distributed Private Convolutional Neural Network Inference with Arithmetic Garbled Circuits.**
  2025 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2302.06361) · [TCHES](https://doi.org/10.46586/TCHES.V2025.I1.420-449)
  Sebastian Berndt, Ida Bruhns, Jonas Sander, Thomas Eisenbarth

  <details><summary>摘要 / Abstract</summary>

  The adoption of machine learning solutions is rapidly increasing across all parts of society. As the models grow larger, both training and inference of machine learning models is increasingly outsourced, e.g. to cloud service providers. This means that potentially sensitive data is processed on untrusted platforms, which bears inherent data security and privacy risks. In this work, we investigate how to protect distributed machine learning systems, focusing on deep convolutional neural networks. The most common and best-performing mixed MPC approaches are based on HE, secret sharing, and garbled circuits. They commonly suffer from large performance overheads, big accuracy losses, and communication overheads that grow linearly in the depth of the neural network. To improve on these problems, we present Dash, a fast and distributed private convolutional neural network inference scheme secure against malicious attackers. Building on arithmetic garbling gadgets [BMR16] and fancy-garbling [BCM+19], Dash is based purely on arithmetic garbled circuits. We introduce LabelTensors that allow us to leverage the massive parallelity of modern GPUs. Combined with state-of-the-art garbling optimizations, Dash outperforms previous garbling approaches up to a factor of about 100. Furthermore, we introduce an efficient scaling operation over the residues of the Chinese remainder theorem representation to arithmetic garbled circuits, which allows us to garble larger networks and achieve much higher accuracy than previous approaches. Finally, Dash requires only a single communication round per inference step, regardless of the depth of the neural network, and a very small constant online communication volume.

  匹配依据：MPC: garbled circuits, secret sharing

  </details>

- **Compute, but Verify: Efficient Multiparty Computation over Authenticated Inputs.**
  2025 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-981-96-0938-3_5) · [IACR ePrint](https://eprint.iacr.org/2022/1648)
  Moumita Dutta, Chaya Ganesh, Sikhar Patranabis, Nitin Singh

  <details><summary>摘要 / Abstract</summary>

  Traditional notions of secure multiparty computation (MPC) allow mutually distrusting parties to jointly compute a function over their private inputs, but typically do not specify how these inputs are chosen. Motivated by real-world applications where corrupt inputs could adversely impact privacy and operational legitimacy, we consider a notion of authenticated MPC where the inputs are authenticated, e.g., signed using a digital signature by some certification authority. We propose a generic and efficient compiler that transforms any linear secret sharing based honest-majority MPC protocol into one with input authentication. Our compiler incurs significantly lower computational costs and competitive communication overheads when compared to the best existing solutions, while entirely avoiding the (potentially expensive) protocol-specific techniques and pre-processing requirements that are inherent to these solutions. For $n$-party honest majority MPC protocols with abort security where each party has $\ell$ inputs, our compiler incurs $O(n\log \ell)$ communication overall and a computational overhead of $O(\ell)$ group exponentiations per party (the corresponding overheads for the most efficient existing solution are $O(n^2)$ and $O(\ell n)$). Finally, for a corruption threshold $t&lt;n/3$, our compiler preserves the stronger identifiable abort security of the underlying MPC protocol. No existing solution for authenticated MPC achieves this regardless of the corruption threshold. Along the way, we make several technical contributions that are of independent interest. This includes the notion of distributed proofs of knowledge and concrete realizations of the same for several relations of interest, such as proving knowledge of many popularly used digital signature schemes, and proving knowledge of opening of a Pedersen commitment.

  匹配依据：MPC: multiparty computation, secret sharing, secure multiparty computation

  </details>

- **Bitwise Garbling Schemes - A Model with 32λ\\documentclass\[12pt\]{minimal} \\usepackage{amsmath} \\usepackage{wasysym} \\usepackage{amsfonts} \\usepackage{amssymb} \\usepackage{amsbsy} \\usepackage{mathrsfs} \\usepackage{upgreek} \\setlength{\\oddsidemargin}{-69pt} \\begin{document}$$\\frac{3}{2}\\lambda $$\\end{document}-Bit Lower Bound of Ciphertexts.**
  2025 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-032-01884-7_15)
  Honggang Hu, Changhong Xu, Fei Xu

- **BitGC: Garbled Circuits with 1 Bit per Gate.**
  2025 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-031-91098-2_16) · [IACR ePrint](https://eprint.iacr.org/2024/1988)
  Xiao Wang, Hanlin Liu, Yu Yu, Kang Yang

  <details><summary>摘要 / Abstract</summary>

  We present BitGC, a garbling scheme for Boolean circuits with 1 bit per gate communication based on either ring learning with errors (RLWE) or NTRU assumption, with key-dependent message security. The garbling consists of 1) a homomorphically encrypted seed that can be expanded to encryption of many pseudo-random bits and 2) one-bit stitching information per gate to reconstruct garbled tables from the expanded ciphertexts. By using low-complexity PRGs, both the garbling and evaluation of each gate require only O(1) homomorphic addition/multiplication operations without bootstrapping.

  匹配依据：MPC: garbled circuits, garbling scheme

  </details>

- **An Improvement Upon the Bounds for the Local Leakage Resilience of Shamir's Secret Sharing Scheme.**
  2025 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-78023-3_13)
  Dustin Kasser

- **Adaptive Security, Erasures, and Network Assumptions in Communication-Local MPC.**
  2025 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-78023-3_10) · [IACR ePrint](https://eprint.iacr.org/2024/1489)
  Juan A. Garay, Ankit Kumar Misra, Nishanth Chandran, Vassilis Zikas, Rafail Ostrovsky, Juan Garay

  <details><summary>摘要 / Abstract</summary>

  The problem of reliable/secure all-to-all communication over low-degree networks has been essential for communication-local (CL) n-party MPC (i.e., MPC protocols where every party directly communicates only with a few, typically polylogarithmic in n, parties) and more recently for communication over ad hoc networks, which are used in blockchain protocols. However, a limited number of adaptively secure solutions exist, and they all make relatively strong assumptions on the ability of parties to act in some specific manner before the adversary can corrupt them. Two such assumptions were made in the work of Chandran et al. [ITCS ’15]---parties can (a) multisend messages to several receivers simultaneously; and (b) securely erase the message and the identities of the receivers, before the adversary gets a chance to corrupt the sender (even if a receiver is corrupted). A natural question to ask is: Are these assumptions necessary for adaptively secure CL MPC? In this paper, we characterize the feasibility landscape for all-to-all reliable message transmission (RMT) under these two assumptions, and use this characterization to obtain (asymptotically) tight feasibility results for CL MPC. – First, we prove a strong impossibility result for a broad class of RMT protocols, termed here store-and-forward protocols, which includes all known communication protocols for CL MPC from standard cryptographic assumptions. Concretely, we show that no such protocol with a certain expansion rate can tolerate a constant fraction of parties being corrupted. – Next, under the assumption of only a PKI, we show that assuming secure erasures, we can obtain an RMT protocol between all pairs of parties with polylogarithmic locality (even without assuming multisend) for the honest majority setting. We complement this result by showing a negative result for the setting of dishonest majority. – Finally, and somewhat surprisingly, under stronger assumptions (i.e., trapdoor permutations with a reverse domain sampler, and compact and malicious circuit-private FHE), we construct a polylogarithmic-locality all-to-one RMT protocol, which is adaptively secure and tolerates any constant fraction of corruptions, without assuming either secure erasures or multisend. This last result uses a novel combination of adaptively secure (e.g., non-committing) encryption and (static) FHE to bypass the impossibility of compact adaptively secure FHE by Katz et al. [PKC’13], which we believe may be of independent interest. Intriguingly, even such assumptions do not allow reducing all-to-all RMT to all-to-one RMT (a reduction which is trivial in the non-CL setting). Still, we can implement what we call sublinear output-set RMT (SOS-RMT for short). We show how SOS-RMT can be used for SOS-MPC under the known bounds for feasibility of MPC in the standard (i.e., non-CL) setting assuming, in addition to SOS-RMT, an anonymous PKI.

  匹配依据：MPC: mpc (context)

  </details>

- **A Scheme of Robust Privacy-Preserving Multi-Party Computation via Public Verification.**
  2025 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2025.3555284)
  Keke Gai, Jing Yu, Weizhi Meng, Dongjue Wang, Liehuang Zhu

- **A Note on Low-Communication Secure Multiparty Computation via Circuit Depth-Reduction.**
  2025 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-78023-3_6) · [IACR ePrint](https://eprint.iacr.org/2024/1473)
  Geoffroy Couteau, Pierre Charbit, Pierre Meyer, Reza Naserasr

  <details><summary>摘要 / Abstract</summary>

  We consider the graph-theoretic problem of removing (few) nodes from a directed acyclic graph in order to reduce its depth. While this problem is intractable in the general case, we provide a variety of algorithms in the case where the graph is that of a circuit of fan-in (at most) two, and explore applications of these algorithms to secure multiparty computation with low communication. Over the past few years, a paradigm for low-communication secure multiparty computation has found success based on decomposing a circuit into low-depth ``chunks&#x27;&#x27;. This approach was however previously limited to circuits with a ``layered&#x27;&#x27; structure. Our graph-theoretic approach extends this paradigm to all circuits. In particular, we obtain the following contributions: 1) Fractionally linear-communication MPC in the correlated randomness model: We provide an $N$-party protocol for computing an $n$-input, $m$-output $\mathsf{F}$-arithmetic circuit with $s$ internal gates (over any basis of binary gates) with communication complexity $(\frac{2}{3}s + n + m)\cdot N\cdot\log |\mathsf{F}|$, which can be improved to $((1+\epsilon)\cdot\frac{2}{5}s+n+m)\cdot N\cdot\log |\mathsf{F}|$ (at the cost of increasing the computational overhead from a small constant factor to a large one). Previously, comparable protocols either used more than $s\cdot N\cdot \log |\mathsf{F}|$ bits of communication, required super-polynomial computation, were restricted to layered circuits, or tolerated a sub-optimal corruption threshold. 2) Sublinear-Communication MPC: Assuming the existence of $N$-party Homomorphic Secret Sharing for logarithmic depth circuits (respectively doubly logarithmic depth circuits), we show there exists sublinear-communication secure $N$-party computation for \emph{all} $\log^{1+o(1)}$-depth (resp.~$(\log\log)^{1+o(1)}$-depth) circuits. Previously, this result was limited to $(\mathcal{O}(\log))$-depth (resp.~$(\mathcal{O}(\log\log))$-depth) circuits, or to circuits with a specific structure (e.g. layered). 3) The 1-out-of-M-OT complexity of MPC: We introduce the `` 1-out-of-M-OT complexity of MPC&#x27;&#x27; of a function $f$, denoted $C_M(f)$, as the number of oracle calls required to securely compute $f$ in the 1-out-of-M-OT hybrid model. We establish the following upper bound: for every $M\geq 2$, $C_N(f) \leq (1+g(M))\cdot \frac{2 |f|}{5}$, where $g(M)$ is an explicit vanishing function. We also obtain additional contributions to reducing the amount of bootstrapping for fully homomorphic encryption, and to other types of sublinear-communication MPC protocols such as those based on correlated symmetric private information retrieval.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>
