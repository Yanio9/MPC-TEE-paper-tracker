# 2020 · MPC · 仅预印本来源 · 第 2/3 页

[总目录](../PAPERS.md) · [上一页](2020-mpc-preprint-01.md) · [下一页](2020-mpc-preprint-03.md)

- **Minimal Symmetric PAKE and 1-out-of-N OT from Programmable-Once Public Functions**
  2020-08-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1043)
  Ian McQuoid, Mike Rosulek, Lawrence Roy

  <details><summary>摘要 / Abstract</summary>

  Symmetric password-authenticated key exchange (sPAKE) can be seen as an extension of traditional key exchange where two parties agree on a shared key if and only if they share a common secret (possibly low-entropy) password. We present the first sPAKE protocol to simultaneously achieve the following properties: - only two exponentiations per party, the same as plain unauthenticated Diffie-Hellman key agreement (and likely optimal); - optimal round complexity: a single flow (one message from each party that can be sent in parallel) to achieve implicit authentication, or two flows to achieve explicit mutual authentication; - security in the random oracle model, rather than ideal cipher or generic group model; - UC security, rather than game-based. Our protocol is a generalization of the seminal EKE protocol of Bellovin &amp; Merritt (S&amp;P 1992). We also present a UC-secure 1-out-of-$N$ oblivious transfer (OT) protocol, for random payloads. Its communication complexity is independent of $N$, meaning that $N$ can even be exponential in the security parameter. Such a protocol can also be considered a kind of oblivious PRF (OPRF). Our protocol improves over the leading UC-secure 1-out-of-$N$ OT construction of Masny &amp; Rindal (CCS 2019) for all $N&gt;2$, and has essentially the same cost for $N=2$. The new technique underlying these results is a primitive we call programmable-once public function (POPF). Intuitively, a POPF is a function whose output can be programmed by one party on exactly one point. All other outputs of the function are outside of any party&#x27;s control, in a provable sense. Update: dos Santos et al. (Eurocrypt 2023) showed that our POPF definition is not strong enough to prove security of EKE against a man-in-the-middle. See Januzelli et al. (Eurocrypt 2025) for a fixed POPF abstraction and EKE security proof.

  匹配依据：MPC: oblivious transfer

  </details>

- **Evolving Secret Sharing with Essential Participants**
  2020-08-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1035)
  Jyotirmoy Pramanik, Avishek Adhikari

  <details><summary>摘要 / Abstract</summary>

  Komargodski et.al. introduced {\em Evolving Secret Sharing} which allows an imaprtial participant, called \emph{dealer}, to share a secret among unbounded number of participants over any given access structure. In their construction for evolving secret sharing over general access structure, the size of share of the $i^{th}$ participant happens to be exponential $(\mathcal{O}(2^{i-1}))$. They also provided constructions for $(k,\infty)$ threshold secret sharing. We consider the problem of evolving secret sharing with $t$ essential participants, namely, over $t$-$(k,\infty)$ access structure, a generalization of $(k,\infty)$ secret sharing $(t=0)$. We further generalize this access structure to a possible case of unbounded number of essential participants and provide a construction for secret sharing on it. Both the constructions are information theoretically secure and reduce the share size of the construction due to Komargodski et.al. over general access structure, exponentially. Moreover, the essential participants receive ideal (and hence, optimal) shares in the first construction.

  匹配依据：MPC: secret sharing

  </details>

- **Private Join and Compute from PIR with Default**
  2020-08-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1011)
  Tancrède Lepoint, Sarvar Patel, Mariana Raykova, Karn Seth, Ni Trieu

  <details><summary>摘要 / Abstract</summary>

  The private join and compute (PJC) functionality enables secure computation over data distributed across different databases, which is a functionality with a wide range of applications, many of which address settings where the input databases are of significantly different sizes. We introduce the notion of private information retrieval (PIR) with default, which enables two-party PJC functionalities in a way that hides the size of the intersection of the two databases and incurs sublinear communication cost in the size of the bigger database. We provide two constructions for this functionality, one of which requires offline linear communication, which can be amortized across queries, and one that provides sublinear cost for each query but relies on more computationally expensive tools. We construct inner-product PJC, which has applications to ads conversion measurement and contact tracing, relying on an extension of PIR with default. We evaluate the efficiency of our constructions, which can enable $\mathbf{2^{12}}$ PIR with default lookups on a database of size $\mathbf{2^{30}}$ (or inner-product PJC on databases with such sizes) with the communication of $\mathbf{945}$MB, which costs less than $\mathbf{\$0.04}$ for the client and $\mathbf{\$5.22}$ for the server.

  匹配依据：MPC: secure computation

  </details>

- **A Study on Privacy-Preserving GRU Inference Framework**
  2020-08-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1013)
  Shou-Ching Hsiao, Zi-Yuan Liu, Raylin Tso

  <details><summary>摘要 / Abstract</summary>

  Gated Recurrent Unit (GRU) has broad application fields, such as sentiment analysis, speech recognition, malware analysis, and other sequential data processing. For low-cost deployment and efficient machine learning services, a growing number of model owners choose to deploy the trained GRU models through Machine-learning-as-a-service (MLaaS). However, privacy has become a significant concern for both model owners and prediction clients, including model weights privacy, input data privacy, and output results privacy. The privacy leakage may be caused by either external intrusion or insider attacks. To address the above issues, this research designs a framework for privacy-preserving GRU models, which aims for privacy scenarios such as predicting on textual data, network packets, heart rate data, and so on. In consideration of accuracy and efficiency, this research uses additive secret sharing to design the basic operations and gating mechanisms of GRU. The protocols can meet the security requirements of privacy and correctness under the Universal Composability framework with the semi-honest adversary. Additionally, the framework and protocols are realized with a proof-of-concept implementation. The experiment results are presented with respect to time consumption and inference accuracy.

  匹配依据：MPC: secret sharing

  </details>

- **When Homomorphic Encryption Marries Secret Sharing: Secure Large-Scale Sparse Logistic Regression and Applications in Risk Control**
  2020-08-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.08753)
  Chaochao Chen, Jun Zhou, Li Wang, Xibin Wu, Wenjing Fang, Jin Tan, Lei Wang, Alex X. Liu, Hao Wang, Cheng Hong

  <details><summary>摘要 / Abstract</summary>

  Logistic Regression (LR) is the most widely used machine learning model in industry for its efficiency, robustness, and interpretability. Due to the problem of data isolation and the requirement of high model performance, many applications in industry call for building a secure and efficient LR model for multiple parties. Most existing work uses either Homomorphic Encryption (HE) or Secret Sharing (SS) to build secure LR. HE based methods can deal with high-dimensional sparse features, but they incur potential security risks. SS based methods have provable security, but they have efficiency issue under high-dimensional sparse features. In this paper, we first present CAESAR, which combines HE and SS to build secure large-scale sparse logistic regression model and achieves both efficiency and security. We then present the distributed implementation of CAESAR for scalability requirement. We have deployed CAESAR in a risk control task and conducted comprehensive experiments. Our experimental results show that CAESAR improves the state-of-the-art model by around 130 times.

  匹配依据：MPC: secret sharing

  </details>

- **Analog Lagrange Coded Computing**
  2020-08-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.08565)
  Mahdi Soleymani, Hessam Mahdavifar, A. Salman Avestimehr

  <details><summary>摘要 / Abstract</summary>

  A distributed computing scenario is considered, where the computational power of a set of worker nodes is used to perform a certain computation task over a dataset that is dispersed among the workers. Lagrange coded computing (LCC), proposed by Yu et al., leverages the well-known Lagrange polynomial to perform polynomial evaluation of the dataset in such a scenario in an efficient parallel fashion while keeping the privacy of data amidst possible collusion of workers. This solution relies on quantizing the data into a finite field, so that Shamir&#x27;s secret sharing, as one of its main building blocks, can be employed. Such a solution, however, is not properly scalable with the size of dataset, mainly due to computation overflows. To address such a critical issue, we propose a novel extension of LCC to the analog domain, referred to as analog LCC (ALCC). All the operations in the proposed ALCC protocol are done over the infinite fields of R/C but for practical implementations floating-point numbers are used. We characterize the privacy of data in ALCC, against any subset of colluding workers up to a certain size, in terms of the distinguishing security (DS) and the mutual information security (MIS) metrics. Also, the accuracy of outcome is characterized in a practical setting assuming operations are performed using floating-point numbers. Consequently, a fundamental trade-off between the accuracy of the outcome of ALCC and its privacy level is observed and is numerically evaluated. Moreover, we implement the proposed scheme to perform matrix-matrix multiplication over a batch of matrices. It is observed that ALCC is superior compared to the state-of-the-art LCC, implemented using fixed-point numbers, assuming both schemes use an equal number of bits to represent data symbols.

  匹配依据：MPC: secret sharing

  </details>

- **Shared MF: A privacy-preserving recommendation system**
  2020-08-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.07759)
  Senci Ying

  <details><summary>摘要 / Abstract</summary>

  Matrix factorization is one of the most commonly used technologies in recommendation system. With the promotion of recommendation system in e-commerce shopping, online video and other aspects, distributed recommendation system has been widely promoted, and the privacy problem of multi-source data becomes more and more important. Based on Federated learning technology, this paper proposes a shared matrix factorization scheme called SharedMF. Firstly, a distributed recommendation system is built, and then secret sharing technology is used to protect the privacy of local data. Experimental results show that compared with the existing homomorphic encryption methods, our method can have faster execution speed without privacy disclosure, and can better adapt to recommendation scenarios with large amount of data.

  匹配依据：MPC: secret sharing

  </details>

- **Fuzzy Asymmetric Password-Authenticated Key Exchange**
  2020-08-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/987)
  Andreas Erwig, Julia Hesse, Maximilian Orlt, Siavash Riahi

  <details><summary>摘要 / Abstract</summary>

  Password-Authenticated Key Exchange (PAKE) lets users with passwords exchange a cryptographic key. There have been two variants of PAKE which make it more applicable to real-world scenarios: - Asymmetric PAKE (aPAKE), which aims at protecting a client&#x27;s password even if the authentication server is untrusted, and - Fuzzy PAKE (fPAKE), which enables key agreement even if passwords of users are noisy, but ``close enough&#x27;&#x27;. Supporting fuzzy password matches eases the use of higher entropy passwords and enables using biometrics and environmental readings (both of which are naturally noisy). Until now, both variants of PAKE have been considered only in separation. In this paper, we consider both of them simultaneously. We introduce the notion of Fuzzy Asymmetric PAKE (fuzzy aPAKE), which protects against untrusted servers and supports noisy passwords. We formulate our new notion in the Universal Composability framework of Canetti (FOCS&#x27;01), which is the preferred model for password-based primitives. We then show that fuzzy aPAKE can be obtained from oblivious transfer and some variant of robust secret sharing (Cramer et al, EC&#x27;15). We achieve security against malicious parties while avoiding expensive tools such as non-interactive zero-knowledge proofs. Our construction is round-optimal, with message and password file sizes that are independent of the schemes error tolerance.

  匹配依据：MPC: oblivious transfer, secret sharing

  </details>

- **Efficient Protocols for Oblivious Linear Function Evaluation from Ring-LWE**
  2020-08-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/970)
  Carsten Baum, Daniel Escudero, Alberto Pedrouzo-Ulloa, Peter Scholl, Juan Ramón Troncoso-Pastoriza

  <details><summary>摘要 / Abstract</summary>

  An oblivious linear function evaluation protocol, or OLE, is a two-party protocol for the function $f(x) = ax + b$, where a sender inputs the field elements $a,b$, and a receiver inputs $x$ and learns $f(x)$. OLE can be used to build secret-shared multiplication, and is an essential component of many secure computation applications including general-purpose multi-party computation, private set intersection and more. In this work, we present several efficient OLE protocols from the ring learning with errors (RLWE) assumption. Technically, we build two new passively secure protocols, which build upon recent advances in homomorphic secret sharing from (R)LWE (Boyle et al., Eurocrypt 2019), with optimizations tailored to the setting of OLE. We upgrade these to active security using efficient amortized zero-knowledge techniques for lattice relations (Baum et al., Crypto 2018), and design new variants of zero-knowledge arguments that are necessary for some of our constructions. Our protocols offer several advantages over existing constructions. Firstly, they have the lowest communication complexity amongst previous, practical protocols from RLWE and other assumptions; secondly, they are conceptually very simple, and have just one round of interaction for the case of OLE where $b$ is randomly chosen. We demonstrate this with an implementation of one of our passively secure protocols, which can perform more than 1 million OLEs per second over the ring $\mathbb{Z}_m$, for a 120-bit modulus $m$, on standard hardware.

  匹配依据：MPC: multi party computation, private set intersection, secret sharing, secure computation

  </details>

- **Efficient Private Machine Learning by Differentiable Random Transformations**
  2020-08-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.07758)
  Fei Zheng

  <details><summary>摘要 / Abstract</summary>

  With the increasing demands for privacy protection, many privacy-preserving machine learning systems were proposed in recent years. However, most of them cannot be put into production due to their slow training and inference speed caused by the heavy cost of homomorphic encryption and secure multiparty computation(MPC) methods. To circumvent this, I proposed a privacy definition which is suitable for large amount of data in machine learning tasks. Based on that, I showed that random transformations like linear transformation and random permutation can well protect privacy. Merging random transformations and arithmetic sharing together, I designed a framework for private machine learning with high efficiency and low computation cost.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Access Structure Hiding Secret Sharing from Novel Set Systems and Vector Families**
  2020-08-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.07969)
  Vipin Singh Sehrawat, Yvo Desmedt

  <details><summary>摘要 / Abstract</summary>

  Secret sharing provides a means to distribute shares of a secret such that any authorized subset of shares, specified by an access structure, can be pooled together to recompute the secret. The standard secret sharing model requires public access structures, which violates privacy and facilitates the adversary by revealing high-value targets. In this paper, we address this shortcoming by introducing \emph{hidden access structures}, which remain secret until some authorized subset of parties collaborate. The central piece of this work is the construction of a set-system $\mathcal{H}$ with strictly greater than $\exp\left(c \dfrac{1.5 (\log h)^2}{\log \log h}\right)$ subsets of a set of $h$ elements. Our set-system $\mathcal{H}$ is defined over $\mathbb{Z}_m$, where $m$ is a non-prime-power, such that the size of each set in $\mathcal{H}$ is divisible by $m$ but the sizes of their pairwise intersections are not divisible by $m$, unless one set is a subset of another. We derive a vector family $\mathcal{V}$ from $\mathcal{H}$ such that superset-subset relationships in $\mathcal{H}$ are represented by inner products in $\mathcal{V}$. We use $\mathcal{V}$ to &quot;encode&quot; the access structures and thereby develop the first \emph{access structure hiding} secret sharing scheme. For a setting with $\ell$ parties, our scheme supports $2^{\binom{\ell}{\ell/2+1}}$ out of the $2^{2^{\ell - O(\log \ell)}}$ total monotone access structures, and its maximum share size for any access structures is $(1+ o(1)) \dfrac{2^{\ell+1}}{\sqrt{π\ell/2}}$. The scheme assumes semi-honest polynomial-time parties, and its security relies on the Generalized Diffie-Hellman assumption.

  匹配依据：MPC: secret sharing

  </details>

- **Multi-Party Private Set Intersection: An Information-Theoretic Approach**
  2020-08-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.07504)
  Zhusheng Wang, Karim Banawan, Sennur Ulukus

  <details><summary>摘要 / Abstract</summary>

  We investigate the problem of multi-party private set intersection (MP-PSI). In MP-PSI, there are $M$ parties, each storing a data set $\mathcal{p}_i$ over $N_i$ replicated and non-colluding databases, and we want to calculate the intersection of the data sets $\cap_{i=1}^M \mathcal{p}_i$ without leaking any information beyond the set intersection to any of the parties. We consider a specific communication protocol where one of the parties, called the leader party, initiates the MP-PSI protocol by sending queries to the remaining parties which are called client parties. The client parties are not allowed to communicate with each other. We propose an information-theoretic scheme that privately calculates the intersection $\cap_{i=1}^M \mathcal{p}_i$ with a download cost of $D = \min_{t \in \{1, \cdots, M\}} \sum_{i \in \{1, \cdots M\}\setminus {t}} \left\lceil \frac{|\mathcal{p}_t|N_i}{N_i-1}\right\rceil$. Similar to the 2-party PSI problem, our scheme builds on the connection between the PSI problem and the multi-message symmetric private information retrieval (MM-SPIR) problem. Our scheme is a non-trivial generalization of the 2-party PSI scheme as it needs an intricate design of the shared common randomness. Interestingly, in terms of the download cost, our scheme does not incur any penalty due to the more stringent privacy constraints in the MP-PSI problem compared to the 2-party PSI problem.

  匹配依据：MPC: private set intersection

  </details>

- **PPContactTracing: A Privacy-Preserving Contact Tracing Protocol for COVID-19 Pandemic**
  2020-08-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.06648)
  Priyanka Singh, Abhishek Singh, Gabriel Cojocaru, Praneeth Vepakomma, Ramesh Raskar

  <details><summary>摘要 / Abstract</summary>

  Several contact tracing solutions have been proposed and implemented all around the globe to combat the spread of COVID-19 pandemic. But, most of these solutions endanger the privacy rights of the individuals and hinder their widespread adoption. We propose a privacy-preserving contact tracing protocol for the efficient tracing of the spread of the global pandemic. It is based on the private set intersection (PSI) protocol and utilizes the homomorphic properties to preserve the privacy at the individual level. A hierarchical model for the representation of landscapes and rate-limiting factor on the number of queries have been adopted to maintain the efficiency of the protocol.

  匹配依据：MPC: private set intersection

  </details>

- **Fourier's quantum information processing**
  2020-08-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.07914)
  Mario Mastriani

  <details><summary>摘要 / Abstract</summary>

  We demonstrate that quantum information processing (QIP) completely rests on quantum Fourier transform (QFT), and 190 years after his death, the work of Jean-Baptiste Joseph Fourier is more present than ever in Physics, constituting the heart of QIP, and showing the spectral nature of quantum entanglement, quantum teleportation, and quantum secret sharing.

  匹配依据：MPC: secret sharing

  </details>

- **On the Hardness of Massively Parallel Computation**
  2020-08-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.06554)
  Kai-Min Chung, Kuan-Yi Ho, Xiaorui Sun

  <details><summary>摘要 / Abstract</summary>

  We investigate whether there are inherent limits of parallelization in the (randomized) massively parallel computation (MPC) model by comparing it with the (sequential) RAM model. As our main result, we show the existence of hard functions that are essentially not parallelizable in the MPC model. Based on the widely-used random oracle methodology in cryptography with a cryptographic hash function $h:\{0,1\}^n \rightarrow \{0,1\}^n$ computable in time $t_h$, we show that there exists a function that can be computed in time $O(T\cdot t_h)$ and space $S$ by a RAM algorithm, but any MPC algorithm with local memory size $s 1$ requires at least $\tildeΩ(T)$ rounds to compute the function, even in the average case, for a wide range of parameters $n \leq S \leq T \leq 2^{n^{1/4}}$. Our result is almost optimal in the sense that by taking $T$ to be much larger than $t_h$, \textit{e.g.}, $T$ to be sub-exponential in $t_h$, to compute the function, the round complexity of any MPC algorithm with small local memory size is asymptotically the same (up to a polylogarithmic factor) as the time complexity of the RAM algorithm. Our result is obtained by adapting the so-called compression argument from the data structure lower bounds and cryptography literature to the context of massively parallel computation.

  匹配依据：MPC: mpc (context)

  </details>

- **Genuine Secret-Sharing States**
  2020-08-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.06202)
  Minjin Choi, Soojoon Lee

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing allows each player to have classical information for secret sharing in quantum mechanical ways. In this work, we construct a class of quantum states on which players can quantumly perform secret sharing secure against dishonest players as well as eavesdropper. We here call them the genuine secret-sharing states. In addition, we show that if $N$ players share an $N$-party genuine secret-sharing state, then arbitrary $M$ players out of the total players can share an $M$-party genuine secret-sharing state by means of local operations and classical communication on the state. We also define the distillable rate with respect to the genuine secret-sharing state, and explain the connection between the distillable rate and the relative entropy of entanglement.

  匹配依据：MPC: secret sharing

  </details>

- **A novel three party Quantum secret sharing scheme based on Bell state sequential measurements with application in quantum image sharing**
  2020-08-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.06228)
  Farhan Musanna, Sanjeev Kumar

  <details><summary>摘要 / Abstract</summary>

  In this work, we present a quantum secret sharing scheme based on Bell state entanglement and sequential projection measurements. The protocol verifies the $n$ out of $n$ scheme and supports the aborting of the protocol in case all the parties do not divulge in their valid measurement outcomes. The operator-qubit pair forms an integral part of the scheme determining the classical secret to be shared. The protocol is robust enough to neutralize any eavesdropping on a particular qubit of the dealer. The experimental demonstration of the scheme is done on IBM-QE cloud platform with backends \texttt{IBMQ\_16\_Melbourne} and \texttt{IBMQ\_QASM\_SIMULATOR\_V0.1.547} simulator. The security analysis performed on the scheme and the comparative analysis supports our claim of a stringent and an efficient scheme as compared to some recent quantum and semi-quantum techniques of secret sharing.

  匹配依据：MPC: secret sharing

  </details>

- **Enable Dynamic Parameters Combination to Boost Linear Convolutional Neural Network for Sensitive Data Inference**
  2020-08-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/961)
  Qizheng Wang, Wenping Ma, Jie Li, Ge Liu

  <details><summary>摘要 / Abstract</summary>

  As cloud computing matures, Machine Learning as a Service(MLaaS) has received more attention. In many scenarios, sensitive information also has a demand for MLaaS, but it should not be exposed to others, which brings a dilemma. In order to solve this dilemma, many works have proposed some privacy-protected machine learning frameworks. Compared with plain-text tasks, cipher-text inference has higher computation and communication overhead. In addition to the difficulties caused by cipher-text calculations, the nonlinear activation functions in machine learning models are not friendly to Homomorphic Encryption(HE) and Secure Multi-Party Computation(MPC). The nonlinear activation function can effectively improve the performance of the network, and it seems that the high overhead brought by it is inevitable. In order to solve this problem, this paper re-explains the mechanism of the nonlinear activation function in forward propagation from another perspective, and based on this observation, proposed a dynamic parameters combination scheme as an alternative, called DPC. DPC allows the decoupling of nonlinear operations and linear operations in neural networks. This work further uses this feature to design the HE-based framework and MPC-based framework, so that non-linear operations can be completed locally by the user through pre-computation, which greatly improves the efficiency of privacy protection data prediction. The evaluation result shows that the linear neural networks with DPC can perform high accuracy. Without other optimizations, the HE-based proposed in this work shows 2x faster executions than CryptoNets only relying on the advantage of the DPC. The MPC-based framework proposed in this work can achieve similar efficiency to plain-text prediction, and has advantages over other work in terms of communication complexity and computational complexity.

  匹配依据：MPC: secure multi party computation

  </details>

- **Configurable Private Querying: Lookup and Partial Matching under Homomorphic Encryption**
  2020-08-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/964)
  Hamish Hunt, Jack Crawford, Oliver Masters, Enrico Steffinlongo, Flavio Bergamaschi

  <details><summary>摘要 / Abstract</summary>

  The ability to query a database privately is nowadays ubiquitous via an encrypted channel. With the advent of homomorphic encryption, there is a want to expand the notion of privacy in this context to querying privately on the database with the database learning as little to no information of the query data or its result. The ability to compute the intersection from at least two parties’ sets that are kept private only to themselves is known as private set intersection (PSI) and should be considered a fundamental operation in several homomorphic computation scenarios to do useful work; not least for the ability to implement queries on a database. We outline in this paper a novel highly configurable PSI structure to be used in private querying providing the possibility that even the exact query itself can be protected from the database if required. As well as complex database lookups, there is also a more complex partial matching. The outline of the system design is discussed and we report preliminary results on some of the fundamental operations. We demonstrate that this technology is emerging as a viable given response to lookup queries and partially matching on an encrypted database with over a million entries in approximately 9 minutes.

  匹配依据：MPC: private set intersection

  </details>

- **Amplifying the Security of Functional Encryption, Unconditionally**
  2020-08-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/951)
  Aayush Jain, Alexis Korb, Nathan Manohar, Amit Sahai

  <details><summary>摘要 / Abstract</summary>

  Security amplification is a fundamental problem in cryptography. In this work, we study security amplification for functional encryption (FE). We show two main results: 1) For any constant epsilon in (0,1), we can amplify any FE scheme for P/poly which is epsilon-secure against all polynomial sized adversaries to a fully secure FE scheme for P/poly, unconditionally. 2) For any constant epsilon in (0,1), we can amplify any FE scheme for P/poly which is epsilon-secure against subexponential sized adversaries to a fully subexponentially secure FE scheme for P/poly, unconditionally. Furthermore, both of our amplification results preserve compactness of the underlying FE scheme. Previously, amplification results for FE were only known assuming subexponentially secure LWE. Along the way, we introduce a new form of homomorphic secret sharing called set homomorphic secret sharing that may be of independent interest. Additionally, we introduce a new technique, which allows one to argue security amplification of nested primitives, and prove a general theorem that can be used to analyze the security amplification of parallel repetitions.

  匹配依据：MPC: secret sharing

  </details>

- **SplitNN-driven Vertical Partitioning**
  2020-08-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.04137)
  Iker Ceballos, Vivek Sharma, Eduardo Mugica, Abhishek Singh, Alberto Roman, Praneeth Vepakomma, Ramesh Raskar

  <details><summary>摘要 / Abstract</summary>

  In this work, we introduce SplitNN-driven Vertical Partitioning, a configuration of a distributed deep learning method called SplitNN to facilitate learning from vertically distributed features. SplitNN does not share raw data or model details with collaborating institutions. The proposed configuration allows training among institutions holding diverse sources of data without the need of complex encryption algorithms or secure computation protocols. We evaluate several configurations to merge the outputs of the split models, and compare performance and resource efficiency. The method is flexible and allows many different configurations to tackle the specific challenges posed by vertically split datasets.

  匹配依据：MPC: secure computation

  </details>

- **On the relationship between (secure) multi-party computation and (secure) federated learning**
  2020-08-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2008.02609)
  Huafei Zhu

  <details><summary>摘要 / Abstract</summary>

  The contribution of this short note, contains the following two parts: in the first part, we are able to show that the federate learning (FL) procedure presented by Kairouz et al. \cite{Kairouz1901}, is a random processing. Namely, an $m$-ary functionality for the FL procedure can be defined in the context of multi-party computation (MPC); Furthermore, an instance of FL protocol along Kairouz et al.&#x27;s definition can be viewed as an implementation of the defined $m$-ary functionality. As such, an instance of FL procedure is also an instance of MPC protocol. In short, FL is a subset of MPC. To privately computing the defined FL (m-ary) functionality, various techniques such as homomorphic encryption (HE), secure multi-party computation (SMPC) and differential privacy (DP) have been deployed. In the second part, we are able to show that if the underlying FL instance privately computes the defined $m$-ary functionality in the simulation-based framework, then the simulation-based FL solution is also an instance of SMPC. Consequently, SFL is a subset of SMPC.

  匹配依据：MPC: multi party computation, secure multi party computation

  </details>

- **Secure Computation Framework for Multiple Data Providers Against Malicious Adversaries**
  2020-07-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.14915)
  Zhili Chen, Xin Chen

  <details><summary>摘要 / Abstract</summary>

  Due to the great development of secure multi-party computation, many practical secure computation schemes have been proposed. As an example, different secure auction mechanisms have been widely studied, which can protect bid privacy while satisfying various economic properties. However, as far as we know, none of them solve the secure computation problems for multiple data providers (e.g., secure cloud resource auctions) in the malicious security model. In this paper, we use the techniques of cut-and-choose and garbled circuits to propose a general secure computation framework for multiple data providers against malicious adversaries. Specifically, our framework checks input consistency with the cut-and-choose paradigm, conducts maliciously secure computations by running two independent garbled circuits, and verifies the correctness of output by comparing two versions of outputs. Theoretical analysis shows that our framework is secure against a malicious computation party, or a subset of malicious data providers. Taking secure cloud resource auctions as an example, we implement our framework. Extensive experimental evaluations show that the performance of the proposed framework is acceptable in practice.

  匹配依据：MPC: garbled circuits, secure computation, secure multi party computation

  </details>

- **Efficient Sparse Secure Aggregation for Federated Learning**
  2020-07-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.14861)
  Constance Beguier, Mathieu Andreux, Eric W. Tramel

  <details><summary>摘要 / Abstract</summary>

  Federated Learning enables one to jointly train a machine learning model across distributed clients holding sensitive datasets. In real-world settings, this approach is hindered by expensive communication and privacy concerns. Both of these challenges have already been addressed individually, resulting in competing optimisations. In this article, we tackle them simultaneously for one of the first times. More precisely, we adapt compression-based federated techniques to additive secret sharing, leading to an efficient secure aggregation protocol, with an adaptable security level. We prove its privacy against malicious adversaries and its correctness in the semi-honest setting. Experiments on deep convolutional networks demonstrate that our secure protocol achieves high accuracy with low communication costs. Compared to prior works on secure aggregation, our protocol has a lower communication and computation costs for a similar accuracy.

  匹配依据：MPC: secret sharing

  </details>

- **Secure Computation over Lattices and Elliptic Curves**
  2020-07-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/926)
  Brett Hemenway Falk, Daniel Noble

  <details><summary>摘要 / Abstract</summary>

  Traditional threshold cryptosystems have decentralized core cryptographic primitives like key generation, decryption and signatures. Most threshold cryptosystems, however, rely on special purpose protocols that cannot easily be integrated into more complex multiparty protocols. In this work, we design and implement decentralized versions of lattice-based and elliptic-curve-based public-key cryptoystems using generic secure multiparty computation (MPC) protocols. These are standard cryptosystems, so we introduce no additional work for encrypting devices and no new assumptions beyond those of the generic MPC framework. Both cryptosystems are also additively homomorphic, which allows for secure additions directly on ciphertexts. By using generic MPC techniques, our multiparty decryption protocols compute secret-shares of the plaintext, whereas most special-purpose cryptosystems either do not support decryption or must reveal the decryptions in the clear. Our method allows complex functions to be securely evaluated after decryption, revealing only the results of the functions and not the plaintexts themselves. To improve performance, we present a novel oblivious elliptic curve multiplication protocol and a new noise-masking technique which may be of independent interest. We implemented our protocols using the SCALE-MAMBA secure multiparty computation platform, which provides security against malicious adversaries and supports arbitrary numbers of participants.

  匹配依据：MPC: secure computation, secure multiparty computation

  </details>

- **Ferret: Fast Extension for coRRElated oT with small communication**
  2020-07-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/924)
  Kang Yang, Chenkai Weng, Xiao Lan, Jiang Zhang, Xiao Wang

  <details><summary>摘要 / Abstract</summary>

  Correlated oblivious transfer (COT) is a crucial building block for secure multi-party computation (MPC) and can be generated efficiently via OT extension. Recent works based on the pseudorandom correlation generator (PCG) paradigm presented a new way to generate random COT correlations using only communication sublinear to the output length. However, due to their high computational complexity, these protocols are only faster than the classical IKNP-style OT extension under restricted network bandwidth. In this paper, we propose new COT protocols in the PCG paradigm that achieve unprecedented performance. With 50 Mbps network bandwidth, our maliciously secure protocol can produce one COT correlation in 22 nanoseconds. More specifically, our results are summarized as follows: - We propose a semi-honest COT protocol with sublinear communication and linear computation. This protocol assumes primal-LPN and is built upon a recent VOLE protocol with semi-honest security by Schoppmann et al. (CCS 2019). We are able to apply various optimizations to reduce its communication cost by roughly 15x, not counting a one-time setup cost that diminishes as we generate more COTs. - We strengthen our COT protocol to malicious security with no loss of efficiency. Among all optimizations, our new protocol features a new checking technique that ensures correctness and consistency essentially for free. In particular, our maliciously secure protocol is only 1-3 nanoseconds slower for each COT. - We implemented our protocols, and the code will be publicly available at EMP-toolkit. We observe at least 9x improvement in running time compared to the state-of-the-art protocol by Boyle et al. (CCS 2019) in both semi-honest and malicious settings under any network faster than 50 Mbps. With this new record of efficiency for generating COT correlations, we anticipate new protocol designs and optimizations will flourish on top of our protocol.

  匹配依据：MPC: oblivious transfer, secure multi party computation

  </details>

- **Black-Box Transformations from Passive to Covert Security with Public Verifiability**
  2020-07-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/916)
  Ivan Damgård, Claudio Orlandi, Mark Simkin

  <details><summary>摘要 / Abstract</summary>

  In the context of secure computation, protocols with security against covert adversaries ensure that any misbehavior by malicious parties will be detected by the honest parties with some constant probability. As such, these protocols provide better security guarantees than passively secure protocols and, moreover, are easier to construct than protocols with full security against active adversaries. Protocols that, upon detecting a cheating attempt, allow the honest parties to compute a certificate that enables third parties to verify whether an accused party misbehaved or not are called publicly verifiable. In this work, we present the first generic compilers for constructing two-party protocols with covert security and public verifiability from protocols with passive security. We present two separate compilers, which are both fully blackbox in the underlying protocols they use. Both of them only incur a constant multiplicative factor in terms of bandwidth overhead and a constant additive factor in terms of round complexity on top of the passively secure protocols they use. The first compiler applies to all two-party protocols that have no private inputs. This class of protocols covers the important class of preprocessing protocols that are used to setup correlated randomness among parties. We use our compiler to obtain the first secret-sharing based two-party protocol with covert security and public verifiability. Notably, the produced protocol achieves public verifiability essentially for free when compared with the best known previous solutions based on secret-sharing that did not provide public verifiability Our second compiler constructs protocols with covert security and public verifiability for arbitrary functionalities from passively secure protocols. It uses our first compiler to perform a setup phase, which is independent of the parties&#x27; inputs as well as the protocol they would like to execute. Finally, we show how to extend our techniques to obtain multiparty computation protocols with covert security and public verifiability against arbitrary constant fractions of corruptions.

  匹配依据：MPC: multiparty computation, secret sharing, secure computation

  </details>

- **SOTERIA: In Search of Efficient Neural Networks for Private Inference**
  2020-07-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.12934)
  Anshul Aggarwal, Trevor E. Carlson, Reza Shokri, Shruti Tople

  <details><summary>摘要 / Abstract</summary>

  ML-as-a-service is gaining popularity where a cloud server hosts a trained model and offers prediction (inference) service to users. In this setting, our objective is to protect the confidentiality of both the users&#x27; input queries as well as the model parameters at the server, with modest computation and communication overhead. Prior solutions primarily propose fine-tuning cryptographic methods to make them efficient for known fixed model architectures. The drawback with this line of approach is that the model itself is never designed to operate with existing efficient cryptographic computations. We observe that the network architecture, internal functions, and parameters of a model, which are all chosen during training, significantly influence the computation and communication overhead of a cryptographic method, during inference. Based on this observation, we propose SOTERIA -- a training method to construct model architectures that are by-design efficient for private inference. We use neural architecture search algorithms with the dual objective of optimizing the accuracy of the model and the overhead of using cryptographic primitives for secure inference. Given the flexibility of modifying a model during training, we find accurate models that are also efficient for private computation. We select garbled circuits as our underlying cryptographic primitive, due to their expressiveness and efficiency, but this approach can be extended to hybrid multi-party computation settings. We empirically evaluate SOTERIA on MNIST and CIFAR10 datasets, to compare with the prior work. Our results confirm that SOTERIA is indeed effective in balancing performance and accuracy.

  匹配依据：MPC: garbled circuits, multi party computation

  </details>

- **MPC-enabled Privacy-Preserving Neural Network Training against Malicious Attack**
  2020-07-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.12557)
  Ziyao Liu, Ivan Tjuawinata, Chaoping Xing, Kwok-Yan Lam

  <details><summary>摘要 / Abstract</summary>

  The application of secure multiparty computation (MPC) in machine learning, especially privacy-preserving neural network training, has attracted tremendous attention from the research community in recent years. MPC enables several data owners to jointly train a neural network while preserving the data privacy of each participant. However, most of the previous works focus on semi-honest threat model that cannot withstand fraudulent messages sent by malicious participants. In this paper, we propose an approach for constructing efficient $n$-party protocols for secure neural network training that can provide security for all honest participants even when a majority of the parties are malicious. Compared to the other designs that provide semi-honest security in a dishonest majority setting, our actively secure neural network training incurs affordable efficiency overheads of around 2X and 2.7X in LAN and WAN settings, respectively. Besides, we propose a scheme to allow additive shares defined over an integer ring $\mathbb{Z}_N$ to be securely converted to additive shares over a finite field $\mathbb{Z}_Q$, which may be of independent interest. Such conversion scheme is essential in securely and correctly converting shared Beaver triples defined over an integer ring generated in the preprocessing phase to triples defined over a field to be used in the calculation in the online phase.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Study on Entanglement and its Utility in Information Processing**
  2020-07-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.10890)
  Sovik Roy

  <details><summary>摘要 / Abstract</summary>

  The efficacies of maximally and that of non-maximally entangled mixed states as teleportation channels have been studied. A new class of non-maximally entangled mixed states have been proposed also. Their advantages as quantum teleportation channels over existing non-maximally entangled mixed states have been verified. The mixed states can also be generated using quantum cloning machines. We have also studied how one can utilize the mixed entangled states obtained as output from a state independent quantum cloning machine in teleportation and dense coding. Mixed states can also be used in secret sharing. A new protocol of secret sharing has been devised where four parties are involved. One of them is honest by nature and the other is dishonest. The dishonest one has two associates who are also involved in the protocol. It has been shown how the honest party, by using quantum cloning machine, can prevent the dishonest party from communicating the secret message to his accomplices. A relation has been established among entanglement of the initially prepared state, entanglement of the mixed state received by the recipients of the dishonest one after honest party applies the cloning scheme and the cloning parameters of the cloning machine. The usefulness of tri-partite and four-partite entangled states in controlled dense coding has been discussed. The thesis concludes with the summary and possible courses of future works.

  匹配依据：MPC: secret sharing

  </details>

- **Optimally-resilient Unconditionally-secure Asynchronous Multi-party Computation Revisited**
  2020-07-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/906)
  Ashish Choudhury

  <details><summary>摘要 / Abstract</summary>

  In this paper, we present an optimally-resilient, unconditionally-secure asynchronous multi-party computation (AMPC) protocol for $n$ parties, tolerating a computationally unbounded adversary, capable of corrupting up to $t &lt; \frac{n}{3}$ parties. Our protocol needs a communication of ${\cal O}(n^4)$ field elements per multiplication gate. This is to be compared with previous best AMPC protocol (Patra et al, ICITS 2009) in the same setting, which needs a communication of ${\cal O}(n^5)$ field elements per multiplication gate. To design our protocol, we present a simple and highly efficient asynchronous verifiable secret-sharing (AVSS) protocol, which is of independent interest.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **A Not-So-Trival Replay Attack Against DH-PSI**
  2020-07-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/901)
  Hongrui Cui, Yu Yu

  <details><summary>摘要 / Abstract</summary>

  In this short report, we present a simple yet effective inter-session replay attack against the Diffie-Hellman style private set intersection protocol (cf. [Mea86]). The attack is indistinguishable from ordinary protocol execution, and yet allows the attacker to learn the cardinality of the intersection of honest party&#x27;s input sets. This kind of attack demonstrates the inadequacy of semi-honest security guarantee when facing more serious adversarial threats, and highlights the necessity for security augmentation of protocols derived from [Mea86].

  匹配依据：MPC: private set intersection

  </details>

- **Privacy-Preserving Distributed Learning in the Analog Domain**
  2020-07-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.08803)
  Mahdi Soleymani, Hessam Mahdavifar, A. Salman Avestimehr

  <details><summary>摘要 / Abstract</summary>

  We consider the critical problem of distributed learning over data while keeping it private from the computational servers. The state-of-the-art approaches to this problem rely on quantizing the data into a finite field, so that the cryptographic approaches for secure multiparty computing can then be employed. These approaches, however, can result in substantial accuracy losses due to fixed-point representation of the data and computation overflows. To address these critical issues, we propose a novel algorithm to solve the problem when data is in the analog domain, e.g., the field of real/complex numbers. We characterize the privacy of the data from both information-theoretic and cryptographic perspectives, while establishing a connection between the two notions in the analog domain. More specifically, the well-known connection between the distinguishing security (DS) and the mutual information security (MIS) metrics is extended from the discrete domain to the continues domain. This is then utilized to bound the amount of information about the data leaked to the servers in our protocol, in terms of the DS metric, using well-known results on the capacity of single-input multiple-output (SIMO) channel with correlated noise. It is shown how the proposed framework can be adopted to do computation tasks when data is represented using floating-point numbers. We then show that this leads to a fundamental trade-off between the privacy level of data and accuracy of the result. As an application, we also show how to train a machine learning model while keeping the data as well as the trained model private. Then numerical results are shown for experiments on the MNIST dataset. Furthermore, experimental advantages are shown comparing to fixed-point implementations over finite fields.

  匹配依据：MPC: secure multiparty computing

  </details>

- **Gossiping For Communication-Efficient Broadcast**
  2020-07-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/894)
  Georgios Tsimos, Julian Loss, Charalampos Papamanthou

  <details><summary>摘要 / Abstract</summary>

  Byzantine Broadcast is crucial for many cryptographic protocols such as secret sharing, multiparty computation and blockchain consensus. In this paper we apply gossiping (propagating a message by sending to a few random parties who in turn do the same, until the message is delivered) and propose new communication-efficient protocols, under dishonest majority, for Single-Sender Broadcast (BC) and Parallel Broadcast (PBC), improving the state-of-the-art in several ways. As our warm-up result, we present a randomized protocol for BC which achieves $O(n^2\kappa^2)$ communication complexity from plain public key setup assumptions. This is the first protocol with subcubic communication in this setting, but operates only against static adversaries. Using ideas from our BC protocol, we move to our central contribution and present two protocols for PBC that are secure against adaptive adversaries. To the best of our knowledge we are the first to study PBC specifically: All previous approaches for Parallel Broadcast naively run $n$ instances of single-sender Broadcast, increasing the communication complexity by an undesirable factor of $n$. Our insight of avoiding black-box invocations of BC is particularly crucial for achieving our asymptotic improvements. In particular: 1. Our first PBC protocol achieves $\tilde{O}(n^3\kappa^2)$ communication complexity and relies only on plain public key setup assumptions. 2. Our second PBC protocol uses trusted setup and achieves nearly optimal communication complexity $\tilde{O}(n^2\kappa^4)$. Both PBC protocols yield an almost linear improvement over the best known solutions involving $n$ parallel invocations of the respective BC protocols such as those of Dolev and Strong (SIAM Journal on Computing, 1983) and Chan et al. (Public Key Cryptography, 2020). Central to our PBC protocols is a new problem that we define and solve, which we name &quot;Converge&quot;. In Converge, parties must run an adaptively-secure and efficient protocol such that by the end of the protocol, all honest parties that remain possess a superset of the union of the initial honest parties&#x27; inputs.

  匹配依据：MPC: multiparty computation, secret sharing

  </details>

- **A Blockchain-based Iterative Double Auction Protocol using Multiparty State Channels**
  2020-07-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.08595)
  Truc D. T. Nguyen, My T. Thai

  <details><summary>摘要 / Abstract</summary>

  Although the iterative double auction has been widely used in many different applications, one of the major problems in its current implementations is that they rely on a trusted third party to handle the auction process. This imposes the risk of single point of failures, monopoly, and bribery. In this paper, we aim to tackle this problem by proposing a novel decentralized and trustless framework for iterative double auction based on blockchain. Our design adopts the smart contract and state channel technologies to enable a double auction process among parties that do not need to trust each other, while minimizing the blockchain transactions. In specific, we propose an extension to the original concept of state channels that can support multiparty computation. Then we provide a formal development of the proposed framework and prove the security of our design against adversaries. Finally, we develop a proof-of-concept implementation of our framework using Elixir and Solidity, on which we conduct various experiments to demonstrate its feasibility and practicality.

  匹配依据：MPC: multiparty computation

  </details>

- **PrivColl: Practical Privacy-Preserving Collaborative Machine Learning**
  2020-07-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.06953)
  Yanjun Zhang, Guangdong Bai, Xue Li, Caitlin Curtis, Chen Chen, Ryan K L Ko

  <details><summary>摘要 / Abstract</summary>

  Collaborative learning enables two or more participants, each with their own training dataset, to collaboratively learn a joint model. It is desirable that the collaboration should not cause the disclosure of either the raw datasets of each individual owner or the local model parameters trained on them. This privacy-preservation requirement has been approached through differential privacy mechanisms, homomorphic encryption (HE) and secure multiparty computation (MPC), but existing attempts may either introduce the loss of model accuracy or imply significant computational and/or communicational overhead. In this work, we address this problem with the lightweight additive secret sharing technique. We propose PrivColl, a framework for protecting local data and local models while ensuring the correctness of training processes. PrivColl employs secret sharing technique for securely evaluating addition operations in a multiparty computation environment, and achieves practicability by employing only the homomorphic addition operations. We formally prove that it guarantees privacy preservation even though the majority (n-2 out of n) of participants are corrupted. With experiments on real-world datasets, we further demonstrate that PrivColl retains high efficiency. It achieves a speedup of more than 45X over the state-of-the-art MPC/HE based schemes for training linear/logistic regression, and 216X faster for training neural network.

  匹配依据：MPC: multiparty computation, secret sharing, secure multiparty computation

  </details>

- **BUNET: Blind Medical Image Segmentation Based on Secure UNET**
  2020-07-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.06855)
  Song Bian, Xiaowei Xu, Weiwen Jiang, Yiyu Shi, Takashi Sato

  <details><summary>摘要 / Abstract</summary>

  The strict security requirements placed on medical records by various privacy regulations become major obstacles in the age of big data. To ensure efficient machine learning as a service schemes while protecting data confidentiality, in this work, we propose blind UNET (BUNET), a secure protocol that implements privacy-preserving medical image segmentation based on the UNET architecture. In BUNET, we efficiently utilize cryptographic primitives such as homomorphic encryption and garbled circuits (GC) to design a complete secure protocol for the UNET neural architecture. In addition, we perform extensive architectural search in reducing the computational bottleneck of GC-based secure activation protocols with high-dimensional input data. In the experiment, we thoroughly examine the parameter space of our protocol, and show that we can achieve up to 14x inference time reduction compared to the-state-of-the-art secure inference technique on a baseline architecture with negligible accuracy degradation.

  匹配依据：MPC: garbled circuits

  </details>

- **Quantum Immune One-Time Memories**
  2020-07-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/871)
  Qipeng Liu, Amit Sahai, Mark Zhandry

  <details><summary>摘要 / Abstract</summary>

  One-time memories (OTM) are the hardware version of oblivious transfer, and are useful for constructing objects that are impossible with software alone, such as one-time programs. In this work, we consider attacks on OTMs where a quantum adversary can leverage his physical access to the memory to mount quantum ``superposition attacks&#x27;&#x27; against the memory. Such attacks result in significantly weakened OTMs. For example, in the application to one-time programs, it may appear that such an adversary can always “quantumize” the classical protocol by running it on a superposition of inputs, and therefore learn superpositions of outputs of the protocol. Perhaps surprisingly, we show that this intuition is false: we construct one-time programs from quantum-accessible one-time memories where the view of an adversary, despite making quantum queries, can be simulated by making only classical queries to the ideal functionality. At the heart of our work is a method of immunizing one-time memories against superposition attacks.

  匹配依据：MPC: oblivious transfer

  </details>

- **Protecting Cryptography Against Compelled Self-Incrimination**
  2020-07-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/862)
  Sarah Scheffler, Mayank Varia

  <details><summary>摘要 / Abstract</summary>

  The information security community has devoted substantial effort to the design, development, and universal deployment of strong encryption schemes that withstand search and seizure by computationally-powerful nation-state adversaries. In response, governments are increasingly turning to a different tactic: issuing subpoenas that compel people to decrypt devices themselves, under the penalty of contempt of court if they do not comply. Compelled decryption subpoenas sidestep questions around government search powers that have dominated the Crypto Wars and instead touch upon a different (and still unsettled) area of the law: how encryption relates to a person&#x27;s right to silence and against self-incrimination. In this work, we provide a rigorous, composable definition of a critical piece of the law that determines whether cryptosystems are vulnerable to government compelled disclosure in the United States. We justify our definition by showing that it is consistent with prior court cases. We prove that decryption is often not compellable by the government under our definition. Conversely, we show that many techniques that bolster security overall can leave one more vulnerable to compelled disclosure. As a result, we initiate the study of protecting cryptographic protocols against the threat of future compelled disclosure. We find that secure multi-party computation is particularly vulnerable to this threat, and we design and implement new schemes that are provably resilient in the face of government compelled disclosure. We believe this work should influence the design of future cryptographic primitives and contribute toward the legal debates over the constitutionality of compelled decryption.

  匹配依据：MPC: secure multi party computation

  </details>

- **Linear Complexity Private Set Intersection for Secure Two-Party Protocols**
  2020-07-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/864)
  Ferhat Karakoç, Alptekin Küpçü

  <details><summary>摘要 / Abstract</summary>

  In this paper, we propose a new private set intersection (PSI) protocol with bi-oblivious data transfer that computes the following functionality. One of the parties $P_1$ inputs a set of items $X$ and a set of data pairs $D_1 = \{ (d_0^j,d_1^j)\}$ and the other party $P_2$ inputs a set of items $Y$. While $P_1$ outputs nothing, $P_2$ outputs a set of data $D_2 = \{ d_{b_j}^j \mid b_j \in \{0,1\}\}$ dependent on the intersection of $X$ and $Y$. This functionality is generally required when the PSI protocol is used as a part of a larger secure two-party secure computation such as threshold PSI or any function of the whole intersecting set in general. Pinkas et al. presented a PSI protocol at Eurocrypt 2019 for this type of functionality, which has linear complexity only in communication. While there are PSI protocols with linear computation and communication complexities in the classical PSI setting where the intersection itself is revealed to one party, to the best of our knowledge, there is no PSI protocol, which outputs a function of the membership results and satisfies linear complexity in both communication and computation. We present the first PSI protocol that outputs only a function of the membership results with linear communication and computation complexities. While creating the protocol, as a side contribution, we provide a one-time batch oblivious programmable pseudo-random function based on garbled Bloom filters. We also implemented our protocol and provide performance results.

  匹配依据：MPC: private set intersection, secure computation

  </details>

- **Dumbo-MVBA: Optimal Multi-valued Validated Asynchronous Byzantine Agreement, Revisited**
  2020-07-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/842)
  Yuan Lu, Zhenliang Lu, Qiang Tang, Guiling Wang

  <details><summary>摘要 / Abstract</summary>

  Multi-valued validated asynchronous Byzantine agreement (MVBA), proposed in the elegant work of Cachin et al. (CRYPTO &#x27;01), is fundamental for critical fault-tolerant services such as atomic broadcast in the asynchronous network. It was left as an open problem to asymptotically reduce the $O(ln^2+n^2*lambda+n^3)$ communication (where $n$ is the number of parties, $l$ is the input length, and $lambda$ is the security parameter). Recently, Abraham et al. (PODC &#x27;19) removed the $n^3$ term to partially answer the question when input is small. However, in other typical cases, e.g., building atomic broadcast through MVBA, the input length $l &gt;= n*lambda$, and thus the communication is dominated by the $ln^2$ term and the problem raised by Cachin et al. remains open. We fill the gap and answer the remaining part of the above open problem. In particular, we present two MVBA protocols with $O(ln+n^2*lambda)$ communicated bits, which is optimal when $l &gt;= n*lambda$. We also maintain other benefits including optimal resilience to tolerate up to $n/3$ adaptive Byzantine corruptions, optimal expected constant running time, and optimal $O(n^2)$ messages. At the core of our design, we propose asynchronous provable dispersal broadcast (APDB) in which each input can be split and dispersed to every party and later recovered in an efficient way. Leveraging APDB and asynchronous binary agreement, we design an optimal MVBA protocol, Dumbo-MVBA; we also present a general self-bootstrap framework Dumbo-MVBA* to reduce the communication of any existing MVBA protocols. Finally, we demonstrate an enticing application of our $\mathsf{MVBA}$ protocols to construct expected constant-round asynchronous common subset ($\mathsf{ACS}$) with only $\mathcal{O}(\ell n^2 +\lambda n^2)$ communication complexity in expect, where $\ell$ is the input length of $\mathsf{ACS}$ represented in bits. The resulting $\mathsf{ACS}$ has asymptotically optimal communication cost when $\ell\geq\lambda$ and might have a broad array of applications like asynchronous atomic broadcasts or asynchronous multi-party computation.

  匹配依据：MPC: multi party computation

  </details>

- **Asynchronous Byzantine Agreement with Subquadratic Communication**
  2020-07-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/851)
  Erica Blum, Jonathan Katz, Chen-Da Liu-Zhang, Julian Loss

  <details><summary>摘要 / Abstract</summary>

  Understanding the communication complexity of Byzantine agreement (BA) is a fundamental problem in distributed computing. In particular, as protocols are run with a large number of parties (as, e.g., in the context of blockchain protocols), it is important to understand the dependence of the communication on the number of parties $n$. Although adaptively secure BA protocols with $o(n^2)$ communication are known in the synchronous and partially synchronous settings, no such protocols are known in the fully asynchronous case. We show here an asynchronous BA protocol with subquadratic communication tolerating an adaptive adversary who can corrupt $f 0$). One variant of our protocol assumes initial setup done by a trusted dealer, after which an unbounded number of BA executions can be run; alternately, we can achieve subquadratic amortized communication with no prior setup. We also show that some form of setup is needed for (non-amortized) subquadratic BA tolerating $\Theta(n)$ corrupted parties. As a contribution of independent interest, we show a secure-computation protocol in the same threat model that has $o(n^2)$ communication when computing no-input functionalities with short output (e.g., coin tossing).

  匹配依据：MPC: secure computation

  </details>

- **Imperfect 1-out-of-2 quantum oblivious transfer: bounds, a protocol, and its experimental implementation**
  2020-07-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.04712)
  Ryan Amiri, Robert Stárek, David Reichmuth, Ittoop V Puthoor, Michal Mičuda, Ladislav Mišta, Miloslav Dušek, Petros Wallden, Erika Andersson

  <details><summary>摘要 / Abstract</summary>

  Oblivious transfer is an important primitive in modern cryptography. Applications include secure multiparty computation, oblivious sampling, e-voting, and signatures. Information-theoretically secure perfect 1-out-of 2 oblivious transfer is impossible to achieve. Imperfect variants, where both participants&#x27; ability to cheat is still limited, are possible using quantum means while remaining classically impossible. Precisely what security parameters are attainable remains unknown. We introduce a theoretical framework for studying semirandom quantum oblivious transfer, which is shown to be equivalent to regular oblivious transfer in terms of cheating probabilities. We then use it to derive bounds on cheating. We also present a protocol with lower cheating probabilities than previous schemes, together with its optical realization. We show that a lower bound of 2/3 on the minimum achievable cheating probability can be directly derived for semirandom protocols using a different method and definition of cheating than used previously. The lower bound increases from 2/3 to approximately 0.749 if the states output by the protocol are pure and symmetric. The oblivious transfer scheme we present uses unambiguous state elimination measurements and can be implemented with the same technological requirements as standard quantum cryptography. The cheating probabilities are 3/4 and approximately 0.729 for sender and receiver respectively, which is lower than in existing protocols. Using a photonic test-bed, we have implemented the protocol with honest parties, as well as optimal cheating strategies.

  匹配依据：MPC: oblivious transfer, secure multiparty computation

  </details>

- **Secure Distributed Matrix Computation with Discrete Fourier Transform**
  2020-07-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.03972)
  Nitish Mital, Cong Ling, Deniz Gunduz

  <details><summary>摘要 / Abstract</summary>

  We consider the problem of secure distributed matrix computation (SDMC), where a \textit{user} queries a function of data matrices generated at distributed \textit{source} nodes. We assume the availability of $N$ honest but curious computation servers, which are connected to the sources, the user, and each other through orthogonal and reliable communication links. Our goal is to minimize the amount of data that must be transmitted from the sources to the servers, called the \textit{upload cost}, while guaranteeing that no $T$ colluding servers can learn any information about the source matrices, and the user cannot learn any information beyond the computation result. We first focus on secure distributed matrix multiplication (SDMM), considering two matrices, and propose a novel polynomial coding scheme using the properties of finite field discrete Fourier transform, which achieves an upload cost significantly lower than the existing results in the literature. We then generalize the proposed scheme to include straggler mitigation, and to the multiplication of multiple matrices while keeping the input matrices, the intermediate computation results, as well as the final result secure against any $T$ colluding servers. We also consider a special case, called computation with own data, where the data matrices used for computation belong to the user. In this case, we drop the security requirement against the user, and show that the proposed scheme achieves the minimal upload cost. We then propose methods for performing other common matrix computations securely on distributed servers, including changing the parameters of secret sharing, matrix transpose, matrix exponentiation, solving a linear system, and matrix inversion, which are then used to show how arbitrary matrix polynomials can be computed securely on distributed servers using the proposed procedure.

  匹配依据：MPC: secret sharing

  </details>

- **Open-Pub: A Transparent yet Privacy-Preserving Academic Publication System based on Blockchain**
  2020-07-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.03915)
  Yan Zhou, Zhiguo Wan, Zhangshuang Guan

  <details><summary>摘要 / Abstract</summary>

  Academic publications of latest research results are crucial to advance the development of all disciplines. However, there are several severe disadvantages in current academic publication systems. The first is the misconduct during the publication process due to the opaque paper review process. An anonymous reviewer may give biased comments to a paper without being noticed because the comments are seldom published for evaluation. Second, access to research papers is restricted to only subscribers, and even the authors cannot access their own papers. To address the above problems, we propose Open-Pub, a decentralized, transparent yet privacy-preserving academic publication scheme using the blockchain technology. In Open-Pub, we first design a threshold identity-based group signature (TIBGS) that protects identities of signers using verifiable secret sharing. Then we develop a strong double-blind mechanism to protect the identities of authors and reviewers. With this strong double-blind mechanism, authors can choose to submit papers anonymously, and validators distribute papers anonymously to reviewers on the blockchain according to their research interests. This process is publicly recorded and traceable on the blockchain so as to realize transparent peer preview. To evaluate its efficiency, we implement Open-Pub based on Ethereum and conduct comprehensive experiments to evaluate its performance, including computation cost and processing delay. The experiment results show that Open-Pub is highly efficient in computation and processing anonymous transactions.

  匹配依据：MPC: secret sharing

  </details>

- **MPC Protocol for G-module and its Application in Secure Compare and ReLU**
  2020-07-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.03975)
  Qizhi Zhang, Lichun Li, Shan Yin, Juanjuan Sun

  <details><summary>摘要 / Abstract</summary>

  Secure comparison and secure selection are two fundamental MPC (secure Multi-Party Computation) protocols. One important application of these protocols is the secure ReLU and DReLU computation in privacy preserving deep learning. In this paper, we introduce G-module, a mathematics tool, to re-design such protocols. In mathematics, given a group G, a G-module is an abelian group M on which G acts compatibly with the abelian group structure on M. We design three secure protocols for three G-module operations. i.e. &quot;G-module action&quot;, &quot;Cross G-module action&quot; and &quot;G-module recover&quot;. As far as we know, this is the first work on secure G-module operations. Based on them, we design secure comparison, selection, ReLU and DReLU protocols, which improve communication efficiency by 2X to 10X compared with state of arts. Our protocols are very computation efficient too. They do not require public key operations or any other expensive operations.

  匹配依据：MPC: secure multi party computation

  </details>

- **Multi-player Equilibria Verification for Concurrent Stochastic Games**
  2020-07-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.03365)
  Marta Kwiatkowska, Gethin Norman, David Parker, Gabriel Santos

  <details><summary>摘要 / Abstract</summary>

  Concurrent stochastic games (CSGs) are an ideal formalism for modelling probabilistic systems that feature multiple players or components with distinct objectives making concurrent, rational decisions. Examples include communication or security protocols and multi-robot navigation. Verification methods for CSGs exist but are limited to scenarios where agents or players are grouped into two coalitions, with those in the same coalition sharing an identical objective. In this paper, we propose multi-coalitional verification techniques for CSGs. We use subgame-perfect social welfare (or social cost) optimal Nash equilibria, which are strategies where there is no incentive for any coalition to unilaterally change its strategy in any game state, and where the total combined objectives are maximised (or minimised). We present an extension of the temporal logic rPATL (probabilistic alternating-time temporal logic with rewards) to specify equilibria-based properties for any number of distinct coalitions, and a corresponding model checking algorithm for a variant of stopping games. We implement our techniques in the PRISM-games tool and apply them to several case studies, including a secret sharing protocol and a public good game.

  匹配依据：MPC: secret sharing

  </details>

- **UC-Secure OT from LWE, Revisited**
  2020-07-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/819)
  Willy Quach

  <details><summary>摘要 / Abstract</summary>

  We build a two-round, UC-secure oblivious transfer protocol (OT) in the common reference string (CRS) model under the Learning with Errors assumption (LWE) with sub-exponential modulus-to-noise ratio. We do so by instantiating the dual-mode encryption framework of Peikert, Vaikuntanathan and Waters (CRYPTO&#x27;08). The resulting OT can be instantiated in either one of two modes: one providing statistical sender security, and the other statistical receiver security. Furthermore, our scheme allows the sender and the receiver to reuse the CRS across arbitrarily many executions of the protocol. To the best of our knowledge, this gives the first construction of a UC-secure OT from LWE that achieves both statistical receiver security and unbounded reusability of the CRS. For comparison, there was, until recently, no such construction from LWE satisfying either one of these two properties. In particular, the construction of UC-secure OT from LWE of Peikert, Vaikuntanathan and Waters only provides computational receiver security and bounded reusability of the CRS. Our main technical contribution is a public-key encryption scheme from LWE where messy public keys (under which encryptions hide the underlying message statistically) can be recognized in time essentially independent of the LWE modulus $q$.

  匹配依据：MPC: oblivious transfer

  </details>

- **Dispelling Myths on Superposition Attacks: Formal Security Model and Attack Analyses**
  2020-07-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.00677) · [IACR ePrint](https://eprint.iacr.org/2020/816)
  Luka Music, Céline Chevalier, Elham Kashefi

  <details><summary>摘要 / Abstract</summary>

  It is of folkloric belief that the security of classical cryptographic protocols is automatically broken if the Adversary is allowed to perform superposition queries and the honest players forced to perform actions coherently on quantum states. Another widely held intuition is that enforcing measurements on the exchanged messages is enough to protect protocols from these attacks. However, the reality is much more complex. Security models dealing with superposition attacks only consider unconditional security. Conversely, security models considering computational security assume that all supposedly classical messages are measured, which forbids by construction the analysis of superposition attacks. Boneh and Zhandry have started to study the quantum computational security for classical primitives in their seminal work at Crypto&#x27;13, but only in the single-party setting. To the best of our knowledge, an equivalent model in the multiparty setting is still missing. In this work, we propose the first computational security model considering superposition attacks for multiparty protocols. We show that our new security model is satisfiable by proving the security of the well-known One-Time-Pad protocol and give an attack on a variant of the equally reputable Yao Protocol for Secure Two-Party Computations. The post-mortem of this attack reveals the precise points of failure, yielding highly counter-intuitive results: Adding extra classical communication, which is harmless for classical security, can make the protocol become subject to superposition attacks. We use this newly imparted knowledge to construct the first concrete protocol for Secure Two-Party Computation that is resistant to superposition attacks. Our results show that there is no straightforward answer to provide for either the vulnerabilities of classical protocols to superposition attacks or the adapted countermeasures.

  匹配依据：MPC: secure two party computation

  </details>

- **Secret Sharing MPC on FPGAs in the Datacenter**
  2020-07-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.00826)
  Pierre-Francois Wolfe, Rushi Patel, Robert Munafo, Mayank Varia, Martin Herbordt

  <details><summary>摘要 / Abstract</summary>

  Multi-Party Computation (MPC) is a technique enabling data from several sources to be used in a secure computation revealing only the result while protecting the original data, facilitating shared utilization of data sets gathered by different entities. The presence of Field Programmable Gate Array (FPGA) hardware in datacenters can provide accelerated computing as well as low latency, high bandwidth communication that bolsters the performance of MPC and lowers the barrier to using MPC for many applications. In this work, we propose a Secret Sharing FPGA design based on the protocol described by Araki et al. We compare our hardware design to the original authors&#x27; software implementations of Secret Sharing and to work accelerating MPC protocols based on Garbled Circuits with FPGAs. Our conclusion is that Secret Sharing in the datacenter is competitive and when implemented on FPGA hardware was able to use at least 10$\times$ fewer computer resources than the original work using CPUs.

  匹配依据：MPC: garbled circuits, multi party computation, secret sharing, secure computation

  </details>

- **Private Speech Classification with Secure Multiparty Computation**
  2020-07-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2007.00253)
  Kyle Bittner, Martine De Cock, Rafael Dowsley

  <details><summary>摘要 / Abstract</summary>

  Deep learning in audio signal processing, such as human voice audio signal classification, is a rich application area of machine learning. Legitimate use cases include voice authentication, gunfire detection, and emotion recognition. While there are clear advantages to automated human speech classification, application developers can gain knowledge beyond the professed scope from unprotected audio signal processing. In this paper we propose the first privacy-preserving solution for deep learning-based audio classification that is provably secure. Our approach, which is based on Secure Multiparty Computation, allows to classify a speech signal of one party (Alice) with a deep neural network of another party (Bob) without Bob ever seeing Alice&#x27;s speech signal in an unencrypted manner. As threat models, we consider both passive security, i.e. with semi-honest parties who follow the instructions of the cryptographic protocols, as well as active security, i.e. with malicious parties who deviate from the protocols. We evaluate the efficiency-security-accuracy trade-off of the proposed solution in a use case for privacy-preserving emotion detection from speech with a convolutional neural network. In the semi-honest case we can classify a speech signal in under 0.3 sec; in the malicious case it takes $\sim$1.6 sec. In both cases there is no leakage of information, and we achieve classification accuracies that are the same as when computations are done on unencrypted data.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Secure merge with $O(n \\log \\log n)$ secure operation**
  2020-06-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/807)
  Brett Hemenway Falk, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  Data-oblivious algorithms are a key component of many secure computation protocols. In this work, we show that advances in secure multiparty shuffling algorithms can be used to increase the efficiency of several key cryptographic tools. The key observation is that many secure computation protocols rely heavily on secure shuffles. The best data-oblivious shuffling algorithms require $O(n \log n)$, operations, but in the two-party or multiparty setting, secure shuffling can be achieved with only $O(n)$ communication. Leveraging the efficiency of secure multiparty shuffling, we give novel algorithms that improve the efficiency of securely sorting sparse lists, secure stable compaction, and securely merging two sorted lists. Securely sorting private lists is a key component of many larger secure computation protocols. The best data-oblivious sorting algorithms for sorting a list of $n$ elements require $O(n \log n)$ comparisons. Using black-box access to a linear-communication secure shuffle, we give a secure algorithm for sorting a list of length $n$ with $t \ll n$ nonzero elements with communication $O(t \log^2 n + n)$, which beats the best oblivious algorithms when the number of nonzero elements, $t$, satisfies $t &lt; n/\log^2 n$. Secure compaction is the problem of removing dummy elements from a list, and is essentially equivalent to sorting on 1-bit keys. The best oblivious compaction algorithms run in $O(n)$-time, but they are unstable, i.e., the order of the remaining elements is not preserved. Using black-box access to a linear-communication secure shuffle, we give a stable compaction algorithm with only $O(n)$ communication. Our main result is a novel secure merge protocol. The best previous algorithms for securely merging two sorted lists into a sorted whole required $O(n \log n)$ secure operations. Using black-box access to an $O(n)$-communication secure shuffle, we give the first secure merge algorithm that requires only $O(n \log \log n)$ communication. Our algorithm takes as input $n$ secret-shared values, and outputs a secret-sharing of the sorted list. All our algorithms are generic, i.e., they can be implemented using generic secure computations techniques and make black-box access to a secure shuffle. Our techniques extend naturally to the multiparty situation (with a constant number of parties) as well as to handle malicious adversaries without changing the asymptotic efficiency. These algorithm have applications to securely computing database joins and order statistics on private data as well as multiparty Oblivious RAM protocols.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Revisiting Asynchronous Fault Tolerant Computation with Optimal Resilience**
  2020-06-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2006.16686)
  Ittai Abraham, Danny Dolev, Gilad Stern

  <details><summary>摘要 / Abstract</summary>

  The celebrated result of Fischer, Lynch and Paterson is the fundamental lower bound for asynchronous fault tolerant computation: any 1-crash resilient asynchronous agreement protocol must have some (possibly measure zero) probability of not terminating. In 1994, Ben-Or, Kelmer and Rabin published a proof-sketch of a lesser known lower bound for asynchronous fault tolerant computation with optimal resilience against a Byzantine adversary: if $n\le 4t$ then any t-resilient asynchronous verifiable secret sharing protocol must have some non-zero probability of not terminating. Our main contribution is to revisit this lower bound and provide a rigorous and more general proof. Our second contribution is to show how to avoid this lower bound. We provide a protocol with optimal resilience that is almost surely terminating for a strong common coin functionality. Using this new primitive we provide an almost surely terminating protocol with optimal resilience for asynchronous Byzantine agreement that has a new fair validity property. To the best of our knowledge this is the first asynchronous Byzantine agreement with fair validity in the information theoretic setting.

  匹配依据：MPC: secret sharing

  </details>

- **Superposition Attack on OT Protocols**
  2020-06-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/798)
  Ehsan Ebrahimi, Céline Chevalier, Marc Kaplan, Michele Minelli

  <details><summary>摘要 / Abstract</summary>

  In this note, we study the security of oblivious transfer protocols in the presence of adversarial superposition queries. We define a security notion for the sender against a corrupted receiver that makes a superposition query. We present an oblivious transfer protocol that is secure against a quantum receiver restricted to a classical query but it is insecure when the receiver makes a quantum query.

  匹配依据：MPC: oblivious transfer

  </details>

- **CRAFT: Composable Randomness Beacons and Output-Independent Abort MPC From Time**
  2020-06-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/784)
  Carsten Baum, Bernardo David, Rafael Dowsley, Ravi Kishore, Jesper Buus Nielsen, Sabine Oechsner

  <details><summary>摘要 / Abstract</summary>

  Recently, time-based primitives such as time-lock puzzles (TLPs) and verifiable delay functions (VDFs) have received a lot of attention due to their power as building blocks for cryptographic protocols. However, even though exciting improvements on their efficiency and security (e.g. achieving non-malleability) have been made, most of the existing constructions do not offer general composability guarantees and thus have limited applicability. Baum et al. (EUROCRYPT 2021) presented in TARDIS the first (im)possibility results on constructing TLPs with Universally Composable (UC) security and an application to secure two party computation with output-independent abort (OIA-2PC), where an adversary has to decide to abort before learning the output. While these results establish the feasibility of UC-secure TLPs and applications, they are limited to the two-party scenario and suffer from complexity overheads. In this paper, we introduce the first UC constructions of VDFs and of the related notion of publicly verifiable TLPs (PV-TLPs). We use our new UC VDF to prove a folklore result on VDF-based randomness beacons used in industry and build an improved randomness beacon from our new UC PV-TLPs. We moreover construct the first multiparty computation protocol with punishable output-independent aborts (POIA MPC), i.e. MPC with OIA and financial punishment for cheating. Our novel POIA-MPC both establishes the feasibility of (non-punishable) OIA-MPC and significantly improves on the efficiency of state-of-the-art OIA-2PC and (non-OIA) MPC with punishable aborts.

  匹配依据：MPC: multiparty computation, secure two party computation

  </details>

- **Adventures in Crypto Dark Matter: Attacks, Fixes for Weak Pseudorandom Functions**
  2020-06-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/783)
  Jung Hee Cheon, Wonhee Cho, Jeong Han Kim, Jiseung Kim

  <details><summary>摘要 / Abstract</summary>

  A weak pseudorandom function (weak PRF) is one of the most important cryptographic primitives for its efficiency although it has lower security than a standard PRF. Recently, Boneh et al. (TCC&#x27;18) introduced two types of new weak PRF candidates, which are called a basic Mod-2/Mod-3 and alternative Mod-2/Mod-3 weak PRF. Both use the mixture of linear computations defined on different small moduli to satisfy conceptual simplicity, low complexity (depth-2 ${\sf ACC^0}$) and MPC friendliness. In fact, the new candidates are conjectured to be exponentially secure against any adversary that allows exponentially many samples, and a basic Mod-2/Mod-3 weak PRF is the only candidate that satisfies all features above. However, none of the direct attacks which focus on basic and alternative Mod-2/Mod-3 weak PRFs use their own structures. In this paper, we investigate weak PRFs from two perspectives; attacks, fixes. We first propose direct attacks for an alternative Mod-2/Mod-3 weak PRF and a basic Mod-2/Mod-3 weak PRF when a circulant matrix is used as a secret key. For an alternative Mod-2/Mod-3 weak PRF, we prove that the adversary&#x27;s advantage is at least $2^{-0.105n}$, where $n$ is the size of the input space of the weak PRF. Similarly, we show that the advantage of our heuristic attack to the weak PRF with a circulant matrix key is larger than $2^{-0.21n}$, which is contrary to the previous expectation that `structured secret key&#x27; does not affect the security of a weak PRF. Thus, for an optimistic parameter choice $n = 2\lambda$ for the security parameter $\lambda$, parameters should be increased to preserve $\lambda$-bit security when an adversary obtains exponentially many samples. Next, we suggest a simple method for repairing two weak PRFs affected by our attack while preserving the parameters.

  匹配依据：MPC: mpc (context)

  </details>

- **Efficient Constant-Round MPC with Identifiable Abort and Public Verifiability**
  2020-06-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/767)
  Carsten Baum, Emmanuela Orsini, Peter Scholl, Eduardo Soria-Vazquez

  <details><summary>摘要 / Abstract</summary>

  Recent years have seen a tremendous growth in the interest in secure multiparty computation (MPC) and its applications. While much progress has been made concerning its efficiency, many current, state-of-the-art protocols are vulnerable to Denial of Service attacks, where a cheating party may prevent the honest parties from learning the output of the computation, whilst remaining anonymous. The security model of identifiable abort aims to prevent these attacks, by allowing honest parties to agree upon the identity of a cheating party, who can then be excluded in the future. Several existing MPC protocols offer security with identifiable abort against a dishonest majority of corrupted parties. However, all of these protocols have a round complexity that scales linearly with the depth of the circuit (and are therefore unsuitable for use in high latency networks) or use cryptographic primitives or techniques that have a high computational overhead. In this work, we present the first efficient MPC protocols with identifiable abort in the dishonest majority setting, which run in a constant number of rounds and make only black-box use of cryptographic primitives. Our main construction is built from highly efficient primitives in a careful way to achieve identifiability at a low cost. In particular, we avoid the use of public-key operations outside of a setup phase, incurring a relatively low overhead on top of the fastest currently known constant-round MPC protocols based on garbled circuits. Our construction also avoids the use of adaptively secure primitives and heavy zero-knowledge machinery, which was inherent in previous works. In addition, we show how to upgrade our protocol to achieve public verifiability using a public bulletin board, allowing any external party to verify correctness of the computation or identify a cheating party.

  匹配依据：MPC: garbled circuits, secure multiparty computation

  </details>

- **A Hybrid Quantum Secret Sharing Scheme based on Mutually Unbiased Bases**
  2020-06-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2006.12790)
  Dan-Li Zhi, Zhu-Hui Li, Li-juan Liu, Zhao-Wei Han

  <details><summary>摘要 / Abstract</summary>

  With the advantages of both classical and quantum secret sharing, many practical hybrid quantum secret sharing have been proposed. In this paper, we propose a hybrid quantum secret sharing scheme based on mutually unbiased bases and monotone span program. First, the dealer sends the shares in the linear secret sharing to the participants in the authorization set via a secure channel. Then, the dealer and participants perform unitary transformation on a d-dimensional quantum state sequentially, and the dealer publishes the measurement result confidentially to the participants in the authorization set to recover the secret. The verifiability of the scheme is guaranteed by the Hash function. Next, the correctness and security of the scheme are proved and our scheme is secure against the general eavesdropper attacks. Finally, a specific example is employed to further clarify the exibility of the scheme and the detailed comparison of similar quantum secret sharing schemes also shows the superiority of our proposed scheme.

  匹配依据：MPC: secret sharing

  </details>

- **Compressing Proofs of $k$-Out-Of-$n$ Partial Knowledge**
  2020-06-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/753)
  Thomas Attema, Ronald Cramer, Serge Fehr

  <details><summary>摘要 / Abstract</summary>

  In an (honest-verifier) zero-knowledge proof of partial knowledge, introduced by Cramer, Damgård and Schoenmakers (CRYPTO 1994), a prover knowing witnesses for some $k$-subset of $n$ given public statements can convince the verifier of this claim without revealing which $k$-subset. The accompanying solution combines $\Sigma$-protocol theory and linear secret sharing, and achieves linear communication complexity for general $k,n$. Especially the ``one-out-of-$n$&#x27;&#x27; case $k=1$ has seen myriad applications during the last decades, e.g., in electronic voting, ring signatures, and confidential transaction systems in general. In this paper we focus on the discrete logarithm (DL) setting, where the prover claims knowledge of DLs of $k$-out-of-$n$ given elements. Groth and Kohlweiss (EUROCRYPT 2015) have shown how to solve the special case $k=1$ with logarithmic (in $n$) communication, instead of linear as prior work. However, their method takes explicit advantage of $k=1$ and does not generalize to $k&gt;1$ without losing all advantage over prior work. Alternatively, an indirect approach for solving the considered problem is by translating the $k$-out-of-$n$ relation into a circuit and then applying recent advances in communication-efficient circuit ZK. Indeed, for the $k=1$ case this approach has been highly optimized, e.g., in ZCash. Our main contribution is a new, simple honest-verifier zero-knowledge proof protocol for proving knowledge of $k$ out of $n$ DLs with logarithmic communication and for general $k$ and $n$, without requiring any generic circuit ZK machinery. Our solution puts forward a novel extension of the compressed $\Sigma$-protocol theory (CRYPTO 2020), which we then utilize to compress a new $\Sigma$-protocol for proving knowledge of $k$-out-of-$n$ DL&#x27;s down to logarithmic size. The latter $\Sigma$-protocol is inspired by the CRYPTO 1994 approach, but a careful re-design of the original protocol is necessary for the compression technique to apply. Interestingly, even for $k=1$ and general $n$ our approach improves prior direct approaches as it reduces prover complexity without increasing the communication complexity. Besides the conceptual simplicity, we also identify regimes of practical relevance where our approach achieves asymptotic and concrete improvements, e.g., in proof size and prover complexity, over the generic approach based on circuit-ZK. Finally, we show various extensions and generalizations of our core result. For instance, we extend our protocol to proofs of partial knowledge of Pedersen (vector) commitment openings, and/or to include a proof that the witness satisfies some additional constraint, and we show how to extend our results to non-threshold access structures.

  匹配依据：MPC: secret sharing

  </details>

- **Communication-Efficient (Proactive) Secure Computation for Dynamic General Adversary Structures and Dynamic Groups**
  2020-06-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/747)
  Karim Eldefrawy, Seoyeon Hwang, Rafail Ostrovsky, Moti Yung

  <details><summary>摘要 / Abstract</summary>

  In modern distributed systems, an adversary’s limitations when corrupting subsets of servers may not necessarily be based on threshold constraints, but rather based on other technical or organizational characteristics in the systems. This means that the corruption patterns (and thus protection guarantees) are not based on the adversary being limited by a threshold, but on the adversary being limited by other constraints, in particular by what is known as a General Adversary Structure (GAS). We consider efficient secure multiparty computation (MPC) under such dynamically-changing GAS settings. During these changes, one desires to protect against and during corruption profile change, which renders some (secret sharing-based) encoding schemes underlying the MPC protocol more efficient than others when operating with the (currently) considered GAS. One of our contributions is a set of novel protocols to efficiently and securely convert back and forth between different MPC schemes for GAS; this process is often called share conversion. Specifically, we consider two MPC schemes, one based on additive secret sharing and the other based on Monotone Span Programs (MSP). The ability to efficiently convert between the secret sharing representations of these MPC schemes enables us to construct the first communication-efficient structure-adaptive proactive MPC protocol for dynamic GAS settings. By structure-adaptive, we mean that the choice of the MPC protocol to execute in future rounds after the GAS is changed (as specified by an administrative entity) is chosen to ensure communication-efficiency (the typical bottleneck in MPC). Furthermore, since such secure collaborative computing may be long-lived, we consider the mobile adversary setting, often called the proactive security setting. As our second contribution, we construct communication-efficient MPC protocols that can adapt to the proactive security setting. Proactive security assumes that at each (well defined) period of time the adversary corrupts different parties and over time may visit the entire system and corrupt all parties, provided that in each period it controls groups obeying the GAS constraints. In our protocol, the shares can be refreshed, meaning that parties receive new shares reconstructing the same secret, and some parties who lost their shares because of the reboot/resetting can recover their shares. As our third contribution, we consider another aspect of global long-term computations, namely, that of the dynamic groups. It is worth pointing out that such a setting with dynamic groups and GAS was not dealt with in existing literature on (proactive) MPC. In dynamic group settings, parties can be added and eliminated from the computation, under different GAS restrictions. We extend our protocols to this additional dynamic group settings defined by different GAS.

  匹配依据：MPC: secret sharing, secure computation, secure multiparty computation

  </details>

- **Anonymous probabilistic payment in payment hub**
  2020-06-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/748)
  Tatsuo Mitani, Akira Otsuka

  <details><summary>摘要 / Abstract</summary>

  Privacy protection and scalability are significant issues with blockchain. We propose an anonymous probabilistic payment under the general functionality for solving them. We consider the situation that several payers pay several payees through a tumbler. We have mediated the tumbler of the payment channel hub between payers and payees. Unlinkability means that the link, which payer pays which payee via the tumbler, is broken. A cryptographic puzzle plays a role in controlling the intermediation and execution of transactions. Masking the puzzle enables the payer and the payee to unlink their payments. The overview of the proposed protocol is similar to TumbleBit (NDSS 2017). We confirm the protocol realizes the ideal functionalities discussed in TumbleBit. The functionality required for our proposal is the hashed time lock contract that various cryptocurrencies use. This request is general, not restricted to any particular cryptocurrency. Our proposal includes a probabilistic payment. In probabilistic payment, one pays an ordinary mount with a certain probability. One pays a small amount as an expected value. One can run fewer transactions than a deterministic payment. It contributes scalability. We introduce a novel fractional oblivious transfer for probabilistic payment. We call it the ring fractional oblivious transfer (RFOT). RFOT is based on the ring learning with errors (RLWE) encryption. Our trick is based on the fact that an element of the ring is indistinguishable from the circular shifted element. We confirm that RFOT holds the properties of fractional hiding and binding presented in the DAM scheme (Eurocrypt 2017).

  匹配依据：MPC: oblivious transfer

  </details>

- **Binary linear codes with few weights from Boolean functions**
  2020-06-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2006.09591)
  Xiaoqiang Wang, Dabin Zheng, Yan Zhang

  <details><summary>摘要 / Abstract</summary>

  Boolean functions have very nice applications in cryptography and coding theory, which have led to a lot of research focusing on their applications. The objective of this paper is to construct binary linear codes with few weights from the defining set, which is defined by some special Boolean functions and some additional restrictions. First, we provide two general constructions of binary linear codes with three or four weights from Boolean functions with at most three Walsh transform values and determine the parameters of their dual codes. Then many classes of binary linear codes with explicit weight enumerators are obtained. Some binary linear codes and their duals obtained are optimal or almost optimal. The binary linear codes obtained in this paper may have a special interest in secret sharing schemes, association schemes, strongly regular graphs.

  匹配依据：MPC: secret sharing

  </details>

- **Multi-Party Revocation in Sovrin: Performance through Distributed Trust**
  2020-06-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/724)
  Lukas Helminger, Daniel Kales, Sebastian Ramacher, Roman Walch

  <details><summary>摘要 / Abstract</summary>

  Accumulators provide compact representations of large sets and compact membership witnesses. Besides constant-size witnesses, public-key accumulators provide efficient updates of both the accumulator itself and the witness. However, bilinear group based accumulators come with drawbacks: they require a trusted setup and their performance is not practical for real-world applications with large sets. In this paper, we introduce multi-party public-key accumulators dubbed dynamic (threshold) secret-shared accumulators. We present an instantiation using bilinear groups having access to more efficient witness generation and update algorithms that utilize the shares of the secret trapdoors sampled by the parties generating the public parameters. Specifically, for the q-SDH-based accumulators, we provide a maliciously-secure variant sped up by a secure multi-party computation (MPC) protocol (IMACC&#x27;19) built on top of SPDZ and a maliciously secure threshold variant built with Shamir secret sharing. For these schemes, a performant proof-of-concept implementation is provided, which substantiates the practicability of public-key accumulators in this setting. We explore applications of dynamic (threshold) secret-shared accumulators to revocation schemes of group signatures and credentials system. In particular, we consider it as part of Sovrin&#x27;s system for anonymous credentials where credentials are issued by the foundation of trusted nodes.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **MP2ML: A Mixed-Protocol Machine Learning Framework for Private Inference**
  2020-06-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/721)
  Fabian Boemer, Rosario Cammarota, Daniel Demmler, Thomas Schneider, Hossein Yalame

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving machine learning (PPML) has many applications, from medical image classification and anomaly detection to financial analysis. nGraph-HE enables data scientists to perform private inference of deep learning (DL) models trained using popular frameworks such as TensorFlow. nGraph-HE computes linear layers using the CKKS homomorphic encryption (HE) scheme. The non-polynomial activation functions, such as MaxPool and ReLU, are evaluated in the clear by the data owner who obtains the intermediate feature maps. This leaks the feature maps to the data owner from which it may be possible to deduce the DL model weights. As a result, such protocols may not be suitable for deployment, especially when the DL model is intellectual property. In this work, we present MP2ML, a machine learning framework which integrates nGraph-HE and the secure two-party computation framework ABY, to overcome the limitations of leaking the intermediate feature maps to the data owner. We introduce a novel scheme for the conversion between CKKS and secure multi-party computation to execute DL inference while maintaining the privacy of both the input data and model weights. MP2ML is compatible with popular DL frameworks such as TensorFlow that can infer pre-trained neural networks with native ReLU activations. We benchmark MP2ML on the CryptoNets network with ReLU activations, on which it achieves a throughput of 33.3 images/s and an accuracy of 98.6%. This throughput matches the previous state-of-the-art work, even though our protocol is more accurate and scalable.

  匹配依据：MPC: secure multi party computation, secure two party computation

  </details>

- **Hypercube and Cascading-based Algorithms for Secret Sharing Schemes**
  2020-06-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/719)
  Shion Samadder Chaudhury, Sabyasachi Dutta, Kouichi Sakurai

  <details><summary>摘要 / Abstract</summary>

  Secret sharing is a very useful way to maintain secrecy of private data when stored in a distributed way among several nodes. Two significant questions in this area are 1. how to accommodate new nodes and assign shares to the new nodes, the problem becomes harder if the number of joining nodes or the access structure is not known in advance and can be (potentially) unbounded and 2. to reduce the computational complexity of secret sharing schemes. In this paper we propose two new constructions of such secret sharing schemes based on different combinatorial structures. The first construction is based on generalized paths joining the opposite vertices of a hypercube which has been divided into smaller hypercubes. The second construction is a forest- based construction utilizing a dynamic data structure technique known as fractional cascading. The generalized path we call a pavement is new to this paper. Both our constructions use a new secret redistribution scheme to assign and re-assign shares to nodes. Towards the second question we show that allowing certain trade-offs, the constructions are implementable by $AC^0$ circuits which is the lowest complexity class in which secret sharing and reconstruction is possible. To the best of the knowledge of the authors, none of the similar existing schemes (evolving or dynamic) are $AC^0$ computable and this paper for the first time combines the idea of hypercubes and dynamic data structures with secret sharing for preserving long-term confidentiality of secret data.

  匹配依据：MPC: secret sharing

  </details>

- **BoMaNet: Boolean Masking of an Entire Neural Network**
  2020-06-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2006.09532)
  Anuj Dubey, Rosario Cammarota, Aydin Aysu

  <details><summary>摘要 / Abstract</summary>

  Recent work on stealing machine learning (ML) models from inference engines with physical side-channel attacks warrant an urgent need for effective side-channel defenses. This work proposes the first $\textit{fully-masked}$ neural network inference engine design. Masking uses secure multi-party computation to split the secrets into random shares and to decorrelate the statistical relation of secret-dependent computations to side-channels (e.g., the power draw). In this work, we construct secure hardware primitives to mask $\textit{all}$ the linear and non-linear operations in a neural network. We address the challenge of masking integer addition by converting each addition into a sequence of XOR and AND gates and by augmenting Trichina&#x27;s secure Boolean masking style. We improve the traditional Trichina&#x27;s AND gates by adding pipelining elements for better glitch-resistance and we architect the whole design to sustain a throughput of 1 masked addition per cycle. We implement the proposed secure inference engine on a Xilinx Spartan-6 (XC6SLX75) FPGA. The results show that masking incurs an overhead of 3.5\% in latency and 5.9$\times$ in area. Finally, we demonstrate the security of the masked design with 2M traces.

  匹配依据：MPC: secure multi party computation

  </details>

- **Equitable multiparty quantum communication without a trusted third party**
  2020-06-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2006.08091)
  Tanumoy Pramanik, Dong-Hwa Lee, Young-Wook Cho, Hyang-Tag Lim, Sang-Wook Han, Hojoong Jung, Sung Moon, Kwang Jo Lee, Yong-Su Kim

  <details><summary>摘要 / Abstract</summary>

  Multiparty quantum communication provides delightful applications including quantum cryptographic communication and quantum secret sharing. Measurement-Device-Independent (MDI) quantum communication based on the Greenberg-Horne-Zeilinger (GHZ) state measurement provides a practical way to implement multiparty quantum communication. With the standard spatially localized GHZ state measurement, however, information can be imbalanced among the communication parties that can cause significant problems in multiparty cryptographic communication. Here, we propose an equitable multiparty quantum communication where information balance among the communication parties is achieved without a trusted third party. Our scheme is based on the GHZ state measurement which is not spatially localized but implemented in a way that all the distant communication parties symmetrically participate. We also verify the feasibility of our scheme by presenting the proof-of-principle experimental demonstration of informationally balanced three-party quantum communication using weak coherent pulses.

  匹配依据：MPC: secret sharing

  </details>

- **A Logic Synthesis Toolbox for Reducing the Multiplicative Complexity in Logic Networks**
  2020-06-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/706)
  Eleonora Testa, Mathias Soeken, Heinz Riener, Luca Amaru, Giovanni De Micheli

  <details><summary>摘要 / Abstract</summary>

  Logic synthesis is a fundamental step in the realization of modern integrated circuits. It has traditionally been employed for the optimization of CMOS-based designs, as well as for emerging technologies and quantum computing. Recently, it found application in minimizing the number of AND gates in cryptography benchmarks represented as xor-and graphs (XAGs). The number of AND gates in an XAG, which is called the logic network’s multiplicative complexity, plays a critical role in various cryptography and security protocols such as fully homomorphic encryption (FHE) and secure multi-party computation (MPC). Further, the number of AND gates is also important to assess the degree of vulnerability of a Boolean function, and influences the cost of techniques to protect against side-channel attacks. However, so far a complete logic synthesis flow for reducing the multiplicative complexity in logic networks did not exist or relied heavily on manual manipulations. In this paper, we present a logic synthesis toolbox for cryptography and security applications. The proposed tool consists of powerful transformations, namely resubstitution, refactoring, and rewriting, specifically designed to minimize the multiplicative complexity of an XAG. Our flow is fully automatic and achieves significant results over both EPFL benchmarks and cryptography circuits. We improve the best-known results for cryptography up to 59%, resulting in a normalized geometric mean of 0.82.

  匹配依据：MPC: secure multi party computation

  </details>

- **Leakage of Dataset Properties in Multi-Party Machine Learning**
  2020-06-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2006.07267)
  Wanrong Zhang, Shruti Tople, Olga Ohrimenko

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party machine learning allows several parties to build a model on their pooled data to increase utility while not explicitly sharing data with each other. We show that such multi-party computation can cause leakage of global dataset properties between the parties even when parties obtain only black-box access to the final model. In particular, a ``curious&#x27;&#x27; party can infer the distribution of sensitive attributes in other parties&#x27; data with high accuracy. This raises concerns regarding the confidentiality of properties pertaining to the whole dataset as opposed to individual data records. We show that our attack can leak population-level properties in datasets of different types, including tabular, text, and graph data. To understand and measure the source of leakage, we consider several models of correlation between a sensitive attribute and the rest of the data. Using multiple machine learning models, we show that leakage occurs even if the sensitive attribute is not included in the training data and has a low correlation with other attributes or the target variable.

  匹配依据：MPC: multi party computation

  </details>

- **A device-independent protocol for XOR oblivious transfer**
  2020-06-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2006.06671)
  Srijita Kundu, Jamie Sikora, Ernest Y. -Z. Tan

  <details><summary>摘要 / Abstract</summary>

  Oblivious transfer is a cryptographic primitive where Alice has two bits and Bob wishes to learn some function of them. Ideally, Alice should not learn Bob&#x27;s desired function choice and Bob should not learn any more than what is logically implied by the function value. While decent quantum protocols for this task are known, many become completely insecure if an adversary were to control the quantum devices used in the implementation of the protocol. In this work we give a fully device-independent quantum protocol for XOR oblivious transfer.

  匹配依据：MPC: oblivious transfer

  </details>

- **Optimizing Smart Grid Aggregators and Measuring Degree of Privacy in a Distributed Trust Based Anonymous Aggregation System**
  2020-06-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2006.06070)
  Mohammad Saidur Rahman

  <details><summary>摘要 / Abstract</summary>

  A smart grid is an advanced method for supplying electricity to the consumers alleviating the limitations of the existing system. It causes frequent meter reading transmission from the end-user to the supplier. This frequent data transmission poses privacy risks. Several works have been proposed to solve this problem but cannot ensure privacy at the optimal level. This work is based on a distributed trust-based data aggregation system leveraging a secret sharing mechanism. In this work, we show that {\em three aggregators} are enough for ensuring consumer&#x27;s privacy in a distributed trust-based system. We leverage the idea of anonymity in our research and show that neither an active attacker nor a passive attacker can breach consumer&#x27;s privacy. We show proof of our concept mathematically and in a cryptographic game based mechanism. We name our new proposed system \emph{&quot;Distributed Trust Based Anonymous System (DTBAS)&quot;}.

  匹配依据：MPC: secret sharing

  </details>

- **MPC with Friends and Foes**
  2020-06-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/701)
  Bar Alon, Eran Omri, Anat Paskin-Cherniavsky

  <details><summary>摘要 / Abstract</summary>

  Classical definitions for secure multiparty computation assume the existence of a single adversarial entity controlling the set of corrupted parties. Intuitively, the definition requires that the view of the adversary, corrupting $t$ parties, in a real-world execution can be simulated by an adversary in an ideal model, where parties interact only via a trusted-party. No restrictions, however, are imposed on the view of honest parties in the protocol, thus, if honest parties obtain information about the private inputs of other honest parties -- it is not counted as a violation of privacy. This is arguably undesirable in many situations that fall into the MPC framework. Nevertheless, there are secure protocols (e.g., the 2-round multiparty protocol of Ishai et al.~[CRYPTO 2010] tolerating a single corrupted party) that instruct the honest parties to reveal their private inputs to all other honest parties (once the malicious party is somehow identified). In this paper, we put forth a new security notion, which we call \textit{FaF-security}, extending the classical notion. In essence, $(t,h^*)$-FaF-security requires the view of a subset of up to $h^*$ honest parties to also be simulatable in the ideal model (in addition to the view of the malicious adversary, corrupting up to $t$ parties). This property should still hold, even if the adversary leaks information to honest parties by sending them non-prescribed messages. We provide a thorough exploration of the new notion, investigating it in relation to a variety of existing security notions. We further investigate the feasibility of achieving FaF-security and show that every functionality can be computed with (computational) $(t,h^*)$-FaF full-security, if and only if $2t+ h^*&lt;m$. Interestingly, the lower-bound result actually shows that even fair FaF-security is impossible in general when $2t+ h^*\ge m$ (surprisingly, the view of the malicious attacker is not used as the trigger for the attack). We also investigate the optimal round complexity for $(t,h^*)$-FaF-secure protocols and give evidence that the leakage of private inputs of honest parties in the protocol of Ishai et al.~[CRYPTO 2010] is inherent. Finally, we investigate the feasibility of statistical/perfect FaF-security, employing the viewpoint used by Fitzi et al.~[ASIACRYPT 1999] for \textit{mixed-adversaries}.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Improved Threshold Signatures, Proactive Secret Sharing, and Input Certification from LSS Isomorphisms**
  2020-06-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/691)
  Diego Aranha, Anders Dalskov, Daniel Escudero, Claudio Orlandi

  <details><summary>摘要 / Abstract</summary>

  In this paper we present a series of applications steming from a formal treatment of linear secret-sharing isomorphisms, which are linear transformations between different secret-sharing schemes defined over vector spaces over a field $\mathbb{F}$ and allow for efficient multiparty conversion from one secret-sharing scheme to the other. This concept generalizes the folklore idea that moving from a secret-sharing scheme over $\mathbb{F}_{p}$ to a secret sharing ``in the exponent&#x27;&#x27; can be done non-interactively by multiplying the share unto a generator of e.g., an elliptic curve group. We generalize this idea and show that it can also be used to compute arbitrary bilinear maps and in particular pairings over elliptic curves. We include the following practical applications originating from our framework: First we show how to securely realize the Pointcheval-Sanders signature scheme (CT-RSA 2016) in MPC. Second we present a construction for dynamic proactive secret-sharing which outperforms the current state of the art from CCS 2019. Third we present a construction for MPC input certification using digital signatures that we show experimentally to outperform the previous best solution in this area.

  匹配依据：MPC: secret sharing

  </details>

- **Fast Vector Oblivious Linear Evaluation from Ring Learning with Errors**
  2020-06-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/685)
  Leo de Castro, Chiraag Juvekar, Vinod Vaikuntanathan

  <details><summary>摘要 / Abstract</summary>

  Oblivious linear evaluation (OLE) is a fundamental building block in multi-party computation protocols. In OLE, a sender holds a description of an affine function $f_{\alpha,\beta}(z)=\alpha z+\beta$, the receiver holds an input $x$, and gets $\alpha x+\beta$ (where all computations are done over some field, or more generally, a ring). Vector OLE (VOLE) is a generalization where the sender has many affine functions and the receiver learns the evaluation of all of these functions on a single point $x$. The state-of-the-art semi-honest VOLE protocols generally fall into two groups. The first group relies on standard assumptions to achieve security but lacks in concrete efficiency. These constructions are mostly based on additively homomorphic encryption (AHE) and are classified as ``folklore&quot;. The second group relies on less standard assumptions, usually properties of sparse, random linear codes, but they manage to achieve concrete practical efficiency. In this work, we present a conceptually simple VOLE protocol that derives its security from a standard assumption, namely Ring Learning with Errors (RLWE), while still achieving concrete efficiency comparable to the fastest VOLE protocols from non-standard coding assumptions. Furthermore, our protocol admits a natural extension to batch OLE (BOLE), which is yet another variant of OLE that computes many OLEs in parallel.

  匹配依据：MPC: multi party computation

  </details>

- **BETA: Biometric Enabled Threshold Authentication**
  2020-06-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/679)
  Shashank Agrawal, Saikrishna Badrinarayanan, Payman Mohassel, Pratyay Mukherjee, Sikhar Patranabis

  <details><summary>摘要 / Abstract</summary>

  In the past decades, user authentication has been dominated by server-side password-based solutions that rely on &quot;what users know&quot;. This approach is susceptible to breaches and phishing attacks, and poses usability challenges. As a result, the industry is gradually moving to biometric-based client-side solutions that do not store any secret information on servers. This shift necessitates the safe storage of biometric templates and private keys, which are used to generate tokens, on user devices. We propose a new generic framework called Biometric Enabled Threshold Authentication (BETA) to protect sensitive client-side information like biometric templates and cryptographic keys. Towards this, we formally introduce the notion of Fuzzy Threshold Tokenizer (FTS) where an initiator can use a &quot;close&quot; biometric measurement to generate an authentication token if at least $t$ (the threshold) devices participate. We require that the devices only talk to the initiator, and not to each other, to capture the way user devices are connected in the real world. We use the universal composability (UC) framework to model the security properties of FTS, including the unforgeability of tokens and the privacy of the biometric values (template and measurement), under a malicious adversary. We construct three protocols that meet our definition. Our first two protocols are general feasibility results that work for any distance function, any threshold $t$ and tolerate the maximal (i.e. $t-1$) amount of corruption. They are based on any two round UC-secure multi-party computation protocol in the standard model (with a CRS) and threshold fully homomorphic encryption, respectively. We show how to effectively use these primitives to build protocols in a constrained communication model with just four rounds of communication. For the third protocol, we consider inner-product based distance metrics (cosine similarity, Euclidean distance, etc.) specifically, motivated by the recent interest in its use for face recognition. We use Paillier encryption, efficient NIZKs for specific languages, and a simple garbled circuit to build an efficient protocol for the common case of $n=3$ devices with one compromised.

  匹配依据：MPC: garbled circuit, secure multi party computation

  </details>

- **AutoPrivacy: Automated Layer-wise Parameter Selection for Secure Neural Network Inference**
  2020-06-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2006.04219)
  Qian Lou, Song Bian, Lei Jiang

  <details><summary>摘要 / Abstract</summary>

  Hybrid Privacy-Preserving Neural Network (HPPNN) implementing linear layers by Homomorphic Encryption (HE) and nonlinear layers by Garbled Circuit (GC) is one of the most promising secure solutions to emerging Machine Learning as a Service (MLaaS). Unfortunately, a HPPNN suffers from long inference latency, e.g., $\sim100$ seconds per image, which makes MLaaS unsatisfactory. Because HE-based linear layers of a HPPNN cost $93\%$ inference latency, it is critical to select a set of HE parameters to minimize computational overhead of linear layers. Prior HPPNNs over-pessimistically select huge HE parameters to maintain large noise budgets, since they use the same set of HE parameters for an entire network and ignore the error tolerance capability of a network. In this paper, for fast and accurate secure neural network inference, we propose an automated layer-wise parameter selector, AutoPrivacy, that leverages deep reinforcement learning to automatically determine a set of HE parameters for each linear layer in a HPPNN. The learning-based HE parameter selection policy outperforms conventional rule-based HE parameter selection policy. Compared to prior HPPNNs, AutoPrivacy-optimized HPPNNs reduce inference latency by $53\%\sim70\%$ with negligible loss of accuracy.

  匹配依据：MPC: garbled circuit

  </details>

- **Differentially private partition selection**
  2020-06-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2006.03684)
  Damien Desfontaines, James Voss, Bryant Gipson, Chinmoy Mandayam

  <details><summary>摘要 / Abstract</summary>

  Many data analysis operations can be expressed as a GROUP BY query on an unbounded set of partitions, followed by a per-partition aggregation. To make such a query differentially private, adding noise to each aggregation is not enough: we also need to make sure that the set of partitions released is also differentially private. This problem is not new, and it was recently formally introduced as differentially private set union. In this work, we continue this area of study, and focus on the common setting where each user is associated with a single partition. In this setting, we propose a simple, optimal differentially private mechanism that maximizes the number of released partitions. We discuss implementation considerations, as well as the possible extension of this approach to the setting where each user contributes to a fixed, small number of partitions.

  匹配依据：MPC: private set union

  </details>

- **Two-Round Oblivious Linear Evaluation from Learning with Errors**
  2020-06-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/635)
  Pedro Branco, Nico Döttling, Paulo Mateus

  <details><summary>摘要 / Abstract</summary>

  Oblivious Linear Evaluation (OLE) is the arithmetic analogue of the well-know oblivious transfer primitive. It allows a sender, holding an affine function $f(x)=a+bx$ over a finite field or ring, to let a receiver learn $f(w)$ for a $w$ of the receiver&#x27;s choice. In terms of security, the sender remains oblivious of the receiver&#x27;s input $w$, whereas the receiver learns nothing beyond $f(w)$ about $f$. In recent years, OLE has emerged as an essential building block to construct efficient, reusable and maliciously-secure two-party computation. In this work, we present efficient two-round protocols for OLE over large fields based on the Learning with Errors (LWE) assumption, providing a full arithmetic generalization of the oblivious transfer protocol of Peikert, Vaikuntanathan and Waters (CRYPTO 2008). At the technical core of our work is a novel extraction technique which allows to determine if a non-trivial multiple of some vector is close to a $q$-ary lattice.

  匹配依据：MPC: oblivious transfer, secure two party computation

  </details>

- **RSA for poor men: a cryptosystem based on probable primes to base 2 numbers**
  2020-06-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/624)
  Marek Wójtowicz

  <details><summary>摘要 / Abstract</summary>

  We show it is possible to build an RSA-type cryptosystem by utilizing \textit{probable primes to base 2} numbers. Our modulus $N$ is the product $n\cdot m$ of such numbers (so here both prime and some composite, e.g. Carmichael or Fermat, numbers are acceptable) instead of prime numbers. Moreover, we require for $n$ and $m$ to be co-prime only, and so we don&#x27;t have to worry about whether any of the numbers $n, m$ is composite or not. The encryption and decryption processes are similar as those in the RSA. Hence, in this cryptosystem we may apply the above kind of numbers of arbitrary length being still sure that the system works well. The price for that is not so high: the size of a message $M$ (as a number) permitted by the new system must be smaller than log (in base 2) of $n\cdot m$. The proposed cryptosystem can be applied in the case the numbers $n,m$ are &#x27;sufficiently large&#x27; for a user, or as a completion of the classical RSA if $m,n$ are probable primes but possibly not prime, or in a &#x27;secret sharing&#x27;-type cryptosystem. The numbers $n,m$ can be also taken from a narrower class of probable primes to base 2 numbers, e.g., Euler, or strong, or Baillie-PSW.

  匹配依据：MPC: secret sharing

  </details>

- **Multi-Party Computation Mechanism for Anonymous Equity Block Trading: A Secure Implementation of Turquoise Plato Uncross**
  2020-06-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/662)
  John Cartlidge, Nigel P. Smart, Younes Talibi Alaoui

  <details><summary>摘要 / Abstract</summary>

  Dark markets for share trading provide an important function in the financial services industry, however the operators of such markets are not operating in the dark; leaving the possibility open for the market operator to gain a market advantage. Multi-Party Computation (MPC) is a method to remove the need for such trusted third parties. In this paper we show how MPC can be used to implement such a dark market. Importantly we base our solution on the throughputs and algorithms needed in real markets. In particular we base our implementation on the Turquoise Plato market used by the London Stock Exchange.

  匹配依据：MPC: multi party computation

  </details>

- **Mixed-Technique Multi-Party Computations Composed of Two-Party Computations**
  2020-06-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/636)
  Erik-Oliver Blass, Florian Kerschbaum

  <details><summary>摘要 / Abstract</summary>

  Protocols for secure multi-party computation are commonly composed of different sub-protocols, combining techniques such as homomorphic encryption, secret or Boolean sharing, and garbled circuits. In this paper, we design a new class of multi-party computation protocols which themselves are composed out of two-party protocols. We integrate both types of compositions, compositions of fully homomorphic encryption and garbled circuits with compositions of multi-party protocols from two-party protocols. As a result, we can construct communication-efficient protocols for special problems. Furthermore, we show how to efficiently ensure the security of composed protocols against malicious adversaries by proving in zero-knowledge that conversions between individual techniques are correct. To demonstrate the usefulness of this approach, we give an example scheme for private set analytics, i.e., private set disjointness. This scheme enjoys lower communication complexity than a solution based on generic multi-party computation and lower computation cost than fully homomorphic encryption. So, our design is more suitable for deployments in wide-area networks, such as the Internet, with many participants or problems with circuits of moderate or high multiplicative depth.

  匹配依据：MPC: garbled circuits, multi party computation, secure multi party computation

  </details>

- **Cryptanalysis of \`\`FS-PEKS: Lattice-based Forward Secure Public-key Encryption with Keyword Search for Cloud-assisted Industrial Internet of Things''**
  2020-06-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/651)
  Zi-Yuan Liu, Yi-Fan Tseng, Raylin Tso

  <details><summary>摘要 / Abstract</summary>

  In this note, we review lattice-based public-key encryption with the keyword search against inside keyword guess attacks (IKGAs) proposed by Zhang \textit{et al}. in IEEE Transactions on Dependable and Secure Computing in 2021. We demonstrate that this scheme is insecure for IKGAs, although Zhang \textit{et al.} demonstrated a secure proof.

  匹配依据：MPC: secure computing

  </details>

- **A simple generic construction to build oblivious transfer protocols from homomorphic encryption schemes**
  2020-06-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/647)
  Saeid Esmaeilzade, Ziba Eslami, Nasrollah Pakniat

  <details><summary>摘要 / Abstract</summary>

  Oblivious transfer (OT) is a fundamental problem in cryptography where it is required that a sender transfers one of potentially many pieces of information to a receiver and at the same time remains oblivious as to which piece has been transferred. After its introduction back in 1981 by Rabin, some more useful variations of OT appeared in the literature such as $OT^1_2$, $OT^1_n$, and $OT^k_n$. In 2015, a very simple and efficient OT protocol was proposed by Chou and Orlandi. Later, Hauck and Loss proposed an improved protocol and proved it to be fully UC-secure under the CDH assumption. Our goal in this paper is to extend the results of Hauck and Loss and propose a simple generic construction to build $OT^1_2$ and in general $OT^1_n$. The machinery we employ is homomorphic encryption. We instantiate our construction with some well known homomorphic encryption schemes such as RSA, Paillier, and NTRU to obtain concrete OT protocols. We further provide the details of the proof of the UC-security of our generic construction.

  匹配依据：MPC: oblivious transfer

  </details>

- **Generation of perfect W-state and demonstration of its application to quantum information splitting**
  2020-06-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2006.01742)
  Manoranjan Swain, Vipin Devrari, Amit Rai, Bikash K. Behera, Prasanta K. Panigrahi

  <details><summary>摘要 / Abstract</summary>

  We report the first experimental realization of perfect W-state in a superconducting qubit based system. In contrast to maximally entangled state, the perfect W state is different in weights and phases of the terms contained in the maximally entangled W-state. The prefect W state finds important applications in quantum information processing tasks such as perfect teleportation, superdense coding, secret sharing etc. The efficiency of generation is quantified by fidelity which is calculated by performing full quantum state tomography. To verify the presence of genuine nonlocality in the generated state, we experimentally perform Mermin&#x27;s inequality tests. Further, we have also demonstrated splitting and sharing of quantum information using the experimentally generated state.

  匹配依据：MPC: secret sharing

  </details>

- **DatashareNetwork: A Decentralized Privacy-Preserving Search Engine for Investigative Journalists**
  2020-05-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.14645)
  Kasra EdalatNejad, Wouter Lueks, Julien Pierre Martin, Soline Ledésert, Anne L'Hôte, Bruno Thomas, Laurent Girod, Carmela Troncoso

  <details><summary>摘要 / Abstract</summary>

  Investigative journalists collect large numbers of digital documents during their investigations. These documents can greatly benefit other journalists&#x27; work. However, many of these documents contain sensitive information. Hence, possessing such documents can endanger reporters, their stories, and their sources. Consequently, many documents are used only for single, local, investigations. We present DatashareNetwork, a decentralized and privacy-preserving search system that enables journalists worldwide to find documents via a dedicated network of peers. DatashareNetwork combines well-known anonymous authentication mechanisms and anonymous communication primitives, a novel asynchronous messaging system, and a novel multi-set private set intersection protocol (MS-PSI) into a *decentralized peer-to-peer private document search engine*. We prove that DatashareNetwork is secure; and show using a prototype implementation that it scales to thousands of users and millions of documents.

  匹配依据：MPC: private set intersection

  </details>

- **PSI-Stats: Private Set Intersection Protocols Supporting Secure Statistical Functions**
  2020-05-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/623)
  Jason H. M. Ying, Shuwei Cao, Geong Sen Poh, Jia Xu, Hoon Wei Lim

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection (PSI) enables two parties, each holding a private set to securely compute their intersection without revealing other information. This paper considers settings of secure statistical computations over PSI, where both parties hold sets containing identifiers with one of the parties having an additional positive integer value associated with each of the identifiers in her set. The main objective is to securely compute some desired statistics of the associated values for which its corresponding identifiers occur in the intersection of the two sets. This is achieved without revealing the identifiers of the set intersection. In this paper, we present protocols which enable the secure computations of statistical functions over PSI, which we collectively termed PSI-Stats. Implementations of our constructions are also carried out based on simulated datasets as well as on actual datasets in the business use cases that we defined, in order to demonstrate practicality of our solution. PSI-Stats incurs 5x less monetary cost compared to the current state-of-the-art circuit-based PSI approach due to Pinkas et al. (EUROCRYPT&#x27;19). Our solution is more tailored towards business applications where monetary cost is the primary consideration.

  匹配依据：MPC: private set intersection

  </details>

- **Private Identity Agreement for Private Set Functionalities**
  2020-05-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/620)
  Ben Kreuter, Sarvar Patel, Ben Terner

  <details><summary>摘要 / Abstract</summary>

  Private set intersection and related functionalities are among the most prominent real-world applications of secure multiparty computation. While such protocols have attracted significant attention from the research community, other functionalities are often required to support a PSI application in practice. For example, in order for two parties to run a PSI over the unique users contained in their databases, they might first invoke on a support functionality to agree on the primary keys to represent their users. This paper studies a secure approach to agreeing on primary keys. We introduce and realize a functionality that computes a common set of identifiers based on incomplete information held by two parties, which we refer to as private identity agreement. We explain the subtleties in designing such a functionality that arise from privacy requirements when intending to compose securely with PSI protocols. We also argue that the cost of invoking this functionality can be amortized over a large number of PSI sessions, and that for applications that require many repeated PSI executions, this represents an improvement over a PSI protocol that directly uses incomplete or fuzzy matches.

  匹配依据：MPC: private set intersection, secure multiparty computation

  </details>

- **How to Base Security on the Perfect/Statistical Binding Property of Quantum Bit Commitment?**
  2020-05-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/621)
  Junbin Fang, Dominique Unruh, Jun Yan, Dehua Zhou

  <details><summary>摘要 / Abstract</summary>

  The concept of quantum bit commitment was introduced in the early 1980s for the purpose of basing bit commitments solely on principles of quantum theory. Unfortunately, such unconditional quantum bit commitments still turn out to be impossible. As a compromise like in classical cryptography, Dumais et al. [DMS00] introduce the conditional quantum bit commitments that additionally rely on complexity assumptions. However, in contrast to classical bit commitments which are widely used in classical cryptography, up until now there is relatively little work towards studying the application of quantum bit commitments in quantum cryptography. This may be partly due to the well-known weakness of the general quantum binding that comes from the possible superposition attack of the sender of quantum commitments, making it unclear whether quantum commitments could be useful in quantum cryptography. In this work, following Yan et al. [YWLQ15] we continue studying using (canonical non-interactive) perfectly/statistically-binding quantum bit commitments as the drop-in replacement of classical bit commitments in some well-known constructions. Specifically, we show that the (quantum) security can still be established for zero-knowledge proof, oblivious transfer, and proof-of-knowledge. In spite of this, we stress that the corresponding security analyses are by no means trivial extensions of their classical analyses; new techniques are needed to handle possible superposition attacks by the cheating sender of quantum bit commitments. Since (canonical non-interactive) statistically-binding quantum bit commitments can be constructed from quantum-secure one-way functions, we hope using them (as opposed to classical commitments) in cryptographic constructions can reduce the round complexity and weaken the complexity assumption simultaneously.

  匹配依据：MPC: oblivious transfer

  </details>

- **Cross Hashing: Anonymizing encounters in Decentralised Contact Tracing Protocols**
  2020-05-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.12884)
  Junade Ali, Vladimir Dyo

  <details><summary>摘要 / Abstract</summary>

  During the COVID-19 (SARS-CoV-2) epidemic, Contact Tracing emerged as an essential tool for managing the epidemic. App-based solutions have emerged for Contact Tracing, including a protocol designed by Apple and Google (influenced by an open-source protocol known as DP3T). This protocol contains two well-documented de-anonymisation attacks. Firstly that when someone is marked as having tested positive and their keys are made public, they can be tracked over a large geographic area for 24 hours at a time. Secondly, whilst the app requires a minimum exposure duration to register a contact, there is no cryptographic guarantee for this property. This means an adversary can scan Bluetooth networks and retrospectively find who is infected. We propose a novel &quot;cross hashing&quot; approach to cryptographically guarantee minimum exposure durations. We further mitigate the 24-hour data exposure of infected individuals and reduce computational time for identifying if a user has been exposed using $k$-Anonymous buckets of hashes and Private Set Intersection. We empirically demonstrate that this modified protocol can offer like-for-like efficacy to the existing protocol.

  匹配依据：MPC: private set intersection

  </details>

- **Broadcast Secret-Sharing, Bounds and Applications**
  2020-05-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/618)
  Ivan Damgård, Kasper Green Larsen, Sophia Yakoubov

  <details><summary>摘要 / Abstract</summary>

  Consider a sender S and a group and of n recipients. S holds a secret message m of length l bits and the goal is to allow S to create a secret sharing of m with privacy threshold t among the recipients, by broadcasting a single message c to the recipients. Our goal is to do this with information theoretic security in a model with a simple form of correlated randomness. Namely, for each subset A of recipients of size q, S may share a secret random bit string with all recipients in A. We call this Broadcast Secret-Sharing (BSS) with parameters l, n, t and q. Our main question is: how large must c be, as a function of the parameters? We show that l(n-t)/q is a lower bound, and we show an upper bound of l((n(t+1))/(q+t)-t), matching the lower bound whenever t = 0, or when q = 1 or n-t. When q = n-t, the size of c is exactly l which is clearly minimal. The protocol demonstrating the upper bound in this case requires S to share a key with every subset of size n-t. We show that this overhead cannot be avoided when c has minimal size. We also show that if access is additionally given to an idealized PRG, the lower bound on ciphertext size becomes (k(n-t)/q)+l-negl(k) (where k is the length of the input to the PRG). The upper bound becomes k((n(t+1))/(q+t)-t)+l. BSS can be applied directly to secret-key threshold encryption. We can also consider a setting where the correlated randomness is generated using computationally secure and non-interactive key exchange, where we assume that each recipient has an (independently generated) public key for this purpose. In this model, any protocol for non-interactive secret sharing becomes an ad hoc threshold encryption (ATE) scheme, which is a threshold encryption scheme with no trusted setup beyond a PKI. Our upper bounds imply new ATE schemes, and our lower bound becomes a lower bound on the ciphertext size in any ATE scheme that uses a key exchange functionality and no other cryptographic primitives.

  匹配依据：MPC: secret sharing

  </details>

- **Two-Phase Multi-Party Computation Enabled Privacy-Preserving Federated Learning**
  2020-05-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.11901)
  Renuga Kanagavelu, Zengxiang Li, Juniarto Samsudin, Yechao Yang, Feng Yang, Rick Siow Mong Goh, Mervyn Cheah, Praewpiraya Wiwatphonthana, Khajonpong Akkarajitsakul, Shangguang Wangz

  <details><summary>摘要 / Abstract</summary>

  Countries across the globe have been pushing strict regulations on the protection of personal or private data collected. The traditional centralized machine learning method, where data is collected from end-users or IoT devices, so that it can discover insights behind real-world data, may not be feasible for many data-driven industry applications in light of such regulations. A new machine learning method, coined by Google as Federated Learning (FL) enables multiple participants to train a machine learning model collectively without directly exchanging data. However, recent studies have shown that there is still a possibility to exploit the shared models to extract personal or confidential data. In this paper, we propose to adopt Multi Party Computation (MPC) to achieve privacy-preserving model aggregation for FL. The MPC-enabled model aggregation in a peer-to-peer manner incurs high communication overhead with low scalability. To address this problem, the authors proposed to develop a two-phase mechanism by 1) electing a small committee and 2) providing MPC-enabled model aggregation service to a larger number of participants through the committee. The MPC enabled FL framework has been integrated in an IoT platform for smart manufacturing. It enables a set of companies to train high quality models collectively by leveraging their complementary data-sets on their own premises, without compromising privacy, model accuracy vis-a-vis traditional machine learning methods and execution efficiency in terms of communication cost and execution time.

  匹配依据：MPC: multi party computation

  </details>

- **A First Step Towards Content Protecting Plagiarism Detection**
  2020-05-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.11504)
  Cornelius Ihle, Moritz Schubotz, Norman Meuschke, Bela Gipp

  <details><summary>摘要 / Abstract</summary>

  Plagiarism detection systems are essential tools for safeguarding academic and educational integrity. However, today&#x27;s systems require disclosing the full content of the input documents and the document collection to which the input documents are compared. Moreover, the systems are centralized and under the control of individual, typically commercial providers. This situation raises procedural and legal concerns regarding the confidentiality of sensitive data, which can limit or prohibit the use of plagiarism detection services. To eliminate these weaknesses of current systems, we seek to devise a plagiarism detection approach that does not require a centralized provider nor exposing any content as cleartext. This paper presents the initial results of our research. Specifically, we employ Private Set Intersection to devise a content-protecting variant of the citation-based similarity measure Bibliographic Coupling implemented in our plagiarism detection system HyPlag. Our evaluation shows that the content-protecting method achieves the same detection effectiveness as the original method while making common attacks to disclose the protected content practically infeasible. Our future work will extend this successful proof-of-concept by devising plagiarism detection methods that can analyze the entire content of documents without disclosing it as cleartext.

  匹配依据：MPC: private set intersection

  </details>

- **SWIFT: Super-fast and Robust Privacy-Preserving Machine Learning**
  2020-05-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.10296) · [IACR ePrint](https://eprint.iacr.org/2020/592)
  Nishat Koti, Mahak Pancholi, Arpita Patra, Ajith Suresh

  <details><summary>摘要 / Abstract</summary>

  Performing machine learning (ML) computation on private data while maintaining data privacy, aka Privacy-preserving Machine Learning~(PPML), is an emergent field of research. Recently, PPML has seen a visible shift towards the adoption of the Secure Outsourced Computation~(SOC) paradigm due to the heavy computation that it entails. In the SOC paradigm, computation is outsourced to a set of powerful and specially equipped servers that provide service on a pay-per-use basis. In this work, we propose SWIFT, a robust PPML framework for a range of ML algorithms in SOC setting, that guarantees output delivery to the users irrespective of any adversarial behaviour. Robustness, a highly desirable feature, evokes user participation without the fear of denial of service. At the heart of our framework lies a highly-efficient, maliciously-secure, three-party computation (3PC) over rings that provides guaranteed output delivery (GOD) in the honest-majority setting. To the best of our knowledge, SWIFT is the first robust and efficient PPML framework in the 3PC setting. SWIFT is as fast as (and is strictly better in some cases than) the best-known 3PC framework BLAZE (Patra et al. NDSS&#x27;20), which only achieves fairness. We extend our 3PC framework for four parties (4PC). In this regime, SWIFT is as fast as the best known fair 4PC framework Trident (Chaudhari et al. NDSS&#x27;20) and twice faster than the best-known robust 4PC framework FLASH (Byali et al. PETS&#x27;20). We demonstrate our framework&#x27;s practical relevance by benchmarking popular ML algorithms such as Logistic Regression and deep Neural Networks such as VGG16 and LeNet, both over a 64-bit ring in a WAN setting. For deep NN, our results testify to our claims that we provide improved security guarantee while incurring no additional overhead for 3PC and obtaining 2x improvement for 4PC.

  匹配依据：MPC: secure three party computation

  </details>

- **Private Matching for Compute**
  2020-05-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/599)
  Prasad Buddhavarapu, Andrew Knox, Payman Mohassel, Shubho Sengupta, Erik Taubeneck, Vlad Vlaskin

  <details><summary>摘要 / Abstract</summary>

  We revisit the problem of two-party private set intersection for aggregate computation which we refer to as private matching for compute. In this problem, two parties want to perform various downstream computation on the intersection of their two datasets according to a previously agreed-upon identifier. We observe that prior solutions to this problem have important limitations. For example, any change or update to the records in either party&#x27;s dataset triggers a rerun of the private matching component; and it is not clear how to support a streaming arrival of one party&#x27;s set in small batches without revealing the match rate for each individual batch. We introduce two new formulations of the private matching for compute problem meeting these requirements, called private-ID and streaming private secret shared set intersection, and design new DDH-based constructions for both. Our implementation shows that when taking advantage of the inherent parallelizability of these solutions, we can execute the matching for datasets of size upto 100 million records within an hour.

  匹配依据：MPC: private set intersection

  </details>

- **A Note on Cryptographic Algorithms for Private Data Analysis in Contact Tracing Applications**
  2020-05-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.10634)
  Rajan M A, Manish Shukla, Sachin Lodha

  <details><summary>摘要 / Abstract</summary>

  Contact tracing is an important measure to counter the COVID-19 pandemic. In the early phase, many countries employed manual contact tracing to contain the rate of disease spread, however it has many issues. The manual approach is cumbersome, time consuming and also requires active participation of a large number of people to realize it. In order to overcome these drawbacks, digital contact tracing has been proposed that typically involves deploying a contact tracing application on people&#x27;s mobile devices which can track their movements and close social interactions. While studies suggest that digital contact tracing is more effective than manual contact tracing, it has been observed that higher adoption rates of the contact tracing app may result in a better controlled epidemic. This also increases the confidence in the accuracy of the collected data and the subsequent analytics. One key reason for low adoption rate of contact tracing applications is the concern about individual privacy. In fact, several studies report that contact tracing applications deployed in multiple countries are not privacy friendly and have potential to be used for mass surveillance by the concerned governments. Hence, privacy respecting contact tracing application is the need of the hour that can lead to highly effective, efficient contact tracing. As part of this study, we focus on various cryptographic techniques that can help in addressing the Private Set Intersection problem which lies at the heart of privacy respecting contact tracing. We analyze the computation and communication complexities of these techniques under the typical client-server architecture utilized by contact tracing applications. Further we evaluate those computation and communication complexity expressions for India scenario and thus identify cryptographic techniques that can be more suitably deployed there.

  匹配依据：MPC: private set intersection

  </details>

- **Private Edge Computing for Linear Inference Based on Secret Sharing**
  2020-05-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.08593)
  Reent Schlegel, Siddhartha Kumar, Eirik Rosnes, Alexandre Graell i Amat

  <details><summary>摘要 / Abstract</summary>

  We consider an edge computing scenario where users want to perform a linear computation on local, private data and a network-wide, public matrix. Users offload computations to edge servers located at the edge of the network, but do not want the servers, or any other party with access to the wireless links, to gain any information about their data. We provide a scheme that guarantees information-theoretic user data privacy against an eavesdropper with access to a number of edge servers or their corresponding communication links. The novelty of the proposed scheme lies in the utilization of secret sharing and partial replication to provide privacy, mitigate the effect of straggling servers, and to allow for joint beamforming opportunities in the download phase, to minimize the overall latency, consisting of upload, computation, and download latencies.

  匹配依据：MPC: secret sharing

  </details>

- **Large-Scale Secure XGB for Vertical Federated Learning**
  2020-05-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.08479)
  Wenjing Fang, Derun Zhao, Jin Tan, Chaochao Chen, Chaofan Yu, Li Wang, Lei Wang, Jun Zhou, Benyu Zhang

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving machine learning has drawn increasingly attention recently, especially with kinds of privacy regulations come into force. Under such situation, Federated Learning (FL) appears to facilitate privacy-preserving joint modeling among multiple parties. Although many federated algorithms have been extensively studied, there is still a lack of secure and practical gradient tree boosting models (e.g., XGB) in literature. In this paper, we aim to build large-scale secure XGB under vertically federated learning setting. We guarantee data privacy from three aspects. Specifically, (i) we employ secure multi-party computation techniques to avoid leaking intermediate information during training, (ii) we store the output model in a distributed manner in order to minimize information release, and (iii) we provide a novel algorithm for secure XGB predict with the distributed model. Furthermore, by proposing secure permutation protocols, we can improve the training efficiency and make the framework scale to large dataset. We conduct extensive experiments on both public datasets and real-world datasets, and the results demonstrate that our proposed XGB models provide not only competitive accuracy but also practical performance.

  匹配依据：MPC: secure multi party computation

  </details>

- **Secure large-scale genome-wide association studies using homomorphic encryption**
  2020-05-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/563)
  Marcelo Blatt, Alexander Gusev, Yuriy Polyakov, Shafi Goldwasser

  <details><summary>摘要 / Abstract</summary>

  Genome-Wide Association Studies (GWAS) seek to identify genetic variants associated with a trait, and have been a powerful approach for understanding complex diseases. A critical challenge for GWAS has been the dependence on individual-level data that typically have strict privacy requirements, creating an urgent need for methods that preserve the individual-level privacy of participants. Here, we present a privacy-preserving framework based on several advances in homomorphic encryption and demonstrate that it can perform an accurate GWAS analysis for a real dataset of more than 25,000 individuals, keeping all individual data encrypted and requiring no user interactions. Our extrapolations show that it can evaluate GWAS of 100,000 individuals and 500,000 SNPs in 5.6 hours on a single server node (or in 11 minutes on 31 server nodes running in parallel). Our performance results are more than one order of magnitude faster than prior state-of-the-art results using secure multi-party computation, which requires continuous user interactions, with the accuracy of both solutions being similar. Our homomorphic encryption advances can also be applied to other domains where large-scale statistical analyses over encrypted data are needed.

  匹配依据：MPC: secure multi party computation

  </details>

- **SNI-in-the-head: Protecting MPC-in-the-head Protocols against Side-channel Analysis**
  2020-05-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/544)
  Okan Seker, Sebastian Berndt, Luca Wilke, Thomas Eisenbarth

  <details><summary>摘要 / Abstract</summary>

  MPC-in-the-head based protocols have recently gained much popularity and are at the brink of seeing widespread usage. With such widespread use come the spectres of implementation issues and implementation attacks such as side-channel attacks. We show that implementations of protocols implementing the MPC-in-the-head paradigm are vulnerable to side-channel attacks. As a case study, we choose the ZKBoo-protocol of Giacomelli, Madsen, and Orlandi (USENIX 2016) and show that even a single leaked value is sufficient to break the security of the protocol. To show that this attack is not just a theoretical vulnerability, we apply differential power analysis to show the vulnerabilities via a simulation. In order to remedy this situation, we extend and generalize the ZKBooprotocol by making use of the notion of strong non-interference of Barthe et al. (CCS 2016). To apply this notion to ZKBoo, we construct novel versions of strongly non-interfering gadgets that balance the randomness across the different branches evenly. Finally, we show that each circuit can be decomposed into branches using only these balanced strongly noninterfering gadgets. This allows us to construct a version of ZKBoo, called (n + 1)-ZKBoo which is secure against side-channel attacks with limited overhead in both signature-size and running time. Furthermore, (n + 1)-ZKBoo is scalable to the desired security against adversarial probes. We experimentally confirm that the attacks successful against ZKBoo no longer work on (n + 1)-ZKBoo. Moreover, we present an extensive performance analysis and quantify the overhead of our scheme using a practical implementation.

  匹配依据：MPC: mpc (context)

  </details>

- **Practical MPC+FHE with Applications in Secure Multi-PartyNeural Network Evaluation**
  2020-05-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/550)
  Ruiyu Zhu, Changchang Ding, Yan Huang

  <details><summary>摘要 / Abstract</summary>

  The theoretical idea of using FHE to realize MPC has been therefor over a decade. Existing threshold (and multi-key) FHE schemes were constructed by modifying and analyzing a traditional single-keyFHE in a case-by-case manner, thus technically highly-demanding.This work explores a new approach to build threshold FHE (therebyMPC schemes) through tailoring generic MPC protocols to the base FHE scheme while requiring no effort in FHE redesign. We applied our approach to two representative Ring-LWE-based FHE schemes: CKKS and GHS, producing GMPFHE-CKKS and GMPFHE-GHS. We developed MPC protocols based on GMPFHE-CKKS and GMPFHE-GHS which are secure against any number of passive but colluding adversaries. The online cost of our MPC protocol is $O(|C|)$, as opposed to $O(|C|·n^2)$ for existing MPC protocols, and our offline cost is independent of $|C|$. We experimentally show that the GMPFHE-CKKS-based MPC protocol offers unparalleled amortized performance on multi-party neural network evaluation.

  匹配依据：MPC: mpc (context)

  </details>

- **Private Two-Terminal Hypothesis Testing**
  2020-05-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.05961)
  Varun Narayanan, Manoj Mishra, Vinod M. Prabhakaran

  <details><summary>摘要 / Abstract</summary>

  We study private two-terminal hypothesis testing with simple hypotheses where the privacy goal is to ensure that participating in the testing protocol reveals little additional information about the other user&#x27;s observation when a user is told what the correct hypothesis is. We show that, in general, meaningful correctness and privacy cannot be achieved if the users do not have access to correlated (but, not common) randomness. We characterize the optimal correctness and privacy error exponents when the users have access to non-trivial correlated randomness (those that permit secure multiparty computation).

  匹配依据：MPC: secure multiparty computation

  </details>

- **Secure Computation to Hide Functions of Inputs**
  2020-05-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.05111)
  Gowtham R. Kurri, Vinod M. Prabhakaran

  <details><summary>摘要 / Abstract</summary>

  We consider a two-user secure computation problem in which Alice and Bob communicate interactively in order to compute some deterministic functions of the inputs. The privacy requirement is that each user should not learn any additional information about a function of the inputs other than what can be inferred from its own input and output. For the distribution-free setting, i.e., when the protocol must be correct and private for any joint input distribution, we completely characterize the set of all securely computable functions. When privacy is required only against Bob who computes a function based on a single transmission from Alice, we show that asymptotically secure computability is equivalent to perfectly secure computability. Separately, we consider an eavesdropper who has access to all the communication and should not learn any information about some function of the inputs (possibly different from the functions to be computed by the users) and show that interaction may be necessary for secure computation.

  匹配依据：MPC: secure computation

  </details>

- **Minimal Linear Codes From Weakly Regular Plateaued Balanced Functions**
  2020-05-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.04781)
  Ahmet Sınak

  <details><summary>摘要 / Abstract</summary>

  Linear codes have diverse applications in secret sharing schemes, secure two-party computation, association schemes, strongly regular graphs, authentication codes and communication. There are a large number of linear codes with few weights in the literature, but a little of them are minimal. In this paper, we are using for the first time weakly regular plateaued balanced functions over the finite fields of odd characteristic in the second generic construction method of linear codes. The main results of this paper are stated below. We first construct several three-weight and four-weight linear codes with flexible parameters from weakly regular plateaued balanced functions. It is worth noting that the (almost) optimal codes may be obtained from these functions. We next observe that all codes obtained in this paper are minimal, thereby they can be directly employed to construct secret sharing schemes with high democracy. Finally, the democratic secret sharing schemes are obtained from the dual codes of our minimal codes.

  匹配依据：MPC: secret sharing, secure two party computation

  </details>

- **Cloud-based Federated Boosting for Mobile Crowdsensing**
  2020-05-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.05304)
  Zhuzhu Wang, Yilong Yang, Yang Liu, Ximeng Liu, Brij B. Gupta, Jianfeng Ma

  <details><summary>摘要 / Abstract</summary>

  The application of federated extreme gradient boosting to mobile crowdsensing apps brings several benefits, in particular high performance on efficiency and classification. However, it also brings a new challenge for data and model privacy protection. Besides it being vulnerable to Generative Adversarial Network (GAN) based user data reconstruction attack, there is not the existing architecture that considers how to preserve model privacy. In this paper, we propose a secret sharing based federated learning architecture FedXGB to achieve the privacy-preserving extreme gradient boosting for mobile crowdsensing. Specifically, we first build a secure classification and regression tree (CART) of XGBoost using secret sharing. Then, we propose a secure prediction protocol to protect the model privacy of XGBoost in mobile crowdsensing. We conduct a comprehensive theoretical analysis and extensive experiments to evaluate the security, effectiveness, and efficiency of FedXGB. The results indicate that FedXGB is secure against the honest-but-curious adversaries and attains less than 1% accuracy loss compared with the original XGBoost model.

  匹配依据：MPC: secret sharing

  </details>

- **Access Structures Determined by Uniform Polymatroids**
  2020-05-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2005.04509)
  Renata Kawa, Mieczyslaw Kula

  <details><summary>摘要 / Abstract</summary>

  An access structure is said to be multipartite, if the set of participants is divided into several parts and all participants in the same part play an equivalent role. The search for ideal secret sharing schemes for some special interesting families of multipartite access structures, has been carried out by many authors. In this paper a new concept of study of ideal access structures is proposed. We do not consider special classes of access structures defined by imposing certain prescribed assumptions, but we investigate all access structures obtained from uniform polymatroids using the method developed by Farràs, Martí-Farré and Padró. They satisfy necessary condition to be ideal, i.e., they are matroid ports. Moreover some objects in this family can be useful for the applications of secret sharing. The choice of uniform polymatroids is motivated by the fact that each such polymatroid defines ideal access structures. The method presented in this article is universal and can be continued with other classes of polymatroids in further similar studies. Here we are especially interested in hierarchy of participants determined by the access structure and we distinguish two main classes: they are compartmented and hierarchical access structures. The vast majority of papers discussing hierarchical access structures consider access structures which are compartment or totally hierarchical. The main results are summarized in Section 4, which presents situations where partial hierarchy properties may arise. In particular, hierarchical orders of obtained structures are described. It is surprising, that the hierarchical orders of access structures obtained from uniform polymatroids are flat, i.e., every chain has at most 2 elements. The ideality of some families of hierarchical access structures is proved in Section 5.

  匹配依据：MPC: secret sharing

  </details>

- **TARDIS: A Foundation of Time-Lock Puzzles in UC**
  2020-05-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/537)
  Carsten Baum, Bernardo David, Rafael Dowsley, Jesper Buus Nielsen, Sabine Oechsner

  <details><summary>摘要 / Abstract</summary>

  Time-based primitives like time-lock puzzles (TLP) are finding widespread use in practical protocols, partially due to the surge of interest in the blockchain space where TLPs and related primitives are perceived to solve many problems. Unfortunately, the security claims are often shaky or plainly wrong since these primitives are used under composition. One reason is that TLPs are inherently not UC secure and time is tricky to model and use in the UC model. On the other hand, just specifying standalone notions of the intended task, left alone correctly using standalone notions like non-malleable TLPs only, might be hard or impossible for the given task. And even when possible a standalone secure primitive is harder to apply securely in practice afterwards as its behavior under composition is unclear. The ideal solution would be a model of TLPs in the UC framework to allow simple modular proofs. In this paper we provide a foundation for proving composable security of practical protocols using time-lock puzzles and related timed primitives in the UC model. We construct UC-secure TLPs based on random oracles and show that using random oracles is necessary. In order to prove security, we provide a simple and abstract way to reason about time in UC protocols. Finally, we demonstrate the usefulness of this foundation by constructing applications that are interesting in their own right, such as UC-secure two-party computation with output-independent abort.

  匹配依据：MPC: secure two party computation

  </details>

- **Influence of the Linear Layer on the Algebraic Degree in SP-Networks**
  2020-05-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/536)
  Carlos Cid, Lorenzo Grassi, Aldo Gunsing, Reinhard Lüftenegger, Christian Rechberger, Markus Schofnegger

  <details><summary>摘要 / Abstract</summary>

  We consider SPN schemes, i.e., schemes whose non-linear layer is defined as the parallel application of $t\ge 1$ independent S-Boxes over $\mathbb{F}_{2^n}$ and whose linear layer is defined by the multiplication with a $(n\cdot t)\times(n\cdot t)$ matrix over $\mathbb{F}_2$. Even if the algebraic representation of a scheme depends on all its components, upper bounds on the growth of the algebraic degree in the literature usually only consider the details of the non-linear layer. Hence a natural question arises: (how) do the details of the linear layer influence the growth of the algebraic degree? We show that the linear layer plays a crucial role in the growth of the algebraic degree and present a new upper bound on the algebraic degree in SP-networks. As main results, we prove that in the case of low-degree round functions with large S-Boxes: $\textit{(a)}$ an initial exponential growth of the algebraic degree can be followed by a linear growth until the maximum algebraic degree is reached; $\textit{(b)}$ the rate of the linear growth is proportional to the degree of the linear layer over $\mathbb{F}_{2^n}^t$. Besides providing a theoretical insight, our analysis is particularly relevant for assessing the security of cryptographic permutations designed to be competitive in applications like MPC, FHE, SNARKs, and STARKs, including permutations based on the Hades design strategy. We have verified our findings on small-scale instances and we have compared them against the currently best results in the literature, showing a substantial improvement of upper bounds on the algebraic degree in case of low-degree round functions with large S-Boxes.

  匹配依据：MPC: mpc (context)

  </details>

- **E-cclesia: Universally Composable Self-Tallying Elections**
  2020-05-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/513)
  Myrto Arapinis, Nikolaos Lamprou, Lenka Mareková, Thomas Zacharias, Léo Ackermann, Pavlos Georgiou

  <details><summary>摘要 / Abstract</summary>

  The technological advancements of the digital era paved the way for the facilitation of electronic voting (e-voting) in the promise of efficiency and enhanced security. In standard e-voting designs, the tally process is assigned to a committee of designated entities called talliers. Naturally, the security analysis of any e-voting system with tallier designation hinges on the assumption that a subset of the talliers follows the execution guidelines and does not attempt to breach privacy. As an alternative approach, Kiayias and Yung [PKC ’02] pioneered the self-tallying elections (STE) paradigm, where the post-ballot-casting (tally) phase can be performed by any interested party, removing the need for tallier designation. In this work, we explore the prospect of decentralized e-voting where security is preserved under concurrent protocol executions. In particular, we provide the first comprehensive formalization of STE in the universal composability (UC) framework introduced by Canetti [FOCS ’01] via an ideal functionality that captures required security properties such as voter privacy, eligibility, fairness, one-voter one-vote, and verifiability. We provide a concrete instantiation, called E-cclesia , that UC realizes our functionality. The design of E-cclesia integrates several cryptographic primitives such as signatures of knowledge for anonymous eligibility check, dynamic accumulators for scalability, time-lock encryption for fairness and anonymous broadcast channels for voter privacy. For the latter primitive, we provide the first UC formalization along with a construction based on mix-nets that utilises layered encryption, threshold secret sharing and equivocation techniques. Finally, we discuss deployment and scalability considerations for E-cclesia . We present preliminary benchmarks of the key operations (in terms of computational cost) of the voting client and demonstrate the feasibility of our proposal with readily available cryptographic tools for mid-sized elections (∼100,000 voters).

  匹配依据：MPC: secret sharing

  </details>

- **Storing and Retrieving Secrets on a Blockchain**
  2020-04-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/504)
  Vipul Goyal, Abhiram Kothapalli, Elisaweta Masserova, Bryan Parno, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  Multiple protocols implementing exciting cryptographic functionalities using blockchains such as time-lock encryption, one-time programs and fair multi-party computation assume the existence of a cryptographic primitive called extractable witness encryption. Unfortunately, there are no known efficient constructions (or even constructions based on any well studied assumptions) of extractable witness encryption. In this work, we propose a protocol that uses a blockchain itself to provide a functionality that is effectively the same as extractable witness encryption. By making small adjustments to the blockchain code, it is possible to easily implement applications that rely on extractable witness encryption and existed only as theoretical designs until now. There is also potential for new applications. As a key building block, our protocol uses a new and highly efficient batched dynamic proactive secret sharing scheme which may be of independent interest. We provide a proof-of-concept implementation of the extractable witness encryption construction and the underlying dynamic proactive secret sharing protocol.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Fast Threshold ECDSA with Honest Majority**
  2020-04-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/501)
  Ivan Damgård, Thomas Pelle Jakobsen, Jesper Buus Nielsen, Jakob Illeborg Pagter, Michael Bæksvang Østergård

  <details><summary>摘要 / Abstract</summary>

  ECDSA is a widely adopted digital signature standard. A number of threshold protocols for ECDSA have been developed that let a set of parties jointly generate the secret signing key and compute signatures, without ever revealing the signing key. Threshold protocols for ECDSA have seen recent interest, in particular due to the need for additional security in cryptocurrency wallets where leakage of the signing key is equivalent to an immediate loss of money. We propose a threshold ECDSA protocol secure against an active adversary in the honest majority model with abort. Our protocol is efficient in terms of both computation and bandwidth usage, and it allows the parties to pre-process parts of the signature, such that once the message to sign becomes known, they can compute a secret sharing of the signature very efficiently, using only local operations. We also show how to obtain fairness in the online phase at the cost of some additional work in the pre-processing, i.e., such that the protocol either aborts during the pre-processing phase, in which case nothing is revealed, or the signature is guaranteed to be delivered to all honest parties.

  匹配依据：MPC: secret sharing

  </details>

- **Collusion-Preserving Computation without a Mediator**
  2020-04-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/497)
  Michele Ciampi, Yun Lu, Vassilis Zikas

  <details><summary>摘要 / Abstract</summary>

  Collusion-free (CF) and collusion-preserving (CP) protocols enrich the standard security offered by multi-party computation (MPC), to tackle settings where subliminal communication is undesirable. However, all existing solutions make arguably unrealistic assumptions on setups, such as physical presence of the parties, access to physical envelopes, or extreme isolation, where the only means of communication is a star-topology network. The above state of affairs remained a limitation of such protocols, which was even reinforced by impossibility results. Thus, for years, it has been unclear if and how the above setup assumptions could be relaxed towards more realistic scenarios. Motivated also by the increasing interest in using hardware tokens for cryptographic applications, in this work we provide the first solution to collusion preserving computation which uses weaker and more common assumptions than the state of the art, i.e., an authenticated broadcast functionality and access to honestly generated trusted hardware tokens. We prove that our protocol is collusion-preserving (in short, {\em CP}) secure as long as no parties abort. In the case of an aborting adversary, our protocol still achieves standard (G)UC security with identifiable (and unanimous) abort. Leveraging the above identifiability property, we augment our protocol with a penalization scheme which ensures that it is not profitable to abort, thereby obtaining CP security against incentive-driven attackers. To define (and prove) this latter result, we combine the Rational Protocol Design (RPD) methodology by Garay {\em et al.} [FOCS 2013] with the CP framework of Alwen {\em et al.} [CRYPTO 2012] to derive a definition of security in the presence of incentive-driven local adversaries which can be of independent interest. Similar to existing CP/CF solutions, our protocol preserves, as a fallback, security against monolithic adversaries, even when the setup (i.e., the hardware tokens) is compromised or corrupted. In addition, our fallback solution achieves identifiable and unanimous abort, which we prove are impossible in previous CP solutions.

  匹配依据：MPC: multi party computation

  </details>

- **Private Dataset Generation Using Privacy Preserving Collaborative Learning**
  2020-04-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.13598)
  Amit Chaulwar

  <details><summary>摘要 / Abstract</summary>

  With increasing usage of deep learning algorithms in many application, new research questions related to privacy and adversarial attacks are emerging. However, the deep learning algorithm improvement needs more and more data to be shared within research community. Methodologies like federated learning, differential privacy, additive secret sharing provides a way to train machine learning models on edge without moving the data from the edge. However, it is very computationally intensive and prone to adversarial attacks. Therefore, this work introduces a privacy preserving FedCollabNN framework for training machine learning models at edge, which is computationally efficient and robust against adversarial attacks. The simulation results using MNIST dataset indicates the effectiveness of the framework.

  匹配依据：MPC: secret sharing

  </details>

- **On the weight distribution of some minimal codes**
  2020-04-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.13774)
  Daniele Bartoli, Matteo Bonini, Marco Timpanella

  <details><summary>摘要 / Abstract</summary>

  Minimal codes are a class of linear codes which gained interest in the last years, thanks to their connections to secret sharing schemes. In this paper we provide the weight distribution and the parameters of families of minimal codes recently introduced by C. Tang, Y. Qiu, Q. Liao, Z. Zhou, answering some open questions.

  匹配依据：MPC: secret sharing

  </details>

- **On Ideal and Weakly-Ideal Access Structures**
  2020-04-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/483)
  Reza Kaboli, Shahram Khazaei, Maghsoud Parviz

  <details><summary>摘要 / Abstract</summary>

  For more than two decades, proving or refuting the following statement has remained a challenging open problem in the theory of secret sharing schemes (SSSs): every ideal access structure admits an ideal perfect multi-linear SSS. We consider a weaker statement in this paper asking if: every ideal access structure admits an ideal perfect group-characterizable (GC) SSS. Since the class of GC SSSs is known to include the multi-linear ones (as well as several classes of non-linear schemes), it might turn out that the second statement is not only true but also easier to tackle. Unfortunately, our understanding of GC SSSs is still too basic to tackle the weaker statement. As a first attempt, it is natural to ask if every ideal perfect SSS is equivalent to some GC scheme. The main contribution of this paper is to construct counterexamples using tools from theory of Latin squares and some recent results developed by the present authors for studying GC SSSs.

  匹配依据：MPC: secret sharing

  </details>

- **Leakage-Resilient Extractors and Secret-Sharing against Bounded Collusion Protocols**
  2020-04-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/478)
  Eshan Chattopadhyay, Jesse Goodman, Vipul Goyal, Xin Li

  <details><summary>摘要 / Abstract</summary>

  In a recent work, Kumar, Meka, and Sahai (FOCS 2019) introduced the notion of bounded collusion protocols (BCPs), in which $N$ parties wish to compute some joint function $f:(\{0,1\}^n)^N\to\{0,1\}$ using a public blackboard, but such that only $p$ parties may collude at a time. This generalizes well studied models in multiparty communication complexity, such as the number-in-hand (NIH) and number-on-forehead (NOF) models, which are just endpoints on this rich spectrum. We construct explicit hard functions against this spectrum, and achieve a tradeoff between collusion and complexity. Using this, we obtain improved leakage-resilient secret sharing schemes against bounded collusion protocols. Our main tool in obtaining hard functions against BCPs are explicit constructions of leakage resilient extractors against BCPs for a wide range of parameters. Kumar et al. (FOCS 2019) studied such extractors and called them cylinder intersection extractors. In fact, such extractors directly yield correlation bounds against BCPs. We focus on the following setting: the input to the extractor consists of $N$ independent sources of length $n$, and the leakage function Leak $:(\{0,1\}^n)^N\to\{0,1\}^\mu\in\mathcal{F}$ is a BCP with some collusion bound $p$ and leakage (output length) $\mu$. While our extractor constructions are very general, we highlight some interesting parameter settings: 1. In the case when the input sources are uniform, and $p=0.99N$ parties collude, our extractor can handle $n^{\Omega(1)}$ bits of leakage, regardless of the dependence between $N,n$. The best NOF lower bound (i.e., $p=N-1$) on the other hand requires $N&lt;\log n$ even to handle $1$ bit of leakage. 2. Next, we show that for the same setting as above, we can drop the entropy requirement to $k=$ polylog $n$, while still handling polynomial leakage for $p=0.99N$. This resolves an open question about cylinder intersection extractors raised by Kumar et al. (FOCS 2019), and we find an application of such low entropy extractors in a new type of secret sharing. We also provide an explicit compiler that transforms any function with high NOF (distributional) communication complexity into a leakage-resilient extractor that can handle polylogarithmic entropy and substantially more leakage against BCPs. Thus any improvement of NOF lower bounds will immediately yield better leakage-resilient extractors. Using our extractors against BCPs, we obtain improved $N$-out-of-$N$ leakage-resilient secret sharing schemes. The previous best scheme from Kumar et al. (FOCS 2019) required share size to grow exponentially in the collusion bound, and thus cannot efficiently handle $p=\omega(\log N)$. Our schemes have no dependence of this form, and can thus handle collusion size $p=0.99N$.

  匹配依据：MPC: secret sharing

  </details>

- **Improved Black-Box Constructions of Composable Secure Computation**
  2020-04-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/494)
  Rohit Chatterjee, Xiao Liang, Omkant Pandey

  <details><summary>摘要 / Abstract</summary>

  We close the gap between black-box and non-black-box constructions of $\mathit{composable}$ secure multiparty computation in the plain model under the $\mathit{minimal}$ assumption of semi-honest oblivious transfer. The notion of protocol composition we target is $\mathit{angel\text{-}based}$ security, or more precisely, security with super-polynomial helpers. In this notion, both the simulator and the adversary are given access to an oracle called an $\mathit{angel}$ that can perform some predefined super-polynomial time task. Angel-based security maintains the attractive properties of the universal composition framework while providing meaningful security guarantees in complex environments without having to trust anyone. Angel-based security can be achieved using non-black-box constructions in $\max(R_{\mathsf{OT}},\widetilde{O}(\log n))$ rounds where $R_{\mathsf{OT}}$ is the round-complexity of the semi-honest oblivious transfer. However, currently, the best known $\mathit{black\text{-}box}$ constructions under the same assumption require $\max(R_{\mathsf{OT}},\widetilde{O}(\log^2 n))$ rounds. If $R_{\mathsf{OT}}$ is a constant, the gap between non-black-box and black-box constructions can be a multiplicative factor $\log n$. We close this gap by presenting a $\max(R_{\mathsf{OT}},\widetilde{O}(\log n))$-round black-box construction. We achieve this result by constructing constant-round 1-1 CCA-secure commitments assuming only black-box access to one-way functions.

  匹配依据：MPC: oblivious transfer, secure computation, secure multiparty computation

  </details>

- **Generalized Channels from Limited Blockchain Scripts and Adaptor Signatures**
  2020-04-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/476)
  Lukas Aumayr, Oguzhan Ersoy, Andreas Erwig, Sebastian Faust, Kristina Hostakova, Matteo Maffei, Pedro Moreno-Sanchez, Siavash Riahi

  <details><summary>摘要 / Abstract</summary>

  Decentralized and permissionless ledgers offer an inherently low transaction rate, as a result of their consensus protocol demanding the storage of each transaction on-chain. A prominent proposal to tackle this scalability issue is to utilize off-chain protocols, where parties only need to post a limited number of transactions on-chain. Existing solutions can roughly be categorized into: (i) application-specific channels (e.g., payment channels), offering strictly weaker functionality than the underlying blockchain; and (ii) state channels, supporting arbitrary smart contracts at the cost of being compatible only with the few blockchains having Turing-complete scripting languages (e.g., Ethereum). In this work, we introduce and formalize the notion of generalized channels allowing users to perform any operation supported by the underlying blockchain in an off-chain manner. Generalized channels thus extend the functionality of payment channels and relax the definition of state channels. We present a concrete construction compatible with any blockchain supporting transaction authorization, time-locks and constant number of Boolean $\land$ and $\lor$ operations -- requirements fulfilled by many (non-Turing-complete) blockchains including the popular Bitcoin. To this end, we leverage adaptor signatures -- a cryptographic primitive already used in the cryptocurrency literature but formalized as a standalone primitive in this work for the first time. We formally prove the security of our generalized channel construction in the Universal Composability framework. As an important practical contribution, our generalized channel construction outperforms the state-of-the-art payment channel construction, the Lightning Network, in efficiency. Concretely, it halves the off-chain communication complexity and reduces the on-chain footprint in case of disputes from linear to constant in the number of off-chain applications funded by the channel. Finally, we evaluate the practicality of our construction via a prototype implementation and discuss various applications including financially secured fair two-party computation.

  匹配依据：MPC: two party computation

  </details>
