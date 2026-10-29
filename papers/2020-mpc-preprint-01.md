# 2020 · MPC · 仅预印本来源 · 第 1/3 页

[总目录](../PAPERS.md) · [下一页](2020-mpc-preprint-02.md)

- **An Ideal Compartmented Secret Sharing Scheme Based on Linear Homogeneous Recurrence Relations**
  2020-12-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1615)
  Jiangtao Yuan, Guoai Xu, Guosheng Xu

  <details><summary>摘要 / Abstract</summary>

  Multipartite secret sharing schemes are those that have multipartite access structures. The set of the participants in those schemes is divided into several parts, and all the participants in the same part play the equivalent role. One type of such access structure is the compartmented access structure. We propose an ideal and efficient compartmented multi-secret sharing scheme based on the linear homogeneous recurrence (LHR) relations. In the construction phase, the shared secrets are hidden in some terms of the linear homogeneous recurrence sequence. In the recovery phase, the shared secrets are obtained by solving those terms in which the shared secrets are hidden. When the global threshold is $t$, our scheme can reduce the computational complexity from $O(n^{t-1})$ to $O(n^{\max(t_i-1)}\log n)$, where $t_i&lt;t$. The security of the proposed scheme is based on Shamir&#x27;s threshold scheme. Moreover, it is efficient to share the multi-secret and to change the shared secrets in the proposed scheme. That is, the proposed scheme can improve the performances of the key management and the distributed system.

  匹配依据：MPC: secret sharing

  </details>

- **SLAP: Simple Lattice-Based Private Stream Aggregation Protocol**
  2020-12-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1611)
  Jonathan Takeshita, Ryan Karl, Ting Gong, Taeho Jung

  <details><summary>摘要 / Abstract</summary>

  Private Stream Aggregation (PSA) protocols allow for the secure aggregation of time-series data, affording security and privacy to users&#x27; private data, with significantly better efficiency than general secure computation such as homomorphic encryption, multiparty computation, and secure hardware based approaches. Earlier PSA protocols face limitations including needless complexity, a lack of post-quantum security, or other practical issues. In this work, we present SLAP, a Simple Lattice-based Private Stream Aggregation Protocol. SLAP features two variants with post-quantum security, with simpler and more efficient computations enabled by (1) our white-box approach that builds the encryption directly from the Ring Learning With Errors assumption and (2) application of state-of-the-art algorithmic optimizations in lattice-based cryptography. We prove that SLAP with differentially private inputs is an aggregator oblivious PSA scheme. We implement SLAP, and show experimentally the improvements of SLAP over similar work. We show a speedup of 20.76x over the previous state-of-the-art RLWE-based PSA work&#x27;s aggregation, and apply techniques including RNS, NTT, and batching to obtain a throughput of 390,691 aggregations per second for 1000 users. The communication overhead of SLAP is less than in previous work, with decreases of up to 99.96% in ciphertext sizes as compared to previous work in RLWE-based PSA. We also show the improvement of SLAP over other state-of-the-art post-quantum PSA with regards to throughput, and compare and contrast our RLWE-based approach with other work based upon secret sharing and Learning-With-Rounding.

  匹配依据：MPC: multiparty computation, secret sharing, secure computation

  </details>

- **Denoising quantum states with Quantum Autoencoders -- Theory and Applications**
  2020-12-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2012.14714)
  Tom Achache, Lior Horesh, John Smolin

  <details><summary>摘要 / Abstract</summary>

  We implement a Quantum Autoencoder (QAE) as a quantum circuit capable of correcting Greenberger-Horne-Zeilinger (GHZ) states subject to various noisy quantum channels : the bit-flip channel and the more general quantum depolarizing channel. The QAE shows particularly interesting results, as it enables to perform an almost perfect reconstruction of noisy states, but can also, more surprisingly, act as a generative model to create noise-free GHZ states. Finally, we detail a useful application of QAEs : Quantum Secret Sharing (QSS). We analyze how noise corrupts QSS, causing it to fail, and show how the QAE allows the QSS protocol to succeed even in the presence of noise.

  匹配依据：MPC: secret sharing

  </details>

- **A New Efficient Hierarchical Multi-secret Sharing Scheme Based on Linear Homogeneous Recurrence Relations**
  2020-12-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1612)
  Jiangtao Yuan, Jing Yang, Guoai Xu, Xingxing Jia, Fang-wei Fu, Chenyu Wang

  <details><summary>摘要 / Abstract</summary>

  Hierarchical secret sharing is an important key management technique since it is specially customized for hierarchical organizations with different departments allocated with different privileges, such as the government agencies or companies. Hierarchical access structures have been widely adopted in secret sharing schemes, where efficiency is the primary consideration for various applications. How to design an efficient hierarchical secret sharing scheme is an important issue. In 2007, a famous hierarchical secret sharing (HSS) scheme was proposed by Tassa based on Birkhoff interpolation, and later, based on the same method, many other HSS schemes were proposed. However, these schemes all depend on Polya&#x27;s condition, which is a necessary condition not a sufficient condition. It cannot guarantee that Tassa&#x27;s HSS scheme always exists. Furthermore, this condition needs to check the non-singularity of many matrices. We propose a hierarchical multi-secret sharing scheme based on the linear homogeneous recurrence (LHR) relations and the one-way function. In our scheme, we select $m$ linearly independent homogeneous recurrence relations. The participants in the highly-ranked subsets $\gamma_1, \gamma_2 ,\cdots, \gamma_{j-1}$ join in the $j$-th subset to construct the $j$-th LHR relation. In addition, the proposed hierarchical multi-secret sharing scheme just requires one share for each participant, and keeps the same computational complexity. Compared with the state-of-the-art hierarchical secret sharing schemes, our scheme has high efficiency.

  匹配依据：MPC: secret sharing

  </details>

- **An Embedded Domain-Specific Language for Logical Circuit Descriptions with Applications to Garbled Circuits**
  2020-12-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1604)
  Andrei Lapets, Wyatt Howe, Ben Getchell, Frederick Jansen

  <details><summary>摘要 / Abstract</summary>

  Contemporary libraries and frameworks that make it possible to incorporate secure multi-party computation protocols and capabilities into production software systems and applications must sometimes deliver underlying capabilities (such as logical circuit synthesis) to new kinds of environments (such as web browsers or serverless cloud computing platforms). In order to illustrate some of the benefits of addressing this challenge by building a solution from the ground up that leverages the features of a contemporary and widely used programming language, we present an embedded domain-specific language that allows programmers to describe and synthesize logical circuits. Notably, this approach allows programmers to employ many of the language features and any of the programming paradigms supported by the host language. We illustrate this flexibility by considering two use cases: synthesizing circuits for relational operations and synthesizing circuits corresponding to the SHA-256 cryptographic hash function.

  匹配依据：MPC: garbled circuits, secure multi party computation

  </details>

- **Secure Hot Path Crowdsourcing with Local Differential Privacy under Fog Computing Architecture**
  2020-12-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2012.13807)
  Mengmeng Yang, Ivan Tjuawinata, Kwok Yan Lam, Jun Zhao, Lin Sun

  <details><summary>摘要 / Abstract</summary>

  Crowdsourcing plays an essential role in the Internet of Things (IoT) for data collection, where a group of workers is equipped with Internet-connected geolocated devices to collect sensor data for marketing or research purpose. In this paper, we consider crowdsourcing these worker&#x27;s hot travel path. Each worker is required to report his real-time location information, which is sensitive and has to be protected. Encryption-based methods are the most direct way to protect the location, but not suitable for resource-limited devices. Besides, local differential privacy is a strong privacy concept and has been deployed in many software systems. However, the local differential privacy technology needs a large number of participants to ensure the accuracy of the estimation, which is not always the case for crowdsourcing. To solve this problem, we proposed a trie-based iterative statistic method, which combines additive secret sharing and local differential privacy technologies. The proposed method has excellent performance even with a limited number of participants without the need of complex computation. Specifically, the proposed method contains three main components: iterative statistics, adaptive sampling, and secure reporting. We theoretically analyze the effectiveness of the proposed method and perform extensive experiments to show that the proposed method not only provides a strict privacy guarantee, but also significantly improves the performance from the previous existing solutions.

  匹配依据：MPC: secret sharing

  </details>

- **Function Secret Sharing for PSI-CA: With Applications to Private Contact Tracing**
  2020-12-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2012.13053) · [IACR ePrint](https://eprint.iacr.org/2020/1599)
  Samuel Dittmer, Yuval Ishai, Steve Lu, Rafail Ostrovsky, Mohamed Elsabagh, Nikolaos Kiourtis, Brian Schulte, Angelos Stavrou

  <details><summary>摘要 / Abstract</summary>

  In this work we describe a token-based solution to Contact Tracing via Distributed Point Functions (DPF) and, more generally, Function Secret Sharing (FSS). The key idea behind the solution is that FSS natively supports secure keyword search on raw sets of keywords without a need for processing the keyword sets via a data structure for set membership. Furthermore, the FSS functionality enables adding up numerical payloads associated with multiple matches without additional interaction. These features make FSS an attractive tool for lightweight privacy-preserving searching on a database of tokens belonging to infected individuals.

  匹配依据：MPC: secret sharing

  </details>

- **Batched Differentially Private Information Retrieval**
  2020-12-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1596)
  Kinan Dak Albab, Rawane Issa, Mayank Varia, Kalman Graffi

  <details><summary>摘要 / Abstract</summary>

  Private Information Retrieval (PIR) allows several clients to query a database held by one or more servers, such that the contents of their queries remain private. Prior PIR schemes have achieved sublinear communication and computation by leveraging computational assumptions, federating trust among many servers, relaxing security to permit differentially private leakage, refactoring effort into an offline stage to reduce online costs, or amortizing costs over a large batch of queries. In this work, we present an efficient PIR protocol that combines all of the above techniques to achieve constant amortized communication and computation complexity in the size of the database and constant client work. We leverage differentially private leakage in order to provide better trade-offs between privacy and efficiency. Our protocol achieves speed-ups up to and exceeding $10$x in practical settings compared to state of the art PIR protocols, and can scale to batches with hundreds of millions of queries on cheap commodity AWS machines. Our protocol builds upon a new secret sharing scheme that is both incremental and non-malleable, which may be of interest to a wider audience. Our protocol provides security up to abort against malicious adversaries that can corrupt all but one party.

  匹配依据：MPC: secret sharing

  </details>

- **RandPiper -- Reconfiguration-Friendly Random Beacons with Quadratic Communication**
  2020-12-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1590)
  Adithya Bhat, Nibesh Shrestha, Aniket Kate, Kartik Nayak

  <details><summary>摘要 / Abstract</summary>

  Random beacon protocols provide a continuous public source of randomness and their applications range from public lotteries to zero-knowledge proofs. Existing random beacon protocols in the bounded synchronous model sacrifice either the fault tolerance or the communication complexity for security, or ease of reconfigurability. This work overcomes the challenges with the existing works through a novel communication efficient combination of state machine replication and (publicly) verifiable secret sharing (PVSS/VSS) protocols. We first design a new Byzantine fault-tolerant state machine replication protocol with $O(\kappa n^2)$ bits communication per consensus decision without using threshold signatures. Next, we design GRandPiper (Good Pipelined Random beacon), a random beacon protocol with bias-resistance and unpredictability, that uses PVSS and has a communication complexity of $O(\kappa n^2)$ always (best and worst cases), for a static adversary. However, GRandPiper allows an adaptive adversary to predict beacon values up to $t+1$ epochs into the future. Therefore, we design BRandPiper (Better RandPiper), that uses VSS and has a communication complexity of $O(\kappa fn^2)$, where $f$ is the actual number of faults, while offering a strong unpredictability with an advantage of only a single round even for an adaptive adversary.

  匹配依据：MPC: secret sharing

  </details>

- **How to Make Private Distributed Cardinality Estimation Practical, and Get Differential Privacy for Free**
  2020-12-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1576)
  Changhui Hu, Jin Li, Zheli Liu, Xiaojie Guo, Yu Wei, Xuan Guang, Grigorios Loukides, Changyu Dong

  <details><summary>摘要 / Abstract</summary>

  Secure computation is a promising privacy enhancing technology, but it is often not scalable enough for data intensive applications. On the other hand, the use of sketches has gained popularity in data mining, because sketches often give rise to highly efficient and scalable sub-linear algorithms. It is natural to ask: what if we put secure computation and sketches together? We investigated the question and the findings are interesting: we can get security, we can get scalability, and somewhat unexpectedly, we can also get differential privacy -- for free. Our study started from building a secure computation protocol based on the Flajolet-Martin (FM) sketches, for solving the Private Distributed Cardinality Estimation (PDCE) problem, which is a fundamental problem with applications ranging from crowd tracking to network monitoring. The state of art protocol for PDCE (Fenske et al. CCS&#x27;17) is computationally expensive and not scalable enough to cope with big data applications, which prompted us to design a better protocol. Our further analysis revealed that if the cardinality to be estimated is large enough, our protocol can achieve $(\epsilon,\delta)$-differential privacy automatically, without requiring any additional manipulation of the output. The result signifies a new approach for achieving differential privacy that departs from the mainstream approach (i.e. adding noise to the result). Free differential privacy can be achieved because of two reasons: secure computation minimizes information leakage, and the intrinsic estimation variance of the FM sketch makes the output of our protocol uncertain. We further show that the result is not just theoretical: the minimal cardinality for differential privacy to hold is only $10^2-10^4$ for typical parameters.

  匹配依据：MPC: secure computation

  </details>

- **CirC: Compiler infrastructure for proof systems, software verification, and more**
  2020-12-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1586)
  Alex Ozdemir, Fraser Brown, Riad S. Wahby

  <details><summary>摘要 / Abstract</summary>

  Cryptographic tools like proof systems, multi-party computation, and fully homomorphic encryption are usually applied to computations expressed as systems of arithmetic constraints. In practice, this means that these applications rely on compilers from high-level programming languages (like C) to such constraints. This compilation task is challenging, but not entirely new: the software verification community has a rich literature on compiling programs to logical constraints (like SAT or SMT). In this work, we show that building shared compiler infrastructure for compiling to constraint representations is possible, because these representations share a common abstraction: stateless, non-uniform, non-deterministic computations that we call existentially quantified circuits, or EQCs. Moreover, we show that this shared infrastructure is useful, because it allows compilers for proof systems to benefit from decades of work on constraint compilation techniques for software verification. To make our approach concrete we create CirC, an infrastructure for building compilers to EQCs. CirC makes it easy to compile to new EQCs: we build support for three, R1CS (used for proof systems), SMT (used for verification and bug-finding), and ILP (used for optimization), in ≈2000 LOC. It&#x27;s also easy to extend CirC to support new source languages: we build a feature-complete compiler for a cryptographic language in one week and ≈900 LOC, whereas the reference compiler for the same language took years to write, comprises ≈24000 LOC, and produces worse-performing output than our compiler. Finally, CirC enables novel applications that combine multiple EQCs. For example, we build the first pipeline that (1) automatically identifies bugs in programs, then (2) automatically constructs cryptographic proofs of the bugs&#x27; existence.

  匹配依据：MPC: multi party computation

  </details>

- **NN-EMD: Efficiently Training Neural Networks using Encrypted Multi-Sourced Datasets**
  2020-12-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2012.10547)
  Runhua Xu, James Joshi, Chao Li

  <details><summary>摘要 / Abstract</summary>

  Training a machine learning model over an encrypted dataset is an existing promising approach to address the privacy-preserving machine learning task, however, it is extremely challenging to efficiently train a deep neural network (DNN) model over encrypted data for two reasons: first, it requires large-scale computation over huge datasets; second, the existing solutions for computation over encrypted data, such as homomorphic encryption, is inefficient. Further, for an enhanced performance of a DNN model, we also need to use huge training datasets composed of data from multiple data sources that may not have pre-established trust relationships among each other. We propose a novel framework, NN-EMD, to train DNN over multiple encrypted datasets collected from multiple sources. Toward this, we propose a set of secure computation protocols using hybrid functional encryption schemes. We evaluate our framework for performance with regards to the training time and model accuracy on the MNIST datasets. Compared to other existing frameworks, our proposed NN-EMD framework can significantly reduce the training time, while providing comparable model accuracy and privacy guarantees as well as supporting multiple data sources. Furthermore, the depth and complexity of neural networks do not affect the training time despite introducing a privacy-preserving NN-EMD setting.

  匹配依据：MPC: secure computation

  </details>

- **Verifiable Timed Signatures Made Practical**
  2020-12-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1563)
  Sri Aravinda KrishnanThyagarajan, Adithya Bhat, Giulio Malavolta, Nico Döttling, Aniket Kate, Dominique Schröder

  <details><summary>摘要 / Abstract</summary>

  A verifiable timed signature (VTS) scheme allows one to time-lock a signature on a known message for a given amount of time $T$ such that after performing a sequential computation for time $T$ anyone can extract the signature from the time-lock. Verifiability ensures that anyone can publicly check if a time-lock contains a valid signature on the message without solving it first, and that the signature can be obtained by solving the same for time $T$. This work formalizes VTS, presents efficient constructions compatible with BLS, Schnorr, and ECDSA signatures, and experimentally demonstrates that these constructions can be employed in practice. On a technical level, we design an efficient cut-and-choose protocol based on the homomorphic time-lock puzzles to prove the validity of a signature encapsulated in a time-lock puzzle. We also present a new efficient {range proof} protocol that significantly improves upon existing proposals in terms of the proof size, and is also of independent interest. While VTS is a versatile tool with numerous existing applications, we demonstrate VTS&#x27;s applicability to resolve three novel challenging issues in the space of cryptocurrencies. Specifically, we show how VTS is the cryptographic cornerstone to construct: (i) Payment channel networks with improved on-chain unlinkability of users involved in a transaction, (ii) multi-party signing of transactions for cryptocurrencies without any on-chain notion of time and (iii) cryptocurrency-enabled fair multi-party computation protocol.

  匹配依据：MPC: multi party computation

  </details>

- **Towards Scalable and Privacy-Preserving Deep Neural Network via Algorithmic-Cryptographic Co-design**
  2020-12-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2012.09364)
  Jun Zhou, Longfei Zheng, Chaochao Chen, Yan Wang, Xiaolin Zheng, Bingzhe Wu, Cen Chen, Li Wang, Jianwei Yin

  <details><summary>摘要 / Abstract</summary>

  Deep Neural Networks (DNNs) have achieved remarkable progress in various real-world applications, especially when abundant training data are provided. However, data isolation has become a serious problem currently. Existing works build privacy preserving DNN models from either algorithmic perspective or cryptographic perspective. The former mainly splits the DNN computation graph between data holders or between data holders and server, which demonstrates good scalability but suffers from accuracy loss and potential privacy risks. In contrast, the latter leverages time-consuming cryptographic techniques, which has strong privacy guarantee but poor scalability. In this paper, we propose SPNN - a Scalable and Privacy-preserving deep Neural Network learning framework, from algorithmic-cryptographic co-perspective. From algorithmic perspective, we split the computation graph of DNN models into two parts, i.e., the private data related computations that are performed by data holders and the rest heavy computations that are delegated to a server with high computation ability. From cryptographic perspective, we propose using two types of cryptographic techniques, i.e., secret sharing and homomorphic encryption, for the isolated data holders to conduct private data related computations privately and cooperatively. Furthermore, we implement SPNN in a decentralized setting and introduce user-friendly APIs. Experimental results conducted on real-world datasets demonstrate the superiority of SPNN.

  匹配依据：MPC: secret sharing

  </details>

- **Quantum Secret Sharing and Tripartite Information**
  2020-12-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2012.08445)
  Marius Junge, Chloe Kim, Guangkuo Liu, Peixue Wu

  <details><summary>摘要 / Abstract</summary>

  We develop a connection between tripartite information $I_3$, secret sharing protocols and multi-unitaries. This leads to explicit ((2,3)) threshold schemes in arbitrary dimension minimizing tripartite information $I_3$. As an application we show that Page scrambling unitaries simultaneously work for all secrets shared by Alice. Using the $I_3$-Ansatz for imperfect sharing schemes we discover examples of VIP sharing schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Two-server Distributed ORAM with Sublinear Computation and Constant Rounds**
  2020-12-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1547)
  Ariel Hamlin, Mayank Varia

  <details><summary>摘要 / Abstract</summary>

  Distributed ORAM (DORAM) is a multi-server variant of Oblivious RAM. Originally proposed to lower bandwidth, DORAM has recently been of great interest due to its applicability to secure computation in the RAM model, where circuit complexity and rounds of communication are equally important metrics of efficiency. In this work, we construct the first DORAM schemes in the 2-server, semi-honest setting that simultaneously achieve sublinear server computation and constant rounds of communication. We provide two constant-round constructions, one based on square root ORAM that has $O(\sqrt{N}\log N)$ local computation and another based on secure computation of a doubly efficient PIR that achieves local computation of $O(N^\epsilon)$ for any $\epsilon &gt; 0$ but that allows the servers to distinguish between reads and writes. As a building block in the latter construction, we provide secure computation protocols for evaluation and interpolation of multivariate polynomials based on the Fast Fourier Transform, which may be of independent interest.

  匹配依据：MPC: secure computation

  </details>

- **PsiBench: Pragmatic Benchmark of Two-party Private Set Intersection.**
  2020-12-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1541)
  Ziyuan Liang, Weiran Liu, Hanwen Feng, Feng Han, Liqiang Peng, Li Peng, Chao Li, Guorui Xu, Lei Zhang, Fan Zhang

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection (PSI) allows two parties to obtain the intersection of their data sets while revealing nothing else. PSI is attractive in many scenarios and has wide applications in academia and industry. Over the last three decades, a large number of PSI protocols have been proposed using different cryptographic techniques, under different assumptions, for different scenarios. The inherent complexity, heterogeneous constructions, and rapid evolution of PSI protocols make it difficult to have a unified perspective and further promote the field. We make the following three contributions to present a pragmatic benchmark of two-party PSI. First, we propose the Map-and-Compare framework, which generalizes almost all efficient PSI constructions to date, and intuitively explains the idea and challenge of PSI constructions. Based on the framework, we divide existing proposals into several categories and perform a systematic analysis of the features and use cases of different PSI variants. Second, we present a Java-based benchmark library that implements almost all two-party PSI protocols (which are considered to define the state-of-the-art in terms of concrete performance) and supports rapid prototyping of new PSI protocols. Third, by using our library as a common ground, we provide a comprehensive and impartial comparison of all our PSI implementations in detail. We discuss the performance of different proposals in various settings.

  匹配依据：MPC: private set intersection

  </details>

- **Multi-Client Oblivious RAM with Poly-Logarithmic Communication**
  2020-12-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1551)
  Sherman S. M. Chow, Katharina Fech, Russell W. F. Lai, Giulio Malavolta

  <details><summary>摘要 / Abstract</summary>

  Oblivious RAM enables oblivious access to memory in the single-client setting, which may not be the best fit in the network setting. Multi-client oblivious RAM (MCORAM) considers a collaborative but untrusted environment, where a database owner selectively grants read access and write access to different entries of a confidential database to multiple clients. Their access pattern must remain oblivious not only to the server but also to fellow clients. This upgrade rules out many techniques for constructing ORAM, forcing us to pursue new techniques. MCORAM not only provides an alternative solution to private anonymous data access (Eurocrypt 2019) but also serves as a promising building block for equipping oblivious file systems with access control and extending other advanced cryptosystems to the multi-client setting. Despite being a powerful object, the current state-of-the-art is unsatisfactory: The only existing scheme requires $O(\sqrt n)$ communication and client computation for a database of size $n$. Whether it is possible to reduce these complexities to $\mathsf{polylog}(n)$, thereby matching the upper bounds for ORAM, is an open problem, i.e., can we enjoy access control and client-obliviousness under the same bounds? Our first result answers the above question affirmatively by giving a construction from fully homomorphic encryption (FHE). Our main technical innovation is a new technique for cross-key trial evaluation of ciphertexts. We also consider the same question in the setting with $N$ non-colluding servers, out of which at most $t$ of them can be corrupt. We build multi-server MCORAM from distributed point functions (DPF), and propose new constructions of DPF via a virtualization technique with bootstrapping, assuming the existence of homomorphic secret sharing and pseudorandom generators in NC0, which are not known to imply FHE.

  匹配依据：MPC: secret sharing

  </details>

- **Honest Majority MPC with Abort with Minimal Online Communication**
  2020-12-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1556)
  Daniel Escudero, Anders Dalskov

  <details><summary>摘要 / Abstract</summary>

  In this work we focus on improving the communication complexity of the \emph{online phase} of honest majority MPC protocols. To this end, we present a general and simple method to compile arbitrary secret-sharing-based passively secure protocols defined over an arbitrary ring that are secure up to additive attacks in a malicious setting, to actively secure protocols with abort. The resulting protocol has a total communication complexity in the online phase of $1.5(n-1)$ shares, which amounts to $1.5$ shares per party asymptotically. An important aspect of our techniques is that they can be seen as generalization of ideas that have been used in other works in a rather \emph{ad-hoc} manner for different secret-sharing protocols. Thus, our work serves as a way of unifying key ideas in recent honest majority protocols, to understand better the core techniques and similarities among these works. Furthermore, for $n=3$, when instantiated with replicated secret-sharing-based protocols (Araki et al.~CCS 2016), the communication complexity in the online phase amounts to only $1$ ring element per party, matching the communication complexity of the BLAZE protocol (Patra \&amp; Suresh, NDSS 2020), while having a much simpler design.

  匹配依据：MPC: secret sharing

  </details>

- **Data Appraisal Without Data Sharing**
  2020-12-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2012.06430)
  Mimee Xu, Laurens van der Maaten, Awni Hannun

  <details><summary>摘要 / Abstract</summary>

  One of the most effective approaches to improving the performance of a machine learning model is to procure additional training data. A model owner seeking relevant training data from a data owner needs to appraise the data before acquiring it. However, without a formal agreement, the data owner does not want to share data. The resulting Catch-22 prevents efficient data markets from forming. This paper proposes adding a data appraisal stage that requires no data sharing between data owners and model owners. Specifically, we use multi-party computation to implement an appraisal function computed on private data. The appraised value serves as a guide to facilitate data selection and transaction. We propose an efficient data appraisal method based on forward influence functions that approximates data value through its first-order loss reduction on the current model. The method requires no additional hyper-parameters or re-training. We show that in private, forward influence functions provide an appealing trade-off between high quality appraisal and required computation, in spite of label noise, class imbalance, and missing data. Our work seeks to inspire an open market that incentivizes efficient, equitable exchange of domain-specific training data.

  匹配依据：MPC: multi party computation

  </details>

- **Data Privacy in Trigger-Action Systems**
  2020-12-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2012.05749)
  Yunang Chen, Amrita Roy Chowdhury, Ruizhe Wang, Andrei Sabelfeld, Rahul Chatterjee, Earlence Fernandes

  <details><summary>摘要 / Abstract</summary>

  Trigger-action platforms (TAPs) allow users to connect independent web-based or IoT services to achieve useful automation. They provide a simple interface that helps end-users create trigger-compute-action rules that pass data between disparate Internet services. Unfortunately, TAPs introduce a large-scale security risk: if they are compromised, attackers will gain access to sensitive data for millions of users. To avoid this risk, we propose eTAP, a privacy-enhancing trigger-action platform that executes trigger-compute-action rules without accessing users&#x27; private data in plaintext or learning anything about the results of the computation. We use garbled circuits as a primitive, and leverage the unique structure of trigger-compute-action rules to make them practical. We formally state and prove the security guarantees of our protocols. We prototyped eTAP, which supports the most commonly used operations on popular commercial TAPs like IFTTT and Zapier. Specifically, it supports Boolean, arithmetic, and string operations on private trigger data and can run 100% of the top-500 rules of IFTTT users and 93.4% of all publicly-available rules on Zapier. Based on ten existing rules that exercise a wide variety of operations, we show that eTAP has a modest performance impact: on average rule execution latency increases by 70 ms (55%) and throughput reduces by 59%.

  匹配依据：MPC: garbled circuits

  </details>

- **Communication-Computation Efficient Secure Aggregation for Federated Learning**
  2020-12-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2012.05433)
  Beongjun Choi, Jy-yong Sohn, Dong-Jun Han, Jaekyun Moon

  <details><summary>摘要 / Abstract</summary>

  Federated learning has been spotlighted as a way to train neural networks using distributed data with no need for individual nodes to share data. Unfortunately, it has also been shown that adversaries may be able to extract local data contents off model parameters transmitted during federated learning. A recent solution based on the secure aggregation primitive enabled privacy-preserving federated learning, but at the expense of significant extra communication/computational resources. In this paper, we propose a low-complexity scheme that provides data privacy using substantially reduced communication/computational resources relative to the existing secure solution. The key idea behind the suggested scheme is to design the topology of secret-sharing nodes as a sparse random graph instead of the complete graph corresponding to the existing solution. We first obtain the necessary and sufficient condition on the graph to guarantee both reliability and privacy. We then suggest using the Erdős-Rényi graph in particular and provide theoretical guarantees on the reliability/privacy of the proposed scheme. Through extensive real-world experiments, we demonstrate that our scheme, using only $20 \sim 30\%$ of the resources required in the conventional scheme, maintains virtually the same levels of reliability and data privacy in practical federated learning systems.

  匹配依据：MPC: secret sharing

  </details>

- **Secure Medical Image Analysis with CrypTFlow**
  2020-12-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2012.05064)
  Javier Alvarez-Valle, Pratik Bhatu, Nishanth Chandran, Divya Gupta, Aditya Nori, Aseem Rastogi, Mayank Rathee, Rahul Sharma, Shubham Ugare

  <details><summary>摘要 / Abstract</summary>

  We present CRYPTFLOW, a system that converts TensorFlow inference code into Secure Multi-party Computation (MPC) protocols at the push of a button. To do this, we build two components. Our first component is an end-to-end compiler from TensorFlow to a variety of MPC protocols. The second component is an improved semi-honest 3-party protocol that provides significant speedups for inference. We empirically demonstrate the power of our system by showing the secure inference of real-world neural networks such as DENSENET121 for detection of lung diseases from chest X-ray images and 3D-UNet for segmentation in radiotherapy planning using CT images. In particular, this paper provides the first evaluation of secure segmentation of 3D images, a task that requires much more powerful models than classification and is the largest secure inference task run till date.

  匹配依据：MPC: secure multi party computation

  </details>

- **Oblivious Pseudorandom Functions from Isogenies**
  2020-12-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1532)
  Dan Boneh, Dmitry Kogan, Katharine Woo

  <details><summary>摘要 / Abstract</summary>

  An oblivious PRF, or OPRF, is a protocol between a client and a server, where the server has a key $k$ for a secure pseudorandom function $F$, and the client has an input $x$ for the function. At the end of the protocol the client learns $F(k,x)$, and nothing else, and the server learns nothing. An OPRF is verifiable if the client is convinced that the server has evaluated the PRF correctly with respect to a prior commitment to $k$. OPRFs and verifiable OPRFs have numerous applications, such as private-set-intersection protocols, password-based key-exchange protocols, and defense against denial-of-service attacks. Existing OPRF constructions use RSA-, Diffie-Hellman-, and lattice-type assumptions. The first two are not post-quantum secure. In this paper we construct OPRFs and verifiable OPRFs from isogenies. Our main construction uses isogenies of supersingular elliptic curves over $\mathbb{F}_{p^{2}}$ and tries to adapt the Diffie-Hellman OPRF to that setting. However, a recent attack on supersingular-isogeny systems due to Galbraith et al. [ASIACRYPT 2016] makes this approach difficult to secure. To overcome this attack, and to validate the server&#x27;s response, we develop two new zero-knowledge protocols that convince each party that its peer has sent valid messages. With these protocols in place, we obtain an OPRF in the SIDH setting and prove its security in the UC framework. Our second construction is an adaptation of the Naor-Reingold PRF to commutative group actions. Combining it with recent constructions of oblivious transfer from isogenies, we obtain an OPRF in the CSIDH setting.

  匹配依据：MPC: oblivious transfer, private set intersection

  </details>

- **Witness Encryption from Garbled Circuit and Multikey Fully Homomorphic Encryption Techniques**
  2020-12-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1502)
  Kamil Kluczniak

  <details><summary>摘要 / Abstract</summary>

  In a witness encryption scheme, to decrypt a ciphertext associated with an NP statement, the decrypter takes as input a witness testifying that the statement is in the language. When the statement is not in the language, then the message is hidden. Thus far, the only provably secure constructions assume the existence of indistinguishability obfuscation (iO) and multilinear maps (MMaps). We make progress towards building polynomially efficient witness encryption for NP without resorting to iO or MMaps. In particular, we give a witness encryption scheme from Yao&#x27;s garbled circuit technique and a new type of fully homomorphic encryption (FHE) that we call annihilating. Interestingly, we require a version of the annihilating FHE that is circularly insecure, i.e., allows testing the presence of a key cycle. We prove our witness encryption&#x27;s security from a novel assumption about our annihilating FHE. We formulate the assumption as an interplay between an annihilating FHE and ideal ciphers. We show a candidate (leveled) annihilating FHE built from a multikey variant of the BGV/BFV fully homomorphic cryptosystems.

  匹配依据：MPC: garbled circuit

  </details>

- **Revisiting the Privacy Needs of Real-World Applicable Company Benchmarking**
  2020-12-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1512)
  Jan Pennekamp, Patrick Sapel, Ina Berenice Fink, Simon Wagner, Sebastian Reuter, Christian Hopmann, Klaus Wehrle, Martin Henze

  <details><summary>摘要 / Abstract</summary>

  Benchmarking the performance of companies is essential to identify improvement potentials in various industries. Due to a competitive environment, this process imposes strong privacy needs, as leaked business secrets can have devastating effects on participating companies. Consequently, related work proposes to protect sensitive input data of companies using secure multi-party computation or homomorphic encryption. However, related work so far does not consider that also the benchmarking algorithm, used in today&#x27;s applied real-world scenarios to compute all relevant statistics, itself contains significant intellectual property, and thus needs to be protected. Addressing this issue, we present PCB — a practical design for Privacy-preserving Company Benchmarking that utilizes homomorphic encryption and a privacy proxy — which is specifically tailored for realistic real-world applications in which we protect companies&#x27; sensitive input data and the valuable algorithms used to compute underlying key performance indicators. We evaluate PCB&#x27;s performance using synthetic measurements and showcase its applicability alongside an actual company benchmarking performed in the domain of injection molding, covering 48 distinct key performance indicators calculated out of hundreds of different input values. By protecting the privacy of all participants, we enable them to fully profit from the benefits of company benchmarking.

  匹配依据：MPC: secure multi party computation

  </details>

- **Wireless Secret Sharing Game between Two Legitimate Users and an Eavesdropper**
  2020-12-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2012.00796)
  Lei Miao, Dingde Jiang

  <details><summary>摘要 / Abstract</summary>

  Wireless secret sharing is crucial to information security in the era of Internet of Things. One method is to utilize the effect of the randomness of the wireless channel in the data link layer to generate the common secret between two legitimate users Alice and Bob. This paper studies this secret sharing mechanism from the perspective of game theory. In particular, we formulate a non-cooperative zero-sum game between the legitimate users and an eavesdropper Eve. In a symmetrical game where Eve has the same probability of successfully receiving a packet from Alice and Bob when the transmission distance is the same, we show that both pure and mixed strategy Nash equilibria exist. In an asymmetric game where Eve has different probabilities of successfully receiving a packet from Alice and Bob, a pure strategy may not exist; in this case, we show how a mixed strategy Nash equilibrium can be found.

  匹配依据：MPC: secret sharing

  </details>

- **Extremal Set Theory and LWE Based Access Structure Hiding Verifiable Secret Sharing with Malicious-Majority and Free Verification**
  2020-11-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.14804)
  Vipin Singh Sehrawat, Foo Yee Yeo, Yvo Desmedt

  <details><summary>摘要 / Abstract</summary>

  Secret sharing allows distributing a secret among several parties such that only authorized subsets, specified by an access structure, can reconstruct the secret. Sehrawat and Desmedt (COCOON 2020) introduced hidden access structures, that remain secret until some authorized subset of parties collaborate. However, their scheme assumes semi-honest parties and supports only restricted access structures. We address these shortcomings by constructing an access structure hiding verifiable secret sharing scheme that supports all monotone access structures. It is the first secret sharing scheme to support cheater identification and share verifiability in malicious-majority settings. The verification procedure of our scheme incurs no communication overhead. As the building blocks of our scheme, we introduce and construct: (i) a set-system with $&gt; \exp\left(c\frac{2(\log h)^2}{(\log\log h)}\right)+2\exp\left(c\frac{(\log h)^2}{(\log\log h)}\right)$ subsets of a set of $h$ elements. Our set-system, $\mathcal{H}$, is defined over $\mathbb{Z}_m$, where $m$ is a non-prime-power. The size of each set in $\mathcal{H}$ is divisible by $m$ but the sizes of their pairwise intersections are not, unless one set is a subset of another, (ii) a new variant of the learning with errors (LWE) problem, called PRIM-LWE, wherein the secret matrix is sampled such that its determinant is a generator of $\mathbb{Z}_q^*$, where $q$ is the LWE modulus. The security of our scheme relies on the hardness of the LWE problem, and its share size is $$(1+ o(1)) \dfrac{2^{\ell}}{\sqrt{π\ell/2}}(2 q^{\varrho + 0.5} + \sqrt{q} + \mathrmΘ(h)),$$ where $\varrho \leq 1$ is a constant and $\ell$ is the total number of parties. We also provide directions for future work to reduce the share size to \[\leq \dfrac{1}{3} \left( (1+ o(1)) \dfrac{2^{\ell}}{\sqrt{π\ell/2}}(2 q^{\varrho + 0.5} + 2\sqrt{q}) \right).\]

  匹配依据：MPC: secret sharing

  </details>

- **Distributed Additive Encryption and Quantization for Privacy Preserving Federated Deep Learning**
  2020-11-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.12623)
  Hangyu Zhu, Rui Wang, Yaochu Jin, Kaitai Liang, Jianting Ning

  <details><summary>摘要 / Abstract</summary>

  Homomorphic encryption is a very useful gradient protection technique used in privacy preserving federated learning. However, existing encrypted federated learning systems need a trusted third party to generate and distribute key pairs to connected participants, making them unsuited for federated learning and vulnerable to security risks. Moreover, encrypting all model parameters is computationally intensive, especially for large machine learning models such as deep neural networks. In order to mitigate these issues, we develop a practical, computationally efficient encryption based protocol for federated deep learning, where the key pairs are collaboratively generated without the help of a third party. By quantization of the model parameters on the clients and an approximated aggregation on the server, the proposed method avoids encryption and decryption of the entire model. In addition, a threshold based secret sharing technique is designed so that no one can hold the global private key for decryption, while aggregated ciphertexts can be successfully decrypted by a threshold number of clients even if some clients are offline. Our experimental results confirm that the proposed method significantly reduces the communication costs and computational complexity compared to existing encrypted federated learning without compromising the performance and security.

  匹配依据：MPC: secret sharing

  </details>

- **Round Efficient Secure Multiparty Quantum Computation with Identifiable Abort**
  2020-11-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1464)
  Bar Alon, Hao Chung, Kai-Min Chung, Mi-Ying Huang, Yi Lee, Yu-Ching Shen

  <details><summary>摘要 / Abstract</summary>

  A recent result by Dulek et al. (EUROCRYPT 2020) showed a secure protocol for computing any quantum circuit even without the presence of an honest majority. Their protocol, however, is susceptible to a ``denial of service&#x27;&#x27; attack and allows even a single corrupted party to force an abort. We propose the first quantum protocol that admits security-with-identifiable-abort, which allows the honest parties to agree on the identity of a corrupted party in case of an abort. Additionally, our protocol is the first to have the property that the number of rounds where quantum communication is required is independent of the circuit complexity. Furthermore, if there exists a post-quantum secure classical protocol whose round complexity is independent of the circuit complexity, then our protocol has this property as well. Our protocol is secure under the assumption that classical quantum-resistant fully homomorphic encryption schemes with decryption circuit of logarithmic depth exist. Interestingly, our construction also admits a reduction from quantum fair secure computation to classical fair secure computation.

  匹配依据：MPC: secure computation

  </details>

- **On The Round Complexity of Secure Quantum Computation**
  2020-11-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.11212) · [IACR ePrint](https://eprint.iacr.org/2020/1471)
  James Bartusek, Andrea Coladangelo, Dakshita Khurana, Fermi Ma

  <details><summary>摘要 / Abstract</summary>

  We construct the first constant-round protocols for secure quantum computation in the two-party (2PQC) and multi-party (MPQC) settings with security against malicious adversaries. Our protocols are in the common random string (CRS) model. - Assuming two-message oblivious transfer (OT), we obtain (i) three-message 2PQC, and (ii) five-round MPQC with only three rounds of online (input-dependent) communication; such OT is known from quantum-hard Learning with Errors (QLWE). - Assuming sub-exponential hardness of QLWE, we obtain (i) three-round 2PQC with two online rounds and (ii) four-round MPQC with two online rounds. - When only one (out of two) parties receives output, we achieve minimal interaction (two messages) from two-message OT; classically, such protocols are known as non-interactive secure computation (NISC), and our result constitutes the first maliciously-secure quantum NISC. Additionally assuming reusable malicious designated-verifier NIZK arguments for NP (MDV-NIZKs), we give the first MDV-NIZK for QMA that only requires one copy of the quantum witness. Finally, we perform a preliminary investigation into two-round secure quantum computation where each party must obtain output. On the negative side, we identify a broad class of simulation strategies that suffice for classical two-round secure computation that are unlikely to work in the quantum setting. Next, as a proof-of-concept, we show that two-round secure quantum computation exists with respect to a quantum oracle.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **Constant-round Multi-party Quantum Computation for Constant Parties**
  2020-11-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.12061)
  Zhu Cao

  <details><summary>摘要 / Abstract</summary>

  One of the central themes in classical cryptography is multi-party computation, which performs joint computation on multiple participants&#x27; data while maintaining data privacy. The extension to the quantum regime was proposed in 2002, but despite two decades of research, the current state-of-the-art multi-party quantum computation protocol for a fixed number of parties (even 2 parties) requires unbounded rounds of communication, which greatly limit its practical usage. In this work, we propose the first constant-round multi-party quantum computation protocol for a fixed number of parties against specious adversaries, thereby significantly reducing the required number of rounds. Our work constitutes a key step towards practical implementation of secure multi-party quantum computation, and opens the door for practitioners to be involved in this exciting field. The result of our work has wide implications to quantum fidelity evaluation, quantum machine learning, quantum voting, and distributed quantum information processing.

  匹配依据：MPC: multi party computation

  </details>

- **Effectiveness of MPC-friendly Softmax Replacement**
  2020-11-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.11202)
  Marcel Keller, Ke Sun

  <details><summary>摘要 / Abstract</summary>

  Softmax is widely used in deep learning to map some representation to a probability distribution. As it is based on exp/log functions that are relatively expensive in multi-party computation, Mohassel and Zhang (2017) proposed a simpler replacement based on ReLU to be used in secure computation. However, we could not reproduce the accuracy they reported for training on MNIST with three fully connected layers. Later works (e.g., Wagh et al., 2019 and 2021) used the softmax replacement not for computing the output probability distribution but for approximating the gradient in back-propagation. In this work, we analyze the two uses of the replacement and compare them to softmax, both in terms of accuracy and cost in multi-party computation. We found that the replacement only provides a significant speed-up for a one-layer network while it always reduces accuracy, sometimes significantly. Thus we conclude that its usefulness is limited and one should use the original softmax function instead.

  匹配依据：MPC: multi party computation, secure computation

  </details>

- **Rate-1 Quantum Fully Homomorphic Encryption**
  2020-11-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1454)
  Orestis Chardouvelis, Nico Doettling, Giulio Malavolta

  <details><summary>摘要 / Abstract</summary>

  Secure function evaluation (SFE) allows Alice to publish an encrypted version of her input $m$ such that Bob (holding a circuit $C$) can send a single message that reveals $C(m)$ to Alice, and nothing more. Security is required to hold against malicious parties, that may behave arbitrarily. In this work we study the notion of SFE in the quantum setting, where Alice outputs an encrypted quantum state $|\psi&gt;$ and learns $C(|\psi&gt;)$ after receiving Bob&#x27;s message. We show that, assuming the quantum hardness of the learning with errors problem (LWE), there exists an SFE protocol for quantum computation with communication complexity $(||\psi&gt;| + |C(|\psi&gt;)|) · (1 + o(1))$, which is nearly optimal. This result is obtained by two main technical steps, which might be of independent interest. Specifically, we show (i) a construction of a rate-1 quantum fully-homomorphic encryption and (ii) a generic transformation to achieve malicious circuit privacy in the quantum setting.

  匹配依据：MPC: secure function evaluation

  </details>

- **New (k,l,m)-verifiable multi-secret sharing schemes based on XTR public key system**
  2020-11-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.08648) · [IACR ePrint](https://eprint.iacr.org/2020/1453)
  Jing Yang, Fang-Wei Fu

  <details><summary>摘要 / Abstract</summary>

  Secret sharing was proposed primarily in 1979 to solve the problem of key distribution. In recent decades, researchers have proposed many improvement schemes. Among all these schemes, the verifiable multi-secret sharing (VMSS) schemes are studied sufficiently, which share multiple secrets simultaneously and perceive malicious dealer as well as participants. By pointing out that the schemes presented by Dehkordi and Mashhadi in 2008 cannot detect some vicious behaviors of the dealer, we propose two new VMSS schemes by adding validity check in the verification phase to overcome this drawback. Our new schemes are based on XTR public key system, and can realize $GF(p^{6})$ security by computations in $GF(p^{2})$ without explicit constructions of $GF(p^{6})$, where $p$ is a prime. Compared with the VMSS schemes using RSA and linear feedback shift register (LFSR) public key cryptosystems, our schemes can achieve the same security level with shorter parameters by using trace function. What&#x27;s more, our schemes are much simpler to operate than those schemes based on Elliptic Curve Cryptography (ECC). In addition, our schemes are dynamic and threshold changeable, which means that it is efficient to implement our schemes according to the actual situation when participants, secrets or the threshold needs to be changed.

  匹配依据：MPC: secret sharing

  </details>

- **Line-Point Zero Knowledge and Its Applications**
  2020-11-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1446)
  Samuel Dittmer, Yuval Ishai, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  We introduce and study a simple kind of proof system called line-point zero knowledge (LPZK). In an LPZK proof, the prover encodes the witness as an affine line $\mathbf{v}(t) := \mathbf{a}t + \mathbf{b}$ in a vector space $\mathbb{F}^n$, and the verifier queries the line at a single random point $t=\alpha$. LPZK is motivated by recent practical protocols for vector oblivious linear evaluation (VOLE), which can be used to compile LPZK proof systems into lightweight designated-verifier NIZK protocols. We construct LPZK systems for proving satisfiability of arithmetic circuits with attractive efficiency features. These give rise to designated-verifier NIZK protocols that require only 2-5 times the computation of evaluating the circuit in the clear (following an input-independent preprocessing phase), and where the prover communicates roughly 2 field elements per multiplication gate, or roughly 1 element in the random oracle model with a modestly higher computation cost. On the theoretical side, our LPZK systems give rise to the first linear interactive proofs (Bitansky et al., TCC 2013) that are zero knowledge against a malicious verifier. We then apply LPZK towards simplifying and improving recent constructions of reusable non-interactive secure computation (NISC) from VOLE (Chase et al., Crypto 2019). As an application, we give concretely efficient and reusable NISC protocols over VOLE for bounded inner product, where the sender&#x27;s input vector should have a bounded $L_2$-norm.

  匹配依据：MPC: secure computation

  </details>

- **DPaSE: Distributed Password-Authenticated Symmetric Encryption**
  2020-11-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1443)
  Poulami Das, Julia Hesse, Anja Lehmann

  <details><summary>摘要 / Abstract</summary>

  Cloud storage is becoming increasingly popular among end users that outsource their personal data to services such as Dropbox or Google Drive. For security, uploaded data should ideally be encrypted under a key that is controlled and only known by the user. Current solutions that support user-centric encryption either require the user to manage strong cryptographic keys, or derive keys from weak passwords. While the former has massive usability issues and requires secure storage by the user, the latter approach is more convenient but offers only little security since encrypted data is susceptible to offline attacks. The recent concept of password-authenticated secret-sharing (PASS) enables users to securely derive strong keys from weak passwords by leveraging a distributed server setup, and has been considered a promising step towards secure and usable encryption. However, using PASS for encryption is not as suitable as originally thought: it only considers the (re)construction of a \emph{single}, static key -- whereas practical encryption will require the management of \emph{many}, object-specific keys. Using a dedicated PASS instance for every key makes the solution vulnerable against online attacks, inherently leaks access patterns to the servers and poses the risk of permanent data loss when an incorrect password is used at encryption. We therefore propose a new protocol that directly targets the problem of boostrapping encryption from a single password: distributed password-authenticated symmetric encryption DPaSE. DPaSE offers strong security and usability, such as protecting the user&#x27;s password against online and offline attacks, and ensuring message privacy and ciphertext integrity as long as at least one server is honest. We formally define the desired security properties in the UC framework and propose a provably secure instantiation. The core of our protocol is a new type of Oblivious Pseudorandom Function (OPRF) that allows to extend a previous partially-blind query with a follow-up request and will be used to blindly carry over passwords across evaluations and avoid online attacks. Our (proof-of-concept) implementation of DPaSE uses $10$ exponentiations at the user, $4$ exponentiations and $2$ pairings at each server, and has a server throughput of $76$ account creations and $37$ (user authentication followed by) encryptions per second, when run between a user and 2-10 servers.

  匹配依据：MPC: secret sharing

  </details>

- **Consensus with Preserved Privacy against Neighbor Collusion**
  2020-11-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.09646)
  Silun Zhang, Thomas Ohlson Timoudas, Munther Dahleh

  <details><summary>摘要 / Abstract</summary>

  This paper proposes a privacy-preserving algorithm to solve the average consensus problem based on Shamir&#x27;s secret sharing scheme, in which a network of agents reach an agreement on their states without exposing their individual state until an agreement is reached. Unlike other methods, the proposed algorithm renders the network resistant to the collusion of any given number of neighbors (even with all neighbors&#x27; colluding). Another virtue of this work is that such a method can protect the network consensus procedure from eavesdropping.

  匹配依据：MPC: secret sharing

  </details>

- **Multi-copy adaptive local discrimination: Strongest possible two-qubit nonlocal bases**
  2020-11-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.09287)
  Manik Banik, Tamal Guha, Mir Alimuddin, Guruprasad Kar, Saronath Halder, Some Sankar Bhattacharya

  <details><summary>摘要 / Abstract</summary>

  Ensembles of composite quantum states can exhibit nonlocal behaviour in the sense that their optimal discrimination may require global operations. Such an ensemble containing N pairwise orthogonal pure states, however, can always be perfectly distinguished under adaptive local scheme if (N-1) copies of the state are available. In this letter, we provide examples of orthonormal bases in two-qubit Hilbert space whose adaptive discrimination require 3 copies of the state. For this composite system we analyze multi-copy adaptive local distinguishability of orthogonal ensembles in full generality which in turn assigns varying nonlocal strength to different such ensembles. We also come up with ensembles whose discrimination under adaptive separable scheme require less number of copies than adaptive local schemes. Our construction finds important application in multipartite secret sharing tasks and indicates towards an intriguing super-additivity phenomenon for locally accessible information.

  匹配依据：MPC: secret sharing

  </details>

- **Asymmetric Private Set Intersection with Applications to Contact Tracing and Private Vertical Federated Machine Learning**
  2020-11-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.09350)
  Nick Angelou, Ayoub Benaissa, Bogdan Cebere, William Clark, Adam James Hall, Michael A. Hoeh, Daniel Liu, Pavlos Papadopoulos, Robin Roehm, Robert Sandmann, Phillipp Schoppmann, Tom Titcombe

  <details><summary>摘要 / Abstract</summary>

  We present a multi-language, cross-platform, open-source library for asymmetric private set intersection (PSI) and PSI-Cardinality (PSI-C). Our protocol combines traditional DDH-based PSI and PSI-C protocols with compression based on Bloom filters that helps reduce communication in the asymmetric setting. Currently, our library supports C++, C, Go, WebAssembly, JavaScript, Python, and Rust, and runs on both traditional hardware (x86) and browser targets. We further apply our library to two use cases: (i) a privacy-preserving contact tracing protocol that is compatible with existing approaches, but improves their privacy guarantees, and (ii) privacy-preserving machine learning on vertically partitioned data.

  匹配依据：MPC: private set intersection

  </details>

- **Secured Distributed Algorithms Without Hardness Assumptions**
  2020-11-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.07863)
  Leonid Barenboim, Harel Levin

  <details><summary>摘要 / Abstract</summary>

  We study algorithms in the distributed message-passing model that produce secured output, for an input graph $G$. Specifically, each vertex computes its part in the output, the entire output is correct, but each vertex cannot discover the output of other vertices, with a certain probability. This is motivated by high-performance processors that are embedded nowadays in a large variety of devices. In such situations, it no longer makes sense, and in many cases it is not feasible, to leave the whole processing task to a single computer or even a group of central computers. As the extensive research in the distributed algorithms field yielded efficient decentralized algorithms for many classic problems, the discussion about the security of distributed algorithms was somewhat neglected. Nevertheless, many protocols and algorithms were devised in the research area of secure multi-party computation problem (MPC or SMC). However, the notions and terminology of these protocols are quite different than in classic distributed algorithms. As a consequence, the focus in those protocols was to work for every function $f$ at the expense of increasing the round complexity, or the necessity of several computational assumptions. In this work, we present a novel approach, which rather than turning existing algorithms into secure ones, identifies and develops those algorithms that are inherently secure (which means they do not require any further constructions). This approach yields efficient secure algorithms for various locality problems, such as coloring, network decomposition, forest decomposition, and a variety of additional labeling problems. Remarkably, our approach does not require any hardness assumption, but only a private randomness generator in each vertex. This is in contrast to previously known techniques in this setting that are based on public-key encryption schemes.

  匹配依据：MPC: secure multi party computation

  </details>

- **The Resiliency of MPC with Low Interaction: The Benefit of Making Errors**
  2020-11-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1419)
  Benny Applebaum, Eliran Kachlon, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  We study information-theoretic secure multiparty protocols that achieve full security, including guaranteed output delivery, at the presence of an active adversary that corrupts a constant fraction of the parties. It is known that 2 rounds are insufficient for such protocols even when the adversary corrupts only two parties (Gennaro, Ishai, Kushilevitz, and Rabin; Crypto 2002), and that perfect protocols can be implemented in $3$ rounds as long as the adversary corrupts less than a quarter of the parties (Applebaum , Brakerski, and Tsabary; Eurocrypt, 2019). Furthermore, it was recently shown that the quarter threshold is tight for any 3-round \emph{perfectly-secure} protocol (Applebaum, Kachlon, and Patra; FOCS 2020). Nevertheless, one may still hope to achieve a better-than-quarter threshold at the expense of allowing some negligible correctness errors and/or statistical deviations in the security. Our main results show that this is indeed the case. Every function can be computed by 3-round protocols with \emph{statistical} security as long as the adversary corrupts less than a third of the parties. Moreover, we show that any better resiliency threshold requires $4$ rounds. Our protocol is computationally inefficient and has an exponential dependency in the circuit&#x27;s depth $d$ and in the number of parties $n$. We show that this overhead can be avoided by relaxing security to computational, assuming the existence of a non-interactive commitment (NICOM). Previous 3-round computational protocols were based on stronger public-key assumptions. When instantiated with statistically-hiding NICOM, our protocol provides \emph{everlasting statistical} security, i.e., it is secure against adversaries that are computationally unlimited \emph{after} the protocol execution. To prove these results, we introduce a new hybrid model that allows for 2-round protocols with a linear resiliency threshold. Here too we prove that, for perfect protocols, the best achievable resiliency is $n/4$, whereas statistical protocols can achieve a threshold of $n/3$. In the plain model, we also construct the first 2-round $n/3$-statistical verifiable secret sharing that supports second-level sharing and prove a matching lower-bound, extending the results of Patra, Choudhary, Rabin, and Rangan (Crypto 2009). Overall, our results refine the differences between statistical and perfect models of security and show that there are efficiency gaps even for thresholds that are realizable in both models.

  匹配依据：MPC: secret sharing

  </details>

- **Secure Graph Database Search with Oblivious Filter**
  2020-11-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1415)
  Jamie Cui, Chaochao Chen, Alex X. Liu, Li Wang

  <details><summary>摘要 / Abstract</summary>

  With the emerging popularity of cloud computing, the problem of how to query over cryptographically-protected data has been widely studied. However, most existing works focus on querying protected relational databases, few work has shown interests in graph databases. In this paper, we first investigate and summarize two single-instruction queries, namely Graph Pattern Matching (GPM) and Graph Navigation (GN). Then we follow their design intuitions and leverage secure Multi-Party Computation (MPC) to implement their functionalities in a privacy-preserving manner. Moreover, we propose a general framework for processing multi-instruction query on secret-shared graph databases and present a novel cryptographic primitive Oblivious Filter (OF) as a core building block. Nevertheless, we formalize the problem of OF and present its constructions using homomorphic encryption. Finally, we conduct an empirical study to evaluate the efficiency of our proposed OF protocol.

  匹配依据：MPC: secure multi party computation

  </details>

- **Revisiting Fairness in MPC: Polynomial Number of Parties and General Adversarial Structures**
  2020-11-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1430)
  Dana Dachman-Soled

  <details><summary>摘要 / Abstract</summary>

  We investigate fairness in secure multiparty computation when the number of parties $n = poly(\lambda)$ grows polynomially in the security parameter, $\lambda$. Prior to this work, efficient protocols achieving fairness with no honest majority and polynomial number of parties were known only for the AND and OR functionalities (Gordon and Katz, TCC&#x27;09). We show the following: --We first consider symmetric Boolean functions $F : \{0,1\}^n \to \{0,1\}$, where the underlying function $f_{n/2,n/2}: \{0, \ldots, n/2\} \times \{0, \ldots, n/2\} \to \{0,1\}$ can be computed fairly and efficiently in the $2$-party setting. We present an efficient protocol for any such $F$ tolerating $n/2$ or fewer corruptions, for $n = poly(\lambda)$ number of parties. --We present an efficient protocol for $n$-party majority tolerating $n/2+1$ or fewer corruptions, for $n = poly(\lambda)$ number of parties. The construction extends to $n/2+c$ or fewer corruptions, for constant $c$. --We extend both of the above results to more general types of adversarial structures and present instantiations of non-threshold adversarial structures of these types. These instantiations are obtained via constructions of projective planes and combinatorial designs.

  匹配依据：MPC: secure multiparty computation

  </details>

- **On Computational Shortcuts for Information-Theoretic PIR**
  2020-11-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1429)
  Matthew M. Hong, Yuval Ishai, Victor I. Kolobov, Russell W. F. Lai

  <details><summary>摘要 / Abstract</summary>

  Information-theoretic private information retrieval (PIR) schemes have attractive concrete efficiency features. However, in the standard PIR model, the computational complexity of the servers must scale linearly with the database size. We study the possibility of bypassing this limitation in the case where the database is a truth table of a &quot;simple&quot; function, such as a union of (multi-dimensional) intervals or convex shapes, a decision tree, or a DNF formula. This question is motivated by the goal of obtaining lightweight homomorphic secret sharing (HSS) schemes and secure multiparty computation (MPC) protocols for the corresponding families. We obtain both positive and negative results. For &quot;first-generation&quot; PIR schemes based on Reed-Muller codes, we obtain computational shortcuts for the above function families, with the exception of DNF formulas for which we show a (conditional) hardness result. For &quot;third-generation&quot; PIR schemes based on matching vectors, we obtain stronger hardness results that apply to all of the above families. Our positive results yield new information-theoretic HSS schemes and MPC protocols with attractive efficiency features for simple but useful function families. Our negative results establish new connections between information-theoretic cryptography and fine-grained complexity.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Correlated Pseudorandom Functions from Variable-Density LPN**
  2020-11-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1417)
  Elette Boyle, Geoffroy Couteau, Niv Gilboa, Yuval Ishai, Lisa Kohl, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  Correlated secret randomness is a useful resource for many cryptographic applications. We initiate the study of pseudorandom correlation functions (PCFs) that offer the ability to securely generate virtually unbounded sources of correlated randomness using only local computation. Concretely, a PCF is a keyed function $F_k$ such that for a suitable joint key distribution $(k_0,k_1)$, the outputs $(f_{k_0}(x),f_{k_1}(x))$ are indistinguishable from instances of a given target correlation. An essential security requirement is that indistinguishability hold not only for outsiders, who observe the pairs of outputs, but also for insiders who know one of the two keys. We present efficient constructions of PCFs for a broad class of useful correlations, including oblivious transfer and multiplication triple correlations, from a variable-density variant of the Learning Parity with Noise assumption (VDLPN). We also present several cryptographic applications that motivate our efficient PCF constructions. The VDLPN assumption is independently motivated by two additional applications. First, different flavors of this assumption give rise to weak pseudorandom function candidates in depth-2 $\mathsf{AC}^0[\oplus]$ that can be conjectured to have subexponential security, matching the best known learning algorithms for this class. This is contrasted with the quasipolynomial security of previous (higher-depth) $\mathsf{AC}^0[\oplus]$ candidates. We support our conjectures by proving resilience to several classes of attacks. Second, VDLPN implies simple constructions of pseudorandom generators and weak pseudorandom functions with security against XOR related-key attacks.

  匹配依据：MPC: oblivious transfer

  </details>

- **Revisiting Secure Computation Using Functional Encryption: Opportunities and Research Directions**
  2020-11-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.06191)
  Runhua Xu, James Joshi

  <details><summary>摘要 / Abstract</summary>

  Increasing incidents of security compromises and privacy leakage have raised serious privacy concerns related to cyberspace. Such privacy concerns have been instrumental in the creation of several regulations and acts to restrict the availability and use of privacy-sensitive data. The secure computation problem, initially and formally introduced as secure two-party computation by Andrew Yao in 1986, has been the focus of intense research in academia because of its fundamental role in building many of the existing privacy-preserving approaches. Most of the existing secure computation solutions rely on garbled-circuits and homomorphic encryption techniques to tackle secure computation issues, including efficiency and security guarantees. However, it is still challenging to adopt these secure computation approaches in emerging compute-intensive and data-intensive applications such as emerging machine learning solutions. Recently proposed functional encryption scheme has shown its promise as an underlying secure computation foundation in recent privacy-preserving machine learning approaches proposed. This paper revisits the secure computation problem using emerging and promising functional encryption techniques and presents a comprehensive study. We first briefly summarize existing conventional secure computation approaches built on garbled-circuits, oblivious transfer, and homomorphic encryption techniques. Then, we elaborate on the unique characteristics and challenges of emerging functional encryption based secure computation approaches and outline several research directions.

  匹配依据：MPC: garbled circuits, oblivious transfer, secure computation, secure two party computation

  </details>

- **Photonic implementation of quantum information masking**
  2020-11-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.04963)
  Zheng-Hao Liu, Xiao-Bin Liang, Kai Sun, Qiang Li, Yu Meng, Mu Yang, Bo Li, Jing-Ling Chen, Jin-Shi Xu, Chuan-Feng Li, Guang-Can Guo

  <details><summary>摘要 / Abstract</summary>

  Masking of quantum information spreads it over nonlocal correlations and hides it from the subsystems. It is known that no operation can simultaneously mask all pure states [Phys. Rev. Lett. 120, 230501 (2018)], so in what sense is quantum information masking useful? Here, we extend the definition of quantum information masking to general mixed states, and show that the resource of maskable quantum states are far more abundant than the no-go theorem seemingly suggests. Geometrically, the simultaneously maskable states lays on hyperdisks in the state hypersphere, and strictly contain the broadcastable states. We devise a photonic quantum information masking machine using time-correlated photons to experimentally investigate the properties of qubit masking, and demonstrate the transfer of quantum information into bipartite correlations and its faithful retrieval. The versatile masking machine has decent extensibility, and may be applicable to quantum secret sharing and fault-tolerant quantum communication. Our results provide some insights on the comprehension and potential application of quantum information masking.

  匹配依据：MPC: secret sharing

  </details>

- **Efficient Privacy Preserving Logistic Regression Inference and Training**
  2020-11-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1396)
  Kyoohyung Han, Jinhyuck Jeong, Jung Hoon Sohn, Yongha Son

  <details><summary>摘要 / Abstract</summary>

  Recently, privacy-preserving logistic regression techniques on distributed data among several data owners drew attention in terms of their applicability in federated learning environment. Many of them have been built upon cryptographic primitives such as secure multiparty computations(MPC) and homomorphic encryptions(HE) to protect the privacy of data. The secure multiparty computation provides fast and secure unit operations for arithmetic and bit operations but they often does not scale with large data well enough due to large computation cost and communication overhead. From recent works, many HE primitives provide their operations in a batch sense so that the technique can be an appropriate choice in a big data environment. However computationally expensive operations such as ciphertext slot rotation or refreshment(so called bootstrapping) and large public key size are hurdles that hamper widespread of the technique in the industry-level environment. In this paper, we provide a new hybrid approach of a privacy-preserving logistic regression training and a inference, which utilizes both MPC and HE techniques to provide efficient and scalable solution while minimizing needs of key management and complexity of computation in encrypted state. Utilizing batch sense properties of HE, we present a method to securely compute multiplications of vectors and matrices using one HE multiplication, compared to the naive approach which requires linear number of multiplications regarding to the size of input data. We also show how we used a 2-party additive secret sharing scheme to control noises of expensive HE operations such as bootstrapping efficiently.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Decentralized Multi-Authority ABE for DNFs from LWE**
  2020-11-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1386)
  Pratish Datta, Ilan Komargodski, Brent Waters

  <details><summary>摘要 / Abstract</summary>

  We construct the first decentralized multi-authority attribute-based encryption (MA-ABE) scheme for a non-trivial class of access policies whose security is based (in the random oracle model) solely on the Learning With Errors (LWE) assumption. The supported access policies are ones described by DNF formulas. All previous constructions of MA-ABE schemes supporting any non-trivial class of access policies were proven secure (in the random oracle model) assuming various assumptions on bilinear maps. In our system, any party can become an authority and there is no requirement for any global coordination other than the creation of an initial set of common reference parameters. A party can simply act as a standard ABE authority by creating a public key and issuing private keys to different users that reflect their attributes. A user can encrypt data in terms of any DNF formulas over attributes issued from any chosen set of authorities. Finally, our system does not require any central authority. In terms of efficiency, when instantiating the scheme with a global bound $s$ on the size of access policies, the sizes of public keys, secret keys, and ciphertexts, all grow with $s$. Technically, we develop new tools for building ciphertext-policy ABE (CP-ABE) schemes using LWE. Along the way, we construct the first provably secure CP-ABE scheme supporting access policies in $\mathsf{NC}^1$ that avoids the generic universal-circuit-based key-policy to ciphertext-policy transformation. In particular, our construction relies on linear secret sharing schemes with new properties and in some sense is more similar to CP-ABE schemes that rely on bilinear maps. While our CP-ABE construction is not more efficient than existing ones, it is conceptually intriguing and further we show how to extend it to get the MA-ABE scheme described above.

  匹配依据：MPC: secret sharing

  </details>

- **A Survey of ECDSA Threshold Signing**
  2020-11-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1390)
  Jean-Philippe Aumasson, Adrian Hamelink, Omer Shlomovits

  <details><summary>摘要 / Abstract</summary>

  Threshold signing research progressed a lot in the last three years, especially for ECDSA, which is less MPC-friendly than Schnorr-based signatures such as EdDSA. This progress was mainly driven by blockchain applications, and boosted by breakthrough results concurrently published by Lindell and by Gennaro &amp; Goldfeder. Since then, several research teams published threshold signature schemes with different features, design trade-offs, building blocks, and proof techniques. Furthermore, threshold signing is now deployed within major organizations to protect large amounts of digital assets. Researchers and practitioners therefore need a clear view of the research state, of the relative merits of the protocols available, and of the open problems, in particular those that would address &quot;real-world&quot; challenges. This survey therefore proposes to (1) describe threshold signing and its building blocks in a general, unified way, based on the extended arithmetic black-box formalism (ABB+); (2) review the state-of-the-art threshold signing protocols, highlighting their unique properties and comparing them in terms of security assurance and performance, based on criteria relevant in practice; (3) review the main open-source implementations available.

  匹配依据：MPC: mpc (context)

  </details>

- **Using Five Cards to Encode Each Integer in $\\mathbb{Z}/6\\mathbb{Z}$**
  2020-11-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.02980)
  Suthee Ruangwises

  <details><summary>摘要 / Abstract</summary>

  Research in secure multi-party computation using a deck of playing cards, often called card-based cryptography, dates back to 1989 when Den Boer introduced the &quot;five-card trick&quot; to compute the logical AND function. Since then, many protocols to compute different functions have been developed. In this paper, we propose a new encoding scheme that uses five cards to encode each integer in $\mathbb{Z}/6\mathbb{Z}$. Using this encoding scheme, we develop protocols that can copy a commitment with 13 cards, add two integers with 10 cards, and multiply two integers with 14 cards. All of our protocols are the currently best known protocols in terms of the required number of cards. Our encoding scheme can be generalized to encode integers in $\mathbb{Z}/n\mathbb{Z}$ for other values of $n$ as well.

  匹配依据：MPC: secure multi party computation

  </details>

- **Quantum randomized encoding, verification of quantum computing, no-cloning, and blind quantum computing**
  2020-11-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.03141)
  Tomoyuki Morimae

  <details><summary>摘要 / Abstract</summary>

  Randomized encoding is a powerful cryptographic primitive with various applications such as secure multiparty computation, verifiable computation, parallel cryptography, and complexity lower-bounds. Intuitively, randomized encoding $\hat{f}$ of a function $f$ is another function such that $f(x)$ can be recovered from $\hat{f}(x)$, and nothing except for $f(x)$ is leaked from $\hat{f}(x)$. Its quantum version, quantum randomized encoding, has been introduced recently [Brakerski and Yuen, arXiv:2006.01085]. Intuitively, quantum randomized encoding $\hat{F}$ of a quantum operation $F$ is another quantum operation such that, for any quantum state $ρ$, $F(ρ)$ can be recovered from $\hat{F}(ρ)$, and nothing except for $F(ρ)$ is leaked from $\hat{F}(ρ)$. In this paper, we show that if quantum randomized encoding of BB84 state generations is possible with an encoding operation $E$, then a two-round verification of quantum computing is possible with a classical verifier who can additionally do the operation $E$. One of the most important goals in the field of the verification of quantum computing is to construct a verification protocol with a verifier as classical as possible. This result therefore demonstrates a potential application of quantum randomized encoding to the verification of quantum computing: if we can find a good quantum randomized encoding (in terms of the encoding complexity), then we can construct a good verification protocol of quantum computing. We, however, also show that too good quantum randomized encoding is impossible: if quantum randomized encoding with a classical encoding operation is possible, then the no-cloning is violated. We finally consider a natural modification of blind quantum computing protocols in such a way that the server gets the output like quantum randomized encoding. We show that the modified protocol is not secure.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Entangled state generation via quantum walks with multiple coins**
  2020-11-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.01643)
  Meng Li, Yun Shang

  <details><summary>摘要 / Abstract</summary>

  Generation of entangled state is of paramount importance both from quantum theoretical foundation and technology applications. Entanglement swapping provides an efficient method to generate entanglement in quantum communication protocols. However, perfect Bell measurements for qudits, the key to entanglement swapping, have been proven impossible to achieve by using only linear elements and particle detectors. To avoid this bottleneck, we propose a novel scheme to generate entangled state including two-qubit entangled state, two-qudit entangled state, three-qubit GHZ state and three-qudit GHZ state between several designate parties via the model of quantum walks with multiple coins. Then we conduct experimental realization of Bell state and three-qubit GHZ state between several designate parties on IBM quantum platform and the result has high fidelity by preforming quantum tomography. In the end, we give a practical application of our scheme in multiparty quantum secret sharing.

  匹配依据：MPC: secret sharing

  </details>

- **A novel group based cryptosystem based on electromagnetic rotor machine**
  2020-11-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.01803)
  Ashish Kumar, N S Raghava

  <details><summary>摘要 / Abstract</summary>

  In this paper, an algorithm is aimed to make a cryptosystem for gray level images based on voice features, secret sharing scheme and electromagnetic rotor machine. Here, Shamir secret sharing (k n) threshold scheme is used to secure a key along with voice features of (n k) users. Keystream is molded by coefficients of a voice sample, using this key stream, rotor machines rotating cylinders positions are initialized and internal wiring is decided by pseudo random number of Henon chaotic map, where initial seed for chaotic system is chosen from keystream. And furthermore, shares of key stream are distributed among users. Speech processing is fused with electromagnetic machine to provide authentication as well as group based encryption. Perceptual linear predication (PLP) coefficients are utilized for formation of secret key. Simulation experiments and statistical analysis demonstrate that the proposed algorithm is sensitive to initial secret keystream, entropy, mean value analysis and histogram of the encrypted image is admirable. Hence, the proposed scheme is resistible to any vulnerable situation.

  匹配依据：MPC: secret sharing

  </details>

- **A Secure Two-Party Computation Protocol for Intersection Detection between Two Convex Hulls**
  2020-10-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.00319)
  Amirahmad Chapnevis, Babak Sadeghiyan

  <details><summary>摘要 / Abstract</summary>

  Intersection detection between three-dimensional bodies has various applications in computer graphics, video game development, robotics as well as military industries. In some respects, entities do not want to disclose sensitive information about themselves, including their location. In this paper, we present a secure two-party protocol to determine the existence of an intersection between entities. The protocol presented in this paper allows for intersection detection in three-dimensional spaces in geometry. Our approach is to use an intersecting plane between two spaces to determine their separation or intersection. For this purpose, we introduce a computational geometry protocol to determine the existence of an intersecting plane. In this paper, we first use the Minkowski difference to reduce the two-space problem into one-space. Then, the separating set is obtained and the separation of two shapes is determined based on the inclusion of the center point. We then secure the protocol by modifying the separating set computation method as a privacy-preserver and changing the Minkowski difference method to achieve this goal. The proposed protocol applies to any form of convex three-dimensional shape. The experiments successfully found a secure protocol for intersection detection between two convex hulls in geometrical shapes such as the pyramid and cuboid.

  匹配依据：MPC: secure two party computation

  </details>

- **SodsMPC: FSM based Anonymous and Private Quantum-safe Smart Contracts**
  2020-10-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1346)
  Shlomi Dolev, Ziyu Wang

  <details><summary>摘要 / Abstract</summary>

  SodsMPC is a quantum-safe smart contract system. SodsMPC permissioned servers (verification nodes) execute contracts by secure multi-party computation (MPC) protocols. MPC ensures the contract execution correctness while trivially keeping the \textit{data privacy}. Moreover, SodsMPC accomplishes the contract \textit{business logic privacy} while protecting the contract user \textit{anonymous identity} simultaneously. We express the logic of a contract by a finite state machine (FSM). A state transition of the FSM is represented by a \textit{blind polynomial} with secret-shared coefficients. When using MPC to compute this blind polynomial, the contract business logic privacy is obtained. These coefficients which control the logic are binary secret shares. We also propose a base conversion method among binary and integer secret shares by MPC. Our contract anonymity comes from the ``mixing-then-contract&#x27;&#x27; paradigm. The online phase of the SodsMPC mixing is a multiplication between a preprocessed permutation matrix and an input vector in the form of secret sharing, which accomplishes a fully randomized shuffle of the inputs and keeps the secret share form for the following contract execution. All SodsMPC components, including a verifiable secret sharing scheme, are quantum-safe, asynchronous, coping with $t&lt;n/3$ compromised servers, and robust (tolerates Byzantine servers) in both preprocessing and online phases.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **The Min-entropy as a Resource for One-Shot Private State Transfer, Quantum Masking and State Transition**
  2020-10-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.14796)
  Seok Hyung Lie, Seongjeon Choi, Hyunseok Jeong

  <details><summary>摘要 / Abstract</summary>

  We give an operational meaning to the min-entropy of a quantum state as a resource measure for various interconnected tasks. In particular, we show that the min-entropy without smoothing measures the amount of quantum information that can be hidden or encoded perfectly in the one-shot setting when the quantum state is used as a randomness/correlation source. First, we show that the min-entropy of entanglement of a pure bipartite state is the maximum number of qubits privately transferable when the state is used as quantum one-time pad. Then, through the equivalence of quantum secret sharing(QSS)-like protocols, it is also shown that the min-entropy of a quantum state is the maximum number of qubits that can be masked when the state is used as a randomness source for a quantum masking process. Consequently we show that the min-entropy of a quantum state is the half of the size of quantum state it can catalytically dephase.This gives a necessary and sufficient condition for catalysts for state transition processes.

  匹配依据：MPC: secret sharing

  </details>

- **Revolutionizing Medical Data Sharing Using Advanced Privacy Enhancing Technologies: Technical, Legal and Ethical Synthesis**
  2020-10-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.14445)
  James Scheibner, Jean Louis Raisaro, Juan Ramón Troncoso-Pastoriza, Marcello Ienca, Jacques Fellay, Effy Vayena, Jean-Pierre Hubaux

  <details><summary>摘要 / Abstract</summary>

  Multisite medical data sharing is critical in modern clinical practice and medical research. The challenge is to conduct data sharing that preserves individual privacy and data usability. The shortcomings of traditional privacy-enhancing technologies mean that institutions rely on bespoke data sharing contracts. These contracts increase the inefficiency of data sharing and may disincentivize important clinical treatment and medical research. This paper provides a synthesis between two novel advanced privacy enhancing technologies (PETs): Homomorphic Encryption and Secure Multiparty Computation (defined together as Multiparty Homomorphic Encryption or MHE). These PETs provide a mathematical guarantee of privacy, with MHE providing a performance advantage over separately using HE or SMC. We argue MHE fulfills legal requirements for medical data sharing under the General Data Protection Regulation (GDPR) which has set a global benchmark for data protection. Specifically, the data processed and shared using MHE can be considered anonymized data. We explain how MHE can reduce the reliance on customized contractual measures between institutions. The proposed approach can accelerate the pace of medical research whilst offering additional incentives for healthcare and research institutes to employ common data interoperability standards.

  匹配依据：MPC: secure multiparty computation

  </details>

- **2FE: Two-Factor Encryption for Cloud Storage**
  2020-10-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.14417)
  Anders Dalskov, Daniele Lain, Enis Ulqinaku, Kari Kostiainen, Srdjan Capkun

  <details><summary>摘要 / Abstract</summary>

  Encrypted cloud storage services are steadily increasing in popularity, with many commercial solutions currently available. In such solutions, the cloud storage is trusted for data availability, but not for confidentiality. Additionally, the user&#x27;s device is considered secure, and the user is expected to behave correctly. We argue that such assumptions are not met in reality: e.g., users routinely forget passwords and fail to make backups, and users&#x27; devices get stolen or become infected with malware. Therefore, we consider a more extensive threat model, where users&#x27; devices are susceptible to attacks and common human errors are possible. Given this model, we analyze 10 popular commercial services and show that none of them provides good confidentiality and data availability. Motivated by the lack of adequate solutions in the market, we design a novel scheme called Two-Factor Encryption (2FE) that draws inspiration from two-factor authentication and turns file encryption and decryption into an interactive process where two user devices, like a laptop and a smartphone, must interact. 2FE provides strong confidentiality and availability guarantees, as it withstands compromised cloud storage, one stolen or compromised user device at a time, and various human errors. 2FE achieves this by leveraging secret sharing with additional techniques such as oblivious pseudorandom functions and zero-knowledge proofs. We evaluate 2FE experimentally and show that its performance overhead is small. Finally, we explain how our approach can be adapted to other related use cases such as cryptocurrency wallets.

  匹配依据：MPC: secret sharing

  </details>

- **Protocols for creating and distilling multipartite GHZ states with Bell pairs**
  2020-10-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.12259)
  Sébastian de Bone, Runsheng Ouyang, Kenneth Goodenough, David Elkouss

  <details><summary>摘要 / Abstract</summary>

  The distribution of high-quality Greenberger-Horne-Zeilinger (GHZ) states is at the heart of many quantum communication tasks, ranging from extending the baseline of telescopes to secret sharing. They also play an important role in error-correction architectures for distributed quantum computation, where Bell pairs can be leveraged to create an entangled network of quantum computers. We investigate the creation and distillation of GHZ states out of non-perfect Bell pairs over quantum networks. In particular, we introduce a heuristic dynamic programming algorithm to optimize over a large class of protocols that create and purify GHZ states. All protocols considered use a common framework based on measurements of non-local stabilizer operators of the target state (i.e., the GHZ state), where each non-local measurement consumes another (non-perfect) entangled state as a resource. The new protocols outperform previous proposals for scenarios without decoherence and local gate noise. Furthermore, the algorithms can be applied for finding protocols for any number of parties and any number of entangled pairs involved.

  匹配依据：MPC: secret sharing

  </details>

- **CSI-RAShi: Distributed key generation for CSIDH**
  2020-10-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1323)
  Ward Beullens, Lucas Disson, Robi Pedersen, Frederik Vercauteren

  <details><summary>摘要 / Abstract</summary>

  We present an honest-majority Distributed Key Generation protocol (DKG) based on Shamir&#x27;s $(k,n)$-threshold secret sharing in the setting of Very Hard Homogenous Spaces (VHHS). DKG&#x27;s in the DLOG setting use Pedersen commitments, for which there is no known analogue in the VHHS setting. As a replacement, we introduce a new primitive called piecewise verifiable proofs, which allow a prover to prove that a list of NP-statements is valid with respect to a common witness, and such that the different statements can be verified individually. Our protocol is robust and actively secure in the Quantum Random Oracle Model. For $n$ participants, the total runtime of our protocol is\break $2+\lambda+n(1+4\lambda)$ group action evaluations, where $\lambda$ is the underlying security parameter, and is thus independent of the threshold $k$. When instantiated with CSIDH-512, this amounts to approximately $4.5+18n$ seconds.

  匹配依据：MPC: secret sharing

  </details>

- **CryptoGRU: Low Latency Privacy-Preserving Text Analysis With GRU**
  2020-10-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.11796)
  Bo Feng, Qian Lou, Lei Jiang, Geoffrey C. Fox

  <details><summary>摘要 / Abstract</summary>

  Billions of text analysis requests containing private emails, personal text messages, and sensitive online reviews, are processed by recurrent neural networks (RNNs) deployed on public clouds every day. Although prior secure networks combine homomorphic encryption (HE) and garbled circuit (GC) to preserve users&#x27; privacy, naively adopting the HE and GC hybrid technique to implement RNNs suffers from long inference latency due to slow activation functions. In this paper, we present a HE and GC hybrid gated recurrent unit (GRU) network, CryptoGRU, for low-latency secure inferences. CryptoGRU replaces computationally expensive GC-based $tanh$ with fast GC-based $ReLU$, and then quantizes $sigmoid$ and $ReLU$ with a smaller bit length to accelerate activations in a GRU. We evaluate CryptoGRU with multiple GRU models trained on 4 public datasets. Experimental results show CryptoGRU achieves top-notch accuracy and improves the secure inference latency by up to $138\times$ over one of state-of-the-art secure networks on the Penn Treebank dataset.

  匹配依据：MPC: garbled circuit

  </details>

- **Private Weighted Sum Aggregation**
  2020-10-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.10640)
  Andreea B. Alexandru, George J. Pappas

  <details><summary>摘要 / Abstract</summary>

  As large amounts of data are circulated both from users to a cloud server and between users, there is a critical need for privately aggregating the shared data. This paper considers the problem of private weighted sum aggregation with secret weights, where an aggregator wants to compute the weighted sum of the local data of some agents. Depending on the privacy requirements posed on the weights, there are different secure multi-party computation schemes exploiting the information structure. First, when each agent has a local private value and a local private weight, we review private sum aggregation schemes. Second, we discuss how to extend the previous schemes for when the agents have a local private value, but the aggregator holds the corresponding weights. Third, we treat a more general case where the agents have their local private values, but the weights are known neither by the agents nor by the aggregator; they are generated by a system operator, who wants to keep them private. We give a solution where aggregator obliviousness is achieved, even under collusion between the participants, and we show how to obtain a more efficient communication and computation strategy for multi-dimensional data, by batching the data into fewer ciphertexts. Finally, we implement our schemes and discuss the numerical results and efficiency improvements.

  匹配依据：MPC: secure multi party computation

  </details>

- **Multiparty Cardinality Testing for Threshold Private Set Intersection**
  2020-10-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1307)
  Pedro Branco, Nico Döttling, Sihang Pu

  <details><summary>摘要 / Abstract</summary>

  Threshold Private Set Intersection (PSI) allows multiple parties to compute the intersection of their input sets if and only if the intersection is larger than $n-t$, where $n$ is the size of the sets and $t$ is some threshold. The main appeal of this primitive is that, in contrast to standard PSI, known upper-bounds on the communication complexity only depend on the threshold $t$ and not on the sizes of the input sets. Current Threshold PSI protocols split themselves into two components: A Cardinality Testing phase, where parties decide if the intersection is larger than some threshold; and a PSI phase, where the intersection is computed. The main source of inefficiency of Threshold PSI is the former part. In this work, we present a new Cardinality Testing protocol that allows $N$ parties to check if the intersection of their input sets is larger than $n-t$. The protocol incurs in $\tilde{ \mathcal{O}} (Nt^2)$ communication complexity. We thus obtain a Threshold PSI scheme for $N$ parties with communication complexity $\tilde{ \mathcal{O}}(Nt^2)$.

  匹配依据：MPC: private set intersection

  </details>

- **Virtual Secure Platform: A Five-Stage Pipeline Processor over TFHE**
  2020-10-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.09410)
  Kotaro Matsuoka, Ryotaro Banno, Naoki Matsumoto, Takashi Sato, Song Bian

  <details><summary>摘要 / Abstract</summary>

  We present Virtual Secure Platform (VSP), the first comprehensive platform that implements a multi-opcode general-purpose sequential processor over Fully Homomorphic Encryption (FHE) for Secure Multi-Party Computation (SMPC). VSP protects both the data and functions on which the data are evaluated from the adversary in a secure computation offloading situation like cloud computing. We proposed a complete processor architecture with a five-stage pipeline, which improves the performance of the VSP by providing more parallelism in circuit evaluation. In addition, we also designed a custom Instruction Set Architecture (ISA) to reduce the gate count of our processor, along with an entire set of toolchains to ensure that arbitrary C programs can be compiled into our custom ISA. In order to speed up instruction evaluation over VSP, CMUX Memory based ROM and RAM constructions over FHE are also proposed. Our experiments show that both the pipelined architecture and the CMUX Memory technique are effective in improving the performance of the proposed processor. We provide an open-source implementation of VSP which achieves a per-instruction latency of less than 1 second. We demonstrate that compared to the best existing processor over FHE, our implementation runs nearly 1,600$\times$ faster.

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **Privacy-preserving Data Sharing on Vertically Partitioned Data**
  2020-10-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.09293)
  Razane Tajeddine, Joonas Jälkö, Samuel Kaski, Antti Honkela

  <details><summary>摘要 / Abstract</summary>

  In this work, we introduce a differentially private method for generating synthetic data from vertically partitioned data, \emph{i.e.}, where data of the same individuals is distributed across multiple data holders or parties. We present a differentially privacy stochastic gradient descent (DP-SGD) algorithm to train a mixture model over such partitioned data using variational inference. We modify a secure multiparty computation (MPC) framework to combine MPC with differential privacy (DP), in order to use differentially private MPC effectively to learn a probabilistic generative model under DP on such vertically partitioned data. Assuming the mixture components contain no dependencies across different parties, the objective function can be factorized into a sum of products of the contributions calculated by the parties. Finally, MPC is used to compute the aggregate between the different contributions. Moreover, we rigorously define the privacy guarantees with respect to the different players in the system. To demonstrate the accuracy of our method, we run our algorithm on the Adult dataset from the UCI machine learning repository, where we obtain comparable results to the non-partitioned case.

  匹配依据：MPC: secure multiparty computation

  </details>

- **From Distributed Machine Learning To Federated Learning: In The View Of Data Privacy And Security**
  2020-10-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.09258)
  Sheng Shen, Tianqing Zhu, Di Wu, Wei Wang, Wanlei Zhou

  <details><summary>摘要 / Abstract</summary>

  Federated learning is an improved version of distributed machine learning that further offloads operations which would usually be performed by a central server. The server becomes more like an assistant coordinating clients to work together rather than micro-managing the workforce as in traditional DML. One of the greatest advantages of federated learning is the additional privacy and security guarantees it affords. Federated learning architecture relies on smart devices, such as smartphones and IoT sensors, that collect and process their own data, so sensitive information never has to leave the client device. Rather, clients train a sub-model locally and send an encrypted update to the central server for aggregation into the global model. These strong privacy guarantees make federated learning an attractive choice in a world where data breaches and information theft are common and serious threats. This survey outlines the landscape and latest developments in data privacy and security for federated learning. We identify the different mechanisms used to provide privacy and security, such as differential privacy, secure multi-party computation and secure aggregation. We also survey the current attack models, identifying the areas of vulnerability and the strategies adversaries use to penetrate federated systems. The survey concludes with a discussion on the open challenges and potential directions of future work in this increasingly popular learning paradigm.

  匹配依据：MPC: secure multi party computation

  </details>

- **Secure Two-Party Quantum Computation Over Classical Channels**
  2020-10-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.07925) · [IACR ePrint](https://eprint.iacr.org/2020/1286)
  Michele Ciampi, Alexandru Cojocaru, Elham Kashefi, Atul Mantri

  <details><summary>摘要 / Abstract</summary>

  Secure two-party computation considers the problem of two parties computing a joint function of their private inputs without revealing anything beyond the output of the computation. In this work, we take the first steps towards understanding the setting where: 1) the two parties (Alice and Bob) can communicate only via a classical channel, 2) the input of Bob is quantum, and 3) the input of Alice is classical. Our first result indicates that in this setting it is in general impossible to realize a two-party quantum functionality with black-box simulation in the case of malicious quantum adversaries. In particular, we show that the existence of a secure quantum computing protocol that relies only on classical channels would contradict the quantum no-cloning argument. We circumvent this impossibility following three different approaches. The first is by considering a weaker security notion called one-sided simulation security. This notion protects the input of one party (the quantum Bob) in the standard simulation-based sense and protects the privacy of the other party&#x27;s input (the classical Alice). We show how to realize a protocol that satisfies this notion relying on the learning with errors assumption. The second way to circumvent the impossibility result, while at the same time providing standard simulation-based security also against a malicious Bob, is by assuming that the quantum input has an efficient classical representation. Finally, we focus our attention on the class of zero-knowledge functionalities and provide a compiler that takes as input a classical proof of quantum knowledge (PoQK) protocol for a QMA relation R (a classical PoQK is a PoQK that can be verified by a classical verifier) and outputs a zero-knowledge PoQK for R that can be verified by classical parties. The direct implication of our result is that Mahadev’s protocol for classical verification of quantum computations (FOCS’18) can be turned into a zero-knowledge proof of quantum knowledge with classical verifiers. To the best of our knowledge, we are the first to instantiate such a primitive.

  匹配依据：MPC: secure two party computation

  </details>

- **Efficient Composable Oblivious Transfer from CDH in the Global Random Oracle Model**
  2020-10-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1291)
  Bernardo David, Rafael Dowsley

  <details><summary>摘要 / Abstract</summary>

  Oblivious Transfer (OT) is a fundamental cryptographic protocol that finds a number of applications, in particular, as an essential building block for two-party and multi-party computation. We construct the first universally composable (UC) protocol for oblivious transfer secure against active static adversaries based on the Computational Diffie-Hellman (CDH) assumption. Our protocol is proven secure in the observable Global Random Oracle model. We start by constructing a protocol that realizes an OT functionality with a selective failure issue, but shown to be sufficient to instantiate efficient OT extension protocols. In terms of complexity, this protocol only requires the computation of 6 modular exponentiations and the communication of 5 group elements, five binary strings of security parameter length, and two binary strings of message length. Finally, we lift this weak construction to obtain a protocol that realizes the standard OT functionality (without any selective failures) at an additional cost of computing 9 modular exponentiations and communicating 4 group elements, four binary strings of security parameter length and two binary strings of message length. As an intermediate step before constructing our CDH based protocols, we design generic OT protocols from any OW-CPA secure public-key encryption scheme with certain properties, which could potentially be instantiated from more assumptions other than CDH.

  匹配依据：MPC: multi party computation, oblivious transfer

  </details>

- **Barrington Plays Cards: The Complexity of Card-based Protocols**
  2020-10-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.08445)
  Pavel Dvořák, Michal Koucký

  <details><summary>摘要 / Abstract</summary>

  In this paper we study the computational complexity of functions that have efficient card-based protocols. Card-based protocols were proposed by den Boer [EUROCRYPT &#x27;89] as a means for secure two-party computation. Our contribution is two-fold: We classify a large class of protocols with respect to the computational complexity of functions they compute, and we propose other encodings of inputs which require fewer cards than the usual 2-card representation.

  匹配依据：MPC: secure two party computation

  </details>

- **Secret Sharing from Correlated Gaussian Random Variables and Public Communication**
  2020-10-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.07536)
  Vidhi Rana, Remi A. Chou, Hyuck Kwon

  <details><summary>摘要 / Abstract</summary>

  In this paper, we study an information-theoretic secret sharing problem, where a dealer distributes shares of a secret among a set of participants under the following constraints: (i) authorized sets of users can recover the secret by pooling their shares, and (ii) non-authorized sets of colluding users cannot learn any information about the secret. We assume that the dealer and participants observe the realizations of correlated Gaussian random variables and that the dealer can communicate with participants through a one-way, authenticated, rate-limited, and public channel. Unlike traditional secret sharing protocols, in our setting, no perfectly secure channel is needed between the dealer and the participants. Our main result is a closed-form characterization of the fundamental trade-off between secret rate and public communication rate.

  匹配依据：MPC: secret sharing

  </details>

- **PrivaLog: a privacy-aware logic programming language**
  2020-10-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.07057)
  Joosep Jääger, Alisa Pankova

  <details><summary>摘要 / Abstract</summary>

  Logic Programming (LP) is a subcategory of declarative programming that is considered to be relatively simple for non-programmers. LP developers focus on describing facts and rules of a logical derivation, and do not need to think about the algorithms actually implementing the derivation. Secure multiparty computation (MPC) is a cryptographic technology that allows to perform computation on private data without actually seeing the data. In this paper, we bring together the notions of MPC and LP, allowing users to write privacy-preserving applications in logic programming language.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Lightweight Mediated Semi-Quantum Secret Sharing Protocol**
  2020-10-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.06911)
  Chia-Wei Tsai, Zong-Liang Zhang, Bo-Cheng Jian, Yao-Chung Chang

  <details><summary>摘要 / Abstract</summary>

  Due to the exiting semi-quantum secret sharing protocol have two challenges including (1) the dealer must be the quantum user, and (2) the classical users must equip with the Trojan Horse detectors, this study wants to propose a novel mediate semi-quantum secret sharing (MSQSS) protocol to let a classical dealer can share his/her secrets to the classical agents with the help of a dishonest third-party (TP). The proposed MSQSS protocol adopts the one-way quantum communication and thus it is free from the Trojan Horse attacks. Furthermore, the security analysis is given for proving that the proposed protocol can be against the collective attack. Comparing to the exiting SQSS protocols, the proposed MSQSS protocol is more lightweight and more practical.

  匹配依据：MPC: secret sharing

  </details>

- **Asymptotically Good Multiplicative LSSS over Galois Rings and Applications to MPC over Z/p^k Z**
  2020-10-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1256)
  Mark Abspoel, Ronald Cramer, Ivan Damgård, Daniel Escudero, Matthieu Rambaud, Chaoping Xing, Chen Yuan

  <details><summary>摘要 / Abstract</summary>

  We study information-theoretic multiparty computation (MPC) protocols over rings $\mathbb{Z}/p^k \mathbb{Z}$ that have good asymptotic communication complexity for a large number of players. An important ingredient for such protocols is arithmetic secret sharing, i.e., linear secret-sharing schemes with multiplicative properties. The standard way to obtain these over fields is with a family of linear codes $C$, such that $C$, $C^\perp$ and $C^2$ are asymptotically good (strongly multiplicative). For our purposes here it suffices if the square code $C^2$ is not the whole space, i.e., has codimension at least 1 (multiplicative). Our approach is to lift such a family of codes defined over a finite field $\mathbb F$ to a Galois ring, which is a local ring that has $\mathbb F$ as its residue field and that contains $\mathbb{Z}/p^k \mathbb{Z}$ as a subring, and thus enables arithmetic that is compatible with both structures. Although arbitrary lifts preserve the distance and dual distance of a code, as we demonstrate with a counterexample, the multiplicative property is not preserved. We work around this issue by showing a dedicated lift that preserves \emph{self-orthogonality} (as well as distance and dual distance), for $p \geq 3$. Self-orthogonal codes are multiplicative, therefore we can use existing results of asymptotically good self-dual codes over fields to obtain arithmetic secret sharing over Galois rings. For $p = 2$ we obtain multiplicativity by using existing techniques of secret-sharing using both $C$ and $C^\perp$, incurring a constant overhead. As a result, we obtain asymptotically good arithmetic secret-sharing schemes over Galois rings. With these schemes in hand, we extend existing field-based MPC protocols to obtain MPC over $\mathbb{Z}/p^k \mathbb{Z}$, in the setting of a submaximal adversary corrupting less than a fraction $1/2 - \varepsilon$ of the players, where $\varepsilon &gt; 0$ is arbitrarily small. We consider 3 different corruption models. For passive and active security with abort, our protocols communicate $O(n)$ bits per multiplication. For full security with guaranteed output delivery we use a preprocessing model and get $O(n)$ bits per multiplication in the online phase and $O(n \log n)$ bits per multiplication in the offline phase. Thus, we obtain true linear bit complexities, without the common assumption that the ring size depends on the number of players.

  匹配依据：MPC: multiparty computation, secret sharing

  </details>

- **CrypTFlow2: Practical 2-Party Secure Inference**
  2020-10-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.06457) · [IACR ePrint](https://eprint.iacr.org/2020/1002)
  Deevashwer Rathee, Mayank Rathee, Nishant Kumar, Nishanth Chandran, Divya Gupta, Aseem Rastogi, Rahul Sharma

  <details><summary>摘要 / Abstract</summary>

  We present CrypTFlow2, a cryptographic framework for secure inference over realistic Deep Neural Networks (DNNs) using secure 2-party computation. CrypTFlow2 protocols are both correct -- i.e., their outputs are bitwise equivalent to the cleartext execution -- and efficient -- they outperform the state-of-the-art protocols in both latency and scale. At the core of CrypTFlow2, we have new 2PC protocols for secure comparison and division, designed carefully to balance round and communication complexity for secure inference tasks. Using CrypTFlow2, we present the first secure inference over ImageNet-scale DNNs like ResNet50 and DenseNet121. These DNNs are at least an order of magnitude larger than those considered in the prior work of 2-party DNN inference. Even on the benchmarks considered by prior work, CrypTFlow2 requires an order of magnitude less communication and 20x-30x less time than the state-of-the-art.

  匹配依据：MPC: secure 2 party computation

  </details>

- **Differentially Private Secure Multi-Party Computation for Federated Learning in Financial Applications**
  2020-10-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.05867)
  David Byrd, Antigoni Polychroniadou

  <details><summary>摘要 / Abstract</summary>

  Federated Learning enables a population of clients, working with a trusted server, to collaboratively learn a shared machine learning model while keeping each client&#x27;s data within its own local systems. This reduces the risk of exposing sensitive data, but it is still possible to reverse engineer information about a client&#x27;s private data set from communicated model parameters. Most federated learning systems therefore use differential privacy to introduce noise to the parameters. This adds uncertainty to any attempt to reveal private client data, but also reduces the accuracy of the shared model, limiting the useful scale of privacy-preserving noise. A system can further reduce the coordinating server&#x27;s ability to recover private client information, without additional accuracy loss, by also including secure multiparty computation. An approach combining both techniques is especially relevant to financial firms as it allows new possibilities for collaborative learning without exposing sensitive client data. This could produce more accurate models for important tasks like optimal trade execution, credit origination, or fraud detection. The key contributions of this paper are: We present a privacy-preserving federated learning protocol to a non-specialist audience, demonstrate it using logistic regression on a real-world credit card fraud data set, and evaluate it using an open-source simulation platform which we have adapted for the development of federated learning systems.

  匹配依据：MPC: secure multi party computation, secure multiparty computation

  </details>

- **Bankrupting Sybil Despite Churn**
  2020-10-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.06834)
  Diksha Gupta, Jared Saia, Maxwell Young

  <details><summary>摘要 / Abstract</summary>

  A Sybil attack occurs when an adversary controls multiple identifiers (IDs) in a system. Limiting the number of Sybil (bad) IDs to a minority is critical to the use of well-established tools for tolerating malicious behavior, such as Byzantine agreement and secure multiparty computation. A popular technique for enforcing a Sybil minority is resource burning: the verifiable consumption of a network resource, such as computational power, bandwidth, or memory. Unfortunately, typical defenses based on resource burning require non-Sybil (good) IDs to consume at least as many resources as the adversary. Additionally, they have a high resource burning cost, even when the system membership is relatively stable. Here, we present a new Sybil defense, ERGO, that guarantees (1) there is always a minority of bad IDs; and (2) when the system is under significant attack, the good IDs consume asymptotically less resources than the bad. In particular, for churn rate that can vary exponentially, the resource burning rate for good IDs under ERGO is O(\sqrt{TJ} + J), where T is the resource burning rate of the adversary, and J is the join rate of good IDs. We show this resource burning rate is asymptotically optimal for a large class of algorithms. We empirically evaluate ERGO alongside prior Sybil defenses. Additionally, we show that ERGO can be combined with machine learning techniques for classifying Sybil IDs, while preserving its theoretical guarantees. Based on our experiments comparing ERGO with two previous Sybil defenses, ERGO improves on the amount of resource burning relative to the adversary by up to 2 orders of magnitude without machine learning, and up to 3 orders of magnitude using machine learning.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Voting-based Approaches For Differentially Private Federated Learning**
  2020-10-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.04851)
  Yuqing Zhu, Xiang Yu, Yi-Hsuan Tsai, Francesco Pittaluga, Masoud Faraki, Manmohan chandraker, Yu-Xiang Wang

  <details><summary>摘要 / Abstract</summary>

  Differentially Private Federated Learning (DPFL) is an emerging field with many applications. Gradient averaging based DPFL methods require costly communication rounds and hardly work with large-capacity models, due to the explicit dimension dependence in its added noise. In this work, inspired by knowledge transfer non-federated privacy learning from Papernot et al.(2017; 2018), we design two new DPFL schemes, by voting among the data labels returned from each local model, instead of averaging the gradients, which avoids the dimension dependence and significantly reduces the communication cost. Theoretically, by applying secure multi-party computation, we could exponentially amplify the (data-dependent) privacy guarantees when the margin of the voting scores are large. Extensive experiments show that our approaches significantly improve the privacy-utility trade-off over the state-of-the-arts in DPFL.

  匹配依据：MPC: secure multi party computation

  </details>

- **Random-index PIR and Applications**
  2020-10-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1248)
  Craig Gentry, Shai Halevi, Bernardo Magri, Jesper Buus Nielsen, Sophia Yakoubov

  <details><summary>摘要 / Abstract</summary>

  Private information retrieval (PIR) lets a client retrieve an entry from a database without the server learning which entry was retrieved. Here we study a weaker variant that we call \emph{random-index PIR} (RPIR), where the retrieved index is an \emph{output} rather than an input of the protocol, and is chosen at random. RPIR is clearly weaker than PIR, but it suffices for some interesting applications and may be realized more efficiently than full-blown PIR. We report here on two lines of work, both tied to RPIR but otherwise largely unrelated. The first line of work studies RPIR as a primitive on its own. Perhaps surprisingly, we show that RPIR is in fact equivalent to PIR when there are no restrictions on the number of communication rounds. On the other hand, RPIR can be implemented in a ``noninteractive&#x27;&#x27; setting (with pre-processing), which is clearly impossible for PIR. For two-server RPIR we even show a truly noninteractive solution, offering information-theoretic security without any pre-processing. The other line of work, which was the original motivation for our work, uses RPIR to improve on the recent work of Benhamouda \etal (TCC&#x27;20) for maintaining secret values on public blockchains. Their solution depends on a method for selecting many random public keys from a PKI while hiding most of the selected keys from an adversary. However, the method they proposed is vulnerable to a double-dipping attack, limiting its resilience. Here we observe that a RPIR protocol, where the client is implemented via secure MPC, can eliminate that vulnerability. We thus get a secrets-on-blockchain protocol (and more generally large-scale MPC), resilient to any fraction $f &lt; 1/2$ of corrupted parties, resolving the main open problem left from the work of Benhamouda \etal As the client in this solution is implemented via secure MPC, it really brings home the need to make it as efficient as possible. We thus strive to explore whatever efficiency gains we can get by using RPIR rather than PIR. We achieve more gains by using \emph{batch RPIR} where multiple indexes are retrieved at once. Lastly, we observe that this application can make do with a weaker security guarantee than full RPIR, and show that this weaker variant can be realized even more efficiently. We discuss one protocol in particular, that may be attractive for practical implementations.

  匹配依据：MPC: mpc (context)

  </details>

- **BVOT: Self-Tallying Boardroom Voting with Oblivious Transfer**
  2020-10-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.02421) · [IACR ePrint](https://eprint.iacr.org/2020/1233)
  Farid Javani, Alan T. Sherman

  <details><summary>摘要 / Abstract</summary>

  A boardroom election is an election with a small number of voters carried out with public communications. We present BVOT, a self-tallying boardroom voting protocol with ballot secrecy, fairness (no tally information is available before the polls close), and dispute-freeness (voters can observe that all voters correctly followed the protocol). BVOT works by using a multiparty threshold homomorphic encryption system in which each candidate is associated with a masked unique prime. Each voter engages in an oblivious transfer with an untrusted distributor: the voter selects the index of a prime associated with a candidate and receives the selected prime in masked form. The voter then casts their vote by encrypting their masked prime and broadcasting it to everyone. The distributor does not learn the voter&#x27;s choice, and no one learns the mapping between primes and candidates until the audit phase. By hiding the mapping between primes and candidates, BVOT provides voters with insufficient information to carry out effective cheating. The threshold feature prevents anyone from computing any partial tally---until everyone has voted. Multiplying all votes, their decryption shares, and the unmasking factor yields a product of the primes each raised to the number of votes received. In contrast to some existing boardroom voting protocols, BVOT does not rely on any zero-knowledge proof; instead, it uses oblivious transfer to assure ballot secrecy and correct vote casting. Also, BVOT can handle multiple candidates in one election. BVOT prevents cheating by hiding crucial information: an attempt to increase the tally of one candidate might increase the tally of another candidate. After all votes are cast, any party can tally the votes.

  匹配依据：MPC: oblivious transfer

  </details>

- **Adversarial Level Agreements for Two-Party Protocols**
  2020-10-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1249)
  Marilyn George, Seny Kamara

  <details><summary>摘要 / Abstract</summary>

  Adversaries in cryptography have traditionally been modeled as either semi-honest or malicious. Over the years, however, several lines of work have investigated the design of cryptographic protocols against rational adversaries. The most well-known example are covert adversaries in secure computation (Aumann &amp; Lindell, TCC &#x27;07) which are adversaries that wish to deviate from the protocol but without being detected. To protect against such adversaries, protocols secure in the covert model guarantee that deviations are detected with probability at least $\varepsilon$ which is known as the deterrence factor. In this work, we initiate the study of contracts in cryptographic protocol design. We show how to design, use and analyze contracts between parties for the purpose of incentivizing honest behavior from rational adversaries. We refer to such contracts as adversarial level agreements (ALA). The framework we propose can result in more efficient protocols and can enforce deterrence in covert protocols; meaning that one can guarantee that a given deterrence factor will deter the adversary instead of assuming it. We show how to apply our framework to two-party protocols, including secure two-party computation (2PC) and proofs of storage (PoS). In the 2PC case, we integrate ALAs to publicly-verifiable covert protocols and show, through a game-theoretic analysis, how to set the parameters of the ALA to guarantee honest behavior. We do the same in the setting of PoS which are two-party protocols that allow a client to efficiently verify the integrity of a file stored in the cloud.

  匹配依据：MPC: secure computation, secure two party computation

  </details>

- **Synchronous Constructive Cryptography**
  2020-10-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1226)
  Chen-Da Liu-Zhang, Ueli Maurer

  <details><summary>摘要 / Abstract</summary>

  This paper proposes a simple synchronous composable security framework as an instantiation of the Constructive Cryptography framework, aiming to capture minimally, without unnecessary artefacts, exactly what is needed to state synchronous security guarantees. The objects of study are specifications (i.e., sets) of systems, and traditional security properties like consistency and validity can naturally be understood as specifications, thus unifying composable and property-based definitions. The framework&#x27;s simplicity is in contrast to current composable frameworks for synchronous computation which are built on top of an asynchronous framework (e.g. the UC framework), thus not only inheriting artefacts and complex features used to handle asynchronous communication, but adding additional overhead to capture synchronous communication. As a second, independent contribution we demonstrate how secure (synchronous) multi-party computation protocols can be understood as constructing a computer that allows a set of parties to perform an arbitrary, on-going computation. An interesting aspect is that the instructions of the computation need not be fixed before the protocol starts but can also be determined during an on-going computation, possibly depending on previous outputs.

  匹配依据：MPC: multi party computation

  </details>

- **Non-Committing Encryption with Constant Ciphertext Expansion from Standard Assumptions**
  2020-10-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1210)
  Yusuke Yoshida, Fuyuki Kitagawa, Keita Xagawa, Keisuke Tanaka

  <details><summary>摘要 / Abstract</summary>

  Non-committing encryption (NCE) introduced by Canetti et al. (STOC &#x27;96) is a central tool to achieve multi-party computation protocols secure in the adaptive setting. Recently, Yoshida et al. (ASIACRYPT &#x27;19) proposed an NCE scheme based on the hardness of the DDH problem, which has ciphertext expansion $\mathcal{O}(\log\lambda)$ and public-key expansion $\mathcal{O}(\lambda^2)$. In this work, we improve their result and propose a methodology to construct an NCE scheme that achieves constant ciphertext expansion.Our methodology can be instantiated from the DDH assumption and the LWE assumption. When instantiated from the LWE assumption, the public-key expansion is $\lambda\cdot\mathsf{poly}(\log\lambda)$. They are the first NCE schemes satisfying constant ciphertext expansion without using iO or common reference strings. Along the way, we define a weak notion of NCE, which satisfies only weak forms of correctness and security.We show how to amplify such a weak NCE scheme into a full-fledged one using wiretap codes with a new security property.

  匹配依据：MPC: multi party computation

  </details>

- **$X$-Secure $T$-Private Federated Submodel Learning with Elastic Dropout Resilience**
  2020-10-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.01059)
  Zhuqing Jia, Syed A. Jafar

  <details><summary>摘要 / Abstract</summary>

  Motivated by recent interest in federated submodel learning, this work explores the fundamental problem of privately reading from and writing to a database comprised of $K$ files (submodels) that are stored across $N$ distributed servers according to an $X$-secure threshold secret sharing scheme. One after another, various users wish to retrieve their desired file, locally process the information and then update the file in the distributed database while keeping the identity of their desired file private from any set of up to $T$ colluding servers. The availability of servers changes over time, so elastic dropout resilience is required. The main contribution of this work is an adaptive scheme, called ACSA-RW, that takes advantage of all currently available servers to reduce its communication costs, fully updates the database after each write operation even though the database is only partially accessible due to server dropouts, and ensures a memoryless operation of the network in the sense that the storage structure is preserved and future users may remain oblivious of the past history of server dropouts. The ACSA-RW construction builds upon CSA codes that were originally introduced for XSTPIR and have been shown to be natural solutions for secure distributed matrix multiplication problems. ACSA-RW achieves the desired private read and write functionality with elastic dropout resilience, matches the best results for private-read from PIR literature, improves significantly upon available baselines for private-write, reveals a striking symmetry between upload and download costs, and exploits redundant storage dimensions to accommodate arbitrary read and write dropout servers up to certain threshold values. It also answers in the affirmative an open question by Kairouz et al. by exploiting synergistic gains from the joint design of private read and write operations.

  匹配依据：MPC: secret sharing

  </details>

- **TinyGarble2: Smart, Efficient, and Scalable Yao’s Garble Circuit**
  2020-09-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1181)
  Siam Hussain, Baiyu Li, Farinaz Koushanfar, Rosario Cammarota

  <details><summary>摘要 / Abstract</summary>

  We present TinyGarble2 – a C++ framework for privacy-preserving computation through the Yao’s Garbled Circuit (GC) protocol in both the honest-but-curious and the malicious security models. TinyGarble2 provides a rich library with arithmetic and logic building blocks for developing GC-based secure applications. The framework offers abstractions among three layers: the C++ program, the GC back-end and the Boolean logic representation of the function being computed. TinyGarble2 thus allowing the most optimized versions of all pertinent components. These abstractions, coupled with secure share transfer among the functions make TinyGarble2 the fastest and most memory-efficient GC framework. In addition, the framework provides a library for Convolutional Neural Networks (CNN). Our evaluations show that TinyGarble2 is the fastest among the current end-to-end GC frameworks while also being scalable in terms of memory footprint. Moreover, it performs 18× faster on the CNN LeNet-5 compared to the existing scalable frameworks.

  匹配依据：MPC: garbled circuit

  </details>

- **Optimal Broadcast Encryption from LWE and Pairings in the Standard Model**
  2020-09-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1179)
  Shweta Agrawal, Daniel Wichs, Shota Yamada

  <details><summary>摘要 / Abstract</summary>

  Broadcast Encryption with optimal parameters was a long-standing problem, whose first solution was provided in an elegant work by Boneh, Waters and Zhandry [BWZ14]. However, this work relied on multilinear maps of logarithmic degree, which is not considered a standard assumption. Recently, Agrawal and Yamada [AY20] improved this state of affairs by providing the first construction of optimal broadcast encryption from Bilinear Maps and Learning With Errors (LWE). However, their proof of security was in the generic bilinear group model. In this work, we improve upon their result by providing a new construction and proof in the standard model. In more detail, we rely on the Learning With Errors (LWE) assumption and the Knowledge of OrthogonALity Assumption (KOALA) [BW19] on bilinear groups. Our construction combines three building blocks: a (computational) nearly linear secret sharing scheme with compact shares which we construct from LWE, an inner-product functional encryption scheme with special properties which is constructed from the bilinear Matrix Decision Diffie Hellman (MDDH) assumption, and a certain form of hyperplane obfuscation, which is constructed using the KOALA assumption. While similar to that of Agrawal and Yamada, our construction provides a new understanding of how to decompose the construction into simpler, modular building blocks with concrete and easy-to-understand security requirements for each one. We believe this sheds new light on the requirements for optimal broadcast encryption, which may lead to new constructions in the future.

  匹配依据：MPC: secret sharing

  </details>

- **Constant Ciphertext-Rate Non-Committing Encryption from Standard Assumptions**
  2020-09-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1186)
  Zvika Brakerski, Pedro Branco, Nico Döttling, Sanjam Garg, Giulio Malavolta

  <details><summary>摘要 / Abstract</summary>

  Non-committing encryption (NCE) is a type of public key encryption which comes with the ability to equivocate ciphertexts to encryptions of arbitrary messages, i.e., it allows one to find coins for key generation and encryption which ``explain&#x27;&#x27; a given ciphertext as an encryption of any message. NCE is the cornerstone to construct adaptively secure multiparty computation [Canetti et al. STOC&#x27;96] and can be seen as the quintessential notion of security for public key encryption to realize ideal communication channels. A large body of literature investigates what is the best message-to-ciphertext ratio (i.e., the rate) that one can hope to achieve for NCE. In this work we propose a near complete resolution to this question and we show how to construct NCE with constant rate in the plain model from a variety of assumptions, such as the hardness of the learning with errors (LWE) or the decisional Diffie-Hellman (DDH). Prior to our work, constructing NCE with constant rate required a trusted setup and indistinguishability obfuscation [Canetti et al. ASIACRYPT&#x27;17].

  匹配依据：MPC: secure multiparty computation

  </details>

- **$(t, n)$ Threshold $d$-level quantum secret sharing based on quantum Fourier transformation**
  2020-09-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.14598)
  Sarbani Roy, Sourav Mukhopadhyay

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) is an important branch of secure multiparty quantum computation. Several schemes for $(n, n)$ threshold QSS based on quantum Fourier transformation (QFT) have been proposed. Inspired by the flexibility of $(t, n)$ threshold schemes, Song {\it et al.} (Scientific Reports, 2017) have proposed a $(t, n)$ threshold QSS utilizing $QFT$. Later, Kao and Hwang (arXiv:1803.00216) have identified a loophole in the scheme but have not suggested any remedy. In this present study, we have proposed a $(t, n)$ threshold QSS scheme to share a $d$ dimensional classical secret. This scheme can be implemented using local operations (such as $QFT$, generalized Pauli operators and local measurement) and classical communication. Security of the proposed scheme is described against outsider and participants&#x27; eavesdropping.

  匹配依据：MPC: secret sharing

  </details>

- **STR: Secure Computation on Additive Shares Using the Share-Transform-Reveal Strategy**
  2020-09-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.13153)
  Zhihua Xia, Qi Gu, Wenhao Zhou, Lizhi Xiong, Jian Weng, Neal N. Xiong

  <details><summary>摘要 / Abstract</summary>

  The rapid development of cloud computing has probably benefited each of us. However, the privacy risks brought by untrustworthy cloud servers arise the attention of more and more people and legislatures. In the last two decades, plenty of works seek to outsource various specific tasks while ensuring the security of private data. The tasks to be outsourced are countless; however, the computations involved are similar. In this paper, we construct a series of novel protocols that support the secure computation of various functions on numbers (e.g., the basic elementary functions) and matrices (e.g., the calculation of eigenvectors and eigenvalues) in arbitrary $n\geq 2$ servers. All protocols only require constant rounds of interactions and achieve the low computation complexity. Moreover, the proposed $n$-party protocols ensure the security of private data even though $n-1$ servers collude. The convolutional neural network models are utilized as the case studies to verify the protocols. The theoretical analysis and experimental results demonstrate the correctness, efficiency, and security of the proposed protocols.

  匹配依据：MPC: secure computation

  </details>

- **An optimization problem for continuous submodular functions**
  2020-09-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.12574)
  Laszlo Csirmaz

  <details><summary>摘要 / Abstract</summary>

  Real continuous submodular functions, as a generalization of the corresponding discrete notion to the continuous domain, gained considerable attention recently. The analog notion for entropy functions requires additional properties: a real function defined on the non-negative orthant of $\mathbb R^n$ is entropy-like (EL) if it is submodular, takes zero at zero, non-decreasing, and has the Diminishing Returns property. Motivated by problems concerning the Shannon complexity of multipartite secret sharing, a special case of the following general optimization problem is considered: find the minimal cost of those EL functions which satisfy certain constraints. In our special case the cost of an EL function is the maximal value of the $n$ partial derivatives at zero. Another possibility could be the supremum of the function range. The constraints are specified by a smooth bounded surface $S$ cutting off a downward closed subset. An EL function is feasible if at the internal points of $S$ the left and right partial derivatives of the function differ by at least one. A general lower bound for the minimal cost is given in terms of the normals of the surface $S$. The bound is tight when $S$ is linear. In the two-dimensional case the same bound is tight for convex or concave $S$. It is shown that the optimal EL function is not necessarily unique. The paper concludes with several open problems.

  匹配依据：MPC: secret sharing

  </details>

- **Walnut: A low-trust trigger-action platform**
  2020-09-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.12447)
  Sandy Schoettler, Andrew Thompson, Rakshith Gopalakrishna, Trinabh Gupta

  <details><summary>摘要 / Abstract</summary>

  Trigger-action platforms are a new type of system that connect IoT devices with web services. For example, the popular IFTTT platform can connect Fitbit with Google Calendar to add a bedtime reminder based on sleep history. However, these platforms present confidentiality and integrity risks as they run on public cloud infrastructure and compute over sensitive user data. This paper describes the design, implementation, and evaluation of Walnut, a low-trust trigger-action platform that mimics the functionality of IFTTT, while ensuring confidentiality of data and correctness of computation, at a low resource cost. The key enabler for Walnut is a new two-party secure computation protocol that (i) efficiently performs strings substitutions, which is a common computation in trigger-action platform workloads, and (ii) replicates computation over heterogeneous trusted-hardware machines from different vendors to ensure correctness of computation output as long as one of the machines is not compromised. An evaluation of Walnut demonstrates its plausible deployability and low overhead relative to a non-secure baseline--3.6x in CPU and 4.3x in network for all but a small percentage of programs.

  匹配依据：MPC: secure computation

  </details>

- **Secure Massively Parallel Computation for Dishonest Majority**
  2020-09-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1157)
  Rex Fernando, Ilan Komargodski, Yanyi Liu, Elaine Shi

  <details><summary>摘要 / Abstract</summary>

  This work concerns secure protocols in the massively parallel computation (MPC) model, which is one of the most widely-accepted models for capturing the challenges of writing protocols for the types of parallel computing clusters which have become commonplace today (MapReduce, Hadoop, Spark, etc.). Recently, the work of Chan et al. (ITCS &#x27;20) initiated this study, giving a way to compile any MPC protocol into a secure one in the common random string model, achieving the standard secure multi-party computation definition of security with up to 1/3 of the parties being corrupt. We are interested in achieving security for much more than 1/3 corruptions. To that end, we give two compilers for MPC protocols, which assume a simple public-key infrastructure, and achieve semi-honest security for all-but-one corruptions. Our first compiler assumes hardness of the learning-with-errors (LWE) problem, and works for any MPC protocol with ``short&#x27;&#x27; output---that is, where the output of the protocol can fit into the storage space of one machine, for instance protocols that output a trained machine learning model. Our second compiler works for any MPC protocol (even ones with a long output, such as sorting) but assumes, in addition to LWE, indistinguishability obfuscation and a circular secure variant of threshold FHE. Both protocols allow the attacker to choose corrupted parties based on the trusted setup, an improvement over Chan et al., whose protocol requires that the CRS is chosen independently of the attacker&#x27;s choices.

  匹配依据：MPC: secure multi party computation

  </details>

- **MOTIF: (Almost) Free Branching in GMW via Vector-Scalar Multiplication**
  2020-09-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1175)
  David Heath, Vladimir Kolesnikov, Stanislav Peceny

  <details><summary>摘要 / Abstract</summary>

  MPC functionalities are increasingly specified in high-level languages, where control-flow constructions such as conditional statements are extensively used. Today, concretely efficient MPC protocols are circuit-based and must evaluate all conditional branches at high cost to hide the taken branch. The Goldreich-Micali-Wigderson, or GMW, protocol is a foundational circuit-based technique that realizes MPC for p players and is secure against up to p - 1 semi-honest corruptions. While GMW requires communication rounds proportional to the computed circuit’s depth, it is effective in many natural settings. Our main contribution is MOTIF (Minimizing OTs for IFs), a novel GMW extension that evaluates conditional branches almost for free by amortizing Oblivious Transfers (OTs) across branches. That is, we simultaneously evaluate multiple independent AND gates, one gate from each mutually exclusive branch, by representing them as a single cheap vector-scalar multiplication (VS) gate. For 2PC with b branches, we simultaneously evaluate up to b AND gates using only two 1-out-of-2 OTs of b-bit secrets. This is a factor ~b improvement over the state-of-the-art 2b 1-out-of-2 OTs of 1-bit secrets. Our factor b improvement generalizes to the multiparty setting as well: b AND gates consume only p(p - 1) 1-out-of-2 OTs of b-bit secrets. We implemented our approach and report its performance. For 2PC and a circuit with 16 branches, each comparing two length-65000 bitstrings, MOTIF outperforms standard GMW in terms of communication by ~9.4x. Total wall-clock time is improved by 4.1 - 9.2x depending on network settings. Our work is in the semi-honest model, tolerating all-but-one corruptions.

  匹配依据：MPC: mpc (context)

  </details>

- **A Reversible Data hiding Scheme in Encrypted Domain for Secret Image Sharing based on Chinese Remainder Theorem**
  2020-09-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.08502)
  Yan Ke, Minqing Zhang, Xinpeng Zhang, Jia Liu, Tingting Su, Xiaoyuan Yang

  <details><summary>摘要 / Abstract</summary>

  Reversible data hiding in encrypted domain (RDH-ED) schemes based on symmetric or public key encryption are mainly applied to the security of end-to-end communication. Aimed at providing reliable technical supports for multi-party security scenarios, a separable RDH-ED scheme for secret image sharing based on Chinese remainder theorem (CRT) is presented. In the application of (t, n) secret image sharing, the image is first shared into n different shares of ciphertext. Only when not less than t shares obtained, can the original image be reconstructed. In our scheme, additional data could be embedded into the image shares. To realize data extraction from the image shares and the reconstructed image separably, two data hiding methods are proposed: one is homomorphic difference expansion in encrypted domain (HDE-ED) that supports data extraction from the reconstructed image by utilizing the addition homomorphism of CRT secret sharing; the other is difference expansion in image shares (DE-IS) that supports the data extraction from the marked shares before image reconstruction. Experimental results demonstrate that the proposed scheme could not only maintain the security and the threshold function of secret sharing system, but also obtain a better reversibility and efficiency compared with most existing RDH-ED algorithms. The maximum embedding rate of HDE-ED could reach 0.5000 bits per pixel and the average embedding rate of DE-IS is 0.0545 bits per bit of ciphertext.

  匹配依据：MPC: secret sharing

  </details>

- **Secure Data Sharing With Flow Model**
  2020-09-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.11762)
  Chenwei Wu, Chenzhuang Du, Yang Yuan

  <details><summary>摘要 / Abstract</summary>

  In the classical multi-party computation setting, multiple parties jointly compute a function without revealing their own input data. We consider a variant of this problem, where the input data can be shared for machine learning training purposes, but the data are also encrypted so that they cannot be recovered by other parties. We present a rotation based method using flow model, and theoretically justified its security. We demonstrate the effectiveness of our method in different scenarios, including supervised secure model training, and unsupervised generative model training. Our code is available at https://github.com/ duchenzhuang/flowencrypt.

  匹配依据：MPC: multi party computation

  </details>

- **Pocket Diagnosis: Secure Federated Learning against Poisoning Attack in the Cloud**
  2020-09-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.10918)
  Zhuoran Ma, Jianfeng Ma, Yinbin Miao, Ximeng Liu, Kim-Kwang Raymond Choo, Robert H. Deng

  <details><summary>摘要 / Abstract</summary>

  Federated learning has become prevalent in medical diagnosis due to its effectiveness in training a federated model among multiple health institutions (i.e. Data Islands (DIs)). However, increasingly massive DI-level poisoning attacks have shed light on a vulnerability in federated learning, which inject poisoned data into certain DIs to corrupt the availability of the federated model. Previous works on federated learning have been inadequate in ensuring the privacy of DIs and the availability of the final federated model. In this paper, we design a secure federated learning mechanism with multiple keys to prevent DI-level poisoning attacks for medical diagnosis, called SFPA. Concretely, SFPA provides privacy-preserving random forest-based federated learning by using the multi-key secure computation, which guarantees the confidentiality of DI-related information. Meanwhile, a secure defense strategy over encrypted locally-submitted models is proposed to defense DI-level poisoning attacks. Finally, our formal security analysis and empirical tests on a public cloud platform demonstrate the security and efficiency of SFPA as well as its capability of resisting DI-level poisoning attacks.

  匹配依据：MPC: secure computation

  </details>

- **FastSecAgg: Scalable Secure Aggregation for Privacy-Preserving Federated Learning**
  2020-09-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.11248)
  Swanand Kadhe, Nived Rajaraman, O. Ozan Koyluoglu, Kannan Ramchandran

  <details><summary>摘要 / Abstract</summary>

  Recent attacks on federated learning demonstrate that keeping the training data on clients&#x27; devices does not provide sufficient privacy, as the model parameters shared by clients can leak information about their training data. A &#x27;secure aggregation&#x27; protocol enables the server to aggregate clients&#x27; models in a privacy-preserving manner. However, existing secure aggregation protocols incur high computation/communication costs, especially when the number of model parameters is larger than the number of clients participating in an iteration -- a typical scenario in federated learning. In this paper, we propose a secure aggregation protocol, FastSecAgg, that is efficient in terms of computation and communication, and robust to client dropouts. The main building block of FastSecAgg is a novel multi-secret sharing scheme, FastShare, based on the Fast Fourier Transform (FFT), which may be of independent interest. FastShare is information-theoretically secure, and achieves a trade-off between the number of secrets, privacy threshold, and dropout tolerance. Riding on the capabilities of FastShare, we prove that FastSecAgg is (i) secure against the server colluding with &#x27;any&#x27; subset of some constant fraction (e.g. $\sim10\%$) of the clients in the honest-but-curious setting; and (ii) tolerates dropouts of a &#x27;random&#x27; subset of some constant fraction (e.g. $\sim10\%$) of the clients. FastSecAgg achieves significantly smaller computation cost than existing schemes while achieving the same (orderwise) communication cost. In addition, it guarantees security against adaptive adversaries, which can perform client corruptions dynamically during the execution of the protocol.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy Preserving K-Means Clustering: A Secure Multi-Party Computation Approach**
  2020-09-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.10453)
  Daniel Hurtado Ramírez, J. M. Auñón

  <details><summary>摘要 / Abstract</summary>

  Knowledge discovery is one of the main goals of Artificial Intelligence. This Knowledge is usually stored in databases spread in different environments, being a tedious (or impossible) task to access and extract data from them. To this difficulty we must add that these datasources may contain private data, therefore the information can never leave the source. Privacy Preserving Machine Learning (PPML) helps to overcome this difficulty, employing cryptographic techniques, allowing knowledge discovery while ensuring data privacy. K-means is one of the data mining techniques used in order to discover knowledge, grouping data points in clusters that contain similar features. This paper focuses in Privacy Preserving Machine Learning applied to K-means using recent protocols from the field of criptography. The algorithm is applied to different scenarios where data may be distributed either horizontally or vertically.

  匹配依据：MPC: secure multi party computation

  </details>

- **Succinct and Adaptively Secure ABE for ABP from k-Lin**
  2020-09-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1139)
  Huijia Lin, Ji Luo

  <details><summary>摘要 / Abstract</summary>

  We present *succinct* and *adaptively secure* attribute-based encryption (ABE) schemes for *arithmetic branching programs*, based on k-Lin in pairing groups. Our key-policy ABE scheme has ciphertexts of *constant size*, independent of the length of the attributes, and our ciphertext-policy ABE scheme has secret keys of *constant size*. Our schemes improve upon the recent succinct ABE schemes in [Attrapadung and Tomida, Asiacrypt &#x27;20], which only handle Boolean formulae. All other prior succinct ABE schemes either achieve only selective security or rely on $q$-type assumptions. Our schemes are obtained through a general and modular approach that combines a public-key inner-product functional encryption satisfying a new security notion called gradual simulation security and an information-theoretic randomized encoding scheme called arithmetic key garbling scheme.

  匹配依据：MPC: garbling scheme

  </details>

- **Several classes of minimal binary linear codes violating the Aschikhmin-Barg's bound**
  2020-09-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1131)
  Enes Pasalic, René Rodríguez, Fengrong Zhang, Yongzhuang Wei

  <details><summary>摘要 / Abstract</summary>

  Minimal linear codes are a special class of codes which have important applications in secret sharing and secure two-party computation. These codes are characterized by the property that none of the codewords is covered by some other codeword. Denoting by $w_{min}$ and $w_{max}$ minimal and maximal weight of the codewords respectively, such codes are relatively easy to design when the ratio $w_{min}/w_{max} &gt; 1/2$ (known as Aschikhmin-Barg&#x27;s bound). On the other hand, there are few known classes of minimal codes violating this bound, hence having the property $w_{min}/w_{max} \leq 1/2$. In this article, we provide several explicit classes of minimal binary linear codes violating the Aschikhmin-Barg&#x27;s bound, at the same time achieving a great variety of the ratio $w_{min}/w_{max}$. Our first generic method employs suitable characteristic functions of relatively low weight within the range $[n+1, 2^{n-2}]$. The second approach addresses a specification of characteristic functions covering the weights in $[2^{n-2}+1, 2^{n-2} + 2^{n-3}-1]$ and containing a skewed (removing one element) affine subspace of dimension $n-2$. Finally, we also characterize an infinite family of such codes that utilize the class of so-called root Boolean functions of weight $2^{n-1}-(n-1)$, which are useful in certain hardware testing applications. Consequently, many infinite classes of minimal codes crossing the Aschikhmin-Barg&#x27;s bound, with a wide range of the weight of their characteristic functions, are deduced. In certain cases we also completely specify the weight distribution of resulting codes.

  匹配依据：MPC: secret sharing, secure two party computation

  </details>

- **Secure training of decision trees with continuous attributes**
  2020-09-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1130)
  Mark Abspoel, Daniel Escudero, Nikolaj Volgushev

  <details><summary>摘要 / Abstract</summary>

  We apply multiparty computation (MPC) techniques to show, given a database that is secret-shared among multiple mutually distrustful parties, how the parties may obliviously construct a decision tree based on the secret data. We consider data with continuous attributes (i.e., coming from a large domain), and develop a secure version of a learning algorithm similar to the C4.5 or CART algorithms. Previous MPC-based work only focused on decision tree learning with discrete attributes (De Hoogh et al. 2014). Our starting point is to apply an existing generic MPC protocol to a standard decision tree learning algorithm, which we then optimize in several ways. We exploit the fact that even if we allow the data to have continuous values, which a priori might require fixed or floating point representations, the output of the tree learning algorithm only depends on the relative ordering of the data. By obliviously sorting the data we reduce the number of comparisons needed per node to $O(N \log^2 N)$ from the naive $O(N^2)$, where $N$ is the number of training records in the dataset, thus making the algorithm feasible for larger datasets. This does however introduce a problem when duplicate values occur in the dataset, but we manage to overcome this problem with a relatively cheap subprotocol. We show a procedure to convert a sorting network into a permutation network of smaller complexity, resulting in a round complexity of $O(\log N)$ per layer in the tree. We implement our algorithm in the MP-SPDZ framework and benchmark our implementation for both passive and active three-party computation using arithmetic modulo $2^{64}$. We apply our implementation to a large scale medical dataset of $\approx 290\,000$ rows using random forests, and thus demonstrate practical feasibility of using MPC for privacy-preserving machine learning based on decision trees for large datasets.

  匹配依据：MPC: multiparty computation, three party computation

  </details>

- **MOTION - A Framework for Mixed-Protocol Multi-Party Computation**
  2020-09-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1137)
  Lennart Braun, Daniel Demmler, Thomas Schneider, Oleksandr Tkachenko

  <details><summary>摘要 / Abstract</summary>

  We present MOTION, an efficient and generic open-source framework for mixed-protocol secure multi-party computation (MPC). MOTION is built in a user-friendly, modular, and extensible way, intended to be used as tool in MPC research and to increase adoption of MPC protocols in practice. Our framework incorporates several important engineering decisions such as full communication serialization, which enables MPC over arbitrary messaging interfaces and removes the need of owning network sockets. MOTION also incorporates several novel performance optimizations that improve the communication complexity and latency, e.g., 2x better online round complexity of precomputed correlated Oblivious Transfer (OT). We instantiate our framework with protocols for N parties and security against up to N-1 passive corruptions: the MPC protocols of Goldreich-Micali-Wigderson (GMW) in its arithmetic and Boolean version and OT-based BMR (Ben-Efraim et al., CCS&#x27;16), as well as novel and highly efficient conversions between them, including a non-interactive conversion from BMR to arithmetic GMW. MOTION is highly efficient, which we demonstrate in our experiments. Compared to secure evaluation of AES-128 with N=3 parties in a high-latency network with OT-based BMR, we achieve a 16x better throughput of 16 AES evaluations per second using BMR. With this, we show that BMR is much more competitive than previously assumed. For N=3 parties and full-threshold protocols in a LAN, MOTION is 10x-18x faster than the previous best passively secure implementation from the MP-SPDZ framework, and 190x-586x faster than the actively secure SCALE-MAMBA framework. Finally, we show that our framework is highly efficient for privacy-preserving neural network inference.

  匹配依据：MPC: multi party computation, oblivious transfer, secure evaluation, secure multi party computation

  </details>

- **Let's Tessellate: Tiling for Security Against Advanced Probe and Fault Adversaries**
  2020-09-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1146)
  Siemen Dhooghe, Svetla Nikova

  <details><summary>摘要 / Abstract</summary>

  The wire probe-and-fault models are currently the most used models to provide arguments for side-channel and fault security. However, several practical attacks are not yet covered by these models. This work extends the wire fault model to include more advanced faults such as area faults and permanent faults. Moreover, we show the tile probe-and-fault adversary model from CRYPTO 2018&#x27;s CAPA envelops the extended wire fault model along with known extensions to the probing model such as glitches, transitions, and couplings. In other words, tiled (tessellated) designs offer security guarantees even against advanced probe and fault adversaries. As tiled models use multi-party computation techniques, countermeasures are typically expensive for software/hardware. This work investigates a tiled countermeasure based on the ISW methodology which is shown to perform significantly better than CAPA for practical parameters.

  匹配依据：MPC: multi party computation

  </details>

- **Two and Three-Party Digital Goods Auctions: Scalable Privacy Analysis**
  2020-09-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.09524)
  Patrick Ah-Fat, Michael Huth

  <details><summary>摘要 / Abstract</summary>

  A digital goods auction is a type of auction where potential buyers bid the maximal price that they are willing to pay for a certain item, which a seller can produce at a negligible cost and in unlimited quantity. To maximise her benefits, the aim for the seller is to find the optimal sales price, which every buyer whose bid is not lower will pay. For fairness and privacy purposes, buyers may be concerned about protecting the confidentiality of their bids. Secure Multi-Party Computation is a domain of Cryptography that would allow the seller to compute the optimal sales price while guaranteeing that the bids remain secret. Paradoxically, as a function of the buyers&#x27; bids, the sales price inevitably reveals some private information. Generic frameworks and entropy-based techniques based on Quantitative Information Flow have been developed in order to quantify and restrict those leakages. Due to their combinatorial nature, these techniques do not scale to large input spaces. In this work, we aim at scaling those privacy analyses to large input spaces in the particular case of digital goods auctions. We derive closed-form formulas for the posterior min-entropy of private inputs in two and three-party auctions, which enables us to effectively quantify the information leaks for arbitrarily large input spaces. We also provide supportive experimental evidence that enables us to formulate a conjecture that would allow us to extend our results to any number of parties.

  匹配依据：MPC: secure multi party computation

  </details>

- **Towards Efficiency-Preserving Round Compression in MPC: Do fewer rounds mean more computation?**
  2020-09-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1100)
  Prabhanjan Ananth, Arka Rai Choudhuri, Aarushi Goel, Abhishek Jain

  <details><summary>摘要 / Abstract</summary>

  Reducing the rounds of interaction in secure multiparty computation (MPC) protocols has been the topic of study of many works. One popular approach to reduce rounds is to construct *round compression compilers*. A round compression compiler is one that takes a highly interactive protocol and transforms it into a protocol with far fewer rounds. The design of round compression compilers has traditionally focused on preserving the security properties of the underlying protocol and in particular, not much attention has been given towards preserving their computational and communication efficiency. Indeed, the recent round compression compilers that yield round-optimal MPC protocols incur large computational and communication overhead. In this work, we initiate the study of *efficiency-preserving* round compression compilers, i.e. compilers that translate the efficiency benefits of the underlying highly interactive protocols to the fewer round setting. Focusing on the honest majority setting (with near-optimal corruption threshold $\frac{1}{2} - \varepsilon$, for any $\varepsilon &gt; 0$), we devise a new compiler that yields two round (i.e., round optimal) semi-honest MPC with similar communication efficiency as the underlying (arbitrary round) protocol. By applying our compiler on the most efficient known MPC protocols, we obtain a two-round semi-honest protocol based on one-way functions, with total communication (and per-party computation) cost $\widetilde{O}(s+n^4)$ -- a significant improvement over prior two-round protocols with cost $\widetilde{O}(n^\tau s+n^{\tau+1}d)$, where $\tau\geq 2$, $s$ is the size of the circuit computing the function and $d$ the corresponding depth. Our result can also be extended to handle malicious adversaries, either using stronger assumptions in the public key infrastructure (PKI) model, or in the plain model using an extra round. An artifact of our approach is that the resultant protocol is ``unbalanced&#x27;&#x27; in the amount of computation performed by different parties. We give evidence that this is *necessary* in our setting. Our impossibility result makes novel use of the ``MPC-in-the-head&quot; paradigm which has typically been used to demonstrate feasibility results.

  匹配依据：MPC: secure multiparty computation

  </details>

- **The Round Complexity of Secure Computation Against Covert Adversaries**
  2020-09-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1092)
  Arka Rai Choudhuri, Vipul Goyal, Abhishek Jain

  <details><summary>摘要 / Abstract</summary>

  We investigate the exact round complexity of secure multiparty computation (MPC) against *covert* adversaries who may attempt to cheat, but do not wish to be caught doing so. Covert adversaries lie in between semi-honest adversaries who follow protocol specification and malicious adversaries who may deviate arbitrarily. Recently, two round protocols for semi-honest MPC and four round protocols for malicious-secure MPC were constructed, both of which are optimal. While these results can be viewed as constituting two end points of a security spectrum, we investigate the design of protocols that potentially span the spectrum. Our main result is an MPC protocol against covert adversaries with variable round complexity: when the detection probability is set to the lowest setting, our protocol requires two rounds and offers same security as semi-honest MPC. By increasing the detecting probability, we can increase the security guarantees, with round complexity five in the extreme case. The security of our protocol is based on standard cryptographic assumptions. We supplement our positive result with a negative result, ruling out *strict* three round protocols with respect to black-box simulation.

  匹配依据：MPC: secure computation, secure multiparty computation

  </details>

- **Privacy-Preserving Image Retrieval Based on Additive Secret Sharing**
  2020-09-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.06893)
  Zhihua Xia, Qi Gu, Lizhi Xiong, Wenhao Zhou, Jian Weng

  <details><summary>摘要 / Abstract</summary>

  The rapid growth of digital images motivates individuals and organizations to upload their images to the cloud server. To preserve privacy, image owners would prefer to encrypt the images before uploading, but it would strongly limit the efficient usage of images. Plenty of existing schemes on privacy-preserving Content-Based Image Retrieval (PPCBIR) try to seek the balance between security and retrieval ability. However, compared to the advanced technologies in CBIR like Convolutional Neural Network (CNN), the existing PPCBIR schemes are far deficient in both accuracy and efficiency. With more cloud service providers, the collaborative secure image retrieval service provided by multiple cloud servers becomes possible. In this paper, inspired by additive secret sharing technology, we propose a series of additive secure computing protocols on numbers and matrices with better efficiency, and then show their application in PPCBIR. Specifically, we extract CNN features, decrease the dimension of features and build the index securely with the help of our protocols, which include the full process of image retrieval in the plaintext domain. The experiments and security analysis demonstrate the efficiency, accuracy, and security of our scheme.

  匹配依据：MPC: secret sharing, secure computing

  </details>

- **Catalic: Delegated PSI Cardinality with Applications to Contact Tracing**
  2020-09-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1105)
  Thai Duong, Duong Hieu Phan, Ni Trieu

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection Cardinality (PSI-CA) allows two parties, each holding a set of items, to learn the size of the intersection of those sets without revealing any additional information. To the best of our knowledge, this work presents the first protocol that allows one of the parties to delegate PSI-CA computation to untrusted servers. At the heart of our delegated PSI-CA protocol is a new oblivious distributed key PRF (Odk-PRF) abstraction, which may be of independent interest. We explore in detail how to use our delegated PSI-CA protocol to perform privacy-preserving contact tracing. It has been estimated that a significant percentage of a given population would need to use a contact tracing app to stop a disease’s spread. Prior privacy-preserving contact tracing systems, however, impose heavy bandwidth or computational demands on client devices. These demands present an economic disincentive to participate for end users who may be billed per MB by their mobile data plan or for users who want to save battery life. We propose Catalic (ContAct TrAcing for LIghtweight Clients), a new contact tracing system that minimizes bandwidth cost and computation workload on client devices. By applying our new delegated PSI-CA protocol, Catalic shifts most of the client-side computation of contact tracing to untrusted servers, and potentially saves each user hundreds of megabytes of mobile data per day while preserving privacy.

  匹配依据：MPC: private set intersection

  </details>

- **Efficient Privacy-Preserving Computation Based on Additive Secret Sharing**
  2020-09-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.05356)
  Lizhi Xiong, Wenhao Zhou, Zhihua Xia, Qi Gu, Jian Weng

  <details><summary>摘要 / Abstract</summary>

  The emergence of cloud computing provides a new computing paradigm for users -- massive and complex computing tasks can be outsourced to cloud servers. However, the privacy issues also follow. Fully homomorphic encryption shows great potential in privacy-preserving computation, yet it is not ready for practice. At present, secure multiparty computation (MPC) remains mainly approach to deal with sensitive data. In this paper, following the secret sharing based MPC paradigm, we propose a secure 2-party computation scheme, in which cloud servers can securely evaluate functions with high efficiency. We first propose the multiplicative secret sharing (MSS) based on typical additive secret sharing (ASS). Then, we design protocols to switch shared secret between MSS and ASS, based on which a series of protocols for comparison and nearly all of the elementary functions are proposed. We prove that all the proposed protocols are Universally Composable secure in the honest-but-curious model. Finally, we will show the remarkable progress of our protocols on both communication efficiency and functionality completeness.

  匹配依据：MPC: secret sharing, secure 2 party computation, secure multiparty computation

  </details>

- **Accelerating 2PC-based ML with Limited Trusted Hardware**
  2020-09-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.05566)
  Muqsit Nawaz, Aditya Gulati, Kunlong Liu, Vishwajeet Agrawal, Prabhanjan Ananth, Trinabh Gupta

  <details><summary>摘要 / Abstract</summary>

  This paper describes the design, implementation, and evaluation of Otak, a system that allows two non-colluding cloud providers to run machine learning (ML) inference without knowing the inputs to inference. Prior work for this problem mostly relies on advanced cryptography such as two-party secure computation (2PC) protocols that provide rigorous guarantees but suffer from high resource overhead. Otak improves efficiency via a new 2PC protocol that (i) tailors recent primitives such as function and homomorphic secret sharing to ML inference, and (ii) uses trusted hardware in a limited capacity to bootstrap the protocol. At the same time, Otak reduces trust assumptions on trusted hardware by running a small code inside the hardware, restricting its use to a preprocessing step, and distributing trust over heterogeneous trusted hardware platforms from different vendors. An implementation and evaluation of Otak demonstrates that its CPU and network overhead converted to a dollar amount is 5.4$-$385$\times$ lower than state-of-the-art 2PC-based works. Besides, Otak&#x27;s trusted computing base (code inside trusted hardware) is only 1,300 lines of code, which is 14.6$-$29.2$\times$ lower than the code-size in prior trusted hardware-based works.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Fair and Sound Secret Sharing from Homomorphic Time-Lock Puzzles**
  2020-09-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1078)
  Jodie Knapp, Elizabeth A. Quaglia

  <details><summary>摘要 / Abstract</summary>

  Achieving fairness and soundness in non-simultaneous rational secret sharing schemes has proved to be challenging. On the one hand, soundness can be ensured by providing side information related to the secret as a check, but on the other, this can be used by deviant players to compromise fairness. To overcome this, the idea of incorporating a time delay was suggested in the literature: in particular, time-delay encryption based on memory-bound functions has been put forth as a solution. In this paper, we propose a different approach to achieve such delay, namely using homomorphic time-lock puzzles (HTLPs), introduced at CRYPTO 2019, and construct a fair and sound rational secret sharing scheme in the non-simultaneous setting from HTLPs. HTLPs are used to embed sub-shares of the secret for a predetermined time. This allows to restore fairness of the secret reconstruction phase, despite players having access to information related to the secret which is required to ensure soundness of the scheme. Key to our construction is the fact that the time-lock puzzles are homomorphic so that players can compactly evaluate sub-shares. Without this efficiency improvement, players would have to independently solve each puzzle sent from the other players to obtain a share of the secret, which would be computationally inefficient. We argue that achieving both fairness and soundness in a non-simultaneous scheme using a time delay based on CPU-bound functions rather than memory-bound functions is more cost effective and realistic in relation to the implementation of the construction.

  匹配依据：MPC: secret sharing

  </details>

- **Hybrid Differentially Private Federated Learning on Vertically Partitioned Data**
  2020-09-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.02763)
  Chang Wang, Jian Liang, Mingkai Huang, Bing Bai, Kun Bai, Hao Li

  <details><summary>摘要 / Abstract</summary>

  We present HDP-VFL, the first hybrid differentially private (DP) framework for vertical federated learning (VFL) to demonstrate that it is possible to jointly learn a generalized linear model (GLM) from vertically partitioned data with only a negligible cost, w.r.t. training time, accuracy, etc., comparing to idealized non-private VFL. Our work builds on the recent advances in VFL-based collaborative training among different organizations which rely on protocols like Homomorphic Encryption (HE) and Secure Multi-Party Computation (MPC) to secure computation and training. In particular, we analyze how VFL&#x27;s intermediate result (IR) can leak private information of the training data during communication and design a DP-based privacy-preserving algorithm to ensure the data confidentiality of VFL participants. We mathematically prove that our algorithm not only provides utility guarantees for VFL, but also offers multi-level privacy, i.e. DP w.r.t. IR and joint differential privacy (JDP) w.r.t. model weights. Experimental results demonstrate that our work, under adequate privacy budgets, is quantitatively and qualitatively similar to GLMs, learned in idealized non-private VFL setting, rather than the increased cost in memory and processing time in most prior works based on HE or MPC. Our codes will be released if this paper is accepted.

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **HACCLE: Metaprogramming for Secure Multi-Party Computation -- Extended Version**
  2020-09-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.01489)
  Yuyan Bao, Kirshanthan Sundararajah, Raghav Malik, Qianchuan Ye, Christopher Wagner, Nouraldin Jaber, Fei Wang, Mohammad Hassan Ameri, Donghang Lu, Alexander Seto, Benjamin Delaware, Roopsha Samanta, Aniket Kate, Christina Garman, Jeremiah Blocki, Pierre-David Letourneau, Benoit Meister, Jonathan Springer, Tiark Rompf, Milind Kulkarni

  <details><summary>摘要 / Abstract</summary>

  Cryptographic techniques have the potential to enable distrusting parties to collaborate in fundamentally new ways, but their practical implementation poses numerous challenges. An important class of such cryptographic techniques is known as Secure Multi-Party Computation (MPC). Developing Secure MPC applications in realistic scenarios requires extensive knowledge spanning multiple areas of cryptography and systems. And while the steps to arrive at a solution for a particular application are often straightforward, it remains difficult to make the implementation efficient, and tedious to apply those same steps to a slightly different application from scratch. Hence, it is an important problem to design platforms for implementing Secure MPC applications with minimum effort and using techniques accessible to non-experts in cryptography. In this paper, we present the HACCLE (High Assurance Compositional Cryptography: Languages and Environments) toolchain, specifically targeted to MPC applications. HACCLE contains an embedded domain-specific language Harpoon, for software developers without cryptographic expertise to write MPC-based programs, and uses Lightweight Modular Staging (LMS) for code generation. Harpoon programs are compiled into acyclic circuits represented in HACCLE&#x27;s Intermediate Representation (HIR) that serves as an abstraction over different cryptographic protocols such as secret sharing, homomorphic encryption, or garbled circuits. Implementations of different cryptographic protocols serve as different backends of our toolchain. The extensible design of HIR allows cryptographic experts to plug in new primitives and protocols to realize computation. And the use of standard metaprogramming techniques lowers the development effort significantly.

  匹配依据：MPC: garbled circuits, secret sharing, secure multi party computation

  </details>

- **Privacy-Preserving Distributed Processing: Metrics, Bounds, and Algorithms**
  2020-09-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.01098)
  Qiongxiu Li, Jaron Skovsted Gundersen, Richard Heusdens, Mads Græsbøll Christensen

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving distributed processing has recently attracted considerable attention. It aims to design solutions for conducting signal processing tasks over networks in a decentralized fashion without violating privacy. Many algorithms can be adopted to solve this problem such as differential privacy, secure multiparty computation, and the recently proposed distributed optimization based subspace perturbation. However, how these algorithms relate to each other is not fully explored yet. In this paper, we therefore first propose information-theoretic metrics based on mutual information. Using the proposed metrics, we are able to compare and relate a number of existing well-known algorithms. We then derive a lower bound on individual privacy that gives insights on the nature of the problem. To validate the above claims, we investigate a concrete example and compare a number of state-of-the-art approaches in terms of different aspects such as output utility, individual privacy and algorithm robustness against the number of corrupted parties, using not only theoretical analysis but also numerical validation. Finally, we discuss and provide principles for designing appropriate algorithms for different applications.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Algebraic geometry codes and some applications**
  2020-09-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2009.01281)
  Alain Couvreur, Hugues Randriambololona

  <details><summary>摘要 / Abstract</summary>

  This article surveys the development of the theory of algebraic geometry codes since their discovery in the late 70&#x27;s. We summarize the major results on various problems such as: asymptotic parameters, improved estimates on the minimum distance, and decoding algorithms. In addition, we present various modern applications of these codes such as public-key cryptography, algebraic complexity theory, multiparty computation or distributed storage.

  匹配依据：MPC: multiparty computation

  </details>

- **Circuit Amortization Friendly Encodings and their Application to Statistically Secure Multiparty Computation**
  2020-09-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1053)
  Anders Dalskov, Eysa Lee, Eduardo Soria-Vazquez

  <details><summary>摘要 / Abstract</summary>

  At CRYPTO 2018, Cascudo et al. introduced Reverse Multiplication Friendly Embeddings (RMFEs). These are a mechanism to compute $\delta$ parallel evaluations of the same arithmetic circuit over a field $\mathbb{F}_q$ at the cost of a single evaluation of that circuit in $\mathbb{F}_{q^d}$, where $\delta &lt; d$. Due to this inequality, RMFEs are a useful tool when protocols require to work over $\mathbb{F}_{q^d}$ but one is only interested in computing over $\mathbb{F}_q$. In this work we introduce Circuit Amortization Friendly Encodings (CAFEs), which generalize RMFEs while having concrete efficiency in mind. For a Galois Ring $R = GR(2^{k}, d)$, CAFEs allow to compute certain circuits over $\mathbb{Z}_{2^k}$ at the cost of a single secure multiplication in $R$. We present three CAFE instantiations, which we apply to the protocol for MPC over $\mathbb{Z}_{2^k}$ via Galois Rings by Abspoel et al. (TCC 2019). Our protocols allow for efficient switching between the different CAFEs, as well as between computation over $GR(2^{k}, d)$ and $\mathbb{F}_{2^{d}}$ in a way that preserves the CAFE in both rings. This adaptability leads to efficiency gains for e.g. Machine Learning applications, which can be represented as highly parallel circuits over $\mathbb{Z}_{2^k}$ followed by bit-wise operations. From an implementation of our techniques, we estimate that an SVM can be evaluated on 250 images in parallel up to $\times 7$ more efficiently using our techniques, compared to the protocol from Abspoel et al. (TCC 2019).

  匹配依据：MPC: secure multiparty computation

  </details>

- **Coding Constructions for Efficient Oblivious Transfer from Noisy Channels**
  2020-08-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.13551)
  Frédérique Oggier, Gilles Zémor

  <details><summary>摘要 / Abstract</summary>

  We consider oblivious transfer protocols performed over binary symmetric channels in a malicious setting where parties will actively cheat if they can. We provide constructions purely based on coding theory that achieve an explicit positive rate, the essential ingredient being the existence of linear codes whose Schur products are asymptotically good.

  匹配依据：MPC: oblivious transfer

  </details>

- **A construction of minimal linear codes from partial difference sets**
  2020-08-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.12998)
  Ran Tao, Tao Feng, Weicong Li

  <details><summary>摘要 / Abstract</summary>

  In this paper, we study a class of linear codes defined by characteristic functions of certain subsets of a finite field. We derive a sufficient and necessary condition for such a code to be a minimal linear code by a character-theoretical approach. We obtain new three-weight or four-weight minimal linear codes that do not satisfy the Ashikhmin-Barg condition by using partial difference sets. We show that our construction yields minimal linear codes that do not arise from cutting vectorial blocking sets, and also discuss their applications in secret sharing schemes.

  匹配依据：MPC: secret sharing

  </details>
