# 2023 · MPC · 含会议/期刊记录 · 第 1/1 页

[总目录](../PAPERS.md)

- **Sublinear-Communication Secure Multiparty Computation does not require FHE**
  2023-11-22 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-30617-4_6) · [IACR ePrint](https://eprint.iacr.org/2023/1802)
  Elette Boyle, Geoffroy Couteau, Pierre Meyer

  <details><summary>摘要 / Abstract</summary>

  Secure computation enables mutually distrusting parties to jointly compute a function on their secret inputs, while revealing nothing beyond the function output. A long-running challenge is understanding the required communication complexity of such protocols---in particular, when communication can be sublinear in the circuit representation size of the desired function. Significant advances have been made affirmatively answering this question within the two-party setting, based on a variety of structures and hardness assumptions. In contrast, in the multi-party setting, only one general approach is known: using Fully Homomorphic Encryption (FHE). This remains the state of affairs even for just three parties, with two corruptions. We present a framework for achieving secure sublinear-communication $(N+1)$-party computation, building from a particular form of Function Secret Sharing for only $N$ parties. In turn, we demonstrate implications to sublinear secure computation for various function classes in the 3-party and 5-party settings based on an assortment of assumptions not known to imply FHE.

  匹配依据：MPC: secret sharing, secure computation, secure multiparty computation

  </details>

- **Three Party Secure Computation with Friends and Foes**
  2023-10-17 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-48618-0_6) · [IACR ePrint](https://eprint.iacr.org/2023/1605)
  Bar Alon, Amos Beimel, Eran Omri

  <details><summary>摘要 / Abstract</summary>

  In secure multiparty computation (MPC), the goal is to allow a set of mutually distrustful parties to compute some function of their private inputs in a way that preserves security properties, even in the face of adversarial behavior by some of the parties. However, classical security definitions do not pose any privacy restrictions on the view of honest parties. Thus, if an attacker adversarially leaks private information to honest parties, it does not count as a violation of privacy. This is arguably undesirable, and in real-life scenarios, it is hard to imagine that possible users would agree to have their private information revealed, even if only to other honest parties. To address this issue, Alon et al. [CRYPTO 20] introduced the notion of security with friends and foes (FaF security). In essence, $(t,h)$-FaF security requires that a malicious adversary corrupting up to $t$ parties cannot help a coalition of $h$ semi-honest parties to learn anything beyond what they can learn from their inputs and outputs (combined with the input and outputs of the malicious parties). They further showed that $(t,h)$-FaF security with $n$ parties is achievable for any functionality if $2t+h&lt;n$, and for some functionality, $(t,h)$-FaF security is impossible assuming $2t+h\geq n$. A remaining important open problem is to characterize the set of $n$-party functionalities that can be computed with $(t,h)$-FaF security assuming $2t+h\geq n$. In this paper, we focus on the special, yet already challenging, case of $(1,1)$-FaF security for three-party, 2-ary (two inputs), symmetric (all parties output the same value) functionalities. We provide several positive results, a lower bound on the round complexity, and an impossibility result. In particular, we prove the following. (1) we identify a large class of three-party Boolean symmetric 2-ary functionalities that can be computed with $(1,1)$-FaF full security, and (2) We identify a large class of three-party (possibly non-Boolean) symmetric 2-ary functionalities, for which no $O(\log\kappa)$-round protocol computes them with $(1,1)$-FaF full security. This matches the round complexity of our positive results for various interesting functionalities, such as equality of strings.

  匹配依据：MPC: secure computation, secure multiparty computation

  </details>

- **Multi-Party Homomorphic Secret Sharing and Sublinear MPC from Sparse LPN**
  2023-10-14 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-38545-2_11) · [IACR ePrint](https://eprint.iacr.org/2023/1593)
  Yuval Ishai, Aayush Jain, Quang Dao, Huijia Lin

  <details><summary>摘要 / Abstract</summary>

  Over the past few years, homomorphic secret sharing (HSS) emerged as a compelling alternative to fully homomorphic encryption (FHE), due to its feasibility from an array of standard assumptions and its potential efficiency benefits. However, all known HSS schemes, with the exception of schemes built from FHE or indistinguishability obfuscation (iO), can only support two or four parties. In this work, we give the first construction of a multi-party HSS scheme for a non-trivial function class, from an assumption not known to imply FHE. In particular, we construct an HSS scheme for an arbitrary number of parties with an arbitrary corruption threshold, supporting evaluations of multivariate polynomials of degree $\log / \log \log$ over arbitrary finite fields. As a consequence, we obtain a secure multiparty computation (MPC) protocol for any number of parties, with (slightly) sub-linear per-party communication of roughly $O(S / \log \log S)$ bits when evaluating a layered Boolean circuit of size $S$. Our HSS scheme relies on the Sparse Learning Parity with Noise assumption, a standard variant of LPN with a sparse public matrix that has been studied and used in prior works. Thanks to this assumption, our construction enjoys several unique benefits. In particular, it can be built on top of any linear secret sharing scheme, producing noisy output shares that can be error-corrected by the decoder. This yields HSS for low-degree polynomials with optimal download rate. Unlike prior works, our scheme also has a low computation overhead in that the per-party computation of a constant degree polynomial takes $O(M)$ work, where $M$ is the number of monomials.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **List Oblivious Transfer and Applications to Round-Optimal Black-Box Multiparty Coin Tossing**
  2023-10-03 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-38557-5_15) · [IACR ePrint](https://eprint.iacr.org/2023/1512)
  Michele Ciampi, Luisa Siniscalchi, Hendrik Waldner, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  In this work we study the problem of minimizing the round complexity for securely evaluating multiparty functionalities while making black-box use of polynomial time assumptions. In Eurocrypt 2016, Garg et al. showed that, assuming all parties have access to a broadcast channel, then at least four rounds of communication are required to securely realize non-trivial functionalities in the plain model. A sequence of works follow-up the result of Garg et al. matching this lower bound under a variety of assumptions. Unfortunately, none of these works make black-box use of the underlying cryptographic primitives. In Crypto 2021, Ishai, Khurana, Sahai, and Srinivasan came closer to matching the four-round lower bound, obtaining a five-round protocol that makes black-box use of oblivious transfer and PKE with pseudorandom public keys. In this work, we show how to realize any input-less functionality (e.g., coin-tossing, generation of key-pairs, and so on) in four rounds while making black-box use of two-round oblivious transfer. As an additional result, we construct the first four-round MPC protocol for generic functionalities that makes black-box use of the underlying primitives, achieving security against non-aborting adversaries. Our protocols are based on a new primitive called list two-party computation. This primitive offers relaxed security compared to the standard notion of secure two-party computation. Despite this relaxation, we argue that this tool suffices for our applications. List two-party computation is of independent interest, as we argue it can also be used for the generation of setups, like oblivious transfer correlated randomness, in three rounds. Prior to our work, generating such a setup required at least four rounds of interactions or a trusted third party.

  匹配依据：MPC: oblivious transfer, secure two party computation, two party computation

  </details>

- **Scalable Multi-party Private Set Union from Multi-Query Secret-Shared Private Membership Test**
  2023-09-19 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-981-99-8721-4_8) · [IACR ePrint](https://eprint.iacr.org/2023/1413)
  Ying Gao, Xiang Liu

  <details><summary>摘要 / Abstract</summary>

  Multi-party private set union (MPSU) allows \(k(k\geq 3)\) parties, each holding a dataset of known size, to compute the union of their sets without revealing any additional information. Although two-party PSU has made rapid progress in recent years, applying its effective techniques to the multi-party setting would render information leakage and thus cannot be directly extended. Existing MPSU protocols heavily rely on computationally expensive public-key operations or generic secure multi-party computation techniques, which are not scalable. In this work, we present a new efficient framework of MPSU from multi-party secret-shared shuffle and a newly introduced protocol called multi-query secret-shared private membership test (mq-ssPMT). Our MPSU is mainly based on symmetric-key operations and is secure against any semi-honest adversary that does not corrupt the leader and clients simultaneously. We also propose new frameworks for computing other multi-party private set operations (MPSO), such as the intersection, and the cardinality of the union and the intersection, meeting the same security requirements. We demonstrate the scalability of our MPSU protocol with an implementation and a comparison with the state-of-the-art MPSU. Experiments show that when computing on datasets of \(2^{10}\) elements, our protocol is \(109\times\) faster than the state-of-the-art MPSU, and the improvement becomes more significant as the set size increases. To the best of our knowledge, ours is the first protocol that reports on large-size experiments. For 7 parties with datasets of \(2^{20}\) elements each, our protocol requires only 46 seconds.

  匹配依据：MPC: private set union, secure multi party computation

  </details>

- **Sigma Protocols from Verifiable Secret Sharing and Their Applications**
  2023-09-17 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-981-99-8724-5_7) · [IACR ePrint](https://eprint.iacr.org/2023/1388)
  Zhichao Wang, Chuanzhou Yao, Yu Chen, Min Zhang

  <details><summary>摘要 / Abstract</summary>

  Sigma protocols are one of the most common and efficient zero-knowledge proofs (ZKPs). Over the decades, a large number of Sigma protocols are proposed, yet few works pay attention to the common design principal. In this work, we propose a generic framework of Sigma protocols for algebraic statements from verifiable secret sharing (VSS) schemes. Our framework provides a general and unified approach to understanding Sigma protocols. It not only neatly explains the classic protocols such as Schnorr, Guillou–Quisquater and Okamoto protocols, but also leads to new Sigma protocols that were not previously known. Furthermore, we show an application of our framework in designing ZKPs for composite statements, which contain both algebraic and non-algebraic statements. We give a generic construction of non-interactive ZKPs for composite statements by combining Sigma protocols from VSS and ZKPs following MPC-in-the-head paradigm in a seamless way via a technique of \textit{witness sharing reusing}. Our construction has advantages of requiring no “glue” proofs for combining algebraic and non-algebraic statements. By instantiating our construction using Ligero++ (Bhadauria et al., CCS 2020) and designing an associated Sigma protocol from VSS, we obtain a concrete ZKP for composite statements which achieves a tradeoff between running time and proof size, thus resolving the open problem left by Backes et al. (PKC 2019).

  匹配依据：MPC: secret sharing

  </details>

- **Let's Go Eevee! A Friendly and Suitable Family of AEAD Modes for IoT-to-Cloud Secure Computation**
  2023-09-11 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3576915.3623091) · [IACR ePrint](https://eprint.iacr.org/2023/1361)
  Aysajan Abidin, Erik Pohle, Amit Singh Bhati, Elena Andreeva, Bart Preneel

  <details><summary>摘要 / Abstract</summary>

  IoT devices collect privacy-sensitive data, e.g., in smart grids or in medical devices, and send this data to cloud servers for further processing. In order to ensure confidentiality as well as authenticity of the sensor data in the untrusted cloud environment, we consider a transciphering scenario between embedded IoT devices and multiple cloud servers that perform secure multi-party computation (MPC). Concretely, the IoT devices encrypt their data with a lightweight symmetric cipher and send the ciphertext to the cloud servers. To obtain the secret shares of the cleartext message for further processing, the cloud servers engage in an MPC protocol to decrypt the ciphertext in a distributed manner. This way, the plaintext is never exposed to the individual servers. As an important building block in this scenario, we propose a new, provably secure family of lightweight modes for authenticated encryption with associated data (AEAD), called Eevee. The Eevee family has fully parallel decryption, making it suitable for MPC protocols for which the round complexity depends on the complexity of the function they compute. Further, our modes use the lightweight forkcipher primitive that offers fixed-length output expansion and a compact yet parallelizable internal structure. All Eevee members improve substantially over the few available state-of-the-art (SotA) MPC-friendly modes and other standard solutions. We benchmark the Eevee family on a microcontroller and in MPC. Our proposed mode Jolteon (when instantiated with ForkSkinny) provides 1.85x to 3.64x speedup in IoT-encryption time and 3x to 4.5x speedup in both MPC-decryption time and data for very short queries of 8 bytes and, 1.55x to 3.04x and 1.23x to 2.43x speedup, respectively, in MPC-decryption time and data for queries up to 500 bytes when compared against SotA MPC-friendly modes instantiated with SKINNY. We also provide two advanced modes, Umbreon and Espeon, that show a favorable performance-security trade-off with stronger security guarantees such as nonce-misuse security. Additionally, all Eevee members have full $n$-bit security (where $n$ is the block size of the underlying primitive), use a single primitive and require smaller state and HW area when compared with the SotA modes under their original security settings.

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **Two-Round Adaptively Secure MPC from Isogenies, LPN, or CDH**
  2023-07-29 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-92075-3_11) · [IACR ePrint](https://eprint.iacr.org/2023/1170)
  Pratik Sarkar, Navid Alamati, Sikhar Patranabis, Hart William Montgomery, Hart Montgomery

  <details><summary>摘要 / Abstract</summary>

  We present a new framework for building round-optimal (two-round) $adaptively$ secure MPC. We show that a relatively weak notion of OT that we call $indistinguishability \ OT \ with \ receiver \ oblivious \ sampleability$ (r-iOT) is enough to build two-round, adaptively secure MPC against $malicious$ adversaries in the CRS model. We then show how to construct r-iOT from CDH, LPN, or isogeny-based assumptions that can be viewed as group actions (such as CSIDH and CSI-FiSh). This yields the first constructions of two-round adaptively secure MPC against malicious adversaries from CDH, LPN, or isogeny-based assumptions. We further extend our non-isogeny results to the plain model, achieving (to our knowledge) the first construction of two-round adaptively secure MPC against semi-honest adversaries in the plain model from LPN. Our results allow us to build a two-round adaptively secure MPC against malicious adversaries from essentially all of the well-studied assumptions in cryptography. In addition, our constructions from isogenies or LPN provide the first post-quantum alternatives to LWE-based constructions for round-optimal adaptively secure MPC. Along the way, we show that r-iOT also implies non-committing encryption(NCE), thereby yielding the first constructions of NCE from isogenies or LPN.

  匹配依据：MPC: mpc (context)

  </details>

- **Malicious Secure, Structure-Aware Private Set Intersection**
  2023-07-28 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-38557-5_19) · [IACR ePrint](https://eprint.iacr.org/2023/1166)
  Jaspal Singh, Gayathri Garimella, Mike Rosulek

  <details><summary>摘要 / Abstract</summary>

  Structure-Aware private set intersection (sa-PSI) is a variant of PSI where Alice&#x27;s input set $A$ has some publicly known structure, Bob&#x27;s input $B$ is an unstructured set of points, and Alice learns the intersection $A \cap B$. sa-PSI was recently introduced by Garimella et al. (Crypto 2022), who described a semi-honest protocol with communication that scales with the description size of Alice&#x27;s set, instead of its cardinality. In this paper, we present the first sa-PSI protocol secure against malicious adversaries. sa-PSI protocols are built from function secret sharing (FSS) schemes, and the main challenge in our work is ensuring that multiple FSS sharings encode the same structured set. We do so using a cut-and-choose approach. In order to make FSS compatible with cut-and-choose, we introduce a new variant of function secret sharing, called derandomizable FSS (dFSS). We show how to construct dFSS for union of geometric balls, leading to a malicious-secure sa-PSI protocol where Alice&#x27;s input is a union of balls. We also improve prior FSS constructions, giving asymptotic improvements to semi-honest sa-PSI.

  匹配依据：MPC: private set intersection, secret sharing

  </details>

- **Improved Polynomial Secret-Sharing Schemes**
  2023-07-27 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-48618-0_13) · [IACR ePrint](https://eprint.iacr.org/2023/1158)
  Or Lasri, Oriol Farràs, Amos Beimel

  <details><summary>摘要 / Abstract</summary>

  Despite active research on secret-sharing schemes for arbitrary access structures for more than 35 years, we do not understand their share size $-$ the best known upper bound for an arbitrary n-party access structure is $2^{O(n)}$ while the best known lower bound is $\Omega(n/\log(n))$. Consistent with our knowledge, the share size can be anywhere between these bounds. To better understand this question, one can study specific families of secret-sharing schemes. For example, linear secret-sharing schemes, in which the sharing and reconstruction are computed by linear mappings, have been studied in many papers, e.g., it is known that they require shares of size at least $2^{0.5n}$. Secret-sharing schemes in which the sharing and/or reconstruction are computed by low-degree polynomials have been recently studied by Paskin-Cherniavsky and Radune [ITC 2020] and by Beimel, Othman, and Peter [CRYPTO 2021]. It was shown that secret-sharing schemes with sharing and reconstruction computed by polynomials of degree 2 are more efficient than linear schemes (i.e., schemes in which the sharing and reconstruction are computed by polynomials of degree one). Prior to our work, it was not known if using polynomials of higher degree can reduce the share size. We show that this is indeed the case, i.e., we construct secret-sharing schemes with reconstruction by degree-$d$ polynomials, where as the reconstruction degree $d$ increases, the share size for arbitrary access structures decreases. As a step in our construction, we construct conditional disclosure of secrets (CDS) protocols. For example, we construct 2-server CDS protocols for functions $f : [N ] \times [N ] \to \{0, 1\}$ with reconstruction computed by degree-d polynomials with message size $N^{O(\log \log d/ \log d)}$. Combining our results with a lower bound of Beimel et al. [CRYPTO 2021], we show that increasing the degree of the reconstruction function in CDS protocols provably reduces the message size. To construct our schemes, we define sparse matching vectors, show constructions of such vectors, and design CDS protocols and secret-sharing schemes with degree-$d$ reconstruction from sparse matching vectors.

  匹配依据：MPC: secret sharing

  </details>

- **TVA: A multi-party computation system for secure and expressive time series analytics**
  2023-07-19 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/faisal) · [IACR ePrint](https://eprint.iacr.org/2023/1120)
  Vasiliki Kalavri, Mayank Varia, John Liagouris, Muhammad Faisal, Jerry Zhang

  <details><summary>摘要 / Abstract</summary>

  We present TVA, a multi-party computation (MPC) system for secure analytics on secret-shared time series data. TVA achieves strong security guarantees in the semi-honest and malicious settings, and high expressivity by enabling complex analytics on inputs with unordered and irregular timestamps. TVA is the first system to support arbitrary composition of oblivious window operators, keyed aggregations, and multiple filter predicates, while keeping all data attributes private, including record timestamps and user-defined values in query predicates. At the core of the TVA system lie novel protocols for secure window assignment: (i) a tumbling window protocol that groups records into fixed-length time buckets and (ii) two session window protocols that identify periods of activity followed by periods of inactivity. We also contribute a new protocol for secure division with a public divisor, which may be of independent interest. We evaluate TVA on real LAN and WAN environments and show that it can efficiently compute complex window-based analytics on inputs of $2^{22}$ records with modest use of resources. When compared to the state-of-the-art, TVA achieves up to $5.8\times$ lower latency in queries with multiple filters and two orders of magnitude better performance in window aggregation.

  匹配依据：MPC: multi party computation

  </details>

- **Reusable Secure Computation in the Plain Model**
  2023-06-28 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-38557-5_14) · [IACR ePrint](https://eprint.iacr.org/2023/1006)
  Akshayaram Srinivasan, Mingyuan Wang, Vipul Goyal

  <details><summary>摘要 / Abstract</summary>

  Consider the standard setting of two-party computation where the sender has a secret function $f$ and the receiver has a secret input $x$ and the output $f(x)$ is delivered to the receiver at the end of the protocol. Let us consider the unidirectional message model where only one party speaks in each round. In this setting, Katz and Ostrovsky (Crypto 2004) showed that at least four rounds of interaction between the parties are needed in the plain model (i.e., no trusted setup) if the simulator uses the adversary in a black-box way (a.k.a. black-box simulation). Suppose the sender and the receiver would like to run multiple sequential iterations of the secure computation protocol on possibly different inputs. For each of these iterations, do the parties need to start the protocol from scratch and exchange four messages? In this work, we explore the possibility of \textit{amortizing} the round complexity or in other words, \textit{reusing} a certain number of rounds of the secure computation protocol in the plain model. We obtain the following results. 1. Under standard cryptographic assumptions, we construct a four-round two-party computation protocol where (i) the first three rounds of the protocol could be reused an unbounded number of times if the receiver input remains the same and only the sender input changes, and (ii) the first two rounds of the protocol could be reused an unbounded number of times if the receiver input needs to change as well. In other words, the sender sends a single additional message if only its input changes, and in the other case, we need one message each from the receiver and the sender. The number of additional messages needed in each of the above two modes is optimal and, additionally, our protocol allows arbitrary interleaving of these two modes. 2. We also extend these results to the multiparty setting (in the simultaneous message exchange model) and give round-optimal protocols such that (i) the first two rounds could be reused an unbounded number of times if the inputs of the parties need to change and (ii) the first three rounds could be reused an unbounded number of times if the inputs remain the same but the functionality to be computed changes. As in the two-party setting, we allow arbitrary interleaving of the above two modes of operation.

  匹配依据：MPC: secure computation, two party computation

  </details>

- **Succinct Computational Secret Sharing**
  2023-06-18 · MPC · 含会议/期刊记录 · [STOC](https://doi.org/10.1145/3564246.3585127) · [IACR ePrint](https://eprint.iacr.org/2023/955)
  Tianren Liu, Yuval Ishai, Benny Applebaum, Vinod Vaikuntanathan, Eyal Kushilevitz, Amos Beimel

  <details><summary>摘要 / Abstract</summary>

  A secret-sharing scheme enables a dealer to share a secret $s$ among $n$ parties such that only authorized subsets of parties, specified by a monotone access structure $f:\{0,1\}^n\to\{0,1\}$, can reconstruct $s$ from their shares. Other subsets of parties learn nothing about $s$. The question of minimizing the (largest) share size for a given $f$ has been the subject of a large body of work. However, in most existing constructions for general access structures $f$, the share size is not much smaller than the size of some natural computational representation of $f$, a fact that has often been referred to as the ``representation size barrier&#x27;&#x27; in secret sharing. In this work, we initiate a systematic study of succinct computational secret sharing (SCSS), where the secrecy requirement is computational and the goal is to substantially beat the representation size barrier. We obtain the following main results. (1) SCSS via Projective PRGs. We introduce the notion of a *projective PRG*, a pseudorandom generator for which any subset of the output bits can be revealed while keeping the other output bits hidden, using a *short* projective seed. We construct projective PRGs with different levels of succinctness under a variety of computational assumptions, and apply them towards constructing SCSS for graph access structures, monotone CNF formulas, and (less succinctly) useful subclasses of monotone circuits and branching programs. Most notably, under the sub-exponential RSA assumption, we obtain a SCSS scheme that, given an arbitrary access structure $f$, represented by a truth table of size $N=2^n$, produces shares of size polylog(N)=\poly(n) in time $\tilde O(N)$. For comparison, the share size of the best known information-theoretic schemes is $O(N^{0.58})$. (2) SCSS via One-way Functions. Under the (minimal) assumption that one-way functions exist, we obtain a near-quadratic separation between the total share size of computational and information-theoretic secret sharing. This is the strongest separation one can hope for, given the state of the art in secret sharing lower bounds. We also construct SCSS schemes from one-way functions for useful classes of access structures, including forbidden graphs and monotone DNF formulas. This leads to constructions of fully-decomposable conditional disclosure of secrets (also known as privacy-free garbled circuits) for general functions, represented by a truth table of size $N=2^n$, with share size polylog(N) and computation time $\tilde O(N)$, assuming sub-exponentially secure one-way functions.

  匹配依据：MPC: garbled circuits, secret sharing

  </details>

- **Proactive Secret Sharing with Constant Communication**
  2023-06-16 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-48618-0_12) · [IACR ePrint](https://eprint.iacr.org/2023/942)
  Daniel Noble, Brett Hemenway, Tal Rabin, Brett Hemenway Falk

  <details><summary>摘要 / Abstract</summary>

  This paper presents the first protocols for Proactive Secret Sharing (PSS) that only require constant (in the number of parties, $n$) communication per party per epoch. By harnessing the power of expander graphs, we are able to obtain strong guarantees about the security of the system. We present the following PSS protocols: – A PSS protocol that provides privacy (but no robustness) against an adversary controlling $O(n)$ parties per epoch. – A PSS protocol that provides robustness (but no privacy) against an adversary controlling $O(n)$ parties per epoch. – A PSS protocol that provides privacy against an adversary controlling $O(n^{a})$ parties per epoch and provides robustness against an adversary controlling $O(n^{1−a})$ parties per epoch, for any constant $0 \leq a \leq 1$. Instantiating this with $a = \frac{1}{2}$ gives a PSS protocol that is proactively secure (private and robust) against an adversary controlling $O(\sqrt{n})$ parties per epoch. Additionally, we discuss how secure channels, whose existence is usually assumed by PSS protocols, are challenging to create in the mobile adversary setting, and we present a method to instantiate them from a weaker assumption.

  匹配依据：MPC: secret sharing

  </details>

- **Threshold Private Set Intersection with Better Communication Complexity**
  2023-06-12 · MPC · 含会议/期刊记录 · [PKC](https://doi.org/10.1007/978-3-031-31371-4_9) · [IACR ePrint](https://eprint.iacr.org/2023/919)
  Satrajit Ghosh, Mark Simkin

  <details><summary>摘要 / Abstract</summary>

  Given $\ell$ parties with sets $X_1, \dots, X_\ell$ of size $n$, we would like to securely compute the intersection $\cap_{i=1}^\ell X_i$, if it is larger than $n-t$ for some threshold $t$, without revealing any other additional information. It has previously been shown (Ghosh and Simkin, Crypto 2019) that this function can be securely computed with a communication complexity that only depends on $t$ and in particular does not depend on $n$. For small values of $t$, this results in protocols that have a communication complexity that is sublinear in the size of the inputs. Current protocols either rely on fully homomorphic encryption or have an at least quadratic dependency on the parameter $t$. In this work, we construct protocols with a quasilinear dependency on $t$ from simple assumptions like additively homomorphic encryption and oblivious transfer. All existing approaches, including ours, rely on protocols for computing a single bit, which indicates whether the intersection is larger than $n-t$ without actually computing it. Our key technical contribution, which may be of independent interest, takes any such protocol with secret shared outputs and communication complexity $\mathcal{O}(\lambda \ell \cdot\mathrm{poly}(t))$, where $\lambda$ is the security parameter, and transforms it into a protocol with communication complexity $\mathcal{O}(\lambda^2 \ell t \cdot\mathrm{polylog}(t))$.

  匹配依据：MPC: oblivious transfer, private set intersection

  </details>

- **Efficient 3PC for Binary Circuits with Application to Maliciously-Secure DNN Inference**
  2023-06-12 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/li-yun) · [IACR ePrint](https://eprint.iacr.org/2023/909)
  Zhicong Huang, Yufei Duan, Yifan Song, Yun Li, Chao Zhang, Cheng Hong

  <details><summary>摘要 / Abstract</summary>

  In this work, we focus on maliciously secure 3PC for binary circuits with honest majority. While the state-of-the-art (Boyle et al. CCS 2019) has already achieved the same amortized communication as the best-known semi-honest protocol (Araki et al. CCS 2016), they suffer from a large computation overhead: when comparing with the best-known implementation result (Furukawa et al. Eurocrypt 2017) which requires $9\times$ communication cost of Araki et al., the protocol by Boyle et al. is around $4.5\times$ slower than that of Furukawa et al. In this paper, we design a maliciously secure 3PC protocol that matches the same communication as Araki et al. with comparable concrete efficiency as Furukawa et al. To obtain our result, we manage to apply the distributed zero-knowledge proofs (Boneh et al. Crypto 2019) for verifying computations over $\mathbb{Z}_2$ by using \emph{prime} fields and explore the algebraic structure of prime fields to make the computation of our protocol friendly for native CPU computation. Experiment results show that our protocol is around $3.5\times$ faster for AES circuits than Boyle et al. We also applied our protocol to the binary part (e.g. comparison and truncation) of secure deep neural network inference, and results show that we could reduce the time cost of achieving malicious security in the binary part by more than $67\%$. Besides our main contribution, we also find a hidden security issue in many of the current probabilistic truncation protocols, which may be of independent interest.

  匹配依据：MPC: 3pc (context)

  </details>

- **Secure Multiparty Computation with Free Branching**
  2023-06-09 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-06944-4_14) · [IACR ePrint](https://eprint.iacr.org/2023/901)
  Aarushi Goel, Aditya Hegde, Mathias Hall-Andersen, Abhishek Jain

  <details><summary>摘要 / Abstract</summary>

  We study secure multi-party computation (MPC) protocols for branching circuits that contain multiple sub-circuits (i.e., branches) and the output of the circuit is that of a single active branch. Crucially, the identity of the active branch must remain hidden from the protocol participants. While such circuits can be securely computed by evaluating each branch and then multiplexing the output, such an approach incurs a communication cost linear in the size of the entire circuit. To alleviate this, a series of recent works have investigated the problem of reducing the communication cost of branching executions inside MPC (without relying on fully homomorphic encryption). Most notably, the stacked garbling paradigm [Heath and Kolesnikov, CRYPTO&#x27;20] yields garbled circuits for branching circuits whose size only depends on the size of the largest branch. Presently, however, it is not known how to obtain similar communication improvements for secure computation involving more than two parties. In this work, we provide a generic framework for branching multi-party computation that supports any number of parties. The communication complexity of our scheme is proportional to the size of the largest branch and the computation is linear in the size of the entire circuit. We provide an implementation and benchmarks to demonstrate practicality of our approach.

  匹配依据：MPC: garbled circuits, multi party computation, secure computation, secure multi party computation, secure multiparty computation

  </details>

- **Towards Topology-Hiding Computation from Oblivious Transfer**
  2023-06-06 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-48615-9_13) · [IACR ePrint](https://eprint.iacr.org/2023/849)
  Lisa Kohl, Marshall Ball, Alexander Bienstock, Pierre Meyer

  <details><summary>摘要 / Abstract</summary>

  Topology-Hiding Computation (THC) enables parties to securely compute a function on an incomplete network without revealing the network topology. It is known that secure computation on a complete network can be based on oblivious transfer (OT), even if a majority of the participating parties are corrupt. In contrast, THC in the dishonest majority setting is only known from assumptions that imply (additively) homomorphic encryption, such as Quadratic Residuosity, Decisional Diffie-Hellman, or Learning With Errors. In this work we move towards closing the gap between MPC and THC by presenting a protocol for THC on general graphs secure against all-but-one semi-honest corruptions from constant-round constant-overhead secure two-party computation. Our protocol is therefore the first to achieve THC on arbitrary networks without relying on assumptions with rich algebraic structure. As a technical tool, we introduce the notion of locally simulatable MPC, which we believe to be of independent interest.

  匹配依据：MPC: oblivious transfer, secure computation, secure two party computation

  </details>

- **Oblivious Transfer with Constant Computational Overhead**
  2023-06-02 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-30545-0_10) · [IACR ePrint](https://eprint.iacr.org/2023/817)
  Lisa Kohl, Elette Boyle, Peter Scholl, Yuval Ishai, Geoffroy Couteau, Nicolas Resch, Niv Gilboa

  <details><summary>摘要 / Abstract</summary>

  The computational overhead of a cryptographic task is the asymptotic ratio between the computational cost of securely realizing the task and that of realizing the task with no security at all. Ishai, Kushilevitz, Ostrovsky, and Sahai (STOC 2008) showed that secure two-party computation of Boolean circuits can be realized with constant computational overhead, independent of the desired level of security, assuming the existence of an oblivious transfer (OT) protocol and a local pseudorandom generator (PRG). However, this only applies to the case of semi-honest parties. A central open question in the area is the possibility of a similar result for malicious parties. This question is open even for the simpler task of securely realizing many instances of a constant-size function, such as OT of bits. We settle the question in the affirmative for the case of OT, assuming: (1) a standard OT protocol, (2) a slightly stronger &quot;correlation-robust&quot; variant of a local PRG, and (3) a standard sparse variant of the Learning Parity with Noise (LPN) assumption. An optimized version of our construction requires fewer than 100 bit operations per party per bit-OT. For 128-bit security, this improves over the best previous protocols by 1-2 orders of magnitude. We achieve this by constructing a constant-overhead pseudorandom correlation generator (PCG) for the bit-OT correlation. Such a PCG generates $N$ pseudorandom instances of bit-OT by locally expanding short, correlated seeds. As a result, we get an end-to-end protocol for generating $N$ pseudorandom instances of bit-OT with $o(N)$ communication, $O(N)$ computation, and security that scales sub-exponentially with $N$. Finally, we present applications of our main result to realizing other secure computation tasks with constant computational overhead. These include protocols for general circuits with a relaxed notion of security against malicious parties, protocols for realizing $N$ instances of natural constant-size functions, and reducing the main open question to a potentially simpler question about fault-tolerant computation.

  匹配依据：MPC: oblivious transfer, secure computation, secure two party computation

  </details>

- **Network Agnostic MPC with Statistical Security**
  2023-06-02 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2306.01401) · [series/lncs](https://doi.org/10.1007/978-3-031-48618-0_3) · [IACR ePrint](https://eprint.iacr.org/2023/820)
  Ananya Appan, Ashish Choudhury

  <details><summary>摘要 / Abstract</summary>

  We initiate the study of the network agnostic MPC protocols with statistical security. Network agnostic protocols give the best possible security guarantees irrespective of the underlying network type. We consider the general-adversary model, where the adversary is characterized by an adversary structure which enumerates all possible candidate subsets of corrupt parties. The $\mathcal{Q}^{(k)}$ condition enforces that the union of no $k$ subsets from the adversary structure covers the party set. Given an unconditionally-secure PKI setup, known statistically-secure synchronous MPC protocols are secure against adversary structures satisfying the $\mathcal{Q}^{(2)}$ condition. Known statistically-secure asynchronous MPC protocols can tolerate $\mathcal{Q}^{(3)}$ adversary structures. Fix a set of $n$ parties $\mathcal{P} = \{P_1, ... ,P_n\}$ and adversary structures $\mathcal{Z}_s$ and $\mathcal{Z}_a$, satisfying the $\mathcal{Q}^{(2)}$ and $\mathcal{Q}^{(3)}$ conditions respectively, where $\mathcal{Z}_a \subset \mathcal{Z}_s$. Then, given an unconditionally-secure PKI, we ask whether it is possible to design a statistically-secure MPC protocol resilient against $\mathcal{Z}_s$ and $\mathcal{Z}_a$ in a synchronous and an asynchronous network respectively if the parties in $\mathcal{P}$ are unaware of the network type. We show that it is possible iff $\mathcal{Z}_s$ and $\mathcal{Z}_a$ satisfy the $\mathcal{Q}^{(2,1)}$ condition, meaning that the union of any two subsets from $\mathcal{Z}_s$ and any one subset from $\mathcal{Z}_a$ is a proper subset of $\mathcal{P}$. We design several important network agnostic building blocks with the $\mathcal{Q}^{(2,1)}$ condition, such as Byzantine broadcast, Byzantine agreement, information checking protocol, verifiable secret-sharing and secure multiplication protocol, whose complexity is polynomial in $n$ and $|\mathcal{Z}_s|$.

  匹配依据：MPC: secret sharing

  </details>

- **New Bounds on the Local Leakage Resilience of Shamir's Secret Sharing Scheme**
  2023-06-01 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-38557-5_5) · [IACR ePrint](https://eprint.iacr.org/2023/805)
  Ohad Klein, Ilan Komargodski

  <details><summary>摘要 / Abstract</summary>

  We study the local leakage resilience of Shamir&#x27;s secret sharing scheme. In Shamir&#x27;s scheme, a random polynomial $f$ of degree $t$ is sampled over a field of size $p&gt;n$, conditioned on $f(0)=s$ for a secret $s$. Any $t$ shares $(i, f(i))$ can be used to fully recover $f$ and thereby $f(0)$. But, any $t-1$ evaluations of $f$ at non-zero coordinates are completely independent of $f(0)$. Recent works ask whether the secret remains hidden even if say only 1 bit of information is leaked from each share, independently. This question is well motivated due to the wide range of applications of Shamir&#x27;s scheme. For instance, it is known that if Shamir&#x27;s scheme is leakage resilient in some range of parameters, then known secure computation protocols are secure in a local leakage model. Over characteristic 2 fields, the answer is known to be negative (e.g., Guruswami and Wootters, STOC &#x27;16). Benhamouda, Degwekar, Ishai, and Rabin (CRYPTO &#x27;18) were the first to give a positive answer assuming computation is done over prime-order fields. They showed that if $t \ge 0.907n$, then Shamir&#x27;s scheme is leakage resilient. Since then, there has been extensive efforts to improve the above threshold and after a series of works, the current record shows leakage resilience for $t\ge 0.78n$ (Maji et al., ISIT &#x27;22). All existing analyses of Shamir&#x27;s leakage resilience for general leakage functions follow a single framework for which there is a known barrier for any $t \le 0.5 n$. In this work, we a develop a new analytical framework that allows us to significantly improve upon the previous record and obtain additional new results. Specifically, we show: $\bullet$ Shamir&#x27;s scheme is leakage resilient for any $t \ge 0.69n$. $\bullet$ If the leakage functions are guaranteed to be ``balanced&#x27;&#x27; (i.e., splitting the domain of possible shares into 2 roughly equal-size parts), then Shamir&#x27;s scheme is leakage resilient for any $t \ge 0.58n$. $\bullet$ If the leakage functions are guaranteed to be ``unbalanced&#x27;&#x27; (i.e., splitting the domain of possible shares into 2 parts of very different sizes), then Shamir&#x27;s scheme is leakage resilient as long as $t \ge 0.01 n$. Such a result is $provably$ impossible to obtain using the previously known technique. All of the above apply more generally to any MDS codes-based secret sharing scheme. Confirming leakage resilience is most important in the range $t \leq n/2$, as in many applications, Shamir’s scheme is used with thresholds $t\leq n/2$. As opposed to the previous approach, ours does not seem to have a barrier at $t=n/2$, as demonstrated by our third contribution.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Unconditionally Secure Multiparty Computation for Symmetric Functions with Low Bottleneck Complexity**
  2023-05-10 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-981-99-8721-4_11) · [IACR ePrint](https://eprint.iacr.org/2023/662)
  Reo Eriguchi

  <details><summary>摘要 / Abstract</summary>

  Bottleneck complexity is an efficiency measure of secure multiparty computation (MPC) introduced by Boyle et al. (ICALP 2018) to achieve load-balancing. Roughly speaking, it is defined as the maximum communication complexity required by any player within the protocol execution. Since it was shown to be impossible to achieve sublinear bottleneck complexity in the number of players $n$ for all functions, a prior work constructed MPC protocols with low bottleneck complexity for specific functions. However, the previous protocol for symmetric functions needs to assume a computational primitive of garbled circuits and its unconditionally secure variant has exponentially large bottleneck complexity in the depth of an arithmetic formula computing the function, which limits the class of symmetric functions the protocol can compute with sublinear bottleneck complexity in $n$. In this work, we make the following contributions to unconditionally secure MPC protocols for symmetric functions with sublinear bottleneck complexity in $n$. \begin{itemize} \item We propose for the first time unconditionally secure MPC protocols computing \textit{any} symmetric function with sublinear bottleneck complexity in $n$. Technically, our first protocol is inspired by the one-time truth-table protocol by Ishai et al. (TCC 2013) but our second and third protocols use a novel technique to express the one-time truth-table as an array of two or higher dimensions and achieve better trade-offs. \item We propose an unconditionally secure protocol tailored to the AND function with lower bottleneck complexity. It avoids pseudorandom functions used by the previous protocol for the AND function, preserving bottleneck complexity up to a logarithmic factor in $n$. \item By combining our protocol for the AND function with Bloom filters, we construct an unconditionally secure protocol for private set intersection (PSI), which computes the intersection of players&#x27; private sets. This is the first PSI protocol with sublinear bottleneck complexity in $n$ and to the best of our knowledge, there has been no such protocol even under cryptographic assumptions. \end{itemize}

  匹配依据：MPC: garbled circuits, private set intersection, secure multiparty computation

  </details>

- **DORAM revisited: Maliciously secure RAM-MPC with logarithmic overhead**
  2023-04-24 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-48615-9_16) · [IACR ePrint](https://eprint.iacr.org/2023/578)
  Brett Hemenway, Daniel Noble, Jacob Zhang, Matan Shtepel, Rafail Ostrovsky, Brett Falk

  <details><summary>摘要 / Abstract</summary>

  Distributed Oblivious Random Access Memory (DORAM) is a secure multiparty protocol that allows a group of participants holding a secret-shared array to read and write to secret-shared locations within the array. The efficiency of a DORAM protocol is measured by the amount of communication and computation required per read/write query into the array. DORAM protocols are a necessary ingredient for executing Secure Multiparty Computation (MPC) in the RAM model. Although DORAM has been widely studied, all existing DORAM protocols have focused on the setting where the DORAM servers are semi-honest. Generic techniques for upgrading a semi-honest DORAM protocol to the malicious model typically increase the asymptotic communication complexity of the DORAM scheme. In this work, we present a 3-party DORAM protocol which requires $O((\kappa + D)\log N)$ communication and computation per query, for a database of size $N$ with $D$-bit values, where $\kappa$ is the security parameter. Our hidden constants in a big-O nation are small. We show that our protocol is UC-secure in the presence of a malicious, static adversary. This matches the communication and computation complexity of the best semi-honest DORAM protocol, and is the first malicious DORAM protocol with this complexity.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Secure Computation with Shared EPR Pairs (Or: How to Teleport in Zero-Knowledge)**
  2023-04-20 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2304.10480) · [CRYPTO](https://doi.org/10.1007/978-3-031-38554-4_8) · [IACR ePrint](https://eprint.iacr.org/2023/564)
  Akshayaram Srinivasan, James Bartusek, Dakshita Khurana

  <details><summary>摘要 / Abstract</summary>

  Can a sender non-interactively transmit one of two strings to a receiver without knowing which string was received? Does there exist minimally-interactive secure multiparty computation that only makes (black-box) use of symmetric-key primitives? We provide affirmative answers to these questions in a model where parties have access to shared EPR pairs, thus demonstrating the cryptographic power of this resource. First, we construct a one-shot (i.e., single message) string oblivious transfer (OT) protocol with random receiver bit in the shared EPR pairs model, assuming the (sub-exponential) hardness of LWE. Building on this, we show that {\em secure teleportation through quantum channels} is possible. Specifically, given the description of any quantum operation $Q$, a sender with (quantum) input $\rho$ can send a single classical message that securely transmits $Q(\rho)$ to a receiver. That is, we realize an ideal quantum channel that takes input $\rho$ from the sender and provably delivers $Q(\rho)$ to the receiver without revealing any other information. This immediately gives a number of applications in the shared EPR pairs model: (1) non-interactive secure computation of unidirectional \emph{classical} randomized functionalities, (2) NIZK for QMA from standard (sub-exponential) hardness assumptions, and (3) a non-interactive \emph{zero-knowledge} state synthesis protocol. Next, we construct a two-round (round-optimal) secure multiparty computation protocol for classical functionalities in the shared EPR pairs model that is \emph{unconditionally-secure} in the (quantum-accessible) random oracle model. Classically, both of these results cannot be obtained without some form of correlated randomness shared between the parties, and the only known approach is to have a trusted dealer set up random (string) OT correlations. In the quantum world, we show that shared EPR pairs (which are simple and can be deterministically generated) are sufficient. At the heart of our work are novel techniques for making use of entangling operations to generate string OT correlations, and for instantiating the Fiat-Shamir transform using correlation-intractability in the quantum setting.

  匹配依据：MPC: oblivious transfer, secure computation, secure multiparty computation

  </details>

- **Detect, Pack and Batch: Perfectly-Secure MPC with Linear Communication and Constant Expected Time**
  2023-04-19 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-30617-4_9) · [IACR ePrint](https://eprint.iacr.org/2023/557)
  Ittai Abraham, Gilad Asharov, Shravani Patil, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  We prove that perfectly-secure optimally-resilient secure Multi-Party Computation (MPC) for a circuit with $C$ gates and depth $D$ can be obtained in $O((Cn+n^4 + Dn^2)\log n)$ communication complexity and $O(D)$ expected time. For $D \ll n$ and $C\geq n^3$, this is the first perfectly-secure optimal-resilient MPC protocol with linear communication complexity per gate and constant expected time complexity per layer. Compared to state-of-the-art MPC protocols in the player elimination framework [Beerliova and Hirt TCC&#x27;08, and Goyal, Liu, and Song CRYPTO&#x27;19], for $C&gt;n^3$ and $D \ll n$, our results significantly improve the run time from $\Omega(n+D)$ to expected $O(D)$ while keeping communication complexity at $O(Cn\log n)$. Compared to state-of-the-art MPC protocols that obtain an expected $O(D)$ time complexity [Abraham, Asharov, and Yanai TCC&#x27;21], for $C&gt;n^3$, our results significantly improve the communication complexity from $O(Cn^4\log n)$ to $O(Cn\log n)$ while keeping the expected run time at $O(D)$. One salient part of our technical contribution is centered around a new primitive we call &quot;detectable secret sharing&quot;. It is perfectly-hiding, weakly-binding, and has the property that either reconstruction succeeds or $O(n)$ parties are (privately) detected. On the one hand, we show that detectable secret sharing is sufficiently powerful to generate multiplication triplets needed for MPC. On the other hand, we show how to share $p$ secrets via detectable secret sharing with communication complexity of just $O(n^4\log n+p \log n)$. When sharing $p\geq n^4$ secrets, the communication cost is amortized to just $O(1)$ field elements per secret. Our second technical contribution is a new Verifiable Secret Sharing protocol that can share $p$ secrets at just $O(n^4\log n+pn\log n)$ word complexity. When sharing $p\geq n^3$ secrets, the communication cost is amortized to just $O(n)$ filed elements per secret. The best prior required $\Omega(n^3)$ communication per secret.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Squirrel: A Scalable Secure Two-Party Computation Framework for Training Gradient Boosting Decision Tree**
  2023-04-12 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/lu) · [IACR ePrint](https://eprint.iacr.org/2023/527)
  Zhicong Huang, Qizhi Zhang, Wen-jie Lu, Yuchen Wang, Cheng Hong

  <details><summary>摘要 / Abstract</summary>

  Gradient Boosting Decision Tree (GBDT) and its variants are widely used in industry, due to their strong interpretability. Secure multi-party computation allows multiple data owners to compute a function jointly while keeping their input private. In this work, we present Squirrel, a two-party GBDT training framework on a vertically split dataset, where two data owners each hold different features of the same data samples. Squirrel is private against semi-honest adversaries, and no sensitive intermediate information is revealed during the training process. Squirrel is also scalable to datasets with millions of samples even under a Wide Area Network (WAN). Squirrel achieves its high performance via several novel co-designs of the GBDT algorithms and advanced cryptography. Especially, 1) we propose a new and efficient mechanism to hide the sample distribution on each node using oblivious transfer. 2) We propose a highly optimized method for gradient aggregation using lattice-based homomorphic encryption (HE). Our empirical results show that our method can be three orders of magnitude faster than the existing HE approaches. 3) We propose a novel protocol to evaluate the sigmoid func- tion on secretly shared values, showing 19×-200×-fold im- provements over two existing methods. Combining all these improvements, Squirrel costs less than 6 seconds per tree on a dataset with 50 thousands samples which outperforms Pivot (VLDB 2020) by more than 28×. We also show that Squirrel can scale up to datasets with more than one million samples, e.g., about 170 seconds per tree over a WAN.

  匹配依据：MPC: oblivious transfer, secure multi party computation, secure two party computation

  </details>

- **Breaking and Fixing Garbled Circuits when a Gate has Duplicate Input Wires**
  2023-04-12 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-023-09472-4) · [IACR ePrint](https://eprint.iacr.org/2023/530)
  Thomas Schneider, Raine Nieminen

  <details><summary>摘要 / Abstract</summary>

  Garbled circuits are a fundamental cryptographic primitive that allows two or more parties to securely evaluate an arbitrary Boolean circuit without revealing any information beyond the output using a constant number of communication rounds. Garbled circuits have been introduced by Yao (FOCS’86) and generalized to the multi-party setting by Beaver, Micali and Rogaway (STOC’90). Since then, several works have improved their efficiency by providing different garbling schemes and several implementations exist. Starting with the seminal Fairplay compiler (USENIX Security’04), several implementation frameworks decoupled the task of compiling the function to be evaluated into a Boolean circuit from the engine that securely evaluates that circuit, e.g., using a secure two-party computation protocol based on garbled circuits. In this paper, we show that this decoupling of circuit generation and evaluation allows a subtle attack on several prominent garbling schemes. It occurs when violating the implicit assumption on the circuit that gates have different input wires which is most often not explicitly specified in the respective papers. The affected garbling schemes use separate calls to a deterministic encryption function for the left and right input wire of a gate to derive pseudo-random encryption pads that are XORed together. When a circuit contains a gate where the left and right input wire are the same, these two per-wire encryption pads cancel out and we demonstrate that this can result in a complete break of privacy. We show how the vulnerable garbling schemes can be fixed easily.

  匹配依据：MPC: garbled circuits, garbling schemes, secure two party computation

  </details>

- **Sublinear Secure Computation from New Assumptions**
  2023-04-10 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-22365-5_5) · [IACR ePrint](https://eprint.iacr.org/2023/513)
  Elette Boyle, Geoffroy Couteau, Pierre Meyer

  <details><summary>摘要 / Abstract</summary>

  Secure computation enables mutually distrusting parties to jointly compute a function on their secret inputs, while revealing nothing beyond the function output. A long-running challenge is understanding the required communication complexity of such protocols---in particular, when communication can be sublinear in the circuit representation size of the desired function. For certain functions, such as Private Information Retrieval (PIR), this question extends to even sublinearity in the input size. We develop new techniques expanding the set of computational assumptions for sublinear communication in both settings: 1) [Circuit size] We present sublinear-communication protocols for secure evaluation of general layered circuits, given any 2-round rate-1 batch oblivious transfer (OT) protocol with a particular ``decomposability&#x27;&#x27; property. In particular, this condition can be shown to hold for the recent batch OT protocols of (Brakerski et al. Eurocrypt 2022), in turn yielding a new sublinear secure computation feasibility result: from Quadratic Residuosity (QR) together with polynomial-noise-rate Learning Parity with Noise (LPN). Our approach constitutes a departure from existing paths toward sublinear secure computation, all based on fully homomorphic encryption or homomorphic secret sharing. 2) [Input size.] We construct single-server PIR based on the Computational Diffie-Hellman (CDH) assumption, with polylogarithmic communication in the database input size $n$. Previous constructions from CDH required communication $\Omega(n)$. In hindsight, our construction comprises of a relatively simple combination of existing tools from the literature.

  匹配依据：MPC: oblivious transfer, secret sharing, secure computation, secure evaluation

  </details>

- **3-Party Secure Computation for RAMs: Optimal and Concretely Efficient**
  2023-04-10 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-48615-9_17) · [IACR ePrint](https://eprint.iacr.org/2023/516)
  Atsunori Ichikawa, Ilan Komargodski, Ryo Kikuchi, Koki Hamada, Dai Ikarashi

  <details><summary>摘要 / Abstract</summary>

  A distributed oblivious RAM (DORAM) is a method for accessing a secret-shared memory while hiding the accessed locations. DORAMs are the key tool for secure multiparty computation (MPC) for RAM programs that avoids expensive RAM-to-circuit transformations. We present new and improved 3-party DORAM protocols. For a logical memory of size $N$ and for each logical operation, our DORAM requires $O(\log N)$ local CPU computation steps. This is known to be asymptotically optimal. Our DORAM satisfies passive security in the honest majority setting. Our technique results with concretely-efficient protocols and does not use expensive cryptography (such as re-randomizable or homomorphic encryption). Specifically, our DORAM is 25X faster than the known most efficient DORAM in the same setting. Lastly, we extend our technique to handle malicious attackers at the expense of using slightly larger blocks (i.e., $\omega(\log^2 N)$ vs. $\Omega(\log N)$). To the best of our knowledge, this is the first concretely-efficient maliciously secure DORAM. Technically, our construction relies on a novel concretely-efficient 3-party oblivious permutation protocol. We combine it with efficient non-oblivious hashing techniques (i.e., Cuckoo hashing) to get a distributed oblivious hash table. From this, we build a full-fledged DORAM using a distributed variant of the hierarchical approach of Goldreich and Ostrovsky (J. ACM &#x27;96). These ideas, and especially the permutation protocol, are of independent interest.

  匹配依据：MPC: secure computation, secure multiparty computation

  </details>

- **Constrained Pseudorandom Functions from Homomorphic Secret Sharing**
  2023-03-17 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-30620-4_7) · [IACR ePrint](https://eprint.iacr.org/2023/387)
  Alain Passelègue, Geoffroy Couteau, Mahshid Riahinia, Pierre Meyer

  <details><summary>摘要 / Abstract</summary>

  We propose and analyze a simple strategy for constructing 1-key constrained pseudorandom functions (CPRFs) from homomorphic secret sharing. In the process, we obtain the following contributions. First, we identify desirable properties for the underlying HSS scheme for our strategy to work. Second, we show that (most) recent existing HSS schemes satisfy these properties, leading to instantiations of CPRFs for various constraints and from various assumptions. Notably, we obtain the first (1-key selectively secure, private) CPRFs for inner-product and (1-key selectively secure) CPRFs for NC 1 from the DCR assumption, and more. Lastly, we revisit two applications of HSS, equipped with these additional properties, to secure computation: we obtain secure computation in the silent preprocessing model with one party being able to precompute its whole preprocessing material before even knowing the other party, and we construct one-sided statistically secure computation with sublinear communication for restricted forms of computation.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **On Homomorphic Secret Sharing from Polynomial-Modulus LWE**
  2023-03-16 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-31371-4_1) · [IACR ePrint](https://eprint.iacr.org/2023/382)
  Lisa Kohl, Thomas Attema, Pedro Capitão

  <details><summary>摘要 / Abstract</summary>

  Homomorphic secret sharing (HSS) is a form of secret sharing that supports the local evaluation of functions on the shares, with applications to multi-server private information retrieval, secure computation, and more. Insisting on additive reconstruction, all known instantiations of HSS from &quot;Learning with Error (LWE)&quot;-type assumptions either have to rely on LWE with superpolynomial modulus, come with non-negligible error probability, and/or have to perform expensive ciphertext multiplications, resulting in bad concrete efficiency. In this work, we present a new 2-party local share conversion procedure, which allows to locally convert noise encoded shares to non-noise plaintext shares such that the parties can detect whenever a (potential) error occurs and in that case resort to an alternative conversion procedure. Building on this technique, we present the first HSS for branching programs from (Ring-)LWE with polynomial input share size which can make use of the efficient multiplication procedure of Boyle et al.~(Eurocrypt 2019) and has no correctness error. Our construction comes at the cost of a -- on expectation -- slightly increased output share size (which is insignificant compared to the input share size) and a more involved reconstruction procedure. More concretely, we show that in the setting of 2-server private counting queries we can choose ciphertext sizes of only a quarter of the size of the scheme of Boyle et al. at essentially no extra cost.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Convolutions in Overdrive: Maliciously Secure Convolutions for MPC**
  2023-03-11 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2023-0084) · [IACR ePrint](https://eprint.iacr.org/2023/359)
  Marc Rivinius, Sebastian Hasler, Pascal Reisert, Ralf Küsters, Ralf Kuesters

  <details><summary>摘要 / Abstract</summary>

  Machine learning (ML) has seen a strong rise in popularity in recent years and has become an essential tool for research and industrial applications. Given the large amount of high quality data needed and the often sensitive nature of ML data, privacy-preserving collaborative ML is of increasing importance. In this paper, we introduce new actively secure multiparty computation (MPC) protocols which are specially optimized for privacy-preserving machine learning applications. We concentrate on the optimization of (tensor) convolutions which belong to the most commonly used components in ML architectures, especially in convolutional neural networks but also in recurrent neural networks or transformers, and therefore have a major impact on the overall performance. Our approach is based on a generalized form of structured randomness that speeds up convolutions in a fast online phase. The structured randomness is generated with homomorphic encryption using adapted and newly constructed packing methods for convolutions, which might be of independent interest. Overall our protocols extend the state-of-the-art Overdrive family of protocols (Keller et al., EUROCRYPT 2018). We implemented our protocols on-top of MP-SPDZ (Keller, CCS 2020) resulting in a full-featured implementation with support for faster convolutions. Our evaluation shows that our protocols outperform state-of-the-art actively secure MPC protocols on ML tasks like evaluating ResNet50 by a factor of 3 or more. Benchmarks for depthwise convolutions show order-of-magnitude speed-ups compared to existing approaches.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Ramen: Souper Fast Three-Party Computation for RAM Programs**
  2023-03-02 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3576915.3623115) · [IACR ePrint](https://eprint.iacr.org/2023/310)
  Mahak Pancholi, Lennart Braun, Rahul Rachuri, Mark Simkin

  <details><summary>摘要 / Abstract</summary>

  Secure RAM computation allows a number of parties to evaluate a function represented as a random-access machine (RAM) program in a way that reveals nothing about the private inputs of the parties except from what is already revealed by the function output itself. In this work we present \emph{Ramen}, which is a new protocol for computing RAM programs securely among three parties, tolerating up to one passive corruption. Ramen provides reasonable asymptotic guarantees and is concretely efficient at the same time. We have implemented our protocol and provide extensive benchmarks for various settings. Asymptotically, our protocol requires a constant number of rounds and an amortized sublinear amount of communication and computation per memory access. In terms of concrete efficiency, our protocol outperforms previous solutions. For a memory of size $2^{26}$ our memory accesses are \(25\times\) faster in the LAN and \(8\times\) faster in the WAN setting, when compared to the previously fastest, and concurrent, solution by Vadapalli, Henry, and Goldberg (USENIX Security 2023). Due to our superior asymptotic guarantees, the efficiency gap is only widening as the memory gets larger and for this reason Ramen provides the currently most scalable concretely efficient solution for securely computing RAM programs.

  匹配依据：MPC: three party computation

  </details>

- **Oblivious Transfer from Zero-Knowledge Proofs, or How to Achieve Round-Optimal Quantum Oblivious Transfer and Zero-Knowledge Proofs on Quantum States**
  2023-03-02 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2303.01476) · [ASIACRYPT](https://doi.org/10.1007/978-981-99-8742-9_1) · [IACR ePrint](https://eprint.iacr.org/2023/311)
  Léo Colisson Palais, Garazi Muguruza, Florian Speelman, Léo Colisson

  <details><summary>摘要 / Abstract</summary>

  We provide a generic construction to turn any classical Zero-Knowledge (ZK) protocol into a composable (quantum) oblivious transfer (OT) protocol, mostly lifting the round-complexity properties and security guarantees (plain-model/statistical security/unstructured functions…) of the ZK protocol to the resulting OT protocol. Such a construction is unlikely to exist classically as Cryptomania is believed to be different from Minicrypt. In particular, by instantiating our construction using Non-Interactive ZK (NIZK), we provide the first round-optimal (2-message) quantum OT protocol secure in the random oracle model, and round-optimal extensions to string and k-out-of-n OT. At the heart of our construction lies a new method that allows us to prove properties on a received quantum state without revealing additional information on it, even in a non-interactive way, without public-key primitives, and/or with statistical guarantees when using an appropriate classical ZK protocol. We can notably prove that a state has been partially measured (with arbitrary constraints on the set of measured qubits), without revealing any additional information on this set. This notion can be seen as an analog of ZK to quantum states, and we expect it to be of independent interest as it extends complexity theory to quantum languages, as illustrated by the two new complexity classes we introduce, ZKstatesQIP and ZKstatesQMA.

  匹配依据：MPC: oblivious transfer

  </details>

- **COMBINE: COMpilation and Backend-INdependent vEctorization for Multi-Party Computation**
  2023-01-24 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3576915.3623181) · [IACR ePrint](https://eprint.iacr.org/2023/089)
  Muhammad Ishaq, Benjamin Sherman, Lindsey Kennard, Ana L. Milanova, Benjamin Levy, Vassilis Zikas, Ben Sherman, Ana Milanova

  <details><summary>摘要 / Abstract</summary>

  Recent years have witnessed significant advances in programming technology for multi-party computation (MPC), bringing MPC closer to practice and wider applicability. Typical MPC programming frameworks focus on either front-end language design (e.g., Wysteria, Viaduct, SPDZ), or back-end protocol implementation (e.g., ABY, MOTION, SPDZ). We propose a methodology for an MPC compilation toolchain, which by mimicking the compilation methodology of classical compilers enables middle-end (i.e., machine-independent) optimizations, yielding significant improvements. We advance an intermediate language, which we call MPC-IR that can be viewed as the analogue of (enriched) Static Single Assignment (SSA) form. MPC-IR enables backend-independent optimizations in a close analogy to machine-independent optimizations in classical compilers. To demonstrate our approach, we focus on a specific backend-independent optimization, SIMD-vectorization: We devise a novel classical-compiler-inspired automatic SIMD vectorization on MPC-IR. To demonstrate backend independence and quality of our optimization, we evaluate our approach with two mainstream backend frameworks that support multiple types of MPC protocols, namely MOTION and MP-SPDZ, and show significant improvements across the board.

  匹配依据：MPC: multi party computation

  </details>

- **Non-Interactive Secure Computation of Inner-Product from LPN and LWE**
  2023-01-22 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-3-031-22963-3_16) · [IACR ePrint](https://eprint.iacr.org/2023/072)
  Geoffroy Couteau, Maryam Zarezadeh

  <details><summary>摘要 / Abstract</summary>

  We put forth a new cryptographic primitive for securely computing inner-products in a scalable, non-interactive fashion: any party can broadcast a public (computationally hiding) encoding of its input, and store a secret state. Given their secret state and the other party&#x27;s public encoding, any pair of parties can non-interactively compute additive shares of the inner-product between the encoded vectors. We give constructions of this primitive from a common template, which can be instantiated under either the LPN (with non-negligible correctness error) or the LWE (with negligible correctness error) assumptions. Our construction uses a novel twist on the standard non-interactive key exchange based on the Alekhnovich cryptosystem, which upgrades it to a non-interactive inner product protocol almost for free. In addition to being non-interactive, our constructions have linear communication (with constants smaller than all known alternatives) and small computation: using LPN or LWE with quasi-cyclic codes, we estimate that encoding a length-$2^{20}$ vector over a 32-bit field takes less that 2s on a standard laptop; decoding amounts to a single cheap inner-product. We show how to remove the non-negligible error in our LPN instantiation using a one-time, logarithmic-communication preprocessing. Eventually, we show to to upgrade its security to the malicious model using new sublinear-communication zero-knowledge proofs for low-noise LPN samples, which might be of independent interest.

  匹配依据：MPC: secure computation

  </details>

- **Verifiable Homomorphic Secret Sharing for Low Degree Polynomials.**
  2023 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2022.3194321)
  Liang Feng Zhang, Xin Chen, Jing Liu

- **Trifecta: Faster High-Throughput Three-Party Computation over WAN Using Multi-Fan-In Logic Gates.**
  2023 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2023-0107)
  Sina Faraji, Florian Kerschbaum

- **Threshold Linear Secret Sharing to the Rescue of MPC-in-the-Head**
  2023 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-981-99-8721-4_14) · [IACR ePrint](https://eprint.iacr.org/2022/1407)
  Matthieu Rivain, Thibauld Feneuil

  <details><summary>摘要 / Abstract</summary>

  The MPC-in-the-Head paradigm is a popular framework to build zero-knowledge proof systems using techniques from secure multi-party computation (MPC). While this paradigm is not restricted to a particular secret sharing scheme, all the efficient instantiations for small circuits proposed so far rely on additive secret sharing. In this work, we show how applying a threshold linear secret sharing scheme (threshold LSSS) can be beneficial to the MPC-in-the-Head paradigm. For a general passively-secure MPC protocol model capturing most of the existing MPCitH schemes, we show that our approach improves the soundness of the underlying proof system from $1/N$ down to $1/\binom{N}{\ell}$, where $N$ is the number of parties and $\ell$ is the privacy threshold of the sharing scheme. While very general, our technique is limited to a number of parties $N \leq |\mathbb{F}|$, where $\mathbb{F}$ is the field underlying the statement, because of the MDS conjecture. Applying our approach with a low-threshold LSSS also boosts the performance of the proof system by making the MPC emulation cost independent of $N$ for both the prover and the verifier. The gain is particularly significant for the verification time which becomes logarithmic in $N$ (while the prover still has to generate and commit the $N$ input shares). We further generalize and improve our framework: we show how homomorphic commitments can get rid of the linear complexity of the prover, we generalize our result to any quasi-threshold LSSS, and we describe an efficient batching technique relying on Shamir&#x27;s secret sharing. We finally apply our techniques to specific use-cases. We first propose a variant of the recent SDitH signature scheme achieving new interesting trade-offs. In particular, for a signature size of 10 KB, we obtain a verification time lower than $0.5$ ms, which is competitive with SPHINCS+, while achieving much faster signing. We further apply our batching technique to two different contexts: batched SDitH proofs and batched proofs for general arithmetic circuits based on the Limbo proof system. In both cases, we obtain an amortized proof size lower than $1/10$ of the baseline scheme when batching a few dozen statements, while the amortized performances are also significantly improved.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Secure Multiparty Computation from Threshold Encryption Based on Class Groups**
  2023 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-38557-5_20) · [IACR ePrint](https://eprint.iacr.org/2022/1437)
  Lennart Braun, Ivan Damgård, Claudio Orlandi

  <details><summary>摘要 / Abstract</summary>

  We construct the first actively-secure threshold version of the cryptosystem based on class groups from the so-called CL~framework (Castagnos and Laguillaumie, 2015). We show how to use our threshold scheme to achieve general universally composable (UC) secure multiparty computation (MPC) with only transparent set-up, i.e., with no secret trapdoors involved. On the way to our goal, we design new zero-knowledge (ZK) protocols with constant communication complexity for proving multiplicative relations between encrypted values. This allows us to use the ZK proofs to achieve MPC with active security with only a constant factor overhead. Finally, we adapt our protocol for the so-called &quot;You-Only-Speak-Once&quot; (YOSO) setting, which is a very promising recent approach for performing MPC over a blockchain. This is possible because our key generation protocol is simpler and requires significantly less interaction compared to previous approaches: in particular, our new key generation protocol allows the adversary to bias the public key, but we show that this has no impact on the security of the resulting cryptosystem.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Secure Computation Meets Distributed Universal Optimality.**
  2023 · MPC · 含会议/期刊记录 · [FOCS](https://doi.org/10.1109/FOCS57990.2023.00144)
  Merav Parter

- **Round-Optimal Oblivious Transfer and MPC from Computational CSIDH**
  2023 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-31368-4_14) · [IACR ePrint](https://eprint.iacr.org/2022/1511)
  Daniel Masny, Pratyay Mukherjee, Saikrishna Badrinarayanan, Pratik Sarkar, Srinivasan Raghuraman, Sikhar Patranabis

  <details><summary>摘要 / Abstract</summary>

  We present the first round-optimal and plausibly quantum-safe oblivious transfer (OT) and multi-party computation (MPC) protocols from the computational CSIDH assumption - the weakest and most widely studied assumption in the CSIDH family of isogeny-based assumptions. We obtain the following results: - The first round-optimal maliciously secure OT and MPC protocols in the plain model that achieve (black-box) simulation-based security while relying on the computational CSIDH assumption. - The first round-optimal maliciously secure OT and MPC protocols that achieves Universal Composability (UC) security in the presence of a trusted setup (common reference string plus random oracle) while relying on the computational CSIDH assumption. Prior plausibly quantum-safe isogeny-based OT protocols (with/without setup assumptions) are either not round-optimal, or rely on potentially stronger assumptions. We also build a 3-round maliciously-secure OT extension protocol where each base OT protocol requires only 4 isogeny computations. In comparison, the most efficient isogeny-based OT extension protocol till date due to Lai et al. [Eurocrypt 2021] requires 12 isogeny computations and 4 rounds of communication, while relying on the same assumption as our construction, namely the reciprocal CSIDH assumption.

  匹配依据：MPC: multi party computation, oblivious transfer

  </details>

- **Reverse Firewalls for Oblivious Transfer Extension and Applications to Zero-Knowledge**
  2023 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-30545-0_9) · [IACR ePrint](https://eprint.iacr.org/2022/1535)
  Suvradip Chakraborty, Pratik Sarkar, Chaya Ganesh

  <details><summary>摘要 / Abstract</summary>

  In the setting of subversion, an adversary tampers with the machines of the honest parties thus leaking the honest parties&#x27; secrets through the protocol transcript. The work of Mironov and Stephens-Davidowitz (EUROCRYPT’15) introduced the idea of reverse firewalls (RF) to protect against tampering of honest parties&#x27; machines. All known constructions in the RF framework rely on the malleability of the underlying operations in order for the RF to rerandomize/sanitize the transcript. RFs are thus limited to protocols that offer some structure, and hence based on public-key operations. In this work, we initiate the study of $efficient$ Multiparty Computation (MPC) protocols in the presence of tampering. In this regard, - We construct the $first$ Oblivious Transfer (OT) extension protocol in the RF setting. We obtain $poly(\kappa)$ maliciously-secure OTs using $O(\kappa)$ public key operations and $O(1)$ inexpensive symmetric key operations, where $\kappa$ is the security parameter. - We construct the $first$ Zero-knowledge protocol in the RF setting where each multiplication gate can be proven using $O(1)$ symmetric key operations. We achieve this using our OT extension protocol and by extending the ZK protocol of Quicksilver (Yang, Sarkar, Weng and Wang, CCS&#x27;21) to the RF setting. - Along the way, we introduce new ideas for malleable interactive proofs that could be of independent interest. We define a notion of $full$ $malleability$ for Sigma protocols that unlike prior notions allow modifying the instance as well, in addition to the transcript. We construct new protocols that satisfy this notion, construct RFs for such protocols and use them in constructing our OT extension. The key idea of our work is to demonstrate that correlated randomness may be obtained in an RF-friendly way $without$ having to rerandomize the entire transcript. This enables us to avoid expensive public-key operations that grow with the circuit-size.

  匹配依据：MPC: multiparty computation, oblivious transfer

  </details>

- **Publicly Verifiable Homomorphic Secret Sharing for Polynomial Evaluation.**
  2023 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2023.3298258)
  Xin Chen, Liang Feng Zhang

- **Private Access Control for Function Secret Sharing**
  2023 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP46215.2023.10179295) · [IACR ePrint](https://eprint.iacr.org/2022/1707)
  Simon Beyzerov, Eli Yablon, Hyojae Park, Sacha Servan-Schreiber

  <details><summary>摘要 / Abstract</summary>

  Function Secret Sharing (FSS; Eurocrypt 2015) allows a dealer to share a function f with two or more evaluators. Given secret shares of a function f, the evaluators can locally compute secret shares of f(x) on an input x, without learning information about f. In this paper, we initiate the study of access control for FSS. Given the shares of f, the evaluators can ensure that the dealer is authorized to share the provided function. For a function family F and an access control list defined over the family, the evaluators receiving the shares of f ∈ F can efficiently check that the dealer knows the access key for f. This model enables new applications of FSS, such as: – anonymous authentication in a multi-party setting, – access control in private databases, and – authentication and spam prevention in anonymous communication systems. Our definitions and constructions abstract and improve the concrete efficiency of several re- cent systems that implement ad-hoc mechanisms for access control over FSS. The main building block behind our efficiency improvement is a discrete-logarithm zero-knowledge proof-of-knowledge over secret-shared elements, which may be of independent interest. We evaluate our constructions and show a 50–70× reduction in computational overhead com- pared to existing access control techniques used in anonymous communication. In other applications, such as private databases, the processing cost of introducing access control is only 1.5–3× when amortized over databases with 500,000 or more items.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy of federated QR decomposition using additive secure multiparty computation**
  2023 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2210.06163) · [TIFS](https://doi.org/10.1109/TIFS.2023.3301710)
  Anne Hartebrodt, Richard Röttger

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) is a privacy-aware data mining strategy keeping the private data on the owners&#x27; machine and thereby confidential. The clients compute local models and send them to an aggregator which computes a global model. In hybrid FL, the local parameters are additionally masked using secure aggregation, such that only the global aggregated statistics become available in clear text, not the client specific updates. Federated QR decomposition has not been studied extensively in the context of cross-silo federated learning. In this article, we investigate the suitability of three QR decomposition algorithms for cross-silo FL and suggest a privacy-aware QR decomposition scheme based on the Gram-Schmidt algorithm which does not blatantly leak raw data. We apply the algorithm to compute linear regression in a federated manner.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Practically Efficient Private Set Intersection from Trusted Hardware with Side-Channels.**
  2023 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-981-99-8730-6_9)
  Jeremias Mechler, Felix Dörre, Jörn Müller-Quade

- **On the Security of a Lattice-Based Multi-Stage Secret Sharing Scheme.**
  2023 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2022.3209011)
  Longjiang Qu, Debiao He, Jianqiao Xu, Zhichao Yang

- **On the Round Complexity of Fully Secure Solitary MPC with Honest Majority**
  2023 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-48618-0_5) · [IACR ePrint](https://eprint.iacr.org/2021/241)
  Saikrishna Badrinarayanan, Peihan Miao, Pratyay Mukherjee, Divya Ravi

  <details><summary>摘要 / Abstract</summary>

  We study the problem of secure multiparty computation for functionalities where only one party receives the output, to which we refer as solitary MPC. Recently, Halevi et al. (TCC 2019) studied fully secure (i.e., with guaranteed output delivery) solitary MPC and showed impossibility of such protocols for certain functionalities when there is no honest majority among the parties. In this work, we study fully secure solitary MPC in the honest majority setting and focus on its round complexity. We note that a broadcast channel or public key infrastructure (PKI) setup is necessary for an $n$-party protocol against malicious adversaries corrupting up to $t$ parties where $n/3 \leq t &lt; n/2$. Therefore, we study the following settings and ask the question: Can fully secure solitary MPC be achieved in fewer rounds than fully secure standard MPC in which all parties receive the output? - When there is a broadcast channel and no PKI: * We start with a negative answer to the above question. In particular, we show that the exact round complexity of fully secure solitary MPC is 3, which is the same as fully secure standard MPC. * We then study the minimal number of broadcast rounds needed in the design of round-optimal fully secure solitary MPC. We show that both the first and second rounds of broadcast are necessary when $2 \lceil n/5 \rceil \leq t &lt; n/2$, whereas pairwise-private channels suffice in the last round. Notably, this result also applies to fully secure standard MPC in which all parties receive the output. - When there is a PKI and no broadcast channel, nevertheless, we show more positive results: * We show an upper bound of 5 rounds for any honest majority. This is superior to the super-constant lower bound for fully secure standard MPC in the exact same setting. * We complement this by showing a lower bound of 4 rounds when $3\lceil n/7 \rceil \leq t &lt; n/2$. * For the special case of $t=1,n=3$, when the output receiving party does not have an input to the function, we show an upper bound of $2$ rounds, which is optimal. When the output receiving party has an input to the function, we show a lower bound of 3, which matches an upper bound from prior work. * For the special case of $t=2,n=5$, we show a lower bound of 3 rounds (an upper bound of 4 follows from prior work). All our results also assume the existence of a common reference string (CRS) and pairwise-private channels. Our upper bounds use a decentralized threshold fully homomorphic encryption (dTFHE) scheme (which can be built from the learning with errors (LWE) assumption) as the main building block.

  匹配依据：MPC: secure multiparty computation

  </details>

- **On the Power of an Honest Majority in Three-Party Computation Without Broadcast**
  2023 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-64378-2_22) · [Journal of Cryptology](https://doi.org/10.1007/S00145-023-09456-4) · [IACR ePrint](https://eprint.iacr.org/2020/1170)
  Ran Cohen, Bar Alon, Tom Suad, Eran Omri

  <details><summary>摘要 / Abstract</summary>

  Fully secure multiparty computation (MPC) allows a set of parties to compute some function of their inputs, while guaranteeing correctness, privacy, fairness, and output delivery. Understanding the necessary and sufficient assumptions that allow for fully secure MPC is an important goal. Cleve (STOC&#x27;86) showed that full security cannot be obtained in general without an honest majority. Conversely, by Rabin and Ben-Or (STOC&#x27;89), assuming a broadcast channel and an honest majority enables a fully secure computation of any function. Our goal is to characterize the set of functionalities that can be computed with full security, assuming an honest majority, but no broadcast. This question was fully answered by Cohen et al. (TCC&#x27;16) -- for the restricted class of symmetric functionalities (where all parties receive the same output). Instructively, their results crucially rely on agreement and do not carry over to general asymmetric functionalities. In this work, we focus on the case of three-party asymmetric functionalities, providing a variety of necessary and sufficient conditions to enable fully secure computation. An interesting use-case of our results is server-aided computation, where an untrusted server helps two parties to carry out their computation. We show that without a broadcast assumption, the resource of an external non-colluding server provides no additional power. Namely, a functionality can be computed with the help of the server if and only if it can be computed without it. For fair coin tossing, we further show that the optimal bias for three-party (server-aided) $r$-round protocol remains $\Theta(1/r)$ (as in the two-party setting).

  匹配依据：MPC: secure computation, secure multiparty computation, three party computation

  </details>

- **On the Communication Efficiency of Statistically-Secure Asynchronous MPC with Optimal Resilience**
  2023 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-023-09451-9) · [IACR ePrint](https://eprint.iacr.org/2022/913)
  Ashish Choudhury, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) is a fundamental problem in secure distributed computing. An MPC protocol allows a set of $n$ mutually distrusting parties with private inputs to securely compute any publicly-known function of their inputs, by keeping their respective inputs as private as possible. While several works in the past have addressed the problem of designing communication-efficient MPC protocols in the synchronous communication setting, not much attention has been paid to the design of efficient MPC protocols in the asynchronous communication setting. In this work, we focus on the design of efficient asynchronous MPC (AMPC) protocol with statistical security, tolerating a computationally unbounded adversary, capable of corrupting up to $t$ parties out of the $n$ parties. The seminal work of Ben-Or, Kelmer and Rabin (PODC 1994) and later Abraham, Dolev and Stern (PODC 2020) showed that the optimal resilience for statistically-secure AMPC is $t &lt; n/3$. Unfortunately, the communication complexity of the protocol presented by Ben-Or et al is significantly high, where the communication complexity per multiplication is $\Omega(n^{13} \kappa^2 \log n)$ bits (where $\kappa$ is the statistical-security parameter). To the best of our knowledge, no work has addressed the problem of improving the communication complexity of the protocol of Ben-Or at al. In this work, our main contributions are the following. -- We present a new statistically-secure AMPC protocol with the optimal resilience $t &lt; n/3$ and where the communication complexity is ${\mathcal O}(n^4 \kappa)$ bits per multiplication. Apart from improving upon the communication complexity of the protocol of Ben-Or et al, our protocol is relatively simpler and based on very few sub-protocols, unlike the protocol of Ben-Or et al which involves several layers of subprotocols. A central component of our AMPC protocol is a new and simple protocol for verifiable asynchronous complete secret-sharing (ACSS), which is of independent interest. -- As a side result, we give the security proof for our AMPC protocol in the standard universal composability (UC) framework of Canetti (FOCS 2001, JACM 2020), which is now the defacto standard for proving the security of cryptographic protocols. This is unlike the protocol of Ben-Or et al, which was missing the formal security proofs.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **On Secure Computation of Solitary Output Functionalities With and Without Broadcast**
  2023 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-48618-0_4) · [IACR ePrint](https://eprint.iacr.org/2022/934)
  Bar Alon, Eran Omri

  <details><summary>摘要 / Abstract</summary>

  Solitary output secure computation models scenarios, where a single entity wishes to compute a function over an input that is distributed among several mutually distrusting parties. The computation should guarantee some security properties, such as correctness, privacy, and guaranteed output delivery. Full security captures all these properties together. This setting is becoming very important, as it is relevant to many real-world scenarios, such as service providers wishing to learn some statistics on the private data of their users. In this paper, we study full security for solitary output three-party functionalities in the point-to-point model (without broadcast) assuming at most a single party is corrupted. We give a characterization of the set of three-party Boolean functionalities and functionalities with up to three possible outputs (over a polynomial-size domain) that are computable with full security in the point-to-point model against a single corrupted party. We also characterize the set of three-party functionalities (over a polynomial-size domain) where the output receiving party has no input. Using this characterization, we identify the set of parameters that allow certain functionalities related to private set intersection to be securely computable in this model. Our main technical contribution is a reinterpretation of the hexagon argument due to Fischer et al. [Distributed Computing &#x27;86]. While the original argument relies on the agreement property (i.e., all parties output the same value) to construct an attack, we extend the argument to the solitary output setting, where there is no agreement. Furthermore, using our techniques, we were also able to advance our understanding of the set of solitary output three-party functionalities that can be computed with full security, assuming broadcast but where two parties may be corrupted. Specifically, we extend the set of such functionalities that were known to be computable, due to Halevi et al. [TCC &#x27;19].

  匹配依据：MPC: private set intersection, secure computation

  </details>

- **Network-Agnostic Security Comes (Almost) for Free in DKG and MPC**
  2023 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-38557-5_3) · [IACR ePrint](https://eprint.iacr.org/2022/1369)
  Julian Loss, Chen-Da Liu-Zhang, Renas Bacho, Daniel Collins

  <details><summary>摘要 / Abstract</summary>

  Distributed key generation (DKG) protocols are an essential building block for threshold cryptosystems. Many DKG protocols tolerate up to $t_s&lt;n/2$ corruptions assuming a well-behaved synchronous network, but become insecure as soon as the network delay becomes unstable. On the other hand, solutions in the asynchronous model operate under arbitrary network conditions, but only tolerate $t_a&lt;n/3$ corruptions, even when the network is well-behaved. In this work, we ask whether one can design a protocol that achieves security guarantees in either scenario. We show a complete characterization of network-agnostic DKG protocols, showing that the tight bound is $t_a+2t_s &lt;n$. As a second contribution, we provide an optimized version of the network-agnostic MPC protocol by Blum, Liu-Zhang and Loss [CRYPTO&#x27;20] which improves over the communication complexity of their protocol by a linear factor. Moreover, using our DKG protocol, we can instantiate our MPC protocol in the plain PKI model, i.e., without the need to assume an expensive trusted setup. Our protocols incur the same communication complexity as state-of-the-art DKG and MPC protocols with optimal resilience in their respective purely synchronous and asynchronous settings, thereby showing that network-agnostic security comes (almost) for free.

  匹配依据：MPC: mpc (context)

  </details>

- **Multi-Party Replicated Secret Sharing over a Ring with Applications to Privacy-Preserving Machine Learning**
  2023 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2023-0035) · [IACR ePrint](https://eprint.iacr.org/2020/1577)
  Alessandro N. Baccarini, Chen Yuan, Marina Blanton, Alessandro Baccarini

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation has seen significant performance advances and increasing use in recent years. Techniques based on secret sharing offer attractive performance and are a popular choice for privacy-preserving machine learning applications. Traditional techniques operate over a field, while designing equivalent techniques for a ring $\mathbb{Z}_{2^k}$ can boost performance. In this work, we develop a suite of multi-party protocols for a ring in the honest majority setting starting from elementary operations to more complex with the goal of supporting general-purpose computation. We demonstrate that our techniques are substantially faster than their field-based equivalents when instantiated with a different number of parties and perform on par with or better than state-of-the-art techniques with designs customized for a fixed number of parties. We evaluate our techniques on machine learning applications and show that they offer attractive performance.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Matrix-Based Secret Sharing for Reversible Data Hiding in Encrypted Images.**
  2023 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2022.3218570)
  Xinpeng Zhang, Yongyong Chen, Zhongyun Hua, Shuang Yi, Yanxiang Wang, Yifeng Zheng, Xingyu Liu

- **Manticore: A Framework for Efficient Multiparty Computation Supporting Real Number and Boolean Arithmetic.**
  2023 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-023-09464-4)
  Mariya Georgieva, Iraklis Leontiadis, Dimitar Jetchev, Abson Sae-Tang, Marius Vuille, Kevin Deforth, Mohsen Mohammadi, Jonathan Katz, Nicolas Gama, Sergiu Carpov

- **Maliciously Secure and Efficient Large-Scale Genome-Wide Association Study With Multi-Party Computation.**
  2023 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2022.3152498)
  Jianfeng Ma, Zhiquan Liu, Anjia Yang, Jia-Nan Liu, Yaxi Yang, Caiqin Dong, Jian Weng

- **Low Communication Secure Computation From Semi-Trusted Hardware.**
  2023 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2023.3282134)
  Kui Ren, Bingsheng Zhang, Yibiao Lu

- **Longshot: Indexing Growing Databases using MPC and Differential Privacy.**
  2023 · MPC · 含会议/期刊记录 · [PVLDB](https://doi.org/10.14778/3594512.3594529)
  Johes Bater, Kartik Nayak, Yanping Zhang, Ashwin Machanavajjhala

- **Linear Private Set Union from Multi-Query Reverse Private Membership Test**
  2023 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/zhang-cong) · [IACR ePrint](https://eprint.iacr.org/2022/358)
  Cong Zhang, Weiran Liu, Min Zhang, Dongdai Lin, Yu Chen

  <details><summary>摘要 / Abstract</summary>

  Private set union (PSU) protocol enables two parties, each holding a set, to compute the union of their sets without revealing anything else to either party. So far, there are two known approaches for constructing PSU protocols. The first mainly depends on additively homomorphic encryption (AHE), which is generally inefficient since it needs to perform a non-constant number of homomorphic computations on each item. The second is mainly based on oblivious transfer and symmetric-key operations, which is recently proposed by Kolesnikov et al. (ASIACRYPT 2019). It features good practical performance, which is several orders of magnitude faster than the first one. However, neither of these two approaches is optimal in the sense that their computation and communication complexity are not both $O(n)$, where $n$ is the size of the set. Therefore, the problem of constructing the optimal PSU protocol remains open. In this work, we resolve this open problem by proposing a generic framework of PSU from oblivious transfer and a newly introduced protocol called multi-query reverse private membership test (mq-RPMT). We present two generic constructions of mq-RPMT. The first is based on symmetric-key encryption and general 2PC techniques. The second is based on re-randomizable public-key encryption. Both constructions lead to PSU with linear computation and communication complexity. We implement our two PSU protocols and compare them with the state-of-the-art PSU. Experiments show that our PKE-based protocol has the lowest communication of all schemes, which is $3.7-14.8\times$ lower depending on set size. The running time of our PSU scheme is $1.2-12\times$ faster than that of state-of-the-art depending on network environments.

  匹配依据：MPC: oblivious transfer, private set union

  </details>

- **Linear Communication in Malicious Majority MPC**
  2023 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3576915.3623162) · [IACR ePrint](https://eprint.iacr.org/2022/781)
  Daniel McVicker, Phi Hung Le, S. Dov Gordon

  <details><summary>摘要 / Abstract</summary>

  The SPDZ multiparty computation protocol allows $n$ parties to securely compute arithmetic circuits over a finite field, while tolerating up to $n − 1$ active corruptions. A line of work building upon SPDZ have made considerable improvements to the protocol’s performance, typically focusing on concrete efficiency. However, the communication complexity of each of these protocols is $\Omega(n^2 |C|)$. In this paper, we present a protocol that achieves $O(n|C|)$ communication. Our construction is very similar to those in the SPDZ family of protocols, but for one modular sub-routine for computing a verified sum. There are a handful of times in the SPDZ protocols in which the $n$ parties wish to sum $n$ public values. Rather than requiring each party to broadcast their input to all other parties, clearly it is cheaper to use some designated &quot;dealer&quot; to compute and broadcast the sum. In prior work, it was assumed that the cost of verifying the correctness of these sums is $O(n^2 )$, erasing the benefit of using a dealer. We show how to amortize this cost over the computation of multiple sums, resulting in linear communication complexity whenever the circuit size is $|C| &gt; n$.

  匹配依据：MPC: multiparty computation

  </details>

- **Improved Protocols for Distributed Secret Sharing.**
  2023 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2022.3213790)
  Roberto De Prisco, Francesco Palmieri, Alfredo De Santis

- **Improved Private Set Intersection for Sets with Small Entries**
  2023 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-31371-4_7) · [IACR ePrint](https://eprint.iacr.org/2022/334)
  Dung Bui, Geoffroy Couteau

  <details><summary>摘要 / Abstract</summary>

  We introduce new protocols for private set intersection (PSI), building upon recent constructions of pseudorandom correlation generators, such as vector-OLE and ring-OLE. Our new constructions improve over the state of the art on several aspects, and perform especially well in the setting where the parties have databases with small entries. We obtain three main contributions: 1. We introduce a new semi-honest PSI protocol that combines subfield vector-OLE with hash-based PSI. Our protocol is the first PSI protocol to achieve communication complexity independent of the computational security parameter κ, and has communication lower than all previous known protocols for input sizes ℓ below 70 bits. 2. We enhance the security of our protocol to the malicious setting, using two different approaches. In particular, we show that applying the dual execution technique yields a malicious PSI whose communication remains independent of κ, and improves over all known PSI protocols for small values of ℓ. 3. As most previous protocols, our above protocols are in the random oracle model. We introduce a third protocol which relies on subfield ring-OLE to achieve maliciously secure PSI in the standard model, under the ring-LPN assumption. Our protocol enjoys extremely low communication, reasonable computation, and standard model security. Furthermore, it is batchable: the message of a client can be reused to compute the intersection of their set with that of multiple servers, yielding further reduction in the overall amortized communication.

  匹配依据：MPC: private set intersection

  </details>

- **High-Throughput Secure Three-Party Computation with an Honest Majority.**
  2023 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-023-09461-7)
  Or Weinstein, Ariel Nof, Jun Furukawa, Yehuda Lindell

- **Garbled-Circuits from an SCA Perspective: Free XOR can be Quite Expensive. . .**
  2023 · MPC · 含会议/期刊记录 · [CHES](https://doi.org/10.46586/TCHES.V2023.I2.54-79) · [IACR ePrint](https://eprint.iacr.org/2022/901)
  Itamar Levi, Carmit Hazay

  <details><summary>摘要 / Abstract</summary>

  Garbling schemes, invented in the 80&#x27;s by Yao (FOCS&#x27;86), have been a versatile and fundamental tool in modern cryptography. A prominent application of garbled circuits is constant round secure two-party computation, led to a long line of study of this object, where one of the most influential optimizations is Free-XOR (Kolesnikov and Schneider ICALP&#x27;08), introducing a global offset $\Delta$ for all garbled wire values where XOR gates are computed locally without garbling them. To date, garbling sachems were not studied per their side-channel attacks (SCA) security characteristics, even though SCA pose a significant security threat to cryptographic devices. In this research we demonstrate that adversaries utilizing advanced SCA tools such as horizontal attacks, mixed with advanced hypothesis building and standard (vertical) SCA tools, can jeopardize garbling implementations. Our main observation is that garbling schemes utilizing a global secret $\Delta$ open a door to quite trivial side-channel attacks. We model our side-channel attacks on the garbler&#x27;s device and discuss the asymmetric setting where various computations are not performed on the evaluator side. This enables dangerous leakage extraction on the garbler and renders our attack impossible on the evaluator&#x27;s side. Theoretically, we first demonstrate on a simulated environment, that such attacks are quite devastating. Concretely, our attack is capable of extracting $\Delta$ when the circuit embeds only $8$ input non-linear gates with fifth/first-order attack Success-Rates of $0.65$/$0.7$. With as little as $3$ such gates, our attack reduces the first-order Guessing Entropy of $\Delta$ from $128$ to $\sim48$-bits. We further demonstrate our attack via an implementation and measurements data over an STM 32-bit processor software implementing circuit garbling, and discuss their limitations and mitigation tactics on logical, protocol and implementation layers.

  匹配依据：MPC: garbled circuits, garbling schemes, secure two party computation

  </details>

- **Funshade: Function Secret Sharing for Two-Party Secure Thresholded Distance Evaluation**
  2023 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2023-0096) · [IACR ePrint](https://eprint.iacr.org/2022/1688)
  Alberto Ibarrondo, Melek Önen, Hervé Chabanne

  <details><summary>摘要 / Abstract</summary>

  We propose a novel privacy-preserving, two-party computation of various distance metrics (e.g., Hamming distance, Scalar Product) followed by a comparison with a fixed threshold, which is known as one of the most useful and popular building blocks for many different applications including machine learning, biometric matching, etc. Our solution builds upon recent advances in function secret sharing and makes use of an optimized version of arithmetic secret sharing. Thanks to this combination, our new solution named Funshade is the first to require only one round of communication and two ring elements of communication in the online phase, outperforming all prior state-of-the-art schemes while relying on lightweight cryptographic primitives. Lastly, we implement our solution from scratch in portable C and expose it in Python, testifying its high performance by running secure biometric identification against a database of 1 million records in ∼10 seconds with full correctness and 32-bit precision, without parallelization.

  匹配依据：MPC: secret sharing, two party computation

  </details>

- **Faster Secure Comparisons with Offline Phase for Efficient Private Set Intersection**
  2023 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2209.13913) · [NDSS](https://www.ndss-symposium.org/ndss-paper/faster-secure-comparisons-with-offline-phase-for-efficient-private-set-intersection/)
  Erik-Oliver Blass, Rasoul Akhavan Mahdavi, Florian Kerschbaum

  <details><summary>摘要 / Abstract</summary>

  In a Private section intersection (PSI) protocol, Alice and Bob compute the intersection of their respective sets without disclosing any element not in the intersection. PSI protocols have been extensively studied in the literature and are deployed in industry. With state-of-the-art protocols achieving optimal asymptotic complexity, performance improvements are rare and can only improve complexity constants. In this paper, we present a new private, extremely efficient comparison protocol that leads to a PSI protocol with low constants. A useful property of our comparison protocol is that it can be divided into an online and an offline phase. All expensive cryptographic operations are performed during the offline phase, and the online phase performs only four fast field operations per comparison. This leads to an incredibly fast online phase, and our evaluation shows that it outperforms related work, including KKRT (CCS 16), VOLE-PSI (EuroCrypt 21), and OKVS (Crypto 21). We also evaluate standard approaches to implement the offline phase using different trust assumptions: cryptographic, hardware, and a third party (dealer model).

  匹配依据：MPC: private set intersection

  </details>

- **Fast Unbalanced Private Set Union from Fully Homomorphic Encryption**
  2023 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3576915.3623064) · [IACR ePrint](https://eprint.iacr.org/2022/653)
  Cong Zhang, Binbin Tu, Qi Liu, Yu Chen

  <details><summary>摘要 / Abstract</summary>

  Private set union (PSU) allows two parties to compute the union of their sets without revealing anything else. It has been widely used in various applications. While several computationally efficient PSU protocols have been developed for the balanced case, they have a potential limitation in their communication complexity, which grows (super)-linearly with the size of the larger set. This poses a challenge when performing PSU in the unbalanced setting, where one party is a constrained device holding a small set, and another is a service provider holding a large set. In this work, we propose a generic construction of unbalanced PSU from leveled fully homomorphic encryption and a newly introduced protocol called permuted matrix private equality test. By instantiating the generic construction, we obtain two unbalanced PSU protocols whose communication complexity is linear in the size of the smaller set, and logarithmic in the larger set. We implement our protocols. Experiments demonstrate that our protocols outperform all previous protocols in the unbalanced setting. The larger difference between the sizes of two sets, the better our protocols perform. For input sets of sizes $2^{10}$ and $2^{20}$ with items of length $128$ bits, our PSU requires only $2.767$ MB of communication. Compared with the state-of-the-art PSU proposed by Zhang et al. (USENIX Security 2023), there are $37 \times$ shrink in communication and roughly $10 - 35 \times$ speedup in the running time depending on the network environments.

  匹配依据：MPC: private set union

  </details>

- **Fast Large-Scale Honest-Majority MPC for Malicious Adversaries.**
  2023 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-023-09453-7)
  Ariel Nof, Yehuda Lindell, Koki Hamada, Ryo Kikuchi, Koji Chida, Dai Ikarashi, Daniel Genkin

- **Endemic Oblivious Transfer via Random Oracles, Revisited**
  2023 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-30545-0_11) · [IACR ePrint](https://eprint.iacr.org/2022/1525)
  Kui Ren, Hong-Sheng Zhou, Zhelei Zhou, Bingsheng Zhang

  <details><summary>摘要 / Abstract</summary>

  The notion of Endemic Oblivious Transfer (EOT) was introduced by Masny and Rindal (CCS&#x27;19). EOT offers a weaker security guarantee than the conventional random OT; namely, the malicious parties can fix their outputs arbitrarily. The authors presented a 1-round UC-secure EOT protocol under a tailor-made and non-standard assumption, Choose-and-Open DDH, in the RO model. In this work, we systematically study EOT in the UC/GUC framework. We present a new 1-round UC-secure EOT construction in the RO model under the DDH assumption. Under the GUC framework, we propose the first 1-round EOT construction under the CDH assumption in the Global Restricted Observable RO (GroRO) model proposed by Canetti et al. (CCS&#x27;14). We also provide an impossibility result, showing there exist no 1-round GUC-secure EOT protocols in the Global Restricted Programmable RO (GrpRO) model proposed by Camenisch et al. (Eurocrypt&#x27;18). Subsequently, we provide the first round-optimal (2-round) EOT protocol with adaptive security under the DDH assumption in the GrpRO model. Finally, we investigate the relations between EOT and other cryptographic primitives. As side products, we present the first 2-round GUC-secure commitment in the GroRO model as well as a separation between the GroRO and the GrpRO models, which may be of independent interest.

  匹配依据：MPC: oblivious transfer

  </details>

- **Efficient decision tree training with new data structure for secure multi-party computation**
  2023 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2112.12906) · [PoPETs](https://doi.org/10.56553/POPETS-2023-0021)
  Koji Chida, Ryo Kikuchi, Koki Hamada, Dai Ikarashi

  <details><summary>摘要 / Abstract</summary>

  We propose a secure multi-party computation (MPC) protocol that constructs a secret-shared decision tree for a given secret-shared dataset. The previous MPC-based decision tree training protocol (Abspoel et al. 2021) requires $O(2^hmn\log n)$ comparisons, being exponential in the tree height $h$ and with $n$ and $m$ being the number of rows and that of attributes in the dataset, respectively. The cause of the exponential number of comparisons in $h$ is that the decision tree training algorithm is based on the divide-and-conquer paradigm, where dummy rows are added after each split in order to hide the number of rows in the dataset. We resolve this issue via secure data structure that enables us to compute an aggregate value for every group while hiding the grouping information. By using this data structure, we can train a decision tree without adding dummy rows while hiding the size of the intermediate data. We specifically describes a decision tree training protocol that requires only $O(hmn\log n)$ comparisons when the input attributes are continuous and the output attribute is binary. Note that the order is now \emph{linear} in the tree height $h$. To demonstrate the practicality of our protocol, we implement it in an MPC framework based on a three-party secret sharing scheme. Our implementation results show that our protocol trains a decision tree with a height of 5 in 33 seconds for a dataset of 100,000 rows and 10 attributes.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Efficient Unbalanced Private Set Intersection Cardinality and User-friendly Privacy-preserving Contact Tracing.**
  2023 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/wu-mingli)
  Tsz Hon Yuen, Mingli Wu

- **Efficient Noise Generation Protocols for Differentially Private Multiparty Computation**
  2023 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2022.3227568) · [IACR ePrint](https://eprint.iacr.org/2022/1391)
  Noboru Kunihiro, Reo Eriguchi, Atsunori Ichikawa, Koji Nuida

  <details><summary>摘要 / Abstract</summary>

  To bound information leakage in outputs of protocols, it is important to construct secure multiparty computation protocols which output differentially private values perturbed by the addition of noise. However, previous noise generation protocols have round and communication complexity growing with differential privacy budgets, or require parties to locally generate non-uniform noise, which makes it difficult to guarantee differential privacy against active adversaries. We propose three kinds of protocols for generating noise drawn from certain distributions providing differential privacy. The two of them generate noise from finite-range variants of the discrete Laplace distribution. For $(\epsilon,\delta)$-differential privacy, they only need constant numbers of rounds independent of $\epsilon,\delta$ while the previous protocol needs the number of rounds depending on $\delta$. The two protocols are incomparable as they make a trade-off between round and communication complexity. Our third protocol non-interactively generates shares of noise from the binomial distribution by predistributing keys for a pseudorandom function. It achieves communication complexity independent of $\epsilon$ or $\delta$ for the computational analogue of $(\epsilon,\delta)$-differential privacy while the previous protocols require communication complexity depending on $\epsilon$. We also prove that our protocols can be extended so that they provide differential privacy in the active setting.

  匹配依据：MPC: multiparty computation, secure multiparty computation

  </details>

- **Efficient Multiparty Probabilistic Threshold Private Set Intersection.**
  2023 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3576915.3623158)
  En Zhang, Leiyong Qin, Feng-Hao Liu

- **Distance-Aware Private Set Intersection**
  2023 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2112.14737) · [USENIX Security](https://www.usenix.org/conference/usenixsecurity23/presentation/chakraborti-intersection)
  Anrin Chakraborti, Giulia Fanti, Michael K. Reiter

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) allows two mutually untrusting parties to compute an intersection of their sets, without revealing information about items that are not in the intersection. This work introduces a PSI variant called distance-aware PSI (DA-PSI) for sets whose elements lie in a metric space. DA-PSI returns pairs of items that are within a specified distance threshold of each other. This paper puts forward DA-PSI constructions for two metric spaces: (i) Minkowski distance of order 1 over the set of integers (i.e., for integers $a$ and $b$, their distance is $|a-b|$); and (ii) Hamming distance over the set of binary strings of length $\ell$. In the Minkowski DA-PSI protocol, the communication complexity scales logarithmically in the distance threshold and linearly in the set size. In the Hamming DA-PSI protocol, the communication volume scales quadratically in the distance threshold and is independent of the dimensionality of string length $\ell$. Experimental results with real applications confirm that DA-PSI provides more effective matching at lower cost than naive solutions.

  匹配依据：MPC: private set intersection

  </details>

- **Cryptography with Weights: MPC, Encryption and Signatures**
  2023 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-38557-5_10) · [IACR ePrint](https://eprint.iacr.org/2022/1632)
  Rohit Sinha, Pratyay Mukherjee, Mingyuan Wang, Sanjam Garg, Abhishek Jain, Yinuo Zhang

  <details><summary>摘要 / Abstract</summary>

  The security of several cryptosystems rests on the trust assumption that a certain fraction of the parties are honest. This trust assumption has enabled a diverse of cryptographic applications such as secure multiparty computation, threshold encryption, and threshold signatures. However, current and emerging practical use cases suggest that this paradigm of one-person-one-vote is outdated. In this work, we consider {\em weighted} cryptosystems where every party is assigned a certain weight and the trust assumption is that a certain fraction of the total weight is honest. This setting can be translated to the standard setting (where each party has a unit weight) via virtualization. However, this method is quite expensive, incurring a multiplicative overhead in the weight. We present new weighted cryptosystems with significantly better efficiency. Specifically, our proposed schemes incur only an {\em additive} overhead in weights. \begin{itemize} \item We first present a weighted ramp secret-sharing scheme where the size of the secret share is as short as $O(w)$ (where $w$ corresponds to the weight). In comparison, Shamir&#x27;s secret sharing with virtualization requires secret shares of size $w\cdot\lambda$, where $\lambda=\log |\mathbb{F}|$ is the security parameter. \item Next, we use our weighted secret-sharing scheme to construct weighted versions of (semi-honest) secure multiparty computation (MPC), threshold encryption, and threshold signatures. All these schemes inherit the efficiency of our secret sharing scheme and incur only an additive overhead in the weights. \end{itemize} Our weighted secret-sharing scheme is based on the Chinese remainder theorem. Interestingly, this secret-sharing scheme is {\em non-linear} and only achieves statistical privacy. These distinct features introduce several technical hurdles in applications to MPC and threshold cryptosystems. We resolve these challenges by developing several new ideas.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Circuit-Free General-Purpose Multi-Party Computation via Co-Utile Unlinkable Outsourcing**
  2023 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2112.15001) · [TDSC](https://doi.org/10.1109/TDSC.2021.3138826)
  Jesús A. Manjón, Josep Domingo-Ferrer, Jesús Manjón

  <details><summary>摘要 / Abstract</summary>

  Multiparty computation (MPC) consists in several parties engaging in joint computation in such a way that each party&#x27;s input and output remain private to that party. Whereas MPC protocols for specific computations have existed since the 1980s, only recently general-purpose compilers have been developed to allow MPC on arbitrary functions. Yet, using today&#x27;s MPC compilers requires substantial programming effort and skill on the user&#x27;s side, among other things because nearly all compilers translate the code of the computation into a Boolean or arithmetic circuit. In particular, the circuit representation requires unrolling loops and recursive calls, which forces programmers to (often manually) define loop bounds and hardly use recursion. We present an approach allowing MPC on an arbitrary computation expressed as ordinary code with all functionalities that does not need to be translated into a circuit. Our notion of input and output privacy is predicated on unlinkability. Our method leverages co-utile computation outsourcing using anonymous channels via decentralized reputation, makes a minimalistic use of cryptography and does not require participants to be honest-but-curious: it works as long as participants are rational (self-interested), which may include rationally malicious peers (who become attackers if this is advantageous to them). We present example applications, including e-voting. Our empirical work shows that reputation captures well the behavior of peers and ensures that parties with high reputation obtain correct results.

  匹配依据：MPC: multi party computation, multiparty computation

  </details>

- **Bingo: Adaptivity and Asynchrony in Verifiable Secret Sharing and Distributed Key Generation**
  2023 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-031-38557-5_2) · [IACR ePrint](https://eprint.iacr.org/2022/1759)
  Philipp Jovanovic, Mary Maller, Ittai Abraham, Gilad Stern, Sarah Meiklejohn

  <details><summary>摘要 / Abstract</summary>

  We present Bingo, an adaptively secure and optimally resilient packed asynchronous verifiable secret sharing (PAVSS) protocol that allows a dealer to share $f+1$ secrets with a total communication complexity of $O(\lambda n^2)$ words, where $\lambda$ is the security parameter and $n$ is the number of parties. Using Bingo, we obtain an adaptively secure validated asynchronous Byzantine agreement (VABA) protocol that uses $O(\lambda n^3)$ expected words and constant expected time, which we in turn use to construct an adaptively secure high-threshold asynchronous distributed key generation (ADKG) protocol that uses $O(\lambda n^3)$ expected words and constant expected time. To the best of our knowledge, our ADKG is the first to allow for an adaptive adversary while matching the asymptotic complexity of the best known static ADKGs.

  匹配依据：MPC: secret sharing

  </details>

- **Adaptively Secure MPC with Sublinear Communication Complexity.**
  2023 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-023-09446-6)
  Ran Cohen, Daniel Wichs, Abhi Shelat

- **Adaptive Distributional Security for Garbling Schemes with 𝒪(\|x\|) Online Complexity.**
  2023 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-981-99-8721-4_5)
  Estuardo Alpirez Bock, Sabine Oechsner, Kirthivaasan Puniamurthy, Pihla Karanko, Christopher Brzuska

- **Actively Secure Garbled Circuits with Constant Communication Overhead in the Plain Model.**
  2023 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-023-09465-3)
  Yuval Ishai, Carmit Hazay, Muthuramakrishnan Venkitasubramaniam

- **A New Framework for Quantum Oblivious Transfer**
  2023 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2209.04520) · [EUROCRYPT](https://doi.org/10.1007/978-3-031-30545-0_13) · [IACR ePrint](https://eprint.iacr.org/2022/1191)
  James Bartusek, Amit Agarwal, Nishant Kumar, Dakshita Khurana

  <details><summary>摘要 / Abstract</summary>

  We present a new template for building oblivious transfer from quantum information that we call the &quot;fixed basis&quot; framework. Our framework departs from prior work (eg., Crepeau and Kilian, FOCS &#x27;88) by fixing the correct choice of measurement basis used by each player, except for some hidden trap qubits that are intentionally measured in a conjugate basis. We instantiate this template in the quantum random oracle model (QROM) to obtain simple protocols that implement, with security against malicious adversaries: 1. Non-interactive random-input bit OT in a model where parties share EPR pairs a priori. 2. Two-round random-input bit OT without setup, obtained by showing that the protocol above remains secure even if the (potentially malicious) OT receiver sets up the EPR pairs. 3. Three-round chosen-input string OT from BB84 states without entanglement or setup. This improves upon natural variations of the CK88 template that require at least five rounds. Along the way, we develop technical tools that may be of independent interest. We prove that natural functions like XOR enable seedless randomness extraction from certain quantum sources of entropy. We also use idealized (i.e. extractable and equivocal) bit commitments, which we obtain by proving security of simple and efficient constructions in the QROM.

  匹配依据：MPC: oblivious transfer

  </details>
