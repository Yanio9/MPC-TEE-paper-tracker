# 2023 · MPC · 仅预印本来源 · 第 2/4 页

[总目录](../PAPERS.md) · [上一页](2023-mpc-preprint-01.md) · [下一页](2023-mpc-preprint-03.md)

- **QR TPM in Programmable Low-Power Devices**
  2023-09-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.17414)
  Luís Fiolhais, Leonel Sousa

  <details><summary>摘要 / Abstract</summary>

  Trusted Platform Modules (TPMs), which serve as the root of trust in secure systems, are secure crypto-processors that carry out cryptographic primitives. Should large-scale quantum computing become a reality, the cryptographic primitives adopted in the TPM 2.0 standard will no longer be secure. Thus, the design of TPMs that provide Quantum Resistant (QR) primitives is of utmost importance, in particular with the restrictions imposed by embedded systems. In this paper, we investigate the deployment of QR primitives and protocols in the standard TPM 2.0. Cryptographic algorithms that are already in the NIST QR cryptography standardization process, as well as an Oblivious Transfer (OT), a fundamental cryptographic primitive, are the QR cryptographic schemes selected to extend TPM 2.0. In particular, the Kyber algorithm for key encapsulation, the Dilithium algorithm for digital signature, and a 3-round Random Oblivious Transfer (ROT) protocol, supporting protocols such as Multi-Party Computation and Private Set Intersection (PSI). The QR extended TPM 2.0 is implemented in ARM and RISC-V embedded processors, its computational requirements are analysed and experimentally evaluated in comparison to the standard TPM. It is shown that Kyber and Dilithium are faster at creating keys than RSA, due to the key size and secure random sampling required in RSA, while they meet the same performance level as ECC. For digital signatures, both in signature creation and verification, Dilithium is on par with RSA and ECC. The ROT protocol shows decent performance and its support required small modifications to the TPM. This paper also shows that it would be possible to backport the required code to already available TPMs to ensure that current TPMs remain secure against quantum adversaries.

  匹配依据：MPC: multi party computation, oblivious transfer, private set intersection

  </details>

- **Mostree : Malicious Secure Private Decision Tree Evaluation with Sublinear Communication**
  2023-09-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.17124)
  Jianli Bai, Xiangfu Song, Xiaowu Zhang, Qifan Wang, Shujie Cui, Ee-Chien Chang, Giovanni Russello

  <details><summary>摘要 / Abstract</summary>

  A private decision tree evaluation (PDTE) protocol allows a feature vector owner (FO) to classify its data using a tree model from a model owner (MO) and only reveals an inference result to the FO. This paper proposes Mostree, a PDTE protocol secure in the presence of malicious parties with sublinear communication. We design Mostree in the three-party honest-majority setting, where an (untrusted) computing party (CP) assists the FO and MO in the secure computation. We propose two low-communication oblivious selection (OS) protocols by exploiting nice properties of three-party replicated secret sharing (RSS) and distributed point function. Mostree combines OS protocols with a tree encoding method and three-party secure computation to achieve sublinear communication. We observe that most of the protocol components already maintain privacy even in the presence of a malicious adversary, and what remains to achieve is correctness. To ensure correctness, we propose a set of lightweight consistency checks and seamlessly integrate them into Mostree. As a result, Mostree achieves sublinear communication and malicious security simultaneously. We implement Mostree and compare it with the state-of-the-art. Experimental results demonstrate that Mostree is efficient and comparable to semi-honest PDTE schemes with sublinear communication. For instance, when evaluated on the MNIST dataset in a LAN setting, Mostree achieves an evaluation using approximately 768 ms with communication of around 168 KB.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Libertas: Privacy-Preserving Collective Computation for Decentralised Personal Data Stores**
  2023-09-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.16365)
  Rui Zhao, Naman Goel, Nitin Agrawal, Jun Zhao, Jake Stein, Wael Albayaydh, Ruben Verborgh, Reuben Binns, Tim Berners-Lee, Nigel Shadbolt

  <details><summary>摘要 / Abstract</summary>

  Data and data processing have become an indispensable aspect for our society. Insights drawn from collective data make invaluable contribution to scientific and societal research and business. But there are increasing worries about privacy issues and data misuse. This has prompted the emergence of decentralised personal data stores (PDS) like Solid that provide individuals more control over their personal data. However, existing PDS frameworks face challenges in ensuring data privacy when performing collective computations with data from multiple users. While Secure Multi-Party Computation (MPC) offers input secrecy protection during the computation without relying on any single party, issues emerge when directly applying MPC in the context of PDS, particularly due to key factors like autonomy and decentralisation. In this work, we discuss the essence of this issue, identify a potential solution, and introduce a modular architecture, Libertas, to integrate MPC with PDS like Solid, without requiring protocol-level changes. We introduce a paradigm shift from an `omniscient&#x27; view to individual-based, user-centric view of trust and security, and discuss the threat model of Libertas. Two realistic use cases for collaborative data processing are used for evaluation, both for technical feasibility and empirical benchmark, highlighting its effectiveness in empowering gig workers and generating differentially private synthetic data. The results of our experiments underscore Libertas&#x27; linear scalability and provide valuable insights into compute optimisations, thereby advancing the state-of-the-art in privacy-preserving data processing practices. By offering practical solutions for maintaining both individual autonomy and privacy in collaborative data processing environments, Libertas contributes significantly to the ongoing discourse on privacy protection in data-driven decision-making contexts.

  匹配依据：MPC: secure multi party computation

  </details>

- **Differentially Private Secure Multiplication: Hiding Information in the Rubble of Noise**
  2023-09-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.16105)
  Viveck R. Cadambe, Ateet Devulapalli, Haewon Jeong, Flavio P. Calmon

  <details><summary>摘要 / Abstract</summary>

  We consider the problem of private distributed multi-party multiplication. It is well-established that Shamir secret-sharing coding strategies can enable perfect information-theoretic privacy in distributed computation via the celebrated algorithm of Ben Or, Goldwasser and Wigderson (the &quot;BGW algorithm&quot;). However, perfect privacy and accuracy require an honest majority, that is, $N \geq 2t+1$ compute nodes are required to ensure privacy against any $t$ colluding adversarial nodes. By allowing for some controlled amount of information leakage and approximate multiplication instead of exact multiplication, we study coding schemes for the setting where the number of honest nodes can be a minority, that is $N&lt; 2t+1.$ We develop a tight characterization privacy-accuracy trade-off for cases where $N &lt; 2t+1$ by measuring information leakage using {differential} privacy instead of perfect privacy, and using the mean squared error metric for accuracy. A novel technical aspect is an intricately layered noise distribution that merges ideas from differential privacy and Shamir secret-sharing at different layers.

  匹配依据：MPC: secret sharing

  </details>

- **SOCI^+: An Enhanced Toolkit for Secure OutsourcedComputation on Integers**
  2023-09-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.15406)
  Bowen Zhao, Weiquan Deng, Xiaoguo Li, Ximeng Liu, Qingqi Pei, Robert H. Deng

  <details><summary>摘要 / Abstract</summary>

  Secure outsourced computation is critical for cloud computing to safeguard data confidentiality and ensure data usability. Recently, secure outsourced computation schemes following a twin-server architecture based on partially homomorphic cryptosystems have received increasing attention. The Secure Outsourced Computation on Integers (SOCI) [1] toolkit is the state-of-the-art among these schemes which can perform secure computation on integers without requiring the costly bootstrapping operation as in fully homomorphic encryption; however, SOCI suffers from relatively large computation and communication overhead. In this paper, we propose SOCI+ which significantly improves the performance of SOCI. Specifically, SOCI+ employs a novel (2, 2)-threshold Paillier cryptosystem with fast encryption and decryption as its cryptographic primitive, and supports a suite of efficient secure arithmetic computation on integers protocols, including a secure multiplication protocol (SMUL), a secure comparison protocol (SCMP), a secure sign bit-acquisition protocol (SSBA), and a secure division protocol (SDIV), all based on the (2, 2)-threshold Paillier cryptosystem with fast encryption and decryption. In addition, SOCI+ incorporates an offline and online computation mechanism to further optimize its performance. We perform rigorous theoretical analysis to prove the correctness and security of SOCI+. Compared with SOCI, our experimental evaluation shows that SOCI+ is up to 5.4 times more efficient in computation and 40% less in communication overhead.

  匹配依据：MPC: secure computation

  </details>

- **Coexistence of multiuser entanglement distribution and classical light in optical fiber network with a semiconductor chip**
  2023-09-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.14602)
  Xu Jing, Cheng Qian, Hu Nian, Chenquan Wang, Jie Tang, Xiaowen Gu, Yuechan Kong, Tangsheng Chen, Yichen Liu, Chong Sheng, Dong Jiang, Bin Niu, Liangliang Lu

  <details><summary>摘要 / Abstract</summary>

  Building communication links among multiple users in a scalable and robust way is a key objective in achieving large-scale quantum networks. In realistic scenario, noise from the coexisting classical light is inevitable and can ultimately disrupt the entanglement. The previous significant fully connected multiuser entanglement distribution experiments are conducted using dark fiber links and there is no explicit relation between the entanglement degradations induced by classical noise and its error rate. Here we fabricate a semiconductor chip with a high figure-of-merit modal overlap to directly generate broadband polarization entanglement. Our monolithic source maintains polarization entanglement fidelity above 96% for 42 nm bandwidth with a brightness of 1.2*10^7 Hz/mW. We perform a continuously working quantum entanglement distribution among three users coexisting with classical light. Under finite-key analysis, we establish secure keys and enable images encryption as well as quantum secret sharing between users. Our work paves the way for practical multiparty quantum communication with integrated photonic architecture compatible with real-world fiber optical communication network.

  匹配依据：MPC: secret sharing

  </details>

- **Zero-Knowledge Systems from MPC-in-the-Head and Oblivious Transfer**
  2023-09-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1470)
  Cyprien Delpech de Saint Guilhem, Ehsan Ebrahimi, Barry van Leeuwen

  <details><summary>摘要 / Abstract</summary>

  Zero-knowledge proof or argument systems for generic NP statements (such as circuit satisfiability) have typically been instantiated with cryptographic commitment schemes; this implies that the security of the proof system (e.g., computational or statistical) depends on that of the chosen commitment scheme. The MPC-in-the-Head paradigm (Ishai et al., JoC 2009) uses the same approach to construct zero-knowledge systems from the simulated execution of secure multiparty computation protocols. This paper presents a novel method to construct zero-knowledge protocols which takes advantage of the unique properties of MPC-in-the-Head and replaces commitments with an oblivious transfer protocol. The security of the new construction is proven in the Universal Composability framework of security and suitable choices of oblivious transfer protocols are discussed together with their implications on the security properties and computational efficiency of the zero-knowledge system.

  匹配依据：MPC: oblivious transfer, secure multiparty computation

  </details>

- **Random-Energy Secret Sharing via Extreme Synergy**
  2023-09-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.14047)
  Vudtiwat Ngampruetikorn, David J. Schwab

  <details><summary>摘要 / Abstract</summary>

  The random-energy model (REM), a solvable spin-glass model, has impacted an incredibly diverse set of problems, from protein folding to combinatorial optimization to many-body localization. Here, we explore a new connection to secret sharing. We formulate a secret-sharing scheme, based on the REM, and analyze its information-theoretic properties. Our analyses reveal that the correlations between subsystems of the REM are highly synergistic and form the basis for secure secret-sharing schemes. We derive the ranges of temperatures and secret lengths over which the REM satisfies the requirement of secure secret sharing. We show further that a special point in the phase diagram exists at which the REM-based scheme is optimal in its information encoding. Our analytical results for the thermodynamic limit are in good qualitative agreement with numerical simulations of finite systems, for which the strict security requirement is replaced by a tradeoff between secrecy and recoverability. Our work offers a further example of information theory as a unifying concept, connecting problems in statistical physics to those in computation.

  匹配依据：MPC: secret sharing

  </details>

- **Efficacy and Mitigation of the Cryptanalysis on AIM**
  2023-09-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1474)
  Seongkwang Kim, Jincheol Ha, Mincheol Son, Byeonghak Lee

  <details><summary>摘要 / Abstract</summary>

  Recent advancements in post-quantum cryptography have highlighted signature schemes based on the MPC-in-the-Head (MPCitH) framework due to their reliance only on the one-way function of the underlying primitive. This reliance offers a diverse set of assumptions regarding the difficulty of post-quantum cryptographic problems. In this context, Kim et al. proposed $\mathsf{AIM}$, an MPCitH-compatible one-way function. This function is distinguished by its large algebraic S-boxes and parallel architecture, contributing to the reduced size of signatures, as presented at CCS 2023. However, $\mathsf{AIM}$ has faced several cryptanalytic challenges, which have potentially weakened its security by up to 15 bits. This paper provides a comprehensive overview of these cryptanalytic methods and proposes $\mathsf{AIM2}$, an enhanced version that addresses these identified vulnerabilities. We conduct an extensive analysis of its resilience to algebraic attacks and detail the modifications in its efficiency.

  匹配依据：MPC: mpc (context)

  </details>

- **Round-Robin is Optimal: Lower Bounds for Group Action Based Protocols**
  2023-09-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1464)
  Daniele Cozzo, Emanuele Giunta

  <details><summary>摘要 / Abstract</summary>

  An hard homogeneous space (HHS) is a finite group acting on a set with the group action being hard to invert and the set lacking any algebraic structure. As such HHS could potentially replace finite groups where the discrete logarithm is hard for building cryptographic primitives and protocols in a post-quantum world. Threshold HHS-based primitives typically require parties to compute the group action of a secret-shared input on a public set element. On one hand this could be done through generic MPC techniques, although they incur in prohibitive costs due to the high complexity of circuits evaluating group actions known to date. On the other hand round-robin protocols only require black box usage of the HHS. However these are highly sequential procedures, taking as many rounds as parties involved. The high round complexity appears to be inherent due the lack of homomorphic properties in HHS, yet no lower bounds were known so far. In this work we formally show that round-robin protocols are optimal. In other words, any at least passively secure distributed computation of a group action making black-box use of an HHS must take a number of rounds greater or equal to the threshold parameter. We furthermore study fair protocols in which all users receive the output in the same round (unlike plain round-robin), and prove communication and computation lower bounds of $\Omega(n \log_2 n)$ for $n$ parties. Our results are proven in Shoup&#x27;s Generic Action Model (GAM), and hold regardless of the underlying computational assumptions.

  匹配依据：MPC: mpc (context)

  </details>

- **Quantum Privacy-Preserving Price E-Negotiation**
  2023-09-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.13668)
  Wen-Jie Liu, Chun-Tang Li, Yu Zheng, Yong Xu, Yin-Song Xu

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving price e-negotiation (3PEN) is an important topic of secure multi-party computation (SMC) in the electronic commerce field, and the key point of its security is to guarantee the privacy of seller&#x27;s and buyer&#x27;s prices. In this study, a novel and efficient quantum solution to the 3PEN problem is proposed, where the oracle operation and the qubit comparator are utilized to obtain the comparative results of buyer&#x27;s and seller&#x27;s prices, and then quantum counting is executed to summarize the total number of products which meets the trading conditions. Analysis shows that our solution not only guarantees the correctness and the privacy of 3PEN, but also has lower communication complexity than those classical ones.

  匹配依据：MPC: secure multi party computation

  </details>

- **A Novel Quantum Visual Secret Sharing Scheme**
  2023-09-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.13659)
  Wenjie Liu, Yinsong Xu, Maojun Zhang, Junxiu Chen, Ching-Nung Yang

  <details><summary>摘要 / Abstract</summary>

  Inspired by Naor et al.&#x27;s visual secret sharing (VSS) scheme, a novel n out of n quantum visual secret sharing (QVSS) scheme is proposed, which consists of two phases: sharing process and recovering process. In the first process, the color information of each pixel from the original secret image is encoded into an n-qubit superposition state by using the strategy of quantum expansion instead of classical pixel expansion, and then these n qubits are distributed as shares to n participants, respectively. During the recovering process, all participants cooperate to collect these n shares of each pixel together, then perform the corresponding measurement on them, and execute the n-qubit XOR operation to recover each pixel of the secret image. The proposed scheme has the advantage of single-pixel parallel processing that is not available in the existing analogous quantum schemes and perfectly solves the problem that in the classic VSS schemes the recovered image has the loss in resolution. Moreover, its experiment implementation with the IBM Q is conducted to demonstrate the practical feasibility.

  匹配依据：MPC: secret sharing

  </details>

- **Secure and Efficient Two-party Quantum Scalar Product Protocol With Application to Privacy-preserving Matrix Multiplication**
  2023-09-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.15856)
  Wen-Jie Liu, Zi-Xian Li

  <details><summary>摘要 / Abstract</summary>

  Secure two-party scalar product (S2SP) is a promising research area within secure multiparty computation (SMC), which can solve a range of SMC problems, such as intrusion detection, data analysis, and geometric computations. However, existing quantum S2SP protocols are not efficient enough, and the complexity is usually close to exponential level. In this paper, a novel secure two-party quantum scalar product (S2QSP) protocol based on Fourier entangled states is proposed to achieve higher efficiency. Firstly, the definition of unconditional security under malicious models is given. And then, an honesty verification method called Entanglement Bondage is proposed, which is used in conjunction with the modular summation gate to resist malicious attacks. The property of Fourier entangled states is used to calculate the scalar product with polynomial complexity. The unconditional security of our protocol is proved, which guarantees the privacy of all parties. In addition, we design a privacy-preserving quantum matrix multiplication protocol based on S2QSP protocol. By transforming matrix multiplication into a series of scalar product processes, the product of two private matrices is calculated without revealing any privacy. Finally, we show our protocol&#x27;s feasibility in IBM Qiskit simulator.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Privacy-Preserving Quantum Two-Party Geometric Intersection**
  2023-09-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.12605)
  Wen-Jie Liu, Yong Xu, James C. N. Yang, Wen-Bin Yu, Lian-Hua Chi

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving computational geometry is the research area on the intersection of the domains of secure multi-party computation (SMC) and computational geometry. As an important field, the privacy-preserving geometric intersection (PGI) problem is when each of the multiple parties has a private geometric graph and seeks to determine whether their graphs intersect or not without revealing their private information. In this study, through representing Alice&#x27;s (Bob&#x27;s) private geometric graph G_A (G_B) as the set of numbered grids S_A (S_B), an efficient privacy-preserving quantum two-party geometric intersection (PQGI) protocol is proposed. In the protocol, the oracle operation O_A (O_B) is firstly utilized to encode the private elements of S_A=(a_0, a_1, ..., a_(M-1)) (S_B=(b_0, b_1, ..., b_(N-1))) into the quantum states, and then the oracle operation O_f is applied to obtain a new quantum state which includes the XOR results between each element of S_A and S_B. Finally, the quantum counting is introduced to get the amount (t) of the states |a_i+b_j&gt; equaling to |0&gt;, and the intersection result can be obtained by judging t&gt;0 or not. Compared with classical PGI protocols, our proposed protocol not only has higher security, but also holds lower communication complexity.

  匹配依据：MPC: secure multi party computation

  </details>

- **Incentivizing Private Data Sharing in Vehicular Networks: A Game-Theoretic Approach**
  2023-09-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.12598)
  Yousef AlSaqabi, Bhaskar Krishnamachari

  <details><summary>摘要 / Abstract</summary>

  In the context of evolving smart cities and autonomous transportation systems, Vehicular Ad-hoc Networks (VANETs) and the Internet of Vehicles (IoV) are growing in significance. Vehicles are becoming more than just a means of transportation; they are collecting, processing, and transmitting massive amounts of data to make driving safer and more convenient. However, this advancement ushers in complex issues concerning the centralized structure of traditional vehicular networks and the privacy and security concerns around vehicular data. This paper offers a novel, game-theoretic network architecture to address these challenges. Our approach decentralizes data collection through distributed servers across the network, aggregating vehicular data into spatio-temporal maps via secure multi-party computation (SMPC). This strategy effectively reduces the chances of adversaries reconstructing a vehicle&#x27;s complete path, increasing privacy. We also introduce an economic model grounded in game theory that incentivizes vehicle owners to participate in the network, balancing the owners&#x27; privacy concerns with the monetary benefits of data sharing. This model aims to maximize the data consumer&#x27;s utility from the gathered sensor data by determining the most suitable payment to participating vehicles, the frequency in which these vehicles share their data, and the total number of servers in the network. We explore the interdependencies among these parameters and present our findings accordingly. To define meaningful utility and loss functions for our study, we utilize a real dataset of vehicular movement traces.

  匹配依据：MPC: secure multi party computation

  </details>

- **Popping “R-propping”: breaking hardness assumptions for matrix groups over F\_{2^8}**
  2023-09-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1425)
  Fernando Virdia

  <details><summary>摘要 / Abstract</summary>

  A recent series of works (Hecht, IACR ePrint, 2020–2021) propose to build post-quantum public-key encapsulation, digital signatures, group key agreement and oblivious transfer from &quot;R-propped&quot; variants of the Symmetrical Decomposition and Discrete Logarithm problems for matrix groups over $\mathbb{F}_{2^8}$. We break all four proposals by presenting a linearisation attack on the Symmetrical Decomposition platform, a forgery attack on the signature scheme, and a demonstration of the insecurity of the instances of the Discrete Logarithm Problem used for signatures, group key agreement and oblivious transfer, showing that none of the schemes provides adequate security.

  匹配依据：MPC: oblivious transfer

  </details>

- **Arithmetic Circuit Implementations of S-boxes for SKINNY and PHOTON in MPC**
  2023-09-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1426)
  Aysajan Abidin, Erik Pohle, Bart Preneel

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) enables multiple distrusting parties to compute a function while keeping their respective inputs private. In a threshold implementation of a symmetric primitive, e.g., of a block cipher, each party holds a share of the secret key or of the input block. The output block is computed without reconstructing the secret key. This enables the construction of distributed TPMs or transciphering for secure data transmission in/out of the MPC context. This paper investigates implementation approaches for the lightweight primitives SKINNY and PHOTON in arithmetic circuits. For these primitives, we identify arithmetic expressions for the S-box that result in smaller arithmetic circuits compared to the Boolean expressions from the literature. We validate the optimization using a generic actively secure MPC protocol and obtain 18% faster execution time with 49% less communication data for SKINNY-64-128 and 27% to 74% faster execution time with 49% to 81% less data for PHOTON $P_{100}$ and $P_{288}$. Furthermore, we find a new set of parameters for the heuristic method of polynomial decomposition, introduced by Coron, Roy and Vivek, specialized for SKINNY&#x27;s 8-bit S-box. We reduce the multiplicative depth from 9 to 5.

  匹配依据：MPC: secure multi party computation

  </details>

- **Generalized Fuzzy Password-Authenticated Key Exchange from Error Correcting Codes**
  2023-09-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1415)
  Jonathan Bootle, Sebastian Faller, Julia Hesse, Kristina Hostáková, Johannes Ottenhues

  <details><summary>摘要 / Abstract</summary>

  Fuzzy Password-Authenticated Key Exchange (fuzzy PAKE) allows cryptographic keys to be generated from authentication data that is both fuzzy and of low entropy. The strong protection against offline attacks offered by fuzzy PAKE opens an interesting avenue towards secure biometric authentication, typo-tolerant password authentication, and automated IoT device pairing. Previous constructions of fuzzy PAKE are either based on Error Correcting Codes (ECC) or generic multi-party computation techniques such as Garbled Circuits. While ECC-based constructions are significantly more efficient, they rely on multiple special properties of error correcting codes such as maximum distance separability and smoothness. We contribute to the line of research on fuzzy PAKE in two ways. First, we identify a subtle but devastating gap in the security analysis of the currently most efficient fuzzy PAKE construction (Dupont et al., Eurocrypt 2018), allowing a man-in-the-middle attacker to test individual password characters. Second, we provide a new fuzzy PAKE scheme based on ECC and PAKE that provides a built-in protection against individual password character guesses and requires fewer, more standard properties of the underlying ECC. Additionally, our construction offers better error correction capabilities than previous ECC-based fuzzy PAKEs.

  匹配依据：MPC: garbled circuits, multi party computation

  </details>

- **Fully Homomorphic Encryption-Based Protocols for Enhanced Private Set Intersection Functionalities**
  2023-09-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1407)
  JINGWEI HU, Junyan Chen, Wangchen Dai, Huaxiong Wang

  <details><summary>摘要 / Abstract</summary>

  This study delves into secure computations for set intersections using fully homomorphic encryption (FHE) within the semi-honest setting. Our protocols facilitate joint computations between two parties, each holding a set of inputs denoted as $N_s$ and $N_r$ in size, respectively. The primary objective is to determine various functionalities, such as intersection size and sum, while maintaining data confidentiality. These functionalities extend the classic private set intersection (PSI) and have practical applications in contact tracing, ad conversion analysis, and online dating, each abstracted into specialized PSI protocols. Our work demonstrates that these extended PSI functionalities are interconnected, with the PSI-cardinality protocol serving as the foundation. By adapting this protocol, we naturally arrive at PSI-sum-cardinality. Additionally, PSI-token-threshold is achieved by augmenting PSI-cardinality with FHE-based oblivious polynomial evaluation (OPE). The tPSI protocol combines PSI-token-threshold and standard PSI, allowing information sharing when the intersection size exceeds a threshold. Our protocols excel in simplicity, enhancing ease of understanding, implementation, optimization, and long-term maintenance. They also exhibit sublinear communication complexity concerning the larger sender&#x27;s set, rendering them well-suited for scenarios involving substantial data. Various optimization techniques further bolster their practical efficiency.

  匹配依据：MPC: private set intersection

  </details>

- **Robust Publicly Verifiable Covert Security: Limited Information Leakage and Guaranteed Correctness with Low Overhead**
  2023-09-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1392)
  Yi Liu, Junzuo Lai, Qi Wang, Xianrui Qin, Anjia Yang, Jian Weng

  <details><summary>摘要 / Abstract</summary>

  Protocols with \emph{publicly verifiable covert (PVC) security} offer high efficiency and an appealing feature: a covert party may deviate from the protocol, but with a probability (\eg $90\%$, referred to as the \emph{deterrence factor}), the honest party can identify this deviation and expose it using a publicly verifiable certificate. These protocols are particularly suitable for practical applications involving reputation-conscious parties. However, in the cases where misbehavior goes undetected (\eg with a probability of $10\%$), \emph{no security guarantee is provided for the honest party}, potentially resulting in a complete loss of input privacy and output correctness. In this paper, we tackle this critical problem by presenting a highly effective solution. We introduce and formally define an enhanced notion called \emph{robust PVC security}, such that even if the misbehavior remains undetected, the malicious party can only gain an additional $1$-bit of information about the honest party&#x27;s input while maintaining the correctness of the output. We propose a novel approach leveraging \emph{dual execution} and \emph{time-lock puzzles} to design a robust PVC-secure two-party protocol with \emph{low overhead} (depending on the deterrence factor). For instance, with a deterrence factor of $90\%$, our robust PVC-secure protocol incurs \emph{only additional ${\sim}10\%$ overhead} compared to the state-of-the-art PVC-secure protocol. Given the stronger security guarantees with low overhead, our protocol is highly suitable for practical applications of secure two-party computation.

  匹配依据：MPC: secure two party computation

  </details>

- **Online Efficient Secure Logistic Regression based on Function Secret Sharing**
  2023-09-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.09486)
  Jing Liu, Jamie Cui, Cen Chen

  <details><summary>摘要 / Abstract</summary>

  Logistic regression is an algorithm widely used for binary classification in various real-world applications such as fraud detection, medical diagnosis, and recommendation systems. However, training a logistic regression model with data from different parties raises privacy concerns. Secure Multi-Party Computation (MPC) is a cryptographic tool that allows multiple parties to train a logistic regression model jointly without compromising privacy. The efficiency of the online training phase becomes crucial when dealing with large-scale data in practice. In this paper, we propose an online efficient protocol for privacy-preserving logistic regression based on Function Secret Sharing (FSS). Our protocols are designed in the two non-colluding servers setting and assume the existence of a third-party dealer who only poses correlated randomness to the computing parties. During the online phase, two servers jointly train a logistic regression model on their private data by utilizing pre-generated correlated randomness. Furthermore, we propose accurate and MPC-friendly alternatives to the sigmoid function and encapsulate the logistic regression training process into a function secret sharing gate. The online communication overhead significantly decreases compared with the traditional secure logistic regression training based on secret sharing. We provide both theoretical and experimental analyses to demonstrate the efficiency and effectiveness of our method.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Modulation to the Rescue: Identifying Sub-Circuitry in the Transistor Morass for Targeted Analysis**
  2023-09-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.09782)
  Xhani Marvin Saß, Thilo Krachenfels, Frederik Dermot Pustelnik, Jean-Pierre Seifert, Christian Große, Frank Altmann

  <details><summary>摘要 / Abstract</summary>

  Physical attacks form one of the most severe threats against secure computing platforms. Their criticality arises from their corresponding threat model: By, e.g., passively measuring an integrated circuit&#x27;s (IC&#x27;s) environment during a security-related operation, internal secrets may be disclosed. Furthermore, by actively disturbing the physical runtime environment of an IC, an adversary can cause a specific, exploitable misbehavior. The set of physical attacks consists of techniques that apply either globally or locally. When compared to global techniques, local techniques exhibit a much higher precision, hence having the potential to be used in advanced attack scenarios. However, using physical techniques with additional spatial dependency expands the parameter search space exponentially. In this work, we present and compare two techniques, namely laser logic state imaging (LLSI) and lock-in thermography (LIT), that can be used to discover sub-circuitry of an entirely unknown IC based on optical and thermal principles. We show that the time required to identify specific regions can be drastically reduced, thus lowering the complexity of physical attacks requiring positional information. Our case study on an Intel H610 Platform Controller Hub showcases that, depending on the targeted voltage rail, our technique reduces the search space by around 90 to 98 percent.

  匹配依据：MPC: secure computing

  </details>

- **Algebraic Attacks on Round-Reduced RAIN and Full AIM-III**
  2023-09-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1397)
  Kaiyi Zhang, Qingju Wang, Yu Yu, Chun Guo, Hongrui Cui

  <details><summary>摘要 / Abstract</summary>

  Picnic is a NIST PQC Round 3 Alternate signature candidate that builds upon symmetric primitives following the MPC-in-the-head paradigm. Recently, researchers have been exploring more secure/efficient signature schemes from conservative one-way functions based on AES, or new low complexity one-way functions like Rain (CCS 2022) and AIM (CCS 2023). The signature schemes based on Rain and AIM are currently the most efficient among MPC-in-the-head-based schemes, making them promising post-quantum digital signature candidates. However, the exact hardness of these new one-way functions deserves further study and scrutiny. This work presents algebraic attacks on RAIN and AIM for certain instances, where one-round Rain can be compromised in $2^{n/2}$ for security parameter $n\in \{128,192,256\}$, and two-round Rain can be broken in $2^{120.3}$, $2^{180.4}$, and $2^{243.1}$ encryptions, respectively. Additionally, we demonstrate an attack on AIM-III (which aims at 192-bit security) with a complexity of $2^{186.5}$ encryptions. These attacks exploit the algebraic structure of the power function over fields with characteristic 2, which provides potential insights into the algebraic structures of some symmetric primitives and thus might be of independent interest.

  匹配依据：MPC: mpc (context)

  </details>

- **Verifiable Privacy-Preserving Computing**
  2023-09-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.08248)
  Tariq Bontekoe, Dimka Karastoyanova, Fatih Turkmen

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving computation (PPC) methods, such as secure multiparty computation (MPC) and homomorphic encryption (HE), are deployed increasingly often to guarantee data confidentiality in computations over private, distributed data. Similarly, we observe a steep increase in the adoption of zero-knowledge proofs (ZKPs) to guarantee (public) verifiability of locally executed computations. We project that applications that are data intensive and require strong privacy guarantees, are also likely to require verifiable correctness guarantees, especially when outsourced. While the combination of methods for verifiability and privacy protection has clear benefits, certain challenges stand before their widespread practical adoption. In this work, we analyze existing solutions that combine verifiability with privacy-preserving computations over distributed data, in order to preserve confidentiality and guarantee correctness at the same time. We classify and compare 37 different schemes, regarding solution approach, security, efficiency, and practicality. Lastly, we discuss some of the most promising solutions in this regard, and present various open challenges and directions for future research.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Sometimes You Can’t Distribute Random-Oracle-Based Proofs**
  2023-09-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1381)
  Jack Doerner, Yashvanth Kondi, Leah Namisa Rosenbloom

  <details><summary>摘要 / Abstract</summary>

  We investigate the conditions under which straight-line extractable NIZKs in the random oracle model (i.e. without a CRS) permit multiparty realizations that are black-box in the same random oracle. We show that even in the semi-honest setting, any MPC protocol to compute such a NIZK cannot make black-box use of the random oracle or a hash function instantiating it if security against all-but-one corruptions is desired, unless the number of queries made by the verifier to the oracle grows linearly with the number of parties. This presents a fundamental barrier to constructing efficient protocols to securely distribute the computation of NIZKs (and signatures) based on MPC-in-the-head, PCPs/IOPs, and sigma protocols compiled with transformations due to Fischlin, Pass, or Unruh. When the adversary is restricted to corrupt only a constant fraction of parties, we give a positive result by means of a tailored construction, which demonstrates that our impossibility does not extend to weaker corruption models in general.

  匹配依据：MPC: mpc (context)

  </details>

- **Secure and Scalable Circuit-based Protocol for Multi-Party Private Set Intersection**
  2023-09-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.07406)
  Jiuheng Su, Zhili Chen

  <details><summary>摘要 / Abstract</summary>

  We propose a novel protocol for computing a circuit which implements the multi-party private set intersection functionality (PSI). Circuit-based approach has advantages over using custom protocols to achieve this task, since many applications of PSI do not require the computation of the intersection itself, but rather specific functional computations over the items in the intersection. Our protocol represents the pioneering circuit-based multi-party PSI protocol, which builds upon and optimizes the two-party SCS \cite{huang2012private} protocol. By using secure computation between two parties, our protocol sidesteps the complexities associated with multi-party interactions and demonstrates good scalability. In order to mitigate the high overhead associated with circuit-based constructions, we have further enhanced our protocol by utilizing simple hashing scheme and permutation-based hash functions. These tricks have enabled us to minimize circuit size by employing bucketing techniques while simultaneously attaining noteworthy reductions in both computation and communication expenses.

  匹配依据：MPC: private set intersection, secure computation

  </details>

- **On Weighted-Sum Orthogonal Latin Squares and Secret Sharing**
  2023-09-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1374)
  Koji Nuida, Tomoko Adachi

  <details><summary>摘要 / Abstract</summary>

  Latin squares are a classical and well-studied topic of discrete mathematics, and recently Takeuti and Adachi (IACR ePrint, 2023) proposed (2,n)-threshold secret sharing based on mutually orthogonal Latin squares (MOLS). Hence efficient constructions of as large sets of MOLS as possible are also important from practical viewpoints. In this letter, we determine the maximum number of MOLS among a known class of Latin squares defined by weighted sums. We also mention some known property of Latin squares interpreted via the relation to secret sharing and a connection of Takeuti-Adachi&#x27;s scheme to Shamir&#x27;s secret sharing scheme.

  匹配依据：MPC: secret sharing

  </details>

- **On Ideal Secret-Sharing Schemes for $k$-homogeneous access structures**
  2023-09-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.07479)
  Younjin Kim, Jihye Kwon, Hyang-Sook Lee

  <details><summary>摘要 / Abstract</summary>

  A $k$-uniform hypergraph is a hypergraph where each $k$-hyperedge has exactly $k$ vertices. A $k$-homogeneous access structure is represented by a $k$-uniform hypergraph $\mathcal{H}$, in which the participants correspond to the vertices of hypergraph $\mathcal{H}$. A set of vertices can reconstruct the secret value from their shares if they are connected by a $k$-hyperedge, while a set of non-adjacent vertices does not obtain any information about the secret. One parameter for measuring the efficiency of a secret sharing scheme is the information rate, defined as the ratio between the length of the secret and the maximum length of the shares given to the participants. Secret sharing schemes with an information rate equal to one are called ideal secret sharing schemes. An access structure is considered ideal if an ideal secret sharing scheme can realize it. Characterizing ideal access structures is one of the important problems in secret sharing schemes. The characterization of ideal access structures has been studied by many authors~\cite{BD, CT,JZB, FP1,FP2,DS1,TD}. In this paper, we characterize ideal $k$-homogeneous access structures using the independent sequence method. In particular, we prove that the reduced access structure of $Γ$ is an $(k, n)$-threshold access structure when the optimal information rate of $Γ$ is larger than $\frac{k-1}{k}$, where $Γ$ is a $k$-homogeneous access structure satisfying specific criteria.

  匹配依据：MPC: secret sharing

  </details>

- **Advisor-Verifier-Prover Games and the Hardness of Information Theoretic Cryptography**
  2023-09-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1378)
  Benny Applebaum, Oded Nir

  <details><summary>摘要 / Abstract</summary>

  A major open problem in information-theoretic cryptography is to obtain a super-polynomial lower bound for the communication complexity of basic cryptographic tasks. This question is wide open even for very powerful non-interactive primitives such as private information retrieval (or locally-decodable codes), general secret sharing schemes, conditional disclosure of secrets, and fully-decomposable randomized encoding (or garbling schemes). In fact, for all these primitives we do not even have super-linear lower bounds. Furthermore, it is unknown how to relate these questions to each other or to other complexity-theoretic questions. In this note, we relate all these questions to the classical topic of query/space trade-offs, lifted to the setting of interactive proof systems. Specifically, we consider the following Advisor-Verifier-Prover (AVP) game: First, a function $f$ is given to the advisor who computes an advice $a$. Next, an input $x$ is given to the verifier and to the prover who claims that $f(x)=1$. The verifier should check this claim via a single round of interaction based on the private advice $a$ and without having any additional information on $f$. We focus on the case where the prover is laconic and communicates only a constant number of bits, and, mostly restrict the attention to the simplest, purely information-theoretic setting, where all parties are allowed to be computationally unbounded. The goal is to minimize the total communication complexity which is dominated by the length of the advice plus the length of the verifier&#x27;s query. As our main result, we show that a super-polynomial lower bound for AVPs implies a super-polynomial lower bound for a wide range of information-theoretic cryptographic tasks. In particular, we present a communication-efficient transformation from any of the above primitives into an AVP protocol. Interestingly, each primitive induces some additional property over the resulting protocol. Thus AVP games form a new common yardstick that highlights the differences between all the above primitives. Equipped with this view, we revisit the existing (somewhat weak) lower bounds for the above primitives, and show that many of these lower bounds can be unified by proving a single counting-based lower bound on the communication of AVPs, whereas some techniques are inherently limited to specific domains. The latter is shown by proving the first polynomial separations between the complexity of secret-sharing schemes and conditional disclosure of secrets and between the complexity of randomized encodings and conditional disclosure of secrets.

  匹配依据：MPC: garbling schemes, secret sharing

  </details>

- **Ramp hyper-invertible matrices and their applications to MPC protocols**
  2023-09-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1369)
  Hongqing Liu, Chaoping Xing, Yanjiang Yang, Chen Yuan

  <details><summary>摘要 / Abstract</summary>

  Beerliová-Trubíniová and Hirt introduced hyper-invertible matrix technique to construct the first perfectly secure MPC protocol in the presence of maximal malicious corruptions $\lfloor \frac{n-1}{3} \rfloor$ with linear communication complexity per multiplication gate [5]. This matrix allows MPC protocol to generate correct shares of uniformly random secrets in the presence of malicious adversary. Moreover, the amortized communication complexity of generating each sharing is linear. Due to this prominent feature, the hyper-invertible matrix plays an important role in the construction of MPC protocol and zero-knowledge proof protocol where the randomness needs to be jointly generated. However, the downside of this matrix is that the size of its base field is linear in the size of its matrix. This means if we construct an $n$-party MPC protocol over $\mathbb{F}_q$ via hyper-invertible matrix, $q$ is at least $2n$. In this paper, we propose the ramp hyper-invertible matrix which can be seen as the generalization of hyper-invertible matrix. Our ramp hyper-invertible matrix can be defined over constant-size field regardless of the size of this matrix. Similar to the arithmetic secret sharing scheme, to apply our ramp hyper-invertible matrix to perfectly secure MPC protocol, the maximum number of corruptions has to be compromised to $\frac{(1-\epsilon)n}{3}$. As a consequence, we present the first perfectly secure MPC protocol in the presence of $\frac{(1-\epsilon)n}{3}$ malicious corruptions with constant communication complexity. Besides presenting the variant of hyper-invertible matrix, we overcome several obstacles in the construction of this MPC protocol. Our arithmetic secret sharing scheme over constant-size field is compatible with the player elimination technique, i.e., it supports the dynamic changes of party number and corrupted party number. Moreover, we rewrite the public reconstruction protocol to support the sharings over constant-size field. Putting these together leads to the constant-size field variant of celebrated MPC protocol in [5]. We note that although it was widely acknowledged that there exists an MPC protocol with constant communication complexity by replacing Shamir secret sharing scheme with arithmetic secret sharing scheme, there is no reference seriously describing such protocol in detail. Our work fills the missing detail by providing MPC primitive for any applications relying on MPC protocol of constant communication complexity. As an application of our perfectly secure MPC protocol which implies perfect robustness in the MPC-in-the-Head framework, we present the constant-rate zero-knowledge proof with $3$ communication rounds. The previous work achieves constant-rate with $5$ communication rounds [32] due to the statistical robustness of their MPC protocol. Another application of our ramp hyper-invertible matrix is the information-theoretic multi-verifier zero-knowledge for circuit satisfiability[43]. We manage to remove the dependence of the size of circuit and security parameter from the share size.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Engineered Value Decomposition Networks for Cooperative Multi-Agent Reinforcement Learning**
  2023-09-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2311.06255)
  Parham Gohari, Matthew Hale, Ufuk Topcu

  <details><summary>摘要 / Abstract</summary>

  In cooperative multi-agent reinforcement learning (Co-MARL), a team of agents must jointly optimize the team&#x27;s long-term rewards to learn a designated task. Optimizing rewards as a team often requires inter-agent communication and data sharing, leading to potential privacy implications. We assume privacy considerations prohibit the agents from sharing their environment interaction data. Accordingly, we propose Privacy-Engineered Value Decomposition Networks (PE-VDN), a Co-MARL algorithm that models multi-agent coordination while provably safeguarding the confidentiality of the agents&#x27; environment interaction data. We integrate three privacy-engineering techniques to redesign the data flows of the VDN algorithm, an existing Co-MARL algorithm that consolidates the agents&#x27; environment interaction data to train a central controller that models multi-agent coordination, and develop PE-VDN. In the first technique, we design a distributed computation scheme that eliminates Vanilla VDN&#x27;s dependency on sharing environment interaction data. Then, we utilize a privacy-preserving multi-party computation protocol to guarantee that the data flows of the distributed computation scheme do not pose new privacy risks. Finally, we enforce differential privacy to preempt inference threats against the agents&#x27; training data, past environment interactions, when they take actions based on their neural network predictions. We implement PE-VDN in StarCraft Multi-Agent Competition (SMAC) and show that it achieves 80% of Vanilla VDN&#x27;s win rate while maintaining differential privacy levels that provide meaningful privacy guarantees. The results demonstrate that PE-VDN can safeguard the confidentiality of agents&#x27; environment interaction data without sacrificing multi-agent coordination.

  匹配依据：MPC: multi party computation

  </details>

- **Quantum multi-secret sharing scheme with access structures and cheat identification**
  2023-09-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.06458)
  Deepa Rathi, Sanjeev Kumar

  <details><summary>摘要 / Abstract</summary>

  This work proposes a $d$-dimensional quantum multi-secret sharing scheme with a cheat detection mechanism. The dealer creates multiple secrets and distributes the shares of these secrets using multi-access structures and a monotone span program. The dealer detects the cheating of each participant using the Black box&#x27;s cheat detection mechanism. To detect the participants&#x27; deceit, the dealer distributes secret shares&#x27; shadows derived from a randomly invertible matrix $X$ to the participants, stored in the black box. The Black box identifies the participant&#x27;s deceitful behavior during the secret recovery phase. Only honest participants authenticated by the Black box acquire their secret shares to recover the multiple secrets. After the Black box cheating verification, the participants reconstruct the secrets by utilizing the unitary operations and quantum Fourier transform. The proposed protocol is reliable in preventing attacks from eavesdroppers and participants. The scheme&#x27;s efficiency is demonstrated in different noise environments: dit-flip noise, $d$-phase-flip noise, and amplitude-damping noise, indicating its robustness in practical scenarios. The proposed protocol provides greater versatility, security, and practicality.

  匹配依据：MPC: secret sharing

  </details>

- **Practical Constructions for Single Input Functionality against a Dishonest Majority**
  2023-09-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1367)
  Zhelei Zhou, Bingsheng Zhang, Hong-Sheng Zhou, Kui Ren

  <details><summary>摘要 / Abstract</summary>

  Single Input Functionality (SIF) is a special case of MPC, where only one distinguished party called dealer holds the secret input. SIF allows the dealer to complete a computation task and send to other parties their respective outputs without revealing any additional information about its secret input. SIF has many applications, including multiple-verifier zero-knowledge and verifiable relation sharing, etc. Recently, several works devote to round-efficient realization of SIF, and achieve 2-round communication in the honest majority setting (Applebaum et al., Crypto 2022; Baum et al., CCS 2022; Yang and Wang, Asiacrypt 2022). In this work, we focus on concrete efficiency and propose \emph{the first} practical construction for SIF against \emph{a dishonest majority} in the preprocessing model; moreover, the online phase of our protocol is only 2-round and is highly efficient, as it requires no cryptographic operations and achieves information theoretical security. For SIF among 5 parties, our scheme takes 152.34ms (total) to evaluate an AES-128 circuit with 7.36ms online time. Compared to the state-of-the-art (honest majority) solution (Baum et al., CCS 2022), our protocol is roughly 2$\times$ faster in the online phase, although more preprocessing time is needed. Compared to the state-of-the-art generic MPC against a dishonest majority (Wang et al., CCS 2017; Cramer et al., Crypto 2018), our protocol outperforms them with respect to both total running time and online running time.

  匹配依据：MPC: mpc (context)

  </details>

- **Amortized NISC over $\\mathbb{Z}\_{2^k}$ from RMFE**
  2023-09-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1363)
  Fuchun Lin, Chaoping Xing, Yizhou Yao, Chen Yuan

  <details><summary>摘要 / Abstract</summary>

  Reversed multiplication friendly embedding (RMFE) amortization has been playing an active role in the state-of-the-art constructions of MPC protocols over rings (in particular, the ring $\mathbb{Z}_{2^k}$). As far as we know, this powerful technique has NOT been able to find applications in the crown jewel of two-party computation, the non-interactive secure computation (NISC), where the requirement of the protocol being non-interactive constitutes a formidable technical bottle-neck. We initiate such a study focusing on statistical NISC protocols in the VOLE-hybrid model. Our study begins with making the {\em decomposable affine randomized encoding (DARE)} based semi-honest NISC protocol compatible with RMFE techniques, which together with known techniques for forcing a malicious sender Sam to honestly follow DARE already yield a secure amortized protocol, assuming both parties follow RMFE encoding. Achieving statistical security in the full malicious setting is much more challenging, as applying known techniques for enforcing compliance with RMFE incurs interaction. To solve this problem, we put forward a new notion dubbed non-malleable RMFE (NM-RMFE), which is a randomized RMFE such that, once one party deviates from the encoding specification, the randomness injected by the other party will randomize the output, preventing information from being leaked. NM-RMFE simultaneously forces both parties to follow RMFE encoding, offering a desired {\em non-interactive} solution to amortizing NISC. We believe that NM-RMFE is on its own an important primitive that has applications in secure computation and beyond, interactive and non-interactive alike. With an asymptotically good instantiation of our NM-RMFE, we obtain the first {\em statistical} reusable NISC protocols in the VOLE-hybrid model with {\em constant communication overhead} for arithmetic branching programs over $\mathbb{Z}_{2^k}$. As side contributions, we consider computational security and present two concretely efficient NISC constructions in the random oracle model from conventional RMFEs.

  匹配依据：MPC: secure computation, two party computation

  </details>

- **On the Security of KZG Commitment for VSS**
  2023-09-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1350)
  Atsuki Momose, Sourav Das, Ling Ren

  <details><summary>摘要 / Abstract</summary>

  The constant-sized polynomial commitment scheme by Kate, Zaverucha, and Goldberg (Asiscrypt 2010), also known as the KZG commitment, is an essential component in designing bandwidth-efficient verifiable secret-sharing (VSS) protocols. We point out, however, that the KZG commitment is missing two important properties that are crucial for VSS protocols. First, the KZG commitment has not been proven to be degree binding in the standard adversary model without idealized group assumptions. In other words, the committed polynomial is not guaranteed to have the claimed degree, which is supposed to be the reconstruction threshold of VSS. Without this property, shareholders in VSS may end up reconstructing different secrets depending on which shares are used. Second, the KZG commitment does not support polynomials with different degrees at once with a single setup. If the reconstruction threshold of the underlying VSS protocol changes, the protocol must redo the setup, which involves an expensive multi-party computation known as the powers of tau setup. In this work, we augment the KZG commitment to address both of these limitations. Our scheme is degree-binding in the standard model under the strong Diffie-Hellman (SDH) assumption. It supports any degree $0 &lt; d \le m$ under a powers-of-tau common reference string with $m+1$ group elements generated by a one-time setup.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Approximating ReLU on a Reduced Ring for Efficient MPC-based Private Inference**
  2023-09-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.04875)
  Kiwan Maeng, G. Edward Suh

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) allows users to offload machine learning inference on untrusted servers without having to share their privacy-sensitive data. Despite their strong security properties, MPC-based private inference has not been widely adopted in the real world due to their high communication overhead. When evaluating ReLU layers, MPC protocols incur a significant amount of communication between the parties, making the end-to-end execution time multiple orders slower than its non-private counterpart. This paper presents HummingBird, an MPC framework that reduces the ReLU communication overhead significantly by using only a subset of the bits to evaluate ReLU on a smaller ring. Based on theoretical analyses, HummingBird identifies bits in the secret share that are not crucial for accuracy and excludes them during ReLU evaluation to reduce communication. With its efficient search engine, HummingBird discards 87--91% of the bits during ReLU and still maintains high accuracy. On a real MPC setup involving multiple servers, HummingBird achieves on average 2.03--2.67x end-to-end speedup without introducing any errors, and up to 8.64x average speedup when some amount of accuracy degradation can be tolerated, due to its up to 8.76x communication reduction.

  匹配依据：MPC: secure multi party computation

  </details>

- **Adaptively Secure (Aggregatable) PVSS and Application to Distributed Randomness Beacons**
  2023-09-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1348)
  Renas Bacho, Julian Loss

  <details><summary>摘要 / Abstract</summary>

  Publicly Verifiable Secret Sharing (PVSS) is a fundamental primitive that allows to share a secret $S$ among $n$ parties via a publicly verifiable transcript $T$. Existing (efficient) PVSS are only proven secure against static adversaries who must choose who to corrupt ahead of a protocol execution. As a result, any protocol (e.g., a distributed randomness beacon) that builds on top of such a PVSS scheme inherits this limitation. To overcome this barrier, we revisit the security of PVSS under adaptive corruptions and show that, surprisingly, many protocols from the literature already achieve it in a meaningful way: - We propose a new security definition for aggregatable PVSS, i.e., schemes that allow to homomorphically combine multiple transcripts into one compact aggregate transcript $AT$ that shares the sum of their individual secrets. Our notion captures that if the secret shared by $AT$ contains at least one contribution from an honestly generated transcript, it should not be predictable. We then prove that several existing schemes satisfy this notion against adaptive corruptions in the algebraic group model. - To motivate our new notion, we show that it implies the adaptive security of two recent random beacon protocols, SPURT (S&amp;P &#x27;22) and OptRand (NDSS &#x27;23), who build on top of aggregatable PVSS schemes satisfying our notion of unpredictability. For a security parameter $\lambda$, our result improves the communication complexity of the best known adaptively secure random beacon protocols to $O(\lambda n^2)$ for synchronous networks with $t&lt;n/2$ corruptions and partially synchronous networks with $t&lt;n/3$ corruptions.

  匹配依据：MPC: secret sharing

  </details>

- **Universally Composable Auditable Surveillance**
  2023-09-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1343)
  Valerie Fetzer, Michael Klooß, Jörn Müller-Quade, Markus Raiber, Andy Rupp

  <details><summary>摘要 / Abstract</summary>

  User privacy is becoming increasingly important in our digital society. Yet, many applications face legal requirements or regulations that prohibit unconditional anonymity guarantees, e.g., in electronic payments where surveillance is mandated to investigate suspected crimes. As a result, many systems have no effective privacy protections at all, or have backdoors, e.g., stored at the operator side of the system, that can be used by authorities to disclose a user’s private information (e.g., lawful interception). The problem with such backdoors is that they also enable silent mass surveillance within the system. To prevent such misuse, various approaches have been suggested which limit possible abuse or ensure it can be detected. Many works consider auditability of surveillance actions but do not enforce that traces are left when backdoors are retrieved. A notable exception which offers retrospective and silent surveillance is the recent work on misuse-resistant surveillance by Green et al. (EUROCRYPT’21). However, their approach relies on extractable witness encryption, which is a very strong primitive with no known efficient and secure implementations. In this work, we develop a building block for auditable surveillance. In our protocol, backdoors or escrow secrets of users are protected in multiple ways: (1) Backdoors are short-term and user-specific; (2) they are shared between trustworthy parties to avoid a single point of failure; and (3) backdoor access is given conditionally. Moreover (4) there are audit trails and public statistics for every (granted) backdoor request; and (5) surveillance remains silent, i.e., users do not know they are surveilled. Concretely, we present an abstract UC-functionality which can be used to augment applications with auditable surveillance capabilities. Our realization makes use of threshold encryption to protect user secrets, and is concretely built in a blockchain context with committee-based YOSO MPC. As a consequence, the committee can verify that the conditions for backdoor access are given, e.g., that law enforcement is in possession of a valid surveillance warrant (via a zero-knowledge proof). Moreover, access leaves an audit trail on the ledger, which allows an auditor to retrospectively examine surveillance decisions. As a toy example, we present an Auditably Sender-Traceable Encryption scheme, a PKE scheme where the sender can be deanonymized by law enforcement. We observe and solve problems posed by retrospective surveillance via a special non-interactive non-committing encryption scheme which allows zero-knowledge proofs over message, sender identity and (escrow) secrets.

  匹配依据：MPC: mpc (context)

  </details>

- **Experimenting with Zero-Knowledge Proofs of Training**
  2023-09-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1345)
  Sanjam Garg, Aarushi Goel, Somesh Jha, Saeed Mahloujifar, Mohammad Mahmoody, Guru-Vamsi Policharla, Mingyuan Wang

  <details><summary>摘要 / Abstract</summary>

  How can a model owner prove they trained their model according to the correct specification? More importantly, how can they do so while preserving the privacy of the underlying dataset and the final model? We study this problem and formulate the notion of zero-knowledge proof of training (zkPoT), which formalizes rigorous security guarantees that should be achieved by a privacy-preserving proof of training. While it is theoretically possible to design zkPoT for any model using generic zero-knowledge proof systems, this approach results in extremely unpractical proof generation times. Towards designing a practical solution, we propose the idea of combining techniques from MPC-in-the-head and zkSNARKs literature to strike an appropriate trade-off between proof size and proof computation time. We instantiate this idea and propose a concretely efficient, novel zkPoT protocol for logistic regression. Crucially, our protocol is streaming-friendly and does not require RAM proportional to the size of the circuit being trained and, hence, can be adapted to the requirements of available hardware. We expect the techniques developed in this paper to also generally be useful for designing efficient zkPoT protocols for other relatively more sophisticated ML models. We implemented and benchmarked prover/verifier runtimes and proof sizes for training a logistic regression model using mini-batch gradient descent on a 4~GB dataset of 262,144 records with 1024 features. We divide our protocol into three phases: (1) data-independent offline phase (2) data-dependent phase that is independent of the model (3) online phase that depends both on the data and the model. The total proof size (across all three phases) is less than $10\%$ of the data set size ($&lt;350$~MB). In the online phase, the prover and verifier times are under 10 minutes and half a minute respectively, whereas in the data-dependent phase, they are close to one hour and a few seconds respectively.

  匹配依据：MPC: mpc (context)

  </details>

- **Private Membership Aggregation**
  2023-09-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.03872)
  Mohamed Nomeir, Sajani Vithana, Sennur Ulukus

  <details><summary>摘要 / Abstract</summary>

  We consider the problem of private membership aggregation (PMA), in which a user counts the number of times a certain element is stored in a system of independent parties that store arbitrary sets of elements from a universal alphabet. The parties are not allowed to learn which element is being counted by the user. Further, neither the user nor the other parties are allowed to learn the stored elements of each party involved in the process. PMA is a generalization of the recently introduced problem of $K$ private set intersection ($K$-PSI). The $K$-PSI problem considers a set of $M$ parties storing arbitrary sets of elements, and a user who wants to determine if a certain element is repeated at least at $K$ parties out of the $M$ parties without learning which party has the required element and which party does not. To solve the general problem of PMA, we dissect it into four categories based on the privacy requirement and the collusions among databases/parties. We map these problems into equivalent private information retrieval (PIR) problems. We propose achievable schemes for each of the four variants of the problem based on the concept of cross-subspace alignment (CSA). The proposed schemes achieve \emph{linear} communication complexity as opposed to the state-of-the-art $K$-PSI scheme that requires \emph{exponential} complexity even though our PMA problems contain more security and privacy constraints.

  匹配依据：MPC: private set intersection

  </details>

- **Abuse-Resistant Location Tracking: Balancing Privacy and Safety in the Offline Finding Ecosystem**
  2023-09-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1332)
  Harry Eldridge, Gabrielle Beck, Matthew Green, Nadia Heninger, Abhishek Jain

  <details><summary>摘要 / Abstract</summary>

  Location tracking accessories (or &quot;tracking tags&quot;) such as those sold by Apple, Samsung, and Tile, allow owners to track the location of their property via offline finding networks. The tracking protocols were designed to ensure that no entity (including the vendor) can use a tag&#x27;s broadcasts to surveil its owner. These privacy guarantees, however, seem to be at odds with the phenomenon of $\textit{tracker-based stalking}$, where attackers use these very tags to monitor a target&#x27;s movements. Numerous such criminal incidents have been reported, and in response, manufacturers have chosen to substantially weaken privacy guarantees in order to allow users to detect stalker tags. This compromise has been adopted in a recent IETF draft jointly proposed by Apple and Google. We put forth the notion of $\textit{abuse-resistant offline finding protocols}$ that aim to achieve a better balance between user privacy and stalker detection. We present an efficient protocol that achieves stalker detection under realistic conditions without sacrificing honest user privacy. At the heart of our result, and of independent interest, is a new notion of $\textit{multi-dealer secret sharing}$ which strengthens standard secret sharing with novel privacy and correctness guarantees. We show that this primitive can be instantiated efficiently on edge devices using variants of Interleaved Reed-Solomon codes combined with new lattice-based decoding algorithms.

  匹配依据：MPC: secret sharing

  </details>

- **Hide and Seek (HaS): A Lightweight Framework for Prompt Privacy Protection**
  2023-09-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.03057)
  Yu Chen, Tingxin Li, Huiming Liu, Yang Yu

  <details><summary>摘要 / Abstract</summary>

  Numerous companies have started offering services based on large language models (LLM), such as ChatGPT, which inevitably raises privacy concerns as users&#x27; prompts are exposed to the model provider. Previous research on secure reasoning using multi-party computation (MPC) has proven to be impractical for LLM applications due to its time-consuming and communication-intensive nature. While lightweight anonymization techniques can protect private information in prompts through substitution or masking, they fail to recover sensitive data replaced in the LLM-generated results. In this paper, we expand the application scenarios of anonymization techniques by training a small local model to de-anonymize the LLM&#x27;s returned results with minimal computational overhead. We introduce the HaS framework, where &quot;H(ide)&quot; and &quot;S(eek)&quot; represent its two core processes: hiding private entities for anonymization and seeking private entities for de-anonymization, respectively. To quantitatively assess HaS&#x27;s privacy protection performance, we propose both black-box and white-box adversarial models. Furthermore, we conduct experiments to evaluate HaS&#x27;s usability in translation and classification tasks. The experimental findings demonstrate that the HaS framework achieves an optimal balance between privacy protection and utility.

  匹配依据：MPC: multi party computation

  </details>

- **Manifesting Unobtainable Secrets: Threshold Elliptic Curve Key Generation using Nested Shamir Secret Sharing**
  2023-09-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.00915)
  J. L. Hall, Y. Hertzog, M. Loewy, M. P. Skerritt, D. Valladolid, G. Verma

  <details><summary>摘要 / Abstract</summary>

  We present a mechanism to manifest unobtainable secrets using a nested Shamir secret sharing scheme to create public/private key pairs for elliptic curves. A threshold secret sharing scheme can be used as a decentralised trust mechanism with applications in identity validation, message decryption, and agreement empowerment. Decentralising trust means that there is no single point vulnerability which could enable compromise of a system. Our primary interest is in twisted Edwards curves as used in EdDSA, and the related Diffie-Hellman key-exchange algorithms. The key generation is also decentralised, so can be used as a decentralised secret RNG suitable for use in other algorithms. The algorithms presented could be used to fill a ``[TBS]&#x27;&#x27; in the draft IETF specification ``Threshold modes in elliptic curves&#x27;&#x27; published in 2020 and updated in 2022.

  匹配依据：MPC: secret sharing

  </details>

- **Constant-Round Private Decision Tree Evaluation for Secret Shared Data**
  2023-09-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1307)
  Nan Cheng, Naman Gupta, Aikaterini Mitrokotsa, Hiraku Morita, Kazunari Tozawa

  <details><summary>摘要 / Abstract</summary>

  Decision tree evaluation is extensively used in machine learning to construct accurate classification models. Often in the cloud-assisted communication paradigm cloud servers execute remote evaluations of classification models using clients’ data. In this setting, the need for private decision tree evaluation (PDTE) has emerged to guarantee no leakage of information for the client’s input nor the service provider’s trained model i.e., decision tree. In this paper, we propose a private decision tree evaluation protocol based on the three-party replicated secret sharing (RSS) scheme. This enables us to securely classify inputs without any leakage of the provided input or the trained decision tree model. Our protocol only requires constant rounds of communication among servers, which is useful in a network with longer delays. Ma et al. (NDSS 2021) presented a lightweight PDTE protocol with sublinear communication cost with linear round complexity in the size of the input data. This protocol works well in the low latency network such as LAN while its total execution time is unfavourably increased in the WAN setting. In contrast, Tsuchida et al. (ProvSec 2020) constructed a constant round PDTE protocol at the cost of communication complexity, which works well in the WAN setting. Although their construction still requires 25 rounds, it showed a possible direction on how to make constant round PDTE protocols. Ji et al. (IEEE Transactions on Dependable and Secure Computing) presented a simplified PDTE with constant rounds using the function secret sharing (FSS) at the cost of communication complexity. Our proposed protocol only requires five rounds among the employed three servers executing secret sharing schemes, which is comparable to previously proposed protocols that are based on garbled circuits and homomorphic encryption. To further demonstrate the efficiency of our protocol, we evaluated it using real-world classification datasets. The evaluation results indicate that our protocol provides better concrete performance in the WAN setting that has a large network delay.

  匹配依据：MPC: garbled circuits, secret sharing, secure computing

  </details>

- **Towards Minimizing Non-linearity in Type-II Generalized Feistel Networks**
  2023-08-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1295)
  Yuqing Zhao, Chun Guo, Weijia Wang

  <details><summary>摘要 / Abstract</summary>

  Recent works have revisited blockcipher structures to achieve MPC- and ZKP-friendly designs. In particular, Albrecht et al. (EUROCRYPT 2015) first pioneered using a novel structure SP networks with partial non-linear layers (P-SPNs) and then (ESORICS 2019) repopularized using multi-line generalized Feistel networks (GFNs). In this paper, we persist in exploring symmetric cryptographic constructions that are conducive to the applications such as MPC. In order to study the minimization of non-linearity in Type-II Generalized Feistel Networks, we generalize the (extended) GFN by replacing the bit-wise shuffle in a GFN with the stronger linear layer in P-SPN and introducing the key in each round. We call this scheme Generalized Extended Generalized Feistel Network (GEGFN). When the block-functions (or S-boxes) are public random permutations or (domain-preserving) functions, we prove CCA security for the 5-round GEGFN. Our results also hold when the block-functions are over the prime fields F_p, yielding blockcipher constructions over (F_p)^*.

  匹配依据：MPC: mpc (context)

  </details>

- **PrivMail: A Privacy-Preserving Framework for Secure Emails**
  2023-08-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1294)
  Gowri R Chandran, Raine Nieminen, Thomas Schneider, Ajith Suresh

  <details><summary>摘要 / Abstract</summary>

  Emails have improved our workplace efficiency and communication. However, they are often processed unencrypted by mail servers, leaving them open to data breaches on a single service provider. Public-key based solutions for end-to-end secured email, such as Pretty Good Privacy (PGP) and Secure/Multipurpose Internet Mail Extensions (S/MIME), are available but are not widely adopted due to usability obstacles and also hinder processing of encrypted emails. We propose PrivMail, a novel approach to secure emails using secret sharing methods. Our framework utilizes Secure Multi-Party Computation techniques to relay emails through multiple service providers, thereby preventing any of them from accessing the content in plaintext. Additionally, PrivMail supports private server-side email processing similar to IMAP SEARCH, and eliminates the need for cryptographic certificates, resulting in better usability than public-key based solutions. An important aspect of our framework is its capability to enable third-party searches on user emails while maintaining the privacy of both the email and the query used to conduct the search. We integrate PrivMail into the current email infrastructure and provide a Thunderbird plugin to enhance user-friendliness. To evaluate our solution, we benchmarked transfer and search operations using the Enron Email Dataset and demonstrate that PrivMail is an effective solution for enhancing email security.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **FedChain: An Efficient and Secure Consensus Protocol based on Proof of Useful Federated Learning for Blockchain**
  2023-08-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.15095)
  Peiran Wang

  <details><summary>摘要 / Abstract</summary>

  Blockchain has become a popular decentralized paradigm for various applications in the zero-trust environment. The core of the blockchain is the consensus protocol, which establishes consensus among all the participants. PoW (Proof-of-Work) is one of the most popular consensus protocols. However, the PoW consensus protocol which incentives the participants to use their computing power to solve a meaningless hash puzzle is continuously questioned as energy-wasting. To address these issues, we propose an efficient and secure consensus protocol based on proof of useful federated learning for blockchain (called FedChain). We first propose a secure and robust blockchain architecture that takes federated learning tasks as proof of work. Then a pool aggregation mechanism is integrated to improve the efficiency of the FedChain architecture. To protect model parameter privacy for each participant within a mining pool, a secret sharing-based ring-all reduce architecture is designed. We also introduce a data distribution-based federated learning model optimization algorithm to improve the model performance of FedChain. At last, a zero-knowledge proof-based federated learning model verification is introduced to preserve the privacy of federated learning participants while proving the model performance of federated learning participants. Our approach has been tested and validated through extensive experiments, demonstrating its performance.

  匹配依据：MPC: secret sharing

  </details>

- **Advancement on Security Applications of Private Intersection Sum Protocol**
  2023-08-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.14741)
  Yuvaraj Athur Raghuvir, Senthil Govindarajan, Sanjeevi Vijayakumar, Pradeep Yadlapalli, Fabio Di Troia

  <details><summary>摘要 / Abstract</summary>

  Secure computation protocols combine inputs from involved parties to generate an output while keeping their inputs private. Private Set Intersection (PSI) is a secure computation protocol that allows two parties, who each hold a set of items, to learn the intersection of their sets without revealing anything else about the items. Private Intersection Sum (PIS) extends PSI when the two parties want to learn the cardinality of the intersection, as well as the sum of the associated integer values for each identifier in the intersection, but nothing more. Finally, Private Join and Compute (PJC) is a scalable extension of PIS protocol to help organizations work together with confidential data sets. The extensions proposed in this paper include: (a) extending PJC protocol to additional data columns and applying columnar aggregation based on supported homomorphic operations, (b) exploring Ring Learning with Errors (RLWE) homomorphic encryption schemes to apply arithmetic operations such as sum and sum of squares, (c) ensuring stronger security using mutual authentication of communicating parties using certificates, and (d) developing a Website to operationalize such a service offering. We applied our results to develop a Proof-of-Concept solution called JingBing, a voter list validation service that allows different states to register, acquire secure communication modules, install it, and then conduct authenticated peer-to-peer communication. We conclude our paper with directions for future research to make such a solution scalable for practical real-life scenarios.

  匹配依据：MPC: private set intersection, secure computation

  </details>

- **Falcon: Accelerating Homomorphically Encrypted Convolutions for Efficient Private Mobile Network Inference**
  2023-08-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.13189)
  Tianshi Xu, Meng Li, Runsheng Wang, Ru Huang

  <details><summary>摘要 / Abstract</summary>

  Efficient networks, e.g., MobileNetV2, EfficientNet, etc, achieves state-of-the-art (SOTA) accuracy with lightweight computation. However, existing homomorphic encryption (HE)-based two-party computation (2PC) frameworks are not optimized for these networks and suffer from a high inference overhead. We observe the inefficiency mainly comes from the packing algorithm, which ignores the computation characteristics and the communication bottleneck of homomorphically encrypted depthwise convolutions. Therefore, in this paper, we propose Falcon, an effective dense packing algorithm for HE-based 2PC frameworks. Falcon features a zero-aware greedy packing algorithm and a communication-aware operator tiling strategy to improve the packing density for depthwise convolutions. Compared to SOTA HE-based 2PC frameworks, e.g., CrypTFlow2, Iron and Cheetah, Falcon achieves more than 15.6x, 5.1x and 1.8x latency reduction, respectively, at operator level. Meanwhile, at network level, Falcon allows for 1.4% and 4.2% accuracy improvement over Cheetah on CIFAR-100 and TinyImagenet datasets with iso-communication, respecitvely.

  匹配依据：MPC: two party computation

  </details>

- **A Univariate Attack against the Limited-Data Instance of Ciminion**
  2023-08-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1283)
  Augustin Bariant

  <details><summary>摘要 / Abstract</summary>

  With the increasing interest for advanced protocols for Multi Party Computation, Fully-Homomorphic Encryption or Zero Knowledge proofs, a need for cryptographic algorithms with new constraints has emerged. These algorithms, called Arithmetization-Oriented ciphers, seek to minimize the number of field multiplications in large finite fields $\mathbb{F}_{2^n}$ or $\mathbb{F}_{p}$. Among them, Ciminion is an encryption algorithm proposed by Dobraunig et al. in Eurocrypt 2021. In this paper, we show a new univariate modelization on a variant of Ciminion proposed by the designers. This instance restricts the attacker to at most $2^{s/2}$ data, where $s$ is the security level. Because the designers chose to reduce the number of rounds in that specific attacker model, we are able to attack the cipher for large security levels. We also propose some slight modifications of Ciminion that would overcome this vulnerability.

  匹配依据：MPC: multi party computation

  </details>

- **Analog Multi-Party Computing: Locally Differential Private Protocols for Collaborative Computations**
  2023-08-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.12544)
  Hsuan-Po Liu, Mahdi Soleymani, Hessam Mahdavifar

  <details><summary>摘要 / Abstract</summary>

  We consider a fully-decentralized scenario in which no central trusted entity exists and all clients are honest-but-curious. The state-of-the-art approaches to this problem often rely on cryptographic protocols, such as multiparty computation (MPC), that require mapping real-valued data to a discrete alphabet, specifically a finite field. These approaches, however, can result in substantial accuracy losses due to computation overflows. To address this issue, we propose A-MPC, a private analog MPC protocol that performs all computations in the analog domain. We characterize the privacy of individual datasets in terms of $(ε, δ)$-local differential privacy, where the privacy of a single record in each client&#x27;s dataset is guaranteed against other participants. In particular, we characterize the required noise variance in the Gaussian mechanism in terms of the required $(ε,δ)$-local differential privacy parameters by solving an optimization problem. Furthermore, compared with existing decentralized protocols, A-MPC keeps the privacy of individual datasets against the collusion of all other participants, thereby, in a notably significant improvement, increasing the maximum number of colluding clients tolerated in the protocol by a factor of three compared with the state-of-the-art collaborative learning protocols. Our experiments illustrate that the accuracy of the proposed $(ε,δ)$-locally differential private logistic regression and linear regression models trained in a fully-decentralized fashion using A-MPC closely follows that of a centralized one performed by a single trusted entity.

  匹配依据：MPC: multi party computing, multiparty computation

  </details>

- **Privacy-Preserving Detection Method for Transmission Line Based on Edge Collaboration**
  2023-08-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.08761)
  Quan Shi, Kaiyuan Deng

  <details><summary>摘要 / Abstract</summary>

  Unmanned aerial vehicles (UAVs) are commonly used for edge collaborative computing in current transmission line object detection, where computationally intensive tasks generated by user nodes are offloaded to more powerful edge servers for processing. However, performing edge collaborative processing on transmission line image data may result in serious privacy breaches. To address this issue, we propose a secure single-stage detection model called SecYOLOv7 that preserves the privacy of object detecting. Based on secure multi-party computation (MPC), a series of secure computing protocols are designed for the collaborative execution of Secure Feature Contraction, Secure Bounding-Box Prediction and Secure Object Classification by two non-edge servers. Performance evaluation shows that both computational and communication overhead in this framework as well as calculation error significantly outperform existing works.

  匹配依据：MPC: secure computing, secure multi party computation

  </details>

- **A novel hybrid protocol for semiquantum key distribution and semiquantum secret sharing**
  2023-08-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.08082)
  Tian-Yu Ye, Xiao Tan

  <details><summary>摘要 / Abstract</summary>

  In this paper, a novel hybrid protocol for semiquantum key distribution (SQKD) and semiquantum secret sharing (SQSS) was constructed by using GHZ-like states. This protocol is capable of establishing two different private keys between one quantum party and two semiquantum parties respectively, and making two semiquantum parties share another private key of the quantum party in the meanwhile. The usages of delay lines, Pauli operations, Hadamard gates and quantum entanglement swapping are not required. Moreover, the semiquantum parties are not necessary to be equipped with any quantum memory. We validate in detail that this protocol resists various attacks from Eve, including the Trojan horse attacks, the entangle-measure attack, the double controlled-not (CNOT) attacks, the measure-resend attack and the intercept-resend attack. To our best knowledge, this protocol is the only protocol which possesses the functions of both SQKD and SQSS simultaneously until now.

  匹配依据：MPC: secret sharing

  </details>

- **Practical Key-Extraction Attacks in Leading MPC Wallets**
  2023-08-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1234)
  Nikolaos Makriyannis, Oren Yomtov, Arik Galansky

  <details><summary>摘要 / Abstract</summary>

  Multi-Party Computation (MPC) has become a major tool for protecting hundreds of billions of dollars in cryptocurrency wallets. MPC protocols are currently powering the wallets of Coinbase, Binance, Zengo, BitGo, Fireblocks and many other fintech companies servicing thousands of financial institutions and hundreds of millions of end-user consumers. We present four novel key-extraction attacks on popular MPC signing protocols showing how a single corrupted party may extract the secret in full during the MPC signing process. Our attacks are highly practical (the practicality of the attack depends on the number of signature-generation ceremonies the attacker participates in before extracting the key). Namely, we show key-extraction attacks against different threshold-ECDSA protocols/implementations requiring $10^6$, $256$, $16$, and *one signature*, respectively. In addition, we provide proof-of-concept code that implements our attacks.

  匹配依据：MPC: multi party computation

  </details>

- **Reinforcing Security and Usability of Crypto-Wallet with Post-Quantum Cryptography and Zero-Knowledge Proof**
  2023-08-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.07309)
  Yathin Kethepalli, Rony Joseph, Sai Raja Vajrala, Jashwanth Vemula, Nenavath Srinivas Naik

  <details><summary>摘要 / Abstract</summary>

  Crypto-wallets or digital asset wallets are a crucial aspect of managing cryptocurrencies and other digital assets such as NFTs. However, these wallets are not immune to security threats, particularly from the growing risk of quantum computing. The use of traditional public-key cryptography systems in digital asset wallets makes them vulnerable to attacks from quantum computers, which may increase in the future. Moreover, current digital wallets require users to keep track of seed-phrases, which can be challenging and lead to additional security risks. To overcome these challenges, a new algorithm is proposed that uses post-quantum cryptography (PQC) and zero-knowledge proof (ZKP) to enhance the security of digital asset wallets. The research focuses on the use of the Lattice-based Threshold Secret Sharing Scheme (LTSSS), Kyber Algorithm for key generation and ZKP for wallet unlocking, providing a more secure and user-friendly alternative to seed-phrase, brain and multi-sig protocol wallets. This algorithm also includes several innovative security features such as recovery of wallets in case of downtime of the server, and the ability to rekey the private key associated with a specific username-password combination, offering improved security and usability. The incorporation of PQC and ZKP provides a robust and comprehensive framework for securing digital assets in the present and future. This research aims to address the security challenges faced by digital asset wallets and proposes practical solutions to ensure their safety in the era of quantum computing.

  匹配依据：MPC: secret sharing

  </details>

- **One-Message Secure Reductions: On the Cost of Converting Correlations**
  2023-08-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1225)
  Yuval Ishai, Mahimna Kelkar, Varun Narayanan, Liav Zafar

  <details><summary>摘要 / Abstract</summary>

  Correlated secret randomness is a useful resource for secure computation protocols, often enabling dramatic speedups compared to protocols in the plain model. This has motivated a line of work on identifying and securely generating useful correlations. Different kinds of correlations can vary greatly in terms of usefulness and ease of generation. While there has been major progress on efficiently generating oblivious transfer (OT) correlations, other useful kinds of correlations are much more costly to generate. Thus, it is highly desirable to develop efficient techniques for securely converting copies of a given source correlation into copies of a given target correlation, especially when the former are cheaper to generate than the latter. In this work, we initiate a systematic study of such conversions that only involve a single uni-directional message. We refer to such a conversion as a one-message secure reduction (OMSR). Recent works (Agarwal et al, Eurocrypt 2022; Khorasgani et al, Eurocrypt 2022) studied a similar problem when no communication is allowed; this setting is quite restrictive, however, with few non-trivial conversions being feasible. The OMSR setting substantially expands the scope of feasible results, allowing for direct applications to existing MPC protocols. We obtain the following positive and negative results. - OMSR constructions. We present a general rejection-sampling based technique for OMSR with OT source correlations. We apply it to substantially improve in the communication complexity of optimized protocols for distributed symmetric cryptography (Dinur et al., Crypto 2021). - OMSR lower bounds. We develop general techniques for proving lower bounds on the communication complexity of OMSR, matching our positive results up to small constant factors.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **A Note on “Secure Quantized Training for Deep Learning”**
  2023-08-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1219)
  Marcel Keller, Ke Sun

  <details><summary>摘要 / Abstract</summary>

  Keller and Sun (ICML&#x27;22) have found a gap in the accuracy between floating-point deep learning in cleartext and secure quantized deep learning using multi-party computation. We have discovered that this gap is caused by a bug in the implementation of max-pooling. In this note, we present updated figures to support this conclusion. We also add figures for another network on CIFAR-10.

  匹配依据：MPC: multi party computation

  </details>

- **Infinite families of minimal binary codes via Krawtchouk polynomials**
  2023-08-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1209)
  Xiaoni Du, René Rodríguez, Hao Wu

  <details><summary>摘要 / Abstract</summary>

  Linear codes play a crucial role in various fields of engineering and mathematics, including data storage, communication, cryptography, and combinatorics. Minimal linear codes, a subset of linear codes, are particularly essential for designing effective secret sharing schemes. In this paper, we introduce several classes of minimal binary linear codes by carefully selecting appropriate Boolean functions. These functions belong to a renowned class of Boolean functions, the general Maiorana-McFarland class. We employ a method first proposed by Ding et al. [7] to construct minimal codes violating the Ashikhmin-Barg bound (wide minimal codes) by using Krawtchouk polynomials. The lengths, dimensions, and weight distributions of the obtained codes are determined using the Walsh spectrum distribution of the chosen Boolean functions. Our findings demonstrate that a vast majority of the newly constructed codes are wide minimal codes. Furthermore, our proposed codes exhibit a significantly larger minimum distance, in some cases, compared to some existing similar constructions. Finally, we address this method, based on Krawtchouk polynomials, more generally, and highlight certain generic properties related to it. This study provides insights into the scope of this method.

  匹配依据：MPC: secret sharing

  </details>

- **A review on the questions of spin and spin quantum correlations in the relativistic regime**
  2023-08-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.05231)
  Shrobona Bagchi

  <details><summary>摘要 / Abstract</summary>

  The majority of current understanding of the quantum correlations is in the field of non-relativistic quantum mechanics. To develop quantum information and computation tasks fully, one must inevitably take into account the relativistic effects. In this regard, the spin is one of the central tools. For this purpose, it is of paramount importance to understand and characterize fully the theory of spin in relativistic quantum information theory where the spin states act as qubit. This area is still far from being resolved. As a result, this article will explore the recent studies of the concepts of the spin and spin quantum correlations in inertial frames and some apparent paradoxes regarding this concept. We will mainly focus on the problem of characterizing the spin, reduced spin density matrices and spin quantum correlations in inertial reference frames and the apparent paradoxes involved therein. Another important aspect is the use of tools of quantum field theory to extend several concepts in non-relativistic domain to relativistic one. In this regard, we analyze the development of the theory of relativistic secret sharing and a correlation measure namely the entanglement of purification.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-preserving edit distance computation using secret-sharing two-party computation**
  2023-08-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1201)
  Hernán Darío Vanegas Madrigal, Daniel Cabarcas Jaramillo, Diego F. Aranha

  <details><summary>摘要 / Abstract</summary>

  The edit distance is a metric widely used in genomics to measure the similarity of two DNA chains. Motivated by privacy concerns, we propose a 2PC protocol to compute the edit distance while preserving the privacy of the inputs. Since the edit distance algorithm can be expressed as a mixed-circuit computation, our approach uses protocols based on secret-sharing schemes like Tinier and SPD$\mathbb{Z}_{2^k}$; and also daBits to perform domain conversion and edaBits to perform arithmetic comparisons. We modify the Wagner-Fischer edit distance algorithm, aiming at reducing the number of rounds of the protocol, and achieve a flexible protocol with a trade-off between rounds and multiplications. We implement our proposal in the MP-SPDZ framework, and our experiments show that it reduces the execution time respectively by 81\% and 54\% for passive and active security with respect to a baseline implementation in a LAN. The experiments also show that our protocol reduces traffic by two orders of magnitude compared to a BMR-MASCOT implementation.

  匹配依据：MPC: secret sharing, two party computation

  </details>

- **On Fully-Secure Honest Majority MPC without $n^2$ Round Overhead**
  2023-08-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1204)
  Daniel Escudero, Serge Fehr

  <details><summary>摘要 / Abstract</summary>

  Fully secure multiparty computation (or guaranteed output delivery) among $n$ parties can be achieved with perfect security if the number of corruptions $t$ is less than $n/3$, or with statistical security with the help of a broadcast channel if $t&lt;n/2$. In the case of $t&lt;n/3$, it is known that it is possible to achieve linear communication complexity, but at a cost of having a round count of $\Omega(\mathsf{depth}(C) + n)$ in the worst case. The number of rounds can be reduced to $O(\mathsf{depth}(C))$ by either increasing communication, or assuming some correlated randomness (a setting also known as the preprocesing model). For $t&lt;n/2$ it is also known that linear communication complexity is achievable, but at the cost of $\Omega(\mathsf{depth}(C) + n^2)$ rounds, due to the use of a technique called dispute control. However, in contrast to the $t&lt;n/3$ setting, it is not known how to reduce this round count for $t&lt;n/2$ to $O(\mathsf{depth}(C))$, neither allowing for larger communication, or by using correlated randomness. In this work we make progress in this direction by taking the second route above: we present a fully secure protocol for $t&lt;n/2$ in the preprocessing model, that achieves linear communication complexity, and whose round complexity is only $O(\mathsf{depth}(C))$, without the additive $n^2$ term that appears from the use of dispute control. While on the $t&lt;n/3$ such result requires circuits of width $\Omega(n)$, in our case circuits must be of width $\Omega(n^2)$, leaving it as an interesting future problem to reduce this gap. Our $O(\mathsf{depth}(C))$ round count is achieved by avoiding the use of dispute control entirely, relying on a different tool for guaranteeing output. In the $t&lt;n/3$ setting when correlated randomness is available, this is done by using error correction to reconstruct secret-shared values, but in the $t&lt;n/2$ case the equivalent is robust secret-sharing, which guarantees the reconstruction of a secret in spite of errors. However, we note that a direct use of such tool would lead to \emph{quadratic} communication, stemming from the fact that each party needs to authenticate their share towards each other party. At the crux of our techniques lies a novel method for reconstructing a batch of robustly secret-shared values while involving only a linear amount of communication per secret, which may also be of independent interest.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Secure Computation over Encrypted Databases**
  2023-08-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.02878)
  Tikaram Sanyashi, Bernard Menezes

  <details><summary>摘要 / Abstract</summary>

  Sensitive applications running on the cloud often require data to be stored in an encrypted domain. To run data mining algorithms on such data, partially homomorphic encryption schemes (allowing certain operations in the ciphertext domain) have been devised. One such line of work yields schemes for secure \textit{k-nearest neighbors} computation that is designed to provide both \textit{Data Privacy} and \textit{Query Privacy}. Enhancements in this area further ensure that the data owner approves each query issued by a query user before the cloud server processes it. In this work, we describe an attack that invalidates the \textit{key confidentiality} claim, which further invalidates the \textit{Data Privacy} claim for these schemes. We show that a query user can specially tailor a query to extract information about the secret key used to encrypt the data points. Furthermore, the recovered secret information can be used to derive all the plaintext data points breaking \textit{data privacy}. We then suggest enhanced encryption schemes that make such attacks on \textit{data privacy} impossible while incurring meager additional costs in performance.

  匹配依据：MPC: secure computation

  </details>

- **Pure Gravitational Wave Estimation of Hubble's Constant using Neutron Star-Black Hole Mergers**
  2023-08-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.02440)
  Leo W. H. Fung, Tom Broadhurst, George F. Smoot

  <details><summary>摘要 / Abstract</summary>

  Here we show how $H_0$ can be derived purely from the gravitational waves (GW) of neutron star-black hole (NSBH) mergers. This new method provides an estimate of $H_0$ spanning the redshift range, $z&lt;0.25$ with current GW sensitivity and without the need for any afterglow detection. We utilise the inherently tight neutron star mass function together with the NSBH waveform amplitude and frequency to estimate distance and redshift respectively, thereby obtaining $H_0$ statistically. Our first estimate is $H_0 = 86^{+55}_{-46}$ km s$^{-1}$ Mpc$^{-1}$ for the secure NSBH events GW190426 and GW200115. We forecast that soon, with 10 more such NSBH events we can reach competitive precision of $δH_0/H_0 \lesssim 20\%$.

  匹配依据：MPC: mpc (context)

  </details>

- **Privacy Preserving In-memory Computing Engine**
  2023-08-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.02648)
  Haoran Geng, Jianqiao Mo, Dayane Reis, Jonathan Takeshita, Taeho Jung, Brandon Reagen, Michael Niemier, Xiaobo Sharon Hu

  <details><summary>摘要 / Abstract</summary>

  Privacy has rapidly become a major concern/design consideration. Homomorphic Encryption (HE) and Garbled Circuits (GC) are privacy-preserving techniques that support computations on encrypted data. HE and GC can complement each other, as HE is more efficient for linear operations, while GC is more effective for non-linear operations. Together, they enable complex computing tasks, such as machine learning, to be performed exactly on ciphertexts. However, HE and GC introduce two major bottlenecks: an elevated computational overhead and high data transfer costs. This paper presents PPIMCE, an in-memory computing (IMC) fabric designed to mitigate both computational overhead and data transfer issues. Through the use of multiple IMC cores for high parallelism, and by leveraging in-SRAM IMC for data management, PPIMCE offers a compact, energy-efficient solution for accelerating HE and GC. PPIMCE achieves a 107X speedup against a CPU implementation of GC. Additionally, PPIMCE achieves a 1,500X and 800X speedup compared to CPU and GPU implementations of CKKS-based HE multiplications. For privacy-preserving machine learning inference, PPIMCE attains a 1,000X speedup compared to CPU and a 12X speedup against CraterLake, the state-of-art privacy preserving computation accelerator.

  匹配依据：MPC: garbled circuits

  </details>

- **Erase and Repair: An Efficient Box-Free Removal Attack on High-Capacity Deep Hiding**
  2023-08-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.01512)
  Hangcheng Liu, Tao Xiang, Shangwei Guo, Han Li, Tianwei Zhang, Xiaofeng Liao

  <details><summary>摘要 / Abstract</summary>

  Deep hiding, embedding images with others using deep neural networks, has demonstrated impressive efficacy in increasing the message capacity and robustness of secret sharing. In this paper, we challenge the robustness of existing deep hiding schemes by preventing the recovery of secret images, building on our in-depth study of state-of-the-art deep hiding schemes and their vulnerabilities. Leveraging our analysis, we first propose a simple box-free removal attack on deep hiding that does not require any prior knowledge of the deep hiding schemes. To improve the removal performance on the deep hiding schemes that may be enhanced by adversarial training, we further design a more powerful removal attack, efficient box-free removal attack (EBRA), which employs image inpainting techniques to remove secret images from container images. In addition, to ensure the effectiveness of our attack and preserve the fidelity of the processed container images, we design an erasing phase based on the locality of deep hiding to remove secret information and then make full use of the visual information of container images to repair the erased visual content. Extensive evaluations show our method can completely remove secret images from container images with negligible impact on the quality of container images.

  匹配依据：MPC: secret sharing

  </details>

- **Broadcast-Optimal Two Round MPC with Asynchronous Peer-to-Peer Channels**
  2023-08-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1187)
  Ivan Damgård, Divya Ravi, Luisa Siniscalchi, Sophia Yakoubov

  <details><summary>摘要 / Abstract</summary>

  In this paper we continue the study of two-round broadcast-optimal MPC, where broadcast is used in one of the two rounds, but not in both. We consider the realistic scenario where the round that does not use broadcast is asynchronous. Since a first asynchronous round (even when followed by a round of broadcast) does not admit any secure computation, we introduce a new notion of asynchrony which we call $(t_d, t_m)$-asynchrony. In this new notion of asynchrony, an adversary can delay or drop up to $t_d$ of a given party&#x27;s incoming messages; we refer to $t_d$ as the deafness threshold. Similarly, the adversary can delay or drop up to $t_m$ of a given party&#x27;s outgoing messages; we refer to $t_m$ as the muteness threshold. We determine which notions of secure two-round computation are achievable when the first round is $(t_d, t_m)$-asynchronous, and the second round is over broadcast. Similarly, we determine which notions of secure two-round computation are achievable when the first round is over broadcast, and the second round is (fully) asynchronous. We consider the cases where a PKI is available, when only a CRS is available but private communication in the first round is possible, and the case when only a CRS is available and no private communication is possible before the parties have had a chance to exchange public keys.

  匹配依据：MPC: secure computation

  </details>

- **Scalable Time-Lock Puzzles**
  2023-08-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1183)
  Aydin Abadi, Dan Ristea, Artem Grigor, Steven J. Murdoch

  <details><summary>摘要 / Abstract</summary>

  Time-Lock Puzzles (TLPs) enable a client to lock a message such that a server can unlock it only after a specified time. They have diverse applications, such as scheduled payments, secret sharing, and zero-knowledge proofs. In this work, we present a scalable TLP designed for real-world scenarios involving a large number of puzzles, where clients or servers may lack the computational resources to handle high workloads. Our contributions are both theoretical and practical. From a theoretical standpoint, we formally define the concept of a &quot;Delegated Time-Lock Puzzle (D-TLP)&quot;, establish its fundamental properties, and introduce an upper bound for TLPs, addressing a previously overlooked aspect. From a practical standpoint, we introduce the &quot;Efficient Delegated Time-Lock Puzzle&quot; (ED-TLP) protocol, which implements the D-TLP concept. This protocol enables both the client and server to securely outsource their resource-intensive tasks to third-party helpers. It enables realtime verification of solutions and guarantees their delivery within predefined time limits by integrating an upper bound and a fair payment algorithm. ED-TLP allows combining puzzles from different clients, enabling a solver to process them sequentially, significantly reducing computational resources, especially for a large number of puzzles or clients. ED-TLP is the first protocol of its kind. We have implemented ED-TLP and conducted a comprehensive analysis of its performance for up to 10,000 puzzles. The results highlight its significant efficiency in TLP applications, demonstrating that EDTLP securely delegates 99% of the client’s workload and 100% of the server’s workload with minimal overhead.

  匹配依据：MPC: secret sharing

  </details>

- **Scalable Time-Lock Puzzle**
  2023-08-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.01280)
  Aydin Abadi, Dan Ristea, Artem Grigor, Steven J. Murdoch

  <details><summary>摘要 / Abstract</summary>

  Time-Lock Puzzles (TLPs) enable a client to lock a message such that a server can unlock it only after a specified time. They have diverse applications, such as scheduled payments, secret sharing, and zero-knowledge proofs. In this work, we present a scalable TLP designed for real-world scenarios involving a large number of puzzles, where clients or servers may lack the computational resources to handle high workloads. Our contributions are both theoretical and practical. From a theoretical standpoint, we formally define the concept of a Delegated Time-Lock Puzzle (D-TLP), establish its fundamental properties, and introduce an upper bound for TLPs, addressing a previously overlooked aspect. From a practical standpoint, we introduce the Efficient Delegated Time-Lock Puzzle (ED-TLP) protocol, which implements the D-TLP concept. This protocol enables both the client and server to securely outsource their resource-intensive tasks to third-party helpers. It enables real-time verification of solutions and guarantees their delivery within predefined time limits by integrating an upper bound and a fair payment algorithm. ED-TLP allows combining puzzles from different clients, enabling a solver to process them sequentially, significantly reducing computational resources, especially for a large number of puzzles or clients. ED-TLP is the first protocol of its kind. We have implemented ED-TLP and conducted a comprehensive analysis of its performance for up to 10,000 puzzles. The results highlight its significant efficiency in TLP applications, demonstrating that ED-TLP securely delegates 99% of the client&#x27;s workload and 100% of the server&#x27;s workload with minimal overhead.

  匹配依据：MPC: secret sharing

  </details>

- **Verifiable Data Sharing Scheme for Dynamic Multi-Owner Setting**
  2023-08-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.00239)
  Jing Zhao, Qianqian Su

  <details><summary>摘要 / Abstract</summary>

  One of scenarios in data-sharing applications is that files are managed by multiple owners, and the list of file owners may change dynamically. However, most existing solutions to this problem rely on trusted third parties and have complicated signature permission processes, resulting in additional overhead. Therefore, we propose a verifiable data-sharing scheme (VDS-DM) that can support dynamic multi-owner scenarios. We introduce a management entity that combines linear secret-sharing technology, multi-owner signature generation, and an aggregation technique to allow multi-owner file sharing. Without the help of trusted third parties, VDS-DM can update file signatures for dynamically changing file owners, which helps save communication overhead. Moreover, users independently verify the integrity of files without resorting to a third party. We analyse the security of VDS-DM through a security game. Finally, we conduct enough simulation experiments and the outcomes of experimental demonstrate the feasibility of VDS-DM.

  匹配依据：MPC: secret sharing

  </details>

- **Composable Oblivious Pseudo-Random Functions via Garbled Circuits**
  2023-08-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1176)
  Sebastian Faller, Astrid Ottenhues, Johannes Ottenhues

  <details><summary>摘要 / Abstract</summary>

  Oblivious Pseudo-Random Functions (OPRFs) are a central tool for building modern protocols for authentication and distributed computation. For example, OPRFs enable simple login protocols that do not reveal the password to the provider, which helps to mitigate known shortcomings of password-based authentication such as password reuse or mix-up. Reliable treatment of passwords becomes more and more important as we login to a multitude of services with different passwords in our daily life. To ensure the security and privacy of such services in the long term, modern protocols should always consider the possibility of attackers with quantum computers. Therefore, recent research has focused on constructing post-quantum-secure OPRFs. Unfortunately, existing constructions either lack efficiency, or they are based on complex and relatively new cryptographic assumptions, some of which have lately been disproved. In this paper, we revisit the security and the efficiency of the well-known “OPRFs via Garbled Circuits” approach. Such an OPRF is presumably post-quantum-secure and built from well-understood primitives, namely symmetric cryptography and oblivious transfer. We investigate security in the strong Universal Composability model, which guarantees security even when multiple instances are executed in parallel and in conjunction with arbitrary other protocols, which is a realistic scenario in today’s internet. At the same time, it is faster than other current post-quantumsecure OPRFs. Our implementation and benchmarks demonstrate that our proposed OPRF is currently among the best choices if the privacy of the data has to be guaranteed for a long time.

  匹配依据：MPC: garbled circuits, oblivious transfer

  </details>

- **Fast batched asynchronous distributed key generation**
  2023-07-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1175)
  Jens Groth, Victor Shoup

  <details><summary>摘要 / Abstract</summary>

  We present new protocols for threshold Schnorr signatures that work in an asynchronous communication setting, providing robustness and optimal resilience. These protocols provide unprecedented performance in terms of communication and computational complexity. In terms of communication complexity, for each signature, a single party must transmit a few dozen group elements and scalars across the network (independent of the size of the signing committee). In terms of computational complexity, the amortized cost for one party to generate a signature is actually less than that of just running the standard Schnorr signing or verification algorithm (at least for moderately sized signing committees, say, up to 100). For example, we estimate that with a signing committee of 49 parties, at most 16 of which are corrupt, we can generate 50,000 Schnorr signatures per second (assuming each party can dedicate one standard CPU core and 500Mbs of network bandwidth to signing). Importantly, this estimate includes both the cost of an offline precomputation phase (which just churns out message independent &quot;presignatures&quot;) and an online signature generation phase. Also, the online signing phase can generate a signature with very little network latency (just one to three rounds, depending on how throughput and latency are balanced). To achieve this result, we provide two new innovations. One is a new secret sharing protocol (again, asynchronous, robust, optimally resilient) that allows the dealer to securely distribute shares of a large batch of ephemeral secret keys, and to publish the corresponding ephemeral public keys. To achieve better performance, our protocol minimizes public-key operations, and in particular, is based on a novel technique that does not use the traditional technique based on &quot;polynomial commitments&quot;. The second innovation is a new algorithm to efficiently combine ephemeral public keys contributed by different parties (some possibly corrupt) into a smaller number of secure ephemeral public keys. This new algorithm is based on a novel construction of a so-called &quot;super-invertible matrix&quot; along with a corresponding highly-efficient algorithm for multiplying this matrix by a vector of group elements. As protocols for verifiably sharing a secret key with an associated public key and the technology of super-invertible matrices both play a major role in threshold cryptography and multi-party computation, our two new innovations should have applicability well beyond that of threshold Schnorr signatures.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Round-Optimal Black-Box MPC in the Plain Model**
  2023-07-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1173)
  Yuval Ishai, Dakshita Khurana, Amit Sahai, Akshayaram Srinivasan

  <details><summary>摘要 / Abstract</summary>

  We give the first construction of a fully black-box round-optimal secure multiparty computation (MPC) protocol in the plain model. Our protocol makes black-box use of a sub-exponentially secure two-message statistical sender private oblivious transfer (SSP-OT), which in turn can be based on (sub-exponential variants of) almost all of the standard cryptographic assumptions known to imply public-key cryptography.

  匹配依据：MPC: oblivious transfer, secure multiparty computation

  </details>

- **Evolving Homomorphic Secret Sharing for Hierarchical Access Structures**
  2023-07-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1168)
  Kittiphop Phalakarn, Vorapong Suppakitpaisarn, Nuttapong Attrapadung, Kanta Matsuura

  <details><summary>摘要 / Abstract</summary>

  Secret sharing is a cryptographic primitive that divides a secret into several shares, and allows only some combinations of shares to recover the secret. As it can also be used in secure multi-party computation protocol with outsourcing servers, several variations of secret sharing are devised for this purpose. Most of the existing protocols require the number of computing servers to be determined in advance. However, in some situations we may want the system to be &quot;evolving&quot;. We may want to increase the number of servers and strengthen the security guarantee later in order to improve availability and security of the system. Although evolving secret sharing schemes are available, they do not support computing on shares. On the other hand, &quot;homomorphic&quot; secret sharing allows computing on shares with small communication, but they are not evolving. As the contribution of our work, we give the definition of &quot;evolving homomorphic&quot; secret sharing supporting both properties. We propose two schemes, one with hierarchical access structure supporting multiplication, and the other with partially hierarchical access structure supporting computation of low degree polynomials. Comparing to the work with similar functionality of Choudhuri et al. (IACR ePrint 2020), our schemes have smaller communication costs.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Efficient Oblivious Evaluation Protocol and Conditional Disclosure of Secrets for DFA**
  2023-07-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1169)
  Kittiphop Phalakarn, Nuttapong Attrapadung, Kanta Matsuura

  <details><summary>摘要 / Abstract</summary>

  In oblivious finite automata evaluation, one party holds a private automaton, and the other party holds a private string of characters. The objective is to let the parties know whether the string is accepted by the automaton or not, while keeping their inputs secret. The applications include DNA searching, pattern matching, and more. Most of the previous works are based on asymmetric cryptographic primitives, such as homomorphic encryption and oblivious transfer. These primitives are significantly slower than symmetric ones. Moreover, some protocols also require several rounds of interaction. As our main contribution, we propose an oblivious finite automata evaluation protocol via conditional disclosure of secrets (CDS), using one (potentially malicious) outsourcing server. This results in a constant-round protocol, and no heavy asymmetric-key primitives are needed. Our protocol is based on a building block called &quot;an oblivious CDS scheme for deterministic finite automata&#x27;&#x27; which we also propose in this paper. In addition, we propose a standard CDS scheme for deterministic finite automata as an independent interest.

  匹配依据：MPC: oblivious transfer

  </details>

- **Constructive $t$-secure Homomorphic Secret Sharing for Low Degree Polynomials**
  2023-07-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1167)
  Kittiphop Phalakarn, Vorapong Suppakitpaisarn, Nuttapong Attrapadung, Kanta Matsuura

  <details><summary>摘要 / Abstract</summary>

  This paper proposes $t$-secure homomorphic secret sharing schemes for low degree polynomials. Homomorphic secret sharing is a cryptographic technique to outsource the computation to a set of servers while restricting some subsets of servers from learning the secret inputs. Prior to our work, at Asiacrypt 2018, Lai, Malavolta, and Schröder proposed a $1$-secure scheme for computing polynomial functions. They also alluded to $t$-secure schemes without giving explicit constructions; constructing such schemes would require solving set cover problems, which are generally NP-hard. Moreover, the resulting implicit schemes would require a large number of servers. In this paper, we provide a constructive solution for threshold-$t$ structures by combining homomorphic encryption with the classic secret sharing scheme for general access structure by Ito, Saito, and Nishizeki. Our scheme also quantitatively improves the number of required servers from $O(t^2)$ to $O(t)$, compared to the implicit scheme of Lai et al. We also suggest several ideas for future research directions.

  匹配依据：MPC: secret sharing

  </details>

- **Swiper: a new paradigm for efficient weighted distributed protocols**
  2023-07-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2307.15561) · [IACR ePrint](https://eprint.iacr.org/2023/1164)
  Andrei Tonkikh, Luciano Freitas

  <details><summary>摘要 / Abstract</summary>

  The majority of fault-tolerant distributed algorithms are designed assuming a nominal corruption model, in which at most a fraction $f_n$ of parties can be corrupted by the adversary. However, due to the infamous Sybil attack, nominal models are not sufficient to express the trust assumptions in open (i.e., permissionless) settings. Instead, permissionless systems typically operate in a weighted model, where each participant is associated with a weight and the adversary can corrupt a set of parties holding at most a fraction $f_w$ of the total weight. In this paper, we suggest a simple way to transform a large class of protocols designed for the nominal model into the weighted model. To this end, we formalize and solve three novel optimization problems, which we collectively call the weight reduction problems, that allow us to map large real weights into small integer weights while preserving the properties necessary for the correctness of the protocols. In all cases, we manage to keep the sum of the integer weights to be at most linear in the number of parties, resulting in extremely efficient protocols for the weighted model. Moreover, we demonstrate that, on weight distributions that emerge in practice, the sum of the integer weights tends to be far from the theoretical worst case and, sometimes, even smaller than the number of participants. While, for some protocols, our transformation requires an arbitrarily small reduction in resilience (i.e., $f_w = f_n - \epsilon$), surprisingly, for many important problems, we manage to obtain weighted solutions with the same resilience ($f_w = f_n$) as nominal ones. Notable examples include erasure-coded distributed storage and broadcast protocols, verifiable secret sharing, and asynchronous consensus. Although there are ad-hoc weighted solutions to some of these problems, the protocols yielded by our transformations enjoy all the benefits of nominal solutions, including simplicity, efficiency, and a wider range of possible cryptographic assumptions.

  匹配依据：MPC: secret sharing

  </details>

- **Semi-Honest 2-Party Faithful Truncation from Two-Bit Extraction**
  2023-07-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1159)
  Huan Zou, Yuting Xiao, Rui Zhang

  <details><summary>摘要 / Abstract</summary>

  As a fundamental operation in fixed-point arithmetic, truncation can bring the product of two fixed-point integers back to the fixed-point representation. In large-scale applications like privacy-preserving machine learning, it is essential to have faithful truncation that accurately eliminates both big and small errors. In this work, we improve and extend the results of the oblivious transfer based faithful truncation protocols initialized by Cryptflow2 (Rathee et al., CCS 2020). Specifically, we propose a new notion of two-bit extraction that is tailored for faithful truncation and demonstrate how it can be used to construct an efficient faithful truncation protocol. Benefiting from our efficient construction for two-bit extraction, our faithful truncation protocol reduces the communication complexity of Cryptflow2 from growing linearly with the fixed-point precision to logarithmic complexity. This efficiency improvement is due to the fact that we reuse the intermediate results of eliminating the big error to further eliminate the small error. Our reuse strategy is effective, as it shows that while eliminating the big error, it is possible to further eliminate the small error at a minimal cost, e.g., as low as communicating only an additional 160 bits in one round.

  匹配依据：MPC: oblivious transfer

  </details>

- **Samplable Anonymous Aggregation for Private Federated Data Analysis**
  2023-07-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2307.15017)
  Kunal Talwar, Shan Wang, Audra McMillan, Vojta Jina, Vitaly Feldman, Pansy Bansal, Bailey Basile, Aine Cahill, Yi Sheng Chan, Mike Chatzidakis, Junye Chen, Oliver Chick, Mona Chitnis, Suman Ganta, Yusuf Goren, Filip Granqvist, Kristine Guo, Frederic Jacobs, Omid Javidbakht, Albert Liu, Richard Low, Dan Mascenik, Steve Myers, David Park, Wonhee Park, Gianni Parsa, Tommy Pauly, Christian Priebe, Rehan Rishi, Guy Rothblum, Michael Scaria, Linmao Song, Congzheng Song, Karl Tarbe, Sebastian Vogt, Luke Winstrom, Shundong Zhou

  <details><summary>摘要 / Abstract</summary>

  We revisit the problem of designing scalable protocols for private statistics and private federated learning when each device holds its private data. Locally differentially private algorithms require little trust but are (provably) limited in their utility. Centrally differentially private algorithms can allow significantly better utility but require a trusted curator. This gap has led to significant interest in the design and implementation of simple cryptographic primitives, that can allow central-like utility guarantees without having to trust a central server. Our first contribution is to propose a new primitive that allows for efficient implementation of several commonly used algorithms, and allows for privacy accounting that is close to that in the central setting without requiring the strong trust assumptions it entails. {\em Shuffling} and {\em aggregation} primitives that have been proposed in earlier works enable this for some algorithms, but have significant limitations as primitives. We propose a {\em Samplable Anonymous Aggregation} primitive, which computes an aggregate over a random subset of the inputs and show that it leads to better privacy-utility trade-offs for various fundamental tasks. Secondly, we propose a system architecture that implements this primitive and perform a security analysis of the proposed system. Our design combines additive secret-sharing with anonymization and authentication infrastructures.

  匹配依据：MPC: secret sharing

  </details>

- **Secure Function Extensions to Additively Homomorphic Cryptosystems**
  2023-07-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1155)
  Mounika Pratapa, Aleksander Essex

  <details><summary>摘要 / Abstract</summary>

  The number-theoretic literature has long studied the question of distributions of sequences of quadratic residue symbols modulo a prime number. In this paper, we present an efficient algorithm for generating primes containing chosen sequences of quadratic residue symbols and use it as the basis of a method extending the functionality of additively homomorphic cryptosystems. We present an algorithm for encoding a chosen Boolean function into the public key and an efficient two-party protocol for evaluating this function on an encrypted sum. We demonstrate concrete parameters for secure function evaluation on encrypted sums up to eight bits at standard key sizes in the integer factorization setting. Although the approach is limited to applications involving small sums, it is a practical way to extend the functionality of existing secure protocols built on partially homomorphic encryption schemes.

  匹配依据：MPC: secure function evaluation

  </details>

- **Quantum Secure Threshold Private Set Intersection Protocol for IoT-Enabled Privacy Preserving Ride-Sharing Application**
  2023-07-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1154)
  Tapaswini Mohanty, Vikas Srivastava, Sumit Kumar Debnath, Ashok Kumar Das, Biplab Sikdar

  <details><summary>摘要 / Abstract</summary>

  The Internet of Things (IoT)-enabled ride sharing is one of the most transforming and innovative technologies in the transportation industry. It has myriads of advantages, but with increasing demands there are security concerns as well. Traditionally, cryptographic methods are used to address the security and privacy concerns in a ride sharing system. Unfortunately, due to the emergence of quantum algorithms, these cryptographic protocols may not remain secure. Hence, there is a necessity for privacy-preserving ride sharing protocols which can resist various attacks against quantum computers. In the domain of privacy preserving ride sharing, a threshold private set intersection (TPSI) can be adopted as a viable solution because it enables the users to determine the intersection of private data sets if the set intersection cardinality is greater than or equal to a threshold value. Although TPSI can help to alleviate privacy concerns, none of the existing TPSI is quantum secure. Furthermore, the existing TPSI faces the issue of long-term security. In contrast to classical and post quantum cryptography, quantum cryptography (QC) provides a more robust solution, where QC is based on the postulates of quantum physics (e.g., Heisenberg uncertainty principle, no cloning theorem, etc.) and it can handle the prevailing issues of quantum threat and long-term security. Herein, we propose the first QC based TPSI protocol which has a direct application in privacy preserving ride sharing. Due to the use of QC, our IoT-enabled ride sharing scheme remains quantum secure and achieves long-term security as well.

  匹配依据：MPC: private set intersection

  </details>

- **Dual and Hull code in the first two generic constructions and relationship with the Walsh transform of cryptographic functions**
  2023-07-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2307.14300)
  Virginio Fratianni

  <details><summary>摘要 / Abstract</summary>

  We contribute to the knowledge of linear codes from special polynomials and functions, which have been studied intensively in the past few years. Such codes have several applications in secret sharing, authentication codes, association schemes and strongly regular graphs. This is the first work in which we study the dual codes in the framework of the two generic constructions; in particular, we propose a Gram-Schmidt (complexity of $\mathcal{O}(n^3)$) process to compute them explicitly. The originality of this contribution is in the study of the existence or not of defining sets $D&#x27;$, which can be used as ingredients to construct the dual code $\mathcal{C}&#x27;$ for a given code $\mathcal{C}$ in the context of the second generic construction. We also determine a necessary condition expressed by employing the Walsh transform for a codeword of $\mathcal{C}$ to belong in the dual. This achievement was done in general and when the involved functions are weakly regularly bent. We shall give a novel description of the Hull code in the framework of the two generic constructions. Our primary interest is constructing linear codes of fixed Hull dimension and determining the (Hamming) weight of the codewords in their duals.

  匹配依据：MPC: secret sharing

  </details>

- **PUMA: Secure Inference of LLaMA-7B in Five Minutes**
  2023-07-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2307.12533)
  Ye Dong, Wen-jie Lu, Yancheng Zheng, Haoqi Wu, Derun Zhao, Jin Tan, Zhicong Huang, Cheng Hong, Tao Wei, Wenguang Chen

  <details><summary>摘要 / Abstract</summary>

  With ChatGPT as a representative, tons of companies have began to provide services based on large Transformers models. However, using such a service inevitably leak users&#x27; prompts to the model provider. Previous studies have studied secure inference for Transformer models using secure multiparty computation (MPC), where model parameters and clients&#x27; prompts are kept secret. Despite this, these frameworks are still limited in terms of model performance, efficiency, and deployment. To address these limitations, we propose framework PUMA to enable fast and secure Transformer model inference. Our framework designs high quality approximations for expensive functions such as GeLU and softmax, and significantly reduce the cost of secure inference while preserving the model performance. Additionally, we design secure Embedding and LayerNorm procedures that faithfully implement the desired functionality without undermining the Transformer architecture. PUMA is about $2\times$ faster than the state-of-the-art framework MPCFORMER(ICLR 2023) and has similar accuracy as plaintext models without fine-tuning (which the previous works failed to achieve). PUMA can even evaluate LLaMA-7B in around 5 minutes to generate 1 token. To our best knowledge, this is the first time that a model with such a parameter size is able to be evaluated under MPC. PUMA has been open-sourced in the Github repository of SecretFlow-SPU.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Instantiating the Hash-Then-Evaluate Paradigm: Strengthening PRFs, PCFs, and OPRFs.**
  2023-07-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1145)
  Chris Brzuska, Geoffroy Couteau, Christoph Egger, Pihla Karanko, Pierre Meyer

  <details><summary>摘要 / Abstract</summary>

  We instantiate the hash-then-evaluate paradigm for pseudorandom functions (PRFs), $\mathsf{PRF}(k, x) := \mathsf{wPRF}(k, \mathsf{RO}(x))$, which builds a PRF $\mathsf{PRF}$ from a weak PRF $\mathsf{wPRF}$ via a public preprocessing random oracle $\mathsf{RO}$. In applications to secure multiparty computation (MPC), only the low-complexity wPRF performs secret-depending operations. Our construction replaces RO by $f(k_H , \mathsf{elf}(x))$, where $f$ is a non-adaptive PRF and the key $k_H$ is public and thus known to the distinguishing adversary. We show that, perhaps surprisingly, several existing weak PRF candidates are plausibly also secure when their inputs are generated by $f(k_H , \mathsf{elf}(x))$. Firstly, analogous cryptanalysis applies (because pseudorandomness of $f$ implies good statistical properties) and/or secondly an attack against the weak PRF with such pseudorandom inputs generated by $f$ would imply surprising results such as key agreement from the hardness of the high-noise version of the Learning Parity with Noise (LPN) when implementing both wPRF and $f$ from this assumption. Our simple transformation of replacing RO(·) public pre-processing by $f(k_H , \mathsf{elf}(x))$ public preprocessing applies to the entire family of PRF-style functions. Specifically, we obtain results for oblivious PRFs, which are a core building block for password-based authenticated key exchange (PAKE) and private set intersection (PSI) protocols, and we also obtain results for pseudorandom correlation functions (PCF), which are a key tool for silent oblivious transfer (OT) extension.

  匹配依据：MPC: oblivious transfer, private set intersection, secure multiparty computation

  </details>

- **Towards Vertical Privacy-Preserving Symbolic Regression via Secure Multiparty Computation**
  2023-07-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2307.11756)
  Du Nguyen Duy, Michael Affenzeller, Ramin-Nikzad Langerodi

  <details><summary>摘要 / Abstract</summary>

  Symbolic Regression is a powerful data-driven technique that searches for mathematical expressions that explain the relationship between input variables and a target of interest. Due to its efficiency and flexibility, Genetic Programming can be seen as the standard search technique for Symbolic Regression. However, the conventional Genetic Programming algorithm requires storing all data in a central location, which is not always feasible due to growing concerns about data privacy and security. While privacy-preserving research has advanced recently and might offer a solution to this problem, their application to Symbolic Regression remains largely unexplored. Furthermore, the existing work only focuses on the horizontally partitioned setting, whereas the vertically partitioned setting, another popular scenario, has yet to be investigated. Herein, we propose an approach that employs a privacy-preserving technique called Secure Multiparty Computation to enable parties to jointly build Symbolic Regression models in the vertical scenario without revealing private data. Preliminary experimental results indicate that our proposed method delivers comparable performance to the centralized solution while safeguarding data privacy.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Secure Multiparty Computation with Identifiable Abort from Vindicating Release**
  2023-07-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1136)
  Ran Cohen, Jack Doerner, Yashvanth Kondi, abhi shelat

  <details><summary>摘要 / Abstract</summary>

  In the dishonest-majority setting, secure multiparty computation (MPC) with identifiable abort (IA) guarantees that honest parties can identify and agree upon at least one cheating party if the protocol does not produce an output. Known MPC constructions with IA rely on generic zero-knowledge proofs, adaptively secure oblivious transfer (OT) protocols, or homomorphic primitives, and thus incur a substantial penalty with respect to protocols that abort without identifiability. We introduce a new, weaker notion of IA called input-revealing IA (IRIA), which can be constructed through selective revealing of committed input values - a technique we call vindicating release. We show that this weaker form of IA can be achieved with small concrete overheads for many interesting protocols in the literature, including the pre-processing protocols needed for several state-of-the-art MPC protocols. We next show how to assemble these IRIA components into an MPC protocol for any functionality with standard IA. Such a realization differs minimally in terms of cost, techniques, and analysis from the equivalent realization that lacks identifiability, e.g., our total bandwidth overhead incurred is less than 2x, which is an asymptotic improvement over prior work on IA. On a practical level, we apply our techniques to the problem of threshold ECDSA, and show that the resulting protocol with standard IA is concretely efficient. On a theoretical level, we present a compiler that transforms any secure protocol into one with standard IA assuming only a variant of statically-corruptable ideal OT.

  匹配依据：MPC: oblivious transfer, secure multiparty computation

  </details>

- **CryptoMask : Privacy-preserving Face Recognition**
  2023-07-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2307.12010)
  Jianli Bai, Xiaowu Zhang, Xiangfu Song, Hang Shao, Qifan Wang, Shujie Cui, Giovanni Russello

  <details><summary>摘要 / Abstract</summary>

  Face recognition is a widely-used technique for identification or verification, where a verifier checks whether a face image matches anyone stored in a database. However, in scenarios where the database is held by a third party, such as a cloud server, both parties are concerned about data privacy. To address this concern, we propose CryptoMask, a privacy-preserving face recognition system that employs homomorphic encryption (HE) and secure multi-party computation (MPC). We design a new encoding strategy that leverages HE properties to reduce communication costs and enable efficient similarity checks between face images, without expensive homomorphic rotation. Additionally, CryptoMask leaks less information than existing state-of-the-art approaches. CryptoMask only reveals whether there is an image matching the query or not, whereas existing approaches additionally leak sensitive intermediate distance information. We conduct extensive experiments that demonstrate CryptoMask&#x27;s superior performance in terms of computation and communication. For a database with 100 million 512-dimensional face vectors, CryptoMask offers ${\thicksim}5 \times$ and ${\thicksim}144 \times$ speed-ups in terms of computation and communication, respectively.

  匹配依据：MPC: secure multi party computation

  </details>

- **Cryptanalysis and Improvement of a Flexible and Lightweight Group Authentication Scheme**
  2023-07-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1132)
  Ali Rezapour, Zahra Ahmadian

  <details><summary>摘要 / Abstract</summary>

  Shamir’s secret sharing scheme is one of the substantial threshold primitives, based on which many security protocols are constructed such as group authentication schemes. Notwithstanding the unconditional security of Shamir&#x27;s secret sharing scheme, protocols that are designed based on this scheme do not necessarily inherit this property. In this work, we evaluate the security of a lightweight group authentication scheme, introduced for IoT networks in IEEE IoT Journal in 2020, and prove its weakness against the linear subspace attack, which is a recently-proposed cryptanalytical method for secret sharing-based schemes. Then, we propose an efficient and attack-resistant group authentication protocol for IoT networks.

  匹配依据：MPC: secret sharing

  </details>

- **Asynchronous Agreement on a Core Set in Constant Expected Time and More Efficient Asynchronous VSS and MPC**
  2023-07-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1130)
  Ittai Abraham, Gilad Asharov, Arpita Patra, Gilad Stern

  <details><summary>摘要 / Abstract</summary>

  A major challenge of any asynchronous MPC protocol is the need to reach an agreement on the set of private inputs to be used as input for the MPC functionality. Ben-Or, Canetti and Goldreich [STOC 93] call this problem Agreement on a Core Set (ACS) and solve it by running $n$ parallel instances of asynchronous binary Byzantine agreements. To the best of our knowledge, all results in the perfect and statistical security setting used this same paradigm for solving ACS. Using all known asynchronous binary Byzantine agreement protocols, this type of ACS has $\Omega(\log n)$ expected round complexity, which results in such a bound on the round complexity of asynchronous MPC protocols as well (even for constant depth circuits). We provide a new solution for Agreement on a Core Set that runs in expected $O(1)$ rounds. Our perfectly secure variant is optimally resilient ($t&lt;n/4$) and requires just $O(n^4\log n)$ expected communication complexity. We show a similar result with statistical security for $t&lt;n/3$. Our ACS is based on a new notion of Asynchronously Validated Asynchronous Byzantine Agreement (AVABA) and new information-theoretic analogs to techniques used in the authenticated model. Along the way, we also construct a new perfectly secure packed asynchronous verifiable secret sharing (AVSS) protocol with just $O(n^3\log n)$ communication complexity, improving the state of the art by a factor of $O(n)$. This leads to a more efficient asynchronous MPC that matches the state-of-the-art synchronous MPC.

  匹配依据：MPC: secret sharing

  </details>

- **Algebraic Attacks on RAIN and AIM Using Equivalent Representations**
  2023-07-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1133)
  Fukang Liu, Mohammad Mahzoun, Morten Øygarden, Willi Meier

  <details><summary>摘要 / Abstract</summary>

  Designing novel symmetric-key primitives for advanced protocols like secure multiparty computation (MPC), fully homomorphic encryption (FHE) and zero-knowledge proof systems (ZK), has been an important research topic in recent years. Many such existing primitives adopt quite different design strategies from conventional block ciphers. Notable features include that many of these ciphers are defined over a large finite field, and that a power map is commonly used to construct the nonlinear component due to its efficiency in these applications as well as its strong resistance against the differential and linear cryptanalysis. In this paper, we target the MPC-friendly ciphers AIM and RAIN used for the post-quantum signature schemes AIMer (CCS 2023 and NIST PQC Round 1 Additional Signatures) and Rainier (CCS 2022), respectively. Specifically, we can find equivalent representations of 2-round RAIN and full-round AIM, respectively, which make them vulnerable to either the polynomial method, or the crossbred algorithm, or the fast exhaustive search attack. Consequently, we can break 2-round RAIN with the 128/192/256-bit key in only $2^{111}/2^{170}/2^{224}$ bit operations. For full-round AIM with the 128/192/256-bit key, we could break them in $2^{136.2}/2^{200.7}/2^{265}$ bit operations, which are equivalent to about $2^{115}/2^{178}/2^{241}$ calls of the underlying primitives. In particular, our analysis indicates that AIM does not reach the required security levels by the NIST competition.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Zone-Based Privacy-Preserving Billing for Local Energy Market Based on Multiparty Computation**
  2023-07-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2307.08778)
  Eman Alqahtani, Mustafa A. Mustafa

  <details><summary>摘要 / Abstract</summary>

  This paper proposes a zone-based privacy-preserving billing protocol for local energy markets that takes into account energy volume deviations of market participants from their bids. Our protocol incorporates participants&#x27; locations on the grid for splitting the deviations cost. The proposed billing model employs multiparty computation so that the accurate calculation of individual bills is performed in a decentralised and privacy-preserving manner. We also present a security analysis as well as performance evaluations for different security settings. The results show superiority of the honest-majority model to the dishonest majority in terms of computational efficiency. They also show that the billing can be executed for 5000 users in less than nine seconds in the online phase for all security settings, demonstrating its feasibility to be deployed in real local energy markets.

  匹配依据：MPC: multiparty computation

  </details>

- **RYDE: A Digital Signature Scheme based on Rank-Syndrome-Decoding Problem with MPCitH Paradigm**
  2023-07-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2307.08726)
  Loïc Bidoux, Jesús-Javier Chi-Domínguez, Thibauld Feneuil, Philippe Gaborit, Antoine Joux, Matthieu Rivain, Adrien Vinçotte

  <details><summary>摘要 / Abstract</summary>

  We present a signature scheme based on the Syndrome-Decoding problem in rank metric. It is a construction from multi-party computation (MPC), using a MPC protocol which is a slight improvement of the linearized-polynomial protocol used in [Fen22], allowing to obtain a zero-knowledge proof thanks to the MPCitH paradigm. We design two different zero-knowledge proofs exploiting this paradigm: the first, which reaches the lower communication costs, relies on additive secret sharings and uses the hypercube technique [AMGH+22]; and the second relies on low-threshold linear secret sharings as proposed in [FR22]. These proofs of knowledge are transformed into signature schemes thanks to the Fiat-Shamir heuristic [FS86].

  匹配依据：MPC: multi party computation

  </details>

- **Privacy-preserving patient clustering for personalized federated learning**
  2023-07-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2307.08847)
  Ahmed Elhussein, Gamze Gursoy

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) is a machine learning framework that enables multiple organizations to train a model without sharing their data with a central server. However, it experiences significant performance degradation if the data is non-identically independently distributed (non-IID). This is a problem in medical settings, where variations in the patient population contribute significantly to distribution differences across hospitals. Personalized FL addresses this issue by accounting for site-specific distribution differences. Clustered FL, a Personalized FL variant, was used to address this problem by clustering patients into groups across hospitals and training separate models on each group. However, privacy concerns remained as a challenge as the clustering process requires exchange of patient-level information. This was previously solved by forming clusters using aggregated data, which led to inaccurate groups and performance degradation. In this study, we propose Privacy-preserving Community-Based Federated machine Learning (PCBFL), a novel Clustered FL framework that can cluster patients using patient-level data while protecting privacy. PCBFL uses Secure Multiparty Computation, a cryptographic technique, to securely calculate patient-level similarity scores across hospitals. We then evaluate PCBFL by training a federated mortality prediction model using 20 sites from the eICU dataset. We compare the performance gain from PCBFL against traditional and existing Clustered FL frameworks. Our results show that PCBFL successfully forms clinically meaningful cohorts of low, medium, and high-risk patients. PCBFL outperforms traditional and existing Clustered FL frameworks with an average AUC improvement of 4.3% and AUPRC improvement of 7.8%.

  匹配依据：MPC: secure multiparty computation

  </details>

- **MIRA: a Digital Signature Scheme based on the MinRank problem and the MPC-in-the-Head paradigm**
  2023-07-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2307.08575)
  Nicolas Aragon, Loïc Bidoux, Jesús-Javier Chi-Domínguez, Thibauld Feneuil, Philippe Gaborit, Romaric Neveu, Matthieu Rivain

  <details><summary>摘要 / Abstract</summary>

  We exploit the idea of [Fen22] which proposes to build an efficient signature scheme based on a zero-knowledge proof of knowledge of a solution of a MinRank instance. The scheme uses the MPCitH paradigm, which is an efficient way to build ZK proofs. We combine this idea with another idea, the hypercube technique introduced in [AMGH+22], which leads to more efficient MPCitH-based scheme. This new approach is more efficient than classical MPCitH, as it allows to reduce the number of party computation. This gives us a first scheme called MIRA-Additive. We then present an other scheme, based on low-threshold secret sharings, called MIRA-Threshold, which is a faster scheme, at the price of larger signatures. The construction of MPCitH using threshold secret sharing is detailed in [FR22]. These two constructions allows us to be faster than classical MPCitH, with a size of signature around 5.6kB with MIRA-Additive, and 8.3kB with MIRA-Threshold. We detail here the constructions and optimizations of the schemes, as well as their security proofs.

  匹配依据：MPC: secret sharing

  </details>

- **MAPLE: A Metadata-Hiding Policy-Controllable Encrypted Search Platform with Minimal Trust**
  2023-07-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1105)
  Tung Le, Thang Hoang

  <details><summary>摘要 / Abstract</summary>

  Commodity encrypted storage platforms (e.g., IceDrive, pCloud) permit data store and sharing across multiple users while preserving data confidentiality. However, end-to-end encryption may not be sufficient since it only offers confidentiality when the data is at rest or in transit. Meanwhile, sensitive information can be leaked from metadata representing activities during data operations (e.g., query, processing). Recent encrypted search platforms such as DORY (OSDI’20) or DURASIFT (WPES’19) permit multi-user data query functionalities, while protecting metadata privacy. However, they either incur a high processing overhead or offer limited secu- rity/functionality, and require strong trust assumptions. We propose MAPLE, a new metadata-hiding encrypted search platform that offers query functionalities (search, update) on the shared data across multiple users with complex policy controls. MAPLE protects metadata privacy all the time during query processing, while achieving significantly (asymptotically) lower processing overhead than state-of-the-art platforms. The core technique of MAPLE is the design of oblivious data structures for search index and access control coupled with secure computation techniques to enable efficient query processing with a minimal trust. We fully implemented MAPLE and evaluated its performance on commodity cloud (Amazon EC2) under real settings. Experimental results showed that MAPLE achieved a concrete performance comparable with its counterparts, while offering provably stronger security guarantees and more diverse functionalities.

  匹配依据：MPC: secure computation

  </details>

- **$\\textsf{Asterisk}$: Super-fast MPC with a Friend**
  2023-07-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1098)
  Banashri Karmakar, Nishat Koti, Arpita Patra, Sikhar Patranabis, Protik Paul, Divya Ravi

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation$~$(MPC) enables privacy-preserving collaborative computation over sensitive data held by multiple mutually distrusting parties. Unfortunately, in the most natural setting where a majority of the parties are maliciously corrupt$~$(also called the $\textit{dishonest majority}$ setting), traditional MPC protocols incur high overheads and offer weaker security guarantees than are desirable for practical applications. In this paper, we explore the possibility of circumventing these drawbacks and achieving practically efficient dishonest majority MPC protocols with strong security guarantees by assuming an additional semi-honest, non-colluding helper party $\mathrm{HP}$. We believe that this is a more realistic alternative to assuming an honest majority, since many real-world applications of MPC involving potentially large numbers of parties$~$(such as dark pools) are typically enabled by a central governing entity that can be modeled as the $\mathrm{HP}$. In the above model, we are the first to design, implement and benchmark a practically-efficient and general multi-party framework, $\textsf{Asterisk}$. Our framework requires invoking $\mathrm{HP}$ only a constant number of times, achieves the strong security guarantee of $\textit{fairness}$ (either all parties learn the output or none do), scales to hundreds of parties, outperforms all existing dishonest majority MPC protocols, and is, in fact, competitive with state-of-the-art honest majority MPC protocols. Our experiments show that $\textsf{Asterisk}$ achieves $228-288\times$ speedup in preprocessing as compared to the best dishonest majority MPC protocol. With respect to online time, $\textsf{Asterisk}$ supports $100$-party evaluation of a circuit with $10^6$ multiplication gates in approximately $20$ seconds. We also implement and benchmark practically efficient and highly scalable dark pool instances using $\textsf{Asterisk}$. The corresponding run times showcase the effectiveness of $\textsf{Asterisk}$ in enabling efficient realizations of real-world privacy-preserving applications with strong security guarantees.

  匹配依据：MPC: secure multiparty computation

  </details>

- **On Derandomizing Yao's Weak-to-Strong OWF Construction**
  2023-07-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1091)
  Chris Brzuska, Geoffroy Couteau, Pihla Karanko, Felix Rohrbach

  <details><summary>摘要 / Abstract</summary>

  The celebrated result of Yao (FOCS&#x27;82) shows that concatenating $n\cdot p(n)$ copies of a weak one-way function (OWF) $f$, which can be inverted with probability $1-\tfrac{1}{p(n)}$, yields a strong OWF $g$, showing that weak and strong OWFs are black-box equivalent. Yao&#x27;s transformation is not security-preserving, i.e., the input to $g$ needs to be much larger than the input to $f$. Understanding whether a larger input is inherent is a long-standing open question. In this work, we explore necessary features of constructions which achieve short input length by proving the following: for any direct product construction of a strong OWF $g$ from a weak OWF $f$, which can be inverted with probability $1-\tfrac{1}{p(n)}$, the input size of $g$ must grow as $\Omega(p(n))$. Here, direct product refers to the following structure: the construction $g$ executes some arbitrary pre-processing function (independent of $f$) on its input $s$, obtaining a vector $(x_1, \cdots, x_l)$, and outputs $f(x_1), \cdots, f(x_l)$. When setting the pre-processing to be the identity, one recovers thus Yao&#x27;s construction. Our result generalizes to functions $g$ with post-processing, as long as the post-processing function is not too lossy. Thus, in essence, any weak-to-strong OWF hardness amplification must either (1) be very far from security-preserving, (2) use adaptivity, or (3) must be very far from a direct-product structure (in the sense that post-processing of the outputs of $f$ is very lossy). On a technical level, we use ideas from lower bounds for secret-sharing to prove the impossibility of derandomizing Yao in a black-box way. Our results are in line with Goldreich, Impagliazzo, Levin, Venkatesan, and Zuckerman (FOCS 1990) who derandomize Yao&#x27;s construction for regular weak OWFs by evaluating the OWF along a random walk on an expander graph – the construction is adaptive, since it alternates steps on the expander graph with evaluations of the weak OWF.

  匹配依据：MPC: secret sharing

  </details>

- **Benchmarking the Security Protocol and Data Model (SPDM) for component authentication**
  2023-07-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2307.06456)
  Renan C. A. Alves, Bruno C. Albertini, Marcos A. Simplicio

  <details><summary>摘要 / Abstract</summary>

  Efforts to secure computing systems via software traditionally focus on the operating system and application levels. In contrast, the Security Protocol and Data Model (SPDM) tackles firmware level security challenges, which are much harder (if at all possible) to detect with regular protection software. SPDM includes key features like enabling peripheral authentication, authenticated hardware measurements retrieval, and secure session establishment. Since SPDM is a relatively recent proposal, there is a lack of studies evaluating its performance impact on real-world applications. In this article, we address this gap by: (1) implementing the protocol on a simple virtual device, and then investigating the overhead introduced by each SDPM message; and (2) creating an SPDM-capable virtual hard drive based on VirtIO, and comparing the resulting read/write performance with a regular, unsecured implementation. Our results suggest that SPDM bootstrap time takes the order of tens of milliseconds, while the toll of introducing SPDM on hard drive communication highly depends on specific workload patterns. For example, for mixed random read/write operations, the slowdown is negligible in comparison to the baseline unsecured setup. Conversely, for sequential read or write operations, the data encryption process becomes the bottleneck, reducing the performance indicators by several orders of magnitude.

  匹配依据：MPC: secure computing

  </details>

- **Taming Adaptivity in YOSO Protocols: The Modular Way**
  2023-07-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1077)
  Ran Canetti, Sebastian Kolby, Divya Ravi, Eduardo Soria-Vazquez, Sophia Yakoubov

  <details><summary>摘要 / Abstract</summary>

  YOSO-style MPC protocols (Gentry et al., Crypto&#x27;21), are a promising framework where the overall computation is partitioned into small, short-lived pieces, delegated to subsets of one-time stateless parties. Such protocols enable gaining from the security benefits provided by using a large community of participants where &quot;mass corruption&quot; of a large fraction of participants is considered unlikely, while keeping the computational and communication costs manageable. However, fully realizing and analyzing YOSO-style protocols has proven to be challenging: While different components have been defined and realized in various works, there is a dearth of protocols that have reasonable efficiency and enjoy full end to end security against adaptive adversaries. The YOSO model separates the protocol design, specifying the short-lived responsibilities, from the mechanisms assigning these responsibilities to machines participating in the computation. These protocol designs must then be translated to run directly on the machines, while preserving security guarantees. We provide a versatile and modular framework for analyzing the security of YOSO-style protocols, and show how to use it to compile any protocol design that is secure against static corruptions of $t$ out of $c$ parties, into protocols that withstand adaptive corruption of $T$ out of $N$ machines (where $T/N$ is closely related to $t/c$, specifically when $t/c&lt;0.5$, we tolerate $T/N \leq 0.29$) at overall communication cost that is comparable to that of the traditional protocol even when $c &lt;&lt; N$. Furthermore, we demonstrate how to minimize the use of costly non-committing encryption, thereby keeping the computational and communication overhead manageable even in practical terms, while still providing end to end security analysis. Combined with existing approaches for transforming stateful protocols into stateless ones while preserving static security (e.g. Gentry et al. 21, Kolby et al. 22), we obtain end to end security.

  匹配依据：MPC: mpc (context)

  </details>

- **ARITHMETIZATION-ORIENTED APN FUNCTIONS**
  2023-07-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1081)
  Lilya Budaghyan, Mohit Pal

  <details><summary>摘要 / Abstract</summary>

  Recently, many cryptographic primitives such as homomorphic encryption (HE), multi-party computation (MPC) and zero-knowledge (ZK) protocols have been proposed in the literature which operate on prime field $\mathbb{F}_p$ for some large prime $p$. Primitives that are designed using such operations are called arithmetization-oriented primitives. As the concept of arithmetization-oriented primitives is new, a rigorous cryptanalysis of such primitives is yet to be done. In this paper, we investigate arithmetization-oriented APN functions. More precisely, we investigate APN permutations in the CCZ-classes of known families of APN power functions over prime field $\mathbb{F}_p$. Moreover, we present a new class of APN binomials over $\mathbb{F}_q$ obtained by modifying the planar function $x^2$ over $\mathbb{F}_q$. We also present a class of binomials having differential uniformity at most $5$ defined via the quadratic character over finite fields of odd characteristic. We give sufficient conditions for which this family of binomials is permutation. Computationally it is confirmed that the latter family contains new APN functions for some small parameters. We conjecture it to contain an infinite subfamily of APN functions.

  匹配依据：MPC: multi party computation

  </details>

- **Towards Fast and Scalable Private Inference**
  2023-07-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2307.04077)
  Jianqiao Mo, Karthik Garimella, Negar Neda, Austin Ebel, Brandon Reagen

  <details><summary>摘要 / Abstract</summary>

  Privacy and security have rapidly emerged as first order design constraints. Users now demand more protection over who can see their data (confidentiality) as well as how it is used (control). Here, existing cryptographic techniques for security fall short: they secure data when stored or communicated but must decrypt it for computation. Fortunately, a new paradigm of computing exists, which we refer to as privacy-preserving computation (PPC). Emerging PPC technologies can be leveraged for secure outsourced computation or to enable two parties to compute without revealing either users&#x27; secret data. Despite their phenomenal potential to revolutionize user protection in the digital age, the realization has been limited due to exorbitant computational, communication, and storage overheads. This paper reviews recent efforts on addressing various PPC overheads using private inference (PI) in neural network as a motivating application. First, the problem and various technologies, including homomorphic encryption (HE), secret sharing (SS), garbled circuits (GCs), and oblivious transfer (OT), are introduced. Next, a characterization of their overheads when used to implement PI is covered. The characterization motivates the need for both GCs and HE accelerators. Then two solutions are presented: HAAC for accelerating GCs and RPU for accelerating HE. To conclude, results and effects are shown with a discussion on what future work is needed to overcome the remaining overheads of PI.

  匹配依据：MPC: garbled circuits, oblivious transfer, secret sharing

  </details>

- **ZK-for-Z2K: MPC-in-the-Head Zero-Knowledge Proofs for $\\mathbb{Z}\_{2^k}$**
  2023-07-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1057)
  Lennart Braun, Cyprien Delpech de Saint Guilhem, Robin Jadoul, Emmanuela Orsini, Nigel P. Smart, Titouan Tanguy

  <details><summary>摘要 / Abstract</summary>

  In this work, we extend the MPC-in-the-head framework, used in recent efficient zero-knowledge protocols, to work over the ring $\mathbb{Z}_{2^k}$, which is the primary operating domain for modern CPUs. The proposed schemes are compatible with any threshold linear secret sharing scheme and draw inspiration from MPC protocols adapted for ring operations. Additionally, we explore various batching methodologies, leveraging Shamir&#x27;s secret sharing schemes and Galois ring extensions, and show the applicability of our approach in RAM program verification. Finally, we analyse different options for instantiating the resulting ZK scheme over rings and compare their communication costs.

  匹配依据：MPC: secret sharing

  </details>

- **DIDO: Data Provenance from Restricted TLS 1.3 Websites**
  2023-07-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1056)
  Kwan Yin Chan, Handong Cui, Tsz Hon Yuen

  <details><summary>摘要 / Abstract</summary>

  Public data can be authenticated by obtaining from a trustworthy website with TLS. Private data, such as user profile, are usually restricted from public access. If a user wants to authenticate his private data (e.g., address) provided by a restricted website (e.g., user profile page of a utility company website) to a verifier, he cannot simply give his username and password to the verifier. DECO (CCS 2020) provides a solution for liberating these data without introducing undesirable trust assumption, nor requiring server-side modification. Their implementation is mainly based on TLS 1.2. In this paper, we propose an optimized solution for TLS 1.3 websites. We tackle a number of open problems, including the support of X25519 key exchange in TLS 1.3, the design of round-optimal three-party key exchange, the architecture of two-party computation of TLS 1.3 key scheduling, and circuit design optimized for two-party computation. We test our implementation with real world website and show that our optimization is necessary to avoid timeout in TLS handshake.

  匹配依据：MPC: two party computation

  </details>

- **OWF Candidates Based on: Xors, Error Detection Codes, Permutations, Polynomials, Interaction and Nesting**
  2023-07-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1033)
  Paweł Cyprys, Shlomi Dolev, Oded Margalit

  <details><summary>摘要 / Abstract</summary>

  Our research focuses on designing efficient commitment schemes by drawing inspiration from (perfect) information-theoretical secure primitives, e.g., the one-time pad and secret sharing. We use a random input as a mask for the committed value, outputting a function on the random input. Then, couple the output with the committed value xored with folded random input. First, we explore the potential of leveraging the unique properties of the one-time pad to design effective one-way functions. Our methodology applies the exclusive-or (xor) operation to two randomly chosen strings. To address concerns related to preimage mappings, we incorporate error detection codes. Additionally, we utilize permutations to overcome linearity issues in the computation process. Feistel networks are employed to ensure super pseudo-random permutation using the (random string) input (that serves as the commitment mask) and also as the encryption key. We propose integrating a secret-sharing scheme based on a linear polynomial to mitigate possible collisions. Lastly, we explore the possibility of nesting one-way functions as a countermeasure against potential backdoors. The resulting commitment schemes are efficient, in particular, have fewer layers than the standard cryptographic hash functions, such as SHA, and may fit the NIST effort for lightweight IoT cryptography (e.g., ASCON).

  匹配依据：MPC: secret sharing

  </details>

- **Data-Free Quantization via Mixed-Precision Compensation without Fine-Tuning**
  2023-07-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2307.00498)
  Jun Chen, Shipeng Bai, Tianxin Huang, Mengmeng Wang, Guanzhong Tian, Yong Liu

  <details><summary>摘要 / Abstract</summary>

  Neural network quantization is a very promising solution in the field of model compression, but its resulting accuracy highly depends on a training/fine-tuning process and requires the original data. This not only brings heavy computation and time costs but also is not conducive to privacy and sensitive information protection. Therefore, a few recent works are starting to focus on data-free quantization. However, data-free quantization does not perform well while dealing with ultra-low precision quantization. Although researchers utilize generative methods of synthetic data to address this problem partially, data synthesis needs to take a lot of computation and time. In this paper, we propose a data-free mixed-precision compensation (DF-MPC) method to recover the performance of an ultra-low precision quantized model without any data and fine-tuning process. By assuming the quantized error caused by a low-precision quantized layer can be restored via the reconstruction of a high-precision quantized layer, we mathematically formulate the reconstruction loss between the pre-trained full-precision model and its layer-wise mixed-precision quantized model. Based on our formulation, we theoretically deduce the closed-form solution by minimizing the reconstruction loss of the feature maps. Since DF-MPC does not require any original/synthetic data, it is a more efficient method to approximate the full-precision model. Experimentally, our DF-MPC is able to achieve higher accuracy for an ultra-low precision quantized model compared to the recent methods without any data and fine-tuning process.

  匹配依据：MPC: mpc (context)

  </details>

- **Stronger Lower Bounds for Leakage-Resilient Secret Sharing**
  2023-06-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1017)
  Charlotte Hoffmann, Mark Simkin

  <details><summary>摘要 / Abstract</summary>

  Threshold secret sharing allows a dealer to split a secret $s$ into $n$ shares, such that any $t$ shares allow for reconstructing $s$, but no $t-1$ shares reveal any information about $s$. Leakage-resilient secret sharing requires that the secret remains hidden, even when an adversary additionally obtains a limited amount of leakage from every share. Benhamouda et al. (CRYPTO&#x27;18) proved that Shamir&#x27;s secret sharing scheme is one bit leakage-resilient for reconstruction threshold $t\geq0.85n$ and conjectured that the same holds for $t=c\cdot n$ for any constant $0\leq c\leq1$. Nielsen and Simkin (EUROCRYPT&#x27;20) showed that this is the best one can hope for by proving that Shamir&#x27;s scheme is not secure against one-bit leakage when $t=c\cdot n/\log(n)$. In this work, we strengthen the lower bound of Nielsen and Simkin. We consider noisy leakage-resilience, where a random subset of leakages is replaced by uniformly random noise. We prove a lower bound for Shamir&#x27;s secret sharing, similar to that of Nielsen and Simkin, which holds even when a constant fraction of leakages is replaced by random noise. To this end, we first prove a lower bound on the share size of any noisy-leakage-resilient sharing scheme. We then use this lower bound to show that there exist universal constants $c_1,c_2$, such that for infinitely many $n$, it holds that Shamir&#x27;s secret sharing scheme is not noisy-leakage-resilient for $t\leq c_1\cdot n/\log(n)$, even when a $c_2$ fraction of leakages are replaced by random noise.

  匹配依据：MPC: secret sharing

  </details>

- **Fast Unbalanced Private Computing on (Labeled) Set Intersection with Cardinality**
  2023-06-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1015)
  Binbin Tu, Xiangling Zhang, Yujie Bai, Yu Chen

  <details><summary>摘要 / Abstract</summary>

  Private computation on (labeled) set intersection (PCSI/PCLSI) is a secure computation protocol that allows two parties to compute fine-grained functions on set intersection, including cardinality, cardinality-sum, secret shared intersection, and arbitrary functions. Recently, some computationally efficient PCSI protocols have emerged, but a limitation of these protocols is the communication complexity, which scales (super)-linear with the size of the large set. This is of particular concern when performing PCSI in the unbalanced case, where one party is a constrained device with a small set, and the other is a service provider holding a large set. In this work, we first formalize a new ideal functionality called shared characteristic and its labeled variety called shared characteristic with labels, from which we propose the frameworks of PCSI/PCLSI protocols. By instantiating our frameworks, we obtain a series of efficient PCSI/PCLSI protocols, whose communication complexity is linear in the size of the small set, and logarithmic in the large set. We demonstrate the practicality of our protocols with implementations. Experiment results show that our protocols outperform previous ones and the larger difference between the sizes of two sets, the better our protocols perform. For input set sizes $2^{10}$ and $2^{22}$ with items of length $128$ bits, our PCSI requires only $4.62$MB of communication to compute the cardinality; $4.71$MB of communication to compute the cardinality-sum. Compared with the state-of-the-art PCSI proposed by Chen et al.~\cite{CZZD22}, there are $ 58 \times$ and $77 \times$ reductions in the communication cost of computing cardinality and cardinality-sum.

  匹配依据：MPC: secure computation

  </details>

- **An Efficient Data-Independent Priority Queue and its Application to Dark Pools**
  2023-06-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1014)
  Sahar Mazloom, Benjamin E. Diamond, Antigoni Polychroniadou, Tucker Balch

  <details><summary>摘要 / Abstract</summary>

  We introduce a new data-independent priority queue which supports amortized polylogarithmic-time insertions and constant-time deletions, and crucially, (non-amortized) constant-time \textit{read-front} operations, in contrast with a prior construction of Toft (PODC&#x27;11). Moreover, we reduce the number of required comparisons. Data-independent data structures - first identified explicitly by Toft, and further elaborated by Mitchell and Zimmerman (STACS&#x27;14) - facilitate computation on encrypted data without branching, which is prohibitively expensive in secure computation. Using our efficient data-independent priority queue, we introduce a new privacy-preserving dark pool application, which significantly improves upon prior constructions which were based on costly sorting operations. Dark pools are securities-trading venues which attain ad-hoc order privacy, by matching orders outside of publicly visible exchanges. In this paper, we describe an efficient and secure dark pool (implementing a full continuous double auction), building upon our priority queue construction. Our dark pool&#x27;s security guarantees are cryptographic - based on secure multiparty computation (MPC) - and do not require that the dark pool operators be trusted. Our approach improves upon the asymptotic and concrete efficiency attained by previous efforts. Existing cryptographic dark pools process new orders in time which grows linearly in the size of the standing order book; ours does so in polylogarithmic time. We describe a concrete implementation of our protocol, with malicious security in the honest majority setting. We also report benchmarks of our implementation, and compare these to prior works. Our protocol reduces the total running time by several orders of magnitude, compared to prior secure dark pool solutions.

  匹配依据：MPC: secure computation, secure multiparty computation

  </details>

- **PSI with computation or Circuit-PSI for Unbalanced Sets from Homomorphic Encryption**
  2023-06-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1009)
  Yongha Son, Jinhyuck Jeong

  <details><summary>摘要 / Abstract</summary>

  Circuit-based Private Set Intersection (circuit-PSI) refers to cryptographic protocols that let two parties with input set $X$ and $Y$ compute a function $f$ over the intersection set $X \cap Y$, without revealing any other information. The research efforts for circuit-PSI mainly focus on the case where input set sizes $|X|$ and $|Y|$ are similar so far, and they scale poorly for extremely unbalanced set sizes $|X| \gg |Y|$. Recently, Lepoint \textit{et al.} (ASIACRYPT&#x27;21) proposed the first dedicated solutions for this problem, which has online cost only linear in the small set size $|Y|$. However, it requires an expensive setup phase that requires huge storage of about $O(|X|)$ on the small set holder side, which can be problematic in applications where the small set holder is assumed to have restricted equipment. In this work, we suggest new efficient proposals for circuit-PSI tailored for unbalanced inputs, which feature {\emph{zero}} small set holder side storage, and comparable online phase performance to the previous work. At the technical core, we use homomorphic encryption (HE) based {\emph{plain}} PSI protocols of Cong \textit{et al.} (CCS&#x27;21), with several technically non-trivial arguments on algorithm and security. We demonstrate the superiority of our proposals in several input set sizes by an implementation. As a representative example, for input sets of size $2^{24}$ and $2^{12}$, our proposals require {\emph{zero}} storage on the small set holder whereas Lepoint \textit{et al.} requires over $7$GB. The online phase remains similar; over LAN network setting, ours takes $7.5$ (or $20.9$s) seconds with $45$MB (or $11.7$MB) communication, while Lepoint \textit{et al.} requires $4.2$ seconds with $117$MB communication.

  匹配依据：MPC: private set intersection

  </details>

- **Matroidal Entropy Functions: Constructions, Characterizations and Representations**
  2023-06-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.17041)
  Qi Chen, Minquan Cheng, Baoming Bai

  <details><summary>摘要 / Abstract</summary>

  Matroidal entropy functions are entropy functions in the form $\mathbf{h} = \log v \cdot \mathbf{r}_M$ , where $v \ge 2$ is an integer and $\mathbf{r}_M$ is the rank function of a matroid $M$. They can be applied into capacity characterization and code construction of information theory problems such as network coding, secret sharing, index coding and locally repairable code. In this paper, by constructing the variable strength arrays of some matroid operations, we characterized matroidal entropy functions induced by regular matroids and some matroids with the same p-characteristic set as uniform matroid $U_{2,4}$.

  匹配依据：MPC: secret sharing

  </details>

- **End-to-end Privacy Preserving Training and Inference for Air Pollution Forecasting with Data from Rival Fleets**
  2023-06-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1010)
  Gauri Gupta, Krithika Ramesh, Anwesh Bhattacharya, Divya Gupta, Rahul Sharma, Nishanth Chandran, Rijurekha Sen

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving machine learning (PPML) promises to train machine learning (ML) models by combining data spread across multiple data silos. Theoretically, secure multiparty computation (MPC) allows multiple data owners to train models on their joint data without revealing the data to each other. However, the prior implementations of this secure training using MPC have three limitations: they have only been evaluated on CNNs, and LSTMs have been ignored; fixed point approximations have affected training accuracies compared to training in floating point; and due to significant latency overheads of secure training via MPC, its relevance for practical tasks with streaming data remains unclear. The motivation of this work is to report our experience of addressing the practical problem of secure training and inference of models for urban sensing problems, e.g., traffic congestion estimation, or air pollution monitoring in large cities, where data can be contributed by rival fleet companies while balancing the privacy-accuracy trade-offs using MPC-based techniques. Our first contribution is to design a custom ML model for this task that can be efficiently trained with MPC within a desirable latency. In particular, we design a GCN-LSTM and securely train it on time-series sensor data for accurate forecasting, within 7 minutes per epoch. As our second contribution, we build an end-toend system of private training and inference that provably matches the training accuracy of cleartext ML training. This work is the first to securely train a model with LSTM cells. Third, this trained model is kept secret-shared between the fleet companies and allows clients to make sensitive queries to this model while carefully handling potentially invalid queries. Our custom protocols allow clients to query predictions from privately trained models in milliseconds, all the while maintaining accuracy and cryptographic security

  匹配依据：MPC: secure multiparty computation

  </details>

- **Best of Both Worlds: Revisiting the Spymasters Double Agent Problem**
  2023-06-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1013)
  Anasuya Acharya, Carmit Hazay, Oxana Poburinnaya, Muthuramakrishnan Venkitasubramaniam

  <details><summary>摘要 / Abstract</summary>

  This work defines a notion of secure multiparty computation: MPC with fall-back security. Fall-back security for an $n$-party protocol is defined with respect to an adversary structure $\mathcal{Z}$ wherein security is guaranteed in the presence of both a computationally unbounded adversary with adversary structure $\mathcal{Z}$, and a computationally bounded adversary corrupting an arbitrarily large subset of the parties. This notion was considered in the work of Chaum (Crypto 89) via the Spymaster&#x27;s double agent problem where he showed a semi-honest secure protocol for the honest majority adversary structure. Subsequent works extend this to give maliciously secure protocols tolerating threshold adversaries. Our first main result is a compiler that can transform any $n$-party protocol that is semi-honestly secure with statistical security tolerating a general adversary structure $\mathcal{Z}$ to one that (additionally) provides semi-honest fall-back security w.r.t $\mathcal{Z}$. The resulting protocol has optimal round complexity, up to a constant factor, and is optimal in assumptions and the adversary structure. Our second result fully characterizes when malicious fall-back security is feasible. More precisely, we show that malicious fallback secure protocol w.r.t $\mathcal{Z}$ exists if and only if $\mathcal{Z}$ admits unconditional MPC against a semi-honest adversary (namely, iff $\mathcal{Z} \in \mathcal{Q}^2$).

  匹配依据：MPC: secure multiparty computation

  </details>

- **A Framework for Statistically Sender Private OT with Optimal Rate**
  2023-06-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1011)
  Pedro Branco, Nico Döttling, Akshayaram Srinivasan

  <details><summary>摘要 / Abstract</summary>

  Statistical sender privacy (SSP) is the strongest achievable security notion for two-message oblivious transfer (OT) in the standard model, providing statistical security against malicious receivers and computational security against semi-honest senders. In this work we provide a novel construction of SSP OT from the Decisional Diffie-Hellman (DDH) and the Learning Parity with Noise (LPN) assumptions achieving (asymptotically) optimal amortized communication complexity, i.e. it achieves rate 1. Concretely, the total communication complexity for $k$ OT instances is $2k(1+o(1))$, which (asymptotically) approaches the information-theoretic lower bound. Previously, it was only known how to realize this primitive using heavy rate-1 FHE techniques [Brakerski et al., Gentry and Halevi TCC&#x27;19]. At the heart of our construction is a primitive called statistical co-PIR, essentially a a public key encryption scheme which statistically erases bits of the message in a few hidden locations. Our scheme achieves nearly optimal ciphertext size and provides statistical security against malicious receivers. Computational security against semi-honest senders holds under the DDH assumption.

  匹配依据：MPC: oblivious transfer

  </details>

- **VERTICES: Efficient Two-Party Vertical Federated Linear Model with TTP-aided Secret Sharing**
  2023-06-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.16139)
  Mingxuan Fan, Yilun Jin, Liu Yang, Zhenghang Ren, Kai Chen

  <details><summary>摘要 / Abstract</summary>

  Vertical Federated Learning (VFL) has emerged as one of the most predominant approaches for secure collaborative machine learning where the training data is partitioned by features among multiple parties. Most VFL algorithms primarily rely on two fundamental privacy-preserving techniques: Homomorphic Encryption (HE) and secure Multi-Party Computation (MPC). Though generally considered with stronger privacy guarantees, existing general-purpose MPC frameworks suffer from expensive computation and communication overhead and are inefficient especially under VFL settings. This study centers around MPC-based VFL algorithms and presents a novel approach for two-party vertical federated linear models via an efficient secret sharing (SS) scheme with a trusted coordinator. Our approach can achieve significant acceleration of the training procedure in vertical federated linear models of between 2.5x and 6.6x than other existing MPC frameworks under the same security setting.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Sparse and Private Distributed Matrix Multiplication with Straggler Tolerance**
  2023-06-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.15134)
  Maximilian Egger, Marvin Xhemrishi, Antonia Wachter-Zeh, Rawad Bitar

  <details><summary>摘要 / Abstract</summary>

  This paper considers the problem of outsourcing the multiplication of two private and sparse matrices to untrusted workers. Secret sharing schemes can be used to tolerate stragglers and guarantee information-theoretic privacy of the matrices. However, traditional secret sharing schemes destroy all sparsity in the offloaded computational tasks. Since exploiting the sparse nature of matrices was shown to speed up the multiplication process, preserving the sparsity of the input matrices in the computational tasks sent to the workers is desirable. It was recently shown that sparsity can be guaranteed at the expense of a weaker privacy guarantee. Sparse secret sharing schemes with only two output shares were constructed. In this work, we construct sparse secret sharing schemes that generalize Shamir&#x27;s secret sharing schemes for a fixed threshold $t=2$ and an arbitrarily large number of shares. We design our schemes to provide the strongest privacy guarantee given a desired sparsity of the shares under some mild assumptions. We show that increasing the number of shares, i.e., increasing straggler tolerance, incurs a degradation of the privacy guarantee. However, this degradation is negligible when the number of shares is comparably small to the cardinality of the input alphabet.

  匹配依据：MPC: secret sharing

  </details>
