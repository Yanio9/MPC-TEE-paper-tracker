# 2023 · MPC + TEE · 仅预印本来源 · 第 1/1 页

[总目录](../PAPERS.md)

- **Puppy: A Publicly Verifiable Watermarking Protocol**
  2023-12-14 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2312.09125)
  Devriş İşler, Seoyeon Hwang, Yoshimichi Nakatsuka, Nikolaos Laoutaris, Gene Tsudik

  <details><summary>摘要 / Abstract</summary>

  In this paper, we propose Puppy, the first formally defined framework for converting any symmetric watermarking into a publicly verifiable one. Puppy allows anyone to verify a watermark any number of times with the help of an untrusted third party, without requiring owner presence during detection. We formally define and prove security of Puppy using the ideal/real-world simulation paradigm and construct two practical and secure instances: (1) Puppy-TEE that uses Trusted Execution Environments (TEEs), and (2) Puppy-2PC that relies on two-party computation (2PC) based on garbled circuits. We then convert four current symmetric watermarking schemes into publicly verifiable ones and run extensive experiments using Puppy-TEE and Puppy-2PC. Evaluation results show that, while Puppy-TEE incurs some overhead, its total latency is on the order of milliseconds for three out of four watermarking schemes. Although the overhead of Puppy-2PC is higher (on the order of seconds), it is viable for settings that lack a TEE or where strong trust assumptions about a TEE need to be avoided. We further optimize the solution to increase its scalability and resilience to denial of service attacks via memoization.

  匹配依据：MPC: garbled circuits, two party computation; TEE: trusted execution environments

  </details>

- **Scalable and Privacy-Preserving Synthetic Data Generation on Decentralised Web**
  2023-10-30 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2310.20062)
  Vishal Ramesh, Rui Zhao, Naman Goel

  <details><summary>摘要 / Abstract</summary>

  Data on the Web has fueled much of the recent progress in AI. As more high-quality data becomes difficult to access, synthetic data is emerging as a promising solution for privacy-friendly data release and complementing real datasets in developing robust and safe AI. But there is limited work on decentralised, scalable and contributor-centric synthetic data generation systems. A recent proposal, called Libertas, allows data contributors to autonomously participate in joint computations over their Web data without relying on a trusted centre. Libertas uses Solid (Social Linked Data) and MPC (Secure Multi-Party Computation) to achieve this goal. Solid is a decentralised Web specification that lets anyone store their data securely in their personal decentralised data stores called Pods and control which applications have access to their data. MPC refers to the set of cryptographic methods for different parties to jointly compute a function over their inputs while keeping those inputs private. Thus, Libertas can also be used to generate synthetic data from otherwise inaccessible Web data in a responsible way, by ensuring contributor autonomy, decentralisation and privacy. However, the scalability of this system remains limited due to the high computation and communication costs in MPC. In this paper, we show how one can improve Libertas using secure enclaves (in addition to MPC) to address the scalability challenge. Secure enclaves such as Intel SGX rely on hardware based features for confidentiality and integrity of code and data. We discuss a principled approach for integrating SGX within the Libertas architecture for scalable differentially private synthetic data generation, and support our analysis with rigorous empirical results on simulated and real datasets and different synthetic data generation algorithms.

  匹配依据：MPC: secure multi party computation; TEE: intel sgx, secure enclaves, sgx

  </details>

- **TGh: A TEE/GC Hybrid Enabling Confidential FaaS Platforms**
  2023-09-14 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.07764) · [IACR ePrint](https://eprint.iacr.org/2023/829)
  James Choncholas, Ketan Bhardwaj, Ada Gavrilovska

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) suffer from performance issues when executing certain management instructions, such as creating an enclave, context switching in and out of protected mode, and swapping cached pages. This is especially problematic for short-running, interactive functions in Function-as-a-Service (FaaS) platforms, where existing techniques to address enclave overheads are insufficient. We find FaaS functions can spend more time managing the enclave than executing application instructions. In this work, we propose a TEE/GC hybrid (TGh) protocol to enable confidential FaaS platforms. TGh moves computation out of the enclave onto the untrusted host using garbled circuits (GC), a cryptographic construction for secure function evaluation. Our approach retains the security guarantees of enclaves while avoiding the performance issues associated with enclave management instructions.

  匹配依据：MPC: garbled circuits, secure function evaluation; TEE: trusted execution environments

  </details>

- **Janus: Safe Biometric Deduplication for Humanitarian Aid Distribution**
  2023-08-05 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.02907)
  Kasra EdalatNejad, Wouter Lueks, Justinas Sukaitis, Vincent Graf Narbel, Massimo Marelli, Carmela Troncoso

  <details><summary>摘要 / Abstract</summary>

  Humanitarian organizations provide aid to people in need. To use their limited budget efficiently, their distribution processes must ensure that legitimate recipients cannot receive more aid than they are entitled to. Thus, it is essential that recipients can register at most once per aid program. Taking the International Committee of the Red Cross&#x27;s aid distribution registration process as a use case, we identify the requirements to detect double registration without creating new risks for aid recipients. We then design Janus, which combines privacy-enhancing technologies with biometrics to prevent double registration in a safe manner. Janus does not create plaintext biometric databases and reveals only one bit of information at registration time (whether the user registering is present in the database or not). We implement and evaluate three instantiations of Janus based on secure multiparty computation, somewhat homomorphic encryption, and trusted execution environments. We demonstrate that they support the privacy, accuracy, and performance needs of humanitarian organizations. We compare Janus with existing alternatives and show it is the first system that provides the accuracy our scenario requires while providing strong protection.

  匹配依据：MPC: secure multiparty computation; TEE: trusted execution environments

  </details>

- **TimeClave: Oblivious In-enclave Time series Processing System**
  2023-06-29 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.16652)
  K. Bagher, S. Cui, X. Yuan, C. Rudolph, X. Yi

  <details><summary>摘要 / Abstract</summary>

  Cloud platforms are widely adopted by many systems, such as time series processing systems, to store and process massive amounts of sensitive time series data. Unfortunately, several incidents have shown that cloud platforms are vulnerable to internal and external attacks that lead to critical data breaches. Adopting cryptographic protocols such as homomorphic encryption and secure multi-party computation adds high computational and network overhead to query operations. We present TimeClave, a fully oblivious in-enclave time series processing system: TimeClave leverages Intel SGX to support aggregate statistics on time series with minimal memory consumption inside the enclave. To hide the access pattern inside the enclave, we introduce a non-blocking read-optimised ORAM named RoORAM. TimeClave integrates RoORAM to obliviously and securely handle client queries with high performance. With an aggregation time interval of $10s$, $2^{14}$ summarised data blocks and 8 aggregate functions, TimeClave run point query in $0.03ms$ and a range query of 50 intervals in $0.46ms$. Compared to the ORAM baseline, TimeClave achieves lower query latency by up to $2.5\times$ and up to $2\times$ throughput, with up to 22K queries per second.

  匹配依据：MPC: secure multi party computation; TEE: intel sgx

  </details>

- **How to Design Fair Protocols in the Multi-Blockchain Setting**
  2023-05-26 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/762)
  Sivanarayana Gaddam, Ranjit Kumaresan, Srinivasan Raghuraman, Rohit Sinha

  <details><summary>摘要 / Abstract</summary>

  Recently, there have been several proposals for secure computation with fair output delivery that require the use of a bulletin board abstraction (in addition to a trusted execution environment (TEE)). These proposals require all protocol participants to have read/write access to the bulletin board. These works envision the use of (public or permissioned) blockchains to implement the bulletin board abstractions. With the advent of consortium blockchains which place restrictions on who can read/write contents on the blockchain, it is not clear how to extend prior proposals to a setting where (1) not all parties have read/write access on a single consortium blockchain, and (2) not all parties prefer to post on a public blockchain. In this paper, we address the above by showing the first protocols for fair secure computation in the multi-blockchain setting. More concretely, in a $n$-party setting where at most $t &lt; n$ parties are corrupt, our protocol for fair secure computation works as long as (1) $t$ parties have access to a TEE (e.g., Intel SGX), and (2) each of the above $t$ parties are on some blockchain with each of the other parties. Furthermore, only these $t$ parties need write access on the blockchains. In an optimistic setting where parties behave honestly, our protocol runs completely off-chain.

  匹配依据：MPC: secure computation; TEE: intel sgx, trusted execution environment

  </details>

- **A Generative Framework for Low-Cost Result Validation of Machine Learning-as-a-Service Inference**
  2023-03-31 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.00083)
  Abhinav Kumar, Miguel A. Guirao Aguilera, Reza Tourani, Satyajayant Misra

  <details><summary>摘要 / Abstract</summary>

  The growing popularity of Machine Learning (ML) has led to its deployment in various sensitive domains, which has resulted in significant research focused on ML security and privacy. However, in some applications, such as Augmented/Virtual Reality, integrity verification of the outsourced ML tasks is more critical--a facet that has not received much attention. Existing solutions, such as multi-party computation and proof-based systems, impose significant computation overhead, which makes them unfit for real-time applications. We propose Fides, a novel framework for real-time integrity validation of ML-as-a-Service (MLaaS) inference. Fides features a novel and efficient distillation technique--Greedy Distillation Transfer Learning--that dynamically distills and fine-tunes a space and compute-efficient verification model for verifying the corresponding service model while running inside a trusted execution environment. Fides features a client-side attack detection model that uses statistical analysis and divergence measurements to identify, with a high likelihood, if the service model is under attack. Fides also offers a re-classification functionality that predicts the original class whenever an attack is identified. We devised a generative adversarial network framework for training the attack detection and re-classification models. The evaluation shows that Fides achieves an accuracy of up to 98% for attack detection and 94% for re-classification.

  匹配依据：MPC: multi party computation; TEE: trusted execution environment

  </details>

- **SGXonerated: Finding (and Partially Fixing) Privacy Flaws in TEE-based Smart Contract Platforms Without Breaking the TEE**
  2023-03-15 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/378)
  Nerla Jean-Louis, Yunqi Li, Yan Ji, Harjasleen Malvai, Thomas Yurek, Sylvain Bellemare, Andrew Miller

  <details><summary>摘要 / Abstract</summary>

  TEE-based smart contracts are an emerging blockchain architecture, offering fully programmable privacy with better performance than alternatives like secure multiparty computation. They can also support compatibility with existing smart contract languages, such that existing (plaintext) applications can be readily ported, picking up privacy enhancements automatically. While previous analysis of TEE-based smart contracts have focused on failures of TEE itself, we asked whether other aspects might be understudied. We focused on state consistency, a concern area highlighted by Li et al., as well as new concerns including access pattern leakage and software upgrade mechanisms. We carried out a code review of a cohort of four TEE-based smart contract platforms. These include Secret Network, the first to market with in-use applications, as well as Oasis, Phala, and Obscuro, which have at least released public test networks. The first and most broadly applicable result is that access pattern leakage occurs when handling persistent contract storage. On Secret Network, its fine-grained access pattern is catastrophic for the transaction privacy of SNIP-20 tokens. If ERC-20 tokens were naively ported to Oasis they would be similarly vulnerable; the others in the cohort leak coarse-grained information at approximately the page level (4 kilobytes). Improving and characterizing this will require adopting techniques from ORAMs or encrypted databases. Second, the importance of state consistency has been under-appreciated, in part because exploiting such vulnerabilities is thought to be impractical. We show they are fully practical by building a proof-of-concept tool that breaks all advertised privacy properties of SNIP-20 tokens, able to query the balance of individual accounts and the token amount of each transfer. We additionally demonstrate MEV attacks against the Sienna Swap application. As a final consequence of lacking state consistency, the developers have inadvertently introduced a decryption backdoor through their software upgrade process. We have helped the Secret developers mitigate this through a coordinated vulnerability disclosure, after which their state consistency should be roughly on par with the rest.

  匹配依据：MPC: secure multiparty computation; TEE: tee (context)

  </details>

- **A Survey of Secure Computation Using Trusted Execution Environments**
  2023-02-23 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.12150)
  Xiaoguo Li, Bowen Zhao, Guomin Yang, Tao Xiang, Jian Weng, Robert H. Deng

  <details><summary>摘要 / Abstract</summary>

  As an essential technology underpinning trusted computing, the trusted execution environment (TEE) allows one to launch computation tasks on both on- and off-premises data while assuring confidentiality and integrity. This article provides a systematic review and comparison of TEE-based secure computation protocols. We first propose a taxonomy that classifies secure computation protocols into three major categories, namely secure outsourced computation, secure distributed computation and secure multi-party computation. To enable a fair comparison of these protocols, we also present comprehensive assessment criteria with respect to four aspects: setting, methodology, security and performance. Based on these criteria, we review, discuss and compare the state-of-the-art TEE-based secure computation protocols for both general-purpose computation functions and special-purpose ones, such as privacy-preserving machine learning and encrypted database queries. To the best of our knowledge, this article is the first survey to review TEE-based secure computation protocols and the comprehensive comparison can serve as a guideline for selecting suitable protocols for deployment in practice. Finally, we also discuss several future research directions and challenges.

  匹配依据：MPC: secure computation, secure multi party computation; TEE: trusted execution environment, trusted execution environments

  </details>

- **Hardware Root-of-Trust implementations in Trusted Execution Environments**
  2023-02-22 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/251)
  Usman Ali, Hamza Omar, Chujiao Ma, Vaibhav Garg, Omer Khan

  <details><summary>摘要 / Abstract</summary>

  Hardware-based Root of Trust (HRT) is considered the gold standard for bootstrapping trust in secure computing. This paper analyzes HRT implementations across state-of-the-art TEEs and differentiates HRT implementation across two dimensions: 1) Security Properties &amp; Threats and 2) Hardware Capabilities. Later, this work analyzes and compares 1) Intel SGX, 2) ARM TrustZone, 3) NXP Trust Architecture, 4) AMD SEV, 5) Microsoft Pluton, and 6) Apple T2 HRTs in terms of threats, security properties, and capabilities.

  匹配依据：MPC: secure computing; TEE: amd sev, intel sgx, trusted execution environments, trustzone

  </details>

- **Individual Cryptography**
  2023-01-24 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/088)
  Stefan Dziembowski, Sebastian Faust, Tomasz Lizurej

  <details><summary>摘要 / Abstract</summary>

  We initiate a formal study of individual cryptography. Informally speaking, an algorithm $\mathsf{Alg}$ is &quot;individual&quot; if, in every implementation of $\mathsf{Alg}$, there always exists an individual user with full knowledge of the cryptographic data $S$ used by $\mathsf{Alg}$. In particular, it should be infeasible to design implementations of this algorithm that would hide $S$ by distributing it between a group of parties using an MPC protocol or outsourcing it to a trusted execution environment. We define and construct two primitives in this model. The first one, called &quot;proofs of individual knowledge&quot;, is a tool for proving that a given message is fully known to a single (&quot;individual&quot;) machine on the Internet, i.e., it cannot be shared between a group of parties. The second one, dubbed &quot;individual secret sharing&quot;, is a scheme for sharing a secret $S$ between a group of parties so that the parties have no knowledge of $S$ as long as they do not reconstruct it. The reconstruction ensures that if the shareholders attempt to collude, one of them will learn the secret entirely. Individual secret sharing has applications for preventing collusion in secret sharing. A central technique for constructing individual cryptographic primitives is the concept of MPC hardness. MPC hardness precludes an adversary from completing a cryptographic task in a distributed fashion within a specific time frame.

  匹配依据：MPC: secret sharing; TEE: trusted execution environment

  </details>

- **Complete Knowledge: Preventing Encumbrance of Cryptographic Secrets**
  2023-01-15 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/044)
  Mahimna Kelkar, Kushal Babel, Philip Daian, James Austgen, Vitalik Buterin, Ari Juels

  <details><summary>摘要 / Abstract</summary>

  Most cryptographic protocols model a player’s knowledge of secrets in a simple way. Informally, the player knows a secret in the sense that she can directly furnish it as a (private) input to a protocol, e.g., to digitally sign a message. The growing availability of Trusted Execution Environments (TEEs) and secure multiparty computation, however, undermines this model of knowledge. Such tools can encumber a secret sk and permit a chosen player to access sk conditionally, without actually knowing sk. By permitting selective access to sk by an adversary, encumbrance of secrets can enable vote-selling in cryptographic voting schemes, illegal sale of credentials for online services, and erosion of deniability in anonymous messaging systems. Unfortunately, existing proof-of-knowledge protocols fail to demonstrate that a secret is unencumbered. We therefore introduce and formalize a new notion called complete knowledge (CK). A proof (or argument) of CK shows that a prover does not just know a secret, but also has fully unencumbered knowledge, i.e., unrestricted ability to use the secret. We introduce two practical CK schemes that use special-purpose hardware, specifically TEEs and off-the-shelf mining ASICs. We prove the security of these schemes and explore their practical deployment with a complete, end-to-end prototype with smart-contract verification that supports both. We show how CK can address encumbrance attacks identified in previous work. Finally, we introduce two new applications enabled by CK that involve proving ownership of blockchain assets.

  匹配依据：MPC: secure multiparty computation; TEE: trusted execution environments

  </details>
