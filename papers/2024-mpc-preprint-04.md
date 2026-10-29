# 2024 · MPC · 仅预印本来源 · 第 4/5 页

[总目录](../PAPERS.md) · [上一页](2024-mpc-preprint-03.md) · [下一页](2024-mpc-preprint-05.md)

- **Rondo: Scalable and Reconfiguration-Friendly Randomness Beacon**
  2024-04-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/641)
  Xuanji Meng, Xiao Sui, Zhaoxin Yang, Kang Rong, Wenbo Xu, Shenglong Chen, Ying Yan, Sisi Duan

  <details><summary>摘要 / Abstract</summary>

  We present Rondo, a scalable and reconfiguration-friendly distributed randomness beacon (DRB) protocol in the partially synchronous model. Rondo is the first DRB protocol that is built from batched asynchronous verifiable secret sharing (bAVSS) and meanwhile avoids the high $O(n^3)$ message cost, where $n$ is the number of nodes. Our key contribution lies in the introduction of a new variant of bAVSS called batched asynchronous verifiable secret sharing with partial output (bAVSS-PO). bAVSS-PO is a weaker primitive than bAVSS but allows us to build a secure and more scalable DRB protocol. We propose a bAVSS-PO protocol Breeze. Breeze achieves the optimal $O(n)$ messages for the sharing stage and allows Rondo to offer better scalability than prior DRB protocols. Additionally, to support the reconfiguration, we introduce Rondo-BFT, a dynamic and partially synchronous Byzantine fault-tolerant protocol inspired by Dyno (S\&amp;P 2022). Unlike Dyno, Rondo-BFT provides a communication pattern that generates randomness beacon output periodically, making it well-suited for DRB applications. We implement our protocols and evaluate the performance on Amazon EC2 using up to 91 instances. Our evaluation results show that Rondo achieves higher throughput than existing works and meanwhile offers better scalability, where the performance does not degrade as significantly as $n$ grows.

  匹配依据：MPC: secret sharing

  </details>

- **SECO: Secure Inference With Model Splitting Across Multi-Server Hierarchy**
  2024-04-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.16232)
  Shuangyi Chen, Ashish Khisti

  <details><summary>摘要 / Abstract</summary>

  In the context of prediction-as-a-service, concerns about the privacy of the data and the model have been brought up and tackled via secure inference protocols. These protocols are built up by using single or multiple cryptographic tools designed under a variety of different security assumptions. In this paper, we introduce SECO, a secure inference protocol that enables a user holding an input data vector and multiple server nodes deployed with a split neural network model to collaboratively compute the prediction, without compromising either party&#x27;s data privacy. We extend prior work on secure inference that requires the entire neural network model to be located on a single server node, to a multi-server hierarchy, where the user communicates to a gateway server node, which in turn communicates to remote server nodes. The inference task is split across the server nodes and must be performed over an encrypted copy of the data vector. We adopt multiparty homomorphic encryption and multiparty garbled circuit schemes, making the system secure against dishonest majority of semi-honest servers as well as protecting the partial model structure from the user. We evaluate SECO on multiple models, achieving the reduction of computation and communication cost for the user, making the protocol applicable to user&#x27;s devices with limited resources.

  匹配依据：MPC: garbled circuit

  </details>

- **Privacy-Preserving Billing for Local Energy Markets**
  2024-04-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.15886)
  Eman Alqahtani, Mustafa A. Mustafa

  <details><summary>摘要 / Abstract</summary>

  We propose a privacy-preserving billing protocol for local energy markets (PBP-LEM) that takes into account market participants&#x27; energy volume deviations from their bids. PBP-LEM enables a group of market entities to jointly compute participants&#x27; bills in a decentralized and privacy-preserving manner without sacrificing correctness. It also mitigates risks on individuals&#x27; privacy arising from any potential internal collusion. We first propose an efficient and privacy-preserving individual billing scheme, achieving information-theoretic security, which serves as a building block. PBP-LEM utilizes this scheme, along with other techniques such as multiparty computation, inner product functional encryption and Pedersen commitments to ensure data confidentiality and accuracy. Additionally, we present three approaches, resulting in different levels of privacy protection and performance. We prove that the protocol meets its security and privacy requirements and is feasible for deployment in real LEMs: bills can be computed in less than five minutes for 4,000 users using the most computationally intensive approach, and in just 0.18 seconds using the least intensive one.

  匹配依据：MPC: multiparty computation

  </details>

- **MUSEN: Aggregatable Key-Evolving Verifiable Random Functions and Applications**
  2024-04-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/628)
  Bernardo David, Rafael Dowsley, Anders Konring, Mario Larangeira

  <details><summary>摘要 / Abstract</summary>

  A Verifiable Random Function (VRF) can be evaluated on an input by a prover who holds a secret key, generating a pseudorandom output and a proof of output validity that can be verified using the corresponding public key. VRFs are a central building block of committee election mechanisms that sample parties to execute tasks in cryptographic protocols, e.g. generating blocks in a Proof-of-Stake (PoS) blockchain or executing a round of MPC protocols. We propose the notion, and a matching construction, of an Aggregatable Key-Evolving VRF (A-KE-VRF) with the following extra properties: 1. Aggregation: combining proofs for several VRF evaluations of different inputs under different secret keys into a single constant size proof; 2. Key-Evolving: preventing adversaries who corrupt a party (learning their secret key) from ``forging&#x27;&#x27; proofs of past VRF evaluations. As an immediate application, we improve on the block size of PoS blockchains and on the efficiency of Proofs of Proof-of-Stake (PoPoS). Furthermore, the A-KE-VRF notion allows us to construct Encryption to the Future (EtF) and Authentication from the Past (AfP) schemes with a Key-Evolving property, which provides forward security. An EtF scheme allows for sending a message to a party who is randomly selected to execute a role in the future, while an AfP scheme allows for this party to authenticate their messages as coming from a past execution of this role. These primitives are essential for realizing the YOSO MPC Framework (CRYPTO&#x27;21).

  匹配依据：MPC: mpc (context)

  </details>

- **Advance Sharing with Ogawa et al.'s Ramp Quantum Secret Sharing Scheme**
  2024-04-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.15646)
  Satoshi Masumori, Ryutaroh Matsumoto

  <details><summary>摘要 / Abstract</summary>

  The ramp quantum secret sharing proposed by Ogawa et al. has the highest possible coding rate given a threshold type access structure. On the other hand, in some quantum secret sharing schemes, it is known that some shares can be distributed to participants before a secret is given to the dealer. However, it is unclear whether some shares can be distributed before a secret is given in Ogawa et al.&#x27;s scheme. In this paper, we propose a method to distribute some shares before a secret is given in Ogawa et al.&#x27;s scheme, then determine a necessary and sufficient condition on sets of shares that can be distributed before a given secret.

  匹配依据：MPC: secret sharing

  </details>

- **On Generating Cancelable Biometric Template using Reverse of Boolean XOR**
  2024-04-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.15394)
  Manisha, Nitin Kumar

  <details><summary>摘要 / Abstract</summary>

  Cancelable Biometric is repetitive distortion embedded in original Biometric image for keeping it secure from unauthorized access. In this paper, we have generated Cancelable Biometric templates with Reverse Boolean XOR technique. Three different methods have been proposed for generation of Cancelable Biometric templates based on Visual Secret Sharing scheme. In each method, one Secret image and n-1 Cover images are used as: (M1) One original Biometric image (Secret) with n- 1 randomly chosen Gray Cover images (M2) One original Secret image with n-1 Cover images, which are Randomly Permuted version of the original Secret image (M3) One Secret image with n-1 Cover images, both Secret image and Cover images are Randomly Permuted version of original Biometric image. Experiment works have performed on publicly available ORL Face database and IIT Delhi Iris database. The performance of the proposed methods is compared in terms of Co-relation Coefficient (Cr), Mean Square Error (MSE), Mean Absolute Error (MAE), Structural Similarity (SSIM), Peak Signal to Noise Ratio (PSNR), Number of Pixel Change Rate (NPCR), and Unified Average Changing Intensity (UACI). It is found that among the three proposed method, M3 generates good quality Cancelable templates and gives best performance in terms of quality. M3 is also better in quantitative terms on ORL dataset while M2 and M3 are comparable on IIT Delhi Iris dataset.

  匹配依据：MPC: secret sharing

  </details>

- **Interactive Threshold Mercurial Signatures and Applications**
  2024-04-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/625)
  Masayuki Abe, Masaya Nanri, Octavio Perez Kempner, Mehdi Tibouchi

  <details><summary>摘要 / Abstract</summary>

  Mercurial signatures are an extension of equivalence class signatures that allow malleability for the public keys, messages, and signatures within the respective classes. Unfortunately, the most efficient construction to date suffers from a weak public key class-hiding property, where the original signer with the signing key can link the public keys in the same class. This is a severe limitation in their applications, where the signer is often considered untrustworthy of privacy. This paper presents two-party and multi-party interactive threshold mercurial signatures that overcome the above limitation by eliminating the single entity who knows the signing key. For the general case, we propose two constructions. The first follows the same interactive structure as the two-party case, avoiding complex distributed computations such as randomness generation, inversion, and multiplication, and even eliminates the need for private communication between parties. The second is based on a blueprint for general multi-party computation using verifiable secret sharing, but adopting optimizations. We show applications in anonymous credential systems that individually fit the two-party and multi-party constructions. In particular, in the two-party case, our approach provides stronger privacy by completely removing the trust in the authorities. We also discuss more applications, from blind signatures to multi-signatures and threshold ring signatures. Finally, to showcase the practicality of our approach, we implement our interactive constructions and compare them against related alternatives.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Private Agent-Based Modeling**
  2024-04-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.12983)
  Ayush Chopra, Arnau Quera-Bofarull, Nurullah Giray-Kuru, Michael Wooldridge, Ramesh Raskar

  <details><summary>摘要 / Abstract</summary>

  The practical utility of agent-based models in decision-making relies on their capacity to accurately replicate populations while seamlessly integrating real-world data streams. Yet, the incorporation of such data poses significant challenges due to privacy concerns. To address this issue, we introduce a paradigm for private agent-based modeling wherein the simulation, calibration, and analysis of agent-based models can be achieved without centralizing the agents attributes or interactions. The key insight is to leverage techniques from secure multi-party computation to design protocols for decentralized computation in agent-based models. This ensures the confidentiality of the simulated agents without compromising on simulation accuracy. We showcase our protocols on a case study with an epidemiological simulation comprising over 150,000 agents. We believe this is a critical step towards deploying agent-based models to real-world applications.

  匹配依据：MPC: secure multi party computation

  </details>

- **Improving Privacy-Preserving Techniques for Smart Grid using Lattice-based Cryptography**
  2024-04-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.16865)
  Saleh Darzi, Bahareh Akhbari, Hassan Khodaiemehr

  <details><summary>摘要 / Abstract</summary>

  Advancements in communication and information tech birthed the Smart Grid, optimizing energy and data transmission. Yet, user privacy is at risk due to frequent data collection. Existing privacy schemes face vulnerability with quantum machines. To tackle this, the LPM2DA scheme is introduced, utilizing lattice-based encryption and signatures for secure data aggregation. It ensures privacy, integrity, and authentication, enabling statistical analysis while preserving user privacy. Traditional aggregation schemes suffer from weak network models and centralization issues. Enter SPDBlock, a blockchain-based solution ensuring privacy, integrity, and resistance to attacks. It detects and prosecutes malicious entities while efficiently handling multi-dimensional data transmission. Through distributed decryption and secret sharing, only valid data can be decrypted with minimal involvement from smart meters. Performance tests reveal SPDBlock&#x27;s superiority in communication and computational efficiency over traditional schemes.

  匹配依据：MPC: secret sharing

  </details>

- **A robust and composable device-independent protocol for oblivious transfer using (fully) untrusted quantum devices in the bounded storage model**
  2024-04-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.11283)
  Rishabh Batra, Sayantan Chakraborty, Rahul Jain, Upendra Kapshikar

  <details><summary>摘要 / Abstract</summary>

  We present a robust and composable device-independent (DI) quantum protocol between two parties for oblivious transfer (OT) using Magic Square devices in the bounded storage model in which the (honest and cheating) devices and parties have no long-term quantum memory. After a fixed constant (real-world) time interval, referred to as DELAY, the quantum states decohere completely. The adversary (cheating party), with full control over the devices, is allowed joint (non-IID) quantum operations on the devices, and there are no time and space complexity bounds placed on its powers. The running time of the honest parties is polylog(λ) (where λ is the security parameter). Our protocol has negligible (in λ) correctness and security errors and can be implemented in the NISQ (Noisy Intermediate Scale Quantum) era. By robustness, we mean that our protocol is correct even when devices are slightly off (by a small constant) from their ideal specification. This is an important property since small manufacturing errors in the real-world devices are inevitable. Our protocol is sequentially composable and, hence, can be used as a building block to construct larger protocols (including DI bit-commitment and DI secure multi-party computation) while still preserving correctness and security guarantees. None of the known DI protocols for OT in the literature are robust and secure against joint quantum attacks. This was a major open question in device-independent two-party distrustful cryptography, which we resolve. We prove a parallel repetition theorem for a certain class of entangled games with a hybrid (quantum-classical) strategy to show the security of our protocol. The hybrid strategy helps to incorporate DELAY in our protocol. This parallel repetition theorem is a main technical contribution of our work.

  匹配依据：MPC: oblivious transfer, secure multi party computation

  </details>

- **Improved Alternating-Moduli PRFs and Post-Quantum Signatures**
  2024-04-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/582)
  Navid Alamati, Guru-Vamsi Policharla, Srinivasan Raghuraman, Peter Rindal

  <details><summary>摘要 / Abstract</summary>

  We revisit the alternating-moduli paradigm for constructing symmetric-key primitives with a focus on constructing efficient protocols to evaluate them using secure multi-party computation (MPC). The alternating-moduli paradigm of Boneh, Ishai, Passelègue, Sahai, and Wu (TCC 2018) enables the construction of various symmetric-key primitives with the common characteristic that the inputs are multiplied by two linear maps over different moduli. The first contribution focuses on efficient two-party evaluation of alternating-moduli pseudorandom functions (PRFs), effectively building an oblivious PRF. We present a generalized alternating-moduli PRF construction along with methods to lower the communication and computation. We then provide several variants of our protocols with different computation and communication tradeoffs for evaluating the PRF. Most of our protocols are in the hybrid model while one is based on specialized garbling. Our most efficient protocol effectively is about $3\times$ faster and requires $1.3\times$ less communication. Our next contribution is the efficient evaluation of the one-way function (OWF) $f(x)=\mathbf{B}\cdot_3 (\mathbf{A} \cdot_2 x)$ proposed by Dinur, Goldfeder, Halevi, Ishai, Kelkar, Sharma, and Zaverucha (CRYPTO 21) where $\mathbf{A} \in \mathbb{F}^{m\times n}_2, \mathbf{B}\in\mathbb{F}^{t\times m}_3$, and $\cdot_p$ is multiplication mod $p$. This surprisingly simple OWF can be evaluated within MPC by secret sharing $[\![x]\!]$ over $\mathbb{F}_2$, locally computing $[\![v]\!]=\mathbf{A}\cdot_2 [\![x]\!]$, performing a modulus switching protocol to $\mathbb{F}_3$ shares, followed by locally computing the output shares $[\![y]\!]=\mathbf{B}\cdot_3 [\![v]\!]$. We design a bespoke MPC-in-the-Head (MPCitH) signature scheme that evaluates the aforementioned OWF, achieving state-of-the-art performance. The resulting signature has a size ranging from $4.0$ to $5.5$ KB, achieving between $2\text{-}3\times$ reduction compared to the prior work. To the best of our knowledge, this is only $\approx 5\%$ larger than the smallest signature based on symmetric-key primitives, including the latest NIST post-quantum cryptography competition submissions. We also show that our core techniques can be extended to build very small post-quantum ring signatures for rings of small to medium size, which are competitive with state-of-the-art lattice-based schemes. Our techniques are in fact more generally applicable to set membership in MPCitH.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Privacy-Preserving Federated Unlearning with Certified Client Removal**
  2024-04-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.09724)
  Ziyao Liu, Huanyi Ye, Yu Jiang, Jiyuan Shen, Jiale Guo, Ivan Tjuawinata, Kwok-Yan Lam

  <details><summary>摘要 / Abstract</summary>

  In recent years, Federated Unlearning (FU) has gained attention for addressing the removal of a client&#x27;s influence from the global model in Federated Learning (FL) systems, thereby ensuring the ``right to be forgotten&quot; (RTBF). State-of-the-art methods for unlearning use historical data from FL clients, such as gradients or locally trained models. However, studies have revealed significant information leakage in this setting, with the possibility of reconstructing a user&#x27;s local data from their uploaded information. Addressing this, we propose Starfish, a privacy-preserving federated unlearning scheme using Two-Party Computation (2PC) techniques and shared historical client data between two non-colluding servers. Starfish builds upon existing FU methods to ensure privacy in unlearning processes. To enhance the efficiency of privacy-preserving FU evaluations, we suggest 2PC-friendly alternatives for certain FU algorithm operations. We also implement strategies to reduce costs associated with 2PC operations and lessen cumulative approximation errors. Moreover, we establish a theoretical bound for the difference between the unlearned global model via Starfish and a global model retrained from scratch for certified client removal. Our theoretical and experimental analyses demonstrate that Starfish achieves effective unlearning with reasonable efficiency, maintaining privacy and security in FL systems.

  匹配依据：MPC: two party computation

  </details>

- **EQO: Exploring Ultra-Efficient Private Inference with Winograd-Based Protocol and Quantization Co-Optimization**
  2024-04-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.09404)
  Wenxuan Zeng, Tianshi Xu, Meng Li, Runsheng Wang

  <details><summary>摘要 / Abstract</summary>

  Private convolutional neural network (CNN) inference based on secure two-party computation (2PC) suffers from high communication and latency overhead, especially from convolution layers. In this paper, we propose EQO, a quantized 2PC inference framework that jointly optimizes the CNNs and 2PC protocols. EQO features a novel 2PC protocol that combines Winograd transformation with quantization for efficient convolution computation. However, we observe naively combining quantization and Winograd convolution is sub-optimal: Winograd transformations introduce extensive local additions and weight outliers that increase the quantization bit widths and require frequent bit width conversions with non-negligible communication overhead. Therefore, at the protocol level, we propose a series of optimizations for the 2PC inference graph to minimize the communication. At the network level, We develop a sensitivity-based mixed-precision quantization algorithm to optimize network accuracy given communication constraints. We further propose a 2PC-friendly bit re-weighting algorithm to accommodate weight outliers without increasing bit widths. With extensive experiments, EQO demonstrates 11.7x, 3.6x, and 6.3x communication reduction with 1.29%, 1.16%, and 1.29% higher accuracy compared to state-of-the-art frameworks SiRNN, COINN, and CoPriv, respectively.

  匹配依据：MPC: secure two party computation

  </details>

- **Make Split, not Hijack: Preventing Feature-Space Hijacking Attacks in Split Learning**
  2024-04-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.09265)
  Tanveer Khan, Mindaugas Budzys, Antonis Michalas

  <details><summary>摘要 / Abstract</summary>

  The popularity of Machine Learning (ML) makes the privacy of sensitive data more imperative than ever. Collaborative learning techniques like Split Learning (SL) aim to protect client data while enhancing ML processes. Though promising, SL has been proved to be vulnerable to a plethora of attacks, thus raising concerns about its effectiveness on data privacy. In this work, we introduce a hybrid approach combining SL and Function Secret Sharing (FSS) to ensure client data privacy. The client adds a random mask to the activation map before sending it to the servers. The servers cannot access the original function but instead work with shares generated using FSS. Consequently, during both forward and backward propagation, the servers cannot reconstruct the client&#x27;s raw data from the activation map. Furthermore, through visual invertibility, we demonstrate that the server is incapable of reconstructing the raw image data from the activation map when using FSS. It enhances privacy by reducing privacy leakage compared to other SL-based approaches where the server can access client input information. Our approach also ensures security against feature space hijacking attack, protecting sensitive information from potential manipulation. Our protocols yield promising results, reducing communication overhead by over 2x and training time by over 7x compared to the same model with FSS, without any SL. Also, we show that our approach achieves &gt;96% accuracy and remains equivalent to the plaintext models.

  匹配依据：MPC: secret sharing

  </details>

- **Communication-Efficient Multi-Party Computation for RMS Programs**
  2024-04-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/568)
  Thomas Attema, Aron van Baarsen, Stefan van den Berg, Pedro Capitão, Vincent Dunning, Lisa Kohl

  <details><summary>摘要 / Abstract</summary>

  Despite much progress, general-purpose secure multi-party computation (MPC) with active security may still be prohibitively expensive in settings with large input datasets. This particularly applies to the secure evaluation of graph algorithms, where each party holds a subset of a large graph. Recently, Araki et al. (ACM CCS &#x27;21) showed that dedicated solutions may provide significantly better efficiency if the input graph is sparse. In particular, they provide an efficient protocol for the secure evaluation of &quot;message passing&quot; algorithms, such as the PageRank algorithm. Their protocol&#x27;s computation and communication complexity are both $\tilde{O}(M\cdot B)$ instead of the $O(M^2)$ complexity achieved by general-purpose MPC protocols, where $M$ denotes the number of nodes and $B$ the (average) number of incoming edges per node. On the downside, their approach achieves only a relatively weak security notion; $1$-out-of-$3$ malicious security with selective abort. In this work, we show that PageRank can instead be captured efficiently as a restricted multiplication straight-line (RMS) program, and present a new actively secure MPC protocol tailored to handle RMS programs. In particular, we show that the local knowledge of the participants can be leveraged towards the first maliciously-secure protocol with communication complexity linear in $M$, independently of the sparsity of the graph. We present two variants of our protocol. In our communication-optimized protocol, going from semi-honest to malicious security only introduces a small communication overhead, but results in quadratic computation complexity $O(M^2)$. In our balanced protocol, we still achieve a linear communication complexity $O(M)$, although with worse constants, but a significantly better computational complexity scaling with $O(M\cdot B)$. Additionally, our protocols achieve security with identifiable abort and can tolerate up to $n-1$ corruptions.

  匹配依据：MPC: multi party computation, secure evaluation, secure multi party computation

  </details>

- **Amortizing Circuit-PSI in the Multiple Sender/Receiver Setting**
  2024-04-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/567)
  Aron van Baarsen, Marc Stevens

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) is a cryptographic functionality for two parties to learn the intersection of their input sets, without leaking any other information. Circuit-PSI is a stronger PSI functionality where the parties learn only a secret-shared form of the desired intersection, thus without revealing the intersection directly. These secret shares can subsequently serve as input to a secure multiparty computation of any function on this intersection. In this paper we consider several settings in which parties take part in multiple Circuit-PSI executions with the same input set, and aim to amortize communications and computations. To that end, we build up a new framework for Circuit-PSI around generalizations of oblivious (programmable) PRFs that are extended with offline setup phases. We present several efficient instantiations of this framework with new security proofs for this setting. As a side result, we obtain a slight improvement in communication and computation complexity over the state-of-the-art semi-honest Circuit-PSI protocol by Bienstock et al. (USENIX &#x27;23). Additionally, we present a novel Circuit-PSI protocol from a PRF with secret-shared outputs, which has linear communication and computation complexity in the parties&#x27; input set sizes, and is able to realize a stronger security notion. Lastly, we derive the potential amortizations over multiple protocol executions, and observe that each of the presented instantiations is favorable in at least one of the multiple-execution settings.

  匹配依据：MPC: private set intersection, secure multiparty computation

  </details>

- **A Round-Optimal Near-Linear Third-Party Private Set Intersection Protocol**
  2024-04-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/566)
  Foo Yee Yeo, Jason H. M. Ying

  <details><summary>摘要 / Abstract</summary>

  Third-party private set intersection (PSI) enables two parties, each holding a private set to compute their intersection and reveal the result only to an inputless third party. In this paper, we present an efficient round-optimal third-party PSI protocol. Our work is motivated by real-world applications such as contact tracing whereby expedition is essential while concurrently preserving privacy. Our construction only requires $2$ communication rounds and attains a near-linear computational complexity of $O(n^{1+\varepsilon})$ for large dataset size $n$, where $\varepsilon&gt;0$ is any fixed constant. Our improvements stem from algorithmic changes and the incorporation of new techniques to achieve a tight asymptotic bound. Furthermore, we also present a third-party PSI cardinality protocol which has not been explored in prior third-party PSI work. In a third-party PSI cardinality setting, only the third-party obtains the size of the intersection and nothing else. Our construction to achieve the cardinality functionality attains a quasilinear computational complexity for the third-party.

  匹配依据：MPC: private set intersection

  </details>

- **Certification of MPC-based zonal controller security properties using accuracy-aware machine learning proxies**
  2024-04-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.07275)
  Pierre Houdouin, Manuel Ruiz, Patrick Panciatici

  <details><summary>摘要 / Abstract</summary>

  The fast growth of renewable energies increases the power congestion risk. To address this issue, the French Transmission System Operator (RTE) has developed closed-loop controllers to handle congestion. RTE wishes to estimate the probability that the controllers ensure the equipment&#x27;s safety to guarantee their proper functioning. The naive approach to estimating this probability relies on simulating many randomly drawn scenarios and then using all the outcomes to build a confidence interval around the probability. Although theory ensures convergence, the computational cost of power system simulations makes such a process intractable. The present paper aims to propose a faster process using machine-learning-based proxies. The amount of required simulations is significantly reduced thanks to an accuracy-aware proxy built with Multivariate Gaussian Processes. However, using a proxy instead of the simulator adds uncertainty to the outcomes. An adaptation of the Central Limit Theorem is thus proposed to include the uncertainty of the outcomes predicted with the proxy into the confidence interval. As a case study, we designed a simple simulator that was tested on a small network. Results show that the proxy learns to approximate the simulator&#x27;s answer accurately, allowing a significant time gain for the machine-learning-based process.

  匹配依据：MPC: mpc (context)

  </details>

- **Distributing Arbitrary Quantum Graph States by Graph Transformation**
  2024-04-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.05537)
  Tingxiang Ji, Jianqing Liu, Zheshen Zhang

  <details><summary>摘要 / Abstract</summary>

  Quantum graph state is a special class of nonlocal state among multiple quantum particles, underpinning several nonclassical and promising applications such as quantum computing and quantum secret sharing. Recently, establishing quantum graph states among physically distant nodes has gained increasing popularity owing to its potential in expanding current quantum applications in scale. Existing research on this topic relies on a two-step approach: first distributing low-dimension elementary entanglement to target nodes, and then fusing them into a high-dimension quantum graph state. However, most existing studies focus solely on minimizing costs (e.g., the number of elementary entanglements consumed) to entangle target nodes, while neglecting the structure of the final quantum graph state. This can easily result in weak system entanglement, jeopardizing the graph state under partial measurement or noises. In this paper, we aim to establish any arbitrary quantum graph states of strong entanglement structures at a much lower cost than the state of the art. The method is to search for and establish an alternative state to the target state that is of lowest cost in creation. Subsequently, we transform such an alternative state back to the target state via compressed single-qubit Clifford operations. To verify the performance of our developed algorithm, we conduct comprehensive simulations based on an open dataset containing all graph state structures up to 8 qubits. The results demonstrate fast algorithm convergence, an increased success probability in distributing any graph states, and $53.57\%$ saving in ERP cost compared with the state-of-the-art baseline.

  匹配依据：MPC: secret sharing

  </details>

- **Breaking Bicoptor from S$\\&amp;$P 2023 Based on Practical Secret Recovery Attack**
  2024-04-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/542)
  Jun Xu, Zhiwei Li, Lei Hu

  <details><summary>摘要 / Abstract</summary>

  At S$\&amp;$P 2023, a family of secure three-party computing protocols called Bicoptor was proposed by Zhou et al., which is used to compute non-linear functions in privacy preserving machine learning. In these protocols, two parties $P_0, P_1$ respectively hold the corresponding shares of the secret, while a third party $P_2$ acts as an assistant. The authors claimed that neither party in the Bicoptor can independently compromise the confidentiality of the input, intermediate, or output. In this paper, we point out that this claim is incorrect. The assistant $P_2$ can recover the secret in the DReLU protocol, which is the basis of Bicoptor. The restoration of its secret will result in the security of the remaining protocols in Bicoptor being compromised. Specifically, we provide two secret recovery attacks regarding the DReLU protocol. The first attack method belongs to a clever enumeration method, which is mainly due to the derivation of the modular equation about the secret and its share. The key of the second attack lies in solving the small integer root problem of a modular equation, as the lattices involved are only 3 or 4 dimensions, the LLL algorithm can effectively work. For the system settings selected by Bicoptor, our experiment shows that the desired secret in the DReLU protocol can be restored within one second on a personal computer. Therefore, when using cryptographic protocols in the field of privacy preserving machine learning, it is not only important to pay attention to design overhead, but also to be particularly careful of potential security threats.

  匹配依据：MPC: secure three party computing

  </details>

- **A post-quantum Distributed OPRF from the Legendre PRF**
  2024-04-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/544)
  Novak Kaluđerović, Nan Cheng, Katerina Mitrokotsa

  <details><summary>摘要 / Abstract</summary>

  A distributed OPRF enables a client to evaluate a pseudo-random function on a client-chosen input using a distributed key shared among multiple servers, ensuring that the servers learn nothing about the input or output, while the client learns nothing about the key. We present a post-quantum OPRF suitable for a distributed server setting, requiring only two rounds of communication between the client and servers, with server-to-server communication limited to a pre-computation phase. Our approach leverages the Legendre PRF, computed through a single MPC multiplication and opening during the online phase. We introduce a novel MPC technique that achieves multiplication and opening in one round using replicated secret sharing (RSS) in a malicious adversarial model. This allows for the quantum-secure, verifiable evaluation of the Legendre OPRF against malicious adversaries under a threshold assumption, without requiring inter-server communication. Beyond the Legendre PRF, this method is also of interest for general MPC operations. To our knowledge, our distributed OPRF (dOPRF) is the first post-quantum construction with these properties. We compare our approach to state-of-the-art MPC solutions and provide an implementation of our proposed dOPRF, benchmarking it against existing OPRF constructions. In our comparison, our dOPRF protocol demonstrates superior efficiency.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Traceable Functional Encryption for Inner Product**
  2024-04-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.04861)
  Muyao Qiu, Jinguang Han

  <details><summary>摘要 / Abstract</summary>

  Functional encryption introduces a new paradigm of public key encryption that decryption only reveals the function value of encrypted data. To curb key leakage issues and trace users in FE-IP, a new primitive called traceable functional encryption for inner product (TFE-IP) has been proposed. However, the privacy protection of user&#x27;s identities has not been considered in the existing TFE-IP schemes. In order to balance privacy and accountability, we propose the concept of privacy-preserving traceable functional encryption for inner product (PPTFE-IP) and give a concrete construction. Our scheme provides the following features: (1) To prevent key sharing, a user&#x27;s key is bound with both his/her identity and a vector; (2) The key generation center (KGC) and a user execute a two-party secure computing protocol to generate a key without the former knowing anything about the latter&#x27;s identity; (3) Each user can verify the correctness of his/her key; (4) A user can calculate the inner product of the two vectors embedded in his/her key and in a ciphertext; (5) Only the tracer can trace the identity embedded in a key. The security of our scheme is formally reduced to well-known complexity assumptions, and the implementation is conducted to evaluate its efficiency. The novelty of our scheme is to protect users&#x27; privacy and provide traceability if required.

  匹配依据：MPC: secure computing

  </details>

- **Lattice-Based Timed Cryptography**
  2024-04-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/540)
  Russell W. F. Lai, Giulio Malavolta

  <details><summary>摘要 / Abstract</summary>

  Timed cryptography studies primitives that retain their security only for a predetermined amount of time, such as proofs of sequential work and time-lock puzzles. This feature has proven to be useful in a large number of practical applications, e.g. randomness generation, sealed-bid auctions, and fair multi-party computation. However, the current state of affairs in timed cryptography is unsatisfactory: Virtually all efficient constructions rely on a single sequentiality assumption, namely that repeated squaring in unknown order groups cannot be parallelised. This is a single point of failure in the classical setting and is even false against quantum adversaries. In this work we put forward a new sequentiality assumption, which essentially says that a repeated application of the standard lattice-based hash function cannot be parallelised. We provide concrete evidence of the validity of this assumption and perform some initial cryptanalysis. We also propose a new template to construct proofs of sequential work, based on lattice techniques.

  匹配依据：MPC: multi party computation

  </details>

- **Dual Support Decomposition in the Head: Shorter Signatures from Rank SD and MinRank**
  2024-04-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/541)
  Loïc Bidoux, Thibauld Feneuil, Philippe Gaborit, Romaric Neveu, Matthieu Rivain

  <details><summary>摘要 / Abstract</summary>

  The MPC-in-the-Head (MPCitH) paradigm is widely used for building post-quantum signature schemes, as it provides a versatile way to design proofs of knowledge based on hard problems. Over the years, the MPCitH landscape has changed significantly, with the most recent improvements coming from VOLE-in-the-Head (VOLEitH) and Threshold-Computation-in-the-Head (TCitH). While a straightforward application of these frameworks already improve the existing MPCitH-based signatures, we show in this work that we can adapt the arithmetic constraints representing the underlying security assumptions (here called the modeling) to achieve smaller sizes using these new techniques. More precisely, we explore existing modelings for the rank syndrome decoding (RSD) and MinRank problems and we introduce a new modeling, named dual support decomposition, which achieves better sizes with the VOLEitH and TCitH frameworks by minimizing the size of the witnesses. While this modeling is naturally more efficient than the other ones for a large set of parameters, we show that it is possible to go even further and explore new areas of parameters. With these new modeling and parameters, we obtain low-size witnesses which drastically reduces the size of the arithmetic part of the signature. We apply the TCitH and VOLEitH frameworks to our new modeling for both RSD and MinRank and compare our results to the NIST candidates RYDE, MiRitH, and MIRA (MPCitH-based schemes from RSD and MinRank). We also note that recent techniques optimizing the sizes of GGM trees are applicable to our schemes and further reduce the signature sizes by a few hundred bytes. We obtain signature sizes below 3.5 kB for 128 bits of security with N=256 parties (a.k.a. leaves in the GGM trees) and going as low as ≈ 2.8 kB with N=2048, for both RSD and MinRank. This represents an improvement of more than 2 kB compared to the original submissions to the 2023 NIST call for additional signatures.

  匹配依据：MPC: mpc (context)

  </details>

- **Confidential and Verifiable Machine Learning Delegations on the Cloud**
  2024-04-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/537)
  Wenxuan Wu, Soamar Homsi, Yupeng Zhang

  <details><summary>摘要 / Abstract</summary>

  With the growing adoption of cloud computing, the ability to store data and delegate computations to powerful and affordable cloud servers have become advantageous for both companies and individual users. However, the security of cloud computing has emerged as a significant concern. Particularly, Cloud Service Providers (CSPs) cannot assure data confidentiality and computations integrity in mission-critical applications. In this paper, we propose a confidential and verifiable delegation scheme that advances and overcomes major performance limitations of existing Secure Multiparty Computation (MPC) and Zero Knowledge Proof (ZKP). Secret-shared Data and delegated computations to multiple cloud servers remain completely confidential as long as there is at least one honest MPC server. Moreover, results are guaranteed to be valid even if all the participating servers are malicious. Specifically, we design an efficient protocol based on interactive proofs, such that most of the computations generating the proof can be done locally on each server. In addition, we propose a special protocol for matrix multiplication where the overhead of generating the proof is asymptotically smaller than the time to evaluate the result in MPC. Experimental evaluation demonstrates that our scheme significantly outperforms prior work, with the online prover time being 1-2 orders of magnitude faster. Notably, in the matrix multiplication protocol, only a minimal 2% of the total time is spent on the proof generation. Furthermore, we conducted tests on machine learning inference tasks. We executed the protocol for a fully-connected neural network with 3 layers on the MNIST dataset and it takes 2.6 seconds to compute the inference in MPC and generate the proof, 88× faster than prior work. We also tested the convolutional neural network of Lenet with 2 convolution layers and 3 dense layers and the running time is less than 300 seconds across three servers.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Avoiding Trusted Setup in Isogeny-based Commitments**
  2024-04-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/531)
  Gustave Tchoffo Saah, Tako Boris Fouotsa, Emmanuel Fouotsa, Célestin Nkuimi-Jugnia

  <details><summary>摘要 / Abstract</summary>

  In 2021, Sterner proposed a commitment scheme based on supersingular isogenies. For this scheme to be binding, one relies on a trusted party to generate a starting supersingular elliptic curve of unknown endomorphism ring. In fact, the knowledge of the endomorphism ring allows one to compute an endomorphism of degree a power of a given small prime. Such an endomorphism can then be split into two to obtain two different messages with the same commitment. This is the reason why one needs a curve of unknown endomorphism ring, and the only known way to generate such supersingular curves is to rely on a trusted party or on some expensive multiparty computation. We observe that if the degree of the endomorphism in play is well chosen, then the knowledge of the endomorphism ring is not sufficient to efficiently compute such an endomorphism and in some particular cases, one can even prove that endomorphism of a certain degree do not exist. Leveraging these observations, we adapt Sterner&#x27;s commitment scheme in such a way that the endomorphism ring of the starting curve can be known and public. This allows us to obtain isogeny-based commitment schemes which can be instantiated without trusted setup requirements.

  匹配依据：MPC: multiparty computation

  </details>

- **Privacy Preserving Biometric Authentication for Fingerprints and Beyond**
  2024-04-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/525)
  Marina Blanton, Dennis Murphy

  <details><summary>摘要 / Abstract</summary>

  Biometric authentication eliminates the need for users to remember secrets and serves as a convenient mechanism for user authentication. Traditional implementations of biometric-based authentication store sensitive user biometry on the server and the server becomes an attractive target of attack and a source of large-scale unintended disclosure of biometric data. To mitigate the problem, we can resort to privacy-preserving computation and store only protected biometrics on the server. While a variety of secure computation techniques is available, our analysis of privacy-preserving biometric computation and biometric authentication constructions revealed that available solutions fall short of addressing the challenges of privacy-preserving biometric authentication. Thus, in this work we put forward new constructions to address the challenges. Our solutions employ a helper server and use strong threat models, where a client is always assumed to be malicious, while the helper server can be semi-honest or malicious. We also determined that standard secure multi-party computation security definitions are insufficient to properly demonstrate security in the two-phase (enrollment and authentication) entity authentication application. We thus extend the model and formally show security in the multi-phase setting, where information can flow from one phase to another and the set of participants can change between the phases. We implement our constructions and show that they exhibit practical performance for authentication in real time.

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **Making Privacy-preserving Federated Graph Analytics with Strong Guarantees Practical (for Certain Queries)**
  2024-04-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.01619)
  Kunlong Liu, Trinabh Gupta

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving federated graph analytics is an emerging area of research. The goal is to run graph analytics queries over a set of devices that are organized as a graph while keeping the raw data on the devices rather than centralizing it. Further, no entity may learn any new information except for the final query result. For instance, a device may not learn a neighbor&#x27;s data. The state-of-the-art prior work for this problem provides privacy guarantees for a broad set of queries in a strong threat model where the devices can be malicious. However, it imposes an impractical overhead: each device locally requires over 8.79 hours of cpu time and 5.73 GiBs of network transfers per query. This paper presents Colo, a new, low-cost system for privacy-preserving federated graph analytics that requires minutes of cpu time and a few MiBs in network transfers, for a particular subset of queries. At the heart of Colo is a new secure computation protocol that enables a device to securely and efficiently evaluate a graph query in its local neighborhood while hiding device data, edge data, and topology data. An implementation and evaluation of Colo shows that for running a variety of COVID-19 queries over a population of 1M devices, it requires less than 8.4 minutes of a device&#x27;s CPU time and 4.93 MiBs in network transfers - improvements of up to three orders of magnitude.

  匹配依据：MPC: secure computation

  </details>

- **Maximal Secret Reconstruction, Teleportation and Bell's Inequality**
  2024-04-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.01212)
  Pratishtha Abrol, Pahulpreet Singh, Indranil Chakrabarty

  <details><summary>摘要 / Abstract</summary>

  A tripartite state is said to be a potential resource for secret sharing if the state imposes restrictions on the teleportation fidelity of the bipartite dealer--reconstructor and dealer--assistant channels in addition of being useful for the state reconstruction. Given a secret shareable state in a pure three-qubit system, we are able to characterize the set of states with maximum possible reconstruction fidelity (abbreviated as MSR states) for a fixed value of the maximum teleportation fidelity that can be obtained out of both the dealer--receiver channels. Similarly for a value giving the maximum of Bell-CHSH value of both dealer--reconstructor and dealer--assistant channels, we are able to find the maximum achievable reconstruction fidelity. Interestingly, we find that all secret shareable states satisfy Bell&#x27;s inequality in both dealer--reconstructor and dealer--assistant partitions. This brings out a new mutual exclusivity between secret shareable state and Bell&#x27;s inequality violations. Our result paves the way in identifying the best candidate among the secret sharing resource states in achieving the maximum reconstruction fidelity thus by setting the practical information transfer limit in a possible resource theoretic extension of secret sharing. It also brings out a new kind of mutual exclusiveness between the bipartite correlation and in the ability of secret sharing in a tripartite setting.

  匹配依据：MPC: secret sharing

  </details>

- **Secure Multi-Party Linear Algebra with Perfect Correctness**
  2024-03-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/508)
  Jules Maire, Damien Vergnaud

  <details><summary>摘要 / Abstract</summary>

  We present new secure multi-party computation protocols for linear algebra over a finite field, which improve the state-of-the-art in terms of security. We look at the case of \emph{unconditional security with perfect correctness}, i.e., information-theoretic security without errors. We notably propose an expected constant-round protocol for solving systems of $m$ linear equations in $n$ variables over $\mathbb{F}_q$ with expected complexity $O(k(n^{2.5} + m^{2.5}+n^2m^{0.5}))$ where $k &gt; m(m+n)+1$ (complexity is measured in terms of the number of secure multiplications required). The previous proposals were not error-free: known protocols can indeed fail and thus reveal information with probability $\Omega(\textsf{poly}(m)/q)$. Our protocols are simple and rely on existing computer-algebra techniques, notably the Preparata-Sarwate algorithm, a simple but poorly known ``baby-step giant-step&#x27;&#x27; method for computing the characteristic polynomial of a matrix, and techniques due to Mulmuley for error-free linear algebra in positive characteristic.

  匹配依据：MPC: secure multi party computation

  </details>

- **Weakly Super-Invertible Matrices and Constant Communication Dishonest Majority MPC**
  2024-03-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/503)
  Alexander Bienstock, Kevin Yeo

  <details><summary>摘要 / Abstract</summary>

  In recent years, there has been tremendous progress in improving the concrete communication complexity of dishonest majority MPC. In the sub-optimal corruption threshold setting where $t&lt;(1-\varepsilon)\cdot n$ for some constant $0&lt;\varepsilon\leq 1/2$, Sharing Transformation (Goyal $\textit{et al.}$, CRYPTO&#x27;22) and SuperPack (Escudero $\textit{et al.}$, EUROCRYPT&#x27;23) presented protocols with information-theoretic online phases requiring $O(1)$ field elements of total communication per multiplication gate. However, Sharing Transformation assumes that their offline phase is instantiated by a trusted party, while SuperPack instantiates their offline phase with large communication of $\Omega(n)$ per multiplication gate assuming oblivious linear evaluation (OLE) correlations. The main bottleneck in instantiating the offline phases of both protocols is generating random packed beaver triples of the form $[\mathbf{a}],[\mathbf{b}],[\mathbf{c}]$, for random $\mathbf{a},\mathbf{b}\in\mathbb{F}^k$, and $\mathbf{c}=\mathbf{a}*\mathbf{b}\in\mathbb{F}^k$, where $k=\Omega(n)$ is the $\textit{packing parameter}$. To address this bottleneck, our main technical contribution is introducing and constructing $\textit{weakly}$ super-invertible matrices, a relaxation of super-invertible matrices in which sub-matrices have high (but not necessarily full) rank. This relaxation allows for matrices with only $\widetilde{O}(n)$ non-zero entries, enabling a first step towards generating packed beaver triples with $\widetilde{O}(1)$ total communication per underlying triple, assuming OLE correlations. As the second (and final) step, we use the efficient $\textit{triple extraction}$ protocol of (Choudhury and Patra, Trans. Inform. Theory &#x27;17). We also implement our packed beaver triple protocol and provide experimental results. Our new protocol obtains up to 38% smaller communication and 9% reduction in runtime compared to SuperPack&#x27;s triple protocol. Additionally, by instantiating SuperPack&#x27;s offline phase with our new protocol, we obtain up to 16% communication reductions. Finally, we use our packed beaver triple protocol to instantiate the offline phase of Sharing Transformation, yielding a dishonest majority MPC protocol with $\widetilde{O}(|C|)$ total communication across both the offline and online phases.

  匹配依据：MPC: mpc (context)

  </details>

- **A Decentralized Federated Learning using Reputation**
  2024-03-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/506)
  Olive Chakraborty, Aymen Boudguiga

  <details><summary>摘要 / Abstract</summary>

  Nowadays Federated learning (FL) is established as one of the best techniques for collaborative machine learning. It allows a set of clients to train a common model without disclosing their sensitive and private dataset to a coordination server. The latter is in charge of the model aggregation. However, FL faces some problems, regarding the security of updates, integrity of computation and the availability of a server. In this paper, we combine some new ideas like clients’ reputation with techniques like secure aggregation using Homomorphic Encryption and verifiable secret sharing using Multi-Party Computation techniques to design a decentralized FL system that addresses the issues of incentives, security and availability amongst others. One of the original contributions of this work is the new leader election protocol which uses a secure shuffling and is based on a proof of reputation. Indeed, we propose to select an aggregator among the clients participating to the FL training using their reputations. That is, we estimate the reputation of each client at every FL iteration and then we select the next round aggregator from the set of clients with the best reputations. As such, we remove misbehaving clients (e.g., byzantines) from the list of clients eligible for the role of aggregation server.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **On the Security of Data Markets and Private Function Evaluation**
  2024-03-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/497)
  István Vajda

  <details><summary>摘要 / Abstract</summary>

  The income of companies working on data markets steadily grows year by year. Private function evaluation (PFE) is a valuable tool in solving corresponding security problems. The task of Controlled Private Function Evaluation and its relaxed version was introduced in [Horvath et.al., 2019]. In this article, we propose and examine several different approaches for such tasks with computational and information theoretical security against static corruption adversary. The latter level of security implies quantum-security. We also build known techniques and constructions into our solution where they fit into our tasks. The main cryptographic primitive, naturally related to the task is 1-out-of-n oblivious transfer. We use Secure Multiparty Computation techniques and in one of the constructions functional encryption primitive. The analysis of the computational complexity of the constructions shows that the considered tasks can efficiently be implemented, however it depends on the range of parameter values (e.g. size of database, size of the set of permitted function), the execution environment (e.g. concurrency) and of course on the level of security.

  匹配依据：MPC: oblivious transfer, secure multiparty computation

  </details>

- **Updatable Policy-Compliant Signatures**
  2024-03-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/491)
  Christian Badertscher, Monosij Maitra, Christian Matt, Hendrik Waldner

  <details><summary>摘要 / Abstract</summary>

  Policy-compliant signatures (PCS) are a recently introduced primitive by Badertscher et al. [TCC 2021] in which a central authority distributes secret and public keys associated with sets of attributes (e.g., nationality, affiliation with a specific department, or age) to its users. The authority also enforces a policy determining which senders can sign messages for which receivers based on a joint check of their attributes. For example, senders and receivers must have the same nationality, or only senders that are at least 18 years old can send to members of the computer science department. PCS further requires attribute-privacy – nothing about the users’ attributes is revealed from their public keys and signatures apart from whether the attributes satisfy the policy or not. The policy in a PCS scheme is fixed once and for all during the setup. Therefore, a policy update requires a redistribution of all keys. This severely limits the practicality of PCS. In this work, we introduce the notion of updatable policy-compliant signatures (UPCS) extending PCS with a mechanism to efficiently update the policy without redistributing keys to all participants. We define the notion of UPCS and provide the corresponding security definitions. We then provide a generic construction of UPCS based on digital signatures, a NIZK proof system, and a so-called secret-key two-input partially-hiding predicate encryption (2-PHPE) scheme. Unfortunately, the only known way to build the latter for general two-input predicates is using indistinguishability obfuscation. We show that the reliance on the heavy tool of 2-PHPE is inherent to build UPCS by proving that non-interactive UPCS implies 2-PHPE. To circumvent the reliance on 2-PHPE, we consider interactive UPCS, which allows the sender and receiver to interact during the message signing procedure. In this setting, we present two schemes: the first one requires only a digital signature scheme, a NIZK proof system, and secure two-party computation. This scheme works for arbitrary policies, but requires sender and receiver to engage in a two-party computation protocol for each policy update. Our second scheme additionally requires a (single-input) predicate-encryption scheme but, in turn, only requires a single interaction between sender and receiver, independent of the updates. In contrast to 2-PHPE, single-input predicate encryption for certain predicate classes is known to exist (e.g., from pairings) under more concrete and well-understood assumptions.

  匹配依据：MPC: secure two party computation, two party computation

  </details>

- **Hawk: Accurate and Fast Privacy-Preserving Machine Learning Using Secure Lookup Table Computation**
  2024-03-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.17296)
  Hamza Saleem, Amir Ziashahabi, Muhammad Naveed, Salman Avestimehr

  <details><summary>摘要 / Abstract</summary>

  Training machine learning models on data from multiple entities without direct data sharing can unlock applications otherwise hindered by business, legal, or ethical constraints. In this work, we design and implement new privacy-preserving machine learning protocols for logistic regression and neural network models. We adopt a two-server model where data owners secret-share their data between two servers that train and evaluate the model on the joint data. A significant source of inefficiency and inaccuracy in existing methods arises from using Yao&#x27;s garbled circuits to compute non-linear activation functions. We propose new methods for computing non-linear functions based on secret-shared lookup tables, offering both computational efficiency and improved accuracy. Beyond introducing leakage-free techniques, we initiate the exploration of relaxed security measures for privacy-preserving machine learning. Instead of claiming that the servers gain no knowledge during the computation, we contend that while some information is revealed about access patterns to lookup tables, it maintains epsilon-dX-privacy. Leveraging this relaxation significantly reduces the computational resources needed for training. We present new cryptographic protocols tailored to this relaxed security paradigm and define and analyze the leakage. Our evaluations show that our logistic regression protocol is up to 9x faster, and the neural network training is up to 688x faster than SecureML. Notably, our neural network achieves an accuracy of 96.6% on MNIST in 15 epochs, outperforming prior benchmarks that capped at 93.4% using the same architecture.

  匹配依据：MPC: garbled circuits

  </details>

- **CipherFormer: Efficient Transformer Private Inference with Low Round Complexity**
  2024-03-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.16860)
  Weize Wang, Yi Kuang

  <details><summary>摘要 / Abstract</summary>

  There is a growing trend to outsource the inference task of large transformer models to cloud servers. However, this poses a severe threat to users&#x27; private data as they are exposed to cloud servers after uploading. Although several works attempted to provide private inference for transformer models, their hundreds of communication rounds limit the application scenarios. Motivated by the desire to minimize round complexity, we propose CipherFormer, a novel transformer private inference scheme using homomorphic encryption and garbled circuits. We present a protocol for quickly computing homomorphic matrix multiplications. We then modify the attention mechanism and design the corresponding garbled circuits. Furthermore, we show how to use a lightweight attention mechanism and mixed-bitwidth to reduce the inference latency while maintaining accuracy. In comparison with an advanced homomorphic encryption scheme on text classification tasks, our model improves accuracy by 3% to 11% while performing private inference with a 7.7x-11.9x speedup.

  匹配依据：MPC: garbled circuits

  </details>

- **Snail: Secure Single Iteration Localization**
  2024-03-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.14916)
  James Choncholas, Pujith Kachana, André Mateus, Gregoire Phillips, Ada Gavrilovska

  <details><summary>摘要 / Abstract</summary>

  Localization is a computer vision task by which the position and orientation of a camera is determined from an image and environmental map. We propose a method for performing localization in a privacy preserving manner supporting two scenarios: first, when the image and map are held by a client who wishes to offload localization to untrusted third parties, and second, when the image and map are held separately by untrusting parties. Privacy preserving localization is necessary when the image and map are confidential, and offloading conserves on-device power and frees resources for other tasks. To accomplish this we integrate existing localization methods and secure multi-party computation (MPC), specifically garbled circuits, yielding proof-based security guarantees in contrast to existing obfuscation-based approaches which recent related work has shown vulnerable. We present two approaches to localization, a baseline data-oblivious adaptation of localization suitable for garbled circuits and our novel Single Iteration Localization. Our technique improves overall performance while maintaining confidentiality of the input image, map, and output pose at the expense of increased communication rounds but reduced computation and communication required per round. Single Iteration Localization is over two orders of magnitude faster than a straightforward application of garbled circuits to localization enabling real-world usage in the first robot to offload localization without revealing input images, environmental map, position, or orientation to offload servers.

  匹配依据：MPC: garbled circuits, secure multi party computation

  </details>

- **Secure Query Processing with Linear Complexity**
  2024-03-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.13492)
  Qiyao Luo, Yilei Wang, Wei Dong, Ke Yi

  <details><summary>摘要 / Abstract</summary>

  We present LINQ, the first join protocol with linear complexity (in both running time and communication) under the secure multi-party computation model (MPC). It can also be extended to support all free-connex queries, a large class of select-join-aggregate queries, still with linear complexity. This matches the plaintext result for the query processing problem, as free-connex queries are the largest class of queries known to be solvable in linear time in plaintext. We have then built a query processing system based on LINQ, and the experimental results show that LINQ significantly outperforms the state of the art. For example, it can finish a query on three relations with an output size of 1 million tuples in around 100s in the LAN setting, while existing protocols that support the query cannot finish in an hour. Thus LINQ brings MPC query processing closer to practicality.

  匹配依据：MPC: secure multi party computation

  </details>

- **Malicious Security for Sparse Private Histograms**
  2024-03-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/469)
  Lennart Braun, Adrià Gascón, Mariana Raykova, Phillipp Schoppmann, Karn Seth

  <details><summary>摘要 / Abstract</summary>

  We present a construction for secure computation of differentially private sparse histograms that aggregates the inputs from a large number of clients. Each client contributes a value to the aggregate at a specific index. We focus on the case where the set of possible indices is superpolynomially large. Hence, the resulting histogram will be sparse, i.e., most entries will have the value zero. Our construction relies on two non-colluding servers and provides security against malicious adversaries that may control one of the servers and any numbers of clients. It achieves communication and computation complexities linear in the input size, and achieves the optimal error $O\big(\frac{\log(1/\delta)}{\epsilon}\big)$, independent of the size of the domain of indices. We compute the communication cost of our protocol, showing its scalability. For a billion clients, the communication cost for each server is under 26 KiB per client. Our paper solves an open problem of the work of Bell et al. (CCS&#x27;22) which presented a solution for the semi-honest setting while incurring sublinear overhead in its efficiency. We formalize a proof approach for proving malicious security in settings where the output and possible additional information revealed during the execution need to provide differential privacy.

  匹配依据：MPC: secure computation

  </details>

- **Fast Secure Computations on Shared Polynomials and Applications to Private Set Operations**
  2024-03-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/470)
  Pascal Giorgi, Fabien Laguillaumie, Lucas Ottow, Damien Vergnaud

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation aims to allow a set of players to compute a given function on their secret inputs without revealing any other information than the result of the computation. In this work, we focus on the design of secure multi-party protocols for shared polynomial operations. We consider the classical model where the adversary is honest-but-curious, and where the coefficients (or any secret values) are either encrypted using an additively homomorphic encryption scheme or shared using a threshold linear secret-sharing scheme. Our protocols terminate after a constant number of rounds and minimize the number of secure multiplications. In their seminal article at PKC 2006, Mohassel and Franklin proposed constant-rounds protocols for the main operations on (shared) polynomials. In this work, we improve the fan-in multiplication of nonzero polynomials, the multi-point polynomial evaluation and the polynomial interpolation (on secret points) to reach a quasi-linear complexity (instead of quadratic in Mohassel and Franklin&#x27;s work) in the degree of shared input/output polynomials. Computing with shared polynomials is a core component of designing multi-party protocols for privacy-preserving operations on private sets, like private disjointness test or private set intersection. Using our new protocols, we are able to improve the complexity of such protocols and to design the first variant which always returns a correct result.

  匹配依据：MPC: private set intersection, secret sharing, secure multi party computation

  </details>

- **Arctic: Lightweight and Stateless Threshold Schnorr Signatures**
  2024-03-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/466)
  Chelsea Komlo, Ian Goldberg

  <details><summary>摘要 / Abstract</summary>

  Threshold Schnorr signatures are seeing increased adoption in practice, and offer practical defenses against single points of failure. However, one challenge with existing randomized threshold Schnorr signature schemes is that signers must carefully maintain secret state across signing rounds, while also ensuring that state is deleted after a signing session is completed. Failure to do so will result in a fatal key-recovery attack by re-use of nonces. While deterministic threshold Schnorr signatures that mitigate this issue exist in the literature, all prior schemes incur high complexity and performance overhead in comparison to their randomized equivalents. In this work, we seek the best of both worlds; a deterministic and stateless threshold Schnorr signature scheme that is also simple and efficient. Towards this goal, we present Arctic, a lightweight two-round threshold Schnorr signature that is deterministic, and therefore does not require participants to maintain state between signing rounds. As a building block, we formalize the notion of a Verifiable Pseudorandom Secret Sharing (VPSS) scheme, and define VPSS1, an efficient VPSS construction. VPSS1 is secure when the total number of participants is at least 2t−1 and the adversary is assumed to corrupt at most t−1; i.e., in the honest majority model. We prove that Arctic is secure under the discrete logarithm assumption in the random oracle model, similarly assuming at minimum 2t−1 number of signers and a corruption threshold of at most t−1. For moderately sized groups (i.e., when n ≤ 20), Arctic is more than an order of magnitude more efficient than prior deterministic threshold Schnorr signatures in the literature. For small groups where n ≤ 10, Arctic is three orders of magnitude more efficient.

  匹配依据：MPC: secret sharing

  </details>

- **Efficient Multi-instance Vector Commitment and Application to Post-quantum Signatures**
  2024-03-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/465)
  Dung Bui

  <details><summary>摘要 / Abstract</summary>

  The MPC-in-the-Head (MPCitH) and the VOLE-in-the-Head (VOLEitH) paradigms have recently been utilized to develop post-quantum signatures. Both rely on a mechanism that allows the signer to commit to $N$ values and then later open all-but-one. In particular, MPCitH-based signatures achieve this using a puncturable pseudorandom function (PPRF) primitive, while VOLEitH-based signatures utilize an all-but-one vector commitment scheme. A novel and efficient multi-instance PPRF, introduced by Bui et al. (Asiacrypt&#x27;24), provides a significant performance boost for MPCitH-based signatures, employing only a fixed-key block cipher to instantiate the PPRF while being provably secure in the ideal cipher model. This work presents an efficient multi-instance vector commitment derived from multi-instance PPRF. Our vector commitment scheme is secure in the multi-instance setting, when handling repetitive parallel executions. As a result, it can be directly applied to enhance the efficiency of VOLEitH-based signatures. We implemented our vector commitment scheme into FAEST (\url{faest.info}), a round one candidate in the NIST post-quantum cryptography standardization. According to our experimental implementation, we achieve $10\%-27\%$ improvement in both signing and verification times for various settings. % In particular, for 128-bit security (128S), we gain $23\%$ improvement with a reasonable trade-off of security loss. On the other hand, we adapt the VOLE-in-the-Head framework to the Multivariate Quadratic (MQ) problem, achieving a reduction in signature size. Specifically, for a 128-bit security level, our approach yields signature sizes between 3.1KB and 3.6KB with a small field size parameter.

  匹配依据：MPC: mpc (context)

  </details>

- **Minimal Ternary Linear Codes from Vectorial Functions**
  2024-03-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.11775)
  Yanjun Li, Haibin Kan, Fangfang Liu, Jie Peng, Lijing Zheng, Zepeng Zhuo

  <details><summary>摘要 / Abstract</summary>

  The study on minimal linear codes has received great attention due to their significant applications in secret sharing schemes and secure two-party computation. Until now, numerous minimal linear codes have been discovered. However, to the best of our knowledge, no infinite family of minimal ternary linear codes was found from vectorial functions. In this paper, we present a necessary and sufficient condition for a large class of ternary linear codes from vectorial functions such that those codes are minimal. Based on that, we construct several minimal ternary linear codes with three-weight from vectorial regular plateaued functions, and determine their weight distributions. Moreover, we also give a necessary and sufficient condition for a large family of ternary linear codes from vectorial functions such that the codes are minimal and violate the AB condition simultaneously. According to this characterization, we find several minimal ternary linear codes violating the AB condition. Notably, our results show that our method can be applied to solve a problem on minimal linear codes proposed by Li et al.

  匹配依据：MPC: secret sharing, secure two party computation

  </details>

- **Pencil: Private and Extensible Collaborative Learning without the Non-Colluding Assumption**
  2024-03-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.11166)
  Xuanqi Liu, Zhuotao Liu, Qi Li, Ke Xu, Mingwei Xu

  <details><summary>摘要 / Abstract</summary>

  The escalating focus on data privacy poses significant challenges for collaborative neural network training, where data ownership and model training/deployment responsibilities reside with distinct entities. Our community has made substantial contributions to addressing this challenge, proposing various approaches such as federated learning (FL) and privacy-preserving machine learning based on cryptographic constructs like homomorphic encryption (HE) and secure multiparty computation (MPC). However, FL completely overlooks model privacy, and HE has limited extensibility (confined to only one data provider). While the state-of-the-art MPC frameworks provide reasonable throughput and simultaneously ensure model/data privacy, they rely on a critical non-colluding assumption on the computing servers, and relaxing this assumption is still an open problem. In this paper, we present Pencil, the first private training framework for collaborative learning that simultaneously offers data privacy, model privacy, and extensibility to multiple data providers, without relying on the non-colluding assumption. Our fundamental design principle is to construct the n-party collaborative training protocol based on an efficient two-party protocol, and meanwhile ensuring that switching to different data providers during model training introduces no extra cost. We introduce several novel cryptographic protocols to realize this design principle and conduct a rigorous security and privacy analysis. Our comprehensive evaluations of Pencil demonstrate that (i) models trained in plaintext and models trained privately using Pencil exhibit nearly identical test accuracies; (ii) The training overhead of Pencil is greatly reduced: Pencil achieves 10 ~ 260x higher throughput and 2 orders of magnitude less communication than prior art; (iii) Pencil is resilient against both existing and adaptive (white-box) attacks.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Verifiable Information-Theoretic Function Secret Sharing**
  2024-03-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/453)
  Stanislav Kruglik, Son Hoang Dau, Han Mao Kiah, Huaxiong Wang, Liang Feng Zhang

  <details><summary>摘要 / Abstract</summary>

  A function secret sharing (FSS) (Boyle et al., Eurocrypt 2015) is a cryptographic primitive that enables additive secret sharing of functions from a given function family $\mathcal{F}$. FSS supports a wide range of cryptographic applications, including private information retrieval (PIR), anonymous messaging systems, private set intersection and more. Formally, given positive integers $r \geq 2$ and $t &lt; r$, and a class $\mathcal{F}$ of functions $f: [n] \to \mathbb{G}$ for an Abelian group $\mathbb{G}$, an $r$-party $t$-private FSS scheme for $\mathcal{F}$ allows a dealer to split each $f \in \mathcal{F}$ into $r$ function shares $f_1, \ldots, f_r$ among $r$ servers. Shares have the property that $f = f_1 + \cdots + f_r$ and functions are indistinguishable for any coalition of up to $t$ servers. FSS for point function $f_{\alpha_1,\ldots,\alpha_l,\beta_1,\ldots,\beta_l}$ for different $\alpha$ and $l&lt;t$ that evaluates to $\beta_i$ on input $\alpha_i$ for all $i\in[l]$ and to zero on all other inputs for $l=1$ are known under the name of distributed point functions (DPF). FSS for special interval functions $f^{&lt;}_{\alpha,\beta}$ that evaluate to $\beta$ on inputs lesser than $\alpha$ and to zero on all other inputs are known under the name of distributed comparison functions (DCF). Most existing FSS schemes are based on the existence of one-way functions or pseudo-random generators, and as a result, hiding of function $f$ holds only against computationally bounded adversaries. Protocols employing them as building blocks are computationally secure. Several exceptions mostly focus on DPF for four, eight or $d(t+1)$ servers for positive integer $d$, and none of them provide verifiability. In this paper, we propose DPF for $d(t+l-1)+1$ servers, where $d$ is a positive integer, offering a better key size compared to the previously proposed DPF for $d(t+1)$ servers and DCF for $dt+1$ servers, also for positive integer $d$. We introduce their verifiable extension in which any set of servers holding $t$ keys cannot persuade us to accept the wrong value of the function. This verifiability notion differs from existing verifiable FSS schemes in the sense that we verify not only the belonging of the function to class $\mathcal{F}$ but also the correctness of computation results. Our schemes provide a secret key size $O(n^{1/d}\cdot s\log(p))$ for DPF and $O(n^{1/d}\cdot s\log(p))$ for DCF, where $p^s$ is the size of group $\mathbb{G}$.

  匹配依据：MPC: private set intersection, secret sharing

  </details>

- **The 2Hash OPRF Framework and Efficient Post-Quantum Instantiations**
  2024-03-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/450)
  Ward Beullens, Lucas Dodgson, Sebastian Faller, Julia Hesse

  <details><summary>摘要 / Abstract</summary>

  An Oblivious Pseudo-Random Function (OPRF) is a two-party protocol for jointly evaluating a Pseudo-Random Function (PRF), where a user has an input x and a server has an input k. At the end of the protocol, the user learns the evaluation of the PRF using key k at the value x, while the server learns nothing about the user&#x27;s input or output. OPRFs are a prime tool for building secure authentication and key exchange from passwords, private set intersection, private information retrieval, and many other privacy-preserving systems. While classical OPRFs run as fast as a TLS Handshake, current *quantum-safe* OPRF candidates are still practically inefficient. In this paper, we propose a framework for constructing OPRFs from post-quantum multi-party computation. The framework captures a family of so-called &quot;2Hash PRFs&quot;, which sandwich a function evaluation in between two hashes. The core of our framework is a compiler that yields an OPRF from a secure evaluation of any function that is key-collision resistant and one-more unpredictable. We instantiate this compiler by providing such functions built from Legendre symbols, and from AES encryption. We then give a case-tailored protocol for securely evaluating our Legendre-based function, built from oblivious transfer (OT) and zero-knowledge proofs (ZKP). Instantiated with lattice-based OT and ZKPs, we obtain a quantum-safe OPRF that completes in 0.57 seconds, with less than 1MB of communication.

  匹配依据：MPC: multi party computation, oblivious transfer, private set intersection, secure evaluation

  </details>

- **Secure Distributed Storage: Optimal Trade-Off Between Storage Rate and Privacy Leakage**
  2024-03-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.10676)
  Remi A. Chou, Joerg Kliewer

  <details><summary>摘要 / Abstract</summary>

  Consider the problem of storing data in a distributed manner over $T$ servers. Specifically, the data needs to (i) be recoverable from any $τ$ servers, and (ii) remain private from any $z$ colluding servers, where privacy is quantified in terms of mutual information between the data and all the information available at any $z$ colluding servers. For this model, our main results are (i) the fundamental trade-off between storage size and the level of desired privacy, and (ii) the optimal amount of local randomness necessary at the encoder. As a byproduct, our results provide an optimal lower bound on the individual share size of ramp secret sharing schemes under a more general leakage symmetry condition than the ones previously considered in the literature.

  匹配依据：MPC: secret sharing

  </details>

- **Device-independent quantum secret sharing with noise preprocessing and postselection**
  2024-03-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.10137)
  Qi Zhang, Wei Zhong, Ming-Ming Du, Shu-Ting Shen, Xi-Yun Li, An-Lei Zhang, Lan Zhou, Yu-Bo Sheng

  <details><summary>摘要 / Abstract</summary>

  Device-independent (DI) quantum secret sharing (QSS) can relax the security assumptions about the devices&#x27; internal workings and provide QSS the highest level of security in theory. The original DI QSS protocol proved its correctness and completeness under a causal independence assumption regarding measurement devices. However, there has been a lack of DI QSS&#x27;s performance characterization in practical communication situations, which impedes its experimental demonstration and application in the future. Here, we propose a three-partite DI QSS protocol with noise preprocessing and postselection strategies and develop the numerical methods to implement its performance characterization in practical communication situations. The adoption of the noise preprocessing and postselection can reduce DI QSS&#x27;s global detection efficiency threshold from 96.32% to 94.30% and increase the noise threshold from 7.148% to 8.072%. Our DI QSS protocol has two advantages. First, it is a DI QSS protocol with performance characterization in practical communication situations. Second, the adoption of noise preprocessing and postselection can effectively relax its experimental requirement and enhance the noise resistance. Our DI QSS protocol has potential for future experimental demonstration and application.

  匹配依据：MPC: secret sharing

  </details>

- **RANDAO-based RNG: Last Revealer Attacks in Ethereum 2.0 Randomness and a Potential Solution**
  2024-03-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.09541)
  Do Hai Son, Tran Thi Thuy Quynh, Le Quang Minh

  <details><summary>摘要 / Abstract</summary>

  Ethereum 2.0 is a major upgrade to improve its scalability, throughput, and security. In this version, RANDAO is the scheme to randomly select the users who propose, confirm blocks, and get rewards. However, a vulnerability, referred to as the `Last Revealer Attack&#x27; (LRA), compromises the randomness of this scheme by introducing bias to the Random Number Generator (RNG) process. This vulnerability is first clarified again in this study. After that, we propose a Shamir&#x27;s Secret Sharing (SSS)-based RANDAO scheme to mitigate the LRA. Through our analysis, the proposed method can prevent the LRA under favorable network conditions.

  匹配依据：MPC: secret sharing

  </details>

- **Perfect Asynchronous MPC with Linear Communication Overhead**
  2024-03-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/432)
  Ittai Abraham, Gilad Asharov, Shravani Patil, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  We study secure multiparty computation in the asynchronous setting with perfect security and optimal resilience (less than one-fourth of the participants are malicious). It has been shown that every function can be computed in this model [Ben-OR, Canetti, and Goldreich, STOC&#x27;1993]. Despite 30 years of research, all protocols in the asynchronous setting require $\Omega(n^2C)$ communication complexity for computing a circuit with $C$ multiplication gates. In contrast, for nearly 15 years, in the synchronous setting, it has been known how to achieve $\mathcal{O}(nC)$ communication complexity (Beerliova and Hirt; TCC 2008). The techniques for achieving this result in the synchronous setting are not known to be sufficient for obtaining an analogous result in the asynchronous setting. We close this gap between synchronous and asynchronous secure computation and show the first asynchronous protocol with $\mathcal{O}(nC)$ communication complexity for a circuit with $C$ multiplication gates. Linear overhead forms a natural barrier for general secret-sharing-based MPC protocols. Our main technical contribution is an asynchronous weak binding secret sharing that achieves rate-1 communication (i.e., $\mathcal{O}(1)$-overhead per secret). To achieve this goal, we develop new techniques for the asynchronous setting, including the use of trivariate polynomials (as opposed to bivariate polynomials).

  匹配依据：MPC: secret sharing, secure computation, secure multiparty computation

  </details>

- **Improved Trade-offs Between Amortization and Download Bandwidth for Linear HSS**
  2024-03-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.08719)
  Keller Blackwell, Mary Wootters

  <details><summary>摘要 / Abstract</summary>

  A Homomorphic Secret Sharing (HSS) scheme is a secret-sharing scheme that shares a secret $x$ among $s$ servers, and additionally allows an output client to reconstruct some function $f(x)$ using information that can be locally computed by each server. A key parameter in HSS schemes is download rate, which quantifies how much information the output client needs to download from the servers. Often, download rate is improved by amortizing over $\ell$ instances of the problem, making $\ell$ also a key parameter of interest. Recent work (Fosli, Ishai, Kolobov, and Wootters 2022) established a limit on the download rate of linear HSS schemes for computing low-degree polynomials and constructed schemes that achieve this optimal download rate; their schemes required amortization over $\ell = Ω(s \log(s))$ instances of the problem. Subsequent work (Blackwell and Wootters, 2023) completely characterized linear HSS schemes that achieve optimal download rate in terms of a coding-theoretic notion termed optimal labelweight codes. A consequence of this characterization was that $\ell = Ω(s \log(s))$ is in fact necessary to achieve optimal download rate. In this paper, we characterize all linear HSS schemes, showing that schemes of any download rate are equivalent to a generalization of optimal labelweight codes. This equivalence is constructive and provides a way to obtain an explicit linear HSS scheme from any linear code. Using this characterization, we present explicit linear HSS schemes with slightly sub-optimal rate but with much improved amortization $\ell = O(s)$. Our constructions are based on algebraic geometry codes (specifically Hermitian codes and Goppa codes).

  匹配依据：MPC: secret sharing

  </details>

- **xMLP: Revolutionizing Private Inference with Exclusive Square Activation**
  2024-03-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.08024)
  Jiajie Li, Jinjun Xiong

  <details><summary>摘要 / Abstract</summary>

  Private Inference (PI) enables deep neural networks (DNNs) to work on private data without leaking sensitive information by exploiting cryptographic primitives such as multi-party computation (MPC) and homomorphic encryption (HE). However, the use of non-linear activations such as ReLU in DNNs can lead to impractically high PI latency in existing PI systems, as ReLU requires the use of costly MPC computations, such as Garbled Circuits. Since square activations can be processed by Beaver&#x27;s triples hundreds of times faster compared to ReLU, they are more friendly to PI tasks, but using them leads to a notable drop in model accuracy. This paper starts by exploring the reason for such an accuracy drop after using square activations, and concludes that this is due to an &quot;information compounding&quot; effect. Leveraging this insight, we propose xMLP, a novel DNN architecture that uses square activations exclusively while maintaining parity in both accuracy and efficiency with ReLU-based DNNs. Our experiments on CIFAR-100 and ImageNet show that xMLP models consistently achieve better performance than ResNet models with fewer activation layers and parameters while maintaining consistent performance with its ReLU-based variants. Remarkably, when compared to state-of-the-art PI Models, xMLP demonstrates superior performance, achieving a 0.58% increase in accuracy with 7x faster PI speed. Moreover, it delivers a significant accuracy improvement of 4.96% while maintaining the same PI latency. When offloading PI to the GPU, xMLP is up to 700x faster than the previous state-of-the-art PI model with comparable accuracy.

  匹配依据：MPC: garbled circuits, multi party computation

  </details>

- **FOLEAGE: $\\mathbb{F}\_4$OLE-Based Multi-Party Computation for Boolean Circuits**
  2024-03-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/429)
  Maxime Bombar, Dung Bui, Geoffroy Couteau, Alain Couvreur, Clément Ducros, Sacha Servan-Schreiber

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-party Computation (MPC) allows two or more parties to compute any public function over their privately-held inputs, without revealing any information beyond the result of the computation. Modern protocols for MPC generate a large amount of input-independent preprocessing material called multiplication triples, in an offline phase. This preprocessing can later be used by the parties to efficiently instantiate an input-dependent online phase computing the function. To date, the state-of-the-art secure multi-party computation protocols in the preprocessing model are tailored to secure computation of arithmetic circuits over large fields and require little communication in the preprocessing phase, typically O(N · m) to generate m triples among N parties. In contrast, when it comes to computing preprocessing for computations that are naturally represented as Boolean circuits, the state-of-the-art techniques have not evolved since the 1980s, and in particular, require every pair of parties to execute a large number of oblivious transfers before interacting to convert them to N-party triples, which induces an Ω(N^2 · m) communication overhead. In this paper, we introduce FOLEAGE, which addresses this gap by introducing an efficient preprocessing protocol tailored to Boolean circuits. FOLEAGE exhibits excellent performance: It generates m multiplication triples over F2 using only N · m + O(N^2 · log m) bits of communication for N-parties, and can concretely produce over 12 million triples per second in the 2-party setting on one core of a commodity machine. Our result builds upon an efficient Pseudorandom Correlation Generator (PCG) for multiplication triples over the field F4. Roughly speaking, a PCG enables parties to stretch a short seed into a large number of pseudorandom correlations non-interactively, which greatly improves the efficiency of the offline phase in MPC protocols. Our construction significantly outperforms the state-of-the-art, which we demonstrate via a prototype implementation. This is achieved by introducing a number of protocol-level, algorithmic-level, and implementation-level optimizations on the recent PCG construction of Bombar et al. (Crypto 2023) from the Quasi-Abelian Syndrome Decoding assumption.

  匹配依据：MPC: multi party computation, secure computation, secure multi party computation

  </details>

- **Fluent: Round-efficient Secure Aggregation for Private Federated Learning**
  2024-03-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.06143)
  Xincheng Li, Jianting Ning, Geong Sen Poh, Leo Yu Zhang, Xinchun Yin, Tianwei Zhang

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) facilitates collaborative training of machine learning models among a large number of clients while safeguarding the privacy of their local datasets. However, FL remains susceptible to vulnerabilities such as privacy inference and inversion attacks. Single-server secure aggregation schemes were proposed to address these threats. Nonetheless, they encounter practical constraints due to their round and communication complexities. This work introduces Fluent, a round and communication-efficient secure aggregation scheme for private FL. Fluent has several improvements compared to state-of-the-art solutions like Bell et al. (CCS 2020) and Ma et al. (SP 2023): (1) it eliminates frequent handshakes and secret sharing operations by efficiently reusing the shares across multiple training iterations without leaking any private information; (2) it accomplishes both the consistency check and gradient unmasking in one logical step, thereby reducing another round of communication. With these innovations, Fluent achieves the fewest communication rounds (i.e., two in the collection phase) in the malicious server setting, in contrast to at least three rounds in existing schemes. This significantly minimizes the latency for geographically distributed clients; (3) Fluent also introduces Fluent-Dynamic with a participant selection algorithm and an alternative secret sharing scheme. This can facilitate dynamic client joining and enhance the system flexibility and scalability. We implemented Fluent and compared it with existing solutions. Experimental results show that Fluent improves the computational cost by at least 75% and communication overhead by at least 25% for normal clients. Fluent also reduces the communication overhead for the server at the expense of a marginal increase in computational cost.

  匹配依据：MPC: secret sharing

  </details>

- **DT-SIM: Property-Based Testing for MPC Security**
  2024-03-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.04991)
  Mako Bates, Joseph P. Near

  <details><summary>摘要 / Abstract</summary>

  Formal methods for guaranteeing that a protocol satisfies a cryptographic security definition have advanced substantially, but such methods are still labor intensive and the need remains for an automated tool that can positively identify an insecure protocol. In this work, we demonstrate that property-based testing, &quot;run it a bunch of times and see if it breaks&quot;, is effective for detecting security bugs in secure protocols. We specifically target Secure Multi-Party Computation (MPC), because formal methods targeting this security definition for bit-model implementations are particularly difficult. Using results from the literature for Probabilistic Programming Languages and statistical inference, we devise a test that can detect various flaws in a bit-level implementation of an MPC protocol. The test is grey-box; it requires only transcripts of randomness consumed by the protocol and of the inputs, outputs, and messages. It successfully detects several different mistakes and biases introduced into two different implementations of the classic GMW protocol. Applied to hundreds of randomly generated protocols, it identifies nearly all of them as insecure. We also include an analysis of the parameters of the test, and discussion of what makes detection of MPC (in)security difficult.

  匹配依据：MPC: secure multi party computation

  </details>

- **Column-wise Garbling, and How to Go Beyond the Linear Model**
  2024-03-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/415)
  Lei Fan, Zhenghao Lu, Hong-Sheng Zhou

  <details><summary>摘要 / Abstract</summary>

  In the linear garbling model introduced by Zahur, Rosulek, and Evans (Eurocrypt 2015), garbling an AND gate requires at least \(2\kappa\) bits of ciphertext, where $\kappa$ is the security parameter. Though subsequent works, including those by Rosulek and Roy (Crypto 2021) and Acharya et al. (ACNS 2023), have advanced beyond these linear constraints, a more comprehensive design framework is yet to be developed. Our work offers a novel, unified, and arguably simple perspective on garbled circuits. We introduce a hierarchy of models that captures all existing practical garbling schemes. By determining the lower bounds for these models, we elucidate the capabilities and limits of each. Notably, our findings suggest that simply integrating a nonlinear processing function or probabilistic considerations does not break the \(2\kappa\) lower bound by Zahur, Rosulek, and Evans. However, by incorporating column correlations, the bound can be reduced to \((1+1/w)\kappa\), where \(w\ge 1\). Additionally, we demonstrate that a straightforward extension of Rosulek and Roy&#x27;s technique (Crypto 2021) does not yield improved results. We also present a methodology for crafting new models and for exploring further extensions of both the new and the existing models. Our new models set the course for future designs. We introduce three innovative garbling schemes based on a common principle called ``majority voting.&#x27;&#x27; The third construction performs on par with the state-of-the-art.

  匹配依据：MPC: garbled circuits, garbling schemes

  </details>

- **Wildest Dreams: Reproducible Research in Privacy-preserving Neural Network Training**
  2024-03-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.03592)
  Tanveer Khan, Mindaugas Budzys, Khoa Nguyen, Antonis Michalas

  <details><summary>摘要 / Abstract</summary>

  Machine Learning (ML), addresses a multitude of complex issues in multiple disciplines, including social sciences, finance, and medical research. ML models require substantial computing power and are only as powerful as the data utilized. Due to high computational cost of ML methods, data scientists frequently use Machine Learning-as-a-Service (MLaaS) to outsource computation to external servers. However, when working with private information, like financial data or health records, outsourcing the computation might result in privacy issues. Recent advances in Privacy-Preserving Techniques (PPTs) have enabled ML training and inference over protected data through the use of Privacy-Preserving Machine Learning (PPML). However, these techniques are still at a preliminary stage and their application in real-world situations is demanding. In order to comprehend discrepancy between theoretical research suggestions and actual applications, this work examines the past and present of PPML, focusing on Homomorphic Encryption (HE) and Secure Multi-party Computation (SMPC) applied to ML. This work primarily focuses on the ML model&#x27;s training phase, where maintaining user data privacy is of utmost importance. We provide a solid theoretical background that eases the understanding of current approaches and their limitations. In addition, we present a SoK of the most recent PPML frameworks for model training and provide a comprehensive comparison in terms of the unique properties and performances on standard benchmarks. Also, we reproduce the results for some of the papers and examine at what level existing works in the field provide support for open science. We believe our work serves as a valuable contribution by raising awareness about the current gap between theoretical advancements and real-world applications in PPML, specifically regarding open-source availability, reproducibility, and usability.

  匹配依据：MPC: secure multi party computation

  </details>

- **Efficient Unbalanced Quorum PSI from Homomorphic Encryption**
  2024-03-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/402)
  Xinpeng Yang, Liang Cai, Yinghao Wang, Yinghao Wang, Lu Sun, Jingwei Hu

  <details><summary>摘要 / Abstract</summary>

  Multiparty private set intersection (mPSI) protocol is capable of finding the intersection of multiple sets securely without revealing any other information. However, its limitation lies in processing only those elements present in every participant&#x27;s set, which proves inadequate in scenarios where certain elements are common to several, but not all, sets. In this paper, we introduce an innovative variant of the mPSI protocol named unbalanced quorum PSI to fill in the gaps of the mPSI protocol. Unlike the previous quorum-PSI proposals which detect elements present in at least $k$ out of $n$ equal sets, our protocol is particularly tailored for unbalanced cases where the size of the receiver&#x27;s set is much smaller than the size of the senders&#x27; sets. Our work achieves logarithmic communication complexity in the semi-honest setting, significantly surpassing previous work in efficiency. The benchmarks show that it takes 22.7 seconds in WAN and 14.7 seconds in LAN for online computation, and only 87.8 MB of total communication to intersect 5535 elements across 15 sets, each containing $2^{24}$ elements. Compared to prior work, this is roughly an 87$\times$ reduction in communication and a 31$\times$ reduction in online time. Our protocols can be easily extended to the larger set with $2^{28}$ elements which is nearly impractical for prior work.

  匹配依据：MPC: private set intersection

  </details>

- **Exponent-VRFs and Their Applications**
  2024-03-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/397)
  Dan Boneh, Iftach Haitner, Yehuda Lindell, Gil Segev

  <details><summary>摘要 / Abstract</summary>

  Verifiable random functions (VRFs) are pseudorandom functions where the function owner can prove that a generated output is correct relative to a committed key. In this paper we introduce the notion of an exponent-VRF (eVRF): a VRF that does not provide its output $y$ explicitly, but instead provides $Y = y \cdot G$, where $G$ is a generator of some finite cyclic group (or $Y=g^y$ in multiplicative notation). We construct eVRFs from the Paillier encryption scheme and from DDH, both in the random-oracle model. We then show that an eVRF is a powerful tool that has many important applications in threshold cryptography. In particular, we construct (1) a one-round fully simulatable distributed key-generation protocol (after a single two-round initialization phase), (2) a two-round fully simulatable signing protocol for multiparty Schnorr with a deterministic variant, (3) a two-party ECDSA protocol that has a deterministic variant, (4) a threshold Schnorr signing protocol where the parties can later prove that they signed without being able to frame another group, and (5) an MPC-friendly and verifiable HD-derivation. All these applications are derived from this single new eVRF abstraction, and the resulting protocols are concretely efficient.

  匹配依据：MPC: mpc (context)

  </details>

- **On the Feasibility of Sliced Garbling**
  2024-03-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/389)
  Tomer Ashur, Carmit Hazay, Rahul Satish

  <details><summary>摘要 / Abstract</summary>

  Garbling schemes are one of the most fundamental objects in cryptography and have been studied extensively due to their broad applicability. The state-of-the-art is a construction in which XOR gates are free and AND gates require $3\kappa/2+\mathcal{O}(1)$ bits per gate, due to Rosulek and Roy (CRYPTO&#x27;21). An important technique in their garbling is slicing, which partitions the labels into two equal-length slices. In this paper, we explore the feasibility of the slicing technique for garbling schemes beyond the results introduced by Rosulek and Roy, demonstrating both its potential and its limitations. In particular, we extend this technique to demonstrate the garbling of certain higher fan-in gadgets, and then use this to show that it is possible to garble 2-input AND gates at a cost of $4\kappa/3 +\mathcal{O}(1)$ bits. We then give a separation result showing that sliced garbling cannot be used to garble higher fan-in gadgets of degree $\geq 3$ when restricted to making queries that are linear functions of the input labels to the random oracle. We further demonstrate the usefulness of our techniques in the context of oblivious garbling, a newly introduced concept for capturing circuit hiding from the garbler. The complexity of our construction is superior to that of universal circuits, and grows linearly with circuit size.

  匹配依据：MPC: garbling schemes

  </details>

- **OPAF: Optimized Secure Two-Party Computation Protocols for Nonlinear Activation Functions in Recurrent Neural Network**
  2024-03-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.00239)
  Qian Feng, Zhihua Xia, Zhifeng Xu, Jiasi Weng, Jian Weng

  <details><summary>摘要 / Abstract</summary>

  Deep neural network (DNN) typically involves convolutions, pooling, and activation function. Due to the growing concern about privacy, privacy-preserving DNN becomes a hot research topic. Generally, the convolution and pooling operations can be supported by additive homomorphic and secure comparison, but the secure implementation of activation functions is not so straightforward for the requirements of accuracy and efficiency, especially for the non-linear ones such as exponential, sigmoid, and tanh functions. This paper pays a special attention to the implementation of such non-linear functions in semi-honest model with two-party settings, for which SIRNN is the current state-of-the-art. Different from previous works, we proposed improved implementations for these functions by using their intrinsic features as well as worthy tiny tricks. At first, we propose a novel and efficient protocol for exponential function by using a divide-and-conquer strategy with most of the computations executed locally. Exponential protocol is widely used in machine learning tasks such as Poisson regression, and is also a key component of sigmoid and tanh functions. Next, we take advantage of the symmetry of sigmoid and Tanh, and fine-tune the inputs to reduce the 2PC building blocks, which helps to save overhead and improve performance. As a result, we implement these functions with fewer fundamental building blocks. The comprehensive evaluations show that our protocols achieve state-of-the-art precision while reducing run-time by approximately 57%, 44%, and 42% for exponential (with only negative inputs), sigmoid, and Tanh functions, respectively.

  匹配依据：MPC: secure two party computation

  </details>

- **Malicious Security for SCALES: Outsourced Computation with Ephemeral Servers**
  2024-03-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/383)
  Anasuya Acharya, Carmit Hazay, Vladimir Kolesnikov, Manoj Prabhakaran

  <details><summary>摘要 / Abstract</summary>

  SCALES (Small Clients And Larger Ephemeral Servers) model is a recently proposed model for MPC (Acharya et al., TCC 2022). While the SCALES model offers several attractive features for practical large-scale MPC, the result of Acharya et al. only offered semi-honest secure protocols in this model. We present a new efficient SCALES protocol secure against malicious adversaries, for general Boolean circuits. We start with the base construction of Acharya et al. and design and use a suite of carefully defined building blocks that may be of independent interest. The resulting protocol is UC-secure without honest majority, with a CRS and bulletin-board as setups, and allows publicly identifying deviations from correct execution.

  匹配依据：MPC: mpc (context)

  </details>

- **SPriFed-OMP: A Differentially Private Federated Learning Algorithm for Sparse Basis Recovery**
  2024-02-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.19016)
  Ajinkya Kiran Mulay, Xiaojun Lin

  <details><summary>摘要 / Abstract</summary>

  Sparse basis recovery is a classical and important statistical learning problem when the number of model dimensions $p$ is much larger than the number of samples $n$. However, there has been little work that studies sparse basis recovery in the Federated Learning (FL) setting, where the client data&#x27;s differential privacy (DP) must also be simultaneously protected. In particular, the performance guarantees of existing DP-FL algorithms (such as DP-SGD) will degrade significantly when $p \gg n$, and thus, they will fail to learn the true underlying sparse model accurately. In this work, we develop a new differentially private sparse basis recovery algorithm for the FL setting, called SPriFed-OMP. SPriFed-OMP converts OMP (Orthogonal Matching Pursuit) to the FL setting. Further, it combines SMPC (secure multi-party computation) and DP to ensure that only a small amount of noise needs to be added in order to achieve differential privacy. As a result, SPriFed-OMP can efficiently recover the true sparse basis for a linear model with only $n = O(\sqrt{p})$ samples. We further present an enhanced version of our approach, SPriFed-OMP-GRAD based on gradient privatization, that improves the performance of SPriFed-OMP. Our theoretical analysis and empirical results demonstrate that both SPriFed-OMP and SPriFed-OMP-GRAD terminate in a small number of steps, and they significantly outperform the previous state-of-the-art DP-FL solutions in terms of the accuracy-privacy trade-off.

  匹配依据：MPC: secure multi party computation

  </details>

- **PrivatEyes: Appearance-based Gaze Estimation Using Federated Secure Multi-Party Computation**
  2024-02-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.18970)
  Mayar Elfares, Pascal Reisert, Zhiming Hu, Wenwu Tang, Ralf Küsters, Andreas Bulling

  <details><summary>摘要 / Abstract</summary>

  Latest gaze estimation methods require large-scale training data but their collection and exchange pose significant privacy risks. We propose PrivatEyes - the first privacy-enhancing training approach for appearance-based gaze estimation based on federated learning (FL) and secure multi-party computation (MPC). PrivatEyes enables training gaze estimators on multiple local datasets across different users and server-based secure aggregation of the individual estimators&#x27; updates. PrivatEyes guarantees that individual gaze data remains private even if a majority of the aggregating servers is malicious. We also introduce a new data leakage attack DualView that shows that PrivatEyes limits the leakage of private training data more effectively than previous approaches. Evaluations on the MPIIGaze, MPIIFaceGaze, GazeCapture, and NVGaze datasets further show that the improved privacy does not lead to a lower gaze estimation accuracy or substantially higher computational costs - both of which are on par with its non-secure counterparts.

  匹配依据：MPC: secure multi party computation

  </details>

- **Perfect (Parallel) Broadcast in Constant Expected Rounds via Statistical VSS**
  2024-02-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/376)
  Gilad Asharov, Anirudh Chandramouli

  <details><summary>摘要 / Abstract</summary>

  We study broadcast protocols in the information-theoretic model under optimal conditions, where the number of corruptions $t$ is at most one-third of the parties, $n$. While worst-case $\Omega(n)$ round broadcast protocols are known to be impossible to achieve, protocols with an expected constant number of rounds have been demonstrated since the seminal work of Feldman and Micali [STOC&#x27;88]. Communication complexity for such protocols has gradually improved over the years, reaching $O(nL)$ plus expected $O(n^4\log n)$ for broadcasting a message of size $L$ bits. This paper presents a perfectly secure broadcast protocol with expected constant rounds and communication complexity of $O(nL)$ plus expected $O(n^3 \log^2n)$ bits. In addition, we consider the problem of parallel broadcast, where $n$ senders, each wish to broadcast a message of size $L$. We show a parallel broadcast protocol with expected constant rounds and communication complexity of $O(n^2L)$ plus expected $O(n^3 \log^2n)$ bits. Our protocol is optimal (up to expectation) for messages of length $L \in \Omega(n \log^2 n)$. Our main contribution is a framework for obtaining perfectly secure broadcast with an expected constant number of rounds from a statistically secure verifiable secret sharing. Moreover, we provide a new statistically secure verifiable secret sharing where the broadcast cost per participant is reduced from $O(n \log n)$ bits to only $O({\sf poly} \log n)$ bits. All our protocols are adaptively secure.

  匹配依据：MPC: secret sharing

  </details>

- **Efficient and Generic Methods to Achieve Active Security in Private Information Retrieval and More Advanced Database Search**
  2024-02-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/375)
  Reo Eriguchi, Kaoru Kurosawa, Koji Nuida

  <details><summary>摘要 / Abstract</summary>

  Motivated by secure database search, we present secure computation protocols for a function $f$ in the client-servers setting, where a client can obtain $f(x)$ on a private input $x$ by communicating with multiple servers each holding $f$. Specifically, we propose generic compilers from passively secure protocols, which only keep security against servers following the protocols, to actively secure protocols, which guarantee privacy and correctness even against malicious servers. Our compilers are applied to protocols computing any class of functions, and are efficient in that the overheads in communication and computational complexity are only polynomial in the number of servers, independent of the complexity of functions. We then apply our compilers to obtain concrete actively secure protocols for various functions including private information retrieval (PIR), bounded-degree multivariate polynomials and constant-depth circuits. For example, our actively secure PIR protocols achieve exponentially better computational complexity in the number of servers than the currently best-known protocols. Furthermore, our protocols for polynomials and constant-depth circuits reduce the required number of servers compared to the previous actively secure protocols. In particular, our protocol instantiated from the sparse Learning Parity with Noise (LPN) assumption is the first actively secure protocol for multivariate polynomials which has the minimum number of servers, without assuming fully homomorphic encryption.

  匹配依据：MPC: secure computation

  </details>

- **PureLottery: Fair and Bias-Resistant Leader Election with a Novel Single-Elimination Tournament Algorithm**
  2024-02-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.17459)
  Jonas Ballweg

  <details><summary>摘要 / Abstract</summary>

  Leader Election (LE) is crucial in distributed systems and blockchain technology, ensuring one participant acts as the leader. Traditional LE methods often depend on distributed random number generation (RNG), facing issues like vulnerability to manipulation, lack of fairness, and the need for complex procedures such as verifiable delay functions (VDFs) and publicly-verifiable secret sharing (PVSS). This Bachelor&#x27;s thesis presents a novel approach to randomized LE, leveraging a game-theoretic assumption that participants, aiming to be chosen as leaders, will naturally avoid actions that diminish their chances. This perspective simplifies LE by eliminating the need for decentralized RNG. Introducing PureLottery, inspired by single-elimination sports tournaments, this method offers a fair, bias-resistant, and efficient LE solution for blockchain environments. It operates on the principle of two participants competing in each match, rendering collusion efforts useless. PureLottery stands out for its low computational and communication complexity, suitable for smart contract implementation. It provides strong game-theoretic incentives for honesty and is robust against adversaries, ensuring no increase in election chances through dishonesty. The protocol guarantees that each honest player has at least a 1/n chance of winning, irrespective of adversary manipulation among the other n-1 participants. PureLottery can also address related problems like participant ranking, electing multiple leaders, and leader aversion, showcasing its versatility across various applications, including lotteries and blockchain protocols. An open-source implementation is made available for public use.

  匹配依据：MPC: secret sharing

  </details>

- **Optimal Communication Unbalanced Private Set Union**
  2024-02-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.16393)
  Jean-Guillaume Dumas, Alexis Galan, Bruno Grenet, Aude Maignan, Daniel S. Roche

  <details><summary>摘要 / Abstract</summary>

  We present new two-party protocols for the Unbalanced Private Set Union (UPSU) problem. Here, the Sender holds a set of data points, and the Receiver holds another (possibly much larger) set, and they would like for the Receiver to learn the union of the two sets and nothing else. Furthermore, the Sender&#x27;s computational cost, along with the communication complexity, should be smaller when the Sender has a smaller set. While the UPSU problem has numerous applications and has seen considerable recent attention in the literature, our protocols are the first where the Sender&#x27;s computational cost and communication volume are linear in the size of the Sender&#x27;s set only, and do not depend on the size of the Receiver&#x27;s set. Our constructions combine linearly homomorphic encryption (LHE) with fully homomorphic encryption (FHE). The first construction uses multi-point polynomial evaluation (MEv) on FHE, and achieves optimal linear cost for the Sender, but has higher quadratic computational cost for the Receiver. In the second construction we explore another trade-off: the Receiver computes fast polynomial Euclidean remainder in FHE while the Sender computes a fast MEv, in LHE only. This reduces the Receiver&#x27;s cost to quasi-linear, with a modest increase in the computational cost for the Sender. Preliminary experimental results using HElib indicate that, for example, a Sender holding 1000 elements can complete our first protocol using less than 2s of computation time and less than 10MB of communication volume, independently of the Receiver&#x27;s set size.

  匹配依据：MPC: private set union

  </details>

- **Haven++: Batched and Packed Dual-Threshold Asynchronous Complete Secret Sharing with Applications**
  2024-02-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/326)
  Nicolas Alhaddad, Mayank Varia, Ziling Yang

  <details><summary>摘要 / Abstract</summary>

  Asynchronous complete secret sharing (ACSS) is a foundational primitive in the design of distributed algorithms and cryptosystems that require confidentiality. ACSS permits a dealer to distribute a secret to a collection of $n$ servers so that everyone holds shares of a polynomial containing the dealer&#x27;s secret. This work contributes a new ACSS protocol, called Haven++, that uses packing and batching to make asymptotic and concrete advances in the design and application of ACSS for large secrets. Haven++ allows the dealer to pack multiple secrets in a single sharing phase, and to reconstruct either one or all of them later. For even larger secrets, we contribute a batching technique to amortize the cost of proof generation and verification across multiple invocations of our protocol. The result is an asymptotic improvement in the worst-case amortized communication and computation complexity, both for ACSS itself and for its application to asynchronous distributed key generation. Our ADKG based on Haven++ achieves, for the first time, an optimal worst case amortized communication complexity of $O(\kappa n)$ without a trusted setup. To show the practicality of Haven++, we implement it and find that it outperforms the work of Yurek et al.\ (NDSS 2022) by more than an order of magnitude when there are malicious, faulty parties.

  匹配依据：MPC: secret sharing

  </details>

- **From Random Probing to Noisy Leakages Without Field-Size Dependence**
  2024-02-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/339)
  Gianluca Brian, Stefan Dziembowski, Sebastian Faust

  <details><summary>摘要 / Abstract</summary>

  Side channel attacks are devastating attacks targeting cryptographic implementations. To protect against these attacks, various countermeasures have been proposed -- in particular, the so-called masking scheme. Masking schemes work by hiding sensitive information via secret sharing all intermediate values that occur during the evaluation of a cryptographic implementation. Over the last decade, there has been broad interest in designing and formally analyzing such schemes. The random probing model considers leakage where the value on each wire leaks with some probability $\epsilon$. This model is important as it implies security in the noisy leakage model via a reduction by Duc et al. (Eurocrypt 2014). Noisy leakages are considered the &quot;gold-standard&quot; for analyzing masking schemes as they accurately model many real-world physical leakages. Unfortunately, the reduction of Duc et al. is non-tight, and in particular requires that the amount of noise increases by a factor of $|\mathbb{F}|$ for circuits that operate over $\mathbb{F}$ (where $\mathbb{F}$ is a finite field). In this work, we give a generic transformation from random probing to average probing, which avoids this loss of $|\mathbb{F}|$. Since the average probing is identical to the noisy leakage model (Eurocrypt 2014), this yields for the first time a security analysis of masked circuits where the noise parameter $\delta$ in the noisy leakage model is independent of $|\mathbb{F}|$. The latter is particularly important for cryptographic schemes operating over large fields, e.g., the AES or the recently standardized post-quantum schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Card-Based Overwriting Protocol for Equality Function and Applications**
  2024-02-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.16290)
  Suthee Ruangwises, Tomoki Ono, Yoshiki Abe, Kyosuke Hatsugai, Mitsugu Iwamoto

  <details><summary>摘要 / Abstract</summary>

  Research in the area of secure multi-party computation with an unconventional method of using a physical deck of playing cards began in 1989 when den Boer proposed a protocol to compute the logical AND function using five cards. Since then, the area has gained interest from many researchers and several card-based protocols to compute various functions have been developed. In this paper, we propose a card-based protocol called the overwriting protocol that can securely compute the $k$-candidate $n$-variable equality function $f: \{0,1,\ldots ,k-1\}^n \rightarrow \{0,1\}$. We also apply the technique used in this protocol to compute other similar functions.

  匹配依据：MPC: secure multi party computation

  </details>

- **Protocols for Quantum Weak Coin Flipping**
  2024-02-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.15855)
  Atul Singh Arora, Jérémie Roland, Chrysoula Vlachou, Stephan Weis

  <details><summary>摘要 / Abstract</summary>

  Weak coin flipping is an important cryptographic primitive$\unicode{x2013}$it is the strongest known secure two-party computation primitive that classically becomes secure only under certain assumptions (e.g. computational hardness), while quantumly there exist protocols that achieve arbitrarily close to perfect security. This breakthrough result was established by Mochon in 2007 [arXiv:0711.4114]. However, his proof relied on the existence of certain unitary operators which was established by a non-constructive argument. Consequently, explicit protocols have remained elusive. In this work, we give exact constructions of related unitary operators. These, together with a new formalism, yield a family of protocols approaching perfect security thereby also simplifying Mochon&#x27;s proof of existence. We illustrate the construction of explicit weak coin flipping protocols by considering concrete examples (from the aforementioned family of protocols) that are more secure than all previously known protocols.

  匹配依据：MPC: secure two party computation

  </details>

- **Holding Secrets Accountable: Auditing Privacy-Preserving Machine Learning**
  2024-02-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.15780)
  Hidde Lycklama, Alexander Viand, Nicolas Küchler, Christian Knabenhans, Anwar Hithnawi

  <details><summary>摘要 / Abstract</summary>

  Recent advancements in privacy-preserving machine learning are paving the way to extend the benefits of ML to highly sensitive data that, until now, have been hard to utilize due to privacy concerns and regulatory constraints. Simultaneously, there is a growing emphasis on enhancing the transparency and accountability of machine learning, including the ability to audit ML deployments. While ML auditing and PPML have both been the subjects of intensive research, they have predominately been examined in isolation. However, their combination is becoming increasingly important. In this work, we introduce Arc, an MPC framework for auditing privacy-preserving machine learning. At the core of our framework is a new protocol for efficiently verifying MPC inputs against succinct commitments at scale. We evaluate the performance of our framework when instantiated with our consistency protocol and compare it to hashing-based and homomorphic-commitment-based approaches, demonstrating that it is up to 10^4x faster and up to 10^6x more concise.

  匹配依据：MPC: mpc (context)

  </details>

- **Threshold Garbled Circuits with Low Overhead**
  2024-02-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/316)
  Schuyler Rosefield, abhi shelat, LaKyah Tyner

  <details><summary>摘要 / Abstract</summary>

  The folklore approach to designing a threshold variant of symmetric cryptographic algorithms involves applying generic MPC methods to se- cret sharing techniques: the MPC first combines participant input shares using the secret sharing scheme, and then evaluates the cryptographic function on the reconstructed key. Hardening this secure against n − 1 malicious parties requires some mechanism to ensure input consistency, e.g., adding MACs to inputs, which consequently, increases the number of inputs and gates to the MPC. In many cases, this extra overhead is substantially more than the underlying cost of evaluating the symmetric cryptographic algorithm. We present a scheme that can convert any suitable maliciously secure dishonest majority boolean-circuit FMPC into a threshold scheme Fthresh with almost no overhead. Specifically, we present an SUC-secure scheme that allows for reactive threshold t-of-n boolean circuit evaluation amongst a group of n parties P , for any t ≤ n, against a malicious adversary that corrupts any number of parties less than the threshold t. Moreover, mul- tiple circuits can be evaluated sequentially with the secret-shared authen- ticated outputs of a circuit to be used subsequently as inputs for a new circuit by any S ⊆ P of size |S| ≥ t. Building upon the works of Wang et al, Hazay et al, and Yang et al, [WRK17, HSSV17, YWZ20] for dishonest majority FMPC, our key insight is to create threshold versions of the “authenticated bits” used to han- dle input in these recent n-party garbled circuits protocols. The resulting design incurs a small overhead to produce the reusable “threshold authen- ticated bits” during preprocessing, and adds no extra communication to evaluate with the authenticated input during the online phase. Using our methods, thresholdizing a boolean circuit has essentially no performance overhead. For example, to compute HMAC, a full Setup+Eval execution of the (n − 2)-out-of-n thresholdized version is approximately 4% more expensive than the state-of-the-art n-party MPC. In contrast, using the folklore method is approximately 100% more expensive. This is especially true for small circuits such as AES which has 6800 gates and thus incurs the most overhead for thresholdizing. Simply considering the online Eval cost, our approach can evaluate AES blocks at 2.3/s with 16 parties, exceeding the baseline MPC cost without preprocessing, and sur- passing the folklore method that only achieves .33/s blocks. Ultimately, this result makes threshold boolean circuit MPC as feasible as any MPC application.

  匹配依据：MPC: garbled circuits, secret sharing

  </details>

- **CAPABARA: A Combined Attack on CAPA**
  2024-02-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/287)
  Dilara Toprakhisar, Svetla Nikova, Ventzislav Nikov

  <details><summary>摘要 / Abstract</summary>

  Physical attacks pose a substantial threat to the secure implementation of cryptographic algorithms. While considerable research efforts are dedicated to protecting against passive physical attacks (e.g., side-channel analysis (SCA)), the landscape of protection against other types of physical attacks remains a challenge. Fault attacks (FA), though attracting growing attention in research, still lack the prevalence of provably secure designs when compared to SCA. The realm of combined attacks, which leverage the capabilities of both SCA and FA adversaries, introduces powerful adversarial models, rendering protection against them challenging. This challenge has consequently led to a relatively unexplored area of research, resulting in a notable gap in understanding and efficiently protecting against combined attacks. The CAPA countermeasure, published at CRYPTO 2018, addresses this challenge with a robust adversarial model that goes beyond conventional SCA and FA adversarial models. Drawing inspiration from the principles of Multiparty Computation (MPC), CAPA claims security against higher-order SCA, higher-order fault attacks, and their combination. In this work, we present a combined attack that breaks CAPA within the constraints of its assumed adversarial model. In response, we propose potential fixes to the design of CAPA that increase the complexity of the proposed attack, although not provably thwarting it. With this presented combined attack, we highlight the difficulty of effectively protecting against combined attacks.

  匹配依据：MPC: multiparty computation

  </details>

- **The Multi-user Constrained PRF Security of Generalized GGM Trees for MPC and Hierarchical Wallets**
  2024-02-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/275)
  Chun Guo, Xiao Wang, Xiang Xie, Yu Yu

  <details><summary>摘要 / Abstract</summary>

  Multi-user (mu) security considers large-scale attackers that, given access to a number of cryptosystem instances, attempt to compromise at least one of them. We initiate the study of mu security of the so-called GGMtree that stems from the PRG-to-PRF transformation of Goldreich, Goldwasser, and Micali, with a goal to provide references for its recently popularized use in applied cryptography. We propose a generalized model for GGM trees and analyze its mu prefix-constrained PRF security in the random oracle model. Our model allows to derive concrete bounds and improvements for various protocols, and we showcase on the Bitcoin-Improvement-Proposal standard Bip32 hierarchical wallets and function secret sharing (FSS) protocols. In both scenarios, we propose improvements with better performance and concrete security bounds at the same time. Compared with the state-of-the-art designs, our SHACAL3- and KeccaK-𝑝-based Bip32 variants reduce the communication cost of MPC-based implementations by 73.3%∼93.8%, while our AES-based FSS substantially improves mu security while reducing computations by 50%.

  匹配依据：MPC: secret sharing

  </details>

- **HARTS: High-Threshold, Adaptively Secure, and Robust Threshold Schnorr Signatures**
  2024-02-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/280)
  Renas Bacho, Julian Loss, Gilad Stern, Benedikt Wagner

  <details><summary>摘要 / Abstract</summary>

  Threshold variants of the Schnorr signature scheme have recently been at the center of attention due to their applications to cryptocurrencies. However, existing constructions for threshold Schnorr signatures among a set of $n$ parties with corruption threshold $t_c$ suffer from at least one of the following drawbacks: (i) security only against static (i.e., non-adaptive) adversaries, (ii) cubic or higher communication cost to generate a single signature, (iii) strong synchrony assumptions on the network, or (iv) $t_c+1$ are sufficient to generate a signature, i.e., the corruption threshold of the scheme equals its reconstruction threshold. Especially (iv) turns out to be a severe limitation for many asynchronous real-world applications where $t_c 2t_c$. This is optimal. We prove our result in a modular fashion in the algebraic group model. At the core of our construction, we design a new simple and adaptively secure high-threshold asynchronous verifiable secret sharing (AVSS) scheme which may be of independent interest.

  匹配依据：MPC: secret sharing

  </details>

- **Perfect/Statistical 2-Party Computation with Improved Circuit Privacy**
  2024-02-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/273)
  Jonathan Trostle

  <details><summary>摘要 / Abstract</summary>

  We present protocols where one entity, the server, evaluates a circuit with encrypted inputs from the second party, the client. We give secret key somewhat additive homomorphic schemes where the client has perfect privacy (server is computationally unbounded). The key idea for client privacy is the permutation table which consists of rows of vectors modulo a prime integer m: The initial row is (1, d2, ..., dc) where di-1|di, di &gt; N(a + 1)di-1, for an integer N which is a power of 2 and integer a, 2 &lt;= i &lt;= c. Subsequent rows are integer multiples of the 1st row, modulo m. The permutation table has a subset of rows (vectors) whose components are relatively short (facilitating addition without overflowing m) and which map to every possible vector modulo N (giving perfect privacy since every plaintext vector is possible given a ciphertext vector from the table.) We give a 2-party computation (2PC) protocol that also incorporates server inputs where the client has perfect privacy, assuming the server is semi-honest in the setup protocol. Client privacy is statistical if the server is malicious during the setup protocol. Server privacy only holds against a computationally bounded adversary since it depends on the hardness of a variant of the HSSP (Hidden Subset Sum Problem) and the DDH (Decisional Diffie Hellman Assumption). We leverage the Castagnos Laguillaumie linear homomorphic public key encryption for setup. The 2PC protocol maintains circuit privacy, without circuit expansion, except for leaking the number of AND gates to the client. Scaling the 2PC protocol via separate encryption parameters for smaller subcircuits allows the ciphertext size to remain constant as circuit size grows.

  匹配依据：MPC: 2 party computation

  </details>

- **Towards Achieving Asynchronous MPC with Linear Communication and Optimal Resilience**
  2024-02-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/243)
  Vipul Goyal, Chen-Da Liu-Zhang, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) allows a set of $n$ parties to jointly compute a function over their private inputs. The seminal works of Ben-Or, Canetti and Goldreich [STOC &#x27;93] and Ben-Or, Kelmer and Rabin [PODC &#x27;94] settled the feasibility of MPC over asynchronous networks. Despite the significant line of work devoted to improving the communication complexity, current protocols with information-theoretic security and optimal resilience $t&lt;n/3$ communicate $\Omega(n^4C)$ field elements for a circuit with $C$ multiplication gates. In contrast, synchronous MPC protocols with $O(nC)$ communication have long been known. In this work we make progress towards closing this gap. We provide a novel MPC protocol in the asynchronous setting with statistical security that makes black-box use of an asynchronous complete secret-sharing (ACSS) protocol. The cost per multiplication reduces to the cost of distributing a constant number of sharings via ACSS, improving a linear factor over the state of the art by Choudhury and Patra [IEEE Trans. Inf. Theory &#x27;17]. With a recent concurrent work achieving ACSS with linear cost per sharing, we achieve an MPC with ${O}(nC)$ communication and optimal resilience.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Robust Additive Randomized Encodings from IO and Pseudo-Non-linear Codes**
  2024-02-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/249)
  Nir Bitansky, Sapir Freizeit

  <details><summary>摘要 / Abstract</summary>

  Additive randomized encodings (ARE), introduced by Halevi, Ishai, Kushilevitz, and Rabin (CRYPTO 2023), reduce the computation of a k-party function $f (x_1, . . . , x_k )$ to locally computing encodings $\hat{x}_i$ of each input xi and then adding them together over some Abelian group into an output encoding $\hat{y} = ∑ \hat{x}_i$, which reveals nothing but the result. In robust ARE (RARE) the sum of any subset of $\hat{x}_i$, reveals only the residual function obtained by restricting the corresponding inputs. The appeal of (R)ARE comes from the simplicity of the online part of the computation involving only addition, which yields for instance non-interactive multi-party computation in the shuffle model where messages from different parties are anonymously shuffled. Halevi, Ishai, Kushilevitz, and Rabin constructed ARE from standard assumptions and RARE in the ideal obfuscation model, leaving open the question of whether RARE can be constructed in the plain model. We construct RARE in the plain model from indistinguishability obfuscation, which is necessary, and a new primitive that we call pseudo-non-linear codes. We provide two constructions of this primitive assuming either Learning with Errors or Decision Diffie Hellman. A bonus feature of our construction is that it is online succinct. Specifically, encodings $\hat{x}_i$ can be decomposed to offline parts $\hat{z}_i$ that can be sent directly to the evaluator and short online parts $\hat{g}_i$ that are added together.

  匹配依据：MPC: multi party computation

  </details>

- **Faster Signatures from MPC-in-the-Head**
  2024-02-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/252)
  Dung Bui, Eliana Carozza, Geoffroy Couteau, Dahmun Goudarzi, Antoine Joux

  <details><summary>摘要 / Abstract</summary>

  We revisit the construction of signature schemes using the MPC-in-the-head paradigm. We obtain two main contributions: – We observe that previous signatures in the MPC-in-the-head paradigm must rely on a salted version of the GGM puncturable pseudorandom function (PPRF) to avoid collision attacks. We design a new efficient PPRF construction that is provably secure in the multi-instance setting. The security analysis of our PPRF, in the ideal cipher model, is quite involved and forms a core technical contribution to our work. While previous constructions had to rely on a hash function, our construction uses only a fixed-key block cipher and is considerably more efficient as a result: we observe a 12× to 55× speed improvement for a recent signature scheme (Joux and Huth, Crypto’24). Our improved PPRF can be used to speed up many MPC-in-the-head signatures. – We introduce a new signature scheme from the regular syndrome decoding assumption, based on a new protocol for the MPC-in-the-head paradigm, which significantly reduces communication compared to previous works. Our scheme is conceptually simple, though its security analysis requires a delicate and nontrivial combinatorial analysis.

  匹配依据：MPC: mpc (context)

  </details>

- **2PC-MPC: Emulating Two Party ECDSA in Large-Scale MPC**
  2024-02-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/253)
  Offir Friedman, Avichai Marmor, Dolev Mutzari, Omer Sadika, Yehonatan C. Scaly, Yuval Spiizer, Avishay Yanai

  <details><summary>摘要 / Abstract</summary>

  Motivated by the need for a massively decentralized network concurrently servicing many clients, we present novel low-overhead UC-secure, publicly verifiable, threshold ECDSA protocols with identifiable abort. For the first time, we show how to reduce the message complexity from O(n^2) to O(n) and the computational complexity from O(n) to practically O(1) (per party, where n is the number of parties). We require only a broadcast channel for communication. Therefore, we natively support use-cases like permissionless bridges and decentralized custody, where P2P channels between every pair of parties are infeasible. Consequently, the message complexity is reduced and the protocol is publicly verifiable. We enable all communication to be public (over a broadcast channel), by using a threshold additively homomorphic encryption scheme and novel zero-knowledge proofs. To further reduce the computation and communication overheads, our protocols employ novel batching and amortization techniques, which may be of independent interest. Our second main contribution is the introduction of the notion of a 2PC-MPC protocol - a two-party ECDSA protocol where the second party is fully emulated by a network of n parties. This notion assures that both the first party (the client) and (a threshold) of the network are required to participate in signing, while abstracting away the internal structure of the network. In particular, the communication and computation complexities of the client remain independent of the network properties (e.g. size). This allows ultimate decentralization in distributed custody use-cases, as recent growing interest in the industry demands. We report that our implementation completes the signing phase in 1.23 and 12.703 seconds, for 256 and 1024 parties, respectively.

  匹配依据：MPC: 2pc (context)

  </details>

- **Seagull: Privacy preserving network verification system**
  2024-02-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.08956)
  Jaber Daneshamooz, Melody Yu, Sucheer Maddury

  <details><summary>摘要 / Abstract</summary>

  The Internet relies on routing protocols to direct traffic efficiently across interconnected networks, with the Border Gateway Protocol (BGP) serving as the core mechanism managing routing between autonomous systems. However, BGP configurations are largely manual, making them susceptible to human errors that can lead to outages or security vulnerabilities. Verifying the correctness and convergence of BGP configurations is therefore essential for maintaining a stable and secure Internet. Yet, this verification process faces two key challenges: preserving the privacy of proprietary routing information and ensuring scalability across large, distributed networks. This paper introduces a privacy-preserving verification framework that leverages multiparty computation (MPC) to validate BGP configurations without exposing sensitive routing data. Our approach overcomes both privacy and scalability challenges by ensuring that no information beyond the verification outcome is revealed. Through formal analysis, we show that the proposed method achieves strong privacy guarantees and practical scalability, providing a secure and efficient foundation for verifying BGP-based routing in the Internet backbone.

  匹配依据：MPC: multiparty computation

  </details>

- **New Black-Box Separations through Mathematically Structured Primitives**
  2024-02-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/236)
  Hart Montgomery, Sikhar Patranabis

  <details><summary>摘要 / Abstract</summary>

  We provide a novel view of public-key cryptography by showing full equivalences of certain primitives to &quot;hard&quot; monoid actions. More precisely, we show that key exchange and two-party computation are exactly equivalent to monoid actions with certain structural and hardness properties. To the best of our knowledge, this is the first &quot;natural&quot; characterization of the mathematical structure inherent to any key exchange or two-party computation protocol, and the first explicit proof of the necessity of mathematical structure for public-key cryptography. We then utilize these characterizations to show new black-box separation results. Concretely, we obtain the following results: Two-Party Key Exchange. We show that that any two-party noninteractive key exchange protocol is equivalent to the existence of an abelian monoid action equipped with a natural hardness property, namely (distributional) unpredictability. More generally, we show that any $k$-round (two-party) key exchange protocol is essentially equivalent to the existence of a (distributional) unpredictable monoid action with certain commutator-like properties. Rudich (Crypto &#x27;91) shows a black-box separation of $k$-round and $(k+1)$-round key exchange for any $k$; we use our generic primitive here to formalize this result and extend it to efficient key exchange protocols (where communication is $\textsf{poly}(k)$). Two-Party Computation. We show that any maliciously secure two-party computation protocol is also equivalent to a monoid action with commutator-like properties and certain hardness guarantees. We then use a generic version of this primitive to show a black-box separation between $k$-round semi-honest secure two-party computation and $(k+1)$-round maliciously secure two-party computation. This yields the first black-box separation (to our knowledge) between $k$-round and $(k+1)$-round maliciously secure two-party computation protocols.

  匹配依据：MPC: secure two party computation, two party computation

  </details>

- **I can't see it but I can Fine-tune it: On Encrypted Fine-tuning of Transformers using Fully Homomorphic Encryption**
  2024-02-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.09059)
  Prajwal Panzade, Daniel Takabi, Zhipeng Cai

  <details><summary>摘要 / Abstract</summary>

  In today&#x27;s machine learning landscape, fine-tuning pretrained transformer models has emerged as an essential technique, particularly in scenarios where access to task-aligned training data is limited. However, challenges surface when data sharing encounters obstacles due to stringent privacy regulations or user apprehension regarding personal information disclosure. Earlier works based on secure multiparty computation (SMC) and fully homomorphic encryption (FHE) for privacy-preserving machine learning (PPML) focused more on privacy-preserving inference than privacy-preserving training. In response, we introduce BlindTuner, a privacy-preserving fine-tuning system that enables transformer training exclusively on homomorphically encrypted data for image classification. Our extensive experimentation validates BlindTuner&#x27;s effectiveness by demonstrating comparable accuracy to non-encrypted models. Notably, our findings highlight a substantial speed enhancement of 1.5x to 600x over previous work in this domain.

  匹配依据：MPC: secure multiparty computation

  </details>

- **On black-box separations of quantum digital signatures from pseudorandom states**
  2024-02-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.08194)
  Andrea Coladangelo, Saachi Mutreja

  <details><summary>摘要 / Abstract</summary>

  It is well-known that digital signatures can be constructed from one-way functions in a black-box way. While one-way functions are essentially the minimal assumption in classical cryptography, this is not the case in the quantum setting. A variety of qualitatively weaker and inherently quantum assumptions (e.g. EFI pairs, one-way state generators, and pseudorandom states) are known to be sufficient for non-trivial quantum cryptography. While it is known that commitments, zero-knowledge proofs, and even multiparty computation can be constructed from these assumptions, it has remained an open question whether the same is true for quantum digital signatures schemes (QDS). In this work, we show that there $\textit{does not}$ exist a black-box construction of a QDS scheme with classical signatures from pseudorandom states with linear, or greater, output length. Our result complements that of Morimae and Yamakawa (2022), who described a $\textit{one-time}$ secure QDS scheme with classical signatures, but left open the question of constructing a standard $\textit{multi-time}$ secure one.

  匹配依据：MPC: multiparty computation

  </details>

- **Mastic: Private Weighted Heavy-Hitters and Attribute-Based Metrics**
  2024-02-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/221)
  Dimitris Mouris, Christopher Patton, Hannah Davis, Pratik Sarkar, Nektarios Georgios Tsoutsos

  <details><summary>摘要 / Abstract</summary>

  Insight into user experience and behavior is critical to the success of large software systems and web services. Gaining such insights, while preserving user privacy, is a significant challenge. Recent advancements in multi-party computation have made it practical to securely compute aggregates over secret shared data. Two such protocols have emerged as candidates for standardization at the IETF: Prio (NSDI 2017) for general-purpose statistics; and Poplar (IEEE S&amp;P 2021) for heavy hitters, where the goal is to compute the most popular inputs held by users without learning the inputs themselves. While each of these protocols is well-suited to certain applications, there remain a number of use cases identified by IETF for which neither Prio nor Poplar is practical. We introduce Mastic, a protocol for the following functionality: each of a large number of clients holds an input (e.g., a URL) and its corresponding weight (e.g., page load time); for a given candidate input (or prefix), a small number of non-colluding servers wish to securely aggregate the weights of clients that hold that input (or some input with that prefix), without learning the weights or which client holds which input. This functionality makes two new classes of applications possible. The first is a natural generalization of heavy hitters we call weighted heavy-hitters. The second is an enhancement of Prio-style metrics we call attribute-based metrics in which aggregates are grouped by hierarchical user attributes (e.g., their geographic location or software version). We demonstrate Mastic&#x27;s practicality for these applications with a real-world example of each. We also compare our protocol with Prio and Poplar on a wide area network. Overall, we report over one order of magnitude performance improvement over Poplar for plain heavy-hitters and $1.5-2\times$ improvement over Prio for attribute-based metrics.

  匹配依据：MPC: multi party computation

  </details>

- **CaPS: Collaborative and Private Synthetic Data Generation from Distributed Sources**
  2024-02-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.08614)
  Sikha Pentyala, Mayana Pereira, Martine De Cock

  <details><summary>摘要 / Abstract</summary>

  Data is the lifeblood of the modern world, forming a fundamental part of AI, decision-making, and research advances. With increase in interest in data, governments have taken important steps towards a regulated data world, drastically impacting data sharing and data usability and resulting in massive amounts of data confined within the walls of organizations. While synthetic data generation (SDG) is an appealing solution to break down these walls and enable data sharing, the main drawback of existing solutions is the assumption of a trusted aggregator for generative model training. Given that many data holders may not want to, or be legally allowed to, entrust a central entity with their raw data, we propose a framework for the collaborative and private generation of synthetic tabular data from distributed data holders. Our solution is general, applicable to any marginal-based SDG, and provides input privacy by replacing the trusted aggregator with secure multi-party computation (MPC) protocols and output privacy via differential privacy (DP). We demonstrate the applicability and scalability of our approach for the state-of-the-art select-measure-generate SDG algorithms MWEM+PGM and AIM.

  匹配依据：MPC: secure multi party computation

  </details>

- **Enhancing Data Security through Rainbow Antimagic Graph Coloring for Secret-Share Distribution and Reconstruction**
  2024-02-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.16843)
  Raul M. Falcon, K. Abirami, N. Mohanapriya, Dafik

  <details><summary>摘要 / Abstract</summary>

  Now-a-days, ensuring data security has become an increasingly formidable challenge in safeguarding individuals&#x27; sensitive information. Secret-sharing scheme has evolved as a most successful cryptographic technique that allows a secret to be divided or distributed among a group of participants in such a way that only a subset of those participants can reconstruct the original secret. This provides a safe level of security and redundancy, ensuring that no single individual possesses the complete secret. The implementation of Rainbow Antimagic coloring within these schemes not only safeguards the data but also ensures an advanced level of information security among multi-participant groups. Additionally, the retrieved data is reconstructed and can be disseminated to all group participants via multiple rounds of communication.

  匹配依据：MPC: secret sharing

  </details>

- **Batch PIR and Labeled PSI with Oblivious Ciphertext Compression**
  2024-02-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/215)
  Alexander Bienstock, Sarvar Patel, Joon Young Seo, Kevin Yeo

  <details><summary>摘要 / Abstract</summary>

  In this paper, we study two problems: oblivious compression and decompression of ciphertexts. In oblivious compression, a server holds a set of ciphertexts with a subset of encryptions of zeroes whose positions are only known to the client. The goal is for the server to effectively compress the ciphertexts obliviously, while preserving the non-zero plaintexts and without learning the plaintext values. For oblivious decompression, the client, instead, succinctly encodes a sequence of plaintexts such that the server may decode encryptions of all plaintexts value, but the zeroes may be replaced with arbitrary values. We present solutions to both problems that construct lossless compressions only 5% more than the optimal minimum using only additive homomorphism. The crux of both algorithms involve embedding ciphertexts as random linear systems that are efficiently solvable. Using our compression schemes, we obtain state-of-the-art schemes for batch private information retrieval (PIR) where a client wishes to privately retrieve multiple entries from a server-held database in one query. We show that our compression schemes may be used to reduce communication by up to 30% for batch PIR in both the single- and two-server settings. Additionally, we study labeled private set intersection (PSI) in the unbalanced setting where one party&#x27;s set is significantly smaller than the other party&#x27;s set and each entry has associated data. By utilizing our novel compression algorithm, we present a protocol with 65-88% reduction in communication with comparable computation compared to prior works.

  匹配依据：MPC: private set intersection

  </details>

- **You Still See Me: How Data Protection Supports the Architecture of AI Surveillance**
  2024-02-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.06609)
  Rui-Jie Yew, Lucy Qin, Suresh Venkatasubramanian

  <details><summary>摘要 / Abstract</summary>

  Data forms the backbone of artificial intelligence (AI). Privacy and data protection laws thus have strong bearing on AI systems. Shielded by the rhetoric of compliance with data protection and privacy regulations, privacy-preserving techniques have enabled the extraction of more and new forms of data. We illustrate how the application of privacy-preserving techniques in the development of AI systems--from private set intersection as part of dataset curation to homomorphic encryption and federated learning as part of model computation--can further support surveillance infrastructure under the guise of regulatory permissibility. Finally, we propose technology and policy strategies to evaluate privacy-preserving techniques in light of the protections they actually confer. We conclude by highlighting the role that technologists could play in devising policies that combat surveillance AI technologies.

  匹配依据：MPC: private set intersection

  </details>

- **Distributed Randomness using Weighted VUFs**
  2024-02-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/198)
  Sourav Das, Benny Pinkas, Alin Tomescu, Zhuolun Xiang

  <details><summary>摘要 / Abstract</summary>

  Shared randomness in blockchain can expand its support for randomized applications and can also help strengthen its security. Many existing blockchains rely on external randomness beacons for shared randomness, but this approach reduces fault tolerance, increases latency, and complicates application development. An alternate approach is to let the blockchain validators generate fresh shared randomness themselves once for every block. We refer to such a design as the \emph{on-chain} randomness. In this paper, we design an efficient on-chain randomness protocol for Byzantine fault-tolerance based Proof-of-Stake blockchains with weighted validators. A key component of our protocol is a weighted verifiable unpredictable function (VUF). The notable feature of our weighted VUF is that the computation and communication costs of parties are independent of their weight. This is crucial for scalability of on-chain randomness where we repeatedly evaluate the weighted VUF in quick succession. We also design a new scalable publicly verifiable secret sharing~(PVSS) scheme with aggregatable transcript and use it to design a distributed key generation~(DKG) protocol for our VUF. We implemented our schemes on top of Aptos, a proof-of-stake blockchain deployed in production, conducted an end-to-end evaluation with 112 validators and a total weight of up to 4053. In this setup, our on-chain randomness protocol adds only 133 milliseconds of latency compared to a protocol without randomness. We also demonstrate the performance improvements of our design through rigorous comparison with baseline methods.

  匹配依据：MPC: secret sharing

  </details>

- **Helium: Scalable MPC among Lightweight Participants and under Churn**
  2024-02-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/194)
  Christian Mouchet, Sylvain Chatel, Apostolos Pyrgelis, Carmela Troncoso

  <details><summary>摘要 / Abstract</summary>

  We introduce Helium, a novel framework that supports scalable secure multiparty computation (MPC) for lightweight participants and tolerates churn. Helium relies on multiparty homomorphic encryption (MHE) as its core building block. While MHE schemes have been well studied in theory, prior works fall short of addressing critical considerations paramount for adoption such as supporting resource-constrained and unstably connected participants. In this work, we systematize the requirements of MHE-based MPC protocols from a practical lens, and we propose a novel execution mechanism that addresses those considerations. We implement this execution mechanism in Helium, which makes it the first implemented framework to support MPC under network churn based solely on cryptographic assumptions. We show that a Helium network of $30$ parties connected with $100$Mbits/s links and experiencing a system-wide churn rate of $40$ failures per minute can compute the product between a fixed $512\times512$ secret matrix (e.g., a collectively-trained private model) and a fresh secret vector (e.g., a feature vector) $8.3$ times per second. This is $\sim\!\!1500$ times faster than a state-of-the-art MPC framework operating under no churn.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Direct FSS Constructions for Branching Programs and More from PRGs with Encoded-Output Homomorphism**
  2024-02-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/192)
  Elette Boyle, Lisa Kohl, Zhe Li, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  Function secret sharing (FSS) for a class $\cal{F}$ allows to split a secret function $f \in \cal{F}$ into (succinct) secret shares $f_0,f_1$, such that for all $x\in \{0,1\}^n$ it holds $f_0(x)-f_1(x)=f(x)$. FSS has numerous applications, including private database queries, nearest neighbour search, private heavy hitters and secure computation in the preprocessing model, where the supported class $\cal{F}$ translates to richness in the application. Unfortunately, concretely efficient FSS constructions are only known for very limited function classes. In this work we introduce the notion of pseudorandom generators with encoded-output homomorphism (EOH-PRGs), and give direct FSS constructions for bit-fixing predicates, branching programs and more based on this primitive. Further, we give constructions of FSS for deterministic finite automatas (DFAs) from a KDM secure variant of EOH-PRGs. - New abstractions. Following the work of Alamati et al.(EUROCRYPT &#x27;19), who classify minicrypt primitives with algebraic structure and their applications, we capture the essence of our FSS constructions in the notion of EOH-PRG, paving the road towards future efficiency improvements via new instantiations of this primitive. The abstraction of EOH-PRG and its instantiations may be of independent interest, as it is an approximate substitution of an ideal homomorphic PRG. - Better efficiency. We show that EOH-PRGs can be instantiated from LWE and a small-exponent variant of the DCR assumption. A theoretical analysis of our instantiations suggest efficiency improvements over the state of the art both in terms of key size and evaluation time: We show that our FSS instantiations lead to smaller key sizes, improving over previous constructions by a factor of $3.5$ and more. While for bit-fixing predicates our FSS constructions show comparable or mildly improved run time (depending on the instantiation), we achieve considerable improvements for branching programs by avoiding the expensive generic transformation via universal circuits, shaving off a factor of $w$ and more in the number of abstract operations, where $w$ corresponds to an upper bound on the width of the underlying class of branching programs. - New constructions. We show that our instantiations of EOH-PRGs additionally support a form of KDM-security, without requiring an additional circular-security assumption. Based on this, we give the first FSS construction for DFAs which supports the evaluation of inputs of a-priori unbounded length without relying on FHE. - Applications. We outline applications of our FSS constructions including pattern matching with wild cards, image matching, nearest neighbor search and regular expression matching.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Mind the Gap: Securely modeling cyber risk based on security deviations from a peer group**
  2024-02-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.04166)
  Taylor Reynolds, Sarah Scheffler, Daniel J. Weitzner, Angelina Wu

  <details><summary>摘要 / Abstract</summary>

  There are two strategic and longstanding questions about cyber risk that organizations largely have been unable to answer: What is an organization&#x27;s estimated risk exposure and how does its security compare with peers? Answering both requires industry-wide data on security posture, incidents, and losses that, until recently, have been too sensitive for organizations to share. Now, privacy enhancing technologies (PETs) such as cryptographic computing can enable the secure computation of aggregate cyber risk metrics from a peer group of organizations while leaving sensitive input data undisclosed. As these new aggregate data become available, analysts need ways to integrate them into cyber risk models that can produce more reliable risk assessments and allow comparison to a peer group. This paper proposes a new framework for benchmarking cyber posture against peers and estimating cyber risk within specific economic sectors using the new variables emerging from secure computations. We introduce a new top-line variable called the Defense Gap Index representing the weighted security gap between an organization and its peers that can be used to forecast an organization&#x27;s own security risk based on historical industry data. We apply this approach in a specific sector using data collected from 25 large firms, in partnership with an industry ISAO, to build an industry risk model and provide tools back to participants to estimate their own risk exposure and privately compare their security posture with their peers.

  匹配依据：MPC: secure computation

  </details>

- **Fast Public-Key Silent OT and More from Constrained Naor-Reingold**
  2024-02-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/178)
  Dung Bui, Geoffroy Couteau, Pierre Meyer, Alain Passelègue, Mahshid Riahinia

  <details><summary>摘要 / Abstract</summary>

  Pseudorandom Correlation Functions (PCFs) allow two parties, given correlated evaluation keys, to locally generate arbitrarily many pseudorandom correlated strings, e.g. Oblivious Transfer (OT) correlations, which can then be used by the two parties to jointly run secure computation protocols. In this work, we provide a novel and simple approach for constructing PCFs for OT correlation, by relying on constrained pseudorandom functions for a class of constraints containing a weak pseudorandom function (wPRF). We then show that tweaking the Naor-Reingold pseudorandom function and relying on low-complexity pseudorandom functions allow us to instantiate our paradigm. We further extend our ideas to obtain efficient public-key PCFs, which allow the distribution of correlated keys between parties to be non-interactive: each party can generate a pair of public/secret keys, and any pair of parties can locally derive their correlated evaluation key by combining their secret key with the other party&#x27;s public key. In addition to these theoretical contributions, we detail various optimizations and provide concrete instantiations of our paradigm relying on the Boneh-Ishai-Passelègue-Sahai-Wu wPRF and the Goldreich-Applebaum-Raykov wPRF. Putting everything together, we obtain public-key PCFs with a throughput of 15k-40k OT/s, which is of a similar order of magnitude to the state-of-the-art interactive PCFs and about 4 orders of magnitude faster than state-of-the-art public-key PCFs. As a side result, we also show that public-key PCFs can serve as a building block to construct reusable designated-verifier non-interactive zero-knowledge proofs (DV-NIZK) for NP. Combined with our instantiations, this yields simple and efficient reusable DV-NIZKs for NP in pairing-free groups.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **Decentralized Blockchain-based Robust Multi-agent Multi-armed Bandit**
  2024-02-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.04417)
  Mengfan Xu, Diego Klabjan

  <details><summary>摘要 / Abstract</summary>

  We study a robust, i.e. in presence of malicious participants, multi-agent multi-armed bandit problem where multiple participants are distributed on a fully decentralized blockchain, with the possibility of some being malicious. The rewards of arms are homogeneous among the honest participants, following time-invariant stochastic distributions, which are revealed to the participants only when certain conditions are met to ensure that the coordination mechanism is secure enough. The coordination mechanism&#x27;s objective is to efficiently ensure the cumulative rewards gained by the honest participants are maximized. To this end, we are the first to incorporate advanced techniques from blockchains, as well as novel mechanisms, into such a cooperative decision making framework to design optimal strategies for honest participants. This framework allows various malicious behaviors and the maintenance of security and participant privacy. More specifically, we select a pool of validators who communicate to all participants, design a new consensus mechanism based on digital signatures for these validators, invent a UCB-based strategy that requires less information from participants through secure multi-party computation, and design the chain-participant interaction and an incentive mechanism to encourage participants&#x27; participation. Notably, we are the first to prove the theoretical regret of the proposed algorithm and claim its optimality. Unlike existing work that integrates blockchains with learning problems such as federated learning which mainly focuses on optimality via computational experiments, we demonstrate that the regret of honest participants is upper bounded by $\log{T}$ under certain assumptions. The regret bound is consistent with the multi-agent multi-armed bandit problem, both without malicious participants and with purely Byzantine attacks which do not affect the entire system.

  匹配依据：MPC: secure multi party computation

  </details>

- **QPP and HPPK: Unifying Non-Commutativity for Quantum-Secure Cryptography with Galois Permutation Group**
  2024-02-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.01852) · [IACR ePrint](https://eprint.iacr.org/2024/174)
  Randy Kuang

  <details><summary>摘要 / Abstract</summary>

  In response to the evolving landscape of quantum computing and the escalating vulnerabilities in classical cryptographic systems, our paper introduces a unified cryptographic framework. Rooted in the innovative work of Kuang et al., we leverage two novel primitives: the Quantum Permutation Pad (QPP) for symmetric key encryption and the Homomorphic Polynomial Public Key (HPPK) for Key Encapsulation Mechanism (KEM) and Digital Signatures (DS). Our approach adeptly confronts the challenges posed by quantum advancements. Utilizing the Galois Permutation Group&#x27;s matrix representations and inheriting its bijective and non-commutative properties, QPP achieves quantum-secure symmetric key encryption, seamlessly extending Shannon&#x27;s perfect secrecy to both classical and quantum-native systems. Meanwhile, HPPK, free from NP-hard problems, fortifies symmetric encryption for the plain public key. It accomplishes this by concealing the mathematical structure through modular multiplications or arithmetic representations of Galois Permutation Group over hidden rings, harnessing their partial homomorphic properties. This allows for secure computation on encrypted data during secret encapsulations, bolstering the security of the plain public key. The seamless integration of KEM and DS within HPPK cryptography yields compact key, cipher, and signature sizes, demonstrating exceptional performance. This paper organically unifies QPP and HPPK under the Galois Permutation Group, marking a significant advancement in laying the groundwork for quantum-resistant cryptographic protocols. Our contribution propels the development of secure communication systems amid the era of quantum computing.

  匹配依据：MPC: secure computation

  </details>

- **On Tweakable Correlation Robust Hashing against Key Leakages**
  2024-02-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/163)
  Chun Guo, Xiao Wang, Kang Yang, Yu Yu

  <details><summary>摘要 / Abstract</summary>

  We continue the study of blockcipher-based (tweakable) correlation robust hash functions, which are central building blocks of circuit garbling and oblivious-transfer extension schemes. Motivated by Roy (CRYPTO 2022), we first enhance the multi-user tweakable correlation robust notion of Guo et al. (CRYPTO 2020) with a {\it key leaking oracle} that tells the adversary whether a certain user key satisfies the adversarially-chosen predicate. We then investigate the state-of-the-art hash construction of Guo et al. with respect to our new security definition, providing security proof as well as matching attacks. As an application, we exhibit an OT extension protocol with non-trivial multi-user security.

  匹配依据：MPC: oblivious transfer

  </details>

- **Federated Learning Priorities Under the European Union Artificial Intelligence Act**
  2024-02-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.05968)
  Herbert Woisetschläger, Alexander Erben, Bill Marino, Shiqiang Wang, Nicholas D. Lane, Ruben Mayer, Hans-Arno Jacobsen

  <details><summary>摘要 / Abstract</summary>

  The age of AI regulation is upon us, with the European Union Artificial Intelligence Act (AI Act) leading the way. Our key inquiry is how this will affect Federated Learning (FL), whose starting point of prioritizing data privacy while performing ML fundamentally differs from that of centralized learning. We believe the AI Act and future regulations could be the missing catalyst that pushes FL toward mainstream adoption. However, this can only occur if the FL community reprioritizes its research focus. In our position paper, we perform a first-of-its-kind interdisciplinary analysis (legal and ML) of the impact the AI Act may have on FL and make a series of observations supporting our primary position through quantitative and qualitative analysis. We explore data governance issues and the concern for privacy. We establish new challenges regarding performance and energy efficiency within lifecycle monitoring. Taken together, our analysis suggests there is a sizable opportunity for FL to become a crucial component of AI Act-compliant ML systems and for the new regulation to drive the adoption of FL techniques in general. Most noteworthy are the opportunities to defend against data bias and enhance private and secure computation

  匹配依据：MPC: secure computation

  </details>

- **Dragon: Decentralization at the cost of Representation after Arbitrary Grouping and Its Applications to Sub-cubic DKG and Interactive Consistency**
  2024-02-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/168)
  Hanwen Feng, Zhenliang Lu, Qiang Tang

  <details><summary>摘要 / Abstract</summary>

  Several distributed protocols, including distributed key generation (DKG) and interactive consistency (IC), depend on $\mathcal{O}(n)$ instances of Byzantine Broadcast or Byzantine Agreement among $n$ nodes, resulting in ${\Theta}(n^3)$ communication overhead. In this paper, we provide a new methodology of realizing such broadcasts we call DRAGON: Decentralization at the cost of Representation after Arbitrary GrOupiNg. At the core of it, we arbitrarily group nodes into small ``shards&#x27;&#x27; and paired with multiple new primitives we call consortium-sender (dealer) broadcast (and secret sharing). The new tools enable a shard of nodes to jointly broadcast (or securely contribute a secret) to the whole population only at the cost of one dealer ({\em as if} there is a representative). With our new Dragon method, we construct the first two DKG protocols, both achieving optimal resilience, with sub-cubic total communication and computation. The first DKG generates a secret key within an Elliptic Curve group, incurring $\widetilde{\mathcal{O}}(n^{2.5}\lambda)$ total communication and computation. The second DKG, while slightly increasing communication and computation by a factor of the statistical security parameter, generates a secret key as a field element, which makes it directly compatible with various off-the-shelf DLog-based threshold cryptographic systems. We also construct a first deterministic IC with sub-cubic communication. Along the way, we also formalize simulation-based security and proved it for publicly verifiable secret sharing (PVSS), making it possible for a modular analysis, which might be of independent interest.

  匹配依据：MPC: secret sharing

  </details>

- **Spin: An Efficient Secure Computation Framework with GPU Acceleration**
  2024-02-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.02320)
  Wuxuan Jiang, Xiangjun Song, Shenbai Hong, Haijun Zhang, Wenxin Liu, Bo Zhao, Wei Xu, Yi Li

  <details><summary>摘要 / Abstract</summary>

  Accuracy and efficiency remain challenges for multi-party computation (MPC) frameworks. Spin is a GPU-accelerated MPC framework that supports multiple computation parties and a dishonest majority adversarial setup. We propose optimized protocols for non-linear functions that are critical for machine learning, as well as several novel optimizations specific to attention that is the fundamental unit of Transformer models, allowing Spin to perform non-trivial CNNs training and Transformer inference without sacrificing security. At the backend level, Spin leverages GPU, CPU, and RDMA-enabled smart network cards for acceleration. Comprehensive evaluations demonstrate that Spin can be up to $2\times$ faster than the state-of-the-art for deep neural network training. For inference on a Transformer model with 18.9 million parameters, our attention-specific optimizations enable Spin to achieve better efficiency, less communication, and better accuracy.

  匹配依据：MPC: multi party computation, secure computation

  </details>

- **Repairing Reed-Solomon Codes over Prime Fields via Exponential Sums**
  2024-02-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.02358)
  Roni Con, Noah Shutty, Itzhak Tamo, Mary Wootters

  <details><summary>摘要 / Abstract</summary>

  This paper presents two repair schemes for low-rate Reed-Solomon (RS) codes over prime fields that can repair any node by downloading a constant number of bits from each surviving node. The total bandwidth resulting from these schemes is greater than that incurred during trivial repair; however, this is particularly relevant in the context of leakage-resilient secret sharing. In that framework, our results provide attacks showing that $k$-out-of-$n$ Shamir&#x27;s Secret Sharing over prime fields for small $k$ is not leakage-resilient, even when the parties leak only a constant number of bits. To the best of our knowledge, these are the first such attacks. Our results are derived from a novel connection between exponential sums and the repair of RS codes. Specifically, we establish that non-trivial bounds on certain exponential sums imply the existence of explicit nonlinear repair schemes for RS codes over prime fields.

  匹配依据：MPC: secret sharing

  </details>

- **Quantum Secret Sharing Enhanced: Utilizing W States for Anonymous and Secure Communication**
  2024-02-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.02413)
  Guo-Dong Li, Wen-Chuan Cheng, Qing-Le Wang, Long Cheng, Ying Mao, Heng-Yue Jia

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) is the result of merging the principles of quantum mechanics with secret information sharing. It enables a sender to share a secret among receivers, and the receivers can then collectively recover the secret when the need arises. To enhance the practicality of these quantum protocols, an innovative concept of quantum anonymous secret sharing (QASS) is advanced. In this paper, we propose a QASS protocol via W states, which can share secrets while ensuring recover-ability, recover-security, and recover-anonymity. We have rigorously evaluated our protocols, verifying their accuracy and fortifying their security against scenarios involving the active adversary. This includes considerations for dishonest receivers and non-receivers. Moreover, acknowledging the imperfections inherent in real-world communication channels, we have also undertaken an exhaustive analysis of our protocol&#x27;s security and effectiveness in a quantum network where some form of noise is present. Our investigations reveal that W states exhibit good performance in mitigating noise interference, making them apt for practical applications.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Distributed Learning for Residential Short-Term Load Forecasting**
  2024-02-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.01546)
  Yi Dong, Yingjie Wang, Mariana Gama, Mustafa A. Mustafa, Geert Deconinck, Xiaowei Huang

  <details><summary>摘要 / Abstract</summary>

  In the realm of power systems, the increasing involvement of residential users in load forecasting applications has heightened concerns about data privacy. Specifically, the load data can inadvertently reveal the daily routines of residential users, thereby posing a risk to their property security. While federated learning (FL) has been employed to safeguard user privacy by enabling model training without the exchange of raw data, these FL models have shown vulnerabilities to emerging attack techniques, such as Deep Leakage from Gradients and poisoning attacks. To counteract these, we initially employ a Secure-Aggregation (SecAgg) algorithm that leverages multiparty computation cryptographic techniques to mitigate the risk of gradient leakage. However, the introduction of SecAgg necessitates the deployment of additional sub-center servers for executing the multiparty computation protocol, thereby escalating computational complexity and reducing system robustness, especially in scenarios where one or more sub-centers are unavailable. To address these challenges, we introduce a Markovian Switching-based distributed training framework, the convergence of which is substantiated through rigorous theoretical analysis. The Distributed Markovian Switching (DMS) topology shows strong robustness towards the poisoning attacks as well. Case studies employing real-world power system load data validate the efficacy of our proposed algorithm. It not only significantly minimizes communication complexity but also maintains accuracy levels comparable to traditional FL methods, thereby enhancing the scalability of our load forecasting algorithm.

  匹配依据：MPC: multiparty computation

  </details>

- **Real-Time Coordination of Integrated Transmission and Distribution Systems: Flexibility Modeling and Distributed NMPC Scheduling**
  2024-02-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.00508)
  Xinliang Dai, Yi Guo, Yuning Jiang, Colin N. Jones, Gabriela Hug, Veit Hagenmeyer

  <details><summary>摘要 / Abstract</summary>

  This paper proposes a real-time distributed operational architecture to efficiently coordinate intergrated transmission and distribution systems (ITD). At the distribution system level, the distribution system operator (DSO) computes the aggregated flexibility of all controllable devices by power-energy envelopes and provides them to the transmission system operators. At the transmission system level, a distributed nonlinear MPC approach is proposed to coordinate the economic dispatch of multiple TSOs, considering the aggregated flexibility of all distribution systems. The subproblems of the proposed approach are associated with different TSOs and individual time periods. In addition, the aggregated flexibility of controllable devices in distribution networks is encapsulated, re-calculated, and communicated through the power-energy envelopes, facilitating a reduction in computational complexity and eliminating redundant information exchanges between TSOs and DSOs, thereby enhancing privacy and security. The framework&#x27;s effectiveness and applicability in real-world scenarios are validated through simulated operational scenarios on a summer day in Germany, highlighting its robustness in the face of significant prediction mismatches due to severe weather conditions.

  匹配依据：MPC: mpc (context)

  </details>

- **Preliminary Cryptanalysis of the Biscuit Signature Scheme**
  2024-02-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/148)
  Charles Bouillaguet, Julia Sauvage

  <details><summary>摘要 / Abstract</summary>

  Biscuit is a recent multivariate signature scheme based on the MPC-in-the-Head paradigm. It has been submitted to the NIST competition for additional signature schemes. Signatures are derived from a zero-knowledge proof of knowledge of the solution of a structured polynomial system. This extra structure enables efficient proofs and compact signatures. This short note demonstrates that it also makes these polynomial systems easier to solve than random ones. As a consequence, the original parameters of Biscuit failed to meet the required security levels and had to be upgraded.

  匹配依据：MPC: mpc (context)

  </details>

- **Municipal cyber risk modeling using cryptographic computing to inform cyber policymaking**
  2024-02-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.01007)
  Avital Baral, Taylor Reynolds, Lawrence Susskind, Daniel J. Weitzner, Angelina Wu

  <details><summary>摘要 / Abstract</summary>

  Municipalities are vulnerable to cyberattacks with devastating consequences, but they lack key information to evaluate their own risk and compare their security posture to peers. Using data from 83 municipalities collected via a cryptographically secure computation platform about their security posture, incidents, security control failures, and losses, we build data-driven cyber risk models and cyber security benchmarks for municipalities. We produce benchmarks of the security posture in a sector, the frequency of cyber incidents, forecasted annual losses for organizations based on their defensive posture, and a weighting of cyber controls based on their individual failure rates and associated losses. Combined, these four items can help guide cyber policymaking by quantifying the cyber risk in a sector, identifying gaps that need to be addressed, prioritizing policy interventions, and tracking progress of those interventions over time. In the case of the municipalities, these newly derived risk measures highlight the need for continuous measured improvement of cybersecurity readiness, show clear areas of weakness and strength, and provide governments with some early targets for policy focus such as security education, incident response, and focusing efforts first on municipalities at the lowest security levels that have the highest risk reduction per security dollar invested.

  匹配依据：MPC: secure computation

  </details>

- **Quantum-Secure Hybrid Blockchain System for DID-based Verifiable Random Function with NTRU Linkable Ring Signature**
  2024-01-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.16906)
  Bong Gon Kim, Dennis Wong, Yoon Seok Yang

  <details><summary>摘要 / Abstract</summary>

  In this study, we present a secure smart contract-based Verifiable Random Function (VRF) model, addressing the shortcomings of existing systems. As quantum computing emerges, conventional public key cryptography faces potential vulnerabilities. To enhance our VRF&#x27;s robustness, we employ post-quantum Ring-LWE encryption for generating pseudo-random sequences. Given the computational intensity of this approach and associated on-chain gas costs, we propose a hybrid architecture of VRF system where on-chain and off-chain can communicate in a scalable and secure way. To ensure the validity and integrity of the off-chain computations (e.g., Ring-LWE encryption), we employ a quantum-secure linkable ring signature scheme on NTRU lattice and also delegated key generation (DKG) with a secure key encapsulation mechanism (KEM). Our decentralized VRF employs multi-party computation (MPC) with blockchain-based decentralized identifiers (DID), ensuring the collective efforts of enhanced randomness and security. We show the security and privacy advantages of our proposed VRF model with the approximated estimation of overall temporal and spatial complexities. We also evaluate our VRF MPC model&#x27;s entropy and outline its Solidity smart contract integration. This research also provides a method to produce and verify the VRF output&#x27;s proof, optimal for scenarios necessitating randomness and validation. Lastly, using NIST SP800-22 test suite for randomness, we demonstrate the commendable result with a 97.73% overall pass rate on 11 standard tests and 0.5459 of average p-value for the total 176 tests.

  匹配依据：MPC: multi party computation

  </details>

- **Flash: A Hybrid Private Inference Protocol for Deep CNNs with High Accuracy and Low Latency on CPU**
  2024-01-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.16732)
  Hyeri Roh, Jinsu Yeo, Yeongil Ko, Gu-Yeon Wei, David Brooks, Woo-Seok Choi

  <details><summary>摘要 / Abstract</summary>

  This paper presents Flash, an optimized private inference (PI) hybrid protocol utilizing both homomorphic encryption (HE) and secure two-party computation (2PC), which can reduce the end-to-end PI latency for deep CNN models less than 1 minute with CPU. To this end, first, Flash proposes a low-latency convolution algorithm built upon a fast slot rotation operation and a novel data encoding scheme, which results in 4-94x performance gain over the state-of-the-art. Second, to minimize the communication cost introduced by the standard nonlinear activation function ReLU, Flash replaces the entire ReLUs with the polynomial $x^2+x$ and trains deep CNN models with the new training strategy. The trained models improve the inference accuracy for CIFAR-10/100 and TinyImageNet by 16% on average (up to 40% for ResNet-32) compared to prior art. Last, Flash proposes an efficient 2PC-based $x^2+x$ evaluation protocol that does not require any offline communication and that reduces the total communication cost to process the activation layer by 84-196x over the state-of-the-art. As a result, the end-to-end PI latency of Flash implemented on CPU is 0.02 minute for CIFAR-100 and 0.57 minute for TinyImageNet classification, while the total data communication is 0.07GB for CIFAR-100 and 0.22GB for TinyImageNet. Flash improves the state-of-the-art PI by 16-45x in latency and 84-196x in communication cost. Moreover, even for ImageNet, Flash can deliver the latency less than 1 minute on CPU with the total communication less than 1GB.

  匹配依据：MPC: secure two party computation

  </details>

- **HEQuant: Marrying Homomorphic Encryption and Quantization for Communication-Efficient Private Inference**
  2024-01-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2401.15970)
  Tianshi Xu, Meng Li, Runsheng Wang

  <details><summary>摘要 / Abstract</summary>

  Secure two-party computation with homomorphic encryption (HE) protects data privacy with a formal security guarantee but suffers from high communication overhead. While previous works, e.g., Cheetah, Iron, etc, have proposed efficient HE-based protocols for different neural network (NN) operations, they still assume high precision, e.g., fixed point 37 bit, for the NN operations and ignore NNs&#x27; native robustness against quantization error. In this paper, we propose HEQuant, which features low-precision-quantization-aware optimization for the HE-based protocols. We observe the benefit of a naive combination of quantization and HE quickly saturates as bit precision goes down. Hence, to further improve communication efficiency, we propose a series of optimizations, including an intra-coefficient packing algorithm and a quantization-aware tiling algorithm, to simultaneously reduce the number and precision of the transferred data. Compared with prior-art HE-based protocols, e.g., CrypTFlow2, Cheetah, Iron, etc, HEQuant achieves $3.5\sim 23.4\times$ communication reduction and $3.0\sim 9.3\times$ latency reduction. Meanwhile, when compared with prior-art network optimization frameworks, e.g., SENet, SNL, etc, HEQuant also achieves $3.1\sim 3.6\times$ communication reduction.

  匹配依据：MPC: secure two party computation

  </details>
