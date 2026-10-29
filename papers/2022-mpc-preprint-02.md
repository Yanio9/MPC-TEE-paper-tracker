# 2022 · MPC · 仅预印本来源 · 第 2/4 页

[总目录](../PAPERS.md) · [上一页](2022-mpc-preprint-01.md) · [下一页](2022-mpc-preprint-03.md)

- **SEEK: model extraction attack against hybrid secure inference protocols**
  2022-09-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2209.06373) · [IACR ePrint](https://eprint.iacr.org/2022/1200)
  Si Chen, Junfeng Fan

  <details><summary>摘要 / Abstract</summary>

  Security concerns about a machine learning model used in a prediction-as-a-service include the privacy of the model, the query and the result. Secure inference solutions based on homomorphic encryption (HE) and/or multiparty computation (MPC) have been developed to protect all the sensitive information. One of the most efficient type of solution utilizes HE for linear layers, and MPC for non-linear layers. However, for such hybrid protocols with semi-honest security, an adversary can malleate the intermediate features in the inference process, and extract model information more effectively than methods against inference service in plaintext. In this paper, we propose SEEK, a general extraction method for hybrid secure inference services outputing only class labels. This method can extract each layer of the target model independently, and is not affected by the depth of the model. For ResNet-18, SEEK can extract a parameter with less than 50 queries on average, with average error less than $0.03\%$.

  匹配依据：MPC: multiparty computation

  </details>

- **On the Field-Based Division Property: Applications to MiMC, Feistel MiMC and GMiMC (Full Version)**
  2022-09-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1210)
  Jiamin Cui, Kai Hu, Meiqin Wang, Puwen Wei

  <details><summary>摘要 / Abstract</summary>

  Recent practical applications using advanced cryptographic protocols such as multi-party computations (MPC) and zero-knowledge proofs (ZKP) have prompted a range of novel symmetric primitives described over large finite fields, characterized as arithmetization-oriented AO ciphers. Such designs, aiming to minimize the number of multiplications over fields, have a high risk of being vulnerable to algebraic attacks, especially to the higher-order differential attack. Thus, it is significant to carefully evaluate the growth of their algebraic degree. However, the degree estimation for AO ciphers has been a challenge for cryptanalysts due to the lack of general and accurate methods. In this paper, we extend the division property, a state-of-the-art framework for finding the upper bound of the algebraic degree over binary fields, to the scope of $\mathbb{F}_{2^n}$. It is a generic method to detect the algebraic degree for AO ciphers, even applicable to Feistel ciphers which have no better bounds than the trivial exponential one. In this general division property, our idea is to evaluate whether the polynomial representation of a block cipher contains some specific monomials. With a deep investigation of the arithmetical feature, we introduce the propagation rules of monomials for field-based operations, which can be efficiently modeled using the bit-vector theory of SMT. Then the new searching tool for degree estimation can be constructed due to the relationship between the algebraic degree and the exponents of monomials. We apply our new framework to some important AO ciphers, including Feistel MiMC, GMiMC, and MiMC. For Feistel MiMC, we show that the algebraic degree grows significantly slower than the native exponential bound. For the first time, we present a secret-key higher-order differential distinguisher for up to 124 rounds, much better than the 83-round distinguisher for Feistel MiMC permutation proposed at CRYPTO 2020. We also exhibit a full-round zero-sum distinguisher with a data complexity of $2^{251}$. Our method can be further extended for the general Feistel structure with more branches and exhibit higher-order differential distinguishers against the practical instance of GMiMC for up to 50 rounds. For MiMC in SP-networks, our results correspond to the exact algebraic degree proved by Bouvier et al. We also point out that the number of rounds in MiMC&#x27;s specification is not sufficient to guarantee the security against the higher-order differential attack for MiMC-like schemes with different exponents. The investigation of different exponents provides some guidance on the cipher design.

  匹配依据：MPC: mpc (context)

  </details>

- **Notes on Reusable Garbling**
  2022-09-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1208)
  Hu Yupu, Dong Siyue, Wang Baocang, Liu Jun

  <details><summary>摘要 / Abstract</summary>

  Garbling is a cryptographic primitive which has many applications. It is mainly used for scenes of limited authority, such as multi-party computation (MPC), attribute-based encryption (ABE), functional encryption (FE), indistinguishability obfuscation (IO), etc. Garbling schemes before 2013 are of one-time garbling. Goldwasser et al and Agrawal presented a reusable garbling scheme, which made use of a symmetric encryption scheme and an FE scheme as the components. In this paper we discuss the validity and the efficiency of reusable garbling scheme. We present the following three notes on the scheme. (1) Reusable garbling scheme does not provide new applications, and it is still a one-time garbling scheme. (2) Even reusable garbling scheme is taken as a one-time garbling scheme, sometimes it is not usable. More detailedly, it can only be used for Basic Scene 2, and cannot be used for Basic Scene 1. For example, it cannot be used for MPC. (3) Even reusable garbling scheme is taken as a one-time garbling scheme used for Basic Scene 2, there is no evidence to show that its efficiency is better than a former one-time garbling scheme.

  匹配依据：MPC: garbling scheme, garbling schemes, multi party computation

  </details>

- **Attaining GOD Beyond Honest Majority With Friends and Foes**
  2022-09-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1207)
  Aditya Hegde, Nishat Koti, Varsha Bhat Kukkala, Shravani Patil, Arpita Patra, Protik Paul

  <details><summary>摘要 / Abstract</summary>

  In the classical notion of multiparty computation (MPC), an honest party learning private inputs of others, either as a part of protocol specification or due to a malicious party&#x27;s unspecified messages, is not considered a potential breach. Several works in the literature exploit this seemingly minor loophole to achieve the strongest security of guaranteed output delivery via a trusted third party, which nullifies the purpose of MPC. Alon et al. (CRYPTO 2020) presented the notion of Friends and Foes ($\mathtt{FaF}$) security, which accounts for such undesired leakage towards honest parties by modelling them as semi-honest (friends) who do not collude with malicious parties (foes). With real-world applications in mind, it&#x27;s more realistic to assume parties are semi-honest rather than completely honest, hence it is imperative to design efficient protocols conforming to the $\mathtt{FaF}$ security model. Our contributions are not only motivated by the practical viewpoint, but also consider the theoretical aspects of $\mathtt{FaF}$ security. We prove the necessity of semi-honest oblivious transfer for $\mathtt{FaF}$-secure protocols with optimal resiliency. On the practical side, we present QuadSquad, a ring-based 4PC protocol, which achieves fairness and GOD in the $\mathtt{FaF}$ model, with an optimal corruption of $1$ malicious and $1$ semi-honest party. QuadSquad is, to the best of our knowledge, the first practically efficient $\mathtt{FaF}$ secure protocol with optimal resiliency. Its performance is comparable to the state-of-the-art dishonest majority protocols while improving the security guarantee from abort to fairness and GOD. Further, QuadSquad elevates the security by tackling a stronger adversarial model over the state-of-the-art honest-majority protocols, while offering a comparable performance for the input-dependent computation. We corroborate these claims by benchmarking the performance of QuadSquad. We also consider the application of liquidity matching that deals with highly sensitive financial transaction data, where $\mathtt{FaF}$ security is apt. We design a range of $\mathtt{FaF}$ secure building blocks to securely realize liquidity matching as well as other popular applications such as privacy-preserving machine learning (PPML). Inclusion of these blocks makes QuadSquad a comprehensive framework.

  匹配依据：MPC: multiparty computation, oblivious transfer

  </details>

- **Knowledge Encryption and Its Applications to Simulatable Protocols With Low Round-Complexity**
  2022-09-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1193)
  Yi Deng, Xinxuan Zhang

  <details><summary>摘要 / Abstract</summary>

  We introduce a new notion of public key encryption, knowledge encryption, for which its ciphertexts can be reduced to the public-key, i.e., any algorithm that can break the ciphertext indistinguishability can be used to extract the (partial) secret key. We show that knowledge encryption can be built solely on any two-round oblivious transfer with game-based security, which are known based on various standard (polynomial-hardness) assumptions, such as the DDH, the Quadratic($N^{th}$) Residuosity or the LWE assumption. We use knowledge encryption to construct the first three-round (weakly) simulatable oblivious transfer. This protocol satisfies (fully) simulatable security for the receiver, and weakly simulatable security ($(T, \epsilon)$-simulatability) for the sender in the following sense: for any polynomial $T$ and any inverse polynomial $\epsilon$, there exists an efficient simulator such that the distinguishing gap of any distinguisher of size less than $T$ is at most $\epsilon$. Equipped with these tools, we construct a variety of fundamental cryptographic protocols with low round-complexity, assuming only the existence of two-round oblivious transfer with game-based security. These protocols include three-round delayed-input weak zero knowledge argument, three-round weakly secure two-party computation, three-round concurrent weak zero knowledge in the BPK model, and a two-round commitment with weak security under selective opening attack. These results improve upon the assumptions required by the previous constructions. Furthermore, all our protocols enjoy the above $(T, \epsilon)$-simulatability (stronger than the distinguisher-dependent simulatability), and are quasi-polynomial time simulatable under the same (polynomial hardness) assumption.

  匹配依据：MPC: oblivious transfer, secure two party computation

  </details>

- **Post-Quantum Oblivious Transfer from Smooth Projective Hash Functions with Grey Zone**
  2022-09-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2209.04149)
  Slim Bettaieb, Loïc Bidoux, Olivier Blazy, Baptiste Cottier, David Pointcheval

  <details><summary>摘要 / Abstract</summary>

  Oblivious Transfer (OT) is a major primitive for secure multiparty computation. Indeed, combined with symmetric primitives along with garbled circuits, it allows any secure function evaluation between two parties. In this paper, we propose a new approach to build OT protocols. Interestingly, our new paradigm features a security analysis in the Universal Composability (UC) framework and may be instantiated from post-quantum primitives. In order to do so, we define a new primitive named Smooth Projective Hash Function with Grey Zone (SPHFwGZ) which can be seen as a relaxation of the classical Smooth Projective Hash Functions, with a subset of the words for which one cannot claim correctness nor smoothness: the grey zone. As a concrete application, we provide two instantiations of SPHFwGZ respectively based on the Diffie-Hellman and the Learning With Errors (LWE) problems. Hence, we propose a quantum-resistant OT protocol with UC-security in the random oracle model.

  匹配依据：MPC: garbled circuits, oblivious transfer, secure function evaluation, secure multiparty computation

  </details>

- **PEA: Practical private epistasis analysis using MPC**
  2022-09-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1185)
  Kay Hamacher, Tobias Kussel, Thomas Schneider, Oleksandr Tkachenko

  <details><summary>摘要 / Abstract</summary>

  Due to the significant drop in prices for genome sequencing in the last decade, genome databases were constantly growing. This enabled genome analyses such as Genome-Wide Association Studies (GWAS) that study associations between a gene and a disease and allow to improve medical treatment. However, GWAS fails at the analysis of complex diseases caused by non-linear gene-gene interactions such as sporadic breast cancer or type 2 diabetes. Epistasis Analysis (EA) is a more powerful approach that complements GWAS and considers non-linear interactions between multiple parts of the genome and environment. Statistical genome analyses require large, well-curated genomic datasets, which are difficult to obtain. Hence, the aggregation of multiple databases is often necessary, but the sharing of genomic data raises severe privacy concerns and is subject to extensive regulations (e.g., GDPR or HIPAA), requiring further privacy protection for collaborative analyses. Although there has been work on private GWAS, there was a lack of attention to Private EA (PEA). In this work, we design the first secure and accurate PEA protocol, with security against passive adversaries. Our efficient PEA protocol consists of two subprotocols: (1) (optional) feature selection for filtering noisy features to reduce the input size for better efficiency and (2) finding relevant associations. For feature selection, we design two protocols based on Secure Multi-Party Computation (MPC) for Relief-F and TuRF. For finding associations, we design an MPC protocol for Multifactor Dimensionality Reduction (MDR). Our private MDR protocol is based on two novel, efficient building blocks, arithmetic greater than and arithmetic swap, which may be of independent interest. This approach omits the need for expensive conversions between sharing types in private MDR and reduces the communication by two orders of magnitude compared to a naïve design using garbled circuits. Our private MDR protocol runs in (extrapolated) three days on a practical database with 10,000 features for all two mutually combined features, i.e., considering about 50 million combinations.

  匹配依据：MPC: garbled circuits, secure multi party computation

  </details>

- **On the computational hardness needed for quantum cryptography**
  2022-09-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2209.04101) · [IACR ePrint](https://eprint.iacr.org/2022/1181)
  Zvika Brakerski, Ran Canetti, Luowen Qian

  <details><summary>摘要 / Abstract</summary>

  In the classical model of computation, it is well established that one-way functions (OWF) are minimal for computational cryptography: They are essential for almost any cryptographic application that cannot be realized with respect to computationally unbounded adversaries. In the quantum setting, however, OWFs appear not to be essential (Kretschmer 2021; Ananth et al., Morimae and Yamakawa 2022), and the question of whether such a minimal primitive exists remains open. We consider EFI pairs -- efficiently samplable, statistically far but computationally indistinguishable pairs of (mixed) quantum states. Building on the work of Yan (2022), which shows equivalence between EFI pairs and statistical commitment schemes, we show that EFI pairs are necessary for a large class of quantum-cryptographic applications. Specifically, we construct EFI pairs from minimalistic versions of commitments schemes, oblivious transfer, and general secure multiparty computation, as well as from $\mathsf{QCZK}$ proofs from essentially any non-trivial language. We also construct quantum computational zero knowledge ($\mathsf{QCZK}$) proofs for all of $\mathsf{QIP}$ from any EFI pair. This suggests that, for much of quantum cryptography, EFI pairs play a similar role to that played by OWFs in the classical setting: they are simple to describe, essential, and also serve as a linchpin for demonstrating equivalence between primitives.

  匹配依据：MPC: oblivious transfer, secure multiparty computation

  </details>

- **Multisecret-sharing scheme with two-level security and its applications in Blockchain**
  2022-09-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2209.03670)
  R. K. Sharma, Ritumoni Sarma, Neha Arora, Vidya Sagar

  <details><summary>摘要 / Abstract</summary>

  A $(t,m)$-threshold secret sharing and multisecret-sharing scheme based on Shamir&#x27;s SSS are introduced with two-level security using a one-way function. Besides we give its application in smart contract-enabled consortium blockchain network. The proposed scheme is thoroughly examined in terms of security and efficiency. Privacy, security, integrity, and scalability are also analyzed while applying it to the blockchain network.

  匹配依据：MPC: secret sharing

  </details>

- **Cryptography with Certified Deletion**
  2022-09-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.01754) · [IACR ePrint](https://eprint.iacr.org/2022/1178)
  James Bartusek, Dakshita Khurana

  <details><summary>摘要 / Abstract</summary>

  We propose a new, unifying framework that yields an array of cryptographic primitives with certified deletion. These primitives enable a party in possession of a quantum ciphertext to generate a classical certificate that the encrypted plaintext has been information-theoretically deleted, and cannot be recovered even given unbounded computational resources. - For X \in {public-key, attribute-based, fully-homomorphic, witness, timed-release}, our compiler converts any (post-quantum) X encryption to X encryption with certified deletion. In addition, we compile statistically-binding commitments to statistically-binding commitments with certified everlasting hiding. As a corollary, we also obtain statistically-sound zero-knowledge proofs for QMA with certified everlasting zero-knowledge assuming statistically-binding commitments. - We also obtain a strong form of everlasting security for two-party and multi-party computation in the dishonest majority setting. While simultaneously achieving everlasting security against all parties in this setting is known to be impossible, we introduce everlasting security transfer (EST). This enables any one party (or a subset of parties) to dynamically and certifiably information-theoretically delete other participants&#x27; data after protocol execution. We construct general-purpose secure computation with EST assuming statistically-binding commitments, which can be based on one-way functions or pseudorandom quantum states. We obtain our results by developing a novel proof technique to argue that a bit b has been information-theoretically deleted from an adversary&#x27;s view once they output a valid deletion certificate, despite having been previously information-theoretically determined by the ciphertext they held in their view. This technique may be of independent interest.

  匹配依据：MPC: multi party computation, secure computation

  </details>

- **Explicit Low-Bandwidth Evaluation Schemes for Weighted Sums of Reed-Solomon-Coded Symbols**
  2022-09-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2209.03251)
  Han Mao Kiah, Wilton Kim, Stanislav Kruglik, San Ling, Huaxiong Wang

  <details><summary>摘要 / Abstract</summary>

  Motivated by applications in distributed storage, distributed computing, and homomorphic secret sharing, we study communication-efficient schemes for computing linear combinations of coded symbols. Specifically, we design low-bandwidth schemes that evaluate the weighted sum of $\ell$ coded symbols in a codeword $\pmb{c}\in\mathbb{F}^n$, when we are given access to $d$ of the remaining components in $\pmb{c}$. Formally, suppose that $\mathbb{F}$ is a field extension of $\mathbb{B}$ of degree $t$. Let $\pmb{c}$ be a codeword in a Reed-Solomon code of dimension $k$ and our task is to compute the weighted sum of $\ell$ coded symbols. In this paper, for some $s&lt;t$, we provide an explicit scheme that performs this task by downloading $d(t-s)$ sub-symbols in $\mathbb{B}$ from $d$ available nodes, whenever $d\geq \ell|\mathbb{B}|^s-\ell+k$. In many cases, our scheme outperforms previous schemes in the literature. Furthermore, we provide a characterization of evaluation schemes for general linear codes. Then in the special case of Reed-Solomon codes, we use this characterization to derive a lower bound for the evaluation bandwidth.

  匹配依据：MPC: secret sharing

  </details>

- **DyCAPS: Asynchronous Dynamic-committee Proactive Secret Sharing**
  2022-09-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1169)
  Bin Hu, Zongyang Zhang, Han Chen, You Zhou, Huazu Jiang, Jianwei Liu

  <details><summary>摘要 / Abstract</summary>

  Dynamic-committee proactive secret sharing (DPSS) enables the refresh of secret shares and the alternation of shareholders without changing the secret. Such a proactivization functionality makes DPSS a promising technology for long-term key management and committee governance. In non-asynchronous networks, CHURP (CCS ’19) and COBRA (S&amp;P ’22) have achieved best-case square and cubic communication cost, respectively, w.r.t. the number of shareholders. However, the overhead of asynchronous DPSS remains high. This gap hinders asynchronous protocols from evolving to the dynamic setting, such as BFT systems and threshold cryptography services. In this paper, we fill this gap and propose DyCAPS, an efficient asynchronous DPSS protocol with a cubic communication cost. DyCAPS supports the transfer of both low- and high-threshold secret shares among dynamic committees with the same communication and computation complexity. Experimental results show that proactivization between two disjoint committees of 4 (resp., 64) members takes 1.3 (resp., 51) seconds. Moreover, DyCAPS is designed to be compatible with asynchronous BFT protocols without increasing the asymptotic communication cost. Given a payload of 5–10 MB per node, DyCAPS achieves member change in Dumbo2 (CCS ’20) at around 10% temporary throughput degradation, with the committee size varying from 4 to 22.

  匹配依据：MPC: secret sharing

  </details>

- **A MUSE view of the massive merging galaxy cluster ACT-CL J0102-4915 (El Gordo) at z = 0.87: robust strong lensing model and data release**
  2022-09-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2209.02718)
  G. B. Caminha, C. Grillo, P. Rosati, A. Liu, A. Acebron, P. Bergamini, K. I. Caputi, A. Mercurio, P. Tozzi, E. Vanzella, R. Demarco, B. Frye, G. Rosani, K. Sharon

  <details><summary>摘要 / Abstract</summary>

  We present a detailed strong lensing analysis of the massive and distant ($z=0.870$) galaxy cluster ACT-CL J0102$-$4915 (ACT0102, also known as El Gordo), taking advantage of new spectroscopic data from the Multi Unit Spectroscopic Explorer (MUSE) on the Very Large Telescope, and archival imaging from the Hubble Space Telescope. Thanks to the MUSE data, we measure secure redshifts for 374 single objects, including 23 multiply lensed galaxies, and 167 cluster members of ACT0102. The observed positions of 56 multiple images, along with their new spectroscopic redshift measurements, are used as constraints for our strong lensing model. Remarkably, some multiple images are detected out to a large projected distance of $\approx 1$ Mpc from the brightest cluster galaxy, allowing us to estimate a projected total mass value of $1.84_{-0.04}^{+0.03} \times 10^{15}\, \rm M_{\odot}$ within that radius. We find that we need two extended cluster mass components, the mass contributions from the cluster members and the additional lensing effect of a foreground ($z=0.633$) group of galaxies, to predict the positions of all multiple images with a root mean square offset of $0.75&quot;$. The main cluster-scale mass component is centered very closely to the brightest cluster galaxy and the other extended mass component is located in the north-west region of the cluster. These two mass components have very similar values of mass projected within 300 kpc from their centers, namely $2.29_{-0.10}^{+0.09}\times10^{14}\,\rm M_{\odot}$ and $2.10_{-0.09}^{+0.08}\times10^{14}\,\rm M_{\odot}$, in agreement with the major merging scenario of ACT0102. We make publicly available the lens model, including the magnification maps and posterior distributions of the model parameter values, as well as the full spectroscopic catalogue containing all redshift measurements obtained with MUSE.

  匹配依据：MPC: mpc (context)

  </details>

- **Private Simultaneous Messages Based on Quadratic Residues**
  2022-09-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2209.01859)
  Kazumasa Shinagawa, Reo Eriguchi, Shohei Satake, Koji Nuida

  <details><summary>摘要 / Abstract</summary>

  Private Simultaneous Messages (PSM) model is a minimal model for secure multiparty computation. Feige, Kilian, and Naor (STOC 1994) and Ishai (Cryptology and Information Security Series 2013) constructed PSM protocols based on quadratic residues. In this paper, we define QR-PSM protocols as a generalization of these protocols. A QR-PSM protocol is a PSM protocol whose decoding function outputs the quadratic residuosity of what is computed from messages. We design a QR-PSM protocol for any symmetric function $f: \{0,1\}^n \rightarrow \{0,1\}$ of communication complexity $O(n^2)$. As far as we know, it is the most efficient PSM protocol since the previously known best PSM protocol was of $O(n^2\log n)$ (Beimel et al., CRYPTO 2014). We also study the sizes of the underlying finite fields $\mathbb{F}_p$ in the protocols since the communication complexity of a QR-PSM protocol is proportional to the bit length of the prime $p$. In particular, we show that the $N$-th Peralta prime $P_N$, which is used for general QR-PSM protocols, can be taken as at most $(1+o(1))N^2 2^{2N-2}$, which improves the Peralta&#x27;s known result (Mathematics of Computation 1992) by a constant factor $(1+\sqrt{2})^2$.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Hawk: Module LIP makes Lattice Signatures Fast, Compact and Simple**
  2022-09-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1155)
  Léo Ducas, Eamonn W. Postlethwaite, Ludo N. Pulles, Wessel van Woerden

  <details><summary>摘要 / Abstract</summary>

  We propose the signature scheme Hawk, a concrete instantiation of proposals to use the Lattice Isomorphism Problem (LIP) as a foundation for cryptography that focuses on simplicity. This simplicity stems from LIP, which allows the use of lattices such as $\mathbb{Z}^n$ , leading to signature algorithms with no floats, no rejection sampling, and compact precomputed distributions. Such design features are desirable for constrained devices, and when computing signatures inside FHE or MPC. The most significant change from recent LIP proposals is the use of module lattices, reusing algorithms and ideas from NTRUSign and Falcon. Its simplicity makes Hawk competitive. We provide cryptanalysis with experimental evidence for the design of Hawk and implement two parameter sets, Hawk-512 and Hawk-1024. Signing using Hawk-512 and Hawk-1024 is four times faster than Falcon on x86 architectures, produces signatures that are about 15% more compact, and is slightly more secure against forgeries by lattice reduction attacks. When floating-points are unavailable, Hawk signs 15 times faster than Falcon. We provide a worst case to average case reduction for module LIP. For certain parametrisations of Hawk this applies to secret key recovery and we reduce signature forgery in the random oracle model to a new problem called the one more short vector problem.

  匹配依据：MPC: mpc (context)

  </details>

- **Quantum Advantage of Threshold Changeable Secret Sharing Scheme**
  2022-09-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2209.01365)
  Xiaogang Cheng, Ren Guo, Changli Zhou

  <details><summary>摘要 / Abstract</summary>

  In TCSS (Threshold Changeable Secret Sharing) scheme, the threshold can be changed to deal with share leakage in the long term. But in classical TCSS, there is no guarantee that old shares are deleted even if the participated parties are honest. So, the changed threshold may not prevent an adversary from reconstructing the secret by the old shares and old threshold number of parties. We show how to tackle this problem quantum mechanically. I.e., quantum mechanically we can make the changed threshold mandatory. So, there is quantum advantage of quantum TCSS over classical TCSS.

  匹配依据：MPC: secret sharing

  </details>

- **Threshold Linearly Homomorphic Encryption on $\\mathbf{Z}/2^k\\mathbf{Z}$**
  2022-09-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1143)
  Guilhem Castagnos, Fabien Laguillaumie, Ida Tucker

  <details><summary>摘要 / Abstract</summary>

  A threshold public key encryption protocol is a public key system where the private key is distributed among $n$ different servers. It offers high security since no single server is entrusted to perform the decryption in its entirety. It is the core component of many multiparty computation protocols which involves mutually distrusting parties with common goals. It is even more useful when it is homomorphic, which means that public operations on ciphertexts translate to operations on the underlying plaintexts. In particular, Cramer, Damgård and Nielsen at Eurocrypt 2001 provided a new approach to multiparty computation from linearly homomorphic threshold encryption schemes. On the other hand, there has been recent interest in developing multiparty computations modulo $2^k$ for a certain integer $k$, that closely match data manipulated by a CPU. Multiparty computation would therefore benefit from an encryption scheme with such a message space that would support a distributed decryption. In this work, we provide the first threshold linearly homomorphic encryption whose message space is $\mathbf{Z}/2^k\mathbf{Z}$ for any $k$. It is inspired by Castagnos and Laguillaumie&#x27;s encryption scheme from RSA 2015, but works with a class group of discriminant whose factorisation is unknown. Its natural structure à la Elgamal makes it possible to distribute the decryption among servers using linear integer secret sharing, allowing any access structure for the decryption policy. Furthermore its efficiency and its flexibility on the choice of the message space make it a good candidate for applications to multiparty computation.

  匹配依据：MPC: multiparty computation, secret sharing

  </details>

- **Trading Off Privacy, Utility and Efficiency in Federated Learning**
  2022-09-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2209.00230)
  Xiaojin Zhang, Yan Kang, Kai Chen, Lixin Fan, Qiang Yang

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) enables participating parties to collaboratively build a global model with boosted utility without disclosing private data information. Appropriate protection mechanisms have to be adopted to fulfill the opposing requirements in preserving \textit{privacy} and maintaining high model \textit{utility}. In addition, it is a mandate for a federated learning system to achieve high \textit{efficiency} in order to enable large-scale model training and deployment. We propose a unified federated learning framework that reconciles horizontal and vertical federated learning. Based on this framework, we formulate and quantify the trade-offs between privacy leakage, utility loss, and efficiency reduction, which leads us to the No-Free-Lunch (NFL) theorem for the federated learning system. NFL indicates that it is unrealistic to expect an FL algorithm to simultaneously provide excellent privacy, utility, and efficiency in certain scenarios. We then analyze the lower bounds for the privacy leakage, utility loss and efficiency reduction for several widely-adopted protection mechanisms including \textit{Randomization}, \textit{Homomorphic Encryption}, \textit{Secret Sharing} and \textit{Compression}. Our analysis could serve as a guide for selecting protection parameters to meet particular requirements.

  匹配依据：MPC: secret sharing

  </details>

- **An Optimal Universal Construction for the Threshold Implementation of Bijective S-boxes**
  2022-09-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1141)
  Enrico Piccione, Samuele Andreoli, Lilya Budaghyan, Claude Carlet, Siemen Dhooghe, Svetla Nikova, George Petrides, Vincent Rijmen

  <details><summary>摘要 / Abstract</summary>

  Threshold implementation is a method based on secret sharing to secure cryptographic ciphers (and in particular S-boxes) against differential power analysis side-channel attacks which was proposed by Nikova, Rechberger, and Rijmen in 2006. Until now, threshold implementations were only constructed for specific types of functions and some small S-boxes, but no generic construction was ever presented. In this paper, we present the first universal threshold implementation with $t+2$ shares that is applicable to any bijective S-box, where $t$ is its algebraic degree (or is larger than the algebraic degree). While being universal, our construction is also optimal with respect to the number of shares, since the theoretically smallest possible number, $t+1$, is not attainable for some bijective S-boxes. Our results enable low latency secure hardware implementations without the need for additional randomness. In particular, we apply this result to find two uniform sharings of the AES S-box. The first sharing is obtained by using the threshold implementation of the inversion in $\mathbb{F}_{2^8}$ and the second by using two threshold implementations of two cubic power permutations that decompose the inversion. Area and performance figures for hardware implementations are provided.

  匹配依据：MPC: secret sharing

  </details>

- **Private Computation On Set Intersection With Sublinear Communication**
  2022-08-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1137)
  Jonas Janneck, Anselme Tueno, Jörn Kußmaul, Matthew Akram

  <details><summary>摘要 / Abstract</summary>

  In this paper, we propose a new protocol for private computation on set intersection (PCI) which is an extension of private set intersection (PSI). In PSI, each party has a private set and both want to securely compute the intersection of their sets such that only the result is revealed and nothing else. In PCI, we want to additionally apply a private computation on the result. The goal is to reveal only the result of such a secure evaluation on the intersection and nothing else. We particularly focus on a client-server setting where the server&#x27;s set is significantly larger than the client&#x27;s set and the result of the computation should be revealed only to the client. The protocol aims at a low communication overhead which is sublinear in the server&#x27;s set size. Such PSI protocols have already been realized using fully homomorphic encryption (FHE). However, they do not allow for private post-processing to enable PCI. There are also protocols enabling PCI which are in addition very fast with respect to the computational overhead. Their drawback is that they have a communication overhead which is at least linear in the larger set. We present a PSI protocol which can be used for arbitrary post-processing without creating a new protocol for every special-purpose PCI functionality. Our construction relies on the evaluation of a branching program using an FHE scheme. Using the properties of an FHE scheme, we build a non-interactive protocol with extendable functionalities. That means, we can not only securely compute the intersection but use the encrypted result to apply further computations without revealing the intersection itself. To the best of our knowledge, this results in the first PCI protocol with communication cost sublinear in the larger set. Compared to previous work, we can reduce the communication by factor 47.

  匹配依据：MPC: private set intersection, secure evaluation

  </details>

- **PentaGOD: Stepping beyond Traditional GOD with Five Parties**
  2022-08-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1118)
  Nishat Koti, Varsha Bhat Kukkala, Arpita Patra, Bhavish Raj Gopal

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) is increasingly being used to address privacy issues in various applications. The recent work of Alon et al. (CRYPTO&#x27;20) identified the shortcomings of traditional MPC and defined a Friends-and-Foes (FaF) security notion to address the same. We showcase the need for FaF security in real-world applications such as dark pools. This subsequently necessitates designing concretely efficient FaF-secure protocols. Towards this, keeping efficiency at the center stage, we design ring-based FaF-secure MPC protocols in the small-party honest-majority setting. Specifically, we provide (1,1)-FaF secure 5 party computation protocols (5PC) that consider one malicious and one semi-honest corruption and constitutes the optimal setting for attaining honest-majority. At the heart of it lies the multiplication protocol that requires a single round of communication with 8 ring elements (amortized). To facilitate having FaF-secure variants for several applications, we design a variety of building blocks optimized for our FaF setting. The practicality of the designed (1,1)-FaF secure 5PC framework is showcased by benchmarking dark pools. In the process, we also improve the efficiency and security of the dark pool protocols over the existing traditionally secure ones. This improvement is witnessed as a gain of up to $62\times$ in throughput compared to the existing ones. Finally, to demonstrate the versatility of our framework, we also benchmark popular deep neural networks.

  匹配依据：MPC: secure multiparty computation

  </details>

- **DP-PSI: Private and Secure Set Intersection**
  2022-08-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.13249)
  Jian Du, Tianxi Ji, Jamie Cui, Lei Zhang, Yufei Lu, Pu Duan

  <details><summary>摘要 / Abstract</summary>

  One way to classify private set intersection (PSI) for secure 2-party computation is whether the intersection is (a) revealed to both parties or (b) hidden from both parties while only the computing function of the matched payload is exposed. Both aim to provide cryptographic security while avoiding exposing the unmatched elements of the other. They may, however, be insufficient to achieve security and privacy in one practical scenario: when the intersection is required and the information leaked through the function&#x27;s output must be considered for legal, ethical, and competitive reasons. Two parties, such as the advertiser and the ads supplier, hold sets of users for PSI computation, for example, to reveal common users to the ads supplier in joint marketing applications. In addition to the security guarantees required by standard PSIs to secure unmatched elements, neither party is allowed to &quot;single out&quot; whether an element/user belongs to the other party or not, even though common users are required for joint advertising. This is a fascinating problem for which none of the PSI techniques have provided a solution. In light of this shortcoming, we compose differential privacy (DP) and S2PC to provide the best of both worlds and propose differentially-private PSI (DP-PSI), a new privacy model that shares PSI&#x27;s strong security protection while adhering to the GDPR&#x27;s recent formalization of the notion of excluding &quot;signaling out&quot; attacks by each party except with very low probability.

  匹配依据：MPC: private set intersection, secure 2 party computation

  </details>

- **Towards Practical Topology-Hiding Computation**
  2022-08-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1106)
  Shuaishuai Li

  <details><summary>摘要 / Abstract</summary>

  \par Topology-hiding computation (THC) enables $n$ parties to perform a secure multiparty computation (MPC) protocol in an incomplete communication graph while keeping the communication graph hidden. The work of Akavia et al. (CRYPTO 2017 and JoC 2020) shown that THC is feasible for any graph. In this work, we focus on the efficiency of THC and give improvements for various tasks including broadcast, sum and general computation. We mainly consider THC on undirected cycles, but we also give two results for THC on general graphs. All of our results are derived in the presence of a passive adversary statically corrupting any number of parties. \par In the undirected cycles, the state-of-the-art topology-hiding broadcast (THB) protocol is the Akavia-Moran (AM) protocol of Akavia et al. (EUROCRYPT 2017). We give an optimization for the AM protocol such that the communication cost of broadcasting $O(\kappa)$ bits is reduced from $O(n^2\kappa^2)$ bits to $O(n^2\kappa)$ bits. We also consider the sum and general computation functionalities. Previous to our work, the only THC protocols realizing the sum and general computation functionalities are constructed by using THB to simulate point-to-point channels in an MPC protocol realizing the sum and general computation functionalities, respectively. By allowing the parties to know the exact value of the number of the parties (the AM protocol and our optimization only assume the parties know an upper bound of the number of the parties), we can derive more efficient THC protocols realizing these two functionalities. As a result, comparing with previous works, we reduce the communication cost by a factor of $O(n\kappa)$ for both the sum and general computation functionalities. \par As we have mentioned, we also get two results for THC on general graphs. The state-of-the-art THB protocol for general graphs is the Akavia-LaVigne-Moran (ALM) protocol of Akavia et al. (CRYPTO 2017 and JoC 2020). Our result is that our optimization for the AM protocol also applies to the ALM protocol and can reduce its communication cost by a factor of $O(\kappa)$. Moreover, we optimize the fully-homomorphic encryption (FHE) based GTHC protocol of LaVigne et al. (TCC 2018) and reduce its communication cost from $O(n^8\kappa^2)$ FHE ciphertexts and $O(n^5\kappa)$ FHE public keys to $O(n^6\kappa)$ FHE ciphertexts and $O(n^5\kappa)$ FHE public keys.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Solutions to quantum weak coin flipping**
  2022-08-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1101)
  Atul Singh Arora, Jérémie Roland, Chrysoula Vlachou, Stephan Weis

  <details><summary>摘要 / Abstract</summary>

  Weak coin flipping is an important cryptographic primitive, as it is the strongest known secure two-party computation primitive, that classically becomes secure only when certain assumptions are made (e.g. computational hardness), while quantumly there exist protocols that achieve arbitrarily close to perfect security. This breakthrough result was established by C. Mochon in 2007 [arXiv:0711.4114], however, his proof of existence was partially non-constructive, thus, setting back the proposal of explicit protocols. In this work, we report three different solutions to the quantum weak coin flipping problem. In particular, we propose different methods that result---either analytically or numerically---in the operators needed to construct weak coin flipping protocols with different levels of security, including nearly perfect security. In order to develop these methods, we study the quantum weak coin flipping problem from both an algebraic and a geometric perspective. We also analytically construct illustrative examples of weak coin flipping protocols achieving different levels of security.

  匹配依据：MPC: secure two party computation

  </details>

- **Solving the Kidney Exchange Problem Using Privacy-Preserving Integer Programming (Updated and Extended Version)**
  2022-08-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.11319)
  Malte Breuer, Pascal Hein, Leonardo Pompe, Ben Temme, Ulrike Meyer, Susanne Wetzel

  <details><summary>摘要 / Abstract</summary>

  The kidney exchange problem (KEP) is to find a constellation of exchanges that maximizes the number of transplants that can be carried out for a set of pairs of patients with kidney disease and their incompatible donors. Recently, this problem has been tackled from a privacy perspective in order to protect the sensitive medical data of patients and donors and to decrease the potential for manipulation of the computing of the exchanges. However, the proposed approaches to date either only compute an approximative solution to the KEP or they suffer from a huge decrease in performance. In this paper, we suggest a novel privacy-preserving protocol that computes an exact solution to the KEP and significantly outperforms the other existing exact approaches. Our novel protocol is based on Integer Programming which is the most efficient method for solving the KEP in the non privacy-preserving case. We achieve an improved performance compared to the privacy-preserving approaches known to date by extending the output of the ideal functionality to include the termination decisions of the underlying algorithm. We implement our protocol in the SMPC benchmarking framework MP-SPDZ and compare its performance to the existing protocols for solving the KEP. In this extended version of our paper, we also evaluate whether and if so how much information can be inferred from the extended output of the ideal functionality.

  匹配依据：MPC: smpc (context)

  </details>

- **Efficient Multiparty Protocols Using Generalized Parseval's Identity and the Theta Algebra**
  2022-08-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.09852)
  Giorgio Sonnino, Alberto Sonnino

  <details><summary>摘要 / Abstract</summary>

  We propose a protocol able to show publicly addition and multiplication on secretly shared values. To this aim we developed a protocol based on the use of masks and on the FMPC (Fourier Multi-Party Computation). FMPC is a novel multiparty computation protocol of arithmetic circuits based on secret-sharing, capable to compute addition and multiplication of secrets with no communication. We achieve this task by introducing the first generalisation of Parseval&#x27;s identity for Fourier series applicable to an arbitrary number of inputs and a new algebra referred to as the &quot;Theta-algebra&quot;. FMPC operates in a setting where users wish to compute a function over some secret inputs by submitting the computation to a set of nodes, without revealing them those inputs. FMPC offloads most of the computational complexity to the end users, and includes an online phase that mainly consists of each node locally evaluating specific functions. FMPC paves the way for a new kind of multiparty computation protocols; making it possible to compute addition and multiplication of secrets stepping away from circuit garbling and the traditional algebra introduced by Donald Beaver in 1991. Our protocol is capable to compute addition and multiplication with no communication and its simplicity provides efficiency and ease of implementation.

  匹配依据：MPC: multi party computation, multiparty computation, secret sharing

  </details>

- **Cluster Based Secure Multi-Party Computation in Federated Learning for Histopathology Images**
  2022-08-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.10919)
  S. Maryam Hosseini, Milad Sikaroudi, Morteza Babaei, H. R. Tizhoosh

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) is a decentralized method enabling hospitals to collaboratively learn a model without sharing private patient data for training. In FL, participant hospitals periodically exchange training results rather than training samples with a central server. However, having access to model parameters or gradients can expose private training data samples. To address this challenge, we adopt secure multiparty computation (SMC) to establish a privacy-preserving federated learning framework. In our proposed method, the hospitals are divided into clusters. After local training, each hospital splits its model weights among other hospitals in the same cluster such that no single hospital can retrieve other hospitals&#x27; weights on its own. Then, all hospitals sum up the received weights, sending the results to the central server. Finally, the central server aggregates the results, retrieving the average of models&#x27; weights and updating the model without having access to individual hospitals&#x27; weights. We conduct experiments on a publicly available repository, The Cancer Genome Atlas (TCGA). We compare the performance of the proposed framework with differential privacy and federated averaging as the baseline. The results reveal that compared to differential privacy, our framework can achieve higher accuracy with no privacy leakage risk at a cost of higher communication overhead.

  匹配依据：MPC: secure multi party computation, secure multiparty computation

  </details>

- **New Bounds on the Multiplicative Complexity of Boolean Functions**
  2022-08-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1077)
  Meltem Sonmez Turan

  <details><summary>摘要 / Abstract</summary>

  Multiplicative Complexity (MC) is defined as the minimum number of AND gates required to implement a function with a circuit over the basis AND, XOR, NOT. This complexity measure is relevant for many advanced cryptographic protocols such as fully homomorphic encryption, multi-party computation, and zero-knowledge proofs, where processing AND gates is more expensive than processing XOR gates. Although there is no known asymptotically efficient technique to compute the MC of a random Boolean function, bounds on the MC of Boolean functions are successfully used to to show existence of Boolean functions with a particular MC. In 2000, Boyar et al. showed that, for all $n\geq 0$, at most $2^{k^2+2k+2kn+n+1}$ $n$-variable Boolean functions can be computed with $k$ AND gates. This bound is used to prove the existence of a 8-variable Boolean functions with MC greater than 7. In this paper, we improve the Boyar et al. bound.

  匹配依据：MPC: multi party computation

  </details>

- **Private, Efficient, and Accurate: Protecting Models Trained by Multi-party Learning with Differential Privacy**
  2022-08-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.08662)
  Wenqiang Ruan, Mingxin Xu, Wenjing Fang, Li Wang, Lei Wang, Weili Han

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation-based machine learning, referred to as MPL, has become an important technology to utilize data from multiple parties with privacy preservation. While MPL provides rigorous security guarantees for the computation process, the models trained by MPL are still vulnerable to attacks that solely depend on access to the models. Differential privacy could help to defend against such attacks. However, the accuracy loss brought by differential privacy and the huge communication overhead of secure multi-party computation protocols make it highly challenging to balance the 3-way trade-off between privacy, efficiency, and accuracy. In this paper, we are motivated to resolve the above issue by proposing a solution, referred to as PEA (Private, Efficient, Accurate), which consists of a secure DPSGD protocol and two optimization methods. First, we propose a secure DPSGD protocol to enforce DPSGD in secret sharing-based MPL frameworks. Second, to reduce the accuracy loss led by differential privacy noise and the huge communication overhead of MPL, we propose two optimization methods for the training process of MPL: (1) the data-independent feature extraction method, which aims to simplify the trained model structure; (2) the local data-based global model initialization method, which aims to speed up the convergence of the model training. We implement PEA in two open-source MPL frameworks: TF-Encrypted and Queqiao. The experimental results on various datasets demonstrate the efficiency and effectiveness of PEA. E.g. when $ε$ = 2, we can train a differentially private classification model with an accuracy of 88% for CIFAR-10 within 7 minutes under the LAN setting. This result significantly outperforms the one from CryptGPU, one SOTA MPL framework: it costs more than 16 hours to train a non-private deep neural network model on CIFAR-10 with the same accuracy.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Programmable Distributed Point Functions**
  2022-08-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1060)
  Elette Boyle, Niv Gilboa, Yuval Ishai, Victor I. Kolobov

  <details><summary>摘要 / Abstract</summary>

  A distributed point function (DPF) is a cryptographic primitive that enables compressed additive sharing of a secret unit vector across two or more parties. Despite growing ubiquity within applications and notable research efforts, the best 2-party DPF construction to date remains the tree-based construction from (Boyle et al, CCS&#x27;16), with no significantly new approaches since. We present a new framework for 2-party DPF construction, which applies in the setting of feasible (polynomial-size) domains. This captures in particular all DPF applications in which the keys are expanded to the full domain. Our approach is motivated by a strengthened notion we put forth, of programmable DPF (PDPF): in which a short, input-independent &quot;offline&quot; key can be reused for sharing many point functions. * PDPF from OWF: We construct a PDPF for feasible domains from the minimal assumption that one-way functions exist, where the second &quot;online&quot; key size is polylogarithmic in the domain size $N$. Our approach offers multiple new efficiency features and applications: * Privately puncturable PRFs: Our PDPF gives the first OWF-based privately puncturable PRFs (for feasible domains) with sublinear keys. * $O(1)$-round distributed DPF Gen: We obtain a (standard) DPF with polylog-size keys that admits an analog of Doerner-shelat (CCS&#x27;17) distributed key generation, requiring only $O(1)$ rounds (versus $\log N$). * PCG with 1 short key: Compressing useful correlations for secure computation, where one key is of minimal size. This provides up to exponential communication savings in some application scenarios.

  匹配依据：MPC: secure computation

  </details>

- **Perfectly Secure Synchronous MPC with Asynchronous Fallback Guarantees Against General Adversaries**
  2022-08-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.06223) · [IACR ePrint](https://eprint.iacr.org/2022/1047)
  Ananya Appan, Anirudh Chandramouli, Ashish Choudhury

  <details><summary>摘要 / Abstract</summary>

  In this work, we study perfectly-secure multi-party computation (MPC) against general (non-threshold) adversaries. Known protocols in a synchronous network are secure against $Q^{(3)}$ adversary structures, while in an asynchronous network, known protocols are secure against $Q^{(4)}$ adversary structures. A natural question is whether there exists a single protocol which remains secure against $Q^{(3)}$ and $Q^{(4)}$ adversary structures in a synchronous and in an asynchronous network respectively, where the parties are not aware of the network type. We design the first such best-of-both-worlds protocol against general adversaries. Our result generalizes the result of Appan, Chandramouli and Choudhury (PODC 2022), which presents a best-of-both-worlds perfectly-secure protocol against threshold adversaries. To design our protocol, we present two important building blocks which are of independent interest. The first building block is a best-of-both-worlds perfectly-secure Byzantine agreement (BA) protocol for $Q^{(3)}$ adversary structures, which remains secure both in a synchronous, as well as an asynchronous network. The second building block is a best-of-both-worlds perfectly-secure verifiable secret-sharing (VSS) protocol, which remains secure against $Q^{(3)}$ and $Q^{(4)}$ adversary structures in a synchronous network and an asynchronous network respectively.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **A framework for constructing Single Secret Leader Election from MPC**
  2022-08-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1040)
  Michael Backes, Pascal Berrang, Lucjan Hanzlik, Ivan Pryvalov

  <details><summary>摘要 / Abstract</summary>

  The emergence of distributed digital currencies has raised the need for a reliable consensus mechanism. In proof-of-stake cryptocur- rencies, the participants periodically choose a closed set of validators, who can vote and append transactions to the blockchain. Each valida- tor can become a leader with the probability proportional to its stake. Keeping the leader private yet unique until it publishes a new block can significantly reduce the attack vector of an adversary and improve the throughput of the network. The problem of Single Secret Leader Election (SSLE) was first formally defined by Boneh et al. in 2020. In this work, we propose a novel framework for constructing SSLE proto- cols, which relies on secure multi-party computation (MPC) and satisfies the desired security properties. Our framework does not use any shuffle or sort operations and has a computational cost for N parties as low as O(N) of basic MPC operations per party. We improve the state-of-the- art for SSLE protocols that do not assume a trusted setup. Moreover, our SSLE scheme efficiently handles weighted elections. That is, for a total weight S of N parties, the associated costs are only increased by a factor of logS. When the MPC layer is instantiated with techniques based on Shamir’s secret-sharing, our SSLE has a communication cost of O(N2) which is spread over O(log N) rounds, can tolerate up to t &lt; N/2 of faulty nodes without restarting the protocol, and its security relies on DDH in the random oracle model. When the MPC layer is instantiated with more efficient techniques based on garbled circuits, our SSLE re- quires all parties to participate, up to N − 1 of which can be malicious, and its security is based on the random oracle model.

  匹配依据：MPC: garbled circuits, secret sharing, secure multi party computation

  </details>

- **RPM: Robust Anonymity at Scale**
  2022-08-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1037)
  Donghang Lu, Aniket Kate

  <details><summary>摘要 / Abstract</summary>

  This work presents RPM, a scalable anonymous communication protocol suite using secure multiparty computation (MPC) with the offline-online model. We generate random, unknown permutation matrices in a secret-shared fashion and achieve improved (online) performance and the lightest communication and computation overhead for the clients compared to the state of art robust anonymous communication protocols. Using square-lattice shuffling, we make our protocol scale well as the number of clients increases. We provide three protocol variants, each targeting different input volumes and MPC frameworks/libraries. Besides, due to the modular design, our protocols can be easily generalized to support more MPC functionalities and security properties as they get developed. We also illustrate how to generalize our protocols to support two-way anonymous communication and secure sorting. We have implemented our protocols using the MP-SPDZ library suit and the benchmark illustrates that our protocols achieve unprecedented online phase performance with practical offline phases.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Efficient Pseudorandom Correlation Generators from Ring-LPN**
  2022-08-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1035)
  Elette Boyle, Geoffroy Couteau, Niv Gilboa, Yuval Ishai, Lisa Kohl, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation can often utilize a trusted source of correlated randomness to achieve better efficiency. A recent line of work, initiated by Boyle et al. (CCS 2018, Crypto 2019), showed how useful forms of correlated randomness can be generated using a cheap, one-time interaction, followed by only &quot;silent&quot; local computation. This is achieved via a pseudorandom correlation generator (PCG), a deterministic function that stretches short correlated seeds into long instances of a target correlation. Previous works constructed concretely efficient PCGs for simple but useful correlations, including random oblivious transfer and vector-OLE, together with efficient protocols to distribute the PCG seed generation. Most of these constructions were based on variants of the Learning Parity with Noise (LPN) assumption. PCGs for other useful correlations had poor asymptotic and concrete efficiency. In this work, we design a new class of efficient PCGs based on different flavors of the ring-LPN assumption. Our new PCGs can generate OLE correlations, authenticated multiplication triples, matrix product correlations, and other types of useful correlations over large fields. These PCGs are more efficient by orders of magnitude than the previous constructions and can be used to improve the preprocessing phase of many existing MPC protocols.

  匹配依据：MPC: oblivious transfer, secure multiparty computation

  </details>

- **SIM: Secure Interval Membership Testing and Applications to Secure Comparison**
  2022-08-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1023)
  Albert Yu, Donghang Lu, Aniket Kate, Hemanta K. Maji

  <details><summary>摘要 / Abstract</summary>

  The offline-online model is a leading paradigm for practical secure multi-party computation (MPC) protocol design that has successfully reduced the overhead for several prevalent privacy-preserving computation functionalities common to diverse application domains. However, the prohibitive overheads associated with secure comparison -- one of these vital functionalities -- often bottlenecks current and envisioned MPC solutions. Indeed, an efficient secure comparison solution has the potential for significant real-world impact through its broad applications. This work identifies and presents SIM, a secure protocol for the functionality of interval membership testing. This security functionality, in particular, facilitates secure less-than-zero testing and, in turn, secure comparison. A key technical challenge is to support a fast online protocol for testing in large rings while keeping the precomputation tractable. Motivated by the map-reduce paradigm, this work introduces the innovation of (1) computing a sequence of intermediate functionalities on a partition of the input into input blocks and (2) securely aggregating the output from these intermediate outputs. This innovation allows controlling the size of the precomputation through a granularity parameter representing these input blocks&#x27; size -- enabling application-specific automated compiler optimizations. To demonstrate our protocols&#x27; efficiency, we implement and test their performance in a high-demand application: privacy-preserving machine learning. The benchmark results show that switching to our protocols yields significant performance improvement, which indicates that using our protocol in a plug-and-play fashion can improve the performance of various security applications. Our new paradigm of protocol design may be of independent interest because of its potential for extensions to other functionalities of practical interest.

  匹配依据：MPC: secure multi party computation

  </details>

- **Minimal Binary Linear Codes from Vectorial Boolean Functions**
  2022-08-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.03864)
  Yanjun Li, Jie Peng, Haibin Kan, Lijing Zheng

  <details><summary>摘要 / Abstract</summary>

  Recently, much progress has been made to construct minimal linear codes due to their preference in secret sharing schemes and secure two-party computation. In this paper, we put forward a new method to construct minimal linear codes by using vectorial Boolean functions. Firstly, we give a necessary and sufficient condition for a generic class of linear codes from vectorial Boolean functions to be minimal. Based on that, we derive some new three-weight minimal linear codes and determine their weight distributions. Secondly, we obtain a necessary and sufficient condition for another generic class of linear codes from vectorial Boolean functions to be minimal and to be violated the AB condition. As a result, we get three infinite families of minimal linear codes violating the AB condition. To the best of our knowledge, this is the first time that minimal liner codes are constructed from vectorial Boolean functions. Compared with other known ones, in general the minimal liner codes obtained in this paper have higher dimensions.

  匹配依据：MPC: secret sharing, secure two party computation

  </details>

- **Maliciously Secure Massively Parallel Computation for All-but-One Corruptions**
  2022-08-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1027)
  Rex Fernando, Yuval Gelles, Ilan Komargodski, Elaine Shi

  <details><summary>摘要 / Abstract</summary>

  The Massive Parallel Computing (MPC) model gained wide adoption over the last decade. By now, it is widely accepted as the right model for capturing the commonly used programming paradigms (such as MapReduce, Hadoop, and Spark) that utilize parallel computation power to manipulate and analyze huge amounts of data. Motivated by the need to perform large-scale data analytics in a privacy-preserving manner, several recent works have presented generic compilers that transform algorithms in the MPC model into secure counterparts, while preserving various efficiency parameters of the original algorithms. The first paper, due to Chan et al. (ITCS ’20), focused on the honest majority setting. Later, Fernando et al. (TCC ’20) considered the dishonest majority setting. The latter work presented a compiler that transforms generic MPC algorithms into ones which are secure against semi-honest attackers that may control all but one of the parties involved. The security of their resulting algorithm relied on the existence of a PKI and also on rather strong cryptographic assumptions: indistinguishability obfuscation and the circular security of certain LWE-based encryption systems. In this work, we focus on the dishonest majority setting, following Fernando et al. In this setting, the known compilers do not achieve the standard security notion called malicious security, where attackers can arbitrarily deviate from the prescribed protocol. In fact, we show that unless very strong setup assumptions as made (such as a programmable random oracle), it is provably impossible to withstand malicious attackers due to the stringent requirements on space and round complexity. As our main contribution, we complement the above negative result by designing the first general compiler for malicious attackers in the dishonest majority setting. The resulting protocols withstand all-but-one corruptions. Our compiler relies on a simple PKI and a (programmable) random oracle, and is proven secure assuming LWE and SNARKs. Interestingly, even with such strong assumptions, it is rather non-trivial to obtain a secure protocol.

  匹配依据：MPC: mpc (context)

  </details>

- **HWGN2: Side-channel Protected Neural Networks through Secure and Private Function Evaluation**
  2022-08-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.03806)
  Mohammad Hashemi, Steffi Roy, Domenic Forte, Fatemeh Ganji

  <details><summary>摘要 / Abstract</summary>

  Recent work has highlighted the risks of intellectual property (IP) piracy of deep learning (DL) models from the side-channel leakage of DL hardware accelerators. In response, to provide side-channel leakage resiliency to DL hardware accelerators, several approaches have been proposed, mainly borrowed from the methodologies devised for cryptographic implementations. Therefore, as expected, the same challenges posed by the complex design of such countermeasures should be dealt with. This is despite the fact that fundamental cryptographic approaches, specifically secure and private function evaluation, could potentially improve the robustness against side-channel leakage. To examine this and weigh the costs and benefits, we introduce hardware garbled NN (HWGN2), a DL hardware accelerator implemented on FPGA. HWGN2 also provides NN designers with the flexibility to protect their IP in real-time applications, where hardware resources are heavily constrained, through a hardware-communication cost trade-off. Concretely, we apply garbled circuits, implemented using a MIPS architecture that achieves up to 62.5x fewer logical and 66x less memory utilization than the state-of-the-art approaches at the price of communication overhead. Further, the side-channel resiliency of HWGN2 is demonstrated by employing the test vector leakage assessment (TVLA) test against both power and electromagnetic side-channels. This is in addition to the inherent feature of HWGN2: it ensures the privacy of users&#x27; input, including the architecture of NNs. We also demonstrate a natural extension to the malicious security modeljust as a by-product of our implementation.

  匹配依据：MPC: garbled circuits

  </details>

- **Garbled EDA: Privacy Preserving Electronic Design Automation**
  2022-08-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.03822)
  Mohammad Hashemi, Steffi Roy, Fatemeh Ganji, Domenic Forte

  <details><summary>摘要 / Abstract</summary>

  The complexity of modern integrated circuits (ICs) necessitates collaboration between multiple distrusting parties, including thirdparty intellectual property (3PIP) vendors, design houses, CAD/EDA tool vendors, and foundries, which jeopardizes confidentiality and integrity of each party&#x27;s IP. IP protection standards and the existing techniques proposed by researchers are ad hoc and vulnerable to numerous structural, functional, and/or side-channel attacks. Our framework, Garbled EDA, proposes an alternative direction through formulating the problem in a secure multi-party computation setting, where the privacy of IPs, CAD tools, and process design kits (PDKs) is maintained. As a proof-of-concept, Garbled EDA is evaluated in the context of simulation, where multiple IP description formats (Verilog, C, S) are supported. Our results demonstrate a reasonable logical-resource cost and negligible memory overhead. To further reduce the overhead, we present another efficient implementation methodology, feasible when the resource utilization is a bottleneck, but the communication between two parties is not restricted. Interestingly, this implementation is private and secure even in the presence of malicious adversaries attempting to, e.g., gain access to PDKs or in-house IPs of the CAD tool providers.

  匹配依据：MPC: secure multi party computation

  </details>

- **Privacy-Preserving Chaotic Extreme Learning Machine with Fully Homomorphic Encryption**
  2022-08-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.02587)
  Syed Imtiaz Ahamed, Vadlamani Ravi

  <details><summary>摘要 / Abstract</summary>

  The Machine Learning and Deep Learning Models require a lot of data for the training process, and in some scenarios, there might be some sensitive data, such as customer information involved, which the organizations might be hesitant to outsource for model building. Some of the privacy-preserving techniques such as Differential Privacy, Homomorphic Encryption, and Secure Multi-Party Computation can be integrated with different Machine Learning and Deep Learning algorithms to provide security to the data as well as the model. In this paper, we propose a Chaotic Extreme Learning Machine and its encrypted form using Fully Homomorphic Encryption where the weights and biases are generated using a logistic map instead of uniform distribution. Our proposed method has performed either better or similar to the Traditional Extreme Learning Machine on most of the datasets.

  匹配依据：MPC: secure multi party computation

  </details>

- **Semiquantum secret sharing by using x-type states**
  2022-08-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.01922)
  Ying Chen, Tian-Yu Ye

  <details><summary>摘要 / Abstract</summary>

  In this paper, a semiquantum secret sharing (SQSS) protocol based on x-type states is proposed, which can accomplish the goal that only when two classical communicants cooperate together can they extract the shared secret key of a quantum communicant. Detailed security analysis turns out that this protocol is completely robust against an eavesdropper. This protocol has some merits: (1) it only requires one kind of quantum entangled state as the initial quantum resource; (2) it doesn&#x27;t employ quantum entanglement swapping or unitary operations; and (3) it needn&#x27;t share private keys among different participants beforehand.

  匹配依据：MPC: secret sharing

  </details>

- **Advance sharing of quantum shares for classical secrets**
  2022-08-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.01847)
  Rina Miyajima, Ryutaroh Matsumoto

  <details><summary>摘要 / Abstract</summary>

  Secret sharing schemes for classical secrets can be classified into classical secret sharing schemes and quantum secret sharing schemes. Classical secret sharing has been known to be able to distribute some shares before a given secret. On the other hand, quantum mechanics extends the capabilities of secret sharing beyond those of classical secret sharing. We propose quantum secret sharing with the capabilities in designing of access structures more flexibly and realizing higher efficiency beyond those of classical secret sharing, that can distribute some shares before a given secret.

  匹配依据：MPC: secret sharing

  </details>

- **Differentially Private Vertical Federated Clustering**
  2022-08-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.01700)
  Zitao Li, Tianhao Wang, Ninghui Li

  <details><summary>摘要 / Abstract</summary>

  In many applications, multiple parties have private data regarding the same set of users but on disjoint sets of attributes, and a server wants to leverage the data to train a model. To enable model learning while protecting the privacy of the data subjects, we need vertical federated learning (VFL) techniques, where the data parties share only information for training the model, instead of the private data. However, it is challenging to ensure that the shared information maintains privacy while learning accurate models. To the best of our knowledge, the algorithm proposed in this paper is the first practical solution for differentially private vertical federated k-means clustering, where the server can obtain a set of global centers with a provable differential privacy guarantee. Our algorithm assumes an untrusted central server that aggregates differentially private local centers and membership encodings from local data parties. It builds a weighted grid as the synopsis of the global dataset based on the received information. Final centers are generated by running any k-means algorithm on the weighted grid. Our approach for grid weight estimation uses a novel, light-weight, and differentially private set intersection cardinality estimation algorithm based on the Flajolet-Martin sketch. To improve the estimation accuracy in the setting with more than two data parties, we further propose a refined version of the weights estimation algorithm and a parameter tuning strategy to reduce the final k-means utility to be close to that in the central private setting. We provide theoretical utility analysis and experimental evaluation results for the cluster centers computed by our algorithm and show that our approach performs better both theoretically and empirically than the two baselines based on existing techniques.

  匹配依据：MPC: private set intersection

  </details>

- **Detecting and Characterizing Propagation of Security Weaknesses in Puppet-based Infrastructure Management**
  2022-08-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.01242)
  Akond Rahman, Chris Parnin

  <details><summary>摘要 / Abstract</summary>

  Despite being beneficial for managing computing infrastructure automatically, Puppet manifests are susceptible to security weaknesses, e.g., hard-coded secrets and use of weak cryptography algorithms. Adequate mitigation of security weaknesses in Puppet manifests is thus necessary to secure computing infrastructure that are managed with Puppet manifests. A characterization of how security weaknesses propagate and affect Puppet-based infrastructure management, can inform practitioners on the relevance of the detected security weaknesses, as well as help them take necessary actions for mitigation. To that end, we conduct an empirical study with 17,629 Puppet manifests mined from 336 open source repositories. We construct Taint Tracker for Puppet Manifests (TaintPup), for which we observe 2.4 times more precision compared to that of a state-of-the-art security static analysis tool. TaintPup leverages Puppet-specific information flow analysis using which we characterize propagation of security weaknesses. From our empirical study, we observe security weaknesses to propagate into 4,457 resources, i.e, Puppet-specific code elements used to manage infrastructure. A single instance of a security weakness can propagate into as many as 35 distinct resources. We observe security weaknesses to propagate into 7 categories of resources, which include resources used to manage continuous integration servers and network controllers. According to our survey with 24 practitioners, propagation of security weaknesses into data storage-related resources is rated to have the most severe impact for Puppet-based infrastructure management.

  匹配依据：MPC: secure computing

  </details>

- **Random-Index Oblivious RAM**
  2022-07-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/982)
  Shai Halevi, Eyal Kushilevitz

  <details><summary>摘要 / Abstract</summary>

  We study the notion of Random-index ORAM (RORAM), which is a weak form of ORAM where the Client is limited to asking for (and possibly modifying) random elements of the $N$-items memory, rather than specific ones. That is, whenever the client issues a request, it gets in return a pair $(r,x_r)$ where $r\in_R[N]$ is a random index and $x_r$ is the content of the $r$-th memory item. Then, the client can also modify the content to some new value $x&#x27;_r$. We first argue that the limited functionality of RORAM still suffices for certain applications. These include various applications of sampling (or sub-sampling), and in particular the very-large-scale MPC application in the setting of~ Benhamouda et al. (TCC 2020). Clearly, RORAM can be implemented using any ORAM scheme (by the Client selecting the random $r$&#x27;s by himself), but the hope is that the limited functionality of RORAM can make it faster and easier to implement than ORAM. Indeed, our main contributions are several RORAM schemes (both of the hierarchical-type and the tree-type) of lighter complexity than that of ORAM.

  匹配依据：MPC: mpc (context)

  </details>

- **Non-Malleable Multi-Party Computation**
  2022-07-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/978)
  Fuchun Lin

  <details><summary>摘要 / Abstract</summary>

  We study a tamper-tolerant implementation security notion for general purpose Multi-Party Computation (MPC) protocols, as an analogue of the leakage-tolerant notion in the MPC literature. An MPC protocol is tamper-tolerant, or more specifically, non-malleable (with respect to a certain type of tampering) if the processing of the protocol under corruption of parties (and tampering of some ideal resource assumed by the protocol) can be simulated by an ideal world adversary who, after the trusted party spit out the output, further decides how the output for honest parties should be tampered with. Intuitively, we relax the correctness of secure computation in a privacy-preserving way, decoupling the two entangled properties that define secure computation. The rationale behind this relaxation is that even the strongest notion of correctness in MPC allows corrupt parties to substitute wrong inputs to the trusted party and the output is incorrect anyway, maybe the importance of insisting on that the adversary does not further tamper with the incorrect output is overrated, at least for some applications. Various weak privacy notions against malicious adversary play an important role in the study of two-party computation, where full security is hard to achieve efficiently. We begin with the honest majority setting, where efficient constructions for general purpose MPC protocols with full security are well understood assuming secure point-to-point channels. We then focus on non-malleability with respect to tampered secure point-to-point channels. (1) We show achievability of non-malleable MPC against the bounded state tampering adversary in the joint tampering model through a naive compiler approach, exploiting a known construction of interactive non-malleable codes. The construction is currently not efficient and should be understood as showing feasibility in a rather strong tampering model. (2) We show efficient constructions of non-malleable MPC protocols against weaker variants of bounded state tampering adversary in the independent tampering model, where the protocol obtained have the same asymptotic communication complexity as best MPC protocols against honest-but-curious adversary. These are all information-theoretic results and are to be contrasted against impossibility of secure MPC when secure point-to-point channels are compromised. Though general non-malleable MPC in no honest majority setting is beyond the scope of this work, we discuss interesting applications of honest majority non-malleable MPC in the celebrated MPC-in-the-head paradigm. Other than an abstract result concerning non-malleability, we also derive, in standard model where there is no tampering, that strong (ideal/real world) privacy against malicious adversary can be achieved in a conceptually very simple way.

  匹配依据：MPC: multi party computation, secure computation, two party computation

  </details>

- **Private network parameter estimation with quantum sensors**
  2022-07-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.14450)
  Nathan Shettell, Majid Hassani, Damian Markham

  <details><summary>摘要 / Abstract</summary>

  Networks of quantum sensors are a central application of burgeoning quantum networks. A key question for the use of such networks will be their security, particularly against malicious participants of the network. We introduce a protocol to securely evaluate linear functions of parameters over a network of quantum sensors, ensuring that all parties only have access to the function value, and no access to the individual parameters. This has application to secure networks of clocks and opens the door to more general applications of secure multiparty computing to networks of quantum sensors.

  匹配依据：MPC: secure multiparty computing

  </details>

- **Long Live The Honey Badger: Robust Asynchronous DPSS and its Applications**
  2022-07-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/971)
  Thomas Yurek, Zhuolun Xiang, Yu Xia, Andrew Miller

  <details><summary>摘要 / Abstract</summary>

  Secret sharing is an essential tool for many distributed applications, including distributed key generation and multiparty computation. For many practical applications, we would like to tolerate network churn, meaning participants can dynamically enter and leave the pool of protocol participants as they please. Such protocols, called Dynamic-committee Proactive Secret Sharing (DPSS), have recently been studied; however, existing DPSS protocols do not gracefully handle faults: the presence of even one unexpectedly slow node can often slow down the whole protocol by a factor of $O(n)$. In this work, we explore optimally fault-tolerant asynchronous DPSS that is not slowed down by crash faults and even handles byzantine faults while maintaining the same performance. We first introduce the first high-threshold DPSS, which offers favorable characteristics relative to prior non-synchronous works in the presence of faults while simultaneously supporting higher privacy thresholds. We then batch-amortize this scheme along with a parallel non-high-threshold scheme which achieves optimal bandwidth characteristics. We implement our schemes and demonstrate that they can compete with prior work in best-case performance while outperforming it in non-optimal settings.

  匹配依据：MPC: multiparty computation, secret sharing

  </details>

- **Certified Everlasting Functional Encryption**
  2022-07-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/969)
  Taiga Hiroka, Tomoyuki Morimae, Ryo Nishimaki, Takashi Yamakawa

  <details><summary>摘要 / Abstract</summary>

  Computational security in cryptography has a risk that computational assumptions underlying the security are broken in the future. One solution is to construct information-theoretically-secure protocols, but many cryptographic primitives are known to be impossible (or unlikely) to have information-theoretical security even in the quantum world. A nice compromise (intrinsic to quantum) is certified everlasting security, which roughly means the following. A receiver with possession of quantum encrypted data can issue a certificate that shows that the receiver has deleted the encrypted data. If the certificate is valid, the security is guaranteed even if the receiver becomes computationally unbounded. Although several cryptographic primitives, such as commitments and zero-knowledge, have been made certified everlasting secure, there are many other important primitives that are not known to be certified everlasting secure. In this paper, we introduce certified everlasting FE. In this primitive, the receiver with the ciphertext of a message $m$ and the functional decryption key of a function $f$ can obtain $f(m)$ and nothing else. The security holds even if the adversary becomes computationally unbounded after issuing a valid certificate. We, first, construct certified everlasting FE for P/poly circuits where only a single key query is allowed for the adversary. We, then, extend it to $q$-bounded one for NC1 circuits where $q$-bounded means that $q$ key queries are allowed for the adversary with an a priori bounded polynomial $q$. For the construction of certified everlasting FE, we introduce and construct certified everlasting versions of secret-key encryption, public-key encryption, receiver non-committing encryption, and a garbling scheme, which are of independent interest.

  匹配依据：MPC: garbling scheme

  </details>

- **Quantifying the Cost of Privately Storing Data in Distributed Storage Systems**
  2022-07-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.13681)
  Remi A. Chou

  <details><summary>摘要 / Abstract</summary>

  Consider a user who wishes to store a file in multiple servers such that at least t servers are needed to reconstruct the file, and z colluding servers cannot learn any information about the file. Unlike traditional secret-sharing models, where perfectly secure channels are assumed to be available at no cost between the user and each server, we assume that the user can only send data to the servers via a public channel, and that the user and each server share an individual secret key with length n. For a given n, we determine the maximal length of the file that the user can store, and thus quantify the necessary cost to store a file of a certain length, in terms of the length of the secret keys that the user needs to share with the servers. Additionally, for this maximal file length, we determine (i) the optimal amount of local randomness needed at the user, (ii) the optimal amount of public communication from the user to the servers, and (iii) the optimal amount of storage requirement at the servers.

  匹配依据：MPC: secret sharing

  </details>

- **Mistakes of A Popular Protocol Calculating Private Set Intersection and Union Cardinality and Its Corrections**
  2022-07-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.13277)
  Yang Tan, Bo Lv

  <details><summary>摘要 / Abstract</summary>

  In 2012, De Cristofaro et al. proposed a protocol to calculate the Private Set Intersection and Union cardinality(PSI-CA and PSU-CA). This protocol&#x27;s security is based on the famous DDH assumption. Since its publication, it has gained lots of popularity because of its efficiency(linear complexity in computation and communication) and concision. So far, it&#x27;s still considered one of the most efficient PSI-CA protocols and the most cited(more than 170 citations) PSI-CA paper based on the Google Scholar search. However, when we tried to implement this protocol, we couldn&#x27;t get the correct result of the test data. Since the original paper lacks of experimental results to verify the protocol&#x27;s correctness, we looked deeper into the protocol and found out it made a fundamental mistake. Needless to say, its correctness analysis and security proof are also wrong. In this paper, we will point out this PSI-CA protocol&#x27;s mistakes, and provide the correct version of this protocol as well as the PSI protocol developed from this protocol. We also present a new security proof and some experimental results of the corrected protocol.

  匹配依据：MPC: private set intersection

  </details>

- **Multi-partite subspaces containing no locally inaccessible information**
  2022-07-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.13138)
  Sarah Croke

  <details><summary>摘要 / Abstract</summary>

  One notion of non-locality in quantum theory is the fact that information may be encoded in a composite system in such a way that it is not accessible through local measurements, even with the assistance of classical communication. Thus, contrary to the classical case, there exists information in quantum many body systems which cannot be accessed locally. We show however that, remarkably, two-dimensional subspaces do not have this property: any physically allowed measurement on information encoded in any two-dimensional subspace, regardless of entanglement or multi-partite structure, may be performed locally. Further, this requires only local measurement and feed-forward of classical information, readily achievable in many experimental platforms. As an application to quantum secret sharing we suggest a twist on a well known quantum information splitting protocol, which ensures that no receiving party ever has access to the full state sent, but parties must work together to perform measurements on the state. These results may have practical applications to the measurement of encoded qubits in e.g. quantum secret sharing, quantum error correction, and reveal a fundamental property unique to two-dimensional subspaces.

  匹配依据：MPC: secret sharing

  </details>

- **Constructions of linear codes with two or three weights from vectorial dual-bent functions**
  2022-07-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.11668)
  Jiaxin Wang, Zexia Shi, Yadi Wei, Fang-Wei Fu

  <details><summary>摘要 / Abstract</summary>

  Linear codes with a few weights are an important class of codes in coding theory and have attracted a lot of attention. In this paper, we present several constructions of $q$-ary linear codes with two or three weights from vectorial dual-bent functions, where $q$ is a power of an odd prime $p$. The weight distributions of the constructed $q$-ary linear codes are completely determined. We illustrate that some known constructions in the literature can be obtained by our constructions. In some special cases, our constructed linear codes can meet the Griesmer bound. Furthermore, based on the constructed $q$-ary linear codes, we obtain secret sharing schemes with interesting access structures.

  匹配依据：MPC: secret sharing

  </details>

- **Spatial data sharing with secure multi-party computation for exploratory spatial data analysis**
  2022-07-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.13069)
  Shuo Shen, Xinyan Zhu, Yanlei Ma, XIe Xiang, Sun Lilin, Xie Hongjun, An Rui

  <details><summary>摘要 / Abstract</summary>

  Spatial data sharing plays a significant role in opening data research and promoting government agency transparency. However, valuable spatial data, like high-precision geographic information and personal traffic records, cannot be made public because they may incur leakage risks such as intrusion, theft, and the unauthorised sale of proprietary information. When participants with confidential data distrust each other but want to use the other datasets for calculations, the most common solution is to provide their original data to a trusted third party. However, the trusted third party frequently risks being attacked and having the data leaked. To maintain data controllability, most companies and organisations refuse to share their data. In this study, we introduce secure multi-party computation to spatial data sharing to address the sharing problem. Additionally, we describe the design and implementation of the protocols of two exploratory spatial data analyses: global Moran&#x27;s I and local Moran&#x27;s I. Furthermore, we build a system to demonstrate process realisation and results visualisation. Comparing our system with existing data-sharing schemes, our system Identifies the correct result without incurring leaking risks during spatial data sharing.

  匹配依据：MPC: secure multi party computation

  </details>

- **Cryptographic and Financial Fairness**
  2022-07-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.10780)
  Daniele Friolo, Fabio Massacci, Chan Nam Ngo, Daniele Venturi

  <details><summary>摘要 / Abstract</summary>

  A recent trend in multi-party computation is to achieve cryptographic fairness via monetary penalties, i.e. each honest player either obtains the output or receives a compensation in the form of a cryptocurrency. We pioneer another type of fairness, financial fairness, that is closer to the real-world valuation of financial transactions. Intuitively, a penalty protocol is financially fair if the net present cost of participation (the total value of cash inflows less cash outflows, weighted by the relative discount rate) is the same for all honest participants, even when some parties cheat. We formally define the notion, show several impossibility results based on game theory, and analyze the practical effects of (lack of) financial fairness if one was to run the protocols for real on Bitcoin using Bloomberg&#x27;s dark pool trading. For example, we show that the ladder protocol (CRYPTO&#x27;14), and its variants (CCS&#x27;15 and CCS&#x27;16), fail to achieve financial fairness both in theory and in practice, while the penalty protocols of Kumaresan and Bentov (CCS&#x27;14) and Baum, David and Dowsley (FC&#x27;20) are financially fair. This version contains formal definitions, detailed security proofs, demos and experimental data in the appendix.

  匹配依据：MPC: multi party computation

  </details>

- **Multi-party Private Function Evaluation for RAM**
  2022-07-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/939)
  Keyu Ji, Bingsheng Zhang, Tianpei Lu, Kui Ren

  <details><summary>摘要 / Abstract</summary>

  Private function evaluation (PFE) is a special type of MPC protocols that, in addition to the input privacy, can preserve the function privacy. In this work, we propose a PFE scheme for RAM. In particular, we first design an efficient 4-server distributed ORAM scheme with amortized communication $O(\log n)$ per access (both reading and writing). We then simulate a RISC RAM machine over the MPC platform, hiding (i) the memory access pattern, (ii) the machine state (including registers, program counter, condition flag, etc.), and (iii) the executed instructions. Our scheme can naturally support a simplified TinyRAM instruction set; if a public RAM program $P$ with given inputs $x$ needs to execute $z$ instruction cycles, our PFE scheme is able to securely evaluate $P(x)$ on private $P$ and $x$ within $5z+1$ online rounds. We prototype and benchmark our system for set intersection, binary search, quicksort, and heapsort algorithms. For instance, to obliviously perform the binary search algorithm on a $2^{10}$ array takes $5.81s$ with function privacy.

  匹配依据：MPC: mpc (context)

  </details>

- **MUD-PQFed: Towards Malicious User Detection in Privacy-Preserving Quantized Federated Learning**
  2022-07-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.09080)
  Hua Ma, Qun Li, Yifeng Zheng, Zhi Zhang, Xiaoning Liu, Yansong Gao, Said F. Al-Sarawi, Derek Abbott

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL), a distributed machine learning paradigm, has been adapted to mitigate privacy concerns for customers. Despite their appeal, there are various inference attacks that can exploit shared-plaintext model updates to embed traces of customer private information, leading to serious privacy concerns. To alleviate this privacy issue, cryptographic techniques such as Secure Multi-Party Computation and Homomorphic Encryption have been used for privacy-preserving FL. However, such security issues in privacy-preserving FL are poorly elucidated and underexplored. This work is the first attempt to elucidate the triviality of performing model corruption attacks on privacy-preserving FL based on lightweight secret sharing. We consider scenarios in which model updates are quantized to reduce communication overhead in this case, where an adversary can simply provide local parameters outside the legal range to corrupt the model. We then propose the MUD-PQFed protocol, which can precisely detect malicious clients performing attacks and enforce fair penalties. By removing the contributions of detected malicious clients, the global model utility is preserved to be comparable to the baseline global model without the attack. Extensive experiments validate effectiveness in maintaining baseline accuracy and detecting malicious clients in a fine-grained manner

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Is Vertical Logistic Regression Privacy-Preserving? A Comprehensive Privacy Analysis and Beyond**
  2022-07-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.09087)
  Yuzheng Hu, Tianle Cai, Jinyong Shan, Shange Tang, Chaochao Cai, Ethan Song, Bo Li, Dawn Song

  <details><summary>摘要 / Abstract</summary>

  We consider vertical logistic regression (VLR) trained with mini-batch gradient descent -- a setting which has attracted growing interest among industries and proven to be useful in a wide range of applications including finance and medical research. We provide a comprehensive and rigorous privacy analysis of VLR in a class of open-source Federated Learning frameworks, where the protocols might differ between one another, yet a procedure of obtaining local gradients is implicitly shared. We first consider the honest-but-curious threat model, in which the detailed implementation of protocol is neglected and only the shared procedure is assumed, which we abstract as an oracle. We find that even under this general setting, single-dimension feature and label can still be recovered from the other party under suitable constraints of batch size, thus demonstrating the potential vulnerability of all frameworks following the same philosophy. Then we look into a popular instantiation of the protocol based on Homomorphic Encryption (HE). We propose an active attack that significantly weaken the constraints on batch size in the previous analysis via generating and compressing auxiliary ciphertext. To address the privacy leakage within the HE-based protocol, we develop a simple-yet-effective countermeasure based on Differential Privacy (DP), and provide both utility and privacy guarantees for the updated algorithm. Finally, we empirically verify the effectiveness of our attack and defense on benchmark datasets. Altogether, our findings suggest that all vertical federated learning frameworks that solely depend on HE might contain severe privacy risks, and DP, which has already demonstrated its power in horizontal federated learning, can also play a crucial role in the vertical setting, especially when coupled with HE or secure multi-party computation (MPC) techniques.

  匹配依据：MPC: secure multi party computation

  </details>

- **Secure Quantized Training for Deep Learning**
  2022-07-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2107.00501) · [IACR ePrint](https://eprint.iacr.org/2022/933)
  Marcel Keller, Ke Sun

  <details><summary>摘要 / Abstract</summary>

  We implement training of neural networks in secure multi-party computation (MPC) using quantization commonly used in said setting. We are the first to present an MNIST classifier purely trained in MPC that comes within 0.2 percent of the accuracy of the same convolutional neural network trained via plaintext computation. More concretely, we have trained a network with two convolutional and two dense layers to 99.2% accuracy in 3.5 hours (under one hour for 99% accuracy). We have also implemented AlexNet for CIFAR-10, which converges in a few hours. We develop novel protocols for exponentiation and inverse square root. Finally, we present experiments in a range of MPC security models for up to ten parties, both with honest and dishonest majority as well as semi-honest and malicious security.

  匹配依据：MPC: secure multi party computation

  </details>

- **A Parallel Privacy-Preserving Shortest Path Protocol from a Path Algebra Problem**
  2022-07-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.07964)
  Mohammad Anagreh, Peeter Laud

  <details><summary>摘要 / Abstract</summary>

  In this paper, we present a secure multiparty computation (SMC) protocol for single-source shortest distances (SSSD) in undirected graphs, where the location of edges is public, but their length is private. The protocol works in the Arithmetic Black Box (ABB) model on top of the separator tree of the graph, achieving good time complexity if the subgraphs of the graph have small separators (which is the case for e.g. planar graphs); the achievable parallelism is significantly higher than that of classical SSSD algorithms implemented on top of an ABB. We implement our protocol on top of the Sharemind MPC platform, and perform extensive benchmarking over different network environments. We compare our algorithm against the baseline picked from classical algorithms - privacy-preserving Bellman-Ford algorithm (with public edges).

  匹配依据：MPC: secure multiparty computation

  </details>

- **Distributed, Private, Sparse Histograms in the Two-Server Model**
  2022-07-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/920)
  James Bell, Adria Gascon, Badih Ghazi, Ravi Kumar, Pasin Manurangsi, Mariana Raykova, Phillipp Schoppmann

  <details><summary>摘要 / Abstract</summary>

  We consider the computation of sparse, $(\varepsilon, \delta)$-differentially private~(DP) histograms in the two-server model of secure multi-party computation~(MPC), which has recently gained traction in the context of privacy-preserving measurements of aggregate user data. We introduce protocols that enable two semi-honest non-colluding servers to compute histograms over the data held by multiple users, while only learning a private view of the data. Our solution achieves the same asymptotic $\ell_\infty$-error of $O\left(\frac{\log(1/\delta)}{\varepsilon}\right)$ as in the central model of DP, but \emph{without} relying on a trusted curator. The server communication and computation costs of our protocol are independent of the number of histogram buckets, and are linear in the number of users, while the client cost is independent of the number of users, $\varepsilon$, and $\delta$. Its linear dependence on the number of users lets our protocol scale well, which we confirm using microbenchmarks: for a billion users, $\varepsilon = 0.5$, and $\delta = 10^{-11}$, the per-user cost of our protocol is only $1.08$ ms of server computation and $339$ bytes of communication. In contrast, a baseline protocol using garbled circuits only allows up to $10^6$ users, where it requires 600 KB communication per user.

  匹配依据：MPC: garbled circuits, secure multi party computation

  </details>

- **DeTrust-FL: Privacy-Preserving Federated Learning in Decentralized Trust Setting**
  2022-07-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.07779)
  Runhua Xu, Nathalie Baracaldo, Yi Zhou, Ali Anwar, Swanand Kadhe, Heiko Ludwig

  <details><summary>摘要 / Abstract</summary>

  Federated learning has emerged as a privacy-preserving machine learning approach where multiple parties can train a single model without sharing their raw training data. Federated learning typically requires the utilization of multi-party computation techniques to provide strong privacy guarantees by ensuring that an untrusted or curious aggregator cannot obtain isolated replies from parties involved in the training process, thereby preventing potential inference attacks. Until recently, it was thought that some of these secure aggregation techniques were sufficient to fully protect against inference attacks coming from a curious aggregator. However, recent research has demonstrated that a curious aggregator can successfully launch a disaggregation attack to learn information about model updates of a target party. This paper presents DeTrust-FL, an efficient privacy-preserving federated learning framework for addressing the lack of transparency that enables isolation attacks, such as disaggregation attacks, during secure aggregation by assuring that parties&#x27; model updates are included in the aggregated model in a private and secure manner. DeTrust-FL proposes a decentralized trust consensus mechanism and incorporates a recently proposed decentralized functional encryption (FE) scheme in which all parties agree on a participation matrix before collaboratively generating decryption key fragments, thereby gaining control and trust over the secure aggregation process in a decentralized setting. Our experimental evaluation demonstrates that DeTrust-FL outperforms state-of-the-art FE-based secure multi-party aggregation solutions in terms of training time and reduces the volume of data transferred. In contrast to existing approaches, this is achieved without creating any trust dependency on external trusted entities.

  匹配依据：MPC: multi party computation

  </details>

- **All for one and one for all: Fully decentralised privacy-preserving dark pool trading using multi-party computation**
  2022-07-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/923)
  Mariana Botelho da Gama, John Cartlidge, Nigel P. Smart, Younes Talibi Alaoui

  <details><summary>摘要 / Abstract</summary>

  Financial dark pool trading venues are designed to keep pre-trade order information secret so that it cannot be misused by others. However, dark pools are vulnerable to an operator misusing the information in their system. Prior work has used MPC to tackle this problem by assuming that the dark pool is operated by a small set of two or three MPC parties. However, this raises the question of who plays the role of these operating parties and whether this scenario could be applied in the real world. In this work, we implement an MPC-based dark pool trading venue with up to 100 parties. This configuration would allow a real-world implementation where the operating parties are the active participants that trade in the venue (i.e., a ``no operator&#x27;&#x27; model), or where the parties are the main stakeholders of the venue (e.g., members of a non-profit partnership such as Plato). We use AWS cloud to empirically test the performance of the system. Results demonstrate that the system can achieve trading throughput required for some real-world venues, while the cost of hosting the system is negligible compared with the savings expected from guaranteeing no information leakage.

  匹配依据：MPC: multi party computation

  </details>

- **Secure Network Function Computation for Linear Functions -- Part I: Source Security**
  2022-07-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.06757)
  Xuan Guang, Yang Bai, Raymond W. Yeung

  <details><summary>摘要 / Abstract</summary>

  In this paper, we put forward secure network function computation over a directed acyclic network. In such a network, a sink node is required to compute with zero error a target function of which the inputs are generated as source messages at multiple source nodes, while a wiretapper, who can access any one but not more than one wiretap set in a given collection of wiretap sets, is not allowed to obtain any information about a security function of the source messages. The secure computing capacity for the above model is defined as the maximum average number of times that the target function can be securely computed with zero error at the sink node with the given collection of wiretap sets and security function for one use of the network. The characterization of this capacity is in general overwhelmingly difficult. In the current paper, we consider securely computing linear functions with a wiretapper who can eavesdrop any subset of edges up to a certain size r, referred to as the security level, with the security function being the identity function. We first prove an upper bound on the secure computing capacity, which is applicable to arbitrary network topologies and arbitrary security levels. When the security level r is equal to 0, our upper bound reduces to the computing capacity without security consideration. We discover the surprising fact that for some models, there is no penalty on the secure computing capacity compared with the computing capacity without security consideration. We further obtain an equivalent expression of the upper bound by using a graph-theoretic approach, and accordingly we develop an efficient approach for computing this bound. Furthermore, we present a construction of linear function-computing secure network codes and obtain a lower bound on the secure computing capacity.

  匹配依据：MPC: secure computing

  </details>

- **Characterizing and Optimizing End-to-End Systems for Private Inference**
  2022-07-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.07177)
  Karthik Garimella, Zahra Ghodsi, Nandan Kumar Jha, Siddharth Garg, Brandon Reagen

  <details><summary>摘要 / Abstract</summary>

  In two-party machine learning prediction services, the client&#x27;s goal is to query a remote server&#x27;s trained machine learning model to perform neural network inference in some application domain. However, sensitive information can be obtained during this process by either the client or the server, leading to potential collection, unauthorized secondary use, and inappropriate access to personal information. These security concerns have given rise to Private Inference (PI), in which both the client&#x27;s personal data and the server&#x27;s trained model are kept confidential. State-of-the-art PI protocols consist of a pre-processing or offline phase and an online phase that combine several cryptographic primitives: Homomorphic Encryption (HE), Secret Sharing (SS), Garbled Circuits (GC), and Oblivious Transfer (OT). Despite the need and recent performance improvements, PI remains largely arcane today and is too slow for practical use. This paper addresses PI&#x27;s shortcomings with a detailed characterization of a standard high-performance protocol to build foundational knowledge and intuition in the systems community. Our characterization pinpoints all sources of inefficiency -- compute, communication, and storage. In contrast to prior work, we consider inference request arrival rates rather than studying individual inferences in isolation and we find that the pre-processing phase cannot be ignored and is often incurred online as there is insufficient downtime to hide pre-compute latency. Finally, we leverage insights from our characterization and propose three optimizations to address the storage (Client-Garbler), computation (layer-parallel HE), and communication (wireless slot allocation) overheads. Compared to the state-of-the-art PI protocol, these optimizations provide a total PI speedup of 1.8$\times$ with the ability to sustain inference requests up to a 2.24$\times$ greater rate.

  匹配依据：MPC: garbled circuits, oblivious transfer, secret sharing

  </details>

- **Almost-Surely Terminating Asynchronous Byzantine Agreement Against General Adversaries with Optimal Resilience**
  2022-07-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/917)
  Ashish Choudhury

  <details><summary>摘要 / Abstract</summary>

  In this work, we present an almost-surely terminating asynchronous Byzantine agreement (ABA) protocol for $n$ parties. Our protocol requires ${\cal O}(n^2)$ expected time and is secure against a computationally-unbounded malicious (Byzantine) adversary, characterized by a non-threshold adversary structure ${\cal Z}$, which enumerates all possible subsets of potentially corrupt parties. Our protocol has optimal resilience where ${\cal Z}$ satisfies the ${\cal Q}^{(3)}$ condition; i.e. union of no three subsets from ${\cal Z}$ covers all the $n$ parties. To the best of our knowledge, this is the first almost-surely terminating ABA protocol with ${\cal Q}^{(3)}$ condition. Previously, almost-surely terminating ABA protocol is known with non-optimal resilience where ${\cal Z}$ satisfies the ${\cal Q}^{(4)}$ condition; i.e. union of no four subsets from ${\cal Z}$ covers all the $n$ parties. To design our protocol, we present a shunning asynchronous verifiable secret-sharing (SAVSS) scheme with ${\cal Q}^{(3)}$ condition, which is of independent interest.

  匹配依据：MPC: secret sharing

  </details>

- **Capacity Results for the Wiretapped Oblivious Transfer**
  2022-07-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.06363)
  Tianyou Pei, Wei Kang, Nan Liu

  <details><summary>摘要 / Abstract</summary>

  In this paper, we study the problem of the 1-of-2 string oblivious transfer (OT) between Alice and Bob in the presence of a passive eavesdropper Eve. The eavesdropper Eve is not allowed to get any information about the private data of Alice or Bob. When Alice and Bob are honest-but-curious users, we propose a protocol that satisfies $1$-private (neither Alice nor Bob colludes with Eve) OT requirements for the binary erasure symmetric broadcast channel, in which the channel provides dependent erasure patterns to Bob and Eve. We find that when the erasure probabilities satisfy certain conditions, the derived lower and upper bounds on the wiretapped OT capacity meet. Our results generalize and improve upon the results on wiretapped OT capacity by Mishra et al. Finally, we propose a protocol for a larger class of wiretapped channels and derive a lower bound on the wiretapped OT capacity.

  匹配依据：MPC: oblivious transfer

  </details>

- **A New Approach to Post-Quantum Non-Malleability**
  2022-07-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.05861) · [IACR ePrint](https://eprint.iacr.org/2022/907)
  Xiao Liang, Omkant Pandey, Takashi Yamakawa

  <details><summary>摘要 / Abstract</summary>

  We provide the first $\mathit{constant}$-$\mathit{round}$ construction of post-quantum non-malleable commitments under the minimal assumption that $\mathit{post}$-$\mathit{quantum}$ $\mathit{one}$-$\mathit{way}$ $\mathit{functions}$ exist. We achieve the standard notion of non-malleability with respect to commitments. Prior constructions required $Ω(\log^*λ)$ rounds under the same assumption. We achieve our results through a new technique for constant-round non-malleable commitments which is easier to use in the post-quantum setting. The technique also yields an almost elementary proof of security for constant-round non-malleable commitments in the classical setting, which may be of independent interest. When combined with existing work, our results yield the first constant-round quantum-secure multiparty computation for both classical and quantum functionalities $\mathit{in}$ $\mathit{the}$ $\mathit{plain}$ $\mathit{model}$, under the $\mathit{polynomial}$ hardness of quantum fully-homomorphic encryption and quantum learning with errors.

  匹配依据：MPC: secure multiparty computation

  </details>

- **SIMC 2.0: Improved Secure ML Inference Against Malicious Clients**
  2022-07-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.04637)
  Guowen Xu, Xingshuo Han, Tianwei Zhang, Shengmin Xu, Jianting Ning, Xinyi Huang, Hongwei Li, Robert H. Deng

  <details><summary>摘要 / Abstract</summary>

  In this paper, we study the problem of secure ML inference against a malicious client and a semi-trusted server such that the client only learns the inference output while the server learns nothing. This problem is first formulated by Lehmkuhl \textit{et al.} with a solution (MUSE, Usenix Security&#x27;21), whose performance is then substantially improved by Chandran et al.&#x27;s work (SIMC, USENIX Security&#x27;22). However, there still exists a nontrivial gap in these efforts towards practicality, giving the challenges of overhead reduction and secure inference acceleration in an all-round way. We propose SIMC 2.0, which complies with the underlying structure of SIMC, but significantly optimizes both the linear and non-linear layers of the model. Specifically, (1) we design a new coding method for homomorphic parallel computation between matrices and vectors. It is custom-built through the insight into the complementarity between cryptographic primitives in SIMC. As a result, it can minimize the number of rotation operations incurred in the calculation process, which is very computationally expensive compared to other homomorphic operations e.g., addition, multiplication). (2) We reduce the size of the garbled circuit (GC) (used to calculate nonlinear activation functions, e.g., ReLU) in SIMC by about two thirds. Then, we design an alternative lightweight protocol to perform tasks that are originally allocated to the expensive GCs. Compared with SIMC, our experiments show that SIMC 2.0 achieves a significant speedup by up to $17.4\times $ for linear layer computation, and at least $1.3\times$ reduction of both the computation and communication overheads in the implementation of non-linear layers under different data dimensions. Meanwhile, SIMC 2.0 demonstrates an encouraging runtime boost by $2.3\sim 4.3\times$ over SIMC on different state-of-the-art ML models.

  匹配依据：MPC: garbled circuit

  </details>

- **Privacy-preserving Decentralized Deep Learning with Multiparty Homomorphic Encryption**
  2022-07-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.04604)
  Guowen Xu, Guanlin Li, Shangwei Guo, Tianwei Zhang, Hongwei Li

  <details><summary>摘要 / Abstract</summary>

  Decentralized deep learning plays a key role in collaborative model training due to its attractive properties, including tolerating high network latency and less prone to single-point failures. Unfortunately, such a training mode is more vulnerable to data privacy leaks compared to other distributed training frameworks. Existing efforts exclusively use differential privacy as the cornerstone to alleviate the data privacy threat. However, it is still not clear whether differential privacy can provide a satisfactory utility-privacy trade-off for model training, due to its inherent contradictions. To address this problem, we propose D-MHE, the first secure and efficient decentralized training framework with lossless precision. Inspired by the latest developments in the homomorphic encryption technology, we design a multiparty version of Brakerski-Fan-Vercauteren (BFV), one of the most advanced cryptosystems, and use it to implement private gradient updates of users&#x27;local models. D-MHE can reduce the communication complexity of general Secure Multiparty Computation (MPC) tasks from quadratic to linear in the number of users, making it very suitable and scalable for large-scale decentralized learning systems. Moreover, D-MHE provides strict semantic security protection even if the majority of users are dishonest with collusion. We conduct extensive experiments on MNIST and CIFAR-10 datasets to demonstrate the superiority of D-MHE in terms of model accuracy, computation and communication cost compared with existing schemes.

  匹配依据：MPC: secure multiparty computation

  </details>

- **MPC for Tech Giants (GMPC): Enabling Gulliver and the Lilliputians to Cooperate Amicably**
  2022-07-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.05047) · [IACR ePrint](https://eprint.iacr.org/2022/902)
  Bar Alon, Moni Naor, Eran Omri, Uri Stemmer

  <details><summary>摘要 / Abstract</summary>

  In the current digital world, large organizations (sometimes referred to as tech giants) provide service to extremely large numbers of users. The service provider is often interested in computing various data analyses over the private data of its users, which in turn have their incentives to cooperate, but do not necessarily trust the service provider. In this work, we introduce the \emph{Gulliver multi-party computation model} (GMPC) to realistically capture the above scenario. The GMPC model considers a single highly powerful party, called the {\em server} or {\em Gulliver}, that is connected to $n$ users over a star topology network (alternatively formulated as a full network, where the server can block any message). The users are significantly less powerful than the server, and, in particular, should have both computation and communication complexities that are polylogarithmic in $n$. Protocols in the GMPC model should be secure against malicious adversaries that may corrupt a subset of the users and/or the server. Designing protocols in the GMPC model is a delicate task, since users can only hold information about $\operatorname{polylog}(n)$ other users (and, in particular, can only communicate with $\operatorname{polylog}(n)$ other users). In addition, the server can block any message between any pair of honest parties. Thus, reaching an agreement becomes a challenging task. Nevertheless, we design generic protocols in the GMPC model, assuming that at most $\alpha&lt;1/8$ fraction of the users may be corrupted (in addition to the server). Our main contribution is a variant of Feige&#x27;s committee election protocol [FOCS 1999] that is secure in the GMPC model. Given this tool we show: 1. Assuming fully homomorphic encryption (FHE), any computationally efficient function with $O\left(n\cdot\operatorname{polylog}(n)\right)$-size output can be securely computed in the GMPC model. 2. Any function that can be computed by a circuit of $O(\operatorname{polylog}(n))$ depth, $O\left(n\cdot\operatorname{polylog}(n)\right)$ size, and bounded fan-in and fan-out can be securely computed in the GMPC model {\em without assuming FHE}. 3. In particular, {\em sorting} can be securely computed in the GMPC model without assuming FHE. This has important applications for the {\emph shuffle model of differential privacy}, and resolves an open question of Bell et al. [CCS 2020].

  匹配依据：MPC: multi party computation

  </details>

- **Deep Learning-Based Medical Diagnostic Services: A Secure, Lightweight, and Accurate Realization**
  2022-07-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/899)
  Xiaoning Liu, Yifeng Zheng, Xingliang Yuan, Xun Yi

  <details><summary>摘要 / Abstract</summary>

  In this paper, we propose CryptMed, a system framework that enables medical service providers to offer secure, lightweight, and accurate medical diagnostic service to their customers via an execution of neural network inference in the ciphertext domain. CryptMed ensures the privacy of both parties with cryptographic guarantees. Our technical contributions include: 1) presenting a secret sharing based inference protocol that can well cope with the commonly-used linear and non-linear NN layers; 2) devising an optimized secure comparison function that can efficiently support comparison-based activation functions in NN architectures; 3) constructing a suite of secure smooth functions built on precise approximation approaches for accurate medical diagnoses. We evaluate CryptMed on 6 neural network architectures across a wide range of non-linear activation functions over two benchmark and four real-world medical datasets. We comprehensively compare our system with prior art in terms of end-to-end service workload and prediction accuracy. Our empirical results demonstrate that CryptMed achieves up to respectively $413\times$, $19\times$, and $43\times$ bandwidth savings for MNIST, CIFAR-10, and medical applications compared with prior art. For the smooth activation based inference, the best choice of our proposed approximations preserve the precision of original functions, with less than 1.2\% accuracy loss and could enhance the precision due to the newly introduced activation function family.

  匹配依据：MPC: secret sharing

  </details>

- **Round-Optimal Black-Box Protocol Compilers**
  2022-07-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/887)
  Yuval Ishai, Dakshita Khurana, Amit Sahai, Akshayaram Srinivasan

  <details><summary>摘要 / Abstract</summary>

  We give black-box, round-optimal protocol compilers from semi-honest security to malicious security in the Random Oracle Model (ROM) and in the 1-out-of-2 oblivious transfer (OT) correlations model. We use our compilers to obtain the following black-box constructions of general-purpose protocols for secure computation tolerating static, malicious corruptions of all-but-one participants: \begin{itemize} \item A two-round, two-party protocol in the random oracle model, making black-box use of a two-round semi-honest secure protocol. Prior to our work, such a result was not known even for special functionalities such as OT. As an application, we get efficient constructions of two-round malicious OT/OLE in the random oracle model based on a black-box use of two-round semi-honest OT/OLE. \item A three-round multiparty protocol in the random oracle model, making a black-box use of two-round semi-honest OT. This protocol matches a known round complexity lower bound due to Applebaum et al. (ITCS 2020) and is based on a minimal cryptographic primitive. \item A two-round multiparty protocol in the OT correlations model, making a black-box use of a semi-malicious protocol. This improves over a similar protocol of the authors (Crypto 2021) by eliminating an adaptive security requirement and replacing nonstandard multiparty OT correlations by standard ones. As an application, we get 2-round protocols for arithmetic branching programs that make a black-box use of the underlying field. \end{itemize} As a contribution of independent interest, we provide a new variant of the IPS compiler (Ishai, Prabhakaran and Sahai, Crypto 2008) in the two-round setting, where we relax requirements on the IPS ``inner protocol&#x27;&#x27; by strengthening the ``outer protocol&#x27;&#x27;.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **Contact Discovery in Mobile Messengers: Low-cost Attacks, Quantitative Analyses, and Efficient Mitigations**
  2022-07-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/875)
  Christoph Hagen, Christian Weinert, Christoph Sendner, Alexandra Dmitrienko, Thomas Schneider

  <details><summary>摘要 / Abstract</summary>

  Contact discovery allows users of mobile messengers to conveniently connect with people in their address book. In this work, we demonstrate that severe privacy issues exist in currently deployed contact discovery methods and propose suitable mitigations. Our study of three popular messengers (WhatsApp, Signal, and Telegram) shows that large-scale crawling attacks are (still) possible. Using an accurate database of mobile phone number prefixes and very few resources, we queried 10% of US mobile phone numbers for WhatsApp and 100% for Signal. For Telegram we find that its API exposes a wide range of sensitive information, even about numbers not registered with the service. We present interesting (cross-messenger) usage statistics, which also reveal that very few users change the default privacy settings. Furthermore, we demonstrate that currently deployed hashing-based contact discovery protocols are severely broken by comparing three methods for efficient hash reversal. Most notably, we show that with the password cracking tool &quot;JTR&quot; we can iterate through the entire world-wide mobile phone number space in &lt;150s on a consumer-grade GPU. We also propose a significantly improved rainbow table construction for non-uniformly distributed input domains that is of independent interest. Regarding mitigations, we most notably propose two novel rate-limiting schemes: our incremental contact discovery for services without server-side contact storage strictly improves over Signal&#x27;s current approach while being compatible with private set intersection, whereas our differential scheme allows even stricter rate limits at the overhead for service providers to store a small constant-size state that does not reveal any contact information.

  匹配依据：MPC: private set intersection

  </details>

- **A New Approach to the Constant-Round Re-encryption Mix-Net**
  2022-07-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/877)
  Myungsun Kim

  <details><summary>摘要 / Abstract</summary>

  The re-encryption mix-net (RMN) is a basic cryptographic tool that is widely used in the privacy protection domain and requires anonymity support; for example, it is used in electronic voting, web browsing, and location systems. To protect information about the relationship between senders and messages, a number of mix servers in RMNs shuffle and forward a list of input ciphertexts in a cascading manner. The output of the last mix server is decrypted to yield the set of original messages. The main downside of this approach is that the mixing process requires a number of rounds that is linear in the number of mix servers. This implies that a long round delay would cause network latency, which can dominate local computational latencies. To minimize the effect of network latency, RMN protocols with constant round complexity are more desirable. In this work, we propose a new RMN protocol that runs in $O(1)$ rounds in the number of mix servers and that UC-realizes a hybrid model with access to some functionalities for secure communication and zero-knowledge proof (ZKP). Interestingly, because our protocol does not require a ZKP protocol for a verifiable shuffle, we also achieve a considerable efficiency gain in terms of computation cost. Our main tools are secret sharing and an ElGamal encryption that is extended in the sense that it works on a multiplicative group under field extension. Importantly, this extended ElGamal encryption scheme acquires a new capability: it can efficiently decompose a decrypted message into unique values. We provide a detailed report on the theoretical performance and security analysis of this method.

  匹配依据：MPC: secret sharing

  </details>

- **Scooby: Improved Multi-Party Homomorphic Secret Sharing Based on FHE**
  2022-07-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/862)
  Ilaria Chillotti, Emmanuela Orsini, Peter Scholl, Nigel Paul Smart, Barry Van Leeuwen

  <details><summary>摘要 / Abstract</summary>

  We present new constructions of multi-party homomorphic secret sharing (HSS) based on a new primitive that we call homomorphic encryption with decryption to shares (HEDS). Our first construction, which we call Scooby, is based on many popular fully homomorphic encryption (FHE) schemes with a linear decryption property. Scooby achieves an $n$-party HSS for general circuits with complexity $O(|F| + \log n)$, as opposed to $O(n^2 \cdot |F|)$ for the prior best construction based on multi-key FHE. Scooby can be based on (ring)-LWE with a super-polynomial modulus-to-noise ratio. In our second construction, Scrappy, assuming any generic FHE plus HSS for NC1-circuits, we obtain a HEDS scheme which does not require a super-polynomial modulus. While these schemes all require FHE, in another instantiation, Shaggy, we show how in some cases it is possible to obtain multi-party HSS without FHE, for a small number of parties and constant-degree polynomials. Finally, we show that our Scooby scheme can be adapted to use multi-key fully homomorphic encryption, giving more efficient spooky encryption and setup-free HSS. This latter scheme, Casper, if concretely instantiated with a B/FV-style multi-key FHE scheme, for functions $F$ which do not require bootstrapping, gives an HSS complexity of $O(n \cdot |F| + n^2 \cdot \log n)$.

  匹配依据：MPC: secret sharing

  </details>

- **Effect of Homomorphic Encryption on the Performance of Training Federated Learning Generative Adversarial Networks**
  2022-07-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.00263)
  Ignjat Pejic, Rui Wang, Kaitai Liang

  <details><summary>摘要 / Abstract</summary>

  A Generative Adversarial Network (GAN) is a deep-learning generative model in the field of Machine Learning (ML) that involves training two Neural Networks (NN) using a sizable data set. In certain fields, such as medicine, the training data may be hospital patient records that are stored across different hospitals. The classic centralized approach would involve sending the data to a centralized server where the model would be trained. However, that would involve breaching the privacy and confidentiality of the patients and their data, which would be unacceptable. Therefore, Federated Learning (FL), an ML technique that trains ML models in a distributed setting without data ever leaving the host device, would be a better alternative to the centralized option. In this ML technique, only parameters and certain metadata would be communicated. In spite of that, there still exist attacks that can infer user data using the parameters and metadata. A fully privacy-preserving solution involves homomorphically encrypting (HE) the data communicated. This paper will focus on the performance loss of training an FL-GAN with three different types of Homomorphic Encryption: Partial Homomorphic Encryption (PHE), Somewhat Homomorphic Encryption (SHE), and Fully Homomorphic Encryption (FHE). We will also test the performance loss of Multi-Party Computations (MPC), as it has homomorphic properties. The performances will be compared to the performance of training an FL-GAN without encryption as well. Our experiments show that the more complex the encryption method is, the longer it takes, with the extra time taken for HE is quite significant in comparison to the base case of FL.

  匹配依据：MPC: mpc (context)

  </details>

- **Split Two-Tower Model for Efficient and Privacy-Preserving Cross-device Federated Recommendation**
  2022-06-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.13715)
  Jiangcheng Qin, Baisong Liu, Xueyuan Zhang, Jiangbo Qian

  <details><summary>摘要 / Abstract</summary>

  Federated Recommendation can mitigate the systematical privacy risks of traditional recommendation since it allows the model training and online inferring without centralized user data collection. Most existing works assume that all user devices are available and adequate to participate in the Federated Learning. However, in practice, the complex recommendation models designed for accurate prediction and massive item data cause a high computation and communication cost to the resource-constrained user device, resulting in poor performance or training failure. Therefore, how to effectively compress the computation and communication overhead to achieve efficient federated recommendations across ubiquitous mobile devices remains a significant challenge. This paper introduces split learning into the two-tower recommendation models and proposes STTFedRec, a privacy-preserving and efficient cross-device federated recommendation framework. STTFedRec achieves local computation reduction by splitting the training and computation of the item model from user devices to a performance-powered server. The server with the item model provides low-dimensional item embeddings instead of raw item data to the user devices for local training and online inferring, achieving server broadcast compression. The user devices only need to perform similarity calculations with cached user embeddings to achieve efficient online inferring. We also propose an obfuscated item request strategy and multi-party circular secret sharing chain to enhance the privacy protection of model training. The experiments conducted on two public datasets demonstrate that STTFedRec improves the average computation time and communication size of the baseline models by about 40 times and 42 times in the best-case scenario with balanced recommendation accuracy.

  匹配依据：MPC: secret sharing

  </details>

- **Formal Verification of Arithmetic Masking in Hardware and Software**
  2022-06-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/849)
  Barbara Gigerl, Robert Primas, Stefan Mangard

  <details><summary>摘要 / Abstract</summary>

  Masking is a popular secret-sharing technique that is used to protect cryptographic implementations against physical attacks like differential power analysis. So far, most research in this direction has focused on finding efficient Boolean masking schemes for well-known symmetric cryptographic algorithms like AES and Keccak. However, especially with the advent of post-quantum cryptography (PQC), arithmetic masking has received increasing attention from the research community. In practice, many PQC algorithms require a combination of arithmetic and Boolean masking, which makes the search for secure and efficient conversion algorithms between these domains (A2B/B2A) an interesting but very challenging research topic. While there already exist lots of tools that can help with the formal verification of Boolean masked implementations, the same cannot be said about arithmetic masking and accompanying mask conversion algorithms. In this work, we demonstrate the first formal verification approach for (any-order) Boolean and arithmetic masking which can be applied to both hardware and software, while considering side-effects such as glitches and transitions. First, we show how a formal verification approach for Boolean masking can be used in the context of arithmetic masking such that we can verify A2B/B2A conversions for arbitrary masking orders. We investigate various conversion algorithms in hardware and software, and point out several new findings such as glitch-based issues for straightforward implementations of [CGV14]-A2B in hardware, transition-based leakage in Goubin-A2B in software, and more general implementation pitfalls when utilizing common optimization techniques in PQC. We provide the first formal analysis of table-based A2Bs from a probing security perspective and point out that they might not be easy to implement securely on processors that use of memory buffers or caches.

  匹配依据：MPC: secret sharing

  </details>

- **MPClan: Protocol Suite for Privacy-Conscious Computations**
  2022-06-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.12224) · [IACR ePrint](https://eprint.iacr.org/2022/675)
  Nishat Koti, Shravani Patil, Arpita Patra, Ajith Suresh

  <details><summary>摘要 / Abstract</summary>

  The growing volumes of data being collected and its analysis to provide better services are creating worries about digital privacy. To address privacy concerns and give practical solutions, the literature has relied on secure multiparty computation. However, recent research has mostly focused on the small-party honest-majority setting of up to four parties, noting efficiency concerns. In this work, we extend the strategies to support a larger number of participants in an honest-majority setting with efficiency at the center stage. Cast in the preprocessing paradigm, our semi-honest protocol improves the online complexity of the decade-old state-of-the-art protocol of Damgård and Nielson (CRYPTO&#x27;07). In addition to having an improved online communication cost, we can shut down almost half of the parties in the online phase, thereby saving up to 50$\%$ in the system&#x27;s operational costs. Our maliciously secure protocol also enjoys similar benefits and requires only half of the parties, except for one-time verification, towards the end. To showcase the practicality of the designed protocols, we benchmark popular applications such as deep neural networks, graph neural networks, genome sequence matching, and biometric matching using prototype implementations. Our improved protocols aid in bringing up to 60-80$\%$ savings in monetary cost over prior work.

  匹配依据：MPC: secure multiparty computation

  </details>

- **FLVoogd: Robust And Privacy Preserving Federated Learning**
  2022-06-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2207.00428)
  Yuhang Tian, Rui Wang, Yanqi Qiao, Emmanouil Panaousis, Kaitai Liang

  <details><summary>摘要 / Abstract</summary>

  In this work, we propose FLVoogd, an updated federated learning method in which servers and clients collaboratively eliminate Byzantine attacks while preserving privacy. In particular, servers use automatic Density-based Spatial Clustering of Applications with Noise (DBSCAN) combined with S2PC to cluster the benign majority without acquiring sensitive personal information. Meanwhile, clients build dual models and perform test-based distance controlling to adjust their local models toward the global one to achieve personalizing. Our framework is automatic and adaptive that servers/clients don&#x27;t need to tune the parameters during the training. In addition, our framework leverages Secure Multi-party Computation (SMPC) operations, including multiplications, additions, and comparison, where costly operations, like division and square root, are not required. Evaluations are carried out on some conventional datasets from the image classification field. The result shows that FLVoogd can effectively reject malicious uploads in most scenarios; meanwhile, it avoids data leakage from the server-side.

  匹配依据：MPC: secure multi party computation

  </details>

- **Covert Authentication from Lattices**
  2022-06-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/835)
  Rajendra Kumar, Khoa Nguyen

  <details><summary>摘要 / Abstract</summary>

  Introduced by von Ahn et al. (STOC’05), covert two-party computation is an appealing cryptographic primitive that allows Al- ice and Bob to securely evaluate a function on their secret inputs in a steganographic manner, i.e., even the existence of a computation is oblivious to each party - unless the output of the function is favourable to both. A prominent form of covert computation is covert authentica- tion, where Alice and Bob want to authenticate each other based on their credentials, in a way such that the party who does not hold the appro- priate credentials cannot pass the authentication and is even unable to distinguish a protocol instance from random noise. Jarecki (PKC’14) put forward a blueprint for designing covert authentication protocols, which relies on a covert conditional key-encapsulation mechanism, an identity escrow scheme, a covert commitment scheme and a Σ-protocol satisfying several specific properties. He also proposed an instantiation based on the Strong RSA, the Decisional Quadratic Residuosity and the Decisional Diffie-Hellman assumptions. Despite being very efficient, Jarecki’s con- struction is vulnerable against quantum adversaries. In fact, designing covert authentication protocols from post-quantum assumptions remains an open problem. In this work, we present several contributions to the study of covert authentication protocols. First, we identify several technical obstacles in realizing Jarecki’s blueprint under lattice assumptions. To remedy, we then provide a new generic construction of covert Mutual Authentica- tion (MA) protocol, that departs from given blueprint and that requires somewhat weaker properties regarding the employed cryptographic ingre- dients. Next, we instantiate our generic construction based on commonly used lattice assumptions. The protocol is proven secure in the random oracle model, assuming the hardness of the Module Learning With Errors (M-LWE) and Module Short Integer Solution (M-SIS) and the NTRU problems, and hence, is potentially quantum-safe. In the process, we also develop an approximate smooth projective hashing function associated with a covert commitment, based on the M-LWE assumption. We then demonstrate that this new ingredient can be smoothly combined with existing lattice-based techniques to yield a secure covert MA scheme.

  匹配依据：MPC: two party computation

  </details>

- **Authenticated Garbling from Simple Correlations**
  2022-06-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/836)
  Samuel Dittmer, Yuval Ishai, Steve Lu, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  We revisit the problem of constant-round malicious secure two-party computation by considering the use of simple correlations, namely sources of correlated randomness that can be securely generated with sublinear communication complexity and good concrete efficiency. The current state-of-the-art protocol of Katz et al. (Crypto 2018) achieves malicious security by realizing a variant of the authenticated garbling functionality of Wang et al. (CCS 2017). Given oblivious transfer correlations, the communication cost of this protocol (with 40 bits of statistical security) is comparable to roughly $10$ garbled circuits (GCs). This protocol inherently requires more than 2 rounds of interaction. In this work, we use other kinds of simple correlations to realize the authenticated garbling functionality with better efficiency. Concretely, we get the following reduced costs in the random oracle model: - Using variants of both vector oblivious linear evaluation (VOLE) and multiplication triples (MT), we reduce the cost to $1.31$ GCs. - Using only variants of VOLE, we reduce the cost to $2.25$ GCs. - Using only variants of MT, we obtain a non-interactive (i.e., 2-message) protocol with cost comparable to $8$ GCs. Finally, we show that by using recent constructions of pseudorandom correlation generators (Boyle et al., CCS 2018, Crypto 2019, 2020), the simple correlations consumed by our protocols can be securely realized without forming an efficiency bottleneck.

  匹配依据：MPC: garbled circuits, oblivious transfer, secure two party computation

  </details>

- **Towards End-to-End Private Automatic Speaker Recognition**
  2022-06-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.11750)
  Francisco Teixeira, Alberto Abad, Bhiksha Raj, Isabel Trancoso

  <details><summary>摘要 / Abstract</summary>

  The development of privacy-preserving automatic speaker verification systems has been the focus of a number of studies with the intent of allowing users to authenticate themselves without risking the privacy of their voice. However, current privacy-preserving methods assume that the template voice representations (or speaker embeddings) used for authentication are extracted locally by the user. This poses two important issues: first, knowledge of the speaker embedding extraction model may create security and robustness liabilities for the authentication system, as this knowledge might help attackers in crafting adversarial examples able to mislead the system; second, from the point of view of a service provider the speaker embedding extraction model is arguably one of the most valuable components in the system and, as such, disclosing it would be highly undesirable. In this work, we show how speaker embeddings can be extracted while keeping both the speaker&#x27;s voice and the service provider&#x27;s model private, using Secure Multiparty Computation. Further, we show that it is possible to obtain reasonable trade-offs between security and computational cost. This work is complementary to those showing how authentication may be performed privately, and thus can be considered as another step towards fully private automatic speaker recognition.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Quadratic Multiparty Randomized Encodings Beyond Honest Majority and Their Applications**
  2022-06-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/813)
  Benny Applebaum, Yuval Ishai, Or Karni, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  Multiparty randomized encodings (Applebaum, Brakerski, and Tsabary, SICOMP 2021) reduce the task of securely computing a complicated multiparty functionality $f$ to the task of securely computing a simpler functionality $g$. The reduction is non-interactive and preserves information-theoretic security against a passive (semi-honest) adversary, also referred to as privacy. The special case of a degree-2 encoding $g$ (2MPRE) has recently found several applications to secure multiparty computation (MPC) with either information-theoretic security or making black-box access to cryptographic primitives. Unfortunately, as all known constructions are based on information-theoretic MPC protocols in the plain model, they can only be private with an honest majority. In this paper, we break the honest-majority barrier and present the first construction of general 2MPRE that remains secure in the presence of a dishonest majority. Our construction encodes every $n$-party functionality $f$ by a 2MPRE that tolerates at most $t=\lfloor 2n/3\rfloor$ passive corruptions. We derive several applications including: (1) The first non-interactive client-server MPC protocol with perfect privacy against any coalition of a minority of the servers and up to $t$ of the $n$ clients; (2) Completeness of 3-party functionalities under non-interactive $t$-private reductions; and (3) A single-round $t$-private reduction from general-MPC to an ideal oblivious transfer (OT). These positive results partially resolve open questions that were posed in several previous works. We also show that $t$-private 2MPREs are necessary for solving (2) and (3), thus establishing new equivalence theorems between these three notions. Finally, we present a new approach for constructing fully-private 2MPREs based on multi-round protocols in the OT-hybrid model that achieve \emph{perfect privacy} against active attacks. Moreover, by slightly restricting the power of the active adversary, we derive an equivalence between these notions. This forms a surprising, and quite unique, connection between a non-interactive passively-private primitive to an interactive actively-private primitive.

  匹配依据：MPC: oblivious transfer, secure multiparty computation

  </details>

- **Multi-party Secure Broad Learning System for Privacy Preserving**
  2022-06-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.11133)
  Xiao-Kai Cao, Chang-Dong Wang, Jian-Huang Lai, Qiong Huang, C. L. Philip Chen

  <details><summary>摘要 / Abstract</summary>

  Multi-party learning is an indispensable technique for improving the learning performance via integrating data from multiple parties. Unfortunately, directly integrating multi-party data would not meet the privacy preserving requirements. Therefore, Privacy-Preserving Machine Learning (PPML) becomes a key research task in multi-party learning. In this paper, we present a new PPML method based on secure multi-party interactive protocol, namely Multi-party Secure Broad Learning System (MSBLS), and derive security analysis of the method. The existing PPML methods generally cannot simultaneously meet multiple requirements such as security, accuracy, efficiency and application scope, but MSBLS achieves satisfactory results in these aspects. It uses interactive protocol and random mapping to generate the mapped features of data, and then uses efficient broad learning to train neural network classifier. This is the first privacy computing method that combines secure multi-party computing and neural network. Theoretically, this method can ensure that the accuracy of the model will not be reduced due to encryption, and the calculation speed is very fast. We verify this conclusion on three classical datasets.

  匹配依据：MPC: secure multi party computing

  </details>

- **MPC for Group Reconstruction Circuits**
  2022-06-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/821)
  Lúcás Críostóir Meier

  <details><summary>摘要 / Abstract</summary>

  In this work, we generalize threshold Schnorr signatures, ElGamal encryption, and a wide variety of other functionalities, using a novel formalism of group reconstruction circuits (GRC)s. We construct a UC secure MPC protocol for computing these circuits on secret shared inputs, even in the presence of malicious parties. Applied to concrete circuits, our protocol yields threshold signature and encryption schemes with similar round complexity and concrete eﬃciency to functionality-speciﬁc protocols. Our formalism also generalizes to other functionalities, such as polynomial commitments and openings.

  匹配依据：MPC: mpc (context)

  </details>

- **Multi-key and Multi-input Predicate Encryption from Learning with Errors**
  2022-06-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/806)
  Danilo Francati, Daniele Friolo, Giulio Malavolta, Daniele Venturi

  <details><summary>摘要 / Abstract</summary>

  We put forward two natural generalizations of predicate encryption (PE), dubbed multi-key and multi-input PE. More in details, our contributions are threefold. - Definitions. We formalize security of multi-key PE and multi-input PE following the standard indistinguishability paradigm, and modeling security both against malicious senders (i.e., corruption of encryption keys) and malicious receivers (i.e., collusions). - Constructions. We construct adaptively secure multi-key and multi-input PE supporting the conjunction of poly-many arbitrary single-input predicates, assuming the sub-exponential hardness of the learning with errors (LWE) problem. - Applications. We show that multi-key and multi-input PE for expressive enough predicates suffices for interesting cryptographic applications, including non-interactive multi-party computation (NI-MPC) and matchmaking encryption (ME). In particular, plugging in our constructions of multi-key and multi-input PE, under the sub-exponential LWE assumption, we obtain the first ME supporting arbitrary policies with unbounded collusions, as well as robust (resp. non-robust) NI-MPC for so-called all-or-nothing functions satisfying a non-trivial notion of reusability and supporting a constant (resp. polynomial) number of parties. Prior to our work, both of these applications required much heavier tools such as indistinguishability obfuscation or compact functional encryption.

  匹配依据：MPC: multi party computation

  </details>

- **BarnOwl: Secure Comparisons using Silent Pseudorandom Correlation Generators**
  2022-06-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/800)
  Sameer Wagh

  <details><summary>摘要 / Abstract</summary>

  Recent advances in function secret sharing (FSS) have led to new possibilities in multi-party computation in the pre-processing model. Silent Pseudorandom Correlation Generators (Crypto &#x27;19, CCS &#x27;19, CCS &#x27;19, CCS &#x27;20) have demonstrated the ability to generate large quantities of pre-processing material such as oblivious transfers and Beaver triples through a non-interactive offline phase (with an initial set-up). However, there has been limited protocols for pre-processing material such as doubly authenticated bits (daBits, IndoCrypt&#x27;19) and extended doubly authenticated bits (edaBits, Crypto &#x27;20) which are critical for state-of-the-art secure comparison protocols over arithmetic secret sharing. In this work, we propose new protocols in a 3-party computation model for these two cryptographic primitives -- daBits and edaBits. We explore how advances in silent PCGs can be used to construct efficient protocols for daBits and edaBits. Our protocols are secure against a single corruption in both the semi-honest and malicious security models. Our contributions can be summarized as follows: (1) New constant round protocols for generating daBits and edaBits. We achieve this by constructing an efficient 3-party oblivious transfer protocol (using just 2 rounds of computation) and using it to build efficient protocols for daBit and edaBit generation. (2) We extend the above semi-honest protocol to achieve malicious security against an honest majority. We use a standard cut-and-choose approach for this. This improves the round complexity of prior edaBit protocols from O(log2 l) to a constant, where l is the bit-length of the inputs. (3) Finally, to understand when the above protocols provide concrete efficiency, we implement and benchmark the performance of our protocols against state-of-the-art implementation of these primitives in MP-SDPZ. Our protocols improve the throughput of daBit generation by up to 10x in the LAN setting and 5x in the WAN setting. Comparing the performance of edaBit generation, our protocols achieve 4x higher throughput in the LAN setting and 32x higher throughput in the WAN setting. It is known that silent PCGs are compute intense and thus the performance of these new protocols can further be improved using works such as CryptGPU (S\&amp;P &#x27;21), Piranha (USENIX &#x27;22) that significantly improve the local computation in MPC protocols.

  匹配依据：MPC: 3 party computation, multi party computation, oblivious transfer, secret sharing

  </details>

- **A 2.1 KHz Zero-Knowledge Processor with BubbleRAM**
  2022-06-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/809)
  David Heath, Vladimir Kolesnikov

  <details><summary>摘要 / Abstract</summary>

  Zero-Knowledge (ZK) proofs (ZKP) are foundational in cryptography. Most recent ZK research focuses on non-interactive proofs (NIZK) of small statements, useful in blockchain scenarios. Another line, and our focus, instead targets proofs of large statements that are useful, e.g., in proving properties of programs in ZK. We specify a zero-knowledge processor that executes arbitrary programs written in a simple instruction set and proves in ZK the correctness of the execution. Such an approach is well-suited for constructing ZK proofs of large statements as it efficiently supports complex programming constructs, such as loops and RAM access. We propose several novel ZK improvements that make our approach concretely efficient: (1) an efficient arithmetic representation with conversions to/from Boolean, (2) an efficient read-only memory that uses $2 \log n$ OTs per access, and (3) an efficient read-write memory, BubbleRAM, which uses $1/2 \log^2 n$ OTs per access. BubbleRAM beats linear scan for RAM of size &gt; 3 elements! Prior ZK systems used generic ORAM costing orders of magnitude more. We cast our system as a garbling scheme that can be plugged into the ZK protocol of [Jawurek et al, CCS’13]. Put together, our system is concretely efficient: for a processor instantiated with 512KB of main memory, each processor cycle costs 24KB of communication. We implemented our approach in C++. On a 1Gbps LAN, our implementation realizes a 2.1KHz processor.

  匹配依据：MPC: garbling scheme

  </details>

- **One Hot Garbling**
  2022-06-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/798)
  David Heath, Vladimir Kolesnikov

  <details><summary>摘要 / Abstract</summary>

  Garbled Circuit (GC) is the main practical 2PC technique, yet despite great interest in its performance, GC notoriously resists improvement. Essentially, we only know how to evaluate GC functions gate-by-gate using encrypted truth tables; given input labels, the GC evaluator decrypts the corresponding output label. Interactive protocols enjoy more sophisticated techniques. For example, we can expose to a party a (masked) private value. The party can then perform useful local computation and feed the resulting cleartext value back into the MPC. Such techniques are not known to work for GC. We show that it is, in fact, possible to improve GC efficiency, while keeping its round complexity, by exposing masked private values to the evaluator. Our improvements use garbled one-hot encodings of values. By using this encoding we improve a number of interesting functions, e.g., matrix multiplication, integer multiplication, field element multiplication, field inverses and AES S-Boxes, integer exponents, and more. We systematize our approach by providing a framework for designing such GC modules. Our constructions are concretely efficient. E.g., we improve binary matrix multiplication inside GC by more than $6\times$ in terms of communication and by more than $4\times$ in terms of WAN wall-clock time. Our improvement circumvents an important GC lower bound and may open GC to further improvement.

  匹配依据：MPC: garbled circuit

  </details>

- **LLAMA: A Low Latency Math Library for Secure Inference**
  2022-06-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/793)
  Kanav Gupta, Deepak Kumaraswamy, Nishanth Chandran, Divya Gupta

  <details><summary>摘要 / Abstract</summary>

  Secure machine learning (ML) inference can provide meaningful privacy guarantees to both the client (holding sensitive input) and the server (holding sensitive weights of the ML model) while realizing inference-as-a-service. Although many specialized protocols exist for this task, including those in the preprocessing model (where a majority of the overheads are moved to an input independent offline phase), they all still suffer from large online complexity. Specifically, the protocol phase that executes once the parties know their inputs, has high communication, round complexity, and latency. Function Secret Sharing (FSS) based techniques offer an attractive solution to this in the trusted dealer model (where a dealer provides input independent correlated randomness to both parties), and 2PC protocols obtained based on these techniques have a very lightweight online phase. Unfortunately, current FSS-based 2PC works (AriaNN, PoPETS 2022; Boyle et al. Eurocrypt 2021; Boyle et al. TCC 2019) fall short of providing a complete solution to secure inference. First, they lack support for math functions (e.g., sigmoid, and reciprocal square root) and hence, are insufficient for a large class of inference algorithms (e.g. recurrent neural networks). Second, they restrict all values in the computation to be of the same bitwidth and this prevents them from benefitting from efficient float-to-fixed converters such as Tensorflow Lite that crucially use low bitwidth representations and mixed bitwidth arithmetic. In this work, we present LLAMA -- an end-to-end, FSS based, secure inference library supporting precise low bitwidth computations (required by converters) as well as provably precise math functions; thus, overcoming all the drawbacks listed above. We perform an extensive evaluation of LLAMA and show that when compared with non-FSS based libraries supporting mixed bitwidth arithmetic and math functions (SIRNN, IEEE S&amp;P 2021), it has at least an order of magnitude lower communication, rounds, and runtimes. We integrate LLAMA with the EzPC framework (IEEE EuroS&amp;P 2019) and demonstrate its robustness by evaluating it on large benchmarks (such as ResNet-50 on the ImageNet dataset) as well as on benchmarks considered in AriaNN -- here too LLAMA outperforms prior work.

  匹配依据：MPC: secret sharing

  </details>

- **Scalable Differentially Private Clustering via Hierarchically Separated Trees**
  2022-06-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.08646)
  Vincent Cohen-Addad, Alessandro Epasto, Silvio Lattanzi, Vahab Mirrokni, Andres Munoz, David Saulpic, Chris Schwiegelshohn, Sergei Vassilvitskii

  <details><summary>摘要 / Abstract</summary>

  We study the private $k$-median and $k$-means clustering problem in $d$ dimensional Euclidean space. By leveraging tree embeddings, we give an efficient and easy to implement algorithm, that is empirically competitive with state of the art non private methods. We prove that our method computes a solution with cost at most $O(d^{3/2}\log n)\cdot OPT + O(k d^2 \log^2 n / ε^2)$, where $ε$ is the privacy guarantee. (The dimension term, $d$, can be replaced with $O(\log k)$ using standard dimension reduction techniques.) Although the worst-case guarantee is worse than that of state of the art private clustering methods, the algorithm we propose is practical, runs in near-linear, $\tilde{O}(nkd)$, time and scales to tens of millions of points. We also show that our method is amenable to parallelization in large-scale distributed computing environments. In particular we show that our private algorithms can be implemented in logarithmic number of MPC rounds in the sublinear memory regime. Finally, we complement our theoretical analysis with an empirical evaluation demonstrating the algorithm&#x27;s efficiency and accuracy in comparison to other privacy clustering baselines.

  匹配依据：MPC: mpc (context)

  </details>

- **YOU SHALL NOT COMPUTE on my Data: Access Policies for Privacy-Preserving Data Marketplaces and an Implementation for a Distributed Market using MPC**
  2022-06-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.07507)
  Stefan More, Lukas Alber

  <details><summary>摘要 / Abstract</summary>

  Personal data is an attractive source of insights for a diverse field of research and business. While our data is highly valuable, it is often privacy-sensitive. Thus, regulations like the GDPR restrict what data can be legally published, and what a buyer may do with this sensitive data. While personal data must be protected, we can still sell some insights gathered from our data that do not hurt our privacy. A data marketplace is a platform that helps users to sell their data while assisting buyers in discovering relevant datasets. The major challenge such a marketplace faces is balancing between offering valuable insights into data while preserving privacy requirements. Private data marketplaces try to solve this challenge by offering privacy-preserving computations on personal data. Such computations allow for calculating statistics or training machine learning models on personal data without accessing the data in plain. However, the user selling the data cannot restrict who can buy or what type of computation the data is allowed. We close the latter gap by proposing a flexible access control architecture for private data marketplaces, which can be applied to existing data markets. Our architecture enables data sellers to define detailed policies restricting who can buy their data. Furthermore, a seller can control what computation a specific buyer can purchase on the data, and make constraints on its parameters to mitigate privacy breaches. The data market&#x27;s computation system then enforces the policies before initiating a computation. To demonstrate the feasibility of our approach, we provide an implementation for the KRAKEN marketplace, a distributed data market using MPC. We show that our approach is practical since it introduces a negligible performance overhead and is secure against several adversaries.

  匹配依据：MPC: mpc (context)

  </details>

- **Maliciously Secure Multi-Party PSI with Lower Bandwidth and Faster Computation**
  2022-06-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/772)
  Zhi Qiu, Kang Yang, Yu Yu, Lijing Zhou

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection (PSI) allows a set of mutually distrustful parties, each holds a private data set, to compute the intersection of all sets, such that no information is revealed except for the intersection. The state-of-the-art PSI protocol (Garimella et al., CRYPTO&#x27;21) in the multi-party setting tolerating any number of malicious corruptions requires the communication bandwidth of $O(n\ell|\mathbb{F}|)$ bits for the central party $P_0$ due to the star architecture, where $n$ is the number of parties, $\ell$ is the size of each set and $|\mathbb{F}|$ is the size of an exponentially large field $\mathbb{F}$. When $n$ and $\ell$ are large, this forms an efficiency bottleneck (especially for networks with restricted bandwidthes). In this paper, we present a new multi-party PSI protocol in dishonest-majority malicious setting, which reduces the communication bandwidth of the central party $P_0$ from $O(n\ell|\mathbb{F}|)$ bits to $O(\ell|\mathbb{F}|)$ bits using a tree architecture. Furthermore, our PSI protocol reduces the expensive LPN encoding operations performed by $P_0$ by a factor of $n$ as well as the computational cost by $2n\ell$ hash operations in total. Additionally, while the multi-party PSI protocol (Garimella et al., CRYPTO&#x27;21) with a single output is secure, we present a simple attack against its multi-output extension, which allows an adversary to learn more information on the sets of honest parties beyond the intersection of all sets.

  匹配依据：MPC: private set intersection

  </details>

- **The Cost of Statistical Security in Interactive Proofs for Repeated Squaring**
  2022-06-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/766)
  Cody Freitag, Ilan Komargodski

  <details><summary>摘要 / Abstract</summary>

  In recent years, the number of applications of the repeated squaring assumption has been growing rapidly. The assumption states that, given a group element $x$, an integer $T$, and an RSA modulus $N$, it is hard to compute $x^{2^T} \mod N$---or even decide whether $y\stackrel{?}{=}x^{2^T} \mod N$---in parallel time less than the trivial approach of computing $T$ sequential squarings. This rise has been driven by efficient interactive proofs for repeated squaring, opening the door to more efficient constructions of verifiable delay functions, various secure computation primitives, and proof systems for more general languages. In this work, we study the complexity of statistically-sound interactive proofs for the repeated squaring relation. Technically, we consider interactive proofs where the prover sends at most $k \ge 0$ elements per round and the verifier performs generic group operations over the group $\mathbb{Z}_N^\star$. As our main contribution, we show that for any one-round proof with a randomized verifier (i.e., an MA proof) the verifier either runs in parallel time $\Omega(T/(k+1))$ with high probability, or is able to factor $N$ given the proof provided by the prover. This shows that either the prover essentially sends $p,q$ such that $N = p\cdot q$ (which is infeasible or undesirable in most applications), or a variant of Pietrzak&#x27;s proof of repeated squaring (ITCS 2019) has optimal verifier complexity $O(T/(k+1))$. In particular, it is impossible to obtain a statistically-sound one-round proof of repeated squaring with efficiency on par with the computationally-sound protocol of Wesolowski (EUROCRYPT 2019), with a generic group verifier. We further extend our one-round lower bound to a natural class of recursive (multi-round) interactive proofs for repeated squaring.

  匹配依据：MPC: secure computation

  </details>

- **Semi-Private Computation of Data Similarity with Applications to Data Valuation and Pricing**
  2022-06-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.06650)
  René Bødker Christensen, Shashi Raj Pandey, Petar Popovski

  <details><summary>摘要 / Abstract</summary>

  Consider two data providers that want to contribute data to a certain learning model. Recent works have shown that the value of the data of one of the providers is dependent on the similarity with the data owned by the other provider. It would thus be beneficial if the two providers can calculate the similarity of their data, while keeping the actual data private. In this work, we devise multiparty computation-protocols to compute similarity of two data sets based on correlation, while offering controllable privacy guarantees. We consider a simple model with two participating providers and develop methods to compute exact and approximate correlation, respectively, with controlled information leakage. Both protocols have computational and communication complexities that are linear in the number of data samples. We also provide general bounds on the maximal error in the approximation case, and analyse the resulting errors for practical parameter choices.

  匹配依据：MPC: multiparty computation

  </details>

- **Privacy Preserving Opinion Aggregation**
  2022-06-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/760)
  Aggelos Kiayias, Vanessa Teague, Orfeas Stefanos Thyfronitis Litos

  <details><summary>摘要 / Abstract</summary>

  There are numerous settings in which people’s preferences are aggregated outside of formal elections, and where privacy and verification are important but the stringent coercion-resistant properties of government elections do not apply, a prime example being social media platforms. In contrast to the centrally organised, single-shot elections on which most of the literature is focused, our settings of interest often have no trusted authority and are iterative, i.e., publish partial tallies before all votes are received. In this work, we explore opinion aggregation in a decentralised, iterative setting. In our novel protocol,randomly-chosen parties take turns to decrypt aggregated votes in an incentive-driven manner. Our simple construction leverages homomorphic encryption and secret sharing in a novel manner to provide security of the tally, public and individual verifiability, as well as vote privacy and liveness guarantees. Contrary to existing voting schemes, our protocol is ideal for the iterative setting.

  匹配依据：MPC: secret sharing

  </details>

- **The Ideal Functionalities for Private Set Union, Revisited**
  2022-06-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/750)
  Yanxue Jia, Shi-Feng Sun, Hong-Sheng Zhou, Dawu Gu

  <details><summary>摘要 / Abstract</summary>

  A Private Set Union (PSU) protocol allows parties, each holding an input set, to jointly compute the union of the sets without revealing anything else. In the literature, when we design scalable two-party PSU protocols, we follow the so-called ``split-execute-assemble&#x27;&#x27; paradigm, and also use Oblivious Transfer as a building block. Recently, Kolesnikov et al. (ASIACRYPT 2019) pointed out that security issues could be introduced when we design PSU protocols following the ``split-execute-assemble&#x27;&#x27; paradigm. Surprisingly, we observe that the typical way of invoking Oblivious Transfer also causes unnecessary leakage. In this work, to enable a better understanding of the security for PSU, we provide a systematic treatment of the typical PSU protocols, which may shed light on the design of practical and secure PSU protocols in the future. More specifically, we define different versions of PSU functionalities to properly capture the subtle security issues arising from protocols following the ``split-execute-assemble&#x27;&#x27; paradigm and using Oblivious Transfer as subroutines. Then, we survey the typical PSU protocols, and categorize these protocols into three design frameworks, and prove what PSU functionality the protocols under each framework can achieve at best, in the semi-honest setting.

  匹配依据：MPC: oblivious transfer, private set union

  </details>

- **Static vs. Adaptive Security in Perfect MPC: A Separation and the Adaptive Security of BGW**
  2022-06-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/758)
  Gilad Asharov, Ran Cohen, Oren Shochat

  <details><summary>摘要 / Abstract</summary>

  Adaptive security is a highly desirable property in the design of secure protocols. It tolerates adversaries that corrupt parties as the protocol proceeds, as opposed to static security where the adversary corrupts the parties at the onset of the execution. The well-accepted folklore is that static and adaptive securities are equivalent for perfectly secure protocols. Indeed, this folklore is backed up by a transformation by Canetti et al. (EUROCRYPT&#x27;01), showing that any perfectly secure protocol that is statically secure and satisfies some basic requirements is also adaptively secure. Yet, the transformation results in an adaptively secure protocol with inefficient simulation (i.e., where the simulator might run in super-polynomial time even if the adversary runs just in polynomial time). Inefficient simulation is problematic when using the protocol as a sub-routine in the computational setting. Our main question is whether an alternative efficient transformation from static to adaptive security exists. We show an inherent difficulty in achieving this goal generically. In contrast to the folklore, we present a protocol that is perfectly secure with efficient static simulation (therefore also adaptively secure with inefficient simulation), but for which efficient adaptive simulation does not exist (assuming the existence of one-way permutations). In addition, we prove that the seminal protocol of Ben-Or, Goldwasser, and Wigderson (STOC&#x27;88) is secure against adaptive, semi-honest corruptions with efficient simulation. Previously, adaptive security of the protocol, as is, was only known either for a restricted class of circuits or for all circuits but with inefficient simulation.

  匹配依据：MPC: mpc (context)

  </details>

- **Constant-Round Linear-Broadcast Secure Computation with Penalties**
  2022-06-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.06010)
  Takeshi Nakai, Kazumasa Shinagawa

  <details><summary>摘要 / Abstract</summary>

  It is known that Bitcoin enables achieving fairness in secure computation by imposing monetary penalties on adversarial parties. This functionality is called secure computation with penalties. Bentov and Kumaresan (Crypto 2014) introduced the claim-or-refund functionality that can be implemented via Bitcoin. They achieved secure computation with penalties with $O(n)$ rounds and $O(n)$ broadcasts for any function, where $n$ is the number of parties. After that, Kumaresan and Bentov (CCS 2014) showed a constant-round protocol. Unfortunately, this protocol requires $O(n^2)$ broadcasts. As far as we know, no protocol achieves $O(1)$ rounds and $O(n)$ broadcasts based on Bitcoin. This work accomplishes such efficiency in secure computation with penalties. We first show a protocol in a slightly relaxed setting called secure computation with non-equivalent penalties. This setting is the same as secure computation with penalties except that every honest party receives more than a predetermined amount of compensation, while the previous one requires that every honest party receives the same amount of compensation. Namely, our setting allows the compensations for honest parties to be non-equivalent. Moreover, we present a technique to remove the non-equivalence of our protocol without sacrificing efficiency. We then propose a new ideal functionality called claim-refund-or-give that can be implemented via Bitcoin.

  匹配依据：MPC: secure computation

  </details>

- **SCALES: MPC with Small Clients and Larger Ephemeral Servers**
  2022-06-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/751)
  Anasuya Acharya, Carmit Hazay, Vladimir Kolesnikov, Manoj Prabhakaran

  <details><summary>摘要 / Abstract</summary>

  The recently proposed YOSO model is a groundbreaking approach to MPC, executable on a public blockchain, circumventing adaptive player corruption by hiding the corruption targets until they are worthless. Players are selected unpredictably from a large pool to perform MPC subtasks, in which each selected player sends a single message (and reveals their identity). While YOSO MPC has attractive asymptotic complexity, unfortunately, it is concretely prohibitively expensive due to the cost of its building blocks. We propose a modification to the YOSO model that preserves resilience to adaptive server corruption, but allows for much more efficient protocols. In SCALES (Small Clients And Larger Ephemeral Servers) only the servers facilitating the MPC computation are ephemeral (unpredictably selected and ``speak once&#x27;&#x27;). Input providers (clients) publish problem instances and collect the output, but do not otherwise participate in computation. SCALES offers attractive features, and improves over YOSO protocols in outsourcing MPC to a large pool of servers under adaptive corruption. We build SCALES from rerandomizable garbling schemes, which is a contribution of independent interest, with additional applications.

  匹配依据：MPC: garbling schemes

  </details>

- **Distributed Differential Privacy in Multi-Armed Bandits**
  2022-06-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.05772)
  Sayak Ray Chowdhury, Xingyu Zhou

  <details><summary>摘要 / Abstract</summary>

  We consider the standard $K$-armed bandit problem under a distributed trust model of differential privacy (DP), which enables to guarantee privacy without a trustworthy server. Under this trust model, previous work largely focus on achieving privacy using a shuffle protocol, where a batch of users data are randomly permuted before sending to a central server. This protocol achieves ($ε,δ$) or approximate-DP guarantee by sacrificing an additional additive $O\!\left(\!\frac{K\log T\sqrt{\log(1/δ)}}ε\!\right)\!$ cost in $T$-step cumulative regret. In contrast, the optimal privacy cost for achieving a stronger ($ε,0$) or pure-DP guarantee under the widely used central trust model is only $Θ\!\left(\!\frac{K\log T}ε\!\right)\!$, where, however, a trusted server is required. In this work, we aim to obtain a pure-DP guarantee under distributed trust model while sacrificing no more regret than that under central trust model. We achieve this by designing a generic bandit algorithm based on successive arm elimination, where privacy is guaranteed by corrupting rewards with an equivalent discrete Laplace noise ensured by a secure computation protocol. We also show that our algorithm, when instantiated with Skellam noise and the secure protocol, ensures \emph{Rényi differential privacy} -- a stronger notion than approximate DP -- under distributed trust model with a privacy cost of $O\!\left(\!\frac{K\sqrt{\log T}}ε\!\right)\!$.

  匹配依据：MPC: secure computation

  </details>

- **On entropic and almost multilinear representability of matroids**
  2022-06-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.03465)
  Lukas Kühne, Geva Yashfe

  <details><summary>摘要 / Abstract</summary>

  This article studies two notions of generalized matroid representations motivated by algorithmic information theory and cryptographic secret sharing. The first (entropic representability) involves discrete random variables, while the second (almost-multilinear representability) deals with approximate subspace arrangements. In both cases, we prove that determining whether an input matroid has such a representation is undecidable. Consequently, the conditional independence implication problem is also undecidable, providing an independent answer to a question posed by Geiger and Pearl, recently resolved by Cheuk Ting Li. These problems are also closely related to characterizing achievable rates in network coding and constructing secret sharing schemes. For example, another corollary of our work is that deciding whether an access structure admits an ideal secret sharing scheme is undecidable. Our approach reduces undecidable problems from group theory to matroid representation problems. Specifically, we reduce the uniform word problem for finite groups to entropic representability and the word problem for sofic groups to almost-multilinear representability. A key part of this reduction involves modifying group presentations into forms where linear representations are generic in an appropriate sense when restricted to the generating set.

  匹配依据：MPC: secret sharing

  </details>

- **A Privacy-Preserving Subgraph-Level Federated Graph Neural Network via Differential Privacy**
  2022-06-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.03492)
  Yeqing Qiu, Chenyu Huang, Jianzong Wang, Zhangcheng Huang, Jing Xiao

  <details><summary>摘要 / Abstract</summary>

  Currently, the federated graph neural network (GNN) has attracted a lot of attention due to its wide applications in reality without violating the privacy regulations. Among all the privacy-preserving technologies, the differential privacy (DP) is the most promising one due to its effectiveness and light computational overhead. However, the DP-based federated GNN has not been well investigated, especially in the sub-graph-level setting, such as the scenario of recommendation system. The biggest challenge is how to guarantee the privacy and solve the non independent and identically distributed (non-IID) data in federated GNN simultaneously. In this paper, we propose DP-FedRec, a DP-based federated GNN to fill the gap. Private Set Intersection (PSI) is leveraged to extend the local graph for each client, and thus solve the non-IID problem. Most importantly, DP is applied not only on the weights but also on the edges of the intersection graph from PSI to fully protect the privacy of clients. The evaluation demonstrates DP-FedRec achieves better performance with the graph extension and DP only introduces little computations overhead.

  匹配依据：MPC: private set intersection

  </details>

- **Quantum oblivious transfer: a short review**
  2022-06-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.03313)
  Manuel B. Santos, Paulo Mateus, Armando N. Pinto

  <details><summary>摘要 / Abstract</summary>

  Quantum cryptography is the field of cryptography that explores the quantum properties of matter. Its aim is to develop primitives beyond the reach of classical cryptography or to improve on existing classical implementations. Although much of the work in this field is dedicated to quantum key distribution (QKD), some important steps were made towards the study and development of quantum oblivious transfer (QOT). It is possible to draw a comparison between the application structure of both QKD and QOT primitives. Just as QKD protocols allow quantum-safe communication, QOT protocols allow quantum-safe computation. However, the conditions under which QOT is actually quantum-safe have been subject to a great amount of scrutiny and study. In this review article, we survey the work developed around the concept of oblivious transfer in the area of theoretical quantum cryptography, with an emphasis on some proposed protocols and their security requirements. We review the impossibility results that daunt this primitive and discuss several quantum security models under which it is possible to prove QOT security.

  匹配依据：MPC: oblivious transfer

  </details>

- **Cross Chain Atomic Swaps in the Absence of Time via Attribute Verifiable Timed Commitments**
  2022-06-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/717)
  Yacov Manevich, Adi Akavia

  <details><summary>摘要 / Abstract</summary>

  A Hash Time Lock Contract (HTLC) is a protocol that is commonly used to exchange payments across different blockchains. Using HTLC as a building block for cross blockchain atomic swaps has its drawbacks: The notion of time is handled differently in each blockchain, be it private or public. Additionally, if the swap ends up aborted, the funds are locked in escrow until the safety timeout expires. In this work we formulate a new cryptographic primitive: Attribute Verifiable Timed Commitment which enables to prove that a timed commitment commits to a value which possesses certain attributes. Using our cryptographic primitive, we describe a new cross chain atomic swap protocol that operates without blockchain derived time and unlike the state of the art, all parties can instantly abort the swap without waiting for the safety timeouts to expire. In order to prove in zero knowledge that a secret committed to using a timed commitment has a claimed hash value, we employ the &quot;MPC in the head&quot; technique by Ishai et al. and implement our zero-knowledge proof protocol and evaluate its performance. As part of our techniques, we develop a novel and efficient procedure for integer Lower-Than validation in arithmetic circuits which may be of independent interest.

  匹配依据：MPC: mpc (context)

  </details>

- **The Hardness of LPN over Any Integer Ring and Field for PCG Applications**
  2022-06-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/712)
  Hanlin Liu, Xiao Wang, Kang Yang, Yu Yu

  <details><summary>摘要 / Abstract</summary>

  Learning parity with noise (LPN) has been widely studied and used in cryptography. It was recently brought to new prosperity since Boyle et al. (CCS&#x27;18), putting LPN to a central role in designing secure multi-party computation, zero-knowledge proofs, private set intersection, and many other protocols. In this paper, we thoroughly studied the security of LPN problems in this particular context. We found that some important aspects have long been ignored and many conclusions from classical LPN cryptanalysis do not apply to this new setting, due to the low noise rates, extremely high dimensions, various types (in addition to $\mathbb{F}_2$) and noise distributions. 1. For LPN over a field, we give a parameterized reduction from exact-noise LPN to regular-noise LPN. Compared to the recent result by Feneuil, Joux and Rivain (Crypto&#x27;22), we significantly reduce the security loss by paying only a small additive price in dimension and number of samples. 2. We analyze the security of LPN over a ring $\mathbb{Z}_{2^\lambda}$. Existing protocols based on LPN over integer rings use parameters as if they are over fields, but we found an attack that effectively reduces the weight of a noise by half compared to LPN over fields. Consequently, prior works that use LPN over $\mathbb{Z}_{2^\lambda}$ overestimate up to 40 bits of security. 3. We provide a complete picture of the hardness of LPN over integer rings by showing: 1) the equivalence between its search and decisional versions; 2) an efficient reduction from LPN over $\mathbb{F}_2$ to LPN over $\mathbb{Z}_{2^\lambda}$; and 3) generalization of our results to any integer ring. Finally, we provide an all-in-one estimator tool for the bit security of LPN parameters in the context of PCG, incorporating the recent advanced attacks.

  匹配依据：MPC: private set intersection, secure multi party computation

  </details>

- **Multi-Party Computation in IoT for Privacy-Preservation**
  2022-06-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.01956)
  Himanshu Goyal, Sudipta Saha

  <details><summary>摘要 / Abstract</summary>

  Preservation of privacy has been a serious concern with the increasing use of IoT-assisted smart systems and their ubiquitous smart sensors. To solve the issue, the smart systems are being trained to depend more on aggregated data instead of directly using raw data. However, most of the existing strategies for privacy-preserving data aggregation, either depend on computation-intensive Homomorphic Encryption based operations or communication-intensive collaborative mechanisms. Unfortunately, none of the approaches are directly suitable for a resource-constrained IoT system. In this work, we leverage the concurrent-transmission-based communication technology to efficiently realize a Multi-Party Computation (MPC) based strategy, the well-known Shamir&#x27;s Secret Sharing (SSS), and optimize the same to make it suitable for real-world IoT systems.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **More Efficient (Reusable) Private Set Union**
  2022-06-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/713)
  Dov Gordon, Carmit Hazay, Phi Hung Le, Mingyu Liang

  <details><summary>摘要 / Abstract</summary>

  We study the problem of private set union in the two-party setting, providing several new constructions. We consider the case where one party is designated to receive output. In the semi-honest setting, we provide a four-round protocol and two-round protocol, each with two variants. Our four-round protocol focusing on runtime out-performs the state-of-the-art in runtime for the majority of the medium bandwidth settings ($100$Mbps) and the large set size ($\geq 2^{20}$) settings, with a runtime that is 1.04X-1.25X faster than existing protocols. Our other four-round variant focusing on communication outperforms the state-of-the-art in communication by up to a factor of 1.43 when the set size $\geq 2^{18}$. On the other hand, our two-round protocol is only slightly more expensive but has the property that the receiver message can be re-used across multiple executions. All our semi-honest protocols are post-quantum secure if post-quantum primitives (OKVS and OT) are used. In the setting where the sender is malicious, we provide the first protocols that avoid using expensive zero-knowledge proofs. Our four-round protocol costs less than double in both communication and computation compared to all other semi-honest constructions, showcasing great efficiency. As in the semi-honest setting, we also give a more expensive protocol that allows the receiver message to be re-used. Our work draws on several techniques from the literature on private set intersection and helps clarify how these techniques generalize (and don&#x27;t generalize) to the problem of private set union.

  匹配依据：MPC: private set intersection, private set union

  </details>

- **Key Agreement and Oblivious Transfer from Free-Energy Limitations**
  2022-06-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.01501)
  Xavier Coiteux-Roy, Stefan Wolf

  <details><summary>摘要 / Abstract</summary>

  We propose one of the very few constructive consequences of the second law of thermodynamics. More specifically, we present protocols for secret-key establishment and multiparty computation the security of which is based fundamentally on Landauer&#x27;s principle. The latter states that the erasure cost of each bit of information is at least kTln2 (where k is Boltzmann&#x27;s constant and T is the absolute temperature of the environment). Albeit impractical, our protocols explore the limits of reversible computation, and the only assumption about the adversary is her inability to access a quantity of free energy that is exponential in the one of the honest participants. Our results generalize to the quantum realm.

  匹配依据：MPC: multiparty computation, oblivious transfer

  </details>
