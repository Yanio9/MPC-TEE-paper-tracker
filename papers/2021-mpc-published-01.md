# 2021 · MPC · 含会议/期刊记录 · 第 1/1 页

[总目录](../PAPERS.md)

- **On the Round Complexity of Black-box Secure MPC**
  2021-11-06 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-84245-1_8) · [IACR ePrint](https://eprint.iacr.org/2021/1467)
  Yuval Ishai, Akshayaram Srinivasan, Dakshita Khurana, Amit Sahai

  <details><summary>摘要 / Abstract</summary>

  We consider the question of minimizing the round complexity of secure multiparty computation (MPC) protocols that make a black-box use of simple cryptographic primitives in the setting of security against any number of malicious parties. In the plain model, previous black-box protocols required a high constant number of rounds (&gt;15). This is far from the known lower bound of 4 rounds for protocols with black-box simulators. When allowing a random oblivious transfer (OT) correlation setup, 2-round protocols making a black-box use of a pseudorandom generator were previously known. However, such protocols were obtained via a round-collapsing ``protocol garbling&#x27;&#x27; technique that has poor concrete efficiency and makes a non-black-box use of an underlying malicious-secure protocol. We improve this state of affairs by presenting the following types of black-box protocols. - 4-round ``pairwise MPC&#x27;&#x27; in the plain model. This round-optimal protocol enables each ordered pair of parties to compute a function of both inputs whose output is delivered to the second party. The protocol makes black-box use of any public-key encryption (PKE) with pseudorandom public keys. As a special case, we get a black-box round-optimal realization of secure (copies of) OT between every ordered pair of parties. - 2-round MPC from OT correlations. This round-optimal protocol makes a black-box use of any general 2-round MPC protocol satisfying an augmented notion of {\em semi-honest} security. In the two-party case, this yields new kinds of 2-round black-box protocols. - 5-round MPC in the plain model. This protocol makes a black-box use of PKE with pseudorandom public keys, and 2-round oblivious transfer with ``semi-malicious&#x27;&#x27; security. A key technical tool for the first result is a novel combination of split-state non-malleable codes (Dziembowski, Pietrzak and Wichs, JACM &#x27;18) with standalone secure two-party protocols. The second result is based on a new round-optimized variant of the ``IPS compiler&#x27;&#x27; (Ishai, Prabhakaran and Sahai, Crypto &#x27;08). The third result is obtained via a specialized combination of these two techniques.

  匹配依据：MPC: oblivious transfer, secure multiparty computation

  </details>

- **Oblivious Transfer from Trapdoor Permutations in Minimal Rounds**
  2021-10-26 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-030-90453-1_18) · [IACR ePrint](https://eprint.iacr.org/2021/1433)
  Michele Ciampi, Arka Rai Choudhuri, Vipul Goyal, Abhishek Jain, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  Oblivious transfer (OT) is a foundational primitive within cryptography owing to its connection with secure computation. One of the oldest constructions of oblivious transfer was from certified trapdoor permutations (TDPs). However several decades later, we do not know if a similar construction can be obtained from TDPs in general. In this work, we study the problem of constructing round optimal oblivious transfer from trapdoor permutations. In particular, we obtain the following new results (in the plain model) relying on TDPs in a black-box manner: 1) Three-round oblivious transfer protocol that guarantees indistinguishability-security against malicious senders (and semi-honest receivers). 2) Four-round oblivious transfer protocol secure against malicious adversaries with black-box simulation-based security. By combining our second result with an already known compiler we obtain the first round-optimal 2-party computation protocol that relies in a black-box way on TDPs. A key technical tool underlying our results is a new primitive we call dual witness encryption (DWE) that may be of independent interest.

  匹配依据：MPC: 2 party computation, oblivious transfer, secure computation

  </details>

- **Homomorphic Secret Sharing for Multipartite and General Adversary Structures Supporting Parallel Evaluation of Low-degree Polynomials**
  2021-10-18 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-92075-3_7) · [IACR ePrint](https://eprint.iacr.org/2021/1395)
  Reo Eriguchi, Koji Nuida

  <details><summary>摘要 / Abstract</summary>

  Homomorphic secret sharing (HSS) for a function $f$ allows input parties to distribute shares for their private inputs and then locally compute output shares from which the value of $f$ is recovered. HSS can be directly used to obtain a two-round multiparty computation (MPC) protocol for possibly non-threshold adversary structures whose communication complexity is independent of the size of $f$. In this paper, we propose two constructions of HSS schemes supporting parallel evaluation of a single low-degree polynomial and tolerating multipartite and general adversary structures. Our multipartite scheme tolerates a wider class of adversary structures than the previous multipartite one in the particular case of a single evaluation and has exponentially smaller share size than the general construction. While restricting the range of tolerable adversary structures (but still applicable to non-threshold ones), our schemes perform $\ell$ parallel evaluations with communication complexity approximately $\ell/\log\ell$ times smaller than simply using $\ell$ independent instances. We also formalize two classes of adversary structures taking into account real-world situations to which the previous threshold schemes are inapplicable. Our schemes then perform $O(m)$ parallel evaluations with almost the same communication cost as a single evaluation, where $m$ is the number of parties.

  匹配依据：MPC: multiparty computation, secret sharing

  </details>

- **Reverse Firewalls for Adaptively Secure MPC without Setup**
  2021-09-22 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-92075-3_12) · [IACR ePrint](https://eprint.iacr.org/2021/1262)
  Suvradip Chakraborty, Pratik Sarkar, Chaya Ganesh, Mahak Pancholi

  <details><summary>摘要 / Abstract</summary>

  We study Multi-party computation (MPC) in the setting of subversion, where the adversary tampers with the machines of honest parties. Our goal is to construct actively secure MPC protocols where parties are corrupted adaptively by an adversary (as in the standard adaptive security setting), and in addition, honest parties&#x27; machines are compromised. The idea of reverse firewalls (RF) was introduced at EUROCRYPT&#x27;15 by Mironov and Stephens-Davidowitz as an approach to protecting protocols against corruption of honest parties&#x27; devices. Intuitively, an RF for a party $\mathcal{P}$ is an external entity that sits between $\mathcal{P}$ and the outside world and whose scope is to sanitize $\mathcal{P}$’s incoming and outgoing messages in the face of subversion of their computer. Mironov and Stephens-Davidowitz constructed a protocol for passively-secure two-party computation. At CRYPTO&#x27;20, Chakraborty, Dziembowski and Nielsen constructed a protocol for secure computation with firewalls that improved on this result, both by extending it to multi-party computation protocol, and considering active security in the presence of static corruptions. In this paper, we initiate the study of RF for MPC in the adaptive setting. We put forward a definition for adaptively secure MPC in the reverse firewall setting, explore relationships among the security notions, and then construct reverse firewalls for MPC in this stronger setting of adaptive security. We also resolve the open question of Chakraborty, Dziembowski and Nielsen by removing the need for a trusted setup in constructing RF for MPC. Towards this end, we construct reverse firewalls for adaptively secure augmented coin tossing and adaptively secure zero-knowledge protocols and obtain a constant round adaptively secure MPC protocol in the reverse firewall setting without setup. Along the way, we propose a new multi-party adaptively secure coin tossing protocol in the plain model, that is of independent interest.

  匹配依据：MPC: multi party computation, secure computation, secure two party computation

  </details>

- **Two-Round Maliciously Secure Computation with Super-Polynomial Simulation**
  2021-09-20 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-030-90459-3_22) · [IACR ePrint](https://eprint.iacr.org/2021/1230)
  Giulio Malavolta, James Bartusek, Dakshita Khurana, Vipul Goyal, Amit Agarwal

  <details><summary>摘要 / Abstract</summary>

  We propose the first maliciously secure multi-party computation (MPC) protocol for general functionalities in two rounds, without any trusted setup. Since polynomial-time simulation is impossible in two rounds, we achieve the relaxed notion of superpolynomial-time simulation security [Pass, EUROCRYPT 2003]. Prior to our work, no such maliciously secure protocols were known even in the two-party setting for functionalities where both parties receive outputs. Our protocol is based on the sub-exponential security of standard assumptions plus a special type of non-interactive non-malleable commitment. At the heart of our approach is a two-round multi-party conditional disclosure of secrets (MCDS) protocol in the plain model from bilinear maps, which is constructed from techniques introduced in [Benhamouda and Lin, TCC 2020].

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **Simple, Fast Malicious Multiparty Private Set Intersection**
  2021-09-20 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3460120.3484772) · [IACR ePrint](https://eprint.iacr.org/2021/1221)
  Ni Trieu, Avishay Yanai, Ofri Nevo

  <details><summary>摘要 / Abstract</summary>

  We address the problem of multiparty private set intersection against a malicious adversary. First, we show that when one can assume no collusion amongst corrupted parties then there exists an extremely efficient protocol given only symmetric-key primitives. Second, we present a protocol secure against an adversary corrupting any strict subset of the parties. Our protocol is based on the recently introduced primitives: oblivious programmable PRF (OPPRF) and oblivious key-value store (OKVS). Our protocols follow the client-server model where each party is either a client or a server. However, in contrast to previous works where the client has to engage in an expensive interactive cryptographic protocol, our clients need only send a single key to each server and a single message to a {\em pivot} party (where message size is in the order of the set size). Our experiments show that the client&#x27;s load improves by up to $10 \times$ (compared to both semi-honest and malicious settings) and that factor increases with the number of parties. We implemented our protocol and conducted an extensive experiment over both LAN and WAN and up to 32 parties with up to $2^{20}$ items each. We provide a comparison of the performance of our protocol and the state-of-the-art for both the semi-honest setting (by Chandran et al.) and the malicious setting (by Ben Efraim et al. and Garimella et al.).

  匹配依据：MPC: private set intersection

  </details>

- **Generalized Pseudorandom Secret Sharing and Efficient Straggler-Resilient Secure Computation**
  2021-09-20 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-030-90453-1_5) · [IACR ePrint](https://eprint.iacr.org/2021/1223)
  Fabrice Benhamouda, Elette Boyle, Ariel Nof, Yuval Ishai, Niv Gilboa, Shai Halevi

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) enables $n$ parties, of which up to $t$ may be corrupted, to perform joint computations on their private inputs while revealing only the outputs. Optimizing the asymptotic and concrete costs of MPC protocols has become an important line of research. Much of this research focuses on the setting of an honest majority, where $n \ge 2t+1$, which gives rise to concretely efficient protocols that are either information-theoretic or make a black-box use of symmetric cryptography. Efficiency can be further improved in the case of a {\em strong} honest majority, where $n&gt;2t+1$. Motivated by the goal of minimizing the communication and latency costs of MPC with a strong honest majority, we make two related contributions. \begin{itemize}[leftmargin=*] \item {\bf Generalized pseudorandom secret sharing (PRSS).} Linear correlations serve as an important resource for MPC protocols and beyond. PRSS enables secure generation of many pseudorandom instances of such correlations without interaction, given replicated seeds of a pseudorandom function. We extend the PRSS technique of Cramer et al.\ (TCC 2015) for sharing degree-$d$ polynomials to new constructions leveraging a particular class of combinatorial designs. Our constructions yield a dramatic efficiency improvement when the degree $d$ is higher than the security threshold $t$, not only for standard degree-$d$ correlations but also for several useful generalizations. In particular, correlations for locally converting between slot configurations in ``share packing&#x27;&#x27; enable us to avoid the concrete overhead of prior works. \item {\bf Cheap straggler resilience.} In reality, communication is not fully synchronous: protocol executions suffer from variance in communication delays and occasional node or message-delivery failures. We explore the benefits of PRSS-based MPC with a strong honest majority toward robustness against such failures, in turn yielding improved latency delays. In doing so we develop a novel technique for defending against a subtle ``double-dipping&#x27;&#x27; attack, which applies to the best existing protocols, with almost no extra cost in communication or rounds. \end{itemize} Combining the above tools requires further work, including new methods for batch verification via distributed zero-knowledge proofs (Boneh et al., CRYPTO 2019) that apply to packed secret sharing. Overall, our work demonstrates new advantages of the strong honest majority setting, and introduces new tools---in particular, generalized PRSS---that we believe will be of independent use within other cryptographic applications.

  匹配依据：MPC: secret sharing, secure computation, secure multiparty computation

  </details>

- **On Actively-Secure Elementary MPC Reductions**
  2021-09-17 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-90459-3_24) · [IACR ePrint](https://eprint.iacr.org/2021/1208)
  Aarushi Goel, Benny Applebaum

  <details><summary>摘要 / Abstract</summary>

  We introduce the notion of \emph{elementary MPC} reductions that allow us to securely compute a functionality $f$ by making a single call to a constant-degree ``non-cryptographic&#x27;&#x27; functionality $g$ without requiring any additional interaction. Roughly speaking, ``non-cryptographic&#x27;&#x27; means that $g$ does not make use of cryptographic primitives, though the parties can locally call such primitives. Classical MPC results yield such elementary reductions in various cases including the setting of passive security with full corruption threshold $t&lt;n$ (Yao, FOCS&#x27;86; Beaver, Micali, and Rogaway, STOC&#x27;90), the setting of full active security against a corrupted minority $t&lt;n/2$ (Damgård and Ishai, Crypto&#x27;05), and, for NC1 functionalities, even for the setting of full active (information-theoretic) security with full corruption threshold of $t&lt;n$ (Ishai and Kushilevitz, FOCS&#x27;00). This leaves open the existence of an elementary reduction that achieves full active security in the dishonest majority setting for all efficiently computable functions. Our main result shows that such a reduction is unlikely to exist. Specifically, the existence of a computationally secure elementary reduction that makes black-box use of a PRG and achieves a very weak form of partial fairness (e.g., that holds only when the first party is not corrupted) would allow us to realize any efficiently-computable function by a \emph{constant-round} protocol that achieves a non-trivial notion of information-theoretic passive security. The existence of the latter is a well-known 3-decade old open problem in information-theoretic cryptography (Beaver, Micali, and Rogaway, STOC&#x27;90). On the positive side, we observe that this barrier can be bypassed under any of the following relaxations: (1) non-black-box use of a pseudorandom generator; (2) weaker security guarantees such as security with identifiable abort; or (3) an additional round of communication with the functionality $g$.

  匹配依据：MPC: mpc (context)

  </details>

- **On Communication-Efficient Asynchronous MPC with Adaptive Security**
  2021-09-14 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-030-90453-1_2) · [IACR ePrint](https://eprint.iacr.org/2021/1174)
  Martin Hirt, Chen-Da Liu-Zhang, Annick Chopard

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) allows a set of $n$ parties to jointly compute an arbitrary computation over their private inputs. Two main variants have been considered in the literature according to the underlying communication model. Synchronous MPC protocols proceed in rounds, and rely on the fact that the communication network provides strong delivery guarantees within each round. Asynchronous MPC protocols achieve security guarantees even when the network delay is arbitrary. While the problem of MPC has largely been studied in both variants with respect to both feasibility and efficiency results, there is still a substantial gap when it comes to communication complexity of adaptively secure protocols. Concretely, while adaptively secure synchronous MPC protocols with linear communication are known for a long time, the best asynchronous protocol communicates $\mathcal{O}(n^4 \kappa)$ bits per multiplication. In this paper, we make progress towards closing this gap by providing two protocols. First, we present an adaptively secure asynchronous protocol with optimal resilience $t&lt;n/3$ and $\mathcal{O}(n^2 \kappa)$ bits of communication per multiplication, improving over the state of the art protocols in this setting by a quadratic factor in the number of parties. The protocol has cryptographic security and follows the CDN approach [Eurocrypt&#x27;01], based on additive threshold homomorphic encryption. Second, we show an optimization of the above protocol that tolerates up to $t&lt;(1-\epsilon)n/3$ corruptions and communicates $\mathcal{O}(n\cdot \poly(\kappa))$ bits per multiplication under stronger assumptions.

  匹配依据：MPC: secure multi party computation

  </details>

- **Information-Theoretically Secure MPC against Mixed Dynamic Adversaries**
  2021-09-14 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-030-90459-3_20) · [IACR ePrint](https://eprint.iacr.org/2021/1163)
  Divya Ravi, Daniel Escudero, Ivan Damgård

  <details><summary>摘要 / Abstract</summary>

  In this work we consider information-theoretically secure MPC against a mixed adversary who can corrupt $t_p$ parties passively, $t_a$ parties actively, and can make $t_f$ parties fail-stop. With perfect security, it is known that every function can be computed securely if and only if $3t_a + 2t_p + t_f &lt; n$, and for statistical security the bound is $2t_a + 2t_p + t_f &lt; n$. These results say that for each given set of parameters $(t_a, t_p, t_f)$ respecting the inequality, there exists a protocol secure against this particular choice of corruption thresholds. In this work we consider a dynamic adversary. Here, the goal is a single protocol that is secure, no matter which set of corruption thresholds $(t_a, t_p, t_f)$ from a certain class is chosen by the adversary. A dynamic adversary can choose a corruption strategy after seeing the protocol and so is much stronger than a standard adversary. Dynamically secure protocols have been considered before for computational security. Also the information theoretic case has been studied, but only considering non-threshold general adversaries, leading to inefficient protocols. We consider threshold dynamic adversaries and information theoretic security. For statistical security we show that efficient dynamic secure function evaluation (SFE) is possible if and only if $2t_a + 2t_p + t_f &lt; n$, but any dynamically secure protocol must use $\Omega(n)$ rounds, even if only fairness is required. Further, general reactive MPC is possible if we assume in addition that $2t_a+2t_f \leq n$, but fair reactive MPC only requires $2t_a + 2t_p + t_f &lt; n$. For perfect security we show that both dynamic SFE and verifiable secret sharing (VSS) are impossible if we only assume $3t_a + 2t_p + t_f &lt; n$ and remain impossible even if we also assume $t_f=0$. On the other hand, perfect dynamic SFE with guaranteed output delivery (G.O.D.) is possible when either $t_p = 0$ or $t_a = 0$ i.e. if instead we assume $3t_a+t_f &lt; n$ or $2t_p +t_f &lt; n$. Further, perfect dynamic VSS with G.O.D. is possible under the additional conditions $3t_a + 3/2t_f \leq n$ or $2t_p + 2t_f \leq n$. These conditions are also sufficient for dynamic perfect reactive MPC.

  匹配依据：MPC: secret sharing, secure function evaluation

  </details>

- **Compact and Malicious Private Set Intersection for Small Sets**
  2021-09-14 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3460120.3484778) · [IACR ePrint](https://eprint.iacr.org/2021/1159)
  Ni Trieu, Mike Rosulek

  <details><summary>摘要 / Abstract</summary>

  We describe a protocol for two-party private set intersection (PSI) based on Diffie-Hellman key agreement. The protocol is proven secure against malicious parties, in the ideal permutation + random oracle model. For small sets (500 items or fewer), our protocol requires the least time and communication of any known PSI protocol, even ones that are only semi-honest secure and ones that are not based on Diffie-Hellman. It is one of the few significant improvements to the 20-year old classical Diffie-Hellman PSI protocol of Huberman, Franklin, and Hogg (ACM Elec. Commerce 1999). Our protocol is actually a generic transformation that constructs PSI from a class of key agreement protocols. This transformation is inspired by a technique of Cho, Dachman-Soled, and Jarecki (CT-RSA 2016), which we streamline and optimize in several important ways to achieve our superior efficiency.

  匹配依据：MPC: private set intersection

  </details>

- **Silver: Silent VOLE and Oblivious Transfer from Hardness of Decoding Structured LDPC Codes**
  2021-09-10 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-84252-9_17) · [IACR ePrint](https://eprint.iacr.org/2021/1150)
  Geoffroy Couteau, Peter Rindal, Srinivasan Raghuraman, COUTEAU Geoffroy

  <details><summary>摘要 / Abstract</summary>

  We put forth new protocols for oblivious transfer extension and vector OLE, called \emph{Silver}, for SILent Vole and oblivious transfER. Silver offers extremely high performances: generating 10 million random OTs on one core of a standard laptop requires only 300ms of computation and 122KB of communication. This represents 37% less computation and ~1300x less communication than the standard IKNP protocol, as well as ~4x less computation and ~4x less communication than the recent protocol of Yang et al. (CCS 2020). Silver is \emph{silent}: after a one-time cheap interaction, two parties can store small seeds, from which they can later \emph{locally} generate a large number of OTs \emph{while remaining offline}. Neither IKNP nor Yang et al. enjoys this feature; compared to the best known silent OT extension protocol of Boyle et al. (CCS 2019), upon which we build up, Silver has 19x less computation, and the same communication. Due to its attractive efficiency features, Silver yields major efficiency improvements in numerous MPC protocols. Our approach is a radical departure from the standard paradigm for building MPC protocols, in that we do \emph{not} attempt to base our constructions on a well-studied assumption. Rather, we follow an approach closer in spirit to the standard paradigm in the design of symmetric primitives: we identify a set of fundamental structural properties that allow us to withstand all known attacks, and put forth a candidate design, guided by our analysis. We also rely on extensive experimentations to analyze our candidate and experimentally validate their properties. In essence, our approach boils down to constructing new families of linear codes with (plausibly) high minimum distance and extremely low encoding time. While further analysis is of course warranted to confidently assess the security of Silver, we hope and believe that initiating this approach to the design of MPC primitives will pave the way to new secure primitives with extremely attractive efficiency features.

  匹配依据：MPC: oblivious transfer

  </details>

- **Round-Efficient Byzantine Agreement and Multi-Party Computation with Asynchronous Fallback**
  2021-09-10 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-90459-3_21) · [IACR ePrint](https://eprint.iacr.org/2021/1141)
  Martin Hirt, Chen-Da Liu-Zhang, Giovanni Deligios

  <details><summary>摘要 / Abstract</summary>

  Protocols for Byzantine agreement (BA) and secure multi-party computation (MPC) can be classified according to the underlying communication model. The two most commonly considered models are the synchronous one and the asynchronous one. Synchronous protocols typically lose their security guarantees as soon as the network violates the synchrony assumptions. Asynchronous protocols remain secure regardless of the network conditions, but achieve weaker security guarantees even when the network is synchronous. Recent works by Blum, Katz and Loss [TCC&#x27;19], and Blum, Liu-Zhang and Loss [CRYPTO&#x27;20] introduced BA and MPC protocols achieving security guarantees in both settings: security up to $t_s$ corruptions in a synchronous network, and up to $t_a$ corruptions in an asynchronous network, under the provably optimal threshold trade-offs $t_a \le t_s$ and $t_a + 2t_s &lt; n$. However, current solutions incur a high synchronous round complexity when compared to state-of-the-art purely synchronous protocols. When the network is synchronous, the round complexity of BA protocols is linear in the number of parties, and the round complexity of MPC protocols also depends linearly on the depth of the circuit to evaluate. In this work, we provide round-efficient constructions for both primitives with optimal resilience: fixed-round and expected constant-round BA protocols, and an MPC protocol whose round complexity is independent of the circuit depth.

  匹配依据：MPC: multi party computation, secure multi party computation

  </details>

- **Machine-checked ZKP for NP-relations: Formally Verified Security Proofs and Implementations of MPC-in-the-Head**
  2021-09-10 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2104.05516) · [ACM CCS](https://doi.org/10.1145/3460120.3484771) · [IACR ePrint](https://eprint.iacr.org/2021/1149)
  Karim M. El Defrawy, Hugo Pacheco, Vitor Pereira, Stéphane Lengrand, Manuel Barbosa, Manuel L. Correia, José Bacelar Almeida, José Carlos Bacelar Almeida, Karim Eldefrawy, Stéphane Graham-Lengrand, Manuel L Correia

  <details><summary>摘要 / Abstract</summary>

  MPC-in-the-Head (MitH) is a general framework that enables constructing efficient zero- knowledge (ZK) protocols for NP relations from secure multiparty computation (MPC) protocols. In this paper we present the first machine-checked implementations of this transformation. We begin with an EasyCrypt formalization that preserves modular structure of the original MitH construction and can be instantiated with arbitrary MPC protocols, secret sharing and commitment schemes satisfying standard notions of security. We then formalize various suitable components, which we use to obtain full-fledged ZK protocols for general relations. We compare two approaches for obtaining verified executable implementations. The first approach realizes a fully automated extraction from EasyCrypt to OCaml. The second one reduces the trusted computing base (TCB) and provides better performance for the extracted executable by combining code extraction with manual formal verification of low-level components implemented in the Jasmin language. We conclude the paper with a discussion of the trade-off between formal verification effort and performance, and also discuss how our approach opens the way for fully verified implementations of state-of the-art optimized protocols based on MitH.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Continuously Non-Malleable Secret Sharing: Joint Tampering, Plain Model and Capacity**
  2021-09-06 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-90453-1_12) · [IACR ePrint](https://eprint.iacr.org/2021/1128)
  Antonio Faonio, Gianluca Brian, Daniele Venturi

  <details><summary>摘要 / Abstract</summary>

  We study non-malleable secret sharing against joint leakage and joint tampering attacks. Our main result is the first threshold secret sharing scheme in the plain model achieving resilience to noisy-leakage and continuous tampering. The above holds under (necessary) minimal computational assumptions (i.e., the existence of one-to-one one-way functions), and in a model where the adversary commits to a fixed partition of all the shares into non-overlapping subsets of at most $t-1$ shares (where $t$ is the reconstruction threshold), and subsequently jointly leaks from and tampers with the shares within each partition. We also study the capacity (i.e., the maximum achievable asymptotic information rate) of continuously non-malleable secret sharing against joint continuous tampering attacks. In particular, we prove that whenever the attacker can tamper jointly with $k &gt; t/2$ shares, the capacity is at most $t - k$. The rate of our construction matches this upper bound. An important corollary of our results is the first non-malleable secret sharing scheme against independent tampering attacks breaking the rate-one barrier (under the same computational assumptions as above).

  匹配依据：MPC: secret sharing

  </details>

- **CrypTen: Secure Multi-Party Computation Meets Machine Learning**
  2021-09-02 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2109.00984) · [NeurIPS](https://proceedings.neurips.cc/paper/2021/hash/2754518221cfbc8d25c13a06a4cb8421-Abstract.html)
  Brian Knott, Awni Y. Hannun, Shubho Sengupta, Shobha Venkataraman, Mark Ibrahim, Laurens van der Maaten, Awni Hannun

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) allows parties to perform computations on data while keeping that data private. This capability has great potential for machine-learning applications: it facilitates training of machine-learning models on private data sets owned by different parties, evaluation of one party&#x27;s private model using another party&#x27;s private data, etc. Although a range of studies implement machine-learning models via secure MPC, such implementations are not yet mainstream. Adoption of secure MPC is hampered by the absence of flexible software frameworks that &quot;speak the language&quot; of machine-learning researchers and engineers. To foster adoption of secure MPC in machine learning, we present CrypTen: a software framework that exposes popular secure MPC primitives via abstractions that are common in modern machine-learning frameworks, such as tensor computations, automatic differentiation, and modular neural networks. This paper describes the design of CrypTen and measure its performance on state-of-the-art models for text classification, speech recognition, and image classification. Our benchmarks show that CrypTen&#x27;s GPU support and high-performance communication between (an arbitrary number of) parties allows it to perform efficient private evaluation of modern machine-learning models under a semi-honest threat model. For example, two parties using CrypTen can securely predict phonemes in speech recordings using Wav2Letter faster than real-time. We hope that CrypTen will spur adoption of secure MPC in the machine-learning community.

  匹配依据：MPC: secure multi party computation

  </details>

- **Efficient Information-Theoretic Multi-Party Computation over Non-Commutative Rings**
  2021-08-06 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-84245-1_12) · [IACR ePrint](https://eprint.iacr.org/2021/1025)
  Daniel Escudero, Eduardo Soria-Vazquez

  <details><summary>摘要 / Abstract</summary>

  We construct the first efficient MPC protocol that only requires black-box access to a non-commutative ring $R$. Previous results in the same setting were efficient only either for a constant number of corruptions or when computing branching programs and formulas. Our techniques are based on a generalization of Shamir&#x27;s secret sharing to non-commutative rings, which we derive from the work on Reed Solomon codes by Quintin, Barbier and Chabot (IEEE Transactions on Information Theory, 2013). When the center of the ring contains a set $A = \{\alpha_0, \ldots, \alpha_n\}$ such that $\forall i \neq j, \alpha_i - \alpha_j \in R^*$, the resulting secret sharing scheme is strongly multiplicative and we can generalize existing constructions over finite fields without much trouble. Most of our work is devoted to the case where the elements of $A$ do not commute with all of $R$, but they just commute with each other. For such rings, the secret sharing scheme cannot be linear ``on both sides&quot; and furthermore it is not multiplicative. Nevertheless, we are still able to build MPC protocols with a concretely efficient online phase and black-box access to $R$. As an example we consider the ring $\mathcal{M}_{m\times m}(\mathbb{Z}/2^k\mathbb{Z})$, for which when $m &gt; \log(n+1)$, we obtain protocols that require around $\lceil\log(n+1)\rceil/2$ less communication and $2\lceil\log(n+1)\rceil$ less computation than the state of the art protocol based on Circuit Amortization Friendly Encodings (Dalskov, Lee and Soria-Vazquez, ASIACRYPT 2020). In this setting with a ``less commutative&quot; $A$, our black-box preprocessing phase has a less practical complexity of $\poly(n)$. Due to this, we additionally provide specialized, concretely efficient preprocessing protocols for $R = \mathcal{M}_{m\times m}(\mathbb{Z}/2^k\mathbb{Z})$ that exploit the structure of the matrix ring.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Three-Round Secure Multiparty Computation from Black-Box Two-Round Oblivious Transfer**
  2021-07-22 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-84245-1_7) · [IACR ePrint](https://eprint.iacr.org/2021/957)
  Akshayaram Srinivasan, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  We give constructions of three-round secure multiparty computation (MPC) protocols for general functions that make black-box use of a two-round oblivious transfer. For the case of semi-honest adversaries, we make use of a two-round, semi-honest secure oblivious transfer in the plain model. This resolves the round-complexity of black-box (semi-honest) MPC protocols from minimal assumptions and answers an open question of Applebaum et al. (ITCS 2020). For the case of malicious adversaries, we make use of a two-round maliciously-secure oblivious transfer in the common random/reference string model that satisfies a (mild) variant of adaptive security for the receiver.

  匹配依据：MPC: oblivious transfer, secure multiparty computation

  </details>

- **Breaking the Circuit-Size Barrier for Secure Computation under Quasi-Polynomial LPN**
  2021-07-13 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-030-77886-6_29) · [IACR ePrint](https://eprint.iacr.org/2021/943)
  Geoffroy Couteau, Pierre Meyer

  <details><summary>摘要 / Abstract</summary>

  In this work we introduce a new (circuit-dependent) homomorphic secret sharing (HSS) scheme for any $\log/\log\log$-local circuit, with communication proportional only to the width of the circuit and polynomial computation, which is secure assuming the super-polynomial hardness of learning parity with noise (LPN). At the heart of our new construction is a pseudorandom correlation generator (PCG) which allows two parties to locally stretch short seeds into pseudorandom instances of an arbitrary $\log/\log\log$-local additive correlation. Our main application, and the motivation behind this work, is a generic two-party secure computation protocol for every layered (boolean or arithmetic) circuit of size $s$ with total communication $O(s/\log\log s)$ and polynomial computation, assuming the super-polynomial hardness of the standard learning parity with noise assumption (a circuit is layered if its nodes can be partitioned in layers, such that any wire connects adjacent layers). This expands the set of assumptions under which the `circuit-size barrier&#x27; can be broken, for a large class of circuits. The strength of the underlying assumption is tied to the sublinearity factor: we achieve communication $O(s/k(s))$ under the $s^{2^{k(s)}}$-hardness of LPN, for any $k(s) \leq (\log\log s) / 4$. Previously, the set of assumptions known to imply a PCG for correlations of degree $\omega(1)$ or generic secure computation protocols with sublinear communication was restricted to LWE, DDH, and a circularly secure variant of DCR.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **ROTed: Random Oblivious Transfer for embedded devices**
  2021-07-09 · MPC · 含会议/期刊记录 · [CHES](https://doi.org/10.46586/TCHES.V2021.I4.215-238) · [IACR ePrint](https://eprint.iacr.org/2021/935)
  Paulo Martins, Pedro Branco, Paulo Mateus, Luís Fiolhais, Manuel Goulão, Leonel Sousa

  <details><summary>摘要 / Abstract</summary>

  Oblivious Transfer (OT) is a fundamental primitive in cryptography, supporting protocols such as Multi-Party Computation and Private Set Intersection (PSI), that are used in applications like contact discovery, remote diagnosis and contact tracing. Due to its fundamental nature, it is utterly important that its execution is secure even if arbitrarily composed with other instances of the same, or other protocols. This property can be guaranteed by proving its security under the Universal Composability model. Herein, a 3-round Random Oblivious Transfer (ROT) protocol is proposed, which achieves high computational efficiency, in the Random Oracle Model. The security of the protocol is based on the Ring Learning With Errors assumption (for which no quantum solver is known). ROT is the basis for OT extensions and, thus, achieves wide applicability, without the overhead of compiling ROTs from OTs. Finally, the protocol is implemented in a server-class Intel processor and four application-class ARM processors, all with different architectures. The usage of vector instructions provides on average a 40% speedup. The implementation shows that our proposal is at least one order of magnitude faster than the state-of-the-art, and is suitable for a wide range of applications in embedded systems, IoT, desktop, and servers. From a memory footprint perspective, there is a small increase (16%) when compared to the state-of-the-art. This increase is marginal and should not prevent the usage of the proposed protocol in a multitude of devices. In sum, the proposal achieves up to 37k ROTs/s in an Intel server-class processor and up to 5k ROTs/s in an ARM application-class processor. A PSI application, using the proposed ROT, is up to 6.6 times faster than related art.

  匹配依据：MPC: multi party computation, oblivious transfer, private set intersection

  </details>

- **Traceable Secret Sharing and Applications**
  2021-06-29 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-030-84252-9_24) · [IACR ePrint](https://eprint.iacr.org/2021/871)
  Akshayaram Srinivasan, Vipul Goyal, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  Consider a scenario where Alice stores some secret data $s$ on $n$ servers using a $t$-out-of-$n$ secret sharing scheme. Trudy (the collector) is interested in the secret data of Alice and is willing to pay for it. Trudy publishes an advertisement on the internet which describes an elaborate cryptographic scheme to collect the shares from the $n$ servers. Each server who decides to submit its share is paid a hefty monetary reward and is guaranteed ``immunity&quot; from being caught or prosecuted in a court for violating its service agreement with Alice. Bob is one of the servers and sees this advertisement. On examining the collection scheme closely, Bob concludes that there is no way for Alice to prove anything in a court that he submitted his share. Indeed, if Bob is rational, he might use the cryptographic scheme in the advertisement and submit his share since there are no penalties and no fear of being caught and prosecuted. Can we design a secret sharing scheme which Alice can use to avoid such a scenario? We introduce a new primitive called as Traceable Secret Sharing to tackle this problem. In particular, a traceable secret sharing scheme guarantees that a cheating server always runs the risk of getting traced and prosecuted by providing a valid evidence (which can be examined in a court of law) implicating its dishonest behavior. We explore various definitional aspects and show how they are highly non-trivial to construct (even ignoring efficiency aspects). We then give an efficient construction of traceable secret sharing assuming the existence of a secure two-party computation protocol. We also show an application of this primitive in constructing traceable protocols for multi-server delegation of computation.

  匹配依据：MPC: secret sharing, secure two party computation

  </details>

- **Oblivious Key-Value Stores and Amplification for Private Set Intersection**
  2021-06-29 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-84245-1_14) · [IACR ePrint](https://eprint.iacr.org/2021/883)
  Ni Trieu, Avishay Yanai, Benny Pinkas, Gayathri Garimella, Mike Rosulek

  <details><summary>摘要 / Abstract</summary>

  Many recent private set intersection (PSI) protocols encode input sets as polynomials. We consider the more general notion of an oblivious key-value store (OKVS), which is a data structure that compactly represents a desired mapping $k_i \mapsto v_i$. When the $v_i$ values are random, the OKVS data structure hides the $k_i$ values that were used to generate it. The simplest (and size-optimal) OKVS is a polynomial $p$ that is chosen using interpolation such that $p(k_i)=v_i$. We initiate the formal study of oblivious key-value stores, and show new constructions resulting in the fastest OKVS to date. Similarly to cuckoo hashing, current analysis techniques are insufficient for finding {\em concrete} parameters to guarantee a small failure probability for our OKVS constructions. Moreover, it would cost too much to run experiments to validate a small upper bound on the failure probability. We therefore show novel techniques to amplify an OKVS construction which has a failure probability $p$, to an OKVS with a similar overhead and failure probability $p^c$. Setting $p$ to be moderately small enables to validate it by running a relatively small number of $O(1/p)$ experiments. This validates a $p^c$ failure probability for the amplified OKVS. Finally, we describe how OKVS can significantly improve the state of the art of essentially all variants of PSI. This leads to the fastest two-party PSI protocols to date, for both the semi-honest and the malicious settings. Specifically, in networks with moderate bandwidth (e.g., 30 - 300 Mbps) our malicious two-party PSI protocol has 40\% less communication and is 20-40\% faster than the previous state of the art protocol, even though the latter only has heuristic confidence.

  匹配依据：MPC: private set intersection

  </details>

- **MPC-Friendly Symmetric Cryptography from Alternating Moduli: Candidates, Protocols, and Applications**
  2021-06-29 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-030-84259-8_18) · [IACR ePrint](https://eprint.iacr.org/2021/885)
  Steven Goldfeder, Yuval Ishai, Mahimna Kelkar, Tzipora Halevi, Itai Dinur, Vivek Sharma, Gregory M. Zaverucha, Greg Zaverucha

  <details><summary>摘要 / Abstract</summary>

  We study new candidates for symmetric cryptographic primitives that leverage alternation between linear functions over $\mathbb{Z}_2$ and $\mathbb{Z}_3$ to support fast protocols for secure multiparty computation (MPC). This continues the study of weak pseudorandom functions of this kind initiated by Boneh et al. (TCC 2018) and Cheon et al. (PKC 2021). We make the following contributions. (Candidates). We propose new designs of symmetric primitives based on alternating moduli. These include candidate one-way functions, pseudorandom generators, and weak pseudorandom functions. We propose concrete parameters based on cryptanalysis. (Protocols). We provide a unified approach for securely evaluating modulus-alternating primitives in different MPC models. For the original candidate of Boneh et al., our protocols obtain at least 2x improvement in all performance measures. We report efficiency benchmarks of an optimized implementation. (Applications). We showcase the usefulness of our candidates for a variety of applications. This includes short &quot;Picnic-style&quot; signature schemes, as well as protocols for oblivious pseudorandom functions, hierarchical key derivation, and distributed key generation for function secret sharing.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **MAGE: Nearly Zero-Cost Virtual Memory for Secure Computation**
  2021-06-23 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2106.14651) · [OSDI](https://www.usenix.org/conference/osdi21/presentation/kumar)
  Sam Kumar, Raluca A. Popa, David E. Culler, Raluca Ada Popa

  <details><summary>摘要 / Abstract</summary>

  Secure Computation (SC) is a family of cryptographic primitives for computing on encrypted data in single-party and multi-party settings. SC is being increasingly adopted by industry for a variety of applications. A significant obstacle to using SC for practical applications is the memory overhead of the underlying cryptography. We develop MAGE, an execution engine for SC that efficiently runs SC computations that do not fit in memory. We observe that, due to their intended security guarantees, SC schemes are inherently oblivious -- their memory access patterns are independent of the input data. Using this property, MAGE calculates the memory access pattern ahead of time and uses it to produce a memory management plan. This formulation of memory management, which we call memory programming, is a generalization of paging that allows MAGE to provide a highly efficient virtual memory abstraction for SC. MAGE outperforms the OS virtual memory system by up to an order of magnitude, and in many cases, runs SC computations that do not fit in memory at nearly the same speed as if the underlying machines had unbounded physical memory to fit the entire computation.

  匹配依据：MPC: secure computation

  </details>

- **Environmentally Friendly Composable Multi-Party Computation in the Plain Model from Standard (Timed) Assumptions**
  2021-06-21 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-030-90459-3_25) · [IACR ePrint](https://eprint.iacr.org/2021/843)
  Jeremias Mechler, Brandon Broadnax, Jörn Müller-Quade

  <details><summary>摘要 / Abstract</summary>

  Starting with the work of Rivest et al. in 1996, timed assumptions have found many applications in cryptography, building e.g. the foundation of the blockchain technology. They also have been used in the context of classical MPC, e.g. to enable fairness. We follow this line of research to obtain composable generic MPC in the plain model. This approach comes with a major advantage regarding environmental friendliness, a property coined by Canetti et al. (FOCS 2013). Informally, this means that our constructions do not “hurt” game-based security properties of protocols that hold against polynomial-time adversaries when executed alone. As an additional property, they can be plugged into any UC-secure protocol without loss of security. Towards proving the security of our constructions, we introduce a variant of the UC security notion that captures timed cryptographic assumptions. Combining standard timed commitments and standard polynomial-time hardness assumptions, we construct a composable commitment scheme in the plain model. As this construction is constant-round and black-box, we obtain the first fully environmentally friendly composable constant-round black-box generic MPC protocol in the plain model from standard (timed) assumptions.

  匹配依据：MPC: multi party computation

  </details>

- **ATLAS: Efficient and Scalable MPC in the Honest Majority Setting**
  2021-06-21 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-84245-1_9) · [IACR ePrint](https://eprint.iacr.org/2021/833)
  Vipul Goyal, Hanjun Li, Rafail Ostrovsky, Yifan Song, Antigoni Polychroniadou

  <details><summary>摘要 / Abstract</summary>

  In this work, we address communication, computation, and round efficiency of unconditionally secure multi-party computation for arithmetic circuits in the honest majority setting. We achieve both algorithmic and practical improvements: -- The best known result in the semi-honest setting has been due to Damgard and Nielsen (CRYPTO 2007). Over the last decade, their construction has played an important role in the progress of efficient secure computation. However despite a number of follow-up works, any significant improvements to the basic semi-honest protocol have been hard to come by. We show 33% improvement in communication complexity of this protocol. We show how to generalize this result to the malicious setting, leading to the best known unconditional honest majority MPC with malicious security. -- We focus on the round complexity of the Damgard and Nielsen protocol and improve it by a factor of 2. Our improvement relies on a novel observation relating to an interplay between Damgard and Nielsen multiplication and Beaver triple multiplication. An implementation of our constructions shows an execution run time improvement compared to the state of the art ranging from 30% to 50%.

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **Three Halves Make a Whole? Beating the Half-Gates Lower Bound for Garbled Circuits**
  2021-06-07 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-84242-0_5) · [IACR ePrint](https://eprint.iacr.org/2021/749)
  Lawrence Roy, Mike Rosulek

  <details><summary>摘要 / Abstract</summary>

  We describe a garbling scheme for boolean circuits, in which XOR gates are free and AND gates require communication of $1.5\kappa + 5$ bits. This improves over the state-of-the-art &quot;half-gates&quot; scheme of Zahur, Rosulek, and Evans (Eurocrypt 2015), in which XOR gates are free and AND gates cost $2\kappa$ bits. The half-gates paper proved a lower bound of $2\kappa$ bits per AND gate, in a model that captured all known garbling techniques at the time. We bypass this lower bound with a novel technique that we call slicing and dicing, which involves slicing wire labels in half and operating separately on those halves. Ours is the first to bypass the lower bound while being fully compatible with free-XOR, making it a drop-in replacement for half-gates. Our construction is proven secure from a similar assumption to prior free-XOR garbling (circular correlation-robust hash), and uses only slightly more computation than half-gates.

  匹配依据：MPC: garbled circuits, garbling scheme

  </details>

- **Laconic Private Set Intersection and Applications**
  2021-06-02 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-030-90456-2_4) · [IACR ePrint](https://eprint.iacr.org/2021/728)
  Sihang Pu, Navid Alamati, Sanjam Garg, Pedro Branco, Nico Döttling, Mohammad Hajiabadi

  <details><summary>摘要 / Abstract</summary>

  Consider a server with a large set $S$ of strings $\{x_1,x_2, \dots,x_N\}$ that would like to publish a small hash $h$ of its set $S$ such that any client with a string $y$ can send the server a short message allowing it to learn $y$ if $y \in S$ and nothing otherwise. In this work, we study this problem of two-round private set intersection (PSI) with low (asymptotically optimal) communication cost, or what we call laconic private set intersection ($\ell$PSI) and its extensions. This problem is inspired by the recent general frameworks for laconic cryptography [Cho et al. CRYPTO 2017, Quach et al. FOCS&#x27;18]. We start by showing the first feasibility result for realizing $\ell$PSI based on the CDH assumption, or LWE with polynomial noise-to-modulus ratio. However, these feasibility results use expensive non-black-box cryptographic techniques leading to significant inefficiency. Next, with the goal of avoiding these inefficient techniques, we give a construction of $\ell$PSI schemes making only black-box use of cryptographic functions. Our construction is secure against semi-honest receivers, malicious senders and reusable in the sense that the receiver&#x27;s message can be reused across any number of executions of the protocol. The scheme is secure under the $\phi$-hiding, decisional composite residuosity and subgroup decision assumptions. Finally, we show natural applications of $\ell$PSI to realizing a semantically-secure encryption scheme that supports detection of encrypted messages belonging to a set of ``illegal&#x27;&#x27; messages (e.g., an illegal video) circulating online. Over the past few years, significant effort has gone into realizing laconic cryptographic protocols. Nonetheless, our work provides the first black-box constructions of such protocols for a natural application setting.

  匹配依据：MPC: private set intersection

  </details>

- **On Communication Models and Best-Achievable Security in Two-Round MPC**
  2021-05-28 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-030-90453-1_4) · [IACR ePrint](https://eprint.iacr.org/2021/690)
  Aarushi Goel, Rajeev Raghunath, Manoj Prabhakaran, Abhishek Jain

  <details><summary>摘要 / Abstract</summary>

  Recently, a sequence of works have made strong advances in two-round (i.e., round-optimal) secure multi-party computation (MPC). In the honest-majority setting -- the focus of this work -- Ananth et al. [CRYPTO&#x27;18, EC&#x27;19], Applebaum et al. [TCC&#x27;18, EC&#x27;19] and Garg et al. [TCC&#x27;18] have established the feasibility of general two-round MPC in standard communication models involving broadcast (BC) and private point-to-point (P2P) channels. In this work, we set out to understand what features of the communication model are necessary for these results, and more broadly the design of two-round MPC. Focusing our study on the plain model -- the most natural model for honest-majority MPC -- we obtain the following results: 1. Dishonest majority from Honest majority: In the two round setting, honest-majority MPC and dishonest-majority MPC are surprisingly close, and often equivalent. This follows from our results that the former implies 2-message oblivious transfer, in many settings. (i) We show that without private point-to-point (P2P) channels, i.e., when we use only broadcast (BC) channels, honest-majority MPC implies 2-message oblivious transfer. (ii) Furthermore, this implication holds even when we use both P2P and BC, provided that the MPC protocol is robust against ``fail-stop&#x27;&#x27; adversaries. 2. Best-Achievable Security: While security with guaranteed output delivery (and even fairness) against malicious adversaries is impossible in two rounds, nothing is known with regards to the ``next best&#x27;&#x27; security notion, namely, security with identifiable abort (IA). We show that IA is also impossible to achieve with honest-majority even if we use both P2P and BC channels. However, if we replace P2P channels with a ``bare&#x27;&#x27; (i.e., untrusted) public-key infrastructure (PKI), then even security with guaranteed output delivery (and hence IA) is possible to achieve. These results ``explain&#x27;&#x27; that the reliance on P2P channels (together with BC) in the recent two-round protocols in the plain model was in fact necessary, and that these protocols couldn&#x27;t have achieved a stronger security guarantee, namely, IA. Overall, our results (put together with prior works) fully determine the best-achievable security for honest-majority MPC in different communication models in two rounds. As a consequence, they yield the following hierarchy of communication models: BC &lt; P2P &lt; BC+P2P &lt; BC+PKI This shows that BC channel is the weakest communication model, and that BC+PKI model is strictly stronger than BC+PTP model.

  匹配依据：MPC: oblivious transfer, secure multi party computation

  </details>

- **Order-C Secure Multiparty Computation for Highly Repetitive Circuits**
  2021-04-19 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-030-77886-6_23) · [IACR ePrint](https://eprint.iacr.org/2021/500)
  Gabriel Kaptchuk, Aarushi Goel, Abhishek Jain, Gabrielle Beck

  <details><summary>摘要 / Abstract</summary>

  Running secure multiparty computation (MPC) protocols with hundreds or thousands of players would allow leveraging large volunteer networks (such as blockchains and Tor) and help justify honest majority assumptions. However, most existing protocols have at least a linear (multiplicative)dependence on the number of players, making scaling difficult. Known protocols with asymptotic efficiency independent of the number of parties (excluding additive factors) require expensive circuit transformations that induce large overheads. We observe that the circuits used in many important applications of MPC such as training algorithms used to create machine learning models have a highly repetitive structure. We formalize this class of circuits and propose an MPC protocol that achieves O(|C|) total complexity for this class. We implement our protocol and show that it is practical and outperforms O(n|C|) protocols for modest numbers of players.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Unbounded Multi-Party Computation from Learning with Errors**
  2021-04-06 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-77886-6_26) · [IACR ePrint](https://eprint.iacr.org/2021/431)
  Zhengzhong Jin, Giulio Malavolta, Prabhanjan Vijendra Ananth, Abhishek Jain, Prabhanjan Ananth

  <details><summary>摘要 / Abstract</summary>

  We consider the problem of round-optimal unbounded MPC: in the first round, parties publish a message that depends only on their input. In the second round, any subset of parties can jointly and securely compute any function $f$ over their inputs in a single round of broadcast. We do not impose any a-priori bound on the number of parties nor on the size of the functions that can be computed. Our main result is a semi-malicious two-round protocol for unbounded MPC in the plain model from the hardness of the standard learning with errors (LWE) problem. Prior work in the same setting assumes the hardness of problems over bilinear maps. Thus, our protocol is the first example of unbounded MPC that is post-quantum secure. The central ingredient of our protocol is a new scheme of attribute-based secure function evaluation (AB-SFE) with public decryption. Our construction combines techniques from the realm of homomorphic commitments with delegation of lattice basis. We believe that such a scheme may find further applications in the future.

  匹配依据：MPC: multi party computation, secure function evaluation

  </details>

- **Multiparty Reusable Non-Interactive Secure Computation from LWE**
  2021-03-22 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-77886-6_25) · [IACR ePrint](https://eprint.iacr.org/2021/378)
  Fabrice Benhamouda, Aayush Jain, Huijia Lin, Ilan Komargodski

  <details><summary>摘要 / Abstract</summary>

  Motivated by the goal of designing versatile and flexible secure computation protocols that at the same time require as little interaction as possible, we present new multiparty reusable Non-Interactive Secure Computation (mrNISC) protocols. This notion, recently introduced by Benhamouda and Lin (TCC 2020), is essentially two-round Multi-Party Computation (MPC) protocols where the first round of messages serves as a reusable commitment to the private inputs of participating parties. Using these commitments, any subset of parties can later compute any function of their choice on their respective inputs by just sending a single message to a stateless evaluator, conveying the result of the computation but nothing else. Importantly, the input commitments can be computed without knowing anything about other participating parties (neither their identities nor their number) and they are reusable across any number of desired computations. We give a construction of mrNISC that achieves standard simulation security, as classical multi-round MPC protocols achieve. Our construction relies on the Learning With Errors (LWE) assumption with polynomial modulus, and on the existence of a pseudorandom function (PRF) in $\mathsf{NC}^1$. We achieve semi-malicious security in the plain model and malicious security by further relying on trusted setup (which is unavoidable for mrNISC). In comparison, the only previously known constructions of mrNISC were either using bilinear maps or using strong primitives such as program obfuscation. We use our mrNISC to obtain new Multi-Key FHE (MKFHE) schemes with threshold decryption: $\bullet$ In the CRS model, we obtain threshold MKFHE for $\mathsf{NC}^1$ based on LWE with only $\textit{polynomial}$ modulus and PRFs in $\mathsf{NC}^1$, whereas all previous constructions rely on LWE with super-polynomial modulus-to-noise ratio. $\bullet$ In the plain model, we obtain threshold levelled MKFHE for $\mathsf{P}$ based on LWE with $\textit{polynomial}$ modulus, PRF in $\mathsf{NC}^1$, and NTRU, and another scheme for constant number of parties from LWE with sub-exponential modulus-to-noise ratio. The only known prior construction of threshold MKFHE (Ananth et al., TCC 2020) in the plain model restricts the set of parties who can compute together at the onset.

  匹配依据：MPC: multi party computation, secure computation

  </details>

- **Threshold Garbled Circuits and Ad Hoc Secure Computation**
  2021-03-09 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-030-77883-5_3) · [IACR ePrint](https://eprint.iacr.org/2021/308)
  Michele Ciampi, Vipul Goyal, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  Garbled Circuits (GCs) represent fundamental and powerful tools in cryptography, and many variants of GCs have been considered since their introduction. An important property of the garbled circuits is that they can be evaluated securely if and only if exactly 1 key for each input wire is obtained: no less and no more. In this work we study the case when: 1) some of the wire-keys are missing, but we are still interested in computing the output of the garbled circuit and 2) the evaluator of the GC might have both keys for a constant number of wires. We start to study this question in terms of non-interactive multi-party computation (NIMPC) which is strongly connected with GCs. In this notion there is a fixed number of parties ($n$) that can get correlated information from a trusted setup. Then these parties can send an encoding of their input to an evaluator, which can compute the output of the function. Similarly to the notion of ad hoc secure computation proposed by Beimel et al. [ITCS 2016], we consider the case when less than $n$ parties participate in the online phase, and in addition we let these parties colluding with the evaluator. We refer to this notion as Threshold NIMPC. In addition, we show that when the number of parties participating in the online phase is a fixed threshold $l\leq n$ then it is possible to securely evaluate any $l$-input function. We build our result on top of a new secret-sharing scheme (which can be of independent interest) and on the results proposed by Benhamouda, Krawczyk and Rabin [Crypto 2017]. Our protocol can be used to compute any function in NC1 in the information-theoretic setting and any function in $P$ assuming one-way functions. As a second (and main) contribution, we consider a slightly different notion of security in which the number of parties that can participate in the online phase is not specified, and can be any number $c$ above the threshold $l$ (in this case the evaluator cannot collude with the other parties). We solve an open question left open by Beimel, Ishai and Kushilevitz [Eurocrypt 2017] showing how to build a secure protocol for the case when $c$ is constant, under the Learning with Errors assumption.

  匹配依据：MPC: garbled circuit, garbled circuits, multi party computation, secret sharing, secure computation

  </details>

- **Quadratic Secret Sharing and Conditional Disclosure of Secrets**
  2021-03-07 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-030-84252-9_25) · [IACR ePrint](https://eprint.iacr.org/2021/285)
  Naty Peter, Hussien Othman, Amos Beimel

  <details><summary>摘要 / Abstract</summary>

  There is a huge gap between the upper and lower bounds on the share size of secret-sharing schemes for arbitrary $n$-party access structures, and consistent with our current knowledge the optimal share size can be anywhere between polynomial in $n$ and exponential in $n$. For linear secret-sharing schemes, we know that the share size for almost all $n$-party access structures must be exponential in $n$. Furthermore, most constructions of efficient secret-sharing schemes are linear. We would like to study larger classes of secret-sharing schemes with two goals. On one hand, we want to prove lower bounds for larger classes of secret-sharing schemes, possibly shedding some light on the share size of general secret-sharing schemes. On the other hand, we want to construct efficient secret-sharing schemes for access structures that do not have efficient linear secret-sharing schemes. Given this motivation, Paskin-Cherniavsky and Radune (ITC&#x27;20) defined and studied a new class of secret-sharing schemes in which the shares are generated by applying degree-$d$ polynomials to the secret and some random field elements. The special case $d=1$ corresponds to linear and multi-linear secret-sharing schemes. We define and study two additional classes of polynomial secret-sharing schemes: (1) schemes in which for every authorized set the reconstruction of the secret is done using polynomials and (2) schemes in which both sharing and reconstruction are done by polynomials. For linear secret-sharing schemes, schemes with linear sharing and schemes with linear reconstruction are equivalent. We give evidence that for polynomial secret-sharing schemes, schemes with polynomial sharing are probably stronger than schemes with polynomial reconstruction. We also prove lower bounds on the share size for schemes with polynomial reconstruction. On the positive side, we provide constructions of secret-sharing schemes and conditional disclosure of secrets (CDS) protocols with quadratic sharing and reconstruction. We extend a construction of Liu et al. (CRYPTO&#x27;17) and construct optimal quadratic $k$-server CDS protocols for functions $f:[N]^k\rightarrow \{0,\1}$ with message size $O(N^{(k-1)/3})$. We show how to transform our quadratic $k$-server CDS protocol to a robust CDS protocol, and use the robust CDS protocol to construct quadratic secret-sharing schemes for arbitrary access structures with share size $O(2^{0.705n})$; this is better than the best known share size of $O(2^{0.7576n})$ for linear secret-sharing schemes and worse than the best known share size of $O(2^{0.585n})$ for general secret-sharing schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Large Message Homomorphic Secret Sharing from DCR and Applications**
  2021-03-04 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-84252-9_23) · [IACR ePrint](https://eprint.iacr.org/2021/274)
  Lawrence Roy, Jaspal Singh

  <details><summary>摘要 / Abstract</summary>

  We present the first homomorphic secret sharing (HSS) construction that simultaneously (1) has negligible correctness error, (2) supports integers from an exponentially large range, and (3) relies on an assumption not known to imply FHE --- specifically, the Decisional Composite Residuosity (DCR) assumption. This resolves an open question posed by Boyle, Gilboa, and Ishai (Crypto 2016). Homomorphic secret sharing is analogous to fully-homomorphic encryption, except the ciphertexts are shared across two non-colluding evaluators. Previous constructions of HSS either had non-negligible correctness error and polynomial-size plaintext space or were based on the stronger LWE assumption. We also present two applications of our technique: a multi-server ORAM with constant bandwidth overhead, and a rate-1 trapdoor hash function with negligible error rate.

  匹配依据：MPC: secret sharing

  </details>

- **The Rise of Paillier: Homomorphic Secret Sharing and Public-Key Silent OT**
  2021-03-03 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-030-77870-5_24) · [IACR ePrint](https://eprint.iacr.org/2021/262)
  Sophia Yakoubov, Peter Scholl, Claudio Orlandi

  <details><summary>摘要 / Abstract</summary>

  We describe a simple method for solving the distributed discrete logarithm problem in Paillier groups, allowing two parties to locally convert multiplicative shares of a secret (in the exponent) into additive shares. Our algorithm is perfectly correct, unlike previous methods with an inverse polynomial error probability. We obtain the following applications and further results. - Homomorphic secret sharing. We construct homomorphic secret sharing for branching programs with *negligible* correctness error and supporting *exponentially large* plaintexts, with security based on the decisional composite residuosity (DCR) assumption. - Correlated pseudorandomness. Pseudorandom correlation functions (PCFs), recently introduced by Boyle et al. (FOCS 2020), allow two parties to obtain a practically unbounded quantity of correlated randomness, given a pair of short, correlated keys. We construct PCFs for the oblivious transfer (OT) and vector oblivious linear evaluation (VOLE) correlations, based on the quadratic residuosity (QR) or DCR assumptions, respectively. We also construct a pseudorandom correlation generator (for producing a bounded number of samples, all at once) for general degree-2 correlations including OLE, based on a combination of (DCR or QR) and the learning parity with noise assumptions. - Public-key silent OT/VOLE. We upgrade our PCF constructions to have a *public-key setup*, where after independently posting a public key, each party can locally derive its PCF key. This allows completely *silent generation* of an arbitrary amount of OTs or VOLEs, without any interaction beyond a PKI, based on QR, DCR, a CRS and a random oracle. The public-key setup is based on a novel non-interactive vector OLE protocol, which can be seen as a variant of the Bellare-Micali oblivious transfer protocol.

  匹配依据：MPC: oblivious transfer, secret sharing

  </details>

- **A Geometric Approach to Homomorphic Secret Sharing**
  2021-03-03 · MPC · 含会议/期刊记录 · [PKC](https://doi.org/10.1007/978-3-030-75248-4_4) · [IACR ePrint](https://eprint.iacr.org/2021/260)
  Yuval Ishai, Giulio Malavolta, Russell W. F. Lai

  <details><summary>摘要 / Abstract</summary>

  An (n,m,t)-homomorphic secret sharing (HSS) scheme allows n clients to share their inputs across m servers, such that the inputs are hidden from any t colluding servers, and moreover the servers can evaluate functions over the inputs locally by mapping their input shares to compact output shares. Such compactness makes HSS a useful building block for communication-efficient secure multi-party computation (MPC). In this work, we propose a simple compiler for HSS evaluating multivariate polynomials based on two building blocks: (1) homomorphic encryption for linear functions or low-degree polynomials, and (2) information-theoretic HSS for low-degree polynomials. Our compiler leverages the power of the first building block towards improving the parameters of the second. We use our compiler to generalize and improve on the HSS scheme of Lai, Malavolta, and Schröder [ASIACRYPT&#x27;18], which is only efficient when the number of servers is at most logarithmic in the security parameter. In contrast, we obtain efficient schemes for polynomials of higher degrees and an arbitrary number of servers. This application of our general compiler extends techniques that were developed in the context of information-theoretic private information retrieval (Woodruff and Yekhanin [CCC&#x27;05]), which use partial derivatives and Hermite interpolation to support the computation of polynomials of higher degrees. In addition to the above, we propose a new application of HSS to MPC with preprocessing. By pushing the computation of some HSS servers to a preprocessing phase, we obtain communication-efficient MPC protocols for low-degree polynomials that use fewer parties than previous protocols based on the same assumptions. The online communication of these protocols is linear in the input size, independently of the description size of the polynomial.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **YOSO: You Only Speak Once / Secure MPC with Stateless Ephemeral Roles**
  2021-03-02 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-030-84245-1_3) · [IACR ePrint](https://eprint.iacr.org/2021/210)
  Sophia Yakoubov, Bernardo Magri, Craig Gentry, Jesper Buus Nielsen, Tal Rabin, Shai Halevi, Hugo Krawczyk

  <details><summary>摘要 / Abstract</summary>

  The inherent difficulty of maintaining stateful environments over long periods of time gave rise to the paradigm of serverless computing, where mostly-stateless components are deployed on demand to handle computation tasks, and are teared down once their task is complete. Serverless architecture could offer the added benefit of improved resistance to targeted denial-of-service attacks, by hiding from the attacker the physical machines involved in the protocol until after they complete their work. Realizing such protection, however, requires that the protocol only uses stateless parties, where each party sends only one message and never needs to speaks again. Perhaps the most famous example of this style of protocols is the Nakamoto consensus protocol used in Bitcoin: A peer can win the right to produce the next block by running a local lottery (mining), all while staying covert. Once the right has been won, it is executed by sending a single message. After that, the physical entity never needs to send more messages. We refer to this as the You-Only-Speak-Once (YOSO) property, and initiate the formal study of it within a new model that we call the YOSO model. Our model is centered around the notion of roles, which are stateless parties that can only send a single message. Crucially, our modelling separates the protocol design, that only uses roles, from the role-assignment mechanism, that assigns roles to actual physical entities. This separation enables studying these two aspects separately, and our YOSO model in this work only deals with the protocol-design aspect. We describe several techniques for achieving YOSO MPC; both computational and information theoretic. Our protocols are synchronous and provide guaranteed output delivery (which is important for application domains such as blockchains), assuming honest majority of roles in every time step. We describe a practically efficient computationally-secure protocol, as well as a proof-of-concept information theoretically secure protocol.

  匹配依据：MPC: mpc (context)

  </details>

- **Generic Compiler for Publicly Verifiable Covert Multi-Party Computation**
  2021-03-02 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-030-77886-6_27) · [IACR ePrint](https://eprint.iacr.org/2021/251)
  Benjamin Schlosser, David Kretzler, Carmit Hazay, Sebastian Faust

  <details><summary>摘要 / Abstract</summary>

  Covert security has been introduced as a compromise between semi-honest and malicious security. In a nutshell, covert security guarantees that malicious behavior can be detected by the honest parties with some probability, but in case detection fails all bets are off. While the security guarantee offered by covert security is weaker than full-fledged malicious security, it comes with significantly improved efficiency. An important extension of covert security introduced by Asharov and Orlandi (ASIACRYPT&#x27;12) is public verifiability, which allows the honest parties to create a publicly verifiable certificate of malicious behavior. Public verifiability significantly strengthen covert security as the certificate allows punishment via an external party, e.g., a judge. Most previous work on publicly verifiable covert (PVC) security focuses on the two-party case, and the multi-party case has mostly been neglected. In this work, we introduce a novel compiler for multi-party PVC secure protocols. Our compiler leverages time-lock encryption to offer high probability of cheating detection (often also called deterrence factor) independent of the number of involved parties. Moreover, in contrast to the only earlier work that studies PVC in the multi-party setting (CRYPTO&#x27;20), we provide the first full formal security analysis.

  匹配依据：MPC: multi party computation

  </details>

- **Leakage-resilience of the Shamir Secret-sharing Scheme against Physical-bit Leakages**
  2021-02-20 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-030-77886-6_12) · [IACR ePrint](https://eprint.iacr.org/2021/186)
  Hai H. Nguyen, Tom Suad, Mingyuan Wang, Hemanta K. Maji, Anat Paskin-Cherniavsky

  <details><summary>摘要 / Abstract</summary>

  Efficient Reed-Solomon code reconstruction algorithms, for example, by Guruswami and Wootters (STOC--2016), translate into local leakage attacks on Shamir secret-sharing schemes over characteristic-2 fields. However, Benhamouda, Degwekar, Ishai, and Rabin (CRYPTO--2018) showed that the Shamir secret sharing scheme over prime-fields is leakage resilient to one-bit local leakage if the reconstruction threshold is roughly 0.87 times the total number of parties. In several application scenarios, like secure multi-party multiplication, the reconstruction threshold must be at most half the number of parties. Furthermore, the number of leakage bits that the Shamir secret sharing scheme is resilient to is also unclear. Towards this objective, we study the Shamir secret-sharing scheme&#x27;s leakage-resilience over a prime-field $F$. The parties&#x27; secret-shares, which are elements in the finite field $F$, are naturally represented as $\lambda$-bit binary strings representing the elements $\{0,1,\dotsc,p-1\}$. In our leakage model, the adversary can independently probe $m$ bit-locations from each secret share. The inspiration for considering this leakage model stems from the impact that the study of oblivious transfer combiners had on general correlation extraction algorithms, and the significant influence of protecting circuits from probing attacks has on leakage-resilient secure computation. Consider arbitrary reconstruction threshold $k\geq 2$, physical bit-leakage parameter $m\geq 1$, and the number of parties $n\geq 1$. We prove that Shamir&#x27;s secret-sharing scheme with random evaluation places is leakage-resilient with high probability when the order of the field $F$ is sufficiently large; ignoring polylogarithmic factors, one needs to ensure that $\log \abs F \geq n/k$. Our result, excluding polylogarithmic factors, states that Shamir&#x27;s scheme is secure as long as the total amount of leakage $m\cdot n$ is less than the entropy $k\cdot\lambda$ introduced by the Shamir secret-sharing scheme. Note that our result holds even for small constant values of the reconstruction threshold $k$, which is essential to several application scenarios. To complement this positive result, we present a physical-bit leakage attack for $m=1$ physical bit-leakage from $n=k$ secret shares and any prime-field $F$ satisfying $\abs F=1\mod k$. In particular, there are (roughly) $\abs F^{n-k+1}$ such vulnerable choices for the $n$-tuple of evaluation places. We lower-bound the advantage of this attack for small values of the reconstruction threshold, like $k=2$ and $k=3$, and any $\abs F=1\mod k$. In general, we present a formula calculating our attack&#x27;s advantage for every $k$ as $\abs F\rightarrow\infty.$ Technically, our positive result relies on Fourier analysis, analytic properties of proper rank-$r$ generalized arithmetic progressions, and Bézout&#x27;s theorem to bound the number of solutions to an equation over finite fields. The analysis of our attack relies on determining the ``discrepancy&#x27;&#x27; of the Irwin-Hall distribution. A probability distribution&#x27;s discrepancy is a new property of distributions that our work introduces, which is of potential independent interest.

  匹配依据：MPC: oblivious transfer, secret sharing, secure computation

  </details>

- **Privacy-Preserving Feature Selection with Secure Multiparty Computation**
  2021-02-06 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2102.03517) · [ICML](http://proceedings.mlr.press/v139/li21e.html) · [IACR ePrint](https://eprint.iacr.org/2021/132)
  Rafael Dowsley, Xiling Li, Martine De Cock

  <details><summary>摘要 / Abstract</summary>

  Existing work on privacy-preserving machine learning with Secure Multiparty Computation (MPC) is almost exclusively focused on model training and on inference with trained models, thereby overlooking the important data pre-processing stage. In this work, we propose the first MPC based protocol for private feature selection based on the filter method, which is independent of model training, and can be used in combination with any MPC protocol to rank features. We propose an efficient feature scoring protocol based on Gini impurity to this end. To demonstrate the feasibility of our approach for practical data science, we perform experiments with the proposed MPC protocols for feature selection in a commonly used machine-learning-as-a-service configuration where computations are outsourced to multiple servers, with semi-honest and with malicious adversaries. Regarding effectiveness, we show that secure feature selection with the proposed protocols improves the accuracy of classifiers on a variety of real-world data sets, without leaking information about the feature values or even which features were selected. Regarding efficiency, we document runtimes ranging from several seconds to an hour for our protocols to finish, depending on the size of the data set and the security settings.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Large Scale, Actively Secure Computation from LPN and Free-XOR Garbled Circuits**
  2021-02-05 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-77883-5_2) · [IACR ePrint](https://eprint.iacr.org/2021/120)
  Kelong Cong, Eduardo Soria-Vazquez, Aner Ben-Efraim, Emmanuela Orsini, Eran Omri, Nigel P. Smart

  <details><summary>摘要 / Abstract</summary>

  We present a secure multiparty computation (MPC) protocol based on garbled circuits which is both actively secure and supports the free-XOR technique, and which has communication complexity $O(n)$ per party. This improves on a protocol of Ben-Efraim, Lindell and Omri which only achieved passive security, without support for free-XOR. Our construction is based on a new variant of LPN-based encryption, but has the drawback of requiring a rather expensive garbling phase. To address this issue we present a second protocol that assumes at least $n/c$ of the parties are honest (for an arbitrary fixed value $c$). This second protocol allows for a significantly lighter preprocessing, at the cost of a small sacrifice in online efficiency. We demonstrate the practicality of our evaluation phase with a implementation.

  匹配依据：MPC: garbled circuits, secure computation, secure multiparty computation

  </details>

- **Upslices, Downslices, and Secret-Sharing with Complexity of 1.5n.**
  2021 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-84252-9_21)
  Oded Nir, Benny Applebaum

- **Unconditionally Secure Computation Against Low-Complexity Leakage.**
  2021 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-021-09402-2)
  Akshayaram Srinivasan, Andrej Bogdanov, Yuval Ishai

- **Senate: A Maliciously-Secure MPC Platform for Collaborative Analytics**
  2021 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2010.13752) · [USENIX Security](https://www.usenix.org/conference/usenixsecurity21/presentation/poddar) · [IACR ePrint](https://eprint.iacr.org/2020/1350)
  Avishay Yanai, Sukrit Kalra, Ryan Deng, Rishabh Poddar, Raluca A. Popa, Joseph M. Hellerstein, Raluca Ada Popa

  <details><summary>摘要 / Abstract</summary>

  Many organizations stand to benefit from pooling their data together in order to draw mutually beneficial insights -- e.g., for fraud detection across banks, better medical studies across hospitals, etc. However, such organizations are often prevented from sharing their data with each other by privacy concerns, regulatory hurdles, or business competition. We present Senate, a system that allows multiple parties to collaboratively run analytical SQL queries without revealing their individual data to each other. Unlike prior works on secure multi-party computation (MPC) that assume that all parties are semi-honest, Senate protects the data even in the presence of malicious adversaries. At the heart of Senate lies a new MPC decomposition protocol that decomposes the cryptographic MPC computation into smaller units, some of which can be executed by subsets of parties and in parallel, while preserving its security guarantees. Senate then provides a new query planning algorithm that decomposes and plans the cryptographic computation effectively, achieving a performance of up to 145$\times$ faster than the state-of-the-art.

  匹配依据：MPC: secure multi party computation

  </details>

- **Secure Secret Sharing Enabled b-band Mini Vaults Bio-Cryptosystem for Vectorial Biometrics.**
  2021 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2018.2874245)
  Yen-Lung Lai, Soohyong Kim, Jung Yeon Hwang, Zhe Jin, Sangrae Cho, Andrew Beng Jin Teoh

- **Secure Multi-party Computation of Differentially Private Heavy Hitters.**
  2021 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3460120.3484557)
  Jonas Böhler, Florian Kerschbaum

- **Secure Computation from One-Way Noisy Communication, or: Anti-correlation via Anti-concentration.**
  2021 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-030-84245-1_5)
  Yuval Ishai, Manoj Prabhakaran, Varun Narayanan, Vinod M. Prabhakaran, Shweta Agrawal, Eyal Kushilevitz, Alon Rosen

- **Round-Optimal Secure Multi-party Computation.**
  2021 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-021-09382-3)
  Antigoni Polychroniadou, Carmit Hazay, Shai Halevi, Muthuramakrishnan Venkitasubramaniam

- **Private Set Intersection With Authorization Over Outsourced Encrypted Datasets.**
  2021 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2021.3101059)
  Willy Susilo, Yuanhao Wang, Sha Ma, Qiong Huang, Meiyan Xiao, Hongbo Li

- **Post-Quantum Multi-Party Computation**
  2021 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2005.12904) · [EUROCRYPT](https://doi.org/10.1007/978-3-030-77870-5_16) · [IACR ePrint](https://eprint.iacr.org/2020/1395)
  Giulio Malavolta, James Bartusek, Vipul Goyal, Amit Agarwal, Dakshita Khurana

  <details><summary>摘要 / Abstract</summary>

  We initiate the study of multi-party computation for classical functionalities (in the plain model) with security against malicious polynomial-time quantum adversaries. We observe that existing techniques readily give a polynomial-round protocol, but our main result is a construction of *constant-round* post-quantum multi-party computation. We assume mildly super-polynomial quantum hardness of learning with errors (LWE), and polynomial quantum hardness of an LWE-based circular security assumption. Along the way, we develop the following cryptographic primitives that may be of independent interest: 1. A spooky encryption scheme for relations computable by quantum circuits, from the quantum hardness of an LWE-based circular security assumption. This yields the first quantum multi-key fully-homomorphic encryption scheme with classical keys. 2. Constant-round zero-knowledge secure against multiple parallel quantum verifiers from spooky encryption for relations computable by quantum circuits. To enable this, we develop a new straight-line non-black-box simulation technique against *parallel* verifiers that does not clone the adversary&#x27;s state. This forms the heart of our technical contribution and may also be relevant to the classical setting. 3. A constant-round post-quantum non-malleable commitment scheme, from the mildly super-polynomial quantum hardness of LWE.

  匹配依据：MPC: multi party computation

  </details>

- **One-Way Functions Imply Secure Computation in a Quantum World**
  2021 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2011.13486) · [series/lncs](https://doi.org/10.1007/978-3-030-84242-0_17) · [IACR ePrint](https://eprint.iacr.org/2020/1487)
  Fermi Ma, James Bartusek, Andrea Coladangelo, Dakshita Khurana

  <details><summary>摘要 / Abstract</summary>

  We prove that quantum-hard one-way functions imply simulation-secure quantum oblivious transfer (QOT), which is known to suffice for secure computation of arbitrary quantum functionalities. Furthermore, our construction only makes black-box use of the quantum-hard one-way function. Our primary technical contribution is a construction of extractable and equivocal quantum bit commitments based on the black-box use of quantum-hard one-way functions in the standard model. Instantiating the Crépeau-Kilian (FOCS 1988) framework with these commitments yields simulation-secure QOT.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **On the Local Leakage Resilience of Linear Secret Sharing Schemes.**
  2021 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-021-09375-2)
  Akshay Degwekar, Yuval Ishai, Fabrice Benhamouda, Tal Rabin

- **On the Exact Round Complexity of Secure Three-Party Computation.**
  2021 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-021-09404-0)
  Divya Ravi, Arpita Patra

- **On Abelian and Homomorphic Secret Sharing Schemes.**
  2021 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-021-09410-2)
  Shahram Khazaei, Amir Jafari

- **Oblivious Transfer is in MiniQCrypt**
  2021 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2011.14980) · [series/lncs](https://doi.org/10.1007/978-3-030-77886-6_18) · [IACR ePrint](https://eprint.iacr.org/2020/1500)
  Alex Bredariol Grilo, Huijia Lin, Fang Song, Vinod Vaikuntanathan, Alex B. Grilo

  <details><summary>摘要 / Abstract</summary>

  MiniQCrypt is a world where quantum-secure one-way functions exist, and quantum communication is possible. We construct an oblivious transfer (OT) protocol in MiniQCrypt that achieves simulation-security in the plain model against malicious quantum polynomial-time adversaries, building on the foundational work of Bennett, Brassard, Crépeau and Skubiszewska (CRYPTO 1991). Combining the OT protocol with prior works, we obtain secure two-party and multi-party computation protocols also in MiniQCrypt. This is in contrast to the classical world, where it is widely believed that one-way functions alone do not give us OT. In the common random string model, we achieve a constant-round universally composable (UC) OT protocol.

  匹配依据：MPC: multi party computation, oblivious transfer

  </details>

- **Non-interactive Secure Multiparty Computation for Symmetric Functions, Revisited: More Efficient Constructions and Extensions.**
  2021 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-84245-1_11)
  Shota Yamada, Kazuma Ohara, Reo Eriguchi, Koji Nuida

- **Multi-Party Threshold Private Set Intersection with Sublinear Communication**
  2021 · MPC · 含会议/期刊记录 · [PKC](https://doi.org/10.1007/978-3-030-75248-4_13) · [IACR ePrint](https://eprint.iacr.org/2020/600)
  Peihan Miao, Srinivasan Raghuraman, Peter Rindal, Saikrishna Badrinarayanan

  <details><summary>摘要 / Abstract</summary>

  In multi-party threshold private set intersection (PSI), $n$ parties each with a private set wish to compute the intersection of their sets if the intersection is sufficiently large. Previously, Ghosh and Simkin (CRYPTO 2019) studied this problem for the two-party case and demonstrated interesting lower and upper bounds on the communication complexity. In this work, we investigate the communication complexity of the multi-party setting $(n\geq 2)$. We consider two functionalities for multi-party threshold PSI. In the first, parties learn the intersection if each of their sets and the intersection differ by at most $T$. In the second functionality, parties learn the intersection if the union of all their sets and the intersection differ by at most $T$. For both functionalities, we show that any protocol must have communication complexity $\Omega(nT)$. We build protocols with a matching upper bound of $O(nT)$ communication complexity for both functionalities assuming threshold FHE. We also construct a computationally more efficient protocol for the second functionality with communication complexity $\widetilde{O}(nT)$ under a weaker assumption of threshold additive homomorphic encryption. As a direct implication, we solve one of the open problems in the work of Ghosh and Simkin (CRYPTO 2019) by designing a two-party protocol with communication cost $\widetilde{O}(T)$ from assumptions weaker than FHE. As a consequence of our results, we achieve the first ``regular&#x27;&#x27; multi-party PSI protocol where the communication complexity only grows with the size of the set difference and does not depend on the size of the input sets.

  匹配依据：MPC: private set intersection

  </details>

- **More than a Fair Share: Network Data Remanence Attacks against Secret Sharing-based Schemes.**
  2021 · MPC · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/more-than-a-fair-share-network-data-remanence-attacks-against-secret-sharing-based-schemes/)
  Alexander James, Hamed Okhravi, Samuel Jero, Daniel Kostecki, Anthony Peterson, Leila Rashidi, Reihaneh Safavi-Naini, Majid Ghaderi, Cristina Nita-Rotaru

- **High-Performance Multi-party Computation for Binary Circuits Based on Oblivious Transfer.**
  2021 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-021-09403-1)
  Sai Sheshank Burra, Peter Scholl, Enrique Larraia, Jesper Buus Nielsen, Emmanuela Orsini, Peter Sebastian Nordholt, Claudio Orlandi, Nigel P. Smart

- **Fuzzy Labeled Private Set Intersection with Applications to Private Real-Time Biometric Search.**
  2021 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity21/presentation/uzun)
  Wenke Lee, Alexandra Boldyreva, Simon P. Chung, Vladimir Kolesnikov, Erkam Uzun

- **Function Secret Sharing for Mixed-Mode and Fixed-Point Secure Computation**
  2021 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-77886-6_30) · [IACR ePrint](https://eprint.iacr.org/2020/1392)
  Yuval Ishai, Elette Boyle, Mayank, Niv Gilboa, Nishanth Chandran, Divya Gupta, Nishant Kumar, Mayank Rathee

  <details><summary>摘要 / Abstract</summary>

  Boyle et al. (TCC 2019) proposed a new approach for secure computation in the preprocessing model building on function secret sharing (FSS), where a gate $g$ is evaluated using an FSS scheme for the related offset family $g_r(x)=g(x+r)$. They further presented efficient FSS schemes based on any pseudorandom generator (PRG) for the offset families of several useful gates $g$ that arise in &quot;mixed-mode&#x27;&#x27; secure computation. These include gates for zero test, integer comparison, ReLU, and spline functions. The FSS-based approach offers significant savings in online communication and round complexity compared to alternative techniques based on garbled circuits or secret sharing. In this work, we improve and extend the previous results of Boyle et al. by making the following three kinds of contributions: - Improved Key Size: The preprocessing and storage costs of the FSS-based approach directly depend on the FSS key size. We improve the key size of previous constructions through two steps. First, we obtain roughly 4x reduction in key size for Distributed Comparison Function (DCF), i.e., FSS for the family of functions $f^&lt;_a_,_b(x)$ that output $b$ if $x &lt; a$ and $0$ otherwise. DCF serves as a central building block in the constructions of Boyle et al. Second, we improve the number of DCF instances required for realizing useful gates $g$. For example, whereas previous FSS schemes for ReLU and $m$-piece spline required 2 and $2m$ DCF instances, respectively, ours require only a single instance of DCF in both cases. This improves the FSS key size by 6-22x for commonly used gates such as ReLU and sigmoid. - New Gates: We present the first PRG-based FSS schemes for arithmetic and logical shift gates, as well as for bit-decomposition where both the input and outputs are shared over $Z_N$ for $N = 2^n$. These gates are crucial for many applications related to fixed-point arithmetic and machine learning. - A Barrier: The above results enable a 2-round PRG-based secure evaluation of &quot;multiply-then-truncate,&#x27;&#x27; a central operation in fixed-point arithmetic, by sequentially invoking FSS schemes for multiplication and shift. We identify a barrier to obtaining a 1-round implementation via a single FSS scheme, showing that this would require settling a major open problem in the area of FSS: namely, a PRG-based FSS for the class of bit-conjunction functions.

  匹配依据：MPC: garbled circuits, secret sharing, secure computation, secure evaluation

  </details>

- **Framing in Secret Sharing.**
  2021 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2021.3067468)
  Songbao Mo, Arkadii M. Slinko, Yvo Desmedt

- **Fortified Multi-Party Computation: Taking Advantage of Simple Secure Hardware Modules.**
  2021 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.2478/POPETS-2021-0072)
  Matthias Nagel, Brandon Broadnax, Jeremias Mechler, Tobias Müller, Jörn Müller-Quade, Alexander Koch

- **Fluid MPC: Secure Multiparty Computation with Dynamic Participants**
  2021 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-030-84245-1_4) · [IACR ePrint](https://eprint.iacr.org/2020/754)
  Aarushi Goel, Gabriel Kaptchuk, Arka Rai Choudhuri, Abhishek Jain, Matthew Green

  <details><summary>摘要 / Abstract</summary>

  Existing approaches to secure multiparty computation (MPC) require all the participants to commit to the entire duration of the protocol. As interest in MPC continues to grow, it is inevitable that there will be a desire to use it to evaluate increasingly complex functionalities on massive datasets, resulting in computations spanning several hours or days. Such scenarios call for a dynamic participation model for MPC where participants have the flexibility to go offline as needed and (re)join when they have available computational resources. Such a model would also democratize access to privacy-preserving computation by facilitating an ``MPC-as-a-service&#x27;&#x27; paradigm --- the deployment of MPC in volunteer-operated networks that perform computation on behalf of clients. In this work, we initiate the study of ``fluid MPC&#x27;&#x27;, where parties can dynamically join and leave the computation. The minimum commitment required from each participant is referred to as ``fluidity&#x27;&#x27;, measured in the number of rounds of communication that it must stay online. Our contributions are threefold: 1) We provide a formal treatment of fluid MPC, exploring various possible modeling choices. 2) We construct information-theoretic fluid MPC protocols in the honest-majority setting. Our protocols achieve ``maximal fluidity&#x27;&#x27;, meaning that a party can exit the computation after receiving and sending messages in one round. 3) We implement our protocol and test it in multiple network settings.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Fantastic Four: Honest-Majority Four-Party Secure Computation With Malicious Security**
  2021 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity21/presentation/dalskov) · [IACR ePrint](https://eprint.iacr.org/2020/1330)
  Daniel Escudero, Anders P. K. Dalskov, Marcel Keller, Anders Dalskov

  <details><summary>摘要 / Abstract</summary>

  In this work we introduce a novel four-party honest-majority MPC protocol with active security that achieves comparable efficiency to equivalent protocols in the same setting, while having a much simpler design and not relying on function-dependent preprocessing. Our initial protocol satisfies security with abort, but we present some extensions to achieve guaranteed output delivery. Unlike previous works, we do not achieve this by delegating the computation to one single party that is identified to be honest, which is likely to hinder the adoption of these technologies as it centralizes sensitive data. Instead, our novel approach guarantees termination of the protocol while ensuring that no single party (honest or corrupt) learns anything beyond the output. We implement our four-party protocol with abort in the MP-SPDZ framework for multiparty computation and benchmark multiple applications like MNIST classification training and ImageNet inference. Our results show that our four-party protocol performs similarly to an efficient honest-majority three-party protocol that only provides semi-honest/passive security, which suggest that adding a fourth party can be an effective method to achieve active security without harming performance.

  匹配依据：MPC: multiparty computation, secure computation

  </details>

- **Efficient Server-Aided Secure Two-Party Computation in Heterogeneous Mobile Cloud Computing.**
  2021 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2020.2966632)
  Zoe Lin Jiang, Qian Chen, Willy Susilo, Xuan Wang, Guomin Yang, Peng Xu, Yulin Wu

- **Constructing Locally Leakage-resilient Linear Secret-sharing Schemes**
  2021 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-030-84252-9_26) · [IACR ePrint](https://eprint.iacr.org/2020/1517)
  Mingyuan Wang, Tom Suad, Hemanta K. Maji, Anat Paskin-Cherniavsky, Hemanta Maji

  <details><summary>摘要 / Abstract</summary>

  Innovative side-channel attacks have repeatedly falsified the assumption that cryptographic implementations are opaque black-boxes. Therefore, it is essential to ensure cryptographic constructions&#x27; security even when information leaks via unforeseen avenues. One such fundamental cryptographic primitive is the secret-sharing schemes, which underlies nearly all threshold cryptography. Our understanding of the leakage-resilience of secret-sharing schemes is still in its preliminary stage. This work studies locally leakage-resilient linear secret-sharing schemes. An adversary can leak $m$ bits of arbitrary local leakage from each $n$ secret shares. However, in a locally leakage-resilient secret-sharing scheme, the leakage&#x27;s joint distribution reveals no additional information about the secret. For every constant $m$, we prove that the Massey secret-sharing scheme corresponding to a random linear code of dimension $k$ (over sufficiently large prime fields) is locally leakage-resilient, where $k/n &gt; 1/2$ is a constant. The previous best construction by Benhamouda, Degwekar, Ishai, Rabin (CRYPTO--2018) needed $k/n &gt; 0.907$. A technical challenge arises because the number of all possible $m$-bit local leakage functions is exponentially larger than the number of random linear codes. Our technical innovation begins with identifying an appropriate pseudorandomness-inspired family of tests; passing them suffices to ensure leakage-resilience. We show that most linear codes pass all tests in this family. This Monte-Carlo construction of linear secret-sharing scheme that is locally leakage-resilient has applications to leakage-resilient secure computation. Furthermore, we highlight a crucial bottleneck for all the analytical approaches in this line of work. Benhamouda et al. introduced an analytical proxy to study the leakage-resilience of secret-sharing schemes; if the proxy is small, then the scheme is leakage-resilient. However, we present a one-bit local leakage function demonstrating that the converse is false, motivating the need for new analytically well-behaved functions that capture leakage-resilience more accurately. Technically, the analysis involves probabilistic and combinatorial techniques and (discrete) Fourier analysis. The family of new ``tests&#x27;&#x27; capturing local leakage functions, we believe, is of independent and broader interest.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Constant-Overhead Unconditionally Secure Multiparty Computation over Binary Fields**
  2021 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-030-77886-6_28) · [IACR ePrint](https://eprint.iacr.org/2020/1412)
  Yifan Song, Antigoni Polychroniadou

  <details><summary>摘要 / Abstract</summary>

  We study the communication complexity of unconditionally secure multiparty computation (MPC) protocols in the honest majority setting. Despite tremendous efforts in achieving efficient protocols for binary fields under computational assumptions, there are no efficient unconditional MPC protocols in this setting. In particular, there are no $n$-party protocols with constant overhead admitting communication complexity of $O(n)$ bits per gate. Cascudo, Cramer, Xing and Yuan (CRYPTO 2018) were the first ones to achieve such an overhead in the amortized setting by evaluating $O(\log n)$ copies of the same circuit in the binary field in parallel. In this work, we construct the first unconditional MPC protocol secure against a malicious adversary in the honest majority setting evaluating just a single boolean circuit with amortized communication complexity of $O(n)$ bits per gate.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Compact, Efficient and UC-Secure Isogeny-Based Oblivious Transfer**
  2021 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-030-77870-5_8) · [IACR ePrint](https://eprint.iacr.org/2020/1012)
  Cyprien Delpech de Saint Guilhem, Yi-Fu Lai, Steven D. Galbraith

  <details><summary>摘要 / Abstract</summary>

  Oblivious transfer (OT) is an essential cryptographic tool that can serve as a building block for almost all secure multiparty functionalities. The strongest security notion against malicious adversaries is universal composability (UC-secure). An important goal is to have post-quantum OT protocols. One area of interest for post-quantum cryptography is isogeny-based crypto. Isogeny-based cryptography has some similarities to Diffie-Hellman, but lacks some algebraic properties that are needed for discrete-log-based OT protocols. Hence it is not always possible to directly adapt existing protocols to the isogeny setting. We propose the first practical isogeny-based UC-secure oblivious transfer protocol in the presence of malicious adversaries. Our scheme uses the CSIDH framework and does not have an analogue in the Diffie-Hellman setting. The scheme consists of a constant number of isogeny computations. The underlying computational assumption is a problem that we call the computational reciprocal CSIDH problem, and that we prove polynomial-time equivalent to the computational CSIDH problem.

  匹配依据：MPC: oblivious transfer

  </details>

- **Broadcast-Optimal Two Round MPC with an Honest Majority**
  2021 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-030-84245-1_6) · [IACR ePrint](https://eprint.iacr.org/2020/1254)
  Bernardo Magri, Sophia Yakoubov, Luisa Siniscalchi, Divya Ravi, Ivan Damgård

  <details><summary>摘要 / Abstract</summary>

  This paper closes the question of the possibility of two-round MPC protocols achieving different security guarantees with and without the availability of broadcast in any given round. Cohen et al. (Eurocrypt 2020) study this question in the dishonest majority setting; we complete the picture by studying the honest majority setting. In the honest majority setting, given broadcast in both rounds, it is known that the strongest guarantee — guaranteed output delivery — is achievable (Gordon et al. Crypto 2015). We show that, given broadcast in the first round only, guaranteed output delivery is still achievable. Given broadcast in the second round only, we give a new construction that achieves identifiable abort, and we show that fairness — and thus guaranteed output delivery — are not achievable in this setting. Finally, if only peer-to-peer channels are available, we show that the weakest guarantee — selective abort — is the only one achievable for corruption thresholds $t &gt; 1$ and for $t = 1$ and $n = 3$. On the other hand, it is already known that selective abort can be achieved in these cases. In the remaining cases, i.e., $t = 1$ and $n &gt; 3$, it is known (from the work of Ishai et al. at Crypto 2010, and Ishai et al. at Crypto 2015) that guaranteed output delivery (and thus all weaker guarantees) are possible.

  匹配依据：MPC: mpc (context)

  </details>

- **Asymptotically-Good Arithmetic Secret Sharing over $\\mathbb {Z}/p^{\\ell }\\mathbb {Z}$ with Strong Multiplication and Its Applications to Efficient MPC.**
  2021 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-84252-9_22)
  Matthieu Rambaud, Ronald Cramer, Chaoping Xing

- **Adaptive Extractors and their Application to Leakage Resilient Secret Sharing**
  2021 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-84252-9_20) · [IACR ePrint](https://eprint.iacr.org/2020/1252)
  Sruthi Sekar, Sai Lakshmi Bhavana Obbattu, Bhavana Kanukurthi, Nishanth Chandran

  <details><summary>摘要 / Abstract</summary>

  We introduce Adaptive Extractors, which, unlike traditional randomness extractors, guarantee security even when an adversary obtains leakage on the source after observing the extractor output. We make a compelling case for the study of such extractors by demonstrating their use in obtaining adaptive leakage in secret sharing schemes. Specifically, at FOCS 2020, Chattopadhyay, Goodman, Goyal, Kumar, Li, Meka, Zuckerman, built an adaptively secure leakage resilient secret sharing scheme (LRSS) with both rate and leakage rate being $O(1/n)$, where $n$ is the number of parties. In this work, we build an adaptively secure LRSS that offers an interesting trade-off between rate, leakage rate, and the total number of shares from which an adversary can obtain leakage. As a special case, when considering $t$-out-of-$n$ secret sharing schemes for threshold $t = cn$ (constant $0&lt;c&lt;1$), we build a scheme with a constant rate, constant leakage rate, and allow the adversary leakage from all but $t-1$ of the shares, while giving her the remaining $t-1$ shares completely in the clear. (Prior to this, constant rate LRSS scheme tolerating adaptive leakage was unknown for any threshold.) Finally, we show applications of our techniques to both non-malleable secret sharing and secure message transmission.

  匹配依据：MPC: secret sharing

  </details>

- **ABY2.0: Improved Mixed-Protocol Secure Two-Party Computation**
  2021 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity21/presentation/patra) · [IACR ePrint](https://eprint.iacr.org/2020/1225)
  Thomas Schneider, Ajith Suresh, Hossein Yalame, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-party Computation (MPC) allows a set of mutually distrusting parties to jointly evaluate a function on their private inputs while maintaining input privacy. In this work, we improve semi-honest secure two-party computation (2PC) over rings, with a focus on the efficiency of the online phase. We propose an efficient mixed-protocol framework, outperforming the state-of-the-art 2PC framework of ABY. Moreover, we extend our techniques to multi- input multiplication gates without inflating the online communication, i.e., it remains independent of the fan-in. Along the way, we construct efficient protocols for several primitives such as scalar product, matrix multiplication, comparison, maxpool, and equality testing. The online communication of our scalar product is two ring elements irrespective of the vector dimension, which is a feature achieved for the first time in the 2PC literature. The practicality of our new set of protocols is showcased with four applications: i) AES S-box, ii) Circuit-based Private Set Intersection, iii) Biometric Matching, and iv) Privacy- preserving Machine Learning (PPML). Most notably, for PPML, we implement and benchmark training and inference of Logistic Regression and Neural Networks over LAN and WAN networks. For training, we improve online runtime (both for LAN and WAN) over SecureML (Mohassel et al., IEEE S&amp;P’17) in the range 1.5x-6.1x, while for inference, the improvements are in the range of 2.5x-754.3x.

  匹配依据：MPC: private set intersection, secure multi party computation, secure two party computation

  </details>
