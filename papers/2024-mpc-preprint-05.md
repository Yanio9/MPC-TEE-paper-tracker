# 2024 · MPC · 仅预印本来源 · 第 5/5 页

[总目录](../PAPERS.md) · [上一页](2024-mpc-preprint-04.md)

- **Generative AI-enabled Blockchain Networks: Fundamentals, Applications, and Case Study**
  2024-01-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.15625)
  Cong T. Nguyen, Yinqiu Liu, Hongyang Du, Dinh Thai Hoang, Dusit Niyato, Diep N. Nguyen, Shiwen Mao

  <details><summary>摘要 / Abstract</summary>

  Generative Artificial Intelligence (GAI) has recently emerged as a promising solution to address critical challenges of blockchain technology, including scalability, security, privacy, and interoperability. In this paper, we first introduce GAI techniques, outline their applications, and discuss existing solutions for integrating GAI into blockchains. Then, we discuss emerging solutions that demonstrate the effectiveness of GAI in addressing various challenges of blockchain, such as detecting unknown blockchain attacks and smart contract vulnerabilities, designing key secret sharing schemes, and enhancing privacy. Moreover, we present a case study to demonstrate that GAI, specifically the generative diffusion model, can be employed to optimize blockchain network performance metrics. Experimental results clearly show that, compared to a baseline traditional AI approach, the proposed generative diffusion model approach can converge faster, achieve higher rewards, and significantly improve the throughput and latency of the blockchain network. Additionally, we highlight future research directions for GAI in blockchain applications, including personalized GAI-enabled blockchains, GAI-blockchain synergy, and privacy and security considerations within blockchain ecosystems.

  匹配依据：MPC: secret sharing

  </details>

- **R3PO: Reach-Restricted Reactive Program Obfuscation and its Application to MA-ABE**
  2024-01-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/119)
  Kaartik Bhushan, Sai Lakshmi Bhavana Obbattu, Manoj Prabhakaran, Rajeev Raghunath

  <details><summary>摘要 / Abstract</summary>

  In recent breakthrough results, novel use of garbled circuits yielded constructions for several primitives like Identity-Based Encryption (IBE) and 2-round secure multi-party computation, based on standard assumptions in public-key cryptography. While the techniques in these different results have many common elements, these works did not offer a modular abstraction that could be used across them. Our main contribution is to introduce a novel notion of obfuscation, called Reach-Restricted Reactive Program Obfuscation (R3PO) that captures the essence of these constructions, and exposes additional capabilities. We provide a powerful composition theorem whose proof fully encapsulates the use of garbled circuits in these works. As an illustration of the potential of R3PO, and as an important contribution of independent interest, we present a variant of Multi-Authority Attribute-Based Encryption (MA-ABE) that can be based on (single-authority) CP-ABE in a blackbox manner, using only standard cryptographic assumptions (e.g., DDH). This is in stark contrast to the existing constructions for MA-ABE, which rely on the random oracle model and/or support only limited policy classes.

  匹配依据：MPC: garbled circuits, secure multi party computation

  </details>

- **Demonstration of monogamy laws for Gaussian steering in optomechanics**
  2024-01-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.15521)
  J El Qars, M Daoud, R Ahl Laamara, N Habiballah

  <details><summary>摘要 / Abstract</summary>

  Secrecy and security are crucial in communication. So, quantum secret sharing protocol has recently been proposed to distribute a secret message to a set of parties, where the decoding procedure is forbidden individually, and a cooperative operation is needed. For this, quantum steering as an intriguing kind of nonlocality, is proven to be a useful resource for efficient implementations of the QSS protocol. Here, we study the distribution of Gaussian steering over an asymmetric three-mode optomechanical state. We show that a single-mode cannot be jointly steered by the two others, and further verify the monogamy inequalities of Gaussian steering. The state at hand displays genuine tripartite steering. Also, we observe one-way steering in the configuration (1vs1) mode as well as (1vs2) mode, hence, we reveal that the asymmetry introduced into the state we consider, is a necessary condition but not sufficient for reaching one way steering. As well, we detect one-way steering between two modes never directly interact. Strikingly, our model exhibits an extreme level of steering, where two single-mode cannot steer individually the third mode, while, they can collectively, which is decisive for practical execution of the QSS protocol.

  匹配依据：MPC: secret sharing

  </details>

- **Sliding Secure Symmetric Multilevel Diversity Coding**
  2024-01-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.14723)
  Tao Guo, Laigang Guo, Yinfei Xu, Congduan Li, Shi Jin, Raymond Yeung

  <details><summary>摘要 / Abstract</summary>

  Symmetric multilevel diversity coding (SMDC) is a source coding problem where the independent sources are ordered according to their importance. It was shown that separately encoding independent sources (referred to as ``\textit{superposition coding}&quot;) is optimal. In this paper, we consider an $(L,s)$ \textit{sliding secure} SMDC problem with security priority, where each source $X_α~(s\leq α\leq L)$ is kept perfectly secure if no more than $α-s$ encoders are accessible. The reconstruction requirements of the $L$ sources are the same as classical SMDC. A special case of an $(L,s)$ sliding secure SMDC problem that the first $s-1$ sources are constants is called the $(L,s)$ \textit{multilevel secret sharing} problem. For $s=1$, the two problems coincide, and we show that superposition coding is optimal. The rate regions for the $(3,2)$ problems are characterized. It is shown that superposition coding is suboptimal for both problems. The main idea that joint encoding can reduce coding rates is that we can use the previous source $X_{α-1}$ as the secret key of $X_α$. Based on this idea, we propose a coding scheme that achieves the minimum sum rate of the general $(L,s)$ multilevel secret sharing problem. Moreover, superposition coding of the $s$ sets of sources $X_1$, $X_2$, $\cdots$, $X_{s-1}$, $(X_s, X_{s+1}, \cdots, X_L)$ achieves the minimum sum rate of the general sliding secure SMDC problem.

  匹配依据：MPC: secret sharing

  </details>

- **An Improved Lower Bound on Oblivious Transfer Capacity via Interactive Erasure Emulation**
  2024-01-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.14965)
  So Suda, Shun Watanabe, Haruya Yamaguchi

  <details><summary>摘要 / Abstract</summary>

  We revisit the oblivious transfer (OT) capacities of noisy channels against the passive adversary, which have been identified only for a limited class of channels. In the literature, the general construction of oblivious transfer has been known only for generalized erasure channels (GECs); for other channels, we first convert a given channel to a GEC via alphabet extension and erasure emulation, and then apply the general construction for GEC. In this paper, we derive an improved lower bound on the OT capacity of the binary symmetric channel (BSC) and binary symmetric erasure channel (BSEC) by proposing a new protocol; by using interactive communication between the sender and the receiver, our protocol emulates erasure events recursively in multiple rounds. We also discuss a potential necessity of multiple rounds interactive communication to attain the OT capacity.

  匹配依据：MPC: oblivious transfer

  </details>

- **Privacy-Preserving Face Recognition in Hybrid Frequency-Color Domain**
  2024-01-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.13386)
  Dong Han, Yong Li, Joachim Denzler

  <details><summary>摘要 / Abstract</summary>

  Face recognition technology has been deployed in various real-life applications. The most sophisticated deep learning-based face recognition systems rely on training millions of face images through complex deep neural networks to achieve high accuracy. It is quite common for clients to upload face images to the service provider in order to access the model inference. However, the face image is a type of sensitive biometric attribute tied to the identity information of each user. Directly exposing the raw face image to the service provider poses a threat to the user&#x27;s privacy. Current privacy-preserving approaches to face recognition focus on either concealing visual information on model input or protecting model output face embedding. The noticeable drop in recognition accuracy is a pitfall for most methods. This paper proposes a hybrid frequency-color fusion approach to reduce the input dimensionality of face recognition in the frequency domain. Moreover, sparse color information is also introduced to alleviate significant accuracy degradation after adding differential privacy noise. Besides, an identity-specific embedding mapping scheme is applied to protect original face embedding by enlarging the distance among identities. Lastly, secure multiparty computation is implemented for safely computing the embedding distance during model inference. The proposed method performs well on multiple widely used verification datasets. Moreover, it has around 2.6% to 4.2% higher accuracy than the state-of-the-art in the 1:N verification scenario.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Quaternary codes and their binary images**
  2024-01-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.12486)
  Yansheng Wu, Chao Li, Lin Zhang, Fu Xiao

  <details><summary>摘要 / Abstract</summary>

  Recently, simplicial complexes are used in constructions of several infinite families of minimal and optimal linear codes by Hyun {\em et al.} Building upon their research, in this paper more linear codes over the ring $\mathbb{Z}_4$ are constructed by simplicial complexes. Specifically, the Lee weight distributions of the resulting quaternary codes are determined and two infinite families of four-Lee-weight quaternary codes are obtained. Compared to the databases of $\mathbb Z_4$ codes by Aydin {\em et al.}, at least nine new quaternary codes are found. Thanks to the special structure of the defining sets, we have the ability to determine whether the Gray images of certain obtained quaternary codes are linear or not. This allows us to obtain two infinite families of binary nonlinear codes and one infinite family of binary minimal linear codes. Furthermore, utilizing these minimal binary codes, some secret sharing schemes as a byproduct also are established.

  匹配依据：MPC: secret sharing

  </details>

- **Multi-Party Private Set Intersection: A Circuit-Based Protocol with Jaccard Similarity for Secure and Efficient Anomaly Detection in Network Traffic**
  2024-01-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.12542)
  Jiuheng Su, Zhili Chen, Xiaomin Yang

  <details><summary>摘要 / Abstract</summary>

  We present a new circuit-based protocol for multi-party private set intersection (PSI) that allows m parties to compute the intersection of their datasets without revealing any additional information about the items outside the intersection. Building upon the two-party Sort-Compare-Shuffle (SCS) protocol, we seamlessly extend it to a multi-party setting. Demonstrating its practicality through implementation, our protocol exhibits acceptable performance. Specifically, with 7 parties, each possessing a set size of 2^{12}, our protocol completes in just 19 seconds. Moreover, circuit-based protocols like ours have an advantage over using custom protocols to perform more complex computation. We substantiate this advantage by incorporating a module for calculating the Jaccard similarity metric of the private sets which can be used in the application domain of network traffic analysis for anomaly detection. This extension showcases the versatility of our protocol beyond set intersection computations, demonstrating its efficacy in preserving privacy while efficiently identifying abnormal patterns in network flow.

  匹配依据：MPC: private set intersection

  </details>

- **Laconic Branching Programs from the Diffie-Hellman Assumption**
  2024-01-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/102)
  Sanjam Garg, Mohammad Hajiabadi, Peihan Miao, Alice Murphy

  <details><summary>摘要 / Abstract</summary>

  Laconic cryptography enables secure two-party computation (2PC) on unbalanced inputs with asymptotically-optimal communication in just two rounds of communication. In particular, the receiver (who sends the first-round message) holds a long input and the sender (who sends the second-round message) holds a short input, and the size of their communication to securely compute a function on their joint inputs only grows with the size of the sender&#x27;s input and is independent of the receiver&#x27;s input size. The work on laconic oblivious transfer (OT) [Cho et al. CRYPTO 2017] and laconic private set intersection (PSI) [Alamati et al. TCC 2021] shows how to achieve secure laconic computation for OT and PSI from the Diffie-Hellman assumption. In this work, we push the limits further and achieve laconic branching programs from the Diffie-Hellman assumption. In particular, the receiver holds a large branching program $P$ and the sender holds a short input $x$. We present a two-round 2PC protocol that allows the receiver to learn $x$ iff $P(x) =1$, and nothing else. The communication only grows with the size of $x$ and the depth of $P$, and does not further depend on the size of $P$.

  匹配依据：MPC: oblivious transfer, private set intersection, secure two party computation

  </details>

- **AnonPSI: An Anonymity Assessment Framework for PSI**
  2024-01-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2311.18118) · [IACR ePrint](https://eprint.iacr.org/2024/104)
  Bo Jiang, Jian Du, Qiang Yan

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection (PSI) is a widely used protocol that enables two parties to securely compute a function over the intersected part of their shared datasets and has been a significant research focus over the years. However, recent studies have highlighted its vulnerability to Set Membership Inference Attacks (SMIA), where an adversary might deduce an individual&#x27;s membership by invoking multiple PSI protocols. This presents a considerable risk, even in the most stringent versions of PSI, which only return the cardinality of the intersection. This paper explores the evaluation of anonymity within the PSI context. Initially, we highlight the reasons why existing works fall short in measuring privacy leakage, and subsequently propose two attack strategies that address these deficiencies. Furthermore, we provide theoretical guarantees on the performance of our proposed methods. In addition to these, we illustrate how the integration of auxiliary information, such as the sum of payloads associated with members of the intersection (PSI-SUM), can enhance attack efficiency. We conducted a comprehensive performance evaluation of various attack strategies proposed utilizing two real datasets. Our findings indicate that the methods we propose markedly enhance attack efficiency when contrasted with previous research endeavors. The effective attacking implies that depending solely on existing PSI protocols may not provide an adequate level of privacy assurance. It is recommended to combine privacy-enhancing technologies synergistically to enhance privacy protection even further.

  匹配依据：MPC: private set intersection

  </details>

- **Unconditional Security using (Random) Anonymous Bulletin Board**
  2024-01-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/101)
  Albert Yu, Hai H. Nguyen, Aniket Kate, Hemanta K. Maji

  <details><summary>摘要 / Abstract</summary>

  In a seminal work, Ishai et al. (FOCS–2006) studied the viability of designing unconditionally secure protocols for key agreement and secure multi-party computation (MPC) using an anonymous bulletin board (ABB) as a building block. While their results establish the feasibility of key agreement and honest-majority MPC in the ABB model, the optimality of protocols with respect to their round and communication complexity is not studied. This paper enriches this study of unconditional security in the ABB model in multiple ways. - We present a key agreement protocol with a novel combinatorial insight to offer a 200% throughput over the (FOCS–2006) study; i.e., using the same number of messages, we can (almost) double the bit-length of the agreed key. We also prove the near optimality of our approach. - We offer unconditionally secure protocols for the (random) string oblivious transfer functionalities. We present a $1$-round chosen message random string oblivious transfer and show how to extend it to a non-interactive (random) string oblivious transfer protocol and a $2$-round chosen message string oblivious transfer. - We prove a $1$-round lower bound for BEC under certain conditions. Central to our technical contributions is the abstraction of a distributional variant of the random ABB functionality. Investigating the concrete efficiency of founding MPC from this primitive leads to fascinating new mathematical challenges in well-established MPC models, which will be of broader interest to the community.

  匹配依据：MPC: oblivious transfer, secure multi party computation

  </details>

- **Call Me By My Name: Simple, Practical Private Information Retrieval for Keyword Queries**
  2024-01-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/092)
  Sofía Celi, Alex Davidson

  <details><summary>摘要 / Abstract</summary>

  We introduce $\mathsf{ChalametPIR}$: a single-server Private Information Retrieval (PIR) scheme supporting fast, low-bandwidth \emph{keyword} queries, with a conceptually very simple design. In particular, we develop a generic framework for converting PIR schemes for index queries over flat arrays (based on Learning With Errors) into keyword PIR. This involves representing a key-value map using any probabilistic filter that permits reconstruction of elements from inclusion queries (e.g. Cuckoo filters). In particular, we make use of recently developed \emph{Binary Fuse filters} to construct $\mathsf{ChalametPIR}$, with minimal efficiency blow-up compared with state-of-the-art index-based schemes (all costs bounded by a factor of $\leq 1.08$). Furthermore, we show that $\mathsf{ChalametPIR}$ achieves runtimes and financial costs that are factors of between $6\times$-$11\times$ and $3.75\times$-$11.4\times$ more efficient, respectively, than state-of-the-art keyword PIR approaches, for varying database configurations. Bandwidth costs are reduced or remain competitive, depending on the configuration. Finally, we believe that our application of Binary Fuse filters can have independent value towards developing efficient variants of related cryptographic primitives (e.g. private set intersection), that already benefit from using less efficient filter constructions.

  匹配依据：MPC: private set intersection

  </details>

- **Enabling PERK and other MPC-in-the-Head Signatures on Resource-Constrained Devices**
  2024-01-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/088)
  Slim Bettaieb, Loïc Bidoux, Alessandro Budroni, Marco Palumbi, Lucas Pandolfo Perin

  <details><summary>摘要 / Abstract</summary>

  One category of the digital signatures submitted to the NIST Post-Quantum Cryptography Standardization Process for Additional Digital Signature Schemes comprises proposals constructed leveraging the MPC-in-the-Head (MPCitH) paradigm. Typically, this framework is characterized by the computation and storage in sequence of large data structures both in signing and verification algorithms, resulting in heavy memory consumption. While some research on the efficiency of these schemes on high-performance machines has been done, studying their performance and optimization on resource-constrained ones still needs to be explored. In this work, we aim to address this gap by (1) introducing a general method to reduce the memory footprint of MPCitH schemes and analyzing its application to several MPCitH proposed schemes in the NIST Standardization Process. Additionally, (2) we conduct a detailed examination of potential memory optimizations in PERK, resulting in a streamlined version of the signing and verification algorithms with a reduced memory footprint ranging from 22 to 85 KB, down from the original 0.3 to 6 MB. Finally, (3) we introduce the first implementation of PERK tailored for Arm Cortex M4 alongside extensive experiments and comparisons against reference implementations.

  匹配依据：MPC: mpc (context)

  </details>

- **PRIDA: PRIvacy-preserving Data Aggregation with multiple data customers**
  2024-01-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/074)
  Beyza Bozdemir, Betül Aşkın Özdemir, Melek Önen

  <details><summary>摘要 / Abstract</summary>

  We propose a solution for user privacy-oriented privacy-preserving data aggregation with multiple data customers. Most existing state-of-the-art approaches present too much importance on performance efficiency and seem to ignore privacy properties except for input privacy. Most solutions for data aggregation do not generally discuss the users’ birthright, namely their privacy for their own data control and anonymity when they search for something on the browser or volunteer to participate in a survey. Still, they are ambitious to secure data customers’ rights (which should come later). They focus on resulting in an efficiency-oriented data aggregation enabling input privacy only. We aim to give importance to user privacy, and we have designed a solution for data aggregation in which we keep efficiency in balance. We show that PRIDA provides a good level of computational and communication complexities and is even better in timing evaluation than existing studies published recently (i.e., Bonawitz et al. (CCS’17), Corrigan-Gibbs et al. (NSDI’17), Bell et al. (CCS’20), Addanki et al. (SCN’22)). We employ threshold homomorphic encryption and secure two-party computation to ensure privacy properties. We balance the trade-off between a proper design for users and the desired privacy and efficiency.

  匹配依据：MPC: secure two party computation

  </details>

- **SDitH in Hardware**
  2024-01-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/069)
  Sanjay Deshpande, James Howe, Jakub Szefer, Dongze Yue

  <details><summary>摘要 / Abstract</summary>

  This work presents the first hardware realisation of the Syndrome-Decoding-in-the-Head (SDitH) signature scheme, which is a candidate in the NIST PQC process for standardising post-quantum secure digital signature schemes. SDitH&#x27;s hardness is based on conservative code-based assumptions, and it uses the Multi-Party-Computation-in-the-Head (MPCitH) construction. This is the first hardware design of a code-based signature scheme based on traditional decoding problems and only the second for MPCitH constructions, after Picnic. This work presents optimised designs to achieve the best area efficiency, which we evaluate using the Time-Area Product (TAP) metric. This work also proposes a novel hardware architecture by dividing the signature generation algorithm into two phases, namely offline and online phases for optimising the overall clock cycle count. The hardware designs for key generation, signature generation, and signature verification are parameterised for all SDitH parameters, including the NIST security levels, both syndrome decoding base fields (GF256 and GF251), and thus conforms to the SDitH specifications. The hardware design further supports secret share splitting, and the hypercube optimisation which can be applied in this and multiple other NIST PQC candidates. The results of this work result in a hardware design with a drastic reducing in clock cycles compared to the optimised AVX2 software implementation, in the range of 2-4x for most operations. Our key generation outperforms software drastically, giving a 11-17x reduction in runtime, despite the significantly faster clock speed. On Artix 7 FPGAs we can perform key generation in 55.1 Kcycles, signature generation in 6.7 Mcycles, and signature verification in 8.6 Mcycles for NIST L1 parameters, which increase for GF251, and for L3 and L5 parameters.

  匹配依据：MPC: multi party computation

  </details>

- **Privacy-preserving Anti-Money Laundering using Secure Multi-Party Computation**
  2024-01-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/065)
  Marie Beth van Egmond, Vincent Dunning, Stefan van den Berg, Thomas Rooijakkers, Alex Sangers, Ton Poppe, Jan Veldsink

  <details><summary>摘要 / Abstract</summary>

  Money laundering is a serious financial crime where criminals aim to conceal the illegal source of their money via a series of transactions. Although banks have an obligation to monitor transactions, it is difficult to track these illicit money flows since they typically span over multiple banks, which cannot share this information due to privacy concerns. We present secure risk propagation, a novel efficient algorithm for money laundering detection across banks without violating privacy concerns. In this algorithm, each account is assigned a risk score, which is then propagated through the transaction network. In this article we present two results. Firstly, using data from a large Dutch bank, we show that it is possible to detect unusual activity using this model, with cash ratio as the risk score. With a recall of 20%, the precision improves from 15% to 40% by propagating the risk scores, reducing the number of false positives significantly. Secondly, we present a privacy-preserving solution for securely performing risk propagation over a joint, inter-bank transaction network. To achieve this, we use Secure Multi-Party Computation (MPC) techniques, which are particularly well-suited for the risk propagation algorithm due to its structural simplicity. We also show that the running time of this secure variant scales linearly in the amount of accounts and transactions. For 200, 000 transactions, two iterations of the secure algorithm between three virtual parties, run within three hours on a consumer-grade server.

  匹配依据：MPC: secure multi party computation

  </details>

- **Constrained Pseudorandom Functions for Inner-Product Predicates from Weaker Assumptions**
  2024-01-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/058)
  Sacha Servan-Schreiber

  <details><summary>摘要 / Abstract</summary>

  In this paper, we provide a novel framework for constructing constrained pseudorandom functions (CPRFs) with inner-product constraint predicates, using ideas from subtractive secret sharing and related-key-attack security. Our framework can be instantiated using a random oracle or any suitable related-key-attack (RKA) secure pseudorandom function. This results in three new CPRF constructions: 1. an adaptively-secure construction in the random oracle model; 2. a selectively-secure construction under the DDH assumption; and 3. a selectively-secure construction with a polynomial domain under the assumption that one-way functions exist. All three instantiations are constraint-hiding and support inner-product predicates, leading to the first constructions of such expressive CPRFs under each corresponding assumption. Moreover, while the OWF-based construction is primarily of theoretical interest, the random oracle and DDH-based constructions are concretely efficient, which we show via an implementation.

  匹配依据：MPC: secret sharing

  </details>

- **Do You Need a Zero Knowledge Proof?**
  2024-01-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/050)
  Jens Ernstberger, Stefanos Chaliasos, Liyi Zhou, Philipp Jovanovic, Arthur Gervais

  <details><summary>摘要 / Abstract</summary>

  Zero-Knowledge Proofs (ZKPs), a cryptographic tool known for decades, have gained significant attention in recent years due to advancements that have made them practically applicable in real-world scenarios. ZKPs can provide unique attributes, such as succinctness, non-interactivity, and the ability to prove knowledge without revealing the information itself, making them an attractive solution for a range of applications. This paper aims to critically analyze the applicability of ZKPs in various scenarios. We categorize ZKPs into distinct types: SNARKs (Succinct Non-Interactive Arguments of Knowledge), Commit-then-Prove ZKPs, MPC-in-the-Head, and Sigma Protocols, each offering different trade-offs and benefits. We introduce a flowchart methodology to assist in determining the most suitable ZKP system, given a set of technical application requirements. Next, we conduct an in-depth investigation of three major use cases: Outsourcing Computation, Digital Self-Sovereign Identity, and ZKPs in networking. Additionally, we provide a high-level overview of other applications of ZKPs, exploring their broader implications and opportunities. This paper aims to demystify the decision-making process involved in choosing the right ZKP system, providing clarity on when and how these cryptographic tools can be effectively utilized in various domains — and when they are better to be avoided.

  匹配依据：MPC: mpc (context)

  </details>

- **Send Message to the Future? Blockchain-based Time Machines for Decentralized Reveal of Locked Information**
  2024-01-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.05947)
  Zhuolun Li, Srijoni Majumdar, Evangelos Pournaras

  <details><summary>摘要 / Abstract</summary>

  Conditional information reveal systems automate the release of information upon meeting specific predefined conditions, such as time or location. This paper introduces a breakthrough in the understanding, design, and application of conditional information reveal systems that are highly secure and decentralized. By designing a new practical timed-release cryptography system and a secret sharing scheme with reveal-verifiability, a novel data sharing system is devised on the blockchain that &quot;sends messages in the future&quot; with highly accurate decryption times. Notably, the proposed secret sharing scheme applies to other applications requiring verifiability of revealed secret shares. This paper provides a complete evaluation portfolio of this pioneering paradigm, including analytical results, a validation of its robustness in the Tamarin Prover and a performance evaluation of a real-world, open-source system prototype deployed across the globe. Using real-world election data, we also demonstrate the applicability of this innovative system in e-voting, illustrating its capacity to secure and ensure fair electronic voting processes.

  匹配依据：MPC: secret sharing

  </details>

- **Probabilistic versions of Quantum Private Queries**
  2024-01-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.05754)
  Silvia Onofri, Vittorio Giovannetti

  <details><summary>摘要 / Abstract</summary>

  The no-go theorem regarding unconditionally secure Quantum Bit Commitment protocols is a relevant result in quantum cryptography. Such result has been used to prove the impossibility of unconditional security for other protocols, such as Quantum Oblivious Transfer or One-Sided Two Party Computation. In this paper, we formally define two non-deterministic versions of Quantum Private Queries, a protocol addressing the Symmetric-Private Information Retrieval problem. We show that the strongest variant of such scheme is formally equivalent to Quantum Bit Commitment, Quantum Oblivious Transfer and One-Sided Two Party Computation protocols. This equivalence serves as conclusive evidence of the impracticality of achieving unconditionally secure Strong Probabilistic Quantum Private Queries.

  匹配依据：MPC: oblivious transfer, two party computation

  </details>

- **Adaptive Distributional Security for Garbling Schemes with $\\mathcal{O}(\|x\|)$ Online Complexity**
  2024-01-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/044)
  Estuardo Alpírez Bock, Chris Brzuska, Pihla Karanko, Sabine Oechsner, Kirthivaasan Puniamurthy

  <details><summary>摘要 / Abstract</summary>

  Garbling schemes allow to garble a circuit $C$ and an input $x$ such that $C(x)$ can be computed while hiding both $C$ and $x$. In the context of adaptive security, an adversary specifies the input to the circuit after seeing the garbled circuit, so that one can pre-process the garbling of $C$ and later only garble the input $x$ in the online phase. Since the online phase may be time-critical, it is an interesting question how much information needs to be transmitted in this phase and ideally, this should be close to $|x|$. Unfortunately, Applebaum, Ishai, Kushilevitz, and Waters (AIKW, CRYPTO 2013) show that for some circuits, specifically PRGs, achieving online complexity close to $|x|$ is impossible with simulation-based security, and Hubáček and Wichs (HW, ITCS 2015) show that online complexity of maliciously secure two-party computation needs to grow with the incompressibility entropy of the function. We thus seek to understand under which circumstances optimal online complexity is feasible despite these strong lower bounds. Our starting point is the observation that lower bounds (only) concern cryptographic circuits and that, when an embedded secret is not known to the adversary (distinguisher), then the lower bound techniques do not seem to apply. Our main contribution is distributional simulation-based security (DSIM), a framework for capturing weaker, yet meaningful simulation-based (adaptive) security which does not seem to suffer from impossibility results akin to AIKW. We show that DSIM can be used to prove security of a distributed symmetric encryption protocol built around garbling. We also establish a bootstrapping result from DSIM-security for $\text{NC}^0$ circuits to DSIM-security for arbitrary polynomial-size circuits while preserving their online complexity.

  匹配依据：MPC: garbled circuit, garbling schemes, secure two party computation

  </details>

- **How (not) to hash into class groups of imaginary quadratic fields?**
  2024-01-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/034)
  István András Seres, Péter Burcsi, Péter Kutas

  <details><summary>摘要 / Abstract</summary>

  Class groups of imaginary quadratic fields (class groups for short) have seen a resurgence in cryptography as transparent groups of unknown order. They are a prime candidate for being a trustless alternative to RSA groups because class groups do not need a (distributed) trusted setup to sample a cryptographically secure group of unknown order. Class groups have recently found many applications in verifiable secret sharing, secure multiparty computation, transparent polynomial commitments, and perhaps most importantly, in time-based cryptography, i.e., verifiable delay functions, (homomorphic) time-lock puzzles, timed commitments, etc. However, there are various roadblocks to making class groups widespread in practical cryptographic deployments. We initiate the rigorous study of hashing into class groups. Specifically, we want to sample a uniformly distributed group element in a class group such that nobody knows its discrete logarithm with respect to any public parameter. We point out several flawed algorithms in numerous publicly available class group libraries. We further illustrate the insecurity of these hash functions by showing concrete attacks against cryptographic protocols, i.e., verifiable delay functions, if they were deployed with one of those broken hash-to-class group functions. We propose two families of cryptographically secure hash functions into class groups. We implement these constructions and evaluate their performance. We release our implementation as an open-source library.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **A New Approach to Efficient and Secure Fixed-point Computation**
  2024-01-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/035)
  Tore Kasper Frederiksen, Jonas Lindstrøm, Mikkel Wienberg Madsen, Anne Dorte Spangsberg

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation (MPC) constructions typically allow computation over a finite field or ring. While useful for many applications, certain real-world applications require the usage of decimal numbers. While it is possible to emulate floating-point operations in MPC, fixed-point computation has gained more traction in the practical space due to its simplicity and efficient realizations. Even so, current protocols for fixed-point MPC still require computing a secure truncation after each multiplication gate. In this paper, we show a new paradigm for realizing fixed-point MPC. Starting from an existing MPC protocol over arbitrary, large, finite fields or rings, we show how to realize MPC over a residue number system (RNS). This allows us to leverage certain mathematical structures to construct a secure algorithm for efficient approximate truncation by a static and public value. We then show how this can be used to realize highly efficient secure fixed-point computation. In contrast to previous approaches, our protocol does not require any multiplications of secret values in the underlying MPC scheme to realize truncation but instead relies on preprocessed pairs of correlated random values, which we show can be constructed very efficiently, when accepting a small amount of leakage and robustness in the strong, covert model. We proceed to implement our protocol, with SPDZ as the underlying MPC protocol, and achieve significantly faster fixed-point multiplication.

  匹配依据：MPC: secure multi party computation

  </details>

- **YouChoose: A Lightweight Anonymous Proof of Account Ownership**
  2024-01-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/029)
  Aarav Varshney, Prashant Agrawal, Mahabir Prasad Jhanwar

  <details><summary>摘要 / Abstract</summary>

  Anonymous proofs of account ownership (anonymous PAOs) enable a prover to convince a verifier that the prover owns a valid account at a server without revealing their identity. Importantly, no server-side changes are required - the server does not even learn that such a proof is taking place. This functionality is particularly valuable in sensitive applications such as whistleblowing, or in settings where infrastructural changes at the server are impractical. Anonymous PAOs were first introduced by Wang et al. (IEEE S&amp;P 2019), who realized them in the email setting via secure channel injection (SCI), a technique that requires carefully engineered multi-party computation (MPC) protocols. In this work, we propose YouChoose, a new approach to anonymous PAO that avoids MPC entirely, relying instead on the verifier to selectively forward TLS records. Compared to SCI, YouChoose is simpler, faster, and more adaptable across services. We also provide the first formal security definition for anonymous PAOs, establishing a rigorous framework for analysis and future constructions. Finally, we present a prototype implementation of YouChoose, evaluate it in the context of email and other social media accounts, showing its better performance than SCI with minimal latency overhead in practice.

  匹配依据：MPC: multi party computation

  </details>

- **Feldman's Verifiable Secret Sharing for a Dishonest Majority**
  2024-01-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/031)
  Yi-Hsiu Chen, Yehuda Lindell

  <details><summary>摘要 / Abstract</summary>

  Verifiable secret sharing (VSS) protocols enable parties to share secrets while guaranteeing security (in particular, that all parties hold valid and consistent shares) even if the dealer or some of the participants are malicious. Most work on VSS focuses on the honest majority case, primarily since it enables one to guarantee output delivery (e.g., a corrupted recipient cannot prevent an honest dealer from sharing their value). Feldman&#x27;s VSS is a well known and popular protocol for this task and relies on the discrete log hardness assumption. In this paper, we present a variant of Feldman&#x27;s VSS for the dishonest majority setting and formally prove its security. Beyond the basic VSS protocol, we present a publicly-verifiable version, as well as show how to securely add participants to the sharing and how to refresh an existing sharing (all secure in the presence of a dishonest majority). We prove that our protocols are UC secure, for appropriately defined ideal functionalities.

  匹配依据：MPC: secret sharing

  </details>

- **Unconditionally secure MPC for Boolean circuits with constant online communication**
  2024-01-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/015)
  Zhenkai Hu, Kang Yang, Yu Yu

  <details><summary>摘要 / Abstract</summary>

  Through tremendous efforts, the communication cost of secure multi-party computation (MPC) in the honest-majority setting has been significantly improved. In particular, the state-of-the-art honest-majority MPC protocol by Escudero et al. (CCS&#x27;22) takes 12 field elements in total per multiplication gate for arithmetic circuits in the online phase. However, it still requires $12 \log(5n/4)$ bits of online communication per AND gate for Boolean circuits. That is, for Boolean circuits, no MPC protocol with constant online communication is known. In this paper, we present an unconditionally secure MPC protocol for Boolean circuits in the honest-majority setting, which has constant online communication complexity and the offline communication complexity linear to the number $n$ of parties. We first describe the semi-honest MPC protocol and then show how to extend it to achieve malicious security, where the maliciously secure protocol has the same communication cost as the semi-honest protocol. In particular, our protocol achieves the amortized communication cost $36$ bits per AND gate in the online phase, $18n+24$ bits per AND gate in the offline phase. For those circuit wires that require routing, each wire incurs a communication overhead of $15n$ bits in the offline phase.

  匹配依据：MPC: secure multi party computation

  </details>

- **A Lattice-based Accountable Subgroup Multi-signature Scheme with Verifiable Group Setup**
  2024-01-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/014)
  Ahmet Ramazan Ağırtaş, Oğuz YAYLA

  <details><summary>摘要 / Abstract</summary>

  An accountable subgroup multi-signature (ASM) is a multi-signature that allows any subgroup of potential signers to jointly sign a message such that the subgroup of co-signers are accountable for the resulting signature and their identities are identifiable to any verifier. In this paper, we pro- pose a novel lattice-based accountable subgroup multi-signature scheme, i.e., vMS2, by combining the group setup method of recently proposed vASM scheme and Damgard et al.’s lattice-based MS2 multi-signature scheme. Key generation, signature generation and verification phases of our proposed scheme are almost identical to the MS2 scheme. In the group setup phase, we generate membership keys which is used for signing a message on behalf of a group G of users. These membership keys are generated via a joint verifiable secret sharing (VSS) scheme in a way that they include a piece of information from the secret keys of all users in G so that any subgroup of users in G having a valid membership key can sign in an accountable fashion. We also present a comparison of the underlying MS2 scheme and our accountable subgroup multi-signature scheme vMS2 to show the cost of accountability. We see that lattice-based accountable subgroup multi-signature scheme can be achieved by adding a one-time one-round group setup whose cost is slightly higher than signature generation and verification of the underlying MS2 signature scheme.

  匹配依据：MPC: secret sharing

  </details>

- **Information-Theoretically Secure Distributed Protocols for Two-Party MPC Primitives**
  2024-01-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/009)
  Tamir Tassa, Aviad Ben Arie

  <details><summary>摘要 / Abstract</summary>

  We study two-party secure computation in a \emph{distributed mediated} model with $D$ servers. We present \emph{information-theoretically secure} protocols for foundational primitives— $1$-out-of-$N$ and $k$-out-of-$N$ oblivious transfer (OT), Priced OT, Generalized OT, and Oblivious Multivariate Polynomial Evaluation (OMPE)—that (i) enforce receiver correctness, (ii) support an offline sender after setup, and (iii) achieve robustness against malicious receivers and malicious servers under honest-majority assumptions. Our approach reduces each primitive to a distributed scalar-product core combined with a \emph{distributed vector-validation} (DVV) mechanism that prevents unauthorized linear-combination leakage while preserving privacy. We prove unconditional privacy and robustness in the semi-honest setting and extend the guarantees to the malicious-server setting, tolerating up to $c &lt; D/4$ or $c &lt; D/3$ corrupt servers depending on the variant. The constructions are modular, require only lightweight client work (sharing and reconstruction), and allow the sender’s one-time upload to serve multiple, independent receivers without further interaction. We analyze the round and communication complexity of our protocols and provide empirical evidence of practical efficiency. The mediated setting naturally fits privacy-preserving services such as collaborative filtering, distributed constraint optimization, voting, and federated analytics. Collectively, our results show that distributed mediation yields simple, scalable, and unconditionally private realizations of core two-party MPC functionalities.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **The Multiple Millionaires' Problem: New Algorithmic Approaches and Protocols**
  2024-01-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/005)
  Tamir Tassa, Avishay Yanai

  <details><summary>摘要 / Abstract</summary>

  We study a fundamental problem in Multi-Party Computation, which we call the Multiple Millionaires’ Problem (MMP). Given a set of private integer inputs, the problem is to identify the subset of inputs that equal the maximum (or minimum) of that set, without revealing any further information on the inputs beyond what is implied by the desired output. Such a problem is a natural extension of the Millionaires’ Problem, which is the very first Multi- Party Computation problem that was presented in Andrew Yao’s seminal work [30 ]. A closely related problem is MaxP, in which the value of the maximum is sought. We study these fundamental problems and describe several algorithmic approaches and protocols for their solution. In addition, we compare the performance of the protocols under several selected settings. As applications of privacy-preserving computation are more and more commonly implemented in industrial systems, MMP and MaxP become important building blocks in privacy-preserving statistics, machine learning, auctions and other domains. One of the prominent advantages of the protocols that we present here is their simplicity. As they solve fundamental problems that are essential building blocks in various application scenarios, we believe that the presented solutions to those problems, and the comparison between them, will serve well future researchers and practitioners of secure distributed computing.

  匹配依据：MPC: multi party computation

  </details>

- **Practical Two-party Computational Differential Privacy with Active Security**
  2024-01-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/004)
  Fredrik Meisingseth, Christian Rechberger, Fabian Schmid

  <details><summary>摘要 / Abstract</summary>

  In this work we revisit the problem of using general-purpose MPC schemes to emulate the trusted dataholder in differential privacy (DP), to achieve the same accuracy but without the need to trust one single dataholder. In particular, we consider the two-party model where two computational parties (or dataholders), each with their own dataset, wish to compute a canonical DP mechanism on their combined data and to do so with active security. We start by remarking that available definitions of computational DP (CDP) for protocols are somewhat ill-suited for such a use-case, due to them either poorly capturing some strong security guarantees commonly given by general-purpose MPC protocols, or having too strict requirements in the sense that they need significant adjustment in order to be satisfiable by using common DP and MPC techniques. With this in mind, we propose a new version of simulation-based CDP, called SIM$^*$-CDP, and prove it to be stronger than the IND-CDP and SIM-CDP and incomparable to SIM$^+$-CDP. We demonstrate the usability of the SIM$^*$-CDP definition by showing how to satisfy it by the use of an available distributed protocol for sampling truncated geometric noise. Further, we use the protocol to compute two-party inner-products with CDP and active security, and with accuracy equal to that of the central model, being the first to do so. Finally, we provide an open-sourced implementation and benchmark its practical performance. Our implementation generates a truncated geometric sample in between about 0.035 and 3.5 seconds (amortized), depending on network and parameter settings, comparing favourably to existing implementations.

  匹配依据：MPC: mpc (context)

  </details>

- **SecFormer: Fast and Accurate Privacy-Preserving Inference for Transformer Models via SMPC**
  2024-01-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.00793)
  Jinglong Luo, Yehong Zhang, Zhuo Zhang, Jiaqi Zhang, Xin Mu, Hui Wang, Yue Yu, Zenglin Xu

  <details><summary>摘要 / Abstract</summary>

  With the growing use of Transformer models hosted on cloud platforms to offer inference services, privacy concerns are escalating, especially concerning sensitive data like investment plans and bank account details. Secure Multi-Party Computing (SMPC) emerges as a promising solution to protect the privacy of inference data and model parameters. However, the application of SMPC in Privacy-Preserving Inference (PPI) for Transformer models often leads to considerable slowdowns or declines in performance. This is largely due to the multitude of nonlinear operations in the Transformer architecture, which are not well-suited to SMPC and difficult to circumvent or optimize effectively. To address this concern, we introduce a comprehensive PPI framework called SecFormer to achieve fast and accurate PPI for Transformer models. We successfully eliminate the high-cost exponential and maximum operations in PPI without sacrificing model performance and develop a suite of efficient SMPC protocols by employing suitable numerical computation methods to boost other complex nonlinear functions in PPI, including GeLU, LayerNorm, and a redesigned Softmax. Our extensive experiments reveal that SecFormer outperforms MPCFormer in performance, showing improvements of $3.4\%$ and $24.7\%$ for BERT$_{\text{BASE}}$ and BERT$_{\text{LARGE}}$, respectively. In terms of efficiency, SecFormer is 3.57 and 3.58 times faster than PUMA for BERT$_{\text{BASE}}$ and BERT$_{\text{LARGE}}$, demonstrating its effectiveness and speed.

  匹配依据：MPC: secure multi party computing

  </details>

- **Privacy-Preserving Data in IoT-based Cloud Systems: A Comprehensive Survey with AI Integration**
  2024-01-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.00794)
  D. Dhinakaran, S. M. Udhaya Sankar, D. Selvaraj, S. Edwin Raja

  <details><summary>摘要 / Abstract</summary>

  As the integration of Internet of Things devices with cloud computing proliferates, the paramount importance of privacy preservation comes to the forefront. This survey paper meticulously explores the landscape of privacy issues in the dynamic intersection of IoT and cloud systems. The comprehensive literature review synthesizes existing research, illuminating key challenges and discerning emerging trends in privacy preserving techniques. The categorization of diverse approaches unveils a nuanced understanding of encryption techniques, anonymization strategies, access control mechanisms, and the burgeoning integration of artificial intelligence. Notable trends include the infusion of machine learning for dynamic anonymization, homomorphic encryption for secure computation, and AI-driven access control systems. The culmination of this survey contributes a holistic view, laying the groundwork for understanding the multifaceted strategies employed in securing sensitive data within IoT-based cloud environments. The insights garnered from this survey provide a valuable resource for researchers, practitioners, and policymakers navigating the complex terrain of privacy preservation in the evolving landscape of IoT and cloud computing

  匹配依据：MPC: secure computation

  </details>
