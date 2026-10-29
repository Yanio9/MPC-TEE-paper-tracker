# 2023 · MPC · 仅预印本来源 · 第 3/4 页

[总目录](../PAPERS.md) · [上一页](2023-mpc-preprint-02.md) · [下一页](2023-mpc-preprint-04.md)

- **PASNet: Polynomial Architecture Search Framework for Two-party Computation-based Secure Neural Network Deployment**
  2023-06-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.15513)
  Hongwu Peng, Shanglin Zhou, Yukui Luo, Nuo Xu, Shijin Duan, Ran Ran, Jiahui Zhao, Chenghong Wang, Tong Geng, Wujie Wen, Xiaolin Xu, Caiwen Ding

  <details><summary>摘要 / Abstract</summary>

  Two-party computation (2PC) is promising to enable privacy-preserving deep learning (DL). However, the 2PC-based privacy-preserving DL implementation comes with high comparison protocol overhead from the non-linear operators. This work presents PASNet, a novel systematic framework that enables low latency, high energy efficiency &amp; accuracy, and security-guaranteed 2PC-DL by integrating the hardware latency of the cryptographic building block into the neural architecture search loss function. We develop a cryptographic hardware scheduler and the corresponding performance model for Field Programmable Gate Arrays (FPGA) as a case study. The experimental results demonstrate that our light-weighted model PASNet-A and heavily-weighted model PASNet-B achieve 63 ms and 228 ms latency on private inference on ImageNet, which are 147 and 40 times faster than the SOTA CryptGPU system, and achieve 70.54% &amp; 78.79% accuracy and more than 1000 times higher energy efficiency.

  匹配依据：MPC: two party computation

  </details>

- **Oblivious Transfer from Rerandomizable PKE**
  2023-06-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1002)
  Shuaishuai Li, Cong Zhang, Dongdai Lin

  <details><summary>摘要 / Abstract</summary>

  The relationship between oblivious transfer (OT) and public-key encryption (PKE) has been studied by Gertner et al. (FOCS 2000). They showed that OT can be constructed from special types of PKE, i.e., PKE with oblivious sampleability of public keys or ciphertexts. In this work, we give new black-box constructions of OT from PKE without any oblivious sampleability. Instead, we require that the PKE scheme is rerandomizable, meaning that one can use the public key to rerandomize a ciphertext into a fresh ciphertext. We give two different OT protocols with different efficiency features based on rerandomizable PKE. For $1$-out-of-$n$ OT, in our first OT protocol, the sender has sublinear (in $n$) cost, and in our second OT protocol, the cost of the receiver is independent of $n$. As a comparison, in the PKE-based OT protocols of Gertner et al., both the sender and receiver have linear cost.

  匹配依据：MPC: oblivious transfer

  </details>

- **VSS from Distributed ZK Proofs and Applications**
  2023-06-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/992)
  Shahla Atapoor, Karim Baghery, Daniele Cozzo, Robi Pedersen

  <details><summary>摘要 / Abstract</summary>

  Non-Interactive Verifiable Secret Sharing (NI-VSS) is a technique for distributing a secret among a group of individuals in a verifiable manner, such that shareholders can verify the validity of their received share and only a specific number of them can access the secret. VSS is a fundamental tool in cryptography and distributed computing. In this paper, we present an extremely efficient NI-VSS scheme using Zero-Knowledge (ZK) proofs on secret shared data. While prior VSS schemes have implicitly used ZK proofs on secret shared data, we specifically use their formal definition recently provided by Boneh et al. in CRYPTO 2019. The proposed NI-VSS scheme uses a quantum random oracle and a quantum computationally hiding commitment scheme in a black-box manner, which ensures its ease of use, especially in post-quantum threshold protocols. Implementation results further solidify its practicality and superiority over current constructions. With the new VSS scheme, for parameter sets $(n, t)=(128, 63)$ and $(2048, 1023)$, a dealer can share a secret in less than $0.02$ and $2.0$ seconds, respectively, and shareholders can verify their shares in less than $0.4$ and $5.0$ milliseconds. Compared to the well-established Pedersen VSS scheme, for the same parameter sets, at the cost of slightly higher communication, the new scheme is respectively $22.5\times$ and $3.25\times$ faster in the sharing phase, and notably needs $271\times$ and $479\times$ less time in the verification. Leveraging the new NI-VSS scheme, we revisit several classic and PQ-secure threshold protocols and improve their efficiency. Our revisions led to more efficient versions of both the Pedersen DKG protocol and the GJKR threshold signature scheme. We show similar efficiency enhancements and improved resilience to malicious parties in isogeny-based DKG and threshold signature schemes. We think, due to its remarkable efficiency and ease of use, the new NI-VSS scheme can be a valuable tool for a wide range of threshold protocols.

  匹配依据：MPC: secret sharing

  </details>

- **Tiresias: Large Scale, Maliciously Secure Threshold Paillier**
  2023-06-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/998)
  Offir Friedman, Avichai Marmor, Dolev Mutzari, Yehonatan C. Scaly, Yuval Spiizer, Avishay Yanai

  <details><summary>摘要 / Abstract</summary>

  In the threshold version of Paillier&#x27;s encryption scheme, a set of parties collectively holds the secret decryption key through a secret sharing scheme. Whenever a ciphertext is to be decrypted, the parties send their decryption shares, which are then verified for correctness and combined into the plaintext. The scheme has been widely adopted in various applications, from secure voting to general purpose MPC protocols. However, among the handful existing proposals for a maliciously secure scheme, one must choose between an efficient implementation that relies on non-standard assumptions or a computationally expensive implementation that relies on widely acceptable assumptions. In this work, we show that one can enjoy the benefits of both worlds. Specifically, we adjust a scheme by Damgard et al. (Int. J. Inf. Secur. 2010) to get a practical distributed key generation (DKG). While the original scheme was only known to be secure under ad-hoc non-standard assumptions, we prove that the adjusted scheme is in fact secure under the decisional composite residuosity (DCR) assumption alone, required for the semantic security of the Pallier encryption scheme itself. This is possible thanks to a novel reduction technique, from the soundness of a zero-knowledge proof of equality of discrete logs, to the factoring problem. Furthermore, we use similar ideas to prove that batching techniques by Aditya et al. (ACNS 2004), which allows a prover to batch several statements into a single proof, can be applied to our adjusted scheme. This enables a batched threshold Paillier decryption in the fully distributed setting for the first time. Until now, verifying that a decryption share is correct was the bottleneck of threshold Paillier schemes and hindered real world deployments (unless one is willing to rely on a trusted dealer). Our work accumulates to shifting the bottleneck back to the plaintext reconstruction, just like in the semi-honest setting, and render threshold Paillier practical for the first time, supporting large scale deployments. We exemplify this shift by implementing the scheme and report our evaluation with up to 1000 parties, in the dishonest majority setting. For instance, over an EC2 C6i machine, we get a throughput of about 50 and 3.6 decryptions per second, when run over a network of 100 and 1000 parties, respectively.

  匹配依据：MPC: secret sharing

  </details>

- **Publicly Verifiable Zero-Knowledge and Post-Quantum Signatures From VOLE-in-the-Head**
  2023-06-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/996)
  Carsten Baum, Lennart Braun, Cyprien Delpech de Saint Guilhem, Michael Klooß, Emmanuela Orsini, Lawrence Roy, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  We present a new method for transforming zero-knowledge protocols in the designated verifier setting into public-coin protocols, which can be made non-interactive and publicly verifiable. Our transformation applies to a large class of ZK protocols based on oblivious transfer. In particular, we show that it can be applied to recent, fast protocols based on vector oblivious linear evaluation (VOLE), with a technique we call VOLE-in-the-head, upgrading these protocols to support public verifiability. Our resulting ZK protocols have linear proof size, and are simpler, smaller and faster than related approaches based on MPC-in-the-head. To build VOLE-in-the-head while supporting both binary circuits and large finite fields, we develop several new technical tools. One of these is a new proof of security for the SoftSpokenOT protocol (Crypto 2022), which generalizes it to produce certain types of VOLE correlations over large fields. Secondly, we present a new ZK protocol that is tailored to take advantage of this form of VOLE, which leads to a publicly verifiable VOLE-in-the-head protocol with only 2x more communication than the best, designated-verifier VOLE-based protocols. We analyze the soundness of our approach when made non-interactive using the Fiat-Shamir transform, using round-by-round soundness. As an application of the resulting NIZK, we present FAEST, a post-quantum signature scheme based on AES. FAEST is the first AES-based signature scheme to be smaller than SPHINCS+, with signature sizes between 5.6 and 6.6kB at the 128-bit security level. Compared with the smallest version of SPHINCS+ (7.9kB), FAEST verification is slower, but the signing times are between 8x and 40x faster.

  匹配依据：MPC: oblivious transfer

  </details>

- **Practical Privacy-Preserving Gaussian Process Regression via Secret Sharing**
  2023-06-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.14498)
  Jinglong Luo, Yehong Zhang, Jiaqi Zhang, Shuang Qin, Hui Wang, Yue Yu, Zenglin Xu

  <details><summary>摘要 / Abstract</summary>

  Gaussian process regression (GPR) is a non-parametric model that has been used in many real-world applications that involve sensitive personal data (e.g., healthcare, finance, etc.) from multiple data owners. To fully and securely exploit the value of different data sources, this paper proposes a privacy-preserving GPR method based on secret sharing (SS), a secure multi-party computation (SMPC) technique. In contrast to existing studies that protect the data privacy of GPR via homomorphic encryption, differential privacy, or federated learning, our proposed method is more practical and can be used to preserve the data privacy of both the model inputs and outputs for various data-sharing scenarios (e.g., horizontally/vertically-partitioned data). However, it is non-trivial to directly apply SS on the conventional GPR algorithm, as it includes some operations whose accuracy and/or efficiency have not been well-enhanced in the current SMPC protocol. To address this issue, we derive a new SS-based exponentiation operation through the idea of &#x27;confusion-correction&#x27; and construct an SS-based matrix inversion algorithm based on Cholesky decomposition. More importantly, we theoretically analyze the communication cost and the security of the proposed SS-based operations. Empirical results show that our proposed method can achieve reasonable accuracy and efficiency under the premise of preserving data privacy.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Fast ORAM with Server-aided Preprocessing and Pragmatic Privacy-Efficiency Trade-off**
  2023-06-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/991)
  Vladimir Kolesnikov, Stanislav Peceny, Ni Trieu, Xiao Wang

  <details><summary>摘要 / Abstract</summary>

  Data-dependent accesses to memory are necessary for many real-world applications, but their cost remains prohibitive in secure computation. Prior work either focused on minimizing the need for data-dependent access in these applications, or reduced its cost by improving oblivious RAM for secure computation (SC-ORAM). Despite extensive efforts to improve SC-ORAM, the most concretely efficient solutions still require $\approx0.7$s per access to arrays of $2^{30}$ entries. This plainly precludes using MPC in a number of settings. In this work, we take a pragmatic approach, exploring how concretely cheap MPC RAM access could be made if we are willing to allow one of the participants to learn the access pattern. We design a highly efficient Shared-Output Client-Server ORAM (SOCS-ORAM) that has constant overhead, uses one round trip of interaction per access, and whose access cost is independent of array size. SOCS-ORAM is useful in settings with hard performance constraints, where one party in the computation is more trust-worthy and is allowed to learn the RAM access pattern. Our SOCS-ORAM is assisted by a third helper party that helps initialize (and reinitialize, as needed) the protocol and is designed for the honest-majority semi-honest corruption model. We implement our construction in C++ and report its performance. For an array of length $2^{30}$ with $4$B entries, we communicate $13$B per access and take essentially no overhead beyond network latency.

  匹配依据：MPC: secure computation

  </details>

- **Detection of Password Reuse and Credential Stuffing: A Server-side Approach**
  2023-06-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/989)
  Sai Sandilya Konduru, Sweta Mishra

  <details><summary>摘要 / Abstract</summary>

  Considering password-based authentication technique, password memorability is a real challenge on users. Hence, password reuse across different web applications is a common trend among users which makes websites vulnerable to credential stuffing attack. A solution as password manager helps the users to create random passwords for different websites on the user machine. However, it has practical challenges. Password database breach detection is another related and challenging task. Among recent developments for breach detection, honeyword-based approach is much appreciated by the research community. However, honeyword generation itself is a challenging part of the solution. In this work, we propose i) Password Reuse Detection (PRD) protocol for detecting password reuse using a secure two party private set intersection; ii) Breach Detection (BD) protocol that detects credential stuffing attacks using two party private set inclusion protocol based on random oblivious transfer. Both the proposals are designed for the authentication servers of the respective applications and need communication between multiple websites following the work by wang et al. Through analysis we show that our PRD protocol is around 2.8 times faster, and space efficient than existing works for 5000 honeywords. Our near to real-time BD protcol is around 2 times faster than existing works.

  匹配依据：MPC: oblivious transfer, private set intersection

  </details>

- **HODOR: Shrinking Attack Surface on Node.js via System Call Limitation**
  2023-06-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.13984)
  Wenya Wang, Xingwei Lin, Jingyi Wang, Wang Gao, Dawu Gu, Wei Lv, Jiashui Wang

  <details><summary>摘要 / Abstract</summary>

  Node.js provides Node.js applications with system interaction capabilities using system calls. However, such convenience comes with a price, i.e., the attack surface of JavaScript arbitrary code execution (ACE) vulnerabilities is expanded to the system call level. There lies a noticeable gap between existing protection techniques in the JavaScript code level (either by code debloating or read-write-execute permission restriction) and a targeted defense for emerging critical system call level exploitation. To fill the gap, we design and implement HODOR, a lightweight runtime protection system based on enforcing precise system call restrictions when running a Node.js application. HODOR achieved this by addressing several nontrivialial technical challenges. First, HODOR requires to construct high-quality call graphs for both the Node.js application (in JavaScript) and its underlying Node.js framework (in JavaScript and C/C++). Specifically, HODOR incorporates several important optimizations in both the JavaScript and C/C++ level to improve the state-of-the-art tools for building more precise call graphs. Then, HODOR creates the main-thread whitelist and the thread-pool whitelist respectively containing the identified necessary system calls based on the call graphs mappings. Finally, with the whitelists, HODOR implements lightweight system call restriction using the Linux kernel feature Secure Computing Mode (seccomp) to shrink the attack surface. We utilize HODOR to protect 83 real-world Node.js applications compromised by arbitrary code/command execution attacks. HODOR could reduce the attack surface to 16.75% on average with negligible runtime overhead (i.e., &lt;3%).

  匹配依据：MPC: secure computing

  </details>

- **Efficient Private Multiset ID Protocols**
  2023-06-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/986)
  Cong Zhang, Weiran Liu, Bolin Ding, Dongdai Lin

  <details><summary>摘要 / Abstract</summary>

  Private-ID (PID) protocol enables two parties, each holding a private set of items, to privately compute a set of random universal identifiers (UID) corresponding to the records in the union of their sets, where each party additionally learns which UIDs correspond to which items in its set but not if they belong to the intersection or not. PID is very useful in the privacy computation of databases query, e.g. inner join and join for compute. Known PID protocols all assume the input of both parties is a set. In the case of join, a more common scenario is that one party&#x27;s primary key (unique) needs to join the other party&#x27;s foreign key (duplicate). How to construct an efficient Private Multiset ID (PMID) protocol to support the above \emph{key-foreign key join} remains open. We resolve this problem by constructing efficient PMID protocols from Oblivious PRF, Private Set Union, and a newly introduced primitive called Deterministic-Value Oblivious Programmable PRF (dv-OPPRF). We also propose some PMID applications, including Private Inner Join, Private Full Join, and Private Join for Compute. We implement our PMID protocols and state-of-the-art PID protocols as performance baselines. The experiments show that the performances of our PMID are almost the same as the state-of-the-art PIDs when we set the multiplicity $U_x = U_y = 1$. Our PMID protocols scale well when either $U_x &gt; 1$ or $U_y &gt; 1$. The performances also correctly reflect excessive data expansion when both $U_x, U_y &gt; 1$ for the more general \emph{cross join} case.

  匹配依据：MPC: private set union

  </details>

- **The Landscape of Computing Symmetric $n$-Variable Functions with $2n$ Cards**
  2023-06-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.13551)
  Suthee Ruangwises

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation using a physical deck of cards, often called card-based cryptography, has been extensively studied during the past decade. Card-based protocols to compute various Boolean functions have been developed. As each input bit is typically encoded by two cards, computing an $n$-variable Boolean function requires at least $2n$ cards. We are interested in optimal protocols that use exactly $2n$ cards. In particular, we focus on symmetric functions. In this paper, we formulate the problem of developing $2n$-card protocols to compute $n$-variable symmetric Boolean functions by classifying all such functions into several NPN-equivalence classes. We then summarize existing protocols that can compute some representative functions from these classes, and also solve some open problems in the cases $n=4$, 5, 6, and 7. In particular, we develop a protocol to compute a function $k$Mod3, which determines whether the sum of all inputs is congruent to $k$ modulo 3 ($k \in \{0,1,2\}$).

  匹配依据：MPC: secure multi party computation

  </details>

- **Practical and Efficient FHE-based MPC**
  2023-06-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/981)
  Nigel P. Smart

  <details><summary>摘要 / Abstract</summary>

  We present a reactive MPC protocol built from FHE which is robust in the presence of active adversaries. In addition the protocol enables reduced bandwidth via means of transciphering, and also enables more expressive/efficient programs via means of a $\mathsf{Declassify}$ operation. All sub-components of the protocol can be efficiently realised using existing technology. We prove our protocol secure in the UC framework.

  匹配依据：MPC: mpc (context)

  </details>

- **Timed Commitments Revisited**
  2023-06-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/977)
  Miguel Ambrona, Marc Beunardeau, Raphaël R. Toledo

  <details><summary>摘要 / Abstract</summary>

  Timed commitments (Boneh and Naor, CRYPTO 2000) are a variant of standard commitments which incorporates a forced opening mechanism that allows anyone to reveal the committed message, but not before a certain prescribed date. Timed commitments have a wide-range of applications such as contract signing, fair multi-party computation, sealed bid auctions or new blockchain applications such as preventing front-running or unbiased randomness generation. We revisit the notion of timed commitments and propose an alternative simplified definition. We also provide two new constructions of timed commitments with different trade-offs.

  匹配依据：MPC: multi party computation

  </details>

- **A new color image secret sharing protocol**
  2023-06-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.12107)
  José Ignacio Farrán, David Cerezo

  <details><summary>摘要 / Abstract</summary>

  Visual cryptography aims to protect images against their possible illegitimate use. Thus, one can cipher, hash, or add watermarks for protecting copyright, among others. In this paper we provide a new solution to the problem of secret sharing for the case when the secret is an image. Our method combines the Shamir scheme for secret sharing using finite fields of characteristic 2 with the CBC mode of operation of a secure symmetric cryptographic scheme like AES, so that the security relies on that of the mentioned techniques. The resulting shares have the same resolution as that of the original image. The idea of the method could be generalized to other multimedia formats like audio or video, adapting the method to the corresponding encoded information.

  匹配依据：MPC: secret sharing

  </details>

- **Lightweight Authentication of Web Data via Garble-Then-Prove**
  2023-06-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/964)
  Xiang Xie, Kang Yang, Xiao Wang, Yu Yu

  <details><summary>摘要 / Abstract</summary>

  Transport Layer Security (TLS) establishes an authenticated and confidential channel to deliver data for almost all Internet applications. A recent work (Zhang et al., CCS&#x27;20) proposed a protocol to prove the TLS payload to a third party, without any modification of TLS servers, while ensuring the privacy and originality of the data in the presence of malicious adversaries. However, it required maliciously secure Two-Party Computation (2PC) for generic circuits, leading to significant computational and communication overhead. This paper proposes the garble-then-prove technique to achieve the same security requirement without using any heavy mechanism like generic malicious 2PC. Our end-to-end implementation shows 14$\times$ improvement in communication and an order of magnitude improvement in computation over the state-of-the-art protocol. We also show worldwide performance when using our protocol to authenticate payload data from Coinbase and Twitter APIs. Finally, we propose an efficient gadget to privately convert the above authenticated TLS payload to additively homomorphic commitments so that the properties of the payload can be proven efficiently using zkSNARKs.

  匹配依据：MPC: secure two party computation

  </details>

- **A Survey of Multivariate Polynomial Commitment Schemes**
  2023-06-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.11383)
  Ihyun Nam

  <details><summary>摘要 / Abstract</summary>

  A commitment scheme is a cryptographic tool that allows one to commit to a hidden value, with the option to open it later at requested places without revealing the secret itself. Commitment schemes have important applications in zero-knowledge proofs and secure multi-party computation, just to name a few. This survey introduces a few multivariate polynomial commitment schemes that are built from a variety of mathematical structures. We study how Orion is constructed using hash functions; Dory, Bulletproofs, and Vampire using the inner-product argument; Signatures of Correct Computation using polynomial factoring; DARK and Dew using groups of unknown order; and Orion+ using a CP-SNARK. For each protocol, we prove its completeness and state its security assumptions.

  匹配依据：MPC: secure multi party computation

  </details>

- **Zombies and Ghosts: Optimal Byzantine Agreement in the Presence of Omission Faults**
  2023-06-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/954)
  Julian Loss, Gilad Stern

  <details><summary>摘要 / Abstract</summary>

  Studying the feasibility of Byzantine Agreement (BA) in realistic fault models is an important question in the area of distributed computing and cryptography. In this work, we revisit the mixed fault model with Byzantine (malicious) faults and omission faults put forth by Hauser, Maurer, and Zikas (TCC 2009), who showed that BA (and MPC) is possible with $t$ Byzantine faults, $s$ send faults (whose outgoing messages may be dropped) and $r$ receive faults (whose incoming messages may be lost) if $n&gt;3t+r+s$. We generalize their techniques and results by showing that BA is possible if $n&gt;2t+r+s$, given the availability of a cryptographic setup. Our protocol is the first to match the recent lower bound of Eldefrawy, Loss, and Terner (ACNS 2022) for this setting.

  匹配依据：MPC: mpc (context)

  </details>

- **Towards Generic MPC Compilers via Variable Instruction Set Architectures (VISAs)**
  2023-06-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/953)
  Yibin Yang, Stanislav Peceny, David Heath, Vladimir Kolesnikov

  <details><summary>摘要 / Abstract</summary>

  In MPC, we usually represent programs as circuits. This is a poor fit for programs that use complex control flow, as it is costly to compile control flow to circuits. This motivated prior work to emulate CPUs inside MPC. Emulated CPUs can run complex programs, but they introduce high overhead due to the need to evaluate not just the program, but also the machinery of the CPU, including fetching, decoding, and executing instructions, accessing RAM, etc. Thus, both circuits and CPU emulation seem a poor fit for general MPC. The former cannot scale to arbitrary programs; the latter incurs high per-operation overhead. We propose variable instruction set architectures (VISAs), an approach that inherits the best features of both circuits and CPU emulation. Unlike a CPU, a VISA machine repeatedly executes entire program fragments, not individual instructions. By considering larger building blocks, we avoid most of the machinery associated with CPU emulation: we directly handle each fragment as a circuit. We instantiated a VISA machine via garbled circuits (GC), yielding constant-round 2PC for arbitrary assembly programs. We use improved branching (Stacked Garbling, Heath and Kolesnikov, Crypto 2020) and recent Garbled RAM (GRAM) (Heath et al., Eurocrypt 2022). Composing these securely and efficiently is intricate, and is one of our main contributions. We implemented our approach and ran it on common programs, including Dijkstra&#x27;s and Knuth-Morris-Pratt. Our 2PC VISA machine executes assembly instructions at $300$Hz to $4000$Hz, depending on the target program. We significantly outperform the state-of-the-art CPU-based approach (Wang et al., ESORICS 2016, whose tool we re-benchmarked on our setup). We run in constant rounds, use $6\times$ less bandwidth, and run more than $40\times$ faster on a low-latency network. With $50$ms (resp. $100$ms) latency, we are $898\times$ (resp. $1585\times$) faster on the same setup. While our focus is MPC, the VISA model also benefits CPU-emulation-based Zero-Knowledge proof compilers, such as ZEE and EZEE (Heath et al., Oakland&#x27;21 and Yang et al., EuroS&amp;P&#x27;22).

  匹配依据：MPC: garbled circuits

  </details>

- **Correlated-Output Differential Privacy and Applications to Dark Pools**
  2023-06-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/943)
  James Hsin-yu Chiang, Bernardo David, Mariana Gama, Christian Janos Lebeda

  <details><summary>摘要 / Abstract</summary>

  In the classical setting of differential privacy, a privacy-preserving query is performed on a private database, after which the query result is released to the analyst; a differentially private query ensures that the presence of a single database entry is protected from the analyst’s view. In this work, we contribute the first definitional framework for differential privacy in the trusted curator setting; clients submit private inputs to the trusted curator, which then computes individual outputs privately returned to each client. The adversary is more powerful than the standard setting; it can corrupt up to n − 1 clients and subsequently decide inputs and learn outputs of corrupted parties. In this setting, the adversary also obtains leakage from the honest output that is correlated with a corrupted output. Standard differentially private mechanisms protect client inputs but do not mitigate output correlation leaking arbitrary client information, which can forfeit client privacy completely. We initiate the investigation of a novel notion of correlated output differential privacy to bound the leakage from output correlation in the trusted curator setting. We define the satisfaction of both standard and correlated-output differential privacy as round differential privacy and highlight the relevance of this novel privacy notion to all application domains in the trusted curator model. We explore round differential privacy in traditional “dark pool” market venues, which promise privacy-preserving trade execution to mitigate front-running; privately submitted trade orders and trade execution are kept private by the trusted venue operator. We observe that dark pools satisfy neither classic nor correlated-output differential privacy; in markets with low trade activity, the adversary may trivially observe recurring, honest trading patterns, and anticipate and front-run future trades. In response, we present the first round differentially private market mechanisms that formally mitigate information leakage from all trading activity of a user. This is achieved with fuzzy order matching, inspired by the standard randomized response mechanism; however, this also introduces a liquidity mismatch as buy and sell orders are not guaranteed to execute pairwise, thereby weakening output correlation; this mismatch is compensated for by a round differentially private liquidity provider mechanism, which freezes a noisy amount of assets from the liquidity provider for the duration of a privacy epoch, but leaves trader balances unaffected. We propose oblivious algorithms for realizing our proposed market mechanisms with secure multi-party computation (MPC) and implement these in the Scale-Mamba Framework using Shamir Secret Sharing based MPC. We demonstrate practical, round differentially private trading with comparable throughput as prior work implementing (traditional) dark pool algorithms in MPC; our experiments demonstrate practicality for both traditional finance and decentralized finance settings.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Quantum Secret Reconstruction**
  2023-06-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.08863)
  Ruihai Ma, Fei Gao, Song Lin

  <details><summary>摘要 / Abstract</summary>

  In addition to secret splitting, secret reconstruction is another important component of secret sharing. In this paper, the first quantum secret reconstruction protocol based on cluster states is proposed. Before the protocol, a classical secret is divided into multiple shares, which are distributed among shareholders via secret splitting. In the protocol, the dealer utilizes her secret to encrypt a private quantum state, and sends the encrypted state to a combiner chosen by her from the shareholders. With the help of other shareholders, the combiner utilizes the properties of cluster states to recover the privacy quantum state. It is shown that the proposed protocol is secure against several common attacks, including external and internal attacks. Compared with classical secret reconstruction protocols, this protocol not only achieves theoretical security of all shares, but also is more efficient due to reducing the distribution cost and computation cost. To demonstrate the feasibility of the protocol, a corresponding simulation quantum experiment is conducted on the IBM Q platform. Furthermore, in conjunction with quantum fingerprinting, it can be directly applied to achieve the task of multiple secrets sharing, because the classical shares can be reused in the proposed protocol.

  匹配依据：MPC: secret sharing

  </details>

- **Private Federated Frequency Estimation: Adapting to the Hardness of the Instance**
  2023-06-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.09396)
  Jingfeng Wu, Wennan Zhu, Peter Kairouz, Vladimir Braverman

  <details><summary>摘要 / Abstract</summary>

  In federated frequency estimation (FFE), multiple clients work together to estimate the frequencies of their collective data by communicating with a server that respects the privacy constraints of Secure Summation (SecSum), a cryptographic multi-party computation protocol that ensures that the server can only access the sum of client-held vectors. For single-round FFE, it is known that count sketching is nearly information-theoretically optimal for achieving the fundamental accuracy-communication trade-offs [Chen et al., 2022]. However, we show that under the more practical multi-round FEE setting, simple adaptations of count sketching are strictly sub-optimal, and we propose a novel hybrid sketching algorithm that is provably more accurate. We also address the following fundamental question: how should a practitioner set the sketch size in a way that adapts to the hardness of the underlying problem? We propose a two-phase approach that allows for the use of a smaller sketch size for simpler problems (e.g., near-sparse or light-tailed distributions). We conclude our work by showing how differential privacy can be added to our algorithm and verifying its superior performance through extensive experiments conducted on large-scale datasets.

  匹配依据：MPC: multi party computation

  </details>

- **An Efficient and Multi-private Key Secure Aggregation for Federated Learning**
  2023-06-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.08970)
  Xue Yang, Zifeng Liu, Xiaohu Tang, Rongxing Lu, Bo Liu

  <details><summary>摘要 / Abstract</summary>

  With the emergence of privacy leaks in federated learning, secure aggregation protocols that mainly adopt either homomorphic encryption or threshold secret sharing have been widely developed for federated learning to protect the privacy of the local training data of each client. However, these existing protocols suffer from many shortcomings, such as the dependence on a trusted third party, the vulnerability to clients being corrupted, low efficiency, the trade-off between security and fault tolerance, etc. To solve these disadvantages, we propose an efficient and multi-private key secure aggregation scheme for federated learning. Specifically, we skillfully modify the variant ElGamal encryption technique to achieve homomorphic addition operation, which has two important advantages: 1) The server and each client can freely select public and private keys without introducing a trust third party and 2) Compared to the variant ElGamal encryption, the plaintext space is relatively large, which is more suitable for the deep model. Besides, for the high dimensional deep model parameter, we introduce a super-increasing sequence to compress multi-dimensional data into 1-D, which can greatly reduce encryption and decryption times as well as communication for ciphertext transmission. Detailed security analyses show that our proposed scheme achieves the semantic security of both individual local gradients and the aggregated result while achieving optimal robustness in tolerating both client collusion and dropped clients. Extensive simulations demonstrate that the accuracy of our scheme is almost the same as the non-private approach, while the efficiency of our scheme is much better than the state-of-the-art homomorphic encryption-based secure aggregation schemes. More importantly, the efficiency advantages of our scheme will become increasingly prominent as the number of model parameters increases.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Password Cracking: How a Third Party Can Crack Our Password Hash Without Learning the Hash Value or the Cleartext**
  2023-06-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.08740)
  Norbert Tihanyi, Tamas Bisztray, Bertalan Borsos, Sebastien Raveau

  <details><summary>摘要 / Abstract</summary>

  Using the computational resources of an untrusted third party to crack a password hash can pose a high number of privacy and security risks. The act of revealing the hash digest could in itself negatively impact both the data subject who created the password, and the data controller who stores the hash digest. This paper solves this currently open problem by presenting a Privacy-Preserving Password Cracking protocol (3PC), that prevents the third party cracking server from learning any useful information about the hash digest, or the recovered cleartext. This is achieved by a tailored anonymity set of decoy hashes, based on the concept of predicate encryption, where we extend the definition of a predicate function, to evaluate the output of a one way hash function. The protocol allows the client to maintain plausible deniability where the real choice of hash digest cannot be proved, even by the client itself. The probabilistic information the server obtains during the cracking process can be calculated and minimized to a desired level. While in theory cracking a larger set of hashes would decrease computational speed, the 3PC protocol provides constant-time lookup on an arbitrary list size, bounded by the input/output operation per second (IOPS) capabilities of the third party server, thereby allowing the protocol to scale efficiently. We demonstrate these claims both theoretically and in practice, with a real-life use case implemented on an FPGA architecture.

  匹配依据：MPC: 3pc (context)

  </details>

- **Fast and Private Inference of Deep Neural Networks by Co-designing Activation Functions**
  2023-06-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.08538)
  Abdulrahman Diaa, Lucas Fenaux, Thomas Humphries, Marian Dietz, Faezeh Ebrahimianghazani, Bailey Kacsmar, Xinda Li, Nils Lukas, Rasoul Akhavan Mahdavi, Simon Oya, Ehsan Amjadian, Florian Kerschbaum

  <details><summary>摘要 / Abstract</summary>

  Machine Learning as a Service (MLaaS) is an increasingly popular design where a company with abundant computing resources trains a deep neural network and offers query access for tasks like image classification. The challenge with this design is that MLaaS requires the client to reveal their potentially sensitive queries to the company hosting the model. Multi-party computation (MPC) protects the client&#x27;s data by allowing encrypted inferences. However, current approaches suffer from prohibitively large inference times. The inference time bottleneck in MPC is the evaluation of non-linear layers such as ReLU activation functions. Motivated by the success of previous work co-designing machine learning and MPC, we develop an activation function co-design. We replace all ReLUs with a polynomial approximation and evaluate them with single-round MPC protocols, which give state-of-the-art inference times in wide-area networks. Furthermore, to address the accuracy issues previously encountered with polynomial activations, we propose a novel training algorithm that gives accuracy competitive with plaintext models. Our evaluation shows between $3$ and $110\times$ speedups in inference time on large models with up to $23$ million parameters while maintaining competitive inference accuracy.

  匹配依据：MPC: multi party computation

  </details>

- **Fairness and Privacy-Preserving in Federated Learning: A Survey**
  2023-06-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.08402)
  Taki Hasan Rafi, Faiza Anan Noor, Tahmid Hussain, Dong-Kyu Chae

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) as distributed machine learning has gained popularity as privacy-aware Machine Learning (ML) systems have emerged as a technique that prevents privacy leakage by building a global model and by conducting individualized training of decentralized edge clients on their own private data. The existing works, however, employ privacy mechanisms such as Secure Multiparty Computing (SMC), Differential Privacy (DP), etc. Which are immensely susceptible to interference, massive computational overhead, low accuracy, etc. With the increasingly broad deployment of FL systems, it is challenging to ensure fairness and maintain active client participation in FL systems. Very few works ensure reasonably satisfactory performances for the numerous diverse clients and fail to prevent potential bias against particular demographics in FL systems. The current efforts fail to strike a compromise between privacy, fairness, and model performance in FL systems and are vulnerable to a number of additional problems. In this paper, we provide a comprehensive survey stating the basic concepts of FL, the existing privacy challenges, techniques, and relevant works concerning privacy in FL. We also provide an extensive overview of the increasing fairness challenges, existing fairness notions, and the limited works that attempt both privacy and fairness in FL. By comprehensively describing the existing FL systems, we present the potential future directions pertaining to the challenges of privacy-preserving and fairness-aware FL systems.

  匹配依据：MPC: secure multiparty computing

  </details>

- **Weight hierarchies of 3-weight linear codes from two $p$-ary quadratic functions**
  2023-06-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.07516)
  Xiumei Li, Fei Li

  <details><summary>摘要 / Abstract</summary>

  The weight hierarchy of a linear code has been an important research topic in coding theory since Wei&#x27;s original work in 1991. Choosing $ D=\Big\{(x,y)\in \Big(\F_{p^{s_1}}\times\F_{p^{s_2}}\Big)\Big\backslash\{(0,0)\}: f(x)+g(y)=0\Big\}$ as a defining set , where $f(x),g(y)$ are quadratic forms over $\mathbb{F}_{p^{s_i}},i=1,2$, respectively, with values in $\F_p$, we construct a family of 3-weight $p$-ary linear codes and determine their weight distributions and weight hierarchies completely. Most of the codes can be used in secret sharing schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Public-Key Encryption with Quantum Keys**
  2023-06-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.07698) · [IACR ePrint](https://eprint.iacr.org/2023/877)
  Khashayar Barooti, Alex B. Grilo, Loïs Huguenin-Dumittan, Giulio Malavolta, Or Sattath, Quoc-Huy Vu, Michael Walter

  <details><summary>摘要 / Abstract</summary>

  In the framework of Impagliazzo&#x27;s five worlds, a distinction is often made between two worlds, one where public-key encryption exists (Cryptomania), and one in which only one-way functions exist (MiniCrypt). However, the boundaries between these worlds can change when quantum information is taken into account. Recent work has shown that quantum variants of oblivious transfer and multi-party computation, both primitives that are classically in Cryptomania, can be constructed from one-way functions, placing them in the realm of quantum MiniCrypt (the so-called MiniQCrypt). This naturally raises the following question: Is it possible to construct a quantum variant of public-key encryption, which is at the heart of Cryptomania, from one-way functions or potentially weaker assumptions? In this work, we initiate the formal study of the notion of quantum public-key encryption (qPKE), i.e., public-key encryption where keys are allowed to be quantum states. We propose new definitions of security and several constructions of qPKE based on the existence of one-way functions (OWF), or even weaker assumptions, such as pseudorandom function-like states (PRFS) and pseudorandom function-like states with proof of destruction (PRFSPD). Finally, to give a tight characterization of this primitive, we show that computational assumptions are necessary to build quantum public-key encryption. That is, we give a self-contained proof that no quantum public-key encryption scheme can provide information-theoretic security.

  匹配依据：MPC: multi party computation, oblivious transfer

  </details>

- **Efficient Card-Based Millionaires' Protocols via Non-Binary Input Encoding**
  2023-06-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/921)
  Koji Nuida

  <details><summary>摘要 / Abstract</summary>

  Comparison of integers, a traditional topic in secure multiparty computation since Yao&#x27;s pioneering work on &quot;Millionaires&#x27; Problem&quot; (FOCS 1982), is also well studied in card-based cryptography. For the problem, Miyahara et al. (Theoretical Computer Science, 2020) proposed a protocol using binary cards (i.e., cards with two kinds of symbols) that is highly efficient in terms of numbers of cards and shuffles, and its extension to number cards (i.e., cards with distinct symbols). In this paper, with a different design strategy which we name &quot;Tug-of-War technique&quot;, we propose new protocols based on binary cards and on number cards. For binary cards, our protocol improves the previous protocol asymptotically (in bit lengths of input integers) in terms of numbers of cards and shuffles when adopting ternary encoding of input integers. For number cards, at the cost of increasing the number of cards, our protocol improves the number of shuffles of the previous protocol even with binary encoding, and more with $q$-ary encoding where $q &gt; 2$.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Link Between the Differential Cryptanalysis and Linear Approximations over Finite Abelian Groups And Its Applications**
  2023-06-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/911)
  Zhongfeng Niu, Siwei Sun, Hailun Yan, Qi Wang

  <details><summary>摘要 / Abstract</summary>

  In recent years, progress in practical applications of multi-party computation (MPC), fully homomorphic encryption (FHE), and zero-knowledge proofs (ZKP) motivates people to explore symmetric-key cryptographic algorithms, as well as corresponding cryptanalysis techniques (such as differential cryptanalysis, linear cryptanalysis), over finite Abelian groups or prime fields $\mathbb{F}_p$ for large $p$. In this paper, we establish the links between linear cryptanalysis and differential cryptanalysis over general finite Abelian groups. As the first application, we revisit linear cryptanalysis and give general results of linear approximations over arbitrary finite Abelian groups. More precisely, we consider the {\em linearity}, which is the maximal non-trivial linear approximation, to characterize the resistance of a function against linear cryptanalysis.This thereby generalizes the work of Pott in 2004 and completes the generalization of Sidelnikov–Chabaud–Vaudenay’s bound from $\mathbb{F}_2^n$ to finite Abelian groups. As the second application, we give an exact expression for the correlation of differential-linear approximations over arbitrary finite Abelian groups ($\mathbb{F}_p^n$) under the sole assumption that the two parts of the cipher are independent of each other. In particular, we completely generalize the differential-linear cryptanalysis from $\mathbb{F}_2^n$ to arbitrary finite Abelian groups ($\mathbb{F}_p^n$).

  匹配依据：MPC: multi party computation

  </details>

- **Attribute-based Single Sign-On: Secure, Private, and Efficient**
  2023-06-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/915)
  Tore Kasper Frederiksen, Julia Hesse, Bertram Poettering, Patrick Towa

  <details><summary>摘要 / Abstract</summary>

  A Single Sign-On (SSO) system allows users to access different remote services while authenticating only once. SSO can greatly improve the usability and security of online activities by dispensing with the need to securely remember or store tens or hundreds of authentication secrets. On the downside, today&#x27;s SSO providers can track users&#x27; online behavior, and collect personal data that service providers want to see asserted before letting a user access their resources. In this work, we propose a new policy-based Single Sign-On service, i.e., a system that produces access tokens that are conditioned on the user&#x27;s attributes fulfilling a specified policy. Our solution is based on multi-party computation and threshold cryptography, and generates access tokens of standardized format. The central idea is to distribute the role of the SSO provider among several entities, in order to shield user attributes and access patterns from each individual entity. We provide a formal security model and analysis in the Universal Composability framework, against proactive adversaries. Our implementation and benchmarking show the practicality of our system for many real-world use cases.

  匹配依据：MPC: multi party computation

  </details>

- **Near-Optimal Oblivious Key-Value Stores for Efficient PSI, PSU and Volume-Hiding Multi-Maps**
  2023-06-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/903)
  Alexander Bienstock, Sarvar Patel, Joon Young Seo, Kevin Yeo

  <details><summary>摘要 / Abstract</summary>

  In this paper, we study oblivious key-value stores (OKVS) that enable encoding n key-value pairs into length $m$ encodings while hiding the input keys. The goal is to obtain high rate, $n/m$, with efficient encoding and decoding algorithms. We present $\mathsf{RB\text{-}OKVS}$ built on random band matrices that obtains near-optimal rates as high as 0.97 whereas prior works could only achieve rates up to 0.81 with similar encoding times. Using $\mathsf{RB\text{-}OKVS}$, we obtain state-of-the-art protocols for private set intersection (PSI) and union (PSU). Our semi-honest PSI has up to 12% smaller communication and 13% reductions in monetary cost with slightly larger computation. We also obtain similar improvements for both malicious and circuit PSI. For PSU, our protocol obtains improvements of up to 22% in communication, 40% in computation and 21% in monetary cost. In general, we obtain the most communication- and cost-efficient protocols for all the above primitives. Finally, we present the first connection between OKVS and volume-hiding encrypted multi-maps (VH-EMM) where the goal is to outsource storage of multi-maps while hiding the number of values associated with each key (i.e., volume). We present $\mathsf{RB\text{-}MM}$ with 16% smaller storage, 5x faster queries and 8x faster setup than prior works.

  匹配依据：MPC: private set intersection

  </details>

- **McFIL: Model Counting Functionality-Inherent Leakage**
  2023-06-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.05633)
  Maximilian Zinkus, Yinzhi Cao, Matthew Green

  <details><summary>摘要 / Abstract</summary>

  Protecting the confidentiality of private data and using it for useful collaboration have long been at odds. Modern cryptography is bridging this gap through rapid growth in secure protocols such as multi-party computation, fully-homomorphic encryption, and zero-knowledge proofs. However, even with provable indistinguishability or zero-knowledgeness, confidentiality loss from leakage inherent to the functionality may partially or even completely compromise secret values without ever falsifying proofs of security. In this work, we describe McFIL, an algorithmic approach and accompanying software implementation which automatically quantifies intrinsic leakage for a given functionality. Extending and generalizing the Chosen-Ciphertext attack framework of Beck et al. with a practical heuristic, our approach not only quantifies but maximizes functionality-inherent leakage using Maximum Model Counting within a SAT solver. As a result, McFIL automatically derives approximately-optimal adversary inputs that, when used in secure protocols, maximize information leakage of private values.

  匹配依据：MPC: multi party computation

  </details>

- **Differentially Private Selection from Secure Distributed Computing**
  2023-06-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.04564) · [IACR ePrint](https://eprint.iacr.org/2023/894)
  Ivan Damgård, Hannah Keller, Boel Nelson, Claudio Orlandi, Rasmus Pagh

  <details><summary>摘要 / Abstract</summary>

  Given a collection of vectors $\mathbf{x}^{(1)},\dots,\mathbf{x}^{(n)} \in \{0,1\}^d$, the selection problem asks to report the index of an &quot;approximately largest&quot; entry in $\mathbf{x}=\sum_{j=1}^n \mathbf{x}^{(j)}$. Selection abstracts a host of problems; in machine learning it can be used for hyperparameter tuning, feature selection, or to model empirical risk minimization. We study selection under differential privacy, where a released index guarantees privacy for individual vectors. Though selection can be solved with an excellent utility guarantee in the central model of differential privacy, the distributed setting where no single entity is trusted to aggregate the data lacks solutions. Specifically, strong privacy guarantees with high utility are offered in high trust settings, but not in low trust settings. For example, in the popular shuffle model of distributed differential privacy, there are strong lower bounds suggesting that the utility of the central model cannot be obtained. In this paper we design a protocol for differentially private selection in a trust setting similar to the shuffle model - with the crucial difference that our protocol tolerates corrupted servers while maintaining privacy. Our protocol uses techniques from secure multi-party computation (MPC) to implement a protocol that: (i) has utility on par with the best mechanisms in the central model, (ii) scales to large, distributed collections of high-dimensional vectors, and (iii) uses $k\geq 3$ servers that collaborate to compute the result, where the differential privacy guarantee holds assuming an honest majority. Since general-purpose MPC techniques are not sufficiently scalable, we propose a novel application of integer secret sharing, and evaluate the utility and efficiency of our protocol both theoretically and empirically. Our protocol is the first to demonstrate that large-scale differentially private selection is possible in a distributed setting.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Fully Robust Federated Submodel Learning in a Distributed Storage System**
  2023-06-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.05402)
  Zhusheng Wang, Sennur Ulukus

  <details><summary>摘要 / Abstract</summary>

  We consider the federated submodel learning (FSL) problem in a distributed storage system. In the FSL framework, the full learning model at the server side is divided into multiple submodels such that each selected client needs to download only the required submodel(s) and upload the corresponding update(s) in accordance with its local training data. The server comprises multiple independent databases and the full model is stored across these databases. An eavesdropper passively observes all the storage and listens to all the communicated data, of its controlled databases, to gain knowledge about the remote client data and the submodel information. In addition, a subset of databases may fail, negatively affecting the FSL process, as FSL process may take a non-negligible amount of time for large models. To resolve these two issues together (i.e., security and database repair), we propose a novel coding mechanism coined ramp secure regenerating coding (RSRC), to store the full model in a distributed manner. Using our new RSRC method, the eavesdropper is permitted to learn a controllable amount of submodel information for the sake of reducing the communication and storage costs. Further, during the database repair process, in the construction of the replacement database, the submodels to be updated are stored in the form of their latest version from updating clients, while the remaining submodels are obtained from the previous version in other databases through routing clients. Our new RSRC-based distributed FSL approach is constructed on top of our earlier two-database FSL scheme which uses private set union (PSU). A complete one-round FSL process consists of FSL-PSU phase, FSL-write phase and additional auxiliary phases. Our proposed FSL scheme is also robust against database drop-outs, client drop-outs, client late-arrivals and an active adversary controlling databases.

  匹配依据：MPC: private set union

  </details>

- **Expand-Convolute Codes for Pseudorandom Correlation Generators from LPN**
  2023-06-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/882)
  Srinivasan Raghuraman, Peter Rindal, Titouan Tanguy

  <details><summary>摘要 / Abstract</summary>

  The recent development of pseudorandom correlation generators (PCG) holds tremendous promise for highly efficient MPC protocols. Among other correlations, PCGs allow for the efficient generation of oblivious transfer (OT) and vector oblivious linear evaluations (VOLE) with sublinear communication and concretely good computational overhead. This type of PCG makes use of a so-called LPN-friendly error-correcting code. That is, for large dimensions the code should have very efficient encoding and have high minimum distance. We investigate existing LPN-friendly codes and find that several candidates are less secure than was believed. Beginning with the recent expand-accumulate codes, we find that for their aggressive parameters, aimed at good concrete efficiency, they achieve a smaller [pseudo] minimum distance than conjectured. This decreases the resulting security parameter of the PCG but it remains unclear by how much. We additionally show that the recently proposed and extremely efficient silver codes achieve only very small minimum distance and result in concretely efficient attacks on the resulting PCG protocol. As such, silver codes should not be used. We introduce a new LPN-friendly code which we call \emph{expand-convolute}. These codes have provably high minimum distance and faster encoding time than suitable alternatives, e.g. expand-accumulate. The main contribution of these codes is the introduction of a convolution step that dramatically increases the minimum distance. This in turn allows for a more efficient parameter selection which results in improved concrete performance. In particular, we observe a 3 times improvement in running time for a comparable security level.

  匹配依据：MPC: oblivious transfer

  </details>

- **SoK: Vector OLE-Based Zero-Knowledge Protocols**
  2023-06-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/857)
  Carsten Baum, Samuel Dittmer, Peter Scholl, Xiao Wang

  <details><summary>摘要 / Abstract</summary>

  A zero-knowledge proof is a cryptographic protocol where a prover can convince a verifier that a statement is true, without revealing any further information except for the truth of the statement. More precisely, if $x$ is a statement from an NP language verified by an efficient machine $M$, then a zero-knowledge proof aims to prove to the verifier that there exists a witness $w$ such that $M(x,w)=1$, without revealing any further information about $w$. The proof is a proof of knowledge, if the prover additionally convinces the verifier that it knows the witness $w$, rather than just of its existence. This article is a survey of recent developments in building practical systems for zero-knowledge proofs of knowledge using vector oblivious linear evaluation (VOLE), a tool from secure two-party computation.

  匹配依据：MPC: secure two party computation

  </details>

- **Decoding LTFs in the Generic Group Model**
  2023-06-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/866)
  Dennis Hofheinz, Julia Kastner, Akin Ünal, Bogdan Ursu

  <details><summary>摘要 / Abstract</summary>

  Lossy trapdoor functions (LTFs) constitute a useful and versatile cryptographic building block. LTFs have found applications in various types of encryption schemes, are closely connected to statistically secure oblivious transfer protocols, and have led to the first constructions of group-based trapdoor functions. However, with one recent exception, all known group-based LTFs are comparatively inefficient, and in particular suffer from large images. In this work, we attempt to explain this inefficiency, and derive lower bounds for the image size of group-based LTFs. In essence, we find that purely algebraic group-based LTFs (i.e., LTFs that use the underlying group in a generic way, without considering group representations) must suffer from a large image size (of an at least super-constant number of group elements). Our results also help to explain the mentioned exceptional group-based LTF with compact images.

  匹配依据：MPC: oblivious transfer

  </details>

- **Additive Randomized Encodings and Their Applications**
  2023-06-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/870)
  Shai Halevi, Yuval Ishai, Eyal Kushilevitz, Tal Rabin

  <details><summary>摘要 / Abstract</summary>

  Addition of $n$ inputs is often the easiest nontrivial function to compute securely. Motivated by several open questions, we ask what can be computed securely given only an oracle that computes the sum. Namely, what functions can be computed in a model where parties can only encode their input locally, then sum up the encodings over some Abelian group $\G$, and decode the result to get the function output. An *additive randomized encoding* (ARE) of a function $f(x_1,\ldots,x_n)$ maps every input $x_i$ independently into a randomized encoding $\hat x_i$, such that $\sum_{i=1}^n$ $\hat x_i$ reveals $f(x_1,\ldots,x_n)$ and nothing else about the inputs. In a *robust* ARE, the sum of any subset of the $\hat x_i$ only reveals the residual function obtained by restricting the corresponding inputs. We obtain positive and negative results on ARE. In particular: * Information-theoretic ARE. We fully characterize the 2-party functions $f:X_1\times X_2\to\{0,1\}$ admitting a perfectly secure ARE. For $n\ge 3$ parties, we show a useful ``capped sum&#x27;&#x27; function that separates statistical security from perfect security. * Computational ARE. We present a general feasibility result, showing that *all functions* can be computed in this model, under a standard hardness assumption in bilinear groups. We also describe a heuristic lattice-based construction. * Robust ARE. We present a similar feasibility result for {\em robust} computational ARE based on ideal obfuscation along with standard cryptographic assumptions. We then describe several applications of ARE and the above results. * Under a standard cryptographic assumption, our computational ARE schemes imply the feasibility of general non-interactive secure computation in the shuffle model, where messages from different parties are shuffled. This implies a general utility-preserving compiler from differential privacy in the central model to computational differential privacy in the (non-robust) shuffle model. * The existence of information-theoretic {\em robust} ARE implies &quot;best-possible&quot; information-theoretic MPC protocols (Halevi et al., TCC 2018) and degree-2 multiparty randomized encodings (Applebaum et al., TCC 2018). This yields new positive results for specific functions in the former model, as well as a simple unifying barrier for obtaining negative results in both models.

  匹配依据：MPC: secure computation

  </details>

- **Correlated Pseudorandomness from the Hardness of Quasi-Abelian Decoding**
  2023-06-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.03488) · [IACR ePrint](https://eprint.iacr.org/2023/845)
  Maxime Bombar, Geoffroy Couteau, Alain Couvreur, Clément Ducros

  <details><summary>摘要 / Abstract</summary>

  Secure computation often benefits from the use of correlated randomness to achieve fast, non-cryptographic online protocols. A recent paradigm put forth by Boyle $\textit{et al.}$ (CCS 2018, Crypto 2019) showed how pseudorandom correlation generators (PCG) can be used to generate large amounts of useful forms of correlated (pseudo)randomness, using minimal interactions followed solely by local computations, yielding silent secure two-party computation protocols (protocols where the preprocessing phase requires almost no communication). Furthermore, programmable PCG&#x27;s can be used similarly to generate multiparty correlated randomness to be used in silent secure N-party protocols. Previous works constructed very efficient (non-programmable) PCG&#x27;s for correlations such as random oblivious transfers. However, the situation is less satisfying for the case of random oblivious linear evaluation (OLE), which generalises oblivious transfers over large fields, and are a core resource for secure computation of arithmetic circuits. The state-of-the-art work of Boyle $\textit{et al.}$ (Crypto 2020) constructed programmable PCG&#x27;s for OLE, but their work suffers from two important downsides: (1) it only generates OLE&#x27;s over large fields, and (2) it relies on relatively new &quot;splittable&quot; ring-LPN assumption, which lacks strong security foundations. In this work, we construct new programmable PCG&#x27;s for the OLE correlation, that overcome both limitations. To this end, we introduce the quasi-abelian syndrome decoding problem (QA-SD), a family of assumptions which generalises the well-established quasi-cyclic syndrome decoding assumption. Building upon QA-SD, we construct new programmable PCG&#x27;s for OLE&#x27;s over any field $\mathbb{F}_q$ with $q&gt;2$. Our analysis also sheds light on the security of the ring-LPN assumption used in Boyle $\textit{et al.}$ (Crypto 2020). Using our new PCG&#x27;s, we obtain the first efficient N-party silent secure computation protocols for computing general arithmetic circuit over $\mathbb{F}_q$ for any $q&gt;2$.

  匹配依据：MPC: secure computation, secure two party computation

  </details>

- **$\\mathsf{Mercury}$: Constant-Round Protocols for Multi-Party Computation with Rationals**
  2023-06-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/855)
  Luke Harmon, Gaetan Delavignette

  <details><summary>摘要 / Abstract</summary>

  Most protocols for secure multi-party computation (MPC) work over fields or rings, which means that encoding techniques are needed to map rational-valued data into the algebraic structure being used. Leveraging an encoding technique introduced in recent work of Harmon et al. that is compatible with any MPC protocol over a prime-order field, we present Mercury - a family of protocols for addition, multiplication, subtraction, and division of rational numbers. Notably, the output of our division protocol is exact (i.e., it does not use iterative methods). Our protocols offer improvements in both round complexity and communication complexity when compared with prior art, and are secure for a dishonest minority of semi-honest parties.

  匹配依据：MPC: multi party computation, secure multi party computation

  </details>

- **Unstoppable Wallets: Chain-assisted Threshold ECDSA and its Applications**
  2023-06-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/832)
  Guy Zyskind, Avishay Yanai, Alex "Sandy" Pentland

  <details><summary>摘要 / Abstract</summary>

  The security and usability of cryptocurrencies and other blockchain-based applications depend on the secure management of cryptographic keys. However, current approaches for managing these keys often rely on third parties, trusted to be available at a minimum, and even serve as custodians in some solutions, creating single points of failure and limiting the ability of users to fully control their own assets. In this work, we introduce the concept of unstoppable wallets, which are programmable threshold ECDSA wallets that allow users to co-sign transactions with a confidential smart contract, rather than a singular third-party. We propose a new model that encapsulates the use of a confidential smart contract as both a party and the sole (broadcast) communication channel in secure Multi-Party Computation (MPC) protocols. We construct highly efficient threshold ECDSA protocols that form the basis of unstoppable wallets and prove their security under this model, achieving the standard notion of fairness and robustness even in case of a dishonest majority of signers. Our protocols minimize the write-complexity for threshold ECDSA key-generation and signing, while reducing communication and computation overhead. We implement these protocols as smart contracts, deploy them on Secret Network, and showcase their applicability for two interesting applications, policy checking and wallet exchange, as well as their efficiency by demonstrating low gas costs and fees.

  匹配依据：MPC: secure multi party computation

  </details>

- **On Linear Communication Complexity for (Maximally) Fluid MPC**
  2023-06-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/839)
  Alexander Bienstock, Daniel Escudero, Antigoni Polychroniadou

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation protocols with dynamic parties, which assume that honest parties do not need to be online throughout the whole execution of the protocol, have recently gained a lot of traction for computations of large scale distributed protocols, such as blockchains. More specifically, in Fluid MPC, introduced in (Choudhuri et al. CRYPTO 2021), parties can dynamically join and leave the computation from round to round. The best known Fluid MPC protocol in the honest majority setting communicates $O(n^2)$ elements per gate where $n$ is the number of parties online at a time. While Le Mans (Rachuri and Scholl, CRYPTO 2022) extends Fluid MPC to the dishonest majority setting with preprocessing, it still communicates $O(n^2)$ elements per gate. In this work we present alternative Fluid MPC solutions that require $O(n)$ communication per gate for both the information-theoretic honest majority setting and the information-theoretic dishonest majority setting with preprocessing. Our solutions also achieve maximal fluidity where parties only need to be online for a single communication round. Additionally, we show that a protocol in the information-theoretic dishonest majority setting with sub-quadratic $o(n^2)$ overhead per gate requires for each of the $N$ parties who may ever participate in the (later) execution phase, $\Omega(N)$ preprocessed data per gate.

  匹配依据：MPC: secure multiparty computation

  </details>

- **How to Recover a Secret with O(n) Additions**
  2023-06-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/838)
  Benny Applebaum, Oded Nir, Benny Pinkas

  <details><summary>摘要 / Abstract</summary>

  Threshold cryptography is typically based on the idea of secret-sharing a private-key $s\in F$ ``in the exponent&#x27;&#x27; of some cryptographic group $G$, or more generally, encoding $s$ in some linearly homomorphic domain. In each invocation of the threshold system (e.g., for signing or decrypting) an ``encoding&#x27;&#x27; of the secret is being recovered and so the complexity, measured as the number of group multiplications over $G$, is equal to the number of $F$-additions that are needed to reconstruct the secret. Motivated by this scenario, we initiate the study of $n$-party secret-sharing schemes whose reconstruction algorithm makes a minimal number of \emph{additions}. The complexity of existing schemes either scales linearly with $n\log |F|$ (e.g., Shamir, CACM&#x27;79) or, at least, quadratically with $n$ independently of the size of the domain $F$ (e.g., Cramer-Xing, EUROCRYPT &#x27;20). This leaves open the existence of a secret sharing whose recovery algorithm can be computed by performing only $O(n)$ additions. We resolve the question in the affirmative and present such a near-threshold secret sharing scheme that provides privacy against unauthorized sets of density at most $\tau_p$, and correctness for authorized sets of density at least $\tau_c$, for any given arbitrarily close constants $\tau_p&lt;\tau_c$. Reconstruction can be computed by making at most $O(n)$ additions and, in addition, (1) the share size is constant, (2) the sharing procedure also makes only $O(n)$ additions, and (3) the scheme is a blackbox secret-sharing scheme, i.e., the sharing and reconstruction algorithms work universally for all finite abelian groups $F$. Prior to our work, no such scheme was known even without features (1)--(3) and even for the ramp setting where $\tau_p$ and $\tau_c$ are far apart. As a by-product, we derive the first blackbox near-threshold secret-sharing scheme with linear-time sharing. We also present several concrete instantiations of our approach that seem practically efficient (e.g., for threshold discrete-log-based signatures). Our constructions are combinatorial in nature. We combine graph-based erasure codes that support ``peeling-based&#x27;&#x27; decoding with a new randomness extraction method that is based on inner-product with a small-integer vector. We also introduce a general concatenation-like transform for secret-sharing schemes that allows us to arbitrarily shrink the privacy-correctness gap with only a minor overhead. Our techniques enrich the secret-sharing toolbox and, in the context of blackbox secret sharing, offer a new randomized combinatorial alternative to existing deterministic number-theoretic approaches.

  匹配依据：MPC: secret sharing

  </details>

- **On Concurrent Multi-Party Quantum Computation**
  2023-06-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/827)
  Vipul Goyal, Xiao Liang, Giulio Malavolta

  <details><summary>摘要 / Abstract</summary>

  Recently, significant progress has been made toward quantumly secure multi-party computation (MPC) in the stand-alone setting. In sharp contrast, the picture of concurrently secure MPC (or even 2PC), for both classical and quantum functionalities, still remains unclear. Quantum information behaves in a fundamentally different way, making the job of adversary harder and easier at the same time. Thus, it is unclear if the positive or negative results from the classical setting still apply. This work initiates a systematic study of concurrent secure computation in the quantum setting. We obtain a mix of positive and negative results. We first show that assuming the existence of post-quantum one-way functions (PQ-OWFs), concurrently secure 2PC (and thus MPC) for quantum functionalities is impossible. Next, we focus on the bounded-concurrent setting, where we obtain simulation-sound zero-knowledge arguments for both NP and QMA, assuming PQ-OWFs. This is obtained by a new design of simulation-sound gadget, relying on the recent post-quantum non-malleable commitments by Liang, Pandey, and Yamakawa [FOCS&#x27;23], and the quantum rewinding strategy recently developed by Ananth, Chung, and La Placa [CRYPTO&#x27;21] for bounded-concurrent post-quantum ZK. Moreover, we show that our technique is general enough---It also leads to quantum-secure bounded-concurrent coin-flipping protocols, and eventually general-purpose 2PC and MPC, for both classical and quantum functionalities. All these constructions can be based on the quantum hardness of Learning with Errors.

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **Over-the-Air Federated Learning In Broadband Communication**
  2023-06-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.01963)
  Wayne Lemieux, Raphael Pinard, Mitra Hassani

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) is a privacy-preserving distributed machine learning paradigm that operates at the wireless edge. It enables clients to collaborate on model training while keeping their data private from adversaries and the central server. However, current FL approaches have limitations. Some rely on secure multiparty computation, which can be vulnerable to inference attacks. Others employ differential privacy, but this may lead to decreased test accuracy when dealing with a large number of parties contributing small amounts of data. To address these issues, this paper proposes a novel approach that integrates federated learning seamlessly into the inner workings of MIMO (Multiple-Input Multiple-Output) systems.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Falkor: Federated Learning Secure Aggregation Powered by AES-CTR GPU Implementation**
  2023-06-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/804)
  Mariya Georgieva Belorgey, Sofia Dandjee, Nicolas Gama, Dimitar Jetchev, Dmitry Mikushin

  <details><summary>摘要 / Abstract</summary>

  We propose a novel protocol, Falkor, for secure aggregation for Federated Learning in the multi-server scenario based on masking of local models via a stream cipher based on AES in counter mode and accelerated by GPUs running on the aggregating servers. The protocol is resilient to client dropout and has reduced clients/servers communication cost by a factor equal to the number of aggregating servers (compared to the naïve baseline method). It scales simultaneously in the two major complexity aspects: 1) large number of clients; 2) highly complex machine learning models such as CNNs, RNNs, Transformers, etc. The AES-CTR-based masking function in our aggregation protocol is built on the concept of counter-based cryptographically-secure pseudorandom number generators (csPRNGs) as described in [SMDS&#x27;11] and subsequently used by Facebook for their torchcsprng csPRNG. We improve upon torchcsprng by careful use of shared memory on the GPU device, a recent idea of Cihangir Tezcan [Tezcan&#x27;21] and obtain 100x speedup in the masking function compared to a single CPU core. In addition, we prove the semantic security of the AES-CTR-based masking function. Finally, we demonstrate scalability of our protocol in two real-world Federated Learning scenarios: 1) efficient training of large logistic regression models with 50 features and 50M data points distributed across 1000 clients that can dropout and securely aggregated via three servers (running secure multi-party computation (SMPC)); 2) training a recurrent neural network (RNN) model for sentiment analysis of Twitter feeds coming from a large number of Twitter users (more than 250,000 users). In case 1), our secure aggregation algorithm runs in less than a minute compared to a pure MPC computation (on 3 parties) that takes 27 hours and uses 400GB RAM machines as well as 1 gigabit-per-second network. In case 2), the total training is around $10$ minutes using our GPU powered secure aggregation versus 10 hours using a single CPU core.

  匹配依据：MPC: secure multi party computation

  </details>

- **A Formal Model for Secure Multiparty Computation**
  2023-06-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.00308)
  Amy Rathore, Marina Blanton, Marco Gaboardi, Lukasz Ziarek

  <details><summary>摘要 / Abstract</summary>

  Although Secure Multiparty Computation (SMC) has seen considerable development in recent years, its use is challenging, resulting in complex code which obscures whether the security properties or correctness guarantees hold in practice. For this reason, several works have investigated the use of formal methods to provide guarantees for SMC systems. However, these approaches have been applied mostly to domain specific languages (DSL), neglecting general-purpose approaches. In this paper, we consider a formal model for an SMC system for annotated C programs. We choose C due to its popularity in the cryptographic community and being the only general-purpose language for which SMC compilers exist. Our formalization supports all key features of C -- including private-conditioned branching statements, mutable arrays (including out of bound array access), pointers to private data, etc. We use this formalization to characterize correctness and security properties of annotated C, with the latter being a form of non-interference on execution traces. We realize our formalism as an implementation in the PICCO SMC compiler and provide evaluation results on SMC programs written in C.

  匹配依据：MPC: secure multiparty computation

  </details>

- **A Meta-learning Framework for Tuning Parameters of Protection Mechanisms in Trustworthy Federated Learning**
  2023-05-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.18400)
  Xiaojin Zhang, Yan Kang, Lixin Fan, Kai Chen, Qiang Yang

  <details><summary>摘要 / Abstract</summary>

  Trustworthy Federated Learning (TFL) typically leverages protection mechanisms to guarantee privacy. However, protection mechanisms inevitably introduce utility loss or efficiency reduction while protecting data privacy. Therefore, protection mechanisms and their parameters should be carefully chosen to strike an optimal tradeoff between \textit{privacy leakage}, \textit{utility loss}, and \textit{efficiency reduction}. To this end, federated learning practitioners need tools to measure the three factors and optimize the tradeoff between them to choose the protection mechanism that is most appropriate to the application at hand. Motivated by this requirement, we propose a framework that (1) formulates TFL as a problem of finding a protection mechanism to optimize the tradeoff between privacy leakage, utility loss, and efficiency reduction and (2) formally defines bounded measurements of the three factors. We then propose a meta-learning algorithm to approximate this optimization problem and find optimal protection parameters for representative protection mechanisms, including Randomization, Homomorphic Encryption, Secret Sharing, and Compression. We further design estimation algorithms to quantify these found optimal protection parameters in a practical horizontal federated learning setting and provide a theoretical analysis of the estimation error.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Model Aggregation for Asynchronous Federated Learning**
  2023-05-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.17521)
  Jianxiang Zhao, Xiangman Li, Jianbing Ni

  <details><summary>摘要 / Abstract</summary>

  We present a novel privacy-preserving model aggregation for asynchronous federated learning, named PPA-AFL that removes the restriction of synchronous aggregation of local model updates in federated learning, while enabling the protection of the local model updates against the server. In PPA-AFL, clients can proactive decide when to engage in the training process, and sends local model updates to the server when the updates are available. Thus, it is not necessary to keep synchronicity with other clients. To safeguard client updates and facilitate local model aggregation, we employ Paillier encryption for local update encryption and support homomorphic aggregation. Furthermore, secret sharing is utilized to enable the sharing of decryption keys and facilitate privacy-preserving asynchronous aggregation. As a result, the server remains unable to gain any information about the local updates while asynchronously aggregating to produce the global model. We demonstrate the efficacy of our proposed PPA-AFL framework through comprehensive complexity analysis and extensive experiments on a prototype implementation, highlighting its potential for practical adoption in privacy-sensitive asynchronous federated learning scenarios.

  匹配依据：MPC: secret sharing

  </details>

- **Threshold ECDSA in Three Rounds**
  2023-05-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/765)
  Jack Doerner, Yashvanth Kondi, Eysa Lee, abhi shelat

  <details><summary>摘要 / Abstract</summary>

  We present a three-round protocol for threshold ECDSA signing with malicious security against a dishonest majority, which information-theoretically UC-realizes a standard threshold signing functionality, assuming only ideal commitment and two-party multiplication primitives. Our protocol combines an intermediate representation of ECDSA signatures that was recently introduced by Abram et al. (Eurocrypt&#x27;22) with an efficient statistical consistency check reminiscent of the ones used by the protocols of Doerner et al. (S&amp;P&#x27;18, S&amp;P&#x27;19). We show that shared keys for our signing protocol can be generated using a simple commit-release-and-complain procedure, without any proofs of knowledge, and to compute the intermediate representation of each signature, we propose a two-round vectorized multiplication protocol based on oblivious transfer that outperforms all similar constructions.

  匹配依据：MPC: oblivious transfer

  </details>

- **Scaling Mobile Private Contact Discovery to Billions of Users**
  2023-05-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/758)
  Laura Hetz, Thomas Schneider, Christian Weinert

  <details><summary>摘要 / Abstract</summary>

  Mobile contact discovery is a convenience feature of messengers such as WhatsApp or Telegram that helps users to identify which of their existing contacts are registered with the service. Unfortunately, the contact discovery implementation of many popular messengers massively violates the users&#x27; privacy as demonstrated by Hagen et al. (NDSS &#x27;21, ACM TOPS &#x27;23). Unbalanced private set intersection (PSI) protocols are a promising cryptographic solution to realize mobile private contact discovery, however, state-of-the-art protocols do not scale to real-world database sizes with billions of registered users in terms of communication and/or computation overhead. In our work, we make significant steps towards truly practical large-scale mobile private contact discovery. For this, we combine and substantially optimize the unbalanced PSI protocol of Kales et al. (USENIX Security &#x27;19) and the private information retrieval (PIR) protocol of Kogan and Corrigan-Gibbs (USENIX Security &#x27;21). Our resulting protocol has a total communication overhead that is sublinear in the size of the server&#x27;s user database and also has sublinear online runtimes. We optimize our protocol by introducing database partitioning and efficient scheduling of user queries. To handle realistic change rates of databases and contact lists, we propose and evaluate different possibilities for efficient updates. We implement our protocol on smartphones and measure online runtimes of less than 2s to query up to 1024 contacts from a database with more than two billion entries. Furthermore, we achieve a reduction in setup communication up to factor 32x compared to state-of-the-art mobile private contact discovery protocols.

  匹配依据：MPC: private set intersection

  </details>

- **SDitH in the QROM**
  2023-05-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/756)
  Carlos Aguilar-Melchor, Andreas Hülsing, David Joseph, Christian Majenz, Eyal Ronen, Dongze Yue

  <details><summary>摘要 / Abstract</summary>

  The MPC in the Head (MPCitH) paradigm has recently led to significant improvements for signatures in the code-based setting. In this paper we consider some modifications to a recent twist of MPCitH, called Hypercube-MPCitH, that in the code-based setting provides the currently best known signature sizes. By compressing the Hypercube-MPCitH five-round code-based identification scheme into three-rounds we obtain two main benefits. On the one hand, it allows us to further develop recent techniques to provide a tight security proof in the quantum-accessible random oracle model (QROM), avoiding the catastrophic reduction losses incurred using generic QROM-results for Fiat-Shamir. On the other hand, we can reduce the already low-cost online part of the signature even further. In addition, we propose the use of proof-of-work techniques that allow to reduce the signature size. On the technical side, we develop generalizations of several QROM proof techniques and introduce a variant of the recently proposed extractable QROM.

  匹配依据：MPC: mpc (context)

  </details>

- **Towards the Links of Cryptanalytic Methods on MPC/FHE/ZK-Friendly Symmetric-Key Primitives**
  2023-05-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/748)
  Shiyao Chen, Chun Guo, Jian Guo, Li Liu, Meiqin Wang, Puwen Wei, Zeyu Xu

  <details><summary>摘要 / Abstract</summary>

  Symmetric-key primitives designed over the prime field $\mathbb{F}_p$ with odd characteristics, rather than the traditional $\mathbb{F}_2^{n}$, are becoming the most popular choice for MPC/FHE/ZK-protocols for better efficiencies. However, the security of $\mathbb{F}_p$ is less understood as there are highly nontrivial gaps when extending the cryptanalysis tools and experiences built on $\mathbb{F}_2^{n}$ in the past few decades to $\mathbb{F}_p$. At CRYPTO 2015, Sun et al. established the links among impossible differential, zero-correlation linear, and integral cryptanalysis over $\mathbb{F}_2^{n}$ from the perspective of distinguishers. In this paper, following the definition of linear correlations over $\mathbb{F}_p$ by Baignéres, Stern and Vaudenay at SAC 2007, we successfully establish comprehensive links over $\mathbb{F}_p$, by reproducing the proofs and offering alternatives when necessary. Interesting and important differences between $\mathbb{F}_p$ and $\mathbb{F}_2^n$ are observed. - Zero-correlation linear hulls can not lead to integral distinguishers for some cases over $\mathbb{F}_p$, while this is always possible over $\mathbb{F}_2^n$ proven by Sun et al.. - When the newly established links are applied to GMiMC, its impossible differential, zero-correlation linear hull and integral distinguishers can be increased by up to 3 rounds for most of the cases, and even to an arbitrary number of rounds for some special and limited cases, which only appeared in $\mathbb{F}_p$. It should be noted that all these distinguishers do not invalidate GMiMC&#x27;s security claims. The development of the theories over $\mathbb{F}_p$ behind these links, and properties identified (be it similar or different) will bring clearer and easier understanding of security of primitives in this emerging $\mathbb{F}_p$ field, which we believe will provide useful guides for future cryptanalysis and design.

  匹配依据：MPC: mpc (context)

  </details>

- **Scalable Agreement Protocols with Optimal Optimistic Efficiency**
  2023-05-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/751)
  Yuval Gelles, Ilan Komargodski

  <details><summary>摘要 / Abstract</summary>

  Designing efficient distributed protocols for various agreement tasks such as Byzantine Agreement, Broadcast, and Committee Election is a fundamental problem. We are interested in $scalable$ protocols for these tasks, where each (honest) party communicates a number of bits which is sublinear in $n$, the number of parties. The first major step towards this goal is due to King et al. (SODA 2006) who showed a protocol where each party sends only $\tilde O(1)$ bits throughout $\tilde O(1)$ rounds, but guarantees only that $1-o(1)$ fraction of honest parties end up agreeing on a consistent output, assuming constant $&lt;1/3$ fraction of static corruptions. Few years later, King et al. (ICDCN 2011) managed to get a full agreement protocol in the same model but where each party sends $\tilde O(\sqrt{n})$ bits throughout $\tilde O(1)$ rounds. Getting a full agreement protocol with $o(\sqrt{n})$ communication per party has been a major challenge ever since. In light of this barrier, we propose a new framework for designing efficient agreement protocols. Specifically, we design $\tilde O(1)$-round protocols for all of the above tasks (assuming constant $&lt;1/3$ fraction of static corruptions) with optimistic and pessimistic guarantees: $\bullet$ $Optimistic$ $complexity$: In an honest execution, (honest) parties send only $\tilde O(1)$ bits. $\bullet$ $Pessimistic$ $complexity$: In any other case, (honest) parties send $\tilde O(\sqrt{n})$ bits. Thus, all an adversary can gain from deviating from the honest execution is that honest parties will need to work harder (i.e., transmit more bits) to reach agreement and terminate. Besides the above agreement tasks, we also use our new framework to get a scalable secure multiparty computation (MPC) protocol with optimistic and pessimistic complexities. Technically, we identify a relaxation of Byzantine Agreement (of independent interest) that allows us to fall-back to a pessimistic execution in a coordinated way by all parties. We implement this relaxation with $\tilde O(1)$ communication bits per party and within $\tilde O(1)$ rounds.

  匹配依据：MPC: secure multiparty computation

  </details>

- **PSI from ring-OLE**
  2023-05-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/745)
  Wutichai Chongchitmate, Yuval Ishai, Steve Lu, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) is one of the most extensively studied instances of secure computation. PSI allows two parties to compute the intersection of their input sets without revealing anything else. Other useful variants include PSI-Payload, where the output includes payloads associated with members of the intersection, and PSI-Sum, where the output includes the sum of the payloads instead of individual ones. In this work, we make two related contributions. First, we construct simple and efficient protocols for PSI and PSI-Payload from a ring version of oblivious linear function evaluation (ring-OLE) that can be efficiently realized using recent ring-LPN based protocols. A standard OLE over a field F allows a sender with $a,b \in \mathbb{F}$ to deliver $ax+b$ to a receiver who holds $x \in \mathbb{F}$. Ring-OLE generalizes this to a ring $\mathcal{R}$, in particular, a polynomial ring over $\mathbb{F}$. Our second contribution is an efficient general reduction of a variant of PSI-Sum to PSI-Payload and secure inner product. Our protocols have better communication cost than state-of-the-art PSI protocols, especially when requiring security against malicious parties and when allowing input-independent preprocessing. Compared to previous maliciously secure PSI protocols that have a similar com- putational cost, our online communication is 2x better for small sets (28 − 212 elements) and 20% better for large sets (220 − 224). Our protocol is also simpler to describe and implement. We obtain even bigger improvements over the state of the art (4-5x better running time) for our variant of PSI-Sum.

  匹配依据：MPC: private set intersection, secure computation

  </details>

- **Confidential Truth Finding with Multi-Party Computation (Extended Version)**
  2023-05-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.14727)
  Angelo Saadeh, Pierre Senellart, Stéphane Bressan

  <details><summary>摘要 / Abstract</summary>

  Federated knowledge discovery and data mining are challenged to assess the trustworthiness of data originating from autonomous sources while protecting confidentiality and privacy. Truth-finding algorithms help corroborate data from disagreeing sources. For each query it receives, a truth-finding algorithm predicts a truth value of the answer, possibly updating the trustworthiness factor of each source. Few works, however, address the issues of confidentiality and privacy. We devise and present a secure secret-sharing-based multi-party computation protocol for pseudo-equality tests that are used in truth-finding algorithms to compute additions depending on a condition. The protocol guarantees confidentiality of the data and privacy of the sources. We also present variants of truth-finding algorithms that would make the computation faster when executed using secure multi-party computation. We empirically evaluate the performance of the proposed protocol on two state-of-the-art truth-finding algorithms, Cosine, and 3-Estimates, and compare them with that of the baseline plain algorithms. The results confirm that the secret-sharing-based secure multi-party algorithms are as accurate as the corresponding baselines but for proposed numerical approximations that significantly reduce the efficiency loss incurred.

  匹配依据：MPC: multi party computation, secret sharing, secure multi party computation

  </details>

- **Practical Robust DKG Protocols for CSIDH**
  2023-05-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/740)
  Shahla Atapoor, Karim Baghery, Daniele Cozzo, Robi Pedersen

  <details><summary>摘要 / Abstract</summary>

  A Distributed Key Generation (DKG) protocol is an essential component of threshold cryptography. DKGs enable a group of parties to generate a secret and public key pair in a distributed manner so that the secret key is protected from being exposed, even if a certain number of parties are compromised. Robustness further guarantees that the construction of the key pair is always successful, even if malicious parties try to sabotage the computation. In this paper, we construct two efficient robust DKG protocols in the CSIDH setting that work with Shamir secret sharing. Both the proposed protocols are proven to be actively secure in the quantum random oracle model and use an Information Theoretically (IT) secure Verifiable Secret Sharing (VSS) scheme that is built using bivariate polynomials. As a tool, we construct a new piecewise verifiable proof system for structured public keys, that could be of independent interest. In terms of isogeny computations, our protocols outperform the previously proposed DKG protocols CSI-RAShi and Structured CSI-RAShi. As an instance, using our DKG protocols, 4 parties can sample a PK of size 4kB, for CSI-FiSh and CSI-SharK, respectively, 3.4 and 1.7 times faster than the current alternatives. On the other hand, since we use an IT-secure VSS, the fraction of corrupted parties is limited to less than a third and the communication cost of our schemes scales slightly worse with an increasing number of parties. For a low number of parties, our scheme still outperforms the alternatives in terms of communication.

  匹配依据：MPC: secret sharing

  </details>

- **Fair Differentially Private Federated Learning Framework**
  2023-05-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.13878)
  Ayush K. Varshney, Sonakshi Garg, Arka Ghosh, Sargam Gupta

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) is a distributed machine learning strategy that enables participants to collaborate and train a shared model without sharing their individual datasets. Privacy and fairness are crucial considerations in FL. While FL promotes privacy by minimizing the amount of user data stored on central servers, it still poses privacy risks that need to be addressed. Industry standards such as differential privacy, secure multi-party computation, homomorphic encryption, and secure aggregation protocols are followed to ensure privacy in FL. Fairness is also a critical issue in FL, as models can inherit biases present in local datasets, leading to unfair predictions. Balancing privacy and fairness in FL is a challenge, as privacy requires protecting user data while fairness requires representative training data. This paper presents a &quot;Fair Differentially Private Federated Learning Framework&quot; that addresses the challenges of generating a fair global model without validation data and creating a globally private differential model. The framework employs clipping techniques for biased model updates and Gaussian mechanisms for differential privacy. The paper also reviews related works on privacy and fairness in FL, highlighting recent advancements and approaches to mitigate bias and ensure privacy. Achieving privacy and fairness in FL requires careful consideration of specific contexts and requirements, taking into account the latest developments in industry standards and techniques.

  匹配依据：MPC: secure multi party computation

  </details>

- **Must the Communication Graph of MPC Protocols be an Expander?**
  2023-05-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.11428)
  Elette Boyle, Ran Cohen, Deepesh Data, Pavel Hubáček

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) on incomplete communication networks has been studied within two primary models: (1) Where a partial network is fixed a priori, and thus corruptions can occur dependent on its structure, and (2) Where edges in the communication graph are determined dynamically as part of the protocol. Whereas a rich literature has succeeded in mapping out the feasibility and limitations of graph structures supporting secure computation in the fixed-graph model (including strong classical lower bounds), these bounds do not apply in the latter dynamic-graph setting, which has recently seen exciting new results, but remains relatively unexplored. In this work, we initiate a similar foundational study of MPC within the dynamic-graph model. As a first step, we investigate the property of graph expansion. All existing protocols (implicitly or explicitly) yield communication graphs which are expanders, but it is not clear whether this is inherent. Our results consist of two types (for constant fraction of corruptions): * Upper bounds: We demonstrate secure protocols whose induced communication graphs are not expander graphs, within a wide range of settings (computational, information theoretic, with low locality, even with low locality and adaptive security), each assuming some form of input-independent setup. * Lower bounds: In the plain model (no setup) with adaptive corruptions, we demonstrate that for certain functionalities, no protocol can maintain a non-expanding communication graph against all adversarial strategies. Our lower bound relies only on protocol correctness (not privacy), and requires a surprisingly delicate argument. More generally, we provide a formal framework for analyzing the evolving communication graph of MPC protocols, giving a starting point for studying the relation between secure computation and further, more general graph properties.

  匹配依据：MPC: secure computation, secure multiparty computation

  </details>

- **TPMDP: Threshold Personalized Multi-party Differential Privacy via Optimal Gaussian Mechanism**
  2023-05-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.11192)
  Jiandong Liu, Lan Zhang, Chaojie Lv, Ting Yu, Nikolaos M. Freris, Xiang-Yang Li

  <details><summary>摘要 / Abstract</summary>

  In modern distributed computing applications, such as federated learning and AIoT systems, protecting privacy is crucial to prevent adversarial parties from colluding to steal others&#x27; private information. However, guaranteeing the utility of computation outcomes while protecting all parties&#x27; data privacy can be challenging, particularly when the parties&#x27; privacy requirements are highly heterogeneous. In this paper, we propose a novel privacy framework for multi-party computation called Threshold Personalized Multi-party Differential Privacy (TPMDP), which addresses a limited number of semi-honest colluding adversaries. Our framework enables each party to have a personalized privacy budget. We design a multi-party Gaussian mechanism that is easy to implement and satisfies TPMDP, wherein each party perturbs the computation outcome in a secure multi-party computation protocol using Gaussian noise. To optimize the utility of the mechanism, we cast the utility loss minimization problem into a linear programming (LP) problem. We exploit the specific structure of this LP problem to compute the optimal solution after O(n) computations, where n is the number of parties, while a generic solver may require exponentially many computations. Extensive experiments demonstrate the benefits of our approach in terms of low utility loss and high efficiency compared to existing private mechanisms that do not consider personalized privacy requirements or collusion thresholds.

  匹配依据：MPC: multi party computation, secure multi party computation

  </details>

- **Quantum linear polynomial evaluation based on XOR oblivious transfer compatible with classical partially homomorphic encryption**
  2023-05-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.11114)
  Li Yu, Jie Xu, Fuqun Wang, Chui-Ping Yang

  <details><summary>摘要 / Abstract</summary>

  XOR oblivious transfer is a universal cryptographic primitive that can be related to linear polynomial evaluation. We firstly introduce some bipartite quantum protocols for XOR oblivious transfer, which are not secure if one party cheats, and some of them can be combined with a classical XOR homomorphic encryption scheme for evaluation of linear polynomials modulo 2 with hybrid security. We then introduce a general protocol using modified versions of the XOR oblivious transfer protocols to evaluate linear polynomials modulo 2 with partial information-theoretic security. When combined with the ability to perform arbitrary quantum computation, this would lead to deterministic interactive two-party computation which is quite secure in the information-theoretic sense when the allowed set of inputs is large. For the task of classical function evaluation, although the quantum computation approach is still usable, we also discuss purely classical post-processing methods based on the proposed linear polynomial evaluation protocols.

  匹配依据：MPC: oblivious transfer, two party computation

  </details>

- **Measurement-Device-Independent Quantum Secret Sharing**
  2023-05-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.10755)
  Xiao-Qiu Cai, Zi-Fan Liu, Tian-Yin Wang

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing plays an important role in quantum communications and secure multiparty computation. In this paper, we present a new measurement-device-independent quantum secret sharing protocol, which can double the space distance between the dealer and each sharer for quantum transmission compared with prior works. Furthermore, it is experimentally feasible with current technology for requiring just three-particle Greenberger-Horne-Zeilinger states and Bell state measurements.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **A Two-Party Hierarchical Deterministic Wallets in Practice**
  2023-05-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/714)
  ChihYun Chuang, IHung Hsu, TingFang Lee

  <details><summary>摘要 / Abstract</summary>

  The applications of Hierarchical Deterministic Wallet are rapidly growing in various areas such as cryptocurrency exchanges and hardware wallets. Improving privacy and security is more important than ever. In this study, we proposed a protocol that fully support a two-party computation of BIP32. Our protocol, similar to the distributed key generation, can generate each party’s secret share, the common chain-code, and the public key without revealing a seed and any descendant private keys. We also provided a simulation-based proof of our protocol assuming a rushing, static, and malicious adversary in the hybrid model. Our master key generation protocol produces up to total of two bit leakages from a honest party given the feature that the seeds will be re-selected after each execution. The proposed hardened child key derivation protocol leads up to a one bit leakage in the worst situation of simulation from a honest party and will be accumulated with each execution. Fortunately, in reality, this issue can be largely mitigated by adding some validation criteria of boolean circuits and masking the input shares before each execution. We then implemented the proposed protocol and ran in a single thread on a laptop which turned out with practically acceptable execution time. Lastly, the outputs of our protocol can be easily integrated with many threshold sign protocols.

  匹配依据：MPC: two party computation

  </details>

- **Asymmetric Multi-Party Computation**
  2023-05-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/704)
  Vipul Goyal, Chen-Da Liu-Zhang, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  Current protocols for Multi-Party Computation (MPC) consider the setting where all parties have access to similar resources. For example, all parties have access to channels bounded by the same worst-case delay upper bound $\Delta$, and all channels have the same cost of communication. As a consequence, the overall protocol performance (resp. the communication cost) may be heavily affected by the slowest (resp. the most expensive) channel, even when most channels are fast (resp. cheap). Given the state of affairs, we initiate a systematic study of &#x27;asymmetric&#x27; MPC. In asymmetric MPC, the parties are divided into two categories: fast and slow parties, depending on whether they have access to high-end or low-end resources. We investigate two different models. In the first, we consider asymmetric communication delays: Fast parties are connected via channels with small delay $\delta$ among themselves, while channels connected to (at least) one slow party have a large delay $\Delta \gg \delta$. In the second model, we consider asymmetric communication costs: Fast parties benefit from channels with cheap communication, while channels connected to a slow party have an expensive communication. We provide a wide range of positive and negative results exploring the trade-offs between the achievable number of tolerated corruptions $t$ and slow parties $s$, versus the round complexity and communication cost in each of the models. Among others, we achieve the following results. In the model with asymmetric communication delays, focusing on the information-theoretic (i-t) setting: - An i-t asymmetric MPC protocol with security with abort as long as $t+s &lt; n$ and $t&lt;n/2$, in a constant number of slow rounds. - We show that achieving an i-t asymmetric MPC protocol for $t+s = n$ and with number of slow rounds independent of the circuit size implies an i-t synchronous MPC protocol with round complexity independent of the circuit size, which is a major problem in the field of round-complexity of MPC. - We identify a new primitive, \emph{asymmetric broadcast}, that allows to consistently distribute a value among the fast parties, and at a later time the same value to slow parties. We completely characterize the feasibility of asymmetric broadcast by showing that it is possible if and only if $2t + s &lt; n$. - An i-t asymmetric MPC protocol with guaranteed output delivery as long as $t+s &lt; n$ and $t&lt;n/2$, in a number of slow rounds independent of the circuit size. In the model with asymmetric communication cost, we achieve an asymmetric MPC protocol for security with abort for $t+s&lt;n$ and $t&lt;n/2$, based on one-way functions (OWF). The protocol communicates a number of bits over expensive channels that is independent of the circuit size. We conjecture that assuming OWF is needed and further provide a partial result in this direction.

  匹配依据：MPC: multi party computation

  </details>

- **Unconditionally Secure Non-malleable Secret Sharing and Circular External Difference Families**
  2023-05-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.09405)
  Shannon Veitch, Douglas R. Stinson

  <details><summary>摘要 / Abstract</summary>

  Various notions of non-malleable secret sharing schemes have been considered. In this paper, we review the existing work on non-malleable secret sharing and suggest a novel game-based definition. We provide a new construction of an unconditionally secure non-malleable threshold scheme with respect to a specified relation. To do so, we introduce a new type of algebraic manipulation detection (AMD) code and construct examples of new variations of external difference families, which are of independent combinatorial interest.

  匹配依据：MPC: secret sharing

  </details>

- **Trustworthy Privacy-preserving Hierarchical Ensemble and Federated Learning in Healthcare 4.0 with Blockchain**
  2023-05-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.09209)
  Veronika Stephanie, Ibrahim Khalil, Mohammed Atiquzzaman, Xun Yi

  <details><summary>摘要 / Abstract</summary>

  The advancement of Internet and Communication Technologies (ICTs) has led to the era of Industry 4.0. This shift is followed by healthcare industries creating the term Healthcare 4.0. In Healthcare 4.0, the use of IoT-enabled medical imaging devices for early disease detection has enabled medical practitioners to increase healthcare institutions&#x27; quality of service. However, Healthcare 4.0 is still lagging in Artificial Intelligence and big data compared to other Industry 4.0 due to data privacy concerns. In addition, institutions&#x27; diverse storage and computing capabilities restrict institutions from incorporating the same training model structure. This paper presents a secure multi-party computation-based ensemble federated learning with blockchain that enables heterogeneous models to collaboratively learn from healthcare institutions&#x27; data without violating users&#x27; privacy. Blockchain properties also allow the party to enjoy data integrity without trust in a centralized server while also providing each healthcare institution with auditability and version control capability.

  匹配依据：MPC: secure multi party computation

  </details>

- **On the Invalidity of LV16/Lin17 Obfuscation Schemes**
  2023-05-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/692)
  Yupu Hu, Siyue Dong, Baocang Wang, Xingting Dong

  <details><summary>摘要 / Abstract</summary>

  Indistinguishability obfuscation (IO) is at the frontier of cryptography research for several years. LV16/Lin17 obfuscation schemes are famous progresses towards simplifying obfuscation mechanism. In fact, these two schemes only constructed two compact functional encryption (CFE) algorithms, while other things were taken to AJ15 IO frame or BV15 IO frame. That is, CFE algorithms are inserted into AJ15 IO frame or BV15 IO frame to form a complete IO scheme. The basic structure of two CFE algorithms can be described in the following way. The polynomial-time-computable Boolean function is transformed into a group of low-degree low-locality component functions by using randomized encoding, while some public combination of values of component functions is the value of original Boolean function. The encryptor uses constant-degree multilinear maps (rather than polynomial-degree multilinear maps) to encrypt independent variables of component functions. The decryptor uses zero-testing tool of multilinear maps to obtain values of component functions (rather than to obtain values of independent variables), and then uses public combination to obtain the value of original Boolean function. In this paper we restrict IO to be a real white box (RWB). Under such restriction we point out that LV16/Lin17 CFE algorithms being inserted into AJ15 IO frame are invalid. More detailedly, such insertion makes the adversary gradually learn the shape of the function, therefore the scheme is not secure. In other words, such scheme is not a real IO scheme, but rather a garbling scheme. It needs to be said that RWB restriction is reasonable, which means the essential contribution of IO for cryptography research.

  匹配依据：MPC: garbling scheme

  </details>

- **Third-Party Private Set Intersection**
  2023-05-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/685)
  Foo Yee Yeo, Jason H. M. Ying

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) enables two parties, each holding a private set to compute their intersection without revealing other information in the process. We introduce a variant of conventional PSI termed as third-party PSI, whereby the intersection output of the two parties is only known to an inputless third party. In this setting, the two parties who participate in the protocol have no knowledge of the intersection result or any information of the set content of the other party. In general, third-party PSI settings arise where there is a need for an external party to obtain the intersection outcome without leakage of additional information to any other party. This setting is motivated by an increasing importance in several real-world applications. We describe protocols which achieve this functionality with minimal communication overhead. To the best of knowledge, our work is the first of its kind to explore this variant of PSI.

  匹配依据：MPC: private set intersection

  </details>

- **Invertible Quadratic Non-Linear Functions over $\\mathbb F\_p^n$ via Multiple Local Maps**
  2023-05-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/690)
  Ginevra Giordani, Lorenzo Grassi, Silvia Onofri, Marco Pedicini

  <details><summary>摘要 / Abstract</summary>

  The construction of invertible non-linear layers over $\mathbb F_p^n$ that minimize the multiplicative cost is crucial for the design of symmetric primitives targeting Multi Party Computation (MPC), Zero-Knowledge proofs (ZK), and Fully Homomorphic Encryption (FHE). At the current state of the art, only few non-linear functions are known to be invertible over $\mathbb F_p$, as the power maps $x\mapsto x^d$ for $\gcd(d,p-1)=1$. When working over $\mathbb F_p^n$ for $n\ge2$, a possible way to construct invertible non-linear layers $\mathcal S$ over $\mathbb F_p^n$ is by making use of a local map $F:\mathbb F_p^m\rightarrow \mathbb F_p$ for $m\le n$, that is, $\mathcal S_F(x_0, x_1, \ldots, x_{n-1}) = y_0\|y_1\|\ldots \|y_{n-1}$ where $y_i = F(x_i, x_{i+1}, \ldots, x_{i+m-1})$. This possibility has been recently studied by Grassi, Onofri, Pedicini and Sozzi at FSE/ToSC 2022. Given a quadratic local map $F:\mathbb F_p^m \rightarrow \mathbb F_p$ for $m\in\{1,2,3\}$, they proved that the shift-invariant non-linear function $\mathcal S_F$ over $\mathbb F_p^n$ defined as before is never invertible for any $n\ge 2\cdot m-1$. In this paper, we face the problem by generalizing such construction. Instead of a single local map, we admit multiple local maps, and we study the creation of nonlinear layers that can be efficiently verified and implemented by a similar shift-invariant lifting. After formally defining the construction, we focus our analysis on the case $\mathcal S_{F_0, F_1}(x_0, x_1, \ldots, x_{n-1}) = y_0\|y_1\|\ldots \|y_{n-1}$ for $F_0, F_1 :\mathbb F_p^2\rightarrow \mathbb F_p$ of degree at most 2. This is a generalization of the previous construction using two alternating functions $F_0,F_1$ instead of a single $F$. As main result, we prove that (i) if $n\ge3$, then $\mathcal S_{F_0, F_1}$ is never invertible if both $F_0$ and $F_1$ are quadratic, and that (ii) if $n\ge 4$, then $\mathcal S_{F_0, F_1}$ is invertible if and only if it is a Type-II Feistel scheme.

  匹配依据：MPC: multi party computation

  </details>

- **Characterization of Plotkin-optimal two-weight codes over finite chain rings and related applications**
  2023-05-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.08561)
  Shitao Li, Minjia Shi

  <details><summary>摘要 / Abstract</summary>

  Few-weight codes over finite chain rings are associated with combinatorial objects such as strongly regular graphs (SRGs), strongly walk-regular graphs (SWRGs) and finite geometries, and are also widely used in data storage systems and secret sharing schemes. The first objective of this paper is to characterize all possible parameters of Plotkin-optimal two-homogeneous weight regular projective codes over finite chain rings, as well as their weight distributions. We show the existence of codes with these parameters by constructing an infinite family of two-homogeneous weight codes. The parameters of their Gray images have the same weight distribution as that of the two-weight codes of type SU1 in the sense of Calderbank and Kantor (Bull Lond Math Soc 18: 97-122, 1986). Further, we also construct three-homogeneous weight regular projective codes over finite chain rings combined with some known results. Finally, we study applications of our constructed codes in secret sharing schemes and graph theory. In particular, infinite families of SRGs and SWRGs with non-trivial parameters are obtained.

  匹配依据：MPC: secret sharing

  </details>

- **MPC with Low Bottleneck-Complexity: Information-Theoretic Security and More**
  2023-05-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/683)
  Hannah Keller, Claudio Orlandi, Anat Paskin-Cherniavsky, Divya Ravi

  <details><summary>摘要 / Abstract</summary>

  The bottleneck-complexity (BC) of secure multiparty computation (MPC) protocols is a measure of the maximum number of bits which are sent and received by any party in a protocol. As the name suggests, the goal of studying BC-efficient protocols is to increase overall efficiency by making sure that the workload in the protocol is somehow &quot;amortized&#x27;&#x27; by the protocol participants. Orlandi et al. (PKC 2022) initiated the study of BC-efficient protocols from simple assumptions in the correlated randomness model and for semi-honest adversaries. In this work, we extend the study of Orlandi et al. in two primary directions: (a) to a larger and more general class of functions and (b) to the information-theoretic setting. In particular, we offer semi-honest secure protocols for the useful function classes of abelian programs, &#x27;read-$k$&#x27; non-abelian programs, and &#x27;read-$k$&#x27; generalized formulas. Our constructions use a novel abstraction, called &#x27;incremental function secret-sharing&#x27; (IFSS), that can be instantiated with unconditional security or from one-way functions (with different efficiency trade-offs).

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Private Polynomial Commitments and Applications to MPC**
  2023-05-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/680)
  Rishabh Bhadauria, Carmit Hazay, Muthuramakrishnan Venkitasubramaniam, Wenxuan Wu, Yupeng Zhang

  <details><summary>摘要 / Abstract</summary>

  Polynomial commitment schemes allow a prover to commit to a polynomial and later reveal the evaluation of the polynomial on an arbitrary point along with proof of validity. This object is central in the design of many cryptographic schemes such as zero-knowledge proofs and verifiable secret sharing. In the standard definition, the polynomial is known to the prover whereas the evaluation points are not private. In this paper, we put forward the notion of private polynomial commitments that capture additional privacy guarantees, where the evaluation points are hidden from the verifier while the polynomial is hidden from both. We provide concretely efficient constructions that allow simultaneously batch the verification of many evaluations with a small additive overhead. As an application, we design a new concretely efficient multi-party private set-intersection with malicious security and improved asymptotic communication and space complexities. We demonstrate the concrete efficiency of our construction via an implementation. Our scheme can prove $2^{10}$ evaluations of a private polynomial of degree $2^{10}$ in 157s. The proof size is only 169KB and the verification time is 11.8s. Moreover, we also implemented the multi-party private set intersection protocol and scale it to 1000 parties (which has not been shown before). The total running time for $2^{14}$ elements per party is 2,410 seconds. While existing protocols offer better computational complexity, our scheme offers significantly smaller communication and better scalability (in the number of parties) owing to better memory usage.

  匹配依据：MPC: private set intersection, secret sharing

  </details>

- **Privacy-Preserving Adaptive Traffic Signal Control in a Connected Vehicle Environment**
  2023-05-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.07212)
  Chaopeng Tan, Kaidi Yang

  <details><summary>摘要 / Abstract</summary>

  Although Connected Vehicles (CVs) have demonstrated tremendous potential to enhance traffic operations, they can impose privacy risks on individual travelers, e.g., leaking sensitive information about their frequently visited places, routing behavior, etc. Despite the large body of literature that devises various algorithms to exploit CV information, research on privacy-preserving traffic control is still in its infancy. In this paper, we aim to fill this research gap and propose a privacy-preserving adaptive traffic signal control method using CV data. Specifically, we leverage secure Multi-Party Computation and differential privacy to devise a privacy-preserving CV data aggregation mechanism, which can calculate key traffic quantities without any CVs having to reveal their private data. We further develop a linear optimization model for adaptive signal control based on the traffic variables obtained via the data aggregation mechanism. The proposed linear programming problem is further extended to a stochastic programming problem to explicitly handle the noises added by the differentially private mechanism. Evaluation results show that the linear optimization model preserves privacy with a marginal impact on control performance, and the stochastic programming model can significantly reduce residual queues compared to the linear programming model, with almost no increase in vehicle delay. Overall, our methods demonstrate the feasibility of incorporating privacy-preserving mechanisms in CV-based traffic modeling and control, which guarantees both utility and privacy.

  匹配依据：MPC: secure multi party computation

  </details>

- **Behemoth: transparent polynomial commitment scheme with constant opening proof size and verifier time**
  2023-05-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/670)
  István András Seres, Péter Burcsi

  <details><summary>摘要 / Abstract</summary>

  Polynomial commitment schemes are fundamental building blocks in numerous cryptographic protocols such as verifiable secret sharing, zero-knowledge succinct non-interactive arguments, and many more. The most efficient polynomial commitment schemes rely on a trusted setup which is undesirable in trust-minimized applications, e.g., cryptocurrencies. However, transparent polynomial commitment schemes are inefficient (polylogarithmic opening proofs and/or verification time) compared to their trusted counterparts. It has been an open problem to devise a transparent, succinct polynomial commitment scheme or prove an impossibility result in the transparent setting. In this work, for the first time, we create a transparent, constant-size polynomial commitment scheme called Behemoth with constant-size opening proofs and a constant-time verifier. The downside of Behemoth is that it employs a cubic prover in the degree of the committed polynomial. We prove the security of our scheme in the generic group model and discuss parameter settings in which it remains practical even for the prover.

  匹配依据：MPC: secret sharing

  </details>

- **Universally Composable Simultaneous Broadcast against a Dishonest Majority and Applications**
  2023-05-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.06468)
  Myrto Arapinis, Ábel Kocsis, Nikolaos Lamprou, Liam Medley, Thomas Zacharias

  <details><summary>摘要 / Abstract</summary>

  Simultaneous broadcast (SBC) protocols [Chor et al., FOCS 1985] constitute a special class of broadcast channels which have proved extremely useful in the design of various distributed computing constructions (e.g., multiparty computation, coin flipping, e-voting, fair bidding). As with any communication channel, it is crucial that SBC security is composable, i.e., it is preserved under concurrent protocol executions. The work of [Hevia, SCN 2006] proposes a formal treatment of SBC in the Universal Composability (UC) framework [Canetti, FOCS 2001] and a construction secure assuming an honest majority. In this work, we provide a comprehensive revision of SBC in the UC setting and improve the results of [Hevia, SCN 2006]. In particular, we present a new SBC functionality that captures both simultaneity and liveness by considering a broadcast period such that (i) within this period all messages are broadcast independently and (ii) after the period ends, the session is terminated without requiring participation of all parties. Next, we employ time-lock encryption (TLE) over a standard broadcast channel to devise an SBC protocol that realizes our functionality against any adaptive adversary corrupting up to all-but-one parties. In our study, we capture synchronicity via a global clock [Katz et al., TCC 2013], thus lifting the restrictions of the original synchronous communication setting used in [Hevia, SCN 2006]. As a building block of independent interest, we prove the first TLE protocol that is adaptively secure in the UC setting, strengthening the main result of [Arapinis et al., ASIACRYPT 2021]. Finally, we formally exhibit the power of our SBC construction in the design of UC-secure applications by presenting two interesting use cases: (i) distributed generation of uniform random strings, and (ii) decentralized electronic voting systems, without the presence of a special trusted party.

  匹配依据：MPC: multiparty computation

  </details>

- **MPC in the head for isomorphisms and group actions**
  2023-05-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/664)
  Antoine Joux

  <details><summary>摘要 / Abstract</summary>

  In this paper, we take inspiration from an invited talk presented at CBCrypto&#x27;23 to design identification protocols and signature schemes from group actions using the MPC-in-the-head paradigm. We prove the security of the given identification schemes and rely on the Fiat-Shamir transformation to turn them into signatures. We also establish a parallel with the technique used for the MPC-in-the-head approach and the seed tree method that has been recently used in some signature and ring signatures algorithms based on group action problems.

  匹配依据：MPC: mpc (context)

  </details>

- **Controlled State Reconstruction and Quantum Secret Sharing**
  2023-05-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.06062)
  Pahulpreet Singh, Indranil Chakrabarty

  <details><summary>摘要 / Abstract</summary>

  In this article, we present a benchmark for resource characterization in the process of controlled quantum state reconstruction and secret sharing for general three-qubit states. This is achieved by providing a closed expression for the reconstruction fidelity, which relies on the genuine tripartite correlation and the bipartite channel between the dealer and the reconstructor characterized by the respective correlation parameters. We formulate the idea of quantum advantage in approximate state reconstruction as surpassing the classical limit set at 2/3. This article brings out new interoperability between teleportation and state reconstruction. This is detailed through a case-by-case analysis of relevant correlation matrices. We are reformulating the idea of quantum secret sharing by setting up additional constraints on the teleportation capacity of the bipartite channels between the dealer and shareholders by ensuring that, individually, the shareholders cannot reconstruct the secret. We believe that this will give us the ideal picture of how quantum secret sharing should be.

  匹配依据：MPC: secret sharing

  </details>

- **Griffin: Towards Mixed Multi-Key Homomorphic Encryption**
  2023-05-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/654)
  Thomas Schneider, Hossein Yalame, Michael Yonli

  <details><summary>摘要 / Abstract</summary>

  This paper presents Griffin, an extension of the mixed-scheme single-key homomorphic encryption framework Pegasus (Lu et al., IEEE S&amp;P’21) to a Multi-Key Homomorphic Encryption (MKHE) scheme with applications to secure computation. MKHE is a generalized notion of Homomorphic Encryption (HE) that allows for operations on ciphertexts encrypted under different keys. However, an efficient approach to evaluate both polynomial and non-polynomial functions on encrypted data in MKHE has not yet been developed, hindering the deployment of HE to real-life applications. Griffin addresses this challenge by introducing a method for transforming between MKHE ciphertexts of different schemes. The practicality of Griffin is demonstrated through benchmarks with multiple applications, including the sorting of sixty four 45-bit fixed point numbers with a precision of 7 bits in 21 minutes, and evaluating arbitrary functions with a one-time setup communication of 1.4 GB per party and 2.34 MB per ciphertext. Moreover, Griffin could compute the maximum of two numbers in 3.2 seconds, a 2× improvement over existing MKHE approaches that rely on a single scheme.

  匹配依据：MPC: secure computation

  </details>

- **ScionFL: Efficient and Robust Secure Quantized Aggregation**
  2023-05-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.07376) · [IACR ePrint](https://eprint.iacr.org/2023/652)
  Yaniv Ben-Itzhak, Helen Möllering, Benny Pinkas, Thomas Schneider, Ajith Suresh, Oleksandr Tkachenko, Shay Vargaftik, Christian Weinert, Hossein Yalame, Avishay Yanai

  <details><summary>摘要 / Abstract</summary>

  Secure aggregation is commonly used in federated learning (FL) to alleviate privacy concerns related to the central aggregator seeing all parameter updates in the clear. Unfortunately, most existing secure aggregation schemes ignore two critical orthogonal research directions that aim to (i) significantly reduce client-server communication and (ii) mitigate the impact of malicious clients. However, both of these additional properties are essential to facilitate cross-device FL with thousands or even millions of (mobile) participants. In this paper, we unite both research directions by introducing ScionFL, the first secure aggregation framework for FL that operates efficiently on quantized inputs and simultaneously provides robustness against malicious clients. Our framework leverages (novel) multi-party computation (MPC) techniques and supports multiple linear (1-bit) quantization schemes, including ones that utilize the randomized Hadamard transform and Kashin&#x27;s representation. Our theoretical results are supported by extensive evaluations. We show that with no overhead for clients and moderate overhead for the server compared to transferring and processing quantized updates in plaintext, we obtain comparable accuracy for standard FL benchmarks. Moreover, we demonstrate the robustness of our framework against state-of-the-art poisoning attacks.

  匹配依据：MPC: multi party computation

  </details>

- **Pseudorandom Correlation Functions from Variable-Density LPN, Revisited**
  2023-05-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/650)
  Geoffroy Couteau, Clément Ducros

  <details><summary>摘要 / Abstract</summary>

  Pseudorandom correlation functions (PCF), introduced in the work of (Boyle et al., FOCS 2020), allow two parties to locally gen- erate, from short correlated keys, a near-unbounded amount of pseu- dorandom samples from a target correlation. PCF is an extremely ap- pealing primitive in secure computation, where they allow to confine all preprocessing phases of all future computations two parties could want to execute to a single short interaction with low communication and computation, followed solely by offline computations. Beyond in- troducing the notion, Boyle et al. gave a candidate construction, using a new variable-density variant of the learning parity with noise (LPN) assumption. Then, to provide support for this new assumption, the au- thors showed that it provably resists a large class of linear attacks, which captures in particular all known attacks on LPN. In this work, we revisit the analysis of the VDLPN assumption. We make two key contributions: – First, we observe that the analysis of Boyle et al is purely asymp- totic: they do not lead to any concrete and efficient PCF instanti- ation within the bounds that offer security guarantees. To improve this state of affairs, we combine a new variant of a VDLPN assump- tion with an entirely new, much tighter security analysis, which we further tighten using extensive computer simulations to optimize pa- rameters. This way, we manage to obtain for the first time a set of provable usable parameters (under a simple combinatorial conjec- ture which is easy to verify experimentally), leading to a concretely efficient PCF resisting all linear tests. – Second, we identify a flaw in the security analysis of Boyle et al., which invalidates their proof that VDLPN resists linear attacks. Us- ing several new non-trivial arguments, we repair the proof and fully demonstrate that VDLPN resists linear attack; our new analysis is more involved than the original (flawed) analysis. Our parameters set leads to PCFs with keys around 3MB allowing ∼ 500 evaluations per second on one core of a standard laptop for 110 bits of security; these numbers can be improved to 350kB keys and ∼ 3950 evaluations/s using a more aggressive all-prefix variant. All numbers are quite tight: only within a factor 3 of the best bounds one could heuristically hope for.

  匹配依据：MPC: secure computation

  </details>

- **Communication complexity of entanglement assisted multi-party computation**
  2023-05-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.04435)
  Ruoyu Meng, Aditya Ramamoorthy

  <details><summary>摘要 / Abstract</summary>

  We consider a quantum and classical version multi-party function computation problem with $n$ players, where players $2, \dots, n$ need to communicate appropriate information to player 1, so that a &quot;generalized&quot; inner product function with an appropriate promise can be calculated. The communication complexity of a protocol is the total number of bits that need to be communicated. When $n$ is prime and for our chosen function, we exhibit a quantum protocol (with complexity $(n-1) \log n$ bits) and a classical protocol (with complexity $(n-1)^2 (\log n^2$) bits). In the quantum protocol, the players have access to entangled qudits but the communication is still classical. Furthermore, we present an integer linear programming formulation for determining a lower bound on the classical communication complexity. This demonstrates that our quantum protocol is strictly better than classical protocols.

  匹配依据：MPC: multi party computation

  </details>

- **Privacy-Preserving Regular Expression Matching using Nondeterministic Finite Automata**
  2023-05-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/643)
  Ning Luo, Chenkai Weng, Jaspal Singh, Gefei Tan, Ruzica Piskac, Mariana Raykova

  <details><summary>摘要 / Abstract</summary>

  Motivated by the privacy requirements in network intrusion detection and DNS policy checking, we have developed a suite of protocols and algorithms for regular expression matching with enhanced privacy: - A new regular expression matching algorithm that is oblivious to the input strings, of which the complexity is only $O(mn)$ where $m$ and $n$ are the length of strings and the regular expression respectively. It is achieved by exploiting the structure of the Thompson nondeterministic automata. - A zero-knowledge proof of regular expression pattern matching in which a prover generates a proof to demonstrate that a public regular expression matches her input string without revealing the string itself. -Two secure-regex protocols that ensure the privacy of both the string and regular expression. The first protocol is based on the oblivious stack and reduces the complexity of the state-of-the-art from $O(mn^2)$ to $O(mn\log n)$. The second protocol relies on the oblivious transfer and performs better empirically when the size of regular expressions is smaller than $2^{12}$. We also evaluated our protocols in the context of encrypted DNS policy checking and intrusion detection and achieved 4.5X improvements over the state-of-the-art. These results also indicate the practicality of our approach in real-world applications.

  匹配依据：MPC: oblivious transfer

  </details>

- **OPRFs from Isogenies: Designs and Analysis**
  2023-05-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/639)
  Lena Heimberger, Tobias Hennerbichler, Fredrik Meisingseth, Sebastian Ramacher, Christian Rechberger

  <details><summary>摘要 / Abstract</summary>

  Oblivious Pseudorandom Functions (OPRFs) are an elementary building block in cryptographic and privacy-preserving applications. However, while there are numerous pre-quantum secure OPRF constructions, few options exist in a post-quantum secure setting, and of those even fewer are practical for modern-day applications. In this work, we focus on isogeny group actions, as the associated low bandwidth leads to efficient constructions. Our results focus on the Naor-Reingold OPRF. We introduce OPUS, a novel OPRF from isogenies without oblivious transfer, and show efficient evaluations of the Naor-Reingold PRF using CSIDH and CSI-FiSh. Additionally, we analyze a previous proposal of a CSIDH-based OPRF and that the straightforward instantiation of the protocol leaks the server’s private key. As a result, we propose mitigations to address those shortcomings, which require additional hardness assumptions. Our results report a very competitive protocol when combined with lattices for Oblivious Transfer. Our comparison against the state of the art shows that OPUS and the repaired, generic construction are competitive with other proposals in terms of speed and communication size. More concretely, OPUS achieves almost two orders of magnitude less communication overhead compared to the next-best lattice-based OPRF at the cost of higher latency and higher computational cost, and the repaired construction. Finally, we demonstrate the efficiency of OPUS and the generic NR-OT in two use cases: first, we instantiate OPAQUE, a protocol for asymmetric authenticated key exchange. Compared to classical elliptic curve cryptography, this results in less than 100 × longer computation on average and around 1000× more communication overhead. Second, we perform an unbalanced private set intersection and show that the communication overhead can be roughly the same when using isogenies or elliptic curves, at the cost of much higher runtime. Conversely, for sets of the size 210 , we report a runtime around 200× slower than the elliptic curve PSI. This concretizes the overhead of performing PSI and using OPAQUE with isogenies for the first time

  匹配依据：MPC: oblivious transfer, private set intersection

  </details>

- **Weight hierarchies of three-weight $p$-ary linear codes from inhomogeneous quadratic forms**
  2023-05-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.01891)
  Shupeng Hu, Fei Li, Xiumei Li

  <details><summary>摘要 / Abstract</summary>

  The weight distribution and weight hierarchy of a linear code are two important research topics in coding theory. In this paper, choosing $ D=\Big\{(x,y)\in \Big(\F_{p^{s_1}}\times\F_{p^{s_2}}\Big)\Big\backslash\{(0,0)\}: f(x)+\Tr_1^{s_2}(αy)=0\Big\}$ as a defining set , where $α\in\mathbb{F}_{p^{s_2}}^*$ and $f(x)$ is a quadratic form over $\mathbb{F}_{p^{s_1}}$ with values in $\F_p$, whether $f(x)$ is non-degenerate or not, we construct a family of three-weight $p$-ary linear codes and determine their weight distributions and weight hierarchies. Most of the codes can be used in secret sharing schemes.

  匹配依据：MPC: secret sharing

  </details>

- **SEC: Symmetric Encrypted Computation via Fast Look-ups**
  2023-05-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/628)
  Debadrita Talapatra, Nimish Mishra, Arnab Bag, Sikhar Patranabis, Debdeep Mukhopadhyay

  <details><summary>摘要 / Abstract</summary>

  Garbled Circuits (GCs) and Fully Homomorphic Encryption (FHE) are state-of-the-art general-purpose primitives allowing a client to securely outsource the storage and processing of sensitive private data to an untrusted third party cloud server. GCs provide data privacy and function privacy while being efficient, but suffer from non-reusability of its translation tables. On the other extreme, FHE enables arbitrary encrypted computation ensuring data-privacy but suffers from huge computation overhead and limited scalability. Here, we explore the following question- Can encrypted computation guaranteeing data privacy be enabled through use of encrypted lookup tables (like GC) that are reusable for practically large circuits? Such a solution will retain the efficiency of GCs (because of encrypted table lookups); and while it cannot achieve unbounded reusability (like FHE, because of the inclination on computation rather than lookups), an interesting question is whether its reusability bound can be made sufficient for practically large circuits. In this work, we propose Symmetric Encrypted Computation (SEC), the first practically efficient and provably secure lookup-based construction that supports reusable evaluations of arbitrary Boolean circuits over symmetrically encrypted data, while ensuring data-privacy guarantees. With a single setup of encrypted look-up tables, SEC supports O(k) re-evaluations of the same circuit of size n (for client controlled k (≥ n)). Such reusability improves upon GC and is asymptotically large enough to scale to practical deployments of realistic circuits; also note that SEC completely bypasses bootstrapping, thereby being more efficient than FHE. This is achieved by relying on purely symmetric-key crypto-primitives by extending and generalizing the functional capabilities of Searchable Symmetric Encryption (SSE), while inheriting its desirable performance benefits. Reusability through SSE without leakage is ensured in SEC by the design choice to treat a generic 2-input Boolean gate as a 3-input encrypted query, with the third input randomizing access patterns across reuse. We provide a concrete construction of SEC and analyze its security with respect to a rigorous leakage profile. We also experimentally validate its practical efficiency. SEC outperforms state-of-the-art FHE schemes (such as Torus FHE) substantially. We further showcase the scalability of SEC for functions with multi-bit inputs via experiments performing encrypted evaluation of the entire AES-128 circuit, as well as the max-pooling layers of AlexNet architecture. For both sets of experiments, SEC outperforms state-of-the-art unaccelerated FHE implementations by 1000× in terms of processing time, while incurring 250× lower storage.

  匹配依据：MPC: garbled circuits

  </details>

- **Conflict Checkable and Decodable Codes and Their Applications**
  2023-05-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/627)
  Benny Applebaum, Eliran Kachlon

  <details><summary>摘要 / Abstract</summary>

  Let $C$ be an error-correcting code over a large alphabet $q$ of block length $n$, and assume that, a possibly corrupted, codeword $c$ is distributively stored among $n$ servers where the $i$th entry is being held by the $i$th server. Suppose that every pair of servers publicly announce whether the corresponding coordinates are ``consistent&#x27;&#x27; with some legal codeword or ``conflicted&#x27;&#x27;. What type of information about $c$ can be inferred from this consistency graph? Can we check whether errors occurred and if so, can we find the error locations and effectively decode? We initiate the study of conflict-checkable and conflict-decodable codes and prove the following main results: (1) (Almost-MDS conflict-checkable codes:) For every distance $d\leq n$, there exists a code that supports conflict-based error-detection whose dimension $k$ almost achieves the singleton bound, i.e., $k\geq n-d+0.99$. Interestingly, the code is non-linear, and we give some evidence that suggests that this is inherent. Combinatorially, this yields an $n$-partite graph over $[q]^n$ that contains $q^k$ cliques of size $n$ whose pair-wise intersection is at most $n-d\leq k-0.99$ vertices, generalizing a construction of Alon (Random Struct. Algorithms, &#x27;02) that achieves a similar result for the special case of triangles ($n=3$). (2) (Conflict Decodable Codes below half-distance:) For every distance $d\leq n$ there exists a linear code that supports conflict-based error-decoding up to half of the distance. The code&#x27;s dimension $k$ ``half-meets&#x27;&#x27; the singleton bound, i.e., $k=(n-d+2)/2$, and we prove that this bound is tight for a natural class of such codes. The construction is based on symmetric bivariate polynomials and is rooted in the literature on verifiable secret sharing (Ben-Or, Goldwasser and Wigderson, STOC &#x27;88; Cramer, Damgård, and Maurer, EUROCRYPT &#x27;00). (3) (Robust Conflict Decodable Codes:) We show that the above construction also satisfies a non-trivial notion of robust decoding/detection even when the number of errors is unbounded and up to $d/2$ of the servers are Byzantine and may lie about their conflicts. The resulting conflict-decoder runs in exponential time in this case, and we present an alternative construction that achieves quasipolynomial complexity at the expense of degrading the dimension to $k=(n-d+3)/3$. Our construction is based on trilinear polynomials, and the algorithmic result follows by showing that the induced conflict graph is structured enough to allow efficient recovery of a maximal vertex cover. As an application of the last result, we present the first polynomial-time statistical two-round Verifiable Secret Sharing (resp., three-round general MPC protocol) that remains secure in the presence of an active adversary that corrupts up to $t&lt;n/3.001$ of the parties. We can upgrade the resiliency threshold to $n/3$, which is known to be optimal in this setting, at the expense of increasing the computational complexity to be quasipolynomial. Previous solutions (Applebaum, Kachlon, and Patra, TCC&#x27;20) suffered from an exponential-time complexity even when the adversary corrupts only $n/4$ of the parties.

  匹配依据：MPC: secret sharing

  </details>

- **GTree: GPU-Friendly Privacy-preserving Decision Tree Training and Inference**
  2023-05-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.00645)
  Qifan Wang, Shujie Cui, Lei Zhou, Ye Dong, Jianli Bai, Yun Sing Koh, Giovanni Russello

  <details><summary>摘要 / Abstract</summary>

  Decision tree (DT) is a widely used machine learning model due to its versatility, speed, and interpretability. However, for privacy-sensitive applications, outsourcing DT training and inference to cloud platforms raise concerns about data privacy. Researchers have developed privacy-preserving approaches for DT training and inference using cryptographic primitives, such as Secure Multi-Party Computation (MPC). While these approaches have shown progress, they still suffer from heavy computation and communication overheads. Few recent works employ Graphical Processing Units (GPU) to improve the performance of MPC-protected deep learning. This raises a natural question: \textit{can MPC-protected DT training and inference be accelerated by GPU?} We present GTree, the first scheme that uses GPU to accelerate MPC-protected secure DT training and inference. GTree is built across 3 parties who securely and jointly perform each step of DT training and inference with GPU. Each MPC protocol in GTree is designed in a GPU-friendly version. The performance evaluation shows that GTree achieves ${\thicksim}11{\times}$ and ${\thicksim}21{\times}$ improvements in training SPECT and Adult datasets, compared to the prior most efficient CPU-based work. For inference, GTree shows its superior efficiency when the DT has less than 10 levels, which is $126\times$ faster than the prior most efficient work when inferring $10^4$ instances with a tree of 7 levels. GTree also achieves a stronger security guarantee than prior solutions, which only leaks the tree depth and size of data samples while prior solutions also leak the tree structure. With \textit{oblivious array access}, the access pattern on GPU is also protected.

  匹配依据：MPC: secure multi party computation

  </details>

- **vetKeys: How a Blockchain Can Keep Many Secrets**
  2023-04-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/616)
  Andrea Cerulli, Aisling Connolly, Gregory Neven, Franz-Stefan Preiss, Victor Shoup

  <details><summary>摘要 / Abstract</summary>

  We propose a new cryptographic primitive called &quot;verifiably encrypted threshold key derivation&quot; (vetKD) that extends identity-based encryption with a decentralized way of deriving decryption keys. We show how vetKD can be leveraged on modern blockchains to build scalable decentralized applications (or &quot;dapps&quot;) for a variety of purposes, including preventing front-running attacks on decentralized finance (DeFi) platforms, end-to-end encryption for decentralized messaging and social networks (SocialFi), cross-chain bridges, as well as advanced cryptographic primitives such as witness encryption and one-time programs that previously could only be built from secure hardware or using a trusted third party. And all of that by secret-sharing just a single secret key...

  匹配依据：MPC: secret sharing

  </details>

- **Computational Quantum Secret Sharing**
  2023-04-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.00356) · [IACR ePrint](https://eprint.iacr.org/2023/613)
  Alper Çakan, Vipul Goyal, Chen-Da Liu-Zhang, João Ribeiro, Alper Cakan

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing (QSS) allows a dealer to distribute a secret quantum state among a set of parties so that certain subsets can reconstruct the secret, while unauthorized subsets obtain no information. While QSS was introduced over twenty years ago, previous works focused only on existence of perfectly secure schemes, and the share size of the known schemes is exponential even for access structures computed by polynomial size monotone circuits. This stands in contrast to the classical case, where efficient computationally-secure schemes have been long known for all access structures in $\mathsf{monotone~P}$, and one can even obtain shares which are much shorter than the secret which is impossible with perfect security. In this work, we initiate the study of computationally-secure QSS and show that computational assumptions help significantly in building QSS schemes. We present a simple compiler and use it to obtain a large variety results: We construct polynomial-time QSS schemes under standard assumptions for a rich class of access structures. This includes many access structures for which previous results in QSS required exponential share size. We also construct QSS schemes for which the size of the shares is significantly smaller than the size of the secret. As in the classical case, this is impossible with perfect security. We also use our compiler to obtain results beyond computational QSS. In the information-theoretic setting, we improve the share size of perfect QSS schemes for a large class of access structures to $1.5^{n+o(n)}$, improving upon best known schemes and matching the best known result for general access structures in the classical case. Finally, we show construct efficient schemes for all access structures in $\mathsf{P}$ and $\mathsf{NP}$ when the quantum secret sharing scheme is given multiple of copies of the secret.

  匹配依据：MPC: secret sharing

  </details>

- **Secure and Private Vickrey Auction Protocols: A Secure Multiparty Computation Approach**
  2023-04-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.14626)
  Lucy Klinger, Mengfan Lyu, Lei Zhang

  <details><summary>摘要 / Abstract</summary>

  Recent attention on secure multiparty computation and blockchain technology has garnered new interest in developing auction protocols in a decentralized setting. In this paper, we propose a secure and private Vickrey auction protocol that addresses the challenge of maintaining auction correctness while preserving the confidentiality of bidders&#x27; information. Our protocol leverages secure multiparty computation (SMPC) techniques that enable decentralized computation of the final payment price without disclosing additional information. The total computational complexity of our proposed protocol, including preparation, is $O(n^2 k)$, and the complexity for the main auction is $O(n k)$. Furthermore, we show that our protocol is resistant to collusion and the auction outcome is publicly verifiable, which prevents dishonest bidders from altering this outcome.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Randomness Requirements for Three-Secret Sharing**
  2023-04-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.14934)
  Hari Krishnan P. Anilkumar, Aayush Rajesh, Varun Narayanan, Manoj M. Prabhakaran, Vinod M. Prabhakaran

  <details><summary>摘要 / Abstract</summary>

  We study a secret sharing problem with three secrets where the secrets are allowed to be related to each other, i.e., only certain combinations of the three secrets are permitted. The dealer produces three shares such that every pair of shares reveals a unique secret and reveals nothing about the other two secrets, other than what can be inferred from the revealed secret. For the case of binary secrets, we exactly determine the minimum amount of randomness required by the dealer, for each possible set of permitted combinations. Our characterization is based on new lower and upper bounds.

  匹配依据：MPC: secret sharing

  </details>

- **Private Information Retrieval and Its Applications: An Introduction, Open Problems, Future Directions**
  2023-04-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.14397)
  Sajani Vithana, Zhusheng Wang, Sennur Ulukus

  <details><summary>摘要 / Abstract</summary>

  Private information retrieval (PIR) is a privacy setting that allows a user to download a required message from a set of messages stored in a system of databases without revealing the index of the required message to the databases. PIR was introduced under computational privacy guarantees, and is recently re-formulated to provide information-theoretic guarantees, resulting in \emph{information theoretic privacy}. Subsequently, many important variants of the basic PIR problem have been studied focusing on fundamental performance limits as well as achievable schemes. More recently, a variety of conceptual extensions of PIR have been introduced, such as, private set intersection (PSI), private set union (PSU), and private read-update-write (PRUW). Some of these extensions are mainly intended to solve the privacy issues that arise in distributed learning applications due to the extensive dependency of machine learning on users&#x27; private data. In this article, we first provide an introduction to basic PIR with examples, followed by a brief description of its immediate variants. We then provide a detailed discussion on the conceptual extensions of PIR, along with potential research directions.

  匹配依据：MPC: private set intersection, private set union

  </details>

- **SMPC-based Federated Learning for 6G enabled Internet of Medical Things**
  2023-04-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.13352)
  Aditya Pribadi Kalapaaking, Veronika Stephanie, Ibrahim Khalil, Mohammed Atiquzzaman, Xun Yi, Mahathir Almashor

  <details><summary>摘要 / Abstract</summary>

  Rapidly developing intelligent healthcare systems are underpinned by Sixth Generation (6G) connectivity, ubiquitous Internet of Things (IoT), and Deep Learning (DL) techniques. This portends a future where 6G powers the Internet of Medical Things (IoMT) with seamless, large-scale, and real-time connectivity amongst entities. This article proposes a Convolutional Neural Network (CNN) based Federated Learning framework that combines Secure Multi-Party Computation (SMPC) based aggregation and Encrypted Inference methods, all within the context of 6G and IoMT. We consider multiple hospitals with clusters of mixed IoMT and edge devices that encrypt locally trained models. Subsequently, each hospital sends the encrypted local models for SMPC-based encrypted aggregation in the cloud, which generates the encrypted global model. Ultimately, the encrypted global model is returned to each edge server for more localized training, further improving model accuracy. Moreover, hospitals can perform encrypted inference on their edge servers or the cloud while maintaining data and model privacy. Multiple experiments were conducted with varying CNN models and datasets to evaluate the proposed framework&#x27;s performance.

  匹配依据：MPC: secure multi party computation

  </details>

- **FedVS: Straggler-Resilient and Privacy-Preserving Vertical Federated Learning for Split Models**
  2023-04-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.13407) · [IACR ePrint](https://eprint.iacr.org/2023/597)
  Songze Li, Duanyi Yao, Jin Liu

  <details><summary>摘要 / Abstract</summary>

  In a vertical federated learning (VFL) system consisting of a central server and many distributed clients, the training data are vertically partitioned such that different features are privately stored on different clients. The problem of split VFL is to train a model split between the server and the clients. This paper aims to address two major challenges in split VFL: 1) performance degradation due to straggling clients during training; and 2) data and model privacy leakage from clients&#x27; uploaded data embeddings. We propose FedVS to simultaneously address these two challenges. The key idea of FedVS is to design secret sharing schemes for the local data and models, such that information-theoretical privacy against colluding clients and curious server is guaranteed, and the aggregation of all clients&#x27; embeddings is reconstructed losslessly, via decrypting computation shares from the non-straggling clients. Extensive experiments on various types of VFL datasets (including tabular, CV, and multi-view) demonstrate the universal advantages of FedVS in straggler mitigation and privacy protection over baseline protocols.

  匹配依据：MPC: secret sharing

  </details>

- **C2PI: An Efficient Crypto-Clear Two-Party Neural Network Private Inference**
  2023-04-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.13266)
  Yuke Zhang, Dake Chen, Souvik Kundu, Haomei Liu, Ruiheng Peng, Peter A. Beerel

  <details><summary>摘要 / Abstract</summary>

  Recently, private inference (PI) has addressed the rising concern over data and model privacy in machine learning inference as a service. However, existing PI frameworks suffer from high computational and communication costs due to the expensive multi-party computation (MPC) protocols. Existing literature has developed lighter MPC protocols to yield more efficient PI schemes. We, in contrast, propose to lighten them by introducing an empirically-defined privacy evaluation. To that end, we reformulate the threat model of PI and use inference data privacy attacks (IDPAs) to evaluate data privacy. We then present an enhanced IDPA, named distillation-based inverse-network attack (DINA), for improved privacy evaluation. Finally, we leverage the findings from DINA and propose C2PI, a two-party PI framework presenting an efficient partitioning of the neural network model and requiring only the initial few layers to be performed with MPC protocols. Based on our experimental evaluations, relaxing the formal data privacy guarantees C2PI can speed up existing PI frameworks, including Delphi [1] and Cheetah [2], up to 2.89x and 3.88x under LAN and WAN settings, respectively, and save up to 2.75x communication costs.

  匹配依据：MPC: multi party computation

  </details>

- **Breaking barriers in two-party quantum cryptography via stochastic semidefinite programming**
  2023-04-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.13200)
  Akshay Bansal, Jamie Sikora

  <details><summary>摘要 / Abstract</summary>

  In the last two decades, there has been much effort in finding secure protocols for two-party cryptographic tasks. It has since been discovered that even with quantum mechanics, many such protocols are limited in their security promises. In this work, we use stochastic selection, an idea from stochastic programming, to circumvent such limitations. For example, we find a way to switch between bit commitment, weak coin flipping, and oblivious transfer protocols to improve their security. We also use stochastic selection to turn trash into treasure yielding the first quantum protocol for Rabin oblivious transfer.

  匹配依据：MPC: oblivious transfer

  </details>

- **Blockchain-based Federated Learning with SMPC Model Verification Against Poisoning Attack for Healthcare Systems**
  2023-04-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.13360)
  Aditya Pribadi Kalapaaking, Ibrahim Khalil, Xun Yi

  <details><summary>摘要 / Abstract</summary>

  Due to the rising awareness of privacy and security in machine learning applications, federated learning (FL) has received widespread attention and applied to several areas, e.g., intelligence healthcare systems, IoT-based industries, and smart cities. FL enables clients to train a global model collaboratively without accessing their local training data. However, the current FL schemes are vulnerable to adversarial attacks. Its architecture makes detecting and defending against malicious model updates difficult. In addition, most recent studies to detect FL from malicious updates while maintaining the model&#x27;s privacy have not been sufficiently explored. This paper proposed blockchain-based federated learning with SMPC model verification against poisoning attacks for healthcare systems. First, we check the machine learning model from the FL participants through an encrypted inference process and remove the compromised model. Once the participants&#x27; local models have been verified, the models are sent to the blockchain node to be securely aggregated. We conducted several experiments with different medical datasets to evaluate our proposed framework.

  匹配依据：MPC: smpc (context)

  </details>

- **Implementing and Optimizing Matrix Triples with Homomorphic Encryption**
  2023-04-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/593)
  Johannes Mono, Tim Güneysu

  <details><summary>摘要 / Abstract</summary>

  In today’s interconnected world, data has become a valuable asset, leading to a growing interest in protecting it through techniques such as privacy-preserving computation. Two well-known approaches are multi-party computation and homomorphic encryption with use cases such as privacy-preserving machine learning evaluating or training neural networks. For multi-party computation, one of the fundamental arithmetic operations is the secure multiplication in the malicious security model and by extension the multiplication of matrices which is expensive to compute in the malicious model. Transferring the problem of secure matrix multiplication to the homomorphic domain enables savings in communication complexity, reducing the main bottleneck. In this work, we implement and optimize the homomorphic generation of matrix triples. We provide an open-source implementation for the leveled BGV (Brakerski Gentry Vaikuntanathan) scheme supporting plaintext moduli of arbitrary size using state-of-the-art implementation techniques. We also provide a new, use-case specific approach to parameter generation for leveled BGV-like schemes heuristically optimizing for computation time and taking into account architecture-specific constraints. Finally, we provide an in-depth analysis of the homomorphic circuit enabling the re-use of key switching keys and eliminating constant multiplications, combining our results in an implementation to generate homomorphic matrix triples for arbitrary plaintext moduli. Our implementation is publicly available and up to $2.1\times$ faster compared to previous work while also providing new time-memory trade-offs for different computing environments. Furthermore, we implement and evaluate additional, use-case specific optimization opportunities such as matrix slicing for the matrix triple generation.

  匹配依据：MPC: multi party computation

  </details>

- **General-Purpose Secure Conflict-free Replicated Data Types**
  2023-04-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/584)
  Bernardo Portela, Hugo Pacheco, Pedro Jorge, Rogério Pontes

  <details><summary>摘要 / Abstract</summary>

  Conflict-free Replicated Data Types (CRDTs) are a very popular class of distributed data structures that strike a compromise between strong and eventual consistency. Ensuring the protection of data stored within a CRDT, however, cannot be done trivially using standard encryption techniques, as secure CRDT protocols would require replica-side computation. This paper proposes an approach to lift general-purpose implementations of CRDTs to secure variants using secure multiparty computation (MPC). Each replica within the system is realized by a group of MPC parties that compute its functionality. Our results include: i) an extension of current formal models used for reasoning over the security of CRDT solutions to the MPC setting; ii) a MPC language and type system to enable the construction of secure versions of CRDTs and; iii) a proof of security that relates the security of CRDT constructions designed under said semantics to the underlying MPC library. We provide an open-source system implementation with an extensive evaluation, which compares different designs with their baseline throughput and latency.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Securing Neural Networks with Knapsack Optimization**
  2023-04-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.10442) · [Code](https://github.com/yg320/secure_inference)
  Yakir Gorski, Amir Jevnisek, Shai Avidan

  <details><summary>摘要 / Abstract</summary>

  MLaaS Service Providers (SPs) holding a Neural Network would like to keep the Neural Network weights secret. On the other hand, users wish to utilize the SPs&#x27; Neural Network for inference without revealing their data. Multi-Party Computation (MPC) offers a solution to achieve this. Computations in MPC involve communication, as the parties send data back and forth. Non-linear operations are usually the main bottleneck requiring the bulk of communication bandwidth. In this paper, we focus on ResNets, which serve as the backbone for many Computer Vision tasks, and we aim to reduce their non-linear components, specifically, the number of ReLUs. Our key insight is that spatially close pixels exhibit correlated ReLU responses. Building on this insight, we replace the per-pixel ReLU operation with a ReLU operation per patch. We term this approach &#x27;Block-ReLU&#x27;. Since different layers in a Neural Network correspond to different feature hierarchies, it makes sense to allow patch-size flexibility for the various layers of the Neural Network. We devise an algorithm to choose the optimal set of patch sizes through a novel reduction of the problem to the Knapsack Problem. We demonstrate our approach in the semi-honest secure 3-party setting for four problems: Classifying ImageNet using ResNet50 backbone, classifying CIFAR100 using ResNet18 backbone, Semantic Segmentation of ADE20K using MobileNetV2 backbone, and Semantic Segmentation of Pascal VOC 2012 using ResNet50 backbone. Our approach achieves competitive performance compared to a handful of competitors. Our source code is publicly available: https://github.com/yg320/secure_inference.

  匹配依据：MPC: multi party computation

  </details>

- **FUSE – Flexible File Format and Intermediate Representation for Secure Multi-Party Computation**
  2023-04-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/563)
  Lennart Braun, Moritz Huppert, Nora Khayata, Thomas Schneider, Oleksandr Tkachenko

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation (MPC) is continuously becoming more and more practical. Many optimizations have been introduced, making MPC protocols more suitable for solving real-world problems. However, the MPC protocols and optimizations are usually implemented as a standalone proof of concept or in an MPC framework and are tightly coupled with special-purpose circuit formats, such as Bristol Format. This makes it very hard and time-consuming to re-use algorithmic advances and implemented applications in a different context. Developing generic algorithmic optimizations is exceptionally hard because the available MPC tools and formats are not generic and do not provide the necessary infrastructure. In this paper, we present FUSE: A Framework for Unifying and Optimizing Secure Multi-Party Computation Implementations with Efficient Circuit Storage. FUSE provides a flexible intermediate representation (FUSE IR) that can be used across different platforms and in different programming languages, including C/C++, Java, Rust, and Python. We aim at making MPC tools more interoperable, removing the tight coupling between high-level compilers for MPC and specific MPC protocol engines, thus driving knowledge transfer. Our framework is inspired by the widely known LLVM compiler framework. FUSE is portable, extensible, and it provides implementation-agnostic optimizations. As frontends, we implement HyCC (CCS&#x27;18), the Bristol circuit format, and MOTION (TOPS&#x27;22), meaning that these can be automatically converted to FUSE IR. We implement several generic optimization passes, such as automatic subgraph replacement and vectorization, to showcase the utility and efficiency of our framework. Finally, we implement as backends MOTION and MP-SPDZ (CCS&#x27;20), so that FUSE IR can be run by these frameworks in an MPC protocol, as well as other useful backends for JSON output and the DOT language for graph visualization. With FUSE, it is possible to use any implemented frontend with any implemented backend and vice-versa. FUSE IR is not only efficient to work on and much more generic than any other format so far -- supporting, e.g., function calls, hybrid MPC protocols as well as user-defined building blocks, and annotations -- while maintaining backwards-compatibility, but also compact, with smaller storage size than even minimalistic formats such as Bristol already for a few hundred operations.

  匹配依据：MPC: secure multi party computation

  </details>

- **Decentralized Multi-Authority Attribute-Based Inner-Product FE: Large Universe and Unbounded**
  2023-04-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/565)
  Pratish Datta, Tapas Pal

  <details><summary>摘要 / Abstract</summary>

  This paper presents the first decentralized multi-authority attribute-based inner product functional encryption (MA-ABIPFE) schemes supporting vectors of a priori unbounded lengths. The notion of AB-IPFE, introduced by Abdalla et al. [ASIACRYPT 2020], combines the access control functionality of attribute-based encryption (ABE) with the possibility of evaluating linear functions on encrypted data. A decentralized MA-ABIPFE defined by Agrawal et al. [TCC 2021] essentially enhances the ABE component of AB-IPFE to the decentralized multi-authority setting where several authorities can independently issue user keys involving attributes under their control. In MA-ABIPFE for unbounded vectors (MA-ABUIPFE), encryptors can encrypt vectors of arbitrary length under access policies of their choice whereas authorities can issue secret keys to users involving attributes under their control and vectors of arbitrary lengths. Decryption works in the same way as for MA-ABIPFE provided the lengths of the vectors within the ciphertext and secret keys match. We present two MA-ABUIPFE schemes supporting access policies realizable by linear secret sharing schemes (LSSS), in the significantly faster prime-order bilinear groups under decisional assumptions based on the target groups which are known to be weaker compared to their counterparts based in the source groups. The proposed schemes demonstrate different trade-offs between versatility and underlying assumptions. The first scheme allows each authority to control a bounded number of attributes and is proven secure under the well-studied decisional bilinear Diffie-Hellman (DBDH) assumption. On the other hand, the second scheme allows authorities to control exponentially many attributes, that is, supports large attribute universe, and is proven secure under a non-interactive q-type variant of the DBDH assumption called L-DBDH, similar to what was used in prior large-universe multi-authority ABE (MA-ABE) construction. When compared with the only known MA-ABIPFE scheme due to Agrawal et al. [TCC 2021], our schemes offer significantly higher efficiency while offering greater flexibility and security under weaker assumptions at the same time. Moreover, unlike Agrawal et al., our schemes can support the appearance of the same attributes within an access policy arbitrarily many times. Since efficiency and practicality is the prime focus of this work, we prove the security of our constructions in the random oracle model against static adversaries similar to prior works on MA-ABE with similar motivations and assumptions. On the technical side, we extend the unbounded IPFE techniques of Dufour-Sans and Pointcheval [ACNS 2019] to the context of MA-ABUIPFE by introducing a novel hash-decomposition technique.

  匹配依据：MPC: secret sharing

  </details>

- **SAFEFL: MPC-friendly Framework for Private and Robust Federated Learning**
  2023-04-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/555)
  Till Gehlhar, Felix Marx, Thomas Schneider, Ajith Suresh, Tobias Wehrle, Hossein Yalame

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) has gained widespread popularity in a variety of industries due to its ability to locally train models on devices while preserving privacy. However, FL systems are susceptible to i) privacy inference attacks and ii) poisoning attacks, which can compromise the system by corrupt actors. Despite a significant amount of work being done to tackle these attacks individually, the combination of these two attacks has received limited attention in the research community. To address this gap, we introduce SAFEFL, a secure multiparty computation (MPC)-based framework designed to assess the efficacy of FL techniques in addressing both privacy inference and poisoning attacks. The heart of the SAFEFL framework is a communicator interface that enables PyTorch-based implementations to utilize the well established MP-SPDZ framework, which implements various MPC protocols. The goal of SAFEFL is to facilitate the development of more efficient FL systems that can effectively address privacy inference and poisoning attacks.

  匹配依据：MPC: secure multiparty computation

  </details>

- **InversOS: Efficient Control-Flow Protection for AArch64 Applications with Privilege Inversion**
  2023-04-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.08717)
  Zhuojia Shen, John Criswell

  <details><summary>摘要 / Abstract</summary>

  With the increasing popularity of AArch64 processors in general-purpose computing, securing software running on AArch64 systems against control-flow hijacking attacks has become a critical part toward secure computation. Shadow stacks keep shadow copies of function return addresses and, when protected from illegal modifications and coupled with forward-edge control-flow integrity, form an effective and proven defense against such attacks. However, AArch64 lacks native support for write-protected shadow stacks, while software alternatives either incur prohibitive performance overhead or provide weak security guarantees. We present InversOS, the first hardware-assisted write-protected shadow stacks for AArch64 user-space applications, utilizing commonly available features of AArch64 to achieve efficient intra-address space isolation (called Privilege Inversion) required to protect shadow stacks. Privilege Inversion adopts unconventional design choices that run protected applications in the kernel mode and mark operating system (OS) kernel memory as user-accessible; InversOS therefore uses a novel combination of OS kernel modifications, compiler transformations, and another AArch64 feature to ensure the safety of doing so and to support legacy applications. We show that InversOS is secure by design, effective against various control-flow hijacking attacks, and performant on selected benchmarks and applications (incurring overhead of 7.0% on LMBench, 7.1% on SPEC CPU 2017, and 3.0% on Nginx web server).

  匹配依据：MPC: secure computation

  </details>

- **Ideal Secret Sharing Schemes: Combinatorial Characterizations, Certain Access Structures, and Related Geometric Problems**
  2023-04-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.08741)
  Ryoh Fuji-Hara, Ying Miao

  <details><summary>摘要 / Abstract</summary>

  An ideal secret sharing scheme is a method of sharing a secret key in some key space among a finite set of participants in such a way that only the authorized subsets of participants can reconstruct the secret key from their shares which are of the same length as that of the secret key. The set of all authorized subsets of participants is the access structure of the secret sharing scheme. In this paper, we derive several properties and restate the combinatorial characterization of an ideal secret sharing scheme in Brickell-Stinson model in terms of orthogonality of its representative array. We propose two practical models, namely the parallel and hierarchical models, for access structures, and then, by the restated characterization, we discuss sufficient conditions on finite geometries for ideal secret sharing schemes to realize these access structure models. Several series of ideal secret sharing schemes realizing special parallel or hierarchical access structure model are constructed from finite projective planes.

  匹配依据：MPC: secret sharing

  </details>

- **Compartment-based and Hierarchical Threshold Delegated Verifiable Accountable Subgroup Multi-signatures**
  2023-04-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/548)
  Ahmet Ramazan Ağırtaş, Oğuz Yayla

  <details><summary>摘要 / Abstract</summary>

  In this paper, we study the compartment-based and hierarchical delegation of signing power of the verifiable accountable subgroup multi-signature (vASM). ASM is a multi-signature in which the participants are accountable for the resulting signature, and the number of participants is not fixed. After Micali et al.’s and Boneh et al.’s ASM schemes, the verifiable-ASM (vASM) scheme with a verifiable group setup and more efficient verification phase was proposed recently. The verifiable group setup in vASM verifies the participants at the group setup phase. In this work, we show that the vASM scheme can also be considered as a proxy signature in which an authorized user (original signer, designator) delegates her signing rights to a single (or a group of) unauthorized user(s) (proxy signer). Namely, we propose four new constructions with the properties and functionalities of an ideal proxy signature and a compartment-based/hierarchical structure. In the first construction, we apply the vASM scheme recursively; in the second one, we use Shamir’s secret sharing (SSS) scheme; in the third construction, we use SSS again but in a nested fashion. In the last one, we use the hierarchical threshold secret sharing (HTSS) scheme for delegation. Then, we show the affiliation of our constructions to proxy signatures and compare our constructions with each other in terms of efficiency and security. Finally we compare the vASM scheme with the existing pairing-based proxy signature schemes.

  匹配依据：MPC: secret sharing

  </details>

- **Secure Communication in Dynamic Incomplete Networks**
  2023-04-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/529)
  Ivan Damgård, Divya Ravi, Daniel Tschudi, Sophia Yakoubov

  <details><summary>摘要 / Abstract</summary>

  In this paper, we explore the feasibility of reliable and private communication in dynamic networks, where in each round the adversary can choose which direct peer-to-peer links are available in the network graph, under the sole condition that the graph is k-connected at each round (for some k). We show that reliable communication is possible in such a dynamic network if and only if k &gt; 2t. We also show that if k = cn &gt; 2t for a constant c, we can achieve reliable communication with polynomial round and communication complexity. For unconditionally private communication, we show that for a passive adversary, k &gt; t is sufficient (and clearly necessary). For an active adversary, we show that k &gt; 2t is sufficient for statistical security (and clearly necessary), while k &gt; 3t is sufficient for perfect security. We conjecture that, in contrast to the static case, k &gt; 2t is not enough for perfect security, and we give evidence that the conjecture is true. Once we have reliable and private communication between each pair of parties, we can emulate a complete network with secure channels, and we can use known protocols to do secure computation.

  匹配依据：MPC: secure computation

  </details>

- **SePEnTra: A secure and privacy-preserving energy trading mechanisms in transactive energy market**
  2023-04-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.06179)
  Rumpa Dasgupta, Amin Sakzad, Carsten Rudolph, Rafael Dowsley

  <details><summary>摘要 / Abstract</summary>

  In this paper, we design and present a novel model called SePEnTra to ensure the security and privacy of energy data while sharing with other entities during energy trading to determine optimal price signals. Furthermore, the market operator can use this data to detect malicious activities of users in the later stage without violating privacy (e.g., deviation of actual energy generation/consumption from forecast beyond a threshold). We use two cryptographic primitives, additive secret sharing and Pedersen commitment, in SePEnTra. The performance of our model is evaluated theoretically and numerically. We compare the performance of SePEnTra with the same Transactive energy market (TEM) framework without security mechanisms. The result shows that even though using advanced cryptographic primitives in a large market framework, SePEnTra has very low computational complexity and communication overhead. Moreover, it is storage efficient for all parties.

  匹配依据：MPC: secret sharing

  </details>

- **TREBUCHET: Fully Homomorphic Encryption Accelerator for Deep Computation**
  2023-04-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.05237) · [IACR ePrint](https://eprint.iacr.org/2023/521)
  David Bruce Cousins, Yuriy Polyakov, Ahmad Al Badawi, Matthew French, Andrew Schmidt, Ajey Jacob, Benedict Reynwar, Kellie Canida, Akhilesh Jaiswal, Clynn Mathew, Homer Gamil, Negar Neda, Deepraj Soni, Michail Maniatakos, Brandon Reagen, Naifeng Zhang, Franz Franchetti, Patrick Brinich, Jeremy Johnson, Patrick Broderick, Mike Franusich, Bo Zhang, Zeming Cheng, Massoud Pedram

  <details><summary>摘要 / Abstract</summary>

  Secure computation is of critical importance to not only the DoD, but across financial institutions, healthcare, and anywhere personally identifiable information (PII) is accessed. Traditional security techniques require data to be decrypted before performing any computation. When processed on untrusted systems the decrypted data is vulnerable to attacks to extract the sensitive information. To address these vulnerabilities Fully Homomorphic Encryption (FHE) keeps the data encrypted during computation and secures the results, even in these untrusted environments. However, FHE requires a significant amount of computation to perform equivalent unencrypted operations. To be useful, FHE must significantly close the computation gap (within 10x) to make encrypted processing practical. To accomplish this ambitious goal the TREBUCHET project is leading research and development in FHE processing hardware to accelerate deep computations on encrypted data, as part of the DARPA MTO Data Privacy for Virtual Environments (DPRIVE) program. We accelerate the major secure standardized FHE schemes (BGV, BFV, CKKS, FHEW, etc.) at &gt;=128-bit security while integrating with the open-source PALISADE and OpenFHE libraries currently used in the DoD and in industry. We utilize a novel tile-based chip design with highly parallel ALUs optimized for vectorized 128b modulo arithmetic. The TREBUCHET coprocessor design provides a highly modular, flexible, and extensible FHE accelerator for easy reconfiguration, deployment, integration and application on other hardware form factors, such as System-on-Chip or alternate chip areas.

  匹配依据：MPC: secure computation

  </details>

- **Encrypted Price-based Market Mechanism for Optimal Load Frequency Control**
  2023-04-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.05525)
  Jihoon Suh, Takashi Tanaka

  <details><summary>摘要 / Abstract</summary>

  The global trend of energy deregulation has led to the market mechanism replacing some functionality of load frequency control (LFC). Accordingly, information exchange among participating generators and the market operator plays a crucial role in optimizing social utility. However, privacy has been an equally pressing concern in such settings. This conflict between individuals&#x27; privacy and social utility has been a long-standing challenge in market mechanism literature as well as in Cyber-Physical Systems (CPSs). In this paper, we propose a novel encrypted market architecture that leverages a hybrid encryption method and two-party computation protocols, enabling the secure synthesis and implementation of an optimal price-based market mechanism. This work spotlights the importance of secure and efficient outsourcing of controller synthesis, which is a critical element within the proposed framework. A two-area LFC model is used to conduct a case study.

  匹配依据：MPC: two party computation

  </details>

- **Black-Box Reusable NISC with Random Oracles**
  2023-04-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/514)
  Yuval Ishai, Dakshita Khurana, Amit Sahai, Akshayaram Srinivasan

  <details><summary>摘要 / Abstract</summary>

  We revisit the problem of {\em reusable} non-interactive secure computation (NISC). A standard NISC protocol for a sender-receiver functionality $f$ enables the receiver to encrypt its input $x$ such that any sender, on input $y$, can send back a message revealing only $f(x,y)$. Security should hold even when either party can be malicious. A {\em reusable} NISC protocol has the additional feature that the receiver&#x27;s message can be safely reused for computing multiple outputs $f(x,y_i)$. Here security should hold even when a malicious sender can learn partial information about the honest receiver&#x27;s outputs in each session. We present the first reusable NISC protocol for general functions $f$ that only makes a {\em black-box} use of any two-message oblivious transfer protocol, along with a random oracle. All previous reusable NISC protocols either made a non-black-box use of cryptographic primitives (Cachin et al., ICALP 2002) or alternatively required a stronger arithmetic variant of oblivious transfer and were restricted to $f$ in $\mathsf{NC}^1$ or similar classes (Chase et al., Crypto 2019). Our result is obtained via a general compiler from standard NISC to reusable NISC that makes use of special type of honest-majority protocols for secure multiparty computation. Finally, we extend the above main result to reusable {\em two-sided} NISC, in which two parties can encrypt their inputs in the first round and then reveal different functions of their inputs in multiple sessions. This extension either requires an additional (black-box) use of additively homomorphic commitment or alternatively requires the parties to maintain a state between sessions.

  匹配依据：MPC: oblivious transfer, secure computation, secure multiparty computation

  </details>

- **$\\text{MP}\\ell\\circ \\mathrm{C}$: Privacy-Preserving IP Verification Using Logic Locking and Secure Multiparty Computation**
  2023-04-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/511)
  Dimitris Mouris, Charles Gouert, Nektarios Georgios Tsoutsos

  <details><summary>摘要 / Abstract</summary>

  The global supply chain involves multiple independent entities, and potential adversaries can exploit different attack vectors to steal proprietary designs and information. As a result, intellectual property (IP) owners and consumers have reasons to keep their designs private. Without a trusted third party, this mutual mistrust can lead to a deadlock where IP owners are unwilling to disclose their IP core before a financial agreement is reached, while consumers need assurance that the proprietary design will meet their integration needs without compromising the confidentiality of their test vectors. To address this challenge, we introduce an efficient framework called MPloC that resolves this deadlock by allowing owners and consumers to jointly evaluate the target design with consumer-supplied test vectors while preserving the privacy of both the IP core and the inputs. MPloC is the first work that combines secure multiparty computation (MPC) and logic-locking techniques to accomplish these goals. Our approach supports both semi-honest and malicious security models to allow users to balance stronger security guarantees with performance. We compare our approach to existing state-of-the-art works that utilize homomorphic encryption across several benchmarks and report runtime improvements of more than two orders of magnitude.

  匹配依据：MPC: secure multiparty computation

  </details>
