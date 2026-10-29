# 2020 · MPC · 含会议/期刊记录 · 第 1/1 页

[总目录](../PAPERS.md)

- **Efficient Fully Secure Computation via Distributed Zero-Knowledge Proofs**
  2020-11-19 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-3-030-64840-4_9) · [IACR ePrint](https://eprint.iacr.org/2020/1451)
  Elette Boyle, Yuval Ishai, Ariel Nof, Niv Gilboa

  <details><summary>摘要 / Abstract</summary>

  Secure computation protocols enable mutually distrusting parties to compute a function of their private inputs while revealing nothing but the output. Protocols with {\em full security} (also known as {\em guaranteed output delivery}) in particular protect against denial-of-service attacks, guaranteeing that honest parties receive a correct output. This feature can be realized in the presence of an honest majority, and significant research effort has gone toward attaining full security with good asymptotic and concrete efficiency. We present an efficient protocol for {\em any constant} number of parties $n$, with {\em full security} against $t 1$ corrupted parties. Our protocol relies on {\em replicated secret sharing} to minimize communication and simplify the mechanism for achieving full security. This results in computational cost that scales exponentially with $n$. Our main fully secure protocol builds on a new intermediate honest-majority protocol for verifying the correctness of multiplication triples by making a {\em general} use of distributed zero-knowledge proofs. While this intermediate protocol only achieves the weaker notion of {\em security with abort}, it applies to any linear secret-sharing scheme and provides a conceptually simpler, more general, and more efficient alternative to previous protocols from the literature. In particular, it can be combined with the Fiat-Shamir heuristic to simultaneously achieve logarithmic communication complexity and constant round complexity.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Towards Multiparty Computation Withstanding Coercion of All Parties**
  2020-11-15 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-64378-2_15) · [IACR ePrint](https://eprint.iacr.org/2020/1434)
  Oxana Poburinnaya, Ran Canetti

  <details><summary>摘要 / Abstract</summary>

  Incoercible multi-party computation (Canetti-Gennaro ’96) allows parties to engage in secure computation with the additional guarantee that the public transcript of the computation cannot be used by a coercive outsider to verify representations made by the parties regarding their inputs, outputs, and local random choices. That is, it is guaranteed that the only deductions regarding the truthfulness of such representations, made by an outsider who has witnessed the communication among the parties, are the ones that can be drawn just from the represented inputs and outputs alone. To date, all incoercible secure computation protocols withstand coercion of only a fraction of the parties, or else assume that all parties use an execution environment that makes some crucial parts of their local states physically inaccessible even to themselves. We consider, for the first time, the setting where all parties are coerced, and the coercer expects to see the entire history of the computation. We allow both protocol participants and external attackers to access a common reference string which is generated once and for all by an uncorruptable trusted party. In this setting we construct: - A general multi-party function evaluation protocol, for any number of parties, that withstands coercion of all parties, as long as all parties use the prescribed ``faking algorithm&#x27;&#x27; upon coercion. This holds even if the inputs and outputs represented by coerced parties are globally inconsistent with the evaluated function. - A general two-party function evaluation protocol that withstands even the %``mixed&#x27;&#x27; case where some of the coerced parties do follow the prescribed faking algorithm. (For instance, these parties might collude with the coercer and disclose their true local states.) This protocol is limited to functions where the input of at least one of the parties is taken from a small (poly-size) domain. It uses fully deniable encryption with public deniability for one of the parties; when instantiated using the fully deniable encryption of Canetti, Park, and Poburinnaya (Crypto&#x27;20), it takes 3 rounds of communication. Both protocols operate in the common reference string model, and use fully bideniable encryption (Canetti Park and Poburinnaya, Crypto&#x27;20) and sub-exponential indistinguishability obfuscation. Finally, we show that protocols with certain communication pattern cannot be incoercible, even in a weaker setting where only some parties are coerced.

  匹配依据：MPC: multi party computation, multiparty computation, secure computation

  </details>

- **Simpler Statistically Sender Private Oblivious Transfer from Ideals of Cyclotomic Integers**
  2020-11-15 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-64834-3_13) · [IACR ePrint](https://eprint.iacr.org/2020/1413)
  Daniele Micciancio, Jessica Sorrell

  <details><summary>摘要 / Abstract</summary>

  We present a two-message oblivious transfer protocol achieving statistical sender privacy and computational receiver privacy based on the RLWE assumption for cyclotomic number fields. This work improves upon prior lattice-based statistically sender-private oblivious transfer protocols by reducing the total communication between parties by a factor $O(n\log q)$ for transfer of length $O(n)$ messages. Prior work of Brakerski and Döttling uses transference theorems to show that either a lattice or its dual must have short vectors, the existence of which guarantees lossy encryption for encodings with respect to that lattice, and therefore statistical sender privacy. In the case of ideal lattices from embeddings of cyclotomic integers, the existence of one short vector implies the existence of many, and therefore encryption with respect to either a lattice or its dual is guaranteed to ``lose&quot; more information about the message than can be ensured in the case of general lattices. This additional structure of ideals of cyclotomic integers allows for efficiency improvements beyond those that are typical when moving from the generic to ideal lattice setting, resulting in smaller message sizes for sender and receiver, as well as a protocol that is simpler to describe and analyze.

  匹配依据：MPC: oblivious transfer

  </details>

- **On Statistical Security in Two-Party Computation**
  2020-11-15 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-030-64378-2_19) · [IACR ePrint](https://eprint.iacr.org/2020/1428)
  Muhammad Haris Mughees, Dakshita Khurana

  <details><summary>摘要 / Abstract</summary>

  There has been a large body of work characterizing the round complexity of general-purpose maliciously secure two-party computation (2PC) against probabilistic polynomial time adversaries. This is particularly true for zero-knowledge, which is a special case of 2PC. In fact, in the special case of zero knowledge, optimal protocols with unconditional security against one of the two players have also been meticulously studied and constructed. On the other hand, general-purpose maliciously secure 2PC with statistical or unconditional security against one of the two participants has remained largely unexplored so far. In this work, we initiate the study of such protocols, which we refer to as 2PC with one-sided statistical security. We settle the round complexity of 2PC with one-sided statistical security with respect to black-box simulation by obtaining the following tight results: In a setting where only one party obtains an output, we design 2PC in $4$ rounds with statistical security against receivers and computational security against senders. In a setting where both parties obtain outputs, we design 2PC in $5$ rounds with computational security against the party that obtains output first and statistical security against the party that obtains output last. Katz and Ostrovsky (CRYPTO 2004) showed that 2PC with black-box simulation requires at least $4$ rounds when one party obtains an output and $5$ rounds when both parties obtain outputs, even when only computational security is desired against both parties. Thus in these settings, not only are our results tight, but they also show that statistical security is achievable at no extra cost to round complexity. This still leaves open the question of whether 2PC can be achieved with black-box simulation in $4$ rounds with statistical security against senders and computational security against receivers. Based on a lower bound on computational zero-knowledge proofs due to Katz (TCC 2008), we observe that the answer is negative unless the polynomial hierarchy collapses.

  匹配依据：MPC: secure two party computation, two party computation

  </details>

- **Information-Theoretic 2-Round MPC without Round Collapsing: Adaptive Security, and More**
  2020-11-15 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-030-64378-2_18) · [IACR ePrint](https://eprint.iacr.org/2020/1431)
  Tianren Liu, Huijia Lin, Hoeteck Wee

  <details><summary>摘要 / Abstract</summary>

  We present simpler and improved constructions of 2-round protocols for secure multi-party computation (MPC) in the semi-honest setting. Our main results are new information-theoretically secure protocols for arithmetic NC1 in two settings: (i) the plain model tolerating up to $t &lt; n/2$ corruptions; and (ii) in the OLE-correlation model tolerating any number of corruptions. Our protocols achieve adaptive security and require only black-box access to the underlying field, whereas previous results only achieve static security and require non-black-box field access. Moreover, both results extend to polynomial-size circuits with computational and adaptive security, while relying on black-box access to a pseudorandom generator. In the OLE correlation model, the extended protocols for circuits tolerate up to $n-1$ corruptions. Along the way, we introduce a conceptually novel framework for 2-round MPC that does not rely on the round collapsing framework underlying all of the recent advances in 2-round MPC.

  匹配依据：MPC: secure multi party computation

  </details>

- **On the Exact Round Complexity of Best-of-both-Worlds Multi-party Computation**
  2020-09-01 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-3-030-64840-4_3) · [IACR ePrint](https://eprint.iacr.org/2020/1050)
  Divya Ravi, Swati Singla, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  The two traditional streams of multiparty computation (MPC) protocols consist of-- (a) protocols achieving guaranteed output delivery (god) or fairness (fn) in the honest-majority setting and (b) protocols achieving unanimous or selective abort (ua, sa) in the dishonest-majority setting. The favorable presence of honest majority amongst the participants is necessary to achieve the stronger notions of god or fn. While the constructions of each type are abound in the literature, one class of protocols does not seem to withstand the threat model of the other. For instance, the honest-majority protocols do not guarantee privacy of the inputs of the honest parties in the face of dishonest majority and likewise the dishonest-majority protocols cannot achieve god and fn, tolerating even a single corruption, let alone dishonest minority. The promise of the unconventional yet much sought-after species of MPC, termed as `Best-of-Both-Worlds&#x27; (BoBW), is to offer the best possible security depending on the actual corruption scenario. This work nearly settles the exact round complexity of two classes of BoBW protocols differing on the security achieved in the honest-majority setting, namely god and fn respectively, under the assumption of no setup (plain model), public setup (CRS) and private setup (CRS + PKI or simply PKI). The former class necessarily requires the number of parties to be strictly more than the sum of the bounds of corruptions in the honest-majority and dishonest-majority setting, for a feasible solution to exist. Demoting the goal to the second-best attainable security in the honest-majority setting, the latter class needs no such restriction. Assuming a network with pair-wise private channels and a broadcast channel, we show that 5 and 3 rounds are necessary and sufficient for the class of BoBW MPC with fn under the assumption of `no setup&#x27; and `public and private setup&#x27; respectively. For the class of BoBW MPC with god, we show necessity and sufficiency of 3 rounds for the public setup case and 2 rounds for the private setup case. In the no setup setting, we show the sufficiency of 5 rounds, while the known lower bound is 4. All our upper bounds are based on polynomial-time assumptions and assume black-box simulation. With distinct feasibility conditions, the classes differ in terms of the round requirement. The bounds are in some cases different and on a positive note at most one more, compared to the maximum of the needs of the honest-majority and dishonest-majority setting. Our results remain unaffected when security with abort and fairness are upgraded to their identifiable counterparts.

  匹配依据：MPC: multi party computation, multiparty computation

  </details>

- **Stacked Garbling: Garbled Circuit Proportional to Longest Execution Path**
  2020-08-18 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-030-56880-1_27) · [IACR ePrint](https://eprint.iacr.org/2020/973)
  David Heath, Vladimir Kolesnikov

  <details><summary>摘要 / Abstract</summary>

  Secure two party computation (2PC) of arbitrary programs can be efficiently achieved using garbled circuits (GC). The bottleneck of GC efficiency is communication. It is widely believed that for direct 2PC evaluation of a Boolean circuit, it is necessary to transmit the entire GC, including garbled truth tables corresponding to subcomputations whose output is ultimately discarded by conditional logic. This folklore belief is false. We propose a novel GC technique, stacked garbling, that eliminates the communication cost of inactive conditional branches. We extend the ideas of conditional GC evaluation explored in (Kolesnikov, Asiacrypt 18) and (Heath and Kolesnikov, Eurocrypt 20). Unlike these works, ours is for general 2PC where no player knows which conditional branch is taken. Our garbling scheme, Stack, requires communication proportional to the longest execution path rather than to the entire circuit. Stack is compatible with state-of-the-art techniques, such as free XOR and half-gates. Stack is a garbling scheme. As such, it can be plugged into a variety of existing protocols, and the resulting round complexity is the same as that of standard GC. The approach does incur computation cost quadratic in the conditional branching factor vs linear in standard schemes, but the tradeoff is beneficial for most programs: GC computation even on weak hardware is faster than GC transmission on fast channels. We implemented Stack in C++. Stack reduces communication cost by approximately the branching factor: for 16 branches, communication is reduced by 10.5x. In terms of wall-clock time for circuits with branching factor 16 over a 50 Mbps WAN on a laptop, Stack outperforms state-of- the-art half-gates-based 2PC by more than 4x.

  匹配依据：MPC: garbled circuit, garbled circuits, garbling scheme, secure two party computation

  </details>

- **Reimagining Secret Sharing: Creating a Safer and More Versatile Primitive by Adding Authenticity, Correcting Errors, and Reducing Randomness Requirements**
  2020-06-27 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.2478/POPETS-2020-0082) · [IACR ePrint](https://eprint.iacr.org/2020/800)
  Wei Dai, Phillip Rogaway, Mihir Bellare

  <details><summary>摘要 / Abstract</summary>

  Aiming to strengthen classical secret-sharing to make it a more directly useful primitive for human end-users, we develop definitions, theorems, and efficient constructions for what we call &quot;adept&quot; secret-sharing. Our primary concerns are the properties we call &quot;privacy&quot;, &quot;authenticity&quot;, and &quot;error correction&quot;. Privacy strengthens the classical requirement by ensuring maximal confidentiality even if the dealer does not employ fresh, uniformly random coins with each sharing. That might happen either intentionally--to enable reproducible secret-sharing--or unintentionally, when an entropy source fails. Authenticity is a shareholder&#x27;s guarantee that a secret recovered using his or her share will coincide with the value the dealer committed to at the time the secret was shared. Error correction is the guarantee that recovery of a secret will succeed, also identifying the valid shares, exactly when there is a unique explanation as to which shares implicate what secret. These concerns arise organically from a desire to create general-purpose libraries and apps for secret sharing that can withstand both strong adversaries and routine operational errors.

  匹配依据：MPC: secret sharing

  </details>

- **Always Have a Backup Plan: Fully Secure Synchronous MPC with Asynchronous Fallback**
  2020-06-18 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-030-56880-1_25) · [IACR ePrint](https://eprint.iacr.org/2020/740)
  Julian Loss, Chen-Da Liu-Zhang, Erica Blum

  <details><summary>摘要 / Abstract</summary>

  Protocols for secure Multi-Party Computation (MPC) can be classified according to the underlying communication model. Two prominent communication models considered in the literature are the synchronous and asynchronous models, which considerably differ in terms of the achievable security guarantees. Synchronous MPC protocols can achieve the optimal corruption threshold $n/2$ and allow every party to give input, but become completely insecure when synchrony assumptions are violated. On the other hand, asynchronous MPC protocols remain secure under arbitrary network conditions, but can tolerate only $n/3$ corruptions and parties with slow connections unavoidably cannot give input. A natural question is whether there exists a protocol for MPC that can tolerate up to $t_s &lt; n/2$ corruptions under a synchronous network and $t_a &lt; n/3$ corruptions even when the network is asynchronous. We answer this question by showing tight feasibility and impossibility results. More specifically, we show that such a protocol exists if and only if $t_a + 2t_s &lt; n$ and the number of inputs taken into account under an asynchronous network is at most $n-t_s$.

  匹配依据：MPC: secure multi party computation

  </details>

- **Private Set Intersection in the Internet Setting From Lightweight Oblivious PRF**
  2020-06-17 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-56877-1_2) · [IACR ePrint](https://eprint.iacr.org/2020/729)
  Melissa Chase, Peihan Miao

  <details><summary>摘要 / Abstract</summary>

  We present a new protocol for two-party private set intersection (PSI) with semi-honest security in the plain model and one-sided malicious security in the random oracle model. Our protocol achieves a better balance between computation and communication than existing PSI protocols. Specifically, our protocol is the fastest in networks with moderate bandwidth (e.g., 30 - 100 Mbps). Considering the monetary cost (proposed by Pinkas et al. in CRYPTO 2019) to run the protocol on a cloud computing service, our protocol also compares favorably. Underlying our PSI protocol is a new lightweight multi-point oblivious pesudorandom function (OPRF) protocol based on oblivious transfer (OT) extension. We believe this new protocol may be of independent interest.

  匹配依据：MPC: oblivious transfer, private set intersection

  </details>

- **Non-Malleable Secret Sharing against Bounded Joint-Tampering Attacks in the Plain Model**
  2020-06-16 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-030-56877-1_5) · [IACR ePrint](https://eprint.iacr.org/2020/725)
  Maciej Obremski, Antonio Faonio, Gianluca Brian, Daniele Venturi, Mark Simkin

  <details><summary>摘要 / Abstract</summary>

  Secret sharing enables a dealer to split a secret into a set of shares, in such a way that certain authorized subsets of share holders can reconstruct the secret, whereas all unauthorized subsets cannot. Non-malleable secret sharing (Goyal and Kumar, STOC 2018) additionally requires that, even if the shares have been tampered with, the reconstructed secret is either the original or a completely unrelated one. In this work, we construct non-malleable secret sharing tolerating $p$-time {\em joint-tampering} attacks in the plain model (in the computational setting), where the latter means that, for any $p&gt;0$ fixed {\em a priori}, the attacker can tamper with the same target secret sharing up to $p$ times. In particular, assuming one-to-one one-way functions, we obtain: - A secret sharing scheme for threshold access structures which tolerates joint $p$-time tampering with subsets of the shares of maximal size ({\em i.e.}, matching the privacy threshold of the scheme). This holds in a model where the attacker commits to a partition of the shares into non-overlapping subsets, and keeps tampering jointly with the shares within such a partition (so-called {\em selective partitioning}). - A secret sharing scheme for general access structures which tolerates joint $p$-time tampering with subsets of the shares of size $O(\sqrt{\log n})$, where $n$ is the number of parties. This holds in a stronger model where the attacker is allowed to adaptively change the partition within each tampering query, under the restriction that once a subset of the shares has been tampered with jointly, that subset is always either tampered jointly or not modified by other tampering queries (so-called {\em semi-adaptive partitioning}). At the heart of our result for selective partitioning lies a new technique showing that every one-time {\em statistically} non-malleable secret sharing against joint tampering is in fact {\em leakage-resilient} non-malleable ({\em i.e.},\ the attacker can leak jointly from the shares prior to tampering). We believe this may be of independent interest, and in fact we show it implies lower bounds on the share size and randomness complexity of statistically non-malleable secret sharing against {\em independent} tampering.

  匹配依据：MPC: secret sharing

  </details>

- **Crowd Verifiable Zero-Knowledge and End-to-end Verifiable Multiparty Computation**
  2020-06-14 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-3-030-64840-4_24) · [IACR ePrint](https://eprint.iacr.org/2020/711)
  Foteini Baldimtsi, Aggelos Kiayias, Bingsheng Zhang, Thomas Zacharias

  <details><summary>摘要 / Abstract</summary>

  Auditing a secure multiparty computation (MPC) protocol entails the validation of the protocol transcript by a third party that is otherwise untrusted. In this work we introduce the concept of end-to-end verifiable MPC (VMPC), that requires the validation to provide a correctness guarantee even in the setting that all servers, trusted setup primitives and all the client systems utilized by the input-providing users of the MPC protocol are subverted by an adversary. To instantiate VMPC, we introduce a new concept in the setting of zero-knowlegde protocols that we term crowd verifiable zero-knowledge (CVZK). A CVZK protocol enables a prover to convince a set of verifiers about a certain statement, even though each one individually contributes a small amount of entropy for verification and some of them are adversarially controlled. Given CVZK, we present a VMPC protocol that is based on discrete-logarithm related assumptions. At the high level of adversity that VMPC is meant to withstand, it is infeasible to ensure perfect correctness, thus we investigate the classes of functions and verifiability relations that are feasible in our framework, and present a number of possible applications the underlying functions of which can be implemented via VMPC.

  匹配依据：MPC: multiparty computation, secure multiparty computation

  </details>

- **The Share Size of Secret-Sharing Schemes for Almost All Access Structures and Graphs**
  2020-06-03 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-030-64381-2_18) · [IACR ePrint](https://eprint.iacr.org/2020/664)
  Oriol Farràs, Amos Beimel

  <details><summary>摘要 / Abstract</summary>

  The share size of general secret-sharing schemes is poorly understood. The gap between the best known upper bound on the total share size per party of $2^{0.59n}$ (Applebaum and Nir, CRYPTO 2021) and the best known lower bound of $\Omega(n/\log n)$ (Csirmaz, J. of Cryptology 1997) is huge (where $n$ is the number of parties in the scheme). To gain some understanding on this problem, we study the share size of secret-sharing schemes of almost all access structures, i.e., of almost all collections of authorized sets. This is motivated by the fact that in complexity, many times almost all objects are hardest (e.g., most Boolean functions require exponential size circuits). All previous constructions of secret-sharing schemes were for the worst access structures (i.e., all access structures) or for specific families of access structures. We prove upper bounds on the share size for almost all access structures. We combine results on almost all monotone Boolean functions (Korshunov, Probl. Kibern. 1981) and a construction of (Liu and Vaikuntanathan, STOC 2018) and conclude that almost all access structures have a secret-sharing scheme with share size $2^{\tilde{O}(\sqrt{n})}$. We also study graph secret-sharing schemes. In these schemes, the parties are vertices of a graph and a set can reconstruct the secret if and only if it contains an edge. Again, for this family there is a huge gap between the upper bounds - $O(n/\log n)$ (Erdös and Pyber, Discrete Mathematics 1997) - and the lower bounds - $\Omega(\log n)$ (van Dijk, Des. Codes Crypto. 1995). We show that for almost all graphs, the share size of each party is $n^{o(1)}$. This result is achieved by using robust 2-server conditional disclosure of secrets protocols, a new primitive introduced and constructed in (Applebaum et al., STOC 2020), and the fact that the size of the maximal independent set in a random graph is small. Finally, using robust conditional disclosure of secrets protocols, we improve the total share size for all very dense graphs.

  匹配依据：MPC: secret sharing

  </details>

- **ALBATROSS: publicly AttestabLe BATched Randomness based On Secret Sharing**
  2020-06-03 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-64840-4_11) · [IACR ePrint](https://eprint.iacr.org/2020/644)
  Bernardo Machado David, Ignacio Cascudo, Bernardo David

  <details><summary>摘要 / Abstract</summary>

  In this paper we present ALBATROSS, a family of multiparty randomness generation protocols with guaranteed output delivery and public verification that allows to trade off corruption tolerance for a much improved amortized computational complexity. Our basic stand alone protocol is based on publicly verifiable secret sharing (PVSS) and is secure under in the random oracle model under the decisional Diffie-Hellman (DDH) hardness assumption. We also address the important issue of constructing Universally Composable randomness beacons, showing two UC versions of Albatross: one based on simple UC NIZKs and another one based on novel efficient ``designated verifier&#x27;&#x27; homomorphic commitments. Interestingly this latter version can be instantiated from a global random oracle under the weaker Computational Diffie-Hellman (CDH) assumption. An execution of ALBATROSS with $n$ parties, out of which up to $t=(1/2-\epsilon)\cdot n$ are corrupt for a constant $\epsilon&gt;0$, generates $\Theta(n^2)$ uniformly random values, requiring in the worst case an amortized cost per party of $\Theta(\log n)$ exponentiations per random value. We significantly improve on the SCRAPE protocol (Cascudo and David, ACNS 17), which required $\Theta(n^2)$ exponentiations per party to generate one uniformly random value. This is mainly achieved via two techniques: first, the use of packed Shamir secret sharing for the PVSS; second, the use of linear $t$-resilient functions (computed via a Fast Fourier Transform-based algorithm) to improve the randomness extraction.

  匹配依据：MPC: secret sharing

  </details>

- **The Round Complexity of Perfect MPC with Active Security and Optimal Resiliency**
  2020-05-18 · MPC · 含会议/期刊记录 · [FOCS](https://doi.org/10.1109/FOCS46700.2020.00121) · [IACR ePrint](https://eprint.iacr.org/2020/581)
  Eliran Kachlon, Benny Applebaum, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  In STOC 1988, Ben-Or, Goldwasser, and Wigderson (BGW) established an important milestone in the fields of cryptography and distributed computing by showing that every functionality can be computed with perfect (information-theoretic and error-free) security at the presence of an active (aka Byzantine) rushing adversary that controls up to $n/3$ of the parties. We study the round complexity of general secure multiparty computation in the BGW model. Our main result shows that every functionality can be realized in only four rounds of interaction, and that some functionalities cannot be computed in three rounds. This completely settles the round-complexity of perfect actively-secure optimally-resilient MPC, resolving a long line of research. Our lower-bound is based on a novel round-reduction technique that allows us to lift existing three-round lower-bounds for verifiable secret sharing to four-round lower-bounds for general MPC. To prove the upper-bound, we develop new round-efficient protocols for computing degree-2 functionalities over large fields, and establish the completeness of such functionalities. The latter result extends the recent completeness theorem of Applebaum, Brakerski and Tsabary (TCC 2018, Eurocrypt 2019) that was limited to the binary field.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Efficient and Round-Optimal Oblivious Transfer and Commitment with Adaptive Security**
  2020-05-15 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-64840-4_10) · [IACR ePrint](https://eprint.iacr.org/2020/545)
  Pratik Sarkar, Xiao Wang, Ran Canetti

  <details><summary>摘要 / Abstract</summary>

  We construct the most efficient two-round adaptively secure bit-OT in the Common Random String (CRS) model. The scheme is UC secure under the Decisional Diffie-Hellman (DDH) assumption. It incurs O(1) exponentiations and sends O(1) group elements, whereas the state of the art requires O(k^2) exponentiations and communicates poly(k) bits, where k is the computational security parameter. Along the way, we obtain several other efficient UC-secure OT protocols under DDH : - The most efficient yet two-round adaptive string-OT protocol assuming programmable random oracle. Furthermore, the protocol can be made non-interactive in the simultaneous message setting, assuming random inputs for the sender. - The first two-round string-OT with amortized constant exponentiations and communication overhead which is secure in the observable random oracle model. - The first two-round receiver equivocal string-OT in the CRS model that incurs constant computation and communication overhead. We also obtain the first non-interactive adaptive string UC-commitment in the CRS model which incurs a sublinear communication overhead in the security parameter. Specifically, we commit to polylog(k) bits while communicating O(k) bits. Moreover, it is additively homomorphic in nature. We can also extend our results to the single CRS model where multiple sessions share the same CRS. As a corollary, we obtain a two-round adaptively secure MPC protocol in this model.

  匹配依据：MPC: oblivious transfer

  </details>

- **MP-SPDZ: A Versatile Framework for Multi-Party Computation**
  2020-05-05 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3372297.3417872) · [IACR ePrint](https://eprint.iacr.org/2020/521)
  Marcel Keller

  <details><summary>摘要 / Abstract</summary>

  Multi-Protocol SPDZ (MP-SPDZ) is a fork of SPDZ-2 (Keller et al., CCS &#x27;13), an implementation of the multi-party computation (MPC) protocol called SPDZ (Damgård et al., Crypto &#x27;12). MP-SPDZ extends SPDZ-2 to 34 MPC protocol variants, all of which can be used with the same high-level programming interface based on Python. This considerably simplifies comparing the cost of different protocols and security models. The protocols cover all commonly used security models (honest/dishonest majority and semi-honest/malicious corruption) as well as computation of binary and arithmetic circuits (the latter modulo primes and powers of two). The underlying primitives employed include secret sharing, oblivious transfer, homomorphic encryption, and garbled circuits. The breadth of implemented protocols coupled with an accessible high-level interface makes it suitable to benchmark the cost of computation in various security models for researchers both with and without a background in secure computation This paper aims to outline the variety of protocols implemented and the design choices made in the development of MP-SPDZ as well as the capabilities of the programming interface.

  匹配依据：MPC: garbled circuits, multi party computation, oblivious transfer, secret sharing, secure computation

  </details>

- **Statistical Zaps and New Oblivious Transfer Protocols**
  2020-02-24 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-45727-3_23) · [IACR ePrint](https://eprint.iacr.org/2020/235)
  Zhengzhong Jin, Giulio Malavolta, Abhishek Jain, Vipul Goyal

  <details><summary>摘要 / Abstract</summary>

  We study the problem of achieving statistical privacy in interactive proof systems and oblivious transfer -- two of the most well studied two-party protocols -- when limited rounds of interaction are available. Statistical Zaps: We give the first construction of statistical Zaps, namely, two-round statistical witness-indistinguishable (WI) protocols with a public-coin verifier. Our construction achieves computational soundness based on the quasi-polynomial hardness of learning with errors. Three-Round Statistical Receiver-Private Oblivious Transfer: We give the first construction of a three-round oblivious transfer (OT) protocol -- in the plain model -- that achieves statistical privacy for receivers and computational privacy for senders against malicious adversaries, based on polynomial-time assumptions. The round-complexity of our protocol is optimal. We obtain our first result by devising a public-coin approach to compress sigma protocols, without relying on trusted setup. To obtain our second result, we devise a general framework via a new notion of statistical hash commitments that may be of independent interest.

  匹配依据：MPC: oblivious transfer

  </details>

- **Differentially Private Set Union**
  2020-02-22 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2002.09745) · [series/jmlr](http://proceedings.mlr.press/v119/gopi20a.html)
  Sivakanth Gopi, Sergey Yekhanin, Judy Hanwen Shen, Pankaj Gulhane, Janardhan Kulkarni, Milad Shokouhi

  <details><summary>摘要 / Abstract</summary>

  We study the basic operation of set union in the global model of differential privacy. In this problem, we are given a universe $U$ of items, possibly of infinite size, and a database $D$ of users. Each user $i$ contributes a subset $W_i \subseteq U$ of items. We want an ($ε$,$δ$)-differentially private algorithm which outputs a subset $S \subset \cup_i W_i$ such that the size of $S$ is as large as possible. The problem arises in countless real world applications; it is particularly ubiquitous in natural language processing (NLP) applications as vocabulary extraction. For example, discovering words, sentences, $n$-grams etc., from private text data belonging to users is an instance of the set union problem. Known algorithms for this problem proceed by collecting a subset of items from each user, taking the union of such subsets, and disclosing the items whose noisy counts fall above a certain threshold. Crucially, in the above process, the contribution of each individual user is always independent of the items held by other users, resulting in a wasteful aggregation process, where some item counts happen to be way above the threshold. We deviate from the above paradigm by allowing users to contribute their items in a $\textit{dependent fashion}$, guided by a $\textit{policy}$. In this new setting ensuring privacy is significantly delicate. We prove that any policy which has certain $\textit{contractive}$ properties would result in a differentially private algorithm. We design two new algorithms, one using Laplace noise and other Gaussian noise, as specific instances of policies satisfying the contractive properties. Our experiments show that the new algorithms significantly outperform previously known mechanisms for the problem.

  匹配依据：MPC: private set union

  </details>

- **PSI from PaXoS: Fast, Malicious Private Set Intersection**
  2020-02-18 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-45724-2_25) · [IACR ePrint](https://eprint.iacr.org/2020/193)
  Ni Trieu, Avishay Yanai, Benny Pinkas, Mike Rosulek

  <details><summary>摘要 / Abstract</summary>

  We present a 2-party private set intersection (PSI) protocol which provides security against malicious participants, yet is almost as fast as the fastest known semi-honest PSI protocol of Kolesnikov et al. (CCS 2016). Our protocol is based on a new approach for two-party PSI, which can be instantiated to provide security against either malicious or semi-honest adversaries. The protocol is unique in that the only difference between the semi-honest and malicious versions is an instantiation with different parameters for a linear error-correction code. It is also the first PSI protocol which is concretely efficient while having linear communication and security against malicious adversaries, while running in the OT-hybrid model (assuming a non-programmable random oracle). State of the art semi-honest PSI protocols take advantage of cuckoo hashing, but it has proven a challenge to use cuckoo hashing for malicious security. Our protocol is the first to use cuckoo hashing for malicious-secure PSI. We do so via a new data structure, called a probe-and-XOR of strings (PaXoS), which may be of independent interest. This abstraction captures important properties of previous data structures, most notably garbled Bloom filters. While an encoding by a garbled Bloom filter is larger by a factor of $O(\lambda)$ than the original data, we describe a significantly improved PaXoS based on cuckoo hashing that achieves constant rate while being no worse in other relevant efficiency measures.

  匹配依据：MPC: private set intersection

  </details>

- **Guaranteed Output Delivery Comes Free in Honest Majority MPC**
  2020-02-18 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-030-56880-1_22) · [IACR ePrint](https://eprint.iacr.org/2020/189)
  Vipul Goyal, Chenzhi Zhu, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  We study the communication complexity of unconditionally secure MPC with guaranteed output delivery over point-to-point channels for corruption threshold t &lt; n/2, assuming the existence of a public broadcast channel. We ask the question: “is it possible to construct MPC in this setting s.t. the communication complexity per multiplication gate is linear in the number of parties?” While a number of works have focused on reducing the communication complexity in this setting, the answer to the above question has remained elusive until now. We also focus on the concrete communication complexity of evaluating each multiplication gate. We resolve the above question in the affirmative by providing an MPC with communication complexity O(Cn\phi) bits (ignoring fixed terms which are independent of the circuit) where \phi is the length of an element in the field, C is the size of the (arithmetic) circuit, n is the number of parties. This is the first construction where the asymptotic communication complexity matches the best-known semi-honest protocol. This represents a strict improvement over the previously best-known communication complexity of O(C(n\phi+\kappa)+D_Mn^2\kappa) bits, where \kappa is the security parameter and D_M is the multiplicative depth of the circuit. Furthermore, the concrete communication complexity per multiplication gate is 5.5 field elements per party in the best case and 7.5 field elements in the worst case when one or more corrupted parties have been identified. This also roughly matches the best-known semi-honest protocol, which requires 5.5 field elements per gate.

  匹配依据：MPC: mpc (context)

  </details>

- **A Secret-Sharing Based MPC Protocol for Boolean Circuits with Good Amortized Complexity**
  2020-02-13 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-64378-2_23) · [IACR ePrint](https://eprint.iacr.org/2020/162)
  Ignacio Cascudo, Jaron Skovsted Gundersen

  <details><summary>摘要 / Abstract</summary>

  We present a new secure multiparty computation protocol in the preprocessing model that allows for the evaluation of a number of instances of a boolean circuit in parallel, with a small online communication complexity per instance of 10 bits per party and multiplication gate. Our protocol is secure against an active dishonest majority, and can be also transformed, via known techniques, into a protocol for the evaluation of a single “well-formed” boolean circuit with the same complexity per multiplication gate at the cost of some overhead that depends on the topology of the circuit. Our protocol uses an approach introduced recently in the setting of honest majority and information-theoretical security which, using an algebraic notion called reverse multiplication friendly embeddings, essentially transforms a batch of evaluations of an arithmetic circuit over a small field into one evaluation of another arithmetic circuit over a larger field. To obtain security against a dishonest majority we combine this approach with the well-known SPDZ protocol that operates over a large field. Structurally our protocol is most similar to MiniMAC, a protocol which bases its security on the use of error-correcting codes, but our protocol has a communication complexity which is half of that of MiniMAC when the best available binary codes are used. This makes it fully compatible with the technique from MiniMAC that allows to adapt the protocol for the computation of a well-formed boolean circuit. With respect to certain variant of MiniMAC that utilizes codes over large fields, our communication complexity is slightly worse; however, that variant of MiniMAC needs a much larger preprocessing than ours. We also show that our protocol also has smaller amortized communication complexity than Committed MPC, a protocol for general fields based on homomorphic commitments, if we use the best available constructions for those commitments. Finally, we construct a preprocessing phase from oblivious transfer based on ideas from MASCOT and Committed MPC.

  匹配依据：MPC: oblivious transfer, secret sharing, secure multiparty computation

  </details>

- **Better Secret-Sharing via Robust Conditional Disclosure of Secrets**
  2020-01-28 · MPC · 含会议/期刊记录 · [STOC](https://doi.org/10.1145/3357713.3384293) · [IACR ePrint](https://eprint.iacr.org/2020/080)
  Naty Peter, Oded Nir, Amos Beimel, Benny Applebaum

  <details><summary>摘要 / Abstract</summary>

  A secret-sharing scheme allows to distribute a secret $s$ among $n$ parties such that only some predefined ``authorized&#x27;&#x27; sets of parties can reconstruct the secret, and all other ``unauthorized&#x27;&#x27; sets learn nothing about $s$. For over 30 years, it was known that any (monotone) collection of authorized sets can be realized by a secret-sharing scheme whose shares are of size $2^{n-o(n)}$ and until recently no better scheme was known. In a recent breakthrough, Liu and Vaikuntanathan (STOC 2018) have reduced the share size to $2^{0.994n+o(n)}$, which was later improved to $2^{0.892n+o(n)}$ by Applebaum et al. (EUROCRYPT 2019). In this paper we improve the exponent of general secret-sharing schemes down to $0.637$. For the special case of linear secret-sharing schemes, we get an exponent of $0.762$ (compared to $0.942$ of Applebaum et al.). As our main building block, we introduce a new \emph{robust} variant of conditional disclosure of secrets (robust CDS) that achieves unconditional security even under bounded form of re-usability. We show that the problem of general secret-sharing schemes reduces to robust CDS protocols with sub-exponential overhead and derive our main result by implementing robust CDS with a non-trivial exponent. The latter construction follows by presenting a general immunization procedure that turns standard CDS into a robust CDS.

  匹配依据：MPC: secret sharing

  </details>

- **Two-Round Oblivious Transfer from CDH or LPN.**
  2020 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-030-45724-2_26)
  Daniel Masny, Daniel Wichs, Sanjam Garg, Mohammad Hajiabadi, Nico Döttling

- **Telekine: Secure Computing with Cloud GPUs.**
  2020 · MPC · 含会议/期刊记录 · [NSDI](https://www.usenix.org/conference/nsdi20/presentation/hunt)
  Zhipeng Jia, Tyler Hunt, Yige Hu, Ariel Szekely, Vance Miller, Emmett Witchel, Christopher J. Rossbach

- **Succinct Non-interactive Secure Computation.**
  2020 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-45724-2_8)
  Andrew Morgan, Antigoni Polychroniadou, Rafael Pass

- **Secure Multi-party Computation of Differentially Private Median.**
  2020 · MPC · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity20/presentation/boehler)
  Jonas Böhler, Florian Kerschbaum

- **Secure MPC: Laziness Leads to GOD.**
  2020 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-64840-4_5)
  Saikrishna Badrinarayanan, Aayush Jain, Nathan Manohar, Amit Sahai

- **Round Optimal Secure Multiparty Computation from Minimal Assumptions.**
  2020 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-030-64378-2_11)
  Arka Rai Choudhuri, Michele Ciampi, Vipul Goyal, Abhishek Jain, Rafail Ostrovsky

- **Robust Secret Sharing with Almost Optimal Share Size and Security Against Rushing Adversaries.**
  2020 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-64381-2_17)
  Serge Fehr, Chen Yuan

- **Reversible Image Secret Sharing.**
  2020 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2020.3001735)
  Lintao Liu, Yuliang Lu, Xianhua Song, Xuehu Yan

- **Resource-Restricted Cryptography: Revisiting MPC Bounds in the Proof-of-Work Era.**
  2020 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-030-45724-2_5)
  Giorgos Panagiotakos, Juan A. Garay, Rafail Ostrovsky, Vassilis Zikas, Aggelos Kiayias

- **On the Power of Secure Two-Party Computation.**
  2020 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-019-09314-2)
  Muthuramakrishnan Venkitasubramaniam, Carmit Hazay

- **On the Complexity of Arithmetic Secret Sharing.**
  2020 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-64381-2_16)
  Chen Yuan, Chaoping Xing, Ronald Cramer

- **Non-malleable Codes, Extractors and Secret Sharing for Interleaved Tampering and Composition of Tampering.**
  2020 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-030-64381-2_21)
  Eshan Chattopadhyay, Xin Li

- **Nearly Optimal Robust Secret Sharing Against Rushing Adversaries.**
  2020 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-030-56877-1_6)
  Pasin Manurangsi, Akshayaram Srinivasan, Prashant Nalini Vasudevan

- **Mr NISC: Multiparty Reusable Non-Interactive Secure Computation.**
  2020 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-64378-2_13)
  Fabrice Benhamouda, Huijia Lin

- **More Efficient MPC from Improved Triple Generation and Authenticated Garbling.**
  2020 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3372297.3417285)
  Xiao Wang, Jiang Zhang, Kang Yang

- **Mon$\\mathbb {Z}\_{2^{k}}$a: Fast Maliciously Secure Two Party Computation on $\\mathbb {Z}\_{2^{k}}$.**
  2020 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-45388-6_13)
  Irene Giacomelli, Dario Catalano, Dario Fiore, Mario Di Raimondo

- **Mind the Gap: Ceremonies for Applied Secret Sharing.**
  2020 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.2478/POPETS-2020-0033)
  Bailey Kacsmar, Ian Goldberg, Florian Kerschbaum, Chelsea Komlo

- **MPC with Synchronous Security and Asynchronous Responsiveness.**
  2020 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-3-030-64840-4_4)
  Julian Loss, Daniel Tschudi, Chen-Da Liu-Zhang, Ueli Maurer, Tal Moran

- **Lower Bounds for Leakage-Resilient Secret Sharing.**
  2020 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-45721-1_20)
  Mark Simkin, Jesper Buus Nielsen

- **Low Cost Constant Round MPC Combining BMR and Oblivious Transfer.**
  2020 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-020-09355-Y)
  Eduardo Soria-Vazquez, Peter Scholl, Carmit Hazay

- **Is the Classical GMW Paradigm Practical? The Case of Non-Interactive Actively Secure 2PC.**
  2020 · MPC · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3372297.3423366)
  Mohammad Hossein Faghihi Sereshgi, Yuval Ishai, Jackson Abascal, Muthuramakrishnan Venkitasubramaniam, Carmit Hazay

- **Feasibility and Infeasibility of Secure Computation with Malicious PUFs.**
  2020 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-019-09329-9)
  Dana Dachman-Soled, Nils Fleischhacker, Dominique Schröder, Jonathan Katz, Anna Lysyanskaya

- **Extractors and Secret Sharing Against Bounded Collusion Protocols.**
  2020 · MPC · 含会议/期刊记录 · [FOCS](https://doi.org/10.1109/FOCS46700.2020.00117)
  Eshan Chattopadhyay, Xin Li, Jesse Goodman, Vipul Goyal, David Zuckerman, Raghu Meka, Ashutosh Kumar

- **Evolving Ramp Secret Sharing with a Small Gap.**
  2020 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-030-45721-1_19)
  Hussien Othman, Amos Beimel

- **Efficient and Secure Multiparty Computation from Fixed-Key Block Ciphers.**
  2020 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP40000.2020.00016)
  Xiao Wang, Yu Yu, Jonathan Katz, Chun Guo

- **Efficient Constructions for Almost-Everywhere Secure Computation.**
  2020 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-45724-2_6)
  Siddhartha Jayanti, Srinivasan Raghuraman, Nikhil Vyas

- **Circuit Amortization Friendly Encodingsand Their Application to Statistically Secure Multiparty Computation.**
  2020 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-64840-4_8)
  Eduardo Soria-Vazquez, Anders P. K. Dalskov, Eysa Lee

- **Blackbox Secret Sharing Revisited: A Coding-Theoretic Approach with Application to Expansionless Near-Threshold Schemes.**
  2020 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-030-45721-1_18)
  Ronald Cramer, Chaoping Xing

- **An Optimal Distributed Discrete Log Protocol with Applications to Homomorphic Secret Sharing.**
  2020 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-019-09330-2)
  Ohad Klein, Nathan Keller, Itai Dinur

- **1/p-Secure Multiparty Computation without an Honest Majority and the Best of Both Worlds.**
  2020 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-020-09354-Z)
  Ilan Orlov, Eran Omri, Yehuda Lindell, Amos Beimel
