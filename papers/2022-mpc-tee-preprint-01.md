# 2022 · MPC + TEE · 仅预印本来源 · 第 1/1 页

[总目录](../PAPERS.md)

- **ORTOA: One Round Trip Oblivious Access**
  2022-11-01 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1506)
  Sujaya Maiyya, Yuval Steinhart, Divyakant Agrawal, Prabhanjan Ananth, Amr El Abbadi

  <details><summary>摘要 / Abstract</summary>

  Many applications relying on cloud storage services typically encrypt their data to ensure data privacy. However, reading or writing the encrypted data to serve client requests reveals the type of client operation to a potentially untrusted cloud. An adversary can exploit this information leak to compromise a user’s privacy by tracking read/write access patterns. Existing approaches such as Oblivious RAM (ORAM) schemes hide the type of client access by always reading and then writing the data sequentially for both reads and writes, rendering one of these rounds redundant with respect to a client request. To mitigate this redundancy, we propose ORTOA- a family of protocols enabling single-round data access on remote storage without revealing the operation type. Specifically, we propose three protocols, two using existing cryptographic primitives of fully homomorphic encryption and trusted execution environments (TEEs), and a new primitive inspired by garbled circuits. Each of these protocols has different trust assumptions, allowing an application to choose the option best suited for its needs. To our knowledge, ORTOA is the first to propose generalized protocols to obfuscate the type of access in a single round, reducing the communication overhead in half. The proposed techniques can pave the way for novel ORAM schemes that hide both the type of access and the access pattern in a single round. Our experimental results show ORTOA achieving throughput gains of 1.7x-3.2x compared to a baseline requiring two rounds for access type concealment, with the baseline incurring latency 1.5-1.9x that of ORTOA for 160B-sized objects.

  匹配依据：MPC: garbled circuits; TEE: trusted execution environments

  </details>

- **Bool Network: An Open, Distributed, Secure Cross-chain Notary Platform**
  2022-09-28 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1290)
  Zeyuan Yin, Bingsheng Zhang, Jingzhong Xu, Kaiyu Lu, Kui Ren

  <details><summary>摘要 / Abstract</summary>

  With the advancement of blockchain technology, hundreds of cryptocurrencies have been deployed. The bloom of heterogeneous blockchain platforms brings a new emerging problem: typically, various blockchains are isolated systems, how to securely identify and/or transfer digital properties across blockchains? There are three main kinds of cross-chain approaches: sidechains/relays, notaries, and hashed time-lock contracts. Among them, notary-based cross-chain solutions have the best compatibility and user-friendliness, but they are typically centralized. To resolve this issue, we present Bool Network -- an open, distributed, secure cross-chain notary platform powered by MPC-based distributed key management over evolving hidden committees. More specifically, to protect the identities of the committee members, we propose a Ring verifiable random function (Ring VRF) protocol, where the real public key of a VRF instance can be hidden among a ring, which may be of independent interest to other cryptographic protocols. Furthermore, all the key management procedures are executed in the TEE, such as Intel SGX, to ensure the privacy and integrity of partial key components. A prototype of the proposed Bool Network is implemented in Rust language, using Polkadot Substrate.

  匹配依据：MPC: mpc (context); TEE: intel sgx

  </details>

- **CoVault: A Secure Analytics Platform**
  2022-08-07 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2208.03784)
  Roberta De Viti, Isaac Sheff, Noemi Glaeser, Baltasar Dinis, Rodrigo Rodrigues, Bobby Bhattacharjee, Anwar Hithnawi, Deepak Garg, Peter Druschel

  <details><summary>摘要 / Abstract</summary>

  Analytics on personal data, such as individuals&#x27; mobility, financial, and health data can be of significant benefit to society. Such data is already collected by smartphones, apps and services today, but liberal societies have so far refrained from making it available for large-scale analytics. Arguably, this is due at least in part to the lack of an analytics platform that can secure data through transparent, technical means (ideally with decentralized trust), enforce source policies, handle millions of distinct data sources, and run queries on billions of records with acceptable query latencies. To bridge this gap, we present an analytics platform called CoVault which combines secure multi-party computation (MPC) with trusted execution environment (TEE)-based delegation of trust to be able execute approved queries on encrypted data contributed by individuals within a datacenter to achieve the above properties. We show that CoVault scales well despite the high cost of MPC. For example, CoVault can process data relevant to epidemic analytics for a country of 80M people (about 11.85B data records/day) on a continuous basis using a core pair for every 20,000 people. Compared to a state-of-the-art MPC-based platform, CoVault can process queries between 7 to over 100 times faster, as well as scale to many sources and big data.

  匹配依据：MPC: secure multi party computation; TEE: trusted execution environment

  </details>

- **Paras - A Private NFT Protocol**
  2022-07-30 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/976)
  Vanishree Rao

  <details><summary>摘要 / Abstract</summary>

  Non-fungible tokens (NFTs) are a blockchain application that has recently witnessed significant success. However, NFT marketplaces are majorly built on popular blockchain platforms that do not provide privacy tools. As a result, NFTs are easily visible to everyone. This has naturally given rise to various issues, including stolen/duplicate NFTs and attacks like shill trading. Furthermore, this architecture fails to reflect the real-life privacy notion as it digitizes unique physical goods. In this project, we build Paras - a blockchain-agnostic protocol that offers privacy to NFTs. Specifically, one may hide the real NFTs and only display a reference to them on marketplaces, hide seller and bidder identities, hide bid values and user wallet balances. Paras is based on cryptographic primitives, such as, threshold encryption and robust secret sharing. It does not rely on any trusted execution environments for security, unlike some existing protocols in this direction.

  匹配依据：MPC: secret sharing; TEE: trusted execution environments

  </details>

- **Towards Practical Privacy-Preserving Solution for Outsourced Neural Network Inference**
  2022-06-06 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2206.02384)
  Pinglan Liu, Wensheng Zhang

  <details><summary>摘要 / Abstract</summary>

  When neural network model and data are outsourced to cloud server for inference, it is desired to preserve the confidentiality of model and data as the involved parties (i.e., cloud server, model providing client and data providing client) may not trust mutually. Solutions were proposed based on multi-party computation, trusted execution environment (TEE) and leveled or fully homomorphic encryption (LHE/FHE), but their limitations hamper practical application. We propose a new framework based on synergistic integration of LHE and TEE, which enables collaboration among mutually-untrusted three parties, while minimizing the involvement of (relatively) resource-constrained TEE and allowing the full utilization of the untrusted but more resource-rich part of server. We also propose a generic and efficient LHE-based inference scheme as an important performance-determining component of the framework. We implemented/evaluated the proposed system on a moderate platform and show that, our proposed scheme is more applicable/scalable to various settings, and has better performance, compared to the state-of-the-art LHE-based solutions.

  匹配依据：MPC: multi party computation; TEE: trusted execution environment

  </details>

- **Training Differentially Private Models with Secure Multiparty Computation**
  2022-02-12 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2202.02625) · [IACR ePrint](https://eprint.iacr.org/2022/146)
  Sikha Pentyala, Davis Railsback, Ricardo Maia, Rafael Dowsley, David Melanson, Anderson Nascimento, Martine De Cock

  <details><summary>摘要 / Abstract</summary>

  We address the problem of learning a machine learning model from training data that originates at multiple data owners while providing formal privacy guarantees regarding the protection of each owner&#x27;s data. Existing solutions based on Differential Privacy (DP) achieve this at the cost of a drop in accuracy. Solutions based on Secure Multiparty Computation (MPC) do not incur such accuracy loss but leak information when the trained model is made publicly available. We propose an MPC solution for training DP models. Our solution relies on an MPC protocol for model training, and an MPC protocol for perturbing the trained model coefficients with Laplace noise in a privacy-preserving manner. The resulting MPC+DP approach achieves higher accuracy than a pure DP approach while providing the same formal privacy guarantees. Our work obtained first place in the iDASH2021 Track III competition on confidential computing for secure genome analysis.

  匹配依据：MPC: secure multiparty computation; TEE: confidential computing

  </details>
