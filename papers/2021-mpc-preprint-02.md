# 2021 · MPC · 仅预印本来源 · 第 2/3 页

[总目录](../PAPERS.md) · [上一页](2021-mpc-preprint-01.md) · [下一页](2021-mpc-preprint-03.md)

- **Homomorphic Encryption for Multiple Users with Less Communications**
  2021-08-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1085)
  Jeongeun Park

  <details><summary>摘要 / Abstract</summary>

  Keeping privacy for every entity in outsourced computation is always a crucial issue. For efficient secure computation, homomorphic encryption (HE) can be one of nice solutions. Especially, multikey homomorphic encryption (MKHE) which allows homomorphic evaluation on encrypted data under different keys can be one of the simplest solutions for a secure computation which handles multiple users&#x27; data. However, the current main problem of MKHE is that the dimension of its evaluated ciphertext relies on the number of users. To solve this problem, there are several variants of multikey homomorphic encryption schemes to keep the size of ciphertext constant for a fixed number of users. However, users interact one another before computation to provide their inputs, which increases setup complexity. Moreover, all the existing MKHE schemes and their variants have unique benefits which cannot be easily achieved at the same time in one scheme. In other words, each type of scheme has a suitable computational scenario to put its best performance. In this paper, we suggest more efficient evaluation key generation algorithms (relinearization key and bootstrapping key) for the existing variants of MKHE schemes which have no ciphertext expansion for a fixed number of users. Our method only requires a very simple and minor pre-processing; distributing public keys, which is not counted as a round at all in many other applications. Regarding bootstrapping, we firstly provide an efficient bootstrapping for multiple users which is the same as the base single-key scheme thanks to our simplified key generation method without a communication. As a result, participants have less communication, computation, and memory cost in online phase. Moreover, we provide a practical conversion algorithm between the two types of schemes in order to \emph{efficiently} utilize both schemes&#x27; advantages together in more various applications. We also provide detailed comparison among similar results so that users can choose a suitable scheme for their homomorphic encryption based application scenarios.

  匹配依据：MPC: secure computation

  </details>

- **Deep-learning-based recognition of multi-singularity structured light**
  2021-08-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2108.10067)
  Hao Wang, Xilin Yang, Zeqi Liu, Yijie Shen, Jing Pan, Yuan Meng, Zijian Shi, Zhensong Wan, Hengkang Zhang, Xing Fu, Qiang Liu

  <details><summary>摘要 / Abstract</summary>

  Structured light with customized complex topological pattern inspires diverse classical and quantum investigations underpinned by accurate detection techniques. However, the current detection schemes are limited to vortex beam with simple phase singularity. The precise recognition of general structured light with multiple singularities remains elusive. Here, we report a deep learning (DL) framework that can unveil multi-singularity phase structures in an end-to-end manner after feeding only two intensity patterns upon beam propagation captured via a camera, thus unleashing intuitive information of twisted photons. The DL toolbox can also acquire phases of Laguerre-Gaussian (LG) modes with single singularity and other general phase objects likewise. Leveraging this DL platform, a phase-based optical secret sharing (OSS) protocol is proposed, which is based on a more general class of multi-singularity modes than conventional LG beams. The OSS protocol features strong security, wealthy state space and convenient intensity-based measurements. This study opens new avenues for vortex beam communications, laser mode analysis, microscopy, Bose-Einstein condensates characterization, etc.

  匹配依据：MPC: secret sharing

  </details>

- **AMPPERE: A Universal Abstract Machine for Privacy-Preserving Entity Resolution Evaluation**
  2021-08-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2108.09879)
  Yixiang Yao, Tanmay Ghai, Srivatsan Ravi, Pedro Szekely

  <details><summary>摘要 / Abstract</summary>

  Entity resolution is the task of identifying records in different datasets that refer to the same entity in the real world. In sensitive domains (e.g. financial accounts, hospital health records), entity resolution must meet privacy requirements to avoid revealing sensitive information such as personal identifiable information to untrusted parties. Existing solutions are either too algorithmically-specific or come with an implicit trade-off between accuracy of the computation, privacy, and run-time efficiency. We propose AMMPERE, an abstract computation model for performing universal privacy-preserving entity resolution. AMPPERE offers abstractions that encapsulate multiple algorithmic and platform-agnostic approaches using variants of Jaccard similarity to perform private data matching and entity resolution. Specifically, we show that two parties can perform entity resolution over their data, without leaking sensitive information. We rigorously compare and analyze the feasibility, performance overhead and privacy-preserving properties of these approaches on the Sharemind multi-party computation (MPC) platform as well as on PALISADE, a lattice-based homomorphic encryption library. The AMPPERE system demonstrates the efficacy of privacy-preserving entity resolution for real-world data while providing a precise characterization of the induced cost of preventing information leakage.

  匹配依据：MPC: multi party computation

  </details>

- **A Simple Post-Quantum Non-Interactive Zero-Knowledge Proof from Garbled Circuits**
  2021-08-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1068)
  Hongrui Cui, Kaiyi Zhang

  <details><summary>摘要 / Abstract</summary>

  We construct a simple public-coin zero-knowledge proof system solely based on symmetric primitives, from which we can apply the Fiat-Shamir heuristic to make it non-interactive. Our construction can be regarded as a simplified cut-and-choose-based malicious secure twoparty computation for the zero-knowledge functionality. Our protocol is suitable for pedagogical purpose for its simplicity (code is only 728 lines).

  匹配依据：MPC: garbled circuits, secure twoparty computation

  </details>

- **Privacy-Preserving Batch-based Task Assignment in Spatial Crowdsourcing with Untrusted Server**
  2021-08-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2108.09019)
  Maocheng Li, Jiachuan Wang, Libin Zheng, Han Wu, Peng Cheng, Lei Chen, Xuemin Lin

  <details><summary>摘要 / Abstract</summary>

  In this paper, we study the privacy-preserving task assignment in spatial crowdsourcing, where the locations of both workers and tasks, prior to their release to the server, are perturbed with Geo-Indistinguishability (a differential privacy notion for location-based systems). Different from the previously studied online setting, where each task is assigned immediately upon arrival, we target the batch-based setting, where the server maximizes the number of successfully assigned tasks after a batch of tasks arrive. To achieve this goal, we propose the k-Switch solution, which first divides the workers into small groups based on the perturbed distance between workers/tasks, and then utilizes Homomorphic Encryption (HE) based secure computation to enhance the task assignment. Furthermore, we expedite HE-based computation by limiting the size of the small groups under k. Extensive experiments demonstrate that, in terms of the number of successfully assigned tasks, the k-Switch solution improves batch-based baselines by 5.9X and the existing online solution by 1.74X, with no privacy leak.

  匹配依据：MPC: secure computation

  </details>

- **Phase-stable source of high-quality three-photon polarization entanglement by cascaded downconversion**
  2021-08-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2108.08662)
  Zachary M. E. Chaisson, Patrick F. Poitras, Micaël Richard, Yannick Castonguay-Page, Paul-Henry Glinel, Véronique Landry, Deny R. Hamel

  <details><summary>摘要 / Abstract</summary>

  Stable sources of entangled photons are important requirements for quantum communications. In recent years, cascaded downconversion has been demonstrated as an effective method of directly producing three-photon entanglement. However, to produce polarization entanglement these sources have until now relied on intricate active phase stabilization schemes, thus limiting their robustness and usability. In this work, we present a completely phase-stable source of three-photon entanglement in the polarization degree of freedom. With this source, which is based on a cascade of two pair sources based on Sagnac configurations, we produce states with over 96\% fidelity with an ideal GHZ state. Moreover, we demonstrate the stability of the source over several days without any ongoing optimization. We expect this source to be a useful tool for applications requiring multiphoton entanglement, such as quantum secret sharing and producing heralded entangled photon pairs.

  匹配依据：MPC: secret sharing

  </details>

- **2PPS -- Publish/Subscribe with Provable Privacy**
  2021-08-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2108.08624)
  Sarah Abdelwahab Gaballah, Christoph Coijanovic, Thorsten Strufe, Max Mühlhäuser

  <details><summary>摘要 / Abstract</summary>

  Publish/Subscribe systems like Twitter and Reddit let users communicate with many recipients without requiring prior personal connections. The content that participants of these systems publish and subscribe to is typically public, but they may nevertheless wish to remain anonymous. While many existing systems allow users to omit explicit identifiers, they do not address the obvious privacy risks of being associated with content that may contain a wide range of sensitive information. We present 2PPS (Twice-Private Publish-Subscribe), the first pub/sub protocol to deliver strong provable privacy protection for both publishers and subscribers, leveraging Distributed Point Function-based secret sharing for publishing and Private Information Retrieval for subscribing. 2PPS does not require trust in other clients and its privacy guarantees hold as long as even a single honest server participant remains. Furthermore, it is scalable and delivers latency suitable for microblogging applications. A prototype implementation of 2PPS can handle 100,000 concurrent active clients with 5 seconds end-to-end latency and significantly lower bandwidth requirements than comparable systems.

  匹配依据：MPC: secret sharing

  </details>

- **Towards Secure and Practical Machine Learning via Secret Sharing and Random Permutation**
  2021-08-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2108.07463)
  Fei Zheng, Chaochao Chen, Xiaolin Zheng, Mingjie Zhu

  <details><summary>摘要 / Abstract</summary>

  With the increasing demands for privacy protection, privacy-preserving machine learning has been drawing much attention in both academia and industry. However, most existing methods have their limitations in practical applications. On the one hand, although most cryptographic methods are provable secure, they bring heavy computation and communication. On the other hand, the security of many relatively efficient private methods (e.g., federated learning and split learning) is being questioned, since they are non-provable secure. Inspired by previous work on privacy-preserving machine learning, we build a privacy-preserving machine learning framework by combining random permutation and arithmetic secret sharing via our compute-after-permutation technique. Since our method reduces the cost for element-wise function computation, it is more efficient than existing cryptographic methods. Moreover, by adopting distance correlation as a metric for privacy leakage, we demonstrate that our method is more secure than previous non-provable secure methods. Overall, our proposal achieves a good balance between security and efficiency. Experimental results show that our method not only is up to 6x faster and reduces up to 85% network traffic compared with state-of-the-art cryptographic methods, but also leaks less privacy during the training process compared with non-provable secure methods.

  匹配依据：MPC: secret sharing

  </details>

- **Threshold Schnorr with Stateless Deterministic Signing from Standard Assumptions**
  2021-08-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1055)
  François Garillot, Yashvanth Kondi, Payman Mohassel, Valeria Nikolaenko

  <details><summary>摘要 / Abstract</summary>

  Schnorr&#x27;s signature scheme permits an elegant threshold signing protocol due to its linear signing equation. However each new signature consumes fresh randomness, which can be a major attack vector in practice. Sources of randomness in deployments are frequently either unreliable, or require state continuity, i.e. reliable fresh state resilient to rollbacks. State continuity is a notoriously difficult guarantee to achieve in practice, due to system crashes caused by software errors, malicious actors, or power supply interruptions (Parno et al., S&amp;P &#x27;11). This is a non-issue for Schnorr variants such as EdDSA, which is specified to derive nonces deterministically as a function of the message and the secret key. However, it is challenging to translate these benefits to the threshold setting, specifically to construct a threshold Schnorr scheme where signing neither requires parties to consume fresh randomness nor update long-term secret state. In this work, we construct a dishonest majority threshold Schnorr protocol that enables such stateless deterministic nonce derivation using standardized block ciphers. Our core technical ingredients are new tools for the zero-knowledge from garbled circuits (ZKGC) paradigm to aid in verifying correct nonce derivation: - A mechanism based on UC Commitments that allows a prover to commit once to a witness, and prove an unbounded number of statements online with only cheap symmetric key operations. - A garbling gadget to translate intermediate garbled circuit wire labels to arithmetic encodings. Our scheme prioritizes computation cost, with each proof requiring only a small constant number of exponentiations.

  匹配依据：MPC: garbled circuit, garbled circuits

  </details>

- **On the Multiplicative Complexity of Cubic Boolean Functions**
  2021-08-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1041)
  Meltem Sonmez Turan, Rene Peralta

  <details><summary>摘要 / Abstract</summary>

  Multiplicative complexity is a relevant complexity measure for many advanced cryptographic protocols such as multi-party computation, fully homomorphic encryption, and zero-knowledge proofs, where processing AND gates is more expensive than processing XOR gates. For Boolean functions, multiplicative complexity is defined as the minimum number of AND gates that are sufficient to implement a function with a circuit over the basis (AND, XOR, NOT). In this paper, we study the multiplicative complexity of cubic Boolean functions. We propose a method to implement a cubic Boolean function with a small number of AND gates and provide upper bounds on the multiplicative complexity that are better than the known generic bounds.

  匹配依据：MPC: multi party computation

  </details>

- **Multiparty secret sharing based on hidden multipliers**
  2021-08-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2108.06967)
  Vitaly Roman'kov

  <details><summary>摘要 / Abstract</summary>

  Secret sharing schemes based on the idea of hidden multipliers in encryption are proposed. As a platform, one can use both multiplicative groups of finite fields and groups of invertible elements of commutative rings, in particular, multiplicative groups of residue rings. We propose two versions of the secret sharing scheme and a version of ($k,n$)-thrested scheme. For a given $n$, the dealer can choose any $k.$ The main feature of the proposed schemes is that the shares of secrets are distributed once and can be used multiple times. This property distinguishes the proposed schemes from the secret sharing schemes known in the literature. The proposed schemes are semantically secure. The same message can be transmitted in different forms. From the transferred secret $c$ it is impossible to determine which of the two given secrets $m_1$ or $m_2$ was transferred. For concreteness, we give some numerical examples.

  匹配依据：MPC: secret sharing

  </details>

- **MUSE: Secure Inference Resilient to Malicious Clients**
  2021-08-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1040)
  Ryan Lehmkuhl, Pratyush Mishra, Akshayaram Srinivasan, Raluca Ada Popa

  <details><summary>摘要 / Abstract</summary>

  The increasing adoption of machine learning inference in applications has led to a corresponding increase in concerns surrounding the privacy guarantees offered by existing mechanisms for inference. Such concerns have motivated the construction of efficient secure inference protocols that allow parties to perform inference without revealing their sensitive information. Recently, there has been a proliferation of such proposals, rapidly improving efficiency. However, most of these protocols assume that the client is semi-honest, that is, the client does not deviate from the protocol; yet in practice, clients are many, have varying incentives, and can behave arbitrarily. To demonstrate that a malicious client can completely break the security of semi-honest protocols, we first develop a new model-extraction attack against many state-of-the-art secure inference protocols. Our attack enables a malicious client to learn model weights with 22x-312x fewer queries than the best black-box model-extraction attack and scales to much deeper networks. Motivated by the severity of our attack, we design and implement MUSE, an efficient two-party secure inference protocol resilient to malicious clients. MUSE introduces a novel cryptographic protocol for conditional disclosure of secrets to switch between authenticated additive secret shares and garbled circuit labels, and an improved Beaver&#x27;s triple generation procedure which is 8x-12.5x faster than existing techniques. These protocols allow MUSE to push a majority of its cryptographic overhead into a preprocessing phase: compared to the equivalent semi-honest protocol (which is close to state-of-the-art), MUSE&#x27;s online phase is only 1.7x-2.2x slower and uses 1.4x more communication. Overall, MUSE is 13.4x-21x faster and uses 2x-3.6x less communication than existing secure inference protocols which defend against malicious clients.

  匹配依据：MPC: garbled circuit

  </details>

- **Limits of Polynomial Packings for $\\mathbb{Z}\_{p^k}$ and $\\mathbb{F}\_{p^k}$**
  2021-08-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1033)
  Jung Hee Cheon, Keewoo Lee

  <details><summary>摘要 / Abstract</summary>

  We formally define polynomial packing methods and initiate a unified study of related concepts in various contexts of cryptography. This includes homomorphic encryption (HE) packing and reverse multiplication-friendly embedding (RMFE) in information-theoretically secure multi-party computation (MPC). We prove several upper bounds and impossibility results on packing methods for $\mathbb{Z}_{p^k}$ or $\mathbb{F}_{p^k}$-messages into $\mathbb{Z}_{p^t}[x]/f(x)$ in terms of (i) packing density, (ii) level-consistency, and (iii) surjectivity. These results have implications on recent development of HE-based MPC over $\mathbb{Z}_{2^k}$ secure against actively corrupted majority and provide new proofs for upper bounds on RMFE.

  匹配依据：MPC: secure multi party computation

  </details>

- **Aegis: A Trusted, Automatic and Accurate Verification Framework for Vertical Federated Learning**
  2021-08-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2108.06958)
  Cengguang Zhang, Junxue Zhang, Di Chai, Kai Chen

  <details><summary>摘要 / Abstract</summary>

  Vertical federated learning (VFL) leverages various privacy-preserving algorithms, e.g., homomorphic encryption or secret sharing based SecureBoost, to ensure data privacy. However, these algorithms all require a semi-honest secure definition, which raises concerns in real-world applications. In this paper, we present Aegis, a trusted, automatic, and accurate verification framework to verify the security of VFL jobs. Aegis is separated from local parties to ensure the security of the framework. Furthermore, it automatically adapts to evolving VFL algorithms by defining the VFL job as a finite state machine to uniformly verify different algorithms and reproduce the entire job to provide more accurate verification. We implement and evaluate Aegis with different threat models on financial and medical datasets. Evaluation results show that: 1) Aegis can detect 95% threat models, and 2) it provides fine-grained verification results within 84% of the total VFL job time.

  匹配依据：MPC: secret sharing

  </details>

- **An efficient implementation of the Shamir secret sharing scheme**
  2021-08-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2108.05982)
  Allyson Hineman, Mario Blaum

  <details><summary>摘要 / Abstract</summary>

  The Shamir secret sharing scheme requires a Maximum Distance Separable (MDS) code, and in its most common implementation, a Reed-Solomon (RS) code is used. In this paper, we observe that the encoding procedure can be made simpler and faster by dropping the MDS condition and specifying the possible symbols that can be shared. In particular, the process can be made even faster by using array codes based on XOR operations instead of RS codes.

  匹配依据：MPC: secret sharing

  </details>

- **Polynomial Representation Is Tricky: Maliciously Secure Private Set Intersection Revisited**
  2021-08-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1009)
  Aydin Abadi, Steven J. Murdoch, Thomas Zacharias

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection protocols (PSIs) allow parties to compute the intersection of their private sets, such that nothing about the sets’ elements beyond the intersection is revealed. PSIs have a variety of applications, primarily in efficiently supporting data sharing in a privacy-preserving manner. At Eurocrypt 2019, Ghosh and Nilges pro- posed three efficient PSIs based on the polynomial representation of sets and proved their security against active adversaries. In this work, we show that these three PSIs are susceptible to several serious attacks. The attacks let an adversary (1) learn the correct intersection while making its victim believe that the intersection is empty, (2) learn a certain element of its victim’s set beyond the intersection, and (3) delete multiple elements of its victim’s input set. We explain why the proofs did not identify these attacks and propose a set of mitigations

  匹配依据：MPC: private set intersection

  </details>

- **Differentially Private n-gram Extraction**
  2021-08-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2108.02831)
  Kunho Kim, Sivakanth Gopi, Janardhan Kulkarni, Sergey Yekhanin

  <details><summary>摘要 / Abstract</summary>

  We revisit the problem of $n$-gram extraction in the differential privacy setting. In this problem, given a corpus of private text data, the goal is to release as many $n$-grams as possible while preserving user level privacy. Extracting $n$-grams is a fundamental subroutine in many NLP applications such as sentence completion, response generation for emails etc. The problem also arises in other applications such as sequence mining, and is a generalization of recently studied differentially private set union (DPSU). In this paper, we develop a new differentially private algorithm for this problem which, in our experiments, significantly outperforms the state-of-the-art. Our improvements stem from combining recent advances in DPSU, privacy accounting, and new heuristics for pruning in the tree-based approach initiated by Chen et al. (2012).

  匹配依据：MPC: private set union

  </details>

- **Experimental quantum secure network with digital signatures and encryption**
  2021-07-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2107.14089)
  Hua-Lei Yin, Yao Fu, Chen-Long Li, Chen-Xun Weng, Bing-Hong Li, Jie Gu, Yu-Shuo Lu, Shan Huang, Zeng-Bing Chen

  <details><summary>摘要 / Abstract</summary>

  Cryptography promises four information security objectives, namely, confidentiality, integrity, authenticity, and non-repudiation, to support trillions of transactions annually in the digital economy. Efficient digital signatures, ensuring the integrity, authenticity, and non-repudiation of data with information-theoretical security are highly urgent and intractable open problems in cryptography. Here, we propose a protocol of high-efficiency quantum digital signatures using secret sharing, one-time universal$_2$ hashing, and the one-time pad. We just need to use a 384-bit key to sign documents of up to $2^{64}$ lengths with a security bound of $10^{-19}$. If one-megabit document is signed, the signature efficiency is improved by more than $10^8$ times compared with previous quantum digital signature protocols. Furthermore, we build the first all-in-one quantum secure network integrating information-theoretically secure communication, digital signatures, secret sharing, and conference key agreement and experimentally demonstrate this signature efficiency advantage. Our work completes the cryptography toolbox of the four information security objectives.

  匹配依据：MPC: secret sharing

  </details>

- **Stateful KEM: Towards Optimal Robust Combiner for Key Encapsulation Mechanism**
  2021-07-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/989)
  Jia Xu, Yiwen Gao, Hoon Wei Lim, Hongbing Wang, Ee-Chien Chang

  <details><summary>摘要 / Abstract</summary>

  A $(1,n)$-robust combiner combines $n$ cryptography primitives to construct a new primitive of the same type, and guarantees that if any of the ingredient primitive is secure, then the resulting primitive is secure. In recent two decades, robust combiners for various crypto primitives (e.g. public key encryption, oblivious transfer) have been proposed. Very recently, more works on robust combiners for post-quantum key encapsulation mechanism appear to achieve multi-layer of defence, to counter the future threat from Shor&#x27;s algorithm running on powerful quantum computers. However, typically such combination of $n$ crypto primitives will sum up running times of all ingredient primitives and thus introduce linear overhead in time complexity, which may be a big burden on server side, since the server has to run key encapsulation mechanism (or key exchange protocol) with every online client. We propose the very first robust combiner (of KEMs), with $O(1)$ \emph{amortized} complexity overhead, which not only breaks the linear boundary, but also achieves optimal complexity. Our experiments also confirm that the performance overhead of our robust combiner of $n$ KEMs is constant (i.e. $O(1)$) rather than linear (i.e. $O(n)$). Our cost is that, the resulting KEM has to maintain a secret dynamic state of fixed and linear size (i.e. $O(n)$) . We call such KEM as Stateful Key Encapsulation Mechanism (SKEM). SKEM is suitable for two users (or devices), who will have \emph{frequent} secure communications (e.g. via VPN or SSH). We also formally define the security formulation for SKEM and prove the security of our proposed SKEM scheme in standard model.

  匹配依据：MPC: oblivious transfer

  </details>

- **FLOD: Oblivious Defender for Private Byzantine-Robust Federated Learning with Dishonest-Majority**
  2021-07-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/993)
  Ye Dong, Xiaojun Chen, Kaiyun Li, Dakui Wang, Shuai Zeng

  <details><summary>摘要 / Abstract</summary>

  \textit{Privacy} and \textit{Byzantine-robustness} are two major concerns of federated learning (FL), but mitigating both threats simultaneously is highly challenging: privacy-preserving strategies prohibit access to individual model updates to avoid leakage, while Byzantine-robust methods require access for comprehensive mathematical analysis. Besides, most Byzantine-robust methods only work in the \textit{honest-majority} setting. We present $\mathsf{FLOD}$, a novel oblivious defender for private Byzantine-robust FL in dishonest-majority setting. Basically, we propose a novel Hamming distance-based aggregation method to resist $&gt;1/2$ Byzantine attacks using a small \textit{root-dataset} and \textit{server-model} for bootstrapping trust. Furthermore, we employ two non-colluding servers and use additive homomorphic encryption ($\mathsf{AHE}$) and secure two-party computation (2PC) primitives to construct efficient privacy-preserving building blocks for secure aggregation, in which we propose two novel in-depth variants of Beaver Multiplication triples (MT) to reduce the overhead of Bit to Arithmetic ($\mathsf{Bit2A}$) conversion and vector weighted sum aggregation ($\mathsf{VSWA}$) significantly. Experiments on real-world and synthetic datasets demonstrate our effectiveness and efficiency: (\romannumeral1) $\mathsf{FLOD}$ defeats known Byzantine attacks with a negligible effect on accuracy and convergence, (\romannumeral2) achieves a reduction of $\approx 2\times$ for offline (resp. online) overhead of $\mathsf{Bit2A}$ and $\mathsf{VSWA}$ compared to $\mathsf{ABY}$-$\mathsf{AHE}$ (resp. $\mathsf{ABY}$-$\mathsf{MT}$) based methods (NDSS&#x27;15), (\romannumeral3) and reduces total online communication and run-time by $167$-$1416\times$ and $3.1$-$7.4\times$ compared to $\mathsf{FLGUARD}$ (Crypto Eprint 2021/025).

  匹配依据：MPC: secure two party computation

  </details>

- **Sisyphus: A Cautionary Tale of Using Low-Degree Polynomial Activations in Privacy-Preserving Deep Learning**
  2021-07-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2107.12342)
  Karthik Garimella, Nandan Kumar Jha, Brandon Reagen

  <details><summary>摘要 / Abstract</summary>

  Privacy concerns in client-server machine learning have given rise to private inference (PI), where neural inference occurs directly on encrypted inputs. PI protects clients&#x27; personal data and the server&#x27;s intellectual property. A common practice in PI is to use garbled circuits to compute nonlinear functions privately, namely ReLUs. However, garbled circuits suffer from high storage, bandwidth, and latency costs. To mitigate these issues, PI-friendly polynomial activation functions have been employed to replace ReLU. In this work, we ask: Is it feasible to substitute all ReLUs with low-degree polynomial activation functions for building deep, privacy-friendly neural networks? We explore this question by analyzing the challenges of substituting ReLUs with polynomials, starting with simple drop-and-replace solutions to novel, more involved replace-and-retrain strategies. We examine the limitations of each method and provide commentary on the use of polynomial activation functions for PI. We find all evaluated solutions suffer from the escaping activation problem: forward activation values inevitably begin to expand at an exponential rate away from stable regions of the polynomials, which leads to exploding values (NaNs) or poor approximations.

  匹配依据：MPC: garbled circuits

  </details>

- **Selective MPC: Distributed Computation of Differentially Private Key-Value Statistics**
  2021-07-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2107.12407)
  Thomas Humphries, Rasoul Akhavan Mahdavi, Shannon Veitch, Florian Kerschbaum

  <details><summary>摘要 / Abstract</summary>

  Key-value data is a naturally occurring data type that has not been thoroughly investigated in the local trust model. Existing local differentially private (LDP) solutions for computing statistics over key-value data suffer from the inherent accuracy limitations of each user adding their own noise. Multi-party computation (MPC) maintains better accuracy than LDP and similarly does not require a trusted central party. However, naively applying MPC to key-value data results in prohibitively expensive computation costs. In this work, we present selective multi-party computation, a novel approach to distributed computation that leverages DP leakage to efficiently and accurately compute statistics over key-value data. By providing each party with a view of a random subset of the data, we can capture subtractive noise. We prove that our protocol satisfies pure DP and is provably secure in the combined DP/MPC model. Our empirical evaluation demonstrates that we can compute statistics over 10,000 keys in 20 seconds and can scale up to 30 servers while obtaining results for a single key in under a second.

  匹配依据：MPC: multi party computation

  </details>

- **Revealing the Landscape of Privacy-Enhancing Technologies in the Context of Data Markets for the IoT: A Systematic Literature Review**
  2021-07-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2107.11905)
  Gonzalo Munilla Garrido, Johannes Sedlmeir, Ömer Uludağ, Ilias Soto Alaoui, Andre Luckow, Florian Matthes

  <details><summary>摘要 / Abstract</summary>

  IoT data markets in public and private institutions have become increasingly relevant in recent years because of their potential to improve data availability and unlock new business models. However, exchanging data in markets bears considerable challenges related to disclosing sensitive information. Despite considerable research focused on different aspects of privacy-enhancing data markets for the IoT, none of the solutions proposed so far seems to find a practical adoption. Thus, this study aims to organize the state-of-the-art solutions, analyze and scope the technologies that have been suggested in this context, and structure the remaining challenges to determine areas where future research is required. To accomplish this goal, we conducted a systematic literature review on privacy enhancement in data markets for the IoT, covering 50 publications dated up to July 2020, and provided updates with 24 publications dated up to May 2022. Our results indicate that most research in this area has emerged only recently, and no IoT data market architecture has established itself as canonical. Existing solutions frequently lack the required combination of anonymization and secure computation technologies. Furthermore, there is no consensus on the appropriate use of blockchain technology for IoT data markets and a low degree of leveraging existing libraries or reusing generic data market architectures. We also identified significant challenges remaining, such as the copy problem and the recursive enforcement problem that-while solutions have been suggested to some extent-are often not sufficiently addressed in proposed designs. We conclude that privacy-enhancing technologies need further improvements to positively impact data markets so that, ultimately, the value of data is preserved through data scarcity and users&#x27; privacy and businesses-critical information are protected.

  匹配依据：MPC: secure computation

  </details>

- **Low-bandwidth recovery of linear functions of Reed-Solomon-encoded data**
  2021-07-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2107.11847)
  Noah Shutty, Mary Wootters

  <details><summary>摘要 / Abstract</summary>

  We study the problem of efficiently computing on encoded data. More specifically, we study the question of low-bandwidth computation of functions $F:\mathbb{F}^k \to \mathbb{F}$ of some data $x \in \mathbb{F}^k$, given access to an encoding $c \in \mathbb{F}^n$ of $x$ under an error correcting code. In our model -- relevant in distributed storage, distributed computation and secret sharing -- each symbol of $c$ is held by a different party, and we aim to minimize the total amount of information downloaded from each party in order to compute $F(x)$. Special cases of this problem have arisen in several domains, and we believe that it is fruitful to study this problem in generality. Our main result is a low-bandwidth scheme to compute linear functions for Reed-Solomon codes, even in the presence of erasures. More precisely, let $ε&gt; 0$ and let $\mathcal{C}: \mathbb{F}^k \to \mathbb{F}^n$ be a full-length Reed-Solomon code of rate $1 - ε$ over a field $\mathbb{F}$ with constant characteristic. For any $γ\in [0, ε)$, our scheme can compute any linear function $F(x)$ given access to any $(1 - γ)$-fraction of the symbols of $\mathcal{C}(x)$, with download bandwidth $O(n/(ε- γ))$ bits. In contrast, the naive scheme that involves reconstructing the data $x$ and then computing $F(x)$ uses $Θ(n \log n)$ bits. Our scheme has applications in distributed storage, coded computation, and homomorphic secret sharing.

  匹配依据：MPC: secret sharing

  </details>

- **Secure Quantum Computation with Classical Communication**
  2021-07-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/964)
  James Bartusek

  <details><summary>摘要 / Abstract</summary>

  The study of secure multi-party computation (MPC) has thus far been limited to the following two settings: every party is fully classical, or every party has quantum capabilities. This paper studies a notion of MPC that allows some classical and some quantum parties to securely compute a quantum functionality over their joint private inputs. In particular, we construct (constant-round, composable) protocols for blind and verifiable classical delegation of quantum computation, and give applications to the secure computation of quantum functionalities using only classical communication. Assuming QLWE (the quantum hardness of learning with errors), we obtain the following (maliciously-secure) protocols for computing any pseudo-deterministic quantum functionality. • A six-round protocol between one quantum server and multiple classical clients in the CRS (common random string) model. • A three-round protocol between one quantum server and multiple classical clients in the PKI (public key infrastructure) + QRO (quantum random oracle) model. • A two-message protocol between quantum sender and classical receiver (a quantum non-interactive secure computation protocol), in the QRO model. To enable the composability of our classical verification of quantum computation protocols, we require the notion of malicious blindness, which stipulates that the prover does not learn anything about the verifier’s delegated computation, even if it is able to observe whether or not the verifier accepted the proof. To construct a protocol with malicious blindness, we use a classical verification protocol for sampBQP computation (Chung et al., Arxiv 2020), which in general has inverse polynomial soundness error, to prove honest evaluation of QFHE (quantum fully-homomorphic encryption) ciphertexts with negligible soundness error. Obtaining a constant-round protocol requires a strong parallel repetition theorem for classical verification of quantum computation, which we show following the “nearly orthogonal projector” proof strategy (Alagic et al., TCC 2020).

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **Differential Phase Shift Quantum Secret Sharing Using a Twin Field with Asymmetric Source Intensities**
  2021-07-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2107.10465)
  Zhao-Ying Jia, Jie Gu, Bing-Hong Li, Hua-Lei Yin, Zeng-Bing Chen

  <details><summary>摘要 / Abstract</summary>

  As an essential application of quantum mechanics in classical cryptography, quantum secret sharing has become an indispensable component of quantum internet. Recently, a differential phase shift quantum secret sharing protocol using a twin field has been proposed to break the linear rate-distance boundary. However, this original protocol has a poor performance over channels with asymmetric transmittances. To make it more practical, we present a differential phase shift quantum secret sharing protocol with asymmetric source intensities and give the security proof of our protocol against individual attacks. Taking finite-key effects into account, our asymmetric protocol can theoretically obtain the key rate two orders of magnitude higher than that of the original protocol when the difference in length between Alice&#x27;s channel and Bob&#x27;s is fixed at 14 km. Moreover, our protocol can provide a high key rate even when the difference is quite large and has great robustness against finite-key effects. Therefore, our work is meaningful for the real-life applications of quantum secret sharing.

  匹配依据：MPC: secret sharing

  </details>

- **Cryptimeleon: A Library for Fast Prototyping of Privacy-Preserving Cryptographic Schemes**
  2021-07-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/961)
  Jan Bobolz, Fabian Eidens, Raphael Heitjohann, Jeremy Fell

  <details><summary>摘要 / Abstract</summary>

  We present a cryptographic Java library called Cryptimeleon designed for prototyping and benchmarking privacy-preserving cryptographic schemes. The library is geared towards researchers wanting to implement their schemes (1) as a sanity check for their constructions, and (2) for benchmark numbers in their papers. To ease the implementation process, Cryptimeleon &quot;speaks the language&quot; of paper writers. It offers a similar degree of abstraction as is commonly used in research papers. For example, bilinear groups can be used as the familiar black-box and Schnorr-style proofs can be described on the level of Camenisch-Stadler notation. It employs several optimizations (such as multi-exponentation) transparently, allowing the developer to phrase computations as written in the paper instead of having to conform to an artificial API for better performance. Cryptimeleon implements (among others) finite fields, elliptic curve groups and pairings, hashing, Schnorr-style zero-knowledge proofs, accumulators, digital signatures, secret sharing, group signatures, attribute-based encryption, and other modern cryptographic constructions. In this paper, we present the library, its capabilities, and explain important design decisions.

  匹配依据：MPC: secret sharing

  </details>

- **Multi-institution encrypted medical imaging AI validation without data sharing**
  2021-07-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2107.10230)
  Arjun Soin, Pratik Bhatu, Rohit Takhar, Nishanth Chandran, Divya Gupta, Javier Alvarez-Valle, Rahul Sharma, Vidur Mahajan, Matthew P Lungren

  <details><summary>摘要 / Abstract</summary>

  Adoption of artificial intelligence medical imaging applications is often impeded by barriers between healthcare systems and algorithm developers given that access to both private patient data and commercial model IP is important to perform pre-deployment evaluation. This work investigates a framework for secure, privacy-preserving and AI-enabled medical imaging inference using CrypTFlow2, a state-of-the-art end-to-end compiler allowing cryptographically secure 2-party Computation (2PC) protocols between the machine learning model vendor and target patient data owner. A common DenseNet-121 chest x-ray diagnosis model was evaluated on multi-institutional chest radiographic imaging datasets both with and without CrypTFlow2 on two test sets spanning seven sites across the US and India, and comprising 1,149 chest x-ray images. We measure comparative AUROC performance between secure and insecure inference in multiple pathology classification tasks, and explore model output distributional shifts and resource constraints introduced by secure model inference. Secure inference with CrypTFlow2 demonstrated no significant difference in AUROC for all diagnoses, and model outputs from secure and insecure inference methods were distributionally equivalent. The use of CrypTFlow2 may allow off-the-shelf secure 2PC between healthcare systems and AI model vendors for medical imaging, without changes in performance, and can facilitate scalable pre-deployment infrastructure for real-world secure model evaluation without exposure to patient data or model IP.

  匹配依据：MPC: secure 2 party computation

  </details>

- **Unconditionally secure relativistic multi-party biased coin flipping and die rolling**
  2021-07-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2107.09196)
  Damián Pitalúa-García

  <details><summary>摘要 / Abstract</summary>

  We introduce relativistic multi-party biased die rolling protocols, generalizing coin flipping to $M \geq 2$ parties and to $N \geq 2$ outcomes for any chosen outcome biases, and show them unconditionally secure. Our results prove that the most general random secure multi-party computation, where all parties receive the output and there is no secret input by any party, can be implemented with unconditional security. Our protocols extend Kent&#x27;s [A. Kent, Phys. Rev. Lett. 83, 5382 (1999)] two-party unbiased coin flipping protocol, do not require any quantum communication, are practical to implement with current technology, and to our knowledge are the first multi-party relativistic cryptographic protocols.

  匹配依据：MPC: secure multi party computation

  </details>

- **Payment Schemes from Limited Information with Applications in Distributed Computing**
  2021-07-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2107.08748)
  Nikolaj I. Schwartzbach

  <details><summary>摘要 / Abstract</summary>

  We propose a generic mechanism for incentivizing behavior in an arbitrary finite game using payments. Doing so is trivial if the mechanism is allowed to observe all actions taken in the game, as this allows it to simply punish those agents who deviate from the intended strategy. Instead, we consider an abstraction where the mechanism probabilistically infers information about what happened in the game. We show that payment schemes can be used to implement any set of utilities if and only if the mechanism can essentially infer completely what happened. We show that finding an optimal payment scheme for games of perfect information is \textsf{P}-complete, and conjecture it to be \textsf{PPAD}-hard for games of imperfect information. We prove a lower bound on the size of the payments, showing that the payments must be linear in the intended level of security. We demonstrate the applicability of our model to concrete problems in distributed computing, namely decentralized commerce and secure multiparty computation, for which the payments match the lower bound asymptotically.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Limits on the Adaptive Security of Yao's Garbling**
  2021-07-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/945)
  Chethan Kamath, Karen Klein, Krzysztof Pietrzak, Daniel Wichs

  <details><summary>摘要 / Abstract</summary>

  Yao’s garbling scheme is one of the most fundamental cryptographic constructions. Lindell and Pinkas (Journal of Cryptograhy 2009) gave a formal proof of security in the selective setting where the adversary chooses the challenge inputs before seeing the garbled circuit assuming secure symmetric-key encryption (and hence one-way functions). This was followed by results, both positive and negative, concerning its security in the, stronger, adaptive setting. Applebaum et al. (Crypto 2013) showed that it cannot satisfy adaptive security as is, due to a simple incompressibility argument. Jafargholi and Wichs (TCC 2017) considered a natural adaptation of Yao’s scheme (where the output mapping is sent in the online phase, together with the garbled input) that circumvents this negative result, and proved that it is adaptively secure, at least for shallow circuits. In particular, they showed that for the class of circuits of depth $\delta$, the loss in security is at most exponential in $\delta$. The above results all concern the simulation-based notion of security. In this work, we show that the upper bound of Jafargholi and Wichs is basically optimal in a strong sense. As our main result, we show that there exists a family of Boolean circuits, one for each depth $\delta\in\mathbb{N}$, such that any black-box reduction proving the adaptive indistinguishability of the natural adaptation of Yao’s scheme from any symmetric-key encryption has to lose a factor that is exponential in $\sqrt(\delta)$. Since indistinguishability is a weaker notion than simulation, our bound also applies to adaptive simulation. To establish our results, we build on the recent approach of Kamath et al. (Eprint 2021), which uses pebbling lower bounds in conjunction with oracle separations to prove fine-grained lower bounds on loss in cryptographic security.

  匹配依据：MPC: garbled circuit, garbling scheme

  </details>

- **Argus: A Fully Transparent Incentive System for Anti-Piracy Campaigns (Extended Version)**
  2021-07-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2107.06049)
  Xian Zhang, Xiaobing Guo, Zixuan Zeng, Wenyan Liu, Zhongxin Guo, Yang Chen, Shuo Chen, Qiufeng Yin, Mao Yang, Lidong Zhou

  <details><summary>摘要 / Abstract</summary>

  Anti-piracy is fundamentally a procedure that relies on collecting data from the open anonymous population, so how to incentivize credible reporting is a question at the center of the problem. Industrial alliances and companies are running anti-piracy incentive campaigns, but their effectiveness is publicly questioned due to the lack of transparency. We believe that full transparency of a campaign is necessary to truly incentivize people. It means that every role, e.g., content owner, licensee of the content, or every person in the open population, can understand the mechanism and be assured about its execution without trusting any single role. We see this as a distributed system problem. In this paper, we present Argus, a fully transparent incentive system for anti-piracy campaigns. The groundwork of Argus is to formulate the objectives for fully transparent incentive mechanisms, which securely and comprehensively consolidate the different interests of all roles. These objectives form the core of the Argus design, highlighted by our innovations about a Sybil-proof incentive function, a commit-and-reveal scheme, and an oblivious transfer scheme. In the implementation, we overcome a set of unavoidable obstacles to ensure security despite full transparency. Moreover, we effectively optimize several cryptographic operations so that the cost for a piracy reporting is reduced to an equivalent cost of sending about 14 ETH-transfer transactions to run on the public Ethereum network, which would otherwise correspond to thousands of transactions. With the security and practicality of Argus, we hope real-world anti-piracy campaigns will be truly effective by shifting to a fully transparent incentive mechanism.

  匹配依据：MPC: oblivious transfer

  </details>

- **Two Constructions for Minimal Ternary Linear Codes**
  2021-07-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2107.04992)
  Haibo Liu Qunying Liao, Canze Zhu

  <details><summary>摘要 / Abstract</summary>

  Recently, minimal linear codes have been extensively studied due to their applications in secret sharing schemes, two-party computations, and so on. Constructing minimal linear codes violating the Ashikhmin-Barg condition and then determining their weight distributions have been interesting in coding theory and cryptography. In this paper, basing on exponential sums, Krawtchouk polynomials, and a function defined on special sets of vectors in $\mathbb{F}_3^m$, we present two new classes of minimal ternary linear codes violating the Ashikhmin-Barg condition, and then determine their complete weight enumerators. Especially, the minimal distance of a class of these codes is better than that of codes constructed in \cite{Heng-Ding-Zhou}.

  匹配依据：MPC: secret sharing

  </details>

- **Publicly Auditable MPC-as-a-Service with succinct verification and universal setup**
  2021-07-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2107.04248)
  Sanket Kanjalkar, Ye Zhang, Shreyas Gandlur, Andrew Miller

  <details><summary>摘要 / Abstract</summary>

  In recent years, multiparty computation as a service (MPCaaS) has gained popularity as a way to build distributed privacy-preserving systems. We argue that for many such applications, we should also require that the MPC protocol is publicly auditable, meaning that anyone can check the given computation is carried out correctly -- even if the server nodes carrying out the computation are all corrupt. In a nutshell, the way to make an MPC protocol auditable is to combine an underlying MPC protocol with verifiable computing proof (in particular, a SNARK). Building a general-purpose MPCaaS from existing constructions would require us to perform a costly &quot;trusted setup&quot; every time we wish to run a new or modified application. To address this, we provide the first efficient construction for auditable MPC that has a one-time universal setup. Despite improving the trusted setup, we match the state-of-the-art in asymptotic performance: the server nodes incur a linear computation overhead and constant round communication overhead compared to the underlying MPC, and the audit size and verification are logarithmic in the application circuit size. We also provide an implementation and benchmarks that support our asymptotic analysis in example applications. Furthermore, compared with existing auditable MPC protocols, besides offering a universal setup our construction also has a 3x smaller proof, 3x faster verification time and comparable prover time.

  匹配依据：MPC: multiparty computation

  </details>

- **On Treewidth, Separators and Yao's Garbling**
  2021-07-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/926)
  Chethan Kamath, Karen Klein, Krzysztof Pietrzak

  <details><summary>摘要 / Abstract</summary>

  We show that Yao’s garbling scheme is adaptively indistinguishable for the class of Boolean circuits of size S and treewidth w with only a S^O(w) loss in security. For instance, circuits with constant treewidth are as a result adaptively indistinguishable with only a polynomial loss. This (partially) complements a negative result of Applebaum et al. (Crypto 2013), which showed (assuming one-way functions) that Yao’s garbling scheme cannot be adaptively simulatable. As main technical contributions, we introduce a new pebble game that abstracts out our security reduction and then present a pebbling strategy for this game where the number of pebbles used is roughly O(d w log(S)), d being the fan-out of the circuit. The design of the strategy relies on separators, a graph-theoretic notion with connections to circuit complexity.

  匹配依据：MPC: garbling scheme

  </details>

- **The Round Complexity of Quantum Zero-Knowledge**
  2021-07-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/918)
  Orestis Chardouvelis, Giulio Malavolta

  <details><summary>摘要 / Abstract</summary>

  We study the round complexity of zero-knowledge for QMA (the quantum analogue of NP). Assuming the quantum quasi-polynomial hardness of the learning with errors (LWE) problem, we obtain the following results: - 2-Round statistical witness indistinguishable (WI) arguments for QMA. - 4-Round statistical zero-knowledge arguments for QMA in the plain model, additionally assuming the existence of quantum fully homomorphic encryption. This is the first protocol for constant-round statistical zero-knowledge arguments for QMA. - 2-Round computational (statistical, resp.) zero-knowledge for QMA in the timing model, additionally assuming the existence of post-quantum non-parallelizing functions (time-lock puzzles, resp.). All of these protocols match the best round complexity known for the corresponding protocols for NP with post-quantum security. Along the way, we introduce and construct the notions of sometimes-extractable oblivious transfer and sometimes-simulatable zero-knowledge, which might be of independent interest.

  匹配依据：MPC: oblivious transfer

  </details>

- **Two new classes of projective two-weight linear codes**
  2021-07-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2107.02446)
  Canze Zhu, Qunying Liao

  <details><summary>摘要 / Abstract</summary>

  In this paper, for an odd prime $p$, several classes of two-weight linear codes over the finite field $\mathbb{F}_p$ are constructed from the defining sets, and then their complete weight distributions are determined by employing character sums. These codes can be suitable for applications in secret sharing schemes. Furthermore, two new classes of projective two-weight codes are obtained, and then two new classes of strongly regular graphs are given.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy in Distributed Computations based on Real Number Secret Sharing**
  2021-07-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2107.00911)
  Katrine Tjell, Rafael Wisniewski

  <details><summary>摘要 / Abstract</summary>

  Privacy preservation in distributed computations is an important subject as digitization and new technologies enable collection and storage of vast amounts of data, including private data belonging to individuals. To this end, there is a need for a privacy preserving computation framework that minimises the leak of private information during computations while being efficient enough for practical usage. This paper presents a step towards such a framework with the proposal of a real number secret sharing scheme that works directly on real numbers without the need for conversion to integers which is the case in related schemes. The scheme offers computations like addition, multiplication, and division to be performed directly on secret shared data (the cipher text version of the data). Simulations show that the scheme is much more efficient in terms of accuracy than its counterpart version based on integers and finite field arithmetic. The drawback with the proposed scheme is that it is not perfectly secure. However, we provide a privacy analysis of the scheme, where we show that the leaked information can be upper bounded and asymptotically goes to zero. To demonstrate the scheme, we use it to perform Kalman filtering directly on secret shared data.

  匹配依据：MPC: secret sharing

  </details>

- **DEMO: AirCollect: Efficiently Recovering Hashed Phone Numbers Leaked via Apple AirDrop**
  2021-07-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/893)
  Alexander Heinrich, Matthias Hollick, Thomas Schneider, Milan Stute, Christian Weinert

  <details><summary>摘要 / Abstract</summary>

  Apple&#x27;s file-sharing service AirDrop leaks phone numbers and email addresses by exchanging vulnerable hash values of the user&#x27;s own contact identifiers during the authentication handshake with nearby devices. In a paper presented at USENIX Security&#x27;21, we theoretically describe two attacks to exploit these vulnerabilities and propose &quot;PrivateDrop&quot; as a privacy-preserving drop-in replacement for Apple&#x27;s AirDrop protocol based on private set intersection. In this demo, we show how these vulnerabilities are efficiently exploitable via Wi-Fi and physical proximity to a target. Privacy and security implications include the possibility of conducting advanced spear phishing attacks or deploying multiple &quot;collector&quot; devices in order to build databases that map contact identifiers to specific locations. For our proof-of-concept, we leverage a custom rainbow table construction to reverse SHA-256 hashes of phone numbers in a matter of milliseconds. We discuss the trade-off between success rate and storage requirements of the rainbow table and, after following responsible disclosure with Apple, we publish our proof-of-concept implementation as &quot;AirCollect&quot; on GitHub.

  匹配依据：MPC: private set intersection

  </details>

- **Fully Device-Independent Model on Quantum Networks**
  2021-06-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.15840)
  Ming-Xing Luo

  <details><summary>摘要 / Abstract</summary>

  Bell inequality can provide a useful witness for device-independent applications with quantum (or post-quantum) eavesdroppers. This feature holds only for single entangled systems. Our goal is to explore device-independent model for quantum networks. We firstly propose a Bell inequality to verify the genuinely multipartite nonlocality of connected quantum networks including cyclic networks and universal quantum computational resources for measurement-based computation model. This is further used to construct new monogamy relation in a fully device-independent model with multisource quantum resources. It is finally applied for multiparty quantum key distribution, blind quantum computation, and quantum secret sharing. The present model can inspire various large-scale applications on quantum networks in a device-independent manner.

  匹配依据：MPC: secret sharing

  </details>

- **Computational Hardness of Optimal FairComputation: Beyond Minicrypt**
  2021-06-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/882)
  Hemanta K. Maji, Mingyuan Wang

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation allows mutually distrusting parties to compute securely over their private data. However, guaranteeing output delivery to honest parties when the adversarial parties may abort the protocol has been a challenging objective. As a representative task, this work considers two-party coin-tossing protocols with guaranteed output delivery, a.k.a., fair coin-tossing. In the information-theoretic plain model, as in two-party zero-sum games, one of the parties can force an output with certainty. In the commitment-hybrid, any $r$-message coin-tossing protocol is ${1/\sqrt r}$-unfair, i.e., the adversary can change the honest party&#x27;s output distribution by $1/\sqrt r$ in the statistical distance. Moran, Naor, and Segev (TCC--2009) constructed the first $1/r$-unfair protocol in the oblivious transfer-hybrid. No further security improvement is possible because Cleve (STOC--1986) proved that $1/r$-unfairness is unavoidable. Therefore, Moran, Naor, and Segev&#x27;s coin-tossing protocol is optimal. However, is oblivious transfer necessary for optimal fair coin-tossing? Maji and Wang (CRYPTO--2020) proved that any coin-tossing protocol using one-way functions in a black-box manner is at least $1/\sqrt r$-unfair. That is, optimal fair coin-tossing is impossible in Minicrypt. Our work focuses on tightly characterizing the hardness of computation assumption necessary and sufficient for optimal fair coin-tossing within Cryptomania, outside Minicrypt. Haitner, Makriyannia, Nissim, Omri, Shaltiel, and Silbak (FOCS--2018 and TCC--2018) proved that better than $1/\sqrt r$-unfairness, for any constant $r$, implies the existence of a key-agreement protocol. We prove that any coin-tossing protocol using public-key encryption (or, multi-round key agreement protocols) in a black-box manner must be $1/\sqrt r$-unfair. Next, our work entirely characterizes the additional power of secure function evaluation functionalities for optimal fair coin-tossing. We augment the model with an idealized secure function evaluation of $f$, \aka, the $f$-hybrid. If $f$ is complete, that is, oblivious transfer is possible in the $f$-hybrid, then optimal fair coin-tossing is also possible in the $f$-hybrid. On the other hand, if $f$ is not complete, then a coin-tossing protocol using public-key encryption in a black-box manner in the $f$-hybrid is at least $1/\sqrt r$-unfair.

  匹配依据：MPC: oblivious transfer, secure function evaluation, secure multi party computation

  </details>

- **Studying the merging cluster Abell 3266 with eROSITA**
  2021-06-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.14534)
  J. S. Sanders, V. Biffi, M. Brüggen, E. Bulbul, K. Dennerl, K. Dolag, T. Erben, M. Freyberg, E. Gatuzz, V. Ghirardini, D. N. Hoang, M. Klein, A. Liu, A. Merloni, F. Pacaud, M. E. Ramos-Ceja, T. H. Reiprich, J. A. ZuHone

  <details><summary>摘要 / Abstract</summary>

  Abell 3266 is one of the X-ray brightest galaxy clusters in the sky and is a well-known merging system. Using the ability of the eROSITA telescope onboard SRG (Spectrum Röntgen Gamma) to observe a wide field with a single pointing, we analysed a new observation of the cluster out to a radius of R_200. The X-ray images highlight sub-structures present in the cluster, including the north-east--south-west merger seen in previous ASCA, Chandra, and XMM-Newton data, a merging group towards the north-west, and filamentary structures between the core and one or more groups towards the west. We compute spatially resolved spectroscopic maps of the thermodynamic properties of the cluster, including the metallicity. The merging subclusters are seen as low entropy material within the cluster. The filamentary structures could be the rims of a powerful outburst of an active galactic nucleus, or most likely material stripped from the western group(s) as they passed through the cluster core. Seen in two directions is a pressure jump at a radius of 1.1 Mpc, which is consistent with a shock with a Mach number of ~1.5-1.7. The eROSITA data confirm that the cluster is not a simple merging system, but it is made up of several subclusters which are merging or will shortly merge. We computed a hydrostatic mass from the eROSITA data, finding good agreement with a previous XMM-Newton result. With this pointing we detect several extended sources, where we find secure associations between z=0.36-1.0 for seven of them, that is background galaxy groups and clusters, highlighting the power of eROSITA to find such systems.

  匹配依据：MPC: mpc (context)

  </details>

- **Linear Secret-Sharing Schemes for $k$-uniform access structures**
  2021-06-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.14833)
  Younjin Kim, Jihye Kwon, Hyang-Sook Lee

  <details><summary>摘要 / Abstract</summary>

  A {\it $k$-uniform hypergraph} $\mathcal{H}=(V, E)$ consists of a set $V$ of vertices and a set $E$ of hyperedges ($k$-hyperedges), which is a family of $k$-subsets of $V$. A {\it forbidden $k$-homogeneous (or forbidden $k$-hypergraph)} access structure $\mathcal{A}$ is represented by a $k$-uniform hypergraph $\mathcal{H}=(V, E)$ and has the following property: a set of vertices (participants) can reconstruct the secret value from their shares in the secret sharing scheme if they are connected by a $k$-hyperedge or their size is at least $k+1$. A forbidden $k$-homogeneous access structure has been studied by many authors under the terminology of $k$-uniform access structures. In this paper, we provide efficient constructions on the total share size of linear secret sharing schemes for sparse and dense $k$-uniform access structures for a constant $k$ using the hypergraph decomposition technique and the monotone span programs.

  匹配依据：MPC: secret sharing

  </details>

- **Secure Reversible Data Hiding in Encrypted Images Using Cipher-Feedback Secret Sharing**
  2021-06-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.14139)
  Zhongyun Hua, Yanxiang Wang, Shuang Yi, Yicong Zhou, Xiaohua Jia

  <details><summary>摘要 / Abstract</summary>

  Reversible data hiding in encrypted images (RDH-EI) has attracted increasing attention, since it can protect the privacy of original images while the embedded data can be exactly extracted. Recently, some RDH-EI schemes with multiple data hiders have been proposed using secret sharing technique. However, these schemes protect the contents of the original images with lightweight security level. In this paper, we propose a high-security RDH-EI scheme with multiple data hiders. First, we introduce a cipher-feedback secret sharing (CFSS) technique. It follows the cryptography standards by introducing the cipher-feedback strategy of AES. Then, using the CFSS technique, we devise a new (r,n)-threshold (r&lt;=n) RDH-EI scheme with multiple data hiders called CFSS-RDHEI. It can encrypt an original image into n encrypted images with reduced size using an encryption key and sends each encrypted image to one data hider. Each data hider can independently embed secret data into the encrypted image to obtain the corresponding marked encrypted image. The original image can be completely recovered from r marked encrypted images and the encryption key. Performance evaluations show that our CFSS-RDHEI scheme has high embedding rate and its generated encrypted images are much smaller, compared to existing secret sharing-based RDH-EI schemes. Security analysis demonstrates that it can achieve high security to defense some commonly used security attacks.

  匹配依据：MPC: secret sharing

  </details>

- **SoK: Gröbner Basis Algorithms for Arithmetization Oriented Ciphers**
  2021-06-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/870)
  Jan Ferdinand Sauer, Alan Szepieniec

  <details><summary>摘要 / Abstract</summary>

  Many new ciphers target a concise algebraic description for efficient evaluation in a proof system or a multi-party computation. This new target for optimization introduces algebraic vulnerabilities, particularly involving Gröbner basis analysis. Unfortunately, the literature on Gröbner bases tends to be either purely mathematical, or focused on small fields. In this paper, we survey the most important algorithms and present them in an intuitive way. The discussion of their complexities enables researchers to assess the security of concrete arithmetization-oriented ciphers. Aside from streamlining the security analysis, this paper helps newcomers enter the field.

  匹配依据：MPC: multi party computation

  </details>

- **Secure Computation for G-Module and its Applications**
  2021-06-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/857)
  Qizhi Zhang, Bingsheng Zhang, Lichun Li, Shan Yin, Juanjuan Sun

  <details><summary>摘要 / Abstract</summary>

  Secure computation enables two or more parties to jointly evaluate a function without revealing to each other their private input. G-module is an abelian group M, where the group G acts compatibly with the abelian group structure on M. In this work, we present several secure computation protocols for G-module operations in the online/offline mode. We then show how to instantiate those protocols to implement many widely used secure computation primitives in privacy-preserving machine learning and data mining, such as oblivious cyclic shift, one-round shared OT, oblivious permutation, oblivious shuffle, secure comparison, oblivious selection, DReLU, and ReLU, etc. All the proposed protocols are constant-round, and they are 2X - 10X more efficient than the-state-of-the-art constant-round protocols in terms of communication complexity.

  匹配依据：MPC: secure computation

  </details>

- **Privacy Threats Analysis to Secure Federated Learning**
  2021-06-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.13076)
  Yuchen Li, Yifan Bao, Liyao Xiang, Junhan Liu, Cen Chen, Li Wang, Xinbing Wang

  <details><summary>摘要 / Abstract</summary>

  Federated learning is emerging as a machine learning technique that trains a model across multiple decentralized parties. It is renowned for preserving privacy as the data never leaves the computational devices, and recent approaches further enhance its privacy by hiding messages transferred in encryption. However, we found that despite the efforts, federated learning remains privacy-threatening, due to its interactive nature across different parties. In this paper, we analyze the privacy threats in industrial-level federated learning frameworks with secure computation, and reveal such threats widely exist in typical machine learning models such as linear regression, logistic regression and decision tree. For the linear and logistic regression, we show through theoretical analysis that it is possible for the attacker to invert the entire private input of the victim, given very few information. For the decision tree model, we launch an attack to infer the range of victim&#x27;s private inputs. All attacks are evaluated on popular federated learning frameworks and real-world datasets.

  匹配依据：MPC: secure computation

  </details>

- **PQC: R-Propping of a Simple Oblivious Transfer**
  2021-06-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/854)
  Pedro Hecht

  <details><summary>摘要 / Abstract</summary>

  Post-quantum cryptography (PQC) is nowadays a very active research field [1]. We follow a non-standard way to achieve it, taking any common protocol and replacing arithmetic with GF(2^8) field operations, a procedure defined as R-Propping [2-7]. The resulting protocol security relies on the intractability of a generalized discrete log problem, combined with the power sets of algebraic ring extension tensors and resilience to quantum and algebraic attacks. Oblivious Transfer (OT) is a keystone for Secure Multiparty Computing (SMPC) [8], one of the most pursued cryptographic areas. It is a critical issue to develop a fast OT solution because of its intensive use in many protocols. Here, we adopt the simple OT protocol developed by Chou and Orlandi [9] as the base model to be propped. Our solution is fully scalable to achieve quantum and classical security levels as needed. We present a step-by-step numerical example of the proposed protocol.

  匹配依据：MPC: oblivious transfer, secure multiparty computing

  </details>

- **Unconditional Communication-Efficient MPC via Hall's Marriage Theorem**
  2021-06-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/834)
  Vipul Goyal, Antigoni Polychroniadou, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  The best known $n$ party unconditional multiparty computation protocols with an optimal corruption threshold communicates $O(n)$ field elements per gate. This has been the case even in the semi-honest setting despite over a decade of research on communication complexity in this setting. Going to the slightly sub-optimal corruption setting, the work of Damgard, Ishai, and Kroigaard (EUROCRYPT 2010) provided the first protocol for a single circuit achieving communication complexity of $O(\log|C|)$ elements per gate. While a number of works have improved upon this result, obtaining a protocol with $O(1)$ field elements per gate has been an open problem. In this work, we construct the first unconditional multi-party computation protocol evaluating a single arithmetic circuit with amortized communication complexity of $O(1)$ elements per gate.

  匹配依据：MPC: multi party computation, multiparty computation

  </details>

- **Practical, Label Private Deep Learning Training based on Secure Multiparty Computation and Differential Privacy**
  2021-06-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/835)
  Sen Yuan, Milan Shen, Ilya Mironov, Anderson C. A. Nascimento

  <details><summary>摘要 / Abstract</summary>

  Secure Multiparty Computation (MPC) is an invaluable tool for training machine learning models when the training data cannot be directly accessed by the model trainer. Unfortunately, complex algorithms, such as deep learning models, have their computational complexities increased by orders of magnitude when performed using MPC protocols. In this contribution, we study how to efficiently train an important class of machine learning problems by using MPC where features are known by one of the computing parties and only the labels are private. We propose new protocols combining differential privacy (DP) and MPC in order to privately and efficiently train a deep learning model in such scenario. More specifically, we release differentially private information during the MPC computation to dramatically reduce the training time. All released information does not compromise the privacy of the labels at the individual level. Our protocols can have running times that are orders of magnitude better than a straightforward use of MPC at a moderate cost in model accuracy.

  匹配依据：MPC: secure multiparty computation

  </details>

- **MPC for $Q\_2$ Access Structures over Rings and Fields**
  2021-06-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/841)
  Robin Jadoul, Nigel P. Smart, Barry Van Leeuwen

  <details><summary>摘要 / Abstract</summary>

  We examine Multi-Party Computation protocols in the active-security-with-abort setting for $Q_2$ access structures over small and large finite fields $F_p$ and over rings $Z_{p^k}$. We give general protocols which work for any $Q_2$ access structure which is realised by a multiplicative Extended Span Program. We generalize a number of techniques and protocols from various papers and compare the different methodologies. In particular we examine the expected communication cost per multiplication gate when the protocols are instantiated with different access structures.

  匹配依据：MPC: multi party computation

  </details>

- **Improving security for users of decentralized exchanges through multiparty computation**
  2021-06-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.10972)
  Robert Annessi, Ethan Fast

  <details><summary>摘要 / Abstract</summary>

  Decentralized cryptocurrency exchanges offer compelling security benefits over centralized exchanges: users control their funds and avoid the risk of an exchange hack or malicious operator. However, because user assets are fully accessible by a secret key, decentralized exchanges pose significant internal security risks for trading firms and automated trading systems, where a compromised system can result in total loss of funds. Centralized exchanges mitigate this risk through API key based security policies that allow professional users to give individual traders or automated systems specific and customizable access rights such as trading or withdrawal limits. Such policies, however, are not compatible with decentralized exchanges, where all exchange operations require a signature generated by the owner&#x27;s secret key. This paper introduces a protocol based upon multiparty computation that allows for the creation of API keys and security policies that can be applied to any existing decentralized exchange. Our protocol works with both ECDSA and EdDSA signature schemes and prioritizes efficient computation and communication. We have deployed this protocol on Nash exchange, as well as around several Ethereum-based automated market maker smart contracts, where it secures the trading accounts and wallets of thousands of users.

  匹配依据：MPC: multiparty computation

  </details>

- **Impossibility of composable Oblivious Transfer in relativistic quantum cryptography**
  2021-06-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.11200)
  Lorenzo Laneve, Lidia del Rio

  <details><summary>摘要 / Abstract</summary>

  We study the cryptographic primitive Oblivious Transfer; a composable construction of this resource would allow arbitrary multi-party computation to be carried out in a secure way, i.e. to compute functions in a distributed way while keeping inputs from different parties private. First we review a framework that allows us to analyze composability of classical and quantum cryptographic protocols in special relativity: Abstract Cryptography implemented with Causal Boxes. We then (1) explore and formalize different versions of oblivious transfer found in the literature, (2) prove that their equivalence holds also in relativistic quantum settings, (3) show that it is impossible to composably construct any of these versions of oblivious transfer from only classical or quantum communication among distrusting agents in relativistic settings, (4) prove that the impossibility also extends to multi-party computation, and (5) provide a mutual construction between oblivious transfer and bit commitment.

  匹配依据：MPC: multi party computation, oblivious transfer

  </details>

- **Anonymous and Distributed Authentication for Peer-to-Peer Networks**
  2021-06-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/838)
  Pasan Tennakoon, Supipi Karunathilaka, Rishikeshan Lavakumar, Janaka Alawatugoda

  <details><summary>摘要 / Abstract</summary>

  Well-known authentication mechanisms such as Public-key Infrastructure (PKI) and Identity-based Public-key Certificates (ID-PKC) are not suitable to integrate with the peer-to-peer (P2P) network environment. The reason is the difficulty in maintaining a centralized authority to manage the certificates. The authentication becomes even harder in an anonymous environment. We present three authentication protocols such that the users can authenticate themselves in an anonymous P2P network, without revealing their identities. Firstly, we propose a way to use existing ring signature schemes to obtain anonymous authentication. Secondly, we propose an anonymous authentication scheme utilizing secret sharing schemes. Finally, we propose a zero-knowledge-based anonymous authentication protocol. We provide security justifications of the three protocols in terms of anonymity, completeness, soundness, resilience to impersonation attacks, and resilience to replay attacks.

  匹配依据：MPC: secret sharing

  </details>

- **TOPPool: Time-aware Optimized Privacy-Preserving Ridesharing**
  2021-06-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/812)
  Elena Pagnin, Gunnar Gunnarsson, Pedram Talebi, Claudio Orlandi, Andrei Sabelfeld

  <details><summary>摘要 / Abstract</summary>

  Ridesharing is revolutionizing the transportation industry in many countries. Yet, the state of the art is based on heavily centralized services and platforms, where the service providers have full possession of the users’ location data. Recently, researchers have started addressing the challenge of enabling privacy-preserving ridesharing. The initial proposals, however, have shortcomings, as some rely on a central party, some incur high performance penalties, and most do not consider time preferences for ridesharing. TOPPool encompasses ridesharing based on the proximity of end-points of a ride as well as partial itinerary overlaps. To achieve the latter, we propose a simple yet powerful reduction to a private set intersection on trips represented as sets of consecutive road segments. We show that TOPPool includes time preferences while preserving privacy and without relying on a third party. We evaluate our approach on real-world data from the New York’s Taxi &amp; Limousine Commission. Our experiments demonstrate that TOPPool is superior in performance over the prior work: our intersection-based itinerary matching runs in less than 0.3 seconds for reasonable trip length, in contrast, on the same set of trips prior work takes up to 10 hours.

  匹配依据：MPC: private set intersection

  </details>

- **One-out-of-$q$ OT Combiners**
  2021-06-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/822)
  Oriol Farràs, Jordi Ribes-González

  <details><summary>摘要 / Abstract</summary>

  In $1$-out-of-$q$ Oblivious Transfer (OT) protocols, a sender Alice is able to send one of $q\ge 2$ messages to a receiver Bob, all while being oblivious to which message was transferred. Moreover, the receiver learns only one of these messages. Oblivious Transfer combiners take $n$ instances of OT protocols as input, and produce an OT protocol that is secure if sufficiently many of the $n$ original OT instances are secure. We present new $1$-out-of-$q$ OT combiners that are perfectly secure against active adversaries. Our combiners arise from secret sharing techniques. We show that given an $\mathbb{F}_q$-linear secret sharing scheme on a set of $n$ participants and adversary structure $\mathcal{A}$, we can construct $n$-server, $1$-out-of-$q$ OT combiners that are secure against an adversary corrupting either Alice and a set of servers in $\mathcal{A}$, or Bob and a set of servers $B$ with $\bar{B}\notin\mathcal{A}$. If the normalized total share size of the scheme is $\ell$, then the resulting OT combiner requires $\ell$ calls to OT protocols, and the total amount of bits exchanged during the protocol is $(q^2+q+1)\ell\log q$. We also present a construction based on $1$-out-of-$2$ OT combiners that uses the protocol of Crépeau, Brassard and Robert (FOCS 1986). This construction provides smaller communication costs for certain adversary structures, such as threshold ones: For any prime power $q\geq n$, there are $n$-server, $1$-out-of-$q$ OT combiners that are perfectly secure against active adversaries corrupting either Alice or Bob, and a minority of the OT candidates, exchanging $O(qn\log q)$ bits in total.

  匹配依据：MPC: oblivious transfer, secret sharing

  </details>

- **Balancing Quality and Efficiency in Private Clustering with Affinity Propagation**
  2021-06-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/825)
  Hannah Keller, Helen Möllering, Thomas Schneider, Hossein Yalame

  <details><summary>摘要 / Abstract</summary>

  In many machine learning applications, training data consists of sensitive information from multiple sources. Privacy-preserving machine learning using secure computation enables multiple parties to compute on their joint data without disclosing their inputs to each other. In this work, we focus on clustering, an unsupervised machine learning technique that partitions data into groups. Previous works on privacy-preserving clustering often leak information and focus on the k-means algorithm, which provides only limited clustering quality and flexibility. Additionally, the number of clusters k must be known in advance. We analyze several prominent clustering algorithms&#x27; capabilities and their compatibility with secure computation techniques to create an efficient, fully privacy-preserving clustering implementation superior to k-means. We find affinity propagation to be the most promising candidate and securely implement it using various multi-party computation techniques. Privacy-preserving affinity propagation does not require any input parameters and consists of operations hat are relatively efficient with secure computation. As threat models, we consider passive security as well as active security with an honest and dishonest majority. We offer the first comparison of privacy-preserving clustering between these scenarios, enabling an understanding of the exact trade-offs between them. Based on the clustering quality and the computational and communication costs, privacy-preserving affinity propagation offers a good trade-off between quality and efficiency for practical privacy-preserving clustering.

  匹配依据：MPC: multi party computation, secure computation

  </details>

- **PolyDot Coded Privacy Preserving Multi-Party Computation at the Edge**
  2021-06-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.08290)
  Elahe Vedadi, Yasaman Keshtkarjahromi, Hulya Seferoglu

  <details><summary>摘要 / Abstract</summary>

  We investigate the problem of privacy preserving distributed matrix multiplication in edge networks using multi-party computation (MPC). Coded multi-party computation (CMPC) is an emerging approach to reduce the required number of workers in MPC by employing coded computation. Existing CMPC approaches usually combine coded computation algorithms designed for efficient matrix multiplication with MPC. We show that this approach is not efficient. We design a novel CMPC algorithm; PolyDot coded MPC (PolyDot-CMPC) by using a recently proposed coded computation algorithm; PolyDot codes. We exploit &quot;garbage terms&quot; that naturally arise when polynomials are constructed in the design of PolyDot-CMPC to reduce the number of workers needed for privacy-preserving computation. We show that entangled polynomial codes, which are consistently better than PolyDot codes in coded computation setup, are not necessarily better than PolyDot-CMPC in MPC setting.

  匹配依据：MPC: multi party computation

  </details>

- **Transforming Secure Comparison Protocol from Passive to Active Adversary Model**
  2021-06-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/795)
  Wei Jiang

  <details><summary>摘要 / Abstract</summary>

  Secure comparison (SC) is an essential primitive in Secure Multiparty Computation (SMC) and a fundamental building block in Privacy-Preserving Data Analytics. Although secure comparison has been studied since the introduction of SMC in the early 80s and many protocols have been proposed, there is still room for improvement, especially providing security against malicious adversaries who form the majority among the participating parties. It is not hard to develop an SC protocol secure against malicious majority based on the current state of the art SPDZ framework. SPDZ is design to work for arbitrary polynomially-bounded functionalities, and it may not provide the most efficient SMC implementation for a specific task, such as SC. In this paper, we propose a novel compiler that is specifically designed to convert most existing SC protocols with semi-honest security into the ones secure against the malicious majority. This compiler provides a flexible and efficient way to achieve both covert and active security for passively secure SC protocols.

  匹配依据：MPC: secure multiparty computation

  </details>

- **LLVM-based Circuit Compilation for Practical Secure Computation**
  2021-06-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/797)
  Tim Heldmann, Thomas Schneider, Oleksandr Tkachenko, Christian Weinert, Hossein Yalame

  <details><summary>摘要 / Abstract</summary>

  Multi-party computation (MPC) allows two or more parties to jointly and securely compute functions over private inputs. Cryptographic protocols that realize MPC require functions to be expressed as Boolean or arithmetic circuits. Deriving such circuits is either done manually, or with hardware synthesis tools and specialized MPC compilers. Unfortunately, such existing tools compile only from a single front-end language and neglect decades of research for optimizing regular compilers. In this paper, we make MPC practical for developers by automating circuit compilation based on the compiler toolchain LLVM. For this, we develop an LLVM optimizer suite consisting of multiple transform passes that operate on the LLVM intermediate representation (IR) and gradually lower functions to circuit level. Our approach supports various front-end languages (currently C, C++, and Fortran) and takes advantage of powerful source code optimizations built into LLVM. We furthermore make sure to produce circuits that are optimized for MPC, and even offer fully automated post-processing for efficient post-quantum MPC. We empirically measure the quality of our compilation results and compare them to the state-of-the-art specialized MPC compiler HyCC (Büscher et al., CCS&#x27;2018). For all benchmarked HyCC example applications (e.g., biomatch and linear equation solving), our highly generalizable approach achieves similar quality in terms of gate count and composition.

  匹配依据：MPC: multi party computation, secure computation

  </details>

- **Hip to Be (Latin) Square: Maximal Period Sequences from Orthogonal Cellular Automata**
  2021-06-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.07750)
  Luca Mariot

  <details><summary>摘要 / Abstract</summary>

  Orthogonal Cellular Automata (OCA) have been recently investigated in the literature as a new approach to construct orthogonal Latin squares for cryptographic applications such as secret sharing schemes. In this paper, we consider OCA for a different cryptographic task, namely the generation of pseudorandom sequences. The idea is to iterate a dynamical system where the output of an OCA pair is fed back as a new set of coordinates on the superposed squares. The main advantage is that OCA ensure a certain amount of diffusion in the generated sequences, a property which is usually missing from traditional CA-based pseudorandom number generators. We study the problem of finding OCA pairs with maximal period by first performing an exhaustive search up to local rules of diameter $d=5$, and then focusing on the subclass of linear bipermutive rules. In this case, we characterize the periods of the sequences in terms of the order of the subgroup generated by an invertible Sylvester matrix. We finally devise an algorithm based on Lagrange&#x27;s theorem to efficiently enumerate all linear OCA pairs of maximal period up to diameter $d=11$.

  匹配依据：MPC: secret sharing

  </details>

- **Vertical Federated Learning without Revealing Intersection Membership**
  2021-06-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.05508)
  Jiankai Sun, Xin Yang, Yuanshun Yao, Aonan Zhang, Weihao Gao, Junyuan Xie, Chong Wang

  <details><summary>摘要 / Abstract</summary>

  Vertical Federated Learning (vFL) allows multiple parties that own different attributes (e.g. features and labels) of the same data entity (e.g. a person) to jointly train a model. To prepare the training data, vFL needs to identify the common data entities shared by all parties. It is usually achieved by Private Set Intersection (PSI) which identifies the intersection of training samples from all parties by using personal identifiable information (e.g. email) as sample IDs to align data instances. As a result, PSI would make sample IDs of the intersection visible to all parties, and therefore each party can know that the data entities shown in the intersection also appear in the other parties, i.e. intersection membership. However, in many real-world privacy-sensitive organizations, e.g. banks and hospitals, revealing membership of their data entities is prohibited. In this paper, we propose a vFL framework based on Private Set Union (PSU) that allows each party to keep sensitive membership information to itself. Instead of identifying the intersection of all training samples, our PSU protocol generates the union of samples as training instances. In addition, we propose strategies to generate synthetic features and labels to handle samples that belong to the union but not the intersection. Through extensive experiments on two real-world datasets, we show our framework can protect the privacy of the intersection membership while maintaining the model utility.

  匹配依据：MPC: private set intersection, private set union

  </details>

- **Reply to: Comment on (t, n) Threshold d-level Quantum Secret Sharing**
  2021-06-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.05488)
  Chuang Li, Longwei Zhang, Xiuli Song

  <details><summary>摘要 / Abstract</summary>

  A corresponding comment, raised by Kao and Hwang, claims that the reconstructor Bob1 is unable to obtain the expected secret information in (t, n) Threshold d-level Quantum Secret Sharing (TDQSS)[Scientific Reports, Vol. 7, No. 1 (2017), pp.6366] . In this reply, we show the TDQSS scheme can obtain the dealer&#x27;s secret information in the condition of adding a step on disentanglement.

  匹配依据：MPC: secret sharing

  </details>

- **Multi-key Private Matching for Compute**
  2021-06-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/770)
  Prasad Buddhavarapu, Benjamin M Case, Logan Gore, Andrew Knox, Payman Mohassel, Shubho Sengupta, Erik Taubeneck, Min Xue

  <details><summary>摘要 / Abstract</summary>

  We extend two-party private set union for secure computation, by considering matching between records having multiple identifiers (or keys), for example email and phone. In the classical setting of this problem, two parties want to perform various downstream computations on the union of two datasets. The union is computed by joining two datasets with the help of a single agreed upon identifier, say email. By extending this to joining records with multiple identifiers, we bring it much closer to real world uses where the match rate and match quality can be greatly improved by considering multiple identifiers. We introduce an extension to the Private-ID protocol [3] which outputs a full outer join (union) of two datasets by a match logic that can join rows containing multiple identifiers. We also introduce new techniques for privately sharding the protocol across multiple servers. Both constructions are based on Decisional Diffie–Hellman (DDH) assumptions.

  匹配依据：MPC: private set union, secure computation

  </details>

- **Asynchronous Data Dissemination and its Applications**
  2021-06-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/777)
  Sourav Das, Zhuolun Xiang, Ling Ren

  <details><summary>摘要 / Abstract</summary>

  In this paper, we introduce the problem of Asynchronous Data Dissemination (ADD). Intuitively, an ADD protocol disseminates a message to all honest nodes in an asynchronous network, given that at least $t+1$ honest nodes initially hold the message where $t$ is the maximum number of malicious nodes. We design a simple and efficient ADD protocol for $n$ parties that is information-theoretically secure, tolerates up to one-third malicious nodes, and has a communication cost of $O(n|M|+n^2)$ for disseminating a message $M$. We then use our ADD protocol to improve many important primitives in cryptography and distributed computing. For asynchronous reliable broadcast (RBC), assuming collision-resistant hash functions, we give a RBC protocol with communication cost $O(n|M| + \kappa n^2)$ where $\kappa$ is the size of the hash function output. This improves over the prior best scheme with communication cost $O(n|M| + \kappa n^2 \log n)$ under the same setting. Our improved RBC protocol immediately improves the communication cost of asynchronous atomic broadcast and Asynchronous Distributed Key Generation~(ADKG) protocols. We also use our improved \rbc\ protocol along with additional new techniques to improve the communication cost of Asynchronous Verifiable Secret Sharing (AVSS), Asynchronous Complete Secret Sharing (ACSS), and dual-threshold \acss\ from $O(\kappa n^2 \log n)$ to $O(\kappa n^2)$ without using any trusted setup.

  匹配依据：MPC: secret sharing

  </details>

- **CloudChain: A Cloud Blockchain Using Shared Memory Consensus and RDMA**
  2021-06-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.04122)
  Minghui Xu, Shuo Liu, Dongxiao Yu, Xiuzhen Cheng, Shaoyong Guo, Jiguo Yu

  <details><summary>摘要 / Abstract</summary>

  Blockchain technologies can enable secure computing environments among mistrusting parties. Permissioned blockchains are particularly enlightened by companies, enterprises, and government agencies due to their efficiency, customizability, and governance-friendly features. Obviously, seamlessly fusing blockchain and cloud computing can significantly benefit permissioned blockchains; nevertheless, most blockchains implemented on clouds are originally designed for loosely-coupled networks where nodes communicate asynchronously, failing to take advantages of the closely-coupled nature of cloud servers. In this paper, we propose an innovative cloud-oriented blockchain -- CloudChain, which is a modularized three-layer system composed of the network layer, consensus layer, and blockchain layer. CloudChain is based on a shared-memory model where nodes communicate synchronously by direct memory accesses. We realize the shared-memory model with the Remote Direct Memory Access technology, based on which we propose a shared-memory consensus algorithm to ensure presistence and liveness, the two crucial blockchain security properties countering Byzantine nodes. We also implement a CloudChain prototype based on a RoCEv2-based testbed to experimentally validate our design, and the results verify the feasibility and efficiency of CloudChain.

  匹配依据：MPC: secure computing

  </details>

- **Tetrad: Actively Secure 4PC for Secure Training and Inference**
  2021-06-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.02850) · [IACR ePrint](https://eprint.iacr.org/2021/755)
  Nishat Koti, Arpita Patra, Rahul Rachuri, Ajith Suresh

  <details><summary>摘要 / Abstract</summary>

  Mixing arithmetic and boolean circuits to perform privacy-preserving machine learning has become increasingly popular. Towards this, we propose a framework for the case of four parties with at most one active corruption called Tetrad. Tetrad works over rings and supports two levels of security, fairness and robustness. The fair multiplication protocol costs 5 ring elements, improving over the state-of-the-art Trident (Chaudhari et al. NDSS&#x27;20). A key feature of Tetrad is that robustness comes for free over fair protocols. Other highlights across the two variants include (a) probabilistic truncation without overhead, (b) multi-input multiplication protocols, and (c) conversion protocols to switch between the computational domains, along with a tailor-made garbled circuit approach. Benchmarking of Tetrad for both training and inference is conducted over deep neural networks such as LeNet and VGG16. We found that Tetrad is up to 4 times faster in ML training and up to 5 times faster in ML inference. Tetrad is also lightweight in terms of deployment cost, costing up to 6 times less than Trident.

  匹配依据：MPC: garbled circuit

  </details>

- **Privacy-Preserving Training of Tree Ensembles over Continuous Data**
  2021-06-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.02769) · [IACR ePrint](https://eprint.iacr.org/2021/754)
  Samuel Adams, Chaitali Choudhary, Martine De Cock, Rafael Dowsley, David Melanson, Anderson C. A. Nascimento, Davis Railsback, Jianwei Shen

  <details><summary>摘要 / Abstract</summary>

  Most existing Secure Multi-Party Computation (MPC) protocols for privacy-preserving training of decision trees over distributed data assume that the features are categorical. In real-life applications, features are often numerical. The standard ``in the clear&#x27;&#x27; algorithm to grow decision trees on data with continuous values requires sorting of training examples for each feature in the quest for an optimal cut-point in the range of feature values in each node. Sorting is an expensive operation in MPC, hence finding secure protocols that avoid such an expensive step is a relevant problem in privacy-preserving machine learning. In this paper we propose three more efficient alternatives for secure training of decision tree based models on data with continuous features, namely: (1) secure discretization of the data, followed by secure training of a decision tree over the discretized data; (2) secure discretization of the data, followed by secure training of a random forest over the discretized data; and (3) secure training of extremely randomized trees (``extra-trees&#x27;&#x27;) on the original data. Approaches (2) and (3) both involve randomizing feature choices. In addition, in approach (3) cut-points are chosen randomly as well, thereby alleviating the need to sort or to discretize the data up front. We implemented all proposed solutions in the semi-honest setting with additive secret sharing based MPC. In addition to mathematically proving that all proposed approaches are correct and secure, we experimentally evaluated and compared them in terms of classification accuracy and runtime. We privately train tree ensembles over data sets with 1000s of instances or features in a few minutes, with accuracies that are at par with those obtained in the clear. This makes our solution orders of magnitude more efficient than the existing approaches, which are based on oblivious sorting.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Cerebro: A Platform for Multi-Party Cryptographic Collaborative Learning**
  2021-06-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/759)
  Wenting Zheng, Ryan Deng, Weikeng Chen, Raluca Ada Popa, Aurojit Panda, Ion Stoica

  <details><summary>摘要 / Abstract</summary>

  Many organizations need large amounts of high-quality data for their applications, and one way to acquire such data is to combine datasets from multiple parties. Since these organizations often own sensitive data that cannot be shared in the clear with others due to policy regulation and business competition, there is increased interest in utilizing secure multi-party computation (MPC). MPC allows multiple parties to jointly compute a function without revealing their inputs to each other. We present Cerebro, an end-to-end collaborative learning platform that enables parties to compute learning tasks without sharing plaintext data. By taking an end-to-end approach to the system design, Cerebro allows multiple parties with complex economic relationships to safely collaborate on machine learning computation through the use of release policies and auditing, while also enabling users to achieve good performance without manually navigating the complex performance tradeoffs between MPC protocols.

  匹配依据：MPC: secure multi party computation

  </details>

- **Appenzeller to Brie: Efficient Zero-Knowledge Proofs for Mixed-Mode Arithmetic and $\\mathbb{Z}\_{2^k}$**
  2021-06-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/750)
  Carsten Baum, Lennart Braun, Alexander Munch-Hansen, Benoit Razet, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  Zero-knowledge proofs are highly flexible cryptographic protocols that are an important building block for many secure systems. Typically, these are defined with respect to statements that are formulated as arithmetic operations over a fixed finite field. This inflexibility is a disadvantage when it comes to complex programs, as some fields are more amenable to express certain operations than others. At the same time, there do not seem to be many proofs with a programming model similar to those found in modern computer architectures that perform arithmetic with 32 or 64 bit integers. In this work, we present solutions to both of these problems. First, we show how to efficiently check consistency of secret values between different instances of zero-knowledge protocols based on the commit-and-prove paradigm. This allows a protocol user to easily switch to the most efficient representation for a given task. To achieve this, we modify the extended doubly-authenticated bits (edabits) approach by Escudero et al. (Crypto 2020), originally developed for MPC, and optimize it for the zero-knowledge setting. As an application of our consistency check, we also introduce protocols for efficiently verifying truncations and comparisons of shared values both modulo a large prime $p$ and modulo $2^k$. Finally, we complement our conversion protocols with new protocols for verifying arithmetic statements in $\mathbb{Z}_{2^k}$. Here, we build upon recent interactive proof systems based on information-theoretic MACs and vector oblivious linear evaluation (VOLE), and show how this paradigm can be adapted to the ring setting. In particular, we show that supporting such modular operations natively in a proof system can be almost as efficient as proofs over large fields or bits, and this also easily plugs into our framework for zero-knowledge conversions.

  匹配依据：MPC: mpc (context)

  </details>

- **A Complete Characterization of Game-Theoretically Fair, Multi-Party Coin Toss**
  2021-06-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/748)
  Ke Wu, Gilad Asharov, Elaine Shi

  <details><summary>摘要 / Abstract</summary>

  Cleve’s celebrated lower bound (STOC’86) showed that a de facto strong fairness notion is impossible in 2-party coin toss, i.e., the corrupt party always has a strategy of biasing the honest party’s outcome by a noticeable amount. Nonetheless, Blum’s famous coin-tossing protocol(CRYPTO’81) achieves a strictly weaker “game-theoretic” notion of fairness — specifically, it is a 2-party coin toss protocol in which neither party can bias the outcome towards its own preference; and thus the honest protocol forms a Nash equilibrium in which neither party would want to deviate. Surprisingly, an n-party analog of Blum’s famous coin toss protocol was not studied till recently. The elegant work by Chung et al. was the first to explore the feasibility of game-theoretically fair n-party coin toss in the presence of corrupt majority. We may assume that each party has a publicly stated preference for either the bit 0 or 1, and if the outcome agrees with the party’s preference, it obtains utility 1; else it obtains nothing.A natural game-theoretic formulation is to require that the honest protocol form a coalition-resistant Nash equilibrium, i.e., no coalition should have incentive to deviate from the honest behavior. Chung et al. phrased this game-theoretic notion as “cooperative-strategy-proofness”or “CSP-fairness” for short. Unfortunately, Chung et al. showed that under (n-1)-sized coalitions, it is impossible to design such a CSP-fair coin toss protocol, unless all parties except one prefer the same bit.In this paper, we show that the impossibility of Chung et al. is in fact not as broad as it may seem. When coalitions are majority but not n-1 in size, we can indeed get feasibility results in some meaningful parameter regimes. We give a complete characterization of the regime in whichCSP-fair coin toss is possible, by providing a matching upper- and lower-bound. Our complete characterization theorem also shows that the mathematical structure of game-theoretic fairness is starkly different from the de facto strong fairness notion in the multi-party computation literature.

  匹配依据：MPC: multi party computation

  </details>

- **Adam in Private: Secure and Fast Training of Deep Neural Networks with Adaptive Moment Estimation**
  2021-06-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.02203) · [IACR ePrint](https://eprint.iacr.org/2021/736)
  Nuttapong Attrapadung, Koki Hamada, Dai Ikarashi, Ryo Kikuchi, Takahiro Matsuda, Ibuki Mishina, Hiraku Morita, Jacob C. N. Schuldt

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving machine learning (PPML) aims at enabling machine learning (ML) algorithms to be used on sensitive data. We contribute to this line of research by proposing a framework that allows efficient and secure evaluation of full-fledged state-of-the-art ML algorithms via secure multi-party computation (MPC). This is in contrast to most prior works, which substitute ML algorithms with approximated &quot;MPC-friendly&quot; variants. A drawback of the latter approach is that fine-tuning of the combined ML and MPC algorithms is required, which might lead to less efficient algorithms or inferior quality ML. This is an issue for secure deep neural networks (DNN) training in particular, as this involves arithmetic algorithms thought to be &quot;MPC-unfriendly&quot;, namely, integer division, exponentiation, inversion, and square root. In this work, we propose secure and efficient protocols for the above seemingly MPC-unfriendly computations. Our protocols are three-party protocols in the honest-majority setting, and we propose both passively secure and actively secure with abort variants. A notable feature of our protocols is that they simultaneously provide high accuracy and efficiency. This framework enables us to efficiently and securely compute modern ML algorithms such as Adam and the softmax function &quot;as is&quot;, without resorting to approximations. As a result, we obtain secure DNN training that outperforms state-of-the-art three-party systems; our full training is up to 6.7 times faster than just the online phase of the recently proposed FALCON@PETS&#x27;21 on a standard benchmark network. We further perform measurements on real-world DNNs, AlexNet and VGG16. The performance of our framework is up to a factor of about 12-14 faster for AlexNet and 46-48 faster for VGG16 to achieve an accuracy of 70% and 75%, respectively, when compared to FALCON.

  匹配依据：MPC: secure evaluation, secure multi party computation

  </details>

- **Side-Channel Protections for Picnic Signatures**
  2021-06-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/735)
  Diego F. Aranha, Sebastian Berndt, Thomas Eisenbarth, Okan Seker, Akira Takahashi, Luca Wilke, Greg Zaverucha

  <details><summary>摘要 / Abstract</summary>

  We study masking countermeasures for side-channel attacks against signature schemes constructed from the MPC-in-the-head paradigm, specifically when the MPC protocol uses preprocessing. This class of signature schemes includes Picnic, an alternate candidate in the third round of the NIST post-quantum standardization project. The only previously known approach to masking MPC-in-the-head signatures suffers from interoperability issues and increased signature sizes. Further, we present a new attack to demonstrate that known countermeasures are not sufficient when the MPC protocol uses a preprocessing phase, as in Picnic3. We overcome these challenges by showing how to mask the underlying zero-knowledge proof system due to Katz--Kolesnikov--Wang (CCS 2018) for any masking order, and by formally proving that our approach meets the standard security notions of non-interference for masking countermeasures. As a case study, we apply our masking technique to Picnic. We then implement different masked versions of Picnic signing providing first order protection for the ARM Cortex M4 platform, and quantify the overhead of these different masking approaches. We carefully analyze the side-channel risk of hashing operations, and give optimizations that reduce the CPU cost of protecting hashing in Picnic by a factor of five. The performance penalties of the masking countermeasures ranged from 1.8 to 5.5, depending on the degree of masking applied to hash function invocations.

  匹配依据：MPC: mpc (context)

  </details>

- **Greenberger-Horne-Zeilinger States: Their Identifications and Robust Violations**
  2021-06-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.01550)
  Xing-Yan Fan, Jie Zhou, Hui-Xian Meng, Chunfeng Wu, Arun Kumar Pati, Jing-Ling Chen

  <details><summary>摘要 / Abstract</summary>

  The $N$-qubit Greenberger-Horne-Zeilinger (GHZ) states are the maximally entangled states of $N$ qubits, which have had many important applications in quantum information processing, such as quantum key distribution and quantum secret sharing. Thus how to distinguish the GHZ states from other quantum states becomes a significant problem. In this work, by presenting a family of the generalized Clauser-Horne-Shimony-Holt (CHSH) inequality, we show that the $N$-qubit GHZ states can be indeed identified by the maximal violations of the generalized CHSH inequality under some specific measurement settings. The generalized CHSH inequality is simple and contains only four correlation functions for any $N$-qubit system, thus has the merit of facilitating experimental verification. Furthermore, we present a quantum phenomenon of robust violations of the generalized CHSH inequality, in which the maximal violation of Bell&#x27;s inequality can be robust under some specific noises adding to the $N$-qubit GHZ states.

  匹配依据：MPC: secret sharing

  </details>

- **GenoPPML – a framework for genomic privacy-preserving machine learning**
  2021-06-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/733)
  Sergiu Carpov, Nicolas Gama, Mariya Georgieva, Dimitar Jetchev

  <details><summary>摘要 / Abstract</summary>

  We present a framework GenoPPML for privacy-preserving machine learning in the context of sensitive genomic data processing. The technology combines secure multiparty computation techniques based on the recently proposed Manticore secure multiparty computation framework for model training and fully homomorphic encryption based on TFHE for model inference. The framework was successfully used to solve breast cancer prediction problems on gene expression datasets coming from distinct private sources while preserving their privacy - the solution winning 1st place for both Tracks I and III of the genomic privacy competition iDASH&#x27;2020. Extensive benchmarks and comparisons to existing works are performed. Our 2-party logistic regression computation is $11\times$ faster than the one in De Cock et al. on the same dataset and it uses only a single CPU core.

  匹配依据：MPC: secure multiparty computation

  </details>

- **A New Approach to Garbled Circuits**
  2021-06-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/739)
  Anasuya Acharya, Tomer Ashur, Efrat Cohen, Carmit Hazay, Avishay Yanai

  <details><summary>摘要 / Abstract</summary>

  A garbling scheme is a fundamental cryptographic building block with a long list of applications. The study of different techniques for garbling a function, towards optimizing computation and communication complexity, has been an area of active research. Most common garbling techniques work by representing each gate in the circuit as a set of ciphertexts that encrypt its truth table row-by-row. In this work we present a new garbling scheme in the random oracle (RO) model that garbles circuits in the gate-by-gate paradigm by capturing the gate functionality (AND, XOR) as a whole rather than as a set of ciphertexts. The final gate garbling requires $4\kappa$ bits of communication in expectation, 4 RO calls for garbling and 1 RO call for evaluation. We prove that the scheme satisfies privacy in the non-programmable random oracle model and against PPT adversaries. We also show how this scheme can be extended to support free-XOR and garble any gate functionality over binary inputs.

  匹配依据：MPC: garbled circuits, garbling scheme

  </details>

- **Some hypersurfaces over finite fields, minimal codes and secret sharing schemes**
  2021-05-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.14508)
  Angela Aguglia, Michela Ceria, Luca Giuzzi

  <details><summary>摘要 / Abstract</summary>

  Linear error-correcting codes can be used for constructing secret sharing schemes; however finding in general the access structures of these secret sharing schemes and, in particular, determining efficient access structures is difficult. Here we investigate the properties of certain algebraic hypersurfaces over finite fields, whose intersection numbers with any hyperplane only takes a few values; these varieties give rise to $q$-divisible linear codes with at most $5$ weights. Furthermore, for $q$ odd these codes turn out to be minimal and we characterize the access structures of the secret sharing schemes based on their dual codes. Indeed, the secret sharing schemes thus obtained are democratic, that is each participant belongs to the same number of minimal access sets and can easily be described.

  匹配依据：MPC: secret sharing

  </details>

- **Tight Setup Bounds for Identifiable Abort**
  2021-05-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/684)
  Nicholas Brandt

  <details><summary>摘要 / Abstract</summary>

  We present fundamental (in-)feasibility results for the strongest security notion for Secure Multi-Party Computation (MPC) that is achievable when a majority of parties is malicious, i.e. security with Identifiable Abort. As general Universally Composable (UC) MPC requires a setup, typically in the form of a Common Reference String or Common-Randomness, we investigate whether the setup must provide randomness to all parties. Given broadcast, we give tight bounds for the necessary and sufficient setup cardinality, i.e. number of participating parties, for UC-MPC protocols with Identifiable Abort. Concretely, we improve previous upper bounds by constructing Secure Function Evaluation for \(n\) parties (\(h\) of which are honest) from setups of cardinality \(\beta := \min(n,\lfloor n/h\rfloor+\lfloor(n-1)/h\rfloor-1)\) and broadcast. Conversely, we present the first general lower bound on the minimal setup cardinality for Identifiable Abort by proving that setups of cardinality \(\beta-1\) plus broadcast are insufficient even for a commitment among \(n\) parties. Somewhat surprisingly, we show that Oblivious Transfer plus broadcast is sufficient for \(n = 2h \geq 2\) which is consistent with the fact that in two-party MPC Identifiable Abort comes for free. We present the results in the Universal Composibility (UC) framework and assume the setup functionalities to be secure with Identifiable Abort. Our constructions yield an efficient (poly-time) protocol for any \(n \in \mathrm{poly}(\lambda)\) where \(\lambda\) is the security parameter if at least a constant fraction \(h \in \Theta(n)\) of parties is honest. However for \(h \in \mathrm{o}(n)\) our results suggest that for efficient protocols the overall number of parties \(n\) is limited quite severely by \(\binom{n}{\beta} \in \mathrm{poly}(\lambda)\).

  匹配依据：MPC: oblivious transfer, secure function evaluation, secure multi party computation

  </details>

- **On Interactive Oracle Proofs for Boolean R1CS Statements**
  2021-05-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/694)
  Ignacio Cascudo, Emanuele Giunta

  <details><summary>摘要 / Abstract</summary>

  The framework of interactive oracle proofs (IOP) has been used with great success to construct a number of efficient transparent zk-SNARKs in recent years. However, these constructions are based on Reed-Solomon codes and can only be applied directly to statements given in the form of arithmetic circuits or R1CS over large fields $\mathbb{F}$ since their soundness error is at least $1/|\mathbb{F}|$. This motivates the question of what is the best way to apply these IOPs to statements that are naturally written as R1CS over small fields, and more concretely, the binary field $\mathbb{F}_2$. While one can just see the system as one over an extension field $\mathbb{F}_{2^e}$ containing $\mathbb{F}_2$, this seems wasteful, as it uses $e$ bits to encode just one ``information&#x27;&#x27; bit. In fact, the recent BooLigero has devised a way to apply the well-known Ligero while being able to encode $\sqrt{e}$ bits into one element of $\mathbb{F}_{2^e}$. In this paper, we introduce a new protocol for $\mathbb{F}_2$-R1CS which among other things relies on a more efficient embedding which (for practical parameters) allows to encode $\geq e/4$ bits into an element of $\mathbb{F}_{2^e}$. Our protocol makes then black box use of lincheck and rowcheck protocols for the larger field. Using the lincheck and rowcheck introduced in Aurora and Ligero respectively we obtain $1.31 - 1.65 \times$ smaller proofs for Aurora and $3.71 \times$ for Ligero. We also estimate the reduction of prover time by a factor of $24.7 \times$ for Aurora and between $6.9 - 32.5 \times$ for Ligero without interactive repetitions. Our methodology uses the notion of reverse multiplication friendly embeddings introduced in the area of secure multiparty computation, combined with a new IOPP to test linear statements modulo a subspace $V \leq \mathbb{F}_{2^e}$ which may be of independent interest.

  匹配依据：MPC: secure multiparty computation

  </details>

- **A Holistic Approach to Enhanced Security and Privacy in Digital Health Passports**
  2021-05-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.13910)
  Tore Kasper Frederiksen

  <details><summary>摘要 / Abstract</summary>

  As governments around the world decide to deploy digital health passports as a tool to curb the spread of Covid-19, it becomes increasingly important to consider how these can be constructed with privacy-by-design. In this paper we discuss the privacy and security issues of common approaches for constructing digital health passports. We then show how to construct, and deploy, secure and private digital health passports, in a simple and efficient manner. We do so by using a protocol for distributed password-based token issuance, secret sharing and by leveraging modern smart phones&#x27; secure hardware. Our solution only requires a constant amount of asymmetric cryptographic operations and a single round of communication between the user and the party verifying the user&#x27;s digital health passport, and only two rounds between the user and the server issuing the digital health passport.

  匹配依据：MPC: secret sharing

  </details>

- **Secure cloud-of-clouds storage with space-efficient secret sharing**
  2021-05-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/666)
  Ahad Niknia, Miguel Correia, Jaber Karimpour

  <details><summary>摘要 / Abstract</summary>

  Cloud storage services are top-rated, but there are often concerns about the security of the files there stored. Clouds-of-clouds or multi-clouds are being explored in order to improve that security. The idea is to store the files in several clouds, ensuring integrity and availability. Confidentiality, however, is obtained by encrypting the files with block ciphers that do not provide provable security. Secret sharing allows distributing files among the clouds providing information-theoretic security/secrecy. However, existing secret sharing schemes are space-inefficient (the size of the shares is much larger than the size of the secret) or purely theoretical. In this paper, we propose the first practical space-efficient secret sharing scheme that provides information-theoretic security, which we denominate PRactical Efficient Secret Sharing (PRESS). Moreover, we present the Secure CloUD storage (SCUD) service, a new cloud-of-clouds storage service that leverages PRESS to provide file confidentiality. Additionally, SCUD provides data integrity and availability, leveraging replication.

  匹配依据：MPC: secret sharing

  </details>

- **Batching Base Oblivious Transfers**
  2021-05-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/682)
  Ian McQuoid, Mike Rosulek, Lawrence Roy

  <details><summary>摘要 / Abstract</summary>

  Protocols that make use of oblivious transfer (OT) rarely require just one instance. Usually a batch of OTs is required --- notably, when generating base OTs for OT extension. There is a natural way to optimize 2-round OT protocols when generating a batch, by reusing certain protocol messages across all instances. In this work we show that this batch optimization is error-prone. We catalog many implementations and papers that have an incorrect treatment of this batch optimization, some of them leading to catastrophic leakage in OT extension protocols. We provide a full treatment of how to properly optimize recent 2-round OT protocols for the batch setting. Along the way we show several performance improvements to the OT protocol of McQuoid, Rosulek, and Roy (ACM CCS 2020). In particular, we show an extremely simple OT construction that may be of pedagogical interest.

  匹配依据：MPC: oblivious transfer

  </details>

- **AOT: Anonymization by Oblivious Transfer**
  2021-05-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.10794) · [IACR ePrint](https://eprint.iacr.org/2021/670)
  Farid Javani, Alan T. Sherman

  <details><summary>摘要 / Abstract</summary>

  We introduce AOT, an anonymous communication system based on mix network architecture that uses oblivious transfer (OT) to deliver messages. Using OT to deliver messages helps AOT resist blending (n−1) attacks and helps AOT preserve receiver anonymity, even if a covert adversary controls all nodes in AOT. AOT comprises three levels of nodes, where nodes at each level perform a different function and can scale horizontally. The sender encrypts their payload and a tag, derived from a secret shared between the sender and receiver, with the public key of a Level-2 node and sends them to a Level-1 node. On a public bulletin board, Level-3 nodes publish tags associated with messages ready to be retrieved. Each receiver checks the bulletin board, identifies tags, and receives the associated messages using OT. A receiver can receive their messages even if the receiver is offline when messages are ready. Through what we call a &quot;handshake&quot; process, communicants can use the AOT protocol to establish shared secrets anonymously. Users play an active role in contributing to the unlinkability of messages: periodically, users initiate requests to AOT to receive dummy messages, such that an adversary cannot distinguish real and dummy requests.

  匹配依据：MPC: oblivious transfer

  </details>

- **On the Algebraic Immunity - Resiliency trade-off, implications for Goldreich's Pseudorandom Generator**
  2021-05-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/649)
  Aurélien Dupin, Pierrick Méaux, Mélissa Rossi

  <details><summary>摘要 / Abstract</summary>

  Goldreich&#x27;s pseudorandom generator is a well-known building block for many theoretical cryptographic constructions from multi-party computation to indistinguishability obfuscation. Its unique efficiency comes from the use of random local functions: each bit of the output is computed by applying some fixed public $n$-variable Boolean function $f$ to a random public size-$n$ tuple of distinct input bits. The characteristics that a Boolean function $f$ must have to ensure pseudorandomness is a puzzling issue. It has been studied in several works and particularly by Applebaum and Lovett (STOC 2016) who showed that resiliency and algebraic immunity are key parameters in this purpose. In this paper, we propose the first study on Boolean functions that reach together maximal algebraic immunity and high resiliency. 1) We assess the possible consequences of the asymptotic existence of such optimal functions. We show how they allow to build functions reaching all possible algebraic immunity-resiliency trade-offs (respecting the algebraic immunity and Siegenthaler bounds). We provide a new bound on the minimal number of variables~$n$, and thus on the minimal locality, necessary to ensure a secure Goldreich&#x27;s pseudorandom generator. Our results come with a granularity level depending on the strength of our assumptions, from none to the conjectured asymptotic existence of optimal functions. 2) We extensively analyze the possible existence and the properties of such optimal functions. Our results show two different trends. On the one hand, we were able to show some impossibility results concerning existing families of Boolean functions that are known to be optimal with respect to their algebraic immunity, starting by the promising XOR-MAJ functions. We show that they do not reach optimality and could be beaten by optimal functions if our conjecture is verified. On the other hand, we prove the existence of optimal functions in low number of variables by experimentally exhibiting some of them up to $12$ variables. This directly provides better candidates for Goldreich&#x27;s pseudorandom generator than the existing XOR-MAJ candidates for polynomial stretches from $2$ to $6$.

  匹配依据：MPC: multi party computation

  </details>

- **Non-Interactive, Secure Verifiable Aggregation for Decentralized, Privacy-Preserving Learning**
  2021-05-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/654)
  Carlo Brunetta, Georgia Tsaloli, Bei Liang, Gustavo Banegas, Aikaterini Mitrokotsa

  <details><summary>摘要 / Abstract</summary>

  We propose a novel primitive called NIVA that allows the distributed aggregation of multiple users&#x27; secret inputs by multiple untrusted servers. The returned aggregation result can be publicly verified in a non-interactive way, i.e. the users are not required to participate in the aggregation except for providing their secret inputs. NIVA allows the secure computation of the sum of a large amount of users&#x27; data and can be employed, for example, in the federated learning setting in order to aggregate the model updates for a deep neural network. We implement NIVA and evaluate its communication and execution performance and compare it with the current state-of-the-art, i.e. Segal et al. protocol (CCS 2017) and Xu et al. VerifyNet protocol (IEEE TIFS 2020), resulting in better user&#x27;s communicated data and

  匹配依据：MPC: secure computation

  </details>

- **Locally Reconstructable Non-malleable Secret Sharing**
  2021-05-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/657)
  Bhavana Kanukurthi, Sai Lakshmi Bhavana Obbattu, Sruthi Sekar, Jenit Tomy

  <details><summary>摘要 / Abstract</summary>

  Non-malleable secret sharing (NMSS) schemes, introduced by Goyal and Kumar (STOC 2018), ensure that a secret $m$ can be distributed into shares $m_1,...,m_n$ (for some $n$), such that any $t$ (a parameter $&lt;=n$) shares can be reconstructed to recover the secret $m$, any $t-1$ shares doesn&#x27;t leak information about $m$ and even if the shares that are used for reconstruction are tampered, it is guaranteed that the reconstruction of these tampered shares will either result in the original $m$ or something independent of $m$. Since their introduction, non-malleable secret sharing schemes sparked a very impressive line of research. In this work, we introduce a feature of local reconstructability in NMSS, which allows reconstruction of any portion of a secret by reading just a few locations of the shares. This is a useful feature, especially when the secret is long or when the shares are stored in a distributed manner on a communication network. In this work, we give a compiler that takes in any non-malleable secret sharing scheme and compiles it into a locally reconstructable non-malleable secret sharing scheme. To secret share a message consisting of $k$ blocks of length $l$ each, our scheme would only require reading $l + log k$ bits (in addition to a few more bits, whose quantity is independent of $l$ and $k$) from each party&#x27;s share (of a reconstruction set) to locally reconstruct a single block of the message. We show an application of our locally reconstructable non-malleable secret sharing scheme to a computational non-malleable secure message transmission scheme in the pre-processing model, with an improved communication complexity, when transmitting multiple messages.

  匹配依据：MPC: secret sharing

  </details>

- **Legendre PRF (Multiple) Key Attacks and the Power of Preprocessing**
  2021-05-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/645)
  Alexander May, Floyd Zweydinger

  <details><summary>摘要 / Abstract</summary>

  Due to its amazing speed and multiplicative properties the Legendre PRF recently finds widespread applications e.g. in Ethereum 2.0, multiparty computation and in the quantum-secure signature proposal LegRoast. However, its security is not yet extensively studied. The Legendre PRF computes for a key $k$ on input $x$ the Legendre symbol $L_k(x) = \left( \frac {x+k} {p} \right)$ in some finite field $\F_p$. As standard notion, PRF security is analysed by giving an attacker oracle access to $L_k(\cdot)$. Khovratovich&#x27;s collision-based algorithm recovers $k$ using $L_k(\cdot)$ in time $\sqrt{p}$ with constant memory. It is a major open problem whether this birthday-bound complexity can be beaten. We show a somewhat surprising wide-ranging analogy between the discrete logarithm problem and Legendre symbol computations. This analogy allows us to adapt various algorithmic ideas from the discrete logarithm setting. More precisely, we present a small memory multiple-key attack on $m$ Legendre keys $k_1, \ldots, k_m$ in time $\sqrt{mp}$, i.e. with amortized cost $\sqrt{p/m}$ per key. This multiple-key attack might be of interest in the Ethereum context, since recovering many keys simultaneously maximizes an attacker&#x27;s profit. Moreover, we show that the Legendre PRF admits precomputation attacks, where the precomputation depends on the public $p$ only -- and not on a key $k$. Namely, an attacker may compute e.g. in precomputation time $p^{\frac 2 3}$ a hint of size $p^{\frac 1 3}$. On receiving access to $L_k(\cdot)$ in an online phase, the attacker then uses the hint to recover the desired key $k$ in time only $p^{\frac 1 3}$. Thus, the attacker&#x27;s online complexity again beats the birthday-bound. In addition, our precomputation attack can also be combined with our multiple-key attack. We explicitly give various tradeoffs between precomputation and online phase. E.g. for attacking $m$ keys one may spend time $mp^{\frac 2 3}$ in the precomputation phase for constructing a hint of size $m^2 p^{\frac 1 3}$. In an online phase, one then finds {\em all $m$ keys in total time} only $p^{\frac 1 3}$. Precomputation attacks might again be interesting in the Ethereum 2.0 context, where keys are frequently changed such that a heavy key-independent precomputation pays off.

  匹配依据：MPC: multiparty computation

  </details>

- **Fed-EINI: An Efficient and Interpretable Inference Framework for Decision Tree Ensembles in Federated Learning**
  2021-05-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.09540)
  Xiaolin Chen, Shuai Zhou, Bei guan, Kai Yang, Hao Fan, Hu Wang, Yongji Wang

  <details><summary>摘要 / Abstract</summary>

  The increasing concerns about data privacy and security drive an emerging field of studying privacy-preserving machine learning from isolated data sources, i.e., federated learning. A class of federated learning, vertical federated learning, where different parties hold different features for common users, has a great potential of driving a great variety of business cooperation among enterprises in many fields. In machine learning, decision tree ensembles such as gradient boosting decision trees (GBDT) and random forest are widely applied powerful models with high interpretability and modeling efficiency. However, stateof-art vertical federated learning frameworks adapt anonymous features to avoid possible data breaches, makes the interpretability of the model compromised. To address this issue in the inference process, in this paper, we firstly make a problem analysis about the necessity of disclosure meanings of feature to Guest Party in vertical federated learning. Then we find the prediction result of a tree could be expressed as the intersection of results of sub-models of the tree held by all parties. With this key observation, we protect data privacy and allow the disclosure of feature meaning by concealing decision paths and adapt a communication-efficient secure computation method for inference outputs. The advantages of Fed-EINI will be demonstrated through both theoretical analysis and extensive numerical results. We improve the interpretability of the model by disclosing the meaning of features while ensuring efficiency and accuracy.

  匹配依据：MPC: secure computation

  </details>

- **Quantum Secure Privacy Preserving Technique to Obtain the Intersection of Two Datasets for Contact Tracing**
  2021-05-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/618)
  Sumit Kumar Debnath, Vikas Srivastava, Tapaswini Mohanty, Nibedita Kundu, Kouichi Sakurai

  <details><summary>摘要 / Abstract</summary>

  Contact tracing has emerged as a powerful and effective measure to curb the spread of contagious diseases. It is a robust tool, but on the downside, it possesses a risk of privacy violations as contact tracing requires gathering a lot of personal information. So there is a need for a cryptographic primitive that obfuscate the personal data of the user. Taking everything into account, private set intersection seems to be the natural choice to address the problem. Nearly all of the existing PSI protocols are relying on the number theoretic assumption based hard problems. However, these problems are not secure in quantum domain. As a consequence, it becomes essential to designing PSI that can resist quantum attack and provide long-term security. One may apply quantum cryptography to develop such PSI protocol. This paper deals with the design of PSI using quantum cryptography (QC), where the security depends on the principles of basic quantum mechanics. Our scheme achieves long-term security and remains secure against quantum attacks due to the use of QC. As opposed to the existing quantum PSI protocols, the communication and computation costs of our scheme are independent of the size of universal set. In particular, the proposed protocol achieves optimal communication and computation costs in the domain of quantum PSI. Moreover, we require only single photon quantum resources and simple single-particle projective measurements, unlike most of the existing quantum PSI protocols.

  匹配依据：MPC: private set intersection

  </details>

- **Privacy-preserving Density-based Clustering**
  2021-05-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/612)
  Beyza Bozdemir, Sébastien Canard, Orhan Ermis, Helen Möllering, Melek Önen, Thomas Schneider

  <details><summary>摘要 / Abstract</summary>

  Clustering is an unsupervised machine learning technique that outputs clusters containing similar data items. In this work, we investigate privacy-preserving density-based clustering which is, for example, used in financial analytics and medical diagnosis. When (multiple) data owners collaborate or outsource the computation, privacy concerns arise. To address this problem, we design, implement, and evaluate the first practical and fully private density-based clustering scheme based on secure two-party computation. Our protocol privately executes the DBSCAN algorithm without disclosing any information (including the number and size of clusters). It can be used for private clustering between two parties as well as for private outsourcing of an arbitrary number of data owners to two non-colluding servers. Our implementation of the DBSCAN algorithm privately clusters data sets with 400 elements in 7 minutes on commodity hardware. Thereby, it flexibly determines the number of required clusters and is insensitive to outliers, while being only factor 19x slower than today&#x27;s fastest private K-means protocol (Mohassel et al., PETS&#x27;20) which can only be used for specific data sets. We then show how to transfer our newly designed protocol to related clustering algorithms by introducing a private approximation of the TRACLUS algorithm for trajectory clustering which has interesting real-world applications like financial time series forecasts and the investigation of the spread of a disease like COVID-19.

  匹配依据：MPC: secure two party computation

  </details>

- **PPCA: Privacy-preserving Principal Component Analysis Using Secure Multiparty Computation(MPC)**
  2021-05-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.07612)
  Xiaoyu Fan, Guosai Wang, Kun Chen, Xu He, Wei Xu

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving data mining has become an important topic. People have built several multi-party-computation (MPC)-based frameworks to provide theoretically guaranteed privacy, the poor performance of real-world algorithms have always been a challenge. Using Principal Component Analysis (PCA) as an example, we show that by considering the unique performance characters of the MPC platform, we can design highly effective algorithm-level optimizations, such as replacing expensive operators and batching up. We achieve about 200$\times$ performance boost over existing privacy-preserving PCA algorithms with the same level of privacy guarantee. Also, using real-world datasets, we show that by combining multi-party data, we can achieve better training results.

  匹配依据：MPC: multi party computation, secure multiparty computation

  </details>

- **Group Structure in Correlations and its Applications in Cryptography**
  2021-05-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/624)
  Guru-Vamsi Policharla, Manoj Prabhakaran, Rajeev Raghunath, Parjanya Vyas

  <details><summary>摘要 / Abstract</summary>

  Correlated random variables are a key tool in cryptographic applications like secure multi-party computation. We investigate the power of a class of correlations that we term group correlations: A group correlation is a uniform distribution over pairs $(x,y) \in G^2$ such that $x+y\in S$, where $G$ is a (possibly non-abelian) group and $S$ is a subset of $G$. We also introduce bi-affine correlations and show how they relate to group correlations. We present several structural results, new protocols, and applications of these correlations. The new applications include a completeness result for black-box group computation, perfectly secure protocols for evaluating a broad class of black box ``mixed-groups&#x27;&#x27; circuits with bi-affine homomorphism, and new information-theoretic results. Finally, we uncover a striking structure underlying OLE: In particular, we show that OLE over $\mathrm{GF}(2^n)$, is isomorphic to a group correlation over $\mathbb{Z}_4^n$.

  匹配依据：MPC: secure multi party computation

  </details>

- **Communication Complexity of Private simultaneous Quantum Messages Protocols**
  2021-05-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.07120) · [IACR ePrint](https://eprint.iacr.org/2021/636)
  Akinori Kawachi, Harumichi Nishimura

  <details><summary>摘要 / Abstract</summary>

  The private simultaneous messages model is a non-interactive version of the multiparty secure computation, which has been intensively studied to examine the communication cost of the secure computation. We consider its quantum counterpart, the private simultaneous quantum messages (PSQM) model, and examine the advantages of quantum communication and prior entanglement of this model. In the PSQM model, $k$ parties $P_1,\ldots,P_k$ initially share a common random string (or entangled states in a stronger setting), and they have private classical inputs $x_1,\ldots, x_k$. Every $P_i$ generates a quantum message from the private input $x_i$ and the shared random string (entangled states), and then sends it to the referee $R$. Receiving the messages, $R$ computes $F(x_1,\ldots,x_k)$. Then, $R$ learns nothing except for $F(x_1,\ldots,x_k)$ as the privacy condition. We obtain the following results for this PSQM model. (1) We demonstrate that the privacy condition inevitably increases the communication cost in the two-party PSQM model as well as in the classical case presented by Applebaum, Holenstein, Mishra, and Shayevitz. In particular, we prove a lower bound $(3-o(1))n$ of the communication complexity in two-party PSQM protocols with a shared random string for random Boolean functions of $2n$-bit input, which is larger than the trivial upper bound $2n$ of the communication complexity without the privacy condition. (2) We demonstrate a factor two gap between the communication complexity of PSQM protocols with shared entangled states and with shared random strings by designing a multiparty PSQM protocol with shared entangled states for a total function that extends the two-party equality function. (3) We demonstrate an exponential gap between the communication complexity of PSQM protocols with shared entangled states and with shared random strings for a two-party partial function.

  匹配依据：MPC: secure computation

  </details>

- **Privacy-preserving Logistic Regression with Secret Sharing**
  2021-05-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.06869)
  Ali Reza Ghavamipour, Fatih Turkmen, Xiaoqian Jian

  <details><summary>摘要 / Abstract</summary>

  Logistic regression (LR) is a widely used classification method for modeling binary outcomes in many medical data classification tasks. Research that collects and combines datasets from various data custodians and jurisdictions can excessively benefit from the increased statistical power to support their analyzing goals. However, combining data from these various sources creates significant privacy concerns that need to be addressed. In this paper, we proposed secret sharing-based privacy-preserving logistic regression protocols using the Newton-Raphson method. Our proposed approaches are based on secure Multi-Party Computation (MPC) with different security settings to analyze data owned by several data holders. We conducted experiments on both synthetic data and real-world datasets and compared the efficiency and accuracy of them with those of an ordinary logistic regression model. Experimental results demonstrate that the proposed protocols are highly efficient and accurate. This study introduces iterative algorithms to simplify the federated training a logistic regression model in a privacy-preserving manner. Our implementation results show that our improved method can handle large datasets used in securely training a logistic regression from multiple sources.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **The FeatureCloud AI Store for Federated Learning in Biomedicine and Beyond**
  2021-05-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.05734)
  Julian Matschinske, Julian Späth, Reza Nasirigerdeh, Reihaneh Torkzadehmahani, Anne Hartebrodt, Balázs Orbán, Sándor Fejér, Olga Zolotareva, Mohammad Bakhtiari, Béla Bihari, Marcus Bloice, Nina C Donner, Walid Fdhila, Tobias Frisch, Anne-Christin Hauschild, Dominik Heider, Andreas Holzinger, Walter Hötzendorfer, Jan Hospes, Tim Kacprowski, Markus Kastelitz, Markus List, Rudolf Mayer, Mónika Moga, Heimo Müller, Anastasia Pustozerova, Richard Röttger, Anna Saranti, Harald HHW Schmidt, Christof Tschohl, Nina K Wenke, Jan Baumbach

  <details><summary>摘要 / Abstract</summary>

  Machine Learning (ML) and Artificial Intelligence (AI) have shown promising results in many areas and are driven by the increasing amount of available data. However, this data is often distributed across different institutions and cannot be shared due to privacy concerns. Privacy-preserving methods, such as Federated Learning (FL), allow for training ML models without sharing sensitive data, but their implementation is time-consuming and requires advanced programming skills. Here, we present the FeatureCloud AI Store for FL as an all-in-one platform for biomedical research and other applications. It removes large parts of this complexity for developers and end-users by providing an extensible AI Store with a collection of ready-to-use apps. We show that the federated apps produce similar results to centralized ML, scale well for a typical number of collaborators and can be combined with Secure Multiparty Computation (SMPC), thereby making FL algorithms safely and easily applicable in biomedical and clinical environments.

  匹配依据：MPC: secure multiparty computation

  </details>

- **An Efficient Learning Framework For Federated XGBoost Using Secret Sharing And Distributed Optimization**
  2021-05-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.05717)
  Lunchen Xie, Jiaqi Liu, Songtao Lu, Tsung-hui Chang, Qingjiang Shi

  <details><summary>摘要 / Abstract</summary>

  XGBoost is one of the most widely used machine learning models in the industry due to its superior learning accuracy and efficiency. Targeting at data isolation issues in the big data problems, it is crucial to deploy a secure and efficient federated XGBoost (FedXGB) model. Existing FedXGB models either have data leakage issues or are only applicable to the two-party setting with heavy communication and computation overheads. In this paper, a lossless multi-party federated XGB learning framework is proposed with a security guarantee, which reshapes the XGBoost&#x27;s split criterion calculation process under a secret sharing setting and solves the leaf weight calculation problem by leveraging distributed optimization. Remarkably, a thorough analysis of model security is provided as well, and multiple numerical results showcase the superiority of the proposed FedXGB compared with the state-of-the-art models on benchmark datasets.

  匹配依据：MPC: secret sharing

  </details>

- **SIRNN: A Math Library for Secure RNN Inference**
  2021-05-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.04236) · [IACR ePrint](https://eprint.iacr.org/2021/459)
  Deevashwer Rathee, Mayank Rathee, Rahul Kranti Kiran Goli, Divya Gupta, Rahul Sharma, Nishanth Chandran, Aseem Rastogi

  <details><summary>摘要 / Abstract</summary>

  Complex machine learning (ML) inference algorithms like recurrent neural networks (RNNs) use standard functions from math libraries like exponentiation, sigmoid, tanh, and reciprocal of square root. Although prior work on secure 2-party inference provides specialized protocols for convolutional neural networks (CNNs), existing secure implementations of these math operators rely on generic 2-party computation (2PC) protocols that suffer from high communication. We provide new specialized 2PC protocols for math functions that crucially rely on lookup-tables and mixed-bitwidths to address this performance overhead; our protocols for math functions communicate up to 423x less data than prior work. Some of the mixed bitwidth operations used by our math implementations are (zero and signed) extensions, different forms of truncations, multiplication of operands of mixed-bitwidths, and digit decomposition (a generalization of bit decomposition to larger digits). For each of these primitive operations, we construct specialized 2PC protocols that are more communication efficient than generic 2PC, and can be of independent interest. Furthermore, our math implementations are numerically precise, which ensures that the secure implementations preserve model accuracy of cleartext. We build on top of our novel protocols to build SIRNN, a library for end-to-end secure 2-party DNN inference, that provides the first secure implementations of an RNN operating on time series sensor data, an RNN operating on speech data, and a state-of-the-art ML architecture that combines CNNs and RNNs for identifying all heads present in images. Our evaluation shows that SIRNN achieves up to three orders of magnitude of performance improvement when compared to inference of these models using an existing state-of-the-art 2PC framework.

  匹配依据：MPC: 2 party computation

  </details>

- **Masked Triples: Amortizing Multiplication Triples across Conditionals**
  2021-05-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/604)
  David Heath, Vladimir Kolesnikov, Stanislav Peceny

  <details><summary>摘要 / Abstract</summary>

  A classic approach to MPC uses preprocessed multiplication triples to evaluate arbitrary Boolean circuits. If the target circuit features conditional branching, e.g. as the result of a IF program statement, then triples are wasted: one triple is consumed per AND gate, even if the output of the gate is entirely discarded by the circuit&#x27;s conditional behavior. In this work, we show that multiplication triples can be re-used across conditional branches. For a circuit with $b$ branches, each having $n$ AND gates, we need only a total of $n$ triples, rather than the typically required $b\cdot n$. Because preprocessing triples is often the most expensive step in protocols that use them, this significantly improves performance. Prior work similarly amortized oblivious transfers across branches in the classic GMW protocol (Heath et al., Asiacrypt 2020, [HKP20]). In addition to demonstrating conditional improvements are possible for a different class of protocols, we also concretely improve over [HKP20]: their maximum improvement is bounded by the topology of the circuit. Our protocol yields improvement independent of topology: we need triples proportional to the size of the program&#x27;s longest execution path, regardless of the structure of the program branches. We implemented our approach in C++. Our experiments show that we significantly improve over a naive protocol and over prior work: for a circuit with $16$ branches and in terms of total communication, we improved over naive by $12\times$ and over [HKP20] by an average of $2.6\times$. Our protocol is secure against the semi-honest corruption of $p-1$ parties.

  匹配依据：MPC: mpc (context)

  </details>

- **Key Assistance, Key Agreement, and Layered Secrecy for Bosonic Broadcast Channels**
  2021-05-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.04033)
  Uzi Pereg, Roberto Ferrara, Matthieu R. Bloch

  <details><summary>摘要 / Abstract</summary>

  Secret-sharing building blocks based on quantum broadcast communication are studied. The confidential capacity region of the pure-loss bosonic broadcast channel is determined, both with and without key assistance, and an achievable region is established for the lossy bosonic broadcast channel. If the main receiver has a transmissivity of η&lt;1/2, then confidentiality solely relies on the key-assisted encryption of the one-time pad. We also address conference key agreement for the distillation of two keys, a public key and a secret key. A regularized formula is derived for the key-agreement capacity region in finite dimensions. In the bosonic case, the key-agreement region is included within the capacity region of the corresponding broadcast channel with confidential messages. We then consider a network with layered secrecy, where three users with different security ranks communicate over the same broadcast network. We derive an achievable layered-secrecy region for a pure-loss bosonic channel that is formed by the concatenation of two beam splitters.

  匹配依据：MPC: secret sharing

  </details>

- **Leakage-Resilient Secret Sharing with Constant Share Size**
  2021-05-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.03074)
  Ivan Tjuawinata, Chaoping Xing

  <details><summary>摘要 / Abstract</summary>

  We consider the leakage resilience of AG code-based ramp secret sharing schemes extending the leakage resilience of linear threshold secret sharing schemes over prime fields done by Benhamouda et al. Since there is not any explicit efficient construction of AG codes over prime fields, we consider constructions over prime fields with the help of concatenation method and those over field extensions. Extending the Fourier analysis done by Benhamouda et al., concatenated algebraic geometric codes over prime fields do produce some nice leakage-resilient secret sharing schemes. One natural and curious question is whether AG codes over extension fields produce better leakage-resilient secret sharing schemes than the construction based on concatenated AG codes. Such construction provides several advantages compared to the construction over prime fields using concatenation method. First, AG codes over extension fields give secret sharing schemes with smaller reconstruction for a fixed privacy parameter t. Second, concatenated AG codes do not enjoy strong multiplicity and hence they are not applicable to secure MPC schemes. It is also confirmed that indeed AG codes over extension fields have stronger leakage-resilience under some reasonable assumptions. These three advantages strongly motivate the study of secret sharing schemes from AG codes over extension fields. The current paper has two main contributions: 1, we obtain leakage-resilient secret sharing schemes with constant share sizes and unbounded numbers of players. Like Shamir secret scheme, our schemes enjoy multiplicity and hence can be applied to MPC. 2, via a sophisticated Fourier Analysis, we analyze the leakage-resilience of secret sharing schemes from codes over extension fields. This is of its own theoretical interest independent of its application to secret sharing schemes from algebraic geometric codes over extension fields.

  匹配依据：MPC: secret sharing

  </details>

- **Resolved Dwarf Galaxy Searches within ~5 Mpc with the Vera Rubin Observatory and Subaru Hyper Suprime-Cam**
  2021-05-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.01658)
  Burçin Mutlu-Pakdil, David J. Sand, Denija Crnojević, Alex Drlica-Wagner, Nelson Caldwell, Puragra Guhathakurta, Anil C. Seth, Joshua D. Simon, Jay Strader, Elisa Toloba

  <details><summary>摘要 / Abstract</summary>

  We present a preview of the faint dwarf galaxy discoveries that will be possible with the Vera C. Rubin Observatory and Subaru Hyper Suprime-Cam in the next decade. In this work, we combine deep ground-based images from the Panoramic Imaging Survey of Centaurus and Sculptor (PISCeS) and extensive image simulations to investigate the recovery of faint, resolved dwarf galaxies in the Local Volume with a matched-filter technique. We adopt three fiducial distances - 1.5, 3.5, 5 Mpc, and quantitatively evaluate the effects on dwarf detection of varied stellar backgrounds, ellipticity, and Milky Way foreground contamination and extinction. We show that our matched-filter method is powerful for identifying both compact and extended systems, and near-future surveys will be able to probe at least ~4.5 mag below the tip of the red giant branch (TRGB) for a distance of up to 1.5 Mpc, and ~2 mag below the TRGB at 5 Mpc. This will push the discovery frontier for resolved dwarf galaxies to fainter magnitudes, lower surface brightnesses, and larger distances. Our simulations show the secure census of dwarf galaxies down to $M_{V}$$\approx$-5, -7, -8, will be soon within reach, out to 1.5 Mpc, 3.5 Mpc, and 5 Mpc, respectively, allowing us to quantify the statistical fluctuations in satellite abundances around hosts, and parse environmental effects as a function of host properties.

  匹配依据：MPC: mpc (context)

  </details>

- **Finding Collisions in Interactive Protocols -- Tight Lower Bounds on the Round and Communication Complexities of Statistically Hiding Commitments**
  2021-05-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.01417)
  Iftach Haitner, Jonathan J. Hoch, Omer Reingold, Gil Segev

  <details><summary>摘要 / Abstract</summary>

  We study the round and communication complexities of various cryptographic protocols. We give tight lower bounds on the round and communication complexities of any fully black-box reduction of a statistically hiding commitment scheme from one-way permutations, and from trapdoor permutations. As a corollary, we derive similar tight lower bounds for several other cryptographic protocols, such as single-server private information retrieval, interactive hashing, and oblivious transfer that guarantees statistical security for one of the parties. Our techniques extend the collision-finding oracle due to Simon (EUROCRYPT &#x27;98) to the setting of interactive protocols and the reconstruction paradigm of Gennaro and Trevisan (FOCS &#x27;00).

  匹配依据：MPC: oblivious transfer

  </details>

- **The return of Eratosthenes: Secure Generation of RSA Moduli using Distributed Sieving**
  2021-05-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/565)
  Cyprien Delpech de Saint Guilhem, Eleftheria Makri, Dragos Rotaru, Titouan Tanguy

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty generation of an RSA biprime is a challenging task, which increasingly receives attention, due to the numerous privacy-preserving applications that require it. In this work, we construct a new protocol for the RSA biprime generation task, secure against a malicious adversary, who can corrupt any subset of protocol participants. Our protocol is designed for generic MPC, making it both platform-independent and allowing for weaker security models to be assumed (e.g., honest majority), should the application scenario require it. By carefully ``postponing&quot; the check of possible inconsistencies in the shares provided by malicious adversaries, we achieve noteworthy efficiency improvements. Concretely, we are able to produce additive sharings of the prime candidates, from multiplicative sharings via a semi-honest multiplication, without degrading the overall (active) security of our protocol. This is the core of our sieving technique, increasing the probability of our protocol sampling a biprime. Similarly, we perform the first biprimality test, requiring several repetitions, without checking input share consistency, and perform the more costly consistency check only in case of success of the Jacobi symbol based biprimality test. Moreover, we propose a protocol to convert an additive sharing over a ring, into an additive sharing over the integers. Besides being a necessary sub-protocol for the RSA biprime generation, this conversion protocol is of independent interest. The cost analysis of our protocol demonstrated that our approach improves the current state-of-the-art (Chen et al. -- Crypto 2020), in terms of communication efficiency. Concretely, for the two-party case with malicious security, and primes of 2048 bits, our protocol improves communication by a factor of ~37.

  匹配依据：MPC: mpc (context)

  </details>

- **Prio+: Privacy Preserving Aggregate Statistics via Boolean Shares**
  2021-05-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/576)
  Surya Addanki, Kevin Garbe, Eli Jaffe, Rafail Ostrovsky, Antigoni Polychroniadou

  <details><summary>摘要 / Abstract</summary>

  This paper introduces Prio+, a privacy-preserving system for the collection of aggregate statistics, with the same model and goals in mind as the original and highly influential Prio paper by Henry Corrigan-Gibbs and Dan Boneh (USENIX 2017). As in the original Prio, each client holds a private data value (e.g. number of visits to a particular website) and a small set of servers privately compute statistical functions over the set of client values (e.g. the average number of visits). To achieve security against faulty or malicious clients, Prio+ clients use Boolean secret-sharing instead of zero-knowledge proofs to convince servers that their data is of the correct form and Prio+ servers execute a share conversion protocols as needed in order to properly compute over client data. This allows us to ensure that clients’ data is properly formatted essentially for free, and the work shifts to novel share-conversion protocols between servers, where some care is needed to make it efficient. While our overall approach is a fairly simple observation in retrospect, it turns out that Prio+ strategy reduces the client’s computational burden by up to two orders of magnitude (or more depending on the statistic) while keeping servers costs comparable to Prio. Prio+ permits computation of exactly the same wide range of complex statistics as the original Prio protocol, including high-dimensional linear regression over private values held by clients. We report detailed benchmarks of our Prio+ implementation and compare these to both the original Go implementation of Prio and the Mozilla implementation of Prio. Our Prio+ software is open-source and released with the same license as Prio.

  匹配依据：MPC: secret sharing

  </details>

- **On the Complexity of Fair Coin Flipping**
  2021-05-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.00780)
  Iftach Haitner, Nikolaos Makriyannis, Eran Omri

  <details><summary>摘要 / Abstract</summary>

  A two-party coin-flipping protocol is $ε$-fair if no efficient adversary can bias the output of the honest party (who always outputs a bit, even if the other party aborts) by more than $ε$. Cleve [STOC &#x27;86] showed that $r$-round $o(1/r)$-fair coin-flipping protocols do not exist. Awerbuch, Blum, Chor, Goldwasser, and Micali[Manuscript &#x27;85] constructed a $Θ(1/\sqrt{r})$-fair coin-flipping protocol, assuming the existence of one-way functions. Moran, Naor, and Segev [Journal of Cryptology &#x27;16] constructed an $r$-round coin-flipping protocol that is $Θ(1/r)$-fair (thus matching the aforementioned lower bound of Cleve [STOC &#x27;86]), assuming the existence of oblivious transfer. The above gives rise to the intriguing question of whether oblivious transfer, or more generally ``public-key primitives,&#x27;&#x27; is required for an $o(1/\sqrt r)$-fair coin flipping protocol. We make a different progress towards answering the question by showing that, for any constant $r\in \N$, the existence of an $1/(c\cdot \sqrt{r})$-fair, $r$-round coin-flipping protocol implies the existence of an infinitely-often key-agreement protocol, where $c$ denotes some universal constant (independent of $r$). Our reduction is \emph{non} black-box and makes a novel use of the recent dichotomy for two-party protocols of Haitner, Nissim, Omri, Shaltiel, and Silbak [FOCS &#x27;18] to facilitate a two-party variant of the recent attack of Beimel, Haitner, Makriyannis, and Omri [FOCS &#x27;18] on multi-party coin-flipping protocols.

  匹配依据：MPC: oblivious transfer

  </details>

- **Characterization of Secure Multiparty Computation Without Broadcast**
  2021-05-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.00732)
  Ran Cohen, Iftach Haitner, Eran Omri, Lior Rotem

  <details><summary>摘要 / Abstract</summary>

  A major challenge in the study of cryptography is characterizing the necessary and sufficient assumptions required to carry out a given cryptographic task. The focus of this work is the necessity of a broadcast channel for securely computing symmetric functionalities (where all the parties receive the same output) when one third of the parties, or more, might be corrupted. Assuming all parties are connected via a peer-to-peer network, but no broadcast channel (nor a secure setup phase) is available, we prove the following characterization: 1) A symmetric $n$-party functionality can be securely computed facing $n/3\le t&lt;n/2$ corruptions (\ie honest majority), if and only if it is \emph{$(n-2t)$-dominated}; a functionality is $k$-dominated, if \emph{any} $k$-size subset of its input variables can be set to \emph{determine} its output. 2) Assuming the existence of one-way functions, a symmetric $n$-party functionality can be securely computed facing $t\ge n/2$ corruptions (\ie no honest majority), if and only if it is $1$-dominated and can be securely computed with broadcast. It follows that, in case a third of the parties might be corrupted, broadcast is necessary for securely computing non-dominated functionalities (in which &quot;small&quot; subsets of the inputs cannot determine the output), including, as interesting special cases, the Boolean XOR and coin-flipping functionalities.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Channels of Small Log-Ratio Leakage and Characterization of Two-Party Differentially Private Computation**
  2021-05-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.00770)
  Iftach Haitner, Noam Mazor, Ronen Shaltiel, Jad Silbak

  <details><summary>摘要 / Abstract</summary>

  Consider a PPT two-party protocol $π=(A,B)$ in which the parties get no private inputs and obtain outputs $O^A,O^B\in \{0,1\}$, and let $V^A$ and $V^B$ denote the parties&#x27; individual views. Protocol $π$ has $α$-agreement if $Pr[O^A=O^B]=1/2+α$. The leakage of $π$ is the amount of information a party obtains about the event $\{O^A=O^B\}$; that is, the leakage $ε$ is the maximum, over $P\in\{A,B\}$, of the distance between $V^P|OA=OB$ and $V^P|OA\neq OB$. Typically, this distance is measured in statistical distance, or, in the computational setting, in computational indistinguishability. For this choice, Wullschleger [TCC 09] showed that if $α&gt;&gt;ε$ then the protocol can be transformed into an OT protocol. We consider measuring the protocol leakage by the log-ratio distance (which was popularized by its use in the differential privacy framework). The log-ratio distance between X,Y over domain Ωis the minimal $ε&gt;0$ for which, for every $v\inΩ$, $log(Pr[X=v]/Pr[Y=v])\in [-ε,ε]$. In the computational setting, we use computational indistinguishability from having log-ratio distance $ε$. We show that a protocol with (noticeable) accuracy $α\inΩ(ε^2)$ can be transformed into an OT protocol (note that this allows $ε&gt;&gt;α$). We complete the picture, in this respect, showing that a protocol with $α\in o(ε^2)$ does not necessarily imply OT. Our results hold for both the information theoretic and the computational settings, and can be viewed as a &quot;fine grained&quot; approach to &quot;weak OT amplification&quot;. We then use the above result to fully characterize the complexity of differentially private two-party computation for the XOR function, answering the open question put by Goyal, Khurana, Mironov, Pandey, and Sahai [ICALP 16] and Haitner, Nissim, Omri, Shaltiel, and Silbak [FOCS 18].

  匹配依据：MPC: two party computation

  </details>

- **GRNN: Generative Regression Neural Network -- A Data Leakage Attack for Federated Learning**
  2021-05-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.00529)
  Hanchi Ren, Jingjing Deng, Xianghua Xie

  <details><summary>摘要 / Abstract</summary>

  Data privacy has become an increasingly important issue in Machine Learning (ML), where many approaches have been developed to tackle this challenge, e.g. cryptography (Homomorphic Encryption (HE), Differential Privacy (DP), etc.) and collaborative training (Secure Multi-Party Computation (MPC), Distributed Learning and Federated Learning (FL)). These techniques have a particular focus on data encryption or secure local computation. They transfer the intermediate information to the third party to compute the final result. Gradient exchanging is commonly considered to be a secure way of training a robust model collaboratively in Deep Learning (DL). However, recent researches have demonstrated that sensitive information can be recovered from the shared gradient. Generative Adversarial Network (GAN), in particular, has shown to be effective in recovering such information. However, GAN based techniques require additional information, such as class labels which are generally unavailable for privacy-preserved learning. In this paper, we show that, in the FL system, image-based privacy data can be easily recovered in full from the shared gradient only via our proposed Generative Regression Neural Network (GRNN). We formulate the attack to be a regression problem and optimize two branches of the generative model by minimizing the distance between gradients. We evaluate our method on several image classification tasks. The results illustrate that our proposed GRNN outperforms state-of-the-art methods with better stability, stronger robustness, and higher accuracy. It also has no convergence requirement to the global FL model. Moreover, we demonstrate information leakage using face re-identification. Some defense strategies are also discussed in this work.

  匹配依据：MPC: secure multi party computation

  </details>

- **EntrapNet: a Blockchain-Based Verification Protocol for Trustless Computing**
  2021-05-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.00146)
  Chong Li, Lei Zhang, Serbiao Fang

  <details><summary>摘要 / Abstract</summary>

  In this paper, we propose a blockchain-based computing verification protocol, called EntrapNet, for distributed shared computing networks, an emerging underlying network for many internet of things (IoT) applications. EntrapNet borrows the idea from the practice of entrapment in criminal law to reduce the possibility of receiving incorrect computing results from trustless service providers who have offered the computing resources. Furthermore, we mathematically optimize EntrapNet to deal with the fundamental tradeoff of a network: security and efficiency. We present an asymptotic optimal solution to this optimization. It will be seen that EntrapNet can be performed as an independent and low-cost layer atop any trustless network that requires outsourced computing, thus making secure computing affordable and practical.

  匹配依据：MPC: secure computing

  </details>

- **Secure Computation by Secret Sharing Using Input Encrypted with Random Number (Full Paper)**
  2021-04-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/548)
  Keiichi Iwamura, Ahmad Akmal Aminuddin Mohd Kamal

  <details><summary>摘要 / Abstract</summary>

  Typically, unconditionally secure computation using a (k,n) threshold secret sharing scheme is considered impossible when n&lt;2k-1. Therefore, in our previous work, we first took the approach of finding the conditions required for secure computation under the setting of n&lt;2k-1 and showed that secure computation using a secret sharing scheme can be realized with a semi-honest adversary under the following three preconditions: (1) the result of secure computation does not include 0; (2) random numbers reconstructed by each server are fixed; and (3) each server holds random numbers unknown to the adversary and holds shares of random numbers that make up the random numbers unknown to the adversary. In this paper, we show that by leaving condition (3), secure computation with information-theoretic security against a semi-honest adversary is possible with k≤n&lt;2k-1. In addition, we clarify the advantage of using secret information that has been encrypted with a random number as input to secure computation. One of the advantages is the acceleration of the computation time. Namely, we divide the computation process into a preprocessing phase and an online phase and shift the cost of communication to the preprocessing phase. Thus, for computations such as inner product operations, we realize a faster online phase, compared with conventional methods.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Two-Server Verifiable Homomorphic Secret Sharing for High-Degree Polynomials**
  2021-04-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.12163)
  Xin Chen, Liang Feng Zhang

  <details><summary>摘要 / Abstract</summary>

  Homomorphic secret sharing (HSS) allows multiple input clients to secret-share their data among multiple servers such that each server is able to locally compute a function on its shares to obtain a partial result and all partial results enable the reconstruction of the function&#x27;s value on the outsourced data by an output client. The existing HSS schemes for {\em high-degree} polynomials either {\em require a large number of servers} or {\em lack verifiability}, which is essential for ensuring the correctness of the outsourced computations. In this paper, we propose a two-server verifiable HSS (VHSS) model and construct a scheme that supports the computation of high-degree polynomials. The degree of the outsourced polynomials can be as high as a polynomial in the system&#x27;s security parameter. Despite of using only 2 servers, our VHSS ensures that each single server learns no information about the outsourced data and no single server is able to persuade the client to output a wrong function value. Our VHSS is significantly more efficient. When computing degree-7 polynomials, our scheme could be 3-10 times faster than the previously best construction.

  匹配依据：MPC: secret sharing

  </details>

- **LogStack: Stacked Garbling with $O(b \\log b)$ Computation**
  2021-04-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/531)
  David Heath, Vladimir Kolesnikov

  <details><summary>摘要 / Abstract</summary>

  Secure two party computation (2PC) of arbitrary programs can be efficiently achieved using garbled circuits (GC). Until recently, it was widely believed that a GC proportional to the entire program, including parts of the program that are entirely discarded due to conditional branching, must be transmitted over a network. Recent work shows that this belief is false, and that communication proportional only to the longest program execution path suffices (Heath and Kolesnikov, CRYPTO 20, [HK20a]). Although this recent work reduces needed communication, it increases computation. For a conditional with $b$ branches, the players use $O(b^2)$ computation (traditional GC uses only $O(b)$). Our scheme LogStack reduces stacked garbling computation from $O(b^2)$ to $O(b \log b)$ with no increase in communication over [HK20a]. The cause of [HK20a]&#x27;s increased computation is the oblivious collection of garbage labels that emerge during the evaluation of inactive branches. Garbage is collected by a multiplexer that is costly to generate. At a high level, we redesign stacking and garbage collection to avoid quadratic scaling. Our construction is also more space efficient: [HK20a] algorithms require $O(b)$ space, while ours use only $O(\log b)$ space. This space efficiency allows even modest setups to handle large numbers of branches. [HK20a] assumes a random oracle (RO). We track the source of this need, formalize a simple and natural added assumption on the base garbling scheme, and remove reliance on RO: LogStack is secure in the standard model. Nevertheless, LogStack can be instantiated with typical GC tricks based on non-standard assumptions, such as free XOR and half-gates, and hence can be implemented with high efficiency. We implemented LogStack (in the RO model, based on half-gates garbling) and report performance. In terms of wall-clock time and for fewer than $16$ branches, our performance is comparable to [HK20a]&#x27;s; for larger branching factors, our approach clearly outperforms [HK20a]. For example, given $1024$ branches, our approach is $31\times$ faster.

  匹配依据：MPC: garbled circuits, garbling scheme, secure two party computation

  </details>

- **Improved Circuit Compilation for Hybrid MPC via Compiler Intermediate Representation**
  2021-04-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/521)
  Daniel Demmler, Stefan Katzenbeisser, Thomas Schneider, Tom Schuster, Christian Weinert

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) allows multiple parties to securely evaluate a public function on their private inputs. The field has steadily moved forward and real-world applications have become practical. However, MPC implementations are often hand-built and require cryptographic knowledge. Thus, special compilers like HyCC (Büscher et al., CCS&#x27;18) have been developed, which automatically compile high-level programs to combinations of Boolean and arithmetic circuits required for mixed-protocol (hybrid) MPC. In this work, we explore the advantages of extending MPC compilers with an intermediate representation (IR) as commonly used in modern compiler infrastructures. For this, we extend HyCC with a graph-based IR that facilitates the implementation of well-known algorithms from compiler design as well as further MPC-specific optimizations. We demonstrate the benefits by implementing arithmetic decomposition based on our new IR that automatically extracts arithmetic expressions and then compiles them into separate circuits. For a line intersection algorithm, we require 40% less run-time and improve total communication by a factor of 3x compared to regular HyCC when securely evaluating the corresponding circuit with the hybrid MPC framework ABY (Demmler et al., NDSS&#x27;15).

  匹配依据：MPC: secure multi party computation

  </details>

- **How to Share and Own a Secret**
  2021-04-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/518)
  Victor Ermolaev, Gamze Tillem

  <details><summary>摘要 / Abstract</summary>

  Custodian service is a service safeguarding a firm&#x27;s or individual&#x27;s financial assets or secret information. Such services often present a user with security versus ownership dilemma. The user does not wish to pass full control over their asset to the custodian to facilitate safeguarding. A control sharing mechanism allowing the custodian to hold enough information and keeping the user as the owner of the asset is required. For the assets being secret information, cryptographic protocols addressing this dilemma are known as prepositioned secret sharing~(PSS) protocols. PSS schemes distinguish redundant ``common&#x27;&#x27; shares and specific ``activating&#x27;&#x27; shares controlling the very possibility of the secret information reconstruction. Usually, PSS schemes: 1) lack robustness with respect to the amount of ``common&#x27;&#x27; shares, i.e., a high redundancy degree in ``common&#x27;&#x27; enables them to reconstruct the secret without ``activation&#x27;&#x27;, and 2) are inflexible in configuring the robustness of the ``activating&#x27;&#x27; shares, i.e., how many ``activating&#x27;&#x27; shares can be lost or stolen before the secret can be reconstructed. In this paper, we present a PSS addressing these shortcomings.

  匹配依据：MPC: secret sharing

  </details>

- **CryptGPU: Fast Privacy-Preserving Machine Learning on the GPU**
  2021-04-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.10949) · [IACR ePrint](https://eprint.iacr.org/2021/533)
  Sijun Tan, Brian Knott, Yuan Tian, David J. Wu

  <details><summary>摘要 / Abstract</summary>

  We introduce CryptGPU, a system for privacy-preserving machine learning that implements all operations on the GPU (graphics processing unit). Just as GPUs played a pivotal role in the success of modern deep learning, they are also essential for realizing scalable privacy-preserving deep learning. In this work, we start by introducing a new interface to losslessly embed cryptographic operations over secret-shared values (in a discrete domain) into floating-point operations that can be processed by highly-optimized CUDA kernels for linear algebra. We then identify a sequence of &quot;GPU-friendly&quot; cryptographic protocols to enable privacy-preserving evaluation of both linear and non-linear operations on the GPU. Our microbenchmarks indicate that our private GPU-based convolution protocol is over 150x faster than the analogous CPU-based protocol; for non-linear operations like the ReLU activation function, our GPU-based protocol is around 10x faster than its CPU analog. With CryptGPU, we support private inference and private training on convolutional neural networks with over 60 million parameters as well as handle large datasets like ImageNet. Compared to the previous state-of-the-art, when considering large models and datasets, our protocols achieve a 2x to 8x improvement in private inference and a 6x to 36x improvement for private training. Our work not only showcases the viability of performing secure multiparty computation (MPC) entirely on the GPU to enable fast privacy-preserving machine learning, but also highlights the importance of designing new MPC primitives that can take full advantage of the GPU&#x27;s computing capabilities.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Sharing classical secrets with continuous-variable entanglement: Composable security and network coding advantage**
  2021-04-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.10659)
  Nathan Walk, Jens Eisert

  <details><summary>摘要 / Abstract</summary>

  Secret sharing is a multi-party cryptographic primitive that can be applied to a network of partially distrustful parties for encrypting data that is both sensitive (it must remain secure) and important (it must not be lost or destroyed). When sharing classical secrets (as opposed to quantum states), one can distinguish between protocols that leverage bi-partite quantum key distribution (QKD) and those that exploit multi-partite entanglement. The latter class are known to be vulnerable to so-called participant attacks and, while progress has been made recently, there is currently no analysis that quantifies their performance in the composable, finite-size regime which has become the gold standard for QKD security. Given this - and the fact that distributing multi-partite entanglement is typically challenging - one might well ask: Is there any virtue in pursuing multi-partite entanglement based schemes? Here, we answer this question in the affirmative for a class of secret sharing protocols based on continuous variable graph states. We establish security in a composable framework and identify a network topology, specifically a bottleneck network of lossy channels, and parameter regimes within the reach of present day experiments for which a multi-partite scheme outperforms the corresponding QKD based method in the asymptotic and finite-size setting. Finally, we establish experimental parameters where the multi-partite schemes outperform any possible QKD based protocol. This one of the first concrete compelling examples of multi-partite entangled resources achieving a genuine advantage over point-to-point protocols for quantum communication and represents a rigorous, operational benchmark to assess the usefulness of such resources.

  匹配依据：MPC: secret sharing

  </details>

- **Secure Quantum Secret Sharing without Signal Disturbance Monitoring**
  2021-04-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.10321)
  Hua-Lei Yin, Jie Gu, Yuan-Mei Xie, Wen-Bo Liu, Yao Fu, Zeng-Bing Chen

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) is an essential primitive for the future quantum internet, which promises secure multiparty communication. However, developing a large-scale QSS network is a huge challenge due to the channel loss and the requirement of multiphoton interference or high-fidelity multipartite entanglement distribution. Here, we propose a three-user QSS protocol without monitoring signal disturbance, which is capable of ensuring the unconditional security. The final key rate of our protocol can be demonstrated to break the Pirandola-Laurenza-Ottaviani-Banchi bound of quantum channel and its simulated transmission distance can approach over 600 km using current techniques. Our results pave the way to realizing high-rate and large-scale QSS networks.

  匹配依据：MPC: secret sharing

  </details>

- **zkHawk: Practical Private Smart Contracts from MPC-based Hawk**
  2021-04-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2104.09180) · [IACR ePrint](https://eprint.iacr.org/2021/501)
  Aritra Banerjee, Michael Clear, Hitesh Tewari

  <details><summary>摘要 / Abstract</summary>

  Cryptocurrencies have received a lot of research attention in recent years following the release of the first cryptocurrency Bitcoin. With the rise in cryptocurrency transactions, the need for smart contracts has also increased. Smart contracts, in a nutshell, are digitally executed contracts wherein some parties execute a common goal. The main problem with most of the current smart contracts is that there is no privacy for a party&#x27;s input to the contract from either the blockchain or the other parties. Our research builds on the Hawk project that provides transaction privacy along with support for smart contracts. However, Hawk relies on a special trusted party known as a manager, which must be trusted not to leak each party&#x27;s input to the smart contract. In this paper, we present a practical private smart contract protocol that replaces the manager with an MPC protocol such that the function to be executed by the MPC protocol is relatively lightweight, involving little overhead added to the smart contract function, and uses practical sigma protocols and homomorphic commitments to prove to the blockchain that the sum of the incoming balances to the smart contract matches the sum of the outgoing balances.

  匹配依据：MPC: mpc (context)

  </details>

- **Cryptanalysis of Boyen’s Attribute-Based Encryption Scheme in TCC 2013**
  2021-04-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/505)
  Shweta Agrawal, Rajarshi Biswas, Ryo Nishimaki, Keita Xagawa, Xiang Xie, Shota Yamada

  <details><summary>摘要 / Abstract</summary>

  In TCC 2013, Boyen suggested the first lattice based construction of attribute based encryption (ABE) for the circuit class $NC1$. Unfortunately, soon after, a flaw was found in the security proof of the scheme. However, it remained unclear whether the scheme is actually insecure, and if so, whether it can be repaired. Meanwhile, the construction has been heavily cited and continues to be extensively studied due to its technical novelty. In particular, this is the first lattice based ABE which uses linear secret sharing schemes (LSSS) as a crucial tool to enforce access control. In this work, we show that the scheme is in fact insecure. To do so, we provide a polynomial-time attack that completely breaks the security of the scheme. We suggest a route to fix the security of the scheme, via the notion of admissible linear secret sharing schemes (LSSS) and instantiate these for the class of DNFs. Subsequent to our work, Datta, Komargodski and Waters (Eurocrypt 2021) provided a construction of admissible LSSS for NC1 and resurrected Boyen&#x27;s claimed result.

  匹配依据：MPC: secret sharing

  </details>

- **Almost-Asynchronous MPC under Honest Majority, Revisited**
  2021-04-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/503)
  Matthieu Rambaud, Antoine Urban

  <details><summary>摘要 / Abstract</summary>

  Multiparty computation does not tolerate $n/3$ corruptions under a plain asynchronous communication network, whatever the computational assumptions. However, Beerliová-Hirt-Nielsen [BHN, Podc&#x27;10] showed that, assuming access to a synchronous broadcast at the beginning of the protocol, enables to tolerate up to $t&lt;n/2$ corruptions. This model is denoted as ``Almost asynchronous&#x27;&#x27; MPC. Yet, their work [BHN] has limitations: (i) \emph{Setup assumptions:} their protocol is based on an encryption scheme, with homomorphic additivity, which requires that a trusted entity gives to players secret shares of a global decryption key ahead of the protocol. It was left as an open question in [BHN] whether one can remove this assumption, denoted as ``trusted setup&#x27;&#x27;. (ii) \emph{Common Randomness generation:} the generation of threshold additively homomorphic encrypted randomness uses the broadcast, therefore is allowed only at the beginning of the protocol (iii) \emph{Proactive security:} the previous limitation directly precludes the possibility of tolerating a mobile adversary. Indeed, tolerance to this kind of adversary, which is denoted as ``proactive&#x27;&#x27; MPC, would require, in the above setup, a mechanism by which players refresh their secret shares of the global key, which requires \emph{on-the-fly} generation of common randomness. (iv) \emph{Triple generation latency: } The protocol to preprocess the material necessary for multiplication has latency $t$, which is thus linear in the number of players. We remove all the previous limitations. Of independent interest, the novel computation framework that we introduce for proactivity, revolves around players denoted as ``kings&#x27;&#x27;, which, in contrast to Podc&#x27;10, are now \emph{replaceable} after every elementary step of the computation.

  匹配依据：MPC: multiparty computation

  </details>

- **Efficient Scalable Multi-Party Private Set Intersection Using Oblivious PRF**
  2021-04-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/484)
  Alireza Kavousi, Javad Mohajeri, Mahmoud Salmasizadeh

  <details><summary>摘要 / Abstract</summary>

  In this paper, we present a concretely efficient protocol for private set intersection (PSI) in the multi-party setting using oblivious pseudorandom function (OPRF). In fact, we generalize the approach used in the work of Chase and Miao [CRYPTO 2020] towards deploying a lightweight multi-point OPRF construction for two-party PSI. Our protocol only includes oblivious transfer (OT) extension and garbled Bloom filter as its main ingredients and avoids computationally expensive operations. From a communication pattern perspective, the protocol consists of two types of interactions. The first type is performed over a star-like communication graph in which one designated party interacts with all other parties via performing OTs as the sender. Besides, parties communicate through a path-like communication graph that involves sending a garbled Bloom filter from the first party to its neighboring party following the last one. This design makes our protocol to be highly scalable due to the independence of each party&#x27;s complexity from the number of participating parties and thus causes a communication and computation complexities of $O(n\lambda k)$, where $n$ is the set size, $k$ is the number of hash functions, and $\lambda$ is the security parameter. Moreover, the asymptotic complexity of the designated party is $O(tn\lambda)$ which linearly scales with the number of parties $t$. We prove security of the proposed protocol against semi-honest adversaries.

  匹配依据：MPC: oblivious transfer, private set intersection

  </details>
