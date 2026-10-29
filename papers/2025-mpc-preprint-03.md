# 2025 · MPC · 仅预印本来源 · 第 3/5 页

[总目录](../PAPERS.md) · [上一页](2025-mpc-preprint-02.md) · [下一页](2025-mpc-preprint-04.md)

- **Privacy-Preserving Inference for Quantized BERT Models**
  2025-08-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.01636)
  Tianpei Lu, Bingsheng Zhang, Lekun Peng, Bowen Zheng, Lichun Li, Kui Ren

  <details><summary>摘要 / Abstract</summary>

  With the increasing deployment of generative machine learning models in privacy-sensitive domains such as healthcare and personalized services, ensuring secure inference has become a critical challenge. Secure multi-party computation (MPC) enables privacy-preserving model inference but suffers from high communication and computation overhead. The main bottleneck lies in the expensive secure evaluation of floating-point operations. Quantization offers a promising solution by converting floating-point operations into lower-precision integer computations, significantly reducing overhead. However, existing MPC-based quantized inference methods either rely on public quantization parameters-posing privacy risks-or suffer from inefficiencies, particularly in handling nonlinear functions such as activations and softmax. In this work, we propose a fine-grained, layer-wise quantization scheme and support 1-bit weight fully connected layers in a secure setting. We design a multi-input lookup table protocol to evaluate softmax efficiently and securely. Furthermore, we use dual secret sharing schemes and perform precision conversions via lookup tables, eliminating truncation overhead entirely. Experimental evaluation on BERT-base models demonstrates that our approach achieves up to $8\times$ speedup compared to Lu \emph{et al}. (NDSS 25), $9\times$ speedup compared to Gupta \emph{et al}. (PETS 24) and $22 \times$ speedup compared to Knott \emph{et al}. (NeurIPS 21).

  匹配依据：MPC: secret sharing, secure evaluation, secure multi party computation

  </details>

- **A Survey on Privacy-Preserving Computing in the Automotive Domain**
  2025-08-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2508.01798)
  Nergiz Yuca, Nikolay Matyunin, Ektor Arzoglou, Nikolaos Athanasios Anagnostopoulos, Stefan Katzenbeisser

  <details><summary>摘要 / Abstract</summary>

  As vehicles become increasingly connected and autonomous, they accumulate and manage various personal data, thereby presenting a key challenge in preserving privacy during data sharing and processing. This survey reviews applications of Secure Multi-Party Computation (MPC) and Homomorphic Encryption (HE) that address these privacy concerns in the automotive domain. First, we identify the scope of privacy-sensitive use cases for these technologies, by surveying existing works that address privacy issues in different automotive contexts, such as location-based services, mobility infrastructures, traffic management, etc. Then, we review recent works that employ MPC and HE as solutions for these use cases in detail. Our survey highlights the applicability of these privacy-preserving technologies in the automotive context, while also identifying challenges and gaps in the current research landscape. This work aims to provide a clear and comprehensive overview of this emerging field and to encourage further research in this domain.

  匹配依据：MPC: secure multi party computation

  </details>

- **Scalable Secure Multiparty Computation with Perfect Security from Preprocessing**
  2025-08-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1406)
  Yifan Song, Xiaxi Ye

  <details><summary>摘要 / Abstract</summary>

  In this work, we study the communication complexity of MPC achieving perfect security with optimal resilience ($t&lt;n/3$). We ask the question: ``Is it possible to build a perfectly secure MPC for arithmetic circuits of size $|C|$ with optimal resilience with communication of $o(|C|\cdot n)$ field elements?&#x27;&#x27; On the positive side, we construct a perfectly secure MPC protocol for general arithmetic circuits with communication complexity of $O(|C|)$ elements assuming preprocessing data of size $O(|C|)$, where the preprocessing data consists of packed Beaver triples over bivariate polynomials. Furthermore, we show that packed Beaver triples over bivariate polynomials can be prepared at an amortized cost of $O(1)$ elements plus $O(1)$ three-party Beaver triples per secret. On the negative side, we establish a communication lower bound proving that preparing packed Beaver triples over bivariate polynomials requires at least $\Omega(n)$ elements of communication per secret. This lower bound is derived by first proving a communication lower bound for verifying the correctness of packed Beaver triples with perfect security with abort, and then efficiently reducing the task of verifying packed Beaver triples to preparing packed Beaver triples over bivariate polynomials. To match this bound, we give a concrete construction for preparing packed Beaver triples over bivariate polynomials with $O(n)$ elements per secret, demonstrating the tightness of our lower bound. Our proof technique also extends to show that for the task of computing the inner-product of two length-$|C|$ vectors, any MPC protocol that achieves perfect security with abort requires either $\Omega(|C|\cdot n)$ elements of communication or $\Omega(|C|)$ elements of preprocessing data.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Peeking Into the Future: MPC Resilient to Super-Rushing Adversaries**
  2025-08-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1394)
  Gilad Asharov, Anirudh Chandramouli, Ran Cohen, Yuval Ishai

  <details><summary>摘要 / Abstract</summary>

  An important requirement in synchronous protocols is that, even when a party receives all its messages for a given round ahead of time, it must wait until the round officially concludes before sending its messages for the next round. In practice, however, implementations often overlook this waiting requirement. This leads to a mismatch between the security analysis and real-world deployments, giving adversaries a new, unaccounted-for capability: the ability to ``peek into the future.&#x27;&#x27; Specifically, an adversary can force certain honest parties to advance to round $r+1$, observe their round $r+1$ messages, and then use this information to determine its remaining round $r$ messages. We refer to adversaries with this capability as ``super-rushing&quot; adversaries. We initiate a study of secure computation in the presence of super-rushing adversaries. We focus on understanding the conditions under which existing synchronous protocols remain secure in the presence of super-rushing adversaries. We show that not all protocols remain secure in this model, highlighting a critical gap between theoretical security guarantees and practical implementations. Even worse, we show that security against super-rushing adversaries is not necessarily maintained under sequential composition. Despite those limitations, we present a general positive result: secret-sharing based protocols in the perfect setting, such as BGW, or those that are based on multiplication triplets, remain secure against super-rushing adversaries. This general theorem effectively enhances the security of such protocols ``for free.&#x27;&#x27; It shows that these protocols do not require parties to wait for the end of a round, enabling potential optimizations and faster executions without compromising security. Moreover, it shows that there is no need to spend efforts to achieve perfect synchronization when establishing the communication networks for such protocols.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **FLEX — Capital-Efficient Optimistic Bridges with On-Demand Security Bonds for Bitcoin**
  2025-07-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1392)
  Sergio Demian Lerner, Ariel Futoransky

  <details><summary>摘要 / Abstract</summary>

  This paper presents FLEX (Fraud proofs with Lightweight Escrows for eXits), a garbled circuit-based protocol designed to facilitate two-party disputes on Bitcoin without requiring permanent security bonds. FLEX enables conditional security deposits that are only activated in the event of a dispute, reducing the financial overhead for both parties. The main goal of FLEX is to improve the capital efficiency of BitVM-based bridges in a permissioned challenge setting but can also be used to improve the security of any other fraud proof-based protocol such as payment channels. The paper also introduces enhancements that allow faster reimbursements in scenarios where one party&#x27;s node is unavailable, while preserving security and minimizing race conditions.

  匹配依据：MPC: garbled circuit

  </details>

- **Concrete Security Bounds for Simulation-Based Proofs of Multi-Party Computation Protocols**
  2025-07-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.22705)
  Kristina Sojakova, Mihai Codescu, Joshua Gancher

  <details><summary>摘要 / Abstract</summary>

  The concrete security paradigm aims to give precise bounds on the probability that an adversary can subvert a cryptographic mechanism. This is in contrast to asymptotic security, where the probability of subversion may be eventually small, but large enough in practice to be insecure. Fully satisfactory concrete security bounds for Multi-Party Computation (MPC) protocols are difficult to attain, as they require reasoning about the running time of cryptographic adversaries and reductions. In this paper we close this gap by introducing a new foundational approach that allows us to automatically compute concrete security bounds for MPC protocols. We take inspiration from the meta-theory of IPDL, a prior approach for formally verified distributed cryptography, to support reasoning about the runtime of protocols and adversarial advantage. For practical proof developments, we implement our approach in Maude, an extensible logic for equational rewriting. We carry out four case studies of concrete security for simulation-based proofs. Most notably, we deliver the first formal verification of the GMW MPC protocol over N parties. To our knowledge, this is the first time that formally verified concrete security bounds are computed for a proof of an MPC protocol in the style of Universal Composability. Our tool provides a layer of abstraction that allows the user to write proofs at a high level, which drastically simplifies the proof size. For comparison, a case study that in prior works required 2019 LoC only takes 567 LoC, thus reducing proof size by 72%

  匹配依据：MPC: multi party computation

  </details>

- **Collaborative zkSNARKs with Sublinear Prover Time and Constant Proof Size**
  2025-07-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1388)
  Zhiyong Fang, Sanjam Garg, Bhaskar Roberts, Wenxuan Wu, Yupeng Zhang

  <details><summary>摘要 / Abstract</summary>

  Collaborative zkSNARKs, proposed by Ozdemir and Boneh in 2022, allow a prover to delegate the generation of zkSNARK proofs to multiple servers, without compromising the confidentiality of the secret witness. They enable the use of zkSNARK techniques on computational limited devices in critical applications such as blockchains. However, the running time of each server is at least as slow as computing the proof on a single server. Garg et al. attempted to improve the efficiency in their scheme named zkSaaS using packed secret sharing, but the scheme still requires a powerful central server with linear computation, communication and memory usage. In this paper, we propose a new collaborative zkSNARK scheme with $O(\frac{C}{n}\log\frac{C}{n})$ prover time and $O(1)$ proof size with $n$ servers for a circuit of size $C$. An adversary compromising less than $\frac{n}{4}$ servers cannot learn any information about the witness. The core of our technique lies in a new zkSNARK scheme for the Plonkish constraint system that is friendly to packed secret sharing. We utilize bivariate polynomials to avoid a large Fast Fourier Transform on the entire witness, which was the major bottleneck in prior work. We also construct permutation constraints based on logarithmic derivatives and univariate sumcheck to avoid the computation of prefix products. Finally, we build a bivariate polynomial commitment scheme that can be computed directly on packed secret shares. Experimental results show that for a circuit of size $2^{20}$, with 128 servers, our scheme can accelerate the proof generation by 36.2$\times$ compared to running the zkSNARK on a single server. The prover time of our system is 25.9$\times$ faster than the prior work of zkSaaS. The proof size of our scheme is only 960 Bytes.

  匹配依据：MPC: secret sharing

  </details>

- **Guard-GBDT: Efficient Privacy-Preserving Approximated GBDT Training on Vertical Dataset**
  2025-07-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.20688) · [Code](https://github.com/XidianNSS/Guard-GBDT.git)
  Anxiao Song, Shujie Cui, Jianli Bai, Ke Cheng, Yulong Shen, Giovanni Russello

  <details><summary>摘要 / Abstract</summary>

  In light of increasing privacy concerns and stringent legal regulations, using secure multiparty computation (MPC) to enable collaborative GBDT model training among multiple data owners has garnered significant attention. Despite this, existing MPC-based GBDT frameworks face efficiency challenges due to high communication costs and the computation burden of non-linear operations, such as division and sigmoid calculations. In this work, we introduce Guard-GBDT, an innovative framework tailored for efficient and privacy-preserving GBDT training on vertical datasets. Guard-GBDT bypasses MPC-unfriendly division and sigmoid functions by using more streamlined approximations and reduces communication overhead by compressing the messages exchanged during gradient aggregation. We implement a prototype of Guard-GBDT and extensively evaluate its performance and accuracy on various real-world datasets. The results show that Guard-GBDT outperforms state-of-the-art HEP-XGB (CIKM&#x27;21) and SiGBDT (ASIA CCS&#x27;24) by up to $2.71\times$ and $12.21 \times$ on LAN network and up to $2.7\times$ and $8.2\times$ on WAN network. Guard-GBDT also achieves comparable accuracy with SiGBDT and plaintext XGBoost (better than HEP-XGB ), which exhibits a deviation of $\pm1\%$ to $\pm2\%$ only. Our implementation code is provided at https://github.com/XidianNSS/Guard-GBDT.git.

  匹配依据：MPC: secure multiparty computation

  </details>

- **An Attack to Universally Composable Commitments from Malicious Physically Uncloneable Functions and how to Avoid it**
  2025-07-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1374)
  Lourenço Abecasis, Paulo Mateus, Chrysoula Vlachou

  <details><summary>摘要 / Abstract</summary>

  In this work, we explore the possibility of unconditionally secure universally composable (UC) commitments, a very relevant cryptographic primitive in the context of secure multi-party computation. To this end, we assume the existence of Physically Uncloneable Functions (PUFs), a hardware security assumption that has been proven useful for securely achieving diverse tasks. In prior work [ASIACRYPT 2013, LNCS, vol. 8270, pp. 100–119] it was shown that a protocol for unconditional UC-secure commitments can be constructed even when the PUFs are malicious. Here, we report an attack to this protocol, as well as a few more issues that we identified in its construction. To address them, first we revise some of the previous PUF properties, and introduce new properties and tools that allow us to rigorously develop and present the security proofs. Second, we propose two different ways for making the commitment scheme secure against the attack we found. The first involves considering a new model where the creator of a PUF is notified whenever the PUF is queried and the second involves restricting adversaries to only being able to create stateless malicious PUFs. Finally, we analyze the efficiency of our schemes and show that our constructions are advantageous in this respect compared to the original proposal.

  匹配依据：MPC: secure multi party computation

  </details>

- **Quantum Secret Sharing with Classical and Quantum Shares**
  2025-07-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.17364)
  Hua Sun

  <details><summary>摘要 / Abstract</summary>

  In quantum secret sharing, a quantum secret state is mapped to multiple shares such that shares from qualified sets can recover the secret state and shares from other forbidden sets reveal nothing about the secret state; we study the setting where there are both classical shares and quantum shares. We show that the quantum secret sharing problem with both classical and quantum shares is feasible if and only if any two qualified sets have some quantum share in common. Next, for threshold quantum secret sharing where there are $N_1$ classical shares, $N_2$ quantum shares and qualified sets consist of any $K_1$ (or more) classical shares and any $K_2 &gt; N_2/2$ (or more) quantum shares, we show that to share $1$ qubit secret, each classical share needs to be at least $2$ bits and each quantum share needs to be at least $1$ qubit. Finally, we characterize the minimum share sizes for quantum secret sharing with at most $2$ classical shares and at most $2$ quantum shares. The converse proofs rely on quantum information inequalities and the achievable schemes use classical secret sharing, (encrypted) quantum secret sharing with only quantum shares, superdense coding, treating quantum digits as classical digits, and their various combinations.

  匹配依据：MPC: secret sharing

  </details>

- **Minimax Data Sanitization with Distortion Constraint and Adversarial Inference**
  2025-07-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.17942)
  Amirarsalan Moatazedian, Yauhen Yakimenka, Rémi A. Chou, Jörg Kliewer

  <details><summary>摘要 / Abstract</summary>

  We study a privacy-preserving data-sharing setting where a privatizer transforms private data into a sanitized version observed by an authorized reconstructor and two unauthorized adversaries, each with access to side information correlated with the private data. The reconstructor is evaluated under a distortion function, while each adversary is evaluated using a separate loss function. The privatizer ensures the reconstructor distortion remains below a fixed threshold while maximizing the minimum loss across the two adversaries. This two-adversary setting models cases where individual users cannot reconstruct the data accurately, but their combined side information enables estimation within the distortion threshold. The privatizer maximizes individual loss while permitting accurate reconstruction only through collaboration. This echoes secret-sharing principles, but with lossy rather than perfect recovery. We frame this as a constrained data-driven minimax optimization problem and propose a data-driven training procedure that alternately updates the privatizer, reconstructor, and adversaries. We also analyze the Gaussian and binary cases as special scenarios where optimal solutions can be obtained. These theoretical optimal results are benchmarks for evaluating the proposed minimax training approach.

  匹配依据：MPC: secret sharing

  </details>

- **How to share Multipartite Entanglement in a Real-World Linear Network Connecting Two Metropoles**
  2025-07-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.17480)
  Janka Memmen, Anna Pappa

  <details><summary>摘要 / Abstract</summary>

  The development of large-scale quantum communication networks necessitates the efficient distribution of quantum states to enable advanced cryptographic applications and distributed tasks. Multipartite entanglement is a key resource in many of these proposals, yet its generation is experimentally challenging, especially in noisy and lossy networks. While a substantial body of work focuses on the distribution of multi-partite entanglement in star-like topologies, practical implementations often rely on linear network structures constrained by existing infrastructure. In this work, we investigate the generation of high-fidelity multipartite entangled states in a realistic quantum network, leveraging the existing infrastructure of the Q-net-Q project - a real-world long-distance link connecting Berlin and Frankfurt via seven trusted relay nodes. Given that only bipartite entanglement sources are available in our setting and that the network is highly lossy, we explore the role of quantum memories in enhancing multi-partite entanglement distribution and identify key performance requirements. Furthermore, we analyze the feasibility and performance of cryptographic primitives - including (Anonymous) Conference Key Agreement and Quantum Secret Sharing - highlighting the scenarios where the use of multipartite entanglement yields clear advantages.

  匹配依据：MPC: secret sharing

  </details>

- **The Matrix Subcode Equivalence problem and its application to signature with MPC-in-the-Head**
  2025-07-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.15377)
  Magali Bardet, Charles Brion, Philippe Gaborit, Mercedes Haiech, Romaric Neveu

  <details><summary>摘要 / Abstract</summary>

  Nowadays, equivalence problems are widely used in cryptography, most notably to establish cryptosystems such as digital signatures, with MEDS, LESS, PERK as the most recent ones. However, in the context of matrix codes, only the code equivalence problem has been studied, while the subcode equivalence is well-defined in the Hamming metric. In this work, we introduce two new problems: the Matrix Subcode Equivalence Problem and the Matrix Code Permuted Kernel Problem, to which we apply the MPCitH paradigm to build a signature scheme. These new problems, closely related to the Matrix Code Equivalence problem, ask to find an isometry given a code $C$ and a subcode $D$. Furthermore, we prove that the Matrix Subcode Equivalence problem reduces to the Hamming Subcode Equivalence problem, which is known to be NP-Complete, thus introducing the matrix code version of the Permuted Kernel Problem. We also adapt the combinatorial and algebraic algorithms for the Matrix Code Equivalence problem to the subcode case, and we analyze their complexities. We find with this analysis that the algorithms perform much worse than in the code equivalence case, which is the same as what happens in the Hamming metric. Finally, our analysis of the attacks allows us to take parameters much smaller than in the Matrix Code Equivalence case. Coupled with the effectiveness of \textit{Threshold-Computation-in-the-Head} or \textit{VOLE-in-the-Head}, we obtain a signature size of $\approx$ 4 800 Bytes, with a public key of $\approx$ 275 Bytes. We thus obtain a reasonable signature size, which brings diversity in the landscape of post-quantum signature schemes, by relying on a new hard problem. In particular, this new signature scheme performs better than SPHINCS+, with a smaller size of public key + signature. Our signature compares also well with other signature schemes: compared to MEDS, the signature is smaller, and we reduced the size of the sum of signature and public key by a factor close to 5. We also obtain a signature size that is almost half the size of the CROSS signature scheme.

  匹配依据：MPC: mpc (context)

  </details>

- **Privacy-Preserving Multimodal News Recommendation through Federated Learning**
  2025-07-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.15460)
  Mehdi Khalaj, Shahrzad Golestani Najafabadi, Julita Vassileva

  <details><summary>摘要 / Abstract</summary>

  Personalized News Recommendation systems (PNR) have emerged as a solution to information overload by predicting and suggesting news items tailored to individual user interests. However, traditional PNR systems face several challenges, including an overreliance on textual content, common neglect of short-term user interests, and significant privacy concerns due to centralized data storage. This paper addresses these issues by introducing a novel multimodal federated learning-based approach for news recommendation. First, it integrates both textual and visual features of news items using a multimodal model, enabling a more comprehensive representation of content. Second, it employs a time-aware model that balances users&#x27; long-term and short-term interests through multi-head self-attention networks, improving recommendation accuracy. Finally, to enhance privacy, a federated learning framework is implemented, enabling collaborative model training without sharing user data. The framework divides the recommendation model into a large server-maintained news model and a lightweight user model shared between the server and clients. The client requests news representations (vectors) and a user model from the central server, then computes gradients with user local data, and finally sends their locally computed gradients to the server for aggregation. The central server aggregates gradients to update the global user model and news model. The updated news model is further used to infer news representation by the server. To further safeguard user privacy, a secure aggregation algorithm based on Shamir&#x27;s secret sharing is employed. Experiments on a real-world news dataset demonstrate strong performance compared to existing systems, representing a significant advancement in privacy-preserving personalized news recommendation.

  匹配依据：MPC: secret sharing

  </details>

- **VMask: Tunable Label Privacy Protection for Vertical Federated Learning via Layer Masking**
  2025-07-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.14629)
  Juntao Tan, Lan Zhang, Zhonghao Hu, Kai Yang, Peng Ran, Bo Li

  <details><summary>摘要 / Abstract</summary>

  Though vertical federated learning (VFL) is generally considered to be privacy-preserving, recent studies have shown that VFL system is vulnerable to label inference attacks originating from various attack surfaces. Among these attacks, the model completion (MC) attack is currently the most powerful one. Existing defense methods against it either sacrifice model accuracy or incur impractical computational overhead. In this paper, we propose VMask, a novel label privacy protection framework designed to defend against MC attack from the perspective of layer masking. Our key insight is to disrupt the strong correlation between input data and intermediate outputs by applying the secret sharing (SS) technique to mask layer parameters in the attacker&#x27;s model. We devise a strategy for selecting critical layers to mask, reducing the overhead that would arise from naively applying SS to the entire model. Moreover, VMask is the first framework to offer a tunable privacy budget to defenders, allowing for flexible control over the levels of label privacy according to actual requirements. We built a VFL system, implemented VMask on it, and extensively evaluated it using five model architectures and 13 datasets with different modalities, comparing it to 12 other defense methods. The results demonstrate that VMask achieves the best privacy-utility trade-off, successfully thwarting the MC attack (reducing the label inference accuracy to a random guessing level) while preserving model performance (e.g., in Transformer-based model, the averaged drop of VFL model accuracy is only 0.09%). VMask&#x27;s runtime is up to 60,846 times faster than cryptography-based methods, and it only marginally exceeds that of standard VFL by 1.8 times in a large Transformer-based model, which is generally acceptable.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Drone Navigation Through Homomorphic Encryption for Collision Avoidance**
  2025-07-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.14713)
  Allan Luedeman, Nicholas Baum, Andrew Quijano, Kemal Akkaya

  <details><summary>摘要 / Abstract</summary>

  As drones increasingly deliver packages in neighborhoods, concerns about collisions arise. One solution is to share flight paths within a specific zip code, but this compromises business privacy by revealing delivery routes. For example, it could disclose which stores send packages to certain addresses. To avoid exposing path information, we propose using homomorphic encryption-based comparison to compute path intersections. This allows drones to identify potential collisions without revealing path and destination details, allowing them to adjust altitude to avoid crashes. We implemented and tested our approach on resource-limited virtual machines to mimic the computational power of drones. Our results demonstrate that our method is significantly faster and requires less network communication compared to a garbled circuit-based approach. We also provide a security analysis of the approach against potential attacks.

  匹配依据：MPC: garbled circuit

  </details>

- **FORTA: Byzantine-Resilient FL Aggregation via DFT-Guided Krum**
  2025-07-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.14588)
  Usayd Shahul, J. Harshan

  <details><summary>摘要 / Abstract</summary>

  Secure federated learning enables collaborative model training across decentralized users while preserving data privacy. A key component is secure aggregation, which keeps individual updates hidden from both the server and users, while also defending against Byzantine users who corrupt the aggregation. To this end, Jinhyun So et al. recently developed a Byzantine-resilient secure aggregation scheme using a secret-sharing strategy over finite-field arithmetic. However, such an approach can suffer from numerical errors and overflows when applied to real-valued model updates, motivating the need for secure aggregation methods that operate directly over the real domain. We propose FORTA, a Byzantine-resilient secure aggregation framework that operates entirely in the real domain. FORTA leverages Discrete Fourier Transform (DFT) codes for privacy and employs Krum-based outlier detection for robustness. While DFT decoder is error-free under infinite precision, finite precision introduces numerical perturbations that can distort distance estimates and allow malicious updates to evade detection. To address this, FORTA refines Krum using feedback from DFT decoder, improving the selection of trustworthy updates. Theoretical analysis and experiments show that our modification of Krum offers improved robustness and more accurate aggregation than standard Krum.

  匹配依据：MPC: secret sharing

  </details>

- **Threshold Receipt-Free Voting with Server-Side Vote Validation**
  2025-07-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1321)
  Thi Van Thao Doan, Olivier Pereira, Thomas Peters

  <details><summary>摘要 / Abstract</summary>

  Proving the validity of ballots is a central element of verifiable elections. Such proofs can however create challenges when one desires to make a protocol receipt-free. We explore the challenges raised by validity proofs in the context of protocols where threshold receipt-freeness is obtained by secret sharing an encryption of a vote between multiple authorities. In such contexts, previous solutions verified the validity of votes by decrypting them after passing them through a mix-net. This approach however creates subtle privacy risks, especially when invalid votes leak structural patterns that threaten receipt-freeness. We propose a different approach of threshold receipt-free voting in which authorities re-randomize ballot shares then jointly compute a ZK proof of ballot validity before letting the ballots enter a (possibly homomorphic) tallying phase. Our approach keeps the voter computational costs limited while offering verifiability and improving the ballot privacy of previous solutions. We present two protocols that enable a group of servers to verify and publicly prove that encrypted votes satisfy some validity properties: Minimix, which preserves prior voter-side behavior with minimal overhead, and Homorand, which requires voters to submit auxiliary data to facilitate validation over large vote domains. We show how to use our two protocols within a threshold receipt-free voting framework. We provide formal security proofs and efficiency analyses to illustrate trade-offs in our designs.

  匹配依据：MPC: secret sharing

  </details>

- **NetAdapt: Network-Adaptive Hybrid Protocol Assignment for PPML**
  2025-07-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1315)
  Yuntian Chen, Tianpei Lu, Zhanyong Tang, Bingsheng Zhang, Zhiyuan Ning, Zhiying Shi, Kui Ren

  <details><summary>摘要 / Abstract</summary>

  The widespread use of machine learning on sensitive data makes Privacy-Preserving Machine Learning (PPML) essential for data confidentiality. Current state-of-the-art PPML systems employ hybrid protocol designs to evaluate various operators to achieve better performance; yet, existing hybrid approaches adopt fixed protocol assignments without considering the deployment setting, resulting in inefficiencies across diverse network environments, such as LANs and WANs. To address this, we introduce NetAdapt, a cost-model-driven framework that automatically assigns FHE and MPC protocols to optimize inference efficiency under varying network conditions, by designing a predictive cost model based on the dialect of the Multi-Level Intermediate Representation (MLIR)’s Tensor Operator Set Architecture (TOSA), and an ILP-based solver for managing the cross-protocol conversion while dynamically updating FHE costs based on homomorphic multiplication depth. Experimental results demonstrate that NetAdapt delivers $6.68\times$ to $12.92\times$ improvements in inference running time compared to state-of-the-art solutions, allowing network-agnostic PPML.

  匹配依据：MPC: mpc (context)

  </details>

- **FunBic-CCA: Function Secret Sharing for Biclusterings Applied to Cheng and Church Algorithm (Extended Version)**
  2025-07-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1317)
  Shokofeh VahidianSadegh, Alberto Ibarrondo, Lena Wiese

  <details><summary>摘要 / Abstract</summary>

  High-throughput technologies (e.g., the microarray) have fostered the rapid growth of gene expression data collection. These biomedical datasets, increasingly distributed among research institutes and hospitals, fuel various machine learning applications such as anomaly detection, prediction or clustering. In particular, unsupervised classification techniques based on biclustering like the Cheng and Church Algorithm (CCA) have proven to adapt particularly well to gene expression data. However, biomedical data is highly sensitive, hence its sharing across multiple entities introduces privacy and security concerns, with an ever-present threat of accidental disclosure or leakage of private patient information. To address such threat, this work introduces a novel, highly efficient privacy-preserving protocol based on secure multiparty computation (MPC) between two servers to compute CCA. Our protocol performs operations relying on an additive secret sharing and function secret sharing, leading us to reformulate the steps of the CCA into MPC-friendly equivalents. Leveraging lightweight cryptographic primitives, our new technique named FunBic-CCA is first to exploit the efficiency of function secret sharing to achieve fast evaluation of the CCA biclustering algorithm.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **FuSeFL: Fully Secure and Scalable Federated Learning**
  2025-07-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.13591)
  Sahar Ghoflsaz Ghinani, Elaheh Sadredini

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) enables collaborative model training without centralizing client data, making it attractive for privacy-sensitive domains. While existing approaches employ cryptographic techniques such as homomorphic encryption, differential privacy, or secure multiparty computation to mitigate inference attacks, including model inversion, membership inference, and gradient leakage, they often suffer from high computational and memory overheads. Moreover, many methods overlook the confidentiality of the global model itself, which may be proprietary and sensitive. These challenges limit the practicality of secure FL, especially in settings that involve large datasets and strict compliance requirements. We present FuSeFL, a Fully Secure and scalable FL scheme, which decentralizes training across client pairs using lightweight MPC, while confining the server&#x27;s role to secure aggregation, client pairing, and routing. This design eliminates server bottlenecks, avoids full data offloading, and preserves full confidentiality of data, model, and updates throughout training. Based on our experiment, FuSeFL defends against unauthorized observation, reconstruction attacks, and inference attacks such as gradient leakage, membership inference, and inversion attacks, while achieving up to $13 \times$ speedup in training time and 50% lower server memory usage compared to our baseline.

  匹配依据：MPC: secure multiparty computation

  </details>

- **A Privacy-Preserving Framework for Advertising Personalization Incorporating Federated Learning and Differential Privacy**
  2025-07-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.12098)
  Xiang Li, Yifan Lin, Yuanzhe Zhang

  <details><summary>摘要 / Abstract</summary>

  To mitigate privacy leakage and performance issues in personalized advertising, this paper proposes a framework that integrates federated learning and differential privacy. The system combines distributed feature extraction, dynamic privacy budget allocation, and robust model aggregation to balance model accuracy, communication overhead, and privacy protection. Multi-party secure computing and anomaly detection mechanisms further enhance system resilience against malicious attacks. Experimental results demonstrate that the framework achieves dual optimization of recommendation accuracy and system efficiency while ensuring privacy, providing both a practical solution and a theoretical foundation for applying privacy protection technologies in advertisement recommendation.

  匹配依据：MPC: secure computing

  </details>

- **AlphaFL: Secure Aggregation with Malicious$^2$ Security for Federated Learning against Dishonest Majority**
  2025-07-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1289)
  Yufan Jiang, Maryam Zarezadeh, Tianxiang Dai, Stefan Köpsell

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) proposes to train a global machine learning model across distributed datasets. However, the aggregation protocol as the core component in FL is vulnerable to well-studied attacks, such as inference attacks, poisoning attacks [71] and malicious participants who try to deviate from the protocol [24]. Therefore, it is crucial to achieve both malicious security and poisoning resilience from cryptographic and FL perspectives, respectively. Prior works either achieve incomplete malicious security [76], address issues by using expensive cryptographic tools [22, 59] or assume the availability of a clean dataset on the server side [32]. In this work, we propose AlphaFL, a two-server secure aggregation protocol achieving both malicious security in the universal composability (UC) framework [19] and poisoning resilience in FL (thus malicious$^2$) against a dishonest majority. We design maliciously secure multi-party computation (MPC) protocols [24, 26, 48] and introduce an efficient input commitment protocol tolerating server-client collusion (dishonest majority). We also propose an efficient input commitment protocol for the non-collusion case (honest majority), which triples the efficiency in time and quadruples that in communication, compared to the state-of-the-art solution in MP-SPDZ [46]. To achieve poisoning resilience, we carry out $L_\infty$ and $L_2$-Norm checks with a dynamic $L_2$-Norm bound by introducing a novel silent select protocol, which improves the runtime by at least two times compared to the classic select protocol. Combining these, AlphaFL achieves malicious$^2$ security at a cost of 25% − 79% more runtime overhead than the state-of-the-art semi-malicious counterpart Elsa [76], with even less communication cost.

  匹配依据：MPC: secure multi party computation

  </details>

- **A note on the security of the BitVM3 garbling scheme**
  2025-07-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1291)
  Ariel Futoransky, Gabriel Larotonda, Fadi Barbara

  <details><summary>摘要 / Abstract</summary>

  We provide minimal counterexamples for the security of the BitVM3 garbling scheme: our attack allows the evaluator to forge input and output wires. Then we use the same idea to exhibit an attack on the forward label propagation garbling scheme proposed in a more recent paper. In both cases, the authenticity property of the garbling scheme is broken.

  匹配依据：MPC: garbling scheme

  </details>

- **Split Happens: Combating Advanced Threats with Split Learning and Function Secret Sharing**
  2025-07-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.10494)
  Tanveer Khan, Mindaugas Budzys, Antonis Michalas

  <details><summary>摘要 / Abstract</summary>

  Split Learning (SL) -- splits a model into two distinct parts to help protect client data while enhancing Machine Learning (ML) processes. Though promising, SL has proven vulnerable to different attacks, thus raising concerns about how effective it may be in terms of data privacy. Recent works have shown promising results for securing SL through the use of a novel paradigm, named Function Secret Sharing (FSS), in which servers obtain shares of a function they compute and operate on a public input hidden with a random mask. However, these works fall short in addressing the rising number of attacks which exist on SL. In SplitHappens, we expand the combination of FSS and SL to U-shaped SL. Similarly to other works, we are able to make use of the benefits of SL by reducing the communication and computational costs of FSS. However, a U-shaped SL provides a higher security guarantee than previous works, allowing a client to keep the labels of the training data secret, without having to share them with the server. Through this, we are able to generalize the security analysis of previous works and expand it to different attack vectors, such as modern model inversion attacks as well as label inference attacks. We tested our approach for two different convolutional neural networks on different datasets. These experiments show the effectiveness of our approach in reducing the training time as well as the communication costs when compared to simply using FSS while matching prior accuracy.

  匹配依据：MPC: secret sharing

  </details>

- **Several new classes of self-orthogonal minimal linear codes violating the Ashikhmin-Barg condition**
  2025-07-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.09856)
  Wengang Jin, Kangquan Li, Longjiang Qu

  <details><summary>摘要 / Abstract</summary>

  Linear codes have attracted considerable attention in coding theory and cryptography due to their significant applications in secret sharing schemes, secure two-party computation, Galois geometries, among others. As two special subclasses of linear codes, minimal linear codes and self-orthogonal linear codes are of particular interest. Constructing linear codes that possess both minimality and self-orthogonality is very interesting. The main purpose of this paper is to construct self-orthogonal minimal linear codes that violate the Ashikhmin-Barg (AB for short) condition over the finite field $\mathbb{F}_p$. First, we present several classes of self-orthogonal minimal linear codes violating the AB condition over the finite field $\mathbb{F}_2$ and determine their weight distributions. Next, for any odd prime $p$, we construct two classes of self-orthogonal linear codes from $p$-ary functions, which contain some optimal or almost optimal codes. Finally, based on plateaued functions, we construct two classes of self-orthogonal linear codes that violate the AB condition. Their weight distributions are also provided. To the best of our knowledge, this paper is the first to investigate the constructions of linear codes that violate the AB condition and satisfy self-orthogonality.

  匹配依据：MPC: secret sharing, secure two party computation

  </details>

- **Access Control for Information-Theoretically Secure Key-Document Stores**
  2025-07-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.10730)
  Yin Li, Sharad Mehrota, Shantanu Sharma, Komal Kumari

  <details><summary>摘要 / Abstract</summary>

  This paper presents a novel key-based access control technique for secure outsourcing key-value stores where values correspond to documents that are indexed and accessed using keys. The proposed approach adopts Shamir&#x27;s secret-sharing that offers unconditional or information-theoretic security. It supports keyword-based document retrieval while preventing leakage of the data, access rights of users, or the size (\textit{i}.\textit{e}., volume of the output that satisfies a query). The proposed approach allows servers to detect (and abort) malicious clients from gaining unauthorized access to data, and prevents malicious servers from altering data undetected while ensuring efficient access -- it takes 231.5ms over 5,000 keywords across 500,000 files.

  匹配依据：MPC: secret sharing

  </details>

- **A Hybrid Algorithm for the Regular Syndrome Decoding Problem**
  2025-07-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1284)
  Tianrui Wang, Anyu Wang, Kang Yang, Hanlin Liu, Yu Yu, Jun Zhang, Xiaoyun Wang

  <details><summary>摘要 / Abstract</summary>

  Regular Syndrome Decoding (RSD) is a variant of the traditional Syndrome Decoding (SD) problem, where the error vector is divided into consecutive, equal-length blocks, each containing exactly one nonzero element. Recently, RSD has gained significant attention due to its extensive applications in cryptographic constructions, including MPC, ZK protocols, and more. The computational complexity of RSD has primarily been analyzed using two methods: Information Set Decoding (ISD) approach and algebraic approach. In this paper, we introduce a new hybrid algorithm for solving the RSD problem. This algorithm can be viewed as replacing the meet-in-the-middle enumeration in ISD with a process that solves quadratic equations. Our new algorithm demonstrates superior performance across a wide range of concrete parameters compared to previous methods, including both ISD and algebraic approaches, for parameter sets over both large fields (q = 2^128) and binary fields (q = 2). For parameter sets used in prior works, our algorithm reduces the concrete security of RSD by up to 20 bits compared to the state-of-the-art algorithms. We also provide an asymptotic analysis, identifying a broader parameter region where RSD is solvable in polynomial time compared to ISD and algebraic methods over binary fields. Additionally, we apply our algorithm to evaluate the security of the ZK protocol Wolverine (IEEE S&amp;P 2021) and the OT protocol Ferret (ACM CCS 2020). Our results reduce the security level of Wolverine, which targets a 128-bit security level, to about 111 bits, and also marginally lowers the security of Ferret below the targeted 128-bit level for the first time.

  匹配依据：MPC: mpc (context)

  </details>

- **Multi-Authority Registered Attribute-Based Encryption**
  2025-07-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1279)
  George Lu, Brent Waters, David J. Wu

  <details><summary>摘要 / Abstract</summary>

  Registered attribute-based encryption (ABE) enables fine-grained access control to encrypted data without a trusted authority. In this model, users generate their own public keys and register their public key along with a set of attributes with a key curator. The key curator aggregates the public keys into a short master public key that functions as the public key for an ABE scheme. A limitation of ABE (registered or centralized) is the assumption that a single entity manages all of the attributes in a system. In many settings, the attributes belong to different organizations, making it unrealistic to expect that a single entity manage all of them. In the centralized setting, this motivated the notion of multi-authority ABE, where multiple independent authorities control their individual set of attributes. Access policies are then defined over attributes across multiple authorities. In this work, we introduce multi-authority registered ABE, where multiple (independent) key curators each manage their individual sets of attributes. Users can register their public keys with any key curator, and access policies can be defined over attributes from multiple key curators. Multi-authority registered ABE combines the trustless nature of registered ABE with the decentralized nature of multi-authority ABE. We start by constructing a multi-authority registered ABE scheme from composite-order pairing groups. This scheme supports an a priori bounded number of users and access policies that can be represented by a linear secret sharing scheme (which includes monotone Boolean formulas). Our construction relies on a careful integration of ideas from pairing-based registered ABE and multi-authority ABE schemes. We also construct a multi-authority registered ABE scheme that supports an unbounded number of users and arbitrary monotone policies using indistinguishability obfuscation (and function-binding hash functions).

  匹配依据：MPC: secret sharing

  </details>

- **Efficient and High-Accuracy Private CNN Inference with Helper-Assisted Malicious Security**
  2025-07-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.09607)
  Kaiwen Wang, Xiaolin Chang, Junchao Fan, Yuehan Dong

  <details><summary>摘要 / Abstract</summary>

  Machine Learning as a Service (MLaaS) exposes sensitive client data to service providers. Private inference mitigates this risk while preserving model functionality. Despite extensive progress in MPC-based solutions, they remain constrained by a fundamental three-way tension among strong security, efficiency, and model accuracy. This challenge is particularly acute under the malicious dishonest majority (MSDM) setting, where prior work either incurs high communication overhead or suffers non-negligible accuracy loss due to polynomial approximations of nonlinear functions. Although the helper-assisted MSDM (HA-MSDM) model improves efficiency and fairness, it lacks a dedicated design for accurate and efficient neural network inference. In this work, we present an HA-MSDM-based private CNN inference framework that simultaneously achieves high efficiency and near-plaintext accuracy through a co-design of cryptographic primitives, MPC protocols, and model training. Specifically, we (i) extend authenticated sharing to rings to enable efficient fixed-point computation, (ii) design constant-round protocols for multiplication and polynomial evaluation, with round complexity independent of the polynomial degree, and (iii) introduce a training strategy that recovers the expressiveness of polynomial models via knowledge distillation and warm initialization. Experiments demonstrate 2.3--6.8$\times$ speedup in LAN and 1.3--5.6$\times$ in WAN over state-of-the-art MSDM frameworks, while achieving accuracy within 0.5\% of ReLU-based plaintext models.

  匹配依据：MPC: mpc (context)

  </details>

- **SoK: BitVM with Succinct On-Chain Cost**
  2025-07-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1253)
  Weikeng Chen

  <details><summary>摘要 / Abstract</summary>

  This is a systematization of knowledge (SoK) on BitVM with succinct on-chain cost. 1. from different cryptographic primitives: - Minicrypt privacy-free garbled circuits (PFGC) - homomorphic message authentication codes (HMAC), which implies succinct PFGC - attribute-based laconic function evaluation (AB-LFE), which implies reusable PFGC 2. using different malicious security compilers: - cut-and-choose (C&amp;C) - non-interactive zero-knowledge proofs (NIZK) - fraud proofs on Bitcoin 3. with different proof systems: - publicly verifiable SNARK - designated-verifiable SNARK (DV-SNARK) 4. in different protocol directions: - standard BitVM (operator = garbler, challengers = evaluators) - reverse BitVM (operator = evaluator, challengers = garblers) 5. given different operator liveness setup: - existential honesty - honest majority

  匹配依据：MPC: garbled circuits

  </details>

- **Cascade: Token-Sharded Private LLM Inference**
  2025-07-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.05228)
  Rahul Thomas, Louai Zahran, Erica Choi, Akilesh Potti, Micah Goldblum, Arka Pal

  <details><summary>摘要 / Abstract</summary>

  As LLMs continue to increase in parameter size, the computational resources required to run them are available to fewer parties. Therefore, third-party inference services -- where LLMs are hosted by third parties with significant computational resources -- are becoming increasingly popular. However, third party inference raises critical concerns about user data privacy. To mitigate these risks, privacy researchers have developed provably secure schemes for third-party inference, such as Secure Multi-Party Computation (SMPC). However, SMPC protocols have significant computational and communication overhead, and do not scale to large models. In this work, we propose a new multi-party inference protocol, Cascade, that avoids these punitive costs by leveraging sharding in the sequence dimension to maintain privacy, trading off cryptographic privacy guarantees for increased performance and scalability. We demonstrate that Cascade is resistant to a generalization of a recent attack that is highly effective against other statistical privacy schemes, and that it is further resistant to learning-based attacks. As Cascade is orders of magnitude faster than existing schemes, our findings offer practical solutions for secure deployment of modern state-of-the-art LLMs.

  匹配依据：MPC: secure multi party computation

  </details>

- **On Round-Optimal Computational VSS**
  2025-07-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1246)
  Karim Baghery, Navid Ghaedi Bardeh, Shahram Khazaei, Mahdi Rahimi

  <details><summary>摘要 / Abstract</summary>

  In ASIACRYPT 2011, Backes, Kate, and Patra (BKP) introduced two computationally secure round-optimal (2-round) Verifiable Secret Sharing (VSS) schemes in the honest-majority setting, one based on non-homomorphic commitments and the other on homomorphic ones. Their scheme based on non-homomorphic commitments has $O(n^2)$ computational complexity and necessitates $O(n^2\lambda)$ public and private communication for the dealer, where $n$ denotes the number of parties and $\lambda$ is the security parameter. They showed that these costs are $n$ times higher compared to their round-optimal VSS scheme employing homomorphic commitments and posed a research question regarding the inevitability of this gap. In this paper, we fill this gap by introducing a new variant of the recently proposed unified framework $\mathbf{\Pi}$ by Baghery at PKC 2025, designed to enable the construction of more efficient round-optimal VSS schemes in the honest-majority setting. Compared to the original framework, our variant reduces the required rounds by one while maintaining compatibility with any commitments and achieving comparable efficiency. Leveraging this new general construction, we develop several round-optimal VSS schemes that surpass state-of-the-art alternatives. Particularly noteworthy is the new round-optimal VSS scheme based on non-homomorphic commitments, which improves the BKP scheme by a factor of $n$ across all efficiency metrics. Compared to their schemes based on homomorphic commitments, our schemes demonstrate significantly expedited verification and reconstruction. Implementation results further validate the practicality of these new VSS schemes. For example, for $(n, t)=(256, 127)$, where $t$ represents the threshold, compared to the hash-based BKP VSS scheme, our proposed scheme showcases speed-ups exceeding $120,000\times$ (and $50\times$) for the dealer (and parties, respectively), while also requiring $365\times$ (and $512\times$) less communication.

  匹配依据：MPC: secret sharing

  </details>

- **Quantum protocols for Rabin oblivious transfer**
  2025-07-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.04015)
  Erika Andersson, Akshay Bansal, James T. Peat, Jamie Sikora, Jiawei Wu

  <details><summary>摘要 / Abstract</summary>

  Rabin oblivious transfer is the cryptographic task where Alice wishes to receive a bit from Bob but it may get lost with probability 1/2. In this work, we provide protocol designs which yield quantum protocols with improved security. Moreover, we provide a constant lower bound on any quantum protocol for Rabin oblivious transfer. To quantify the security of this task with asymmetric cheating definitions, we introduce the notion of cheating advantage which may be of independent interest in the study of other asymmetric cryptographic primitives.

  匹配依据：MPC: oblivious transfer

  </details>

- **A Note on Single-Cut Full-Open Protocols**
  2025-07-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2507.03323)
  Kazumasa Shinagawa, Koji Nuida

  <details><summary>摘要 / Abstract</summary>

  Card-based cryptography is a research area that realizes cryptographic protocols such as secure computation by applying shuffles to sequences of cards that encode input values. A single-cut full-open protocol is one that obtains an output value by applying a random cut to an input sequence of cards, after which all cards are opened. In this paper, we propose three single-cut full-open protocols: two protocols for three-variable functions and one protocol for a four-variable function.

  匹配依据：MPC: secure computation

  </details>

- **Efficient Pseudorandom Correlation Generators over $\\mathbb{Z}/p^k\\mathbb{Z}$**
  2025-07-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1223)
  Zhe Li, Chaoping Xing, Yizhou Yao, Chen Yuan

  <details><summary>摘要 / Abstract</summary>

  Modern efficient secure multi-party computation (MPC) protocols typically follow an offline-online design, where offline protocols produce a sufficient amount of correlated randomness that would be consumed during the online phases. The past decades have witnessed maturing of efficient online protocols, for computing circuits over either arbitrary finite fields or rings $\mathbb{Z}_{p^k}$. In particular, protocols tailored for $\mathbb{Z}_{2^k}$ arithmetic have achieved better concrete efficiency in most real-life applications, as it naturally captures modern CPU architectures. On the other hand, a recent paradigm of {\em pseudorandom correlation generator} (PCG) initiated by Boyle et al. (CCS&#x27;18, Crypto&#x27;19) opens a door to efficient preprocessing with sublinear communication. Since then, PCGs have been extensively studied and developed to produce various types of correlations required from online protocols. Although Li et al. (EuroCrypt&#x27;25) recently put a significant step forward and propose efficient PCGs for arbitrary finite fields, the current state of PCGs for rings is not satisfying at all. Towards the great demand for efficiently generating correlations over rings, we investigate PCGs for general Galois rings, which simultaneously unify finite fields and integer rings modulo $p^k$. In summary, we establish the following results: (i) We generalize the state-of-the-art PCG constructions for oblivious linear evaluations (OLE) over Galois fields to {\em arbitrary Galois rings}, basing on Galois theory and the Hensel lift. Moreover, our PCGs for Galois rings are as efficient as PCGs for fields. Concretely, for $mN$ OLE correlations over $\mathbb{Z}_{2^k}$, we require $O(m\log{N})$ communication and $O(m^2N\log{N})$ computation, where $m$ is an arbitrary integer $\geq 2$. In comparison, to our best knowledge, previous approaches incur communication at least linear in $N$. (ii) We extend the above OLE construction to provide various types of correlations over any Galois ring. One of the fascinating applications is an efficient PCG for two-party SPD$\mathbb{Z}_{2^k}$ authenticated multiplication triples (Crypto&#x27;18). For $mN$ SPD$\mathbb{Z}_{2^k}$ triples, our approach requires only $O(m\log{N})$ communication and $O(m^2N\log{N})$ computation. Concrete evaluations show that our method significantly outperforms existing schemes based on homomorphic encryption. (iii) In addition, our PCGs for Galois rings also enable multi-party multiplication triple generation, yielding the first efficient MPC protocol for arithmetic circuits over $\mathbb{Z}_{2^k}$ with \emph{silent} and \emph{sublinear} preprocessing. Additional applications include circuit-dependent preprocessing and matrix multiplication triples, etc, which are of independent interest.

  匹配依据：MPC: secure multi party computation

  </details>

- **Revisiting Module Lattice-based Homomorphic Encryption and Application to Secure-MPC**
  2025-06-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1218)
  Anisha Mukherjee, Sujoy Sinha Roy

  <details><summary>摘要 / Abstract</summary>

  Homomorphic encryption (HE) schemes have gained significant popularity in modern privacy-preserving applications across various domains. While research on HE constructions based on learning with errors (LWE) and ring-LWE has received major attention from both cryptographers and software-hardware designers alike, their module-LWE-based counterpart has remained comparatively under-explored in the literature. A recent work provides a module-LWE-based instantiation (MLWE-HE) of the Cheon-Kim-Kim-Song (CKKS) scheme and showcases several of its advantages such as parameter flexibility and improved parallelism. However, a primary limitation of this construction is the quadratic growth in the size of the relinearization keys. Our contribution is two-pronged: first, we present a new relinearization key-generation technique that addresses the issue of quadratic key size expansion by reducing it to linear growth. Second, we extend the application of MLWE-HE in a multi-group homomorphic encryption (MGHE) framework, thereby generalizing the favorable properties of the single-keyed HE to a multi-keyed setting as well as investigating additional flexibility attributes of the MGHE framework.

  匹配依据：MPC: mpc (context)

  </details>

- **Asymptotically Optimal Secure Aggregation for Wireless Federated Learning with Multiple Servers**
  2025-06-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.23680)
  Zhenhao Huang, Kai Liang, Yuanming Shi, Songze Li, Youlong Wu

  <details><summary>摘要 / Abstract</summary>

  In this paper, we investigate the transmission latency of the secure aggregation problem in a \emph{wireless} federated learning system with multiple curious servers. We propose a privacy-preserving coded aggregation scheme where the servers can not infer any information about the distributed users&#x27; local gradients, nor the aggregation value. In our scheme, each user encodes its local gradient into $\sK$ confidential messages intended exclusively for different servers using a multi-secret sharing method, and each server forwards the summation of the received confidential messages, while the users sequentially employ artificial noise alignment techniques to facilitate secure transmission. Through these summations, the user can recover the aggregation of all local gradients. We prove the privacy guarantee in the information-theoretic sense and characterize the uplink and downlink communication latency measured by \emph{normalized delivery time} (NDT), both of which decrease monotonically with the number of servers $\sK$ while increasing over most of the range of the number of users $\sM$. Finally, we establish a lower bound on the NDT of the considered system and theoretically prove that the scheme achieves the optimal uplink and downlink NDT under the conditions $\sK \gg \sM \gg 0$ and $\sK \gg \sM$, respectively. For arbitrary $\sK$ and $\sM$, the proposed scheme achieves the optimal uplink NDT within a multiplicative gap of $4$.

  匹配依据：MPC: secret sharing

  </details>

- **RingSG: Optimal Secure Vertex-Centric Computation for Collaborative Graph Processing**
  2025-06-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1209)
  Zhenhua Zou, Zhuotao Liu, Jinyong Shan, Qi Li, Ke Xu, Mingwei Xu

  <details><summary>摘要 / Abstract</summary>

  Collaborative graph processing refers to the joint analysis of inter-connected graphs held by multiple graph owners. To honor data privacy and support various graph processing algorithms, existing approaches employ secure multi-party computation (MPC) protocols to express the vertex-centric abstraction. Yet, due to certain computation-intensive cryptography constructions, state-of-the-art (SOTA) approaches are asymptotically suboptimal, imposing significant overheads in terms of computation and communication. In this paper, we present RingSG, the first system to attain optimal communication/computation complexity within the MPC-based vertex-centric abstraction for collaborative graph processing. This optimal complexity is attributed to Ring-ScatterGather, a novel computation paradigm that can avoid exceedingly expensive cryptography operations (e.g., oblivious sort), and simultaneously ensure the overall workload can be optimally decomposed into parallelizable and mutually exclusive MPC tasks. Within Ring-ScatterGather, RingSG improves the concrete runtime efficiency by incorporating 3-party secure computation via share conversion, and optimizing the most cost-heavy part using a novel oblivious group aggregation protocol. Finally, unlike prior approaches, we instantiate RingSG into two end-to-end applications to effectively obtain application-specific results from the protocol outputs in a privacy-preserving manner. We developed a prototype of RingSG and extensively evaluated it across various graph collaboration settings, including different graph sizes, numbers of parties, and average vertex degrees. The results show RingSG reduces the system running time of SOTA approaches by up to 15.34× and per-party communication by up to 10.36×. Notably, RingSG excels in processing sparse global graphs collectively held by more parties, consistent with our theoretical cost analysis.

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **MPC in the Quantum Head (or: Superposition-Secure (Quantum) Zero-Knowledge)**
  2025-06-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.22961)
  Andrea Coladangelo, Ruta Jawale, Dakshita Khurana, Giulio Malavolta, Hendrik Waldner

  <details><summary>摘要 / Abstract</summary>

  The MPC-in-the-head technique (Ishai et al., STOC 2007) is a celebrated method to build zero-knowledge protocols with desirable theoretical properties and high practical efficiency. This technique has generated a large body of research and has influenced the design of real-world post-quantum cryptographic signatures. In this work, we present a generalization of the MPC-in-the-head paradigm to the quantum setting, where the MPC is running a quantum computation. As an application of our framework, we propose a new approach to build zero-knowledge protocols where security holds even against a verifier that can obtain a superposition of transcripts. This notion was pioneered by Damgard et al., who built a zero-knowledge protocol for NP (in the common reference string model) secure against superposition attacks, by relying on perfectly hiding and unconditionally binding dual-mode commitments. Unfortunately, no such commitments are known from standard cryptographic assumptions. In this work we revisit this problem, and present two new three-round protocols in the common reference string model: (i) A zero-knowledge argument for NP, whose security reduces to the standard learning with errors (LWE) problem. (ii) A zero-knowledge argument for QMA from the same assumption.

  匹配依据：MPC: mpc (context)

  </details>

- **BitBatSPIR: Efficient Batch Symmetric Private Information Retrieval from PSI**
  2025-06-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1201)
  Shuaishuai Li, Liqiang Peng, Weiran Liu, Cong Zhang, Zhen Gu, Dongdai Lin

  <details><summary>摘要 / Abstract</summary>

  Private Information Retrieval (PIR) allows a client to retrieve an entry from a database held by a server without leaking which entry is being requested. Symmetric PIR (SPIR) is a stronger variant of PIR with database privacy so that the client knows nothing about the database other than the retrieved entry. This work studies SPIR in the batch setting (BatchSPIR), where the client wants to retrieve multiple entries. In particular, we focus on the case of bit entries, which has important real-world applications. We set up the connection between bit-entry information retrieval and set operation, and propose a black-box construction of BatchSPIR from Private Set Intersection (PSI). By applying an efficient PSI protocol with asymmetric set sizes, we obtain our BatchSPIR protocol named $\mathsf{BitBatSPIR}$. We also introduce several optimizations for the underlying PSI. These optimizations improve the efficiency of our concrete BatchSPIR construction as well as the PSI protocol. We implement $\mathsf{BitBatSPIR}$ and compare the performance with the state-of-the-art PIR protocol in the batch setting. Our experimental results show that $\mathsf{BitBatSPIR}$ not only achieves a stronger security guarantee (symmetric privacy) but also has a better performance for large databases, especially in the Wide Area Network (WAN) setting.

  匹配依据：MPC: private set intersection

  </details>

- **PrivacyGo: Privacy-Preserving Ad Measurement with Multidimensional Intersection**
  2025-06-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1192)
  Jian Du, Haohao Qian, Shikun Zhang, Wen-jie Lu, Donghang Lu, Yongchuan Niu, Bo Jiang, Yongjun Zhao, Qiang Yan

  <details><summary>摘要 / Abstract</summary>

  In digital advertising, accurate measurement is essential for optimiz- ing ad performance, requiring collaboration between advertisers and publishers to compute aggregate statistics—such as total conver- sions—while preserving user privacy. Traditional secure two-party computation methods allow joint computation on single-identifier data without revealing raw inputs, but they fall short when mul- tidimensional matching is needed and leak the intersection size, exposing sensitive information to privacy attacks. This paper tackles the challenging and practical problem of multi- identifier private user profile matching for privacy-preserving ad measurement, a cornerstone of modern advertising analytics. We introduce a comprehensive cryptographic framework leveraging re- versed Oblivious Pseudorandom Functions (OPRF) and novel blind key rotation techniques to support secure matching across multiple identifiers. Our design prevents cross-identifier linkages and in- cludes a differentially private mechanism to obfuscate intersection sizes, mitigating risks such as membership inference attacks. We present a concrete construction of our protocol that achieves both strong privacy guarantees and high efficiency. It scales to large datasets, offering a practical and scalable solution for privacy- centric applications like secure ad conversion tracking. By combin- ing rigorous cryptographic principles with differential privacy, our work addresses a critical need in the advertising industry, setting a new standard for privacy-preserving ad measurement frameworks.

  匹配依据：MPC: secure two party computation

  </details>

- **Non-Homomorphic Key Blinding from Symmetric Primitives**
  2025-06-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1193)
  Thomas Bellebaum

  <details><summary>摘要 / Abstract</summary>

  Key Blinding Signature Schemes allow to derive so-called blinded keys from public keys, which can be used to verify signatures created with the secret key. At the same time, neither the blinded keys nor their signatures disclose from which public key they were derived, effectively implementing pseudonyms for one’s identity. In search of conservative schemes, we deviate from the homomorphism- based re-randomization approach in favor of a novel proof of knowledge- based approach. To authenticate a message, a signer proves that they know an original keypair and a valid way to commit to the corresponding verification key to derive a given blinded key. We provide a framework for such constructions and indicate how MPC-friendly block ciphers and one-way functions may be used for efficient instantiations. While the general framework’s security arguments are stated in the random oracle model, we show a natural instantiation approach whose security can be based on collision-resistance and pseudorandomness instead. The result is the first standard model construction of key blinding. Using our framework, we identify a shortcoming in the usual definition of unlinkability for key blinding signature schemes, which we rectify by considering an additional notion called targeted unlinkability.

  匹配依据：MPC: mpc (context)

  </details>

- **Secure Multi-Key Homomorphic Encryption with Application to Privacy-Preserving Federated Learning**
  2025-06-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.20101) · [Code](https://github.com/JiahuiWu2022/SMHE.git)
  Jiahui Wu, Tiecheng Sun, Fucai Luo, Haiyan Wang, Weizhe Zhang

  <details><summary>摘要 / Abstract</summary>

  Multi-Key Homomorphic Encryption (MKHE), proposed by Lopez-Alt et al. (STOC 2012), allows for performing arithmetic computations directly on ciphertexts encrypted under distinct keys. Subsequent works by Chen and Dai et al. (CCS 2019) and Kim and Song et al. (CCS 2023) extended this concept by proposing multi-key BFV/CKKS variants, referred to as the CDKS scheme. These variants incorporate asymptotically optimal techniques to facilitate secure computation across multiple data providers. In this paper, we identify a critical security vulnerability in the CDKS scheme when applied to multiparty secure computation tasks, such as privacy-preserving federated learning (PPFL). In particular, we show that CDKS may inadvertently leak plaintext information from one party to others. To mitigate this issue, we propose a new scheme, SMHE (Secure Multi-Key Homomorphic Encryption), which incorporates a novel masking mechanism into the multi-key BFV and CKKS frameworks to ensure that plaintexts remain confidential throughout the computation. We implement a PPFL application using SMHE and demonstrate that it provides significantly improved security with only a modest overhead in homomorphic evaluation. For instance, our PPFL model based on multi-key CKKS incurs less than a 2\times runtime and communication traffic increase compared to the CDKS-based PPFL model. The code is publicly available at https://github.com/JiahuiWu2022/SMHE.git.

  匹配依据：MPC: secure computation

  </details>

- **ReBoot: Encrypted Training of Deep Neural Networks with CKKS Bootstrapping**
  2025-06-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.19693)
  Alberto Pirillo, Luca Colombo

  <details><summary>摘要 / Abstract</summary>

  Growing concerns over data privacy underscore the need for deep learning methods capable of processing sensitive information without compromising confidentiality. Among privacy-enhancing technologies, Homomorphic Encryption (HE) stands out by providing post-quantum cryptographic security and end-to-end data protection, safeguarding data even during computation. While Deep Neural Networks (DNNs) have gained attention in HE settings, their use has largely been restricted to encrypted inference. Prior research on encrypted training has primarily focused on logistic regression or has relied on multi-party computation to enable model fine-tuning. This stems from the substantial computational overhead and algorithmic complexity involved in DNNs training under HE. In this paper, we present ReBoot, the first framework to enable fully encrypted and non-interactive training of DNNs. Built upon the CKKS scheme, ReBoot introduces a novel HE-compliant neural network architecture based on local error signals, specifically designed to minimize multiplicative depth and reduce noise accumulation. ReBoot employs a tailored packing strategy that leverages real-number arithmetic via SIMD operations, significantly lowering both computational and memory overhead. Furthermore, by integrating approximate bootstrapping, ReBoot learning algorithm supports effective training of arbitrarily deep multi-layer perceptrons, making it well-suited for machine learning as-a-service. ReBoot is evaluated on both image recognition and tabular benchmarks, achieving accuracy comparable to 32-bit floating-point plaintext training while enabling fully encrypted training. It improves test accuracy by up to +3.27% over encrypted logistic regression, and up to +6.83% over existing encrypted DNN frameworks, while reducing training latency by up to 8.83x. ReBoot is made available to the scientific community as a public repository.

  匹配依据：MPC: multi party computation

  </details>

- **Can One Safety Loop Guard Them All? Agentic Guard Rails for Federated Computing**
  2025-06-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.20000)
  Narasimha Raghavan Veeraragavan, Jan Franz Nygård

  <details><summary>摘要 / Abstract</summary>

  We propose Guardian-FC, a novel two-layer framework for privacy preserving federated computing that unifies safety enforcement across diverse privacy preserving mechanisms, including cryptographic back-ends like fully homomorphic encryption (FHE) and multiparty computation (MPC), as well as statistical techniques such as differential privacy (DP). Guardian-FC decouples guard-rails from privacy mechanisms by executing plug-ins (modular computation units), written in a backend-neutral, domain-specific language (DSL) designed specifically for federated computing workflows and interchangeable Execution Providers (EPs), which implement DSL operations for various privacy back-ends. An Agentic-AI control plane enforces a finite-state safety loop through signed telemetry and commands, ensuring consistent risk management and auditability. The manifest-centric design supports fail-fast job admission and seamless extensibility to new privacy back-ends. We present qualitative scenarios illustrating backend-agnostic safety and a formal model foundation for verification. Finally, we outline a research agenda inviting the community to advance adaptive guard-rail tuning, multi-backend composition, DSL specification development, implementation, and compiler extensibility alongside human-override usability.

  匹配依据：MPC: multiparty computation

  </details>

- **Federated Learning-Based Data Collaboration Method for Enhancing Edge Cloud AI System Security Using Large Language Models**
  2025-06-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.18087)
  Huaiying Luo, Cheng Ji

  <details><summary>摘要 / Abstract</summary>

  With the widespread application of edge computing and cloud systems in AI-driven applications, how to maintain efficient performance while ensuring data privacy has become an urgent security issue. This paper proposes a federated learning-based data collaboration method to improve the security of edge cloud AI systems, and use large-scale language models (LLMs) to enhance data privacy protection and system robustness. Based on the existing federated learning framework, this method introduces a secure multi-party computation protocol, which optimizes the data aggregation and encryption process between distributed nodes by using LLM to ensure data privacy and improve system efficiency. By combining advanced adversarial training techniques, the model enhances the resistance of edge cloud AI systems to security threats such as data leakage and model poisoning. Experimental results show that the proposed method is 15% better than the traditional federated learning method in terms of data protection and model robustness.

  匹配依据：MPC: secure multi party computation

  </details>

- **Simple VESS**
  2025-06-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1175)
  Victor Shoup

  <details><summary>摘要 / Abstract</summary>

  We present a scheme for verifiably encrypting a Shamir secret sharing to a committee of shareholders. Such a scheme can be used to easily implement distributed key generation (DKG) and resharing protocols used in threshold signing and decryption protocols. Our scheme is a minor variation on known techniques, and is not the most efficient in terms of communication and computational complexity. However, it is extremely simple and easy to implement. Moreover, for moderately sized shareholder committees of up to, say, 13 parties or so, and for applications where a DKG/resharing only needs to be performed occasionally, its performance should be acceptable in practice.

  匹配依据：MPC: secret sharing

  </details>

- **Secret Sharing in 5G-MEC: Applicability for joint Security and Dependability**
  2025-06-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.17371)
  Thilina Pathirana, Ruxandra F. Olimid

  <details><summary>摘要 / Abstract</summary>

  Multi-access Edge Computing (MEC), an enhancement of 5G, processes data closer to its generation point, reducing latency and network load. However, the distributed and edge-based nature of 5G-MEC presents privacy and security challenges, including data exposure risks. Ensuring efficient manipulation and security of sensitive data at the edge is crucial. To address these challenges, we investigate the usage of threshold secret sharing in 5G-MEC storage, an approach that enhances both security and dependability. A (k,n) threshold secret sharing scheme splits and stores sensitive data among n nodes, requiring at least k nodes for reconstruction. The solution ensures confidentiality by protecting data against fewer than k colluding nodes and enhances availability by tolerating up to n-k failing nodes. This approach mitigates threats such as unauthorized access and node failures, whether accidental or intentional. We further discuss a method for selecting the convenient MEHs to store the shares, considering the MEHs&#x27; trustworthiness level as a main criterion. Although we define our proposal in the context of secret-shared data storage, it can be seen as an independent, standalone selection process for 5G-MEC trustworthy node selection in other scenarios too.

  匹配依据：MPC: secret sharing

  </details>

- **Quorus: Efficient, Scalable Threshold ML-DSA Signatures from MPC**
  2025-06-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1163)
  Alexander Bienstock, Leo de Castro, Daniel Escudero, Antigoni Polychroniadou, Akira Takahashi

  <details><summary>摘要 / Abstract</summary>

  A threshold signature protocol divides a secret signing key among multiple parties, enabling any subset above a threshold to jointly create a signature. While post-quantum (PQ) threshold signatures are being studied, especially following NIST&#x27;s call for threshold schemes, most solutions focus on specially designed, threshold-friendly signature schemes. However, real-world applications like distributed certificate authorities and digital currencies require signatures verifiable under existing standardized procedures. With NIST&#x27;s standardization of PQ signatures and ongoing industry deployment, designing an efficient threshold scheme compatible with NIST-standardized verification remains a critical challenge. In this work, we present the first efficient and scalable solution for multi-party generation of the module-lattice digital signature algorithm (ML-DSA), one of NIST&#x27;s PQ signature standards. Our contributions are two-fold. First, we present a variant of the ML-DSA signing algorithm that is amenable to efficient multi-party computation (MPC) and prove that this variant achieves the same security as the original ML-DSA scheme. Second, we present several efficient &amp; scalable MPC protocols to instantiate the threshold signing functionality. Our protocols can produce threshold signatures with as little as 100 KB (per party) of online communication per rejection-sampling round. In addition, we instantiate our protocols in the honest-majority setting, which allows us to avoid any additional public key assumptions. Our signatures verify under the same ML-DSA implementation for all security levels, with signature and verification key sizes matching ML-DSA; previous lattice-based threshold schemes could not match both of these sizes. Our solution provides the first method for producing threshold post-quantum signatures compatible with NIST-standardized verification, scalable to any number of parties, without new assumptions.

  匹配依据：MPC: multi party computation

  </details>

- **$\\mathsf{DekartProof}$: Efficient Vector Range Proofs and Their Applications**
  2025-06-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1159)
  Dan Boneh, Trisha Datta, Rex Fernando, Kamilla Nazirkhanova, Alin Tomescu

  <details><summary>摘要 / Abstract</summary>

  Let $p$ be a prime and consider a committed vector $\vec{v} = (v_1, \ldots, v_m) \in \mathbb{F}_p^m$. We develop new techniques for succinctly proving in zero-knowledge that all the elements of $\vec{v}$ are in the range $\{0,1,\ldots,n\}$ for some $n&lt;p$. We refer to this as a batched zero-knowledge range proof, or a batched ZKRP. This problem comes up often in cryptography: it is needed in publicly verifiable secret sharing (PVSS), confidential transactions, and election protocols. Our approach makes use of a multilinear polynomial commitment scheme and the sum check protocol to efficiently provide a batch range proof for the entire vector. Along the way we introduce a new type of a Polynomial Interactive Oracle Proof (PIOP) we call a Homomorphic PIOP that can be compiled into a SNARK. We use an HPIOP to construct a new efficient zero-knowledge version of the sum check protocol. We compare our new techniques with existing range proofs and lookup arguments.

  匹配依据：MPC: secret sharing

  </details>

- **PDLRecover: Privacy-preserving Decentralized Model Recovery with Machine Unlearning**
  2025-06-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.15112)
  Xiangman Li, Xiaodong Wu, Jianbing Ni, Mohamed Mahmoud, Maazen Alsabaan

  <details><summary>摘要 / Abstract</summary>

  Decentralized learning is vulnerable to poison attacks, where malicious clients manipulate local updates to degrade global model performance. Existing defenses mainly detect and filter malicious models, aiming to prevent a limited number of attackers from corrupting the global model. However, restoring an already compromised global model remains a challenge. A direct approach is to remove malicious clients and retrain the model using only the benign clients. Yet, retraining is time-consuming, computationally expensive, and may compromise model consistency and privacy. We propose PDLRecover, a novel method to recover a poisoned global model efficiently by leveraging historical model information while preserving privacy. The main challenge lies in protecting shared historical models while enabling parameter estimation for model recovery. By exploiting the linearity of approximate Hessian matrix computation, we apply secret sharing to protect historical updates, ensuring local models are not leaked during transmission or reconstruction. PDLRecover introduces client-side preparation, periodic recovery updates, and a final exact update to ensure robustness and convergence of the recovered model. Periodic updates maintain accurate curvature information, and the final step ensures high-quality convergence. Experiments show that the recovered global model achieves performance comparable to a fully retrained model but with significantly reduced computation and time cost. Moreover, PDLRecover effectively prevents leakage of local model parameters, ensuring both accuracy and privacy in recovery.

  匹配依据：MPC: secret sharing

  </details>

- **ReDASH: Fast and efficient Scaling in Arithmetic Garbled Circuits for Secure Outsourced Inference**
  2025-06-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.14489)
  Felix Maurer, Jonas Sander, Thomas Eisenbarth

  <details><summary>摘要 / Abstract</summary>

  ReDash extends Dash&#x27;s arithmetic garbled circuits to provide a more flexible and efficient framework for secure outsourced inference. By introducing a novel garbled scaling gadget based on a generalized base extension for the residue number system, ReDash removes Dash&#x27;s limitation of scaling exclusively by powers of two. This enables arbitrary scaling factors drawn from the residue number system&#x27;s modular base, allowing for tailored quantization schemes and more efficient model evaluation. Through the new $\text{ScaleQuant}^+$ quantization mechanism, ReDash supports optimized modular bases that can significantly reduce the overhead of arithmetic operations during convolutional neural network inference. ReDash achieves up to a 33-fold speedup in overall inference time compared to Dash Despite these enhancements, ReDash preserves the robust security guarantees of arithmetic garbling. By delivering both performance gains and quantization flexibility, ReDash expands the practicality of garbled convolutional neural network inference.

  匹配依据：MPC: garbled circuits

  </details>

- **Cut Tracing with E-Graphs for Boolean FHE Circuit Synthesis**
  2025-06-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.12883)
  Julien de Castelnau, Mingfei Yu, Giovanni De Micheli

  <details><summary>摘要 / Abstract</summary>

  Fully Homomorphic Encryption (FHE) is a promising privacy-preserving technology enabling secure computation over encrypted data. A major limitation of current FHE schemes is their high runtime overhead. As a result, automatic optimization of circuits describing FHE computation has garnered significant attention in the logic synthesis community. Existing works primarily target the multiplicative depth (MD) and multiplicative complexity (MC) of FHE circuits, corresponding to the total number of multiplications and maximum number of multiplications in a path from primary input to output, respectively. In many FHE schemes, these metrics are the primary contributors to the homomorphic evaluation runtime of a circuit. However, oftentimes they are opposed: reducing either depth or complexity may result in an increase in the other. To our knowledge, existing works have yet to optimize FHE circuits for overall runtime, only considering one metric at a time and thus making significant tradeoffs. In this paper, we use e-graphs to augment existing flows that individually optimize MC and MD, in a technique called cut tracing. We show how cut tracing can effectively combine two state-of-the-art MC and MD reduction flows and balance their weaknesses to minimize runtime. Our preliminary results demonstrate that cut tracing yields up to a 40% improvement in homomorphic evaluation runtime when applied to these two flows.

  匹配依据：MPC: secure computation

  </details>

- **Reusable Designated Verifier NIZK from Lossy Trapdoor Functions**
  2025-06-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1125)
  Riddhi Ghosal, Ilan Komargodski, Brent Waters

  <details><summary>摘要 / Abstract</summary>

  Understanding the minimal assumptions necessary for constructing non-interactive zero-knowledge arguments (NIZKs) for NP and placing it within the hierarchy of cryptographic primitives has been a central goal in cryptography. Unfortunately, there are very few examples of ``generic&#x27;&#x27; constructions of NIZKs or any of its natural relaxations. In this work, we consider the relaxation of NIZKs to the designated-verifier model (DV-NIZK) and present a new framework for constructing (reusable) DV-NIZKs for NP generically from lossy trapdoor functions and PRFs computable by polynomial-size branching programs (a class that includes NC1). Previous ``generic&#x27;&#x27; constructions of DV-NIZK for NP from standard primitives relied either on (doubly-enhanced) trapdoor permutations or on a public-key encryption scheme plus a KDM-secure secret key encryption scheme. Notably, our DV-NIZK framework achieves statistical zero-knowledge. To our knowledge, this is the first DV-NIZK construction from any ``generic&quot; standard assumption with statistical zero-knowledge that does not already yield a NIZK. A key technical component of our construction is an efficient, unconditionally secure secret sharing scheme for non-monotone functions with randomness recovery for all polynomial-size branching programs. As an independent contribution we present an incomparable randomness recoverable (monotone) secret sharing for NC1 in a model with trusted setup that guarantees computational privacy assuming one-way functions. We believe that these primitives will be useful in related contexts in the future.

  匹配依据：MPC: secret sharing

  </details>

- **VCR: Fast Private Set Intersection with Improved VOLE and CRT-Batching**
  2025-06-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1114)
  Weizhan Jing, Xiaojun Chen, Xudong Chen, Ye Dong, Yaxi Yang, Qiang Liu

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) allows two participants to compute the intersection of their private sets without revealing any additional information beyond the intersection itself. It is known that oblivious linear evaluation (OLE) can be used to construct the online efficient PSI protocol (Kerschbaum \textit{et al.}, NDSS&#x27;23). However, oblivious transfer (OT) and fully homomorphic encryption (FHE)-based offline OLE generation are expensive, and the online computational complexity is super-linear and still a heavy burden for large-scale sets. In this paper, we propose VCR, an efficient PSI protocol from vector OLE (VOLE) with the offline-online paradigm. Concretely, we first propose the batched short VOLE protocol to reduce offline overhead for generating VOLE tuples. Experiments demonstrate that VCR outperforms prior art. Then, we design a batched private membership test protocol from pre-computed VOLE to accelerate the online computation. Compared to the previous work of Kerschbaum \textit{et al.} (NDSS&#x27;23), we reduce the total communication costs (resp. running time) by $341\times$ and $9.1\times$ (resp. $6.5\times$ and $2.5\times$) on average for OT- and FHE-based protocols.

  匹配依据：MPC: oblivious transfer, private set intersection

  </details>

- **SecONNds: Secure Outsourced Neural Network Inference on ImageNet**
  2025-06-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.11586) · [Code](https://github.com/shashankballa/SecONNds)
  Shashank Balla

  <details><summary>摘要 / Abstract</summary>

  The widespread adoption of outsourced neural network inference presents significant privacy challenges, as sensitive user data is processed on untrusted remote servers. Secure inference offers a privacy-preserving solution, but existing frameworks suffer from high computational overhead and communication costs, rendering them impractical for real-world deployment. We introduce SecONNds, a non-intrusive secure inference framework optimized for large ImageNet-scale Convolutional Neural Networks. SecONNds integrates a novel fully Boolean Goldreich-Micali-Wigderson (GMW) protocol for secure comparison -- addressing Yao&#x27;s millionaires&#x27; problem -- using preprocessed Beaver&#x27;s bit triples generated from Silent Random Oblivious Transfer. Our novel protocol achieves an online speedup of 17$\times$ in nonlinear operations compared to state-of-the-art solutions while reducing communication overhead. To further enhance performance, SecONNds employs Number Theoretic Transform (NTT) preprocessing and leverages GPU acceleration for homomorphic encryption operations, resulting in speedups of 1.6$\times$ on CPU and 2.2$\times$ on GPU for linear operations. We also present SecONNds-P, a bit-exact variant that ensures verifiable full-precision results in secure computation, matching the results of plaintext computations. Evaluated on a 37-bit quantized SqueezeNet model, SecONNds achieves an end-to-end inference time of 2.8 s on GPU and 3.6 s on CPU, with a total communication of just 420 MiB. SecONNds&#x27; efficiency and reduced computational load make it well-suited for deploying privacy-sensitive applications in resource-constrained environments. SecONNds is open source and can be accessed from: https://github.com/shashankballa/SecONNds.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **b4M: Holistic Benchmarking for MPC**
  2025-06-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1106)
  Karl W. Koch, Dragos Rotaru, Christian Rechberger

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation (MPC) is becoming more and more usable in practice. The practicality origins primarily from well-established general-purpose MPC frameworks, such as MP-SPDZ. However, to evaluate the practicality of an MPC program in the envisioned environments, still many benchmarks need to be done. We identified three challenges in the context of performance evaluations within the MPC domain: first, the cumbersome process to holistically benchmark MPC programs; second, the difficulty to find the best-possible MPC setting for a given task and envisioned environment; and third, to have consistent evaluations of the same task or problem area across projects and papers. In this work, we address the gap of tedious and complex benchmarking of MPC. Related works so far mostly provide a comparison for certain programs with different engines. To the best of our knowledge, for the first time the whole benchmarking pipeline is automated; provided by our open-sourced framework Holistic Benchmarking for MPC (b4M). b4M is easy to configure using TOML files, outputs ready-to-use graphs, and provides even the MPC engine itself as own benchmark dimension. Furthermore it takes three relatively easy steps to add further engines: first, integrate engine-specific commands into b4M’s runner class; second, output performance metrics in b4M’s format; third, provide a Docker container for the engine’s parties. To showcase b4M, we provide an exemplary evaluation for the computation of the dot product and logistic regression using a real-world dataset. With this work, we move towards fully-automated evaluations of MPC programs, protocols, and engines, which smoothens the setup process and viewing various trade-offs. Hence, b4M advances MPC development by improving the benchmarking usability aspect of it.

  匹配依据：MPC: secure multi party computation

  </details>

- **Quantum secret sharing in a triangular superconducting quantum network**
  2025-06-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.10878)
  Haoxiong Yan, Allen Zang, Joel Grebel, Xuntao Wu, Ming-Han Chou, Gustav Andersson, Christopher R. Conner, Yash J. Joshi, Shiheng Li, Jacob M. Miller, Rhys G. Povey, Hong Qiao, Eric Chitambar, Andrew N. Cleland

  <details><summary>摘要 / Abstract</summary>

  We present a three-node quantum communication testbed with a triangular topology, each side of the triangle formed by a 1.3-meter-long transmission line. We demonstrate state transfer and entanglement generation between any two nodes, generate genuine multipartite entangled GHZ states, and implement quantum secret sharing (QSS) of classical information. Our experiments show that the QSS protocol can effectively detect eavesdropping, ensuring the secure sharing of secrets. This device forms a testbed for robust and secure quantum networking, enabling testing of more advanced quantum communication protocols.

  匹配依据：MPC: secret sharing

  </details>

- **Laconic PSI on Authenticated Inputs and Applications**
  2025-06-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1108)
  James Bartusek, Sanjam Garg, Abhishek Jain, Guru-Vamsi Policharla

  <details><summary>摘要 / Abstract</summary>

  A common issue with using secure computation in practice is that its security does not place any restrictions on what an adversary can use as input in the protocol. In this work, we focus on the practically-motivated setting of (two-message, labeled) private set intersection (PSI), and advocate for a clean and versatile solution to this problem: PSI on authenticated inputs. Our central contributions are summarized as follows. - We formulate a novel definition of PSI on authenticated inputs that has the potential for use in several applications, from content moderation in end-to-end encrypted systems to watchlists in anonymous e-cash systems. - We design a concretely-efficient and laconic (i.e., the size of the receiver&#x27;s message is independent of its set size) protocol for PSI on authenticated inputs. - We build on our PSI protocol to obtain the first laconic set pre-constrained group signature scheme, improving on that of Bartusek et al. (Eurocrypt 23). We also explore various optimizations to our basic protocol, including reducing the receiver&#x27;s concrete run time, and a tradeoff between crs size and message size.

  匹配依据：MPC: private set intersection, secure computation

  </details>

- **Commitment Schemes for Multi-Party Computation**
  2025-06-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.10721)
  Ioan Ionescu, Ruxandra F. Olimid

  <details><summary>摘要 / Abstract</summary>

  The paper presents an analysis of Commitment Schemes (CSs) used in Multi-Party Computation (MPC) protocols. While the individual properties of CSs and the guarantees offered by MPC have been widely studied in isolation, their interrelation in concrete protocols and applications remains mostly underexplored. This paper presents the relation between the two, with an emphasis on (security) properties and their impact on the upper layer MPC. In particular, we investigate how different types of CSs contribute to various MPC constructions and their relation to real-life applications of MPC. The paper can also serve as a tutorial for understanding the cryptographic interplay between CS and MPC, making it accessible to both researchers and practitioners. Our findings emphasize the importance of carefully selecting CS to meet the adversarial and functional requirements of MPC, thereby aiming for more robust and privacy-preserving cryptographic applications

  匹配依据：MPC: multi party computation

  </details>

- **Private Aggregation for Byzantine-Resilient Heterogeneous Federated Learning**
  2025-06-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.09870)
  Maximilian Egger, Rawad Bitar

  <details><summary>摘要 / Abstract</summary>

  Ensuring resilience to Byzantine clients while maintaining the privacy of the clients&#x27; data is a fundamental challenge in federated learning (FL). When the clients&#x27; data is homogeneous, suitable countermeasures were studied from an information-theoretic perspective utilizing secure aggregation techniques while ensuring robust aggregation of the clients&#x27; gradients. However, the countermeasures used fail when the clients&#x27; data is heterogeneous. Suitable pre-processing techniques, such as nearest neighbor mixing, were recently shown to enhance the performance of those countermeasures in the heterogeneous setting. Nevertheless, those pre-processing techniques cannot be applied with the introduced privacy-preserving mechanisms. We propose a multi-stage method encompassing a careful co-design of verifiable secret sharing, secure aggregation, and a tailored symmetric private information retrieval scheme to achieve information-theoretic privacy guarantees and Byzantine resilience under data heterogeneity. We evaluate the effectiveness of our scheme on a variety of attacks and show how it outperforms the previously known techniques. Since the communication overhead of secure aggregation is non-negligible, we investigate the interplay with zero-order estimation methods that reduce the communication cost in state-of-the-art FL tasks and thereby make private aggregation scalable.

  匹配依据：MPC: secret sharing

  </details>

- **Understanding the Error Sensitivity of Privacy-Aware Computing**
  2025-06-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.07957)
  Matías Mazzanti, Esteban Mocskos, Augusto Vega, Pradip Bose

  <details><summary>摘要 / Abstract</summary>

  Homomorphic Encryption (HE) enables secure computation on encrypted data without decryption, allowing a great opportunity for privacy-preserving computation. In particular, domains such as healthcare, finance, and government, where data privacy and security are of utmost importance, can benefit from HE by enabling third-party computation and services on sensitive data. In other words, HE constitutes the &quot;Holy Grail&quot; of cryptography: data remains encrypted all the time, being protected while in use. HE&#x27;s security guarantees rely on noise added to data to make relatively simple problems computationally intractable. This error-centric intrinsic HE mechanism generates new challenges related to the fault tolerance and robustness of HE itself: hardware- and software-induced errors during HE operation can easily evade traditional error detection and correction mechanisms, resulting in silent data corruption (SDC). In this work, we motivate a thorough discussion regarding the sensitivity of HE applications to bit faults and provide a detailed error characterization study of CKKS (Cheon-Kim-Kim-Song). This is one of the most popular HE schemes due to its fixed-point arithmetic support for AI and machine learning applications. We also delve into the impact of the residue number system (RNS) and the number theoretic transform (NTT), two widely adopted HE optimization techniques, on CKKS&#x27; error sensitivity. To the best of our knowledge, this is the first work that looks into the robustness and error sensitivity of homomorphic encryption and, as such, it can pave the way for critical future work in this area.

  匹配依据：MPC: secure computation

  </details>

- **The error-correcting pair for several classes of NMDS linear codes**
  2025-06-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.07380)
  Dong He, Zhaohui Zhang, Qunying Liao

  <details><summary>摘要 / Abstract</summary>

  The error-correcting pair is a general algebraic decoding method for linear codes. The near maximal distance separable (NMDS) linear code is a subclass of linear codes and has applications in secret sharing scheme and communication systems due to the efficient performance, thus we focus on the error-correcting pair of NMDS linear codes. In 2023, He and Liao showed that for an NMDS linear code $\mathcal{C}$ with minimal distance $2\ell+1$ or $2\ell+2$, if $\mathcal{C}$ has an $\ell$-error-correcting pair $\left( \mathcal{A}, \mathcal{B} \right)$, then the parameters of $\mathcal{A}$ have 6 or 10 possibilities, respectively. In this manuscript, basing on Product Singleton Bound, we give several necessary conditions for that the NMDS linear code $\mathcal{C}$ with minimal distance $2\ell+1$ has an $\ell$-error-correcting pair $(\mathcal{A}, \mathcal{B})$, where the parameters of $\mathcal{A}$ is the 1st, 2nd, 4th or 5th case, then basing on twisted generalized Reed-Solomon codes, we give an example for that the parameters of $\mathcal{A}$ is the 1st case. Moreover, we also give several necessary conditions for that the NMDS linear code $\mathcal{C}$ with minimal distance $2\ell+2$ has an $\ell$-error-correcting pair $(\mathcal{A}, \mathcal{B})$, where the parameters of $\mathcal{A}$ is the 2nd, 4th, 7th or 8th case, then we give an example for that the parameters of $\mathcal{A}$ is the 1st or 2nd case, respectively.

  匹配依据：MPC: secret sharing

  </details>

- **Shorter VOLE-in-the-Head-based Signatures from Vector Semi-Commitment**
  2025-06-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1077)
  Seongkwang Kim, Byeonghak Lee, Mincheol Son

  <details><summary>摘要 / Abstract</summary>

  The VOLE-in-the-Head (VOLEitH) paradigm compiles VOLE-based zero-knowledge proofs into publicly verifiable post-quantum signature schemes. A central component of VOLEitH is a GGM-style tree used to realize a vector commitment, whose size dominates the signature. In this work, we adapt vector semi-commitment (VSC)---previously developed for MPC-in-the-Head (MPCitH) by Kim et al. (\emph{Eurocrypt 2025})---to the VOLEitH paradigm and prove its security. While prior MPCitH analyses relied on assumption-specific, fragmented security proofs, we give a \emph{unified} treatment that characterizes which abstract property the underlying tree must satisfy, and instantiate it under the random oracle, Davies--Meyer, counter (CTR), and pseudorandom generator (PRG) models. Building on this, we construct reduced VOLE-in-the-Head (rVOLEitH) and apply it to FAEST, one of the NIST additional post-quantum signature candidates, obtaining signature sizes comparable to those of FAEST v2.0, ranging from 94.9\% to 102.8\% of the corresponding FAEST v2.0 sizes, while attaining 27.7--124.2\% faster signing and 28.3--115.3\% faster verification for 128-bit parameters. Finally, we describe a forgery attack on a recently proposed VOLEitH variant of the subfield bilinear collision (SBC) signature scheme by Huth and Joux (\emph{Asiacrypt 2025}) which replaces leaf commitments with a single global commitment, demonstrating the necessity of the commitment structure retained by VSC.

  匹配依据：MPC: mpc (context)

  </details>

- **Secure Distributed Learning for CAVs: Defending Against Gradient Leakage with Leveled Homomorphic Encryption**
  2025-06-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.07894)
  Muhammad Ali Najjar, Ren-Yi Huang, Dumindu Samaraweera, Prashant Shekhar

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) enables collaborative model training across distributed clients without sharing raw data, making it a promising approach for privacy-preserving machine learning in domains like Connected and Autonomous Vehicles (CAVs). However, recent studies have shown that exchanged model gradients remain susceptible to inference attacks such as Deep Leakage from Gradients (DLG), which can reconstruct private training data. While existing defenses like Differential Privacy (DP) and Secure Multi-Party Computation (SMPC) offer protection, they often compromise model accuracy. To that end, Homomorphic Encryption (HE) offers a promising alternative by enabling lossless computation directly on encrypted data, thereby preserving both privacy and model utility. However, HE introduces significant computational and communication overhead, which can hinder its practical adoption. To address this, we systematically evaluate various leveled HE schemes to identify the most suitable for FL in resource-constrained environments due to its ability to support fixed-depth computations without requiring costly bootstrapping. Our contributions in this paper include a comprehensive evaluation of HE schemes for real-world FL applications, a selective encryption strategy that targets only the most sensitive gradients to minimize computational overhead, and the development of a full HE-based FL pipeline that effectively mitigates DLG attacks while preserving model accuracy. We open-source our implementation to encourage reproducibility and facilitate adoption in safety-critical domains.

  匹配依据：MPC: secure multi party computation

  </details>

- **FABLE: Batched Evaluation on Confidential Lookup Tables in 2PC**
  2025-06-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1081)
  Zhengyuan Su, Qi Pang, Simon Beyzerov, Wenting Zheng

  <details><summary>摘要 / Abstract</summary>

  Abstract Secure two-party computation (2PC) is a cryptographic technique that enables two mutually distrusting parties to jointly evaluate a function over their private inputs. We consider a 2PC primitive called confidential lookup table (LUT) evaluation, which is useful in privacy-preserving ML inference and data analytics. In this setting, a server holds a confidential LUT and evaluates it over an input secret-shared between a client and the server, producing a secret-shared output. Existing approaches for 2PC LUT evaluation suffer from high asymptotic complexity and practical inefficiency, with some designs lacking confidentiality guarantees for the LUT. Recognizing that many applications involving confidential LUT evaluation require processing multiple inputs with the same LUT, we propose FABLE, a system designed to efficiently evaluate a LUT on a large batch of queries simultaneously. Compared to the state-of-the-art confidential LUT evaluation methods, FABLE achieves up to 28.46-101.47$\times$ speedup in LAN environments and up to 50.10-392.93$\times$ speedup in WAN environments.

  匹配依据：MPC: secure two party computation

  </details>

- **Combining Oblivious Pseudorandom Functions**
  2025-06-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1084)
  Sebastian Faller, Marc Fischlin, Julius Hardt, Julia Hesse

  <details><summary>摘要 / Abstract</summary>

  An oblivious pseudorandom function (OPRF) is an interactive protocol between a client and server, where the client aims to evaluate a keyed pseudorandom function for a key held by the server, without revealing its input. OPRFs are a versatile tool for enhancing privacy, inciting extensive research and standardization efforts in this area. The round-efficient 2Hash-Diffie-Hellman OPRF is widely deployed, but unfortunately, it is prone to quantum attacks. The search for post-quantum alternatives started in 2019 and is currently more disputed, with several candidates on the table. Given the lack of test of time of post-quantum OPRFs and their underlying cryptographic assumptions, hybridization can help mitigate risks in this interim period. Most preferably, we want to combine existing classical deployments like 2HashDH with post-quantum candidates. However, analogous two-party settings like oblivious transfer, where both parties have security requirements, indicate that combining OPRFs might be trickier than it is for hashing or encryption. In this paper, we give combiners for OPRFs with minimal overhead over the combined schemes. We also formally prove that &quot;ideal&#x27;&#x27; combiners, i.e., ones that do not make additional assumptions on how an underlying OPRF may break, cannot exist. Our constructions avoid this theoretical result by assuming the underlying OPRFs to satisfy certain statistical guarantees. Crucially, these extra conditions are satisfied by both the 2Hash-Diffie-Hellman OPRF and the currently most efficient post-quantum candidates, rendering our results suitable for upgrading existing deployments with quantum-safe guarantees already today.

  匹配依据：MPC: oblivious transfer

  </details>

- **PICS: Private Intersection over Committed (and reusable) Sets**
  2025-06-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1071)
  Aarushi Goel, Peihan Miao, Phuoc Van Long Pham, Satvinder Singh

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection (PSI) enables two parties to compute the intersection of their private sets without revealing any additional information. While maliciously secure PSI protocols prevent many attacks, adversaries can still exploit them by using inconsistent inputs across multiple sessions. This limitation stems from the definition of malicious security in secure multiparty computation, but is particularly problematic in PSI because: (1) real-world applications---such as Apple’s PSI protocol for CSAM detection and private contact discovery in messaging apps---often require multiple PSI executions over consistent inputs, and (2) the PSI functionality makes it relatively easy for adversaries to infer additional information. We propose {\em Private Intersection over Committed Sets (PICS)}, a new framework that enforces input consistency across multiple sessions via committed sets. Building on the state-of-the-art maliciously secure PSI framework (i.e., VOLE-PSI [EUROCRYPT 2021]), we present an efficient instantiation of PICS using lightweight cryptographic tools. Our protocol achieves strong receiver-side input consistency (i.e., the receiver uses the exact committed set) and weak sender-side input consistency (i.e., the sender cannot inject new elements into the committed set but can potentially use a subset of the committed set). We implement our protocol to demonstrate concrete efficiency. Compared to VOLE-PSI, our communication overhead is a small constant between $1.57 - 2.04\times$ for set sizes between $2^{16}-2^{24}$, and the total end-to-end running time overhead is $1.22 - 1.98\times$ across various network settings. $\textbf{Note:}$ The previous version of this paper had a soundness issue in the way we checked the consistency of the sender’s input. This revised draft presents a much simpler and cleaner approach to ensuring input consistency for the sender.

  匹配依据：MPC: private set intersection, secure multiparty computation

  </details>

- **QualitEye: Public and Privacy-preserving Gaze Data Quality Verification**
  2025-06-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.05908)
  Mayar Elfares, Pascal Reisert, Ralf Küsters, Andreas Bulling

  <details><summary>摘要 / Abstract</summary>

  Gaze-based applications are increasingly advancing with the availability of large datasets but ensuring data quality presents a substantial challenge when collecting data at scale. It further requires different parties to collaborate, therefore, privacy concerns arise. We propose QualitEye--the first method for verifying image-based gaze data quality. QualitEye employs a new semantic representation of eye images that contains the information required for verification while excluding irrelevant information for better domain adaptation. QualitEye covers a public setting where parties can freely exchange data and a privacy-preserving setting where parties cannot reveal their raw data nor derive gaze features/labels of others with adapted private set intersection protocols. We evaluate QualitEye on the MPIIFaceGaze and GazeCapture datasets and achieve a high verification performance (with a small overhead in runtime for privacy-preserving versions). Hence, QualitEye paves the way for new gaze analysis methods at the intersection of machine learning, human-computer interaction, and cryptography.

  匹配依据：MPC: private set intersection

  </details>

- **MIZAR: Boosting Secure Three-Party Deep Learning with Co-Designed Sign-Bit Extraction and GPU Acceleration**
  2025-06-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1063)
  Ye Dong, Xudong Chen, Xiangfu Song, Yaxi Yang, Tianwei Zhang, Jin-Song Dong

  <details><summary>摘要 / Abstract</summary>

  Three-party secret sharing-based computation has emerged as a promising approach for secure deep learning, benefiting from its high throughput. However, it still faces persistent challenges in computing complex operations such as secure Sign-Bit Extraction, particularly in high-latency and low-bandwidth networks. A recent work, Aegis (Lu et al., Cryptology ePrint&#x27;2023), made significant strides by proposing a constant-round DGK-style Sign-Bit Extraction protocol with GPU acceleration on Piranha (Watson et. al., USENIX Security&#x27;2022). However, Aegis exhibits two critical limitations: it \romannumeral1) overlooks the use of \textit{bit-wise prefix-sum}, and \romannumeral2) inherits non-optimized modular arithmetic over prime fields and excessive memory overhead from the underlying GPU-based MPC framework. This results in suboptimal performance in terms of communication, computation, and GPU memory usage. Driven by the limitations of Aegis, we propose an optimized constant-round secure Sign-Bit Extraction protocol with communication and GPU-specific optimizations. Concretely, we construct a new masked randomized list by exploiting the upper bound of bit-wise prefix-sum to reduce online communication by up to $50\%$, and integrate fast modular-reduction and kernel fusion techniques to enhance GPU utilization in MPC protocols. Besides, we propose specific optimizations for secure piecewise polynomial approximations and Maxpool computation in neural network evaluations. Finally, we instantiate these protocols as a framework MIZAR and report their improved performance over state-of-the-art GPU-based solutions: \romannumeral1) For secure Sign-Bit Extraction, we achieve a speedup of $2$--$2.5\times$ and reduce communication by $2$--$3.5\times$. \romannumeral2) Furthermore, we improve the performance of secure evaluation of nonlinear functions and neural networks by $1.5$--$3.5\times$. \romannumeral3) Lastly, our framework achieves $10\%$--$50\%$ GPU memory savings.

  匹配依据：MPC: secret sharing, secure evaluation

  </details>

- **FedShield-LLM: A Secure and Scalable Federated Fine-Tuned Large Language Model**
  2025-06-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.05640)
  Md Jueal Mia, M. Hadi Amini

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) offers a decentralized framework for training and fine-tuning Large Language Models (LLMs) by leveraging computational resources across organizations while keeping sensitive data on local devices. It addresses privacy and security concerns while navigating challenges associated with the substantial computational demands of LLMs, which can be prohibitive for small and medium-sized organizations. FL supports the development of task-specific LLMs for cross-silo applications through fine-tuning but remains vulnerable to inference-related risks that threaten sensitive information. Prior studies have utilized Differential Privacy (DP) in LLM fine-tuning, which, despite being effective at preserving privacy, can degrade model performance. To overcome these challenges, we propose FedShield-LLM which integrates pruning with Fully Homomorphic Encryption (FHE) applied to Low-Rank Adaptation (LoRA) parameters. This combination enables secure computation over encrypted model updates and reduces the attack surface by deactivating less important LoRA parameters. Furthermore, optimized federated algorithms for cross-silo environments enhance scalability and efficiency. Parameter-efficient fine-tuning techniques like LoRA substantially reduce computational and communication overhead, making FL feasible for resource-constrained clients. Extensive experiments using Llama-2 models (7B and 13B) on four diverse datasets demonstrate that FedShield-LLM achieves superior collaborative performance and system efficiency compared to existing methods, supporting practical deployment across multiple domains.

  匹配依据：MPC: secure computation

  </details>

- **Efficient Mixed-Mode Oblivious RAMs**
  2025-06-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1057)
  Wenhao Zhang, Xiao Wang, Chenkai Weng

  <details><summary>摘要 / Abstract</summary>

  Oblivious RAMs (ORAMs) allow data outsourcing to servers so that the access pattern to the outsourced data is kept private. It is also a crucial building block to enable private RAM access within secure multi-party computation (MPC). In recent years, schemes that match the ORAM lower bound have been proposed in both the outsourcing setting and the RAM-model MPC setting, seemingly putting an epilogue in the theory of ORAM. In this paper, we initiate a study of mixed-mode ORAMs, where accesses to the ORAM are a mix of both public and private accesses. Although existing ORAMs can support public access by treating them as private ones, achieving better efficiency is highly non-trivial. - We present a mixed-mode ORAM algorithm, assuming the existence of private information retrieval (PIR). When the PIR scheme is communication-efficient, this ORAM achieves the best possible outcome: it has a bandwidth blowup of $O(\log N)$ for private accesses and $O(1)$ for public accesses. This construction can be easily extended for the MPC setting achieving $O(B\log N )$ circuit size for private accesses to $B$-sized blocks and $O(B)$ circuit size for public accesses to the same array. - We instantiate the above protocol in the three-party computation (3PC) setting with more concrete optimizations, yielding a protocol that performs almost as efficiently as state-of-the-art RAM-3PC protocols for private accesses while being $3\times$ more efficient for public accesses in the LAN setting.

  匹配依据：MPC: secure multi party computation, three party computation

  </details>

- **MULTISS: un protocole de stockage confidentiel {à} long terme sur plusieurs r{é}seaux QKD**
  2025-06-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.04800)
  Thomas Prévost, Olivier Alibart, Marc Kaplan, Anne Marin

  <details><summary>摘要 / Abstract</summary>

  This paper presents MULTISS, a new protocol for long-term storage distributed across multiple Quantum Key Distribution (QKD) networks. This protocol is an extension of LINCOS, a secure storage protocol that uses Shamir secret sharing for secret storage on a single QKD network. Our protocol uses hierarchical secret sharing to distribute a secret across multiple QKD networks while ensuring perfect security. Our protocol further allows for sharing updates without having to reconstruct the entire secret. We also prove that MULTISS is strictly more secure than LINCOS, which remains vulnerable when its QKD network is compromised.

  匹配依据：MPC: secret sharing

  </details>

- **Breaking the 1/λ-Rate Barrier for Arithmetic Garbling**
  2025-06-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1053)
  Geoffroy Couteau, Carmit Hazay, Aditya Hegde, Naman Kumar

  <details><summary>摘要 / Abstract</summary>

  Garbled circuits, introduced in the seminal work of Yao (FOCS, 1986), have received considerable attention in the boolean setting due to their efficiency and application to round-efficient secure computation. In contrast, arithmetic garbling schemes have received much less scrutiny. The main efficiency measure of garbling schemes is their rate, defined as the bit size of each gate&#x27;s output divided by the size of the (amortized) garbled gate. Despite recent progress, state-of-the-art garbling schemes for arithmetic circuits suffer from important limitations: all existing schemes are either restricted to $B$-bounded integer arithmetic circuits (a computational model where the arithmetic is performed over $\mathbb{Z}$ and correctness is only guaranteed if no intermediate computation exceeds the bound $B$) and achieve constant rate only for very large bounds $B = 2^{\Omega(\lambda^3)}$, or have a rate at most $O(1/\lambda)$ otherwise, where $\lambda$ denotes a security parameter. In this work, we improve this state of affairs in both settings. - As our main contribution, we introduce the first arithmetic garbling scheme over modular rings $\mathbb{Z}_B$ with rate $O(\log\lambda/\lambda)$, breaking for the first time the $1/\lambda$-rate barrier for modular arithmetic garbling. Our construction relies on the power-DDH assumption. - As a secondary contribution, we introduce a new arithmetic garbling scheme for $B$-bounded integer arithmetic that achieves a constant rate for bounds $B$ as low as $2^{O(\lambda)}$. Our construction relies on a new non-standard KDM-security assumption on Paillier encryption with small exponents.

  匹配依据：MPC: garbled circuits, garbling scheme, garbling schemes, secure computation

  </details>

- **Authenticated Private Set Intersection: A Merkle Tree-Based Approach for Enhancing Data Integrity**
  2025-06-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.04647)
  Zixian Gong, Zhiyong Zheng, Zhe Hu, Kun Tian, Yi Zhang, Zhedanov Oleksiy, Fengxia Liu

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection (PSI) enables secure computation of set intersections while preserving participant privacy, standard PSI existing protocols remain vulnerable to data integrity attacks allowing malicious participants to extract additional intersection information or mislead other parties. In this paper, we propose the definition of data integrity in PSI and construct two authenticated PSI schemes by integrating Merkle Trees with state-of-the-art two-party volePSI and multi-party mPSI protocols. The resulting two-party authenticated PSI achieves communication complexity $\mathcal{O}(n λ+n \log n)$, aligning with the best-known unauthenticated PSI schemes, while the multi-party construction is $\mathcal{O}(n κ+n \log n)$ which introduces additional overhead due to Merkle tree inclusion proofs. Due to the incorporation of integrity verification, our authenticated schemes incur higher costs compared to state-of-the-art unauthenticated schemes. We also provide efficient implementations of our protocols and discuss potential improvements, including alternative authentication blocks.

  匹配依据：MPC: private set intersection, secure computation

  </details>

- **Topological Mixed States: Phases of Matter from Axiomatic Approaches**
  2025-06-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.04221)
  Tai-Hsuan Yang, Bowen Shi, Jong Yeon Lee

  <details><summary>摘要 / Abstract</summary>

  For closed quantum systems, topological orders are understood through the equivalence classes of ground states of gapped local Hamiltonians. The generalization of this conceptual paradigm to open quantum systems, however, remains elusive, often relying on operational definitions without fundamental principles. Here, we fill this gap by proposing an approach based on three axioms: ($i$) local recoverability, ($ii$) absence of long-range correlations, and ($iii$) spatial uniformity. States that satisfy these axioms are fixed points; requiring the axioms only after coarse-graining promotes each fixed point to an equivalence class, i.e., a phase, presenting the first step towards the axiomatic classification of mixed-state phases of matter: mixed-state bootstrap program. From these axioms, a rich set of topological data naturally emerges; importantly, these data are robust under relaxation of axioms. For example, each topological mixed state supports locally indistinguishable classical and/or quantum logical memories with distinct responses to topological operations. These data label distinct mixed-state phases, allowing one to distinguish them. We further uncover a hierarchy of secret-sharing constraints: in non-Abelian phases, reliable recovery-even of information that looks purely classical-demands a specific coordination among spatial subregions, a requirement different across non-Abelian classes. This originates from non-Abelian fusion rules that can stay robust under decoherence. Finally, we performed large-scale numerical simulations to corroborate stability: weakly decohered fixed points respect the axioms once coarse-grained. These results lay the foundation for a systematic classification of topological states in open quantum systems.

  匹配依据：MPC: secret sharing

  </details>

- **Rubato: Provably Post-Quantum Secure and Batched Asynchronous Randomness Beacon**
  2025-06-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1041)
  Linghe Yang, Tonghong Chong, Jian Liu, Jingyi Cui, Guangquan Xu, Yude Bai, Lei Zhang, Tao Luo

  <details><summary>摘要 / Abstract</summary>

  Distributed randomness beacons are essential for distributed systems (e.g., blockchain and MPC), providing unbiased and unpredictable shared randomness. However, implementations in asynchronous networks often suffer from poor scalability, low throughput, and high resource consumption when deployed as independent protocols. The state-of-the-art HashRand (CCS&#x27;24) achieves high throughput and low computational intensity using only lightweight post-quantum cryptographic primitives for an independent asynchronous beacon. Building further on this, we propose Rubato, a low-overhead, high-throughput beacon protocol that leverages lightweight batched Asynchronous Complete Secret Sharing with Byzantine Atomic Broadcast-based state machine replication (via our tailored RubatoSMR). Rubato reduces communication complexity by an $O(c \log n)$ factor compared to HashRand and resolves the circular dependency between beacon and BAB-SMR in asynchronous settings. Experiments on AWS demonstrate that Rubato achieves ideal overall performance in scalability, resource usage, and throughput; for instance, at $n=121$ nodes, it produces an average of 174 beacons per minute, with RubatoSMR further optimizing memory and bandwidth consumption.

  匹配依据：MPC: secret sharing

  </details>

- **Constant-Round Asynchronous MPC with Optimal Resilience and Linear Communication**
  2025-06-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1032)
  Junru Li, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  In this work, we consider secure multiparty computation (MPC) in the asynchronous network setting. MPC allows $n$ parties to compute a public function on their private inputs against an adversary corrupting at most $t$ of them. We consider both communication complexity and round complexity of asynchronous MPC (AMPC) with the optimal resilience $n=3t+1$. Without fully homomorphic encryptions, the best-known result in this setting is achieved by Coretti, Garay, Hirt, and Zikas (ASIACRYPT 2016), which requires $O(|C|n^3\kappa)$ bits of communication assuming one-way functions, where $\kappa$ is the security parameter. On the other hand, the best-known non-constant-round AMPC by Goyal, Liu, and Song (CRYPTO 2024) can achieve $O(|C|n)$ communication even in the information-theoretic setting. In this work, we give the first construction of a constant-round AMPC with $O(|C|n\kappa)$ bits of communication that achieves malicious security with abort assuming random oracles. We provide new techniques for adapting the MPC-in-the-head framework in the asynchronous network to compute a constant-size garbled circuit.

  匹配依据：MPC: garbled circuit, secure multiparty computation

  </details>

- **Committed Vector Oblivious Linear Evaluation and Its Applications**
  2025-06-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1037)
  Yunqing Sun, Hanlin Liu, Kang Yang, Yu Yu, Xiao Wang, Chenkai Weng

  <details><summary>摘要 / Abstract</summary>

  We introduce the notion of committed vector oblivious linear evaluation (C-VOLE), which allows a party holding a pre-committed vector to generate VOLE correlations with multiple parties on the committed value. It is a unifying tool that can be found useful in zero-knowledge proofs (ZKPs) of committed values, actively secure multi-party computation, private set intersection (PSI), etc. To achieve the best efficiency, we design a tailored commitment scheme and matching C-VOLE protocols, both based on the learning parity with noise assumption. In particular, exploiting the structures of the carefully designed LPN-based commitment minimizes the cost of ensuring consistency between the committed vector and VOLE correlation. As a result, we achieve a 28$\times$ improvement over the protocol proposed in prior work (Usenix 2021) that uses ZKP to prove the correct opening of the commitment. We also apply C-VOLE to design a PSI protocol that allows one server to run PSI repeatedly with multiple clients while ensuring that the same set is used across all executions. Compared with the state-of-the-art PSI (CCS 2024) with similar security requirements, our protocol reduces the communication overhead by a factor of 35$\times$.

  匹配依据：MPC: private set intersection, secure multi party computation

  </details>

- **Secure Noise Sampling for Differentially Private Collaborative Learning**
  2025-06-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1025)
  Olive Franzese, Congyu Fang, Radhika Garg, Somesh Jha, Nicolas Papernot, Xiao Wang, Adam Dziedzic

  <details><summary>摘要 / Abstract</summary>

  Differentially private stochastic gradient descent (DP-SGD) trains machine learning (ML) models with formal privacy guarantees for the training set by adding random noise to gradient updates. In collaborative learning (CL), where multiple parties jointly train a model, noise addition occurs either (i) before or (ii) during secure gradient aggregation. The first option is deployed in distributed DP methods, which require greater amounts of total noise to achieve security, resulting in degraded model utility. The second approach preserves model utility but requires a secure multiparty computation (MPC) protocol. Existing methods for MPC noise generation require tens to hundreds of seconds of runtime per noise sample because of the number of parties involved. This makes them impractical for collaborative learning, which often requires thousands or more samples of noise in each training step. We present a novel protocol for MPC noise sampling tailored to the collaborative learning setting. It works by constructing an approximation of the distribution of interest which can be efficiently sampled by a series of table lookups. Our method achieves significant runtime improvements and requires much less communication compared to previous work, especially at higher numbers of parties. It is also highly flexible – while previous MPC sampling methods tend to be optimized for specific distributions, we prove that our method can generically sample noise from statistically close approximations of arbitrary discrete distributions. This makes it compatible with a wide variety of DP mechanisms. Our experiments demonstrate the efficiency and utility of our method applied to a discrete Gaussian mechanism for differentially private collaborative learning. For 16 parties, we achieve a runtime of 0.06 seconds and 11.59 MB total communication per sample, a 230× runtime improvement and 3× less communication compared to the prior state-of-the-art for sampling from discrete Gaussian distribution in MPC.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Malicious Security in Collaborative zk-SNARKs: More than Meets the Eye**
  2025-06-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1026)
  Sanjam Garg, Aarushi Goel, Abhishek Jain, Bhaskar Roberts, Sruthi Sekar

  <details><summary>摘要 / Abstract</summary>

  Collaborative zk-SNARKs (Ozdemir and Boneh, USENIX’22) are a multiparty variant of zk-SNARKs where multiple, mutually distrustful provers, each holding a private input, jointly compute a zk-SNARK using their combined inputs. A sequence of works has proposed efficient constructions of collaborative zk-SNARKs using a common template that involves designing secure multiparty computation (MPC) protocols to emulate a zk-SNARK prover without making non-black-box use of cryptography. To achieve security against malicious adversaries, these works adopt compilers from the MPC literature that transform semi-honest MPC into malicious-secure MPC. In this work, we revisit this design template. • Pitfalls: We demonstrate two pitfalls in the template, which can lead to a loss of input privacy. We first show that it is possible to compute collaborative proofs on invalid witnesses, which in turn can leak the inputs of honest provers. Next, we show that using state-of-the-art malicious security compilers as-is for proof computation is insecure, in general. Finally, we discuss mitigation strategies. • Malicious Security Essentially for Free: As our main technical result, we show that in the honest-majority setting, one can forego malicious security checks performed by state-of-the-art malicious security compilers during collaborative proof generation of several widely used zk-SNARKs. In other words, we can avoid the overheads of malicious security compilers, enabling faster proof generation. To the best of our knowledge, this is the first example of non-trivial computations where semi-honest MPC protocols achieve malicious security. The observations underlying our positive results are general and may have applications beyond collaborative zkSNARKs.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Burn Your Vote: Decentralized and Publicly Verifiable Anonymous Voting at Scale**
  2025-06-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1022)
  Shahriar Ebrahimi, Haniyeh Habibi, Parisa Hassanizadeh, Pardis Toolabi, Vincenzo Botta, Stefan Dziembowski

  <details><summary>摘要 / Abstract</summary>

  Secure and trustworthy electronic voting requires more than correctness and censorship resistance, it must also ensure voter privacy, vote confidentiality, and protection against coercion. Prior work attempts to address these challenges using heavyweight cryptographic primitives such as homomorphic encryption, time-lock puzzles, or multi-party computation. These approaches often involve complex computations, depend on trusted parties, and typically do not scale well. We propose a lightweight, fully on-chain anonymous voting protocol based on a novel application of the proof-of-burn mechanism in the context of voting. Voters anonymously commit to their votes by burning tokens to pseudorandom addresses and later submit zero-knowledge proofs attesting to their valid participation. Our design achieves vote integrity, coercion resistance, and unlinkability without relying on ballot encryption, trusted parties, or centralized tallying. The tallying process is public and operates on plaintext votes that are authenticated yet unlinkable to voters. This enables support of flexible voting models, including token-weighted and quadratic voting, with minimal on-chain overhead. We formally analyze the protocol&#x27;s security guarantees and demonstrate support for a broad range of voting models. We implement the protocol as an open-source library fully compatible with the Ethereum Virtual Machine and evaluate it on commodity hardware (a consumer-grade laptop). All phases of the voting process are executed on the Sepolia testnet. Experimental results confirm the protocol&#x27;s scalability and improved on-chain efficiency, achieving over 20% reduction in gas consumption compared to the state of the art.

  匹配依据：MPC: multi party computation

  </details>

- **Silentium: Implementation of a Pseudorandom Correlation Generator for Beaver Triples**
  2025-06-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1013)
  Vincent Rieder

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation is a privacy-enhancing technology that allows several parties to securely compute on distributed private data. In the line of the well established SPDZ protocol, the by far most expensive task is the generation of Beaver triples in the so called offline phase. Silentium is our implementation of an actively secure offline phase in the form of a Pseudorandom Correlation Generator for Beaver triples (Bt-PCG, Boyle et al. CRYPTO 2020), which, as any PCG, is designed to have low communication. Compared to previous offline phases, their Bt-PCG reduces the communication costs by three orders of magnitude. However, so far efficiency was only estimated. With Silentium, we demonstrate that their Bt-PCG can achieve even better running times than state-of-the-art offline phase implementations in the MP-SPDZ library. To actually achieve such a performance, Silentium comprises a systematic parallelization strategy and implementation-friendly decomposition scenarios of the Bt-PCG into structured modules. Looking forward for large-scale applications on the cloud, Silentium is designed to be versatile to support hardware acceleration in future.

  匹配依据：MPC: secure multi party computation

  </details>

- **IDCloak: A Practical Secure Multi-party Dataset Join Framework for Vertical Privacy-preserving Machine Learning**
  2025-06-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.01072)
  Shuyu Chen, Guopeng Lin, Haoyu Niu, Lushan Song, Chengxun Hong, Weili Han

  <details><summary>摘要 / Abstract</summary>

  Vertical privacy-preserving machine learning (vPPML) enables multiple parties to train models on their vertically distributed datasets while keeping datasets private. In vPPML, it is critical to perform the secure dataset join, which aligns features corresponding to intersection IDs across datasets and forms a secret-shared and joint training dataset. However, existing methods for this step could be impractical due to: (1) they are insecure when they expose intersection IDs; or (2) they rely on a strong trust assumption requiring a non-colluding auxiliary server; or (3) they are limited to the two-party setting. This paper proposes IDCloak, the first practical secure multi-party dataset join framework for vPPML that keeps IDs private without a non-colluding auxiliary server. IDCloak consists of two protocols: (1) a circuit-based multi-party private set intersection protocol (cmPSI), which obtains secret-shared flags indicating intersection IDs via an optimized communication structure combining OKVS and OPRF; (2) a secure multi-party feature alignment protocol, which obtains the secret-shared and joint dataset using secret-shared flags, via our proposed efficient secure shuffle protocol. Experiments show that: (1) compared to the state-of-the-art secure two-party dataset join framework (iPrivjoin), IDCloak demonstrates higher efficiency in the two-party setting and comparable performance when the party number increases; (2) compared to the state-of-the-art cmPSI protocol under honest majority, our proposed cmPSI protocol provides a stronger security guarantee (dishonest majority) while improving efficiency by up to $7.78\times$ in time and $8.73\times$ in communication sizes; (3) our proposed secure shuffle protocol outperforms the state-of-the-art shuffle protocol by up to $138.34\times$ in time and $132.13\times$ in communication sizes.

  匹配依据：MPC: private set intersection

  </details>

- **Robust and Verifiable MPC with Applications to Linear Machine Learning Inference**
  2025-05-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.00518) · [IACR ePrint](https://eprint.iacr.org/2025/786)
  Tzu-Shen Wang, Jimmy Dani, Juan Garay, Soamar Homsi, Nitesh Saxena

  <details><summary>摘要 / Abstract</summary>

  In this work, we present an efficient secure multi-party computation MPC protocol that provides strong security guarantees in settings with dishonest majority of participants who may behave arbitrarily. Unlike the popular MPC implementation known as SPDZ [Crypto &#x27;12], which only ensures security with abort, our protocol achieves both complete identifiability and robustness. With complete identifiability, honest parties can detect and unanimously agree on the identity of any malicious party. Robustness allows the protocol to continue with the computation without requiring a restart, even when malicious behavior is detected. Additionally, our approach addresses the performance limitations observed in the protocol by Cunningham et al. [ICITS &#x27;17], which, while achieving complete identifiability, is hindered by the costly exponentiation operations required by the choice of commitment scheme. Our protocol is based on the approach by Rivinius et al. [S&amp;P &#x27;22], utilizing lattice-based commitment for better efficiency. We achieved robustness with the help of a semi-honest trusted third party. We benchmark our robust protocol, showing the efficient recovery from parties&#x27; malicious behavior. Finally, we benchmark our protocol on a ML-as-a-service scenario, wherein clients off-load the desired computation to the servers, and verify the computation result. We benchmark on linear ML inference, running on various datasets. While our efficiency is slightly lower compared to SPDZ&#x27;s, we offer stronger security properties that provide distinct advantages.

  匹配依据：MPC: secure multi party computation

  </details>

- **Reviving a Grover based Quantum Secret Sharing Scheme**
  2025-05-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/1008)
  Debajyoti Bera, Santanu Majhi

  <details><summary>摘要 / Abstract</summary>

  Secret-sharing schemes allow a dealer to split a secret into multiple “shares” and distribute them individually among many parties while mandating certain constraints on its reconstruction. Such protocols are usually executed over a secure communication channel since an eavesdropper, after intercepting all the shares, is expected to be able to reconstruct the secret. Leveraging the unique properties of quantum channels, several quantum protocols have been designed for secret sharing. However, almost all of them detect the presence of an eavesdropper by statistical analysis of the outcome of multiple rounds, or simply require a secure channel of communication. We mathematically analyse the correctness and security properties of a quantum-search based secret-sharing framework proposed by Hsu (2003) (and attacked by Hao et al. (2010)) that was proposed as an alternative that works over public channels and does not require multiple rounds.We show how to improve the original protocol to be more resistant towards eavesdropping and other attacks; however, we also prove that complete security against an eavesdropper is not possible in this framework. Our tight characterization will be helpful towards the construction of more quantum secret sharing schemes based on the same framework.

  匹配依据：MPC: secret sharing

  </details>

- **Communication Efficient Multiparty Private Set Intersection from Multi-Point Sequential OPRF**
  2025-05-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2506.00566)
  Xinyu Feng, Yukun Wang, Cong Li, Wu Xin, Ming Yao, Dian Zhang, Wanwan Wang, Hao He

  <details><summary>摘要 / Abstract</summary>

  Multiparty private set intersection (MPSI) allows multiple participants to compute the intersection of their locally owned data sets without revealing them. MPSI protocols can be categorized based on the network topology of nodes, with the star, mesh, and ring topologies being the primary types, respectively. Given that star and mesh topologies dominate current implementations, most existing MPSI protocols are based on these two topologies. However, star-topology MPSI protocols suffer from high leader node load, while mesh topology protocols suffer from high communication complexity and overhead. In this paper, we first propose a multi-point sequential oblivious pseudorandom function (MP-SOPRF) in a multi-party setting. Based on MP-SOPRF, we then develop an MPSI protocol with a ring topology, addressing the challenges of communication and computational overhead in existing protocols. We prove that our MPSI protocol is semi-honest secure under the Hamming correlation robustness assumption. Our experiments demonstrate that our MPSI protocol outperforms state-of-the-art protocols, achieving a reduction of 74.8% in communication and a 6% to 287% improvement in computational efficiency.

  匹配依据：MPC: private set intersection

  </details>

- **Verifiable Weighted Secret Sharing**
  2025-05-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.24289)
  Kareem Shehata, Han Fangqi, Sri AravindaKrishnan Thyagarajan

  <details><summary>摘要 / Abstract</summary>

  Traditionally, threshold secret sharing (TSS) schemes assume all parties have equal weight, yet emerging systems like blockchains reveal disparities in party trustworthiness, such as stake or reputation. Weighted Secret Sharing (WSS) addresses this by assigning varying weights to parties, ensuring security even if adversaries control parties with total weight at most a threshold $t$. Current WSS schemes assume honest dealers, resulting in security from only honest-but-curious behaviour but not protection from malicious adversaries for downstream applications. \emph{Verifiable} secret sharing (VSS) is a well-known technique to address this, but existing VSS schemes are either tailored to TSS, or require additional trust assumptions. We propose the first efficient verifiable WSS scheme that tolerates malicious dealers and is compatible with the latest CRT-based WSS~\cite{crypto_w_weights}. Our solution uses Bulletproofs for efficient verification and introduces new privacy-preserving techniques for proving relations between committed values, which may be of independent interest. Evaluation on Ethereum show up to a $100\times$ improvement in communication complexity compared to the current design and $20\times$ improvement compared to unweighted VSS schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Synopsis: Secure and private trend inference from encrypted semantic embeddings**
  2025-05-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.23880)
  Madelyne Xiao, Palak Jain, Micha Gorelick, Sarah Scheffler

  <details><summary>摘要 / Abstract</summary>

  WhatsApp and many other commonly used communication platforms guarantee end-to-end encryption (E2EE), which requires that service providers lack the cryptographic keys to read communications on their own platforms. WhatsApp&#x27;s privacy-preserving design makes it difficult to study important phenomena like the spread of misinformation or political messaging, as users have a clear expectation and desire for privacy and little incentive to forfeit that privacy in the process of handing over raw data to researchers, journalists, or other parties. We introduce Synopsis, a secure architecture for analyzing messaging trends in consensually-donated E2EE messages using message embeddings. Since the goal of this system is investigative journalism workflows, Synopsis must facilitate both exploratory and targeted analyses -- a challenge for systems using differential privacy (DP), and, for different reasons, a challenge for private computation approaches based on cryptography. To meet these challenges, we combine techniques from the local and central DP models and wrap the system in malicious-secure multi-party computation to ensure the DP query architecture is the only way to access messages, preventing any party from directly viewing stored message embeddings. Evaluations on a dataset of Hindi-language WhatsApp messages (34,024 messages represented as 500-dimensional embeddings) demonstrate the efficiency and accuracy of our approach. Queries on this data run in about 30 seconds, and the accuracy of the fine-grained interface exceeds 94% on benchmark tasks.

  匹配依据：MPC: secure multi party computation

  </details>

- **Lower Bounds on the Bottleneck Complexity of Secure Multiparty Computation**
  2025-05-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/990)
  Reo Eriguchi, Keitaro Hiwatashi

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) is a cryptographic primitive which enables multiple parties to jointly compute a function without revealing any extra information on their private inputs. Bottleneck complexity is an efficiency measure that captures the load-balancing aspect of MPC protocols, defined as the maximum amount of communication required by any party. In this work, we study the problem of establishing lower bounds on the bottleneck complexity of MPC protocols. While the previously known techniques for lower bounding total communication complexity can also be applied to bottleneck complexity, they do not provide nontrivial bounds in the correlated randomness model, which is commonly assumed by existing protocols achieving low bottleneck complexity, or they are applied only to functions of limited practical interest. We propose several novel techniques for lower bounding the bottleneck complexity of MPC protocols. Our methods derive nontrivial lower bounds even in the correlated randomness model and apply to practically relevant functions including the sum function and threshold functions. Furthermore, our lower bounds demonstrate the optimality of some existing MPC protocols in terms of bottleneck complexity or the amount of correlated randomness.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Improved Private Simultaneous Messages Protocols for Symmetric Functions with Universal Reconstruction**
  2025-05-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/992)
  Koji Nuida

  <details><summary>摘要 / Abstract</summary>

  Private Simultaneous Messages (PSM) is a kind of secure multiparty computation with minimal interaction pattern and minimal security requirement. A PSM protocol is said to be with universal reconstruction for a given function family if the algorithm of the referee (the output party) is independent of a function to be computed and the referee cannot infer the function from a protocol execution. In a recent work by Eriguchi and Shinagawa (EUROCRYPT 2025), the authors proposed a compiler to obtain a PSM protocol for symmetric functions from PSM protocols with universal reconstruction for symmetric functions with smaller domains. The authors also constructed the latter PSM protocols with universal reconstruction, by which the former PSM protocol achieves communication complexity better than the previously known protocols. In this paper, we construct the latter PSM protocols with universal reconstruction for symmetric functions more efficiently; the communication complexity is exponentially (in the input range) smaller than the protocols by Eriguchi and Shinagawa. As a consequence, we also obtain a PSM protocol (and also an ad-hoc PSM protocol and a robust PSM protocol) for symmetric functions that is more efficient than their protocol. Technically, a main ingredient of their protocols is a linear and injective encoding of histograms for the input elements, and our improvement is realized by finding a more efficient encoding of the histograms.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Distance-Aware OT with Application to Fuzzy PSI**
  2025-05-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/996)
  Lucas Piske, Jaspal Singh, Ni Trieu, Vladimir Kolesnikov, Vassilis Zikas

  <details><summary>摘要 / Abstract</summary>

  A two-party fuzzy private set intersection (PSI) protocol between Alice and Bob with input sets $A$ and $B$ allows Alice to learn nothing more than the points of Bob that are ``$\delta$-close&#x27;&#x27; to its points in some metric space $\texttt{dist}$. More formally, Alice learns only the set $\{ b\ |~\texttt{dist}{(a,b)} \leq \delta , a \in A,b\in B\}$ for a predefined threshold $\delta$ and distance metric $\texttt{dist}$, while Bob learns nothing about Alice&#x27;s set. Fuzzy PSI is a valuable privacy tool in scenarios where private set intersection needs to be computed over imprecise or measurement-based data, such as GPS coordinates or healthcare data. Previous approaches to fuzzy PSI rely on asymmetric cryptographic primitives, generic two-party computation (2PC) techniques like garbled circuits, or function secret sharing methods, all of which are computationally intensive and lead to poor concrete efficiency. This work introduces a new modular framework for fuzzy PSI, {primarily built on efficient symmetric key primitives}. Our framework reduces the design of efficient fuzzy PSI to a novel variant of oblivious transfer (OT), which we term distance-aware random OT (da-ROT). This variant enables the sender to obtain two random strings $(r_0, r_1)$, while the receiver obtains one of these values $r_b$, depending on whether the receiver’s input keyword $a$ and the sender’s input keyword $b$ are close in some metric space i.e., $\texttt{dist}{(a,b)} \leq \delta$. The da-ROT can be viewed as a natural extension of traditional OT, where the condition (choice bit) is known to the receiver. We propose efficient constructions for da-ROT based on standard OT techniques tailored for small domains, supporting distance metrics such as the Chebyshev norm, the Euclidean norm, and the Manhattan norm. By integrating these da-ROT constructions, our fuzzy PSI framework achieves up to a $14\times$ reduction in communication cost and up to a $54\times$ reduction in computation cost compared to previous state-of-the-art protocols, across input set sizes ranging from $2^8$ to $2^{16}$. Additionally, we extend our framework to compute fuzzy PSI cardinality and fuzzy join from traditional PSI-related functionalities. All proposed protocols are secure in the semi-honest model.

  匹配依据：MPC: garbled circuits, oblivious transfer, private set intersection, secret sharing, two party computation

  </details>

- **Security of Linear Secret Sharing Schemes with Noisy Side-Channel Leakage**
  2025-05-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/987)
  Utkarsh Gupta, Hessam Mahdavifar

  <details><summary>摘要 / Abstract</summary>

  Secret sharing is a foundational cryptographic primitive for sharing secret keys in distributed systems. In a classical threshold setting, it involves a dealer who has a secret, a set of $n$ users to whom shares of the secret are sent, and a threshold $t$ which is the minimum number of shares required to recover the secret. These schemes offer an all-or-nothing security approach where less than $t$ shares reveal no information about the secret. But these guarantees are threatened by side-channel attacks which can leak partial information from each share. Initiated by Benhamouda et. al. (CRYPTO&#x27;18), the security of such schemes has been studied for precise and worst-case bounded leakage models. However, in practice, side-channel attacks are inherently noisy. In this work, we propose a noisy leakage model for secret sharing, where each share is independently leaked to an adversary corrupted by additive noise in the underlying field $\mathbb{F}_q$. Under this model, we study the security of linear secret sharing schemes, and show bounds on the mutual information (MI) and statistical distance (SD) security metrics. We do this by using the MacWilliams&#x27; identity from the theory of error-correcting codes. For a given secret, it enables us to bound the the statistical deviation of the leaked shares from uniform as $\delta^t$, where $\delta$ is the Fourier bias of the added noise. Existing analyses for the security of linear $(n,t)$-threshold schemes only bound the SD metric, and show resilience for schemes with $t \ge 0.668n$. In this work, we show that these constraints are artifacts of the bounded leakage model. In particular, we show that $(n,t)$-threshold schemes over $\mathbb{F}_q$ with $t \ge \tau (n+1)$ leak $\mathcal{O}(q^{-2t(\gamma+1-1/\tau)})$ bits about the secret, given the bias of added noise satisfies $\delta \le q^{-\gamma}$. To the best of our knowledge, this is the first attempt towards understanding the side-channel security of linear secret sharing schemes for the MI metric.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-preserving Prompt Personalization in Federated Learning for Multimodal Large Language Models**
  2025-05-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.22447)
  Sizai Hou, Songze Li, Baturalp Buyukates

  <details><summary>摘要 / Abstract</summary>

  Prompt learning is a crucial technique for adapting pre-trained multimodal language models (MLLMs) to user tasks. Federated prompt personalization (FPP) is further developed to address data heterogeneity and local overfitting, however, it exposes personalized prompts - valuable intellectual assets - to privacy risks like prompt stealing or membership inference attacks. Widely-adopted techniques like differential privacy add noise to prompts, whereas degrading personalization performance. We propose SecFPP, a secure FPP protocol harmonizing generalization, personalization, and privacy guarantees. SecFPP employs hierarchical prompt adaptation with domain-level and class-level components to handle multi-granular data imbalance. For privacy, it uses a novel secret-sharing-based adaptive clustering algorithm for domain-level adaptation while keeping class-level components private. While theoretically and empirically secure, SecFPP achieves state-of-the-art accuracy under severe heterogeneity in data distribution. Extensive experiments show it significantly outperforms both non-private and privacy-preserving baselines, offering a superior privacy-performance trade-off.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Inconsistency Measurement**
  2025-05-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.23825)
  Carl Corea, Timotheus Kampik, Nico Potyka

  <details><summary>摘要 / Abstract</summary>

  We investigate a new form of (privacy-preserving) inconsistency measurement for multi-party communication. Intuitively, for two knowledge bases K_A, K_B (of two agents A, B), our results allow to quantitatively assess the degree of inconsistency for K_A U K_B without having to reveal the actual contents of the knowledge bases. Using secure multi-party computation (SMPC) and cryptographic protocols, we develop two concrete methods for this use-case and show that they satisfy important properties of SMPC protocols -- notably, input privacy, i.e., jointly computing the inconsistency degree without revealing the inputs.

  匹配依据：MPC: secure multi party computation

  </details>

- **Multi-Party Distributed Point Functions with Polylogarithmic Key Size from Invariants of Matrices**
  2025-05-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/978)
  Toomas Krips, Pille Pullonen-Raudvere

  <details><summary>摘要 / Abstract</summary>

  Distributed point functions (DPFs), introduced in 2014, are a widely used primitive in secure computation for a wide variety of applications. However, until recently, constructions for DPFs with polylogarithmic keys were known only for the two-party setting, multi-party schemes have key sizes exponential in the number of parties or the domain size. We generalize the efficient tree-based two-party DPF approach and get a scheme for a polylogarithmic-size DPF for an any number of parties. We use a technique where we have the invariant for off-path leaves such that secret-shared vector is mapped to secret submodules by public matrices. We show, using a technique by Shamir, that these vectors are hard to compute over $\mathbb{Z}_{pq}$ if factoring is hard. Our scheme is a secure DPF under two new assumptions related to Generic Group Model and the Linear Code Equivalence. The output of our scheme is in the exponent in some group where Diffie-Hellman type problems are hard which limits the usability of the scheme. Still, it is the first multi-party DPF generalizing the tree-based two-party DPF approach. Our scheme is the first where the key is polylogarithmic in the domain size and independent of the number of parties and the key generation and evaluation can be computed efficiently independently of the number of parties.

  匹配依据：MPC: secure computation

  </details>

- **Dynamic Security: A Realistic Approach to Adaptive Security With Applications to Strong FaF Security**
  2025-05-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/988)
  Bar Alon, Naty Peter

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation allows multiple parties to jointly compute a function while maintaining security even in the presence of malicious adversaries. There are two types of adversaries in the literature: static adversaries, which choose the parties to corrupt before the protocol begins; and adaptive adversaries, which can corrupt parties during the execution of the protocol based on the messages exchanged by the parties. While adaptive security provides a more robust security guarantee, it may require too much in certain scenarios. Indeed, the adversary must allocate some of its resources to corrupt the parties; however, certain parties might be more susceptible to corruption, for instance, if they have not updated their operating system to the latest version. To address this, we introduce a new security notion called \emph{dynamic security}. Here, adversaries may corrupt new parties \emph{during and after} the protocol&#x27;s execution, but \emph{cannot choose} targets based on the messages. A protocol is said to be $(t,h)$-dynamically secure if it is possible to simulate any adversary that can corrupt up to $t$ parties during the execution and $h$ thereafter. Dynamic security provides meaningful security for many real-world scenarios. Moreover, it circumvents known lower bounds on the communication complexity of adaptive security, allowing for more efficient protocols such as committee-based ones, which would be insecure against adaptive adversaries. We further explore dynamic security and establish the following results. 1. We show a surprising connection between dynamic security and the seemingly unrelated notion of security with friends and foes (FaF security), introduced by Alon et al. (CRYPTO 2020), which aims to protect honest parties not only from adversaries but also against other honest parties. The notion of $(t,h)$-\emph{strong FaF security} strengthens this by requiring the simulatability of the joint view of any $t$ malicious parties alongside any $h$ honest parties to be indistinguishable from their real-world view. We show that $(t,h)$-dynamic security and $(t,h)$-strong FaF security are equivalent. 2. We consider the feasibility of $(t,h)$-dynamic security and show that every $n$-party functionality can be computed with computational $(t,h)$-dynamic security (with guaranteed output delivery) if and only if $2t+h&lt;n$. By our previous result, this also solves an open problem left by Alon et al. on the feasibility of strong FaF security.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Algebraic Cryptanalysis of AO Primitives Based on Polynomial Decomposition Applications to Rain and Full AIM-IIIIV**
  2025-05-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/981)
  Hong-Sen Yang, Qun-Xiong Zheng, Jing Yang

  <details><summary>摘要 / Abstract</summary>

  The LowMC-based post-quantum signature scheme Picnic was selected as a third-round candidate for NIST PQC, attracting wide attention to the design of efficient and secure post-quantum signature schemes using Symmetric Techniques for Advanced Protocols (STAP). Symmetric primitives designed for advanced protocols such as secure multi-party computation (MPC), fully homomorphic encryption (FHE), and zero-knowledge (ZK) proof systems, with the goal of reducing the number of multiplication operations, are referred to as arithmetic-oriented (AO) primitives. These cryptographic primitives are typically constructed over large finite fields, which makes classical statistical analysis methods like differential and linear cryptanalysis inefficient. Due to their inherent algebraic properties, the mainstream security evaluation approaches are based on algebraic attacks. In this paper, we analyze the security of the MPC-friendly primitives \textsc{Rain} (CCS 2022) and AIM (CCS 2023) used in the post-quantum signature schemes Rainier and AIMer. Existing algebraic attacks on \textsc{Rain} and AIM were conducted over $\mathbb{F}_2$. We propose a novel algebraic attack over $\mathbb{F}_{2^n}$ that uses the polynomial decomposition to reduce degrees of equations. By further combining with the guess-and-determine technique, meet-in-the-middle modeling, and resultant, we are able to attack \textsc{Rain} and the full AIM. Specifically, we successfully attacked 2-round \textsc{Rain} with $2^{73.7}/2^{107.0}/2^{138.9}$ primitive calls, 3-round \textsc{Rain} with $2^{167.6}/2^{243.6}/2^{319.1}$ field operations, for the $128/192/256$-bit key. For the full AIM, we successfully attacked it with $2^{114.0}/2^{163.2}/2^{228.3}$ primitive calls for the $128/192/256$-bit key. The attack complexities mainly lie in solving univariate polynomial equations and computing resultants, and hence the complexity evaluations are accurate.

  匹配依据：MPC: secure multi party computation

  </details>

- **Learning with Alternating Moduli, Arora-Ge over Composite Moduli, and Weak PRFs**
  2025-05-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/968)
  Yilei Chen, Liheng Ji, Wenjie Li

  <details><summary>摘要 / Abstract</summary>

  In TCC 2018, Boneh, Ishai, Passelègue, Sahai, and Wu propose candidates of weak and strong PRFs by evaluating linear functions over coprime moduli alternatively. Such PRFs can be evaluated by low-depth circuits and are MPC-friendly. However, they have not been able to base the security of their PRFs on well-formed assumptions other than assuming that the PRF constructions themselves are secure. In this paper, we formalize a new assumption called Learning with Alternating Moduli (LAM). We show that over certain large moduli, the LAM assumption is as hard as the Learning with Errors (LWE) assumption. For LAM over constant moduli, we do not know how to base its hardness on the LWE assumption. Instead, we provide (i) polynomial-time attacks on LAM with constant prime-power moduli and certain constant non-prime-power moduli, and (ii) evidence of the sub-exponential hardness of LAM with other moduli by analyzing the effect of typical attacks. More specifically, we put forward two new attacks. The first attack is a recursive algorithm that solves LWE with certain constant composite moduli and error distributions. The algorithm extends the Arora-Ge algorithm for LWE from prime moduli to composite moduli, and it also solves LAM for certain parameters. The second attack is a polynomial-time attack that rules out the existence of weak PRFs in $\mathsf{NC}^0[p]$ for any prime $p$. Based on our studies, we propose candidate weak PRFs in $\mathsf{NC}^0[p_1,p_2]$ for some distinct primes $p_1,p_2$ based on LAM over constant moduli, or the Learning with Rounding (LWR) assumption over constant moduli. Compared to the weak PRF candidates by Boneh et al., our weak PRF candidates live in the same complexity class while having the advantage of being based on well-formed assumptions.

  匹配依据：MPC: mpc (context)

  </details>

- **An Efficient Framework for Collusion Resistant Multiparty FHE**
  2025-05-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/965)
  Robin Jadoul, Barry van Leeuwen, Oliver Zajonc

  <details><summary>摘要 / Abstract</summary>

  Multiparty fully homomorphic encryption (MPFHE) is a generalization of (multi-key) fully homomorphic encryption ((MK)FHE) that lives on the cusp between multiparty computation (MPC) and FHE, enabling a computation over encrypted data using multiple keys. However, contrary to MKFHE, it seeks to reduce the noise inflation based on the number of parties by allowing the parties to first compute shared data in MPC before executing the computation in FHE. However, many works use specific constructions, e.g. Chang-Li, Koirala et. al., and Ma et. al., reliant on the behaviour of a particular scheme and do not consider security against colluding servers and parties, e.g. Passelègue-Stehlé, Okada-Takagi, and Mouchet et. al. In this work we present a new framework that is secure against collusion between servers and parties and allows the use of a broad spectrum of MPC and FHE protocols, while eliminating the noise inflation based on the participating number of parties. We then show a case study of this using the FINAL scheme and show that we reduce the required key material by 60­–99.9% compared to the MKFHE FINAL scheme, FINALLY, and 65–70% compared to the Park-Rovira scheme in all cases, and by up to 71% compared to the AKÖ scheme when there are 4 or more parties. Moreover, we reduce the bootstrapping time for the AKÖ, Park-Rovira, and KMS schemes by 75–99.7%.

  匹配依据：MPC: multiparty computation

  </details>

- **Towards Better Integral Distinguishers over $\\mathbb{F}\_{p}$ Based on Exact Coefficients of Monomials**
  2025-05-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/955)
  Muzhou Li, Jiamin Cui, Longzheng Cui, Kai Hu, Chao Niu, Meiqin Wang

  <details><summary>摘要 / Abstract</summary>

  Symmetric primitives used in multi-party computation, fully homomorphic encryption, and zero-knowledge proofs are often defined over Finite Field $\mathbb{F}_{q}$ with $q=2^t$ or an odd prime $p$. Integral attack is one of the most effective methods against such primitives due to the common use of low-degree non-linear layers. This in turn highlights the importance of a deeper understanding of degree growth. For ciphers defined over $\mathbb{F}_{2^t}$, numerous works have explored the growth of the algebraic degree. However, these methods cannot be directly applied to $\mathbb{F}_{p}$. At CRYPTO 2020, Beyne et al. extended the integral cryptanalysis to $\mathbb{F}_{p}$ by comparing degree with $s(p-1)$ when using $p^s$ data. However, given that the precise degree evaluation remains fundamentally challenging and often computationally infeasible, one may lose better integral distinguishers. In this paper, we present the first automatic search model over $\mathbb{F}_{p}$ based on the exact coefficient $\mathcal{A}$ of the monomial $\prod_{w=1}^{s}x_w^{p-1}$ contained in the algebraic representation. This model is constructed following the Computation-Traceback-Determine framework, where $\mathcal{A}$ is represented by several sums of multinomial coefficients under specific conditions. The existence of integral properties is then transformed into a determination of whether these sums can consistently equal $0\bmod{p}$. This determination is facilitated by four newly developed propositions based on Lucas Theorem. To demonstrate the effectiveness of our framework, we apply it to all variants of GMiMC. As a result, we achieve the best integral distinguishers for GMiMC-erf/-crf using large primes when they are used as block ciphers. For GMiMC-nyb/-mrf using 32/64-bit primes, our integral distinguishers cover more rounds than all other attacks. Meanwhile, all distinguishers we identified are no worse than those trivial ones predicted only considering the maximal degree. This shows the necessity of considering exact coefficients when searching for integral distinguishers over $\mathbb{F}_p$. Our framework is further employed to assess the security of two HADES designs: HadesMiMC and Poseidon2$^\pi$. The results reveal that the full rounds at the beginning and end of HADES provide sufficient resistance against integral cryptanalysis.

  匹配依据：MPC: multi party computation

  </details>

- **Privacy-Preserving Peer-to-Peer Energy Trading via Hybrid Secure Computations**
  2025-05-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.20577)
  Junhong Liu, Qinfei Long, Rong-Peng Liu, Wenjie Liu, Xin Cui, Yunhe Hou

  <details><summary>摘要 / Abstract</summary>

  The massive integration of uncertain distributed renewable energy resources into power systems raises power imbalance concerns. Peer-to-peer (P2P) energy trading provides a promising way to balance the prosumers&#x27; volatile energy power generation and demands locally. Particularly, to protect the privacy of prosumers, distributed P2P energy trading is broadly advocated. However, severe privacy leakage issues can emerge in the realistic fully distributed P2P energy trading paradigm. Meanwhile, in this paradigm, two-party and multi-party computations coexist, challenging the naive privacy-preserving techniques. To tackle privacy leakage issues arising from the fully distributed P2P energy trading, this paper proposes a privacy-preserving approach via hybrid secure computations. A secure multi-party computation mechanism consisting of offline and online phases is developed to ensure the security of shared data by leveraging the tailored secret sharing method. In addition, the Paillier encryption method based on the Chinese Remainder Theorem is proposed for both the secure two-party computation and the offline phase of the multi-party computation. The random encryption coefficient is designed to enhance the security of the two-party computation and simultaneously guarantee the convergence of the distributed optimization. The feasible range for the encryption coefficient is derived with a strict mathematical proof. Numerical simulations demonstrate the exactness, effectiveness, and scalability of the proposed privacy-preserving approach.

  匹配依据：MPC: multi party computation, secret sharing, secure multi party computation, secure two party computation, two party computation

  </details>

- **Resolving the Efficiency-Utility Dilemma of Threshold Linearly Homomorphic Encryption via Message-Space Adapter**
  2025-05-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/948)
  Yijia Chang, Rongmao Chen, Chao Lin, Songze Li, Xinyi Huang

  <details><summary>摘要 / Abstract</summary>

  Threshold linearly homomorphic encryption (ThLHE) is a useful cryptographic tool for secure computation in multi-party settings, with applications in electronic voting, secure multiparty computation (MPC), and beyond. Although ThLHE offers significant advantages such as low communication overhead, its adoption in modern systems is hindered by a critical dilemma between efficiency and utility. Precisely, existing ThLHE schemes either suffer from high decryption complexity—typically $\mathcal{O}(N^2\log N)$ or worse for $N$ parties—or impose extra restrictions on the message space or participant set, limiting their practicality in large-scale and dynamic settings. In this work, we resolve this efficiency-utility dilemma for ThLHE by introducing a novel primitive termed message-space adapter (MeSA). By developing a lattice-based MeSA for exponential ElGamal (Exp-ElGamal), we mitigate the small-message restriction of Exp-ElGamal while preserving its efficient threshold decryption. This leads to the design of the first ThLHE scheme that achieves quasi-linear decryption complexity without restrictions on the message space or participant set. We implement a prototype of this new ThLHE scheme and validate the quasi-linear growth of its running time with respect to $N$. Beyond resolving this dilemma, we further extend the applications of our new ThLHE scheme. Specifically, we apply it to construct the first multi-party fully homomorphic encryption scheme with quasi-linear computation complexity and constant communication complexity, while supporting arbitrary threshold and dynamic participant set. This demonstrates the extra benefits of our ThLHE scheme with broader applicability.

  匹配依据：MPC: secure computation, secure multiparty computation

  </details>

- **Measurement-free reconstruction circuit of quantum secrets in quantum secret sharing**
  2025-05-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.18840)
  Shogo Chiwaki, Ryutaroh Matsumoto

  <details><summary>摘要 / Abstract</summary>

  For a quantum secret sharing scheme built from a general quantum stabilizer code, no measurement-free circuit has been known for reconstructing its quantum secrets, except particular classes, such as one proposed by Cleve, Gottesman and Lo. We propose a measurement-free reconstruction circuit of quantum secrets in quantum secret sharing based on stabilizer codes. Our reconstruction circuit has width $k+|J|$ and consists of $O(k|J|)$ one- or two-qudit unitary gates when $|J|$ participants reconstruct $k$-qudit quantum secrets.

  匹配依据：MPC: secret sharing

  </details>

- **Almost-Total Puzzles and Their Applications**
  2025-05-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/949)
  Xiao Liang, Omkant Pandey, Yuhao Tang, Takashi Yamakawa

  <details><summary>摘要 / Abstract</summary>

  Public-coin protocols are cryptographic protocols in which all messages sent by a specific party (typically the receiver or verifier) consist solely of random bits. These protocols have been extensively studied $\textit{in the classical setting}$ due to their advantageous properties in several scenarios, such as the parallel repetition of interactive arguments, and the design of secure multi-party computation with low round complexity, among others. Curiously, $\textit{post-quantum}$ constructions of public-coin protocols remain limited, particularly when optimization is sought in additional factors like round complexity or hardness assumptions. We introduce the concept of $\textit{almost-total puzzles}$, a novel cryptographic primitive characterized by two key properties: (i) hardness against any efficient adversary, and (ii) an &quot;almost-total&quot; guarantee of the existence of solutions, even when the puzzle generator is malicious. We demonstrate that this primitive can be derived from one-way functions in public-coin, requiring only two rounds. By leveraging this primitive, we obtain a family of new $\textit{public-coin}$ results in both the classical and post-quantum settings, based on the $\textit{minimal assumption} $ of (post-quantum) one-way functions, including: - five-round post-quantum extractable commitments and witness-indistinguishable arguments of knowledge, where the (knowledge) extractors achieve the $\textit{coherently expected quantum-polynomial-time}$ ($\mathsf{EQPT}_c$) simulation proposed by Lombardi, Ma, and Spooner [FOCS&#x27;22]; - five-round classical extractable commitments that $\textit{do not suffer from over extraction}$; - five-round classical delayed-input strong witness-indistinguishable arguments of knowledge, and delayed-input witness-hiding arguments of knowledge; - the five-round post-quantum analogue of the last item, but with the difference that (1) the input can be delayed until the third round, and (2) post-quantum arguments of knowledge are again defined w.r.t. $\mathsf{EQPT}_c$-simulation; - $O(\log^* \lambda)$-round post-quantum non-malleable commitments.

  匹配依据：MPC: secure multi party computation

  </details>

- **Succinct Witness Encryption for Batch Languages and Applications**
  2025-05-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/944)
  Lalita Devadas, Abhishek Jain, Brent Waters, David J. Wu

  <details><summary>摘要 / Abstract</summary>

  Witness encryption allows one to encrypt a message to an $\mathsf{NP}$ relation $\mathcal{R}$ and a statement $x$. The corresponding decryption key is any valid $\mathsf{NP}$ witness $w$. In a succinct witness encryption scheme, we require that the size of the ciphertext be sublinear in the size of the $\mathsf{NP}$ relation. Currently, all realizations of succinct witness encryption for $\mathsf{NP}$ rely on strong assumptions such as pseudorandom obfuscation, extractable witness encryption, or differing-inputs obfuscation. Notably, none of these notions are known from standard assumptions. In this work, we consider a relaxation of succinct witness encryption for $\mathsf{NP}$ to the setting of batch $\mathsf{NP}$. In this setting, one encrypts to an $\mathsf{NP}$ relation $\mathcal{R}$ together with $K$ statements $x_1, \ldots, x_K$. In the basic version, one can decrypt if they have a witness $w_1, \ldots, w_K$ for all $K$ statements. The succinctness requirement is that the size of the ciphertext should be sublinear in the number of instances $K$, but is allowed to grow with the size of the $\mathsf{NP}$ relation (i.e., the size of a single instance). More generally, we can also impose a (monotone) policy $P \colon \{0,1\}^K \to \{0,1\}$ over the $K$ instances. In this case, decryption is possible only if there exists $w_1, \ldots, w_K$ such that $P(\mathcal{R}(x_1, w_1), \ldots, \mathcal{R}(x_K, w_K)) = 1$. In this work, we initiate a systematic study of succinct witness encryption for batch languages. We start with two simple constructions that support CNF and DNF policies based on plain witness encryption in conjunction with a somewhere statistically sound batch argument for $\mathsf{NP}$ or a function-binding hash function. Then, using indistinguishability obfuscation, we show how to support policies that can be computed by read-once bounded-space Turing machines. The latter construction is in fact a unique witness map for monotone-policy batch $\mathsf{NP}$, and as such, also gives a SNARG for monotone-policy batch $\mathsf{NP}$ where the size of the common reference string is sublinear in the number of instances. Finally, we demonstrate some immediate applications of succinct witness encryption for batch languages. We construct new succinct computational secret sharing schemes for CNFs, DNFs, and weighted threshold policies. We also show how to build distributed monotone-policy encryption, a notion that generalizes recent trustless primitives like distributed broadcast encryption and threshold encryption with silent setup.

  匹配依据：MPC: secret sharing

  </details>

- **An Attack to Break Permutation-Based Private Third-Party Inference Schemes for LLMs**
  2025-05-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2505.18332)
  Rahul Thomas, Louai Zahran, Erica Choi, Akilesh Potti, Micah Goldblum, Arka Pal

  <details><summary>摘要 / Abstract</summary>

  Recent advances in Large Language Models (LLMs) have led to the widespread adoption of third-party inference services, raising critical privacy concerns. Existing methods of performing private third-party inference, such as Secure Multiparty Computation (SMPC), often rely on cryptographic methods. However, these methods are thousands of times slower than standard unencrypted inference, and fail to scale to large modern LLMs. Therefore, recent lines of work have explored the replacement of expensive encrypted nonlinear computations in SMPC with statistical obfuscation methods - in particular, revealing permuted hidden states to the third parties, with accompanying strong claims of the difficulty of reversal into the unpermuted states. In this work, we begin by introducing a novel reconstruction technique that can recover original prompts from hidden states with nearly perfect accuracy across multiple state-of-the-art LLMs. We then show that extensions of our attack are nearly perfectly effective in reversing permuted hidden states of LLMs, demonstrating the insecurity of three recently proposed privacy schemes. We further dissect the shortcomings of prior theoretical `proofs&#x27; of permuation security which allow our attack to succeed. Our findings highlight the importance of rigorous security analysis in privacy-preserving LLM inference.

  匹配依据：MPC: secure multiparty computation

  </details>

- **SEEC: Memory Safety Meets Efficiency in Secure Two-Party Computation**
  2025-05-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/930)
  Henri Dohmen, Robin Hundt, Nora Khayata, Thomas Schneider

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation (MPC) allows multiple parties to perform privacy-preserving computation on their secret data. MPC protocols based on secret sharing have high throughput which makes them well-suited for batch processing, where multiple instances are evaluated in parallel. So far, practical implementations of secret sharing-based MPC protocols mainly focus on runtime and communication efficiency, so the memory overhead of protocol implementations is often overlooked. Established techniques to reduce the memory overhead for constant-round garbled circuit protocols cannot be directly applied to secret sharing-based protocols because they would increase the round complexity. Additionally, state-of-the-art implementations of secret sharing-based MPC protocols are implemented in C/C++ and may exhibit memory unsafety and memory leaks, which could lead to undefined behavior. In this paper, we present SEEC: SEEC Executes Enormous Circuits, a framework for secret sharing-based MPC with a novel approach to address memory efficiency and safety without compromising on runtime and communication efficiency. We realize SEEC in Rust, a language known for memory-safety at close-to-native speed. To reduce the memory footprint, we develop an in-memory representation for sub-circuits. Thus, we never inline sub-circuit calls during circuit evaluation, a common issue that blows up memory usage in MPC implementations. We compare SEEC with the state-of-the-art secret sharing-based MPC frameworks ABY (NDSS&#x27;15), MP-SPDZ (CCS&#x27;20), and MOTION (TOPS&#x27;22) w.r.t. runtime, memory, and communication efficiency. Our results show that our reliable and memory-safe implementation has competitive or even better performance.

  匹配依据：MPC: garbled circuit, secret sharing, secure multi party computation, secure two party computation

  </details>

- **Rep3 Reloaded: On the Cost of Function-Dependent Preprocessing in Semi-Honest 3PC with Honest Majority**
  2025-05-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/919)
  Marcel Keller

  <details><summary>摘要 / Abstract</summary>

  Rep3 denotes the implementation of semi-honest three-party computation with an honest majority in MP-SPDZ (CCS&#x27;20). It uses replicated secret sharing with one message per multiplication and party as proposed by Araki et al. (CCS&#x27;16). This approach is rivaled by Astra (CCSW&#x27;19) and Trio (PETS&#x27;25), which use function-dependent preprocessing. The latter is more involved than, e.g., Beaver triples which can be used as a commodity. In this work, we present a full implementation of Astra and Trio in MP-SPDZ, and we evaluate the costs of the different approaches. We show the equivalence of the schemes, which implies that a protocol in any of the schemes can be translated to one in another with the same overall communication cost. We also present an improvement to two important building blocks for privacy-preserving computation, namely secure comparison and probabilistic truncation used in fixed-point arithmetic. To evaluate our implementation, we have benchmarked machine learning training and inference in all three schemes, improving on Keller and Sun (ICML&#x27;22) by over 30%. Our implementation also highlights the large storage requirements of function-dependent preprocessing as it runs the two phases separately. To the best of our knowledge, this is the first implementation to do so.

  匹配依据：MPC: secret sharing, three party computation

  </details>

- **Card-Based Protocol Counting Connected Components of Graphs**
  2025-05-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2025/924)
  Koji Nuida

  <details><summary>摘要 / Abstract</summary>

  Card-based cryptography is a research area for realizing cryptographic functionality, such as secure multiparty computation and zero-knowledge proofs, by using a deck of physical cards and/or other non-electrical tools. Motivated by zero-knowledge proofs for solutions in pencil puzzles, there is a direction of recent studies on card-based protocols to verify connectivity of a set of cells or edges on lattice-shaped boards. In this paper, we generalize the problem to counting connected components of a subset of the vertex set on any graph, and propose a card-based protocol for the problem.

  匹配依据：MPC: secure multiparty computation

  </details>
