# 2024 · MPC · 仅预印本来源 · 第 1/5 页

[总目录](../PAPERS.md) · [下一页](2024-mpc-preprint-02.md)

- **String commitment from unstructured noise**
  2024-12-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.00281)
  Jiawei Wu, Masahito Hayashi, Marco Tomamichel

  <details><summary>摘要 / Abstract</summary>

  Noisy channels are a foundational resource for constructing cryptographic primitives such as string commitment and oblivious transfer. The noisy channel model has been extended to unfair noisy channels, where adversaries can influence the parameters of a memoryless channel. In this work, we introduce the unstructured noisy channel model as a generalization of the unfair noisy channel model to allow the adversary to manipulate the channel arbitrarily subject to certain entropic constraints. We present a string commitment protocol with established security and derive its achievable commitment rate, demonstrating the feasibility of commitment against this stronger class of adversaries. Furthermore, we show that the entropic constraints in the unstructured noisy channel model can be derived from physical assumptions such as noisy quantum storage. Our work thus connects two distinct approaches to commitment, i.e., the noisy channel and physical limitations.

  匹配依据：MPC: oblivious transfer

  </details>

- **Efficient Multi-party Private Set Union Resistant to Maximum Collusion Attacks**
  2024-12-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/2096)
  Qiang Liu, Joon-Woo Lee

  <details><summary>摘要 / Abstract</summary>

  Multi-party Private Set Union (MPSU) enables multiple participants to jointly compute the union of their private sets without leaking any additional information beyond the resulting union. Liu et al. (ASIACRYPT 2023) proposed the first scalable MPSU protocol fully based on symmetric key encryption (SKE), which designates one participant as the &quot;leader&quot; responsible for obtaining the final union. However, the protocol assumes that the leader does not collude with other participants, which weakens its practicality. In this work, we design a scalable MPSU protocol, $\Pi_\text{MPSU}^\text{one-leader}$, which tolerates maximum collusion. The protocol relies primarily on SKE supplemented with additive homomorphic encryption (AHE), with the designated leader obtaining the union result. Furthermore, to address the issue of fairness in scenarios where obtaining the result early provides an advantage, we extend $\Pi_\text{MPSU}^\text{one-leader}$ and propose a protocol that allows all participants to receive the union result simultaneously, called $\Pi_\text{MPSU}^\text{leaderless}$. We implement our proposed schemes and conduct a comprehensive comparison with state-of-the-art solution (Gao et al. PETS 2024) that resist maximum collusion. The results demonstrate that, while our protocol only offers a moderate improvement in runtime, it significantly reduces communication cost by approximately $4$ to $5$ times.

  匹配依据：MPC: private set union

  </details>

- **Constant Degree Networks for Almost-Everywhere Reliable Transmission**
  2024-12-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.00337)
  Mitali Bafna, Dor Minzer

  <details><summary>摘要 / Abstract</summary>

  In the almost-everywhere reliable message transmission problem, introduced by [Dwork, Pippenger, Peleg, Upfal&#x27;86], the goal is to design a sparse communication network $G$ that supports efficient, fault-tolerant protocols for interactions between all node pairs. By fault-tolerant, we mean that that even if an adversary corrupts a small fraction of vertices in $G$, then all but a small fraction of vertices can still communicate perfectly via the constructed protocols. Being successful to do so allows one to simulate, on a sparse graph, any fault-tolerant distributed computing task and secure multi-party computation protocols built for a complete network, with only minimal overhead in efficiency. Previous works on this problem achieved either constant-degree networks tolerating $o(1)$ faults, constant-degree networks tolerating a constant fraction of faults via inefficient protocols (exponential work complexity), or poly-logarithmic degree networks tolerating a constant fraction of faults. We show a construction of constant-degree networks with efficient protocols (i.e., with polylogarithmic work complexity) that can tolerate a constant fraction of adversarial faults, thus solving the main open problem of Dwork et al.. Our main contribution is a composition technique for communication networks, based on graph products. Our technique combines two networks tolerant to adversarial edge-faults to construct a network with a smaller degree while maintaining efficiency and fault-tolerance. We apply this composition result multiple times, using the polylogarithmic-degree edge-fault tolerant networks constructed in a recent work of [Bafna, Minzer, Vyas&#x27;24] (that are based on high-dimensional expanders) with itself, and then with the constant-degree networks (albeit with inefficient protocols) of [Upfal&#x27;92].

  匹配依据：MPC: secure multi party computation

  </details>

- **ClusterGuard: Secure Clustered Aggregation for Federated Learning with Robustness**
  2024-12-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/2082)
  Yulin Zhao, Zhiguo Wan, Zhangshuang Guan, Guannan Li, Miao Guo

  <details><summary>摘要 / Abstract</summary>

  Federated Learning, as a multi-party machine learning paradigm, has garnered significant attention, but model updates may still leak sensitive information. Secure aggregation protocols are considered an effective solution for privacy protection in Federated Learning. However, in large-scale federated learning systems, designing efficient and practical secure aggregation remains a critical challenge. Moreover, while secure aggregation effectively conceals model updates, it unintentionally complicates the detection and mitigation of poisoning attacks, thereby exposing the system to vulnerabilities from both data and model poisoning. To address these challenges, we propose ClusterGuard, a secure clustered aggregation scheme. ClusterGuard leverages Verifiable Random Function (VRF) to ensure fair and transparent client clustering. Within each cluster, it employs a lightweight key-homomorphic masking mechanism combined with verifiable secret sharing to enable secure and efficient aggregation. Furthermore, we design a dual filtering mechanism based on cosine similarity and norm to effectively detect and resist poisoning attacks. We provide two variants of ClusterGuard for both client-server and decentralized environments with blockchains, respectively. Extensive experiments on standard datasets demonstrate that ClusterGuard achieves over $2\times$ efficiency improvement compared to advanced secure aggregation methods. Even with 20% of clients being malicious, the trained model maintains accuracy comparable to the original model, outperforming state-of-the-art robustness solutions. ClusterGuard provides a more efficient, secure, and robust solution for practical federated learning.

  匹配依据：MPC: secret sharing

  </details>

- **An Embedded Domain-Specific Language for Using One-Hot Vectors and Binary Matrices in Secure Computation Protocols**
  2024-12-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/2088)
  Andrei Lapets

  <details><summary>摘要 / Abstract</summary>

  The use of secure computation protocols within production software systems and applications is complicated by the fact that such protocols sometimes rely upon -- or are most compatible with -- unusual or restricted models of computation. We employ the features of a contemporary and widely used programming language to create an embedded domain-specific language for working with user-defined functions as binary matrices that operate on one-hot vectors. At least when working with small finite domains, this allows programmers to overcome the restrictions of more simple secure computation protocols that support only linear operations (such as addition and scalar multiplication) on private inputs. Notably, programmers are able to define their own input and output domains, to use all available host language features and libraries to define functions that operate on these domains, and to translate inputs, outputs, and functions between their usual host language representations and their one-hot vector or binary matrix forms. Furthermore, these features compose in a straightforward way with simple secure computation libraries available for the host language.

  匹配依据：MPC: secure computation

  </details>

- **Succinct Homomorphic MACs from Groups and Applications**
  2024-12-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/2073)
  Yuval Ishai, Hanjun Li, Huijia Lin

  <details><summary>摘要 / Abstract</summary>

  Homomorphic message authentication codes (HMACs) allow users to authenticate data using a shared secret key, while supporting computation over authenticated data. Given data $(m_1, \ldots, m_n)$ and their tags $(\sigma_1, \ldots, \sigma_n)$, anyone can evaluate a circuit $C$ on the data and tags to produce a succinct tag authenticating the output $C(m_1, \ldots, m_n)$. Importantly, tags remain succinc -- of size polynomial in the security parameter $\lambda$ -- regardless of the size of $C$. This work introduces an enhanced variant of HMACs called algebraic HMAC (aHMAC), in which all tags (input and output) take the form $\Delta \cdot m + K$, as in standard information-theoretic MACs. We construct an aHMAC from group-based assumptions, including variants of the DDH and DCR assumptions, and use it to obtain group-based constructions of several cryptographic primitives: - Succinct CDS for circuits. For any $P: [N]^k \to [N]$ represented by circuit, we obtain a Conditional Disclosure of Secrets protocol with poly$(\lambda, k, \log N )$ communication. - Succinct PSM for simple programs. For any $P:[N]^k \to [N]$ represented by a truth-table or shallow branching program, we obtain a Private Simultaneous Messages protocol or a garbling scheme with poly$(\lambda, k, \log N )$ communication. - Constrained PRFs for circuits. We obtain the first group-based constrained pseudorandom functions for general circuits, improving over a previous construction for NC1 circuits. Prior to our work, these applications could only be obtained from lattice assumptions or indistinguishability obfuscation.

  匹配依据：MPC: garbling scheme

  </details>

- **Sneaking up the Ranks: Partial Key Exposure Attacks on Rank-Based Schemes**
  2024-12-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/2070)
  Giuseppe D'Alconzo, Andre Esser, Andrea Gangemi, Carlo Sanna

  <details><summary>摘要 / Abstract</summary>

  A partial key exposure attack is a key recovery attack where an adversary obtains a priori partial knowledge of the secret key, e.g., through side-channel leakage. While for a long time post-quantum cryptosystems, unlike RSA, have been believed to be resistant to such attacks, recent results by Esser, May, Verbel, and Wen (CRYPTO ’22), and by Kirshanova and May (SCN ’22), have refuted this belief. In this work, we focus on partial key exposure attacks in the context of rank-metric-based schemes, particularly targeting the RYDE, MIRA, and MiRitH digital signatures schemes, which are active candidates in the NIST post-quantum cryptography standardization process. We demonstrate that, similar to the RSA case, the secret key in RYDE can be recovered from a constant fraction of its bits. Specifically, for NIST category I parameters, our attacks remain efficient even when less than 25% of the key material is leaked. Interestingly, our attacks lead to a natural improvement of the best generic attack on RYDE without partial knowledge, reducing security levels by up to 9 bits. For MIRA and MiRitH our attacks remain efficient as long as roughly 57%-60% of the secret key material is leaked. Additionally, we initiate the study of partial exposure of the witness in constructions following the popular MPCitH (MPC-in-the-Head) paradigm. We show a generic reduction from recovering RYDE and MIRA’s witness to the MinRank problem, which again leads to efficient key recovery from constant fractions of the secret witness in both cases.

  匹配依据：MPC: mpc (context)

  </details>

- **Perfectly Secure Fluid MPC with Abort and Linear Communication Complexity**
  2024-12-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/2071)
  Alexander Bienstock, Daniel Escudero, Antigoni Polychroniadou

  <details><summary>摘要 / Abstract</summary>

  The \emph{Fluid} multiparty computation (MPC) model, introduced in (Choudhuri \emph{et al.} CRYPTO 2021), addresses dynamic scenarios where participants can join or leave computations between rounds. Communication complexity initially stood at $\Omega(n^2)$ elements per gate, where $n$ is the number of parties in a committee online at a time. This held for both statistical security (honest majority) and computational security (dishonest majority) in (Choudhuri \emph{et al.}~CRYPTO&#x27;21) and (Rachuri and Scholl, CRYPTO&#x27;22), respectively. The work of Bienstock \emph{et al.}~CRYPTO&#x27;23) improved communication to $O(n)$ elements per gate. However, it&#x27;s important to note that the perfectly secure setting with one-third corruptions per committee has only recently been addressed in the work of (David \emph{et al.}~CRYPTO&#x27;23). Notably, their contribution marked a significant advancement in the Fluid MPC literature by introducing guaranteed output delivery. However, this achievement comes at the cost of prohibitively expensive communication, which scales to $\Omega(n^9)$ elements per gate. In this work, we study the realm of perfectly secure Fluid MPC under one-third active corruptions. Our primary focus lies in proposing efficient protocols that embrace the concept of security with abort. Towards this, we design a protocol for perfectly secure Fluid MPC that requires only \emph{linear} communication of $O(n)$ elements per gate, matching the communication of the non-Fluid setting. Our results show that, as in the case of computational and statistical security, perfect security with abort for Fluid MPC comes &quot;for free (asymptotically linear in $n$) with respect to traditional non-Fluid MPC, marking a substantial leap forward in large scale dynamic computations, such as Fluid MPC.

  匹配依据：MPC: multiparty computation

  </details>

- **QKD protected fiber-based infrastructure for time dissemination**
  2024-12-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.17731)
  Alice Meda, Alberto Mura, Salvatore Virzì, Alessio Avella, Filippo Levi, Ivo P. Degiovanni, Andrea Geraldi, Mauro Valeri, Silvia Di Bartolo, Tommaso Catuogno, Mattia Verducci, Marco Genovese, Davide Calonico

  <details><summary>摘要 / Abstract</summary>

  In this study, we demonstrate the possibility to protect, with Quantum Key Distribution (QKD), a critical infrastructure as the fiber-based one used for time and frequency (TF) dissemination service. The proposed technique allows to disseminate secure and precise TF signals between two fiber-opticconnected locations, on a critical infrastructure, using both QKD and White Rabbit technique. This secure exchange allows the secret sharing of time information between two parties for the synchronization of distant clocks with the highest stability and traceable to the Italian time scale. When encrypted, time signals would reveal to a third party no useful information about the synchronization status, providing a time stability two orders of magnitude worsened.

  匹配依据：MPC: secret sharing

  </details>

- **Considerate Ramp Secret Sharing**
  2024-12-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.17987)
  Olav Geil

  <details><summary>摘要 / Abstract</summary>

  In this work we revisit the fundamental findings by Chen et al. in [5] on general information transfer in linear ramp secret sharing schemes to conclude that their method not only gives a way to establish worst case leakage [5, 25] and best case recovery [5, 19], but can also lead to additional insight on non-qualifying sets for any prescribed amount of information. We then apply this insight to schemes defined from monomial-Cartesian codes and by doing so we demonstrate that the good schemes from Sec.\ IV in [14] have a second layer of security. Elaborating further, when given a designed recovery number, in a new construction the focus is entirely on ensuring that the access structure possesses desirable second layer security, rather on what is the worst case information leakage in terms of number of participants.The particular structure of largest possible sets being not able to determine any amount of information suggests that we coin the concept of considerate ramp secret sharing schemes of which the proposed new construction is a well-structured example

  匹配依据：MPC: secret sharing

  </details>

- **gECC: A GPU-based high-throughput framework for Elliptic Curve Cryptography**
  2024-12-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2501.03245)
  Qian Xiong, Weiliang Ma, Xuanhua Shi, Yongluan Zhou, Hai Jin, Kaiyi Huang, Haozhou Wang, Zhengru Wang

  <details><summary>摘要 / Abstract</summary>

  Elliptic Curve Cryptography (ECC) is an encryption method that provides security comparable to traditional techniques like Rivest-Shamir-Adleman (RSA) but with lower computational complexity and smaller key sizes, making it a competitive option for applications such as blockchain, secure multi-party computation, and database security. However, the throughput of ECC is still hindered by the significant performance overhead associated with elliptic curve (EC) operations. This paper presents gECC, a versatile framework for ECC optimized for GPU architectures, specifically engineered to achieve high-throughput performance in EC operations. gECC incorporates batch-based execution of EC operations and microarchitecture-level optimization of modular arithmetic. It employs Montgomery&#x27;s trick to enable batch EC computation and incorporates novel computation parallelization and memory management techniques to maximize the computation parallelism and minimize the access overhead of GPU global memory. Also, we analyze the primary bottleneck in modular multiplication by investigating how the user codes of modular multiplication are compiled into hardware instructions and what these instructions&#x27; issuance rates are. We identify that the efficiency of modular multiplication is highly dependent on the number of Integer Multiply-Add (IMAD) instructions. To eliminate this bottleneck, we propose techniques to minimize the number of IMAD instructions by leveraging predicate registers to pass the carry information and using addition and subtraction instructions (IADD3) to replace IMAD instructions. Our results show that, for ECDSA and ECDH, gECC can achieve performance improvements of 5.56x and 4.94x, respectively, compared to the state-of-the-art GPU-based system. In a real-world blockchain application, we can achieve performance improvements of 1.56x, compared to the state-of-the-art CPU-based system.

  匹配依据：MPC: secure multi party computation

  </details>

- **Anonymous Shamir's Secret Sharing via Reed-Solomon Codes Against Permutations, Insertions, and Deletions**
  2024-12-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.17003)
  Roni Con

  <details><summary>摘要 / Abstract</summary>

  In this work, we study the performance of Reed-Solomon codes against an adversary that first permutes the symbols of the codeword and then performs insertions and deletions. This adversarial model is motivated by the recent interest in fully anonymous secret-sharing schemes [EBG+24],[BGI+24]. A fully anonymous secret-sharing scheme has two key properties: (1) the identities of the participants are not revealed before the secret is reconstructed, and (2) the shares of any unauthorized set of participants are uniform and independent. In particular, the shares of any unauthorized subset reveal no information about the identity of the participants who hold them. In this work, we first make the following observation: Reed-Solomon codes that are robust against an adversary that permutes the codeword and then deletes symbols from the permuted codeword can be used to construct ramp threshold secret-sharing schemes that are fully anonymous. Then, we show that over large enough fields of size, there are $[n,k]$ Reed-Solomon codes that are robust against an adversary that arbitrary permutes the codeword and then performs $n-2k+1$ insertions and deletions to the permuted codeword. This implies the existence of a $(k-1, 2k-1, n)$ ramp secret sharing scheme that is fully anonymous. That is, any $k-1$ shares reveal nothing about the secret, and, moreover, this set of shares reveals no information about the identities of the players who hold them. On the other hand, any $2k-1$ shares can reconstruct the secret without revealing their identities. We also provide explicit constructions of such schemes based on previous works on Reed-Solomon codes correcting insertions and deletions. The constructions in this paper give the first gap threshold secret-sharing schemes that satisfy the strongest notion of anonymity together with perfect reconstruction.

  匹配依据：MPC: secret sharing

  </details>

- **CBNN: 3-Party Secure Framework for Customized Binary Neural Networks Inference**
  2024-12-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.16449)
  Benchang Dong, Zhili Chen, Xin Chen, Shiwen Wei, Jie Fu, Huifa Li

  <details><summary>摘要 / Abstract</summary>

  Binarized Neural Networks (BNN) offer efficient implementations for machine learning tasks and facilitate Privacy-Preserving Machine Learning (PPML) by simplifying operations with binary values. Nevertheless, challenges persist in terms of communication and accuracy in their application scenarios. In this work, we introduce CBNN, a three-party secure computation framework tailored for efficient BNN inference. Leveraging knowledge distillation and separable convolutions, CBNN transforms standard BNNs into MPC-friendly customized BNNs, maintaining high utility. It performs secure inference using optimized protocols for basic operations. Specifically, CBNN enhances linear operations with replicated secret sharing and MPC-friendly convolutions, while introducing a novel secure activation function to optimize non-linear operations. We demonstrate the effectiveness of CBNN by transforming and securely implementing several typical BNN models. Experimental results indicate that CBNN maintains impressive performance even after customized binarization and security measures

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Accelerating Private Large Transformers Inference through Fine-grained Collaborative Computation**
  2024-12-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.16537)
  Yuntian Chen, Zhanyong Tang, Tianpei Lu, Bingsheng Zhang, Zhiying Shi, Zheng Wang

  <details><summary>摘要 / Abstract</summary>

  Homomorphic encryption (HE) and secret sharing (SS) enable computations on encrypted data, providing significant privacy benefits for large transformer-based models (TBM) in sensitive sectors like medicine and finance. However, private TBM inference incurs significant costs due to the coarse-grained application of HE and SS. We present FASTLMPI, a new approach to accelerate private TBM inference through fine-grained computation optimization. Specifically, through the fine-grained co-design of homomorphic encryption and secret sharing, FASTLMPI achieves efficient protocols for matrix multiplication, SoftMax, LayerNorm, and GeLU. In addition, FASTLMPI introduces a precise segmented approximation technique for differentiable non-linear, improving its fitting accuracy while maintaining a low polynomial degree. Compared to solution BOLT (S&amp;P&#x27;24), FASTLMPI shows a remarkable 54% to 64% decrease in runtime and an impressive 72.2% reduction in communication costs.

  匹配依据：MPC: secret sharing

  </details>

- **Zeroed Out: Cryptanalysis of Weak PRFs in Alternating Moduli**
  2024-12-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/2055)
  Irati Manterola Ayala, Håvard Raddum

  <details><summary>摘要 / Abstract</summary>

  The growing adoption of secure multi-party computation (MPC) has driven the development of efficient symmetric key primitives tailored for MPC. Recent advances, such as the alternating moduli paradigm, have shown promise but leave room for cryptographic and practical improvements. In this paper, we analyze a family of weak pseudorandom functions (wPRF) proposed at Crypto 2024, focusing on their One-to-One parameter sets. We demonstrate that these configurations fail to achieve their intended one-to-one mappings and exploit this observation to develop an efficient key recovery attack. Our analysis reveals critical vulnerabilities, reducing the complexity of key recovery to $\mathcal{O}(2^{\lambda/2} \log_2 \lambda)$ for the Standard One-to-One wPRF and $\mathcal{O}(2^{0.84\lambda})$ for the Reversed Moduli variant -- both substantially below their claimed $\lambda$-bit security. We validate our findings through experimental evaluation, confirming alignment between predicted and observed attack complexities.

  匹配依据：MPC: secure multi party computation

  </details>

- **Minimizing the Use of the Honest Majority in YOSO MPC with Guaranteed Output Delivery**
  2024-12-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/2059)
  Rishabh Bhadauria, James Hsin-yu Chiang, Divya Ravi, Jure Sternad, Sophia Yakoubov

  <details><summary>摘要 / Abstract</summary>

  Cleve (STOC 86) shows that an honest majority is necessary for MPC with guaranteed output delivery. In this paper, we show that while an honest majority is indeed necessary, its involvement can be minimal. We demonstrate an MPC protocol with guaranteed output delivery, the majority of which is executed by a sequence of committees with dishonest majority; we leverage one committee with an honest majority, each member of which does work independent of the circuit size. Our protocol has the desirable property that every participant speaks only once (YOSO, Crypto 2021). As a building block of independent interest, we introduce public computation, which is essentially privacy-free MPC with guaranteed output delivery (akin to smart contracts realized on blockchains). We instantiate public computation on a public bulletin board in three different ways (with different assumption / round / space utilization trade-offs).

  匹配依据：MPC: mpc (context)

  </details>

- **SeaSearch: Secure and Efficient Selection Queries**
  2024-12-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/2041)
  Shantanu Sharma, Yin Li, Sharad Mehrotra, Nisha Panwar, Komal Kumari, Swagnik Roychoudhury

  <details><summary>摘要 / Abstract</summary>

  Information-theoretic or unconditional security provides the highest level of security --- independent of the computational capability of an adversary. Secret-sharing techniques achieve information-theoretic security by splitting a secret into multiple parts (called shares) and storing the shares across non-colluding servers. However, secret-sharing-based solutions suffer from high overheads due to multiple communication rounds among servers and/or information leakage due to access-patterns (i.e.., the identity of rows satisfying a query) and volume (i.e., the number of rows satisfying a query). We propose SeaSearch, an information-theoretically secure approach that uses both additive and multiplicative secret-sharing, to efficiently support a large class of selection queries involving conjunctive, disjunctive, and range conditions. Two major contributions of SeaSearch are: (i) a new search algorithm using additive shares based on fingerprints, which were developed for string-matching over cleartext; and (ii) two row retrieval algorithms: one is based on multiplicative shares and another is based on additive shares. SeaSearch does not require communication among servers storing shares and does not reveal any information to an adversary based on access-patterns and volume.

  匹配依据：MPC: secret sharing

  </details>

- **Multilateral Trade Credit Set-off in MPC via Graph Anonymization and Network Simplex**
  2024-12-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/2037)
  Enrico Bottazzi, Chan Nam Ngo, Masato Tsutsumi

  <details><summary>摘要 / Abstract</summary>

  Multilateral Trade Credit Set-off (MTCS) is a process run by a service provider that collects trade credit data (i.e. obligations from a firm to pay another firm) from a network of firms and detects cycles of debts that can be removed from the system. The process yields liquidity savings for the participants, who can discharge their debts without relying on expensive loans. We propose an MTCS protocol that protects firms&#x27; sensitive data, such as the obligation amount or the identity of the firms they trade with. Mathematically, this is analogous to solving the Minimum Cost Flow (MCF) problem over a graph of $n$ firms, where the $m$ edges are the obligations. State-of-the-art techniques for Secure MCF have an overall complexity of $O(n^{10} \log n)$ communication rounds, making it barely applicable even to small-scale instances. Our solution leverages novel secure techniques such as Graph Anonymization and Network Simplex to reduce the complexity of the MCF problem to $O(max(n, \log\log{n+m}))$ rounds of interaction per pivot operations in which $O(max(n^2, nm))$ comparisons and multiplications are performed. Experimental results show the tradeoff between privacy and optimality.

  匹配依据：MPC: mpc (context)

  </details>

- **Security and Fairness in Multi-Party Quantum Secret Sharing Protocol**
  2024-12-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.11667)
  Alessio Di Santo, Walter Tiberti, Dajana Cassioli

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) is a cryptographic protocol that leverages quantum mechanics to distribute a secret among multiple parties. With respect to the classical counterpart, in QSS the secret is encoded into quantum states and shared by a dealer such that only an authorized subsets of participants, i.e., the players, can reconstruct it. Several state-of-the-art studies aim to transpose classical Secret Sharing into the quantum realm, while maintaining their reliance on traditional network topologies (e.g., star, ring, fully-connected) and require that all the n players calculate the secret. These studies exploit the Greenberger-Horne-Zeilinger (GHZ) state, which is a type of maximally entangled quantum state involving three or more qubits. However, none of these works account for redundancy, enhanced security/privacy features or authentication mechanisms able to fingerprint players. To address these gaps, in this paper we introduce a new concept of QSS which leans on a generic distributed quantum-network, based on a threshold scheme, where all the players collaborate also to the routing of quantum information among them. The dealer, by exploiting a custom flexible weighting system, takes advantage of a newly defined quantum Dijkstra algorithm to select the most suitable subset of t players, out of the entire set on n players, to involve in the computation. To fingerprint and authenticate users, CRYSTAL-Kyber primitives are adopted, while also protecting each player&#x27;s privacy by hiding their identities. We show the effectiveness and performance of the proposed protocol by testing it against the main classical and quantum attacks, thereby improving the state-of-the-art security measures.

  匹配依据：MPC: secret sharing

  </details>

- **Carousel: Fully Homomorphic Encryption with Bootstrapping over Automorphism Group**
  2024-12-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/2032)
  Intak Hwang, Seonhong Min, Yongsoo Song

  <details><summary>摘要 / Abstract</summary>

  Homomorphic Encryption (HE) enables the secure computation of functions on ciphertexts without requiring decryption. Specifically, AP-like HE schemes exploit an intrinsic bootstrapping method called blind rotation. In existing blind rotation methods, a look-up table is homomorphically evaluated on the input ciphertext through iterative multiplication of monomials. However, the algebraic structure of the multiplicative group of monomials imposes certain limitations on the input plaintext space, as it can bootstrap only a fraction of the input plaintext space. In this work, we introduce a new HE scheme, Carousel, that solves this problem. The key idea of our approach is to utilize the automorphism group instead of monomials. More specifically, the look-up table is encoded into a single polynomial that can be rotated via a series of homomorphic multiplications and automorphisms. We instantiate Carousel with subring encoding proposed by Arita and Handa (ICISC &#x27;17) and provide a proof-of-concept implementation. Our benchmark result shows that Carousel can bootstrap 4-bit integers in under 30ms.

  匹配依据：MPC: secure computation

  </details>

- **CENTAUR: Bridging the Impossible Trinity of Privacy, Efficiency, and Performance in Privacy-Preserving Transformer Inference**
  2024-12-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.10652)
  Jinglong Luo, Guanzhong Chen, Yehong Zhang, Shiyu Liu, Hui Wang, Yue Yu, Xun Zhou, Yuan Qi, Zenglin Xu

  <details><summary>摘要 / Abstract</summary>

  With the growing deployment of pre-trained models like Transformers on cloud platforms, privacy concerns about model parameters and inference data are intensifying. Existing Privacy-Preserving Transformer Inference (PPTI) frameworks face the &quot;impossible trinity&quot; of balancing privacy, efficiency, and performance: Secure Multi-Party Computation (SMPC)-based approaches ensure strong privacy but suffer from high computational overhead and performance losses; Conversely, permutation-based methods achieve near-plaintext efficiency and accuracy but compromise privacy by exposing sensitive model parameters and intermediate results. Bridging this gap with a single approach presents substantial challenges, motivating the introduction of CENTAUR, a groundbreaking PPTI framework that seamlessly integrates random permutations and SMPC to address the &quot;impossible trinity&quot;. By designing efficient PPTI algorithms tailored to the structural properties of Transformer models, CENTAUR achieves an unprecedented balance among privacy, efficiency, and performance. Our experiments demonstrate CENTAUR&#x27;s ability to resist diverse data reconstruction attacks, achieve plaintext-level inference accuracy, and boost inference speed by 5.0-30.4 times, unlocking new possibilities for secure and efficient AI deployment.

  匹配依据：MPC: secure multi party computation

  </details>

- **Ring Ring! Who's There? A Privacy Preserving Mobile Number Search**
  2024-12-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/2020)
  Akshit Aggarwal

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) allows any two parties (say client and server) to jointly compute the intersection of their sets without revealing anything else. Fully homomorphic encryption (FHE)-based PSI is a cryptographic solution to implement PSI-based protocols. Most FHE-based PSI protocols implement hash function approach and oblivious transfer approach. The main limitations of their protocols are 1) high communication complexity, that is, $O(xlogy)$ (where $x$ is total number of elements on client side, and $y$ is total number of elements on server side), and 2) high memory usage due to SIMD packing for encrypting large digit numbers. In this work, we design a novel tree-based approach to store the large digit numbers that achieves less communication complexity, that is, $O(|d|^{2})$ (where $d$ is digits of a mobile number). Later we implement our protocol using Tenseal library. Our designed protocol opens the door to find the common elements with less communication complexity and less memory usage.

  匹配依据：MPC: oblivious transfer, private set intersection

  </details>

- **PrivQuant: Communication-Efficient Private Inference with Quantized Network/Protocol Co-Optimization**
  2024-12-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.09531) · [IACR ePrint](https://eprint.iacr.org/2024/2021)
  Tianshi Xu, Shuzhang Zhong, Wenxuan Zeng, Runsheng Wang, Meng Li

  <details><summary>摘要 / Abstract</summary>

  Private deep neural network (DNN) inference based on secure two-party computation (2PC) enables secure privacy protection for both the server and the client. However, existing secure 2PC frameworks suffer from a high inference latency due to enormous communication. As the communication of both linear and non-linear DNN layers reduces with the bit widths of weight and activation, in this paper, we propose PrivQuant, a framework that jointly optimizes the 2PC-based quantized inference protocols and the network quantization algorithm, enabling communication-efficient private inference. PrivQuant proposes DNN architecture-aware optimizations for the 2PC protocols for communication-intensive quantized operators and conducts graph-level operator fusion for communication reduction. Moreover, PrivQuant also develops a communication-aware mixed precision quantization algorithm to improve the inference efficiency while maintaining high accuracy. The network/protocol co-optimization enables PrivQuant to outperform prior-art 2PC frameworks. With extensive experiments, we demonstrate PrivQuant reduces communication by $11\times, 2.5\times \mathrm{and}~ 2.8\times$, which results in $8.7\times, 1.8\times ~ \mathrm{and}~ 2.4\times$ latency reduction compared with SiRNN, COINN, and CoPriv, respectively.

  匹配依据：MPC: secure two party computation

  </details>

- **A Survey on Private Transformer Inference**
  2024-12-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.08145)
  Yang Li, Xinyu Zhou, Yitong Wang, Liangxin Qian, Jun Zhao

  <details><summary>摘要 / Abstract</summary>

  Transformer models have revolutionized AI, enabling applications like content generation and sentiment analysis. However, their use in Machine Learning as a Service (MLaaS) raises significant privacy concerns, as centralized servers process sensitive user data. Private Transformer Inference (PTI) addresses these issues using cryptographic techniques such as Secure Multi-Party Computation (MPC) and Homomorphic Encryption (HE), enabling secure model inference without exposing inputs or models. This paper reviews recent advancements in PTI, analyzing state-of-the-art solutions, their challenges, and potential improvements. We also propose evaluation guidelines to assess resource efficiency and privacy guarantees, aiming to bridge the gap between high-performance inference and data privacy.

  匹配依据：MPC: secure multi party computation

  </details>

- **A New Federated Learning Framework Against Gradient Inversion Attacks**
  2024-12-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.07187) · [Code](https://github.com/Pengxin-Guo/HyperFL)
  Pengxin Guo, Shuang Zeng, Wenhao Chen, Xiaodan Zhang, Weihong Ren, Yuyin Zhou, Liangqiong Qu

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) aims to protect data privacy by enabling clients to collectively train machine learning models without sharing their raw data. However, recent studies demonstrate that information exchanged during FL is subject to Gradient Inversion Attacks (GIA) and, consequently, a variety of privacy-preserving methods have been integrated into FL to thwart such attacks, such as Secure Multi-party Computing (SMC), Homomorphic Encryption (HE), and Differential Privacy (DP). Despite their ability to protect data privacy, these approaches inherently involve substantial privacy-utility trade-offs. By revisiting the key to privacy exposure in FL under GIA, which lies in the frequent sharing of model gradients that contain private data, we take a new perspective by designing a novel privacy preserve FL framework that effectively ``breaks the direct connection&#x27;&#x27; between the shared parameters and the local private data to defend against GIA. Specifically, we propose a Hypernetwork Federated Learning (HyperFL) framework that utilizes hypernetworks to generate the parameters of the local model and only the hypernetwork parameters are uploaded to the server for aggregation. Theoretical analyses demonstrate the convergence rate of the proposed HyperFL, while extensive experimental results show the privacy-preserving capability and comparable performance of HyperFL. Code is available at https://github.com/Pengxin-Guo/HyperFL.

  匹配依据：MPC: secure multi party computing

  </details>

- **Revisiting OKVS-based OPRF and PSI: Cryptanalysis and Better Construction**
  2024-12-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1989)
  Kyoohyung Han, Seongkwang Kim, Byeonghak Lee, Yongha Son

  <details><summary>摘要 / Abstract</summary>

  Oblivious pseudorandom function (OPRF) is a two-party cryptographic protocol that allows the receiver to input $x$ and learn $F(x)$ for some PRF $F$, only known to the sender. For private set intersection (PSI) applications, OPRF protocols have evolved to enhance efficiency, primarily using symmetric key cryptography. Current state-of-the-art protocols, such as those by Rindal and Schoppmann (Eurocrypt &#x27;21), leverage vector oblivious linear evaluation (VOLE) and oblivious key-value store (OKVS) constructions. In this work, we identify a flaw in an existing security proof, and present practical attacks in the malicious model, which results in additional PRF evaluations than the previous works&#x27; claim. In particular, the attack for malicious model is related to the concept of OKVS overfitting, whose hardness is conjectured in previous works. Our attack is the first one to discuss the concrete hardness of OKVS overfitting problem. As another flavour of contribution, we generalize OKVS-based OPRF constructions, suggesting new instantiations using a VOLE protocol with only Minicrypt assumptions. Our generalized construction shows improved performance in high-speed network environments, narrowing the efficiency gap between the OPRF constructions over Cryptomania and Minicrypt.

  匹配依据：MPC: private set intersection

  </details>

- **Lightweight Federated Learning with Differential Privacy and Straggler Resilience**
  2024-12-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.06120)
  Shu Hong, Xiaojun Lin, Lingjie Duan

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) enables collaborative model training through model parameter exchanges instead of raw data. To avoid potential inference attacks from exchanged parameters, differential privacy (DP) offers rigorous guarantee against various attacks. However, conventional methods of ensuring DP by adding local noise alone often result in low training accuracy. Combining secure multi-party computation (SMPC) with DP, while improving the accuracy, incurs high communication and computation overheads as well as straggler vulnerability, in either client-to-server or client-to-client links. In this paper, we propose LightDP-FL, a novel lightweight scheme that ensures provable DP against untrusted peers and server, while maintaining straggler resilience, low overheads and high training accuracy. Our scheme incorporates both individual and pairwise noise into each client&#x27;s parameter, which can be implemented with minimal overheads. Given the uncertain straggler and colluder sets, we utilize the upper bound on the numbers of stragglers and colluders to prove sufficient noise variance conditions to ensure DP in the worst case. Moreover, we optimize the expected convergence bound to ensure accuracy performance by flexibly controlling the noise variances. Using the CIFAR-10 dataset, our experimental results demonstrate that LightDP-FL achieves faster convergence and stronger straggler resilience compared to baseline methods of the same DP level.

  匹配依据：MPC: secure multi party computation

  </details>

- **How To Scale Multi-Party Computation**
  2024-12-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1990)
  Marcel Keller

  <details><summary>摘要 / Abstract</summary>

  We propose a solution for optimized scaling of multi-party computation using the MP-SPDZ framework (CCS’20). It does not use manual optimization but extends the compiler and the virtual machine of the framework, thus providing an improvement for any user. We found that our solution improves timings four-fold for a simple example in MP-SPDZ, and it improves an order of magnitude on every framework using secret sharing considered by Hastings et al. (S&amp;P’19) either in terms of time or RAM usage. The core of our approach is finding a balance between communication round optimization and memory usage.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Batch effects can impair federated learning in multi-center omics studies**
  2024-12-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.05894)
  Yuliya Burankova, Julian Klemm, Jens J. G. Lohmann, Anne Hartebrodt, Ahmad Taheri, Niklas Probul, Jan Baumbach, Olga Zolotareva

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) enables collaborative analysis of biomedical data without exchanging sensitive patient-level information, but its performance in multi-center studies may be compromised by batch effects which can obscure biological signals. Here, we systematically assess the impact of uncorrected batch effects on FL outcomes using four multi-center omics datasets, including transcriptomic, proteomic, and metabolomic data, and two representative algorithms: federated k-means clustering and federated random forest classification. Our results demonstrate that uncorrected batch effects undermine unsupervised FL and can substantially degrade supervised FL performance, indicating that privacy-aware batch-effect correction is essential for reliable FL. To enable privacy-preserving BEC in distributed bulk omics data, we introduce fedRBE ( https://featurecloud.ai/app/fedrbe ), a federated implementation of limma&#x27;s removeBatchEffect() method enhanced by secure multi-party computation, suitable for datasets with missing values and non-identical feature sets across clients, including proteomics and metabolomics data.

  匹配依据：MPC: secure multi party computation

  </details>

- **µLAM: A LLM-Powered Assistant for Real-Time Micro-architectural Attack Detection and Mitigation**
  2024-12-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1978)
  Upasana Mandal, Shubhi Shukla, Ayushi Rastogi, Sarani Bhattacharya, Debdeep Mukhopadhyay

  <details><summary>摘要 / Abstract</summary>

  The rise of microarchitectural attacks has necessitated robust detection and mitigation strategies to secure computing systems. Traditional tools, such as static and dynamic code analyzers and attack detectors, often fall short due to their reliance on predefined patterns and heuristics that lack the flexibility to adapt to new or evolving attack vectors. In this paper, we introduce for the first time a microarchitecture security assistant, built on OpenAI&#x27;s GPT-3.5, which we refer to as µLAM. This assistant surpasses conventional tools by not only identifying vulnerable code segments but also providing context-aware mitigations, tailored to specific system specifications and existing security measures. Additionally, µLAM leverages real-time data from dynamic Hardware Performance Counters (HPCs) and system specifications to detect ongoing attacks, offering a level of adaptability and responsiveness that static and dynamic analyzers cannot match. For fine-tuning µLAM, we utilize a comprehensive dataset that includes system configurations, mitigations already in place for different generations of systems, dynamic HPC values, and both vulnerable and non-vulnerable source codes. This rich dataset enables µLAM to harness its advanced LLM natural language processing capabilities to understand and interpret complex code patterns and system behaviors, learning continuously from new data to improve its predictive accuracy and respond effectively in real time to both known and novel threats, making it an indispensable tool against microarchitectural threats. In this paper, we demonstrate the capabilities of µLAM by fine-tuning and testing it on code utilizing well-known cryptographic libraries such as OpenSSL, Libgcrypt, and NaCl, thereby illustrating its effectiveness in securing critical and complex software environments.

  匹配依据：MPC: secure computing

  </details>

- **Privately Compute the Item with Maximal Weight Sum in Set Intersection**
  2024-12-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1973)
  Hongyuan Cai, Xiaodong Wang, Zijie Lu, Bei Liang

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection (PSI) is a cryptographic primitive that allows two parties to obtain the intersection of their private input sets while revealing nothing more than the intersection. PSI and its numerous variants, which compute on the intersection of items and their associated weights, have been widely studied. In this paper, we revisit the problem of finding the best item in the intersection according to weight sum introduced by Beauregard et al. (SCN &#x27;22), which is a special variant of PSI. We present two new protocols that achieve the functionality. The first protocol is based on Oblivious Pseudorandom Function (OPRF), additively homomorphic encryption and symmetric-key encryption, while the second one is based on Decisional Diffie-Hellman (DDH) assumption, additively homomorphic encryption and symmetric-key encryption. Both protocols are proven to be secure against semi-honest adversaries. Compared with the original protocol proposed by Beauregard et al. (abbreviated as the FOCI protocol), which requires all weights in the input sets to be polynomial in magnitude, our protocols remove this restriction. We compare the performance of our protocols with the FOCI protocol both theoretically and empirically. We find out that the performance of FOCI protocol is primarily affected by the size of the intersection and the values of elements’ weights in intersection when fixing set size, while the performance of ours is independent of these two factors. In particular, in the LAN setting, when the set sizes are $n=10000$, intersection size of $\frac{n}{2}$, the weights of the elements are uniformly distributed as integers from $\left[0, n-1\right]$, our DDH-based protocol has a similar run-time to the FOCI protocol. However, when the weights of the elements belonging to $\left[0, 10n-1\right]$ and $\left[0, 100n-1\right]$, our DDH-based protocol is between a factor $2\times$ and $5\times$ faster than the FOCI protocol.

  匹配依据：MPC: private set intersection

  </details>

- **Efficient and Practical Multi-party Private Set Intersection Cardinality Protocol**
  2024-12-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1974)
  Shengzhe Meng, Xiaodong Wang, Zijie Lu, Bei Liang

  <details><summary>摘要 / Abstract</summary>

  We present an efficient and simple multi-party private set intersection cardinality (PSI-CA) protocol that allows several parties to learn the intersection size of their private sets without revealing any other information. Our protocol is highly efficient because it only utilizes the Oblivious Key-Value Store and zero-sharing techniques, without incorporating components such as OPPRF (Oblivious Programmable Pseudorandom Function) which is the main building block of multi-party PSI-CA protocol by Gao et al. (PoPETs 2024). Our protocol exhibits better communication and computational overhead than the state-of-the-art. To compute the intersection between 16 parties with a set size of $2^{20}$ each, our PSI-CA protocol only takes 5.84 seconds and 326.6 MiB of total communication, which yields a reduction in communication by a factor of up to 2.4× compared to the state-of-the-art multi-party PSI-CA protocol of Gao et al. (PoPETs 2024). We prove that our protocol is secure in the presence of a semi-honest adversary who may passively corrupt any $(t-2)$-out-of-$t$ parties once two specific participants are non-colluding.

  匹配依据：MPC: private set intersection

  </details>

- **Privacy-Preserving in Medical Image Analysis: A Review of Methods and Applications**
  2024-12-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.03924)
  Yanming Zhu, Xuefei Yin, Alan Wee-Chung Liew, Hui Tian

  <details><summary>摘要 / Abstract</summary>

  With the rapid advancement of artificial intelligence and deep learning, medical image analysis has become a critical tool in modern healthcare, significantly improving diagnostic accuracy and efficiency. However, AI-based methods also raise serious privacy concerns, as medical images often contain highly sensitive patient information. This review offers a comprehensive overview of privacy-preserving techniques in medical image analysis, including encryption, differential privacy, homomorphic encryption, federated learning, and generative adversarial networks. We explore the application of these techniques across various medical image analysis tasks, such as diagnosis, pathology, and telemedicine. Notably, we organizes the review based on specific challenges and their corresponding solutions in different medical image analysis applications, so that technical applications are directly aligned with practical issues, addressing gaps in the current research landscape. Additionally, we discuss emerging trends, such as zero-knowledge proofs and secure multi-party computation, offering insights for future research. This review serves as a valuable resource for researchers and practitioners and can help advance privacy-preserving in medical image analysis.

  匹配依据：MPC: secure multi party computation

  </details>

- **Teaching an Old Dog New Tricks: Verifiable FHE Using Commodity Hardware**
  2024-12-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.03550)
  Jules Drean, Fisher Jepsen, Edward Suh, Srini Devadas, Aamer Jaleel, Gururaj Saileshwar

  <details><summary>摘要 / Abstract</summary>

  We present Argos, a simple approach for adding verifiability to fully homomorphic encryption (FHE) schemes using trusted hardware. Traditional approaches to verifiable FHE require expensive cryptographic proofs, which incur an overhead of up to seven orders of magnitude on top of FHE, making them impractical. With Argos, we show that trusted hardware can be securely used to provide verifiability for FHE computations, with minimal overhead relative to the baseline FHE computation. An important contribution of Argos is showing that the major security pitfall associated with trusted hardware, microarchitectural side channels, can be completely mitigated by excluding any secrets from the CPU and the memory hierarchy. This is made possible by focusing on building a platform that only enforces program and data integrity and not confidentiality. All secrets related to the attestation mechanism are kept in a separate coprocessor (e.g., a TPM)-inaccessible to any software-based attacker. Relying on a discrete TPM typically incurs significant performance overhead, which is why (insecure) software-based TPMs are used in practice. As a second contribution, we show that for FHE applications, the attestation protocol can be adapted to only incur a fixed cost. Argos requires no dedicated hardware extensions and is supported on commodity processors from 2008 onward. Our prototype implementation introduces 3% overhead for FHE evaluation, and 8% for more complex protocols. In particular, we show that Argos can be used for real-world applications of FHE, such as private information retrieval (PIR) and private set intersection (PSI), where providing verifiability is imperative. By demonstrating how to combine cryptography with trusted hardware, Argos paves the way for widespread deployment of FHE-based protocols beyond the semi-honest setting, without the overhead of cryptographic proofs.

  匹配依据：MPC: private set intersection

  </details>

- **End to End Collaborative Synthetic Data Generation**
  2024-12-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.03766)
  Sikha Pentyala, Geetha Sitaraman, Trae Claar, Martine De Cock

  <details><summary>摘要 / Abstract</summary>

  The success of AI is based on the availability of data to train models. While in some cases a single data custodian may have sufficient data to enable AI, often multiple custodians need to collaborate to reach a cumulative size required for meaningful AI research. The latter is, for example, often the case for rare diseases, with each clinical site having data for only a small number of patients. Recent algorithms for federated synthetic data generation are an important step towards collaborative, privacy-preserving data sharing. Existing techniques, however, focus exclusively on synthesizer training, assuming that the training data is already preprocessed and that the desired synthetic data can be delivered in one shot, without any hyperparameter tuning. In this paper, we propose an end-to-end collaborative framework for publishing of synthetic data that accounts for privacy-preserving preprocessing as well as evaluation. We instantiate this framework with Secure Multiparty Computation (MPC) protocols and evaluate it in a use case for privacy-preserving publishing of synthetic genomic data for leukemia.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Efficient Succinct Zero-Knowledge Arguments in the CL Framework**
  2024-12-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1966)
  Agathe Beaugrand, Guilhem Castagnos, Fabien Laguillaumie

  <details><summary>摘要 / Abstract</summary>

  The CL cryptosystem, introduced by Castagnos and Laguillaumie in 2015, is a linearly homomorphic encryption scheme that has seen numerous developments and applications in recent years, particularly in the field of secure multiparty computation. Designing efficient zero-knowledge proofs for the CL framework is critical, especially for achieving adaptive security for such multiparty protocols. This is a challenging task due to the particularities of class groups of quadratic fields used to instantiate the groups of unknown order required in the CL framework. In this work, we provide efficient proofs and arguments for statements involving a large number of ciphertexts. We propose a new batched proof for correctness of CL ciphertexts and new succinct arguments for correctness of a shuffle of these ciphertexts. Previous efficient proofs of shuffle for linearly homomorphic encryption were designed for Elgamal “in the exponent” which has only a limited homomorphic property. In the line of a recent work by Braun, Damgard and Orlandi (CRYPTO 2023), all the new proofs and arguments provide partial extractability, a property that we formally introduce here. Thanks to this notion, we show that bulletproof techniques, which are in general implemented with groups of known prime order, can be applied in the CL framework despite the use of unknown order groups, giving non interactive arguments of logarithmic sizes. To prove the practicability of our approach we have implemented these protocols with the BICYCL library, showing that computation and communication costs are competitive. We also illustrate that the partial extractability of our proofs provide enough guarantees for complex applications by presenting a bipartite private set intersection sum protocol which achieves security against malicious adversaries using CL encryption, removing limitations of a solution proposed by Miao et al. (CRYPTO 2020).

  匹配依据：MPC: private set intersection, secure multiparty computation

  </details>

- **GRAND : Graph Reconstruction from potential partial Adjacency and Neighborhood Data**
  2024-12-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.02329)
  Sofiane Azogagh, Zelma Aubin Birba, Josée Desharnais, Sébastien Gambs, Marc-Olivier Killijian, Nadia Tawbi

  <details><summary>摘要 / Abstract</summary>

  Cryptographic approaches, such as secure multiparty computation, can be used to compute in a secure manner the function of a distributed graph without centralizing the data of each participant. However, the output of the protocol itself can leak sensitive information about the structure of the original graph. In particular, in this work we propose an approach by which an adversary observing the result of a private protocol for the computation of the number of common neighbors between all pairs of vertices, can reconstruct the adjacency matrix of the graph. In fact, this can only be done up to co-squareness, a notion we introduce, as two different graphs can have the same matrix of common neighbors. We consider two models of adversary, one who observes the common neighbors matrix only, and a knowledgeable one, that has a partial knowledge of the original graph. Our results demonstrate that secure multiparty protocols are not enough for privacy protection, especially in the context of highly structured data such as graphs. The reconstruction that we propose is interesting in itself from the point of view of graph theory.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Two-Round 2PC ECDSA at the Cost of 1 OLE**
  2024-12-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1950)
  Michael Adjedj, Constantin Blokh, Geoffroy Couteau, Arik Galansky, Antoine Joux, Nikolaos Makriyannis

  <details><summary>摘要 / Abstract</summary>

  We present a novel protocol for two-party ECDSA that achieves two rounds (a single back-and-forth communication) at the cost of a single oblivious linear function evaluation (OLE). In comparison, the previous work of Boneh et al.~(EUROCRYPT 2025) achieves two rounds but requires expensive zero-knowledge proofs on top of the OLE. We demonstrate this by proving that in the generic group model, any adversary capable of generating forgeries for our protocol can be transformed into an adversary that finds preimages for the ECDSA message digest function (e.g., the SHA family). Interestingly, our analysis is closely related to, and has ramifications for, the `presignatures&#x27; mode of operation---Canetti et al.~(CCS 2020), Groth and Shoup (EUROCRYPT 2022). Motivated by applications to embedded cryptocurrency wallets, where a single server maintains distinct, shared public keys with separate clients (i.e., a star-shaped topology), and with the goal of minimizing communication, we instantiate our protocol using Paillier encryption and suitable zero-knowledge proofs. To reduce computational overhead, we thoroughly optimize all components of our protocol under sound cryptographic assumptions, specifically small-exponent variants of RSA-style assumptions. Finally, we implement our protocol and provide benchmarks. At the 128-bit security level, the signing phase requires approximately 50ms of computation time on a standard linux machine, and 2KB of bandwidth.

  匹配依据：MPC: 2pc (context)

  </details>

- **Truncation Untangled: Scaling Fixed-Point Arithmetic for Privacy-Preserving Machine Learning to Large Models and Datasets**
  2024-12-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1953)
  Christopher Harth-Kitzerow, Ajith Suresh, Georg Carle

  <details><summary>摘要 / Abstract</summary>

  Fixed Point Arithmetic (FPA) is widely used in Privacy-Preserving Machine Learning (PPML) to efficiently handle decimal values. However, repeated multiplications in FPA can lead to overflow, as the fractional part doubles in size with each multiplication. To address this, truncation is applied post-multiplication to maintain precision. Various truncation schemes based on Secure Multiparty Computation (MPC) exist, but trade-offs between accuracy and efficiency in PPML models and datasets remain underexplored. In this work, we analyze and consolidate different truncation approaches from the MPC literature. We conduct the first large-scale systematic evaluation of PPML inference accuracy across truncation schemes, ring sizes, neural network architectures, and datasets. Our study provides clear guidelines for selecting the optimal truncation scheme and parameters for PPML inference. All evaluations are implemented in the open-source HPMPC MPC framework, facilitating future research and adoption. Beyond our large scale evaluation, we also present improved constructions for each truncation scheme, achieving up to a fourfold reduction in communication and round complexity over existing schemes. Additionally, we introduce optimizations tailored for PPML, such as strategically fusing different neural network layers. This leads to a mixed-truncation scheme that balances truncation costs with accuracy, eliminating communication overhead in the online phase while matching the accuracy of plaintext floating-point PyTorch inference for VGG-16 on the ImageNet dataset.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Quantum Scheme for Private Set Intersection and Union Cardinality based on Quantum Homomorphic Encryption**
  2024-12-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.01032)
  Chong-Qiang Ye, Jian Li, Tianyu Ye, Xiaoyu Chen

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) and private set union (PSU) are the crucial primitives in secure multiparty computation protocols, which enable several participants to jointly compute the intersection and union of their private sets without revealing any additional information. Quantum homomorphic encryption (QHE) offers significant advantages in handling privacy-preserving computations. However, given the current limitations of quantum resources, developing efficient and feasible QHE-based protocols for PSI and PSU computations remains a critical challenge. In this work, a novel quantum private set intersection and union cardinality protocol is proposed, accompanied by the corresponding quantum circuits. Based on quantum homomorphic encryption, the protocol allows the intersection and union cardinality of users&#x27; private sets to be computed on quantum-encrypted data with the assistance of a semi-honest third party. By operating on encrypted quantum states, it effectively mitigates the risk of original information leakage. Furthermore, the protocol requires only simple Pauli and CNOT operations, avoiding the use of complex quantum manipulations (e.g., $T$ gate and phase rotation gate). Compared to related protocols, this approach offers advantages in feasibility and privacy protection.

  匹配依据：MPC: private set intersection, private set union, secure multiparty computation

  </details>

- **Implementing Semiclassical Szegedy Walks in Classical-Quantum Circuits for Homomorphic Encryption**
  2024-12-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.01966)
  Sergio A. Ortega, Pablo Fernández, Miguel A. Martin-Delgado

  <details><summary>摘要 / Abstract</summary>

  As cloud services continue to expand, the security of private data stored and processed in these environments has become paramount. This work delves into quantum homomorphic encryption (QHE), an emerging technology that facilitates secure computation on encrypted quantum data without revealing the underlying information. We reinterpret QHE schemes through classical-quantum circuits, enhancing efficiency and addressing previous limitations related to key computations. Our approach eliminates the need for exponential key preparation by calculating keys in real-time during simulation, leading to a linear complexity in classically controlled gates. We also investigate the $T/T^{\dagger}$-gate complexity associated with various quantum walks, particularly Szegedy quantum and semiclassical algorithms, demonstrating efficient homomorphic implementations across different graph structures. Our simulations, conducted in Qiskit, validate the effectiveness of QHE for both standard and semiclassical walks. The rules for the homomorphic evaluation of the reset and intermediate measurement operations have also been included to perform the QHE of semiclassical walks. Additionally, we introduce the CQC-QHE library, a comprehensive tool that simplifies the construction and simulation of classical-quantum circuits tailored for quantum homomorphic encryption. Future work will focus on optimizing classical functions within this framework and exploring broader graph types to enhance QHE applications in practical scenarios.

  匹配依据：MPC: secure computation

  </details>

- **Gold OPRF: Post-Quantum Oblivious Power-Residue PRF**
  2024-12-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1955)
  Yibin Yang, Fabrice Benhamouda, Shai Halevi, Hugo Krawczyk, Tal Rabin

  <details><summary>摘要 / Abstract</summary>

  We propose plausible post-quantum (PQ) oblivious pseudorandom functions (OPRFs) based on the Power-Residue PRF (Damgård CRYPTO’88), a generalization of the Legendre PRF. For security parameter $\lambda$, we consider the PRF $\mathsf{Gold}_k(x)$ that maps an integer $x$ modulo a public prime $p = 2^\lambda\cdot g + 1$ to the element $(k + x)^g \bmod p$, where $g$ is public and $\log g \approx 2\lambda$. At the core of our constructions are efficient novel methods for evaluating $\mathsf{Gold}$ within two-party computation ($\mathsf{2PC}\text{-}\mathsf{Gold}$), achieving different security requirements. Here, the server $\mathcal{P}_s$ holds the PRF key $k$ whereas the client $\mathcal{P}_c$ holds the PRF input $x$, and they jointly evaluate $\mathsf{Gold}$ in 2PC. $\mathsf{2PC}\text{-}\mathsf{Gold}$ uses standard Vector Oblivious Linear Evaluation (VOLE) correlations and is information-theoretic and constant-round in the (V)OLE-hybrid model. We show: • For a semi-honest $\mathcal{P}_s$ and a malicious $\mathcal{P}_c$: a $\mathsf{2PC}\text{-}\mathsf{Gold}$ that just uses a single (V)OLE correlation, and has a communication complexity of $3$ field elements ($2$ field elements if we only require a uniformly sampled key) and a computational complexity of $\mathcal{O}(\lambda)$ field operations. We refer to this as half-malicious security. • For malicious $\mathcal{P}_s$ and $\mathcal{P}_c$: a $\mathsf{2PC}\text{-}\mathsf{Gold}$ that just uses $\frac{\lambda}{4} + \mathcal{O}(1)$ VOLE correlations, and has a communication complexity of $\frac{\lambda}{4} + \mathcal{O}(1)$ field elements and a computational complexity of $\mathcal{O}(\lambda)$ field operations. These constructions support additional features and extensions, e.g., batched evaluations with better amortized costs where $\mathcal{P}_c$ repeatedly evaluates the PRF under the same key. Furthermore, we extend $\mathsf{2PC}\text{-}\mathsf{Gold}$ to Verifiable OPRFs and use the methodology from Beullens et al. (ePrint’24) to obtain strong OPRF security in the universally composable setting. All the protocols are efficient in practice. We implemented $\mathsf{2PC}\text{-}\mathsf{Gold}$—with (PQ) VOLEs—and benchmarked them. For example, our half-malicious (resp. malicious) $n$-batched PQ OPRFs incur about $100$B (resp. $1.9$KB) of amortized communication for $\lambda = 128$.

  匹配依据：MPC: two party computation

  </details>

- **Towards Privacy-Preserving Medical Imaging: Federated Learning with Differential Privacy and Secure Aggregation Using a Modified ResNet Architecture**
  2024-12-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.00687)
  Mohamad Haj Fares, Ahmed Mohamed Saad Emam Saad

  <details><summary>摘要 / Abstract</summary>

  With increasing concerns over privacy in healthcare, especially for sensitive medical data, this research introduces a federated learning framework that combines local differential privacy and secure aggregation using Secure Multi-Party Computation for medical image classification. Further, we propose DPResNet, a modified ResNet architecture optimized for differential privacy. Leveraging the BloodMNIST benchmark dataset, we simulate a realistic data-sharing environment across different hospitals, addressing the distinct privacy challenges posed by federated healthcare data. Experimental results indicate that our privacy-preserving federated model achieves accuracy levels close to non-private models, surpassing traditional approaches while maintaining strict data confidentiality. By enhancing the privacy, efficiency, and reliability of healthcare data management, our approach offers substantial benefits to patients, healthcare providers, and the broader healthcare ecosystem.

  匹配依据：MPC: secure multi party computation

  </details>

- **Preserving Privacy in Software Composition Analysis: A Study of Technical Solutions and Enhancements**
  2024-12-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.00898)
  Huaijin Wang, Zhibo Liu, Yanbo Dai, Shuai Wang, Qiyi Tang, Sen Nie, Shi Wu

  <details><summary>摘要 / Abstract</summary>

  Software composition analysis (SCA) denotes the process of identifying open-source software components in an input software application. SCA has been extensively developed and adopted by academia and industry. However, we notice that the modern SCA techniques in industry scenarios still need to be improved due to privacy concerns. Overall, SCA requires the users to upload their applications&#x27; source code to a remote SCA server, which then inspects the applications and reports the component usage to users. This process is privacy-sensitive since the applications may contain sensitive information, such as proprietary source code, algorithms, trade secrets, and user data. Privacy concerns have prevented the SCA technology from being used in real-world scenarios. Therefore, academia and the industry demand privacy-preserving SCA solutions. For the first time, we analyze the privacy requirements of SCA and provide a landscape depicting possible technical solutions with varying privacy gains and overheads. In particular, given that de facto SCA frameworks are primarily driven by code similarity-based techniques, we explore combining several privacy-preserving protocols to encapsulate the similarity-based SCA framework. Among all viable solutions, we find that multi-party computation (MPC) offers the strongest privacy guarantee and plausible accuracy; it, however, incurs high overhead (184 times). We optimize the MPC-based SCA framework by reducing the amount of crypto protocol transactions using program analysis techniques. The evaluation results show that our proposed optimizations can reduce the MPC-based SCA overhead to only 8.5% without sacrificing SCA&#x27;s privacy guarantee or accuracy.

  匹配依据：MPC: multi party computation

  </details>

- **Distributed Differentially Private Data Analytics via Secure Sketching**
  2024-11-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.00497) · [IACR ePrint](https://eprint.iacr.org/2024/1946)
  Jakob Burkhardt, Hannah Keller, Claudio Orlandi, Chris Schwiegelshohn

  <details><summary>摘要 / Abstract</summary>

  We introduce the linear-transformation model, a distributed model of differentially private data analysis. Clients have access to a trusted platform capable of applying a public matrix to their inputs. Such computations can be securely distributed across multiple servers using simple and efficient secure multiparty computation techniques. The linear-transformation model serves as an intermediate model between the highly expressive central model and the minimal local model. In the central model, clients have access to a trusted platform capable of applying any function to their inputs. However, this expressiveness comes at a cost, as it is often prohibitively expensive to distribute such computations, leading to the central model typically being implemented by a single trusted server. In contrast, the local model assumes no trusted platform, which forces clients to add significant noise to their data. The linear-transformation model avoids the single point of failure for privacy present in the central model, while also mitigating the high noise required in the local model. We demonstrate that linear transformations are very useful for differential privacy, allowing for the computation of linear sketches of input data. These sketches largely preserve utility for tasks such as private low-rank approximation and private ridge regression, while introducing only minimal error, critically independent of the number of clients.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Free Linear Online Phase for Secure Multiparty Shuffle**
  2024-11-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1936)
  Jiacheng Gao, Yuan Zhang, Sheng Zhong, Changyu Dong

  <details><summary>摘要 / Abstract</summary>

  Shuffling is a fundamental operation in secure multiparty computation (MPC), yet existing maliciously secure protocols for shuffling $m$ elements among $n$ parties require at least $n^2m$ online communication and computation, compared with $O(nm)$ in the semi-honest additive-sharing setting. We formalize and extend the \emph{permute-in-turn paradigm}, which constructs MPC shuffles from permutation protocols, capturing the methodology adopted in most prior works. Our generic transformations achieve semi-honest or malicious security with only $O(C_{\mathrm{BC}}+nm)$ online communication and computation, where $C_{\mathrm{BC}}$ is the cost of one parallel broadcast (allowing unanimous abort). Our transformations are \emph{for free} in two senses: they yield linear online phases without exceeding the overall asymptotic cost of applying $n$ MPC permutations, while \emph{freeing} the online phase of the shuffle protocol from dependence on the MPC permutation protocol. This decoupling allows future work to optimize permutation protocols independently while benefiting all MPC shuffle protocols that follow the paradigm. Instantiated with additive and Shamir secret sharing, our transformations yield the first maliciously secure shuffles with $O(C_{\mathrm{BC}}+nm)$ online cost, improving previous bounds of $O(Bn^2m)$ and $O(n^2m\log m)$, respectively, where $B$ is a cut-and-choose parameter. We formally prove semi-honest and universally composable (UC) security for the corresponding transformations. For $m=2^{12}$ and $n=15$, our prototype achieves over $60\times$ lower online runtime and $120\times$ lower online communication than prior work, with only a $1.3\times$ increase in total runtime.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **MULTISS: Long-Term Secure Distributed Storage over Remote QKD Networks**
  2024-11-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1915)
  Thomas Prévost, Olivier Alibart, Anne Marin, Marc Kaplan, Pascal Lafourcade, Charles Olivier-Anclin

  <details><summary>摘要 / Abstract</summary>

  We introduce MULTISS, a distributed storage protocol over multiple remote Quantum Key Distribution (QKD) networks that ensures long-term data confidentiality. MULTISS is designed to combine several QKD networks, as QKD links are inherently limited in range, and to connect these networks through classical cryptographic channels. It relies on a hierarchical secret sharing scheme that makes certain shares mandatory for the reconstruction of the original secret. Hence, MULTISS offers a secure distributed storage solution in a scenario that is compatible with the current deployment of quantum networks. We prove that MULTISS preserves the confidentiality of stored data even if an adversary (i) gains full access to all nodes of a subset of the QKD networks, or (ii) records all classical communications between distant QKD networks and compromises them at a later stage. We show that it provides strictly stronger security guarantees than existing QKD-storage protocols. Our protocol also includes a procedure to update the shares without reconstructing the original data. In addition, we provide a recovery mechanism that tolerates the complete compromise of some QKD networks. We further introduce a variant of the protocol, called the local-mode, that minimizes the communication overhead of the recovery procedure when deployed over specific network topologies.

  匹配依据：MPC: secret sharing

  </details>

- **Towards Optimal Garbled Circuits in the Standard Model**
  2024-11-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1907)
  Ruiyang Li, Chun Guo, Xiao Wang

  <details><summary>摘要 / Abstract</summary>

  State-of-the-art garbling schemes for boolean circuits roughly consist of two families, i.e., ideal model garbling that combines linear operations and ideal blockciphers (aiming at maximizing performance), and PRF-based garbling that insists on using theoretically sound assumptions. In the linear garbling framework introduced by Zahur, Rosulek, and Evans (Eurocrypt 2015), it was established that garbling an AND gate requires at least $2(\kappa +1)$ bits of ciphertext, with $\kappa$ as the security parameter. Recent contributions from Lei Fan et al. and Chunghun Baek et al. have provided a detailed model showing that, under the free-XOR setting, which relies on a non-standard assumption, garbling an AND gate requires at least $1.5\kappa + O(1)$ bits. In contrast, regarding PRF-based garbling, the general model and efficiency bounds remain open questions. In this paper, we present a comprehensive model for PRF-based garbled circuits and establish both the communication and computation lower bound. Specifically, we demonstrate that garbling an AND gate requires at least $2\kappa + 2$ bits communication and 6 PRF calls, while an XOR gate requires a minimum of $\kappa$ bits communication and 4 PRF calls. Notably, the state-of-the-art garbling scheme (GLNP scheme) under the PRF assumption, introduced by Shay, Yehuda, Ariel, and Benny (JOC 2018), uses $2\kappa + 4$ bits and 8 PRF calls for an AND gate, which exceeds our established lower bound. We finally introduce an optimal garbling scheme showing that our communication and computation lower bounds are tight.

  匹配依据：MPC: garbled circuits, garbling scheme, garbling schemes

  </details>

- **SilentWood: Efficient Private Inference Over Gradient-Boosting Decision Forests**
  2024-11-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.15494)
  Ronny Ko, Abdelkarim Kati, Robin Geelen, Rasoul Akhavan Mahdavi, Byoungwoo Yoon, Jongho Shin, Zhiqiang Lin, Makoto Onizuka, Florian Kerschbaum

  <details><summary>摘要 / Abstract</summary>

  Gradient boosting decision forests, used by XGBoost or AdaBoost, offer higher accuracy and lower training times than decision trees on large datasets. Private inference protocols for decision trees can preserve both input and tree privacy. However, naively extending them to decision forests by replication leads to impractical running times. In this paper, we propose an efficient private decision inference protocol using homomorphic encryption. We present several optimizations that identify and remove (approximate) duplication between trees, significantly reducing communication and computation costs over the naive approach. We present the private inference protocol for highly scalable gradient boosting decision forests. Our protocol SilentWood is faster than parallel RCC-PDTE by up to 42.5x, Zama&#x27;s Concrete ML XGBoost by up to 27.8x, and SoK-GGG&#x27;s two-party garbled circuit protocol by 2.94x.

  匹配依据：MPC: garbled circuit

  </details>

- **On the Insecurity of Bloom Filter-Based Private Set Intersections**
  2024-11-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1901)
  Jelle Vos, Jorrit van Assen, Tjitske Koster, Evangelia Anna Markatou, Zekeriya Erkin

  <details><summary>摘要 / Abstract</summary>

  Private set intersections are cryptographic protocols that compute the intersection of multiple parties&#x27; private sets without revealing elements that are not in the intersection. These protocols become less efficient when the number of parties grows, or the size of the sets increases. For this reason, many protocols are based on Bloom filters, which speed up the protocol by approximating the intersections, introducing false positives with a small but non-negligible probability. These false positives are caused by hash collisions in the hash functions that parties use to encode their sets as Bloom filters. In this work, we show that these false positives are more than an inaccuracy: an adversary in the augmented semi-honest model can use them to learn information about elements that are not in the intersection. First, we show that existing security proofs for Bloom filter-based private set intersections are flawed. Second, we show that even in the most optimistic setting, Bloom filter-based private set intersections cannot securely realize an approximate private set intersection unless the parameters are so large that false positives only occur with negligible probability. Third, we propose a practical attack that allows a party to learn if an element is contained in a victim&#x27;s private set, showing that the problem with Bloom filters is not just theoretical. We conclude that the efficiency gain of using Bloom filters as an approximation in existing protocols vanishes when accounting for this security problem. We propose three mitigations besides choosing larger parameters: One can use oblivious pseudo-random functions instead of hash functions to reduce the success rate of our attack significantly, or replace them with password-based key derivation functions to significantly slow down attackers. A third option is to let a third party authorize the input sets before proceeding with the protocol.

  匹配依据：MPC: private set intersection

  </details>

- **On Threshold Signatures from MPC-in-the-Head**
  2024-11-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1897)
  Eliana Carozza, Geoffroy Couteau

  <details><summary>摘要 / Abstract</summary>

  We investigate the feasibility of constructing threshold signature schemes from the MPC-in-the-head paradigm. Our work addresses the significant challenge posed by recent impossibility results (Doerner et al., Crypto’24), which establish inherent barriers to efficient thresholdization of such schemes without compromising their security or significantly increasing the signature size. - We introduce a general methodology to adapt any MPC-in-the-head signature into a threshold-friendly scheme, ensuring that the dependency on the number of users $n$ grows as $\lambda^2n + O(1)$. This represents a substantial improvement over the naive concatenation of independent signatures. - We present a threshold signature scheme on top of the scheme of (Carozza, Couteau and Joux, EUROCRYPT’23). Our security analysis introduces the notion of Corruptible Existential Unforgeability under Chosen Message Attacks (CEUF-CMA), which formalizes resilience against adversarial control over parts of the randomness. Our results provide a new perspective on the trade-offs between efficiency and security in threshold settings, opening pathways for future improvements in post-quantum threshold cryptography.

  匹配依据：MPC: mpc (context)

  </details>

- **Constructing Multipartite Planar Maximally Entangled States from Phase States and Quantum Secret Sharing Protocol**
  2024-11-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.15077)
  Lahoucine Bouhouch, Yassine Dakir, Abdallah Slaoui, Rachid Ahl Laamara

  <details><summary>摘要 / Abstract</summary>

  In this paper, we explore the construction of Planar Maximally Entangled (PME) states from phase states. PME states form a class of $n$-partite states in which any subset of adjacent particles whose size is less than or equal to half the total number of particles is in a fully entangled state. This property is essential to ensuring the robustness and stability of PME states in various quantum information applications. We introduce phase states for a set of so-called noninteracting $n$ particles and describe their corresponding separable density matrices. These phase states, although individually separable, serve as a starting point for the generation of entangled states when subjected to unitary dynamics. Using this method, we suggest a way to make complex multi-qubit states by watching how unconnected phase states change over time with a certain unitary interaction operator. In addition, we show how to derive PME states from these intricate phase states for two-, three-, four-, and K-qubit systems. This construction method for PME states represents a significant advance over absolutely maximally entangled (AME) states, as it provides a more accessible and versatile resource for quantum information processing. Not only does it enable the creation of a broader class of multipartite entangled states, overcoming the limitations of AME states, notably their restricted availability in low-dimensional systems; for example, the absence of a four-qubit AME state, but it also offers a systematic construction method for any even number of qudits, paving the way for practical applications in key quantum technologies such as teleportation, secret sharing and error correction, where multipartite entanglement plays a central role in protocol efficiency.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Power Flow Analysis via Secure Multi-Party Computation**
  2024-11-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.14557)
  Jonas von der Heyden, Nils Schlüter, Philipp Binfet, Martin Asman, Markus Zdrallek, Tibor Jager, Moritz Schulze Darup

  <details><summary>摘要 / Abstract</summary>

  Smart grids feature a bidirectional flow of electricity and data, enhancing flexibility, efficiency, and reliability in increasingly volatile energy grids. However, data from smart meters can reveal sensitive private information. Consequently, the adoption of smart meters is often restricted via legal means and hampered by limited user acceptance. Since metering data is beneficial for fault-free grid operation, power management, and resource allocation, applying privacy-preserving techniques to smart metering data is an important research problem. This work addresses this by using secure multi-party computation (SMPC), allowing multiple parties to jointly evaluate functions of their private inputs without revealing the latter. Concretely, we show how to perform power flow analysis on cryptographically hidden prosumer data. More precisely, we present a tailored solution to the power flow problem building on an SMPC implementation of Newtons method. We analyze the security of our approach in the universal composability framework and provide benchmarks for various grid types, threat models, and solvers. Our results indicate that secure multi-party computation can be able to alleviate privacy issues in smart grids in certain applications.

  匹配依据：MPC: secure multi party computation

  </details>

- **The weight hierarchy of decreasing norm-trace codes**
  2024-11-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.13375)
  Eduardo Camps-Moreno, Hiram H. López, Gretchen L. Matthews, Rodrigo San-José

  <details><summary>摘要 / Abstract</summary>

  The Generalized Hamming weights and their relative version, which generalize the minimum distance of a linear code, are relevant to numerous applications, including coding on the wire-tap channel of type II, $t$-resilient functions, bounding the cardinality of the output in list decoding algorithms, ramp secret sharing schemes, and quantum error correction. The generalized Hamming weights have been determined for some families of codes, including Cartesian codes and Hermitian one-point codes. In this paper, we determine the generalized Hamming weights of decreasing norm-trace codes, which are linear codes defined by evaluating monomials that are closed under divisibility on the rational points of the extended norm-trace curve given by $x^{u} = y^{q^{s - 1}} + y^{q^{s - 2}} + \cdots + y$ over the finite field of cardinality $q^s$, where $u$ is a positive divisor of $\frac{q^s - 1}{q - 1}$. As a particular case, we obtain the weight hierarchy of one-point norm-trace codes and recover the result of Barbero and Munuera (2001) giving the weight hierarchy of one-point Hermitian codes. We also study the relative generalized Hamming weights for these codes and use them to construct impure quantum codes with excellent parameters.

  匹配依据：MPC: secret sharing

  </details>

- **Single Trace Side-Channel Attack on the MPC-in-the-Head Framework**
  2024-11-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1882)
  Julie Godard, Nicolas Aragon, Philippe Gaborit, Antoine Loiseau, Julien Maillard

  <details><summary>摘要 / Abstract</summary>

  In this paper, we present the first single trace side-channel attack that targets the MPC-in-the-Head (MPCitH) framework based on threshold secret sharing, also known as Threshold Computation in the Head (TCitH) in its original version. This MPCitH framework can be found in 5 of the 14 digital signatures schemes in the recent second round of the National Institute of Standards and Technology (NIST) call for digital signatures. In this work, we start by highlighting a side-channel vulnerability of the TCitH framework and show an exploitation of it on the SDitH algorithm, which is part of this NIST call. Specifically, we exploit the leakage of a multiplication function in the Galois field to make predictions about intermediate values, and we use the structure of the algorithm to combine information efficiently. This allows us to build an attack that is both the first Soft Analytical Side-Channel Attack (SASCA) targeting the MPCitH framework, as well as the first attack on SDitH. More specifically, we build a SASCA based on Belief Propagation (BP) on the evaluation of polynomials in the signature using the threshold variant structure to reconstruct the secret key. We perform simulated attacks under the Hamming Weight (HW) leakage model, enabling us to evaluate the resistance of the scheme against SASCA. We then perform our attacks in a real case scenario, more specifically on the STM32F407, and recover the secret key for all the security levels. We end this paper by discussing the various shuffling countermeasures we could use to mitigate our attacks.

  匹配依据：MPC: secret sharing

  </details>

- **HW/SW Implementation of MiRitH on Embedded Platforms**
  2024-11-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.12328)
  Maximilian Schöffel, Hiandra Tomasi, Norbert Wehn

  <details><summary>摘要 / Abstract</summary>

  Multi-Party Computation in the Head (MPCitH) algorithms are appealing candidates in the additional US NIST standardization rounds for Post-Quantum Cryptography (PQC) with respect to key sizes and mathematical hardness assumptions. However, their complexity presents a significant challenge for platforms with limited computational capabilities. To address this issue, we present, to the best of our knowledge, the first design space exploration of MiRitH, a promising MPCitH algorithm, for embedded devices. We develop a library of mixed HW/SW blocks on the Xilinx ZYNQ 7000, and, based on this library, we explore optimal solutions under runtime or FPGA resource constraints for a given public key infrastructure. Our results show that MiRitH is a viable algorithm for embedded devices in terms of runtime and FPGA resource requirements.

  匹配依据：MPC: multi party computation

  </details>

- **Resonance: Transaction Fees for Heterogeneous Computation**
  2024-11-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.11789)
  Maryam Bahrani, Naveen Durvasula

  <details><summary>摘要 / Abstract</summary>

  Blockchain networks are facing increasingly heterogeneous computational demands, and in response, protocol designers have started building specialized infrastructure to supply that demand. This paper introduces Resonance: a new kind of transaction fee mechanism for the general two-sided market setting (with users on one side and nodes on the other), where both sides of the market exhibit a high degree of heterogeneity. We allow users submitting transactions to have arbitrary valuations for inclusion, nodes responsible for executing transactions to incur arbitrary costs for running any bundle of transactions, and further allow for arbitrary additional constraints on what allocations are valid. These constraints can, for example, be used to prevent state conflicts by requiring transactions that utilize the same part of the network&#x27;s state to not be executed in parallel. They also enable support for new transaction types, such as transactions that require multiple nodes for execution (e.g. to run multi-party computation for better transaction privacy). Resonance&#x27;s design utilizes competition among sophisticated brokers to find individualized prices for each transaction and node. We show that at pure Nash equilibria, Resonance finds an efficient outcome and minimizes the need for strategization by users and nodes. It is also budget-balanced, individually rational for all parties, and computationally tractable.

  匹配依据：MPC: multi party computation

  </details>

- **The Communication-Friendly Privacy-Preserving Machine Learning against Malicious Adversaries**
  2024-11-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.09287)
  Tianpei Lu, Bingsheng Zhang, Lichun Li, Kui Ren

  <details><summary>摘要 / Abstract</summary>

  With the increasing emphasis on privacy regulations, such as GDPR, protecting individual privacy and ensuring compliance have become critical concerns for both individuals and organizations. Privacy-preserving machine learning (PPML) is an innovative approach that allows for secure data analysis while safeguarding sensitive information. It enables organizations to extract valuable insights from data without compromising privacy. Secure multi-party computation (MPC) is a key tool in PPML, as it allows multiple parties to jointly compute functions without revealing their private inputs, making it essential in multi-server environments. We address the performance overhead of existing maliciously secure protocols, particularly in finite rings like $\mathbb{Z}_{2^\ell}$, by introducing an efficient protocol for secure linear function evaluation. We implement our maliciously secure MPC protocol on GPUs, significantly improving its efficiency and scalability. We extend the protocol to handle linear and non-linear layers, ensuring compatibility with a wide range of machine-learning models. Finally, we comprehensively evaluate machine learning models by integrating our protocol into the workflow, enabling secure and efficient inference across simple and complex models, such as convolutional neural networks (CNNs).

  匹配依据：MPC: secure multi party computation

  </details>

- **Non-interactive Fully Encrypted Machine Learning Protocol for Inference**
  2024-11-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1859)
  Seungwan Hong, Jiseung Kim, Changmin Lee, Minhye Seo

  <details><summary>摘要 / Abstract</summary>

  As privacy concerns have arisen in machine learning, privacy-preserving machine learning (PPML) has received significant attention. Fully homomorphic encryption (FHE) and secure multi-party computation (MPC) are representative building blocks for PPML. However, in PPML protocols based on FHE and MPC, interaction between the client (who provides encrypted input data) and the evaluator (who performs the computation) is essential to obtain the final result in plaintext. Functional encryption (FE) is a promising candidate to remove this constraint, but existing FE-based PPML protocols are restricted to evaluating only simple ML models, such as one-layer neural networks, or they support partially encrypted PPML, which makes them vulnerable to information leakage beyond the inference results. In this paper, we propose a fully encrypted FE-based PPML protocol, which supports the evaluation of arbitrary functions over encrypted data with no information leakage during computation, for the first time. To achieve this, {we introduce a new functional encryption scheme for quadratic polynomials, in which the encryption algorithm is realized as a linear function with respect to a message. This structural property allows for the composition of the encryption algorithm with arbitrary quadratic functions, thereby enabling multiple compositions of quadratic polynomials to compute arbitrary complex functions in an encrypted manner. Our FE-based PPML protocol is secure in the malicious model, which means that an adversary cannot obtain any information about the input data even though they intentionally deviate from the protocol. We then show how to use our protocol to build a fully encrypted 2-layer neural network model with quadratic activation functions and present experimental results.

  匹配依据：MPC: secure multi party computation

  </details>

- **(In)Security of Threshold Fully Homomorphic Encryption based on Shamir Secret Sharing**
  2024-11-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1858)
  Wonhee Cho, Jiseung Kim, Changmin Lee

  <details><summary>摘要 / Abstract</summary>

  Boneh et al. (CRYPTO&#x27;18) proposed two $t$-out-of-$N$ threshold fully homomorphic encryption ($\sf TFHE$) schemes based on Shamir secret sharing scheme and $\{0,1\}$-linear secret sharing scheme. They demonstrated the simulation security, ensuring no information leakage during partial or final decryption. This breakthrough allows any scheme to be converted into a threshold scheme by using $\sf TFHE$. We propose two polynomial time algorithms to break the simulation security of $t$-out-of-$N$ $\sf TFHE$ based on Shamir secret sharing scheme proposed by Boneh et al.. First, we show that an adversary can break the simulation security by recovering the secret key under some constraints on $t$ and $N$, which does not violate the conditions for security proof. Next, we introduce a straightforward fix that theoretically satisfies the simulation security. However, we argue that this modification remains insecure insecure when implemented with any state-of-the-art fully homomorphic encryption libraries in practice. To ensure robustness against our subsequent attacks, we recommend using an error-refreshing algorithm, such as bootstrapping or modulus switching, for each addition operation.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Verifiable Neural Network Inference Service**
  2024-11-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.07468)
  Arman Riasi, Jorge Guajardo, Thang Hoang

  <details><summary>摘要 / Abstract</summary>

  Machine learning has revolutionized data analysis and pattern recognition, but its resource-intensive training has limited accessibility. Machine Learning as a Service (MLaaS) simplifies this by enabling users to delegate their data samples to an MLaaS provider and obtain the inference result using a pre-trained model. Despite its convenience, leveraging MLaaS poses significant privacy and reliability concerns to the client. Specifically, sensitive information from the client inquiry data can be leaked to an adversarial MLaaS provider. Meanwhile, the lack of a verifiability guarantee can potentially result in biased inference results or even unfair payment issues. While existing trustworthy machine learning techniques, such as those relying on verifiable computation or secure computation, offer solutions to privacy and reliability concerns, they fall short of simultaneously protecting the privacy of client data and providing provable inference verifiability. In this paper, we propose vPIN, a privacy-preserving and verifiable CNN inference scheme that preserves privacy for client data samples while ensuring verifiability for the inference. vPIN makes use of partial homomorphic encryption and commit-and-prove succinct non-interactive argument of knowledge techniques to achieve desirable security properties. In vPIN, we develop various optimization techniques to minimize the proving circuit for homomorphic inference evaluation thereby, improving the efficiency and performance of our technique. We fully implemented and evaluated our vPIN scheme on standard datasets (e.g., MNIST, CIFAR-10). Our experimental results show that vPIN achieves high efficiency in terms of proving time, verification time, and proof size, while providing client data privacy guarantees and provable verifiability.

  匹配依据：MPC: secure computation

  </details>

- **Will Central Bank Digital Currencies (CBDC) and Blockchain Cryptocurrencies Coexist in the Post Quantum Era?**
  2024-11-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.06362)
  Abraham Itzhak Weinberg, Pythagoras Petratos, Alessio Faccia

  <details><summary>摘要 / Abstract</summary>

  This paper explores the coexistence possibilities of Central Bank Digital Currencies (CBDCs) and blockchain-based cryptocurrencies within a post-quantum computing landscape. It examines the implications of emerging quantum algorithms and cryptographic techniques such as Multi-Party Computation (MPC) and Oblivious Transfer (OT). While exploring how CBDCs and cryptocurrencies might integrate defenses like post-quantum cryptography, it highlights the substantial hurdles in transitioning legacy systems and fostering widespread adoption of new standards. The paper includes comprehensive evaluations of CBDCs in a quantum context. It also features comparisons to alternative cryptocurrency models. Additionally, the paper provides insightful analyses of pertinent quantum methodologies. Examinations of interfaces between these methods and blockchain architectures are also included. The paper carries out considered appraisals of quantum threats and their relevance for cryptocurrency schemes. Furthermore, it features discussions of the influence of anticipated advances in quantum computing on algorithms and their applications. The paper renders the judicious conclusion that long-term coexistence is viable provided challenges are constructively addressed through ongoing collaborative efforts to validate solutions and guide evolving policies.

  匹配依据：MPC: multi party computation, oblivious transfer

  </details>

- **Private Neural Network Training with Packed Secret Sharing**
  2024-11-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1833)
  Hengcheng Zhou

  <details><summary>摘要 / Abstract</summary>

  We present a novel approach for training neural networks that leverages packed Shamir secret sharing scheme. For specific training protocols based on Shamir scheme, we demonstrate how to realize the conversion between packed sharing and Shamir sharing without additional communication overhead. We begin by introducing a method to locally convert between Shamir sharings with secrets stored at different slots. Building upon this conversion, we achieve free conversion from packed sharing to Shamir sharing. We then show how to embed the conversion from Shamir sharing to packed sharing into the truncation used during the training process without incurring additional communication costs. With free conversion between packed sharing and Shamir sharing, we illustrate how to utilize the packed scheme to parallelize certain computational steps involved in neural network training. On this basis, we propose training protocols with information-theoretic security between general $n$ parties under the semi-honest model. The experimental results demonstrate that, compared to previous work in this domain, applying the packed scheme can effectively improve training efficiency. Specifically, when packing $4$ secrets into a single sharing, we observe a reduction of more than $20\%$ in communication overhead and an improvement of over $10\%$ in training speed under the WAN setting.

  匹配依据：MPC: secret sharing

  </details>

- **Hybrid Zero-Knowledge from Garbled Circuits**
  2024-11-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1835)
  Masayuki Abe, Miguel Ambrona, Miyako Ohkubo

  <details><summary>摘要 / Abstract</summary>

  We present techniques for constructing zero-knowledge argument systems from garbled circuits, extending the GC-to-ZK compiler by Jawurek, Kerschbaum, and Orlandi (ACM CCS 2023) and the GC-to-Σ compiler by Hazay and Venkitasubramaniam (J. Crypto, 2020) to the following directions: - Our schemes are hybrid, commit-and-prove zero-knowledge argument systems that establish a connection between secrets embedded in algebraic commitments and a relation represented by a Boolean circuit. - Our schemes incorporate diverse cross-domain secrets embedded within distinct algebraic commitments, simultaneously supporting Pedersen-like commitments and lattice-based commitments. As an application, we develop circuit-represented compositions of Σ-protocols that support attractive access structures, such as weighted thresholds, that can be easily represented by a small circuit. For predicates P1, . . . , Pn individually associated with a Σ-protocol, and a predicate C represented by a Boolean circuit, we construct a Σ-protocol for proving C(P1, . . . , Pn) = 1. This result answers positively an open question posed by Abe, et. al., at TCC 2021.

  匹配依据：MPC: garbled circuits

  </details>

- **Experimental Secure Multiparty Computation from Quantum Oblivious Transfer with Bit Commitment**
  2024-11-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.04558)
  Kai-Yi Zhang, An-Jing Huang, Kun Tu, Ming-Han Li, Chi Zhang, Wei Qi, Ya-Dong Wu, Yu Yu

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation enables collaborative computations across multiple users while preserving individual privacy, which has a wide range of applications in finance, machine learning and healthcare. Secure multiparty computation can be realized using oblivious transfer as a primitive function. In this paper, we present an experimental implementation of a quantum-secure quantum oblivious transfer (QOT) protocol using an adapted quantum key distribution system combined with a bit commitment scheme, surpassing previous approaches only secure in the noisy storage model. We demonstrate the first practical application of the QOT protocol by solving the private set intersection, a prime example of secure multiparty computation, where two parties aim to find common elements in their datasets without revealing any other information. In our experiments, two banks can identify common suspicious accounts without disclosing any other data. This not only proves the experimental functionality of QOT, but also showcases its real-world commercial applications.

  匹配依据：MPC: oblivious transfer, private set intersection, secure multiparty computation

  </details>

- **Succinct Randomized Encodings from Laconic Function Evaluation, Faster and Simpler**
  2024-11-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1815)
  Nir Bitansky, Rachit Garg

  <details><summary>摘要 / Abstract</summary>

  Succinct randomized encodings allow encoding the input $x$ of a time-$t$ uniform computation $M(x)$ in sub-linear time $o(t)$. The resulting encoding $\tilde{x}$ allows recovering the result of the computation $M(x)$, but hides any other information about $x$. These encodings have powerful applications, including time-lock puzzles, reducing communication in MPC, and bootstrapping advanced encryption schemes. Until not long ago, the only known constructions were based on indistinguishability obfuscation, and in particular were not based on standard post-quantum assumptions. In terms of efficiency, these constructions&#x27; encoding time is $\rm{polylog}(t)$, essentially the best one can hope for. Recently, a new construction was presented based on Circular Learning with Errors, an assumption similar to the one used in fully-homomorphic encryption schemes, and which is widely considered to be post-quantum resistant. However, the encoding efficiency significantly falls behind obfuscation-based scheme and is $\approx \sqrt{t} \cdot s$, where $s$ is the space of the computation. We construct, under the same assumption, succinct randomized encodings with encoding time $\approx t^{\varepsilon} \cdot s$ for arbitrarily small constant $\varepsilon&lt;1$. Our construction is relatively simple, generic and relies on any laconic function evaluation scheme that satisfies a natural &quot;efficiency preservation&quot; property. Under sub-exponential assumptions, the encoding time can be further reduced to $\approx \sqrt{s}$, but at the account of a huge security loss. As a corollary, assuming also bounded-space languages that are worst-case hard-to-parallelize, we obtain time-lock puzzles with an arbitrary polynomial gap between encoding and decoding times.

  匹配依据：MPC: mpc (context)

  </details>

- **On the Power of Oblivious State Preparation**
  2024-11-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.04234) · [IACR ePrint](https://eprint.iacr.org/2024/1820)
  James Bartusek, Dakshita Khurana

  <details><summary>摘要 / Abstract</summary>

  We put forth Oblivious State Preparation (OSP) as a cryptographic primitive that unifies techniques developed in the context of a quantum server interacting with a classical client. OSP allows a classical polynomial-time sender to input a choice of one out of two public observables, and a quantum polynomial-time receiver to recover an eigenstate of the corresponding observable -- while keeping the sender&#x27;s choice hidden from any malicious receiver. We obtain the following results: - The existence of (plain) trapdoor claw-free functions implies OSP, and the existence of dual-mode trapdoor claw-free functions implies round-optimal (two-round) OSP. - OSP implies the existence of proofs of quantumness, test of a qubit, blind classical delegation of quantum computation, and classical verification of quantum computation. - Two-round OSP implies quantum money with classical communication, classically-verifiable position verification, and (additionally assuming classical FHE with log-depth decryption) quantum FHE. Thus, the OSP abstraction helps separate the cryptographic layer from the information-theoretic layer when building cryptosystems across classical and quantum participants. Indeed, several of the aforementioned applications were previously only known via tailored LWE-based constructions, whereas our OSP-based constructions yield new results from a wider variety of assumptions, including hard problems on cryptographic group actions. Finally, towards understanding the minimal hardness assumptions required to realize OSP, we prove the following: - OSP implies oblivious transfer between one classical and one quantum party. - Two-round OSP implies public-key encryption with classical keys and ciphertexts. In particular, these results help to &#x27;&#x27;explain&#x27;&#x27; the use of public-key cryptography in the known approaches to establishing a &#x27;&#x27;classical leash&#x27;&#x27; on a quantum server. For example, combined with a result of Austrin et al. (CRYPTO 22), we conclude that perfectly-correct OSP cannot exist unconditionally in the (quantum) random oracle model.

  匹配依据：MPC: oblivious transfer

  </details>

- **Encrypted RAM Delegation: Homomorphic NIZKs, Malicious MPC with Optimal Communication Complexity, and more**
  2024-11-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1806)
  Abtin Afshar, Jiaqi Cheng, Rishab Goyal, Aayush Yadav, Saikumar Yadugiri

  <details><summary>摘要 / Abstract</summary>

  We construct fully-homomorphic NIZKs from a broader range of cryptographic assumptions, including LWE, $O(1)$-LIN, and DDH (without circular security assumptions). Prior to this work, homomorphic NIZKs were only known based on pairing-based techniques. A key ingredient that we develop in this work is a new notion of a partially-hiding succinct delegation system, that we call encrypted RAM (eRAM) delegation. In addition to homomorphic NIZKs, we show that eRAM delegation is also useful for turning a semi-malicious multiparty computation (MPC) protocol into a full maliciously secure protocol in a communication-complexity-preserving manner (i.e., malicious and semi-malicious protocols have identical asymptotic communication complexity). Prior MPC compilers with similar efficiency required strong non-falsifiable assumptions. Furthermore, eRAM delegation also is useful for designing composable zero-knowledge batch arguments and multi-hop homomorphic signatures with strong-context-hiding.

  匹配依据：MPC: multiparty computation

  </details>

- **EVA-S3PC: Efficient, Verifiable, Accurate Secure Matrix Multiplication Protocol Assembly and Its Application in Regression**
  2024-11-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.03404)
  Shizhao Peng, Tianrui Liu, Tianle Tao, Derun Zhao, Hao Sheng, Haogang Zhu

  <details><summary>摘要 / Abstract</summary>

  Efficient multi-party secure matrix multiplication is crucial for privacy-preserving machine learning, but existing mixed-protocol frameworks often face challenges in balancing security, efficiency, and accuracy. This paper presents an efficient, verifiable and accurate secure three-party computing (EVA-S3PC) framework that addresses these challenges with elementary 2-party and 3-party matrix operations based on data obfuscation techniques. We propose basic protocols for secure matrix multiplication, inversion, and hybrid multiplication, ensuring privacy and result verifiability. Experimental results demonstrate that EVA-S3PC achieves up to 14 significant decimal digits of precision in Float64 calculations, while reducing communication overhead by up to $54.8\%$ compared to state of art methods. Furthermore, 3-party regression models trained using EVA-S3PC on vertically partitioned data achieve accuracy nearly identical to plaintext training, which illustrates its potential in scalable, efficient, and accurate solution for secure collaborative modeling across domains.

  匹配依据：MPC: secure three party computing

  </details>

- **Siniel: Distributed Privacy-Preserving zkSNARK**
  2024-11-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1803)
  Yunbo Yang, Yuejia Cheng, Kailun Wang, Xiaoguo Li, Jianfei Sun, Jiachen Shen, Xiaolei Dong, Zhenfu Cao, Guomin Yang, Robert H. Deng

  <details><summary>摘要 / Abstract</summary>

  Zero-knowledge Succinct Non-interactive Argument of Knowledge (zkSNARK) is a powerful cryptographic primitive, in which a prover convinces a verifier that a given statement is true without leaking any additional information. However, existing zkSNARKs suffer from high computation overhead in the proof generation. This limits the applications of zkSNARKs, such as private payments, private smart contracts, and anonymous credentials. Private delegation has become a prominent way to accelerate proof generation. In this work, we propose Siniel, an efficient private delegation framework for zkSNARKs constructed from polynomial interactive oracle proof (PIOP) and polynomial commitment scheme (PCS). Our protocol allows a computationally limited prover (a.k.a. delegator) to delegate its expensive prover computation to several workers without leaking any information about the private witness. Most importantly, compared with the recent work EOS (USENIX&#x27;23), the state-of-the-art zkSNARK prover delegation framework, a prover in Siniel needs not to engage in the MPC protocol after sending its shares of private witness. This means that a Siniel prover can outsource the entire computation to the workers. We compare Siniel with EOS and show significant performance advantages of the former. The experimental results show that, under low bandwidth conditions (10MBps), Siniel saves about 16% time for delegators than that of EOS, whereas under high bandwidth conditions (1000MBps), Siniel saves about 80% than EOS.

  匹配依据：MPC: mpc (context)

  </details>

- **Quantum-Computable One-Way Functions without One-Way Functions**
  2024-11-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.02554)
  William Kretschmer, Luowen Qian, Avishay Tal

  <details><summary>摘要 / Abstract</summary>

  We construct a classical oracle relative to which $\mathsf{P} = \mathsf{NP}$ but quantum-computable quantum-secure trapdoor one-way functions exist. This is a substantial strengthening of the result of Kretschmer, Qian, Sinha, and Tal (STOC 2023), which only achieved single-copy pseudorandom quantum states relative to an oracle that collapses $\mathsf{NP}$ to $\mathsf{P}$. For example, our result implies multi-copy pseudorandom states and pseudorandom unitaries, but also classical-communication public-key encryption, signatures, and oblivious transfer schemes relative to an oracle on which $\mathsf{P}=\mathsf{NP}$. Hence, in our new relativized world, classical computers live in &quot;Algorithmica&quot; whereas quantum computers live in &quot;Cryptomania,&quot; using the language of Impagliazzo&#x27;s worlds. Our proof relies on a new distributional block-insensitivity lemma for $\mathsf{AC^0}$ circuits, wherein a single block is resampled from an arbitrary distribution.

  匹配依据：MPC: oblivious transfer

  </details>

- **FLock: Robust and Privacy-Preserving Federated Learning based on Practical Blockchain State Channels**
  2024-11-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1797)
  Ruonan Chen, Ye Dong, Yizhong Liu, Tingyu Fan, Dawei Li, Zhenyu Guan, Jianwei Liu, Jianying Zhou

  <details><summary>摘要 / Abstract</summary>

  \textit{Federated Learning} (FL) is a distributed machine learning paradigm that allows multiple clients to train models collaboratively without sharing local data. Numerous works have explored security and privacy protection in FL, as well as its integration with blockchain technology. However, existing FL works still face critical issues. \romannumeral1) It is difficult to achieving \textit{poisoning robustness} and \textit{data privacy} while ensuring high \textit{model accuracy}. Malicious clients can launch \textit{poisoning attacks} that degrade the global model. Besides, aggregators can infer private data from the gradients, causing \textit{privacy leakages}. Existing privacy-preserving poisoning defense FL solutions suffer from decreased model accuracy and high computational overhead. \romannumeral2) Blockchain-assisted FL records iterative gradient updates on-chain to prevent model tampering, yet existing schemes are not compatible with practical blockchains and incur high costs for maintaining the gradients on-chain. Besides, incentives are overlooked, where unfair reward distribution hinders the sustainable development of the FL community. In this work, we propose FLock, a robust and privacy-preserving FL scheme based on practical blockchain state channels. First, we propose a lightweight secure \textit{Multi-party Computation} (MPC)-friendly robust aggregation method through quantization, median, and Hamming distance, which could resist poisoning attacks against up to $&lt;50\%$ malicious clients. Besides, we propose communication-efficient Shamir&#x27;s secret sharing-based MPC protocols to protect data privacy with high model accuracy. Second, we utilize blockchain off-chain state channels to achieve immutable model records and incentive distribution. FLock achieves cost-effective compatibility with practical cryptocurrency platforms, e.g. Ethereum, along with fair incentives, by merging the secure aggregation into a multi-party state channel. In addition, a pipelined \textit{Byzantine Fault-Tolerant} (BFT) consensus is integrated where each aggregator can reconstruct the final aggregated results. Lastly, we implement FLock and the evaluation results demonstrate that FLock enhances robustness and privacy, while maintaining efficiency and high model accuracy. Even with 25 aggregators and 100 clients, FLock can complete one secure aggregation for ResNet in $2$ minutes over a WAN. FLock successfully implements secure aggregation with such a large number of aggregators, thereby enhancing the fault tolerance of the aggregation.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **An Efficient and Secure Boolean Function Evaluation Protocol**
  2024-11-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1787)
  Sushmita Sarkar, Vikas Srivastava, Tapaswini Mohanty, Nibedita Kundu, Sumit Kumar Debnath, Pantelimon Stanica

  <details><summary>摘要 / Abstract</summary>

  The secure evaluation of Boolean functions or Secure Boolean Evaluation (SBE) is a fundamental component in this area of research. SBE allows parties to jointly compute Boolean functions without exposing their private inputs. SBE finds applications in privacy-preserving protocols and secure multi-party computations. The existing schemes need at least $(1.5\lambda+5)$-bit strings to garble an AND gate with security parameter $\lambda$, where $\lambda$ is the length of arbitrary bit strings associated with inputs $0$ and $1$. In this manuscript, we discuss how we circumvent the communication cost of non-input gates independent of $\lambda$. We present an efficient and generic two-party protocol (namely $\mathsf{BooleanEval}$) for the secure evaluation of Boolean functions by utilizing a 1-out-of-2 Oblivious Transfer (OT) as a building block. We introduce randomized Bloom filter (namely, $\mathsf{ RBF}_S$) associated with a set $S$ to compute non-input $\mathsf{AND}$ gates. Moreover, $\mathsf{BooleanEval}$ only employs hash evaluations and XOR operations as the core computational step, making it lightweight and fast. Unlike other lightweight state-of-the-art designs of SBE, $\mathsf{BooleanEval}$ avoids the use of additional cryptographic primitives, such as commitment schemes, to reduce the computational overhead.

  匹配依据：MPC: oblivious transfer, secure evaluation

  </details>

- **Universal Adaptor Signatures from Blackbox Multi-Party Computation**
  2024-10-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1773)
  Michele Ciampi, Xiangyu Liu, Ioannis Tzannetos, Vassilis Zikas

  <details><summary>摘要 / Abstract</summary>

  Adaptor signatures (AS) extend the functionality of traditional digital signatures by enabling the generation of a pre-signature tied to an instance of a hard NP relation, which can later be turned (adapted) into a full signature upon revealing a corresponding witness. The recent work by Liu et al. [ASIACRYPT 2024] devised a generic AS scheme that can be used for any NP relation---which here we will refer to as universal adaptor signatures scheme, in short UAS---from any one-way function. However, this generic construction depends on the Karp reduction to the Hamiltonian cycle problem, which adds significant overhead and hinders practical applicability. In this work, we present an alternative approach to construct universal adaptor signature schemes relying on the multi-party computation in the head (MPCitH) paradigm. This overcomes the reliance on the costly Karp reduction, while inheriting the core property of the MPCitH---which makes it an invaluable tool in efficient cryptographic protocols---namely, that the construction is black-box with respect to the underlying cryptographic primitive (while it remains non-black-box in the relation being proven). Our framework simplifies the design of UAS and enhances their applicability across a wide range of decentralized applications, such as blockchain and privacy-preserving systems. Our results demonstrate that MPCitH-based UAS schemes offer strong security guarantees while making them a promising tool in the design of real-world cryptographic protocols.

  匹配依据：MPC: multi party computation

  </details>

- **PANTHER: Private Approximate Nearest Neighbor Search in the Single Server Setting**
  2024-10-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1774)
  Jingyu Li, Zhicong Huang, Min Zhang, Cheng Hong, Jian Liu, Tao Wei, Wenguang Chen

  <details><summary>摘要 / Abstract</summary>

  Approximate nearest neighbor search (ANNS), also known as vector search, is an important building block for various applications, such as recommendation systems, biometric authentication, and machine learning. In this work, we are interested in the private ANNS problem, where the client wants to learn (and can only learn) the ANNS results without revealing the query to the server. Previous private ANNS works either suffer from high communication cost (Chen et al., USENIX Security 2020) or work under a stronger security assumption of two non-colluding servers (Servan-Schreiber et al., SP 2022). We present Panther, an efficient private ANNS framework under the single server setting. Panther achieves its high performance via several novel co-designs of private information retrieval, secret-sharing, garbled circuits, and homomorphic encryption. We made extensive experiments using Panther on four public datasets, showing that Panther could answer an ANNS query on $10$ million points in $18$ seconds with $284$ MB of communication. This is more than $7.8\times$ faster and $20\times$ more compact than Chen et al..

  匹配依据：MPC: garbled circuits, secret sharing

  </details>

- **New results in Share Conversion, with applications to evolving access structures**
  2024-10-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1781)
  Tamar Ben David, Varun Narayanan, Olga Nissenbaum, Anat Paskin-Cherniavsky

  <details><summary>摘要 / Abstract</summary>

  We say there is a share conversion from a secret-sharing scheme $\Pi$ to another scheme $\Pi&#x27;$ implementing the same access structure if each party can locally apply a deterministic function to their share to transform any valid secret-sharing under $\Pi$ to a valid (but not necessarily random) secret-sharing under $\Pi&#x27;$ of the same secret. If such a conversion exists, we say that $\Pi\ge\Pi&#x27;$. This notion was introduced by Cramer et al. (TCC&#x27;05), where they particularly proved that for any access structure, any linear secret-sharing scheme over a given field $\mathbb{F}$, has a conversion from a CNF scheme, and is convertible to a DNF scheme. In this work, we initiate a systematic study of convertability between secret-sharing schemes, and present a number of results with implications to the understanding of the convertibility landscape. - In the context of linear schemes, we present two key theorems providing necessary conditions for convertibility, proved using linear-algebraic tools. It has several implications, such as the fact that Shamir secret-sharing scheme can be neither maximal or minimal. Another implication of it is that a scheme may be minimal if its share complexity is at least as high as that of DNF. - Our second key result is a necessary condition for convertibility to CNF from a broad class of (not necessarily linear) schemes. This result is proved via information-theoretic techniques and implies non-maximality for schemes with share complexity smaller than that of CNF. We also provide a condition which is both necessary and sufficient for the existence of a share conversion to some linear scheme. The condition is stated as a system of linear equations, such that a conversion exists if and only if a solution to the linear system exists. We note that the impossibility results for linear schemes may be viewed as identifying a subset of contradicting equations in the system. Another contribution of our paper, is in defining and studying share conversion for evolving secret-sharing schemes. In such a schemes, recently introduced by Komargodski et al. (IEEE ToIT&#x27;18), the number of parties is not bounded apriori, and every party receives a share as it arrives, which never changes in the sequel. Our impossibility results have implications to the evolving setting as well. Interestingly, unlike in the standard setting, there is no maximum or minimum in a broad class of evolving schemes, even without any restriction on the share size. Finally, we show that, generally, there is no conversion between additive schemes over different fields, even from CNF to DNF! However by relaxing from perfect to statistical security, it may be possible to convert, and examplify this for (n,n)-threshold access structures.

  匹配依据：MPC: secret sharing

  </details>

- **Measurement-device-independent quantum-secret-sharing networks with linear Bell-state analysis**
  2024-10-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.23562)
  Tianqi Liu, Jiancheng Lai, Zhenhua Li, Tao Li

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) plays a pivotal role in multiparty quantum communication, ensuring the secure distribution of private information among multiple parties. However, the security of QSS schemes can be compromised by attacks exploiting imperfections in measurement devices. Here, we propose a reconfigurable approach to implement QSS based on measurement-device-independent (MDI) principles, utilizing linear two-photon Bell state analysis.By employing single-qubit conjugate operations for encoding private classical information, our approach offers reconfigurability, allowing for the inclusion of additional parties without sacrificing efficiency. Furthermore, we demonstrate the robust security of our MDI-QSS scheme against inter-eavesdropping by dishonest participants and establish lower bounds for secure communication among three legitimate parties. This work presents a flexible configuration for implementing multiparty secure quantum communication with imperfect measurement devices and represents a significant advancement in the development of secure quantum communication technologies.

  匹配依据：MPC: secret sharing

  </details>

- **PRIME: Differentially Private Distributed Mean Estimation with Malicious Security**
  2024-10-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1771)
  Laasya Bangalore, Albert Cheu, Muthuramakrishnan Venkitasubramaniam

  <details><summary>摘要 / Abstract</summary>

  Distributed mean estimation (DME) is a fundamental and important task as it serves as a subroutine in convex optimization, aggregate statistics, and, more generally, federated learning. The inputs for distributed mean estimation (DME) are provided by clients (such as mobile devices), and these inputs often contain sensitive information. Thus, protecting privacy and mitigating the influence of malicious adversaries are critical concerns in DME. A surge of recent works has focused on building multiparty computation (MPC) based protocols tailored for the task of secure aggregation. However, MPC fails to directly address these two issues: (i) the potential manipulation of input by adversaries, and (ii) the leakage of information from the underlying function. This paper presents a novel approach that addresses both these issues. We propose a secure aggregation protocol with a robustness guarantee, effectively protecting the system from &quot;faulty&quot; inputs introduced by malicious clients. Our protocol further ensures differential privacy, so that the underlying function will not leak significant information about individuals. Notably, this work represents the first comprehensive effort to combine robustness and differential privacy guarantees in the context of DME. In particular, we capture the security of the protocol via a notion of &quot;usefulness&quot; combined with differential privacy inspired by the work of Mironov et al. (CRYPTO 2009) and formally analyze this security guarantee for our protocol.

  匹配依据：MPC: multiparty computation

  </details>

- **Critical Rounds in Multi-Round Proofs: Proof of Partial Knowledge and Trapdoor Commitments**
  2024-10-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1766)
  Masayuki Abe, David Balbás, Dung Bui, Miyako Ohkubo, Zehua Shang, Akira Takahashi, Mehdi Tibouchi

  <details><summary>摘要 / Abstract</summary>

  Zero-knowledge simulators, initially developed for proving the security of proof systems, turned out to be also useful in constructing advanced protocols from simple three-move interactive proofs. However, in the context of multi-round public-coin protocols, the interfaces of these auxiliary algorithms become more complex, introducing a range of technical challenges that hinder the generalization of these constructions. We introduce a framework to enhance the usability of zero-knowledge simulators in multi-round argument systems for protocol designs. Critical-round zero-knowledge relies on the ability to perform complete zero-knowledge simulations by knowing the challenge of just one specific round in advance. We show that these notions are satisfied by diverse protocols based on MPC-in-the-Head, interactive oracle proofs, and split-and-fold arguments. We demonstrate the usefulness of the critical round framework by constructing proofs of partial knowledge (Cramer, Damgård, and Schoenmakers, CRYPTO’94) and trapdoor commitments (Damgård, CRYPTO’89) from critical-round multi-round proofs.

  匹配依据：MPC: mpc (context)

  </details>

- **Resilience-Optimal Lightweight High-threshold Asynchronous Verifiable Secret Sharing**
  2024-10-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1761)
  Hao Cheng, Jiliang Li, Yizhong Liu, Yuan Lu, Weizhi Meng, Zhenfeng Zhang

  <details><summary>摘要 / Abstract</summary>

  Shoup and Smart (SS24) recently introduced a lightweight asynchronous verifiable secret sharing (AVSS) protocol with optimal resilience directly from cryptographic hash functions (JoC 2024), offering plausible quantum resilience and computational efficiency. However, SS24 AVSS only achieves standard secrecy to keep the secret confidential against $n/3$ corrupted parties \textit{if no honest party publishes its share}. In contrast, from ``heavyweight&#x27;&#x27; public-key cryptography, one can realize so-called \textit{high-threshold} asynchronous verifiable secret sharing (HAVSS), with a stronger \textit{high-threshold} secrecy to tolerate $n/3$ corrupted parties and additional leaked shares from $n/3$ honest parties. This raises the following question: can we bridge the remaining gap to design an efficient HAVSS using only lightweight cryptography? We answer the question in the affirmative by presenting a lightweight HAVSS with optimal resilience. When executing across $n$ parties to share a secret, it attains a worst-case communication complexity of $\Tilde{\bigO}(\lambda n^3)$ (where $\lambda$ is the cryptographic security parameter) and realizes high-threshold secrecy to tolerate a fully asynchronous adversary that can control $t= \lfloor \frac{n-1}{3} \rfloor$ malicious parties and also learn $t$ additional secret shares from some honest parties. The (worst-case) communication complexity of our lightweight HAVSS protocol matches that of SS24 AVSS---the state-of-the-art lightweight AVSS without high-threshold secrecy. Notably, our design is a direct and concretely efficient reduction to hash functions in the random oracle model, without extra setup assumptions like CRS/PKI or heavy intermediate steps like hash-based zk-STARK.

  匹配依据：MPC: secret sharing

  </details>

- **$\\mathsf{OPA}$: One-shot Private Aggregation with Single Client Interaction and its Applications to Federated Learning**
  2024-10-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.22303) · [IACR ePrint](https://eprint.iacr.org/2024/723)
  Harish Karthikeyan, Antigoni Polychroniadou

  <details><summary>摘要 / Abstract</summary>

  Our work aims to minimize interaction in secure computation due to the high cost and challenges associated with communication rounds, particularly in scenarios with many clients. In this work, we revisit the problem of secure aggregation in the single-server setting where a single evaluation server can securely aggregate client-held individual inputs. Our key contribution is the introduction of One-shot Private Aggregation ($\mathsf{OPA}$) where clients speak only once (or even choose not to speak) per aggregation evaluation. Since each client communicates only once per aggregation, this simplifies managing dropouts and dynamic participation, contrasting with multi-round protocols and aligning with plaintext secure aggregation, where clients interact only once. We construct $\mathsf{OPA}$ based on LWR, LWE, class groups, DCR and demonstrate applications to privacy-preserving Federated Learning (FL) where clients \emph{speak once}. This is a sharp departure from prior multi-round FL protocols whose study was initiated by Bonawitz et al. (CCS, 2017). Moreover, unlike the YOSO (You Only Speak Once) model for general secure computation, $\mathsf{OPA}$ eliminates complex committee selection protocols to achieve adaptive security. Beyond asymptotic improvements, $\mathsf{OPA}$ is practical, outperforming state-of-the-art solutions. We benchmark logistic regression classifiers for two datasets, while also building an MLP classifier to train on MNIST, CIFAR-10, and CIFAR-100 datasets. We build two flavors of $\caps$ (1) from (threshold) key homomorphic PRF and (2) from seed homomorphic PRG and secret sharing.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Somewhat Homomorphic Encryption from Linear Homomorphism and Sparse LPN**
  2024-10-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1760)
  Henry Corrigan-Gibbs, Alexandra Henzinger, Yael Tauman Kalai, Vinod Vaikuntanathan

  <details><summary>摘要 / Abstract</summary>

  We construct somewhat homomorphic encryption from the sparse learning-parities-with-noise problem, along with any assumption that implies linearly homomorphic encryption (e.g., the decisional Diffie-Hellman or decisional composite residuosity assumptions). Our resulting schemes support an a-priori bounded number of homomorphic operations: $O(\log \lambda / \log \log \lambda)$ multiplications followed by poly($\lambda$) additions, where $\lambda$ is a security parameter. These schemes have compact ciphertexts: before and after homomorphic evaluation, the bit length of each ciphertext is a fixed polynomial in the security parameter $\lambda$, independent of the number of homomorphic operations that the scheme supports. This gives the first constructions of somewhat homomorphic encryption that can evaluate the class of bounded-degree polynomials without relying on lattice assumptions or bilinear maps. Our new encryption schemes are conceptually simple: much as in Gentry, Sahai, and Waters’ fully homomorphic encryption scheme, ciphertexts in our scheme are matrices, homomorphic addition is matrix addition, and homomorphic multiplication is matrix multiplication. Moreover, when encrypting many messages at once and performing many homomorphic evaluations at once, the bit length of the ciphertexts in (some of) our schemes can be made arbitrarily close to the bit length of the plaintexts. The main limitation of our schemes is that they require a large evaluation key, whose size scales with the complexity of the homomorphic computation performed, though this key can be re-used across any polynomial number of encryptions and evaluations. Our construction builds on recent work of Dao, Ishai, Jain, and Lin, who construct a homomorphic secret-sharing scheme from the sparse-LPN assumption.

  匹配依据：MPC: secret sharing

  </details>

- **Accelerating Privacy-Preserving Medical Record Linkage: A Three-Party MPC Approach**
  2024-10-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.21605)
  Şeyma Selcan Mağara, Noah Dietrich, Ali Burak Ünal, Mete Akgün

  <details><summary>摘要 / Abstract</summary>

  Record linkage is a crucial concept for integrating data from multiple sources, particularly when datasets lack exact identifiers, and it has diverse applications in real-world data analysis. Privacy-Preserving Record Linkage (PPRL) ensures this integration occurs securely, protecting sensitive information from unauthorized access. This is especially important in sectors such as healthcare, where datasets include private identity information (IDAT) governed by strict privacy laws. However, maintaining both privacy and efficiency in large-scale record linkage poses significant challenges. Consequently, researchers must develop advanced methods to protect data privacy while optimizing processing performance. This paper presents a novel and efficient PPRL method based on a secure 3-party computation (MPC) framework. Our approach allows multiple parties to compute linkage results without exposing their private inputs and significantly improves the speed of linkage process compared to existing privacy-preserving solutions. We demonstrated that our method preserves the linkage quality of the state-of-the-art PPRL method while achieving up to 14 times faster performance. For example, linking a record against a database of 10,000 records takes just 8.74 seconds in a realistic network with 700 Mbps bandwidth and 60 ms latency. Even on a slower internet connection with 100 Mbps bandwidth and 60 ms latency, the linkage completes in 28 seconds, highlighting the scalability and efficiency of our solution.

  匹配依据：MPC: secure 3 party computation

  </details>

- **$\\mathsf{Graphiti}$: Secure Graph Computation Made More Scalable**
  2024-10-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1756)
  Nishat Koti, Varsha Bhat Kukkala, Arpita Patra, Bhavish Raj Gopal

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving graph analysis allows performing computations on graphs that store sensitive information while ensuring all the information about the topology of the graph, as well as data associated with the nodes and edges, remains hidden. The current work addresses this problem by designing a highly scalable framework, $\mathsf{Graphiti}$, that allows securely realising any graph algorithm. $\mathsf{Graphiti}$ relies on the technique of secure multiparty computation (MPC) to design a generic framework that improves over the state-of-the-art framework of GraphSC by Araki et al. (CCS&#x27;21). The key technical contribution is that $\mathsf{Graphiti}$ has round complexity independent of the graph size, which in turn allows attaining the desired scalability. Specifically, this is achieved by (i) decoupling the $\mathsf{Scatter}$ primitive of GraphSC into separate operations of $\mathsf{Propagate}$ and $\mathsf{ApplyE}$, (ii) designing a novel constant-round approach to realise $\mathsf{Propagate}$, as well as (iii) designing a novel constant-round approach to realise the $\mathsf{Gather}$ primitive of GraphSC by leveraging the linearity of the aggregation operation. We benchmark the performance of $\mathsf{Graphiti}$ for the application of contact tracing via BFS for 10 hops and observe that it takes less than 2 minutes when computing over a graph of size $10^7$. Concretely it improves over the state-of-the-art up to a factor of $1034\times$ in online run time. Similar to GraphSC by Araki et al., since $\mathsf{Graphiti}$ relies on a secure protocol for shuffle, we additionally design a shuffle protocol secure against a semi-honest adversary in the 2-party with a helper setting. Given the versatility of shuffle protocol, the designed solution is of independent interest. Hence, we also benchmark the performance of the designed shuffle where we observe improvements of up to $1.83\times$ in online run time when considering an input vector of size $10^7$, in comparison to the state-of-the-art in the considered setting.

  匹配依据：MPC: secure multiparty computation

  </details>

- **FL-DABE-BC: A Privacy-Enhanced, Decentralized Authentication, and Secure Communication for Federated Learning Framework with Decentralized Attribute-Based Encryption and Blockchain for IoT Scenarios**
  2024-10-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.20259)
  Sathwik Narkedimilli, Amballa Venkata Sriram, Satvik Raghav

  <details><summary>摘要 / Abstract</summary>

  This study proposes an advanced Federated Learning (FL) framework designed to enhance data privacy and security in IoT environments by integrating Decentralized Attribute-Based Encryption (DABE), Homomorphic Encryption (HE), Secure Multi-Party Computation (SMPC), and Blockchain technology. Unlike traditional FL, our framework enables secure, decentralized authentication and encryption directly on IoT devices using DABE, allowing sensitive data to remain locally encrypted. Homomorphic Encryption permits computations on encrypted data, and SMPC ensures privacy in collaborative computations, while Blockchain technology provides transparent, immutable record-keeping for all transactions and model updates. Local model weights are encrypted and transmitted to fog layers for aggregation using HE and SMPC, then iteratively refined by the central server using differential privacy to safeguard against data leakage. This secure, privacy-preserving FL framework delivers a robust solution for efficient model training and real-time analytics across distributed IoT devices, offering significant advancements in secure decentralized learning for IoT applications.

  匹配依据：MPC: secure multi party computation

  </details>

- **A distributed and parallel $(k, n)$ QSS scheme with verification capability**
  2024-10-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.18643)
  Theodore Andronikos

  <details><summary>摘要 / Abstract</summary>

  This article introduces a novel Quantum Secret Sharing scheme with $( k, n )$ threshold and endowed with verification capability. The new protocol exploits the power of entanglement and evolves in three phases. The primary novelty of the new protocol lies in its ability to operate completely parallelly in a fully distributed setup, where the spymaster and her agents all are in different locations, in contrast to the vast majority of analogous protocols that assume a localized scenario in which all agents are at the same place. The spymaster sends all necessary information to all intended recipients simultaneously in one step. All phases are executed in parallel, minimizing the overall execution cost of the protocol. Given its comparative complexity, we provide a comprehensive and detailed analysis to establish its information-theoretic security in the sense of preventing both outside eavesdroppers from obtaining any useful information and inside rogue agents from sabotaging its successful completion. The protocol eliminates the need for a quantum signature scheme or pre-shared keys, thereby simplifying the process and lowering complexity. Finally, the possibility of its implementation by contemporary quantum computers is promising because the protocol relies exclusively on CNOT and Hadamard gates and all players operating on similar or identical quantum circuits.

  匹配依据：MPC: secret sharing

  </details>

- **Federated Transformer: Multi-Party Vertical Federated Learning on Practical Fuzzily Linked Data**
  2024-10-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.17986)
  Zhaomin Wu, Junyi Hou, Yiqun Diao, Bingsheng He

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) is an evolving paradigm that enables multiple parties to collaboratively train models without sharing raw data. Among its variants, Vertical Federated Learning (VFL) is particularly relevant in real-world, cross-organizational collaborations, where distinct features of a shared instance group are contributed by different parties. In these scenarios, parties are often linked using fuzzy identifiers, leading to a common practice termed as multi-party fuzzy VFL. Existing models generally address either multi-party VFL or fuzzy VFL between two parties. Extending these models to practical multi-party fuzzy VFL typically results in significant performance degradation and increased costs for maintaining privacy. To overcome these limitations, we introduce the Federated Transformer (FeT), a novel framework that supports multi-party VFL with fuzzy identifiers. FeT innovatively encodes these identifiers into data representations and employs a transformer architecture distributed across different parties, incorporating three new techniques to enhance performance. Furthermore, we have developed a multi-party privacy framework for VFL that integrates differential privacy with secure multi-party computation, effectively protecting local representations while minimizing associated utility costs. Our experiments demonstrate that the FeT surpasses the baseline models by up to 46\% in terms of accuracy when scaled to 50 parties. Additionally, in two-party fuzzy VFL settings, FeT also shows improved performance and privacy over cutting-edge VFL models.

  匹配依据：MPC: secure multi party computation

  </details>

- **Beyond Yao's Millionaires: Secure Multi-Party Computation of Non-Polynomial Functions**
  2024-10-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.17000)
  Seyed Reza Hoseini Najarkolaei, Mohammad Mahdi Mojahedian, Mohammad Reza Aref

  <details><summary>摘要 / Abstract</summary>

  In this paper, we present an unconditionally secure $N$-party comparison scheme based on Shamir secret sharing, utilizing the binary representation of private inputs to determine the $\max$ without disclosing any private inputs or intermediate results. Specifically, each party holds a private number and aims to ascertain the greatest number among the $N$ available private numbers without revealing its input, assuming that there are at most $T &lt; \frac{N}{2}$ honest-but-curious parties. The proposed scheme demonstrates a lower computational complexity compared to existing schemes that can only compare two secret numbers at a time. To the best of our knowledge, our scheme is the only information-theoretically secure method for comparing $N$ private numbers without revealing either the private inputs or any intermediate results. We demonstrate that by modifying the proposed scheme, we can compute other well-known non-polynomial functions of the inputs, including the minimum, median, and rank. Additionally, in the proposed scheme, before the final reveal phase, each party possesses a share of the result, enabling the nodes to compute any polynomial function of the comparison result. We also explore various applications of the proposed comparison scheme, including federated learning.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **ZK-DPPS: A Zero-Knowledge Decentralised Data Sharing and Processing Middleware**
  2024-10-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.15568)
  Amir Jabbari, Gowri Ramachandran, Sidra Malik, Raja Jurdak

  <details><summary>摘要 / Abstract</summary>

  In the current digital landscape, supply chains have transformed into complex networks driven by the Internet of Things (IoT), necessitating enhanced data sharing and processing capabilities to ensure traceability and transparency. Leveraging Blockchain technology in IoT applications advances reliability and transparency in near-real-time insight extraction processes. However, it raises significant concerns regarding data privacy. Existing privacy-preserving approaches often rely on Smart Contracts for automation and Zero Knowledge Proofs (ZKP) for privacy. However, apart from being inflexible in adopting system changes while effectively protecting data confidentiality, these approaches introduce significant computational expenses and overheads that make them impractical for dynamic supply chain environments. To address these challenges, we propose ZK-DPPS, a framework that ensures zero-knowledge communications without the need for traditional ZKPs. In ZK-DPPS, privacy is preserved through a combination of Fully Homomorphic Encryption (FHE) for computations and Secure Multi-Party Computations (SMPC) for key reconstruction. To ensure that the raw data remains private throughout the entire process, we use FHE to execute computations directly on encrypted data. The &quot;zero-knowledge&quot; aspect of ZK-DPPS refers to the system&#x27;s ability to process and share data insights without exposing sensitive information, thus offering a practical and efficient alternative to ZKP-based methods. We demonstrate the efficacy of ZK-DPPS through a simulated supply chain scenario, showcasing its ability to tackle the dual challenges of privacy preservation and computational trust in decentralised environments.

  匹配依据：MPC: smpc (context)

  </details>

- **Secure Computation and Trustless Data Intermediaries in Data Spaces**
  2024-10-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.16442)
  Christoph Fabianek, Stephan Krenn, Thomas Loruenser, Veronika Siska

  <details><summary>摘要 / Abstract</summary>

  This paper explores the integration of advanced cryptographic techniques for secure computation in data spaces to enable secure and trusted data sharing, which is essential for the evolving data economy. In addition, the paper examines the role of data intermediaries, as outlined in the EU Data Governance Act, in data spaces and specifically introduces the idea of trustless intermediaries that do not have access to their users&#x27; data. Therefore, we exploit the introduced secure computation methods, i.e. Secure Multi-Party Computation (MPC) and Fully Homomorphic Encryption (FHE), and discuss the security benefits. Overall, we identify and address key challenges for integration, focusing on areas such as identity management, policy enforcement, node selection, and access control, and present solutions through real-world use cases, including air traffic management, manufacturing, and secondary data use. Furthermore, through the analysis of practical applications, this work proposes a comprehensive framework for the implementation and standardization of secure computing technologies in dynamic, trustless data environments, paving the way for future research and development of a secure and interoperable data ecosystem.

  匹配依据：MPC: secure computation, secure computing, secure multi party computation

  </details>

- **Practical Asynchronous MPC from Lightweight Cryptography**
  2024-10-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1717)
  Atsuki Momose

  <details><summary>摘要 / Abstract</summary>

  We present an asynchronous secure multi-party computation (MPC) protocol that is practically efficient. Our protocol can evaluate any arithmetic circuit with linear communication in the number of parties per multiplication gate, while relying solely on computationally lightweight cryptography such as hash function and symmetric encryption. Our protocol is optimally resilient and tolerates $t$ malicious parties among $n = 3t+1$ parties. At the technical level, we manage to apply the \emph{player-elimination} paradigm to asynchronous MPC. This framework enables the detection and eviction of cheating parties by repeatedly attempting to generate Beaver triples. Once all malicious parties are eliminated, honest parties can proceed with efficient Beaver triple generation. While this approach is standard in synchronous MPC, it presents several technical challenges when adopted in an asynchronous network, which we address in this work.

  匹配依据：MPC: secure multi party computation

  </details>

- **Universally Composable Non-Interactive Zero-Knowledge from Sigma Protocols via a New Straight-line Compiler**
  2024-10-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1713)
  Megan Chen, Pousali Dey, Chaya Ganesh, Pratyay Mukherjee, Pratik Sarkar, Swagata Sasmal

  <details><summary>摘要 / Abstract</summary>

  Non-interactive zero-knowledge proofs (NIZK) are essential building blocks in threshold cryptosystems like multiparty signatures, distributed key generation, and verifiable secret sharing, allowing parties to prove correct behavior without revealing secrets. Furthermore, universally composable (UC) NIZKs enable seamless composition in the larger cryptosystems. A popular way to construct NIZKs is to compile interactive protocols using the Fiat-Shamir transform. Unfortunately, Fiat-Shamir transformed NIZK requires rewinding the adversary and is not $\textit{straight-line extractable}$, making it at odds with UC. Using Fischlin&#x27;s transform gives straight-line extractability, but at the expense of many repetitions of the underlying protocol leading to poor concrete efficiency and difficulty in setting parameters. In this work, we propose a simple new transform that compiles a Sigma protocol for an algebraic relation into a UC-NIZK protocol $\textit{without any overheads of repetition}$. - Given a Sigma protocol for proving m algebraic statements over n witnesses, we construct a compiler to transform it into a $\textit{straight-line extractable}$ protocol using an additively homomorphic encryption scheme AHE. Our prover executes the Sigma protocol&#x27;s prover once and computes 2n encryptions. The verification process involves running the Sigma protocol verifier once and then computing n encryptions, which are homomorphically verified against the prover generated encryptions. - We apply the Fiat-Shamir transform to the above straight-line extractable Sigma protocol to obtain a UC-NIZK. We instantiate AHE using class group-based encryption where the public key of the encryption scheme is obliviously sampled using a suitable hash function. This yields a UC-NIZK protocol in the random oracle model.

  匹配依据：MPC: secret sharing

  </details>

- **Efficient Updatable PSI from Asymmetric PSI and PSU**
  2024-10-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1712) · [Code](https://github.com/ShallMate/upsi)
  Guowei Ling, Peng Tang, Weidong Qiu

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection (PSI) allows two mutually untrusted parties to compute the intersection of their private sets without revealing additional information. In general, PSI operates in a static setting, where the computation is performed only once on the input sets of both parties. Badrinarayanan et al. initiated the study of Updatable PSI (UPSI), which extends this capability to dynamically updating sets, enabling both parties to securely compute the intersection as their sets are modified while incurring significantly less overhead than re-executing a conventional PSI. However, existing UPSI protocols either do not support arbitrary deletion of elements or incur high computational and communication overhead. This work combines asymmetric PSI with Private Set Union (PSU) to present a novel UPSI protocol, which supports arbitrary additions and deletions of elements, offering a flexible approach to update sets. Furthermore, our protocol enjoys efficient performance compared to previous work. Specifically, we implement our protocol and compare it against state-of-the-art conventional PSI and UPSI protocols. Experimental results demonstrate that our UPSI protocol achieves up to three orders of magnitude reduction in computational overhead and incurs $190 \sim 707 \times$ less communication overhead than the state-of-the-art UPSI protocol that supports arbitrary additions and deletions. Our implementation is available at: \url{https://github.com/ShallMate/upsi}.

  匹配依据：MPC: private set intersection, private set union

  </details>

- **$\\widetilde{\\mbox{O}}$ptimal Adaptively Secure Hash-based MVBA and Asynchronous Common Subset**
  2024-10-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1710)
  Hanwen Feng, Zhenliang Lu, Qiang Tang

  <details><summary>摘要 / Abstract</summary>

  Asynchronous multiparty computation (AMPC) requires an input agreement phase where all participants have a consistent view of the set of private inputs. While the input agreement problem can be precisely addressed by a Byzantine fault-tolerant consensus known as Asynchronous Common Subset (ACS), existing ACS constructions with potential post-quantum security have a large $\widetilde{\mathcal{O}}(n^3)$ communication complexity for a network of $n$ nodes. This poses a bottleneck for AMPC in the same setting. In contrast, ACS has optimal constructions with quadratic communication complexity based on bilinear map assumptions. In this paper, we bridge this gap by introducing a nearly optimal ACS, which, assuming a common coin oracle, relies on the blackbox use of collision-resistant hash functions. It exhibits $\widetilde{\mathcal{O}}(n^2)$ communication complexity, expected constant round complexity, and security against adaptive adversaries who can corrupt up to $n/3$ nodes and perform “after-the-fact-removal” attacks. At the core of our new ACS is the first nearly optimal hash-based asynchronous Multi-valued Validated Byzantine Agreement (MVBA). To reduce cubic communication while avoiding heavy cryptographic tools, we introduce a new design paradigm with several novel components. This paradigm also enables an information-theoretic MVBA construction, whose communication complexity is higher than its hash-based counterpart but still quadratic. We give standard treatment of those using the conventional property based definitions. We also define and analyze our MVBA and components within the UC-framework, facilitating their modular use in broader applications, particularly in AMPC.

  匹配依据：MPC: multiparty computation

  </details>

- **Dumbo-MPC: Efficient Fully Asynchronous MPC with Optimal Resilience**
  2024-10-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1705)
  Yuan Su, Yuan Lu, Jiliang Li, Yuyi Wang, Chengyi Dong, Qiang Tang

  <details><summary>摘要 / Abstract</summary>

  Fully asynchronous multi-party computation (AMPC) has superior robustness in realizing privacy and guaranteed output delivery (G.O.D.) against asynchronous adversaries that can arbitrarily delay communications. However, none of these protocols are truly practical, as they either have sub-optimal resilience, incur cumbersome communication cost, or suffer from an online phase with extra cryptographic overhead. The only attempting implementation---HoneyBadgerMPC (hbMPC)---merely ensures G.O.D. in some implausible optimistic cases due to a non-robust offline pre-processing phase. We propose Dumbo-MPC a concretely efficient AMPC-as-a-service design with all phases G.O.D. and optimal resilience against $t&lt;n/3$ malicious parties (where $n$ is the total number of parties). Same to hbMPC, Dumbo-MPC has a robust (almost) information-theoretic online phase that can efficiently perform online computations, given pre-processed multiplication triples. While for achieving all phases G.O.D., we design a novel dual-mode offline protocol that can robustly pre-process multiplication triples in asynchrony. The offline phase features $O(n)$ per-triple communication in the optimistic case, followed by a fully asynchronous fallback to a pessimistic path to securely restore G.O.D. in the bad case. To efficiently implement the pessimistic path, we devise a concretely efficient zk-proof for product relationship of secret shares over compact KZG polynomial commitments, which enables us to reduce the degree of two secret shares&#x27; product from $2t$ to $t$ and could be of independent interest. We also implement and extensively evaluate Dumbo-MPC (particularly its offline phase) in varying network settings with up to 31 AWS servers. To our knowledge, we provide the first implementation of AMPC with all-phase G.O.D. A recent asynchronous triple generation protocol from Groth and Shoup (GS23) is also implemented and experimentally compared. When $n = 31$, Dumbo-MPC generates 94 triples/sec (almost twice of GS23) in the pessimistic case and 349 triples/sec (6X of GS23) in the good case, such that 31 parties require only 2-8 min to prepare a private Vickrey auction of 100 bidders or 10-36 min for a mixing network of $2^{10}$ inputs.

  匹配依据：MPC: multi party computation

  </details>

- **A Note on Security Definitions for Secret Sharing with Certified Deletion**
  2024-10-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1690)
  Dominique Bazin, Ryo Nishimaki

  <details><summary>摘要 / Abstract</summary>

  Bartusek and Raizes (CRYPTO 2024) proposed two security definitions for secret sharing, no-signaling certified deletion and adaptive certified deletion. We prove that adaptive certified deletion does not imply no-signaling certified deletion.

  匹配依据：MPC: secret sharing

  </details>

- **A Construction of Evolving $3$-threshold Secret Sharing Scheme with Perfect Security and Smaller Share Size**
  2024-10-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.13529)
  Qi Cheng, Hongru Cao, Sian-Jheng Lin

  <details><summary>摘要 / Abstract</summary>

  The evolving $k$-threshold secret sharing scheme allows the dealer to distribute the secret to many participants such that only no less than $k$ shares together can restore the secret. In contrast to the conventional secret sharing scheme, the evolving scheme allows the number of participants to be uncertain and even ever-growing. In this paper, we consider the evolving secret sharing scheme with $k=3$. First, we point out that the prior approach has risks in the security. To solve this issue, we then propose a new evolving $3$-threshold scheme with perfect security. Given a $\ell$-bit secret, the $t$-th share of the proposed scheme has $\lceil\log_2 t\rceil +O({\lceil \log_4 \log_2 t\rceil}^2)+\log_2 p(2\lceil \log_4 \log_2 t\rceil-1)$ bits, where $p$ is a prime. Compared with the prior result $2 \lfloor\log_2 t\rfloor+O(\lfloor\log_2 t\rfloor)+\ell$, the proposed scheme reduces the leading constant from $2$ to $1$. Finally, we propose a conventional $3$-threshold secret sharing scheme over a finite field. Based on this model of the revised scheme and the proposed conventional $3$-threshold scheme, we present a brand-new and more concise evolving $3$-threshold secret sharing scheme.

  匹配依据：MPC: secret sharing

  </details>

- **Unclonable Functional Encryption**
  2024-10-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.06029) · [IACR ePrint](https://eprint.iacr.org/2024/1683)
  Arthur Mehta, Anne Müller

  <details><summary>摘要 / Abstract</summary>

  In a functional encryption (FE) scheme, a user that holds a ciphertext and a function key can learn the result of applying the function to the plaintext message. Security requires that the user does not learn anything beyond the function evaluation. We extend this notion to the quantum setting by providing definitions and a construction for a quantum functional encryption (QFE) scheme which allows for the evaluation of polynomialy-sized circuits on arbitrary quantum messages. Our construction is built upon quantum garbled circuits [BY22]. We also investigate the relationship of QFE to the seemingly unrelated notion of unclonable encryption (UE) and find that any QFE scheme universally achieves the property of unclonable functional encryption (UFE). In particular we assume the existence of an unclonable encryption scheme with quantum decryption keys which was recently constructed by [AKY24]. Our UFE guarantees that two parties cannot simultaneously recover the correct function outputs using two independently sampled function secret keys. As an application we give the first construction for public-key UE with variable decryption keys. Lastly, we establish a connection between quantum indistinguishability obfuscation (qiO) and quantum functional encryption (QFE); Showing that any multi-input indistinguishability-secure quantum functional encryption scheme unconditionally implies the existence of qiO.

  匹配依据：MPC: garbled circuits

  </details>

- **Statistical Layered MPC**
  2024-10-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1670)
  Giovanni Deligios, Anders Konring, Chen-Da Liu-Zhang, Varun Narayanan

  <details><summary>摘要 / Abstract</summary>

  The seminal work of Rabin and Ben-Or (STOC&#x27;89) showed that the problem of secure $n$-party computation can be solved for $t&lt;n/2$ corruptions with guaranteed output delivery and statistical security. This holds in the traditional static model where the set of parties is fixed throughout the entire protocol execution. The need to better capture the dynamics of large scale and long-lived computations, where compromised parties may recover and the set of parties can change over time, has sparked renewed interest in the proactive security model by Ostrovsky and Yung (PODC&#x27;91). This abstraction, where the adversary may periodically uncorrupt and corrupt a new set of parties, is taken even a step further in the more recent YOSO and Fluid MPC models (CRYPTO&#x27;21) which allow, in addition, disjoint sets of parties participating in each round. Previous solutions with guaranteed output delivery and statistical security only tolerate $t&lt;n/3$ corruptions, or assume a random corruption pattern plus non-standard communication models. Matching the Rabin and Ben-Or bound in these settings remains an open problem. In this work, we settle this question considering the unifying Layered MPC abstraction recently introduced by David et al. (CRYPTO&#x27;23). In this model, the interaction pattern is defined by a layered acyclic graph, where each party sends secret messages and broadcast messages only to parties in the very next layer. We complete the feasibility landscape of layered MPC, by extending the Rabin and Ben-Or result to this setting. Our results imply maximally-proactive MPC with statistical security in the honest-majority setting.

  匹配依据：MPC: mpc (context)

  </details>

- **Secure Stateful Aggregation: A Practical Protocol with Applications in Differentially-Private Federated Learning**
  2024-10-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.11368) · [IACR ePrint](https://eprint.iacr.org/2024/1655)
  Marshall Ball, James Bell-Clark, Adria Gascon, Peter Kairouz, Sewoong Oh, Zhiye Xie

  <details><summary>摘要 / Abstract</summary>

  Recent advances in differentially private federated learning (DPFL) algorithms have found that using correlated noise across the rounds of federated learning (DP-FTRL) yields provably and empirically better accuracy than using independent noise (DP-SGD). While DP-SGD is well-suited to federated learning with a single untrusted central server using lightweight secure aggregation protocols, secure aggregation is not conducive to implementing modern DP-FTRL techniques without assuming a trusted central server. DP-FTRL based approaches have already seen widespread deployment in industry, albeit with a trusted central curator who provides and applies the correlated noise. To realize a fully private, single untrusted server DP-FTRL federated learning protocol, we introduce secure stateful aggregation: a simple append-only data structure that allows for the private storage of aggregate values and reading linear functions of the aggregates. Assuming Ring Learning with Errors, we provide a lightweight and scalable realization of this protocol for high-dimensional data in a new security/resource model, Federated MPC : where a powerful persistent server interacts with weak, ephemeral clients. We observe that secure stateful aggregation suffices for realizing DP-FTRL-based private federated learning: improving DPFL utility guarantees over the state of the art while maintaining privacy with an untrusted central party. Our approach has minimal overhead relative to existing techniques which do not yield comparable utility. The secure stateful aggregation primitive and the federated MPC paradigm may be of interest for other practical applications.

  匹配依据：MPC: mpc (context)

  </details>

- **Multi-party Setup Ceremony for Generating Multivariate zk-SNARK Parameters**
  2024-10-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1671)
  Muhammed Ali Bingol

  <details><summary>摘要 / Abstract</summary>

  The development of succinct non-interactive arguments of knowledge (SNARKs), which maintain a constant proof size regardless of computational complexity, has led to substantial improvements in both the scalability and privacy of verifiable computations. By enabling efficient verification of complex computations without revealing sensitive data, SNARK systems underpin modern applications ranging from privacy-focused protocols to high-performance blockchain infrastructures. This work presents a generalised specification for a Multi-Party Computation (MPC) setup ceremony designed to generate structured reference strings for non-transparent, pairing-based zk-SNARKs. Building on the MMORPG framework of Bowe, Gabizon, and Miers, we design a unified MPC protocol that accommodates multi-dimensional parameter structures required by contemporary SNARK designs. While our methodology is applicable to a broad class of structured CRS constructions, the Tokamak zk-SNARK serves as a motivating example illustrating the need for such a generalisation. The proposed ceremony supports universal and circuit-specific parameter generation, enabling reuse of CRS components across multiple instantiations while maintaining strong soundness guarantees under the presence of at least one honest participant. The protocol operates in two phases: (i) a universal ``Powers of &quot;tau&#x27;&#x27;-style phase generating parameter sets independent of circuit topology; and (ii) a circuit-specialised phase derived from a subcircuit-based universal circuit paradigm. For both phases, we formalise complete computation and verification procedures, including proof-of-knowledge mechanisms, cross-parameter consistency checks, and structured multivariate parameter updates. Optional integration of a random beacon---as in the MMORPG construction---is supported to enhance unpredictability and public auditability without altering the core security assumptions. Overall, this work provides a modular, extensible, and publicly verifiable MPC framework suitable for SNARK systems requiring structured, multi-parameter CRS generation, while Tokamak serves as a practical motivating instance of the broader methodology.

  匹配依据：MPC: multi party computation

  </details>

- **Modelings for generic PoK and Applications: Shorter SD and PKP based Signatures**
  2024-10-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1668)
  Slim Bettaieb, Loïc Bidoux, Philippe Gaborit, Mukul Kulkarni

  <details><summary>摘要 / Abstract</summary>

  The Multi-Party Computation in the Head (MPCitH) paradigm has proven to be a versatile tool to design proofs of knowledge (PoK) based on variety of computationally hard problems. For instance, many post-quantum signatures have been designed from MPC based proofs combined with the Fiat-Shamir transformation. Over the years, MPCitH has evolved significantly with developments based on techniques such as threshold computing and other optimizations. Recently, Vector Oblivious Linear Evaluation (VOLE) and the VOLE in the Head framework has spurred further advances. In this work, we introduce three VOLE-friendly modelings for generic and communication efficient PoK to prove the knowledge of secret witness in the form of elementary vectors, vectors of Hamming weight at most $\omega$, and permutation matrices. Remarkably, these modelings scale logarithmically with respect to the original witness sizes. Specifically, our modeling for elementary vectors of size $n$ transforms the witness size to $\mathcal{O}(\log_2(n))$, in case of vectors of size $n$ and Hamming weight at most $\omega$ the reduced witness is of size $\mathcal{O}\left(\omega \log_2(n)\right)$ while our modeling for permutation matrix of size $n \times n$ results in an (equivalent) witness of size $\mathcal{O}(n\log_2(n))$, which leads to small proofs in practice. To achieve this, we consider modelings with higher multiplicative depth $d &gt; 2$. Even if this increases the proof size, we show that our approach compares favorably with existing proofs. Such design choices were mostly overlooked in previous comparable works, maybe because prior to the VOLEitH framework, multiplications were often emulated with Beaver&#x27;s triples causing the proof size to scale poorly with $d$. We also provide several applications for our modelings namely i) post-quantum signature schemes based on the $\mathsf{SD}$ (Syndrome Decoding) problem and $\mathsf{PKP}$ (Permuted Kernel Problem), ii) PoK of secrets key for code-based key encapsulation mechanism (KEM), and iii) ring signatures from $\mathsf{SD}$ and $\mathsf{PKP}$. Our signatures based on $\mathsf{SD}$ over $\mathbb{F}_2$ and $\mathsf{PKP}$ feature sizes of $3.9$ kB and $3.6$ kB for NIST-I security level which is respectively $26\%$ and $38\%$ shorter than state-of-the-art alternatives. Our PoK of secret key of BIKE and HQC are twice shorter than similar PoK for Kyber. In addition, we obtain the smallest ring signature based on $\mathsf{SD}$ and the first ring signature based on $\mathsf{PKP}$.

  匹配依据：MPC: multi party computation

  </details>

- **Implementing Quantum Secret Sharing on Current Hardware**
  2024-10-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.11640)
  Jay Graves, Mike Nelson, Eric Chitambar

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing is a cryptographic scheme that enables a secure storage and reconstruction of quantum information. While the theory of secret sharing is mature in its development, relatively few studies have explored the performance of quantum secret sharing on actual devices. In this work, we provide a pedagogical description of encoding and decoding circuits for different secret sharing codes, and we test their performance on IBM&#x27;s 127-qubit Brisbane system. We evaluate the quality of implementation by performing a SWAP test between the decoded state and the ideal one, as well as by estimating how well the code preserves entanglement with a reference system. Results indicate that a ((3,5)) threshold secret sharing scheme performs slightly better overall than a ((5,7)) scheme based on the SWAP test, but is outperformed by the Steane Code scheme in regards to the entanglement fidelity. We also investigate one implementation of a ((2,3)) qutrit scheme and find that it performs the worst of all, which is expected due to the additional number of multi-qubit gate operations needed to encode and decode qutrits.

  匹配依据：MPC: secret sharing

  </details>

- **Computationally Efficient Asynchronous MPC with Linear Communication and Low Additive Overhead**
  2024-10-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1666)
  Akhil Bandarupalli, Xiaoyu Ji, Aniket Kate, Chen-Da Liu-Zhang, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  We explore the setting of asynchronous multi-party computation (AMPC) with optimal resilience $n=3t+1$, and develop an efficient protocol that optimizes both communication and computation. The recent work by Goyal, Liu-Zhang, and Song [Crypto&#x27; 24] was the first to achieve AMPC with amortized linear communication cost without using computationally heavy public-key cryptography. However, its $\mathcal{O}(n^{14})$ additive communication overhead renders it impractical for most real-world applications. It is possible to reduce the communication overhead significantly by leveraging cryptographic tools such as %random oracle hash, homomorphic commitments, public-key cryptography, or zero-knowledge proofs; however, the corresponding AMPC protocols introduce computation overhead of $\Omega(nC)$ public-key cryptographic operations that become bottleneck as $n$ grows. Overall, achieving AMPC with linear communication complexity, low additive communication overhead, and low computation overhead remains an open challenge. In this work, we resolve this efficiency challenge by utilizing the random oracle model. By relying solely on computationally efficient primitives such as random oracle hash and symmetric-key cryptography, our protocol is not only efficient in terms of computation and communication overhead but also post-quantum secure. For a circuit with $C$ multiplication gates, our protocol achieves $\mathcal{O}(Cn)$ communication per multiplication gate with an additive overhead of $\mathcal{O}(n^4)$ communication. In terms of computation, our protocol only introduces an additive overhead of $\mathcal{O}(n^5)$ hash computations independent of the circuit size.

  匹配依据：MPC: multi party computation

  </details>

- **High-Throughput Three-Party DPFs with Applications to ORAM and Digital Currencies**
  2024-10-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1658)
  Guy Zyskind, Avishay Yanai, Alex "Sandy" Pentland

  <details><summary>摘要 / Abstract</summary>

  Distributed point functions (DPF) are increasingly becoming a foundational tool with applications for application-specific and general secure computation. While two-party DPF constructions are readily available for those applications with satisfiable performance, the three-party ones are left behind in both security and efficiency. In this paper we close this gap and propose the first three-party DPF construction that matches the state-of-the-art two-party DPF on all metrics. Namely, it is secure against a malicious adversary corrupting both the dealer and one out of the three evaluators, its function&#x27;s shares are of the same size and evaluation takes the same time as in the best two-party DPF. Compared to the state-of-the-art three-party DPF, our construction enjoys $40-120\times$ smaller function&#x27;s share size and shorter evaluation time, for function domains of $2^{16}-2^{40}$, respectively. Apart from DPFs as a stand-alone tool, our construction finds immediate applications to private information retrieval (PIR), writing (PIW) and oblivious RAM (ORAM). To further showcase its applicability, we design and implement an ORAM with access policy, an extension to ORAMs where a policy is being checked before accessing the underlying database. The policy we plug-in is the one suitable for account-based digital currencies, and in particular to central bank digital currencies (CBDCs). Our protocol offers the first design and implementation of a large scale privacy-preserving account-based digital currency. While previous works supported anonymity sets of 64-256 clients and less than 10 transactions per second (tps), our protocol supports anonymity sets in the millions, performing $\{500,200,58\}$ tps for anonymity sets of $\{2^{16},2^{18},2^{20}\}$, respectively. Toward that application, we introduce a new primitive called updatable DPF, which enables a direct computation of a dot product between a DPF and a vector; we believe that updatable DPF and the new dot-product protocol will find interest in other applications.

  匹配依据：MPC: secure computation

  </details>

- **AD-MPC: Asynchronous Dynamic MPC with Guaranteed Output Delivery**
  2024-10-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1653)
  Wenxuan Yu, Minghui Xu, Bing Wu, Sisi Duan, Xiuzhen Cheng

  <details><summary>摘要 / Abstract</summary>

  MPC-as-a-Service (MPCaaS) systems enable clients to outsource privacy-preserving computations to distributed servers, offering flexibility by adapting and configuring MPC protocols to meet diverse security requirements. However, traditional MPC protocols rely on a fixed set of servers for the entire computation process, limiting scalability. Dynamic MPC (DMPC) addresses this limitation by permitting participants to join or leave during the computation. Nevertheless, existing DMPC protocols assume synchronous networks, which can lead to failures under unbounded network delays. In this paper, we present AD-MPC, the first asynchronous dynamic MPC protocol. Our protocol ensures guaranteed output delivery under optimal resilience ($n=3t+1$). To achieve this, we introduce two critical components: an asynchronous dynamic preprocessing protocol that facilitates the on-demand generation of Beaver triples for secure multiplication, and an asynchronous transfer protocol that maintains consistency during party hand-offs. These components collectively ensure computation correctness and transfer consistency across participants. We implement AD-MPC and evaluate its performance across up to 20 geographically distributed nodes. Experimental results demonstrate that the protocol not only offers strong security guarantees in dynamic and asynchronous network environments but also achieves performance comparable to state-of-the-art DMPC protocols.

  匹配依据：MPC: mpc (context)

  </details>

- **Fuzzy PSI via Oblivious Protocol Routing**
  2024-10-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1642)
  David Richardson, Mike Rosulek, Jiayu Xu

  <details><summary>摘要 / Abstract</summary>

  In private set intersection (PSI), two parties who each hold sets of items can learn their intersection without revealing anything about their other items. Fuzzy PSI corresponds to a relaxed variant that reveals pairs of items which are ``close enough,&#x27;&#x27; with respect to some distance metric. In this paper we propose a new protocol framework for fuzzy PSI, compatible with arbitrary distance metrics. We then show how to efficiently instantiate our framework for $\ell_1$, $\ell_2$, and $\ell_\infty$ metrics, in a way that uses exclusively cheap symmetric-key operations. One notable feature of our protocol is that it has only logarithmic dependency on the distance threshold, whereas most other protocols have linear (or higher) dependency. For many reasonable combinations of parameters, our protocol has the lowest communication cost of existing fuzzy PSI protocols.

  匹配依据：MPC: private set intersection

  </details>

- **Rhombus: Fast Homomorphic Matrix-Vector Multiplication for Secure Two-Party Inference**
  2024-10-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1611)
  Jiaxing He, Kang Yang, Guofeng Tang, Zhangjie Huang, Li Lin, Changzheng Wei, Ying Yan, Wei Wang

  <details><summary>摘要 / Abstract</summary>

  We present $\textit{Rhombus}$, a new secure matrix-vector multiplication (MVM) protocol in the semi-honest two-party setting, which is able to be seamlessly integrated into existing privacy-preserving machine learning (PPML) frameworks and serve as the basis of secure computation in linear layers. $\textit{Rhombus}$ adopts RLWE-based homomorphic encryption (HE) with coefficient encoding, which allows messages to be chosen from not only a field $\mathbb{F}_p$ but also a ring $\mathbb{Z}_{2^\ell}$, where the latter supports faster computation in non-linear layers. To achieve better efficiency, we develop an input-output packing technique that reduces the communication cost incurred by HE with coefficient encoding by about $21\times$, and propose a split-point picking technique that reduces the number of rotations to that sublinear in the matrix dimension. Compared to the recent protocol $\textit{HELiKs}$ by Balla and Koushanfar (CCS&#x27;23), our implementation demonstrates that $\textit{Rhombus}$ improves the whole performance of an MVM protocol by a factor of $7.4\times \sim 8\times$, and improves the end-to-end performance of secure two-party inference of ResNet50 by a factor of $4.6\times \sim 18\times$.

  匹配依据：MPC: secure computation

  </details>

- **Revisiting the Primitives of Transaction Fee Mechanism Design**
  2024-10-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.07566)
  Aadityan Ganesh, Clayton Thomas, S. Matthew Weinberg

  <details><summary>摘要 / Abstract</summary>

  Transaction Fee Mechanism Design studies auctions run by untrusted miners for transaction inclusion in a blockchain. Under previously-considered desiderata, an auction is considered `good&#x27; if, informally-speaking, each party (i.e., the miner, the users, and coalitions of both miners and users) has no incentive to deviate from the fixed and pre-determined protocol. In this paper, we propose a novel desideratum for transaction fee mechanisms. We say that a TFM is off-chain influence proof when the miner cannot achieve additional revenue by running a separate auction off-chain. While the previously-highlighted EIP-1559 is the gold-standard according to prior desiderata, we show that it does not satisfy off-chain influence proofness. Intuitively, this holds because a Bayesian revenue-maximizing miner can strictly increase profits by persuasively threatening to censor any bids that do not transfer a tip directly to the miner off-chain. On the other hand, we reconsider the Cryptographic (multi-party computation assisted) Second Price Auction mechanism, which is technically not `simple for miners&#x27; according to previous desiderata (since miners may wish to set a reserve by fabricating bids). We show that, in a slightly different model where the miner is allowed to set the reserve directly, this auction satisfies simplicity for users and miners, and off-chain influence proofness. Finally, we prove a strong impossibility result: no mechanism satisfies all previously-considered properties along with off-chain influence proofness, even with unlimited supply, and even after soliciting input from the miner.

  匹配依据：MPC: multi party computation

  </details>

- **PP-GWAS: Privacy Preserving Multi-Site Genome-wide Association Studies**
  2024-10-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.08122)
  Arjhun Swaminathan, Anika Hannemann, Ali Burak Ünal, Nico Pfeifer, Mete Akgün

  <details><summary>摘要 / Abstract</summary>

  Genome-wide association studies are pivotal in understanding the genetic underpinnings of complex traits and diseases. Collaborative, multi-site GWAS aim to enhance statistical power but face obstacles due to the sensitive nature of genomic data sharing. Current state-of-the-art methods provide a privacy-focused approach utilizing computationally expensive methods such as Secure Multi-Party Computation and Homomorphic Encryption. In this context, we present a novel algorithm PP-GWAS designed to improve upon existing standards in terms of computational efficiency and scalability without sacrificing data privacy. This algorithm employs randomized encoding within a distributed architecture to perform stacked ridge regression on a Linear Mixed Model to ensure rigorous analysis. Experimental evaluation with real world and synthetic data indicates that PP-GWAS can achieve computational speeds twice as fast as similar state-of-the-art algorithms while using lesser computational resources, all while adhering to a robust security model that caters to an all-but-one semi-honest adversary setting. We have assessed its performance using various datasets, emphasizing its potential in facilitating more efficient and private genomic analyses.

  匹配依据：MPC: secure multi party computation

  </details>
