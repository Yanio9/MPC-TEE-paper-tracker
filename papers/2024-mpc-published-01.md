# 2024 · MPC · 含会议/期刊记录 · 第 1/1 页

[总目录](../PAPERS.md)

- **Secret Sharing with Snitching.**
  2024-10-09 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3658644.3690296) · [IACR ePrint](https://eprint.iacr.org/2024/1610)
  Tomasz Lizurej, Marcin Mielniczuk, Stefan Dziembowski, Sebastian Faust

  <details><summary>摘要 / Abstract</summary>

  We address the problem of detecting and punishing shareholder collusion in secret-sharing schemes. We do it in the recently proposed cryptographic model called individual cryptography (Dziembowski, Faust, and Lizurej, Crypto 2023), which assumes that there exist tasks that can be efficiently computed by a single machine but distributing this computation across multiple (mutually distrustful devices) is infeasible. Within this model, we introduce a novel primitive called secret sharing with snitching (SSS), in which each attempt to illegally reconstruct the shared secret $S$ results in a proof that can be used to prove such misbehavior (and, e.g., financially penalize the cheater on a blockchain). This holds in a very strong sense, even if the shareholders attempt not to reconstruct the entire secret~$S$ but only learn some partial information about it. Our notion also captures the attacks performed using multiparty computation protocols (MPCs), i.e., those where the malicious shareholders use MPCs to compute partial information on $S$. The main idea of SSS is that any illegal reconstruction can be proven and punished, which suffices to discourage illegal secret reconstruction. Hence, our SSS scheme effectively prevents shareholders&#x27; collusion. We provide a basic definition of threshold ($t$-out-of-$n$) SSS. We then show how to construct it for $t = n$, and later, we use this construction to build an SSS scheme for an arbitrary $t$. In order to prove the security of our construction, we introduce a generalization of the random oracle model (Bellare, Rogaway, CCS 1993), which allows modelling hash evaluations made inside MPC.

  匹配依据：MPC: multiparty computation, secret sharing

  </details>

- **MPC-in-the-Head Framework without Repetition and its Applications to the Lattice-based Cryptography.**
  2024-10-08 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00157) · [IACR ePrint](https://eprint.iacr.org/2024/1591)
  Qianwen Gao, Long Chen, Zhenfeng Zhang, Weihao Bai

  <details><summary>摘要 / Abstract</summary>

  The MPC-in-the-Head framework has been pro- posed as a solution for Non-Interactive Zero-Knowledge Arguments of Knowledge (NIZKAoK) due to its efficient proof generation. However, most existing NIZKAoK constructions using this approach require multiple MPC evaluations to achieve negligible soundness error, resulting in proof size and time that are asymptotically at least λ times the size of the circuit of the NP relation. In this paper, we propose a novel method to eliminate the need for repeated MPC evaluations, resulting in a NIZKAoK protocol for any NP relation that we call Diet. The proof size and time of Diet are asymptotically only polylogarithmic with respect to the size of the circuit C of the NP relation but are independent of the security parameter λ. Hence, both the proof size and time can be significantly reduced. Moreover, Diet offers promising concrete efficiency for proving Learning With Errors (LWE) problems and its variants. Our solution provides significant advantages over other schemes in terms of both proof size and proof time, when considering both factors together. Specifically, Diet is a promising method for proving knowledge of secret keys for lattice-based key encapsulation mechanisms (KEMs) such as Frodo and Kyber, offering a practical solution to future post-quantum certificate management. For Kyber 512, our implementation achieves an online proof size of 83.65 kilobytes (KB) with a preprocessing overhead of 152.02KB. The implementation is highly efficient, with an online proof time of only 0.68 seconds and a preprocessing time of 0.81 seconds. Notably, our approach provides the first reported implementation of proving knowledge of secret keys for Kyber 512 using post-quantum primitives-based zero-knowledge proofs.

  匹配依据：MPC: mpc (context)

  </details>

- **Coral: Maliciously Secure Computation Framework for Packed and Mixed Circuits.**
  2024-09-02 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3658644.3690223) · [IACR ePrint](https://eprint.iacr.org/2024/1372)
  Zhicong Huang, Wen-jie Lu, Wenguang Chen, Yuchen Wang, Tao Wei, Cheng Hong, WenGuang Chen

  <details><summary>摘要 / Abstract</summary>

  Achieving malicious security with high efficiency in dishonest-majority secure multiparty computation is a formidable challenge. The milestone works SPDZ and TinyOT have spawn a large family of protocols in this direction. For boolean circuits, state-of-the-art works (Cascudo et. al, TCC 2020 and Escudero et. al, CRYPTO 2022) have proposed schemes based on reverse multiplication-friendly embedding (RMFE) to reduce the amortized cost. However, these protocols are theoretically described and analyzed, resulting in a significant gap between theory and concrete efficiency. Our work addresses existing gaps by refining and correcting several issues identified in prior research, leading to the first practically efficient realization of RMFE. We introduce an array of protocol enhancements, including RMFE-based quintuples and (extended) double-authenticated bits, aimed at improving the efficiency of maliciously secure boolean and mixed circuits. The culmination of these efforts is embodied in Coral, a comprehensive framework developed atop the MP-SPDZ library. Through rigorous evaluation across multiple benchmarks, Coral demonstrates a remarkable efficiency gain, outperforming the foremost theoretical approach by Escudero et al. (which incorporates our RMFE foundation albeit lacks our protocol enhancements) by a factor of 16-30×, and surpassing the leading practical implementation for Frederiksen et al. (ASIACRYPT 2015) by 4-7×.

  匹配依据：MPC: secure computation, secure multiparty computation

  </details>

- **Secure Multiparty Computation with Lazy Sharing.**
  2024-08-28 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3658644.3690207) · [IACR ePrint](https://eprint.iacr.org/2024/1347)
  Cong Zhang, Shuaishuai Li, Dongdai Lin

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) protocols enable $n$ parties, each with private inputs, to compute a given function without leaking information beyond the outputs. One of the main approaches to designing efficient MPC protocols is to use secret sharing. In general, secret sharing based MPC contains three phases: input sharing, circuit evaluation, and output recovery. If the adversary corrupts at most $t$ parties, the protocol typically uses $(t,n)$ threshold secret sharing to share the inputs. In this work, we consider a weaker variant of threshold secret sharing called lazy threshold secret sharing (or simply lazy sharing) and show that - Lazy sharing can serve as a viable alternative to threshold secret sharing in MPC without compromising security. - Lazy sharing could be generated more efficiently than threshold secret sharing. As a result, replacing threshold secret sharing with lazy sharing can lead to a more efficient input sharing phase. Moreover, we propose that the efficiency of the circuit evaluation phase can also be further improved. To support this claim, we apply lazy sharing to several state-of-the-art MPC protocols and analyze the efficiency gain in various settings. These protocols include the GMW protocol (Goldreich et al., STOC 1987), the AFLNO protocol (Araki et al., CCS 2016), and the SPDZ protocol (Damg{\aa}rd et al., CRYPTO 2012). By doing so, we analyze the efficiency gains in various settings and highlight the advantages of incorporating lazy sharing into MPC protocols.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Unbalanced Private Set Union with Reduced Computation and Communication.**
  2024-08-27 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3658644.3690308) · [IACR ePrint](https://eprint.iacr.org/2024/1340)
  Cong Zhang, Meng Hao, Anyu Wang, Liqiang Peng, Weiran Liu, Xiaoyun Wang, Yu Chen

  <details><summary>摘要 / Abstract</summary>

  Private set union (PSU) is a cryptographic protocol that allows two parties to compute the union of their sets without revealing anything else. Despite some efficient PSU protocols that have been proposed, they mainly focus on the balanced setting, where the sets held by the parties are of similar size. Recently, Tu et al. (CCS 2023) proposed the first unbalanced PSU protocol which achieves sublinear communication complexity in the size of the larger set. In this paper, we are interested in improving the efficiency of the unbalanced PSU protocol. We find that oblivious key-value store (OKVS) data structure plays an essential role in the most recently proposed PSU constructions and formalize unbalanced PSU as an OKVS decoding process with sublinear communication. Our key insight lies in when OKVS satisfies sparsity property, obtaining the necessary decoding information precisely aligns with the batch private information retrieval (BatchPIR) problem. We give two concrete constructions of unbalanced PSU protocols based on different OKVS encoding strategies. The first is based on oblivious PRF (OPRF) and a newly introduced cryptographic protocol called permuted private equality test, while the second is based on re-randomizable public key encryption. Both our two constructions achieve sublinear communication complexity in the size of the larger set. We implement our two unbalanced PSU protocols and compare them with the state-of-the-art unbalanced PSU of Tu et al. Experiments show that our protocols achieve a $1.3-5.6\times $ speedup in running time and $2.1-11.8\times$ shrinking in communication cost, depending on set sizes and network environments.

  匹配依据：MPC: private set union

  </details>

- **GAuV: A Graph-Based Automated Verification Framework for Perfect Semi-Honest Security of Multiparty Computation Protocols.**
  2024-07-02 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00131) · [IACR ePrint](https://eprint.iacr.org/2024/1078)
  Wei Zhang, Shizhen Xu, Xingyu Xie, Tuowei Wang, Yifei Li, Jun Zhu, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  Proving the security of a Multiparty Computation (MPC) protocol is a difficult task. Under the current simulation-based definition of MPC, a security proof consists of a simulator, which is usually specific to the concrete protocol and requires to be manually constructed, together with a theoretical analysis of the output distribution of the simulator and corrupted parties&#x27; views in the real world. This presents an obstacle in verifying the security of a given MPC protocol. Moreover, an instance of a secure MPC protocol can easily lose its security guarantee due to careless implementation, and such a security issue is hard to detect in practice. In this work, we propose a general automated framework to verify the perfect security of instances of MPC protocols against the semi-honest adversary. Our framework has perfect soundness: any protocol that is proven secure under our framework is also secure under the simulation-based definition of MPC. We demonstrate the completeness of our framework by showing that for any instance of the well-known BGW protocol, our framework can prove its security for every corrupted party set with polynomial time. Unlike prior work that only focuses on black-box privacy which requires the outputs of corrupted parties to contain no information about the inputs of the honest parties, our framework may potentially be used to prove the security of arbitrary MPC protocols. We implement our framework as a prototype. The evaluation shows that our prototype automatically proves the perfect semi-honest security of BGW protocols and B2A (binary to arithmetic) conversion protocols in reasonable durations.

  匹配依据：MPC: multiparty computation

  </details>

- **AITIA: Efficient Secure Computation of Bivariate Causal Discovery.**
  2024-06-30 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3658644.3670337) · [IACR ePrint](https://eprint.iacr.org/2024/1065)
  Lun Wang, Ni Trieu, Truong Son Nguyen, Evgenios M. Kornaropoulos

  <details><summary>摘要 / Abstract</summary>

  Researchers across various fields seek to understand causal relationships but often find controlled experiments impractical. To address this, statistical tools for causal discovery from naturally observed data have become crucial. Non-linear regression models, such as Gaussian process regression, are commonly used in causal inference but have limitations due to high costs when adapted for secure computation. Support vector regression (SVR) offers an alternative but remains costly in an Multi-party computation context due to conditional branches and support vector updates. In this paper, we propose Aitia, the first two-party secure computation protocol for bivariate causal discovery. The protocol is based on optimized multi-party computation design choices and is secure in the semi-honest setting. At the core of our approach is BSGD-SVR, a new non-linear regression algorithm designed for MPC applications, achieving both high accuracy and low computation and communication costs. Specifically, we reduce the training complexity of the non-linear regression model from approximately from $\mathcal{O}(N^3)$ to $\mathcal{O}(N^2)$ where $N$ is the number of training samples. We implement Aitia using CrypTen and assess its performance across various datasets. Empirical evaluations show a significant speedup of $3.6\times$ to $340\times$ compared to the baseline approach.

  匹配依据：MPC: multi party computation, secure computation

  </details>

- **Stochastic Secret Sharing with 1-Bit Shares and Applications to MPC.**
  2024-06-28 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-031-68388-6_11) · [IACR ePrint](https://eprint.iacr.org/2024/1053)
  Eliran Kachlon, Benny Applebaum

  <details><summary>摘要 / Abstract</summary>

  The problem of minimizing the share size of threshold secret-sharing schemes is a basic research question that has been extensively studied. Ideally, one strives for schemes in which the share size equals the secret size. While this is achievable for large secrets (Shamir, CACM &#x27;79), no similar solutions are known for the case of binary, single-bit secrets. Current approaches often rely on so-called ramp secret sharing that achieves a constant share size at the expense of a slight gap between the privacy and the correctness thresholds. In the case of single-bit shares, this leads to a large gap which is typically unacceptable. The possibility of a meaningful notion of secret sharing scheme with 1-bit shares and almost optimal threshold has been left wide open. Of special interest is the case of threshold 0.5, which is motivated by information-theoretic honest-majority secure multiparty computation (MPC). In this work, we present a new stochastic model for secret-sharing where each party is corrupted by the adversary with probability $p$, independently of the other parties, and correctness and privacy are required to hold with high probability over the choice of the corrupt parties. We present new secret sharing schemes with single-bit shares that tolerate any constant corruption probability $p&lt;0.5$. Our construction is based on a novel connection between such stochastic secret-sharing schemes and error-correcting codes that achieve capacity over the binary erasure channel. Our schemes are linear and multiplicative. We demonstrate the usefulness of the model by using our new schemes to construct MPC protocols with security against an adversary that passively corrupts an arbitrary subset of $0.499n$ of the parties, where the online communication per party consists of a single bit per AND gate and zero communication per XOR gate. Unlike competing approaches for communication-efficient MPC, our solution is applicable even in a real-time model in which the parties should compute a Boolean circuit whose gates arrive in real-time, one at a time, and are not known in advance.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Efficient Secret Sharing for Large-Scale Applications.**
  2024-06-27 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3658644.3670379) · [IACR ePrint](https://eprint.iacr.org/2024/1045)
  Sarvar Patel, Kevin Yeo, Joon Young Seo, Giuseppe Persiano

  <details><summary>摘要 / Abstract</summary>

  Threshold secret sharing enables distributing a message to $n$ parties such that no subset of fewer than $t$ parties can learn the message, whereas any subset of at least $t$ parties can recover the message. Despite being a fundamental primitive, secret sharing still suffers from one significant drawback, where its message reconstruction algorithm is computationally expensive for large privacy thresholds $t$. In this paper, we aim to address this significant drawback. We study general $(t,c)$-ramp secret sharing schemes where the number of parties c needed to reconstruct the secret may be larger than $t$. We present a ramp secret sharing scheme whose reconstruction time is 2-7.8x faster than prior constructions suitable against adversaries that adaptively corrupt parties. For $t = 2^{20}$, our new protocol has reconstruction time of 5 seconds whereas prior work requires nearly half a minute. We see improvements starting from as small as $t = 256$. Furthermore, we obtain correctness threshold as small as $c \ge 1.05t$. To obtain our construction, we first improve the secret sharing frameworks by Cramer et al. (EUROCRYPT&#x27;15) and Applebaum et al. (CRYPTO&#x27;23) from erasure codes. Our new framework obtains secret sharing schemes that may be used against adversaries with adaptive corruptions while requiring only weaker correctness guarantees from the underlying erasure code with a distributed generation property. Furthermore, our new framework also maintains the linear homomorphism of the prior works. Afterwards, we present a concretely efficient erasure code from random band matrices that satisfies the distributed generation property. We show that our secret sharing scheme can improve many real-world applications. In secure aggregation protocols for federated learning, we obtain up to 22% reductions in computational cost by replacing Shamir&#x27;s scheme with our construction. We extend our protocol to obtain a verifiable ramp secret sharing scheme where each party can verify the consistency of the shares. Our new verifiable ramp secret sharing has 8.2-25.2x faster sharing and 2.7-23.2x faster reconstruction time compared to prior works. Finally, we present an improved distributed verifiable random function that may be used for decentralized randomness beacons.

  匹配依据：MPC: secret sharing

  </details>

- **Scalable Private Set Union, with Stronger Security.**
  2024-06-10 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity24/presentation/jia-yanxue) · [IACR ePrint](https://eprint.iacr.org/2024/922)
  Shifeng Sun, Yanxue Jia, Hong-Sheng Zhou, Dawu Gu, Shi-Feng Sun

  <details><summary>摘要 / Abstract</summary>

  Private Set Union (PSU) protocol allows parties, each holding an input set, to jointly compute the union of the sets without revealing anything else. In the literature, scalable PSU protocols follow the “split-execute-assemble” paradigm (Kolesnikov et al., ASIACRYPT 2019); in addition, those fast protocols often use Oblivious Transfer as building blocks. Kolesnikov et al. (ASIACRYPT 2019) and Jia et al. (USENIX Security 2022), pointed out that certain security issues can be introduced in the “split-execute-assemble” paradigm. In this work, surprisingly, we observe that the typical way of invoking Oblivious Transfer also causes unnecessary leakage, and only the PSU protocols based on additively homomorphic encryption (AHE) can avoid the leakage. However, the AHE-based PSU protocols are far from being practical. To bridge the gap, we also design a new PSU protocol that can avoid the unnecessary leakage. Unlike the AHE-based PSU protocols, our new construction only relies on symmetric-key operations other than base OTs, thereby being much more scalable. The experimental results demonstrate that our protocol can obtain at least 873.74× speedup over the best-performing AHE-based scheme. Moreover, our performance is comparable to that of the state-of-the-art PSU protocol (Chen et al., USENIX Security 2023), which also suffers from the unnecessary leakage.

  匹配依据：MPC: oblivious transfer, private set union

  </details>

- **Fast Evaluation of S-Boxes With Garbled Circuits.**
  2024-05-31 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2405.20713) · [TIFS](https://doi.org/10.1109/TIFS.2024.3402145) · [IACR ePrint](https://eprint.iacr.org/2022/1278)
  Aysajan Abidin, Erik Pohle, Bart Preneel

  <details><summary>摘要 / Abstract</summary>

  Garbling schemes are vital primitives for privacy-preserving protocols and secure two-party computation. In projective garbling schemes, $n$ values are assigned to each wire in the circuit. Current state-of-the-art schemes project two values. This paper presents a projective garbling scheme that assigns $2^n$ values to wires in a circuit comprising XOR and unary projection gates. A generalization of FreeXOR allows the XOR of wires with $2^n$ values to be very efficient. We then analyze the performance of our scheme by evaluating substitution-permutation ciphers. Using our proposal, we measure high-speed evaluation of the ciphers with a moderately increased cost in garbling and bandwidth. Theoretical analysis suggests that for evaluating the nine examined ciphers, one can expect a 4- to 70-fold improvement in evaluation performance with, at most, a 4-fold increase in garbling cost and, at most, an 8-fold increase in communication cost compared to state-of-the-art garbling schemes. In an offline/online setting, such as secure function evaluation as a service, the circuit garbling and communication to the evaluator can proceed before the input phase. Thus, our scheme offers a fast online phase. Furthermore, we present efficient Boolean circuits for the S-boxes of TWINE and Midori64 ciphers. To our knowledge, our formulas give the smallest number of AND gates for the S-boxes of these two ciphers.

  匹配依据：MPC: garbled circuits, garbling scheme, garbling schemes, secure function evaluation, secure two party computation

  </details>

- **Computation Efficient Structure-Aware PSI from Incremental Function Secret Sharing.**
  2024-05-29 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-031-68397-8_10) · [IACR ePrint](https://eprint.iacr.org/2024/842)
  Peihan Miao, Gayathri Garimella, Benjamin Goff

  <details><summary>摘要 / Abstract</summary>

  Structure-Aware Private Set Intersection (sa-PSI), recently introduced by Garimella et al. (Crypto&#x27;22), is a PSI variant where Alice&#x27;s input set $S_A$ has a publicly known structure (for example, interval, ball or union of balls) and Bob&#x27;s input $S_B$ is an unstructured set of elements. Prior work achieves sa-PSI where the communication cost only scales with the description size of $S_A$ instead of the set cardinality. However, the computation cost remains linear in the cardinality of $S_A$, which could be prohibitively large. In this work, we present a new semi-honest sa-PSI framework where both computation and communication costs only scale with the description size of $S_A$. Our main building block is a new primitive that we introduce called Incremental Boolean Function Secret Sharing (ibFSS), which is a generalization of FSS that additionally allows for evaluation on input prefixes. We formalize definitions and construct a weak ibFSS for a $d$-dimensional ball with $\ell_\infty$ norm, which may be of independent interest. Independently, we improve spatial hashing techniques (from prior work) when $S_A$ has structure union of $d$-dimensional balls in $(\{0,1\}^u)^d$, each of diameter $\delta$, from $O(u \cdot d \cdot (\log \delta)^d)$ to $O(\log \delta \cdot d)$ in terms of both computation and communication. Finally, we resolve the following open questions from prior work with communication and computation scaling with the description size of the structured set. - Our PSI framework can handle a union of overlapping structures, while prior work strictly requires a disjoint union. - We have a new construction that enables Bob with unstructured input $S_B$ to learn the intersection. - We extend to a richer class of functionalities like structure-aware PSI Cardinality and PSI-Sum of associated values.

  匹配依据：MPC: private set intersection, secret sharing

  </details>

- **Fully Secure MPC and zk-FLIOP over Rings: New Constructions, Improvements and Extensions.**
  2024-05-28 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-68397-8_5) · [IACR ePrint](https://eprint.iacr.org/2024/837)
  Ariel Nof, Anders P. K. Dalskov, Daniel Escudero, Anders Dalskov

  <details><summary>摘要 / Abstract</summary>

  We revisit the question of the overhead to achieve full security (i.e., guaranteed output delivery) in secure multiparty computation (MPC). Recent works have closed the gap between full security and semi-honest security, by introducing protocols where the parties first compute the circuit using a semi-honest protocol and then run a verification step with sublinear communication in the circuit size. However, in these works the number of interaction rounds in the verification step is also sublinear in the circuit&#x27;s size. Unlike communication, the round complexity of the semi-honest execution typically grows with the circuit&#x27;s depth and not its size. Hence, for large but shallow circuits, this additional number of rounds incurs a significant overhead. Motivated by this gap, we make the following contributions: 1. We present a new MPC framework to obtain full security, compatible with effectively any ring, that has an additive communication overhead of only $O(\log |C|)$, where $|C|$ is the number of multiplication gates in the circuit, and a constant number of additional rounds beyond the underlying semi-honest protocol. Our framework works with any linear secret sharing scheme and relies on a new to utilize the machinery of zero-knowledge fully linear interactive oracle proofs (zk-FLIOP) in a black-box way. We present several instantiations to the building blocks of our compiler, from which we derive concretely efficient protocols in different settings. 2. We present extensions to the zk-FLIOP primitive for very general settings. The first one is for proving statements over potentially non-commutative rings, where the only requirement is that the ring has a large enough set where (1) every element in the set commutes with every element in the ring, and (2) the difference between any two distinct elements is invertible. Our second zk-FLIOP extension is for proving statements over Galois Rings. For these rings, we present concrete improvements on the current state-of-the-art for the case of constant-round proofs, by making use of Reverse Multiplication Friendly Embeddings (RMFEs).

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Succinct Homomorphic Secret Sharing.**
  2024-05-24 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-58751-1_11) · [IACR ePrint](https://eprint.iacr.org/2024/814)
  Lawrence Roy, Peter Scholl, Damiano Abram

  <details><summary>摘要 / Abstract</summary>

  This work introduces homomorphic secret sharing (HSS) with succinct share size. In HSS, private inputs are shared between parties, who can then homomorphically evaluate a function on their shares, obtaining a share of the function output. In succinct HSS, a portion of the inputs can be distributed using shares whose size is sublinear in the number of such inputs. The parties can then locally evaluate a function $f$ on the shares, with the restriction that $f$ must be linear in the succinctly shared inputs. We construct succinct, two-party HSS for branching programs, based on either the decisional composite residuosity assumption, a DDH-like assumption in class groups, or learning with errors with a superpolynomial modulus-to-noise ratio. We then give several applications of succinct HSS, which were only previously known using fully homomorphic encryption, or stronger tools: - Succinct vector oblivious linear evaluation (VOLE): Two parties can obtain secret shares of a long, arbitrary vector $\vec x$, multiplied by a scalar $\Delta$, with communication sublinear in the size of the vector. - Batch, multi-party distributed point functions: A protocol for distributing a batch of secret, random point functions among $N$ parties, for any polynomial $N$, with communication sublinear in the number of DPFs. - Sublinear MPC for any number of parties: Two new constructions of MPC with sublinear communication complexity, with $N$ parties for any polynomial $N$: (1) For general layered Boolean circuits of size $s$, with communication $O(N s/\log\log s)$, and (2) For layered, sufficiently wide Boolean circuits, with communication $O(N s/\log s)$.

  匹配依据：MPC: secret sharing

  </details>

- **Secret Sharing with Certified Deletion.**
  2024-05-13 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2405.08117) · [CRYPTO](https://doi.org/10.1007/978-3-031-68394-7_7) · [IACR ePrint](https://eprint.iacr.org/2024/736)
  James Bartusek, Justin Raizes

  <details><summary>摘要 / Abstract</summary>

  Secret sharing allows a user to split a secret into many shares so that the secret can be recovered if, and only if, an authorized set of shares is collected. Although secret sharing typically does not require any computational hardness assumptions, its security does require that an adversary cannot collect an authorized set of shares. Over long periods of time where an adversary can benefit from multiple data breaches, this may become an unrealistic assumption. We initiate the systematic study of secret sharing with certified deletion in order to achieve security even against an adversary that eventually collects an authorized set of shares. In secret sharing with certified deletion, a (classical) secret is split into quantum shares which can be verifiably destroyed. We define two natural notions of security: no-signaling security and adaptive security. Next, we show how to construct (i) a secret sharing scheme with no-signaling certified deletion for any monotone access structure, and (ii) a threshold secret sharing scheme with adaptive certified deletion. Our first construction uses Bartusek and Khurana&#x27;s (CRYPTO 2023) 2-out-of-2 secret sharing scheme with certified deletion as a building block, while our second construction is built from scratch and requires several new technical ideas. For example, we significantly generalize the ``XOR extractor&#x27;&#x27; of Agarwal, Bartusek, Khurana, and Kumar (EUROCRYPT 2023) in order to obtain high rate seedless extraction from certain quantum sources of entropy.

  匹配依据：MPC: secret sharing

  </details>

- **Ditto: Quantization-aware Secure Inference of Transformers upon MPC.**
  2024-05-09 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2405.05525) · [series/jmlr](https://proceedings.mlr.press/v235/wu24d.html)
  Lei Wang, Junming Ma, Wenjing Fang, Jin Tan, Yancheng Zheng, Haoqi Wu, Yinggui Wang

  <details><summary>摘要 / Abstract</summary>

  Due to the rising privacy concerns on sensitive client data and trained models like Transformers, secure multi-party computation (MPC) techniques are employed to enable secure inference despite attendant overhead. Existing works attempt to reduce the overhead using more MPC-friendly non-linear function approximations. However, the integration of quantization widely used in plaintext inference into the MPC domain remains unclear. To bridge this gap, we propose the framework named Ditto to enable more efficient quantization-aware secure Transformer inference. Concretely, we first incorporate an MPC-friendly quantization into Transformer inference and employ a quantization-aware distillation procedure to maintain the model utility. Then, we propose novel MPC primitives to support the type conversions that are essential in quantization and implement the quantization-aware MPC execution of secure quantized inference. This approach significantly decreases both computation and communication overhead, leading to improvements in overall efficiency. We conduct extensive experiments on Bert and GPT2 models to evaluate the performance of Ditto. The results demonstrate that Ditto is about $3.14\sim 4.40\times$ faster than MPCFormer (ICLR 2023) and $1.44\sim 2.35\times$ faster than the state-of-the-art work PUMA with negligible utility degradation.

  匹配依据：MPC: secure multi party computation

  </details>

- **Actively Secure Private Set Intersection in the Client-Server Setting.**
  2024-04-15 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3658644.3690349) · [IACR ePrint](https://eprint.iacr.org/2024/570)
  Mariana Raykova, Phillipp Schoppmann, Xiao Wang, Yunqing Sun, Jonathan Katz

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) allows two parties to compute the intersection of their sets without revealing anything else. In some applications of PSI, a server holds a large set and runs a PSI protocol with multiple clients, each with its own smaller set. In this setting, existing protocols fall short: they either achieve only semi-honest security, or else require the server to run the protocol from scratch for each execution. We design an efficient protocol for this setting with simulation-based security against malicious adversaries. In our protocol, the server publishes a one-time, linear-size encoding of its set. Then, multiple clients can independently execute a PSI protocol with the server, with complexity linear in the size of each client’s set. To learn the intersection, a client can download the server’s encoding, which can be accelerated via content-distribution or peer-to-peer networks since the same encoding is used by all clients; alternatively, clients can fetch only the relevant parts of the encoding using verifiable private information retrieval. A key ingredient of our protocol is an efficient instantiation of an oblivious verifiable unpredictable function, which may be of independent interest. Our implementation shows that our protocol is highly efficient. For a server holding $10^8$ elements and each client holding $10^3$ elements, the size of the server’s encoding is 800MB; an execution of the protocol uses 60MB of communication, runs in under 5s in a WAN network with 120 Mbps bandwidth, and costs only 0.017 USD when utilizing network-caching infrastructures, a 5× saving compared to a state-of-the-art PSI protocol.

  匹配依据：MPC: private set intersection

  </details>

- **NodeGuard: A Highly Efficient Two-Party Computation Framework for Training Large-Scale Gradient Boosting Decision Tree.**
  2024-04-05 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SPW63631.2024.00015) · [IACR ePrint](https://eprint.iacr.org/2024/535)
  Yufan Jiang, Tianxiang Dai, Fei Mei, Yong Li

  <details><summary>摘要 / Abstract</summary>

  The Gradient Boosting Decision Tree (GBDT) is a well-known machine learning algorithm, which achieves high performance and outstanding interpretability in real-world scenes such as fraud detection, online marketing and risk management. Meanwhile, two data owners can jointly train a GBDT model without disclosing their private dataset by executing secure Multi-Party Computation (MPC) protocols. In this work, we propose NodeGuard, a highly efficient two party computation (2PC) framework for large-scale GBDT training and inference. NodeGuard guarantees that no sensitive intermediate results are leaked in the training and inference. The efficiency advantage of NodeGuard is achieved by applying a novel keyed bucket aggregation protocol, which optimizes the communication and computation complexity globally in the training. Additionally, we introduce a probabilistic approximate division protocol with an optimization for re-scaling, when the divisor is publicly known. Finally, we compare NodeGuard to state-of-the-art frameworks, and we show that NodeGuard is extremely efficient. It can improve the privacy preserving GBDT training performance by a factor of 5.0 to 131 in LAN and 2.7 to 457 in WAN.

  匹配依据：MPC: secure multi party computation, two party computation

  </details>

- **Efficient Actively Secure DPF and RAM-based 2PC with One-Bit Leakage.**
  2024-03-12 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00205) · [IACR ePrint](https://eprint.iacr.org/2024/426)
  Ruiyu Zhu, Xiao Wang, Yu Yu, Xiaojie Guo, Wenhao Zhang, Kang Yang

  <details><summary>摘要 / Abstract</summary>

  Secure two-party computation (2PC) in the RAM model has attracted huge attention in recent years. Most existing results only support semi-honest security, with the exception of Keller and Yanai (Eurocrypt 2018) with very high cost. In this paper, we propose an efficient RAM-based 2PC protocol with active security and one-bit leakage. 1) We propose an actively secure protocol for distributed point function (DPF), with one-bit leakage, that is essentially as efficient as the state-of-the-art semi-honest protocol. Compared with previous work, our protocol takes about $50 \times$ less communication for a domain with $2^{20}$ entries, and no longer requires actively secure generic 2PC. 2) We extend the dual-execution protocol to allow reactive computation, and then build a RAM-based 2PC protocol with active security on top of our new building blocks. The protocol follows the paradigm of Doerner and shelat (CCS 2017). We are able to prove that the protocol has end-to-end one-bit leakage. 3) Our implementation shows that our protocol is almost as efficient as the state-of-the-art semi-honest RAM-based 2PC protocol, and is at least two orders of magnitude faster than prior actively secure RAM-based 2PC without leakage, providing a realistic trade-off in practice.

  匹配依据：MPC: secure two party computation

  </details>

- **Traceable Secret Sharing: Strong Security and Efficient Constructions.**
  2024-03-05 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-031-68388-6_9) · [IACR ePrint](https://eprint.iacr.org/2024/405)
  Lior Rotem, Aditi Partap, Dan Boneh

  <details><summary>摘要 / Abstract</summary>

  Suppose Alice uses a $t$-out-of-$n$ secret sharing to store her secret key on $n$ servers. Her secret key is protected as long as $t$ of them do not collude. However, what if a less-than-$t$ subset of the servers decides to offer the shares they have for sale? In this case, Alice should be able to hold them accountable, or else nothing prevents them from selling her shares. With this motivation in mind, Goyal, Song, and Srinivasan (CRYPTO 21) introduced the concept of {\em traceable secret sharing}. In such schemes, it is possible to provably trace the leaked secret shares back to the servers who leaked them. Goyal et al.~presented the first construction of a traceable secret sharing scheme. However, secret shares in their construction are quadratic in the secret size, and their tracing algorithm is quite involved as it relies on Goldreich-Levin decoding. In this work, we put forth new definitions and practical constructions for traceable secret sharing. In our model, some $f &lt; t$ servers output a reconstruction box~$R$ that may arbitrarily depend on their shares. Given additional $t-f$ shares, $R$ reconstructs and outputs the secret. The task is to trace $R$ back to the corrupted servers given black-box access to $R$. Unlike Goyal et al., we do not assume that the tracing algorithm has any information on how the corrupted servers constructed~$R$ from the shares in their possession. We then present two very efficient constructions of traceable secret sharing based on two classic secret sharing schemes. In both of our schemes, shares are only twice as large as the secret, improving over the quadratic overhead of Goyal et al. Our first scheme is obtained by presenting a new practical tracing algorithm for the widely-used Shamir secret sharing scheme. Our second construction is based on an extension of Blakley&#x27;s secret sharing scheme. Tracing in this scheme is optimally efficient, and requires just one successful query to $R$. We believe that our constructions are an important step towards bringing traceable secret-sharing schemes to practice. This work also raises several interesting open problems that we describe in the paper.

  匹配依据：MPC: secret sharing

  </details>

- **On Information-Theoretic Secure Multiparty Computation with Local Repairability.**
  2024-03-03 · MPC · 含会议/期刊记录 · [PKC](https://doi.org/10.1007/978-3-031-57722-2_7) · [IACR ePrint](https://eprint.iacr.org/2024/391)
  Daniel Escudero, Ivan Tjuawinata, Chaoping Xing

  <details><summary>摘要 / Abstract</summary>

  In this work we consider the task of designing information-theoretic MPC protocols for which the state of a given party can be recovered from a small amount of parties, a property we refer to as local repairability. This is useful when considering MPC over dynamic settings where parties leave and join a computation, a scenario that has gained notable attention in recent literature. Thanks to the results of (Cramer et al. EUROCRYPT&#x27;00), designing such protocols boils down to constructing a linear secret-sharing scheme (LSSS) with good locality, that is, each share is determined by only a small amount of other shares, that also satisfies the so-called multiplicativity property. Previous constructions that achieve locality (e.g. using locally recoverable codes---LRCs) do not enjoy multiplicativity, and LSSS that are multiplicative (e.g. Shamir&#x27;s secret-sharing) do not satisfy locality. Our construction bridges this literature gap by showing the existence of an LSSS that achieves both properties simultaneously. Our results are obtained by making use of well known connection between error correcting codes and LSSS, in order to adapt the LRC construction by (Tamo &amp; Barg, IEEE Transactions on Information Theory 2014) to turn it into a LSSS. With enough care, such coding-theoretic construction yields our desired locality property, but it falls short at satisfying multiplicativity. In order to address this, we perform an extensive analysis of the privacy properties of our scheme in order to identify parameter regimes where our construction satisfies multiplicativity. Finally, since our LSSS satisfies locality, every share is determined by a small amount of shares. However, in an MPC context it is not enough to let the (small set of) parties to send their shares to the repaired party, since this may leak more information than the regenerated share. To obtain our final result regarding MPC with local repairability, we construct a lightweight MPC protocol that performs such repairing process without any leakage. We provide both a passively secure construction (for the plain multiplicative regime) and an actively secure one (for strong multiplicativity).

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Two-Round Maliciously-Secure Oblivious Transfer with Optimal Rate.**
  2024-02-29 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-58751-1_10) · [IACR ePrint](https://eprint.iacr.org/2024/372)
  Akshayaram Srinivasan, Pedro Branco, Nico Döttling

  <details><summary>摘要 / Abstract</summary>

  We give a construction of a two-round batch oblivious transfer (OT) protocol in the CRS model that is UC-secure against malicious adversaries and has (near) optimal communication cost. Specifically, to perform a batch of $k$ oblivious transfers where the sender&#x27;s inputs are bits, the sender and the receiver need to communicate a total of $3k + o(k) \cdot \mathsf{poly}(\lambda)$ bits. We argue that $3k$ bits are required by any protocol with a black-box and straight-line simulator. The security of our construction is proven assuming the hardness of Quadratic Residuosity (QR) and the Learning Parity with Noise (LPN).

  匹配依据：MPC: oblivious transfer

  </details>

- **Connecting Leakage-Resilient Secret Sharing to Practice: Scaling Trends and Physical Dependencies of Prime Field Masking.**
  2024-02-29 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-58737-5_12) · [IACR ePrint](https://eprint.iacr.org/2024/377)
  Elena Micheli, François-Xavier Standaert, Maximilian Orlt, Loïc Masure, Sebastian Faust

  <details><summary>摘要 / Abstract</summary>

  Symmetric ciphers operating in (small or mid-size) prime fields have been shown to be promising candidates to maintain security against low-noise (or even noise-free) side-channel leakage. In order to design prime ciphers that best trade physical security and implementation efficiency, it is essential to understand how side-channel security evolves with the field size (i.e., scaling trends). Unfortunately, it has also been shown that such a scaling trend depends on the leakage functions and cannot be explained by the standard metrics used to analyze Boolean masking with noise. In this work, we therefore initiate a formal study of prime field masking for two canonical leakage functions: bit leakages and Hamming weight leakages. By leveraging theoretical results from the leakage-resilient secret sharing literature, we explain formally why (1) bit leakages correspond to a worst-case and do not encourage operating in larger fields, and (2) an opposite conclusion holds for Hamming weight leakages, where increasing the prime field modulus p can contribute to a security amplification that is exponential in the number of shares,with log(p) seen as security parameter like the noise variance in Boolean masking. We combine these theoretical results with experimental ones and show that the interest masking in larger prime fields can degrade gracefully when leakage functions slightly deviate from the Hamming weight abstraction, motivating further research towards characterizing (ideally wide) classes of leakage functions offering such guarantees.

  匹配依据：MPC: secret sharing

  </details>

- **Garbled Circuit Lookup Tables with Logarithmic Number of Ciphertexts.**
  2024-02-28 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-58740-5_7) · [IACR ePrint](https://eprint.iacr.org/2024/369)
  David Heath, Lucien K. L. Ng, Vladimir Kolesnikov

  <details><summary>摘要 / Abstract</summary>

  Garbled Circuit (GC) is a basic technique for practical secure computation. GC handles Boolean circuits; it consumes significant network bandwidth to transmit encoded gate truth tables, each of which scales with the computational security parameter $\kappa$. GC optimizations that reduce bandwidth consumption are valuable. It is natural to consider a generalization of Boolean two-input one-output gates (represented by $4$-row one-column lookup tables, LUTs) to arbitrary $N$-row $m$-column LUTs. Known techniques for this do not scale, with naive size-$O(Nm\kappa)$ garbled LUT being the most practical approach in many scenarios. Our novel garbling scheme -- logrow -- implements GC LUTs while sending only a logarithmic in $N$ number of ciphertexts! Specifically, let $n = \lceil \log_2 N \rceil$. We allow the GC parties to evaluate a LUT for $(n-1)\kappa + nm\kappa + Nm$ bits of communication. logrow is compatible with modern GC advances, e.g. half gates and free XOR. Our work improves state-of-the-art GC handling of several interesting applications, such as privacy-preserving machine learning, floating-point arithmetic, and DFA evaluation.

  匹配依据：MPC: garbled circuit, garbling scheme, secure computation

  </details>

- **Fuzzy Private Set Intersection with Large Hyperballs.**
  2024-02-26 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-58740-5_12) · [IACR ePrint](https://eprint.iacr.org/2024/330)
  Sihang Pu, Aron van Baarsen

  <details><summary>摘要 / Abstract</summary>

  Traditional private set intersection (PSI) involves a receiver and a sender holding sets $X$ and $Y$, respectively, with the receiver learning only the intersection $X\cap Y$. We turn our attention to its fuzzy variant, where the receiver holds \(|X|\) hyperballs of radius \(\delta\) in a metric space and the sender has $|Y|$ points. Representing the hyperballs by their center, the receiver learns the points $x\in X$ for which there exists $y\in Y$ such that $\mathsf{dist}(x,y)\leq \delta$ with respect to some distance metric. Previous approaches either require general-purpose multi-party computation (MPC) techniques like garbled circuits or fully homomorphic encryption (FHE), leak details about the sender’s precise inputs, support limited distance metrics, or scale poorly with the hyperballs&#x27; volume. This work presents the first black-box construction for fuzzy PSI (including other variants such as PSI cardinality, labeled PSI, and circuit PSI), which can handle polynomially large radius and dimension (i.e., a potentially exponentially large volume) in two interaction messages, supporting general \(L_{p\in[1,\infty]}\) distance, without relying on garbled circuits or FHE. The protocol excels in both asymptotic and concrete efficiency compared to existing works. For security, we solely rely on the assumption that the Decisional Diffie-Hellman (DDH) holds in the random oracle model.

  匹配依据：MPC: garbled circuits, multi party computation, private set intersection

  </details>

- **Toward Malicious Constant-Rate 2PC via Arithmetic Garbling.**
  2024-02-20 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-58740-5_14) · [IACR ePrint](https://eprint.iacr.org/2024/283)
  Yibin Yang, Carmit Hazay

  <details><summary>摘要 / Abstract</summary>

  A recent work by Ball, Li, Lin, and Liu [Eurocrypt&#x27;23] presented a new instantiation of the arithmetic garbling paradigm introduced by Applebaum, Ishai, and Kushilevitz [FOCS&#x27;11]. In particular, Ball et al.&#x27;s garbling scheme is the first constant-rate garbled circuit over large enough bounded integer computations, inferring the first constant-round constant-rate secure two-party computation (2PC) over bounded integer computations in the presence of semi-honest adversaries. The main source of difficulty in lifting the security of garbling schemes-based protocols to the malicious setting lies in proving the correctness of the underlying garbling scheme. In this work, we analyze the security of Ball et al.&#x27;s scheme in the presence of malicious attacks. - We demonstrate an overflow attack, which is inevitable in this computational model, even if the garbled circuit is fully correct. Our attack follows by defining an adversary, corrupting either the garbler or the evaluator, that chooses a bad input and causes the computation to overflow, thus leaking information about the honest party&#x27;s input. By utilizing overflow attacks, we show that $1$-bit leakage is necessary for achieving security against a malicious garbler, discarding the possibility of achieving full malicious security in this model. We further demonstrate a wider range of overflow attacks against a malicious evaluator with more than $1$ bit of leakage. - We boost the security level of Ball et al.&#x27;s scheme by utilizing two variants of Vector Oblivious Linear Evaluation, denoted by VOLEc and aVOLE. We present the first constant-round constant-rate 2PC protocol over bounded integer computations, in the presence of a malicious garbler with $1$-bit leakage and a semi-honest evaluator, in the {VOLEc,aVOLE}-hybrid model and being black-box in the underlying group and ring. Compared to the semi-honest variant, our protocol incurs only a constant factor overhead, both in computation and communication. The constant-round and constant-rate properties hold even in the plain model.

  匹配依据：MPC: garbled circuit, garbling scheme, garbling schemes, secure two party computation

  </details>

- **Linear-Communication Asynchronous Complete Secret Sharing with Optimal Resilience.**
  2024-02-15 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-031-68397-8_13) · [IACR ePrint](https://eprint.iacr.org/2024/245)
  Junru Li, Yifan Song, Xiaoyu Ji

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) allows a set of $n$ parties to jointly compute a function on their private inputs. In this work, we focus on the information-theoretic MPC in the \emph{asynchronous network} setting with optimal resilience ($t&lt;n/3$). The best-known result in this setting is achieved by Choudhury and Patra [J. Cryptol &#x27;23], which requires $O(n^4\kappa)$ bits per multiplication gate, where $\kappa$ is the size of a field element. An asynchronous complete secret sharing (ACSS) protocol allows a dealer to share a batch of Shamir sharings such that all parties eventually receive their shares. ACSS is an important building block in AMPC. The best-known result of ACSS is due to Choudhury and Patra [J. Cryptol &#x27;23], which requires $O(n^3\kappa)$ bits per sharing. On the other hand, in the synchronous setting, it is known that distributing Shamir sharings can be achieved with $O(n\kappa)$ bits per sharing. There is a gap of $n^2$ in the communication between the synchronous setting and the asynchronous setting. Our work closes this gap by presenting the first ACSS protocol that achieves $O(n\kappa)$ bits per sharing. When combined with the compiler from ACSS to AMPC by Choudhury and Patra [IEEE Trans. Inf. Theory &#x27;17], we obtain an AMPC with $O(n^2\kappa)$ bits per multiplication gate, improving the previously best-known result by a factor of $n^2$. Moreover, with a concurrent work that improves the compiler by Choudhury and Patra by a factor of $n$, we obtain the first AMPC with $O(n\kappa)$ bits per multiplication gate.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Efficient Arithmetic in Garbled Circuits.**
  2024-01-31 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-031-58740-5_1) · [IACR ePrint](https://eprint.iacr.org/2024/139)
  David Heath

  <details><summary>摘要 / Abstract</summary>

  Garbled Circuit (GC) techniques usually work with Boolean circuits. Despite intense interest, efficient arithmetic generalizations of GC were only known from heavy assumptions, such as LWE. We construct arithmetic garbled circuits from circular correlation robust hashes, the assumption underlying the celebrated Free XOR garbling technique. Let $\lambda$ denote a computational security parameter, and consider the integers $\mathbb{Z}_m$ for any $m \geq 2$. Let $\ell = \lceil \log_2 m \rceil$ be the bit length of $\mathbb{Z}_m$ values. We garble arithmetic circuits over $\mathbb{Z}_m$ where the garbling of each gate has size $O(\ell \cdot \lambda)$ bits. Constrast this with Boolean-circuit-based arithmetic, requiring $O(\ell^2\cdot \lambda)$ bits via the schoolbook multiplication algorithm, or $O(\ell^{1.585}\cdot \lambda)$ bits via Karatsuba&#x27;s algorithm. Our arithmetic gates are compatible with Boolean operations and with Garbled RAM, allowing to garble complex programs of arithmetic values.

  匹配依据：MPC: garbled circuit, garbled circuits

  </details>

- **Updatable Private Set Intersection With Forward Privacy.**
  2024 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2024.3461475)
  Xiaolei Dong, Zhenfu Cao, Jun Zhou, Ruochen Wang, Kim-Kwang Raymond Choo

- **Towards Breaking the Half-Barrier of Local Leakage-Resilient Shamir's Secret Sharing.**
  2024 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-031-68388-6_10)
  Hai H. Nguyen

- **Toward A Practical Multi-party Private Set Union.**
  2024 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2024-0133) · [IACR ePrint](https://eprint.iacr.org/2023/1930)
  Ni Trieu, Jiahui Gao, Son Nguyen

  <details><summary>摘要 / Abstract</summary>

  This paper studies a multi-party private set union (mPSU), a fundamental cryptographic problem that allows multiple parties to compute the union of their respective datasets without revealing any additional information. We propose an efficient mPSU protocol which is secure in the presence of any number of colluding semi-honest participants. Our protocol avoids computationally expensive homomorphic operations or generic multi-party computation, thus providing an efficient solution for mPSU. The crux of our protocol lies in the utilization of new cryptographic tool, namely, Membership Oblivious Transfer (mOT) . We believe that the mOT and cOPRF may be of independent interest. We implement our mPSU protocol and evaluate their performance. Our protocol shows an improvement of up to $80.84\times$ in terms of running time and $405.73\times$ bandwidth cost compared to the existing state-of-the-art protocols. *Note: June 2024 - Fixed a bug in the original version and simplified the protocol by removing the OPRF.

  匹配依据：MPC: multi party computation, oblivious transfer, private set union

  </details>

- **The Capacity Region of Distributed Multi-User Secret Sharing Under Perfect Secrecy.**
  2024 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2024.3484666)
  Jiahong Wu, Wei Kang, Nan Liu

- **Sparsity and Privacy in Secret Sharing: A Fundamental Trade-Off.**
  2024 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2308.06413) · [TIFS](https://doi.org/10.1109/TIFS.2024.3394256)
  Maximilian Egger, Marvin Xhemrishi, Rawad Bitar, Antonia Wachter-Zeh

  <details><summary>摘要 / Abstract</summary>

  This work investigates the design of sparse secret sharing schemes that encode a sparse private matrix into sparse shares. This investigation is motivated by distributed computing, where the multiplication of sparse and private matrices is moved from a computationally weak main node to untrusted worker machines. Classical secret-sharing schemes produce dense shares. However, sparsity can help speed up the computation. We show that, for matrices with i.i.d. entries, sparsity in the shares comes at a fundamental cost of weaker privacy. We derive a fundamental tradeoff between sparsity and privacy and construct optimal sparse secret sharing schemes that produce shares that leak the minimum amount of information for a desired sparsity of the shares. We apply our schemes to distributed sparse and private matrix multiplication schemes with no colluding workers while tolerating stragglers. For the setting of two non-communicating clusters of workers, we design a sparse one-time pad so that no private information is leaked to a cluster of untrusted and colluding workers, and the shares with bounded but non-zero leakage are assigned to a cluster of partially trusted workers. We conclude by discussing the necessity of using permutations for matrices with correlated entries.

  匹配依据：MPC: secret sharing

  </details>

- **Secure and Efficient Federated Learning via Novel Authenticable Multi-Party Computation and Compressed Sensing.**
  2024 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2024.3486611)
  Di Xiao, Yushu Zhang, Xiangli Xiao, Lvjun Chen

- **Secure Sorting and Selection via Function Secret Sharing.**
  2024 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3658644.3690359)
  Yuval Ishai, Elette Boyle, Mahimna Kelkar, Yiping Ma, Amit Agarwal, Divya Gupta, Nishanth Chandran, Niv Gilboa

- **Secure Multiparty Computation with Identifiable Abort via Vindicating Release.**
  2024 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-031-68397-8_2)
  Yashvanth Kondi, Ran Cohen, Jack Doerner, Abhi Shelat

- **Secure Multiparty Computation of Threshold Signatures Made More Efficient.**
  2024 · MPC · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/secure-multiparty-computation-of-threshold-signatures-made-more-efficient/)
  Harry W. H. Wong, Jack P. K. Ma, Sherman S. M. Chow

- **Secret Cracking and Security Enhancement for the Image Application of CRT-Based Secret Sharing.**
  2024 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2024.3477265)
  Rui Wang, Xuehu Yan, Guozheng Yang, Wei Yan, Longlong Li

- **Scalable Multi-Party Computation Protocols for Machine Learning in the Honest-Majority Setting.**
  2024 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity24/presentation/liu-fengrun)
  Xiang Xie, Yu Yu, Fengrun Liu

- **SIGMA: Secure GPT Inference with Function Secret Sharing.**
  2024 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2024-0107) · [IACR ePrint](https://eprint.iacr.org/2023/1269)
  Ashish Panwar, Rahul Sharma, Ananta Mukherjee, Neha Jawalkar, Kanav Gupta, Divya Gupta, Nishanth Chandran

  <details><summary>摘要 / Abstract</summary>

  Secure 2-party computation (2PC) enables secure inference that offers protection for both proprietary machine learning (ML) models and sensitive inputs to them. However, the existing secure inference solutions suffer from high latency and communication overheads, particularly for transformers. Function secret sharing (FSS) is a recent paradigm for obtaining efficient 2PC protocols with a preprocessing phase. We provide SIGMA, the first end-to-end system for secure transformer inference based on FSS. By constructing new FSS-based protocols for complex machine learning functionalities, such as Softmax, GeLU and SiLU, and also accelerating their computation on GPUs, SIGMA improves the latency of secure inference of transformers by $11-19\times$ over the state-of-the-art that uses preprocessing and GPUs. We present the first secure inference of generative pre-trained transformer (GPT) models. In particular, SIGMA executes Meta&#x27;s LLaMA2 (available on HuggingFace) with 13 billion parameters in 44 seconds and GPT2 in 1.6 seconds.

  匹配依据：MPC: secret sharing, secure 2 party computation

  </details>

- **Randomness Recoverable Secret Sharing Schemes.**
  2024 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-024-09515-4) · [IACR ePrint](https://eprint.iacr.org/2023/959)
  Behzad Vahdani, Shahram Khazaei, Mohammad Hajiabadi

  <details><summary>摘要 / Abstract</summary>

  It is well-known that randomness is essential for secure cryptography. The randomness used in cryptographic primitives is not necessarily recoverable even by the party who can, e.g., decrypt or recover the underlying secret/message. Several cryptographic primitives that support randomness recovery have turned out useful in various applications. In this paper, we study randomness recoverable secret sharing schemes (RR-SSS), in both information-theoretic and computational settings and provide two results. First, we show that while every access structure admits a perfect RR-SSS, there are very simple access structures (e.g., in monotone $\mathsf{AC}^0$) that do not admit efficient perfect (or even statistical) RR-SSS. Second, we show that the existence of efficient computational RR-SSS for certain access structures in monotone $\mathsf{AC}^0$ implies the existence of one-way functions. This stands in sharp contrast to (non-RR) SSS schemes for which no such results are known. RR-SSS plays a key role in making advanced attributed-based encryption schemes randomness recoverable, which in turn have applications in the context of designated-verifier non-interactive zero knowledge.

  匹配依据：MPC: secret sharing

  </details>

- **P²FRPSI: Privacy-Preserving Feature Retrieved Private Set Intersection.**
  2024 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2023.3343973)
  Chaochao Cai, Weidong Qiu, Haiyang Xue, Guowei Ling, Jinyong Shan, Wulu Li, Peng Tang, Xinyi Huang, Fei Tang

- **Publicly Verifiable Secret Sharing Over Class Groups and Applications to DKG and YOSO.**
  2024 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-58740-5_8) · [IACR ePrint](https://eprint.iacr.org/2023/1651)
  Bernardo Machado David, Ignacio Cascudo, Bernardo David

  <details><summary>摘要 / Abstract</summary>

  Publicly Verifiable Secret Sharing (PVSS) allows a dealer to publish encrypted shares of a secret so that parties holding the corresponding decryption keys may later reconstruct it. Both dealing and reconstruction are non-interactive and any verifier can check their validity. PVSS finds applications in randomness beacons, distributed key generation (DKG) and in YOSO MPC (Gentry et al. CRYPTO&#x27;21), when endowed with suitable publicly verifiable re-sharing as in YOLO YOSO (Cascudo et al. ASIACRYPT&#x27;22). We introduce a PVSS scheme over class groups that achieves similar efficiency to state-of-the art schemes that only allow for reconstructing a function of the secret, while our scheme allows the reconstruction of the original secret. Our construction generalizes the DDH-based scheme of YOLO YOSO to operate over class groups, which poses technical challenges in adapting the necessary NIZKs in face of the unknown group order and the fact that efficient NIZKs of knowledge are not as simple to construct in this setting. Building on our PVSS scheme&#x27;s ability to recover the original secret, we propose two DKG protocols for discrete logarithm key pairs: a biasable 1-round protocol, which improves on the concrete communication/computational complexities of previous works; and a 2-round unbiasable protocol, which improves on the round complexity of previous works. We also add publicly verifiable resharing towards anonymous committees to our PVSS, so that it can be used to efficiently transfer state among committees in the YOSO setting. Together with a recent construction of MPC in the YOSO model based on class groups (Braun et al. CRYPTO&#x27;23), this results in the most efficient full realization (i.e without assuming receiver anonymous channels) of YOSO MPC based on the CDN framework with transparent setup.

  匹配依据：MPC: secret sharing

  </details>

- **Poster: Multiparty Private Set Intersection from Multiparty Homomorphic Encryption.**
  2024 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3658644.3691405)
  Wouter Lueks, Christian Mouchet, Lea Nürnberger, Sylvain Chatel

- **Poster: A Secure Multiparty Computation Platform for Squeaky-Clean Data Rooms.**
  2024 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3658644.3691371)
  Sikhar Patranabis, Vinayaka Pandit, Abhishek Singh, Nitin Singh, Pankaj Dayama

- **PEPSI: Practically Efficient Private Set Intersection in the Unbalanced Setting.**
  2024 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2310.14565) · [USENIX Security](https://www.usenix.org/conference/usenixsecurity24/presentation/mahdavi)
  Ehsan Amjadian, Simon Oya, Florian Kerschbaum, Thomas Humphries, Faezeh Ebrahimianghazani, Bailey Kacsmar, Xinda Li, Nils Lukas, John A. Premkumar, Rasoul Akhavan Mahdavi, John Premkumar

  <details><summary>摘要 / Abstract</summary>

  Two parties with private data sets can find shared elements using a Private Set Intersection (PSI) protocol without revealing any information beyond the intersection. Circuit PSI protocols privately compute an arbitrary function of the intersection - such as its cardinality, and are often employed in an unbalanced setting where one party has more data than the other. Existing protocols are either computationally inefficient or require extensive server-client communication on the order of the larger set. We introduce Practically Efficient PSI or PEPSI, a non-interactive solution where only the client sends its encrypted data. PEPSI can process an intersection of 1024 client items with a million server items in under a second, using less than 5 MB of communication. Our work is over 4 orders of magnitude faster than an existing non-interactive circuit PSI protocol and requires only 10% of the communication. It is also up to 20 times faster than the work of Ion et al., which computes a limited set of functions and has communication costs proportional to the larger set. Our work is the first to demonstrate that non-interactive circuit PSI can be practically applied in an unbalanced setting.

  匹配依据：MPC: private set intersection

  </details>

- **On Sigma-Protocols and (Packed) Black-Box Secret Sharing Schemes.**
  2024 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-57722-2_14) · [IACR ePrint](https://eprint.iacr.org/2023/1652)
  Ignacio Cascudo, Claudia Bartoli

  <details><summary>摘要 / Abstract</summary>

  $\Sigma$-protocols are a widely utilized, relatively simple and well understood type of zero-knowledge proofs. However, the well known Schnorr $\Sigma$-protocol for proving knowledge of discrete logarithm in a cyclic group of known prime order, and similar protocols working over this type of groups, are hard to generalize to dealing with other groups. In particular with hidden order groups, due to the inability of the knowledge extractor to invert elements modulo the order. In this paper, we introduce a universal construction of $\Sigma$-protocols designed to prove knowledge of preimages of group homomorphisms for any abelian finite group. In order to do this, we first establish a general construction of a $\Sigma$-protocol for $\mathfrak{R}$-module homomorphism given only a linear secret sharing scheme over the ring $\mathfrak{R}$, where zero knowledge and special soundness can be related to the privacy and reconstruction properties of the secret sharing scheme. Then, we introduce a new construction of 2-out-of-$n$ packed black-box secret sharing scheme capable of sharing $k$ elements of an arbitrary (abelian, finite) group where each share consists of $k+\log n-3$ group elements. From these two elements we obtain a generic ``batch&#x27;&#x27; $\Sigma$-protocol for proving knowledge of $k$ preimages of elements via the same group homomorphism, which communicates $k+\lambda-3$ elements of the group to achieve $2^{-\lambda}$ knowledge error. For the case of class groups, we show that our $\Sigma$-protocol improves in several aspects on existing proofs for knowledge of discrete logarithm and other related statements that have been used in a number of works. Finally, we extend our constructions from group homomorphisms to the case of ZK-ready functions, introduced by Cramer and Damg\aa rd in Crypto 09, which in particular include the case of proofs of knowledge of plaintext (and randomness) for some linearly homomorphic encryption schemes such as Joye-Libert encryption. However, in the case of Joye-Libert, we show an even better alternative, using Shamir secret sharing over Galois rings, which achieves $2^{-k}$ knowledge soundness by communicating $k$ ciphertexts to prove $k$ statements.

  匹配依据：MPC: secret sharing

  </details>

- **O-Ring and K-Star: Efficient Multi-party Private Set Intersection.**
  2024 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity24/presentation/wu-mingli)
  Tsz Hon Yuen, Kwan Yin Chan, Mingli Wu

- **Network-Agnostic Multi-party Computation Revisited (Extended Abstract).**
  2024 · MPC · 含会议/期刊记录 · [PKC](https://doi.org/10.1007/978-3-031-57722-2_6)
  Supreeth Varadarajan, Nidhish Bhimrajka, Ashish Choudhury

- **Multiparty Private Set Intersection Cardinality and Its Applications.**
  2024 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2024-0041) · [IACR ePrint](https://eprint.iacr.org/2022/735)
  Ni Trieu, Avishay Yanai, Jiahui Gao

  <details><summary>摘要 / Abstract</summary>

  We describe a new paradigm for multi-party private set intersection cardinality (\psica) that allows $n$ parties to compute the intersection size of their datasets without revealing any additional information. We explore a variety of instantiations of this paradigm. Our protocols avoid computationally expensive public-key operations and are secure in the presence of a semi-honest adversary. We demonstrate the practicality of our \psica\ with an implementation. For $n=16$ parties with data-sets of $2^{20}$ items each, our server-aided variant takes 71 seconds. Interestingly, in the server-less setting, the same task takes only 7 seconds. To the best of our knowledge, this is the first `special purpose&#x27; implementation of a multi-party \psica\ from symmetric-key techniques (i.e., an implementation that does not rely on a generic underlying MPC). We study two interesting applications -- heatmap computation and associated rule learning (ARL) -- that can be computed securely using a dot-product as a building block. We analyse the performance of securely computing heatmap and ARL using our protocol and compare that to the state-of-the-art.

  匹配依据：MPC: private set intersection

  </details>

- **Maliciously Secure MPC From Semi-Honest 2PC in the Server-Aided Model.**
  2024 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2023.3322397)
  Yibiao Lu, Kui Ren, Bingsheng Zhang

- **MPC-Pipe: an Efficient Pipeline Scheme for Semi-honest MPC Machine Learning.**
  2024 · MPC · 含会议/期刊记录 · [ASPLOS](https://doi.org/10.1145/3622781.3674175)
  Murali Annavaram, Rachit Rajat, Yongqin Wang

- **Lightweight Asynchronous Verifiable Secret Sharing with Optimal Resilience.**
  2024 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-024-09505-6) · [IACR ePrint](https://eprint.iacr.org/2023/536)
  Victor Shoup, Nigel P. Smart

  <details><summary>摘要 / Abstract</summary>

  We present new protocols for *Asynchronous Verifiable Secret Sharing* for Shamir (i.e., threshold $t&lt;n$) sharing of secrets. Our protocols: * Use only &quot;lightweight&quot; cryptographic primitives, such as hash functions; * Can share secrets over rings such as $\mathbb{Z}_{p^k}$ as well as finite fields $\mathbb{F}_q$; * Provide *optimal resilience*, in the sense that they tolerate up to $t &lt; n/3$ corruptions, where $n$ is the total number of parties; * Are *complete*, in the sense that they guarantee that if any honest party receives their share then all honest parties receive their shares; * Employ *batching* techniques, whereby a dealer shares many secrets in parallel, and achieves an amortized communication complexity that is linear in $n$, at least on the &quot;happy path&quot;, where no party *provably* misbehaves.

  匹配依据：MPC: secret sharing

  </details>

- **Fast RS-IOP Multivariate Polynomial Commitments and Verifiable Secret Sharing.**
  2024 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity24/presentation/zhang-zongyang)
  Kexin Shi, Ximeng Liu, Weihan Li, Jin Dong, Yanpei Guo, Zongyang Zhang, Sherman S. M. Chow

- **FSS-DBSCAN: Outsourced Private Density-Based Clustering via Function Secret Sharing.**
  2024 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2024.3446233)
  Yulong Shen, Zhao Chang, Jiaxuan Fu, Yuheng Xia, Anxiao Song, Ke Cheng

- **Enabling Threshold Functionality for Private Set Intersection Protocols in Cloud Computing.**
  2024 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2024.3402355)
  Yongjun Zhao, Khin Mi Mi Aung, Benjamin Hong Meng Tan, Huaxiong Wang, Jingwei Hu

- **Efficiently Compiling Secure Computation Protocols From Passive to Active Security: Beyond Arithmetic Circuits.**
  2024 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2024-0006)
  Dennis Murphy, Marina Blanton, Chen Yuan

- **Efficient Scalable Multi-Party Private Set Intersection(-Variants) from Bicentric Zero-Sharing.**
  2024 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3658644.3690245)
  Ying Gao, Mengmeng Zhou, Wei Wang, Longxin Wang, Xiang Liu, Yuanchao Luo, Lin Qi

- **Efficient Coded Multi-Party Computation at Edge Networks.**
  2024 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2305.07142) · [TIFS](https://doi.org/10.1109/TIFS.2023.3326970)
  Hulya Seferoglu, Elahe Vedadi, Yasaman Keshtkarjahromi

  <details><summary>摘要 / Abstract</summary>

  Multi-party computation (MPC) is promising for designing privacy-preserving machine learning algorithms at edge networks. An emerging approach is coded-MPC (CMPC), which advocates the use of coded computation to improve the performance of MPC in terms of the required number of workers involved in computations. The current approach for designing CMPC algorithms is to merely combine efficient coded computation constructions with MPC. We show that this approach fails short of being efficient; e.g., entangled polynomial codes are not necessarily better than PolyDot codes in MPC setting, while they are always better for coded computation. Motivated by this observation, we propose a new construction; Adaptive Gap Entangled (AGE) polynomial codes for MPC. We show through analysis and simulations that MPC with AGE codes always perform better than existing CMPC algorithms in terms of the required number of workers as well as computation, storage, and communication overhead.

  匹配依据：MPC: multi party computation

  </details>

- **Dual-Cloud Multi-Secret Sharing Architecture for Privacy Preserving Persistent Computation.**
  2024 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2024.3436662)
  Jhe-Kai Yang, Hsin-Chan Yen, Pei-Wen Lin, Yu-Chi Chen

- **Don't Eject the Impostor: Fast Three-Party Computation With a Known Cheater.**
  2024 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00164)
  Ajith Suresh, Thomas Schneider, Oliver Schick, Hossein Yalame, Andreas Brüggemann

- **Constructing Leakage-Resilient Shamir's Secret Sharing: Over Composite Order Fields.**
  2024 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-58737-5_11)
  Hai H. Nguyen, Xiuyu Ye, Anat Paskin-Cherniavsky, Hemanta K. Maji

- **Compact: Approximating Complex Activation Functions for Secure Computation.**
  2024 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2309.04664) · [PoPETs](https://doi.org/10.56553/POPETS-2024-0065)
  Rahul Chatterjee, Peter Rindal, Sunpreet S. Arora, Maliheh Shirvanian, Mazharul Islam

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) techniques can be used to provide data privacy when users query deep neural network (DNN) models hosted on a public cloud. State-of-the-art MPC techniques can be directly leveraged for DNN models that use simple activation functions such as ReLU. However, these techniques are ineffective and/or inefficient for the complex and highly non-linear activation functions used in cutting-edge DNN models. We present Compact, which produces piece-wise polynomial approximations of complex AFs to enable their efficient use with state-of-the-art MPC techniques. Compact neither requires nor imposes any restriction on model training and results in near-identical model accuracy. To achieve this, we design Compact with input density awareness and use an application-specific simulated annealing type optimization to generate computationally more efficient approximations of complex AFs. We extensively evaluate Compact on four different machine-learning tasks with DNN architectures that use popular complex AFs silu, gelu, and mish. Our experimental results show that Compact incurs negligible accuracy loss while being 2x-5x computationally more efficient than state-of-the-art approaches for DNN models with large number of hidden layers. Our work accelerates easy adoption of MPC techniques to provide user data privacy even when the queried DNN models consist of a number of hidden layers and trained over complex AFs.

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **Communication-Efficient Privacy-Preserving Neural Network Inference via Arithmetic Secret Sharing.**
  2024 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2024.3420216)
  Jianting Ning, Yan Zhang, Changqing Luo, Jinbo Xiong, Ximeng Liu, Youliang Tian, Renwan Bi

- **Collusion-Resilient and Maliciously Secure Cloud- Assisted Two-Party Computation Scheme in Mobile Cloud Computing.**
  2024 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2024.3428410)
  Zhenfu Cao, Zhe Liu, Nan Min, Zhusen Liu, Weizheng Wang, Lu Zhou, Yutong Ye

- **Bounds and Protocols for Graph-Based Distributed Secret Sharing.**
  2024 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2023.3261239)
  Alfredo De Santis, Roberto De Prisco, Francesco Palmieri

- **Application of Randomness for Security and Privacy in Multi-Party Computation.**
  2024 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2024.3381959)
  William J. Buchanan, Rahul Saha, Gulshan Kumar, G. Geetha, Mauro Conti

- **Abuse Reporting for Metadata-Hiding Communication Based on Secret Sharing.**
  2024 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity24/presentation/eskandarian) · [IACR ePrint](https://eprint.iacr.org/2023/1144)
  Saba Eskandarian

  <details><summary>摘要 / Abstract</summary>

  As interest in metadata-hiding communication grows in both research and practice, a need exists for stronger abuse reporting features on metadata-hiding platforms. While message franking has been deployed on major end-to-end encrypted platforms as a lightweight and effective abuse reporting feature, there is no comparable technique for metadata-hiding platforms. Existing efforts to support abuse reporting in this setting, such as asymmetric message franking or the Hecate scheme, require order of magnitude increases in client and server computation or fundamental changes to the architecture of messaging systems. As a result, while metadata-hiding communication inches closer to practice, critical content moderation concerns remain unaddressed. This paper demonstrates that, for broad classes of metadata-hiding schemes, lightweight abuse reporting can be deployed with minimal changes to the overall architecture of the system. Our insight is that much of the structure needed to support abuse reporting already exists in these schemes. By taking a non-generic approach, we can reuse this structure to achieve abuse reporting with minimal overhead. In particular, we show how to modify schemes based on secret sharing user inputs to support a message franking-style protocol. Compared to prior work, our shared franking technique more than halves the time to prepare a franked message and gives order of magnitude reductions in server-side message processing times, as well as in the time to decrypt a message and verify a report.

  匹配依据：MPC: secret sharing

  </details>

- **A Secure Computing System With Hardware-Efficient Lazy Bonsai Merkle Tree for FPGA-Attached Embedded Memory.**
  2024 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2023.3324935)
  Yu Zou, Rakin Muhammad Shadab, Sanjay Gandham, Mingjie Lin, Amro Awad

- **A New Shift-Add Secret Sharing Scheme for Partial Data Protection With Parallel Zigzag Decoding.**
  2024 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2024.3488498)
  Chi Wan Sung, Yichen Shen, Jiajun Chen
