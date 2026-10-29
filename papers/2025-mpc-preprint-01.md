# 2025 · MPC · 仅预印本来源 · 第 1/5 页

[总目录](../PAPERS.md) · [下一页](2025-mpc-preprint-02.md)

- **OOPS: One-time Oblivious Polynomial Signatures**
  2025-12-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2340)
  Kobi Gurkan, Philipp Jovanovic, Andrija Novakovic

  <details><summary>摘要 / Abstract</summary>

  We introduce one-time oblivious polynomial signatures (OOPS), a signature scheme based on polynomials over pairing-based elliptic curves that can securely produce signatures for up to a threshold of $n$ different messages. Signing more than $n$ messages allows anyone to forge signatures under the given parameters, making it necessary to reparameterize the scheme occasionally. We show that this property is not a severe limitation though by demonstrating how to build various efficient OOPS-based cryptographic protocols, including delegatable signatures, $1$-out-of-$n$ oblivious transfer, and partially oblivious PRFs.

  匹配依据：MPC: oblivious transfer

  </details>

- **Multiparty Authorization for Secure Data Storage in Cloud Environments using Improved Attribute-Based Encryption**
  2025-12-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.23216)
  Partha Paul, Keshav Sinha

  <details><summary>摘要 / Abstract</summary>

  In todays scenario, various organizations store their sensitive data in the cloud environment. Multiple problems are present while retrieving and storing vast amounts of data, such as the frequency of data requests (increasing the computational overhead of the server) and data leakage while storing. To cope with said problem, Attribute-Based Encryption (ABE) is one of the potential security and access control techniques for secure data storage and authorization. The proposed work divides into two objectives: (i) provide access to authorized users and (ii) secure data storage in a cloud environment. The improved ABE using Functional Based Stream Cipher (FBSE) is proposed for data storage. The proposed technique uses simple scalar points over a parabolic curve to provide multiparty authorization. The authorization points are generated and share only with the authorized recipients. The Shamir secret sharing technique generate the authorization points and 2D-Lagrange Interpolation is used to reconstruct the secret points from regular parabola. The proposed scheme has specified the threshold (Ts&gt;3) legally authorized users to reconstruct the attribute-associated keys for decryption. The encryption of data is evaluated using Statistical analysis (NIST Statistical Test Suite, Correlation Coefficient, and Histogram) test to investigate image pixel deviation. The parameters like encryption and decryption are used for performance analysis, where an increase in the number of attributes for the authorization policy will increase the encryption time. The proposed scheme imposes minimal storage overhead, irrespective of the users identity. The security analysis evidence that it resists collision attacks. The security and performance analysis results demonstrate that the proposed scheme is more robust and secure.

  匹配依据：MPC: secret sharing

  </details>

- **Verifiable Aggregate Receipts with Applications to User Engagement Auditing**
  2025-12-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2330)
  Ioannis Kaklamanis, Wenhao Wang, Harjasleen Malvai, Sen Yang, Fan Zhang

  <details><summary>摘要 / Abstract</summary>

  Accurate measurements of user engagement underpin important decisions in various settings, such as determining advertising fees based on viewership of online content, allocating public funding based on a clinic’s reported patient volume, or determining whether a group chat app disseminated a message without censorship. While common, self-reporting is inherently untrustworthy due to misaligned incentives (e.g., to inflate). Motivated by this problem, we introduce the notion of Verifiable Aggregate Receipts (VAR). A VAR system allows an issuer to issue receipts to users and to verify the number of receipts possessed by a prover, who is given receipts upon serving users. An ideal VAR system should satisfy inflation soundness (the prover cannot overstate the count), privacy (the verifier learns only the count), and be performant for large-scale applications with millions of users. We formalize VAR using an ideal functionality and present two novel constructions. Our first protocol, S-VAR, leverages bottom-up secret-sharing to enable tiered &#x27;&#x27;fuzzy&#x27;&#x27; audits, and achieves constant-size receipts regardless of the number of supported thresholds. Our second protocol, P-VAR, uses bilinear pairings to aggregate receipts into a proof verifiable in constant time, enables exact auditing, and can be extended to handle a dynamic user set. We prove both constructions secure with respect to our ideal functionality. We implement and benchmark our VAR constructions, showing that they outperform all baseline and existing solutions by at least an order of magnitude in both proving and verification time. Finally, we show how VAR applies to the aforementioned use cases and further demonstrate its practicality by integrating it with Bluesky, a decentralized social network.

  匹配依据：MPC: secret sharing

  </details>

- **A note on \`\`a fully dynamic multi-secret sharing scheme with redundant authorization''**
  2025-12-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2329)
  Zhengjun Cao, Lihua Liu

  <details><summary>摘要 / Abstract</summary>

  We show that the secret sharing scheme [Cryptogr. Commun. 16(1): 3-20 (2024)] cannot be put into practice. (1) It confused the elements in a residue class ring modulo a prime $p$ with the points in an elliptic curve group over the finite field $F_p$. (2) It confused the underlying elliptic curve with the Lagrange interpolating curve, and falsely requires the interpolating polynomial to map a point on the elliptic curve to another point on the same elliptic curve. (3) It misuses the bit-wise XOR operator for the operands with unequal bit-length, which results in the exposure of any participant&#x27;s share, and the loss of confidentiality.

  匹配依据：MPC: secret sharing

  </details>

- **Quantum Secret Sharing Rates**
  2025-12-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.22049)
  Gabrielle Lalou, Husein Natur, Uzi Pereg

  <details><summary>摘要 / Abstract</summary>

  This paper studies the capacity limits for quantum secret sharing (QSS). The goal of a QSS scheme is to distribute a quantum secret among multiple participants, such that only authorized parties can recover it through collaboration, while no information can be obtained without such collaboration. We introduce an information-theoretic model for the rate analysis of QSS and its relation to compound quantum channels, following a similar approach as of Zou et al. (2015) on classical secret sharing. We establish a regularized characterization for the QSS capacity, and determine the capacity for QSS with dephasing noise.

  匹配依据：MPC: secret sharing

  </details>

- **SHAFT: Secure, Handy, Accurate, and Fast Transformer Inference**
  2025-12-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2324)
  Andes Y. L. Kei, Sherman S. M. Chow

  <details><summary>摘要 / Abstract</summary>

  A growing adoption of transformer-based machine learning models is raising concerns about sensitive data exposure. Nonetheless, current secure inference solutions incur substantial overhead due to their extensive reliance on non-linear protocols, such as softmax and Gaussian error linear unit (GELU). Driven by numerical stability needs, softmax approximations (e.g., NeurIPS 2021) typically extract the maximum element of an input vector, incurring logarithmic rounds (in the input length). Existing GELU protocols (e.g., S&amp;P 2024) use piecewise approximations with high-degree polynomials that rely heavily on secure multiplications and comparisons, which are expensive. Such complexities also hinder model owners unfamiliar with cryptography from deploying custom models. SHAFT, our proposed system, provides a secure, handy, accurate, and fast transformer inference framework for deployment. Highlights of our contributions include 1) the first constant-round (independent of sequence length) softmax protocol for transformers, using input clipping and an ordinary differential equation characterization, and 2) a highly accurate GELU protocol on a novel characterization designed for Fourier series approximation. Extending to broader contexts, our new protocols also apply to general neural networks that use softmax as the final layer and to transformer architectures with different activation functions. Remarkably, SHAFT outperforms state-of-the-art SIGMA (PETS 2024), which uses secret sharing, and BumbleBee (NDSS 2025), which additionally uses RLWE-based homomorphic encryption. More specifically, SHAFT reduces communication by 62–70% and is 1.8–2.4× faster than SIGMA, while also surpassing BumbleBee in terms of running time by 2.6–3.7× under LAN settings. Alongside these improvements, SHAFT attains accuracy comparable to plaintext models, confirming its numerical stability. Next in this progression, SHAFT provides an accessible open-source framework for secure and handy deployment by smoothly integrating with the Hugging Face library (EMNLP Demos 2020).

  匹配依据：MPC: secret sharing

  </details>

- **Enhancing Distributed Authorization With Lagrange Interpolation And Attribute-Based Encryption**
  2025-12-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.21525)
  Keshav Sinha, Sumitra, Richa Kumari, Akashdeep Bhardwaj, Shawon Rahman

  <details><summary>摘要 / Abstract</summary>

  In todays security landscape, every user wants to access large amounts of data with confidentiality and authorization. To maintain confidentiality, various researchers have proposed several techniques. However, to access secure data, researchers use access control lists to grant authentication and provide authorization. The above several steps will increase the server&#x27;s computation overhead and response time. To cope with these two problems, we proposed multiparty execution on the server. In this paper, we introduce two different approaches. The first approach is encryption, utilizing the Involution Function Based Stream Cipher to encrypt the file data. The second approach is key distribution, using the Shamir secret sharing scheme to divide and distribute the symmetric key to every user. The decryption process required key reconstruction, which used second order Lagrange interpolation to reconstruct the secret keys from the hidden points. The process will reduce the server&#x27;s computational overhead. The results are evaluated based on the encryption and decryption time, throughput, computational overhead, and security analysis. In the future, the proposed mechanism will be used to share large-scale, secure data within the organization.

  匹配依据：MPC: secret sharing

  </details>

- **New Constructions of Multiplicative Secret Sharing Schemes**
  2025-12-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2320)
  Chunming Tang, Haonan Fu, Zheng Chen, Hongwei Zhu

  <details><summary>摘要 / Abstract</summary>

  This paper investigates the multiplicative properties of linear codes in secret sharing schemes. To address the limitation that certain access structures cannot be realized by ideal linear codes, we introduce the notion of shortest linear codes as an ideal benchmark for code length. Since explicitly determining such shortest codes is generally computationally difficult, we propose an explicit construction that, for any given access structure, produces a length-efficient linear code whose induced the access structure. On this basis, we further define multiplicative ideal linear codes and multiplicative length-efficient linear codes, and derive necessary and sufficient conditions for the existence of multiplicativity. The effectiveness of the proposed approach is demonstrated by concrete examples. Compared with the construction of Cramer et al., the multiplicative linear codes obtained in this work have smaller length.

  匹配依据：MPC: secret sharing

  </details>

- **One-Time Memories Secure against Depth-Bounded Quantum Circuits**
  2025-12-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2319)
  Kyosuke Sekii, Takashi Nishide

  <details><summary>摘要 / Abstract</summary>

  A one-time memory (OTM) is a useful cryptographic primitive, classically modeled after a non-interactive oblivious transfer. It is well known that secure OTMs (and more generally one-time deterministic programs) cannot exist in the standard model in either the classical or quantum setting due to Broadbent et al. (CRYPTO&#x27;13). Broadbent et al.\ circumvented this impossibility by assuming the existence of hardware tokens that cannot be queried in superposition. In this work, we take a different approach. Building on Liu&#x27;s assumption (ITCS&#x27;23) that adversaries are limited to depth-bounded quantum circuits, we present two OTM constructions. The first is efficiently realizable and secure against adversaries restricted to constant-depth quantum circuits. The second is a feasibility result that achieves security against adversaries limited to $\mathcal{O}(\lambda^\gamma)$-depth quantum circuits by ensuring that a successful attack would necessarily require deeper quantum computations, where $\lambda^\gamma$ is a polynomial in the security parameter $\lambda$. Our results therefore extend prior work, which either relied on hardware assumptions or considered only constant-depth-bounded adversaries. As a result, by combining our proposed quantum OTMs with the framework of Broadbent et al. (CRYPTO&#x27;13), one can also realize quantum one-time programs (OTPs) for deterministic programs.

  匹配依据：MPC: oblivious transfer

  </details>

- **Nested YOSO MPC: Near Optimal Resilience Without an MPC Setup**
  2025-12-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2313)
  Ittai Abraham, Eli Chouatt, Ivan Damgård, Yossi Gilad, Gilad Stern, Sophia Yakoubov

  <details><summary>摘要 / Abstract</summary>

  You Only Speak Once (YOSO) secure Multi-Party Computation (MPC) provides scalability and adaptive security by distributing the computation across a sequence of anonymous committees. This relies on role assignment, which sets up the infrastructure necessary for the members of one committee to send secret messages to members of subsequent committees without knowing their identities. Existing approaches to role assignment suffer from significant limitations: high broadcast complexity, reliance on secure computation (which creates a circular dependency), or the requirement of an overwhelming honest majority among available nodes in order to guarantee output delivery in the MPC. In this work, we introduce Nested YOSO MPC, which overcomes all of these drawbacks by departing from the traditional threshold adversary structure. We design our MPC to run over a sequence of size-$m^2$ committees, each composed of $m$ subcommittees of size $m$. This MPC is secure (with guaranteed output delivery) as long as most subcommittees on each committee have an honest majority. Our efficient, setup-free role assignment protocol guarantees an honest majority on most subcommittees as long as $(\frac{1}{2} + \epsilon)N$ of the available participants are honest, where $\epsilon$ is a constant and $N$ is the total number of available participants. As a complementary contribution, we prove that no MPC with polylogarithmic (in $N$) broadcast complexity can rely on $\frac{N}{2} + o(\frac{N}{polylog(N)})$ honest parties, indicating that our construction is near-optimal in terms of the number of corruptions it can tolerate.

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **Conditionally Input-Revealing 2PC and Fuzzy Password-Authenticated Key Exchange**
  2025-12-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2315)
  David Richardson, Mike Rosulek, Jiayu Xu

  <details><summary>摘要 / Abstract</summary>

  Yao&#x27;s famous protocol for secure 2-party computation, based on garbled circuits, is well-known to be insecure against an actively corrupt garbler. We introduce a new and extremely simple variant of Yao&#x27;s protocol that is fully secure against active adversaries, for a certain class of functions that we call conditionally input-revealing. We then show how to use this new protocol as the basis for fuzzy password authenticated key exchange (fuzzy PAKE). In fuzzy PAKE, two parties each hold a low-entropy secret (e.g., a password), and they interact to obtain a secure high-entropy key if and only if the passwords are sufficiently ``close.&#x27;&#x27; Our new fuzzy PAKE protocol supports completely arbitrary predicates for password ``closeness&#x27;&#x27;. Compared to prior fuzzy PAKE protocols, ours is roughly $2\times$ cheaper in communication, computation, and round complexity.

  匹配依据：MPC: garbled circuits, secure 2 party computation

  </details>

- **Streaming Function Secret Sharing and Its Applications**
  2025-12-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2304)
  Xiangfu Song, Jianli Bai, Ye Dong, Yijian Liu, Yu Zhang, Xianhui Lu, Tianwei Zhang

  <details><summary>摘要 / Abstract</summary>

  Collecting statistics from users of software and online services is crucial to improve service quality, yet obtaining such insights while preserving individual privacy remains a challenge. Function secret sharing (FSS) is a promising tool for this problem. However, FSS-based solutions still face several challenges for streaming analytics, where messages are continuously sent, and secure computation tasks are repeatedly performed over incoming messages. We introduce a new cryptographic primitive called streaming function secret sharing (SFSS), a new variant of FSS that is particularly suitable for secure computation over streaming messages. We formalize SFSS and propose concrete constructions, including SFSS for point functions, predicate functions, and feasibility results for generic functions. SFSS powers several promising applications in a simple and modular fashion, including conditional transciphering, policy-hiding aggregation, and attribute-hiding aggregation. In particular, our SFSS formalization and constructions identify security flaws and efficiency bottlenecks in existing solutions, and SFSS-powered solutions achieve the expected security goal with asymptotically and concretely better efficiency and/or enhanced functionality.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Computationally Succinct Authentication from DCR: Attribute-Based Laconic Function Evaluation and More**
  2025-12-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2307)
  Pierre Meyer, Claudio Orlandi, Lawrence Roy, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  We present the first construction of attribute-based laconic function evaluation (AB-LFE) from the decisional composite residuosity (DCR) assumption. This yields the first example of computationally succinct secure computation from a group-based assumption, avoiding reliance on noisy lattice assumptions such as LWE. Our construction builds on recent work in fully homomorphic MACs and homomorphic secret sharing by Ishai, Li and Lin (FOCS 2025) and Meyer, Orlandi, Roy, and Scholl (Crypto 2025), which we extend by constructing a fully homomorphic MAC for packed vector operations, where the evaluation time of one party is independent of the vector length. As applications, we obtain full-fledged laconic function evaluation (LFE) from the combination of DCR and standard LWE, avoiding the need for sub-exponential modulus-to-noise ratio LWE used in previous work. We also obtain the first constrained pseudorandom function whose master evaluation key is succinct in the constraint. These results highlight the unexplored power of group-based cryptography for succinct secure computation.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **A New Approach to Large Party Beaver-Style MPC with Small Computational Overhead**
  2025-12-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2305)
  Aayush Jain, Huijia Lin, Nuozhou Sun

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) enables $N$ parties to jointly evaluate any function over their private inputs while preserving confidentiality. While decades of research have produced concretely efficient protocols for small to moderate numbers of participants, scaling MPC to thousands of parties remains a central challenge. Most of the existing approaches either incur per-party costs linear in $N$, due to pairwise computations, or rely on heavy cryptographic tools such as homomorphic encryption, which introduces prohibitive overheads when evaluating Boolean circuits. In this work, we introduce a new lightweight approach to designing semi-honest MPC protocols with per-party, per-gate computation and communication costs that are independent of $N$. Our construction leverages the Sparse Learning Parity with Noise (Sparse LPN) assumption in the random oracle model to achieve per-gate costs of $O(k^2 \cdot c(\lambda))$ computation and $O(c(\lambda))$ communication, where $k$ is the sparsity parameter for the Sparse LPN assumption and $c(\lambda)$ is an arbitrarily small super-constant in the security parameter $\lambda$. Assuming Sparse LPN remains hard for any super-constant sparsity, this yields the first semi-honest MPC protocol in the dishonest-majority setting with per-party, per-gate costs bounded by an arbitrarily small super-constant overhead in $\lambda$. Structurally, our MPC instantiates a Beaver-style MPC with the required correlations generated efficiently. Departing from prior approaches that generate Beaver triples either silently (Boyle et al., 2019; 2020; 2022) or through homomorphic computation (Damgård et al., 2012), our focus is on efficiently generating a weaker correlation. In particular, using Sparse LPN we show that if we relax the correctness requirement in generating random Beaver triples to permit a tunably small inverse-polynomial error probability, such triples can be silently generated with arbitrarily small super-constant per-party computation. We then show that such correlations can be used in an efficient online phase similar to Beaver&#x27;s protocol (with a tiny super-constant factor blow-up in communication).

  匹配依据：MPC: secure multi party computation

  </details>

- **ALKAID: Accelerating Three-Party Boolean Circuits by Mixing Correlations and Redundancy (Full Version)**
  2025-12-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2298)
  Ye Dong, Xudong Chen, Xiangfu Song, Yaxi Yang, Wen-jie Lu, Tianwei Zhang, Jianying Zhou, Jin-Song Dong

  <details><summary>摘要 / Abstract</summary>

  Secure three-party computation (3PC) with semi-honest security under an honest majority offers notable efficiency in computation and communication; for Boolean circuits, each party sends a single bit for every AND gate, and nothing for XOR. However, round complexity remains a significant challenge, especially in high-latency networks. Some works can support multi-input AND and thereby reduce online round complexity, but they require \textit{exponential} communication for generating the correlations in either preprocessing or online phase. How to extend the AND gate to multi-input while maintaining high correlation generation efficiency is still not solved. To address this problem, we propose a round-efficient 3PC framework ALKAID for Boolean circuits through improved multi-input AND gate. By mixing correlations and redundancy, we propose a concretely efficient correlation generation approach for small input bits $N 4$. Exploiting the improved multi-input AND gates, we design fast depth-optimized parallel prefix adder and share conversion primitives in 3PC, achieved with new techniques and optimizations for better concrete efficiency. We further apply these optimized primitives to enhance the efficiency of secure non-linear functions in machine learning. We implement ALKAID and extensively evaluate its performance. Compared to state of the arts like ABY3 (CCS&#x27;2018), Trifecta (PoPETs&#x27;2023), and METEOR (WWW&#x27;2023), ALKAID enjoys $1.5\times$--$2.5\times$ efficiency improvements for boolean primitives and non-linear functions, with better or comparable communication.

  匹配依据：MPC: secure three party computation

  </details>

- **Theodosian: A Deep Dive into Memory-Hierarchy-Centric FHE Acceleration**
  2025-12-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.18345)
  Wonseok Choi, Hyunah Yu, Jongmin Kim, Hyesung Ji, Jaiyoung Park, Jung Ho Ahn

  <details><summary>摘要 / Abstract</summary>

  Fully homomorphic encryption (FHE) enables secure computation on encrypted data, mitigating privacy concerns in cloud and edge environments. However, due to its high compute and memory demands, extensive acceleration research has been pursued across diverse hardware platforms, especially GPUs. In this paper, we perform a microarchitectural analysis of CKKS, a popular FHE scheme, on modern GPUs. Focusing on the memory hierarchy, we demonstrate that dominant kernels remain bound by the on-chip L2 cache despite its high bandwidth, exposing a persistent inner memory wall beyond the conventional off-chip DRAM bottleneck. Further, we reveal that the overall CKKS throughput is constrained by low per-kernel hardware utilization, caused by insufficient intra-kernel parallelism. Motivated by these findings, we introduce Theodosian, a set of complementary, memory-aware optimizations that improve cache efficiency and reduce runtime overheads. Theodosian achieves 1.45--1.83x performance improvements over a highly optimized baseline, Cheddar, across representative CKKS workloads. On an RTX 5090, we reduce the bootstrapping latency for 32,768 complex numbers from 22.1ms to 15.2ms, and further to 12.8ms with additional algorithmic optimizations, establishing a new state-of-the-art GPU performance to the best of our knowledge.

  匹配依据：MPC: secure computation

  </details>

- **Experimental Efficient Source-Independent Quantum Secret Sharing against Coherent Attacks**
  2025-12-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.18325)
  Yi-Ran Xiao, Hua-Lei Yin, Wen-Ji Hua, Xiao-Yu Cao, Zeng-Bing Chen

  <details><summary>摘要 / Abstract</summary>

  Source-independent quantum secret sharing (SI QSS), while essential for secure multiuser cryptographic operations in quantum networks, faces significant implementation challenges stemming from the inherent complexity of generating and distributing multipartite entangled states. Recently, a resource-efficient SI QSS protocol utilizing entangled photon pairs combined with a postmatching method has been proposed to address this limitation. In this Letter, we report an experimental demonstration of this protocol using high-fidelity polarization-entangled photon pairs in a star topology. For a three-user network, we obtain secure key rates of 21.18, 4.69, and 1.71 kbps under single-user channel losses of 7.6, 10.9, and 12.9 dB respectively. Furthermore, under conditions of equal channel loss per user, we achieve secure key rates of 6.97, 6.46, and 5.88 kbps for three-, four-, and five-user scenarios respectively. These results demonstrate the advantageous independence of the key rate from the number of users. Our work paves the way for large-scale deployment of SI QSS in multiuser quantum networks.

  匹配依据：MPC: secret sharing

  </details>

- **An Ideal Linear Secret Sharing Scheme for Complete $t$-Partite $k$-Uniform Hypergraph Access Structures**
  2025-12-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2295)
  Chunming Tang, Zheng Chen, Haonan Fu, Hongwei Zhu

  <details><summary>摘要 / Abstract</summary>

  Secret sharing schemes represent a crucial cryptographic protocol, with linear codes serving as a primary tool for their construction. This paper systematically investigates the construction of ideal secret sharing schemes for complete $t$-partite $k$-uniform hypergraph access structures using linear codes as the tool. First, it is proved that the generator matrix $G$ of an ideal linear code realizing a complete $t$-partite $2$-uniform hypergraph access structure must have a rank of $2$. Simultaneously, a novel method for constructing an ideal secret sharing scheme that realizes such access structures is proposed. Building on this foundation, the case of complete $t$-partite $2$-uniform hypergraphs is extended to complete $t$-partite $k$-uniform hypergraphs, and a method for constructing ideal secret sharing schemes to realize them is provided. Compared with existing approaches, both Shamir’s method and the scheme proposed by Brickell et al. are special cases of our proposed approach.

  匹配依据：MPC: secret sharing

  </details>

- **Towards Practical Multi-Party Hash Chains using Arithmetization-Oriented Primitives - With Applications to Threshold Hash-Based Signatures**
  2025-12-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2290)
  Alexandre Adomnicăi

  <details><summary>摘要 / Abstract</summary>

  Despite their simplicity and quantum-resistant security properties, the deployment of hash chains in distributed settings through secure multi-party computation (MPC) has been demonstrated to be impractical when employing traditional hash functions (i.e., SHA2/SHA3) due to their high number of non-linear gates which lead to heavy computational costs. In this work, we present a comprehensive evaluation of hash chain computations over MPC using arithmetization-oriented (AO) primitives, specifically focusing on the Poseidon2 family of hash functions. We systematically analyze the MPC-friendliness of various Poseidon2 instantiations across different prime fields and parameter choices to minimize both multiplicative depth and preprocessing requirements. We conduct extensive benchmarks using the MP-SPDZ framework across three state-of-the-art MPC protocols under varying network conditions and adversarial models. We further explore practical applications to threshold cryptography, presenting optimized implementations of threshold hash-based signatures that achieve signing times less than 1 second in a 3-party setting for practical parameter sets. Specifically, we demonstrate how structural parallelism in hash-based signatures can be exploited to batch independent hash chains within a single MPC execution, and introduce a time-memory trade-off that enables non-interactive online signature generation through systematic precomputation of all chain intermediates. Our work suggests the practical viability of moderate length AO-based hash chains for MPC applications.

  匹配依据：MPC: secure multi party computation

  </details>

- **Scalable Multiterminal Key Agreement via Error-Correcting Codes**
  2025-12-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.18025)
  Benjamin D. Kim, Daniel Alabi, Lav R. Varshney

  <details><summary>摘要 / Abstract</summary>

  We explore connections between secret sharing and secret key agreement, which yield a simple and scalable multiterminal key agreement protocol. In our construction, we use error-correcting codes, specifically Reed-Solomon codes with threshold reconstruction, to ensure no information is leaked to an eavesdropper. We then derive novel bounds for both full-rank maximum distance separable codes and our scheme&#x27;s secret key capacity, using key capacity&#x27;s duality with multivariate mutual information.

  匹配依据：MPC: secret sharing

  </details>

- **MIOPE: A Modular framework for Input and Output Privacy in Ensemble inference**
  2025-12-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2287)
  Kyrian Maat, Gareth T. Davies, Zoltán Ádám Mann, Joppe W. Bos, Francesco Regazzoni

  <details><summary>摘要 / Abstract</summary>

  We introduce a simple yet novel framework for privacy-preserving machine learning inference that allows a client to query multiple models without a trusted third party aggregator by leveraging homomorphically encrypted model evaluation and multi-party computation. This setting allows for dispersed training of models such that a client can query each separately, and aggregate the results of this `ensemble inference&#x27;; this avoids the data leakage inherent to techniques that train collectively such as federated learning. Our framework, which we call MIOPE, allows the data providers to keep the training phase local to provide tighter control over these models, and additionally provides the benefit of easily retraining to improve inference of the ensemble. MIOPE uses homomorphic encryption to keep the querying client&#x27;s data private and multi-party computation to hide the individual model outputs. We illustrate the design and trade-offs of input- and output-hiding ensemble inference as provided by MIOPE and compare performance to a centralized approach.We evaluate our approach with a standard dataset and various regression models and observe that the MIOPE framework can lead to accuracy scores that are only marginally lower than centralized learning. The modular design of our approach allows the system to adapt to new data, better models, or security requirements of the involved parties.

  匹配依据：MPC: multi party computation

  </details>

- **UFOs: An Ultra-fast Toolkit for Multiparty Computation of Small Elements**
  2025-12-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2281)
  Jiacheng Gao, Moyang Xie, Yuan Zhang, Sheng Zhong

  <details><summary>摘要 / Abstract</summary>

  In many secure multiparty computation (MPC) applications, the semantic domains of some operands are much smaller than the underlying arithmetic field or ring. The arithmetic domain is typically chosen to meet computation and security requirements (e.g., a 128-bit prime field), whereas the actual data may consist of only a few bits, such as 4-bit values in a 16-category classification task. This mismatch can lead to substantial communication and computation overhead in existing MPC protocols, which typically treat data of different ranges uniformly. We introduce UFO$_\mathrm{s}$, an ultra-fast toolkit for MPC on small elements, with optimized protocols for one-hot encoding, comparison, and digit decomposition. For $t=2^k$, our random one-hot vector generator attains, in the fan-in-two arithmetic-circuit model, the lower bounds of $t-\log t-1$ multiplication gates and $\lceil\log\log t\rceil$ multiplication depth. Our comparison protocol applies to any public small domain, while DigitDecomp avoids binary expansion and supports any public base $t&gt;1$. Using these primitives, we construct a higher-radix sorting protocol for large field elements. Experiments confirm the resulting gains in random one-hot vector generation, digit decomposition, and sorting. In particular, our sorting protocol achieves a $3.4\times$ online and $1.4\times$ offline speedup over Hamada et al.&#x27;s radix-sort baseline when sorting $2^{16}$ elements among five parties.

  匹配依据：MPC: multiparty computation, secure multiparty computation

  </details>

- **Leakage-Resilient Multi-Party Computation: Protecting the Evaluator in Circuits Garbling**
  2025-12-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2264)
  Francesco Berti, Itamar Levi

  <details><summary>摘要 / Abstract</summary>

  Garbling schemes allow two parties to compute a joint function on private inputs without revealing them. Yet, a semi-honest garbler might exploit hardware/software sidechannel leakages from the evaluator. An alarming threat with no concrete solution yet. Using the homomorphic properties of ElGamal encryption, we can prevent such leakage-based attacks.

  匹配依据：MPC: garbling schemes, multi party computation

  </details>

- **FAME: FPGA Acceleration of Secure Matrix Multiplication with Homomorphic Encryption**
  2025-12-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.15515)
  Zhihan Xu, Rajgopal Kannan, Viktor K. Prasanna

  <details><summary>摘要 / Abstract</summary>

  Homomorphic Encryption (HE) enables secure computation on encrypted data, addressing privacy concerns in cloud computing. However, the high computational cost of HE operations, particularly matrix multiplication (MM), remains a major barrier to its practical deployment. Accelerating homomorphic encrypted MM (HE MM) is therefore crucial for applications such as privacy-preserving machine learning. In this paper, we present a bandwidth-efficient FPGA implementation of HE MM. We first develop a cost model to evaluate the on-chip memory requirements for a given set of HE parameters and input matrix sizes. Our analysis shows that optimizing on-chip memory usage is critical for scalable and efficient HE MM. To this end, we design a novel datapath for Homomorphic Linear Transformation (HLT), the primary bottleneck in HE MM. The proposed datapath significantly reduces off-chip memory traffic and on-chip memory demand by enabling fine-grained data reuse. Leveraging this datapath, we introduce FAME, the first FPGA-based accelerator specifically tailored for HE MM. FAME supports arbitrary matrix shapes and is configurable across a wide range of HE parameter sets. We implement FAME on an Alveo U280 FPGA and evaluate its performance across diverse matrix sizes and shapes. Experimental results show that FAME achieves an average speedup of 221x over state-of-the-art CPU-based implementations, demonstrating its scalability and practicality for large-scale consecutive HE MM and real-world workloads.

  匹配依据：MPC: secure computation

  </details>

- **TSS-PV: Traceable Secret Sharing with Public Verifiability**
  2025-12-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2261)
  Duc Anh Luong, Jong Hwan Park, Changmin Lee, Hyoseung Kim

  <details><summary>摘要 / Abstract</summary>

  High-value custodial systems require both Public Verifiability to audit key distribution and Traceability to identify insider leakage via black-box \textit{reconstruction boxes}. Existing schemes achieve one property but not both, leaving practical systems exposed to either undetectable dealer misbehavior or untraceable share leakage. Combining these properties introduces the Provenance Paradox: a verifiability-aware reconstruction box with access to verification predicates and public transcripts can reject dummy shares used for tracing because they have no provenance in the public transcript. We present TSS-PV, the first publicly verifiable traceable secret sharing scheme that resolves this paradox. Our key insight is to inject indistinguishable dummy shares during the sharing phase itself, ensuring they are committed to the public transcript before any reconstruction box is constructed. We formalize syntax and security under a modular adversarial model: public verifiability holds against fully malicious dealers and parties; traceability identifies leaking parties after honest distribution; and non-imputability prevents a malicious dealer from framing honest parties. Both tracing properties assume a verifiability-aware perfect reconstruction box. We instantiate TSS-PV over cyclic groups using Schnorr-based NIZKs including a new $\Sigma$-protocol for power-chain relations and a recent generic tracing framework (CRYPTO&#x27;24). Public verification costs scale linearly in the number of parties; tracing costs are quadratic. A Curve25519 prototype on commodity hardware demonstrates practicality: for $32\text{ - }256$ parties, distribution verification completes in $\approx 14\text{ - }107$ ms, tracing in $\approx0.23\text{ - }78$ s, and trace verification in $\approx 0.13\text{ - }26$ s.

  匹配依据：MPC: secret sharing

  </details>

- **Scalable Private Set Intersection over Distributed Encrypted Data**
  2025-12-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2256)
  Seunghun Paik, Nirajan Koirala, Jack Nero, Hyunjung Son, Yunki Kim, Jae Hong Seo, Taeho Jung

  <details><summary>摘要 / Abstract</summary>

  Finding intersections across sensitive data is a core operation in many real-world data-driven applications, such as healthcare, anti-money laundering, financial fraud, or watchlist applications. These applications often require large-scale collaboration across thousands or more independent sources, such as hospitals, financial institutions, or identity bureaus, where all records must remain encrypted during storage and computation, and are typically outsourced to dedicated/cloud servers. Such a highly distributed, large-scale, and encrypted setting makes it very challenging to apply existing solutions, e.g., (multi-party) private set intersection (PSI) or private membership test (PMT). In this paper, we present Distributed and Outsourced PSI (DO-PSI), an efficient and scalable PSI protocol over outsourced, encrypted, and highly distributed datasets. Our key technique lies in a generic threshold fully homomorphic encryption (FHE) based framework that aggregates equality results additively, which ensures high scalability to a large number of data sources. In addition, we propose a novel technique called \textit{nonzero-preserving mapping}, which maps a zero vector to zero and preserves nonzero values. This allows homomorphic equality tests over a smaller base field, substantially reducing computation while enabling higher-precision representations. We implement DO-PSI and conduct extensive experiments, showing that ours substantially outperforms existing methods in both computation and communication overheads. Our protocol handles a billion-scale set distributed and outsourced to a thousand data owners within one minute, directly reflecting large-scale deployment scenarios, and achieves up to an 11.16$\times$ improvement in end-to-end latency over prior state-of-the-art methods.

  匹配依据：MPC: private set intersection

  </details>

- **Privacy-Preserving Feature Valuation in Vertical Federated Learning Using Shapley-CMI and PSI Permutation**
  2025-12-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.14767)
  Unai Laskurain, Aitor Aguirre-Ortuzar, Urko Zurutuza

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) is an emerging machine learning paradigm that enables multiple parties to collaboratively train models without sharing raw data, ensuring data privacy. In Vertical FL (VFL), where each party holds different features for the same users, a key challenge is to evaluate the feature contribution of each party before any model is trained, particularly in the early stages when no model exists. To address this, the Shapley-CMI method was recently proposed as a model-free, information-theoretic approach to feature valuation using Conditional Mutual Information (CMI). However, its original formulation did not provide a practical implementation capable of computing the required permutations and intersections securely. This paper presents a novel privacy-preserving implementation of Shapley-CMI for VFL. Our system introduces a private set intersection (PSI) server that performs all necessary feature permutations and computes encrypted intersection sizes across discretized and encrypted ID groups, without the need for raw data exchange. Each party then uses these intersection results to compute Shapley-CMI values, computing the marginal utility of their features. Initial experiments confirm the correctness and privacy of the proposed system, demonstrating its viability for secure and efficient feature contribution estimation in VFL. This approach ensures data confidentiality, scales across multiple parties, and enables fair data valuation without requiring the sharing of raw data or training models.

  匹配依据：MPC: private set intersection

  </details>

- **QoeSiGN: Towards Qualified Collaborative eSignatures**
  2025-12-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.13613)
  Karl W. Koch, Stephan Krenn, Alexandra Hofer

  <details><summary>摘要 / Abstract</summary>

  eSignatures ensure data&#x27;s authenticity, non-repudiation, and integrity. EU&#x27;s eIDAS regulation specifies, e.g., advanced and qualified (QES) eSignatures. While eSignatures&#x27; concrete legal effects depend on the individual case, QESs constitute the highest level of technical protection and authenticity under eIDAS. QESs are based on a qualified certificate issued by a qualified trust service provider (QTSP). Despite legal requirements, technically, a QTSP represents a single point of failure. Contrary, privacy-preserving collaborative computations (P2C2s) have become increasingly practical in recent years; yet lacking an extensive investigation on potential integrations in the QES landscape. We perform a threat analysis on the QES-creation process of Austria&#x27;s national eID, using STRIDE and a DREAD-like model to extract requirement challenges (RCs) primarily related to: (1) Distributed Service Robustness, (2) Agile Crypto Deployment, and (3) Active User Involvement. To address these RCs, we present QoeSiGN, utilizing novel P2C2 technologies. While currently no P2C2 addresses all RCs, legal aspects, and practical efficiency simultaneously, QoeSiGN gives instantiation possibilities for different needs. For instance, &quot;Multi-Party HSMs&quot; for distributed hardware-secured computations; or secure multi-party computation (software) for highest crypto agility and user involvement, where the user participates in the QES computation. Deployment-wise, QTSPs would need to adapt the signing process and setup trusted communication channels. Legal-wise, QoeSiGN&#x27;s implementation appears permissible, needing further analysis for realization. Technically, QoeSiGN addresses some regulation requirements better than the current solution, such as &quot;sole control&quot; or crypto agility. Our identified threats and extracted requirements can be transferred to the general QES ecosystem.

  匹配依据：MPC: secure multi party computation

  </details>

- **Nimbus: Secure and Efficient Two-Party Inference for Transformers**
  2025-12-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.15707) · [IACR ePrint](https://eprint.iacr.org/2025/2250)
  Zhengyi Li, Kang Yang, Jin Tan, Wen-jie Lu, Haoqi Wu, Xiao Wang, Yu Yu, Derun Zhao, Yancheng Zheng, Minyi Guo, Jingwen Leng

  <details><summary>摘要 / Abstract</summary>

  Transformer models have gained significant attention due to their power in machine learning tasks. Their extensive deployment has raised concerns about the potential leakage of sensitive information during inference. However, when being applied to Transformers, existing approaches based on secure two-party computation (2PC) bring about efficiency limitations in two folds: (1) resource-intensive matrix multiplications in linear layers, and (2) complex non-linear activation functions like $\mathsf{GELU}$ and $\mathsf{Softmax}$. This work presents a new two-party inference framework $\mathsf{Nimbus}$ for Transformer models. For the linear layer, we propose a new 2PC paradigm along with an encoding approach to securely compute matrix multiplications based on an outer-product insight, which achieves $2.9\times \sim 12.5\times$ performance improvements compared to the state-of-the-art (SOTA) protocol. For the non-linear layer, through a new observation of utilizing the input distribution, we propose an approach of low-degree polynomial approximation for $\mathsf{GELU}$ and $\mathsf{Softmax}$, which improves the performance of the SOTA polynomial approximation by $2.9\times \sim 4.0\times$, where the average accuracy loss of our approach is 0.08\% compared to the non-2PC inference without privacy. Compared with the SOTA two-party inference, $\mathsf{Nimbus}$ improves the end-to-end performance of BERT inference by $2.7\times \sim 4.7\times$ across different network settings.

  匹配依据：MPC: secure two party computation

  </details>

- **Multi-Party Private Join**
  2025-12-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2254)
  Anja Lehmann, Christian Mouchet, Andrey Sidorenko

  <details><summary>摘要 / Abstract</summary>

  A multi-party private join (MPPJ) protocol enables multiple source parties to provide a receiver party with the inner joins over their respective datasets, while revealing as little information as possible. There is currently no protocol that directly and efficiently enables such a MPPJ beyond the two- or three-party setting. The presently known protocols either achieve weaker functionality (e.g., multi- party private set intersection protocols) or more general ones (e.g., private-join-compute and generic secure multi-party computation protocols) and are therefore more costly to run for the sources. This work formally introduces MPPJ as an explicit goal, and proposes an efficient, helper-assisted protocol that achieves 𝑛-party inner joins with small leakage and close-to-optimal overhead for the sources. Specifically, for 𝑛 databases with 𝑚 rows, it requires only a single 𝑂 (𝑚) upload from the sources to the helper, and a single 𝑂 (𝑛 · 𝑚) download from the helper to the receiver. Moreover, the helper is entirely oblivious: it enables the efficiency and simplicity goals we are striving for, but it does not learn anything about the computation it facilitates. We formally model and prove the security of our protocol from standard assumptions, in the passive-adversary model. Then, we provide an open-source implementation and an extensive performance evaluation. According to our experiments, our protocol requires 1.02 to 20 times less communication than a current private-join-compute protocol (with no computation over the join) for 2 to 6 parties and input database sizes from 1.5K to 250K records. Finally, we demonstrate the versatility of our approach by extending our protocol to threshold-joins.

  匹配依据：MPC: private set intersection, secure multi party computation

  </details>

- **SoK: Demystifying the multiverse of MPC protocols**
  2025-12-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.11699)
  Roberta De Viti, Vaastav Anand, Pierfrancesco Ingo, Deepak Garg

  <details><summary>摘要 / Abstract</summary>

  This paper systematizes knowledge on the performance of Multi-Party Computation (MPC) protocols. Despite strong privacy and correctness guarantees, MPC adoption in real-world applications remains limited by high costs (especially in the malicious setting) and lack of guidance on choosing suitable protocols for concrete workloads. We identify the theoretical and practical parameters that shape MPC efficiency and conduct an extensive experimental study across diverse benchmarks. Our analysis discusses the trade-offs between protocols, and highlights which techniques align best with different application scenarios and needs. By providing actionable guidance for developers and outlining open challenges for researchers, this work seeks to narrow the gap between MPC theory and practice.

  匹配依据：MPC: multi party computation

  </details>

- **An LLVM-Based Optimization Pipeline for SPDZ**
  2025-12-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.11112)
  Tianye Dai, Hammurabi Mendes, Heuichan Lim

  <details><summary>摘要 / Abstract</summary>

  Actively secure arithmetic MPC is now practical for real applications, but performance and usability are still limited by framework-specific compilation stacks, the need for programmers to explicitly express parallelism, and high communication overhead. We design and implement a proof-of-concept LLVM-based optimization pipeline for the SPDZ protocol that addresses these bottlenecks. Our front end accepts a subset of C with lightweight privacy annotations and lowers it to LLVM IR, allowing us to reuse mature analyses and transformations to automatically batch independent arithmetic operations. Our back end performs data-flow and control-flow analysis on the optimized IR to drive a non-blocking runtime scheduler that overlaps independent operations and aggressively overlaps communication with computation; when enabled, it can map batched operations to GPU kernels. This design preserves a low learning curve by using a mainstream language and hiding optimization and hardware-specific mechanics from programmers. We evaluate the system on controlled microbenchmarks against MP-SPDZ, focusing on online phase performance. Our CPU back end achieves up to 5.56 times speedup under intermediate and heavy algebraic workloads, shows strong scaling with thread count, and our GPU back end scales better as the input size increases. Overall, these results indicate that leveraging LLVM with protocol-aware scheduling is an effective architectural direction for extracting parallelism without sacrificing usability.

  匹配依据：MPC: mpc (context)

  </details>

- **Device Independent Quantum Secret Sharing Using Multiparty Pseudo-telepathy Game**
  2025-12-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.09699)
  Santanu Majhi, Goutam Paul

  <details><summary>摘要 / Abstract</summary>

  Device-independent quantum secret sharing (DI-QSS) provides security against untrusted quantum devices. While device-independent quantum key distribution (DI-QKD) using Mermin-Peres magic square game [Zhen et al., Phys. Rev. Lett, 2023] has been proposed, we present the first DI-QSS protocol based on a pseudo-telepathy parity game without requiring dedicated rounds and specific basis configuration, unlike CHSH-based DI-QSS schemes [Zhang et al., Phys. Rev. A, 2024]. Our scheme simultaneously certifies device-independence and key generation using a single test, achieving optimal performance for a seven-qubit GHZ state configuration. Security against collective attacks is analyzed, and a positive key rate is obtained under white noise and photon loss. Moreover, we show a bitwise advantage over the previous protocol for producing the same raw key length.

  匹配依据：MPC: secret sharing

  </details>

- **Labeled Delegated PSI and its Applications in the Public Sector**
  2025-12-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.08558)
  Kristof Verslype, Florian Kerschbaum, Cyprien Delpech de Saint Guilhem, Bart De Decker, Jorn Lapon

  <details><summary>摘要 / Abstract</summary>

  Sensitive citizen data, such as social, medical, and fiscal data, is heavily fragmented across public bodies and the private domain. Mining the combined data sets allows for new insights that otherwise remain hidden. Examples are improved healthcare, fraud detection, and evidence-based policy making. (Multi-party) delegated private set intersection (D-PSI) is a privacy-enhancing technology to link data across multiple data providers using a data collector. However, before it can be deployed in these use cases, it needs to be enhanced with additional functions, e.g., securely delivering payload only for elements in the intersection. Although there has been recent progress in the communication and computation requirements of D-PSI, these practical obstacles have not yet been addressed. This paper is the result of a collaboration with a governmental organization responsible for collecting, linking, and pseudonymizing data. Based on their requirements, we design a new D-PSI protocol with composable output functions, including encrypted payload and pseudonymized identifiers. We show that our protocol is secure in the standard model against colluding semi-honest data providers and against a non-colluding, possibly malicious independent party, the data collector. It, hence, allows to privately link and collect data from multiple data providers suitable for deployment in these use cases in the public sector.

  匹配依据：MPC: private set intersection

  </details>

- **Ideal Private Simultaneous Messages Schemes and Their Applications**
  2025-12-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2217)
  Keitaro Hiwatashi, Reo Eriguchi

  <details><summary>摘要 / Abstract</summary>

  Private Simultaneous Messages (PSM) is a minimal model for secure computation, where two parties, Alice and Bob, have private inputs $x,y$ and a shared random string. Each of them sends a single message to an external party, Charlie, who can compute $f(x,y)$ for a public function $f$ but learns nothing else. The problem of narrowing the gap between upper and lower bounds on the communication complexity of PSM has been widely studied, but the gap still remains exponential. In this work, we study the communication complexity of PSM from a different perspective and introduce a special class of PSM, referred to as \textit{ideal PSM}, in which each party&#x27;s message length attains the minimum, that is, their messages are taken from the same domain as inputs. We initiate a systematic study of ideal PSM with a complete characterization, several positive results, and applications. First, we provide a characterization of the class of functions that admit ideal PSM, based on permutation groups acting on the input domain. This characterization allows us to derive asymptotic upper bounds on the total number of such functions and a complete list for small domains. We also present several infinite families of functions of practical interest that admit ideal PSM. Interestingly, by simply restricting the input domains of these ideal PSM schemes, we can recover most of the existing PSM schemes that achieve the best known communication complexity in various computation models. As applications, we show that these ideal PSM schemes yield novel communication-efficient PSM schemes for functions with sparse or dense truth-tables and those with low-rank truth-tables. Furthermore, we obtain a PSM scheme for general functions that improves the constant factor in the dominant term of the best known communication complexity. An additional advantage is that our scheme simplifies the existing construction by avoiding the hierarchical design of internally invoking PSM schemes for smaller functions.

  匹配依据：MPC: secure computation

  </details>

- **Obfuscating Pseudorandom Functions is Post-Quantum Complete**
  2025-12-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2215)
  Pedro Branco, Abhishek Jain, Akshayaram Srinivasan

  <details><summary>摘要 / Abstract</summary>

  The last decade has seen remarkable success in designing and uncovering new applications of indistinguishability obfuscation (i$\mathcal{O}$). The main pressing question in this area is whether post-quantum i$\mathcal{O}$ exists. All current lattice-based candidates rely on new, non-standard assumptions, many of which are known to be broken. To make systematic progress on this front, we investigate the following question: can general-purpose i$\mathcal{O}$ be reduced, assuming only learning with errors (LWE), to obfuscating a smaller class of functions? The specific class of functions we consider are {\em pseudorandom functions} (PRFs), which constitute a natural functionality of independent interest. We show the following results: - We construct exponentially-efficient i$\mathcal{O}$ (xi$\mathcal{O}$) for general circuits based on LWE in the pseudorandom oracle model -- a variant of the Random Oracle model (Jain et al., CRYPTO&#x27;23). Our construction requires the pseudorandom oracle model heuristic to hold for a specific pseudorandom function and we prove its security against classical adversaries. - We construct (post-quantum) i$\mathcal{O}$ for general circuits in the standard model based on (post-quantum) sub-exponentially secure LWE and (post-quantum) sub-exponentially secure {\em average-case} i$\mathcal{O}$ -- a natural notion of i$\mathcal{O}$ for pseudorandom functions that we define. To obtain these results, we generalize the ``encrypt-evaluate-decrypt&#x27;&#x27; paradigm used in prior works by replacing the use of fully homomorphic encryption with succinct secure two-party computation where parties obtain additive output shares (Boyle et al., EUROCRYPT&#x27;25 and Abram et al., STOC&#x27;25).

  匹配依据：MPC: secure two party computation

  </details>

- **Linear codes over a mixed-alphabet ring and their Gray images with applications to projective and locally repairable codes**
  2025-12-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.07343)
  Leijo Jose, Lavanya G., Anuradha Sharma

  <details><summary>摘要 / Abstract</summary>

  Let $m \geq 2$ be an integer, and let $\mathbb{F}_q$ be the finite field of prime power order $q.$ Let $\mathcal{R}=\frac{\mathbb{F}_q[u]}{\langle u^2 \rangle}\times \mathbb{F}_q$ be the mixed-alphabet ring, where $\frac{\mathbb{F}_q[u]}{\langle u^2 \rangle}$ is the quasi-Galois ring with maximal ideal $\langle u\rangle$ of nilpotency index $2$ and residue field $\mathbb{F}_q.$ In this paper, we construct four infinite families of linear codes over the ring $\frac{\mathbb{F}_q[u]}{\langle u^2 \rangle}$ whose defining sets are certain non-empty subsets of $\mathcal{R}^m$ associated with three simplicial complexes of $\mathbb{F}_q^m,$ each possessing a single maximal element. We explicitly determine the parameters and Lee weight distributions of these codes. We also study their Gray images and identify several infinite families of few-weight codes over $\mathbb{F}_q,$ as well as an infinite family of minimal, near-Griesmer and distance-optimal codes over $\mathbb{F}_q.$ We also observe that their Gray images are self-orthogonal codes for $q=2$ or $3.$ We determine spanning matrices of these codes. Leveraging this result, we provide two constructions of infinite families of projective few-weight codes over $\mathbb{F}_q$ with new parameters. As an application of our newly constructed minimal codes over $\mathbb{F}_q,$ we examine the minimal access structures of Masseys secret sharing schemes based on their duals and determine the number of dictatorial participants in these schemes. Finally, we investigate the locality properties of our newly constructed projective codes and show that these codes have locality either $2$ or $3.$ As a consequence, we obtain four infinite families of $q$-ary locally repairable codes (LRCs) with locality $2,$ and two infinite families of binary LRCs with locality $3.$

  匹配依据：MPC: secret sharing

  </details>

- **Chromatic Feature Vectors for 2-Trees: Exact Formulas for Partition Enumeration with Network Applications**
  2025-12-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.07120)
  J. Allagan, G. Morgan, S. Langley, R. Lopez-Bonilla, V. Deriglazov

  <details><summary>摘要 / Abstract</summary>

  We establish closed-form enumeration formulas for chromatic feature vectors of 2-trees under the bichromatic triangle constraint. These efficiently computable structural features derive from constrained graph colorings where each triangle uses exactly two colors, forbidding monochromatic and rainbow triangles, a constraint arising in distributed systems where components avoid complete concentration or isolation. For theta graphs Theta_n, we prove r_k(Theta_n) = S(n-2, k-1) for k &gt;= 3 (Stirling numbers of the second kind) and r_2(Theta_n) = 2^(n-2) + 1, computable in O(n) time. For fan graphs Phi_n, we establish r_2(Phi_n) = F_{n+1} (Fibonacci numbers) and derive explicit formulas r_k(Phi_n) = sum_{t=k-1}^{n-1} a_{n-1,t} * S(t, k-1) with efficiently computable binomial coefficients, achieving O(n^2) computation per component. Unlike classical chromatic polynomials, which assign identical features to all n-vertex 2-trees, bichromatic constraints provide informative structural features. While not complete graph invariants, these features capture meaningful structural properties through connections to Fibonacci polynomials, Bell numbers, and independent set enumeration. Applications include Byzantine fault tolerance in hierarchical networks, VM allocation in cloud computing, and secret-sharing protocols in distributed cryptography.

  匹配依据：MPC: secret sharing

  </details>

- **AgentCrypt: Advancing Privacy and (Secure) Computation in AI Agent Collaboration**
  2025-12-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.08104) · [IACR ePrint](https://eprint.iacr.org/2025/2216)
  Harish Karthikeyan, Yue Guo, Leo de Castro, Antigoni Polychroniadou, Udari Madhushani Sehwag, Leo Ardon, Sumitra Ganesh, Manuela Veloso

  <details><summary>摘要 / Abstract</summary>

  As AI agents increasingly operate in complex environments, ensuring reliable, context-aware privacy is critical for regulatory compliance. Traditional access controls are insufficient because privacy risks often arise after access is granted; agents may inadvertently compromise privacy during reasoning by messaging humans, leaking context to peers, or executing unsafe tool calls. Existing approaches typically treat privacy as a binary constraint, overlooking nuanced, computation-dependent requirements. Furthermore, Large Language Model (LLM) agents are inherently probabilistic, lacking formal guarantees for security-critical operations. To address this, we introduce AgentCrypt, a three-tiered framework for secure agent communication that adds a deterministic protection layer atop any AI platform. AgentCrypt spans the full spectrum of privacy needs: from unrestricted data exchange (Level 1), to context-aware masking (Level 2), up to fully encrypted computation using Homomorphic Encryption (Level 3). Unlike prompt-based defenses, our approach guarantees that tagged data privacy is strictly preserved even when the underlying model errs. Security is decoupled from the agent&#x27;s probabilistic reasoning, ensuring sensitive data remains protected throughout the computational lifecycle. AgentCrypt enables collaborative computation on otherwise inaccessible data, overcoming barriers like data silos. We implemented and validated it using LangGraph and Google ADK, demonstrating versatility across architectures. Finally, we introduce a benchmark dataset simulating privacy-critical tasks to enable systematic evaluation and foster the development of trustworthy, regulatable machine learning systems.

  匹配依据：MPC: secure computation

  </details>

- **Accelerating TFHE with Sorted Bootstrapping Techniques**
  2025-12-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2214)
  Loris Bergerat, Jean-Baptiste Orfila, Adeline Roux-Langlois, Samuel Tap

  <details><summary>摘要 / Abstract</summary>

  Fully Homomorphic Encryption (FHE) enables secure computation over encrypted data, offering a breakthrough in privacy-preserving computing. Despite its promise, the practical deployment of FHE has been hindered by the significant computational overhead, especially in general-purpose bootstrapping schemes. In this work, we build upon the recent advancements of [LY23] to introduce a variant of the functional/programmable bootstrapping. By carefully sorting the steps of the blind rotation, we reduce the overall number of external products without compromising correctness. To further enhance efficiency, we propose a novel modulus-switching technique that increases the likelihood of satisfying pruning conditions, reducing computational overhead. Extensive benchmarks demonstrate that our method achieves a speedup ranging from 1.75x to 8.28x compared to traditional bootstrapping and from 1.26x to 2.14x compared to [LY23] bootstrapping techniques. Moreover, we show that this technique is better adapted to the IND-CPA-D security model by reducing the performance downgrade it implies.

  匹配依据：MPC: secure computation

  </details>

- **A General Framework for Registered Functional Encryption via User-Specific Pre-Constraining**
  2025-12-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2207)
  Tapas Pal, Robert Schädlich

  <details><summary>摘要 / Abstract</summary>

  We present a unified framework for constructing registered attribute-based encryption (RABE) and registered functional encryption (RFE) from the standard (bilateral) $k$-Lin assumption in asymmetric bilinear pairing groups. Specifically, our schemes capture the following functionalities. - RABE for logspace Turing machines. We present the first RABE for deterministic and nondeterministic logspace Turing machines (TMs), corresponding to the uniform complexity classes $\mathsf L$ and $\mathsf{NL}$. That is, we consider policies $g$ computable by a TM with a polynomial time bound $T$ and a logarithmic space bound $S$. The public parameters of our schemes scale only with the number of states of the TM, but remain independent of the attribute length and the bounds $T,S$. Thus, our system is capable of verifying unbounded-length attributes $\mathbf y$ while the maximum number of states needs to be fixed upfront. - RFE for attribute-based attribute-weighted sums (AB-AWS). Building upon our RABE, we develop RFE for AB-AWS. In this functionality, a function is described by a tuple $f=(g,h)$, takes $(\mathbf y, \{(\mathbf x_j, \mathbf z_j)\}_{j\in[N]})$ as input for an unbounded integer $N$, and outputs $\sum_{j\in[N]}\mathbf z_jh(\mathbf x_j)^\top$ if and only if $g(\mathbf y) = 0$. Here, $\{\mathbf z_j\}_j$ are private inputs that are hidden in the ciphertext, whereas $\mathbf y$ and $\{\mathbf x_j\}_j$ can be public. Our construction can instantiate $g,h$ with deterministic logspace TMs, while a previous construction due to [Pal and Schädlich, Eprint 2025] only supports arithmetic branching programs (ABPs), i.e. a non-uniform model of computation. - RFE for attribute-based quadratic functions (AB-QF). Furthermore, we build the first RFE for AB-QF with compact ciphertexts. In this functionality, a function is described by a tuple $f=(g,\mathbf h)$, takes input $(\mathbf y,(\mathbf z_1,\mathbf z_2))$ and outputs $(\mathbf z_1\otimes\mathbf z_2)\mathbf h^\top$ if and only if $g(\mathbf y)=0$. Here, $(\mathbf z_1, \mathbf z_2)$ are private inputs whereas the attribute $\mathbf y$ is public. Policies can be computed by ABPs or deterministic logspace TMs. Prior to our work, the only known construction of RFE for quadratic functions from standard assumptions [Zhu et al., Eurocrypt 2024] did not provide any access control. Conceptually, we transfer the framework of [Lin and Luo, Eurocrypt 2020], which combines linear FE with information-theoretic garbling schemes, from standard to registered FE. At the core of our constructions, we introduce a novel RFE for inner products with user-specific pre-constraining of the functions which enables the on-the-fly randomization of garbling schemes akin to standard inner-product FE. This solves an open question raised in [Zhu et al., Asiacrypt 2023] who constructed RABE from predicate encodings but left open the problem of building RABE in a more general setting from linear garbling schemes.

  匹配依据：MPC: garbling schemes

  </details>

- **PrivLLMSwarm: Privacy-Preserving LLM-Driven UAV Swarms for Secure IoT Surveillance**
  2025-12-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.06747)
  Jifar Wakuma Ayana, Huang Qiming

  <details><summary>摘要 / Abstract</summary>

  Large Language Models (LLMs) are emerging as powerful enablers for autonomous reasoning and natural-language coordination in unmanned aerial vehicle (UAV) swarms operating within Internet of Things (IoT) environments. However, existing LLM-driven UAV systems process sensitive operational data in plaintext, exposing them to privacy and security risks. This work introduces PrivLLMSwarm, a privacy-preserving framework that performs secure LLM inference for UAV swarm coordination through Secure Multi-Party Computation (MPC). The framework incorporates MPC-optimized transformer components with efficient approximations of nonlinear activations, enabling practical encrypted inference on resource-constrained aerial platforms. A fine-tuned GPT-based command generator, enhanced through reinforcement learning in simulation, provides reliable instructions while maintaining confidentiality. Experimental evaluation in urban-scale simulations demonstrates that PrivLLMSwarm achieves high semantic accuracy, low encrypted inference latency, and robust formation control under privacy constraints. Comparative analysis shows PrivLLMSwarm offers a superior privacy-utility balance compared to differential privacy, federated learning, and plaintext baselines. To support reproducibility, the full implementation including source code, MPC components, and a synthetic dataset is publicly available. PrivLLMSwarm establishes a practical foundation for secure, LLM-enabled UAV swarms in privacy-sensitive IoT applications including smart-city monitoring and emergency response.

  匹配依据：MPC: secure multi party computation

  </details>

- **Privacy-Preserving Fully Distributed Gaussian Process Regression**
  2025-12-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.05473)
  Yeongjun Jang, Kaoru Teranishi, Jihoon Suh, Takashi Tanaka

  <details><summary>摘要 / Abstract</summary>

  Although distributed Gaussian process regression (GPR) enables multiple agents to jointly learn a model of the target function, its collaborative nature poses a risk of private data leakage. To address this, we propose a privacy-preserving fully distributed GPR protocol based on secure multi-party computation, which hides each agent&#x27;s individual contribution from semi-honest coalitions of bounded size, beyond what is implied by the aggregated value. Building upon a secure distributed average consensus algorithm, it guarantees that each agent&#x27;s local model practically converges to the same global model obtained by the standard distributed GPR. Formal privacy guarantees are established within the simulation based security paradigm. The protocol is further extended to privacy-preserving optimization of kernel hyperparameters, which is critical yet often overlooked in the literature. Experimental results demonstrate the effectiveness and practical applicability of the proposed method.

  匹配依据：MPC: secure multi party computation

  </details>

- **Towards Privacy-Preserving Range Queries with Secure Learned Spatial Index over Encrypted Data**
  2025-12-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.03669)
  Zuan Wang, Juntao Lu, Jiazhuang Wu, Youliang Tian, Wei Song, Qiuxian Li, Duo Zhang

  <details><summary>摘要 / Abstract</summary>

  With the growing reliance on cloud services for large-scale data management, preserving the security and privacy of outsourced datasets has become increasingly critical. While encrypting data and queries can prevent direct content exposure, recent research reveals that adversaries can still infer sensitive information via access pattern and search path analysis. However, existing solutions that offer strong access pattern privacy often incur substantial performance overhead. In this paper, we propose a novel privacy-preserving range query scheme over encrypted datasets, offering strong security guarantees while maintaining high efficiency. To achieve this, we develop secure learned spatial index (SLS-INDEX), a secure learned index that integrates the Paillier cryptosystem with a hierarchical prediction architecture and noise-injected buckets, enabling data-aware query acceleration in the encrypted domain. To further obfuscate query execution paths, SLS-INDEXbased Range Queries (SLRQ) employs a permutation-based secure bucket prediction protocol. Additionally, we introduce a secure point extraction protocol that generates candidate results to reduce the overhead of secure computation. We provide formal security analysis under realistic leakage functions and implement a prototype to evaluate its practical performance. Extensive experiments on both real-world and synthetic datasets demonstrate that SLRQ significantly outperforms existing solutions in query efficiency while ensuring dataset, query, result, and access pattern privacy.

  匹配依据：MPC: secure computation

  </details>

- **Game-Theoretically Fair Distributed Coin Tossing With Private Preferences**
  2025-12-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2190)
  Pedro Branco, Pratik Soni, Sri AravindaKrishnan Thyagarajan, Ke Wu

  <details><summary>摘要 / Abstract</summary>

  Secure coin-tossing is typically modeled as an input-less functionality, where parties with no private inputs jointly generate a fair coin. In the dishonest majority setting, however, a strongly fair coin-tossing protocol is impossible. To circumvent this barrier, recent work has adopted the weaker notion of game-theoretic fairness, where adversaries are rational parties with preferences for specific outcomes, seeking to bias the coin in their favor. Yet these preferences may encode secret information, making prior protocols that assume preferences are public, fundamentally incompatible with privacy. We initiate a comprehensive study of privacy-preserving game-theoretically fair coin-tossing, where the preferences of honest parties remain private. We propose a simulation-based security framework and a new ideal functionality that reconciles both preference-privacy and game-theoretic fairness. A key ingredient is a certifying authority that authenticates each party’s preference and publishes only aggregate statistics, preventing misreporting while hiding parties&#x27; preferences. The functionality guarantees that every honest party receives an output: either a uniform coin; or, if an adversary deviates, a coin that strictly decreases the adversarial coalition&#x27;s expected utility. Within this framework, we construct a protocol realizing our ideal functionality under standard cryptographic assumptions that works for both binary and general $m$-sided coin-tossing. Our schemes tolerate the same optimal (or nearly optimal) corruption thresholds as the best known protocols with public preferences (Wu-Asharov-Shi, EUROCRYPT &#x27;22; Thyagarajan-Wu-Soni, CRYPTO &#x27;24). Technically, our protocols combine authenticated preferences with an anonymous communication layer that decouples identities from preference-dependent actions, together with a deviation-penalty mechanism that enforces game-theoretic fairness. Our work is the first to reconcile game-theoretic fairness with preference privacy, offering new definitional tools and efficient protocols for rational multi-party computation in dishonest majority settings.

  匹配依据：MPC: multi party computation

  </details>

- **ALIOTH: An Efficient and Secure Weight-of-Evidence Framework for Privacy-Preserving Data Processing**
  2025-12-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2188)
  Ye Dong, Xiangfu Song, W.j Lu, Xudong Chen, Yaxi Yang, Ruonan Chen, Tianwei Zhang, Jin-Song Dong

  <details><summary>摘要 / Abstract</summary>

  Secure two-party computation (2PC)-based privacy-preserving machine learning (ML) has made remarkable progress in recent years. However, most existing works overlook the privacy challenges that arise during the data preprocessing stage. Although some recent studies have introduced efficient techniques for privacy-preserving feature selection and data alignment on well-structured datasets, they still fail to address the privacy risks involved in transforming raw data features into ML-effective numerical representations. In this work, we present ALIOTH, an efficient 2PC framework that securely transforms raw categorical and numerical features into Weight-of-Evidence (WoE)-based numerical representations under both vertical and horizontal data partitions. By incorporating our proposed partition-aware 2PC protocols and vectorization optimizations, ALIOTH efficiently generates WoE-transformed datasets in secret. To demonstrate scalability, we conduct experiments on diverse datasets. Notably, ALIOTH can transform 3 million data samples with 100 features securely within half an hour over a wide-area network. Furthermore, ALIOTH can be seamlessly integrated with existing 2PC-based ML frameworks. Empirical evaluations on real-world financial datasets show ALIOTH improves both the predictive performance of logistic regression and 2PC training efficiency.

  匹配依据：MPC: secure two party computation

  </details>

- **On the Context-Hiding Property of Shamir-Based Homomorphic Secret Sharing**
  2025-12-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.01604)
  Shuai Feng, Liang Feng Zhang

  <details><summary>摘要 / Abstract</summary>

  Homomorphic secret sharing (HSS) allows multiple input clients to secretly share their private inputs to a function among several servers such that each server can homomorphically compute the function over its share to produce a share of the function&#x27;s output. In HSS-enabled applications such as secure multi-party computation (MPC), security requires that the output shares leak no more information about the inputs than the function output. Such security is ensured by the context-hiding property of HSS. The typical rerandomization technique achieves context hiding but increases the share size. To address this, we formalize the context-hiding property of HSS for individual functions, examine the context-hiding property of Shamir-based HSS for monomials, and extend the study to polynomials.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Quantum ramp secret sharing from Haar scrambling**
  2025-11-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2512.00970)
  Kiran Adhikari

  <details><summary>摘要 / Abstract</summary>

  Quantum information scrambling has emerged as a powerful tool for studying the dynamics of chaotic quantum many-body systems, assessing benchmarking protocols, and even investigating exotic black hole models. During quantum information scrambling, localized quantum information disperses across the entire system, hiding from the observers who can only access part of it. On the other side, we have a fundamental cryptographic primitive called secret-sharing schemes, where a dealer shares a quantum secret with a group of parties, such that any subset of parties above a specific threshold size can reconstruct it. In this paper, we demonstrate that two protocols, Haar scrambling, which serves as a baseline for other scrambling techniques, and quantum secret sharing, are indeed equivalent. The scheme one gets out of this is of a ramp secret-sharing nature rather than a threshold scheme. We expect this because of the inherent randomness present in Haar unitaries. Moreover, by varying the purity of the initial states, we demonstrate that it is possible to obtain all possible types of ramp secret-sharing schemes. Furthermore, utilizing complexity theoretic arguments, we argue that the protocol can be implemented efficiently, i.e., in polynomial time. Finally, we explore potential applications, ranging from security implications for distributed quantum networks to cryptography in the Noisy Intermediate-Scale Quantum (NISQ) era, and draw insights for fundamental physics, such as many-body physics and quantum black holes.

  匹配依据：MPC: secret sharing

  </details>

- **Optimal Threshold Traitor Tracing**
  2025-11-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2154)
  Sourav Das, Pratish Datta, Aditi Partap, Swagata Sasmal, Mark Zhandry

  <details><summary>摘要 / Abstract</summary>

  Threshold encryption distributes decryption capability across $n$ parties such that any $t$ of them can jointly decrypt a ciphertext, while smaller coalitions learn nothing. However, once $t$ or more parties collude, traditional threshold schemes provide no accountability: a coalition of $t$ or more parties can pool its keys into a pirate decoder that enables unrestricted decryption, all without any risk of being exposed. To address this, Boneh, Partap, and Rotem [CRYPTO &#x27;24] introduced threshold traitor tracing (TTT), which equips threshold encryption with traceability. Yet, all known TTT schemes either suffer from parameter sizes growing with at least $n^{1/3}$, or rely on indistinguishability obfuscation to achieve optimal parameters. In this paper, we present the first TTT schemes with optimal parameters, where public keys, secret keys, and ciphertexts are all bounded by ${\sf poly}(\lambda,\log n)$, built solely from standard cryptographic tools and assumptions. Our first construction relies on the decisional Bilinear Diffie–Hellman (DBDH) assumption in prime order bilinear groups. Our second scheme is a candidate construction based on the Learning with Errors (LWE) assumption, which relies on the existence of secret sharing schemes with certain properties. This construction is plausibly post-quantum secure, and supports ramp-thresholds where decryption requires a larger coalition than those tolerated by security. Both of our constructions provide traceability against coalitions of arbitrary sizes. To achieve these results, we introduce a new primitive, Attribute-Based Threshold Encryption (ABTE), which generalizes both threshold and attribute-based encryption. We then combine ABTE with Mixed Functional Encryption through a new compiler to obtain our TTT schemes. We believe ABTE is a powerful primitive that may have independent applications beyond optimal TTT.

  匹配依据：MPC: secret sharing

  </details>

- **Private Data Imputation**
  2025-11-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.20832)
  Abdelkarim Kati, Florian Kerschbaum, Marina Blanton

  <details><summary>摘要 / Abstract</summary>

  Data imputation is an important data preparation task where the data analyst replaces missing or erroneous values to increase the expected accuracy of downstream analyses. The accuracy improvement of data imputation extends to private data analyses across distributed databases. However, existing data imputation methods violate the privacy of the data rendering the privacy protection in the downstream analyses obsolete. We conclude that private data analysis requires private data imputation. In this paper, we present the first optimized protocols for private data imputation. We consider the case of horizontally and vertically split data sets. Our optimization aims to reduce most of the computation to private set intersection (or at least oblivious programmable pseudo-random function) protocols which can be very efficiently computed. We show that private data imputation has -- on average across all evaluated datasets -- an accuracy advantage of 20\% in case of vertically split data and 5\% in case of horizontally split data over imputing data locally. In case of the worst data split we observed that imputing using our method resulted in an increase of up to 32.7 times in the quality of imputation over the vertically split data and 3.4 times in case of horizontally split data. Our protocols are very efficient and run in 2.4 seconds in case of vertically split data and 8.4 seconds in case of horizontally split data for 100,000 records evaluated in the 10 Gbps network setting, performing one data imputation.

  匹配依据：MPC: private set intersection

  </details>

- **Zero-Knowledge Protocols with PVC Security: Striking the Balance between Security and Efficiency**
  2025-11-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2146)
  Yi Liu, Yipeng Song, Anjia Yang, Junzuo Lai

  <details><summary>摘要 / Abstract</summary>

  Zero-knowledge protocols allow a prover to prove possession of a witness for an NP-statement without revealing any information about the witness itself. This kind of protocol has found extensive applications in various fields, including secure computation and blockchain. However, in certain scenarios (e.g. when the statements are complicated), existing zero-knowledge protocols may not be well-suited due to their limited applicability or high computational overhead. We address these limitations by incorporating the notion of publicly verifiable covert (PVC) security into zero-knowledge protocols. PVC security, recently emerging from secure computation, effectively balances security and efficiency in practical scenarios. With PVC security, while a malicious party may attempt to cheat, such cheating will be detected and become publicly verifiable with a significant probability (called deterrence factor, e.g. ${&gt;}90\%$). This notion is well-suited for practical scenarios involving reputation-conscious parties (e.g. companies) and offers substantial efficiency improvements. In this paper, we present the first definition of zero-knowledge protocols with PVC security. We then propose a generic transformation to convert Sigma protocols with $1$-bit challenge, a kind of protocol widely used for zero-knowledge, into efficient zero-knowledge protocols with PVC security. By applying our transformation, we can substantially improve the efficiency of existing protocols for reputation-sensitive parties. For instance, applying the transformation to achieve a deterrence factor of $93.75\%$ incurs a cost of only around $20\%$ compared to the original protocol. Therefore, our results contribute to significant advancements in practical zero-knowledge protocols.

  匹配依据：MPC: secure computation

  </details>

- **Updatable Private Set Intersection and Beyond: Efficient Constructions via Circuit Private Set Intersection**
  2025-11-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2147)
  Ferran Alborch, Tom Chauvier, Antonio Faonio, Alexandre Fontaine, Ferhat Karakoç, Alptekin Küpçü, Camille Malek, Melek Önen

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection (PSI) has been widely studied, deployed, and demonstrated on static datasets. In this work, we investigate the problem of designing efficient and secure updatable PSIs in the honest-but-curious model by adopting the approach of executing a small number of PSIs over smaller sets instead of one PSI over the entire updated sets. We first identify that existing constructions suffer from privacy leakages and further propose to mitigate them thanks to the use of circuit PSIs, which are variants of PSI protocols that output the secret shares of the intersection instead of outputting the resulting intersection, combined with secure shuffling when needed. We construct a generic framework for PSI over updated sets and show that this framework can easily be extended to a protocol that outputs the cardinality of the intersection instead of the intersection itself.

  匹配依据：MPC: private set intersection

  </details>

- **CrypTorch: PyTorch-based Auto-tuning Compiler for Machine Learning with Multi-party Computation**
  2025-11-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.19711)
  Jinyu Liu, Gang Tan, Kiwan Maeng

  <details><summary>摘要 / Abstract</summary>

  MPC-based ML uses multi-party computation (MPC) to run machine learning (ML) workloads across multiple parties without each having to share their private data or model parameters. However, existing frameworks frequently degrade accuracy and performance due to a series of MPC-specific transformations that add errors and overheads. These transformations are mostly opaque to users, making it hard to find and/or optimize problematic transformations. We propose CrypTorch, a modular, extensible, and iteratively-testable compiler framework for MPC-based ML. CrypTorch splits MPC-specific transformations into modular compilation stages, allowing users to easily inspect and optimize them. CrypTorch emits an executable graph after each transformation, allowing iterative testing to pinpoint any problematic transformations. Building on these features, CrypTorch automatically chooses a set of transformations from a pool of choices to balance performance and accuracy during the operator approximation stage, which we identified as the biggest contributor to accuracy/performance degradation. CrypTorch&#x27;s auto-tuning alone provides 1.21-1.5x speedup without accuracy loss, and 1.33-1.74x speedup when some accuracy degradation is allowed. Combined with better engineering and adoption of state-of-the-art practices (made easier due to CrypTorch&#x27;s modular design), CrypTorch brings 3.74-8.32x end-to-end speedup compared to the popular CrypTen. CrypTorch is built as an extension to PyTorch 2&#x27;s compiler.

  匹配依据：MPC: multi party computation

  </details>

- **Computational Quantum Anamorphic Encryption and Quantum Anamorphic Secret-Sharing**
  2025-11-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.17924)
  Sayantan Ganguly, Shion Samadder Chaudhury

  <details><summary>摘要 / Abstract</summary>

  The concept of anamorphic encryption, first formally introduced by Persiano et al. in their influential 2022 paper titled ``Anamorphic Encryption: Private Communication Against a Dictator,&#x27;&#x27; enables embedding covert messages within ciphertexts. One of the key distinctions between a ciphertext embedding a covert message and an original ciphertext, compared to an anamorphic ciphertext, lies in the indistinguishability between the original ciphertext and the anamorphic ciphertext. This encryption procedure has been defined based on a public-key cryptosystem. Initially, we present a quantum analogue of the classical anamorphic encryption definition that is based on public-key encryption. Additionally, we introduce a definition of quantum anamorphic encryption that relies on symmetric key encryption. Furthermore, we provide a detailed generalized construction of quantum anamorphic symmetric key encryption within a general framework, which involves taking any two quantum density matrices of any different dimensions and constructing a single quantum density matrix, which is the quantum anamorphic ciphertext containing ciphertexts of both of them. Subsequently, we introduce a definition of computational anamorphic secret-sharing and extend the work of Çakan et al. on computational quantum secret-sharing to computational quantum anamorphic secret-sharing, specifically addressing scenarios with multiple messages, multiple keys, and a single share function. This proposed secret-sharing scheme demonstrates impeccable security measures against quantum adversaries.

  匹配依据：MPC: secret sharing

  </details>

- **Improved Robust Secret-Sharing for Honest-Majority Preprocessing-MPC**
  2025-11-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2135)
  Charanjit S. Jutla, Nathan Manohar, Arnab Roy

  <details><summary>摘要 / Abstract</summary>

  We design a novel robust secret-sharing scheme in the honest-majority setting for $n$ parties that allows constant communication per opening per party when amortized over $\Theta(n)$ simultaneous openings. We attain this scheme by a novel application of list decoding of folded Reed-Solomon codes. This was stated as an open problem by Escudero and Fehr (2023), who could obtain this amortized complexity only for $\Theta(n^2)$ simultaneous openings. Additionally, the dealing of such shares for a random value in a finite field $\mathbb{F}$ can itself be done using an honest-majority MPC protocol using only $O(n^2)$ multiplications between Shamir-shared values. This allows us to build an offline-online fully-secure (GOD) honest-majority MPC protocol, which has a fast online stage with amortized communication cost only $O(n)$ per multiplication gate (assuming the circuit has width $\Omega(n)$) and with no additional overhead, and an offline preprocessing stage with incremental communication cost only $O(n^3)$ per multiplication gate. This improves the previous best protocol in this setting by Escudero and Fehr (2023), which required the circuit to have width $\Omega(n^2)$. Further, the earlier scheme had an incremental preprocessing cost of $O(n^4)$ per multiplication gate. Due to requiring non-responsive rounds, the online stage of these protocols may still be concretely far less efficient than the online stage of the offline-online BGW protocol. Since the BGW protocol only provides security against fewer than $n/3$ malicious parties, we also devise a novel MPC protocol that boosts the BGW protocol&#x27;s correctness threshold to $n/2$, while maintaining privacy and robustness thresholds at $n/3$, and with minimal online overhead. This is useful in applications, such as elections and auctions, where certification of a correct result is paramount. To achieve this correctness against fewer than $n/2$ malicious parties and to keep the pre-processing cost low, we use our novel robust honest-majority secret-sharing scheme, but only once during a final SPDZ-style attestation.

  匹配依据：MPC: secret sharing

  </details>

- **Bandwidth Efficient Partial Authorized PSI**
  2025-11-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2132)
  Tjitske Ollie Koster, Francesca Falzon, Evangelia Anna Markatou

  <details><summary>摘要 / Abstract</summary>

  Recent attacks on private set intersection (PSI) and PSI-like protocols have demonstrated that input privacy can be compromised when parties maliciously choose their inputs, even in protocols proven secure against malicious adversaries. To counter such attacks, Authorized PSI (APSI) introduces a judge who authorizes the elements of the parties before the intersection is computed. Falzon and Markatou (PETS 2025) proposed Partial-APSI, a privacy-preserving variant of APSI that prevents revealing the entire set to a judge. Their Partial-APSI protocol requires significant bandwidth overhead due to the use of bilinear pairings and because the judge must sign each element in the input set. In this work, we present a bandwidth-efficient Partial-APSI protocol that outperforms Falzon and Markatou, both asymptotically and empirically. For example, for sets of size $2^{20}$, we require around $21\times$ less bandwidth and are about $6\times$ faster over a LAN network. In addition to our protocol, we model the real-world behavior of rational parties through a game-theoretic analysis. We introduce payout mechanisms for detected cheating and establish lower bounds on their values, ensuring that the best strategy for rational parties is to provide honest input.

  匹配依据：MPC: private set intersection

  </details>

- **Are ideal functionalities really ideal?**
  2025-11-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2125)
  Myrto Arapinis, Véronique Cortier, Hubert de Groote, Charlie Jacomme, Steve Kremer

  <details><summary>摘要 / Abstract</summary>

  Ideal functionalities are used to study increasingly complex protocols within the Universal Composability framework. However, such functionalities are often complex themselves, making it difficult to assess whether they truly fulfill their promises. In this paper, we present four attacks on functionalities from various applications (e-voting, SMPC, anonymous lotteries, and smart metering), demonstrating that they do not capture the intuitively expected properties. We argue that ideal functionalities should not merely be justified secure at a high level but rigorously proven to be so. To this end, we propose a methodology that combines game-based proofs and computer-aided verification: ideal functionalities can in fact be treated as protocols, and one can use traditional game-based proofs to study them, where any game-based security property proven on the functionality does transfer to any protocol that realizes it. We also propose fixed versions of the ideal functionalities we studied, and formally define the security properties they should satisfy through a game. Finally, using Squirrel, a proof assistant for protocol security, we formally prove that the fixed functionalities verify the specified game-based security properties.

  匹配依据：MPC: smpc (context)

  </details>

- **Privacy-Preserving IoT in Connected Aircraft Cabin**
  2025-11-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.15278)
  Nilesh Vyas, Benjamin Zhao, Aygün Baltaci, Gustavo de Carvalho Bertoli, Hassan Asghar, Markus Klügel, Gerrit Schramm, Martin Kubisch, Dali Kaafar

  <details><summary>摘要 / Abstract</summary>

  The proliferation of IoT devices in shared, multi-vendor environments like the modern aircraft cabin creates a fundamental conflict between the promise of data collaboration and the risks to passenger privacy, vendor intellectual property (IP), and regulatory compliance. While emerging standards like the Cabin Secure Media-Independent Messaging (CSMIM) protocol provide a secure communication backbone, they do not resolve data governance challenges at the application layer, leaving a privacy gap that impedes trust. This paper proposes and evaluates a framework that closes this gap by integrating a configurable layer of Privacy-Enhancing Technologies (PETs) atop a CSMIM-like architecture. We conduct a rigorous, empirical analysis of two pragmatic PETs: Differential Privacy (DP) for statistical sharing, and an additive secret sharing scheme (ASS) for data obfuscation. Using a high-fidelity testbed with resource-constrained hardware, we quantify the trade-offs between data privacy, utility, and computing performance. Our results demonstrate that the computational overhead of PETs is often negligible compared to inherent network and protocol latencies. We prove that architectural choices, such as on-device versus virtualized processing, have a far greater impact on end-to-end latency and computational performance than the PETs themselves. The findings provide a practical roadmap for system architects to select and configure appropriate PETs, enabling the design of trustworthy collaborative IoT ecosystems in avionics and other critical domains.

  匹配依据：MPC: secret sharing

  </details>

- **Oblivious Batch Updates for Bloom-Filter-based Outsourced Cryptographic Protocols**
  2025-11-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2116)
  Marten van Dijk, Dandan Yuan

  <details><summary>摘要 / Abstract</summary>

  In this work, we initiate the formal study of oblivious batch updates over outsourced encrypted Bloom filters, focusing on scenarios where a storage-limited sender must insert or delete batches of elements in a Bloom filter maintained on an untrusted server. Our survey identifies only two prior approaches (CCS 2008 and CCS 2012) that can be adapted to this problem. However, they either fail to provide adequate security in dynamic scenarios or incur prohibitive update costs that scale with the filter’s maximum capacity rather than the actual batch size. To address these limitations, we introduce a new cryptographic primitive, $\textit{Oblivious Bloom Filter Insertion}$ ($\textsf{OBFI}$), and propose novel constructions. At the core of our design is a novel building block, $\textit{Oblivious Bucket Distribution}$ ($\textsf{OBD}$), which enables a storage-limited sender to distribute a large array of elements, uniformly sampled from a finite domain, into small, fixed-size buckets in a data-oblivious manner determined by element order. The design of $\textsf{OBD}$ is further supported by identifying and proving a new structural property of such arrays, which establishes tight and explicit probabilistic bounds on the number of elements falling within predefined subranges of the domain. Our $\textsf{OBFI}$ constructions achieve adaptive data-obliviousness and ensure that batch update costs scale primarily with the batch size. Depending on the variant, the sender’s storage requirement ranges from $O(\lambda)$, where $\lambda$ is the security parameter, down to $O(1)$. Finally, we demonstrate the practicality of $\textsf{OBFI}$ by integrating it into representative Bloom-filter-based cryptographic protocols for Searchable Symmetric Encryption, Public-key Encryption with Keyword Search, and Outsourced Private Set Intersection, thereby obtaining batch-updatable counterparts with state-of-the-art security and performance.

  匹配依据：MPC: private set intersection

  </details>

- **SoK: Secure Computation over Secret Shares**
  2025-11-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2111)
  Tamir Tassa, Arthur Zamarin

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) enables mutually distrustful parties to jointly compute functions over private data without revealing their inputs. A central paradigm in MPC is the secret-sharing-based model, where secret sharing underpins the efficient realization of arithmetic, comparison, numerical, and Boolean operations on shares of private inputs. In this paper, we systematize protocols for these operations, with particular attention to two foundational contributions \cite{ChidaGHIKLN18,NO07} that devised secure multiplication and comparison. Our survey provides a unified, self-contained exposition that highlights the composability, performance trade-offs, and implementation choices of these protocols. We further demonstrate how they support practical privacy-preserving systems, including recommender systems, distributed optimization platforms, and e-voting infrastructures. By clarifying the protocol landscape and connecting it to deployed and emerging applications, we identify concrete avenues for improving efficiency, scalability, and integration into real-world MPC frameworks. Our goal is to bridge theory and practice, equipping both researchers and practitioners with a deeper understanding of secret-sharing-based MPC as a foundation for privacy technologies.

  匹配依据：MPC: secret sharing, secure computation, secure multiparty computation

  </details>

- **Secure Lookup Tables: Faster, Leaner, and More General**
  2025-11-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2109)
  Chongrong Li, Pengfei Zhu, Yun Li, Zhanpeng Guo, Jingyu Li, Yuncong Hu, Zhicong Huang, Cheng Hong

  <details><summary>摘要 / Abstract</summary>

  Secure lookup table (LUT) protocols allow retrieving values from a table at secret indices, and have become a promising approach for the secure evaluation of non-linear functions. Most existing LUT protocols target the two-party setting, where the best protocols achieve a communication cost of $O(N)$ for a table of size $N$. MAESTRO (Morita et al., USENIX Security 2025) represents the state-of-the-art LUT protocol for AES in the three-party honest-majority setting, with a communication cost of $O(N^{1/2})$; malicious security is achieved with distributed zero-knowledge proofs. However, it only supports single-input tables over characteristic-2 fields $\mathbb{F}_{2^k}$ and lacks support for multi-input tables over rings $\mathbb{Z}_{2^k}$, which are more widely used in modern computation. Moreover, the $O(N^{1/2})$ cost remains expensive for large-scale applications; their efficient distributed zero-knowledge proofs are specialized for AES and cannot be easily applied to $\mathbb{Z}_{2^k}$. In this work, we present MARLUT, a new generalized and optimized LUT construction supporting multi-input tables over both rings $\mathbb{Z}_{2^k}$ and fields $\mathbb{F}_{2^k}$ with malicious security. We achieve this by (1) extending the semi-honest LUT protocol from MAESTRO, utilizing high-dimensional tensors to reduce its communication cost to $O(N^{1/3})$, and (2) designing a new distributed zero-knowledge proof for inner-product relations over $\mathbb{Z}_{2^k}$. Our distributed zero-knowledge proof is more efficient than the state-of-the-art work (Li et al., CCS 2024) and may be of independent interest. Experiments show that on a table of size $2^{16}$, our semi-honest LUT protocol reduces the offline computational and communication cost by a factor of $5.95$ and $3.23$, respectively. Our distributed zero-knowledge proofs show up to $7.07\times$ and $4.97\times$ speedups over the state-of-the-art protocol on ring $\mathbb{Z}_{2^8}$ and $\mathbb{Z}_{2^{16}}$, respectively.

  匹配依据：MPC: secure evaluation

  </details>

- **An Improved Quantum Anonymous Notification Protocol for Quantum-Augmented Networks**
  2025-11-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.12313)
  Nitin Jha, Abhishek Parakh, Mahadevan Subramaniam

  <details><summary>摘要 / Abstract</summary>

  The scalability of current quantum networks is limited due to noisy quantum components and high implementation costs, thereby limiting the security advantages that quantum networks provide over their classical counterparts. Quantum Augmented Networks (QuANets) address this by integrating quantum components in classical network infrastructure to improve robustness and end-to-end security. To enable such integration, Quantum Anonymous Notification (QAN) is a method to anonymously inform a receiver of an incoming quantum communication. Therefore, several quantum primitives will serve as core tools, namely, quantum voting, quantum anonymous protocols, quantum secret sharing, etc. However, all current quantum protocols can be compromised in the presence of several common channel noises. In this work, we propose an improved quantum anonymous notification (QAN) protocol that utilizes rotation operations on shared GHZ states to produce an anonymous notification in an n-user quantum-augmented network. We study the behavior of this modified QAN protocol under the dephasing noise model and observe stronger resilience to false notifications than earlier QAN approaches. The QAN framework is also proposed to be integrated with a machine-learning classifier, an enhanced quantum-augmented network. Finally, we discuss how this notification layer integrates with QuANets so that receivers can allow switch-bypass handling of quantum payloads, reducing header-based information leakage and vulnerability to targeted interference at compromised switches.

  匹配依据：MPC: secret sharing

  </details>

- **Optimal and Efficient Partite Decompositions of Hypergraphs**
  2025-11-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.11855)
  Andrew Krapivin, Benjamin Przybocki, Nicolás Sanhueza-Matamala, Bernardo Subercaseaux

  <details><summary>摘要 / Abstract</summary>

  We study the problem of partitioning the edges of a $d$-uniform hypergraph $H$ into a family $F$ of complete $d$-partite hypergraphs ($d$-cliques). We show that there is a partition $F$ in which every vertex $v \in V(H)$ belongs to at most $(\frac{1}{d!} + o_d(1))n^{d-1}/\lg n$ members of $F$. This settles the central question of a line of research initiated by Erdős and Pyber (1997) for graphs, and more recently by Csirmaz, Ligeti, and Tardos (2014) for hypergraphs. The $d=2$ case of this theorem answers a 40-year-old question of Chung, Erdős, and Spencer (1983). An immediate corollary of our result is an improved upper bound for the maximum share size for binary secret sharing schemes on uniform hypergraphs. Building on results of Nechiporuk (1969), we prove that every graph with fixed edge density $γ\in (0,1)$ has a biclique partition of total weight at most $(\tfrac{1}{2}+o(1))\cdot h_2(γ) \frac{n^2}{\lg n}$, where $h_2$ is the binary entropy function. Our construction implies that such biclique partitions can be constructed in time $O(m)$, which answers a question of Feder and Motwani (1995) and also improves upon results of Mubayi and Turán (2010) as well as Chavan, Rabinia, Grosu, and Brocanelli (2025). Using similar techniques, we also give an $n^{1+o(1)}$ algorithm for finding a subgraph $K_{t,t}$ with $t = (1-o(1)) \fracγ{h_2(γ)} \lg n$. Our results show that biclique partitions are information-theoretically optimal representations for graphs at every fixed density. We show that with this succinct representation one can answer independent set queries and cut queries in time $O(n^2/ \lg n)$, and if we increase the space usage by a constant factor, we can compute a $2α$-approximation for the densest subgraph problem in time $O(n^2/\lg α)$ for any $α&gt; 1$.

  匹配依据：MPC: secret sharing

  </details>

- **UP TO 50% OFF: Efficient Implementation of Polynomial Masking**
  2025-11-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2088)
  Jorge Andresen, Paula Arnold, Sebastian Berndt, Thomas Eisenbarth, Sebastian Faust, Marc Gourjon, Eric Landthaler, Elena Micheli, Maximilian Orlt, Pajam Pauls, Kathrin Wirschem, Liang Zhao

  <details><summary>摘要 / Abstract</summary>

  While passive probing attacks and active fault attacks have been studied for multiple decades, research has only started to consider combined attacks that use both probes and faults relatively recently. During this period, polynomial masking became a promising, provably secure countermeasure to protect cryptographic computations against such combined attacks. Unlike other countermeasures, such as duplicated additive masking, polynomial masking can be implemented using a linear number of shares, as shown by Berndt et al. at CRYPTO &#x27;23. Based upon this fact, Arnold et al. noted at CHES &#x27;24 that polynomial masking is particularly well-suited for parallel computation. This characteristic is especially effective in scenarios involving multiple circuits with identical structures, such as the 16 SBoxes in AES. Just recently, Faust et al. showed at CHES &#x27;25 that one can also incorporate the technique of packed secret sharing into these masking schemes, given that the state-of-the-art polynomial masking scheme is secure against combined attacks. In this work, we present provably secure advancements regarding this state-of-the-art scheme in both computational and randomness efficiency, reducing the randomness complexity by up to 50% and the computational complexity even more by going from a quadratic term to a linear one for many parameters. Moreover, we present the first implementation of a polynomial masking scheme against combined attacks along with an extensive experimental evaluation for a wide range of parameters and configurations as well as a statistical leakage detection to evaluate the security of the implementation on an Arm Cortex-M processor. Our implementation is publicly available to encourage further research in practical combined resilience.

  匹配依据：MPC: secret sharing

  </details>

- **Traceable Bottom-Up Secret Sharing and Law &amp; Order on Community Social Key Recovery (Full Version)**
  2025-11-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2089)
  Rittwik Hajra, Subha Kar, Pratyay Mukherjee, Soumit Pal

  <details><summary>摘要 / Abstract</summary>

  A recent work by Kate et al. [EPRINT 2025] proposes a community-based social recovery scheme (SKR), where key-owners can use a subset of other community members as guardians, and in exchange, they play guardians to support other participants&#x27; key recovery. Their construction relies on a new concept called bottom-up secret sharing (BUSS). However, they do not consider a crucial feature, called traceability, which ensures that if more than a threshold number of the guardians collude, at least some colluders&#x27; identities can be traced -- thereby deterring participants from colluding. In this paper, we incorporate traceability into the community social key recovery as an important feature. We first introduce the notion of traceable BUSS, which allows tracing colluders by accessing a reconstruction box. Then, extending the work of Boneh et al. [CRYPTO 2024], we propose the first traceable BUSS construction. Finally, we show how to generically use a traceable BUSS scheme to construct a traceable SKR in the aforementioned community setting. Overall, this is the first scheme combining decentralized key management with traceability, marrying BUSS’s scalability with the deterrence of traceable secret sharing.

  匹配依据：MPC: secret sharing

  </details>

- **Leakage-Free Enhanced Private Set Union for Balanced and Unbalanced Scenarios**
  2025-11-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2087)
  Qiang Liu, JaeYoung Bae, JoonWoo Lee

  <details><summary>摘要 / Abstract</summary>

  Private Set Union (PSU) enables two parties to compute the union of their input sets without revealing anything else. Depending on set sizes, PSU is studied in balanced and unbalanced settings. Tu et al. (USENIX Security 2025) presented state-of-the-art enhanced PSU (ePSU) protocols under a unified framework in both settings, achieving enhanced security by preventing during-execution leakage. However, we observe that directly applying hash-to-bin on input sets within their framework introduces potential privacy risks. Moreover, the communication of their unbalanced ePSU still scales with the larger set size, rather than being linear in only the smaller set size. In this work, we address these open problems. We employ a combination of oblivious pseudorandom function (OPRF) and shuffling to mitigate the potential privacy leakage that arises when directly applying the hash-to-bin within the framework of Tu et al. (USENIX Security 2025). Building upon this, we further optimize their balanced ePSU protocol by leveraging a bidirectional oblivious key-value store (OKVS). Compared with the corrected version of Tu et al.&#x27;s balanced ePSU, ours achieves a $1.1-3.0\times$ shrinking in communication and a $1.2-1.6\times$ speedup in runtime. We design the first unbalanced ePSU whose communication is linear solely in the smaller set size. Since no hash-to-bin is used, it is inherently free from the associated privacy leakage. With the smaller set size fixed at $2^{10}$, ours reduces communication by $1.5-45.8\times$ compared with corrected version of Tu et al.&#x27;s unbalanced ePSU, while achieving $1.3-6.7\times$ runtime speedups.

  匹配依据：MPC: private set union

  </details>

- **Reliable and Private Utility Signaling for Data Markets**
  2025-11-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.07975)
  Li Peng, Jiayao Zhang, Yihang Wu, Weiran Liu, Jinfei Liu, Zheng Yan, Kui Ren, Lei Zhang, Lin Qu

  <details><summary>摘要 / Abstract</summary>

  The explosive growth of data has highlighted its critical role in driving economic growth through data marketplaces, which enable extensive data sharing and access to high-quality datasets. To support effective trading, signaling mechanisms provide participants with information about data products before transactions, enabling informed decisions and facilitating trading. However, due to the inherent free-duplication nature of data, commonly practiced signaling methods face a dilemma between privacy and reliability, undermining the effectiveness of signals in guiding decision-making. To address this, this paper explores the benefits and develops a non-TCP-based construction for a desirable signaling mechanism that simultaneously ensures privacy and reliability. We begin by formally defining the desirable utility signaling mechanism and proving its ability to prevent suboptimal decisions for both participants and facilitate informed data trading. To design a protocol to realize its functionality, we propose leveraging maliciously secure multi-party computation (MPC) to ensure the privacy and robustness of signal computation and introduce an MPC-based hash verification scheme to ensure input reliability. In multi-seller scenarios requiring fair data valuation, we further explore the design and optimization of the MPC-based KNN-Shapley method with improved efficiency. Rigorous experiments demonstrate the efficiency and practicality of our approach.

  匹配依据：MPC: secure multi party computation

  </details>

- **Postponing the Glitches is Not Enough - A Critical Analysis of the DATE 2024 E-ISW Masking Scheme**
  2025-11-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2084)
  Amir Moradi

  <details><summary>摘要 / Abstract</summary>

  The Enhanced ISW (E-ISW) masking scheme, recently proposed at DATE 2024, was introduced as a refinement to the classical ISW construction to restore provable security guarantees in hardware implementations affected by glitches. By enforcing input-complete gate evaluations through the use of artificial delays, E-ISW seeks to mitigate the glitch-induced leakage that compromises standard masking techniques. However, in this work, we demonstrate that this modification is fundamentally insufficient to ensure robust side-channel resistance in realistic hardware environments. We conduct a detailed analysis and present concrete examples where E-ISW fails to prevent information leakage, even when the prescribed countermeasures are correctly applied. These vulnerabilities arise due to deeper conceptual shortcomings in the design, particularly the absence of compositional reasoning about the interaction between glitches and masking. Our results show that the security claims of E-ISW do not hold in practice, and they expose critical limitations in relying on heuristic delay-based fixes without formal and compositional proofs of security. This study serves as a cautionary note for the cryptographic engineering community, emphasizing the necessity of rigorous validation when proposing enhancements to established secure computation techniques.

  匹配依据：MPC: secure computation

  </details>

- **Non-Interactive Blind Signatures from RSA Assumption and More**
  2025-11-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2076)
  Lucjan Hanzlik, Eugenio Paracucchi, Riccardo Zanotto

  <details><summary>摘要 / Abstract</summary>

  Blind signatures have received increased attention from researchers and practitioners. They allow users to obtain a signature under a message without revealing it to the signer. One of the most popular applications of blind signatures is to use them as one-time tokens, where the issuing is not linkable to the redeeming phase, and the signature under a random identifier forms a valid token. This concept is the backbone of the Privacy Pass system, which uses it to identify honest but anonymous users and protect content delivery networks from botnets. Non-interactive blind signatures for random messages were introduced by Hanzlik (Eurocrypt&#x27;23). They allow a signer to create a pre-signature with respect to a particular public key, while the corresponding secret key can later be used to finalize the signature. This non-interaction allows for more applications than in the case of blind signatures. In particular, the author suggested using regular PKI keys as the recipient public key, allowing for a distribution of one-time tokens to users outside the system, e.g., to public keys of GitHub users, similar to airdropping of cryptocurrencies. Unfortunately, despite introducing this concept, the paper fails to provide schemes that work with keys used in the wild. We solve this open problem. We introduce a generic construction of non-interactive blind signatures that relies on Yao&#x27;s garbled circuit techniques and provide particular improvements to this generic setting. We replace oblivious transfer with their non-interactive variant and show how to construct them so that the recipient&#x27;s public key, encoding the $\mathsf{OT}$ choice, is a standard RSA public key $(e,N)$. To improve the efficiency of the garbling, we show how to garble the signing algorithm of the pairing-based Pointcheval-Sanders (PS) signatures and the RSA-based signature scheme with efficient protocols by Camenisch and Lysyanskaya. Our technique also apply to the well-known BBS signatures. All our improvements are of independent interest and are central to our contribution.

  匹配依据：MPC: garbled circuit, oblivious transfer

  </details>

- **FedRW: Efficient Privacy-Preserving Data Reweighting for Enhancing Federated Learning of Language Models**
  2025-11-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.07505)
  Pukang Ye, Junwei Luo, Xiaolei Dong, Yunbo Yang

  <details><summary>摘要 / Abstract</summary>

  Data duplication within large-scale corpora often impedes large language models&#x27; (LLMs) performance and privacy. In privacy-concerned federated learning scenarios, conventional deduplication methods typically rely on trusted third parties to perform uniform deletion, risking loss of informative samples while introducing privacy vulnerabilities. To address these gaps, we propose Federated ReWeighting (FedRW), the first privacy-preserving framework, to the best of our knowledge, that performs soft deduplication via sample reweighting instead of deletion in federated LLM training, without assuming a trusted third party. At its core, FedRW proposes a secure, frequency-aware reweighting protocol through secure multi-party computation, coupled with a parallel orchestration strategy to ensure efficiency and scalability. During training, FedRW utilizes an adaptive reweighting mechanism with global sample frequencies to adjust individual loss contributions, effectively improving generalization and robustness. Empirical results demonstrate that FedRW outperforms the state-of-the-art method by achieving up to 28.78x speedup in preprocessing and approximately 11.42% improvement in perplexity, while offering enhanced security guarantees. FedRW thus establishes a new paradigm for managing duplication in federated LLM training.

  匹配依据：MPC: secure multi party computation

  </details>

- **Feasibility of Broadcast with Dynamic Committees**
  2025-11-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2078)
  Gabriel Dettling, Chen-Da Liu-Zhang, Elisaweta Masserova, Matthieu Rambaud, Antoine Urban

  <details><summary>摘要 / Abstract</summary>

  A significant number of works have considered the problem of multi-party computation over dynamic committees in synchronous networks, including YOSO MPC [Crypto&#x27;21], Fluid MPC [Crypto&#x27;21], SCALES MPC [TCC&#x27;22] and Layered MPC [Crypto&#x27;23]. However, prior works assume that every party has access to an ideal synchronous broadcast channel towards the next committee. While this assumption is partly justified due to the seminal work of Garay [WDAG&#x27;94] stating that deterministic broadcast with dynamic committees is impossible, it is open whether there are randomized solutions. We answer this question in the affirmative, by providing a complete characterization of broadcast with dynamic committees. We use the formalization introduced in the Layered MPC setting and achieve the following results for layered broadcast: - A statistically secure protocol tolerating $t&lt;n/3$ corruptions with no setup. - A computationally secure protocol tolerating $t&lt;n/2$ corruptions, assuming only a bulletin-board PKI for signatures. - A matching impossibility result showing that broadcast is impossible for $t \geq n/2$ corruptions. Using our broadcast, we achieve the following polynomial-time results: - YOSO MPC protocols without broadcast (statistical for $t&lt;n/3$ without setup; and computational for $t&lt;n/2$ assuming a plain PKI for signatures). - Assuming plain PKIs for signatures and public-key encryption, a Layered MPC protocol without broadcast for $t&lt;n/2$. - Assuming homomorphic commitments, a Layered MPC without broadcast for $(t+1)^2 \le n$. To achieve this, we introduce a secure-message-transmission protocol for $(t+1)^2 \le n$ which has linear communication in $\ell$ and polynomial communication in $n$ when transmitting a message across $\ell$ layers. This result is of independent interest.

  匹配依据：MPC: multi party computation

  </details>

- **Distributed Key Generation for Efficient Threshold-CKKS**
  2025-11-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2057)
  Seonhong Min, Guillaume Hanrot, Jai Hyun Park, Alain Passelègue, Damien Stehlé

  <details><summary>摘要 / Abstract</summary>

  Threshold fully homomorphic encryption provides efficient multi-party computation with low round-complexity. Among fully homomorphic encryption schemes, CKKS (Cheon-Kim-Kim-Song) enables high-throughput computations on both approximate and exact data. As most interesting applications involve deep computations, they require bootstrapping, the most efficient variants of which rely on sparse ternary secret keys. Unfortunately, so far, key generation protocols for threshold-CKKS either assume a trusted dealer, or lead to dense and non-ternary secret keys that severely damage computational throughput. In the latter case, the impact is so large that one often considers off-loading bootstrapping to an interactive protocol [Mouchet et al., PETS&#x27;21]. We introduce a novel Distributed Key Generation (DKG) protocol for threshold-CKKS. At a high level, it consists in running the existing distributed key generation algorithm from Mouchet et al. resulting in large secret keys, and using it to homomorphically evaluate the sparse-secret key generation algorithm. At the end, the parties obtain additive shares of a sparse secret key. The main technical challenge is to obtain an algorithm for sampling sparse ternary vectors of prescribed Hamming weight that can be CKKS-evaluated in an efficient manner. In the process, we design a new sampler of one-hot vectors that outperforms the one from [Boneh et al., AFT&#x27;20]. We also design a rejection-sampling algorithm to map several one-hot vectors into a vector of prescribed Hamming weight. The whole process can be performed with only two CKKS bootstraps, even for a significant number of users. We present several variants of the DKG protocol, with~2 to~4 communication rounds, as well as an extension to key generation delegation. We implemented the 4-round protocol; its computational components run in 2s on GPU (RTX4090) for up to 1024 parties.

  匹配依据：MPC: multi party computation

  </details>

- **Confidentiality in a Card-Based Protocol Under Repeated Biased Shuffles**
  2025-11-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.05111)
  Do Hyun Kim, Ahmet Cetinkaya

  <details><summary>摘要 / Abstract</summary>

  In this paper, we provide a probabilistic analysis of the confidentiality in a card-based protocol. We focus on Bert den Boer&#x27;s original Five Card Trick to develop our approach. Five Card Trick was formulated as a secure two-party computation method, where two players use colored cards with identical backs to calculate the logical AND operation on the bits that they choose. In this method, the players first arrange the cards privately, and then shuffle them through a random cut. Finally, they reveal the shuffled arrangement to determine the result of the operation. An unbiased random cut is essential to prevent players from exposing their chosen bits to each other. However, players typically choose to move cards within the deck even though not moving any cards should be equally likely. This unconscious behavior results in a biased, nonuniform shuffling-distribution in the sense that some arrangements of cards are slightly more probable after the cut. Such a nonuniform distribution creates an opportunity for a malicious player to gain advantage in guessing the other player&#x27;s choice. We provide the conditional probabilities of such guesses as a way to quantify the information leakage. Furthermore, we utilize the eigenstructure of a Markov chain to derive tight bounds on the number of times the biased random cuts must be repeated to reduce the leakage to an acceptable level. We also discuss the generalization of our approach to the setting where shuffling is conducted by a malicious player.

  匹配依据：MPC: secure two party computation

  </details>

- **Tight Analysis of a One-Shot Quantum Secret Sharing Scheme**
  2025-11-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.04399)
  Santanu Majhi, Debajyoti Bera

  <details><summary>摘要 / Abstract</summary>

  Quantum communication protocols can be designed to detect eavesdropping attacks, something that classical technologies are unable to do since classical information can be replicated in a non-destructive manner. Eavesdropping detection is, therefore, a standard feature in all the proposed quantum secret sharing (QSS) protocols. However, detection is often done by a statistical analysis of the outcome of multiple decoy rounds, and this causes a significant communication overhead. In our quest for a QSS protocol that works even in one round, we came across a one-shot secret-sharing framework proposed by Hsu (Phys. Rev. A 2003). The scheme was designed to work over public channels without requiring multiple rounds to detect eavesdropping but it lacked a thorough security analysis. In this work we present a complete characterisation of the correctness and security properties of this framework. Our characterisation allowed us to improve the original protocol to be more resistant towards eavesdropping. However, we prove a couple of impossibility results, including one that dictates that complete security against an eavesdropper is not possible in this framework. Thus, it is not possible to design a perfect QSS using this framework.

  匹配依据：MPC: secret sharing

  </details>

- **Multi-Twisted Generalized Reed-Solomon Codes: Structure, Properties, and Constructions**
  2025-11-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.03398)
  Zhonghao Liang, Chenlu Jia, Dongmei Huang, Qunying Liao, Chunming Tang

  <details><summary>摘要 / Abstract</summary>

  Maximum distance separable (in short, MDS), near MDS (in short, NMDS), and self-orthogonal codes play a pivotal role in algebraic coding theory, particularly in applications such as quantum communications and secret sharing scheme. Recently, the construction of non-generalized Reed-Solomon (in short, non-GRS) codes has emerged as a significant research frontier. This paper presents a systematic investigation into a generalized class of $(\mathcal{L}, \mathcal{P})$-twisted generalized Reed-Solomon (TGRS) codes characterized by $\ell$ twists, extending the structures previously introduced by Beelen et al. and Hu et al.. We first derive the explicit parity-check matrices for these codes by analyzing the properties of symmetric polynomials. Based on this algebraic framework, we establish necessary and sufficient conditions for the self-orthogonality of the proposed codes, generalizing several recent results. Leveraging these self-orthogonal structures, we construct new families of LCD MDS codes that offer greater flexibility in code length compared to existing literature. Furthermore, we provide a characterization of the NMDS property for these codes, offering a partial solution to the open problem concerning general $(\mathcal{L}, \mathcal{P})$-TGRS codes posed by Hu et al. (2025). Finally, we rigorously prove that these codes are of non-GRS type when $2k &gt; n$, providing an improvement over previous bounds. Theoretical constructions are validated through numerical examples.

  匹配依据：MPC: secret sharing

  </details>

- **PrivGNN: High-Performance Secure Inference for Cryptographic Graph Neural Networks**
  2025-11-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.02185)
  Fuyi Wang, Zekai Chen, Mingyuan Fan, Jianying Zhou, Lei Pan, Leo Yu Zhang

  <details><summary>摘要 / Abstract</summary>

  Graph neural networks (GNNs) are powerful tools for analyzing and learning from graph-structured (GS) data, facilitating a wide range of services. Deploying such services in privacy-critical cloud environments necessitates the development of secure inference (SI) protocols that safeguard sensitive GS data. However, existing SI solutions largely focus on convolutional models for image and text data, leaving the challenge of securing GNNs and GS data relatively underexplored. In this work, we design, implement, and evaluate $\sysname$, a lightweight cryptographic scheme for graph-centric inference in the cloud. By hybridizing additive and function secret sharings within secure two-party computation (2PC), $\sysname$ is carefully designed based on a series of novel 2PC interactive protocols that achieve $1.5\times \sim 1.7\times$ speedups for linear layers and $2\times \sim 15\times$ for non-linear layers over state-of-the-art (SotA) solutions. A thorough theoretical analysis is provided to prove $\sysname$&#x27;s correctness, security, and lightweight nature. Extensive experiments across four datasets demonstrate $\sysname$&#x27;s superior efficiency with $1.3\times \sim 4.7\times$ faster secure predictions while maintaining accuracy comparable to plaintext graph property inference.

  匹配依据：MPC: secure two party computation

  </details>

- **FLAME: Flexible and Lightweight Biometric Authentication Scheme in Malicious Environments**
  2025-11-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.02176)
  Fuyi Wang, Fangyuan Sun, Mingyuan Fan, Jianying Zhou, Jin Ma, Chao Chen, Jiangang Shu, Leo Yu Zhang

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving biometric authentication (PPBA) enables client authentication without revealing sensitive biometric data, addressing privacy and security concerns. Many studies have proposed efficient cryptographic solutions to this problem based on secure multi-party computation, typically assuming a semi-honest adversary model, where all parties follow the protocol but may try to learn additional information. However, this assumption often falls short in real-world scenarios, where adversaries may behave maliciously and actively deviate from the protocol. In this paper, we propose, implement, and evaluate $\sysname$, a \underline{F}lexible and \underline{L}ightweight biometric \underline{A}uthentication scheme designed for a \underline{M}alicious \underline{E}nvironment. By hybridizing lightweight secret-sharing-family primitives within two-party computation, $\sysname$ carefully designs a line of supporting protocols that incorporate integrity checks with rationally extra overhead. Additionally, $\sysname$ enables server-side authentication with various similarity metrics through a cross-metric-compatible design, enhancing flexibility and robustness without requiring any changes to the server-side process. A rigorous theoretical analysis validates the correctness, security, and efficiency of $\sysname$. Extensive experiments highlight $\sysname$&#x27;s superior efficiency, with a communication reduction by {$97.61\times \sim 110.13\times$} and a speedup of {$ 2.72\times \sim 2.82\times$ (resp. $ 6.58\times \sim 8.51\times$)} in a LAN (resp. WAN) environment, when compared to the state-of-the-art work.

  匹配依据：MPC: secret sharing, secure multi party computation, two party computation

  </details>

- **Several classes of three-weight or four-weight linear codes**
  2025-11-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2511.01309)
  Qunying Liao, Zhaohui Zhang, Peipei Zheng

  <details><summary>摘要 / Abstract</summary>

  In this manuscript, we construct a class of projective three-weight linear codes and two classes of projective four-weight linear codes over F2 from the defining sets construction, and determine their weight distributions by using additive characters. Especially, the projective three-weight linear code and one class of projective four-weight linear codes (Theorem 4.1) can be applied in secret sharing schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Quantum Secret Sharing Scheme on Hypercyclic Quantum Structures**
  2025-10-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.27466)
  Lei Li, Zhi Li

  <details><summary>摘要 / Abstract</summary>

  This paper investigates the construction of efficient quantum secret sharing schemes for quantum access structures based on hypergraphs with three hyperedges. We prove that hypercycles with three hyperedges are quantum access structures if and only if they can be classified into 12 non-isomorphic types under hypergraph isomorphism, and these hypercyclic quantum access structures encompass all four hyperstars with three hyperedges.In prior work, efficient and perfect quantum secret sharing schemes were constructed for hyperstar access structures with three hyperedges using single photons in d -dimensional quantum systems. These schemes correspond to classical perfect secret sharing schemes with optimal information rates. However, for hypercyclic access structures with three hyperedges, the method described above fails to yield classical perfect secret sharing schemes with optimal information rates. In this work, we explicitly construct classical perfect secret sharing schemes with optimal information rates for these access structures by combining Simmons&#x27; geometric method with Shamir&#x27;s threshold scheme. Subsequently, we employ single photons in d-dimensional quantum systems to build perfect QSS schemes upon these classical constructions.We introduce the concept of idealized information rate for minimal access structures in perfect QSS schemes. By extending the notion of efficiency proposed by Cabello [Phys. Rev. Lett., vol. 85, no. 26, p. 5635, 2000] for quantum key distribution protocols to QSS, we define the efficiency of minimally authorized subsets. Furthermore, we establish the relationship between the efficiency of minimally authorized subsets and the idealized information rate of minimal access structures. Finally, we rigorously prove that the QSS schemes constructed in this work achieve the highest efficiency among existing solutions.

  匹配依据：MPC: secret sharing

  </details>

- **Select-Then-Compute: Encrypted Label Selection and Analytics over Distributed Datasets using FHE**
  2025-10-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2023)
  Nirajan Koirala, Seunghun Paik, Sam Martin, Helena Berens, Tasha Januszewicz, Jonathan Takeshita, Jae Hong Seo, Taeho Jung

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection (PSI) protocols allow a querier to determine whether an item exists in a dataset without revealing the query or exposing non-matching records. It has many applications in fraud detection, compliance monitoring, healthcare analytics, and secure collaboration across distributed data sources. In these cases, the results obtained through PSI can be sensitive and even require some kind of downstream computation on the associated data before the outcome is revealed to the querier, computation that may involve floating-point arithmetic, such as the inference of a machine learning model. Although many such protocols have been proposed, and some of them even enable secure queries over distributed encrypted sets, they fail to address the aforementioned real-world complexities. In this work, we present the first encrypted label selection and analytics protocol construction, which allows the querier to securely retrieve not just the results of intersections among identifiers but also the outcomes of downstream functions on the data/label associated with the intersected identifiers. To achieve this, we construct a novel protocol based on an approximate CKKS fully homomorphic encryption that supports efficient label retrieval and downstream computations over real-valued data. In addition, we introduce several techniques to handle identifiers in large domains, e.g., 64 or 128 bits, while ensuring high precision for accurate downstream computations. Finally, we implement and benchmark our protocol, compare it against state-of-the-art methods, and perform evaluation over real-world fraud datasets, demonstrating its scalability and efficiency in large-scale use case scenarios. Our results show up to 1.4$\times$ to 6.8$\times$ speedup over prior approaches and select and analyze encrypted labels over real-world datasets in under 65 sec., making our protocol practical for real-world deployments.

  匹配依据：MPC: private set intersection

  </details>

- **Constructions of a Family of Nonlinear Permutations of Any Possible Algebraic Degrees with the Optimal Threshold Implementations**
  2025-10-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2016)
  Zhaole Li, Deng Tang

  <details><summary>摘要 / Abstract</summary>

  Side-channel attacks can uncover sensitive data by analyzing information leakages of cryptographic hardware devices caused by the power consumption, timing, electromagnetic, glitches, etc. An attack exploiting these leakages is the differential power analysis (DPA). Threshold Implementation (TI), introduced by Nikova et al. [JoC 24(2):292-321, 2011], was proposed to resist DPA on hardware implementations of block ciphers and eliminate information leakage due to glitches. TI is based on secret sharing and multi-party computation. Since the cost of implementing a TI is directly proportional to the number of shares, minimizing the number of shares is of importance. Note that Nikova et al. proved that, for a target function of algebraic degree $t\geq 2$, the lower bound on the number of shares to implement a TI is $t+1$. And we call a TI with $t+1$ shares an optimal TI. However, achieving this bound is challenging. To date, the only universal construction for any bijective function of algebraic degree $t\geq 2$ achieves a TI with $t+2$ shares, which was proposed by Piccione et al. [IEEE TIT 69(10):6700-6710, 2023]. Only two studies managed to implement optimal TIs. They either concentrated on the Feistel structure or were based on Shannon&#x27;s expansion. It should be noted that adding randomness can meet the $t+1$ bound, but generating randomness is expensive in practice. Consequently, this paper endeavors to fill this gap by systematically investigating the substitution-boxes (S-boxes to be brief) that can achieve optimal TIs without additional randomness. In this paper, inspired by the Feistel structure in the design of S-boxes, we present two constructions of bijective S-boxes with optimal TIs. Of particular interest is the S-boxes constructed from two permutations exhibiting nonzero nonlinearity, making them potential candidates for S-boxes with desirable properties. For applications, our constructions can interpret the existence of $3$-share or $4$-share TIs for certain functions in $3$, $4$ and $5$ variables, as previously reported by Bilgin et al. [CHES 7428:76-91, 2012] and Božilov et al. [ToSC 2017(1):398-404, 2017], including $\mathcal{Q}_5^{25}$, which cannot be interpreted by the previous works. We also give the bijective S-boxes, which are Examples 4 to 11, that possess the optimal TIs by our results.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Batched and Packed (Publicly) Verifiable Secret Sharing: A Unified Framework and Applications**
  2025-10-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2018)
  Shahla Atapoor, Karim Baghery, Georgio Nicolas, Robi Pedersen, Jannik Spiessens

  <details><summary>摘要 / Abstract</summary>

  Verifiable Secret Sharing (VSS) allows a dealer to distribute a secret among $n$ parties so that each can verify their share&#x27;s validity, and any qualified subset can reconstruct the secret. Publicly Verifiable Secret Sharing (PVSS) extends VSS by enabling anyone to verify the correctness of distributed shares. Both VSS and PVSS schemes are core building blocks in many cryptographic applications. We introduce a $k$-batched and $l$-packed extension of $\Pi$, a unified framework from PKC 2025 for Shamir-based computational VSS in the synchronous setting with optimal resilience. Our framework enables the sharing and verification of $l\times k$ secrets in a single protocol execution, offering a tunable trade-off between efficiency and robustness: the $k$-batched, non-packed variant ($l=1$) improves performance while maintaining optimal resilience, whereas the $k$-batched, $l$-packed variant achieves even greater efficiency at the cost of slightly reduced fault tolerance. Using this framework, we construct several Batched and Packed (BP) VSS and PVSS schemes that significantly reduce both computational and communication costs for the dealer and parties. When sharing many secrets, two of our VSS schemes and our PVSS scheme perform almost as efficiently as plain Shamir sharing. For example, when sharing more than 100 secrets, the overhead of our hash-based BP-VSS is below 3%, for our BP-VSS with information-theoretic privacy it remains around 8%, and for our BP-PVSS it is under 1%. These results show that verifiability in Shamir secret sharing can be achieved in post-quantum and large-scale settings with negligible overhead for the dealer. Our proposed BP-PVSS scheme is the first that can achieve these properties and outperforms existing state-of-the-art protocols. We discuss several applications and, as a concrete case study, use our BP-PVSS scheme to revisit the ALBATROSS randomness generation protocol from ASIACRYPT 2020, yielding a more efficient variant.

  匹配依据：MPC: secret sharing

  </details>

- **Weight distributions of two classes of linear codes with few weights derived from Weil sums**
  2025-10-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.25578)
  Mrinal Kanti Bose, Abhay Kumar Singh

  <details><summary>摘要 / Abstract</summary>

  Linear codes with few weights have been a subject of study for many years, as they have applications in secret sharing, authentication codes, association schemes, and strongly regular graphs. In this article, two distinct classes of $p$-ary linear codes are constructed through the selection of two specific defining sets. Their weight distributions are completely determined for each case by detailed calculations on certain Weil sums. The constructed codes are shown to have only two, four, six, eight, and nine nonzero weights under different cases. In particular, we obtained an infinite family of two-weight optimal linear codes with respect to the Griesmer bound. Moreover, we observe that some of our newly constructed codes are minimal under certain conditions.

  匹配依据：MPC: secret sharing

  </details>

- **Network Oblivious Transfer via Noisy Broadcast Channels**
  2025-10-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.25343)
  Hadi Aghaee, Christian Deppe, Holger Boche

  <details><summary>摘要 / Abstract</summary>

  This paper investigates information-theoretic oblivious transfer via a discrete memoryless broadcast channel with one sender and two receivers. We analyze both non-colluding and colluding honest-but-curious user models and establish general upper bounds on the achievable oblivious transfer capacity region for each case. Two explicit oblivious transfer protocols are proposed. The first ensures correctness and privacy for independent, non-colluding receivers by leveraging the structure of binary erasure broadcast channels. The second protocol, secure even under receiver collusion, introduces additional entropy-sharing and privacy amplification mechanisms to preserve secrecy despite information leakage between users. Our results show that for the non-colluding case, the upper and lower bounds on oblivious transfer capacity coincide, providing a complete characterization of the achievable region. The work provides a unified theoretical framework bridging network information theory and cryptographic security, highlighting the potential of noisy broadcast channels as powerful primitives for multi-user privacy-preserving communication.

  匹配依据：MPC: oblivious transfer

  </details>

- **Towards a Functionally Complete and Parameterizable TFHE Processor**
  2025-10-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.23483)
  Valentin Reyes Häusler, Gabriel Ott, Aruna Jayasena, Andreas Peter

  <details><summary>摘要 / Abstract</summary>

  Fully homomorphic encryption allows the evaluation of arbitrary functions on encrypted data. It can be leveraged to secure outsourced and multiparty computation. TFHE is a fast torus-based fully homomorphic encryption scheme that allows both linear operations, as well as the evaluation of arbitrary non-linear functions. It currently provides the fastest bootstrapping operation performance of any other FHE scheme. Despite its fast performance, TFHE suffers from a considerably higher computational overhead for the evaluation of homomorphic circuits. Computations in the encrypted domain are orders of magnitude slower than their unencrypted equivalents. This bottleneck hinders the widespread adoption of (T)FHE for the protection of sensitive data. While state-of-the-art implementations focused on accelerating and outsourcing single operations, their scalability and practicality are constrained by high memory bandwidth costs. In order to overcome this, we propose an FPGA-based hardware accelerator for the evaluation of homomorphic circuits. Specifically, we design a functionally complete TFHE processor for FPGA hardware capable of processing instructions on the data completely on the FPGA. In order to achieve a higher throughput from our TFHE processor, we implement an improved programmable bootstrapping module, which outperforms the current state-of-the-art by 240% to 480% more bootstrappings per second. Our efficient, compact, and scalable design lays the foundation for implementing complete FPGA-based TFHE processor architectures.

  匹配依据：MPC: multiparty computation

  </details>

- **Experimental Multipartite Entanglement Detection With Minimal-Size Correlations**
  2025-10-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.22918)
  Dian Wu, Fei Shi, Jia-Cheng Sun, Bo-Wen Wang, Xue-Mei Gu, Giulio Chiribella, Qi Zhao, Jian Wu

  <details><summary>摘要 / Abstract</summary>

  Multiparticle entanglement is a valuable resource for quantum technologies, including measurement based quantum computing, quantum secret sharing, and a variety of quantum sensing applications. The direct way to detect this resource is to observe correlations arising from local measurements performed simultaneously on all particles. However, this approach is increasingly vulnerable to measurement imperfections when the number of particles grows, and becomes unfeasible for large-scale entangled states. It is therefore crucial to devise detection methods that minimize the number of simultaneously measured particles. Here we provide the first experimental demonstration of multipartite entanglement detection with minimal-size correlations, showing that our setup is robust to misalignment of the local measurement bases and enables the certification of genuine multipartite entanglement in a regime where the direct approach fails. Overall, our results indicate a promising route to the experimental detection of genuine multipartite entanglement in large-scale entangled states.

  匹配依据：MPC: secret sharing

  </details>

- **Trust, But Verify When Using the Powers of Tau**
  2025-10-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2000)
  Karim Baghery

  <details><summary>摘要 / Abstract</summary>

  To mitigate trust concerns in the setup phase of pairing-based zk-SNARKs, the primary solution has been the sampling of the Structured Reference String (SRS) using an MPC protocol. In 2017, Bowe, Gabizon, and Miers introduced the Powers of Tau MPC protocol for sampling a universal SRS, which has since become the main SRS generation protocol for numerous practical projects. The protocol&#x27;s designers showed that for a circuit with $2^{21}$ multiplication gates, verifying the universal SRS for Groth16 zk-SNARK could take $55$ minutes for a single update. However, they clarified that &quot;the verification is not run by individual users; it is done by the coordinator and anyone who wishes to verify the transcript of the protocol after completion&quot;. This note demonstrates the importance of verifying the final SRS by either $\textit{each}$ individual end-user or $\textit{all}$ ceremony participants to mitigate potential attacks. We discuss simple attack scenarios that highlight vulnerabilities if $\textit{each}$ end-user or $\textit{all}$ participants fail to verify the final SRS. Additionally, by leveraging batching and aggregating techniques, we introduce an efficient verification algorithm for the (original) Powers of Tau protocol, substantially reducing SRS verification time and making it practical even for large-scale ceremonies. In the case of rejection, a more efficient recursive verification approach aids in identifying malicious parties more effectively. This note aims to enhance procedural understanding of SRS generation ceremonies through the Powers of Tau protocol and improve the reliability of current ceremonies against potential threats.

  匹配依据：MPC: mpc (context)

  </details>

- **Pseudorandom Correlation Functions for Multiparty Beaver Triples from Sparse LPN**
  2025-10-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2002)
  Sebastian Hasler, Pascal Reisert

  <details><summary>摘要 / Abstract</summary>

  We construct a pseudorandom correlation function (PCF) for oblivious linear evaluation (OLE) from sparse LPN over any finite field. The programmability property of our PCF implies a PCF for any multiparty degree-two correlation, e.g., Beaver triples. Our PCF is the first PCF for degree-two correlations from a well-established cryptographic assumption, apart from (inefficient) generic PCFs based on homomorphic secret sharing or fully homomorphic encryption. Our PCF outperforms the previously fastest PCF for Beaver triples (Boyle et al., Crypto 2022) by 3.2-28x. We build on the recent pseudorandom correlation generator (PCG) by Miao et al. (Asiacrypt 2025) and extend it to a PCF using a recursive approach similar to Braun et al. (Asiacrypt 2025). Moreover, we extend these techniques to support authenticated degree-two correlations in the important two-party case.

  匹配依据：MPC: secret sharing

  </details>

- **On Computational VSS for General Access Structures**
  2025-10-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/2001)
  Shahla Atapoor, Karim Baghery, Robin Jadoul, Barry van Leeuwen

  <details><summary>摘要 / Abstract</summary>

  Verifiable Secret Sharing (VSS) schemes are fundamental building blocks in distributed cryptography. While most existing works focus on threshold structures, many real-world applications require more general access structures, where participants have different levels of power and only certain subsets are authorized to reconstruct the secret. Existing computational VSS schemes for general access structures typically rely on Discrete Logarithm (DL)-based homomorphic commitments, which limits their applicability, particularly in scenarios requiring Post-Quantum (PQ) security. In this work, we present a generalized version of $\mathrm{\Pi}$, a unified framework introduced at PKC 2025 for constructing computational VSS schemes without relying on homomorphic commitments. Our framework supports arbitrary monotone $\mathcal{Q}_2$ access structures, encompassing replicated and threshold secret sharing (e.g., Shamir&#x27;s scheme), while preserving the efficiency and modularity of $\mathrm{\Pi}$. Notably, it requires only a random oracle and any commitment scheme satisfying hiding and binding, making it compatible with a wide range of instantiations, including PQ-secure commitments. In particular, our hash-based instantiation yields the first symmetric-key-based VSS scheme for general access structures. Compared to prior general-access VSS schemes based on homomorphic commitments (e.g., variants of Pedersen scheme from FC 2003), our DL-based constructions eliminate the need for homomorphic commitments and achieve asymptotic improvements in verification and reconstruction costs. We believe that this extension enhances the versatility of the original $\mathrm{\Pi}$ framework and paves the way for its deployment in a broader range of practical distributed systems.

  匹配依据：MPC: secret sharing

  </details>

- **New Security Proofs of MPC-in-the-Head Signatures in the Quantum Random Oracle Model**
  2025-10-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1999)
  Haruhisa Kosuge, Keita Xagawa

  <details><summary>摘要 / Abstract</summary>

  The MPC-in-the-Head paradigm is a promising approach for constructing post-quantum signature schemes. Its significance is underscored by NIST&#x27;s selection of six signatures based on this paradigm and its variants, TC-in-the-Head and VOLE-in-the-Head, among the fourteen round-2 candidates in its additional post-quantum cryptography standardization process. Recent works by Aguilar-Melchor et al. (ASIACRYPT 2023), Hülsing et al. (CRYPTO 2024), and Baum et al. (CRYPTO 2025) have established EUF-CMA security for these signatures in the Quantum Random Oracle Model (QROM). However, their proofs do not account for crucial optimization techniques such as rejection sampling and grinding, rendering them inapplicable to practical schemes like the NIST round-2 candidates Mirath and RYDE. This paper addresses this gap by analyzing the QROM security of MPC-in-the-Head signatures that incorporate these optimizations, with a focus on Mirath and RYDE. We make two main contributions: 1) We provide a new (strong) EUF-CMA security proof that accommodates rejection sampling and grinding. We also present a new EUF-NMA security proof compatible with these optimizations, by extending the techniques of Don et al. (CRYPTO 2022) and Aguilar-Melchor et al. (ASIACRYPT 2023). 2) We also point out a gap in the EUF-CMA security proof of the MPC-in-the-Head signature schemes using correlated-tree techniques, MQOM, SBC (Huth and Joux, CRYPTO 2024), and rBN++ (Kim, Lee, and Son, EUROCRYPT 2025).

  匹配依据：MPC: mpc (context)

  </details>

- **OUF: Oblivious Universal Function with domain specific optimizations**
  2025-10-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1985)
  Victor Delfour, Marc-Olivier Killijian

  <details><summary>摘要 / Abstract</summary>

  The growing need for secure computation has spurred interest in cryptographic techniques that operate on encrypted data without revealing its content. Fully Homomorphic Encryption (FHE), especially LWE-based schemes, enables such processing while preserving confidentiality. Decentralized computing offers scalable resources without requiring in-house servers, but it relies heavily on the confidentiality guarantees of underlying schemes. While many existing protocols successfully protect input privacy, function confidentiality remains a largely overlooked but crucial aspect of secure delegated computation. In this work, we present a novel Oblivious Universal Function (OUF) scheme that enables a client to outsource computation of an arbitrary function to an untrusted server while hiding both the input data and the function being applied. Our construction leverages LWE-based FHE and a virtual-tape evaluation model to support composable, non-interactive, and reusable function execution. Crucially, the server remains oblivious not only to the encrypted inputs but also to the structure, type, and identity of the function it is executing. OUF thus bridges the gap between theoretical privacy guarantees and practical secure computation in decentralized environments.

  匹配依据：MPC: secure computation

  </details>

- **zk-Agreements: A Privacy-Preserving Way to Establish Deterministic Trust in Confidential Agreements**
  2025-10-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.20007)
  To-Wen Liu, Matthew Green

  <details><summary>摘要 / Abstract</summary>

  Digital transactions currently exceed trillions of dollars annually, yet traditional paper-based agreements remain a bottleneck for automation, enforceability, and dispute resolution. Natural language contracts introduce ambiguity, require manual processing, and lack computational verifiability, all of which hinder efficient digital commerce. Computable legal contracts, expressed in machine-readable formats, offer a potential solution by enabling automated execution and verification. Blockchain-based smart contracts further strengthen enforceability and accelerate dispute resolution; however, current implementations risk exposing sensitive agreement terms on public ledgers, raising serious privacy and competitive intelligence concerns that limit enterprise adoption. We introduce zk-agreements, a protocol designed to transition from paper-based trust to cryptographic trust while preserving confidentiality. Our design combines zero-knowledge proofs to protect private agreement terms, secure two-party computation to enable private compliance evaluation, and smart contracts to guarantee automated enforcement. Together, these components achieve both privacy preservation and computational enforceability, resolving the fundamental tension between transparency and confidentiality in blockchain-based agreements.

  匹配依据：MPC: secure two party computation

  </details>

- **Cryptography with Weak Privacy**
  2025-10-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1978)
  Amos Beimel, Yuval Ishai, Eyal Kushilevitz, Hanjun Li

  <details><summary>摘要 / Abstract</summary>

  We initiate a systematic study of information-theoretic cryptography with {\em weak privacy}, only requiring that the adversary cannot rule out any possible secret. For a parameter $0 0$. We obtain the following main results. Positive results. We present efficient WP constructions for generalized secret sharing, decomposable randomized encodings, and the related notions of garbling schemes and PSM protocols, as well as interactive secure multiparty computation protocols in the plain model and in the OT-hybrid model. For secret sharing, we settle a question of Beimel and Franklin (TCC 2007), showing that every $n$-party access structure admits a WP scheme with per-party share size $O(n)$. When all unauthorized sets have constant size, we get a $p$-WP scheme with constant share size and $p\ge 1/poly(n)$. Negative result. For decomposable randomized encodings, we show that a previous lower bound technique of Ball et al.\ (ITCS 2020) applies also to the WP notion. Together with our upper bound, this shows that the optimal WP garbling size of the worst-case $f:\{0,1\}^n\to\{0,1\}$ is $\tilde{\Theta}(n^2)$. Application. While WP may seem like an unrealistically weak security notion, we demonstrate its usefulness towards achieving traditional security guarantees. Concretely, under the standard LPN assumption, we show that any $p$-WP secret-sharing scheme with inverse-polynomial $p$ implies a {\em computationally secure} secret-sharing scheme for a related access structure. Together with our positive results for WP secret sharing, this implies a super-polynomial improvement of the share size for a natural class of access structures.

  匹配依据：MPC: garbling schemes, secret sharing, secure multiparty computation

  </details>

- **General Key Recovery Attack on Pointwise-Keyed Functions - Application to Alternating Moduli Weak PRFs**
  2025-10-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1971)
  Antoine Sidem, Qingju Wang

  <details><summary>摘要 / Abstract</summary>

  The increasing use of multi-party computation (MPC) has spurred the design of symmetric key primitives specifically suited for MPC environments. Recently, weak pseudorandom functions (wPRFs) based on the alternating moduli paradigm have been proposed as a promising class of MPC-friendly primitives. The wPRF proposed at CRYPTO 2024, in its One-to-One parameter set, has been shown to be vulnerable to a key recovery attack dubbed Zeroed-Out, exploiting collisions in the queries. In this paper, we identify that the aforementioned wPRFs conform to a specific structure, called pointwise-keyed function, and further show a different, general key recovery attack. This method, applied to wPRFs in the One-to-One parameter set attacked by Zeroed-out, improves upon the complexity and achieves an attack with complexity below the birthday bound, and stays effective against the proposed countermeasures. For the first time, it succeeds in attacking one of the two Many-to-One parameter sets and stays effective against one of the proposed countermeasures. We also consider its applicability to the alternative wPRF of similar structure proposed by Boneh et al at TCC 2018.

  匹配依据：MPC: multi party computation

  </details>

- **Formalisation of the KZG polynomial commitment schemes in EasyCrypt**
  2025-10-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1972)
  Palak, Thomas Haines

  <details><summary>摘要 / Abstract</summary>

  In this paper, we present formally verified proofs of the popular KZG Polynomial Commitment Schemes (PCSs), including the security proofs for the properties of correctness, polynomial binding, evaluation binding and hiding. Polynomial commitment schemes have various applications in cryptography and computer science, including verifiable computation, blockchain and cryptocurrencies, secure multi-party computation as well as in the construction of ZK-SNARKs. To validate security, we utilise EasyCrypt, an interactive theorem prover that allows for formal verification of cryptographic primitives and protocols. This approach enforces correct proofs which cover all required cases and formalising assumptions reducing the risk of overlooked vulnerabilities. This formalisation validates the current understanding of KZG&#x27;s PCSs as secure while clarifying various issues in the original claims.

  匹配依据：MPC: secure multi party computation

  </details>

- **Single-Shuffle Full-Open Card-Based Secure Computation Protocols for Any Function**
  2025-10-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.17308)
  Reo Eriguchi, Kazumasa Shinagawa

  <details><summary>摘要 / Abstract</summary>

  A card-based secure computation protocol is a method for $n$ parties to compute a function $f$ on their private inputs $(x_1,\ldots,x_n)$ using physical playing cards, in such a way that the suits of revealed cards leak no information beyond the value of $f(x_1,\ldots,x_n)$. A \textit{single-shuffle full-open} protocol is a minimal model of card-based secure computation in which, after the parties place face-down cards representing their inputs, a single shuffle operation is performed and then all cards are opened to derive the output. Despite the simplicity of this model, the class of functions known to admit single-shuffle full-open protocols has been limited to a few small examples. In this work, we prove for the first time that every function admits a single-shuffle full-open protocol. We present two constructions that offer a trade-off between the number of cards and the complexity of the shuffle operation. These feasibility results are derived from a novel connection between single-shuffle full-open protocols and a cryptographic primitive known as \textit{Private Simultaneous Messages} protocols, which has rarely been studied in the context of card-based cryptography. We also present variants of single-shuffle protocols in which only a subset of cards are revealed. These protocols reduce the complexity of the shuffle operation compared to existing protocols in the same setting.

  匹配依据：MPC: secure computation

  </details>

- **On the Communication Complexity of PSM and CDS for Symmetric Functions**
  2025-10-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1959)
  Reo Eriguchi

  <details><summary>摘要 / Abstract</summary>

  Private Simultaneous Messages (PSM) and Conditional Disclosure of Secrets (CDS) are two fundamental primitives in information-theoretic cryptography. In a PSM protocol, each party sends a single message to a referee, who can then compute a function $f$ of their private inputs but learns nothing else. A CDS protocol follows the same model as PSM, but the goal is to disclose a secret shared among all parties to the referee if and only if the function $f$ evaluates to $1$. Minimizing the communication complexity of these primitives is a central question in this area. Since the best known constructions for general functions require high communication complexity, recent studies have attempted to obtain more efficient constructions by focusing on symmetric functions, whose outputs are invariant under permutations of inputs. However, the extent to which exploiting symmetry can improve efficiency has remained unclear. In this work, we show upper and lower bounds that relate the optimal communication complexities of PSM and CDS for symmetric functions to those for general functions. When the number of parties is larger than the input domain size, our upper bound for PSM improves the best known communication complexity for symmetric functions. Furthermore, our upper bound for CDS demonstrates for the first time that symmetry can be exploited to reduce communication in CDS protocols. In contrast, when the number of parties is constant, our lower bounds show that focusing on symmetric functions yields only a constant-factor improvement. We also derive an analogous implication for PSM protocols under a plausible conjecture. In addition, our new constructions for symmetric functions lead to improvements over the state-of-the-art results in related models such as ad hoc PSM and secret sharing.

  匹配依据：MPC: secret sharing

  </details>

- **A Lattice-Based IND-CCA Threshold KEM from the BCHK+ Transform**
  2025-10-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1958)
  Oleksandra Lapiha, Thomas Prest

  <details><summary>摘要 / Abstract</summary>

  We present a simple IND-CCA lattice-based threshold KEM. At a high level, our design is based on the BCHK transform (Canetti et al., EUROCRYPT 2004), which we adapt to the lattice setting by combining it with the FO transform (Fujisaki and Okamoto, PKC 1999) in order to achieve decryption consistency. As for the BCHK transform, our construction requires a threshold identity-based encryption (TIBE) scheme with suitable properties. We build such an IBE by combining the ABB IBE (Agrawal, Boneh, Boyen, EUROCRYPT 2010) with recent advances in lattice threshold cryptography, such as the threshold-friendly signature Plover (Esgin et al., EUROCRYPT 2024) and a variant of the Threshold Raccoon scheme (Katsumata et al., CRYPTO 2024). The security proof of our scheme relies on a new assumption which we call the Coset-Hint-MLWE assumption, and which is a natural generalisation of the Hint-MLWE assumption (Kim et al., CRYPTO 2023). We prove the hardness of Coset-Hint-MLWE under standard assumptions. We believe this new assumption may be of independent interest. Unlike prior works on IND-CCA lattice-based threshold KEMs, our construction only relies on simple algorithmic tools and does not use heavy machinery such as multi-party computation or threshold fully homomorphic encryption.

  匹配依据：MPC: multi party computation

  </details>

- **Robust and Scalable Lattice-Based Distributed Key Generation for Asynchronous Networks**
  2025-10-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1946)
  Linghe Yang, Jian Liu, Jingyi Cui, Guangquan Xu, Zhongshan Li, Lei Zhang, Mingzi Zuo, Kaitai Liang

  <details><summary>摘要 / Abstract</summary>

  Distributed Key Generation (DKG) is essential for secure, decentralized cryptographic systems, enabling collaborative key pair generation without a trusted authority. This capability underpins critical applications such as threshold signatures and blockchain-based protocols. To achieve post-quantum security, existing robust lattice-based DKG protocols, tailored for synchronous networks, rely on complaint-based Verifiable Secret Sharing (VSS). However, these protocols lack public verifiability and compatibility with asynchronous environments, constraining their use in Byzantine fault-tolerant settings. This paper presents LADKG, the first Lattice-Based Asynchronous Distributed Key Generation protocol designed for post-quantum secure and scalable distributed systems. LADKG integrates Asynchronous Verifiable Short Secret Sharing (AV3S) with an Approximate Asynchronous Common Subset (AACS) protocol to achieve efficient key generation. By deferring verification and leveraging deterministic approximate agreement, LADKG reduces computational and communication overhead while maintaining security and robustness. Evaluations on geo-distributed AWS EC2 clusters demonstrate that LADKG is comparable or better than classical Asynchronous Distributed Key Generation (ADKG) schemes in scalability and efficiency. Under optimistic conditions with $n=121$ nodes, completion is achieved in 45 seconds, ensuring robust key generation for post-quantum secure applications.

  匹配依据：MPC: secret sharing

  </details>

- **Minicrypt PRFs Do Not Admit Black-Box Oblivious Evaluations**
  2025-10-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1947)
  Cruz Barnum, Mohammad Hajiabadi, David Heath, Jake Januzelli, Naman Kumar, Mike Rosulek

  <details><summary>摘要 / Abstract</summary>

  Oblivious Pseudorandom Function (OPRF) protocols can be categorized into two variants: chosen-key OPRFs -- where the server provides the PRF key $k$ as an input -- and ephemeral-key OPRFs -- where the functionality randomly samples $k$ on behalf of the server. Ephemeral-key OPRFs can be constructed from simple cryptography, such as black-box OT and a random oracle. Chosen-key OPRFs, on the other hand, are only known by employing one of the following (more expensive) approaches: - Express the underlying PRF as a circuit, then use generic MPC techniques to evaluate it in a non-black-box manner. - Base the underlying PRF on some specific public-key assumption, such as RSA or DDH, then build a custom protocol that achieves obliviousness by leveraging the PRF&#x27;s algebraic structure. Thus, there exists a qualitative gap between known instantiations of these two OPRF variants, in terms of both assumptions and efficiency. We show that this gap is inherent. In particular, one might hope for an OPRF with all of the following characteristics: the protocol (1) is chosen-key, (2) supports domains of super-polynomial size, and (3) is constructed from &quot;simple&quot; cryptography, such as the minimal assumption of OT, plus a random oracle. We show that no such protocol can exist. Let $\Pi$ be any chosen-key OPRF protocol defined in terms of a PRF $F$, where $F$ is defined with respect to (only) a random oracle. This restriction on $F$ rules out the above approaches of either using a PRF in a non-black-box way or basing the underlying PRF itself on public-key cryptography. While $F$ is restricted in its use of cryptography, the protocol $\Pi$ is not: $\Pi$ may use arbitrary cryptography, e.g., OT, FHE, iO, etc. We show that each invocation of any such $\Pi$ necessarily leaks information about the server&#x27;s key $k$. After a bounded number of queries, an adversarial client can effectively recover $k$, breaking server privacy. To complement our negative result, we provide a matching positive result: we construct a chosen-key OPRF from black-box OT and RO, where server privacy holds for some bounded number of queries $n$. This protocol&#x27;s underlying PRF is constructed from a $(n+1)$-wise independent hash function and RO; the server&#x27;s key $k$ has length scaling linearly in $n$ which, by our lower bound, is optimal. Thus, our two results tightly (i.e., up to $\mathrm{poly}(\lambda)$ factors) characterize (im)possibility for chosen-key OPRFs, unless one uses non-black-box cryptography or a public-key-style PRF.

  匹配依据：MPC: mpc (context)

  </details>

- **Efficient and Privacy-Preserving Binary Dot Product via Multi-Party Computation**
  2025-10-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.16331)
  Fatemeh Jafarian Dehkordi, Elahe Vedadi, Alireza Feizbakhsh, Yasaman Keshtkarjahromi, Hulya Seferoglu

  <details><summary>摘要 / Abstract</summary>

  Striking a balance between protecting data privacy and enabling collaborative computation is a critical challenge for distributed machine learning. While privacy-preserving techniques for federated learning have been extensively developed, methods for scenarios involving bitwise operations, such as tree-based vertical federated learning (VFL), are still underexplored. Traditional mechanisms, including Shamir&#x27;s secret sharing and multi-party computation (MPC), are not optimized for bitwise operations over binary data, particularly in settings where each participant holds a different part of the binary vector. This paper addresses the limitations of existing methods by proposing a novel binary multi-party computation (BiMPC) framework. The BiMPC mechanism facilitates privacy-preserving bitwise operations, with a particular focus on dot product computations of binary vectors, ensuring the privacy of each individual bit. The core of BiMPC is a novel approach called Dot Product via Modular Addition (DoMA), which uses regular and modular additions for efficient binary dot product calculation. To ensure privacy, BiMPC uses random masking in a higher field for linear computations and a three-party oblivious transfer (triot) protocol for non-linear binary operations. The privacy guarantees of the BiMPC framework are rigorously analyzed, demonstrating its efficiency and scalability in distributed settings.

  匹配依据：MPC: multi party computation, oblivious transfer, secret sharing

  </details>

- **Secure Sparse Matrix Multiplications and their Applications to Privacy-Preserving Machine Learning**
  2025-10-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.14894)
  Marc Damie, Florian Hahn, Andreas Peter, Jan Ramon

  <details><summary>摘要 / Abstract</summary>

  To preserve data privacy, multi-party computation (MPC) enables executing Machine Learning (ML) algorithms on private data. However, MPC frameworks do not include optimized operations on sparse data. This absence makes them unsuitable for ML applications involving sparse data; e.g., recommender systems or genomics. Even in plaintext, such applications involve high-dimensional sparse data, that cannot be processed without sparsity-related optimizations due to prohibitively large memory requirements. Since matrix multiplication is a central building block of ML algorithms, our work proposes dedicated MPC algorithms to multiply secret-shared sparse matrices. Our sparse algorithms have several advantages over secure dense matrix multiplications (i.e., the classic multiplication). On the one hand, they avoid the memory issues caused by the &quot;dense&quot; data representation of dense multiplications. On the other hand, our algorithms can significantly reduce communication costs (up to $\times1000$) for realistic problem sizes. We validate our algorithms in two machine learning applications where dense matrix multiplications are impractical. Finally, we take inspiration from real-world sparse data properties to build 3 techniques minimizing the public knowledge necessary to secure sparse algorithms.

  匹配依据：MPC: multi party computation

  </details>

- **Noisy Function Secret Sharing and its applications to Differentially Private computations**
  2025-10-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1937)
  Marc Damie, Federico Mazzone, Florian Hahn, Andreas Peter, Jan Ramon

  <details><summary>摘要 / Abstract</summary>

  Function Secret Sharing (FSS) schemes enable to share secret functions between multiple parties, with notable applications in anonymous communication and privacy-preserving machine learning. While two-party schemes offer logarithmic key sizes, multi-party schemes remain less practical due to significantly larger keys. Although several approaches have been proposed to improve multi-party schemes, a significant efficiency gap remains between the two-party and multi-party settings. Our work introduces noisy FSS: a relaxation of FSS preserving the standard privacy guarantees but relaxing the correctness definition by allowing a small amount of noise in the output. We formally define noisy FSS and show how the noise introduced by the scheme can be leveraged to provide differential private outputs in statistics applications. To demonstrate the benefits of this relaxation, we adapt a scheme proposed by Corrigan-Gibbs et al. (S&amp;P&#x27;15). While their scheme provides the smallest key sizes among multi-party schemes, they do not support some applications notably in statistics due to their non-linear share decoding. On the contrary, recent works such as Goel et al. (CRYPTO&#x27;25) have larger keys, but support all FSS applications. Our noisy adapted scheme offers the best of both worlds by matching the best key sizes, while providing the properties necessary to statistics applications.

  匹配依据：MPC: secret sharing

  </details>

- **High-efficiency and long-distance quantum memory-assisted device-independent quantum secret sharing with single photon sources**
  2025-10-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.12288)
  Qi Zhang, Jia-Wei Ying, Shi-Pu Gu, Xing-Fu Wang, Ming-Ming Du, Wei Zhong, Lan Zhou, Yu-Bo Sheng

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) plays a critical role in building the distributed quantum networks. Device-independent (DI) QSS provides the highest security level for QSS. However, the photon transmission loss and extremely low multipartite entanglement generation rate largely limit DI QSS&#x27;s secure photon transmission distance (less than 1 km) and practical key generation efficiency. To address the above drawbacks, we propose the quantum memory-assisted (QMA) DI QSS protocol based on single photon sources (SPSs). The single photons from the SPSs are used to construct long-distance multipartite entanglement channels with the help of the heralded architecture. The heralded architecture enables our protocol to have an infinite secure photon transmission distance in theory. The QMA technology can not only increase the multi-photon synchronization efficiency, but also optimize the photon transmittance to maximize the construction efficiency of the multipartite entanglement channels. Our protocol achieves the practical key generation efficiency seven orders of magnitude higher than that of the existing DI QSS protocols based on cascaded spontaneous parametric down-conversion sources and six orders of magnitude higher than that of the DI QSS based on SPSs without QMA. Our protocol has modular characteristics and is feasible under the current experimental technical conditions. Combining with the advanced random key generation basis strategy, the requirement on experimental devices can be effectively reduced. Our protocol is expected to promote the development of long-distance and high-efficiency DI quantum network in the future.

  匹配依据：MPC: secret sharing

  </details>

- **MPCitH Signature from Restricted Syndrome Decoding**
  2025-10-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1908)
  Michele Battagliola, Ethan Y. Chen, Hugo Sauerbier Couvée, Violetta Weger

  <details><summary>摘要 / Abstract</summary>

  Abstract. CROSS is a code-based signature based on the Restricted Syndrome Decoding Problem (R-SDP) that is currently among the fourteen candidates in the NIST standardization process. While CROSS enjoys a very competitive verification time, its primary drawback is its significantly large signature size. In this work, we introduce a new Multi-Party Computation in the Head (MPCitH) protocol for the R-SDP with the primary goal of reducing CROSS signature size. To do so, we design a publicly verifiable secret sharing scheme tailored for restricted vectors and a new multiplicative-to-additive conversion for it. These new cryptographic gadgets may be of independent interest as they can serve as building blocks for future research in multi-party computation, such as a threshold version of CROSS.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Post-Quantum Cryptography and Quantum-Safe Security: A Comprehensive Survey**
  2025-10-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.10436)
  Gaurab Chhetri, Shriyank Somvanshi, Pavan Hebli, Shamyo Brotee, Subasish Das

  <details><summary>摘要 / Abstract</summary>

  Post-quantum cryptography (PQC) is moving from evaluation to deployment as NIST finalizes standards for ML-KEM, ML-DSA, and SLH-DSA. This survey maps the space from foundations to practice. We first develop a taxonomy across lattice-, code-, hash-, multivariate-, isogeny-, and MPC-in-the-Head families, summarizing security assumptions, cryptanalysis, and standardization status. We then compare performance and communication costs using representative, implementation-grounded measurements, and review hardware acceleration (AVX2, FPGA/ASIC) and implementation security with a focus on side-channel resistance. Building upward, we examine protocol integration (TLS, DNSSEC), PKI and certificate hygiene, and deployment in constrained and high-assurance environments (IoT, cloud, finance, blockchain). We also discuss complementarity with quantum technologies (QKD, QRNGs) and the limits of near-term quantum computing. Throughout, we emphasize crypto-agility, hybrid migration, and evidence-based guidance for operators. We conclude with open problems spanning parameter agility, leakage-resilient implementations, and domain-specific rollout playbooks. This survey aims to be a practical reference for researchers and practitioners planning quantum-safe systems, bridging standards, engineering, and operations.

  匹配依据：MPC: mpc (context)

  </details>

- **Prismo: A Decision Support System for Privacy-Preserving ML Framework Selection**
  2025-10-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.09985)
  Nges Brian Njungle, Eric Jahns, Luigi Mastromauro, Edwin P. Kayang, Milan Stojkov, Michel A. Kinsy

  <details><summary>摘要 / Abstract</summary>

  Machine learning has become a crucial part of our lives, with applications spanning nearly every aspect of our daily activities. However, using personal information in machine learning applications has sparked significant security and privacy concerns about user data. To address these challenges, different privacy-preserving machine learning (PPML) frameworks have been developed to protect sensitive information in machine learning applications. These frameworks generally attempt to balance design trade-offs such as computational efficiency, communication overhead, security guarantees, and scalability. Despite the advancements, selecting the optimal framework and parameters for specific deployment scenarios remains a complex and critical challenge for privacy and security application developers. We present Prismo, an open-source recommendation system designed to aid in selecting optimal parameters and frameworks for different PPML application scenarios. Prismo enables users to explore a comprehensive space of PPML frameworks through various properties based on user-defined objectives. It supports automated filtering of suitable candidate frameworks by considering parameters such as the number of parties in multi-party computation or federated learning and computation cost constraints in homomorphic encryption. Prismo models every use case into a Linear Integer Programming optimization problem, ensuring tailored solutions are recommended for each scenario. We evaluate Prismo&#x27;s effectiveness through multiple use cases, demonstrating its ability to deliver best-fit solutions in different deployment scenarios.

  匹配依据：MPC: multi party computation

  </details>

- **Beholder Signatures**
  2025-10-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1900)
  Stefan Dziembowski, Sebastian Faust, Paweł Kędzior, Marcin Mielniczuk, Susil Kumar Mohanty, Krzysztof Pietrzak

  <details><summary>摘要 / Abstract</summary>

  We introduce a new primitive, called beholder signatures, which, in some sense, are the opposite of blind signatures. In a beholder signature, one signs a commitment to a (potentially very long) message, and the signature attests that the parties participating in the signing process who know the secret key, jointly also know the entire committed message. This guarantee holds even against distributed adversaries that use secure multi-party computation (MPC) to produce the signature. We work in the distributed adversarial model (Dziembowski, Faust, and Lizurej, Crypto&#x27;23), where one assumes that it is infeasible to evaluate a large number of hash queries without any of the participating parties learning the input. We propose a construction of beholder signatures in the random oracle model. The starting point of our construction is proofs of complete knowledge, recently proposed by (Kelkar et al. CCS&#x27;24), which again build on Fischlin&#x27;s transformation of a sigma protocol to a noninteractive, straight-line extractable zero-knowledge proof of knowledge. Our scheme is concretely efficient and comes with a proof-of-concept implementation using Schnorr as the underlying sigma protocol. The primary applications of beholder signatures can be found within the blockchain ecosystem. In particular, we describe how to use them to construct proofs of custody (Feist, 2021) that do not require ephemeral keys and are noninteractive. We also outline applications to data dissemination, data availability, and proofs of replication.

  匹配依据：MPC: secure multi party computation

  </details>

- **Quantum Channel Masking**
  2025-10-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2510.09456)
  Anna Honeycutt, Hailey Murray, Eric Chitambar

  <details><summary>摘要 / Abstract</summary>

  Quantum masking is a special type of secret sharing in which some information gets reversibly distributed into a multipartite system, leaving the original information inaccessible to each subsystem. This paper proposes a dynamical extension of quantum masking to the level of quantum channels. In channel masking, the identity of a channel becomes locally hidden but still globally accessible after its output is sent through a bipartite broadcasting channel. We first characterize all families of d-dimensional unitaries that can be isometrically masked, a condition that holds even in the presence of depolarizing noise. For the case of qubits, we identify which families of Pauli channels can be masked, and we prove that a qubit channel can be masked against the identity if and only if it is unital and has a pure-state fixed point. Masking against the identity describes a scenario in which channel noise becomes completely delocalized through a broadcast map and undetectable through subsystem dynamics alone.

  匹配依据：MPC: secret sharing

  </details>

- **Fraud Mitigation in Privacy-Preserving Attribution**
  2025-10-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1891)
  Rutchathon Chairattana-Apirom, Stefano Tessaro, Nirvan Tyagi

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving advertisement attribution allows websites selling goods to learn statistics on which advertisement campaigns can be attributed to converting sales. Existing proposals rely on users to locally store advertisement history on their browser and report attribution measurements to an aggregation service (instantiated with multiparty computation over non-colluding servers). The service computes and reveals the aggregate statistic. The service hides individual user contributions, but it does not guarantee integrity against misbehaving users that may submit fraudulent measurements. Our work proposes a new cryptographic primitive, &quot;secret share attestation&quot;, in which secret shares input into a multiparty computation protocol are accompanied by an attestation of integrity by a third party: advertisers include signature attestations when serving ads that are later included in contributed measurements. We propose two constructions based on the standards-track BBS signatures and efficient signatures over equivalence classes, respectively. We implement and evaluate our protocols in the context of the advertising application to demonstrate their practicality.

  匹配依据：MPC: multiparty computation

  </details>
