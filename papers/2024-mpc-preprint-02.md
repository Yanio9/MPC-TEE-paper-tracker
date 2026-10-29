# 2024 · MPC · 仅预印本来源 · 第 2/5 页

[总目录](../PAPERS.md) · [上一页](2024-mpc-preprint-01.md) · [下一页](2024-mpc-preprint-03.md)

- **Non-Interactive Oblivious Transfer and One-Time Programs from Noisy Quantum Storage**
  2024-10-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.08367)
  Ricardo Faleiro, Manuel Goulão, Leonardo Novo, Emmanuel Zambrini Cruzeiro

  <details><summary>摘要 / Abstract</summary>

  Few primitives are as intertwined with the foundations of cryptography as Oblivious Transfer (OT). Not surprisingly, with the advent of quantum information processing, a major research path has emerged, aiming to minimize the requirements necessary to achieve OT by leveraging quantum resources, while also exploring the implications for secure computation. Indeed, OT has been the target of renewed focus regarding its newfound quantum possibilities (and impossibilities), both towards its computation and communication complexity. For instance, non-interactive OT, known to be impossible classically, has been strongly pursued. In its most extreme form, non-interactive chosen-input OT (one-shot OT) is equivalent to a One-Time Memory (OTM). OTMs have been proposed as tamper-proof hardware solutions for constructing One-Time Programs -- single-use programs that execute on an arbitrary input without revealing anything about their internal workings. In this work, we leverage quantum resources in the Noisy-Quantum-Storage Model to achieve: 1. Unconditionally-secure two-message non-interactive OT -- the smallest number of messages known to date for unconditionally-secure chosen-input OT. 2. Computationally-secure one-shot OT/OTM, with everlasting security, assuming only one-way functions and sequential functions -- without requiring trusted hardware, QROM, or pre-shared entanglement. 3. One-Time Programs without the need for hardware-based solutions or QROM, by compiling our OTM construction with the [GKR08, GIS+10] compiler.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **A New Approach Towards Encrypted Data Sharing and Computation: Enhancing Efficiency Beyond MPC and Multi-Key FHE**
  2024-10-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1622)
  Anil Kumar Pradhan

  <details><summary>摘要 / Abstract</summary>

  In this paper, we introduce a novel approach to Multi-Key Fully Homomorphic Encryption (MK-FHE) that enhances both efficiency and security beyond the capabilities of traditional MK-FHE and MultiParty Computation (MPC) systems. Our method generates a unified key structure, enabling constant ciphertext size and constant execution time for encrypted computations, regardless of the number of participants involved. This approach addresses critical limitations such as ciphertext size expansion, noise accumulation, and the complexity of relinearization, which typically hinder scalability in multi-user environments. We also propose a new decryption method that simplifies decryption to a single information exchange, in contrast to traditional multi-key FHE systems that require information to be passed between all parties sequentially. Additionally, it significantly enhances the scalability of MK-FHE systems, allowing seamless integration of additional participants without introducing performance overhead. Through theoretical analysis and practical implementation, we demonstrate the superiority of our approach in large-scale, collaborative encrypted computation scenarios, paving the way for more robust and efficient secure data processing frameworks. Further more, unlike the threshold based FHE schemes, the proposed system doesn’t require a centralised trusted third party to split and distribute the individual secret keys, instead each participant independently generates their own secret key, ensuring both security and decentralization.

  匹配依据：MPC: multiparty computation

  </details>

- **MORSE: An Efficient Homomorphic Secret Sharing Scheme Enabling Non-Linear Operation**
  2024-10-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.06514)
  Weiquan Deng, Bowen Zhao, Yang Xiao, Yantao Zhong, Qingqi Pei, Ximeng Liu

  <details><summary>摘要 / Abstract</summary>

  Homomorphic secret sharing (HSS) enables two servers to locally perform functions on encrypted data directly and obtain the results in the form of shares. A Paillier-based HSS solution seamlessly achieves multiplicative homomorphism and consumes less communication costs. Unfortunately, existing Paillier-based HSS schemes suffer from a large private key size, potential calculation error, expensive computation and storage overhead, and only valid on linear operations (e.g., addition and multiplication). To this end, inspired by the Paillier cryptosystem with fast encryption and decryption, we propose MORSE, an efficient homomorphic secret sharing scheme enabling non-linear operation, which enjoys a small key size, no calculation error and low overhead. In terms of functions, MORSE supports addition, subtraction, multiplication, scalar-multiplication, and comparison. Particularly, we carefully design two conversion protocols achieving the mutual conversion between one Paillier ciphertext and two secret shares, which allows MORSE to continuously perform the above operations. Rigorous analyses demonstrate that MORSE securely outputs correct results. Experimental results show that MORSE makes a runtime improvement of up to 9.3 times in terms of secure multiplication, and a communication costs reduction of up to 16.6% in secure comparison, compared to the state-of-the-art.

  匹配依据：MPC: secret sharing

  </details>

- **Matching radar signals and fingerprints with MPC**
  2024-10-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1590)
  Benjamin Hansen Mortensen, Mathias Karsrud Nordal, Martin Strand

  <details><summary>摘要 / Abstract</summary>

  Vessels can be recognised by their navigation radar due to the characteristics of the emitted radar signal. This is particularly useful if one wants to build situational awareness without revealing one&#x27;s own presence. Most countries maintain databases of radar fingerprints but will not readily share these due to national security regulations. Sharing of such information will generally require some form of information exchange agreement. However, all parties in a coalition benefit from correct identification. We use secure multiparty computation to match a radar signal measurement against secret databases and output plausible matches with their likelihoods. We also provide a demonstrator using MP-SPDZ.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Experimental coherent-state quantum secret sharing with finite pulses**
  2024-10-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.05836)
  Yuan-Zhuo Wang, Xiao-Ran Sun, Xiao-Yu Cao, Hua-Lei Yin, Zeng-Bing Chen

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) plays a significant role in multiparty quantum communication and is a crucial component of future quantum multiparty computing networks. Therefore, it is highly valuable to develop a QSS protocol that offers both information-theoretic security and validation in real optical systems under a finite-key regime. In this work, we propose a three-user QSS protocol based on phase-encoding technology. By adopting symmetric procedures for the two players, our protocol resolves the security loopholes introduced by asymmetric basis choice without prior knowledge of the identity of the malicious player. Kato&#x27;s concentration inequality is exploited to provide security against coherent attacks with the finite-key effect. Moreover, the practicality of our protocol has been validated under a 30-dB channel loss with a transmission distance of 5-km fiber. Our protocol achieves secure key rates ranging from 432 to 192 bps by choosing different pulse intensities and basis selection probabilities. Offering enhanced security and practicality, our protocol stands as an essential element for the realization of quantum multiparty computing networks.

  匹配依据：MPC: multiparty computing, secret sharing

  </details>

- **Attacks on Goldreich's Pseudorandom Generators by Grouping and Solving**
  2024-10-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1594)
  Ximing Fu, Mo Li, Shihan Lyu, Chuanyi Liu

  <details><summary>摘要 / Abstract</summary>

  Goldreich&#x27;s pseudorandom generators (PRGs) with constant locality admit highly parallel implementations, yet the concrete security of instantiations based on the $\mathsf{XOR}\text{-}\mathsf{THR}$ predicate has remained unclear. In this work, we present novel seed recovery attacks on Goldreich&#x27;s PRGs instantiated on $\mathsf{XOR}\text{-}\mathsf{THR}$ predicates with $m=n^s$, where $m$ and $n$ are the length of output and input, respectively. By partitioning the output bits into groups according to common input bits, high-biased noisy equations can be derived for the group whose common input bits are all 1s (or all 0s). Leveraging two solvers tailored to these equations, we achieve the seed recovery attacks, which needs roughly $2^{n(1-\log_2{(1 + \frac{2s}{\sqrt{2\pi (b-s)}})})}$ calls to Gaussian elimination when the input length of the $\mathsf{THR}$ predicate $b\geq (n-s)^{1/s}+s-1$ with small stretch $s$. Applying our attack to the $\mathsf{XOR}\text{-}\mathsf{MAJ}$ challenges in STOC 2016 yields complexity \(2^{\,n\!\left(1-\log_{2}\!\left(1+\sqrt{\frac{s}{18\pi}}\right)\right)} \le 2^{0.82n}\), i.e., at least a \(2^{0.18n}\) speedup over exhaustive search for any stretch \(s&gt;1\). We also deploy our attack on an instance used in the construction of silent oblivious transfer protocols (Eurocrypt 2024) with \(n = 256\). This attack is capable of breaking the instance using approximately \(2^{31.3}\) calls to Gaussian elimination over 244 variables. We successfully implemented the attack on a cluster of 14 CPU cores, recovering the seed in 71 hours, demonstrating the attack&#x27;s efficiency. Beyond PRGs, with appropriate adaptations our method extends to FiLIP stream ciphers instantiated with \mathsf{THR}-related predicates. Our evaluation indicates that most FiLIP instances do not meet their claimed security. For instance, the configuration \(\mathsf{XOR}_{100}\text{-}\mathsf{THR}_{11,22}\text{-}\mathsf{THR}_{11,22}\) is broken in about \(2^{59}\) calls to Gaussian elimination over 357 variables despite a 397-bit key and a claimed 80-bit security level.

  匹配依据：MPC: oblivious transfer

  </details>

- **A Systematic Study of Sparse LWE**
  2024-10-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1589)
  Aayush Jain, Huijia Lin, Sagnik Saha

  <details><summary>摘要 / Abstract</summary>

  In this work, we introduce the sparse LWE assumption, an assumption that draws inspiration from both Learning with Errors (Regev JACM 10) and Sparse Learning Parity with Noise (Alekhnovich FOCS 02). Exactly like LWE, this assumption posits indistinguishability of $(\mathbf{A}, \mathbf{s}\mathbf{A}+\mathbf{e} \mod p)$ from $(\mathbf{A}, \mathbf{u})$ for a random $\mathbf{u}$ where the secret $\mathbf{s}$, and the error vector $\mathbf{e}$ is generated exactly as in LWE. However, the coefficient matrix $\mathbf{A}$ in sparse LPN is chosen randomly from $\mathbb{Z}^{n\times m}_{p}$ so that each column has Hamming weight exactly $k$ for some small $k$. We study the problem in the regime where $k$ is a constant or polylogarithmic. The primary motivation for proposing this assumption is efficiency. Compared to LWE, the samples can be computed and stored with roughly $O(n/k)$ factor improvement in efficiency. Our results can be summarized as: Foundations: We show several properties of sparse LWE samples, including: 1) The hardness of LWE/LPN with dimension $k$ implies the hardness of sparse LWE/LPN with sparsity $k$ and arbitrary dimension $n \ge k$. 2) When the number of samples $m=\Omega(n \log p)$, length of the shortest vector of a lattice spanned by rows of a random sparse matrix is large, close to that of a random dense matrix of the same dimension (up to a small constant factor). 3) Trapdoors with small polynomial norm exist for random sparse matrices with dimension $n \times m = O(n \log p)$. 4) Efficient algorithms for sampling such matrices together with trapdoors exist when the dimension is $n \times m = \widetilde{\mathcal{O}}(n^2)$. Cryptanalysis: We examine the suite of algorithms that have been used to break LWE and sparse LPN. While naively many of the attacks that apply to LWE do not exploit sparsity, we consider natural extensions that make use of sparsity. We propose a model to capture all these attacks. Using this model we suggest heuristics on how to identify concrete parameters. Our initial cryptanalysis suggests that concretely sparse LWE with a modest $k$ and slightly bigger dimension than LWE will satisfy similar level of security as LWE with similar parameters. Applications: We show that the hardness of sparse LWE implies very efficient homomorphic encryption schemes for low degree computations. We obtain the first secret key Linearly Homomorphic Encryption (LHE) schemes with slightly super-constant, or even constant, overhead, which further has applications to private information retrieval, private set intersection, etc. We also obtain secret key homomorphic encryption for arbitrary constant-degree polynomials with slightly super-constant, or constant, overhead. We stress that our results are preliminary. However, our results make a strong case for further investigation of sparse LWE.

  匹配依据：MPC: private set intersection

  </details>

- **Efficient Pairing-Free Adaptable k-out-of-N Oblivious Transfer Protocols**
  2024-10-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1583)
  Keykhosro Khosravani, Taraneh Eghlidos, Mohammad reza Aref

  <details><summary>摘要 / Abstract</summary>

  Oblivious Transfer (OT) is one of the fundamental building blocks in cryptography that enables various privacy-preserving applications. Constructing efficient OT schemes has been an active research area. This paper presents three efficient two-round pairing-free k-out-of-n oblivious transfer protocols with standard security. Our constructions follow the minimal communication pattern: the receiver sends k messages to the sender, who responds with n+k messages, achieving the lowest data transmission among pairing-free k-out-of-n OT schemes. Furthermore, our protocols support adaptivity and enable the sender to encrypt the n messages offline, independent of the receiver’s variables, offering significant performance advantages in one-sender-multiple-receiver scenarios. We provide security proofs under the Computational Diffie-Hellman (CDH) and RSA assumptions, without relying on the Random Oracle Model. Our protocols combine minimal communication rounds, adaptivity, offline encryption capability, and provable security, making them well-suited for privacy-preserving applications requiring efficient oblivious transfer.

  匹配依据：MPC: oblivious transfer

  </details>

- **Efficiently-Thresholdizable Batched Identity Based Encryption, with Applications**
  2024-10-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1575)
  Amit Agarwal, Rex Fernando, Benny Pinkas

  <details><summary>摘要 / Abstract</summary>

  We propose a new cryptographic primitive called &quot;batched identity-based encryption&quot; (Batched IBE) and its thresholdized version. The new primitive allows encrypting messages with specific identities and batch labels, where the latter can represent, for example, a block number on a blockchain. Given an arbitrary subset of identities for a particular batch, our primitive enables efficient issuance of a single decryption key that can be used to decrypt all ciphertexts having identities that are included in the subset while preserving the privacy of all ciphertexts having identities that are excluded from the subset. At the heart of our construction is a new technique that enables public aggregation (i.e. without knowledge of any secrets) of any subset of identities, into a succinct digest. This digest is used to derive, via a master secret key, a single succinct decryption key for all the identities that were digested in this batch. In a threshold system, where the master key is distributed as secret shares among multiple authorities, our method significantly reduces the communication (and in some cases, computation) overhead for the authorities. It achieves this by making their costs for key issuance independent of the batch size. We present a concrete instantiation of a Batched IBE scheme based on the KZG polynomial commitment scheme by Kate et al. (Asiacrypt&#x27;10) and a modified form of the BLS signature scheme by Boneh et al. (Asiacrypt&#x27;01). The construction is proven secure in the generic group model (GGM). In a blockchain setting, the new construction can be used for achieving mempool privacy by encrypting transactions to a block, opening only the transactions included in a given block and hiding the transactions that are not included in it. With the thresholdized version, multiple authorities (validators) can collaboratively manage the decryption process. Other possible applications include scalable support via blockchain for fairness of dishonest majority MPC, and conditional batched threshold decryption that can be used for implementing secure Dutch auctions and privacy preserving options trading.

  匹配依据：MPC: mpc (context)

  </details>

- **Device-independent quantum secret sharing with advanced random key generation basis**
  2024-10-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.04003)
  Qi Zhang, Jia-Wei Ying, Zhong-Jian Wang, Wei Zhong, Ming-Ming Du, Shu-Ting Shen, Xi-Yun Li, An-Lei Zhang, Shi-Pu Gu, Xing-Fu Wang, Lan Zhou, Yu-Bo Sheng

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) enables a dealer to securely distribute keys to multiple players. Device-independent (DI) QSS can resist all possible attacks from practical imperfect devices and provide QSS the highest level of security in theory. However, DI QSS requires high-performance devices, especially for low-noise channels, which is a big challenge for its experimental demonstration. We propose a DI QSS protocol with the advanced random key generation basis strategy, which combines the random key generation basis with the noise preprocessing and postselection strategies. We develop the methods to simplify Eve&#x27;s conditional entropy bound and numerically simulate the key generation rate in an acceptable time. Our DI QSS protocol has some advantages. First, it can increase the noise tolerance threshold from initial 7.147% to 9.231% (29.16% growth), and reduce the global detection efficiency threshold from 96.32% to 93.41%. The maximal distance between any two users increases to 1.43 km, which is about 5.5 times of the initial value. Second, by randomly selecting two basis combinations to generate the key, our DI QSS protocol can reduce the entanglement resource consumption. Our protocol has potential for DI QSS&#x27;s experimental demonstration and application in the future.

  匹配依据：MPC: secret sharing

  </details>

- **Bounded Collusion-Resistant Registered Functional Encryption for Circuits**
  2024-10-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1572)
  Yijian Zhang, Jie Chen, Debiao He, Yuqing Zhang

  <details><summary>摘要 / Abstract</summary>

  As an emerging primitive, Registered Functional Encryption (RFE) eliminates the key-escrow issue that threatens numerous works for functional encryption, by replacing the trusted authority with a transparent key curator and allowing each user to sample their decryption keys locally. In this work, we present a new black-box approach to construct RFE for all polynomial-sized circuits. It considers adaptive simulation-based security in the bounded collusion model (Gorbunov et al. - CRYPTO&#x27;12), where the security can be ensured only if there are no more than Q &gt;= 1 corrupted users and $Q$ is fixed at the setup phase. Unlike earlier works, we do not employ unpractical Indistinguishability Obfuscation (iO). Conversely, it can be extended to support unbounded users, which is previously only known from iO. Technically, our general compiler exploits garbled circuits and a novel variant of slotted Registered Broadcast Encryption (RBE), namely global slotted RBE. This primitive is similar to slotted RBE, but needs optimally compact public parameters and ciphertext, so as to satisfy the efficiency requirement of the resulting RFE. Then we present two concrete global slotted RBE from pairings and lattices, respectively. With proposed compiler, we hence obtain two bounded collusion-resistant RFE schemes. Here, the first scheme relies on k-Lin assumption, while the second one supports unbounded users under LWE and evasive LWE assumptions.

  匹配依据：MPC: garbled circuits

  </details>

- **Private Set Operations from Circuit-Based PSI**
  2024-10-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1560)
  Jiseung Kim, Hyung Tae Lee, Yongha Son

  <details><summary>摘要 / Abstract</summary>

  Private set operations~(PSOs) have been extensively studied due to their wide range of applications. In many practical scenarios, it is essential to perform advanced computations on the set operation result while maintaining the security. However, existing PSO protocols for advanced computations often suffer from the during-execution leakage, allowing an adversary to extract additional information beyond the final operation result. In this paper, we propose a novel framework for constructing PSO protocols by leveraging circuit-based private set intersection~(circuit-PSI) in a black-box manner, enabling a range of advanced operations on the set intersection result while mitigating information leakage. Specifically, we present PSI variants, including PSI-Sum, which computes the sum of associated values; PSI-Card, which determines the cardinality of the intersection; PSI-Threshold, which evaluates whether the intersection cardinality exceeds a given threshold; and PSI-InnerProd, which computes the inner product of vectors associated with the intersection. We also provide a private set union~(PSU) protocol based on circuit-PSI without the during-execution leakage. To evaluate the efficiency of our proposed protocols, we provide implementation results of ours and existing PSO protocols closely related to our work. The experimental results demonstrate that our proposed protocols achieve performance comparable to state-of-the-art methods, while resolving the during-execution leakage that the state-of-the-art methods suffer from. Furthermore, as a unique feature of our proposals, our protocols can significantly reduce the online protocol execution time by separating time-consuming setup phase, which comes from the preprocessing optimization of circuit-PSI. In terms of online execution time, PSI-Card and PSI-Sum show a 9.92--13$\times$ improvement over prior work, while PSU achieves a 4.8--5.2$\times$ speedup. Additionally, PSI-InnerProd demonstrates a remarkable 47--56$\times$ speedup over the previous result over a LAN network environment.

  匹配依据：MPC: private set intersection, private set union

  </details>

- **Oracle Separation Between Quantum Commitments and Quantum One-wayness**
  2024-10-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.03358) · [IACR ePrint](https://eprint.iacr.org/2024/1568)
  John Bostanci, Boyang Chen, Barak Nehoran

  <details><summary>摘要 / Abstract</summary>

  We show that there exists a unitary quantum oracle relative to which quantum commitments exist but no (efficiently verifiable) one-way state generators exist. Both have been widely considered candidates for replacing one-way functions as the minimal assumption for cryptography—the weakest cryptographic assumption implied by all of computational cryptography. Recent work has shown that commitments can be constructed from one-way state generators, but the other direction has remained open. Our results rule out any black-box construction, and thus settle this crucial open problem, suggesting that quantum commitments (as well as its equivalency class of EFI pairs, quantum oblivious transfer, and secure quantum multiparty computation) appear to be strictly weakest among all known cryptographic primitives.

  匹配依据：MPC: multiparty computation, oblivious transfer

  </details>

- **SNARKs for Virtual Machines are Non-Malleable**
  2024-10-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1551)
  Matteo Campanelli, Antonio Faonio, Luigi Russo

  <details><summary>摘要 / Abstract</summary>

  Cryptographic proof systems have a plethora of applications: from building other cryptographic tools (e.g., malicious security for MPC protocols) to concrete settings such as private transactions or rollups. In several settings it is important for proof systems to be non-malleable: an adversary should not to be able to modify a proof they have observed into another for a statement for which they do not know the witness. Proof systems that have been deployed in practice should arguably satisfy this notion: it is crucial in settings such as transaction systems and in order to securely compose proofs with other cryptographic protocols. As a consequence, results on non-malleability should keep up with designs of proofs being deployed. Recently, Arun et al. proposed $\mathsf{Jolt}$ (Eurocrypt 2024), arguably the first efficient proof system whose architecture is based on the lookup singularity approach (Barry Whitehat, 2022). This approach consists in representing a general computation as a series of table lookups. The final result is a SNARK for a Virtual Machine execution (or SNARK VM). Both SNARK VMs and lookup-singularity SNARKs are architectures with enormous potential and will probably be adopted more and more in the next years (and they already are). As of today, however, there is no literature regarding the non-malleability of SNARK VMs. The goal of this work is to fill this gap by providing both concrete non-malleability results and a set of technical tools for a more general study of SNARK VMs security (as well as &quot;modular&quot; SNARKs in general). As a concrete result, we study the non-malleability of (an idealized version of) $\mathsf{Jolt}$ and its fundamental building block, the lookup argument $\mathsf{Lasso}$. While connecting our new result on the non-malleability of $\mathsf{Lasso}$ to that of $\mathsf{Jolt}$, we develop a set of tools that enable the composition of non-malleable SNARKs. We believe this toolbox to be valuable in its own right.

  匹配依据：MPC: mpc (context)

  </details>

- **GORAM: Graph-oriented ORAM for Efficient Ego-centric Queries on Federated Graphs**
  2024-10-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.02234)
  Xiaoyu Fan, Kun Chen, Jiping Yu, Xiaowei Zhu, Yunyi Chen, Huanchen Zhang, Wei Xu

  <details><summary>摘要 / Abstract</summary>

  Ego-centric queries, focusing on a target vertex and its direct neighbors, are essential for various applications. Enabling such queries on graphs owned by mutually distrustful data providers, without breaching privacy, holds promise for more comprehensive results. In this paper, we propose GORAM, a graph-oriented data structure that enables efficient ego-centric queries on federated graphs with strong privacy guarantees. GORAM is built upon secure multi-party computation (MPC) and ensures that no single party can learn any sensitive information about the graph data or the querying keys during the process. However, achieving practical performance with privacy guaranteed presents a challenge. To overcome this, GORAM is designed to partition the federated graph and construct an Oblivious RAM(ORAM)-inspired index atop these partitions. This design enables each ego-centric query to process only a single partition, which can be accessed fast and securely. To evaluate the performance of GORAM, we developed a prototype querying engine on a real-world MPC framework. We conduct a comprehensive evaluation with five commonly used queries on both synthetic and real-world graphs. Our evaluation shows that all benchmark queries can be completed in just 58.1 milliseconds to 35.7 seconds, even on graphs with up to 41.6 million vertices and 1.4 billion edges. To the best of our knowledge, this represents the first instance of processing billion-scale graphs with practical performance on MPC.

  匹配依据：MPC: secure multi party computation

  </details>

- **VOLE-in-the-head signatures from Subfield Bilinear Collisions**
  2024-10-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1537)
  Janik Huth, Antoine Joux

  <details><summary>摘要 / Abstract</summary>

  In this paper, we introduce a new signature scheme based on the subfield bilinear collision problem published at Crypto 2024. We use techniques based on vector oblivious linear evaluation (VOLE) to significantly improve both the running time and the signature size of the scheme compared to the MPC-in-the-Head version. Furthermore, we introduce the correlated GGM forest construction, which is a generic method to correlate several GGM trees across multiple rounds of the signature scheme. This construction combines the correlated tree derivation with the hypercube folding in a layered construction.

  匹配依据：MPC: mpc (context)

  </details>

- **More Efficient Lattice-based OLE from Circuit-private Linear HE with Polynomial Overhead**
  2024-10-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1534)
  Leo de Castro, Duhyeong Kim, Miran Kim, Keewoo Lee, Seonhong Min, Yongsoo Song

  <details><summary>摘要 / Abstract</summary>

  We present a new and efficient method to obtain circuit privacy for lattice-based linearly homomorphic encryptions (LHE). In particular, our method does not involve noise-flooding with exponetially large errors or iterative bootstrapping. As a direct result, we obtain a semi-honest oblivious linear evaluation (OLE) protocol with the same efficiency, reducing the communication cost of the prior state of the art by 50%. Consequently, the amortized time of our protocol improves the prior work by 33% under 100Mbps network setting. Our semi-honest OLE is the first to achieve both concrete efficiency and asymptotic quasi-optimality. Together with an extension of the recent zero-knowledge proof of plaintext knowledge, our LHE yields actively-secure OLE with 2.7x reduced communication from the prior work. When applied to Overdrive (Eurocrypt &#x27;18), an MPC preprocessing protocol, our method provides 1.4x improvement in communication over the state of the art.

  匹配依据：MPC: mpc (context)

  </details>

- **Local equivalence of stabilizer states: a graphical characterisation**
  2024-09-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.20183)
  Nathan Claudet, Simon Perdrix

  <details><summary>摘要 / Abstract</summary>

  Stabilizer states form a ubiquitous family of quantum states that can be graphically represented through the graph state formalism. A fundamental property of graph states is that applying a local complementation - a well-known and extensively studied graph transformation - results in a graph that represents the same entanglement as the original. In other words, the corresponding graph states are LU-equivalent. This property served as the cornerstone for capturing non-trivial quantum properties in a simple graphical manner, in the study of quantum entanglement but also for developing protocols and models based on graph states and stabilizer states, such as measurement-based quantum computing, secret sharing, error correction, entanglement distribution... However, local complementation fails short to fully characterise entanglement: there exist pairs of graph states that are LU-equivalent but cannot be transformed one into the other using local complementations. Only few is known about the equivalence of graph states beyond local complementation. We introduce a generalisation of local complementation which graphically characterises the LU-equivalence of graph states. We use this characterisation to show the existence of a strict infinite hierarchy of equivalences of graph states. Our approach is based on minimal local sets, which are subsets of vertices that are known to cover any graph, and to be invariant under local complementation and even LU-equivalence. We use these structures to provide a type to each vertex of a graph, leading to a natural standard form in which the LU-equivalence can be exhibited and captured by means of generalised local complementation.

  匹配依据：MPC: secret sharing

  </details>

- **Bitwise Garbling Schemes --- A Model with $\\frac{3}{2}\\kappa$-bit Lower Bound of Ciphertexts**
  2024-09-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1532)
  Fei Xu, Honggang Hu, Changhong Xu

  <details><summary>摘要 / Abstract</summary>

  At Eurocrypt 2015, Zahur, Rosulek, and Evans proposed the model of Linear Garbling Schemes. This model proved a $2\kappa$-bit lower bound of ciphertexts for a broad class of garbling schemes. At Crypto 2021, Rosulek and Roy presented the innovative &quot;three-halves&quot; garbling scheme in which AND gates cost $1.5\kappa+5$ bits and XOR gates are free. A noteworthy aspect of their scheme is the slicing-and-dicing technique, which is applicable universally to all AND gates when garbling a boolean circuit. Following this revelation, Rosulek and Roy presented several open problems. Our research primarily addresses one of them: ``Is $1.5\kappa$ bits optimal for garbled AND gates in a more inclusive model than Linear Garbling Schemes?&#x27;&#x27; In this paper, we propose theBitwise Garbling Schemes. Our key revelation is that $1.5\kappa$ bits is indeed optimal for arbitrary garbled AND gates in our model. Moreover, we prove the necessity of the free-XOR technique: If free-XOR is forbidden, we prove a $2\kappa$-bit lower bound. As an extension, we apply our idea to construct a model for fan-in 3 gates. Somewhat unexpectedly, we prove a $\frac{7}{4}\kappa$-bit lower bound. Unfortunately, the corresponding construction is not suitable for 3-input AND gates. This construction may be of independent interest.

  匹配依据：MPC: garbling scheme, garbling schemes

  </details>

- **BEAT-MEV: Epochless Approach to Batched Threshold Encryption for MEV Prevention**
  2024-09-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1533)
  Jan Bormet, Sebastian Faust, Hussien Othman, Ziyan Qu

  <details><summary>摘要 / Abstract</summary>

  In decentralized finance (DeFi), the public availability of pending transactions presents significant privacy concerns, enabling market manipulation through miner extractable value (MEV). MEV occurs when block proposers exploit the ability to reorder, omit, or include transactions, causing financial loss to users from frontrunning. Recent research has focused on encrypting pending transactions, hiding transaction data until block finalization. To this end, Choudhuri et al. (USENIX &#x27;24) introduce an elegant new primitive called Batched Threshold Encryption (BTE) where a batch of encrypted transactions is selected by a committee and only decrypted after block finalization. Crucially, BTE achieves low communication complexity during decryption and guarantees that all encrypted transactions outside the batch remain private. An important shortcoming of their construction is, however, that it progresses in epochs and requires a costly setup in MPC for each batch decryption. In this work, we introduce a novel BTE scheme addressing the limitations by eliminating the need for an expensive epoch setup while achieving practical encryption and decryption times. Additionally, we explore a previously ignored question of how users can coordinate their transactions, which is crucial for the functionality of the system. Along the way, we present several optimizations and trade-offs between communication and computational complexity that allows us to achieve practical performance on standard hardware ($&lt;2$ ms for encryption and $&lt;440$ ms for decrypting $512$ transactions). Finally, we prove our constructions secure in a model that captures practical attacks on MEV-prevention mechanisms.

  匹配依据：MPC: mpc (context)

  </details>

- **Do LLMs suffer from Multi-Party Hangover? A Diagnostic Approach to Addressee Recognition and Response Selection in Conversations**
  2024-09-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.18602)
  Nicolò Penzo, Maryam Sajedinia, Bruno Lepri, Sara Tonelli, Marco Guerini

  <details><summary>摘要 / Abstract</summary>

  Assessing the performance of systems to classify Multi-Party Conversations (MPC) is challenging due to the interconnection between linguistic and structural characteristics of conversations. Conventional evaluation methods often overlook variances in model behavior across different levels of structural complexity on interaction graphs. In this work, we propose a methodological pipeline to investigate model performance across specific structural attributes of conversations. As a proof of concept we focus on Response Selection and Addressee Recognition tasks, to diagnose model weaknesses. To this end, we extract representative diagnostic subdatasets with a fixed number of users and a good structural variety from a large and open corpus of online MPCs. We further frame our work in terms of data minimization, avoiding the use of original usernames to preserve privacy, and propose alternatives to using original text messages. Results show that response selection relies more on the textual content of conversations, while addressee recognition requires capturing their structural dimension. Using an LLM in a zero-shot setting, we further highlight how sensitivity to prompt variations is task-dependent.

  匹配依据：MPC: mpc (context)

  </details>

- **Practical Mempool Privacy via One-time Setup Batched Threshold Encryption**
  2024-09-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1516)
  Arka Rai Choudhuri, Sanjam Garg, Guru-Vamsi Policharla, Mingyuan Wang

  <details><summary>摘要 / Abstract</summary>

  An important consideration with the growth of the DeFi ecosystem is the protection of clients who submit transactions to the system. As it currently stands, the public visibility of these transactions in the memory pool (mempool) makes them susceptible to market manipulations such as frontrunning and backrunning. More broadly, for various reasons—ranging from avoiding market manipulation to including time-sensitive information in their transactions—clients may want the contents of their transactions to remain private until they are executed, i.e. they have *pending transaction privacy*. Therefore, *mempool privacy* is becoming an increasingly important feature as DeFi applications continue to spread. We construct the first *practical* mempool privacy scheme that uses a *one-time* DKG setup for $n$ decryption servers. Our scheme ensures the strong privacy requirement by not only hiding the transactions until they are decrypted but also guaranteeing privacy for transactions that were not selected in the epoch (*pending transaction privacy*). For each epoch (or block), clients can encrypt their transactions so that, once $B$ (encrypted) transactions are selected for the epoch, they can be decrypted by each decryption server while communicating only $O(1)$ information. Our result improves upon the best-known prior works, which either: (i) require an expensive initial setup involving a (special purpose) multiparty computation protocol executed by the $n$ decryption servers, along with an additional *per-epoch* setup; (ii) require each decryption server to communicate $O(B)$ information; or (iii) do not guarantee pending transaction privacy. We implement our scheme and find that transactions can be encrypted in approximately 8.5 ms, independent of committee size, and the communication required to decrypt an entire batch of transactions is 48 bytes per party, independent of the number of transactions. If deployed on Ethereum, which processes close to 500 transactions per block, it takes close to 3.2 s for each committee member to compute a partial decryption and 3.0 s to decrypt all transactions for a block in single-threaded mode. Compared to prior work, which had an expensive setup phase per epoch, we incur $&lt;2\times$ overhead in the worst case. On some metrics such as partial decryptions size, we actually fare better.

  匹配依据：MPC: multiparty computation

  </details>

- **Incomplete quantum oblivious transfer with perfect one-sided security**
  2024-09-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.17571)
  David Reichmuth, Ittoop Vergheese Puthoor, Petros Wallden, Erika Andersson

  <details><summary>摘要 / Abstract</summary>

  Oblivious transfer is a fundamental cryptographic primitive which is useful for secure multiparty computation. There are several variants of oblivious transfer. We consider 1 out of 2 oblivious transfer, where a sender sends two bits of information to a receiver. The receiver only receives one of the two bits, while the sender does not know which bit the receiver has received. Perfect quantum oblivious transfer with information theoretic security is known to be impossible. We aim to find the lowest possible cheating probabilities. Bounds on cheating probabilities have been investigated for complete protocols, where if both parties follow the protocol, the bit value obtained by the receiver matches the sender bit value. We instead investigate incomplete protocols, where the receiver obtains an incorrect bit value with probability pf. We present optimal non interactive protocols where Alice bit values are encoded in four symmetric pure quantum states, and where she cannot cheat better than with a random guess. We find the protocols such that for a given pf, Bob cheating probability pr is as low as possible, and vice versa. Furthermore, we show that non-interactive quantum protocols can outperform non-interactive classical protocols, and give a lower bound on Bob cheating probability in interactive quantum protocols. Importantly for optical implementations, our protocols do not require entanglement nor quantum memory.

  匹配依据：MPC: oblivious transfer, secure multiparty computation

  </details>

- **A Comprehensive Review of TLSNotary Protocol**
  2024-09-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.17670)
  Maciej Kalka, Marek Kirejczyk

  <details><summary>摘要 / Abstract</summary>

  Transport Layer Security (TLS) protocol is a cryptographic protocol designed to secure communication over the internet. The TLS protocol has become a fundamental in secure communication, most commonly used for securing web browsing sessions. In this work, we investigate the TLSNotary protocol, which aim to enable the Client to obtain proof of provenance for data from TLS session, while getting as much as possible from the TLS security properties. To achieve such proofs without any Server-side adjustments or permissions, the power of secure multi-party computation (MPC) together with zero knowledge proofs is used to extend the standard TLS Protocol. To make the compliacted landscape of MPC as comprehensible as possible we first introduce the cryptographic primitives required to understand the TLSNotary protocol and go through standard TLS protocol. Finally, we look at the TLSNotary protocol in detail.

  匹配依据：MPC: secure multi party computation

  </details>

- **PhD Forum: Efficient Privacy-Preserving Processing via Memory-Centric Computing**
  2024-09-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.16777)
  Mpoki Mwaisela

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving computation techniques like homomorphic encryption (HE) and secure multi-party computation (SMPC) enhance data security by enabling processing on encrypted data. However, the significant computational and CPU-DRAM data movement overhead resulting from the underlying cryptographic algorithms impedes the adoption of these techniques in practice. Existing approaches focus on improving computational overhead using specialized hardware like GPUs and FPGAs, but these methods still suffer from the same processor-DRAM overhead. Novel hardware technologies that support in-memory processing have the potential to address this problem. Memory-centric computing, or processing-in-memory (PIM), brings computation closer to data by introducing low-power processors called data processing units (DPUs) into memory. Besides its in-memory computation capability, PIM provides extensive parallelism, resulting in significant performance improvement over state-of-the-art approaches. We propose a framework that uses recently available PIM hardware to achieve efficient privacy-preserving computation. Our design consists of a four-layer architecture: (1) an application layer that decouples privacy-preserving applications from the underlying protocols and hardware; (2) a protocol layer that implements existing secure computation protocols (HE and MPC); (3) a data orchestration layer that leverages data compression techniques to mitigate the data transfer overhead between DPUs and host memory; (4) a computation layer which implements DPU kernels on which secure computation algorithms are built.

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **MatriGear: Accelerating Authenticated Matrix Triple Generation with Scalable Prime Fields via Optimized HE Packing**
  2024-09-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1502)
  Hyunho Cha, Intak Hwang, Seonhong Min, Jinyeong Seo, Yongsoo Song

  <details><summary>摘要 / Abstract</summary>

  The SPDZ protocol family is a popular choice for secure multi-party computation (MPC) in a dishonest majority setting with active adversaries. Over the past decade, a series of studies have focused on improving its offline phase, where special additive shares called authenticated triples are generated. However, to accommodate recent demands for matrix operations in secure machine learning and big integer arithmetic in distributed RSA key generation, updates to the offline phase are required. In this work, we propose a new protocol for the SPDZ offline phase, MatriGear, which improves upon the previous state-of-the-art construction, TopGear (Baum et al., SAC &#x27;19), and its variant for matrix triples (Chen et al., Asiacrypt &#x27;20). Our protocol aims to achieve a speedup in matrix triple generation and support for larger prime fields up to 4096 bits in size. To achieve this, we devise a variant of the BFV scheme and a new homomorphic matrix multiplication algorithm optimized for our purpose. As a result, our protocol achieves about 3.6x speedup for generating scalar triples in a 1024-bit prime field and about 34x speedup for generating 128x128 matrix triples. In addition, we reduce the size of evaluation keys from 27.4 GB to 0.22 GB and the communication cost for MAC key generation from 816 MB to 16.6 MB.

  匹配依据：MPC: secure multi party computation

  </details>

- **CryptoTrain: Fast Secure Training on Encrypted Dataset**
  2024-09-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.16675)
  Jiaqi Xue, Yancheng Zhang, Yanshan Wang, Xueqiang Wang, Hao Zheng, Qian Lou

  <details><summary>摘要 / Abstract</summary>

  Secure training, while protecting the confidentiality of both data and model weights, typically incurs significant training overhead. Traditional Fully Homomorphic Encryption (FHE)-based non-inter-active training models are heavily burdened by computationally demanding bootstrapping. To develop an efficient secure training system, we established a foundational framework, CryptoTrain-B, utilizing a hybrid cryptographic protocol that merges FHE with Oblivious Transfer (OT) for handling linear and non-linear operations, respectively. This integration eliminates the need for costly bootstrapping. Although CryptoTrain-B sets a new baseline in performance, reducing its training overhead remains essential. We found that ciphertext-ciphertext multiplication (CCMul) is a critical bottleneck in operations involving encrypted inputs and models. Our solution, the CCMul-Precompute technique, involves precomputing CCMul offline and resorting to the less resource-intensive ciphertext-plaintext multiplication (CPMul) during private training. Furthermore, conventional polynomial convolution in FHE systems tends to encode irrelevant and redundant values into polynomial slots, necessitating additional polynomials and ciphertexts for input representation and leading to extra multiplications. Addressing this, we introduce correlated polynomial convolution, which encodes only related input values into polynomials, thus drastically reducing the number of computations and overheads. By integrating CCMul-Precompute and correlated polynomial convolution into CryptoTrain-B, we facilitate a rapid and efficient secure training framework, CryptoTrain. Extensive experiments demonstrate that CryptoTrain achieves a ~5.3X training time reduction compared to prior methods.

  匹配依据：MPC: oblivious transfer

  </details>

- **Low-degree Security of the Planted Random Subgraph Problem**
  2024-09-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.16227) · [IACR ePrint](https://eprint.iacr.org/2024/1497)
  Andrej Bogdanov, Chris Jones, Alon Rosen, Ilias Zadik

  <details><summary>摘要 / Abstract</summary>

  The planted random subgraph detection conjecture of Abram et al. (TCC 2023) asserts the pseudorandomness of a pair of graphs $(H, G)$, where $G$ is an Erdos-Renyi random graph on $n$ vertices, and $H$ is a random induced subgraph of $G$ on $k$ vertices. Assuming the hardness of distinguishing these two distributions (with two leaked vertices), Abram et al. construct communication-efficient, computationally secure (1) 2-party private simultaneous messages (PSM) and (2) secret sharing for forbidden graph structures. We prove the low-degree hardness of detecting planted random subgraphs all the way up to $k\leq n^{1 - \Omega(1)}$. This improves over Abram et al.&#x27;s analysis for $k \leq n^{1/2 - \Omega(1)}$. The hardness extends to $r$-uniform hypergraphs for constant $r$. Our analysis is tight in the distinguisher&#x27;s degree, its advantage, and in the number of leaked vertices. Extending the constructions of Abram et al, we apply the conjecture towards (1) communication-optimal multiparty PSM protocols for random functions and (2) bit secret sharing with share size $(1 + \epsilon)\log n$ for any $\epsilon &gt; 0$ in which arbitrary minimal coalitions of up to $r$ parties can reconstruct and secrecy holds against all unqualified subsets of up to $\ell = o(\epsilon \log n)^{1/(r-1)}$ parties.

  匹配依据：MPC: secret sharing

  </details>

- **Concretely Efficient Private Set Union via Circuit-based PSI**
  2024-09-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1494)
  Gowri R Chandran, Thomas Schneider, Maximilian Stillger, Christian Weinert

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) is a type of private set operation (PSO) for which concretely efficient linear-complexity protocols do exist. However, the situation is currently less satisfactory for other relevant PSO problems such as private set union (PSU): For PSU, the most promising protocols either rely entirely on computationally expensive public-key operations or suffer from substantial communication overhead. In this work, we present the first PSU protocol that is mainly based on efficient symmetric-key primitives yet enjoys comparable communication as public-key-based alternatives. Our core idea is to re-purpose state-of-the-art circuit-based PSI to realize a multi-query reverse private membership test (mq-RPMT), which is instrumental for building PSU. We carefully analyze a privacy leakage issue resulting from the hashing paradigm commonly utilized in circuit-based PSI and show how to mitigate this via oblivious pseudorandom function (OPRF) and new shuffle sub-protocols. Our protocol is modularly designed as a sequential execution of different building blocks that can be easily replaced by more efficient variants in the future, which will directly benefit the overall performance. We implement our resulting PSU protocol, showing a run-time improvement of 10% over the state-of-the-art public-key-based protocol of Chen et al. (PKC&#x27;24) for input sets of size $2^{20}$. Furthermore, we improve communication by $1.6\times$ over the state-of-the-art symmetric-key-based protocol of Zhang et al. (USENIX Sec&#x27;23).

  匹配依据：MPC: private set intersection, private set union

  </details>

- **UTrace: Poisoning Forensics for Private Collaborative Learning**
  2024-09-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.15126)
  Evan Rose, Hidde Lycklama, Harsh Chaudhari, Niklas Britz, Anwar Hithnawi, Alina Oprea

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving machine learning (PPML) systems enable multiple data owners to collaboratively train models without revealing their raw, sensitive data by leveraging cryptographic protocols such as secure multi-party computation (MPC). While PPML offers strong privacy guarantees, it also introduces new attack surfaces: malicious data owners can inject poisoned data into the training process without being detected, thus undermining the integrity of the learned model. Although recent defenses, such as private input validation within MPC, can mitigate some specific poisoning strategies, they remain insufficient, particularly in preventing stealthy or distributed attacks. As the robustness of PPML remains an open challenge, strengthening trust in these systems increasingly necessitates post-hoc auditing mechanisms that instill accountability. In this paper we present UTrace, a framework for user-level traceback in PPML that attributes integrity failures to responsible data owners without compromising the privacy guarantees of MPC. UTrace encapsulates two mechanisms: a gradient similarity method that identifies suspicious update patterns linked to poisoning, and a user-level unlearning technique that quantifies each user&#x27;s marginal influence on model behavior. Together, these methods allow UTrace to attribute model misbehavior to specific users with high precision. We implement UTrace within an MPC-compatible training and auditing pipeline and evaluate its effectiveness on four datasets spanning vision, text, and malware. Across ten canonical poisoning attacks, UTrace consistently achieves high detection accuracy with low false positive rates.

  匹配依据：MPC: secure multi party computation

  </details>

- **PrivaMatch: A Privacy-Preserving DNA Matching Scheme for Forensic Investigation**
  2024-09-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.14798)
  Sankha Das

  <details><summary>摘要 / Abstract</summary>

  DNA fingerprinting and matching for identifying suspects has been a common practice in criminal investigation. Such proceedings involve multiple parties such as investigating agencies, suspects and forensic labs. A major challenge in such settings is to carry out the matching process between the suspects&#x27; DNA samples and the samples obtained from the crime scene without compromising the privacy of the suspects&#x27; DNA profiles. Additionally, it is necessary that sensitive details pertaining to the investigation such as the identities of the suspects and evidence obtained from the crime scene must be kept private to the investigating agency. We present a novel DNA matching scheme, termed as PrivaMatch, which addresses multiple concerns about privacy of the suspects&#x27; DNA profiles and the crime scene evidence. In the proposed scheme, the investigating agencies oblivious transfer and zero-knowledge proofs to privately obtain the DNA profiles of the suspects from the forensic lab&#x27;s database.In addition, we present a clever data obfuscation technique using homomorphic encryption and modular arithmetic for the investigating agency to privately obtain the DNA profile of the crime scene&#x27;s sample, keeping the profile oblivious from the forensic lab. The DNA profile of the crime scene sample is operated on using a homomorphic cryptosystem such that neither of the parties (e.g., the investigation agency, forensic labs, DNA database owners) learns about the private data of the other parties. The proposed scheme is analysed formally and the practicality of its security strengths is verified using simulations under standard assumptions.

  匹配依据：MPC: oblivious transfer

  </details>

- **Founding Quantum Cryptography on Quantum Advantage, or, Towards Cryptography from $\\\#\\mathsf{P}$-Hardness**
  2024-09-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.15248) · [IACR ePrint](https://eprint.iacr.org/2024/1490)
  Dakshita Khurana, Kabir Tomer

  <details><summary>摘要 / Abstract</summary>

  Recent oracle separations [Kretschmer, TQC&#x27;21, Kretschmer et. al., STOC&#x27;23] have raised the tantalizing possibility of building quantum cryptography from sources of hardness that persist even if the polynomial hierarchy collapses. We realize this possibility by building quantum bit commitments and secure computation from unrelativized, well-studied mathematical problems that are conjectured to be hard for $\mathsf{P}^{\#\mathsf{P}}$ -- such as approximating the permanents of complex Gaussian matrices, or approximating the output probabilities of random quantum circuits. Indeed, we show that as long as \any one of the conjectures underlying sampling-based quantum advantage (e.g., BosonSampling, Random Circuit Sampling, IQP, etc.) is true, quantum cryptography can be based on the extremely mild assumption that $\mathsf{P}^{\#\mathsf{P}} \not\subseteq \mathsf{(io)BQP}/\mathsf{qpoly}$. Our techniques uncover strong connections between the hardness of approximating the probabilities of outcomes of quantum processes, the existence of ``one-way&#x27;&#x27; state synthesis problems, and the existence of useful cryptographic primitives such as one-way puzzles and quantum bit commitments. Specifically, we prove that the following hardness assumptions are equivalent under $\mathsf{BQP}$ reductions. 1. The hardness of approximating the probabilities of outcomes of certain efficiently sampleable distributions. That is, there exist quantumly efficiently sampleable distributions for which it is hard to approximate the probability assigned to a randomly chosen string in the support of the distribution (upto inverse polynomial multiplicative error). 2. The existence of one-way puzzles, where a quantum sampler outputs a pair of classical strings -- a puzzle and its key -- and where the hardness lies in finding the key corresponding to a random puzzle. These are known to imply quantum bit commitments [Khurana and Tomer, STOC&#x27;24]. 3. The existence of state puzzles, or one-way state synthesis, where it is hard to synthesize a secret quantum state given a public classical identifier. These capture the hardness of search problems with quantum inputs (secrets) and classical outputs (challenges). These are the first constructions of quantum cryptographic primitives (one-way puzzles, quantum bit commitments, state puzzles) from concrete, well-founded mathematical assumptions that do not imply the existence of classical cryptography. Along the way, we also show that distributions that admit efficient quantum samplers but cannot be pseudo-deterministically efficiently sampled imply quantum commitments.

  匹配依据：MPC: secure computation

  </details>

- **An Integrated Blockchain and IPFS Solution for Secure and Efficient Source Code Repository Hosting using Middleman Approach**
  2024-09-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.14530)
  Md. Rafid Haque, Sakibul Islam Munna, Sabbir Ahmed, Md. Tahmid Islam, Md Mehedi Hassan Onik, A. B. M. Ashikur Rahman

  <details><summary>摘要 / Abstract</summary>

  Centralized version control systems (VCS) are vital for software development but pose risks of data loss and ownership disputes. While blockchain offers a decentralized alternative, existing solutions are often hindered by high latency, compromising the real-time collaboration essential for modern workflows. This study introduces a novel hybrid architecture combining the security of the Ethereum blockchain and the InterPlanetary File System (IPFS) with two key contributions: 1) Shamir&#x27;s Secret Sharing (SSS) to create a trust-minimized model for key distribution, and 2) an authoritative-first, optimistic-fallback retrieval protocol utilizing a temporary middleware to decouple the user experience from blockchain confirmation delays. We implemented a full prototype and conducted a comprehensive performance evaluation on the public Sepolia testnet. Our results demonstrate that this architecture not only provides a secure, auditable, and resilient platform for source code hosting but also achieves highly competitive user-perceived performance. Our user-perceived push time reduces submission latency by up to 49% compared to a standard git push for common repository sizes, proving that a well-designed decentralized VCS can balance the core tenets of security and decentralization with the practical need for speed and efficiency.

  匹配依据：MPC: secret sharing

  </details>

- **Towards Lightweight and Privacy-preserving Data Provision in Digital Forensics for Driverless Taxi**
  2024-09-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.14039)
  Yanwei Gong, Xiaolin Chang, Jelena Mišić, Vojislav B. Mišić, Junchao Fan, Kaiwen Wang

  <details><summary>摘要 / Abstract</summary>

  Data provision, referring to the data upload and data access, is one key phase in vehicular digital forensics. The unique features of Driverless Taxi (DT) bring new issues to this phase: 1) efficient verification of data integrity when diverse Data Providers (DPs) upload data; 2) DP privacy preservation during data upload; and 3) privacy preservation of both data and INvestigator (IN) under complex data ownership when accessing data. To this end, we propose a novel Lightweight and Privacy-preserving Data Provision (LPDP) approach consisting of three mechanisms: 1) the Privacy-friendly Batch Verification Mechanism (PBVm) based on elliptic curve cryptography, 2) Data Access Control Mechanism (DACm) based on ciphertext-policy attribute-based encryption, and 3) Decentralized IN Warrant Issuance Mechanism (DIWIm) based on secret sharing. Privacy preservation of data provision is achieved through: 1) ensuring the DP privacy preservation in terms of the location privacy and unlinkability of data upload requests by PBVm, 2) ensuring data privacy preservation by DACm and DIWIm, and 3) ensuring the identity privacy of IN in terms of the anonymity and unlinkability of data access requests without sacrificing the traceability. Lightweight of data provision is achieved through: 1) ensuring scalable verification of data integrity by PBVm, and 2) ensuring low-overhead warrant update with respect to DIWIm. Security analysis and performance evaluation are conducted to validate the security and performance features of LPDP.

  匹配依据：MPC: secret sharing

  </details>

- **Perfect Gradient Inversion in Federated Learning: A New Paradigm from the Hidden Subset Sum Problem**
  2024-09-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.14260)
  Qiongxiu Li, Lixia Luo, Agnese Gini, Changlong Ji, Zhanhao Hu, Xiao Li, Chengfang Fang, Jie Shi, Xiaolin Hu

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) has emerged as a popular paradigm for collaborative learning among multiple parties. It is considered privacy-friendly because local data remains on personal devices, and only intermediate parameters -- such as gradients or model updates -- are shared. Although gradient inversion is widely viewed as a common attack method in FL, analytical research on reconstructing input training samples from shared gradients remains limited and is typically confined to constrained settings like small batch sizes. In this paper, we aim to overcome these limitations by addressing the problem from a cryptographic perspective. We mathematically formulate the input reconstruction problem using the gradient information shared in FL as the Hidden Subset Sum Problem (HSSP), an extension of the well-known NP-complete Subset Sum Problem (SSP). Leveraging this formulation allows us to achieve perfect input reconstruction, thereby mitigating issues such as dependence on label diversity and underperformance with large batch sizes that hinder existing empirical gradient inversion attacks. Moreover, our analysis provides insights into why empirical input reconstruction attacks degrade with larger batch sizes. By modeling the problem as HSSP, we demonstrate that the batch size \( B \) significantly affects attack complexity, with time complexity reaching \( \mathcal{O}(B^9) \). We further show that applying secure data aggregation techniques -- such as homomorphic encryption and secure multiparty computation -- provides a strong defense by increasing the time complexity to \( \mathcal{O}(N^9 B^9) \), where \( N \) is the number of local clients in FL. To the best of our knowledge, this is the first work to rigorously analyze privacy issues in FL by modeling them as HSSP, providing a concrete analytical foundation for further exploration and development of defense strategies.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Honest Majority GOD MPC with $O(\\mathsf{depth}(C))$ Rounds and Low Online Communication**
  2024-09-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1479)
  Amit Agarwal, Alexander Bienstock, Ivan Damgård, Daniel Escudero

  <details><summary>摘要 / Abstract</summary>

  In the context of secure multiparty computation (MPC) protocols with guaranteed output delivery (GOD) for the honest majority setting, the state-of-the-art in terms of communication is the work of (Goyal et al. CRYPTO&#x27;20), which communicates O(n|C|) field elements, where |C| is the size of the circuit being computed and n is the number of parties. Their round complexity, as usual in secret-sharing based MPC, is proportional to O(depth(C)), but only in the optimistic case where there is no cheating. Under attack, the number of rounds can increase to \Omega(n^2) before honest parties receive output, which is undesired for shallow circuits with depth(C) &lt;&lt; n^2. In contrast, other protocols that only require O(depth(C) rounds even in the worst case exist, but the state-of-the-art from (Choudhury and Patra, Transactions on Information Theory, 2017) still requires \Omega(n^4|C|) communication in the offline phase, and \Omega(n^3|C|) in the online (for both point-to-point and broadcast channels). We see there exists a tension between efficient communication and number of rounds. For reference, the recent work of (Abraham et al., EUROCRYPT&#x27;23) shows that for perfect security and t&lt;n/3, protocols with both linear communication and O(depth(C)) rounds exist. We address this state of affairs by presenting a novel honest majority GOD protocol that maintains O(depth(C)) rounds, even under attack, while improving over the communication of the most efficient protocol in this setting by Choudhury and Patra. More precisely, our protocol has point-to-point (P2P) online communication of O(n|C|), accompanied by O(n|C|) broadcasted (BC) elements, while the offline has O(n^3|C|) P2P communication with O(n^3|C|) BC. This improves over the previous best result, and reduces the tension between communication and round complexity. Our protocol is achieved via a careful use of packed secret-sharing in order to improve the communication of existing verifiable secret-sharing approaches, although at the expense of weakening their robust guarantees: reconstruction of shared values may fail, but only if the adversary gives away the identities of many corrupt parties. We show that this less powerful notion is still useful for MPC, and we use this as a core building block in our construction. Using this weaker VSS, we adapt the recent secure-with-abort Turbopack protocol (Escudero et al. CCS&#x27;22) to the GOD setting without significantly sacrificing in efficiency.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **CorBin-FL: A Differentially Private Federated Learning Mechanism using Common Randomness**
  2024-09-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.13133)
  Hojat Allah Salehi, Md Jueal Mia, S. Sandeep Pradhan, M. Hadi Amini, Farhad Shirani

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) has emerged as a promising framework for distributed machine learning. It enables collaborative learning among multiple clients, utilizing distributed data and computing resources. However, FL faces challenges in balancing privacy guarantees, communication efficiency, and overall model accuracy. In this work, we introduce CorBin-FL, a privacy mechanism that uses correlated binary stochastic quantization to achieve differential privacy while maintaining overall model accuracy. The approach uses secure multi-party computation techniques to enable clients to perform correlated quantization of their local model updates without compromising individual privacy. We provide theoretical analysis showing that CorBin-FL achieves parameter-level local differential privacy (PLDP), and that it asymptotically optimizes the privacy-utility trade-off between the mean square error utility measure and the PLDP privacy measure. We further propose AugCorBin-FL, an extension that, in addition to PLDP, achieves user-level and sample-level central differential privacy guarantees. For both mechanisms, we derive bounds on privacy parameters and mean squared error performance measures. Extensive experiments on MNIST and CIFAR10 datasets demonstrate that our mechanisms outperform existing differentially private FL mechanisms, including Gaussian and Laplacian mechanisms, in terms of model accuracy under equal PLDP privacy budgets.

  匹配依据：MPC: secure multi party computation

  </details>

- **Communication Efficient Secure and Private Multi-Party Deep Learning**
  2024-09-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1471)
  Sankha Das, Sayak Ray Chowdhury, Nishanth Chandran, Divya Gupta, Satya Lokam, Rahul Sharma

  <details><summary>摘要 / Abstract</summary>

  Distributed training that enables multiple parties to jointly train a model on their respective datasets is a promising approach to address the challenges of large volumes of diverse data for training modern machine learning models. However, this approach immedi- ately raises security and privacy concerns; both about each party wishing to protect its data from other parties during training and preventing leakage of private information from the model after training through various inference attacks. In this paper, we ad- dress both these concerns simultaneously by designing efficient Differentially Private, secure Multiparty Computation (DP-MPC) protocols for jointly training a model on data distributed among multiple parties. Our DP-MPC protocol in the two-party setting is 56-794× more communication-efficient and 16-182× faster than previous such protocols. Conceptually, our work simplifies and improves on previous attempts to combine techniques from secure multiparty computation and differential privacy, especially in the context of ML training.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Password-Protected Threshold Signatures**
  2024-09-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1469)
  Stefan Dziembowski, Stanislaw Jarecki, Paweł Kędzior, Hugo Krawczyk, Chan Nam Ngo, Jiayu Xu

  <details><summary>摘要 / Abstract</summary>

  We witness an increase in applications like cryptocurrency wallets, which involve users issuing signatures using private keys. To protect these keys from loss or compromise, users commonly outsource them to a custodial server. This creates a new point of failure, because compromise of such a server leaks the user’s key, and if user authentication is implemented with a password then this password becomes open to an offline dictionary attack (ODA). A better solution is to secret-share the key among a set of servers, possibly including user’s own device(s), and implement password authentication and signature computation using threshold cryptography. We propose a notion of augmented password protected threshold signature scheme (aptSIG) which captures the best possible security level for this setting. Using standard threshold cryptography techniques, i.e. threshold password authentication and threshold signatures, one can guarantee that compromising up to t out of n servers reveals no information on either the key or the password. However, we extend this with a novel property, namely that compromising even all n servers also does not leak any information, except via an unavoidable ODA attack, which reveals the key (and the password) only if the attacker guesses the password. We define aptSIG in the Universally Composable (UC) framework and show that it can be constructed very efficiently, using a black-box composition of any UC threshold signature and a UC augmented Password-Protected Secret Sharing (aPPSS), which we define as an extension of prior notion of PPSS. As concrete instantiations we obtain secure aptSIG schemes for ECDSA and BLS signatures with very small overhead over the respective threshold signature. Finally, we note that both the notion and our generic solution for augmented password-protected threshold signatures can be generalized to password-protecting MPC for any keyed functions.

  匹配依据：MPC: secret sharing

  </details>

- **Dishonest Majority Constant-Round MPC with Linear Communication from DDH**
  2024-09-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1466)
  Vipul Goyal, Junru Li, Ankit Kumar Misra, Rafail Ostrovsky, Yifan Song, Chenkai Weng

  <details><summary>摘要 / Abstract</summary>

  In this work, we study constant round multiparty computation (MPC) for Boolean circuits against a fully malicious adversary who may control up to $n-1$ out of $n$ parties. Without relying on fully homomorphic encryption (FHE), the best-known results in this setting are achieved by Wang et al. (CCS 2017) and Hazay et al. (ASIACRYPT 2017) based on garbled circuits, which require a quadratic communication in the number of parties $O(|C|\cdot n^2)$. In contrast, for non-constant round MPC, the recent result by Rachuri and Scholl (CRYPTO 2022) has achieved linear communication $O(|C|\cdot n)$. In this work, we present the first concretely efficient constant round MPC protocol in this setting with linear communication in the number of parties $O(|C|\cdot n)$. Our construction can be based on any public-key encryption scheme that is linearly homomorphic for public keys. Our work gives a concrete instantiation from a variant of the El-Gamal Encryption Scheme assuming the DDH assumption. The analysis shows that when the computational security parameter $\lambda=128$ and statistical security parameter $\kappa=80$, our protocol achieves a smaller communication than Wang et al. (CCS 2017) when there are $16$ parties for AES circuit and $8$ parties for general Boolean circuits (where we assume that the numbers of AND gates and XOR gates are the same). When comparing with the recent work by Beck et al. (CCS 2023) that achieves constant communication complexity $O(|C|)$ in the strong honest majority setting ($t&lt;(1/2-\epsilon)n$ where $\epsilon$ is a constant), our protocol is better as long as $n&lt;3500$ (when $t=n/4$ for their work).

  匹配依据：MPC: garbled circuits, multiparty computation

  </details>

- **Asynchronous Distributed Key Generation with Flexible Threshold and Batched Key Derivation**
  2024-09-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1463)
  Junming Li, Renfei Shen, Zhi Lu, Songfeng Lu, Xueming Tang, Yuanqing Feng

  <details><summary>摘要 / Abstract</summary>

  Distributed Key Generation (DKG) is a vital security foundation for decentralized technologies like blockchain and threshold signatures. However, existing asynchronous DKG (ADKG) protocols face bottlenecks in rigid configuration, limited throughput, and poor scalability, failing to meet the dynamic security management demands of large-scale services.In this paper, we propose an efficient suite of ADKG protocols that support flexible threshold configurations. First, we design a Flexible-Threshold Asynchronous Complete Secret Sharing (FT-ACSS) protocol using bivariate polynomials and zero-knowledge proofs. In an $n \ge 3f+1$ network, FT-ACSS enables dealers to freely configure the threshold $t \in [f, n-f)$, surpassing the limitations of traditional fixed $f$ or $2f$ thresholds. Furthermore, FT-ACSS implements a batch processing mechanism to share up to $t$ secrets simultaneously with $O(\lambda n^2)$ communication cost. We additionally extend the Schnorr protocol into $m$-Schnorr to support multi-secret commitments, significantly reducing amortized resource overhead.Combined with RBC and ABA, these components form a complete FT-ADKG protocol. Theoretical and experimental evaluations demonstrate that our scheme offers superior flexibility and efficiency compared to state-of-the-art protocols, providing a practical security management solution for large-scale asynchronous distributed systems.

  匹配依据：MPC: secret sharing

  </details>

- **Threshold PAKE with Security against Compromise of all Servers**
  2024-09-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1455)
  Yanqi Gu, Stanislaw Jarecki, Pawel Kedzior, Phillip Nazarian, Jiayu Xu

  <details><summary>摘要 / Abstract</summary>

  We revisit the notion of threshold Password-Authenticated Key Exchange (tPAKE), and we extend it to augmented tPAKE (atPAKE), which protects password information even in the case all servers are compromised, except for allowing an (inevitable) offline dictionary attack. Compared to prior notions of tPAKE this is analogous to replacing symmetric PAKE, where the server stores the user&#x27;s password, with an augmented (or asymmetric) PAKE, like OPAQUE [JKX18], where the server stores a password hash, which can be used only as a target in an offline dictionary search for the password. An atPAKE scheme also strictly improves on the security of an aPAKE, by secret-sharing the password hash among a set of servers. Indeed, our atPAKE protocol is a natural realization of threshold OPAQUE. We formalize atPAKE in the framework of Universal Composability (UC), and show practical ways to realize it. All our schemes are generic compositions which interface to any aPAKE used as a sub-protocol, making them easier to adopt. Our main scheme relies on threshold Oblivious Pseudorandom Function (tOPRF), and our independent contribution fixes a flaw in the UC tOPRF notion of [JKKX17] and upgrades the tOPRF scheme therein to achieve the fixed definition while preserving its minimal cost and round complexity. The technique we use enforces implicit agreement on arbitrary context information within threshold computation, and it is of general interest.

  匹配依据：MPC: secret sharing

  </details>

- **Provable Privacy Guarantee for Individual Identities and Locations in Large-Scale Contact Tracing**
  2024-09-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.12341)
  Tyler Nicewarner, Wei Jiang, Aniruddha Gokhale, Dan Lin

  <details><summary>摘要 / Abstract</summary>

  The task of infectious disease contact tracing is crucial yet challenging, especially when meeting strict privacy requirements. Previous attempts in this area have had limitations in terms of applicable scenarios and efficiency. Our paper proposes a highly scalable, practical contact tracing system called PREVENT that can work with a variety of location collection methods to gain a comprehensive overview of a person&#x27;s trajectory while ensuring the privacy of individuals being tracked, without revealing their plain text locations to any party, including servers. Our system is very efficient and can provide real-time query services for large-scale datasets with millions of locations. This is made possible by a newly designed secret-sharing based architecture that is tightly integrated into unique private space partitioning trees. Notably, our experimental results on both real and synthetic datasets demonstrate that our system introduces negligible performance overhead compared to traditional contact tracing methods. PREVENT could be a game-changer in the fight against infectious diseases and set a new standard for privacy-preserving location tracking.

  匹配依据：MPC: secret sharing

  </details>

- **Optimal Offline ORAM with Perfect Security via Simple Oblivious Priority Queues**
  2024-09-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.12021)
  Thore Thießen, Jan Vahrenhold

  <details><summary>摘要 / Abstract</summary>

  Oblivious RAM (ORAM) is a well-researched primitive to hide the memory access pattern of a RAM computation; it has a variety of applications in trusted computing, outsourced storage, and multiparty computation. In this paper, we study the so-called offline ORAM in which the sequence of memory access locations to be hidden is known in advance. Apart from their theoretical significance, offline ORAMs can be used to construct efficient oblivious algorithms. We obtain the first optimal offline ORAM with perfect security from oblivious priority queues via time-forward processing. For this, we present a simple construction of an oblivious priority queue with perfect security. Our construction achieves an asymptotically optimal (amortized) runtime of $Θ(\log N)$ per operation for a capacity of $N$ elements and is of independent interest. Building on our construction, we additionally present efficient external-memory instantiations of our oblivious, perfectly-secure construction: For the cache-aware setting, we match the optimal I/O complexity of $Θ(\frac{1}{B} \log \frac{N}{M})$ per operation (amortized), and for the cache-oblivious setting we achieve a near-optimal I/O complexity of $O(\frac{1}{B} \log \frac{N}{M} \log\log_M N)$ per operation (amortized).

  匹配依据：MPC: multiparty computation

  </details>

- **Towards Quantum Multiparty Session Types**
  2024-09-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.11133)
  Ivan Lanese, Ugo Dal Lago, Vikraman Choudhury

  <details><summary>摘要 / Abstract</summary>

  Multiparty Session Types (MPSTs) offer a structured way of specifying communication protocols and guarantee relevant communication properties, such as deadlock-freedom. In this paper, we extend a minimal MPST system with quantum data and operations, enabling the specification of quantum protocols. Quantum MPSTs (QMPSTs) provide a formal notation to describe quantum protocols, both at the abstract level of global types, describing which communications can take place in the system and their dependencies, and at the concrete level of local types and quantum processes, describing the expected behavior of each participant in the protocol. Type-checking relates these two levels formally, ensuring that processes behave as prescribed by the global type. Beyond usual communication properties, QMPSTs also allow us to prove that qubits are owned by a single process at any time, capturing the quantum no-cloning and no-deleting theorems. We use our approach to verify four quantum protocols from the literature, respectively Teleportation, Secret Sharing, Bit-Commitment, and Key Distribution.

  匹配依据：MPC: secret sharing

  </details>

- **Randomness in Private Sequential Stateless Protocols**
  2024-09-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1448)
  Hari Krishnan P. Anilkumar, Varun Narayanan, Manoj Prabhakaran, Vinod M. Prabhakaran

  <details><summary>摘要 / Abstract</summary>

  A significant body of work in information-theoretic cryptography has been devoted to the fundamental problem of understanding the power of randomness in private computation. This has included both in-depth study of the randomness complexity of specific functions (e.g., Couteau and Ros ́en, ASIACRYPT 2022, gives an upper bound of 6 for n-party $\mathsf{AND}$), and results for broad classes of functions (e.g., Kushilevitz et al. STOC 1996, gives an $O(1)$ upper bound for all functions with linear-sized circuits). In this work, we make further progress on both fronts by studying randomness complexity in a new simple model of secure computation called Private Sequential Stateless (PSS) model. We show that functions with $O(1)$ randomness complexity in the PSS model are exactly those with constant-width branching programs, restricting to “speak-constant-times” protocols and to “read-constant-times” branching programs. Towards this our main construction is a novel PSS protocol for “strongly regular branching programs” (SRBP). As we show, any constant-width branching program can be converted to a constant-width SRBP, yielding one side of our characterization. The converse direction uses ideas from Kushilevitz et al. to translate randomness to communication. Our protocols are concretely efficient, has a simple structure, covers the broad class of functions with small-width, read-once (or read-a-few-times) branching programs, and hence may be of practical interest when 1-privacy is considered adequate. Also, as a consequence of our general result for SRBPs, we obtain an improvement over the protocol of Couteau and Ros ́en for $\mathsf{AND}$ in certain cases — not in terms of the number of bits of randomness, but in terms of a simpler protocol structure (sequential, stateless).

  匹配依据：MPC: secure computation

  </details>

- **Benchmarking Secure Sampling Protocols for Differential Privacy**
  2024-09-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.10667)
  Yucheng Fu, Tianhao Wang

  <details><summary>摘要 / Abstract</summary>

  Differential privacy (DP) is widely employed to provide privacy protection for individuals by limiting information leakage from the aggregated data. Two well-known models of DP are the central model and the local model. The former requires a trustworthy server for data aggregation, while the latter requires individuals to add noise, significantly decreasing the utility of aggregated results. Recently, many studies have proposed to achieve DP with Secure Multi-party Computation (MPC) in distributed settings, namely, the distributed model, which has utility comparable to central model while, under specific security assumptions, preventing parties from obtaining others&#x27; information. One challenge of realizing DP in distributed model is efficiently sampling noise with MPC. Although many secure sampling methods have been proposed, they have different security assumptions and isolated theoretical analyses. There is a lack of experimental evaluations to measure and compare their performances. We fill this gap by benchmarking existing sampling protocols in MPC and performing comprehensive measurements of their efficiency. First, we present a taxonomy of the underlying techniques of these sampling protocols. Second, we extend widely used distributed noise generation protocols to be resilient against Byzantine attackers. Third, we implement discrete sampling protocols and align their security settings for a fair comparison. We then conduct an extensive evaluation to study their efficiency and utility.

  匹配依据：MPC: secure multi party computation

  </details>

- **Another Walk for Monchi**
  2024-09-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1445)
  Riccardo Taiello, Emre Tosun, Alberto Ibarrondo, Hervé Chabanne, Melek Önen

  <details><summary>摘要 / Abstract</summary>

  Monchi is a new protocol aimed at privacy-preserving biometric identification. It begins with scores computation in the encrypted domain thanks to homomorphic encryption and ends with comparisons of these scores to a given threshold with function secret sharing. We here study the integration in that context of scores computation techniques recently introduced by Bassit et al. that eliminate homomorphic multiplications by replacing them by lookup tables. First, we extend this lookup tables biometric recognition solution by adding the use of function secret sharing for the final comparison of scores. Then, we introduce a two-party computation of the scores with lookup tables which fits nicely together with the function secret sharing scores comparison. Our solutions accommodate well with the flight boarding use case introduced by Monchi.

  匹配依据：MPC: secret sharing, two party computation

  </details>

- **Trojan Insertion versus Layout Defenses for Modern ICs: Red-versus-Blue Teaming in a Competitive Community Effort**
  2024-09-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1440)
  Johann Knechtel, Mohammad Eslami, Peng Zou, Min Wei, Xingyu Tong, Binggang Qiu, Zhijie Cai, Guohao Chen, Benchao Zhu, Jiawei Li, Jun Yu, Jianli Chen, Chun-Wei Chiu, Min-Feng Hsieh, Chia-Hsiu Ou, Ting-Chi Wang, Bangqi Fu, Qijing Wang, Yang Sun, Qin Luo, Anthony W. H. Lau, Fangzhou Wang, Evangeline F. Y. Young, Shunyang Bi, Guangxin Guo, Haonan Wu, Zhengguang Tang, Hailong You, Cong Li, Ramesh Karri, Ozgur Sinanoglu, Samuel Pagliarini

  <details><summary>摘要 / Abstract</summary>

  Hardware Trojans (HTs) are a longstanding threat to secure computation. Among different threat models, it is the fabrication-time insertion of additional malicious logic directly into the layout of integrated circuits (ICs) that constitutes the most versatile, yet challenging scenario, for both attackers and defenders. Here, we present a large-scale, first-of-its-kind community effort through red-versus-blue teaming that thoroughly explores this threat. Four independently competing blue teams of 23 IC designers in total had to analyze and fix vulnerabilities of representative IC layouts, whereas a red team of 3 experts in hardware security and IC design continuously pushed the boundaries of these defense efforts through different HTs and novel insertion techniques. Importantly, we find that, despite the blue teams’ commendable efforts, even highly-optimized layouts retained at least some exploitable vulnerabilities. Our effort follows a real-world setting for a modern 7nm technology node and industry-grade tooling for IC design, all embedded into a fully-automated and extensible benchmarking framework. To ensure the relevance of this work, strict rules that adhere to real-world requirements for IC design and manufacturing were postulated by the organizers. For example, not a single violation for timing and design-rule checks were allowed for defense techniques. Besides, in an advancement over prior art, neither red nor blue teams were allowed to use any so-called fillers and spares for trivial attack or defense approaches. Finally, we release all methods and artifacts: the representative IC layouts and HTs, the devised attack and defense techniques, the evaluation metrics and setup, the technology setup and commercial-grade reference flow for IC design, the encompassing benchmarking framework, and all best results. This full release enables the community to continue exploring this important challenge for hardware security, in particular to focus on the urgent need for further advancements in defense strategies.

  匹配依据：MPC: secure computation

  </details>

- **Nebula: Efficient, Private and Accurate Histogram Estimation**
  2024-09-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.09676)
  Ali Shahin Shamsabadi, Peter Snyder, Ralph Giles, Aurélien Bellet, Hamed Haddadi

  <details><summary>摘要 / Abstract</summary>

  We present \textit{Nebula}, a system for differentially private histogram estimation on data distributed among clients. \textit{Nebula} allows clients to independently decide whether to participate in the system, and locally encode their data so that an untrusted server only learns data values whose multiplicity exceeds a predefined aggregation threshold, with $(\varepsilon,δ)$ differential privacy guarantees. Compared to existing systems, \textit{Nebula} uniquely achieves: \textit{i)} a strict upper bound on client privacy leakage; \textit{ii)} significantly higher utility than standard local differential privacy systems; and \textit{iii)} no requirement for trusted third-parties, multi-party computation, or trusted hardware. We provide a formal evaluation of \textit{Nebula}&#x27;s privacy, utility and efficiency guarantees, along with an empirical assessment on three real-world datasets. On the United States Census dataset, clients can submit their data in just 0.0036 seconds and 0.0016 MB (\textbf{efficient}), under strong $(\varepsilon=1,δ=10^{-8})$ differential privacy guarantees (\textbf{private}), enabling \textit{Nebula}&#x27;s untrusted aggregation server to estimate histograms with over 88\% better utility than existing local differential privacy deployments (\textbf{accurate}). Additionally, we describe a variant that allows clients to submit multi-dimensional data, with similar privacy, utility, and performance. Finally, we provide an implementation of \textit{Nebula}.

  匹配依据：MPC: multi party computation

  </details>

- **Actively Secure Polynomial Evaluation from Shared Polynomial Encodings**
  2024-09-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1435)
  Pascal Reisert, Marc Rivinius, Toomas Krips, Sebastian Hasler, Ralf Küsters

  <details><summary>摘要 / Abstract</summary>

  Many of the currently best actively secure Multi-Party Computation (MPC) protocols like SPDZ (Damgård et al., CRYPTO 2012) and improvements thereof use correlated randomness to speed up the time-critical online phase. Although many of these protocols still rely on classical Beaver triples, recent results show that more complex correlations like matrix or convolution triples lead to more efficient evaluations of the corresponding operations, i.e. matrix multiplications or tensor convolutions. In this paper, we address the evaluation of multivariate polynomials with a new form of randomness: polytuples. We use the polytuples to construct a new family of randomized encodings which then allow us to evaluate the given multivariate polynomial. Our approach can be fine-tuned in various ways to the constraints of applications at hand, in terms of round complexity, bandwidth, and tuple size. We show that for many real-world setups, a polytuples-based online phase outperforms state-of-the-art protocols based on Beaver triples.

  匹配依据：MPC: secure multi party computation

  </details>

- **$Shortcut$: Making MPC-based Collaborative Analytics Efficient on Dynamic Databases**
  2024-09-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1433)
  Peizhao Zhou, Xiaojie Guo, Pinzhi Chen, Tong Li, Siyi Lv, Zheli Liu

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-party Computation (MPC) provides a promising solution for privacy-preserving multi-source data analytics. However, existing MPC-based collaborative analytics systems (MCASs) have unsatisfying performance for scenarios with dynamic databases. Naively running an MCAS on a dynamic database would lead to significant redundant costs and raise performance concerns, due to the substantial duplicate contents between the pre-updating and post-updating databases. In this paper, we propose $Shortcut$, a framework that can work with MCASs to enable efficient queries on dynamic databases that support data insertion, deletion, and update. The core idea of $Shortcut$ is to materialize previous query results and directly update them via our query result update (QRU) protocol to obtain current query results. We customize several efficient QRU protocols for common SQL operators, including Order-by-Limit, Group-by-Aggregate, Distinct, Join, Select, and Global Aggregate. These protocols are composable to implement a wide range of query functions. In particular, we propose two constant-round protocols to support data insertion and deletion. These protocols can serve as important building blocks of other protocols and are of independent interest. They address the problem of securely inserting/deleting a row into/from an ordered table while keeping the order. Our experiments show that $Shortcut$ outperforms naive MCASs for minor updates arriving in time, which captures the need of many realistic applications (e.g., insurance services, account data management). For example, for a single query after an insertion, $Shortcut$ achieves up to $186.8 \times$ improvement over those naive MCASs without our QRU protocols on a dynamic database with $2^{16} \sim 2^{20}$ rows, which is common in real-life applications.

  匹配依据：MPC: secure multi party computation

  </details>

- **MYao: Multiparty \`\`Yao'' Garbled Circuits with Row Reduction, Half Gates, and Efficient Online Computation**
  2024-09-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1430)
  Aner Ben-Efraim, Lior Breitman, Jonathan Bronshtein, Olga Nissenbaum, Eran Omri

  <details><summary>摘要 / Abstract</summary>

  Garbled circuits are a powerful and important cryptographic primitive, introduced by Yao [FOCS 1986] for secure two-party computation. Beaver, Micali and Rogaway (BMR) [STOCS 1990] extended the garbled circuit technique to construct the first constant-round secure multiparty computation (MPC) protocol. In the BMR protocol, the garbled circuit size grows linearly and the online computation time grows quadratically with the number of parties. Previous solutions to avoid this relied on key-homomorphic PRFs, incurring a large garbled circuit size and slow online computation time. We present MYao, a new multiparty protocol for achieving a ``Yao&#x27;&#x27; garbled circuit, i.e., the garbled circuit size and online computation time are independent of the number of parties. The key innovation is that the parties collaboratively compute the PRF in MPC, which was previously believed to be inefficient. In this paper, we challenge this long-standing assumption by basing the garbled circuit construction on ``MPC-friendly&#x27;&#x27; PRFs. One of the highlights of our new technique is that we are able to achieve, for the first time, full row-reduction in multiparty garbled circuits. To achieve this optimization without increasing the number of rounds, we utilize free-XOR and half gates, presenting a new technique for choosing the keys, based on a naturally occurring relation between the 2 keys of the 2 half-gates. MYao reduces the garbled circuit size by more than 90%, the total communication by more than 75%, and the online computation time by more than 10%, compared to all known solutions based on key-homomorphic PRFs, thus substantially improving the overall efficiency in both the offline and the online phases. Furthermore, MYao significantly improves over semi-honest BMR in online phase efficiency when the number of parties exceeds 80.

  匹配依据：MPC: garbled circuit, garbled circuits, secure multiparty computation, secure two party computation

  </details>

- **Collaboration Encouraging Quantum Secret Sharing Scheme with Seal Property**
  2024-09-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.07863)
  Xiaogang Cheng, Ren Guo

  <details><summary>摘要 / Abstract</summary>

  A new concept of quantum secret sharing is introduced, in which collaboration among participants are encourage. And the dealer can ask the participants to send back their share and revoke the secret before a predefined date or event, i.e. so-called seal property. We also give two concrete constructions of CE-QSS-Seal (Collaboration-Encouraging Quantum Secret Sharing with Seal property) scheme. The first one is unconditional secure and achieve the optimal bound of a seal scheme. The second one improve the optimal bound of seal by introducing post-quantum secure computational assumption.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Breadth-First-Search and Maximal-Flow**
  2024-09-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1420)
  Vincent Ehrmanntraut, Ulrike Meyer

  <details><summary>摘要 / Abstract</summary>

  We present novel Secure Multi-Party Computation (SMPC) protocols to perform Breadth-First-Searches (BFSs) and determine maximal flows on dense secret-shared graphs. In particular, we introduce a novel BFS protocol that requires only $\mathcal{O}(\log n)$ communication rounds on graphs with $n$ nodes, which is a big step from prior work that requires $\mathcal{O}(n \log n)$ rounds. This BFS protocol is then used in a maximal flow protocol based on the Edmonds-Karp algorithm, which requires $\mathcal{O}(n^3 \log n)$ rounds. We further optimize the protocol for cases where an upper bound $U$ on the capacities is publicly known by using a capacity scaling approach. This yields a new protocol which requires $\mathcal{O}(n^2 \log n \log U)$ rounds. Finally, we introduce a novel max flow protocol based on algorithms by Dinic and Tarjan with round complexity $\mathcal{O}(n^3)$. All protocols presented in this paper use SMPC primitives as a black-box, allowing our protocols to be used as building blocks in a wide range of settings and applications. We evaluate our protocols with semi-honest and malicious security in different network settings. Our logarithmic BFS protocol is up to 69 times faster than prior protocols on small graphs with less than 100 nodes, but is outperformed by protocols with lower computational complexity on graphs with thousands of nodes. Further, we find our Dinic-Tarjan protocol to be faster than the Edmonds-Karp and capacity scaling protocols in our evaluation, albeit trends indicating capacity scaling protocols to be faster on graph sizes not reached in our evaluation.

  匹配依据：MPC: secure multi party computation

  </details>

- **On the Relationship between Public Key Primitives via Indifferentiability**
  2024-09-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1419)
  Shuang Hu, Bingsheng Zhang, Cong Zhang, Kui Ren

  <details><summary>摘要 / Abstract</summary>

  Recently, Masny and Rindal [MR19] formalized a notion called Endemic Oblivious Transfer (EOT), and they proposed a generic transformation from Non-Interactive Key Exchange (NIKE) to EOT with standalone security in the random oracle (RO) model. However, from the model level, the relationship between idealized NIKE and idealized EOT and the relationship between idealized elementary public key primitives have been rarely researched. In this work, we investigate the relationship between ideal NIKE and ideal one-round EOT, as well as the relationship between ideal public key encryption (PKE) and ideal two-round Oblivious Transfer (OT), in the indifferentiability framework proposed by Maurer et al.(MRH04). Our results are threefold: Firstly, we model ideal PKE without public key validity test, ideal one-round EOT and ideal two-round OT in the indifferentiability framework. Secondly, we show that ideal NIKE and ideal one-round EOT are equivalent, and ideal PKE without public key validity test are equivalent to ideal two-round OT. Thirdly, we show a separation between ideal two-round OT and ideal one-round EOT, which implies a separation between ideal PKE and ideal NIKE.

  匹配依据：MPC: oblivious transfer

  </details>

- **Is merging worth it? Securely evaluating the information gain for causal dataset acquisition**
  2024-09-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.07215) · [Code](https://github.com/LucileTerminassian/causal_prospective_merge)
  Jake Fawkes, Lucile Ter-Minassian, Desi Ivanova, Uri Shalit, Chris Holmes

  <details><summary>摘要 / Abstract</summary>

  Merging datasets across institutions is a lengthy and costly procedure, especially when it involves private information. Data hosts may therefore want to prospectively gauge which datasets are most beneficial to merge with, without revealing sensitive information. For causal estimation this is particularly challenging as the value of a merge depends not only on reduction in epistemic uncertainty but also on improvement in overlap. To address this challenge, we introduce the first cryptographically secure information-theoretic approach for quantifying the value of a merge in the context of heterogeneous treatment effect estimation. We do this by evaluating the Expected Information Gain (EIG) using multi-party computation to ensure that no raw data is revealed. We further demonstrate that our approach can be combined with differential privacy (DP) to meet arbitrary privacy requirements whilst preserving more accurate computation compared to DP alone. To the best of our knowledge, this work presents the first privacy-preserving method for dataset acquisition tailored to causal estimation. We demonstrate the effectiveness and reliability of our method on a range of simulated and realistic benchmarks. Code is publicly available: https://github.com/LucileTerminassian/causal_prospective_merge.

  匹配依据：MPC: multi party computation

  </details>

- **Oraqle: A Depth-Aware Secure Computation Compiler**
  2024-09-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1409)
  Jelle Vos, Mauro Conti, Zekeriya Erkin

  <details><summary>摘要 / Abstract</summary>

  In the past decade, tens of homomorphic encryption compilers have been released, and there are good reasons for these compilers to exist. Firstly, homomorphic encryption is a powerful secure computation technique in that it is relatively easy for parties to switch from plaintext computation to secure computations when compared to techniques like secret sharing. However, the technique is mathematically involved and requires expert knowledge to express computations as homomorphic encryption operations. So, these compilers support users who might otherwise not have the time or expertise to optimize the computation manually. Another reason is that homomorphic encryption is still computationally expensive, so compilers allow users to optimize their secure computation tasks. One major shortcoming of these compilers is that they often do not allow users to use high-level primitives, such as equality checks, comparisons, and AND and OR operations between many operands. The compilers that do are either based on TFHE, requiring large bootstrapping keys that must be sent to the evaluator, or they only work in the Boolean domain, excluding many potentially more performant circuits. Moreover, compilers must reduce the multiplicative depth of the circuits they generate to minimize the noise growth inherent to these homomorphic encryption schemes. However, many compilers only consider reducing the depth as an afterthought. We propose the Oraqle compiler, which solves both problems at once by implementing depth-aware arithmetization, a technique for expressing high-level primitives as arithmetic operations that are executable by homomorphic encryption libraries. Instead of generating one possible circuit, the compiler generates multiple circuits that trade off the number of multiplications with the multiplicative depth. If the depth of the resulting circuits is low enough, they may be evaluated using a BFV or BGV library that does not require bootstrapping keys. We demonstrate that our compiler allows for significant performance gains.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Conditional Encryption with Applications to Secure Personalized Password Typo Correction**
  2024-09-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.06128)
  Mohammad Hassan Ameri, Jeremiah Blocki

  <details><summary>摘要 / Abstract</summary>

  We introduce the notion of a conditional encryption scheme as an extension of public key encryption. In addition to the standard public key algorithms ($\mathsf{KG}$, $\mathsf{Enc}$, $\mathsf{Dec}$) for key generation, encryption and decryption, a conditional encryption scheme for a binary predicate $P$ adds a new conditional encryption algorithm $\mathsf{CEnc}$. The conditional encryption algorithm $c=\mathsf{CEnc}_{pk}(c_1,m_2,m_3)$ takes as input the public encryption key $pk$, a ciphertext $c_1 = \mathsf{Enc}_{pk}(m_1)$ for an unknown message $m_1$, a control message $m_2$ and a payload message $m_3$ and outputs a conditional ciphertext $c$. Intuitively, if $P(m_1,m_2)=1$ then the conditional ciphertext $c$ should decrypt to the payload message $m_3$. On the other hand if $P(m_1,m_2) = 0$ then the ciphertext should not leak any information about the control message $m_2$ or the payload message $m_3$ even if the attacker already has the secret decryption key $sk$. We formalize the notion of conditional encryption secrecy and provide concretely efficient constructions for a set of predicates relevant to password typo correction. Our practical constructions utilize the Paillier partially homomorphic encryption scheme as well as Shamir Secret Sharing. We prove that our constructions are secure and demonstrate how to use conditional encryption to improve the security of personalized password typo correction systems such as TypTop. We implement a C++ library for our practically efficient conditional encryption schemes and evaluate the performance empirically. We also update the implementation of TypTop to utilize conditional encryption for enhanced security guarantees and evaluate the performance of the updated implementation.

  匹配依据：MPC: secret sharing

  </details>

- **Code-Based Zero-Knowledge from VOLE-in-the-Head and Their Applications: Simpler, Faster, and Smaller**
  2024-09-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1414)
  Ying Ouyang, Deng Tang, Yanhong Xu

  <details><summary>摘要 / Abstract</summary>

  Zero-Knowledge (ZK) protocols allow a prover to demonstrate the truth of a statement without disclosing additional information about the underlying witness. Code-based cryptography has a long history but did suffer from periods of slow development. Recently, a prominent line of research have been contributing to designing efficient code-based ZK from MPC-in-the-head (Ishai et al., STOC 2007) and VOLE-in-the head (VOLEitH) (Baum et al., Crypto 2023) paradigms, resulting in quite efficient standard signatures. However, none of them could be directly used to construct privacy-preserving cryptographic primitives. Therefore, Stern&#x27;s protocols remain to be the major technical stepping stones for developing advanced code-based privacy-preserving systems. This work proposes new code-based ZK protocols from VOLEitH paradigm for various relations and designs several code-based privacy-preserving systems that considerably advance the state-of-the-art in code-based cryptography. Our first contribution is a new ZK protocol for proving the correctness of a regular (non-linear) encoding process, which is utilized in many advanced privacy-preserving systems. Our second contribution are new ZK protocols for concrete code-based relations. In particular, we provide a ZK of accumulated values with optimal witness size for the accumulator (Nguyen et al., Asiacrypt 2019). Our protocols thus open the door for constructing more efficient privacy-preserving systems. Moreover, our ZK protocols have the advantage of being simpler, faster, and smaller compared to Stern-like protocols. To illustrate the effectiveness of our new ZK protocols, we develop ring signature (RS) scheme, group signature (GS) scheme, fully dynamic attribute-based signature scheme from our new ZK. The signature sizes of the resulting schemes are two to three orders of magnitude smaller than those based on Stern-like protocols in various parameter settings. Finally, our first ZK protocol yields a standard signature scheme, achieving ``signature size + public key size&#x27;&#x27; as small as $3.05$ KB, which is slightly smaller than the state-of-the-art signature scheme (Cui et al., PKC 2024) based on the regular syndrome decoding problems.

  匹配依据：MPC: mpc (context)

  </details>

- **Encrypted MultiChannel Communication (EMC2): Johnny Should Use Secret Sharing**
  2024-09-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1407)
  Gowri R. Chandran, Kilian Demuth, Kasra Edalatnejad, Sebastian Linsner, Christian Reuter, Thomas Schneider

  <details><summary>摘要 / Abstract</summary>

  Nowadays, the problem of point-to-point encryption is solved by the wide adaptation of protocols like TLS. However, challenges persist for End-to-End Encryption (E2EE). Current E2EE solutions, such as PGP and secure messengers like Signal, suffer from issues like 1) low usability, 2) small user base, 3) dependence on central service providers, and 4) susceptibility to backdoors. Concerns over legally mandated backdoors are rising as the US and EU are proposing new surveillance regulations requiring chat monitoring. We present a new E2EE solution called Encrypted MultiChannel Communication, based on n-out-of-n secret sharing. EMC2 splits messages into multiple secret shares and sends them through independent channels. We show that multiple independent channels exist between users and EMC2 provides E2EE with no single point of trust, no setup, and is understandable by the general public. Our solution complements existing tools and aims to strengthen the argument against legally enforced backdoors by demonstrating their ineffectiveness.

  匹配依据：MPC: secret sharing

  </details>

- **CipherDM: Secure Three-Party Inference for Diffusion Model Sampling**
  2024-09-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.05414)
  Xin Zhao, Xiaojun Chen, Xudong Chen, He Li, Tingyu Fan, Zhendong Zhao

  <details><summary>摘要 / Abstract</summary>

  Diffusion Models (DMs) achieve state-of-the-art synthesis results in image generation and have been applied to various fields. However, DMs sometimes seriously violate user privacy during usage, making the protection of privacy an urgent issue. Using traditional privacy computing schemes like Secure Multi-Party Computation (MPC) directly in DMs faces significant computation and communication challenges. To address these issues, we propose CipherDM, the first novel, versatile and universal framework applying MPC technology to DMs for secure sampling, which can be widely implemented on multiple DM based tasks. We thoroughly analyze sampling latency breakdown, find time-consuming parts and design corresponding secure MPC protocols for computing nonlinear activations including SoftMax, SiLU and Mish. CipherDM is evaluated on popular architectures (DDPM, DDIM) using MNIST dataset and on SD deployed by diffusers. Compared to direct implementation on SPU, our approach improves running time by approximately 1.084\times \sim 2.328\times, and reduces communication costs by approximately 1.212\times \sim 1.791\times.

  匹配依据：MPC: secure multi party computation

  </details>

- **A Novel Efficient Multiparty Semi-Quantum Secret Sharing Protocol Using Entangled States for Sharing Specific Bits**
  2024-09-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.05154)
  Mustapha Anis Younes, Sofia Zebboudj, Abdelhakim Gharbi

  <details><summary>摘要 / Abstract</summary>

  Recently, Younes et al. proposed an efficient multi-party semi-quantum secret sharing (SQSS) scheme that generalizes Tian et al.&#x27;s three-party protocol \cite{Tian2021} to accommodate multiple participants. This scheme retains the original advantages, such as high qubit efficiency and allowing the secret dealer, Alice, to control the message content. However, He et al. \cite{He2024} identified a vulnerability in Tian et al.&#x27;s protocol to the double CNOT attack (DCNA), which also affects the generalized scheme. In response, He et al. proposed an improved protocol to address this issue. Despite these improvements, their protocol is limited to two participants and remains a primarily two-way communication scheme, which does not fully prevent the Trojan horse attack without expensive quantum devices such as photon number splitters (PNS) and wavelength filters (WF). To address these issues, this paper develops a novel multi-party SQSS scheme using the quantum property between Bell states and the Hadamard operation to detect eavesdroppers. This new scheme is secure against the DCNA, intercept-resend attack, and collective attack. It employs a fully one-way communication scheme, entirely preventing the Trojan horse attack without costly quantum devices, aligning with the semi-quantum environment&#x27;s original intent. This new protocol also offers better qubit efficiency and allows Alice to share specific secrets.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Race/Ethnicity Estimation for Algorithmic Bias Measurement in the U.S**
  2024-09-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.04652)
  Saikrishna Badrinarayanan, Osonde Osoba, Miao Cheng, Ryan Rogers, Sakshi Jain, Rahul Tandra, Natesh S. Pillai

  <details><summary>摘要 / Abstract</summary>

  AI fairness measurements, including tests for equal treatment, often take the form of disaggregated evaluations of AI systems. Such measurements are an important part of Responsible AI operations. These measurements compare system performance across demographic groups or sub-populations and typically require member-level demographic signals such as gender, race, ethnicity, and location. However, sensitive member-level demographic attributes like race and ethnicity can be challenging to obtain and use due to platform choices, legal constraints, and cultural norms. In this paper, we focus on the task of enabling AI fairness measurements on race/ethnicity for \emph{U.S. LinkedIn members} in a privacy-preserving manner. We present the Privacy-Preserving Probabilistic Race/Ethnicity Estimation (PPRE) method for performing this task. PPRE combines the Bayesian Improved Surname Geocoding (BISG) model, a sparse LinkedIn survey sample of self-reported demographics, and privacy-enhancing technologies like secure two-party computation and differential privacy to enable meaningful fairness measurements while preserving member privacy. We provide details of the PPRE method and its privacy guarantees. We then illustrate sample measurement operations. We conclude with a review of open research and engineering challenges for expanding our privacy-preserving fairness measurement capabilities.

  匹配依据：MPC: secure two party computation

  </details>

- **SLAMP-FSS: Two-Party Multi-Point Function Secret Sharing from Simple Linear Algebra**
  2024-09-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1394)
  Erki Külaots, Toomas Krips, Hendrik Eerikson, Darya Pisetskaya, Pille Pullonen-Raudvere

  <details><summary>摘要 / Abstract</summary>

  Multi-point function secret sharing (FSS) is a building block for pseudo-random correlation generators used in the novel silent correlation generation methods for various secure multi-party computation applications. However, the main construction used so far is the naive approach to combining several point functions. In this paper, we propose an efficient and natural generalisation of the point function FSS scheme of Boyle et al. 2016 using a tree structure, a pseudorandom generator and systems of linear equations. We propose a new notion of distributed random multi-point function. Our construction splits the distributed multi-point function scheme into a random multi-point function scheme and an algorithm to transform a random output into the desired output value. The resulting scheme, which we call SLAMP-FSS, improves upon the state of the art in terms of calls to a pseudorandom generator (PRG).

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **An Array Intermediate Language for Mixed Cryptography**
  2024-09-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.01587)
  Vivian Ding, Coşku Acay, Andrew C. Myers

  <details><summary>摘要 / Abstract</summary>

  We introduce AIRduct, a new array-based intermediate representation designed to support generating efficient code for interactive programs employing multiple cryptographic mechanisms. AIRduct is intended as an IR for the Viaduct compiler, which can synthesize secure, distributed programs with an extensible suite of cryptography. Therefore, AIRduct supports an extensible variety of cryptographic mechanisms, including MPC and ZKP.

  匹配依据：MPC: mpc (context)

  </details>

- **ACCESS-FL: Agile Communication and Computation for Efficient Secure Aggregation in Stable Federated Learning Networks**
  2024-09-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.01722)
  Niousha Nazemi, Omid Tavallaie, Shuaijun Chen, Anna Maria Mandalari, Kanchana Thilakarathna, Ralph Holz, Hamed Haddadi, Albert Y. Zomaya

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) is a promising distributed learning framework designed for privacy-aware applications. FL trains models on client devices without sharing the client&#x27;s data and generates a global model on a server by aggregating model updates. Traditional FL approaches risk exposing sensitive client data when plain model updates are transmitted to the server, making them vulnerable to security threats such as model inversion attacks where the server can infer the client&#x27;s original training data from monitoring the changes of the trained model in different rounds. Google&#x27;s Secure Aggregation (SecAgg) protocol addresses this threat by employing a double-masking technique, secret sharing, and cryptography computations in honest-but-curious and adversarial scenarios with client dropouts. However, in scenarios without the presence of an active adversary, the computational and communication cost of SecAgg significantly increases by growing the number of clients. To address this issue, in this paper, we propose ACCESS-FL, a communication-and-computation-efficient secure aggregation method designed for honest-but-curious scenarios in stable FL networks with a limited rate of client dropout. ACCESS-FL reduces the computation/communication cost to a constant level (independent of the network size) by generating shared secrets between only two clients and eliminating the need for double masking, secret sharing, and cryptography computations. To evaluate the performance of ACCESS-FL, we conduct experiments using the MNIST, FMNIST, and CIFAR datasets to verify the performance of our proposed method. The evaluation results demonstrate that our proposed method significantly reduces computation and communication overhead compared to state-of-the-art methods, SecAgg and SecAgg+.

  匹配依据：MPC: secret sharing

  </details>

- **Expanding self-orthogonal codes over a ring $\\Z\_4$ to self-dual codes and unimodular lattices**
  2024-08-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2409.00404)
  Minjia Shi, Sihui Tao, Jihoon Hong, Jon-Lark Kim

  <details><summary>摘要 / Abstract</summary>

  Self-dual codes have been studied actively because they are connected with mathematical structures including block designs and lattices and have practical applications in quantum error-correcting codes and secret sharing schemes. Nevertheless, there has been less attention to construct self-dual codes from self-orthogonal codes with smaller dimensions. Hence, the main purpose of this paper is to propose a way to expand any self-orthogonal code over a ring $\Z_4$ to many self-dual codes over $\Z_4$. We show that all self-dual codes over $\Z_4$ of lengths $4$ to $8$ can be constructed this way. Furthermore, we have found five new self-dual codes over $\Z_4$ of lengths $27, 28, 29, 33,$ and $34$ with the highest Euclidean weight $12$. Moreover, using Construction $A$ applied to our new Euclidean-optimal self-dual codes over $\Z_4$, we have constructed a new odd extremal unimodular lattice in dimension 34 whose kissing number was not previously known.

  匹配依据：MPC: secret sharing

  </details>

- **Leakage-Resilience of Circuit Garbling**
  2024-08-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1356)
  Ruiyang Li, Yiteng Sun, Chun Guo, Francois-Xavier Standaert, Weijia Wang, Xiao Wang

  <details><summary>摘要 / Abstract</summary>

  Due to the ubiquitous requirements and performance leap in the past decade, it has become feasible to execute garbling and secure computations in settings sensitive to side-channel attacks, including smartphones, IoTs and dedicated hardwares, and the possibilities have been demonstrated by recent works. To maintain security in the presence of a moderate amount of leaked information about internal secrets, we investigate {\it leakage-resilient garbling}. We augment the classical privacy, obliviousness and authenticity notions with leakages of the garbling function, and define their leakage-resilience analogues. We examine popular garbling schemes and unveil additional side-channel weaknesses due to wire label reuse and XOR leakages. We then incorporate the idea of label refreshing into the GLNP garbling scheme of Gueron et al. and propose a variant GLNPLR that provably satisfies our leakage-resilience definitions. Performance comparison indicates that GLNPLR is 60X (using AES-NI) or 5X (without AES-NI) faster than the HalfGates garbling with second order side-channel masking, for garbling AES circuit when the bandwidth is 2Gbps.

  匹配依据：MPC: garbling scheme, garbling schemes

  </details>

- **Enhancing MOTION2NX for Efficient, Scalable and Secure Image Inference using Convolutional Neural Networks**
  2024-08-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.16387)
  Haritha K, Ramya Burra, Srishti Mittal, Sarthak Sharma, Abhilash Venkatesh, Anshoo Tandon

  <details><summary>摘要 / Abstract</summary>

  This work contributes towards the development of an efficient and scalable open-source Secure Multi-Party Computation (SMPC) protocol on machines with moderate computational resources. We use the ABY2.0 SMPC protocol implemented on the C++ based MOTION2NX framework for secure convolutional neural network (CNN) inference application with semi-honest security. Our list of contributions are as follows. Firstly, we enhance MOTION2NX by providing a tensorized version of several primitive functions including the Hadamard product, indicator function and argmax function. Secondly, we adapt an existing Helper node algorithm, working in tandem with the ABY2.0 protocol, for efficient convolution computation to reduce execution time and RAM usage. Thirdly, we also present a novel splitting algorithm that divides the computations at each CNN layer into multiple configurable chunks. This novel splitting algorithm, providing significant reduction in RAM usage, is of independent interest and is applicable to general SMPC protocols.

  匹配依据：MPC: secure multi party computation

  </details>

- **Direct Range Proofs for Paillier Cryptosystem and Their Applications**
  2024-08-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1355)
  Zhikang Xie, Mengling Liu, Haiyang Xue, Man Ho Au, Robert H. Deng, Siu-Ming Yiu

  <details><summary>摘要 / Abstract</summary>

  The Paillier cryptosystem is renowned for its applications in electronic voting, threshold ECDSA, multi-party computation, and more, largely due to its additive homomorphism. In these applications, range proofs for the Paillier cryptosystem are crucial for maintaining security, because of the mismatch between the message space in the Paillier system and the operation space in application scenarios. In this paper, we present novel range proofs for the Paillier cryptosystem, specifically aimed at optimizing those for both Paillier plaintext and affine operation. We interpret encryptions and affine operations as commitments over integers, as opposed to solely over $\mathbb{Z}_{N}$. Consequently, we propose direct range proof for the updated cryptosystem, thereby eliminating the need for auxiliary integer commitments as required by the current state-of-the-art. Our work yields significant improvements: In the range proof for Paillier plaintext, our approach reduces communication overheads by approximately $60\%$, and computational overheads by $30\%$ and $10\%$ for the prover and verifier, respectively. In the range proof for Paillier affine operation, our method reduces the bandwidth by $70\%$, and computational overheads by $50\%$ and $30\%$ for the prover and verifier, respectively. Furthermore, we demonstrate that our techniques can be utilized to improve the performance of threshold ECDSA and the DCR-based instantiation of the Naor-Yung CCA2 paradigm.

  匹配依据：MPC: multi party computation

  </details>

- **Protecting Privacy in Federated Time Series Analysis: A Pragmatic Technology Review for Application Developers**
  2024-08-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.15694)
  Daniel Bachlechner, Ruben Hetfleisch, Stephan Krenn, Thomas Lorünser, Michael Rader

  <details><summary>摘要 / Abstract</summary>

  The federated analysis of sensitive time series has huge potential in various domains, such as healthcare or manufacturing. Yet, to fully unlock this potential, requirements imposed by various stakeholders must be fulfilled, regarding, e.g., efficiency or trust assumptions. While many of these requirements can be addressed by deploying advanced secure computation paradigms such as fully homomorphic encryption, certain aspects require an integration with additional privacy-preserving technologies. In this work, we perform a qualitative requirements elicitation based on selected real-world use cases. We match the derived requirements categories against the features and guarantees provided by available technologies. For each technology, we additionally perform a maturity assessment, including the state of standardization and availability on the market. Furthermore, we provide a decision tree supporting application developers in identifying the most promising technologies available matching their needs. Finally, existing gaps are identified, highlighting research potential to advance the field.

  匹配依据：MPC: secure computation

  </details>

- **On the overflow and $p$-adic theory applied to homomorphic encryption**
  2024-08-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1353)
  Jacob Blindenbach, Jung Hee Cheon, Gamze Gürsoy, Jiayi Kang

  <details><summary>摘要 / Abstract</summary>

  When integer and rational arithmetics are performed using modular arithmetics over $\mathbb{Z}/q\mathbb{Z}$, overflows naturally occur due to the mismatch between the infinite cardinality of $\mathbb{Z}$ or $\mathbb{Q}$ and the finite cardinality of $\mathbb{Z}/q\mathbb{Z}$. Since $\mathbb{Z}/q\mathbb{Z}$ is also the (sub) message space for many secure computation designs, secure computations of integer and rational arithmetics using these schemes must also consider the overflow problem. Previous works [CLPX, CT-RSA&#x27;18] and [HDRdS, ACNS&#x27;23] perform integer and rational arithmetics using the CLPX homomorphic encryption scheme, where overflows are avoided by restricting supported circuits. This introduces an additional constraint beyond the noise budget limitation. In our work, we discuss the possibilities of tolerating overflows. Firstly, we explain that when input messages and the final result are well-bounded, intermediate values can go arbitrarily large without affecting output correctness. This kind of overflow is called pseudo-overflow and does not need to be avoided. Secondly, we note that for prime-power modulus $q=p^r$, overflow errors are small in the $p$-adic norm. Therefore, we apply the $p$-adic encoding technique in [HDRdS, ACNS&#x27;23] to the BGV/BFV homomorphic encryption scheme with plaintext modulus $p^r$. Compared to [CLPX, CT-RSA&#x27;18] and [HDRdS, ACNS&#x27;23], our method supports circuits that are up to $2 \times$ deeper under the same ciphertext parameters, at the cost of an output error bounded by $p^{-r}$ in the $p$-adic norm.

  匹配依据：MPC: secure computation

  </details>

- **The Extended Mapping Obscuration to Reionization with ALMA (Ex-MORA) Survey: 5$σ$ Source Catalog and Redshift Distribution**
  2024-08-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.14546)
  Arianna S. Long, Caitlin M. Casey, Jed McKinney, Jorge A. Zavala, Hollis B. Akins, Olivia R. Cooper, Matthieu Bethermin Erini L. Lambrides, Maximilien Franco, Karina Caputi, Jaclyn B. Champagne, Allison W. S. Man, Ezequiel Treister, Sinclaire M. Manning, David B. Sanders, Margherita Talia, Manuel Aravena, D. L. Clements, Elisabete da Cunha, Andreas L. Faisst, Fabrizio Gentile, Jacqueline Hodge, Gabriel Brammer, Marcella Brusa, Steven L. Finkelstein, Seiji Fujimoto, Christopher C. Hayward, Olivier Ilbert, Jean-Baptiste Jolly, Jeyhan S. Kartaltepe, Kirsten Knudsen, Anton M. Koekemoer, Daizhong Liu, Georgios Magdis, Henry Joy McCracken, Jason Rhodes, Brant E. Robertson, Nick Scoville, Kartik Sheth, Vernesa Smolcic, Justin Spilker, Yoshiaki Taniguchi, Sune Toft, C. Megan Urry, Min Yun

  <details><summary>摘要 / Abstract</summary>

  One of the greatest challenges in galaxy evolution over the last decade has been constraining the prevalence of heavily dust-obscured galaxies in the early Universe. At $z&gt;3$, these galaxies are increasingly rare, and difficult to identify as they are interspersed among the more numerous dust-obscured galaxy population at $z=1-3$, making efforts to secure confident spectroscopic redshifts expensive, and sometimes unsuccessful. In this work, we present the Extended Mapping Obscuration to Reionization with ALMA (Ex-MORA) Survey -- a 2mm blank-field survey in the COSMOS-Web field, and the largest ever ALMA blank-field survey to-date covering 577 arcmin$^2$. Ex-MORA is an expansion of the MORA survey designed to identify primarily $z&gt;3$ dusty, star-forming galaxies while simultaneously filtering out the more numerous $z $5$σ$) sources, 33 of which are robust thermal dust emitters. We measure a median redshift of $\langle z \rangle = 3.6^{+0.1}_{-0.2}$, with two-thirds of the sample at $z&gt;3$, and just under half at $z&gt;4$, demonstrating the overall success of the 2mm-selection technique. The integrated $z&gt;3$ volume density of Ex-MORA sources is $\sim1-3\times10^{-5}$ Mpc$^{-3}$, consistent with other surveys of infrared luminous galaxies at similar epochs. We also find that techniques using rest-frame optical emission (or lack thereof) to identify $z&gt;3$ heavily dust-obscured galaxies miss at least half of Ex-MORA galaxies. This supports the idea that the dusty galaxy population is heterogeneous, and that synergies across observatories spanning multiple energy regimes are critical to understanding their formation and evolution at $z&gt;3$.

  匹配依据：MPC: mpc (context)

  </details>

- **FRB Line-of-sight Ionization Measurement From Lightcone AAOmega Mapping Survey: the First Data Release**
  2024-08-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.12864)
  Yuxin Huang, Sunil Simha, Ilya Khrykin, Khee-Gan Lee, J. Xavier Prochaska, Nicolas Tejos, Keith Bannister, Jason Barrios, John Chisholm, Jeff Cooke, Adam Deller, Marcin Glowacki, Lachlan Marnoch, Ryan Shannon, Jielai Zhang

  <details><summary>摘要 / Abstract</summary>

  This paper presents the first public data release (DR1) of the FRB Line-of-sight Ionization Measurement From Lightcone AAOmega Mapping (FLIMFLAM) Survey, a wide field spectroscopic survey targeted on the fields of 10 precisely localized Fast Radio Bursts (FRBs). DR1 encompasses spectroscopic data for 10,468 galaxy redshifts across 10 FRBs fields with z 10 Mpc scales), `Narrow&#x27;, (several-arcminute or ~ Mpc) and integral field unit (`IFU&#x27;; ~ arcminute or ~ 100 kpc ) components. The bulk of the data comprise spectroscopy from the 2dF-AAOmega on the 3.9-meter Anglo-Australian Telescope, while most of the Narrow and IFU data was achieved using an ensemble of 8-10-meter class telescopes. We summarize the information on our selected FRB fields, the criteria for target selection, methodologies employed for data reduction, spectral analysis processes, and an overview of our data products. An evaluation of our data reveals an average spectroscopic completeness of 48.43%, with over 80% of the observed targets having secure redshifts. Additionally, we describe our approach on generating angular masks and calculating the target selection functions, setting the stage for the impending reconstruction of the matter density field.

  匹配依据：MPC: mpc (context)

  </details>

- **MAESTRO: Multi-party AES using Lookup Tables**
  2024-08-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1317)
  Hiraku Morita, Erik Pohle, Kunihiko Sadakane, Peter Scholl, Kazunari Tozawa, Daniel Tschudi

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) enables multiple distrusting parties to jointly compute a function while keeping their inputs private. Computing the AES block cipher in MPC, where the key and/or the input are secret-shared among the parties is important for various applications, particularly threshold cryptography. In this work, we propose a family of dedicated, high-performance MPC protocols to compute the non-linear S-box part of AES in the honest majority setting. Our protocols come in both semi-honest and maliciously secure variants. The core technique is a combination of lookup table protocols based on random one-hot vectors and the decomposition of finite field inversion in $GF(2^8)$ into multiplications and inversion in the smaller field $GF(2^4)$, taking inspiration from ideas used for hardware implementations of AES. We also apply and improve the analysis of a batch verification technique for checking inner products with logarithmic communication. This allows us to obtain malicious security with almost no communication overhead, and we use it to obtain new, secure table lookup protocols with only $O(\sqrt{N})$ communication for a table of size $N$, which may be useful in other applications. Our protocols have different trade-offs, such as having a similar round complexity as previous state-of-the-art by Chida et al. [WAHC&#x27;18] but $37\%$ lower bandwidth costs, or having $27\%$ fewer rounds and $16\%$ lower bandwidth costs. An experimental evaluation in various network conditions using three party replicated secret sharing shows improvements in throughput between $28\%$ and $71\%$ in the semi-honest setting. For malicious security, we improve throughput by $319\%$ to $384\%$ in LAN and by $717\%$ in WAN due to sublinear batch verification.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Generalized Triangular Dynamical System: An Algebraic System for Constructing Cryptographic Permutations over Finite Fields**
  2024-08-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2204.01802) · [IACR ePrint](https://eprint.iacr.org/2024/1316)
  Arnab Roy, Matthias Johann Steiner

  <details><summary>摘要 / Abstract</summary>

  In recent years a new class of symmetric-key primitives over $\mathbb{F}_p$ that are essential to Multi-Party Computation and Zero-Knowledge Proofs based protocols has emerged. Towards improving the efficiency of such primitives, a number of new block ciphers and hash functions over $\mathbb{F}_p$ were proposed. These new primitives also showed that following alternative design strategies to the classical Substitution-Permutation Network (SPN) and Feistel Networks leads to more efficient cipher and hash function designs over $\mathbb{F}_p$ specifically for large odd primes $p$. In view of these efforts, in this work we build an \emph{algebraic framework} that allows the systematic exploration of viable and efficient design strategies for constructing symmetric-key (iterative) permutations over $\mathbb{F}_p$. We first identify iterative polynomial dynamical systems over finite fields as the central building block of almost all block cipher design strategies. We propose a generalized triangular polynomial dynamical system (GTDS), and based on the GTDS we provide a generic definition of an iterative (keyed) permutation over $\mathbb{F}_p^n$. Our GTDS-based generic definition is able to describe the three most well-known design strategies, namely SPNs, Feistel networks (FN) and Lai--Massey (LM). Consequently, the block ciphers that are constructed following these design strategies can also be instantiated from our generic definition. Moreover, we find that the recently proposed \texttt{Griffin} design, which neither follows the Feistel nor the SPN design, can be described using the generic GTDS-based definition. We also show that a new generalized Lai--Massey construction can be instantiated from the GTDS-based definition. The latter results confirm that our GTDS-based definition is able to instantiate cryptographic permutations that are beyond SPN, FN and LM based. We further provide generic (security) analysis of the GTDS including an upper bound on the differential uniformity and the correlation.

  匹配依据：MPC: multi party computation

  </details>

- **Cheating in quantum Rabin oblivious transfer using delayed measurements**
  2024-08-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.12388)
  James T. Peat, Erika Andersson

  <details><summary>摘要 / Abstract</summary>

  Oblivious transfer has been the interest of study as it can be used as a building block for multiparty computation. There are many forms of oblivious transfer; we explore a variant known as Rabin oblivious transfer. Here the sender Alice has one bit, and the receiver Bob obtains this bit with a certain probability. The sender does not know whether the receiver obtained the bit or not. For a previously suggested protocol, we show a possible attack using a delayed measurement. This allows a cheating party to pass tests carried out by the other party, while gaining more information than if they would have been honest. We show how this attack allows perfect cheating, unless the protocol is modified, and suggest changes which lower the cheating probability for the examined cheating strategies.

  匹配依据：MPC: multiparty computation, oblivious transfer

  </details>

- **Good binary quantum codes with transversal CCZ gate**
  2024-08-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.10140)
  Quynh T. Nguyen

  <details><summary>摘要 / Abstract</summary>

  We give an asymptotically good family of quantum CSS codes on qubits with a transversal CCZ gate, meaning that the parallel logical CCZ on all logical qubits is performed by parallel physical CCZs on (a subset of) physical qubits. The construction is based on the observation that any classical code satisfying a multiplication property can be used to construct a quantum CSS code with transversal (qudit) CCZ. To obtain a constant-rate and linear-distance family, we then instantiate this construction with a classical good family of algebraic-geometry codes on a non-binary, but constant-sized, alphabet. Finally, we use a technique from the arithmetic secret sharing literature to reduce the alphabet to binary. As a corollary, the constructed code family provides a magic state distillation scheme with constant space overhead.

  匹配依据：MPC: secret sharing

  </details>

- **Robust Multiparty Computation from Threshold Encryption Based on RLWE**
  2024-08-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1285)
  Antoine Urban, Matthieu Rambaud

  <details><summary>摘要 / Abstract</summary>

  We consider protocols for secure multi-party computation (MPC) built from FHE under honest majority, i.e., for $n=2t+1$ players of which $t$ are corrupt, that are robust. Surprisingly there exists no robust threshold FHE scheme based on BFV to design such MPC protocols. Precisely, all existing methods for generating a common relinearization key can abort as soon as one player deviates. We address this issue, with a new relinearization key (adapted from [CDKS19, CCS&#x27;19]) which we show how to securely generate in parallel of the threshold encryption key, in the same broadcast. We thus obtain the first robust threshold BFV scheme, moreover using only one broadcast for the generation of keys instead of two previously. Of independent interest, as an optional alternative, we propose the first threshold FHE decryption enabling simultaneously: (i) robustness over asynchronous channels with honest majority; (ii) tolerating a power-of-small-prime ciphertext modulus, e.g., $2^e$; and (iii) secret shares of sizes quasi-independent of $n$.

  匹配依据：MPC: multiparty computation, secure multi party computation

  </details>

- **GridSE: Towards Practical Secure Geographic Search via Prefix Symmetric Searchable Encryption (Full Version)**
  2024-08-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.07916) · [Code](https://github.com/rykieguo1771/GridSE-RAM)
  Ruoyang Guo, Jiarui Li, Shucheng Yu

  <details><summary>摘要 / Abstract</summary>

  The proliferation of location-based services and applications has brought significant attention to data and location privacy. While general secure computation and privacy-enhancing techniques can partially address this problem, one outstanding challenge is to provide near latency-free search and compatibility with mainstream geographic search techniques, especially the Discrete Global Grid Systems (DGGS). This paper proposes a new construction, namely GridSE, for efficient and DGGS-compatible Secure Geographic Search (SGS) with both backward and forward privacy. We first formulate the notion of a semantic-secure primitive called \textit{symmetric prefix predicate encryption} (SP$^2$E), for predicting whether or not a keyword contains a given prefix, and provide a construction. Then we extend SP$^2$E for dynamic \textit{prefix symmetric searchable encryption} (pSSE), namely GridSE, which supports both backward and forward privacy. GridSE only uses lightweight primitives including cryptographic hash and XOR operations and is extremely efficient. Furthermore, we provide a generic pSSE framework that enables prefix search for traditional dynamic SSE that supports only full keyword search. Experimental results over real-world geographic databases of sizes (by the number of entries) from $10^3$ to $10^7$ and mainstream DGGS techniques show that GridSE achieves a speedup of $150\times$ - $5000\times$ on search latency and a saving of $99\%$ on communication overhead as compared to the state-of-the-art. Interestingly, even compared to plaintext search, GridSE introduces only $1.4\times$ extra computational cost and $0.9\times$ additional communication cost. Source code of our scheme is available at https://github.com/rykieguo1771/GridSE-RAM.

  匹配依据：MPC: secure computation

  </details>

- **Password-authenticated Cryptography from Consumable Tokens**
  2024-08-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1283)
  Ghada Almashaqbeh

  <details><summary>摘要 / Abstract</summary>

  Passwords are widely adopted for user authentication in practice, which led to the question of whether we can bootstrap a strongly-secure setting based on them. Historically, this has been extensively studied for key exchange; bootstrap from a low-entropy password to a high entropy key securing the communication. Other instances include digital lockers, signatures, secret sharing, and encryption. Motivated by a recent work on consumable tokens (Almashaqbeh et al., Eurocrypt 2022), we extend these efforts and investigate the unified notion of password-authenticated cryptography in which knowing a password allows executing cryptographic functionalities. Our model is resistant to exhaustive search attacks due to the self-destruction and unclonability properties of consumable tokens. We study two directions; the first is password-authenticated delegation of cryptographic capabilities in which a party can delegate her, e.g., signing or encryption/decryption, rights to another such that exercising the delegation requires knowing a password. The second direction is password-authenticated MPC, in which only participants who share the correct password can execute the MPC protocol. In both cases, an adversary who does not know the password can try a few guesses after which the functionality self-destructs. We formally define the notions above and build constructions realizing them. Our primary goal in this work is examining the power of consumable tokens in building password-authenticated cryptography in terms of viable constructions and supported adversary models, and thus, outlining open problems and potential future work directions.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy in Federated Learning**
  2024-08-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.08904)
  Jaydip Sen, Hetvi Waghela, Sneha Rakshit

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) represents a significant advancement in distributed machine learning, enabling multiple participants to collaboratively train models without sharing raw data. This decentralized approach enhances privacy by keeping data on local devices. However, FL introduces new privacy challenges, as model updates shared during training can inadvertently leak sensitive information. This chapter delves into the core privacy concerns within FL, including the risks of data reconstruction, model inversion attacks, and membership inference. It explores various privacy-preserving techniques, such as Differential Privacy (DP) and Secure Multi-Party Computation (SMPC), which are designed to mitigate these risks. The chapter also examines the trade-offs between model accuracy and privacy, emphasizing the importance of balancing these factors in practical implementations. Furthermore, it discusses the role of regulatory frameworks, such as GDPR, in shaping the privacy standards for FL. By providing a comprehensive overview of the current state of privacy in FL, this chapter aims to equip researchers and practitioners with the knowledge necessary to navigate the complexities of secure federated learning environments. The discussion highlights both the potential and limitations of existing privacy-enhancing techniques, offering insights into future research directions and the development of more robust solutions.

  匹配依据：MPC: secure multi party computation

  </details>

- **Generation of Authenticated Secret-Shared Scaled Unit Vectors for Beaver Triples**
  2024-08-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1274)
  Vincent Rieder

  <details><summary>摘要 / Abstract</summary>

  For secure multi-party computation in the line of the secret-sharing based SPDZ protocol, actively secure multiplications consume correlated randomness in the form of authenticated Beaver triples, which need to be generated in advance. Although it is a well-studied problem, the generation of Beaver triples is still a bottleneck in practice. In the two-party setting, the best solution with low communication overhead is the protocol by Boyle et al. (Crypto 2020), which is derived from the recent primitive of Pseudorandom Correlation Generators (PCGs) (Crypto 2019). Their protocol requires less than 2 MB of communication to generate about 100 MB of Beaver triples (per party). In this work, we improve their protocol in terms of communication (7%), computation (20% for its interactive phase), and the amount of correlated randomness consumed by internal secure two-party computations (11% storage). To achieve our improvements, we propose a novel actively secure protocol for the efficient generation of (authenticated) secret-shared scaled unit vectors, which in general are the main building blocks of current PCG protocols.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **AES-based Multi-instance TCCR Hash with High Security, and Applications**
  2024-08-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1271)
  Hongrui Cui, Chun Guo, Xiao Wang, Chenkai Weng, Kang Yang, Yu Yu

  <details><summary>摘要 / Abstract</summary>

  Correlation robust hash function (CRHF) is an important class of building blocks that have found applications in many cryptographic applications, including various protocols for zero-knowledge (ZK) proof, circuit garbling, vector oblivious linear evaluation (VOLE), etc. It offers more efficient instantiations from block ciphers as compared to cryptographic hash functions like SHA-3. State-of-the-art instantiations work provide near-optimal security in the ideal cipher model that can in turn be efficiently instantiated using AES, which is standardized and provides instruction-level acceleration. However, since AES is only available for 128-bit block size, they cannot be generalized beyond 128-bit security while enjoying the same level of efficiency. In this paper, we fill this gap by constructing a new multi-instance tweakable circular CRHF (miTCCR) from AES, supporting up to 256-bit security. Since miTCCR is the most general notion of CRHF, it directly leads to numerous applications. 1. The state-of-the-art optimization of GGM tree (Eurocrypt&#x27;23), which builds on circular CRHF as a black box, can be instantiated with our construction, boosting its security strength, as well as the security of the VOLE-ZK protocols building on top, from 128 bits to 256 bits. 2. With a new extractability notion, we use the miTCCR hash to instantiate the leaf commitment in an all-but-one vector commitment scheme, which is a core primitive of post-quantum digital signature schemes and ZK in the VOLE-in-the-Head framework. Experiments show that our technique could reduce the end-to-end signing/verification time of FAEST (resp. FAEST-EM) by 13.1%~40.4% / 15.2%~46.4% (resp. 1.5%~25.0% / 2.9%~24.2%). 3. The multi-instance-secure half-gates garbling scheme (Crypto&#x27;20) uses miTCCR as a black box. Our construction can strengthen its security as well as the security of constant-round multiparty computation building on half-gates to 246-bit.

  匹配依据：MPC: garbling scheme, multiparty computation

  </details>

- **Quantum-secure multiparty deep learning**
  2024-08-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.05629)
  Kfir Sulimany, Sri Krishna Vadlamani, Ryan Hamerly, Prahlad Iyengar, Dirk Englund

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation enables the joint evaluation of multivariate functions across distributed users while ensuring the privacy of their local inputs. This field has become increasingly urgent due to the exploding demand for computationally intensive deep learning inference. These computations are typically offloaded to cloud computing servers, leading to vulnerabilities that can compromise the security of the clients&#x27; data. To solve this problem, we introduce a linear algebra engine that leverages the quantum nature of light for information-theoretically secure multiparty computation using only conventional telecommunication components. We apply this linear algebra engine to deep learning and derive rigorous upper bounds on the information leakage of both the deep neural network weights and the client&#x27;s data via the Holevo and the Cramér-Rao bounds, respectively. Applied to the MNIST classification task, we obtain test accuracies exceeding $96\%$ while leaking less than $0.1$ bits per weight symbol and $0.01$ bits per data symbol. This weight leakage is an order of magnitude below the minimum bit precision required for accurate deep learning using state-of-the-art quantization techniques. Our work lays the foundation for practical quantum-secure computation and unlocks secure cloud deep learning as a field.

  匹配依据：MPC: secure computation, secure multiparty computation

  </details>

- **Improved YOSO Randomness Generation with Worst-Case Corruptions**
  2024-08-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1268)
  Chen-Da Liu-Zhang, Elisaweta Masserova, João Ribeiro, Pratik Soni, Sri AravindaKrishnan Thyagarajan

  <details><summary>摘要 / Abstract</summary>

  We study the problem of generating public unbiased randomness in a distributed manner within the recent You Only Speak Once (YOSO) framework for stateless multiparty computation, introduced by Gentry et al. in CRYPTO 2021. Such protocols are resilient to adaptive denial-of-service attacks and are, by their stateless nature, especially attractive in permissionless environments. While most works in the YOSO setting focus on independent random corruptions, we consider YOSO protocols with worst-case corruptions, a model introduced by Nielsen et al. in CRYPTO 2022. Prior work on YOSO public randomness generation with worst-case corruptions designed information-theoretic protocols for $t$ corruptions with either $n=6t+1$ or $n=5t$ roles, depending on the adversarial network model. However, a major drawback of these protocols is that their communication and computational complexities scale exponentially with $t$. In this work, we complement prior inefficient results by presenting and analyzing simple and efficient protocols for YOSO public randomness generation secure against worst-case corruptions in the computational setting. Our first protocol is based on publicly verifiable secret sharing and uses $n=3t+2$ roles. Since this first protocol requires setup and somewhat heavy cryptographic machinery, we also provide a second lighter protocol based on ElGamal commitments and verifiable secret sharing which uses $n=5t+4$ or $n=4t+4$ roles depending on the underlying network model. We demonstrate the practicality of our second protocol by showing experimental evaluations, significantly improving over prior proposed solutions for worst-case corruptions, especially in terms of transmitted data size.

  匹配依据：MPC: multiparty computation, secret sharing

  </details>

- **Dilithium-Based Verifiable Timed Signature Scheme**
  2024-08-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1262)
  Erkan Uslu, Oğuz Yayla

  <details><summary>摘要 / Abstract</summary>

  Verifiable Timed Signatures (VTS) are cryptographic constructs that enable obtaining a signature at a specific time in the future and provide evidence that the signature is legitimate. This framework particularly finds utility in applications such as payment channel networks, multiparty signing operations, or multiparty computation, especially within blockchain architectures. Currently, VTS schemes are based on signature algorithms such as BLS signature, Schnorr signature, and ECDSA. These signature algorithms are considered insecure against quantum attacks due to the effect of Shor&#x27;s Algorithm on the discrete logarithm problem. We present a new VTS scheme called VT-Dilithium based on CRYSTALS-Dilithium Digital Signature Algorithm that has been selected as NIST&#x27;s quantum-resistant digital signature standard and is considered secure against both classical and quantum attacks. Integrating Dilithium into the VTS scheme is more challenging problem due to its complex mathematical operations (i.e. polynomial multiplications, rounding operations) and large module parameters such as polynomials, polynomial vectors, and matrices. This work aims to provide a comprehensive exposition of the VT-Dilithium scheme.

  匹配依据：MPC: multiparty computation

  </details>

- **MPC-Minimized Secure LLM Inference**
  2024-08-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.03561)
  Deevashwer Rathee, Dacheng Li, Ion Stoica, Hao Zhang, Raluca Popa

  <details><summary>摘要 / Abstract</summary>

  Many inference services based on large language models (LLMs) pose a privacy concern, either revealing user prompts to the service or the proprietary weights to the user. Secure inference offers a solution to this problem through secure multi-party computation (MPC), however, it is still impractical for modern LLM workload due to the large overhead imposed by MPC. To address this overhead, we propose Marill, a framework that adapts LLM fine-tuning to minimize MPC usage during secure inference. Marill introduces high-level architectural changes during fine-tuning that significantly reduce the number of expensive operations needed within MPC during inference, by removing some and relocating others outside MPC without compromising security. As a result, Marill-generated models are more efficient across all secure inference protocols and our approach complements MPC-friendly approximations for such operations. Compared to standard fine-tuning, Marill results in 3.6-11.3x better runtime and 2.4-6.9x better communication during secure inference across various MPC settings, while typically preserving over 90% performance across downstream tasks.

  匹配依据：MPC: secure multi party computation

  </details>

- **Efficient Differentially Private Set Intersection**
  2024-08-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1239)
  Xinyu Peng, Yufei Wang, Weiran Liu, Liqiang Peng, Feng Han, Zhen Gu, Jianling Sun, Yuan Hong

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection (PSI) enables a sender and a receiver to jointly compute the intersection of their sets without disclosing non-trivial information about other items. However, depending on the context of joint data analysis, information derived from the items in the intersection may also be considered sensitive. To protect such sensitive information, prior work proposed Differentially private PSI (DPSI), which can be instantiated with circuit-PSI using Fully Homomorphic Encryption. Although asymptotically efficient, its concrete performance is sub-optimal compared with the practical state-of-the-art (SOTA) circuit-PSI. In this paper, we propose two generic DPSI constructions with provable security and privacy. We revisit the DPSI definition and identify the critical criteria for selecting essential PSI-related tools. Then, we present two generic DPSI constructions. The first construction allows us to achieve provable privacy and efficiency by integrating any circuit-PSI with the randomized response mechanism. By plugging the SOTA circuit-PSI protocol, we obtain a DPSI protocol with concrete performance enhancement. The second construction offers a more efficient DPSI alternative by using multi-query Reverse Private Membership Test (mqRPMT) at the price of intersection size leakage, but such leakages can be bounded with differential privacy by padding random dummy items in input sets. We conduct comprehensive experiments with various instantiations. The experiments show that our instantiations significantly outperform the existing DPSI construction: 2.5-22.6$\times$ more communication-efficient and up to 110.5-151.8$\times$ faster. Our work also shows a new application for mqRPMT besides obtaining Private Set Operation (PSO).

  匹配依据：MPC: private set intersection

  </details>

- **TreeCSS: An Efficient Framework for Vertical Federated Learning**
  2024-08-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.01691)
  Qinbo Zhang, Xiao Yan, Yukai Ding, Quanqing Xu, Chuang Hu, Xiaokai Zhou, Jiawei Jiang

  <details><summary>摘要 / Abstract</summary>

  Vertical federated learning (VFL) considers the case that the features of data samples are partitioned over different participants. VFL consists of two main steps, i.e., identify the common data samples for all participants (alignment) and train model using the aligned data samples (training). However, when there are many participants and data samples, both alignment and training become slow. As such, we propose TreeCSS as an efficient VFL framework that accelerates the two main steps. In particular, for sample alignment, we design an efficient multi-party private set intersection (MPSI) protocol called Tree-MPSI, which adopts a tree-based structure and a data-volume-aware scheduling strategy to parallelize alignment among the participants. As model training time scales with the number of data samples, we conduct coreset selection (CSS) to choose some representative data samples for training. Our CCS method adopts a clustering-based scheme for security and generality, which first clusters the features locally on each participant and then merges the local clustering results to select representative samples. In addition, we weight the samples according to their distances to the centroids to reflect their importance to model training. We evaluate the effectiveness and efficiency of our TreeCSS framework on various datasets and models. The results show that compared with vanilla VFL, TreeCSS accelerates training by up to 2.93x and achieves comparable model accuracy.

  匹配依据：MPC: private set intersection

  </details>

- **Fed-RD: Privacy-Preserving Federated Learning for Financial Crime Detection**
  2024-08-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.01609)
  Md. Saikat Islam Khan, Aparna Gupta, Oshani Seneviratne, Stacy Patterson

  <details><summary>摘要 / Abstract</summary>

  We introduce Federated Learning for Relational Data (Fed-RD), a novel privacy-preserving federated learning algorithm specifically developed for financial transaction datasets partitioned vertically and horizontally across parties. Fed-RD strategically employs differential privacy and secure multiparty computation to guarantee the privacy of training data. We provide theoretical analysis of the end-to-end privacy of the training algorithm and present experimental results on realistic synthetic datasets. Our results demonstrate that Fed-RD achieves high model accuracy with minimal degradation as privacy increases, while consistently surpassing benchmark results.

  匹配依据：MPC: secure multiparty computation

  </details>

- **MapComp: A Secure View-based Collaborative Analytics Framework for Join-Group-Aggregation**
  2024-08-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.01246)
  Xinyu Peng, Feng Han, Li Peng, Weiran Liu, Zheng Yan, Kai Kang, Xinyuan Zhang, Guoxing Wei, Jianling Sun, Jinfei Liu, Lin Qu

  <details><summary>摘要 / Abstract</summary>

  Join-group-aggregation (JGA) queries are fundamental to data analytics, yet executing them collaboratively across different parties poses significant privacy risks. Secure multi-party computation (MPC) offers a cryptographic solution. However, existing MPC-based JGA approaches consider only a one-time query paradigm and suffer from significant performance bottlenecks. It executes expensive join operations from scratch across multiple queries and employs inefficient group-aggregation (GA) protocols, both of which hinder their practical use for scalable, real-time analysis. This paper introduces MapComp, a novel view-based framework to facilitate JGA queries for secure collaborative analytics. Through specially crafted materialized views for join and novel design of GA protocols, MapComp removes duplicate join workload and expedites subsequent GA, improving the efficiency of JGA query execution. To address the challenge of continuous data updates, our materialized view offers payload-independence feature and provides significant efficiency improvements in view refreshing with free MPC overhead. This feature, on the other hand, also allows further acceleration for GA, where we devise multiple novel protocols that outperform prior works. Notably, our work represents the first endeavor to expedite secure collaborative JGA queries using materialized views. Our rigorous experiments demonstrate a significant advantage of MapComp, achieving up to a 308.9x improvement in efficiency over the baseline in real-world query simulations. Moreover, our optimized GA protocols achieve up to a 1140.5x improvement compared to prior oblivious sorting-based solutions.

  匹配依据：MPC: secure multi party computation

  </details>

- **Secret Sharing for Secure and Private Information Retrieval: A Construction Using Algebraic Geometry Codes**
  2024-08-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.00542)
  Okko Makkonen, David Karpuk, Camilla Hollanti

  <details><summary>摘要 / Abstract</summary>

  Private information retrieval (PIR) considers the problem of retrieving a data item from a database or distributed storage system without disclosing any information about which data item was retrieved. Secure PIR complements this problem by further requiring the contents of the data to be kept secure. Privacy and security can be achieved by adding suitable noise to the queries and data using methods from secret sharing. In this paper, a new framework for homomorphic secret sharing in secure and private information retrieval from colluding servers is proposed, generalizing the original cross-subspace alignment (CSA) codes proposed by Jia, Sun, and Jafar. We utilize this framework to give a secure PIR construction using algebraic geometry codes over hyperelliptic curves of arbitrary genus. It is shown that the proposed scheme offers interesting tradeoffs between the field size, file size, number of colluding servers, and the total number of servers. When the field size is fixed, this translates in some cases to higher retrieval rates than those of the original scheme. In addition, the new schemes exist also for some parameters where the original ones do not.

  匹配依据：MPC: secret sharing

  </details>

- **A Survey on the Applications of Zero-Knowledge Proofs**
  2024-08-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2408.00243)
  Ryan Lavin, Xuekai Liu, Hardhik Mohanty, Logan Norman, Giovanni Zaarour, Bhaskar Krishnamachari

  <details><summary>摘要 / Abstract</summary>

  Zero-knowledge proofs (ZKPs) enable computational integrity and privacy by allowing one party to prove the truth of a statement without revealing underlying data. Compared with alternatives such as homomorphic encryption and secure multiparty computation, ZKPs offer distinct advantages in universality and minimal trust assumptions, with applications spanning blockchain systems and confidential verification of computational tasks. This survey provides a technical overview of ZKPs with a focus on an increasingly relevant subset called zkSNARKs. Unlike prior surveys emphasizing algorithmic and theoretical aspects, we take a broader view of practical deployments and recent use cases across multiple domains including blockchain privacy, scaling, storage, and interoperability, as well as non-blockchain applications such as voting, authentication, timelocks, and machine learning. To support consistent comparison, we provide (i) a taxonomy of application areas, (ii) evaluation criteria including proof size, prover and verifier time, memory, and setup assumptions, and (iii) comparative tables summarizing key tradeoffs and representative systems. The survey also covers supporting infrastructure, including zero-knowledge virtual machines, domain-specific languages, libraries, and frameworks. While emphasizing zkSNARKs for their prevalence in deployed systems, we compare them with zkSTARKs and Bulletproofs to clarify transparency and performance tradeoffs. We conclude with future research and application directions.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Distributed Symmetric Key Establishment: a Scalable Quantum-Safe Key Distribution Protocol**
  2024-07-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.20969)
  Jie Lin, Hoi-Kwong Lo, Jacob Johannsson, Mattia Montagna, Manfred von Willich

  <details><summary>摘要 / Abstract</summary>

  Pre-shared keys (PSK) have been widely used in network security. Nonetheless, existing PSK solutions are not scalable. Moreover, whenever a new user joins a network, PSK requires an existing user to get a new key before they are able to communicate with the new user. The key issue is how to distribute the PSK between different users. Here, we solve this problem by proposing a new protocol called Distributed Symmetric Key Establishment (DSKE). DSKE has the advantage of being scalable. Unlike standard public key infrastructure (PKI) which relies on computational assumptions, DSKE provides information-theoretic security in a universally composable security framework. Specifically, we prove the security (correctness and confidentiality) and robustness of this protocol against a computationally unbounded adversary, who additionally may have fully compromised a bounded number of the intermediaries and can eavesdrop on all communication. DSKE also achieves distributed trust through secret sharing. We present several implementations of DSKE in real environments, such as providing client services to link encryptors, network encryptors, and mobile phones, as well as the implementation of intermediaries, called Security Hubs, and associated test data as evidence for its versatility. As DSKE is highly scalable in a network setting with no distance limit, it is expected to be a cost-effective quantum-safe cryptographic solution to the network security threat presented by quantum computers.

  匹配依据：MPC: secret sharing

  </details>

- **Advance Sharing Procedures for the Ramp Quantum Secret Sharing Schemes With the Highest Coding Rate**
  2024-07-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.20661)
  Ryutaroh Matsumoto

  <details><summary>摘要 / Abstract</summary>

  In some quantum secret sharing schemes, it is known that some shares can be distributed to participants before a secret is given to the dealer. However, it is unclear whether some shares can be distributed before a secret is given in the ramp quantum secret sharing schemes with the highest coding rate. In this paper, we propose procedures to distribute some shares before a secret is given in those schemes. The new procedures enhances applicability of the secret sharing schemes to wider scenarios as some participants can be unavailable when the dealer obtains the quantum secret. Then we prove that our new encoding procedures retain the correspondences between quantum secrets and quantum shares in the original schemes, which ensures the highest coding rates of the original schemes are also retained.

  匹配依据：MPC: secret sharing

  </details>

- **Dynamic Bounded-Collusion Streaming Functional Encryption from Minimal Assumptions**
  2024-07-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1213)
  Kaartik Bhushan, Alexis Korb, Amit Sahai

  <details><summary>摘要 / Abstract</summary>

  Streaming functional encryption (sFE), recently introduced by Guan, Korb, and Sahai [Crypto 2023], is an extension of functional encryption (FE) tailored for iterative computation on dynamic data streams. Unlike in regular FE, in an sFE scheme, users can encrypt and compute on the data as soon as it becomes available and in time proportional to just the size of the newly arrived data. As sFE implies regular FE, all known constructions of sFE and FE for P/poly require strong cryptographic assumptions which are powerful enough to build indistinguishability obfuscation (iO). In contrast, dynamic bounded-collusion FE, in which the adversary is restricted to making at most Q function queries for some Q determined during encryption (but not fixed at time of setup), can be built from the minimal assumptions of identity-based encryption (for public-key FE) [Agrawal, Maitra, Vempati and Yamada, Crypto 2021; Garg, Goyal, Lu and Waters, Eurocrypt 2022] and one-way functions (for secret-key FE), as secret-key IBE is implied by one-way functions (folklore). In this paper, we introduce and build dynamic bounded-collusion streaming FE from the same minimal assumptions of identity-based encryption (for public-key sFE) and one-way functions (for secret-key sFE). Similarly to the original sFE paper of Guan, Korb, and Sahai, our scheme satisfies semi-adaptive-function-selective security which is similar to standard adaptive indistinguishability-based security except that we require all functions to be queried before any of the challenge messages. Along the way, our work also replaces a key ingredient (called OnesFE) from the original work of Guan, Korb, and Sahai with a much simpler construction based on garbled circuits. In contrast, the original approach relied on the powerful object of compact FE (which is known to imply iO) to construct this primitive.

  匹配依据：MPC: garbled circuits

  </details>

- **Collaborative CP-NIZKs: Modular, Composable Proofs for Distributed Secrets**
  2024-07-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.19212) · [IACR ePrint](https://eprint.iacr.org/2024/1209)
  Mohammed Alghazwi, Tariq Bontekoe, Leon Visscher, Fatih Turkmen

  <details><summary>摘要 / Abstract</summary>

  Non-interactive zero-knowledge (NIZK) proofs of knowledge have proven to be highly relevant for securely realizing a wide array of applications that rely on both privacy and correctness. They enable a prover to convince any party of the correctness of a public statement for a secret witness. However, most NIZKs do not natively support proving knowledge of a secret witness that is distributed over multiple provers. Previously, collaborative proofs [51] have been proposed to overcome this limitation. We investigate the notion of composability in this setting, following the Commit-and-Prove design of LegoSNARK [17]. Composability allows users to combine different, specialized NIZKs (e.g., one arithmetic circuit, one boolean circuit, and one for range proofs) with the aim of reducing the prove generation time. Moreover, it opens the door to efficient realizations of many applications in the collaborative setting such as mutually exclusive prover groups, combining collaborative and single-party proofs and efficiently implementing publicly auditable MPC (PA-MPC). We present the first, general definition for collaborative commit-and-prove NIZK (CP-NIZK) proofs of knowledge and construct distributed protocols to enable their realization. We implement our protocols for two commonly used NIZKs, Groth16 and Bulletproofs, and evaluate their practicality in a variety of computational settings. Our findings indicate that composability adds only minor overhead, especially for large circuits. We experimented with our construction in an application setting, and when compared to prior works, our protocols reduce latency by 18-55x while requiring only a fraction (0.2%) of the communication.

  匹配依据：MPC: mpc (context)

  </details>

- **Privacy-Preserving Hierarchical Model-Distributed Inference**
  2024-07-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.18353)
  Fatemeh Jafarian Dehkordi, Yasaman Keshtkarjahromi, Hulya Seferoglu

  <details><summary>摘要 / Abstract</summary>

  This paper focuses on designing a privacy-preserving Machine Learning (ML) inference protocol for a hierarchical setup, where clients own/generate data, model owners (cloud servers) have a pre-trained ML model, and edge servers perform ML inference on clients&#x27; data using the cloud server&#x27;s ML model. Our goal is to speed up ML inference while providing privacy to both data and the ML model. Our approach (i) uses model-distributed inference (model parallelization) at the edge servers and (ii) reduces the amount of communication to/from the cloud server. Our privacy-preserving hierarchical model-distributed inference, privateMDI design uses additive secret sharing and linearly homomorphic encryption to handle linear calculations in the ML inference, and garbled circuit and a novel three-party oblivious transfer are used to handle non-linear functions. privateMDI consists of offline and online phases. We designed these phases in a way that most of the data exchange is done in the offline phase while the communication overhead of the online phase is reduced. In particular, there is no communication to/from the cloud server in the online phase, and the amount of communication between the client and edge servers is minimized. The experimental results demonstrate that privateMDI significantly reduces the ML inference time as compared to the baselines.

  匹配依据：MPC: garbled circuit, oblivious transfer, secret sharing

  </details>

- **Privacy Threats and Countermeasures in Federated Learning for Internet of Things: A Systematic Review**
  2024-07-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.18096)
  Adel ElZemity, Budi Arief

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) in the Internet of Things (IoT) environments can enhance machine learning by utilising decentralised data, but at the same time, it might introduce significant privacy and security concerns due to the constrained nature of IoT devices. This represents a research challenge that we aim to address in this paper. We systematically analysed recent literature to identify privacy threats in FL within IoT environments, and evaluate the defensive measures that can be employed to mitigate these threats. Using a Systematic Literature Review (SLR) approach, we searched five publication databases (Scopus, IEEE Xplore, Wiley, ACM, and Science Direct), collating relevant papers published between 2017 and April 2024, a period which spans from the introduction of FL until now. Guided by the PRISMA protocol, we selected 49 papers to focus our systematic review on. We analysed these papers, paying special attention to the privacy threats and defensive measures -- specifically within the context of IoT -- using inclusion and exclusion criteria tailored to highlight recent advances and critical insights. We identified various privacy threats, including inference attacks, poisoning attacks, and eavesdropping, along with defensive measures such as Differential Privacy and Secure Multi-Party Computation. These defences were evaluated for their effectiveness in protecting privacy without compromising the functional integrity of FL in IoT settings. Our review underscores the necessity for robust and efficient privacy-preserving strategies tailored for IoT environments. Notably, there is a need for strategies against replay, evasion, and model stealing attacks. Exploring lightweight defensive measures and emerging technologies such as blockchain may help improve the privacy of FL in IoT, leading to the creation of FL models that can operate under variable network conditions.

  匹配依据：MPC: secure multi party computation

  </details>

- **Depth-Aware Arithmetization of Common Primitives in Prime Fields**
  2024-07-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1200)
  Jelle Vos, Mauro Conti, Zekeriya Erkin

  <details><summary>摘要 / Abstract</summary>

  A common misconception is that the computational abilities of circuits composed of additions and multiplications are restricted to simple formulas only. Such arithmetic circuits over finite fields are actually capable of computing any function, including equality checks, comparisons, and other highly non-linear operations. While all those functions are computable, the challenge lies in computing them efficiently. We refer to this search problem as arithmetization. Arithmetization is a key problem in secure computation, as techniques like homomorphic encryption and secret sharing compute arithmetic circuits rather than the high-level programs that programmers are used to. The objective in arithmetization has typically been to minimize the number of multiplications (multiplicative size), as multiplications in most secure computation techniques are significantly more expensive to compute than additions. However, the multiplicative depth of a circuit arguably plays an even more important role in deciding the computational cost: For homomorphic encryption, it strongly affects the choice of cryptographic parameters and the number of bootstrapping operations required, which are orders of magnitude more expensive to compute than multiplications. In fact, if we can limit the multiplicative depth of a circuit such that we do not need to perform any bootstrapping, we can omit the large bootstrapping keys required to perform them all together. We argue that arithmetization should be treated as a multi-objective minimization problem, in which a trade-off can be made between a circuit&#x27;s multiplicative size and depth. We present efficient depth-aware arithmetization methods for many primitive operations such as exponentiation, univariate functions, equality checks, comparisons, and ANDs and ORs, which take into account that squaring can be cheaper than arbitrary multiplications, and we study how to compose them.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Low-Latency Privacy-Preserving Deep Learning Design via Secure MPC**
  2024-07-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.18982)
  Ke Lin, Yasir Glani, Ping Luo

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) facilitates privacy-preserving computation between multiple parties without leaking private information. While most secure deep learning techniques utilize MPC operations to achieve feasible privacy-preserving machine learning on downstream tasks, the overhead of the computation and communication still hampers their practical application. This work proposes a low-latency secret-sharing-based MPC design that reduces unnecessary communication rounds during the execution of MPC protocols. We also present a method for improving the computation of commonly used nonlinear functions in deep learning by integrating multivariate multiplication and coalescing different packets into one to maximize network utilization. Our experimental results indicate that our method is effective in a variety of settings, with a speedup in communication latency of $10\sim20\%$.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Source-independent quantum secret sharing with entangled photon pair networks**
  2024-07-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.16462)
  Yi-Ran Xiao, Zhao-Ying Jia, Yu-Chen Song, Yu Bao, Yao Fu, Hua-Lei Yin, Zeng-Bing Chen

  <details><summary>摘要 / Abstract</summary>

  The large-scale deployment of quantum secret sharing (QSS) in quantum networks is currently challenging due to the requirements for the generation and distribution of multipartite entanglement states. Here we present an efficient source-independent QSS protocol utilizing entangled photon pairs in quantum networks. Through the post-matching method, which means the measurement events in the same basis are matched, the key rate is almost independent of the number of participants. In addition, the unconditional security of our QSS against internal and external eavesdroppers can be proved by introducing an equivalent virtual protocol. Our protocol has great performance and technical advantages in future quantum networks.

  匹配依据：MPC: secret sharing

  </details>

- **Language-Based Security for Low-Level MPC**
  2024-07-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.16504)
  Christian Skalka, Joseph P. Near

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation (MPC) is an important enabling technology for data privacy in modern distributed applications. Currently, proof methods for low-level MPC protocols are primarily manual and thus tedious and error-prone, and are also non-standardized and unfamiliar to most PL theorists. As a step towards better language support and language-based enforcement, we develop a new staged PL for defining a variety of low-level probabilistic MPC protocols. We also formulate a collection of confidentiality and integrity hyperproperties for our language model that are familiar from information flow, including conditional noninterference, gradual release, and robust declassification. We demonstrate their relation to standard MPC threat models of passive and malicious security, and how they can be leveraged in security verification of protocols. To prove these properties we develop automated tactics in $\mathbb{F}_2$ that can be integrated with separation logic-style reasoning.

  匹配依据：MPC: secure multi party computation

  </details>

- **Efficient Two-Party Secure Aggregation via Incremental Distributed Point Function**
  2024-07-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1190)
  Nan Cheng, Aikaterini Mitrokotsa, Feng Zhang, Frank Hartmann

  <details><summary>摘要 / Abstract</summary>

  Computing the maximum from a list of secret inputs is a widely-used functionality that is employed ei- ther indirectly as a building block in secure computation frameworks, such as ABY (NDSS’15) or directly used in multiple applications that solve optimisation problems, such as secure machine learning or secure aggregation statistics. Incremental distributed point function (I-DPF) is a powerful primitive (IEEE S&amp;P’21) that significantly reduces the client- to-server communication and are employed to efficiently and securely compute aggregation statistics. In this paper, we investigate whether I-DPF can be used to improve the efficiency of secure two-party computation (2PC) with an emphasis on computing the maximum value and the k-th (with k unknown to the computing parties) ranked value from a list of secret inputs. Our answer is affir- mative, and we propose novel secure 2PC protocols that use I-DPF as a building block, resulting in significant efficiency gains compared to the state-of-the-art. More precisely, our contributions are: (i) We present two new secure computa- tion frameworks that efficiently compute secure aggregation statistics bit-wisely or batch-wisely; (ii) we propose novel protocols to compute the maximum value, the k-th ranked value from a list of secret inputs; (iii) we provide variations of the proposed protocols that can perform batch computations and thus provide further efficiency improvements; and (iv) we provide an extensive performance evaluation for all proposed protocols. Our protocols have a communication complexity that is independent of the number of secret inputs and linear to the length of the secret input domain. Our experimental re- sults show enhanced efficiency over state-of-the-art solutions, particularly notable when handling large-scale inputs. For instance, in scenarios involving an input set of five million elements with an input domain size of 31 bits, our protocol ΠMax achieves an 18% reduction in online execution time and a 67% decrease in communication volume compared to the most efficient existing solution.

  匹配依据：MPC: secure computation, secure two party computation

  </details>

- **Updatable Private Set Intersection from Structured Encryption**
  2024-07-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1183)
  Archita Agarwal, David Cash, Marilyn George, Seny Kamara, Tarik Moataz, Jaspal Singh

  <details><summary>摘要 / Abstract</summary>

  Many efficient custom protocols have been developed for two-party private set intersection (PSI), that allow the parties to learn the intersection of their private sets. However, these approaches do not yield efficient solutions in the dynamic setting when the parties’ sets evolve and the intersection has to be computed repeatedly. In this work we propose a new framework for this problem of updatable PSI — with elements being inserted and deleted — in the semihonest model based on structured encryption. The framework reduces the problem of updatable PSI to a new variant of structured encryption (StE) for an updatable set datatype, which may be of independent interest. Our final construction is a constant round protocol with worst-case communication and computation complexity that grows linearly in the size of the updates and only poly-logarithmically with the size of the accumulated sets. Our protocol is the first to support arbitrary inserts and deletes for updatable PSI.

  匹配依据：MPC: private set intersection

  </details>

- **Privacy-Preserving Multi-Center Differential Protein Abundance Analysis with FedProt**
  2024-07-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.15220)
  Yuliya Burankova, Miriam Abele, Mohammad Bakhtiari, Christine von Törne, Teresa Barth, Lisa Schweizer, Pieter Giesbertz, Johannes R. Schmidt, Stefan Kalkhof, Janina Müller-Deile, Peter A van Veelen, Yassene Mohammed, Elke Hammer, Lis Arend, Klaudia Adamowicz, Tanja Laske, Anne Hartebrodt, Tobias Frisch, Chen Meng, Julian Matschinske, Julian Späth, Richard Röttger, Veit Schwämmle, Stefanie M. Hauck, Stefan Lichtenthaler, Axel Imhof, Matthias Mann, Christina Ludwig, Bernhard Kuster, Jan Baumbach, Olga Zolotareva

  <details><summary>摘要 / Abstract</summary>

  Quantitative mass spectrometry has revolutionized proteomics by enabling simultaneous quantification of thousands of proteins. Pooling patient-derived data from multiple institutions enhances statistical power but raises significant privacy concerns. Here we introduce FedProt, the first privacy-preserving tool for collaborative differential protein abundance analysis of distributed data, which utilizes federated learning and additive secret sharing. In the absence of a multicenter patient-derived dataset for evaluation, we created two, one at five centers from LFQ E.coli experiments and one at three centers from TMT human serum. Evaluations using these datasets confirm that FedProt achieves accuracy equivalent to DEqMS applied to pooled data, with completely negligible absolute differences no greater than $\text{$4 \times 10^{-12}$}$. In contrast, -log10(p-values) computed by the most accurate meta-analysis methods diverged from the centralized analysis results by up to 25-27. FedProt is available as a web tool with detailed documentation as a FeatureCloud App.

  匹配依据：MPC: secret sharing

  </details>

- **Relationships among FuncCPA and Its Related Notions**
  2024-07-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/1166)
  Takumi Shinozaki, Tatsuaki Okamoto, Keisuke Takana, Masayuki Tezuka, Yusuke Yoshida

  <details><summary>摘要 / Abstract</summary>

  Akavia, Gentry, Halevi, and Vald (TCC’22, JoC&#x27;25) introduced the security notion of function-chosen-plaintext-attack ($\mathsf{FuncCPA}$ security) for public-key encryption schemes. $\mathsf{FuncCPA}$ is deﬁned by adding a functional re-encryption oracle to the $\mathsf{IND}$-$\mathsf{CPA}$ game. This notion is crucial for secure computation applications where the server is allowed to delegate a part of the computation to the client. Dodis, Halevi, and Wichs (TCC’23) introduced a stronger variant called $\mathsf{FuncCPA^+}$, and conjectured that $\mathsf{FuncCPA^+}$ is strictly stronger than $\mathsf{FuncCPA}$, while they showed $\mathsf{FuncCPA^+}$ implies $\mathsf{FuncCPA}$. Seeking insights into this conjecture, they showed that $\mathsf{ReEncCPA^+}$ is strictly stronger than $\mathsf{ReEncCPA}$, where $\mathsf{ReEncCPA}$ and $\mathsf{ReEncCPA^+}$ are restricted versions of $\mathsf{FuncCPA}$ and $\mathsf{FuncCPA^+}$ respectively. In this paper, contrary to their conjecture, we show that $\mathsf{FuncCPA^+}$ is equivalent to $\mathsf{FuncCPA}$. We also introduce new variants of $\mathsf{FuncCPA}$; $\mathsf{WeakFuncCPA}$, $\mathsf{OW}$-$\mathsf{FuncCPA}$, and $\mathsf{OW}$-$\mathsf{WeakFuncCPA}$. $\mathsf{WeakFuncCPA}$ is a restricted variant of $\mathsf{FuncCPA}$ in that an oracle query is prohibited after the challenge query (like $\mathsf{IND}$-$\mathsf{CCA1}$). $\mathsf{OW}$-$\mathsf{FuncCPA}$ and $\mathsf{OW}$-$\mathsf{WeakFuncCPA}$ are the one-way ($\mathsf{OW}$) versions of $\mathsf{FuncCPA}$ and $\mathsf{WeakFuncCPA}$, respectively. This paper shows that $\mathsf{WeakFuncCPA}$ and $\mathsf{OW}$-$\mathsf{FuncCPA}$ are equivalent to $\mathsf{FuncCPA}$, that is, all of $\mathsf{FuncCPA}$, $\mathsf{FuncCPA^+}$, $\mathsf{WeakFuncCPA}$, and $\mathsf{OW}$-$\mathsf{FuncCPA}$ are equivalent. Considering the separation of $\mathsf{IND}$-$\mathsf{CCA1}$ and $\mathsf{IND}$-$\mathsf{CCA2}$, and that of $\mathsf{OW}$-$\mathsf{CPA}$ and $\mathsf{IND}$-$\mathsf{CPA}$, these results are surprising. To show the equivalence, we develop novel techniques to utilize functional re-encryption oracles. We then provide the separation results that $\mathsf{OW}$-$\mathsf{WeakFuncCPA}$ does not imply $\mathsf{FuncCPA}$ and $\mathsf{ReEncCPA^+}$ does not imply $\mathsf{FuncCPA}$.

  匹配依据：MPC: secure computation

  </details>
