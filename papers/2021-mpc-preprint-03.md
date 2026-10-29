# 2021 · MPC · 仅预印本来源 · 第 3/3 页

[总目录](../PAPERS.md) · [上一页](2021-mpc-preprint-02.md)

- **Trust but Verify: Cryptographic Data Privacy for Mobility Management**
  2021-04-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.07768)
  Matthew Tsao, Kaidi Yang, Stephen Zoepf, Marco Pavone

  <details><summary>摘要 / Abstract</summary>

  The era of Big Data has brought with it a richer understanding of user behavior through massive data sets, which can help organizations optimize the quality of their services. In the context of transportation research, mobility data can provide Municipal Authorities (MA) with insights on how to operate, regulate, or improve the transportation network. Mobility data, however, may contain sensitive information about end users and trade secrets of Mobility Providers (MP). Due to this data privacy concern, MPs may be reluctant to contribute their datasets to MA. Using ideas from cryptography, we propose an interactive protocol between a MA and a MP in which MA obtains insights from mobility data without MP having to reveal its trade secrets or sensitive data of its users. This is accomplished in two steps: a commitment step, and a computation step. In the first step, Merkle commitments and aggregated traffic measurements are used to generate a cryptographic commitment. In the second step, MP extracts insights from the data and sends them to MA. Using the commitment and zero-knowledge proofs, MA can certify that the information received from MP is accurate, without needing to directly inspect the mobility data. We also present a differentially private version of the protocol that is suitable for the large query regime. The protocol is verifiable for both MA and MP in the sense that dishonesty from one party can be detected by the other. The protocol can be readily extended to the more general setting with multiple MPs via secure multi-party computation.

  匹配依据：MPC: secure multi party computation

  </details>

- **PrivateDrop: Practical Privacy-Preserving Authentication for Apple AirDrop**
  2021-04-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/481)
  Alexander Heinrich, Matthias Hollick, Thomas Schneider, Milan Stute, Christian Weinert

  <details><summary>摘要 / Abstract</summary>

  Apple&#x27;s offline file-sharing service AirDrop is integrated into more than 1.5 billion end-user devices worldwide. We discovered two design flaws in the underlying protocol that allow attackers to learn the phone numbers and email addresses of both sender and receiver devices. As a remediation, we study the applicability of private set intersection (PSI) to mutual authentication, which is similar to contact discovery in mobile messengers. We propose a novel optimized PSI-based protocol called PrivateDrop that addresses the specific challenges of offline resource-constrained operation and integrates seamlessly into the current AirDrop protocol stack. Using our native PrivateDrop implementation for iOS and macOS, we experimentally demonstrate that PrivateDrop preserves AirDrop&#x27;s exemplary user experience with an authentication delay well below one second. We responsibly disclosed our findings to Apple and open-sourced our PrivateDrop implementation.

  匹配依据：MPC: private set intersection

  </details>

- **Private Liquidity Matching using MPC**
  2021-04-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/475)
  Shahla Atapoor, Nigel P. Smart, Younes Talibi Alaoui

  <details><summary>摘要 / Abstract</summary>

  Many central banks, as well as blockchain systems, are looking into distributed versions of interbank payment systems, in particular the netting procedure. When executed in a distributed manner this presents a number of privacy problems. This paper studies a privacy preserving netting protocol to solve the gridlock resolution problem in such Real Time Gross Settlement systems. Our solution utilizes Multi-party Computation and is implemented in the SCALE MAMBA system, using Shamir secret sharing scheme over three parties in an actively secure manner. Our experiments show that, even for large throughput systems, such a privacy preserving operation is often feasible.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Fast Private Parameter Learning and Inference for Sum-Product Networks**
  2021-04-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.07353)
  Ernst Althaus, Mohammad Sadeq Dousti, Stefan Kramer, Nick Johannes Peter Rassau

  <details><summary>摘要 / Abstract</summary>

  A sum-product network (SPN) is a graphical model that allows several types of inferences to be drawn efficiently. There are two types of learning for SPNs: Learning the architecture of the model, and learning the parameters. In this paper, we tackle the second problem: We show how to learn the weights for the sum nodes, assuming the architecture is fixed, and the data is horizontally partitioned between multiple parties. The computations will preserve the privacy of each participant. Furthermore, we will use secret sharing instead of (homomorphic) encryption, which allows fast computations and requires little computational resources. To this end, we use a novel integer division to compute approximate real divisions. We also show how simple and private inferences can be performed using the learned SPN.

  匹配依据：MPC: secret sharing

  </details>

- **On Mignotte Secret Sharing Schemes over Gaussian Integers**
  2021-04-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.06361)
  Diego Munuera-Merayo

  <details><summary>摘要 / Abstract</summary>

  Secret Sharing Schemes (SSS) are methods for distributing a secret among a set of participants. One of the first Secret Sharing Schemes was proposed by M. Mignotte, based on the Chinese remainder theorem over the ring of integers. In this article we extend the Mignotte&#x27;s scheme to the ring of Gaussian Integers and study some of its properties. While doing this we aim to solve a gap in a previous construction of such extension. In addition we show that any access structure can be made through a SSS over $ \mathbb{Z}[i]$.

  匹配依据：MPC: secret sharing

  </details>

- **Fair and Differentially Private Distributed Frequency Estimation**
  2021-04-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.05974)
  Mengmeng Yang, Ivan Tjuawinata, Kwok-Yan Lam, Tianqing Zhu, Jun Zhao

  <details><summary>摘要 / Abstract</summary>

  In order to remain competitive, Internet companies collect and analyse user data for the purpose of improving user experiences. Frequency estimation is a widely used statistical tool which could potentially conflict with the relevant privacy regulations. Privacy preserving analytic methods based on differential privacy have been proposed, which either require a large user base or a trusted server; hence may give big companies an unfair advantage while handicapping smaller organizations in their growth opportunity. To address this issue, this paper proposes a fair privacy-preserving sampling-based frequency estimation method and provides a relation between its privacy guarantee, output accuracy, and number of participants. We designed decentralized privacy-preserving aggregation mechanisms using multi-party computation technique and established that, for a limited number of participants and a fixed privacy level, our mechanisms perform better than those that are based on traditional perturbation methods; hence, provide smaller companies a fair growth opportunity. We further propose an architectural model to support weighted aggregation in order to achieve higher accuracy estimate to cater for users with different privacy requirements. Compared to the unweighted aggregation, our method provides a more accurate estimate. Extensive experiments are conducted to show the effectiveness of the proposed methods.

  匹配依据：MPC: multi party computation

  </details>

- **Viaduct: An Extensible, Optimizing Compiler for Secure Distributed Programs (Technical Report)**
  2021-04-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/468)
  Coşku Acay, Rolph Recto, Joshua Gancher, Andrew C. Myers, Elaine Shi

  <details><summary>摘要 / Abstract</summary>

  Modern distributed systems involve interactions between principals with limited trust, so cryptographic mechanisms are needed to protect confidentiality and integrity. At the same time, most developers lack the training to securely employ cryptography. We present Viaduct, a compiler that transforms high-level programs into secure, efficient distributed realizations. Viaduct&#x27;s source language allows developers to declaratively specify security policies by annotating their programs with information flow labels. The compiler uses these labels to synthesize distributed programs that use cryptography efficiently while still defending the source-level security policy. The Viaduct approach is general, and can be easily extended with new security mechanisms. Our implementation of the Viaduct compiler comes with an extensible runtime system that includes plug-in support for multiparty computation, commitments, and zero-knowledge proofs. We have evaluated the system on a set of benchmarks, and the results indicate that our approach is feasible and can use cryptography in efficient, nontrivial ways.

  匹配依据：MPC: multiparty computation

  </details>

- **Upslices, Downslices, and Secret-Sharing with Complexity of $1.5^n$**
  2021-04-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/470)
  Benny Applebaum, Oded Nir

  <details><summary>摘要 / Abstract</summary>

  A secret-sharing scheme allows to distribute a secret $s$ among $n$ parties such that only some predefined ``authorized&#x27;&#x27; sets of parties can reconstruct the secret, and all other ``unauthorized&#x27;&#x27; sets learn nothing about $s$. The collection of authorized/unauthorized sets can be captured by a monotone function $f:\{0,1\}^n\rightarrow \{0,1\}$. In this paper, we focus on monotone functions that all their min-terms are sets of size $a$, and on their duals -- monotone functions whose max-terms are of size $b$. We refer to these classes as $(a,n)$-upslices and $(b,n)$-downslices, and note that these natural families correspond to monotone $a$-regular DNFs and monotone $(n-b)$-regular CNFs. We derive the following results. 1. (General downslices) Every downslice can be realized with total share size of $1.5^{n+o(n)}&lt;2^{0.585 n}$. Since every monotone function can be cheaply decomposed into $n$ downslices, we obtain a similar result for general access structures improving the previously known $2^{0.637n+o(n)}$ complexity of Applebaum, Beimel, Nir and Peter (STOC 2020). We also achieve a minor improvement in the exponent of linear secrets sharing schemes. 2. (Random mixture of upslices) Following Beimel and Farras (TCC 2020) who studied the complexity of random DNFs with constant-size terms, we consider the following general distribution $F$ over monotone DNFs: For each width value $a\in [n]$, uniformly sample $k_a$ monotone terms of size $a$, where $k=(k_1,\ldots,k_n)$ is an arbitrary vector of non-negative integers. We show that, except with exponentially small probability, $F$ can be realized with share size of $2^{0.5 n+o(n)}$ and can be linearly realized with an exponent strictly smaller than $2/3$. Our proof also provides a candidate distribution for ``exponentially-hard&#x27;&#x27; access structure. We use our results to explore connections between several seemingly unrelated questions about the complexity of secret-sharing schemes such as worst-case vs. average-case, linear vs. non-linear and primal vs. dual access structures. We prove that, in at least one of these settings, there is a significant gap in secret-sharing complexity.

  匹配依据：MPC: secret sharing

  </details>

- **Practical Two-party Privacy-preserving Neural Network Based on Secret Sharing**
  2021-04-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.04709)
  Zhengqiang Ge, Zhipeng Zhou, Dong Guo, Qiang Li

  <details><summary>摘要 / Abstract</summary>

  Neural networks, with the capability to provide efficient predictive models, have been widely used in medical, financial, and other fields, bringing great convenience to our lives. However, the high accuracy of the model requires a large amount of data from multiple parties, raising public concerns about privacy. Privacy-preserving neural network based on multi-party computation is one of the current methods used to provide model training and inference under the premise of solving data privacy. In this study, we propose a new two-party privacy-preserving neural network training and inference framework in which privacy data is distributed to two non-colluding servers. We construct a preprocessing protocol for mask generation, support and realize secret sharing comparison on 2PC, and propose a new method to further reduce the communication rounds. Based on the comparison protocol, we construct building blocks such as division and exponential, and realize the process of training and inference that no longer needs to convert between different types of secret sharings and is entirely based on arithmetic secret sharing. Compared with the previous works, our work obtains higher accuracy, which is very close to that of plaintext training. While the accuracy has been improved, the runtime is reduced, considering the online phase, our work is 5x faster than SecureML, 4.32-5.75x faster than SecureNN, and is very close to the current optimal 3PC implementation, FALCON. For secure inference, as far as known knowledge is concerned, we should be the current optimal 2PC implementation, which is 4-358x faster than other works.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Non-Destructive Zero-Knowledge Proofs on Quantum States, and Multi-Party Generation of Authorized Hidden GHZ States**
  2021-04-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.04742)
  Léo Colisson, Frédéric Grosshans, Elham Kashefi

  <details><summary>摘要 / Abstract</summary>

  We propose the first generalization of the famous Non-Interactive Zero-Knowledge (NIZK) proofs to quantum languages (NIZKoQS) and we provide a protocol to prove advanced properties on a received quantum state non-destructively and non-interactively (a single message being sent from the prover to the verifier). In our second orthogonal contribution, we improve the costly Remote State Preparation protocols [CCKW18,CCKW19,GV19] that can classically fake a quantum channel (this is at the heart of our NIZKoQS protocol) by showing how to create a multi-qubits state from a single superposition. Finally, we generalize these results to a multi-party setting and prove that multiple parties can anonymously distribute a GHZ state in such a way that only participants knowing a secret credential can share this state, which could have applications to quantum anonymous transmission, quantum secret sharing, quantum onion routing and more.

  匹配依据：MPC: secret sharing

  </details>

- **RandChain: Practical Scalable Decentralized Randomness Attested by Blockchain**
  2021-04-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/450)
  Gang Wang, Mark Nixon

  <details><summary>摘要 / Abstract</summary>

  Reliable and verifiable public randomness is not only an essential building block in various cryptographic primitives, but also is a critical component in many distributed and decentralized protocols, e.g., blockchain sharding. A &#x27;good&#x27; randomness generator should preserve several distinctive properties, such as public-verifiability, bias-resistance, unpredictability, and availability. However, it is a challenging task to generate such good randomness. For instance, a dishonest party may behave deceptively to bias the final randomness, which is toward his preferences. And this challenge is more serious in a distributed and decentralized system. Blockchain technology provides several promising features, such as decentralization, immutability, and trustworthiness. Due to extremely high overheads on both communication and computation, most existing solutions face an additional scalability issue. We propose a sharding-based scheme, RandChain, to obtain a practical scalable distributed and decentralized randomness attested by blockchain in large-scale applications. In RandChain, we eliminate the use of computation-heavy cryptographic operations, e.g., Publicly Verifiable Secret Sharing (PVSS), in prevalent approaches. We build a sub-routine, RandGene, which utilizes a commit-then-reveal strategy to establish local randomness, enforced by efficient Verifiable Random Function (VRF). RandGene generates the randomness based on statistical approaches, instead of cryptographic operations, to eliminate computational operations. RandChain maintains a two-layer hierarchical chain structure via a sharding scheme. The first level chain is maintained by RandGene within each shard to provide a verifiable randomness source by blockchain. The second level chain uses the randomnesses from each shard to build a randomness chain.

  匹配依据：MPC: secret sharing

  </details>

- **Differential phase shift quantum secret sharing using twin field**
  2021-04-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.03467)
  Jie Gu, Xiao-Yu Cao, Hua-Lei Yin, Zeng-Bing Chen

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) is essential for multiparty quantum communication, which is one of cornerstones in the future quantum internet. However, a linear rate-distance limitation severely constrains the secure key rate and transmission distance of QSS. Here, we present a practical QSS protocol among three participants based on the differential phase shift scheme and twin field ideas for the solution of high-efficiency multiparty communication task. In contrast to formerly proposed differential phase shift QSS protocol, our protocol can break the linear rate-distance bound, theoretically improving the secret key rate by three orders of magnitude in a 300-km-long fiber. Furthermore, the new protocol is secure against Trojan horse attacks that cannot be resisted by previous differential phase shift QSS.

  匹配依据：MPC: secret sharing

  </details>

- **Shared-Dining: Broadcasting Secret Shares using Dining-Cryptographers Groups**
  2021-04-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.03032)
  David Mödinger, Juri Dispan, Franz J. Hauck

  <details><summary>摘要 / Abstract</summary>

  A k-anonymous broadcast can be implemented using a small group of dining cryptographers to first share the message, followed by a flooding phase started by group members. Members have little incentive to forward the message in a timely manner, as forwarding incurs costs, or they may even profit from keeping the message. In worst case, this leaves the true originator as the only sender, rendering the dining-cryptographers phase useless and compromising their privacy. We present a novel approach using a modified dining-cryptographers protocol to distributed shares of an (n,k)-Shamir&#x27;s secret sharing scheme. Finally, all group members broadcast their received share through the network, allowing any recipient of k shares to reconstruct the message, enforcing anonymity. If less than k group members broadcast their shares, the message cannot be decoded thus preventing privacy breaches for the originator. Our system provides (n-|attackers|)-anonymity for up to k-1 attackers and has little performance impact on dissemination. We show these results in a security analysis and performance evaluation based on a proof-of-concept prototype. Throughput rates between 10 and 100 kB/s are enough for many real applications with high privacy requirements, e.g., financial blockchain system.

  匹配依据：MPC: secret sharing

  </details>

- **Prism: Private Verifiable Set Computation over Multi-Owner Outsourced Databases**
  2021-04-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.03354)
  Yin Li, Dhrubajyoti Ghosh, Peeyush Gupta, Sharad Mehrotra, Nisha Panwar, Shantanu Sharma

  <details><summary>摘要 / Abstract</summary>

  This paper proposes Prism, a secret sharing based approach to compute private set operations (i.e., intersection and union), as well as aggregates over outsourced databases belonging to multiple owners. Prism enables data owners to pre-load the data onto non-colluding servers and exploits the additive and multiplicative properties of secret-shares to compute the above-listed operations in (at most) two rounds of communication between the servers (storing the secret-shares) and the querier, resulting in a very efficient implementation. Also, Prism does not require communication among the servers and supports result verification techniques for each operation to detect malicious adversaries. Experimental results show that Prism scales both in terms of the number of data owners and database sizes, to which prior approaches do not scale.

  匹配依据：MPC: secret sharing

  </details>

- **Lower Bounds Implementing Mediators in Asynchronous Systems**
  2021-04-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.02759)
  Ivan Geffner, Joseph Y. Halpern

  <details><summary>摘要 / Abstract</summary>

  Abraham, Dolev, Geffner, and Halpern proved that, in asynchronous systems, a $(k,t)$-robust equilibrium for $n$ players and a trusted mediator can be implemented without the mediator as long as $n &gt; 4(k+t)$, where an equilibrium is $(k,t)$-robust if, roughly speaking, no coalition of $t$ players can decrease the payoff of any of the other players, and no coalition of $k$ players can increase their payoff by deviating. We prove that this bound is tight, in the sense that if $n \le 4(k+t)$ there exist $(k,t)$-robust equilibria with a mediator that cannot be implemented by the players alone. Even though implementing $(k,t)$-robust mediators seems closely related to implementing asynchronous multiparty $(k+t)$-secure computation \cite{BCG93}, to the best of our knowledge there is no known straightforward reduction from one problem to another. Nevertheless, we show that there is a non-trivial reduction from a slightly weaker notion of $(k+t)$-secure computation, which we call $(k+t)$-strict secure computation, to implementing $(k,t)$-robust mediators. We prove the desired lower bound by showing that there are functions on $n$ variables that cannot be $(k+t)$-strictly securely computed if $n \le 4(k+t)$. This also provides a simple alternative proof for the well-known lower bound of $4t+1$ on asynchronous secure computation in the presence of up to $t$ malicious agents.

  匹配依据：MPC: secure computation

  </details>

- **Formal security analysis of MPC-in-the-head zero-knowledge protocols**
  2021-04-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/437)
  Nikolaj Sidorenco, Sabine Oechsner, Bas Spitters

  <details><summary>摘要 / Abstract</summary>

  Zero-knowledge proofs allow a prover to convince a verifier of the veracity of a statement without revealing any other information. An interesting class of zero-knowledge protocols are those following the MPC-in-the-head paradigm (Ishai et al., STOC ’07) which use secure multiparty computation (MPC) protocols as the basis. Efficient instances of this paradigm have emerged as an active research topic in the last years, starting with ZKBoo (Giacomelli et al., USENIX ’16). Zero-knowledge protocols are a vital building block in the design of privacy-preserving technologies as well as cryptographic primitives like digital signature schemes that provide post-quantum security. This work investigates the security of zero-knowledge protocols following the MPC-in-the-head paradigm. We provide the first machine-checked security proof of such a protocol on the example of ZKBoo. Our proofs are checked in the EasyCrypt proof assistant. To enable a modular security proof, we develop a new security notion for the MPC protocols used in MPC-in-the-head zero-knowledge protocols. This allows us to recast existing security proofs in a black-box fashion which we believe to be of independent interest.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Private Computation of Polynomials over Networks**
  2021-04-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.01369)
  Teimour Hosseinalizadeh, Fatih Turkmen, Nima Monshizadeh

  <details><summary>摘要 / Abstract</summary>

  This study concentrates on preserving privacy in a network of agents where each agent seeks to evaluate a general polynomial function over the private values of her immediate neighbors. We provide an algorithm for the exact evaluation of such functions while preserving privacy of the involved agents. The solution is based on a reformulation of polynomials and adoption of two cryptographic primitives: Paillier as a Partially Homomorphic Encryption scheme and multiplicative-additive secret sharing. The provided algorithm is fully distributed, lightweight in communication, robust to dropout of agents, and can accommodate a wide class of functions. Moreover, system theoretic and secure multi-party conditions guaranteeing the privacy preservation of an agent&#x27;s private values against a set of colluding agents are established. The theoretical developments are complemented by numerical investigations illustrating the accuracy of the algorithm and the resulting computational cost.

  匹配依据：MPC: secret sharing

  </details>

- **Monte Carlo execution time estimation for Privacy-preserving Distributed Function Evaluation protocols**
  2021-04-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.01281)
  Stefano M P C Souza, Daniel G Silva

  <details><summary>摘要 / Abstract</summary>

  Recent developments in Machine Learning and Deep Learning depend heavily on cloud computing and specialized hardware, such as GPUs and TPUs. This forces those using those models to trust private data to cloud servers. Such scenario has prompted a large interest on Homomorphic Cryptography and Secure Multi-Party Computation protocols that allow the use of cloud computing power in a privacy-preserving manner. When comparing the efficiency of such protocols, most works in literature resort to complexity analysis that gives asymptotic higher-bounding limits of computational cost when input size tends to infinite. These limits may be very different from the actual cost or execution time, when performing such computations over small, or average-sized datasets. We argue that Monte Carlo methods can render better computational cost and time estimates, fostering better design and implementation decisions for complex systems, such as Privacy-Preserving Machine Learning Frameworks.

  匹配依据：MPC: secure multi party computation

  </details>

- **PolyDNN: Polynomial Representation of NN for Communication-less SMPC Inference**
  2021-04-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.00863)
  Philip Derbeko, Shlomi Dolev

  <details><summary>摘要 / Abstract</summary>

  The structure and weights of Deep Neural Networks (DNN) typically encode and contain very valuable information about the dataset that was used to train the network. One way to protect this information when DNN is published is to perform an interference of the network using secure multi-party computations (MPC). In this paper, we suggest a translation of deep neural networks to polynomials, which are easier to calculate efficiently with MPC techniques. We show a way to translate complete networks into a single polynomial and how to calculate the polynomial with an efficient and information-secure MPC algorithm. The calculation is done without intermediate communication between the participating parties, which is beneficial in several cases, as explained in the paper.

  匹配依据：MPC: smpc (context)

  </details>

- **PyVertical: A Vertical Federated Learning Framework for Multi-headed SplitNN**
  2021-04-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.00489)
  Daniele Romanini, Adam James Hall, Pavlos Papadopoulos, Tom Titcombe, Abbas Ismail, Tudor Cebere, Robert Sandmann, Robin Roehm, Michael A. Hoeh

  <details><summary>摘要 / Abstract</summary>

  We introduce PyVertical, a framework supporting vertical federated learning using split neural networks. The proposed framework allows a data scientist to train neural networks on data features vertically partitioned across multiple owners while keeping raw data on an owner&#x27;s device. To link entities shared across different datasets&#x27; partitions, we use Private Set Intersection on IDs associated with data points. To demonstrate the validity of the proposed framework, we present the training of a simple dual-headed split neural network for a MNIST classification task, with data samples vertically distributed across two data owners and a data scientist.

  匹配依据：MPC: private set intersection

  </details>

- **Stacking Sigmas: A Framework to Compose $\\Sigma$-Protocols for Disjunctions**
  2021-03-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/422)
  Aarushi Goel, Matthew Green, Mathias Hall-Andersen, Gabriel Kaptchuk

  <details><summary>摘要 / Abstract</summary>

  Zero-Knowledge (ZK) Proofs for disjunctive statements have been a focus of a long line of research. Classical results such as Cramer {\em et al.} [CRYPTO&#x27;94] and Abe {\em et al.} [AC&#x27;02] design generic compilers that transform certain classes of ZK proofs into ZK proofs for disjunctive statements. However, communication complexity of the resulting protocols in these results ends up being proportional to the complexity of proving all clauses in the disjunction. More recently, Heath {\em et al.} [EC&#x27;20] exploited special properties of garbled circuits to construct efficient ZK proofs for disjunctions, where the proof size is only proportional to the length of the largest clause in the disjunction. However, these techniques do not appear to generalize beyond garbled circuits. In this work, we focus on achieving the best of both worlds. We design a \textit{general framework} that compiles a large class of {unmodified} $\Sigma$-protocols, each for an individual statement, into a new $\Sigma$-protocol that proves a disjunction of these statements. Our framework can be used both when each clause is proved with the same $\Sigma$-protocol and when different $\Sigma$-protocols are used for different clauses. The resulting $\Sigma$-protocol is concretely efficient and has communication complexity proportional to the communication required by the largest clause, with additive terms that are only logarithmic in the number of clauses. We show that our compiler can be applied to many well-known $\Sigma$-protocols, including classical protocols (\emph{e.g.} Schnorr [JC&#x27;91] and Guillou-Quisquater [CRYPTO&#x27;88]) and modern MPC-in-the-head protocols such as the recent work of Katz, Kolesnikov and Wang [CCS&#x27;18] and the Ligero protocol of Ames {\em et al.} [CCS&#x27;17]. Finally, since all of the protocols in our class can be made non-interactive in the random oracle model using the Fiat-Shamir transform, our result yields the first generic non-interactive zero-knowledge protocol for disjunctions where the communication only depends on the size of the largest clause.

  匹配依据：MPC: garbled circuits

  </details>

- **Multi-party computation enables secure polynomial control based solely on secret-sharing**
  2021-03-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2103.16335)
  Sebastian Schlor, Michael Hertneck, Stefan Wildhagen, Frank Allgöwer

  <details><summary>摘要 / Abstract</summary>

  Encrypted control systems allow to evaluate feedback laws on external servers without revealing private information about state and input data, the control law, or the plant. While there are a number of encrypted control schemes available for linear feedback laws, only few results exist for the evaluation of more general control laws. Recently, an approach to encrypted polynomial control was presented, relying on two-party secret sharing and an inter-server communication protocol using homomorphic encryption. As homomorphic encryptions are much more computationally demanding than secret sharing, they make up for a tremendous amount of the overall computational demand of this scheme. For this reason, in this paper, we demonstrate that multi-party computation enables secure polynomial control based solely on secret sharing. We introduce a novel secure three-party control scheme based on three-party computation. Further, we propose a novel $n$-party control scheme to securely evaluate polynomial feedback laws of arbitrary degree without inter-server communication. The latter property makes it easier to realize the necessary requirement regarding non-collusion of the servers, with which perfect security can be guaranteed. Simulations suggest that the presented control schemes are many times less computationally demanding than the two-party scheme mentioned above.

  匹配依据：MPC: multi party computation, secret sharing, three party computation

  </details>

- **Topology-Hiding Communication from Minimal Assumptions.**
  2021-03-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/388)
  Marshall Ball, Elette Boyle, Ran Cohen, Lisa Kohl, Tal Malkin, Pierre Meyer, Tal Moran

  <details><summary>摘要 / Abstract</summary>

  Topology-hiding broadcast (THB) enables parties communicating over an incomplete network to broadcast messages while hiding the topology from within a given class of graphs. THB is a central tool underlying general topology-hiding secure computation (THC) (Moran et al. TCC’15). Although broadcast is a privacy-free task, it was recently shown that THB for certain graph classes necessitates computational assumptions, even in the semi-honest setting, and even given a single corrupted party. In this work we investigate the minimal assumptions required for topology-hiding communication: both Broadcast or Anonymous Broadcast (where the broadcaster’s identity is hidden). We develop new techniques that yield a variety of necessary and sufficient conditions for the feasibility of THB/THAB in different cryptographic settings: information theoretic, given existence of key agreement, and given existence of oblivious transfer. Our results show that feasibility can depend on various properties of the graph class, such as connectivity, and highlight the role of different properties of topology when kept hidden, including direction, distance, and/or distance-of-neighbors to the broadcaster. An interesting corollary of our results is a dichotomy for THC with a public number of at least three parties, secure against one corruption: information-theoretic feasibility if all graphs are 2-connected; necessity and sufficiency of key agreement otherwise.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **SAFELearn: Secure Aggregation for private FEderated Learning**
  2021-03-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/386)
  Hossein Fereidooni, Samuel Marchal, Markus Miettinen, Azalia Mirhoseini, Helen Möllering, Thien Duc Nguyen, Phillip Rieger, Ahmad Reza Sadeghi, Thomas Schneider, Hossein Yalame, Shaza Zeitouni

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) is an emerging distributed machine learning paradigm which addresses critical data privacy issues in machine learning by enabling clients, using an aggregation server (aggregator), to jointly train a global model without revealing their training data. Thereby, it improves not only privacy but is also efficient as it uses the computation power and data of potentially millions of clients for training in parallel. However, FL is vulnerable to so-called inference attacks by malicious aggregators which can infer information about clients’ data from their model updates. Secure aggregation restricts the central aggregator to only learn the summation or average of the updates of clients. Unfortunately, existing protocols for secure aggregation for FL suffer from high communication, computation, and many communication rounds. In this work, we present SAFELearn, a generic design for efficient private FL systems that protects against inference attacks that have to analyze individual clients&#x27; model updates using secure aggregation. It is flexibly adaptable to the efficiency and security requirements of various FL applications and can be instantiated with MPC or FHE. In contrast to previous works, we only need 2 rounds of communication in each training iteration, do not use any expensive cryptographic primitives on clients, tolerate dropouts, and do not rely on a trusted third party. We implement and benchmark an instantiation of our generic design with secure two-party computation. Our implementation aggregates 500~models with more than 300K parameters in less than 0.5 seconds.

  匹配依据：MPC: secure two party computation

  </details>

- **Blindly Follow: SITS CRT and FHE for DCLSMPC of DUFSM**
  2021-03-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/410)
  Shlomi Dolev, Stav Doolman

  <details><summary>摘要 / Abstract</summary>

  A Statistical Information Theoretic Secure (SITS) system utilizing the Chinese Remainder Theorem (CRT), coupled with Fully Homomorphic Encryption (FHE) for Distributed Communication-less Secure Multiparty Computation (DCLSMPC) of any Distributed Unknown Finite State Machine (DUFSM) is presented. Namely, secret shares of the input(s) and output(s) are passed to/from the computing parties, while there is no communication between them throughout the computation. We propose a novel approach of transition table representation and polynomial representation for arithmetic circuits evaluation, joined with a CRT secret sharing scheme and FHE to achieve SITS communication-less within computational secure execution of DUFSM. We address the severe limitation of FHE implementation over a single server to cope with a malicious or Byzantine server. We use several distributed memory-efficient solutions that are significantly better than the majority vote in replicated state machines, where each participant maintains an FHE replica. A Distributed Unknown Finite State Machine (DUFSM) is achieved when the transition table is secret shared or when the (possible zero value) coefficients of the polynomial are secret shared, implying communication-less SMPC of an unknown finite state machine.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **A Synergistic Approach to Digital Privacy**
  2021-03-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2103.14783)
  Christopher Gorog

  <details><summary>摘要 / Abstract</summary>

  This paper outlines an approach for IEEE to take leadership for digital privacy to align many existing IEEE Societies and efforts in the areas of computer systems &amp; applications security, organizational &amp; global architectures, policy-supporting legislation, originating new standards, integrating compliance into technologies, and helping design decision-board infrastructures for governance bodies. Much of the current emphasis on evolving privacy technologies centers on big corporate enterprises and institutions, causing the industry to support corporate assets protection mainly. Fostering technology to empower individual privacy-enabling tools has lagged, and personal privacy has diminished because corporate big data applications have made sizable investments into exploiting private data. As one of the largest individual-member-based organizations, IEEE is urged to develop a collaborative approach for digital privacy with privacy-enabling technologies to benefit its members. The recommendations outlined define a prospective course that could result in future global individualized privacy capabilities which employ a combination of synergistic technologies such as distributed ledgers, differential privacy, homomorphic encryption, secure distributed multi-party computation, zero-trust architectures, proof-of-origin of data, software, or other techniques. Such an effort would involve community engagement and outreach, academic peer-review events, the establishment of governance bodies, coordination &amp; expansion of existing standards, and the development of publicly-accessible prototypes. Collaboration with other IEEE-sponsored efforts for transactive energy systems, confidentiality and security of healthcare records and devices, and other IEEE-funded projects will help magnify digital privacy investments already in progress in these applications of emerging technologies.

  匹配依据：MPC: multi party computation

  </details>

- **Secure Platform for Processing Sensitive Data on Shared HPC Systems**
  2021-03-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2103.14679)
  Michel Scheerman, Narges Zarrabi, Martijn Kruiten, Maxime Mogé, Lykle Voort, Annette Langedijk, Ruurd Schoonhoven, Tom Emery

  <details><summary>摘要 / Abstract</summary>

  High performance computing clusters operating in shared and batch mode pose challenges for processing sensitive data. In the meantime, the need for secure processing of sensitive data on HPC system is growing. In this work we present a novel method for creating secure computing environments on traditional multi-tenant high-performance computing clusters. Our platform as a service provides a customizable, virtualized solution using PCOCC and SLURM to meet strict security requirements without modifying the exist-ing HPC infrastructure. We show how this platform has been used in real-world research applications from different research domains. The solution is scalable by design with low performance overhead and can be generalized for processing sensitive data on shared HPC systems imposing high security criteria

  匹配依据：MPC: secure computing

  </details>

- **Additive Tridiagonal Codes over $\\mathbb{F}\_{4}$**
  2021-03-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.05405)
  N. Annamalai, Anandhu Mohan, C. Durairajan

  <details><summary>摘要 / Abstract</summary>

  In this paper, we introduce a additive Tridiagonal and Double-Tridiagonal codes over $\mathbb{F}_4$ and then we study the properties of the code. Also, we find the number of additive Tridiagonal codes over $\mathbb{F}_4.$ Finally, we study the applications of Double-Tridiagonal codes to secret sharing scheme based on matrix projection.

  匹配依据：MPC: secret sharing

  </details>

- **A family of projective two-weight linear codes**
  2021-03-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2103.13633)
  Ziling Heng, Dexiang Li, Jiao Du, Fuling Chen

  <details><summary>摘要 / Abstract</summary>

  Projective two-weight linear codes are closely related to finite projective spaces and strongly regular graphs. In this paper, a family of $q$-ary projective two-weight linear codes is presented, where $q$ is a power of 2. The parameters of both the codes and their duals are excellent. As applications, the codes are used to derive strongly regular graphs with new parameters and secret sharing schemes with interesting access structures.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-preserving Identity Broadcast for Contact Tracing Applications**
  2021-03-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2103.12865)
  Vladimir Dyo, Jahangir Ali

  <details><summary>摘要 / Abstract</summary>

  Wireless Contact tracing has emerged as an important tool for managing the COVID19 pandemic and relies on continuous broadcasting of a person&#x27;s presence using Bluetooth Low Energy beacons. The limitation of current contact tracing systems in that a reception of a single beacon is sufficient to reveal the user identity, potentially exposing users to malicious trackers installed along the roads, passageways, and other infrastructure. In this paper, we propose a method based on Shamir secret sharing algorithm, which lets mobile nodes reveal their identity only after a certain predefined contact duration, remaining invisible to trackers with short or fleeting encounters. Through data-driven evaluation, using a dataset containing 18 million BLE sightings, we show that the method drastically reduces the privacy exposure of users. Finally, we implemented the approach on Android phones to demonstrate its feasibility and measure performance for various network densities.

  匹配依据：MPC: secret sharing

  </details>

- **Multiparty Computation with Covert Security and Public Verifiability**
  2021-03-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/366)
  Peter Scholl, Mark Simkin, Luisa Siniscalchi

  <details><summary>摘要 / Abstract</summary>

  Multiparty computation protocols (MPC) are said to be \emph{secure against covert adversaries} if the honest parties are guaranteed to detect any misbehavior by the malicious parties with a constant probability. Protocols that, upon detecting a cheating attempt, additionally allow the honest parties to compute certificates, which enable third parties to be convinced of the malicious behavior of the accused parties, are called \emph{publicly verifiable}. In this work, we make several contributions to the domain of MPC with security against covert adversaries. We identify a subtle flaw in a protocol of Goyal, Mohassel, and Smith (Eurocrypt 2008) and show how to modify their original construction to obtain security against covert adversaries. We present generic compilers that transform arbitrary passively secure preprocessing protocols, i.e. protocols where the parties have no private inputs, into protocols that are secure against covert adversaries and publicly verifiable. Using our compiler, we construct the first efficient variants of the BMR and the SPDZ protocols that are secure and publicly verifiable against a covert adversary that corrupts all but one party and also construct variants with covert security and identifiable abort. We observe that an existing impossibility result by Ishai, Ostrovsky, and Seyalioglu (TCC 2012) can be used to show that there exist certain functionalities that cannot be realized by parties, that have oracle-access to broadcast and arbitrary two-party functionalities, with information-theoretic security against a covert adversary.

  匹配依据：MPC: multiparty computation

  </details>

- **Construction of minimal linear codes with few weights from weakly regular plateaued functions**
  2021-03-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/371)
  Ahmet Sinak

  <details><summary>摘要 / Abstract</summary>

  The construction of linear (minimal) codes from functions over finite fields has been greatly studied in the literature since determining the parameters of linear codes based on functions is rather easy due to the nice structures of functions. In this paper, we derive 3-weight and 4-weight linear codes from weakly regular plateaued unbalanced functions in the recent construction method of linear codes over the odd characteristic finite fields. The Hamming weights and their weight distributions for proposed codes are determined by using the Walsh transform values and Walsh distribution of the employed functions, respectively. We next derive projective 3-weight punctured codes with good parameters from the constructed codes. These punctured codes may be almost optimal due to the Griesmer bound, and they can be employed to design association schemes. We lastly show that all constructed codes are minimal, which approves that they can be employed to design high democratic secret sharing schemes.

  匹配依据：MPC: secret sharing

  </details>

- **An Efficient Simulation of Quantum Secret Sharing**
  2021-03-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2103.11206)
  Kartick Sutradhar, Hari Om

  <details><summary>摘要 / Abstract</summary>

  In quantum cryptography, quantum secret sharing $(QSS)$ is a fundamental primitive. $QSS$ can be used to create complex and secure multiparty quantum protocols. Existing $QSS$ protocols are either at the $(n, n)$ threshold $2$ level or at the $(t, n)$ threshold $d$ level with a trusted player, where $n$ denotes the number of players and $t$ denotes the threshold number of players. Here, we propose a secure $d$-level $QSS$ protocol for sharing a secret with efficient simulation. This protocol is more secure, flexible, and practical as compared to the existing $QSS$ protocols: $(n, n)$ threshold $2$-level and $(t,n)$ threshold $d$-level with a trusted player. Further, it does not disclose any information about the secret to players. Its security analysis shows that the intercept-resend, intercept, entangle-measure, forgery, collision and collusion attacks are not possible in this protocol.

  匹配依据：MPC: secret sharing

  </details>

- **Zooid: a DSL for Certified Multiparty Computation**
  2021-03-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2103.10269)
  David Castro-Perez, Francisco Ferreira, Lorenzo Gheri, Nobuko Yoshida

  <details><summary>摘要 / Abstract</summary>

  We design and implement Zooid, a domain specific language for certified multiparty communication, embedded in Coq and implemented atop our mechanisation framework of asynchronous multiparty session types (the first of its kind). Zooid provides a fully mechanised metatheory for the semantics of global and local types, and a fully verified end-point process language that faithfully reflects the type-level behaviours and thus inherits the global types properties such as deadlock freedom, protocol compliance, and liveness guarantees.

  匹配依据：MPC: multiparty computation

  </details>

- **Information Leakages in Code-based Masking: A Unified Quantification Approach**
  2021-03-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/363)
  Wei Cheng, Sylvain Guilley, Claude Carlet, Jean-Luc Danger, Sihem Mesnager

  <details><summary>摘要 / Abstract</summary>

  This paper presents a unified approach to quantifying the information leakages in the most general code-based masking schemes. Specifically, by utilizing a uniform representation, we highlight first that all code-based masking schemes&#x27; side-channel resistance can be quantified by an all-in-one framework consisting of two easy-to-compute parameters (the dual distance and the number of conditioned codewords) from a coding-theoretic perspective. In particular, we use signal-to-noise ratio (SNR) and mutual information (MI) as two complementary metrics, where a closed-form expression of SNR and an approximation of MI are proposed by connecting both metrics to the two coding-theoretic parameters. Secondly, considering the connection between Reed-Solomon code and SSS (Shamir&#x27;s Secret Sharing) scheme, the SSS-based masking is viewed as a particular case of generalized code-based masking. Hence as a straightforward application, we evaluate the impact of public points on the side-channel security of SSS-based masking schemes, namely the polynomial masking, and enhance the SSS-based masking by choosing optimal public points for it. Interestingly, we show that given a specific security order, more shares in SSS-based masking leak more information on secrets in an information-theoretic sense. Finally, our approach provides a systematic method for optimizing the side-channel resistance of every code-based masking. More precisely, this approach enables us to select optimal linear codes (parameters) for the generalized code-based masking by choosing appropriate codes according to the two coding-theoretic parameters. Summing up, we provide a best-practice guideline for the application of code-based masking to protect cryptographic implementations.

  匹配依据：MPC: secret sharing

  </details>

- **Efficient permutation protocol for MPC in the head**
  2021-03-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/354)
  Peeter Laud

  <details><summary>摘要 / Abstract</summary>

  The MPC-in-the-head construction (Ishai et al., STOC&#x27;07) give zero-knowledge proofs from secure multiparty computation (MPC) protocols. This paper presents an efficient MPC protocol for permuting a vector of values, making use of the relaxed communication model that can be handled by the MPC-in-the-head construction. Our construction allows more efficient ZK proofs for relations expressed in the Random Access Machine (RAM) model. As a standalone application of our construction, we present batch anonymizable ring signatures.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Round-optimal Honest-majority MPC in Minicrypt and with Everlasting Security**
  2021-03-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/346)
  Benny Applebaum, Eliran Kachlon, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  We study the round complexity of secure multiparty computation (MPC) in the challenging model where full security, including guaranteed output delivery, should be achieved at the presence of an active rushing adversary who corrupts up to half of parties. It is known that 2 rounds are insufficient in this model (Gennaro et al., Crypto 2002), and that 3 round protocols can achieve computational security under public-key assumptions (Gordon et al., Crypto 2015; Ananth et al., Crypto 2018; and Badrinarayanan et al., Asiacrypt 2020). However, despite much effort, it is unknown whether public-key assumptions are inherently needed for such protocols, and whether one can achieve similar results with security against computationally-unbounded adversaries. In this paper, we use Minicrypt-type assumptions to realize 3-round MPC with full and active security. Our protocols come in two flavors: for a small (logarithmic) number of parties $n$, we achieve an optimal resiliency threshold of $t\leq \lfloor (n-1)/2\rfloor$, and for a large (polynomial) number of parties we achieve an almost-optimal resiliency threshold of $t\leq 0.5n(1-\epsilon)$ for an arbitrarily small constant $\epsilon &gt; 0$. Both protocols can be based on sub-exponentially hard injective one-way functions in the plain model. If the parties have an access to a collision resistance hash function, we can derive statistical everlasting security for every NC1 functionality, i.e., the protocol is secure against adversaries that are computationally bounded during the execution of the protocol and become computationally unlimited after the protocol execution. As a secondary contribution, we show that in the strong honest-majority setting ($t&lt;n/3$), every NC1 functionality can be computed in 3 rounds with everlasting security and complexity polynomial in $n$ based on one-way functions. Previously, such a result was only known based on collision-resistance hash function.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Non-interactive distributed key generation and key resharing**
  2021-03-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/339)
  Jens Groth

  <details><summary>摘要 / Abstract</summary>

  We present a non-interactive publicly verifiable secret sharing scheme where a dealer can construct a Shamir secret sharing of a field element and confidentially yet verifiably distribute shares to multiple receivers. We also develop a non-interactive publicly verifiable resharing scheme where existing share holders of a Shamir secret sharing can create a new Shamir secret sharing of the same secret and distribute it to a set of receivers in a confidential, yet verifiable manner. A public key may be associated with the secret being shared in the form of a group element raised to the secret field element. We use our verifiable secret sharing scheme to construct a non-interactive distributed key generation protocol that creates such a public key together with a secret sharing of the discrete logarithm. We also construct a non-interactive distributed resharing protocol that preserves the public key but creates a fresh secret sharing of the secret key and hands it to a set of receivers, which may or may not overlap with the original set of share holders. Our protocols build on a new pairing-based CCA-secure public-key encryption scheme with forward secrecy. As a consequence our protocols can use static public keys for participants but still provide compromise protection. The scheme uses chunked encryption, which comes at a cost, but the cost is offset by a saving gained by our ciphertexts being comprised only of source group elements and no target group elements. A further efficiency saving is obtained in our protocols by extending our single-receiver encryption scheme to a multi-receiver encryption scheme, where the ciphertext is up to a factor 5 smaller than just having single-receiver ciphertexts. The non-interactive key management protocols are deployed on the Internet Computer to facilitate the use of threshold BLS signatures. The protocols provide a simple interface to remotely create secret-shared keys to a set of receivers, to refresh the secret sharing whenever there is a change of key holders, and provide proactive security against mobile adversaries.

  匹配依据：MPC: secret sharing

  </details>

- **MPCAuth: Multi-factor Authentication for Distributed-trust Systems**
  2021-03-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/342)
  Sijun Tan, Weikeng Chen, Ryan Deng, Raluca Ada Popa

  <details><summary>摘要 / Abstract</summary>

  Systems with distributed trust have attracted growing research attention and seen increasing industry adoptions. In these systems, critical secrets are distributed across N servers, and computations are performed privately using secure multi-party computation (SMPC). Authentication for these distributed-trust systems faces two challenges. The first challenge is ease-of-use. Namely, how can an authentication protocol maintain its user experience without sacrificing security? To avoid a central point of attack, a client needs to authenticate to each server separately. However, this would require the client to authenticate N times for each authentication factor, which greatly hampers usability. The second challenge is privacy, as the client’s sensitive profiles are now exposed to all N servers under different trust domains, which creates N times the attack surface for the profile data. We present MPCAuth, a multi-factor authentication system for distributed-trust applications that address both challenges. Our system enables a client to authenticate to N servers independently with the work of only one authentication. In addition, our system is profile hiding, meaning that the client’s authentication profiles such as her email username, phone number, passwords, and biometric features are not revealed unless all servers are compromised. We propose secure and practical protocols for an array of widely adopted authentication factors, including email passcodes, SMS messages, U2F, security questions/passwords, and biometrics. Our system finds practical applications in the space of cryptocurrency custody and collaborative machine learning, and benefits future adoptions of distributed-trust applications.

  匹配依据：MPC: secure multi party computation

  </details>

- **Reusable Two-Round MPC from LPN**
  2021-03-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/316)
  James Bartusek, Sanjam Garg, Akshayaram Srinivasan, Yinuo Zhang

  <details><summary>摘要 / Abstract</summary>

  We present a new construction of maliciously-secure, two-round multiparty computation (MPC) in the CRS model, where the first message is reusable an unbounded number of times. The security of the protocol relies on the Learning Parity with Noise (LPN) assumption with inverse polynomial noise rate 1/n^{1-epsilon} for small enough epsilon, where n is the LPN dimension. Prior works on reusable two-round MPC required assumptions such as DDH or LWE that imply some flavor of homomorphic computation. We obtain our result in two steps: We obtain the first construction of this primitive from an assumption that is not known to support general homomorphic operations. In the first step, we construct a two-round MPC protocol in the silent pre-processing model (Boyle et al., Crypto 2019). Specifically, the parties engage in a computationally inexpensive setup procedure that generates some correlated random strings. Then, the parties commit to their inputs. Finally, each party sends a message depending on the function to be computed, and these messages can be decoded to obtain the output. Crucially, the complexity of the pre-processing phase and the input commitment phase do not grow with the size of the circuit to be computed. We call this multiparty silent NISC, generalizing the notion of two-party silent NISC of Boyle et al. (CCS 2019). We provide a construction of multiparty silent NISC from LPN in the random oracle model. In the second step, we give a transformation that removes the pre-processing phase and use of random oracle from the previous protocol. This transformation additionally adds (unbounded) reusability of the first round message, giving the first construction of reusable two-round MPC from the LPN assumption. This step makes novel use of randomized encoding of circuits (Applebaum et al., FOCS 2004) and a variant of the ``tree of MPC messages&quot; technique of Ananth et al. and Bartusek et al. (TCC 2020).

  匹配依据：MPC: multiparty computation

  </details>

- **Oblivious TLS via Multi-Party Computation**
  2021-03-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/318)
  Damiano Abram, Ivan Damgård, Peter Scholl, Sven Trieflinger

  <details><summary>摘要 / Abstract</summary>

  In this paper, we describe Oblivious TLS: an MPC protocol that we prove UC secure against a majority of actively corrupted parties. The protocol securely implements TLS 1.3. Thus, any party P who runs TLS can communicate securely with a set of servers running Oblivious TLS; P does not need to modify anything, or even be aware that MPC is used. Applications of this include communication between servers who offer MPC services and clients, to allow the clients to easily and securely provide inputs or receive outputs. Also, an organization could use Oblivious TLS to improve in-house security while seamlessly connecting to external parties. Our protocol runs in the preprocessing model, and we did a preliminary non-optimized implementation of the on-line phase. In this version, the hand-shake completes in about 1 second. Performance of the record protocol depends, of course, on the encryption scheme used. We designed an MPC friendly scheme which achieved a throughput of about 300 KB/sec. Based on implementation results from other work, the standard AES-GCM can be expected to be as fast, although our implementation did not do as well.

  匹配依据：MPC: multi party computation

  </details>

- **Multiphoton and side-channel attacks in mistrustful quantum cryptography**
  2021-03-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2103.06970)
  Mathieu Bozzio, Adrien Cavaillès, Eleni Diamanti, Adrian Kent, Damián Pitalúa-García

  <details><summary>摘要 / Abstract</summary>

  Mistrustful cryptography includes important tasks like bit commitment, oblivious transfer, coin flipping, secure computations, position authentication, digital signatures and secure unforgeable tokens. Practical quantum implementations presently use photonic setups. In many such implementations, Alice sends photon pulses encoding quantum states and Bob chooses measurements on these states. In practice, Bob generally uses single photon threshold detectors, which cannot distinguish the number of photons in detected pulses. Also, losses and other imperfections require Bob to report the detected pulses. Thus, malicious Alice can send and track multiphoton pulses and thereby gain information about Bob&#x27;s measurement choices, violating the protocols&#x27; security. Here, we provide a theoretical framework for analysing such multiphoton attacks, and present known and new attacks. We illustrate the power of these attacks with an experiment, and study their application to earlier experimental demonstrations of mistrustful quantum cryptography. We analyse countermeasures based on selective reporting and prove them inadequate. We also discuss side-channel attacks where Alice controls further degrees of freedom or sends other physical systems.

  匹配依据：MPC: oblivious transfer

  </details>

- **MPCCache: Privacy-Preserving Multi-Party Cooperative Cache Sharing at the Edge**
  2021-03-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/317)
  Duong Tung Nguyen, Ni Trieu

  <details><summary>摘要 / Abstract</summary>

  Edge computing and caching have emerged as key technologies in the future communication network to enhance the user experience, reduce backhaul traffic, and enable various Internet of Things applications. Different from conventional resources like CPU and memory that can be utilized by only one party at a time, a cached data item, which can be considered as a public good, can serve multiple parties simultaneously. Therefore, instead of independent caching, it is beneficial for the parties (e.g., Telcos) to cooperate and proactively store their common items in a shared cache that can be accessed by all the parties at the same time. In this work, we present MPCCache, a novel privacy-preserving Multi-party Cooperative Cache sharing framework, which allows multiple network operators to determine a set of common data items with the highest access frequencies to be stored in their capacity-limited shared cache while guaranteeing the privacy of their individual datasets. The technical core of our MPCCache is a new construction that allows multiple parties to compute a specific function on the intersection set of their datasets, without revealing the intersection itself to any party. We evaluate our protocols to demonstrate their practicality and show that MPCCache scales well to large datasets and achieves a few hundred times faster compared to a baseline scheme that optimally combines existing MPC protocols.

  匹配依据：MPC: mpc (context)

  </details>

- **DIMY: Enabling Privacy-preserving Contact Tracing**
  2021-03-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2103.05873)
  Nadeem Ahmed, Regio A. Michelin, Wanli Xue, Guntur Dharma Putra, Sushmita Ruj, Salil S. Kanhere, Sanjay Jha

  <details><summary>摘要 / Abstract</summary>

  The infection rate of COVID-19 and lack of an approved vaccine has forced governments and health authorities to adopt lockdowns, increased testing, and contact tracing to reduce the spread of the virus. Digital contact tracing has become a supplement to the traditional manual contact tracing process. However, although there have been a number of digital contact tracing apps proposed and deployed, these have not been widely adopted owing to apprehensions surrounding privacy and security. In this paper, we propose a blockchain-based privacy-preserving contact tracing protocol, &quot;Did I Meet You&quot; (DIMY), that provides full-lifecycle data privacy protection on the devices themselves as well as on the back-end servers, to address most of the privacy concerns associated with existing protocols. We have employed Bloom filters to provide efficient privacy-preserving storage, and have used the Diffie-Hellman key exchange for secret sharing among the participants. We show that DIMY provides resilience against many well known attacks while introducing negligible overheads. DIMY&#x27;s footprint on the storage space of clients&#x27; devices and back-end servers is also significantly lower than other similar state of the art apps.

  匹配依据：MPC: secret sharing

  </details>

- **The More The Merrier: Reducing the Cost of Large Scale MPC**
  2021-03-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/303)
  S. Dov Gordon, Daniel Starin, Arkady Yerukhimovich

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) allows multiple parties to perform secure joint computations on their private inputs. Today, applications for MPC are growing with thousands of parties wishing to build federated machine learning models or trusted setups for blockchains. To address such scenarios we propose a suite of novel MPC protocols that maximize throughput when run with large numbers of parties. In particular, our protocols have both communication and computation complexity that decrease with the number of parties. Our protocols build on prior protocols based on packed secret-sharing, introducing new techniques to build more efficient computation for general circuits. Specifically, we introduce a new approach for handling linear attacks that arise in protocols using packed secret-sharing and we propose a method for unpacking shared multiplication triples without increasing the asymptotic costs. Compared with prior work, we avoid the $\log |C|$ overhead required when generically compiling circuits of size $|C|$ for use in a SIMD computation, and we improve over folklore ``committee-based&#x27;&#x27; solutions by a factor of $O(s)$, the statistical security parameter. In practice, our protocol is up to $10X$ faster than any known construction, under a reasonable set of parameters.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **A Compressed $\\Sigma$-Protocol Theory for Lattices**
  2021-03-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/307)
  Thomas Attema, Ronald Cramer, Lisa Kohl

  <details><summary>摘要 / Abstract</summary>

  We show a lattice-based solution for commit-and-prove transparent circuit zero-knowledge (ZK) with polylog-communication, the first not depending on PCPs. We start from compressed $\Sigma$-protocol theory (CRYPTO 2020), which is built around basic $\Sigma$-protocols for opening an arbitrary linear form on a long secret vector that is compactly committed to. These protocols are first compressed using a recursive ``folding-technique&#x27;&#x27; adapted from Bulletproofs, at the expense of logarithmic rounds. Proving in ZK that the secret vector satisfies a given constraint -- captured by a circuit -- is then by (blackbox) reduction to the linear case, via arithmetic secret-sharing techniques adapted from MPC. Commit-and-prove is also facilitated, i.e., when commitment(s) to the secret vector are created ahead of any circuit-ZK proof. On several platforms (incl.\ DL) this leads to logarithmic communication. Non-interactive versions follow from Fiat-Shamir. This abstract modular theory strongly suggests that it should somehow be supported by a lattice-platform as well. However, when going through the motions and trying to establish low communication (on an SIS-platform), a certain significant lack in current understanding of multi-round protocols is exposed. Namely, as opposed to the DL-case, the basic $\Sigma$-protocol in question typically has poly-small challenge space. Taking into account the compression-step -- which yields non-constant rounds -- and the necessity for parallelization to reduce error, there is no known tight result that the compound protocol admits an efficient knowledge extractor. We resolve the state of affairs here by a combination of two novel results which are fully general and of independent interest. The first gives a tight analysis of efficient knowledge extraction in case of non-constant rounds combined with poly-small challenge space, whereas the second shows that parallel repetition indeed forces rapid decrease of knowledge error. Moreover, in our present context, arithmetic secret sharing is not defined over a large finite field but over a quotient of a number ring and this forces our careful adaptation of how the linearization techniques are deployed. We develop our protocols in an abstract framework that is conceptually simple and can be flexibly instantiated. In particular, the framework applies to arbitrary rings and norms.

  匹配依据：MPC: secret sharing

  </details>

- **Multiparty Protocol that Usually Shuffles**
  2021-03-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2103.05072)
  Dhaneshwar Mardi, Surbhi Tanwar, Jaydeep Howlader

  <details><summary>摘要 / Abstract</summary>

  Multiparty computation is raising importance because it&#x27;s primary objective is to replace any trusted third party in the distributed computation. This work presents two multiparty shuffling protocols where each party, possesses a private input, agrees on a random permutation while keeping the permutation secret. The proposed shuffling protocols are based on permutation network, thereby data-oblivious. The first proposal is $n\text{-}permute$ that permutes $n$ inputs in all $n!$ possible ways. $n$-permute network consists of $2\log{n}-1$ layers, and in each layer there are $n/2$ gates. Our second protocol is $n_π$-permute shuffling that defines a permutation set $Π=\{π_1,\dots,π_N\}$ where $|Π| &lt; n!$, and the resultant shuffling is a random permutation $π_i \in Π$. The $n_π$-permute network contains leases number of layers compare to $n$-permute network. Let $n=n_1n_2$, the $n_π$-permute network would define $2\log{n_1}-1+\log{n_2}$ layers. \par The proposed shuffling protocols are unconditionally secure against malicious adversary who can corrupt at most $t&lt;n/3$ parties. The probability that adversary can learn the outcome of $n$-permute is upper bound by $((n-t)!)^{-1}$. Whereas, the probability that adversary can learn the outcome of $n_π$-permute is upper bounded by $\big(f_Π(n_1-θ_1)^{n_2}2^{θ_2}\big)^{-1}$, for some positive integer $θ_1, θ_2$, and a recursive definition of $f_Π$. The protocols allow the parties to build quorums, and distribute the load among the quorums.

  匹配依据：MPC: multiparty computation

  </details>

- **Bipartite secret sharing and staircases**
  2021-03-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2103.04904)
  Laszlo Csirmaz, František Matúš, Carles Padró

  <details><summary>摘要 / Abstract</summary>

  Bipartite secret sharing schemes have a bipartite access structure in which the set of participants is divided into two parts and all participants in the same part play an equivalent role. Such a bipartite scheme can be described by a \emph{staircase}: the collection of its minimal points. The complexity of a scheme is the maximal share size relative to the secret size; and the $κ$-complexity of an access structure is the best lower bound provided by the entropy method. An access structure is $κ$-ideal if it has $κ$-complexity 1. Motivated by the abundance of open problems in this area, the main results can be summarized as follows. First, a new characterization of $κ$-ideal multipartite access structures is given which offers a straightforward and simple approach to describe ideal bipartite and tripartite access structures. Second, the $κ$-complexity is determined for a range of bipartite access structures, including those determined by two points, staircases with equal widths and heights, and staircases with all heights 1. Third, matching linear schemes are presented for some non-ideal cases, including staircases where all heights are 1 and all widths are equal. Finally, finding the Shannon complexity of a bipartite access structure can be considered as a discrete submodular optimization problem. An interesting and intriguing continuous version is defined which might give further insight to the large-scale behavior of these optimization problems.

  匹配依据：MPC: secret sharing

  </details>

- **Reactive Key-Loss Protection in Blockchains**
  2021-03-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/289)
  Sam Blackshear, Konstantinos Chalkias, Panagiotis Chatzigiannis, Riyaz Faizullabhoy, Irakliy Khaburzaniya, Eleftherios Kokoris Kogias, Joshua Lind, David Wong, Tim Zakian

  <details><summary>摘要 / Abstract</summary>

  We present a novel approach for blockchain asset owners to reclaim their funds in case of accidental private-key loss or transfer to a mistyped address. Our solution can be deployed upon failure or absence of proactively implemented backup mechanisms, such as secret sharing and cold storage. The main advantages against previous proposals is it does not require any prior action from users and works with both single-key and multi-sig accounts. We achieve this by a 3-phase Commit() -&gt; Reveal() -&gt; Claim() - or - Challenge() smart contract that enables accessing funds of addresses for which the spending key is not available. We provide an analysis of the threat and incentive models and formalize the concept of reactive KEy-Loss Protection (KELP).

  匹配依据：MPC: secret sharing

  </details>

- **P2DEX: Privacy-Preserving Decentralized Cryptocurrency Exchange**
  2021-03-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/283)
  Carsten Baum, Bernardo David, Tore Frederiksen

  <details><summary>摘要 / Abstract</summary>

  Cryptocurrency exchange services are either trusted central entities that have been routinely hacked (losing over 8 billion USD), or decentralized services that make all orders public before they are settled. The latter allows market participants to ``front run&#x27;&#x27; each other, an illegal operation in most jurisdictions. We extend the ``Insured MPC&#x27;&#x27; approach of Baum et al. (FC 2020) to construct an efficient universally composable privacy preserving decentralized exchange where a set of servers run private cross-chain exchange order matching in an outsourced manner, while being financially incentivised to behave honestly. Our protocol allows for exchanging assets over multiple public ledgers, given that users have access to a ledger that supports standard public smart contracts. If parties behave honestly, the on-chain complexity of our construction is as low as that of performing the transactions necessary for a centralized exchange. In case malicious behavior is detected, users are automatically refunded by malicious servers at low cost. Thus, an actively corrupted majority can only mount a denial-of-service attack that makes exchanges fail, in which case the servers are publicly identified and punished, while honest clients do not to lose their funds. For the first time in this line of research, we report experimental results on the MPC building block, showing the approach is efficient enough to be used in practice.

  匹配依据：MPC: mpc (context)

  </details>

- **Privacy-preserving Analytics for Data Markets using MPC**
  2021-03-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2103.03739)
  Karl Koch, Stephan Krenn, Donato Pellegrino, Sebastian Ramacher

  <details><summary>摘要 / Abstract</summary>

  Data markets have the potential to foster new data-driven applications and help growing data-driven businesses. When building and deploying such markets in practice, regulations such as the European Union&#x27;s General Data Protection Regulation (GDPR) impose constraints and restrictions on these markets especially when dealing with personal or privacy-sensitive data. In this paper, we present a candidate architecture for a privacy-preserving personal data market, relying on cryptographic primitives such as multi-party computation (MPC) capable of performing privacy-preserving computations on the data. Besides specifying the architecture of such a data market, we also present a privacy-risk analysis of the market following the LINDDUN methodology.

  匹配依据：MPC: multi party computation

  </details>

- **Network Consensus with Privacy: A Secret Sharing Method**
  2021-03-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2103.03432)
  Silun Zhang, Thomas Ohlson Timoudas, Munther Dahleh

  <details><summary>摘要 / Abstract</summary>

  In this work, inspired by secret sharing schemes, we introduce a privacy-preserving approach for network consensus, by which all nodes in a network can reach an agreement on their states without exposing the individual state to neighbors. With the privacy degree defined for the agents, the proposed method makes the network resistant to the collusion of any given number of neighbors, and protects the consensus procedure from communication eavesdropping. Unlike existing works, the proposed privacy-preserving algorithm is resilient to node failures. When a node fails, the method offers the possibility of rebuilding the lost node via the information kept in its neighbors, even though none of the neighbors knows the exact state of the failing node. Moreover, it is shown that the proposed method can achieve consensus and average consensus almost surely, when the agents have arbitrary privacy degrees and a common privacy degree, respectively. To illustrate the theory, two numerical examples are presented.

  匹配依据：MPC: secret sharing

  </details>

- **More Communication Lower Bounds for Information-Theoretic MPC**
  2021-03-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/278)
  Ivan Damgård, Boyang Li, Nikolaj I. Schwartzbach

  <details><summary>摘要 / Abstract</summary>

  We prove two classes of lower bounds on the communication complexity of information-theoretically secure multiparty computation. The first lower bound applies to perfect passive secure multiparty computation, in the standard model with $n=2t+1$ parties of which $t$ are corrupted. We show a lower bound that applies to secure evaluation of any function, assuming that each party can choose to learn to learn or not learn the output. Specifically, we show that there is a function $H^*$ such that for any protocol that evaluates $y_i=b_i \cdot f(x_1,...,x_n)$ with perfect passive security (where $b_i$ is a private boolean input), the total communication must be at least $\frac{1}{2} \sum_{i=1}^n H_f^*(x_i)$ bits of information. The second lower bound applies to the perfect maliciously secure setting with $n=3t+1$ parties. We show that for any $n$ and all large enough $S$, there exists a reactive functionality $F_S$ taking an $S$-bit string as input (and with short output) such that any protocol implementing $F_S$ with perfect malicious security must communicate $\Omega(nS)$ bits. Since the functionalities we study can be implemented with linear size circuits, the result can equivalently be stated as follows: for any $n$ and all large enough $g \in \mathbb{N}$ there exists a reactive functionality $F_C$ doing computation specified by a Boolean circuit $C$ with $g$ gates, where any perfectly secure protocol implementing $F_C$ must communicate $\Omega(n g)$ bits. The results easily extends to constructing similar functionalities defined over any fixed finite field. Using known techniques, we also show an upper bound that matches the lower bound up to a constant factor (existing upper bounds are a factor $\log n$ off for Boolean circuits). Both results also extend to the case where the threshold $t$ is suboptimal. Namely if $n=kt+s$ the bound is weakened by a factor $O(s)$, which corresponds to known optimizations via packed secret-sharing.

  匹配依据：MPC: secret sharing, secure evaluation, secure multiparty computation

  </details>

- **VOLE-PSI: Fast OPRF and Circuit-PSI from Vector-OLE**
  2021-03-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/266)
  Peter Rindal, Phillipp Schoppmann

  <details><summary>摘要 / Abstract</summary>

  In this work we present a new construction for a batched Oblivious Pseudorandom Function (OPRF) based on Vector-OLE and the PaXoS data structure. We then use it in the standard transformation for achieving Private Set Intersection (PSI) from an OPRF. Our overall construction is highly efficient with $O(n)$ communication and computation. We demonstrate that our protocol can achieve malicious security at only a very small overhead compared to the semi-honest variant. For input sizes $n = 2^{20}$, our malicious protocol needs 6.2 seconds and less than 59 MB communication. This corresponds to under 450 bits per element, which is the lowest number for any published PSI protocol (semi-honest or malicious) to date. Moreover, in theory our semi-honest (resp. malicious) protocol can achieve as low as 219 (resp. 260) bits per element for $n=2^{20}$ at the added cost of interpolating a polynomial over $n$ elements. As a second contribution, we present an extension where the output of the PSI is secret-shared between the two parties. This functionality is generally referred to as Circuit-PSI. It allows the parties to perform a subsequent MPC protocol on the secret-shared outputs, e.g., train a machine learning model. Our circuit PSI protocol builds on our OPRF construction along with another application of the PaXoS data structure. It achieves semi-honest security and allows for a highly efficient implementation, up to 3x faster than previous work.

  匹配依据：MPC: private set intersection

  </details>

- **Improved single-round secure multiplication using regenerating codes**
  2021-03-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/253)
  Mark Abspoel, Ronald Cramer, Daniel Escudero, Ivan Damgård, Chaoping Xing

  <details><summary>摘要 / Abstract</summary>

  In 2016, Guruswami and Wootters showed Shamir&#x27;s secret-sharing scheme defined over an extension field has a regenerating property. Namely, we can compress each share to an element of the base field by applying a linear form, such that the secret is determined by a linear combination of the compressed shares. Immediately it seemed like an application to improve the complexity of unconditionally secure multiparty computation must be imminent; however, thus far, no result has been published. We present the first application of regenerating codes to MPC, and show that its utility lies in reducing the number of rounds. Concretely, we present a protocol that obliviously evaluates a depth-$d$ arithmetic circuit in $d + O(1)$ rounds, in the amortized setting of parallel evaluations, with $o(n^2)$ ring elements communicated per multiplication. Our protocol is secure against the maximal adversary corrupting $t &lt; n/2$ parties. All existing approaches in this setting have complexity $\Omega(n^2)$. Moreover, we extend some of the theory on regenerating codes to Galois rings. It was already known that the repair property of MDS codes over fields can be fully characterized in terms of its dual code. We show this characterization extends to linear codes over Galois rings, and use it to show the result of Guruswami and Wootters also holds true for Shamir&#x27;s scheme over Galois rings.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Gage MPC: Bypassing Residual Function Leakage for Non-Interactive MPC**
  2021-03-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/256)
  Ghada Almashaqbeh, Fabrice Benhamouda, Seungwook Han, Daniel Jaroslawicz, Tal Malkin, Alex Nicita, Tal Rabin, Abhishek Shah, Eran Tromer

  <details><summary>摘要 / Abstract</summary>

  Existing models for non-interactive MPC cannot provide full privacy for inputs, because they inherently leak the residual function (i.e., the output of the function on the honest parties’ input together with all possible values of the adversarial inputs). For example, in any non-interactive sealed-bid auction, the last bidder can figure out what was the highest previous bid. We present a new MPC model which avoids this privacy leak. To achieve this, we utilize a blockchain in a novel way, incorporating smart contracts and arbitrary parties that can be incentivized to perform computation (“bounty hunters,” akin to miners). Security is maintained under a monetary assumption about the parties: an honest party can temporarily supply a recoverable collateral of value higher than the computational cost an adversary can expend. We thus construct non-interactive MPC protocols with strong security guarantees (full security, no residual leakage) in the short term. Over time, as the adversary can invest more and more computational resources, the security guarantee decays. Thus, our model, which we call Gage MPC, is suitable for secure computation with limited-time secrecy, such as auctions. A key ingredient in our protocols is a primitive we call “Gage Time Capsules” (GaTC): a time capsule that allows a party to commit to a value that others are able to reveal but only at a designated computational cost. A GaTC allows a party to commit to a value together with a monetary collateral. If the original party properly opens the GaTC, it can recover the collateral. Otherwise, the collateral is used to incentivize bounty hunters to open the GaTC. This primitive is used to ensure completion of Gage MPC protocols on the desired inputs. As a requisite tool (of independent interest), we present a generalization of garbled circuit that are more robust: they can tolerate exposure of extra input labels. This is in contrast to Yao’s garbled circuits, whose secrecy breaks down if even a single extra label is exposed. Finally, we present a proof-of-concept implementation of a special case of our construction, yielding an auction functionality over an Ethereum-like blockchain.

  匹配依据：MPC: garbled circuit, garbled circuits, secure computation

  </details>

- **Ciminion: Symmetric Encryption Based on Toffoli-Gates over Large Finite Fields**
  2021-03-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/267)
  Christoph Dobraunig, Lorenzo Grassi, Anna Guinet, Daniël Kuijsters

  <details><summary>摘要 / Abstract</summary>

  Motivated by new applications such as secure Multi-Party Computation (MPC), Fully Homomorphic Encryption (FHE), and Zero-Knowledge proofs (ZK), the need for symmetric encryption schemes that minimize the number of field multiplications in their natural algorithmic description is apparent. This development has brought forward many dedicated symmetric encryption schemes that minimize the number of multiplications in GF(2^n) or GF(p), with p being prime. These novel schemes have lead to new cryptanalytic insights that have broken many of said schemes. Interestingly, to the best of our knowledge, all of the newly proposed schemes that minimize the number of multiplications use those multiplications exclusively in S-boxes based on a power mapping that is typically x^3 or x^{-1}. Furthermore, most of those schemes rely on complex and resource-intensive linear layers to achieve a low multiplication count. In this paper, we present Ciminion, an encryption scheme minimizing the number of field multiplications in large binary or prime fields, while using a very lightweight linear layer. In contrast to other schemes that aim to minimize field multiplications in GF(2^n) or GF(p), Ciminion relies on the Toffoli gate to improve the non-linear diffusion of the overall design. In addition, we have tailored the primitive for the use in a Farfalle-like construction in order to minimize the number of rounds of the used primitive, and hence, the number of field multiplications as far as possible.

  匹配依据：MPC: secure multi party computation

  </details>

- **The Capacity Region of Distributed Multi-User Secret Sharing**
  2021-03-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2103.01568)
  Ali Khalesi, Mahtab Mirmohseni, Mohammad Ali Maddah-Ali

  <details><summary>摘要 / Abstract</summary>

  In this paper, we study the problem of distributed multi-user secret sharing, including a trusted master node, $N\in \mathbb{N}$ storage nodes, and $K$ users, where each user has access to the contents of a subset of storage nodes. Each user has an independent secret message with certain rate, defined as the size of the message normalized by the size of a storage node. Having access to the secret messages, the trusted master node places encoded shares in the storage nodes, such that (i) each user can recover its own message from the content of the storage nodes that it has access to, (ii) each user cannot gain any information about the message of any other user. We characterize the capacity region of the distributed multi-user secret sharing, defined as the set of all achievable rate tuples, subject to the correctness and privacy constraints. In the achievable scheme, for each user, the master node forms a polynomial with the degree equal to the number of its accessible storage nodes minus one, where the value of this polynomial at certain points are stored as the encoded shares. The message of that user is embedded in some of the coefficients of the polynomial. The remaining coefficients are determined such that the content of each storage node serves as the encoded shares for all users that have access to that storage node.

  匹配依据：MPC: secret sharing

  </details>

- **Private Set Operations from Oblivious Switching**
  2021-03-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/243)
  Gayathri Garimella, Payman Mohassel, Mike Rosulek, Saeed Sadeghian, Jaspal Singh

  <details><summary>摘要 / Abstract</summary>

  Private set intersection reveals the intersection of two private sets, but many real-world applications require the parties to learn $\textit{only}$ partial information about the intersection. In this paper we introduce a new approach for computing arbitrary functions of the intersection, provided that it is safe to also reveal the cardinality of the intersection. In the most general case, our new protocol provides the participants with secret shares of the intersection, which can be fed into any generic 2PC protocol. Certain computations on the intersection can also be done even more directly and efficiently, avoiding this secret-sharing step. These cases include computing only the cardinality of intersection, or the ``cardinality-sum&#x27;&#x27; application proposed in Ion et al. (ePrint 2017). Compared to the state-of-the-art protocol for computing on intersection (Pinkas et al., Eurocrypt 2019), our protocol has about $2.5-3\times$ less communication, and has faster running time on slower (50Mbps) networks. Our new techniques can also be used to privately compute the {\em union} of two sets as easily as computing the intersection. Our protocol concretely improves the leading private set union protocol (Kolesnikov et al., Asiacrypt 2020) by a factor of $2-2.5\times$, depending on the network speed. We then show how private set union can be used in a simple way to realize the ``Private-ID&#x27;&#x27; functionality suggested by Buddhavarapu et al.~(ePrint 2020). Our protocol is significantly faster than the prior Private-ID protocol, especially on fast networks. All of our protocols are in the two-party setting and are secure against semi-honest adversaries.

  匹配依据：MPC: private set intersection, private set union, secret sharing

  </details>

- **Everlasting UC Commitments from Fully Malicious PUFs**
  2021-03-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/248)
  Bernardo Magri, Giulio Malavolta, Dominique Schröder, Dominique Unruh

  <details><summary>摘要 / Abstract</summary>

  Everlasting security models the setting where hardness assumptions hold during the execution of a protocol but may get broken in the future. Due to the strength of this adversarial model, achieving any meaningful security guarantees for composable protocols is impossible without relying on hardware assumptions (Müller-Quade and Unruh, JoC&#x27;10). For this reason, a rich line of research has tried to leverage physical assumptions to construct well-known everlasting cryptographic primitives, such as commitment schemes. The only known everlastingly UC secure commitment scheme, due to Müller-Quade and Unruh (JoC&#x27;10), assumes honestly generated hardware tokens. The authors leave the possibility of constructing everlastingly UC secure commitments from malicious hardware tokens as an open problem. Goyal et al. (Crypto&#x27;10) constructs unconditionally UC-secure commitments and secure computation from malicious hardware tokens, with the caveat that the honest tokens must encapsulate other tokens. This extra restriction rules out interesting classes of hardware tokens, such as physically uncloneable functions (PUFs). In this work we present the first construction of an everlastingly UC-secure commitment scheme in the fully malicious token model without requiring honest token encapsulation. Our scheme assumes the existence of PUFs and is secure in the common reference string model. We also show that our results are tight by giving an impossibility proof for everlasting UC-secure computation from non-erasable tokens (such as PUFs), even with trusted setup.

  匹配依据：MPC: secure computation

  </details>

- **Secure Poisson Regression**
  2021-03-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/208)
  Mahimna Kelkar, Phi Hung Le, Mariana Raykova, Karn Seth

  <details><summary>摘要 / Abstract</summary>

  We introduce the first construction for secure two-party computation of Poisson regression, which enables two parties who hold shares of the input samples to learn only the resulting Poisson model while protecting the privacy of the inputs. Our construction relies on new protocols for secure fixed-point exponentiation and correlated matrix multiplications. Our secure exponentiation construction avoids expensive bit decomposition and achieves orders of magnitude improvement in both online and offline costs over state of the art works. As a result, the dominant cost for our secure Poisson regression are matrix multiplications with one fixed matrix. We introduce a new technique, called correlated Beaver triples, which enables many such multiplications at the cost of roughly one matrix multiplication. This further brings down the cost of secure Poisson regression. We implement our constructions and show their extreme efficiency. In a LAN setting, our secure exponentiation for 20-bit fractional precision takes less than 0.07ms with a batch-size of 100,000. One iteration of secure Poisson regression on a dataset with 10,000 samples with 1000 binary features needs about 65.82s in the offline phase, 55.14s in the online phase and 17MB total communication. For several real datasets this translates into training that takes seconds and only a couple of MB communication.

  匹配依据：MPC: secure two party computation

  </details>

- **PASSAT: Single Password Authenticated Secret-Shared Intrusion-Tolerant Storage with Server Transparency**
  2021-02-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2102.13607)
  Kiavash Satvat, Maliheh Shirvanian, Nitesh Saxena

  <details><summary>摘要 / Abstract</summary>

  In this paper, we introduce PASSAT, a practical system to boost the security assurance delivered by the current cloud architecture without requiring any changes or cooperation from the cloud service providers. PASSAT is an application transparent to the cloud servers that allows users to securely and efficiently store and access their files stored on public cloud storage based on a single master password. Using a fast and light-weight XOR secret sharing scheme, PASSAT secret-shares users&#x27; files and distributes them among n publicly available cloud platforms. To access the files, PASSAT communicates with any k out of n cloud platforms to receive the shares and runs a secret-sharing reconstruction algorithm to recover the files. An attacker (insider or outsider) who compromises or colludes with less than k platforms cannot learn the user&#x27;s files or modify the files stealthily. To authenticate the user to multiple cloud platforms, PASSAT crucially stores the authentication credentials, specific to each platform on a password manager, protected under the user&#x27;s master password. Upon requesting access to files, the user enters the password to unlock the vault and fetches the authentication tokens using which PASSAT can interact with cloud storage. Our instantiation of PASSAT based on (2, 3)-XOR secret sharing of Kurihara et al., implemented with three popular storage providers, namely, Google Drive, Box, and Dropbox, confirms that our approach can efficiently enhance the confidentiality, integrity, and availability of the stored files with no changes on the servers.

  匹配依据：MPC: secret sharing

  </details>

- **Emerging Trends in Federated Learning: From Model Fusion to Federated X Learning**
  2021-02-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2102.12920)
  Shaoxiong Ji, Yue Tan, Teemu Saravirta, Zhiqin Yang, Yixin Liu, Lauri Vasankari, Shirui Pan, Guodong Long, Anwar Walid

  <details><summary>摘要 / Abstract</summary>

  Federated learning is a new learning paradigm that decouples data collection and model training via multi-party computation and model aggregation. As a flexible learning setting, federated learning has the potential to integrate with other learning frameworks. We conduct a focused survey of federated learning in conjunction with other learning algorithms. Specifically, we explore various learning algorithms to improve the vanilla federated averaging algorithm and review model fusion methods such as adaptive aggregation, regularization, clustered methods, and Bayesian methods. Following the emerging trends, we also discuss federated learning in the intersection with other learning paradigms, termed federated X learning, where X includes multitask learning, meta-learning, transfer learning, unsupervised learning, and reinforcement learning. In addition to reviewing state-of-the-art studies, this paper also identifies key challenges and applications in this field, while also highlighting promising future directions.

  匹配依据：MPC: multi party computation

  </details>

- **Delegating Multi-Party Quantum Computations vs. Dishonest Majority in Two Quantum Rounds**
  2021-02-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2102.12949)
  Theodoros Kapourniotis, Elham Kashefi, Luka Music, Harold Ollivier

  <details><summary>摘要 / Abstract</summary>

  Multi-Party Quantum Computation (MPQC) has attracted a lot of attention as a potential killer-app for quantum networks through it&#x27;s ability to preserve privacy and integrity of the highly valuable computations they would enable. Contributing to the latest challenges in this field, we present a composable protocol achieving blindness and verifiability even in the case of a single honest client. The security of our protocol is reduced, in an information-theoretically secure way, to that of a classical composable Secure Multi-Party Computation (SMPC) used to coordinate the various parties. Our scheme thus provides a statistically secure upgrade of such classical scheme to a quantum one with the same level of security. In addition, (i) the clients can delegate their computation to a powerful fully fault-tolerant server and only need to perform single qubit operations to unlock the full potential of multi-party quantum computation; (ii) the amount of quantum communication with the server is reduced to sending quantum states at the beginning of the computation and receiving the output states at the end, which is optimal and removes the need for interactive quantum communication; and (iii) it has a low constant multiplicative qubit overhead compared to the single-client delegated protocol it is built upon. The main technical ingredient of our paper is the bootstraping of the MPQC construction by Double Blind Quantum Computation, a new composable resource for blind multiparty quantum computation, that demonstrates the surprising fact that the full protocol does not require verifiability of all components to achieve security.

  匹配依据：MPC: secure multi party computation

  </details>

- **Manticore: Efficient Framework for Scalable Secure Multiparty Computation Protocols**
  2021-02-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/200)
  Sergiu Carpov, Kevin Deforth, Nicolas Gama, Mariya Georgieva, Dimitar Jetchev, Jonathan Katz, Iraklis Leontiadis, M. Mohammadi, Abson Sae-Tang, Marius Vuille

  <details><summary>摘要 / Abstract</summary>

  We propose a novel MPC framework, Manticore, in the multiparty setting, with full threshold and semi-honest security model, supporting a combination of real number arithmetic (arithmetic shares), Boolean arithmetic (Boolean shares) and garbled circuits (Yao shares). In contrast to prior work [MZ17, MR18], Manticore never overflows, an important feature for machine learning applications. It achieves this without compromising efficiency or security. Compared to other overflow-free recent techniques such as MP-SPDZ [EGKRS20] that convert arithmetic to Boolean shares, we introduce a novel highly efficient modular lifting/truncation method that stays in the arithmetic domain. We revisit some of the basic MPC operations such as real-valued polynomial evaluation, division, logarithm, exponential and comparison by employing our modular lift in combination with existing efficient conversions between arithmetic, Boolean and Yao shares. Furthermore, we provide a highly efficient and scalable implementation supporting logistic regression models with real-world training data sizes and high numerical precision through PCA and blockwise variants (for memory and runtime optimizations). On a dataset of 50 million rows and 50 columns distributed among two players, it completes in one day with at least 10 decimal digits of precision.Our logistic regression solution placed first at Track 3 of the annual iDASH’2020 Competition. Finally, we mention a novel oblivious sorting algorithm built using Manticore.

  匹配依据：MPC: garbled circuits, secure multiparty computation

  </details>

- **Decidability of Secure Non-interactive Simulation of Doubly Symmetric Binary Source**
  2021-02-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/190)
  Hamidreza Amini Khorasgani, Hemanta K. Maji, Hai H. Nguyen

  <details><summary>摘要 / Abstract</summary>

  Noise, which cannot be eliminated or controlled by parties, is an incredible facilitator of cryptography. For example, highly efficient secure computation protocols based on independent samples from the doubly symmetric binary source (BSS) are known. A modular technique of extending these protocols to diverse forms of other noise without any loss of round and communication complexity is the following strategy. Parties, beginning with multiple samples from an arbitrary noise source, non-interactively, albeit securely, simulate the BSS samples. After that, they can use custom-designed efficient multi-party solutions using these BSS samples. Khorasgani, Maji, and Nguyen (EPRINT--2020) introduce the notion of secure non-interactive simulation (SNIS) as a natural cryptographic extension of concepts like non-interactive simulation and non-interactive correlation distillation in theoretical computer science and information theory. In SNIS, the parties apply local reduction functions to their samples to produce samples of another distribution. This work studies the decidability problem of whether samples from the noise $(X,Y)$ can securely and non-interactively simulate BSS samples. As is standard in analyzing non-interactive simulations, our work relies on Fourier-analytic techniques to approach this decidability problem. Our work begins by algebraizing the simulation-based security definition of SNIS. Using this algebraized definition of security, we analyze the properties of the Fourier spectrum of the reduction functions. Given $(X,Y)$ and BSS with noise parameter $\epsilon$, the objective is to distinguish between the following two cases. (A) Does there exist a SNIS from $BSS(\epsilon)$ to $(X,Y)$ with $\delta$-insecurity? (B) Do all SNIS from $BSS(\epsilon)$ to $(X,Y)$ incur $\delta&#x27;$-insecurity, where $\delta&#x27;&gt;\delta$? We prove that there is a bounded computable time algorithm achieving this objective for the following cases. (1) $\delta=O{1/n}$ and $\delta&#x27;=$ positive constant, and (2) $\delta=$ positive constant, and $\delta&#x27;=$ another (larger) positive constant. We also prove that $\delta=0$ is achievable only when $(X,Y)$ is another BSS, where $(X,Y)$ is an arbitrary distribution over $\{-1,1\}\times\{-1,1\}$. Furthermore, given $(X,Y)$, we provide a sufficient test determining if simulating BSS samples incurs a constant-insecurity, irrespective of the number of samples of $(X,Y)$. Handling the security of the reductions in Fourier analysis presents unique challenges because the interaction of these analytical techniques with security is unexplored. Our technical approach diverges significantly from existing approaches to the decidability problem of (insecure) non-interactive reductions to develop analysis pathways that preserve security. Consequently, our work shows a new concentration of the Fourier spectrum of secure reduction functions, unlike their insecure counterparts. We show that nearly the entire weight of secure reduction functions&#x27; spectrum is concentrated on the lower-degree components. The authors believe that examining existing analytical techniques through the facet of security and developing new analysis methodologies respecting security is of independent and broader interest.

  匹配依据：MPC: secure computation

  </details>

- **Compilation of Function Representations for Secure Computing Paradigms**
  2021-02-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/195)
  Karim Baghery, Cyprien Delpech de Saint Guilhem, Emmanuela Orsini, Nigel P. Smart, Titouan Tanguy

  <details><summary>摘要 / Abstract</summary>

  This paper introduces M-Circuits, a program representation which generalizes arithmetic and binary circuits. This new representation is motivated by the way modern multi-party computation (MPC) systems based on linear secret sharing schemes actually operate. We then show how this representation also allows one to construct zero knowledge proof (ZKP) systems based on the MPC-in-the-head paradigm. The use of the M-Circuit program abstraction then allows for a number of program-specific optimizations to be applied generically. It also allows to separate complexity and security optimizations for program compilation from those for application protocols (MPC or ZKP).

  匹配依据：MPC: multi party computation, secret sharing, secure computing

  </details>

- **PRICURE: Privacy-Preserving Collaborative Inference in a Multi-Party Setting**
  2021-02-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2102.09751)
  Ismat Jarin, Birhanu Eshete

  <details><summary>摘要 / Abstract</summary>

  When multiple parties that deal with private data aim for a collaborative prediction task such as medical image classification, they are often constrained by data protection regulations and lack of trust among collaborating parties. If done in a privacy-preserving manner, predictive analytics can benefit from the collective prediction capability of multiple parties holding complementary datasets on the same machine learning task. This paper presents PRICURE, a system that combines complementary strengths of secure multi-party computation (SMPC) and differential privacy (DP) to enable privacy-preserving collaborative prediction among multiple model owners. SMPC enables secret-sharing of private models and client inputs with non-colluding secure servers to compute predictions without leaking model parameters and inputs. DP masks true prediction results via noisy aggregation so as to deter a semi-honest client who may mount membership inference attacks. We evaluate PRICURE on neural networks across four datasets including benchmark medical image classification datasets. Our results suggest PRICURE guarantees privacy for tens of model owners and clients with acceptable accuracy loss. We also show that DP reduces membership inference attack exposure without hurting accuracy.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **ppAURORA: Privacy Preserving Area Under Receiver Operating Characteristic and Precision-Recall Curves**
  2021-02-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2102.08788)
  Ali Burak Ünal, Nico Pfeifer, Mete Akgün

  <details><summary>摘要 / Abstract</summary>

  Computing an AUC as a performance measure to compare the quality of different machine learning models is one of the final steps of many research projects. Many of these methods are trained on privacy-sensitive data and there are several different approaches like $ε$-differential privacy, federated machine learning and cryptography if the datasets cannot be shared or used jointly at one place for training and/or testing. In this setting, it can also be a problem to compute the global AUC, since the labels might also contain privacy-sensitive information. There have been approaches based on $ε$-differential privacy to address this problem, but to the best of our knowledge, no exact privacy preserving solution has been introduced. In this paper, we propose an MPC-based solution, called ppAURORA, with private merging of individually sorted lists from multiple sources to compute the exact AUC as one could obtain on the pooled original test samples. With ppAURORA, the computation of the exact area under precision-recall and receiver operating characteristic curves is possible even when ties between prediction confidence values exist. We use ppAURORA to evaluate two different models predicting acute myeloid leukemia therapy response and heart disease, respectively. We also assess its scalability via synthetic data experiments. All these experiments show that we efficiently and privately compute the exact same AUC with both evaluation metrics as one can obtain on the pooled test samples in plaintext according to the semi-honest adversary setting.

  匹配依据：MPC: mpc (context)

  </details>

- **hbACSS: How to Robustly Share Many Secrets**
  2021-02-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/159)
  Thomas Yurek, Licheng Luo, Jaiden Fairoze, Aniket Kate, Andrew Miller

  <details><summary>摘要 / Abstract</summary>

  Despite significant recent progress toward making multi-party computation (MPC) practical, no existing MPC library offers complete robustness---meaning guaranteed output delivery, including in the offline phase---in a network that even has intermittent delays. Importantly, several theoretical MPC constructions already ensure robustness in this setting. We observe that the key reason for this gap between theory and practice is the absence of efficient verifiable/complete secret sharing (VSS/CSS) constructions; existing CSS protocols either require a) challenging broadcast channels in practice or b) introducing computation and communication overhead that is at least quadratic in the number of players. This work presents hbACSS, a suite of optimal-resilience asynchronous complete secret sharing protocols that are (quasi)linear in both computation and communication overhead. Towards developing hbACSS, we develop hbPolyCommit, an efficient polynomial commitment scheme that is (quasi)linear (in the polynomial degree) in terms of computation and communication overhead without requiring a trusted setup. We implement our hbACSS protocols, extensively analyze their practicality, and observe that our protocols scale well with an increasing number of parties. In particular, we use hbACSS to generate MPC input masks: a useful primitive which had previously only been calculated nonrobustly in practice.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Efficient Linear Multiparty PSI and Extensions to Circuit/Quorum PSI**
  2021-02-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/172)
  Nishanth Chandran, Nishka Dasgupta, Divya Gupta, Sai Lakshmi Bhavana Obbattu, Sruthi Sekar, Akash Shah

  <details><summary>摘要 / Abstract</summary>

  Multiparty Private Set Intersection (mPSI), enables $n$ parties, each holding private sets (each of size $m$) to compute the intersection of these private sets, without revealing any other information to each other. While several protocols for this task are known, the only concretely efficient protocol is due to the work of Kolesnikov et al. (KMPRT, CCS 2017), who gave a semi-honest secure protocol with communication complexity $\mathcal{O}(nmt\lambda)$, where $t&lt;n$ is the number of corrupt parties and $\lambda$ is the security parameter. In this work, we make the following contributions: $-$ First, for the natural adversarial setting of semi-honest honest majority (i.e. $t&lt;n/2$), we asymptotically improve upon the above result and provide a concretely efficient protocol with total communication of $\mathcal{O}(nm\lambda)$. $-$ Second, concretely, our protocol has $6(t+2)/5$ times lesser communication than KMPRT and is upto $5\times$ and $6.2\times$ faster than KMPRT in the LAN and WAN setting even for 15 parties. $-$ Finally, we introduce and consider two important variants of mPSI - circuit PSI (that allows the parties to compute a function over the intersection set without revealing the intersection itself) and quorum PSI (that allows $P_1$ to learn all the elements in his/her set that are present in at least $k$ other sets) and provide concretely efficient protocols for these variants.

  匹配依据：MPC: private set intersection

  </details>

- **CNF-FSS and its Applications**
  2021-02-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/163)
  Paul Bunn, Eyal Kushilevitz, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  Function Secret Sharing (FSS), introduced by Boyle, Gilboa and Ishai [BGI15], extends the classical notion of secret-sharing a *value* to secret sharing a *function*. Namely, for a secret function f (from a class $F$), FSS provides a sharing of f whereby *succinct shares (``keys&#x27;&#x27;) are distributed to a set of parties, so that later the parties can non-interactively compute an additive sharing of f(x), for any input x in the domain of f. Previous work on FSS concentrated mostly on the two-party case, where highly efficient schemes are obtained for some simple, yet extremely useful, classes $F$ (in particular, FSS for the class of point functions, a task referred to as DPF -- Distributed Point Functions [GI14,BGI15]. In this paper, we concentrate on the multi-party case, with p &gt;= 3 parties and t-security (1 1 (semi-honest) corruptions. For example, we build a 2-out-of-5 secure (standard) DPF scheme of communication complexity O(N^{1/4}), where N is the domain size of f (compared with the current best-known of O(N^{1/2}) for (2,5)-DPF). More generally, with p &gt; d*t parties, we give a (t,p)-DPF whose complexity grows as O(N^{1/2d}) (rather than O(\sqrt{N}) that follows from the (p-1,p)-DPF scheme of [BGI15]). We also present a 1-out-of-3 secure CNF-DPF scheme, in which each party holds two of the three keys, with poly-logarithmic communication complexity. These results have immediate implications to scenarios where (multi-server) DPF was shown to be applicable. For example, we show how to use such a scheme to obtain asymptotic improvement (O(\log^2N) versus O(\sqrt{N})) in communication complexity over the 3-party protocol of [BKKO20].

  匹配依据：MPC: secret sharing

  </details>

- **Multiparty Mediated Quantum Secret Sharing Protocol**
  2021-02-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2102.06846)
  Chia-Wei Tsai, Chun-Wei Yang, Jason Lin

  <details><summary>摘要 / Abstract</summary>

  This study proposes a multiparty mediated quantum secret sharing (MQSS) protocol that allows n restricted quantum users to share a secret via the assistance of a dishonest third-party (TP) with full quantum capabilities. Under the premise that a restricted quantum user can only perform the Hadamard transformation and the Z-basis measurement, the proposed MQSS protocol has addressed two common challenges in the existing semi-quantum secret sharing protocols: (1) the dealer must have full quantum capability, and (2) the classical users must equip with the wavelength quantum filter and the photon number splitters (PNS) to detect the Trojan horse attacks. The security analysis has also delivered proof to show that the proposed MQSS protocol can avoid the collective attack, the collusion attack, and the Trojan horse attacks. In addition, the proposed MQSS protocol is more efficient than the existing SQSS protocols due to the restricted quantum users can only equip with two quantum operations, and the qubits are transmitted within a shorter distance.

  匹配依据：MPC: secret sharing

  </details>

- **Securely Computing Piecewise Constant Codes**
  2021-02-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/146)
  Benjamin E. Diamond

  <details><summary>摘要 / Abstract</summary>

  Piecewise constant codes form an expressive and well-understood class of codes. In this work, we show that many piecewise constant codes admit exact coverings by polynomial-cardinality collections of hyperplanes. We prove that any boolean function whose &quot;on-set&quot; has been covered in just this manner can be evaluated by two parties with malicious security. This represents an interesting connection between covering codes, affine-linear algebra over prime fields, and secure computation. We observe that many natural boolean functions&#x27; on-sets admit expressions as piecewise constant codes (and hence can be computed securely). Our protocol supports secure computation on committed inputs; we describe applications in blockchains and credentials. We finally present an efficient implementation of our protocol.

  匹配依据：MPC: secure computation

  </details>

- **On Sufficient Oracles for Secure Computation with Identifiable Abort**
  2021-02-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/151)
  Mark Simkin, Luisa Siniscalchi, Sophia Yakoubov

  <details><summary>摘要 / Abstract</summary>

  Identifiable abort is the strongest security guarantee that is achievable for secure multi-party computation in the dishonest majority setting. Protocols that achieve this level of security ensure that, in case of an abort, all honest parties agree on the identity of at least one corrupt party who can be held accountable for the abort. It is important to understand what computational primitives must be used to obtain secure computation with identifiable abort. This can be approached by asking which oracles can be used to build perfectly secure computation with identifiable abort. Ishai, Ostrovsky, and Zikas (Crypto 2014) show that an oracle that returns correlated randomness to all $n$ parties is sufficient; however, they leave open the question of whether oracles that return output to fewer than $n$ parties can be used. In this work, we show that for $t \leq n - 2$ corruptions, oracles that return output to $n - 1$ parties are sufficient to obtain information-theoretically secure computation with identifiable abort. Using our construction recursively, we see that for $t \leq n - \ell - 2$ and $\ell \in \mathcal{O}(1)$, oracles that return output to $n - \ell - 1$ parties are sufficient. For our construction, we introduce a new kind of secret sharing scheme which we call unanimously identifiable secret sharing with public and private shares (UISSwPPS). In a UISSwPPS scheme, each share holder is given a public and a private shares. Only the public shares are necessary for reconstruction, and the knowledge of a private share additionally enables the identification of at least one party who provided an incorrect share in case reconstruction fails. The important new property of UISSwPPS is that, even given all the public shares, an adversary should not be able to come up with a different public share that causes reconstruction of an incorrect message, or that avoids the identification of a cheater if reconstruction fails.

  匹配依据：MPC: secret sharing, secure computation, secure multi party computation

  </details>

- **IPDL: A Simple Framework for Formally Verifying Distributed Cryptographic Protocols**
  2021-02-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/147) · [Code](https://github.com/ipdl/ipdl)
  Greg Morrisett, Elaine Shi, Kristina Sojakova, Xiong Fan, Joshua Gancher

  <details><summary>摘要 / Abstract</summary>

  Although there have been many successes in verifying proofs of non-interactive cryptographic primitives such as encryption and signatures, formal verification of interactive cryptographic protocols is still a nascent area. While in principle, it seems possible to extend general frameworks such as Easycrypt to encode proofs for more complex, interactive protocols, a big challenge is whether the human effort would be scalable enough for proof mechanization to eventually acquire mainstream usage among the cryptography community. We work towards closing this gap by introducing a simple framework, Interactive Probabilistic Dependency Logic (IPDL), for reasoning about a certain well-behaved subset of cryptographic protocols. A primary design goal of IPDL is for formal cryptographic proofs to resemble their on-paper counterparts. To this end, IPDL includes an equational logic to reason about approximate observational equivalence (i.e., computational indistinguishability) properties between protocols. IPDL adopts a channel-centric core logic, which decomposes the behavior of the protocol into the behaviors along each communication channel. IPDL supports straight-line programs with statically bounded loops. This design allows us to capture a broad class of protocols encountered in the cryptography literature, including multi-party, reactive, and/or inductively-defined protocols; meanwhile, the logic can track the runtime of the computational reduction in security proofs, thus ensuring computational soundness. We demonstrate the use of IPDL by a number of case studies, including a multi-use, secure message communication protocol, a multi-party coin toss with abort protocol, several oblivious transfer constructions, as well as the two-party GMW protocol for securely evaluating general circuits. We provide a mechanization of the IPDL proof system and our case studies in Coq, and our code is open sourced at https://github.com/ipdl/ipdl.

  匹配依据：MPC: oblivious transfer

  </details>

- **CaPC Learning: Confidential and Private Collaborative Learning**
  2021-02-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2102.05188)
  Christopher A. Choquette-Choo, Natalie Dullerud, Adam Dziedzic, Yunxiang Zhang, Somesh Jha, Nicolas Papernot, Xiao Wang

  <details><summary>摘要 / Abstract</summary>

  Machine learning benefits from large training datasets, which may not always be possible to collect by any single entity, especially when using privacy-sensitive data. In many contexts, such as healthcare and finance, separate parties may wish to collaborate and learn from each other&#x27;s data but are prevented from doing so due to privacy regulations. Some regulations prevent explicit sharing of data between parties by joining datasets in a central location (confidentiality). Others also limit implicit sharing of data, e.g., through model predictions (privacy). There is currently no method that enables machine learning in such a setting, where both confidentiality and privacy need to be preserved, to prevent both explicit and implicit sharing of data. Federated learning only provides confidentiality, not privacy, since gradients shared still contain private information. Differentially private learning assumes unreasonably large datasets. Furthermore, both of these learning paradigms produce a central model whose architecture was previously agreed upon by all parties rather than enabling collaborative learning where each party learns and improves their own local model. We introduce Confidential and Private Collaborative (CaPC) learning, the first method provably achieving both confidentiality and privacy in a collaborative setting. We leverage secure multi-party computation (MPC), homomorphic encryption (HE), and other techniques in combination with privately aggregated teacher models. We demonstrate how CaPC allows participants to collaborate without having to explicitly join their training sets or train a central model. Each party is able to improve the accuracy and fairness of their model, even in settings where each party has a model that performs well on their own dataset or when datasets are not IID and model architectures are heterogeneous across parties.

  匹配依据：MPC: secure multi party computation

  </details>

- **Privacy-Preserving Video Classification with Convolutional Neural Networks**
  2021-02-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2102.03513) · [IACR ePrint](https://eprint.iacr.org/2021/131)
  Sikha Pentyala, Rafael Dowsley, Martine De Cock

  <details><summary>摘要 / Abstract</summary>

  Many video classification applications require access to personal data, thereby posing an invasive security risk to the users&#x27; privacy. We propose a privacy-preserving implementation of single-frame method based video classification with convolutional neural networks that allows a party to infer a label from a video without necessitating the video owner to disclose their video to other entities in an unencrypted manner. Similarly, our approach removes the requirement of the classifier owner from revealing their model parameters to outside entities in plaintext. To this end, we combine existing Secure Multi-Party Computation (MPC) protocols for private image classification with our novel MPC protocols for oblivious single-frame selection and secure label aggregation across frames. The result is an end-to-end privacy-preserving video classification pipeline. We evaluate our proposed solution in an application for private human emotion recognition. Our results across a variety of security settings, spanning honest and dishonest majority configurations of the computing parties, and for both passive and active adversaries, demonstrate that videos can be classified with state-of-the-art accuracy, and without leaking sensitive user information.

  匹配依据：MPC: secure multi party computation

  </details>

- **Rabbit: Efficient Comparison for Secure Multi-Party Computation**
  2021-02-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/119)
  Eleftheria Makri, Dragos Rotaru, Frederik Vercauteren, Sameer Wagh

  <details><summary>摘要 / Abstract</summary>

  Secure comparison has been a fundamental challenge in privacy-preserving computation, since its inception as the Yao&#x27;s millionaires&#x27; problem (FOCS 1982). In this work, we present a novel construction for general n-party private comparison, secure against an active adversary, in the dishonest majority setting. For the case of comparisons over fields, our protocol is more efficient than the best prior work (edaBits: Crypto 2020), with ~1.5x better throughput in most adversarial settings, over 2.3x better throughput in particular in the passive, honest majority setting, and lower communication. Our comparisons crucially eliminate the need for bounded inputs as well as the need for statistical security that prior works require. An important consequence of removing this &quot;slack&quot; (a gap between the bit-length of the input and the MPC representation) is that multi-party computation (MPC) protocols can be run in a field of smaller size, reducing the overhead incurred by privacy-preserving computations. We achieve this novel construction using the commutative nature of addition over rings and fields. This makes the protocol both simple to implement and highly efficient and we provide an implementation in MP-SPDZ (CCS 2020).

  匹配依据：MPC: multi party computation, secure multi party computation

  </details>

- **PSImple: Practical Multiparty Maliciously-Secure Private Set Intersection**
  2021-02-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/122)
  Aner Ben Efraim, Olga Nissenbaum, Eran Omri, Anat Paskin-Cherniavsky

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) protocols allow a set of mutually distrustful parties, each holding a private set of items, to compute the intersection over all their sets, such that no other information is revealed. PSI has a wide variety of applications including online advertising (e.g., efficacy computation), security (e.g., botnet detection, intrusion detection), proximity testing (e.g., COVID-19 contact tracing), and more. Private set intersection is a rapidly developing area and there exist many highly efficient protocols. However, almost all of these protocols are for the case of two parties or for semi-honest security. In particular, despite the high interest in this problem, prior to our work there has been no concretely efficient, maliciously secure multiparty PSI protocol. We present PSImple, the first concretely efficient maliciously-secure multiparty PSI protocol. Our construction is based on oblivious transfer and garbled Bloom filters. To demonstrate the practicality of the PSImple protocol, we implemented the protocol and ran experiments with up to $32$ parties and $2^{20}$ inputs. We show that PSImple is competitive even with the state-of-the-art concretely efficient semi-honest multiparty PSI protocols. Additionally, we revisit the garbled Bloom filter parameters used in the 2-party PSI protocol of Rindal and Rosulek (Eurocrypt 2017). Using a more careful analysis, we show that the size of the garbled Bloom filters and the number of oblivious transfers required for malicious security can be significantly reduced, often by more than $20\%$. These improved parameters can be used both in the 2-party PSI protocol of Rindal and Rosulek and in PSImple.

  匹配依据：MPC: oblivious transfer, private set intersection

  </details>

- **High-Threshold AVSS with Optimal Communication Complexity**
  2021-02-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/118)
  Nicolas Alhaddad, Mayank Varia, Haibin Zhang

  <details><summary>摘要 / Abstract</summary>

  Asynchronous verifiable secret sharing (AVSS) protocols protect a secret that is distributed among N parties. Dual-threshold AVSS protocols guarantee consensus in the presence of T Byzantine failures and privacy if fewer than P parties attempt to reconstruct the secret. In this work, we construct a dual-threshold AVSS protocol that is optimal along several dimensions. First, it is a high-threshold AVSS scheme, meaning that it is a dual-threshold AVSS with optimal parameters T &lt; N/3 and P &lt; N - T. Second, it has O(N^2) message complexity, and for large secrets it achieves the optimal O(N) communication overhead, without the need for a public key infrastructure or trusted setup. While these properties have been achieved individually before, to our knowledge this is the first protocol that is achieves all of the above simultaneously. The core component of our construction is a high-threshold AVSS scheme for small secrets based on polynomial commitments that achieves O(N^2 log(N)) communication overhead, as compared to prior schemes that require O(N^3) overhead with T&lt;N/4 Byzantine failures or O(N^4) overhead for the recent high-threshold protocol of Kokoris-Kogias et al (CCS 2020). Using standard amortization techniques based on erasure coding, we can reduce the communication complexity to O(N*|F|) for a large secret F.

  匹配依据：MPC: secret sharing

  </details>

- **Secrecy: Secure collaborative analytics on secret-shared data**
  2021-02-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2102.01048)
  John Liagouris, Vasiliki Kalavri, Muhammad Faisal, Mayank Varia

  <details><summary>摘要 / Abstract</summary>

  We present a relational MPC framework for secure collaborative analytics on private data with no information leakage. Our work targets challenging use cases where data owners may not have private resources to participate in the computation, thus, they need to securely outsource the data analysis to untrusted third parties. We define a set of oblivious operators, explain the secure primitives they rely on, and analyze their costs in terms of operations and inter-party communication. We show how these operators can be composed to form end-to-end oblivious queries, and we introduce logical and physical optimizations that dramatically reduce the space and communication requirements during query execution, in some cases from quadratic to linear or from linear to logarithmic with respect to the cardinality of the input. We implement our framework on top of replicated secret sharing in a system called Secrecy and evaluate it using real queries from several MPC application areas. Our experiments demonstrate that the proposed optimizations can result in over 1000x lower execution times compared to baseline approaches, enabling Secrecy to outperform state-of-the-art frameworks and compute MPC queries on millions of input rows with a single thread per party.

  匹配依据：MPC: secret sharing

  </details>

- **On Secure Distributed Linearly Separable Computation**
  2021-02-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2102.00926)
  Kai Wan, Hua Sun, Mingyue Ji, Giuseppe Caire

  <details><summary>摘要 / Abstract</summary>

  Distributed linearly separable computation, where a user asks some distributed servers to compute a linearly separable function, was recently formulated by the same authors and aims to alleviate the bottlenecks of stragglers and communication cost in distributed computation. For this purpose, the data center assigns a subset of input datasets to each server, and each server computes some coded packets on the assigned datasets, which are then sent to the user. The user should recover the task function from the answers of a subset of servers, such the effect of stragglers could be tolerated. In this paper, we formulate a novel secure framework for this distributed linearly separable computation, where we aim to let the user only retrieve the desired task function without obtaining any other information about the input datasets, even if it receives the answers of all servers. In order to preserve the security of the input datasets, some common randomness variable independent of the datasets should be introduced into the transmission. We show that any non-secure linear-coding based computing scheme for the original distributed linearly separable computation problem, can be made secure without increasing the communication cost. Then we focus on the case where the computation cost of each server is minimum and aim to minimize the size of the randomness variable introduced in the system while achieving the optimal communication cost. We first propose an information theoretic converse bound on the randomness size. We then propose secure computing schemes based on two well-known data assignments, namely fractional repetition assignment and cyclic assignment. We then propose a computing scheme with novel assignment, which strictly outperforms the above two schemes. Some additional optimality results are also obtained.

  匹配依据：MPC: secure computing

  </details>

- **Improvement of Secure Multi-Party Multiplication of (k,n) Threshold Secret Sharing Using Only N=k Servers (Revised Version)**
  2021-02-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/113)
  Ahmad Akmal Aminuddin Mohd Kamal, Keiichi Iwamura

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) allows a set of n servers to jointly compute an arbitrary function of their inputs, without revealing these inputs to each other. A (k,n) threshold secret sharing is a protocol in which a single secret is divided into n shares and the secret can be recovered from a threshold k shares. Typically, multiplication of (k,n) secret sharing will result in increase of polynomial degree from k-1 to 2k-2, thus increasing the number of shares required from k to 2k-1. Since each server typically hold only one share, the number of servers required in MPC will also increase from k to 2k-1. Therefore, a set of n servers can compute multiplication securely if the adversary corrupts at most k-1&lt;n/2 of the servers. In this paper, we differentiate the number of servers N required and parameter n of (k,n) secret sharing scheme, and propose a method of computing (k-1) sharing of multiplication ab by using only N=k servers. By allowing each server to hold two shares, we realize MPC of multiplication with the setting of N=k,n≥2k-1. We also show that our proposed method is information theoretic secure against a semi-honest adversary.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Genuine entanglement, distillability and quantum information masking under noise**
  2021-02-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2102.00673)
  Mengyao Hu, Lin Chen

  <details><summary>摘要 / Abstract</summary>

  Genuineness and distillability of entanglement play a key role in quantum information tasks, and they are easily disturbed by the noise. We construct a family of multipartite states without genuine entanglement and distillability sudden death across every bipartition, respectively. They are realized by establishing the noise as the multipartite high dimensional Pauli channels. Further, we construct a locally unitary channel as another noise such that the multipartite Greenberger-Horne-Zeilinger state becomes the D{ü}r&#x27;s multipartite state. We also show that the quantum information masking still works under the noise we constructed, and thus show a novel quantum secret sharing scheme under noise. The evolution of a family of three-qutrit genuinely entangled states distillable across every bipartition under noise is also investigated.

  匹配依据：MPC: secret sharing

  </details>

- **A Decentralized and Encrypted National Gun Registry**
  2021-02-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/107)
  Seny Kamara, Tarik Moataz, Andrew Park, Lucy Qin

  <details><summary>摘要 / Abstract</summary>

  Gun violence results in a significant number of deaths in the United States. Starting in the 1960’s, the US Congress passed a series of gun control laws to regulate the sale and use of firearms. One of the most important but politically fraught gun control measures is a national gun registry. A US Senate office is currently drafting legislation that proposes the creation of a voluntary national gun registration system. At a high level, the bill envisions a decentralized system where local county officials would control and manage the registration data of their constituents. These local databases could then be queried by other officials and law enforcement to trace guns. Due to the sensitive nature of this data, however, these databases should guarantee the confidentiality of the data. In this work, we translate the high-level vision of the proposed legislation into technical requirements and design a cryptographic protocol that meets them. Roughly speaking, the protocol can be viewed as a decentralized system of locally-managed end-to-end encrypted databases. Our design relies on various cryptographic building blocks including structured encryption, secure multi-party computation and secret sharing. We propose a formal security definition and prove that our design meets it. We implemented our protocol and evaluated its performance empirically at the scale it would have to run if it were deployed in the United States. Our results show that a decentralized and end-to-end encrypted national gun registry is not only possible in theory but feasible in practice.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **A Quantum Interpretation of Bunched Logic for Quantum Separation Logic**
  2021-01-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2102.00329)
  Li Zhou, Gilles Barthe, Justin Hsu, Mingsheng Ying, Nengkun Yu

  <details><summary>摘要 / Abstract</summary>

  We propose a model of the substructural logic of Bunched Implications (BI) that is suitable for reasoning about quantum states. In our model, the separating conjunction of BI describes separable quantum states. We develop a program logic where pre- and post-conditions are BI formulas describing quantum states -- the program logic can be seen as a counterpart of separation logic for imperative quantum programs. We exercise the logic for proving the security of quantum one-time pad and secret sharing, and we show how the program logic can be used to discover a flaw in Google Cirq&#x27;s tutorial on the Variational Quantum Algorithm (VQA).

  匹配依据：MPC: secret sharing

  </details>

- **Theory of Communication Efficient Quantum Secret Sharing**
  2021-01-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2101.12419)
  Kaushik Senthoor, Pradeep Kiran Sarvepalli

  <details><summary>摘要 / Abstract</summary>

  A $((k,n))$ quantum threshold secret sharing (QTS) scheme is a quantum cryptographic protocol for sharing a quantum secret among $n$ parties such that the secret can be recovered by any $k$ or more parties while $k-1$ or fewer parties have no information about the secret. Despite extensive research on these schemes, there has been very little study on optimizing the quantum communication cost during recovery. Recently, we initiated the study of communication efficient quantum threshold secret sharing (CE-QTS) schemes. These schemes reduce the communication complexity in QTS schemes by accessing $d\geq k$ parties for recovery; here $d$ is fixed ahead of encoding the secret. In contrast to the standard QTS schemes which require $k$ qudits for recovering each qudit in the secret, these schemes have a lower communication cost of $\frac{d}{d-k+1}$ for $d&gt;k$. In this paper, we further develop the theory of communication efficient quantum threshold schemes. Here, we propose universal CE-QTS schemes which reduce the communication cost for all $d\geq k$ simultaneously. We provide a framework based on ramp quantum secret sharing to construct CE-QTS and universal CE-QTS schemes. We give another construction for universal CE-QTS schemes based on Staircase codes. We derived a lower bound on communication complexity and show that our constructions are optimal. Finally, an information theoretic model is developed to analyse CE-QTS schemes and the lower bound on communication complexity is proved again using this model.

  匹配依据：MPC: secret sharing

  </details>

- **Beyond traditional assumptions in fair machine learning**
  2021-01-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2101.12476)
  Niki Kilbertus

  <details><summary>摘要 / Abstract</summary>

  This thesis scrutinizes common assumptions underlying traditional machine learning approaches to fairness in consequential decision making. After challenging the validity of these assumptions in real-world applications, we propose ways to move forward when they are violated. First, we show that group fairness criteria purely based on statistical properties of observed data are fundamentally limited. Revisiting this limitation from a causal viewpoint we develop a more versatile conceptual framework, causal fairness criteria, and first algorithms to achieve them. We also provide tools to analyze how sensitive a believed-to-be causally fair algorithm is to misspecifications of the causal graph. Second, we overcome the assumption that sensitive data is readily available in practice. To this end we devise protocols based on secure multi-party computation to train, validate, and contest fair decision algorithms without requiring users to disclose their sensitive data or decision makers to disclose their models. Finally, we also accommodate the fact that outcome labels are often only observed when a certain decision has been made. We suggest a paradigm shift away from training predictive models towards directly learning decisions to relax the traditional assumption that labels can always be recorded. The main contribution of this thesis is the development of theoretically substantiated and practically feasible methods to move research on fair machine learning closer to real-world applications.

  匹配依据：MPC: secure multi party computation

  </details>

- **Security, Fault Tolerance, and Communication Complexity in Distributed Systems**
  2021-01-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2101.12143)
  Donald Rozinak Beaver

  <details><summary>摘要 / Abstract</summary>

  We present efficient and practical algorithms for a large, distributed system of processors to achieve reliable computations in a secure manner. Specifically, we address the problem of computing a general function of several private inputs distributed among the processors of a network, while ensuring the correctness of the results and the privacy of the inputs, despite accidental or malicious faults in the system. [...] Our algorithms maintain a low cost in local processing time, are the first to achieve optimal levels of fault-tolerance, and most importantly, have low communication complexity. In contrast to the best known previous methods, which require large numbers of rounds even for fairly simple computations, we devise protocols that use small messages and a constant number of rounds regardless of the complexity of the function to be computed. Through direct algebraic approaches, we separate the communication complexity of secure computing from the computational complexity of the function to be computed. We examine security under both the modern approach of computational complexity-based cryptography and the classical approach of unconditional, information-theoretic security. We [...] support formal proofs of claims to security, addressing an important deficiency in the literature. Our protocols are provably secure. In the realm of information-theoretic security, we characterize those functions which two parties can compute jointly with absolute privacy. We also characterize those functions which a weak processor can compute using the aid of powerful processors without having to reveal the instances of the problem it would like to solve. Our methods include a promising new technique called a locally random reduction, which has given rise not only to efficient solutions for many of the problems considered in this work but to several powerful new results in complexity theory.

  匹配依据：MPC: secure computing

  </details>

- **S++: A Fast and Deployable Secure-Computation Framework for Privacy-Preserving Neural Network Training**
  2021-01-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2101.12078)
  Prashanthi Ramachandran, Shivam Agarwal, Arup Mondal, Aastha Shah, Debayan Gupta

  <details><summary>摘要 / Abstract</summary>

  We introduce S++, a simple, robust, and deployable framework for training a neural network (NN) using private data from multiple sources, using secret-shared secure function evaluation. In short, consider a virtual third party to whom every data-holder sends their inputs, and which computes the neural network: in our case, this virtual third party is actually a set of servers which individually learn nothing, even with a malicious (but non-colluding) adversary. Previous work in this area has been limited to just one specific activation function: ReLU, rendering the approach impractical for many use-cases. For the first time, we provide fast and verifiable protocols for all common activation functions and optimize them for running in a secret-shared manner. The ability to quickly, verifiably, and robustly compute exponentiation, softmax, sigmoid, etc., allows us to use previously written NNs without modification, vastly reducing developer effort and complexity of code. In recent times, ReLU has been found to converge much faster and be more computationally efficient as compared to non-linear functions like sigmoid or tanh. However, we argue that it would be remiss not to extend the mechanism to non-linear functions such as the logistic sigmoid, tanh, and softmax that are fundamental due to their ability to express outputs as probabilities and their universal approximation property. Their contribution in RNNs and a few recent advancements also makes them more relevant.

  匹配依据：MPC: secure computation, secure function evaluation

  </details>

- **SPURT: Scalable Distributed Randomness Beacon with Transparent Setup**
  2021-01-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/100)
  Sourav Das, Vinith Krishnan, Irene Miriam Isaac, Ling Ren

  <details><summary>摘要 / Abstract</summary>

  Having shared access to high-quality random numbers is essential in many important applications. Yet, existing constructions of distributed random beacons still have limitations such as imperfect security guarantees, strong setup or network assumptions, or high costs. In this paper, we present SPURT, an efficient distributed randomness beacon protocol that does not require any trusted or expensive setup and is secure against a malicious adversary that controls up to one-third of the nodes in a partially synchronous network. We formally prove that each output of SPURT is unpredictable, bias-resistant, and publicly verifiable. SPURT has an amortized total communication cost of $O(\lambda n^2)$ per beacon output where $\lambda$ is the security parameter. While designing SPURT, we also design a publicly verifiable secret sharing (PVSS) scheme whose security is based on the standard Decisional Bilinear Diffie-Hellman assumption and does not require a Random Oracle. We implement SPURT and evaluate it using a network of up to 128 nodes running in geographically distributed AWS instances. Our evaluation shows that SPURT can produce about 84 beacon outputs per minute in a network of 32 nodes and is comparable to systems with stronger assumptions or weaker security.

  匹配依据：MPC: secret sharing

  </details>

- **Private Stream Aggregation from Labeled Secret Sharing Schemes**
  2021-01-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/081)
  Hendrik Waldner, Tilen Marc, Miha Stopar, Michel Abdalla

  <details><summary>摘要 / Abstract</summary>

  The concept of private stream aggregation (PSA) has been proposed by Shi et al. (NDSS 2011) to allow for data analysis in a privacy-preserving manner. In this work, we introduce the notion of labeled secret sharing (LaSS) schemes and show how to use it to construct PSA schemes. We also show how to realize LaSS using pseudorandom functions or alternatively with a hash function modeled as a random oracle and how it can be used to construct PSA schemes. Additionally, we revisit the security model of Becker et al. (NDSS 2018) and describe stronger security notions for PSA. We then present additional constructions achieving the stronger security notions by relying on recent results on multi-client functional encryption. For all of our constructions, we present implementations to show their practicality and the performance gains over existing solutions.

  匹配依据：MPC: secret sharing

  </details>

- **Grades of Trust in Multiparty Computation**
  2021-01-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/082)
  Jaskaran V. Singh, Nicholas Hopper

  <details><summary>摘要 / Abstract</summary>

  Secure Multiparty Computation involves a protocol between parties with an aim to produce a computed result just as a trusted party would produce if the parties provided their inputs to it. The trusted party in conventional computation is replaced with &quot;un-trusted&quot; parties in Secure Multiparty Computation. We first show that this existing binary definition of trust is inadequate. Real world is rife with disparities, that which produce a perceivable trust gradient between the participants. Conventional MPC models do not take this into account and rather provide security guarantees based on the thresholds of the number of corrupted parties. The thresholds are supposed to cover for some of the parties turning out to be corrupt. Often, with the knowledge of prior probability of a party being corrupt, we can do better if we allot weight to each party based on how trusted we perceive it to be. Our paper explores this idea and our contributions towards it are three folds. First, we introduce the Graded Trust model where each party essentially has a &quot;trust grade&quot; assigned to it in the protocol based on the prior of it being corrupt. Second, we present a method for protocol translation and execution by by simulating players. Lastly, we present a discussion on the philosophy behind graded trust, and the potential benefits for large scale public MPC systems.

  匹配依据：MPC: multiparty computation, secure multiparty computation

  </details>

- **Equivalence of Non-Perfect Secret Sharing and Symmetric Private Information Retrieval with General Access Structure**
  2021-01-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2101.11194)
  Seunghoan Song, Masahito Hayashi

  <details><summary>摘要 / Abstract</summary>

  We study the equivalence between non-perfect secret sharing (NSS) and symmetric private information retrieval (SPIR) with arbitrary response and collusion patterns. NSS and SPIR are defined with an access structure, which corresponds to the authorized/forbidden sets for NSS and the response/collusion patterns for SPIR. We prove the equivalence between NSS and SPIR in the following two senses. 1) Given any SPIR protocol with an access structure, an NSS protocol is constructed with the same access structure and the same rate. 2) Given any linear NSS protocol with an access structure, a linear SPIR protocol is constructed with the same access structure and the same rate. We prove the first relation even if the SPIR protocol has imperfect correctness and secrecy. From the first relation, we derive an upper bound of the SPIR capacity for arbitrary response and collusion patterns. For the special case of $\mathsf{n}$-server SPIR with $\mathsf{r}$ responsive and $\mathsf{t}$ colluding servers, this upper bound proves that the SPIR capacity is $(\mathsf{r}-\mathsf{t})/\mathsf{n}$. From the second relation, we prove that a SPIR protocol exists for any response and collusion patterns.

  匹配依据：MPC: secret sharing

  </details>

- **Collusion-Deterrent Threshold Information Escrow**
  2021-01-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/095)
  Easwar Vivek Mangipudi, Donghang Lu, Alexandros Psomas, Aniket Kate

  <details><summary>摘要 / Abstract</summary>

  An information escrow (IE) service allows its users to encrypt a message such that the message is unlocked only when a user-specified condition is satisfied. Its instantiations include timed-release encryption and allegation escrows with applications ranging from e-auctions to the #metoo movement. The proposed IE systems typically employ threshold cryptography towards mitigating the single-point-of-failure problem. Here, a set of escrow agents securely realize the IE functionality as long as a threshold or more agents behave honestly. Nevertheless, these threshold information escrow (TIE) protocols are vulnerable to premature and undetectable unlocking of messages through collusion among rational agents offering the IE service. This work presents a provably secure TIE scheme in the mixed-behavior model consisting of rational and malicious escrow agents.; any collusion attempt among the agents towards premature decryption results in penalization through a loss of (crypto-)currency and getting banned from the system. The proposed collusion-deterrent escrow (CDE) scheme introduces a novel incentive-penalty mechanism among the agents to stay honest until the user-specified decryption condition is met. In particular, each agent makes a cryptocurrency deposit before the start of the protocol instance such that the deposit amount is returned to the agent when the user-specified condition is met or can be transferred by anyone who holds a secret key corresponding to a public key associated with the instance. Using a novel combination of oblivious transfer, robust bit watermarking, and secure multi-party computation, CDE ensures that whenever the agents collude to decrypt the user data prematurely, one or more whistle-blower agents can withdraw/transfer the deposits of all other agents, thereby penalizing them. We model collusion as a game induced among rational agents offering the CDE service and show that the agents do not collude at equilibrium in game-theoretic terms. We also present a prototype implementation of the CDE protocol and demonstrate its efficiency towards use in practice. While this work does not aim to solve the collusion problem fully, it significantly raises the bar for collusion. It offers an important step towards weakening the strong non-collusion assumption pervasive across multi-party computation applications.

  匹配依据：MPC: multi party computation, oblivious transfer, secure multi party computation

  </details>

- **Personal Data Access Control Through Distributed Authorization**
  2021-01-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2101.10464)
  Mirko Zichichi, Stefano Ferretti, Gabriele D'Angelo, Víctor Rodríguez-Doncel

  <details><summary>摘要 / Abstract</summary>

  This paper presents an architecture of a Personal Information Management System, in which individuals can define the access to their personal data by means of smart contracts. These smart contracts, running on the Ethereum blockchain, implement access control lists and grant immutability, traceability and verifiability of the references to personal data, which is stored itself in a (possibly distributed) file system. A distributed authorization mechanism is devised, where trust from multiple network nodes is necessary to grant the access to the data. To this aim, two possible alternatives are described: a Secret Sharing scheme and Threshold Proxy Re-Encryption scheme. The performance of these alternatives is experimentally compared in terms of execution time. Threshold Proxy Re-Encryption appears to be faster in different scenarios, in particular when increasing message size, number of nodes and the threshold value, i.e. number of nodes needed to grant the data disclosure.

  匹配依据：MPC: secret sharing

  </details>

- **Short Secret Sharing Using Repeatable Random Sequence Generators**
  2021-01-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2101.09317)
  Arvind Srinivasan, Chien-Chung Chan

  <details><summary>摘要 / Abstract</summary>

  We present a new secret sharing algorithm that provides the storage efficiency of an Information Dispersal Algorithm (IDA) while providing perfect secret sharing. We achieve this by mixing the input message with random bytes generated using Repeatable Random Sequence Generator (RRSG). We also use the data from the RRSG to provide random polynomial evaluation points and optionally compute the polynomials on random isomorphic fields rather than a single fixed field.

  匹配依据：MPC: secret sharing

  </details>

- **High efficient multipartite entanglement purification using hyperentanglement**
  2021-01-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2101.08920)
  Lan Zhou, Pei-Shun Yan, Wei Zhong, Yu-Bo Sheng

  <details><summary>摘要 / Abstract</summary>

  Multipartite entanglement plays an important role in controlled quantum teleportation, quantum secret sharing, quantum metrology and some other important quantum information branches. However, the maximally multipartite entangled state will degrade into the mixed state because of the noise. We present an efficient multipartite entanglement purification protocol (EPP) which can distill the high quality entangled states from low quality entangled states for N-photon systems in a Greenberger-Horne-Zeilinger (GHZ) state in only linear optics. After performing the protocol, the spatial-mode entanglement is used to purify the polarization entanglement and one pair of high quality polarization entangled state will be obtained. This EPP has several advantages. Firstly, with the same purification success probability, this EPP only requires one pair of multipartite GHZ state, while existing EPPs usually require two pairs of multipartite GHZ state. Secondly, if consider the practical transmission and detector efficiency, this EPP may be extremely useful for the ratio of purification efficiency is increased rapidly with both the number of photons and the transmission distance. Thirdly, this protocol requires linear optics and does not add additional measurement operations, so that it is feasible for experiment. All these advantages will make this protocol have potential application for future quantum information processing.

  匹配依据：MPC: secret sharing

  </details>

- **Banquet: Short and Fast Signatures from AES**
  2021-01-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/068)
  Carsten Baum, Cyprien Delpech de Saint Guilhem, Daniel Kales, Emmanuela Orsini, Peter Scholl, Greg Zaverucha

  <details><summary>摘要 / Abstract</summary>

  In this work we introduce Banquet, a digital signature scheme with post-quantum security, constructed using only symmetric-key primitives. The design is based on the MPC-in-head paradigm also used by Picnic (CCS 2017) and BBQ (SAC 2019). Like BBQ, Banquet uses only standardized primitives, namely AES and SHA-3, but signatures are more than 50% shorter, making them competitive with Picnic (which uses a non-standard block cipher to improve performance). The MPC protocol in Banquet uses a new technique to verify correctness of the AES S-box computations, which is efficient because the cost is amortized with a batch verification strategy. Our implementation and benchmarks also show that both signing and verification can be done in under 10ms on a current x64 CPU. We also explore the parameter space to show the range of trade-offs that are possible with the Banquet design, and show that Banquet can nearly match the signature sizes possible with Picnic (albeit with slower, but still practical run times) or have speed within a factor of two of Picnic (at the cost of larger signatures).

  匹配依据：MPC: mpc (context)

  </details>

- **Exploring Design and Governance Challenges in the Development of Privacy-Preserving Computation**
  2021-01-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2101.08048)
  Nitin Agrawal, Reuben Binns, Max Van Kleek, Kim Laine, Nigel Shadbolt

  <details><summary>摘要 / Abstract</summary>

  Homomorphic encryption, secure multi-party computation, and differential privacy are part of an emerging class of Privacy Enhancing Technologies which share a common promise: to preserve privacy whilst also obtaining the benefits of computational analysis. Due to their relative novelty, complexity, and opacity, these technologies provoke a variety of novel questions for design and governance. We interviewed researchers, developers, industry leaders, policymakers, and designers involved in their deployment to explore motivations, expectations, perceived opportunities and barriers to adoption. This provided insight into several pertinent challenges facing the adoption of these technologies, including: how they might make a nebulous concept like privacy computationally tractable; how to make them more usable by developers; and how they could be explained and made accountable to stakeholders and wider society. We conclude with implications for the development, deployment, and responsible governance of these privacy-preserving computation techniques.

  匹配依据：MPC: secure multi party computation

  </details>

- **The Cost of IEEE Arithmetic in Secure Computation**
  2021-01-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/054)
  David W. Archer, Shahla Atapoor, Nigel P. Smart

  <details><summary>摘要 / Abstract</summary>

  Programmers are used to the rounding and error properties of IEEE double precision arithmetic, however in secure computing paradigms, such as provided by Multi-Party Computation (MPC), usually a different form of approximation is provided for real number arithmetic. We compare the two standard variants using for LSSS-based MPC, with an implementation of IEEE compliant double precision using binary circuit-based MPC. We compare the relative performance, and conclude that the addition cost of IEEE compliance maybe too great for some applications. Thus in the secure domain standards bodies may wish to examine a different form of real number approximations.

  匹配依据：MPC: multi party computation, secure computation, secure computing

  </details>

- **SoK: Fully Homomorphic Encryption Compilers**
  2021-01-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2101.07078)
  Alexander Viand, Patrick Jattke, Anwar Hithnawi

  <details><summary>摘要 / Abstract</summary>

  Fully Homomorphic Encryption (FHE) allows a third party to perform arbitrary computations on encrypted data, learning neither the inputs nor the computation results. Hence, it provides resilience in situations where computations are carried out by an untrusted or potentially compromised party. This powerful concept was first conceived by Rivest et al. in the 1970s. However, it remained unrealized until Craig Gentry presented the first feasible FHE scheme in 2009. The advent of the massive collection of sensitive data in cloud services, coupled with a plague of data breaches, moved highly regulated businesses to increasingly demand confidential and secure computing solutions. This demand, in turn, has led to a recent surge in the development of FHE tools. To understand the landscape of recent FHE tool developments, we conduct an extensive survey and experimental evaluation to explore the current state of the art and identify areas for future development. In this paper, we survey, evaluate, and systematize FHE tools and compilers. We perform experiments to evaluate these tools&#x27; performance and usability aspects on a variety of applications. We conclude with recommendations for developers intending to develop FHE-based applications and a discussion on future directions for FHE tools development.

  匹配依据：MPC: secure computing

  </details>

- **Banners: Binarized Neural Networks with Replicated Secret Sharing**
  2021-01-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/045)
  Alberto Ibarrondo, Hervé Chabanne, Melek Önen

  <details><summary>摘要 / Abstract</summary>

  Binarized Neural Networks (BNN) provide efficient implementations of Convolutional Neural Networks (CNN). This makes them particularly suitable to perform fast and memory-light inference of neural networks running on resource-constrained devices. Motivated by the growing interest in CNN-based biometric recognition on potentially insecure devices, or as part of strong multi-factor authentication for sensitive applications, the protection of BNN inference on edge devices is rendered imperative. We propose a new method to perform secure inference of BNN relying on secure multiparty computation. While preceding papers offered security in a semi-honest setting for BNN or malicious security for standard CNN, our work yields security with abort against one malicious adversary for BNN by leveraging on Replicated Secret Sharing (RSS) for an honest majority with three computing parties. Experimentally, we implement BaNNeRS on top of MP-SPDZ and compare it with prior work over binarized models trained for MNIST and CIFAR10 image classification datasets. Our results attest the efficiency of BaNNeRS as a privacy-preserving inference technique.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **MPC-CSAS: Multi-Party Computation for Real-time Privacy-preserving Speed Advisory Systems**
  2021-01-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2101.06451)
  Mingming Liu, Long Cheng, Yingqi Gu, Ying Wang, Qingzhi Liu, Noel E. O'Connor

  <details><summary>摘要 / Abstract</summary>

  As a part of Advanced Driver Assistance Systems (ADASs), Consensus-based Speed Advisory Systems (CSAS) have been proposed to recommend a common speed to a group of vehicles for specific application purposes, such as emission control and energy management. With Vehicle-to-Vehicle (V2V), Vehicle-to-Infrastructure (V2I) technologies and advanced control theories in place, state-of-the-art CSAS can be designed to get an optimal speed in a privacy-preserving and decentralized manner. However, the current method only works for specific cost functions of vehicles, and its execution usually involves many algorithm iterations leading long convergence time. Therefore, the state-of-the-art design method is not applicable to a CSAS design which requires real-time decision making. In this paper, we address the problem by introducing MPC-CSAS, a Multi-Party Computation (MPC) based design approach for privacy-preserving CSAS. Our proposed method is simple to implement and applicable to all types of cost functions of vehicles. Moreover, our simulation results show that the proposed MPC-CSAS can achieve very promising system performance in just one algorithm iteration without using extra infrastructure for a typical CSAS.

  匹配依据：MPC: multi party computation

  </details>

- **Privacy-Preserving Randomized Controlled Trials: A Protocol for Industry Scale Deployment**
  2021-01-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2101.04766)
  Mahnush Movahedi, Benjamin M. Case, Andrew Knox, James Honaker, Li Li, Yiming Paul Li, Sanjay Saravanan, Shubho Sengupta, Erik Taubeneck

  <details><summary>摘要 / Abstract</summary>

  In this paper, we outline a way to deploy a privacy-preserving protocol for multiparty Randomized Controlled Trials on the scale of 500 million rows of data and more than a billion gates. Randomized Controlled Trials (RCTs) are widely used to improve business and policy decisions in various sectors such as healthcare, education, criminology, and marketing. A Randomized Controlled Trial is a scientifically rigorous method to measure the effectiveness of a treatment. This is accomplished by randomly allocating subjects to two or more groups, treating them differently, and then comparing the outcomes across groups. In many scenarios, multiple parties hold different parts of the data for conducting and analyzing RCTs. Given privacy requirements and expectations of each of these parties, it is often challenging to have a centralized store of data to conduct and analyze RCTs. We accomplish this by a three-stage solution. The first stage uses the Private Secret Share Set Intersection (PS$^3$I) solution to create a joined set and establish secret shares without revealing membership, while discarding individuals who were placed into more than one group. The second stage runs multiple instances of a general purpose MPC over a sharded database to aggregate statistics about each experimental group while discarding individuals who took an action before they received treatment. The third stage adds distributed and calibrated Differential Privacy (DP) noise to the aggregate statistics and uncertainty measures, providing formal two-sided privacy guarantees. We also evaluate the performance of multiple open source general purpose MPC libraries for this task. We additionally demonstrate how we have used this to create a working ads effectiveness measurement product capable of measuring hundreds of millions of individuals per experiment.

  匹配依据：MPC: mpc (context)

  </details>

- **Circuit-PSI with Linear Complexity via Relaxed Batch OPPRF**
  2021-01-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/034)
  Nishanth Chandran, Divya Gupta, Akash Shah

  <details><summary>摘要 / Abstract</summary>

  In $2$-party Circuit-based Private Set Intersection (Circuit-PSI), $P_0$ and $P_1$ hold sets $\mathsf{S}_{0}$ and $\mathsf{S}_{1}$ respectively and wish to securely compute a function $f$ over the set $\mathsf{S}_{0} \cap \mathsf{S}_{1}$ (e.g., cardinality, sum over associated attributes, or threshold intersection). Following a long line of work, Pinkas et al. ($\mathsf{PSTY}$, Eurocrypt 2019) showed how to construct a concretely efficient Circuit-PSI protocol with linear communication complexity. However, their protocol requires super-linear computation. In this work, we construct concretely efficient Circuit-PSI protocols with linear computational and communication cost. Further, our protocols are more performant than the state-of-the-art, $\mathsf{PSTY}$ -- we are $\approx 2.3\times$ more communication efficient and are up to $2.8\times$ faster. We obtain our improvements through a new primitive called Relaxed Batch Oblivious Programmable Pseudorandom Functions ($\mathsf{RBOPPRF}$) that can be seen as a strict generalization of Batch $\mathsf{OPPRF}$s that were used in $\mathsf{PSTY}$. We believe that this primitive could be of independent interest.

  匹配依据：MPC: private set intersection

  </details>

- **Lightweight Techniques for Private Heavy Hitters**
  2021-01-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2012.14884) · [IACR ePrint](https://eprint.iacr.org/2021/017)
  Dan Boneh, Elette Boyle, Henry Corrigan-Gibbs, Niv Gilboa, Yuval Ishai

  <details><summary>摘要 / Abstract</summary>

  This paper presents Poplar, a new system for solving the private heavy-hitters problem. In this problem, there are many clients and a small set of data-collection servers. Each client holds a private bitstring. The servers want to recover the set of all popular strings, without learning anything else about any client&#x27;s string. A web-browser vendor, for instance, can use Poplar to figure out which homepages are popular, without learning any user&#x27;s homepage. We also consider the simpler private subset-histogram problem, in which the servers want to count how many clients hold strings in a particular set without revealing this set to the clients. Poplar uses two data-collection servers and, in a protocol run, each client send sends only a single message to the servers. Poplar protects client privacy against arbitrary misbehavior by one of the servers and our approach requires no public-key cryptography (except for secure channels), nor general-purpose multiparty computation. Instead, we rely on incremental distributed point functions, a new cryptographic tool that allows a client to succinctly secret-share the labels on the nodes of an exponentially large binary tree, provided that the tree has a single non-zero path. Along the way, we develop new general tools for providing malicious security in applications of distributed point functions.

  匹配依据：MPC: multiparty computation

  </details>

- **HERMES: Scalable, Secure, and Privacy-Enhancing Vehicle Access System**
  2021-01-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2101.01950) · [IACR ePrint](https://eprint.iacr.org/2020/1583)
  Iraklis Symeonidis, Dragos Rotaru, Mustafa A. Mustafa, Bart Mennink, Bart Preneel, Panos Papadimitratos

  <details><summary>摘要 / Abstract</summary>

  We propose HERMES, a scalable, secure, and privacy-enhancing system for users to share and access vehicles. HERMES securely outsources operations of vehicle access token generation to a set of untrusted servers. It builds on an earlier proposal, namely SePCAR [1], and extends the system design for improved efficiency and scalability. To cater to system and user needs for secure and private computations, HERMES utilizes and combines several cryptographic primitives with secure multiparty computation efficiently. It conceals secret keys of vehicles and transaction details from the servers, including vehicle booking details, access token information, and user and vehicle identities. It also provides user accountability in case of disputes. Besides, we provide semantic security analysis and prove that HERMES meets its security and privacy requirements. Last but not least, we demonstrate that HERMES is efficient and, in contrast to SePCAR, scales to a large number of users and vehicles, making it practical for real-world deployments. We build our evaluations with two different multiparty computation protocols: HtMAC-MiMC and CBC-MAC-AES. Our results demonstrate that HERMES with HtMAC-MiMC requires only approx 1,83 ms for generating an access token for a single-vehicle owner and approx 11,9 ms for a large branch of rental companies with over a thousand vehicles. It handles 546 and 84 access token generations per second, respectively. This results in HERMES being 696 (with HtMAC-MiMC) and 42 (with CBC-MAC-AES) times faster compared to in SePCAR for a single-vehicle owner access token generation. Furthermore, we show that HERMES is practical on the vehicle side, too, as access token operations performed on a prototype vehicle on-board unit take only approx 62,087 ms.

  匹配依据：MPC: multiparty computation, secure multiparty computation

  </details>

- **Algebraic Geometric Secret Sharing Schemes over Large Fields Are Asymptotically Threshold**
  2021-01-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2101.01304) · [IACR ePrint](https://eprint.iacr.org/2020/1616)
  Fan Peng, Hao Chen, Chang-An Zhao

  <details><summary>摘要 / Abstract</summary>

  In Chen-Cramer Crypto 2006 paper \cite{cc} algebraic geometric secret sharing schemes were proposed such that the &quot;Fundamental Theorem in Information-Theoretically Secure Multiparty Computation&quot; by Ben-Or, Goldwasser and Wigderson \cite{BGW88} and Chaum, Crépeau and Damgård \cite{CCD88} can be established over constant-size base finite fields. These algebraic geometric secret sharing schemes defined by a curve of genus $g$ over a constant size finite field ${\bf F}_q$ is quasi-threshold in the following sense, any subset of $u \leq T-1$ players (non qualified) has no information of the secret and any subset of $u \geq T+2g$ players (qualified) can reconstruct the secret. It is natural to ask that how far from the threshold these quasi-threshold secret sharing schemes are? How many subsets of $u \in [T, T+2g-1]$ players can recover the secret or have no information of the secret? In this paper it is proved that almost all subsets of $u \in [T,T+g-1]$ players have no information of the secret and almost all subsets of $u \in [T+g,T+2g-1]$ players can reconstruct the secret when the size $q$ goes to the infinity and the genus satisfies $\lim \frac{g}{\sqrt{q}}=0$. Then algebraic geometric secret sharing schemes over large finite fields are asymptotically threshold in this case. We also analyze the case when the size $q$ of the base field is fixed and the genus goes to the infinity.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Protecting Big Data Privacy Using Randomized Tensor Network Decomposition and Dispersed Tensor Computation**
  2021-01-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2101.04194)
  Jenn-Bing Ong, Wee-Keong Ng, Ivan Tjuawinata, Chao Li, Jielin Yang, Sai None Myne, Huaxiong Wang, Kwok-Yan Lam, C. -C. Jay Kuo

  <details><summary>摘要 / Abstract</summary>

  Data privacy is an important issue for organizations and enterprises to securely outsource data storage, sharing, and computation on clouds / fogs. However, data encryption is complicated in terms of the key management and distribution; existing secure computation techniques are expensive in terms of computational / communication cost and therefore do not scale to big data computation. Tensor network decomposition and distributed tensor computation have been widely used in signal processing and machine learning for dimensionality reduction and large-scale optimization. However, the potential of distributed tensor networks for big data privacy preservation have not been considered before, this motivates the current study. Our primary intuition is that tensor network representations are mathematically non-unique, unlinkable, and uninterpretable; tensor network representations naturally support a range of multilinear operations for compressed and distributed / dispersed computation. Therefore, we propose randomized algorithms to decompose big data into randomized tensor network representations and analyze the privacy leakage for 1D to 3D data tensors. The randomness mainly comes from the complex structural information commonly found in big data; randomization is based on controlled perturbation applied to the tensor blocks prior to decomposition. The distributed tensor representations are dispersed on multiple clouds / fogs or servers / devices with metadata privacy, this provides both distributed trust and management to seamlessly secure big data storage, communication, sharing, and computation. Experiments show that the proposed randomization techniques are helpful for big data anonymization and efficient for big data storage and computation.

  匹配依据：MPC: secure computation

  </details>

- **A Research Ecosystem for Secure Computing**
  2021-01-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2101.01264)
  Nadya Bliss, Lawrence A. Gordon, Daniel Lopresti, Fred Schneider, Suresh Venkatasubramanian

  <details><summary>摘要 / Abstract</summary>

  Computing devices are vital to all areas of modern life and permeate every aspect of our society. The ubiquity of computing and our reliance on it has been accelerated and amplified by the COVID-19 pandemic. From education to work environments to healthcare to defense to entertainment - it is hard to imagine a segment of modern life that is not touched by computing. The security of computers, systems, and applications has been an active area of research in computer science for decades. However, with the confluence of both the scale of interconnected systems and increased adoption of artificial intelligence, there are many research challenges the community must face so that our society can continue to benefit and risks are minimized, not multiplied. Those challenges range from security and trust of the information ecosystem to adversarial artificial intelligence and machine learning. Along with basic research challenges, more often than not, securing a system happens after the design or even deployment, meaning the security community is routinely playing catch-up and attempting to patch vulnerabilities that could be exploited any minute. While security measures such as encryption and authentication have been widely adopted, questions of security tend to be secondary to application capability. There needs to be a sea-change in the way we approach this critically important aspect of the problem: new incentives and education are at the core of this change. Now is the time to refocus research community efforts on developing interconnected technologies with security &quot;baked in by design&quot; and creating an ecosystem that ensures adoption of promising research developments. To realize this vision, two additional elements of the ecosystem are necessary - proper incentive structures for adoption and an educated citizenry that is well versed in vulnerabilities and risks.

  匹配依据：MPC: secure computing

  </details>

- **Privacy-Preserving Privacy Profile Proposal Protocol**
  2021-01-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/006)
  Wyatt Howe, Andrei Lapets

  <details><summary>摘要 / Abstract</summary>

  Many web-based and mobile applications and services allow users to indicate their preferences regarding whether and how their personal information can be used or reused by the application itself, by the service provider, and/or by third parties. The number of possible configurations that constitute a user&#x27;s preference profile can be overwhelming to a typical user. This report describes a practical, privacy-preserving technique for reducing the burden users face when specifying their preferences by offering users data-driven recommendations for fully-specified preference profiles based on their inputs for just a few settings. The feasibility of the approach is demonstrated by a browser-based prototype application that relies on secure multi-party computation and uses the web-compatible JIFF library as the backbone for managing communications between the client application and the recommendation service. The principal algorithms used for generating proposed preference profiles are $k$-means clustering (for privacy-preserving analysis of preference profile data across multiple users) and $k$-nearest neighbors (for selecting a proposed preference profile to recommend to the user).

  匹配依据：MPC: secure multi party computation

  </details>
