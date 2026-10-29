# 2022 · MPC · 仅预印本来源 · 第 4/4 页

[总目录](../PAPERS.md) · [上一页](2022-mpc-preprint-03.md)

- **PFE: Linear Active Security, Double-Shuffle Proofs, and Low-Complexity Communication**
  2022-02-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/219)
  Hanyu Jia, Xiangxue Li

  <details><summary>摘要 / Abstract</summary>

  We consider private function evaluation (PFE) in malicious adversary model. Current state-of-the-art in PFE from Valiant&#x27;s universal circuits (Liu, Yu, et al., CRYPTO 2021) does not avoid the logarithmic factor in circuit size. In constructing linear active PFE, one essential building block is to prove the correctness of an extended permutation (EP, Mohassel and Sadeghian at EUROCRYPT 2013) by zero-knowledge protocols with linear complexity. The linear instantiation $\mathcal{ZK}_{EP}$ by Mohassel, Sadeghian, and Smart (ASIACRYPT 2014) is a three-phase protocol, and each phase (dummy placement, replication, and permutation) is of size $2g$. Its overhead thus seems really outrageous, reducing its practicability. We present in this paper a novel and efficient framework $\mathcal{ZK}_{DS}$ for proving the correct EP. We show that \underline{d}ouble \underline{s}huffles suffice for EP (exponentiations and communication overheads are about 27% and 31% of $\mathcal{ZK}_{EP}$, respectively). Data owner(s) generates the randomness for the first shuffle whose outputs determine outgoing wires of the circuit defined by the function. Function owner reuses and extends the randomness in the second shuffle whose outputs determine the incoming wires. From $\mathcal{ZK}_{DS}$, we build an online/offline PFE framework with linear active security. The online phase could be instantiated by any well-studied secure function evaluation (SFE) with linear active security (e.g., Tiny-OT at CRYPTO 2012). The offline phase depends only on the private function $f$ and uses $\mathcal{ZK}_{DS}$ to prove the EP relationship between outgoing wires and incoming wires in the circuit $\mathcal{C}_f$ derived from $f$.

  匹配依据：MPC: secure function evaluation

  </details>

- **Multi-Client Functional Encryption with Fine-Grained Access Control**
  2022-02-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/215)
  Ky Nguyen, Duong Hieu Phan, David Pointcheval

  <details><summary>摘要 / Abstract</summary>

  Multi-Client Functional Encryption ($\mathsf{MCFE}$) and Multi-Input Functional Encryption ($\mathsf{MIFE}$) are very interesting extensions of Functional Encryption for practical purpose. They allow to compute joint function over data from multiple parties. Both primitives are aimed at applications in multi-user settings where decryption can be correctly output for users with appropriate functional decryption keys only. While the definitions for a single user or multiple users were quite general and can be realized for general classes of functions as expressive as Turing machines or all circuits, efficient schemes have been proposed so far for concrete classes of functions: either only for access control, $\mathit{i.e.}$ the identity function under some conditions, or linear/quadratic functions under no condition. In this paper, we target classes of functions that explicitly combine some evaluation functions independent of the decrypting user under the condition of some access control. More precisely, we introduce a framework for $\mathsf{MCFE}$ with fine-grained access control and propose constructions for both single-client and multi-client settings, for inner-product evaluation and access control via Linear Secret Sharing Schemes ($\mathsf{LSSS}$), with selective and adaptive security. The only known work that combines functional encryption in multi-user setting with access control was proposed by Abdalla $\mathit{et~al.}$ (Asiacrypt &#x27;20), which relies on a generic transformation from the single-client schemes to obtain $\mathsf{MIFE}$ schemes that suffer a quadratic factor of $n$ (where $n$ denotes the number of clients) in the ciphertext size. We follow a different path, via $\mathsf{MCFE}$: we present a $\mathit{duplicate\text{-}and\text{-}compress}$ technique to transform the single-client scheme and obtain a $\mathsf{MCFE}$ with fine-grained access control scheme with only a linear factor of $n$ in the ciphertext size. Our final scheme thus outperforms the Abdalla $\mathit{et~al.}$&#x27;s scheme by a factor $n$, as one can obtain $\mathsf{MIFE}$ from $\mathsf{MCFE}$ by making all the labels in $\mathsf{MCFE}$ a fixed public constant. The concrete constructions are secure under the $\mathsf{SXDH}$ assumption, in the random oracle model for the $\mathsf{MCFE}$ scheme, but in the standard model for the $\mathsf{MIFE}$ improvement.

  匹配依据：MPC: secret sharing

  </details>

- **Differential Secrecy for Distributed Data and Applications to Robust Differentially Secure Vector Summation**
  2022-02-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.10618)
  Kunal Talwar

  <details><summary>摘要 / Abstract</summary>

  Computing the noisy sum of real-valued vectors is an important primitive in differentially private learning and statistics. In private federated learning applications, these vectors are held by client devices, leading to a distributed summation problem. Standard Secure Multiparty Computation (SMC) protocols for this problem are susceptible to poisoning attacks, where a client may have a large influence on the sum, without being detected. In this work, we propose a poisoning-robust private summation protocol in the multiple-server setting, recently studied in PRIO. We present a protocol for vector summation that verifies that the Euclidean norm of each contribution is approximately bounded. We show that by relaxing the security constraint in SMC to a differential privacy like guarantee, one can improve over PRIO in terms of communication requirements as well as the client-side computation. Unlike SMC algorithms that inevitably cast integers to elements of a large finite field, our algorithms work over integers/reals, which may allow for additional efficiencies.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Sender-controlled measurement-device-independent multiparty quantum communication**
  2022-02-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.10003)
  Yuyan Wei, Siying Wang, Yajing Zhu, Tao Li

  <details><summary>摘要 / Abstract</summary>

  Multiparty quantum communication is an important branch of quantum networks. It enables private information transmission with information-theoretic security among legitimate parties. We propose a sender-controlled measurement-device-independent multiparty quantum communication protocol. The sender Alice divides a private message into several parts and delivers them to different receivers for secret sharing with imperfect measurement devices and untrusted ancillary nodes. Furthermore, Alice acts as an active controller and checks the security of quantum channels and the reliability of each receiver before she encodes her private message for secret sharing, which makes the protocol convenient for multiparity quantum communication.

  匹配依据：MPC: secret sharing

  </details>

- **gOTzilla: Efficient Disjunctive Zero-Knowledge Proofs from MPC in the Head, with Application to Proofs of Assets in Cryptocurrencies**
  2022-02-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/170)
  Foteini Baldimtsi, Panagiotis Chatzigiannis, S. Dov Gordon, Phi Hung Le, Daniel McVicker

  <details><summary>摘要 / Abstract</summary>

  We present gOTzilla, a protocol for interactive zero-knowledge proofs for very large disjunctive statements of the following format: given publicly known circuit $C$, and set of values $Y = \{y_1, \ldots, y_n\}$, prove knowledge of a witness $x$ such that $C(x) = y_1 \lor C(x) = y_2 \lor \cdots \lor C(x) = y_n$. These type of statements are extremely important for the proof of assets (PoA) problem in cryptocurrencies where a prover wants to prove the knowledge of a secret key $sk$ that associates with the hash of a public key $H(pk)$ posted on the ledger. We note that the size of $n$ in popular cryptocurrencies, such as Bitcoin, is estimated to 80 million. For the construction of gOTzilla, we start by observing that if we restructure the proof statement to an equivalent of proving knowledge of $(x,y)$ such that $(C(x) = y) \land (y = y_1 \lor \cdots \lor y = y_n))$, then we can reduce the disjunction of equalities to 1-out-of-N oblivious transfer (OT). Our overall protocol is based on the MPC in the head (MPCitH) paradigm. We additionally provide a concrete, efficient extension of our protocol for the case where $C$ combines algebraic and non-algebraic statements (which is the case in the PoA application). We achieve an asymptotic communication cost of $O(\log n)$ plus the proof size of the underlying MPCitH protocol. While related work has similar asymptotic complexity, our approach results in concrete performance improvements. We implement our protocol and provide benchmarks. Concretely, for a set of size 1 million entries, the total run-time of our protocol is 14.89 seconds using 48 threads, with 6.18 MB total communication, which is about 4x faster compared to the state of the art when considering a disjunctive statement with algebraic and non-algebraic elements.

  匹配依据：MPC: oblivious transfer

  </details>

- **Verifiable Relation Sharing and Multi-Verifier Zero-Knowledge in Two Rounds: Trading NIZKs with Honest Majority**
  2022-02-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/167)
  Benny Applebaum, Eliran Kachlon, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  We introduce the problem of Verifiable Relation Sharing (VRS) where a client (prover) wishes to share a vector of secret data items among $k$ servers (the verifiers) while proving in zero-knowledge that the shared data satisfies some properties. This combined task of sharing and proving generalizes notions like verifiable secret sharing and zero-knowledge proofs over secret-shared data. We study VRS from a theoretical perspective and focus on its round complexity. As our main contribution, we show that every efficiently-computable relation can be realized by a VRS with an optimal round complexity of two rounds where the first round is input-independent (offline round). The protocol achieves full UC-security against an active adversary that is allowed to corrupt any $t$-subset of the parties that may include the client together with some of the verifiers. For a small (logarithmic) number of parties, we achieve an optimal resiliency threshold of $t 0$. Both protocols can be based on sub-exponentially hard injective one-way functions. If the parties have an access to a collision resistance hash function, we can derive statistical everlasting security, i.e., the protocols are secure against adversaries that are computationally bounded during the protocol execution and become computationally unbounded after the protocol execution. Previous 2-round solutions achieve smaller resiliency thresholds and weaker security notions regardless of the underlying assumptions. As a special case, our protocols give rise to 2-round offline/online constructions of multi-verifier zero-knowledge proofs (MVZK). Such constructions were previously obtained under the same type of assumptions that are needed for NIZK, i.e., public-key assumptions or random-oracle type assumptions (Abe et al., Asiacrypt 2002; Groth and Ostrovsky, Crypto 2007; Boneh et al., Crypto 2019; Yang, and Wang, Eprint 2022). Our work shows, for the first time, that in the presence of an honest majority these assumptions can be replaced with more conservative ``Minicrypt&#x27;&#x27;-type assumptions like injective one-way functions and collision-resistance hash functions. Indeed, our MVZK protocols provide a round-efficient substitute for NIZK in settings where an honest majority is present. Additional applications are also presented.

  匹配依据：MPC: secret sharing

  </details>

- **Towards Fair Multiparty Computation in Scriptless Distributed Ledger Systems**
  2022-02-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/176)
  Minze Xu, Yuan Zhang, Sheng Zhong

  <details><summary>摘要 / Abstract</summary>

  Fairness is one of the fundamental properties for multiparty computation (MPC) protocols. Although fair MPC protocols for general functions is shown to be impossible with a dishonest majority, a variant of fairness called ``fairness with penalty&#x27;&#x27; has been explored recently. A MPC protocol provides fairness with penalty if either all participants can get the output, or the dishonest parties who break the protocol after getting the output will be financially penalized. Fairness with penalty is enabled by previous works leveraging the emerging distributed ledger systems (DLS), e.g. Bitcoin and Ethereum. They utilize the scripting functionality provided by the DLSs to make automatic penalty practical without relying on any trusted third party. However, there is also a significant number of DLSs that do not provide the scripting functionality. In this paper, we propose the ROSE protocol which enables fairness with penalty while only requiring the underlying DLS can verify and broadcast digital signatures on transactions. This requirement can be fulfilled by almost all DLSs, including the scriptless DLSs. To the best of our knowledge, it is still unknown how to realize fairness with penalty on scriptless DLSs before our work. We also provide a implementation of ROSE. The experimental results show that applying ROSE only brings little computation and communication overhead.

  匹配依据：MPC: multiparty computation

  </details>

- **Through the Looking-Glass: Benchmarking Secure Multi-Party Computation Comparisons for ReLU's**
  2022-02-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/202)
  Abdelrahaman Aly, Kashif Nawaz, Eugenio Salazar, Victor Sucasas

  <details><summary>摘要 / Abstract</summary>

  Comparisons or Inequality Tests are an essential building block of Rectified Linear Unit functions (ReLU&#x27;s), ever more present in Machine Learning, specifically in Neural Networks. Motivated by the increasing interest in privacy-preserving Artificial Intelligence, we explore the current state of the art of privacy preserving comparisons over Multi-Party Computation (MPC). We then introduce constant round variations and combinations, which are compatible with customary fixed point arithmetic over MPC. Our main focus is implementation and benchmarking; hence, we showcase our contributions via an open source library, compatible with current MPC software tools. Furthermore, we include a comprehensive comparative analysis on various adversarial settings. Our results improve running times in practical scenarios. Finally, we offer conclusions about the viability of these protocols when adopted for privacy-preserving Machine Learning.

  匹配依据：MPC: multi party computation, secure multi party computation

  </details>

- **Syndrome Decoding in the Head: Shorter Signatures from Zero-Knowledge Proofs**
  2022-02-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/188)
  Thibauld Feneuil, Antoine Joux, Matthieu Rivain

  <details><summary>摘要 / Abstract</summary>

  Zero-knowledge proofs of knowledge are useful tools to design signature schemes. The ongoing effort to build a quantum computer urges the cryptography community to develop new secure cryptographic protocols based on quantum-hard cryptographic problems. One of the few directions is code-based cryptography for which the strongest problem is the syndrome decoding (SD) for random linear codes. This problem is known to be NP-hard and the cryptanalysis state of the art has been stable for many years. A zero-knowledge protocol for this problem was pioneered by Stern in 1993. Since its publication, many articles proposed optimizations, implementation, or variants. In this paper, we introduce a new zero-knowledge proof for the syndrome decoding problem on random linear codes. Instead of using permutations like most of the existing protocols, we rely on the MPC-in-the-head paradigm in which we reduce the task of proving the low Hamming weight of the SD solution to proving some relations between specific polynomials. Specifically, we propose a 5-round zero-knowledge protocol that proves the knowledge of a vector $x$ such that $y=Hx$ and $\operatorname{wt}(x)\leq w$ and which achieves a soundness error closed to $1/N$ for an arbitrary $N$. While turning this protocol into a signature scheme, we achieve a signature size of 11-12 KB for 128-bit security when relying on the hardness of the SD problem on binary fields. Using larger fields (like $\mathbb{F}_{2^8}$), we can produce fast signatures of around 8 KB. This allows us to outperform Picnic3 and to be competitive with SPHINCS+, both post-quantum signature candidates in the ongoing NIST standardization effort. Moreover, our scheme outperforms all the existing code-based signature schemes for the common &quot;signature size + public key size&quot; metric.

  匹配依据：MPC: mpc (context)

  </details>

- **Statistically Sender-Private OT from LPN and Derandomization**
  2022-02-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/185)
  Nir Bitansky, Sapir Freizeit

  <details><summary>摘要 / Abstract</summary>

  We construct a two-message oblivious transfer protocol with statistical sender privacy (SSP OT) based on the Learning Parity with Noise (LPN) Assumption and a standard Nisan-Wigderson style derandomization assumption. Beyond being of interest on their own, SSP OT protocols have proven to be a powerful tool toward minimizing the round complexity in a wide array of cryptographic applications from proofs systems, through secure computation protocols, to hard problems in statistical zero knowledge (SZK). The protocol is plausibly post-quantum secure. The only other constructions with plausible post quantum security are based on the Learning with Errors (LWE) Assumption. Lacking the geometric structure of LWE, our construction and analysis rely on a different set of techniques. Technically, we first construct an SSP OT protocol in the common random string model from LPN alone, and then derandomize the common random string. Most of the technical difficulty lies in the first step. Here we prove a robustness property of the inner product randomness extractor to a certain type of linear splitting attacks. A caveat of our construction is that it relies on the so called low noise regime of LPN. This aligns with our current complexity-theoretic understanding of LPN, which only in the low noise regime is known to imply hardness in SZK.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **Shanrang: Fully Asynchronous Proactive Secret Sharing with Dynamic Committees**
  2022-02-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/164)
  Yunzhou Yan, Yu Xia, Srinivas Devadas

  <details><summary>摘要 / Abstract</summary>

  We present Shanrang, the first fully asynchronous proactive secret sharing scheme with dynamic committee support. Even in the worst possible network environment, where messages could have arbitrary latencies, Shanrang allows a dynamic committee to store a secret and periodically refresh the secret shares in a distributed fashion. When the committee changes, both the old committee and the new committee jointly refresh and transfer the shares to the new committee, without revealing the secret to the adversary. With n parties, Shanrang tolerates n/4 Byzantine faults and maintains liveness as long as the messages are delivered. In contrast to prior work, Shanrang makes no assumptions on the network latency. Designing an asynchronous protocol is challenging because it is impossible to distinguish an adversary sending no messages from an honest party whose messages have not arrived yet. We evaluated Shanrang on geographically distributed machines and we found Shanrang achieved 200 seconds for handing off between 2 committees of 41 parties. Shanrang requires O(λn3 log n) messages and runs in expected O(log n) rounds for every handoff. To show Shanrang is robust even in a harsh network environ- ment, we test Shanrang on the Tor network and it shows robust performance.

  匹配依据：MPC: secret sharing

  </details>

- **OptRand: Optimistically responsive distributed random beacons**
  2022-02-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/193)
  Adithya Bhat, Nibesh Shrestha, Aniket Kate, Kartik Nayak

  <details><summary>摘要 / Abstract</summary>

  Public random beacons publish random numbers at regular intervals, which anyone can obtain and verify. The design of public distributed random beacons has been an exciting research direction with significant implications for blockchains, voting, and beyond. Distributed random beacons, in addition to being bias-resistant and unpredictable, also need to have low communication overhead and latency, high resilience to faults, and ease of reconfigurability. Existing synchronous random beacon protocols sacrifice one or more of these properties. In this work, we design an efficient unpredictable synchronous random beacon protocol, OptRand, with quadratic (in the number n of system nodes) communication complexity per beacon output. First, we innovate by employing a novel combination of bilinear pairing based publicly verifiable secret-sharing and non-interactive zero-knowledge proofs to build a linear (in n) sized publicly verifiable random sharing. Second, we develop a state machine replication protocol with linear-sized inputs that is also optimistically responsive, i.e., it can progress responsively at actual network speed during optimistic conditions, despite the synchrony assumption, and thus incur low latency. In addition, we present an efficient reconfiguration mechanism for OptRand that allows nodes to leave and join the system. Our experiments show our protocols perform significantly better compared to state-of-the-art protocols under optimistic conditions and on par with state-of-the-art protocols in the normal case. We are also the first to implement a reconfiguration mechanism for distributed beacons and demonstrate that our protocol continues to be live during reconfigurations.

  匹配依据：MPC: secret sharing

  </details>

- **Non-Black-Box Approach to Secure Two-Party Computation in Three Rounds**
  2022-02-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/200)
  Akshayaram Srinivasan

  <details><summary>摘要 / Abstract</summary>

  The round complexity of secure two-party computation is a long studied problem with matching upper and lower bounds for the case of black-box simulators (i.e., the simulators that use the adversary as a black-box). In this work, we focus on going beyond this black-box barrier via non-black-box techniques. Specifically, based on standard cryptographic assumptions, we give a construction of a 3-round two-party computation protocol for computing inputless functionalities (such as coin-tossing) that satisfies standard security against malicious senders and $\epsilon$-security against malicious receivers. Prior to our work such protocols were only known for the case of (weak) zero-knowledge.

  匹配依据：MPC: secure two party computation, two party computation

  </details>

- **NanoGRAM: Garbled RAM with $\\widetilde{O}(\\log N)$ Overhead**
  2022-02-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/191)
  Andrew Park, Wei-Kai Lin, Elaine Shi

  <details><summary>摘要 / Abstract</summary>

  We propose a new garbled RAM construction called NanoGRAM, which achieves an amortized cost of $\widetilde{O}(\lambda \cdot (W \log N + \log^3 N))$ bits per memory access, where $\lambda$ is the security parameter, $W$ is the block size, and $N$ is the total number of blocks, and $\widetilde{O}(\cdot)$ hides $poly\log\log$ factors. For sufficiently large blocks where $W = \Omega(\log^2 N)$, our scheme achieves $\widetilde{O}(\lambda \cdot W \log N)$ cost per memory access, where the dependence on $N$ is optimal (barring $poly\log\log$ factors), in terms of the evaluator&#x27;s runtime. Our asymptotical performance matches even the {\it interactive} state-of-the-art (modulo $poly\log\log$ factors), that is, running Circuit ORAM atop garbled circuit, and yet we remove the logarithmic number of interactions necessary in this baseline. Furthermore, we achieve asymptotical improvement over the recent work of Heath et al. Our scheme adopts the same assumptions as the mainstream literature on practical garbled circuits, i.e., circular correlation-robust hashes or a random oracle. We evaluate the concrete performance of NanoGRAM and compare it with a couple of baselines that are asymptotically less efficient. We show that NanoGRAM starts to outperform the naive linear-scan garbled RAM at a memory size of $N = 2^9$ and starts to outperform the recent construction of Heath et al. at $N = 2^{13}$. Finally, as a by product, we also show the existence of a garbled RAM scheme assuming only one-way functions, with an amortized cost of $\widetilde{O}(\lambda^2 \cdot (W \log N + \log^3 N))$ per memory access. Again, the dependence on $N$ is nearly optimal for blocks of size $W = \Omega(\log^2 N)$ bits.

  匹配依据：MPC: garbled circuit, garbled circuits

  </details>

- **D-KODE: Mechanism to Generate and Maintain a Billion Keys**
  2022-02-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/161)
  Easwar Vivek Mangipudi, Aniket Kate

  <details><summary>摘要 / Abstract</summary>

  This work considers two prominent key management problems in the blockchain space: (i) allowing a (distributed) blockchain system to securely airdrop/send some tokens to a potential client Bob, who is yet to set up the required cryptographic key for the system, and (ii) creating a (distributed) cross-chain bridge that allows interoperability at scale by allowing a (changing) set of nodes in a blockchain to perform transactions on the other blockchain. The existing solutions for the first problem need Bob to either generate and maintain private keys locally for the first time in his life — a usability bottleneck — or place trust in third-party custodial services — a privacy and censorship nightmare. Towards solving both problems in a distributed setting against a threshold-bounded adversary, distributed key generation (DKG) based solutions are actively employed; here, a set of servers generate the transactions in a distributed manner and link them to clients’ ids. Nevertheless, these solutions introduce computation and communication overhead that is linear in the number of keys and do not scale well even for a million keys, especially for proactive security against a mobile adversary. This work presents a Keys-On-Demand (D-KODE) distributed protocol suite that lets the blockchain system securely generate the public key of any Bob against a mobile threshold adversary. Multiple servers, here, compute discrete-log private/public keys on the fly through distributed pseudo-random function evaluations on the queried public string. D-KODE also introduces a proactive security mechanism for the employed black-box secret-sharing based DKG to maintain the system’s longitudinal security. The proposed protocol scales well for a very high number of keys as its communication and computation complexity is independent of the number of keys. Our experimental analysis demonstrates that, for a 20-node network with a 2/3 honest majority, D-KODE starts to outperform the state of the art as the number of keys reaches 94K. D-KODE is practical as it takes less than 100msec to generate a secret key for a single-threaded server in a 20-node setup

  匹配依据：MPC: secret sharing

  </details>

- **Cheetah: Lean and Fast Secure Two-Party Deep Neural Network Inference**
  2022-02-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/207)
  Zhicong Huang, Wen-jie Lu, Cheng Hong, Jiansheng Ding

  <details><summary>摘要 / Abstract</summary>

  Secure two-party neural network inference (2PC-NN) can offer privacy protection for both the client and the server and is a promising technique in the machine-learning-as-a-service setting. However, the large overhead of the current 2PC-NN in- ference systems is still being a headache, especially when applied to deep neural networks such as ResNet50. In this work, we present Cheetah, a new 2PC-NN inference system that is faster and more communication-efficient than state-of-the-arts. The main contributions of Cheetah are two-fold: the first part includes carefully designed homomorphic encryption-based protocols that can evaluate the linear layers (namely convolution, batch normalization, and fully-connection) without any expensive rotation operation. The second part includes several lean and communication-efficient primitives for the non-linear functions (e.g., ReLU and truncation). Using Cheetah, we present intensive benchmarks over several large-scale deep neural networks. Take ResNet50 for an example, an end- to-end execution of Cheetah under a WAN setting costs less than 2.5 minutes and 2.3 gigabytes of communication, which outperforms CrypTFlow2 (ACM CCS 2020) by about 5.6× and 12.9×, respectively.

  匹配依据：MPC: 2pc (context)

  </details>

- **Post-quantum Multi-stage Secret Sharing Schemes using Inhomogeneous Linear Recursion and Ajtai's Function**
  2022-02-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.09026)
  Jing Yang, Fang-Wei Fu

  <details><summary>摘要 / Abstract</summary>

  Secret sharing was firstly proposed in 1979 by Shamir and Blakley respectively. To avoid deficiencies of original schemes, researchers presented improvement schemes, among which the multi-secret sharing scheme (MSS) is significant. There are three categories of MSSs, however, we focus on multi-stage secret sharing scheme (MSSS) recovering secrets with any order in this work. By observing inhomogeneous linear recursions (ILRs) in the literature, we conclude a general formula and divide ILRs into two types according to different variables in them. Utilizing these two kinds of ILRs, we propose four verifiable MSSSs with Ajtai&#x27;s function, which is a lattice-based function. Our schemes have the following advantages. Firstly, our schemes can detect cheat of the dealer and participants, and are multi-use. Secondly, we have several ways to restore secrets. Thirdly, we can turn our schemes into other types of MSSs due to the universality of our method. Fourthly, since we utilize a lattice-based function to mask shares, our schemes can resist the attack from the quantum computer with computational security. Finally, although our schemes need more memory consumption than some known schemes, we need much less time consumption, which makes our schemes more suitable facing limited computing power.

  匹配依据：MPC: secret sharing

  </details>

- **Code-routing: a new attack on position verification**
  2022-02-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.07812)
  Joy Cree, Alex May

  <details><summary>摘要 / Abstract</summary>

  The cryptographic task of position verification attempts to verify one party&#x27;s location in spacetime by exploiting constraints on quantum information and relativistic causality. A popular verification scheme known as $f$-routing involves requiring the prover to redirect a quantum system based on the value of a Boolean function $f$. Cheating strategies for the $f$-routing scheme require the prover use pre-shared entanglement, and security of the scheme rests on assumptions about how much entanglement a prover can manipulate. Here, we give a new cheating strategy in which the quantum system is encoded into a secret-sharing scheme, and the authorization structure of the secret-sharing scheme is exploited to direct the system appropriately. This strategy completes the $f$-routing task using $O(SP_p(f))$ EPR pairs, where $SP_p(f)$ is the minimal size of a span program over the field $\mathbb{Z}_p$ computing $f$. This shows we can efficiently attack $f$-routing schemes whenever $f$ is in the complexity class $\text{Mod}_p\text{L}$, after allowing for local pre-processing. The best earlier construction achieved the class L, which is believed to be strictly inside of $\text{Mod}_p\text{L}$. We also show that the size of a quantum secret sharing scheme with indicator function $f_I$ upper bounds entanglement cost of $f$-routing on the function $f_I$.

  匹配依据：MPC: secret sharing

  </details>

- **Exploiting Data Sparsity in Secure Cross-Platform Social Recommendation**
  2022-02-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.07253)
  Jamie Cui, Chaochao Chen, Lingjuan Lyu, Carl Yang, Li Wang

  <details><summary>摘要 / Abstract</summary>

  Social recommendation has shown promising improvements over traditional systems since it leverages social correlation data as an additional input. Most existing work assumes that all data are available to the recommendation platform. However, in practice, user-item interaction data (e.g.,rating) and user-user social data are usually generated by different platforms, and both of which contain sensitive information. Therefore, &quot;How to perform secure and efficient social recommendation across different platforms, where the data are highly-sparse in nature&quot; remains an important challenge. In this work, we bring secure computation techniques into social recommendation, and propose S3Rec, a sparsity-aware secure cross-platform social recommendation framework. As a result, our model can not only improve the recommendation performance of the rating platform by incorporating the sparse social data on the social platform, but also protect data privacy of both platforms. Moreover, to further improve model training efficiency, we propose two secure sparse matrix multiplication protocols based on homomorphic encryption and private information retrieval. Our experiments on two benchmark datasets demonstrate the effectiveness of S3Rec.

  匹配依据：MPC: secure computation

  </details>

- **Constant-weight PIR: Single-round Keyword PIR via Constant-weight Equality Operators**
  2022-02-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.07569)
  Rasoul Akhavan Mahdavi, Florian Kerschbaum

  <details><summary>摘要 / Abstract</summary>

  Equality operators are an essential building block in tasks over secure computation such as private information retrieval. In private information retrieval (PIR), a user queries a database such that the server does not learn which element is queried. In this work, we propose \emph{equality operators for constant-weight codewords}. A constant-weight code is a collection of codewords that share the same Hamming weight. Constant-weight equality operators have a multiplicative depth that depends only on the Hamming weight of the code, not the bit-length of the elements. In our experiments, we show how these equality operators are up to 10 times faster than existing equality operators. Furthermore, we propose PIR using the constant-weight equality operator or \emph{constant-weight PIR}, which is a PIR protocol using an approach previously deemed impractical. We show that for private retrieval of large, streaming data, constant-weight PIR has a smaller communication complexity and lower runtime compared to SEALPIR and MulPIR, respectively, which are two state-of-the-art solutions for PIR. Moreover, we show how constant-weight PIR can be extended to keyword PIR. In keyword PIR, the desired element is retrieved by a unique identifier pertaining to the sought item, e.g., the name of a file. Previous solutions to keyword PIR require one or multiple rounds of communication to reduce the problem to normal PIR. We show that constant-weight PIR is the first practical single-round solution to single-server keyword PIR.

  匹配依据：MPC: secure computation

  </details>

- **Highly Scalable Beaver Triple Generator from Additive-only Homomorphic Encryption**
  2022-02-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.06326)
  Huafei Zhu

  <details><summary>摘要 / Abstract</summary>

  In a convolution neural network, a composition of linear scalar product, non-linear activation function and maximum pooling computations are intensively invoked. As such, to design and implement privacy-preserving, high efficiency machine learning mechanisms, one highly demands a practical crypto tool for secure arithmetic computations. SPDZ, an interesting framework of secure multi-party computations is a promising technique deployed for industry-scale machine learning development if one is able to generate Beaver (multiplication) triple offline efficiently. This paper studies secure yet efficient Beaver triple generators leveraging privacy-preserving scalar product protocols which in turn can be constructed from additive-only homomorphic encryptions(AHEs). Different from the state-of-the-art solutions, where a party first splits her private input into a shared vector and then invokes an AHE to compute scalar product of the shared vectors managed by individual MPC server, we formalize Beaver triple generators in the context of 2-party shared scalar product protocol and then dispense the generated shares to MPC servers. As such, the protocol presented in this paper can be viewed as a dual construction of the state-of-the-art AHE based solutions. Furthermore, instead of applying the Paillier encryption as a basis of our previous constructions or inheriting from somewhat homomorphic encryptions, we propose an alternative construction of AHE from polynomial ring learning with error (RLWE) which results in an efficient implementation of Beaver triple generators.

  匹配依据：MPC: mpc (context)

  </details>

- **SwiftAgg: Communication-Efficient and Dropout-Resistant Secure Aggregation for Federated Learning with Worst-Case Security Guarantees**
  2022-02-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.04169)
  Tayyebeh Jahani-Nezhad, Mohammad Ali Maddah-Ali, Songze Li, Giuseppe Caire

  <details><summary>摘要 / Abstract</summary>

  We propose SwiftAgg, a novel secure aggregation protocol for federated learning systems, where a central server aggregates local models of $N$ distributed users, each of size $L$, trained on their local data, in a privacy-preserving manner. Compared with state-of-the-art secure aggregation protocols, SwiftAgg significantly reduces the communication overheads without any compromise on security. Specifically, in presence of at most $D$ dropout users, SwiftAgg achieves a users-to-server communication load of $(T+1)L$ and a users-to-users communication load of up to $(N-1)(T+D+1)L$, with a worst-case information-theoretic security guarantee, against any subset of up to $T$ semi-honest users who may also collude with the curious server. The key idea of SwiftAgg is to partition the users into groups of size $D+T+1$, then in the first phase, secret sharing and aggregation of the individual models are performed within each group, and then in the second phase, model aggregation is performed on $D+T+1$ sequences of users across the groups. If a user in a sequence drops out in the second phase, the rest of the sequence remain silent. This design allows only a subset of users to communicate with each other, and only the users in a single group to directly communicate with the server, eliminating the requirements of 1) all-to-all communication network across users; and 2) all users communicating with the server, for other secure aggregation protocols. This helps to substantially slash the communication costs of the system.

  匹配依据：MPC: secret sharing

  </details>

- **PrivFair: a Library for Privacy-Preserving Fairness Auditing**
  2022-02-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.04058)
  Sikha Pentyala, David Melanson, Martine De Cock, Golnoosh Farnadi

  <details><summary>摘要 / Abstract</summary>

  Machine learning (ML) has become prominent in applications that directly affect people&#x27;s quality of life, including in healthcare, justice, and finance. ML models have been found to exhibit discrimination based on sensitive attributes such as gender, race, or disability. Assessing if an ML model is free of bias remains challenging to date, and by definition has to be done with sensitive user characteristics that are subject of anti-discrimination and data protection law. Existing libraries for fairness auditing of ML models offer no mechanism to protect the privacy of the audit data. We present PrivFair, a library for privacy-preserving fairness audits of ML models. Through the use of Secure Multiparty Computation (MPC), PrivFair protects the confidentiality of the model under audit and the sensitive data used for the audit, hence it supports scenarios in which a proprietary classifier owned by a company is audited using sensitive audit data from an external investigator. We demonstrate the use of PrivFair for group fairness auditing with tabular data or image data, without requiring the investigator to disclose their data to anyone in an unencrypted manner, or the model owner to reveal their model parameters to anyone in plaintext.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Genuine Activation of Quantum Nonlocality: Stronger Than Local Indistinguishability**
  2022-02-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.03127)
  Tathagata Gupta, Subhendu B. Ghosh, Ardra A, Anandamay Das Bhowmik, Sutapa Saha, Tamal Guha, Ramij Rahaman, Amit Mukherjee

  <details><summary>摘要 / Abstract</summary>

  The structure of quantum theory assures the discrimination of any possible orthogonal set of states. However, the scenario becomes highly nontrivial in the limited measurement setting and leads to different classes of impossibility, viz., indistinguishability, unmarkability, irreducibility etc. These phenomena, often referred to as other nonlocal aspects of quantum theory, have utmost importance in the domain of secret sharing etc. It, therefore, becomes a pertinent question to distill/activate such behaviours from a set, apparently devoid of these nonlocal features and free from local redundancy. While the activation of local indisitinguishability in the sets of entangled states has recently been reported, other stronger notion of quantum nonlocality has yet not been inspected in the parlance of activation. Here, we explored all such stronger versions of nonlocality and affirmatively answered to activate each of them. We also find a locally distinguishable set of multipartite entangled states which can be converted with certainty to a nontrivial set of locally irreducible genuinely entangled states.

  匹配依据：MPC: secret sharing

  </details>

- **ABG: A Multi-Party Mixed Protocol Framework for Privacy-Preserving Cooperative Learning**
  2022-02-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.02928)
  Hao Wang, Zhi Li, Chunpeng Ge, Willy Susilo

  <details><summary>摘要 / Abstract</summary>

  Cooperative learning, that enables two or more data owners to jointly train a model, has been widely adopted to solve the problem of insufficient training data in machine learning. Nowadays, there is an urgent need for institutions and organizations to train a model cooperatively while keeping each other&#x27;s data privately. To address the issue of privacy-preserving in collaborative learning, secure outsourced computation and federated learning are two typical methods. Nevertheless, there are many drawbacks for these two methods when they are leveraged in cooperative learning. For secure outsourced computation, semi-honest servers need to be introduced. Once the outsourced servers collude or perform other active attacks, the privacy of data will be disclosed. For federated learning, it is difficult to apply to the scenarios where vertically partitioned data are distributed over multiple parties. In this work, we propose a multi-party mixed protocol framework, ABG$^n$, which effectively implements arbitrary conversion between Arithmetic sharing (A), Boolean sharing (B) and Garbled-Circuits sharing (G) for $n$-party scenarios. Based on ABG$^n$, we design a privacy-preserving multi-party cooperative learning system, which allows different data owners to cooperate in machine learning in terms of data security and privacy-preserving. Additionally, we design specific privacy-preserving computation protocols for some typical machine learning methods such as logistic regression and neural networks. Compared with previous work, the proposed method has a wider scope of application and does not need to rely on additional servers. Finally, we evaluate the performance of ABG$^n$ on the local setting and on the public cloud setting. The experiments indicate that ABG$^n$ has excellent performance, especially in the network environment with low latency.

  匹配依据：MPC: garbled circuits

  </details>

- **IVeri: Privacy-Preserving Interdomain Verification**
  2022-02-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.02729)
  Ning Luo, Qiao Xiang, Timos Antonopoulos, Ruzica Piskac, Y. Richard Yang, Franck Le

  <details><summary>摘要 / Abstract</summary>

  In an interdomain network, autonomous systems (ASes) often establish peering agreements, so that one AS (agreement consumer) can influence the routing policies of the other AS (agreement provider). Peering agreements are implemented in the BGP configuration of the agreement provider. It is crucial to verify their implementation because one error can lead to disastrous consequences. However, the fundamental challenge for peering agreement verification is how to preserve the privacy of both ASes involved in the agreement. To this end, this paper presents IVeri, the first privacy-preserving interdomain agreement verification system. IVeri models the interdomain agreement verification problem as a SAT formula, and develops a novel, efficient, privacy-serving SAT solver, which uses oblivious shuffling and garbled circuits as the key building blocks to let the agreement consumer and provider collaboratively verify the implementation of interdomain peering agreements without exposing their private information. A prototype of IVeri is implemented and evaluated extensively. Results show that IVeri achieves accurate, privacy-preserving interdomain agreement verification with reasonable overhead.

  匹配依据：MPC: garbled circuits

  </details>

- **Efficient Privacy Preserving Logistic Regression for Horizontally Distributed Data**
  2022-02-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.02650)
  Guanhong Miao

  <details><summary>摘要 / Abstract</summary>

  Internet of Things devices are expanding rapidly and generating huge amount of data. There is an increasing need to explore data collected from these devices. Collaborative learning provides a strategic solution for the Internet of Things settings but also raises public concern over data privacy. In recent years, large amount of privacy preserving techniques have been developed based on secure multi-party computation and differential privacy. A major challenge of collaborative learning is to balance disclosure risk and data utility while maintaining high computation efficiency. In this paper, we proposed privacy preserving logistic regression model using matrix encryption approach. The secure scheme is resilient to chosen plaintext attack, known plaintext attack, and collusion attack that could compromise any agencies in the collaborative learning. Encrypted model estimate is decrypted to provide true model results with no accuracy degradation. Verification phase is implemented to examine dishonest behavior among agencies. Experimental evaluations demonstrate fast convergence rate and high efficiency of proposed scheme.

  匹配依据：MPC: secure multi party computation

  </details>

- **Perfectly-Secure Synchronous MPC with Asynchronous Fallback Guarantees**
  2022-01-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2201.12194) · [IACR ePrint](https://eprint.iacr.org/2022/109)
  Ananya Appan, Anirudh Chandramouli, Ashish Choudhury

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) is a fundamental problem in secure distributed computing. An MPC protocol allows a set of $n$ mutually distrusting parties to carry out any joint computation of their private inputs, without disclosing any additional information about their inputs. MPC with information-theoretic security (also called unconditional security) provides the strongest security guarantees and remains secure even against computationally unbounded adversaries. Perfectly-secure MPC protocols is a class of information-theoretically secure MPC protocols, which provides all the security guarantees in an error-free fashion. The focus of this work is perfectly-secure MPC. Known protocols are designed assuming either a synchronous or an asynchronous communication network. It is well known that perfectly-secure synchronous MPC protocol is possible as long as adversary can corrupt any $t_s &lt; n/3$ parties. On the other hand, perfectly-secure asynchronous MPC protocol can tolerate up to $t_a &lt; n/4$ corrupt parties. A natural question is does there exist a single MPC protocol for the setting where the parties are not aware of the exact network type and which can tolerate up to $t_s &lt; n/3$ corruptions in a synchronous network and up to $t_a &lt; n/4$ corruptions in an asynchronous network. We design such a best-of-both-worlds perfectly-secure MPC protocol, provided $3t_s + t_a &lt; n$ holds. For designing our protocol, we design two important building blocks, which are of independent interest. The first building block is a best-of-both-worlds Byzantine agreement (BA) protocol tolerating $t &lt; n/3$ corruptions and which remains secure, both in a synchronous as well as asynchronous network. The second building block is a polynomial-based best-of-both-worlds verifiable secret-sharing (VSS) protocol, which can tolerate up to $t_s$ and $t_a$ corruptions in a synchronous and in an asynchronous network respectively.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **On Regenerating Codes and Proactive Secret Sharing: Relationships and Implications**
  2022-01-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/096)
  Karim Eldefrawy, Nicholas Genise, Rutuja Kshirsagar, Moti Yung

  <details><summary>摘要 / Abstract</summary>

  We look at two basic coding theoretic and cryptographic mechanisms developed separately and investigate relationships between them and their implications. The first mechanism is Proactive Secret Sharing (PSS), which allows randomization and repair of shares using information from other shares. PSS enables constructing secure multi-party computation protocols that can withstand mobile dynamic attacks. This self-recovery and the redundancy of uncorrupted shares allows a system to overcome recurring faults throughout its lifetime, eventually finishing the computation (or continuing forever to maintain stored data). The second mechanismis Regenerating Codes (RC) which were extensively studied and adopted in distributed storage systems. RC are error correcting (or erasure handling) codes capable of recovering a block of a distributively held codeword from other servers&#x27; blocks. This self-healing nature enables more robustness of a code distributed over different machines. Given that the two mechanisms have a built-in self-healing (leading to stabilizing) and that both can be based on Reed Solomon Codes, it is natural to formally investigate deeper relationships between them. We prove that a PSS scheme can be converted into an RC scheme, and that under some conditions RC can be utilized to instantiate a PSS scheme. This allows us, in turn, to leverage recent results enabling more efficient polynomial interpolation (due to Guruswami and Wooters) to improve the efficiency of a PSS scheme. We also show that if parameters are not carefully calibrated, such interpolation techniques (allowing partial word leakage) may be used to attack a PSS scheme over time. Secondly, the above relationships give rise to extended (de)coding notions. Our first example is mapping the generalized capabilities of adversaries (called generalized adversary structures) from the PSS realm into the RC one. Based on this we define a new variant of RC we call Generalized-decoding Regenerating Code (GRC) where not all network servers have a uniform sub-codeword (motivated by non-uniform probability of attacking different servers case). We finally highlight several interesting research directions due to our results, e.g., designing new improved GRC, and more adaptive RC re-coding techniques.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Symmetries in Linear Programming for Information Inequalities**
  2022-01-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2201.11656)
  Emirhan Gürpınar

  <details><summary>摘要 / Abstract</summary>

  We study the properties of secret sharing schemes, where a random secret value is transformed into shares distributed among several participants in such a way that only the qualified groups of participants can recover the secret value. We improve the lower bounds on the sizes of shares for several specific problems of secret sharing. To this end, we use the method of non-Shannon-type information inequalities going back to Z. Zhang and R.W. Yeung. We employ and extend the linear programming technique that allows to apply new information inequalities indirectly, without even writing them down explicitly. To reduce the complexity of the problems of linear programming involved in the bounds we extensively use symmetry considerations.

  匹配依据：MPC: secret sharing

  </details>

- **Report: State of the Art Solutions for Privacy Preserving Machine Learning in the Medical Context**
  2022-01-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2201.11406)
  Jasmin Zalonis, Frederik Armknecht, Björn Grohmann, Manuel Koch

  <details><summary>摘要 / Abstract</summary>

  Machine Learning on Big Data gets more and more attention in various fields. Even so privacy-preserving techniques become more important, even necessary due to legal regulations such as the General Data Protection Regulation (GDPR). On the other hand data is often distributed among various parties. Especially in the medical context there are several data holders, e.g. hospitals and we need to deal with highly sensitive values. A real world scenario would be data that is held in an electronic patient record that is available in many countries by now. The medical data is encrypted. Users (e.g. physicians, hospitals) can only decrypt the data after patient authorization. One of the main questions concerning this scenario is whether it is possible to process the data for research purposes without violating the privacy of the data owner. We want to evaluate which cryptographic mechanism - homomorphic encryption, multiparty computation or trusted execution environements - can be used for this task.

  匹配依据：MPC: multiparty computation

  </details>

- **Multiple Noisy Private Remote Source Observations for Secure Function Computation**
  2022-01-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/077)
  Onur Gunlu, Matthieu Bloch, Rafael F. Schaefer

  <details><summary>摘要 / Abstract</summary>

  The problem of reliable function computation is extended by imposing privacy, secrecy, and storage constraints on a remote source whose noisy measurements are observed by multiple parties. The main additions to the classic function computation problem include 1) privacy leakage to an eavesdropper is measured with respect to the remote source rather than the transmitting terminals&#x27; observed sequences; 2) the information leakage to a fusion center with respect to the remote source is considered as another privacy leakage metric; 3) two transmitting node observations are used to compute a function. Inner and outer bounds on the rate regions are derived for lossless single-function computation with two transmitting nodes, which recover previous results in the literature, and for special cases that consider invertible functions simplified bounds are established.

  匹配依据：MPC: secure function computation

  </details>

- **SCOTCH: An Efficient Secure Computation Framework for Secure Aggregation**
  2022-01-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2201.07730)
  Yash More, Prashanthi Ramachandran, Priyam Panda, Arup Mondal, Harpreet Virk, Debayan Gupta

  <details><summary>摘要 / Abstract</summary>

  Federated learning enables multiple data owners to jointly train a machine learning model without revealing their private datasets. However, a malicious aggregation server might use the model parameters to derive sensitive information about the training dataset used. To address such leakage, differential privacy and cryptographic techniques have been investigated in prior work, but these often result in large communication overheads or impact model performance. To mitigate this centralization of power, we propose SCOTCH, a decentralized m-party secure-computation framework for federated aggregation that deploys MPC primitives, such as secret sharing. Our protocol is simple, efficient, and provides strict privacy guarantees against curious aggregators or colluding data-owners with minimal communication overheads compared to other existing state-of-the-art privacy-preserving federated learning frameworks. We evaluate our framework by performing extensive experiments on multiple datasets with promising results. SCOTCH can train the standard MLP NN with the training dataset split amongst 3 participating users and 3 aggregating servers with 96.57% accuracy on MNIST, and 98.40% accuracy on the Extended MNIST (digits) dataset, while providing various optimizations.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **More is Merrier: Relax the Non-Collusion Assumption in Multi-Server PIR**
  2022-01-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2201.07740)
  Tiantian Gong, Ryan Henry, Alexandros Psomas, Aniket Kate

  <details><summary>摘要 / Abstract</summary>

  A long line of research on secure computation has confirmed that anything that can be computed, can be computed securely using a set of non-colluding parties. Indeed, this non-collusion assumption makes a number of problems solvable, as well as reduces overheads and bypasses computational hardness results, and it is pervasive across different privacy-enhancing technologies. However, it remains highly susceptible to covert, undetectable collusion among computing parties. This work stems from an observation that if the number of available computing parties is much higher than the number of parties required to perform a secure computation task, collusion attempts in privacy-preserving computations could be deterred. We focus on the prominent privacy-preserving computation task of multi-server $1$-private information retrieval (PIR) that inherently assumes no pair-wise collusion. For PIR application scenarios, such as those for blockchain light clients, where the available servers can be plentiful, a single server&#x27;s deviating action is not tremendously beneficial to itself. We can make deviations undesired via small amounts of rewards and penalties, thus significantly raising the bar for collusion resistance. We design and implement a collusion mitigation mechanism on a public bulletin board with payment execution functions, considering only rational and malicious parties with no honest non-colluding servers. Privacy protection is offered for an extended period after the query executions.

  匹配依据：MPC: secure computation

  </details>

- **An Introduction to Secret-Sharing-Based Secure Multiparty Computation**
  2022-01-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/062)
  Daniel Escudero

  <details><summary>摘要 / Abstract</summary>

  This text serves as a general guide to secure multiparty computation based on secret-sharing, focusing more on practical aspects of the techniques and constructions rather than their theoretical grounds. It is intended to serve as an introductory reference text for readers interested in the area, assuming essentially no background in these topics. This work in progress currently includes an introduction to several core concepts in secure multiparty computation, an overview of simulation-based security, and detailed constructions for honest and two-thirds honest majority MPC, and also dishonest majority in the preprocessing model.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **AESPA: Accuracy Preserving Low-degree Polynomial Activation for Fast Private Inference**
  2022-01-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2201.06699)
  Jaiyoung Park, Michael Jaemin Kim, Wonkyung Jung, Jung Ho Ahn

  <details><summary>摘要 / Abstract</summary>

  Hybrid private inference (PI) protocol, which synergistically utilizes both multi-party computation (MPC) and homomorphic encryption, is one of the most prominent techniques for PI. However, even the state-of-the-art PI protocols are bottlenecked by the non-linear layers, especially the activation functions. Although a standard non-linear activation function can generate higher model accuracy, it must be processed via a costly garbled-circuit MPC primitive. A polynomial activation can be processed via Beaver&#x27;s multiplication triples MPC primitive but has been incurring severe accuracy drops so far. In this paper, we propose an accuracy preserving low-degree polynomial activation function (AESPA) that exploits the Hermite expansion of the ReLU and basis-wise normalization. We apply AESPA to popular ML models, such as VGGNet, ResNet, and pre-activation ResNet, to show an inference accuracy comparable to those of the standard models with ReLU activation, achieving superior accuracy over prior low-degree polynomial studies. When applied to the all-RELU baseline on the state-of-the-art Delphi PI protocol, AESPA shows up to 42.1x and 28.3x lower online latency and communication cost.

  匹配依据：MPC: garbled circuit, multi party computation

  </details>

- **(Nondeterministic) Hardness vs. Non-Malleability**
  2022-01-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/070)
  Marshall Ball, Dana Dachman-Soled, Julian Loss

  <details><summary>摘要 / Abstract</summary>

  We present the first truly explicit constructions of non-malleable codes against tampering by bounded polynomial size circuits. These objects imply unproven circuit lower bounds and our construction is secure provided E requires exponential size nondeterministic circuits, an assumption from the derandomization literature. Prior works on NMC for polysize circuits, either required an untamperable CRS [Cheraghchi, Guruswami ITCS&#x27;14; Faust, Mukherjee, Venturi, Wichs EUROCRYPT&#x27;14] or very strong cryptographic assumptions [Ball, Dachman-Soled, Kulkarni, Lin, Malkin EUROCRYPT&#x27;18; Dachman-Soled, Komargodski, Pass CRYPTO&#x27;21]. Both of works in the latter category only achieve non-malleability with respect to efficient distinguishers and, more importantly, utilize cryptographic objects for which no provably secure instantiations are known outside the random oracle model. In this sense, none of the prior yields fully explicit codes from non-heuristic assumptions. Our assumption is not known to imply the existence of one-way functions, which suggests that cryptography is unnecessary for non-malleability against this class. Technically, security is shown by non-deterministically reducing polynomial size tampering to split-state tampering. The technique is general enough that it allows us to to construct the first seedless non-malleable extractors [Cheraghchi, Guruswami TCC&#x27;14] for sources sampled by polynomial size circuits [Trevisan, Vadhan FOCS&#x27;00] (resp. recognized by polynomial size circuits [Shaltiel CC&#x27;11]) and tampered by polynomial size circuits. Our construction is secure assuming E requires exponential size $\Sigma_4$-circuits (resp. $\Sigma_3$-circuits), this assumption is the state-of-the-art for extracting randomness from such sources (without non-malleability). We additionally observe that non-malleable codes and non-malleable secret sharing [Goyal, Kumar STOC&#x27;18] are essentially equivalent with respect to polynomial size tampering. In more detail, assuming E is hard for exponential size nondeterministic circuits, any efficient secret sharing scheme can be made non-malleable against polynomial size circuit tampering. Unfortunately, all of our constructions only achieve inverse polynomial (statistical) security. Extending a result from [Applebaum, Artemenko, Shaltiel, Yang CC&#x27;16] we show it is impossible to do better using black-box reductions. However, we extend the notion of relative error from [Applebaum, Artemenko, Shaltiel, Yang CC&#x27;16] to non-malleable extractors and show that they can be constructed from similar assumptions. We additionally observe that relative-error non-malleable extractors can be utilized to render a broad class of cryptographic primitives tamper and leakage resilient, while preserving negligible security guarantees.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Maximum Matching on General Graphs and its Application to Enable Privacy-Preserving Kidney Exchange**
  2022-01-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2201.06446)
  Malte Breuer, Ulrike Meyer, Susanne Wetzel

  <details><summary>摘要 / Abstract</summary>

  To this day, there are still some countries where the exchange of kidneys between multiple incompatible patient-donor pairs is restricted by law. Typically, legal regulations in this context are put in place to prohibit coercion and manipulation in order to prevent a market for organ trade. Yet, in countries where kidney exchange is practiced, existing platforms to facilitate such exchanges generally lack sufficient privacy mechanisms. In this paper, we propose a privacy-preserving protocol for kidney exchange that not only addresses the privacy problem of existing platforms but also is geared to lead the way in overcoming legal issues in those countries where kidney exchange is still not practiced. In our approach, we use the concept of secret sharing to distribute the medical data of patients and donors among a set of computing peers in a privacy-preserving fashion. These computing peers then execute our new Secure Multi-Party Computation (SMPC) protocol among each other to determine an optimal set of kidney exchanges. As part of our new protocol, we devise a privacy-preserving solution to the maximum matching problem on general graphs. We have implemented the protocol in the SMPC benchmarking framework MP-SPDZ and provide a comprehensive performance evaluation. Furthermore, we analyze the practicality of our protocol when used in a dynamic setting (where patients and donors arrive and depart over time) based on a data set from the United Network for Organ Sharing.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Integrated semi-quantum layered communication**
  2022-01-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2201.06540)
  Rajni Bala, Sooryansh Asthana, V. Ravishankar

  <details><summary>摘要 / Abstract</summary>

  In recent times, secure quantum communication in layered networks has emerged as an important area of study. In this paper, we harness the potential offered by multidimensional states in secure quantum communication with only one quantum participant and all the other classical participants. We propose three protocols for (i) entanglement-based layered semi--quantum key distribution, (ii) layered semi-quantum secret sharing, and, (iii) integrated layered semi-quantum key distribution and secret sharing to share secret information in an arbitrarily layered network. These protocols integrate the features of semi quantum communication in layered networks. All three protocols allow for the simultaneous distribution of secure information in all the layers of a network, thanks to the employment of multidimensional states. We present these protocols for a small network of at most five participants and three layers and show the robustness of the same against various eavesdropping strategies. Finally, we provide a detailed procedure for the generalization of the proposed protocols to distribute keys/secrets in any arbitrarily structured quantum network.

  匹配依据：MPC: secret sharing

  </details>

- **EFMVFL: An Efficient and Flexible Multi-party Vertical Federated Learning without a Third Party**
  2022-01-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2201.06244)
  Yimin Huang, Xinyu Feng, Wanwan Wang, Hao He, Yukun Wang, Ming Yao

  <details><summary>摘要 / Abstract</summary>

  Federated learning allows multiple participants to conduct joint modeling without disclosing their local data. Vertical federated learning (VFL) handles the situation where participants share the same ID space and different feature spaces. In most VFL frameworks, to protect the security and privacy of the participants&#x27; local data, a third party is needed to generate homomorphic encryption key pairs and perform decryption operations. In this way, the third party is granted the right to decrypt information related to model parameters. However, it isn&#x27;t easy to find such a credible entity in the real world. Existing methods for solving this problem are either communication-intensive or unsuitable for multi-party scenarios. By combining secret sharing and homomorphic encryption, we propose a novel VFL framework without a third party called EFMVFL, which supports flexible expansion to multiple participants with low communication overhead and is applicable to generalized linear models. We give instantiations of our framework under logistic regression and Poisson regression. Theoretical analysis and experiments show that our framework is secure, more efficient, and easy to be extended to multiple participants.

  匹配依据：MPC: secret sharing

  </details>

- **Time-Traveling Simulators Using Blockchains and Their Applications**
  2022-01-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/035)
  Vipul Goyal, Justin Raizes, Pratik Soni

  <details><summary>摘要 / Abstract</summary>

  Blockchain technology has the potential of transforming cryptography. We study the problem of round-complexity of zero-knowledge, and more broadly, of secure computation in the blockchain-hybrid model, where all parties can access the blockchain as an oracle. We study zero-knowledge and secure computation through the lens of a new security notion where the simulator is given the ability to ``time-travel” or more accurately, to look into the future states of the blockchain and use this information to perform simulation. Such a time-traveling simulator gives a novel security guarantee of the following form: whatever the adversary could have learnt from an interaction, it could have computed on its own shortly into the future (e.g., a few hours from now). We exhibit the power of time-traveling simulators by constructing round-efficient protocols in the blockchain-hybrid model. In particular, we construct: 1. Three-round zero-knowledge (ZK) argument for NP with a polynomial-time black-box time-traveling simulator. 2. Three-round secure two-party computation (2PC) for any functionality with a polynomial-time black-box time-traveling simulator for both parties. In addition to standard cryptographic assumptions, we rely on natural hardness assumptions for Proof-of-Work based blockchains. In comparison, in the plain model, three-round protocols with black-box simulation are impossible, and constructions with non-black-box simulation for ZK require novel cryptographic assumptions while no construction for three-round 2PC is known. Our three-round 2PC result relies on a new, two-round extractable commitment that admits a time-traveling extractor.

  匹配依据：MPC: secure computation, secure two party computation

  </details>

- **Private Set Intersection with Delegated Blind Quantum Computing**
  2022-01-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2201.03496)
  Michele Amoretti

  <details><summary>摘要 / Abstract</summary>

  Private set intersection is an important problem with implications in many areas, ranging from remote diagnostics to private contact discovery. In this work, we consider the case of two-party PSI in the honest-but-curious setting. We propose a protocol that solves the server-aided PSI problem using delegated blind quantum computing. More specifically, the proposed protocol allows Alice and Bob (who do not have any quantum computational resources or quantum memory) to interact with Steve (who has a quantum computer) in order for Alice and Bob to obtain set intersection such that privacy is preserved. In particular, Steve learns nothing about the clients&#x27; input, output, or desired computation. The proposed protocol is correct, secure and blind against a malicious server, and characterized by a quantum communication complexity that is linear in the input size.

  匹配依据：MPC: private set intersection

  </details>

- **Locality-Preserving Hashing for Shifts with Connections to Cryptography**
  2022-01-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2201.03041) · [IACR ePrint](https://eprint.iacr.org/2022/028)
  Elette Boyle, Itai Dinur, Niv Gilboa, Yuval Ishai, Nathan Keller, Ohad Klein

  <details><summary>摘要 / Abstract</summary>

  Can we sense our location in an unfamiliar environment by taking a sublinear-size sample of our surroundings? Can we efficiently encrypt a message that only someone physically close to us can decrypt? To solve this kind of problems, we introduce and study a new type of hash functions for finding shifts in sublinear time. A function $h:\{0,1\}^n\to \mathbb{Z}_n$ is a $(d,\delta)$ {\em locality-preserving hash function for shifts} (LPHS) if: (1) $h$ can be computed by (adaptively) querying $d$ bits of its input, and (2) $\Pr [ h(x) \neq h(x \ll 1) + 1 ] \leq \delta$, where $x$ is random and $\ll 1$ denotes a cyclic shift by one bit to the left. We make the following contributions. Near-optimal LPHS via Distributed Discrete Log: We establish a general two-way connection between LPHS and algorithms for distributed discrete logarithm in the generic group model. Using such an algorithm of Dinur et al. (Crypto 2018), we get LPHS with near-optimal error of $\delta=\tilde O(1/d^2)$. This gives an unusual example for the usefulness of group-based cryptography in a post-quantum world. We extend the positive result to non-cyclic and worst-case variants of LPHS. Multidimensional LPHS: We obtain positive and negative results for a multidimensional extension of LPHS, making progress towards an optimal 2-dimensional LPHS. Applications: We demonstrate the usefulness of LPHS by presenting cryptographic and algorithmic applications. In particular, we apply multidimensional LPHS to obtain an efficient &quot;packed&quot; implementation of homomorphic secret sharing and a sublinear-time implementation of location-sensitive encryption whose decryption requires a significantly overlapping view.

  匹配依据：MPC: secret sharing

  </details>

- **A New Constructions of Minimal Binary Linear Codes**
  2022-01-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2201.02981)
  Haibo Liu, Qunying Liao

  <details><summary>摘要 / Abstract</summary>

  Recently, minimal linear codes have been extensively studied due to their applications in secret sharing schemes, secure two-party computations, and so on. Constructing minimal linear codes violating the Ashikhmin-Barg condition and then determining their weight distributions have been interesting in coding theory and cryptography. In this paper, a generic construction for binary linear codes with dimension $m+2$ is presented, then a necessary and sufficient condition for this binary linear code to be minimal is derived. Based on this condition and exponential sums, a new class of minimal binary linear codes violating the Ashikhmin-Barg condition is obtained, and then their weight enumerators are determined.

  匹配依据：MPC: secret sharing

  </details>

- **Pairing-based Accountable Subgroup Multi-signatures with Verifiable Group Setup**
  2022-01-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/018)
  Ahmet Ramazan Ağırtaş, Oğuz Yayla

  <details><summary>摘要 / Abstract</summary>

  An accountable subgroup multi-signature is a kind of multi-signature scheme in which any subgroup $\mathcal{S}$ of a group $\mathcal{G}$ of potential signers jointly sign a message $m$, ensuring that each member of $\mathcal{S}$ is accountable for the resulting signature. In this paper, we propose three novel pairing-based accountable subgroup multi-signature (ASM) schemes, which are secure against existential forgery under chosen-message attacks and computational co-Diffie-Hellman assumption. In the first one, we use Feldman’s verifiable secret sharing scheme as an implicit authentication and proof-of-possession for setting up group $\mathcal{G}$. In the second one, the members participating in authentication are decided by the subgroup. In the third one, we consider a designated combiner managing the authentication process. All schemes we propose here require fewer computations in the signature generation, signature aggregation, and verification phases than the pairing-based ASM scheme proposed by Boneh, Drijvers, and Neven. Moreover, our first and third ones solve the open problem of constructing an ASM scheme in which the subgroup $\mathcal{S}$ of signers is unknown before the signature generation. Besides, we give a method of eliminating the combiner in case of knowing the subgroup of signers $\mathcal{S}$ in advance. Further, we extend our proposed schemes to aggregated versions. For $N$ accountable subgroup multi-signatures, aggregated versions of our proposed schemes output an aggregated signature with the size of a single group ($\mathbb{G}_1$) element and require $N + 1$ pairings in aggregated signature verification. In contrast, the partially aggregated ASM scheme of Boneh, Drijvers, and Neven gives an aggregated signature with the size of $N + 1$ group elements and requires $2N + 1$ pairings in aggregated signature verification.

  匹配依据：MPC: secret sharing

  </details>

- **PI-Cut-Choo and Friends: Compact Blind Signatures via Parallel Instance Cut-and-Choose and More**
  2022-01-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/007)
  Rutchathon Chairattana-Apirom, Lucjan Hanzlik, Julian Loss, Anna Lysyanskaya, Benedikt Wagner

  <details><summary>摘要 / Abstract</summary>

  Blind signature schemes are one of the best-studied tools for privacy-preserving authentication. Unfortunately, known constructions of provably secure blind signatures either rely on non-standard hardness assumptions, or require parameters that grow linearly with the number of concurrently issued signatures, or involve prohibitively inefficient general techniques such as general secure two-party computation. Recently, Katz, Loss and Rosenberg (ASIACRYPT&#x27;21) gave a technique that, for the security parameter n transforms blind signature schemes secure for O(log n) concurrent executions of the blind signing protocol into ones that are secure for any poly(n) concurrent executions. This transform has two drawbacks that we eliminate in this paper: 1) the communication complexity of the resulting blind signing protocol grows linearly with the number of signing interactions; 2) the resulting schemes inherit a very loose security bound from the underlying scheme and, as a result, require impractical parameter sizes. In this work, we give an improved transform for obtaining a secure blind signing protocol tolerating any poly(n) concurrent executions from one that is secure for O(log n) concurrent executions. While preserving the advantages of the original transform, the communication complexity of our new transform only grows logarithmically with the number of interactions. Under the CDH and RSA assumptions, we improve on this generic transform in terms of concrete efficiency and give (1) a BLS-based blind signature scheme over a standard-sized group where signatures are of size roughly 3 KB and communication per signature is roughly 120 KB; and (2) an Okamoto-Guillou-Quisquater-based blind signature scheme with signatures and communication of roughly 9 KB and 8 KB, respectively.

  匹配依据：MPC: secure two party computation

  </details>

- **Secret Sharing Sharing For Highly Scalable Secure Aggregation**
  2022-01-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2201.00864)
  Timothy Stevens, Joseph Near, Christian Skalka

  <details><summary>摘要 / Abstract</summary>

  Secure Multiparty Computation (MPC) can improve the security and privacy of data owners while allowing analysts to perform high quality analytics. Secure aggregation is a secure distributed mechanism to support federated deep learning without the need for trusted third parties. In this paper we present a highly performant secure aggregation protocol with sub-linear communication complexity. Our protocol achieves greater communication and computation efficiencies through a group-based approach. It is similar to secret sharing protocols extended to vectors of values-aka gradients-but within groups we add an additional layer of secret sharing of shares themselves-aka sharding. This ensures privacy of secret inputs in the standard real/ideal security paradigm, in both semi-honest and malicious settings where the server may collude with the adversary. In the malicious setting with 5% corrupt clients and 5% dropouts, our protocol can aggregate over a federation with 100,000,000 members and vectors of length 100 while requiring each client to communicate with only 350 other clients. The concrete computation cost for this aggregation is less than half a second for the server and less than 100ms for the client.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>
