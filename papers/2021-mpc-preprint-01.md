# 2021 · MPC · 仅预印本来源 · 第 1/3 页

[总目录](../PAPERS.md) · [下一页](2021-mpc-preprint-02.md)

- **Verifiable Encryption from MPC-in-the-Head**
  2021-12-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1704)
  Akira Takahashi, Greg Zaverucha

  <details><summary>摘要 / Abstract</summary>

  Verifiable encryption (VE) is a protocol where one can provide assurance that an encrypted plaintext satisfies certain properties, or relations. It is an important building block in cryptography with many useful applications, such as key escrow, group signatures, optimistic fair exchange, and others. However, the majority of previous VE schemes are restricted to instantiation with specific public-key encryption schemes or relations. In this work, we propose a novel framework that realizes VE protocols using zero-knowledge proof systems based on the MPC-in-the-head paradigm (Ishai et al. STOC 2007). Our generic compiler can turn a large class of zero-knowledge proofs into secure VE protocols for any secure public-key encryption scheme with the undeniability property, a notion that essentially guarantees binding of encryption when used as a commitment scheme. Our framework is versatile: because the circuit proven by the MPC-in-the-head prover is decoupled from a complex encryption function, the work of the prover is focused on proving the encrypted data satisfies the relation, not the proof of plaintext knowledge. Hence, our approach allows for instantiation with various combinations of properties about the encrypted data and encryption functions. We then consider concrete applications, to demonstrate the efficiency of our framework, by first giving a new approach and implementation to verifiably encrypt discrete logarithms in any prime order group more efficiently than was previously known. Then we give the first practical verifiable encryption scheme for AES keys with post-quantum security, along with an implementation and benchmarks.

  匹配依据：MPC: mpc (context)

  </details>

- **Invertible Quadratic Non-Linear Layers for MPC-/FHE-/ZK-Friendly Schemes over $\\mathbb F\_p^n$**
  2021-12-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1695)
  Lorenzo Grassi, Silvia Onofri, Marco Pedicini, Luca Sozzi

  <details><summary>摘要 / Abstract</summary>

  Motivated by new applications such as secure Multi-Party Computation (MPC), Fully Homomorphic Encryption (FHE), and Zero-Knowledge proofs (ZK), many MPC-, FHE- and ZK-friendly symmetric-key primitives that minimize the number of multiplications over $\mathbb{F}_p$ for a large prime $p$ have been recently proposed in the literature. This goal is often achieved by instantiating the non-linear layer via power maps $x\mapsto x^d$. In this paper, we start an analysis of new non-linear permutation functions over $\mathbb{F}_p^n$ that can be used as building blocks in such symmetric-key primitives. Given a local map $F:\mathbb{F}_p^m \rightarrow \mathbb{F}_p$, we limit ourselves to focus on S-Boxes over $\mathbb{F}_p^n$ for $n\ge m$ defined as $\mathcal{S}_F(x_0, x_1, \ldots, x_{n-1}) = y_0\| y_1\| \ldots \| y_{n-1}$ where $y_i := F(x_i, x_{i+1}, \ldots, x_{i+m-1} )$. As main results, we prove that - given any quadratic function $F:\mathbb{F}_p^2 \rightarrow \mathbb{F}_p$, the corresponding S-Box $\mathcal{S}_F$ over $\mathbb{F}_p^n$ for $n\ge 3$ is never invertible; - similarly, given any quadratic function $F:\mathbb{F}_p^3 \rightarrow \mathbb{F}_p$, the corresponding S-Box $\mathcal{S}_F$ over $\mathbb{F}_p^n$ for $n\ge 5$ is never invertible. Moreover, for each $p\ge 3$, we present (1st) generalizations of the Lai-Massey construction over $\mathbb{F}_p^n$ defined as before via functions $F:\mathbb{F}_p^m \rightarrow \mathbb{F}_p$ for each $n=m\ge 2$ and (2nd) (non-trivial) quadratic functions $F:\mathbb{F}_p^3 \rightarrow \mathbb{F}_p$ such that $\mathcal{S}_F$ over $\mathbb{F}_p^n$ for $n\in \{3,4\}$ is invertible. As an open problem for future work, we conjecture that for each $m\ge 1$ there exists a \textit{finite} integer $n_{\text{max}}(m)$ such that $\mathcal{S}_F$ over $\mathbb{F}_p^n$ defined as before via a quadratic function $F:\mathbb{F}_p^m \rightarrow \mathbb{F}_p$ is \textit{not} invertible for each $n\ge n_{\text{max}}(m)$. Finally, as a concrete application, we propose Neptune, a variant of the sponge hash function Poseidon, whose non-linear layer is designed by taking into account the results presented in this paper. We show that this variant leads to a concrete multiplication reduction with respect to Poseidon.

  匹配依据：MPC: secure multi party computation

  </details>

- **Computational Irrelevancy: Bridging the Gap between Pseudo- and Real Randomness in MPC Protocols**
  2021-12-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1687)
  Nariyasu Heseri, Koji Nuida

  <details><summary>摘要 / Abstract</summary>

  Due to the fact that classical computers cannot efficiently obtain random numbers, it is common practice to design cryptosystems in terms of real random numbers and then replace them with (cryptographically secure) pseudorandom ones for concrete implementations. However, as pointed out by [Nuida, PKC 2021], this technique may lead to compromise of security in secure multiparty computation (MPC) protocols. Although this work suggests using information-theoretically secure protocols and pseudorandom generators (PRGs) with high min-entropy to alleviate the problem, yet it is preferable to base the security on computational assumptions rather than the stronger information-theoretic ones. By observing that the contrived constructions in the aforementioned work use MPC protocols and PRGs that are closely related to each other, we notice that it may help to alleviate the problem by using protocols and PRGs that are &quot;unrelated&quot; to each other. In this paper, we propose a notion called &quot;computational irrelevancy&quot; to formalise the term &quot;unrelated&quot; and under this condition provide a security guarantee under computational assumptions.

  匹配依据：MPC: secure multiparty computation

  </details>

- **MPCLeague: Robust MPC Platform for Privacy-Preserving Machine Learning**
  2021-12-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2112.13338)
  Ajith Suresh

  <details><summary>摘要 / Abstract</summary>

  In the modern era of computing, machine learning tools have demonstrated their potential in vital sectors, such as healthcare and finance, to derive proper inferences. The sensitive and confidential nature of the data in such sectors raises genuine concerns for data privacy. This motivated the area of Privacy-preserving Machine Learning (PPML), where privacy of data is guaranteed. In this thesis, we design an efficient platform, MPCLeague, for PPML in the Secure Outsourced Computation (SOC) setting using Secure Multi-party Computation (MPC) techniques. MPC, the holy-grail problem of secure distributed computing, enables a set of n mutually distrusting parties to perform joint computation on their private inputs in a way that no coalition of t parties can learn more information than the output (privacy) or affect the true output of the computation (correctness). While MPC, in general, has been a subject of extensive research, the area of MPC with a small number of parties has drawn popularity of late mainly due to its application to real-time scenarios, efficiency and simplicity. This thesis focuses on designing efficient MPC frameworks for 2, 3 and 4 parties, with at most one corruption and supports ring structures. At the heart of this thesis are four frameworks - ASTRA, SWIFT, Tetrad, ABY2.0 - catered to different settings. The practicality of our framework is argued through improvements in the benchmarking of widely used ML algorithms -- Linear Regression, Logistic Regression, Neural Networks, and Support Vector Machines. We propose two variants for each of our frameworks, with one variant aiming to minimise the execution time while the other focuses on the monetary cost. The concrete efficiency gains of our frameworks coupled with the stronger security guarantee of robustness make our platform an ideal choice for a real-time deployment of PPML techniques.

  匹配依据：MPC: secure multi party computation

  </details>

- **Mitigating Leakage from Data Dependent Communications in Decentralized Computing using Differential Privacy**
  2021-12-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2112.12411)
  Riad Ladjel, Nicolas Anciaux, Aurélien Bellet, Guillaume Scerri

  <details><summary>摘要 / Abstract</summary>

  Imagine a group of citizens willing to collectively contribute their personal data for the common good to produce socially useful information, resulting from data analytics or machine learning computations. Sharing raw personal data with a centralized server performing the computation could raise concerns about privacy and a perceived risk of mass surveillance. Instead, citizens may trust each other and their own devices to engage into a decentralized computation to collaboratively produce an aggregate data release to be shared. In the context of secure computing nodes exchanging messages over secure channels at runtime, a key security issue is to protect against external attackers observing the traffic, whose dependence on data may reveal personal information. Existing solutions are designed for the cloud setting, with the goal of hiding all properties of the underlying dataset, and do not address the specific privacy and efficiency challenges that arise in the above context. In this paper, we define a general execution model to control the data-dependence of communications in user-side decentralized computations, in which differential privacy guarantees for communication patterns in global execution plans can be analyzed by combining guarantees obtained on local clusters of nodes. We propose a set of algorithms which allow to trade-off between privacy, utility and efficiency. Our formal privacy guarantees leverage and extend recent results on privacy amplification by shuffling. We illustrate the usefulness of our proposal on two representative examples of decentralized execution plans with data-dependent communications.

  匹配依据：MPC: secure computing

  </details>

- **Long-term secure distributed storage using quantum key distribution network with third-party verification**
  2021-12-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2112.12292)
  Mikio Fujiwara, Ryo Nojima, Toyohiro Tsurumaru, Shiho Moriai, Masahiro Takeoka, Masahide Sasaki

  <details><summary>摘要 / Abstract</summary>

  The quantum key distribution network with Vernam&#x27;s One Time Pad encryption and secret sharing are powerful security tools to realize an information theoretically secure distributed storage system. In our previous work, a single-password-authenticated secret sharing scheme based on the QKD network and Shamir&#x27;s secret sharing was experimentally demonstrated; it confirmed ITS data transmission, storage, authentication, and integrity. To achieve data integrity, an ITS message authentication code tag is employed and a data owner of the secret sharing performs both the MAC tag generation and verification. However, for a scenario in which the data owner and end users are different entities, the above approach may not work since the data owner can cheat the end users. In this paper, we resolve this problem by proposing an ITS integrity protection scheme employing a third-party verification with time-stamp.

  匹配依据：MPC: secret sharing

  </details>

- **PUBA: Privacy-Preserving User-Data Bookkeeping and Analytics**
  2021-12-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1683)
  Valerie Fetzer, Marcel Keller, Sven Maier, Markus Raiber, Andy Rupp, Rebecca Schwerdt

  <details><summary>摘要 / Abstract</summary>

  In this paper we propose Privacy-preserving User-data Bookkeeping &amp; Analytics (PUBA), a building block destined to enable the implementation of business models (e.g., targeted advertising) and regulations (e.g., fraud detection) requiring user-data analysis in a privacy-preserving way. In PUBA, users keep an unlinkable but authenticated cryptographic logbook containing their historic data on their device. This logbook can only be updated by the operator while its content is not revealed. Users can take part in a privacy-preserving analytics computation, where it is ensured that their logbook is up-to-date and authentic while the potentially secret analytics function is verified to be privacy-friendly. Taking constrained devices into account, users may also outsource analytic computations (to a potentially malicious proxy not colluding with the operator). We model our novel building block in the Universal Composability framework and provide a practical protocol instantiation. To demonstrate the flexibility of PUBA, we sketch instantiations of privacy-preserving fraud detection and targeted advertising, although it could be used in many more scenarios, e.g. data analytics for multi-modal transportation systems. We implemented our bookkeeping protocols and an exemplary outsourced analytics computation based on logistic regression using the MP-SPDZ MPC framework. Performance evaluations using a smartphone as user device and more powerful hardware for operator and proxy suggest that PUBA for smaller logbooks can indeed be practical.

  匹配依据：MPC: mpc (context)

  </details>

- **Secure Publish-Process-Subscribe System for Dispersed Computing**
  2021-12-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1668)
  Weizhao Jin, Bhaskar Krishnamachari, Muhammad Naveed, Srivatsan Ravi, Eduard Sanou, Kwame-Lante Wright

  <details><summary>摘要 / Abstract</summary>

  Publish-subscribe protocols enable real-time multi-point-to-multi-point communications for many dispersed computing systems like Internet of Things (IoT) applications. Recent interest has focused on adding processing to such publish-subscribe protocols to enable computation over real-time streams such that the protocols can provide functionalities such as sensor fusion, compression, and other statistical analysis on raw sensor data. However, unlike pure publish-subscribe protocols, which can be easily deployed with end-to-end transport layer encryption, it is challenging to ensure security in such publish-process-subscribe protocols when the processing is carried out on an untrusted third party. In this work, we present XYZ, a secure publish-process-subscribe system that can preserve the confidentiality of computations and support multi-publisher-multi-subscriber settings. Within XYZ, we design two distinct schemes: the first using Yao&#x27;s garbled circuits (the GC-Based Scheme) and the second using homomorphic encryption with proxy re-encryption (the Proxy-HE Scheme). We build implementations of the two schemes as an integrated publish-process-subscribe system. We evaluate our system on several functions and also demonstrate real-world applications. The evaluation shows that the GC-Based Scheme can finish most tasks two orders of magnitude times faster than the Proxy-HE Scheme while Proxy-HE can still securely complete tasks within an acceptable time for most functions but with a different security assumption and a simpler system structure.

  匹配依据：MPC: garbled circuits

  </details>

- **A Survey on Perfectly-Secure Verifiable Secret-Sharing**
  2021-12-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2112.11393) · [IACR ePrint](https://eprint.iacr.org/2021/445)
  Anirudh Chandramouli, Ashish Choudhury, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  Verifiable Secret-Sharing (VSS) is a fundamental primitive in secure distributed computing. It is used as an important building block in several distributed computing tasks, such as Byzantine agreement and secure multi-party computation. VSS has been widely studied in various dimensions over the last three decades and several important results have been achieved related to the fault-tolerance, round-complexity and communication efficiency of VSS schemes. In this article, we consider VSS schemes with perfect security, tolerating computationally unbounded adversaries. We comprehensively survey the existing perfectly-secure VSS schemes in three different settings, namely synchronous, asynchronous and hybrid communication settings and provide the full details of each of the existing schemes in these settings. The aim of this survey is to provide a clear knowledge and foundation to researchers who are interested in knowing and extending the state-of-the-art perfectly-secure VSS schemes.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Cryptography from Pseudorandom Quantum States**
  2021-12-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2112.10020) · [IACR ePrint](https://eprint.iacr.org/2021/1663)
  Prabhanjan Ananth, Luowen Qian, Henry Yuen

  <details><summary>摘要 / Abstract</summary>

  Pseudorandom states, introduced by Ji, Liu and Song (Crypto&#x27;18), are efficiently-computable quantum states that are computationally indistinguishable from Haar-random states. One-way functions imply the existence of pseudorandom states, but Kretschmer (TQC&#x27;20) recently constructed an oracle relative to which there are no one-way functions but pseudorandom states still exist. Motivated by this, we study the intriguing possibility of basing interesting cryptographic tasks on pseudorandom states. We construct, assuming the existence of pseudorandom state generators that map a $λ$-bit seed to a $ω(\logλ)$-qubit state, (a) statistically binding and computationally hiding commitments and (b) pseudo one-time encryption schemes. A consequence of (a) is that pseudorandom states are sufficient to construct maliciously secure multiparty computation protocols in the dishonest majority setting. Our constructions are derived via a new notion called pseudorandom function-like states (PRFS), a generalization of pseudorandom states that parallels the classical notion of pseudorandom functions. Beyond the above two applications, we believe our notion can effectively replace pseudorandom functions in many other cryptographic applications.

  匹配依据：MPC: secure multiparty computation

  </details>

- **SecNDP: Secure Near-Data Processing with Untrusted Memory**
  2021-12-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1642)
  Wenjie Xiong, Liu Ke, Dimitrije Jankov, Michael Kounavis, Xiaochen Wang, Eric Northup, Jie Amy Yang, Bilge Acun, Carole-Jean Wu, Ping Tak Peter Tang, G. Edward Suh, Xuan Zhang, Hsien-Hsin S. Lee.

  <details><summary>摘要 / Abstract</summary>

  Today&#x27;s data-intensive applications increasingly suffer from significant performance bottlenecks due to the limited memory bandwidth of the classical von Neumann architecture. Near-Data Processing (NDP) has been proposed to perform computation near memory or data storage to reduce data movement for improving performance and energy consumption. However, the untrusted NDP processing units (PUs) bring in new threats to workloads that are private and sensitive, such as private database queries and private machine learning inferences. Meanwhile, most existing secure hardware designs do not consider off-chip components trustworthy. Once data leaving the processor, they must be protected, e.g., via block cipher encryption. Unfortunately, current encryption schemes do not support computation over encrypted data stored in memory or storage, hindering the adoption of NDP techniques for sensitive workloads. In this paper, we propose SecNDP, a lightweight encryption and verification scheme for untrusted NDP devices to perform computation over ciphertext and verify the correctness of linear operations. Our encryption scheme leverages arithmetic secret sharing in secure Multi-Party Computation (MPC) to support operations over ciphertext, and uses counter-mode encryption to reduce the decryption latency. The security of the scheme is formally proven. Compared with a non-NDP baseline, secure computation with SecNDP significantly reduces the memory bandwidth usage while providing security guarantees. We evaluate SecNDP for two workloads of distinct memory access patterns. In the setting of eight NDP units, we show a speedup up to 7.46x and energy savings of 18% over an unprotected non-NDP baseline, approaching the performance gain attained by native NDP without protection.Furthermore, SecNDP does not require any security assumption on NDP to hold, thus, using the same threat model as existing secure processors. SecNDP can be implemented without changing the NDP protocols and their inherent hardware design.

  匹配依据：MPC: secret sharing, secure computation, secure multi party computation

  </details>

- **Efficient Set Membership Proofs using MPC-in-the-Head**
  2021-12-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1656)
  Aarushi Goel, Matthew Green, Mathias Hall-Andersen, Gabriel Kaptchuk

  <details><summary>摘要 / Abstract</summary>

  Set membership proofs are an invaluable part of privacy preserving systems. These proofs allow a prover to demonstrate knowledge of a witness $w$ corresponding to a secret element $x$ of a public set, such that they jointly satisfy a given NP relation, {\em i.e.} $\mathcal{R}(w,x)=1$ and $x$ is a member of a public set $\{x_1, \ldots, x_\ell\}$. This allows the identity of the prover to remain hidden, eg. ring signatures and confidential transactions in cryptocurrencies. In this work, we develop a new technique for efficiently adding logarithmic-sized set membership proofs to any MPC-in-the-head based zero-knowledge protocol (Ishai et al. [STOC&#x27;07]). We integrate our technique into an open source implementation of the state-of-the-art, post quantum secure zero-knowledge protocol of Katz et al. [CCS&#x27;18]. We find that using our techniques to construct ring signatures results in signatures (based only on symmetric key primitives) that are between 5 and 10 times smaller than state-of-the-art techniques based on the same assumptions. We also show that our techniques can be used to efficiently construct post-quantum secure RingCT from only symmetric key primitives.

  匹配依据：MPC: mpc (context)

  </details>

- **A PKI-based Framework for Establishing Efficient MPC Channels**
  2021-12-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1627)
  Daniel Masny, Gaven Watson

  <details><summary>摘要 / Abstract</summary>

  The Transport Layer Security (TLS) protocol is a fundamental building block for ensuring security on Internet. It provides an easy to use framework for the purposes of establishing an authenticated and secure channel between two parties that have never physically met. Nevertheless, TLS only provides a simple cryptographic functionality compared to more advanced protocols such as protocols for secure multiparty computation (MPC). In this work, we provide a framework for efficiently establishing channels for MPC over the Internet. We focus on MPC protocols in the oblivious transfer (OT) hybrid model such that it is sufficient to establish OT correlations for such a channel. We revisit and combine different notions of UC security proposed in both the MPC and authenticated key exchange settings. Through this work, we show how an OT protocol can be composed with a secure authenticator to ensure the authenticity of messages sent during the OT. In addition, we adapt and analyse non-interactive OTs based on dense key encapsulation mechanisms (KEMs) in the random oracle model, where the first message, i.e. public key, can be reused. These KEMs can be instantiated based on CDH, RSA and LWE and after a performance and security evaluation, it turns out that the resulting OT protocols are very competitive with the state of the art and are able to leverage existing PKIs.

  匹配依据：MPC: oblivious transfer, secure multiparty computation

  </details>

- **Construction of Differentially Private Summaries over Fully Homomorphic Encryption**
  2021-12-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2112.08662)
  S. Ushiyama, T. Takahashi, M. Kudo, H. Yamana

  <details><summary>摘要 / Abstract</summary>

  Cloud computing has garnered attention as a platform of query processing systems. However, data privacy leakage is a critical problem. Chowdhury et al. proposed Crypt(epsilon), which executes differential privacy (DP) over encrypted data on two non-colluding semi-honest servers. Further, the DP index proposed by these authors summarizes a dataset to prevent information leakage while improving the performance. However, two problems persist: 1) the original data are decrypted to apply sorting via a garbled circuit, and 2) the added noise becomes large because the sorted data are partitioned with equal width, regardless of the data distribution. To solve these problems, we propose a new method called DP-summary that summarizes a dataset into differentially private data over a homomorphic encryption without decryption, thereby enhancing data security. Furthermore, our scheme adopts Li et al.&#x27;s data-aware and workload-aware (DAWA) algorithm for the encrypted data, thereby minimizing the noise caused by DP and reducing the errors of query responses. An experimental evaluation using torus fully homomorphic encryption (TFHE), a bit-wise fully homomorphic encryption library, confirms the applicability of the proposed method, which summarized eight 16-bit data in 12.5 h. We also confirmed that there was no accuracy degradation even after adopting TFHE along with the DAWA algorithm.

  匹配依据：MPC: garbled circuit

  </details>

- **CodedPaddedFL and CodedSecAgg: Straggler Mitigation and Secure Aggregation in Federated Learning**
  2021-12-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2112.08909)
  Reent Schlegel, Siddhartha Kumar, Eirik Rosnes, Alexandre Graell i Amat

  <details><summary>摘要 / Abstract</summary>

  We present two novel federated learning (FL) schemes that mitigate the effect of straggling devices by introducing redundancy on the devices&#x27; data across the network. Compared to other schemes in the literature, which deal with stragglers or device dropouts by ignoring their contribution, the proposed schemes do not suffer from the client drift problem. The first scheme, CodedPaddedFL, mitigates the effect of stragglers while retaining the privacy level of conventional FL. It combines one-time padding for user data privacy with gradient codes to yield straggler resiliency. The second scheme, CodedSecAgg, provides straggler resiliency and robustness against model inversion attacks and is based on Shamir&#x27;s secret sharing. We apply CodedPaddedFL and CodedSecAgg to a classification problem. For a scenario with 120 devices, CodedPaddedFL achieves a speed-up factor of 18 for an accuracy of 95% on the MNIST dataset compared to conventional FL. Furthermore, it yields similar performance in terms of latency compared to a recently proposed scheme by Prakash et al. without the shortcoming of additional leakage of private data. CodedSecAgg outperforms the state-of-the-art secure aggregation scheme LightSecAgg by a speed-up factor of 6.6-18.7 for the MNIST dataset for an accuracy of 95%.

  匹配依据：MPC: secret sharing

  </details>

- **Succinct Publicly-Certifiable Proofs (or: Can a Blockchain Verify a Designated-Verifier Proof?)**
  2021-12-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1618)
  Matteo Campanelli, Hamidreza Khoshakhlagh

  <details><summary>摘要 / Abstract</summary>

  We study zero-knowledge arguments where proofs are: of knowledge, short, publicly-verifiable and produced without interaction. While zkSNARKs satisfy these requirements, we build such proofs in a constrained theoretical setting: in the standard-model---i.e., without a random oracle---and without assuming public-verifiable SNARKs (or even NIZKs, for some of our constructions) or primitives currently known to imply them. We model and construct a new primitive, SPuC (Succinct Publicly-Certifiable System), where: a party can prove knowledge of a witness $w$ by publishing a proof $\pi_0$; the latter can then be certified non-interactively by a committee sharing a secret; any party in the system can now verify the proof through its certificates; the total communication complexity should be sublinear in $|w|$. We construct SPuCs generally from (leveled) Threshold FHE, homomorphic signatures and linear-only encryption, all instantiatable from lattices and thus plausibly quantum-resistant. We also construct them in the two-party case replacing TFHE with the simpler primitive of homomorphic secret-sharing. Our model has practical applications in blockchains and in other protocols where there exist committees sharing a secret and it is necessary for parties to prove knowledge of a solution to some puzzle. We show that one can construct a version of SPuCs with robust proactive security from similar assumptions. In a proactively secure model the committee reshares its secret from time to time. Such a model is robust if the committee members can prove they performed this resharing step correctly. Along the way to our goal we define and build Proactive Universal Thresholdizers, a proactive version of the Universal Thresholdizer defined in Boneh et al. [Crypto 2018].

  匹配依据：MPC: secret sharing

  </details>

- **Efficient Differentially Private Secure Aggregation for Federated Learning via Hardness of Learning with Errors**
  2021-12-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2112.06872)
  Timothy Stevens, Christian Skalka, Christelle Vincent, John Ring, Samuel Clark, Joseph Near

  <details><summary>摘要 / Abstract</summary>

  Federated machine learning leverages edge computing to develop models from network user data, but privacy in federated learning remains a major challenge. Techniques using differential privacy have been proposed to address this, but bring their own challenges -- many require a trusted third party or else add too much noise to produce useful models. Recent advances in \emph{secure aggregation} using multiparty computation eliminate the need for a third party, but are computationally expensive especially at scale. We present a new federated learning protocol that leverages a novel differentially private, malicious secure aggregation protocol based on techniques from Learning With Errors. Our protocol outperforms current state-of-the art techniques, and empirical results show that it scales to a large number of parties, with optimal accuracy for any differentially private federated learning scheme.

  匹配依据：MPC: multiparty computation

  </details>

- **Constructions For Several Few-weight Linear Codes And Their Applications**
  2021-12-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2112.06027)
  Canze Zhu, Qunying Liao

  <details><summary>摘要 / Abstract</summary>

  In this paper, for any odd prime $p$ and an integer $m\ge 3$, several classes of linear codes with $t$-weight $(t=3,5,7)$ are obtained based on some defining sets, and then their complete weight enumerators are determined explicitly by employing Gauss sums and quadratic character sums. Especially for $m = 3$, a class of MDS codes with parameters $[p,3,p-2]$ are obtained. Furthermore, some of these codes can be suitable for applications in secret sharing schemes and $s$-sum sets for any odd $s&gt;1$.

  匹配依据：MPC: secret sharing

  </details>

- **Linear complementary dual code-based Multi-secret sharing scheme**
  2021-12-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2112.05469)
  Haradhan Ghosh, Sanjit Bhowmick, Pramod Kumar Maurya, Satya Bagchi

  <details><summary>摘要 / Abstract</summary>

  Hiding a secret is needed in many situations. Secret sharing plays an important role in protecting information from getting lost, stolen, or destroyed and has been applicable in recent years. A secret sharing scheme is a cryptographic protocol in which a dealer divides the secret into several pieces of share and one share is given to each participant. To recover the secret, the dealer requires a subset of participants called access structure. In this paper, we present a multi-secret sharing scheme over a local ring based on linear complementary dual codes using Blakley&#x27;s method. We take a large secret space over a local ring that is greater than other code-based schemes and obtain a perfect and almost ideal scheme.

  匹配依据：MPC: secret sharing

  </details>

- **How to prove any NP statement jointly? Efficient Distributed-prover Zero-Knowledge Protocols**
  2021-12-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1599)
  Pankaj Dayama, Arpita Patra, Protik Paul, Nitin Singh, Dhinakaran Vinayagamurthy

  <details><summary>摘要 / Abstract</summary>

  Traditional zero-knowledge protocols have been studied and optimized for the setting where a single prover holds the complete witness and tries to convince a verifier about a predicate on the witness, without revealing any additional information to the verifier. In this work, we study the notion of distributed-prover zero knowledge (DPZK) for arbitrary predicates where the witness is shared among multiple mutually distrusting provers and they want to convince a verifier that their shares together satisfy the predicate. We make the following contributions to the notion of distributed proof generation: (i) we propose a new MPC-style security definition to capture the adversarial settings possible for different collusion models between the provers and the verifier, (ii) we discuss new efficiency parameters for distributed proof generation such as the number of rounds of interaction and the amount of communication among the provers, and (iii) we propose a compiler that realizes distributed proof generation from the zero-knowledge protocols in the Interactive Oracle Proofs (IOP) paradigm. Our compiler can be used to obtain DPZK from arbitrary IOP protocols, but the concrete efficiency overheads are substantial in general. To this end, we contribute (iv) a new zero-knowledge IOP $\textsf{Graphene}$ which can be compiled into an efficient DPZK protocol. The $(\mathsf{D} + 1)$-DPZK protocol $\text{D-Graphene}$, with $\mathsf{D}$ provers and one verifier, admits $O(N^{1/c})$ proof size with a communication complexity of $O(\mathsf{D}^2\cdot (N^{1-2/c} + N_s))$, where $N$ is the number of gates in the arithmetic circuit representing the predicate and $N_s$ is the number of wires that depends on inputs from two or more parties. Significantly, only the distributed proof generation in $\text{D-Graphene}$ requires interaction among the provers. $\text{D-Graphene}$ compares favourably with the DPZK protocols obtained from the state-of-art zero-knowledge protocols, even those not modelled as IOPs.

  匹配依据：MPC: mpc (context)

  </details>

- **Secure learning-based MPC via garbled circuit**
  2021-12-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2112.03654)
  K. Tjell, N. Schlüter, P. Binfet, M. Schulze Darup

  <details><summary>摘要 / Abstract</summary>

  Encrypted control seeks confidential controller evaluation in cloud-based or networked systems. Many existing approaches build on homomorphic encryption (HE) that allow simple mathematical operations to be carried out on encrypted data. Unfortunately, HE is computationally demanding and many control laws (in particular non-polynomial ones) cannot be efficiently implemented with this technology. We show in this paper that secure two-party computation using garbled circuits provides a powerful alternative to HE for encrypted control. More precisely, we present a novel scheme that allows to efficiently implement (non-polynomial) max-out neural networks with one hidden layer in a secure fashion. These networks are of special interest for control since they allow, in principle, to exactly describe piecewise affine control laws resulting from, e.g., linear model predictive control (MPC). However, exact fits require high-dimensional preactivations of the neurons. Fortunately, we illustrate that even low-dimensional learning-based approximations are sufficiently accurate for linear MPC. In addition, these approximations can be securely evaluated using garbled circuit in less than 100~ms for our numerical example. Hence, our approach opens new opportunities for applying encrypted control.

  匹配依据：MPC: garbled circuit, garbled circuits, secure two party computation

  </details>

- **Practical Asynchronous Distributed Key Generation**
  2021-12-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1591)
  Sourav Das, Thomas Yurek, Zhuolun Xiang, Andrew Miller, Lefteris Kokoris-Kogias, Ling Ren

  <details><summary>摘要 / Abstract</summary>

  Distributed Key Generation (DKG) is a technique to bootstrap threshold cryptosystems without a trusted third party and is a building block to decentralized protocols such as randomness beacons, threshold signatures, and general multiparty computation. Until recently, DKG protocols have assumed the synchronous model and thus are vulnerable when their underlying network assumptions do not hold. The recent advancements in asynchronous DKG protocols are insufficient as they either have poor efficiency or limited functionality, resulting in a lack of concrete implementations. In this paper, we present a simple and concretely efficient asynchronous DKG (ADKG) protocol. In a network of $n$ nodes, our ADKG protocol can tolerate up to $t&lt;n/3$ malicious nodes and have an expected $O(\kappa n^3)$ communication cost, where $\kappa$ is the security parameter. Our ADKG protocol produces a field element as the secret and is thus compatible with off-the-shelf threshold cryptosystems. We implement our ADKG protocol and evaluate it using a network of up to 128 nodes in geographically distributed AWS instances. Our evaluation shows that our protocol takes as low as 3 and 9.5 seconds to terminate for 32 and 64 nodes, respectively. Also, each node sends only 0.7 Megabytes and 2.9 Megabytes of data during the two experiments, respectively.

  匹配依据：MPC: multiparty computation

  </details>

- **On the Bottleneck Complexity of MPC with Correlated Randomness**
  2021-12-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1594)
  Claudio Orlandi, Divya Ravi, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  At ICALP 2018, Boyle et al. introduced the notion of the bottleneck complexity of a secure multi-party computation (MPC) protocol. This measures the maximum communication complexity of any one party in the protocol, aiming to improve load-balancing among the parties. In this work, we study the bottleneck complexity of MPC in the preprocessing model, where parties are given correlated randomness ahead of time. We present two constructions of bottleneck-efficient MPC protocols, whose bottleneck complexity is independent of the number of parties: 1. A protocol for computing abelian programs, based only on one-way functions. 2. A protocol for selection functions, based on any linearly homomorphic encryption scheme. Compared with previous bottleneck-efficient constructions, our protocols can be based on a wider range of assumptions, and avoid the use of fully homomorphic encryption.

  匹配依据：MPC: secure multi party computation

  </details>

- **Garbling, Stacked and Staggered: Faster k-out-of-n Garbled Function Evaluation**
  2021-12-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1590)
  David Heath, Vladimir Kolesnikov, Stanislav Peceny

  <details><summary>摘要 / Abstract</summary>

  Stacked Garbling (SGC) is a Garbled Circuit (GC) improvement that efficiently and securely evaluates programs with conditional branching. SGC reduces bandwidth consumption such that communication is proportional to the size of the single longest program execution path, rather than to the size of the entire program. Crucially, the parties expend increased computational effort compared to classic GC. Motivated by procuring a subset in a menu of computational services or tasks, we consider GC evaluation of k-out-of-n branches, whose indices are known (or eventually revealed) to the GC evaluator E. Our stack-and-stagger technique amortizes GC computation in this setting. We retain the communication advantage of SGC, while significantly improving computation and wall-clock time. Namely, each GC party garbles (or evaluates) the total of n branches, a significant improvement over the O(nk) garblings/evaluations needed by standard SGC. We present our construction as a garbling scheme. Our technique brings significant overall performance improvement in various settings, including those typically considered in the literature: e.g. on a 1Gbps LAN we evaluate 16-out-of-128 functions ~7.68x faster than standard stacked garbling.

  匹配依据：MPC: garbled circuit, garbling scheme

  </details>

- **ppSAT: Towards Two-Party Private SAT Solving**
  2021-12-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1584)
  Ning Luo, Samuel Judson, Timos Antonopoulos, Ruzica Piskac, Xiao Wang

  <details><summary>摘要 / Abstract</summary>

  We design and implement a privacy-preserving Boolean satisfiability (ppSAT) solver, which allows mutually distrustful parties to evaluate the conjunction of their input formulas while maintaining privacy. We first define a family of security guarantees reconcilable with the (known) exponential complexity of SAT solving, and then construct an oblivious variant of the classic DPLL algorithm which can be integrated with existing secure two-party computation (2PC) techniques. We further observe that most known SAT solving heuristics are unsuitable for 2PC, as they are highly data-dependent in order to minimize the number of exploration steps. Faced with how best to trade off between the number of steps and the cost of obliviously executing each one, we design three efficient oblivious heuristics, one deterministic and two randomized. As a result of this effort we are able to evaluate our ppSAT solver on small but practical instances arising from the haplotype inference problem in bioinformatics. We conclude by looking towards future directions for making ppSAT solving more practical, most especially the integration of conflict-driven clause learning (CDCL).

  匹配依据：MPC: secure two party computation

  </details>

- **Le Mans: Dynamic and Fluid MPC for Dishonest Majority**
  2021-12-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1579)
  Rahul Rachuri, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  Most MPC protocols require the set of parties to be active for the entire duration of the computation. Deploying MPC for use cases such as complex and resource-intensive scientific computations increases the barrier of entry for potential participants. The model of Fluid MPC (Crypto 2021) tackles this issue by giving parties the flexibility to participate in the protocol only when their resources are free. As such, the set of parties is dynamically changing over time. In this work, we extend Fluid MPC, which only considered an honest majority, to the setting where the majority of participants at any point in the computation may be corrupt. We do this by presenting variants of the SPDZ protocol, which support dynamic participants. Firstly, we describe a universal preprocessing for SPDZ, which allows a set of $n$ parties to compute some correlated randomness, such that later on, any subset of the parties can use this to take part in an online secure computation. We complement this with a Dynamic SPDZ online phase, designed to work with our universal preprocessing, as well as a protocol for securely realising the preprocessing. Our preprocessing protocol is designed to efficiently use pseudorandom correlation generators, thus, the parties&#x27; storage and communication costs can be almost independent of the function being evaluated. We then extend this to support a fluid online phase, where the set of parties can dynamically evolve during the online phase. Our protocol achieves maximal fluidity and security with abort, similarly to the previous, honest majority construction. Achieving this requires a careful design and techniques to guarantee a small state complexity, allowing us to switch between committees efficiently.

  匹配依据：MPC: secure computation

  </details>

- **Integral Attacks on Pyjamask-96 and Round-Reduced Pyjamask-128 (Full version)**
  2021-12-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1572)
  Jiamin Cui, Kai Hu, Qingju Wang, Meiqin Wang

  <details><summary>摘要 / Abstract</summary>

  In order to provide benefits in the areas of fully homomorphic encryption (FHE), multi-party computation (MPC), post-quantum signature schemes, or efficient masked implementations for side-channel resistance, reducing the number of multiplications has become a quite popular trend for the symmetric cryptographic primitive designs. With an aggressive design strategy exploiting the extremely simple and low-degree S-box and low number of rounds, Pyjamask, the fundamental block cipher of the AEAD with the same name, has the smallest number of AND gates per bit among all the existing block ciphers (except LowMC or Rasta which work on unconventional plaintext/key sizes). Thus, although the AEAD Pyjamask stuck at the second round of the NIST lightweight cryptography standardization process, the block cipher Pyjamask itself still attracts a lot of attention. Not very unexpectedly, the low degree and the low number of rounds are the biggest weakness of Pyjamask. At FSE 2020, Dobraunig et al. successfully mounted an algebraic and higher-order differential attack on full Pyjamask-96, one member of the Pyjamask block cipher family. However, the drawback of this attack is that it has to use the full codebook, which makes the attack less appealing. In this paper, we take integral attacks as our weapon, which are also sensitive to the low degree. Based on a new 11-round integral distinguisher found by state-of-the-art detection techniques, and combined with the relationship between round keys that reduces the involved keys, we give the key recovery attack on the full Pyjamask-96 without the full codebook for the first time. Further, the algebraic and higher-order differential technique does not work for Pyjamask-128, the other member of the Pyjamask block cipher family. To better understand the security margin of Pyjamask-128, we present the first third-party cryptanalysis on Pyjamask-128 up to 11 out of 14 rounds.

  匹配依据：MPC: multi party computation

  </details>

- **Differential Privacy in Privacy-Preserving Big Data and Learning: Challenge and Opportunity**
  2021-12-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2112.01704)
  Honglu Jiang, Yifeng Gao, S M Sarwar, Luis GarzaPerez, Mahmudul Robin

  <details><summary>摘要 / Abstract</summary>

  Differential privacy (DP) has become the de facto standard of privacy preservation due to its strong protection and sound mathematical foundation, which is widely adopted in different applications such as big data analysis, graph data process, machine learning, deep learning, and federated learning. Although DP has become an active and influential area, it is not the best remedy for all privacy problems in different scenarios. Moreover, there are also some misunderstanding, misuse, and great challenges of DP in specific applications. In this paper, we point out a series of limits and open challenges of corresponding research areas. Besides, we offer potentially new insights and avenues on combining differential privacy with other effective dimension reduction techniques and secure multiparty computing to clearly define various privacy models.

  匹配依据：MPC: secure multiparty computing

  </details>

- **Communication-Efficient Proactive MPC for Dynamic Groups with Dishonest Majorities**
  2021-12-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1564)
  Karim Eldefrawy, Tancrède Lepoint, Antonin Leroux

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) has recently been increasingly adopted to secure cryptographic keys in enterprises, cloud infrastructure, and cryptocurrency and blockchain-related settings such as wallets and exchanges. Using MPC in blockchains and other distributed systems highlights the need to consider dynamic settings. In such dynamic settings, parties, and potentially even parameters of underlying secret sharing and corruption tolerance thresholds of sub-protocols, may change over the lifetime of the protocol. In particular, stronger threat models -- in which \emph{mobile} adversaries control a changing set of parties (up to $t$ out of $n$ involved parties at any instant), and may eventually corrupt \emph{all $n$ parties} over the course of a protocol&#x27;s execution -- are becoming increasingly important for such real world deployments; secure protocols designed for such models are known as Proactive MPC (PMPC). In this work, we construct the first efficient PMPC protocol for \emph{dynamic} groups (where the set of parties changes over time) secure against a \emph{dishonest majority} of parties. Our PMPC protocol only requires $O(n^2)$ (amortized) communication per secret, compared to existing PMPC protocols that require $O(n^4)$ and only consider static groups with dishonest majorities. At the core of our PMPC protocol is a new efficient technique to perform multiplication of secret shared data (shared using a bivariate scheme) with $O(n \sqrt{n})$ communication with security against a dishonest majority without requiring pre-computation. We also develop a new efficient bivariate batched proactive secret sharing (PSS) protocol for dishonest majorities, which may be of independent interest. This protocol enables multiple dealers to contribute different secrets that are efficiently shared together in one batch; previous batched PSS schemes required all secrets to come from a single dealer.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **The Legendre Symbol and the Modulo-2 Operator in Symmetric Schemes over (F\_p)^n**
  2021-11-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1533)
  Lorenzo Grassi, Dmitry Khovratovich, Sondre Rønjom, Markus Schofnegger

  <details><summary>摘要 / Abstract</summary>

  Motivated by modern cryptographic use cases such as multi-party computation (MPC), homomorphic encryption (HE), and zero-knowledge (ZK) protocols, several symmetric schemes that are efficient in these scenarios have recently been proposed in the literature. Some of these schemes are instantiated with low-degree nonlinear functions, for example low-degree power maps (e.g., MiMC, HadesMiMC, Poseidon) or the Toffoli gate (e.g., Ciminion). Others (e.g., Rescue, Vision, Grendel) are instead instantiated via high-degree functions which are easy to evaluate in the target application. A recent example for the latter case is the hash function Grendel, whose nonlinear layer is constructed using the Legendre symbol. In this paper, we analyze high-degree functions such as the Legendre symbol or the modulo-2 operation as building blocks for the nonlinear layer of a cryptographic scheme over (F_p)^n. Our focus regards the security analysis rather than the efficiency in the mentioned use cases. For this purpose, we present several new invertible functions that make use of the Legendre symbol or of the modulo-2 operation. Even though these functions often provide strong statistical properties and ensure a high degree after a few rounds, the main problem regards their small number of possible outputs, that is, only three for the Legendre symbol and only two for the modulo-2 operation. By fixing them, it is possible to reduce the overall degree of the function significantly. We exploit this behavior by describing the first preimage attack on full Grendel, and we verify it in practice.

  匹配依据：MPC: multi party computation

  </details>

- **SIMC: ML Inference Secure Against Malicious Clients at Semi-Honest Cost**
  2021-11-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1538)
  Nishanth Chandran, Divya Gupta, Sai Lakshmi Bhavana Obbattu, Akash Shah

  <details><summary>摘要 / Abstract</summary>

  Secure inference allows a model owner (or, the server) and the input owner (or, the client) to perform inference on machine learning model without revealing their private information to each other. A large body of work has shown efficient cryptographic solutions to this problem through secure 2- party computation. However, they assume that both parties are semi-honest, i.e., follow the protocol specification. Recently, Lehmkuhl et al. showed that malicious clients can extract the whole model of the server using novel model-extraction attacks. To remedy the situation, they introduced the client-malicious threat model and built a secure inference system, MUSE, that provides security guarantees, even when the client is malicious. In this work, we design and build SIMC, a new cryptographic system for secure inference in the client malicious threat model. On secure inference benchmarks considered by MUSE, SIMC has 23 − 29× lesser communication and is up to 11.4× faster than MUSE. SIMC obtains these improvements using a novel protocol for non-linear activation functions (such as ReLU) that has &gt; 28× lesser communication and is up to 43× more performant than MUSE. In fact, SIMC&#x27;s performance beats the state-of-the-art semi-honest secure inference system! Finally, similar to MUSE, we show how to push the majority of the cryptographic cost of SIMC to an input independent preprocessing phase. While the cost of the online phase of this protocol, SIMC++, is same as that of MUSE, the overall improvements of SIMC translate to similar improvements to the preprocessing phase of MUSE.

  匹配依据：MPC: secure 2 party computation

  </details>

- **Route Discovery in Private Payment Channel Networks**
  2021-11-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1539)
  Zeta Avarikioti, Mahsa Bastankhah, Mohammad Ali Maddah-Ali, Krzysztof Pietrzak, Jakub Svoboda, Michelle Yeo

  <details><summary>摘要 / Abstract</summary>

  In this work, we are the first to explore route discovery in private channel networks. We first determine what ``ideal&quot; privacy for a routing protocol means in this setting. We observe that protocols achieving this strong privacy definition exist by leveraging (topology hiding) Multi-Party Computation but they are (inherently) inefficient as route discovery must involve the entire network. We then present protocols with weaker privacy guarantees but much better efficiency. In particular, route discovery typically only involves small fraction of the nodes but some information on the topology and balances -- beyond what is necessary for performing the transaction -- is leaked. The core idea is that both sender and receiver gossip a message which then slowly propagates through the network, and the moment any node in the network receives both messages, a path is found. In our first protocol the message is always sent to all neighbouring nodes with a delay proportional to the fees of that edge. In our second protocol the message is only sent to one neighbour chosen randomly with a probability proportional to its degree. While the first instantiation always finds the cheapest path, the second might not, but it involves a smaller fraction of the network. % We discuss some extensions like employing bilinear maps so the gossiped messages can be re-randomized, making them unlikeable and thus improving privacy. We also discuss some extensions to further improve privacy by employing bilinear maps. Simulations of our protocols on the Lightning network topology (for random transactions and uniform fees) show that our first protocol (which finds the cheapest path) typically involves around 12\% of the 6376 nodes, while the second only touches around 18 nodes $(&lt;0.3\%)$, and the cost of the path that is found is around twice the cost of the optimal one.

  匹配依据：MPC: multi party computation

  </details>

- **On the Download Rate of Homomorphic Secret Sharing**
  2021-11-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2111.10126) · [IACR ePrint](https://eprint.iacr.org/2021/1532)
  Ingerid Fosli, Yuval Ishai, Victor I. Kolobov, Mary Wootters

  <details><summary>摘要 / Abstract</summary>

  A homomorphic secret sharing (HSS) scheme is a secret sharing scheme that supports evaluating functions on shared secrets by means of a local mapping from input shares to output shares. We initiate the study of the download rate of HSS, namely, the achievable ratio between the length of the output shares and the output length when amortized over $\ell$ function evaluations. We obtain the following results. * In the case of linear information-theoretic HSS schemes for degree-$d$ multivariate polynomials, we characterize the optimal download rate in terms of the optimal minimal distance of a linear code with related parameters. We further show that for sufficiently large $\ell$ (polynomial in all problem parameters), the optimal rate can be realized using Shamir&#x27;s scheme, even with secrets over $\mathbb{F}_2$. * We present a general rate-amplification technique for HSS that improves the download rate at the cost of requiring more shares. As a corollary, we get high-rate variants of computationally secure HSS schemes and efficient private information retrieval protocols from the literature. * We show that, in some cases, one can beat the best download rate of linear HSS by allowing nonlinear output reconstruction and $2^{-Ω(\ell)}$ error probability.

  匹配依据：MPC: secret sharing

  </details>

- **Experimenting with Collaborative zk-SNARKs: Zero-Knowledge Proofs for Distributed Secrets**
  2021-11-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1530)
  Alex Ozdemir, Dan Boneh

  <details><summary>摘要 / Abstract</summary>

  A zk-SNARK is a powerful cryptographic primitive that provides a succinct and efficiently checkable argument that the prover has a witness to a public NP statement, without revealing the witness. However, in their native form, zk-SNARKs only apply to a secret witness held by a single party. In practice, a collection of parties often need to prove a statement where the secret witness is distributed or shared among them. We implement and experiment with *collaborative zk-SNARKs*: proofs over the secrets of multiple, mutually distrusting parties. We construct these by lifting conventional zk-SNARKs into secure protocols among $N$ provers to jointly produce a single proof over the distributed witness. We optimize the proof generation algorithm in pairing-based zk-SNARKs so that algebraic techniques for multiparty computation (MPC) yield efficient proof generation protocols. For some zk-SNARKs, optimization is more challenging. This suggests MPC &quot;friendliness&quot; as an additional criterion for evaluating zk-SNARKs. We implement three collaborative proofs and evaluate the concrete cost of proof generation. We find that over a 3Gb/s link, security against a malicious minority of provers can be achieved with *approximately the same runtime* as a single prover. Security against $N-1$ malicious provers requires only a $2\times$ slowdown. This efficiency is unusual since most computations slow down by orders of magnitude when securely distributed. This efficiency means that most applications that can tolerate the cost of a single-prover proof should also be able to tolerate the cost of a collaborative proof.

  匹配依据：MPC: multiparty computation

  </details>

- **Amortizing Rate-1 OT and Applications to PIR and PSI**
  2021-11-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1525)
  Melissa Chase, Sanjam Garg, Mohammad Hajiabadi, Jialin Li, Peihan Miao

  <details><summary>摘要 / Abstract</summary>

  Recent new constructions of rate-1 OT [Döttling, Garg, Ishai, Malavolta, Mour, and Ostrovsky, CRYPTO 2019] have brought this primitive under the spotlight and the techniques have led to new feasibility results for private-information retrieval, and homomorphic encryption for branching programs. The receiver communication of this construction consists of a quadratic (in the sender&#x27;s input size) number of group elements for a single instance of rate-1 OT. Recently [Garg, Hajiabadi, Ostrovsky, TCC 2020] improved the receiver communication to a linear number of group elements for a single string-OT. However, most applications of rate-1 OT require executing it multiple times, resulting in large communication costs for the receiver. In this work, we introduce a new technique for amortizing the cost of multiple rate-1 OTs. Specifically, based on standard pairing assumptions, we obtain a two-message rate-1 OT protocol for which the amortized cost per string-OT is asymptotically reduced to only four group elements. Our results lead to significant communication improvements in PSI and PIR, special cases of SFE for branching programs. - PIR: We obtain a rate-1 PIR scheme with client communication cost of $O(\lambda\cdot\log N)$ group elements for security parameter $\lambda$ and database size $N$. Notably, after a one-time setup (or one PIR instance), any following PIR instance only requires communication cost $O(\log N)$ number of group elements. - PSI with unbalanced inputs: We apply our techniques to private set intersection with unbalanced set sizes (where the receiver has a smaller set) and achieve receiver communication of $O((m+\lambda) \log N)$ group elements where $m, N$ are the sizes of the receiver and sender sets, respectively. Similarly, after a one-time setup (or one PSI instance), any following PSI instance only requires communication cost $O(m \cdot \log N)$ number of group elements. All previous sublinear-communication non-FHE based PSI protocols for the above unbalanced setting were also based on rate-1 OT, but incurred at least $O(\lambda^2 m \log N)$ group elements.

  匹配依据：MPC: private set intersection

  </details>

- **Practical Garbled RAM: GRAM with $O(\\log^2 n)$ Overhead**
  2021-11-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1519)
  David Heath, Vladimir Kolesnikov, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  Garbled RAM (GRAM) is a powerful technique introduced by Lu and Ostrovsky that equips Garbled Circuit (GC) with a sublinear cost RAM without adding rounds of interaction. While multiple GRAM constructions are known, none are suitable for practice, due to costs that have high constants and poor scaling. We present the first GRAM suitable for practice. For computational security parameter $\kappa$ and for a size-$n$ RAM that stores blocks of size $w = \Omega(\log^2 n)$ bits, our GRAM incurs amortized $O(w \cdot \log^2 n \cdot \kappa)$ communication and computation per access. We evaluate the concrete cost of our GRAM; our approach outperforms trivial linear-scan-based RAM for as few as $512$ $128$-bit elements.

  匹配依据：MPC: garbled circuit

  </details>

- **Post-Quantum Simulatable Extraction with Minimal Assumptions: Black-Box and Constant-Round**
  2021-11-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2111.08665) · [IACR ePrint](https://eprint.iacr.org/2021/1516)
  Nai-Hui Chia, Kai-Min Chung, Xiao Liang, Takashi Yamakawa

  <details><summary>摘要 / Abstract</summary>

  From the minimal assumption of post-quantum semi-honest oblivious transfers, we build the first $ε$-simulatable two-party computation (2PC) against quantum polynomial-time (QPT) adversaries that is both constant-round and black-box (for both the construction and security reduction). A recent work by Chia, Chung, Liu, and Yamakawa (FOCS&#x27;21) shows that post-quantum 2PC with standard simulation-based security is impossible in constant rounds, unless either $\mathbf{NP} \subseteq \mathbf{BQP}$ or relying on non-black-box simulation. The $ε$-simulatability we target is a relaxation of the standard simulation-based security that allows for an arbitrarily small noticeable simulation error $ε$. Moreover, when quantum communication is allowed, we can further weaken the assumption to post-quantum secure one-way functions (PQ-OWFs), while maintaining the constant-round and black-box property. Our techniques also yield the following set of constant-round and black-box two-party protocols secure against QPT adversaries, only assuming black-box access to PQ-OWFs: - extractable commitments for which the extractor is also an $ε$-simulator; - $ε$-zero-knowledge commit-and-prove whose commit stage is extractable with $ε$-simulation; - $ε$-simulatable coin-flipping; - $ε$-zero-knowledge arguments of knowledge for $\mathbf{NP}$ for which the knowledge extractor is also an $ε$-simulator; - $ε$-zero-knowledge arguments for $\mathbf{QMA}$. At the heart of the above results is a black-box extraction lemma showing how to efficiently extract secrets from QPT adversaries while disturbing their quantum state in a controllable manner, i.e., achieving $ε$-simulatability of the post-extraction state of the adversary.

  匹配依据：MPC: two party computation

  </details>

- **HOLMES: Efficient Distribution Testing for Secure Collaborative Learning**
  2021-11-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1517)
  Ian Chang, Katerina Sotiraki, Weikeng Chen, Murat Kantarcioglu, Raluca Ada Popa

  <details><summary>摘要 / Abstract</summary>

  Using secure multiparty computation (MPC), organizations which own sensitive data (e.g., in healthcare, finance or law enforcement) can train machine learning models over their joint dataset without revealing their data to each other. At the same time, secure computation restricts operations on the joint dataset, which impedes computation to assess its quality. Without such an assessment, deploying a jointly trained model is potentially illegal. Regulations, such as the European Union&#x27;s General Data Protection Regulation (GDPR), require organizations to be legally responsible for the errors, bias, or discrimination caused by their machine learning models. Hence, testing data quality emerges as an indispensable step in secure collaborative learning. However, performing distribution testing is prohibitively expensive using current techniques, as shown in our experiments. We present HOLMES, a protocol for performing distribution testing efficiently. In our experiments, compared with three non-trivial baselines, HOLMES achieves a speedup of more than 10x for classical distribution tests and up to 10^4x for multidimensional tests. The core of HOLMES is a hybrid protocol that integrates MPC with zero-knowledge proofs and a new ZK-friendly and naturally oblivious sketching algorithm for multidimensional tests, both with significantly lower computational complexity and concrete execution costs.

  匹配依据：MPC: secure computation, secure multiparty computation

  </details>

- **A Four-Party Quantum Secret-Sharing Scheme based on Grover's Search Algorithm**
  2021-11-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2111.08932)
  Deepa Rathi, Farhan Musanna, Sanjeev Kumar

  <details><summary>摘要 / Abstract</summary>

  The work presents an amalgam of quantum search algorithm (QSA) and quantum secret sharing (QSS). The proposed QSS scheme utilizes Grover&#x27;s three-particle quantum state. In this scheme, the dealer prepares an encoded state by encoding the classical information as a marked state and shares the states&#x27; qubits between three participants. The participants combine their qubits and find the marked state as a measurement result of the three-qubit state. The security analysis shows the scheme is stringent against malicious participants or eavesdroppers. In comparison to the existing schemes, our protocol fairs pretty well and has a high encoding capacity. The simulation analysis is done on the cloud platform IBM-QE thereby showing the practical feasibility of the scheme.

  匹配依据：MPC: secret sharing

  </details>

- **Device-Independent Oblivious Transfer from the Bounded-Quantum-Storage-Model and Computational Assumptions**
  2021-11-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2111.08595)
  Anne Broadbent, Peter Yuen

  <details><summary>摘要 / Abstract</summary>

  We present a device-independent protocol for oblivious transfer (DIOT) and analyze its security under the assumption that the receiver&#x27;s quantum storage is bounded during protocol execution and that the device behaves independently and identically in each round. We additionally require that, for each device component, the input corresponding to the choice of measurement basis, and the resulting output, is communicated only with the party holding that component. Our protocol is everlastingly secure and, compared to previous DIOT protocols, it is less strict about the non-communication assumptions that are typical from protocols that use Bell inequality violations; instead, the device-independence comes from a protocol for self-testing of a single (quantum) device which makes use of a post-quantum computational assumption.

  匹配依据：MPC: oblivious transfer

  </details>

- **Asymptotically secure All-or-nothing Quantum Oblivious Transfer**
  2021-11-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2111.08484)
  Ramij Rahaman

  <details><summary>摘要 / Abstract</summary>

  We present a device independently secure quantum scheme for p-threshold all-or-nothing oblivious transfer. Novelty of the scheme is that, its security does not depend -- unlike the usual case -- on any quantum bit commitment protocol, rather it depends on Hardy&#x27;s argument for two-qubit system. This scheme is shown to be unconditionally secure against any strategy allowed by quantum mechanics. By providing a secure scheme for all-or-nothing quantum oblivious transfer, we have answered a long standing open problem, other than the quantum key distribution, whether there is any two-party quantum cryptographic protocol, which is unconditionally secure.

  匹配依据：MPC: oblivious transfer

  </details>

- **VASA: Vector AES Instructions for Security Applications**
  2021-11-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1493)
  Jean-Pierre Münch, Thomas Schneider, Hossein Yalame

  <details><summary>摘要 / Abstract</summary>

  Due to standardization, AES is today’s most widely used block cipher. Its security is well-studied and hardware acceleration is available on a variety of platforms. Following the success of the Intel AES New Instructions (AES-NI), support for Vectorized AES (VAES) has been added in 2018 and already shown to be useful to accelerate many implementations of AES-based algorithms where the order of AES evaluations is fixed a priori. In our work, we focus on using VAES to accelerate the computation in secure multi-party computation protocols and applications. For some MPC building blocks, such as OT extension, the AES operations are independent and known a priori and hence can be easily parallelized, similar to the original paper on VAES by Drucker et al. (ITNG’19). We evaluate the performance impact of using VAES in the AES-CTR implementations used in Microsoft CrypTFlow2, and the EMP-OT library which we accelerate by up to 24%. The more complex case that we study for the first time in our paper are dependent AES calls that are not fixed yet in advance and hence cannot be parallelized manually. This is the case for garbling schemes. To get optimal efficiency from the hardware, enough independent calls need to be combined for each batch of AES executions. We identify such batches using a deferred execution technique paired with early execution to reduce non-locality issues and more static techniques using circuit depth and explicit gate independence. We present a performance and a modularity focused technique to compute the AES operations efficiently while also immediately using the results and preparing the inputs. Using these techniques, we achieve a performance improvement via VAES of up to 244% for the ABY framework and of up to 28% for the EMP-AGMPC framework. By implementing several garbling schemes from the literature using VAES acceleration, we obtain a 171% better performance for ABY.

  匹配依据：MPC: garbling schemes, secure multi party computation

  </details>

- **Interaction-Preserving Compilers for Secure Computation**
  2021-11-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1503)
  Nico Döttling, Vipul Goyal, Giulio Malavolta, Justin Raizes

  <details><summary>摘要 / Abstract</summary>

  In this work we consider the following question: What is the cost of security for multi-party protocols? Specifically, given an insecure protocol where parties exchange (in the worst case) $\Gamma$ bits in $N$ rounds, is it possible to design a secure protocol with communication complexity close to $\Gamma$ and $N$ rounds? We systematically study this problem in a variety of settings and we propose solutions based on the intractability of different cryptographic problems. For the case of two parties we design an interaction-preserving compiler where the number of bits exchanged in the secure protocol approaches $\Gamma$ and the number of rounds is exactly $N$, assuming the hardness of standard problems over lattices. For the more general multi-party case, we obtain the same result assuming either (i) an additional round of interaction or (ii) the existence of extractable witness encryption and succinct non-interactive arguments of knowledge. As a contribution of independent interest, we construct the first multi-key fully homomorphic encryption scheme with message-to-ciphertext ratio (i.e., rate) of $1 - o(1)$, assuming the hardness of the learning with errors (LWE) problem. We view our work as a support for the claim that, as far as interaction and communication are concerned, one does not need to pay a significant price for security in multi-party protocols.

  匹配依据：MPC: secure computation

  </details>

- **Extractors: Low Entropy Requirements Colliding With Non-Malleability**
  2021-11-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1480)
  Divesh Aggarwal, Eldon Chung, Maciej Obremski

  <details><summary>摘要 / Abstract</summary>

  Two-source extractors are deterministic functions that, given two independent weak sources of randomness, output a (close to) uniformly random string of bits. Cheraghchi and Guruswami (TCC 2015) introduced two-source non-malleable extractors that combine the properties of randomness extraction with tamper resilience. Two-source non-malleable extractors have since then attracted a lot of attention, and have very quickly become fundamental objects in cryptosystems involving communication channels that cannot be fully trusted. Various applications of two-source non-malleable extractors include in particular non-malleable codes, non-malleable commitments, non-malleable secret sharing, network extraction, and privacy amplification with tamperable memory. The best known constructions of two-source non-malleable extractors are due to Chattopadhyay, Goyal, and Li (STOC 2016), Li (STOC 2017), and Li (CCC 2019). All of these constructions require both sources to have min-entropy at least $0.99 n$, where $n$ is the bit-length of each source. In this work, we introduce collision-resistant randomness extractors. This allows us to design a compiler that, given a two-source non-malleable extractor, and a collision-resistant extractor, outputs a two-source non-malleable extractor that inherits the non-malleability property from the non-malleable extractor, and the entropy requirement from the collision-resistant extractor. Nested application of this compiler leads to a dramatic improvement of the state-of-the-art mentioned above. We obtain a construction of a two-source non-malleable extractor where one source is required to have min-entropy greater than $0.8n$, and the other source is required to have only $\text{polylog} (n)$ min-entropy. Moreover, the other parameters of our construction, i.e., the output length, and the error remain comparable to prior constructions.

  匹配依据：MPC: secret sharing

  </details>

- **Concurrent-Secure Two-Party Computation in Two Rounds from Subexponential LWE**
  2021-11-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1470)
  Saikrishna Badrinarayanan, Rex Fernando, Amit Sahai

  <details><summary>摘要 / Abstract</summary>

  Very recently, two works were able to construct two-round secure multi-party computation (MPC) protocols in the plain model, without setup, relying on the superpolynomial simulation framework of Pass [Pas03]. The first work [ABG+21] achieves this relying on subexponential non-interactive witness indistinguishable arguments, the subexponential SXDH assumption, and the existence of a special type of non-interactive non-malleable commitment. The second work [FJK21] additionally achieves concurrent security, and relies on subexponential quantum hardness of the learning-with-errors (LWE) problem, subexponential classical hardness of SXDH, the existence of a subexponentially-secure (classically-hard) indistinguishablity obfuscation (iO) scheme, and time-lock puzzles. This paper focuses on the assumptions necessary to construct secure computation protocols in two rounds without setup, focusing on the subcase of two-party functionalities. In this particular case, we show how to build a two-round, concurrent-secure, two-party computation (2PC) protocol based on a single, standard, post-quantum assumption, namely subexponential hardness of the learning-with-errors (LWE) problem. We note that our protocol is the first two-round concurrent-secure 2PC protocol that does not require the existence of a one-round non-malleable commitment (NMC). Instead, we are able to use the two-round NMCs of [KS17a], which is instantiable from subexponential LWE.

  匹配依据：MPC: secure computation, secure multi party computation, secure two party computation

  </details>

- **Circuit-based PSI for Covid-19 Risk Scoring**
  2021-11-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1475)
  Leonie Reichert, Marcel Pazelt, Björn Scheuermann

  <details><summary>摘要 / Abstract</summary>

  —Many solutions have been proposed to improve manual contact tracing for infectious diseases through automation. Privacy is crucial for the deployment of such a system as it greatly influences adoption. Approaches for digital contact tracing like Google Apple Exposure Notification (GAEN) protect the privacy of users by decentralizing risk scoring. But GAEN leaks information about diagnosed users as ephemeral pseudonyms are broadcast to everyone. To combat deanonymisation based on the time of encounter while providing extensive risk scoring functionality we propose to use a private set intersection (PSI) protocol based on garbled circuits. Using oblivious programmable pseudo random functions PSI (PPRF-PSI) , we implement our solution CERTAIN which leaks no information to querying users other than one risk score for each of the last 14 days representing their risk of infection. We implement payload inclusion for OPPRF-PSI and evaluate the efficiency and performance of different risk scoring mechanisms on an Android device

  匹配依据：MPC: garbled circuits, private set intersection

  </details>

- **3-Party Distributed ORAM from Oblivious Set Membership**
  2021-11-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1463)
  Brett Hemenway Falk, Daniel Noble, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  Distributed Oblivious RAM (DORAM) protocols allow a group of participants to obliviously access a secret-shared array at a secret-shared index, and DORAM is the key tool for secure multiparty computation (MPC) in the RAM model. In this work, we present a novel 3-party semi-honest DORAM protocol with O((κ + D) log N) communication per access, where N is the size of the memory, κ is a security parameter and D is the block size. Our protocol performs polylogarithmic computation and does not require homomorphic encryption. Under natural parameter choices, this is the most communication-efficient DORAM with these properties. To build this DORAM protocol, we first present an extremely efficient oblivious data structure for answering set membership queries. From this we build an oblivious hash table with asymptotically optimal memory usage and access cost and with negligible failure probability. We believe these are of independent interest.

  匹配依据：MPC: secure multiparty computation

  </details>

- **CryptoNite: Revealing the Pitfalls of End-to-End Private Inference at Scale**
  2021-11-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2111.02583)
  Karthik Garimella, Nandan Kumar Jha, Zahra Ghodsi, Siddharth Garg, Brandon Reagen

  <details><summary>摘要 / Abstract</summary>

  The privacy concerns of providing deep learning inference as a service have underscored the need for private inference (PI) protocols that protect users&#x27; data and the service provider&#x27;s model using cryptographic methods. Recently proposed PI protocols have achieved significant reductions in PI latency by moving the computationally heavy homomorphic encryption (HE) parts to an offline/pre-compute phase. Paired with recent optimizations that tailor networks for PI, these protocols have achieved performance levels that are tantalizingly close to being practical. In this paper, we conduct a rigorous end-to-end characterization of PI protocols and optimization techniques and find that the current understanding of PI performance is overly optimistic. Specifically, we find that offline storage costs of garbled circuits (GC), a key cryptographic protocol used in PI, on user/client devices are prohibitively high and force much of the expensive offline HE computation to the online phase, resulting in a 10-1000$\times$ increase to PI latency. We propose a modified PI protocol that significantly reduces client-side storage costs for a small increase in online latency. Evaluated end-to-end, the modified protocol outperforms current protocols by reducing the mean PI latency by $4\times$ for ResNet18 on TinyImageNet. We conclude with a discussion of several recently proposed PI optimizations in light of the findings and note many actually increase PI latency when evaluated from an end-to-end perspective.

  匹配依据：MPC: garbled circuits

  </details>

- **Towards Sparse Federated Analytics: Location Heatmaps under Distributed Differential Privacy with Secure Aggregation**
  2021-11-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2111.02356)
  Eugene Bagdasaryan, Peter Kairouz, Stefan Mellem, Adrià Gascón, Kallista Bonawitz, Deborah Estrin, Marco Gruteser

  <details><summary>摘要 / Abstract</summary>

  We design a scalable algorithm to privately generate location heatmaps over decentralized data from millions of user devices. It aims to ensure differential privacy before data becomes visible to a service provider while maintaining high data accuracy and minimizing resource consumption on users&#x27; devices. To achieve this, we revisit distributed differential privacy based on recent results in secure multiparty computation, and we design a scalable and adaptive distributed differential privacy approach for location analytics. Evaluation on public location datasets shows that this approach successfully generates metropolitan-scale heatmaps from millions of user samples with a worst-case client communication overhead that is significantly smaller than existing state-of-the-art private protocols of similar accuracy.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Privacy-Preserving Energy Storage Sharing with Blockchain and Secure Multi-Party Computation**
  2021-11-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2111.02005)
  Nan Wang, Sid Chi-Kin Chau, Yue Zhou

  <details><summary>摘要 / Abstract</summary>

  Energy storage provides an effective way of shifting temporal energy demands and supplies, which enables significant cost reduction under time-of-use energy pricing plans. Despite its promising benefits, the cost of present energy storage remains expensive, presenting a major obstacle to practical deployment. A more viable solution to improve the cost-effectiveness is by sharing energy storage, such as community sharing, cloud energy storage and peer-to-peer sharing. However, revealing private energy demand data to an external energy storage operator may compromise user privacy, and is susceptible to data misuses and breaches. In this paper, we explore a novel approach to support energy storage sharing with privacy protection, based on privacy-preserving blockchain and secure multi-party computation. We present an integrated solution to enable privacy-preserving energy storage sharing, such that energy storage service scheduling and cost-sharing can be attained without the knowledge of individual users&#x27; demands. It also supports auditing and verification by the grid operator via blockchain. Furthermore, our privacy-preserving solution can safeguard against a dishonest majority of users, who may collude in cheating, without requiring a trusted third-party. We implemented our solution as a smart contract on real-world Ethereum blockchain platform, and provide empirical evaluation in this paper.

  匹配依据：MPC: secure multi party computation

  </details>

- **Introducing a Framework to Enable Anonymous Secure Multi-Party Computation in Practice (Extended Version)**
  2021-11-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2111.02269)
  Malte Breuer, Ulrike Meyer, Susanne Wetzel

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation (SMPC) allows a set of parties to securely compute a functionality in a distributed fashion without the need for any trusted external party. Usually, it is assumed that the parties know each other and have already established authenticated channels among each other. However, in practice the parties sometimes must stay anonymous. In this paper, we conceptualize a framework that enables the repeated execution of an SMPC protocol for a given functionality such that the parties can keep their participation in the protocol executions private and at the same time be sure that only authorized parties may take part in a protocol execution. We identify the security properties that an implementation of our framework must meet and introduce a first implementation of the framework that achieves these properties.

  匹配依据：MPC: secure multi party computation

  </details>

- **How to Find New Characteristic-Dependent Linear Rank Inequalities using Secret Sharing**
  2021-10-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2111.00120)
  Victor Peña-Macias

  <details><summary>摘要 / Abstract</summary>

  Determining information ratios of access structures is an important problem in secret sharing. Information inequalities and linear rank inequalities play an important role for proving bounds. Characteristic-dependent linear rank inequalities are rank inequalities which are true over vector spaces with specific field characteristic. In this paper, using ideas of secret sharing, we show a theorem that produces characteristic-dependent linear rank inequalities. These inequalities can be used for getting lower bounds on information ratios in linear secret sharing.

  匹配依据：MPC: secret sharing

  </details>

- **A State-Separating Proof for Yao’s Garbling Scheme**
  2021-10-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1453)
  Chris Brzuska, Sabine Oechsner

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation enables mutually distrusting parties to compute a public function of their secret inputs. One of the main approaches for designing MPC protocols are garbled circuits whose core component is usually referred to as a garbling scheme. In this work, we revisit the security of Yao’s garbling scheme and provide a modular security proof which composes the security of multiple layer garblings to prove security of the full circuit garbling. We perform our security proof in the style of state-separating proofs (ASIACRYPT 2018).

  匹配依据：MPC: garbled circuits, garbling scheme, secure multiparty computation

  </details>

- **HD-cos Networks: Efficient Neural Architectures for Secure Multi-Party Computation**
  2021-10-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.15440)
  Wittawat Jitkrittum, Michal Lukasik, Ananda Theertha Suresh, Felix Yu, Gang Wang

  <details><summary>摘要 / Abstract</summary>

  Multi-party computation (MPC) is a branch of cryptography where multiple non-colluding parties execute a well designed protocol to securely compute a function. With the non-colluding party assumption, MPC has a cryptographic guarantee that the parties will not learn sensitive information from the computation process, making it an appealing framework for applications that involve privacy-sensitive user data. In this paper, we study training and inference of neural networks under the MPC setup. This is challenging because the elementary operations of neural networks such as the ReLU activation function and matrix-vector multiplications are very expensive to compute due to the added multi-party communication overhead. To address this, we propose the HD-cos network that uses 1) cosine as activation function, 2) the Hadamard-Diagonal transformation to replace the unstructured linear transformations. We show that both of the approaches enjoy strong theoretical motivations and efficient computation under the MPC setup. We demonstrate on multiple public datasets that HD-cos matches the quality of the more expensive baselines.

  匹配依据：MPC: multi party computation, secure multi party computation

  </details>

- **Masked LARk: Masked Learning, Aggregation and Reporting worKflow**
  2021-10-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.14794)
  Joseph J. Pfeiffer, Denis Charles, Davis Gilton, Young Hun Jung, Mehul Parsana, Erik Anderson

  <details><summary>摘要 / Abstract</summary>

  Today, many web advertising data flows involve passive cross-site tracking of users. Enabling such a mechanism through the usage of third party tracking cookies (3PC) exposes sensitive user data to a large number of parties, with little oversight on how that data can be used. Thus, most browsers are moving towards removal of 3PC in subsequent browser iterations. In order to substantially improve end-user privacy while allowing sites to continue to sustain their business through ad funding, new privacy-preserving primitives need to be introduced. In this paper, we discuss a new proposal, called Masked LARk, for aggregation of user engagement measurement and model training that prevents cross-site tracking, while remaining (a) flexible, for engineering development and maintenance, (b) secure, in the sense that cross-site tracking and tracing are blocked and (c) open for continued model development and training, allowing advertisers to serve relevant ads to interested users. We introduce a secure multi-party compute (MPC) protocol that utilizes &quot;helper&quot; parties to train models, so that once data leaves the browser, no downstream system can individually construct a complete picture of the user activity. For training, our key innovation is through the usage of masking, or the obfuscation of the true labels, while still allowing a gradient to be accurately computed in aggregate over a batch of data. Our protocol only utilizes light cryptography, at such a level that an interested yet inexperienced reader can understand the core algorithm. We develop helper endpoints that implement this system, and give example usage of training in PyTorch.

  匹配依据：MPC: 3pc (context)

  </details>

- **Improved Circuit-based PSI via Equality Preserving Compression**
  2021-10-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1440)
  Kyoohyung Han, Dukjae Moon, Yongha Son

  <details><summary>摘要 / Abstract</summary>

  Circuit-based private set intersection (circuit-PSI) enables two parties with input set $X$ and $Y$ to compute a function $f$ over the intersection set $X \cap Y$, without revealing any other information. State-of-the-art protocols for circuit-PSI commonly involves a procedure that securely checks whether two input strings are equal and outputs an additive share of the equality result. This procedure is typically performed by generic two party computation protocols, and its cost occupies quite large portion of the total cost of circuit-PSI. In this work, we propose {\textit{equality preserving compression}} (EPC) protocol that compresses the length of equality check targets while preserving equality using homomorphic encryption (HE) scheme, which is secure against the semi-honest adversary. This can be seamlessly applied to state-of-the-art circuit-PSI protocol frameworks. We demonstrate by implementation that our EPC provides $10-40\%$ speed-up for circuit-PSI with set size from $2^{16}$ to $2^{20}$, on LAN network. We believe that EPC protocol itself can be independent interest, which can be applied to other application than PSI.

  匹配依据：MPC: private set intersection, two party computation

  </details>

- **Quantum cryptographic resource distillation and entanglement**
  2021-10-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.13707)
  Minjin Choi, Soojoon Lee

  <details><summary>摘要 / Abstract</summary>

  We look into multipartite quantum states on which quantum cryptographic protocols including quantum key distribution and quantum secret sharing can be perfectly performed, and define the quantum cryptographic resource distillable rate as the asymptotic rate at which such multipartite state can be distilled from a given multipartite state. Investigating several relations between entanglement and the rate, we show that there exists a multipartite bound entangled state whose quantum cryptographic resource distillable rate is strictly positive, that is, there exists a multipartite entangled state which is not distillable, but can be useful for quantum cryptography such as quantum key distribution and quantum secret sharing.

  匹配依据：MPC: secret sharing

  </details>

- **Improved Zero-Knowledge Argument of Encrypted Extended Permutation**
  2021-10-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1430)
  Yi Liu, Qi Wang, Siu-Ming Yiu

  <details><summary>摘要 / Abstract</summary>

  Extended permutation (EP) is a generalized notion of the standard permutation. Unlike the one-to-one correspondence mapping of the standard permutation, EP allows to replicate or omit elements as many times as needed during the mapping. EP is useful in the area of secure multi-party computation (MPC), especially for the problem of private function evaluation (PFE). As a special class of MPC problems, PFE focuses on the scenario where a party holds a private circuit $C$ while all other parties hold their private inputs $x_1, \ldots, x_n$, respectively. The goal of PFE protocols is to securely compute the evaluation result $C(x_1, \ldots, x_n)$, while any other information beyond $C(x_1, \ldots, x_n)$ is hidden. EP here is introduced to describe the topological structure of the circuit $C$, and it is further used to support the evaluation of $C$ privately. For an actively secure PFE protocol, it is crucial to guarantee that the private circuit provider cannot deviate from the protocol to learn more information. Hence, we need to ensure that the private circuit provider correctly performs an EP. This seeks the help of the so-called \emph{zero-knowledge argument of encrypted extended permutation} protocol. In this paper, we provide an improvement of this protocol. Our new protocol can be instantiated to be non-interactive while the previous protocol should be interactive. Meanwhile, compared with the previous protocol, our protocol is significantly (\eg more than $3.4\times$) faster, and the communication cost is only around $24\%$ of that of the previous one.

  匹配依据：MPC: secure multi party computation

  </details>

- **How to Handle Invalid Queries for Malicious-Private Protocols Based on Homomorphic Encryption**
  2021-10-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1417)
  Koji Nuida

  <details><summary>摘要 / Abstract</summary>

  We consider a setting of two-party computation between a server and a client where every message received by the server is encrypted by a fully homomorphic encryption (FHE) scheme and its decryption key is held by the client only. Akavia and Vald (IACR ePrint Archive, 2021) revisited the privacy problem in such protocols against malicious servers and revealed (as opposed to a naive expectation) that under certain condition, a malicious server can recover the client&#x27;s input even if the underlying FHE scheme is IND-CPA secure. They also gave some sufficient conditions for the FHE scheme to ensure the privacy against malicious servers. However, their argument did not consider the possibility that a query from a malicious server to a client involves an invalid ciphertext. In this paper, we show, by giving a concrete example, that if such an invalid query is just rejected by the client, then the sufficient conditions in Akavia and Vald&#x27;s result do not in general ensure the privacy against malicious servers. We also propose another option to handle an invalid query in a way that the client returns a random ciphertext (without explicitly rejecting the query), and show that such a protocol is private against malicious servers if the underlying FHE scheme is IND-CPA secure, sanitizable (in the sense of Ducas and Stehl\&#x27;{e}, EUROCRYPT 2016), and circular secure.

  匹配依据：MPC: two party computation

  </details>

- **Extending the Tally-Hiding Ordinos System: Implementations for Borda, Hare-Niemeyer, Condorcet, and Instant-Runoff Voting**
  2021-10-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1420)
  Fabian Hertel, Nicolas Huber, Jonas Kittelberger, Ralf Kuesters, Julian Liedtke, Daniel Rausch

  <details><summary>摘要 / Abstract</summary>

  Modern electronic voting systems (e-voting systems) are designed to achieve a variety of security properties, such as verifiability, accountability, and vote privacy. Some of these systems aim at so-called tally-hiding: they compute the election result, according to some result function, like the winner of the election, without revealing any other information to any party. In particular, if desired, they neither reveal the full tally consisting of all (aggregated or even individual) votes nor parts of it, except for the election result, according to the result function. Tally-hiding systems offer many attractive features, such as strong privacy guarantees both for voters and for candidates, and protection against Italian attacks. The Ordinos system is a recent provably secure framework for accountable tally-hiding e-voting that extends Helios and can be instantiated for various election methods and election result functions. So far, practical instantiations and implementations for only rather simple result functions (e.g., computing the $k$ best candidates) and single/multi-vote elections have been developed for Ordinos. In this paper, we propose and implement several new Ordinos instantiations in order to support Borda voting, the Hare-Niemeyer method for proportional representation, multiple Condorcet methods, and Instant-Runoff Voting. Our instantiations, which are based on suitable secure multi-party computation (MPC) components, offer the first tally-hiding implementations for these voting methods. To evaluate the practicality of our MPC components and the resulting e-voting systems, we provide extensive benchmarks for all our implementations.

  匹配依据：MPC: secure multi party computation

  </details>

- **A General Framework of Homomorphic Encryption for Multiple Parties with Non-Interactive Key-Aggregation**
  2021-10-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1412)
  Hyesun Kwak, Dongwon Lee, Yongsoo Song, Sameer Wagh

  <details><summary>摘要 / Abstract</summary>

  Homomorphic Encryption (HE) is a useful primitive for secure computation, but it is not generally applicable when multiple parties are involved, as the authority is solely concentrated in a single party, the secret key owner. To solve this issue, several variants of HE have emerged in the context of multiparty setting, resulting in two major lines of work -- Multi-Party HE (MPHE) and Multi-Key HE (MKHE). In short, MPHEs tend to be more efficient, but all parties should be specified at the beginning to collaboratively generate a public key, and the access structure is fixed throughout the entire computation. On the other hand, MKHEs have relatively poor performance but provide better flexibility in that a new party can generate its own key and join the computation anytime. In this work, we propose a new HE primitive, called Multi-Group HE (MGHE). Stated informally, an MGHE scheme provides seamless integration between MPHE and MKHE, and has the best of both worlds. In an MGHE scheme, a group of parties jointly generates a public key for efficient single-key encryption and homomorphic operations similar to MPHE. However, it also supports computation on encrypted data under different keys, in the MKHE manner. We formalize the security and correctness notions for MGHE and discuss the relation with previous approaches. We also present a concrete instantiation of MGHE from the BFV scheme and provide a proof-of-concept implementation to demonstrate its performance. In particular, our MGHE construction has a useful property that the key generation is simply done by aggregating individual keys without any interaction between the parties, while all the existing MPHE constructions relied on multi-round key-generation protocols. Finally, we describe a method to design a general multi-party computation protocol from our MGHE scheme.

  匹配依据：MPC: multi party computation, secure computation

  </details>

- **PRECAD: Privacy-Preserving and Robust Federated Learning via Crypto-Aided Differential Privacy**
  2021-10-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.11578)
  Xiaolan Gu, Ming Li, Li Xiong

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) allows multiple participating clients to train machine learning models collaboratively by keeping their datasets local and only exchanging model updates. Existing FL protocol designs have been shown to be vulnerable to attacks that aim to compromise data privacy and/or model robustness. Recently proposed defenses focused on ensuring either privacy or robustness, but not both. In this paper, we develop a framework called PRECAD, which simultaneously achieves differential privacy (DP) and enhances robustness against model poisoning attacks with the help of cryptography. Using secure multi-party computation (MPC) techniques (e.g., secret sharing), noise is added to the model updates by the honest-but-curious server(s) (instead of each client) without revealing clients&#x27; inputs, which achieves the benefit of centralized DP in terms of providing a better privacy-utility tradeoff than local DP based solutions. Meanwhile, a crypto-aided secure validation protocol is designed to verify that the contribution of model update from each client is bounded without leaking privacy. We show analytically that the noise added to ensure DP also provides enhanced robustness against malicious model submissions. We experimentally demonstrate that our PRECAD framework achieves higher privacy-utility tradeoff and enhances robustness for the trained models.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Distributed Secret Sharing over a Public Channel from Correlated Random Variables**
  2021-10-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.10307)
  Remi A. Chou

  <details><summary>摘要 / Abstract</summary>

  We consider a secret-sharing model where a dealer distributes the shares of a secret among a set of participants with the constraint that only predetermined subsets of participants must be able to reconstruct the secret by pooling their shares. Our study generalizes Shamir&#x27;s secret-sharing model in three directions. First, we allow a joint design of the protocols for the creation of the shares and the distribution of the shares, instead of constraining the model to independent designs. Second, instead of assuming that the participants and the dealer have access to information-theoretically secure channels at no cost, we assume that they have access to a public channel and correlated randomness. Third, motivated by a wireless network setting where the correlated randomness is obtained from channel gain measurements, we explore a setting where the dealer is an entity made of multiple sub-dealers. Our main results are inner and outer regions for the achievable secret rates that the dealer and the participants can obtain in this model. To this end, we develop two new achievability techniques, a first one to successively handle reliability and security constraints in a distributed setting, and a second one to reduce a multi-dealer setting to multiple single-user dealer settings. Our results yield the capacity region for threshold access structures when the correlated randomness corresponds to pairwise secret keys shared between each sub-dealer and each participant, and the capacity for the all-or-nothing access structure in the presence of a single dealer and arbitrarily correlated randomness.

  匹配依据：MPC: secret sharing

  </details>

- **HIDE &amp; SEEK: Privacy-Preserving Rebalancing on Payment Channel Networks**
  2021-10-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.08848) · [IACR ePrint](https://eprint.iacr.org/2021/1401)
  Zeta Avarikioti, Krzysztof Pietrzak, Iosif Salem, Stefan Schmid, Samarth Tiwari, Michelle Yeo

  <details><summary>摘要 / Abstract</summary>

  Payment channels effectively move the transaction load off-chain thereby successfully addressing the inherent scalability problem most cryptocurrencies face. A major drawback of payment channels is the need to ``top up&#x27;&#x27; funds on-chain when a channel is depleted. Rebalancing was proposed to alleviate this issue, where parties with depleting channels move their funds along a cycle to replenish their channels off-chain. Protocols for rebalancing so far either introduce local solutions or compromise privacy. In this work, we present an opt-in rebalancing protocol that is both private and globally optimal, meaning our protocol maximizes the total amount of rebalanced funds. We study rebalancing from the framework of linear programming. To obtain full privacy guarantees, we leverage multi-party computation in solving the linear program, which is executed by selected participants to maintain efficiency. Finally, we efficiently decompose the rebalancing solution into incentive-compatible cycles which conserve user balances when executed atomically.

  匹配依据：MPC: multi party computation

  </details>

- **DE-RSTC: A rational secure two-party computation protocol based on direction entropy**
  2021-10-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.09160)
  Yuling Chen, Juan Ma, Xianmin Wang, Xinyu Zhang, Huiyu Zhou

  <details><summary>摘要 / Abstract</summary>

  Rational secure multi-party computation (RSMC) means two or more rational parties to complete a function on private inputs. In the process, the rational parties choose strategies to maximize utility, which will cause players to maliciously execute the protocol and undermine the fairness and correctness of the protocol. To solve this problem, we leverage game theory to propose the direction entropy-based solution. First, we utilize the direction vector of the direction entropy to examine the player&#x27;s strategy uncertainty and quantify its strategy from different dimensions. Specifically, when parties choose a cooperation strategy, the direction vector is positive, and the information transmitted is positive, conversely, it is negative information. Then, we provide mutual information to construct new utility functions for the players. What&#x27;s more, we measure the mutual information of players to appraise their strategies. Finally, we prove in detail the protocol we gave, and the result show that the fairness problem in rational secure two-party computation. We also prove that the proposed protocol reaches the Nash equilibrium. Furthermore, we conduct experiments using mutual information to construct utility, and the results show that the utility obtained when the player is honest will be higher.

  匹配依据：MPC: secure multi party computation, secure two party computation

  </details>

- **UC Secure Private Branching Program and Decision Tree Evaluation**
  2021-10-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1390)
  Keyu Ji, Bingsheng Zhang, Tianpei Lu, Lichun Li, Kui Ren

  <details><summary>摘要 / Abstract</summary>

  Branching program (BP) is a DAG-based non-uniform computational model for L/poly class. It has been widely used in formal verification, logic synthesis, and data analysis. As a special BP, a decision tree is a popular machine learning classifier for its effectiveness and simplicity. In this work, we propose a UC-secure efficient 3-party computation platform for outsourced branching program and/or decision tree evaluation. We construct a constant-round protocol and a linear-round protocol. In particular, the overall (online + offline) communication cost of our linear-round protocol is $O(d(\ell + \log m+\log n))$ and its round complexity is $2d-1$, where $m$ is the DAG size, $n$ is the number of features, $\ell$ is the feature length, and $d$ is the longest path length. To enable efficient oblivious hopping among the DAG nodes, we propose a lightweight $1$-out-of-$N$ shared OT protocol with logarithmic communication in both online and offline phase. This partial result may be of independent interest to some other cryptographic protocols. Our benchmark shows, compared with the state-of-the-arts, the proposed constant-round protocol is up to 10X faster in the WAN setting, while the proposed linear-round protocol is up to 15X faster in the LAN setting.

  匹配依据：MPC: 3 party computation

  </details>

- **The Privacy-preserving Padding Problem: Non-negative Mechanisms for Conservative Answers with Differential Privacy**
  2021-10-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.08177)
  Benjamin M. Case, James Honaker, Mahnush Movahedi

  <details><summary>摘要 / Abstract</summary>

  Differentially private noise mechanisms commonly use symmetric noise distributions. This is attractive both for achieving the differential privacy definition, and for unbiased expectations in the noised answers. However, there are contexts in which a noisy answer only has utility if it is conservative, that is, has known-signed error, which we call a padded answer. Seemingly, it is paradoxical to satisfy the DP definition with one-sided error, but we show how it is possible to bury the paradox into approximate DP&#x27;s delta parameter. We develop a few mechanisms for one-sided padding mechanisms that always give conservative answers, but still achieve approximate differential privacy. We show how these mechanisms can be applied in a few select areas including making the cardinalities of set intersections and unions revealed in Private Set Intersection protocols differential private and enabling multiparty computation protocols to compute on sparse data which has its exact sizes made differential private rather than performing a fully oblivious more expensive computation.

  匹配依据：MPC: multiparty computation, private set intersection

  </details>

- **MHz2k: MPC from HE over $\\mathbb{Z}\_{2^k}$ with New Packing, Simpler Reshare, and Better ZKP**
  2021-10-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1383)
  Jung Hee Cheon, Dongwoo Kim, Keewoo Lee

  <details><summary>摘要 / Abstract</summary>

  We propose a multi-party computation (MPC) protocol over $\mathbb{Z}_{2^k}$ secure against actively corrupted majority from somewhat homomorphic encryption. The main technical contributions are: (i) a new efficient packing method for $\mathbb{Z}_{2^k}$-messages in lattice-based somewhat homomorphic encryption schemes, (ii) a simpler reshare protocol for level-dependent packings, (iii) a more efficient zero-knowledge proof of plaintext knowledge on cyclotomic rings $\mathbb{Z}[X]/\Phi_M(X)$ with $M$ being a prime. Integrating them, our protocol shows from 2.2x upto 4.8x improvements in amortized communication costs compared to the previous best results. Our techniques not only improve the efficiency of MPC over $\mathbb{Z}_{2^k}$ considerably, but also provide a toolkit that can be leveraged when designing other cryptographic primitives over $\mathbb{Z}_{2^k}$.

  匹配依据：MPC: multi party computation

  </details>

- **zk-Fabric, a Polylithic Syntax Zero Knowledge Joint Proof System**
  2021-10-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.07449)
  Sheng Sun, Tong Wen

  <details><summary>摘要 / Abstract</summary>

  In this paper, we create a single-use and full syntax zero-knowledge proof system, a.k.a zk-Fabric. Comparing with zk-SNARKS and another variant zero-knowledge proofing system, zkBOO and it&#x27;s variant zkBOO++. We present multiple new approaches on how to use partitioned garbled circuits to achieve a joint zero-knowledge proof system, with the benefits of less overhead and full syntax verification. zk-Fabric based on partitioned garbled circuits has the advantage of being versatile and single-use, meaning it can be applied to arbitrary circuits with more comprehensive statements, and it can achieve the non-interactivity among all participants. One of the protocols proposed within is used for creating a new kind of partitioned garbled circuits to match the comprehensive Boolean logical expression with multiple variables, we use the term &quot;polythitic syntax&quot; to refer to the context-based multiple variables in a comprehensive statement. We also designed a joint zero knowledge proof protocol that uses partitioned garbled circuits

  匹配依据：MPC: garbled circuits

  </details>

- **Quantum communications infrastructure architecture: theoretical background, network structure and technologies. A review of recent studies from a European public infrastructure perspective**
  2021-10-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.06762)
  Adam M. Lewis, Petra F. Scudo

  <details><summary>摘要 / Abstract</summary>

  Progress in the development of techniques for the construction of multiuser quantum communications networks is reviewed in light of the plans for an EU quantum communications infrastructure (EU QCI). Quantum key distribution networks may be classified as trusted node; quantum repeater-entanglement-swapping based; point-to-multipoint based on passive beam splitters, active optical switchers or WDM; high dimensional-multipartite entanglement and flexible reconfigurable multipartite networks. Both satellite and terrestrial implementations are possible and ore both planned for EU QCI; their relative merits are discussed. Current technology falls short in several respects of what is required to address use cases well. Bit rates as a function of distance are currently limited by the characteristics of available devices and are an order of magnitude or more below the theoretical bounds. Non-ideal device behaviour can open loopholes for side-channel attacks. Limited range constrains network geometry. New techniques are being developed to overcome these problems. The more sophisticated schemes depend on ongoing advances in the generation and distribution of entanglement. Particularly promising are the measurement device independent protocol, which eliminates photon-detector related security weaknesses, and the twin-field protocol, which uses similar techniques to extend range, in principle even beyond previously accepted theoretical bounds. Agreement of keys between more than two users can be accomplished classically after pairwise quantum key exchange but direct quantum multipartite agreement using may offer advantages. The same applies to secret sharing. Practical quantum repeaters, to eliminate the need for trusted nodes, are closer to being realised due to recent progress in optical memories.

  匹配依据：MPC: secret sharing

  </details>

- **Phoenix: Secure Computation in an Unstable Network with Dropouts and Comebacks**
  2021-10-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1376)
  Ivan Damgård, Daniel Escudero, Antigoni Polychroniadou

  <details><summary>摘要 / Abstract</summary>

  We consider the task of designing secure computation protocols in an unstable network where honest parties can drop out at any time, according to a schedule provided by the adversary. This type of setting, where even honest parties are prone to failures, is more realistic than traditional models, and has therefore gained a lot of attention recently. Our model, Phoenix, enables a new approach to secure multiparty computation with dropouts, allowing parties to drop out and re-enter the computation on an adversarially-chosen schedule and without assuming that these parties receive the messages that were sent to them while being offline - features that are not available in the existing models of Sleepy MPC (Guo et al., CRYPTO &#x27;19), Fluid MPC (Choudhuri et al., CRYPTO &#x27;21 ) and YOSO (Gentry et al. CRYPTO &#x27;21). Phoenix does assume an upper bound on the number of rounds that an honest party can be off-line---otherwise protocols in this setting cannot guarantee termination within a bounded number of rounds; however, if one settles for a weaker notion, namely guaranteed output delivery only for honest parties who stay on-line long enough, this requirement is not necessary. In this work, we study the settings of perfect, statistical and computational security and design MPC protocols in each of these scenarios. We assume that the intersection of online-and-honest parties from one round to the next is at least $2t+1$, $t+1$ and $1$ respectively, where $t$ is the number of (actively) corrupt parties. We show the intersection requirements to be optimal. Our (positive) results are obtained in a way that may be of independent interest: we implement a traditional stable network on top of the unstable one, which allows us to plug in \emph{any} MPC protocol on top. This approach adds a necessary overhead to the round count of the protocols, which is related to the maximal number of rounds an honest party can be offline. We also present a novel, perfectly secure MPC protocol in the preprocessing model that avoids this overhead by following a more &quot;direct&quot; approach rather than first building a stable network and then using existing protocols. We introduce our network model in the UC-framework, show that the composition theorem still holds, and prove the security of our protocols within this setting.

  匹配依据：MPC: secure computation, secure multiparty computation

  </details>

- **Quasi-Cyclic Stern Proof of Knowledge**
  2021-10-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.05005)
  Loïc Bidoux, Philippe Gaborit, Mukul Kulkarni, Nicolas Sendrier

  <details><summary>摘要 / Abstract</summary>

  The ongoing NIST standardization process has shown that Proof of Knowledge (PoK) based signatures have become an important type of possible post-quantum signatures. Regarding code-based cryptography, the original approach for PoK based signatures is the Stern protocol which allows to prove the knowledge of a small weight vector solving a given instance of the Syndrome Decoding (SD) problem over F2. It features a soundness error equal to 2/3. This protocol was improved a few years later by Véron who proposed a variation of the scheme based on the General Syndrome Decoding (GSD) problem which leads to better results in term of communication. A few years later, the AGS protocol introduced a variation of the Véron protocol based on Quasi-Cyclic (QC) matrices. The AGS protocol permits to obtain an asymptotic soundness error of 1/2 and an improvement in term of communications. In the present paper, we introduce the Quasi-Cyclic Stern PoK which constitutes an adaptation of the AGS scheme in a SD context, as well as several new optimizations for code-based PoK. Our main optimization on the size of the signature can&#x27;t be applied to GSD based protocols such as AGS and therefore motivated the design of our new protocol. In addition, we also provide a special soundness proof that is compatible with the use of the Fiat-Shamir transform for 5-round protocols. This approach is valid for our protocol but also for the AGS protocol which was lacking such a proof. We compare our results with existing signatures including the recent code-based signatures based on PoK leveraging the MPC in the head paradigm. In practice, our new protocol is as fast as AGS while reducing its associated signature length by 20%. As a consequence, it constitutes an interesting trade-off between signature length and execution time for the design of a code-based signature relying only on the difficulty of the SD problem.

  匹配依据：MPC: mpc (context)

  </details>

- **Function-private Conditional Disclosure of Secrets and Multi-evaluation Threshold Distributed Point Functions**
  2021-10-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.04293)
  Nolan Miranda, Foo Yee Yeo, Vipin Singh Sehrawat

  <details><summary>摘要 / Abstract</summary>

  Conditional disclosure of secrets (CDS) allows multiple parties to reveal a secret to a third party if and only if some pre-decided condition is satisfied. In this work, we bolster the privacy guarantees of CDS by introducing function-private CDS wherein the pre-decided condition is never revealed to the third party. We also derive a function secret sharing scheme from our function-private CDS solution. The second problem that we consider concerns threshold distributed point functions, which allow one to split a point function such that at least a threshold number of shares are required to evaluate it at any given input. We consider a setting wherein a point function is split among a set of parties such that multiple evaluations do not leak non-negligible information about it. Finally, we present a provably optimal procedure to perform threshold function secret sharing of any polynomial in a finite field.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Coded Mobile Edge Computing for Low-Latency Distributed Inference**
  2021-10-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.03545)
  Reent Schlegel, Siddhartha Kumar, Eirik Rosnes, Alexandre Graell i Amat

  <details><summary>摘要 / Abstract</summary>

  We consider a mobile edge computing scenario where a number of devices want to perform a linear inference $\boldsymbol{W}\boldsymbol{x}$ on some local data $\boldsymbol{x}$ given a network-side matrix $\boldsymbol{W}$. The computation is performed at the network edge over a number of edge servers. We propose a coding scheme that provides information-theoretic privacy against $z$ colluding (honest-but-curious) edge servers, while minimizing the overall latency\textemdash comprising upload, computation, download, and decoding latency\textemdash in the presence of straggling servers. The proposed scheme exploits Shamir&#x27;s secret sharing to yield data privacy and straggler mitigation, combined with replication to provide spatial diversity for the download. We also propose two variants of the scheme that further reduce latency. For a considered scenario with $9$ edge servers, the proposed scheme reduces the latency by $8\%$ compared to the nonprivate scheme recently introduced by Zhang and Simeone, while providing privacy against an honest-but-curious edge server.

  匹配依据：MPC: secret sharing

  </details>

- **Optical secret sharing with cascaded metasurface holography**
  2021-10-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.03265)
  Philip Georgi, Qunshuo Wei, Basudeb Sain, Christian Schlickriede, Yongtian Wang, Lingling Huang, Thomas Zentgraf

  <details><summary>摘要 / Abstract</summary>

  Secret sharing is a well-established cryptographic primitive for storing highly sensitive information like encryption keys for encoded data. It describes the problem of splitting a secret into different shares, without revealing any information about the secret to its shareholders. Here, we demonstrate an all-optical solution for secret sharing based on metasurface holography. In our concept, metasurface holograms are used as spatially separable shares that carry an encrypted message in form of a holographic image. Two of these shares can be recombined by bringing them close together. Light passing through this stack of metasurfaces accumulates the phase shift of both holograms and can optically reconstruct the secret with high fidelity. On the other hand, the holograms generated by the single metasurfaces can be used for identifying each shareholder. Furthermore, we demonstrate that the inherent translational alignment sensitivity between the two stacked metasurface holograms can be used for spatial multiplexing, which can be further extended to realize optical rulers.

  匹配依据：MPC: secret sharing

  </details>

- **Neural Networks, Inside Out: Solving for Inputs Given Parameters (A Preliminary Investigation)**
  2021-10-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.03649)
  Mohammad Sadeq Dousti

  <details><summary>摘要 / Abstract</summary>

  Artificial neural network (ANN) is a supervised learning algorithm, where parameters are learned by several back-and-forth iterations of passing the inputs through the network, comparing the output with the expected labels, and correcting the parameters. Inspired by a recent work of Boer and Kramer (2020), we investigate a different problem: Suppose an observer can view how the ANN parameters evolve over many iterations, but the dataset is oblivious to him. For instance, this can be an adversary eavesdropping on a multi-party computation of an ANN parameters (where intermediate parameters are leaked). Can he form a system of equations, and solve it to recover the dataset?

  匹配依据：MPC: multi party computation

  </details>

- **Secure Byzantine-Robust Distributed Learning via Clustering**
  2021-10-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.02940)
  Raj Kiriti Velicheti, Derek Xia, Oluwasanmi Koyejo

  <details><summary>摘要 / Abstract</summary>

  Federated learning systems that jointly preserve Byzantine robustness and privacy have remained an open problem. Robust aggregation, the standard defense for Byzantine attacks, generally requires server access to individual updates or nonlinear computation -- thus is incompatible with privacy-preserving methods such as secure aggregation via multiparty computation. To this end, we propose SHARE (Secure Hierarchical Robust Aggregation), a distributed learning framework designed to cryptographically preserve client update privacy and robustness to Byzantine adversaries simultaneously. The key idea is to incorporate secure averaging among randomly clustered clients before filtering malicious updates through robust aggregation. Experiments show that SHARE has similar robustness guarantees as existing techniques while enhancing privacy.

  匹配依据：MPC: multiparty computation

  </details>

- **Secure Multiparty Computation in the Bounded Storage Model**
  2021-10-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1327)
  Jiahui Liu, Satyanarayana Vusirikala

  <details><summary>摘要 / Abstract</summary>

  Most cryptography is based on assumptions such as factoring and discrete log, which assume an adversary has bounded computational power. With the recent development in quantum computing as well as concern with everlasting security, there is an interest in coming up with information-theoretic constructions in the bounded storage model. In this model, an adversary is computationally unbounded but has lim- ited space. Past works have constructed schemes such as key exchange and bit commitment in this model. In this work, we expand the function- alities further by building a semi-honest MPC protocol in the bounded storage model. We use the hardness of the parity learning problem (recently shown by Ran Raz (FOCS 16) without any cryptographic assump- tions) to prove the security of our construction, following the work by Guan and Zhandry (EUROCRYPT 19).

  匹配依据：MPC: secure multiparty computation

  </details>

- **Distributed Privacy-Preserving Electric Vehicle Charging Control Based on Secret Sharing**
  2021-10-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.02280)
  Xiang Huo, Mingxi Liu

  <details><summary>摘要 / Abstract</summary>

  Cooperative electric vehicle (EV) charging control has emerged as a key component in grid-edge resource (GER) management. However, customers&#x27; privacy remains a major barrier to large-scale implementation of EV charging control. In this paper, we develop a distributed privacy-preserving EV charging control protocol based on secret sharing (SS) that 1) achieves scalability over EV population size; 2) enjoys higher computation efficiency compared to homomorphic encryption (HE) based methods; and 3) secures the privacy of the participating EVs against honest-but-curious adversaries and external eavesdroppers. The cooperative EV charging control is formulated to achieve overnight valley-filling and framed into the projected gradient algorithm (PGA) structure as a distributed optimization problem. SS is integrated into PGA to achieve secure updates of both primal and dual variables. Theoretical security analyses and simulations in a residential area are conducted to prove the privacy preservation guarantee as well as the efficacy and efficiency of the proposed privacy preservation method. Broadly, the proposed method can be readily extended to various GER control applications.

  匹配依据：MPC: secret sharing

  </details>

- **LQP: The Dynamic Logic of Quantum Information**
  2021-10-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.01361)
  Alexandru Baltag, Sonja Smets

  <details><summary>摘要 / Abstract</summary>

  The main contribution of this paper is the introduction of a dynamic logic formalism for reasoning about information flow in composite quantum systems. This builds on our previous work on a complete quantum dynamic logic for single systems. Here we extend that work to a sound (but not necessarily complete) logic for composite systems, which brings together ideas from the quantum logic tradition with concepts from (dynamic) modal logic and from quantum computation. This Logic of Quantum Programs (LQP) is capable of expressing important features of quantum measurements and unitary evolutions of multi-partite states, as well as giving logical characterisations to various forms of entanglement (for example, the Bell states, the GHZ states etc.). We present a finitary syntax, a relational semantics and a sound proof system for this logic. As applications, we use our system to give formal correctness proofs for the Teleportation protocol and for a standard Quantum Secret Sharing protocol; a whole range of other quantum circuits and programs, including other well-known protocols (for example, superdense coding, entanglement swapping, logic-gate teleportation etc.), can be similarly verified using our logic.

  匹配依据：MPC: secret sharing

  </details>

- **A Lightweight, Anonymous and Confidential Genomic Computing for Industrial Scale Deployment**
  2021-10-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.01390)
  Huafei Zhu

  <details><summary>摘要 / Abstract</summary>

  This paper studies anonymous and confidential genomic case and control computing within the federated framework leveraging SPDZ. Our contribution mainly comprises the following three-fold: \begin{itemize} \item In the first fold, an efficient construction of Beaver triple generators (BTGs) formalized in the 3-party computation leveraging multiplicatively homomorphic key management protocols (mHKMs) is presented and analysed. Interestingly, we are able to show the equivalence between BTGs and mHKMs. We then propose a lightweight construction of BTGs, and show that our construction is secure against semi-honest adversary if the underlying multiplicatively homomorphic encryption is semantically secure. \item In the second fold, a decoupling model for SPDZ with explicit separation of BTGs from MPC servers (MPCs) is introduced and formalized, where BTGs aim to generate the Beaver triples while MPCs to process the input data. A new notion, which we call blind triple dispensation protocol, is then introduced for securely dispensing the generated Beaver triples, and constructed from mHKMs. We demonstrate the power of mHKMs by showing that it is a useful notion not only for generating Beaver triples but also for securely dispensing triples as well. \item In the third-fold, a lightweight genomic case and control computing model is proposed, which reaches the anonymity and confidentiality simultaneously. An efficient truncation algorithm leveraging the depicted BTGs above is then proposed by eliminating computational cost heavy PRandBitL() and PRandInt() protocols involved in the state-of-the-art solutions and thus largely benefits us computing residual vectors for industrial scale deployment.

  匹配依据：MPC: 3 party computation

  </details>

- **Enhancing Cold Wallet Security with Native Multi-Signature schemes in Centralized Exchanges**
  2021-10-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2110.00274)
  Shahriar Ebrahimi, Parisa Hasanizadeh, Seyed Mohammad Aghamirmohammadali, Amirali Akbari

  <details><summary>摘要 / Abstract</summary>

  Currently, one of the most widely used protocols to secure cryptocurrency assets in centralized exchanges is categorizing wallets into cold and hot. While cold wallets hold user deposits, hot} wallets are responsible for addressing withdrawal requests. However, this method has some shortcomings such as: 1) availability of private keys in at least one cold device, and~2) exposure of all private keys to one trusted cold wallet admin. To overcome such issues, we design a new protocol for managing cold wallet assets by employing native multi-signature schemes. The proposed cold wallet system, involves at least two distinct devices and their corresponding admins for both wallet creation and signature generation. The method ensures that no final private key is stored on any device. To this end, no individual authority can spend from exchange assets. Moreover, we provide details regarding practical implementation of the proposed method and compare it against state-of-the-art. Furthermore, we extend the application of the proposed method to an scalable scenario where users are directly involved in wallet generation and signing process of cold wallets in an MPC manner.

  匹配依据：MPC: mpc (context)

  </details>

- **m-Stability: Threshold Security Meets Transferable Utility**
  2021-09-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1317)
  Osman Biçer, Burcu Yıldız, Alptekin Küpçü

  <details><summary>摘要 / Abstract</summary>

  Use of game theory and mechanism design in cloud security is a well-studied topic. When applicable, it has the advantages of being efficient and simple compared to cryptography alone. Most analyses consider two-party settings, or multi-party settings where coalitions are not allowed. However, many cloud security problems that we face are in the multi-party setting and the involved parties can almost freely collaborate with each other. To formalize the study of disincentivizing coalitions from deviating strategies, a well-known definition named k-resiliency has been proposed by Abraham et al. (ACM PODC &#x27;06). Since its proposal, k-resiliency and related definitions are used extensively for mechanism design. However, in this work we observe the shortcoming of k-resiliency. That is, although this definition is secure, it is too strict to use for many cases and rule out secure mechanisms as insecure. To overcome this issue, we propose a new definition named l-repellence against the presence of a single coalition to replace k-resiliency. Our definition incorporates transferable utility in game theory as it is realistic in many distributed and multi-party computing settings. We also propose m-stability definition against the presence of multiple coalitions, which is inspired by threshold security in cryptography. We then show the advantages of our novel definitions on three mechanisms, none of which were previously analyzed against coalitions: incentivized cloud computation, forwarding data packages in ad hoc networks, and connectivity in ad hoc networks. Regarding the former, our concepts improve the proposal by Küpçü (IEEE TDSC &#x27;17), by ensuring a coalition-proof mechanism.

  匹配依据：MPC: multi party computing

  </details>

- **Maliciously-Secure MrNISC in the Plain Model**
  2021-09-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1319)
  Rex Fernando, Aayush Jain, Ilan Komargodski

  <details><summary>摘要 / Abstract</summary>

  A recent work of Benhamouda and Lin (TCC~&#x27;20) identified a dream version of secure multiparty computation (MPC), termed **Multiparty reusable Non-Interactive Secure Computation** (MrNISC), that combines at the same time several fundamental aspects of secure computation with standard simulation security into one primitive: round-optimality, succinctness, concurrency, and adaptivity. In more detail, MrNISC is essentially a two-round MPC protocol where the first round of messages serves as a reusable commitment to the private inputs of participating parties. Using these commitments, any subset of parties can later compute any function of their choice on their respective inputs by broadcasting one message each. Anyone who sees these parties&#x27; commitments and evaluation messages (even an outside observer) can learn the function output and nothing else. Importantly, the input commitments can be computed without knowing anything about other participating parties (neither their identities nor their number) and they are reusable across any number of computations. By now, there are several known MrNISC protocols from either (bilinear) group-based assumptions or from LWE. They all satisfy semi-malicious security (in the plain model) and require trusted setup assumptions in order to get malicious security. We are interested in maliciously secure MrNISC protocols **in the plain model, without trusted setup**. Since the standard notion of polynomial simulation is un-achievable in less than four rounds, we focus on MrNISC with **super-polynomial**-time simulation (SPS). Our main result is the first maliciously secure SPS MrNISC in the plain model. The result is obtained by generically compiling any semi-malicious MrNISC and the security of our compiler relies on several well-founded assumptions, including an indistinguishability obfuscator and a time-lock puzzle (all of which need to be sub-exponentially hard). As a special case we also obtain the first 2-round maliciously secure SPS MPC based on well-founded assumptions. This MPC is also concurrently self-composable and its first message is short (i.e., its size is independent of the number of the participating parties) and reusable throughout any number of computations.

  匹配依据：MPC: secure computation, secure multiparty computation

  </details>

- **Secure Multi-Party Computation based Privacy Preserving Data Analysis in Healthcare IoT Systems**
  2021-09-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2109.14334)
  Kevser Şahinbaş, Ferhat Ozgur Catak

  <details><summary>摘要 / Abstract</summary>

  Recently, many innovations have been experienced in healthcare by rapidly growing Internet-of-Things (IoT) technology that provides significant developments and facilities in the health sector and improves daily human life. The IoT bridges people, information technology and speed up shopping. For these reasons, IoT technology has started to be used on a large scale. Thanks to the use of IoT technology in health services, chronic disease monitoring, health monitoring, rapid intervention, early diagnosis and treatment, etc. facilitates the delivery of health services. However, the data transferred to the digital environment pose a threat of privacy leakage. Unauthorized persons have used them, and there have been malicious attacks on the health and privacy of individuals. In this study, it is aimed to propose a model to handle the privacy problems based on federated learning. Besides, we apply secure multi party computation. Our proposed model presents an extensive privacy and data analysis and achieve high performance.

  匹配依据：MPC: secure multi party computation

  </details>

- **LightSecAgg: a Lightweight and Versatile Design for Secure Aggregation in Federated Learning**
  2021-09-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2109.14236)
  Jinhyun So, Chaoyang He, Chien-Sheng Yang, Songze Li, Qian Yu, Ramy E. Ali, Basak Guler, Salman Avestimehr

  <details><summary>摘要 / Abstract</summary>

  Secure model aggregation is a key component of federated learning (FL) that aims at protecting the privacy of each user&#x27;s individual model while allowing for their global aggregation. It can be applied to any aggregation-based FL approach for training a global or personalized model. Model aggregation needs to also be resilient against likely user dropouts in FL systems, making its design substantially more complex. State-of-the-art secure aggregation protocols rely on secret sharing of the random-seeds used for mask generations at the users to enable the reconstruction and cancellation of those belonging to the dropped users. The complexity of such approaches, however, grows substantially with the number of dropped users. We propose a new approach, named LightSecAgg, to overcome this bottleneck by changing the design from &quot;random-seed reconstruction of the dropped users&quot; to &quot;one-shot aggregate-mask reconstruction of the active users via mask encoding/decoding&quot;. We show that LightSecAgg achieves the same privacy and dropout-resiliency guarantees as the state-of-the-art protocols while significantly reducing the overhead for resiliency against dropped users. We also demonstrate that, unlike existing schemes, LightSecAgg can be applied to secure aggregation in the asynchronous FL setting. Furthermore, we provide a modular system design and optimized on-device parallelization for scalable implementation, by enabling computational overlapping between model training and on-device encoding, as well as improving the speed of concurrent receiving and sending of chunked masks. We evaluate LightSecAgg via extensive experiments for training diverse models on various datasets in a realistic FL system with large number of users and demonstrate that LightSecAgg significantly reduces the total training time.

  匹配依据：MPC: secret sharing

  </details>

- **Morse-STF: Improved Protocols for Privacy-Preserving Machine Learning**
  2021-09-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2109.11726)
  Qizhi Zhang, Sijun Tan, Lichun Li, Yun Zhao, Dong Yin, Shan Yin

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation enables multiple mutually distrusting parties to perform computations on data without revealing the data itself, and has become one of the core technologies behind privacy-preserving machine learning. In this work, we present several improved privacy-preserving protocols for both linear and non-linear layers in machine learning. For linear layers, we present an extended beaver triple protocol for bilinear maps that significantly reduces communication of convolution layer. For non-linear layers, we introduce novel protocols for computing the sigmoid and softmax function. Both functions are essential building blocks for machine learning training of classification tasks. Our protocols are both more scalable and robust than prior constructions, and improves runtime performance by 3-17x. Finally, we introduce Morse-STF, an end-to-end privacy-preserving system for machine learning training that leverages all these improved protocols. Our system achieves a 1.8x speedup on logistic regression and 3.9-4.9x speedup on convolutional neural networks compared to prior state-of-the-art systems.

  匹配依据：MPC: secure multi party computation

  </details>

- **Large-Scale Non-Interactive Threshold Cryptosystems in the YOSO Model**
  2021-09-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1290)
  Andreas Erwig, Sebastian Faust, Siavash Riahi

  <details><summary>摘要 / Abstract</summary>

  A $(t,n)$-public key threshold cryptosystem allows distributing the execution of a cryptographic task among a set of $n$ parties by splitting the secret key required for the computation into $n$ shares. A subset of at least $t+1$ honest parties is required to execute the task of the cryptosystem correctly, while security is guaranteed as long as at most $t &lt; \frac{n}{2}$ parties are corrupted. Unfortunately, traditional threshold cryptosystems do not scale well, when executed at large-scale (e.g., in the Internet-environment). In such settings, a possible approach is to select a subset of $n$ players (called a committee) out of the entire universe of $N\gg n$ parties to run the protocol. If done naively, however, this means that the adversary&#x27;s corruption power does not scale with $N$ as otherwise, the adversary would be able to corrupt the entire committee. A beautiful solution for this problem is given by Benhamouda et al. (TCC 2020) who present a novel form of secret sharing, where the efficiency of the protocol is \emph{independent} of $N$, but the adversarial corruption power \emph{scales} with $N$ (a.k.a. fully mobile adversary). They achieve this through a novel mechanism that guarantees parties in a committee to stay anonymous -- also referred to as the YOSO (You Only Speak Once) model -- until they start to interact within the protocol. In this work, we initiate the study of large-scale threshold cryptography in the YOSO model of communication. We formalize and present novel protocols for distributed key generation, threshold encryption, and signature schemes that guarantee security in large-scale environments. A key challenge in our analysis is that we cannot use the secret sharing protocol of Benhamouda et al. as a black-box to construct our schemes, and instead we require a more generalized version, which may be of independent interest. Finally, we show how our protocols can be concretely instantiated in the YOSO model, and discuss interesting applications of our schemes.

  匹配依据：MPC: secret sharing

  </details>

- **APAS: Application-Specific Accelerators for RLWE-based Homomorphic Linear Transformations**
  2021-09-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1284)
  Song Bian, Dur E Shahwar Kundi, Kazuma Hirozawa, Weiqiang Liu, Takashi Sato

  <details><summary>摘要 / Abstract</summary>

  Recently, the application of multi-party secure computing schemes based on homomorphic encryption in the field of machine learning attracts attentions across the research fields. Previous studies have demonstrated that secure protocols adopting packed additive homomorphic encryption (PAHE) schemes based on the ring learning with errors (RLWE) problem exhibit significant practical merits, and are particularly promising in enabling efficient secure inference in machine-learning-as-a-service applications. In this work, we introduce a new technique for performing homomorphic linear transformation (HLT) over PAHE ciphertexts. Using the proposed HLT technique, homomorphic convolutions and inner products can be executed without the use of number theoretic transform and the rotate-and-add algorithms that were proposed in existing works. To maximize the efficiency of the HLT technique, we propose APAS, a hardware-software co-design framework consisting of approximate arithmetic units for the hardware acceleration of HLT. In the experiments, we use actual neural network architectures as benchmarks to show that APAS can improve the computational and communicational efficiency of homomorphic convolution by 8x and 3x, respectively, with an energy reduction of up to 26x as compared to the ASIC implementations of existing methods.

  匹配依据：MPC: secure computing

  </details>

- **A Tight Computational Indistinguishability Bound for Product Distributions**
  2021-09-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1274)
  Nathan Geier

  <details><summary>摘要 / Abstract</summary>

  Assume that distributions $X_0,X_1$ (respectively $Y_0,Y_1$) are $d_X$ (respectively $d_Y$) indistinguishable for circuits of a given size. It is well known that the product distributions $X_0Y_0,\,X_1Y_1$ are $d_X+d_Y$ indistinguishable for slightly smaller circuits. However, in probability theory where unbounded adversaries are considered through statistical distance, it is folklore knowledge that in fact $X_0Y_0$ and $X_1Y_1$ are $d_X+d_Y-d_X\cdot d_Y$ indistinguishable, and also that this bound is tight. We formulate and prove the computational analog of this tight bound. Our proof is entirely different from the proof in the statistical case, which is non-constructive. As a corollary, we show that if $X$ and $Y$ are $d$ indistinguishable, then $k$ independent copies of $X$ and $k$ independent copies of $Y$ are almost $1-(1-d)^k$ indistinguishable for smaller circuits, as against $d\cdot k$ using the looser bound. Our bounds are useful in settings where only weak (i.e. non-negligible) indistinguishability is guaranteed. We demonstrate this in the context of cryptography, showing that our bounds yield simple analysis for amplification of weak oblivious transfer protocols.

  匹配依据：MPC: oblivious transfer

  </details>

- **Secure PAC Bayesian Regression via Real Shamir Secret Sharing**
  2021-09-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2109.11200)
  Jaron Skovsted Gundersen, Bulut Kuskonmaz, Rafael Wisniewski

  <details><summary>摘要 / Abstract</summary>

  A common approach of system identification and machine learning is to generate a model by using training data to predict the test data instances as accurate as possible. Nonetheless, concerns about data privacy are increasingly raised, but not always addressed. We present a secure protocol for learning a linear model relying on recently described technique called real number secret sharing. We take as our starting point the PAC Bayesian bounds and deduce a closed form for the model parameters which depends on the data and the prior from the PAC Bayesian bounds. To obtain the model parameters one needs to solve a linear system. However, we consider the situation where several parties hold different data instances and they are not willing to give up the privacy of the data. Hence, we suggest to use real number secret sharing and multiparty computation to share the data and solve the linear regression in a secure way without violating the privacy of data. We suggest two methods; a secure inverse method and a secure Gaussian elimination method, and compare these methods at the end. The benefit of using secret sharing directly on real numbers is reflected in the simplicity of the protocols and the number of rounds needed. However, this comes with the drawback that a share might leak a small amount of information, but in our analysis we argue that the leakage is small.

  匹配依据：MPC: multiparty computation, secret sharing

  </details>

- **Efficient CCA Timed Commitments in Class Groups**
  2021-09-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1272)
  Sri AravindaKrishnan Thyagarajan, Guilhem Castagnos, Fabien Laguillaumie, Giulio Malavolta

  <details><summary>摘要 / Abstract</summary>

  Timed commitments [Boneh and Naor, CRYPTO 2000] are the timed analogue of standard commitments, where the commitment can be non-interactively opened after a pre-specified amount of time passes. Timed commitments have a large spectrum of applications, such as sealed bid auctions, fair contract signing, fair multi-party computation, and cryptocurrency payments. Unfortunately, all practical constructions rely on a (private-coin) trusted setup and do not scale well with the number of participants. These are two severe limiting factors that have hindered the widespread adoption of this primitive. In this work, we set out to resolve these two issues and propose an efficient timed commitment scheme that also satisfies the strong notion of CCA-security. Specifically, our scheme has a transparent (i.e. public-coin) one-time setup and the amount of sequential computation is essentially independent of the number of participants. As a key technical ingredient, we propose the first (linearly) homomorphic time-lock puzzle with a transparent setup, from class groups of imaginary quadratic order. To demonstrate the applicability of our scheme, we use it to construct a new distributed randomness generation protocol, where $n$ parties jointly sample a random string. Our protocol is the first to simultaneously achieve (1) high scalability in the number of participants, (2) transparent one-time setup, (3) lightning speed in the optimistic case where all parties are honest, and (4) ensure that the output random string is unpredictable and unbiased, even when the adversary corrupts $n-1$ parties. To substantiate the practicality of our approach, we implemented our protocol and our experimental evaluation shows that it is fast enough to be used in practice. We also evaluated a heuristic version of the protocol that is at least 3 orders of magnitude more efficient both in terms of communication size and computation time. This makes the protocol suitable for supporting hundreds of participants.

  匹配依据：MPC: multi party computation

  </details>

- **Speak Much, Remember Little: Cryptography in the Bounded Storage Model, Revisited**
  2021-09-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1270)
  Yevgeniy Dodis, Willy Quach, Daniel Wichs

  <details><summary>摘要 / Abstract</summary>

  The goal of the bounded storage model (BSM) is to construct unconditionally secure cryptographic protocols, by only restricting the storage capacity of the adversary, but otherwise giving it unbounded computational power. Here, we consider a streaming variant of the BSM, where honest parties can stream huge amounts of data to each other so as to overwhelm the adversary&#x27;s storage, even while their own storage capacity is significantly smaller than that of the adversary. Prior works showed several impressive results in this model, including key agreement and oblivious transfer, but only as long as adversary&#x27;s storage $m = O(n^2)$ is at most quadratically larger than the honest user storage $n$. Moreover, the work of Dziembowski and Maurer (DM) also gave a seemingly matching lower bound, showing that key agreement in the BSM is impossible when $m &gt; n^2$. In this work, we observe that the DM lower bound only applies to a significantly more restricted version of the BSM, and does not apply to the streaming variant. Surprisingly, we show that it is possible to construct key agreement and oblivious transfer protocols in the streaming BSM, where the adversary&#x27;s storage can be significantly larger, and even exponential $m = 2^{O(n)}$. The only price of accommodating larger values of $m$ is that the round and communication complexities of our protocols grow accordingly, and we provide lower bounds to show that an increase in rounds and communication is necessary. As an added benefit of our work, we also show that our oblivious transfer (OT) protocol in the BSM satisfies a simulation-based notion of security. In contrast, even for the restricted case of $m = O(n^2)$, prior solutions only satisfied a weaker indistinguishability based definition. As an application of our OT protocol, we get general multiparty computation (MPC) in the BSM that allows for up to exponentially large gaps between $m$ and $n$, while also achieving simulation-based security.

  匹配依据：MPC: multiparty computation, oblivious transfer

  </details>

- **DeSMP: Differential Privacy-exploited Stealthy Model Poisoning Attacks in Federated Learning**
  2021-09-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2109.09955)
  Md Tamjid Hossain, Shafkat Islam, Shahriar Badsha, Haoting Shen

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) has become an emerging machine learning technique lately due to its efficacy in safeguarding the client&#x27;s confidential information. Nevertheless, despite the inherent and additional privacy-preserving mechanisms (e.g., differential privacy, secure multi-party computation, etc.), the FL models are still vulnerable to various privacy-violating and security-compromising attacks (e.g., data or model poisoning) due to their numerous attack vectors which in turn, make the models either ineffective or sub-optimal. Existing adversarial models focusing on untargeted model poisoning attacks are not enough stealthy and persistent at the same time because of their conflicting nature (large scale attacks are easier to detect and vice versa) and thus, remain an unsolved research problem in this adversarial learning paradigm. Considering this, in this paper, we analyze this adversarial learning process in an FL setting and show that a stealthy and persistent model poisoning attack can be conducted exploiting the differential noise. More specifically, we develop an unprecedented DP-exploited stealthy model poisoning (DeSMP) attack for FL models. Our empirical analysis on both the classification and regression tasks using two popular datasets reflects the effectiveness of the proposed DeSMP attack. Moreover, we develop a novel reinforcement learning (RL)-based defense strategy against such model poisoning attacks which can intelligently and dynamically select the privacy level of the FL models to minimize the DeSMP attack surface and facilitate the attack detection.

  匹配依据：MPC: secure multi party computation

  </details>

- **Trojan-Resilience without Cryptography**
  2021-09-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1224)
  Suvradip Chakraborty, Stefan Dziembowski, Malgorzata Galazka, Tomasz Lizurej, Krzysztof Pietrzak, Michelle Yeo

  <details><summary>摘要 / Abstract</summary>

  Digital hardware Trojans are integrated circuits whose implementation differ from the specification in an arbitrary and malicious way. For example, the circuit can differ from its specified input/output behavior after some fixed number of queries (known as ``time bombs&#x27;&#x27;) or on some particular input (known as ``cheat codes&#x27;&#x27;). To detect such Trojans, countermeasures using multiparty computation (MPC) or verifiable computation (VC), have been proposed. On a high level, to realize a circuit with specification $\cF$ one has more sophisticated circuits $\cF^\diamond$ manufactured (where $\cF^\diamond$ specifies a MPC or VC of $\cF$), and then embeds these $\cF^\diamond$&#x27;s into a \emph{master circuit} which must be trusted but is relatively simple compared to $\cF$. Those solutions have a significant overhead as $\cF^\diamond$ is significantly more complex than $\cF$ and also the master circuits are not exactly trivial either. In this work, we show that in restricted settings, where $\cF$ has no evolving state and is queried on independent inputs, we can achieve a relaxed security notion using very simple constructions. In particular, we do not change the specification of the circuit at all (i.e., $\cF=\cF^\diamond$). Moreover the master circuit basically just queries a subset of its manufactured circuits and checks if they&#x27;re all the same. The security we achieve guarantees that, if the manufactured circuits are initially tested on up to $T$ inputs, the master circuit will catch Trojans that try to deviate on significantly more than a $1/T$ fraction of the inputs. This bound is optimal for the type of construction considered, and we provably achieve it using a construction where $12$ instantiations of $\cF$ need to be embedded into the master. We also discuss an extremely simple construction with just $2$ instantiations for which we conjecture that it already achieves the optimal bound.

  匹配依据：MPC: multiparty computation

  </details>

- **Gröbner Basis Attack on STARK-Friendly Symmetric-Key Primitives: JARVIS, MiMC and GMiMCerf**
  2021-09-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1232)
  Gizem Kara, Oğuz Yayla

  <details><summary>摘要 / Abstract</summary>

  A number of arithmetization-oriented ciphers emerge for use in advanced cryptographic protocols such as secure multi-party computation (MPC), fully homomorphic encryption (FHE) and zero-knowledge proofs (ZK) in recent years. The standard block ciphers like AES and the hash functions SHA2/SHA3 are proved to be efficient in software and hardware but not optimal to use in this field, for this reason, new kind of cryptographic primitives were proposed recently. However, unlike traditional ones, there is no standard approach to design and analyze such block ciphers and the hash functions, therefore their security analysis needs to be done carefully. In 2018, StarkWare launched a public STARK-Friendly Hash (SFH) Challenge to select an efficient and secure hash function to be used within ZK-STARKs, transparent and post-quantum secure proof systems. The block cipher JARVIS is one of the first ciphers designed for STARK applications but, shortly after its publication, the cipher has been shown vulnerable to Gröbner basis attack. This paper aims to describe a Gröbner basis attack on new block ciphers, MiMC, GMiMCerf (SFH candidates) and the variants of JARVIS. We present the complexity of Gröbner basis attack on JARVIS-like ciphers. Then we give results from our experiments for the attack on reduced-round MiMC and a structure we found in the Gröbner basis attack for GMiMCerf.

  匹配依据：MPC: secure multi party computation

  </details>

- **Algebraic Adversaries in the Universal Composability Framework**
  2021-09-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1218)
  Michel Abdalla, Manuel Barbosa, Jonathan Katz, Julian Loss, Jiayu Xu

  <details><summary>摘要 / Abstract</summary>

  The algebraic-group model (AGM), which lies between the generic group model and the standard model of computation, provides a means by which to analyze the security of cryptosystems against so-called algebraic adversaries. We formalize the AGM within the framework of universal composability, providing formal definitions for this setting and proving an appropriate composition theorem. This extends the applicability of the AGM to more-complex protocols, and lays the foundations for analyzing algebraic adversaries in a composable~fashion. Our results also clarify the meaning of composing proofs in the AGM with other proofs and they highlight a natural form of independence between idealized groups that seems inherent to the AGM and has not been made formal before---these insights also apply to the composition of game-based proofs in the AGM. We show the utility of our model by proving several important protocols universally composable for algebraic adversaries, specifically: (1) the Chou-Orlandi protocol for oblivious transfer, and (2) the SPAKE2 and CPace protocols for password-based authenticated key exchange.

  匹配依据：MPC: oblivious transfer

  </details>

- **JUBILEE: Secure Debt Relief and Forgiveness**
  2021-09-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2109.07267) · [IACR ePrint](https://eprint.iacr.org/2021/1193)
  David Cerezo Sánchez

  <details><summary>摘要 / Abstract</summary>

  JUBILEE is a securely computed mechanism for debt relief and forgiveness in a frictionless manner without involving trusted third parties, leading to more harmonious debt settlements by incentivising the parties to truthfully reveal their private information. JUBILEE improves over all previous methods: - individually rational, incentive-compatible, truthful/strategy-proof, ex-post efficient, optimal mechanism for debt relief and forgiveness with private information - by the novel introduction of secure computation techniques to debt relief, the “blessing of the debtor ” is hereby granted for the first time: debt settlements with higher expected profits and a higher probability of success than without using secure computation A simple and practical implementation is included for “The Secure Spreadsheet”. Another implementation is realised using Raziel smart contracts on a blockchain with Pravuil consensus.

  匹配依据：MPC: secure computation

  </details>

- **Partial islands and subregion complexity in geometric secret-sharing model**
  2021-09-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2109.07842)
  Aranya Bhattacharya, Arpan Bhattacharyya, Pratik Nandy, Ayan K. Patra

  <details><summary>摘要 / Abstract</summary>

  We compute the holographic subregion complexity of a radiation subsystem in a geometric secret-sharing model of Hawking radiation in the &quot;complexity = volume&quot; proposal. The model is constructed using multiboundary wormhole geometries in AdS$_{3}$. The entanglement curve for secret-sharing captures a crossover between two minimal curves in the geometry apart from the usual eternal Page curve present for the complete radiation entanglement. We compute the complexity dual to the secret-sharing minimal surfaces and study their &quot;time&quot; evolution. When we have access to a small part of the radiation, the complexity shows a jump at the secret-sharing time larger than the Page time. Moreover, the minimal surfaces do not have access to the entire island region for this particular case. They can only access it partially. We describe this inaccessibility in the context of &quot;classical&quot; Markov recovery.

  匹配依据：MPC: secret sharing

  </details>

- **Check-based generation of one-time tables using qutrits**
  2021-09-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2109.08107)
  Li Yu, Xue-Tong Zhang, Fuqun Wang, Chui-Ping Yang

  <details><summary>摘要 / Abstract</summary>

  One-time tables are a class of two-party correlations that can help achieve information-theoretically secure two-party (interactive) classical or quantum computation. In this work we propose a bipartite quantum protocol for generating a simple type of one-time tables (the correlation in the Popescu-Rohrlich nonlocal box) with partial security. We then show that by running many instances of the first protocol and performing checks on some of them, asymptotically information-theoretically secure generation of one-time tables can be achieved. The first protocol is adapted from a protocol for semi-honest quantum oblivious transfer, with some changes so that no entangled state needs to be prepared, and the communication involves only one qutrit in each direction. We show that some information tradeoffs in the first protocol are similar to that in the semi-honest oblivious transfer protocol. We also obtain two types of inequalities about guessing probabilities in some protocols for generating one-time tables, from a single type of inequality about guessing probabilities in semi-honest quantum oblivious transfer protocols.

  匹配依据：MPC: oblivious transfer

  </details>

- **SynCirc: Efficient Synthesis of Depth-Optimized Circuits for Secure Computation**
  2021-09-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1153)
  Arpita Patra, Thomas Schneider, Ajith Suresh, Hossein Yalame

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-party Computation (MPC) allows to securely compute on private data. To make MPC practical, logic synthesis can be used to automatically translate a description of the function to be computed securely into optimized and error-free boolean circuits. TinyGMW (Demmler et al., CCS&#x27;15) used industry-grade hardware synthesis tools (DC, Yosys) to generate depth-optimized circuits for MPC. To evaluate their optimized circuits, they used the ABY framework (Demmler et al., NDSS&#x27;15) for secure two-party computation. The recent ABY2.0 framework (Patra et al., USENIX Security&#x27;21) presented round-efficient constructions using multi-input AND gates and improved over ABY by at least 6x in online communication for 4-input AND gate evaluation. In this work, we propose SynCirc, an efficient hardware synthesis framework designed for MPC applications. Our framework is based on Verilog and the open-source tool Yosys-ABC. It provides custom libraries and new constraints that accommodate multi-input AND gates. With this, we improve over TinyGMW by up to 3x in multiplicative depth with a corresponding improvement in online round complexity. Moreover, we provide efficient realizations of several new building blocks including comparison, multiplexers, and equality check. For these building blocks, we achieve improvements in multiplicative depth/online rounds between 22.3% and 66.7%. With these improvements, our framework makes multi-round MPC better-suited for high-latency networks such as the Internet. With respect to the look-up table based approach of Dessouky et al (NDSS’17), our framework improves the online communication by 1.3x - 18x.

  匹配依据：MPC: secure computation, secure multi party computation, secure two party computation

  </details>

- **Reputation at Stake! A Trust Layer over Decentralized Ledger for Multiparty Computation and Reputation-Fair Lottery**
  2021-09-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1165)
  Mario Larangeira

  <details><summary>摘要 / Abstract</summary>

  This work leverages on the framework of Karakostas et al. (SCN&#x27;20) by extending it to the realm of reputation and trust. At the best of our knowledge, it is the first to introduce reputation and trust to proof of stake systems. Namely, we show that their delegation framework can be repurposed to construct a trust layer over a proof of stake consensus protocol in addition to its original stake delegation application. Furthermore, we show that such extension yields a concrete reputation system satisfying the positive results of (1) Asharov et al. (Asiacrypt&#x27;13), therefore allowing the secure execution of multiparty protocols such as GMW (STOC&#x27; 87) and Damgard and Ishai (Crypto&#x27;05), and (2) Kleinrock et al. (Indocrypt&#x27;20), therefore allowing the construction of Reputation-fair Lottery and therefore Proof of Reputation. More concretely, our devised layer is used to construct a concrete reputation system based on arbitrary stake distribution. In this layer groups of users can freely ``assign their respective trust&#x27;&#x27; to members of a set of trustees, i.e., participants that offered themselves as receivers of such assignment. Furthermore, our work offers the advantage of providing a clear stake based criteria, verifiable in the ledger, and, therefore, naturally resistant to sybil attack, that the set of trustees indeed yields an honest majority. This setting provides a better situation than a simple assumption of honest majority, since it involves stake in a decentralized ledger, and the public verifiability of the reputation score via verification of the stake distribution.

  匹配依据：MPC: multiparty computation

  </details>

- **Grafting Key Trees: Efficient Key Management for Overlapping Groups**
  2021-09-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1158)
  Joël Alwen, Benedikt Auerbach, Mirza Ahad Baig, Miguel Cueto, Karen Klein, Guillermo Pascual-Perez, Krzysztof Pietrzak, Michael Walter

  <details><summary>摘要 / Abstract</summary>

  Key trees are often the best solution in terms of transmission cost and storage requirements for managing keys in a setting where a group needs to share a secret key, while being able to efficiently rotate the key material of users (in order to recover from a potential compromise, or to add or remove users). Applications include multicast encryption protocols like LKH (Logical Key Hierarchies) or group messaging like the current IETF proposal TreeKEM. A key tree is a (typically balanced) binary tree, where each node is identified with a key: leaf nodes hold users&#x27; secret keys while the root is the shared group key. For a group of size $N$, each user just holds $\log(N)$ keys (the keys on the path from its leaf to the root) and its entire key material can be rotated by broadcasting $2\log(N)$ ciphertexts (encrypting each fresh key on the path under the keys of its parents). In this work we consider the natural setting where we have many groups with partially overlapping sets of users, and ask if we can find solutions where the cost of rotating a key is better than in the trivial one where we have a separate key tree for each group. We show that in an asymptotic setting (where the number $m$ of groups is fixed while the number $N$ of users grows) there exist more general key graphs whose cost converges to the cost of a single group, thus saving a factor linear in the number of groups over the trivial solution. As our asymptotic ``solution&quot; converges very slowly and performs poorly on concrete examples, we propose an algorithm that uses a natural heuristic to compute a key graph for any given group structure. Our algorithm combines two greedy algorithms, and is thus very efficient: it first converts the group structure into a ``lattice graph&quot;, which is then turned into a key graph by repeatedly applying the algorithm for constructing a Huffman code. To better understand how far our proposal is from an optimal solution, we prove lower bounds on the update cost of continuous group-key agreement and multicast encryption in a symbolic model admitting (asymmetric) encryption, pseudorandom generators, and secret sharing as building blocks.

  匹配依据：MPC: secret sharing

  </details>

- **Evolving Secret Sharing in Almost Semi-honest Model**
  2021-09-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1156)
  Jyotirmoy Pramanik, Avishek Adhikari

  <details><summary>摘要 / Abstract</summary>

  Evolving secret sharing is a special kind of secret sharing where the number of shareholders is not known beforehand, i.e., at time t = 0. In classical secret sharing such a restriction was assumed inherently i.e., the the number of shareholders was given to the dealer’s algorithm as an input. Evolving secret sharing relaxes this condition. Pramanik and Adhikari left an open problem regarding malicious shareholders in the evolving setup, which we answer in this paper. We introduce a new cheating model, called the almost semi-honest model, where a shareholder who joins later can check the authenticity of share of previous ones. We use collision resistant hash function to construct such a secret sharing scheme with malicious node identification. Moreover, our scheme preserves the share size of Komargodski et al. (TCC 2016).

  匹配依据：MPC: secret sharing

  </details>

- **Algebraic Restriction Codes and their Applications**
  2021-09-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1177)
  Divesh Aggarwal, Nico Döttling, Jesko Dujmovic, Mohammad Hajiabadi, Giulio Malavolta, Maciej Obremski

  <details><summary>摘要 / Abstract</summary>

  Consider the following problem: You have a device that is supposed to compute a linear combination of its inputs, which are taken from some finite field. However, the device may be faulty and compute arbitrary functions of its inputs. Is it possible to encode the inputs in such a way that only linear functions can be evaluated over the encodings? I.e., learning an arbitrary function of the encodings will not reveal more information about the inputs than a linear combination. In this work, we introduce the notion of algebraic restriction codes (AR codes), which constrain adversaries who might compute any function to computing a linear function. Our main result is an information-theoretic construction AR codes that restrict any class of function with a bounded number of output bits to linear functions. Our construction relies on a seed which is not provided to the adversary. While interesting and natural on its own, we show an application of this notion in cryptography. In particular, we show that AR codes lead to the first construction of rate-1 oblivious transfer with statistical sender security from the Decisional Diffie-Hellman assumption, and the first-ever construction that makes black-box use of cryptography. Previously, such protocols were known only from the LWE assumption, using non-black-box cryptographic techniques. We expect our new notion of AR codes to find further applications, e.g., in the context of non-malleability, in the future.

  匹配依据：MPC: oblivious transfer

  </details>

- **Adaptive Security of Multi-Party Protocols, Revisited**
  2021-09-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1175)
  Martin Hirt, Chen-Da Liu-Zhang, Ueli Maurer

  <details><summary>摘要 / Abstract</summary>

  The goal of secure multi-party computation (MPC) is to allow a set of parties to perform an arbitrary computation task, where the security guarantees depend on the set of parties that are corrupted. The more parties are corrupted, the less is guaranteed, and typically the guarantees are completely lost when the number of corrupted parties exceeds a certain corruption bound. Early and also many recent protocols are only statically secure in the sense that they provide no security guarantees if the adversary is allowed to choose adaptively which parties to corrupt. Security against an adversary with such a strong capability is often called adaptive security and a significant body of literature is devoted to achieving adaptive security, which is known as a difficult problem. In particular, a main technical obstacle in this context is the so-called ``commitment problem&#x27;&#x27;, where the simulator is unable to consistently explain the internal state of a party with respect to its pre-corruption outputs. As a result, protocols typically resort to the use of cryptographic primitives like non-committing encryption, incurring a substantial efficiency loss. This paper provides a new, clean-slate treatment of adaptive security in MPC, exploiting the specification concept of constructive cryptography (CC). A new natural security notion, called CC-adaptive security, is proposed, which is technically weaker than standard adaptive security but nevertheless captures security against a fully adaptive adversary. Known protocol examples separating between adaptive and static security are also insecure in our notion. Moreover, our notion avoids the commitment problem and thereby the need to use non-committing or equivocal tools. We exemplify this by showing that the protocols by Cramer, Damgard and Nielsen (EUROCRYPT&#x27;01) for the honest majority setting, and (the variant without non-committing encryption) by Canetti, Lindell, Ostrovsky and Sahai (STOC&#x27;02) for the dishonest majority setting, achieve CC-adaptive security. The latter example is of special interest since all UC-adaptive protocols in the dishonest majority setting require some form of non-committing or equivocal encryption.

  匹配依据：MPC: secure multi party computation

  </details>

- **Secure Blockchain-Based Supply Chain Management with Verifiable Digital Twins**
  2021-09-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2109.03870)
  Vincenzo Botta, Laura Fusco, Attilio Mondelli, Ivan Visconti

  <details><summary>摘要 / Abstract</summary>

  A major problem in blockchain-based supply chain management is the potential unreliability of digital twins when considering digital representations of physical goods. Indeed, the use of blockchain technology to trace goods is obviously ineffective if there is no strong correspondence between what is physically exchanged and the digital information that appears in blockchain transactions. In this work, we propose a model for strengthening the supply chain management of physical goods by leveraging blockchain technology along with a digital-twin verification feature. Our model can be instantiated in various scenarios and we have in particular considered the popular case of food traceability. In contrast to other models known in the literature that propose their own ad-hoc properties to assess the robustness of their supply chain management systems, in this work we use the formalism of secure computation, where processes are described through generic and natural ideal functionalities.

  匹配依据：MPC: secure computation

  </details>

- **Multi-party Semi-quantum Secret Sharing Protocol based on Measure-flip and Reflect Operations**
  2021-09-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2109.01380)
  Li Jian, Chong-Qiang Ye

  <details><summary>摘要 / Abstract</summary>

  Semi-quantum secret sharing (SQSS) protocols serve as fundamental frameworks in quantum secure multi-party computations, offering the advantage of not requiring all users to possess intricate quantum devices. However, the current landscape of SQSS protocols predominantly caters to bipartite scenarios, rendering them inadequate for practical multi-party secret sharing requirements. Addressing this gap, this paper proposes a novel SQSS protocol based on multi-particle GHZ states. In this protocol, the quantum user distributes predetermined secret information to multiple classical users with limited quantum capabilities, necessitating collaborative efforts among all classical users to reconstruct the correct secret information. By utilizing measure-flip and reflect operations, the transmitted multi-particle GHZ states can all contribute keys, thereby improving the utilization of transmitted particles. Security analysis shows that the protocol&#x27;s resilience against prevalent external and internal threats. Additionally, employing IBM Qiskit, we conduct quantum circuit simulations to validate the protocol&#x27;s accuracy and feasibility. Compared with similar studies, the proposed protocol has advantages in terms of protocol scalability, qubit efficiency, and shared message types.

  匹配依据：MPC: secret sharing

  </details>

- **Low-Latency and Secure Computation Offloading Assisted by Hybrid Relay-Reflecting Intelligent Surface**
  2021-09-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2109.01335)
  Khac-Hoang Ngo, Nhan Thanh Nguyen, Thinh Quang Dinh, Trong-Minh Hoang, Markku Juntti

  <details><summary>摘要 / Abstract</summary>

  Recently, the hybrid relay-reflecting intelligent surface (HRRIS) has been introduced as a spectral- and energy-efficient architecture to assist wireless communication systems. In the HRRIS, a single or few active relay elements are deployed along with a large number of passive reflecting elements, allowing it to not only reflect but also amplify the incident signals. In this work, we investigate the potential of the HRRIS in aiding the computation offloading in a single-user mobile edge computing system. The objective is to minimize the offloading latency while ensuring the secrecy of user data against a malicious eavesdropper. We develop efficient solutions to this latency minimization problem based on alternating optimization. Through numerical results, we show that the deployment of the HRRIS can result in a considerable reduction in latency. Furthermore, the latency reduction gain offered by the HRRIS is much more significant than that of the conventional reconfigurable intelligent surface (RIS).

  匹配依据：MPC: secure computation

  </details>

- **Labeled PSI from Homomorphic Encryption with Reduced Computation and Communication**
  2021-09-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1116)
  Kelong Cong, Radames Cruz Moreno, Mariana Botelho da Gama, Wei Dai, Ilia Iliashenko, Kim Laine, Michael Rosenberg

  <details><summary>摘要 / Abstract</summary>

  It is known that fully homomorphic encryption (FHE) can be used to build efficient (labeled) Private Set Intersection protocols in the unbalanced setting, where one of the sets is much larger than the other (Chen et al. (CCS&#x27;17, CCS&#x27;18)). In this paper we demonstrate multiple algorithmic improvements upon these works. In particular, our protocol has an asymptotically better computation cost, requiring only $O(\sqrt{|X|})$ homomorphic multiplications, and communication complexity sublinear in the larger set size $|X|$. We demonstrate that our protocol is significantly better than that of Chen et al. (CCS&#x27;18) for many practical parameters, especially in terms of online communication cost. For example, when intersecting $2^{28}$ and $2048$ item sets, our protocol reduces the online computation time by more than 83% and communication by more than 32%. When intersecting $2^{24}$ and $4096$ item sets, our protocol reduces the online computation time by 50% and communication by 52%. Our comparison to other state-of-the-art unbalanced PSI protocols shows that our protocol has the best total communication complexity when $|X| \geq 2^{24}$. For labeled PSI our protocol also outperforms Chen et al. (CCS&#x27;18). When intersecting $2^{20}$ and $256$ item sets, with the larger set having associated $288$-byte labels, our protocol reduces the online computation time by more than 85% and communication by 36%. Finally, we demonstrate a modification that results in nearly constant communication cost in the larger set size $|X|$, but impractically high computation complexity on today&#x27;s CPUs. For example, to intersect a $210$-item set with sets of size $2^{22}$, $2^{24}$, or $2^{26}$, our proof-of-concept implementation requires only $0.76$ MB of online communication, which is more than a $24$-fold improvement over Chen et al. (CCS&#x27;18).

  匹配依据：MPC: private set intersection

  </details>

- **Evolving Secret Sharing Schemes Based on Polynomial Evaluations and Algebraic Geometry Codes**
  2021-09-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1115)
  Chaoping Xing, Chen Yuan

  <details><summary>摘要 / Abstract</summary>

  A secret sharing scheme enables the dealer to share a secret among $n$ parties. A classic secret sharing scheme takes the number $n$ of parties and the secret as the input. If $n$ is not known in advance, the classic secret sharing scheme may fail. Komargodski, Naor, and Yogev \cite[TCC 2016]{KNY16} first proposed the evolving secret sharing scheme that only takes the secret as the input. In the work \cite[TCC 2016]{KNY16}, \cite[TCC 2017]{KC17} and \cite[Eurocrypt 2020]{BO20}, evolving threshold and ramp secret sharing schemes were extensively investigated. However, all of their constructions except for the first construction in \cite{BO20} are inspired by the scheme given in \cite{KNY16}, namely, these schemes rely on the scheme for st-connectivity which allows to generate infinite number of shares. In this work, we revisit evolving secret sharing schemes and present three constructions that take completely different approach. Most of the previous schemes mentioned above have more combinatorial flavor, while our schemes are more algebraic in nature. More precisely speaking, our evolving secret sharing schemes are obtained via either the Shamir secret sharing or arithmetic secret sharing from algebraic geometry codes alone. Our first scheme is an evolving $k$-threshold secret sharing scheme with share size $k^{1+\epsilon}\log t$ for any constant $\epsilon&gt;0$. Thus, our scheme achieves almost the same share size as in \cite[TCC 2016]{KNY16}. Moreover, our scheme is obtained by a direct construction while the scheme in \cite[TCC 2016]{KNY16} that achieves the $(k-1)\log t$ share size is obtained by a recursive construction which makes their structure complicated. Our second scheme is an evolving $k_t$-threshold secret sharing scheme with any sequence $\{k_t\}_{t=1}^\infty$ of threshold values that has share size $t^4$. This scheme improves the share size by $\log t$ given in \cite{KC17} where a dynamic evolving $k_t$-threshold secret sharing scheme with the share size $O(t^4\log t)$ was proposed. In addition, we also show that if the threshold values $k_t$ grow in rate $\lfloor \beta t\rfloor$ for a real $\beta\in(0,1)$, then we have a dynamic evolving threshold secret sharing scheme with the share size $O(t^{4\beta})$. For $\beta&lt;0.25$, this scheme has sub-linear share size which was not known before. Our last scheme is an evolving $(\Ga t,\Gb t)$-ramp secret sharing scheme with constant share size. One major feature of this ramp scheme is that it is multiplicative as the scheme is also an arithmetic secret sharing scheme. We note that the same technique in \cite{KC17} can also transform all of our schemes to a robust scheme as our scheme is linear.\footnote{We note that by replacing the building block scheme with an arithmetic secret sharing scheme, the evolving $(\Ga t,\Gb t)$-ramp secret sharing scheme in \cite{BO20} can also be multiplicative. However, their share size is much bigger than ours as each party hold multiple shares. }

  匹配依据：MPC: secret sharing

  </details>

- **On Actively Secure Fine-grained Access Structures from Isogeny Assumptions**
  2021-08-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1109)
  Philipp Muth, Fabio Campos

  <details><summary>摘要 / Abstract</summary>

  We present an actively secure threshold scheme in the setting of Hard Homogeneous Spaces (HHS) which allows ﬁne-grained access structures. More precisely, we elevate a passively secure isogeny-based threshold scheme to an actively secure setting. We prove the active security and simulatability of our advanced schemes. By characterising the necessary properties, we open our schemes to a signiﬁcantly wider ﬁeld of applicable secret sharing schemes. Furthermore, we show that Shamir’s scheme has our generalised properties, and thereby our approach truly represents a less restrictive generalisation.

  匹配依据：MPC: secret sharing

  </details>

- **Mt. Random: Multi-Tiered Randomness Beacons**
  2021-08-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1096)
  Ignacio Cascudo, Bernardo David, Omer Shlomovits, Denis Varlakov

  <details><summary>摘要 / Abstract</summary>

  Many decentralized applications require a common source of randomness that cannot be biased or predicted by any single party. Randomness beacons provide such a functionality, allowing parties to periodically obtain fresh random outputs and verify that they are computed correctly. In this work, we propose Mt. Random, a multi-tiered randomness beacon that combines Publicly Verifiable Secret Sharing (PVSS) and (Threshold) Verifiable Random Function (VRF) techniques in order to provide efficiency/randomness quality trade-offs with security under the standard DDH assumption (in the random oracle model) using only a bulletin board as setup (a requirement for the vast majority of beacons). Each tier provides a constant stream of random outputs offering progressive efficiency vs. quality trade-offs: true uniform randomness is refreshed less frequently than pseudorandomness, which in turn is refreshed less frequently than (bounded) biased randomness. This wide span of efficiency/quality allows for applications to consume random outputs from an optimal point in this trade-off spectrum. In order to achieve these results, we construct two new building blocks of independent interest: GULL, a PVSS-based beacon that preprocesses a large batch of random outputs but allows for gradual release of smaller &quot;sub-batches&#x27;&#x27;, which is a first in the literature of randomness beacons; and a publicly verifiable and unbiasable protocol for Distributed Key Generation protocol (DKG), which is significantly more efficient than most of previous DKGs secure under standard assumptions and closely matches the efficiency of the currently most efficient biasable DKG protocol. We showcase the efficiency of our novel building blocks and of the Mt. Random beacon via benchmarks made with a prototype implementation.

  匹配依据：MPC: secret sharing

  </details>

- **Towards Accountability in CRS Generation**
  2021-08-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1090)
  Prabhanjan Ananth, Gilad Asharov, Hila Dahari, Vipul Goyal

  <details><summary>摘要 / Abstract</summary>

  It is well known that several cryptographic primitives cannot be achieved without a common reference string (CRS). Those include, for instance, non-interactive zero-knowledge for NP, or maliciously secure computation in fewer than four rounds. The security of those primitives heavily relies upon on the assumption that the trusted authority, who generates the CRS, does not misuse the randomness used in the CRS generation. However, we argue that there is no such thing as an unconditionally trusted authority and every authority must be held accountable for any trust to be well-founded. Indeed, a malicious authority can, for instance, recover private inputs of honest parties given transcripts of the protocols executed with respect to the CRS it has generated. While eliminating trust in the trusted authority may not be entirely feasible, can we at least move towards achieving some notion of accountability? We propose a new notion in which, if the CRS authority releases the private inputs of protocol executions to others, we can then provide a publicly-verifiable proof that certifies that the authority misbehaved. We study the feasibility of this notion in the context of non-interactive zero knowledge and two-round secure two-party computation.

  匹配依据：MPC: secure computation, secure two party computation

  </details>
