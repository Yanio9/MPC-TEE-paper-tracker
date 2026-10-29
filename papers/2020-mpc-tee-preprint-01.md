# 2020 · MPC + TEE · 仅预印本来源 · 第 1/1 页

[总目录](../PAPERS.md)

- **PCT-TEE: Trajectory-based Private Contact Tracing System with Trusted Execution Environment**
  2020-12-07 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2012.03782)
  Fumiyuki Kato, Yang Cao, Masatoshi Yoshikawa

  <details><summary>摘要 / Abstract</summary>

  Existing Bluetooth-based Private Contact Tracing (PCT) systems can privately detect whether people have come into direct contact with COVID-19 patients. However, we find that the existing systems lack functionality and flexibility, which may hurt the success of the contact tracing. Specifically, they cannot detect indirect contact (e.g., people may be exposed to coronavirus because of used the same elevator even without direct contact); they also cannot flexibly change the rules of &quot;risky contact&quot;, such as how many hours of exposure or how close to a COVID-19 patient that is considered as risk exposure, which may be changed with the environmental situation. In this paper, we propose an efficient and secure contact tracing system that enables both direct contact and indirect contact. To address the above problems, we need to utilize users&#x27; trajectory data for private contact tracing, which we call trajectory-based PCT. We formalize this problem as Spatiotemporal Private Set Intersection. By analyzing different approaches such as homomorphic encryption that could be extended to solve this problem, we identify that Trusted Execution Environment (TEE) is a proposing method to achieve our requirements. The major challenge is how to design algorithms for spatiotemporal private set intersection under limited secure memory of TEE. To this end, we design a TEE-based system with flexible trajectory data encoding algorithms. Our experiments on real-world data show that the proposed system can process thousands of queries on tens of million records of trajectory data in a few seconds.

  匹配依据：MPC: private set intersection; TEE: trusted execution environment

  </details>

- **A Systematic Comparison of Encrypted Machine Learning Solutions for Image Classification**
  2020-11-10 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2011.05296)
  Veneta Haralampieva, Daniel Rueckert, Jonathan Passerat-Palmbach

  <details><summary>摘要 / Abstract</summary>

  This work provides a comprehensive review of existing frameworks based on secure computing techniques in the context of private image classification. The in-depth analysis of these approaches is followed by careful examination of their performance costs, in particular runtime and communication overhead. To further illustrate the practical considerations when using different privacy-preserving technologies, experiments were conducted using four state-of-the-art libraries implementing secure computing at the heart of the data science stack: PySyft and CrypTen supporting private inference via Secure Multi-Party Computation, TF-Trusted utilising Trusted Execution Environments and HE- Transformer relying on Homomorphic encryption. Our work aims to evaluate the suitability of these frameworks from a usability, runtime requirements and accuracy point of view. In order to better understand the gap between state-of-the-art protocols and what is currently available in practice for a data scientist, we designed three neural network architecture to obtain secure predictions via each of the four aforementioned frameworks. Two networks were evaluated on the MNIST dataset and one on the Malaria Cell image dataset. We observed satisfying performances for TF-Trusted and CrypTen and noted that all frameworks perfectly preserved the accuracy of the corresponding plaintext model.

  匹配依据：MPC: secure computing, secure multi party computation; TEE: trusted execution environments

  </details>

- **Secure and Efficient Trajectory-Based Contact Tracing using Trusted Hardware**
  2020-10-26 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2010.13381)
  Fumiyuki Kato, Yang Cao, Masatoshi Yoshikawa

  <details><summary>摘要 / Abstract</summary>

  The COVID-19 pandemic has prompted technological measures to control the spread of the disease. Private contact tracing (PCT) is one of the promising techniques for the purpose. However, the recently proposed Bluetooth-based PCT has several limitations in terms of functionality and flexibility. The existing systems are only able to detect direct contact (i.e., human-human contact), but cannot detect indirect contact (i.e., human-object, such as the disease transmission through surface). Moreover, the rule of risky contact cannot be flexibly changed with the environmental situation and the nature of the virus. In this paper, we propose a secure and efficient trajectory-based PCT system using trusted hardware. We formalize trajectory-based PCT as a generalization of the well-studied Private Set Intersection (PSI), which is mostly based on cryptographic primitives and thus insufficient. We solve the problem by leveraging trusted hardware such as Intel SGX and designing a novel algorithm to achieve a secure, efficient and flexible PCT system. Our experiments on real-world data show that the proposed system can achieve high performance and scalability. Specifically, our system (one single machine with Intel SGX) can process thousands of queries on 100 million records of trajectory data in a few seconds.

  匹配依据：MPC: private set intersection; TEE: intel sgx

  </details>

- **Correlated Randomness Teleportation via Semi-trusted Hardware - Enabling Silent Multi-party Computation**
  2020-10-14 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1259)
  Yibiao Lu, Bingsheng Zhang, Hong-Sheng Zhou, Weiran Liu, Lei Zhang, Kui Ren

  <details><summary>摘要 / Abstract</summary>

  With the advancement of the trusted execution environment (TEE) technologies, hardware-supported secure computing becomes increasingly popular due to its efficiency. During the protocol execution, typically, the players need to contact a third-party server for remote attestation, ensuring the validity of the involved trusted hardware component, such as Intel SGX, as well as the integrity of the computation result. When the hardware manufacturer is not fully trusted, sensitive information may be leaked to the third-party server through backdoors, steganography, and kleptography, etc. In this work, we introduce a new security notion called semi-trusted hardware model, where the adversary is allowed to passively or maliciously corrupt the hardware. Therefore, she can learn the input of the hardware component and might also tamper its output. We then show how to utilize such semi-trusted hardwares for correlated randomness teleportation. When the semi-trusted hardware is instantiated by Intel SGX, to generate 10k random OT&#x27;s, our protocol is 24X and 450X faster than the EMP-IKNP-ROT in the LAN and WAN setting, respectively. When SGX is used to teleport garbled circuits, the resulting two-party computation protocol is 5.3-5.7X and 43-47X faster than the EMP-SH2PC in the LAN and WAN setting, respectively, for the AES-128, SHA-256, and SHA-512 evaluation. We also show how to achieve malicious security with little overhead.

  匹配依据：MPC: garbled circuits, multi party computation, secure computing, two party computation; TEE: intel sgx, sgx, trusted execution environment

  </details>

- **(F)unctional Sifting: A Privacy-Preserving Reputation System Through Multi-Input Functional Encryption (extended version)**
  2020-10-14 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/1271)
  Alexandros Bakas, Antonis Michalas

  <details><summary>摘要 / Abstract</summary>

  Functional Encryption (FE) allows users who hold a specific secret key (known as the functional key) to learn a specific function of encrypted data whilst learning nothing about the content of the underlying data. Considering this functionality and the fact that the field of FE is still in its infancy, we sought a route to apply this potent tool to solve the existing problem of designing decentralised additive reputation systems. To this end, we first built a symmetric FE scheme for the $\ell_1$ norm of a vector space, which allows us to compute the sum of the components of an encrypted vector (i.e. the votes). Then, we utilized our construction, along with functionalities offered by Intel SGX, to design the first FE-based decentralized additive reputation system with Multi-Party Computation. While our reputation system faces certain limitations, this work is amongst the first attempts that seek to utilize FE in the solution of a real-life problem.

  匹配依据：MPC: multi party computation; TEE: intel sgx

  </details>

- **SAFE: A Secure and Efficient Long-Term Distributed Storage System**
  2020-06-09 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/690)
  Johannes Buchmann, Ghada Dessouky, Tommaso Frassetto, Ágnes Kiss, Ahmad-Reza Sadeghi, Thomas Schneider, Giulia Traverso, Shaza Zeitouni

  <details><summary>摘要 / Abstract</summary>

  Secret sharing-based distributed storage systems are one approach to provide long-term protection of data even against quantum computing. Confidentiality is provided because the shares of data are renewed periodically while integrity is provided by commitment schemes. However, this solution is prohibitively costly and impractical: share renewal requires an information-theoretically secure channel between any two nodes and long-term confidential commitment schemes are computationally impractical for large files. In this paper, we present SAFE, a secret sharing-based long-term secure distributed storage system that leverages a Trusted Execution Environment (TEE) to overcome the above limitations. Share generation and renewal are performed inside the TEE and the shares are securely distributed to the storage servers. We prototype SAFE protocols using a TEE instantiation, and show their efficiency, even for large files, compared to existing schemes.

  匹配依据：MPC: secret sharing; TEE: trusted execution environment

  </details>

- **Efficient Oblivious Database Joins**
  2020-03-20 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2003.09481)
  Simeon Krastnikov, Florian Kerschbaum, Douglas Stebila

  <details><summary>摘要 / Abstract</summary>

  A major algorithmic challenge in designing applications intended for secure remote execution is ensuring that they are oblivious to their inputs, in the sense that their memory access patterns do not leak sensitive information to the server. This problem is particularly relevant to cloud databases that wish to allow queries over the client&#x27;s encrypted data. One of the major obstacles to such a goal is the join operator, which is non-trivial to implement obliviously without resorting to generic but inefficient solutions like Oblivious RAM (ORAM). We present an oblivious algorithm for equi-joins which (up to a logarithmic factor) matches the optimal $O(n\log n)$ complexity of the standard non-secure sort-merge join (on inputs producing $O(n)$ outputs). We do not use use expensive primitives like ORAM or rely on unrealistic hardware or security assumptions. Our approach, which is based on sorting networks and novel provably-oblivious constructions, is conceptually simple, easily verifiable, and very efficient in practice. Its data-independent algorithmic structure makes it secure in various different settings for remote computation, even in those that are known to be vulnerable to certain side-channel attacks (such as Intel SGX) or with strict requirements for low circuit complexity (like secure multiparty computation). We confirm that our approach is easily realizable through a compact implementation which matches our expectations for performance and is shown, both formally and empirically, to possess the desired security characteristics.

  匹配依据：MPC: secure multiparty computation; TEE: intel sgx

  </details>

- **Efficient and Fair Multiparty Protocols using Blockchain and Trusted Hardware**
  2020-02-10 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2020/133)
  Souradyuti Paul, Ananya Shrivastava

  <details><summary>摘要 / Abstract</summary>

  In ACM CCS&#x27;17, Choudhuri et al. designed two fair public-ledger-based multi-party protocols (in the malicious model with dishonest majority) for computing an arbitrary function $f$. One of their protocols is based on a trusted hardware enclave $G$ (which can be implemented using Intel SGX-hardware) and a public ledger (which can be implemented using a blockchain platform, such as Ethereum). Subsequently, in NDSS&#x27;19, a stateless version of the protocol was published. This is the first time, (a certain definition of) fairness -- that guarantees either all parties learn the final output or nobody does -- is achieved without any monetary or computational penalties. However, these protocols are fair, if the underlying core MPC component guarantees both privacy and correctness. While privacy is easy to achieve (using a secret sharing scheme), correctness requires expensive operations (such as ZK proofs and commitment schemes). We improve on this work in three different directions: attack, design and performance. Our first major contribution is building practical attacks that demonstrate: if correctness is not satisfied then the fairness property of the aforementioned protocols collapse. Next, we design two new protocols -- stateful and stateless -- based on public ledger and trusted hardware that are: resistant against the aforementioned attacks, and made several orders of magnitude more efficient (related to both time and memory) than the existing ones by eliminating ZK proofs and commitment schemes in the design. Last but not the least, we implemented the core MPC part of our protocols using the SPDZ-2 framework to demonstrate the feasibility of its practical implementation.

  匹配依据：MPC: secret sharing; TEE: hardware enclave, intel sgx

  </details>
