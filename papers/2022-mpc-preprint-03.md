# 2022 · MPC · 仅预印本来源 · 第 3/4 页

[总目录](../PAPERS.md) · [上一页](2022-mpc-preprint-02.md) · [下一页](2022-mpc-preprint-04.md)

- **Finding and Evaluating Parameters for BGV**
  2022-06-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/706)
  Johannes Mono, Chiara Marcolla, Georg Land, Tim Güneysu, Najwa Aaraj

  <details><summary>摘要 / Abstract</summary>

  Fully Homomorphic Encryption (FHE) is a groundbreaking technology that allows for arbitrary computations to be performed on encrypted data. State-of-the-art schemes such as Brakerski Gentry Vaikuntanathan (BGV) are based on the Learning with Errors over rings (RLWE) assumption, and each ciphertext has an associated error that grows with each homomorphic operation. For correctness, the error needs to stay below a certain threshold, requiring a trade-off between security and error margin for computations in the parameters. Choosing the parameters accordingly, for example, the polynomial degree or the ciphertext modulus, is challenging and requires expert knowledge specific to each scheme. In this work, we improve the parameter generation process across all steps of its process. We provide a comprehensive analysis for BGV in the Double Chinese Remainder Theorem (DCRT) representation providing more accurate and better bounds than previous work on the DCRT, and empirically derive a closed formula linking the security level, the polynomial degree, and the ciphertext modulus. Additionally, we introduce new circuit models and combine our theoretical work in an easy-to-use parameter generator for researchers and practitioners interested in using BGV for secure computation. Our formula results in better security estimates than previous closed formulas, while our DCRT analysis results in reduced prime sizes of up to 42% compared to previous work.

  匹配依据：MPC: secure computation

  </details>

- **Proof-of-possession for KEM certificates using verifiable generation**
  2022-06-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/703)
  Tim Güneysu, Philip Hodges, Georg Land, Mike Ounsworth, Douglas Stebila, Greg Zaverucha

  <details><summary>摘要 / Abstract</summary>

  Certificate authorities in public key infrastructures typically require entities to prove possession of the secret key corresponding to the public key they want certified. While this is straightforward for digital signature schemes, the most efficient solution for public key encryption and key encapsulation mechanisms (KEMs) requires an interactive challenge-response protocol, requiring a departure from current issuance processes. In this work we investigate how to non-interactively prove possession of a KEM secret key, specifically for lattice-based KEMs, motivated by the recently proposed KEMTLS protocol which replaces signature-based authentication in TLS 1.3 with KEM-based authentication. Although there are various zero-knowledge (ZK) techniques that can be used to prove possession of a lattice key, they yield large proofs or are inefficient to generate. We propose a technique called verifiable generation, in which a proof of possession is generated at the same time as the key itself is generated. Our technique is inspired by the Picnic signature scheme and uses the multi-party-computation-in-the-head (MPCitH) paradigm; this similarity to a signature scheme allows us to bind attribute data to the proof of possession, as required by certificate issuance protocols. We show how to instantiate this approach for two lattice-based KEMs in Round 3 of the NIST post-quantum cryptography standardization project, Kyber and FrodoKEM, and achieve reasonable proof sizes and performance. Our proofs of possession are faster and an order of magnitude smaller than the previous best MPCitH technique for knowledge of a lattice key, and in size-optimized cases can be comparable to even state-of-the-art direct lattice-based ZK proofs for Kyber. Our approach relies on a new result showing the uniqueness of Kyber and FrodoKEM secret keys, even if the requirement that all secret key components are small is partially relaxed, which may be of independent interest for improving efficiency of zero-knowledge proofs for other lattice-based statements.

  匹配依据：MPC: multi party computation

  </details>

- **State Machine Replication under Changing Network Conditions**
  2022-06-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/698)
  Andreea B. Alexandru, Erica Blum, Jonathan Katz, Julian Loss

  <details><summary>摘要 / Abstract</summary>

  Protocols for state machine replication (SMR) are typically designed for synchronous or asynchronous networks, with a lower corruption threshold in the latter case. Recent network-agnostic protocols are secure when run in either a synchronous or an asynchronous network. We propose two new constructions of network-agnostic SMR protocols that improve on existing protocols in terms of either the adversarial model or communication complexity: 1. an adaptively secure protocol with optimal corruption thresholds and quadratic amortized communication complexity per transaction; 2. a statically secure protocol with near-optimal corruption thresholds and linear amortized communication complexity per transaction. We further explore SMR protocols run in a network that may change between synchronous and asynchronous arbitrarily often; parties can be uncorrupted (as in the proactive model), and the protocol should remain secure as long as the appropriate corruption thresholds are maintained. We show that purely asynchronous proactive secret sharing is impossible without some form of synchronization between the parties, ruling out a natural approach to proactively secure network-agnostic SMR protocols. Motivated by this negative result, we consider a model where the adversary is limited in the total number of parties it can corrupt over the duration of the protocol and show, in this setting, that our SMR protocols remain secure even under arbitrarily changing network conditions.

  匹配依据：MPC: secret sharing

  </details>

- **Authentication in the Bounded Storage Model**
  2022-05-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/690)
  Yevgeniy Dodis, Willy Quach, Daniel Wichs

  <details><summary>摘要 / Abstract</summary>

  We consider the streaming variant of the Bounded Storage Model (BSM), where the honest parties can stream large amounts of data to each other, while only maintaining a small memory of size $n$. The adversary also operates as a streaming algorithm, but has a much larger memory size $m \gg n$. The goal is to construct unconditionally secure cryptographic schemes in the BSM, and prior works did so for symmetric-key encryption, key agreement, oblivious transfer and multiparty computation. In this work, we construct message authentication and signatures in the BSM. First, we consider the symmetric-key setting, where Alice and Bob share a small secret key. Alice can authenticate arbitrarily many messages to Bob by streaming long authentication tags of size $k \gg m$, while ensuring that the tags can be generated and verified using only $n$ bits of memory. We show a solution using local extractors (Vadhan; JoC &#x27;04), which allows for up to exponentially large adversarial memory $m = 2^{O(n)}$, and has tags of size $k= O(m)$. Second, we consider the same setting as above, but now additionally require each individual tag to be small, of size $k \leq n$. We show a solution is still possible when the adversary&#x27;s memory is $m = O(n^2)$, which is optimal. Our solution relies on a space lower bound for leaning parities (Raz; FOCS &#x27;16). Third, we consider the public-key signature setting. A signer Alice initially streams a long verification key over an authentic channel, while only keeping a short signing key in her memory. A verifier Bob receives the streamed verification key and generates some short verification digest that he keeps in his memory. Later, Alice can sign arbitrarily many messages using her signing key by streaming the signatures to Bob, who can verify them using his verification digest. We show a solution for $m= O(n^2)$, which we show to be optimal. Our solution relies on a novel entropy lemma, of independent interest. We show that, if a sequence of blocks has sufficiently high min-entropy, then a large fraction of individual blocks must have high min-entropy. Naive versions of this lemma are false, but we show how to patch it to make it hold.

  匹配依据：MPC: multiparty computation, oblivious transfer

  </details>

- **Refuting the Dream XOR Lemma via Ideal Obfuscation and Resettable MPC**
  2022-05-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/681)
  Saikrishna Badrinarayanan, Yuval Ishai, Dakshita Khurana, Amit Sahai, Daniel Wichs

  <details><summary>摘要 / Abstract</summary>

  We provide counterexamples to the ``dream&#x27;&#x27; version of Yao&#x27;s XOR Lemma. In particular, we put forward explicit candidates for hard predicates, such that the advantage of predicting the XOR of many independent copies does not decrease beyond some fixed negligible function, even as the number of copies gets arbitrarily large. We provide two such constructions: 1) Our first construction is in the ideal obfuscation model (alternatively, assuming virtual black-box obfuscation for a concrete class of circuits). It develops a general framework that may be of broader interest, and allows us to embed an instance of a resettably-secure multiparty computation protocol into a one-way function. Along the way, we design the first resettably-secure multiparty computation protocol for general functionalities in the plain model with super-polynomial simulation, under standard assumptions. 2) The second construction relies on public-coin differing-inputs obfuscation (PCdiO) along with a certain form of hash-function security called extended second-preimage resistance (ESPR). It starts with a previously known counterexample to the dream direct-product hardness amplification based on ESPR, and uses PCdiO to upgrade it into a counterexample for the XOR lemma. Prior to our work, even completely heuristic counterexamples of this type were not known.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Unified Approach to Secret Sharing and Symmetric Private Information Retrieval with Colluding Servers in Quantum Systems**
  2022-05-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.14622)
  Masahito Hayashi, Seunghoan Song

  <details><summary>摘要 / Abstract</summary>

  This paper unifiedly addresses two kinds of key quantum secure tasks, i.e., quantum versions of secret sharing (SS) and symmetric private information retrieval (SPIR) by using multi-target monotone span program (MMSP), which characterizes the classical linear protocols of SS and SPIR. SS has two quantum extensions; One is the classical-quantum (CQ) setting, in which the secret to be sent is classical information and the shares are quantum systems. The other is the quantum-quantum (QQ) setting, in which the secret to be sent is a quantum state and the shares are quantum systems. The relation between these quantum protocols and MMSP has not been studied sufficiently. We newly introduce the third setting, i.e., the entanglement-assisted (EA) setting, which is defined by modifying the CQ setting with allowing prior entanglement between the dealer and the end-user who recovers the secret by collecting the shares. Showing that the linear version of SS with the EA setting is directly linked to MMSP, we characterize linear quantum versions of SS with the CQ ad QQ settings via MMSP. Further, we introduce the EA setting of SPIR, which is shown to link to MMSP. In addition, we discuss the quantum version of maximum distance separable codes.

  匹配依据：MPC: secret sharing

  </details>

- **Practical UC-Secure Zero-Knowledge Smart Contracts**
  2022-05-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/670)
  Jayamine Alupotha, Xavier Boyen

  <details><summary>摘要 / Abstract</summary>

  Zero-knowledge defines that verifier(s) learns nothing but predefined statement(s); e.g., verifiers learn nothing except the program&#x27;s path for the respective transaction in a zero-knowledge contract program. Intra-Privacy or insiders&#x27; zero-knowledge --- ability to maintain a secret in a multi-party computation --- is an essential security property for smart contracts of Confidential Transactions (CT). Otherwise, the users have to reveal their confidential coin amounts to each other even if it is not a condition of the contract, contradicting the idea of zero-knowledge. For example, in an escrow contract, the escrow should not learn buyers&#x27; or sellers&#x27; account balances if the escrow has to pay into their accounts. Current private computational platforms, including homomorphic encryption and (ZK-)SNARK, can not be used in CT&#x27;s smart contracts because homomorphic encryption requires secret key sharing, and (ZK-)SNARK requires a different setup for each computation which has to be stored on the blockchain. Existing private smart contracts are not intra-private even though they are inter-private --- participants can maintain secrets from verifiers but not from other participants, accordingly. To fill this research gap, we introduce the notion of ``Confidential Integer Processing&#x27;&#x27; (CIP) with two intra-private single-setup zero-knowledge programming protocols, (1) ``CIP-DLP&#x27;&#x27; from the Discrete Log Problem (DLP) targeting Ring/Aggregable CT like Monero and Mimblewimble, and (2) ``CIP-SIS&#x27;&#x27; from Approximate (Ring-Modular-) Short Integer Solution Problem (Approx-SIS) aiming at lattice-based Ring/Aggregable CT. To the best of our knowledge, our CIP protocols are the first practical public zero-knowledge contract protocols that are also secure under the Universal Composability (UC) framework without any hardware magic or trusted offline computations.

  匹配依据：MPC: multi party computation

  </details>

- **SafeNet: The Unreasonable Effectiveness of Ensembles in Private Collaborative Learning**
  2022-05-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.09986) · [IACR ePrint](https://eprint.iacr.org/2022/663)
  Harsh Chaudhari, Matthew Jagielski, Alina Oprea

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) has been proposed to allow multiple mutually distrustful data owners to jointly train machine learning (ML) models on their combined data. However, by design, MPC protocols faithfully compute the training functionality, which the adversarial ML community has shown to leak private information and can be tampered with in poisoning attacks. In this work, we argue that model ensembles, implemented in our framework called SafeNet, are a highly MPC-amenable way to avoid many adversarial ML attacks. The natural partitioning of data amongst owners in MPC training allows this approach to be highly scalable at training time, provide provable protection from poisoning attacks, and provably defense against a number of privacy attacks. We demonstrate SafeNet&#x27;s efficiency, accuracy, and resilience to poisoning on several machine learning datasets and models trained in end-to-end and transfer learning scenarios. For instance, SafeNet reduces backdoor attack success significantly, while achieving $39\times$ faster training and $36 \times$ less communication than the four-party MPC framework of Dalskov et al. Our experiments show that ensembling retains these benefits even in many non-iid settings. The simplicity, cheap setup, and robustness properties of ensembling make it a strong first choice for training ML models privately in MPC.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Arithmetic Tuples for MPC**
  2022-05-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/667)
  Pascal Reisert, Marc Rivinius, Toomas Krips, Ralf Küsters

  <details><summary>摘要 / Abstract</summary>

  Some of the most efficient protocols for Multi-Party Computation (MPC) use a two-phase approach where correlated randomness, in particular Beaver triples, is generated in the offline phase and then used to speed up the online phase. Recently, more complex correlations have been introduced to optimize certain operations even further, such as matrix triples for matrix multiplications. In this paper, our goal is to speed up the evaluation of multivariate polynomials and therewith of whole arithmetic circuits in the online phase. To this end, we introduce a new form of correlated randomness: arithmetic tuples. Arithmetic tuples can be fine tuned in various ways to the constraints of application at hand, in terms of round complexity, bandwidth, and tuple size. We show that for many real-world setups an arithmetic tuples based online phase outperforms state-of-the-art protocols based on Beaver triples.

  匹配依据：MPC: multi party computation

  </details>

- **Evolution as a Service: A Privacy-Preserving Genetic Algorithm for Combinatorial Optimization**
  2022-05-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.13948)
  Bowen Zhao, Wei-Neng Chen, Feng-Feng Wei, Ximeng Liu, Qingqi Pei, Jun Zhang

  <details><summary>摘要 / Abstract</summary>

  Evolutionary algorithms (EAs), such as the genetic algorithm (GA), offer an elegant way to handle combinatorial optimization problems (COPs). However, limited by expertise and resources, most users do not have enough capability to implement EAs to solve COPs. An intuitive and promising solution is to outsource evolutionary operations to a cloud server, whilst it suffers from privacy concerns. To this end, this paper proposes a novel computing paradigm, evolution as a service (EaaS), where a cloud server renders evolutionary computation services for users without sacrificing users&#x27; privacy. Inspired by the idea of EaaS, this paper designs PEGA, a novel privacy-preserving GA for COPs. Specifically, PEGA enables users outsourcing COPs to the cloud server holding a competitive GA and approximating the optimal solution in a privacy-preserving manner. PEGA features the following characteristics. First, any user without expertise and enough resources can solve her COPs. Second, PEGA does not leak contents of optimization problems, i.e., users&#x27; privacy. Third, PEGA has the same capability as the conventional GA to approximate the optimal solution. We implements PEGA falling in a twin-server architecture and evaluates it in the traveling salesman problem (TSP, a widely known COP). Particularly, we utilize encryption cryptography to protect users&#x27; privacy and carefully design a suit of secure computing protocols to support evolutionary operators of GA on encrypted data. Privacy analysis demonstrates that PEGA does not disclose the contents of the COP to the cloud server. Experimental evaluation results on four TSP datasets show that PEGA is as effective as the conventional GA in approximating the optimal solution.

  匹配依据：MPC: secure computing

  </details>

- **BASALISC: Programmable Hardware Accelerator for BGV Fully Homomorphic Encryption**
  2022-05-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.14017) · [IACR ePrint](https://eprint.iacr.org/2022/657)
  Robin Geelen, Michiel Van Beirendonck, Hilder V. L. Pereira, Brian Huffman, Tynan McAuley, Ben Selfridge, Daniel Wagner, Georgios Dimou, Ingrid Verbauwhede, Frederik Vercauteren, David W. Archer

  <details><summary>摘要 / Abstract</summary>

  Fully Homomorphic Encryption (FHE) allows for secure computation on encrypted data. Unfortunately, huge memory size, computational cost and bandwidth requirements limit its practicality. We present BASALISC, an architecture family of hardware accelerators that aims to substantially accelerate FHE computations in the cloud. BASALISC is the first to implement the BGV scheme with fully-packed bootstrapping – the noise removal capability necessary for arbitrary-depth computation. It supports a customized version of bootstrapping that can be instantiated with hardware multipliers optimized for area and power. BASALISC is a three-abstraction-layer RISC architecture, designed for a 1 GHz ASIC implementation and underway toward 150mm2 die tape-out in a 12nm GF process. BASALISC&#x27;s four-layer memory hierarchy includes a two-dimensional conflict-free inner memory layer that enables 32 Tb/s radix-256 NTT computations without pipeline stalls. Its conflict-resolution permutation hardware is generalized and re-used to compute BGV automorphisms without throughput penalty. BASALISC also has a custom multiply-accumulate unit to accelerate BGV key switching. The BASALISC toolchain comprises a custom compiler and a joint performance and correctness simulator. To evaluate BASALISC, we study its physical realizability, emulate and formally verify its core functional units, and we study its performance on a set of benchmarks. Simulation results show a speedup of more than 5,000× over HElib – a popular software FHE library.

  匹配依据：MPC: secure computation

  </details>

- **Revisiting the Efficiency of Asynchronous Multi Party Computation Against General Adversaries**
  2022-05-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.13169) · [IACR ePrint](https://eprint.iacr.org/2022/651)
  Ananya Appan, Anirudh Chandramouli, Ashish Choudhury

  <details><summary>摘要 / Abstract</summary>

  In this paper, we design secure multi-party computation (MPC) protocols in the asynchronous communication setting with optimal resilience. Our protocols are secure against a computationally-unbounded malicious adversary, characterized by an adversary structure $\mathcal{Z}$, which enumerates all possible subsets of potentially corrupt parties. Our protocols incur a communication of $\mathcal{O}(|\mathcal{Z}|^2)$ and $\mathcal{O}(|\mathcal{Z}|)$ bits per multiplication for perfect and statistical security respectively. These are the first protocols with this communication complexity, as such protocols were known only in the synchronous communication setting (Hirt and Tschudi, ASIACRYPT 2013).

  匹配依据：MPC: multi party computation, secure multi party computation

  </details>

- **Private Set Operations from Multi-Query Reverse Private Membership Test**
  2022-05-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/652)
  Yu Chen, Min Zhang, Cong Zhang, Minglang Dong, Weiran Liu

  <details><summary>摘要 / Abstract</summary>

  Private set operations allow two parties to perform secure computation on their private sets, including intersection, union and functions of intersection/union. In this paper, we put forth a framework to perform private set operations. The technical core of our framework is the multi-query reverse private membership test (mqRPMT) protocol (Zhang et al., USENIX Security 2023), in which a client with a vector $X = (x_1, \dots, x_n)$ interacts with a server holding a set $Y$, and eventually the server learns only a bit vector $(e_1, \dots, e_n)$ indicating whether $x_i \in Y$ without learning the value of $x_i$, while the client learns nothing. We present two constructions of mqRPMT from newly introduced cryptographic notions, one is based on commutative weak pseudorandom function (cwPRF), and the other is based on permuted oblivious pseudorandom function (pOPRF). Both cwPRF and pOPRF can be realized from the decisional Diffie-Hellman (DDH)-like assumptions in the random oracle model. We also introduce a slightly weaker version of mqRPMT dubbed mqRPMT$^*$, in which the client also learns the cardinality of $X \cap Y$. We show that mqRPMT$^*$ can be built from a category of multi-query private membership test (mqPMT) called Sigma-mqPMT, which in turn can be realized from DDH-like assumptions or oblivious polynomial evaluation. This makes the first step towards establishing the relation between mqPMT and mqRPMT. We demonstrate the practicality of our framework with implementations. By plugging our cwPRF-based mqRPMT into the framework, we obtain various PSO protocols that are superior or competitive to the state-of-the-art protocols. For intersection functionality, our protocol is faster than the most efficient one for small sets. For cardinality functionality, our protocol achieves a $2.4-10.5\times$ speedup and a $10.9-14.8\times$ shrink in communication cost. For cardinality-with-sum functionality, our protocol achieves a $28.5-76.3\times$ speedup and $7.4\times$ shrink in communication cost. For union functionality, our protocol is the first one that attains strict linear complexity, and requires the lowest concrete computation and communication costs in all settings, achieving a $2.7-17\times$ speedup and about $2\times$ shrink in communication cost. Specifically, for input sets of size $2^{20}$, our PSU protocol requires roughly 100 MB of communication and 16 seconds using 4 threads on a laptop in the LAN setting. Our improvement on PSU also translates to related functionality, yielding the most efficient private-ID protocol to date. Moreover, by plugging our FHE-based mqRPMT$^*$ to the general framework, we obtain a PSU$^*$ protocol (the sender additionally learns the intersection size) suitable for unbalanced setting, whose communication complexity is linear in the size of the smaller set and logarithmic in the larger set.

  匹配依据：MPC: secure computation

  </details>

- **Privacy-Preserving Wavelet Neural Network with Fully Homomorphic Encryption**
  2022-05-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.13265)
  Syed Imtiaz Ahamed, Vadlamani Ravi

  <details><summary>摘要 / Abstract</summary>

  The main aim of Privacy-Preserving Machine Learning (PPML) is to protect the privacy and provide security to the data used in building Machine Learning models. There are various techniques in PPML such as Secure Multi-Party Computation, Differential Privacy, and Homomorphic Encryption (HE). The techniques are combined with various Machine Learning models and even Deep Learning Networks to protect the data privacy as well as the identity of the user. In this paper, we propose a fully homomorphic encrypted wavelet neural network to protect privacy and at the same time not compromise on the efficiency of the model. We tested the effectiveness of the proposed method on seven datasets taken from the finance and healthcare domains. The results show that our proposed model performs similarly to the unencrypted model.

  匹配依据：MPC: secure multi party computation

  </details>

- **IBE with Incompressible Master Secret and Small Identity Secrets**
  2022-05-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/649)
  Nico Döttling, Sanjam Garg, Sruthi Sekar, Mingyuan Wang

  <details><summary>摘要 / Abstract</summary>

  Side-stepping the protection provided by cryptography, exfiltration attacks are becoming a considerable real-world threat. With the goal of mitigating the exfiltration of cryptographic keys, big-key cryptosystems have been developed over the past few years. These systems come with very large secret keys which are thus hard to exfiltrate. Typically, in such systems, the setup time must be large as it generates the large secret key. However, subsequently, the encryption and decryption operations, that must be performed repeatedly, are required to be efficient. Specifically, the encryption uses only a small public key and the decryption only accesses small ciphertext-dependent parts of the full secret key. Nonetheless, these schemes require decryption to have access to the entire secret key. Thus, using such big-key cryptosystems necessitate that users carry around large secret keys on their devices, which can be a hassle and in some cases might also render exfiltration easy. With the goal of removing this problem, in this work, we initiate the study of big-key identity-based encryption (bk-IBE). In such a system, the master secret key is allowed to be large but we require that the identity-based secret keys are short. This allows users to use the identity-based short keys as the ephemeral secret keys that can be more easily carried around and allow for decrypting ciphertexts matching a particular identity, e.g. messages that were encrypted on a particular date. In particular: -We build a new definitional framework for bk-IBE capturing a range of applications. In the case when the exfiltration is small our definition promises stronger security --- namely, an adversary can break semantic security for only a few identities, proportional to the amount of leakage it gets. In contrast, in the catastrophic case where a large fraction of the master secret key has been ex-filtrated, we can still resort to a guarantee that the ciphertexts generated for a randomly chosen identity (or, an identity with enough entropy) remain protected. We demonstrate how this framework captures the best possible security guarantees. -We show the first construction of such a bk-IBE offering strong security properties. Our construction is based on standard assumptions on groups with bilinear pairings and brings together techniques from seemingly different contexts such as leakage resilient cryptography, reusable two-round MPC, and laconic oblivious transfer. We expect our techniques to be of independent interest.

  匹配依据：MPC: oblivious transfer

  </details>

- **Privacy and correctness trade-offs for information-theoretically secure quantum homomorphic encryption**
  2022-05-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.12127)
  Yanglin Hu, Yingkai Ouyang, Marco Tomamichel

  <details><summary>摘要 / Abstract</summary>

  Quantum homomorphic encryption, which allows computation by a server directly on encrypted data, is a fundamental primitive out of which more complex quantum cryptography protocols can be built. For such constructions to be possible, quantum homomorphic encryption must satisfy two privacy properties: data privacy which ensures that the input data is private from the server, and circuit privacy which ensures that the ciphertext after the computation does not reveal any additional information about the circuit used to perform it, beyond the output of the computation itself. While circuit privacy is well-studied in classical cryptography and many homomorphic encryption schemes can be equipped with it, its quantum analogue has received little attention. Here we establish a definition of circuit privacy for quantum homomorphic encryption with information-theoretic security. Furthermore, we reduce quantum oblivious transfer to quantum homomorphic encryption. By using this reduction, our work unravels fundamental trade-offs between circuit privacy, data privacy and correctness for a broad family of quantum homomorphic encryption protocols, including schemes that allow only the computation of Clifford circuits.

  匹配依据：MPC: oblivious transfer

  </details>

- **PrivFairFL: Privacy-Preserving Group Fairness in Federated Learning**
  2022-05-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.11584)
  Sikha Pentyala, Nicola Neophytou, Anderson Nascimento, Martine De Cock, Golnoosh Farnadi

  <details><summary>摘要 / Abstract</summary>

  Group fairness ensures that the outcome of machine learning (ML) based decision making systems are not biased towards a certain group of people defined by a sensitive attribute such as gender or ethnicity. Achieving group fairness in Federated Learning (FL) is challenging because mitigating bias inherently requires using the sensitive attribute values of all clients, while FL is aimed precisely at protecting privacy by not giving access to the clients&#x27; data. As we show in this paper, this conflict between fairness and privacy in FL can be resolved by combining FL with Secure Multiparty Computation (MPC) and Differential Privacy (DP). In doing so, we propose a method for training group-fair ML models in cross-device FL under complete and formal privacy guarantees, without requiring the clients to disclose their sensitive attribute values.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Honorific Security: Efficient Two-Party Computation with Offloaded Arbitration and Public Verifiability**
  2022-05-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/606)
  Tianxiang Dai, Yufan Jiang, Yong Li, Jörn Müller-Quade, Andy Rupp

  <details><summary>摘要 / Abstract</summary>

  Secure two-party computation (2PC) allows two distrustful parties to jointly compute some functions while keeping their private secrets unrevealed. Adversaries are often categorized as semi-honest and malicious, depending on whether they follow the protocol specifications or not. While a semi-honest secure protocol is fast but strongly assumed that all participants will follow the protocol, a malicious protocol often requires heavy verification steps and preprocessing phase to prohibit any cheat. Covert security [10] was first introduced by Aumann and Lindell, which looks into the &quot;middle ground&quot; between semi-honest security and malicious security, such that active adversaries who cheat will be caught with a predefined probability. However, it is still an open question that how to properly determine such a probability before protocol execution, and the misbehavior detection must be made by other honest participants with cut-and-choose in current constructions. To achieve public verifiability and meanwhile outsource the verification steps, [12] presented publicly auditable security to enable an external auditor to verify the result correctness. Essentially, an additional existence assumption of a bulletin board functionality is required to keep tracking the broadcasted messages for the auditor. And moreover, the auditor cannot identify the cheater, but only points out the incorrect result. The (robust) accountability family [40, 62, 76] achieves both output delivery guarantee and public verifiability, which relies on heavy offline and online constructions with zero knowledge proofs. In this paper, we propose a new security notion called honorific security, where an external arbiter can find the cheater with overwhelming probability under the malicious corruption. With honorific security, we do not prohibit cheat of a corrupted party during the online stage, but enable the honest party to detect and punish the cheater later on in public. We show that a maliciously secure garbled circuit (GC) [83] protocol can thus be constructed with only slightly more overhead than a passively secure protocol. Our construction performs up to 2.37 times and 13.30 times as fast as the state-of-the-art protocols with covert and malicious security, respectively.

  匹配依据：MPC: garbled circuit, secure two party computation, two party computation

  </details>

- **Feel the Quantum Functioning: Instantiating Generic Multi-Input Functional Encryption from Learning with Errors (extended version)?**
  2022-05-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/629)
  Alexandros Bakas, Antonis Michalas, Eugene Frimpong, Reyhaneh Rabbaninejad

  <details><summary>摘要 / Abstract</summary>

  Functional Encryption (FE) allows users who hold a specific decryption key, to learn a specific function of encrypted data while the actual plaintexts remain private. While FE is still in its infancy, it is our strong belief that in the years to come, this remarkable cryptographic primitive will have matured to the degree that will make it an integral part of access control systems, especially cloud-based ones. To this end, we believe it is of great importance to provide not only theoretical and generic constructions but also concrete instantiations of FE schemes from well-studied cryptographic assumptions. Therefore, in this paper, we undertake the task of presenting two instantiations of the generic work presented in [8] from the Decisional Diffie-Hellman (DDH) problem that also satisfies the property of verifiable decryption. Moreover, we present a novel multi-input FE (MIFE) scheme, that can be instantiated from Regev&#x27;s cryptosystem, and thus remains secure even against quantum adversaries. Finally, we provide a multi-party computation (MPC) protocol that allows our MIFE construction to be deployed in the multi-client mode

  匹配依据：MPC: multi party computation

  </details>

- **Breaking the $t&lt; n/3$ Consensus Bound: Asynchronous Dynamic Proactive Secret Sharing under Honest Majority**
  2022-05-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/619)
  Christophe Levrat, Matthieu Rambaud, Antoine Urban

  <details><summary>摘要 / Abstract</summary>

  A proactive secret sharing scheme (PSS), expressed in the dynamic-membership setting, enables a committee of n holders of secret-shares, dubbed as players, to securely hand-over new shares of the same secret to a new committee. We dub such a sub-protocol as a Refresh. All existing PSS under an honest majority, require the use of a broadcast (BC) in each refresh. BC is costly to implement, and its security relies on timing assumptions on the network. So the privacy of the secret and/or its guaranteed delivery, either depend on network assumptions, or, on the reliability of a public ledger. By contrast, PSS over asynchronous channels do not have these constraints. However, all of them (but one, with exponential complexity) use asynchronous verifiable secret sharing (AVSS) and consensus (MVBA and/or ACS), which are impossible under asynchrony beyond t&lt;n/3 corruptions, whatever the setup. We present a PSS, named asynchronous-proactive secret sharing (APSS), which is the first PSS under honest majority with guaranteed output delivery in a completely asynchronous network. More generally, APSS allows any flexible threshold $t&lt;n$, such that privacy and correctness are guaranteed up to t corruptions, and liveness as soon as $t+1$ players behave honestly. Correctness can be lifted to any number of corruptions, provided a linearly homomorphic commitment scheme. Moreover, each refresh completes at the record speed of $2\delta$, where $\delta$ is the actual message delivery delay. APSS demonstrates that proactive refreshes are possible as long as players of the initial committee only, have a common view on a set of (publicly committed or encrypted) shares. Despite not providing consensus on a unique set of shares, APSS surprisingly enables the opening of any linear map over secrets { non-interactively, without consensus }. This, in turn, applies to threshold signing, decryption and randomness generation. APSS can also be directly integrated into the asynchronous Schnorr threshold signing scheme &quot;Roast&quot; [CCS&#x27;22]. Of independent interest, we: - provide the first UC formalization (and proof) of proactive AVSS, furthermore for arbitrary thresholds; - provide additional mechanisms enabling players of a committee to start a refresh then erase their old shares, synchronously up to $\delta$ from each other; - improve by 50x the verification speed of the NIZKs of encrypted re-sharing of [Cascudo et al, Asiacrypt&#x27;22], by using novel optimizations of batch Schnorr proofs of knowledge. We demonstrate efficiency of APSS with an implementation which uses this optimization as baseline.

  匹配依据：MPC: secret sharing

  </details>

- **Secure Order Based Voting Using Distributed Tallying**
  2022-05-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.10580)
  Tamir Tassa, Lihi Dery, Arthur Zamarin

  <details><summary>摘要 / Abstract</summary>

  Electronic voting systems have significant advantages in comparison with physical voting systems. One of the main challenges in e-voting systems is to secure the voting process: namely, to certify that the computed results are consistent with the cast ballots and that the voters&#x27; privacy is preserved. We propose herein a secure voting protocol for elections that are governed by order-based voting rules. Our protocol, in which the tallying task is distributed among several independent talliers, offers perfect ballot secrecy in the sense that it issues only the required output while no other information on the cast ballots is revealed. Such perfect secrecy, achieved by employing secure multiparty computation tools, may increase the voters&#x27; confidence and, consequently, encourage them to vote according to their true preferences. We implemented a demo of a voting system that is based on our protocol and we describe herein the system&#x27;s components and its operation. Our implementation demonstrates that our secure order-based voting protocol can be readily implemented in real-life large-scale electronic elections.

  匹配依据：MPC: secure multiparty computation

  </details>

- **A New Metric and Its Scheme Construction for Evolving $2$-Threshold Secret Sharing Schemes**
  2022-05-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.10614)
  Wei Yan, Sian-Jheng Lin

  <details><summary>摘要 / Abstract</summary>

  Evolving secret sharing schemes do not require prior knowledge of the number of parties $n$ and $n$ may be infinitely countable. It is known that the evolving $2$-threshold secret sharing scheme and prefix coding of integers have a one-to-one correspondence. However, it is not known what prefix coding of integers to use to construct the scheme better. In this paper, we propose a new metric $K_Σ$ for evolving $2$-threshold secret sharing schemes $Σ$. We prove that the metric $K_Σ\geq 1.5$ and construct a new prefix coding of integers, termed $λ$ code, to achieve the metric $K_Λ=1.59375$. Thus, it is proved that the range of the metric $K_Σ$ for the optimal $(2,\infty)$-threshold secret sharing scheme is $1.5\leq K_Σ\leq1.59375$. In addition, the reachable lower bound of the sum of share sizes for $(2,n)$-threshold secret sharing schemes is proved.

  匹配依据：MPC: secret sharing

  </details>

- **Federated learning: Applications, challenges and future directions**
  2022-05-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.09513)
  Subrato Bharati, M. Rubaiyat Hossain Mondal, Prajoy Podder, V. B. Surya Prasath

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) is a system in which a central aggregator coordinates the efforts of multiple clients to solve machine learning problems. This setting allows training data to be dispersed in order to protect privacy. The purpose of this paper is to provide an overview of FL systems with a focus on healthcare. FL is evaluated here based on its frameworks, architectures, and applications. It is shown here that FL solves the preceding issues with a shared global deep learning (DL) model via a central aggregator server. This paper examines recent developments and provides a comprehensive list of unresolved issues, inspired by the rapid growth of FL research. In the context of FL, several privacy methods are described, including secure multiparty computation, homomorphic encryption, differential privacy, and stochastic gradient descent. Furthermore, a review of various FL classes, such as horizontal and vertical FL and federated transfer learning, is provided. FL has applications in wireless communication, service recommendation, intelligent medical diagnosis systems, and healthcare, all of which are discussed in this paper. We also present a thorough review of existing FL challenges, such as privacy protection, communication cost, system heterogeneity, and unreliable model upload, followed by future research directions.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Secure Merge in Linear Time and O(log log N) Rounds**
  2022-05-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/590)
  Mark Blunk, Paul Bunn, Samuel Dittmer, Steve Lu, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  The problem of Secure Merge consists of combining two sorted lists (which are either held separately by two parties, or secret-shared among two or more parties), and outputting a single merged (sorted) list, secret-shared among all parties. Just as insecure algorithms for comparison-based sorting are slower than merging (i.e., for lists of size $n$, $\Theta(n \log n)$ versus $\Theta(n)$), we explore whether the analogous separation exists for secure protocols; namely, if there exist techniques for performing secure merge that are more performant than simply invoking a secure multiparty sort. We answer this question affirmatively by constructing a semi-honest protocol with optimal $\Theta(n)$ communication and computation, and $\Theta(\log \log n)$ rounds of communication. Our results are based solely on black-box use of basic secure primitives, such as secure comparison and secure shuffle. Since two-party secure primitives require computational assumptions, while three-party secure primitive do not, our result imply a computationally secure two-party secure merge protocol and an information-theoretically secure three-party secure merge protocol with these bounds. Secure sort is a fundamental building block used in many MPC protocols, e.g., various private set intersection protocols and oblivious RAM protocols. More efficient secure sort can lead to concrete improvements in the overall run-time. Since secure sort can often be replaced by secure merge -- since inputs (from different participating players) can be presorted -- an efficient secure merge protocol has wide applicability. There are also a range of applications in the field of secure databases, including secure database joins, as well as updatable database storage and search, whereby secure merge can be used to insert new entries into an existing (sorted) database. In building our secure merge protocol, we develop several subprotocols that may be of independent interest. For example, we develop a protocol for secure asymmetric merge (where one list is much larger than the other).

  匹配依据：MPC: private set intersection

  </details>

- **Privacy Preserving Image Registration**
  2022-05-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.10120)
  Riccardo Taiello, Melek Önen, Francesco Capano, Olivier Humbert, Marco Lorenzi

  <details><summary>摘要 / Abstract</summary>

  Image registration is a key task in medical imaging applications, allowing to represent medical images in a common spatial reference frame. Current approaches to image registration are generally based on the assumption that the content of the images is usually accessible in clear form, from which the spatial transformation is subsequently estimated. This common assumption may not be met in practical applications, since the sensitive nature of medical images may ultimately require their analysis under privacy constraints, preventing to openly share the image content.In this work, we formulate the problem of image registration under a privacy preserving regime, where images are assumed to be confidential and cannot be disclosed in clear. We derive our privacy preserving image registration framework by extending classical registration paradigms to account for advanced cryptographic tools, such as secure multi-party computation and homomorphic encryption, that enable the execution of operations without leaking the underlying data. To overcome the problem of performance and scalability of cryptographic tools in high dimensions, we propose several techniques to optimize the image registration operations by using gradient approximations, and by revisiting the use of homomorphic encryption trough packing, to allow the efficient encryption and multiplication of large matrices. We demonstrate our privacy preserving framework in linear and non-linear registration problems, evaluating its accuracy and scalability with respect to standard, non-private counterparts. Our results show that privacy preserving image registration is feasible and can be adopted in sensitive medical imaging applications.

  匹配依据：MPC: secure multi party computation

  </details>

- **Doubly Efficient Interactive Proofs over Infinite and Non-Commutative Rings**
  2022-05-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/587)
  Eduardo Soria-Vazquez

  <details><summary>摘要 / Abstract</summary>

  We introduce the first proof system for layered arithmetic circuits over an arbitrary ring $R$ that is (possibly) non-commutative and (possibly) infinite, while only requiring black-box access to its arithmetic and a subset $A \subseteq R$. Our construction only requires limited commutativity and regularity properties from $A$, similar to recent work on efficient information theoretic multi-party computation over non-commutative rings by Escudero and Soria-Vazquez (CRYPTO 2021), but furthermore covering infinite rings. We achieve our results through a generalization of GKR-style interactive proofs (Goldwasser, Kalai and Rothblum, Journal of the ACM, 2015). When $A$ is a subset of the center of $R$, generalizations of the sum-check protocol and other building blocks are not too problematic. The case when the elements of $A$ only commute with each other, on the other hand, introduces a series of challenges. In order to overcome those, we need to introduce a new definition of polynomial ring over a non-commutative ring, the notion of left (and right) multi-linear extensions, modify the layer consistency equation and adapt the sum-check protocol. Despite these changes, our results are compatible with recent developments such as linear time provers. Moreover, for certain rings our construction achieves provers that run in sublinear time in the circuit size. We obtain such result both for known cases, such as matrix and polynomial rings, as well as new ones, such as for some rings resulting from Clifford algebras. Besides efficiency improvements in computation and/or round complexity for several instantiations, the core conclusion of our results is that state of the art doubly efficient interactive proofs do not require much algebraic structure. This enables exact rather than approximate computation over infinite rings as well as agile proof systems, where the black-box choice of the underlying ring can be easily switched through the software life cycle.

  匹配依据：MPC: multi party computation

  </details>

- **Chaghri --- an FHE-friendly Block Cipher**
  2022-05-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/592)
  Tomer Ashur, Mohammad Mahzoun, Dilara Toprakhisar

  <details><summary>摘要 / Abstract</summary>

  The Recent progress in practical applications of secure computation protocols has also attracted attention to the symmetric-key primitives underlying them. Whereas traditional ciphers have evolved to be efficient with respect to certain performance metrics, advanced cryptographic protocols call for a different focus. The so called arithmetic complexity is viewed through the number and layout of non-linear operations in the circuit implemented by the protocol. Symmetric-key algorithms that are optimized with respect to this metric are said to be algebraic ciphers. Previous work targeting ZK and MPC protocols delivered great improvement in the performance of these applications both in lab and in practical use. Interestingly, despite its apparent benefits to privacy-aware cloud computing, algebraic ciphers targeting FHE did not attract similar attention. In this paper we present Chaghri, an FHE-friendly block cipher enabling efficient transciphering in BGV-like schemes. A complete Chaghri circuit can be implemented using only 16 multiplications, 32 Frobenius automorphisms and 32 rotations, all arranged in a depth-32 circuit. Our HElib implemention achieves a throughput of 0.26 seconds-per-bit which is 65% faster than AES in the same setting.

  匹配依据：MPC: secure computation

  </details>

- **A Nearly Tight Proof of Duc et al.'s Conjectured Security Bound for Masked Implementations**
  2022-05-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/600)
  Loïc Masure, Olivier Rioul, François-Xavier Standaert

  <details><summary>摘要 / Abstract</summary>

  We prove a bound that approaches Duc et al.&#x27;s conjecture from Eurocrypt 2015 for the side-channel security of masked implementations. Let \(Y\) be a sensitive intermediate variable of a cryptographic primitive taking its values in a set \(\mathcal{Y}\). If \(Y\) is protected by masking (a.k.a. secret sharing) at order \(d\) (i.e., with $d+1$ shares), then the complexity of any non-adaptive side-channel analysis --- measured by the number of queries to the target implementation required to guess the secret key with sufficient confidence --- is lower bounded by a quantity inversely proportional to the product of mutual informations between each share of \(Y\) and their respective leakage. Our new bound is nearly tight in the sense that each factor in the product has an exponent of \(-1\) as conjectured, and its multiplicative constant is\(\mathcal{O}\left(\log |\mathcal{Y}| \cdot |\mathcal{Y}|^{-1} \cdot C^{-d}\right)\), where \(C = 2 \log(2) \approx 1.38\). It drastically improves upon previous proven bounds, where the exponent was \(-1/2\), and the multiplicative constant was \(\mathcal{O}\left(|\mathcal{Y}|^{-d}\right)\). As a consequence for side-channel security evaluators, it is possible to provably and efficiently infer the security level of a masked implementation by simply analyzing each individual share, under the necessary condition that the leakage of these shares are independent.

  匹配依据：MPC: secret sharing

  </details>

- **Finding One Common Item, Privately**
  2022-05-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/573)
  Tyler Beauregard, Janabel Xia, Mike Rosulek

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) allows two parties, who each hold a set of items, to learn which items they have in common, without revealing anything about their other items. Some applications of PSI would be better served by revealing only one common item, rather than the entire set of all common items. In this work we develop simple special-purpose protocols for privately finding one common item (FOCI) from the intersection of two sets. The protocols differ in how that item is chosen --- e.g., uniformly at random from the intersection; the &quot;best&quot; item in the intersection according to one party&#x27;s ranking; or the &quot;best&quot; item in the intersection according to the sum of both party&#x27;s scores. All of our protocols are proven secure against semi-honest adversaries, under the Decisional Diffie-Hellman (DDH) assumption and assuming a random oracle. All of our protocols leak a small amount of information (e.g., the cardinality of the intersection), which we precisely quantify.

  匹配依据：MPC: private set intersection

  </details>

- **Digital Blind Box: Random Symmetric Private Information Retrieval**
  2022-05-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.07828)
  Zhusheng Wang, Sennur Ulukus

  <details><summary>摘要 / Abstract</summary>

  We introduce the problem of random symmetric private information retrieval (RSPIR). In canonical PIR, a user downloads a message out of $K$ messages from $N$ non-colluding and replicated databases in such a way that no database can know which message the user has downloaded (user privacy). In SPIR, the privacy is symmetric, in that, not only that the databases cannot know which message the user has downloaded, the user itself cannot learn anything further than the particular message it has downloaded (database privacy). In RSPIR, different from SPIR, the user does not have an input to the databases, i.e., the user does not pick a specific message to download, instead is content with any one of the messages. In RSPIR, the databases need to send symbols to the user in such a way that the user is guaranteed to download a message correctly (random reliability), the databases do not know which message the user has received (user privacy), and the user does not learn anything further than the one message it has received (database privacy). This is the digital version of a blind box, also known as gachapon, which implements the above specified setting with physical objects for entertainment. This is also the blind version of $1$-out-of-$K$ oblivious transfer (OT), an important cryptographic primitive. We study the information-theoretic capacity of RSPIR for the case of $N=2$ databases. We determine its exact capacity for the cases of $K = 2, 3, 4$ messages. While we provide a general achievable scheme that is applicable to any number of messages, the capacity for $K\geq 5$ remains open.

  匹配依据：MPC: oblivious transfer

  </details>

- **Comparison-Based MPC in Star Topology (Full Version)**
  2022-05-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/574)
  Gowri R Chandran, Carmit Hazay, Robin Hundt, Thomas Schneider

  <details><summary>摘要 / Abstract</summary>

  With the large amount of data generated nowadays, analysis of this data has become eminent. Since a vast amount of this data is private, it is also important that the analysis is done in a secure manner. Comparison-based functions are commonly used in data analysis. These functions use the comparison operation as the basis. Secure computation of such functions have been discussed for median by Aggarwal et al. (EUROCRYPT&#x27;04) and for convex hull by Shelat and Venkitasubramaniam (ASIACRYPT&#x27;15). In this paper, we present a generic protocol for the secure computation of comparison-based functions. In order to scale to a large number of participants, we propose this protocol in a star topology with an aim to reduce the communication complexity. We also present a protocol for one specific comparison-based function, the $k^{th}$ ranked element. The construction of one of our protocols leaks some intermediate values but does not reveal information about an individual party&#x27;s inputs. We demonstrate that our protocol offers better performance than the protocol for $k^{th}$ ranked element by Tueno et. al. (FC&#x27;20) by providing an implementation.

  匹配依据：MPC: secure computation

  </details>

- **Impala: Low-Latency, Communication-Efficient Private Deep Learning Inference**
  2022-05-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.06437)
  Woo-Seok Choi, Brandon Reagen, Gu-Yeon Wei, David Brooks

  <details><summary>摘要 / Abstract</summary>

  This paper proposes Impala, a new cryptographic protocol for private inference in the client-cloud setting. Impala builds upon recent solutions that combine the complementary strengths of homomorphic encryption (HE) and secure multi-party computation (MPC). A series of protocol optimizations are developed to reduce both communication and performance bottlenecks. First, we remove MPC&#x27;s overwhelmingly high communication cost from the client by introducing a proxy server and developing a low-overhead key switching technique. Key switching reduces the clients bandwidth by multiple orders of magnitude, however the communication between the proxy and cloud is still excessive. Second, to we develop an optimized garbled circuit that leverages truncated secret shares for faster evaluation and less proxy-cloud communication. Finally, we propose sparse HE convolution to reduce the computational bottleneck of using HE. Compared to the state-of-the-art, these optimizations provide a bandwidth savings of over 3X and speedup of 4X for private deep learning inference.

  匹配依据：MPC: garbled circuit, secure multi party computation

  </details>

- **A class of few-Lee weight $\\mathbb{Z}\_2\[u\]$-linear codes using simplicial complexes and minimal codes via Gray map**
  2022-05-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.06470)
  Pramod Kumar Kewat, Nilay Kumar Mondal

  <details><summary>摘要 / Abstract</summary>

  Recently some mixed alphabet rings are involved in constructing few-Lee weight additive codes with optimal or minimal Gray images using suitable defining sets or down-sets. Inspired by these works, we choose the mixed alphabet ring $\mathbb{Z}_2\mathbb{Z}_2[u]$ to construct a special class of linear code $C_L$ over $\mathbb{Z}_2[u]$ with $u^2=0$ by employing simplicial complexes generated by a single maximal element. We show that $C_L$ has few-Lee weights by determining the Lee weight distribution of $C_L$. Theoretically, this shows that we may employ simplicial complexes to obatin few-weight codes even in the case of mixed alphabet rings. We show that the Gray image of $C_L$ is self-orthogonal and we have an infinite family of minimal codes over $\mathbb{Z}_2$ via Gray map, which can be used to secret sharing schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Circular semi-quantum secret sharing using single particles**
  2022-05-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.05558)
  Chong-Qiang Ye, Tian-Yu Ye

  <details><summary>摘要 / Abstract</summary>

  Semi-quantum secret sharing (SQSS) is an important branch of semi-quantum cryptography, and differs from quantum secret sharing (QSS) in that not all parties are required to possess quantum capabilities. All previous SQSS protocols have three common features: (1) they adopt product states or entangled states as initial quantum resource; (2) the particles prepared by quantum party are transmitted in a tree-type way; and (3) they require the classical parties to possess the measurement capability. In this paper, two circular SQSS protocols with single particles are suggested, where the first one requires the classical parties to possess the measurement capability while the second one does not have this requirement. Compared with the previous SQSS protocols, the proposed SQSS protocols have some distinct features: (1) they adopt single particles rather than product states or entangled states as initial quantum resource; (2) the particles prepared by quantum party are transmitted in a circular way; and (3) the second protocol releases the classical parties from the measurement capability. The proposed SQSS protocols are robust against some famous attacks from an eavesdropper, such as the measure-resend attack, the intercept-resend attack and the entangle-measure attack, and are feasible with present quantum technologies in reality.

  匹配依据：MPC: secret sharing

  </details>

- **Smart Contracts Obfuscation from Blockchain-based One-time Program**
  2022-05-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/549)
  Sora Suegami

  <details><summary>摘要 / Abstract</summary>

  We propose a cryptographic obfuscation scheme for smart contracts from one-time programs using a blockchain, a garbled circuit, and witness encryption. The proposed scheme protects not only the privacy of its input data and states but also the privacy of its algorithm and hardcoded secrets. Its security depends on existing secure blockchains and does not require the honest majority of secure multiparty computation and trusted hardware. This scheme is more efficient than obfuscating an entire program with indistinguishability obfuscation. In addition, it needs a trusted setup, but its security is protected unless all participants of the setup process are malicious.

  匹配依据：MPC: garbled circuit, secure multiparty computation

  </details>

- **Resumable Zero-Knowledge for Circuits from Symmetric Key Primitives**
  2022-05-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/556)
  Handong Zhang, Puwen Wei, Haiyang Xue, Yi Deng, Jinsong Li, Wei Wang, Guoxiao Liu

  <details><summary>摘要 / Abstract</summary>

  Consider the scenario that the prover and the verifier perform the zero-knowledge (ZK) proof protocol for the same statement multiple times sequentially, where each proof is modeled as a session. We focus on the problem of how to resume a ZK proof efficiently in such scenario. We introduce a new primitive called resumable honest verifier zero-knowledge proof of knowledge (resumable HVZKPoK) and propose a general construction of the resumable HVZKPoK for circuits based on the ``MPC-in-the-head&quot; paradigm, where the complexity of the resumed session is less than that of the original ZK proofs. To ensure the knowledge soundness for the resumed session, we identify a property called extractable decomposition. Interestingly, most block ciphers satisfy this property and the cost of resuming session can be reduced dramatically when the underlying circuits are implemented with block ciphers. As a direct application of our resumable HVZKPoK, we construct a post quantum secure stateful signature scheme, which makes Picnic3 suitable for blockchain protocol. Using the same parameter setting of Picnic3, the sign/verify time of our subsequent signatures can be reduced to 3.1%/3.3% of Picnic3 and the corresponding signature size can be reduced to 36%. Moreover, by applying a parallel version of our method to the well known Cramer, Damgaard and Schoenmakers (CDS) transformation, we get a compressed one-out-of-$N$ proof for circuits, which can be further used to construct a ring signature from symmetric key primitives only. When the ring size is less than $2^4$, the size of our ring signature scheme is only about 1/3 of Katz et al.&#x27;s construction.

  匹配依据：MPC: mpc (context)

  </details>

- **Privadome: Protecting Citizen Privacy from Delivery Drones**
  2022-05-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.04961)
  Gokulnath Pillai, Eikansh Gupta, Ajith Suresh, Vinod Ganapathy, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  As e-commerce companies begin to consider using delivery drones for customer fulfillment, there are growing concerns around citizen privacy. Drones are equipped with cameras, and the video feed from these cameras is often required as part of routine navigation, be it for semi autonomous or fully-autonomous drones. Footage of ground-based citizens may be captured in this video feed, thereby leading to privacy concerns. This paper presents Privadome, a system that implements the vision of a virtual privacy dome centered around the citizen. Privadome is designed to be integrated with city-scale regulatory authorities that oversee delivery drone operations and realizes this vision through two components, PD-MPC and PD-ROS. PD-MPC allows citizens equipped with a mobile device to identify drones that have captured their footage. It uses secure two-party computation to achieve this goal without compromising the privacy of the citizen&#x27;s location. PD-ROS allows the citizen to communicate with such drones and obtain an audit trail showing how the drone uses their footage and determine if privacy-preserving steps are taken to sanitize the footage. An experimental evaluation of Privadome using our prototype implementations of PD-MPC and PD-ROS shows that the system scales to near-term city-scale delivery drone deployments (hundreds of drones). We show that with PD-MPC the mobile data usage on the citizen&#x27;s mobile device is comparable to that of routine activities on the device, such as streaming videos. We also show that the workflow of PD-ROS consumes a modest amount of additional CPU resources and power on our experimental platform.

  匹配依据：MPC: secure two party computation

  </details>

- **Power Contracts: Provably Complete Power Leakage Models for Processors**
  2022-05-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/565)
  Roderick Bloem, Barbara Gigerl, Marc Gourjon, Vedad Hadžić, Stefan Mangard, Robert Primas

  <details><summary>摘要 / Abstract</summary>

  The protection of cryptographic software implementations against power-analysis attacks is critical for applications in embedded systems. A commonly used algorithmic countermeasure against these attacks is masking, a secret-sharing scheme that splits a sensitive computation into computations on multiple random shares. In practice, the security of masking schemes relies on several assumptions that are often violated by microarchitectural side-effects of CPUs. Many past works address this problem by studying these leakage effects and building corresponding leakage models that can then be integrated into a software verification workflow. However, these models have only been derived empirically, putting in question the otherwise rigorous security statements made with verification. We solve this problem in two steps. First, we introduce a contract layer between the (CPU) hardware and the software that allows the specification of microarchitectural side-effects on masked software in an intuitive language. Second, we present a method for proving the correspondence between contracts and CPU netlists to ensure the completeness of the specified leakage models. Then, any further security proofs only need to happen between software and contract, which brings benefits such as reduced verification runtime, improved user experience, and the possibility of working with vendor-supplied contracts of CPUs whose design is not available on netlist-level due to IP restrictions. We apply our approach to the popular RISC-V IBEX core, provide a corresponding formally verified contract, and describe how this contract could be used to verify masked software implementations.

  匹配依据：MPC: secret sharing

  </details>

- **FAPRIL: Towards Faster Privacy-Preserving Fingerprint-Based Localization**
  2022-05-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/564)
  Christopher van der Beets, Raine Nieminen, Thomas Schneider

  <details><summary>摘要 / Abstract</summary>

  Fingerprinting is a commonly used technique to provide accurate localization for indoor areas, where global navigation satellite systems, such as GPS and Galileo, cannot function or are not precise enough. Although fingerprint-based indoor localization has gained wide popularity, existing solutions that preserve privacy either rely on non-colluding servers or have high communication which hinder deployment. In this work we present FAPRIL, a privacy-preserving indoor localization scheme, which takes advantage of the latest secure two-party computation protocol improvements. We can split our scheme into two parts: an input independent setup phase and an online phase. We concentrate on optimizing the online phase for mobile clients who run on a mobile data plan and observe that recurring operands allow to optimize the total communication overhead even further. Our observation can be generalized, e.g., to improve multiplication of Arithmetic secret shared matrices. We implement FAPRIL on mobile devices and our benchmarks over a simulated LTE network show that the online phase of a private localization takes under 0.15 seconds with less than 0.20 megabytes of communication even for large buildings. The setup phase, which can be pre-computed, depends heavily on the setting but stays in the range 0.28 - 4.14 seconds and 0.69 - 16.00 megabytes per localization query. The round complexity of FAPRIL is constant for both phases.

  匹配依据：MPC: secure two party computation

  </details>

- **Automorphism Shuffles for Graphs and Hypergraphs and Its Applications**
  2022-05-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.04774)
  Kazumasa Shinagawa, Kengo Miyamoto

  <details><summary>摘要 / Abstract</summary>

  In card-based cryptography, a deck of physical cards is used to achieve secure computation. A shuffle, which randomly permutes a card-sequence along with some probability distribution, ensures the security of a card-based protocol. The authors proposed a new class of shuffles called graph shuffles, which randomly permutes a card-sequence by an automorphism of a directed graph (New Generation Computing 2022). For a directed graph $G$ with $n$ vertices and $m$ edges, such a shuffle could be implemented with pile-scramble shuffles with $2(n+m)$ cards. In this paper, we study graph shuffles and give an implementation, an application, and a slight generalization of them. First, we propose a new protocol for graph shuffles with $2n+m$ cards. Second, as a new application of graph shuffles, we show that any cyclic group shuffle, which is a shuffle over a cyclic group, is a graph shuffle associated with some graph. Third, we define a hypergraph shuffle, which is a shuffle by an automorphism of a hypergraph, and show that any hypergraph shuffle can also be implemented with pile-scramble shuffles.

  匹配依据：MPC: secure computation

  </details>

- **Fusion: Efficient and Secure Inference Resilient to Malicious Servers**
  2022-05-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.03040)
  Caiqin Dong, Jian Weng, Jia-Nan Liu, Yue Zhang, Yao Tong, Anjia Yang, Yudan Cheng, Shun Hu

  <details><summary>摘要 / Abstract</summary>

  In secure machine learning inference, most of the schemes assume that the server is semi-honest (honestly following the protocol but attempting to infer additional information). However, the server may be malicious (e.g., using a low-quality model or deviating from the protocol) in the real world. Although a few studies have considered a malicious server that deviates from the protocol, they ignore the verification of model accuracy (where the malicious server uses a low-quality model) meanwhile preserving the privacy of both the server&#x27;s model and the client&#x27;s inputs. To address these issues, we propose \textit{Fusion}, where the client mixes the public samples (which have known query results) with their own samples to be queried as the inputs of multi-party computation to jointly perform the secure inference. Since a server that uses a low-quality model or deviates from the protocol can only produce results that can be easily identified by the client, \textit{Fusion} forces the server to behave honestly, thereby addressing all those aforementioned issues without leveraging expensive cryptographic techniques. Our evaluation indicates that \textit{Fusion} is 48.06$\times$ faster and uses 30.90$\times$ less communication than the existing maliciously secure inference protocol (which currently does not support the verification of the model accuracy). In addition, to show the scalability, we conduct ImageNet-scale inference on the practical ResNet50 model and it costs 8.678 minutes and 10.117 GiB of communication in a WAN setting, which is 1.18$\times$ faster and has 2.64$\times$ less communication than those of the semi-honest protocol.

  匹配依据：MPC: multi party computation

  </details>

- **A Verifiable Multiparty Computation Solver for the Assignment Problem and Applications to Air Traffic Management**
  2022-05-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.03048)
  Thomas Loruenser, Florian Wohner, Stephan Krenn

  <details><summary>摘要 / Abstract</summary>

  The assignment problem is an essential problem in many application fields and frequently used to optimize resource usage. The problem is well understood and various efficient algorithms exist to solve the problem. However, it was unclear what practical performance could be achieved for privacy preserving implementations based on multiparty computation (MPC) by leveraging more efficient solution strategies than MPC based simplex solvers for linear programs. We solve this question by implementing and comparing different optimized MPC algorithms to solve the assignment problem for reasonable problem sizes. Our empirical approach revealed various insights to MPC based optimization and we measured a significant (50x) speedup compared to the known simplex based approach. Furthermore, we also study the overhead introduced by making the results publicly verifiable by means of non-interactive zero-knowledge proofs. By leveraging modern proof systems we also achieve significant speedup for proof and verification times compared to the previously proposed approaches as well as compact proof sizes.

  匹配依据：MPC: multiparty computation

  </details>

- **On The Distributed Discrete Logarithm Problem with Preprocessing**
  2022-05-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/521)
  Pavel Hubáček, Ľubica Jančová, Veronika Králová

  <details><summary>摘要 / Abstract</summary>

  Protocols solving the Distributed Discrete Logarithm (DDLog) problem are a core component of many recent constructions of group-based homomorphic secret sharing schemes. On a high-level, these protocols enable two parties to transform multiplicative shares of a secret into additive share locally without any communication. Due to their important applications, various generic optimized DDLog protocols were proposed in the literature, culminating in the asymptotically optimal generic protocol of Dinur, Keller, and Klein (J. Cryptol. 2020) solving DDLog in time $T$ with error probability $O(W/T^2)$ when the magnitude of the secret is bounded by $W$. Given that DDLog is solved repeatedly with respect to a fixed group in its applications, a natural approach for improving the efficiency of DDLog protocols could be via leveraging some precomputed group-specific advice. To understand the limitations of this approach, we revisit the distributed discrete logarithm problem in the preprocessing model and study the possible time-space trade-offs for DDLog in the generic group model. As our main result, we show that, in a group of size $N$, any generic DDLog protocol for secrets of magnitude $W$ with parties running in time $T$ using precomputed group-specific advice of size $S$ has success probability \[ \epsilon = O\left(\dfrac{T^2}{W} + \dfrac{\max\{S,\log W\} \cdot T^2}{N}\right). \] Thus, assuming $N \geq W \log W$, we get a lower bound $ST^2= \Omega(\epsilon N)$ on the time-space trade-off for DDLog protocols using large advice of size $S= \Omega(N/W)$. Interestingly, for DDLog protocols using \emph{small advice} of size $S=O(N/W)$, we get a lower bound $T^2=\Omega(\epsilon W)$ on the running time, which, in the constant-error regime, asymptotically matches the running time of the DDLog protocol \emph{without any advice} of Dinur et al. (J. Cryptol. 2020). In other words, we show that generic DDLog protocols achieving constant success probability do not benefit from any advice of size $S= O(N/W)$ in the online phase of the DDLog problem.

  匹配依据：MPC: secret sharing

  </details>

- **Distributed Symmetric Key Establishment: A scalable, quantum-proof key distribution system**
  2022-05-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2205.00615)
  Hoi-Kwong Lo, Mattia Montagna, Manfred von Willich

  <details><summary>摘要 / Abstract</summary>

  We propose and implement a protocol for a scalable, cost-effective, information-theoretically secure key distribution and management system. The system, called Distributed Symmetric Key Establishment (DSKE), relies on pre-shared random numbers between DSKE clients and a group of Security Hubs. Any group of DSKE clients can use the DSKE protocol to distill from the pre-shared numbers a secret key. The clients are protected from Security Hub compromise via a secret sharing scheme that allows the creation of the final key without the need to trust individual Security Hubs. Precisely, if the number of compromised Security Hubs does not exceed a certain threshold, confidentiality is guaranteed to DSKE clients and, at the same time, robustness against denial-of-service (DoS) attacks. The DSKE system can be used for quantum-secure communication, can be easily integrated into existing network infrastructures, and can support arbitrary groups of communication parties that have access to a key. We discuss the high-level protocol, analyze its security, including its robustness against disruption. A proof-of-principle demonstration of secure communication between two distant clients with a DSKE-based VPN using Security Hubs on Amazon Web Server (AWS) nodes thousands of kilometres away from them was performed, demonstrating the feasibility of DSKE-enabled secret sharing one-time-pad encryption with a data rate above 50 Mbit/s and a latency below 70 ms.

  匹配依据：MPC: secret sharing

  </details>

- **Quantum Universally Composable Oblivious Linear Evaluation**
  2022-04-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.14171)
  Manuel B. Santos, Paulo Mateus, Chrysoula Vlachou

  <details><summary>摘要 / Abstract</summary>

  Oblivious linear evaluation is a generalization of oblivious transfer, whereby two distrustful parties obliviously compute a linear function, f (x) = ax + b, i.e., each one provides their inputs that remain unknown to the other, in order to compute the output f (x) that only one of them receives. From both a structural and a security point of view, oblivious linear evaluation is fundamental for arithmetic-based secure multi-party computation protocols. In the classical case, oblivious linear evaluation protocols can be generated using oblivious transfer, and their quantum counterparts can, in principle, be constructed as straightforward extensions using quantum oblivious transfer. Here, we present the first, to the best of our knowledge, quantum protocol for oblivious linear evaluation that, furthermore, does not rely on quantum oblivious transfer. We start by presenting a semi-honest protocol, and then extend it to the dishonest setting employing a commit-and-open strategy. Our protocol uses high-dimensional quantum states to obliviously compute f (x) on Galois Fields of prime and prime-power dimension. These constructions utilize the existence of a complete set of mutually unbiased bases in prime-power dimension Hilbert spaces and their linear behaviour upon the Heisenberg-Weyl operators. We also generalize our protocol to achieve vector oblivious linear evaluation, where several instances of oblivious linear evaluation are generated, thus making the protocol more efficient. We prove the protocols to have static security in the framework of quantum universal composability.

  匹配依据：MPC: oblivious transfer, secure multi party computation

  </details>

- **Design and analysis of a distributed ECDSA signing service**
  2022-04-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/506)
  Jens Groth, Victor Shoup

  <details><summary>摘要 / Abstract</summary>

  We present and analyze a new protocol that provides a distributed ECDSA signing service, with the following properties: * it works in an asynchronous communication model; * it works with $n$ parties with up to $f &lt; n/3$ Byzantine corruptions; * it provides guaranteed output delivery; * it provides a very efficient, non-interactive online signing phase; * it supports additive key derivation according to the BIP32 standard. While there has been a flurry of recent research on distributed ECDSA signing protocols, none of these newly designed protocols provides guaranteed output delivery over an asynchronous communication network; moreover, the performance of our protocol (in terms of asymptotic communication and computational complexity) meets or beats the performance of any of these other protocols. This service is being implemented and integrated into the architecture of the Internet Computer, enabling smart contracts running on the Internet Computer to securely hold and spend Bitcoin and other cryptocurrencies. Along the way, we present some results of independent interest: * a new asynchronous verifiable secret sharing (AVSS) scheme that is simple and efficient; * a new scheme for multi-recipient encryption that is simple and efficient.

  匹配依据：MPC: secret sharing

  </details>

- **Cryptographic Oracle-Based Conditional Payments**
  2022-04-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/499)
  Varun Madathil, Sri AravindaKrishnan Thyagarajan, Dimitrios Vasilopoulos, Lloyd Fournier, Giulio Malavolta, Pedro Moreno-Sanchez

  <details><summary>摘要 / Abstract</summary>

  We consider a scenario where two mutually distrustful parties, Alice and Bob, want to perform a payment conditioned on the outcome of some real-world event. A semi-trusted oracle (or a threshold number of oracles, in a distributed trust setting) is entrusted to attest that such an outcome indeed occurred, and only then the payment is successfully made. Such oracle-based conditional (ObC) payments are ubiquitous in many real-world applications, like financial adjudication, pre-scheduled payments or trading, and are a necessary building block to introduce information about real-world events into blockchains. In this work we show how to realize ObC payments with provable security guarantees and efficient instantiations. To do this, we propose a new cryptographic primitive that we call verifiable witness encryption based on threshold signatures (VweTS): Users can encrypt signatures on payments that can be decrypted if a threshold number of signers (e.g., oracles) sign another message (e.g., the description of an event outcome). We require two security notions: (1) one-wayness that guarantees that without the threshold number of signatures, the ciphertext hides the encrypted signature, and (2) verifiability, that guarantees that a ciphertext that correctly verifies can be successfully decrypted to reveal the underlying signature. We present provably secure and efficient instantiations of VweTS where the encrypted signature can be some of the widely used schemes like Schnorr, ECDSA or BLS signatures. Our main technical innovation is a new batching technique for cut-and-choose, inspired by the work of Lindell-Riva on garbled circuits. Our VweTS instantiations can be readily used to realize ObC payments on virtually all cryptocurrencies of today in a fungible, cost-efficient, and scalable manner. The resulting ObC payments are the first to support distributed trust (i.e., multiple oracles) without requiring any form of synchrony or coordination among the users and the oracles. To demonstrate the practicality of our scheme, we present a prototype implementation and our benchmarks in commodity hardware show that the computation overhead is less than 25 seconds even for a threshold of 4-of-7 and a payment conditioned on 1024 different real-world event outcomes, while the communication overhead is below 2.3 MB

  匹配依据：MPC: garbled circuits

  </details>

- **A symmetric extensible protocol for quantum secret sharing**
  2022-04-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.13397)
  Michael Ampatzis, Theodore Andronikos

  <details><summary>摘要 / Abstract</summary>

  This paper introduces the Symmetric Extensible Quantum Secret Sharing protocol, which is a novel quantum protocol for secret sharing. At its heart, it is an entanglement based protocol that relies on the use of maximally entangled GHZ tuples, evenly distributed among the players, endowing the spymaster with the ability to securely share a secret message with her agents. It offers uncompromising security, making virtually impossible for a malicious eavesdropper or a rogue double agent to disrupt its successful execution. It is characterized by symmetry, since all agents are treated indiscriminately, utilizing identical quantum circuits. Furthermore, it can be seamlessly extended to an arbitrary number of agents. After the completion of the quantum part of the protocol, the spymaster will have to publicly transmit some information, in order to enable the agents to discover the secret message. Finally, it has the additional advantage that the spymaster has the privilege to decide when it is the right time for the agents to discover the secret message.

  匹配依据：MPC: secret sharing

  </details>

- **Hardware Acceleration for Third-Generation FHE and PSI Based on It**
  2022-04-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.11334)
  Zhehong Wang, Dennis Sylvester, Hun-Seok Kim, David Blaauw

  <details><summary>摘要 / Abstract</summary>

  With the expansion of cloud services, serious concerns about the privacy of users&#x27; data arise due to the exposure of the unencrypted data to the server during computation. Various security primitives are under investigation to preserve privacy while evaluating private data, including Fully Homomorphic Encryption (FHE), Private Set Intersection (PSI), and others. However, the prohibitive processing time of these primitives hinders their practical applications. This work proposes and implements an architecture for accelerating third-generation FHE with Amazon Web Services (AWS) cloud FPGAs, marking the first hardware acceleration solution for third-generation FHE. We also introduce a novel unbalanced PSI protocol based on third-generation FHE, optimized for the proposed hardware architecture. Several algorithm-architecture co-optimization techniques are introduced to allow the communication and computation costs to be independent of the Sender&#x27;s set size. The measurement results show that the proposed accelerator achieves $&gt;21\times$ performance improvement compared to a software implementation for various crucial subroutines of third-generation FHE and the proposed PSI.

  匹配依据：MPC: private set intersection

  </details>

- **Multi-Party Computation in the GDPR**
  2022-04-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/491)
  Lukas Helminger, Christian Rechberger

  <details><summary>摘要 / Abstract</summary>

  The EU GDPR has two main goals: Protecting individuals from personal data abuse and simplifying the free movement of personal data. Privacy-enhancing technologies promise to fulfill both goals simultaneously. A particularly effective and versatile technology solution is multi-party computation (MPC). It allows protecting data during a computation involving multiple parties. This paper aims for a better understanding of the role of MPC in the GDPR. Although MPC is relatively mature, little research was dedicated to its GDPR compliance. First, we try to give an understanding of MPC for legal scholars and policymakers. Then, we examine the GDPR relevant provisions regarding MPC with a technical audience in mind. Finally, we devise a test that can assess the impact of a given MPC solution with regard to the GDPR. The test consists of several questions, which a controller can answer without the help of a technical or legal expert. Going through the questions will classify the MPC solution as (1) a means of avoiding the GDPR, (2) Data Protection by Design, or (3) having no legal benefits. Two concrete case studies should provide a blueprint on how to apply the test. We hope that this work also contributes to an interdisciplinary discussion of MPC certification and standardization.

  匹配依据：MPC: multi party computation

  </details>

- **Towards Privacy-Preserving Neural Architecture Search**
  2022-04-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.10958)
  Fuyi Wang, Leo Yu Zhang, Lei Pan, Shengshan Hu, Robin Doss

  <details><summary>摘要 / Abstract</summary>

  Machine learning promotes the continuous development of signal processing in various fields, including network traffic monitoring, EEG classification, face identification, and many more. However, massive user data collected for training deep learning models raises privacy concerns and increases the difficulty of manually adjusting the network structure. To address these issues, we propose a privacy-preserving neural architecture search (PP-NAS) framework based on secure multi-party computation to protect users&#x27; data and the model&#x27;s parameters/hyper-parameters. PP-NAS outsources the NAS task to two non-colluding cloud servers for making full advantage of mixed protocols design. Complement to the existing PP machine learning frameworks, we redesign the secure ReLU and Max-pooling garbled circuits for significantly better efficiency ($3 \sim 436$ times speed-up). We develop a new alternative to approximate the Softmax function over secret shares, which bypasses the limitation of approximating exponential operations in Softmax while improving accuracy. Extensive analyses and experiments demonstrate PP-NAS&#x27;s superiority in security, efficiency, and accuracy.

  匹配依据：MPC: garbled circuits, secure multi party computation

  </details>

- **Information Leakage in Code-based Masking: A Systematic Evaluation by Higher-Order Attacks**
  2022-04-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/461)
  Wei Cheng, Sylvain Guilley, Jean-Luc Danger

  <details><summary>摘要 / Abstract</summary>

  Code-based masking is a recent line of research on masking schemes aiming at provably counteracting side-channel attacks. It generalizes and unifies many masking schemes within a coding-theoretic formalization. In code-based masking schemes, the tuning parameters are the underlying linear codes, whose choice significantly affects the side-channel resilience. In this paper, we investigate the exploitability of the information leakage in code-based masking and present attack-based evaluation results of higher-order optimal distinguisher (HOOD). Particularly, we consider two representative instances of code-based masking, namely inner product masking (IPM) and Shamir&#x27;s secret sharing (SSS) based masking. Our results do confirm the state-of-the-art theoretical derivatives in an empirical manner with numerically simulated measurements. Specifically, theoretical results are based on quantifying information leakage; we further complete the panorama with attack-based evaluations by investigating the exploitability of the leakage. Moreover, we classify all possible candidates of linear codes in IPM with 2 and 3 shares and (3,1)-SSS based masking, and highlight both optimal and worst codes for them. Relying on our empirical evaluations, we therefore recommend investigating the coding-theoretic properties to find the best linear codes in strengthening instances of code-based masking. As for applications, our attack-based evaluation directly empowers designers, by employing optimal linear codes, to enhance the protection of code-based masking. Our framework leverages simulated leakage traces, hence allowing for source code validation or patching in case it is found to be attackable.

  匹配依据：MPC: secret sharing

  </details>

- **Breaking Masked Implementations of the Clyde-Cipher by Means of Side-Channel Analysis - A Report on the CHES Challenge Side-Channel Contest 2020**
  2022-04-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/471)
  Aron Gohr, Friederike Laus, Werner Schindler

  <details><summary>摘要 / Abstract</summary>

  In this paper we present our solution to the CHES Challenge 2020, the task of which it was to break masked hardware respective software implementations of the lightweight cipher Clyde by means of side-channel analysis. We target the secret cipher state after processing of the first $S$-box layer. Using the provided trace data we obtain a strongly biased posterior distribution for the secret-shared cipher state at the targeted point; this enables us to see exploitable biases even before the secret sharing based masking. These biases on the unshared state can be evaluated one $S$-box at a time and combined across traces, which enables us to recover likely key hypotheses $S$-box by $S$-box. In order to see the shared cipher state, we employ a deep neural network similar to the one used by Gohr, Jacob and Schindler to solve the CHES 2018 AES challenge. We modify their architecture to predict the exact bit sequence of the secret-shared cipher state. We find that convergence of training on this task is unsatisfying with the standard encoding of the shared cipher state and therefore introduce a different encoding of the prediction target, which we call the scattershot encoding. In order to further investigate how exactly the scattershot encoding helps to solve the task at hand, we construct a simple synthetic task where convergence problems very similar to those we observed in our side-channel task appear with the naive target data encoding but disappear with the scattershot encoding. We complete our analysis by showing results that we obtained with a classical method (as opposed to an AI-based method), namely the stochastic approach, that we generalize for this purpose first to the setting of shared keys. We show that the neural network draws on a much broader set of features, which may partially explain why the neural-network based approach massively outperforms the stochastic approach. On the other hand, the stochastic approach provides insights into properties of the implementation, in particular the observation that the $S$-boxes behave very different regarding the easiness respective hardness of their prediction.

  匹配依据：MPC: secret sharing

  </details>

- **SPIKE: Secure and Private Investigation of the Kidney Exchange problem**
  2022-04-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.09937)
  Timm Birka, Kay Hamacher, Tobias Kussel, Helen Möllering, Thomas Schneider

  <details><summary>摘要 / Abstract</summary>

  Background: The kidney exchange problem (KEP) addresses the matching of patients in need for a replacement organ with compatible living donors. Ideally many medical institutions should participate in a matching program to increase the chance for successful matches. However, to fulfill legal requirements current systems use complicated policy-based data protection mechanisms that effectively exclude smaller medical facilities to participate. Employing secure multi-party computation (MPC) techniques provides a technical way to satisfy data protection requirements for highly sensitive personal health information while simultaneously reducing the regulatory burdens. Results: We have designed, implemented, and benchmarked SPIKE, a secure MPC-based privacy-preserving KEP which computes a solution by finding matching donor-recipient pairs in a graph structure. SPIKE matches 40 pairs in cycles of length 2 in less than 4 minutes and outperforms the previous state-of-the-art protocol by a factor of 400x in runtime while providing medically more robust solutions. Conclusions: We show how to solve the KEP in a robust and privacy-preserving manner achieving practical performance. The usage of MPC techniques fulfills many data protection requirements on a technical level, allowing smaller health care providers to directly participate in a kidney exchange with reduced legal processes.

  匹配依据：MPC: secure multi party computation

  </details>

- **HMT: A Hardware-Centric Hybrid Bonsai Merkle Tree Algorithm for High-Performance Authentication**
  2022-04-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.08976)
  Rakin Muhammad Shadab, Yu Zou, Sanjay Gandham, Amro Awad, Mingjie Lin

  <details><summary>摘要 / Abstract</summary>

  Merkle tree is a widely used tree structure for authentication of data/metadata in a secure computing system. Recent state-of-the art secure systems use a smaller-sized MT, namely Bonsai Merkle Tree (BMT) to protect the metadata such as encryption counters. Common BMT algorithms were designed for traditional Von Neumann architectures with a software-centric implementation in mind, hence they use a lot of recursions and are often sequential in nature. However, the modern heterogeneous computing platforms employing Field-Programmable Gate Array (FPGA) devices require concurrency-focused algorithms to fully utilize the versatility and parallel nature of such systems. Our goal for this work is to introduce HMT, a hardware-friendly BMT algorithm that enables the verification and update processes to function independently and provides the benefits of relaxed update while being comparable to eager update in terms of update complexity. The methodology of HMT contributes both novel algorithm revisions and innovative hardware techniques to implementing BMT. We introduce a hybrid BMT algorithm that is hardware-targeted, parallel and relaxes the update depending on BMT cache hit but makes the update conditions more flexible compared to lazy update to save additional write-backs. Deploying this new algorithm, we have designed a new BMT controller with a dataflow architecture, speculative buffers and parallel write-back engines that allows for multiple concurrent relaxed authentication. Our empirical performance measurements have demonstrated that HMT can achieve up to 7x improvement in bandwidth and 4.5x reduction in latency over baseline in subsystem level tests. In a real secure-memory system on a Xilinx U200 accelerator FPGA, HMT exhibits up to 14\% faster execution in standard benchmarks compared to state-of-the art BMT solution on FPGA.

  匹配依据：MPC: secure computing

  </details>

- **Homomorphic Encryption and Federated Learning based Privacy-Preserving CNN Training: COVID-19 Detection Use-Case**
  2022-04-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.07752)
  Febrianti Wibawa, Ferhat Ozgur Catak, Salih Sarp, Murat Kuzlu, Umit Cali

  <details><summary>摘要 / Abstract</summary>

  Medical data is often highly sensitive in terms of data privacy and security concerns. Federated learning, one type of machine learning techniques, has been started to use for the improvement of the privacy and security of medical data. In the federated learning, the training data is distributed across multiple machines, and the learning process is performed in a collaborative manner. There are several privacy attacks on deep learning (DL) models to get the sensitive information by attackers. Therefore, the DL model itself should be protected from the adversarial attack, especially for applications using medical data. One of the solutions for this problem is homomorphic encryption-based model protection from the adversary collaborator. This paper proposes a privacy-preserving federated learning algorithm for medical data using homomorphic encryption. The proposed algorithm uses a secure multi-party computation protocol to protect the deep learning model from the adversaries. In this study, the proposed algorithm using a real-world medical dataset is evaluated in terms of the model performance.

  匹配依据：MPC: secure multi party computation

  </details>

- **UTT: Decentralized Ecash with Accountable Privacy**
  2022-04-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/452)
  Alin Tomescu, Adithya Bhat, Benny Applebaum, Ittai Abraham, Guy Gueta, Benny Pinkas, Avishay Yanai

  <details><summary>摘要 / Abstract</summary>

  We present UnTraceable Transactions (UTT), a system for decentralized ecash with accountable privacy. UTT is the first ecash system that obtains three critical properties: (1) it provides decentralized trust by implementing the ledger, bank, auditor, and registration authorities via threshold cryptography and Byzantine Fault Tolerant infrastructure; (2) it balances accountability and privacy by implementing anonymity budgets: users can anonymously send payments, but only up to a limited amount of currency per month. Past this point, transactions can either be made public or subjected to customizable auditing rules; (3) by carefully choosing cryptographic building blocks and co-designing the cryptography and decentralization, UTT is tailored for high throughput and low latency. With a combination of optimized cryptographic building blocks and vertical scaling (optimistic concurrency control), UTT can provide almost 1,000 payments with accountable privacy per second, with latencies of around 100 milliseconds and less. Through horizontal scaling (multiple shards), UTT can scale to tens of thousands of such transactions per second. With 60 shards we measure over 10,000 transactions with accountable privacy per second. We formally define and prove the security of UTT using an MPC-style ideal functionality. Along the way, we define a new MPC framework that captures the security of reactive functionalities in a stand-alone setting, thus filling an important gap in the MPC literature. Our new framework is compatible with practical instantiations of cryptographic primitives and provides a trade-off between concrete efficiency and provable security that may be also useful for future work.

  匹配依据：MPC: mpc (context)

  </details>

- **Improved Stock Market Structure Using Cryptography**
  2022-04-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/451)
  Charanjit S. Jutla, Barry Mishra

  <details><summary>摘要 / Abstract</summary>

  The stock market has two primary functions, that of providing liquidity and price discovery. While historically, the market micro-structure was mostly ignored or assumed to function ideally for the purpose of asset pricing, O’Hara (Journal of Finance, 2003) established that both liquidity and price discovery affect asset pricing, and consequently asset returns. In this work, we extend the analysis of Easley and O’Hara (Journal of finance, 2004) to study common stock market mechanisms, including open-bid and sealed-bid auctions, as well as the fact that the auctioneer may not be trustworthy. Our analysis shows that open-bid auctions dis-incentivize stock research, leading to higher volatility. On the other hand, we also show that in sealed-bid auctions, the price and volume of an auction reveals only partial private research information, thus retaining incentive for traders to do research. We also show how secure computation can be used to build auctions with a distributed auctioneer, where the clearing and partial-fulfillment information of the auction does not reveal unfilled orders of others, thus maintaining private information

  匹配依据：MPC: secure computation

  </details>

- **Efficient Compiler to Covert Security with Public Verifiability for Honest Majority MPC**
  2022-04-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/454)
  Thomas Attema, Vincent Dunning, Maarten Everts, Peter Langenkamp

  <details><summary>摘要 / Abstract</summary>

  We present a novel compiler for transforming arbitrary, passively secure MPC protocols into efficient protocols with covert security and public verifiability in the honest majority setting. Our compiler works for protocols with any number of parties &gt; 2 and treats the passively secure protocol in a black-box manner. In multi-party computation (MPC), covert security provides an attractive trade-off between the security of actively secure protocols and the efficiency of passively secure protocols. In this security notion, honest parties are only required to detect an active attack with some constant probability, referred to as the deterrence rate. Extending covert security with public verifiability additionally ensures that any party, even an external one not participating in the protocol, is able to identify the cheaters if an active attack has been detected. Recently, Faust et al. (EUROCRYPT 2021) and Scholl et al. (Pre-print 2021) introduced similar covert security compilers based on computationally expensive time-lock puzzles. At the cost of requiring an honest majority, our work avoids the use of time-lock puzzles completely. Instead, we adopt a much more efficient publicly verifiable secret sharing scheme to achieve a similar functionality. This obviates the need for a trusted setup and a general-purpose actively secure MPC protocol. We show that our computation and communication costs are orders of magnitude lower while achieving the same deterrence rate.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **SoK: Privacy Preserving Machine Learning using Functional Encryption: Opportunities and Challenges**
  2022-04-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.05136)
  Prajwal Panzade, Daniel Takabi

  <details><summary>摘要 / Abstract</summary>

  With the advent of functional encryption, new possibilities for computation on encrypted data have arisen. Functional Encryption enables data owners to grant third-party access to perform specified computations without disclosing their inputs. It also provides computation results in plain, unlike Fully Homomorphic Encryption. The ubiquitousness of machine learning has led to the collection of massive private data in the cloud computing environment. This raises potential privacy issues and the need for more private and secure computing solutions. Numerous efforts have been made in privacy-preserving machine learning (PPML) to address security and privacy concerns. There are approaches based on fully homomorphic encryption (FHE), secure multiparty computation (SMC), and, more recently, functional encryption (FE). However, FE-based PPML is still in its infancy and has not yet gotten much attention compared to FHE-based PPML approaches. In this paper, we provide a systematization of PPML works based on FE summarizing state-of-the-art in the literature. We focus on Inner-product-FE and Quadratic-FE-based machine learning models for the PPML applications. We analyze the performance and usability of the available FE libraries and their applications to PPML. We also discuss potential directions for FE-based PPML approaches. To the best of our knowledge, this is the first work to systematize FE-based PPML approaches.

  匹配依据：MPC: secure computing, secure multiparty computation

  </details>

- **Distributed Hardware Accelerated Secure Joint Computation on the COPA Framework**
  2022-04-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.04816)
  Rushi Patel, Pouya Haghi, Shweta Jain, Andriy Kot, Venkata Krishnan, Mayank Varia, Martin Herbordt

  <details><summary>摘要 / Abstract</summary>

  Performance of distributed data center applications can be improved through use of FPGA-based SmartNICs, which provide additional functionality and enable higher bandwidth communication. Until lately, however, the lack of a simple approach for customizing SmartNICs to application requirements has limited the potential benefits. Intel&#x27;s Configurable Network Protocol Accelerator (COPA) provides a customizable FPGA framework that integrates both hardware and software development to improve computation and communication performance. In this first case study, we demonstrate the capabilities of the COPA framework with an application from cryptography -- secure Multi-Party Computation (MPC) -- that utilizes hardware accelerators connected directly to host memory and the COPA network. We find that using the COPA framework gives significant improvements to both computation and communication as compared to traditional implementations of MPC that use CPUs and NICs. A single MPC accelerator running on COPA enables more than 17Gbps of communication bandwidth while using only 1% of Stratix 10 resources. We show that utilizing the COPA framework enables multiple MPC accelerators running in parallel to fully saturate a 100Gbps link enabling higher performance compared to traditional NICs.

  匹配依据：MPC: secure multi party computation

  </details>

- **Network Shuffling: Privacy Amplification via Random Walks**
  2022-04-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.03919)
  Seng Pei Liew, Tsubasa Takahashi, Shun Takagi, Fumiyuki Kato, Yang Cao, Masatoshi Yoshikawa

  <details><summary>摘要 / Abstract</summary>

  Recently, it is shown that shuffling can amplify the central differential privacy guarantees of data randomized with local differential privacy. Within this setup, a centralized, trusted shuffler is responsible for shuffling by keeping the identities of data anonymous, which subsequently leads to stronger privacy guarantees for systems. However, introducing a centralized entity to the originally local privacy model loses some appeals of not having any centralized entity as in local differential privacy. Moreover, implementing a shuffler in a reliable way is not trivial due to known security issues and/or requirements of advanced hardware or secure computation technology. Motivated by these practical considerations, we rethink the shuffle model to relax the assumption of requiring a centralized, trusted shuffler. We introduce network shuffling, a decentralized mechanism where users exchange data in a random-walk fashion on a network/graph, as an alternative of achieving privacy amplification via anonymity. We analyze the threat model under such a setting, and propose distributed protocols of network shuffling that is straightforward to implement in practice. Furthermore, we show that the privacy amplification rate is similar to other privacy amplification techniques such as uniform shuffling. To our best knowledge, among the recently studied intermediate trust models that leverage privacy amplification techniques, our work is the first that is not relying on any centralized entity to achieve privacy amplification.

  匹配依据：MPC: secure computation

  </details>

- **Multiverse of HawkNess: A Universally-Composable MPC-based Hawk Variant**
  2022-04-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/421)
  Aritra Banerjee, Hitesh Tewari

  <details><summary>摘要 / Abstract</summary>

  The evolution of Smart contracts in recent years inspired a crucial question: Do smart contract evaluation protocols provide the required level of privacy when executing contracts on the Blockchain? The Hawk (IEEE S&amp;P &#x27;16) paper introduces a way to solve the problem of privacy in smart contracts by evaluating the contracts off-chain, albeit with the trust assumption of a manager. To avoid the partially trusted manager altogether, a novel approach named zkHawk (IEEE BRAINS &#x27;21) explains how we can evaluate the contracts privately off-chain using a multi-party computation (MPC) protocol instead of trusting said manager. This paper dives deeper into the detailed construction of a variant of the zkHawk protocol titled V-zkHawk using formal proofs to construct the said protocol and model its security in the universal composability (UC) framework (FOCS &#x27;01). The V-zkHawk protocol discussed here does not support immediate closure, i.e, all the parties ($n$) have to send a message to inform the blockchain that the contract has been executed with corruption allowed for up to $t$ parties, where $t&lt;n$. In the most quintessential sense, the V-zkHawk is a variant because the outcome of the protocol is similar (i.e., execution of smart contract via an MPC function evaluation) to zkHawk, but we modify key aspects of the protocol essentially creating a small trade-off (removing immediate closure) to provide UC (stronger) security. The V-zkHawk protocol leverages joint Schnorr signature schemes, encryption schemes, Non-Interactive Zero-Knowledge Proofs (NIZKs), and commitment schemes with Common Reference String (CRS) assumptions, MPC function evaluations, and assumes the existence of asynchronous, authenticated broadcast channels. We achieve malicious security in a dishonest majority setting in the UC framework.

  匹配依据：MPC: multi party computation

  </details>

- **Efficient, Actively Secure MPC with a Dishonest Majority: a Survey**
  2022-04-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/417)
  Emmanuela Orsini

  <details><summary>摘要 / Abstract</summary>

  The last ten years have seen a tremendous growth in the interest and practicality of secure multiparty computation (MPC) and its possible applications. Secure MPC is indeed a very hot research topic and recent advances in the eld have already been translated into commercial products world-wide. A major pillar in this advance has been in the case of active security with a dishonest majority, mainly due to the SPDZ-line of work protocols. This survey gives an overview of these protocols, with a focus of the original SPDZ paper (CRYPTO 2012) and its subsequent optimizations. It also covers some alternative approaches based on oblivious transfer, oblivious linear-function evaluation, and constant-round protocols.

  匹配依据：MPC: oblivious transfer, secure multiparty computation

  </details>

- **Constant Size Secret Sharing: with General Thresholds, Towards Standard Assumptions, and Applications**
  2022-04-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/427)
  Katarzyna Kapusta, Matthieu Rambaud, Ferdinand Sibleyras

  <details><summary>摘要 / Abstract</summary>

  We consider threshold Computational Secret Sharing Schemes, i.e., such that the secret can be recovered from any $t+1$ out of $n$ shares, and such that no computationally bounded adversary can distinguish between $t$ shares of a chosen secret and a uniform string. We say that such a scheme has Constant Size (CSSS) if, in the asymptotic regime of many shares of small size the security parameter, then the total size of shares reaches the minimum, which is the size of an erasures-correction encoding of the secret with same threshold. But all CSSS so far have only maximum threshold, i.e., $t=n-1$. They are known as All Or Nothing Transforms (AONT). On the other hand, for arbitrary thresholds $t&lt;n-1$, the shortest scheme known so far is [Kra93, Crypto], which has instead twice larger size in the previous regime, due to a size overhead of $n$ times the security parameter. The other limitation of known CSSS is that they require a number of calls to idealized primitives which grows linearly with the size of the secret. Our first contribution is to show that the CSSS of [Des00, Crypto], which holds under the ideal cipher assumption, looses its privacy when instantiated with a plain pseudorandom permutation. Our main contribution is a scheme which: is the first CSSS for any threshold $t$, and furthermore, whose security holds, for the first time, under any plain pseudorandom function, with the only idealized assumption being in the key-derivation function. It is based on the possibly new observation that the scheme of [Des00] can be seen as an additive secret-sharing of an encryption key, using the ciphertext itself as a source of randomness. A variation of our construction enables to improve upon known schemes, that we denote as Encryption into Shares with Resilience against Key exposure (ESKE), having the property that all ciphertext blocks are needed to obtain any information, even when the key is leaked. We obtain the first ESKE with arbitrary threshold $t$ and constant size, furthermore in one pass of encryption. Also, for the first time, the only idealized assumption is in the key-derivation. Then, we demonstrate how to establish fast revocable storage on an untrusted server, from any black box ESKE. Instantiated with our ESKE, then encryption and decryption both require only $1$ pass of symmetric primitives under standard assumptions (except the key-derivation), compared to at least $2$ consecutive passes in [MS18, CT-RSA] and more in [Bac+16, CCS]. We finally bridge the gap between two conflicting specifications of AONT in the literature: one very similar to CSSS, which has indistinguishability, and one which has not.

  匹配依据：MPC: secret sharing

  </details>

- **Compact Post-Quantum Signatures from Proofs of Knowledge leveraging Structure for the PKP, SD and RSD Problems**
  2022-04-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.02915)
  Loïc Bidoux, Philippe Gaborit

  <details><summary>摘要 / Abstract</summary>

  The MPC-in-the-head introduced in [IKOS07] has established itself as an important paradigm to design efficient digital signatures. It has been leveraged in the Picnic scheme [CDG+ 20] that reached the third round of the NIST PQC Standardization process. It has also been used in [Beu20] to introduce the Proof of Knowledge (PoK) with Helper paradigm. This construction permits to design shorter signatures but induces a non negligible performance overhead as it uses cut-and-choose. In this paper, we introduce the PoK leveraging structure paradigm along with its associated challenge space amplification technique. Our new approach to design PoK brings some improvements over the PoK with Helper one. Indeed, we show how one can substitute the Helper in these constructions by leveraging the underlying structure of the considered problem. This approach does not suffer from the performance overhead inherent to the PoK with Helper paradigm hence offers different trade-offs between security, signature sizes and performances. We also present four new post-quantum signature schemes. The first one is based on a new PoK with Helper for the Syndrome Decoding problem. It relies on ideas from [BGKM22] and [FJR21] and improve the latter using a new technique that can be seen as performing some cut-and-choose with a meet in the middle approach. The three other signatures are based on our new PoK leveraging structure approach and as such illustrate its versatility. We provide new PoK related to the Permuted Kernel Problem (PKP), Syndrome Decoding (SD) problem and Rank Syndrome Decoding (RSD) problem. In practice, these PoK lead to comparable or shorter signatures than existing ones. Indeed, considering (public key + signature), we get sizes below 9kB for our signature related to the PKP problem, below 15kB for our signature related to the SD problem and below 7kB for our signature related to the RSD problem.

  匹配依据：MPC: mpc (context)

  </details>

- **Efficient and Tight Oblivious Transfer from PKE with Tight Multi-User Security**
  2022-04-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/415)
  Saikrishna Badrinarayanan, Daniel Masny, Pratyay Mukherjee

  <details><summary>摘要 / Abstract</summary>

  We propose an efficient oblivious transfer in the random oracle model based on public key encryption with pseudorandom public keys. The construction is as efficient as the state of art though it has a significant advantage. It has a tight security reduction to the multi-user security of the underlying public key encryption. In previous constructions, the security reduction has a multiplicative loss that amounts in at least the amount of adversarial random oracle queries. When considering this loss for a secure parameter choice, the underlying public key encryption or elliptic curve would require a significantly higher security level which would decrease the overall efficiency. Our OT construction can be instantiated from a wide range of assumptions such as DDH, LWE, or codes based assumptions as well as many public key encryption schemes such as the NIST PQC finalists. Since tight multi-user security is a very natural requirement which many public key encryption schemes suffice, many public key encryption schemes can be straightforwardly plugged in our construction without the need of reevaluating or adapting any parameter choices.

  匹配依据：MPC: oblivious transfer

  </details>

- **Truth Serum: Poisoning Machine Learning Models to Reveal Their Secrets**
  2022-03-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.00032)
  Florian Tramèr, Reza Shokri, Ayrton San Joaquin, Hoang Le, Matthew Jagielski, Sanghyun Hong, Nicholas Carlini

  <details><summary>摘要 / Abstract</summary>

  We introduce a new class of attacks on machine learning models. We show that an adversary who can poison a training dataset can cause models trained on this dataset to leak significant private details of training points belonging to other parties. Our active inference attacks connect two independent lines of work targeting the integrity and privacy of machine learning training data. Our attacks are effective across membership inference, attribute inference, and data extraction. For example, our targeted attacks can poison &lt;0.1% of the training dataset to boost the performance of inference attacks by 1 to 2 orders of magnitude. Further, an adversary who controls a significant fraction of the training data (e.g., 50%) can launch untargeted attacks that enable 8x more precise inference on all other users&#x27; otherwise-private data points. Our results cast doubts on the relevance of cryptographic privacy guarantees in multiparty computation protocols for machine learning, if parties can arbitrarily select their share of training data.

  匹配依据：MPC: multiparty computation

  </details>

- **Efficient Dropout-resilient Aggregation for Privacy-preserving Machine Learning**
  2022-03-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.17044)
  Ziyao Liu, Jiale Guo, Kwok-Yan Lam, Jun Zhao

  <details><summary>摘要 / Abstract</summary>

  With the increasing adoption of data-hungry machine learning algorithms, personal data privacy has emerged as one of the key concerns that could hinder the success of digital transformation. As such, Privacy-Preserving Machine Learning (PPML) has received much attention from both academia and industry. However, organizations are faced with the dilemma that, on the one hand, they are encouraged to share data to enhance ML performance, but on the other hand, they could potentially be breaching the relevant data privacy regulations. Practical PPML typically allows multiple participants to individually train their ML models, which are then aggregated to construct a global model in a privacy-preserving manner, e.g., based on multi-party computation or homomorphic encryption. Nevertheless, in most important applications of large-scale PPML, e.g., by aggregating clients&#x27; gradients to update a global model for federated learning, such as consumer behavior modeling of mobile application services, some participants are inevitably resource-constrained mobile devices, which may drop out of the PPML system due to their mobility nature. Therefore, the resilience of privacy-preserving aggregation has become an important problem to be tackled. In this paper, we propose a scalable privacy-preserving aggregation scheme that can tolerate dropout by participants at any time, and is secure against both semi-honest and active malicious adversaries by setting proper system parameters. By replacing communication-intensive building blocks with a seed homomorphic pseudo-random generator, and relying on the additive homomorphic property of Shamir secret sharing scheme, our scheme outperforms state-of-the-art schemes by up to 6.37$\times$ in runtime and provides a stronger dropout-resilience. The simplicity of our scheme makes it attractive both for implementation and for further improvements.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Strong quantum nonlocality and unextendibility without entanglement in $N$-partite systems with odd $N$**
  2022-03-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.14503)
  Yiyun He, Fei Shi, Xiande Zhang

  <details><summary>摘要 / Abstract</summary>

  A set of orthogonal product states is strongly nonlocal if it is locally irreducible in every bipartition, which shows the phenomenon of strong quantum nonlocality without entanglement. Although such a phenomenon has been shown to any three-, four-, and five-partite systems, the existence of strongly nonlocal orthogonal product sets in multipartite systems remains unknown. In this paper, by using a general decomposition of the $N$-dimensional hypercubes, we present strongly nonlocal orthogonal product sets in $N$-partite systems for all odd $N\geq 3$. Based on this decomposition, we give explicit constructions of unextendible product bases in $N$-partite systems for odd $N\geq 3$. Furthermore, we apply our results to quantum secret sharing, uncompletable product bases, and PPT entangled states.

  匹配依据：MPC: secret sharing

  </details>

- **Share $\\&amp;$ Shrink: (In-)Feasibility of MPC from one Broadcast-then-Asynchrony, and Delegated Computation**
  2022-03-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/378)
  Antoine Urban, Matthieu Rambaud

  <details><summary>摘要 / Abstract</summary>

  We consider protocols for secure multi-party computation (MPC) under honest majority, i.e., for $n$=$2t+1$ players of which $t$ are corrupt, that achieve guaranteed output delivery (GOD), and operate in a single initial round of broadcast (BC), followed by steps of asynchronous peer-to-peer (P2P) messages. The power of closely related ``hybrid networks&#x27;&#x27; was studied in [Fitzi-Nielsen, Disc&#x27;09], [BHN, Podc&#x27;10] and [Patra-Ravi, IEEE Tr. Inf. Theory&#x27;18]. The interest of such protocols is that they go at the actual speed of the network, and security is preserved under arbitrary network conditions (past the initial BC). We first complete the picture of this model with an impossibility result showing that some setup is required to achieve honest majority MPC with GOD. We then consider a bare bulletin-board PKI setup, and leverage recent advances in multi-key homomorphic encryption [BJMS, Asiacrypt&#x27;20], to state the feasibility of MPC in a tight 1-BC-then-1 single step of asynchronous P2P messages. We then consider efficiency. The only protocols adaptable to such a network model and setup are [BJMS, Asiacrypt&#x27;20], which does not scale well for many players, and [GLS, Crypto&#x27;15], which does not support input delegation from external resource-constrained owners (such as IoT devices or smartphones), limiting its practical use. Our main contribution is a generic design that enables MPC in 1BC-then-asynchronous P2P. It operates over ciphertexts encrypted under a (threshold) single-key encryption scheme, resulting in the smallest sizes expectable and efficient evaluation. It can be implemented from any homomorphic encryption scheme built from linear maps (e.g., GSW, CL, ...). Our main building block is the squishing of the verifiable input sharing (``Share&#x27;&#x27;), in parallel with the distributed key generation (DKG) in the single BC, followed by threshold encryption (``Shrink&#x27;&#x27;) in one asynchronous step. Interestingly, it can be compiled as the first constant-round YOSO protocol in 1 BC.

  匹配依据：MPC: secure multi party computation

  </details>

- **Secure Two-party Computation Approach for NTRUEncrypt**
  2022-03-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/386)
  Lin You, Yan Wang, Liang Li, Gengran Hu

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation can provide a solution for privacy protection and ensure the correctness of the final calculation results. Lattice-based algorithms are considered to be one of the most promising post-quantum cryptographic algorithms due to a better balance among security, key sizes and calculation speeds. The NTRUEncrypt is a lattice-based anti-quantum attack cryptographic algorithm. Since there haven&#x27;t been much candidate post-quantum cryptographic algorithms for secure multi-party computation. In this paper, we propose a novel secure two-party computation scheme based on NTRUEncrypt and implement the polynomial multiplication operations under NTRUEncrypt-OT. Our secure two-party computation scheme mainly uses oblivious transfer and privacy set interaction. We prove the security of our scheme in the semi-honest model. Our scheme can be applied for multi-party computation scenarios, such as quantum attack-resisted E-votes or E-auctions.

  匹配依据：MPC: multi party computation, oblivious transfer, secure multi party computation, secure two party computation

  </details>

- **Poly Onions: Achieving Anonymity in the Presence of Churn**
  2022-03-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/392)
  Megumi Ando, Miranda Christ, Anna Lysyanskaya, Tal Malkin

  <details><summary>摘要 / Abstract</summary>

  Onion routing is a popular approach towards anonymous communication. Practical implementations are widely used (for example, Tor has millions of users daily), but are vulnerable to various traffic correlation attacks, and the theoretical foundations, despite recent progress, still lag behind. In particular, all works that model onion routing protocols and prove their security only address a single run, where each party sends and receives a single message of fixed length, once. Moreover, they all assume a static network setting, where the parties are stable throughout the lifetime of the protocol. In contrast, real networks have a high rate of churn (nodes joining and exiting the network), real users want to send multiple messages, and realistic adversaries may observe multiple runs of the protocol. In this paper, we initiate a formal treatment of onion routing in a setting with multiple runs over a dynamic network with churn. We provide the following contributions. -We define the cryptographic primitive of poly onion encryption, which is appropriate for a setting with churn. This primitive is inspired by duo onions, introduced by Iwanik, Klonowski, and Kutylowski (Communications and Multimedia Security, 2005) towards improving onion delivery rate. We generalize the idea, change it to add auxiliary helpers towards supporting better security, and propose formal definitions. -We construct an instantiation of poly onion encryption based on standard cryptographic primitives (CCA secure public key encryption with tags, PRP, MAC, and secret sharing). Our construction is secure against an active adversary, and is parameterized to allow flexible instantiations supporting a range of corruption thresholds and churn limits. -We formally model anonymous onion routing for multiple runs in the setting with churn, including a definition of strong anonymity, where the adversary has CCA-like access to oracles for generating and processing onions. -We prove that if an onion routing protocol satisfies a natural condition we define (&quot;simulatability&quot;), then strong single-run anonymity implies strong multiple-run anonymity. This condition is satisfied by existing onion routing schemes, such as the $\Pi_p$ protocol of Ando, Lysyanskaya, and Upfal (ICALP 2018). As a consequence, these schemes are anonymous also for multiple runs (although not when there is churn). -We provide an anonymous routing protocol, &quot;Poly $\Pi_p$,&quot; and prove that it is anonymous in the setting with churn, against a passive adversary. We obtain this construction by using an instance of our poly onion encryption within the $\Pi_p$ protocol.

  匹配依据：MPC: secret sharing

  </details>

- **Auditable, Available and Resilient Private Computation on the Blockchain via MPC**
  2022-03-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/398)
  Christopher Cordi, Michael P. Frank, Kasimir Gabert, Carollan Helinski, Ryan C. Kao, Vladimir Kolesnikov, Abrahim Ladha, Nicholas Pattengale

  <details><summary>摘要 / Abstract</summary>

  Simple but mission-critical internet-based applications that require extremely high reliability, availability, and verifiability (e.g., auditability) could benefit from running on robust public programmable blockchain platforms such as Ethereum. Unfortunately, program code running on such blockchains is normally publicly viewable, rendering these platforms unsuitable for applications requiring strict privacy of application code, data, and results. In this work, we investigate using MPC techniques to protect the privacy of a blockchain computation. While our main goal is to hide both the data and the computed function itself, we also consider the standard MPC setting where the function is public. We describe GABLE (Garbled Autonomous Bots Leveraging Ethereum), a blockchain MPC architecture and system. The GABLE architecture specifies the roles and capabilities of the players. GABLE includes two approaches for implementing MPC over blockchain: Garbled Circuits (GC), evaluating universal circuits, and Garbled Finite State Automata (GFSA). We formally model and prove the security of GABLE implemented over garbling schemes, a popular abstraction of GC and GFSA from (Bellare et al, CCS 2012). We analyze in detail the performance (including Ethereum gas costs) of both approaches and discuss the trade-offs. We implement a simple prototype of GABLE and report on the implementation issues and experience.

  匹配依据：MPC: garbled circuits, garbling schemes

  </details>

- **A lightweight verifiable secret sharing scheme in IoTs**
  2022-03-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/395)
  Likang Lu, Jianzhu Lu

  <details><summary>摘要 / Abstract</summary>

  Verifiable secret sharing (VSS) is a fundamental tool of cryptography and distributed computing in Internet of things (IoTs). Since network bandwidth is a scarce resource, minimizing the number of verification data will improve the performance of VSS. Existing VSS schemes, however, face limitations in meeting the number of verification data and energy consumptions for low-end devices, which make their adoption challenging in resource-limited IoTs. To address above limitations, we propose a VSS scheme according to Nyberg’s oneway accumulator for one-way hash functions (NAHFs). The proposed scheme has two distinguished features: first, the security of the scheme is based on NAHFs whose computational requirements are the basic criteria for known IoT devices and, second, upon receiving only one verification data, participants can verify the correctness of both their shares and the secret without any communication. Experimental results demonstrate that, compared to the Feldman scheme and Rajabi-Eslami scheme, the energy consumption of a participant in the proposed scheme is respectively reduced by at least 24% and 83% for a secret.

  匹配依据：MPC: secret sharing

  </details>

- **A Linear-Time 2-Party Secure Merge Protocol**
  2022-03-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/380)
  Brett Hemenway Falk, Rohit Nema, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  We present a linear-time, space and communication data-oblivious algorithm for securely merging two private, sorted lists into a single sorted, secret-shared list in the two party setting. Although merging two sorted lists can be done insecurely in linear time, previous secure merge algorithms all require super-linear time and communication. A key feature of our construction is a novel method to obliviously traverse permuted lists in sorted order. Our algorithm only requires black-box use of the underlying Additively Homomorphic cryptosystem and generic secure computation schemes for comparison and equality testing.

  匹配依据：MPC: secure computation

  </details>

- **Privacy-preserving record linkage using local sensitive hash and private set intersection**
  2022-03-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.14284)
  Allon Adir, Ehud Aharoni, Nir Drucker, Eyal Kushnir, Ramy Masalha, Michael Mirkin, Omri Soceanu

  <details><summary>摘要 / Abstract</summary>

  The amount of data stored in data repositories increases every year. This makes it challenging to link records between different datasets across companies and even internally, while adhering to privacy regulations. Address or name changes, and even different spelling used for entity data, can prevent companies from using private deduplication or record-linking solutions such as private set intersection (PSI). To this end, we propose a new and efficient privacy-preserving record linkage (PPRL) protocol that combines PSI and local sensitive hash (LSH) functions, and runs in linear time. We explain the privacy guarantees that our protocol provides and demonstrate its practicality by executing the protocol over two datasets with $2^{20}$ records each, in $11-45$ minutes, depending on network settings.

  匹配依据：MPC: private set intersection

  </details>

- **Adversarial Representation Sharing: A Quantitative and Secure Collaborative Learning Framework**
  2022-03-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.14299)
  Jikun Chen, Feng Qiang, Na Ruan

  <details><summary>摘要 / Abstract</summary>

  The performance of deep learning models highly depends on the amount of training data. It is common practice for today&#x27;s data holders to merge their datasets and train models collaboratively, which yet poses a threat to data privacy. Different from existing methods such as secure multi-party computation (MPC) and federated learning (FL), we find representation learning has unique advantages in collaborative learning due to the lower communication overhead and task-independency. However, data representations face the threat of model inversion attacks. In this article, we formally define the collaborative learning scenario, and quantify data utility and privacy. Then we present ARS, a collaborative learning framework wherein users share representations of data to train models, and add imperceptible adversarial noise to data representations against reconstruction or attribute extraction attacks. By evaluating ARS in different contexts, we demonstrate that our mechanism is effective against model inversion attacks, and achieves a balance between privacy and utility. The ARS framework has wide applicability. First, ARS is valid for various data types, not limited to images. Second, data representations shared by users can be utilized in different tasks. Third, the framework can be easily extended to the vertical data partitioning scenario.

  匹配依据：MPC: secure multi party computation

  </details>

- **Physical Layer Security Assisted Computation Offloading in Intelligently Connected Vehicle Networks**
  2022-03-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.13536)
  Yiliang Liu, Wei Wang, Hsiao-Hwa Chen, Feng Lyu, Liangmin Wang, Weixiao Meng, Xuemin, Shen

  <details><summary>摘要 / Abstract</summary>

  In this paper, we propose a secure computation offloading scheme (SCOS) in intelligently connected vehicle (ICV) networks, aiming to minimize overall latency of computing via offloading part of computational tasks to nearby servers in small cell base stations (SBSs), while securing the information delivered during offloading and feedback phases via physical layer security. Existing computation offloading schemes usually neglected time-varying characteristics of channels and their corresponding secrecy rates, resulting in an inappropriate task partition ratio and a large secrecy outage probability. To address these issues, we utilize an ergodic secrecy rate to determine how many tasks are offloaded to the edge, where ergodic secrecy rate represents the average secrecy rate over all realizations in a time-varying wireless channel. Adaptive wiretap code rates are proposed with a secrecy outage constraint to match time-varying wireless channels. In addition, the proposed secure beamforming and artificial noise (AN) schemes can improve the ergodic secrecy rates of uplink and downlink channels even without eavesdropper channel state information (CSI). Numerical results demonstrate that the proposed schemes have a shorter system delay than the strategies neglecting time-varying characteristics.

  匹配依据：MPC: secure computation

  </details>

- **Energy-Efficient and Physical Layer Secure Computation Offloading in Blockchain-Empowered Internet of Things**
  2022-03-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.13526)
  Yiliang Liu, Zhou Su, Yuntao Wang

  <details><summary>摘要 / Abstract</summary>

  This paper investigates computation offloading in blockchain-empowered Internet of Things (IoT), where the task data uploading link from sensors to a base station (BS) is protected by intelligent reflecting surface (IRS)-assisted physical layer security (PLS). After receiving task data, the BS allocates computational resources provided by mobile edge computing (MEC) servers to help sensors perform tasks. Existing blockchain-based computation offloading schemes usually focus on network performance improvements, such as energy consumption minimization or latency minimization, and neglect the Gas fee for computation offloading, resulting in the dissatisfaction of high Gas providers. Also, the secrecy rate during the data uploading process can not be measured by a steady value because of the time-varying characteristics of IRS-based wireless channels, thereby computational resources allocation with a secrecy rate measured before data uploading is inappropriate. In this paper, we design a Gas-oriented computation offloading scheme that guarantees a low degree of dissatisfaction of sensors, while reducing energy consumption. Also, we deduce the ergodic secrecy rate of IRS-assisted PLS transmission that can represent the global secrecy performance to allocate computational resources. The simulations show that the proposed scheme has lower energy consumption compared to existing schemes, and ensures that the node paying higher Gas gets stronger computational resources.

  匹配依据：MPC: secure computation

  </details>

- **Secure Multi-Party Delegated Authorisation For Access and Sharing of Electronic Health Records**
  2022-03-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.12837)
  Kheng-Leong Tan, Chi-Hung Chi, Kwok-Yan Lam

  <details><summary>摘要 / Abstract</summary>

  Timely sharing of electronic health records (EHR) across providers is essential and significance in facilitating medical researches and prompt patients&#x27; care. With sharing, it is crucial that patients can control who can access their data and when, and guarantee the security and privacy of their data. In current literature, various system models, cryptographic techniques and access control mechanisms are proposed which requires patient&#x27;s consent before sharing. However, they mostly focus on patient is available to authorize the access of the EHR upon requested. This is impractical given that the patient may not always be in a good state to provide this authorization, eg, being unconscious and requires immediate medical attention. To address this gap, this paper proposes an efficient and secure protocol for the pre-delegation of authorization to multi-party for the access of the EHR when patient is unavailable to do so. The solution adopts a novel approach to combine self-sovereign identity concepts and framework with secure multi-party computation to enable secure identity and authorization verification. Theoretical analysis showed that it increased the efficiency of the protocol and verification processes to ensure the security and privacy of patient&#x27;s data.

  匹配依据：MPC: secure multi party computation

  </details>

- **CRGC -- A Practical Framework for Constructing Reusable Garbled Circuits**
  2022-03-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.12646)
  Christopher Harth-Kitzerow, Georg Carle, Fan Fei, Andre Luckow, Johannes Klepsch

  <details><summary>摘要 / Abstract</summary>

  In this work, we introduce two schemes to construct reusable garbled circuits (RGCs) in the semi-honest setting. Our completely reusable garbled circuit (CRGC) scheme allows the generator (party A) to construct and send an obfuscated boolean circuit along with an encoded input to the evaluator (party B). In contrast to Yao&#x27;s Garbled Circuit protocol, B can securely evaluate the same CRGC with an arbitrary number of inputs. As a tradeoff, CRGCs predictably leak some input bits of A to B. We also propose a partially reusable garbled circuit (PRGC) scheme that divides a circuit into reusable and non-reusable sections. PRGCs do not leak input bits of A. We benchmark our CRGC implementation against the state-of-the-art garbled circuit libraries EMP SH2PC and TinyGarble2. Using our framework, evaluating a CRGC is up to twenty times faster, albeit with weaker privacy guarantees, than evaluating an equivalent garbled circuit constructed by the two existing libraries. Our open-source library can convert any C++ function to a CRGC at approx. 80 million gates per second and repeatedly evaluate a CRGC at approx. 350 million gates per second. Additionally, a compressed CRGC is approx. 75% smaller in file size than the unobfuscated boolean circuit.

  匹配依据：MPC: garbled circuit, garbled circuits

  </details>

- **Weight distributions of two classes of linear codes**
  2022-03-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.11813)
  Xina Zhang

  <details><summary>摘要 / Abstract</summary>

  In this paper, based on the theory of defining sets, two classes of at most six-weight linear codes over $\mathbb{F}_p$ are constructed. The weight distributions of the linear codes are determined by means of Gaussian period and Weil sums. In some case, there is an almost optimal code with respect to Griesmer bound, which is also an optimal one according to the online code table. The linear codes can also be employed to get secret sharing schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Simple Three-Round Multiparty Schnorr Signing with Full Simulatability**
  2022-03-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/374)
  Yehuda Lindell

  <details><summary>摘要 / Abstract</summary>

  In a multiparty signing protocol, also known as a threshold signature scheme, the private signing key is shared amongst a set of parties and only a quorum of those parties can generate a signature. Research on multiparty signing has been growing in popularity recently due to its application to cryptocurrencies. Most work has focused on reducing the number of rounds to two, and as a result: (a) are not fully simulatable in the sense of MPC real/ideal security definitions, and/or (b) are not secure under concurrent composition, and/or (c) utilize non-standard assumptions of different types in their proofs of security. In this paper, we describe a simple three-round multiparty protocol for Schnorr signatures and prove its security. The protocol is fully simulatable, secure under concurrent composition, and proven secure in the standard model or random-oracle model (depending on the instantiations of the commitment and zero-knowledge primitives). The protocol realizes an ideal Schnorr signing functionality with perfect security in the ideal commitment and zero-knowledge hybrid model (and thus the only assumptions needed are for realizing these functionalities). In our presentation, we do not assume that all parties begin with the message to be signed, the identities of the participating parties and a unique common session identifier, since this is often not the case in practice. Rather, the parties achieve consensus on these parameters as the protocol progresses.

  匹配依据：MPC: mpc (context)

  </details>

- **SPRITE: A Scalable Privacy-Preserving and Verifiable Collaborative Learning for Industrial IoT**
  2022-03-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.11914)
  Jayasree Sengupta, Sushmita Ruj, Sipra Das Bit

  <details><summary>摘要 / Abstract</summary>

  Recently collaborative learning is widely applied to model sensitive data generated in Industrial IoT (IIoT). It enables a large number of devices to collectively train a global model by collaborating with a server while keeping the datasets on their respective premises. However, existing approaches are limited by high overheads and may also suffer from falsified aggregated results returned by a malicious server. Hence, we propose a Scalable, Privacy-preserving and veRIfiable collaboraTive lEarning (SPRITE) algorithm to train linear and logistic regression models for IIoT. We aim to reduce burden from resource-constrained IIoT devices and trust dependence on cloud by introducing fog as a middleware. SPRITE employs threshold secret sharing to guarantee privacy-preservation and robustness to IIoT device dropout whereas verifiable additive homomorphic secret sharing to ensure verifiability during model aggregation. We prove the security of SPRITE in an honest-but-curious setting where the cloud is untrustworthy. We validate SPRITE to be scalable and lightweight through theoretical overhead analysis and extensive testbed experimentation on an IIoT use-case with two real-world industrial datasets. For a large-scale industrial setup, SPRITE records 65% and 55% improved performance over its competitor for linear and logistic regressions respectively while reducing communication overhead for an IIoT device by 90%.

  匹配依据：MPC: secret sharing

  </details>

- **An Algebraic Framework for Silent Preprocessing with Trustless Setup and Active Security**
  2022-03-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/363)
  Damiano Abram, Ivan Damgård, Claudio Orlandi, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  Recently, number-theoretic assumptions including DDH, DCR and QR have been used to build powerful tools for secure computation, in the form of homomorphic secret-sharing (HSS), which leads to secure two-party computation protocols with succinct communication, and pseudorandom correlation functions (PCFs), which allow non-interactive generation of a large quantity of correlated randomness. In this work, we present a group-theoretic framework for these classes of constructions, which unifies their approach to computing distributed discrete logarithms in various groups. We cast existing constructions in our framework, and also present new constructions, including one based on class groups of imaginary quadratic fields. This leads to the first construction of two-party homomorphic secret sharing for branching programs from class group assumptions. Using our framework, we also obtain pseudorandom correlation functions for generating oblivious transfer and vector-OLE correlations from number-theoretic assumptions. These have a trustless, public-key setup when instantiating our framework using class groups. Previously, such constructions either needed a trusted setup in the form of an RSA modulus with unknown factorisation, or relied on multi-key fully homomorphic encryption from the learning with errors assumption. We also show how to upgrade our constructions to achieve active security using appropriate zero-knowledge proofs. In the random oracle model, this leads to a one-round, actively secure protocol for setting up the PCF, as well as a 3-round, actively secure HSS-based protocol for secure two-party computation of branching programs with succinct communication.

  匹配依据：MPC: oblivious transfer, secret sharing, secure computation, secure two party computation

  </details>

- **A constant lower bound for any quantum protocol for secure function evaluation**
  2022-03-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.08268)
  Sarah Osborn, Jamie Sikora

  <details><summary>摘要 / Abstract</summary>

  Secure function evaluation is a two-party cryptographic primitive where Bob computes a function of Alice&#x27;s and his respective inputs, and both hope to keep their inputs private from the other party. It has been proven that perfect (or near perfect) security is impossible, even for quantum protocols. We generalize this no-go result by exhibiting a constant lower bound on the cheating probabilities for any quantum protocol for secure function evaluation, and present many applications from oblivious transfer to the millionaire&#x27;s problem. Constant lower bounds are of practical interest since they imply the impossibility to arbitrarily amplify the security of quantum protocols by any means.

  匹配依据：MPC: oblivious transfer, secure function evaluation

  </details>

- **Shorter Signatures from MQ**
  2022-03-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/344)
  William Wang

  <details><summary>摘要 / Abstract</summary>

  We describe a simple MPC protocol in the preprocessing model for computing multivariate quadratic maps. This yields Mesquite, a KKW-style signature scheme which, to our knowledge, produces the shortest signatures of any based on the MQ assumption. For example, our compact parameter set targeting NIST security level I has an average signature size of 8.8KB and runtimes on par with Picnic3 L1.

  匹配依据：MPC: mpc (context)

  </details>

- **Information-Theoretic Secure and Private Voting System**
  2022-03-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.07355)
  Seyed Reza Hoseini Najarkolaei, Narges Kazempour, Hasti Rostami, Mohammad Reza Aref

  <details><summary>摘要 / Abstract</summary>

  In this paper, we present a private voting system that consists of N authorized voters who may vote to one of the K candidates or vote abstain. Each voter wants to compute the final tally while staying private and robust against malicious voters, who try to gain information about the vote of the other voters beyond the final result, or send incorrect information to affect the final tally. We design an information-theoretic private voting system based on Shamir secret sharing, which is secure and robust as long as there are up to (N-1)/3 malicious voters.

  匹配依据：MPC: secret sharing

  </details>

- **From Farfalle to Megafono via Ciminion: The PRF Hydra for MPC Applications**
  2022-03-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/342)
  Lorenzo Grassi, Morten Øygarden, Markus Schofnegger, Roman Walch

  <details><summary>摘要 / Abstract</summary>

  The area of multi-party computation (MPC) has recently increased in popularity and number of use cases. At the current state of the art, Ciminion, a Farfalle-like cryptographic function, achieves the best performance in MPC applications involving symmetric primitives. However, it has a critical weakness. Its security highly relies on the independence of its subkeys, which is achieved by using an expensive key schedule. Many MPC use cases involving symmetric pseudo-random functions (PRFs) rely on secretly shared symmetric keys, and hence the expensive key schedule must also be computed in MPC. As a result, Ciminion&#x27;s performance is significantly reduced in these use cases. In this paper we solve this problem. Following the approach introduced by Ciminion&#x27;s designers, we present a novel primitive in symmetric cryptography called Megafono. Megafono is a keyed extendable PRF, expanding a fixed-length input to an arbitrary-length output. Similar to Farfalle, an initial keyed permutation is applied to the input, followed by an expansion layer, involving the parallel application of keyed ciphers. The main novelty regards the expansion of the intermediate/internal state for &quot;free&quot;, by appending the sum of the internal states of the first permutation to its output. The combination of this and other modifications, together with the impossibility for the attacker to have access to the input state of the expansion layer, make Megafono very efficient in the target application. As a concrete example, we present the PRF Hydra, an instance of Megafono based on the Hades strategy and on generalized versions of the Lai--Massey scheme. Based on an extensive security analysis, we implement Hydra in an MPC framework. The results show that it outperforms all MPC-friendly schemes currently published in the literature.

  匹配依据：MPC: multi party computation

  </details>

- **Extracting perfect GHZ states from imperfect weighted graph states via entanglement concentration**
  2022-03-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.07210)
  Rafail Frantzeskakis, Chenxu Liu, Zahra Raissi, Edwin Barnes, Sophia E. Economou

  <details><summary>摘要 / Abstract</summary>

  Photonic GHZ states serve as the central resource for a number of important applications in quantum information science, including secret sharing, sensing, and fusion-based quantum computing. The use of photon-emitter entangling gates is a promising approach to creating these states that sidesteps many of the difficulties associated with intrinsically probabilistic methods based on linear optics. However, the efficient creation of high-fidelity GHZ states of many photons remains an outstanding challenge due to both coherent and incoherent errors during the generation process. Here, we propose an entanglement concentration protocol that is capable of generating perfect GHZ states using only local gates and measurements on imperfect weighted graph states. We show that our protocol is both efficient and robust to incoherent noise errors.

  匹配依据：MPC: secret sharing

  </details>

- **CostCO: An automatic cost modeling framework for secure multi-party computation**
  2022-03-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/332)
  Vivian Fang, Lloyd Brown, William Lin, Wenting Zheng, Aurojit Panda, Raluca Ada Popa

  <details><summary>摘要 / Abstract</summary>

  The last decade has seen an explosion in the number of new secure multi-party computation (MPC) protocols that enable collaborative computation on sensitive data. No single MPC protocol is optimal for all types of computation. As a result, researchers have created hybrid-protocol compilers that translate a program into a hybrid protocol that mixes different MPC protocols. Hybrid-protocol compilers crucially rely on accurate cost models, which are handwritten by the compilers&#x27; developers, to choose the correct schedule of protocols. In this paper, we propose CostCO, the first automatic MPC cost modeling framework. CostCO develops a novel API to interface with a variety of MPC protocols, and leverages domain-specific properties of MPC in order to enable efficient and automatic cost-model generation for a wide range of MPC protocols. CostCO employs a two-phase experiment design to efficiently synthesize cost models of the MPC protocol’s runtime as well as its memory and network usage. We verify CostCO’s modeling accuracy for several full circuits, characterize the engineering effort required to port existing MPC protocols, and demonstrate how hybrid-protocol compilers can leverage CostCO’s cost models.

  匹配依据：MPC: secure multi party computation

  </details>

- **Adaptive Gap Entangled Polynomial Coding for Multi-Party Computation at the Edge**
  2022-03-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.06759)
  Elahe Vedadi, Yasaman Keshtkarjahromi, Hulya Seferoglu

  <details><summary>摘要 / Abstract</summary>

  Multi-party computation (MPC) is promising for designing privacy-preserving machine learning algorithms at edge networks. An emerging approach is coded-MPC (CMPC), which advocates the use of coded computation to improve the performance of MPC in terms of the required number of workers involved in computations. The current approach for designing CMPC algorithms is to merely combine efficient coded computation constructions with MPC. Instead, we propose a new construction; Adaptive Gap Entangled polynomial (AGE) codes, where the degrees of polynomials used in computations are optimized for MPC. We show that MPC with AGE codes (AGE-CMPC) performs better than existing CMPC algorithms in terms of the required number of workers as well as storage, communication and computation load.

  匹配依据：MPC: multi party computation

  </details>

- **Efficient Online-friendly Two-Party ECDSA Signature**
  2022-03-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/318)
  Haiyang Xue, Man Ho Au, Xiang Xie, Tsz Hon Yuen, Handong Cui

  <details><summary>摘要 / Abstract</summary>

  Two-party ECDSA signatures have received much attention due to their widespread deployment in cryptocurrencies. Depending on whether or not the message is required, we could divide two-party signing into two different phases, namely, offline and online. Ideally, the online phase should be made as lightweight as possible. At the same time, the cost of the offline phase should remain similar to that of a normal signature generation. However, the existing two-party protocols of ECDSA are not optimal: either their online phase requires decryption of a ciphertext, or their offline phase needs at least two executions of multiplicative-to-additive conversion which dominates the overall complexity. This paper proposes an online-friendly two-party ECDSA with a lightweight online phase and a single multiplicative-to-additive function in the offline phase. It is constructed by a novel design of a re-sharing of the secret key and a linear sharing of the nonce. Our scheme significantly improves previous protocols based on either oblivious transfer or homomorphic encryption. We implement our scheme and show that it outperforms prior online-friendly schemes (i.e., those have lightweight online cost) by a factor of roughly 2 to 9 in both communication and computation. Furthermore, our two-party scheme could be easily extended to the $2$-out-of-$n$ threshold ECDSA.

  匹配依据：MPC: oblivious transfer

  </details>

- **Quantum Local Differential Privacy and Quantum Statistical Query Model**
  2022-03-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.03591)
  Armando Angrisani, Elham Kashefi

  <details><summary>摘要 / Abstract</summary>

  Quantum statistical queries provide a theoretical framework for investigating the computational power of a learner with limited quantum resources. This model is particularly relevant in the current context, where available quantum devices are subject to severe noise and have limited quantum memory. On the other hand, the framework of quantum differential privacy demonstrates that noise can, in some cases, benefit the computation, enhancing robustness and statistical security. In this work, we establish an equivalence between quantum statistical queries and quantum differential privacy in the local model, extending a celebrated classical result to the quantum setting. Furthermore, we derive strong data processing inequalities for the quantum relative entropy under local differential privacy and apply this result to the task of asymmetric hypothesis testing with restricted measurements. Finally, we consider the task of quantum multi-party computation under local differential privacy. As a proof of principle, we demonstrate that the parity function is efficiently learnable in this model, whereas the corresponding classical task requires exponentially many samples.

  匹配依据：MPC: multi party computation

  </details>

- **Minimizing Setup in Broadcast-Optimal Two Round MPC**
  2022-03-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/293)
  Ivan Damgård, Divya Ravi, Luisa Siniscalchi, Sophia Yakoubov

  <details><summary>摘要 / Abstract</summary>

  In this paper we consider two-round secure computation protocols which use different communication channels in different rounds: namely, protocols where broadcast is available in neither round, both rounds, only the first round, or only the second round. The prior works of Cohen, Garay and Zikas (Eurocrypt 2020) and Damgård, Magri, Ravi, Siniscalchi and Yakoubov (Crypto 2021) give tight characterizations of which security guarantees are achievable for various thresholds in each communication structure. In this work, we introduce a new security notion, namely, selective identifiable abort, which guarantees that every honest party either obtains the output, or aborts identifying one corrupt party (where honest parties may potentially identify different corrupted parties). We investigate what broadcast patterns in two-round MPC allow achieving this guarantee across various settings (such as with or without PKI, with or without an honest majority). Further, we determine what is possible in the honest majority setting without a PKI, closing a question left open by Damgård et al. We show that without a PKI, having an honest majority does not make it possible to achieve stronger security guarantees compared to the dishonest majority setting. However, if two-thirds of the parties are guaranteed to be honest, identifiable abort is additionally achievable using broadcast only in the second round. We use fundamentally different techniques from the previous works to avoid relying on private communication in the first round when a PKI is not available, since assuming such private channels without the availability of public encryption keys is unrealistic. We also show that, somewhat surprisingly, the availability of private channels in the first round does not enable stronger security guarantees unless the corruption threshold is one.

  匹配依据：MPC: secure computation

  </details>

- **Low-Communication Multiparty Triple Generation for SPDZ from Ring-LPN**
  2022-03-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/315)
  Damiano Abram, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  The SPDZ protocol for multi-party computation relies on a correlated randomness setup consisting of authenticated, multiplication triples. A recent line of work by Boyle et al. (Crypto 2019, Crypto 2020) has investigated the possibility of producing this correlated randomness in a silent preprocessing phase, which involves a “small” setup protocol with less communication than the total size of the triples being produced. These works do this using a tool called a pseudorandom correlation generator (PCG), which allows a large batch of correlated randomness to be compressed into a set of smaller, correlated seeds. However, existing methods for compressing SPDZ triples only apply to the 2-party setting. In this work, we construct a PCG for producing SPDZ triples over large prime fields in the multi-party setting. The security of our PCG is based on the ring-LPN assumption over fields, similar to the work of Boyle et al. (Crypto 2020) in the 2-party setting. We also present a corresponding, actively secure setup protocol, which can be used to generate the PCG seeds and instantiate SPDZ with a silent preprocessing phase. As a building block, which may be of independent interest, we construct a new type of 3-party distributed point function supporting outputs over arbitrary groups (including large prime order), as well as an efficient protocol for setting up our DPF keys with active security.

  匹配依据：MPC: multi party computation

  </details>

- **Efficient Proof of RAM Programs from Any Public-Coin Zero-Knowledge System**
  2022-03-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/313)
  Cyprien Delpech de Saint Guilhem, Emmanuela Orsini, Titouan Tanguy, Michiel Verbauwhede

  <details><summary>摘要 / Abstract</summary>

  We show a compiler that allows to prove the correct execution of RAM programs using any zero-knowledge system for circuit satisfiability. At the core of this work is an arithmetic circuit which verifies the consistency of a list of memory access tuples in zero-knowledge. Using such a circuit, we obtain the first constant-round and concretely efficient zero-knowledge proof protocol for RAM programs using any stateless zero-knowledge proof system for Boolean or arithmetic circuits. Both the communication complexity and the prover and verifier run times asymptotically scale linearly in the size of the memory and the run time of the RAM program; we demonstrate concrete efficiency with performance results of our C++ implementation. We concretely instantiate our construction with an efficient MPC-in-the-Head proof system, Limbo (ACM CCS 2021). The C++ implementation of our access protocol extends that of Limbo and provides interactive proofs with 40 bits of statistical security with an amortized cost of 0.42ms of prover time and 2.8KB of communication per memory access, independently of the size of the memory; with multi-threading, this cost is reduced to 0.12ms and 1.8KB respectively. This performance of our public-coin protocol approaches that of private-coin protocol BubbleRAM (ACM CCS 2020, 0.15ms and 1.5KB per access).

  匹配依据：MPC: mpc (context)

  </details>

- **Bounded Functional Encryption for Turing Machines: Adaptive Security from General Assumptions**
  2022-03-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/316)
  Shweta Agrawal, Fuyuki Kitagawa, Anuja Modi, Ryo Nishimaki, Shota Yamada, Takashi Yamakawa

  <details><summary>摘要 / Abstract</summary>

  The recent work of Agrawal et al., [Crypto &#x27;21] and Goyal et al. [Eurocrypt &#x27;22] concurrently introduced the notion of dynamic bounded collusion security for functional encryption (FE) and showed a construction satisfying the notion from identity based encryption (IBE). Agrawal et al., [Crypto &#x27;21] further extended it to FE for Turing machines in non-adaptive simulation setting from the sub-exponential learining with errors assumption (LWE). Concurrently, the work of Goyal et al. [Asiacrypt &#x27;21] constructed attribute based encryption (ABE) for Turing machines achieving adaptive indistinguishability based security against bounded (static) collusions from IBE, in the random oracle model. In this work, we significantly improve the state of art for dynamic bounded collusion FE and ABE for Turing machines by achieving adaptive simulation style security from a broad class of assumptions, in the standard model. In more detail, we obtain the following results: - We construct an adaptively secure (AD-SIM) FE for Turing machines, supporting dynamic bounded collusion, from sub-exponential LWE. This improves the result of Agrawal et al. which achieved only non-adaptive (NA-SIM) security in the dynamic bounded collusion model. - Towards achieving the above goal, we construct a ciphertext policy FE scheme (CPFE) for circuits of unbounded size and depth, which achieves AD-SIM security in the dynamic bounded collusion model from IBE and laconic oblivious transfer (LOT). Both IBE and LOT can be instantiated from a large number of mild assumptions such as the computational Diffie-Hellman assumption, the factoring assumption, and polynomial LWE. - We construct an AD-SIM secure FE for Turing machines, supporting dynamic bounded collusions, from LOT, ABE for NC1 (or NC) and private information retrieval (PIR) schemes which satisfy certain properties. This significantly expands the class of assumptions on which AD-SIM secure FE for Turing machines can be based. In particular, it leads to new constructions of FE for Turing machines including one based on polynomial LWE and one based on the combination of the bilinear decisional Diffie-Hellman assumption and the decisional Diffie-Hellman assumption on some specific groups. In contrast the only prior construction by Agrawal et al. achieved only NASIM security and relied on sub-exponential LWE. To achieve the above result, we define the notion of CPFE for read only RAM programs and succinct FE for LOT, which may be of independent interest. - We also construct an ABE scheme for Turing machines which achieves AD-IND security in the standard model supporting dynamic bounded collusions. Our scheme is based on IBE and LOT. Previously, the only known candidate that achieved AD-IND security from IBE by Goyal et al. relied on the random oracle model.

  匹配依据：MPC: oblivious transfer

  </details>

- **Batch-OT with Optimal Rate**
  2022-03-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/314)
  Zvika Brakerski, Pedro Branco, Nico Döttling, Sihang Pu

  <details><summary>摘要 / Abstract</summary>

  We show that it is possible to perform $n$ independent copies of $1$-out-of-$2$ oblivious transfer in two messages, where the communication complexity of the receiver and sender (each) is $n(1+o(1))$ for sufficiently large $n$. Note that this matches the information-theoretic lower bound. Prior to this work, this was only achievable by using the heavy machinery of rate-$1$ fully homomorphic encryption (Rate-$1$ FHE, Brakerski et al., TCC 2019). To achieve rate-$1$ both on the receiver&#x27;s and sender&#x27;s end, we use the LPN assumption, with slightly sub-constant noise rate $1/m^{\epsilon}$ for any $\epsilon&gt;0$ together with either the DDH, QR or LWE assumptions. In terms of efficiency, our protocols only rely on linear homomorphism, as opposed to the FHE-based solution which inherently requires an expensive ``bootstrapping&#x27;&#x27; operation. We believe that in terms of efficiency we compare favorably to existing batch-OT protocols, while achieving superior communication complexity. We show similar results for Oblivious Linear Evaluation (OLE). For our DDH-based solution we develop a new technique that may be of independent interest. We show that it is possible to ``emulate&#x27;&#x27; the binary group $\mathbb{Z}_2$ (or any other small-order group) inside a prime-order group $\mathbb{Z}_p$ in a function-private manner. That is, $\mathbb{Z}_2$ operations are mapped to $\mathbb{Z}_p$ operations such that the outcome of the latter do not reveal additional information beyond the $\mathbb{Z}_2$ outcome. Our encoding technique uses the discrete Gaussian distribution, which to our knowledge was not done before in the context of DDH.

  匹配依据：MPC: oblivious transfer

  </details>

- **A Plug-n-Play Framework for Scaling Private Set Intersection to Billion-sized Sets**
  2022-03-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/294)
  Saikrishna Badrinarayanan, Ranjit Kumaresan, Mihai Christodorescu, Vinjith Nagaraja, Karan Patel, Srinivasan Raghuraman, Peter Rindal, Wei Sun, Minghua Xu

  <details><summary>摘要 / Abstract</summary>

  Motivated by the recent advances in practical secure computation, we design and implement a framework for scaling solutions for the problem of private set intersection (PSI) into the realm of big data. A protocol for PSI enables two parties each holding a set of elements to jointly compute the intersection of these sets without revealing the elements that are not in the intersection. Following a long line of research, recent protocols for PSI only have $\approx 5\times$ computation and communication overhead over an insecure set intersection. However, this performance is typically demonstrated for set sizes in the order of ten million. In this work, we aim to scale these protocols to efficiently handle set sizes of one billion elements or more. We achieve this via a careful application of a binning approach that enables parallelizing any arbitrary PSI protocol. Building on this idea, we designed and implemented a framework that takes a pair of PSI executables (i.e., for each of the two parties) that typically works for million-sized sets, and then scales it to billion-sized sets (and beyond). For example, our framework can perform a join of billion-sized sets in 83 minutes compared to 2000 minutes of Pinkas et al. (ACM TPS 2018), an improvement of $25\times$. Furthermore, we present an end-to-end Spark application where two enterprises, each possessing private databases, can perform a restricted class of database join operations (specifically, join operations with only an on clause which is a conjunction of equality checks involving attributes from both parties, followed by a where clause which can be split into conjunctive clauses where each conjunction is a function of a single table) without revealing any data that is not part of the output.

  匹配依据：MPC: private set intersection, secure computation

  </details>

- **Tabula: Efficiently Computing Nonlinear Activation Functions for Secure Neural Network Inference**
  2022-03-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.02833)
  Maximilian Lam, Michael Mitzenmacher, Vijay Janapa Reddi, Gu-Yeon Wei, David Brooks

  <details><summary>摘要 / Abstract</summary>

  Multiparty computation approaches to secure neural network inference commonly rely on garbled circuits for securely executing nonlinear activation functions. However, garbled circuits require excessive communication between server and client, impose significant storage overheads, and incur large runtime penalties. To reduce these costs, we propose an alternative to garbled circuits: Tabula, an algorithm based on secure lookup tables. Our approach precomputes lookup tables during an offline phase that contains the result of all possible nonlinear function calls. Because these tables incur exponential storage costs in the number of operands and the precision of the input values, we use quantization to reduce these storage costs to make this approach practical. This enables an online phase where securely computing the result of a nonlinear function requires just a single round of communication, with communication cost equal to twice the number of bits of the input to the nonlinear function. In practice our approach costs 2 bytes of communication per nonlinear function call in the online phase. Compared to garbled circuits with 8-bit quantized inputs, when computing individual nonlinear functions during the online phase, experiments show Tabula with 8-bit activations uses between $280$-$560 \times$ less communication, is over $100\times$ faster, and uses a comparable (within a factor of 2) amount of storage; compared against other state-of-the-art protocols Tabula achieves greater than $40\times$ communication reduction. This leads to significant performance gains over garbled circuits with quantized inputs during the online phase of secure inference of neural networks: Tabula reduces end-to-end inference communication by up to $9 \times$ and achieves an end-to-end inference speedup of up to $50 \times$, while imposing comparable storage and offline preprocessing costs.

  匹配依据：MPC: garbled circuits, multiparty computation

  </details>

- **Verifiably Distributed Multi-User Secret Sharing schemes**
  2022-03-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/266)
  Likang Lu, Jianzhu Lu

  <details><summary>摘要 / Abstract</summary>

  Distributed secret sharing techniques, where a specific secret is encoded into its shares which are conveyed to the IoT device or its user via storage nodes, are considered. A verifiably distributed secret sharing (VDSS) provides a way for a legitimate user to verify the secret he reconstructs through the downloaded shares while the secrecy condition is satisfied in a weak or a perfect sense. This article examines the impact of minimizing verification information in a VDSS on the communication complexity and storage overhead, and achieves the verifiability in resource-limited IoTs by aggregating the verification information of different devices/users. Then, two secure VDSS are proposed. The first VDSS attains the lower bound on the communication complexity while providing the fault tolerance. The second VDSS simultaneously achieves the lower bounds of both communication complexity and storage overhead while providing the balanced storage load, thus showing the scheme that is optimal in terms of both parameters.

  匹配依据：MPC: secret sharing

  </details>

- **Universally Composable Subversion-Resilient Cryptography**
  2022-03-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/244)
  Suvradip Chakraborty, Bernardo Magri, Jesper Buus Nielsen, Daniele Venturi

  <details><summary>摘要 / Abstract</summary>

  Subversion attacks undermine security of cryptographic protocols by replacing a legitimate honest party&#x27;s implementation with one that leaks information in an undetectable manner. An important limitation of all currently known techniques for designing cryptographic protocols with security against subversion attacks is that they do not automatically guarantee security in the realistic setting where a protocol session may run concurrently with other protocols. We remedy this situation by providing a foundation of *reverse firewalls* (Mironov and Stephens-Davidowitz, EUROCRYPT&#x27;15) in the *universal composability* (UC) framework (Canetti, FOCS&#x27;01 and J. ACM&#x27;20). More in details, our contributions are threefold: - We generalize the UC framework to the setting where each party consists of a core (which has secret inputs and is in charge of generating protocol messages) and a firewall (which has no secrets and sanitizes the outgoing/incoming communication from/to the core). Both the core and the firewall can be subject to different flavors of corruption, modeling different kinds of subversion attacks. For instance, we capture the setting where a subverted core looks like the honest core to any efficient test, yet it may leak secret information via covert channels (which we call *specious subversion*). - We show how to sanitize UC commitments and UC coin tossing against specious subversion, under the DDH assumption. - We show how to sanitize the classical GMW compiler (Goldreich, Micali and Wigderson, STOC 1987) for turning MPC with security in the presence of semi-honest adversaries into MPC with security in the presence of malicious adversaries. This yields a completeness theorem for maliciously secure MPC in the presence of specious subversion. Additionally, all our sanitized protocols are *transparent*, in the sense that communicating with a sanitized core looks indistinguishable from communicating with an honest core. Thanks to the composition theorem, our methodology allows, for the first time, to design subversion-resilient protocols by sanitizing different sub-components in a modular way.

  匹配依据：MPC: mpc (context)

  </details>

- **Sublinear GMW-Style Compiler for MPC with Preprocessing**
  2022-03-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/261)
  Elette Boyle, Niv Gilboa, Yuval Ishai, Ariel Nof

  <details><summary>摘要 / Abstract</summary>

  We consider the efficiency of protocols for secure multiparty computation (MPC) with a dishonest majority. A popular approach for the design of such protocols is to employ preprocessing. Before the inputs are known, the parties generate correlated secret randomness, which is consumed by a fast and possibly ``information-theoretic&#x27;&#x27; online protocol. A powerful technique for securing such protocols against malicious parties uses homomorphic MACs to authenticate the values produced by the online protocol. Compared to a baseline protocol, which is only secure against semi-honest parties, this involves a significant increase in the size of the correlated randomness, by a factor of up to a statistical security parameter. Different approaches for partially mitigating this extra storage cost come at the expense of increasing the online communication. In this work we propose a new technique for protecting MPC with preprocessing against malicious parties. We show that for circuit evaluation protocols that satisfy mild security and structural requirements, that are met by many standard protocols with semi-honest security, the extra additive storage and online communication costs are both logarithmic in the circuit size. This applies to Boolean circuits and to arithmetic circuits over fields or rings, and to both information-theoretic and computationally secure protocols. Our protocol can be viewed as a sublinear information-theoretic variant of the celebrated ``GMW compiler&#x27;&#x27; that applies to natural protocols for MPC with preprocessing. Our compiler makes a novel use of the techniques of Boneh et al. (Crypto 2019) for sublinear distributed zero knowledge, which were previously only used in the setting of honest-majority MPC.

  匹配依据：MPC: secure multiparty computation

  </details>

- **On Codes and Learning With Errors over Function Fields**
  2022-03-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.13990) · [IACR ePrint](https://eprint.iacr.org/2022/269)
  Maxime Bombar, Alain Couvreur, Thomas Debris-Alazard

  <details><summary>摘要 / Abstract</summary>

  It is a long standing open problem to find search to decision reductions for structured versions of the decoding problem of linear codes. Such results in the lattice-based setting have been carried out using number fields: Polynomial–LWE, Ring–LWE, Module–LWE and so on. We propose a function field version of the LWE problem. This new framework leads to another point of view on structured codes, e.g. quasi-cyclic codes, strengthening the connection between lattice-based and code-based cryptography. In particular, we obtain the first search to decision reduction for structured codes. Following the historical constructions in lattice–based cryptography, we instantiate our construction with function fields analogues of cyclotomic fields, namely Carlitz extensions, leading to search to decision reductions on various versions of Ring-LPN, which have applications to secure multi party computation and to an authentication protocol.

  匹配依据：MPC: secure multi party computation

  </details>

- **Compact Storage for Homomorphic Encryption**
  2022-03-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/273)
  Adi Akavia, Neta Oren, Boaz Sapir, Margarita Vald

  <details><summary>摘要 / Abstract</summary>

  Homomorphic encryption (HE) is a promising technology for protecting data in use, with considerable recent years progress towards attaining practical runtime performance. However the high storage overhead associated with HE remains an obstacle preventing its large scale adoption. In this work we propose a new storage solution in the two-server model resolving the high storage overhead associated with HE, while preserving data confidentiality. Our solution attains the following desired properties: 1) *Compact storage* with zero overhead over storing AES ciphertexts, and $10\times$ to $10,000\times$ better than storing CKKS ciphertexts. 2) *Fast runtime performance* for storage and retrieval, only twice the time of directly storing and retrieving HE ciphertexts. 3) *Dynamic control during retrieval* of the HE parameters and the data items to be packed in each HE ciphertext. 4) *Plug-and-play compatibility* with any homomorphic computation. We implemented our solution into a proof-of-concept system running on AWS EC2 instances with AWS S3 storage, empirically demonstrating its appealing performance. As a central tool we introduce the first perfect secret sharing scheme with fast homomorphic reconstruction over the reals; this may be of independent interest.

  匹配依据：MPC: secret sharing

  </details>

- **VaultDB: A Real-World Pilot of Secure Multi-Party Computation within a Clinical Research Network**
  2022-02-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2203.00146)
  Jennie Rogers, Elizabeth Adetoro, Johes Bater, Talia Canter, Dong Fu, Andrew Hamilton, Amro Hassan, Ashley Martinez, Erick Michalski, Vesna Mitrovic, Fred Rachman, Raj Shah, Matt Sterling, Kyra VanDoren, Theresa L. Walunas, Xiao Wang, Abel Kho

  <details><summary>摘要 / Abstract</summary>

  Electronic health records represent a rich and growing source of clinical data for research. Privacy, regulatory, and institutional concerns limit the speed and ease of sharing this data. VaultDB is a framework for securely computing SQL queries over private data from two or more sources. It evaluates queries using secure multiparty computation: cryptographic protocols that evaluate a function such that the only information revealed from running it is the query answer. We describe the development of a HIPAA-compliant version of VaultDB on the Chicago Area Patient Centered Outcomes Research Network (CAPriCORN). This multi-institutional clinical research network spans the electronic health records of nearly 13M patients over hundreds of clinics and hospitals in the Chicago metropolitan area. Our results from deploying at three health systems within this network show its efficiency and scalability for distributed clinical research analyses without moving patient records from their site of origin.

  匹配依据：MPC: secure multi party computation, secure multiparty computation

  </details>

- **Private Location Sharing for Decentralized Routing services**
  2022-02-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.13305)
  Matthew Tsao, Kaidi Yang, Karthik Gopalakrishnan, Marco Pavone

  <details><summary>摘要 / Abstract</summary>

  Data-driven methodologies offer many exciting upsides, but they also introduce new challenges, particularly in the realm of user privacy. Specifically, the way data is collected can pose privacy risks to end users. In many routing services, a single entity (e.g., the routing service provider) collects and manages user trajectory data. When it comes to user privacy, these systems have a central point of failure since users have to trust that this entity will not sell or use their data to infer sensitive private information. Unfortunately, in practice many advertising companies offer to buy such data for the sake of targeted advertisements. With this as motivation, we study the problem of using location data for routing services in a privacy-preserving way. Rather than having users report their location to a central operator, we present a protocol in which users participate in a decentralized and privacy-preserving computation to estimate travel times for the roads in the network in a way that no individuals&#x27; location is ever observed by any other party. The protocol uses the Laplace mechanism in conjunction with secure multi-party computation to ensure that it is cryptogrpahically secure and that its output is differentially private. A natural question is if privacy necessitates degradation in accuracy or system performance. We show that if a road has sufficiently high capacity, then the travel time estimated by our protocol is provably close to the ground truth travel time. We validate the protocol through numerical experiments which show that using the protocol as a routing service provides privacy guarantees with minimal overhead to user travel time.

  匹配依据：MPC: secure multi party computation

  </details>

- **Zero-Knowledge Protocols for the Subset Sum Problem from MPC-in-the-Head with Rejection**
  2022-02-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/223)
  Thibauld Feneuil, Jules Maire, Matthieu Rivain, Damien Vergnaud

  <details><summary>摘要 / Abstract</summary>

  We propose zero-knowledge arguments for the modular subset sum problem. Given a set of integers, this problem asks whether a subset adds up to a given integer $t$ modulo a given integer $q$. This NP-complete problem is considered since the 1980s as an interesting alternative in cryptography to hardness assumptions based on number theory and it is in particular believed to provide post-quantum security. Previous combinatorial approaches, notably one due to Shamir, yield arguments with cubic communication complexity (in the security parameter). More recent methods, based on the MPC-in-the-head technique, also produce arguments with cubic communication complexity. We improve this approach by using a secret-sharing over small integers (rather than modulo $q$) to reduce the size of the arguments and remove the prime modulus restriction. Since this sharing may reveal information on the secret subset, we introduce the idea of rejection to the MPC-in-the-head paradigm. Special care has to be taken to balance completeness and soundness and preserve zero-knowledge of our arguments. We combine this idea with two techniques to prove that the secret vector (which selects the subset) is well made of binary coordinates. Our new techniques have the significant advantage to result in arguments of size independent of the modulus $q$. Our new protocols for the subset sum problem achieve an asymptotic improvement by producing arguments of quadratic size (against cubic size for previous proposals). This improvement is also practical: for a 256-bit modulus $q$, the best variant of our protocols yields 13KB arguments while previous proposals gave 1180KB arguments, for the best general protocol, and 122KB, for the best protocol restricted to prime modulus. Our techniques can also be applied to vectorial variants of the subset sum problem and in particular the inhomogeneous short integer solution (ISIS) problem for which they provide an efficient alternative to state-of-the-art protocols when the underlying ring is not small and NTT-friendly. We also show the application of our protocol to build efficient zero-knowledge arguments of plaintext and/or key knowledge in the context of fully-homomorphic encryption. When applied to the TFHE scheme, the obtained arguments are more than 20 times smaller than those obtained with previous protocols. Eventually, we use our technique to construct an efficient digital signature scheme based on a pseudo-random function due to Boneh-Halevi-Howgrave-Graham.

  匹配依据：MPC: secret sharing

  </details>
