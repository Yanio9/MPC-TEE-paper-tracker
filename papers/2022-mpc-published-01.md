# 2022 · MPC · 含会议/期刊记录 · 第 1/1 页

[总目录](../PAPERS.md)

- **On Perfectly Secure Two-Party Computation for Symmetric Functionalities with Correlated Randomness**
  2022-11-07 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-22365-5_19) · [IACR ePrint](https://eprint.iacr.org/2022/1504)
  Bar Alon, Olga Nissenbaum, Anat Paskin-Cherniavsky, Eran Omri, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  A multiparty computation protocol is {\em perfectly secure} for some function $f$ if it perfectly emulates an ideal computation of $f$. Thus, perfect security is the strongest and most desirable notion of security, as it guarantees security in the face of any adversary and eliminates the dependency on any security parameter. Ben-Or et al. [STOC &#x27;88] and Chaum et al. [STOC &#x27;88] showed that any function can be computed with perfect security if strictly less than one-third of the parties can be corrupted. For two-party sender-receiver functionalities (where only one party receives an output), Ishai et al. [TCC &#x27;13] showed that any function can be computed with perfect security in the correlated randomness model. Unfortunately, they also showed that perfect security cannot be achieved in general for two-party functions that give outputs to both parties (even in the correlated randomness model). We study the feasibility of obtaining perfect security for deterministic symmetric two-party functionalities (i.e., where both parties obtain the same output) in the face of malicious adversaries. We explore both the plain model as well as the correlated randomness model. We provide positive results in the plain model, and negative results in the correlated randomness model. As a corollary, we obtain the following results. \begin{enumerate} \item We provide a characterization of symmetric functionalities with (up to) four possible outputs that can be computed with perfect security. The characterization is further refined when restricted to three possible outputs and to Boolean functions. All characterizations are the same for both the plain model and the correlated randomness model. \item We show that if a functionality contains an embedded XOR or an embedded AND, then it cannot be computed with perfect security (even in the correlated randomness model). \end{enumerate}

  匹配依据：MPC: multiparty computation, secure two party computation

  </details>

- **Oblivious-Transfer Complexity of Noisy Coin-Toss via Secure Zero Communication Reductions**
  2022-11-07 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-22368-6_4) · [IACR ePrint](https://eprint.iacr.org/2022/1539)
  Manoj Prabhakaran, Saumya Goyal, Varun Narayanan

  <details><summary>摘要 / Abstract</summary>

  In p-noisy coin-tossing, Alice and Bob obtain fair coins which are of opposite values with probability p. Its Oblivious-Transfer (OT) complexity refers to the least number of OTs required by a semi-honest perfectly secure 2-party protocol for this task. We show a tight bound of Θ(log 1/p) for the OT complexity of p-noisy coin-tossing. This is the first instance of a lower bound for OT complexity that is independent of the input/output length of the function. We obtain our result by providing a general connection between the OT complexity of randomized functions and the complexity of Secure Zero Communication Reductions (SZCR), as recently de- fined by Narayanan et al. (TCC 2020), and then showing a lower bound for the complexity of an SZCR from noisy coin-tossing to (a predicate corresponding to) OT.

  匹配依据：MPC: oblivious transfer

  </details>

- **TurboPack: Honest Majority MPC with Constant Online Communication**
  2022-10-04 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3548606.3560633) · [IACR ePrint](https://eprint.iacr.org/2022/1316)
  Daniel Escudero, Vipul Goyal, Antigoni Polychroniadou, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  We present a novel approach to honest majority secure multiparty computation in the preprocessing model with information theoretic security that achieves the best online communication complexity. The online phase of our protocol requires $12$ elements in total per multiplication gate with circuit-dependent preprocessing, or $20$ elements in total with circuit-independent preprocessing. Prior works achieved linear online communication complexity in $n$, the number of parties, with the best prior existing solution involving $1.5n$ elements per multiplication gate. Only one recent work (Goyal et al, CRYPTO&#x27;22) achieves constant online communication complexity, but the constants are large ($108$ elements for passive security, and twice that for active security). That said, our protocol offers a very efficient information theoretic online phase for any number of parties. The total end-to-end communication cost with the preprocessing phase is linear in $n$, i.e., $10n + 44$, which is larger than the $4n$ complexity of the state-of-the-art protocols. The gap is not significant when the online phase must be optimized as a priority and a reasonably large number of parties is involved. Unlike previous works based on packed secret-sharing to reduce communication complexity, we further reduce the communication by avoiding the use of complex and expensive network routing or permutations tools. Furthermore, we also allow for a maximal honest majority adversary, while most previous works require the set of honest parties to be strictly larger than a majority. Our protocol is simple and offers concrete efficiency. To illustrate this we present a full-fledged implementation together with experimental results that show improvements in online phase runtimes that go up to $5\times$ in certain settings (e.g. $45$ parties, LAN network, circuit of depth $10$ with $1$M gates).

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Round-Optimal Black-Box Secure Computation from Two-Round Malicious OT**
  2022-09-28 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-22365-5_16) · [IACR ePrint](https://eprint.iacr.org/2022/1288)
  Akshayaram Srinivasan, Yuval Ishai, Dakshita Khurana, Amit Sahai

  <details><summary>摘要 / Abstract</summary>

  We give round-optimal {\em black-box} constructions of two-party and multiparty protocols in the common random/reference string (CRS) model, with security against malicious adversaries, based on any two-round oblivious transfer (OT) protocol in the same model. Specifically, we obtain two types of results. \begin{enumerate} \item {\bf Two-party protocol.} We give a (two-round) {\it two-sided NISC} protocol that makes black-box use of two-round (malicious-secure) OT in the CRS model. In contrast to the standard setting of non-interactive secure computation (NISC), two-sided NISC allows communication from both parties in each round and delivers the output to both parties at the end of the protocol. Prior black-box constructions of two-sided NISC relied on idealized setup assumptions such as OT correlations, or were proven secure in the random oracle model. \item {\bf Multiparty protocol.} We give a three-round secure multiparty computation protocol for an arbitrary number of parties making black-box use of a two-round OT in the CRS model. The round optimality of this construction follows from a black-box impossibility proof of Applebaum et al. (ITCS 2020). Prior constructions either required the use of random oracles, or were based on two-round malicious-secure OT protocols that satisfied additional security properties. \end{enumerate}

  匹配依据：MPC: oblivious transfer, secure computation, secure multiparty computation

  </details>

- **Fully-Secure MPC with Minimal Trust**
  2022-09-20 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-22365-5_17) · [IACR ePrint](https://eprint.iacr.org/2022/1248)
  Divya Ravi, Sikhar Patranabis, Akshayaram Srinivasan, Yuval Ishai, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  The task of achieving full security (with guaranteed output delivery) in secure multiparty computation (MPC) is a long-studied problem. Known impossibility results (Cleve, STOC 86) rule out general solutions in the dishonest majority setting. In this work, we consider solutions that use an external trusted party (TP) to bypass the impossibility results, and study the minimal requirements needed from this trusted party. In particular, we restrict ourselves to the extreme setting where the size of the TP is independent of the size of the functionality to be computed (called “small” TP) and this TP is invoked only once during the protocol execution. We present several positive and negative results for fully-secure MPC in this setting. -- For a natural class of protocols, specifically, those with a universal output decoder, we show that the size of the TP must necessarily be exponential in the number of parties. This result holds irrespective of the computational assumptions used in the protocol. The class of protocols to which our lower bound applies is broad enough to capture prior results in the area, implying that the prior techniques necessitate the use of an exponential-sized TP. We additionally rule out the possibility of achieving information-theoretic full security (without the restriction of using a universal output decoder) using a “small” TP in the plain model (i.e., without any setup). -- In order to get around the above negative result, we consider protocols without a universal output decoder. The main positive result in our work is a construction of such a fully-secure MPC protocol assuming the existence of a succinct Functional Encryption scheme. We also give evidence that such an assumption is likely to be necessary for fully-secure MPC in certain restricted settings. -- Finally, we explore the possibility of achieving full-security with a semi-honest TP that could collude with other malicious parties (which form a dishonest majority). In this setting, we show that even fairness is impossible to achieve regardless of the “small TP” requirement.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Statistical Security in Two-Party Computation Revisited**
  2022-09-09 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-22365-5_7) · [IACR ePrint](https://eprint.iacr.org/2022/1190)
  Saikrishna Badrinarayanan, Pratik Sarkar, Sikhar Patranabis

  <details><summary>摘要 / Abstract</summary>

  We present a new framework for building round-optimal one-sided statistically secure two party computation (2PC) protocols in the plain model. We demonstrate that a relatively weak notion of oblivious transfer (OT), namely a three round elementary oblivious transfer $\textsf{eOT}$ with statistical receiver privacy, along with a non-interactive commitment scheme suffices to build a one-sided statistically secure two party computation protocol with black-box simulation. Our framework enables the first instantiations of round-optimal one-sided statistically secure 2PC protocols from the CDH assumption and certain families of isogeny-based assumptions. As part of our compiler, we introduce the following new one-sided statistically secure primitives in the pre-processing model that might also be of independent interest: 1. Three round statistically sender private random-OT where only the last OT message depends on the receiver&#x27;s choice bit and the sender receives random outputs generated by the protocol. 2. Four round delayed-input statistically sender private conditional disclosure of secrets where the first two rounds of the protocol are independent of the inputs of the parties. The above primitives are directly constructed from $\textsf{eOT}$ and hence we obtain their instantiations from the same set of assumptions as our 2PC.

  匹配依据：MPC: oblivious transfer, secure two party computation, two party computation

  </details>

- **Structure-Aware Private Set Intersection, With Applications to Fuzzy Matching**
  2022-08-05 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-15802-5_12) · [IACR ePrint](https://eprint.iacr.org/2022/1011)
  Jaspal Singh, Gayathri Garimella, Mike Rosulek

  <details><summary>摘要 / Abstract</summary>

  In two-party private set intersection (PSI), Alice holds a set $X$, Bob holds a set $Y$, and they learn (only) the contents of $X \cap Y$. We introduce structure-aware PSI protocols, which take advantage of situations where Alice&#x27;s set $X$ is publicly known to have a certain structure. The goal of structure-aware PSI is to have communication that scales with the description size of Alice&#x27;s set, rather its cardinality. We introduce a new generic paradigm for structure-aware PSI based on function secret-sharing (FSS). In short, if there exists compact FSS for a class of structured sets, then there exists a semi-honest PSI protocol that supports this class of input sets, with communication cost proportional only to the FSS share size. Several prior protocols for efficient (plain) PSI can be viewed as special cases of our new paradigm, with an implicit FSS for unstructured sets. Our PSI protocol can be instantiated from a significantly weaker flavor of FSS, which has not been previously studied. We develop several improved FSS techniques that take advantage of these relaxed requirements, and which are in some cases exponentially better than existing FSS. Finally, we explore in depth a natural application of structure-aware PSI. If Alice&#x27;s set $X$ is the union of many radius-$\delta$ balls in some metric space, then an intersection between $X$ and $Y$ corresponds to fuzzy PSI, in which the parties learn which of their points are within distance $\delta$. In structure-aware PSI, the communication cost scales with the number of balls in Alice&#x27;s set, rather than their total volume. Our techniques lead to efficient fuzzy PSI for $\ell_\infty$ and $\ell_1$ metrics (and approximations of $\ell_2$ metric) in high dimensions. We implemented this fuzzy PSI protocol for 2-dimensional $\ell_\infty$ metrics. For reasonable input sizes, our protocol requires 45--60% less time and 85% less communication than competing approaches that simply reduce the problem to plain PSI.

  匹配依据：MPC: private set intersection, secret sharing

  </details>

- **Two-Round MPC without Round Collapsing Revisited -- Towards Efficient Malicious Protocols**
  2022-07-20 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-15802-5_13) · [IACR ePrint](https://eprint.iacr.org/2022/944)
  Tianren Liu, Huijia Lin

  <details><summary>摘要 / Abstract</summary>

  Recent works have made exciting progress on the construction of round optimal, *two-round*, Multi-Party Computation (MPC) protocols. However, most proposals so far are still complex and inefficient. In this work, we improve the simplicity and efficiency of two-round MPC in the setting with dishonest majority and malicious security. Our protocols make use of the Random Oracle (RO) and a generalization of the Oblivious Linear Evaluation (OLE) correlated randomness, called tensor OLE, over a finite field $\mathbb{F}$, and achieve the following: - MPC for Boolean Circuits: Our two-round, maliciously secure MPC protocols for computing Boolean circuits, has overall (asymptotic) computational cost $O(S\cdot n^3 \cdot \log |\mathbb{F}|)$, where $S$ is the size of the circuit computed, $n$ the number of parties, and $\mathbb{F}$ a field of characteristic two. The protocols also make black-box calls to a Pseudo-Random Function (PRF). - MPC for Arithmetic Branching Programs (ABPs): Our two-round, information theoretically and maliciously secure protocols for computing ABPs over a general field $\mathbb{F}$ has overall computational cost $O(S^{1.5}\cdot n^3\cdot \log |\mathbb{F}|)$, where $S$ is the size of ABP computed. Both protocols achieve security levels inverse proportional to the size of the field $|\mathbb{F}|$. Our construction is built upon the simple two-round MPC protocols of [Lin-Liu-Wee TCC&#x27;20], which are only semi-honest secure. Our main technical contribution lies in ensuring malicious security using simple and lightweight checks, which incur only a constant overhead over the complexity of the protocols by Lin, Liu, and Wee. In particular, in the case of computing Boolean circuits, our malicious MPC protocols have the same complexity (up to a constant overhead) as (insecurely) computing Yao&#x27;s garbled circuits in a distributed fashion. Finally, as an additional contribution, we show how to efficiently generate tensor OLE correlation in fields of characteristic two using OT.

  匹配依据：MPC: garbled circuits, multi party computation

  </details>

- **Piranha: A GPU Platform for Secure Computation**
  2022-07-07 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity22/presentation/watson) · [IACR ePrint](https://eprint.iacr.org/2022/892) · [Code](https://github.com/ucbrise/piranha)
  Sameer Wagh, Jean-Luc Watson, Raluca A. Popa, Raluca Ada Popa

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) is an essential tool for privacy-preserving machine learning (ML). However, secure training of large-scale ML models currently requires a prohibitively long time to complete. Given that large ML inference and training tasks in the plaintext setting are significantly accelerated by Graphical Processing Units (GPUs), this raises the natural question: can secure MPC leverage GPU acceleration? A few recent works have studied this question in the context of accelerating specific components or protocols, but do not provide a general-purpose solution. Consequently, MPC developers must be both experts in cryptographic protocol design and proficient at low-level GPU kernel development to achieve good performance on any new protocol implementation. We present Piranha, a general-purpose, modular platform for accelerating secret sharing-based MPC protocols using GPUs. Piranha allows the MPC community to easily leverage the benefits of a GPU without requiring GPU expertise. Piranha contributes a three-layer architecture: (1) a device layer that can independently accelerate secret-sharing protocols by providing integer-based kernels absent in current general-purpose GPU libraries, (2) a modular protocol layer that allows developers to maximize utility of limited GPU memory with in-place computation and iterator-based support for non-standard memory access patterns, and (3) an application layer that allows applications to remain completely agnostic to the underlying protocols they use. To demonstrate the benefits of Piranha, we implement 3 state-of-the-art linear secret sharing MPC protocols for secure NN training: 2-party SecureML (IEEE S&amp;P ’17), 3-party Falcon (PETS ’21), and 4-party FantasticFour (USENIX Security ’21). Compared to their CPU-based implementations, the same protocols implemented on top of Piranha’s protocol-agnostic acceleration exhibit a 16−48× decrease in training time. For the first time, Piranha demonstrates the feasibility of training a realistic neural network (e.g. VGG), end-to-end, using MPC in a little over one day. Piranha is open source and available at https://github.com/ucbrise/piranha.

  匹配依据：MPC: secret sharing, secure computation, secure multi party computation

  </details>

- **Sharing Transformation and Dishonest Majority MPC with Packed Secret Sharing**
  2022-06-23 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-031-15985-5_1) · [IACR ePrint](https://eprint.iacr.org/2022/831)
  Vipul Goyal, Yifan Song, Antigoni Polychroniadou

  <details><summary>摘要 / Abstract</summary>

  In the last few years, the efficiency of secure multi-party computation (MPC) in the dishonest majority setting has increased by several orders of magnitudes starting with the SPDZ protocol family which offers a speedy information-theoretic online phase in the prepossessing model. However, state-of-the-art $n$-party MPC protocols in the dishonest majority setting incur online communication complexity per multiplication gate which is linear in the number of parties, i.e. $O(n)$, per gate across all parties. In this work, we construct the first MPC protocols in the preprocessing model for dishonest majority with sub-linear communication complexity per gate in the number of parties $n$. To achieve our results, we extend the use of packed secret sharing to the dishonest majority setting. For a constant fraction of corrupted parties (i.e. if 99 percent of the parties are corrupt), we can achieve a communication complexity of $O(1)$ field elements per multiplication gate across all parties. At the crux of our techniques lies a new technique called sharing transformation. The sharing transformation technique allows us to transform shares under one type of linear secret sharing scheme into another, and even perform arbitrary linear maps on the secrets of (packed) secret sharing schemes with optimal communication complexity. This technique can be of independent interest since transferring shares from one type of scheme into another (e.g., for degree reduction) is ubiquitous in MPC. Furthermore, we introduce what we call sparsely packed Shamir sharing which allows us to address the issue of network routing efficiently, and packed Beaver triples which is an extension of the widely used technique of Beaver triples for packed secret sharing (for dishonest majority).

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Pika: Secure Computation using Function Secret Sharing over Rings**
  2022-06-23 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2022-0113) · [IACR ePrint](https://eprint.iacr.org/2022/826)
  Sameer Wagh

  <details><summary>摘要 / Abstract</summary>

  Machine learning algorithms crucially depend on non-linear mathematical functions such as division (for normalization), exponentiation (for softmax and sigmoid), tanh (as an activation function), logarithm (for cross-entropy loss), and square root (for back-propagation of normalization layers). However, when machine learning is performed over secure computation, these protocols incur a large communication overhead and high round complexity. In this work, we propose new multi-party computation (MPC) protocols for such functions. Our protocols achieve constant round complexity (3 for semi-honest, 4 for malicious), an order of magnitude lower communication (54-121x lower than prior art), and high concrete efficiency (2-1163x faster runtime). We rely on recent advances in function secret sharing (FSS) to construct these protocols. Our contributions can be summarized as follows: (1) A constant round protocol to securely evaluate non-linear functions such as division, exponentiation, logarithm, and tanh (in comparison to prior art which uses round complexity proportional to the rounds of iterative methods/required precision) with high accuracy. This construction largely follows prior work in look-up style secure computation. (2) Our main contribution is the extension of the above protocol to be secure in the presence of malicious adversaries in the honest majority setting. We provide a malicious sketching protocol for FSS schemes that works over rings and in order to prove its security, we extend (and prove) a corresponding form of Schwartz-Zippel lemma over rings. This is the first such extension of the lemma and it can be of independent interest in other domains of secure computation. (3) We implement our protocol and showcase order of magnitude improvements in runtime and communication. Given the low round complexity and substantially lower communication, our protocols achieve even better performance over network constrained environments such as WAN. Finally, we showcase how such functions can lead to scalability in machine learning. Note that techniques presented are applicable beyond the application of machine learning as the protocols effectively present an efficient 1-out-of-N oblivious transfer or an efficient private information retrieval protocol.

  匹配依据：MPC: multi party computation, oblivious transfer, secret sharing, secure computation

  </details>

- **More Efficient Dishonest Majority Secure Computation over $\\mathbb{Z}\_{2^k}$ via Galois Rings**
  2022-06-22 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-031-15802-5_14) · [IACR ePrint](https://eprint.iacr.org/2022/815)
  Daniel Escudero, Chen Yuan, Chaoping Xing

  <details><summary>摘要 / Abstract</summary>

  In this work we present a novel actively secure multiparty computation protocol in the dishonest majority setting, where the computation domain is a ring of the type $\mathbb{Z}_{2^k}$. Instead of considering an &quot;extension ring&quot; of the form $\mathbb{Z}_{2^{k+\kappa}}$ as in SPD$\mathbb{Z}_{2^k}$ (Cramer et al, CRYPTO 2018) and its derivatives, we make use of an actual ring extension, or more precisely, a Galois ring extension $\mathbb{Z}_{p^k}[\mathtt{X}]/(h(\mathtt{X}))$ of large enough degree, in order to ensure that the adversary cannot cheat except with negligible probability. These techniques have been used already in the context of honest majority MPC over $\mathbb{Z}_{p^k}$, and to the best of our knowledge, our work constitutes the first study of the benefits of these tools in the dishonest majority setting. Making use of Galois ring extensions requires great care in order to avoid paying an extra overhead due to the use of larger rings. To address this, reverse multiplication-friendly embeddings (RMFEs) have been used in the honest majority setting (e.g. Cascudo et al, CRYPTO 2018), and more recently in the dishonest majority setting for computation over $\mathbb{Z}_2$ (Cascudo and Gundersen, TCC 2020). We make use of the recent RMFEs over $\mathbb{Z}_{p^k}$ from (Cramer et al, CRYPTO 2021), together with adaptations of some RMFE optimizations introduced in (Abspoel et al, ASIACRYPT 2021) in the honest majority setting, to achieve an efficient protocol that only requires in its online phase $12.4k(n-1)$ bits of amortized communication complexity and one round of communication for each multiplication gate. We also instantiate the necessary offline phase using Oblivious Linear Evaluation (OLE) by generalizing the approach based on Oblivious Transfer (OT) proposed in MASCOT (Keller et al, CCS 2016). To this end, and as an additional contribution of potential independent interest, we present a novel technique using Multiplication-Friendly Embeddings (MFEs) to achieve OLE over Galois ring extensions using black-box access to an OLE protocol over the base ring $\mathbb{Z}_{p^k}$ without paying a quadratic cost in terms of the extension degree. This generalizes the approach in MASCOT based on Correlated OT Extension. Finally, along the way we also identify a bug in a central proof in MASCOT, and we implicitly present a fix in our generalized proof.

  匹配依据：MPC: oblivious transfer, secure computation, secure multiparty computation

  </details>

- **Tight Bounds on the Randomness Complexity of Secure Multiparty Computation**
  2022-06-20 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-15985-5_17) · [IACR ePrint](https://eprint.iacr.org/2022/799)
  Yuval Ishai, Vipul Goyal, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  We revisit the question of minimizing the randomness complexity of protocols for secure multiparty computation (MPC) in the setting of perfect information-theoretic security. Kushilevitz and Mansour (SIAM J. Discret. Math., 1997) studied the case of $n$-party semi-honest MPC for the XOR function with security threshold $t&lt;n$, showing that $O(t^2\log(n/t))$ random bits are sufficient and $\Omega(t)$ random bits are necessary. Their positive result was obtained via a non-explicit protocol, whose existence was proved using the probabilistic method. We essentially close the question by proving an $\Omega(t^2)$ lower bound on the randomness complexity of XOR, matching the previous upper bound up to a logarithmic factor (or constant factor when $t=\Omega(n)$). We also obtain an explicit protocol that uses $O(t^2\cdot\log^2n)$ random bits, matching our lower bound up to a polylogarithmic factor. We extend these results from XOR to general symmetric Boolean functions and to addition over a finite Abelian group, showing how to amortize the randomness complexity over multiple additions. Finally, combining our techniques with recent randomness-efficient constructions of private circuits, we obtain an explicit protocol for evaluating a general circuit $C$ using only $O(t^2\cdot\log |C|)$ random bits, by employing additional ``helper parties&#x27;&#x27; who do not contribute any inputs. This upper bound too matches our lower bound up to a logarithmic factor.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Garbled Circuits With Sublinear Evaluator**
  2022-06-20 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-031-06944-4_2) · [IACR ePrint](https://eprint.iacr.org/2022/797)
  Akash Shah, David Heath, Abida Haque, Vladimir Kolesnikov, Steve Lu, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  Arecentlineofwork, Stacked Garbled Circuit(SGC), showed that Garbled Circuit (GC) can be improved for functions that include conditional behavior. SGC relieves the communication bottleneck of 2PC by only sending enough garbled material for a single branch out of the b total branches. Hence, communication is sublinear in the circuit size. However, both the evaluator and the generator pay in computation and perform at least factor $\log b$ extra work as compared to standard GC. We extend the sublinearity of SGC to also include the work performed by the GC evaluator E; thus we achieve a fully sublinear E, which is essential when optimizing for the online phase. We formalize our approach as a garbling scheme called GCWise: GC WIth Sublinear Evaluator. We show one attractive and immediate application, Garbled PIR, a primitive that marries GC with Private Information Retrieval. Garbled PIR allows the GC to non-interactively and sublinearly access a privately indexed element from a publicly known database, and then use this element in continued GC evaluation.

  匹配依据：MPC: garbled circuit, garbled circuits, garbling scheme

  </details>

- **Round-Optimal Multi-Party Computation with Identifiable Abort**
  2022-05-25 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-031-06944-4_12) · [IACR ePrint](https://eprint.iacr.org/2022/645)
  Michele Ciampi, Luisa Siniscalchi, Divya Ravi, Hendrik Waldner

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) protocols that are resilient to a dishonest majority allow the adversary to get the output of the computation while, at the same time, forcing the honest parties to abort. Aumann and Lindell introduced the enhanced notion of security with identifiable abort, which still allows the adversary to trigger an abort but, at the same time, it enables the honest parties to agree on the identity of the party that led to the abort. More recently, in Eurocrypt 2016, Garg et al. showed that, assuming access to a simultaneous message exchange channel for all the parties, at least four rounds of communication are required to securely realize non-trivial functionalities in the plain model. Following Garg et al., a sequence of works has matched this lower bound, but none of them achieved security with identifiable abort. In this work, we close this gap and show that four rounds of communication are also sufficient to securely realize any functionality with identifiable abort using standard and generic polynomial-time assumptions. To achieve this result we introduce the new notion of bounded-rewind secure MPC that guarantees security even against an adversary that performs a mild form of reset attacks. We show how to instantiate this primitive starting from any MPC protocol and by assuming trapdoor-permutations. The notion of bounded-rewind secure MPC allows for easier parallel composition of MPC protocols with other (interactive) cryptographic primitives. Therefore, we believe that this primitive can be useful in other contexts in which it is crucial to combine multiple primitives with MPC protocols while keeping the round complexity of the final protocol low.

  匹配依据：MPC: multi party computation, secure multi party computation

  </details>

- **Fast Fully Secure Multi-Party Computation over Any Ring with Two-Thirds Honest Majority**
  2022-05-23 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3548606.3559389) · [IACR ePrint](https://eprint.iacr.org/2022/623)
  Daniel Escudero, Ariel Nof, Anders P. K. Dalskov, Anders Dalskov

  <details><summary>摘要 / Abstract</summary>

  We introduce a new MPC protocol to securely compute any functionality over an arbitrary black-box finite ring (which may not be commutative), tolerating $t 10$).

  匹配依据：MPC: secure multi party computation

  </details>

- **Laconic Private Set-Intersection From Pairings**
  2022-05-10 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3548606.3560642) · [IACR ePrint](https://eprint.iacr.org/2022/529)
  Chuanwei Lin, Diego F. Aranha, Mark Simkin, Claudio Orlandi, Diego Aranha

  <details><summary>摘要 / Abstract</summary>

  Private set-intersection (PSI) is one of the most practically relevant special-purpose secure multiparty computation tasks, as it is motivated by many real-world applications. In this paper we present a new private set-intersection protocol which is laconic, meaning that the protocol only has two rounds and that the first message is independent of the set sizes. Laconic PSI can be useful in applications, where servers with large sets would like to learn the intersection of their set with smaller sets owned by resource-constrained clients and where multiple rounds of interactions are not possible. Previously, practically relevant laconic PSI protocols were only known from factoring-type assumptions. The contributions of this work are twofold: 1) We present the first laconic PSI protocol based on assumptions over pairing-friendly elliptic curves; and 2) For the first time we provide empirical evaluation of any laconic PSI protocol by carefully implementing and optimising both our and previous protocols. Our experimental results shows that our protocol outperforms prior laconic PSI protocols.

  匹配依据：MPC: private set intersection, secure multiparty computation

  </details>

- **Publicly Accountable Robust Multi-Party Computation**
  2022-04-06 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP46214.2022.9833608) · [IACR ePrint](https://eprint.iacr.org/2022/436)
  Daniel Rausch, Pascal Reisert, Marc Rivinius, Ralf Küsters, Ralf Kuesters

  <details><summary>摘要 / Abstract</summary>

  In recent years, lattice-based secure multi-party computation (MPC) has seen a rise in popularity and is used more and more in large scale applications like privacy-preserving cloud computing, electronic voting, or auctions. Many of these applications come with the following high security requirements: a computation result should be publicly verifiable, with everyone being able to identify a malicious party and hold it accountable, and a malicious party should not be able to corrupt the computation, force a protocol restart, or block honest parties or an honest third-party (client) that provided private inputs from receiving a correct result. The protocol should guarantee verifiability and accountability even if all protocol parties are malicious. While some protocols address one or two of these often essential security features, we present the first publicly verifiable and accountable, and (up to a threshold) robust SPDZ-like MPC protocol without restart. We propose protocols for accountable and robust online, offline, and setup computations. We adapt and partly extend the lattice-based commitment scheme by Baum et al. (SCN 2018) as well as other primitives like ZKPs. For the underlying commitment scheme and the underlying BGV encryption scheme we determine ideal parameters. We give a performance evaluation of our protocols and compare them to state-of-the-art protocols both with and without our target security features: public accountability, public verifiability and robustness.

  匹配依据：MPC: multi party computation, secure multi party computation

  </details>

- **Fully Secure PSI via MPC-in-the-Head**
  2022-03-28 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2022-0073) · [IACR ePrint](https://eprint.iacr.org/2022/379)
  Phi Hung Le, Carmit Hazay, S. Dov Gordon

  <details><summary>摘要 / Abstract</summary>

  We design several new protocols for private set intersection (PSI) with active security: one for the two party setting, and two protocols for the multi-party setting. In recent years, the state-of-the-art protocols for two party PSI have all been built from OT-extension. This has led to extremely efficient protocols that provide correct output to one party;~seemingly inherent to the approach, however, is that there is no efficient way to relay the result to the other party with a provable correctness guarantee. Furthermore, there is no natural way to extend this line of works to more parties. We consider a new instantiation of an older approach. Using the MPC-in-the-head paradigm of Ishai et al [IPS08], we construct a polynomial with roots that encode the intersection, without revealing the inputs. Our reliance on this paradigm allows us to base our protocol on passively secure Oblivious Linear Evaluation (OLE) (requiring 4 such amortized calls per input element). Unlike state-of-the-art prior work, our protocols provide correct output to all parties. We have implemented our protocols, providing the first benchmarks for PSI that provides correct output to all parties. Additionally, we present a variant of our multi-party protocol that provides output only to a central server.

  匹配依据：MPC: private set intersection

  </details>

- **IncShrink: Architecting Efficient Outsourced Databases using Incremental MPC and Differential Privacy**
  2022-03-09 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2203.05084) · [SIGMOD](https://doi.org/10.1145/3514221.3526151)
  Kartik Nayak, Johes Bater, Ashwin Machanavajjhala, Chenghong Wang

  <details><summary>摘要 / Abstract</summary>

  In this paper, we consider secure outsourced growing databases that support view-based query answering. These databases allow untrusted servers to privately maintain a materialized view, such that they can use only the materialized view to process query requests instead of accessing the original data from which the view was derived. To tackle this, we devise a novel view-based secure outsourced growing database framework, Incshrink. The key features of this solution are: (i) Incshrink maintains the view using incremental MPC operators which eliminates the need for a trusted third party upfront, and (ii) to ensure high performance, Incshrink guarantees that the leakage satisfies DP in the presence of updates. To the best of our knowledge, there are no existing systems that have these properties. We demonstrate Incshrink&#x27;s practical feasibility in terms of efficiency and accuracy with extensive empirical evaluations on real-world datasets and the TPC-ds benchmark. The evaluation results show that Incshrink provides a 3-way trade-off in terms of privacy, accuracy, and efficiency guarantees, and offers at least a 7,800 times performance advantage over standard secure outsourced databases that do not support the view-based query paradigm.

  匹配依据：MPC: mpc (context)

  </details>

- **SecFloat: Accurate Floating-Point meets Secure 2-Party Computation**
  2022-03-08 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP46214.2022.9833697) · [IACR ePrint](https://eprint.iacr.org/2022/322)
  Rahul Sharma, Deevashwer Rathee, Anwesh Bhattacharya, Aseem Rastogi, Divya Gupta, Nishanth Chandran

  <details><summary>摘要 / Abstract</summary>

  We build a library SecFloat for secure 2-party computation (2PC) of 32-bit single-precision floating-point operations and math functions. The existing functionalities used in cryptographic works are imprecise and the precise functionalities used in standard libraries are not crypto-friendly, i.e., they use operations that are cheap on CPUs but have exorbitant cost in 2PC. SecFloat bridges this gap with its novel crypto-friendly precise functionalities. Compared to the prior cryptographic libraries, SecFloat is up to six orders of magnitude more precise and up to two orders of magnitude more efficient. Furthermore, against a precise 2PC baseline, SecFloat is three orders of magnitude more efficient. The high precision of SecFloat leads to the first accurate implementation of secure inference. All prior works on secure inference of deep neural networks rely on ad hoc float-to-fixed converters. We evaluate a model where the fixed-point approximations used in privacy-preserving machine learning completely fail and floating-point is necessary. Thus, emphasizing the need for libraries like SecFloat.

  匹配依据：MPC: secure 2 party computation

  </details>

- **YOLO YOSO: Fast and Simple Encryption and Secret Sharing in the YOSO Model**
  2022-03-02 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-3-031-22963-3_22) · [IACR ePrint](https://eprint.iacr.org/2022/242)
  Bernardo Machado David, Ignacio Cascudo, Lydia Garms, Anders Konring, Bernardo David

  <details><summary>摘要 / Abstract</summary>

  Achieving adaptive (or proactive) security in cryptographic protocols is notoriously difficult due to the adversary&#x27;s power to dynamically corrupt parties as the execution progresses. Inspired by the work of Benhamouda et al. in TCC 2020, Gentry et al. in CRYPTO 2021 introduced the YOSO (You Only Speak Once) model for constructing adaptively (or proactively) secure protocols in massively distributed settings (e.g. blockchains). In this model, instead of having all parties execute an entire protocol, smaller anonymous committees are randomly chosen to execute each individual round of the protocol. After playing their role, parties encrypt protocol messages towards the the next anonymous committee and erase their internal state before publishing their ciphertexts. However, a big challenge remains in realizing YOSO protocols: efficiently encrypting messages towards anonymous parties selected at random without learning their identities, while proving the encrypted messages are valid w.r.t. the protocol. In particular, the protocols of Benhamouda et al. and of Gentry et al. require showing ciphertexts contain valid shares of secret states. We propose concretely efficient methods for encrypting a protocol&#x27;s secret state towards a random anonymous committee. We start by proposing a very simple and efficient scheme for encrypting messages towards randomly and anonymously selected parties. We then show constructions of publicly verifiable secret (re-)sharing (PVSS) schemes with concretely efficient proofs of (re-)share validity that can be generically instantiated from encryption schemes with certain linear homomorphic properties. Finally, we show that our PVSS schemes can be efficiently realized from our encyption scheme.

  匹配依据：MPC: secret sharing

  </details>

- **Short Leakage Resilient and Non-malleable Secret Sharing Schemes**
  2022-02-25 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-15802-5_7) · [IACR ePrint](https://eprint.iacr.org/2022/216)
  Sai Lakshmi Bhavana Obbattu, Sruthi Sekar, Nishanth Chandran, Bhavana Kanukurthi

  <details><summary>摘要 / Abstract</summary>

  Leakage resilient secret sharing (LRSS) allows a dealer to share a secret amongst $n$ parties such that any authorized subset of the parties can recover the secret from their shares, while an adversary that obtains shares of any unauthorized subset of parties along with bounded leakage from the other shares learns no information about the secret. Non-malleable secret sharing (NMSS) provides a guarantee that even shares that are tampered by an adversary will reconstruct to either the original message or something independent of it. The most important parameter of LRSS and NMSS schemes is the size of each share. For LRSS, in the &quot;local leakage model&quot; (i.e., when the leakage functions on each share are independent of each other and bounded), Srinivasan and Vasudevan (CRYPTO 2019), gave a scheme for threshold access structures with a share size of approximately ($3$.(message length) + $\mu$), where $\mu$ is the number of bits of leakage tolerated from every share. For the case of NMSS, the best known result (again due to the above work) has a share size of ($11$.(message length)). In this work, we build LRSS and NMSS schemes with much improved share sizes. Additionally, our LRSS scheme obtains optimal share and leakage size. In particular, we get the following results: -We build an information-theoretic LRSS scheme for threshold access structures with a share size of ((message length) + $\mu$). -As an application of the above result, we obtain an NMSS with a share size of ($4$.(message length)). Further, for the special case of sharing random messages, we obtain a share size of ($2$.(message length)).

  匹配依据：MPC: secret sharing

  </details>

- **Shuffle-based Private Set Union: Faster and More Secure**
  2022-02-12 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity22/presentation/jia) · [IACR ePrint](https://eprint.iacr.org/2022/157)
  Shifeng Sun, Jiajun Du, Yanxue Jia, Hong-Sheng Zhou, Dawu Gu, Shi-Feng Sun

  <details><summary>摘要 / Abstract</summary>

  Private Set Union ($\mathsf{PSU}$) allows two players, the sender and the receiver, to compute the union of their input datasets without revealing any more information than the result. While it has found numerous applications in practice, not much research has been carried out so far, especially for large datasets. In this work, we take shuffling technique as a key to design $\mathsf{PSU}$ protocols for the first time. By shuffling receiver&#x27;s set, we put forward the first protocol, denoted as $\Pi_{\mathsf{PSU}}^{\mathsf{receiver}}$, that eliminates the expensive operations in previous works, such as additive homomorphic encryption and repeated operations on the receiver&#x27;s set. It outperforms the state-of-the-art design by Kolesnikov et al. (ASIACRYPT 2019) in both efficiency and security; the unnecessary leakage in Kolesnikov et al.&#x27;s design, can be avoided in our design. We further extend our investigation to the application scenarios in which both players may hold unbalanced input datasets. We propose our second protocol $\Pi_{\mathsf{PSU}}^{\mathsf{sender}}$, by shuffling the sender&#x27;s dataset. This design can be viewed as a dual version of our first protocol, and it is suitable in the cases where the sender&#x27;s input size is much smaller than the receiver&#x27;s. Finally, we implement our protocols $\Pi_{\mathsf{PSU}}^{\mathsf{receiver}}$ and $\Pi_{\mathsf{PSU}}^{\mathsf{sender}}$ in C++ on big datasets, and perform a comprehensive evaluation in terms of both scalability and parallelizability. The results demonstrate that our design can obtain a $4$-$5 \times$ improvement over the state-of-the-art by Kolesnikov et al. with a single thread in WAN/LAN settings.

  匹配依据：MPC: private set union

  </details>

- **MPC-Friendly Commitments for Publicly Verifiable Covert Security**
  2022-01-31 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2109.07461) · [ACM CCS](https://doi.org/10.1145/3460120.3485375) · [IACR ePrint](https://eprint.iacr.org/2022/102)
  Matt J. Kusner, James Bell-Clark, Nitin Agrawal, Adrià Gascón, James Bell

  <details><summary>摘要 / Abstract</summary>

  We address the problem of efficiently verifying a commitment in a two-party computation. This addresses the scenario where a party P1 commits to a value x to be used in a subsequent secure computation with another party P2 that wants to receive assurance that P1 did not cheat, i.e. that x was indeed the value inputted into the secure computation. Our constructions operate in the publicly verifiable covert (PVC) security model, which is a relaxation of the malicious model of MPC appropriate in settings where P1 faces a reputational harm if caught cheating. We introduce the notion of PVC commitment scheme and indexed hash functions to build commitments schemes tailored to the PVC framework, and propose constructions for both arithmetic and Boolean circuits that result in very efficient circuits. From a practical standpoint, our constructions for Boolean circuits are 60× faster to evaluate securely, and use 36× less communication than baseline methods based on hashing. Moreover, we show that our constructions are tight in terms of required non-linear operations, by proving lower bounds on the nonlinear gate count of commitment verification circuits. Finally, we present a technique to amplify the security properties our constructions that allows to efficiently recover malicious guarantees with statistical security.

  匹配依据：MPC: secure computation, two party computation

  </details>

- **Better Security-Efficiency Trade-Offs in Permutation-Based Two-Party Computation**
  2022-01-23 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-92075-3_10) · [IACR ePrint](https://eprint.iacr.org/2022/080)
  Yu Long Chen, Stefano Tessaro

  <details><summary>摘要 / Abstract</summary>

  We improve upon the security of (tweakable) correlation-robust hash functions, which are essential components of garbling schemes and oblivious-transfer extension schemes. We in particular focus on constructions from permutations, and improve upon the work by Guo et al. (IEEE S&amp;P &#x27;20) in terms of security and efficiency. We present a tweakable one-call construction which matches the security of the most secure two-call construction -- the resulting security bound takes form O((p+q)q/2^n), where q is the number of construction evaluations and p is the number of direct adversarial queries to the underlying n-bit permutation, which is modeled as random. Moreover, we present a new two-call construction with much better security degradation -- in particular, for applications of interest, where only a constant number of evaluations per tweak are made, the security degrades as O((sqrt(q)p+q^2)/2^n). Our security proof relies on on the sum-capture theorems (Babai ’02; Steinberger ’12, Cogliati and Seurin ’18), as well as on new balls-into-bins combinatorial lemmas for limited independence ball-throws. Of independent interest, we also provide a self-contained concrete security treatment of oblivious transfer extension.

  匹配依据：MPC: garbling schemes, oblivious transfer, two party computation

  </details>

- **ZK-PCPs from Leakage-Resilient Secret Sharing**
  2022 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-022-09433-3) · [IACR ePrint](https://eprint.iacr.org/2021/606)
  Mor Weiss, Carmit Hazay, Muthuramakrishnan Venkitasubramaniam

  <details><summary>摘要 / Abstract</summary>

  Zero-Knowledge PCPs (ZK-PCPs; Kilian, Petrank, and Tardos, STOC `97) are PCPs with the additional zero-knowledge guarantee that the view of any (possibly malicious) verifier making a bounded number of queries to the proof can be efficiently simulated up to a small statistical distance. Similarly, ZK-PCPs of Proximity (ZK-PCPPs; Ishai and Weiss, TCC `14) are PCPPs in which the view of an adversarial verifier can be efficiently simulated with few queries to the input. Previous ZK-PCP constructions obtained an exponential gap between the query complexity $q$ of the honest verifier, and the bound $q^*$ on the queries of a malicious verifier (i.e., $q=polylog(q^*)$), but required either exponential-time simulation, or adaptive honest verification. This should be contrasted with standard PCPs, that can be verified non-adaptively (i.e., with a single round of queries to the proof). The problem of constructing such ZK-PCPs, even when $q^*=q$, has remained open since they were first introduced more than 2 decades ago. This question is also open for ZK-PCPPs, for which no construction with non-adaptive honest verification is known (not even with exponential-time simulation). We resolve this question by constructing the first ZK-PCPs and ZK-PCPPs which simultaneously achieve efficient zero-knowledge simulation and non-adaptive honest verification. Our schemes have a square-root query gap, namely $q^*/q=O(sqrt(n))$ where $n$ is the input length. Our constructions combine the &quot;MPC-in-the-head&quot; technique (Ishai et al., STOC `07) with leakage-resilient secret sharing. Specifically, we use the MPC-in-the-head technique to construct a ZK-PCP variant over a large alphabet, then employ leakage-resilient secret sharing to design a new alphabet reduction for ZK-PCPs which preserves zero-knowledge.

  匹配依据：MPC: secret sharing

  </details>

- **XORBoost: Tree Boosting in the Multiparty Computation Setting**
  2022 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2022-0099) · [IACR ePrint](https://eprint.iacr.org/2021/432)
  Marc Desgroseilliers, Mariya Georgieva, Dimitar Jetchev, Marius Vuille, Kevin Deforth, Nicolas Gama

  <details><summary>摘要 / Abstract</summary>

  We present a novel protocol XORBoost for both training gradient boosted tree models and for using these models for inference in the multiparty computation (MPC) setting. Similarly to [AEV20], our protocol supports training for generically split datasets (vertical and horizontal splitting, or combination of those) while keeping all the information about the features and thresholds associated with the nodes private, thus, having only the depths and the number of the binary trees as public parameters of the model. By using optimization techniques reducing the number of oblivious permutation evaluations as well as the quicksort and real number arithmetic algorithms from the recent Manticore MPC framework [CDG+21], we obtain a scalable implementation operating under information-theoretic security model in the honest-but-curious setting with a trusted dealer. On a training dataset of 25,000 samples and 300 features in the 2-player setting, we are able to train 10 regression trees of depth 4 in less than 1.5 minutes per tree (using histograms of 128 bins).

  匹配依据：MPC: multiparty computation

  </details>

- **Waldo: A Private Time-Series Database from Function Secret Sharing**
  2022 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP46214.2022.9833611) · [IACR ePrint](https://eprint.iacr.org/2021/1661)
  Mayank, Emma Dauterman, Ion Stoica, Raluca A. Popa, Mayank Rathee, Raluca Ada Popa

  <details><summary>摘要 / Abstract</summary>

  Applications today rely on cloud databases for storing and querying time-series data. While outsourcing storage is convenient, this data is often sensitive, making data breaches a serious concern. We present Waldo, a time-series database with rich functionality and strong security guarantees: Waldo supports multi-predicate filtering, protects data contents as well as query filter values and search access patterns, and provides malicious security in the 3-party honest-majority setting. In contrast, prior systems such as Timecrypt and Zeph have limited functionality and security: (1) these systems can only filter on time, and (2) they reveal the queried time interval to the server. Oblivious RAM (ORAM) and generic multiparty computation (MPC) are natural choices for eliminating leakage from prior work, but both of these are prohibitively expensive in our setting due to the number of roundtrips and bandwidth overhead, respectively. To minimize both, Waldo builds on top of function secret sharing, enabling Waldo to evaluate predicates without client interaction. We develop new techniques for applying function secret sharing to the encrypted database setting where there are malicious servers, secret inputs, and chained predicates. With 32-core machines, Waldo runs a query with 8 range predicates over $2^{18}$ records in 3.03s, compared to 12.88s for an MPC baseline and 16.56s for an ORAM baseline. Compared to Waldo, the MPC baseline uses 9 − 82× more bandwidth between servers (for different numbers of records), while the ORAM baseline uses 20 − 152× more bandwidth between the client and server(s) (for different numbers of predicates).

  匹配依据：MPC: multiparty computation, secret sharing

  </details>

- **Updatable Private Set Intersection**
  2022 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.2478/POPETS-2022-0051) · [IACR ePrint](https://eprint.iacr.org/2021/1349)
  Saikrishna Badrinarayanan, Peihan Miao, Tiancheng Xie

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) allows two mutually distrusting parties each with a set as input, to learn the intersection of both their sets without revealing anything more about their respective input sets. Traditionally, PSI studies the static setting where the computation is performed only once on both parties&#x27; input sets. We initiate the study of updatable private set intersection (UPSI), which allows parties to compute the intersection of their private sets on a regular basis with sets that also constantly get updated. We consider two specific settings. In the first setting called UPSI with addition, parties can add new elements to their old sets. We construct two protocols in this setting, one allowing both parties to learn the output and the other only allowing one party to learn the output. In the second setting called UPSI with weak deletion, parties can additionally delete their old elements every $t$ days. We present a protocol for this setting allowing both parties to learn the output. All our protocols are secure against semi-honest adversaries and have the guarantee that both the computational and communication complexity only grow with the set updates instead of the entire sets. Finally, we implement our UPSI with addition protocols and compare with the state-of-the-art PSI protocols. Our protocols compare favorably when the total set size is sufficiently large, the new updates are sufficiently small, or in networks with low bandwidth.

  匹配依据：MPC: private set intersection

  </details>

- **TinyKeys: A New Approach to Efficient Multi-Party Computation.**
  2022 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-022-09423-5)
  Peter Scholl, Eduardo Soria-Vazquez, Emmanuela Orsini, Carmit Hazay

- **Self-Stabilizing Secure Computation.**
  2022 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2020.2986751)
  Dan Brownstein, Shlomi Dolev, Muni Venkateswarlu K.

- **Secure Multiparty Computation with Sublinear Preprocessing.**
  2022 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-031-06944-4_15)
  Elette Boyle, Ariel Nof, Yuval Ishai, Niv Gilboa

- **Secret Sharing Based Reversible Data Hiding in Encrypted Images With Multiple Data-Hiders.**
  2022 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2020.3011923)
  Jiwu Huang, Jian Weng, Bing Chen, Wei Lu, Yicong Zhou

- **STAR: Secret Sharing for Private Threshold Aggregation Reporting**
  2022 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2109.10074) · [ACM CCS](https://doi.org/10.1145/3548606.3560631)
  Peter Snyder, Alex Davidson, Hamed Haddadi, Joseph Genereux, E. B. Quirk, Benjamin Livshits

  <details><summary>摘要 / Abstract</summary>

  Threshold aggregation reporting systems promise a practical, privacy-preserving solution for developers to learn how their applications are used &quot;\emph{in-the-wild}&quot;. Unfortunately, proposed systems to date prove impractical for wide scale adoption, suffering from a combination of requiring: \emph{i)} prohibitive trust assumptions; \emph{ii)} high computation costs; or \emph{iii)} massive user bases. As a result, adoption of truly-private approaches has been limited to only a small number of enormous (and enormously costly) projects. In this work, we improve the state of private data collection by proposing $\mathsf{STAR}$, a highly efficient, easily deployable system for providing cryptographically-enforced $κ$-anonymity protections on user data collection. The $\mathsf{STAR}$ protocol is easy to implement and cheap to run, all while providing privacy properties similar to, or exceeding the current state-of-the-art. Measurements of our open-source implementation of $\mathsf{STAR}$ find that it is $1773\times$ quicker, requires $62.4\times$ less communication, and is $24\times$ cheaper to run than the existing state-of-the-art.

  匹配依据：MPC: secret sharing

  </details>

- **Round-Optimal and Communication-Efficient Multiparty Computation**
  2022 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-06944-4_3) · [IACR ePrint](https://eprint.iacr.org/2020/1437)
  Michele Ciampi, Hendrik Waldner, Vassilis Zikas, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  Typical approaches for minimizing the round complexity of multiparty computation (MPC) come at the cost of increased communication complexity (CC) or the reliance on setup assumptions. A notable exception is the recent work of Ananth et al. [TCC 2019], which used Functional Encryption (FE) combiners to obtain a round optimal (two-round) semi-honest MPC in the plain model with a CC proportional to the depth and input-output length of the circuit being computed—we refer to such protocols as circuit scalable. This leaves open the question of obtaining communication efficient protocols that are secure against malicious adversaries in the plain model, which we present in this work. Concretely, our two main contributions are: 1) We provide a round-preserving black-box compiler that compiles a wide class of MPC protocols into circuit-scalable maliciously secure MPC protocols in the plain model, assuming (succinct) FE combiners. 2) We provide a round-preserving black-box compiler that compiles a wide class of MPC protocols into circuit-independent— i.e., with a CC that depends only on the input-output length of the circuit—maliciously secure MPC protocols in the plain model, assuming Multi-Key Fully-Homomorphic Encryption (MFHE). Our constructions are based on a new compiler that turns a wide class of MPC protocols into k-delayed-input function MPC protocols (a notion we introduce), where the function that is being computed is specified only in the k-th round of the protocol. As immediate corollaries of our two compilers, we derive (1) the first round-optimal and circuit-scalable maliciously secure MPC protocol, and (2) the first round-optimal and circuit-independent maliciously secure MPC protocol in the plain model. The latter achieves the best to-date CC for a round-optimal maliciously secure MPC protocol. In fact, it is even communication-optimal when the output size of the function being evaluated is smaller than its input size (e.g., for boolean functions). All of our results are based on standard polynomial time assumptions.

  匹配依据：MPC: multiparty computation

  </details>

- **Round-Optimal Honest-Majority MPC in Minicrypt and with Everlasting Security - (Extended Abstract).**
  2022 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-22365-5_4)
  Eliran Kachlon, Benny Applebaum, Arpita Patra

- **Quantum Garbled Circuits**
  2022 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2006.01085) · [STOC](https://doi.org/10.1145/3519935.3520073) · [IACR ePrint](https://eprint.iacr.org/2020/1401)
  Henry Yuen, Zvika Brakerski

  <details><summary>摘要 / Abstract</summary>

  We present a garbling scheme for quantum circuits, thus achieving a decomposable randomized encoding scheme for quantum computation. Specifically, we show how to compute an encoding of a given quantum circuit and quantum input, from which it is possible to derive the output of the computation and nothing else. In the classical setting, garbled circuits (and randomized encodings in general) are a versatile cryptographic tool with many applications such as secure multiparty computation, delegated computation, depth-reduction of cryptographic primitives, complexity lower-bounds, and more. However, a quantum analogue for garbling general circuits was not known prior to this work. We hope that our quantum randomized encoding scheme can similarly be useful for applications in quantum computing and cryptography. To illustrate the usefulness of quantum randomized encoding, we use it to design a conceptually-simple zero-knowledge (ZK) $\Sigma$-protocol for the complexity class QMA. Our protocol has a single-bit challenge, and allows the inputs to be delayed to the last round. The only previously-known ZK $\Sigma$-protocol for QMA is due to Broadbent and Grilo (FOCS 2020), which does not have the aforementioned properties.

  匹配依据：MPC: garbled circuits, garbling scheme, secure multiparty computation

  </details>

- **Practical Non-interactive Publicly Verifiable Secret Sharing with Thousands of Parties**
  2022 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-06944-4_16) · [IACR ePrint](https://eprint.iacr.org/2021/1397)
  Craig Gentry, Vadim Lyubashevsky, Shai Halevi

  <details><summary>摘要 / Abstract</summary>

  Non-interactive publicly verifiable secret sharing (PVSS) schemes enables (re-)sharing of secrets in a decentralized setting in the presence of malicious parties. A recently proposed application of PVSS schemes is to enable permissionless proof-of-stake blockchains to ``keep a secret&quot; via a sequence of committees that share that secret. These committees can use the secret to produce signatures on the blockchain&#x27;s behalf, or to disclose hidden data conditioned on consensus that some event has occurred. That application needs very large committees with thousands of parties, so the PVSS scheme in use must be efficient enough to support such large committees, in terms of both computation and communication. Yet, previous PVSS schemes have large proofs and/or require many exponentiations over large groups. We present a non-interactive PVSS scheme in which the underlying encryption scheme is based on the learning with errors (LWE) problem. While lattice-based encryption schemes are very fast, they often have long ciphertexts and public keys. We use the following two techniques to conserve bandwidth: First, we adapt the Peikert-Vaikuntanathan-Waters (PVW) encryption scheme to the multi-receiver setting, so that the bulk of the parties&#x27; keys is a common random string. The resulting scheme yields $\Omega(1)$ amortized plaintext/ciphertext rate, where concretely the rate is $\approx 1/60$ for 100 parties, $\approx 1/8$ for 1000 parties, and approaching 1/2 as the number of parties grows. Second, we use bulletproofs over a DL-group of order about 256 bits to get compact proofs of correct encryption/decryption of shares. Alternating between the lattice and DL settings is relatively painless, as we equate the LWE modulus with the order of the group. We also show how to reduce the the number of exponentiations in the bulletproofs by applying Johnson-Lindenstrauss-like compression to reduce the dimension of the vectors whose properties must be verified. An implementation of our PVSS with 1000 parties showed that it is feasible even at that size, and should remain so even with one or two order of magnitude increase in the committee size.

  匹配依据：MPC: secret sharing

  </details>

- **Practical Multi-Party Private Set Intersection Protocols.**
  2022 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2021.3118879)
  Aslí Bay, Zekeriya Erkin, Simona Samardjiska, Jelle Vos, Jaap-Henk Hoepman

- **Polymath: Low-Latency MPC via Secure Polynomial Evaluations and its Applications**
  2022 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.2478/POPETS-2022-0020) · [IACR ePrint](https://eprint.iacr.org/2021/978)
  Aniket Kate, Donghang Lu, Albert Yu, Hemanta K. Maji, Hemanta Maji

  <details><summary>摘要 / Abstract</summary>

  While the practicality of secure multi-party computation (MPC) has been extensively analyzed and improved over the past decade, we are hitting the limits of efficiency with the traditional approaches of representing the computed functionalities as generic arithmetic or Boolean circuits. This work follows the design principle of identifying and constructing fast and provably-secure MPC protocols to evaluate useful high-level algebraic abstractions; thus, improving the efficiency of all applications relying on them. We present Polymath, a constant-round secure computation protocol suite for the secure evaluation of (multi-variate) polynomials of scalars and matrices, functionalities essential to numerous data-processing applications. Using precise natural precomputation and high-degree of parallelism prevalent in the modern computing environments, Polymath can make latency of secure polynomial evaluations of scalars and matrices independent of polynomial degree and matrix dimensions. We implement our protocols over the HoneyBadgerMPC library and apply them to two prominent secure computation tasks: privacy-preserving evaluation of decision trees and privacy-preserving evaluation of Markov processes. For the decision tree evaluation problem, we demonstrate the feasibility of evaluating high-depth decision tree models in a general n-party setting. For the Markov process application, we demonstrate that Polymath can compute large powers of transition matrices with better online time and less communication.

  匹配依据：MPC: secure computation, secure evaluation, secure multi party computation

  </details>

- **PPMLAC: high performance chipset architecture for secure multi-party computation.**
  2022 · MPC · 含会议/期刊记录 · [ISCA](https://doi.org/10.1145/3470496.3527392)
  Cong Wang, Zhilei Xu, Xing Zhou, Mingyu Gao

- **On Secret Sharing, Randomness, and Random-less Reductions for Secret Sharing**
  2022 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-22318-1_12) · [IACR ePrint](https://eprint.iacr.org/2021/802)
  Maciej Obremski, Divesh Aggarwal, João Ribeiro, Eldon Chung

  <details><summary>摘要 / Abstract</summary>

  Secret-sharing is one of the most basic and oldest primitives in cryptography, introduced by Shamir and Blakely in the 70s. It allows to strike a meaningful balance between availability and confidentiality of secret information. It has a host of applications most notably in threshold cryptography and multi-party computation. All known constructions of secret sharing (with the exception of those with a pathological choice of parameters) require access to uniform randomness. In practice, it is extremely challenging to generate a source of uniform randomness. This has led to a large body of research devoted to designing randomized algorithms and cryptographic primitives from imperfect sources of randomness. Motivated by this, 15 years ago, Bosley and Dodis asked whether it is even possible to build 2-out-of-2 secret sharing without access to uniform randomness. In this work, we make progress towards resolving this question. We answer this question for secret sharing schemes with important additional properties, i.e., either leakage-resilience or non-malleability. We prove that, unfortunately, for not too small secrets, it is impossible to construct any of 2-out-of-2 leakage-resilient secret sharing or 2-out-of-2 non-malleable secret sharing without access to uniform randomness. Given that the problem whether 2-out-of-2 secret sharing requires uniform randomness has been open for a long time, it is reasonable to consider intermediate problems towards resolving the open question. In a spirit similar to NP-completeness, we study how the existence of a t-out-of-n secret sharing without access to uniform randomness is related to the existence of a t&#x27;-out-of-n&#x27; secret sharing without access to uniform randomness for a different choice of the parameters t,n,t&#x27;,n&#x27;.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Lightweight, Maliciously Secure Verifiable Function Secret Sharing**
  2022 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-06944-4_6) · [IACR ePrint](https://eprint.iacr.org/2021/580)
  Leo de Castro, Antigoni Polychroniadou

  <details><summary>摘要 / Abstract</summary>

  In this work, we present a lightweight construction of verifiable two-party function secret sharing (FSS) for point functions and multi-point functions. Our verifiability method is lightweight in two ways. Firstly, it is concretely efficient, making use of only symmetric key operations and no public key or MPC techniques are involved. Our performance is comparable with the state-of-the-art non-verifiable DPF constructions, and we outperform all prior DPF verification techniques in both computation and communication complexity, which we demonstrate with an implementation of our scheme. Secondly, our verification procedure is essentially unconstrained. It will verify that distributed point function (DPF) shares correspond to some point function irrespective of the output group size, the structure of the DPF output, or the set of points on which the DPF must be evaluated. This is in stark contrast with prior works, which depend on at least one and often all three of these constraints. In addition, our construction is the first DPF verification protocol that can verify general DPFs while remaining secure even if one server is malicious. Prior work on maliciously secure DPF verification could only verify DPFs where the non-zero output is binary. As an additional feature, our verification procedure can be batched so that verifying a polynomial number of DPF shares requires the exact same amount of communication as verifying one pair of DPF shares. We combine this packed DPF verification with a novel method for packing DPFs into shares of a multi-point function where the evaluation time, verification time, and verification communication are independent of the number of non-zero points in the function. An immediate corollary of our results are two-server protocols for PIR and PSI that remain secure when any one of the three parties is malicious (either the client or one of the servers).

  匹配依据：MPC: secret sharing

  </details>

- **Leakage-resilient Linear Secret-sharing Against Arbitrary Bounded-size Leakage Family.**
  2022 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-031-22318-1_13)
  Hai H. Nguyen, Tom Suad, Mingyuan Wang, Xiuyu Ye, Anat Paskin-Cherniavsky, Albert Yu, Hemanta K. Maji

- **Geometry of Secure Two-party Computation.**
  2022 · MPC · 含会议/期刊记录 · [FOCS](https://doi.org/10.1109/FOCS54457.2022.00101)
  Hamidreza Amini Khorasgani, Hai H. Nguyen, Hemanta K. Maji, Saugata Basu

- **From Fairness to Full Security in Multiparty Computation**
  2022 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2105.00962) · [Journal of Cryptology](https://doi.org/10.1007/S00145-021-09415-X)
  Lior Rotem, Ran Cohen, Iftach Haitner, Eran Omri

  <details><summary>摘要 / Abstract</summary>

  In the setting of secure multiparty computation (MPC), a set of mutually distrusting parties wish to jointly compute a function, while guaranteeing the privacy of their inputs and the correctness of the output. An MPC protocol is called \emph{fully secure} if no adversary can prevent the honest parties from obtaining their outputs. A protocol is called \emph{fair} if an adversary can prematurely abort the computation, however, only before learning any new information. We present highly efficient transformations from fair computations to fully secure computations, assuming the fraction of honest parties is constant (e.g., $1\%$ of the parties are honest). Compared to previous transformations that require linear invocations (in the number of parties) of the fair computation, our transformations require super-logarithmic, and sometimes even super-constant, such invocations. The main idea is to delegate the computation to chosen random committees that invoke the fair computation. Apart from the benefit of uplifting security, the reduction in the number of parties is also useful, since only committee members are required to work, whereas the remaining parties simply &quot;listen&quot; to the computation over a broadcast channel.

  匹配依据：MPC: multiparty computation, secure multiparty computation

  </details>

- **Fast Privacy-Preserving Text Classification based on Secure Multiparty Computation**
  2022 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2101.07365) · [TIFS](https://doi.org/10.1109/TIFS.2022.3144007) · [IACR ePrint](https://eprint.iacr.org/2021/069)
  Anderson C. A. Nascimento, Amanda Cristina Davi Resende, Davis Railsback, Rafael Dowsley, Diego F. Aranha, Amanda Resende

  <details><summary>摘要 / Abstract</summary>

  We propose a privacy-preserving Naive Bayes classifier and apply it to the problem of private text classification. In this setting, a party (Alice) holds a text message, while another party (Bob) holds a classifier. At the end of the protocol, Alice will only learn the result of the classifier applied to her text input and Bob learns nothing. Our solution is based on Secure Multiparty Computation (SMC). Our Rust implementation provides a fast and secure solution for the classification of unstructured text. Applying our solution to the case of spam detection (the solution is generic, and can be used in any other scenario in which the Naive Bayes classifier can be employed), we can classify an SMS as spam or ham in less than 340ms in the case where the dictionary size of Bob&#x27;s model includes all words (n = 5200) and Alice&#x27;s SMS has at most m = 160 unigrams. In the case with n = 369 and m = 8 (the average of a spam SMS in the database), our solution takes only 21ms.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Estimating Incidental Collection in Foreign Intelligence Surveillance: Large-Scale Multiparty Private Set Intersection with Union and Sum.**
  2022 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity22/presentation/kulshrestha)
  Anunay Kulshrestha, Jonathan R. Mayer

- **Efficient Perfectly Secure Computation with Optimal Resilience**
  2022 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-030-90453-1_3) · [Journal of Cryptology](https://doi.org/10.1007/S00145-022-09434-2) · [IACR ePrint](https://eprint.iacr.org/2021/1206)
  Avishay Yanai, Gilad Asharov, Ittai Abraham

  <details><summary>摘要 / Abstract</summary>

  Secure computation enables $n$ mutually distrustful parties to compute a function over their private inputs jointly. In 1988 Ben-Or, Goldwasser, and Wigderson (BGW) demonstrated that any function can be computed with perfect security in the presence of a malicious adversary corrupting at most $t&lt; n/3$ parties. After more than 30 years, protocols with perfect malicious security, with round complexity proportional to the circuit&#x27;s depth, still require sharing a total of $O(n^2)$ values per multiplication. In contrast, only $O(n)$ values need to be shared per multiplication to achieve semi-honest security. Indeed sharing $\Omega(n)$ values for a single multiplication seems to be the natural barrier for polynomial secret sharing-based multiplication. In this paper, we close this gap by constructing a new secure computation protocol with perfect, optimal resilience and malicious security that incurs sharing of only $O(n)$ values per multiplication, thus, matching the semi-honest setting for protocols with round complexity that is proportional to the circuit depth. Our protocol requires a constant number of rounds per multiplication. Like BGW, it has an overall round complexity that is proportional only to the multiplicative depth of the circuit. Our improvement is obtained by a novel construction for {\em weak VSS for polynomials of degree-$2t$}, which incurs the same communication and round complexities as the state-of-the-art constructions for {\em VSS for polynomials of degree-$t$}. Our second contribution is a method for reducing the communication complexity for any depth-1 sub-circuit to be proportional only to the size of the input and output (rather than the size of the circuit). This implies protocols with \emph{sublinear communication complexity} (in the size of the circuit) for perfectly secure computation for important functions like matrix multiplication.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Differentially Private Set Intersection for Asymmetrical ID Alignment.**
  2022 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2022.3207911)
  Xinyu Tan, Yuanyuan He, Xianjun Deng, Jianbing Ni, Laurence T. Yang

- **Correction to: Unconditionally Secure Computation Against Low-Complexity Leakage.**
  2022 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-021-09412-0) · [Journal of Cryptology](https://doi.org/10.1007/S00145-021-09417-9)
  Akshayaram Srinivasan, Andrej Bogdanov, Yuval Ishai

- **Concurrently Composable Non-Interactive Secure Computation**
  2022 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-3-031-22963-3_18) · [IACR ePrint](https://eprint.iacr.org/2021/1562)
  Rafael Pass, Andrew Morgan

  <details><summary>摘要 / Abstract</summary>

  We consider the feasibility of non-interactive secure two-party computation (NISC) in the plain model satisfying the notion of superpolynomial-time simulation (SPS). While stand-alone secure SPS-NISC protocols are known from standard assumptions (Badrinarayanan et al., Asiacrypt 2017), it has remained an open problem to construct a concurrently composable SPS-NISC. Prior to our work, the best protocols require 5 rounds (Garg et al., Eurocrypt 2017), or 3 simultaneous-message rounds (Badrinarayanan et al., TCC 2017). In this work, we demonstrate the first concurrently composable SPS-NISC. Our construction assumes the existence of: - a non-interactive (weakly) CCA-secure commitment, - a stand-alone secure SPS-NISC with subexponential security, and satisfies the notion of &quot;angel-based&quot; UC security (i.e., UC with a superpolynomial-time helper) with perfect correctness. We additionally demonstrate that both of the primitives we use (albeit only with polynomial security) are necessary for such concurrently composable SPS-NISC with perfect correctness. As such, our work identifies essentially necessary and sufficient primitives for concurrently composable SPS-NISC with perfect correctness in the plain model.

  匹配依据：MPC: secure computation, secure two party computation

  </details>

- **COBRA: Dynamic Proactive Secret Sharing for Confidential BFT Services.**
  2022 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP46214.2022.9833658)
  Eduardo Alchieri, Bernardo Ferreira, Robin Vassantlal, Alysson Neves Bessani

- **Binary Search in Secure Computation**
  2022 · MPC · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/auto-draft-224/) · [IACR ePrint](https://eprint.iacr.org/2021/1049)
  Marina Blanton, Chen Yuan

  <details><summary>摘要 / Abstract</summary>

  Binary search is one of the most popular algorithms in computer science. Realizing it in the context of secure multiparty computation which demands data-oblivious execution, however, is extremely non-trivial. It has been previously implemented only using oblivious RAM (ORAM) for secure computation and in this work we initiate the study of this topic using conventional secure computation techniques based on secret sharing. We develop a suite of protocols with different properties and of different structure for searching a private dataset of $m$ elements by a private numeric key. Our protocols result in $O(m)$ and $O(\sqrt{m})$ communication using only standard and readily available operations based on secret sharing. We further extend our protocols to support write operations, namely, binary search that obliviously updates the selected element, and realize two variants: updating non-key fields and updating the key field. Our implementation results indicate that even after applying known and our own optimizations to the fastest ORAM constructions, our solutions are faster than optimized ORAM schemes for datasets of up to $2^{30}$ elements and by up to two orders of magnitude. We hope that this work will prompt further interest in seeking efficient realizations of this important problem.

  匹配依据：MPC: secret sharing, secure computation, secure multiparty computation

  </details>

- **Analog Secret Sharing With Applications to Private Distributed Learning.**
  2022 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2022.3173417)
  Hessam Mahdavifar, Mahdi Soleymani, Amir Salman Avestimehr

- **Adaptively Secure Computation for RAM Programs.**
  2022 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-031-07085-3_7)
  Oxana Poburinnaya, Laasya Bangalore, Rafail Ostrovsky, Muthuramakrishnan Venkitasubramaniam

- **ARIANN: Low-Interaction Privacy-Preserving Deep Learning via Function Secret Sharing**
  2022 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2006.04593) · [PoPETs](https://doi.org/10.2478/POPETS-2022-0015)
  Théo Ryffel, Pierre Tholoniat, David Pointcheval, Francis R. Bach, Francis Bach

  <details><summary>摘要 / Abstract</summary>

  We propose AriaNN, a low-interaction privacy-preserving framework for private neural network training and inference on sensitive data. Our semi-honest 2-party computation protocol (with a trusted dealer) leverages function secret sharing, a recent lightweight cryptographic protocol that allows us to achieve an efficient online phase. We design optimized primitives for the building blocks of neural networks such as ReLU, MaxPool and BatchNorm. For instance, we perform private comparison for ReLU operations with a single message of the size of the input during the online phase, and with preprocessing keys close to 4X smaller than previous work. Last, we propose an extension to support n-party private federated learning. We implement our framework as an extensible system on top of PyTorch that leverages CPU and GPU hardware acceleration for cryptographic and machine learning operations. We evaluate our end-to-end system for private inference between distant servers on standard neural networks such as AlexNet, VGG16 or ResNet18, and for private training on smaller networks like LeNet. We show that computation rather than communication is the main bottleneck and that using GPUs together with reduced key size is a promising solution to overcome this barrier.

  匹配依据：MPC: 2 party computation, secret sharing

  </details>
