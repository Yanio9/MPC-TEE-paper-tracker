# 2023 · MPC · 仅预印本来源 · 第 4/4 页

[总目录](../PAPERS.md) · [上一页](2023-mpc-preprint-03.md)

- **Robust, privacy-preserving, transparent, and auditable on-device blocklisting**
  2023-04-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.02810)
  Kurt Thomas, Sarah Meiklejohn, Michael A. Specter, Xiang Wang, Xavier Llorà, Stephan Somogyi, David Kleidermacher

  <details><summary>摘要 / Abstract</summary>

  With the accelerated adoption of end-to-end encryption, there is an opportunity to re-architect security and anti-abuse primitives in a manner that preserves new privacy expectations. In this paper, we consider two novel protocols for on-device blocklisting that allow a client to determine whether an object (e.g., URL, document, image, etc.) is harmful based on threat information possessed by a so-called remote enforcer in a way that is both privacy-preserving and trustworthy. Our protocols leverage a unique combination of private set intersection to promote privacy, cryptographic hashes to ensure resilience to false positives, cryptographic signatures to improve transparency, and Merkle inclusion proofs to ensure consistency and auditability. We benchmark our protocols -- one that is time-efficient, and the other space-efficient -- to demonstrate their practical use for applications such as email, messaging, storage, and other applications. We also highlight remaining challenges, such as privacy and censorship tensions that exist with logging or reporting. We consider our work to be a critical first step towards enabling complex, multi-stakeholder discussions on how best to provide on-device protections.

  匹配依据：MPC: private set intersection

  </details>

- **New Ways to Garble Arithmetic Circuits**
  2023-04-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/501)
  Marshall Ball, Hanjun Li, Huijia Lin, Tianren Liu

  <details><summary>摘要 / Abstract</summary>

  The beautiful work of Applebaum, Ishai, and Kushilevitz [FOCS&#x27;11] initiated the study of arithmetic variants of Yao&#x27;s garbled circuits. An arithmetic garbling scheme is an efficient transformation that converts an arithmetic circuit $C: \mathcal{R}^n \rightarrow \mathcal{R}^m$ over a ring $\mathcal{R}$ into a garbled circuit $\widehat C$ and $n$ affine functions $L_i$ for $i \in [n]$, such that $\widehat C$ and $L_i(x_i)$ reveals only the output $C(x)$ and no other information of $x$. AIK presented the first arithmetic garbling scheme supporting computation over integers from a bounded (possibly exponentially large) range, based on Learning With Errors (LWE). In contrast, converting $C$ into a Boolean circuit and applying Yao&#x27;s garbled circuit treats the inputs as bit strings instead of ring elements, and hence is not &quot;arithmetic&quot;. In this work, we present new ways to garble arithmetic circuits, which improve the state-of-the-art on efficiency, modularity, and functionality. To measure efficiency, we define the rate of a garbling scheme as the maximal ratio between the bit-length of the garbled circuit $|\widehat C|$ and that of the computation tableau $|C|\ell$ in the clear, where $\ell$ is the bit length of wire values (e.g., Yao&#x27;s garbled circuit has rate $O(\lambda)$). $\bullet$ We present the first constant-rate arithmetic garbled circuit for computation over large integers based on the Decisional Composite Residuosity (DCR) assumption, significantly improving the efficiency of the schemes of Applebaum, Ishai, and Kushilevitz. $\bullet$ We construct an arithmetic garbling scheme for modular computation over $\mathcal{R} = \mathbb{Z}_p$ for any integer modulus $p$, based on either DCR or LWE. The DCR-based instantiation achieves rate $O(\lambda)$ for large $p$. Furthermore, our construction is modular and makes black-box use of the underlying ring and a simple key extension gadget. $\bullet$ We describe a variant of the first scheme supporting arithmetic circuits over bounded integers that are augmented with Boolean computation (e.g., truncation of an integer value, and comparison between two values), while keeping the constant rate when garbling the arithmetic part. To the best of our knowledge, constant-rate (Boolean or arithmetic) garbling was only achieved before using the powerful primitive of indistinguishability obfuscation, or for restricted circuits with small depth.

  匹配依据：MPC: garbled circuit, garbled circuits, garbling scheme

  </details>

- **FLUTE: Fast and Secure Lookup Table Evaluations (Full Version)**
  2023-04-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/499)
  Andreas Brüggemann, Robin Hundt, Thomas Schneider, Ajith Suresh, Hossein Yalame

  <details><summary>摘要 / Abstract</summary>

  The concept of using Lookup Tables (LUTs) instead of Boolean circuits is well-known and been widely applied in a variety of applications, including FPGAs, image processing, and database management systems. In cryptography, using such LUTs instead of conventional gates like AND and XOR results in more compact circuits and has been shown to substantially improve online performance when evaluated with secure multi-party computation. Several recent works on secure floating-point computations and privacy-preserving machine learning inference rely heavily on existing LUT techniques. However, they suffer from either large overhead in the setup phase or subpar online performance. We propose FLUTE, a novel protocol for secure LUT evaluation with good setup and online performance. In a two-party setting, we show that FLUTE matches or even outperforms the online performance of all prior approaches, while being competitive in terms of overall performance with the best prior LUT protocols. In addition, we provide an open-source implementation of FLUTE written in the Rust programming language, and implementations of the Boolean secure two-party computation protocols of ABY2.0 and silent OT. We find that FLUTE outperforms the state of the art by two orders of magnitude in the online phase while retaining similar overall communication.

  匹配依据：MPC: secure multi party computation, secure two party computation

  </details>

- **Force: Highly Efficient Four-Party Privacy-Preserving Machine Learning on GPU**
  2023-04-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/493)
  Tianxiang Dai, Li Duan, Yufan Jiang, Yong Li, Fei Mei, Yulian Sun

  <details><summary>摘要 / Abstract</summary>

  Tremendous efforts have been made to improve the efficiency of secure Multi-Party Computation (MPC), which allows n ≥ 2 parties to jointly evaluate a target function without leaking their own private inputs. It has been confirmed by previous research that Three-Party Computation (3PC) and outsourcing computations to GPUs can lead to huge performance improvement of MPC in computationally intensive tasks such as Privacy-Preserving Machine Learning (PPML). A natural question to ask is whether super-linear performance gain is possible for a linear increase in resources. In this paper, we give an affirmative answer to this question. We propose Force, an extremely efficient Four-Party Computation (4PC) system for PPML. To the best of our knowledge, each party in Force enjoys the least number of local computations, smallest graphic memory consumption and lowest data exchanges between parties. This is achieved by introducing a new sharing type X-share along with MPC protocols in privacy-preserving training and inference that are semi-honest secure in the honest-majority setting. By comparing the results with state-of-the-art research, we showcase that Force is sound and extremely efficient, as it can improve the PPML performance by a factor of 2 to 38 compared with other latest GPU-based semi-honest secure systems, such as Piranha (including SecureML, Falcon, FantasticFour), CryptGPU and CrypTen.

  匹配依据：MPC: secure multi party computation, three party computation

  </details>

- **FedBot: Enhancing Privacy in Chatbots with Federated Learning**
  2023-04-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.03228)
  Addi Ait-Mlouk, Sadi Alawadi, Salman Toor, Andreas Hellander

  <details><summary>摘要 / Abstract</summary>

  Chatbots are mainly data-driven and usually based on utterances that might be sensitive. However, training deep learning models on shared data can violate user privacy. Such issues have commonly existed in chatbots since their inception. In the literature, there have been many approaches to deal with privacy, such as differential privacy and secure multi-party computation, but most of them need to have access to users&#x27; data. In this context, Federated Learning (FL) aims to protect data privacy through distributed learning methods that keep the data in its location. This paper presents Fedbot, a proof-of-concept (POC) privacy-preserving chatbot that leverages large-scale customer support data. The POC combines Deep Bidirectional Transformer models and federated learning algorithms to protect customer data privacy during collaborative model training. The results of the proof-of-concept showcase the potential for privacy-preserving chatbots to transform the customer support industry by delivering personalized and efficient customer service that meets data privacy regulations and legal requirements. Furthermore, the system is specifically designed to improve its performance and accuracy over time by leveraging its ability to learn from previous interactions.

  匹配依据：MPC: secure multi party computation

  </details>

- **Establishing shared secret keys on quantum line networks: protocol and security**
  2023-04-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.01881)
  Mina Doosti, Lucas Hanouz, Anne Marin, Elham Kashefi, Marc Kaplan

  <details><summary>摘要 / Abstract</summary>

  We show the security of multi-user key establishment on a single line of quantum communication. More precisely, we consider a quantum communication architecture where the qubit generation and measurement happen at the two ends of the line, whilst intermediate parties are limited to single-qubit unitary transforms. This network topology has been previously introduced to implement quantum-assisted secret-sharing protocols for classical data, as well as the key establishment, and secure computing. This architecture has numerous advantages. The intermediate nodes are only using simplified hardware, which makes them easier to implement. Moreover, key establishment between arbitrary pairs of parties in the network does not require key routing through intermediate nodes. This is in contrast with quantum key distribution (QKD) networks for which non-adjacent nodes need intermediate ones to route keys, thereby revealing these keys to intermediate parties and consuming previously established ones to secure the routing process. Our main result is to show the security of key establishment on quantum line networks. We show the security using the framework of abstract cryptography. This immediately makes the security composable, showing that the keys can be used for encryption or other tasks.

  匹配依据：MPC: secret sharing, secure computing

  </details>

- **Hyper Suprime-Cam Year 3 Results: Cosmology from Galaxy Clustering and Weak Lensing with HSC and SDSS using the Minimal Bias Model**
  2023-04-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.00705)
  Sunao Sugiyama, Hironao Miyatake, Surhud More, Xiangchong Li, Masato Shirasaki, Masahiro Takada, Yosuke Kobayashi, Ryuichi Takahashi, Takahiro Nishimichi, Atsushi J. Nishizawa, Markus M. Rau, Tianqing Zhang, Roohi Dalal, Rachel Mandelbaum, Michael A. Strauss, Takashi Hamana, Masamune Oguri, Ken Osato, Arun Kannawadi, Robert Armstrong, Yutaka Komiyama, Robert H. Lupton, Nate B. Lust, Satoshi Miyazaki, Hitoshi Murayama, Yuki Okura, Paul A. Price, Philip J. Tait, Masayuki Tanaka, Shiang-Yu Wang

  <details><summary>摘要 / Abstract</summary>

  We present cosmological parameter constraints from a blind joint analysis of three two-point correlation functions measured from the Year 3 Hyper Suprime-Cam (HSC-Y3) imaging data, covering 416 deg$^2$, and the SDSS DR11 spectroscopic galaxies spanning the redshift range $[0.15, 0.70]$. We subdivide the SDSS galaxies into three volume-limited samples separated in redshift, each of which acts as a large-scale structure tracer characterized by the measurement of the projected correlation function, $w_{\rm p}(R)$. We also use the measurements of the galaxy-galaxy weak lensing signal $ΔΣ(R)$ for each of these SDSS samples which act as lenses for a secure sample of source galaxies selected from the HSC-Y3 shape catalog based on their photometric redshifts. We combine these measurements with the cosmic shear correlation functions, $ξ_{\pm}(\vartheta)$, measured for our HSC source sample. We model these observables with the minimal bias model of the galaxy clustering observables in the context of a flat $Λ$CDM cosmology. We use conservative scale cuts, $R&gt;12$ and $8~h^{-1}$Mpc, for $ΔΣ$ and $w_{\rm p}$, respectively, where the minimal bias model is valid, in addition to conservative prior on the residual bias in the mean redshift of the HSC photometric source galaxies. Our baseline analysis yields $S_8=0.775^{+0.043}_{-0.038}$ (68% C.I.) for the $Λ$CDM model, after marginalizing over uncertainties in other parameters. Our value of $S_8$ is consistent with that from the Planck 2018 data, but the credible interval of our result is still relatively large. Our results are statistically consistent with those of a companion paper, which extends this analysis to smaller scales with an emulator-based halo model.

  匹配依据：MPC: mpc (context)

  </details>

- **A private set intersection protocol based on multi-party quantum computation for greatest common divisor**
  2023-04-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/476)
  Muhammad Imran

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) is a cryptographic primitive that allows two or more parties to learn the intersection of their input sets and nothing else. In this paper, we present a private set intersection protocol based on a new secure multi-party quantum protocol for greatest common divisor (GCD). The protocol is mainly inspired by the recent quantum private set union protocol based on least common multiple by Liu, Yang, and Li. Performance analysis guarantees the correctness and it also shows that the proposed protocols are completely secure in semi-honest model. Moreover, the complexity is proven to be efficient (poly logarithmic) in the size of the input sets.

  匹配依据：MPC: private set intersection, private set union

  </details>

- **Secure Floating-Point Training**
  2023-03-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/467)
  Deevashwer Rathee, Anwesh Bhattacharya, Divya Gupta, Rahul Sharma, Dawn Song

  <details><summary>摘要 / Abstract</summary>

  Secure 2-party computation (2PC) of floating-point arithmetic is improving in performance and recent work runs deep learning algorithms with it, while being as numerically precise as commonly used machine learning (ML) frameworks like PyTorch. We find that the existing 2PC libraries for floating-point support generic computations and lack specialized support for ML training. Hence, their latency and communication costs for compound operations (e.g., dot products) are high. We provide novel specialized 2PC protocols for compound operations and prove their precision using numerical analysis. Our implementation BEACON outperforms state-of-the-art libraries for 2PC of floating-point by over $6\times$.

  匹配依据：MPC: secure 2 party computation

  </details>

- **Scalable and Privacy-Preserving Federated Principal Component Analysis**
  2023-03-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.00129)
  David Froelicher, Hyunghoon Cho, Manaswitha Edupalli, Joao Sa Sousa, Jean-Philippe Bossuat, Apostolos Pyrgelis, Juan R. Troncoso-Pastoriza, Bonnie Berger, Jean-Pierre Hubaux

  <details><summary>摘要 / Abstract</summary>

  Principal component analysis (PCA) is an essential algorithm for dimensionality reduction in many data science domains. We address the problem of performing a federated PCA on private data distributed among multiple data providers while ensuring data confidentiality. Our solution, SF-PCA, is an end-to-end secure system that preserves the confidentiality of both the original data and all intermediate results in a passive-adversary model with up to all-but-one colluding parties. SF-PCA jointly leverages multiparty homomorphic encryption, interactive protocols, and edge computing to efficiently interleave computations on local cleartext data with operations on collectively encrypted data. SF-PCA obtains results as accurate as non-secure centralized solutions, independently of the data distribution among the parties. It scales linearly or better with the dataset dimensions and with the number of data providers. SF-PCA is more precise than existing approaches that approximate the solution by combining local analysis results, and between 3x and 250x faster than privacy-preserving alternatives based solely on secure multiparty computation or homomorphic encryption. Our work demonstrates the practical applicability of secure and federated PCA on private distributed datasets.

  匹配依据：MPC: secure multiparty computation

  </details>

- **A new approach on IoT security: n-out-of-n**
  2023-03-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/468)
  Tuğberk KOCATEKİN, Cafer ÇALIŞKAN

  <details><summary>摘要 / Abstract</summary>

  Internet of Things (IoT) has become an established part of our daily lives by interconnecting billions of devices in diverse areas such as health care, smart home technologies, agriculture, etc. However, IoT devices are limited in memory, energy and computational capabilities. This creates a great potential for security issues, since being constrained prevents producers from implementing mostly complex cryptographic algorithms in IoT devices. In this study, we propose a novel method to provide a low-cost and secure communication for constrained IoT devices. The proposed method is based on an $n$-out-of-$n$ secret sharing scheme and mimicks the idea of visual cryptography in a digital setup. Whenever an IoT device communicates with an outer party, it establishes the communication by itself or through a mediary such as a central hub or gateway; in which the latter mostly leads to a single point of failure. Our proposed method aims for a distributed environment in which IoT devices within a secure network collaborate with each other in order to send a message to a master device over an insecure channel.

  匹配依据：MPC: secret sharing

  </details>

- **Secure multiparty quantum computations for greatest common divisor and private set intersection**
  2023-03-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.17196)
  Muhammad Imran

  <details><summary>摘要 / Abstract</summary>

  We present a secure multiparty quantum computation (MPQC) for computing greatest common divisor (GCD) based on quantum multiparty private set union (PSU) by Liu, Yang, and Li. As the first step, we improve the security of the MPQC protocol for computing least common multiple (LCM) by Liu and Li by constructing an efficient exact quantum period-finding algorithm (EQPA) as a subroutine instead of the standard (probabilistic) Shor&#x27;s quantum period-finding algorithm (QPA). The use of EQPA instead of the standard QPA guarantees the correctness of the protocol without repetitions. The improvement of LCM protocol also improves the private set union protocol which is based on computing LCM. Finally, using the same idea of the PSU protocol, we construct a quantum multiparty private set intersection (PSI) by transforming the PSI problem into the problem of computing GCD. Performance analysis shows that the correctness and the unconditional security in the semihonest model are guaranteed directly from the correctness and the security of the subroutine protocols (LCM and PSU protocols). Moreover, we show that the complexity of the proposed protocols is polynomial in the size of the secret inputs and the number of parties.

  匹配依据：MPC: private set intersection, private set union

  </details>

- **Registered FE beyond Predicates: (Attribute-Based) Linear Functions and more**
  2023-03-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/457)
  Pratish Datta, Tapas Pal, Shota Yamada

  <details><summary>摘要 / Abstract</summary>

  This paper introduces the first registered functional encryption RFE scheme tailored for linear functions. Distinctly different from classical functional encryption (FE), RFE addresses the key-escrow issue and negates the master key exfiltration attack. Instead of relying on a centralized trusted authority, it introduces a “key curator” - a fully transparent entity that does not retain secrets. In an RFE framework, users independently generate secret keys and subsequently register their respective public keys, along with their authorized functions, with the key curator. This curator consolidates public keys from various users into a unified, concise master public key. For decryption, users occasionally secure helper decryption keys from the key curator, which they use in conjunction way with their private keys. It is imperative that the aggregate public key, helper decryption keys, ciphertexts, and the times for encryption/decryption are polylogarithmic in the number of registered users. All existing RFE designs were confined to predicates where given the correct credentials a user can retrieve the entire payload from a ciphertext or gain no information about it otherwise. Contrarily, our RFE scheme facilitates the computation of linear functions on encrypted content and extraction of only the computation results. Recognizing potential leaks from linear functions, we further enhance our RFE by incorporating an attribute-based access control mechanism. The outcome is the first registered attribute-based linear FE (RABIPFE), which supports access policies depicted as linear secret sharing schemes LSSS. Our proposed schemes are realized in the common reference string (CRS) model as introduced by Hohenberger et al.[EUROCRYPT 2023], employ simple tools and black-box methods. Specifically, our constructs operate in asymmetric prime-order bilinear group regime setting and are proven secure in the generic bilinear group model. Aligning with all pre-existing black-box RFE designs within the CRS model, our schemes cater to a predetermined maximum user count. A notable variant of our RABIPFE scheme also yields the first efficient register ABE (RABE) system for LSSS access policies in asymmetric prime-order bilinear groups. Conclusively, demonstrating feasibility, we formulated an RFE blueprint that supports general functionalities and an infinite user base, leveraging indistinguishability obfuscation and one-way functions.

  匹配依据：MPC: secret sharing

  </details>

- **Overdrive LowGear 2.0: Reduced-Bandwidth MPC without Sacrifice**
  2023-03-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/462)
  Sebastian Hasler, Toomas Krips, Ralf Küsters, Pascal Reisert, Marc Rivinius

  <details><summary>摘要 / Abstract</summary>

  Some of the most efficient protocols for Multi-Party Computation (MPC) follow a two-phase approach where correlated randomness, in particular Beaver triples, is generated in the offline phase and then used to speed up the online phase. Recently, more complex correlations have been introduced to optimize certain operations even further, such as matrix triples for matrix multiplications. In this paper, our goal is to improve the efficiency of the triple generation in general and in particular for classical field values as well as matrix operations. To this end, we modify the Overdrive LowGear protocol to remove the costly sacrificing step and therewith reduce the round complexity and the bandwidth. We extend the state-of-the-art MP-SPDZ implementation with our new protocols and show that the new offline phase outperforms state-of-the-art protocols for the generation of Beaver triples and matrix triples. For example, we save 33 % in bandwidth compared to Overdrive LowGear.

  匹配依据：MPC: multi party computation

  </details>

- **Tri-State Circuits: A Circuit Model that Captures RAM**
  2023-03-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/455)
  David Heath, Vladimir Kolesnikov, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  We introduce tri-state circuits (TSCs). TSCs form a natural model of computation that, to our knowledge, has not been considered by theorists. The model captures a surprising combination of simplicity and power. TSCs are simple in that they allow only three wire values ($0,1,$ and undefined - $\mathcal{Z}$) and three types of fan-in two gates; they are powerful in that their statically placed gates fire (execute) eagerly as their inputs become defined, implying orders of execution that depend on input. This behavior is sufficient to efficiently evaluate RAM programs. We construct a TSC that emulates $T$ steps of any RAM program and that has only $O(T \cdot \log^3 T \cdot \log \log T)$ gates. Contrast this with the reduction from RAM to Boolean circuits, where the best approach scans all of memory on each access, incurring quadratic cost. We connect TSCs with cryptography by using them to improve Yao&#x27;s Garbled Circuit (GC) technique. TSCs capture the power of garbling far better than Boolean Circuits, offering a more expressive model of computation that leaves per-gate cost essentially unchanged. As an important application, we construct authenticated Garbled RAM (GRAM), enabling constant-round maliciously-secure 2PC of RAM programs. Let $\lambda$ denote the security parameter. We extend authenticated garbling to TSCs; by simply plugging in our TSC-based RAM, we obtain authenticated GRAM running at cost $O(T \cdot \log^3 T \cdot \log \log T \cdot \lambda)$, outperforming all prior work, including prior semi-honest GRAM. We also give semi-honest garbling of TSCs from a one-way function (OWF). This yields OWF-based GRAM at cost $O(T \cdot \log^3 T \cdot \log \log T \cdot \lambda)$, outperforming the best prior OWF-based GRAM by more than factor $\lambda$.

  匹配依据：MPC: garbled circuit

  </details>

- **Federated Learning in MIMO Satellite Broadcast System**
  2023-03-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.16603)
  Raphael Pinard, Mitra Hassani, Wayne Lemieux

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) is a type of distributed machine learning at the wireless edge that preserves the privacy of clients&#x27; data from adversaries and even the central server. Existing federated learning approaches either use (i) secure multiparty computation (SMC) which is vulnerable to inference or (ii) differential privacy which may decrease the test accuracy given a large number of parties with relatively small amounts of data each. To tackle the problem with the existing methods in the literature, In this paper, we introduce incorporate federated learning in the inner-working of MIMO systems.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Non-interactive VSS using Class Groups and Application to DKG**
  2023-03-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/451)
  Aniket Kate, Easwar Vivek Mangipudi, Pratyay Mukherjee, Hamza Saleem, Sri Aravinda Krishnan Thyagarajan

  <details><summary>摘要 / Abstract</summary>

  We put forward a non-interactive verifiable secret sharing (NI-VSS) scheme using class groups – we call it cgVSS. Our construction follows the standard framework of encrypting the shares to a set of recipients and generating a non-interactive proof of correct sharing. However, as opposed to prior works, such as Groth’s [Eprint 2021], or Gentry et al.’s [Eurocrypt 2022], we do not require any range proof - this is possible due to the unique structure of class groups, that enables efficient encryption/decryption of large field elements in the exponent of an ElGamal-style encryption scheme. Importantly, this is possible without destroying the additive holomorphic structure, which is required to make the proof-of-correctness highly efficient. This approach not only substantially simplifies the NI-VSS process, but also outperforms the state-of-art schemes significantly. For example, our implementation shows that for a 150 node system cgVSS outperforms (a simplified implementation of) Groth’s protocol in overall communication complexity by 5.6x, about 9.3 − 9.7x in the dealer time and 2.4 − 2.7x in the receiver time per node. Additionally, we formalize the notion of public verifiability, which enables anyone, possibly outside the participants, to verify the correctness of the dealing. In fact, we re-interpret the notion of public verifiability and extend it to the setting when potentially all recipients may be corrupt and yet can not defy public verifiability – to distinguish from state-of-art, we call this strong public verifiability. Our formalization uses the universal composability framework. Finally, through a generic transformation, we obtain a non-interactive distributed key generation (NI-DKG) scheme for threshold systems, where the secret key is the discrete log of the public key. Our security analysis in the VSS-hybrid model uses a formalization that considers a (strong) public verifiability notion for DKG, even when more than threshold parties are corrupt. Instantiating with cgVSS we obtain a NI-DKG scheme from class groups – we call it cgDKG.

  匹配依据：MPC: secret sharing

  </details>

- **Standard Model Time-Lock Puzzles: Defining Security and Constructing via Composition**
  2023-03-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/439)
  Karim Eldefrawy, Sashidhar Jakkamsetti, Ben Terner, Moti Yung

  <details><summary>摘要 / Abstract</summary>

  The introduction of time-lock puzzles initiated the study of publicly “sending information into the future.” For time-lock puzzles, the underlying security-enabling mechanism is the computational complexity of the operations needed to solve the puzzle, which must be tunable to reveal the solution after a predetermined time, and not before that time. Time-lock puzzles are typically constructed via a commitment to a secret, paired with a reveal algorithm that sequentially iterates a basic function over such commitment. One then shows that short-cutting the iterative process violates cryptographic hardness of an underlying problem. To date, and for more than twenty-five years, research on time-lock puzzles relied heavily on iteratively applying well-structured algebraic functions. However, despite the tradition of cryptography to reason about primitives in a realistic model with standard hardness assumptions (often after initial idealized assumptions), most analysis of time-lock puzzles to date still relies on cryptography modeled (in an ideal manner) as a random oracle function or a generic group function. Moreover, Mahmoody et al. showed that time-lock puzzles with superpolynomial gap cannot be constructed from random-oracles; yet still, current treatments generally use an algebraic trapdoor to efficiently construct a puzzle with a large time gap, and then apply the inconsistent (with respect to Mahmoody et al.) random-oracle idealizations to analyze the solving process. Finally, little attention has been paid to the nuances of composing multi-party computation with timed puzzles that are solved as part of the protocol. In this work, we initiate a study of time-lock puzzles in a model built upon a realistic (and falsifiable) computational framework. We present a new formal definition of residual complexity to characterize a realistic, gradual time-release for time-lock puzzles. We also present a general definition of timed multi-party computation (MPC) and both sequential and concurrent composition theorems for MPC in our model.

  匹配依据：MPC: multi party computation

  </details>

- **Interoperable Private Attribution: A Distributed Attribution and Aggregation Protocol**
  2023-03-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/437)
  Benjamin Case, Richa Jain, Alex Koshelev, Andy Leiserson, Daniel Masny, Thurston Sandberg, Ben Savage, Erik Taubeneck, Martin Thomson, Taiki Yamaguchi

  <details><summary>摘要 / Abstract</summary>

  Measuring people’s interactions that span multiple websites can provide unique insight that enables better products and improves people’s experiences, but directly observing people’s individual journeys creates privacy risks that conflict with the newly emerging privacy model for the web. We propose a protocol that uses the combination of multi-party computation and differential privacy that enables the processing of peoples’ data such that only aggregate measurements are revealed, strictly limiting the information leakage about individual people. Our primary application of this protocol is measuring, in aggregate, the effectiveness of digital advertising without enabling cross-site tracking of individuals. In this paper we formalize our protocol, Interoperable Private Attribution (IPA), and analyze its security. IPA is proposed in the W3C’s Private Advertising Technology Community Group (PATCG) [8]. We have implemented our protocol in the malicious honest majority MPC setting for three parties where network costs dominate compute costs. For processing a query with 1M records it uses around 18GB of network which at \$0.08 per GB leads to a network cost of \$1.44.

  匹配依据：MPC: multi party computation

  </details>

- **Experimental quantum secret sharing based on phase encoding of coherent states**
  2023-03-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.14622)
  Ao Shen, Xiao-Yu Cao, Yang Wang, Yao Fu, Jie Gu, Wen-Bo Liu, Chen-Xun Weng, Hua-Lei Yin, Zeng-Bing Chen

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) is one of the basic communication primitives in future quantum networks which addresses part of the basic cryptographic tasks of multiparty communication and computation. Nevertheless, it is a challenge to provide a practical QSS protocol with security against general attacks. A QSS protocol that balances security and practicality is still lacking. Here, we propose a QSS protocol with simple phase encoding of coherent states among three parties. Removing the requirement of impractical entangled resources and the need for phase randomization, our protocol can be implemented with accessible technology. We provide the finite-key analysis against coherent attacks and implement a proof-of-principle experiment to demonstrate our scheme&#x27;s feasibility. Our scheme achieves a key rate of 85.3 bps under a 35 dB channel loss. Combined with security against general attacks and accessible technology, our protocol is a promising candidate for practical multiparty quantum communication networks.

  匹配依据：MPC: secret sharing

  </details>

- **Ruffle: Rapid 3-party shuffle protocols**
  2023-03-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/431)
  Pranav Shriram A, Nishat Koti, Varsha Bhat Kukkala, Arpita Patra, Bhavish Raj Gopal, Somya Sangal

  <details><summary>摘要 / Abstract</summary>

  Secure shuffle is an important primitive that finds use in several applications such as secure electronic voting, oblivious RAMs, secure sorting, to name a few. For time-sensitive shuffle-based applications that demand a fast response time, it is essential to design a fast and efficient shuffle protocol. In this work, we design secure and fast shuffle protocols relying on the techniques of secure multiparty computation. We make several design choices that aid in achieving highly efficient protocols. Specifically, we consider malicious 3-party computation setting with an honest majority and design robust ring-based protocols. Our shuffle protocols provide a fast online (i.e., input-dependent) phase compared to the state-of-the-art for the considered setting. To showcase the efficiency improvements brought in by our shuffle protocols, we consider two distinct applications of anonymous broadcast and secure graph computation via the GraphSC paradigm. In both cases, multiple shuffle invocations are required. Hence, going beyond standalone shuffle invocation, we identify two distinct scenarios of multiple invocations and provide customised protocols for the same. Further, we showcase that our customized protocols not only provide a fast response time, but also provide improved overall run time for multiple shuffle invocations. With respect to the applications, we not only improve in terms of efficiency, but also work towards providing improved security guarantees, thereby outperforming the respective state-of-the-art works. We benchmark our shuffle protocols and the considered applications to analyze the efficiency improvements with respect to various parameters.

  匹配依据：MPC: 3 party computation, secure multiparty computation

  </details>

- **The Round Complexity of Statistical MPC with Optimal Resiliency**
  2023-03-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/418)
  Benny Applebaum, Eliran Kachlon, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  In STOC 1989, Rabin and Ben-Or (RB) established an important milestone in the fields of cryptography and distributed computing by showing that every functionality can be computed with statistical (information-theoretic) security in the presence of an active (aka Byzantine) rushing adversary that controls up to half of the parties. We study the round complexity of general secure multiparty computation and several related tasks in the RB model. Our main result shows that every functionality can be realized in only four rounds of interaction which is known to be optimal. This completely settles the round complexity of statistical actively-secure optimally-resilient MPC, resolving a long line of research. Along the way, we construct the first round-optimal statistically-secure verifiable secret sharing protocol (Chor, Goldwasser, Micali, and Awerbuch; STOC 1985), show that every single-input functionality (e.g., multi-verifier zero-knowledge) can be realized in 3 rounds, and prove that the latter bound is optimal. The complexity of all our protocols is exponential in the number of parties, and the question of deriving polynomially-efficient protocols is left for future research. Our main technical contribution is a construction of a new type of statistically-secure signature scheme whose existence was open even for smaller resiliency thresholds. We also describe a new statistical compiler that lifts up passively-secure protocols to actively-secure protocols in a round-efficient way via the aid of protocols for single-input functionalities. This compiler can be viewed as a statistical variant of the GMW compiler (Goldreich, Micali, Wigderson; STOC, 1987) that originally employed zero-knowledge proofs and public-key encryption.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Primer: Fast Private Transformer Inference on Encrypted Data**
  2023-03-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.13679)
  Mengxin Zheng, Qian Lou, Lei Jiang

  <details><summary>摘要 / Abstract</summary>

  It is increasingly important to enable privacy-preserving inference for cloud services based on Transformers. Post-quantum cryptographic techniques, e.g., fully homomorphic encryption (FHE), and multi-party computation (MPC), are popular methods to support private Transformer inference. However, existing works still suffer from prohibitively computational and communicational overhead. In this work, we present, Primer, to enable a fast and accurate Transformer over encrypted data for natural language processing tasks. In particular, Primer is constructed by a hybrid cryptographic protocol optimized for attention-based Transformer models, as well as techniques including computation merge and tokens-first ciphertext packing. Comprehensive experiments on encrypted language modeling show that Primer achieves state-of-the-art accuracy and reduces the inference latency by 90.6% ~ 97.5% over previous methods.

  匹配依据：MPC: multi party computation

  </details>

- **Single Instance Self-Masking via Permutations**
  2023-03-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/416)
  Asaf Cohen, Paweł Cyprys, Shlomi Dolev

  <details><summary>摘要 / Abstract</summary>

  Self-masking allows the masking of success criteria, part of a problem instance (such as the sum in a subset-sum instance) that restricts the number of solutions. Self-masking is used to prevent the leakage of helpful information to attackers; while keeping the original solution valid and, at the same time, not increasing the number of unplanned solutions. Self-masking can be achieved by xoring the sums of two (or more) independent subset sum instances \cite{DD20, CDM22}, and by doing so, eliminate all known attacks that use the value of the sum of the subset to find the subset fast, namely, in a polynomial time; much faster than the naive exponential exhaustive search. We demonstrate that the concept of self-masking can be applied to a single instance of the subset sum and a single instance of the permuted secret-sharing polynomials. We further introduce the benefit of permuting the bits of the success criteria, avoiding leakage of information on the value of the $i$&#x27;th bit of the success criteria, in the case of a single instance, or the parity of the $i$&#x27;th bit of the success criteria in the case of several instances. In the case of several instances, we permute the success criteria bits of each instance prior to xoring them with each other. One basic permutation and its nesting versions (e.g., $\pi^i$) are used, keeping the solution space small and at the same time, attempting to create an ``all or nothing&#x27;&#x27; effect, where the result of a wrong $\pi$ trials does not imply much.

  匹配依据：MPC: secret sharing

  </details>

- **Maximally-Fluid MPC with Guaranteed Output Delivery**
  2023-03-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/415)
  Giovanni Deligios, Aarushi Goel, Chen-Da Liu-Zhang

  <details><summary>摘要 / Abstract</summary>

  To overcome the limitations of traditional secure multi-party computation (MPC) protocols that consider a static set of participants, in a recent work, Choudhuri et al. [CRYPTO 2021] introduced a new model called Fluid MPC, which supports {\em dynamic} participants. Protocols in this model allow parties to join and leave the computation as they wish. Unfortunately, known fluid MPC protocols (even with strong honest-majority), either only achieve security with abort, or require strong computational and trusted setup assumptions. In this work, we also consider the &quot;hardest&quot; setting --- called the maximally-fluid model --- where each party can leave the computation after participating in a single round. We study the problem of designing maximally-fluid MPC protocols that achieve security with {guaranteed output delivery}, and obtain the following main results: 1. We design a perfectly secure maximally-fluid MPC protocol, that achieves guaranteed output delivery against unbounded adversaries who are allowed to corrupt less than a third of the parties in every round/committee. 2. For the case where the adversary is allowed to corrupt up to half of the parties in each committee, we present a new computationally secure maximally-fluid MPC protocol with guaranteed output delivery. Unlike prior works that require correlated setup and NIZKs, our construction only uses a common random string setup and is based on linearly-homomorphic equivocal commitments.

  匹配依据：MPC: secure multi party computation

  </details>

- **Efficient Laconic Cryptography from Learning With Errors**
  2023-03-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/404)
  Nico Döttling, Dimitris Kolonelos, Russell W. F. Lai, Chuanwei Lin, Giulio Malavolta, Ahmadreza Rahimi

  <details><summary>摘要 / Abstract</summary>

  Laconic cryptography is an emerging paradigm that enables cryptographic primitives with sublinear communication complexity in just two messages. In particular, a two-message protocol between Alice and Bob is called laconic if its communication and computation complexity are essentially independent of the size of Alice&#x27;s input. This can be thought of as a dual notion of fully-homomorphic encryption, as it enables &quot;Bob-optimized&quot; protocols. This paradigm has led to tremendous progress in recent years. However, all existing constructions of laconic primitives are considered only of theoretical interest: They all rely on non-black-box cryptographic techniques, which are highly impractical. This work shows that non-black-box techniques are not necessary for basic laconic cryptography primitives. We propose a completely algebraic construction of laconic encryption, a notion that we introduce in this work, which serves as the cornerstone of our framework. We prove that the scheme is secure under the standard Learning With Errors assumption (with polynomial modulus-to-noise ratio). We provide proof-of-concept implementations for the first time for laconic primitives, demonstrating the construction is indeed practical: For a database size of $2^{50}$, encryption and decryption are in the order of single digit milliseconds. Laconic encryption can be used as a black box to construct other laconic primitives. Specifically, we show how to construct: - Laconic oblivious transfer - Registration-based encryption scheme - Laconic private-set intersection protocol All of the above have essentially optimal parameters and similar practical efficiency. Furthermore, our laconic encryption can be preprocessed such that the online encryption step is entirely combinatorial and therefore much more efficient. Using similar techniques, we also obtain identity-based encryption with an unbounded identity space and tight security proof (in the standard model).

  匹配依据：MPC: oblivious transfer, private set intersection

  </details>

- **Practical Solutions in Fully Homomorphic Encryption -- A Survey Analyzing Existing Acceleration Methods**
  2023-03-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.10877)
  Yanwei Gong, Xiaolin Chang, Jelena Mišić, Vojislav B. Mišić, Jianhua Wang, Haoran Zhu

  <details><summary>摘要 / Abstract</summary>

  Fully homomorphic encryption (FHE) has experienced significant development and continuous breakthroughs in theory, enabling its widespread application in various fields, like outsourcing computation and secure multi-party computing, in order to preserve privacy. Nonetheless, the application of FHE is constrained by its substantial computing overhead and storage cost. Researchers have proposed practical acceleration solutions to address these issues. This paper aims to provide a comprehensive survey for systematically comparing and analyzing the strengths and weaknesses of FHE acceleration schemes, which is currently lacking in the literature. The relevant researches conducted between 2019 and 2022 are investigated. We first provide a comprehensive summary of the latest research findings on accelerating FHE, aiming to offer valuable insights for researchers interested in FHE acceleration. Secondly, we classify existing acceleration schemes from algorithmic and hardware perspectives. We also propose evaluation metrics and conduct a detailed comparison of various methods. Finally, our study presents the future research directions of FHE acceleration, and also offers both guidance and support for practical application and theoretical research in this field.

  匹配依据：MPC: secure multi party computing

  </details>

- **Linear Codes Constructed From Two Weakly Regular Plateaued Functions with Index (p-1)/2**
  2023-03-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.10833)
  Shudi Yang, Tonghui Zhang, Zheng-An Yao

  <details><summary>摘要 / Abstract</summary>

  Linear codes are the most important family of codes in cryptography and coding theory. Some codes have only a few weights and are widely used in many areas, such as authentication codes, secret sharing schemes and strongly regular graphs. By setting $ p\equiv 1 \pmod 4 $, we construct an infinite family of linear codes using two distinct weakly regular unbalanced (and balanced) plateaued functions with index $ (p-1)/2 $. Their weight distributions are completely determined by applying exponential sums and Walsh transform. As a result, most of our constructed codes have a few nonzero weights and are minimal.

  匹配依据：MPC: secret sharing

  </details>

- **Asymmetric Quantum Secure Multi-Party Computation With Weak Clients Against Dishonest Majority**
  2023-03-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.08865) · [IACR ePrint](https://eprint.iacr.org/2023/379)
  Theodoros Kapourniotis, Elham Kashefi, Dominik Leichtle, Luka Music, Harold Ollivier

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (SMPC) protocols allow several parties that distrust each other to collectively compute a function on their inputs. In this paper, we introduce a protocol that lifts classical SMPC to quantum SMPC in a composably and statistically secure way, even for a single honest party. Unlike previous quantum SMPC protocols, our proposal only requires very limited quantum resources from all but one party; it suffices that the weak parties, i.e. the clients, are able to prepare single-qubit states in the X-Y plane. The novel quantum SMPC protocol is constructed in a naturally modular way, and relies on a new technique for quantum verification that is of independent interest. This verification technique requires the remote preparation of states only in a single plane of the Bloch sphere. In the course of proving the security of the new verification protocol, we also uncover a fundamental invariance that is inherent to measurement-based quantum computing.

  匹配依据：MPC: secure multi party computation

  </details>

- **Weak entanglement improves quantum communication using only product measurements**
  2023-03-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.07907)
  Amélie Piveteau, Alastair A. Abbott, Sadiq Muhammad, Mohamed Bourennane, Armin Tavakoli

  <details><summary>摘要 / Abstract</summary>

  We show that weakly entangled states can improve communication over a qubit channel using only separate, interference-free, measurements of individual photons. We introduce a communication task corresponding to the cryptographic primitive known as secret sharing and show that all steerable two-qubit isotropic states provide a quantum advantage in the success rate using only product measurements. Furthermore, we show that such measurements can even reveal communication advantages from noisy partially entangled states that admit no quantum steering. We then go further and consider a stochastic variant of secret sharing based on more sophisticated, yet standard, partial Bell state analysers, and show that this reveals advantages also for a range of unsteerable isotropic states. By preparing polarisation qubits in unsteerable states, we experimentally demonstrate improved success rates of both secret sharing tasks beyond the best entanglement-unassisted qubit protocol. Our results reveal the capability of simple and scalable measurements in entanglement-assisted quantum communication to overcome large amounts of noise.

  匹配依据：MPC: secret sharing

  </details>

- **Semantically Secure Private Set Intersection over Outsourced Multi-Owner Secret-Shared Databases**
  2023-03-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.06863)
  Dongfang Zhao

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) aims to allow users to find out the commonly shared items among the users without revealing other membership information. The most recently proposed approach to PSI in the database community was Prism, which is built upon secret sharing and the assumption that multiple non-colluding servers are available. One limitation of Prism lies in its semantic security: the encoding on the servers is deterministic, implying that the scheme cannot be indistinguishable under a chosen-plaintext attack (IND-CPA). This paper extends the original PSI scheme of Prism by two orthogonal primitives, namely Kaleido-RND and Kaleido-AES: the former exhibits highly efficient performance with randomized encoding and the latter is provably secure under CPA attacks with more computational overhead. A system prototype is implemented and deployed on a 34-node cluster of SQLite instances. Extensive experiments on the TPC-H benchmark and three real-world applications confirm the effectiveness of the proposed Kaleido primitives.

  匹配依据：MPC: private set intersection, secret sharing

  </details>

- **Composable Long-Term Security with Rewinding**
  2023-03-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/363)
  Robin Berger, Brandon Broadnax, Michael Klooß, Jeremias Mechler, Jörn Müller-Quade, Astrid Ottenhues, Markus Raiber

  <details><summary>摘要 / Abstract</summary>

  Long-term security, a variant of Universally Composable (UC) security introduced by Müller-Quade and Unruh (JoC ’10), allows to analyze the security of protocols in a setting where all hardness assumptions no longer hold after the protocol execution has finished. Such a strict notion is highly desirable when properties such as input privacy need to be guaranteed for a long time, e.g. zero-knowledge proofs for secure electronic voting. Strong impossibility results rule out so-called long-term-revealing setups, e.g. a common reference string (CRS), to achieve long-term security, with known constructions for long-term security requiring hardware assumptions, e.g. signature cards. We circumvent these impossibility results by making use of new techniques, allowing rewinding-based simulation in a way that universal composability is possible. The new techniques allow us to construct a long-term-secure composable commitment scheme in the CRS-hybrid model, which is provably impossible in the notion of Müller-Quade and Unruh. We base our construction on a statistically hiding commitment scheme in the CRS-hybrid model with CCA-like properties. To provide a CCA oracle, we cannot rely on superpolynomial extraction techniques, as statistically hiding commitments do not define a unique value. Thus, we extract the value committed to via rewinding. However, even a CCA “rewinding oracle” without additional properties may be useless, as extracting a malicious committer could require to rewind other protocols the committer participates in. If this is e.g. a reduction, this clearly is forbidden. Fortunately, we can establish the well-known and important property of k-robust extractability, which guarantees that extraction is possible without rewinding k-round protocols the malicious committer participates in. While establishing this property for statistically binding commitment schemes is already non-trivial, it is even more complicated for statistically hiding ones. We then incorporate rewinding-based commitment extraction into the UC framework via a helper in analogy to Canetti, Lin and Pass (FOCS 2010), allowing both adversary and environment to extract statistically hiding commitments. Despite the rewinding, our variant of long-term security is universally composable. Our new framework provides the first setting in which a commitment scheme that is both statistically hiding and composable can be constructed from standard polynomial-time hardness assumptions and a CRS only. Unfortunately, we can prove that our setting does not admit long-term-secure oblivious transfer (and thus general two-party computations). Still, our long-term-secure commitment scheme suffices for natural applications, such as long-term secure and composable (commit-and-prove) zero-knowledge arguments of knowledge.

  匹配依据：MPC: oblivious transfer

  </details>

- **Secure and Multi-Step Computation Offloading and Resource Allocation in Ultra-Dense Multi-Task NOMA-Enabled IoT Networks**
  2023-03-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.06353)
  Tianqing Zhou, Yanyan Fu, Dong Qin, Xuefang Nie, Nan Jiang, Chunguo Li

  <details><summary>摘要 / Abstract</summary>

  Ultra-dense networks are widely regarded as a promising solution to explosively growing applications of Internet-of-Things (IoT) mobile devices (IMDs). However, complicated and severe interferences need to be tackled properly in such networks. To this end, both orthogonal multiple access (OMA) and non-orthogonal multiple access (NOMA) are utilized at first. Then, in order to attain a goal of green and secure computation offloading, under the proportional allocation of computational resources and the constraints of latency and security cost, joint device association, channel selection, security service assignment, power control and computation offloading are done for minimizing the overall energy consumed by all IMDs. It is noteworthy that multi-step computation offloading is concentrated to balance the network loads and utilize computing resources fully. Since the finally formulated problem is in a nonlinear mixed-integer form, it may be very difficult to find its closed-form solution. To solve it, an improved whale optimization algorithm (IWOA) is designed. As for this algorithm, the convergence, computational complexity and parallel implementation are analyzed in detail. Simulation results show that the designed algorithm may achieve lower energy consumption than other existing algorithms under the constraints of latency and security cost.

  匹配依据：MPC: secure computation

  </details>

- **How to achieve bidirectional zero-knowledge authentication?**
  2023-03-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/346)
  Jin Li, Xingyu Li, Chang Chen, Guoyu Yang, Junyang Li, Qi Chen, Hongyang Yan

  <details><summary>摘要 / Abstract</summary>

  Due to the completeness, reliability and zero-knowledge nature, the zero-knowledge proof is widely used to designed various protocols, including zero-knowledge authentication protocols. However, the existing zero-knowledge proof scheme cannot realize bidirectional authentication. In this paper, we design a series of bidirectional zero-knowledge protocols based on two new flavors of operations applicable to multiplicative cyclic group. The two notions are formally defined in this paper. We also provide some formal definitions and properties for the two notions. According to our definitions, any bounded polynomial function defined on multiplicative cyclic group has duality and mirror. Based on the two operations, we introduce and formally define dual commitment scheme and mirror commitment scheme. Besides, we provide two efficient constructions for dual commitment and mirror commitment respectively based on CDH assumption and RSA assumption, and named DCCDH, DCRSA, MCCDH and MCRSA respectively. We also provide the extended version supporting multiple messages in the appendix. Then, we design some efficient non-interactive as well as interactive zero-knowledge authentication protocols based on these commitments. The protocols allow two participants to submit commitments to each other so that they can achieve mutual zero-knowledge authentication only a communication initialization needed. Moreovere , similar to other commitment schemes, our schemes also can be widely used to construction of other schemes for cryptography, such as, verifiable secret sharing, zero-knowledge sets, credentials and content extraction signatures.

  匹配依据：MPC: secret sharing

  </details>

- **Encryption with Quantum Public Keys**
  2023-03-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.05368) · [IACR ePrint](https://eprint.iacr.org/2023/345)
  Alex B. Grilo, Or Sattath, Quoc-Huy Vu

  <details><summary>摘要 / Abstract</summary>

  It is an important question to find constructions of quantum cryptographic protocols which rely on weaker computational assumptions than classical protocols. Recently, it has been shown that oblivious transfer and multi-party computation can be constructed from one-way functions, whereas this is impossible in the classical setting in a black-box way. In this work, we study the question of building quantum public-key encryption schemes from one-way functions and even weaker assumptions. Firstly, we revisit the definition of IND-CPA security to this setting. Then, we propose three schemes for quantum public-key encryption from one-way functions, pseudorandom function-like states with proof of deletion and pseudorandom function-like states, respectively.

  匹配依据：MPC: multi party computation, oblivious transfer

  </details>

- **Shield: Secure Allegation Escrow System with Stronger Guarantees**
  2023-03-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/338)
  Nishat Koti, Varsha Bhat Kukkala, Arpita Patra, Bhavish Raj Gopal

  <details><summary>摘要 / Abstract</summary>

  The rising issues of harassment, exploitation, corruption, and other forms of abuse have led victims to seek comfort by acting in unison against common perpetrators (e.g., #MeToo movement). One way to curb these issues is to install allegation escrow systems that allow victims to report such incidents. The escrows are responsible for identifying victims of a common perpetrator and taking the necessary action to bring justice to them. However, users hesitate to participate in these systems due to the fear of such sensitive reports being leaked to perpetrators, who may further misuse them. Thus, to increase trust in the system, cryptographic solutions are being designed to realize secure allegation escrow (SAE) systems. In the work of Arun et al. (NDSS&#x27;20), which presents the state-of-the-art solution, we identify attacks that can leak sensitive information and compromise victim privacy. We also report issues present in prior works that were left unidentified. To arrest all these breaches, we put forth an SAE system that prevents the identified attacks and retains the salient features from all prior works. The cryptographic technique of secure multi-party computation (MPC) serves as the primary underlying tool in designing our system. At the heart of our system lies a new duplicity check protocol and an improved matching protocol. We also provide additional features such as allegation modification and deletion, which were absent in the state of the art. To demonstrate feasibility, we benchmark the proposed system with state-of-the-art MPC protocols and report the cost of processing an allegation. Different settings that affect system performance are analyzed, and the reported values showcase the practicality of our solution.

  匹配依据：MPC: secure multi party computation

  </details>

- **Secret Sharing Scheme with Perfect Concealment**
  2023-03-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/333)
  Izumi Takeuti, Tomoko Adachi

  <details><summary>摘要 / Abstract</summary>

  In 1979, Shamir and Blakley introduced secret sharing schemes to provide both security and reliability. In this study, we construct two secret sharing schemes with perfect concealment. The first is an \((n,n)\)-threshold scheme by a group. Although the scheme itself is already known, we prove that its concealment is perfect. We propose the second as a new \((2,n)\)-threshold scheme by a quasigroup.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Fair Item Ranking**
  2023-03-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.02916)
  Jia Ao Sun, Sikha Pentyala, Martine De Cock, Golnoosh Farnadi

  <details><summary>摘要 / Abstract</summary>

  Users worldwide access massive amounts of curated data in the form of rankings on a daily basis. The societal impact of this ease of access has been studied and work has been done to propose and enforce various notions of fairness in rankings. Current computational methods for fair item ranking rely on disclosing user data to a centralized server, which gives rise to privacy concerns for the users. This work is the first to advance research at the conjunction of producer (item) fairness and consumer (user) privacy in rankings by exploring the incorporation of privacy-preserving techniques; specifically, differential privacy and secure multi-party computation. Our work extends the equity of amortized attention ranking mechanism to be privacy-preserving, and we evaluate its effects with respect to privacy, fairness, and ranking quality. Our results using real-world datasets show that we are able to effectively preserve the privacy of users and mitigate unfairness of items without making additional sacrifices to the quality of rankings in comparison to the ranking mechanism in the clear.

  匹配依据：MPC: secure multi party computation

  </details>

- **Perfect MPC over Layered Graphs**
  2023-03-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/330)
  Bernardo David, Yuval Ishai, Anders Konring, Eyal Kushilevitz, Varun Narayanan

  <details><summary>摘要 / Abstract</summary>

  The classical &quot;BGW protocol&quot; (Ben-Or, Goldwasser and Wigderson, STOC 1988) shows that secure multiparty computation (MPC) among $n$ parties can be realized with perfect full security if $t &lt; n/3$ parties are corrupted. This holds against malicious adversaries in the &quot;standard&quot; model for MPC, where a fixed set of $n$ parties is involved in the full execution of the protocol. However, the picture is less clear in the mobile adversary setting of Ostrovsky and Yung (PODC 1991), where the adversary may periodically &quot;move&quot; by uncorrupting parties and corrupting a new set of $t$ parties. In this setting, it is unclear if full security can be achieved against an adversary that is maximally mobile, i.e., moves after every round. The question is further motivated by the &quot;You Only Speak Once&quot; (YOSO) setting of Gentry et al. (Crypto 2021), where not only the adversary is mobile but also each round is executed by a disjoint set of parties. Previous positive results in this model do not achieve perfect security, and either assume probabilistic corruption and a nonstandard communication model, or only realize the weaker goal of security-with-abort. The question of matching the BGW result in these settings remained open. In this work, we tackle the above two challenges simultaneously. We consider a layered MPC model, a simplified variant of the fluid MPC model of Choudhuri et al. (Crypto 2021). Layered MPC is an instance of standard MPC where the interaction pattern is defined by a layered graph of width $n$, allowing each party to send secret messages and broadcast messages only to parties in the next layer. We require perfect security against a malicious adversary who may corrupt at most $t$ parties in each layer. Our main result is a perfect, fully secure layered MPC protocol with an optimal corruption threshold of $t &lt; n/3$, thus extending the BGW feasibility result to the layered setting. This implies perfectly secure MPC protocols against a maximally mobile adversary.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Paper 1: The JWST PEARLS View of the El Gordo Galaxy Cluster and of the Structure It Magnifies**
  2023-03-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.03556)
  Brenda L. Frye, Massimo Pascale, Nicholas Foo, Reagen Leimbach, Nikhil Garuda, Paulina Soto Robles, Jake Summers, Carlos Diaz, Patrick Kamieneski, Lukas Furtak, Seth Cohen, Jose Diego, Benjamin Beauchesne, Rogier Windhorst, Steve Willner, Anton M. Koekemoer, Adi Zitrin, Gabriel Caminha, Karina Caputi, Dan Coe, Christopher J. Conselice, Liang Dai, Herve Dole, Simon Driver, Norman Grogin, Kevin Harrington, Rolf A. Jansen, Jean-Paul Kneib, Matt Lehnert, James Lowenthal, Madeline A. Marshall, Felipe Menanteau, Belen Alcalde Pampleiga, Nor Pirzkal, Mari Polletta, Johan Richard, Aaron Robotham, Russell E. Ryan, Michael J. Rutkowski, Christobal Sifon, Scott Tompkins, Daniel Wang, Haojing Yan, Min S. Yun

  <details><summary>摘要 / Abstract</summary>

  The massive galaxy cluster El Gordo (z=0.87) imprints multitudes of gravitationally lensed arcs onto James Webb Space Telescope (JWST) Near-Infrared Camera (NIRCam) images. Eight bands of NIRCam imaging were obtained in the ``Prime Extragalactic Areas for Reionization and Lensing Science&#x27;&#x27; (``PEARLS&#x27;&#x27;) program. PSF-matched photometry across Hubble Space Telescope (HST) and NIRCam filters supplies new photometric redshifts. A new light-traces-mass lens model based on 56 image multiplicities identifies the two mass peaks and yields a mass estimate within 500 kpc of ~(7.0 +/- 0.30) x 10^14 Msun. A search for substructure in the 140 cluster members with spectroscopic redshifts confirms the two main mass components. The southeastern mass peak that contains the BCG is more tightly bound than the northwestern one. The virial mass within 1.7 Mpc is (5.1 +/- 0.60) x 10^14 Msun, lower than the lensing mass. A significant transverse velocity component could mean the virial mass is underestimated. We contribute one new member to the previously known z=4.32 galaxy group. Intrinsic (delensed) positions of the five secure group members span a physical extent of ~60 kpc. Thirteen additional candidates selected by spectroscopic/photometric constraints are small and faint with a mean intrinsic luminosity ~2.2 mag fainter than L*. NIRCam imaging admits a fairly wide range of brightnesses and morphologies for the group members, suggesting a more diverse galaxy population in this galaxy overdensity.

  匹配依据：MPC: mpc (context)

  </details>

- **Efficient and Accurate Range Counting on Privacy-preserving Spatial Data Federation \[Technical Report\]**
  2023-03-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.02842)
  Maocheng Li, Yuxiang Zeng, Lei Chen

  <details><summary>摘要 / Abstract</summary>

  A spatial data federation is a collection of data owners (e.g., a consortium of taxi companies), and collectively it could provide better location-based services (LBS). For example, car-hailing services over a spatial data federation allow end users to easily pick the best offers. We focus on the range counting queries, which are primitive operations in spatial databases but received little attention in related research, especially considering the privacy requirements from data owners, who are reluctant to disclose their proprietary data. We propose a grouping-based technical framework named FedGroup, which groups data owners without compromising privacy, and achieves superior query accuracy (up to 50% improvement) as compared to directly applying existing privacy mechanisms achieving Differential Privacy (DP). Our experimental results also demonstrate that FedGroup runs orders-of-magnitude faster than traditional Secure Multiparty Computation (MPC) based method, and FedGroup even scales to millions of data owners, which is a common setting in the era of ubiquitous mobile devices.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Accurate and Efficient Trajectory-based Contact Tracing with Secure Computation and Geo-Indistinguishability**
  2023-03-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.02838)
  Maocheng Li, Yuxiang Zeng, Libin Zheng, Lei Chen, Qing Li

  <details><summary>摘要 / Abstract</summary>

  Contact tracing has been considered as an effective measure to limit the transmission of infectious disease such as COVID-19. Trajectory-based contact tracing compares the trajectories of users with the patients, and allows the tracing of both direct contacts and indirect contacts. Although trajectory data is widely considered as sensitive and personal data, there is limited research on how to securely compare trajectories of users and patients to conduct contact tracing with excellent accuracy, high efficiency, and strong privacy guarantee. Traditional Secure Multiparty Computation (MPC) techniques suffer from prohibitive running time, which prevents their adoption in large cities with millions of users. In this work, we propose a technical framework called ContactGuard to achieve accurate, efficient, and privacy-preserving trajectory-based contact tracing. It improves the efficiency of the MPC-based baseline by selecting only a small subset of locations of users to compare against the locations of the patients, with the assist of Geo-Indistinguishability, a differential privacy notion for Location-based services (LBS) systems. Extensive experiments demonstrate that ContactGuard runs up to 2.6$\times$ faster than the MPC baseline, with no sacrifice in terms of the accuracy of contact tracing.

  匹配依据：MPC: secure computation, secure multiparty computation

  </details>

- **A Comparison of Methods for Neural Network Aggregation**
  2023-03-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.03488)
  John Pomerat, Aviv Segev

  <details><summary>摘要 / Abstract</summary>

  Deep learning has been successful in the theoretical aspect. For deep learning to succeed in industry, we need to have algorithms capable of handling many inconsistencies appearing in real data. These inconsistencies can have large effects on the implementation of a deep learning algorithm. Artificial Intelligence is currently changing the medical industry. However, receiving authorization to use medical data for training machine learning algorithms is a huge hurdle. A possible solution is sharing the data without sharing the patient information. We propose a multi-party computation protocol for the deep learning algorithm. The protocol enables to conserve both the privacy and the security of the training data. Three approaches of neural networks assembly are analyzed: transfer learning, average ensemble learning, and series network learning. The results are compared to approaches based on data-sharing in different experiments. We analyze the security issues of the proposed protocol. Although the analysis is based on medical data, the results of multi-party computation of machine learning training are theoretical and can be implemented in multiple research areas.

  匹配依据：MPC: multi party computation

  </details>

- **A Sharding-Based Approach for Enhancing Efficiency in ISSDOs for Sharing Scattered Values**
  2023-03-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/319)
  Reza Ghasemi

  <details><summary>摘要 / Abstract</summary>

  Data outsourcing is a solution aimed at addressing the security and reliability issues of data storage by ensuring professional handling of the data. The growing use of outsourcing is causing concern among users due to the lack of assurance regarding the security and reliability of data stored on servers. To address these issues, some attempts have been made to implement Secret Sharing-based Data Outsourcing (SSDO) schemes. The low efficiency of these schemes led researchers to use an index server (IS). However, IS are susceptible to frequency analysis. Bucket-Chain $B^+Tree$ ($BCB^+Tree$) was proposed to tackle the frequency analysis in the current Index Server Secret Sharing-based Data Outsourcing (ISSDO) schemes. Nevertheless, this scheme works very well when the data is discrete with a limited range. Otherwise, the scheme&#x27;s efficiency declines significantly as it has to store one index in each bucket and the number of buckets rises significantly, rendering the use of an IS useless. In this paper, a new data structure is proposed to store the indexes in IS to mitigate this efficiency concern. Briefly, the domain of values is divided into several segments, and indexes of values in each segment are stored inside a $Shard$. Additionally, a data outsourcing scheme has been presented based on the proposed data structure. It can withstand collaboration from up to $k-1$ dishonest servers even if they have access to the IS.

  匹配依据：MPC: secret sharing

  </details>

- **SUPERPACK: Dishonest Majority MPC with Constant Online Communication**
  2023-03-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/307)
  Daniel Escudero, Vipul Goyal, Antigoni Polychroniadou, Yifan Song, Chenkai Weng

  <details><summary>摘要 / Abstract</summary>

  In this work we present a novel actively secure dishonest majority MPC protocol, \textsc{SuperPack}, whose efficiency improves as the number of \emph{honest} parties increases. Concretely, let $0&lt;\epsilon&lt;1/2$ and consider an adversary that corrupts $t&lt;n(1-\epsilon)$ out of $n$ parties. \textsc{SuperPack} requires $6/\epsilon$ field elements of online communication per multiplication gate across all parties, assuming circuit-dependent preprocessing, and $10/\epsilon$ assuming circuit-independent preprocessing. In contrast, most of the previous works such as SPDZ (Damg\aa rd \emph{et al}, ESORICS 2013) and its derivatives perform the same regardless of whether there is only one honest party or a constant (non-majority) fraction of honest parties. A notable exception is due to Goyal \emph{et al} (CRYPTO 2022), which achieves $58/\epsilon + 96/\epsilon^2$ field elements assuming circuit-independent preprocessing. Our work improves this result substantially by a factor of at least $25$ in the circuit-independent preprocessing model. Practically, we also compare our work with the best concretely efficient online protocol Turbospeedz (Ben-Efraim \emph{et al}, ACNS 2019), which achieves $2(1-\epsilon)n$ field elements per multiplication gate among all parties. Our online protocol improves over Turbospeedz as $n$ grows, and as $\epsilon$ approaches $1/2$. For example, if there are $90\%$ corruptions ($\epsilon=0.1$), with $n=50$ our online protocol is $1.5\times$ better than Turbospeedz and with $n=100$ this factor is $3\times$, but for $70\%$ corruptions ($\epsilon=0.3$) with $n=50$ our online protocol is $3.5\times$ better, and for $n=100$ this factor is $7\times$. Our circuit-dependent preprocessing can be instantiated from OLE/VOLE. The amount of OLE/VOLE correlations required in our work is a factor of $\approx \epsilon n/2$ smaller than these required by Le Mans (Rachuri and Scholl, CRYPTO 2022) leveraged to instantiate the preprocessing of Turbospeedz. Our dishonest majority protocol relies on packed secret-sharing and leverages ideas from the honest majority \textsc{TurboPack} (Escudero \emph{et al}, CCS 2022) protocol to achieve concrete efficiency for any circuit topology, not only SIMD. We implement both \textsc{SuperPack} and Turbospeedz and verify with experimental results that our approach indeed leads to more competitive runtimes in distributed environments with a moderately large number of parties.

  匹配依据：MPC: secret sharing

  </details>

- **SMPC Task Decomposition: A Theory for Accelerating Secure Multi-party Computation Task**
  2023-03-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.00343)
  Yuanqing Feng, Tao Bai, Songfeng Lu, Xueming Tang, Junjun Wu

  <details><summary>摘要 / Abstract</summary>

  Today, we are in the era of big data, and data are becoming more and more important, especially private data. Secure Multi-party Computation (SMPC) technology enables parties to perform computing tasks without revealing original data. However, the underlying implementation of SMPC is too heavy, such as garbled circuit (GC) and oblivious transfer(OT). Every time a piece of data is added, the resources consumed by GC and OT will increase a lot. Therefore, it is unacceptable to process large-scale data in a single SMPC task. In this work, we propose a novel theory called SMPC Task Decomposition (SMPCTD), which can securely decompose a single SMPC task into multiple SMPC sub-tasks and multiple local tasks without leaking the original data. After decomposition, the computing time, memory and communication consumption drop sharply. We then decompose three machine learning (ML) SMPC tasks using our theory and implement them based on a hybrid protocol framework called ABY. Furthermore, we use incremental computation technique to expand the amount of data involved in these three SMPC tasks. The experimental results show that after decomposing these three SMPC tasks, the time, memory and communication consumption are not only greatly reduced, but also stabilized within a certain range.

  匹配依据：MPC: garbled circuit, oblivious transfer, secure multi party computation

  </details>

- **Efficient Quantum Secret Sharing Scheme Based On Monotone Span Program**
  2023-03-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.00226)
  Shuangshuang Luo, Zhihui Li, Depeng Meng, Jiansheng Guo

  <details><summary>摘要 / Abstract</summary>

  How to efficiently share secrets among multiple participants is a very important problem in key management. In this paper, we propose a multi-secret sharing scheme based on the GHZ state. First, the distributor uses monotone span program to encode the secrets and generate the corresponding secret shares to send to the participants. Then, each participant uses the generalized Pauli operator to embed its own secret share into the transmitted particle. The participant who wants to get the secrets can get multiple secrets at the same time by performing a GHZ-state joint measurement. Futhermore, the scheme is based on a monotone span program, and its access structure is more general than the access structure (t,n) threshold. Compared with other schemes, our proposed scheme is more efficient, less computational cost.

  匹配依据：MPC: secret sharing

  </details>

- **On Circuit Private, Multikey and Threshold Approximate Homomorphic Encryption**
  2023-02-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/301)
  Kamil Kluczniak, Giacomo Santato

  <details><summary>摘要 / Abstract</summary>

  Homomorphic encryption for approximate arithmetic allows one to encrypt discretized real/complex numbers and evaluate arithmetic circuits over them. The first scheme, called CKKS, was introduced by Cheon et al. (Asiacrypt 2017) and gained tremendous attention. The enthusiasm for CKKS-type encryption stems from its potential to be used in inference or multiparty computation tasks that do not require an exact output. A desirable property for homomorphic encryption is circuit privacy, which requires that a ciphertext leaks no information on the computation performed to obtain it. Despite numerous improvements directed toward improving efficiency, the question of circuit privacy for approximate homomorphic encryption remains open. In this paper, we give the first formal study of circuit privacy for homomorphic encryption over approximate arithmetic. We introduce formal models that allow us to reason about circuit privacy. Then, we show that approximate homomorphic encryption can be made circuit private using tools from differential privacy with appropriately chosen parameters. In particular, we show that by applying an exponential (in the security parameter) Gaussian noise on the evaluated ciphertext, we remove useful information on the circuit from the ciphertext. Crucially, we show that the noise parameter is tight, and taking a lower one leads to an efficient adversary against such a system. We expand our definitions and analysis to the case of multikey and threshold homomorphic encryption for approximate arithmetic. Such schemes allow users to evaluate a function on their combined inputs and learn the output without leaking anything on the inputs. A special case of multikey and threshold encryption schemes defines a so-called partial decryption algorithm where each user publishes a ``masked&#x27;&#x27; version of its secret key, allowing all users to decrypt a ciphertext. Similarly, in this case, we show that applying a proper differentially private mechanism gives us IND-CPA-style security where the adversary additionally gets as input the partial decryptions. This is the first security analysis of approximate homomorphic encryption schemes that consider the knowledge of partial decryptions. As part of our study, we scrutinize recent proposals for the definition and constructions of threshold homomorphic encryption schemes and show new random oracle uninstantiability results that may be of independent interest.

  匹配依据：MPC: multiparty computation

  </details>

- **Advance sharing of quantum shares for quantum secrets**
  2023-02-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.14448)
  Mamoru Shibata, Ryutaroh Matsumoto

  <details><summary>摘要 / Abstract</summary>

  Secret sharing is a cryptographic scheme to encode a secret to multiple shares being distributed to participants, so that only qualified sets of participants can restore the original secret from their shares. When we encode a secret by a secret sharing scheme and distribute shares, sometimes not all participants are accessible, and it is desirable to distribute shares to those participants before a secret information is determined. Secret sharing schemes for classical secrets have been known to be able to distribute some shares before a given secret. Lie et al. found any pure $(k,2k-1)$-threshold secret sharing for quantum secrets can distribute some shares before a given secret. However, it is unknown whether distributing some shares before a given secret is possible with other access structures of secret sharing for quantum secrets. We propose a quantum secret sharing scheme for quantum secrets that can distribute some shares before a given secret with other access structures.

  匹配依据：MPC: secret sharing

  </details>

- **A Formal Treatment of Distributed Key Generation, and New Constructions**
  2023-02-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/292)
  Chelsea Komlo, Ian Goldberg, Douglas Stebila

  <details><summary>摘要 / Abstract</summary>

  In this work, we present a novel generic construction for a Distributed Key Generation (DKG) scheme. Our generic construction relies on three modular cryptographic building blocks. The first is an aggregatable Verifiable Secret Sharing (AgVSS) scheme, the second is a Non-Interactive Key Exchange (NIKE) scheme, and the third is a secure hash function. We give formal definitions for the AgVSS and NIKE schemes, as well as concrete constructions. The utility of this generic construction is flexibility; i.e., any aggregatable VSS and NIKE scheme can be employed, and the construction will remain secure. To prove the security of our generic construction, we introduce formalized game based notions of security for DKGs, building upon existing notions in the literature. However, these prior security notions either were presented informally, omitted important requirements, or assumed certain algebraic structure of the underlying scheme. Our security notions make no such assumption of underlying algebraic structure, and explicitly consider details such as participant consistency, communication patterns, and key validity. Further, our security notions imply simulatability with respect to a target key generation scheme without rewinding. Hence, any construction that is proven secure using our security notions additionally imply UC security. We then present STORM, a concrete instantiation of our generic construction that is secure in the discrete logarithm setting in the random oracle model. STORM is more efficient than related DKG schemes in the literature. Because of its simple design and composability, it is a practical choice for real world settings and standardization efforts.

  匹配依据：MPC: secret sharing

  </details>

- **Lower Bounds for Secret-Sharing Schemes for k-Hypergraphs**
  2023-02-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/289)
  Amos Beimel

  <details><summary>摘要 / Abstract</summary>

  A secret-sharing scheme enables a dealer, holding a secret string, to distribute shares to parties such that only pre-defined authorized subsets of parties can reconstruct the secret. The collection of authorized sets is called an access structure. There is a huge gap between the best known upper bounds on the share size of a secret-sharing scheme realizing an arbitrary access structure and the best known lower bounds on the size of these shares. For an arbitrary $n$-party access structure, the best known upper bound on the share size is $2^{O(n)}$. On the other hand, the best known lower bound on the total share size is much smaller, i.e., $\Omega(n^2/\log (n))$ [Csirmaz, \emph{Studia Sci. Math. Hungar.}]. This lower bound was proved more than 25 years ago and no major progress has been made since. In this paper, we study secret-sharing schemes for $k$-hypergraphs, i.e., for access structures where all minimal authorized sets are of size exactly $k$ (however, unauthorized sets can be larger). We consider the case where $k$ is small, i.e., constant or at most $\log (n)$. The trivial upper bound for these access structures is $O(n\cdot \binom{n-1}{k-1})$ and this can be slightly improved. If there were efficient secret-sharing schemes for such $k$-hypergraphs (e.g., $2$-hypergraphs or $3$-hypergraphs), then we would be able to construct secret-sharing schemes for arbitrary access structures that are better than the best known schemes. Thus, understanding the share size required for $k$-hypergraphs is important. Prior to our work, the best known lower bound for these access structures was $\Omega(n \log (n))$, which holds already for graphs (i.e., $2$-hypergraphs). We improve this lower bound, proving a lower bound of $\Omega(n^{2-1/(k-1)}/k)$ on the total share size for some explicit $k$-hypergraphs, where $3 \leq k \leq \log (n)$. For example, for $3$-hypergraphs we prove a lower bound of $\Omega(n^{3/2})$. For $\log (n)$-hypergraphs, we prove a lower bound of $\Omega(n^{2}/\log (n))$, i.e., we show that the lower bound of Csirmaz holds already when all minimal authorized sets are of size $\log (n)$. Our proof is simple and shows that the lower bound of Csirmaz holds for a simple variant of the access structure considered by Csirmaz. Using our results, we prove a near quadratic separation between the required share size for realizing an explicit access structure and the monotone circuit size describing the access structure,i.e., the share size in $\Omega(n^2/\log(n))$ and the monotone circuit size is $O(n\log(n))$ (where the circuit has depth $3$).

  匹配依据：MPC: secret sharing

  </details>

- **Maximizing Miner Revenue in Transaction Fee Mechanism Design**
  2023-02-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.12895) · [IACR ePrint](https://eprint.iacr.org/2023/283)
  Ke Wu, Elaine Shi, Hao Chung

  <details><summary>摘要 / Abstract</summary>

  Transaction fee mechanism design is a new decentralized mechanism design problem where users bid for space on the blockchain. Several recent works showed that the transaction fee mechanism design fundamentally departs from classical mechanism design. They then systematically explored the mathematical landscape of this new decentralized mechanism design problem in two settings: in the plain setting where no cryptography is employed, and in a cryptography-assisted setting where the rules of the mechanism are enforced by a multi-party computation protocol. Unfortunately, in both settings, prior works showed that if we want the mechanism to incentivize honest behavior for both users as well as miners (possibly colluding with users), then the miner revenue has to be zero. Although adopting a relaxed, approximate notion of incentive compatibility gets around this zero miner-revenue limitation, the scaling of the miner revenue is nonetheless poor. In this paper, we show that if we make a mildly stronger reasonable-world assumption than prior works, we can circumvent the known limitations on miner revenue, and design auctions that generate optimal miner revenue. We also systematically explore the mathematical landscape of transaction fee mechanism design under the new reasonable-world and demonstrate how such assumptions can alter the feasibility and infeasibility landscape.

  匹配依据：MPC: multi party computation

  </details>

- **Actively Secure Half-Gates with Minimum Overhead under Duplex Networks**
  2023-02-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/278)
  Hongrui Cui, Xiao Wang, Kang Yang, Yu Yu

  <details><summary>摘要 / Abstract</summary>

  Actively secure two-party computation (2PC) is one of the canonical building blocks in modern cryptography. One main goal for designing actively secure 2PC protocols is to reduce the communication overhead, compared to semi-honest 2PC protocols. In this paper, we make significant progress in closing this gap by proposing two new actively secure constant-round 2PC protocols, one with one-way communication of $2\kappa+5$ bits per AND gate (for $\kappa$-bit computational security and any statistical security) and one with total communication of $2\kappa+\rho+5$ bits per AND gate (for $\rho$-bit statistical security). In particular, our first protocol essentially matches the one-way communication of semi-honest half-gates protocol. Our optimization is achieved by three new techniques: 1. The recent compression technique by Dittmer et al. (Crypto 2022) shows that a relaxed preprocessing is sufficient for authenticated garbling that does not reveal masked wire values to the garbler. We introduce a new form of authenticated bits and propose a new technique of generating authenticated AND triples to reduce the one-way communication of preprocessing from $5\rho+1$ bits to $2$ bits per AND gate for $\rho$-bit statistical security. 2. Unfortunately, the above compressing technique is only compatible with a less compact authenticated garbled circuit of size $2\kappa+3\rho$ bits per AND gate. We designed a new authenticated garbling that does not use information theoretic MACs but rather dual execution without leakage to authenticate wire values in the circuit. This allows us to use a more compact half-gates based authenticated garbled circuit of size $2\kappa+1$ bits per AND gate, and meanwhile keep compatible with the compression technique. Our new technique can achieve one-way communication of $2\kappa+5$ bits per AND gate. 3. In terms of total communication, we notice that the communication overhead of the consistency checking method by Dittmer et al. (Crypto 2022) can be optimized by adding one-round of interaction and utilizing the Free-XOR property. This reduces the online communication from $2\kappa+3\rho$ bits down to $2\kappa+\rho+1$ bits per AND gate. Combined with our first contribution, this yields total amortized communication of $2\kappa+\rho+5$ bits.

  匹配依据：MPC: garbled circuit, secure two party computation

  </details>

- **Smaller Is Bigger: Rethinking the Embedding Rate of Deep Hiding**
  2023-02-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.11918)
  Han Li, Hangcheng Liu, Shangwei Guo, Mingliang Zhou, Ning Wang, Tao Xiang, Tianwei Zhang

  <details><summary>摘要 / Abstract</summary>

  Deep hiding, concealing secret information using Deep Neural Networks (DNNs), can significantly increase the embedding rate and improve the efficiency of secret sharing. Existing works mainly force on designing DNNs with higher embedding rates or fancy functionalities. In this paper, we want to answer some fundamental questions: how to increase and what determines the embedding rate of deep hiding. To this end, we first propose a novel Local Deep Hiding (LDH) scheme that significantly increases the embedding rate by hiding large secret images into small local regions of cover images. Our scheme consists of three DNNs: hiding, locating, and revealing. We use the hiding network to convert a secret image in a small imperceptible compact secret code that is embedded into a random local region of a cover image. The locating network assists the revealing process by identifying the position of secret codes in the stego image, while the revealing network recovers all full-size secret images from these identified local regions. Our LDH achieves an extremely high embedding rate, i.e., $16\times24$ bpp and exhibits superior robustness to common image distortions. We also conduct comprehensive experiments to evaluate our scheme under various system settings. We further quantitatively analyze the trade-off between the embedding rate and image quality with different image restoration algorithms.

  匹配依据：MPC: secret sharing

  </details>

- **Actively Secure Arithmetic Computation and VOLE with Constant Computational Overhead**
  2023-02-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/270)
  Benny Applebaum, Niv Konstantini

  <details><summary>摘要 / Abstract</summary>

  We study the complexity of two-party secure arithmetic computation where the goal is to evaluate an arithmetic circuit over a finite field $F$ in the presence of an active (aka malicious) adversary. In the passive setting, Applebaum et al. (Crypto 2017) constructed a protocol that only makes a *constant* (amortized) number of field operations per gate. This protocol uses the underlying field $F$ as a black box, makes black-box use of (standard) oblivious transfer, and its security is based on arithmetic analogs of well-studied cryptographic assumptions. We present an actively-secure variant of this protocol that achieves, for the first time, all the above features. The protocol relies on the same assumptions and adds only a minor overhead in computation and communication. Along the way, we construct a highly-efficient Vector Oblivious Linear Evaluation (VOLE) protocol and present several practical and theoretical optimizations, as well as a prototype implementation. Our most efficient variant can achieve an asymptotic rate of $1/4$ (i.e., for vectors of length $w$ we send roughly $4w$ elements of $F$), which is only slightly worse than the passively-secure protocol whose rate is $1/3$. The protocol seems to be practically competitive over fast networks, even for relatively small fields $F$ and relatively short vectors. Specifically, our VOLE protocol has 3 rounds, and even for 10K-long vectors, it has an amortized cost per entry of less than 4 OT&#x27;s and less than 300 arithmetic operations. Most of these operations (about 200) can be pre-processed locally in an offline non-interactive phase. (Better constants can be obtained for longer vectors.) Some of our optimizations rely on a novel intractability assumption regarding the non-malleability of noisy linear codes that may be of independent interest. Our technical approach employs two new ingredients. First, we present a new information-theoretic construction of Conditional Disclosure of Secrets (CDS) and show how to use it in order to immunize the VOLE protocol of Applebaum et al. against active adversaries. Second, by using elementary properties of low-degree polynomials, we show that, for some simple arithmetic functionalities, one can easily upgrade Yao&#x27;s garbled-circuit protocol to the active setting with a minor overhead while preserving the round complexity.

  匹配依据：MPC: garbled circuit, oblivious transfer

  </details>

- **Experimental Demonstration of Sequential Multiparty Quantum Secret Sharing and Quantum Conference Key Agreement**
  2023-02-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.11133)
  Shuaishuai Liu, Zhengguo Lu, Pu Wang, Yan Tian, Qing Lu, Xuyang Wang, Yongmin Li

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) and quantum conference key agreement (QCKA) provide efficient encryption approaches for realizing multi-party secure communication, which are essential components of future quantum networks. We present three practical, scalable, verifiable (k, n) threshold QSS protocols that are secure against eavesdroppers and dishonest players. The proposed QSS protocols eliminate the need for each player preparing the laser source and laser phase locking of the overall players. The dealer can implement the parameter evaluation and get the secret information of each player without the cooperation from other players. We consider the practical security of the proposed QSS systems with Trojan-horse attack, untrusted source intensity fluctuating and untrusted noisy sources. Our QSS systems are versatile, they can support the QCKA protocol by only modifying the classic post-processing and requiring no changes to the underlying hardware architecture. We experimentally implement the QSS and QCKA protocol with five parties over 25 km (55 km) single mode fibers, and achieve a key rate of 0.0061 (7.14*10^-4) bits per pulse. Our work paves the way for the practical applications of future QSS and QCKA.

  匹配依据：MPC: secret sharing

  </details>

- **WW-FL: Secure and Private Large-Scale Federated Learning**
  2023-02-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.09904)
  Felix Marx, Thomas Schneider, Ajith Suresh, Tobias Wehrle, Christian Weinert, Hossein Yalame

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) is an efficient approach for large-scale distributed machine learning that promises data privacy by keeping training data on client devices. However, recent research has uncovered vulnerabilities in FL, impacting both security and privacy through poisoning attacks and the potential disclosure of sensitive information in individual model updates as well as the aggregated global model. This paper explores the inadequacies of existing FL protection measures when applied independently, and the challenges of creating effective compositions. Addressing these issues, we propose WW-FL, an innovative framework that combines secure multi-party computation (MPC) with hierarchical FL to guarantee data and global model privacy. One notable feature of WW-FL is its capability to prevent malicious clients from directly poisoning model parameters, confining them to less destructive data poisoning attacks. We furthermore provide a PyTorch-based FL implementation integrated with Meta&#x27;s CrypTen MPC framework to systematically measure the performance and robustness of WW-FL. Our extensive evaluation demonstrates that WW-FL is a promising solution for secure and private large-scale federated learning.

  匹配依据：MPC: secure multi party computation

  </details>

- **Symphony: Expressive Secure Multiparty Computation with Coordination**
  2023-02-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.10076)
  Ian Sweet, David Darais, David Heath, William Harris, Ryan Estes, Michael Hicks

  <details><summary>摘要 / Abstract</summary>

  Context: Secure Multiparty Computation (MPC) refers to a family of cryptographic techniques where mutually untrusting parties may compute functions of their private inputs while revealing only the function output. Inquiry: It can be hard to program MPCs correctly and efficiently using existing languages and frameworks, especially when they require coordinating disparate computational roles. How can we make this easier? Approach: We present Symphony, a new functional programming language for MPCs among two or more parties. Symphony starts from the single-instruction, multiple-data (SIMD) semantics of prior MPC languages, in which each party carries out symmetric responsibilities, and generalizes it using constructs that can coordinate many parties. Symphony introduces **first-class shares** and **first-class party sets** to provide unmatched language-level expressive power with high efficiency. Knowledge: Developing a core formal language called $λ$-Symphony, we prove that the intuitive, generalized SIMD view of a program coincides with its actual distributed semantics. Thus the programmer can reason about her programs by reading them from top to bottom, even though in reality the program runs in a coordinated fashion, distributed across many machines. We implemented a prototype interpreter for Symphony leveraging multiple cryptographic backends. With it we wrote a variety of MPC programs, finding that Symphony can express optimized protocols that other languages cannot, and that in general Symphony programs operate efficiently. [ full abstract at https://doi.org/10.22152/programming-journal.org/2023/7/14 ]

  匹配依据：MPC: secure multiparty computation

  </details>

- **Certified Everlasting Secure Collusion-Resistant Functional Encryption, and More**
  2023-02-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.10354) · [IACR ePrint](https://eprint.iacr.org/2023/236)
  Taiga Hiroka, Fuyuki Kitagawa, Tomoyuki Morimae, Ryo Nishimaki, Tapas Pal, Takashi Yamakawa

  <details><summary>摘要 / Abstract</summary>

  We study certified everlasting secure functional encryption (FE) and many other cryptographic primitives in this work. Certified everlasting security roughly means the following. A receiver possessing a quantum cryptographic object can issue a certificate showing that the receiver has deleted the cryptographic object and information included in the object was lost. If the certificate is valid, the security is guaranteed even if the receiver becomes computationally unbounded after the deletion. Many cryptographic primitives are known to be impossible (or unlikely) to have information-theoretical security even in the quantum world. Hence, certified everlasting security is a nice compromise (intrinsic to quantum). In this work, we define certified everlasting secure versions of FE, compute-and-compare obfuscation, predicate encryption (PE), secret-key encryption (SKE), public-key encryption (PKE), receiver non-committing encryption (RNCE), and garbled circuits. We also present the following constructions: - Adaptively certified everlasting secure collusion-resistant public-key FE for all polynomial-size circuits from indistinguishability obfuscation and one-way functions. - Adaptively certified everlasting secure bounded collusion-resistant public-key FE for NC1 circuits from standard PKE. - Certified everlasting secure compute-and-compare obfuscation from standard fully homomorphic encryption and standard compute-and-compare obfuscation - Adaptively (resp., selectively) certified everlasting secure PE from standard adaptively (resp., selectively) secure attribute-based encryption and certified everlasting secure compute-and-compare obfuscation. - Certified everlasting secure SKE and PKE from standard SKE and PKE, respectively. - Certified everlasting secure RNCE from standard PKE. - Certified everlasting secure garbled circuits from standard SKE.

  匹配依据：MPC: garbled circuits

  </details>

- **ByzSecAgg: A Byzantine-Resistant Secure Aggregation Scheme for Federated Learning Based on Coded Computing and Vector Commitment**
  2023-02-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.09913)
  Tayyebeh Jahani-Nezhad, Mohammad Ali Maddah-Ali, Giuseppe Caire

  <details><summary>摘要 / Abstract</summary>

  In this paper, we propose ByzSecAgg, an efficient secure aggregation scheme for federated learning that is resistant to Byzantine attacks and privacy leakages. Processing individual updates to manage adversarial behavior, while preserving the privacy of the data against colluding nodes, requires some sort of secure secret sharing. However, the communication load for secret sharing of long vectors of updates can be very high. In federated settings, where users are often edge devices with potential bandwidth constraints, excessive communication overhead is undesirable. ByzSecAgg solves this problem by partitioning local updates into smaller sub-vectors and sharing them using ramp secret sharing. However, this sharing method does not admit bilinear computations, such as pairwise distances calculations, which are needed for distance-based outlier-detection algorithms, and effective methods for mitigating Byzantine attacks. To overcome this issue, each user runs another round of ramp sharing, with a different embedding of the data in the sharing polynomial. This technique, motivated by ideas from coded computing, enables secure computation of pairwise distance. In addition, to maintain the integrity and privacy of the local update, ByzSecAgg also uses a vector commitment method, in which the commitment size remains constant (i.e., does not increase with the length of the local update), while simultaneously allowing verification of the secret sharing process. In terms of communication load, ByzSecAgg significantly outperforms the related baseline scheme, known as BREA.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Performance comparison of the two reconstruction methods for stabilizer-based quantum secret sharing**
  2023-02-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.08663)
  Shogo Chiwaki, Ryutaroh Matsumoto

  <details><summary>摘要 / Abstract</summary>

  Stabilizer-based quantum secret sharing has two methods to reconstruct a quantum secret: The erasure correcting procedure and the unitary procedure. It is known that the unitary procedure has a smaller circuit width. On the other hand, it is unknown which method has smaller depth and fewer circuit gates. In this paper, it is shown that the unitary procedure has smaller depth and fewer circuit gates when the circuits are designed for quantum secret sharing using $[[5, 1, 3]]$ binary stabilizer codes.

  匹配依据：MPC: secret sharing

  </details>

- **Practically Efficient Secure Computation of Rank-based Statistics Over Distributed Datasets**
  2023-02-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.08121)
  Nan Wang, Sid Chi-Kin Chau

  <details><summary>摘要 / Abstract</summary>

  In this paper, we propose a practically efficient model for securely computing rank-based statistics, e.g., median, percentiles and quartiles, over distributed datasets in the malicious setting without leaking individual data privacy. Based on the binary search technique of Aggarwal et al. (EUROCRYPT \textquotesingle 04), we respectively present an interactive protocol and a non-interactive protocol, involving at most $\log ||R||$ rounds, where $||R||$ is the range size of the dataset elements. Besides, we introduce a series of optimisation techniques to reduce the round complexity. Our computing model is modular and can be instantiated with either homomorphic encryption or secret-sharing schemes. Compared to the state-of-the-art solutions, it provides stronger security and privacy while maintaining high efficiency and accuracy. Unlike differential-privacy-based solutions, it does not suffer a trade-off between accuracy and privacy. On the other hand, it only involves $O(N \log ||R||)$ time complexity, which is far more efficient than those bitwise-comparison-based solutions with $O(N^2\log ||R||)$ time complexity, where $N$ is the dataset size. Finally, we provide a UC-secure instantiation with the threshold Paillier cryptosystem and $Σ$-protocol zero-knowledge proofs of knowledge.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Orca: FSS-based Secure Training and Inference with GPUs**
  2023-02-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/206)
  Neha Jawalkar, Kanav Gupta, Arkaprava Basu, Nishanth Chandran, Divya Gupta, Rahul Sharma

  <details><summary>摘要 / Abstract</summary>

  Secure Two-party Computation (2PC) allows two parties to compute any function on their private inputs without revealing their inputs to each other. In the offline/online model for 2PC, correlated randomness that is independent of all inputs to the computation, is generated in a preprocessing (offline) phase and this randomness is then utilized in the online phase once the inputs to the parties become available. Most 2PC works focus on optimizing the online time as this overhead lies on the critical path. A recent paradigm for obtaining efficient 2PC protocols with low online cost is based on the cryptographic technique of function secret sharing (FSS). We build an end-to-end system ORCA to accelerate the computation of FSS-based 2PC protocols with GPUs. Next, we observe that the main performance bottleneck in such accelerated protocols is in storage (due to the large amount of correlated randomness), and we design new FSS-based 2PC protocols for several key functionalities in ML which reduce storage by up to 5×. Compared to prior state-of-the-art on secure training accelerated with GPUs in the same computation model (PIRANHA, Usenix Security 2022), we show that ORCA has 4% higher accuracy, 98× lesser communication, and is 26× faster on CIFAR-10. Moreover, maintaining training accuracy while using fixed-point needs stochastic truncations, and all prior works on secure fixed-point training (including PIRANHA) use insecure protocols for it. We provide the first secure protocol for stochastic truncations and build on it to provide the first evaluation of training with end-to-end security. For secure ImageNet inference, ORCA achieves sub-second latency for VGG-16 and ResNet-50, and outperforms the state-of-the-art by 8 − 103×.

  匹配依据：MPC: secret sharing, secure two party computation

  </details>

- **Lightweight Encryption and Anonymous Routing in NoC based SoCs**
  2023-02-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.06118)
  Subodha Charles, Prabhat Mishra

  <details><summary>摘要 / Abstract</summary>

  Advances in manufacturing technologies have enabled System-on-Chip (SoC) designers to integrate an increasing number of cores on a single SoC. Increasing SoC complexity coupled with tight time-to-market deadlines has led to increased utilization of Intellectual Property (IP) cores from third-party vendors. SoC supply chain is widely acknowledged as a major source of security vulnerabilities. Potentially malicious third-party IPs integrated on the same Network-on-Chip (NoC) with the trusted components can lead to security and trust concerns. While secure communication is a well-studied problem in the computer networks domain, it is not feasible to implement those solutions on resource-constrained SoCs. In this paper, we present a lightweight encryption and anonymous routing protocol for communication between IP cores in NoC based SoCs. Our method eliminates the major overhead associated with traditional encryption and anonymous routing protocols using a novel secret sharing mechanism while ensuring that the desired security goals are met. Experimental results demonstrate that existing security solutions on NoC can introduce significant (1.5X) performance degradation, whereas our approach provides the same security features with minor (4%) impact on performance.

  匹配依据：MPC: secret sharing

  </details>

- **Degree-$D$ Reverse Multiplication-Friendly Embeddings: Constructions and Applications**
  2023-02-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/173)
  Daniel Escudero, Cheng Hong, Hongqing Liu, Chaoping Xing, Chen Yuan

  <details><summary>摘要 / Abstract</summary>

  In the recent work of (Cheon &amp; Lee, Eurocrypt&#x27;22), the concept of a degree-$D$ packing method was formally introduced, which captures the idea of embedding multiple elements of a smaller ring into a larger ring, so that element-wise multiplication in the former is somewhat &quot;compatible&quot; with the product in the latter. Then, several optimal bounds and results are presented, and furthermore, the concept is generalized from one multiplication to degrees larger than two. These packing methods encompass several constructions seen in the literature in contexts like secure multiparty computation and fully homomorphic encryption. One such construction is the concept of reverse multiplication-friendly embeddings (RMFEs), which are essentially degree-2 packing methods. In this work we generalize the notion of RMFEs to \emph{degree-$D$ RMFEs} which, in spite of being &quot;more algebraic&quot; than packing methods, turn out to be essentially equivalent. Then, we present a general construction of degree-$D$ RMFEs by generalizing the ideas on algebraic geometry used to construct traditional degree-$2$ RMFEs which, by the aforementioned equivalence, leads to explicit constructions of packing methods. Furthermore, our theory is given in an unified manner for general Galois rings, which include both rings of the form $\mathbb{Z}_{p^k}$ and fields like $\mathbb{F}_{p^k}$, which have been treated separately in prior works. We present multiple concrete sets of parameters for degree-$D$ RMFEs (including $D=2$), which can be useful for future works. Finally, we apply our RMFEs to the task of non-interactively generating high degree correlations for secure multiparty computation protocols. This requires the use of Shamir secret sharing for a large number of parties, which is known to require large-degree Galois ring extensions. Our RMFE enables the generation of such preprocessing data over small rings, without paying for the multiplicative overhead incurred by using Galois ring extensions of large degree. For our application we also construct along the way, as a side contribution of potential independent interest, a pseudo-random secret-sharing solution for non-interactive generation of packed Shamir-sharings over Galois rings with structured secrets, inspired by the PRSS solutions from (Benhamouda et al, TCC 2021).

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **XFL: A High Performace, Lightweighted Federated Learning Framework**
  2023-02-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.05076) · [Code](https://github.com/paritybit-ai/XFL)
  Hong Wang, Yuanzhi Zhou, Chi Zhang, Chen Peng, Mingxia Huang, Yi Liu, Lintao Zhang

  <details><summary>摘要 / Abstract</summary>

  This paper introduces XFL, an industrial-grade federated learning project. XFL supports training AI models collaboratively on multiple devices, while utilizes homomorphic encryption, differential privacy, secure multi-party computation and other security technologies ensuring no leakage of data. XFL provides an abundant algorithms library, integrating a large number of pre-built, secure and outstanding federated learning algorithms, covering both the horizontally and vertically federated learning scenarios. Numerical experiments have shown the prominent performace of these algorithms. XFL builds a concise configuration interfaces with presettings for all federation algorithms, and supports the rapid deployment via docker containers.Therefore, we believe XFL is the most user-friendly and easy-to-develop federated learning framework. XFL is open-sourced, and both the code and documents are available at https://github.com/paritybit-ai/XFL.

  匹配依据：MPC: secure multi party computation

  </details>

- **On Achieving Privacy-Preserving State-of-the-Art Edge Intelligence**
  2023-02-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.05323)
  Daphnee Chabal, Dolly Sapra, Zoltán Ádám Mann

  <details><summary>摘要 / Abstract</summary>

  Deep Neural Network (DNN) Inference in Edge Computing, often called Edge Intelligence, requires solutions to insure that sensitive data confidentiality and intellectual property are not revealed in the process. Privacy-preserving Edge Intelligence is only emerging, despite the growing prevalence of Edge Computing as a context of Machine-Learning-as-a-Service. Solutions are yet to be applied, and possibly adapted, to state-of-the-art DNNs. This position paper provides an original assessment of the compatibility of existing techniques for privacy-preserving DNN Inference with the characteristics of an Edge Computing setup, highlighting the appropriateness of secret sharing in this context. We then address the future role of model compression methods in the research towards secret sharing on DNNs with state-of-the-art performance.

  匹配依据：MPC: secret sharing

  </details>

- **Secret Sharing on Superconcentrator**
  2023-02-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.04482)
  Yuan Li

  <details><summary>摘要 / Abstract</summary>

  We study the arithmetic circuit complexity of threshold secret sharing schemes by characterizing the graph-theoretic properties of arithmetic circuits that compute the shares. Using information inequalities, we prove that any unrestricted arithmetic circuit (with arbitrary gates and unbounded fan-in) computing the shares must satisfy superconcentrator-like connectivity properties. Specifically, when the inputs consist of the secret and $t-1$ random elements, and the outputs are the $n$ shares of a $(t, n)$-threshold secret sharing scheme, the circuit graph must be a $(t, n)$-concentrator; moreover, after removing the secret input, the remaining graph is a $(t-1, n)$-concentrator. Conversely, we show that any graph satisfying these properties can be transformed into a linear arithmetic circuit computing the shares of a threshold secret sharing scheme, assuming a sufficiently large field. As a consequence, we derive upper and lower bounds on the arithmetic circuit complexity of computing the shares in threshold secret sharing schemes.

  匹配依据：MPC: secret sharing

  </details>

- **FIN: Practical Signature-Free Asynchronous Common Subset in Constant Time**
  2023-02-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/154)
  Sisi Duan, Xin Wang, Haibin Zhang

  <details><summary>摘要 / Abstract</summary>

  Asynchronous common subset (ACS) is a powerful paradigm enabling applications such as Byzantine fault-tolerance (BFT) and multi-party computation (MPC). The most efficient ACS framework in the information-theoretic setting is due to Ben-Or, Kelmer, and Rabin (BKR, 1994). The BKR ACS protocol has been both theoretically and practically impactful. However, the BKR protocol has an $O(\log n)$ running time (where $n$ is the number of replicas) due to the usage of $n$ parallel asynchronous binary agreement (ABA) instances, impacting both performance and scalability. Indeed, for a network of 16$\sim$64 replicas, the parallel ABA phase occupies about 95%$\sim$97% of the total runtime in BKR. A long-standing open problem is whether we can build an ACS framework with $O(1)$ time while not increasing the message or communication complexity of the BKR protocol. In this paper, we resolve the open problem, presenting the first constant-time ACS protocol with $O(n^3)$ messages in the information-theoretic and signature-free settings. Moreover, as a key ingredient of our new ACS framework and an interesting primitive in its own right, we provide the first information-theoretic multivalued validated Byzantine agreement (MVBA) protocol with $O(1)$ time and $O(n^3)$ messages. Both results can improve---asymptotically and concretely---various applications using ACS and MVBA in the information-theoretic, quantum-safe, or signature-free settings. As an example, we implement FIN, a BFT protocol instantiated using our framework. Via a 121-server deployment on Amazon EC2, we show FIN is significantly more efficient than PACE (CCS 2022), the state-of-the-art asynchronous BFT protocol of the same type. In particular, FIN reduces the overhead of the ABA phase to as low as 1.23% of the total runtime, and FIN achieves up to 3.41x the throughput of PACE. We also show that FIN outperforms other BFT protocols with the standard liveness property such as Dumbo and Speeding Dumbo.

  匹配依据：MPC: multi party computation

  </details>

- **The Capacity Region of Distributed Multi-User Secret Sharing under The Perfect Privacy Condition**
  2023-02-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.03920)
  Jiahong Wu, Nan Liu, Wei Kang

  <details><summary>摘要 / Abstract</summary>

  We study the distributed multi-user secret sharing (DMUSS) problem under the perfect privacy condition. In a DMUSS problem, multiple secret messages are deployed and the shares are offloaded to the storage nodes. Moreover, the access structure is extremely incomplete, as the decoding collection of each secret message has only one set, and by the perfect privacy condition such collection is also the colluding collection of all other secret messages. The secret message rate is defined as the size of the secret message normalized by the size of a share. We characterize the capacity region of the DMUSS problem when given an access structure, defined as the set of all achievable rate tuples. In the achievable scheme, we assume all shares are mutually independent and then design the decoding function based on the fact that the decoding collection of each secret message has only one set. Then it turns out that the perfect privacy condition is equivalent to the full rank property of some matrices consisting of different indeterminates and zeros. Such a solution does exist if the field size is bigger than the number of secret messages. Finally with a matching converse saying that the size of the secret is upper bounded by the sum of sizes of non-colluding shares, we characterize the capacity region of DMUSS problem under the perfect privacy condition.

  匹配依据：MPC: secret sharing

  </details>

- **Error-tolerant oblivious transfer in the noisy-storage model**
  2023-02-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.04236)
  Cosmo Lupo, James T. Peat, Erika Andersson, Pieter Kok

  <details><summary>摘要 / Abstract</summary>

  The noisy-storage model of quantum cryptography allows for information-theoretically secure two-party computation based on the assumption that a cheating user has at most access to an imperfect, noisy quantum memory, whereas the honest users do not need a quantum memory at all. In general, the more noisy the quantum memory of the cheating user, the more secure the implementation of oblivious transfer, which is a primitive that allows universal secure two-party and multi-party computation. For experimental implementations of oblivious transfer, one has to consider that also the devices held by the honest users are lossy and noisy, and error correction needs to be applied to correct these trusted errors. The latter are expected to reduce the security of the protocol, since a cheating user may hide themselves in the trusted noise. Here we leverage entropic uncertainty relations to derive tight bounds on the security of oblivious transfer with a trusted and untrusted noise. In particular, we discuss noisy storage and bounded storage, with independent and correlated noise.

  匹配依据：MPC: multi party computation, oblivious transfer, secure two party computation

  </details>

- **Secret sharing scheme based on hashing**
  2023-02-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.02507)
  M. Andrecut

  <details><summary>摘要 / Abstract</summary>

  We propose an adaptive threshold multi secret sharing scheme based solely on cryptographically secure hash functions. We show that the proposed scheme is also: perfect, ideal, verifiable, and proactive. Moreover the proposed scheme has a low computational complexity comparing to the most common schemes operating over finite fields.

  匹配依据：MPC: secret sharing

  </details>

- **Approximate reconstructability of quantum states and noisy quantum secret sharing schemes**
  2023-02-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.02509)
  Yingkai Ouyang, Kaumudibikash Goswami, Jacquiline Romero, Barry C. Sanders, Min-Hsiu Hsieh, Marco Tomamichel

  <details><summary>摘要 / Abstract</summary>

  We introduce and analyse approximate quantum secret sharing in a formal cryptographic setting, wherein a dealer encodes and distributes a quantum secret to players such that authorized structures (sets of subsets of players) can approximately reconstruct the quantum secret and omnipotent adversarial agents controlling non-authorized subsets of players are approximately denied the quantum secret. In particular, viewing the map encoding the quantum secret to shares for players in an authorized structure as a quantum channel, we show that approximate reconstructability of the quantum secret by these players is possible if and only if the information leakage, given in terms of a certain entanglement-assisted capacity of the complementary quantum channel to the players outside the structure and the environment, is small.

  匹配依据：MPC: secret sharing

  </details>

- **RRNet: Towards ReLU-Reduced Neural Network for Two-party Computation Based Private Inference**
  2023-02-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.02292)
  Hongwu Peng, Shanglin Zhou, Yukui Luo, Nuo Xu, Shijin Duan, Ran Ran, Jiahui Zhao, Shaoyi Huang, Xi Xie, Chenghong Wang, Tong Geng, Wujie Wen, Xiaolin Xu, Caiwen Ding

  <details><summary>摘要 / Abstract</summary>

  The proliferation of deep learning (DL) has led to the emergence of privacy and security concerns. To address these issues, secure Two-party computation (2PC) has been proposed as a means of enabling privacy-preserving DL computation. However, in practice, 2PC methods often incur high computation and communication overhead, which can impede their use in large-scale systems. To address this challenge, we introduce RRNet, a systematic framework that aims to jointly reduce the overhead of MPC comparison protocols and accelerate computation through hardware acceleration. Our approach integrates the hardware latency of cryptographic building blocks into the DNN loss function, resulting in improved energy efficiency, accuracy, and security guarantees. Furthermore, we propose a cryptographic hardware scheduler and corresponding performance model for Field Programmable Gate Arrays (FPGAs) to further enhance the efficiency of our framework. Experiments show RRNet achieved a much higher ReLU reduction performance than all SOTA works on CIFAR-10 dataset.

  匹配依据：MPC: secure two party computation, two party computation

  </details>

- **Prism: Private Set Intersection and Union with Aggregation over Multi-Owner Outsourced Data**
  2023-02-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/133)
  Shantanu Sharma, Yin Li, Sharad Mehrotra, Nisha Panwar, Dhrubajyoti Ghosh, Peeyush Gupta

  <details><summary>摘要 / Abstract</summary>

  This paper proposes Prism, Private Verifiable Set Computation over Multi-Owner Outsourced Databases, a secret sharing based approach to compute private set operations (i.e., intersection and union), as well as aggregates over outsourced databases belonging to multiple owners. Prism enables data owners to pre-load the data onto non-colluding servers and exploits the additive and multiplicative properties of secret-shares to compute the above-listed operations in (at most) two rounds of communication between the servers (storing the secret-shares) and the querier, resulting in a very efficient implementation. Also, Prism does not require communication among the servers and supports result verification techniques for each operation to detect malicious adversaries. Experimental results show that Prism scales both in terms of the number of data owners and database sizes, to which prior approaches do not scale.

  匹配依据：MPC: private set intersection, secret sharing

  </details>

- **Verifiable Distributed Aggregation Functions**
  2023-02-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/130)
  Hannah Davis, Christopher Patton, Mike Rosulek, Phillipp Schoppmann

  <details><summary>摘要 / Abstract</summary>

  The modern Internet is built on systems that incentivize collection of information about users. In order to minimize privacy loss, it is desirable to prevent these systems from collecting more information than is required for the application. The promise of multi-party computation is that data can be aggregated without revealing individual measurements to the data collector. This work offers a provable security treatment for &quot;Verifiable Distributed Aggregation Functions (VDAFs)&quot;, a class of multi-party computation protocols being considered for standardization by the IETF. We propose a formal framework for the analysis of VDAFs and apply it to two constructions. The first is Prio3, one of the candidates for standardization. This VDAF is based on the Prio system of Corrigan-Gibbs and Boneh (NSDI 2017). We prove that Prio3 achieves our security goals with only minor changes to the draft. The second construction, called Doplar, is introduced by this paper. Doplar is a round-reduced variant of the Poplar system of Boneh et al. (IEEE S&amp;P 2021), itself a candidate for standardization. The cost of this improvement is a modest increase in overall bandwidth and computation.

  匹配依据：MPC: multi party computation

  </details>

- **An Effective and Differentially Private Protocol for Secure Distributed Cardinality Estimation**
  2023-02-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.02158)
  Pinghui Wang, Chengjin Yang, Dongdong Xie, Junzhou Zhao, Hui Li, Jing Tao, Xiaohong Guan

  <details><summary>摘要 / Abstract</summary>

  Counting the number of distinct elements distributed over multiple data holders is a fundamental problem with many real-world applications ranging from crowd counting to network monitoring. Although a number of space and computational efficient sketch methods (e.g., the Flajolet-Martin sketch and the HyperLogLog sketch) for cardinality estimation have been proposed to solve the above problem, these sketch methods are insecure when considering privacy concerns related to the use of each data holder&#x27;s personal dataset. Despite a recently proposed protocol that successfully implements the well-known Flajolet-Martin (FM) sketch on a secret-sharing based multiparty computation (MPC) framework for solving the problem of private distributed cardinality estimation (PDCE), we observe that this MPC-FM protocol is not differentially private. In addition, the MPC-FM protocol is computationally expensive, which limits its applications to data holders with limited computation resources. To address the above issues, in this paper we propose a novel protocol DP-DICE, which is computationally efficient and differentially private for solving the problem of PDCE. Experimental results show that our DP-DICE achieves orders of magnitude speedup and reduces the estimation error by several times in comparison with state-of-the-arts under the same security requirements.

  匹配依据：MPC: multiparty computation, secret sharing

  </details>

- **A Lower Bound on the Share Size in Evolving Secret Sharing**
  2023-02-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/129)
  Noam Mazor

  <details><summary>摘要 / Abstract</summary>

  Secret sharing schemes allow sharing a secret between a set of parties in a way that ensures that only authorized subsets of the parties learn the secret. Evolving secret sharing schemes (Komargodski, Naor, and Yogev [TCC ’16]) allow achieving this end in a scenario where the parties arrive in an online fashion, and there is no a-priory bound on the number of parties. An important complexity measure of a secret sharing scheme is the share size, which is the maximum number of bits that a party may receive as a share. While there has been a significant progress in recent years, the best constructions for both secret sharing and evolving secret sharing schemes have a share size that is exponential in the number of parties. On the other hand, the best lower bound, by Csirmaz [Eurocrypt ’95], is sub-linear. In this work, we give a tight lower bound on the share size of evolving secret sharing schemes. Specifically, we show that the sub-linear lower bound of Csirmaz implies an exponential lower bound on evolving secret sharing.

  匹配依据：MPC: secret sharing

  </details>

- **SoK: Privacy-Enhancing Technologies in Finance**
  2023-02-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/122)
  Carsten Baum, James Hsin-yu Chiang, Bernardo David, Tore Kasper Frederiksen

  <details><summary>摘要 / Abstract</summary>

  Recent years have seen the emergence of practical advanced cryptographic tools that not only protect data privacy and authenticity, but also allow for jointly processing data from different institutions without sacrificing privacy. The ability to do so has enabled implementations a number of traditional and decentralized financial applications that would have required sacrificing privacy or trusting a third party. The main catalyst of this revolution was the advent of decentralized cryptocurrencies that use public ledgers to register financial transactions, which must be verifiable by any third party, while keeping sensitive data private. Zero Knowledge (ZK) proofs rose to prominence as a solution to this challenge, allowing for the owner of sensitive data (e.g. the identities of users involved in an operation) to convince a third party verifier that a certain operation has been correctly executed without revealing said data. It quickly became clear that performing arbitrary computation on private data from multiple sources by means of secure Multiparty Computation (MPC) and related techniques allows for more powerful financial applications, also in traditional finance. In this SoK, we categorize the main traditional and decentralized financial applications that can benefit from state-of-the-art Privacy-Enhancing Technologies (PETs) and identify design patterns commonly used when applying PETs in the context of these applications. In particular, we consider the following classes of applications: 1. Identity Management, KYC &amp; AML; and 2. Markets &amp; Settlement; 3. Legal; and 4. Digital Asset Custody. We examine how ZK proofs, MPC and related PETs have been used to tackle the main security challenges in each of these applications. Moreover, we provide an assessment of the technological readiness of each PET in the context of different financial applications according to the availability of: theoretical feasibility results, preliminary benchmarks (in scientific papers) or benchmarks achieving real-world performance (in commercially deployed solutions). Finally, we propose future applications of PETs as Fintech solutions to currently unsolved issues. While we systematize financial applications of PETs at large, we focus mainly on those applications that require privacy preserving computation on data from multiple parties.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Privacy Preserving Ultra-Short-term Wind Power Prediction Based on Secure Multi Party Computation**
  2023-01-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2301.13513)
  Hang Fan, Xiaoyu Fan, Tianyi Hao, Wei Wei, Kun Chen, Guosai Wang, Xiaofeng Jia, Yidong Li, Wei Xu

  <details><summary>摘要 / Abstract</summary>

  Mining the spatial and temporal correlation of wind farm output data is beneficial for enhancing the precision of ultra-short-term wind power prediction. However, if the wind farms are owned by separate entities, they may be reluctant to share their data directly due to privacy concerns as well as business management regulation policies. Although cryptographic approaches have been designed to protect privacy in the process of data sharing, it is still a challenging problem to encrypt the original data while extracting the nonlinear relationship among multiple wind farms in the machine learning process. This paper presents pwXGBoost, a technique based on the machine learning tree model and secure multi-party computation (SMPC) that can successfully extract complicated relationships while preserving data privacy. A maximum mean discrepancy (MMD) based scheme is proposed to effectively choose adjacent candidate wind farms to participate in the collaborative model training, therefore improving the accuracy and reducing the burden of data acquisition. The proposed method was evaluated on real world data collected from a cluster of wind farms in Inner Mongolia, China, demonstrating that it is capable of achieving considerable efficiency and performance improvements while preserving privacy

  匹配依据：MPC: secure multi party computation

  </details>

- **Meteor: Improved Secure 3-Party Neural Network Inference with Reducing Online Communication Costs**
  2023-01-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/100)
  Ye Dong, Xiaojun Chen, Weizhan Jing, Kaiyun Li, Weiping Wang

  <details><summary>摘要 / Abstract</summary>

  Secure neural network inference has been a promising solution to private Deep-Learning-as-a-Service, which enables the service provider and user to execute neural network inference without revealing their private inputs. However, the expensive overhead of current schemes is still an obstacle when applied in real applications. In this work, we present \textsc{Meteor}, an online communication-efficient and fast secure 3-party computation neural network inference system aginst semi-honest adversary in honest-majority. The main contributions of \textsc{Meteor} are two-fold: \romannumeral1) We propose a new and improved 3-party secret sharing scheme stemming from the \textit{linearity} of replicated secret sharing, and design efficient protocols for the basic cryptographic primitives, including linear operations, multiplication, most significant bit extraction, and multiplexer. \romannumeral2) Furthermore, we build efficient and secure blocks for the widely used neural network operators such as Matrix Multiplication, ReLU, and Maxpool, along with exploiting several specific optimizations for better efficiency. Our total communication with the setup phase is a little larger than SecureNN (PoPETs&#x27;19) and \textsc{Falcon} (PoPETs&#x27;21), two state-of-the-art solutions, but the gap is not significant when the online phase must be optimized as a priority. Using \textsc{Meteor}, we perform extensive evaluations on various neural networks. Compared to SecureNN and \textsc{Falcon}, we reduce the online communication costs by up to $25.6\times$ and $1.5\times$, and improve the running-time by at most $9.8\times$ (resp. $8.1\times$) and $1.5\times$ (resp. $2.1\times$) in LAN (resp. WAN) for the online inference.

  匹配依据：MPC: secret sharing, secure 3 party computation

  </details>

- **Scalable Multiparty Garbling**
  2023-01-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/099)
  Gabrielle Beck, Aarushi Goel, Aditya Hegde, Abhishek Jain, Zhengzhong Jin, Gabriel Kaptchuk

  <details><summary>摘要 / Abstract</summary>

  Multiparty garbling is the most popular approach for constant-round secure multiparty computation (MPC). Despite being the focus of significant research effort, instantiating prior approaches to multiparty garbling results in constant-round MPC that can not realistically accommodate large numbers of parties. In this work we present the first global-scale multiparty garbling protocol. The per-party communication complexity of our protocol decreases as the number of parties participating in the protocol increases --- for the first time matching the asymptotic communication complexity of non-constant round MPC protocols. Our protocol achieves malicious security in the honest-majority setting and relies on the hardness of the Learning Party with Noise assumption.

  匹配依据：MPC: garbling protocol, secure multiparty computation

  </details>

- **MPC With Delayed Parties Over Star-Like Networks**
  2023-01-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/096)
  Mariana Gama, Emad Heydari Beni, Emmanuela Orsini, Nigel P. Smart, Oliver Zajonc

  <details><summary>摘要 / Abstract</summary>

  While the efficiency of secure multi-party computation protocols has greatly increased in the last few years, these improvements and protocols are often based on rather unrealistic, idealised, assumptions about how technology is deployed in the real world. In this work we examine multi-party computation protocols in the presence of two major constraints present in deployed systems. Firstly, we consider the situation where the parties are connected not by direct point-to-point connections, but by a star-like topology with a few central post-office style relays. Secondly, we consider MPC protocols with a strong honest majority ($n \gg t/2$) in which we have stragglers (some parties are progressing slower than others). We model stragglers by allowing the adversary to delay messages to and from some parties for a given length of time. We first show that having only a single honest rely is enough to ensure consensus of the messages sent within a protocol; secondly, we show that special care must be taken to describe multiplication protocols in the case of relays and stragglers and that some well known protocols do not guarantee privacy and correctness in this setting; thirdly, we present an efficient honest-majority MPC protocol which can be run on top of the relays and which provides active-security with abort in the case of a strong honest majority, even when run with stragglers. We back up our protocol presentation with both experimental evaluations and simulations of the effect of the relays and delays on our protocol.

  匹配依据：MPC: multi party computation, secure multi party computation

  </details>

- **FssNN: Communication-Efficient Secure Neural Network Training via Function Secret Sharing**
  2023-01-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/073)
  Peng Yang, Zoe Lin Jiang, Shiqi Gao, Hongxiao Wang, Jun Zhou, Yangyiye Jin, Siu-Ming Yiu, Junbin Fang

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving neural network based on secure multi-party computation (MPC) enables multiple parties to jointly train neural network models without revealing sensitive data. In privacy-preserving neural network, the high communication costs of securely computing non-linear functions is the primary performance bottleneck. For commonly used non-linear functions, such as ReLU, existing work adopts an offline-online computation paradigm and utilizes distributed comparison function (DCF) to reduce communication costs. Specifically, these works prepare DCF keys in the offline phase and perform secure ReLU using these DCF keys in the online phase. However, the practicality of existing work is significantly limited due to the substantial size of DCF keys and the heavy reliance on a trusted third party in the offline phase. In this work, we introduce a communication-efficient secure two-party neural network framework called FssNN, which proposes a key-reduced DCF scheme without a trusted third party to enable practical secure training and inference. First, by analyzing the correlations between DCF keys to eliminate redundant parameters, we propose a key-reduced DCF scheme with a compact additive construction, which decreases the size of DCF keys by about $17.9\%$ and the offline communication costs by approximately $28.0\%$. Secondly, by leveraging an MPC-friendly pseudorandom number generator, we propose a secure two-party distributed key generation protocol for our key-reduced DCF, thereby eliminating the reliance on the trusted third party. Finally, we utilize the key-reduced DCF and additive secret sharing to compute non-linear and linear functions, respectively, and design secure computation protocols with constant online communication rounds for neural network operators, reducing the online communication costs by $28.9\% \sim 43.4\%$. We provide formal security proofs and evaluate the performance of FssNN on various models and datasets. Experimental results show that compared to the state-of-the-art framework AriaNN, our framework reduces the total communication costs of secure training and inference by approximately $25.4\%$ and $26.4\%$ respectively.

  匹配依据：MPC: secret sharing, secure computation, secure multi party computation

  </details>

- **Robust, Secure and Private Cache-aided Scalar Linear Function Retrieval from Distributed System with Blind and Adversarial Servers**
  2023-01-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2301.08711)
  Qifa Yan, Xiaohu Tang, Zhengchun Zhou

  <details><summary>摘要 / Abstract</summary>

  In this work, a distributed server system composed of multiple servers that holds some coded files and multiple users that are interested in retrieving the linear functions of the files is investigated, where the servers are robust, blind and adversarial in the sense that any $J$ servers can together recover all files, while any $I$ colluding servers cannot obtain any information about the files, and at most $A$ servers maliciously provides erroneous information. In addition, the file library must be secure from a wiretapper who obtains all the signals, and the demands of any subset of users must kept private from the other users and servers, even if they collude. A coding scheme is proposed by incorporating the ideas of Shamir&#x27;s secret sharing and key superposition into the framework of Placement Delivery Array (PDA), originally proposed to characterize the single-server coded caching system without any security or privacy constraints. It is shown that PDAs associated to Maddah-Ali and Niesen&#x27;s coded caching scheme results in an achievable memory-storage-communication region, such that the storage size and communication load were optimal to within a multiplicative gap, except for the small memory regime when the number of files was smaller than the number of users.

  匹配依据：MPC: secret sharing

  </details>

- **Silph: A Framework for Scalable and Accurate Generation of Hybrid MPC Protocols**
  2023-01-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/060)
  Edward Chen, Jinhao Zhu, Alex Ozdemir, Riad S. Wahby, Fraser Brown, Wenting Zheng

  <details><summary>摘要 / Abstract</summary>

  Many applications in finance and healthcare need access to data from multiple organizations. While these organizations can benefit from computing on their joint datasets, they often cannot share data with each other due to regulatory constraints and business competition. One way mutually distrusting parties can collaborate without sharing their data in the clear is to use secure multiparty computation (MPC). However, MPC’s performance presents a serious obstacle for adoption as it is difficult for users who lack expertise in advanced cryptography to optimize. In this paper, we present Silph, a framework that can automatically compile a program written in a high-level language to an optimized, hybrid MPC protocol that mixes multiple MPC primitives securely and efficiently. Compared to prior works, our compilation speed is improved by up to 30000×. On various database analytics and machine learning workloads, the MPC protocols generated by Silph match or outperform prior work by up to 3.6×.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Private Federated Submodel Learning via Private Set Union**
  2023-01-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2301.07686)
  Zhusheng Wang, Sennur Ulukus

  <details><summary>摘要 / Abstract</summary>

  We consider the federated submodel learning (FSL) problem and propose an approach where clients are able to update the central model information theoretically privately. Our approach is based on private set union (PSU), which is further based on multi-message symmetric private information retrieval (MM-SPIR). The server has two non-colluding databases which keep the model in a replicated manner. With our scheme, the server does not get to learn anything further than the subset of submodels updated by the clients: the server does not get to know which client updated which submodel(s), or anything about the local client data. In comparison to the state-of-the-art private FSL schemes of Jia-Jafar and Vithana-Ulukus, our scheme does not require noisy storage of the model at the databases; and in comparison to the secure aggregation scheme of Zhao-Sun, our scheme does not require pre-distribution of client-side common randomness, instead, our scheme creates the required client-side common randomness via random SPIR and one-time pads. The protocol starts with a common randomness generation (CRG) phase where the two databases establish common randomness at the client-side using RSPIR and one-time pads (this phase is called FSL-CRG). Next, the clients utilize the established client-side common randomness to have the server determine privately the union of indices of submodels to be updated collectively by the clients (this phase is called FSL-PSU). Then, the two databases broadcast the current versions of the submodels in the set union to clients. The clients update the submodels based on their local training data. Finally, the clients use a variation of FSL-PSU to write the updates back to the databases privately (this phase is called FSL-write). Our proposed private FSL scheme is robust against client drop-outs, client late-arrivals, and database drop-outs.

  匹配依据：MPC: private set union

  </details>

- **Putting the Online Phase on a Diet: Covert Security from Short MACs**
  2023-01-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/052)
  Sebastian Faust, Carmit Hazay, David Kretzler, Benjamin Schlosser

  <details><summary>摘要 / Abstract</summary>

  An important research direction in secure multi-party computation (MPC) is to improve the efficiency of the protocol. One idea that has recently received attention is to consider a slightly weaker security model than full malicious security -- the so-called setting of $\textit{covert security}$. In covert security, the adversary may cheat but only is detected with certain probability. Several works in covert security consider the offline/online approach, where during a costly offline phase correlated randomness is computed, which is consumed in a fast online phase. State-of-the-art protocols focus on improving the efficiency by using a covert offline phase, but ignore the online phase. In particular, the online phase is usually assumed to guarantee security against malicious adversaries. In this work, we take a fresh look at the offline/online paradigm in the covert security setting. Our main insight is that by weakening the security of the online phase from malicious to covert, we can gain significant efficiency improvements during the offline phase. Concretely, we demonstrate our technique by applying it to the online phase of the well-known TinyOT protocol (Nielsen et al., CRYPTO &#x27;12). The main observation is that by reducing the MAC length in the online phase of TinyOT to $t$ bits, we can guarantee covert security with a detection probability of $1- \frac{1}{2^t}$. Since the computation carried out by the offline phase depends on the MAC length, shorter MACs result in a more efficient offline phase and thus speed up the overall computation. Our evaluation shows that our approach reduces the communication complexity of the offline protocol by at least 35% for a detection rate up to $\frac{7}{8}$. In addition, we present a new generic composition result for analyzing the security of online/offline protocols in terms of concrete security.

  匹配依据：MPC: secure multi party computation

  </details>

- **Order-Preserving Database Encryption with Secret Sharing**
  2023-01-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2301.04370)
  Dongfang Zhao

  <details><summary>摘要 / Abstract</summary>

  The order-preserving encryption (OPE) problem was initially formulated by the database community in 2004 soon after the paradigm database-as-a-service (DaaS) was coined in 2002. Over the past two decades, OPE has drawn tremendous research interest from communities of databases, cryptography, and security; we have witnessed significant advances in OPE schemes both theoretically and systematically. All existing OPE schemes assume that the outsourced database is modeled as a single semi-honest adversary who should learn nothing more than the order information of plaintext messages up to a negligible probability. This paper addresses the OPE problem from a new perspective: instead of modeling the outsourced database as a single semi-honest adversary, we assume the outsourced database \textit{service} compromises a cluster of non-colluding servers, which is a practical assumption as all major cloud vendors support multiple database instances deployed to exclusive sub-networks or even to distinct data centers. This assumption allows us to design a new stateless OPE protocol, namely order-preserving database encryption with secret sharing (ODES), by employing secret-sharing schemes among those presumably non-colluding servers. We will demonstrate that ODES guarantees the latest security level, namely IND-FAOCPA, and outperforms the state-of-the-art scheme by orders of magnitude.

  匹配依据：MPC: secret sharing

  </details>

- **Earn While You Reveal: Private Set Intersection that Rewards Participants**
  2023-01-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2301.03889) · [IACR ePrint](https://eprint.iacr.org/2023/030)
  Aydin Abadi

  <details><summary>摘要 / Abstract</summary>

  In Private Set Intersection protocols (PSIs), a non-empty result always reveals something about the private input sets of the parties. Moreover, in various variants of PSI, not all parties necessarily receive or are interested in the result. Nevertheless, to date, the literature has assumed that those parties who do not receive or are not interested in the result still contribute their private input sets to the PSI for free, although doing so would cost them their privacy. In this work, for the first time, we propose a multi-party PSI, called &quot;Anesidora&quot;, that rewards parties who contribute their private input sets to the protocol. Anesidora is efficient; it mainly relies on symmetric key primitives and its computation and communication complexities are linear with the number of parties and set cardinality. It remains secure even if the majority of parties are corrupted by active colluding adversaries.

  匹配依据：MPC: private set intersection

  </details>

- **Information-Theoretic Distributed Point Functions**
  2023-01-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/028)
  Elette Boyle, Niv Gilboa, Yuval Ishai, Victor I. Kolobov

  <details><summary>摘要 / Abstract</summary>

  A distributed point function (DPF) (Gilboa-Ishai, Eurocrypt 2014) is a cryptographic primitive that enables compressed additive secret-sharing of a secret weight-1 vector across two or more servers. DPFs support a wide range of cryptographic applications, including efficient private information retrieval, secure aggregation, and more. Up to now, the study of DPFs was restricted to the computational security setting, relying on one-way functions. This assumption is necessary in the case of a dishonest majority. We present the first statistically private 3-server DPF for domain size $N$ with subpolynomial key size $N^{o(1)}$. We also present a similar perfectly private 4-server DPF. Our constructions offer benefits over their computationally secure counterparts, beyond the superior security guarantee, including better computational complexity and better protocols for distributed key generation, all while having comparable communication complexity for moderate-sized parameters.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Distributed Energy Resource Control with Decentralized Cloud Computing**
  2023-01-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2301.02198)
  Xiang Huo, Mingxi Liu

  <details><summary>摘要 / Abstract</summary>

  The rapidly growing penetration of renewable energy resources brings unprecedented challenges to power distribution networks - management of a large population of grid-tied controllable devices encounters control scalability crises and potential end-user privacy breaches. Despite the importance, research on privacy preservation of distributed energy resource (DER) control in a fully scalable manner is lacked. To fill the gap, this paper designs a novel decentralized privacy-preserving DER control framework that 1) achieves control scalability over DER population and heterogeneity; 2) eliminates peer-to-peer communications and secures the privacy of all participating DERs against various types of adversaries; and 3) enjoys higher computation efficiency and accuracy compared to state-of-the-art privacy-preserving methods. A strongly coupled optimization problem is formulated to control the power consumption and output of DERs, including solar photovoltaics and energy storage systems, then solved using the projected gradient method. Cloud computing and secret sharing are seamlessly integrated into the proposed decentralized computing to achieve privacy preservation. Simulation results prove the capabilities of the proposed approach in DER control applications.

  匹配依据：MPC: secret sharing

  </details>

- **Delegated Private Matching for Compute**
  2023-01-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/012)
  Dimitris Mouris, Daniel Masny, Ni Trieu, Shubho Sengupta, Prasad Buddhavarapu, Benjamin Case

  <details><summary>摘要 / Abstract</summary>

  Private matching for compute (PMC) establishes a match between two datasets owned by mutually distrusted parties ($C$ and $P$) and allows the parties to input more data for the matched records for arbitrary downstream secure computation without rerunning the private matching component. The state-of-the-art PMC protocols only support two parties and assume that both parties can participate in computationally intensive secure computation. We observe that such operational overhead limits the adoption of these protocols to solely powerful entities as small data owners or devices with minimal computing power will not be able to participate. We introduce two protocols to delegate PMC from party $P$ to untrusted cloud servers, called delegates, allowing multiple smaller $P$ parties to provide inputs containing identifiers and associated values. Our Delegated Private Matching for Compute protocols, called DPMC and D$_s$PMC, establish a join between the datasets of party $C$ and multiple delegators $P$ based on multiple identifiers and compute secret shares of associated values for the identifiers that the parties have in common. We introduce a rerandomizable encrypted oblivious pseudorandom function (OPRF) primitive, called EO, which allows two parties to encrypt, mask, and shuffle their data. Note that EO may be of independent interest. Our D$_s$PMC protocol limits the leakages of DPMC by combining our EO scheme and secure three-party shuffling. Finally, our implementation demonstrates the efficiency of our constructions by outperforming related works by approximately $10\times$ for the total protocol execution and by at least $20\times$ for the computation on the delegators.

  匹配依据：MPC: secure computation

  </details>

- **Time is money, friend! Timing Side-channel Attack against Garbled Circuit Constructions**
  2023-01-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/001)
  Mohammad Hashemi, Domenic Forte, Fatemeh Ganji

  <details><summary>摘要 / Abstract</summary>

  With the advent of secure function evaluation (SFE), distrustful parties can jointly compute on their private inputs without disclosing anything besides the results. Yao’s garbled circuit protocol has become an integral part of secure computation thanks to considerable efforts made to make it feasible, practical, and more efficient. These efforts have resulted in multiple optimizations on this primitive to enhance its performance by orders of magnitude over the last years. The advancement in protocols has also led to the development of general-purpose compilers and tools made available to academia and industry. For decades, the security of protocols offered in those tools has been assured with regard to sound proofs and the promise that during the computation, no information on parties’ input would be leaking. In a parallel effort, however, side-channel analysis (SCA) has gained momentum in connection with the real-world implementation of cryptographic primitives. Timing side-channel attacks have proven themselves effective in retrieving secrets from implementations, even through remote access to them. Nevertheless, the vulnerability of garbled circuit frameworks to timing attacks has, surprisingly, never been discussed in the literature. This paper introduces Goblin, the first timing attack against commonly employed garbled circuit frameworks. Goblin is a machine learning-assisted, non-profiling, single-trace timing SCA, which successfully recovers the garbler’s input during the computation under different scenarios, including various GC frameworks, benchmark functions, and the number of garbler’s input bits. Furthermore, we discuss Gob- lin’s success factors and countermeasures against that. In doing so, Goblin hopefully paves the way for further research in this matter.

  匹配依据：MPC: garbled circuit, secure computation, secure function evaluation

  </details>
