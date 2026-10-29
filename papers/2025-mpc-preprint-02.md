# 2025 · MPC · 仅预印本来源 · 第 2/5 页

[总目录](../PAPERS.md) · [上一页](2025-mpc-preprint-01.md) · [下一页](2025-mpc-preprint-03.md)

- **Differential Fault Attacks on MQOM, Breaking the Heart of Multivariate Evaluation**
  2025-10-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1895)
  Vladimir Sarde, Nicolas Debande

  <details><summary>摘要 / Abstract</summary>

  MQOM is one of the fourteen remaining candidates in the second round of the NIST post-quantum signature standardization process. Introduced in 2023, MQOM instantiates the Multi-Party Computation in the Head (MPCitH) paradigm over the well-established hard problem of solving Multivariate Quadratic (MQ) equations. In this paper, we present the first fault attacks on MQOM targeting the MQ evaluation phase, which is a central component of the algorithm. We introduce four differential fault attacks and demonstrate their effectiveness against both unprotected and masked implementations. The first two target the secret key using a random fault model, making them particularly realistic and practical. With as little as one or two injected faults, depending on the variant, the entire secret key can be recovered through linear algebra. The other two attacks exploit faults on the coefficients of the MQ system directly. Our results highlight that the MQ evaluation, despite not being identified as a sensitive component until now, can be exploited using just a few fault injections.

  匹配依据：MPC: multi party computation

  </details>

- **Utilizing Model-Free Reinforcement Learning for Optimizing Secure Multi-Party Computation Protocols**
  2025-10-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.07814)
  Javad Sayyadi, Mahdi Nangir, Mahmood Mohassel Feghhi, Hamid Sayyadi

  <details><summary>摘要 / Abstract</summary>

  In this manuscript, we explore the application of model-free reinforcement learning in optimizing secure multiparty computation (SMPC) protocols. SMPC is a crucial tool for performing computations on private data without the need to disclose it, holding significant importance in various domains, including information security and privacy. However, the efficiency of current protocols is often suboptimal due to computational and communicational complexities. Our proposed approach leverages model-free reinforcement learning algorithms to enhance the performance of these protocols. We have designed a reinforcement learning model capable of dynamically learning and adapting optimal strategies for secure computations. Our experimental results demonstrate that employing this method leads to a substantial reduction in execution time and communication costs of the protocols. These achievements highlight the high potential of reinforcement learning in improving the efficiency of secure multiparty computation protocols, providing an effective solution to the existing challenges in this field.

  匹配依据：MPC: secure multi party computation, secure multiparty computation

  </details>

- **Role-Conditioned Refusals: Evaluating Access Control Reasoning in Large Language Models**
  2025-10-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.07642)
  Đorđe Klisura, Joseph Khoury, Ashish Kundu, Ram Krishnan, Anthony Rios

  <details><summary>摘要 / Abstract</summary>

  Access control is a cornerstone of secure computing, yet large language models often blur role boundaries by producing unrestricted responses. We study role-conditioned refusals, focusing on the LLM&#x27;s ability to adhere to access control policies by answering when authorized and refusing when not. To evaluate this behavior, we created a novel dataset that extends the Spider and BIRD text-to-SQL datasets, both of which have been modified with realistic PostgreSQL role-based policies at the table and column levels. We compare three designs: (i) zero or few-shot prompting, (ii) a two-step generator-verifier pipeline that checks SQL against policy, and (iii) LoRA fine-tuned models that learn permission awareness directly. Across multiple model families, explicit verification (the two-step framework) improves refusal precision and lowers false permits. At the same time, fine-tuning achieves a stronger balance between safety and utility (i.e., when considering execution accuracy). Longer and more complex policies consistently reduce the reliability of all systems. We release RBAC-augmented datasets and code.

  匹配依据：MPC: secure computing

  </details>

- **Classification of Small-size Quantum Secret Sharing Schemes using Uniform States**
  2025-10-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.07753)
  Xuhong Liu, Shuai Shao

  <details><summary>摘要 / Abstract</summary>

  We study the connection between quantum secret sharing (QSS) schemes and $k$-uniform states of qubits beyond the equivalence between threshold QSS schemes and AME states. Specifically, we show that $3$-uniformity is a necessary but not sufficient condition for constructing a $3$-homogeneous QSS scheme using states of qubits. To the best of our knowledge, this is the first result connecting \emph{non-threshold} QSS schemes with $k$-uniform states. As an application of our result, we classify QSS schemes for up to 7 players and provide explicit characterizations of their existence. Our results offer new insights into the role of $k$-uniform states in the design of QSS schemes (not necessarily threshold) and provide a foundation for future classifications of QSS schemes with more complex structures.

  匹配依据：MPC: secret sharing

  </details>

- **Comparison of Fully Homomorphic Encryption and Garbled Circuit Techniques in Privacy-Preserving Machine Learning Inference**
  2025-10-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.07457)
  Kalyan Cheerla, Lotfi Ben Othmane, Kirill Morozov

  <details><summary>摘要 / Abstract</summary>

  Machine Learning (ML) is making its way into fields such as healthcare, finance, and Natural Language Processing (NLP), and concerns over data privacy and model confidentiality continue to grow. Privacy-preserving Machine Learning (PPML) addresses this challenge by enabling inference on private data without revealing sensitive inputs or proprietary models. Leveraging Secure Computation techniques from Cryptography, two widely studied approaches in this domain are Fully Homomorphic Encryption (FHE) and Garbled Circuits (GC). This work presents a comparative evaluation of FHE and GC for secure neural network inference. A two-layer neural network (NN) was implemented using the CKKS scheme from the Microsoft SEAL library (FHE) and the TinyGarble2.0 framework (GC) by IntelLabs. Both implementations are evaluated under the semi-honest threat model, measuring inference output error, round-trip time, peak memory usage, communication overhead, and communication rounds. Results reveal a trade-off: modular GC offers faster execution and lower memory consumption, while FHE supports non-interactive inference.

  匹配依据：MPC: garbled circuit, garbled circuits, secure computation

  </details>

- **The Role of Federated Learning in Improving Financial Security: A Survey**
  2025-10-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.14991)
  Cade Houston Kennedy, Amr Hilal, Morteza Momeni

  <details><summary>摘要 / Abstract</summary>

  With the growth of digital financial systems, robust security and privacy have become a concern for financial institutions. Even though traditional machine learning models have shown to be effective in fraud detections, they often compromise user data by requiring centralized access to sensitive information. In IoT-enabled financial endpoints such as ATMs and POS Systems that regularly produce sensitive data that is sent over the network. Federated Learning (FL) offers a privacy-preserving, decentralized model training across institutions without sharing raw data. FL enables cross-silo collaboration among banks while also using cross-device learning on IoT endpoints. This survey explores the role of FL in enhancing financial security and introduces a novel classification of its applications based on regulatory and compliance exposure levels ranging from low-exposure tasks such as collaborative portfolio optimization to high-exposure tasks like real-time fraud detection. Unlike prior surveys, this work reviews FL&#x27;s practical use within financial systems, discussing its regulatory compliance and recent successes in fraud prevention and blockchain-integrated frameworks. However, FL deployment in finance is not without challenges. Data heterogeneity, adversarial attacks, and regulatory compliance make implementation far from easy. This survey reviews current defense mechanisms and discusses future directions, including blockchain integration, differential privacy, secure multi-party computation, and quantum-secure frameworks. Ultimately, this work aims to be a resource for researchers exploring FL&#x27;s potential to advance secure, privacy-compliant financial systems.

  匹配依据：MPC: secure multi party computation

  </details>

- **N-Parties Private Structure and Parameter Learning for Sum-Product Networks**
  2025-10-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.05946)
  Xenia Heilmann, Ernst Althaus, Mattia Cerrato, Nick Johannes Peter Rassau, Mohammad Sadeq Dousti, Stefan Kramer

  <details><summary>摘要 / Abstract</summary>

  A sum-product network (SPN) is a graphical model that allows several types of probabilistic inference to be performed efficiently. In this paper, we propose a privacy-preserving protocol which tackles structure generation and parameter learning of SPNs. Additionally, we provide a protocol for private inference on SPNs, subsequent to training. To preserve the privacy of the participants, we derive our protocol based on secret sharing, which guarantees privacy in the honest-but-curious setting even when at most half of the parties cooperate to disclose the data. The protocol makes use of a forest of randomly generated SPNs, which is trained and weighted privately and can then be used for private inference on data points. Our experiments indicate that preserving the privacy of all participants does not decrease log-likelihood performance on both homogeneously and heterogeneously partitioned data. We furthermore show that our protocol&#x27;s performance is comparable to current state-of-the-art SPN learners in homogeneously partitioned data settings. In terms of runtime and memory usage, we demonstrate that our implementation scales well when increasing the number of parties, comparing favorably to protocols for neural networks, when they are trained to reproduce the input-output behavior of SPNs.

  匹配依据：MPC: secret sharing

  </details>

- **BATTLE for Bitcoin: Capital-Efficient Optimistic Bridges with Large Committees**
  2025-10-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.06468)
  Sergio Demian Lerner, Ariel Futoransky

  <details><summary>摘要 / Abstract</summary>

  We present BATTLE for Bitcoin, a DoS-resilient dispute layer that secures optimistic bridges between Bitcoin and rollups or sidechains. Our design adapts the BATTLE tournament protocol to Bitcoin&#x27;s UTXO model using BitVM-style FLEX components and garbled circuits with on-demand L1 security bonds. Disputes are resolved in logarithmic rounds while recycling rewards, keeping the honest asserter&#x27;s minimum initial capital constant even under many permissionless challengers. The construction is fully contestable (challengers can supply higher-work counter-proofs) and relies only on standard timelocks and pre-signed transaction DAGs, without new opcodes. For $N$ operators, the protocol requires $O(N^2)$ pre-signed transactions, signatures, and message exchanges, yet remains practical at $N\!\gtrsim\!10^3$, enabling high decentralization.

  匹配依据：MPC: garbled circuits

  </details>

- **On the Cryptographic Futility of Non-Collapsing Measurements**
  2025-10-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.05055)
  Alper Cakan, Dakshita Khurana, Tomoyuki Morimae, Yuki Shirakawa, Kabir Tomer, Takashi Yamakawa

  <details><summary>摘要 / Abstract</summary>

  We investigate quantum analogues of collision resistance and obtain separations between quantum ``one-way&#x27;&#x27; and ``collision-resistant&#x27;&#x27; primitives. 1. Our first result studies one-wayness versus collision-resistance defined over quantum circuits that output classical strings. We show that there is a classical oracle $\mathcal{O}$ relative to which (sub-exponentially secure) indistinguishability obfuscation and one-way permutations exist even against adversaries that make quantum queries to a non-collapsing measurement oracle, $\mathcal{Q}^{\mathcal{O}}$. Very roughly, $\mathcal{Q}^{\mathcal{O}}$ outputs the result of multiple non-collapsing measurements on the output of any quantum $\mathcal{O}$-aided circuit. This rules out fully black-box {\em quantum} constructions of $Y$ from $X$ for any $X \in \{$indistinguishability obfuscation and one-way permutations, public-key encryption, deniable encryption, oblivious transfer, non-interactive ZK, trapdoor permutations, quantum money$\}, Y \in \{$collision-resistant hash functions, hard problems in SZK, homomorphic encryption, distributional collision-resistant puzzles$\}$. 2. Our second result studies one-wayness versus collision-resistance defined over quantum states. Here, we show that relative to the same classical oracle $\mathcal{O}$, (sub-exponentially secure) indistinguishability obfuscation and one-way permutations exist even against adversaries that make quantum queries to a {\em cloning unitary} $\mathsf{QCol}^\mathcal{O}$. Very roughly, this latter oracle implements a well-defined, linear operation to clone a subset of the qubits output by any quantum $\mathcal{O}$-aided circuit. This rules out fully black-box constructions of quantum lightning from public-key quantum money.

  匹配依据：MPC: oblivious transfer

  </details>

- **Multi-Agent Distributed Optimization With Feasible Set Privacy**
  2025-10-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.05068)
  Shreya Meel, Sennur Ulukus

  <details><summary>摘要 / Abstract</summary>

  We consider the problem of decentralized constrained optimization with multiple agents $E_1,\ldots,E_N$ who jointly wish to learn the optimal solution set while keeping their feasible sets $\mathcal{P}_1,\ldots,\mathcal{P}_N$ private from each other. We assume that the objective function $f$ is known to all agents and each feasible set is a collection of points from a universal alphabet $\mathcal{P}_{alph}$. A designated agent (leader) starts the communication with the remaining (non-leader) agents, and is the first to retrieve the solution set. The leader searches for the solution by sending queries to and receiving answers from the non-leaders, such that the information on the individual feasible sets revealed to the leader should be no more than nominal, i.e., what is revealed from learning the solution set alone. We develop achievable schemes for obtaining the solution set at nominal information leakage, and characterize their communication costs under two communication setups between agents. In this work, we focus on two kinds of network setups: i) ring, where each agent communicates with two adjacent agents, and ii) star, where only the leader communicates with the remaining agents. We show that, if the leader first learns the joint feasible set through an existing private set intersection (PSI) protocol and then deduces the solution set, the information leaked to the leader is greater than nominal. Moreover, we draw connection of our schemes to threshold PSI (ThPSI), which is a PSI-variant where the intersection is revealed only when its cardinality is larger than a threshold value. Finally, for various realizations of $f$ mapped uniformly at random to a fixed range of values, our schemes are more communication-efficient with a high probability compared to retrieving the entire feasible set through PSI.

  匹配依据：MPC: private set intersection

  </details>

- **HE-based On-the-Fly MPC, Revisited: Universal Composability, Approximate and Imperfect Computation, Circuit Privacy**
  2025-10-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1845)
  Ganyuan Cao, Sylvain Chatel, Christian Knabenhans

  <details><summary>摘要 / Abstract</summary>

  On-the-fly multi-party computation (OtF-MPC, López-Alt, Tromer, and Vaikuntanathan, STOC 2012) allows clients to join a computation dynamically without remaining online, while outsourcing the computation to an untrusted but powerful server. Existing OtF-MPC constructions rely on composing multi-party homomorphic encryption with zero-knowledge or succinct arguments. While both components have seen substantial efficiency and expressivity improvements in recent years, the security of their composition has not been revisited under these modern refinements. In this work, we revisit OtF-MPC through the lens of composable security. We extend the original analysis to systematically capture recent advances in these two building blocks, and to reason about their secure composition. We focus on multi-group homomorphic encryption (MGHE), a unifying abstraction that generalizes threshold and multi-key HE, and emerges as the natural backbone for OtF-MPC. Our contributions are fourfold. (1) We introduce the first Universal Composability (UC) ideal functionality for MGHE, jointly modeling client and server privacy, approximate or imperfect computation, and threshold security. (2) We define fine-grained security notions for MGHE and show that they are sufficient to realize this functionality against semi-malicious adversaries. (3) We revisit generic compilers that combine MGHE with any-simulation-extractable zkSNARKs, and prove that they realize OtF-MPC against fully malicious adversaries. (4) We introduce a split-witness ideal functionality for NIZKs, which separates the witness component that must be supplied by the ideal adversary from an existential component that only needs to be certified. We show that a Naor--Yung-style composition of MGHE and split-witness NIZKs realizes OtF-MPC while avoiding full extraction from the NIZK

  匹配依据：MPC: multi party computation

  </details>

- **Authenticated Garbling with Tensor Gates**
  2025-10-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1831)
  Nakul Khambhati, Turan Vural, David Heath, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  Authenticated garbling (Wang et al., CCS&#x27;17) is the leading framework for achieving constant-round maliciously secure 2PC, achieving total communication comparable to protocols in the semi-honest setting. In the semi-honest setting, the one-hot garbling scheme of Heath and Kolesnikov (CCS&#x27;21) supports tensor gates $\vec x \otimes \vec y$, for $\vec x \in \{0,1\}^n$ and $\vec y \in \{0,1\}^m$, in $O(n+m)\kappa$ bits, versus $O(nm)\kappa$ for an AND-gate-based garbling. Extending this improvement to the malicious setting has remained open. We present two authenticated garbling protocols that efficiently handle tensor gates. Our first protocol minimizes garbled circuit size, matching the size of semi-honest one-hot garbling; all additional overhead is confined to preprocessing. We also design a custom preprocessing protocol for efficiently generating random authenticated tensor triples, proved secure assuming only a circular correlation robust hash function and base OTs. Our second protocol minimizes total communication via compressed (PCG-style) preprocessing. We construct an authenticated variant of one-hot garbling where the additional overhead in garbled-circuit size as compared to the semi-honest garbling scales with tensor-gate input length rather than output length. As in the semi-honest case, tensor gates are restricted to inputs of length $O(\log \kappa)$ and arbitrary-length tensor products are handled by tiling multiple short input gates. This yields an $O(\log \kappa)$ factor reduction in communication for general tensor products compared to previous state-of-the-art authenticated garbling protocols, with concrete improvements in communication and runtime for practical workloads such as integer and matrix multiplication within an authenticated garbled circuit.

  匹配依据：MPC: garbled circuit, garbling protocols, garbling scheme

  </details>

- **Ajax: Fast Threshold Fully Homomorphic Encryption without Noise Flooding**
  2025-10-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1834)
  Zhenkai Hu, Haofei Liang, Xiao Wang, Xiang Xie, Kang Yang, Yu Yu, Wenhao Zhang

  <details><summary>摘要 / Abstract</summary>

  Threshold fully homomorphic encryption (ThFHE) enables multiple parties to perform arbitrary computation over encrypted data, while the secret key is distributed across the parties. The main task of designing ThFHE is to construct threshold key-generation and decryption protocols for FHE schemes. Among existing FHE schemes, FHEW-like cryptosystems enjoy the advantage of fast bootstrapping and small parameters. However, known ThFHE solutions use the ``noise-flooding&#x27;&#x27; technique to realize threshold decryption, which requires either large parameters or switching to a scheme with large parameters via bootstrapping, leading to a slow decryption process. Besides, for key generation, existing ThFHE schemes either assume a generic MPC or a trusted setup, or incur noise growth that is linear in the number $n$ of parties. In this paper, we propose a fast ThFHE scheme Ajax, by designing threshold key-generation and decryption protocols for FHEW-like cryptosystems. In particular, for threshold decryption, we eliminate the need for noise flooding, and instead present a new technique called ``mask-then-open&#x27;&#x27; based on random double sharings over different rings, while keeping the advantage of small parameters. For threshold key generation, we show a simple approach to reduce the noise growth from $n$ times to $max(0.038n,2)$ times in the honest-majority setting, where at most $t=\floor{(n-1)/2}$ parties are corrupted. Our end-to-end implementation reports the running time 17.6 $s$ and 0.9 $ms$ (resp., 91.9 $s$ and 4.4 $ms$) of generating a set of keys and decrypting a single ciphertext respectively, for $n=3$ (resp., $n=21$) parties under the network of 1 Gbps bandwidth and 1 $ms$ ping time. Compared to the state-of-the-art implementation, our protocol improves the end-to-end performance of the threshold decryption protocol by a factor of at least $5.7\times$ $\sim$ $283.6\times$ across different network latencies from $t=1$ to $t=13$. Our approaches can also be applied in other types of FHE schemes like BGV, BFV, and CKKS.

  匹配依据：MPC: mpc (context)

  </details>

- **Two-party ECDSA Signing at Constant Communication Overhead**
  2025-10-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1813)
  Yashvanth Kondi

  <details><summary>摘要 / Abstract</summary>

  In this work, we investigate whether the cost of two-party ECDSA signing can be brought within the realm of plain ECDSA signing. We answer the question in the affirmative for the case of communication complexity, by means of a new signing protocol. Our protocol consumes bandwidth linear in the security parameter, and hence the size of an ECDSA signature. Our scheme makes only blackbox use of generic tools---Oblivious Transfer during key generation, and any Pseudorandom Function when signing. While computation complexity is not asymptotically optimal, benchmarks of our protocol confirm that concrete costs are the lowest known for ECDSA signing. Our protocol is therefore the most concretely efficient in the literature on all fronts: bandwidth, computation, and rounds. On a technical level, our protocol is enabled by a novel Pseudorandom Correlation Function (PCF) for the Vector Oblivious Linear Evaluation correlation over a large ring. The PCF relies on one-way functions alone, and may be of independent interest. Our scheme supports standard extensions, such as pre-signing, and including backup servers for key shares in a $(2,n)$ configuration.

  匹配依据：MPC: oblivious transfer

  </details>

- **Simulation-based Security Notion of Correlation Robust Hashing with Applications to MPC**
  2025-10-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1818)
  Hongrui Cui, Chun Guo, Xiaojie Guo, Xiao Wang, Kang Yang, Yu Yu

  <details><summary>摘要 / Abstract</summary>

  This work studies the security and constructions of correlation robust (CR) hash functions in secure multi-party computation (MPC). Existing definitions of CR hashing are all game-based (i.e., no simulator to achieve programmability or extractability), but MPC protocols are proven secure in the simulation-based models including both stand-alone and universal composability models. We found that for some MPC protocols, e.g., TinyOT-like authenticated-triple generation protocols and correlated oblivious transfer (COT) extension protocols, such a mismatch could lead to a gap in security proofs, even for the semi-honest adversary and stand-alone model. To bridge the gap, we introduce a simulation-based security notion for CR hash functions to allow secure composition. Instead of building from scratch, we introduce such a simulator to a wide class of existing ideal-cipher-based CR hashing constructions, and derive the security bound from their original game-based CR security. This enables us to obtain an efficient CR hashing construction making just one call to a blockcipher, and is much more efficient than the construction from a random oracle used in previous TinyOT-like protocols. We showcase the utility of the new CR notion in easing security proofs and mitigating the risk of errors on two classes of protocols: (1) authenticated-triple generation protocols in the TinyOT family with a countermeasure; (2) COT extension protocols with bootstrapped iterations.

  匹配依据：MPC: oblivious transfer, secure multi party computation

  </details>

- **Pool: A Practical OT-based OPRF from Learning with Rounding**
  2025-10-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1816)
  Alex Davidson, Amit Deo, Louis Tremblay Thibault

  <details><summary>摘要 / Abstract</summary>

  We propose Pool: a conceptually simple post-quantum (PQ) oblivious pseudorandom function (OPRF) protocol, that is round-optimal (with input-independent preprocessing), practically efficient, and has security based on the well-understood hardness of the learning with rounding (LWR) problem. Specifically, our design permits oblivious computation of the LWR-based pseudorandom function $F_{\mathsf{sk}}(x) = \lceil H(x)^{\top} \cdot \mathsf{sk} \rfloor_{q,p}$, for random oracle $H: \{0,1\}^* \mapsto \mathbb{Z}_q^n$ and uniformly chosen $\mathsf{sk} \in \{0,1\}^n$. For 128-bits of semi-honest security, the Pool OPRF has an online communication cost of 11.9~kB, and a computational runtime of less than 2~ms on a single thread (via an open-source software implementation). This is more efficient (in either online communication cost or runtime) than constructions from well-known PQ PRFs, and is competitive even with constructions that only conjecture PQ security on lesser-known assumptions. As a result, our design gives high-performance, post-quantum variants of established OPRF applications in multi-party computation and private set operation protocols.

  匹配依据：MPC: multi party computation

  </details>

- **Extending Mental Poker**
  2025-10-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1821)
  Donald Beaver

  <details><summary>摘要 / Abstract</summary>

  Mental Poker enables two players to play card games at a distance without having a physical deck of cards at hand, as long as they have reliable trapdoor permutations or access to Oblivious Transfer (OT). OT itself can be stored and extended using just a one-way function. We examine whether Mental Poker can be extended from initial hands of ordinary physical poker. On the theoretical side, this work establishes OT amplification/extraction as a cryptographic primitive using asymmetrically-viewed fully-randomizing permutations. On the pragmatic, it is naturally related to ``card cryptography&#x27;&#x27; although in a very restricted sense: 52-card deck protocols using fully scrambling shuffles. While secret-key exchange protocols make strong use of full shuffles, full shuffles are avoided in 2PC/AND/Solitaire card settings because of detrimental over-randomization. Within those domains, this work explains decades-old impossibility conjectures in certain circumstances. More positively, we provide several practical and information-theoretically secure ways to establish base OTs from 5-Card Draw over ordinary decks at rates sufficient to establish a foothold for indefinite Mental Poker extension in just an afternoon of play.

  匹配依据：MPC: oblivious transfer

  </details>

- **Efficient Multiparty Private Simultaneous Messages for Symmetric Functions**
  2025-10-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1815)
  Reo Eriguchi, Kazumasa Shinagawa

  <details><summary>摘要 / Abstract</summary>

  A Private Simultaneous Messages (PSM) protocol is a secure multiparty computation protocol with a minimal interaction pattern, which allows input parties sharing common randomness to securely reveal the output of a function by sending messages only once to an external party. Since existing PSM protocols for arbitrary functions have exponentially large communication complexity in the number $n$ of parties, it is important to explore efficient protocols by focusing on special functions of practical use. In this paper, we study the communication efficiency of PSM protocols for symmetric functions, which provide many useful functionalities for real-world applications. We present a new $n$-party PSM protocol for symmetric functions with communication complexity $n^{2d/3+O(1)}$, where $d$ is the size of the input domain of each party. Our protocol improves the currently best known communication complexity of $n^{d+O(1)}$. As applications to other related models, we show that our novel protocol implies improved communication complexity of ad-hoc PSM, where only a subset of parties actually send messages, and also leads to a more communication-efficient robust PSM protocol, which is secure against collusion of the external party and input parties. The extension to ad-hoc PSM is not a straightforward application of the previous transformation but includes an optimization technique based on the symmetry of functions.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Cheat-Penalised Quantum Weak Coin-Flipping**
  2025-10-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.03218)
  Atul Singh Arora, Carl A. Miller, Mauro E. S. Morales, Jamie Sikora

  <details><summary>摘要 / Abstract</summary>

  Coin-flipping is a fundamental task in two-party cryptography where two remote mistrustful parties wish to generate a shared uniformly random bit. While quantum protocols promising near-perfect security exist for weak coin-flipping -- when the parties want opposing outcomes -- it has been shown that they must be inefficient in terms of their round complexity, and it is an open question of how space efficient they can be. In this work, we consider a variant called cheat-penalised weak coin-flipping in which if a party gets caught cheating, they lose $Λ$ points (compared to $0$ in the standard definition). We find that already for a small cheating penalty, the landscape of coin-flipping changes dramatically. For example, with $Λ=0.01$, we exhibit a protocol where neither Alice nor Bob can bias the result in their favour beyond $1/2 + 10^{-8}$, which uses $24$ qubits and $10^{16}$ rounds of communication (provably $10^{7}$ times better than any weak coin-flipping protocol with matching security). For the same space requirements, we demonstrate how one can choose between lowering how much a malicious party can bias the result (down to $1/2 + 10^{-10}$) and reducing the rounds of communication (down to $25,180$), depending on what is preferred. To find these protocols, we make two technical contributions. First, we extend the point game-protocol correspondence introduced by Kitaev and Mochon, to incorporate: (i) approximate point games, (ii) the cheat-penalised setting, and (iii) round and space complexity. Second, we give the first (to the best of our knowledge) numerical algorithm for constructing (approximate) point games that correspond to high security and low complexity. Our results open up the possibility of having secure and practical quantum protocols for multiparty computation.

  匹配依据：MPC: multiparty computation

  </details>

- **Block-Accumulate Codes: Accelerated Linear Codes for PCGs and ZK**
  2025-10-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1828)
  Vladimir Kolesnikov, Stanislav Peceny, Rahul Rachuri, Srinivasan Raghuraman, Peter Rindal, Harshal Shah

  <details><summary>摘要 / Abstract</summary>

  Linear error-correcting codes with fast encoding and high minimum distance are a central primitive across modern cryptography. They appear prominently in at least two domains: (1) pseudorandom correlation generators (PCGs), which enable sublinear-communication generation of correlations such as oblivious transfer and vector oblivious linear evaluation, and (2) zero-knowledge proof systems, where linear-time encoders underpin proof soundness and scalability. In both settings, the prover or sender must multiply by a large generator matrix $\mathbf{G}$, often with dimensions in the millions, making computational efficiency the dominant bottleneck. We propose a generalized paradigm for building crypto-friendly binary codes with provable minimum distance. Roughly speaking, these codes are based on randomized turbo codes such as repeat-accumulate codes. We prove linear asymptotic minimum distance and compute the exact expected weight spectrum for concrete sizes. We observe that our codes approach the Gilbert-Varshamov distance bound and outperform prior constructions. We construct several novel codes, the most promising of which we call Block-Accumulate codes. Among codes with provable distance, our code is $8\times$ faster than the state of the art on a CPU and $50\times$ faster on a GPU; even against aggressive parameters with conjectured distance, it is $3\times$ and $20\times$ faster, respectively. Under these parameters, this yields overall PCG speedups of $2.5\times$ on the CPU and $15\times$ on the GPU, achieving a projected 200$+$ million OTs per second, or about 100 million binary Beaver triples per second, on the GPU (excluding the one-time 10 ms GGM seed expansion). We also observe a $2\times$ encoding speedup and half the peak memory consumption in the Blaze zero-knowledge (PCS) scheme of Brehm et al. (EUROCRYPT~&#x27;25).

  匹配依据：MPC: oblivious transfer

  </details>

- **Blind ECDSA from the ECDSA Assumption**
  2025-10-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1827)
  Jules Maire, Alan Pulval-Dady

  <details><summary>摘要 / Abstract</summary>

  Blind signatures have become a cornerstone for privacy-sensitive applications such as digital cash, anonymous credentials, and electronic voting. The elliptic curve variant of the Digital Signature Algorithm (ECDSA) is widely adopted due to its efficiency in resource-constrained environments, such as mobile devices and blockchain systems. Building blind ECDSA is hence a natural goal. One presents the first such construction relying solely on the ECDSA assumption. Despite the inherent complexities in integrating blindness with ECDSA, we design a protocol that ensures both unforgeability and blindness without introducing new computational assumptions and ensuring concurrent security. It involves zero-knowledge proofs based on the MPC-in-the-head paradigm for complex statements combining relations on encrypted elliptic curve points, their coordinates, and discrete logarithms.

  匹配依据：MPC: mpc (context)

  </details>

- **HERDS: : Multi-Key Fully Homomorphic Encryption with Sublinear Bootstrapping**
  2025-10-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1804)
  Binwu Xiang, Seonhong Min, Intak Hwang, Zhiwei Wang, Haoqi He, Yuanju Wei, Kang Yang, Jiang Zhang, Yi Deng, Yu Yu

  <details><summary>摘要 / Abstract</summary>

  Multi-key fully homomorphic encryption (MK-FHE) enables secure computation over ciphertexts under different keys, but its practicality is hindered by inefficient bootstrapping. In this work, we propose \ours, a new MK-FHE scheme with highly efficient bootstrapping. Our bootstrapping framework improves upon the best-known complexity, reducing it from ${O}(dkn)$ to ${O}(kn)$, and further to ${O}(\sqrt{kn})$ under parallelization, where $d$ is the gadget length (typically scaling with the number of parties $k$) and $n$ is the LWE dimension. The framework consists of two main components: (i) a ciphertext conversion algorithm that transforms a multi-key LWE ciphertext into $k$ vectorized RLWE ciphertexts via $k$ optimized blind rotations and $dk$ key-switching operations, and (ii) a hybrid accumulator that aggregates these into a single multi-key RLWE ciphertext. We implemented HERDS on both CPU and GPU platforms to demonstrate its practicality. For $k=16$, we achieve $3.3\times$ and $7.2\times$ improvements on CPU, compared to the state-of-the-art schemes by Kwak et al. (PKC 2024) and by Xiang et al. (ASIACRYPT 2024), respectively. We further achieve a $195\times$ GPU acceleration, compared to our CPU runtime. As a byproduct, we design a new distributed-decryption protocol, which allows us to obtain a ciphertext with a small noise bound, and thus does not blow up the parameters.

  匹配依据：MPC: secure computation

  </details>

- **BitGC Made (More) Efficient**
  2025-10-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1810)
  Wenhao Zhang, Hanlin Liu, Kang Yang, Wen-jie Lu, Yu Yu, Xiao Wang, Chenkai Weng

  <details><summary>摘要 / Abstract</summary>

  Garbled circuits with one-bit-per-gate communication were recently introduced by Liu et al. (BitGC, Eurocrypt 2025), Meyer et al. (Crypto 2025), and Ishai et al. (Crypto 2025). However, these works focus primarily on the theoretical communication complexity, leaving open questions about practical computational efficiency. In this paper, we present a set of optimizations that substantially improve its practical efficiency. First, we eliminate key barriers to enable SIMD support for BitGC, leading to a substantial speedup in its homomorphic operations. Second, we demonstrate that XOR gates can be garbled without any communication, improving both efficiency and simplicity. Finally, we present a computationally efficient garbling scheme that requires zero communication for XOR gates and only 5 bits per AND gate. When applied to an AES-128 circuit, our fastest garbling scheme generates a garbled circuit of just 4 KB in 2 minutes on a single CPU core.

  匹配依据：MPC: garbled circuit, garbled circuits, garbling scheme

  </details>

- **Going Faster: Privacy-Preserving Shortest paths from Start to End (Extended Version)**
  2025-10-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1794)
  Vincent Ehrmanntraut, Ulrike Meyer

  <details><summary>摘要 / Abstract</summary>

  Finding shortest paths in graphs is a fundamental combinatorial optimization problem with numerous applications, e.g., in graph centrality measures, computational biology, and business process analysis. To address privacy constraints in such applications, Secure Multi-Party Computation (SMPC) protocols can compute the lengths of shortest paths on secret-shared graphs. Many such protocols have been proposed in the past, but they only compute the lengths of the shortest paths and not the paths themselves. In this paper, we close this gap by proposing two SMPC protocols that output secret-shared shortest paths. The first composes sub-protocols to calculate predecessors, to follow them, and to reorder wrongly positioned padding. Our second protocol optimizes the predecessor-following by decomposing it into sub-functionalities and proposing new sub-protocols for each. Further, the padding-reorder is replaced by a graph transformation. We evaluate our protocols across multiple network and security settings. Our optimized predecessor-following is up to 23 times faster than prior art, and our graph transformation is orders of magnitude faster than the padding-reorder. Overall, our second protocol is 5% to 49% faster than the first protocol due to the predecessor-calculation dominating the runtime on large graphs. Finally, we introduce a novel demultiplex protocol that, in fast networks, outperforms prior protocols on vector sizes up to 500, and on all evaluated vector sizes in slow networks. Due to the ubiquity of demultiplexes, this protocol is of independent interest.

  匹配依据：MPC: secure multi party computation

  </details>

- **A Monoid Ring Approach to Color Visual Cryptography**
  2025-10-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.00763)
  Maximilian Reif, Jens Zumbrägel

  <details><summary>摘要 / Abstract</summary>

  A visual cryptography scheme is a secret sharing scheme in which the secret information is an image and the shares are printed on transparencies, so that the secret image can be recovered by simply stacking the shares on top of each other. Such schemes do therefore not require any knowledge of cryptography tools to recover the secret, and they have widespread applications, for example, when sharing QR codes or medical images. In this work we deal with visual cryptography threshold schemes for color images. Our color model differs from most previous work by allowing arbitrary colors to be stacked, resulting in a possibly different color. This more general color monoid model enables us to achieve shorter pixel expansion and higher contrast than comparable schemes. We revisit the polynomial framework of Koga and Ishihara for constructing visual cryptography schemes and apply the monoid ring to obtain new schemes for color visual cryptography.

  匹配依据：MPC: secret sharing

  </details>

- **Two-Dimensional XOR-Based Secret Sharing for Layered Multipath Communication**
  2025-09-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.25113)
  Wai Ming Chan, Remi Chou, Taejoon Kim

  <details><summary>摘要 / Abstract</summary>

  This paper introduces the first two-dimensional XOR-based secret sharing scheme for layered multipath communication networks. We present a construction that guarantees successful message recovery and perfect privacy when an adversary observes and disrupts any single path at each transmission layer. The scheme achieves information-theoretic security using only bitwise XOR operations with linear $O(|S|)$ complexity, where $|S|$ is the message length. We provide mathematical proofs demonstrating that the scheme maintains unconditional security regardless of computational resources available to adversaries. Unlike encryption-based approaches vulnerable to quantum computing advances, our construction offers provable security suitable for resource-constrained military environments where computational assumptions may fail.

  匹配依据：MPC: secret sharing

  </details>

- **PRIVMARK: Private Large Language Models Watermarking with MPC**
  2025-09-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.24624)
  Thomas Fargues, Ye Dong, Tianwei Zhang, Jin-Song Dong

  <details><summary>摘要 / Abstract</summary>

  The rapid growth of Large Language Models (LLMs) has highlighted the pressing need for reliable mechanisms to verify content ownership and ensure traceability. Watermarking offers a promising path forward, but it remains limited by privacy concerns in sensitive scenarios, as traditional approaches often require direct access to a model&#x27;s parameters or its training data. In this work, we propose a secure multi-party computation (MPC)-based private LLMs watermarking framework, PRIVMARK, to address the concerns. Concretely, we investigate PostMark (EMNLP&#x27;2024), one of the state-of-the-art LLMs Watermarking methods, and formulate its basic operations. Then, we construct efficient protocols for these operations using the MPC primitives in a black-box manner. In this way, PRIVMARK enables multiple parties to collaboratively watermark an LLM&#x27;s output without exposing the model&#x27;s weights to any single computing party. We implement PRIVMARK using SecretFlow-SPU (USENIX ATC&#x27;2023) and evaluate its performance using the ABY3 (CCS&#x27;2018) backend. The experimental results show that PRIVMARK achieves semantically identical results compared to the plaintext baseline without MPC and is resistant against paraphrasing and removing attacks with reasonable efficiency.

  匹配依据：MPC: secure multi party computation

  </details>

- **Optimizing Privacy-Preserving Primitives to Support LLM-Scale Applications**
  2025-09-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.25072)
  Yaman Jandali, Ruisi Zhang, Nojan Sheybani, Farinaz Koushanfar

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving technologies have introduced a paradigm shift that allows for realizable secure computing in real-world systems. The significant barrier to the practical adoption of these primitives is the computational and communication overhead that is incurred when applied at scale. In this paper, we present an overview of our efforts to bridge the gap between this overhead and practicality for privacy-preserving learning systems using multi-party computation (MPC), zero-knowledge proofs (ZKPs), and fully homomorphic encryption (FHE). Through meticulous hardware/software/algorithm co-design, we show progress towards enabling LLM-scale applications in privacy-preserving settings. We demonstrate the efficacy of our solutions in several contexts, including DNN IP ownership, ethical LLM usage enforcement, and transformer inference.

  匹配依据：MPC: multi party computation, secure computing

  </details>

- **Multi-Layer Secret Sharing for Cross-Layer Attack Defense in 5G Networks: a COTS UE Demonstration**
  2025-09-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.13824)
  Wai Ming Chan, Remi Chou, Taejoon Kim

  <details><summary>摘要 / Abstract</summary>

  This demo presents the first implementation of multi-layer secret sharing on commercial-off-the-shelf (COTS) 5G user equipment (UE), operating without infrastructure modifications or pre-shared keys. Our XOR-based approach distributes secret shares across network operators and distributed relays, ensuring perfect recovery and data confidentiality even if one network operator and one relay are simultaneously lost (e.g., under denial of service (DoS) or unanticipated attacks).

  匹配依据：MPC: secret sharing

  </details>

- **High-Throughput Universally Composable Threshold FHE Decryption**
  2025-09-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1781)
  Guy Zyskind, Doron Zarchy, Max Leibovich, Chris Peikert

  <details><summary>摘要 / Abstract</summary>

  Threshold Fully Homomorphic Encryption (FHE) enables arbitrary computation on encrypted data, while distributing the decryption capability across multiple parties. A primary application of interest is low-communication multi-party computation (MPC), which benefits from a fast and secure threshold FHE decryption protocol. Several works have addressed this problem, but all existing solutions rely on &quot;noise flooding&quot; for security. This incurs significant overhead and necessitates large parameters in practice, making it unsuitable for many real-world deployments. Some constructions have somewhat better efficiency, but at the cost of weaker, non-simulation-based security definitions, which limits their usability and composability. In this work, we propose a novel threshold FHE decryption protocol that avoids &quot;noise flooding&quot; altogether, and provides simulation-based security. Rather than masking the underlying ciphertext noise, our technique securely removes it via an efficient MPC rounding procedure. The cost of this MPC is mitigated by an offline/online design that preprocesses special gates for secure comparisons in the offline phase, and has low communication and computation in the online phase. This approach is of independent interest, and should also benefit other MPC protocols (e.g., secure machine learning) that make heavy use of non-linear comparison operations. We prove our protocol secure in the Universal Composability (UC) framework, and it can be generally instantiated for a variety of adversary models (e.g., security-with-abort against a dishonest majority, or guaranteed output delivery with honest majority). Compared to the state of the art, our protocol offers significant gains both in the adversary model (i.e., dishonest vs. honest majority) and practical performance: empirically, our online phase obtains approximately 20,000$\times$ better throughput, and up to a 37$\times$ improvement in latency.

  匹配依据：MPC: multi party computation

  </details>

- **Bootstrapping as a Morphism: An Arithmetic Geometry Approach to Asymptotically Faster Homomorphic Encryption**
  2025-09-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.02365)
  Dongfang Zhao

  <details><summary>摘要 / Abstract</summary>

  Fully Homomorphic Encryption (FHE) provides a powerful paradigm for secure computation, but its practical adoption is severely hindered by the prohibitive computational cost of its bootstrapping procedure. The complexity of all current bootstrapping methods is fundamentally tied to the multiplicative depth of the decryption circuit, denoted $L_{dec}$, making it the primary performance bottleneck. This paper introduces a new approach to bootstrapping that completely bypasses the traditional circuit evaluation model. We apply the tools of modern arithmetic geometry to reframe the bootstrapping operation as a direct geometric projection. Our framework models the space of ciphertexts as an affine scheme and rigorously defines the loci of decryptable and fresh ciphertexts as distinct closed subschemes. The bootstrapping transformation is then realized as a morphism between these two spaces. Computationally, this projection is equivalent to solving a specific Closest Vector Problem (CVP) instance on a highly structured ideal lattice, which we show can be done efficiently using a technique we call algebraic folding. The primary result of our work is a complete and provably correct bootstrapping algorithm with a computational complexity of $O(d \cdot \text{poly}(\log q))$, where $d$ is the ring dimension and $q$ is the ciphertext modulus. The significance of this result lies in the complete elimination of the factor $L_{dec}$ from the complexity, representing a fundamental asymptotic improvement over the state of the art. This geometric perspective offers a new and promising pathway toward achieving truly practical and high-performance FHE.

  匹配依据：MPC: secure computation

  </details>

- **Untelegraphable Encryption and its Applications**
  2025-09-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.24189) · [IACR ePrint](https://eprint.iacr.org/2025/1765)
  Jeffrey Champion, Fuyuki Kitagawa, Ryo Nishimaki, Takashi Yamakawa

  <details><summary>摘要 / Abstract</summary>

  We initiate the study of untelegraphable encryption (UTE), founded on the no-telegraphing principle, which allows an encryptor to encrypt a message such that a binary string representation of the ciphertext cannot be decrypted by a user with the secret key, a task that is classically impossible. This is a natural relaxation of unclonable encryption (UE), inspired by the recent work of Nehoran and Zhandry (ITCS 2024), who showed a computational separation between the no-cloning and no-telegraphing principles. In this work, we define and construct UTE information-theoretically in the plain model. Building off this, we give several applications of UTE and study the interplay of UTE with UE and well-studied tasks in quantum state learning, yielding the following contributions: - A construction of collusion-resistant UTE from standard secret-key encryption (SKE). We additionally show that hyper-efficient shadow tomography (HEST) is impossible assuming collusion-resistant UTE exists. By considering a relaxation of collusion-resistant UTE, we are able to show the impossibility of HEST assuming only pseudorandom state generators (which may not imply one-way functions). This almost unconditionally answers an open inquiry of Aaronson (STOC 2018). - A construction of UTE from a quasi-polynomially secure one-shot message authentication code (OSMAC) in the classical oracle model, such that there is an explicit attack that breaks UE security for an unbounded polynomial number of decryptors. - A construction of everlasting secure collusion-resistant UTE, where the decryptor adversary can run in unbounded time, in the quantum random oracle model (QROM), and formal evidence that a construction in the plain model is a challenging task. We additionally show that HEST with unbounded post-processing time (which we call weakly-efficient shadow tomography) is impossible assuming everlasting secure collusion-resistant UTE exists. - A construction of secret sharing for all polynomial-size policies that is resilient to joint and unbounded classical leakage from collusion-resistant UTE and classical secret sharing for all policies. - A construction (and definition) of collusion-resistant untelegraphable secret-key functional encryption (UTSKFE) from single-decryptor functional encryption and plain secret-key functional encryption, and a construction of collusion-resistant untelegraphable public-key functional encryption from UTSKFE, plain SKE, and plain public-key functional encryption.

  匹配依据：MPC: secret sharing

  </details>

- **New Quantum Internet Applications via Verifiable One-Time Programs**
  2025-09-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.22290)
  Lev Stambler

  <details><summary>摘要 / Abstract</summary>

  We introduce Verifiable One-Time Programs (Ver-OTPs) and use them to construct single-round Open Secure Computation (OSC), a novel primitive enabling applications like (1) single-round sealed-bid auctions, (2) single-round and honest-majority atomic proposes -- a building block of consensus protocols, and (3) single-round differentially private statistical aggregation without pre-registration. First, we construct Ver-OTPs from single-qubit states and classical cryptographic primitives. Then, assuming a multi-key homomorphic scheme (MHE) with certain properties, we use Ver-OTPs with MHE to construct OSC. The underlying quantum requirement is minimal: only single-qubit states are needed alongside a hardware assumption on the receiver&#x27;s quantum resources. Our work therefore provides a new framework for quantum-assisted cryptography that may be implementable with near-term quantum technology.

  匹配依据：MPC: secure computation

  </details>

- **An Empirical Analysis of Secure Federated Learning for Autonomous Vehicle Applications**
  2025-09-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.20223)
  Md Jueal Mia, M. Hadi Amini

  <details><summary>摘要 / Abstract</summary>

  Federated Learning lends itself as a promising paradigm in enabling distributed learning for autonomous vehicles applications and ensuring data privacy while enhancing and refining predictive model performance through collaborative training on edge client vehicles. However, it remains vulnerable to various categories of cyber-attacks, necessitating more robust security measures to effectively mitigate potential threats. Poisoning attacks and inference attacks are commonly initiated within the federated learning environment to compromise secure system performance. Secure aggregation can limit the disclosure of sensitive information from outsider and insider attackers of the federated learning environment. In this study, our aim is to conduct an empirical analysis on the transportation image dataset (e.g., LISA traffic light) using various secure aggregation techniques and multiparty computation in the presence of diverse categories of cyber-attacks. Multiparty computation serves as a state-of-the-art security mechanism, offering standard privacy for secure aggregation of edge autonomous vehicles local model updates through various security protocols. The presence of adversaries can mislead the autonomous vehicle learning model, leading to the misclassification of traffic lights, and resulting in detrimental impacts. This empirical study explores the resilience of various secure federated learning aggregation techniques and multiparty computation in safeguarding autonomous vehicle applications against various cyber threats during both training and inference times.

  匹配依据：MPC: multiparty computation

  </details>

- **Breaking the Barrier for Asynchronous MPC with a Friend**
  2025-09-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1736)
  Banashri Karmakar, Aniket Kate, Shravani Patil, Arpita Patra, Sikhar Patranabis, Protik Paul, Divya Ravi

  <details><summary>摘要 / Abstract</summary>

  Multiparty computation (MPC) is a topic of growing interest for privacy-preserving computation tasks. A few MPC libraries have been developed, and newer protocols are regularly proposed to reduce the latency overhead, improve scalability, and achieve strong termination guarantees. However, most current MPC protocols are designed and implemented assuming network synchrony: in theory, they assume that all messages are delivered within a known time bound, while for experimental analysis, most assume all nodes to be honest, such that the time bounds are never deployed. While deploying MPC systems in the wild and trying to minimize the latency, network synchrony is indeed a strong assumption to make: natural adverse network conditions can break the safety and/or liveness of the protocol due to simply delayed messages. Asynchronous MPC (AMPC) protocols can overcome the challenge as they do not assume fixed time bounds for message delivery delays; however, AMPC faces a natural threshold barrier of 2/3rd honest majority and introduces significant computation and/or communication overheads. This work aims to achieve the best-of-both network models by designing a practical AMPC protocol that has stronger resilience guarantees matching those for synchronous MPC. We achieve this by adopting the emerging helper-aided model, and designing protocols that achieve fairness not only in the simple honest majority setting but also in the dishonest majority setting. Our protocols follow the standard preprocessing-online paradigm, enabling a lightweight and fast input-dependent online phase. In the honest majority setting, our protocol relies solely on lightweight cryptographic operations. In the dishonest majority setting, the protocol requires oblivious transfer (OT) during preprocessing, which we prove is necessary in this setting. We implement our constructions and provide a thorough performance comparison with state-of-the-art MPC protocols in the helper-aided model. Our experiments demonstrate that our protocols substantially outperform the state-of-the-art helper-aided MPC scheme, while being significantly more resilient to network delays.

  匹配依据：MPC: multiparty computation, oblivious transfer

  </details>

- **On the Impossibility of Actively Secure Distributed Samplers**
  2025-09-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1730)
  Damiano Abram, Serge Fehr, Maciej Obremski, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  One-round secure computation is generally believed impossible due to the residual function attack: any honest-but-curious participant can replay the protocol in their head changing their input, and learn, in this way, a new output. Inputless functionalities are among the few that are immune to this problem. This paper studies one-round, multi-party computation protocols (MPC) that implement the most natural inputless functionality: one that generates a random sample from a fixed distribution. These are called distributed samplers. At Eurocrypt 2022, Abram, Scholl and Yakoubov showed how to build this primitive in the semi-honest model with dishonest majority. In this work, we give a lower bound for constructing distributed samplers with a malicious adversary in the standard model. More in detail, we show that for any construction in the stand-alone model with black-box simulation, even with a CRS and honest majority, the output of the sampling protocol must have low entropy. This essentially implies that this type of construction is useless in applications. Our proof is based on an entropic argument, drawing a new connection between computationally secure MPC, information theory and learning theory.

  匹配依据：MPC: multi party computation, secure computation

  </details>

- **GuardianMPC: Backdoor-resilient Neural Network Computation**
  2025-09-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1729)
  Mohammad Hashemi, Domenic Forte, Fatemeh Ganji

  <details><summary>摘要 / Abstract</summary>

  The rapid growth of deep learning (DL) has raised serious concerns about users’ data and neural network (NN) models’ security and privacy, particularly the risk of backdoor insertion when outsourcing the training or employing pre-trained models. To ensure resilience against such backdoor attacks, this work presents GuardianMPC, a novel framework leveraging secure multiparty computation (MPC). GuardianMPC is built upon garbled circuits (GC) within the LEGO protocol framework to accelerate oblivious inference on FPGAs in the presence of malicious adversaries that can manipulate the model weights and/or insert a backdoor in the architecture of a pre-trained model. In this regard, GuardianMPC is the first to offer private function evaluation in the LEGO family. GuardianMPC also supports private training to effectively counter backdoor attacks targeting NN model architectures and parameters. With optimized pre-processing, GuardianMPC significantly accelerates the online phase, achieving up to x13.44 faster computation than its software counterparts. Our experimental results for multilayer perceptrons (MLPs) and convolutional neural networks (CNNs) assess GuardianMPC’s time complexity and scalability across diverse NN model architectures. Interestingly, GuardianMPC does not adversely affect the training accuracy, as opposed to many existing private training frameworks. These results confirm GuardianMPC as a high-performance, model-agnostic solution for secure NN computation with robust security and privacy guarantees.

  匹配依据：MPC: garbled circuits, secure multiparty computation

  </details>

- **From OT to OLE with Subquadratic Communication**
  2025-09-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1722)
  Jack Doerner, Iftach Haitner, Yuval Ishai, Nikolaos Makriyannis

  <details><summary>摘要 / Abstract</summary>

  Oblivious Linear Evaluation (OLE) is an algebraic generalization of oblivious transfer (OT) that forms a critical part of a growing number of applications. An OLE protocol over a modulus $q$ enables the receiver party to securely evaluate a line $a\cdot X+b$ chosen by the sender party on a secret point $x\in\mathbb{Z}_q$. Motivated by the big efficiency gap between OLE and OT and by fast OT extension techniques, we revisit the question of reducing OLE to OT, aiming to improve the communication cost of known reductions. We start by observing that the Chinese Remainder Theorem (CRT) can be combined with a prior protocol of Gilboa (Crypto ’99) to reduce its communication cost from $O(\ell^2)$ to $\tilde O(\ell)$ bits, for $\ell=\log q$. Unfortunately, whereas Gilboa&#x27;s protocol is secure against a semi-honest sender and a malicious receiver, a direct application of the CRT technique is only semi-honest secure (it is insecure against malicious receivers). Thus, we employ number-theoretic techniques to protect our CRT-based protocol against malicious receivers, while still retaining a concrete advantage over Gilboa&#x27;s protocol (e.g., $10.2\times$ less communication for $\ell=256$). Furthermore, we obtain a fully malicious OLE-to-OT reduction by applying either information-theoretic techniques with moderate overhead, or RSA-based cryptographic techniques with very low overhead. We demonstrate the usefulness of our results in the context of OLE applications, including a post-quantum oblivious pseudorandom function (OPRF) and distributed signatures. In particular, assuming pre-existing random OT correlations, we can use our malicious-receiver OLE protocol to realize (a single instance of) the power-residue based OPRF candidate with security against a malicious client and a semi-honest server using only 1.14 KB of communication, a $16\times$ improvement over the best previous protocol in this setting. Using our RSA-based fully malicious OLE protocol, we achieve a $5\times$ communication improvement over previous OT and EC-based distributed ECDSA protocols. Compared to other ECDSA protocols (including ones that use Paillier and class groups), the communication gains are more modest, but come at only a fraction of the computational cost as we avoid all expensive group operations.

  匹配依据：MPC: oblivious transfer

  </details>

- **Information-Theoretic Broadcast-Optimal MPC**
  2025-09-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1710)
  Michele Ciampi, Ivan Damgård, Divya Ravi, Luisa Siniscalchi, Sophia Yakoubov

  <details><summary>摘要 / Abstract</summary>

  Broadcast, though often used as a black box in cryptographic protocols, is expensive to realize in terms of rounds and communication complexity. We investigate the minimal use of broadcast in round-optimal information-theoretic MPC, with statistical security. For information-theoretic MPC with guaranteed output delivery, four rounds of communication are necessary and sufficient (Applebaum, Kachlon and Patra, FOCS 2020; Applebaum, Kachlon and Patra, STOC 2023). We show that broadcast is unavoidable in the second and third rounds of statistical MPC protocols. To complement our lower bounds, we modify the protocol of Applebaum, Kachlon and Patra (STOC 2023) to make use of broadcast only in the second and third round. Along the way, we show that the sharing phase of any three-round information-theoretic VSS protocol must also make use of broadcast in the second and third rounds.

  匹配依据：MPC: mpc (context)

  </details>

- **Is It Even Possible? On the Parallel Composition of Asynchronous MPC Protocols**
  2025-09-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1707)
  Ran Cohen, Pouyan Forghani, Juan Garay, Rutvik Patel, Vassilis Zikas

  <details><summary>摘要 / Abstract</summary>

  Despite several known idiosyncrasies separating the synchronous and the asynchronous models, asynchronous secure multi-party computation (MPC) protocols demonstrate high-level similarities to synchronous MPC, both in design philosophy and abstract structure. As such, a coveted, albeit elusive, desideratum is to devise automatic translators (e.g., protocol compilers) of feasibility and efficiency results from one model to the other. In this work, we demonstrate new challenges associated with this goal. Specifically, we study the case of parallel composition in the asynchronous setting. We provide formal definitions of this composition operation in the UC framework, which, somewhat surprisingly, have been missing from the literature. Using these definitions, we then turn to charting the feasibility landscape of asynchronous parallel composition. We first prove strong impossibility results for composition operators that do not assume knowledge of the functions and/or the protocols that are being composed. These results draw a grim feasibility picture, which is in sharp contrast with the synchronous model, and highlight the question: Is asynchronous parallel composition even a realistic goal? To answer the above (in the affirmative), we provide conditions on the composed protocols that enable a useful form of asynchronous parallel composition, as it turns out to be common in existing constructions.

  匹配依据：MPC: secure multi party computation

  </details>

- **Robust and Secure Computation Offloading and Trajectory Optimization for Multi-UAV MEC Against Aerial Eavesdropper**
  2025-09-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.14883)
  Can Cui, Ziye Jia, Jiahao You, Chao Dong, Qihui Wu, Han Zhu

  <details><summary>摘要 / Abstract</summary>

  The unmanned aerial vehicle (UAV) based multi-access edge computing (MEC) appears as a popular paradigm to reduce task processing latency. However, the secure offloading is an important issue when occurring aerial eavesdropping. Besides, the potential uncertainties in practical applications and flexible trajectory optimizations of UAVs pose formidable challenges for realizing robust offloading. In this paper, we consider the aerial secure MEC network including ground users, service unmanned aerial vehicles (S-UAVs) integrated with edge servers, and malicious UAVs overhearing transmission links. To deal with the task computation complexities, which are characterized as uncertainties, a robust problem is formulated with chance constraints. The energy cost is minimized by optimizing the connections, trajectories of S-UAVs and offloading ratios. Then, the proposed non-linear problem is tackled via the distributionally robust optimization and conditional value-at-risk mechanism, which is further transformed into the second order cone programming forms. Moreover, we decouple the reformulated problem and design the successive convex approximation for S-UAV trajectories. The global algorithm is designed to solve the sub-problems in a block coordinate decent manner. Finally, extensive simulations and numerical analyses are conducted to verify the robustness of the proposed algorithms, with just 2\% more energy cost compared with the ideal circumstance.

  匹配依据：MPC: secure computation

  </details>

- **Computationally-Sound Symbolic Cryptography in Lean**
  2025-09-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1700)
  Stefan Dziembowski, Grzegorz Fabiański, Daniele Micciancio, Rafał Stefański

  <details><summary>摘要 / Abstract</summary>

  We present a formally-verified (in Lean 4) framework for translating symbolic cryptographic proofs into the computationally-sound ones. Symbolic cryptography is a well-established field that allows reasoning about cryptographic protocols in an abstract way and is relatively easy to verify using proof assistants. Unfortunately, it often lacks a connection to the computational aspects of real-world cryptography. Computationally-sound cryptography, on the other hand, captures this connection much better, but it is often more complex, less accessible, and much harder to verify formally. Several works in the past have provided a bridge between the two, but, to our knowledge, none of them have been implemented in a proof assistant. We close this gap by formalizing the translation from symbolic to computationally-sound cryptography in Lean 4. Our framework is based on the work of Micciancio (Eurocrypt, 2010) and Li and Micciancio (CSF, 2018), which builds on the idea of using co-induction (instead of induction) for reasoning about an adversary&#x27;s knowledge in a symbolic setting. Our work encompasses (1) the formalization of the symbolic cryptography framework, (2) the formalization of the computationally sound cryptography framework, and (3) the formalization of the translation between the two. We also provide (4) an extended example of circuit garbling, which is a well-known cryptographic protocol frequently used in secure multi-party computation. We believe that our work will serve as a foundation for future research in the area of formal verification of cryptographic protocols, as it enables reasoning about cryptographic protocols more abstractly while still providing a formally verified connection to the computational aspects of real-world cryptography.

  匹配依据：MPC: secure multi party computation

  </details>

- **A Constant-Rate Compiler for MPC over Noisy Networks**
  2025-09-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1699)
  Ran Gelles, Carmit Hazay, Manuj Mukherjee, Jaspal Singh, Arun Yeragudipati, Vassilis Zikas

  <details><summary>摘要 / Abstract</summary>

  The study of efficient multi-party computation (MPC) has been a central focus of cryptographic research, leading to a broad range of techniques across diverse practical models. However, the vast majority of this work assumes reliable communication channels and largely ignores network-level noise, a fundamental characteristic of modern communication systems. In this work we study information-theoretic MPC over noisy networks in the multi-party setting. We construct an $n$-party MPC protocol that is secure against semi-honest adversaries corrupting a majority of the parties assuming all communication is carried over BSC channels with a fixed bit-flip probability. Our construction incurs only constant-factor communication overhead compared to the underlying MPC protocol over noiseless channels: specifically, it computes any circuit $C$ with communication complexity $O(n^2(|C|+\kappa))$, where $\kappa$ is a statistical security parameter. This substantially improves the naive approach, which can only guarantee super-linear communication, namely, $O(n^2|C|(\kappa+\log |C|))$. To achieve this result, we introduce a novel multi-party interactive coding scheme tailored to cryptographic protocols that rely on correlated randomness. We show that combining this coding scheme with the classical GMW protocol yields a noise-resilient MPC protocol that preserves its security guarantees while incurring only linear overhead. A central technical challenge we address is a subtle correctness issue that arises in the simulation of protocols with correlated randomness: without careful synchronization, different parties may use inconsistent correlated randomness for what is logically the same protocol step, causing the computation to fail even in the absence of noise. Our novel interactive coding scheme ensures that all parties use consistent correlated randomness in every simulated round of the MPC. Surprisingly, this issue also affects the two-party simulation over noisy channels [Gelles, Paskin-Cherniavsky, and Zikas, SCN’18], leaving an unaddressed gap in its analysis. Our techniques provide a way to resolve this gap.

  匹配依据：MPC: multi party computation

  </details>

- **Publicly Verifiable Private Information Retrieval Protocols Based on Function Secret Sharing**
  2025-09-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.13684)
  Lin Zhu, Lingwei Kong, Xin Ning, Xiaoyang Qu, Jianzong Wang

  <details><summary>摘要 / Abstract</summary>

  Private Information Retrieval (PIR) is a fundamental cryptographic primitive that enables users to retrieve data from a database without revealing which item is being accessed, thereby preserving query privacy. However, PIR protocols also face the challenge of result verifiability, as users expect the reconstructed data to be trustworthy and authentic. In this work, we propose two effective constructions of publicly verifiable PIR (PVPIR) in the multi-server setting, which achieve query privacy, correctness, and verifiability simultaneously. We further present three concrete instantiations based on these constructions. For the point query, our protocol introduces minimal computational overhead and achieves strong verifiability guarantees with significantly lower communication costs compared to existing Merkle tree-based approaches. For the predicate query, the communication complexity of our scheme remains stable as the database size increases, demonstrating strong scalability and suitability for large-scale private query applications.

  匹配依据：MPC: secret sharing

  </details>

- **Piquant$\\varepsilon$: Private Quantile Estimation in the Two-Server Model**
  2025-09-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.14035)
  Hannah Keller, Jacob Imola, Fabrizio Boninsegna, Rasmus Pagh, Amrita Roy Chowdhury

  <details><summary>摘要 / Abstract</summary>

  Quantiles are key in distributed analytics, but computing them over sensitive data risks privacy. Local differential privacy (LDP) offers strong protection but lower accuracy than central DP, which assumes a trusted aggregator. Secure multi-party computation (MPC) can bridge this gap, but generic MPC solutions face scalability challenges due to large domains, complex secure operations, and multi-round interactions. We present Piquant$\varepsilon$, a system for privacy-preserving estimation of multiple quantiles in a distributed setting without relying on a trusted server. Piquant$\varepsilon$ operates under the malicious threat model and achieves accuracy of the central DP model. Built on the two-server model, Piquant$\varepsilon$ uses a novel strategy of releasing carefully chosen intermediate statistics, reducing MPC complexity while preserving end-to-end DP. Empirically, Piquant$\varepsilon$ estimates 5 quantiles on 1 million records in under a minute with domain size $10^9$, achieving up to $10^4$-fold higher accuracy than LDP, and up to $\sim 10\times$ faster runtime compared to baselines.

  匹配依据：MPC: secure multi party computation

  </details>

- **Pilvi: Lattice Threshold PKE with Small Decryption Shares and Improved Security**
  2025-09-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1691)
  Valerio Cini, Russell W. F. Lai, Ivy K. Y. Woo

  <details><summary>摘要 / Abstract</summary>

  Threshold public-key encryption (tPKE) enables any subset of $t$ out of $K$ parties to decrypt non-interactively, while any ciphertext remains secure if less than $t$ decryption shares are known. Despite recent progress, existing lattice-based tPKEs face at least one of the following drawbacks: (1) having large decryption share size -- polynomial in $K$ and some even exponential in $t$, (2) proven secure only against relaxed security models where the adversary is not allowed to see decryption shares of challenge ciphertexts, and (3) lack of concrete efficiency, in particular due to the requirement of super-polynomial modulus for noise flooding. We present $\mathsf{Pilvi}$, a new thresholdised variant of Regev’s public-key encryption scheme, which achieves both small decryption shares and a strong form of simulation-based security under the Learning with Errors (LWE) assumption. Our construction has decryption share size $t \cdot \log K \cdot \mathsf{poly}(\lambda)$ and allows the use of a polynomial-size modulus assuming an a priori bound on the number of queries $Q$. It remains secure even when an adaptive adversary requests partial decryptions of both challenge and non-challenge ciphertexts, as long as for each ciphertext the number of corrupt parties plus the number of shares obtained is less than $t$. We provide concrete parameter suggestions for 128-bit security for a wide range of $(t,K,Q)$, including cases where $t \approx K/2$ for up to $K \leq 32$ users and $Q \leq 2^{60}$ partial decryption queries. The ciphertext size ranges from $14$ to $58$ KB and the partial decryption share size ranges from $1$ to $4$ KB. Along the way, we abstract out a general purpose tool called the threshold-LWE assumption, which we prove to follow from LWE. The threshold-LWE assumption captures the core steps in security proofs of schemes involving Shamir&#x27;s secret-sharing the LWE secret with carefully chosen evaluation points, the algebraic structures from the latter being what enabling the efficiency of our tPKE scheme. As an additional application, we also show how to construct distributed pseudorandom functions (dPRFs) from the threshold-LWE assumption.

  匹配依据：MPC: secret sharing

  </details>

- **Universal share based quantum multi secret image sharing scheme**
  2025-09-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.12979)
  Dipak K. Rabari, Yogesh K. Meghrajani, Laxmi S. Desai

  <details><summary>摘要 / Abstract</summary>

  Image security for information has become increasingly critical as internet become more prevalent due to hacking and unauthorized access. To ensure the security of confidential image data, image encryption using visual cryptography plays a crucial role. To share multiple images using visual cryptography, the company organizer utilizes the concept of a universal or common share. Likewise, quantum computing is an emerging technology that facilitates secure communication. The ability of quantum computers to solve certain mathematical problems efficiently threatens the security of many current encryption algorithms. Hence, to leverage the strengths of quantum computing and visual cryptography, this research introduces a novel universal share-based quantum multi-secret sharing technique for secure image communication. Quantum computing enables the scheme to exhibit high resilience to different eavesdropping threats. Consequently, the proposed method offers robust security solution for sharing confidential images across a range of applications, including enterprise data access and military communications.

  匹配依据：MPC: secret sharing

  </details>

- **Toss: Garbled PIR from Table-Only Stacking**
  2025-09-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1685)
  Lucien K. L. Ng, Vladimir Kolesnikov

  <details><summary>摘要 / Abstract</summary>

  Garbled Circuits (GC) are a foundational primitive for secure two-party computation (2PC). Garbled Private Information Retrieval (GPIR) is a GC technique for looking up a public array or database (DB) on a private index unknown to either party. GPIR immediately enables GC evaluation of functions implemented as a publicly known lookup table (LUT). However, GPIR is costly. It can be realized by a linear scan, by adapting Garbled RAM, by stacking GC branches implementing access to table elements, and, most recently, via the GC lookup table scheme logrow (Heath et al., Eurocrypt 2024). For an $N$-row DB lookup of $m$-bit rows, logrow has computation cost $\approx O(N m \kappa)$ and communication cost $O(m(\log N \cdot \kappa + N))$. This makes logrow practical only for tables up to about $2^{15}$ rows. We propose Toss, a new efficient GPIR protocol with dramatically reduced bandwidth consumption—an especially scarce resource in MPC—both asymptotically and concretely. Our communication cost is $O\!\left(\sqrt{N}\, m \sqrt{\kappa}\right)$ with a small constant, which is sublinear in both $N$ and the security parameter $\kappa$. Our computation cost is $O\!\left(N m \kappa + \bigl(\sqrt{N/\kappa}\, m + N\bigr) c_\kappa \right)$, where $c_\kappa$ is the cost of a hash evaluation. This computation cost is comparable to, or slightly lower than, that of logrow. In concrete terms, for a $2^{20}$-row LUT of 8-bit items, we achieve more than a $31\times$ reduction in communication compared to logrow. On a laptop over a 100 Mbps channel, throughput increases from approximately $10.6$ lookups/s to $81$ lookups/s, a $&gt;7.5\times$ improvement. On a 10 Mbps channel, Toss achieves more than $28\times$ better throughput. The improvement grows with $N$; for example, for $N=2^{25}$ and $m=32$, the gain exceeds $512\times$. Toss builds on stacked garbling (SGC) and logrow, incorporating multiple low-level optimizations and requiring a reworking of their internals and interfaces. We emphasize that constructing GPIR directly from SGC incurs logarithmic computational overhead, which decreases throughput in typical “laptop + LAN” testbeds. Our design avoids this pitfall. We implement Toss and report on its performance, demonstrating its substantial communication savings and practical efficiency.

  匹配依据：MPC: garbled circuits, secure two party computation

  </details>

- **SoK: Connecting the Dots in Privacy-Preserving ML - Systematization of MPC Protocols and Conversions Between Secret Sharing Schemes**
  2025-09-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1679)
  Martin Zbudila, Ajith Suresh, Hossein Yalame, Omid Mirzamohammadi, Aysajan Abidin, Bart Preneel

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving machine learning (PPML) has become increasingly important due to the need to protect sensitive data during training and inference. Secure multiparty computation (MPC) and homomorphic encryption (HE) have emerged as foundational technologies, enabling secure computation over private data. In this work, we provide a systematic comparative overview of MPC frameworks for PPML, focusing on protocols that introduce novel approaches rather than incremental improvements. Frameworks are analyzed based on computational and communication complexity, throughput, security guarantees, and applicability in small-party settings. Each underlying primitive in PPML is examined from an MPC perspective, highlighting its role and trade-offs. We also emphasize the diversity of secret-sharing schemes and associated interoperability challenges, proposing scheme conversions to facilitate efficient hybrid solutions. This Systematization of Knowledge guides researchers in identifying open problems and practitioners in selecting effective MPC-based frameworks for real-world PPML deployment.

  匹配依据：MPC: secret sharing, secure computation, secure multiparty computation

  </details>

- **EByFTVeS: Efficient Byzantine Fault Tolerant-based Verifiable Secret-sharing in Distributed Privacy-preserving Machine Learning**
  2025-09-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.12899)
  Zhen Li, Zijian Zhang, Wenjin Yang, Pengbo Wang, Zhaoqi Wang, Yan Wu, Xuyang Liu, Jing Sun

  <details><summary>摘要 / Abstract</summary>

  Verifiable Secret Sharing (VSS) has been widespread in Distributed Privacy-preserving Machine Learning (DPML), because invalid shares from malicious dealers or participants can be recognized by verifying the commitment of the received shares for honest participants. However, the consistency and the computation and communitation burden of the VSS-based DPML schemes are still two serious challenges. Although Byzantine Fault Tolerance (BFT) system has been brought to guarantee the consistency and improve the efficiency of the existing VSS-based DPML schemes recently, we explore an Adaptive Share Delay Provision (ASDP) strategy, and launch an ASDP-based Customized Model Poisoning Attack (ACuMPA) for certain participants in this paper. We theoretically analyzed why the ASDP strategy and the ACuMPA algorithm works to the existing schemes. Next, we propose an [E]fficient [By]zantine [F]ault [T]olerant-based [Ve]rifiable [S]ecret-sharing (EByFTVeS) scheme. Finally, the validity, liveness, consistency and privacy of the EByFTVeS scheme are theoretically analyzed, while the efficiency of the EByFTVeS scheme outperforms that of the-state-of-art VSS scheme according to comparative experiment results.

  匹配依据：MPC: secret sharing

  </details>

- **Cosmology with supernova Encore in the strong lensing cluster MACS J0138-2155: Lens model comparison and H0 measurement**
  2025-09-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.12319)
  S. H. Suyu, A. Acebron, C. Grillo, P. Bergamini, G. B. Caminha, S. Cha, J. M. Diego, S. Ertl, N. Foo, B. L. Frye, Y. Fudamoto, G. Granata, A. Halkola, M. J. Jee, P. S. Kamieneski, A. M. Koekemoer, A. K. Meena, A. B. Newman, S. Nishida, M. Oguri, P. Rosati, S. Schuldt, A. Zitrin, R. Cañameras, E. E. Hayes, C. Larison, E. Mamuzic, M. Millon, J. D. R. Pierel, L. Tortorelli, H. Wang

  <details><summary>摘要 / Abstract</summary>

  MACS J0138-2155 is the only known cluster to strongly lens two supernovae (SNe), Requiem and Encore, from the same host galaxy at z=1.949. We present seven independent mass models of the galaxy cluster built using six software packages. By conducting a blind analysis (no exchanges of results between modeling teams), we quantified uncertainties due to modeling and software. Through HST, JWST and MUSE observations, we assembled high-quality data products, including eight &quot;gold&quot; lensed image systems consisting of 23 images with secure spectroscopic redshifts, and one &quot;silver&quot; system with a likely redshift value. Restricting to the gold images, we obtain overall consistent model predictions of the positions, magnifications and time delays of SN Encore and SN Requiem images, especially for models with $χ^2 \leq 25$. We predict the appearance of the next images of SNe Encore and Requiem with a time delay of &gt;~3000 days and of ~3700 to 4000 days, respectively, based on a fiducial cosmological model of $H_0 = 70 {\rm\ km\ s^{-1}\ Mpc^{-1}}$ and $Ω_{\rm m} = 0.3$. We obtain relations between $H_0$ and the time delays of SNe Encore and Requiem. In particular, for $H_0 = 73 {\rm\ km\ s^{-1}\ Mpc^{-1}}$, the four lowest $χ^2$ models predict SN Requiem to reappear in ~Apr-Dec 2026; for $H_0 = 67 {\rm\ km\ s^{-1}\ Mpc^{-1}}$, in ~Mar-Nov 2027. Using the newly measured time delay between the two detected images of SN Encore by Pierel et al. (2026) and our mass models, we jointly infer $H_0 = {\rm 66.9^{+11.2}_{-8.1}\ km\ s^{-1}\ Mpc^{-1}}$, where the uncertainty is dominated by that of the time delay. The long delays of the next-appearing SN Requiem and SN Encore images provide excellent opportunities to measure $H_0$ with an uncertainty of 2-3%. Our mass models form the basis for cosmological inference from this unique lens cluster with two strongly lensed SNe. (Abridged)

  匹配依据：MPC: mpc (context)

  </details>

- **ORQ: Complex Analytics on Private Data with Strong Security Guarantees**
  2025-09-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.10793) · [IACR ePrint](https://eprint.iacr.org/2025/1657)
  Eli Baum, Sam Buxbaum, Nitin Mathai, Muhammad Faisal, Vasiliki Kalavri, Mayank Varia, John Liagouris

  <details><summary>摘要 / Abstract</summary>

  We present ORQ, a system that enables collaborative analysis of large private datasets using cryptographically secure multi-party computation (MPC). ORQ protects data against semi-honest or malicious parties and can efficiently evaluate relational queries with multi-way joins and aggregations that have been considered notoriously expensive under MPC. To do so, ORQ eliminates the quadratic cost of secure joins by leveraging the fact that, in practice, the structure of many real queries allows us to join records and apply the aggregations &quot;on the fly&quot; while keeping the result size bounded. On the system side, ORQ contributes generic oblivious operators, a data-parallel vectorized query engine, a communication layer that amortizes MPC network costs, and a dataflow API for expressing relational analytics -- all built from the ground up. We evaluate ORQ in LAN and WAN deployments on a diverse set of workloads, including complex queries with multiple joins and custom aggregations. When compared to state-of-the-art solutions, ORQ significantly reduces MPC execution times and can process one order of magnitude larger datasets. For our most challenging workload, the full TPC-H benchmark, we report results entirely under MPC with Scale Factor 10 -- a scale that had previously been achieved only with information leakage or the use of trusted third parties.

  匹配依据：MPC: secure multi party computation

  </details>

- **Dory: Streaming PCG with Small Memory**
  2025-09-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1660)
  Xiaojie Guo, Hanlin Liu, Zhicong Huang, Hongrui Cui, Wenhao Zhang, Cheng Hong, Xiao Wang, Kang Yang, Yu Yu

  <details><summary>摘要 / Abstract</summary>

  Pseudorandom correlation generators (PCGs) have been popular in generating a huge amount of correlated randomness, a critical resource in secure computation. However, existing PCGs are memory-consuming and not friendly to resource-constrained devices. Even for moderate devices, the need for large memory can also be a disadvantage in applications like zero-knowledge proofs or large-scale secure computation. In this paper, we propose a malicious streaming PCG (sPCG), which generates a bounded number of tuples of subfield vector oblivious linear evaluation (sVOLE) on-the-fly, each with sublinear memory and computation. 1. We propose an efficient protocol that replaces the relaxed distributed comparison function in the best pseudorandom correlation function (PCF) for sVOLE (CRYPTO&#x27;22), which has the same streaming features for any polynomial number of tuples. With this protocol, our sPCG is doubly efficient in memory and the computation per sVOLE. Moreover, we augment the black-box distributed setup to malicious security and yield 4x communication improvement. Our sPCG can be extended to a more efficient sVOLE PCF with the same improvements in memory and computation, and a 2x faster malicious non-black-box distributed setup. 2. We present a practical attack on the Learning Parity with Noise (LPN) assumption for expand-accumulate codes with regular noise, revealing that some previous parameters provide around 14~22 bits of security over binary noises, far below the target 128 bits. To address this, we introduce a low-Hamming-weight noise distribution to withstand the attack. We then derive some updated LPN parameters with the new noise distribution, restoring 128-bit security and reducing the noise-related computation and communication. 3. We provide an implementation of our sPCG for the special case of correlated oblivious transfer (COT). In addition to the improvements over the best PCF, our sPCG can have a comparable end-to-end performance to Ferret (CCS&#x27;20) and the PCG from expand-convolute codes (CRYPTO&#x27;23), two state-of-the-art PCGs, with the advantage of being able to produce 10 million COTs on-the-fly and reducing the memory from 337 MB and 624 MB to 20 MB, respectively.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **WISCH: Efficient data signing via correlated signatures**
  2025-09-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1650)
  Ariel Futoransky, Ramses Fernandez, Emilio Garcia, Gabriel Larotonda, Sergio Demian Lerner

  <details><summary>摘要 / Abstract</summary>

  We present WISCH, a commit-reveal protocol that combines compact aggregate signatures with hash-based commitments to enable selective disclosure of correlated data in multiparty computation. The protocol separates an on-chain verification core from off chain preparation, so that verification cost depends only on the number of openings, not on the size of the underlying message space. This yields asymptotic efficiency: on-chain cost grows linearly in the number of revealed items and is independent of the ambient domain, while the per-byte overhead decreases with the message granularity. Security is established via a simulation-based proof in a UC framework with an ideal ledger functionality, in the algebraic group and global random-oracle models, under standard assumptions for discrete-log-based signatures and hash-based commitments. Thus WISCH provides selectively verifiable revelation with succinct on-chain checks and provable security guarantees.

  匹配依据：MPC: multiparty computation

  </details>

- **Lattice-based Multi-message Multi-recipient KEM/PKE with Malicious Security**
  2025-09-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1655)
  Zeyu Liu, Katerina Sotiraki, Eran Tromer, Yunhao Wang

  <details><summary>摘要 / Abstract</summary>

  The efficiency of Public Key Encryption (PKE) and Key Encapsulation Mechanism (KEM), and in particular their large ciphertext size, is a bottleneck in real-world systems. This worsens in post-quantum secure schemes (e.g., lattice-based ones), whose ciphertexts are an order of magnitude larger than prior ones.%their non-post-quantum counterparts. The work of Kurosawa (PKC&#x27;02) introduced multi-message multi-recipient PKE (mmPKE) to reduce the amortized ciphertext size when sending messages to more than one recipient. This notion naturally extends to multi-message multi-recipient KEM (mmKEM). In this work, we first show concrete attacks on existing lattice-based mmPKE schemes: Using maliciously-crafted recipient public keys, these attacks completely break semantic security and key privacy, and are inherently undetectable. We then introduce the first lattice-based mmKEM scheme that maintains full privacy even in the presence of maliciously-generated public keys. Concretely, the ciphertext size of our mmKEM for 100 recipients is ${\sim} 8\times$ smaller than naively using Crystals-Kyber. We also show how to extend our mmKEM to mmPKE, achieving a scheme that outperforms all prior lattice-based mmPKE schemes in terms of both security and efficiency. We additionally show a similar efficiency gain when applied to batched random oblivious transfer, and to group oblivious message retrieval. Our scheme is proven secure under a new Module-LWE variant assumption, Oracle Module-LWE, which can be of its own independent interest. We reduce standard MLWE to this new assumption for some parameter regimes, which also gives intuition on why this assumption holds for the parameter we are interested in (along with additional cryptanalysis). Furthermore, we show an asymptotically efficient compiler that removes the assumption made in prior works that recipients know their position in the list of intended recipients for every ciphertext.

  匹配依据：MPC: oblivious transfer

  </details>

- **Mixed Arithmetic-Binary Circuits in Fluid MPC Against Honest Majority of 4-Party and Its Applications Against Semi-Honest Adversary**
  2025-09-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1642)
  Furkan Kerim Çabaş, Oğuz Yayla

  <details><summary>摘要 / Abstract</summary>

  Secure multi party computation protocols (MPC) translating between arithmetic and binary data types have recently gained attraction which is introduced by Rotaru and Wood in 2019, called daBit, and improved by Escudero et. al. called edaBits. EdaBits are simply secret shares in arithmetic domain and bit decomposition of the arithmetic share is the binary form the secret shares. These protocols are preprocessing for MPC protocols in order to improve efficiency. Furthermore, fluid MPC setting, introduced by Choudhuri, Goel, Green, Jain and Kaptchuk in 2021, is a framework which the parties, called dynamic parties, do not have be online throughout the whole process. Fluid MPC framework is still has to be worked and conventional protocols and techniques has to be adapted for it. Our work introduces an edaBits protocol specifically designed for the fluid MPC setting under a four-party honest-majority model. The protocol, which consists of eight subprotocols, achieves security against an honest majority and departs slightly from the traditional cut-and-choose paradigm. It attains linear memory and time complexity, as well as constant communication complexity. Finally, we demonstrate two applications that employ edaBits within the fluid MPC framework under the semi-honest adversary model.

  匹配依据：MPC: secure multi party computation

  </details>

- **CryptGNN: Enabling Secure Inference for Graph Neural Networks**
  2025-09-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.09107)
  Pritam Sen, Yao Ma, Cristian Borcea

  <details><summary>摘要 / Abstract</summary>

  We present CryptGNN, a secure and effective inference solution for third-party graph neural network (GNN) models in the cloud, which are accessed by clients as ML as a service (MLaaS). The main novelty of CryptGNN is its secure message passing and feature transformation layers using distributed secure multi-party computation (SMPC) techniques. CryptGNN protects the client&#x27;s input data and graph structure from the cloud provider and the third-party model owner, and it protects the model parameters from the cloud provider and the clients. CryptGNN works with any number of SMPC parties, does not require a trusted server, and is provably secure even if P-1 out of P parties in the cloud collude. Theoretical analysis and empirical experiments demonstrate the security and efficiency of CryptGNN.

  匹配依据：MPC: secure multi party computation

  </details>

- **Pseudorandom Correlation Functions from Ring-LWR**
  2025-09-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1637)
  Sebastian Hasler, Pascal Reisert, Ralf Küsters

  <details><summary>摘要 / Abstract</summary>

  State-of-the-art actively secure multiparty computation protocols, like SPDZ (Damgård et al., CRYPTO 2012), use correlated randomness, like Beaver triples, to achieve a highly efficient online phase. For a long time, the generation of the correlated randomness in the offline phase relied on classical cryptographic primitives, like somewhat homomorphic encryption or oblivious transfer, that required significant communication. More recently, Boyle et al. (FOCS 2020) defined a new primitive called pseudorandom correlation functions (PCFs) to generate correlated randomness non-interactively. PCFs set up keys for each party in an initial interactive phase, which can then be used by the parties to generate a large number of shares of the correlated randomness without further communication. In the random oracle model (ROM), two-party PCFs can be generically constructed based on evaluating a weak pseudorandom function (WPRF) using a powerful-enough homomorphic secret sharing scheme. However, the concrete efficiency of instantiations of this approach has not been analyzed so far. There are also some works that construct PCFs based on other approaches, but they cannot be used for correlations of degree $\ge 2$ (e.g., Beaver triples) over large rings/fields (such as those used in SPDZ). In this paper, we improve the complexity and concrete efficiency of PCFs over large rings/fields by presenting a new generic PCF based on the hardness of the ring-learning with rounding (Ring-LWR) problem and FHE. We only share BFV keys in the initial interactive phase. The two parties then use the random oracle to locally sample BFV (pseudo-)ciphertexts encrypting pseudorandom plaintexts. We use a new bootstrapping algorithm for these (pseudo-)ciphertexts that reduces initially saturated noise to a level where the parties can use the homomorphic properties of the BFV scheme to correlate the encrypted randomness locally. Both parties can then produce, without further interaction, shares of the correlated randomness with their secret key share. Our new PCF works with any form of correlated randomness that can be expressed as an arithmetic circuit over a base ring $\mathbb Z_t$ or field $\mathbb F_{p^d}$, e.g., Beaver or matrix triples.

  匹配依据：MPC: oblivious transfer, secret sharing, secure multiparty computation

  </details>

- **Perfectly-Private Analog Secure Aggregation in Federated Learning**
  2025-09-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.08683)
  Delio Jaramillo-Velez, Charul Rajput, Ragnar Freij-Hollanti, Camilla Hollanti, Alexandre Graell i Amat

  <details><summary>摘要 / Abstract</summary>

  In federated learning, multiple parties train models locally and share their parameters with a central server, which aggregates them to update a global model. To address the risk of exposing sensitive data through local models, secure aggregation via secure multiparty computation has been proposed to enhance privacy. At the same time, perfect privacy can only be achieved by a uniform distribution of the masked local models to be aggregated. This raises a problem when working with real valued data, as there is no measure on the reals that is invariant under the masking operation, and hence information leakage is bound to occur. Shifting the data to a finite field circumvents this problem, but as a downside runs into an inherent accuracy complexity tradeoff issue due to fixed point modular arithmetic as opposed to floating point numbers that can simultaneously handle numbers of varying magnitudes. In this paper, a novel secure parameter aggregation method is proposed that employs the torus rather than a finite field. This approach guarantees perfect privacy for each party&#x27;s data by utilizing the uniform distribution on the torus, while avoiding accuracy losses. Experimental results show that the new protocol performs similarly to the model without secure aggregation while maintaining perfect privacy. Compared to the finite field secure aggregation, the torus-based protocol can in some cases significantly outperform it in terms of model accuracy and cosine similarity, hence making it a safer choice.

  匹配依据：MPC: secure multiparty computation

  </details>

- **From Physical to Logical: Graph-State-Based Connectivity in Quantum Networks**
  2025-09-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.08384)
  Mateo M. Blanco, Manuel Fernández-Veiga, Ana Fernández-Vilas, Rebeca P. Díaz-Redondo

  <details><summary>摘要 / Abstract</summary>

  Entanglement is a key resource in quantum communication, but bipartite schemes are often insufficient for advanced protocols like quantum secret sharing or distributed computing. Graph states offer a flexible way to represent and manage multipartite entanglement in quantum networks, enabling logical connectivity through local operations and classical communication (LOCC). In this work, we extend existing approaches based on bi-star configurations to more complex multi-star topologies. We analyze the maximum connectivity that can be achieved in networks of $m$ switches, each connected to $n$ clients, including asymmetric cases where the number of clients varies per switch. We also propose methods to enable logical communication between distant nodes. Our results support the development of scalable quantum networks with rich connectivity beyond traditional bipartite structures.

  匹配依据：MPC: secret sharing

  </details>

- **Computationally and Communication Efficient Batched Asynchronous DPSS from Lightweight Cryptography**
  2025-09-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1631)
  Akhil Bandarupalli, Xiaoyu Ji, Soham Jog, Aniket Kate, Chen-Da Liu-Zhang, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  Verifiable Secret Sharing (VSS) is a fundamental primitive in threshold cryptography and multi-party computation. It preserves secrecy, integrity, and availability of a shared secret for a fixed set of parties, with a subset of them being malicious. In practical applications, especially when the secret sharing is expected to be maintained over long durations, the VSS scheme should be able to cater to a dynamic setting where involved parties may change. The primitive known as Dynamic Proactive Secret Sharing (DPSS) is beneficial here, as it facilitates the secure transfer of secrets from the original committee to a new committee. Nevertheless, prior works on DPSS protocols either rely on unrealistic time bounds on message delivery or have a high computational cost, which limits their scalability beyond tens of parties. In this work, we present a scalable asynchronous DPSS protocol that utilizes lightweight cryptographic tools, such as hash functions and symmetric-key encryption. Our protocol achieves full security and optimal fault tolerance with amortized linear communication costs. Unlike existing solutions, our proposed protocol is also post-quantum secure. By balancing computation and communication, our approach offers practical performance at scale. Our implementation results demonstrate improved scalability and efficiency, surpassing the current state-of-the-art achieving a $22.1\times$ lower latency than the prior best work. Furthermore, our solution also scales gracefully with increasing $n$ and reshares a batch of $100,000$ secrets between committees of sizes $n=112$ parties in under a minute.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Linear time encodable binary code achieving GV bound with linear time encodable dual achieving GV bound**
  2025-09-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.07639)
  Martijn Brehm, Nicolas Resch

  <details><summary>摘要 / Abstract</summary>

  We initiate the study of what we term ``fast good codes&#x27;&#x27; with ``fast good duals.&#x27;&#x27; Specifically, we consider the task of constructing a rate 1/2 binary linear code such that both it and its dual are asymptotically good (in fact, have rate-distance tradeoff approaching the GV bound), and are encodable in linear time. While we believe such codes should find applications more broadly, as motivation we describe how such codes can be used the secure computation task of encrypted matrix-vector product. Our main contribution is a construction of such a fast good code with fast good dual. Our construction is inspired by the repeat multiple accumulate (RMA) code. To create the rate 1/2 code, after repeating each message coordinate, we perform accumulation steps -- where first a uniform coordinate permutation is applied, and afterwards the prefix-sum mod 2 is applied -- which are alternated with discrete derivative steps -- where again a uniform coordinate permutation is applied, and afterwards the previous two coordinates are summed mod 2. Importantly, these two operations are inverse of each other. In particular, the dual of the code is very similar, with the accumulation and discrete derivative steps reversed. Our analysis is inspired by a prior analysis of RMA: we bound the expected number of codewords of weight below the GV bound. We face new challenges in controlling the behaviour of the discrete derivative operation (which can significantly drop the weight of a vector), which we overcome by careful case analysis.

  匹配依据：MPC: secure computation

  </details>

- **Round-Efficient Composable Two-Party Quantum Computation**
  2025-09-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1595)
  Vipul Goyal, Xiao Liang, Omkant Pandey, Yuhao Tang, Takashi Yamakawa

  <details><summary>摘要 / Abstract</summary>

  We study secure computation in the plain model against fully concurrent quantum adversaries. While classical simulation-based notions --- such as Super-Polynomial Simulation (SPS) security --- have enabled meaningful forms of concurrent security, very little is known about their quantum counterparts, particularly under standard polynomial-time hardness assumptions. Our main result is the first post-quantum two-party computation protocol that achieves concurrent SPS security, based solely on the minimal assumption of semi-honest post-quantum oblivious transfer (PQ-OT). Moreover, our protocol has constant round complexity when the underlying PQ-OT protocol is constant-round. This can be viewed as a post-quantum analog of the classical result by Garg et al. [Eurocrypt&#x27;12], but with a crucial difference: our security proof completely avoids rewinding, making it suitable for quantum settings where rewinding is notoriously challenging due to the no-cloning principle. By leveraging a compiler of Bartusek et al. [Crypto&#x27;21], we further extend our result to the fully quantum setting, yielding the first constant-round concurrent SPS two-party computation for quantum functionalities in the plain model. Additionally, we construct a two-round, public-coin, concurrent SPS post-quantum zero-knowledge protocol for languages in $\mathsf{NP} \cap \mathsf{coNP}$, under the quantum polynomial-time hardness of LWE. This result is notable even in the classical setting.

  匹配依据：MPC: oblivious transfer, secure computation, two party computation

  </details>

- **HE-SecureNet: An Efficient and Usable Framework for Model Training via Homomorphic Encryption**
  2025-09-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1591)
  Thomas Schneider, Huan-Chih Wang, Hossein Yalame

  <details><summary>摘要 / Abstract</summary>

  Energy-efficient edge devices are essential for the widespread deployment of machine learning (ML) services. However, their limited computational capabilities make local model training infeasible. While cloud-based training offers a scalable alternative, it raises serious privacy concerns when sensitive data is outsourced. Homomorphic Encryption (HE) enables computation directly on encrypted data and has emerged as a promising solution to this privacy challenge. Yet, current HE-based training frameworks face several shortcomings: they often lack support for complex models and non-linear functions, struggle to train over multiple epochs, and require cryptographic expertise from end users. We present HE-SecureNet, a novel framework for privacy-preserving model training on encrypted data in a single-client–server setting, using hybrid HE cryptosystems. Unlike prior HE-based solutions, HE-SecureNet supports advanced models such as Convolutional Neural Networks and handles non-linear operations including ReLU, Softmax, and MaxPooling. It introduces a level-aware training strategy that eliminates costly ciphertext level alignment across epochs. Furthermore, HE-SecureNet automatically converts ONNX models into optimized secure C++ training code, enabling seamless integration into privacy-preserving ML pipeline—without requiring cryptographic knowledge. Experimental results demonstrate the efficiency and practicality of our approach. On the Breast Cancer dataset, HE-SecureNet achieves a 5.2× speedup and 33% higher accuracy compared to ConcreteML (Zama) and TenSEAL (OpenMined). On the MNIST dataset, it reduces CNN training latency by 2× relative to Glyph (Lou et al., NeurIPS’20), and cuts communication overhead by up to 66× on MNIST and 42× on CIFAR-10 compared to MPC-based solutions.

  匹配依据：MPC: mpc (context)

  </details>

- **Secure Agents**
  2025-09-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1587)
  Nakul Khambhati, Joonwon Lee, Gary Song, Rafail Ostrovsky, Sam Kumar

  <details><summary>摘要 / Abstract</summary>

  Organizations increasingly need to pool their sensitive data for collaborative computation while keeping their own data private from each other. One approach is to use a family of cryptographic protocols called Secure Multi-Party Computation (MPC). Another option is to use a set of cloud services called clean rooms. Unfortunately, neither approach is satisfactory. MPC is orders of magnitude more resource-intensive than regular computation, making it impractical for workloads like data analytics and AI. Clean rooms do not give users the flexibility to perform arbitrary computations. We propose and develop an approach and system called a secure agent and utilize it to create a virtual clean room, Flexroom, that is both performant and flexible. Secure agents enable parties to create a phantom identity that they can collectively control, using maliciously secure MPC, which issues API calls to external services with parameters that remain secret from all participating parties. Importantly, in Flexroom, the secure agent uses MPC not to perform the computation itself, but instead merely to orchestrate the computation in the cloud, acting as a distinct trusted entity jointly governed by all parties. As a result, Flexroom enables collaborative computation with unfettered flexibility, including the ability to use convenient cloud services. By design, the collaborative computation runs at plaintext speeds, so the overhead of Flexroom will be amortized over a long computation.

  匹配依据：MPC: secure multi party computation

  </details>

- **Efficient and Secure Sleepy Model for BFT Consensus**
  2025-09-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.03145)
  Pengkun Ren, Hai Dong, Zahir Tari, Pengcheng Zhang

  <details><summary>摘要 / Abstract</summary>

  Byzantine Fault Tolerant (BFT) consensus protocols for dynamically available systems face a critical challenge: balancing latency and security in fluctuating node participation. Existing solutions often require multiple rounds of voting per decision, leading to high latency or limited resilience to adversarial behavior. This paper presents a BFT protocol integrating a pre-commit mechanism with publicly verifiable secret sharing (PVSS) into message transmission. By binding users&#x27; identities to their messages through PVSS, our approach reduces communication rounds. Compared to other state-of-the-art methods, our protocol typically requires only four network delays (4$Δ$) in common scenarios while being resilient to up to 1/2 adversarial participants. This integration enhances the efficiency and security of the protocol without compromising integrity. Theoretical analysis demonstrates the robustness of the protocol against Byzantine attacks. Experimental evaluations show that, compared to traditional BFT protocols, our protocol significantly prevents fork occurrences and improves chain stability. Furthermore, compared to longest-chain protocol, our protocol maintains stability and lower latency in scenarios with moderate participation fluctuations.

  匹配依据：MPC: secret sharing

  </details>

- **Breaking Omertà: On Threshold Cryptography, Smart Collusion, and Whistleblowing**
  2025-09-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1582)
  Mahimna Kelkar, Aadityan Ganesh, Aditi Partap, Joseph Bonneau, S. Matthew Weinberg

  <details><summary>摘要 / Abstract</summary>

  Cryptographic protocols often make honesty assumptions---e.g., fewer than $t$ out of $n$ participants are adversarial. In practice, these assumptions can be hard to ensure, particularly given monetary incentives for participants to collude and deviate from the protocol. In this work, we explore combining techniques from cryptography and mechanism design to discourage collusion. We formalize protocols in which colluders submit a cryptographic proof to whistleblow against their co-conspirators, revealing the dishonest behavior publicly. We provide general results on the cryptographic feasibility, and show how whistleblowing fits a number of applications including secret sharing, randomness beacons, and anonymous credentials. We also introduce smart collusion---a new model for players to collude. Analogous to blockchain smart contracts, smart collusion allows colluding parties to arbitrarily coordinate and impose penalties on defectors (e.g., those that blow the whistle). We show that unconditional security is impossible against smart colluders even when whistleblowing is anonymous and can identify all colluding players. On the positive side, we construct a whistleblowing protocol that requires only a small deposit and can protect against smart collusion even with roughly $t$ times larger deposit.

  匹配依据：MPC: secret sharing

  </details>

- **BitPriv: A Privacy-Preserving Protocol for DeFi Applications on Bitcoin**
  2025-09-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1575)
  Ioannis Alexopoulos, Zeta Avarikioti, Paul Gerhart, Matteo Maffei, Dominique Schröder

  <details><summary>摘要 / Abstract</summary>

  Bitcoin secures over a trillion dollars in assets, yet its scripting language limits expressive decentralized-finance applications. BitVM enables arbitrary off-chain computation to be enforced through Bitcoin fraud proofs, but it does not provide privacy for inputs such as bids, quotes, and reserve prices. We present BitPriv, to our knowledge the first protocol that conditions payments on the outcome of an arbitrary secure two-party computation over private inputs on unmodified Bitcoin. Its core primitive, the Garbled Hashed Timelock Contract (GHTLC), binds Bitcoin payments to garbled-circuit output labels. Parties evaluate the circuit off-chain, while cut-and-choose detects malformed garbling and BitVM punishes detected violations. Under application-specific bounds, collateral can make deviations unprofitable for rational adversaries. We instantiate BitPriv in BitMarket, a Bitcoin-native sealed-bid auction, and BitBridge, an intent-based cross-chain bridge. Inputs remain private until the protocol execution fixes the outcome. Optimistic settlement costs less than \$3 in both applications. Depending on the backend, BitMarket disputes cost \$47–\$312 and BitBridge disputes cost \$47–\$657. BitPriv provides a blueprint for enforceable, privacy-preserving DeFi primitives on Bitcoin without trusted hardware, sidechains, or consensus changes.

  匹配依据：MPC: garbled circuit, secure two party computation

  </details>

- **Efficient and High-Accuracy Secure Two-Party Protocols for a Class of Functions with Real-number Inputs**
  2025-09-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.01178)
  Hao Guo, Zhaoqian Liu, Liqiang Peng, Shuaishuai Li, Ximing Fu, Weiran Liu, Lin Qu

  <details><summary>摘要 / Abstract</summary>

  In two-party secret sharing scheme, values are typically encoded as unsigned integers $\mathsf{uint}(x)$, whereas real-world applications often require computations on signed real numbers $\mathsf{Real}(x)$. To enable secure evaluation of practical functions, it is essential to computing $\mathsf{Real}(x)$ from shared inputs, as protocols take shares as input. At USENIX&#x27;25, Guo et al. proposed an efficient method for computing signed integer values $\mathsf{int}(x)$ from shares, which can be extended to compute $\mathsf{Real}(x)$. However, their approach imposes a restrictive input constraint $|x| &lt; \frac{L}{3}$ for $x \in \mathbb{Z}_L$, limiting its applicability in real-world scenarios. In this work, we significantly relax this constraint to $|x| &lt; B$ for any $B \leq \frac{L}{2}$, where $B = \frac{L}{2}$ corresponding to the natural representable range in $x \in \mathbb{Z}_L$. This relaxes the restrictions and enables the computation of $\mathsf{Real}(x)$ with loose or no input constraints. Building upon this foundation, we present a generalized framework for designing secure protocols for a broad class of functions, including integer division ($\lfloor \frac{x}{d} \rfloor$), trigonometric ($\sin(x)$) and exponential ($e^{-x}$) functions. Our experimental evaluation demonstrates that the proposed protocols achieve both high efficiency and high accuracy. Notably, our protocol for evaluating $e^{-x}$ reduces communication costs to approximately 31% of those in SirNN (S&amp;P 21) and Bolt (S&amp;P 24), with runtime speedups of up to $5.53 \times$ and $3.09 \times$, respectively. In terms of accuracy, our protocol achieves a maximum ULP error of $1.435$, compared to $2.64$ for SirNN and $8.681$ for Bolt.

  匹配依据：MPC: secret sharing, secure evaluation

  </details>

- **Duality of extremal quantum states in verification and data hiding**
  2025-09-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.01281)
  Seiseki Akibue, Yuki Takeuchi

  <details><summary>摘要 / Abstract</summary>

  Quantum state verification (QSV) and quantum data hiding (QDH) have so far been studied separately. QSV decides whether a given quantum state is close to the ideal one, with significantly lower sample complexity compared with direct application of quantum tomography. On the other hand, QDH is a cryptographic protocol that encodes secret classical information in multipartite quantum states, providing stronger security guarantees than conventional classical secret-sharing schemes. Here, we consider two fundamental quantities of a pure quantum state, determining the sample complexity needed for QSV or the security level in QDH. We demonstrate that a pure state is most difficult to verify in QSV if and only if it is most secure in QDH with respect to those quantities. Furthermore, for such extremal states, the two fundamental quantities coincide. We also generalize this relationship to one between the security of QDH using mixed states and the sample complexity for quantum subspace verification, which is a generalization of QSV. As an application, we show the existence of efficient QSV protocols that are generalizations of the existing ones and examine the fundamental limitations on QDH by synthesizing research from both domains.

  匹配依据：MPC: secret sharing

  </details>

- **Large cliques and large independent sets: can they coexist?**
  2025-08-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.00721)
  Uriel Feige, Ilia Pauzner

  <details><summary>摘要 / Abstract</summary>

  For a graph $G$ and a parameter $k$, we call a vertex $k$-enabling if it belongs both to a clique of size $k$ and to an independent set of size $k$, and we call it $k$-excluding otherwise. Motivated by issues that arise in secret sharing schemes, we study the complexity of detecting vertices that are $k$-excluding. We show that for every $ε$, for sufficiently large $n$, if $k &gt; (\frac{1}{4} + ε)n$, then every graph on $n$ vertices must have a $k$-excluding vertex, and moreover, such a vertex can be found in polynomial time. In contrast, if $k &lt; (\frac{1}{4} - ε)n$, a regime in which it might be that all vertices are $k$-enabling, deciding whether a graph has no $k$-excluding vertex is NP-hard.

  匹配依据：MPC: secret sharing

  </details>

- **A Traceable Threshold Asmuth--Bloom Secret Sharing Scheme**
  2025-08-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1561)
  Maria Leslie, Ratna Dutta

  <details><summary>摘要 / Abstract</summary>

  In a t-out-of-n threshold secret sharing scheme, accountability is crucial when a subset of f &lt; t servers collude to leak secret shares. Traceable Threshold Secret Sharing (TTSS) ensures that leaked shares can be traced back to the compromised servers while preventing false accusations through non-imputability. In Crypto’24, Boneh et al. proposed new definitions and more practical constructions for TTSS based on Shamir’s and Blakley’s secret sharing schemes, removing the practical limitation of existing TTSS. Our work presents a traceable secret sharing scheme built upon an additive variant of the Asmuth-Bloom scheme, relying only on black-box access to the reconstruction box R. In our model, a subset of f &lt; t colluding servers can construct a reconstruction box R that recovers the secret with the assistance of an additional t − f random shares. We note that integrating tracing in the standard (t, n)-Asmuth-Bloom Secret Sharing (ABSS) scheme exhibits a tracing leakage issue. We fix this limitation by introducing additive variants of ABSS, ABSS-I and ABSS-II that retain the security of the original scheme ABSS while splitting the secret s into t additive components and generating all shares from the additive components of s. Based on ABSS-I, we construct a TTSS scheme, TTSS-I, that introduces traceability into the framework and is proven to be universally traceable in the random oracle model, assuming R is a universally good reconstruction box. We integrate a tracing mechanism in ABSS-II and propose a second scheme, TTSS-II, which extends TTSS-I by additionally concealing partial information about the additive component of the secret s to introduce non-imputability to prevent the tracer from falsely accusing any honest party by fabricating evidence of its corruption. The security of TTSS-II is also in the random oracle model and relies on the hardness of the discrete logarithm problem.

  匹配依据：MPC: secret sharing

  </details>

- **On Achieving \`\`Best-in-the-Multiverse'' MPC**
  2025-08-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1557)
  Anasuya Acharya, Carmit Hazay, Muthuramakrishnan Venkitasubramaniam

  <details><summary>摘要 / Abstract</summary>

  The notion of Best-of-Both-Worlds introduced in the work of Ishai et al. (CRYPTO 2006) investigated whether an MPC protocol can simultaneously provide two incomparable security guarantees: guaranteed output delivery against an honest majority and security with abort against a dishonest majority and provided tight upper and lower bounds in the presence of computationally bounded, i.e., PPT adversaries. Another line of works starting from the work of Chaum (CRYPTO 1989) considered protocols that simultaneously achieved security against an unbounded adversary corrupting a minority of the parties and security against arbitrary corruption by a PPT adversary. In this work, we generalize previous work to investigate a fundamental challenge of designing an MPC in a multiverse where security is specified with respect to (1) GOD, (2) fairness, (3) security w.r.t. unbounded adversaries, and (4) security with abort. The work of Lucas et al. (PODC 2010) resolved this question when considering threshold adversaries; however, the case of general adversary structures remains open. Our main result completely characterizes when a protocol can simultaneously achieve all properties. Namely, given adversary structures $Z_{\mathsf{GOD}}, Z_{fair}, Z_{S}$ and $Z_{C}$, we provide tight upper and lower bounds for when an MPC protocol can provide GOD, fairness, and security with abort respectively for unbounded and PPT adversaries w.r.t. these adversary structures.

  匹配依据：MPC: mpc (context)

  </details>

- **Generation of Large Kitten states via thermally driven dissipative freezing**
  2025-08-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.00601)
  Caspar Groiseau

  <details><summary>摘要 / Abstract</summary>

  We show that one can exploit the representation of the Dicke state with magnetic quantum number $0$ in orthogonal bases to increase the probability of producing a large Kitten state or even a Cat state via dissipative one-axis twisting, resulting in a net increase in metrological sensitivity and robustness against white noise with respect to the initial state. The resulting states are also useful for quantum secret sharing. The success of the scheme is heralded by the rate of photoemissions. Unlike previous iterations, we have an important population of the larger Kitten states, which makes post-selecting trajectories for them feasible.

  匹配依据：MPC: secret sharing

  </details>

- **Statistical MPC with a Constant Communication Overhead**
  2025-08-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1555)
  Ashish Choudhury, Ivan Damgård, Shravani Patil, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  We study the feasibility of constant communication-overhead statistically-secure MPC tolerating malicious adversaries in the synchronous setting and guaranteed output delivery (GOD). We propose a protocol with $n = 3t + 1$ for SIMD circuits with a communication overhead of ${\cal O}(1)$ and round complexity ${\cal O}(D)$ for circuit depth $D$, where $n$ is the number of parties and $t$ is the maximum number of corruptions. Moreover, our protocol achieves GOD. This is the first MPC protocol with above characteristics. To design our protocol, we give two major contributions. Our first technical contribution is a verifiable secret sharing (VSS) protocol that achieves constant per-secret overhead via two-dimensional packing. Our second contribution is a constant-overhead degree-reduction protocol that converts a high-degree packed sharing into a lower-degree packed sharing.

  匹配依据：MPC: secret sharing

  </details>

- **M&amp;M: Secure Two-Party Machine Learning through Efficient Modulus Conversion and Mixed-Mode Protocols (Full Version)**
  2025-08-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1551)
  Ye Dong, Wen-jie Lu, Xiaoyang Hou, Kang Yang, Jian Liu

  <details><summary>摘要 / Abstract</summary>

  Secure two-party machine learning has made substantial progress through the use of mixed-mode protocols. Despite these advancements, existing approaches often suffer from efficiency bottlenecks due to the inherent mismatch between the optimal domains of various cryptographic primitives, such as Homomorphic Encryption and Oblivious Transfer. In response to these challenges, we introduce the \tNAME{} framework, which features an efficient modulus conversion protocol. This breakthrough enables seamless integration of the most suitable cryptographic subprotocols within their optimal modulus domains, allowing linear computations to be executed over a prime modulus and nonlinear computations over a two-power modulus, with a minimal modulus conversion overhead. We further establish new benchmarks for the performance of fundamental primitives, namely comparison and multiplication, across various two-party techniques, together with our practical optimizations to improve efficiency. By incorporating these techniques, \tNAME{} demonstrates significant performance enhancements over state-of-the-art solutions: \romannumeral1) we report a $6\times$-$100\times$ improvement for approximated truncations with 1-bit error tolerance; \romannumeral2) an average of $5\times$ (resp. $4\times$) reduction in communication (resp. runtime) for machine learning functions; \romannumeral3) and a 25\%-99\% improvement in cost-efficiency for private inference of deep neural networks and 50\% improvement in private training of gradient boosting decision trees.

  匹配依据：MPC: oblivious transfer

  </details>

- **SCE-NTT: A Hardware Accelerator for Number Theoretic Transform Using Superconductor Electronics**
  2025-08-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.21265)
  Sasan Razmkhah, Mingye Li, Zeming Cheng, Robert S. Aviles, Kyle Jackman, Joey Delport, Lieze Schindler, Wenhui Luo, Takuya Suzuki, Mehdi Kamal, Christopher L. Ayala, Coenrad J. Fourie, Nabuyuki Yoshikawa, Peter A. Beerel, Sandeep Gupta, Massoud Pedram

  <details><summary>摘要 / Abstract</summary>

  This research explores the use of superconductor electronics (SCE) for accelerating fully homomorphic encryption (FHE), focusing on the Number-Theoretic Transform (NTT), a key computational bottleneck in FHE schemes. We present SCE-NTT, a dedicated hardware accelerator based on superconductive single flux quantum (SFQ) logic and memory, targeting high performance and energy efficiency beyond the limits of conventional CMOS. To address SFQ constraints such as limited dense RAM and restricted fanin/fanout, we propose a deeply pipelined NTT-128 architecture using shift register memory (SRM). Designed for N=128 32-bit coefficients, NTT-128 comprises log2(N)=7 processing elements (PEs), each featuring a butterfly unit (BU), dual coefficient memories operating in ping-pong mode via FIFO-based SRM queues, and twiddle factor buffers. The BU integrates a Shoup modular multiplier optimized for a small area, leveraging precomputed twiddle factors. A new RSFQ cell library with over 50 parameterized cells, including compound logic units, was developed for implementation. Functional and timing correctness were validated using JoSIM analog simulations and Verilog models. A multiphase clocking scheme was employed to enhance robustness and reduce path-balancing overhead, improving circuit reliability. Fabricated results show the NTT-128 unit achieves 531 million NTT/sec at 34 GHz, over 100x faster than state-of-the-art CMOS equivalents. We also project that the architecture can scale to larger sizes, such as a 2^14-point NTT in approximately 482 ns. Key-switch throughput is estimated at 1.63 million operations/sec, significantly exceeding existing hardware. These results demonstrate the strong potential of SCE-based accelerators for scalable, energy-efficient secure computation in the post-quantum era, with further gains anticipated through advances in fabrication.

  匹配依据：MPC: secure computation

  </details>

- **Enhanced Rényi Entropy-Based Post-Quantum Key Agreement with Provable Security and Information-Theoretic Guarantees**
  2025-08-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2509.00104)
  Ruopengyu Xu, Chenglian Liu

  <details><summary>摘要 / Abstract</summary>

  This paper presents an enhanced post-quantum key agreement protocol based on Rényi entropy, addressing vulnerabilities in the original construction while preserving information-theoretic security properties. We develop a theoretical framework leveraging entropy-preserving operations and secret-shared verification to achieve provable security against quantum adversaries. Through entropy amplification techniques and quantum-resistant commitments, the protocol establishes $2^{128}$ quantum security guarantees under the quantum random oracle model. Key innovations include a confidentiality-preserving verification mechanism using distributed polynomial commitments, tightened min-entropy bounds with guaranteed non-negativity, and composable security proofs in the quantum universal composability framework. Unlike computational approaches, our method provides information-theoretic security without hardness assumptions while maintaining polynomial complexity. Theoretical analysis demonstrates resilience against known quantum attack vectors, including Grover-accelerated brute force and quantum memory attacks. The protocol achieves parameterization for 128-bit quantum security with efficient $\mathcal{O}(n^{2})$ communication complexity. Extensions to secure multiparty computation and quantum network applications are established, providing a foundation for long-term cryptographic security.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Privacy-Preserving Two-Party RBF Kernel SVM Training Based on Neat and Accurate Secure Exponentiation**
  2025-08-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1537)
  Qingyu Mo, Wenyuan Wu, Jingwei Chen

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving machine learning (PPML) is a powerful tool for multiple parties to collaboratively train a model or perform model inference without exposing their private data in the context of Internet of things. A key challenge in PPML is the efficient evaluation of non-polynomial functions. In this work, we propose NASE, a neat and accurate secure exponentiation protocol for radius basis function (RBF) kernel evaluation. Leveraging the property of the RBF kernel, NASE enjoys a lightweight construction that reduces computation overhead by up to 1.65$\times$ and communication overhead by up to 3.97$\times$ compared to SIRNN, the prior SOTA framework for secure exponentiation published in IEEE S\&amp;P 2021. Taking NASE as the foundation stone, we propose a privacy-preserving two-party kernel SVM training protocol. Based on BFV scheme and MPC technique, we introduce group-batch sampling for sampling in ciphertext and propose the partial rotation method tailored to our scenario to optimize dot product computation. Additionally, we propose an error-tolerant $DReLU$ protocol for secure sign evaluation of secret sharings over a prime field that reduces the communication cost by around $\frac{1}{3}$ compared to the existing method. Our protocol achieves model accuracy comparable to plaintext training according to experiments on real-world datasets, and an order-of-magnitude reduction in both communication and computation overhead is attained compared to the previous work.

  匹配依据：MPC: mpc (context)

  </details>

- **Evaluating Ascon in Secure Multi-Party Computation using Reverse Multiplication-Friendly Embeddings**
  2025-08-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1538)
  Peter Schwarz, Erik Pohle, Aysajan Abidin, Bart Preneel

  <details><summary>摘要 / Abstract</summary>

  We present the first systematic study on communication-efficient evaluation of the lightweight cipher family Ascon within secure multi-party computation (MPC). By leveraging Ascon’s parallel, bit-oriented structure, we adapt its design using Reverse Multiplication-Friendly Embeddings (RMFEs, introduced by Cascudo et al.\ in CRYPTO&#x27;18) in a single-circuit evaluation, enabling efficient packing of groups of bits into field elements. Our protocol, which uses relatively small RMFEs, achieves substantial reductions in communication cost compared to baseline MPC protocols. For example, in a medium-sized setting (with $n = 13$ MPC parties), our protocol reduces the communication cost for an Ascon permutation by roughly $38\%$. For large amounts of parties (e.g., $n=255$), the reduction can reach $50\%$. These improvements are achieved even though RMFEs only pack a few bits per field element, due to favorable amortization of both substitution and linear layers. We also provide a Boolean circuit implementation of Ascon in the MP-SPDZ framework, enabling straightforward benchmarking. Our findings are particularly beneficial for bandwidth-constrained environments where the use of lightweight ciphers, such as Ascon, is necessary due to the resource limitations of client devices, as in the case of transciphering data from IoT sensors. Since our optimizations target the Ascon permutation, they naturally extend to all cryptographic modes (encryption, decryption, hashing) defined for the standard.

  匹配依据：MPC: secure multi party computation

  </details>

- **Breaking the Layer Barrier: Remodeling Private Transformer Inference with Hybrid CKKS and MPC**
  2025-08-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.19525) · [IACR ePrint](https://eprint.iacr.org/2025/1532)
  Tianshi Xu, Wen-jie Lu, Jiangrui Yu, Chen Yi, Chenqi Lin, Runsheng Wang, Meng Li, Yi Chen

  <details><summary>摘要 / Abstract</summary>

  This paper presents an efficient framework for private Transformer inference that combines Homomorphic Encryption (HE) and Secure Multi-party Computation (MPC) to protect data privacy. Existing methods often leverage HE for linear layers (e.g., matrix multiplications) and MPC for non-linear layers (e.g., Softmax activation functions), but the conversion between HE and MPC introduces significant communication costs. The proposed framework, dubbed BLB, overcomes this by breaking down layers into fine-grained operators and further fusing adjacent linear operators, reducing the need for HE/MPC conversions. To manage the increased ciphertext bit width from the fused linear operators, BLB proposes the first secure conversion protocol between CKKS and MPC and enables CKKS-based computation of the fused operators. Additionally, BLB proposes an efficient matrix multiplication protocol for fused computation in Transformers. Extensive evaluations on BERT-base, BERT-large, and GPT2-base show that BLB achieves a $21\times$ reduction in communication overhead compared to BOLT (S\&amp;P&#x27;24) and a $2\times$ reduction compared to Bumblebee (NDSS&#x27;25), along with latency reductions of $13\times$ and $1.8\times$, respectively, when leveraging GPU acceleration.

  匹配依据：MPC: secure multi party computation

  </details>

- **SecureV2X: An Efficient and Privacy-Preserving System for Vehicle-to-Everything (V2X) Applications**
  2025-08-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.19115)
  Joshua Lee, Ali Arastehfard, Weiran Liu, Xuegang Ban, Yuan Hong

  <details><summary>摘要 / Abstract</summary>

  Autonomous driving and V2X technologies have developed rapidly in the past decade, leading to improved safety and efficiency in modern transportation. These systems interact with extensive networks of vehicles, roadside infrastructure, and cloud resources to support their machine learning capabilities. However, the widespread use of machine learning in V2X systems raises issues over the privacy of the data involved. This is particularly concerning for smart-transit and driver safety applications which can implicitly reveal user locations or explicitly disclose medical data such as EEG signals. To resolve these issues, we propose SecureV2X, a scalable, multi-agent system for secure neural network inferences deployed between the server and each vehicle. Under this setting, we study two multi-agent V2X applications: secure drowsiness detection, and secure red-light violation detection. Our system achieves strong performance relative to baselines, and scales efficiently to support a large number of secure computation interactions simultaneously. For instance, SecureV2X is $9.4 \times$ faster, requires $143\times$ fewer computational rounds, and involves $16.6\times$ less communication on drowsiness detection compared to other secure systems. Moreover, it achieves a runtime nearly $100\times$ faster than state-of-the-art benchmarks in object detection tasks for red light violation detection.

  匹配依据：MPC: secure computation

  </details>

- **Universally Composable Treatment of Multi-Party Isomorphic State Channels**
  2025-08-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1517)
  Maxim Jourenko, Xiangyu Su, Adam Blatchley Hansen, Mario Larangeira

  <details><summary>摘要 / Abstract</summary>

  Layer-2 protocols are pivotal in enhancing the scalability of blockchain systems, enabling faster off-chain transactions while maintaining security. These protocols can bridge consensus-based blockchain systems and advanced applications, such as Multiparty Computation (MPC) protocols, often defined within the Universal Composability (UC) Framework. However, despite the existence of some UC-defined protocols, there is currently no comprehensive UC definition for isomorphic multiparty state channels, in particular that are not dependent on the ledger model: account or UTxO based ledger. These protocols depend heavily on timelock mechanisms and the accurate representation of time, which are challenging to model within the UC Framework. Our work addresses this gap by proposing a UC-based definition, i.e., functionality, for isomorphic multi-party state channels that realistically model timely actions of honest users, a critical feature for the security of the channel protocol. Moreover our definition is agnostic with respect to the ledger model. Additionally, we introduce an extended timelock-aided global ledger functionality and demonstrate the security of existing protocols, namely Hydra proposed by Chakravarty et al. (FC&#x27;21), under the UC Framework and our proposed functionalities. This contribution provides a robust foundation for developing secure and scalable off-chain protocols in blockchain ecosystems. Finally, we concretely provide the construction of the extension of the Hydra Protocol, only outlined by the original work, and also prove it secure under our framework.

  匹配依据：MPC: multiparty computation

  </details>

- **Mosformer: Maliciously Secure Three-Party Inference Framework for Large Transformers**
  2025-08-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1510)
  Ke Cheng, Yuheng Xia, Anxiao Song, Jiaxuan Fu, Wenjie Qu, Yulong Shen, Jiaheng Zhang

  <details><summary>摘要 / Abstract</summary>

  Transformer-based models like BERT and GPT have achieved state-of-the-art performance across a wide range of AI tasks but raise serious privacy concerns when deployed as cloud inference services. To address this, secure multi-party computation (MPC) is commonly employed, encrypting both user inputs and model parameters to enable inference without revealing any private information. However, existing MPC-based secure transformer inference protocols are predominantly designed under the semi-honest security model. Extending these protocols to support malicious security remains a significant challenge, primarily due to the substantial overhead introduced by securely evaluating complex non-linear functions required for adversarial resilience. We introduce Mosformer, the first maliciously secure three-party (3PC) inference framework that efficiently supports large transformers such as BERT and GPT. We first design constant-round comparison and lookup table protocols with malicious security, leveraging verifiable distributed point functions (VDPFs). Building on these, we develop a suite of 3PC protocols for efficient and secure evaluation of complex non-linear functions in transformers. Together with optimized modulus conversion, our approach substantially reduces the overhead of secure transformer inference while preserving model accuracy. Experimental results on the vanilla transformer block show that Mosformer achieves up to a $5.3\times$ speedup and a $4.3\times$ reduction in communication over prior maliciously secure protocols. Despite offering stronger security guarantees, Mosformer achieves comparable or even superior online performance to state-of-the-art semi-honest 2PC and 3PC frameworks, including BOLT (Oakland 2024), BumbleBee (NDSS 2025), SHAFT (NDSS 2025), and Ditto (ICML 2024), on full-scale models such as BERT and GPT-2.

  匹配依据：MPC: secure evaluation, secure multi party computation

  </details>

- **Concretely Efficient Fluid MPC with Linear Communication**
  2025-08-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1508)
  Yubo Zeng, Kang Yang, Dengguo Feng, Min Zhang

  <details><summary>摘要 / Abstract</summary>

  Traditional Secure Multi-Party Computation (MPC) requires parties to stay online through the whole computation, which compromises scalability when dealing with large-scale and complex tasks. The notion of fluid MPC, introduced by Choudhuri et al. (Crypto 2021), aims to address this challenge by presenting a dynamic participation model where parties have the flexibility to join and leave as needed. The best-known honest-majority MPC protocol by Bienstock et al. (Crypto 2023) in the fluid setting achieves linear communication complexity, but still incurs a substantially higher communication overhead than MPC in the classical setting. In this paper, we present two concretely efficient fluid MPC protocols in the honest-majority setting. The first, Velora, is an unconditionally secure maximal-fluid MPC protocol, which achieves the lowest communication cost among maximally fluid MPC protocols by introducing a new approach of transferring the output sharings held by the current committee to the next committee. To eliminate the inherent overhead of Velora, we also propose a separation-generation approach for random double sharings and integrate it into the second protocol as Ion. As a trade-off, Ion relaxes the fluidity requirement to the submaximal fluidity, allowing an extra internal communication round for each committee. Both protocols Velora and Ion enable us to extend the ATLAS technique from the classical setting to the fluid setting for further lowering communication overhead. Compared to the best-known fluid MPC protocol, our protocols reduce the communication cost per multiplication gate by a factor of 5.4 ∼ 7.5× (resp., 20.7 ∼ 28×) for semi-honest security (resp., malicious security). Compared to the state-of-the-art ATLAS protocol by Goyal et al. (Crypto 2021) in the classical setting, our semi-honest protocols only introduce a 1 ∼ 1.5× larger communication overhead for securely computing multiplication gates.

  匹配依据：MPC: secure multi party computation

  </details>

- **Evolving k-Threshold Visual Cryptography Schemes**
  2025-08-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.15917)
  Xiaoli Zhuo, Xuehu Yan, Lintao Liu, Wei Yan

  <details><summary>摘要 / Abstract</summary>

  In evolving access structures, the number of participants is countably infinite with no predetermined upper bound. While such structures have been realized in secret sharing, research in secret image sharing has primarily focused on visual cryptography schemes (VCS). However, there exists no construction for $(k,\infty)$ VCS that applies to arbitrary $k$ values without pixel expansion currently, and the contrast requires enhancement. In this paper, we first present a formal mathematical definition of $(k,\infty)$ VCS. Then, propose a $(k,\infty)$ VCS based on random grids that works for arbitrary $k$. In addition, to further improve contrast, we develop optimized $(k,\infty)$ VCS for $k=2$ and $3$, along with contrast enhancement strategies for $k\geq 4$. Theoretical analysis and experimental results demonstrate the superiority of our proposed schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Ransomware Negotiation: Dynamics and Privacy-Preserving Mechanism Design**
  2025-08-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.15844)
  Haohui Zhang, Sirui Shen, Xinyu Hu, Chenglu Jin

  <details><summary>摘要 / Abstract</summary>

  Ransomware attacks have become a pervasive and costly form of cybercrime, causing tens of millions of dollars in losses as organizations increasingly pay ransoms to mitigate operational disruptions and financial risks. While prior research has largely focused on proactive defenses, the post-infection negotiation dynamics between attackers and victims remains underexplored. This paper presents a formal analysis of attacker-victim interactions in modern ransomware incidents using a finite-horizon alternating-offers bargaining game model. Our analysis demonstrates how bargaining alters the optimal strategies of both parties. In practice, incomplete information-attackers lacking knowledge of victims&#x27; data valuations and victims lacking knowledge of attackers&#x27; reservation ransoms-can prolong negotiations and increase victims&#x27; business interruption costs. To address this, we design a Bayesian incentive-compatible mechanism that facilitates rapid agreement on a fair ransom without requiring either party to disclose private valuations. We further implement this mechanism using secure two-party computation based on garbled circuits, thereby eliminating the need for trusted intermediaries and preserving the privacy of both parties throughout the negotiation. To the best of our knowledge, this is the first automated, privacy-preserving negotiation mechanism grounded in a formal analysis of ransomware negotiation dynamics.

  匹配依据：MPC: garbled circuits, secure two party computation

  </details>

- **Efficient and Verifiable Privacy-Preserving Convolutional Computation for CNN Inference with Untrusted Clouds**
  2025-08-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.12832)
  Jinyu Lu, Xinrong Sun, Yunting Tao, Tong Ji, Fanyu Kong, Guoqiang Yang

  <details><summary>摘要 / Abstract</summary>

  The widespread adoption of convolutional neural networks (CNNs) in resource-constrained scenarios has driven the development of Machine Learning as a Service (MLaaS) system. However, this approach is susceptible to privacy leakage, as the data sent from the client to the untrusted cloud server often contains sensitive information. Existing CNN privacy-preserving schemes, while effective in ensuring data confidentiality through homomorphic encryption and secret sharing, face efficiency bottlenecks, particularly in convolution operations. In this paper, we propose a novel verifiable privacy-preserving scheme tailored for CNN convolutional layers. Our scheme enables efficient encryption and decryption, allowing resource-constrained clients to securely offload computations to the untrusted cloud server. Additionally, we present a verification mechanism capable of detecting the correctness of the results with a success probability of at least $1-\frac{1}{\left|Z\right|}$. Extensive experiments conducted on 10 datasets and various CNN models demonstrate that our scheme achieves speedups ranging $26 \times$ ~ $\ 87\times$ compared to the original plaintext model while maintaining accuracy.

  匹配依据：MPC: secret sharing

  </details>

- **AuthenTree: A Scalable MPC-Based Distributed Trust Architecture for Chiplet-based Heterogeneous Systems**
  2025-08-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.13033)
  Ishraq Tashdid, Tasnuva Farheen, Sazadur Rahman

  <details><summary>摘要 / Abstract</summary>

  The rapid adoption of chiplet-based heterogeneous integration is reshaping semiconductor design by enabling modular, scalable, and faster time-to-market solutions for AI and high-performance computing. However, multi-vendor assembly in post-fabrication environments fragments the supply chain and exposes SiP systems to serious security threats, including cloning, overproduction, and chiplet substitution. Existing authentication solutions depend on trusted integrators or centralized security anchors, which can expose sensitive data or create single points of failure. We introduce AuthenTree, a distributed authentication framework that leverages multi-party computation (MPC) in a scalable tree-based architecture, removing the need for dedicated security hardware or centralized trust. AuthenTree enables secure chiplet validation without revealing raw signatures, distributing trust across multiple integrator chiplets. Our evaluation in five SiP benchmarks demonstrates that AuthenTree imposes minimal overhead, with an area as low as 0.48% (7,000 sq-micrometers), an overhead power under 0.5%, and an authentication latency below 1 microsecond, surpassing previous work in some cases by 700 times. These results establish AuthenTree as an efficient, robust, and scalable solution for next-generation chiplet-based security in zero-trust SiP environments.

  匹配依据：MPC: multi party computation

  </details>

- **Towards Building Efficient SCALES Protocols**
  2025-08-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1487)
  Anasuya Acharya, Carmit Hazay, Vladimir Kolesnikov, Manoj Prabhakaran

  <details><summary>摘要 / Abstract</summary>

  SCALES (Small Clients And Larger Ephemeral Servers) (Acharya et al., TCC 2022, CRYPTO 2024) is a recently proposed model for MPC with several attractive features, including resilience to adaptive corruption. Known SCALES constructions, while offering reasonable asymptotics for large-scale MPC, incur high concrete costs both in computation and communication. As our primary contribution, we dramatically improve both asymptotic and concrete costs of SCALES for permutation branching programs (PBP), a well-motivated practical model of computation. We achieve linear cost in program length, input size, and the security parameter. Our instantiations of the building blocks may be of independent interest. Further, we present generic transformations to extend any semi-honestly secure SCALES protocol to achieve (1) guaranteed output delivery in the presence of mixed adversaries (that corrupt servers maliciously and clients semi-honestly) in the all-but-one corruption setting; and (2) protocols for computing general functionalities where each server&#x27;s computation scales sub-linearly in the function~size.

  匹配依据：MPC: mpc (context)

  </details>

- **CryptPEFT: Efficient and Private Neural Network Inference via Parameter-Efficient Fine-Tuning**
  2025-08-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.12264)
  Saisai Xia, Wenhao Wang, Zihao Wang, Yuhui Zhang, Yier Jin, Dan Meng, Rui Hou

  <details><summary>摘要 / Abstract</summary>

  Publicly available large pretrained models (i.e., backbones) and lightweight adapters for parameter-efficient fine-tuning (PEFT) have become standard components in modern machine learning pipelines. However, preserving the privacy of both user inputs and fine-tuned adapters -- often trained on sensitive data -- during inference remains a significant challenge. Applying cryptographic techniques, such as multi-party computation (MPC), to PEFT settings still incurs substantial encrypted computation across both the backbone and adapter, mainly due to the inherent two-way communication between them. To address this limitation, we propose CryptPEFT, the first PEFT solution specifically designed for private inference scenarios. CryptPEFT introduces a novel one-way communication (OWC) architecture that confines encrypted computation solely to the adapter, significantly reducing both computational and communication overhead. To maintain strong model utility under this constraint, we explore the design space of OWC-compatible adapters and employ an automated architecture search algorithm to optimize the trade-off between private inference efficiency and model utility. We evaluated CryptPEFT using Vision Transformer backbones across widely used image classification datasets. Our results show that CryptPEFT significantly outperforms existing baselines, delivering speedups ranging from $20.62\times$ to $291.48\times$ in simulated wide-area network (WAN) and local-area network (LAN) settings. On CIFAR-100, CryptPEFT attains 85.47% accuracy with just 2.26 seconds of inference latency. These findings demonstrate that CryptPEFT offers an efficient and privacy-preserving solution for modern PEFT-based inference.

  匹配依据：MPC: multi party computation

  </details>

- **Glock: Garbled Locks for Bitcoin**
  2025-08-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1485)
  Liam Eagen

  <details><summary>摘要 / Abstract</summary>

  Bitcoin is a decentralized, permissionless network for digital payments. Bitcoin also supports a limited set of smart contracts, which restrict how bitcoin can be spent, through bitcoin script. In order to support more expressive scripting functionality, Robin Linus introduced the BitVM family of protocols. These implement a weaker form of ``optimistic&quot; smart contracts, and for the first time allowed bitcoin to verify arbitrary computation. BitVM allows a challenger to publish a ``fraud proof&quot; that the computation was carried out incorrectly which can be verified on chain, even when the entire computation cannot. Jermey Rubin introduced an alternative optimistic smart contract protocol called Delbrag. This protocol uses Garbled Circuits (GC) to replace the BitVM fraud proof with by simply revealing a secret. He also introduced the Grug technique for malicious security. We introduce a new formalization of GC based optimistic techniques called Garbled Locks or Glocks. Much like Delbrag, we use the GC to leak a secret and produce a signature as a fraud proof. We further propose the first concretely practical construction that does not require Grug. Like BitVM2 and Delbrag, Glock25 reduces verification of arbitrary bounded computation to verification of a SNARK. In Glock25, we use a designated verifier version of a modified of the SNARK Pari with smaller proof size. We make Glock25 maliciously secure using a combination of Cut-and-Choose, Verifiable Secret Sharing (VSS), and Adaptor Signatures. These techniques reduce the communication, computational, and on-chain complexity of the protocol compared to other approaches to construct a Glock, e.g. based on Groth16.

  匹配依据：MPC: garbled circuits, secret sharing

  </details>

- **Complex Elections via Threshold (Fully) Homomorphic Encryption**
  2025-08-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1482)
  Charlotte Bonte, Georgio Nicolas, Nigel P. Smart

  <details><summary>摘要 / Abstract</summary>

  We discuss how Fully Homomorphic Encryption (FHE), and in particular the TFHE scheme, can be used to define an e-voting scheme for the Alternative Vote (AV) election system. This system has a more complex tallying phase than traditional First-Past-The-Post (FPTP) election variants. Previous work on e-voting schemes that used homomorphic encryption has focused on FPTP systems only, and utilized mainly linearly homomorphic encryption. We show, by using FHE, that more complex electoral systems such as AV can also be supported by homomorphic encryption. We show security of our protocol by considering it as a simple MPC functionality, and we also show practicality by presenting some experimental runtimes using the tfhe-rs library.

  匹配依据：MPC: mpc (context)

  </details>

- **Stateless 2PC Signatures for Internet-Scale Authentication and Authorization**
  2025-08-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1475)
  Michael Adjedj, Geoffroy Couteau, Arik Galansky, Nikolaos Makriyannis, Oren Yomtov

  <details><summary>摘要 / Abstract</summary>

  The industry is moving away from passwords for authentication and authorization, with hardware devices for storing long-term cryptographic keys emerging as the leading alternative. However, these devices often have limited displays and remain vulnerable to theft, malware, or tricking users into signing malicious payloads. Current systems provide little fallback security in such cases. Any solution must also meet strict requirements: compatibility with industry standards, scalability to handle high request volumes, and high availability. We present a novel design for authentication and authorization that meets these demands. Our approach virtualizes the authenticating/authorizing party via a two-party signing protocol with a helper entity, ensuring that keys remain secure even if a device is compromised and that every signed message conforms to a security policy. We formalize the required properties for such protocols and show how they are met by existing schemes (e.g., FROST for Schnorr, Boneh–Haitner–Lindell-Segev&#x27;25 for ECDSA). Motivated by the widespread use of ECDSA (FIDO2/Passkeys, blockchains), we introduce a new, optimized two-party ECDSA protocol that is significantly more efficient than prior work. At its core is a new variant of exponent-VRF, improving on earlier constructions and of independent interest. We validate our design with a proof-of-concept virtual authenticator for the FIDO2 Passkeys framework.

  匹配依据：MPC: 2pc (context)

  </details>

- **PicoGRAM: Practical Garbled RAM from Decisional Diffie-Hellman**
  2025-08-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1479) · [Code](https://github.com/picogramimpl/picogram)
  Tianyao Gu, Afonso Tinoco, Sri Harish G Rajan, Elaine Shi

  <details><summary>摘要 / Abstract</summary>

  Making 2-party computation scale up to big datasets is a long-cherished dream of our community. More than a decade ago, a line of work has implemented and optimized interactive RAM-model 2-party computation (2PC), achieving somewhat reasonable concrete performance on large datasets, but unfortunately suffering from $\widetilde{O}(T)$ roundtrips for a $T$-time computation. Garbled RAM promises to compress the number of roundtrips to $2$, and encouragingly, a line of recent work has designed concretely efficient Garbled RAM schemes whose asymptotic communication and computation costs almost match the best known interactive RAM-model 2PC, but still leaves $({\sf poly})\log\log$ gaps. We present ${\sf PicoGRAM}$, a practical garbled RAM (GRAM) scheme that not only asymptotically matches the prior best RAM-model 2PC, but also achieves an order of magnitude concrete improvement in online time relative to interactive RAM-model 2PC, on a dataset of size $8$GB. Moreover, our work also gives the first Garbled RAM whose total cost (including bandwidth and computation) achieves an optimal dependency on the database size (up to an arbitrarily small super-constant factor). Our work shows that for high-value real-life applications such as Signal, blockchains, and Meta that require oblivious accesses to large datasets, Garbled RAM is a promising direction towards eventually removing the trusted hardware assumption that exist in production implementations today. Our open source code is available at https://github.com/picogramimpl/picogram.

  匹配依据：MPC: 2 party computation

  </details>

- **Surpassing the PLOB bound in continuous-variable quantum secret sharing using a state-discrimination detector**
  2025-08-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.09445)
  Qin Liao, Chong Tang, Qingquan Peng, Chao Ding, Lingjin Zhu, Yijun Wang, Xiquan Fu

  <details><summary>摘要 / Abstract</summary>

  Continuous-variable quantum secret sharing (CVQSS) is a promising approach to ensuring multi-party information security. While CVQSS offers practical ease of implementation, its present performance remains limited. In this paper, we propose a novel CVQSS protocol integrated with a state-discrimination detector (SDD), dubbed SDD-CVQSS. In particular, we first develop the detailed procedure of SDD-CVQSS, which replaces the traditional coherent detector with an SDD and eliminates the long-standing necessary step of establishing multiple point-to-point quantum key distribution links between all users and the dealer. We then elaborate on the principle of the specifically designed SDD, which can efficiently discriminate mixed states with a much lower error probability. Finally, we construct a security model for SDD-CVQSS and derive its security bound against beam-splitting collective attacks. Numerical simulations show that SDD-CVQSS outperforms conventional CVQSS in both maximum transmission distance and secret key rate, even surpassing the PLOB bound. Additionally, we find that the performance degradation of SDD-CVQSS in long-distance transmission scenarios can be effectively compensated for using a post-selection scheme, providing a feasible way to achieve high-performance CVQSS.

  匹配依据：MPC: secret sharing

  </details>

- **Succinct Oblivious Tensor Evaluation and Applications: Adaptively-Secure Laconic Function Evaluation and Trapdoor Hashing for All Circuits**
  2025-08-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.09673) · [IACR ePrint](https://eprint.iacr.org/2025/336)
  Damiano Abram, Giulio Malavolta, Lawrence Roy

  <details><summary>摘要 / Abstract</summary>

  We propose the notion of succinct oblivious tensor evaluation (OTE), where two parties compute an additive secret sharing of a tensor product of two vectors $\mathbf{x} \otimes \mathbf{y}$, exchanging two simultaneous messages. Crucially, the size of both messages and of the CRS is independent of the dimension of $\mathbf{x}$. We present a construction of OTE with optimal complexity from the standard learning with errors (LWE) problem. Then we show how this new technical tool enables a host of cryptographic primitives, all with security reducible to LWE, such as: * Adaptively secure laconic function evaluation for depth-$D$ functions $f:\{0, 1\}^m\rightarrow\{0, 1\}^\ell$ with communication $m+\ell+D\cdot \mathrm{poly}(λ)$. * A trapdoor hash function for all functions. * An (optimally) succinct homomorphic secret sharing for all functions. * A rate-$1/2$ laconic oblivious transfer for batch messages, which is best possible. In particular, we obtain the first laconic function evaluation scheme that is adaptively secure from the standard LWE assumption, improving upon Quach, Wee, and Wichs (FOCS 2018). As a key technical ingredient, we introduce a new notion of \emph{adaptive lattice encodings}, which may be of independent interest.

  匹配依据：MPC: oblivious transfer, secret sharing

  </details>

- **Efficient Fuzzy Labeled PSI from Vector Ring-OLE**
  2025-08-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1470)
  Dung Bui, Kelong Cong

  <details><summary>摘要 / Abstract</summary>

  Fuzzy-labeled private set intersection (PSI) outputs the corresponding label if there is a ``fuzzy&#x27;&#x27; match between two items, for example, when the Hamming distance is low between the two items. Such protocols can be applied in privacy-preserving biometric authentication, proximity testing, and so on. The only fuzzy-labeled PSI protocol designed for practical purposes is by Uzun et al. (USENIX’21), which is based on homomorphic encryption. This design puts constraints on the item size, label size, and communication cost since it is difficult for homomorphic encryption to support large plaintext space and it is well-known that the ciphertext-expansion factor is large. Our construction begins with a new primitive which we call vector ring-oblivious linear evaluation (vector ring-OLE). This primitive does not rely on existing instantiations of ring-OLE over the quotient ring, but leverages the more efficient vector-OLE. It is ideal for building unbalanced threshold-labeled PSI and is also of independent interest. Our main contribution, fuzzy-labeled PSI, is bootstrapped from our threshold-labeled PSI protocol. Through a prototype implementation, we demonstrate our communication cost is up to $4.6\times$ better than the prior state-of-the-art with comparable end-to-end latency while supporting a significantly higher label size.

  匹配依据：MPC: private set intersection

  </details>

- **Rumors MPC: GOD for Dynamic Committees, Low Communication via Constant-Round Chat**
  2025-08-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1464)
  Bernardo David, Arup Mondal, Rahul Satish

  <details><summary>摘要 / Abstract</summary>

  Constructing MPC with ephemeral committees has gained a lot of attention since the seminal works on Fluid MPC and YOSO MPC (CRYPTO&#x27;21). However, most protocols in this setting focus on the extreme case of ephemeral committees who can only act for one round (i.e., the maximally fluid case). The Layered MPC model (CRYPTO&#x27;23) recasts this notion as a protocol execution against an adaptive rushing adversary over a layered interaction graph, where each committee sits on a layer and can only communicate with the immediate next committee. Although protocols with abort allow for linear communication complexity (CRYPTO&#x27;23, CiC&#x27;24), Perfect Layered MPC with guaranteed output delivery (GOD) and its statistically secure counterpart (TCC&#x27;24) suffer from $O(n^9)$ and $O(\kappa n^{18})$ communication complexity for $n$ parties per committee, respectively. In this work, we investigate communication complexity improvements gained in a relaxed Multi-Layered MPC model that allows for limited interaction among the parties in each committee, while still allowing only one round to communicate towards the immediate next committee. We construct Rumors MPC protocols, where the interaction among each committee&#x27;s members is constant-round. Our protocols achieve GOD and optimal corruption threshold in the perfect (resp. statistical) security setting with committees acting for $\delta=5$ (resp. $\delta=13$) rounds and $O(n^6)$ (resp. $O(\kappa n^8)$) communication.

  匹配依据：MPC: mpc (context)

  </details>

- **Privacy-Preserving Machine Learning on Web Browsing for Public Opinion**
  2025-08-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1468)
  Sam Buxbaum, Lucas M. Tassis, Lucas Boschelli, Giovanni Comarela, Mayank Varia, Mark Crovella, Dino P. Christenson

  <details><summary>摘要 / Abstract</summary>

  We present a real-world deployment of secure multiparty computation to predict political preference from private web browsing data. To estimate aggregate preferences for the 2024 U.S. presidential election candidates, we collect and analyze secret-shared data from nearly 8000 users from August 2024 through February 2025, with over 2000 daily active users sustained throughout the bulk of the survey. The use of MPC allows us to compute over sensitive web browsing data that users would otherwise be more hesitant to provide. We collect data us- ing a custom-built Chrome browser extension and perform our analysis using the CrypTen MPC library. To our knowledge, we provide the first implementation under MPC of a model for the learning from label pro- portions (LLP) problem in machine learning, which allows us to train on unlabeled web browsing data using publicly available polling and elec- tion results as the ground truth. The client code is open source, and the remaining code will be open source in the future.

  匹配依据：MPC: secure multiparty computation

  </details>

- **VOIDFace: A Privacy-Preserving Multi-Network Face Recognition With Enhanced Security**
  2025-08-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.07960) · [Code](https://github.com/ajnasmuhammed89/VOIDFace)
  Ajnas Muhammed, Iurri Medvedev, Nuno Gonçalves

  <details><summary>摘要 / Abstract</summary>

  Advancement of machine learning techniques, combined with the availability of large-scale datasets, has significantly improved the accuracy and efficiency of facial recognition. Modern facial recognition systems are trained using large face datasets collected from diverse individuals or public repositories. However, for training, these datasets are often replicated and stored in multiple workstations, resulting in data replication, which complicates database management and oversight. Currently, once a user submits their face for dataset preparation, they lose control over how their data is used, raising significant privacy and ethical concerns. This paper introduces VOIDFace, a novel framework for facial recognition systems that addresses two major issues. First, it eliminates the need of data replication and improves data control to securely store training face data by using visual secret sharing. Second, it proposes a patch-based multi-training network that uses this novel training data storage mechanism to develop a robust, privacy-preserving facial recognition system. By integrating these advancements, VOIDFace aims to improve the privacy, security, and efficiency of facial recognition training, while ensuring greater control over sensitive personal face data. VOIDFace also enables users to exercise their Right-To-Be-Forgotten property to control their personal data. Experimental evaluations on the VGGFace2 dataset show that VOIDFace provides Right-To-Be-Forgotten, improved data control, security, and privacy while maintaining competitive facial recognition performance. Code is available at: https://github.com/ajnasmuhammed89/VOIDFace

  匹配依据：MPC: secret sharing

  </details>

- **MUSE-VFL: Multi-party Unified System for Private and Communication Efficient Backpropagation in Vertical Federated Learning**
  2025-08-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1451)
  Ivan Tjuawinata, Yann Fraboni, Ziyao Liu, Jun Zhao, Pu Duan, Kwok-Yan Lam

  <details><summary>摘要 / Abstract</summary>

  Vertical federated learning (VFL) enables a cohort of parties with vertically partitioned data to collaboratively train a machine learning (ML) model without requiring them to centralise their data. Each party feeds its data to its local model, with output fed to a global model. However, this configuration requires parties to share some intermediary results during training, which include the output and the gradients of the local models. These intermediary results can reveal insights into the parties&#x27; data, and can be protected by secret sharing them with secure multiparty computation (MPC). However, this increases the total number of communications and makes the VFL training significantly slower. In this work, we introduce MUSE-VFL to accelerate the computation of the local gradients by using homomorphic encryption on top of MPC for parties to directly complete this computation during backpropagation. We show theoretically that MUSE-VFL improves the complexity of the MPC baseline. Our experiments, conducted on four different ML tasks, show that the runtime needed to compute the gradients of the local models significantly outweighs the combined runtime of all other steps. This highlights the significance of MUSE-VFL, with experiments demonstrating a training runtime faster by 30% to 35% for LAN and 32% to 50% for WAN.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **DOC★: Access Control for Information-Theoretically Secure Key-Document Stores**
  2025-08-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1457)
  Yin Li, Sharad Mehrota, Shantanu Sharma, Komal Kumari

  <details><summary>摘要 / Abstract</summary>

  This paper presents a novel key-based access control technique for secure outsourcing key-value stores where values correspond to documents that are indexed and accessed using keys. The proposed approach adopts Shamir’s secret-sharing that offers unconditional or information-theoretic security. It supports keyword-based document retrieval while preventing leakage of the data, access rights of users, or the size (i.e., volume of the output that satisfies a query). The proposed approach allows servers to detect (and abort) malicious clients from gaining unauthorized access to data, and prevents malicious servers from altering data undetected while ensuring efficient access – it takes 231.5ms over 5,000 keywords across 500,000 files

  匹配依据：MPC: secret sharing

  </details>

- **Shuffling is Universal: Statistical Additive Randomized Encodings for All Functions**
  2025-08-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1442)
  Nir Bitansky, Saroja Erabelli, Rachit Garg, Yuval Ishai

  <details><summary>摘要 / Abstract</summary>

  The shuffle model is a widely used abstraction for non-interactive anonymous communication. It allows $n$ parties holding private inputs $x_1,\dots,x_n$ to simultaneously send messages to an evaluator, so that the messages are received in a random order. The evaluator can then compute a joint function $f(x_1,\dots,x_n)$, ideally while learning nothing else about the private inputs. The model has become increasingly popular both in cryptography, as an alternative to non-interactive secure computation in trusted setup models, and even more so in differential privacy, as an intermediate between the high-privacy, little-utility local model and the little-privacy, high-utility central curator model. The main open question in this context is which functions $f$ can be computed in the shuffle model with statistical security. While general feasibility results were obtained using public-key cryptography, the question of statistical security has remained elusive. The common conjecture has been that even relatively simple functions cannot be computed with statistical security in the shuffle model. We refute this conjecture, showing that all functions can be computed in the shuffle model with statistical security. In particular, any differentially private mechanism in the central curator model can also be realized in the shuffle model with essentially the same utility, and while the evaluator learns nothing beyond the central model result. This feasibility result is obtained by constructing a statistically secure additive randomized encoding (ARE) for any function. An ARE randomly maps individual inputs to group elements whose sum only reveals the function output. Similarly to other types of randomized encoding of functions, our statistical ARE is efficient for functions in $NC^1$ or $NL$. Alternatively, we get computationally secure ARE for all polynomial-time functions using a one-way function. More generally, we can convert any (information-theoretic or computational) ``garbling scheme&#x27;&#x27; to an ARE with a constant-factor size overhead.

  匹配依据：MPC: garbling scheme, secure computation

  </details>

- **Secure Protocols for Best Arm Identification Using Secret Sharing Schemes**
  2025-08-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1438)
  Shanuja Sasi, Asaf Cohen, Onur Günlü

  <details><summary>摘要 / Abstract</summary>

  This paper addresses the challenge of best arm identification in stochastic multi-armed bandit (MAB) models under privacy-preserving constraints, such as in dynamic spectrum access networks where secondary users must privately detect underutilized channels. While previous network security research has explored securing MAB algorithms through techniques such as homomorphic encryption or differential privacy, these methods often suffer from high computational overhead or introduce noise that strictly decreases accuracy. In contrast, this work focuses on lightweight solutions that ensure data confidentiality without compromising the accuracy of best arm identification. We introduce two secure protocols that leverage additive secret sharing and threshold secret sharing. The proposed model, employing aggregation nodes and a comparator node, securely distributes computations to prevent any entity from accessing complete reward or ranking data. Furthermore, the protocol ensures resistance to collusion and fault tolerance, while maintaining computational efficiency. These contributions establish a scalable and robust framework for privacy-preserving best arm identification, offering practical and secure solutions that use MAB methods for network security.

  匹配依据：MPC: secret sharing

  </details>

- **Efficient Mediated Multiparty Semi-Quantum Secret Sharing Protocol Based on Single-Qubit Reordering**
  2025-08-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.05487)
  Mustapha Anis Younes, Sofia Zebboudj, Abdelhakim Gharbi

  <details><summary>摘要 / Abstract</summary>

  Typical multiparty semi-quantum secret sharing (MSQSS) protocols require the dealer to possess full quantum capabilities, while the classical users usually need to perform three operations. To address this practical limitation, this paper introduces a new mediated MSQSS protocol that enables Alice, a classical user, to share a secret with $M$ classical Bobs, with the assistance of an untrusted third party (TP) who may attempt any possible attack to steal Alice&#x27;s secret. Furthermore, the classical participants require only two capabilities instead of three, namely: (a) performing measurements in the $Z$ basis; and (b) reordering qubits. The proposed scheme offers significant advantages over existing mediated QSS protocols: (1) it is the first mediated SQSS protocol to adopt single qubits, instead of entangled states, as the quantum resource, which makes it more practical and easier to implement; (2) It achieves higher qubit efficiency. Security analysis also demonstrates that the protocol is secure against well-known attacks.

  匹配依据：MPC: secret sharing

  </details>

- **TLShare: Private Authenticated MPC and FHE Inputs Over TLS**
  2025-08-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1434)
  Manuel B. Santos, Dimitris Mouris, Xiang Xie, Miguel de Vega, Andrei Lapets

  <details><summary>摘要 / Abstract</summary>

  Transport Layer Security (TLS) is the backbone of the web, allowing clients to establish secure and private channels with servers. DECO (CCS&#x27;20) and follow-up works proposed protocols that enable proving the provenance of a TLS response, i.e., that a payload came from a particular server, without needing server-side modifications. Unfortunately, these works are limited to proving Boolean statements over the payload (e.g., age $\ge$ 18) and cannot combine payloads from multiple clients. We introduce TLShare, a framework that extracts authenticated data from a TLS connection and imports it into secure multiparty computation (MPC) or fully homomorphic encryption (FHE), without requiring server-side changes or exposing client credentials. Unlike prior work, TLShare allows the payload itself, not just a predicate about it, to serve as private input to secure downstream computation. TLShare supports combining verifiable inputs across multiple clients and servers, enabling new applications such as privacy-preserving financial risk assessment and collaborative analytics. We design three protocols for TLShare: one for MPC using verifiable secret sharing, and two for FHE using interactive and non-interactive zero-knowledge proofs, each ensuring input authenticity, integrity, and end-to-end privacy. We evaluate all three protocols of TLShare over both LAN and WAN settings, comparing their trade-offs and demonstrating their practicality.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Absolutely maximally entangled pure states of multipartite quantum systems**
  2025-08-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.04777)
  Grzegorz Rajchel-Mieldzioć, Rafał Bistroń, Albert Rico, Arul Lakshminarayan, Karol Życzkowski

  <details><summary>摘要 / Abstract</summary>

  Absolutely maximally entangled (AME) pure states of a system composed of $N$ parties are distinguished by the property that for any splitting at least one partial trace is maximally mixed. Due to maximal possible correlations between any two selected subsystems these states have numerous applications in various fields of quantum information processing including multi-user teleportation, quantum error correction and secret sharing. We present an updated survey of various techniques to generate such strongly entangled states, including those going beyond the standard construction of graph and stabilizer states. Our contribution includes, in particular, analysis of the degree of entanglement of reduced states obtained by partial trace of AME projectors, states obtained by a symmetric superposition of GHZ states, an orthogonal frequency square representation of the &quot;golden&quot; AME state and an updated summary of the number of local unitary equivalence classes.

  匹配依据：MPC: secret sharing

  </details>

- **A Fully-Adaptive Threshold Partially-Oblivious PRF**
  2025-08-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1433)
  Ruben Baecker, Paul Gerhart, Daniel Rausch, Dominique Schröder

  <details><summary>摘要 / Abstract</summary>

  Oblivious Pseudorandom Functions (OPRFs) are fundamental cryptographic primitives essential for privacy-enhancing technologies such as private set intersection, oblivious keyword search, and password-based authentication protocols. We present the first fully adaptive, partially oblivious threshold pseudorandom function that supports proactive key refresh and provides composable security under the One-More Gap Diffie-Hellman assumption in the random oracle model. Our construction is secure with respect to a new ideal functionality for OPRFs that addresses three critical shortcomings of previous models–specifically, key refresh and non-verifiability issues that rendered them unrealizable. In addition, we identify a gap in a prior work&#x27;s proof of partial obliviousness and develop a novel proof technique to salvage their scheme.

  匹配依据：MPC: private set intersection

  </details>

- **Frequency subspace encoding for multiplexed quantum secret sharing**
  2025-08-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.03295)
  Meritxell Cabrejo-Ponce, Christopher Spiess, Carlos Sevilla-Gutiérrez, Fabian Steinlechner

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) is a multi-party quantum communication protocol that can be realized with bipartite entanglement and relative phase encoding. Previous implementations typically encoded the phase in the pump, applying it across the entire source bandwidth, thereby limiting scalability via wavelength multiplexing. In contrast, we present a variant of the standard QSS protocol that leverages frequency correlations to connect multiple users with a single source. The secret owner, who has access to the source, encodes classical information by applying frequency-dependent phase modulation to a broadband polarization-entangled photon pair. Each frequency channel therefore provides an independent QSS session among the secret owner and a pair of users. We demonstrate state fidelities of at least 90% for a channel pair of the 200 GHz ITU grid, which could be extended to more than 40 frequency bins with adequate dense-wavelength division multiplexed filters. Our results provide a resource-efficient path toward multi-user secret sharing over wavelength-multiplexed networks, eliminating the need for multiple two-photon or multi-photon sources.

  匹配依据：MPC: secret sharing

  </details>

- **Collusion-Safe Proxy Re-Encryption**
  2025-08-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1423)
  Haotian Yin, Jie Zhang, Wanxin Li, Yuji Dong, Eng Gee Lim, Dominik Wojtczak

  <details><summary>摘要 / Abstract</summary>

  Proxy re-encryption is a cryptographic scheme enabling a delegator (user $i$) to delegate its decryption right to a valid delegatee (user $j$) through a proxy, who cannot extract any information about the message during the procedure. An important security notion is the security against collusion between the proxy and the delegatee. In this case, the adversary has the secret key of the delegatee, $\mathsf{sk}_j$, and the re-encryption key, $\mathsf{rk}_{i\to j}$. The master secret security is first formalised by Ateniese et al. (NDSS&#x27;05) to capture the secrecy of $i$&#x27;s secret key during collusion. This notion was further formalised by Zhou et al. (ASIACRYPT&#x27;23) as the indistinguishability of re-encrypted ciphertext against chosen-message attacks, called collusion safety, which implies the master secret security. In this paper, we find that a PRE scheme is not master secret secure as they claimed, and many other schemes were not master secret secure. Then, we propose a generic construction to achieve collusion safety at the cost of doubling the key size from the IND-CPA secure PRE, enjoying a much better generality and efficiency than the existing technique by secret sharing.

  匹配依据：MPC: secret sharing

  </details>

- **Efficient randomized strong $2$-source non-malleable extractor for any linear min-entropy**
  2025-08-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1421)
  Divesh Aggarwal, Pranjal Dutta, Saswata Mukherjee, Satyajeet Nagargoje, Maciej Obremski

  <details><summary>摘要 / Abstract</summary>

  Randomness is a fundamental requirement in cryptographic systems, enabling secure encryption, commitments, and zero-knowledge proofs. However, real-world randomness sources often suffer from weaknesses that adversaries can exploit, leading to significant security vulnerabilities. While deterministic randomness extraction from a single min-entropy source is impossible, two-source extractors provide a robust solution by generating nearly uniform randomness from two independent weak sources. Moreover, cryptographic systems must also be resilient to leakage and tampering attacks, necessitating the development of non-malleable two-source extractors. In this work, we construct a two-source non-malleable extractor in the Common Reference String (CRS) model, where a random low-degree polynomial is sampled once and made accessible to independent random sources, the distinguisher, and the tamperer. Our extractor requires only linear min-entropy in both sources and doesn&#x27;t rely on strong computational assumptions, in contrast to prior constructions requiring computational assumptions such as sub-exponential hardness of the Decisional Diffie-Hellman (DDH) problem. Notably, our construction builds upon and relies on the recent breakthrough proof of the polynomial Freiman-Ruzsa conjecture. A connection of the Freiman-Ruzsa conjecture with two-source extractors was considered in prior work [ZBS11],[AGMR24], but their construction did not achieve non-malleability. Our results advance the state of non-malleable cryptographic primitives, with applications in secure storage, leakage-resilient cryptography, and privacy amplification. By eliminating the need for strong computational hardness assumptions, our techniques provide a more foundational and widely applicable method for randomness extraction. We also show, that the requirements on CRS for our application are so mild that the CRS can be sampled with $2$ party computation even when one of the parties is malicious (setting in which establishing unbiased coins is impossible).

  匹配依据：MPC: 2 party computation

  </details>
