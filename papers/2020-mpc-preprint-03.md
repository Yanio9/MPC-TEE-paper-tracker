# 2020 · MPC · 仅预印本来源 · 第 3/3 页

[总目录](../PAPERS.md) · [上一页](2020-mpc-preprint-02.md)

- **Epione: Lightweight Contact Tracing with Strong Privacy**
  2020-04-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.13293)
  Ni Trieu, Kareem Shehata, Prateek Saxena, Reza Shokri, Dawn Song

  <details><summary>摘要 / Abstract</summary>

  Contact tracing is an essential tool in containing infectious diseases such as COVID-19. Many countries and research groups have launched or announced mobile apps to facilitate contact tracing by recording contacts between users with some privacy considerations. Most of the focus has been on using random tokens, which are exchanged during encounters and stored locally on users&#x27; phones. Prior systems allow users to search over released tokens in order to learn if they have recently been in the proximity of a user that has since been diagnosed with the disease. However, prior approaches do not provide end-to-end privacy in the collection and querying of tokens. In particular, these approaches are vulnerable to either linkage attacks by users using token metadata, linkage attacks by the server, or false reporting by users. In this work, we introduce Epione, a lightweight system for contact tracing with strong privacy protections. Epione alerts users directly if any of their contacts have been diagnosed with the disease, while protecting the privacy of users&#x27; contacts from both central services and other users, and provides protection against false reporting. As a key building block, we present a new cryptographic tool for secure two-party private set intersection cardinality (PSI-CA), which allows two parties, each holding a set of items, to learn the intersection size of two private sets without revealing intersection items. We specifically tailor it to the case of large-scale contact tracing where clients have small input sets and the server&#x27;s database of tokens is much larger.

  匹配依据：MPC: private set intersection

  </details>

- **Bounded Collusion Protocols, Cylinder-Intersection Extractors and Leakage-Resilient Secret Sharing**
  2020-04-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/473)
  Ashutosh Kumar, Raghu Meka, David Zuckerman

  <details><summary>摘要 / Abstract</summary>

  In this work we study bounded collusion protocols (BCPs) recently introduced in the context of secret sharing by Kumar, Meka, and Sahai (FOCS 2019). These are multi-party communication protocols on $n$ parties where in each round a subset of $p$-parties (the collusion bound) collude together and write a function of their inputs on a public blackboard. BCPs interpolate elegantly between the well-studied number-in-hand (NIH) model ($p=1$) and the number-on-forehead (NOF) model ($p=n-1$). Motivated by questions in communication complexity, secret sharing, and pseudorandomness we investigate BCPs more thoroughly, answering several questions about them. * We prove a polynomial (in the input-length) lower bound for an explicit function against BCPs where any constant fraction of players can collude. Previously, nontrivial lower bounds were known only when the collusion bound was at most logarithmic in the input-length (owing to bottlenecks in NOF lower bounds). * For all $t \leq n$, we construct efficient $t$-out-of-$n$ secret sharing schemes where the secret remains hidden even given the transcript of a BCP with collusion bound $O(t/\log t)$. Prior work could only handle collusions of size $O(\log n)$. Along the way, we construct leakage-resilient schemes against disjoint and adaptive leakage, resolving a question asked by Goyal and Kumar (STOC 2018). * An explicit $n$-source cylinder intersection extractor whose output is close to uniform even when given the transcript of a BCP with a constant fraction of parties colluding. The min-entropy rate we require is $0.3$ (independent of collusion bound $p \ll n$). Our results rely on a new class of exponential sums that interpolate between the ones considered in additive combinatorics by Bourgain (Geometric and Functional Analysis 2009) and Petridis and Shparlinski (Journal d&#x27;Analyse Mathématique 2019).

  匹配依据：MPC: secret sharing

  </details>

- **Attacks on Image Encryption Schemes for Privacy-Preserving Deep Neural Networks**
  2020-04-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.13263)
  Alex Habeen Chang, Benjamin M. Case

  <details><summary>摘要 / Abstract</summary>

  Privacy preserving machine learning is an active area of research usually relying on techniques such as homomorphic encryption or secure multiparty computation. Recent novel encryption techniques for performing machine learning using deep neural nets on images have recently been proposed by Tanaka and Sirichotedumrong, Kinoshita, and Kiya. We present new chosen-plaintext and ciphertext-only attacks against both of these proposed image encryption schemes and demonstrate the attacks&#x27; effectiveness on several examples.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Obscure: Information-Theoretically Secure, Oblivious, and Verifiable Aggregation Queries on Secret-Shared Outsourced Data -- Full Version**
  2020-04-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.13115)
  Peeyush Gupta, Yin Li, Sharad Mehrotra, Nisha Panwar, Shantanu Sharma, Sumaya Almanee

  <details><summary>摘要 / Abstract</summary>

  Despite exciting progress on cryptography, secure and efficient query processing over outsourced data remains an open challenge. We develop a communication-efficient and information-theoretically secure system, entitled Obscure for aggregation queries with conjunctive or disjunctive predicates, using secret-sharing. Obscure is strongly secure (i.e., secure regardless of the computational-capabilities of an adversary) and prevents the network, as well as, the (adversarial) servers to learn the user&#x27;s queries, results, or the database. In addition, Obscure provides additional security features, such as hiding access-patterns (i.e., hiding the identity of the tuple satisfying a query) and hiding query-patterns (i.e., hiding which two queries are identical). Also, Obscure does not require any communication between any two servers that store the secret-shared data before/during/after the query execution. Moreover, our techniques deal with the secret-shared data that is outsourced by a single or multiple database owners, as well as, allows a user, which may not be the database owner, to execute the query over secret-shared data. We further develop (non-mandatory) privacy-preserving result verification algorithms that detect malicious behaviors, and experimentally validate the efficiency of Obscure on large datasets, the size of which prior approaches of secret-sharing or multi-party computation systems have not scaled to.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Optimal Threshold Padlock Systems**
  2020-04-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.11552)
  Jannik Dreier, Jean-Guillaume Dumas, Pascal Lafourcade, Léo Robert

  <details><summary>摘要 / Abstract</summary>

  In 1968, Liu described the problem of securing documents in a shared secret project. In an example, at least six out of eleven participating scientists need to be present to open the lock securing the secret documents. Shamir proposed a mathematical solution to this physical problem in 1979, by designing an efficient $k$-out-of-$n$ secret sharing scheme based on Lagrange&#x27;s interpolation. Liu and Shamir also claimed that the minimal solution using physical locks is clearly impractical and exponential in the number of participants. In this paper we relax some implicit assumptions in their claim and propose an optimal physical solution to the problem of Liu that uses physical padlocks, but the number of padlocks is not greater than the number of participants. Then, we show that no device can do better for $k$-out-of-$n$ threshold padlock systems as soon as $k\geq{\sqrt{2n}}$, which holds true in particular for Liu&#x27;s example. More generally, we derive bounds required to implement any threshold system and prove a lower bound of $\mathcal{O}{\log(n)}$ padlocks for any threshold larger than $2$. For instance we propose an optimal scheme reaching that bound for $2$-out-of-$n$ threshold systems and requiring less than $2\log_2(n)$ padlocks. We also discuss more complex access structures, a wrapping technique, and other sublinear realizations like an algorithm to generate $3$-out-of-$n$ systems with $2.5\sqrt{n}$ padlocks. Finally we give an algorithm building $k$-out-of-$n$ threshold padlock systems with only $\mathcal{O}{\log(n)^{k-1}}$ padlocks. Apart from the physical world, our results also show that it is possible to implement secret sharing over small fields.

  匹配依据：MPC: secret sharing

  </details>

- **Leia: A Lightweight Cryptographic Neural Network Inference System at the Edge**
  2020-04-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/463)
  Xiaoning Liu, Bang Wu, Xingliang Yuan, Xun Yi

  <details><summary>摘要 / Abstract</summary>

  The advances in machine learning have revealed its great potential for emerging mobile applications such as face recognition and voice assistant. Models trained via a Neural Network (NN) can offer accurate and efficient inference services for mobile users. Unfortunately, the current deployment of such service encounters privacy concerns. Directly offloading the model to the mobile device violates model privacy of the model owner, while feeding user input to the service compromises user privacy. To address this issue, we propose, tailor, and evaluate Leia, a lightweight cryptographic NN inference system at the edge. Unlike prior cryptographic NN inference systems, Leia is designed with two mobile-friendly perspectives. First, Leia leverages the paradigm of edge computing wherein the inference procedure keeps the model closer to the mobile user to foster low latency service. Specifically, Leia&#x27;s architecture consists of two non-colluding edge services to obliviously perform NN inference on the encoded user data and model. Second, Leia&#x27;s realization makes the judicious use of potentially constrained computational and communication resources in edge devices. In particular, Leia adapts the Binarized Neural Network (BNN), a trending flavor of NN model with low memory footprint and computational cost, and purely chooses the lightweight secret sharing techniques to develop secure blocks of BNN. Empirical validation executed on Raspberry Pi confirms the practicality of Leia, showing that Leia can produce a prediction result with 97% accuracy by 4 seconds in the edge environment.

  匹配依据：MPC: secret sharing

  </details>

- **Can a Public Blockchain Keep a Secret?**
  2020-04-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/464)
  Fabrice Benhamouda, Craig Gentry, Sergey Gorbunov, Shai Halevi, Hugo Krawczyk, Chengyu Lin, Tal Rabin, Leonid Reyzin

  <details><summary>摘要 / Abstract</summary>

  Blockchains are gaining traction and acceptance, not just for cryptocurrencies, but increasingly as an architecture for distributed computing. In this work we seek solutions that allow a \emph{public} blockchain to act as a trusted long-term repository of secret information: Our goal is to deposit a secret with the blockchain, specify how it is to be used (e.g., the conditions under which it is released), and have the blockchain keep the secret and use it only in the specified manner (e.g., release only it once the conditions are met). This simple functionality enables many powerful applications, including signing statements on behalf of the blockchain, using it as the control plane for a storage system, performing decentralized program-obfuscation-as-a-service, and many more. Using proactive secret sharing techniques, we present a scalable solution for implementing this functionality on a public blockchain, in the presence of a mobile adversary controlling a small minority of the participants. The main challenge is that, on the one hand, scalability requires that we use small committees to represent the entire system, but, on the other hand, a mobile adversary may be able to corrupt the entire committee if it is small. For this reason, existing proactive secret sharing solutions are either non-scalable or insecure in our setting. We approach this challenge via &quot;player replaceability&quot;, which ensures the committee is anonymous until after it performs its actions. Our main technical contribution is a system that allows sharing and re-sharing of secrets among the members of small dynamic committees, without knowing who they are until after they perform their actions and erase their secrets. Our solution handles a fully mobile adversary corrupting roughly 1/4 of the participants at any time, and is scalable in terms of both the number of parties and the number of time intervals.

  匹配依据：MPC: secret sharing

  </details>

- **Performance Evaluation of Secure Multi-party Computation on Heterogeneous Nodes**
  2020-04-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.10926)
  Zhou Ni, Rujia Wang

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) is a broad cryptographic concept that can be adopted for privacy-preserving computation. With MPC, a number of parties can collaboratively compute a function, without revealing the actual input or output of the plaintext to others. The applications of MPC range from privacy-preserving voting, arithmetic calculation, and large-scale data analysis. From the system perspective, each party in MPC can run on one compute node. The compute nodes of multiple parties could be either homogeneous or heterogeneous; however, the distributed workloads from the MPC protocols tend to be always homogeneous (symmetric). In this work, we study a representative MPC framework and a set of MPC applications from the system performance perspective. We show the detailed online computation workflow of a state-of-the-art MPC protocol and analyze the root cause of its stall time and performance bottleneck on homogeneous and heterogeneous compute nodes.

  匹配依据：MPC: secure multi party computation

  </details>

- **On Bit Commitment and Oblivious Transfer in Measurement-Device Independent settings**
  2020-04-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.10515)
  Jeremy Ribeiro, Stephanie Wehner

  <details><summary>摘要 / Abstract</summary>

  Among the most studied tasks in Quantum Cryptography one can find Bit Commitment (BC) and Oblivious Transfer (OT), two central cryptographic primitives. In this paper we propose for the first time protocols for these tasks in the measurement-device independent (MDI) settings and analyze their security. We analyze two different cases: first we assume the parties have access to perfect single photon sources (but still in the presence of noise and losses), and second we assume that they only have imperfect single photon sources. In the first case we propose a protocol for both BC and OT and prove their security in the Noisy Quantum Storage model. Interestingly, in the case where honest parties do not have access to perfect single photon sources, we find that BC is still possible, but that it is &quot;more difficult&quot; to get a secure protocol for OT: We show that there is a whole class of protocols that cannot be secure. All our security analyses are done in the finite round regime.

  匹配依据：MPC: oblivious transfer

  </details>

- **Switched Threshold Signatures from K-Private PolyShamir Secret Sharing**
  2020-04-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/449)
  Kristian L. McDonald

  <details><summary>摘要 / Abstract</summary>

  Variant secret sharing schemes deriving from Shamir&#x27;s threshold secret sharing protocol are presented. Results include multi-secret sharing protocols using shares with $O(1)$ elements, independent of the number of secrets. The new schemes achieve a weaker notion of security (they&#x27;re secure rather than strongly secure) but maintain a property called $K$-privacy (inspired by $k$-anonymity). $K$-privacy ensures that all secrets remain private with respect to a subset of the secret space, though the particular subset providing privacy may vary among adversaries that acquire distinct sub-threshold sets of shares. Depending on the number of secrets and the protocol details, secure $K$-private multi-secret sharing schemes may be ``almost&#x27;&#x27; strongly secure or may remain merely secure and $K$-private - a difference captured by the notion of $K$-security. Novel applications of the multi-secret sharing schemes are presented, realising a primitive called a switched threshold signature. Switched threshold signatures have the quirky property that aggregating a threshold number of signatures of one type (e.g. Pointcheval-Sanders signatures) ``switches&#x27;&#x27; the signatures into a master signature of a different type. Collectively these results may permit efficiencies within, e.g., threshold credential issuance protocols.

  匹配依据：MPC: secret sharing

  </details>

- **Partial Secret Sharing Schemes**
  2020-04-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/448)
  Amir Jafari, Shahram Khazaei

  <details><summary>摘要 / Abstract</summary>

  The information ratio of an access structure is an important parameter for quantifying the efficiency of the best secret sharing scheme (SSS) realizing it. The most common security notion is perfect security. The following relaxations, in increasing level of security, have been presented in the literature: quasi-perfect, almost-perfect and statistical. Understanding the power of relaxing the correctness and privacy requirements in the efficiency of SSSs is a long-standing open problem. In this article, we introduce and study an extremely relaxed security notion, called partial security, for which it is only required that any qualified set gains strictly more information about the secret than any unqualified one. We refer to this gap as the nominal capacity. We quantify the efficiency of such schemes using a parameter called partial information ratio. It is defined to be the same as the (standard) information ratio, except that we divide the largest share entropy by nominal capacity instead of the secret entropy. Despite this modification, partial security turns out weaker than the weakest mentioned non-perfect security notion, i.e., quasi-perfect security. We present three main results in this paper. First, we prove that partial and perfect information ratios coincide for the class of linear SSSs. Consequently, for this class, information ratio is invariant with respect to all security notions. Second, by viewing a partial SSS as a wiretap channel, we prove that for the general (i.e., non-linear) class of SSSs, partial and statistical information ratios are equal. Consequently, for this class, information ratio is invariant with respect to all non-perfect security notions. Third, we show that partial and almost-perfect information ratios do not coincide for the class of mixed-linear schemes (i.e., schemes constructed by combining linear schemes with different underlying finite fields). Our first result strengthens the previous decomposition theorems for constructing perfect linear schemes. Our second result leads to a very strong decomposition theorem for constructing general (i.e., non-linear) statistical schemes. Our third result provides a rare example of the effect of imperfection on the efficiency of SSSs for a certain class of schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Maliciously Secure Matrix Multiplication with Applications to Private Deep Learning**
  2020-04-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/451)
  Hao Chen, Miran Kim, Ilya Razenshteyn, Dragos Rotaru, Yongsoo Song, Sameer Wagh

  <details><summary>摘要 / Abstract</summary>

  Computing on data in a manner that preserve the privacy is of growing importance. Multi-Party Computation (MPC) and Homomorphic Encryption (HE) are two cryptographic techniques for privacy-preserving computations. In this work, we have developed efficient UC-secure multiparty protocols for matrix multiplications and two-dimensional convolutions. We built upon the SPDZ framework and integrated the state-of-the-art HE algorithms for matrix multiplication. Our protocol achieved communication cost linear only in the input and output dimensions and not on the number of multiplication operations. We eliminate the ``triple sacrifice&#x27;&#x27; step of SPDZ to improve efficiency and simplify the zero-knowledge proofs. We implemented our protocols and benchmarked them against the SPDZ LowGear variant (Keller et al. Eurocrypt&#x27;18). For multiplying two square matrices of size 128, we reduced the communication cost from 1.54 GB to 12.46 MB, an improvement of over two orders of magnitude that only improves with larger matrix sizes. For evaluating all convolution layers of the ResNet-50 neural network, the communication reduces cost from 5 TB to 41 GB.

  匹配依据：MPC: multi party computation

  </details>

- **Impossibility of masking a set of quantum states of nonzero measure**
  2020-04-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.09667)
  Xiao-Bin Liang, Bo Li, Shao-Ming Fei, Heng Fan

  <details><summary>摘要 / Abstract</summary>

  We study the quantum information masking based on isometric linear operators that distribute the information encoded in pure states to the correlations in bipartite states. It is shown that a isometric linear operator can not mask any nonzero measure set of pure states. We present a geometric characterization of the maskable sets, and show that any maskable set must be on a spherical circle in certain Euclidean spaces. Detailed examples and potential applications in such as secret sharing and quantum cryptography are analyzed.

  匹配依据：MPC: secret sharing

  </details>

- **On Pseudorandom Encodings**
  2020-04-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/445)
  Thomas Agrikola, Geoffroy Couteau, Yuval Ishai, Stanislaw Jarecki, Amit Sahai

  <details><summary>摘要 / Abstract</summary>

  We initiate a study of pseudorandom encodings: efficiently computable and decodable encoding functions that map messages from a given distribution to a random-looking distribution. For instance, every distribution that can be perfectly and efficiently compressed admits such a pseudorandom encoding. Pseudorandom encodings are motivated by a variety of cryptographic applications, including password-authenticated key exchange, &#x27;&#x27;honey encryption&#x27;&#x27; and steganography. The main question we ask is whether every efficiently samplable distribution admits a pseudorandom encoding. Under different cryptographic assumptions, we obtain positive and negative answers for different flavors of pseudorandom encodings, and relate this question to problems in other areas of cryptography. In particular, by establishing a two-way relation between pseudorandom encoding schemes and efficient invertible sampling algorithms, we reveal a connection between adaptively secure multiparty computation for randomized functionalities and questions in the domain of steganography.

  匹配依据：MPC: secure multiparty computation

  </details>

- **DP-Cryptography: Marrying Differential Privacy and Cryptography in Emerging Applications**
  2020-04-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.08887)
  Sameer Wagh, Xi He, Ashwin Machanavajjhala, Prateek Mittal

  <details><summary>摘要 / Abstract</summary>

  Differential privacy (DP) has arisen as the state-of-the-art metric for quantifying individual privacy when sensitive data are analyzed, and it is starting to see practical deployment in organizations such as the US Census Bureau, Apple, Google, etc. There are two popular models for deploying differential privacy - standard differential privacy (SDP), where a trusted server aggregates all the data and runs the DP mechanisms, and local differential privacy (LDP), where each user perturbs their own data and perturbed data is analyzed. Due to security concerns arising from aggregating raw data at a single server, several real world deployments in industry have embraced the LDP model. However, systems based on the LDP model tend to have poor utility - &quot;a gap&quot; in the utility achieved as compared to systems based on the SDP model. In this work, we survey and synthesize emerging directions of research at the intersection of differential privacy and cryptography. First, we survey solutions that combine cryptographic primitives like secure computation and anonymous communication with differential privacy to give alternatives to the LDP model that avoid a trusted server as in SDP but close the gap in accuracy. These primitives introduce performance bottlenecks and necessitate efficient alternatives. Second, we synthesize work in an area we call &quot;DP-Cryptography&quot; - cryptographic primitives that are allowed to leak differentially private outputs. These primitives have orders of magnitude better performance than standard cryptographic primitives. DP-cryptographic primitives are perfectly suited for implementing alternatives to LDP, but are also applicable to scenarios where standard cryptographic primitives do not have practical implementations. Through this unique lens of research taxonomy, we survey ongoing research in these directions while also providing novel directions for future research.

  匹配依据：MPC: secure computation

  </details>

- **Asymmetrical Vertical Federated Learning**
  2020-04-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.07427)
  Yang Liu, Xiong Zhang, Libin Wang

  <details><summary>摘要 / Abstract</summary>

  Federated learning is a distributed machine learning method that aims to preserve the privacy of sample features and labels. In a federated learning system, ID-based sample alignment approaches are usually applied with few efforts made on the protection of ID privacy. In real-life applications, however, the confidentiality of sample IDs, which are the strongest row identifiers, is also drawing much attention from many participants. To relax their privacy concerns about ID privacy, this paper formally proposes the notion of asymmetrical vertical federated learning and illustrates the way to protect sample IDs. The standard private set intersection protocol is adapted to achieve the asymmetrical ID alignment phase in an asymmetrical vertical federated learning system. Correspondingly, a Pohlig-Hellman realization of the adapted protocol is provided. This paper also presents a genuine with dummy approach to achieving asymmetrical federated model training. To illustrate its application, a federated logistic regression algorithm is provided as an example. Experiments are also made for validating the feasibility of this approach.

  匹配依据：MPC: private set intersection

  </details>

- **Improving the Performance of the Picnic Signature Scheme**
  2020-04-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/427)
  Daniel Kales, Greg Zaverucha

  <details><summary>摘要 / Abstract</summary>

  Picnic is a digital signature algorithm designed to provide security against attacks by quantum computers. The design uses only symmetric-key primitives, and is an efficient instantiation of the MPC-in-the-head paradigm. In this work, we explore the Picnic design in great detail. We investigate and benchmark different parameter choices and show that there exist better parameter choices than those in the current specification. We also present improvements to the MPC protocol that shorten signatures and reduce signing time. The proposed MPC changes tailor the protocol to the circuit of interest in Picnic, but may also be of independent interest. Taken together, these changes give a new instantiation of Picnic that signs messages 7.9 to 13.9 times faster, and verifies signatures 4.5 to 5.5 times faster than the existing ``Picnic2&#x27;&#x27; design, while having nearly the same signature sizes.

  匹配依据：MPC: mpc (context)

  </details>

- **Secure Federated Learning in 5G Mobile Networks**
  2020-04-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.06700)
  Martin Isaksson, Karl Norrman

  <details><summary>摘要 / Abstract</summary>

  Machine Learning (ML) is an important enabler for optimizing, securing and managing mobile networks. This leads to increased collection and processing of data from network functions, which in turn may increase threats to sensitive end-user information. Consequently, mechanisms to reduce threats to end-user privacy are needed to take full advantage of ML. We seamlessly integrate Federated Learning (FL) into the 3GPP 5G Network Data Analytics (NWDA) architecture, and add a Multi-Party Computation (MPC) protocol for protecting the confidentiality of local updates. We evaluate the protocol and find that it has much lower overhead than previous work, without affecting ML performance.

  匹配依据：MPC: multi party computation

  </details>

- **Secure Two-Party Computation in a Quantum World**
  2020-04-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/411)
  Niklas Büscher, Daniel Demmler, Nikolaos P. Karvelas, Stefan Katzenbeisser, Juliane Krämer, Deevashwer Rathee, Thomas Schneider, Patrick Struck

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation has been extensively studied in the past years and has reached a level that is considered practical for several applications. The techniques developed thus far have been steadily optimized for performance and were shown to be secure in the classical setting, but are not known to be secure against quantum adversaries. In this work, we start to pave the way for secure two-party computation in a quantum world where the adversary has access to a quantum computer. We show that post-quantum secure two-party computation has comparable efficiency to their classical counterparts. For this, we develop a lattice-based OT protocol which we use to implement a post-quantum secure variant of Yao&#x27;s famous garbled circuits (GC) protocol (FOCS&#x27;82). Along with the OT protocol, we show that the oblivious transfer extension protocol of Ishai et al. (CRYPTO&#x27;03), which allows running many OTs using mainly symmetric cryptography, is post-quantum secure. To support these results, we prove that Yao&#x27;s GC protocol achieves post-quantum security if the underlying building blocks do.

  匹配依据：MPC: garbled circuits, oblivious transfer, secure multi party computation, secure two party computation

  </details>

- **Ordinos: A Verifiable Tally-Hiding E-Voting System**
  2020-04-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/405)
  Ralf Kuesters, Julian Liedtke, Johannes Mueller, Daniel Rausch, Andreas Vogt

  <details><summary>摘要 / Abstract</summary>

  Modern electronic voting systems (e-voting systems) are designed to provide not only vote privacy but also (end-to-end) verifiability. Several verifiable e-voting systems have been proposed in the literature, with Helios being one of the most prominent ones. Almost all such systems, however, reveal not just the voting result but also the full tally, consisting of the exact number of votes per candidate or even all single votes. There are several situations where this is undesirable. For example, in elections with only a few voters (e.g., boardroom or jury votings), revealing the complete tally leads to a low privacy level, possibly deterring voters from voting for their actual preference. In other cases, revealing the complete tally might unnecessarily embarrass some candidates. Often, the voting result merely consists of a single winner or a ranking of candidates, so revealing only this information but not the complete tally is sufficient. This property is called tally-hiding and it offers completely new options for e-voting. In this paper, we propose the first provably secure end-to-end verifiable tally-hiding e-voting system, called Ordinos. We instantiated our system with suitable cryptographic primitives, including an MPC protocol for greater-than tests, implemented the system, and evaluated its performance, demonstrating its practicality. Moreover, our work provides a deeper understanding of tally-hiding in general, in particular in how far tally-hiding affects the levels of privacy and verifiability of e-voting systems.

  匹配依据：MPC: mpc (context)

  </details>

- **Feather: Lightweight Multi-party Updatable Delegated Private Set Intersection**
  2020-04-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/407)
  Aydin Abadi, Sotirios Terzis, Changyu Dong

  <details><summary>摘要 / Abstract</summary>

  Abstract. With the growth of cloud computing, the need arises for Private Set Intersection (PSI) protocols that can operate on outsourced data and delegate computation to cloud servers. One limitation of existing delegated PSI protocols is that they are all designed for static data and do not allow efficient update on outsourced data. Another limitation is that they cannot efficiently support PSI among multiple clients, which is often needed in practice. This paper presents “Feather”, the first delegated PSI protocol that supports efficient data updates and scalable multi-party PSI computation on outsourced datasets. It lets clients independently prepare and upload their private data to the cloud once, then delegate the computation an unlimited number of times. The update operation has very low communication and computation complexity, and this is achieved without sacrificing PSI efficiency and security. Feather does not use public key cryptography, that makes it more scalable. We have implemented a prototype and compared the concrete performance against the state of the art. The evaluation indicates that Feather does achieve better performance in both update and PSI computation.

  匹配依据：MPC: private set intersection

  </details>

- **PrivEdge: From Local to Distributed Private Training and Prediction**
  2020-04-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.05574) · [Code](https://github.com/smartcameras/PrivEdge)
  Ali Shahin Shamsabadi, Adria Gascon, Hamed Haddadi, Andrea Cavallaro

  <details><summary>摘要 / Abstract</summary>

  Machine Learning as a Service (MLaaS) operators provide model training and prediction on the cloud. MLaaS applications often rely on centralised collection and aggregation of user data, which could lead to significant privacy concerns when dealing with sensitive personal data. To address this problem, we propose PrivEdge, a technique for privacy-preserving MLaaS that safeguards the privacy of users who provide their data for training, as well as users who use the prediction service. With PrivEdge, each user independently uses their private data to locally train a one-class reconstructive adversarial network that succinctly represents their training data. As sending the model parameters to the service provider in the clear would reveal private information, PrivEdge secret-shares the parameters among two non-colluding MLaaS providers, to then provide cryptographically private prediction services through secure multi-party computation techniques. We quantify the benefits of PrivEdge and compare its performance with state-of-the-art centralised architectures on three privacy-sensitive image-based tasks: individual identification, writer identification, and handwritten letter recognition. Experimental results show that PrivEdge has high precision and recall in preserving privacy, as well as in distinguishing between private and non-private images. Moreover, we show the robustness of PrivEdge to image compression and biased training data. The source code is available at https://github.com/smartcameras/PrivEdge.

  匹配依据：MPC: secure multi party computation

  </details>

- **Secret Sharing based Secure Regressions with Applications**
  2020-04-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.04898)
  Chaochao Chen, Liang Li, Wenjing Fang, Jun Zhou, Li Wang, Lei Wang, Shuang Yang, Alex Liu, Hao Wang

  <details><summary>摘要 / Abstract</summary>

  Nowadays, the utilization of the ever expanding amount of data has made a huge impact on web technologies while also causing various types of security concerns. On one hand, potential gains are highly anticipated if different organizations could somehow collaboratively share their data for technological improvements. On the other hand, data security concerns may arise for both data holders and data providers due to commercial or sociological concerns. To make a balance between technical improvements and security limitations, we implement secure and scalable protocols for multiple data holders to train linear regression and logistic regression models. We build our protocols based on the secret sharing scheme, which is scalable and efficient in applications. Moreover, our proposed paradigm can be generalized to any secure multiparty training scenarios where only matrix summation and matrix multiplications are used. We demonstrate our approach by experiments which shows the scalability and efficiency of our proposed protocols, and finally present its real-world applications.

  匹配依据：MPC: secret sharing

  </details>

- **Coded Secure Multi-Party Computation for Massive Matrices with Adversarial Nodes**
  2020-04-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.04985)
  Seyed Reza Hoseini Najarkolaei, Mohammad Ali Maddah-Ali, Mohammad Reza Aref

  <details><summary>摘要 / Abstract</summary>

  In this work, we consider the problem of secure multi-party computation (MPC), consisting of $Γ$ sources, each has access to a large private matrix, $N$ processing nodes or workers, and one data collector or master. The master is interested in the result of a polynomial function of the input matrices. Each source sends a randomized functions of its matrix, called as its share, to each worker. The workers process their shares in interaction with each other, and send some results to the master such that it can derive the final result. There are several constraints: (1) each worker can store a function of each input matrix, with the size of $\frac{1}{m}$ fraction of that input matrix, (2) up to $t$ of the workers, for some integer $t$, are adversary and may collude to gain information about the private inputs or can do malicious actions to make the final result incorrect. The objective is to design an MPC scheme with the minimum number the workers, called the recovery threshold, such that the final result is correct, workers learn no information about the input matrices, and the master learns nothing beyond the final result. In this paper, we propose an MPC scheme that achieves the recovery threshold of $3t+2m-1$ workers, which is order-wise less than the recovery threshold of the conventional methods. The challenge in dealing with this set up is that when nodes interact with each other, the malicious messages that adversarial nodes generate propagate through the system, and can mislead the honest nodes. To deal with this challenge, we design some subroutines that can detect erroneous messages, and correct or drop them.

  匹配依据：MPC: secure multi party computation

  </details>

- **A note on blind contact tracing at scale with applications to the COVID-19 pandemic**
  2020-04-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.05116)
  Jack K. Fitzsimons, Atul Mantri, Robert Pisarczyk, Tom Rainforth, Zhikuan Zhao

  <details><summary>摘要 / Abstract</summary>

  The current COVID-19 pandemic highlights the utility of contact tracing, when combined with case isolation and social distancing, as an important tool for mitigating the spread of a disease [1]. Contact tracing provides a mechanism of identifying individuals with a high likelihood of previous exposure to a contagious disease, allowing additional precautions to be put in place to prevent continued transmission. Here we consider a cryptographic approach to contact tracing based on secure two-party computation (2PC). We begin by considering the problem of comparing a set of location histories held by two parties to determine whether they have come within some threshold distance while at the same time maintaining the privacy of the location histories. We propose a solution to this problem using pre-shared keys, adapted from an equality testing protocol due to Ishai et al [2]. We discuss how this protocol can be used to maintain privacy within practical contact tracing scenarios, including both app-based approaches and approaches which leverage location history held by telecoms and internet service providers. We examine the efficiency of this approach and show that existing infrastructure is sufficient to support anonymised contact tracing at a national level.

  匹配依据：MPC: secure two party computation

  </details>

- **A Novel Application of Boolean Functions with High Algebraic Immunity in Minimal Codes**
  2020-04-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.04932)
  Hang Chen, Cunsheng Ding, Sihem Mesnager, Chunming Tang

  <details><summary>摘要 / Abstract</summary>

  Boolean functions with high algebraic immunity are important cryptographic primitives in some stream ciphers. In this paper, two methodologies for constructing binary minimal codes from sets, Boolean functions and vectorial Boolean functions with high algebraic immunity are proposed. More precisely, a general construction of new minimal codes using minimal codes contained in Reed-Muller codes and sets without nonzero low degree annihilators is presented. The other construction allows us to yield minimal codes from certain subcodes of Reed-Muller codes and vectorial Boolean functions with high algebraic immunity. Via these general constructions, infinite families of minimal binary linear codes of dimension $m$ and length less than or equal to $m(m+1)/2$ are obtained. In addition, a lower bound on the minimum distance of the proposed minimal linear codes is established. Conjectures and open problems are also presented. The results of this paper show that Boolean functions with high algebraic immunity have nice applications in several fields such as symmetric cryptography, coding theory and secret sharing schemes.

  匹配依据：MPC: secret sharing

  </details>

- **LevioSA: Lightweight Secure Arithmetic Computation**
  2020-04-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/393)
  Carmit Hazay, Yuval Ishai, Antonio Marcedone, Muthuramakrishnan Venkitasubramaniam

  <details><summary>摘要 / Abstract</summary>

  We study the problem of secure two-party computation of arithmetic circuits in the presence of active (``malicious&#x27;&#x27;) parties. This problem is motivated by privacy-preserving numerical computations, such as ones arising in the context of machine learning training and classification, as well as in threshold cryptographic schemes. In this work, we design, optimize, and implement an actively secure protocol for secure two-party arithmetic computation. A distinctive feature of our protocol is that it can make a fully modular black-box use of any passively secure implementation of oblivious linear function evaluation (OLE). OLE is a commonly used primitive for secure arithmetic computation, analogously to the role of oblivious transfer in secure computation for Boolean circuits. For typical (large but not-too-narrow) circuits, our protocol requires roughly 4 invocations of passively secure OLE per multiplication gate. This significantly improves over the recent TinyOLE protocol (Dottling et al., ACM CCS 2017), which requires 22 invocations of actively secure OLE in general, or 44 invocations of a specific code-based passively secure OLE. Our protocol follows the high level approach of the IPS compiler (Ishai et al., CRYPTO 2008, TCC 2009), optimizing it in several ways. In particular, we adapt optimization ideas that were used in the context of the practical zero-knowledge argument system Ligero (Ames et al., ACM CCS 2017) to the more general setting of secure computation, and explore the possibility of boosting efficiency by employing a ``leaky&#x27;&#x27; passively secure OLE protocol. The latter is motivated by recent (passively secure) lattice-based OLE implementations in which allowing such leakage enables better efficiency. We showcase the performance of our protocol by applying its implementation to several useful instances of secure arithmetic computation. On ``wide&#x27;&#x27; circuits, such as ones computing a fixed function on many different inputs, our protocol is 5x faster and transmits 4x less data than the state-of-the-art Overdrive (Keller et al., Eurocrypt 2018). Our benchmarks include a general passive-to-active OLE compiler, authenticated generation of ``Beaver triples&#x27;&#x27;, and a system for securely outsourcing neural network classification. The latter is the first actively secure implementation of its kind, strengthening the passive security provided by recent related works (Mohassel and Zhang, IEEE S&amp;P 2017; Juvekar et al., USENIX 2018).

  匹配依据：MPC: oblivious transfer, secure computation, secure two party computation

  </details>

- **TraceSecure: Towards Privacy Preserving Contact Tracing**
  2020-04-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.04059)
  James Bell, David Butler, Chris Hicks, Jon Crowcroft

  <details><summary>摘要 / Abstract</summary>

  Contact tracing is being widely employed to combat the spread of COVID-19. Many apps have been developed that allow for tracing to be done automatically based off location and interaction data generated by users. There are concerns, however, regarding the privacy and security of users data when using these apps. These concerns are paramount for users who contract the virus, as they are generally required to release all their data. Motivated by the need to protect users privacy we propose two solutions to this problem. Our first solution builds on current &quot;message based&quot; methods and our second leverages ideas from secret sharing and additively homomorphic encryption.

  匹配依据：MPC: secret sharing

  </details>

- **Improved Secure Efficient Delegated Private Set Intersection**
  2020-04-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.03976)
  Alireza Kavousi, Javad Mohajeri, Mahmoud Salmasizadeh

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection (PSI) is a vital cryptographic technique used for securely computing common data of different sets. In PSI protocols, often two parties hope to find their common set elements without needing to disclose their uncommon ones. In recent years, the cloud has been playing an influential role in PSI protocols which often need huge computational tasks. In 2017, Abadi et al. introduced a scheme named EO-PSI which uses a cloud to pass on the main computations to it and does not include any public-key operations. In EO-PSI, parties need to set up secure channels beforehand; otherwise, an attacker can easily eavesdrop on communications between honest parties and find private information. This paper presents an improved EO-PSI scheme which has the edge on the previous scheme in terms of privacy and complexity. By providing possible attacks on the prior scheme, we show the necessity of using secure channels between parties. Also, our proposed protocol is secure against passive attacks without having to have any secure channels. We measure the protocol&#x27;s overhead and show that computational complexity is considerably reduced and also is fairer compared to the previous scheme.

  匹配依据：MPC: private set intersection

  </details>

- **FALCON: Honest-Majority Maliciously Secure Framework for Private Deep Learning**
  2020-04-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2004.02229)
  Sameer Wagh, Shruti Tople, Fabrice Benhamouda, Eyal Kushilevitz, Prateek Mittal, Tal Rabin

  <details><summary>摘要 / Abstract</summary>

  We propose Falcon, an end-to-end 3-party protocol for efficient private training and inference of large machine learning models. Falcon presents four main advantages - (i) It is highly expressive with support for high capacity networks such as VGG16 (ii) it supports batch normalization which is important for training complex networks such as AlexNet (iii) Falcon guarantees security with abort against malicious adversaries, assuming an honest majority (iv) Lastly, Falcon presents new theoretical insights for protocol design that make it highly efficient and allow it to outperform existing secure deep learning solutions. Compared to prior art for private inference, we are about 8x faster than SecureNN (PETS&#x27;19) on average and comparable to ABY3 (CCS&#x27;18). We are about 16-200x more communication efficient than either of these. For private training, we are about 6x faster than SecureNN, 4.4x faster than ABY3 and about 2-60x more communication efficient. Our experiments in the WAN setting show that over large networks and datasets, compute operations dominate the overall latency of MPC, as opposed to the communication.

  匹配依据：MPC: mpc (context)

  </details>

- **Privacy-Preserving Contact Tracing of COVID-19 Patients**
  2020-04-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/375)
  Leonie Reichert, Samuel Brack, Björn Scheuermann

  <details><summary>摘要 / Abstract</summary>

  The current Covid-19 pandemic shows that our modern globalized world can be heavily affected by a quickly spreading, highly infectious, deadly virus in a matter of weeks. It became apparent that manual contact tracing and quarantining of suspects can only be effective in the first days of the spread before the exponential growth overwhelms the health authorities. By automating tracing processes and quarantining everyone who came in contact with infected people, as well as arriving travelers, it should be possible to quickly loosen lockdown measures. Countries like China, Singapore and Israel hastily developed privacy-endangering schemes to computationally trace contacts using user-generated location histories or mass surveillance data . There have been reports of deanonymizations of South Korean citizens from the public “anonymized” data set of infected people. To approach this conflict of interests first identify and formulate of privacy risks of contact tracing. On this basis we propose a privacy-preserving approach to contact tracing using secure multi party computation and binary search. Our preliminary evaluation shows the idea is feasible in different scenarios derived from real-world case studies.

  匹配依据：MPC: secure multi party computation

  </details>

- **Multiparty Generation of an RSA Modulus**
  2020-04-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/370)
  Megan Chen, Ran Cohen, Jack Doerner, Yashvanth Kondi, Eysa Lee, Schuyler Rosefield, abhi shelat

  <details><summary>摘要 / Abstract</summary>

  We present a new multiparty protocol for the distributed generation of biprime RSA moduli, with security against any subset of maliciously colluding parties assuming oblivious transfer and the hardness of factoring. Our protocol is highly modular, and its uppermost layer can be viewed as a template that generalizes the structure of prior works and leads to a simpler security proof. We introduce a combined sampling-and-sieving technique that eliminates both the inherent leakage in the approach of Frederiksen et al. (Crypto&#x27;18), and the dependence upon additively homomorphic encryption in the approach of Hazay et al. (JCrypt&#x27;19). We combine this technique with an efficient, privacy-free check to detect malicious behavior retroactively when a sampled candidate is not a biprime, and thereby overcome covert rejection-sampling attacks and achieve both asymptotic and concrete efficiency improvements over the previous state of the art.

  匹配依据：MPC: oblivious transfer

  </details>

- **Diogenes: Lightweight Scalable RSA Modulus Generation with a Dishonest Majority**
  2020-04-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/374)
  Megan Chen, Carmit Hazay, Yuval Ishai, Yuriy Kashnikov, Daniele Micciancio, Tarik Riviere, abhi shelat, Muthu Venkitasubramaniam, Ruihan Wang

  <details><summary>摘要 / Abstract</summary>

  In this work, we design and implement the first protocol for RSA modulus construction that can support thousands of parties and offers security against an arbitrary number of corrupted parties. In a nutshell, we design the ``best&#x27;&#x27; protocol for this scale that is secure against passive corruption, then amplify it to obtain active security using efficient non-interactive zero-knowledge arguments. Our protocol satisfies a stronger security guarantee where a deviating party can be identified when the protocol aborts (referred to as security with identifiable-abort) and allows for ``public verifiability&#x27;&#x27;. Our passively secure protocol extends the recent work of Chen et al. that, in turn, is based on the blueprint introduced in the original work of Boneh-Franklin protocol (CRYPTO 1997, J. ACM, 2001). Specifically, we reduce the task of sampling a modulus to secure distributed multiplication, which we implement via an efficient threshold additively homomorphic encryption (AHE) scheme based on the Ring-LWE assumption. This results in a protocol where the amortized per-party communication cost grows logarithmically in the number of parties. In order to keep the parties lightweight, we employ an ``untrusted&#x27;&#x27; coordinator that is connected to all parties and performs all public and broadcast operations. We amplify this protocol to obtain active security (with identifiable-abort) by attaching zero-knowledge proofs. We instantiate our ZK proof system by composing two different types of ZK proof systems: (1) the Ligero sub-linear zero-knowledge proof system (Ames et al., CCS 2017), and (2) Sigma-protocol for proving the knowledge of a discrete logarithm in unknown order groups (Shoup, Eurocrypt 2000). We implemented both the passive and the active variants of our protocol and ran experiments using 2 to 4,000 parties. This is the first such implementation of any MPC protocol that can scale to more than 1,000 parties. For generating a 2048-bit modulus among 1,000 parties, our passive protocol executed in under 4 minutes and the active variant ran in 22 minutes.

  匹配依据：MPC: mpc (context)

  </details>

- **Yet another insecure group key distribution scheme using secret sharing**
  2020-03-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2003.14356)
  Chris J Mitchell

  <details><summary>摘要 / Abstract</summary>

  A recently proposed group key distribution scheme known as UMKESS, based on secret sharing, is shown to be insecure. Not only is it insecure, but it does not always work, and the rationale for its design is unsound. UMKESS is the latest in a long line of flawed group key distribution schemes based on secret sharing techniques.

  匹配依据：MPC: secret sharing

  </details>

- **Assessing Disease Exposure Risk with Location Data: A Proposal for Cryptographic Preservation of Privacy**
  2020-03-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2003.14412)
  Alex Berke, Michiel Bakker, Praneeth Vepakomma, Kent Larson, Alex 'Sandy' Pentland

  <details><summary>摘要 / Abstract</summary>

  Governments and researchers around the world are implementing digital contact tracing solutions to stem the spread of infectious disease, namely COVID-19. Many of these solutions threaten individual rights and privacy. Our goal is to break past the false dichotomy of effective versus privacy-preserving contact tracing. We offer an alternative approach to assess and communicate users&#x27; risk of exposure to an infectious disease while preserving individual privacy. Our proposal uses recent GPS location histories, which are transformed and encrypted, and a private set intersection protocol to interface with a semi-trusted authority. There have been other recent proposals for privacy-preserving contact tracing, based on Bluetooth and decentralization, that could further eliminate the need for trust in authority. However, solutions with Bluetooth are currently limited to certain devices and contexts while decentralization adds complexity. The goal of this work is two-fold: we aim to propose a location-based system that is more privacy-preserving than what is currently being adopted by governments around the world, and that is also practical to implement with the immediacy needed to stem a viral outbreak.

  匹配依据：MPC: private set intersection

  </details>

- **Tracking the Invisible: Privacy-Preserving Contact Tracing to Control the Spread of a Virus**
  2020-03-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2003.13073)
  Didem Demirag, Erman Ayday

  <details><summary>摘要 / Abstract</summary>

  Today, tracking and controlling the spread of a virus is a crucial need for almost all countries. Doing this early would save millions of lives and help countries keep a stable economy. The easiest way to control the spread of a virus is to immediately inform the individuals who recently had close contact with the diagnosed patients. However, to achieve this, a centralized authority (e.g., a health authority) needs detailed location information from both healthy individuals and diagnosed patients. Thus, such an approach, although beneficial to control the spread of a virus, results in serious privacy concerns, and hence privacy-preserving solutions are required to solve this problem. Previous works on this topic either (i) compromise privacy (especially privacy of diagnosed patients) to have better efficiency or (ii) provide unscalable solutions. In this work, we propose a technique based on private set intersection between physical contact histories of individuals (that are recorded using smart phones) and a centralized database (run by a health authority) that keeps the identities of the positive diagnosed patients for the disease. Proposed solution protects the location privacy of both healthy individuals and diagnosed patients and it guarantees that the identities of the diagnosed patients remain hidden from other individuals. Notably, proposed scheme allows individuals to receive warning messages indicating their previous contacts with a positive diagnosed patient. Such warning messages will help them realize the risk and isolate themselves from other people. We make sure that the warning messages are only observed by the corresponding individuals and not by the health authority. We also implement the proposed scheme and show its efficiency and scalability via simulations.

  匹配依据：MPC: private set intersection

  </details>

- **Efficient MPC with a Mixed Adversary**
  2020-03-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/356)
  Martin Hirt, Marta Mularczyk

  <details><summary>摘要 / Abstract</summary>

  Over the past 20 years, the efficiency of secure multi-party protocols has been greatly improved. While the seminal protocols from the late 80&#x27;s require a communication of $\Omega(n^6)$ field elements per multiplication among $n$ parties, recent protocols offer linear communication complexity. This means that each party needs to communicate a constant number of field elements per multiplication, independent of $n$. However, these efficient protocols only offer active security, which implies that at most $t&lt;n/3$ (perfect security), respectively $t&lt;n/2$ (statistical or computational security) parties may be corrupted. Higher corruption thresholds (i.e., $t\geq n/2$) can only be achieved with degraded security (unfair abort), where one single corrupted party can prevent honest parties from learning their outputs. The aforementioned upper bounds ($t&lt;n/3$ and $t&lt;n/2$) have been circumvented by considering mixed adversaries (Fitzi et al., Crypto&#x27; 98), i.e., adversaries that corrupt, at the same time, some parties actively, some parties passively, and some parties in the fail-stop manner. It is possible, for example, to achieve perfect security even if $2/3$ of the parties are faulty (three quarters of which may abort in the middle of the protocol, and a quarter may even arbitrarily misbehave). This setting is much better suited to many applications, where the crash of a party is more likely than a coordinated active attack. Surprisingly, since the presentation of the feasibility result for the mixed setting, no progress has been made in terms of efficiency: the state-of-the-art protocol still requires a communication of $\Omega(n^6)$ field elements per multiplication. In this paper, we present a perfectly-secure MPC protocol for the mixed setting with essentially the same efficiency as the best MPC protocols for the active-only setting. For the first time, this allows to tolerate faulty majorities, while still providing optimal efficiency. As a special case, this also results in the first fully-secure MPC protocol secure against any number of crashing parties, with optimal (i.e., linear in $n$) communication. We provide simulation-based proofs of our construction.

  匹配依据：MPC: mpc (context)

  </details>

- **Cooperation and dependencies in multipartite systems**
  2020-03-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2003.12489)
  Waldemar Klobus, Marek Miller, Mahasweta Pandit, Ray Ganardi, Lukas Knips, Jan Dziewior, Jasmin Meinecke, Harald Weinfurter, Wieslaw Laskowski, Tomasz Paterek

  <details><summary>摘要 / Abstract</summary>

  We propose an information-theoretic quantifier for the advantage gained from cooperation that captures the degree of dependency between subsystems of a global system. The quantifier is distinct from measures of multipartite correlations despite sharing many properties with them. It is directly computable for classical as well as quantum systems and reduces to comparing the respective conditional mutual information between any two subsystems. Exemplarily we show the benefits of using the new quantifier for symmetric quantum secret sharing. We also prove an inequality characterizing the lack of monotonicity of conditional mutual information under local operations and provide intuitive understanding for it. This underlines the distinction between the multipartite dependence measure introduced here and multipartite correlations.

  匹配依据：MPC: secret sharing

  </details>

- **An ideal hierarchical secret sharing scheme**
  2020-03-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2003.12651)
  Ghanem Meriem, Bouroubi Sadek

  <details><summary>摘要 / Abstract</summary>

  One of the methods used in order to protect a secret K is a secret sharing scheme. In this scheme the secret K is distributed among a finite set of participants P by a special participant called the dealer, in such a way that only predefined subsets of participants can recover the secret after collaborating with their secret shares. The construction of secret sharing schemes has received a considerable attention of many searchers whose main goal was to improve the information rate. In this paper, we propose a novel construction of a secret sharing scheme which is based on the hierarchical concept of companies illustrated through its organization chart and represented by a tree. We proof that the proposed scheme is ideal by showing that the information rate equals 1. In order to show the efficiency of the proposed scheme, we discuss all possible kinds of attacks and proof that the security in ensured. Finally, we include a detailed didactic example for a small company organization chart.

  匹配依据：MPC: secret sharing

  </details>

- **Some Low Round Zero Knowledge Protocols**
  2020-03-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/347)
  Hongda Li, Peifang Ni, Dongxue Pan

  <details><summary>摘要 / Abstract</summary>

  In this paper, we focus on zero-knowledge protocols for NP with low round complexity under the augmented black-box simulation technique, in which the simulator has access to the verifier&#x27;s secret information, and obtain positive results on 3-round zero-knowledge proofs and 2-round zero-knowledge arguments for NP and 2-round zero-knowledge proofs for QNR. More precisely, our contributions are five-fold: (i) we propose the notion of generalized claw-free function and the notion of trapdoor generalized claw-free function, and then we show a construction of trapdoor generalized claw-free function under the discrete logarithm assumption and the knowledge of exponent assumption, (ii) we propose the notion of completely extractable bit-commitment and give a construction of it from trapdoor generalized claw-free functions, (iii) we present a 3-round zero-knowledge proof for NP based on the completely extractable bit-commitment schemes and Yao&#x27;s garbling circuit technique, (iv) we show a 2-round zero-knowledge argument for NP based on indistinguishable obfuscator, (v) we transform the basic 2-round honest verifier zero-knowledge proof protocol for quadratic non-residue into a 2-round zero-knowledge proof protocol.

  匹配依据：MPC: garbling circuit

  </details>

- **Corella: A Private Multi Server Learning Approach based on Correlated Queries**
  2020-03-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2003.12052)
  Hamidreza Ehteram, Mohammad Ali Maddah-Ali, Mahtab Mirmohseni

  <details><summary>摘要 / Abstract</summary>

  The emerging applications of machine learning algorithms on mobile devices motivate us to offload the computation tasks of training a model or deploying a trained one to the cloud or at the edge of the network. One of the major challenges in this setup is to guarantee the privacy of the client data. Various methods have been proposed to protect privacy in the literature. Those include (i) adding noise to the client data, which reduces the accuracy of the result, (ii) using secure multiparty computation (MPC), which requires significant communication among the computing nodes or with the client, (iii) relying on homomorphic encryption (HE) methods, which significantly increases computation load at the servers. In this paper, we propose $\textit{Corella}$ as an alternative approach to protect the privacy of data. The proposed scheme relies on a cluster of servers, where at most $T \in \mathbb{N}$ of them may collude, each running a learning model (e.g., a deep neural network). Each server is fed with the client data, added with $\textit{strong}$ noise, independent from user data. The variance of the noise is set to be large enough to make the information leakage to any subset of up to $T$ servers information-theoretically negligible. On the other hand, the added noises for different servers are $\textit{correlated}$. This correlation among the queries allows the parameters of the models running on different servers to be $\textit{trained}$ such that the client can mitigate the contribution of the noises by combining the outputs of the servers, and recover the final result with high accuracy and with a minor computational effort. Simulation results for various datasets demonstrate the accuracy of the proposed approach for the classification, using deep neural networks, and the autoencoder, as supervised and unsupervised learning tasks, respectively.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Improved Primitives for MPC over Mixed Arithmetic-Binary Circuits**
  2020-03-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/338)
  Daniel Escudero, Satrajit Ghosh, Marcel Keller, Rahul Rachuri, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  This work introduces novel techniques to improve the translation between arithmetic and binary data types in secure multi-party computation. We introduce a new approach to performing these conversions using what we call extended doubly-authenticated bits (edaBits), which correspond to shared integers in the arithmetic domain whose bit decomposition is shared in the binary domain. These can be used to considerably increase the efficiency of non-linear operations such as truncation, secure comparison and bit-decomposition. Our edaBits are similar to the daBits technique introduced by Rotaru et al. (Indocrypt 2019). However, we show that edaBits can be directly produced much more efficiently than daBits, with active security, while enabling the same benefits in higher-level applications. Our method for generating edaBits involves a novel cut-and-choose technique that may be of independent interest, and improves efficiency by exploiting natural, tamper-resilient properties of binary circuits that occur in our construction. We also show how edaBits can be applied to efficiently implement various non-linear protocols of interest, and we thoroughly analyze their correctness for both signed and unsigned integers. The results of this work can be applied to any corruption threshold, although they seem best suited to dishonest majority protocols such as SPDZ. We implement and benchmark our constructions, and experimentally verify that our technique yield a substantial increase in efficiency. EdaBits save in communication by a factor that lies between $2$ and $60$ for secure comparisons with respect to a purely arithmetic approach, and between 2 and 25 with respect to using daBits. Improvements in throughput per second are slightly lower but still as high as a factor of 47. We also apply our novel machinery to the tasks of biometric matching and convolutional neural networks, obtaining a noticeable improvement as well.

  匹配依据：MPC: secure multi party computation

  </details>

- **Privacy-preserving Weighted Federated Learning within Oracle-Aided MPC Framework**
  2020-03-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2003.07630)
  Huafei Zhu, Zengxiang Li, Mervyn Cheah, Rick Siow Mong Goh

  <details><summary>摘要 / Abstract</summary>

  This paper studies privacy-preserving weighted federated learning within the oracle-aided multi-party computation (MPC) framework. The contribution of this paper mainly comprises the following three-fold: In the first fold, a new notion which we call weighted federated learning (wFL) is introduced and formalized inspired by McMahan et al.&#x27;s seminal paper. The weighted federated learning concept formalized in this paper differs from that presented in McMahan et al.&#x27;s paper since both addition and multiplication operations are executed over ciphers in our model while these operations are executed over plaintexts in McMahan et al.&#x27;s model. In the second fold, an oracle-aided MPC solution for computing weighted federated learning is formalized by decoupling the security of federated learning systems from that of underlying multi-party computations. Our decoupling formulation may benefit machine learning developers to select their best security practices from the state-of-the-art security tool sets; In the third fold, a concrete solution to the weighted federated learning problem is presented and analysed. The security of our implementation is guaranteed by the security composition theorem assuming that the underlying multiplication algorithm is secure against honest-but-curious adversaries.

  匹配依据：MPC: multi party computation

  </details>

- **Hardness vs. (Very Little) Structure in Cryptography: A Multi-Prover Interactive Proofs Perspective**
  2020-03-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/330)
  Gil Segev, Ido Shahaf

  <details><summary>摘要 / Abstract</summary>

  The hardness of highly-structured computational problems gives rise to a variety of public-key primitives. On one hand, the structure exhibited by such problems underlies the basic functionality of public-key primitives, but on the other hand it may endanger public-key cryptography in its entirety via potential algorithmic advances. This subtle interplay initiated a fundamental line of research on whether structure is inherently necessary for cryptography, starting with Rudich&#x27;s early work (PhD Thesis &#x27;88) and recently leading to that of Bitansky, Degwekar and Vaikuntanathan (CRYPTO &#x27;17). Identifying the structure of computational problems with their corresponding complexity classes, Bitansky et al. proved that a variety of public-key primitives (e.g., public-key encryption, oblivious transfer and even functional encryption) cannot be used in a black-box manner to construct either any hard language that has $\mathsf{NP}$-verifiers both for the language itself and for its complement, or any hard language (and even promise problem) that has a statistical zero-knowledge proof system -- corresponding to hardness in the structured classes $\mathsf{NP} \cap \mathsf{coNP}$ or $\mathsf{SZK}$, respectively, from a black-box perspective. In this work we prove that the same variety of public-key primitives do not inherently require even very little structure in a black-box manner: We prove that they do not imply any hard language that has multi-prover interactive proof systems both for the language and for its complement -- corresponding to hardness in the class $\mathsf{MIP} \cap \mathsf{coMIP}$ from a black-box perspective. Conceptually, given that $\mathsf{MIP} = \mathsf{NEXP}$, our result rules out languages with very little structure. Additionally, we prove a similar result for collision-resistant hash functions, and more generally for any cryptographic primitive that exists relative to a random oracle. Already the cases of languages that have $\mathsf{IP}$ or $\mathsf{AM}$ proof systems both for the language itself and for its complement, which we rule out as immediate corollaries, lead to intriguing insights. For the case of $\mathsf{IP}$, where our result can be circumvented using non-black-box techniques, we reveal a gap between black-box and non-black-box techniques. For the case of $\mathsf{AM}$, where circumventing our result via non-black-box techniques would be a major development, we both strengthen and unify the proofs of Bitansky et al. for languages that have $\mathsf{NP}$-verifiers both for the language itself and for its complement and for languages that have a statistical zero-knowledge proof system.

  匹配依据：MPC: oblivious transfer

  </details>

- **Secure k-ish nearest neighbors classifier**
  2020-03-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/319)
  Hayim Shaul, Dan Feldman, Daniela Rus

  <details><summary>摘要 / Abstract</summary>

  The $k$-nearest neighbors ($k$NN) classifier predicts a class of a query, $q$, by taking the majority class of its $k$ neighbors in an existing (already classified) database, $S$. In secure $k$NN, $q$ and $S$ are owned by two different parties and $q$ is classified without sharing data. In this work we present a classifier based on $k$NN, that is more efficient to implement with homomorphic encryption (HE). The efficiency of our classifier comes from a relaxation we make to consider $\kappa$ nearest neighbors for $\kappa\approx k$ with probability that increases as the statistical distance between Gaussian and the distribution of the distances from $q$ to $S$ decreases. We call our classifier $k$-ish Nearest Neighbors ($k$-ish NN). For the implementation we introduce {\em double-blinded coin-toss} where the bias and output of the toss are encrypted. We use it to approximate the average and variance of the distances from $q$ to $S$ in a scalable circuit whose depth is independent of $|S|$. We believe these to be of independent interest. We implemented our classifier in an open source library based on HElib and tested it on a breast tumor database. Our classifier has accuracy and running time comparable to current state of the art (non-HE) MPC solution that have better running time but worse communication complexity. It also has communication complexity similar to naive HE implementation that have worse running time.

  匹配依据：MPC: mpc (context)

  </details>

- **Multiparty Homomorphic Encryption from Ring-Learning-With-Errors**
  2020-03-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/304) · [Code](https://github.com/ldsec/lattigo)
  Christian Mouchet, Juan Troncoso-Pastoriza, Jean-Philippe Bossuat, Jean-Pierre Hubaux

  <details><summary>摘要 / Abstract</summary>

  We propose and evaluate a secure-multiparty-computation (MPC) solution in the semi-honest model with dishonest majority that is based on multiparty homomorphic encryption (MHE). To support our solution, we introduce a multiparty version of the Brakerski-Fan-Vercauteren homomorphic cryptosystem and implement it in an open-source library. MHE-based MPC solutions have several advantages: Their transcript is public, their offline phase is compact, and their circuit-evaluation procedure is non-interactive. By exploiting these properties, the communication complexity of MPC tasks is reduced from quadratic to linear in the number of parties, thus enabling secure computation among potentially thousands of parties and in a broad variety of computing paradigms, from the traditional peer-to-peer setting to cloud-outsourcing and smart-contract technologies. MHE-based approaches can also outperform the state-of-the-art solutions, even for a small number of parties. We demonstrate this for three circuits: private input selection with application to private-information retrieval, component-wise vector multiplication with application to private-set intersection, and Beaver multiplication triples generation. For the first circuit, privately selecting one input among eight thousand parties&#x27; (of 32 KB each) requires only 1.31 MB of communication per party and completes in 61.7 seconds. For the second circuit with eight parties, our approach is 8.6 times faster and requires 39.3 times less communication than the current methods. For the third circuit and ten parties, our approach generates 20 times more triples per second while requiring 136 times less communication per-triple than an approach based on oblivious transfer. We implemented our scheme in the Lattigo library and open-sourced the code at https://github.com/ldsec/lattigo.

  匹配依据：MPC: oblivious transfer, private set intersection, secure computation, secure multiparty computation

  </details>

- **A Blockchain Traceable Scheme with Oversight Function**
  2020-03-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/311)
  Tianjun Ma, Haixia Xu, Peili Li

  <details><summary>摘要 / Abstract</summary>

  Many blockchain researches focus on the privacy protection. However, criminals can leverage strong privacy protection of the blockchain to do illegal crimes (such as ransomware) without being punished. These crimes have caused huge losses to society and users. Implementing identity tracing is an important step in dealing with issues arising from privacy protection. In this paper, we propose a blockchain traceable scheme with oversight function (BTSOF). The design of BTSOF builds on SkyEye (Tianjun Ma et al., Cryptology ePrint Archive 2020). In BTSOF, the regulator must obtain the consent of the committee to enable tracing. Moreover, we construct a non-interactive verifiable multi-secret sharing scheme (VMSS scheme) and leverage the VMSS scheme to design a distributed multi-key generation (DMKG) protocol for the Cramer-Shoup public key encryption scheme. The DMKG protocol is used in the design of BTSOF. We provide the security definition and security proof of the VMSS scheme and DMKG protocol.

  匹配依据：MPC: secret sharing

  </details>

- **Geometric secret sharing in a model of Hawking radiation**
  2020-03-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2003.05448)
  Vijay Balasubramanian, Arjun Kar, Onkar Parrikar, Gábor Sárosi, Tomonori Ugajin

  <details><summary>摘要 / Abstract</summary>

  We consider a black hole in three dimensional AdS space entangled with an auxiliary radiation system. We model the microstates of the black hole in terms of a field theory living on an end of the world brane behind the horizon, and allow this field theory to itself have a holographic dual geometry. This geometry is also a black hole since entanglement of the microstates with the radiation leaves them in a mixed state. This &quot;inception black hole&quot; can be purified by entanglement through a wormhole with an auxiliary system which is naturally identified with the external radiation, giving a realization of the ER=EPR scenario. In this context, we propose an extension of the Ryu-Takayanagi (RT) formula, in which extremal surfaces computing entanglement entropy are allowed to pass through the brane into its dual geometry. This new rule reproduces the Page curve for evaporating black holes, consistently with the recently proposed &quot;island formula&quot;. We then separate the radiation system into pieces. Our extended RT rule shows that the entanglement wedge of the union of radiation subsystems covers the black hole interior at late times, but the union of entanglement wedges of the subsystems may not. This result points to a secret sharing scheme in Hawking radiation wherein reconstruction of certain regions in the interior is impossible with any subsystem of the radiation, but possible with all of it.

  匹配依据：MPC: secret sharing

  </details>

- **ENSEI: Efficient Secure Inference via Frequency-Domain Homomorphic Convolution for Privacy-Preserving Visual Recognition**
  2020-03-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2003.05328)
  Song Bian, Tianchen Wang, Masayuki Hiromoto, Yiyu Shi, Takashi Sato

  <details><summary>摘要 / Abstract</summary>

  In this work, we propose ENSEI, a secure inference (SI) framework based on the frequency-domain secure convolution (FDSC) protocol for the efficient execution of privacy-preserving visual recognition. Our observation is that, under the combination of homomorphic encryption and secret sharing, homomorphic convolution can be obliviously carried out in the frequency domain, significantly simplifying the related computations. We provide protocol designs and parameter derivations for number-theoretic transform (NTT) based FDSC. In the experiment, we thoroughly study the accuracy-efficiency trade-offs between time- and frequency-domain homomorphic convolution. With ENSEI, compared to the best known works, we achieve 5--11x online time reduction, up to 33x setup time reduction, and up to 10x reduction in the overall inference time. A further 33% of bandwidth reductions can be obtained on binary neural networks with only 1% of accuracy degradation on the CIFAR-10 dataset.

  匹配依据：MPC: secret sharing

  </details>

- **Secure Multiparty Computation (MPC)**
  2020-03-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/300)
  Yehuda Lindell

  <details><summary>摘要 / Abstract</summary>

  Protocols for secure multiparty computation (MPC) enable a set of parties to interact and compute a joint function of their private inputs while revealing nothing but the output. The potential applications for MPC are huge: privacy-preserving auctions, private DNA comparisons, private machine learning, threshold cryptography, and more. Due to this, MPC has been an intensive topic of research in academia ever since it was introduced in the 1980s by Yao for the two-party case (FOCS 1986), and by Goldreich, Micali and Wigderson for the multiparty case (STOC 1987). Recently, MPC has become efficient enough to be used in practice, and has made the transition from an object of theoretical study to a technology being used in industry. In this article, we will review what MPC is, what problems it solves, and how it is being currently used. We note that the examples and references brought in this review article are far from comprehensive, and due to the lack of space many highly relevant works are not cited.

  匹配依据：MPC: secure multiparty computation

  </details>

- **A quantum secret sharing scheme with verifiable function**
  2020-03-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2003.04309)
  Li-Juan Liu, Zhi-Hui Li, Zhao-Wei Han, Dan-Li Zhi

  <details><summary>摘要 / Abstract</summary>

  In the $\left( {t,n} \right)$ threshold quantum secret sharing scheme, it is difficult to ensure that internal participants are honest. In this paper, a verifiable $\left( {t,n} \right)$ threshold quantum secret sharing scheme is designed combined with classical secret sharing scheme. First of all, the distributor uses the asymmetric binary polynomials to generate the shares and sends them to each participant. Secondly, the distributor sends the initial quantum state with the secret to the first participant, and each participant performs unitary operation that using the mutually unbiased bases on the obtained $d$ dimension single bit quantum state ($d$ is a large odd prime number). In this process, distributor can randomly check the participants, and find out the internal fraudsters by unitary inverse operation gradually upward. Then the secret is reconstructed after all other participants simultaneously public transmission. Security analysis show that this scheme can resist both external and internal attacks.

  匹配依据：MPC: secret sharing

  </details>

- **A Verifiable Quantum Secret Sharing Scheme Based on a Single Qubit**
  2020-03-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2003.04024)
  Dan-Li Zhi, Zhi-Hui Li, Zhao-Wei Han, Li-Juan Liu

  <details><summary>摘要 / Abstract</summary>

  To detect frauds from some internal participants or external attackers, some verifiable threshold quantum secret sharing schemes have been proposed. In this paper, we present a new verifiable threshold structure based on a single qubit using bivariate polynomial. First, Alice chooses an asymmetric bivariate polynomial and sends a pair of values from this polynomial to each participant. Then Alice and participants implement in sequence unitary transformation on the $d$-dimensional quantum state based on unbiased bases, where those unitary transformations are contacted by this polynomial. Finally, security analysis shows that the proposed scheme can detect the fraud from external and internal attacks compared with the exiting schemes and is comparable to the recent schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Weight hierarchies and weight distributions of a familiy of $p$-ary linear codes**
  2020-03-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2003.03048)
  Fei Li, Xiumei Li

  <details><summary>摘要 / Abstract</summary>

  The weight distribution and weight hierarchy of linear codes are two important research topics in coding theory. In this paper, by choosing proper defining sets from inhomogeneous quadratic functions over $\mathbb{F}_{q}^{2},$ we construct a family of $3$-weight $p$-ary linear codes and determine their weight distributions and weight hierarchies. Most of the codes can be used in secret sharing schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Differential Power Analysis of the Picnic Signature Scheme**
  2020-03-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/267)
  Tim Gellersen, Okan Seker, Thomas Eisenbarth

  <details><summary>摘要 / Abstract</summary>

  This work introduces the first differential side-channel analysis of the Picnic Signature Scheme, an alternate candidate in the ongoing competition for post-quantum cryptography by the National Institute of Standards and Technology (NIST). We present a successful side-channel analysis of the underlying multiparty implementation of the LowMC block cipher (MPC-LowMC) and show how side-channel information can be used to recover the entire secret key by exploiting two different parts of the algorithm. LowMC key recovery then allows to forge signatures for the calling Picnic post-quantum signature scheme. We target the NIST reference implementation executed on a FRDM-K66F development board. Key recovery succeeds with fewer than 1000 LowMC traces, which can be obtained from fewer than 30 observed Picnic signatures.

  匹配依据：MPC: mpc (context)

  </details>

- **Statistical ZAPR Arguments from Bilinear Maps**
  2020-02-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/256)
  Alex Lombardi, Vinod Vaikuntanathan, Daniel Wichs

  <details><summary>摘要 / Abstract</summary>

  Dwork and Naor (FOCS &#x27;00) defined ZAPs as 2-message witness-indistinguishable proofs that are public-coin. We relax this to ``ZAPs with private randomness&#x27;&#x27; (ZAPRs), where the verifier can use private coins to sample the first message (independently of the statement being proved), but the proof must remain publicly verifiable given only the protocol transcript. In particular, ZAPRs are reusable, meaning that the first message can be reused for multiple proofs without compromising security. Known constructions of ZAPs from trapdoor permutations or bilinear maps are only computationally WI (and statistically sound). Two recent results of Badrinarayanan-Fernando-Jain-Khurana-Sahai and Goyal-Jain-Jin-Malavolta [EUROCRYPT &#x27;20] construct the first statistical ZAP arguments, which are statistically WI (and computationally sound), from the quasi-polynomial LWE assumption. Here, we construct statistical ZAPR arguments from the quasi-polynomial decision-linear (DLIN) assumption on groups with a bilinear map. Our construction relies on a combination of several tools, including the Groth-Ostrovsky-Sahai NIZK and NIWI [EUROCRYPT &#x27;06, CRYPTO &#x27;06, JACM &#x27;12], ``sometimes-binding statistically hiding commitments&#x27;&#x27; [Kalai-Khurana-Sahai, EUROCRYPT &#x27;18] and the ``MPC-in-the-head&#x27;&#x27; technique [Ishai-Kushilevitz-Ostrovsky-Sahai, STOC &#x27;07].

  匹配依据：MPC: mpc (context)

  </details>

- **Secure Non-interactive Simulation: Feasibility &amp; Rate**
  2020-02-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/252)
  Hamidreza Amini Khorasgani, Hemanta K. Maji, Hai H. Nguyen

  <details><summary>摘要 / Abstract</summary>

  A natural solution to increase the efficiency of secure computation will be to non-interactively and securely transform diverse inexpensive-to-generate correlated randomness, like, joint samples from noise sources, into correlations useful for the secure computation while incurring low computational overhead. Motivated by this general application for secure computation, our work introduces the notion of \textit{secure non-interactive simulation} (SNIS). Parties receive samples of correlated randomness, and they, without any interaction, securely convert them into samples from another correlated randomness. SNIS is an extension of \textit{non-interactive simulation of joint distributions} (NIS), and \textit{non-interactive correlation distillation} (NICD) to the cryptographic context. It is a non-interactive version of \textit{one-way secure computation} (OWSC). Our work presents a simulation-based security definition for SNIS and initiates the study of the feasibility and efficiency of SNIS. We also study SNIS among fundamental correlated randomnesses like random samples from the binary symmetric and binary erasure channels, represented by BSS and BES, respectively. The impossibility of realizing a BES sample from BSS samples in NIS and OWSC extends to SNIS. Additionally, we prove that a SNIS of BSS sample from BES samples is impossible, which remains an open problem in NIS and OWSC. Next, we prove that a SNIS of a BES$(\varepsilon&#x27;)$ sample (a BES with noise characteristic $\varepsilon&#x27;$) from BES$(\varepsilon)$ is feasible if and only if $(1-\varepsilon&#x27;)=(1-\varepsilon)^k$, for some $k\in N$. In this context, we prove that all SNIS constructions must be linear. Furthermore, if $(1-\varepsilon&#x27;) = (1-\varepsilon)^k$, then the rate of simulating multiple independent BES$(\varepsilon&#x27;)$ samples is at most $1/k$, which is also achievable using (block) linear constructions. Finally, we show that a SNIS of a BSS$(\varepsilon&#x27;)$ sample from BSS$(\varepsilon)$ samples is feasible if and only if $(1-2\varepsilon&#x27;)=(1-2\varepsilon)^k$, for some $k\in N$. Interestingly, there are linear as well as non-linear SNIS constructions. When $(1-2\varepsilon&#x27;)=(1-2\varepsilon)^k$, we prove that the rate of a \textit{perfectly secure} SNIS is at most $1/k$, which is achievable using linear and non-linear constructions. Our results leave open the fascinating problem of determining the rate of \textit{statistically secure} SNIS among BSS samples. Our technical approach algebraizes the definition of SNIS and proceeds via Fourier analysis. Our work develops general analysis methodologies for Boolean functions, explicitly incorporating cryptographic security constraints. Our work also proves strong forms of \textit{statistical-to-perfect security} transformations: one can error-correct a statistically secure SNIS to make it perfectly secure. We show a connection of our research with \textit{homogeneous Boolean functions} and \textit{distance-invariant codes}, which may be of independent interest.

  匹配依据：MPC: secure computation

  </details>

- **MPC for MPC: Secure Computation on a Massively Parallel Computing Architecture**
  2020-02-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/240)
  T-H. Hubert Chan, Kai-Min Chung, Wei-Kai Lin, Elaine Shi

  <details><summary>摘要 / Abstract</summary>

  Massively Parallel Computation (MPC) is a model of computation widely believed to best capture realistic parallel computing architectures such as large-scale MapReduce and Hadoop clusters. Motivated by the fact that many data analytics tasks performed on these platforms involve sensitive user data, we initiate the theoretical exploration of how to leverage MPC architectures to enable efficient, privacy-preserving computation over massive data. Clearly if a computation task does not lend itself to an efficient implementation on MPC even without security, then we cannot hope to compute it efficiently on MPC with security. We show, on the other hand, that any task that can be efficiently computed on MPC can also be securely computed with comparable efficiency. Specifically, we show the following results: • any MPC algorithm can be compiled to a communication-oblivious counterpart while asymp- totically preserving its round and space complexity, where communication-obliviousness ensures that any network intermediary observing the communication patterns learn no information about the secret inputs; • assuming the existence of Fully Homomorphic Encryption with a suitable notion of compact- ness and other standard cryptographic assumptions, any MPC algorithm can be compiled to a secure counterpart that defends against an adversary who controls not only intermediate network routers but additionally up to 1/3 − η fraction of machines (for an arbitrarily small constant η) — moreover, this compilation preserves the round complexity tightly, and preserves the space complexity upto a multiplicative security parameter related blowup. As an initial exploration of this important direction, our work suggests new definitions and proposes novel protocols that blend algorithmic and cryptographic techniques.

  匹配依据：MPC: secure computation

  </details>

- **Computational and Information-Theoretic Two-Source (Non-Malleable) Extractors**
  2020-02-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/259)
  Divesh Aggarwal, Maciej Obremski, João Ribeiro, Mark Simkin, Luisa Siniscalchi

  <details><summary>摘要 / Abstract</summary>

  Two-source non-malleable extractors are pseudorandom objects which extract randomness even when an adversary is allowed to learn the behavior of the extractor on tamperings of the input weak sources, and they have found important applications in non-malleable coding and secret sharing. We begin by asking how hard it is to improve upon the best known constructions of such objects (Chattopadhyay, Goyal, Li, STOC 2016, and Li, STOC 2017). We show that even small improvements to these constructions lead to explicit low-error two-source extractors for very low linear min-entropy, a longstanding open problem in pseudorandomness. Given the result above in the information-theoretic setting, we turn to studying two-source non-malleable extractors in the computational setting, namely in the CRS model first considered in (Garg, Kalai, Khurana, Eurocrypt 2020). We enforce that both the sampling process for the input sources and the tampering functions must be efficient, but we do not necessarily put such a constraint on the adversary distinguishing the output of the extractor from uniform. We obtain results about two-source non-malleable extractors in the CRS model under different types of hardness assumptions: - Under standard assumptions, we show that small improvements upon state-of-the-art statistical two-source non-malleable extractors also yield explicit low-error two-source non-malleable extractors in the CRS model for low min-entropy against computationally unbounded distinguishers. Remarkably, all previous results on computational extractors require much stronger assumptions; - Under a quasi-polynomial hardness assumption, we give explicit constructions of low-error two-source non-malleable extractors in the CRS model with much lower min-entropy requirements than their best statistical counterparts, against a computationally bounded distinguisher; - Assuming the existence of nearly optimal collision-resistant hash functions, we give a simple explicit construction of a low-error two-source non-malleable extractors in the CRS model for very low min-entropy, against a computationally unbounded distinguisher.

  匹配依据：MPC: secret sharing

  </details>

- **Communication Lower Bounds for Perfect Maliciously Secure MPC**
  2020-02-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/251)
  Ivan Damgård, Nikolaj I. Schwartzbach

  <details><summary>摘要 / Abstract</summary>

  We prove a lower bound on the communication complexity of perfect maliciously secure multiparty computation, in the standard model with $n=3t+1$ parties of which $t$ are corrupted. We show that for any $n$ and all large enough $g \in \mathbb{N}$ there exists a Boolean circuit $C$ with $g$ gates, where any perfectly secure protocol implementing $C$ must communicate $\Omega(n g)$ bits. The results easily extends to constructing similar circuits over any fixed finite field. Our results also extend to the case where the threshold $t$ is suboptimal. Namely if $n= 3t+s$ the bound is $\Omega(ng/s)$, which corresponds to known optimizations via packed secret-sharing. Using known techniques, we also show an upper bound that matches the lower bound up to a constant factor (existing upper bounds are a factor $\log n$ off for Boolean circuits).

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Blinder: MPC Based Scalable and Robust Anonymous Committed Broadcast**
  2020-02-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/248)
  Ittai Abraham, Benny Pinkas, Avishay Yanai

  <details><summary>摘要 / Abstract</summary>

  Anonymous Committed Broadcast is a functionality that extends DC-nets and allows a set of clients to privately commit a message to set of servers, which can then simultaneously open all committed messages in a random ordering. Anonymity holds since no one can learn the ordering or the content of the client’s committed message. We present Blinder, the first system that provides a scalable and fully robust solution for anonymous committed broadcast. Blinder maintains both properties of security (anonymity) and robustness (aka. ‘guaranteed output delivery’ or ‘availability’) in the face of a global active (malicious) adversary. Moreover, Blinder is censorship resistant, meaning that a honest client cannot be blocked from participating. Blinder obtains its security and scalability by carefully combining classical and state-of-the-art techniques from the fields of anonymous communication and secure multiparty computation (MPC). In order to demonstrate scalability, we evaluate Blinder with up to 1 million clients, up to 100 servers and a message size of up to 10 kilobytes. In addition, we show that it is a perfect fit to be implemented on a GPU. A GPU based implementation of Blinder with 5 servers, which accepts 1 million clients, incurs a latency of less than 8 minutes; faster by a factor of &gt; 100 than the 3-servers Riposte protocol (SOSP ’15), which is not robust and not censorship resistant; we get an even larger factor when comparing to AsynchroMix and PowerMix (CCS ’19), which are the only constructions that guarantee fairness (or robustness in the online phase).

  匹配依据：MPC: secure multiparty computation

  </details>

- **Black-box use of One-way Functions is Useless for Optimal Fair Coin-Tossing**
  2020-02-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/253)
  Hemanta K. Maji, Mingyuan Wang

  <details><summary>摘要 / Abstract</summary>

  A two-party fair coin-tossing protocol guarantees output delivery to the honest party even when the other party aborts during the protocol execution. Cleve (STOC--1986) demonstrated that a computationally bounded fail-stop adversary could alter the output distribution of the honest party by (roughly) $1/r$ (in the statistical distance) in an $r$-message coin-tossing protocol. An optimal fair coin-tossing protocol ensures that no adversary can alter the output distribution beyond $1/r$. In a seminal result, Moran, Naor, and Segev (TCC--2009) constructed the first optimal fair coin-tossing protocol using (unfair) oblivious transfer protocols. Whether the existence of oblivious transfer protocols is a necessary hardness of computation assumption for optimal fair coin-tossing remains among the most fundamental open problems in theoretical cryptography. The results of Impagliazzo and Luby (FOCS–1989) and Cleve and Impagliazzo (1993) prove that optimal fair coin-tossing implies the necessity of one-way functions&#x27; existence; a significantly weaker hardness of computation assumption compared to the existence of secure oblivious transfer protocols. However, the sufficiency of the existence of one-way functions is not known. Towards this research endeavor, our work proves a black-box separation of optimal fair coin-tossing from the existence of one-way functions. That is, the black-box use of one-way functions cannot enable optimal fair coin-tossing. Following the standard Impagliazzo and Rudich (STOC--1989) approach of proving black-box separations, our work considers any $r$-message fair coin-tossing protocol in the random oracle model where the parties have unbounded computational power. We demonstrate a fail-stop attack strategy for one of the parties to alter the honest party&#x27;s output distribution by $1/\sqrt r$ by making polynomially-many additional queries to the random oracle. As a consequence, our result proves that the $r$-message coin-tossing protocol of Blum (COMPCON--1982) and Cleve (STOC--1986), which uses one-way functions in a black-box manner, is the best possible protocol because an adversary cannot change the honest party&#x27;s output distribution by more than $1/\sqrt r$. Several previous works, for example, Dachman--Soled, Lindell, Mahmoody, and Malkin (TCC--2011), Haitner, Omri, and Zarosim (TCC--2013), and Dachman--Soled, Mahmoody, and Malkin (TCC--2014), made partial progress on proving this black-box separation assuming some restrictions on the coin-tossing protocol. Our work diverges significantly from these previous approaches to prove this black-box separation in its full generality. The starting point is the recently introduced potential-based inductive proof techniques for demonstrating large gaps in martingales in the information-theoretic plain model. Our technical contribution lies in identifying a global invariant of communication protocols in the random oracle model that enables the extension of this technique to the random oracle model.

  匹配依据：MPC: oblivious transfer

  </details>

- **Optimizing Privacy-Preserving Outsourced Convolutional Neural Network Predictions**
  2020-02-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.10944)
  Minghui Li, Sherman S. M. Chow, Shengshan Hu, Yuejing Yan, Chao Shen, Qian Wang

  <details><summary>摘要 / Abstract</summary>

  Convolutional neural network is a machine-learning model widely applied in various prediction tasks, such as computer vision and medical image analysis. Their great predictive power requires extensive computation, which encourages model owners to host the prediction service in a cloud platform. Recent researches focus on the privacy of the query and results, but they do not provide model privacy against the model-hosting server and may leak partial information about the results. Some of them further require frequent interactions with the querier or heavy computation overheads, which discourages querier from using the prediction service. This paper proposes a new scheme for privacy-preserving neural network prediction in the outsourced setting, i.e., the server cannot learn the query, (intermediate) results, and the model. Similar to SecureML (S&amp;P&#x27;17), a representative work that provides model privacy, we leverage two non-colluding servers with secret sharing and triplet generation to minimize the usage of heavyweight cryptography. Further, we adopt asynchronous computation to improve the throughput, and design garbled circuits for the non-polynomial activation function to keep the same accuracy as the underlying network (instead of approximating it). Our experiments on MNIST dataset show that our scheme achieves an average of 122x, 14.63x, and 36.69x reduction in latency compared to SecureML, MiniONN (CCS&#x27;17), and EzPC (EuroS&amp;P&#x27;19), respectively. For the communication costs, our scheme outperforms SecureML by 1.09x, MiniONN by 36.69x, and EzPC by 31.32x on average. On the CIFAR dataset, our scheme achieves a lower latency by a factor of 7.14x and 3.48x compared to MiniONN and EzPC, respectively. Our scheme also provides 13.88x and 77.46x lower communication costs than MiniONN and EzPC on the CIFAR dataset.

  匹配依据：MPC: garbled circuits, secret sharing

  </details>

- **Universal Communication Efficient Quantum Threshold Secret Sharing Schemes**
  2020-02-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.09229)
  Kaushik Senthoor, Pradeep Kiran Sarvepalli

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) is a cryptographic protocol in which a quantum secret is distributed among a number of parties where some subsets of the parties are able to recover the secret while some subsets are unable to recover the secret. In the standard $((k,n))$ quantum threshold secret sharing scheme, any subset of $k$ or more parties out of the total $n$ parties can recover the secret while other subsets have no information about the secret. But recovery of the secret incurs a communication cost of at least $k$ qudits for every qudit in the secret. Recently, a class of communication efficient QSS schemes were proposed which can improve this communication cost to $\frac{d}{d-k+1}$ by contacting $d\geq k$ parties where $d$ is fixed prior to the distribution of shares. In this paper, we propose a more general class of $((k,n))$ quantum secret sharing schemes with low communication complexity. Our schemes are universal in the sense that the combiner can contact any number of parties to recover the secret with communication efficiency i.e. any $d$ in the range $k\leq d\leq n$ can be chosen by the combiner. This is the first such class of universal communication efficient quantum threshold schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Quantum secret sharing using GHZ state qubit positioning and selective qubits strategy for secret reconstruction**
  2020-02-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.09182)
  Farhan Musanna, Sanjeev Kumar

  <details><summary>摘要 / Abstract</summary>

  The work presents a novel quantum secret sharing strategy based on GHZ product state sharing between three parties. The dealer, based on the classical information to be shared, toggles his qubit and shares the product state. The other parties make their Bell measurements and collude to reconstruct the secret. Unlike the other protocols, this protocol does not involve the entire initial state reconstruction, rather uses selective qubits to discard the redundant qubits at the time of reconstruction to decrypt the secret. The protocol also allows for security against malicious attacks by an adversary without affecting the integrity of the secret. The security of the protocol lies in the fact that each party&#x27;s correct announcement of their measurement is required for reconstruction, failing which the reconstruction process is jeopardized, thereby ascertaining the $(3,3)$ scheme which can further be extended for a $(n,n)$ scheme.

  匹配依据：MPC: secret sharing

  </details>

- **Multiparty Reusable Non-Interactive Secure Computation**
  2020-02-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/221)
  Fabrice Benhamouda, Huijia Lin

  <details><summary>摘要 / Abstract</summary>

  Reducing interaction in Multiparty Computation (MPC) is a highly desirable goal in cryptography. It is known that 2-round MPC can be based on the minimal assumption of 2-round Oblivious Transfer (OT) [Benhamouda and Lin, Garg and Srinivasan, EC 2018], and 1-round MPC is impossible in general. In this work, we propose a natural ``hybrid&#x27;&#x27; model, called \textbf{multiparty reusable Non-Interactive Secure Computation Market (mrNISC)}. In this model, parties publish encodings of their private inputs $x_i$ at the beginning, once and for all. Later, any subset $I$ of them can compute \emph{on-the-fly} a function $f$ on their inputs $\vec x_I = {\{x_i\}}_{i \in I}$ by just sending a single message to a stateless evaluator, conveying the result $f(\vec x_I)$ and nothing else. Importantly, the input encodings can be \emph{reused} in any number of on-the-fly computations, and the same classical simulation security guaranteed by multi-round MPC, is achieved. In short, mrNISC has minimal yet ``tractable&#x27;&#x27; interaction pattern. We initiate the study of mrNISC on several fronts. First, we formalize the security of mrNISC protocols in both a UC definition and a game-based definition. Second, we construct mrNISC protocols in the plain model with semi-honest and semi-malicious security based on bilinear groups. Third, we demonstrate the power of mrNISC by showing two applications: non-interactive MPC (NIMPC) with reusable setup and a distributed version of program obfuscation. In addition, at the core of our construction of mrNISC is a witness encryption scheme for a special language that verifies Non-Interactive Zero-Knowledge (NIZK) proofs of the validity of computations over committed values, which we believe is of independent interest.

  匹配依据：MPC: multiparty computation, oblivious transfer, secure computation

  </details>

- **An Easy-to-implement Construction for $(k,n)$-threshold Progressive Visual Secret Sharing Schemes**
  2020-02-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.09125)
  Hong-Bin Chen, Hsiang-Chun Hsu, Justie Su-Tzu Juan

  <details><summary>摘要 / Abstract</summary>

  Visual cryptography encrypts the secret image into $n$ shares (transparency) so that only stacking a qualified number of shares can recover the secret image by the human visual system while no information can be revealed without a large enough number of shares. This paper investigates the $(k,n)$-threshold Visual Secret Sharing (VSS) model, where one can decrypt the original image by stacking at least $k$ shares and get nothing with less than $k$ shares. There are two main approaches in the literature: codebook-based schemes and random-grid-based schemes; the former is the case of this paper. In general, given any positive integers $k$ and $n$, it is not easy to design a valid scheme for the $(k,n)$-threshold VSS model. In this paper, we propose a simple strategy to construct an efficient scheme for the $(k,n)$-threshold VSS model for any positive integers $2\leq k\leq n$. The crucial idea is to establish a seemingly unrelated connection between the $(k,n)$-threshold VSS scheme and a mathematical structure -- the generalized Pascal&#x27;s triangle. This paper improves and extends previous results in four aspects: Our construction offers a unified viewpoint and covers several known results; The resulting scheme has a progressive-viewing property that means the more shares being stacked together the clearer the secret image would be revealed. The proposed scheme can be constructed explicitly and efficiently based on the generalized Pascal&#x27;s triangle without a computer. Performance of the proposed scheme is comparable with known results.

  匹配依据：MPC: secret sharing

  </details>

- **Thresholdizing HashEdDSA: MPC to the Rescue**
  2020-02-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/214)
  Charlotte Bonte, Nigel P. Smart, Titouan Tanguy

  <details><summary>摘要 / Abstract</summary>

  Following recent comments in a NIST document related to threshold cryptographic standards, we examine the case of thresholdizing the HashEdDSA signature scheme. This is a deterministic signature scheme based on Edwards elliptic curves. Unlike DSA, it has a Schnorr like signature equation, which is an advantage for threshold implementations, but it has the disadvantage of having the ephemeral secret obtained by hashing the secret key and the message. We show that one can obtain relatively efficient implementations of threshold HashEdDSA with no modifications to the behaviour of the signing algorithm; we achieve this using a doubly-authenticated bit (daBit) generation protocol tailored for Q2 access structures, that is more efficient than prior work. However, if one was to modify the standard algorithm to use an MPC-friendly hash function, such as Rescue, the performance becomes very fast indeed.

  匹配依据：MPC: mpc (context)

  </details>

- **PrivacyFL: A simulator for privacy-preserving and secure federated learning**
  2020-02-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.08423)
  Vaikkunth Mugunthan, Anton Peraire-Bueno, Lalana Kagal

  <details><summary>摘要 / Abstract</summary>

  Federated learning is a technique that enables distributed clients to collaboratively learn a shared machine learning model while keeping their training data localized. This reduces data privacy risks, however, privacy concerns still exist since it is possible to leak information about the training dataset from the trained model&#x27;s weights or parameters. Setting up a federated learning environment, especially with security and privacy guarantees, is a time-consuming process with numerous configurations and parameters that can be manipulated. In order to help clients ensure that collaboration is feasible and to check that it improves their model accuracy, a real-world simulator for privacy-preserving and secure federated learning is required. In this paper, we introduce PrivacyFL, which is an extensible, easily configurable and scalable simulator for federated learning environments. Its key features include latency simulation, robustness to client departure, support for both centralized and decentralized learning, and configurable privacy and security mechanisms based on differential privacy and secure multiparty computation. In this paper, we motivate our research, describe the architecture of the simulator and associated protocols, and discuss its evaluation in numerous scenarios that highlight its wide range of functionality and its advantages. Our paper addresses a significant real-world problem: checking the feasibility of participating in a federated learning environment under a variety of circumstances. It also has a strong practical impact because organizations such as hospitals, banks, and research institutes, which have large amounts of sensitive data and would like to collaborate, would greatly benefit from having a system that enables them to do so in a privacy-preserving and secure manner.

  匹配依据：MPC: secure multiparty computation

  </details>

- **MACAO: A Maliciously-Secure and Client-Efficient Active ORAM Framework**
  2020-02-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/203)
  Thang Hoang, Jorge Guajardo, Attila A. Yavuz

  <details><summary>摘要 / Abstract</summary>

  Oblivious Random Access Machine (ORAM) allows a client to hide the access pattern and thus, offers a strong level of privacy for data outsourcing. An ideal ORAM scheme is expected to offer desirable properties such as low client bandwidth, low server computation overhead and the ability to compute over encrypted data. S3ORAM (CCS’17) is an efficient active ORAM scheme, which takes advantage of secret sharing to provide ideal properties for data outsourcing such as low client bandwidth, low server computation and low delay. Despite its merits, S3ORAM only offers security in the semi-honest setting. In practice, an ORAM protocol is likely to operate in the presence of malicious adversaries who might deviate from the protocol to compromise the client privacy. In this paper, we propose MACAO, a new multi-server ORAM framework, which offers integrity, access pattern obliviousness against active adversaries, and the ability to perform secure computation over the accessed data. MACAO harnesses authenticated secret sharing techniques and tree-ORAM paradigm to achieve low client communication, efficient server computation, and low storage overhead at the same time. We fully implemented MACAO and conducted extensive experiments in real cloud platforms (Amazon EC2) to validate the performance of MACAO compared with the state-of-the-art. Our results indicate that MACAO can achieve comparable performance to S3ORAM while offering security against malicious adversaries. MACAO is a suitable candidate for integration into distributed file systems with encrypted computation capabilities towards enabling an oblivious functional data outsourcing infrastructure.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Common Information, Matroid Representation, and Secret Sharing for Matroid Ports**
  2020-02-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.08108)
  Michael Bamiloshin, Aner Ben-Efraim, Oriol Farràs, Carles Padró

  <details><summary>摘要 / Abstract</summary>

  Linear information and rank inequalities as, for instance, Ingleton inequality, are useful tools in information theory and matroid theory. Even though many such inequalities have been found, it seems that most of them remain undiscovered. Improved results have been obtained in recent works by using the properties from which they are derived instead of the inequalities themselves. We apply here this strategy to the classification of matroids according to their representations and to the search for bounds on secret sharing for matroid ports.

  匹配依据：MPC: secret sharing

  </details>

- **Black-Box Constructions of Bounded-Concurrent Secure Computation**
  2020-02-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/216)
  Sanjam Garg, Xiao Liang, Omkant Pandey, Ivan Visconti

  <details><summary>摘要 / Abstract</summary>

  We construct a general purpose secure multiparty computation protocol which remains secure under (a-priori) bounded-concurrent composition and makes only black-box use of cryptographic primitives. Prior to our work, constructions of such protocols required non-black-box usage of cryptographic primitives; alternatively, black-box constructions could only be achieved for super-polynomial simulation based notions of security which offer incomparable security guarantees. Our protocol has a constant number of rounds and relies on standard polynomial-hardness assumptions, namely, the existence of semi-honest oblivious transfers and collision-resistant hash functions. Previously, such protocols were not known even under sub-exponential assumptions.

  匹配依据：MPC: secure computation, secure multiparty computation

  </details>

- **Algebraic Extension Ring Framework for Non-Commutative Asymmetric Cryptography**
  2020-02-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.08343)
  Pedro Hecht

  <details><summary>摘要 / Abstract</summary>

  Post-Quantum Cryptography PQC attempts to find cryptographic protocols resistant to attacks using Shors polynomial time algorithm for numerical field problems or Grovers algorithm to find the unique input to a black-box function that produces a particular output value. The use of non-standard algebraic structures like non-commutative or non-associative structures, combined with one-way trapdoor functions derived from combinatorial group theory, are mainly unexplored choices for these new kinds of protocols and overlooked in current PQC solutions. In this paper, we develop an algebraic extension ring framework who could be applied to different asymmetric protocols, i.e. key exchange, key transport, enciphering, digital signature, zero-knowledge authentication, oblivious transfer, secret sharing etc.. A valuable feature is that there is no need for big number libraries as all arithmetic is performed in F256 extension field operations (precisely the AES field). We assume that the new framework is cryptographical secure against strong classical attacks like the sometimes-useful length-based attack, Romankovs linearization attacks and Tsabans algebraic span attack. This statement is based on the non-linear structure of the selected platform which proved to be useful protecting the AES protocol. Otherwise, it could resist post-quantum attacks Grover, Shor and be particularly useful for computational platforms with limited capabilities like USB cryptographic keys or smartcards. Semantic security IND-CCA2 could also be inferred for this new platform.

  匹配依据：MPC: oblivious transfer, secret sharing

  </details>

- **Dynamic Decentralized Functional Encryption**
  2020-02-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/197)
  Jérémy Chotard, Edouard Dufour-Sans, Romain Gay, Duong Hieu Phan, David Pointcheval

  <details><summary>摘要 / Abstract</summary>

  We introduce Dynamic Decentralized Functional Encryption (DDFE), a generalization of Functional Encryption which allows multiple users to join the system dynamically, without relying on a trusted third party or on expensive and interactive Multi-Party Computation protocols. This notion subsumes existing multi-user extensions of Functional Encryption, such as Multi-Input, Multi-Client, and Ad Hoc Multi-Input Functional Encryption. We define and construct schemes for various functionalities which serve as building-blocks for latter primitives and may be useful in their own right, such as a scheme for dynamically computing sums in any Abelian group. These constructions build upon simple primitives in a modular way, and have instantiations from well-studied assumptions, such as DDH or LWE. Our constructions culminate in an Inner-Product scheme for computing weighted sums on aggregated encrypted data, from standard assumptions in prime-order groups in the Random Oracle Model.

  匹配依据：MPC: multi party computation

  </details>

- **An Algebraic Attack on Ciphers with Low-Degree Round Functions: Application to Full MiMC**
  2020-02-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/182)
  Maria Eichlseder, Lorenzo Grassi, Reinhard Lüftenegger, Morten Øygarden, Christian Rechberger, Markus Schofnegger, Qingju Wang

  <details><summary>摘要 / Abstract</summary>

  Algebraically simple PRFs, ciphers, or cryptographic hash functions are becoming increasingly popular, for example due to their attractive properties for MPC and new proof systems (SNARKs, STARKs, among many others). In this paper, we focus on the algebraically simple construction MiMC, which became an attractive cryptanalytic target due to its simplicity, but also due to its use as a baseline in a competition for more recent algorithms exploring this design space. For the first time, we are able to describe key-recovery attacks on all full-round versions of MiMC over GF(2^n), requiring half the code book. In the chosen-ciphertext scenario, recovering the key from this data for the n-bit full version of MiMC takes the equivalent of less than 2^(n - log_2(n) + 1) calls to MiMC and negligible amounts of memory. The attack procedure is a generalization of higher-order differential cryptanalysis, and it is based on two main ingredients. First, we present a higher-order distinguisher which exploits the fact that the algebraic degree of MiMC grows significantly slower than originally believed. Secondly, we describe an approach to turn this distinguisher into a key-recovery attack without guessing the full subkey. Finally, we show that approximately ceil(log_3(2 * R)) more rounds (where R = ceil(n * log_3(2)) is the current number of rounds of MiMC-n/n) can be necessary and sufficient to restore the security against the key-recovery attack presented here. The attack has been practically verified on toy versions of MiMC. Note that our attack does not affect the security of MiMC over prime fields.

  匹配依据：MPC: mpc (context)

  </details>

- **A note on secure multiparty computation via higher residue symbols**
  2020-02-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/183)
  Ignacio Cascudo, Reto Schnyder

  <details><summary>摘要 / Abstract</summary>

  We generalize a protocol by Yu for comparing two integers with relatively small difference in a secure multiparty computation setting. Yu&#x27;s protocol is based on the Legendre symbol. A prime number $p$ is found for which the Legendre symbol $(\cdot \mid p)$ agrees with the sign function for integers in a certain range $\{-N, \ldots, N\} \subset \mathbb{Z}$. This can then be computed efficiently. We generalize this idea to higher residue symbols in cyclotomic rings $\mathbb{Z}[\zeta_r]$ for $r$ a small odd prime. We present a way to determine a prime number $p$ such that the $r$-th residue symbol $(\cdot \mid p)_r$ agrees with a desired function $f\colon A \to \{\zeta_r^0, \ldots, \zeta_r^{r - 1}\}$ on a given small subset $A \subset \mathbb{Z}[\zeta_r]$, when this is possible. We also explain how to efficiently compute the $r$-th residue symbol in a secret shared setting.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Reusable Two-Round MPC from DDH**
  2020-02-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/170)
  James Bartusek, Sanjam Garg, Daniel Masny, Pratyay Mukherjee

  <details><summary>摘要 / Abstract</summary>

  We present a reusable two-round multi-party computation (MPC) protocol from the Decisional Diffie Hellman assumption (DDH). In particular, we show how to upgrade any secure two-round MPC protocol to allow reusability of its first message across multiple computations, using Homomorphic Secret Sharing (HSS) and pseudorandom functions in NC1— each of which can be instantiated from DDH. In our construction, if the underlying two-round MPC protocol is secure against semi-honest adversaries (in the plain model) then so is our reusable two-round MPC protocol. Similarly, if the underlying two-round MPC protocol is secure against malicious adversaries (in the common random/reference string model) then so is our reusable two-round MPC protocol. Previously, such reusable two-round MPC protocols were only known under assumptions on lattices. At a technical level, we show how to upgrade any two-round MPC protocol to a first message succinct two-round MPC protocol, where the first message of the protocol is generated independently of the computed circuit (though it is not reusable). This step uses homomorphic secret sharing (HSS) and low-depth pseudorandom functions. Next, we show a generic transformation that upgrades any first message succinct two-round MPC to allow for reusability of its first message.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Multiparty Homomorphic Encryption (or: On Removing Setup in Multi-Key FHE)**
  2020-02-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/169)
  Prabhanjan Ananth, Abhishek Jain, Zhengzhong Jin

  <details><summary>摘要 / Abstract</summary>

  The notion of threshold multi-key fully homomorphic encryption (TMK-FHE) [Lopez-Alt, Tromer, Vaikuntanathan, STOC&#x27;12] was proposed as a generalization of fully homomorphic encryption to the multiparty setting. In a TMK-FHE scheme for $n$ parties, each party can individually choose a key pair and use it to encrypt its own private input. Given $n$ ciphertexts computed in this manner, the parties can homomorphically evaluate a circuit $C$ over them to obtain a new ciphertext containing the output of $C$, which can then be decrypted via a threshold decryption protocol. The key efficiency property is that the size of the (evaluated) ciphertext is independent of the size of the circuit. TMK-FHE with one-round threshold decryption, first constructed by Mukherjee and Wichs [Eurocrypt&#x27;16], has found several powerful applications in cryptography over the past few years. However, an important drawback of all such TMK-FHE schemes is that they require a common setup which results in applications in the common random string model. To address this concern, we propose a notion of multiparty homomorphic encryption (MHE) that retains the communication efficiency property of TMK-FHE, but sacrifices on the efficiency of final decryption. Specifically, MHE is defined in a similar manner as TMK-FHE, except that the final output computation process performed locally by each party is ``non-compact&#x27;&#x27; in that we allow its computational complexity to depend on the size of the circuit. We observe that this relaxation does not have a significant bearing in many important applications of TMK-FHE. Our main contribution is a construction of MHE from the learning with errors assumption in the plain model. Our scheme can be used to remove the setup in many applications of TMK-FHE. For example, it yields the first construction of low-communication reusable non-interactive MPC in the plain model. To obtain our result, we devise a recursive self-synthesis procedure to transform any ``delayed-function&#x27;&#x27; two-round MPC protocol into an MHE scheme.

  匹配依据：MPC: mpc (context)

  </details>

- **High Performance Logistic Regression for Privacy-Preserving Genome Analysis**
  2020-02-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.05377) · [IACR ePrint](https://eprint.iacr.org/2020/171)
  Martine De Cock, Rafael Dowsley, Anderson C. A. Nascimento, Davis Railsback, Jianwei Shen, Ariel Todoki

  <details><summary>摘要 / Abstract</summary>

  In this paper, we present a secure logistic regression training protocol and its implementation, with a new subprotocol to securely compute the activation function. To the best of our knowledge, we present the fastest existing secure Multi-Party Computation implementation for training logistic regression models on high dimensional genome data distributed across a local area network.

  匹配依据：MPC: secure multi party computation

  </details>

- **Turbo-Aggregate: Breaking the Quadratic Aggregation Barrier in Secure Federated Learning**
  2020-02-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.04156) · [IACR ePrint](https://eprint.iacr.org/2020/167)
  Jinhyun So, Basak Guler, A. Salman Avestimehr

  <details><summary>摘要 / Abstract</summary>

  Federated learning is a distributed framework for training machine learning models over the data residing at mobile devices, while protecting the privacy of individual users. A major bottleneck in scaling federated learning to a large number of users is the overhead of secure model aggregation across many users. In particular, the overhead of the state-of-the-art protocols for secure model aggregation grows quadratically with the number of users. In this paper, we propose the first secure aggregation framework, named Turbo-Aggregate, that in a network with $N$ users achieves a secure aggregation overhead of $O(N\log{N})$, as opposed to $O(N^2)$, while tolerating up to a user dropout rate of $50\%$. Turbo-Aggregate employs a multi-group circular strategy for efficient model aggregation, and leverages additive secret sharing and novel coding techniques for injecting aggregation redundancy in order to handle user dropouts while guaranteeing user privacy. We experimentally demonstrate that Turbo-Aggregate achieves a total running time that grows almost linear in the number of users, and provides up to $40\times$ speedup over the state-of-the-art protocols with up to $N=200$ users. Our experiments also demonstrate the impact of model size and bandwidth on the performance of Turbo-Aggregate.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-preserving collaborative machine learning on genomic data using TensorFlow**
  2020-02-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.04344) · [IACR ePrint](https://eprint.iacr.org/2020/159)
  Cheng Hong, Zhicong Huang, Wen-jie Lu, Hunter Qu, Li Ma, Morten Dahl, Jason Mancuso

  <details><summary>摘要 / Abstract</summary>

  Machine learning (ML) methods have been widely used in genomic studies. However, genomic data are often held by different stakeholders (e.g. hospitals, universities, and healthcare companies) who consider the data as sensitive information, even though they desire to collaborate. To address this issue, recent works have proposed solutions using Secure Multi-party Computation (MPC), which train on the decentralized data in a way that the participants could learn nothing from each other beyond the final trained model. We design and implement several MPC-friendly ML primitives, including class weight adjustment and parallelizable approximation of activation function. In addition, we develop the solution as an extension to TF Encrypted~\citep{dahl2018private}, enabling us to quickly experiment with enhancements of both machine learning techniques and cryptographic protocols while leveraging the advantages of TensorFlow&#x27;s optimizations. Our implementation compares favorably with state-of-the-art methods, winning first place in Track IV of the iDASH2019 secure genome analysis competition.

  匹配依据：MPC: secure multi party computation

  </details>

- **Multi-Source Non-Malleable Extractors and Applications**
  2020-02-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/157)
  Vipul Goyal, Akshayaram Srinivasan, Chenzhi Zhu

  <details><summary>摘要 / Abstract</summary>

  We introduce a natural generalization of two-source non-malleable extractors (Cheragachi and Guruswami, TCC 2014) called as \textit{multi-source non-malleable extractors}. Multi-source non-malleable extractors are special independent source extractors which satisfy an additional non-malleability property. This property requires that the output of the extractor remains close to uniform even conditioned on its output generated by tampering {\it several sources together}. We formally define this primitive, give a construction that is secure against a wide class of tampering functions, and provide applications. More specifically, we obtain the following results: \begin{itemize} \item For any $s \geq 2$, we give an explicit construction of a $s$-source non-malleable extractor for min-entropy $\Omega(n)$ and error $2^{-n^{\Omega(1)}}$ in the {\it overlapping joint tampering model}. This means that each tampered source could depend on any strict subset of all the sources and the sets corresponding to each tampered source could be overlapping in a way that we define. Prior to our work, there were no known explicit constructions that were secure even against disjoint tampering (where the sets are required to be disjoint without any overlap). %Our extractor is pre-image sampleable and hence, gives rise to non-malleable codes against the same tampering family. % \item We show how to efficiently preimage sample given the output of (a variant of) our extractor and this immediately gives rise to a $s$-state non-malleable code secure in the overlapping joint tampering model (via a generalization of the result by Cheragachi and Guruswami). \item We adapt the techniques used in the above construction to give a $t$-out-of-$n$ non-malleable secret sharing scheme (Goyal and Kumar, STOC 2018) for any $t \leq n$ in the \emph{disjoint tampering model}. This is the first general construction of a threshold non-malleable secret sharing (NMSS) scheme in the disjoint tampering model. All prior constructions had a restriction that the size of the tampered subsets could not be equal. \item We further adapt the techniques used in the above construction to give a $t$-out-of-$n$ non-malleable secret sharing scheme (Goyal and Kumar, STOC 2018) for any $t \leq n$ in the \emph{overlapping joint tampering model}. This is the first construction of a threshold NMSS in the overlapping joint tampering model. \item We show that a stronger notion of $s$-source non-malleable extractor that is multi-tamperable against disjoint tampering functions gives a single round network extractor protocol (Kalai et al., FOCS 2008) with attractive features. Plugging in with a new construction of multi-tamperable, 2-source non-malleable extractors provided in our work, we get a network extractor protocol for min-entropy $\Omega(n)$ that tolerates an {\it optimum} number ($t = p-2$) of faulty processors and extracts random bits for {\it every} honest processor. The prior network extractor protocols could only tolerate $t = \Omega(p)$ faulty processors and failed to extract uniform random bits for a fraction of the honest processors. \end{itemize}

  匹配依据：MPC: secret sharing

  </details>

- **Constructing Secure Multi-Party Computation with Identifiable Abort**
  2020-02-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/153)
  Nicholas Brandt, Sven Maier, Tobias Müller, Jörn Müller-Quade

  <details><summary>摘要 / Abstract</summary>

  Composable protocols for Multi-Party Computation that provide security with Identifiable Abort against a dishonest majority require some form of setup, e.g. correlated randomness among the parties. While this is a very useful model, it has the downside that the setup&#x27;s randomness must be programmable, otherwise security becomes provably impossible. Since programmability is more realistic for smaller setups (in terms of number of parties), it is crucial to minimize the correlation complexity (degree of correlation) of the setup&#x27;s randomness. We give a tight tradeoff between the correlation complexity \(\beta\) and the corruption threshold \(t\). Our bounds are strong in that \(\beta\)-wise correlation is sufficient for statistical security while \(\beta-1\)-wise correlation is insufficient even for computational security. In particular, for strong security, i.e., \(t &lt; n\), full \(n\)-wise correlation is necessary. However, for any constant fraction of honest parties, we provide a protocol with constant correlation complexity which tightens the gap between the theoretical model and the setup&#x27;s implementation in the real world. In contrast, previous state-of-the-art protocols require full \(n\)-wise correlation regardless of \(t\).

  匹配依据：MPC: multi party computation, secure multi party computation

  </details>

- **Compressed $\\Sigma$-Protocol Theory and Practical Application to Plug &amp; Play Secure Algorithmics**
  2020-02-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/152)
  Thomas Attema, Ronald Cramer

  <details><summary>摘要 / Abstract</summary>

  Sigma-Protocols provide a well-understood basis for secure algorithmics. Recently, Bulletproofs (Bootle et al., EUROCRYPT 2016, and Bünz et al., S&amp;P 2018) have been proposed as a drop-in replacement in case of zero-knowledge (ZK) for arithmetic circuits, achieving logarithmic communication instead of linear. Its pivot is an ingenious, logarithmic-size proof of knowledge BP for certain quadratic relations. However, reducing ZK for general relations to it forces a somewhat cumbersome ``reinvention&#x27;&#x27; of cryptographic protocol theory. We take a rather different viewpoint and reconcile Bulletproofs with Sigma-Protocol Theory such that (a) simpler circuit ZK is developed within established theory, while (b) achieving exactly the same logarithmic communication. The natural key here is linearization. First, we repurpose BPs as a blackbox compression mechanism for standard Sigma-Protocols handling ZK proofs of general linear relations (on compactly committed secret vectors); our pivot. Second, we reduce the case of general nonlinear relations to blackbox applications of our pivot via a novel variation on arithmetic secret sharing based techniques for Sigma-Protocols (Cramer et al., ICITS 2012). Orthogonally, we enhance versatility by enabling scenarios not previously addressed, e.g., when a secret input is dispersed across several commitments. Standard implementation platforms leading to logarithmic communication follow from a Discrete-Log assumption or a generalized Strong-RSA assumption. Also, under a Knowledge-of-Exponent Assumption (KEA) communication drops to constant, as in ZK-SNARKS. All in all, our theory should more generally be useful for modular (``plug &amp; play&#x27;&#x27;) design of practical cryptographic protocols; this is further evidenced by our separate work (2020) on proofs of partial knowledge.

  匹配依据：MPC: secret sharing

  </details>

- **Efficient Cloud-based Secret Shuffling via Homomorphic Encryption**
  2020-02-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.05231)
  Kilian Becher, Thorsten Strufe

  <details><summary>摘要 / Abstract</summary>

  When working with joint collections of confidential data from multiple sources, e.g., in cloud-based multi-party computation scenarios, the ownership relation between data providers and their inputs itself is confidential information. Protecting data providers&#x27; privacy desires a function for secretly shuffling the data collection. We present the first efficient secure multi-party computation protocol for secret shuffling in scenarios with a central server. Based on a novel approach to random index distribution, our solution enables the randomization of the order of a sequence of encrypted data such that no observer can map between elements of the original sequence and the shuffled sequence with probability better than guessing. It allows for shuffling data encrypted under an additively homomorphic cryptosystem with constant round complexity and linear computational complexity. Being a general-purpose protocol, it is of relevance for a variety of practical use cases.

  匹配依据：MPC: multi party computation, secure multi party computation

  </details>

- **Stacked Garbling for Disjunctive Zero-Knowledge Proofs**
  2020-02-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/136)
  David Heath, Vladimir Kolesnikov

  <details><summary>摘要 / Abstract</summary>

  Zero-knowledge (ZK) proofs receive wide attention, especially with respect to non-interactivity, small proof size, and fast verification. We instead focus on fast total proof time, in particular for large Boolean circuits. Under this metric, Garbled Circuit (GC)-based ZK, originally proposed by Jawurek et al. ([JKO], CCS 2013), remains state-of-the-art due to the low-constant linear scaling of garbling. We improve GC-ZK for proof statements with conditional clauses. Our communication is proportional to the longest clause rather than to the entire proof statement. This is most useful when the number of branches $m$ is large, resulting in up to $m\times$ communication improvement over JKO. In our proof-of-concept illustrative application, the prover demonstrates knowledge of a bug in a codebase consisting of any number of snippets of C code. Our computation cost is linear in the size of the codebase and communication is constant in the number of snippets. That is, we require only enough communication for the single largest snippet! Our conceptual contribution is stacked garbling for ZK, a privacy-free circuit garbling scheme that, when used with the JKO GC-ZK protocol, constructs efficient ZK proofs. Given a Boolean circuit $C$ and computational security parameter $\kappa$, our garbling is $L\kappa$ bits long, where $L$ is the length of the longest execution path in $C$. All prior concretely efficient garbling schemes produce garblings of size $|C|\kappa$. The computational cost of our scheme is not increased over prior state-of-the-art. We implemented our technique and demonstrate significantly improved performance. For functions with branching factor $m$, we improve communication by $m\times$ compared to JKO. Compared with recent systems (STARK, Libra, KKW, Ligero, Aurora, Bulletproofs), our scheme offers better proof times for large circuits: $35-1000\times$ or more, depending on circuit size and on the compared scheme. For our illustrative application, we consider four C code snippets. Each snippet has 30-50 LOC; one snippet allows an invalid memory dereference. The entire proof takes 0.15 seconds and communicates 1.5 MB.

  匹配依据：MPC: garbled circuit, garbling scheme, garbling schemes

  </details>

- **Non-Malleability against Polynomial Tampering**
  2020-02-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/147)
  Marshall Ball, Eshan Chattopadhyay, Jyun-Jie Liao, Tal Malkin, Li-Yang Tan

  <details><summary>摘要 / Abstract</summary>

  We present the first explicit construction of a non-malleable code that can handle tampering functions that are bounded-degree polynomials. Prior to our work, this was only known for degree-1 polynomials (affine tampering functions), due to Chattopadhyay and Li (STOC 2017). As a direct corollary, we obtain an explicit non-malleable code that is secure against tampering by bounded-size arithmetic circuits. We show applications of our non-malleable code in constructing non-malleable secret sharing schemes that are robust against bounded-degree polynomial tampering. In fact our result is stronger: we can handle adversaries that can adaptively choose the polynomial tampering function based on initial leakage of a bounded number of shares. Our results are derived from explicit constructions of seedless non-malleable extractors that can handle bounded-degree polynomial tampering functions. Prior to our work, no such result was known even for degree-2 (quadratic) polynomials.

  匹配依据：MPC: secret sharing

  </details>

- **Malicious Security Comes Free in Honest-Majority MPC**
  2020-02-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/134)
  Vipul Goyal, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  We study the communication complexity of unconditionally secure MPC over point-to-point channels for corruption threshold t &lt; n/2. We ask the question: &quot;is it possible to achieve security-with-abort with the same concrete cost as the best-known semi-honest MPC protocol?&quot; While a number of works have focused on improving the concrete efficiency in this setting, the answer to the above question has remained elusive until now. We resolve the above question in the affirmative by providing a secure-with-abort MPC protocol with the same cost per gate as the best-known semi-honest protocol. Concretely, our protocol only needs 5.5 field elements per multiplication gate per party which matches (and even improves upon) the corresponding cost of the best known protocol in the semi-honest setting by Damgard and Nielsen. Previously best-known maliciously secure (with abort) protocols require 12 field elements. An additional feature of our protocol is its conceptual simplicity.

  匹配依据：MPC: mpc (context)

  </details>

- **Going Beyond Dual Execution: MPC for Functions with Efficient Verification**
  2020-02-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/139)
  Carmit Hazay, abhi shelat, Muthuramakrishnan Venkitasubramaniam

  <details><summary>摘要 / Abstract</summary>

  The dual execution paradigm of Mohassel and Franklin (PKC&#x27;06) and Huang, Katz and Evans (IEEE &#x27;12) shows how to achieve the notion of 1-bit leakage security at roughly twice the cost of semi-honest security for the special case of two-party secure computation. To date, there are no multi-party computation (MPC) protocols that offer such a strong trade-off between security and semi-honest performance. Our main result is to address this shortcoming by designing 1-bit leakage protocols for the multi-party setting, albeit for a special class of functions. We say that function f(x,y) is efficiently verifiable by g if the running time of g is always smaller than f and g(x,y,z)=1 if and only if f(x,y)=z. In the two-party setting, we first improve dual execution by observing that the ``second execution&#x27;&#x27; can be an evaluation of g instead of f, and that by definition, the evaluation of g is asymptotically more efficient. Our main MPC result is to construct a 1-bit leakage protocol for such functions from any passive protocol for f that is secure up to additive errors and any active protocol for g. An important result by Genkin et al. (STOC &#x27;14) shows how the classic protocols by Goldreich et al. (STOC &#x27;87) and Ben-Or et al. (STOC &#x27;88) naturally support this property, which allows to instantiate our compiler with two-party and multi-party protocols. A key technical result we prove is that the passive protocol for distributed garbling due to Beaver et al. (STOC &#x27;90) is in fact secure up to additive errors against malicious adversaries, thereby, yielding another powerful instantiation of our paradigm in the constant-round multi-party setting. As another concrete example of instantiating our approach, we present a novel protocol for computing perfect matching that is secure in the 1-bit leakage model and whose communication complexity is less than the honest-but-curious implementations of textbook algorithms for perfect matching.

  匹配依据：MPC: multi party computation, secure computation

  </details>

- **Communication Efficient Secret Sharing in the Presence of Malicious Adversary**
  2020-02-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.03374)
  Rawad Bitar, Sidharth Jaggi

  <details><summary>摘要 / Abstract</summary>

  Consider the communication efficient secret sharing problem. A dealer wants to share a secret with $n$ parties such that any $k\leq n$ parties can reconstruct the secret and any $z&lt;k$ parties eavesdropping on their shares obtain no information about the secret. In addition, a legitimate user contacting any $d$, $k\leq d \leq n$, parties to decode the secret can do so by reading and downloading the minimum amount of information needed. We are interested in communication efficient secret sharing schemes that tolerate the presence of malicious parties actively corrupting their shares and the data delivered to the users. The knowledge of the malicious parties about the secret is restricted to the shares they obtain. We characterize the capacity, i.e. maximum size of the secret that can be shared. We derive the minimum amount of information needed to to be read and communicated to a legitimate user to decode the secret from $d$ parties, $k\leq d \leq n$. Error-correcting codes do not achieve capacity in this setting. We construct codes that achieve capacity and achieve minimum read and communication costs for all possible values of $d$. Our codes are based on Staircase codes, previously introduced for communication efficient secret sharing, and on the use of a pairwise hashing scheme used in distributed data storage and network coding settings to detect errors inserted by a limited knowledge adversary.

  匹配依据：MPC: secret sharing

  </details>

- **Separating Two-Round Secure Computation from Oblivious Transfer**
  2020-02-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/116)
  Benny Applebaum, Zvika Brakerski, Sanjam Garg, Yuval Ishai, Akshayaram Srinivasan

  <details><summary>摘要 / Abstract</summary>

  We consider the question of minimizing the round complexity of protocols for secure multiparty computation (MPC) with security against an arbitrary number of semi-honest parties. Very recently, Garg and Srinivasan (Eurocrypt 2018) and Benhamouda and Lin (Eurocrypt 2018) constructed such 2-round MPC protocols from minimal assumptions. This was done by showing *a round preserving reduction* to the task of secure *2-party* computation of the oblivious transfer functionality (OT). These constructions made a novel non-black-box use of the underlying OT protocol. The question remained whether this can be done by only making black-box use of 2-round OT. This is of theoretical and potentially also practical value as black-box use of primitives tends to lead to more efficient constructions. Our main result proves that such a black-box construction is impossible, namely that non-black-box use of OT is necessary. As a corollary, a similar separation holds when starting with any 2-party functionality other than OT. As a secondary contribution, we prove several additional results that further clarify the landscape of black-box MPC with minimal interaction. In particular, we complement the separation from 2-party functionalities by presenting a complete 4-party functionality, give evidence for the difficulty of ruling out a complete 3-party functionality and for the difficulty of ruling out black-box constructions of 3-round MPC from 2-round OT, and separate a relaxed ``non-compact&#x27;&#x27; variant of 2-party *secret sharing* from 2-round OT.

  匹配依据：MPC: oblivious transfer, secret sharing, secure 2 party computation, secure computation, secure multiparty computation

  </details>

- **Secure Social Recommendation based on Secret Sharing**
  2020-02-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.02088)
  Chaochao Chen, Liang Li, Bingzhe Wu, Cheng Hong, Li Wang, Jun Zhou

  <details><summary>摘要 / Abstract</summary>

  Nowadays, privacy preserving machine learning has been drawing much attention in both industry and academy. Meanwhile, recommender systems have been extensively adopted by many commercial platforms (e.g. Amazon) and they are mainly built based on user-item interactions. Besides, social platforms (e.g. Facebook) have rich resources of user social information. It is well known that social information, which is rich on social platforms such as Facebook, are useful to recommender systems. It is anticipated to combine the social information with the user-item ratings to improve the overall recommendation performance. Most existing recommendation models are built based on the assumptions that the social information are available. However, different platforms are usually reluctant to (or cannot) share their data due to certain concerns. In this paper, we first propose a SEcure SOcial RECommendation (SeSoRec) framework which can (1) collaboratively mine knowledge from social platform to improve the recommendation performance of the rating platform, and (2) securely keep the raw data of both platforms. We then propose a Secret Sharing based Matrix Multiplication (SSMM) protocol to optimize SeSoRec and prove its correctness and security theoretically. By applying minibatch gradient descent, SeSoRec has linear time complexities in terms of both computation and communication. The comprehensive experimental results on three real-world datasets demonstrate the effectiveness of our proposed SeSoRec and SSMM.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy Preserving PCA for Multiparty Modeling**
  2020-02-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.02091)
  Yingting Liu, Chaochao Chen, Longfei Zheng, Li Wang, Jun Zhou, Guiquan Liu, Shuang Yang

  <details><summary>摘要 / Abstract</summary>

  In this paper, we present a general multiparty modeling paradigm with Privacy Preserving Principal Component Analysis (PPPCA) for horizontally partitioned data. PPPCA can accomplish multiparty cooperative execution of PCA under the premise of keeping plaintext data locally. We also propose implementations using two techniques, i.e., homomorphic encryption and secret sharing. The output of PPPCA can be sent directly to data consumer to build any machine learning models. We conduct experiments on three UCI benchmark datasets and a real-world fraud detection dataset. Results show that the accuracy of the model built upon PPPCA is the same as the model with PCA that is built based on centralized plaintext data.

  匹配依据：MPC: secret sharing

  </details>

- **LegRoast: Efficient post-quantum signatures from the Legendre PRF**
  2020-02-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/128)
  Ward Beullens, Cyprien Delpech de Saint Guilhem

  <details><summary>摘要 / Abstract</summary>

  We introduce an efficient post-quantum signature scheme that relies on the one-wayness of the Legendre PRF. This &quot;LEGendRe One-wAyness SignaTure&quot; (LegRoast) builds upon the MPC-in-the-head technique to construct an efficient zero-knowledge proof, which is then turned into a signature scheme with the Fiat-Shamir transform. Unlike many other Fiat-Shamir signatures, the security of LegRoast can be proven without using the forking lemma, and this leads to a tight (classical) ROM proof. We also introduce a generalization that relies on the one-wayness of higher-power residue characters; the &quot;POwer Residue ChaRacter One-wAyness SignaTure&quot; (PorcRoast). LegRoast outperforms existing MPC-in-the-head-based signatures (most notably Picnic/Picnic2) in terms of signature size and speed. Moreover, PorcRoast outperforms LegRoast by a factor of 2 in both signature size and signing time. For example, one of our parameter sets targeting NIST security level I results in a signature size of 7.2 KB and a signing time of 2.8ms. This makes PorcRoast the most efficient signature scheme based on symmetric primitives in terms of signature size and signing time.

  匹配依据：MPC: mpc (context)

  </details>

- **InfoCommit: Information-Theoretic Polynomial Commitment and Verification**
  2020-02-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/118)
  Saeid Sahraei, Salman Avestimehr

  <details><summary>摘要 / Abstract</summary>

  We introduce InfoCommit, a protocol for polynomial commitment and verification. InfoCommit consists of two phases. An initial commitment phase and an evaluation phase. During the commitment phase, the verifier and the prover engage in a private two-party computation algorithm so that the verifier extracts a private verification key. In the evaluation phase, the verifier is interested in learning the evaluations of the polynomial at several input points. InfoCommit has four main features. Firstly, the verifier is able to detect, with high probability, if the prover has responded with evaluations of the same polynomial that he has initially committed to. Secondly, InfoCommit provides rigorous privacy guarantees for the prover: upon observing the initial commitment and the response provided by the prover to $m$ evaluation requests, the verifier only learns $O(m^2)$ symbols about the coefficients of the polynomial. Thirdly, the verifiability guarantee is unconditional and without the need for a trusted party, while ``bounded storage&quot; is the only assumption underlying the privacy of the algorithm. In particular, both properties hold regardless of the computation power of the two parties. Lastly, InfoCommit is doubly-efficient in the sense that in the evaluation phase, the verifier runs in $O(\sqrt{d})$ and the prover runs in $O(d)$, where $d-1$ is the degree of the polynomial.

  匹配依据：MPC: two party computation

  </details>

- **Knowledge Federation: A Unified and Hierarchical Privacy-Preserving AI Framework**
  2020-02-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.01647)
  Hongyu Li, Dan Meng, Hong Wang, Xiaolin Li

  <details><summary>摘要 / Abstract</summary>

  With strict protections and regulations of data privacy and security, conventional machine learning based on centralized datasets is confronted with significant challenges, making artificial intelligence (AI) impractical in many mission-critical and data-sensitive scenarios, such as finance, government, and health. In the meantime, tremendous datasets are scattered in isolated silos in various industries, organizations, different units of an organization, or different branches of an international organization. These valuable data resources are well underused. To advance AI theories and applications, we propose a comprehensive framework (called Knowledge Federation - KF) to address these challenges by enabling AI while preserving data privacy and ownership. Beyond the concepts of federated learning and secure multi-party computation, KF consists of four levels of federation: (1) information level, low-level statistics and computation of data, meeting the requirements of simple queries, searching and simplistic operators; (2) model level, supporting training, learning, and inference; (3) cognition level, enabling abstract feature representation at various levels of abstractions and contexts; (4) knowledge level, fusing knowledge discovery, representation, and reasoning. We further clarify the relationship and differentiation between knowledge federation and other related research areas. We have developed a reference implementation of KF, called iBond Platform, to offer a production-quality KF platform to enable industrial applications in finance, insurance et al. The iBond platform will also help establish the KF community and a comprehensive ecosystem and usher in a novel paradigm shift towards secure, privacy-preserving and responsible AI. As far as we know, knowledge federation is the first hierarchical and unified framework for secure multi-party computing and learning.

  匹配依据：MPC: secure multi party computation, secure multi party computing

  </details>

- **Weight distributions of several families of 3-weight binary linear codes**
  2020-02-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.01853)
  Fei Li, Xiumei Li

  <details><summary>摘要 / Abstract</summary>

  The linear codes with a few weights have been applied widely in combinatorial designs, secret sharing, association schemes, authentication codes and strongly regular graphs. In this paper, we first correct an erroneous result about the exponential sum $\sum_{x\in \mathbb{F}_{2^{e}}}χ_1\left(ax^{2^α+1}+bx\right).$ Then, using the above exponential sum, we construct several families of binary linear codes of $3$-weight and determine their weight distributions. Moreover, Most of them can be used in secret sharing schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Blazing Fast OT for Three-Round UC OT Extension**
  2020-02-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/110)
  Ran Canetti, Pratik Sarkar, Xiao Wang

  <details><summary>摘要 / Abstract</summary>

  Oblivious Transfer (OT) is an important building block for multi-party computation (MPC). Since OT requires expensive public-key operations, efficiency-conscious MPC protocols use an OT extension (OTE) mechanism [Beaver 96, Ishai et al. 03] to provide the functionality of many independent OT instances with the same sender and receiver, using only symmetric-key operations plus few instances of some base OT protocol. Consequently there is significant interest in constructing OTE friendly protocols, namely protocols that, when used as base-OT for OTE, result in extended OT that are both round-efficient and cost-efficient. We present the most efficient OTE-friendly protocol to date. Specifically: - Our base protocol incurs only 3 exponentiations per instance. - Our base protocol results in a 3 round extended OT protocol. - The extended protocol is UC secure in the Observable Random Oracle Model (ROM) under the CDH assumption. For comparison, the state of the art for base OTs that result in 3-round OTE are proven only in the programmable ROM, and require 4 exponentiations under Interactive DDH or 6 exponentiations under DDH [Masney-Rindal 19]. We also implement our protocol and benchmark it against the Simplest OT protocol [Chou and Orlandi, Latincrypt 2015], which is the most efficient and widely used OT protocol but not known to suffice for OTE. The computation cost is roughly the same in both cases. Interestingly, our base OT is also 3 rounds. However, we slightly modify the extension mechanism (which normally adds a round) so as to preserve the number of rounds in our case.

  匹配依据：MPC: multi party computation, oblivious transfer

  </details>

- **CryptoSPN: Privacy-preserving Sum-Product Network Inference**
  2020-02-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.00801)
  Amos Treiber, Alejandro Molina, Christian Weinert, Thomas Schneider, Kristian Kersting

  <details><summary>摘要 / Abstract</summary>

  AI algorithms, and machine learning (ML) techniques in particular, are increasingly important to individuals&#x27; lives, but have caused a range of privacy concerns addressed by, e.g., the European GDPR. Using cryptographic techniques, it is possible to perform inference tasks remotely on sensitive client data in a privacy-preserving way: the server learns nothing about the input data and the model predictions, while the client learns nothing about the ML model (which is often considered intellectual property and might contain traces of sensitive data). While such privacy-preserving solutions are relatively efficient, they are mostly targeted at neural networks, can degrade the predictive accuracy, and usually reveal the network&#x27;s topology. Furthermore, existing solutions are not readily accessible to ML experts, as prototype implementations are not well-integrated into ML frameworks and require extensive cryptographic knowledge. In this paper, we present CryptoSPN, a framework for privacy-preserving inference of sum-product networks (SPNs). SPNs are a tractable probabilistic graphical model that allows a range of exact inference queries in linear time. Specifically, we show how to efficiently perform SPN inference via secure multi-party computation (SMPC) without accuracy degradation while hiding sensitive client and training information with provable security guarantees. Next to foundations, CryptoSPN encompasses tools to easily transform existing SPNs into privacy-preserving executables. Our empirical results demonstrate that CryptoSPN achieves highly efficient and accurate inference in the order of seconds for medium-sized SPNs.

  匹配依据：MPC: secure multi party computation

  </details>

- **A Quantum-based Database Query Scheme for Privacy Preservation in Cloud Environment**
  2020-02-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2002.00192)
  Wenjie Liu, Peipei Gao, Zhihao Liu, Hanwu Chen, Maojun Zhang

  <details><summary>摘要 / Abstract</summary>

  Cloud computing is a powerful and popular information technology paradigm that enables data service outsourcing and provides higher-level services with minimal management effort. However, it is still a key challenge to protect data privacy when a user accesses the sensitive cloud data. Privacy-preserving database query allows the user to retrieve a data item from the cloud database without revealing the information of the queried data item, meanwhile limiting user&#x27;s ability to access other ones. In this study, in order to achieve the privacy preservation and reduce the communication complexity, a quantum-based database query scheme for privacy preservation in cloud environment is developed. Specifically, all the data items of the database are firstly encrypted by different keys for protecting server&#x27;s privacy, and in order to guarantee the clients&#x27; privacy, the server is required to transmit all these encrypted data items to the client with the oblivious transfer strategy. Besides, two oracle operations, a modified Grover iteration, and a special offset encryption mechanism are combined together to ensure that the client can correctly query the desirable data item. Finally, performance evaluation is conducted to validate the correctness, privacy, and efficiency of our proposed scheme.

  匹配依据：MPC: oblivious transfer

  </details>

- **SecEL: Privacy-Preserving, Verifiable and Fault-Tolerant Edge Learning for Autonomous Vehicles**
  2020-01-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2001.09624)
  Jiasi Weng, Jian Weng, Yue Zhang, Ming Li, Zhaodi Wen

  <details><summary>摘要 / Abstract</summary>

  Mobile edge computing (MEC) is an emerging technology to transform the cloud-based computing services into the edge-based ones. Autonomous vehicular network (AVNET), as one of the most promising applications of MEC, can feature edge learning and communication techniques, improving the safety for autonomous vehicles (AVs). This paper focuses on the edge learning in AVNET, where AVs at the edge of the network share model parameters instead of data in a distributed manner, and an aggregator (e.g., a base station) aggregates parameters from AVs and at the end obtains a trained model. Despite promising, security issues, such as data leakage, computing integrity invasion and fault connection in existing edge learning cases are not considered fully. To the best of our knowledge, there lacks an effective scheme simultaneously covering the foregoing security issues. Therefore, we propose \textit{SecEL}, a privacy-preserving, verifiable and fault-tolerant scheme for edge learning in AVNET. First, we leverage the primitive of bivariate polynomial-based secret sharing to encrypt model parameters by one-time padding. Second, we use homomorphic authenticator based on message authentication code to support verifiable computation. Third, we mitigate the computation failure problem caused by fault connection. Last, we simulate and evaluate SecEL in terms of time cost, throughput and classification accuracy. The experiment results demonstrate the effectiveness of SecEL.

  匹配依据：MPC: secret sharing

  </details>

- **Agile and versatile quantum communication: signatures and secrets**
  2020-01-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2001.10089)
  Stefan Richter, Matthew Thornton, Imran Khan, Hannah Scott, Kevin Jaksch, Ulrich Vogl, Birgit Stiller, Gerd Leuchs, Christoph Marquardt, Natalia Korolkova

  <details><summary>摘要 / Abstract</summary>

  Agile cryptography allows for a resource-efficient swap of a cryptographic core in case the security of an underlying classical cryptographic algorithm becomes compromised. Conversely, versatile cryptography allows the user to switch the cryptographic task without requiring any knowledge of its inner workings. In this paper, we suggest how these related principles can be applied to the field of quantum cryptography by explicitly demonstrating two quantum cryptographic protocols, quantum digital signatures (QDS) and quantum secret sharing (QSS), on the same hardware sender and receiver platform. Crucially, the protocols differ only in their classical post-processing. The system is also suitable for quantum key distribution (QKD) and is highly compatible with deployed telecommunication infrastructures, since it uses standard quadrature phase shift keying (QPSK) encoding and heterodyne detection. For the first time, QDS protocols are modified to allow for postselection at the receiver, enhancing protocol performance. The cryptographic primitives QDS and QSS are inherently multipartite and we prove that they are secure not only when a player internal to the task is dishonest, but also when (external) eavesdropping on the quantum channel is allowed. In our first proof-of-principle demonstration of an agile and versatile quantum communication system, the quantum states were distributed at GHz rates. This allows for a one-bit message to be securely signed using our QDS protocols in less than 0.05 ms over a 2 km fiber link and in less than 0.2~s over a 20 km fiber link. To our knowledge, this also marks the first demonstration of a continuous-variable direct QSS protocol.

  匹配依据：MPC: secret sharing

  </details>

- **Weight distributions and weight hierarchies of two classes of binary linear codes**
  2020-01-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2001.08875)
  Fei Li, Xiumei Li

  <details><summary>摘要 / Abstract</summary>

  Linear codes with a few weights can be applied to communication, consumer electronics and data storage system. In addition, the weight hierarchy of linear codes has many applications such as on the type II wire-tap channel, dealing with $t$-resilient functions and trellis or branch complexity of linear codes and so on. In this paper, we first present a formula for computing the weight hierarchies of linear codes constructed by the generalized method of defining sets. Then, we construct two classes of binary linear codes with a few weights and determine their weight distributions and weight hierarchies completely. Some codes of them can be used in secret sharing schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Locally Decodable Codes with Randomized Encoding**
  2020-01-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2001.03692) · [IACR ePrint](https://eprint.iacr.org/2020/031)
  Kuan Cheng, Xin Li, Yu Zheng

  <details><summary>摘要 / Abstract</summary>

  We initiate a study of locally decodable codes with randomized encoding. Standard locally decodable codes are error correcting codes with a deterministic encoding function and a randomized decoding function, such that any desired message bit can be recovered with good probability by querying only a small number of positions in the corrupted codeword. This allows one to recover any message bit very efficiently in sub-linear or even logarithmic time. Besides this straightforward application, locally decodable codes have also found many other applications such as private information retrieval, secure multiparty computation, and average-case complexity. However, despite extensive research, the tradeoff between the rate of the code and the number of queries is somewhat disappointing. For example, the best known constructions still need super-polynomially long codeword length even with a logarithmic number of queries, and need a polynomial number of queries to achieve a constant rate. In this paper, we show that by using a randomized encoding, in several models we can achieve significantly better rate-query tradeoff. In addition, our codes work for both the standard Hamming errors, and the more general and harder edit errors.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Quantum Advantage for Shared Randomness Generation**
  2020-01-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2001.01889)
  Tamal Guha, Mir Alimuddin, Sumit Rout, Amit Mukherjee, Some Sankar Bhattacharya, Manik Banik

  <details><summary>摘要 / Abstract</summary>

  Sharing correlated random variables is a resource for a number of information theoretic tasks such as privacy amplification, simultaneous message passing, secret sharing and many more. In this article, we show that to establish such a resource called shared randomness, quantum systems provide an advantage over their classical counterpart. Precisely, we show that appropriate albeit fixed measurements on a shared two-qubit state can generate correlations which cannot be obtained from any possible state on two classical bits. In a resource theoretic set-up, this feature of quantum systems can be interpreted as an advantage in winning a two players co-operative game, which we call the `non-monopolize social subsidy&#x27; game. It turns out that the quantum states leading to the desired advantage must possess non-classicality in the form of quantum discord. On the other hand, while distributing such sources of shared randomness between two parties via noisy channels, quantum channels with zero capacity as well as with classical capacity strictly less than unity perform more efficiently than the perfect classical channel. Protocols presented here are noise-robust and hence should be realizable with state-of-the-art quantum devices.

  匹配依据：MPC: secret sharing

  </details>

- **Secret Sharing Schemes for Ports of Matroids of Rank 3**
  2020-01-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/008)
  Oriol Farràs

  <details><summary>摘要 / Abstract</summary>

  A secret sharing scheme is ideal if the size of each share is equal to the size of the secret. Brickell and Davenport showed that the access structure of an ideal secret sharing scheme is determined by a matroid. Namely, the minimal authorized subsets of an ideal secret sharing scheme are in correspondence with the circuits of a matroid containing a fixed point. In this case, we say that the access structure is a matroid port. It is known that, for an access structure, being a matroid port is not a sufficient condition to admit an ideal secret sharing scheme. In this work we present a linear secret sharing scheme construction for ports of matroids of rank 3 in which the size of each share is at most $n$ times the size of the secret. Using the previously known secret sharing constructions, the size of each share was $O(n^2/\log n)$ the size of the secret. Our construction is extended to ports of matroids of any rank $k\geq 2$, obtaining secret sharing schemes in which the size of each share is at most $n^{k-2}$ times the size of the secret. This work is complemented by presenting lower bounds: There exist matroid ports that require $(F_q,\ell)$-linear secret schemes with total information ratio $\Omega(2^{n/2}/\ell n^{3/4}\sqrt{\log q})$.

  匹配依据：MPC: secret sharing

  </details>

- **Expand-and-Randomize: An Algebraic Approach to Secure Computation**
  2020-01-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2001.00539)
  Yizhou Zhao, Hua Sun

  <details><summary>摘要 / Abstract</summary>

  We consider the secure computation problem in a minimal model, where Alice and Bob each holds an input and wish to securely compute a function of their inputs at Carol without revealing any additional information about the inputs. For this minimal secure computation problem, we propose a novel coding scheme built from two steps. First, the function to be computed is expanded such that it can be recovered while additional information might be leaked. Second, a randomization step is applied to the expanded function such that the leaked information is protected. We implement this expand-and-randomize coding scheme with two algebraic structures - the finite field and the modulo ring of integers, where the expansion step is realized with the addition operation and the randomization step is realized with the multiplication operation over the respective algebraic structures.

  匹配依据：MPC: secure computation

  </details>
