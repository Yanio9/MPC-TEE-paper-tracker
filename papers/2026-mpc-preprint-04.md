# 2026 · MPC · 仅预印本来源 · 第 4/6 页

[总目录](../PAPERS.md) · [上一页](2026-mpc-preprint-03.md) · [下一页](2026-mpc-preprint-05.md)

- **Beyond the Canonical Protocol: Quantum Encrypted Cloning from Secret-Sharing Access Structures**
  2026-06-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.06552)
  Gabriele Gianini, Stelvio Cimato, Jianyi Lin, Omar Hasan, Corrado Mio, Ernesto Damiani

  <details><summary>摘要 / Abstract</summary>

  Quantum encrypted cloning shows that an unknown quantum state can be distributed into multiple encrypted copies without contradicting the no-cloning theorem: each copy is unusable on its own, but can be redeemed together with a suitable quantum key. Recent work has related canonical encrypted-cloning protocols to particular forms of quantum secret sharing. Here we take the converse perspective: instead of mapping a given encrypted-cloning protocol into QSS, we use QSS access structures as a design library from which encrypted-cloning schemes can be extracted. The criterion is access-structural. A QSS scheme supports a quantum encrypted-cloning structure whenever it contains a family of qualified sets with a non-qualified common intersection. The common subsystem is interpreted as the key, while the non-common parts are interpreted as encrypted clones relative to that key. Thus quantum encrypted cloning does not require a new notion of recoverability beyond QSS; what changes is the operational reading of QSS constituents as a mechanism for delayed and alternative redemption opportunities. This viewpoint separates redemption from perfect secrecy. Perfect QSS yields encrypted-cloning schemes with forbidden non-qualified subsystems, whereas ramp QSS naturally allows intermediate, partially informative non-redeeming subsystems. The resulting framework broadens quantum encrypted cloning from a specific protocol to a general access-structure primitive. We illustrate the extraction principle with threshold-like, ramp, hierarchical, and compartmented architectures, showing how encrypted clones may be symmetric or asymmetric, individual or composite, perfectly hidden or leaky. Equivalently, these constructions can be viewed as overlapping erasure-recovery regions of an isometric quantum code. This establishes secret sharing as a systematic design language for encrypted quantum redundancy.

  匹配依据：MPC: secret sharing

  </details>

- **To Catch a Cheater: Some notes on the malicious (in)security of ORQ**
  2026-06-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1152)
  Eli Baum

  <details><summary>摘要 / Abstract</summary>

  Malicious-secure multiparty computation protocols protect against an adversary&#x27;s arbitrary misbehavior. In the honest-majority four-party setting, one common technique relies on all communication between parties being duplicated. Under this approach, all correct messages are sent twice, while corrupted messages are only sent by the adversary and will not match concurrent correct messages. When a receiver observes that inconsistency, it announces cheating has occurred (and possibly aborts). Existing implementations often optimize this procedure by batching many such checks into a single hash and running a final consistency check just before revealing the result of a computation. Brüggemann and Schneider (Eurocrypt 2026) recently showed that these delayed consistency checks in honest-majority, malicious-secure protocols can violate privacy. Adversaries can introduce errors such that subsequent incorrect hashes reveal their missing secret share and allow plaintext secrets to be recovered just before the honest parties abort. Their suggested fix evaluates the hash comparison under multiparty computation, rather than in plaintext. In this report, we detail our fix for the Fantastic Four protocol in ORQ, a recent system for secure analytics that is vulnerable to the attack. The new implementation has a modest overhead that amortizes with larger inputs. The complexity of the modified protocol highlights the difficulty of implementing malicious-secure systems in practice; even seemingly harmless optimizations can break privacy.

  匹配依据：MPC: multiparty computation, secure multiparty computation

  </details>

- **Constant-Round Interactive Consistency in Dishonest Majority, or with Quadratic Communication in Honest Majority**
  2026-06-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1146)
  Pierre Civit, Grigorii Emdin, Rachid Guerraoui

  <details><summary>摘要 / Abstract</summary>

  We present the first constant-expected-latency protocols for Interactive Consistency (IC), also known as Parallel Byzantine Broadcast, that achieve either: (1) security in dishonest majority, namely $t \leq (1-\varepsilon)n$ for any constant $\varepsilon\in \Omega(1)$; or (2) quadratic communication $O\!\left(n^2(L_{in}+\kappa)\right)$ in honest majority (i.e., $\varepsilon &gt;1/2$). In IC, $n$ processes must agree on a vector that maps every honest process to its input of size $L_{in}$, despite up to $t$ dishonest (Byzantine) processes that may collude and behave arbitrarily. IC is the strongest one-shot distributed task: by fully determining the honest input configuration, it subsumes every other solvable one-shot task in the same model. Moreover, most multiparty computation protocols rely on IC as a building block. These guarantees are qualitatively optimal. First, Garay, Katz, Koo, and Ostrovsky (FOCS~2007) rule out constant-round protocols unless the honest fraction is constant. Second, Pease, Shostak, and Lamport (JACM~1980) rule out setup-free information-theoretic solutions once $n\leq 3t$. Thus, to overcome this barrier, we rely on cryptographic objects of size $\kappa$, obtaining correctness with all but negligible probability in $\kappa$ against any adversary running in time polynomial in $\kappa$. This includes digital signatures, for which the corresponding public keys must be published on a bulletin-board public key infrastructure before the protocol begins. Third, IC trivially requires \(\Omega(n^2L_{in})\) communication, since every honest process must learn the inputs of all honest processes. Our results follow from a single generic compiler that transforms any constant-expected-latency Byzantine Broadcast protocol into an IC protocol with the same latency profile.

  匹配依据：MPC: multiparty computation

  </details>

- **Threshold Signatures in the Head**
  2026-06-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1125)
  Thibauld Feneuil, Matthieu Rivain, Damien Vergnaud, Auguste Warmé-Janville

  <details><summary>摘要 / Abstract</summary>

  Threshold cryptography distributes trust among multiple parties by enabling joint cryptographic operations without reconstructing secret keys. While post-quantum signature schemes based on the MPC-in-the-Head (MPCitH) paradigm are highly generic, recent impossibility results show that their thresholdization either incurs prohibitive distributed symmetric computations or leads to signature sizes growing with the number of signers. Achieving practical tradeoffs in this setting remains challenging. In this paper, we propose a generic framework for threshold MPCitH signatures based on Merkle-tree commitments. Our approach adapts the PIOP+PCS paradigm to the distributed setting by introducing and instantiating the notion of threshold polynomial commitment schemes (TPCS). We present a generic compiler combining a PIOP, a TPCS, and an arithmetic black box into a threshold signature scheme, and prove its unforgeability from the security of its components. We further provide a concrete Merkle-tree-based TPCS achieving moderate signature-size overhead, as low as 200 bytes per signer at the 128-bit security level. This is to be compared with an overhead of roughly 2 kB per signer for the previously suggested approach to thresholdize MPC-in-the-Head based on GGM trees. By compiling this TPCS with a standard PIOP, we obtain a generic threshold signature scheme from any hard problem or one-way function, which we showcase MQ-based and AES-based instantiations.

  匹配依据：MPC: mpc (context)

  </details>

- **Oblivious Garbling and its Applications**
  2026-06-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1132)
  Tomer Ashur, Carmit Hazay, Rahul Satish

  <details><summary>摘要 / Abstract</summary>

  A garbling scheme encodes a function and an input into two independent artifacts from which the output can be recovered, but nothing else is revealed. This clean separation between function and input has made garbling one of the most versatile primitives in cryptography. Yet it hides an asymmetry that has gone largely unexamined: while the input is cryptographically protected, the function is fully exposed to whoever performs the garbling. As garbling is increasingly deployed in settings where garbling is delegated to untrusted infrastructure, published on public ledgers, or distributed among multiple parties, this asymmetry becomes a fundamental barrier. The function, which may encode proprietary models, confidential policies, or sensitive decision logic, is leaked unconditionally to the garbling server. We introduce oblivious garbling, a new paradigm that closes this gap. In our framework, the garbler receives only a designated leakage of the circuit and remains oblivious to everything else. We present the first construction instantiating this notion where the leakage is the circuit topology alone, achieving linear complexity with no blow-up in the size of the garbled circuit. The construction extends to the malicious setting with no asymptotic overhead. Beyond its theoretical contribution, oblivious garbling has immediate practical consequences: it enables outsourced garbling without function exposure, garbling on untrusted hardware without leaking proprietary logic, and a multi-party garbling protocol in which no garbling party learns the function, all without resorting to universal circuits.

  匹配依据：MPC: garbled circuit, garbling protocol, garbling scheme

  </details>

- **I-(OT)^2: A Client-optimal Oblivious Transfer Protocol for IoT Devices**
  2026-06-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.02344)
  Elia Onofri, Andrea Ciccotelli, Roberto Di Pietro

  <details><summary>摘要 / Abstract</summary>

  Oblivious Transfer (OT) is a fundamental cryptographic primitive enabling privacy-preserving computation and constitutes a core building block for secure multi-party computation while supporting a wide range of security-sensitive applications: private information retrieval, zero-knowledge proofs, and password-authenticated key exchange, to cite a few. While recent advances in OT extension have significantly reduced amortised costs, their reliance on batches of random base OTs and substantial pre-computation phases limits their practicality in scenarios where the number of transfers is modest or where communication latency and client-side computation are critical constraints. In such settings, efficient base OT protocols remain both relevant and necessary. In this work, we introduce $I$-$(OT)^2$, a novel base 1-out-of-2 OT protocol grounded in the quadratic residuosity problem, specifically designed to minimise receiver-side computation and interaction. Our construction is particularly appealing on client--server architectures in which the receiver operates on low-power hardware, such as Internet of Things (IoT) devices. Through a lightweight offline pre-computation phase, $I$-$(OT)^2$ shifts the on-transfer computational burden almost entirely to the Sender, while reducing online communication to only six messages and four digests exchanged. We provide a detailed description of the protocol, accompanied by a formal proof of its security. Moreover, to demonstrate the viability of $I$-$(OT)^2$, we also present an open-source proof-of-concept implementation (in C language) evaluated on real IoT hardware. Results are staggering: for 128-bit security using a 3072-bit RSA modulus, the receiver incurs an average online cost per OT as low as 2.80 μs on desktop platforms and 39.90 μs on IoT devices, more than 10$\times$ faster than the well known SimplestOT.

  匹配依据：MPC: oblivious transfer, secure multi party computation

  </details>

- **An Explicit Scott-Type Bound for Absolutely Maximally Entangled States with Arbitrary Defect**
  2026-06-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.01943)
  Shixuan Zeng, Xiande Zhang

  <details><summary>摘要 / Abstract</summary>

  Absolutely maximally entangled (AME) states and, more generally, $k$-uniform states in $(\C^q)^{\otimes n}$ are central objects in multipartite entanglement theory, with applications to quantum secret sharing, quantum masking, and quantum error correction. In the extremal case $k=\lfloor n/2\rfloor$, Scott (2004) proved a sharp nonexistence bound showing that AME states cannot exist once the number of parties $n$ exceeds a threshold of order $2q^{2}$ (with a parity dependence on $n$), where $q$ is the local dimension. Recently, Ning et al.\ studied \emph{defective} AME states (i.e., $k=\lfloor n/2\rfloor-l$ with $l&gt;0$), gave explicit Scott-type bounds for defects $l=1,2$ and conjectured a general $(2l+2)q^{2}+o(q^{2})$ behavior. In this paper, we solve this conjecture and establish a fully explicit Scott-type upper bound for AME states with arbitrary defect $l\ge 0$, yielding Scott&#x27;s bound for $l=0$ and Ning et al.&#x27;s bounds for $l=1,2$ as special cases. Equivalently, this gives nonexistence bounds for one-dimensional pure quantum error-correcting codes near the quantum Singleton regime. The proof uses a truncated MacWilliams linear-programming system and an explicit infeasibility certificate. As a direct application, we derive explicit asymptotic upper bounds on $k/n$ for fixed local dimension $q$, improving the implicit upper bounds given by Ning et al.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Smart Surveillance with Cross-Dataset Violence Detection and Decentralized Evidence Governance**
  2026-05-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.01225)
  Hasan Coşkun, Furkan Çolhak, Andrea Kulakov, Vesna Dimitrova

  <details><summary>摘要 / Abstract</summary>

  AI-enabled surveillance can accelerate public-safety response, yet most systems still leave recorded evidence under centralized administrative control. This paper proposes a privacy-preserving smart surveillance framework that separates incident detection from evidence disclosure. A lightweight MobileNetV2-based video classifier detects violent clips, while each recorded incident segment is immediately encrypted and made accessible only through threshold-based approval. The decryption key is split with Shamir&#x27;s Secret Sharing, member shares are protected with public-key cryptography, and voting is supported by time-limited tokens, two-factor authentication, signatures, and audit logs. This study evaluates MobileNetV2+LSTM, MobileNetV2+BiLSTM, and MobileNetV2+temporal CNN heads on SCVD, RWF-2000, and Real-Life Violence Situations under seven in-domain and cross-dataset scenarios. The best all-source model, MobileNetV2+BiLSTM, reaches 93.5% test accuracy and ROC-AUC 0.980% on the merged held-out set, while lower RWF-2000 slice performance confirms persistent dataset shift.

  匹配依据：MPC: secret sharing

  </details>

- **Packed Pre-Constructed PVSS for Randomness Generation and E-Voting**
  2026-05-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1119)
  Karim Baghery, Eleftheria Makri, Dheeraj Kumar Suryakari

  <details><summary>摘要 / Abstract</summary>

  Pre-constructed Publicly Verifiable Secret Sharing (PPVSS) extends conventional Publicly Verifiable Secret Sharing (PVSS) by requiring the dealer to publish a commitment or encryption of the shared secret, enabling more efficient and versatile constructions for a variety of cryptographic protocols. In this paper, we further enhance this paradigm by introducing Packed Pre-constructed PVSS (3PVSS), which allows a dealer to encode multiple secrets within a single polynomial while maintaining the pre-constructability property. We present two constructions of 3PVSS schemes. In the first construction, the dealer publishes a single commitment to all shared secrets, providing a compact representation that is particularly suitable for applications requiring efficient communication. In the second construction, the dealer publishes individual commitments to each secret, enabling greater flexibility in applications that require independent verification of multiple shared values. Both schemes preserve the key advantages of PPVSS, including the optimistic reconstruction approach enabled by pre-constructability. We demonstrate that these two variants naturally support different applications. Using the first 3PVSS construction, we revisit the ALBATROSS randomness generation protocol proposed by Cascudo and David (ASIACRYPT 2020) and present a more efficient variant with reduced computation and communication costs. As an application of the second construction, we extend the universally verifiable e-voting protocol recently proposed by Baghery, Knapen, Nicolas, and Rahimi (ACNS 2025) to support multi-candidate elections, while preserving universal verifiability. Our results show that the resulting protocols outperform their original counterparts in terms of efficiency.

  匹配依据：MPC: secret sharing

  </details>

- **A Comparative Evaluation of End-to-End-Encrypted Key Retrieval in Backup Protocols**
  2026-05-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1108)
  Dennis Funke, Kai Gellert

  <details><summary>摘要 / Abstract</summary>

  End-to-end encryption (E2EE) provides strong confidentiality guarantees to users by preventing service providers from accessing their data. At the same time, it introduces new operational challenges, most notably the restoration of an E2EE-protected backup on a new device after loss of the original device. In recent years, major instant messengers have deployed increasingly sophisticated key-retrieval schemes for encrypted backups, ranging from simple recovery codes to designs that depend on trusted hardware or advanced cryptographic primitives such as oblivious pseudorandom functions (OPRFs), threshold OPRFs, and secret sharing. While recent work has largely emphasized stronger cryptographic guarantees, the practical costs and trust assumptions implied by hardware dependencies and complex primitives are often not made explicit. We present a structured framework for the comparative evaluation of E2EE backup key-retrieval schemes across usability, deployability, and security properties, and apply it to simple recovery codes, real-world deployments, and recent proposals from the literature, explicitly distinguishing recovery that depends on user-chosen low-entropy secrets from recovery using high-entropy material. Our evaluation shows that schemes whose recovery ultimately relies on user-chosen low-entropy secrets can provide substantially weaker resistance against large-scale adversaries than an approach using simple recovery codes. Even when assuming high-entropy recovery secrets, many recovery protocol designs introduce additional trust assumptions and potential single points of failure (e.g., compromise of specialized components or trusted setups) that can amplify the impact of large-scale adversaries. Overall, our results highlight that added system complexity often trades off against limited security gains under realistic threat models, motivating clearer accounting of cost and distribution of trust in future designs.

  匹配依据：MPC: secret sharing

  </details>

- **Tail-Hammer: Optimized Statistics for Anonymous Committees and Applications**
  2026-05-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1101)
  Bernardo David, Lucia Lavagnino, Elena Pagnin, Paul Stankovski Wagner

  <details><summary>摘要 / Abstract</summary>

  Techniques to randomly select sets of anonymous parties are ubiquitous in efficient and adaptively secure consensus protocols, as well as in Multi-Party Computation in the YOSO model, where each round is executed by a different random anonymous committee. Anonymous committee selection aims at randomly selecting a set of $n$ parties (the committee), where at most $t$ parties are corrupted (except with negligible probability), drawing from a population of $N \gg n$ parties with at most $T$ corrupted parties. Additionally, each party knows (and can prove) if they belong to the committee, but ignores other members&#x27; identities. A very common and efficient instantiation of anonymous committee selection is to select parties according to a VRF output, this however, leads to committees of probabilistic size ($n$ behaves as a Binomial random variable). Despite wide adoption, only Blum et al. (CCS23) provides an analysis of VRF-based probabilistic anonymous committee selection that estimates the size of committees. This analysis relies on lose bounds (Chernoff) and approximations (Poisson). In this work, we revisit Blum et al.&#x27;s estimates and derive accurate closed-form formulas (based on a tight Binomial approximation), as well as an efficient high-precision library called Tail-Hammer for computing exact parameters. Notably, Tail-Hammer identifies smaller committee sizes (approximately -25% on average) than Blum et al. (CCS23) for the same security level, leading to improved efficiency in protocols relying on random committee selection, also when anonymity is not needed. Our analysis applies to committee selection techniques that employ unbiased (uniformly random), or bounded-bias randomness, to both synchronous and asynchronous communication settings, and it can account for inactive parties. As a new application, we present a verifiable consistent broadcast protocol that leverages quorums in anonymous committees to achieve efficiency without requiring threshold signatures.

  匹配依据：MPC: multi party computation

  </details>

- **Key Transport over Untrusted QKD Relay Networks**
  2026-05-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1095)
  Sebastian Clermont, Antoine Gansel, Patrick Struck

  <details><summary>摘要 / Abstract</summary>

  Quantum key distribution (QKD) enables the exchange of information-theoretically secure symmetric keys, but is fundamentally limited in range. Existing long-distance QKD networks rely on trusted relay nodes, any one of which can compromise the entire key. We propose a key-transport protocol that removes this trust assumption by combining proactive secret sharing with one-time pad encryption over pairwise QKD links. At each layer of relay nodes, shares are reshared so that corruptions across different layers cannot be combined; security depends only on the maximum number of corruptions within any single layer, not on the total number of corrupted nodes. We formalize a game-based security model for layered secret transport, identify a cross-layer attack that affects a prior construction, and prove our protocol information-theoretically secure against a semi-honest adversary corrupting up to $t{-}1$ nodes per layer.

  匹配依据：MPC: secret sharing

  </details>

- **Dishonest Majority Multi-Party Arithmetic Garbling with Constant Rate**
  2026-05-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1105)
  Tianyao Gu, Hanjun Li, Elaine Shi

  <details><summary>摘要 / Abstract</summary>

  Minimizing round complexity is a central goal in secure Multi-Party Computation (MPC), particularly for deployment on high-latency networks. While constant-round protocols with concrete efficiency have been constructed, they are typically designed for Boolean circuits and each gate incurs a bandwidth cost linear in the security parameter. Moreover, for arithmetic-heavy applications such as privacy-preserving machine learning and statistical analysis, compiling arithmetic operations into Boolean gates incurs another substantial overhead in circuit size and communication. Conversely, existing arithmetic MPC protocols, such as SPDZ, require interaction rounds proportional to the circuit depth, imposing significant latency. In this work, we bridge this gap by presenting the first concretely-efficient maliciously-secure MPC protocol that achieves both constant-round and constant-rate communication, where the rate is defined as the bandwidth cost per party divided by the number of gates and the size of the values each gate operates on. Our protocol computes over bounded integers and is secure against a static, malicious adversary corrupting up to $n-1$ parties. The protocol is built upon the arithmetic garbling framework of Ball et al. (Eurocrypt 2023) and follows the BMR template, assuming the Decisional Composite Residuosity for the garbling phase and Learning Parity with Noise for preprocessing. We evaluate our protocol on matrix-vector multiplication, a fundamental operation for data analysis. For standard computation parameters, we reduce communication bandwidth by $101\times$ to $247\times$ and improves end-to-end runtime by $4.4\times$ to $10.7\times$ compared to state-of-the-art constant-round Boolean MPC baselines, even when accounting for the overhead of a full bit-decomposition on the output vector.

  匹配依据：MPC: secure multi party computation

  </details>

- **Adaptively Secure (Aggregatable) PVSS from Standard Assumptions**
  2026-05-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1100)
  Renas Bacho, Yanbo Chen, Julian Loss

  <details><summary>摘要 / Abstract</summary>

  Publicly verifiable secret sharing (PVSS) is a fundamental primitive in threshold cryptography that allows a dealer to share a secret $S$ among a set of $n$ parties via a publicly verifiable transcript. Any subset of $t+1$ parties can then use their individual shares to reconstruct the full secret $S$, whereas $t$ or fewer shares give no information about $S$. As such, the secret $S$ remains hidden from an adversary that corrupts up to $t$ parties. Recently, Bacho and Loss (CCS 2023) gave the first proof of any PVSS scheme under an adaptive adversary. However, their security proof relies on strong and non-standard assumptions such as the algebraic group model (AGM) and the hardness of the one-more discrete logarithm (OMDL) problem. In particular, any protocol (e.g., distributed randomness beacon or distributed key generation) that makes use of a PVSS scheme either inherits these limitations or is not provably adaptively secure. In this work, we present for the first time an adaptively secure PVSS scheme from well-established assumptions. In more detail, we provide two PVSS schemes with different properties. Our first scheme works over any pairing-free cyclic group and its security relies on the decisional Diffie-Hellman (DDH) assumption. Our second scheme works over an asymmetric pairing group, its security relies on the DDH and the co-computational Diffie-Hellman (co-CDH) assumption, and has the particularly valuable feature of aggregatability, which allows the aggregation of multiple PVSS transcripts into a single transcript while preserving verifiability. Notably, both our schemes are highly efficient, non-interactive, and work in the established plain public key model. These properties along with their provable adaptive security make them suitable candidates as building block in higher-level distributed protocols that aim to minimize communication.

  匹配依据：MPC: secret sharing

  </details>

- **Witness Pseudorandom Functions for Vector Commitments and Applications**
  2026-05-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1079)
  Rishabh Bhadauria, Pedro Branco, Nico Döttling, Sanjam Garg, Guru-Vamsi Policharla

  <details><summary>摘要 / Abstract</summary>

  A witness pseudorandom function (WPRF) is a PRF which has an additional mode of public evaluation. Given the public key, it can be evaluated publicly if one provides a valid NP witness for that input, while the output remains pseudorandom to anyone without such a witness. WPRFs are powerful objects, and general-purpose constructions are currently only known from assumptions that imply indistinguishability obfuscation. In this work, we construct a WPRF for a specific language related to the Libert-Yung vector commitment (TCC 2010). More specifically, public evaluation of the WPRF on an input is possible if a valid local opening for that input is provided. Our construction relies only on standard assumptions on pairing groups and is fully black-box. We further show that this primitive enables us to solve several open problems in the study of communication-efficient secure computation: - Rate-1 Laconic Oblivious Transfer. We construct a laconic oblivious transfer protocol with total communication complexity $2k+\mathsf{poly}(\lambda)$ for $k$ executions. Previously, achieving this efficiency required non-falsifiable assumptions such as evasive LWE (Wee, CRYPTO&#x27;24). - Near-optimal Laconic Private Set Intersection. We construct laconic private set intersection for which the amortized communication complexity approaches $\lambda$ bits per element in the sender&#x27;s set (assuming each set element is represented by $\lambda$ bits) and is independent of the receiver&#x27;s set. This is within a constant factor of the information-theoretic lower bound. - Rate-1 Batch Registration-Based Encryption. We construct a registration-based encryption scheme in which, when the encryptor sends multiple messages to multiple receivers, the ciphertext overhead is only two group elements.

  匹配依据：MPC: oblivious transfer, private set intersection, secure computation

  </details>

- **Self-Guarding Arbitrary Cryptographic Primitives and 2PC Protocols**
  2026-05-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1068)
  Daniele Friolo, Andrea Reale, Daniele Venturi

  <details><summary>摘要 / Abstract</summary>

  In IEEE CSF &#x27;18, Fischlin and Mazaheri introduced the notion of self-guarding cryptographic protocols as a countermeasure to algorithm substitution attacks. After a trusted initialization phase, a Self-Guarder wraps the user&#x27;s cryptographic algorithm implementation and sanitizes it in a way that (1) prevents that an adversary can exploit the subverted implementation to exfiltrate user&#x27;s data and (2) maintain the correctness of the genuine implementation. Whilst the proposed solutions in CSF &#x27;18 support a bounded number of executions before requiring a re-initialization phase, we show a universal self-guarder supporting an unbounded number of executions from a single trusted setup. Our self-guarder can be applied to any cryptographic primitive and any two-party computation protocol in the stand-alone setting with the aid of a verifiable-computation-enabling compiler.

  匹配依据：MPC: two party computation

  </details>

- **Proactive Secret Sharing without Erasures**
  2026-05-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1072)
  Alexandru Cojocaru, Aggelos Kiayias, Yu Shen, Petros Wallden

  <details><summary>摘要 / Abstract</summary>

  Proactive secret-sharing (PSS) offers security for shared secrets in a setting of a mobile adversary which, over time, may corrupt the whole shareholder set. This remarkable property is achieved by having parties proactively and in a coordinated manner refresh their shares on a regular basis, while it assumes that the adversary never manages to corrupt more than a threshold number of parties between two consecutive share refresh operations. A common assumption for achieving PSS is the ability of parties to securely erase their private state once they have performed the refresh operation. Motivated by the difficulty in the real world to ensure secure erasure, we investigate whether it is possible to achieve PSS without erasures. As in the classic model of computation it can be easily shown that PSS without erasures is impossible, we hence ask whether it is possible to achieve PSS via quantum computation, while still requiring only classical communication. We answer the question in the affirmative by utilizing one-shot signatures and post-quantum classical extractable witness encryption. In the process of developing our result, we define and construct threshold one-shot decryption and make connections to quantum money with classical communication both of which may be of independent interest. Finally, we show how, by combining post-quantum secure functional witness encryption with our PSS, it is possible for the secret to be used without explicitly being reconstructed, something that paves the way towards proactively secure threshold cryptography without erasures.

  匹配依据：MPC: secret sharing

  </details>

- **Post-Quantum Security of Practical Correlation-Robust Hashing**
  2026-05-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1064)
  Akinori Hosoyamada, Haruhisa Kosuge, Keita Xagawa

  <details><summary>摘要 / Abstract</summary>

  Correlation-robust (CR) hashing and its variants are central components in efficient secure-computation protocols, including OT extension, garbled-circuit optimizations such as Free-XOR and half-gates, and GGM-style tree constructions. In practice, these hashes are typically instantiated from block ciphers such as AES. Prominent constructions include the Matyas-Meyer-Oseas (MMO) construction and its variants such as \(\widehat{\mathsf{MMO}}\). Existing analyses, however, are classical and do not cover quantum adversaries with superposition access to the underlying random permutation or ideal cipher. We establish post-quantum security for these practical block-cipher-based CR hashes. In the quantum ideal cipher model (QICM), we prove multi-user tweakable correlation robustness with leakage (mTCRL) for the MMO construction, and multi-user tweakable circular correlation robustness with leakage (mTCCRL) for \(\widehat{\mathsf{MMO}}\) and the Encryption-with-Feed-Forward ($\mathsf{EncFF}$) construction. These results also imply the corresponding leakage-free and single-user guarantees: CR and TCR for MMO, and CR, CCR, TCR, and TCCR for \(\widehat{\mathsf{MMO}}\) and \(\mathsf{EncFF}\). Security in the quantum random permutation model (QRPM) follows as a special case. We further verify that, in the QICM/QRPM, the above MMO-type constructions securely instantiate CR-type hashes used in various existing protocol analyses. This covers several representative analyses involving OT extension, half-gates garbling, (correlated) GGM trees, and certain distributed point/comparison function constructions. When the remaining components are post-quantum secure or modeled as ideal functionalities, the resulting protocol instantiations are post-quantum secure in the corresponding model. Technically, our proof relies on the reprogramming-and-resampling technique of Alagic et al.~(Eurocrypt 2022). To handle adaptive key leakage, as needed for some malicious OT-extension analyses, we introduce the conditional min-entropy with leakage (cmel) advantage, which separates leakage-induced entropy loss from the quantum ideal-cipher analysis. Without leakage, our bounds guarantee security up to roughly \(2^{\rho/3}\) queries, where \(\rho\) is the min-entropy of the secret shift.

  匹配依据：MPC: garbled circuit, secure computation

  </details>

- **GATOR: Group Action AdapTOR Signatures via MPC-in-the-Head**
  2026-05-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1067)
  Nico Döttling, Manar Mohamed, Riccardo Zanotto

  <details><summary>摘要 / Abstract</summary>

  Adaptor signatures are a foundational fairness primitive for blockchain applications. They enhance blockchain functionality by enabling applications such as atomic swaps, payment channels, and other fair-exchange protocols. At a high level, they allow a buyer to produce a pre-signature tied to a public statement, which a seller holding a corresponding witness can adapt into a valid signature. Once this signature is posted on-chain, the seller obtains payment, while the buyer can extract the witness from the finalized signature. Existing practical adaptor signature constructions are predominantly tied to discrete-logarithm-based signatures, such as ECDSA and Schnorr, reflecting their widespread use in current blockchain deployments. However, the threat of Shor&#x27;s algorithm and the broader transition toward post-quantum cryptography raise the question of whether adaptor functionality can also be realized efficiently for post-quantum signature schemes. In this work, we answer this question for a broad class of signatures based on cryptographic group actions. Building on efficient MPC-in-the-Head-style group-action signatures, we obtain adaptor functionality through small modifications, yielding a general framework for adaptor signatures from arbitrary group actions. In particular, our construction supports selling group-action discrete logarithms, which in certain parameter regimes correspond to the secret keys of the underlying signature scheme. We further discuss concrete instantiations from several group-action families, including those underlying schemes such as CSI-FiSh, LESS, MEDS, and ALTEQ, and present a modular proof-of-concept implementation. We obtain a ~25kB pre-signature with ~100ms pre-signing time for LESS, MEDS and ALTEQ, while a ~4kB pre-signature with ~3.6s pre-signing time for CSI-FiSh.

  匹配依据：MPC: mpc (context)

  </details>

- **S4 Is All You Need**
  2026-05-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1061)
  Donald Beaver

  <details><summary>摘要 / Abstract</summary>

  A fully shuffled permutation of four cards suffices to implement 1-of-2 Oblivious Transfer at a rate of one transfer per shuffle. After dealing two cards to Alice and one to Bob, Alice deterministically selects item from a threefold partition of the edges of a tetrahedron, at which point OT is established. Unlike decades of 2-player computation results employing restricted permutations (as in den Boer&#x27;s groundbreaking Five Card Trick) and artificial decks with repeated symbols, the &quot;Tetrahedral OT&quot; is the first to achieve two-party secret computations using a fully-shuffled set of unique elements. New &quot;tenancy&quot; and &quot;narrowing&quot; techniques are developed. Design patterns and protocol generation parameters are presented, along with some insightful but less efficient choices. The geometric symmetries behind the Tetrahedral OT protocol open up connections from Oblivious Transfer to Secret Key Exchange protocols as well. Decoupling information-theoretic permutations from computational one-wayness provides systematic access to broader and novel MPC protocol design, insight and simplification.

  匹配依据：MPC: oblivious transfer

  </details>

- **Practical Anonymous Two-Party Gradient Boosting Decision Tree**
  2026-05-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.26903)
  Chenyu Huang, Fan Zhang, Minxin Du, Sherman S. M. Chow, Huangxun Chen, Huaming Rao, Danqing Huang, Bo Qian, Peng Chen

  <details><summary>摘要 / Abstract</summary>

  Structured data is well handled by gradient-boosted decision trees (GBDT), which are usually trained on vertically partitioned features across mutually distrustful parties. High speed and interpretability make GBDTs popular in finance and healthcare, where neural networks may fall short. Enabling secure computation for GBDTs poses unique challenges, requiring secure record alignment for comparison. Relying on private set intersection (PSI) is a de facto approach. Mistaking PSI for a safety measure actually exposes which record identifiers (IDs) are shared between the datasets. Although circuit-PSI could help, it is costly for generic uses. New ideas are needed to efficiently train in a &quot;dark forest&quot;. Aiming to hide the IDs, we initiate the study of anonymous GBDT training on split data held by two parties. Dual circuit-PSI in our design lets the parties alternate as receiver to run pick-then-sum over local features. Via oblivious programmable pseudorandom functions, we propagate circuit-PSI outputs as shared state across runs. Avoiding universal alignment, we resolve the neglected dilemma that ID hiding incurs a cost that scales with domain size. Next, we halve the cost of ciphertext packing used to convert single-instruction multiple-data homomorphic encryption from (ring) learning with errors in prior secure GBDT (Usenix Security&#x27; 23) and related secure machine-learning computations. Comparative experiments show our protocol remains competitive with leaky approaches in efficiency. Enabling ID-hiding aggregation, our techniques can extend to other vertically partitioned analytics.

  匹配依据：MPC: private set intersection, secure computation

  </details>

- **Encrypted Cloning, Absolute Maximal Entanglement and Quantum Secret Sharing**
  2026-05-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.26866)
  Zheng Liang Lim, Hoi-Kwong Lo

  <details><summary>摘要 / Abstract</summary>

  The no-cloning theorem prohibits the creation of identical copies of quantum information, imposing fundamental constraints on quantum technologies. A recently proposed protocol, encrypted cloning, introduced by Yamaguchi and Kempf, showed that perfect qubit clones can be produced if they are simultaneously encrypted with a single-use key. They also observed a connection between this scheme and quantum secret sharing (QSS). However, it remained an open question whether encrypted cloning could be generalised to arbitrary dimensions, and the broader relationship between the two schemes had not been formally established. In this work, we address both questions by framing encrypted clones as Absolutely Maximally Entangled (AME) states. In parallel with recent work by Ceará that utilises Zadoff-Chu sequences, we independently develop a complementary framework for arbitrary dimensions based on Weyl-Heisenberg displacement operators, both tracing back to the original qubit construction by Yamaguchi and Kempf. We analytically compute the encrypted state and prove that an encrypted qudit system comprising two signal-noise qudit pairs is equivalent to a five-party AME state in any dimension, provided the input state is uniform. We then formalise the connection to QSS by proving that a threshold QSS scheme can achieve the fundamental objectives of encrypted cloning, establishing QSS as the natural general framework within which encrypted cloning can be contextualised.

  匹配依据：MPC: secret sharing

  </details>

- **Efficient MPC-Based Modulus Conversion for Threshold FHE Decryption**
  2026-05-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1058)
  Ivan Damgård, Sebastian Kolby, Claudio Orlandi, Stanislas Pawlak

  <details><summary>摘要 / Abstract</summary>

  We present new techniques for converting secret-shared values between different moduli in arithmetic MPC, without relying on bit decomposition. More concretely, our protocols convert a sharing \([x]_q\) over a source modulus \(q\) into a sharing \([x]_t\) over a target modulus \(t\), under a mild bound on the size of \(x\). We give three variants: a particularly simple protocol for power-of-two moduli, a protocol for arbitrary source modulus and prime target modulus, and a general protocol for arbitrary target modulus via an intermediate prime modulus. All variants use only a constant number of openings and a small amount of preprocessing. We present them in the arithmetic black box model, so they can be instantiated on top of any MPC protocol supporting basic modular arithmetic. As a main application, we use these techniques to construct efficient threshold decryption protocols for lattice-based fully homomorphic encryption (FHE), including BFV, BGV, and related schemes. The resulting protocols are special-purpose MPC protocols with a small constant number of rounds. They avoid noise flooding, allowing the parameters of the underlying FHE scheme to be chosen without making room for additional decryption noise. The resulting protocols achieve statistical UC security against malicious adversaries. We improve substantially on previous work on MPC-based threshold FHE decryption: as a concrete example, the state-of-the-art protocol by Zyskind et al. (ACM CCS 2025) implements decryption of the BFV scheme (with ciphertext modulus $2^{64}$), using about 17.000 bits of preprocessed correlated randomness, while we need only 63.

  匹配依据：MPC: mpc (context)

  </details>

- **Round-Optimal Subversion-Resilient UC PAKE from Malleable Trapdoor Smooth Projective Hash Functions**
  2026-05-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1047)
  Behzad Abdolmaleki, Suvradip Chakraborty, Shahram Khazaei, Lorenzo Magliocco, Nahid Roustaeifar, Behzad Vahdani, Daniele Venturi

  <details><summary>摘要 / Abstract</summary>

  Password-Authenticated Key Exchange (PAKE) allows two parties to establish a common high-entropy secret from a possibly low-entropy pre-shared secret such as a password. In this paper, we revisit the question of constructing PAKE protocols with subversion resilience in the framework of universal composability (UC), where the latter roughly means that UC security still holds even if one of the two parties is malicious and the honest party&#x27;s code has been subverted (in an undetectable manner). The latter goal was recently achieved by Chakraborty, Magliocco, Magri and Venturi (ASIACRYPT 2024), based on sanitation of oblivious transfer protocols and dual-mode cryptosystems via cryptographic reverse firewalls (Mironov and Stephens-Davidowitz, EUROCRYPT 2015). Our contributions are as follows: - We introduce so-called malleable trapdoor smooth projective hash functions (M-TSPHF), as an enhancement of trapdoor smooth projective hash functions (Benhamouda et al., CRYPTO 2013). Our extension incorporates new properties including key malleability and element rerandomizability. - We give a generic construction of subversion-resilient UC PAKE based on M-TSPHF and other standard cryptographic primitives. As we demonstrate, our PAKE protocol can be instantiated efficiently yielding an improved round and communication complexity with respect to the previous protocol of Chakraborty et al. In particular, our PAKE protocol achieves round optimality, as it concludes in a single round.

  匹配依据：MPC: oblivious transfer

  </details>

- **Symmetric Attribute-Based Encryption from Minimal Hardness Assumptions**
  2026-05-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1018)
  Riccardo Longo, Enrico Sorbera

  <details><summary>摘要 / Abstract</summary>

  We present a novel construction that applies the Ciphertext-Policy Attribute-Based Encryption paradigm in an original symmetric framework, where also the encryptor needs to have enough attributes to be able to produce a ciphertext for a given policy. The scheme is built from minimal assumptions on collision-resistant hash functions and pseudorandom functions, exploiting the properties of linear secret sharing and polynomial interpolation. Thus, it is natively Post-Quantum secure. We formally define a novel extended form for access trees, that trades a polynomial space expansion for a more predictable topological structure. This structure enhance the arithmetic possibilities of the associated secret sharing primitive. Moreover, we propose a comprehensive notation for access trees, sharing and interpolation, which may help in the study of these powerful primitives.

  匹配依据：MPC: secret sharing

  </details>

- **On the Security of Public Key Authenticated Encryption with Keyword Search with Sender-independent Search Complexity**
  2026-05-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1019)
  Takeshi Yoshida, Keita Emura

  <details><summary>摘要 / Abstract</summary>

  Li et al. (IEEE Transactions on Dependable and Secure Computing 2026) proposed proxy-free public key authenticated encryption with ciphertext update and keyword search (proxy-free PAUKS). In this short note, we demonstrate that keyword information is leaked from updated ciphertexts. We also demonstrate that our attack is effective against the PAUKS scheme proposed by Li et al. (IEEE Transactions on Information Forensics and Security 2023).

  匹配依据：MPC: secure computing

  </details>

- **Device-Independent Quantum Secret Sharing Protocol Enhanced by Advantage Distillation**
  2026-05-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.21880)
  Yong-Hui Yang, Jian-Hong Shi, Hong-Wei Li, Hai-Long Zhang, Yun-Teng Yang, Yu-Bing Zhu, Yan-Yang Zhou

  <details><summary>摘要 / Abstract</summary>

  Device-independent quantum secret sharing (DI-QSS) provides high security by eliminating the need to trust devices, yet its practical performance is limited by channel loss and noise. This work extends advantage distillation from two-party quantum key distribution (QKD) to three-party DI-QSS, redesigning the corresponding data interaction and verification procedures. The technique is systematically applied to the basic protocol and three active improvement strategies: noise preprocessing, post-selection, and their combination. This approach enhances noise tolerance, reduces the required global detection efficiency threshold, and significantly extends the maximum secure communication distance. Numerical simulations demonstrate that for the basic protocol over fiber, the maximum secure distance increases from 0.16 km to 1.85 km, and the noise tolerance improves from 10.17% to 28.49%. The results show that generalizing advantage distillation to the three-party setting effectively strengthens the protocol&#x27;s robustness and practicality, enhancing its adaptability to realistic noise and advancing the development of more reliable quantum secret sharing systems.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Distributed Optimization Under Time Constraints Using Secure Multi-Party Computation and Evolutionary Algorithms**
  2026-05-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.20944)
  Sebastian Gruber, Tobias Harzfeld, Christoph G. Schuetz, Florian Wohner, Thomas Lorünser

  <details><summary>摘要 / Abstract</summary>

  In distributed optimization, multiple parties collaborate to find an optimal solution to a problem. Privacy-preserving distributed optimization uses techniques, such as secure multi-party computation (MPC), to protect the private inputs of each party. In time-critical settings, the runtime overhead introduced by privacy-preserving computations may prevent the optimization from finishing within the deadline. This paper presents an approach for privacy-preserving distributed optimization in time-critical settings that combines evolutionary algorithms for solution search and MPC for the evaluation of solutions. The approach reduces the impact of privacy-preserving computations on runtime and allows to return solution within the deadline. Obfuscation of evaluation results provides additional protection for private inputs from an honest-but-curious platform provider, but introduces a potential trade-off between protection and solution quality. This trade-off is investigated in experiments using a genetic algorithm for both the single-objective assignment problem and the traveling salesperson problem, as well as NSGA-II for the multi-objective assignment problem.

  匹配依据：MPC: secure multi party computation

  </details>

- **Information-Theoretic Optimistic Verifiable Secret Sharing**
  2026-05-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1000)
  Martin Hirt, Chen-Da Liu-Zhang, Emanuele Marsicano

  <details><summary>摘要 / Abstract</summary>

  Verifiable secret sharing (VSS) is a fundamental primitive for secure computation and its round complexity has been well studied. The works of Gennaro et al. [STOC&#x27;01] and Fitzi et al. [TCC&#x27;06] settled the landscape in the perfect-security setting, showing that for the optimal corruption threshold $t&lt;n/3$, the exact round complexity is three, and for the sub-optimal corruption threshold $t&lt;n/4$ it is two rounds. Similarly, Patra et al. [CRYPTO&#x27;09] and Kumaresan et al. [ASIACRYPT&#x27;10] settled the landscape in the statistical setting, showing that for $t&lt;n/2$ (resp. $t&lt;n/3$), the exact round complexity is three (resp. two). Current protocols with optimal resilience incur three rounds even when the actual number of corruptions $f$ is sub-optimal. Fix corruption threshold parameters $0\le k \le t$. We ask whether it is possible to obtain a VSS protocol that incurs two rounds when $f\le k$, and three rounds when $k&lt;f\le t$. We show matching feasibility and impossibility results demonstrating that this is possible if and only if $3t+k &lt; n$ for perfect security, and $2t+k &lt; n$ for statistical security.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Constant-Online PVSS from CCA2-Secure Threshold Encryption: A Generic Framework**
  2026-05-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1009)
  Liang Zhang, Dongliang Cai, Haibin Kan, Jiheng Zhang, Moti Yung

  <details><summary>摘要 / Abstract</summary>

  Publicly Verifiable Secret Sharing (PVSS) is widely used in distributed systems. Existing schemes usually incur at least $O(n)$ online cost: the dealer encrypts, proves, and publishes $n$ shareholder-dependent objects, which public verification must process. In this work, we present a generic framework that transforms publicly verifiable CCA2-secure threshold encryption (CCATE) into \emph{constant-online} PVSS, with distribution and public- verification costs independent of the number of shareholders. The framework moves the share-generation work into a reusable setup phase: once threshold keys and public verification material are fixed, online sharing amounts to a single publicly verifiable threshold encryption. We instantiate the framework with two CCATE constructions: 1) a pairing-free instantiation using standard Threshold ElGamal encryption under a committee-based setup assumption; and 2) a silent-setup scheme leveraging non-interactive key generation via a Power-of-Tau ceremony, eliminating inter-party coordination during setup. Furthermore, we discuss epoch-based membership updates under the corresponding setup assumptions, clarifying the security boundary of reconfiguration. The resulting schemes incur higher setup costs, but the critical online distribution and public-verification phases are constant-size and constant-time. This trade-off is particularly useful when setup can be amortized over many PVSS instances, as in blockchain and distributed-system deployments.

  匹配依据：MPC: secret sharing

  </details>

- **Topology-Hiding Computation From Key Agreement in Diameter-Two Graphs**
  2026-05-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/996)
  D'or Banoun, Elette Boyle, Ran Cohen

  <details><summary>摘要 / Abstract</summary>

  Topology-hiding computation (THC) enables a set of parties, communicating over an incomplete network, to execute a secure multiparty computation (MPC) protocol for securely computing a function, while also hiding the network topology from within a given class of graphs. Semi-honest THC can be achieved over arbitrary graph classes, facing an arbitrary number of corruptions, from various assumptions implying oblivious transfer (OT). These assumptions are justified by strong lower bounds, indicating that $2$-secure topology-hiding broadcast (THB) over certain diameter-$3$ graph classes requires OT, as well as $1$-secure THC over certain diameter-$2$ graph classes of variable size. While THC from weaker assumptions, such as key agreement (KA), is achievable for $t=1$ over fixed-size graphs, the case of multiple corruptions remains unclear, with no known candidate constructions. Even in the simpler, privacy-free case of THB, tolerating $t&gt;1$ corruptions without assuming OT is only known for &quot;friendship&quot; graphs (which are diameter-$2$ graphs of a certain form): in fact, the latter holds information theoretically and for $t 1$, where given a graph class, THB either holds unconditionally or requires OT? In this work we study these questions over graphs of diameter $2$ (in which the lower bounds requiring OT do not hold) and provide THC protocols for various graph classes supporting many corruptions assuming KA. For some of these results we obtain optimal resilience assuming KA: $t&lt;n$ for THB and $t&lt;n/2$ for THC. We also present new lower bounds, showing that in certain graph classes that support information-theoretic THB for $t=1$, KA is necessary for $t=2$.

  匹配依据：MPC: oblivious transfer, secure multiparty computation

  </details>

- **The Privacy Subsidy in Glosten-Milgrom: Bid-Ask Spread and Welfare under Flip-Noise Direction Observation**
  2026-05-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.19742)
  Yuki Nakamura

  <details><summary>摘要 / Abstract</summary>

  We derive a closed-form bid-ask spread and welfare decomposition for the Glosten-Milgrom 1985 sequential-trading model when the market maker observes the trade direction perturbed by a binary flip channel of probability $η$ -- a natural information-theoretic model of privacy mechanisms acting on the direction signal. Under a committed Bayesian market-maker pricing rule, the equilibrium spread is $μ(1-2η)Δ$, where $μ$ is the informed-trader fraction and $Δ= v_H - v_L$ the value range. The welfare decomposition identifies a per-trade transfer $μηΔ$ from the protocol&#x27;s liquidity pool to traders -- the &quot;privacy subsidy&quot;, mirroring the Gaussian-Kyle analog established in prior work. The result extends the privacy-subsidy concept from continuous Gaussian to discrete two-state microstructure, demonstrating robustness across both classical models. Primary application: MPC-based matching engines with $\varepsilon$-differentially-private direction disclosure, where the engine prices on a noisy direction signal.

  匹配依据：MPC: mpc (context)

  </details>

- **ThriftyMPC: Reducing the Cost of Large-Scale MPC in the Cloud**
  2026-05-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/977)
  David Inyangson, Sahbaaz Ansari, Tushar M. Jois, Rosario Gennaro, Gamze Gursoy, Gabriel Kaptchuk, Moti Yung, Diogo Barradas

  <details><summary>摘要 / Abstract</summary>

  Cloud computing has become the standard for large-scale computation, offering elastic scalability and on-demand resources that exceed typical on-premise capabilities. However, many large-scale computations over sensitive data -- such as genome-wide association studies (GWAS) -- face significant barriers to cloud adoption due to privacy concerns and regulatory constraints. While cryptographic primitives like multi-party computation can alleviate these concerns through provable privacy guaranties, their substantial communication and computational overhead can make cloud deployment cost-prohibitive. To address both privacy and cost constraints, we present ThriftyMPC. ThriftyMPC is a framework that leverages spot instances (ephemeral cloud compute at reduced rates) to enable cost-effective, privacy-preserving computation at scale by combining secure multi-party computation with preemption-tolerant execution. We introduce a formal model for multi-party execution under ephemeral compute conditions, demonstrate how ThriftyMPC handles spot instance preemptions while maintaining cryptographic security guaranties, and provide a formal discussion of these guaranties. Our evaluations on realistic GWAS-inspired workloads over the Google Cloud Platform demonstrate robust execution despite spot instance churn, and show significant cost reduction compared to the state-of-the-art multi-party computation framework (MP-SPDZ) run traditionally using on-demand instances. We show that leveraging multi-party computation on spot instances makes privacy-preserving computation economically viable, enabling organizations to harness the cloud for sensitive workloads previously confined to isolated, on-premise deployments.

  匹配依据：MPC: multi party computation, secure multi party computation

  </details>

- **Asynchronous Shamir-Based Threshold FHE: Smaller Moduli and Strong Simulation Security**
  2026-05-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/973)
  Won Kim, Changmin Lee, JeongHwan Lee, Alain Passelègue, Damien Stehlé

  <details><summary>摘要 / Abstract</summary>

  We study $t$-out-of-$n$ threshold fully homomorphic encryption (ThFHE) based on Shamir secret sharing (SSS) in the asynchronous setting. With SSS, a partial decryption share is a single ring element; this allows to avoid the large number of ring elements stored per party required by prior strongly secure constructions based on $\{0,1\}$ reconstruction coefficients. However, this reduction introduces a fundamental trade-off: Lagrange reconstruction during distributed decryption severely amplifies noise, forcing a substantially larger ciphertext modulus. In this work, we give SSS-based asynchronous ThFHE constructions over standard RLWE-based FHE schemes (BFV, BGV, and CKKS) for both standard and strong simulation security. Through tight analysis of the modulus constraints, our constructions simultaneously reduce the required modulus, compared with prior asynchronous Shamir-based constructions, and the per-party storage, compared with the prior strongly secure construction. For example, for $n=512$ under standard simulation security, our analysis reduces the modulus overhead of distributed decryption by $33 \%$ at $t=n/2$ and by up to $90\%$ for $t$ close to $n$, relative to the prior works. Under strong simulation security, the per-party storage for $n=16$ and $t=8$ at $128$-bit security drops from $79$ GB in prior work to $897$ KB.

  匹配依据：MPC: secret sharing

  </details>

- **Magic Secret Sharing: Threshold Control of Quantum Computational Power via GHZ Entanglement**
  2026-05-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.16614)
  Soumyojyoti Dutta, Tushar

  <details><summary>摘要 / Abstract</summary>

  We introduce Magic Secret Sharing (MSS), a quantum cryptographic primitive in which the secret is the computational capability of a quantum state rather than its classical description. In the resource theory of magic, non-stabilizer states fuel universal quantum computation via non-Clifford gates; MSS distributes this resource with an (n-1,n) threshold structure using a pre-shared GHZ state and a single local phase gate P(phi) = diag(1, exp(i*phi)). Any individual party holds the maximally mixed state I/2, with Wigner distance C(I/2) = 0, so no local operation can yield non-Clifford computational advantage regardless of what operations are applied or what noise acts on the device. The authorised coalition reconstructs magic content C(phi) = (|sin(phi)| + |cos(phi)| - 1)/2 exactly, enabling a logical T gate via gate teleportation in multi-server blind quantum computation (BQC). Among diagonal parametric gates, phase gates are the unique class satisfying the security condition, characterised via an exact column-sum condition. The protocol is elevated to a one-sided device-independent (1SDI) setting via a steering inequality: the assemblage produced on the recipient&#x27;s side certifies magic delivery without trusting the coalition&#x27;s devices. We demonstrate the (2,3) instance on ibm_marrakesh (156-qubit IBM Heron): security (C(rho_Bob) &lt; 10^-6, the linear-programming solver tolerance) holds in every run and is independently reproduced on a second qubit assignment, and state fidelity reaches 0.959-0.973 for the authorised party, with faithfulness confirmed for all four test values of phi to within 0.025 in magic content, a residual that depolarising noise alone accounts for.

  匹配依据：MPC: secret sharing

  </details>

- **Threshold FHE with Short Decryption Shares without a Semi-trusted Server**
  2026-05-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/957)
  Hiroki Okada, Tsuyoshi Takagi

  <details><summary>摘要 / Abstract</summary>

  Threshold fully homomorphic encryption (ThFHE) enables decryption by collecting decryption shares from any T-out-of-N parties. A major drawback of previous ThFHE schemes is that they require a super-polynomial modulus (or are subject to other limitations), resulting in long ciphertexts, keys, and decryption shares. Passel`egue and Stehl´e (Asiacrypt 2024) proposed a ThFHE scheme in which a semi-trusted server rounds the input ciphertexts to produce polynomially short ciphertexts and sends them to the parties, thereby making the rest of the decryption process efficient. Although the input ciphertexts are still super-polynomially large, the communication cost of sending them from the parties to the server can be reduced to polynomial size via the transciphering technique; as a result, an entirely low-communication ThFHE is achieved. However, if even a single party colludes with the server (contrary to the assumption), the secret key can be efficiently recovered. Such a risky scenario would be unsuitable for practical deployment. In this paper, we tackle this issue. We propose two serverless ThFHE schemes with polynomially short decryption shares. The core idea is to let the parties directly round the decryption shares, rather than rely on the semi-trusted server to round the ciphertexts. We can also achieve low-communication ThFHE by reducing the communication required to send input ciphertexts to the parties to polynomial size via transciphering. Our first scheme, based on binary coefficient linear secret sharing ({0,1}-LSS), strictly improves upon Boneh et al. (CRYPTO 2018), achieving short decryption shares without any trade-offs. Our second scheme, based on Shamir secret sharing, adapts the technique of Okada and Takagi (Asiacrypt 2025) to eliminate the $O(N^{4.3})$ overhead in share size of our first scheme, further reducing communication costs.

  匹配依据：MPC: secret sharing

  </details>

- **On the (non-)resilience of encrypted controllers to covert attacks**
  2026-05-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.14230)
  Philipp Binfet, Janis Adamek, Moritz Schulze Darup

  <details><summary>摘要 / Abstract</summary>

  The security of networked control systems (NCS) is receiving increasing attention from both cyber-security and system-theoretic perspectives. The former focuses on classical IT security goals such as confidentiality, integrity, and availability of process data, while the latter investigates tailored attacks (and detection schemes), including covert and zero-dynamics attacks. Confidentiality in control systems can, for instance, be achieved by securely outsourcing the evaluation of the controller to third-party platforms, such as cloud services. The underlying technology enabling such secure computation often is homomorphic encryption (HE). Recent works in encrypted control have proposed modifications to underlying HE schemes to achieve not only confidentiality but also resilience to certain types of integrity attacks. While extensions in this direction are desirable in principle, we show that the integrity problem in encrypted control cannot be solved by public-key HE schemes alone due to their inherent malleability. In other words, the same homomorphisms that enable encrypted control in the first place can be leveraged not only constructively but also destructively. More precisely, we demonstrate that NCS are vulnerable to covert attacks, even when encrypted control is employed. Remarkably, this remains possible without knowledge of an unencrypted model. Yet, resilience to such attacks can still be achieved through complementary techniques. We present an approach based on verifiable computation that integrates with modern homomorphic cryptosystems and is asymptotically secure while incurring no communication overhead.

  匹配依据：MPC: secure computation

  </details>

- **Construction of Minimal Ternary Linear Codes with Dimension $m+2$ Via Krawtchouk Polynomials**
  2026-05-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.14848)
  Haibo Liu, Xin Guo, Qunying Liao

  <details><summary>摘要 / Abstract</summary>

  Recently, minimal linear codes have been extensively studied due to their applications in secret sharing schemes, secure two-party computations, and so on. Constructing minimal linear codes violating the Ashikhmin-Barg condition and then determining their weight distributions have been interesting in coding theory and cryptography. In this paper, a generic construction for ternary linear codes with dimension $m+2$ is presented, where $m$ is an integer, and a necessary and sufficient condition for this ternary linear code to be minimal is derived. Based on this condition and Krawtchouk Polynomials, a new class of minimal ternary linear codes violating the Ashikhmin-Barg condition are obtained, and then their complete weight enumerators are determined.

  匹配依据：MPC: secret sharing

  </details>

- **On MPC-friendly Softmax**
  2026-05-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/944)
  Marcel Keller, Ke Sun

  <details><summary>摘要 / Abstract</summary>

  Softmax is widely used in deep learning to map some representation to a probability distribution. As it is based on the exponential function, which is relatively expensive in multi-party computation, Mohassel and Zhang (S&amp;P, 2017) proposed a simpler replacement based on ReLU (the maximum of the input and zero) to be used in secure computation. Later works (e.g., Wagh et al., PETS 2019 and 2021) used the softmax replacement not for computing the output probability distribution but for approximating the gradient in backpropagation. In this work, we analyze the two uses of the replacement and compare them to softmax, both in terms of accuracy and cost in multi-party computation. We found that the replacement only provides a significant speed-up for a one-layer network, while it always reduces accuracy, sometimes significantly. Thus, we conclude that its usefulness is limited, and one should use the original softmax function instead. We also present a novel protocol for secure exponentiation that reduces communication up to fourfold while preserving accuracy when used for softmax.

  匹配依据：MPC: multi party computation, secure computation

  </details>

- **Distribution of GHz sequential Time-bin Entanglement in a Metropolitan Fiber Network**
  2026-05-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.13359)
  Martin Achleitner, Alessandro Trenti, Philip Walther, Hannes Hübel

  <details><summary>摘要 / Abstract</summary>

  Efficient generation and high-quality distribution of entanglement is becoming increasingly more relevant in the field of quantum technologies, with important applications such as multiparty computation as well as quantum key distribution (QKD) on the rise. Quantum communication protocols based on entanglement offer an inherent quantum based randomness for key generation and provide in general higher security compared to prepare and measure implementations. Moreover, the future quantum internet will also be based on the distribution of entanglement for securely connecting quantum computers in a network. In this work we show the feasibility of using sequential time-bin entangled states for quantum key distribution in metropolitan networks using off-the-shelf components. The time-bin encoding ensures high fidelity distribution robust against random polarisation fluctuations occuring in optical fibers. Modulated laser pulses in the GHz frequency range are used to generate time-bin entangled photon pairs. The entangled photons are then sent over an about 30km long (9.5dB loss) fiber link within the Vienna fiber network, showing high degree of distributed entanglement with a measured 93\% quantum visibility.

  匹配依据：MPC: multiparty computation

  </details>

- **Storing Less in-the-Head: An Area-Efficient Hardware Architecture for SDitH-v2**
  2026-05-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/938)
  Stef Halmans, Niklas Höher, Dina Hesse, Sanjay Deshpande, Jakub Szefer, Tim Güneysu

  <details><summary>摘要 / Abstract</summary>

  In 2022, the National Institute of Standards and Technology (NIST) initiated a second call for post-quantum digital signature proposals to broaden algorithmic diversity beyond the already standardized schemes based on structured lattices and hashes. While five out of the 14 second-round entries were built on the MPC-in-the-Head paradigm, only two advanced into the recently announced third round. Despite their theoretical appeal, available results on their implementation costs imply a reduced applicability to resource-constrained embedded devices. In this work we analyze one of the remaining candidates, the revised second version of the Syndrome Decoding in the Head (SDitH) signature scheme based on the VOLE-in-the-Head framework, and showcase that these issues are not inherent to the family of algorithms. We propose an area-efficient hardware design including highly optimized variants of both Batch Line Commitment (BLC) and Polynomial Interactive Oracle Proof (PIOP) routines. As a result, we reduce memory requirements by a factor of 22 to 52 compared to the approach of the reference implementation and by a factor of 40 to 88 compared to the previous hardware implementation of SDitH-v1, while still achieving competitive runtimes. To the best of our knowledge, this yields the most compact hardware implementation of any MPCitH or code-based signature primitive, with our algorithmic improvements directly transferable to software designs. During our analysis, we additionally determined nine significant discrepancies between specification and reference implementation of SDitH-v2, with a subset breaking test vector compatibility. Beyond addressing these issues, we suggest specification changes to further reduce resource usage on embedded targets without compromising security assumptions.

  匹配依据：MPC: mpc (context)

  </details>

- **ORCHID: Orchestrated Reduction Consensus for Hash-based Integrity in Distributed Ledgers**
  2026-05-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.12211)
  Abraham Itzhak Weinberg

  <details><summary>摘要 / Abstract</summary>

  We present \textbf{ORCHID} (\textit{Orchestrated Reduction Consensus for Hash-based Integrity in Distributed Ledgers}), a novel bio-inspired consensus protocol that maps the neuroscientific \emph{binding problem} -- how the brain integrates distributed neural oscillations into a unified conscious percept -- onto the distributed systems \emph{consensus problem}, how blockchain nodes agree on a single ledger state under Byzantine faults. Grounded in the Penrose--Hameroff Orchestrated Objective Reduction (Orch~OR) hypothesis and the Kuramoto synchronisation model, ORCHID equips each node with a quantum-noisy phase oscillator; consensus is triggered when the network&#x27;s order parameter $r(t)$ crosses a \emph{binding threshold} $θ_b$, mirroring the gamma-band binding event in conscious perception. ORCHID is further strengthened by a coherence-weighted Quantum Secret Sharing (QSS) layer, extending the survey framework of Weinberg to a concrete consensus application. Simulation results on Watts--Strogatz small-world networks ($n=10$--$150$) demonstrate: (i)~the Kuramoto order parameter reaches $r_{\max}=0.988$ under coupling $K=3.0$, well above the theoretical critical coupling $K_c \approx 1.41$; (ii)~a sharp QSS fidelity phase transition at coherence $c^*\approx 0.82$, confirming Theorem~2; (iii)100\% consensus rate at all tested Byzantine fractions (0\%--40\%), with median convergence under 4~s for $n=30$; and (iv)~ORCHID achieves $O(n{\cdot}k)$ message complexity, outperforming PBFT&#x27;s $O(n^2)$ at $n\geq150$. These results establish ORCHID as a scalable, biologically plausible, and quantum-augmented consensus mechanism for post-quantum distributed ledgers.

  匹配依据：MPC: secret sharing

  </details>

- **Experimental Examination of Secure Two-Party Controller Computation**
  2026-05-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.11443)
  Kaoru Teranishi, Jihoon Suh, Takashi Tanaka

  <details><summary>摘要 / Abstract</summary>

  A secure two-party computation protocol for running dynamic controllers over secret sharing has recently been proposed. Unlike encrypted control schemes based on homomorphic encryption, this protocol enables operating dynamic controllers for an infinite time horizon without controller-state decryption, controller-state reset, or input re-encryption. However, the two-party setting introduces additional online communication between the computing parties, which may hinder real-time feasibility. In this study, we demonstrate the feasibility of the protocol through implementation on a commercial cloud platform with an inverted pendulum testbed. Experimental results show that the proposed protocol successfully stabilized the pendulum despite the online communication overhead.

  匹配依据：MPC: secret sharing, secure two party computation

  </details>

- **Efficient and Privacy-preserving Outsourced Training of Decision Tree Models Based on (Leveled) Fully Homomorphic Encryption**
  2026-05-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/936)
  Tongyu Xu, Jun Wang, Honglian Liang, Shiwei Xu

  <details><summary>摘要 / Abstract</summary>

  Training machine learning models is computationally intensive, making cloud-based outsourcing an attractive solution to alleviate local resource constraints. However, untrusted cloud environments pose serious privacy risks to both training data and resulting models. Existing works primarily rely on multi-party computation (MPC) or lattice-based Homomorphic Encryption (HE), which often incur high communication or computation overheads. To address these challenges, we propose an efficient privacy-preserving scheme for outsourced decision tree training. Specifically, we leverage Symmetric Homomorphic Encryption (SHE) to achieve faster training speed. However, since SHE only supports integer-based homomorphic operations, we propose a Modified Gini Impurity Index (MGII) to adapt to this restriction and use Single Instruction Multiple Data (SIMD) packing to accelerate processing. Experimental results demonstrate that our scheme significantly reduces overall execution time compared to related works and achieves comparable (and for deeper trees, better) accuracy, while security analysis confirms that data and model confidentiality are preserved.

  匹配依据：MPC: multi party computation

  </details>

- **Private Function Evaluation with Linear Complexity**
  2026-05-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/926)
  Shuaishuai Li, Cong Zhang, Anyu Wang, Xiaoyun Wang

  <details><summary>摘要 / Abstract</summary>

  We present new frameworks for secure function evaluation (SFE) and private function evaluation (PFE) that support both Boolean and arithmetic circuits. While SFE requires multiple parties to jointly compute a \textit{public} circuit, PFE generalizes SFE by allowing one party to keep the circuit \textit{private}. Our work achieves the first linear-complexity PFE protocol with respect to both the number of parties $n$ and circuit size $m$, significantly improving upon prior PFE constructions that require $O(mn^2)$ complexity and are limited to Boolean circuits.

  匹配依据：MPC: secure function evaluation

  </details>

- **Practical and Verifiable Encrypted Vector Search for Retrieval-Augmented Generation**
  2026-05-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/923)
  Xiangyu Hui, Xingliang Yuan, Olga Ohrimenko, Sid Chi-Kin Chau

  <details><summary>摘要 / Abstract</summary>

  Retrieval-augmented generation (RAG) systems critically depend on a vector-retrieval stage that selects relevant documents from a large embedding database. When this stage is outsourced to a RAG-as-a-Service provider, query embeddings can reveal sensitive user intent, the outsourced index can leak proprietary corpus information, and a malicious provider can silently manipulate retrieval results. This motivates privacy-preserving verifiable retrieval. The client must be able to confirm that the returned top-$k$ identifiers were produced by faithfully executing an agreed approximate nearest neighbor (ANN) algorithm on a committed encrypted index, while leaking no non-public database information beyond the functional baseline induced by the returned top-$k$ identifiers. We present VeriANN, the \emph{first} encrypted ANN retrieval framework, to our knowledge, that simultaneously achieves \emph{query privacy}, \emph{database confidentiality}, and \emph{verifiability of retrieval results} against malicious servers, under a two-server non-colluding trust model. VeriANN couples distributed-point-function--based PIR over locality-sensitive hashing indexes with authenticated garbled circuits, so that the entire top-$k$ pipeline---bucket decryption, Merkle-root reconstruction, frequency counting, and top-$k$ selection---is executed obliviously and with end-to-end integrity. Making this integration practical requires three new techniques: (i) a sort-based hierarchical oblivious frequency-counting algorithm that enables a distance-free post-processing stage, reducing top-$k$ aggregation from quadratic to quasi-linear complexity; (ii) an end-to-end authenticated verification design that binds the full retrieval pipeline against selective-failure attacks while reducing client-side verification to a single hash check against the published Merkle root; and (iii) a modular state-pool design with an authenticated state-transfer mechanism that dynamically composes precomputed garbled states across query parameters while preserving cross-circuit verifiability. On million-scale corpora, VeriANN achieves second-scale end-to-end latency with KB-scale client-to-server communication, while adding minimal online overhead over a non-verifiable baseline.

  匹配依据：MPC: garbled circuits

  </details>

- **LogVOLE: Succinct and Efficient Chosen-Input VOLE for ZK and Beyond**
  2026-05-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/925)
  Lucien K. L. Ng, Peter Rindal, Akash Shah

  <details><summary>摘要 / Abstract</summary>

  Random Vector Oblivious Linear Evaluation (VOLE) correlations can be generated efficiently for zero-knowledge proofs and secure computation. Applications that need correlations on the receiver’s actual input typically derandomize random VOLE by sending a linear-size vector, a main communication bottleneck. We study chosen-input VOLE (CI-VOLE), where the receiver privately chooses a large vector \(\mathbf{x}\), the sender fixes \(\Delta\), and the parties obtain shares of \(\mathbf{x}\cdot\Delta\) without communicating a linear-size object. This work presents LogVOLE, a concretely efficient CI-VOLE protocol with polylogarithmic end-to-end communication under Ring-LWE. The construction uses a recursive shrink/expand design: it authenticates short digests of the chosen input and then uses a succinct telescope to expand those relations back to the full vector. The protocol has \(O(\lambda\log^2(|\mathbf{x}|+m_{\mathsf{msg}}))\) one-time setup and query communication and \(O(|\mathbf{x}|/n)\) ring operations. Here, \(n\) is the underlying ring degree, \(\lambda\) is the computational security parameter, and \(m_{\mathsf{msg}}\) is the size of the shares. LogVOLE also supports a public-key non-interactive mode: for a fixed \(\Delta\), the sender publishes reusable parameters, and a receiver sends one compact \(\mathbf{x}\)-dependent message to obtain the matching VOLE shares. This gives a route to non-interactive VOLE-based ZK with polylogarithmic communication for arbitrary circuits. We also give a malicious-security extension in the random oracle model. Using LogVOLE, we construct the first concretely efficient VOLE-based designated-verifier ZK protocol for arbitrary circuits with polylogarithmic communication. At 128-bit computational and 40-bit statistical security, our implementation achieves online throughput of 13.9 million \(\mathbb{Z}_p\) correlations/s and 12.9 million ZK multiplication gates/s using 16 CPU cores per party. With golden-seed optimization and reusable setup, our GPU implementation processes 532.3 million \(\mathbb{Z}_p\) correlations/s and 451.7 million ZK multiplication gates/s online on an H200 GPU. With one CPU thread per party, our implementation proves \(1024\times1024\) matrix multiplication in about 4 seconds online, with 226 kB of online communication.

  匹配依据：MPC: secure computation

  </details>

- **BitVM3: Efficient Bitcoin Bridges via Garbled Circuits**
  2026-05-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/933)
  Robin Linus Woll, Ioannis Alexopoulos, Lukas Aumayr, Zeta Avarikioti, Matteo Maffei, David Tse

  <details><summary>摘要 / Abstract</summary>

  Bitcoin bridges, protocols that lock BTC on Bitcoin and represent it on a secondary system, underpin much of Bitcoin&#x27;s application layer, yet remain poorly secured. Deployed bridges rely on federated custody with honest-majority assumptions, while BitVM2, the state of the art in trust-minimized bridging, incurs worst-case dispute costs of approximately \$16,000, requiring large operator bonds and deposits that restrict participation to well-capitalized parties. We present BitVM3-BRIDGE, a trust-minimized bridge architecture from Bitcoin to (i) chains with finality certificates, such as Ethereum, and (ii) Bitcoin rollups. Our main contribution is an end-to-end bridge construction that makes trust-minimized Bitcoin bridging practical at scale. The bridge is powered by BitVM3-CORE, a modular abstraction for permissionless off-chain computation on Bitcoin using garbled circuits. In BitVM3-CORE, a challenger evaluates a garbled circuit entirely off-chain and obtains a fraud-proof witness if and only if the operator&#x27;s claim is incorrect. This paradigm reduces total on-chain costs to approximately \$9, with the challenge transaction itself costing just \$0.20. This nearly 1000× cost reduction enables smaller bonds, broader operator participation, and smaller deposit sizes. Beyond the bridge itself, we make two additional contributions. First, we formalize BitVM3-CORE as a sound and complete on-chain proof system under standard cryptographic assumptions. Prior GC-based proposals typically provide either informal security arguments or construction-specific formalizations. By contrast, our framework captures existing constructions within a uniform model and gives a generic treatment based on axiomatized security and functional assumptions. Second, we introduce an on-chain Bitcoin light client secure in the variable-difficulty setting, enabling permissionless chain introspection on Bitcoin and thereby the rollup variant of BitVM3-BRIDGE.

  匹配依据：MPC: garbled circuit, garbled circuits

  </details>

- **Towards Practical Committee Sizes in YOSO MPC**
  2026-05-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/919)
  Paweł Kędzior, Marcin Mielniczuk, Daniele Venturi

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation in permissionless settings like blockchains faces the challenge of maintaining security under adaptive corruptions. YOSO MPC (Benhamouda et al., TCC 2020; Gentry et al., Crypto 2021) addresses this through ephemeral roles, allowing committee members to speak only once before erasing state, thus preventing adaptive attacks within each role&#x27;s lifetime. However, prior work on YOSO MPC relied on an honest majority within committees and required enormous committee sizes, often numbering in the thousands. In this paper, we challenge both requirements by leveraging the cryptoeconomic properties of the underlying blockchain. We introduce a mechanism for identifying parties who fail to fulfill their roles during protocol execution, using time-lock puzzles. This enables misbehaving parties to be penalized based on publicly verifiable fraud proofs, allowing for a more aggressive committee threshold. Furthermore, we propose a new sortition procedure that ensures the resulting committee always has a constant size, not just in expectation. This reduces fluctuations in committee size, enabling an even higher committee threshold. These techniques allow us to handle any constant fraction $f &lt; 1$ of total corruptions. Finally, we refine and generalize the analysis of corruptions in YOSO protocols, obtaining tighter bounds. Combined with our other enhancements, this enables committees of around 100 parties. Our analysis yields a $70$--$80\%$ improvement over the estimates of the seminal work by Benhamouda et al. (TCC 2020). We believe our work paves the way for practical deployments of YOSO MPC protocols.

  匹配依据：MPC: secure multi party computation

  </details>

- **Privacy-Preserving Distributed Learning in IoT Systems: A Unified Threat Model and Evaluation Framework**
  2026-05-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.09232)
  John Cartmell, Alexander Williams

  <details><summary>摘要 / Abstract</summary>

  The increasing deployment of Internet-of-Things (IoT) devices has accelerated the use of distributed learning frameworks, where data remains local while model updates are shared across decentralized systems. Although this reduces centralized data collection, it introduces privacy risks through the exchange of gradients, model parameters, and intermediate representations. A variety of privacy-preserving techniques have been proposed to address these risks, including differential privacy, cryptographic methods, and lightweight system-level approaches. However, existing surveys often evaluate these methods in isolation and lack a unified framework for comparing their effectiveness under realistic attack models and IoT resource constraints. This paper presents a structured analysis of privacy-preserving techniques for distributed learning in IoT environments. A unified threat model is introduced that captures model inversion, membership inference, gradient leakage, and communication-based attacks. Building on this model, an evaluation framework is developed to compare methods in terms of both privacy robustness and system-level efficiency, including computational, memory, and communication overhead. Using this framework, representative approaches including differential privacy, homomorphic encryption, secure multi-party computation, distributed selective stochastic gradient descent, and Bloom Filter-based methods are analyzed. The results highlight a fundamental trade-off between privacy strength and system efficiency. In particular, Bloom Filter-based encodings are shown to provide lightweight privacy through collision-induced ambiguity while maintaining low computational and communication overhead. The paper provides a unified perspective on privacy-preserving design choices for distributed learning in IoT systems.

  匹配依据：MPC: secure multi party computation

  </details>

- **Cryptanalysis of the Subfield Bilinear Collision Problem**
  2026-05-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/916)
  Pierre Briaud, Romaric Neveu

  <details><summary>摘要 / Abstract</summary>

  The security of a recent MPC-in-the-Head signature scheme introduced at Crypto 2024 by Huth and Joux required the introduction of a new ad hoc hardness assumption called the Subfield Bilinear Collision (SBC) problem. By relying on the VOLE-in-the-Head framework, the authors further improved the performance of this scheme at Asiacrypt 2025, resulting in a very compact construction. In this paper, we improve the original cryptanalysis of SBC in several ways. First, we describe a link between the SBC problem and the decoding problem in the rank metric for codes linear over an extension field $\mathbb{F}_{q^m}$, strengthening its theoretical hardness and expanding the range of attacks on the SBC problem. Second, we analyze Gröbner basis algorithms applied to the bilinear modeling of SBC proposed by Huth and Joux and formulate conjectures on the behavior of this system. Finally, we describe another algebraic modeling of SBC obtained by using the Plücker relations between the maximal minors of a matrix. While we do not threaten the parameters of the proposed signature schemes relying on SBC, our work opens the door to a more accurate analysis. In particular, we were not able to analyze the inclusion of the field equations of $\mathbb{F}_{q}$ in the Gröbner basis algorithm, which is especially relevant since $q=2$ in these parameters. We leave this task for future work.

  匹配依据：MPC: mpc (context)

  </details>

- **Private Vertical Federated Inference for Time-Series**
  2026-05-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.08343)
  Lucas Fenaux, Larris Xie, Aditya Bang, Alex Zhang, Kevin Wilson, Florian Kerschbaum

  <details><summary>摘要 / Abstract</summary>

  Institutions may benefit from collaborative inference on time-series data. In settings where privacy is necessary, multi-party computation (MPC) is a straightforward approach to providing strong guarantees, yet it remains prohibitively expensive and scales poorly with modern transformer architectures. Vertical Federated Learning (VFL) offers efficiency but suffers from privacy leakage at the embedding level, and securing the entire VFL model head via MPC remains prohibitively slow and communication-heavy for larger models. To enable practical, secure inference at scale, we propose &quot;Public/Private Hybrid Head-VFL&quot; (PPHH-VFL). This hybrid architecture splits the model head into an efficient plaintext public head and a secure, lightweight MPC private head. By applying adversarial training to the public embeddings, we mitigate privacy leakage; concurrently, the small private head securely preserves the flow of sensitive information needed for high downstream utility. Empirical evaluations on models ranging up to 86 million parameters demonstrate that PPHH-VFL accelerates inference by up to six orders of magnitude compared to end-to-end MPC. Compared to a standard VFL+MPC baseline, our approach scales significantly better, achieving a speedup of up to 44.4x in WAN and a 91.2x reduction in communication costs (dropping from 1.7 GB to 19 MB per batch), while simultaneously improving downstream classification accuracy by 2.50% and regression RMSE by 40.7%.

  匹配依据：MPC: multi party computation

  </details>

- **A Privacy-Preserving Machine Learning Framework for Edge Intelligence: An Empirical Analysis**
  2026-05-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.05751)
  Quoc Lap Trieu, Bahman Javadi, Jim Basilakis

  <details><summary>摘要 / Abstract</summary>

  As Edge Intelligence (EI) becomes increasingly prevalent in domains such as smart healthcare, manufacturing, and critical infrastructure, ensuring data privacy while maintaining system efficiency is a growing challenge. This paper presents a new privacy-preserving machine learning (PPML) framework tailored for EI applications, including a four-layer system architecture and training and inference algorithms. We focus on three leading approaches: Differential Privacy (DP), Secure Multi-party Computation (SMC), and Fully Homomorphic Encryption (FHE), and assess their impact on key performance metrics, including model accuracy, response time, and energy consumption. Results from real implementation and extensive trace-based simulations of inference tasks show that DP generally preserves throughput and latency close to plaintext baselines, while accuracy drops with model complexity (up to 35 percent on AlexNet and under 18 percent on LeNet for FordA). SMC performance is driven by communication; network bandwidth and round complexity determine end-to-end latency. For AlexNet, increasing link capacity from 250 Mbps to 500 Mbps reduces latency by about 30 percent. FHE is highly sensitive to model structure and numerical precision bit width, with tighter parameters imposing substantial compute overhead; we observe roughly a 1000 times increase in response time compared to DP. Beyond efficiency, DP shifts the privacy-utility-extractability frontier by reducing the attacker&#x27;s data efficiency in black-box model stealing, whereas SMC and FHE, while protecting inputs and parameters during inference, require complementary output controls to achieve similar resistance to extraction. These findings provide critical insights into the trade-offs between privacy, performance, and resource efficiency in edge computing scenarios.

  匹配依据：MPC: secure multi party computation

  </details>

- **A Pragmatic Comparison of Cryptographic Computation Technologies for Machine Learning**
  2026-05-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.04858)
  Marcus Taubert, Adam Skuta, Thomas Loruenser

  <details><summary>摘要 / Abstract</summary>

  As security demands increase, the importance of secure computation technologies grows, yet these technologies can often seem overwhelming to practitioners. Furthermore, many approaches focus only on a single technology, potentially overlooking superior alternatives. This work aims to address the issue of selecting the right technology for secure computation by presenting a comparative analysis of two highly relevant cryptographic methods and their software implementations, with a particular focus on machine learning. Firstly, we provide a theoretical summary and comparison of the secure computation paradigms of secure multi-party computation (SMPC) and fully homomorphic encryption (FHE). We outline the advantages and limitations of the protocols, as well as the relevant open-source software implementations. Secondly, we present the results of extensive benchmarking of the main software frameworks identified for machine learning operations and models. Regarding the current state of the art in FHE, we observe that it outperforms SMPC for regressions. Additionally it may be faster for simple dense networks using GPUs or Hybrid Models. Conversely, SMPC showed superior performance for complex models such as CNNs. Our results should pave the way for more technology-agnostic benchmarking of secure computation technologies for machine learning, providing guidance for practitioners looking to adopt these technologies.

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **Secure Two-Party Quantum Computation with Complete Fairness without Trusted Third Party**
  2026-05-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/883)
  Arpita Maitra, Goutam Paul, Asim K. Pal, Asmita Samanta, Hridam Basu

  <details><summary>摘要 / Abstract</summary>

  In 1997, Lo proved that if one of the parties is malicious, it is not possible to achieve unconditional security in quantum bit-commitment (Phy. Rev. Lett, 1997) and hence in two-party quantum computation (Phy. Rev. A, 1997). However, restricting the computational power of the adversary, via assumptions like the existence of one-wayness, it has been shown that secure quantum bit-commitment is indeed possible by Dumais et al. (EUROCRYPT 2000). In their paper, they showed that with the assumption of a one-way permutation that is secure against any polynomial-time quantum adversary, one can achieve a secure quantum bit-commitment scheme. Although security is guaranteed, complete fairness remains an issue in quantum two-party computation for the real-world framework. In this paper, we show for the first time that there are some functions for which secure two-party quantum computation with complete fairness is achievable. This seems in sharp contrast with the impossibility result of Ben-Or et al. (FOCS, 2006). In Ben-Or et al.&#x27;s work, they have considered a malicious quantum adversary with unconditional computational power and used a broadcast channel. We have used the hybrid model idea of Gordon et al. (STOC 2008) using a non-simultaneous channel and the idea of composition of multiparty computations by Ran Canetti (Journal of Cryptology, 2000), to achieve complete fairness in the quantum domain, under the assumption of computationally bounded adversary. The functions we study are of two types (similar to Gordon et al.): one is any function without an embedded XOR, and the other is a particular function containing an embedded XOR. At first, we design secure two-party computation protocols in a hybrid model, using a trusted third party. Then we prove how these protocols achieve complete fairness in the hybrid model. Finally, we construct a secure two-party communication protocol and show how we can use this to remove the trusted third party of the hybrid model, and achieve both security and complete fairness in the real-world model.

  匹配依据：MPC: secure two party computation, two party computation

  </details>

- **Quantum-Resistant Networks: A Review of Primitives, Protocols and Best Practices**
  2026-05-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.04129)
  Elisa Bertino, Ramana Kompella, Ashish Kundu, Cristina Nita-Rotaru, Jaideep Vaidya, Attila A. Yavuz

  <details><summary>摘要 / Abstract</summary>

  Large-scale quantum computers threaten the public-key cryptographic foundations underpinning today&#x27;s network security infrastructures. While significant progress has been made in standardizing post-quantum cryptographic (PQC) primitives and adapting individual protocols such as TLS and SSH, far less attention has been paid to the broader architectural consequences of the post-quantum transition for networked systems. In particular, many real-world deployments such as mobile networks, industrial control systems, IoT environments, and regulated infrastructures cannot assume the universal availability, deployability, or desirability of PQ public-key infrastructures. This paper presents the first comprehensive systematization of PQ-resistant network architectures, focusing on key distribution and management as a system-level design problem rather than a protocol-local substitution. We introduce a unified taxonomy spanning cryptographic foundations (symmetric-only, PQ-PKI, hybrid, and information-theoretic multi-path), key-distribution architectures (centralized, hierarchical, replicated, threshold, MPC-backed, and serverless), trust and threat models, key-management lifecycle, and deployment environments. Using this framework, we analyze the security, scalability, and operational trade-offs of a wide range of architectures under realistic PQ adversary assumptions, including harvest-now, decrypt-later attacks and partial infrastructure compromise. Our study highlights fundamental gaps in existing approaches, clarifies when PQ-PKI is necessary or avoidable, and identifies promising research directions for building cryptographically agile, quantum-resilient network infrastructures.

  匹配依据：MPC: mpc (context)

  </details>

- **Post-Quantum Public-Key Pseudorandom Correlation Functions for OT**
  2026-05-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/877)
  Shweta Agrawal, Kaartik Bhushan, Geoffroy Couteau, Mahshid Riahinia

  <details><summary>摘要 / Abstract</summary>

  Public-key pseudorandom correlation functions (PK-PCF) are an exciting recent primitive introduced to enable &quot;non-interactive key exchange for secure computation&quot;. Despite significant advances in the group-based setting, success in the post-quantum regime has been much more limited. To the best of our knowledge, there does not exist even a single efficient candidate post-quantum PK-PCF for the standard string oblivious transfer (OT) correlation. In this work, we address this gap by constructing the first efficient lattice-based public-key PCF for the string OT correlation. Our PK-PCF generates a few hundred OTs per second, and requires a large but manageable public key size (a few hundred megabytes). In contrast, the only previous lattice-based non-public-key PCF, proposed in the very recent work of Hasler, Reisert and Küsters (Asiacrypt 2025), can generate up to 9 OT/s and has key sizes of several gigabytes. At the heart of our result lie several technical contributions that might be of independent interest. In particular, we introduce the first efficient lattice-based constrained pseudorandom functions for low-degree polynomials, from a new but natural &quot;secret-power&quot; variant of ring learning with errors. Our assumption is non-interactive and falsifiable, and we carefully analyze it for attacks. Additionally, we introduce a new packing mechanism compatible with local rounding of noisy shares from a &quot;truncated&quot; variant of our previous assumption, which allows further efficiency. We remark that in the pre-quantum regime, the state of art for PK-PCF only two years ago was 1 OT/s, while they now clock at ~30k OT/s. We are optimistic that our construction will follow a similar trajectory.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **On the Common Bias of Majorities: Poly-Time Attacks on THR-XOR PRGs**
  2026-05-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/880)
  Antonio Giulio D’Antona, Pierrick Méaux, Akin Ünal

  <details><summary>摘要 / Abstract</summary>

  Pseudorandom Generators (PRGs) based on Threshold-XOR predicates with large locality and high stretches have recently gained traction, since they lend themselves as shallow weak Pseudorandom Functions (PRFs) to fast multiparty computation protocols. In this work, we present novel fast attacks on such PRGs that achieve substantial advantages. Concretely, we break the security levels of most parameters collected by Boura, Couteau, Perrin and Rotella (ToSC&#x27;25), as well as those proposed by Fu, Li, Lyu and Liu (EC&#x27;26). On the asymptotic side, we prove that our attacks achieve an advantage of $n^{-n/a}$ where $n$ denotes the seed length and $a$ the locality of threshold predicates. As a consequence, when $a \in \Theta(n)$, we get poly-time attacks with noticeable advantage. These results close current gaps on the theoretical study of THR-XOR based Goldreich PRGs. Additionally, we demonstrate how the attack advantage can be amplified for PRGs with large output lengths (which are common in the context of weak PRFs). Finally, we discuss alternative predicates for Goldreich PRGs that resist all currently known attacks.

  匹配依据：MPC: multiparty computation

  </details>

- **Secret-Key PIR from One-Way Functions**
  2026-05-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/865)
  Nir Bitansky, Noam Mazor

  <details><summary>摘要 / Abstract</summary>

  In secret-key private information retrieval (SK-PIR), the client in an offline phase processes the database using a short secret key. In the online phase the client could then use the secret key to make queries to the server, without revealing the entries accessed, and using only sublinear communication $o(N)$ in the database size $N$. While (non-SK) PIR requires public-key cryptography, recent work provides evidence that SK-PIR may not. In particular, Chen, Ishai, Mour, and Rosen (STOC 26) construct SK-PIR with communication $N^{\varepsilon}$, for any $\varepsilon$, from high-noise LPN, which is not known to imply public-key cryptography. We construct SK-PIR with online communication $\tilde{O}(\sqrt{N)}$, under the minimal assumption of one-way functions. More generally we can achieve client-to-server communication $\tilde{O}(N_c)$ and server-to-client communication $\tilde{O}(N_s)$ as long as $N_c \cdot N_s \geq N$. Our construction is simple and is based on garbled circuits with an uncorrelated input encoding property, which is satisfied by schemes from the literature.

  匹配依据：MPC: garbled circuits

  </details>

- **SILMARILS: Information-Theoretic and Quantum-Secure Designated-Verifier Signatures**
  2026-05-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.03230)
  Hassan Khodaiemehr, Khadijeh Bagheri, Chen Feng, Dariia Porechna

  <details><summary>摘要 / Abstract</summary>

  SILMARILS is built from a minimal algebraic core over $\mathbb{F}_p$ using true randomness and perfect $2$-out-of-$2$ Shamir secret sharing. The framework supports both two-party and three-party modes. In the two-party setting, SILMARILS realizes a transferable designated-verifier (TDV) signature scheme. The designated verifier can simulate accepting transcripts indistinguishable from real ones, achieving Jakobsson-Sako-Impagliazzo DV security. The verifier may publish a receipt $r$ enabling public verification, yet even with $r$, no external party can tell whether a transcript was signed or simulated. As DV signatures permit simulation, standard EUF-CMA cannot hold for the designated verifier; instead, we prove $\mathsf{EUF\text{-}CMA}^{\neg\mathsf{DV}}$ security for all non-designated verifiers in both the random oracle model (ROM) and quantum random oracle model (QROM). In the three-party mode, adopting the broadcast model of Fitzi et al., we obtain a statistically secure signature protocol with simulation-based security and error $1/p$. We analyze security in the Pure IT model, the IT+ROM, and the QROM, extending the Fitzi et al. framework to quantum adversaries with classical I/O. Correctness, secrecy, transferability, and unforgeability for non-designated parties remain equivalent to simulation-based security. Thanks to its simple algebraic structure, SILMARILS offers very compact keys and signatures for the blockchain settings we target, where standardized PQC schemes are already more than sufficient. Our goal is not to compare SILMARILS with PQC, but to highlight its suitability for lightweight TDV authentication. A fair comparison with other DV schemes is omitted due to space and the complexity of aligning models.

  匹配依据：MPC: secret sharing

  </details>

- **Quantum Anonymous Secret Sharing with Permutation Invariant Codes**
  2026-04-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.27284)
  Varin Sikand, Andrew Nemec

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing schemes are a family of quantum cryptographic protocols which provide secure quantum encodings, mapping one secret to multiple shares of information such that the original secret cannot be accessed without an authorized set of shares present for decoding. In this work, we describe a protocol that enables sender-anonymity during the secret decoding process. By using permutation-invariant QEC codes along with a set of anonymous quantum transmission algorithms, we construct a quantum anonymous secret sharing scheme that achieves sender-anonymity. We quantify information leakage in ramp quantum secret sharing schemes via the quantum conditional min-entropy, justifying it as a valid measure of leaked information by relating it to the Knill-Laflamme quantum error correction conditions. Finally, we evaluate several permutation-invariant codes using this measure to make observations on the information leakage of intermediate shares for each quantum anonymous secret sharing scheme.

  匹配依据：MPC: secret sharing

  </details>

- **Merces: Confidential Token Transfers via MPC and CoSNARKs**
  2026-04-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/850)
  Daniel Escudero, Florian Lugstein, Christian Rechberger, Verena Schröppel, Roman Walch

  <details><summary>摘要 / Abstract</summary>

  Fungible tokens on public blockchains expose all balances and transfer amounts in the clear, which is incompatible with the financial privacy required by many real-world applications. We present Merces a confidential token contract that hides user balances and transaction amounts while preserving on-chain verifiability. The core idea is to store secret shares of balances within a decentralized MPC network, while only commitments are published to a smart contract. Thereby, Merces is capable of translating any existing token (e.g., any ERC20 token) into a confidential version. Deposits, withdrawals, and transfers are computed privately within the MPC network, which generates a collaborative SNARK (CoSNARK) to prove the validity of each state transition. In particular, the proof ensures that on-chain commitments are updated consistently and that the sender has sufficient funds. In this paper we give a full formalization of our construction in the Universal Composability (UC) framework, provide rigorous security proofs, and describe a concrete instantiation using Groth16 over BN254 with Poseidon2-based commitments. We further provide a complete end-to-end implementation, accompanied by extensive benchmarks and discussion of a working demo: our system achieves over 300 transactions per second, including proof generation, while requiring only minimal client-side computation.

  匹配依据：MPC: mpc (context)

  </details>

- **Federated Generation of Synthetic RNA-seq Data**
  2026-04-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.27456)
  Daniil Filienko, Martine De Cock, Sikha Pentyala

  <details><summary>摘要 / Abstract</summary>

  Access to genomic data is highly regulated due to its sensitive nature. While safeguards are essential, cumbersome data access processes pose a significant barrier to the development of AI methods for genomics. Synthetic data generation can mitigate this tension by enabling broader data sharing without exposing sensitive information. Synthetic genomic data are produced by training generative models on real data and subsequently sampling artificial data that preserves relevant statistics while limiting disclosures about the underlying individuals. In some settings, a single data holder may have sufficient data to train such generative models; however, in many applications data must be combined across multiple sites to achieve adequate scale. This need arises, e.g., in rare disease studies, where individual hospitals typically hold data for only a small number of patients. The solution we present in this paper enables multiple data holders to jointly train a synthetic data generator without revealing their raw data. Our approach combines secure multiparty computation (MPC) to ensure input privacy, so that no party ever discloses its data in unencrypted form, with differential privacy (DP) to provide output privacy by mitigating information leakage from the released synthetic data. We empirically demonstrate the effectiveness of the proposed method by generating high-utility synthetic datasets from multiple real RNA-seq cohorts in federated settings, showing that our approach enables privacy-preserving data synthesis even when data are distributed across institutions.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Scale, Round, Break: Simple Leakage Attacks on Secret Sharing Schemes**
  2026-04-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/833)
  Katharina Boudgoust, Mark Simkin

  <details><summary>摘要 / Abstract</summary>

  We study the local leakage resilience of $t$-out-of-$n$ threshold secret sharing schemes. We present a remarkably simple, perfectly correct attack that fully breaks any scheme with linear reconstruction over a finite field using $\lg t + \mathcal{O}(1)$ bits of leakage per share. In particular, this yields concretely efficient attacks on additive secret sharing and on Shamir’s scheme for arbitrarily large thresholds over arbitrarily large finite fields. Our key technical idea is an approximately linear scale-and-round function that maps shares from an arbitrarily large field into a much smaller ring, while preserving the distance of well-separated secrets. Our results provides two surprising insights: Bigger finite fields do not necessarily improve leakage resilience and increasing the reconstruction threshold in Shamir’s scheme does not help too much either.

  匹配依据：MPC: secret sharing

  </details>

- **Maliciously Secure Exact Fixed-Point Multiplication over Power-of-Two Rings for Replicated 3PC**
  2026-04-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/822)
  Yutao Sun, Jianguo Xie, Guozhen Shi, Jiale Han, Huiyan Chen, Rongna Xie

  <details><summary>摘要 / Abstract</summary>

  Exact fixed-point multiplication over $\mathbb{Z}_{2^k}$ is a fundamental primitive for secure fixed-point arithmetic. However, in the honest-majority, maliciously secure 3PC setting, no prior work simultaneously provides cross-ring compatibility, exact semantics, and malicious security within this efficient framework. In this paper, we address this gap by showing that the core cross-ring bottlenecks, namely exact signed truncation and signed extension, share a unified algebraic structure. Based on this insight, we propose a general \textbf{quotient-correction framework} that reduces complex non-linear cross-ring operations to a highly efficient \textbf{2-bit bounded-quotient extraction} problem. We instantiate this framework to construct maliciously secure protocols for exact truncation and extension. By sequentially composing these primitives with standard in-ring multiplication, we realize the first end-to-end exact fixed-point multiplication protocol that satisfies all aforementioned requirements in the replicated 3PC setting. We also present optimized variants under relaxed guarantees (e.g., 1-ULP error) that offer superior performance trade-offs. We formalize our constructions within the Universal Composability (UC) framework and provide rigorous security proofs. Theoretical analysis and experimental results demonstrate that our approach achieves practical online efficiency while maintaining exact semantics and malicious security, overcoming the limitations of prior baselines regarding security assumptions, input domains, or output precision.

  匹配依据：MPC: 3pc (context)

  </details>

- **Suffix-Invariant Programmable PRFs and Applications to Stacked Garbling**
  2026-04-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/815)
  Vipul Goyal, David Heath, Abhishek Jain, Yibin Yang

  <details><summary>摘要 / Abstract</summary>

  Garbled circuits are a fundamental primitive in cryptography. While the size of garbled circuits in Yao&#x27;s original scheme grows linearly with the circuit size, a recent line of work on stacked garbling (SGC) [Heath-Kolesnikov, CRYPTO&#x27;20] has achieved near-sublinear size for branching computations, based only on one-way functions. Specifically, these schemes achieve garbled size growing only with the size of a single branch and the total input length to all the branches. Due to the latter dependence, these results are best suited to &quot;small&quot; input settings. We present a stacked garbling scheme for &quot;large&quot; input settings based on one-way functions. The garbled size in our scheme grows only with the size of a single branch and its input length (up to logarithmic factors), plus an additive term in the number of branches (as in prior SGC). To obtain our result, we uncover a connection between stacked garbling and the notion of (adaptive) programmable pseudorandom functions (apPRFs) [Boneh-Lewi-Wu, PKC&#x27;17]. While existing apPRF constructions either rely on stronger assumptions (e.g., learning with errors or indistinguishability obfuscation) or incur noticeable security losses under weaker assumptions, we identify a relaxed notion of suffix-invariant programmable PRFs (sipPRFs) that suffices for our result, and establish its feasibility based on OWFs. Interestingly, we build on techniques from the SGC literature to construct sipPRFs with our desired efficiency, and then apply sipPRFs back to SGC to obtain our main result. Along the way, as an additional result of independent interest, we provide the first construction of (adaptive) programmable PRFs for polynomial-size domains based on one-way functions.

  匹配依据：MPC: garbled circuits, garbling scheme

  </details>

- **Practical Post-Quantum Secure Publicly Verifiable Secret Sharing and Applications**
  2026-04-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/813)
  Aniket Kate, Pratyay Mukherjee, Hamza Saleem, Pratik Sarkar, Rohit Sinha

  <details><summary>摘要 / Abstract</summary>

  We present a new framework for constructing practically efficient publicly verifiable secret sharing (PVSS) with $non-interactive$ $dealers$, in that the dealer may go offline after sending a single message, and is not involved in the share verification process. We use identity-based encryption (IBE) and commitments as the main ingredients and avoid expensive zero-knowledge proofs. By instantiating them with post-quantum secure schemes, a lattice-based IBE and a hash-based commitment, we obtain our first construction: a post-quantum secure PVSS with non-interactive dealers that outperforms the prior lattice-based practical construction by Gentry et al. [Eurocrypt 2022]. However, to enable the aggregation of PVSS transcripts (which facilitates many additional applications such as secure voting), we propose our second construction by replacing hash-based commitments with Pedersen&#x27;s homomorphic commitments. While this does not achieve full-fledged post-quantum security (as Pedersen&#x27;s scheme is not quantum safe), it still provides privacy against a post-quantum adversary. We prove the security of this construction in a new model, which we call long-lasting security. This model guarantees that the protocol is secure in the present (pre-quantum era) while maintaining privacy in the long term (post-quantum era). This new model is of independent interest for constructing efficient schemes that are resilient to the harvest-now-decrypt-later line of attacks. In this model, we propose a blockchain-compatible secure voting scheme using our PVSS scheme. Our PVSS schemes demonstrate practical efficiency: our post-quantum PVSS shares a secret among $1024$ receivers in $667$~ms and verifies the dealing in $&lt;5$ ms, and communicates $4.4$MB, overall whereas the state of the art [Gentry et al., Eurocrypt 2022] communicates $251$MB and requires $2060$s for dealing the secret.

  匹配依据：MPC: secret sharing

  </details>

- **Mosaic: Practical Malicious Security for Garbled Circuits on Bitcoin**
  2026-04-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/812)
  Nakul Khambhati, Mukesh Tiwari, Azz, Sapin Bajracharya, Manish Bista, Liam Eagen, Christian Lewe, Aaron Feickert

  <details><summary>摘要 / Abstract</summary>

  Bitcoin&#x27;s scripting language cannot verify arbitrary computation natively, yet applications such as trust-minimized bridges depend on this capability. Recent techniques employ garbled circuits: the prover commits off chain to a garbled circuit encoding a verifier, designed so that evaluating it on an invalid witness reveals a secret. Posting that secret on chain serves as a fraud proof, allowing the verifier to claim the prover&#x27;s stake without any on-chain computation. To evaluate the garbled circuit and recover the secret, the verifier needs the prover&#x27;s input labels, which the prover must post on chain. Since Bitcoin charges permanently for block space, minimizing this on-chain footprint is a primary design concern. Achieving malicious security via cut-and-choose compounds this: the prover must produce multiple independently garbled copies of the circuit, requiring one set of labels per copy. We present Mosaic, a protocol that achieves malicious security via cut-and-choose but reduces the on-chain footprint so that it is independent of the number of garbled copies. The key technique, first introduced by Eagen (Glock, 2025) in this setting, is polynomial label correlation: labels across all $N$ garbled copies are arranged as evaluations of a degree-$t$ polynomial, so the $t$ shares revealed during cut-and-choose fall one short of the reconstruction threshold. We use adaptor signatures to arrange that the prover&#x27;s on-chain witness commitment reveals the missing share as a byproduct; the evaluator then reconstructs labels for all unchallenged copies by interpolation. We sketch why Mosaic is secure against a malicious prover and verifier and instantiate it for trust-minimized Bitcoin bridging with a Groth16 verifier circuit, a full protocol specification, and a Rust implementation.

  匹配依据：MPC: garbled circuit, garbled circuits

  </details>

- **Efficient Two-Online-Round Secure Comparison in the Plain Model**
  2026-04-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/808)
  Koji Nuida, Satsuya Ohata

  <details><summary>摘要 / Abstract</summary>

  Secure comparison is a fundamental building block frequently employed in various applications of secure multiparty computation, such as secure machine learning. Such protocols based on secret sharing (SS) typically excel in throughput, but they historically suffer from higher (online) round complexity. To address this issue, Attrapadung et al. (AsiaCCS 2022) proposed a protocol with two online rounds in the client-aided model (i.e., assuming a trusted third party in the offline phase), and Lu et al. (USENIX Security 2025) proposed a protocol with three online rounds in the plain model. In this paper, we propose a plaintext comparison protocol with two online rounds in the plain model. While keeping the lowest online round complexity, our protocol also reduces the total bit complexity. For example, for the case of 64-bit integers, the total bit complexity of our protocol is 25.7% of Lu et al.&#x27;s protocol and 23.3% of Attrapadung et al.&#x27;s protocol adjusted to the plain model.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Outsourced Private Set Intersection for Pairwise Analytics**
  2026-04-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/801)
  Ferran Alborch, Tangi De Kerdrel, Antonio Faonio, Melek Önen

  <details><summary>摘要 / Abstract</summary>

  This paper studies privacy-preserving data analytics in settings where multiple parties hold sensitive datasets and want to compute global statistics without revealing their data. We focus on computing the total number of common elements (cardinality of intersections) across multiple pairs of datasets, while ensuring that only the final aggregated result is disclosed and no intermediate information (such as individual intersections) is leaked. To address this problem, we introduce a new cryptographic primitive called outsourced cardinality private set intersection with secret-shared outputs (CaOPSI-SS). Our solution is extremely simple and uses pseudorandom functions and two non-colluding servers to offload computation, making it suitable for environments with heterogeneous resources. Building on this primitive, we design a protocol for aggregated pairwise analytics that computes the sum of intersection cardinalities across many parties. We apply our framework to a real-world use case: privacy-preserving mail analytics in large organizations with multiple subsidiaries. The system allows useful fine-grained queries over email logs while protecting sensitive HR data. We also extend the solution with differential privacy mechanisms to further protect individual records. Finally, we implement and evaluate the protocol, showing its scalability and practicality for large datasets. Our solution enables parties to obliviously offload their datasets to two non-colluding servers using pseudorandom functions and further execute a circuit-PSI among these two servers to obtain secret shares of the output.

  匹配依据：MPC: private set intersection

  </details>

- **Sherpa.ai Privacy-Preserving Multi-Party Entity Alignment without Intersection Disclosure for Noisy Identifiers**
  2026-04-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.19219)
  Daniel M. Jimenez-Gutierrez, Dario Pighin, Enrique Zuazua, Georgios Kellaris, Joaquin Del Rio, Oleksii Sliusarenko, Xabi Uribe-Etxebarria

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) enables collaborative model training among multiple parties without centralizing raw data. There are two main paradigms in FL: Horizontal FL (HFL), where all participants share the same feature space but hold different samples, and Vertical FL (VFL), where parties possess complementary features for the same set of samples. A prerequisite for VFL training is privacy-preserving entity alignment (PPEA), which establishes a common index of samples across parties (alignment) without revealing which samples are shared between them. Conventional private set intersection (PSI) achieves alignment but leaks intersection membership, exposing sensitive relationships between datasets. The standard private set union (PSU) mitigates this risk by aligning on the union of identifiers rather than the intersection. However, existing approaches are often limited to two parties or lack support for typo-tolerant matching. In this paper, we introduce the Sherpa.ai multi-party PSU protocol for VFL, a PPEA method that hides intersection membership and enables both exact and noisy matching. The protocol generalizes two-party approaches to multiple parties with low communication overhead and offers two variants: an order-preserving version for exact alignment and an unordered version tolerant to typographical and formatting discrepancies. We prove correctness and privacy, analyze communication and computational (exponentiation) complexity, and formalize a universal index mapping from local records to a shared index space. This multi-party PSU offers a scalable, mathematically grounded protocol for PPEA in real-world VFL deployments, such as multi-institutional healthcare disease detection, collaborative risk modeling between banks and insurers, and cross-domain fraud detection between telecommunications and financial institutions, while preserving intersection privacy.

  匹配依据：MPC: private set intersection, private set union

  </details>

- **Secure Storage and Privacy-Preserving Scanpath Comparison via Garbled Circuits in Eye Tracking**
  2026-04-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.19422)
  Suleyman Ozdel, Amr Nader, Yasmeen Abdrabou, Enkelejda Kasneci

  <details><summary>摘要 / Abstract</summary>

  With the growing use of eye tracking on VR and mobile platforms, gaze data is increasing. While scanpath comparison is important to gaze behavior analysis, existing methods lack privacy-preserving capabilities for real-world use. We present a garbled-circuit (GC)-based approach enabling secure storage and privacy-preserving scanpath comparison under the semi-honest model. It supports two configurations: (1) a two-party setting where the data owner and processor jointly compute similarity scores without revealing their inputs, and (2) a server-assisted setting where encrypted scanpaths are stored and processed while the data owner remains offline. All decryption and comparison operations are executed inside the GC. Experiments on three eye-tracking datasets evaluate fidelity, runtime, and communication, and show secure results for MultiMatch, ScanMatch, and SubsMatch closely match plaintext outcomes, with manageable runtime and communication overhead. Tests under various network conditions indicate that the design remains feasible for real-world privacy-preserving scanpath analysis and can be extended to other GC-based behavioral algorithms.

  匹配依据：MPC: garbled circuit, garbled circuits

  </details>

- **Secret-Carrying Puzzles and Garbled Circuits Optimized for Zero-knowledge Proofs**
  2026-04-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/788)
  Debasish Ray Chawdhuri, Manoj Prabhakaran

  <details><summary>摘要 / Abstract</summary>

  In this work, we introduce the concept of Obliviously Checkable Secret-Carrying Puzzles (OxSP) and build proof-friendly Garbled Circuits (GCs) to enable their practical implementation. OxSPs allow one to publicly pose puzzles and verify purported solutions received in response, keeping the desired parts of the puzzles and the responses hidden. We show how OxSPs can be based on Garbled Circuits (GCs). However, this requires ZK-SNARK proofs of correctness of garbling. We note that combining existing GC and ZK-SNARK constructions results in very large computational costs for the OxSP solvers. Our main technical contribution is to design a new proof-friendly GC construction which cuts down the cost of generating a proof of correct garbling to almost a third, without resorting to non-standard cryptographic assumptions. Beyond its use in OxSP, we expect our proof-friendly GCs to be of significant independent interest, as a tool for auditable secure 2-party computation.

  匹配依据：MPC: garbled circuits, secure 2 party computation

  </details>

- **Party Autonomy in Determining the Law Applicable to Non-contractual Obligations concerning Cross-Border Data Transfers**
  2026-04-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.17806)
  Yuki Okamura, Ren Yatsunami, Kumiko Kameishi, Oliver Posani, Soma Araoka, Miho Ikeda, Makiko Aoyagi

  <details><summary>摘要 / Abstract</summary>

  (1)Cross-border data transfers have become a matter of daily occurrence against the backdrop of the development of cloud computing and artificial intelligence. Consequently, where a data leak gives rise to civil liability, the determination of that liability inevitably assumes an international dimension involving foreign elements. (2)As is starkly demonstrated by secret sharing technology in cloud computing, fragments of data may be presumed to be distributed across multiple jurisdictions on a global scale. This renders traditional private international law measures -- predicated on the identification of a physical location -- inadequate for the purposes of determining the applicable law, a difficulty that is particularly acute in relation to non-contractual obligations. (3)Bearing in mind the typical scenario encountered in practice -- in which a Data Subject brings a claim for damages against a SaaS (Software as a Service) provider, which in turn seeks recourse against an IaaS (Infrastructure as a Service) or PaaS (Platform as a Service) provider -- a characteristic feature of such cases is the concurrence of contractual and non-contractual obligations. Taking this feature into account, it is possible to determine the applicable law governing non-contractual obligations through party autonomy -- by aligning it with the law governing the contractual obligation as selected by the parties, an approach that may be termed private ordering. This serves to overcome the difficulties associated with the identification of a physical location and, at the same time, contributes to ensuring the foreseeability of the parties.

  匹配依据：MPC: secret sharing

  </details>

- **MBU: Scalable and Constant-Round Evaluation of Non-linear Functions in Standard MPC Setting**
  2026-04-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/765)
  Min Yang, Dongcan Guo, Zihang Zhou, Jinxuan Du, Qingshu Meng

  <details><summary>摘要 / Abstract</summary>

  After more than four decades of research, multi-party computation (MPC) has achieved remarkable success in handling 2-variable multiplication and comparison-based functions (e.g., ReLU) with practical efficiency. However, for general non-linear functions—such as multiplication of many variables, power, exponential, trigonometric functions, sigmoid, softmax, and GeLU—no native MPC algorithm exists as Beaver-based mutiplication that is constant-round, scalable and exact. Existing solutions rely on either polynomial approximations (trading precision for efficiency), iterative multi-round protocols like Multiplication-to-Addition (M2A) conversion (requiring \(\log_2 k\) rounds for \(k\) parties), or Function Secret Sharing (FSS) with lookup tables (introducing quantization errors and large storage, mainly limited to 2-4 parties). These approaches suffer from fundamental trade-offs among accuracy, communication rounds, and scalability. In this work, we propose a unified \emph{mask-broadcast-unmask} design pattern that enables constant-round, scalable and \emph{approximation-free} evaluation of a wide range of non-linear functions. Our contributions include: \begin{itemize} \item A \textbf{general multiplication} protocol for \(k\) variables in \emph{one round} with optimal \(O(kn)\) communication. When \(k=2\), it reduces to the classic Beaver triple multiplication; when each secret has only one non-zero share and \(k=2\), it becomes the well-known M2A protocol. \item \textbf{Power functions} (\(x^k\)) in one round. \item \textbf{Trigonometric functions} (\(\sin x, \cos x\)) and \textbf{exponential functions} (\(a^x\)) in 4 rounds. \item \textbf{Sigmoid, softmax} in 6 rounds. \end{itemize} All these protocols are provably secure in the semi-honest model, support arbitrary number of parties, introduce \textbf{no approximation error} beyond plaintext floating-point rounding, and require only constant communication rounds (1–6) independent of function complexity. Furthermore, by restricting the random mask to a suitable range (e.g., $0 \le r &lt;2^l-2^{l_x}$), we can reduce the rounds from 1-6 to 1-3. This work fills the long-standing gap for general non-linear functions in standard MPC settings, making privacy-preserving machine learning more practical for modern DNNs.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Privacy-Preserving LLMs Routing**
  2026-04-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.15728)
  Xidong Wu, Yukuan Zhang, Yuqiong Ji, Reza Shirkavand, Qian Lou, Shangqian Gao

  <details><summary>摘要 / Abstract</summary>

  Large language model (LLM) routing has emerged as a critical strategy to balance model performance and cost-efficiency by dynamically selecting services from various model providers. However, LLM routing adds an intermediate layer between users and LLMs, creating new privacy risks to user data. These privacy risks have not been systematically studied. Although cryptographic techniques such as Secure Multi-Party Computation (MPC) enable privacy-preserving computation, their protocol design and implementation remain under-explored, and naïve implementations typically incur prohibitive computational overhead. To address this, we propose a privacy-preserving LLM routing framework (PPRoute). PPRoute includes multiple strategies to speed up encoder inference and nearest neighbor search under the MPC and maintain the quality of LLM routing. First, PPRoute uses MPC-friendly operations to boost the encoder inference. Second, PPRoute uses a multiple-step model training algorithm to maintain routing quality despite the constraints of the encrypted domain. Third, PPRoute proposes an unsorted Top-k algorithm with $O(1)$ communication complexity for secure sorting in model search, significantly reducing communication latency. Across different datasets, PPRoute achieves the performance of plaintext counterparts, while achieving approximately a 20$\times$ speedup over naïve MPC implementations.

  匹配依据：MPC: secure multi party computation

  </details>

- **Improved Garbled RAM via Garbled Merge**
  2026-04-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/761)
  Can Liu, Lenny Liu, Ning Luo, David Heath

  <details><summary>摘要 / Abstract</summary>

  Consider the problem of merging inside a garbled circuit (GC) two arrays of $w$-bit elements, yielding a single length-$n$ array. This garbled merge problem is core to garbled random access memory (GRAM), a technique that enables efficient garbling of general-purpose programs. We present a novel symmetric-key-based garbled merge that achieves a garbling size of $(w + 1) \cdot n \cdot \lambda$ bits, providing both asymptotic and concrete improvements over the state of the art. By applying our garbled merge, we obtain a symmetric-key GRAM of size $O(n \lg^3 n \cdot \lambda) \cdot \omega(1)$ for a word RAM program that manipulates words of size $\Theta(\lg n)$ bits and halts within $n$ steps, improving over the previous best result (Heath et al., CRYPTO&#x27;23) by an $O(\lg \lg n)$ factor. This communication cost was previously only achieved under the public-key-style DDH assumption (Gu et al., CRYPTO&#x27;25). We implement our construction, and our evaluation shows that our garbled merge reduces the communication cost over the DDH-based merge by about $3\times$.

  匹配依据：MPC: garbled circuit

  </details>

- **SecureRouter: Encrypted Routing for Efficient Secure Inference**
  2026-04-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.15499) · [Code](https://github.com/UCF-ML-Research/SecureRouter)
  Yukuan Zhang, Mengxin Zheng, Qian Lou

  <details><summary>摘要 / Abstract</summary>

  Cryptographically secure neural network inference typically relies on secure computing techniques such as Secure Multi-Party Computation (MPC), enabling cloud servers to process client inputs without decrypting them. Although prior privacy-preserving inference systems co-design network optimizations with MPC, they remain slow and costly, limiting real-world deployment. A major bottleneck is their use of a single, fixed transformer model for all encrypted inputs, ignoring that different inputs require different model sizes to balance efficiency and accuracy. We present SecureRouter, an end-to-end encrypted routing and inference framework that accelerates secure transformer inference through input-adaptive model selection under encryption. SecureRouter establishes a unified encrypted pipeline that integrates a secure router with an MPC-optimized model pool, enabling coordinated routing, inference, and protocol execution while preserving full data and model confidentiality. The framework includes training-phase and inference-phase components: an MPC-cost-aware secure router that predicts per-model utility and cost from encrypted features, and an MPC-optimized model pool whose architectures and quantization schemes are co-trained to minimize MPC communication and computation overhead. Compared to prior work, SecureRouter achieves a latency reduction by 1.95x with negligible accuracy loss, offering a practical path toward scalable and efficient secure AI inference. Our open-source implementation is available at: https://github.com/UCF-ML-Research/SecureRouter

  匹配依据：MPC: secure computing, secure multi party computation

  </details>

- **MCU: Algebraic and Transcendental Function Evaluation in MPC without Preprocessing**
  2026-04-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/750)
  Min Yang, Jinxuan Du, Zihang Zhou, Dongcan Guo, Qingshu Meng

  <details><summary>摘要 / Abstract</summary>

  The rapid proliferation of privacy-sensitive machine learning and scientific computing applications has intensified the demand for secure multi-party computation (MPC) protocols that can efficiently evaluate complex nonlinear functions. Despite four decades of research, MPC systems face two fundamental barriers: heavy offline preprocessing and limited support for transcendental functions. Existing preprocessing-free frameworks are confined to comparison-related functions (e.g., Bicoptor) and cannot handle exponentials or trigonometric functions. In this paper, we propose MCU (Mask-Compute-Unmask), a novel MPC architecture that directly supports a broad class of algebraic and transcendental functions without any offline preprocessing. MCU introduces a semi-honest, non-colluding helper party (HP) as an active computational engine: parties additively mask their inputs, the HP computes the target function on the aggregated masked data, and the parties then unmask using locally known masks. This paradigm enables constant-round, scalable protocols for general multiplication (2 rounds), power functions (2 rounds), exponentials (8 rounds), and trigonometric functions (2 rounds). All protocols achieve simulation-based security and rely solely on synchronized pseudorandom generators—no preprocessing, no polynomial approximations. To the best of our knowledge, MCU is the first MPC framework that simultaneously achieves preprocessing-free, constant-round, exact evaluation of exponentials and trigonometric functions—functions essential for scientific computing, differential privacy mechanisms, and advanced neural network architectures. Our multiplication protocol scales better than Beaver-based multiplication in multi-party settings, and our exponential and trigonometric protocols achieve sub-ULP accuracy. The rapid proliferation of privacy-sensitive machine learning and scientific computing applications has intensified the demand for secure multi-party computation (MPC) protocols that can efficiently evaluate complex nonlinear functions. Despite four decades of research, MPC systems face two fundamental barriers: heavy offline preprocessing and limited support for transcendental functions. Existing preprocessing-free frameworks are confined to comparison-related functions (e.g., Bicoptor) and cannot handle exponentials or trigonometric functions. In this paper, we propose MCU (Mask-Compute-Unmask), a novel MPC architecture that directly supports a broad class of algebraic and transcendental functions without any offline preprocessing. MCU introduces a semi-honest, non-colluding helper party (HP) as an active computational engine: parties additively mask their inputs, the HP computes the target function on the aggregated masked data, and the parties then unmask using locally known masks. This paradigm enables constant-round, scalable protocols for general multiplication (2 rounds), power functions (2 rounds), exponentials (8 rounds), and trigonometric functions (2 rounds). All protocols achieve simulation-based security and rely solely on synchronized pseudorandom generators—no preprocessing, no polynomial approximations. To the best of our knowledge, MCU is the first MPC framework that simultaneously achieves preprocessing-free, constant-round, exact evaluation of exponentials and trigonometric functions—functions essential for scientific computing, differential privacy mechanisms, and advanced neural network architectures. Our multiplication protocol scales better than Beaver-based multiplication in multi-party settings, and our exponential and trigonometric protocols achieve sub-ULP accuracy. To the best of our knowledge, MCU is the first MPC framework that simultaneously achieves preprocessing-free, constant-round, exact evaluation of exponentials and trigonometric functions—functions essential for scientific computing, differential privacy mechanisms, and advanced neural network architectures. Our multiplication protocol scales better than Beaver-based multiplication in multi-party settings, and our exponential and trigonometric protocols achieve sub-ULP accuracy.

  匹配依据：MPC: secure multi party computation

  </details>

- **Secure and Privacy-Preserving Vertical Federated Learning**
  2026-04-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.13474)
  Shan Jin, Sai Rahul Rachuri, Yizhen Wang, Anderson C. A. Nascimento, Yiwei Cai

  <details><summary>摘要 / Abstract</summary>

  We propose a novel end-to-end privacy-preserving framework, instantiated by three efficient protocols for different deployment scenarios, covering both input and output privacy, for the vertically split scenario in federated learning (FL), where features are split across clients and labels are not shared by all parties. We do so by distributing the role of the aggregator in FL into multiple servers and having them run secure multiparty computation (MPC) protocols to perform model and feature aggregation and apply differential privacy (DP) to the final released model. While a naive solution would have the clients delegating the entirety of training to run in MPC between the servers, our optimized solution, which supports purely global and also global-local models updates with privacy-preserving, drastically reduces the amount of computation and communication performed using multiparty computation. The experimental results also show the effectiveness of our protocols.

  匹配依据：MPC: multiparty computation, secure multiparty computation

  </details>

- **Quantum secret sharing in tripartite superconducting network**
  2026-04-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.13643)
  W. K. Yam, C. Wilkinson, S. Gandorfer, F. Fesquet, M. Handschuh, A. Marx, R. Gross, N. Korolkova, K. G. Fedorov

  <details><summary>摘要 / Abstract</summary>

  Superconducting microwave quantum networks is a rapidly developing field, enabling distributed quantum computing and holding a promise for hybrid architectures in quantum internet. Quantum secret sharing (QSS) is one of the key protocols for multipartite quantum networks and can provide an unconditionally secure way to share quantum states among $n$ players. Using microwave two-mode squeezed states as an entanglement resource, we experimentally implement a QSS protocol with $n = 3$, where a subset of at least $k = 2$ players must collaborate to faithfully reconstruct the original secret state. We demonstrate reconstructed-state fidelities that surpass the asymptotic no-cloning threshold of $F_\textrm{nc} = 2/3$ and identify a parameter regime that allows for unconditionally secure communication in the presence of an omnipotent dishonest player. Furthermore, we experimentally explore inherent connections between QSS and other important quantum information processing tasks, such as quantum dense coding and elementary quantum error correction of channel erasures. Finally, we discuss extensions of QSS and its relation to the concept of blind quantum computing.

  匹配依据：MPC: secret sharing

  </details>

- **MDSS-STAR: Private Heavy-Hitters through Multi-Dealer Secret Sharing**
  2026-04-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/747)
  Harry Eldridge, Aditya Hegde, Brennon Brimhall, Gabrielle Beck, Matthew Green

  <details><summary>摘要 / Abstract</summary>

  We propose a new private telemetry system for computing t-heavy hitters in the STAR (Davidson et al., CCS 2022) and POPSTAR (Li et al., USENIX 2024) model. In this setting, each client generates a report with the assistance of a lightweight Randomness Server and submits it to a central Aggregation Server, which can then locally compute only the heavy hitters. As compared to STAR and POPSTAR---which reveal either the full (pseudonymized) frequency histogram or a complex function of it---our protocol reduces leakage: the Aggregation Server learns non-heavy-hitter values only if their frequency exceeds a well-defined threshold. Additionally, while STAR and POPSTAR are insecure in the face of an Aggregation Server that colludes with clients, our protocol provides optimal security against such a colluding server. To achieve these privacy guarantees, our protocol efficiently adapts multi-dealer secret sharing (Eldridge et al., USENIX 2024) to the STAR/POPSTAR model and introduces a novel oblivious secret-share sampling protocol to ensure security against a colluding Aggregation Server. We implement and benchmark the performance of our protocol and find that it is practical for a number of use cases. Moreover, we show that it supports a tunable three-way tradeoff between correctness, efficiency and privacy.

  匹配依据：MPC: secret sharing

  </details>

- **The Cost of Fluidity: Communication Complexity Trade-offs in Fluid MPC**
  2026-04-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/725)
  Shancheng Zhang, Zongyang Zhang, Bernardo Magri

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) enables mutually distrustful parties to jointly evaluate a function on their private inputs. Classic MPC protocols, however, assume a static set of participants in which every party must remain online throughout the entire computation. Recent advances have introduced MPC models with dynamic participation, such as Fluid MPC, in which computation steps are delegated to a sequence of committees that change across epochs. This approach improves robustness, enabling parties to go offline once their roles are complete. Yet, this flexibility comes at a cost: the most efficient dynamic-participation MPC protocols still incur communication overheads exceeding traditional MPC by more than an order of magnitude. In this work, we formalize the communication complexity of $(d,n)$-threshold secret-sharing-based Fluid MPC. We prove a tight trade-off between communication cost and the adversary&#x27;s corruption threshold, showing that linear communication complexity $O(n)$ is impossible when the corruption threshold $t$ exceeds a proportion of $d$. Matching this bound, we construct a protocol with a communication cost of $9.3n$ elements per multiplication gate against a semi-honest adversary and $37.3n$ elements against a malicious adversary. A C++ implementation confirms that our approach brings the cost of fluidity within practical limits.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **SecDTD: Dynamic Token Drop for Secure Transformers Inference**
  2026-04-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.13670) · [IACR ePrint](https://eprint.iacr.org/2026/731)
  Yifei Cai, Zhuoran Li, Yizhou Feng, Qiao Zhang, Hongyi Wu, Danella Zhao, Chunsheng Xin

  <details><summary>摘要 / Abstract</summary>

  The rapid adoption of Transformer-based AI has been driven by accessible models such as ChatGPT, which provide API-based services for developers and businesses. However, as these online inference services increasingly handle sensitive inputs, privacy concerns have emerged as a significant challenge. To address this, secure inference frameworks have been proposed, but their high computational and communication overhead often limit practical deployment. In plaintext settings, token drop is an effective technique for reducing inference cost; however, our analysis reveals that directly applying such methods to ciphertext scenarios is suboptimal due to distinct cost distributions in secure computation. We propose SecDTD, a dynamic token drop scheme tailored for secure Transformer inference. SecDTD advances token drop by shifting the dropping to earlier inference stages, effectively reducing the cost of key components such as Softmax. To support this, we introduce two core techniques. Max-Centric Normalization (MCN): A novel, Softmax-independent scoring method that enables early token drop with minimal overhead and improved normalization, supporting more aggressive dropping without accuracy loss. OMSel: A faster, oblivious median selection protocol that securely identifies the median of importance scores to support token drop. Compared to existing sorting-based methods, OMSel achieves a 16.9 times speedup while maintaining security, obliviousness and randomness. We evaluate SecDTD through 48 experiments across eight GLUE datasets under various network settings using the BOLT and BumbleBee frameworks. SecDTD achieves 4.47 times end-to-end inference acceleration without degradation in accuracy.

  匹配依据：MPC: secure computation

  </details>

- **Zero-Knowledge Proof of Progress: Secure Multi-Phase Capture-the-Flag Competitions**
  2026-04-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/718)
  Salam Khanji, Behzad Abdolmaleki, John Clark, Aryan Pasikhani

  <details><summary>摘要 / Abstract</summary>

  Existing Capture-the-Flag (CTF) platforms trust a single organizer, offer limited auditability, and are vulnerable to infrastructure-level manipulation. We propose zk–MPSFV, a zk-SNARK-based, multi-phase sub-flag verification scheme that replaces centralized scoring with an on-chain, zero-knowledge, publicly verifiable scoreboard. Challenges are decomposed into sub-challenges arranged as a directed acyclic graph (DAG): a team unlocks the next step only after proving completion of all parent nodes. Sub-flags and decryption keys are jointly generated by n organizers and released via an off-chain (t, n) Shamir–BLS threshold signature produced through multi-party computation (MPC), preventing any single organizer from leaking oraltering keys. Teams submit zk-PLONK proofs that the contract verifies, timestamps, and records immutably. Under standard assumptions (collision-resistant hashing, SNARK soundness/zero-knowledge, IND-CCA2 ECIES, and at least t honest organizers), we prove that zk–MPSFV achieves the stated security goals, including DAG-gated progress, anti-replay, and threshold-robust organizer security, while out-of-band flag sharing remains out of scope. On a three-organizer testbed with 30 simulated teams, setup costs 0.45 ms per sub-flag, proof generation averages 5.34 s on an 8 core system, and on-chain verification costs ≈ 170k L2 gas on zkSync Era with a median fee of 1.33 × 10−6 ETH (about $0.0046 at $3,435 ETH). Stress replays sustain ≈ 7 proof transactions/s up to 5000 proofs; extrapolating to 50,000 proofs (1000 teams × 50 submissions) yields ≈ 0.0665 ETH (about $200–$228) and ≈ 2 hours of settlement time. Overall, zk–MPSFV is practical for small- to mid-scale, audit-ready progression CTFs.

  匹配依据：MPC: multi party computation

  </details>

- **How to reconstruct (anonymously) a secret cellular automaton**
  2026-04-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.11362)
  Luca Mariot, Federico Mazzone, Luca Manzoni, Alberto Leporati

  <details><summary>摘要 / Abstract</summary>

  We consider threshold secret sharing schemes based on cellular automata (CA) that allows for anonymous reconstruction, meaning that the secret can be recovered only as a function of the shares, without knowing the participants&#x27; identities. To this end, we revisit the basic characterization of $(2,n)$ threshold schemes based on CA in terms of Mutually Orthogonal Latin Squares (MOLS), and redefine the secret space as the MOLS family itself, showing that the new resulting scheme enables anonymous reconstruction of secret CA rules. Finally, we discuss the trade-off between the number of secret CA that can be shared and the computational complexity of the recovery phase.

  匹配依据：MPC: secret sharing

  </details>

- **ABRA-CAPA-DABRA: Full break of CAPA**
  2026-04-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/720)
  Paco Azevedo-Oliveira

  <details><summary>摘要 / Abstract</summary>

  In a paper presented at CRYPTO18, Reparaz et al. introduce a new model called the ``Tile-Probe-and-Fault-Model&#x27;&#x27;. This model proposes to cover more realistic side-channel attacks by considering so-called ``combined&#x27;&#x27; attacks, in other words attacks using both side-channel leakage and fault injection. In addition, they introduce CAPA, a combined ``Countermeasure Against Physical Attacks&#x27;&#x27;, which is inspired by an MPC protocol called SPDZ. In this paper, by attacking the original Beaver triples generation described in CAPA, we demonstrate that the CAPA countermeasure is not secure in its model, by breaking the countermeasures with a simple resolution of a linear system.

  匹配依据：MPC: mpc (context)

  </details>

- **Chorus: Secret Recovery with Ephemeral Client Committees**
  2026-04-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/715)
  Deevashwer Rathee, Emma Dauterman, Allison Li, Raluca Ada Popa

  <details><summary>摘要 / Abstract</summary>

  End-to-end encrypted applications protect user data by ensuring that user secrets are only available on client devices. However, if a user loses all of their devices, they need a way to recover their data using only a short password. To realize a password-based secret recovery system resilient to brute-force attacks, prior works relied on secure hardware or a few non-colluding servers. In this work, we take a conceptually different approach that distributes trust across the many clients already in the system, while using the server only as an orchestrator without relying on it for privacy. To achieve this, we design and implement Chorus, a secret recovery system that employs ephemeral committees, each consisting of approximately a thousand clients, to provide strong privacy with high scalability. Committees change frequently in Chorus, typically on the order of a few minutes, to severely limit an attacker&#x27;s ability to compromise clients on a committee. We design Chorus for unreliable, resource-constrained clients and show that the per-client overhead decreases as more clients join the system. Assuming each user performs recovery once a year, the expected per-client overhead in Chorus is under $30$ s of computation on a mobile device and $13.2$ MB of communication, both incurred only once every four months in a configuration with $100$M clients, up to $50$M of which may be offline and at most $10$M may be compromised. To achieve this performance, we contribute two key techniques: (i) a password-based secret recovery scheme that confines expensive committee interactions to infrequent, latency-tolerant operations, and (ii) a non-interactive verifiable secret-sharing scheme that reduces client overhead by two orders of magnitude by delegating computation to the server.

  匹配依据：MPC: secret sharing

  </details>

- **Aerial IRS Deployment-Aided Secure Computation Offloading Against DISCO Jamming Attacks**
  2026-04-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.10558)
  Minghui Min, Peng Zhang, Jiayang Xiao, Ruixin Yang, Shiyin Li, Huan Huang, Hongliang Zhang, Zhu Han

  <details><summary>摘要 / Abstract</summary>

  With the rapid growth of Multi-access Edge Computing (MEC), secure and efficient computation offloading from user equipment (UEs) to edge access points (APs) is critical. However, DISCO intelligent reflective surface-based fully-passive jammers (DIRS-based FPJs) use random time-varying phase shifts to launch DISCO jamming attacks, disrupting offloading performance. This paper leverages an aerial intelligent reflective surface (AIRS) to enable secure computation offloading against DISCO jamming by jointly optimizing offloading ratios, AIRS phase shifts, and deployment. A two-timescale (2Ts) framework is proposed to address the optimization challenge caused by the distinct update frequencies of different strategies. Specifically, AIRS deployment is adjusted on a long timescale to boost antijamming capability due to the impracticality of frequent physical adjustment, while offloading ratios and phase shifts are optimized on a short timescale to adapt to DIRS-jammed dynamic channel conditions. We propose a dual-agent deep reinforcement learning (DRL)-based AIRS deployment-aided secure computation offloading (DDADSO) scheme to maximize the secure offloading utility under DISCO jamming. Simulation results verify that the proposed DDADSO scheme outperforms benchmark schemes, demonstrating the effectiveness of AIRS deployment in improving offloading performance against DISCO jamming attacks.

  匹配依据：MPC: secure computation

  </details>

- **Optimizing and Implementing Threshold MAYO**
  2026-04-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/710)
  Diego F. Aranha, Giacomo Borin, Sofia Celi, Guilhem Niot

  <details><summary>摘要 / Abstract</summary>

  Threshold signatures distribute trust across multiple parties, eliminating single points of failure and reducing insider and key-exfiltration risks—properties that are increasingly important for high-assurance deployments and recently emphasized by NIST’s Multi-Party Threshold Cryptography (MPTC) initiative. We present a practical t-out-of-n threshold variant and emulation of MAYO, a post-quantum signature candidate to NIST’s call for additional signatures. Our proposal builds upon the threshold MAYO design of Celi, Escudero and Niot (PQCrypto2025), which we significantly refine to achieve practical performance. To this end, we introduce two algorithmic modifications to MAYO tailored for the distributed setting: (1) Explicit-Salt MAYO, which allows for pre-determined salts to enable a single-round online phase; and (2) Depth-Reduced MAYO, which restructures the signing algorithm to minimize the depth of secret-dependent operations. We then propose a unified protocol framework that integrate these techniques, plus other MPC specific optimizations, with the goal of minimizing online latency. Finally, we provide a concrete instantiation and local emulation in the dishonest majority setting, secure against active adversaries. Our emulation shows that threshold signing is practical at typical threshold sizes and amenable to deployment. By releasing an open-source implementation and reporting end-to-end performance, this work offers a concrete reference for the thresholdization of post-quantum signatures. Clearly the aforementioned framework is not limited to MAYO, and can be applied to the UOV family of signatures more generally.

  匹配依据：MPC: mpc (context)

  </details>

- **EncFormer: Secure and Efficient Transformer Inference over Encrypted Data**
  2026-04-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.09975)
  Yufan Zhu, Chao Jin, Khin Mi Mi Aung, Xiaokui Xiao

  <details><summary>摘要 / Abstract</summary>

  Transformer inference in machine-learning-as-a-service (MLaaS) raises privacy concerns for sensitive user inputs. Prior secure solutions that combine fully homomorphic encryption (FHE) and secure multiparty computation (MPC) are bottlenecked by inefficient FHE kernels, communication-heavy MPC protocols, and expensive FHE-MPC conversions. We present EncFormer, a two-party private Transformer inference framework that introduces Stage Compatible Patterns so that FHE kernels compose efficiently, reducing repacking and conversions. EncFormer also provides a cost analysis model built around a minimal-conversion baseline, enabling principled selection of FHE-MPC boundaries. To further reduce communication, EncFormer proposes a secure complex CKKS-MPC conversion protocol and designs communication-efficient MPC protocols for nonlinearities. With GPU optimizations, evaluations on GPT- and BERT-style models show that EncFormer achieves 1.4x-30.4x lower online MPC communication and 1.3x-9.8x lower end-to-end latency against prior hybrid FHE-MPC systems, and 1.9x-3.5x lower end-to-end latency on BERT-base than FHE-only pipelines under a matched backend, while maintaining near-plaintext accuracy on selected GLUE tasks.

  匹配依据：MPC: secure multiparty computation

  </details>

- **S3CDM: A secret-sharing-scheme-based cyberattack detection model and its simulation implementation**
  2026-04-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.09924)
  Chi Sing Chum, Jia Lu, Claire Tang, Xiaowen Zhang

  <details><summary>摘要 / Abstract</summary>

  We design and develop a secret-sharing-scheme-based cyberattack detection model(S3CDM)that can detect unauthorized or illegal activities (especially insider attacks) and protect sensitive information within complex network infrastructures of large organizations. The model splits a secret among a group of legitimate participants or components for authentication, integration and detection of unauthorized activities. Traditional Shamir&#x27;s polynomial interpolation based and our own hash function based schemes are utilized in the model, they both are practical and efficient to make sure the communications between different components are secure and any unauthorized activities can be detected. The model offers a flexible multi-factor authentication method to enhance the overall system security. Probability analysis [3] shows that multiple component model is more resistant against cyberattacks than the single component one. To demonstrate the feasibility, we implement the S3CDM in three parts on Google Cloud Platform, i.e., the front end UI (User Interface) running on an HTTP server, the back end individual services written in Python, and a PostgreSQL database. Docker is used to manage the start and stop of individual services and their URLs. We demonstrate how to use the UI with a use case of simulation of broken path in details.

  匹配依据：MPC: secret sharing

  </details>

- **On Worst-Case Optimal Polynomial Intersection**
  2026-04-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.09533)
  Yihang Sun, Mary Wootters

  <details><summary>摘要 / Abstract</summary>

  The Optimal Polynomial Intersection (OPI) problem is the following: Given sets $S_1, \ldots, S_m \subseteq \mathbb{F}$ and evaluation points $a_1, \ldots, a_m \in \mathbb{F}$, find a polynomial $Q \in \mathbb{F}[x]$ of degree less than $n$ so that $Q(a_i) \in S_i$ for as many $i \in \{1, 2, \ldots, m\}$ as possible. Decoded Quantum Interferometry (DQI) is a quantum algorithm that efficiently returns good solutions to the problem, even on worst-case instances (Jordan et. al., 2025). The quality of the solutions returned follows a semicircle law, which outperforms known efficient classical algorithms. But does DQI obtain the best possible solutions? That is, are there solutions better than the semicircle law for worst-case OPI instances? Surprisingly, before this work, the best existential results coincide with (and follow from) the best algorithmic results. In this work, we show that there are better solutions for worst-case OPI instances over prime fields. In particular, DQI and the semicircle law are not optimal. For example, when the lists $S_i$ have size $ρp$ for $ρ\sim 1/2$, our results imply the existence of a solution that asymptotically beats the semicircle law whenever $n/m \geq 0.6225$, and we show that an asymptotically perfect solution exists whenever $n/m \geq 0.7496$. Our results generalize to Max-LINSAT problems derived from any Maximum Distance Separable (MDS) code, and to any $ρ\in (0,1)$. The key insight to our improvement is a connection to local leakage resilience of secret sharing schemes. Along the way, we recover several re-proofs of the existence of solutions achieving the semicircle law.

  匹配依据：MPC: secret sharing

  </details>

- **Scalable and Private Federated Learning Using Distributed Differential Privacy and Secure Aggregation**
  2026-04-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.07125)
  Wenjing Wei, Farid Nait-Abdesselam, Alla Jammine

  <details><summary>摘要 / Abstract</summary>

  This article presents DDP-SA, a scalable privacy-preserving federated learning framework that jointly leverages client-side local differential privacy (LDP) and full-threshold additive secret sharing (ASS) for secure aggregation. Unlike existing methods that rely solely on differential privacy or on secure multi-party computation (MPC), DDP-SA integrates both techniques to deliver stronger end-to-end privacy guarantees while remaining computationally practical. The framework introduces a two-stage protection mechanism: clients first perturb their local gradients with calibrated Laplace noise, then decompose the noisy gradients into additive secret shares that are distributed across multiple intermediate servers. This design ensures that (i) no single compromised server or communication channel can reveal any information about individual client updates, and (ii) the parameter server reconstructs only the aggregated noisy gradient, never any client-specific contribution. Extensive experiments show that DDP-SA achieves substantially higher model accuracy than standalone LDP while providing stronger privacy protection than MPC-only approaches. The proposed framework scales linearly with the number of participants and offers a practical, privacy-preserving solution for federated learning applications with controllable computational and communication overhead.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **FLOSS: Fast Linear Online Secret-Shared Shuffling**
  2026-04-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/672)
  Ian Chang, Sela Navot, Alex Ozdemir, Nirvan Tyagi

  <details><summary>摘要 / Abstract</summary>

  Randomly permuting secret data vectors is a core building block in many privacy-preserving protocols, including those for analytics, advertising, and communication. Existing approaches either rely on computation-heavy public key cryptography and zero-knowledge proofs or scale poorly for large vectors due to use of a quasilinear-sized permutation network. This work presents a preprocessing approach to enable fast linear-time online shuffles in the malicious-secure two-party computation (2PC) setting. We propose FLOSS, a 2PC protocol for securely computing any interactive arithmetic permutation circuit, a notion we introduce to capture how higher level protocols are built on secret-shared field arithmetic and permutations. We show how secret-shared sorting (a subprotocol in data analytics) can be described as an arithmetic permutation circuit, and can thus be compiled to an efficient online 2PC protocol using FLOSS. Our implementation and evaluation confirm FLOSS performs online shuffles fast: shuffling $2^{20}$ elements in under 500ms, greater than $800\times$ faster than state-of-the-art alternatives.

  匹配依据：MPC: secure two party computation

  </details>

- **Cryptanalysis of the Legendre Pseudorandom Function over Extension Fields**
  2026-04-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.04833)
  Daksh Pandey

  <details><summary>摘要 / Abstract</summary>

  The Legendre Pseudorandom Function (PRF) is a highly efficient cryptographic primitive built upon the Legendre symbol, valued for its low multiplicative complexity in Multi-Party Computation (MPC) and Zero-Knowledge Proof (ZKP) protocols. While its security over prime fields $\mathbb{F}_p$ is well-documented, recent interest has shifted toward instantiations over extension fields $\mathbb{F}_{p^r}$. This paper presents the first comprehensive cryptanalysis of the single-degree Legendre PRF operating over $\mathbb{F}_{p^r}$. First, we analyze polynomial input encoding under a standard passive threat model (sequential additive counter queries). We demonstrate that while the absence of polynomial carry-overs causes an asynchronous &quot;no-carry fracture&quot; that neutralizes classical sliding-window collision attacks, the fracture itself is deterministically periodic. By introducing a novel &quot;Differential Signature&quot; bucketing technique, we prove that an adversary can systematically group fractured sequences by their structural shapes to bypass this defense, recovering the secret key in $\mathcal{O}(U \cdot p^r/M)$ operations, where $U$ is the unicity distance. Second, we evaluate the PRF under an active Chosen-Query threat model. We demonstrate that an adversary can circumvent the additive fracture by evaluating the PRF along a geometric sequence generated by a primitive polynomial. This structure invokes strict multiplicative homomorphism over $\mathbb{F}^*_{p^r}$, permitting a direct generalization of state-of-the-art table collision attacks to extract the key in $\mathcal{O}(p^r/M)$ operations. Finally, we establish the cryptographic boundaries of these attacks, formally proving the necessity of higher-degree key variants ($d \ge 2$) to achieve exponential security against structural reduction in extension fields.

  匹配依据：MPC: multi party computation

  </details>

- **Tighter Bounds for the Oblivious Bit-Fixing Inner Product Extractor on Biased Seeds**
  2026-04-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/654)
  Jack Doerner, Lawrence Roy

  <details><summary>摘要 / Abstract</summary>

  The Inner Product Extractor (IPE) of Impagliazzo, Levin, and Luby (STOC&#x27;89) takes a seed $h\in\mathbb{F}^\gamma$ and a source $x\in\{0,1\}^\gamma$ for some $\gamma\in\mathbb{N}$ and produces $\langle h,x\rangle$ with error $\varepsilon=\mathsf{SD}((\langle\mathcal{H},\mathcal{X}\rangle,\mathcal{H}),(\mathcal{Y},\mathcal{H}))$ such that $$ \varepsilon\le\frac{1}{2}\sqrt{|\mathbb{F}|^{\gamma}/2^{H_\infty(\mathcal{H})}}\,\,\sqrt{|\mathbb{F}|/2^{H_\infty(\mathcal{X})}} $$ where $\mathcal{Y}$ is the uniform distribution over $\mathbb{F}$, and $\mathcal{H}$ and $\mathcal{X}$ are the independent but possibly non-uniform distributions from which $h$ and $x$ are drawn, respectively. In other words, the IPE&#x27;s error grows with the square root of seed bias, at most. This square root arises because prior works bound the squared error using the 2-universality of the IPE. The analysis requires an even power of the error, and the IPE is not $4$-universal. Motivated by applications to multiparty computation, we revisit the problem of the IPE with biased seeds and prove far tighter bounds on the influence of seed bias by bypassing universal hashing. We first prove an Elevated General Leftover Hash Lemma, which yields an $n^{\text{th}}$ root bound for functions that are almost $n$-universal. Bounding number of inputs on which the IPE is not 4-universal yields $\varepsilon=\mathsf{SD}((\langle\mathcal{H},\mathcal{W}\rangle,\mathcal{H}),(\mathcal{Y},\mathcal{H}))$ where $$ \varepsilon\lesssim\frac{2.1}{2}\left(|\mathcal{F}|^\gamma/2^{H_\infty(\mathcal{H})}\right)^{\frac14} \sqrt{|\mathbb{F}|/2^{H_\infty(\mathcal{W})}} $$ for any oblivious bit-fixing source $\mathcal{W}$ with $2^{0.585 H_\infty(\mathcal{W})} \le |\mathbb{F}| \le 2^{H_\infty(\mathcal{W})}$. Next, we use matroid theory to directly analyze the $n$-way multicollision probability of the IPE, yielding an asymptotic bound for any even $n$. For $n\ge4$, $0 &lt; \epsilon \le 0.83/(n - 2)$, and $|\mathbb{F}| \le 2^{(1 - \epsilon)\cdot H_\infty(\mathcal{W})}$, as $|\mathbb{F}|\to\infty$, $$ \varepsilon \le\frac{(n - 1)}{2}\left({|\mathcal{F}|}^\gamma/2^{H_\infty(\mathcal{H})}\right)^{\frac1n} \sqrt{\vphantom{/}2^{-\epsilon\cdot H_\infty(\mathcal{W})}}\,\, (1 + o(1)). $$ Computing a \emph{concrete} version of this bound requires time exponential in $n$. We compute concrete $\{4,6,8\}^{\text{th}}$-root bounds and demonstrate that no one choice of $n$ is optimal. Finally, we introduce a new class of seed-adaptive oblivious bit-fixing sources, extend our results to such sources, and use this extension to fix a bug that we identify in the proof of the oblivious linear evaluation protocol of Doerner et al. (SP&#x27;24).

  匹配依据：MPC: multiparty computation

  </details>

- **Random Robust Secret Sharing with Perfect Privacy and its Applications**
  2026-04-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/653)
  Mohammad Hassan Ameri, Jeremiah Blocki

  <details><summary>摘要 / Abstract</summary>

  Secret Sharing schemes allow a dealer to distribute $n$ shares $s_1,\ldots, s_n$ of a secret $s$ so that any $t$ shares suffice to reconstruct the secret, while any $t-1$ shares reveal no information about $s$. In fact, schemes such as Shamir Secret Sharing satisfy a stronger guarantee called $(t\!-\!1)$-perfect privacy, meaning that for any subset $S \subseteq [n]$ with $|S| \le t-1$, the joint distribution $(s_i)_{i \in S}$ is uniformly distributed over its domain. This strong guarantee is essential for applications such as fuzzy password-authenticated key exchange (fPAKE) and conditional encryption --- a recent cryptographic primitive introduced to enable secure personalized password typo correction. Unfortunately, Shamir secret sharing is not robust: corrupted shares can prevent correct reconstruction or cause reconstruction of an incorrect secret. Existing robust secret sharing schemes address this issue but necessarily sacrifice perfect privacy. We introduce and construct Random Robust Secret Sharing with Perfect Privacy (RRSS), a new notion that preserves $(t\!-\!1)$-perfect privacy while providing robustness against random share corruptions. In our schemes, the secret is recovered with high probability even if an arbitrary subset of up to $n-t$ shares is independently corrupted at random. We demonstrate the utility of RRSS through two applications. First, we present the first practically efficient fPAKE construction that tolerates Hamming errors. Second, we obtain the first efficient conditional encryption scheme for arbitrary Hamming distances, improving upon prior work that achieved efficiency only for constant distances. We implement both constructions and empirically demonstrate their practicality.

  匹配依据：MPC: secret sharing

  </details>

- **Return to the Great Attractor: Strong Evidence for a Steradian-sized Flow Converging at $\\sim$70 Mpc within the GA Supercluster and Aligned with the CMB Dipole**
  2026-04-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.02470)
  Alan Dressler, Andrew Monson

  <details><summary>摘要 / Abstract</summary>

  We used the FourStar near-IR camera on Magellan-Baade to obtain high S/N H-Band imaging of 66 galaxies with radial velocities of 2000 &lt; V &lt; 5000 km/s. Our goal was to use the superior distance measurements of surface-brightness-fluctuations (SBF) to derive ``peculiar velocities&#x27;&#x27; to test claims that the CMB dipole anisotropy, equivalent to $\approx$600 km/s with respect to the Local Group, arises from a &#x27;local&#x27; overdensity in the galaxy/dark-matter distribution -- the Great Attractor. SBF&#x27;s ability to measure distances with 5% accuracy confirms a strong flow over a steradian of the sky peaking at Vpec $\sim$ 1000 km/s and converging to zero at D $\approx$70 Mpc from the Local Group. The modest spatial extent of this flow $R_V$ $\sim$ 5000 km/s is consistent with the original Great Attractor model (a diameter D $\sim$ 140 Mpc), as well as the magnitude and direction of the CMB dipole anisotropy, and the power spectrum of CMB fluctuations -- the latter two arguably the most secure measurements in astrophysics. In contrast, our results are at-odds with reports of comparable amplitude &#x27;bulk flows&#x27; on scales of hundreds of Mpc that themselves may be inconsistent with the expected fluctuations in the CMB for a $Λ$CDM universe. We contend that only distance-estimators as accurate as SBF are able settle the question of whether the CMB dipole arises from the gravitational influence of large-scale structure within, or without $\sim$100 Mpc of the Local Group.

  匹配依据：MPC: mpc (context)

  </details>

- **Quantum-Enhanced Processing with Tensor-Network Frontends for Privacy-Aware Federated Medical Diagnosis**
  2026-04-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.01616)
  Hiroshi Yamauchi, Anders Peter Kragh Dalskov, Hideaki Kawaguchi, Rodney Van Meter

  <details><summary>摘要 / Abstract</summary>

  We propose a privacy-aware hybrid framework for federated medical image classification that combines tensor-network representation learning, MPC-secured aggregation, and post-aggregation quantum refinement. The framework is motivated by two practical constraints in privacy-aware federated learning: MPC can introduce substantial communication overhead, and direct quantum processing of high-dimensional medical images is unrealistic with a small number of qubits. To address both constraints within a single architecture, client-side tensor-network frontends, Matrix Product State (MPS), Tree Tensor Network (TTN), and Multi-scale Entanglement Renormalization Ansatz (MERA), compress local inputs into compact latent representations, after which a Quantum-Enhanced Processor (QEP) refines the aggregated latent feature through quantum-state embedding and observable-based readout. Experiments on PneumoniaMNIST show that the effect of the QEP is frontend-dependent rather than uniform across architectures. In the present setting, the TTN+QEP combination exhibits the most balanced overall profile. The results also suggest that the QEP behaves more stably when the qubit count is sufficiently matched to the latent dimension, while noisy conditions degrade performance relative to the noiseless setting. The MPC benchmark further shows that communication cost is governed primarily by the dimension of the protected latent representation. This indicates that tensor-network compression plays a dual role: it enables small-qubit quantum processing on compressed latent features and reduces the communication overhead associated with secure aggregation. Taken together, these results support a co-design perspective in which representation compression, post-aggregation quantum refinement, and privacy-aware deployment should be optimized jointly.

  匹配依据：MPC: mpc (context)

  </details>

- **One-Shot Secret Sharing with Monotone Access Structures over Classical-Quantum Broadcast Channels**
  2026-04-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.02275)
  Truman Welling, Rémi A. Chou, Aylin Yener

  <details><summary>摘要 / Abstract</summary>

  We consider a secret sharing setting with a monotone access structure involving a control node and $L$ users, connected via a classical-quantum broadcast channel whose input is controlled by the control node, referred to as the dealer. Unlike traditional secret sharing settings, where the dealer fully controls the shares given to each user, in our model, the dealer encodes the secret for transmission over the broadcast channel. This means that the shares received by users are perturbed by the channel and are not fully controlled by the dealer. Our main results are achievable one-shot secret sharing rates, as well as converse bounds for arbitrary monotone access structures. We further derive second-order and asymptotic achievable rates for arbitrary monotone access structures. In the special case where all shares are required to recover the secret, we show that our result coincides with the existing secret sharing capacity over classical channels.

  匹配依据：MPC: secret sharing

  </details>

- **Secure Network Function Computation for General Target and Security Functions**
  2026-04-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.01051)
  Qin Zhou, Fang-Wei Fu

  <details><summary>摘要 / Abstract</summary>

  Secure network function computation is a critical research direction in network coding, which aims to ensure that the target function is correctly computed at the sink node while preventing the wiretapper from obtaining any information about the security function. In this paper, we focus on the general secure network function computation model, where the target function f and the security function ζ are arbitrary, and the wiretapper can eavesdrop on any subset of edges with size at most a given security level. Using information-theoretic techniques, we establish a nontrivial upper bound on the secure computing capacity, which is applicable to arbitrary networks, arbitrary target and security functions, and arbitrary security levels. This upper bound is shown to degenerate to the existing bounds in the literature when the target and security functions are specific forms. Furthermore, we consider two specific models: one where the target function is vector-linear and the security function is the identity function, and another where both functions are vector-linear. For the former, we derive a simplified form of the upper bound on the secure computing capacity via order-theoretic methods and propose an efficient algorithm to compute this bound with linear time complexity in the number of network edges. For the latter, we characterize the equivalent conditions for the computability and security of linear secure network codes, develop two constructive schemes for such codes, and derive an upper bound on the minimal finite field size required for the constructions, thereby obtaining a nontrivial lower bound on the secure computing capacity.

  匹配依据：MPC: secure computing

  </details>

- **Towards Formal Security Proofs of MQOM**
  2026-03-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/629)
  Haruhisa Kosuge, Keita Xagawa

  <details><summary>摘要 / Abstract</summary>

  Recent MPC-in-the-Head (MPCitH) signatures increasingly rely on aggressive GGM-tree optimizations to reduce signature size and computational cost, culminating in __secret-key-root correlated GGM trees__ as used in SBC (Huth and Joux, CRYPTO 2024), MQOM (NIST PQC Standardization for Additional Signature Round-2, 2024), and rBN++ (Kim, Lee, and Son, EUROCRYPT 2025). While this technique yields substantial compression, it introduces a dependency loop in the proof (Kosuge and Xagawa, CiC 2026(3)). We analyze MQOM and resolve this circularity by providing EUF-CMA security proofs for a slightly modified variant. The modifications consist of incorporating a salt into the input of a hash function and modifying the evaluation domain to ensure that all evaluation points are nonzero. For the resulting variant of MQOM, we prove EUF-CMA security for the GF(2) parameter sets in the random-oracle plus ideal-cipher model, assuming EUF-NMA security, standard one-wayness, and a heuristic conjecture on matrices. Our proof combines the H-coefficient technique with one-wayness, which may be of independent interest. We also prove EUF-CMA security in the (quantum) random-oracle model, where block-cipher-based hash functions are modeled as random oracles. The proof relies on EUF-NMA security and partial-guessing one-wayness (Feneuil and Rivain, ASIACRYPT 2026), which can be reduced classically to partial-domain one-wayness.

  匹配依据：MPC: mpc (context)

  </details>

- **Beyond Latency: A System-Level Characterization of MPC and FHE for PPML**
  2026-03-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.00169)
  Pengzhi Huang, Kiwan Maeng, G. Edward Suh

  <details><summary>摘要 / Abstract</summary>

  Privacy protection has become an increasing concern in modern machine learning applications. Privacy-preserving machine learning (PPML) has attracted growing research attention, with approaches such as secure multiparty computation (MPC) and fully homomorphic encryption (FHE) being actively explored. However, existing evaluations of these approaches have frequently been done on a narrow, fragmented setup and only focused on a specific performance metric, such as the online inference latency of a specific batch size. From the existing reports, it is hard to compare different approaches, especially when considering other metrics like energy/cost or broader system setups (various hyperparameters, offline overheads, future hardware/network configurations, etc.). We present a unified characterization of three popular approaches -- two variants of MPC based on arithmetic/binary sharing conversion and function secret sharing, and FHE -- on their performance and cost in performing privacy-preserving inference on multiple CNN and Transformer models. We study a range of LAN and WAN environments, model sizes, batch sizes, and input sequence lengths. We evaluate not only the performance but also the energy consumption and monetary cost of deploying under a realistic scenario, taking into account their offline and online computation/communication overheads. We provide empirical guidance for selecting, optimizing, and deploying these privacy-preserving compute paradigms, and outline how evolving hardware and network trends are likely to shift trade-offs between the two MPC schemes and FHE. This work provides system-level insights for researchers and practitioners who seek to understand or accelerate PPML workloads.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Silent Guardians: Independent and Secure Decision Tree Evaluation Without Chatter**
  2026-03-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.28143)
  Jinyuan Li, Liang Feng Zhang

  <details><summary>摘要 / Abstract</summary>

  As machine learning as a service (MLaaS) gains increasing popularity, it raises two critical challenges: privacy and verifiability. For privacy, clients are reluctant to disclose sensitive private information to access MLaaS, while model providers must safeguard their proprietary models. For verifiability, clients lack reliable mechanisms to ensure that cloud servers execute model inference correctly. Decision trees are widely adopted in MLaaS due to their popularity, interpretability, and broad applicability in domains like medicine and finance. In this context, outsourcing decision tree evaluation (ODTE) enables both clients and model providers to offload their sensitive data and decision tree models to the cloud securely. However, existing ODTE schemes often fail to address both privacy and verifiability simultaneously. To bridge this gap, we propose $\sf PVODTE$, a novel two-server private and verifiable ODTE protocol that leverages homomorphic secret sharing and a MAC-based verification mechanism. $\sf PVODTE$ eliminates the need for server-to-server communication, enabling independent computation by each cloud server. This ``non-interactive&#x27;&#x27; setting addresses the latency and synchronization bottlenecks of prior arts, making it uniquely suitable for wide-area network (WAN) deployments. To our knowledge, $\sf PVODTE$ is the first two-server ODTE protocol that eliminates server-to-server communication. Furthermore, $\sf PVODTE$ achieves security against \emph{malicious} servers, where servers cannot learn anything about the client&#x27;s input or the providers&#x27; decision tree models, and servers cannot alter the inference result without being detected.

  匹配依据：MPC: secret sharing

  </details>

- **Asynchronous Routing for Multipartite Entanglement in Quantum Networks**
  2026-03-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.27551)
  Chenliang Tian, Zebo Yang, Raj Jain, Ramana Kompella, Reza Nejabati, Eneet Kaur, Aiman Erbad, Mounir Hamdi, Mohamed Abdallah

  <details><summary>摘要 / Abstract</summary>

  In quantum networks, one way to communicate is to distribute entanglements through swapping at intermediate nodes. Most existing work primarily aims to create efficient two-party end-to-end entanglement over long distances. However, some scenarios also require remote multipartite entanglement for applications such as quantum secret sharing and multi-party computation. Our previous study improved end-to-end entanglement rates using an asynchronous, tree-based routing scheme that relies solely on local knowledge of entanglement links, conserving unused entanglement and avoiding synchronous operations. This article extends this approach to multipartite entanglements, particularly the three-party Greenberger-Horne-Zeilinger (GHZ) states. It shows that our asynchronous protocol outperforms traditional synchronous methods in entanglement rates, especially as coherence times increase. This approach can also be extended to four-party and larger multipartite GHZ states, highlighting the effectiveness and adaptability of asynchronous routing for multipartite scenarios across various network topologies.

  匹配依据：MPC: multi party computation, secret sharing

  </details>
