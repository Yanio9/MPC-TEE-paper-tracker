# 2026 · MPC · 仅预印本来源 · 第 3/6 页

[总目录](../PAPERS.md) · [上一页](2026-mpc-preprint-02.md) · [下一页](2026-mpc-preprint-04.md)

- **SoK: Cryptographic Key Recovery for Cryptoasset Custody and Financial Technologies**
  2026-08-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.07104)
  Francisco Javier Becerra Sanchez, Antonio Ken Iannillo, Radu State

  <details><summary>摘要 / Abstract</summary>

  Cryptoasset systems often bind cryptographic key control to financial control: losing a wallet seed, custody share, hardware device, or smart-account credential can remove spend authority, while compromised recovery can enable theft. Existing work treats recovery through separate vocabularies--key backup, secret sharing, account recovery, credential re-issuance, social recovery, and asset migration--making mechanisms and tradeoffs difficult to compare. This paper presents a Systematization of Knowledge (SoK) on cryptographic key recovery for cryptoasset custody and financial technologies. Starting from a 118-paper systematic-review discovery corpus, we derive a 77-paper synthesis corpus and code each retained system in a master matrix covering recovered objects, recovery semantics, mechanisms, enrollment and storage, authorization, trust placement, failure events, post-recovery state, validation evidence, deployment status, privacy, usability, and limitations. The matrix supports an axis-first taxonomy that separates secret-restoring, hybrid, control-restoring, forensic/extractive, and framework-oriented recovery. Our central observation is that recovery is not a single operation: systems may reconstruct an original secret, regenerate a seed, restore a share, reissue a credential, migrate signing authority, restore account control, move assets, or extract forensic artifacts. We derive a generalized construction model, check it against production-facing designs, and identify six findings: recovery semantics are heterogeneous; recovery shifts trust; liveness improvements create abuse paths; post-recovery lifecycle management is uneven; protocol evidence outpaces user evidence; and recovery metadata remains underprotected. These gaps motivate a research agenda for recovery-aware financial technologies.

  匹配依据：MPC: secret sharing

  </details>

- **Preprocessed Private Function Evaluation: Achieving Sublinear Online Complexity for Lookup Tables**
  2026-08-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1631)
  Tanping Zhou, Xiaoyi Wang, Yi Qu, Wenchao Liu, Long Chen, Zhenfeng Zhang

  <details><summary>摘要 / Abstract</summary>

  Private Function Evaluation (PFE) facilitates the secure computation of private functions on private inputs in an oblivious manner, ensuring that both the function and the inputs remain confidential throughout the entire computational process. PFE has garnered significant attention due to its critical applications in various domains, such as privacy-preserving healthcare systems and privacy-preserving credit checks, where safeguarding the confidentiality of the function itself is of paramount importance. However, despite its broad applicability, existing PFE schemes often exhibit inefficiencies, even in relatively straightforward scenarios such as the evaluation of lookup tables. To mitigate these limitations, we propose a novel variant of PFE, termed Preprocessed Private Function Evaluation (PPFE), which leverages preprocessing techniques to significantly enhance the efficiency of online computations. Within this framework, we introduce a specialized construction tailored specifically for lookup table operations, achieving sublinear complexity during the online computation phase. The efficacy of the proposed approach is demonstrated through experimental evaluations. For a lookup table of size $2^{24}$, the online computation time required to process a single query is about 3 milliseconds, representing a performance improvement of more than an order of magnitude compared to existing results. Furthermore, the proposed scheme exhibits strong scalability, effectively handling thousands of adaptive queries within the same framework.

  匹配依据：MPC: secure computation

  </details>

- **The Locality Gap: A Thermodynamic Law for Objective Facts**
  2026-08-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.05753)
  Maxim V. Churilov

  <details><summary>摘要 / Abstract</summary>

  Objective facts in quantum Darwinism are values recorded redundantly in many independently accessible fragments of the environment. Redundancy does not create additional logical information, so its thermodynamic meaning has remained unclear. We show that it creates an exact work asymmetry between controllers with different access architectures. For a record cloud $F$ and a partition $\mathcal{P}$ into blocks that cannot be jointly controlled, the reversible isothermal erasure penalty relative to a global controller is $k_{\mathrm{B}}T$ times the partition total correlation. If the source event $X$ is supplied as catalytic classical side information, subtracting the corresponding penalty gives the source-loss law $\mathcal{F}_{\mathcal{P}}^{T}=k_{\mathrm{B}}T\left[\sum_{B\in\mathcal{P}}I(X{:}F_B)-I(X{:}F)\right]$. We call this the thermodynamic factuality charge. It ranges from $-k_{\mathrm{B}}T H(X)$ for perfect secret sharing to $(|\mathcal{P}|-1)k_{\mathrm{B}}T H(X)$ for perfect broadcast objectivity. Its normalized form defines a thermodynamic record number between $0$ and $|\mathcal{P}|$. We derive Landauer--Darwin bounds, endpoint-rigidity certificates, exact growth and partition-refinement laws, spectrum-broadcast saturation, and closed formulas for noisy classical and quantum collision models. The theory does not modify quantum mechanics or posit objective collapse; it identifies the thermodynamic resource generated by redundant records under restricted control.

  匹配依据：MPC: secret sharing

  </details>

- **Adaptive-Input-Secure Updatable Private Set Union**
  2026-08-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1626)
  Seongbong Choi, Jiseung Kim, Hyung Tae Lee

  <details><summary>摘要 / Abstract</summary>

  In multi-epoch deployments, private set union~(PSU) operates in an adaptive-input loop: after observing the union at epoch $t$, the receiver may choose its next input for epoch $t+1$. Liu et al.~(EUROCRYPT 2026) formalized this multi-epoch adaptive-input setting for updatable private set intersection and provided an instantiation, but their framework does not extend to PSU. Meanwhile, existing PSU protocols are analyzed only in the single-shot setting. We present the first semi-honest, adaptive-input-secure updatable PSU protocol supporting two-sided add/delete updates in the multi-epoch adaptive-input setting of Liu et al. Our construction is built around a new primitive, the updatable oblivious key-value store (uOKVS). Its defining rule, distributional erasure, requires each refresh to be distributed identically to a fresh static encoding of the current key set, rather than merely indistinguishably. We realize uOKVS by combining the Band-OKVS of Bienstock et al. with a PRF under a persistent key. The resulting refresh reuses a cached factorization, so its per-epoch encoding cost scales linearly rather than quadratically in the band width $w$. Building on this layer, we obtain a multi-epoch PSU protocol whose leakage is limited to set and update cardinalities, even against adaptive-input adversaries. We implement the protocol and benchmark it in a single-threaded setting. At $n = 2^{20}$ with per-epoch updates $\Delta = 55$ over $10$ epochs, the online per-epoch wall-clock time is $1.41$ s on LAN, yielding a $30.9\times$--$98.9\times$ speedup over prior static PSU protocols re-executed from scratch at each epoch.

  匹配依据：MPC: private set intersection, private set union

  </details>

- **AES-Based Grinding for MPC-in-the-Head Signatures**
  2026-08-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1625)
  Matthieu Rivain

  <details><summary>摘要 / Abstract</summary>

  Grinding is a technique which introduces a proof of work into the Fiat-Shamir transform: by constraining the challenge to satisfy a $w$-bit condition, forging a proof requires about $2^w/\varepsilon$ evaluations of the hash function instead of $1/\varepsilon$, where $\varepsilon$ is the soundness error of the underlying protocol. This allows one to select reduced parameters, yielding shorter proofs and signatures. Grinding is used in FAEST, MQOM and SDitH, the three MPC-in-the-Head schemes selected for the third round of the NIST additional post-quantum signature standardization process, where it is instantiated with Keccak. In this short paper, we investigate grinding schemes in which the proof of work is expressed in terms of block cipher computations, specifically AES, which is significantly faster than Keccak on modern CPUs, is already a building block of these schemes, and underlies the very definition of the NIST security categories. We formalize the notion of grinding scheme together with a protocol-agnostic security notion, we propose a construction performing two cipher calls per iteration, and we prove, in the ideal cipher and random oracle models, that an adversary making $Q_E$ cipher queries breaks it with probability at most $\frac{4}{3} \cdot \varepsilon\, Q_E / 2^w$, up to negligible terms. We further generalize the scheme to use more cipher calls per iteration, which makes the constant $\frac43$ tend to $1$.

  匹配依据：MPC: mpc (context)

  </details>

- **Minimal Binary Linear Codes of Dimension n+4 from Partial Spreads and Their Dual Access Structures**
  2026-08-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.04889)
  Apurba Sarkar, Kalyan Hansda, Makhan Maji

  <details><summary>摘要 / Abstract</summary>

  Minimal linear codes have significant applications in secret sharing schemes, secure multi-party computation, and cryptography. In this paper, we propose a generic construction of a new family of minimal binary linear codes with dimension n+4 from a special class of Boolean functions. By leveraging the geometric properties of partial spreads in finite fields, we determine the explicit weight distribution and weight enumerator of the constructed codes. Furthermore, we derive a necessary and sufficient condition for these codes to be minimal, and establish that the proposed family yields minimal codes that structurally violate the well-known Ashikhmin-Barg condition, making them highly desirable for advanced communication systems.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **KORD: Breaking the Key-Generation Bottleneck in Dealerless Function Secret Sharing via Protocol–Hardware Co-Design**
  2026-08-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1615)
  Yijing Peng, Lin Liu, Yujie Xue, Shaojing Fu, Shaoqing Li, Yaohua Wang, Rongmao Chen, Yang Guo

  <details><summary>摘要 / Abstract</summary>

  Function secret sharing (FSS) has become a core primitive in privacy‑preserving computation. However, each FSS invocation requires a fresh pair of function keys, typically produced by a trusted dealer—a dependency that expands the system&#x27;s trust boundary and hinders practical deployment. Existing dealerless protocols eliminate this dependency, but incur substantial communication and a number of interaction rounds that grows linearly with the input bit‑width, making key generation a major bottleneck. This paper presents KORD, a protocol–hardware co‑design that dramatically reduces the cost of dealerless FSS key generation. At its core is a pair of chips that establish a common root of trust through mutual attestation and, within it, reconstruct FSS keys—eliminating the need for a dealer. This root of trust further forms a security boundary within which KORD restructures the generation protocol, collapsing the interaction of prior dealerless protocols into a single round, independent of GGM depth. A cross‑key scheduling scheme then interleaves independent GGM‑tree traversals, sustaining high computational throughput. KORD reduces key‑generation communication per operation by $7{,}633$–$70{,}274\times$ over the state‑of‑the‑art distributed FSS protocol. On a ZCU102 FPGA, cross‑key interleaving lifts AES lane utilization from $8.3\%$ to a board‑measured $99.0\%$, for $11.60$ million $32$-bit DPF keys per second at $187.5\,\text{MHz}$ on a $21.5\,\text{K}$ LUT engine ($12.38\,\text{M}$ at the separately validated $200\,\text{MHz}$ operating point). On private ResNet‑18 inference, key generation&#x27;s share of end‑to‑end time falls to $10.1\%$, from $82.6\%$ under a trusted dealer and over $96\%$ under the dealerless baseline.

  匹配依据：MPC: secret sharing

  </details>

- **DYNAFIX: Dynamic Fixed‑Point Encoding for Arbitrary‑Range MPC**
  2026-08-05 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1612)
  Yuntian Chen, Tianpei Lu, Zhanyong Tang, Bingsheng Zhang, Wenjing Yang, Zhuzhu Wang, Kui Ren

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving computation over real numbers typically employs either floating-point or fixed-point arithmetic. While fixed-point methods are highly efficient, they struggle to handle wide dynamic ranges. Conversely, floating-point methods support a much larger numerical scope but incur overheads more than a hundred times higher than their fixed-point counterparts. In this paper, we propose DYNAFIX, a dynamic fixed-point computation scheme that strikes a balance between floating-point and fixed-point arithmetic. Compared to traditional fixed-point approaches, our scheme supports an arbitrary numerical range; compared to floating-point computation, it maintains performance comparable to fixed-point execution. Experimental results demonstrate that our method achieves a $24.1\times$ speedup over the state-of-the-art when evaluating high-precision functions, such as the exponential function.

  匹配依据：MPC: mpc (context)

  </details>

- **Paras: Actively Secure Two-Server Private Histograms**
  2026-08-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1600)
  Dimitris Mouris, Lucas Piske, Pratik Sarkar, Ni Trieu, Mehmet Ugurbil

  <details><summary>摘要 / Abstract</summary>

  Private histogram computation is a fundamental building block for many data analytics tasks, enabling frequency analysis without revealing individual inputs. Existing protocols achieving robustness against malicious clients and servers typically require three servers with limited adversarial tolerance, restricting practicality. In this work, we present Paras, the first two-server protocol for private histogram computation that achieves robustness against collusion between a malicious server and arbitrarily many malicious clients. Paras builds upon distributed point function-based approaches and introduces novel consistency checks leveraging vector oblivious linear evaluation (VOLE) to enforce both input correctness and output integrity. To realize these checks, we design two new cryptographic primitives: (1) aBV, an authenticated bit verification protocol that ensures VOLE committed shares correspond to valid bits, and (2) adIPA, an authenticated double inner product argument that enables secure consistency checks across two different VOLE sessions. These primitives may be of independent interest for other secure computation tasks. We show that Paras is highly efficient and scalable: clients incur minimal cost independent of domain size, while servers achieve low per-client runtime, communication, and storage even at scale. For example, with 8192 clients over a domain of 128 inputs, each server requires only 14 ms runtime and 24 KB communication per client.

  匹配依据：MPC: secure computation

  </details>

- **Updatable Oblivious Key Value Stores with Access Control and Application to Multi Key Searchable Encryption**
  2026-08-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1590)
  Benjamin Fuller, Ariel Hamlin, Arinjita Paul, Maryam Rezapour, Ronak Sahu, Amey Shukla, Mason Stuart

  <details><summary>摘要 / Abstract</summary>

  Oblivious Key-Value Stores (OKVS) (Garimella et al., CRYPTO 2021), once encoded, provide indistinguishability over keys and random values. This is an important property in many secure computation applications, such as private set intersection and multi-key searchable encryption. We introduce an Updatable Oblivious Key-Value Store with access control (UOKVS), a dynamic extension of OKVS that supports insertions over time. We provide meaningful security in the presence of updates by equipping UOKVS with fine-grained access control. As a building block in UOKVS, we provide the first analysis of oblivious insertions for Cuckoo hashing, which may be of independent interest. We show the application of UOKVS to multi-key searchable encryption where a data owner wishes to share parts of a multimap with multiple clients. We construct an oblivious multimap with insertions from UOKVS and private information retrieval (PIR). Unlike prior multi-key searchable encryption schemes, our construction supports sharing without replicating data across authorized users, substantially reducing storage costs in addition to stronger privacy guarantees. We implement our multi-key searchable encryption construction on a dataset containing up to 24 million entries using the Enron email dataset. For keywords matching 100 documents on a WAN, query processing completes in $0.6$ seconds using FrodoPIR as the underlying PIR protocol. By comparison, the scheme of Wang and Papadopoulos (Cloud Computing 2023) achieves a query time of $0.6$ seconds and also incurs data replication and leaks access patterns. Our construction reduces leakage, maintains performance, and only requires a $3.1$x storage overhead.

  匹配依据：MPC: private set intersection, secure computation

  </details>

- **Privacy-Preserving Inclusion Lists**
  2026-08-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1582)
  Zhengwei Tong, Saba Eskandarian, Kartik Nayak

  <details><summary>摘要 / Abstract</summary>

  Blockchains aim to provide open access and censorship resistance, but centralization of block production in blockchains like Ethereum undermines these goals. Inclusion List (IL) protocols mitigate this by requiring block proposers to include transactions selected by an IL committee to enforce the inclusion of transactions that appear to have been censored. However, protecting the confidentiality of individual committee members’ contributions is essential to prevent retaliation and ensure robust censorship resistance. We propose a lightweight, privacy-preserving inclusion list protocol that allows committees to collectively construct transaction lists while hiding individual contributions and ensuring plausible deniability. Our approach builds on multiparty computation (MPC) techniques to achieve strong privacy without relying on heavyweight cryptography or anonymous broadcast channels. We implement two variants of our protocol design: an optimistic version providing malicious security with abort (latency $\sim 4.0$s) for speed, and a robust variant (latency $\sim 124.7$s) for guaranteed output delivery in the presence of a Byzantine threshold of $t &lt; n/3$ malicious parties.

  匹配依据：MPC: multiparty computation

  </details>

- **Pivot: Proactive and Verifiable Threshold Oblivious Pseudorandom Functions From Isogeny Group Actions**
  2026-08-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.01390)
  Abhinav Sharma, Vikas Srivastava

  <details><summary>摘要 / Abstract</summary>

  Oblivious pseudorandom functions (OPRFs) allow a client to evaluate a keyed pseudorandom function on a private input without revealing that input to the server. In a threshold OPRF, the secret key is distributed among (n) servers so that any qualified set of at least (t) servers can complete an evaluation, while fewer than (t) shares reveal no information about the key. Existing isogeny-based threshold OPRFs, however, are primarily designed for static corruption models. If the same shares remain valid throughout the lifetime of the service, a mobile adversary can compromise different servers over time, accumulate (t) shares from the same sharing state, and eventually recover the master key. We introduce PIVOT (Proactive Isogeny-based Verifiable Oblivious Threshold PRF), a dealerless threshold VOPRF framework based on effective isogeny group actions. PIVOT periodically refreshes the server shares without changing the master key, public key, or previously generated OPRF outputs. The construction combines Shamir secret sharing, additively homomorphic coefficient commitments, sequential Lagrange-weighted group actions, and joint zero-knowledge relations that link certified shares to their corresponding isogeny actions. It also supports coordinated epoch transitions, publicly verifiable blame, secure erasure, and committee resharing under a possibly different threshold. We formalize the functionality of a long-lived proactive threshold VOPRF, prove the correctness of distributed key generation, threshold evaluation, proactive refresh, and committee resharing, and provide a simulation-based security analysis under the vectorization and one-more hidden-group- action assumptions. As an application, we describe a distributed private lookup service whose encrypted database remains valid across repeated share renewals and committee migrations.

  匹配依据：MPC: secret sharing

  </details>

- **The Non-Intersecting Codewords Problem and its Application to MPC-in-the-Head Signatures**
  2026-07-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1573)
  Pierre Briaud, Philippe Gaborit, Romaric Neveu, Gilles Zémor

  <details><summary>摘要 / Abstract</summary>

  Since McEliece introduced the first code-based encryption scheme in 1978, most code-based cryptographic constructions have relied on hard problems related to decoding random linear codes (or variants thereof) or code equivalence. More recently, the use of the MPC-in-the-Head paradigm has enabled the construction of a new class of very competitive digital signature schemes relying on such assumptions, including the NIST submissions Mirath, PERK, RYDE, and SDitH, as well as a recent proposal based on the so-called Subfield Bilinear Collision problem by Huth and Joux (Crypto 2024). In this work, we enrich the portfolio of code-based MPC-in-the-Head signature schemes by introducing a new hard problem to cryptography, referred to as the Non-Intersecting Codewords (NIC) problem. In this problem, one has to find two codewords of a given linear code such that their supports in the Hamming metric do not intersect. After discussing how to generate hard instances and studying several attacks on it, we show that the NIC problem can be used to construct a competitive MPC-in-the-Head signature scheme. Using generic constructions, we obtain smaller signature sizes than SDitH and PERK, attaining a signature size of 2~934~Bytes for NIST security level I.

  匹配依据：MPC: mpc (context)

  </details>

- **Tensor Encodings for SIMD HSS**
  2026-07-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1569)
  Jaehyung Kim

  <details><summary>摘要 / Abstract</summary>

  We study SIMD packing for the lattice-based homomorphic secret sharing scheme of Boyle-Kohl-Scholl (BKS) over dimension-$N$ cyclotomic rings. A trace construction with alternating tensor encodings matches the $\Theta(\sqrt N)$ packing of SIMD-HSS by Kim et al. (ePrint 2026/485). Its addition-closed mode uses $O(\log N)$ authenticated automorphisms, two BKS multiplications, and two constant multiplications; an alternating fast path roughly halves these costs. A second construction uses a three-term-progression-free slot set $A$: homomorphic traces isolate the product coefficients at $2a$ for $a\in A$, and a halving automorphism returns them to $a$. For fixed $k$ and conductor primes, with balanced prime-power factors, this packs $N^{1-o(1)}$ slots with one BKS multiplication, $O(kN^{1/(2k)})$ authenticated automorphisms, and $O(kN^{1/k})$ constant multiplications. Both constructions support standard (non-entropic) secrets. Two-party executions at 162 and 495 slots confirm the algebra and exact call counts.

  匹配依据：MPC: secret sharing

  </details>

- **Antichain Winternitz: Guaranteed Garbled-Circuit Label Revelation on Bitcoin with Permissionless Recovery**
  2026-07-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1568)
  Mukesh Tiwari, Aaron Feickert

  <details><summary>摘要 / Abstract</summary>

  Trust-minimized bridges on Bitcoin move SNARK verification off chain by evaluating the verifier as a garbled circuit. The bridge&#x27;s on-chain spending condition obliges the Garbler to reveal the labels for one input without enabling the Evaluator to derive labels for any other input. Existing designs commit to each input bit with a Lamport signature which is costlier on chain, or with adaptors where there is no guarantee that the spend actually reveals the labels. We present Antichain Winternitz, a parametrized hash-chain construction whose admissible codewords form a constant-sum antichain. The on-chain locking script accepts an opening witness only if it encodes a valid codeword consistent with the committed chain terminals. Every accepted opening witness yields a valid codeword while the public off-chain table, verified during setup, maps every admissible codeword to its garbled-circuit labels, so any observer can recover them. Depending on the parameter set, we can obtain up to a 52.9% saving over Lamport signatures with only added off-chain storage of 43.8 kB per message bit.

  匹配依据：MPC: garbled circuit

  </details>

- **Secure Aggregation for Privacy-Preserving Federated Learning on Clinical EEG Data**
  2026-07-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.28191)
  Pouya Rajabi, Mohsen Toorani

  <details><summary>摘要 / Abstract</summary>

  Federated learning enables multiple institutions to collaboratively train a shared model without exchanging their raw data. However, individual model updates are data-dependent and may reveal information about clients&#x27; local training data. This paper presents a privacy-preserving federated learning framework for clinical EEG data that uses masking-based secure aggregation as its core protection mechanism. The framework combines graph-based communication, threshold secret sharing, dropout recovery, local update clipping, an optional Bloom filter-based privacy-preserving record-linkage initialization module, and auxiliary-notary-based verifiability. It supports semi-honest and malicious aggregation settings and is implemented using the Flower federated learning framework. The secure aggregation variants are evaluated in a simulated cross-silo healthcare setting using TUH EEG-derived data under different client configurations. Under the stated assumptions, the secure variants hide individual updates from the aggregation server. The results show that these variants remain compatible with federated model training, although malicious-setting safeguards and lightweight consistency-checking mechanisms introduce additional computation, communication, and round-duration overhead. Among the proposed secure configurations, the base semi-honest variant incurs the lowest overhead; the malicious-server variants add protocol-consistency and authenticity safeguards, and the auxiliary-notary variants add lightweight aggregate-consistency checking.

  匹配依据：MPC: secret sharing

  </details>

- **Revisiting Shamir Secret Sharing for Threshold Fully Homomorphic Encryption**
  2026-07-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1559)
  Jiseung Kim, Seunghu Kim, Hyung Tae Lee

  <details><summary>摘要 / Abstract</summary>

  Recent advances in lattice-based threshold cryptography, including threshold fully homomorphic encryption (ThFHE) and threshold public key encryption (ThPKE), commonly employ Shamir secret sharing over rings. While conceptually simple, these schemes suffer from rapidly growing denominator-clearing factors required for secret reconstruction as the number of parties $N$ increases, which in turn necessitates larger ciphertext moduli and complex reconstruction procedures. In this work, we revisit the notion of subtractive sets underlying ring-based Shamir secret sharing and present a refined framework for constructing integer-reconstructible sharing over cyclotomic rings. To that end, we introduce a new geometric analysis of Lagrange coefficients and show that the resulting reconstruction factors can be made significantly smaller under specific settings. In particular, our framework enables smaller ciphertext sizes in $(t,N)$-threshold settings, and yields improved correctness and efficiency when applied to any ring-based threshold construction employing Shamir secret sharing over cyclotomic rings. Specifically, in lattice-based one-round $(t, N)$-ThFHE schemes, our approach reduces the bit-size of ciphertext moduli from $O(N)$ to $O(t\log (N/t^2))$ while ensuring efficient denominator handling. For lattice-based ThPKE, our method yields a new bound on reconstruction factors that improves upon the recent state-of-the-art result of Pilvi. Moreover, we implement ThFHE schemes over cyclotomic rings based on our framework and demonstrate their practical efficiency. Our experimental results show that each algorithm completes within $0.2$ seconds for $N=64$ and remains scalable for larger configurations with $N\geq 256$.

  匹配依据：MPC: secret sharing

  </details>

- **Power Analysis and Countermeasures on the MiMC Block Cipher**
  2026-07-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1562)
  Elena Andreeva, Stefan Mangard, Rishub Nagpal, Arnab Roy, Stefano Trevisani

  <details><summary>摘要 / Abstract</summary>

  Modern zero-knowledge (ZK), fully homomorphic encryption (FHE) and Multi-party Computation (MPC) protocols have motivated research interest in Arithmetization-Oriented (AO) cryptographic primitives. The use of these protocols on embedded platforms requires consideration for protection against side-channel analysis (SCA), including timing and power attacks. Compared to traditional bit-oriented block ciphers, the design of side-channel countermeasures for AO-based ciphers poses unique challenges due to their different mathematical properties and computation requirements. In this work, we perform side-channel analysis of MiMC, a well-known AO block cipher. We first consider its constant-time implementation over the BN254 prime field for both x86 and ARM-v7 targets. Next, we demonstrate both profiled (SASCA) and unprofiled (linear regression) power analysis of our implementation on the ARM Cortex-M4 microcontroller, showing that a DPA adversary can reduce the key-guessing space to just \(2^{30}\) candidates using only \(\approx\) 32000 power measurements, and the profiling adversary can perform full key recovery in as few as 100 measurements. Hence, we consider and compare two side-channel countermeasures: a classical ISW masking approach, and the redundant number representation (RNR) adapted for large prime fields. For the RNR countermeasure, we show that \(\approx 64\) bits of redundancy are sufficient to reduce the information leakage enough to make DPA attacks impractical. Our claim is supported both by a standard fixed-vs-random leakage assessment with 10 million collected traces and by quantitative analysis via SASCA attacks. Finally, we compare the performance of the RNR countermeasure with first-order masking. While masking incurs in a \(\approx 8.3\times \) overhead on a Cortex-M4 MCU and in an \(\approx 81\times \) overhead on an x86-64 CPU, the RNR approach only introduces a \(\approx 50\%\) overhead on both targets.

  匹配依据：MPC: multi party computation

  </details>

- **Partial Derandomization for Leakage-Resilient Shamir's Secret Sharing over Composite Order Fields**
  2026-07-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.28757) · [IACR ePrint](https://eprint.iacr.org/2026/1475)
  S. Venkitesh

  <details><summary>摘要 / Abstract</summary>

  We make progress on the question of constructing explicit evaluation places for leakage-resilient Shamir&#x27;s secret sharing, over composite order fields. Previously, Maji et al. (EUROCRYPT 2024) showed that random evaluation places yield Shamir&#x27;s secret sharing over the composite order field $\mathbb{F}_{p^d}$ that is statistically secure against physical-bit leakage. Later, Nguyen (EUROCRYPT 2025) established a dichotomy that linear code-based secret-sharing scheme over the field $\mathbb{F}_{p^d}$ is either statistically secure or completely insecure against such leakage. Building upon Nguyen&#x27;s dichotomy, we present a partial derandomization of evaluation places, improving upon the Maji et al. result for a restricted regime of parameters. We replace the random choice of $n$ independent evaluation places by the iterates $x_j = Φ^j(x_0)$ of a simple fixed rational function $Φ$, where the initial point $x_0 \in \mathbb{F}_{p^d}^*$ is randomly chosen. The randomness in the evaluation places thus drops from $nd \log p$ bits to $d\log p$ bits. Our construction is valid for the regime $n = O(d/\log_p d)$, and any reconstruction threshold $k \ge 2$; in fact, the scheme attains perfect security (statistical distance exactly zero) against single-block leakage. Our technique is a partial fraction nondegeneracy argument that exploits the distinct poles of the rational iterates.

  匹配依据：MPC: secret sharing

  </details>

- **Distributed Point Functions and Function Secret Sharing**
  2026-07-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.27696)
  Elette Boyle, Niv Gilboa, Yuval Ishai, Peter Scholl

  <details><summary>摘要 / Abstract</summary>

  A distributed point function (DPF) is a cryptographic primitive that enables compressed additive sharing of a secret weight-1 vector (equivalently, a point function) across two or more parties. The appealing lightweight structure of DPF constructions has enabled a wide range of applications. These include private information retrieval, anonymous messaging, secure computation with preprocessing, and pseudorandom correlation generators for expanding small correlated seeds into large pseudorandom instances of cryptographic correlations. In this article, we survey definitions, constructions, and applications of DPFs. We also discuss the extension of DPF to function secret sharing (FSS), which generalizes point functions to support richer function classes. Efficient FSS schemes yield a similar generalization for most of the applications of DPFs.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Silent Distributed Cryptography for DNFs and Threshold Policies from Lattices**
  2026-07-29 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1547)
  Abtin Afshar, Rishab Goyal, Saikumar Yadugiri

  <details><summary>摘要 / Abstract</summary>

  We study two central problems in threshold cryptography from lattices: (1) threshold encryption with silent setup for general thresholds $t \geq 2$, where no post-quantum constructions were previously known, and (2) threshold fully homomorphic encryption (TFHE) with sublinear parameters, an open problem since the work of [Boneh et al.; CRYPTO&#x27;18]. We introduce $\textit{$(\alpha,\beta)$-Scaled Linear Secret Sharing Schemes}$ (LSSS), a relaxation of standard LSSS in which each authorized set $S$ reconstructs a scaled version of the secret, $\gamma_S \cdot k$, where both the reconstruction coefficients and the set-dependent scaling factor $\gamma_S$ are bounded over the integers. Unlike prior approaches based on bit decomposition, this preserves the uniform distribution of unauthorized shares. Building on this, we obtain: 1. $\textbf{Silent Threshold and Distributed monotone-policy encryption.}$ We provide the first post-quantum construction supporting: (i) threshold policies with ciphertexts growing as $\tau^{16} \cdot \mathsf{poly}(\lambda, \log N)$, where $\tau = \min(t^2,N{-}t)$, and (ii) DNF formulas with fully compact parameters. Our constructions are proven secure under the decomposed LWE assumption in the random oracle model. If we additionally rely on a common reference string, then the ciphertext size for our threshold policy scheme can be reduced to $\tau^4 \cdot \mathsf{poly}(\lambda, \log N)$ under the Succinct LWE assumption. 2. $\textbf{Decentralized TFHE with silent setup.}$ We provide the first $\textit{decentralized}$ TFHE, for threshold policies and DNFs, from the decomposed LWE assumption. Our construction supports homomorphic evaluation of arbitrary circuits, one-round distributed decryption, and silent setup. This was left as an open problem by [Boneh et al.; CRYPTO&#x27;18] and, prior to this work, we did not have any non-trivial construction for decentralized TFHE from any assumption. 3. $\textbf{Sublinear centralized TFHE from LWE.}$ We also extend our techniques to $\textit{centralized}$ TFHE. We provide a TFHE scheme under the standard LWE assumption, where all parameters are simultaneously sublinear in $N$ for any threshold $t$ as long as $\min(t^2,N{-}t)=o(N^{1/6})$. This breaks the $\omega(N)$ barrier that has persisted in the TFHE literature since 2018.

  匹配依据：MPC: secret sharing

  </details>

- **SafeStats: Efficient 2PC Protocols for Data Statistic-Related Functions**
  2026-07-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.25430)
  Tanren Liu, Xianjia Meng, Yang Liu, Xin Kang, Chenhui You, Yong Zeng, Zhuo Ma

  <details><summary>摘要 / Abstract</summary>

  Statistical analysis on sensitive datasets like medical records and financial transactions is essential for decision-making, but raises significant privacy concerns. While existing secure Two-Party Computation (2PC) makes extensive efforts in designing the common secure primitives (e.g., addition and multiplication) or machine learning-related functions, few pay attention to the statistical functions. In this paper, we propose SafeStats, a secure toolkit tailored for 2PC secure statistical analysis. Specifically, to develop SafeStats, we first refer to Microsoft Excel&#x27;s statistical library and summarize that most statistical operations can be achieved with three core functions:1) frequency counting, 2) sorting, and 3) non-linear math functions. Then, for each core statistical function, SafeStats presents an efficient 2PC implementation. For secure frequency counting, SafeStats adopts a secure shift-based strategy to avoid invoking expensive 2PC equality test protocols. For secure sort, SafeStats involves a secure segment-indicator protocol to achieve secure counting-based sort, which enables fast element sorting over specific statistical scenarios without the need for secure comparison. For non-linear math functions, we enhance the current reduce-then-approximate paradigm by introducing a bisection-based range reduction protocol. Finally, we implement SafeStats and test it on 14 common statistical analysis cases. As an example, for the chi-square test, SafeStats achieves a 1.5 $\times$ runtime speedup and a 4.2 $\times$ reduction in communication compared to directly using the current general-purpose 2PC library to realize it.

  匹配依据：MPC: secure two party computation

  </details>

- **Efficient Private Filtering and Aggregation for Weighted Set Intersection via Oblivious Encrypted Weight Transfer**
  2026-07-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1543)
  Xiaodong Wang, Shengzhe Meng, Zijie Lu, Bei Liang

  <details><summary>摘要 / Abstract</summary>

  Private Set Intersection (PSI) enables parties to compute the intersection of their input item sets while preserving privacy. In many real-world applications, however, each item is accompanied by a sensitive weight, and the ability to privately compute over such weights is crucial. Existing research in this direction is fragmented and driven by application-specific goals, with representative examples including PI-Sum (computing the sum of weights over the intersection), inner-product Private Join and Compute (computing the inner product of weight vectors over the intersection), and Item with Maximum Weight Sum (identifying the intersection item with the maximum combined weight). In this work, we propose a unified framework for private computation on weighted set intersection. We formalize \textit{Private Filtering and Aggregation for Weighted Set Intersection} (PFA-WSI) as an ideal functionality parameterized by a joint scoring function $f$ and a predicate $P$, supporting two output modes: (i) \emph{predicate-filtered output}, which reveals a predicate-selected subset of intersection items, and (ii) \emph{aggregated output}, which reveals only aggregate statistics over matched items. By instantiating $f$ and $P$ appropriately, PFA-WSI captures deployed and studied tasks such as PI-Sum, inner-product PJC, and IMWS, and also accommodates richer metrics arising in practice, such as $L_1$- and $L_2$-type distance statistics on matched item weights. To realize PFA-WSI efficiently, we introduce a novel core building block, Oblivious Encrypted Weight Transfer (OEWT), which enables a receiver to obtain encryptions of the sender&#x27;s weights for intersection items and random-looking ciphertexts otherwise. Building on OEWT and additively homomorphic encryption, we present modular protocol constructions for different instantiations of $f$ and for both output modes. We prove simulation-based security in the semi-honest model and provide detailed communication and computation analyses. Our experiments show that our constructions scale to million-sized sets with practical performance that matches or surpasses the state-of-the-art.

  匹配依据：MPC: private set intersection

  </details>

- **Ciphertext-Native Watermarking for RLWE-Based Homomorphic Encryption**
  2026-07-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.25222)
  Yufei Zhou, Peijia Zheng

  <details><summary>摘要 / Abstract</summary>

  Homomorphic encryption (HE) schemes based on the Ring Learning with Errors (RLWE) problem have been rapidly developed and widely applied to secure computation tasks, such as privacy-preserving deep learning inference and database queries. However, existing HE schemes mainly focus on the feasibility and efficiency of homomorphic computation, while practical requirements including ciphertext copyright protection, provenance tracking, and computation supervision remain largely unexplored. In this work, we propose a watermarking technique for RLWE-based HE ciphertexts. By exploiting the algebraic structure of RLWE polynomials, we embed watermark information into ciphertext noise without affecting plaintext correctness. To address watermark degradation caused by homomorphic operations, we introduce two practical schemes. The first scheme, ARWMark, leverages noise stratification to achieve robustness against homomorphic additive operations. The second scheme, MRWMark, is based on the roots of a linear equation and supports zero-bit watermarking while remaining robust against both homomorphic addition and multiplication. We provide rigorous theoretical analysis demonstrating that the proposed schemes preserve the original security of HE while maintaining correctness and watermark robustness. Extensive experiments further validate the effectiveness and practicality of the proposed watermarking schemes.

  匹配依据：MPC: secure computation

  </details>

- **Batched Oblivious Transfer with Square-Root Communication**
  2026-07-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1541)
  Yicheng Li, Claudio Orlandi, Lawrence Roy, Yizhou Yao

  <details><summary>摘要 / Abstract</summary>

  Oblivious Transfer (OT) is a fundamental cryptographic primitive and a core building block for many multiparty cryptographic protocols. While existing OT extension techniques achieve excellent asymptotic efficiency for very large batches, their performance degrades when the total number of OTs is only moderate, since the cost of generating the required base OTs is no longer effectively amortized. In this work, we close this gap by presenting OT constructions that achieve square-root communication complexity for batched OT generation. Concretely, our most efficient protocol generates ell random OTs using O(lambda sqrt(ell)) bits of communication, where lambda is the security parameter. Our constructions are inspired by recent advances in homomorphic secret sharing and techniques for distributed discrete logarithm computation, and explore complementary points in the design space. The first construction is based on the Damgård-Jurik cryptosystem and standard assumptions, at the cost of a one-time trusted setup. The second eliminates the need for trusted setup, relying instead on a power-DDH assumption over prime-order groups. For 128-bit security, our schemes require approximately 2.6 KiB and 1.25 KiB of communication, respectively, to generate 128 random OTs, including the hash key in the power-DDH construction. Our best construction outperforms existing OT extension techniques for batch sizes of up to 32,768 OTs.

  匹配依据：MPC: oblivious transfer, secret sharing

  </details>

- **UM-PSO: A Unified Multi-Party Framework for Private Set Operations against a Dishonest Majority**
  2026-07-27 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1537)
  Yaxi Yang, Xiaojian Liang, Weizhan Jing, Ye Dong, Xiangfu Song, Fangyuan Sun, Pu Duan, Tianwei Zhang

  <details><summary>摘要 / Abstract</summary>

  Private Set Operations (PSO) enable mutually untrusted parties to securely compute arbitrary functions (e.g., union, intersection, and cardinality) over their private input sets. These operations have wide applications in many real-world scenarios. Existing PSO protocols fall short of practical deployment for several reasons. (1) \textit{Function-specific}. Real-world privacy-preserving applications often require multiple set operations within the same task, while existing solutions typically address individual functionalities (e.g., intersection or union) in isolation, making it difficult and costly to support diverse set operations in a unified and efficient manner. (2) \textit{Lacking malicious security}. As PSO is commonly employed in highly sensitive applications, it is often necessary to provide strong security guarantees against malicious adversaries. Unfortunately, most existing works only achieve semi-honest security, which limits their practical applicability. (3) \textit{Restricted settings}. The majority of existing works focus exclusively on the two-party setting. How to extend them securely and efficiently to the multi-party setting while tolerating a malicious majority remains unclear. To date, designing a maliciously secure multi-party PSO (mPSO) framework that efficiently supports diverse set operations remains an open challenge. This paper presents the \textit{first} maliciously secure mPSO framework, named UM-PSO, that supports a broad range of set operations with practical efficiency. At the core of our framework is a function-independent preprocessing phase that prepares a reusable pool of secret-shared items, which can then be leveraged to securely compute diverse set functionalities in the online phase. To achieve malicious security efficiently, we design verification mechanisms on top of SPDZ-based authenticated secret sharing, along with tailored techniques and optimizations to further improve practical performance. We implement our protocols and report concrete performance results. For a representative setting with 5 parties and a total of $2^{12}$ 128-bit items, our framework achieves an online running time of $0.627$ seconds and incurs $3.35$ MB of communication. Compared to the baselines, our framework achieves up to $51\times$ speedup and up to a $76\times$ reduction in communication.

  匹配依据：MPC: secret sharing

  </details>

- **STEBR: A Timed-Erasure, Threshold-Gated Backup Ratchet**
  2026-07-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1513)
  Shaurya Pratap Singh

  <details><summary>摘要 / Abstract</summary>

  The Signal Protocol’s Double Ratchet and X3DH/PQXDH handshakes give in-transit messages forward secrecy and post-compromise security: compromising a session key does not expose past traffic, and the protocol self-heals after a fresh Diffie–Hellman step. Encrypted backups, by contrast, are commonly protected by a single static secret, a “Backup Recovery Key” generated once and held constant until manually rotated. We show, with an explicit attack, that this baseline design provably fails even a minimal forward-secrecy-style security notion: disclosure of the key at any time exposes the entire backup history, with no self-healing. This is not a hypothetical concern: a June 26, 2026 joint FBI/CISA advisory attributes exactly this exploitation pattern to two Russian intelligence-linked clusters, tracked as UNC5792 and UNC4221, who obtained victims’ Backup Recovery Keys through impersonation-based social engineering rather than cryptanalysis. We propose STEBR (Secure Timed-Erasure Backup Ratchet), a backup-key architecture built from three composable layers: (1) a self-erasing hashchain key ratchet so that compromise of the current backup key exposes only a bounded, recent window of history rather than the full archive; (2) (t, n) threshold secret sharing of the current epoch key across independently held devices/guardians so that no single credential extracted in one social engineering interaction is sufficient; and (3) an interactive, rate-limited, out-of-band confirmation gate on any restore request so that possession of valid recovery material is necessary but not sufficient to complete a restore. We give formal security definitions for each property and prove them via standard reductions (PRF security of the key-derivation function, IND-CPA security of the backup AEAD scheme, the information-theoretic secrecy of Shamir sharing, and the authenticity of the existing ratchet-protected control channel). All three layers are composed on top of existing Signal Protocol primitives; none require modifying the Double Ratchet, X3DH/PQXDH, or the wire format of message envelopes. This is a proposal for hardening the backup-key management layer specifically; we make no claim that the Signal Protocol’s transport-layer cryptography is broken or requires replacement the cited advisory itself states plainly that it is not.

  匹配依据：MPC: secret sharing

  </details>

- **ConvertInput-Free Vector Homomorphic Secret Sharing and Its Applications**
  2026-07-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1517)
  Fan Yang, Fucai Luo, Xingfu Yan, Haining Yang, Zheng Gong, Wing W. Y. Ng

  <details><summary>摘要 / Abstract</summary>

  This work presents ConvertInput-Free Vector Homomorphic Secret Sharing (Vector-HSS), a novel HSS primitive based on the Decisional Composite Residuosity (DCR) assumption. Our construction enables efficient high-dimensional vector computations while avoiding the costly $\texttt{ConvertInput}$ operation. As a unified framework, Vector-HSS can be used as a building block for Private Information Retrieval (PIR), Secure Multi-Party Computation (MPC), Privacy-Preserving Machine Learning (PPML), etc. The key idea behind Vector-HSS is to introduce a vector-centric computation paradigm. Unlike traditional approaches, this design allows the server to perform natural and efficient vector computations without the $\texttt{ConvertInput}$ operation while keeping client-side overhead comparable to that of state-of-the-art solutions. To further improve efficiency, we develop a batching mechanism based on the Chinese Remainder Theorem (CRT) that enables parallel computation across multiple vectors. Building on these techniques, we further design a suite of protocol modules to securely support Euclidean/cosine distance computation, comparison, and matrix-vector multiplication in practical applications. Experiments show that our scheme achieves $280\times$ and $70\times$ speedups over prior HSS schemes (EUROCRYPT 2021 and S&amp;P 2026, respectively) for batched inner product evaluation. When applied to privacy-preserving image retrieval, our method achieves sub-second retrieval time, outperforming state-of-the-art solutions under similar security requirements.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **QuantumChain: Blockchain-Backed Quantum Federated Learning for Financial Fraud Detection**
  2026-07-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.21449)
  Epameinondas Douros, Konstantinos Dalampekis, Nouhaila Innan, Ioannis Theodonis, Muhammad Shafique

  <details><summary>摘要 / Abstract</summary>

  Financial fraud detection is challenged by decentralized data, severe class imbalance, and privacy constraints. This paper presents QuantumChain, a secure Quantum Federated Learning (QFL) framework that combines hybrid quantum-classical neural networks, encrypted federated aggregation, blockchain-based auditability, and quantum-secure communication. Each client trains a local hybrid model in which a variational quantum circuit is embedded between classical neural layers, while model updates are protected through homomorphic encryption, threshold secret sharing, and QKD-based keying. A permissioned blockchain records aggregation events and supports reputation-weighted trust among participants. We evaluate QuantumChain on financial transaction data using a compact, size-matched classical baseline to isolate the effect of the quantum layer. Results show that the HQNN achieves comparable accuracy while improving fraud-class recall in most settings, reaching 94.6% recall compared with 93.2% for the classical model. The Deep QLayer improves performance in full-data settings, suggesting that added circuit depth helps recover representational capacity when the shallow circuit becomes limited. Mixed-state simulations further show that the recall trend persists under non-ideal quantum evolution. In federated deployment with 10 heterogeneous clients, global accuracy increases from 97.7% to 98.8% over five rounds before stabilizing. These results show that QuantumChain can integrate depth-aware hybrid quantum models into a secure federated fraud-detection pipeline while maintaining stable global convergence.

  匹配依据：MPC: secret sharing

  </details>

- **Updatable Private Set Union: Generic Construction with Efficient Instantiation**
  2026-07-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1497)
  Seongbong Choi, Hyung Tae Lee

  <details><summary>摘要 / Abstract</summary>

  Private set union~(PSU) allows two parties to compute the union of their private sets without revealing their intersection. In many real-world applications, parties&#x27; datasets undergo frequent updates as elements are added or removed over time. Existing PSU protocols, however, must recompute the entire union from scratch whenever either party&#x27;s set changes. This becomes highly inefficient when updates are small or frequent relative to the original set sizes. In this paper, we introduce the first updatable PSU~(uPSU) protocol for the standard two-party setting, which supports efficient incremental updates. We present a systematic classification of all possible update scenarios, which shows that only a small subset of updated elements actually modify the union, and establish the leakage baseline for uPSU. Based on these classification and leakage baseline, we provide a generic construction for uPSU that uses existing PSI and a tagged variant of PSU as building blocks. We prove security against semi-honest adversaries in the simulation-based model, and guarantee that incremental updates reveal no more information than a fresh execution of a standard PSU protocol on the updated sets. We instantiate and implement our generic construction using Kim et al.&#x27;s PSU protocol~(ACM SAC 2026) and Raghuraman and Rindal&#x27;s PSI protocol~(ACM CCS 2022), demonstrating significant performance improvements over full recomputation of the union, even though its cost still depends on the original set size rather than purely on the update size. For set size $n = 2^{20}$ and update size $t = 2^{12}$, our protocol achieves a 14.1--45.4$\times$ speedup with a 4.8--59.1$\times$ communication reduction over full recomputation using baseline PSU protocols.

  匹配依据：MPC: private set union

  </details>

- **Construction of a Class of Communication-Efficient Quantum Secret Sharing Schemes**
  2026-07-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.19891)
  Chenhao Li, Zhihui Li, Jiansheng Guo, Yixin Chen, Yewei Wang

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing is a fundamental technique in quantum cryptography. However, in practical quantum networks, it still faces several bottlenecks, such as high quantum communication cost and low transmission efficiency. To reduce the communication cost, ramp quantum secret sharing schemes have been proposed in existing studies. Nevertheless, intermediate sets in such schemes may leak partial information about the secret. To address this problem, this paper presents a method for detecting intermediate sets. Based on this method, we further propose a communication-efficient perfect quantum secret sharing scheme with eavesdropping detection capability.We analyze the communication cost under different numbers of participating parties and determine the range of participants that minimizes the reconstruction communication cost. The results verify the communication efficiency and security of the proposed scheme.

  匹配依据：MPC: secret sharing

  </details>

- **Privacy-Preserving Counterfactual Explanations for Federated AI**
  2026-07-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1488)
  Sjoerd Berning, Vincent Dunning, Thijs Veugen, Kevin Witlox

  <details><summary>摘要 / Abstract</summary>

  As the usage of Artificial Intelligence (AI) for sensitive purposes increases, there is a growing need for privacy-aware explainable AI (XAI) tools. In this paper, we present a privacy-preserving counterfactual explanation algorithm. Our starting point is a decision-support model that is able to operate on vertically partitioned datasets, meaning that each party holds a different subset of datapoint attributes. The goal of a counterfactual algorithm is to find, given an observation, a datapoint from the (virtual) dataset that is closest to the observation but has a different label. Our algorithm fully preserves the privacy of the n datapoints belonging to the different parties by combining the strengths of homomorphic encryption and secret sharing. Through a number of experiments, we demonstrate the added value of combining multiple datasets in a realistic scenario and show that the privacy-preserving solution does not affect the accuracy. We fully implement our solution and demonstrate that it scales as to thousands of datapoints.

  匹配依据：MPC: secret sharing

  </details>

- **MQ on my Hardware: Performance Analysis of MQOM on FPGA**
  2026-07-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1483)
  Stelios Manasidis, Quinten Norga, Suparna Kundu, Ingrid Verbauwhede

  <details><summary>摘要 / Abstract</summary>

  Recent algorithmic advancements in the Multi-Party Computation-in-the-Head (MPCitH) paradigm have resulted in more efficient post-quantum digital signature schemes. MQOM is a MPCitH-based digital signature scheme and candidate in the ongoing NIST Post-Quantum Cryptography (PQC) standardization effort, offering performance competitive with lattice- and multivariate-based schemes in software. In this work, we develop a dedicated hardware accelerator for MQOM and analyze the impact of recent algorithmic modifications on hardware performance. This is achieved through the careful co-design of high-throughput symmetric primitive engines and highly-optimized polynomial arithmetic cores, minimizing stalling and supporting entirely on-the-fly computations of all polynomial arithmetic. As a result, no intermediate buffers are required and re-computation or sampling is avoided. Secondly, we analyze MQOM&#x27;s use of correlated GGM trees for generating MPC party shares, which reduce computational cost at the cost of increased signature size. We observe that this choice leads to increased design flexibility and significantly reduces on-chip memory requirements for hardware designs. Furthermore, MQOM proposes several parameter sets per security level. We analyze the impact of different MQOM parameter sets on hardware cost and performance. Our design with NIST L1 parameters only requires 15 812/9 384 LUTs/FFs and 4.5 BRAMs on FPGA, while performing the signature generation in 0.46 ms and signature verification in 0.38 ms. Compared to state-of-the-art hardware implementations of other MPCitH-based DSAs, we improve the area-time-product (ATP) by a factor $3.5\times$ up to $66.4\times$. Compared to the lattice-based ML-DSA scheme, our MQOM hardware design is only outperformed by a factor $1.5\times$. Our results show that MQOM and the correlated GGM tree structure are hardware-friendly designs, leading to one of the highest HW-vs-SW speedup ratios among similar PQC DSAs, while also attaining the smallest on-chip memory footprint among high-performance hardware implementations.

  匹配依据：MPC: multi party computation

  </details>

- **GHZ-Equivalent State Distribution in Quantum Networks: Reducing Decoherence and Quantum Resource Consumption**
  2026-07-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.17101)
  Chun-Hsiang Wang, Chia-Wei Tsai

  <details><summary>摘要 / Abstract</summary>

  This study proposes a novel scheme for distributing GHZ-equivalent states across repeater-based quantum networks, with particular focus on the analysis and mitigation of decoherence effects during transmission. The proposed scheme enables remote users to share graph states, which can be leveraged to implement various quantum communication protocols, such as quantum key distribution and quantum secret sharing. Compared with existing approaches, the proposed distributed scheme requires only O(N) qubits without introducing redundant entanglement structures. Together with the linear-scaling merging procedure in both controlled gate count and qubit usage, the proposed framework supports more efficient large-scale graph state distribution. To evaluate its feasibility and correctness, this study utilizes the quantum network simulation tool, NetSquid, to implement the proposed scheme. Simulation results demonstrate that the proposed approach is both effective and practical for executing quantum communication protocols within quantum networks.

  匹配依据：MPC: secret sharing

  </details>

- **Blind Transpiler: An open-source library for universally blind and homomorphic quantum computations**
  2026-07-19 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.17131)
  Mohit Joshi, Manoj Kumar Mishra, S. Karthikeyan

  <details><summary>摘要 / Abstract</summary>

  Blind quantum computation is a cryptographic primitive that allows a limited-capability client to delegate its complex computation to a remote server without revealing its data and/or computation. This branch of quantum cryptography has been bifurcated into two distinct primitives, quantum homomorphic encryption (concerning the security of only data) and universal blind quantum computation (concerning the security of data and the computing algorithm). These primitives have immense applicability in problems like secure cloud computing, secure quantum variational algorithms, quantum federated learning, and secure multiparty computation. However, no software tools exist for the rapid prototyping of such protocols, hindering the academic interrogation for potential applications. In this paper, we describe the development of the first such library for transpiling circuits written in Qiskit to its blind counterpart, which can then be delegated in a client-server architecture without revealing the client&#x27;s data and/or computation. The proposed library is designed in modular and reusable component layers, enabling easier scalability to newer BQC primitives and robustness against changes in underlying primitives. We show the implementation of these primitives to a blind variational quantum classifier for the IRIS dataset.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Optimal Distributed Monotone-Policy Encryption for DNFs and More from Lattices**
  2026-07-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1464)
  Jeffrey Champion, David J. Wu

  <details><summary>摘要 / Abstract</summary>

  Distributed cryptography is a new cryptographic paradigm that enables fine-grained decryption capabilities in a trustless setting. In a distributed monotone-policy encryption scheme, users generate their own public and private keys. Thereafter, one can encrypt a message with respect to an arbitrary set of public keys together with an access policy. Any group of users that satisfies the access policy can recover the message; conversely, the message is computationally hidden from any group of users that does not satisfy the policy. The key requirement is succinctness: the size of the ciphertext should be sublinear in the size of the access policy. Distributed monotone-policy encryption generalizes related notions like distributed broadcast encryption (where the access policy is set membership) and silent threshold encryption (where the access policy is a threshold policy). In this work, we achieve the following: - First, we give the first optimal distributed monotone-policy encryption scheme for the class of DNF policies from the decomposed LWE assumption in the random oracle model. Here, optimal means that the size of the public parameters, the user public keys, and the size of the ciphertext are independent of the size of the policy. As a corollary, we also obtain a (reusable) succinct computational secret sharing scheme for DNFs from decomposed LWE in the random oracle model. - Next, we show how to adapt our techniques to obtain a distributed monotone-policy encryption scheme for $k$-DNFs in the plain model where the size of the ciphertext is $k \cdot L^{1/2}$, $k$ is the maximum size of each min-term, and $L$ is the number of min-terms in the DNF. This is the first scheme from the decomposed LWE assumption in the plain model. If we settle for a much weaker notion of selective security, then we also achieve full succinctness in the plain model (i.e., where the ciphertext size is independent of the size of the DNF). - By specializing our results to the setting of broadcast encryption, we obtain an adaptively-secure distributed broadcast encryption scheme with ciphertext size $|S|^{2/3}$, where $|S|$ is the size of the broadcast set. Security relies on decomposed LWE (with a polynomial modulus-to-noise ratio) in the plain model. This scheme is the first lattice-based scheme with adaptive security that supports an a priori unbounded number of users in the plain model. Previous lattice-based distributed broadcast encryption schemes with adaptive security in the plain model assumed an a priori bound on the number of users (but achieved optimal-size ciphertexts that are independent of the size of the broadcast set).

  匹配依据：MPC: secret sharing

  </details>

- **IBE and PIR from Isogenies**
  2026-07-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1457)
  Shweta Agrawal, Andrea Basso, Sikhar Patranabis

  <details><summary>摘要 / Abstract</summary>

  We significantly expand the reach of isogeny-based cryptography by constructing, for the first time, two fundamental primitives that have long remained out of reach from isogenies: identity-based encryption (IBE) and semi-honest single-server private information retrieval (PIR) with communication polylogarithmic in the database size. Our IBE additionally achieves anonymity, which means that the ciphertexts hide both the message and the recipient identity. Our results are enabled by new techniques for constructing cryptographic primitives from structured isogeny computations, centered around the first construction of blind batch encryption from isogenies. To establish its security, we introduce a new hardness assumption, CDH with Mismatched Torsion (CDHwMT), which informally captures the hardness of a CDH-like problem in the presence of structured auxiliary isogeny information. We provide evidence for its plausibility by showing that, in the Algebraic Isogeny Model, CDHwMT reduces to well-studied isogeny assumptions. The same techniques yield further cryptographic applications: the first isogeny-based hierarchical IBE, laconic oblivious transfer, and public-key encryption simultaneously achieving high-rate leakage resilience and key-dependent-message/circular security. All of our constructions can be conjectured to be post-quantum secure. Beyond these individual primitives, our results demonstrate that isogenies can support substantially richer cryptographic functionality than previously known, and provide new tools toward building advanced post-quantum cryptography.

  匹配依据：MPC: oblivious transfer

  </details>

- **Combinatorial aspects of holographic quantum secret sharing**
  2026-07-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.16110)
  Ning Bao, Keiichiro Furuya, Jacob March

  <details><summary>摘要 / Abstract</summary>

  We introduce combinatorial holographic quantum secret sharing (CHQSS) for a bulk subregion in AdS$_3$/CFT$_2$ to study how logical information of the bulk subregion is encoded in the boundary and protected from erasures of boundary subregions. We introduce a distance, a reconstruction threshold, and a secret threshold to characterize CHQSS schemes. We present the phase transitions of multipartite entanglement wedges in a symmetric setup and observe multiple distinct phase transition points. The distance and thresholds depend on the holographic phase and the choice of bulk subregion. We derive the maximum distance. Moreover, we derive the relations between the distance and the thresholds. We construct a family of CHQSS schemes in the symmetric setting that includes perfect threshold CHQSS and perfect non-threshold CHQSS.

  匹配依据：MPC: secret sharing

  </details>

- **NFSA: Non-Forward Secure Aggregation with One Server via Two Layer Secret Sharing**
  2026-07-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.15052)
  Yufei Zhou

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) enables collaborative model training while preserving privacy by keeping data local. However, the risk of sensitive data leakage through model updates necessitates the use of secure aggregation protocols. Existing server-based secure aggregation protocols typically require the server to forward sensitive data shared between users, which increases communication overhead and introduces potential security risks. In this work, we propose a novel secure aggregation protocol based on two-layer secret sharing to address these issues. By combining Shamir&#x27;s Secret Sharing with 2-out-of-2 additive secret sharing using a Pseudo-Random Function (PRF), our protocol eliminates direct communication between users, thereby removing the need for the server to forward data. We further extend the protocol with Key-homomorphic PRF (KhPRF) to support high-dimensional data aggregation and apply it to FL, enabling one-shot secure aggregation with a single server and no intermediary data forwarding. To reduce user overhead, we design a new encoding method based on the Chinese Remainder Theorem for the almost KhPRF-based mask, reducing the number of KhPRF calls and mitigating the model update expansion issue after masking. Experimental results show that our scheme significantly outperforms existing methods in terms of auxiliary node overhead. For instance, when the number of users is 100, our scheme improves communication efficiency by nearly 100 times and reduces computational overhead by approximately 17\%. Moreover, user computation time can be reduced by 51\% to 75\% when the input length is $2^{18}$.

  匹配依据：MPC: secret sharing

  </details>

- **Batched Attribute-Based Encryption from Bilinear Pairings**
  2026-07-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1454)
  Ramprasad Sarkar, Shayeef Murshid, Mriganka Mandal

  <details><summary>摘要 / Abstract</summary>

  Batched identity-based encryption (batched IBE), introduced by Agarwal, Fernando, and Pinkas (CRYPTO 2025), enables a key authority to issue a single succinct key that decrypts an entire batch of ciphertexts. However, existing batched encryption protocols support only identity-based access control and do not accommodate expressive attribute-based policies. We are the first to introduce Batched Attribute-Based Encryption (B-ABE), a generalization of batched encryption to the attribute-based setting. In B-ABE, ciphertexts are associated with attribute sets and batch labels, while a single batch key is bound to an access policy and a public digest of the batch. The key decrypts exactly those ciphertexts in the batch whose attributes satisfy the policy, and its size is independent of the batch size. We construct B-ABE in asymmetric bilinear groups and prove security under the standard Decisional Bilinear Diffie-Hellman (DBDH) assumption in the random oracle model. We further introduce the first Threshold Batched Attribute-Based Encryption (TB-ABE), in which the master secret is distributed among L authorities via Shamir secret sharing. Any subset of at least T authorities can non-interactively generate publicly verifiable key shares that aggregate into a succinct batch key of the same asymptotic size as in the single-authority setting. We formalize security against static corruptions of up to (T-1) authorities and adaptive key-share queries and prove security under the DBDH assumption in the random oracle model.

  匹配依据：MPC: secret sharing

  </details>

- **Sublinear-Communication Layered MPC from HSS**
  2026-07-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1445)
  Anasuya Acharya, Pierre Meyer, Divya Ravi, Rahul Satish

  <details><summary>摘要 / Abstract</summary>

  The server-aided Secure Multi-Party Computation (MPC) model with dynamic participation, where servers may join or leave during the computation is particularly well-suited for practical, long-running applications. Unfortunately, existing protocols supporting dynamic participation either incur communication costs that scale linearly with the circuit size or rely on the heavy hammer of Fully Homomorphic Encryption (FHE). This contrasts with “classic” MPC protocols, where sublinear communication can be achieved without FHE. Focusing on the Layered MPC framework (introduced by David, Ishai, Konring, Kushilevitz, and Narayanan, CRYPTO 2023), we show that this overhead is not inherent. We construct sublinear-communication Layered MPC protocols while maintaining a minimal number of online servers — only two or three per layer. Our constructions rely on a layered-friendly adaptation of Homomorphic Secret Sharing (HSS), which we formalize as HSS with Layered Resharing.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Compressed Post-Quantum Silent OT from Isogenies**
  2026-07-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1444)
  Pouria Fallahpour, Arthur Herlédan Le Merdy, Mahshid Riahinia

  <details><summary>摘要 / Abstract</summary>

  Oblivious transfer (OT) is a foundational tool in secure computation. Random OT-correlated pairs of the form $(r_0,r_1)$ and $(b,r_b)$, where $r_0,r_1,b \stackrel{{}_\$}{\leftarrow} \{0,1\}$, significantly speed up secure computation protocols. Pseudorandom correlation functions (PCFs), introduced by Boyle et al. (FOCS 2020), are an efficient means of non-interactively generating correlated pairs. In a PCF, two parties store short keys that are used to locally generate large amounts of correlated pairs. While pre-quantum PCFs for OT achieve highly compact key sizes (e.g., $30$ kB), a significant gap remains in the post-quantum regime, where existing solutions rely on lattices or learning-parity-with-noise-style assumptions and yield much larger keys. We construct compact post-quantum PCFs for OT. Our construction has key sizes in the range of $100$ kB, approaching the compactness of pre-quantum PCFs and seven times smaller than the most compact state-of-the-art post-quantum alternatives. The key size of our PCF remains invariant regardless of the target number of OTs, in contrast to prior alternatives. We estimate a throughput of $7$ OTs per second for our PCF. We additionally provide a security proof in the quantum random oracle model, constituting the first such analysis of a post-quantum PCF. The core of our construction is a new, compact constrained pseudorandom function (CPRF) for inner-product membership predicates. Its security is based on a natural extension of the parallelization problem, which we introduce as the parallelization problem with auxiliary inputs. We provide an extensive analysis of this assumption as well as an implementation of our construction.

  匹配依据：MPC: oblivious transfer, secure computation

  </details>

- **CoSecRAG: Efficient Vector Similarity Search with Database and Query Privacy for RAG**
  2026-07-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1442)
  Moyang Xie, Jiacheng Gao, Yuan Zhang, Sheng Zhong

  <details><summary>摘要 / Abstract</summary>

  Retrieval-augmented generation (RAG) grounds large language models on external knowledge by using vector similarity search over document embeddings to identify relevant documents and supplying their contents as generation context. However, its retrieval stage creates privacy risks: user queries may reveal sensitive intents, while the database may contain proprietary or confidential records. Existing secret-sharing-based solutions that protect both query and database privacy remain costly. To make private vector similarity search more efficient, we present CoSecRAG, a two-server system for RAG that protects both database and query embeddings. CoSecRAG introduces Inner Product Preserving Query Mask (IPQ-Mask) to lower similarity-scoring costs by avoiding online secure multiplications and Post-Scoring Cluster Pruning (PSCP) to reorganize the execution pipeline for approximate retrieval, reducing private-extraction volume and secure top-K selection costs. We implement CoSecRAG and evaluate it on six BEIR datasets and large-scale synthetic benchmarks. CoSecRAG maintains strong retrieval quality while substantially reducing the cost of private vector similarity search. Compared with P²RAG, the most recent two-server baseline for private vector similarity search in RAG, CoSecRAG achieves up to 181× online score-computation speedup and 81× online speedup in secure top-K computation. End-to-end, it achieves up to 99× online and 34× offline runtime speedups. Compared with PRAG, CoSecRAG achieves 19×–58× online and 2×–16× offline end-to-end speedups.

  匹配依据：MPC: secret sharing

  </details>

- **Verifiable and Collusion-Resistant Multi-Party Quantum Private Set Operations**
  2026-07-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.27994) · [IACR ePrint](https://eprint.iacr.org/2026/1436)
  Zixian Gong, Kun Tian, Yi Zhang, Fengxia Liu

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) and, more broadly, private set operations (PSO) are fundamental primitives for secure multiparty computation (SMC), enabling participants to jointly compute set relations while revealing no information beyond the prescribed output. As quantum technologies advance, PSI have correspondingly evolved toward quantum secure phase. Existing quantum PSI (QPSI) solutions are limited in their threat models and collusion behavior between third party (TP) and participants. In this work, we present a multi-party QPSI (MP-QPSI) protocol that integrates verifiable quantum fully homomorphic encryption (vQFHE) as the verifiable outsourced quantum-evaluation layer and threshold fully homomorphic encryption (TFHE) as the threshold key-management mechanism. We instantiate the intersection computation via a \(C^{\mathsf{AND}}\) circuit accompanied by simulations on IBM Quantum Platform. We analyze correctness and participant privacy against TP, external eavesdroppers, and collusive behaviors, and we further prove verifiability against a malicious TP under the semantic security model. Finally, we present a modular framework perspective with several realizations, show how to extend the construction to quantum private set union (QPSU) via open-controlled operations. Compared with prior schemes, our protocol provides flexible set operations and stronger resilience under the TP model, including TP-participant collusion, thereby offering enhanced security and broader applicability.

  匹配依据：MPC: private set intersection, private set union, secure multiparty computation

  </details>

- **Proof in a Bottle: Long-Lived Verifiable Secret Sharing via Pre-Quantum Commitment and Immutable Ledger Binding**
  2026-07-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.13235)
  Markus Jakobsson, Keir Finlow-Bates

  <details><summary>摘要 / Abstract</summary>

  Traditional secret sharing techniques such as Verifiable Secret sharing (VSS) are vulnerable to quantum attacks by a Cryptographically Relevant Quantum Computer (CRQC) running Shor&#x27;s algorithm. We observe that the binding a VSS needs is required only at the moment of dealing, and this binding can be made before any CRQC exists. We propose Proof in a Bottle (PiB), which decouples verifiability from long-term binding: standard Pedersen commitments provide zero-knowledge, publicly checkable consistency during a pre-quantum window, while a salted, index-bound hash of the share set, anchored to an immutable public ledger, preserves the binding established in that window into the post-quantum era. The guarantee is explicitly a commit-now, reveal-later one: it protects today&#x27;s honest dealings against tomorrow&#x27;s quantum adversary.

  匹配依据：MPC: secret sharing

  </details>

- **TRAPGC-DV: Trapdoor Garbled Circuit Designated Verification of Groth16 on Bitcoin**
  2026-07-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1430)
  Ariel Futoransky, Fadi Barbàra, Ramses Fernandez, Gabriel Larotonda, Sergio Demian Lerner

  <details><summary>摘要 / Abstract</summary>

  Verifying Groth16 proofs on Bitcoin enables a broad class of trust-minimised applications, bridges, light clients, validity rollups, but Bitcoin script lacks the pairing operations required to evaluate the verification equation natively. A recent line of work on Bitcoin-side garbled-circuit SNARK verification (Delbrag, BitVM3, BitVMX-GC, Glock, Argo MAC) has produced practical constructions but does not provide formal universal-composability analysis. We present $\Pi_{\mathsf{DV\text{-}Groth16}}$, a protocol for designated evaluation of Groth16 proofs on Bitcoin. The prover holds a standard Groth16 proof $\pi_{\mathsf{in}}$ under a public, one-time ceremony SRS. The verifier generates, from a secret seed, a compact per-session trapdoor SRS for a fixed outer circuit, the inner Groth16 verifier, computed natively over a one-layer 2-chain (BLS12-377 inside BW6-761), and proves it well-formed. The prover produces an outer Groth16 proof that her inner proof verifies, and garbles a small circuit that checks the outer proof in scalar form: after the verifier reveals his seed, the prover signs the discrete logarithms of her pre-committed outer proof elements, and the circuit checks them against the commitments together with the scalarized verification identity, releasing a slashing key on failure. Cut-and-choose enforces garbling correctness; deposits and commitments are locked in Bitcoin UTXOs with a three-tier settlement (refund, slash-fast, slash-commit). The per-session SRS has fixed size, independent of the assertion circuit, and all elliptic-curve computation inside the garbled circuit reduces to three fixed-base scalar multiplications. We prove that $\Pi_{\mathsf{DV\text{-}Groth16}}$ GUC-emulates an ideal functionality $\mathcal{F}_{\mathsf{DV\text{-}Groth16}}$ capturing the three-tier behaviour against static corruption in the GUC-hybrid model, with a concrete bound assembled from named primitive advantages. We make precise how designated evaluation and enforcement differs from designated-verifier deniability, and exhibit a variant achieving the latter at the cost of a per-proof SRS for the assertion circuit itself.

  匹配依据：MPC: garbled circuit

  </details>

- **Coupling Leakage in Theory and Practice - Unveiling (Post-PnR) Security Flaws in Masked FPGA-Mapped Designs**
  2026-07-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1426)
  Nicolai Müller, Daniel Lammers, Simon Osterheider, Amir Moradi

  <details><summary>摘要 / Abstract</summary>

  With the widespread adoption of Field Programmable Gate Arrays (FPGAs) in security-critical industries such as defense and telecommunications, ensuring the confidentiality of sensitive data processed by these devices has become paramount. Side-Channel Analysis (SCA) poses a significant threat, necessitating the protection of cryptographic primitives through effective and efficient countermeasures. Within the framework of well-established formal adversary models, Boolean masking offers provable resistance to SCA by randomizing sensitive intermediate computations using Shamir’s secret sharing. However, the secure and efficient implementation of Boolean masking in hardware presents a complex and error-prone challenge. Physical effects such as glitches, transitions, and couplings can undermine essential security assumptions, potentially weakening the effectiveness of masking. Although robust masking schemes are designed to maintain their security in the presence of glitches and transitions, and their secure implementation can be verified at the gate level using a wide range of automated verification tools – albeit mostly for Application-Specific Integrated Circuits (ASICs) and not FPGAs – leakages caused by coupling effects remain undetectable by such tools, as they occur at a lower abstraction level. In this work, we focus on detecting (low-level) vulnerabilities in masked FPGA designs through experimental and tool-assisted evaluation. The flaws that we target are not detectable at the Register Transfer Level (RTL ) level, and in some cases, not even at the gate level, as they arise from optimizations introduced during synthesis or implementation, or from the specific outcomes of the Place and Route (PnR) process. We demonstrate that these flaws are not only theoretically concerning, but can lead to observable leakages in practical experiments. Furthermore, we show how to formally abstract, unveil, and mitigate such leakages, thereby enabling a security-aware FPGA design flow that spans from the behavioral to the physical level. As an example, we implement all the evaluation steps presented as an extension of PROLEAD and validate its accuracy and effectiveness through practical case studies.

  匹配依据：MPC: secret sharing

  </details>

- **Accelerating the AIMer Post-Quantum Signature with AVX-512: A Field–Keccak Speedup Analysis**
  2026-07-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1417)
  Seung-Won Lee, Si-Woo Eum, Hwa-Jeong Seo

  <details><summary>摘要 / Abstract</summary>

  AIMer is a post-quantum digital signature scheme with a conservative design. Its security relies only on the symmetric-key one-way function AIM2 and an MPC-in-the-Head (MPCitH) zero-knowledge proof. AIMer is a Korean post-quantum cryptography (KpqC) standard. However, the AIMer standard code released in January 2026 is a portable C reference implementation. It does not include processor-specific optimizations. As a result, it does not exploit AVX-512, a 512-bit vector instruction set available on modern processors. This paper presents an AVX-512 optimized implementation for all six AIMer variants. We parallelize binary-field multiplication with VPCLMULQDQ. The implementation processes four MPC parties per 512-bit register. We also handle conditional XOR accumulation in the linear layer with a single VPTERNLOGQ instruction. In addition, we accelerate the Keccak permutation using AVX-512VL. Our implementation is 1.60–1.84× faster than the AVX2 implementation for signing. We further analyze the source of this speedup. Contrary to common intuition, most of the improvement comes from Keccak. In the 128-bit and 192-bit variants, Keccak accounts for about 86% of the total improvement. Only in the 256-bit variants does the field-arithmetic contribution increase to about 42%, due to the wider field size. These results show that vectorizing symmetric primitives is as important as binary-field arithmetic in MPCitH signatures. In some cases, it is even more important.

  匹配依据：MPC: mpc (context)

  </details>

- **A Cryptographic Perspective on California's Delete Request and Opt-out Platform**
  2026-07-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1421)
  Aarushi Goel, Gabriel Kaptchuk, Peihan Miao, Phuoc Van Long Pham, Satvinder Singh, Rachel E. Thomas

  <details><summary>摘要 / Abstract</summary>

  The California Consumer Privacy Act (CCPA) grants consumers the right to request deletion of personal data held by registered data brokers. California’s 2023 Delete Act provides a new mechanism through which consumers can exercise this right by leveraging a centralized Delete Request and Opt-out Platform (DROP), enabling users to submit a single request that must be periodically processed by all registered data brokers. Since this platform aggregates sensitive user information, it is intentionally designed with safeguards against information leakage and unauthorized disclosure. This legislation, and the system it introduces, are positioned to serve as a template for wider deployment, with copy-cat legislation already introduced in many US states. In this document, we evaluate the privacy architecture of the first-generation DROP system from a cryptographic perspective. The proposed design relies on hash-based record linkage---a widely used technique that offers heuristic rather than rigorous privacy guarantees. We begin by analyzing the inherent risks of this approach and identifying simple, lightweight modifications that can modestly improve its privacy guarantees by making it more difficult for malicious actors to exploit these vulnerabilities. We then contrast this approach with Private Set Intersection (PSI), a class of provably secure cryptographic protocols that only reveal the intended matching records and nothing more. For future iterations of DROP, we propose a comprehensive PSI-based redesign, arguing that it would substantially reduce the risk of accidental information leakage while incurring only moderate additional computational overhead. Next, we highlight how DROP presents a compelling application for advanced variants of PSI with extended functionalities and stronger security guarantees, and we outline several research directions for the cryptography community, motivated by the unique requirements of such systems. Finally, we identify systemic risks that cannot be mitigated by PSI alone and discuss potential complementary approaches for addressing these broader challenges. We hope this document serves as a common starting point for the cryptography and policy communities working to design future data deletion systems.

  匹配依据：MPC: private set intersection

  </details>

- **Continuous-Variable MIMO THz Quantum Secret Sharing: Gaussian-modulation and Passive-modulation**
  2026-07-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.08158)
  Leixin Wu, Jiayu Pan, Fangzhe Chen, Lingtao Zhang, Bowen Zheng, Tie Qiu

  <details><summary>摘要 / Abstract</summary>

  Although quantum key distribution (QKD) enables information-theoretically secure key distribution, it is mainly designed for point-to-point communication and cannot directly support multi-user collaborative scenarios. To address this limitation, quantum secret sharing (QSS) has been proposed to enable secure multiparty key sharing. However, most existing QSS protocols rely on a single-input single-output (SISO) channel, which limits the achievable secret key rate (SKR) and transmission distance. This paper proposes a continuous-variable (CV) QSS protocol based on a multiple-input multiple-output (MIMO) architecture operating in the terahertz (THz) band. In the proposed scheme, transmit-receive beamforming decomposes the MIMO channel into multiple parallel SISO subchannels, thereby improving both the SKR and transmission distance. We describe the QSS transmission procedure and derive the SKR expressions for eight protocol variants under Gaussian collective attacks. Specifically, Gaussian modulation and passive modulation are considered at the transmitter, while homodyne and heterodyne detection are considered at the receiver. Both asymptotic and composable finite-size SKR formulas are derived to characterize the ideal upper-bound performance and the achievable performance under finite resources, respectively. Simulation results show that, under ideal assumptions including perfect channel state information, perfect phase synchronization, and ideal beamforming, the Gaussian-modulation protocol with a 32 x 32 antenna configuration and the passive-modulation protocol with a 1024 x 1024 antenna configuration achieve transmission distances of 14.99 m and 160 m in the atmospheric channel, respectively. These results provide an idealized theoretical benchmark for evaluating the potential performance gains of MIMO-assisted THz CV-QSS in indoor and short-range outdoor wireless networks.

  匹配依据：MPC: secret sharing

  </details>

- **Coded Task Offloading for Fluid Computing: A Privacy-Aware Approach under D2D Networks**
  2026-07-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.08440)
  Diego Cajaraville-Aboy, Manuel Fernández-Veiga, Ana Fernández-Vilas, Rebeca P. Díaz-Redondo

  <details><summary>摘要 / Abstract</summary>

  Fluid Computing aims to support distributed applications execution across heterogeneous cloud, edge, and device resources, motivating task execution mechanisms that adapt to dynamic and privacy-sensitive environments under runtime conditions. In this context, current task offloading schemes rarely address privacy risks and information leakage under adversarial execution settings; furthermore, most coded computing proposals focus on straggler mitigation without considering system-level objectives such as energy awareness. This paper proposes a coded task offloading scheme for D2D networks under stochastic task arrivals and queue-based dynamics. The proposal combines task offloading techniques with linear secret sharing schemes, where tasks are encoded into redundant shares to support threshold-based recovery, straggler mitigation, and privacy preservation while enhancing system performance. Then, we formulate a privacy-aware offloading problem that jointly optimizes delay and energy while penalizing the theoretical privacy leakage of coded tasks under noisy leakage observations. The problem is solved using a branch-and-bound solver alongside a lightweight heuristic scheduler, both of which are evaluated through a discrete-event simulator. Results show that coded offloading improves the delay--energy trade-off with respect to classical full and parallel offloading schemes, while the heuristic achieves near-optimal performance, outperforming baseline and state-of-the-art solvers. The results also show how privacy leakage penalties reshape offloading decisions, exposing an inherent delay--energy--privacy trade-off.

  匹配依据：MPC: secret sharing

  </details>

- **zk-ScalHard: Scalable and Hardware-Rooted Privacy-Preserving Authentication for Secure OTA Updates in Zonal SDVs**
  2026-07-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.07371)
  Shrikant Tangade, Bansi Pambhar, Valeria Loscri, Mauro Conti

  <details><summary>摘要 / Abstract</summary>

  The automotive industry is transitioning to Zonal-oriented Architectures (ZoA) for Software-Defined Vehicles (SDVs), enabling frequent over-the-air (OTA) updates for 100+ Electronic Control Units (ECUs). While OTA updates improve efficiency, they introduce safety-critical security risks. Current standards like Uptane and AUTOSAR Adaptive rely on Public-Key Infrastructure (PKI). However, PKI-based authentication creates bandwidth bottlenecks in in-vehicle and vehicle-to-cloud (V2I) communication as ECU density increases. It also risks exposing sensitive vehicle configurations and passenger privacy due to centralized architectures. Next-generation Zonal SDVs require decentralized, scalable authentication with data privacy. To address this, we propose zk-ScalHard, a hardware-rooted, privacy-preserving authentication protocol. We introduce a decentralized, hierarchical trust-promotion model utilizing Silicon Physical Unclonable Functions (PUFs) and two novel Zero-Knowledge Proof (ZKP) circuits: (1) Zonal Identity and Integrity (ZIDI) and (2) High-Performance Computing Aggregation (HPCA). These circuits employ multi-party computation (MPC) and recursive aggregation to achieve decentralization and scalability. The integration of ZKPs and PUFs ensures 100% vehicle-level data sovereignty. Benchmarked against Uptane, zk-ScalHard achieves constant O(1) communication and verification complexity, improving upon the linear O(n) complexity of current systems. Evaluation shows a 99.2% reduction in authentication bandwidth and a 99.9% reduction in the temporal attack surface. Our results demonstrate that zk-ScalHard provides a scalable, secure, and GDPR-compliant architecture for future Zonal SDVs.

  匹配依据：MPC: multi party computation

  </details>

- **SC-DT: Scalable Constant Round Secure Comparison and its Application to Privacy Decision Tree Evaluation**
  2026-07-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1389)
  Qinghui Zhang, Xiaojun Chen, Yansong Zhang, Xudong Chen

  <details><summary>摘要 / Abstract</summary>

  Numerous private decision tree evaluation (PDTE) protocols based on secure multi-party computation (MPC) have been proposed to protect sensitive data during evaluation. However, existing MPC-based PDTE protocols primarily focus on the two or three-party setting. Moreover, their core building block, secure threshold comparison, typically incurs logarithmic-round communication and dominates the online cost of tree evaluation. These limitations motivate the design of scalable and efficient secure comparison protocols for large-scale PDTE. In this paper, inspired by Falcon (PETs’2020), we propose a scalable constant round secure comparison protocol based on Shamir secret sharing in the honest-majority setting. Concretely, we leverage random shuffle to achieve zero detection with constant-round communication. Furthermore, we reduce random shuffle to random shift, thereby significantly decreasing the offline communication overhead. Besides, we reformulate feature selection and path selection in PDTE as private lookup table functionalities and integrate PLUT with our scalable comparison protocol to achieve scalable PDTE. Finally, we extend the above Shamir secret sharing-based protocols to the packed secret sharing variants and further optimize the online communication efficiency of these packed variants. We instantiate the above protocols as a framework SC-DT and report their improved performance: i) For secure comparison, our packed secure comparison achieves a speedup of $1.7-2.3\times$ and reduce communication by $1.7-2.5\times$ in the online phase compared with Helix (Cryptology ePrint’2025). ii) For large-scale PDTE, our packed secret sharing-based protocol improves online communication efficiency by up to $1.9\times$ over our Shamir-based protocol. In a 21-party WAN setting, it evaluates a 50-tree random forest with 42,550 nodes at an amortized latency of about one second per tree.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **On the Differential Uniformity of Polynomials over Galois Rings**
  2026-07-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1393)
  Sondre Rønjom, Arne Sandrib

  <details><summary>摘要 / Abstract</summary>

  Design of hash functions and pseudo-random permutations over Galois extensions of $\mathbb Z_q$ for prime powers $q$ has recently gained some interest in relation to recent directions in advanced cryptography, such as multiparty computation and zero-knowledge protocol design. Thus investigating optimality of cryptographic properties of S-boxes defined by polynomials over Galois rings is of interest. Of particular interest is the differential uniformity of such functions. To our knowledge, there are very few results on the differential uniformity for polynomials over Galois rings $\mathrm{GR}(p^k,m)$ when $k,m\geq 2$. Motivated by designing secure hash functions and block ciphers over Galois rings, a main contribution of this paper is an investigation into the differential properties of polynomials over Galois rings. Finally, we provide a classification of APN permutations in $\mathrm{GR}(4,2)$ up to affine and CCZ-equivalence.

  匹配依据：MPC: multiparty computation

  </details>

- **HANNS: Low-Storage Non-Interactive Approximate Private Nearest Neighbor Search with Sublinear Comparison Complexity**
  2026-07-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1397)
  Haowen Pan, Ruiqi Gan, Yunhao Fu, Yintai Sun, Zhou Zhang, Yuxiang Wang, Yi Chen, Bo Zhang, Haoyi Zhou, Yongxin Tong, Zhenyu Guan, Jin Dong, Song Bian

  <details><summary>摘要 / Abstract</summary>

  With growing concerns over data privacy, private nearest neighbors search (PNNS) attracts increasing research attention. Existing PNNS follow two main approaches: i) interactive PNNS based on secure multi-party computation protocols that leverage index structures to achieve sublinear complexity, and ii) non-interactive PNNS utilizing fully homomorphic encryption to minimize communication bandwid that the cost of superlinear computational complexity. To address the communication-computation dilemma, we propose HANNS, a non-interactive PNNS protocol with a sublinear number of encrypted comparisons. Our key observation is that, while the full-table scan is inevitable under the non-interactive setting, the number of costly encrypted comparisons can be significantly reduced. Specifically, we develop a cluster ordering scheme over FHE that leverages a segmented rigid transformation to obliviously identify candidate clusters with only a sublinear number of homomorphic comparisons. Furthermore, we introduce a homomorphic product quantization (PQ) scheme that enables coarse search and reranking over PQ-encoded vectors, which significantly reduces the computational and storage overheads. In the experiment, we show that HANNS achieves 41x to 277x speedup and a storage reduction of 12x to 31.7x compared to the most recent non-interactive schemes, while reducing communication by 1,258x to 80,536x and achieving a speedup of 8x to 119x over interactive schemes in low-bandwidth scenarios.

  匹配依据：MPC: secure multi party computation

  </details>

- **CILC: Cryptographically-secure Inter-agent Loop Closure Candidate Detection for Multi-Agent Collaborative SLAM**
  2026-07-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.06700)
  Andrew Fishberg, Yixuan Jia, Jonathan P. How

  <details><summary>摘要 / Abstract</summary>

  Multi-agent Simultaneous Localization and Mapping (SLAM) and collaborative SLAM (CSLAM) require robots to continuously exchange global descriptors (GDs) to detect inter-agent loop closures (ILCs). While encrypted radios protect this traffic from external eavesdroppers, they offer no protection against a compromised swarm member. We show this threat is concrete by demonstrating how a corrupted agent can reconstruct approximations of an honest agent&#x27;s imagery and trajectory from its public GD broadcasts. To address this, we propose CILC (Cryptographically-secure Inter-agent Loop Closure candidate detection), a first-of-its-kind system leveraging Secure Multi-Party Computation (SMPC) to detect ILC candidates without exchanging GDs in the clear. Rather than securing the entire CSLAM pipeline, we apply SMPC only to ILC candidate detection (i.e., GD similarity comparison), a privacy-sensitive yet computationally lightweight step, yielding an advantageous privacy-to-overhead trade-off. We validate in both simulation and hardware experiments that CILC remains real-time and communication-feasible across multimodal GDs (visual and LiDAR), while mitigating information leakage to a compromised swarm agent.

  匹配依据：MPC: secure multi party computation

  </details>

- **Privacy-Preserving Robustness Verification for Neural Networks**
  2026-07-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.05251)
  Nianyun Song, Xiaokun Luan, Yu Guo, Rongfang Bie, Meng Sun, Xiyue Zhang

  <details><summary>摘要 / Abstract</summary>

  Neural network verification and data privacy are inherently in tension: verification demands full access to model parameters and input data, yet both are increasingly restricted by privacy regulations and intellectual property constraints. This tension has left robustness verification impractical in privacy-sensitive domains. In this work, we address this gap with SecureCROWN, the first framework for privacy-preserving neural network robustness verification. Built upon secure two-party computation (2PC), our framework enables a model owner and a data owner to jointly compute certified robustness bounds -- revealing only the final result while provably protecting both parties&#x27; private data under the semi-honest security model. A key challenge is securely computing the conditional operations in Linear Bound Propagation, where the data-dependent branching is incompatible with standard secure computation protocols. We eliminate branching by formulating conditional logic as continuous arithmetic operations. Additionally, we introduce a Newton--Raphson refinement method to improve numerical stability. Extensive analysis and experiments show that SecureCROWN strictly matches plaintext verification results, while completing in 0.1--200s across varied model sizes and communication settings (LAN/WAN), demonstrating the feasibility of privacy-preserving neural network verification.

  匹配依据：MPC: secure computation, secure two party computation

  </details>

- **PriFT: Private Fine-Tuning using off-the-shelf MPC and HE libraries**
  2026-07-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1381)
  Qiuxuan Ma, Eleftheria Makri, Nusa Zisaric

  <details><summary>摘要 / Abstract</summary>

  Privacy-Preserving Machine Learning (PPML) is a methodology designed to maintain data privacy throughout the machine learning pipeline. Although cryptographically protecting input privacy at the training phase is theoretically feasible, it remains computationally intensive in practice. As such, most recent works in this area focus on the inference phase. In contrast, we consider the training phase. Our goal is to enable machine learning engineers to use customer data earlier in the ML pipeline without compromising customer privacy or violating regulations. In this work, we introduce a framework named PriFT (Private Fine-Tuning), which leverages a transformer as a feature extractor and then performs training of a neural network on privacy-protected features. PriFT supports fully-private training, where the data is encrypted in the entire ML pipeline, as well as semi-private training, which balances privacy and performance by decrypting the true and predicted labels during training. PriFT can perform secure training both by means of Multiparty Computation (MPC) and based on Homomorphic Encryption (HE), which allows for a direct comparison of the two most prevalent cryptographic solutions for secure computation on a real-world use case. The codebase of our experiments is fully open-sourced and based on well-established libraries, namely Crypten and TenSEAL. Our experimental results show that the MPC approach largely outperforms the HE approach, especially in the semi-private setting. Furthermore, the MPC-based solution in the semi-private setting outperforms the fully-private training approximately by 3×, offering an adequate privacy-performance tradeoff. Our results show that both HE and MPC can achieve accuracy close to that of plaintext models.

  匹配依据：MPC: multiparty computation, secure computation

  </details>

- **MPC with Weighted and Fluid Participation**
  2026-07-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1375)
  Ghada Almashaqbeh, Sumedh Ghude

  <details><summary>摘要 / Abstract</summary>

  Most existing multiparty computation (MPC) protocols assume static and equal participation. All computing parties can dedicate resources and stay online for the entire computation, and they have equal influence on computation correctness and security (i.e., they are equally hard to corrupt). Supporting dynamic participation, so parties can join/leave at will, and associating weights to these parties reflecting their trust level, are essential to enable MPC in contemporary emerging applications. Existing solutions addressed these issues separately at varying security levels, and attempting to combine them while addressing malicious security raises several challenges and open questions. In this paper, we close this gap and develop maliciously-secure MPC protocols that support weighted participation in both static and dynamic (or fluid) settings. In particular, we extend prior work on weighted ramp secret sharing (WRSS) to support verifiability and proactivity, which could be of independent interest. Then, we show how to perform arithmetic operations over weighted shares in a verifiable way, thus enabling maliciously-secure weighted MPC with guaranteed output delivery under static participation. Utilizing the proactivity feature of our secret sharing scheme, we develop a state handover protocol and employ it to support dynamic participation in committee-based MPC with the same security guarantees. Both protocols are synchronous and assume honest majority. To the best of our knowledge, our work is the first to support both weighted and dynamic participation in MPC.

  匹配依据：MPC: multiparty computation, secret sharing

  </details>

- **Retrieve-Compute PIR and Its Applications**
  2026-07-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1372)
  Benny Applebaum, Shahar Shechter

  <details><summary>摘要 / Abstract</summary>

  Two-server Private Information Retrieval achieves arbitrarily small polynomial communication, but relies on a strong non-collusion assumption that is difficult to justify in practice. We introduce a new variant of two-server PIR in which one server acts as a standard \emph{compute} server, while the other is a restricted \emph{retrieval-only} server. The latter stores a public encoding of the database and merely serves requested symbols or blocks of this encoding, without performing any PIR-specific computation. We argue that such a retrieval-only server can be instantiated using existing static-content or repository-hosting services, thereby grounding the non-collusion assumption in realistic architectural and deployment constraints. Assuming Learning Parity with Noise (LPN) over the ternary field with inverse-polynomial noise rate, we construct RC-PIR with arbitrarily small polynomial communication and polynomial storage. Leveraging this construction, we derive the following unexpected applications for every constant \(k\): \begin{enumerate} \item \(k\)-server PIR with arbitrarily small polynomial communication and privacy against any coalition of \(k-1\) servers. \item \(k\)-server robust PIR with arbitrarily small polynomial communication that simultaneously achieves correctness and privacy with respect to an arbitrary monotone access structure \(\mathcal{A}\). Namely, correctness is guaranteed whenever the set of online servers \(S\) satisfies \(S \in \mathcal{A}\), while privacy holds against every coalition \(S \notin \mathcal{A}\). \item A \(k\)-party secure computation protocol for size-\(n\) truth tables also known as lookup tables, with arbitrarily small polynomial communication and passive security against any coalition of \(k-1\) parties. This result extends to active security either in the honest-majority setting, or without an honest majority assuming collision-resistant hash functions. \end{enumerate} None of these results were previously known under the LPN assumption. Along the way, we uncover new relationships between different complexity measures of PIR.

  匹配依据：MPC: secure computation

  </details>

- **PSOs as fast as PSI: Efficient Private Set Operations from Batch Homomorphic OKVS Decoding**
  2026-07-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1358)
  Hyun Ji Kwag, Junhyuk Kwon, Changmin Lee, Yongha Son

  <details><summary>摘要 / Abstract</summary>

  Private set operations (PSOs) let two parties compute set-theoretic functionalities on private inputs while revealing nothing beyond the prescribed output. While private set intersection (PSI) has become highly efficient, many other PSOs remain significantly more expensive. The most effective general framework for such tasks is based on reverse private membership test (RPMT), but even state-of-the-art RPMT constructions rely on heavy elliptic-curve-based primitives. In this work, we propose a substantially faster RPMT protocol by replacing the elliptic-curve core with RLWE-based one. Our starting point is the Oblivious Key-Value Store (OKVS) based RPMT framework, whose direct adaptation to RLWE is obstructed by the batching structure of RLWE encryption. To address this, we introduce a batching-friendly variant of OKVS together with a homomorphic batched decoding procedure. We believe that this batching-friendly OKVS and its homomorphic decoding process may be of independent interest. For a set size $2^{20}$, our RPMT-based PSO protocols take only about $3$ seconds over LAN network and $120$-$138$MB communication, whose running time is comparable to state-of-the-art PSI. Compared to state-of-the-art PSI-Cardinality and PSI-Card-SUM, this is up to \(13.0\times\) speedups. Compared to state-of-the-art PSU, this is up to \(3.0\times\) smaller communication while achieving comparable computational cost, which results in up to $3.9\times$ faster running time over WAN.

  匹配依据：MPC: private set intersection

  </details>

- **From Cramer Rule to Lagrange Interpolation**
  2026-07-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1362)
  Zhengjun Cao, Lihua Liu

  <details><summary>摘要 / Abstract</summary>

  Multivariate interpolation arises in a wide range, including computer graphics, multi-secret sharing and secure multiparty computation. But its general representation is rarely discussed. In this note, a general representation for univariate interpolation and multivariate interpolation is formulated, which is helpful for multi-secret sharing illustrations and security arguments. The finding offers a new glimpse into the relation between Cramer rule and Lagrange interpolation formula.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Dead Man’s Switch Cryptography**
  2026-07-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1352)
  Shalini Banerjee, Andrey Bozhko, Raphael Heitjohann, Andy Rupp

  <details><summary>摘要 / Abstract</summary>

  We initiate the formal study of &quot;dead man switch cryptography&quot; — the problem of cryptographically enforcing the fate of a long-lived secret upon the death of its sole keeper — either by releasing it exclusively to designated nominees or by provably destroying it. Despite the natural practical demand, no prior work formalizes this primitive. We identify Dead Man&#x27;s Switch (DMS) as a standalone cryptographic primitive with two modes: release and delete, capturing these dual functionalities. Our abstraction isolates the core conceptual properties of this primitive, and gives its first rigorous treatment in the UC framework. To realize the notion, we introduce Dealer-Controlled Evolving-Committee Proactive Secret Sharing (DC-EPSS), an extension of the Evolving-Committee Proactive Secret Sharing by Benhamouda et al. (TCC &#x27;20). We provide the UC formalization of DC-EPSS and instantiate it generically using the nested YOSO framework of Abraham, Chouatt, Damgard, Gilad, Stern, and Yakoubov. Building on DC-EPSS, we realize DMS-release by coupling it with a multi-recipient authorized recovery mechanism based on a PKI infrastructure, a multi-recipient PKE, a key committing SKE, and NIZK proof systems, while DMS-delete directly follows from DC-EPSS instantiated in the delete mode. We prove the security of both constructions in the UC framework under standard assumptions.

  匹配依据：MPC: secret sharing

  </details>

- **Compressing Correlations via Secret Replication: PCFs from Symmetric Cryptography**
  2026-07-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1355)
  Yuval Ishai, Hugo Krawczyk, Tal Rabin

  <details><summary>摘要 / Abstract</summary>

  We revisit the question of securely compressing multiparty correlations using only symmetric cryptography. A *linear correlation* ${\cal C}$, defined by a linear subspace $C\subseteq \mathbb F^n$, samples a secret random ${\bf c}\in C$ and assigns to each party a fixed subset of the entries of ${\bf c}$. Gilboa and Ishai (Crypto 1999) and Cramer, Damgård and Ishai (TCC 2005) provide a general technique for securely compressing many independent samples from $\cal C$ by replicating independent keys of a pseudorandom function (PRF) among the parties. This implies a *pseudorandom correlation function* (PCF) for $\cal C$ from any PRF, where the PCF key size scales with the number of minimal-support codewords in $C$. We observe that the above generalizes to other types of useful target correlations ${\cal C}_T$ by using a *secret* replication pattern obtained via a random secret assignment of parties in $\cal C$ to parties in ${\cal C}_T$. We present several corollaries of this general blueprint. These include a re-derivation of two-party PCF constructions for VOLE and subfield-VOLE over small domains (Roy, Crypto 2022) as well as new multiparty PCFs for small-domain VOLE-style correlations, including scalar-vector multiplication triples and their authenticated variants. Finally, we discuss applications to secure computation.

  匹配依据：MPC: secure computation

  </details>

- **Reliable Homomorphic Matching for Fuzzy Labeled PSI at Scale**
  2026-06-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.27803) · [IACR ePrint](https://eprint.iacr.org/2026/1322)
  Erkam Uzun

  <details><summary>摘要 / Abstract</summary>

  Fuzzy Labeled Private Set Intersection (FLPSI) lets a receiver learn the labels of enrolled records that are similar to its query, and nothing else. FLPSI can be built in several ways. Constructions based on a set-threshold reduction reach practical performance: a query matches a record when the two agree on a threshold number of components. These constructions delegate the private matching to an inner set-threshold kernel. We study its homomorphic form, which combines leveled-BFV homomorphic encryption (HE), a garbled circuit, and secret sharing to decide the match under encryption and release the record&#x27;s label. We identify a composition gap in this kernel, an instance of a protocol-level problem: efficiency is bought with a per-trial false-accept probability, but one query runs a trial for every record, so the error compounds with the database size into the kernel&#x27;s realization soundness error (RSE), the rate at which it accepts a query the plaintext matcher would reject. The RSE is a reliability property of the cryptographic matching layer, not the matcher&#x27;s accuracy. On a spurious accept the kernel also returns a value the plaintext matcher would never produce. A sound kernel must contribute zero or negligible RSE of its own. We formalize this requirement as a composable security property, give a closed-form bound on the receiver&#x27;s advantage, and close the gap with CSTPSI, a kernel that runs independent token rounds and raises the per-trial bound to a matching power. We prove CSTPSI secure in the semi-honest model. The closed-form bound sets the round count: two token rounds suffice for million-scale databases and three for billion-scale at the $10^{-6}$ engineering threshold. Our evaluation confirms the prediction. At a million records the baseline kernel&#x27;s RSE reaches $100\%$ while CSTPSI holds it at $0$ in every measured configuration. CSTPSI decouples threshold-checking and upload costs from label size. For large labels at small to moderate scale it is more than $20\times$ faster than the baseline kernel, with up to $93\%$ less communication. It converges to the baseline only at the million-scale database size. Our implementation, with a one-command reproducibility harness, is publicly available.

  匹配依据：MPC: garbled circuit, private set intersection, secret sharing

  </details>

- **Quantum Multi-Party Threshold Private Set Intersection with Explicit Cardinality Testing**
  2026-06-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.27996)
  Zixian Gong, Kun Tian, Yi Zhang, Fengxia Liu

  <details><summary>摘要 / Abstract</summary>

  Threshold private set intersection (TPSI) allows parties to reveal their intersection only when its cardinality reaches a prescribed threshold. Existing quantum TPSI protocols typically rely on a third party (TP) to interpret the final results, which deviates from the cardinality-testing paradigm of TPSI. In this paper, we propose a quantum multiparty TPSI protocol with explicit cardinality testing. Our protocol develops a rotation-based quantum construction in which single-photon sequences are sequentially processed through participant-side data rotations, TP--participant masking rotations, and correlated aggregate rotations. This design produces hidden-label measurement vectors: TP can complete the final measurement, but cannot interpret the semantic meaning of the outcomes. Based on these hidden measurements, we further realize the threshold decision through an oblivious linear evaluation (OLE)-based inner product procedure and a lightweight garbled circuit, revealing only \(\mathbf 1[|\bigcap_i X_i|\ge τ]\) before conditional intersection reconstruction. We prove the correctness and security of the proposed protocol, and further validate its feasibility through quantum-circuit simulations implemented on the IBM \textsf{Qiskit} platform.

  匹配依据：MPC: garbled circuit, private set intersection

  </details>

- **On the generic structures of the protocols for quantum auction and quantum summation and their relation**
  2026-06-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.27693)
  Kabir Sandhu, Sandeep Mishra, Anirban Pathak

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (SMC) addresses the problem of jointly computing global functions of private inputs while revealing minimal information about individual data. Two prominent examples of SMC tasks are sealed-bid auction and secure multi-party summation. Existing schemes for quantum auction and quantum summation have largely been developed independently, motivated by distinct applications and employing different computational primitives. In this work, mutual reductions between the two tasks are established for single-item sealed-bid auctions with first-price payment. In one direction, an auction used as a black box computes a secure sum: each party bids a private random key drawn from its input, so the clearing price depends on the inputs only through their sum $S$. The reduction is perfectly private against colluding semi-honest parties and uses $O(S^2\log(1/δ))$ auction rounds, which is optimal, or $O(S\log(1/δ))$ under coherent access. It can be instantiated with an existing auctioneer-free quantum auction after a one-line change to its disjunction subroutine, which as published leaks occupancy counts. In the other direction, summation with randomized inputs yields threshold disjunctions, and a single search over composite keys locates the highest bid and a winner, revealing nothing else. Because each query consumes the bidders&#x27; encodings, a bidder can adapt its effective bid undetected, while a fixed query set restores sealed bidding. Combinatorial auctions and general payment rules lie outside this framework. On a superconducting processor, one instance of each direction is executed, recovering the winner for four-bidder instances with ties and the sum of private inputs from repeated auctions.

  匹配依据：MPC: secure multi party computation

  </details>

- **Productionized Fairness Measurement Under Privacy Constraints**
  2026-06-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.27558)
  Osonde A. Osoba, Yuzi He, Saikrishna Badrinarayanan, Varun Mithal, Sakshi Jain, Natesh S. Pillai

  <details><summary>摘要 / Abstract</summary>

  Fairness measurements in the form of disaggregated evaluations often rely on demographic signals that are legally constrained or culturally sensitive. Race and ethnicity signals are among the more difficult signals to curate and use for this task. This paper presents Privacy-Preserving Probabilistic Race/Ethnicity Estimation (PPRE) as a method for enabling fairness measurements with respect to race/ethnicity for U.S.\ LinkedIn members in a privacy-preserving manner. PPRE applies privacy technologies (specifically: secure two-party computation, differential privacy, and additive homomorphic encryption) on top of two race/ethnicity demographic signal sources (the Bayesian Improved Surname Geocoding estimator and a sparse golden survey set of self-reported demographics) to power a fairness measurement solution with respect to US-based race/ethnicity demographics. We detail its privacy guarantees and demonstrate its application on candidate- and viewer-side fairness measurements. We close with a transferable framework for institutions seeking to implement similar privacy-preserving measurement infrastructure.

  匹配依据：MPC: secure two party computation

  </details>

- **Differentially Private Intermediate Result Resizing for Scalable Secure Multi-Party Analytics**
  2026-06-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1320)
  Long Gu, Gowri R Chandran, Shaza Zeitouni, Thomas Schneider, Zsolt István

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation (MPC) enables collaborative analytics without exposing raw data. Yet, complex data retrieval operations in relational databases (i.e., relational queries) remain limited by scalability bottlenecks: oblivious operators must pad intermediate results to worst-case sizes to prevent information leakage, thereby inflating communication and computation costs. We propose Resizer, a lightweight operator that can be inserted transparently into relational query plans to bound intermediate result sizes while preserving rigorous privacy guarantees. Resizer reduces intermediate results from fully-oblivious to noisy size bounds that satisfy differential privacy (DP). We propose two Resizer variants, shuffle-based and sort-based, and provide a formal analysis of the privacy guarantees and security in the semi-honest model. We evaluate the Resizer variants in the ORQ framework under semi-honest and honest-majority assumptions using TPC-H benchmark queries, demonstrating that Resizer incurs negligible overhead while reducing data volume. In both LAN and WAN settings, complex queries achieve speedups compared with state-of-the-art oblivious baselines, confirming that Resizer reduces the padding bottleneck and enables scalable, privacy-preserving relational analytics.

  匹配依据：MPC: secure multi party computation

  </details>

- **TL++: Accuracy and Privacy Preserving Traversal Learning for Distributed Intelligent Systems**
  2026-06-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.25627)
  Erdenebileg Batbaatar, Young Yoon

  <details><summary>摘要 / Abstract</summary>

  Distributed intelligent systems increasingly need to train across data silos without centralizing raw data. Federated learning keeps data local but can suffer under heterogeneous partitions and requires repeated full-model exchange. Split learning reduces communication through cut-layer activations, but standard protocols generally do not recover centralized mini-batch gradient behavior and may expose activations and gradients in plaintext. We present TL++, a two-mode traversal-learning framework that constructs virtual batches across nodes to recover centralized mini-batch gradient behavior under explicit synchronization assumptions. Base mode exchanges cut-layer activations and gradients rather than full models. Secure mode secret-shares each cut-layer activation and gradient between an orchestrator and a non-colluding helper, preventing either server from observing plaintext cut-layer tensors. This protection is limited to a semi-honest two-server setting; labels and loss-related outputs remain visible to the orchestrator. In the lightweight secure path evaluated here, exactness requires a linear or affine server path, while nonlinear operations require nonlinear MPC or approximation. We formalize TL++, analyze communication and computation costs, and evaluate it against federated and split-learning baselines on CIFAR-10 and BioGPT/PubMedQA using full fine-tuning and LoRA. On CIFAR-10, TL++ base cut 1 and exact secure cut 3 achieve accuracies of 91.41% (SD 0.19) and 90.93% (SD 0.17), respectively, exceeding the strongest measured non-TL++ baseline by more than 12 percentage points. TL++ base cut 1 also reduces per-step communication by 13.1-fold relative to full-model synchronization. PubMedQA results similarly favor TL++. Overall, TL++ approaches centralized-training performance while reducing communication and providing activation-level secret sharing.

  匹配依据：MPC: secret sharing

  </details>

- **General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference**
  2026-06-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.25349)
  Wenshao Yang, Zhenhua Liu, Dongdong Yao

  <details><summary>摘要 / Abstract</summary>

  In secure two-party Transformer inference, linear layers are typically evaluated using Fully Homomorphic Encryption (FHE) through plaintext-ciphertext or ciphertext-ciphertext matrix multiplications, where key switching primarily occurs and dominates computational overhead in both FHE-based and hybrid FHE-MPC systems. Existing optimizations rely heavily on packing-specific algorithms, limiting their general applicability. Targeting this overhead from a packing-independent perspective, we propose a preprocessing-assisted method for secure attention computation. By decomposing attention into precomputable operations and online interactions, this method reduces online inference-phase key switching without modifying existing packing strategies. However, the first method shifting key switching offline introduces additional storage requirements. To address this, we propose storage-communication trade-off techniques that replace large precomputed ciphertexts with modest online communication, enabling flexible deployment under varying resource constraints. While ciphertext-ciphertext matrix multiplication is offloaded to the preprocessing phase in hybrid schemes and the first layer of FHE-based schemes, these operations still persist in the offline stage and subsequent FHE layers. To further optimize it, we propose a fused key-switch technique targeting the multiplication-followed-by-rotation pattern, which frequently arises in existing RNS-CKKS matrix multiplication schemes. By combining relinearization and rotation into a single procedure, this technique reduces the associated computation costs. Analytical evaluations demonstrate that our proposed techniques significantly reduce online key-switch overhead and provide flexible trade-offs between storage and communication without requiring modifications to existing packing strategies.

  匹配依据：MPC: mpc (context)

  </details>

- **Discrepancy for Random Linear Codes**
  2026-06-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.24471)
  Dean Doron, Tal Leonov, Jonathan Mosheiff, Henrique Navas, Nicolas Resch, João Ribeiro

  <details><summary>摘要 / Abstract</summary>

  We show that random linear codes (RLCs) possess nearly optimal discrepancy-type properties in a broad range of settings. Our main results are two general discrepancy theorems: one controls all translates of a fixed test, and the other controls large families of Fourier-pseudorandom tests. Two motivating examples follow: First, RLCs behave essentially like unstructured random codes for list-decoding from errors above capacity. More precisely, an RLC $C\subseteq \mathbb{F}_q^n$ of rate $1 - \frac{1}{n}\log_q|B_ρ| + \varepsilon$, where $|B_ρ|$ is the volume of a radius-$ρ$ Hamming ball in $\mathbb{F}_q^n$, satisfies $|C \cap B| = (1\pm o(1)) \frac{|C|\cdot |B|}{q^n}$ simultaneously for all radius-$ρ$ Hamming balls $B$ with high probability. This vastly generalizes the previously best known fact that RLCs of this rate have covering radius at most $ρn$ with high probability (Blinovsky, 1987). Second, over prime fields, RLCs behave essentially like unstructured random codes for zero-error list-recovery, and list-recovery from erasures, above capacity. More precisely, for a prime $q&gt;2$ and input list size $2\leq \ell\leq q-1$, an RLC $C\subseteq \mathbb{F}_q^n$ of rate $1-\log_q \ell+\varepsilon$ will satisfy $|C \cap S| = (1\pm o(1)) \frac{|C|\cdot \ell^n}{q^n}$ simultaneously for all combinatorial rectangles $S=S_1\times S_2\times\cdots\times S_n$, where $|S_i|=\ell$ for all $i$, with high probability. An analogous result also holds when we can bound $|S_i|$ only for some of the $i$&#x27;s. We use this to show the abundance of locally leakage-resilient $n$-party linear ramp secret sharing schemes with any linear reconstruction threshold and sublinear threshold gap $O(n/\log n)$ over fields of polynomial size $q=Θ(n^γ)$ for a constant $γ\in(0,1/5)$. Prior work was stuck at reconstruction thresholds above $n/2$ for both threshold and ramp schemes.

  匹配依据：MPC: secret sharing

  </details>

- **A Communication-Efficient Local-Verification Framework for Maliciously Secure MPC with a Two-Thirds Honest Majority**
  2026-06-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1307)
  Hanchao Ku, Hikaru Tsuchida, Mingwu Zhang, Takashi Nishide

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation (MPC) is a cryptographic primitive that enables multiple parties to jointly compute a function over their inputs without revealing the inputs. An MPC protocol is required to provide security against adversarial behavior, typically considered in two classic models: the \textit{semi-honest} model, where adversaries follow the protocol but attempt to learn additional information from the transcript, and the \textit{malicious} model, where adversaries may arbitrarily deviate from the protocol. Protocols secure against semi-honest adversaries are often more efficient, but in many real-world applications the stronger guarantee of malicious security is required. In this work, we propose an efficient MPC protocol secure against static malicious adversaries controlling at most $t&lt;n/3$ out of $n$ parties. Our protocol builds on Shamir&#x27;s secret sharing and follows a compiler-based approach: the parties first evaluate the circuit using a semi-honest protocol and then run a verification procedure that enables honest parties to detect cheating except with small statistical error. Our construction injects fresh randomness into the verification procedure to detect cheating even in the presence of incorrect multiplication triples. It also reduces communication overhead by replacing several invocations of multiplication verification with local degree-$2t$ computations and a batched opening, while keeping the local verification cost comparable to or lower than that of prior protocols. We give a concrete instantiation of the compiler and prove that the resulting protocol is secure against malicious adversaries.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Thresholdizing Standardized FALCON Signatures**
  2026-06-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1300)
  Radhika Garg, Daniel Escudero, Antigoni Polychroniadou, Akira Takahashi, Xiao Wang

  <details><summary>摘要 / Abstract</summary>

  Threshold signatures allow a quorum of parties to jointly produce a signature while preventing any smaller subset from doing so. Following NIST&#x27;s post-quantum standardization, designing threshold schemes compatible with the newly selected primitives is a pressing task. In particular, no prior threshold signature scheme produces signatures verifiable under the unmodified FALCON verification algorithm - the NIST-selected post-quantum scheme with the smallest signatures and keys. In this work, we present the first such threshold FALCON signing protocol, establishing its feasibility. Our technical contributions are threefold. First, we adapt the MPC-based discrete Gaussian sampling protocol of Wei et al. [CCS:WYFCW23] to support private centers and standard deviations, as required by FALCON&#x27;s signing process. Second, we carry out a Rényi divergence analysis of the Klein sampler under fixed-point arithmetic, showing that $73$ bits of precision suffice to achieve the same security as the FALCON specification. Third, we design an efficient MPC protocol for the Klein sampler that exploits the fixed trapdoor basis to construct a pseudorandom correlation generator for authenticated VOLE using only two-party DPFs, reducing per-signature communication significantly over standard authenticated triple generation. We implement and benchmark our protocol in two settings: $N$-party signing with all-but-one corruption, and 3-party signing with honest majority, demonstrating that threshold FALCON signing is feasible for applications where compatibility with the FALCON standard is required.

  匹配依据：MPC: mpc (context)

  </details>

- **TRIP: Thresholding in Regression with Input Privacy**
  2026-06-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1302)
  Chrysa Oikonomou, Katerina Sotiraki

  <details><summary>摘要 / Abstract</summary>

  Secure computation allows multiple parties to jointly evaluate a function without leaking their individual inputs. An intrinsic issue with these techniques is that they do not offer any protection against parties which may contribute bad quality or even maliciously crafted data. We introduce TRIP, a protocol which protects against malicious manipulations of the input in secure computation of linear regression tasks. Linear regression is the cornerstone in many machine learning tasks, and hence creating secure protocols for this task is a crucial step towards secure machine learning. Our protocol utilizes a novel combination of techniques from secure computation, robust statistics, and differential privacy. On synthetic data, TRIP recovers the planted ground truth; on real-world datasets, its model remains close to the clean OLS baseline under up to 40\% target corruption. In terms of efficiency, our protocol runs up to $250\times$ faster than an MPC-only baseline for $10^6$ samples. Even in the smallest parameter setting, TRIP is $10\times$ faster than our baseline.

  匹配依据：MPC: secure computation

  </details>

- **An Efficient and Perfect Secret Sharing Scheme on a Class of Non-Maximal Quantum Access Structure**
  2026-06-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.23082)
  Lei Li, Zhi Li

  <details><summary>摘要 / Abstract</summary>

  Quantum secret sharing is one of the core security technologies in the field of quantum communication. Aiming at the problems of high quantum resource consumption and the difficulty in balancing security and efficiency existing in current quantum secret sharing schemes under non-maximal quantum access structure(QAS), this paper focuses on the judgment criteria of non-maximal QAS and the construction methods of efficient and perfect quantum secret sharing schemes on a kind of non-maximal QAS, i.e. hyperstar with three hyperedges. Firstly, we characterizes the forbidden sets and intermediate sets within this non-maximal QAS, and provides a characterization for non-maximal QAS realizable by pure-state encoding. Secondly, the representative element QAS of hyperstar with three hyperedges is defined, which serves as a substructure of this hyperstar QAS, and belongs to non-maximal QAS. Furthermore, we propose a universal, efficient, and perfect quantum secret sharing scheme based on this hyperstar QAS using corresponding classical secret sharing scheme as an auxiliary. By deploying lightweight quantum resources to representative element access structures, the proposed scheme reduces the difficulty in quantum state preparation and distribution, and enhances its security and resource utilization efficiency.

  匹配依据：MPC: secret sharing

  </details>

- **Breaking the $\\Omega(\|C\|\\kappa)$ Barrier on Garbled Circuit Size in the Random Oracle Model**
  2026-06-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1297)
  Junru Li, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  In this paper, we study garbled circuits in the random oracle model against a computationally unbounded adversary with $T$ queries to a (programmable) random oracle. From Yao&#x27;s garbled circuits (SFCS 1986) to Three-Halves (CRYPTO 2021), the garbled circuit size has been reduced from $8|C|(\log T+\kappa)$ bits to $1.5|C|(\log T+\kappa)$ bits for achieving a statistical error of $2^{-\kappa}$, where $|C|$ is the circuit size and $\kappa$ is the statistical security parameter. However, no known result achieves $o(|C|\kappa)$ bits of garbled circuit size by now, and it is widely believed that a garbled circuit must have $\Omega(|C|\kappa)$ bits in the random oracle model. In this work, we present the first garbling scheme that achieves $o(|C|\kappa)$ bits of garbled circuit size in the random oracle model. In particular, for a circuit $C$ of size $|C|$ and depth $D$, the achieved garbled circuit size is $O(|C|\log T+D\kappa^2\log T)$ bits. This breaks the long-standing $\Omega(|C|\kappa)$ barrier on the garbled circuit size. We extend our garbling scheme to a maliciously secure two-party computation protocol with communication of $O(|C|\log T+D(\log T+\kappa)^2\log T+{\sf poly}(\kappa,\log T))$ bits against any $T$-query adversary assuming parallel oblivious transfers and a (programmable) random oracle. The protocol only requires 1 OT round and 3 one-way communication rounds. If only requiring one of the two parties to have output, a similar communication complexity can be achieved for constructing a non-interactive secure computation (NISC) protocol, which only relies on the preprocessing of bit-OT correlations and a random oracle. Compared to a concurrent work on NISC by Ishai et al. (EUROCRYPT 2026) in the same setting, we achieve a better amortized communication cost per gate at the cost of an additional term related to the circuit depth. The NISC protocol with a similar communication cost can also be constructed from a (slightly stronger version of) semi-malicious 2-round OT protocol.

  匹配依据：MPC: garbled circuit, garbled circuits, garbling scheme, secure computation, secure two party computation

  </details>

- **Achieving Guaranteed Output Delivery MPC with Constant Rounds and Linear Communication in Minicrypt**
  2026-06-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1296)
  Junru Li, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  In this work, we study the communication complexity of constant-round MPC with guaranteed output delivery (GOD) in Minicrypt. We construct the first MPC protocol in this setting with linear communication complexity of $O(|C|n\kappa+Dn^3\kappa^3+W_I{\sf poly}(n,\kappa))$ bits under the assumption of a random oracle, where $|C|$ is the circuit size, $D$ is the circuit depth, $W_I$ is the number of input wires, and $\kappa$ is the security parameter. In comparison, the previously best-known construction with linear communication ($O(|C|n)$), presented by Goyal et al. (CRYPTO 2020), requires $O(D+n^2)$ round complexity. When targeting $O(D)$ round complexity, the best-known result by Agarwal et al. (ASIACRYPT 2024) still requires $O(|C|n^3)$ communication complexity. More communication is needed to achieve constant round complexity, even with non-black-box use of the underlying cryptographic primitives.

  匹配依据：MPC: mpc (context)

  </details>

- **Game-Theoretic Framework for Private Data Sharing in Vehicular Networks**
  2026-06-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.22115)
  Yousef AlSaqabi, Yinan Zhou, Faisal Nawab, Bhaskar Krishnamachari

  <details><summary>摘要 / Abstract</summary>

  We present a novel game-theoretic framework designed to enhance privacy and scalability in decentralized vehicular data collection systems. The proposed hybrid architecture comprises vehicles that supply sensor data, independent servers that process data via secure multiparty computation, a coordinator node that manages data flow, and data consumers that set economic incentives. Crucially, our framework ensures that only the data consumer can access the fully aggregated data, preventing individual raw data exposure and significantly reducing privacy risks. By integrating principles of the Stackelberg competition from game theory, our approach dynamically balances privacy and economic incentives, enabling vehicles to make participation decisions based on perceived privacy risks and incentives. We empirically validate our framework using real-world vehicular location data, quantifying privacy risks by evaluating the accuracy with which a potential adversary can reconstruct a vehicle&#x27;s path using only a subset of the shared data. This paper details the development and deployment of a data-trading platform within this framework, introducing a practical and privacy-preserving marketplace for profitable vehicle data sharing. Through experiments and simulations, we evaluate the effectiveness of the system in preserving privacy and explore the dynamics that influence vehicle participation. Our findings highlight the robustness of the proposed framework in preserving privacy while supporting an active data market.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Privacy-Preserving Outsourced Witness Updates for Append-Only RSA Accumulators**
  2026-06-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1283)
  Hongzi He, Qianhong Wu, Bo Qin, Hao Gao, Willy Susilo

  <details><summary>摘要 / Abstract</summary>

  Append-only accumulators are a natural way to realize compact public-state registries, but under high-frequency updates, witness maintenance becomes a severe challenge because each insertion typically invalidates most existing witnesses. This challenge is particularly acute for intermittently online users in anonymous credential systems, who cannot continuously synchronize update information, while directly outsourcing witness updates may make repeated requests linkable. In this paper, we present a privacy-preserving outsourced witness-update protocol for append-only RSA accumulators. The protocol combines witness updates with Linear Integer Secret Sharing (LISS), enabling on-demand, client-stateless witness updates while preserving witness privacy and unlinkability against coalitions of update servers below the threshold, and providing accountability for malicious or malformed server responses. We formalize the system and threat models and analyze the security of the protocol. We further develop server-side optimizations for long catch-up windows and implement the full end-to-end protocol in Rust. Evaluation under multiple threshold settings and offline windows shows that the protocol supports practical one-shot witness updates after long offline periods, with client-side cost remaining independent of the number of missed updates and server-side cost being mainly determined by the catch-up span and the LISS distribution matrix.

  匹配依据：MPC: secret sharing

  </details>

- **Data-Driven Control from Poisoned Data: Fundamental Limitations and Secure DeePC**
  2026-06-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.20301)
  Takumi Shinohara, Henrik Sandberg, Karl Henrik Johansson

  <details><summary>摘要 / Abstract</summary>

  We study a data-driven control problem in the presence of arbitrary data poisoning attacks. We assume that a subset of offline output data is stored in unprotected locations and may be poisoned by an adversary. We first establish fundamental limitations for data-driven control arising from such poisoned data: poisoning attacks are not detected/identified from the dataset alone; unprotected data are non-informative for controller design with worst-case guarantees; and hard constraints on unprotected outputs are not certifiable. Motivated by these limitations and the data-enabled predictive control (DeePC) technique, we propose Secure DeePC, a data-driven control algorithm that is resilient against poisoning attacks. It first runs output-truncated DeePC using only the protected dataset until the online input becomes persistently exciting. It then uses online measurements to reconstruct the partial offline dataset, and finally returns to full-output DeePC. Secure DeePC achieves MPC-equivalent performance in finite time almost surely under certain conditions. Simulation results illustrate the efficacy of the proposed framework against poisoning attacks.

  匹配依据：MPC: mpc (context)

  </details>

- **Secret key-distribution over networks with node-based adversarial errors**
  2026-06-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.19305)
  Reza Sayyari, Michael Langberg

  <details><summary>摘要 / Abstract</summary>

  We study the multiple key-cast problem in network coding under active node-based adversaries. In multiple key-cast, a source generates independent secret keys to be securely and reliably delivered to designated terminal subsets. The network adversary can observe \(\ell_o\) nodes, inject additive or overwrite errors into \(\ell_e\) nodes, and simultaneously observe and corrupt \(\ell_{oe}\) nodes, while having full knowledge of the topology and coding operations. Adversarial models of similar nature, however, where corruption and eavesdropping is done on edges instead of nodes, have seen previous studies in the context of secure multicast network-coding. The work at hand builds on and extends these studies to address the challenges in node-based adversaries in the context of (multiple) key distribution. For single-source networks where every node is d-vertex connected from the source, we show that perfectly secure multiple key-cast under additive and overwrite error models is asymptotically achievable at the key-capacity of \(d-\ell_o-\ell_e-2\ell_{oe}\). We then extend our analysis to networks where only terminal nodes satisfy this connectivity requirement, while intermediate nodes may be only partially connected. For these topologies, we develop coding schemes that achieve secure and reliable multiple key-cast capacities determined by the source vertex-connectivity and additional structural properties of the network. Finally, we show that our results generalize to multi-source settings, ensuring perfect secrecy even if the adversary observes all but one source node, and establish that our constructions apply directly to secure multicast network coding and to network secret-sharing scenarios. As part of our studies, we improve the security guarantee of a central scheme in [Zhang et al., IEEE Trans. Comm., 2023] addressing parallel-edge networks, from weak-security to perfect-security.

  匹配依据：MPC: secret sharing

  </details>

- **On the Round Complexity of Dishonest-Majority MPC**
  2026-06-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1277)
  Ran Cohen, Daniel Collins, Pouyan Forghani, Juan Garay, Vassilis Zikas

  <details><summary>摘要 / Abstract</summary>

  What is the round complexity of $n$-party secure multiparty computation (MPC) over point-to-point networks in the dishonest-majority setting with unanimous or identifiable abort? Despite decades of research, this foundational question remains open. While two-round MPC is achievable given a broadcast channel, and broadcast protocols with expected-constant rounds exist tolerating any constant fraction of corruptions, a naive combination of the two yields MPC with expected $O(\log n)$ rounds. The core obstacle lies in maintaining round efficiency under parallel composition without an honest majority. Moreover, existing lower bounds for standard broadcast do not apply to broadcast with abort, leaving the exact round complexity of this setting unknown. In this work, we systematically investigate the round complexity of MPC over point-to-point networks, providing positive and negative results: - We show that any broadcast protocol (and thus generic MPC) with unanimous abort tolerating super-constant corruptions requires super-constant rounds, ruling out strict-constant-round protocols. - We construct a round-preserving, black-box parallel composition compiler for broadcast with unanimous abort. This yields our main result: Expected-constant-round MPC with unanimous abort in the PKI model against any constant fraction of corruptions, assuming oblivious transfer (OT) and verifiable random functions (VRFs). - Finally, we prove that expected-constant round broadcast (and MPC) with identifiable abort is impossible against $n - o(n)$ corruptions.

  匹配依据：MPC: oblivious transfer, secure multiparty computation

  </details>

- **Giskard : Byzantine Robust and Private Aggregation for Large-Scale Decentralized Learning**
  2026-06-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.19129)
  Ousmane Touat, César Sabater, Mohamed Maouche, Sonia Ben Mokhtar

  <details><summary>摘要 / Abstract</summary>

  In decentralized learning, clients train a machine learning model while keeping their data locally and share their model parameters or gradients with a set of neighbors, making it vulnerable to both privacy attacks and model poisoning attacks. Jointly addressing privacy and Byzantine behavior in decentralized learning is challenging. Indeed, Differential Privacy (DP) applied on the client side is known to increase the variance of honest model updates, which weakens Byzantine-robust aggregation against poisoning attacks. Distributed DP can mitigate this issue by adding noise after aggregation, but implementing it without a trusted curator requires both confidential and Byzantine-resilient computation. Recent work addresses this challenge using secure multi-party computation (MPC) to implement robust aggregation while preserving input confidentiality. However, these solutions scale badly: they either require all-to-all communication between participants or delegate the entire computation to a small subset of parties whose computational and communication cost grows with network size. In this paper, we present Giskard, a scalable protocol for private and Byzantine-robust decentralized aggregation. Giskard organizes $n$ parties into a tree of committees of size $O(\log n)$ and evaluates a differentially private coordinate-wise approximate median via a committee-adapted secure quantile search over the value domain, using MPC within each committee. We assess Giskard both theoretically by proving its security and privacy properties and empirically through extensive experiments involving up to one million participants. Compared to its closest competitors, Giskard reduces per-party communication complexity by close to three orders of magnitude over the closest competitor while exhibiting comparable robustness under up to $n/4$ Byzantine parties.

  匹配依据：MPC: secure multi party computation

  </details>

- **G-Lox: Group-Adaptive, Privacy-Preserving Bridge Distribution with Two-Party Computation**
  2026-06-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.19620)
  Baigang Chen, Nicholas Hopper

  <details><summary>摘要 / Abstract</summary>

  We present G-Lox (group-adaptive Lox), a bridge-distribution system that preserves Lox-style distributor blindness while enabling hidden, stateful group-level adaptation. G-Lox places adaptive assignment logic behind a two-server privacy wall, so no single server learns group identifiers or group-to-bridge assignments. Private state access and state-dependent updates use two-server DPF/FSS protocols and secure two-party computation, supporting blockage reporting, transport-aware reassignment, and privacy-preserving group splitting. We evaluate G-Lox through system measurements and policy simulation. In our C++/EMP implementation over real TCP sockets, private state access has low client-visible overhead: across state sizes up to 2^16, communication remains in the low-KiB range per iteration. At M=1024, the client sends 1,968 bytes, receives 1,280 bytes, and completes an iteration in about 0.25 s. Simulations with group-specific blocking and Sybil enumeration show that G-Lox improves robustness over Lox- and rBridge-like baselines among systems that maintain broad issuance.

  匹配依据：MPC: secure two party computation, two party computation

  </details>

- **Practical End-to-end Fault Attacks on PERK**
  2026-06-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1266)
  Tanguy Stekke, Durba Chatterjee, Lejla Batina

  <details><summary>摘要 / Abstract</summary>

  This paper presents the first practical end-to-end fault injection attacks on the post-quantum signature scheme PERK, based on the MPC-in-the-Head paradigm and relies on GGM tree expansions for efficient randomness generation. While GGM trees reduce memory requirements, they introduce implementation-level deviations from the theoretical model. We show that these implementation choices fundamentally alter the fault surface and enable new attack vectors that are not captured by the original security assumptions. We propose two attacks targeting distinct stages of the GGM tree construction. The first attack fixes the root seed, resulting in deterministic tree generation and enabling full reconstruction of all leaf labels. The second attack induces reuse of GGM roots via an instruction skip, allowing recovery of hidden leaf values across consecutive rounds. Both attacks require only a single fault to recover the secret key. We demonstrate both attacks end-to-end on the pqm4 reference implementation compiled with optimization levels -O3 as well as -Os for ARM Cortex-M4 microcontrollers. Our evaluation is performed on two hardware platforms (ChipWhisperer-Lite with STM32F303 and Nucleo-L4R5ZI-P) using clock glitching and electromagnetic fault injection (EMFI). We achieve success probabilities of 100% and 85% for the two attacks, respectively. Finally, we propose countermeasures for both attacks.

  匹配依据：MPC: mpc (context)

  </details>

- **Efficient Private Set Intersection and Searchable Encryption using Homomorphic Bloom Filters**
  2026-06-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1267)
  Anil Kumar Pradhan, Killari Nandini, Harsh Kasyap, Sayantan Mukherjee

  <details><summary>摘要 / Abstract</summary>

  Existing encrypted search and private set intersection (PSI) protocols struggle to reconcile post-quantum security with practical efficiency, often leaking search and access patterns or requiring prohibitively deep fully homomorphic encryption (FHE) circuits. We address these limitations by introducing a new Homomorphic Bloom Filters (HBF) framework, a quantum-resilient framework that embeds length-$m$ Bloom filters directly into the plaintext space of an RLWE-based FHE scheme, enabling shallow homomorphic evaluation and matching without structural leakage. Building on HBF, we construct a searchable encryption (SE) scheme and a private set intersection (PSI) protocol, both based on a depth-1 homomorphic missing-bit circuit. The SE scheme requires no rotations or bootstrapping at server side and incurs no additional computational cost as the number of query keywords increases. The PSI protocol reduces each packed Bloom-filter comparison to a single ciphertext--plaintext multiplication, with cost depending on the Bloom-filter length rather than direct element-wise comparisons with the responder&#x27;s set. This framework confines leakage to benign dataset dimensions, tunable false-positive rates, and other public metadata, thereby eliminating explicit pattern leakage.

  匹配依据：MPC: private set intersection

  </details>

- **A Billion Hard CRYSTALS: Automated Design Space Exploration of Mixed-Domain Masking for PQC in Hardware**
  2026-06-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1265)
  Fabian Buschkowski, Niklas Höher, Pascal Sasdrich, Tim Güneysu

  <details><summary>摘要 / Abstract</summary>

  Lattice-based post-quantum cryptographic schemes such as ML-KEM or ML-DSA combine bitwise operations, which are most efficiently masked using Boolean secret sharing, with arithmetic operations modulo q, which are cheaper to mask using an additive sharing in the respective field or ring. Previous work has automated the generation of Boolean-masked hardware circuits as well as the design space exploration process, but to the best of our knowledge, no similar generic framework exists for hardware designs requiring mixed masking domains. Such designs pose three additional challenges. First, share-wise arithmetic requires no registers to be secure, leading to long critical paths without deliberate pipelining. Second, the conversions required at domain boundaries increase both complexity and susceptibility to human error. Finally, generation of masking randomness from a traditional PRNG requires post-processing, e.g., via rejection sampling, to achieve uniformity modulo q, which results in a variable output rate. We solve these issues and integrate our scheme-agnostic solutions into the masking and design space exploration framework HADES. An efficient pre-synthesis critical path estimation, which is around 60 times faster than synthesis with traditional timing analysis, enables effective exploration of mixed-domain masked circuits without compromising the maximum clock frequency. Our adapted gadget-based masking procedure tracks masking domains and inserts pipelined conversions at domain boundaries automatically, or lets the template developer place resource-shared conversions manually. Lastly, a Markov-chain model of probabilistic masking randomness generation and buffering yields cost-minimal design configurations that guarantee stall-free masked operation except for a user-defined failure probability. We evaluate our methodology for multiple relevant moduli and implement an arbitrary-order masked ML-KEM decapsulation core as a case study for our open-source framework. Its area-optimized configurations represent, to the best of our knowledge, the most compact reported ML-KEM designs, with 54.1 kGE unmasked and 125.4 kGE at first order using the NanGate45 library. Jointly optimizing for area and critical path yields competitive clock frequencies of 325–429 MHz for at most 31% more area, which is still smaller than all previous designs. Practical side-channel security at both first and second masking order is validated through FPGA-based TVLA measurements of the full decapsulation routine using 10 million traces each.

  匹配依据：MPC: secret sharing

  </details>

- **RondoMPC: Asynchronous MPC with G.O.D. made More Practical**
  2026-06-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1261)
  Xuanji Meng, Zhaoyang Xie, Zhaoxin Yang, Sisi Duan, Aggelos Kiayias

  <details><summary>摘要 / Abstract</summary>

  Asynchronous multi-party computation (AMPC) en- ables a set of mutually distrustful parties to securely compute any joint function on their private inputs under arbitrary network delays. The guaranteed output delivery (i.e., G.O.D.) property is essential for availability, but can be very challenging to achieve in practice. HoneyBadgerMPC (CCS 2019), the first practical AMPC protocol, follows Beaver’s paradigm that generates Beaver triples offline to simplify online computation. One of the underlying building blocks, the random double sharing protocol that generates random double shares, how- ever, implicitly assumes a synchronous network. DumboMPC (Usenix Sec 2025) overcomes the issue by adopting a two-phase workflow where the underlying consensus protocol has to be executed twice, and thus incurs high latency. Velox (CCS 2025) achieves lower latency and weaker cryptographic assumptions at the cost of sacrificing G.O.D. It remains an open question whether there exists a more practical AMPC protocol with the G.O.D. property. In this paper, we present RondoMPC, a practical AMPC protocol with G.O.D. with only one phase of consensus. To achieve this goal, we build a practical asynchronous and complete random double sharing (ACRDS) protocol. Our ACRDS protocol supports batching, so a batch of random double shares can be generated simultaneously. Furthermore, ACRDS supports efficient verification of aggregated secret shares, allowing the random double shares to be used for Beaver triple generation using only one phase of consensus. Our experimentation results show that RondoMPC is highly practical, achieving both higher throughput and lower latency for Beaver triple generation compared to existing protocols.

  匹配依据：MPC: multi party computation

  </details>

- **Construction of codes over a commutative non-unital ring from simplicial complexes and their applications**
  2026-06-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.17300)
  Vidya Sagar, Shikha Patel, Sanjay Kumar Singh

  <details><summary>摘要 / Abstract</summary>

  In this article, we investigate the construction of linear codes over a finite ring $\mathcal{S}$, where $\mathcal{S}$ is taken to be an extension of a commutative non-unital ring $I$ of order $p^2$. Our approach is based on the defining set method. The defining sets considered in this work are derived from general simplicial complexes that may contain multiple maximal elements. We determine the parameters of these codes over $\mathcal{S}$ and study their Gray images. We also study the corresponding subfield-like codes. We show that these Gray image codes and subfield-like codes produce several families of divisible codes. Furthermore, we establish sufficient conditions under which these codes are minimal, optimal, and self-orthogonal. As applications of our results, we obtain several families of projective few-weight codes, and locally recoverable codes with small locality. We also study the minimal access structures of secret-sharing schemes associated with the duals of these minimal codes. Moreover, we construct several families of strongly regular graphs from projective two-weight codes and determine their parameters explicitly.

  匹配依据：MPC: secret sharing

  </details>

- **Collaborative Rate Limiting Nullifier Signaling**
  2026-06-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1259)
  Yağmur Gürel, Uğur Şen, Oğuz Yayla

  <details><summary>摘要 / Abstract</summary>

  Rate Limiting Nullifier (RLN) is a privacy-preserving and decentralized spam-prevention mechanism for anonymous broadcast networks: each member can emit at most $r$ signals per epoch, and any violation reveals a secret that enables the member&#x27;s stake to be slashed. The standard construction binds each membership to a single secret key $\mathsf{sk}_G$, so the unit of identity, the unit of authorization, and the unit of slashing all coincide with one party. This rules out settings in which a group should speak with one voice, share one rate budget, and stand behind one collective bond without any single member being able to act unilaterally. We introduce Collaborative RLN Signaling (coRLN), a protocol that lets $n$ parties register as a single RLN member and signal only by acting jointly. The group secret $\mathsf{sk}_G$ is held as additive shares under SPDZ and never reconstructed; the identity (or rate) commitment, the per-epoch RLN evaluation, and the broadcast proof are produced inside an MPC network using collaborative zk-SNARKs. The group occupies one leaf in the membership Merkle tree, locks one aggregated stake $\mathsf{stake}_G$, and is bound by one rate limit. We present the construction in both the rate-limit-1 and the general $r \geq 1$ settings, and we extend the protocol with a collaborative withdrawal procedure that lets the group exit without ever reconstructing $\mathsf{sk}_G$. We prove three security properties of coRLN by reduction to the collaborative-SNARK composition and the standard primitives underneath: (i) no PPT adversary corrupting up to $n-1$ parties recovers $\mathsf{sk}_G$ as long as one party is honest; (ii) two signals in the same epoch with the same $\mathsf{messageId}$ yield an efficient extractor that recovers $\mathsf{sk}_G$ and triggers forfeiture of $\mathsf{stake}_G$; and (iii) no strict subset of $G$ can produce a verifying signal. The verifier interface and signal shape match classical RLN at the byte level, so coRLN deploys on existing RLN-aware infrastructure with only the verification key updated.

  匹配依据：MPC: mpc (context)

  </details>

- **Fuzzy PSI from Symmetric Primitives with Exact Logarithmic Dependence on Distance Threshold**
  2026-06-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.15093)
  Cong Zhang, Yang Cao, Yujie Bai, Shuaishuai Li, Juntong Lin, Yu Chen, Anyu Wang, Xiaoyun Wang

  <details><summary>摘要 / Abstract</summary>

  Previous FPSI works have demonstrated a linear scaling with the distance threshold $δ$, while some recent works have achieved a poly-logarithmic dependence on $δ$. However, these protocols either support only the $L_\infty$ distance, or they support general $L_{p\in[1,\infty]}$ distances but rely on expensive additive homomorphic encryption (AHE). Achieving exact logarithmic dependence on $δ$ for general $L_{p\in[1,\infty]}$ distances without relying on costly AHE would constitute a theoretical breakthrough in optimal threshold scaling and a practical advance toward scalable FPSI applications. In this work, we present new FPSI protocols for $L_{p\in[1,\infty]}$ distances that are entirely built from oblivious transfer (OT) and symmetric-key primitives. We propose FPSI protocols based on both the apart and the separate assumptions, which are applicable to low- and high-dimensional settings, respectively. Our constructions achieve strictly logarithmic complexity in $δ$, which is optimal in the sense that distinguishing all values in an interval of length $O(δ)$ necessarily requires $Ω(\log δ)$ bits of information. Our core idea is to perform fuzzy matching via prefix representation and interactively determine the correct prefix using equality conditions. To this end, we propose a suite of new components that can be implemented efficiently using only OT and symmetric-key operations. We implement our FPSI protocols and compare them with the state-of-the-art FPSI protocols for $L_{p\in[1,\infty]}$ distance. Experiments show that our protocols outperform the prior state-of-the-art by up to $43.7\times$ in runtime and $31.3\times$ in communication.

  匹配依据：MPC: oblivious transfer

  </details>

- **Accountable Asynchronous Multi-Party Computation**
  2026-06-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1245)
  Pierre Civit, Rachid Guerraoui

  <details><summary>摘要 / Abstract</summary>

  In non-synchronous networks, classic partition arguments imply that any $t\text{-resilient}$ protocol among $n$ parties cannot ensure safety for many meaningful functionalities once the number of corruptions reaches $f \geq n - 2t$. This motivates building in accountability to detect (and deter) safety violations. We present the first accountable asynchronous MPC (AAMPC) protocol that securely evaluates any arithmetic circuit $\mathcal{C}$ (asynchronously computable by a trusted third party). Our protocol: (1) Ensures all target hyperproperties (correctness, privacy, input-independence, and guaranteed output delivery) whenever $f \leq t &lt; n/3$. (2) Provides strong accountability for $f \in (t,\,t_{\mathrm{acc}}]$ with $t_{\mathrm{acc}} &lt; n - t$: either (i) all hypersafety properties continue to hold (without guaranteed output delivery), or (ii) every honest party obtains publicly verifiable evidence implicating at least $n - 2t$ faulty processes. The construction follows the standard offline/online paradigm and assumes only a transparent setup: a bulletin-board public key infrastructure (PKI) and a common random string (CRS). Our main technical contribution is an accountable additively homomorphic high-threshold asynchronous complete (verifiable) secret sharing functionality with amortized linear communication for both sharing and reconstruction. This yields an efficient online phase with $O\big(\mathsf{Depth}(\mathcal{C})\big)$ latency and amortized $O(|\mathcal{C}|n)$ communication. We additionally provide a constant-round offline phase with cubic communication per generated Beaver triple. Our results are formalized and proven in the Accountable Universal Composability (AUC) framework (S&amp;P 2023), an extension of UC designed to support modular analysis of accountability guarantees.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **SING: Improving the Efficiency of MPC Protocol Assignment using Graph Neural Networks**
  2026-06-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1237)
  Jannis Blüml, Moritz Huppert, Nora Khayata, Joachim Schmidt, Thomas Schneider

  <details><summary>摘要 / Abstract</summary>

  Secure Multi-Party Computation (MPC) enables private computation, but has significantly higher overhead than plaintext execution. Hybrid MPC compilers improve concrete efficiency by mapping distinct computation parts to contextually optimal MPC protocols. However, state-of-the-art systems like Silph (Chen et al., S&amp;P’23) depend on deployment-specific cost models that are cumbersome to retune, and compute mappings via brittle heuristics or costly Integer Linear Programming (ILP), limiting scalability and portability across protocols and deployment settings. We present SING, the first machine-learning-based framework for hybrid MPC share assignment. SING leverages Graph Neural Networks (GNNs) for: (1) imitation of Silph’s assignments, accelerating share assignment by up to $76,697\times$ with comparable quality; and (2) cost-driven learning, where we train a GNN cost predictor on synthetic or empirical costs (e.g., runtime or communication), freeze it, and train the share-assigning GNN to minimize predicted costs. The latter supports expressive non-linear cost models, avoiding ILP&#x27;s linearity constraints, and enables retargeting to new protocol suites and deployment settings by re-fitting the predictor. Finally, we release our synthetic benchmark resources, including a dataset of 704 MPC circuits with wide-ranging hybrid assignments.

  匹配依据：MPC: secure multi party computation

  </details>

- **New bounds on private simultaneous quantum message passing**
  2026-06-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.12557) · [IACR ePrint](https://eprint.iacr.org/2026/1236)
  Uma Girish, Alex May, Natalie Parham, Henry Yuen

  <details><summary>摘要 / Abstract</summary>

  In the private simultaneous message (PSM) setting, $k$ players obtain inputs $x_i\in\{0,1\}^n$ and then each send messages to a referee, who should learn $f(x_1,...,x_k)$ but no other information about $(x_1,...,x_k)$. The PSM setting was introduced as a minimal model for secure multiparty computation and has connections to Boolean function complexity. In the quantum setting, PSM has been related to non-local quantum computation (NLQC). The communication and correlation cost of implementing PSM remains poorly understood. Here, we give new upper and lower bounds on the (quantum) PSM model. For lower bounds, we show: 1) Nečiporuk&#x27;s measure lower bounds the entanglement required for $k$-player quantum PSM with perfect correctness. This leads to quadratic lower bounds for explicit functions. 2) The rank of the communication matrix of $f(x_1,x_2)$ lower bounds 2-player quantum PSM with perfect privacy but imperfect correctness. This implies a previously unknown lower bound on classical PSM with imperfect correctness. When allowing quantum communication and shared entanglement, these are the first lower bounds on quantum PSM that make use of the privacy condition. For upper bounds, we show: 1) Letting $s$ be the size of a quantum circuit computing $f$, $d_f$ be the circuit depth, $k$ the number of players, $n$ the number of bits received by each player, and $ε$ a correctness parameter, we obtain $\mathsf{PSM}_k^*(f) \leq (kn +s) \cdot \log^{O(d_f)}(s/ε)$. 2) The square of the Fourier 1 norm of $f$, $\Vert \hat{f}\Vert_1^2$, upper bounds the classical PSM complexity, $\mathsf{PSM}(f)\leq O(\Vert \hat{f} \Vert^2_1)$. In proving the first upper bound, we generalize existing $T$-depth based techniques for NLQC from $2$ to $k\geq 2$ parties, and consider cases where the Clifford layers are restricted to having small light cones.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Secure Computation against $\\mathsf{NC^1}$ Leakage without Secure Hardware**
  2026-06-09 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1217)
  Yuyu Wang

  <details><summary>摘要 / Abstract</summary>

  In this work, we construct (stateful) leakage-resilient circuits (LRCs) secure against bounded-output-length leakage functions computable by \(\mathsf{NC}^1\) circuits under the mild worst-case assumption \(\mathsf{NC}^1 \subsetneq \oplus\mathsf{L}/\mathsf{poly}\), without relying on any leak-free hardware components, thereby resolving the open problem left by Bogdanov, Ishai, and Srinivasan (CRYPTO 2019; Journal of Cryptology, 2021) and Wang (CRYPTO 2025). Concretely, we first construct a leakage-tolerant circuit with succinct setup (sAI-LTC) secure against 2-adaptive \(\mathsf{NC}^1\) leakage, and then generically combine it with a 2-adaptive leakage-resilient composable encoding scheme to obtain the desired LRC. We further give a direct non-black-box instantiation that optimizes the compiled circuit size at the cost of a slightly larger setup, matching the circuit size of Wang&#x27;s construction that relies on leak-free hardware while using a more compact setup. Finally, we show that our sAI-LTC generically implies a fine-grained multi-theorem non-interactive proof system for all \(\mathsf{NP}\), with compact common reference strings, perfect soundness, and multi-theorem zero-knowledge with offline simulation against \(\mathsf{NC}^1\) adversaries.

  匹配依据：MPC: secure computation

  </details>

- **On the Cryptographic Structure Required for Verifying Qubits**
  2026-06-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.05527) · [IACR ePrint](https://eprint.iacr.org/2026/1215)
  James Bartusek, Itay Shalit

  <details><summary>摘要 / Abstract</summary>

  Classically testing for the presence of anti-commuting operators on a quantum device is a critical tool underpinning recent progress in classical verification of quantum computation. While such tests can be based on cryptographic assumptions, known constructions rely on highly structured assumptions, e.g. trapdoor claw-free functions. In this work, we seek to explain this state of affairs by constructing strong cryptography from (certain forms of) classical tests of anti-commutation. In particular, we formulate the notion of a test of non-commutation (ToNC), an interactive protocol between a quantum prover and classical verifier in which the prover&#x27;s final-round response is obtained by measuring one of two binary observables $P_0,P_1$ depending on the verifier&#x27;s challenge bit $c$. We prove that, for a broad range of parameters, ToNC implies classical-communication key agreement (KA), and ToNC combined with one-way functions implies oblivious transfer (OT). Along the way, we develop tools for and provide the first known results on hardness amplification for post-quantum KA and OT, where communication is classical but adversaries may be quantum. In particular, we prove the following results of independent interest. - Post-quantum hard-core measure theorem: For any efficiently sampleable high-min-entropy distribution $D$ over pairs $(x,b)$ such that quantum circuits have advantage at most $δ$ in predicting $b$ from $x$, there exists a sub-distribution $M\preceq D$ of density $(1-δ)$ on which $b$ is nearly optimally quantum-hard to predict. - Post-quantum interactive XOR lemma: Given any classically-interactive protocol, if quantum adversaries have advantage at most $δ$ in guessing a private challenger bit $b$, then two sequential repetitions reduce the advantage for predicting the XOR of the challenger bits $b_1\oplus b_2$ to at most $δ^2+\rm{negl}(λ)$.

  匹配依据：MPC: oblivious transfer

  </details>

- **MPC-Patch-Bench: Security-Aware LLM Code Patch for Multi-Party Computation**
  2026-06-09 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.11416)
  Yukuan Zhang, Mengxin Zheng, Qian Lou

  <details><summary>摘要 / Abstract</summary>

  Repository-level benchmarks for evaluating Large Language Model (LLM) code repair on Secure Multi-Party Computation (MPC) software do not yet exist, and directly transplanting general-purpose benchmarks such as SWE-bench fails on three structural fronts: (i) MPC repositories are dominated by generic Python infrastructure rather than cryptographic logic; (ii) high-value MPC fixes lack the standardized tests rigid extraction pipelines require; and (iii) standard fail-to-pass evaluation is insufficient for code that must also be cryptographically safe. MPC is increasingly deployed for privacy-preserving machine learning, biomedical collaboration, and secure analytics. Existing MPC-specific code-synthesis efforts cover only operator-level or single-framework tasks; evaluating LLM agents on real repository-level MPC repair instead demands MPC-aware data curation and a verifier matched to the security and numerical-fidelity guarantees MPC programs must obey neither of which existing benchmarks provide. We introduce MPC-Patch-Bench, a repository-level benchmark organised around two frameworks. (1)The Data Curation Framework combines a domain-specific curation agent that filters raw pull requests through three cryptographic layers with a human-AI completion engine that synthesizes missing problem statements and Fail-to-Pass/Pass-to-Pass tests, yielding 205 fully verified instances. (2)The MPC Verifier provides dedicated security and numerical-fidelity checks via dynamic differential testing against plaintext oracles and MPC-specific static analysis rules that flag unsafe reveals, insecure arithmetic, and illegal public/private casts. The strongest evaluated LLM functionally resolves only 22.9% of MPC-Patch-Bench tasks; the MPC Verifier further reduces verified resolution to 17.1%, with up to 40% of functionally-passing patches rejected for cryptographic or numerical-fidelity violations.

  匹配依据：MPC: multi party computation, secure multi party computation

  </details>

- **Silentium revisited: Pseudorandom Beaver Triple Expansion**
  2026-06-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1201)
  Vincent Rieder, Enrico Sorbera

  <details><summary>摘要 / Abstract</summary>

  In the line of the SPDZ protocol for secure multi-party computation, the generation of Beaver triples is the most expensive task. Silentium (Rieder, PrivCryp 25) is the implementation of a Pseudorandom Correlation Generator (PCG) for Beaver triples (Boyle et al., Crypto 20). PCGs focus on low-communication costs., e.g. their PCG reduces the communication by one order of magnitude compared to protocols in MP-SPDZ. Silentium is an implementation of their PCG, achieving similar running times than MP-SPDZ. We make three theoretical contributions to Silentium, including an implementation. First, we make a practical proposal how to generate Beaver triples over binary fields F2λ, which extends the previous setting over prime fields. For this, we propose a suitable instantiation of the Number Theoretic Transform. Second, we show how to use the binary triples to construct what we call a Beaver triple expansion scheme, that is we construct a scheme that expands a small batch of Beaver triples into a large batch of Beaver triples, in the sense of recently established oblivious transfer extension schemes. This feature enables an efficient preprocessing stage for the PCG, closing a practical issue of Silentium. Finally, we provide details about the Silentium implementation, by clearing a technical bug in the initial theoretical protocol description.

  匹配依据：MPC: oblivious transfer, secure multi party computation

  </details>

- **Private Information Retrieval: Share Conversions vs. Decoding Polynomials**
  2026-06-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1211)
  Amos Beimel, Or Lasri

  <details><summary>摘要 / Abstract</summary>

  A private information retrieval (PIR) protocol enables a client to retrieve a bit from an $N$ bit database replicated among $k$ servers in such a way that each server learns no information about the retrieved bit. Modern PIR protocols with information-theoretic privacy (Efremenko, SICOMP, 2012; Dvir and Gopi, STOC, 2015; Ghasemi et al., STOC, 25) are based on matching vectors over a composite number $m$. To construct a PIR protocol from the matching vectors, these protocols use a decoding polynomial, a sparse polynomial that returns a non-zero value on 1 and returns zero on a certain set implied by the matching vectors. Beimel et al. (CCC, 2012) abstracted the properties required by the transformation computed by the decoding polynomial, defining the notion of share conversion. In such a conversion, a set of parties is given shares of a secret in one secret-sharing scheme, and each party locally computes a new share (without any communication) such that the new shares are shares in a second secret-sharing scheme of a related secret. Beimel et al. showed that share conversion can replace the decoding polynomial in the PIR protocol of Efremenko and constructed a share conversion from the ring $\mathbb{Z}_6$ to the field $\mathbb{F}_{2^2}$. This share conversion cannot be computed by a decoding polynomial, as decoding polynomials convert shares from a ring $\mathbb{Z}_m$ to a finite field of characteristic $p$ such that $p$ does not divide $m$. Alon et al. (TCC, 2025) simplified and generalized the PIR protocols of Dvir and Gopi and Ghasemi et al., using share conversion; however, in this protocol, the share conversion is from a ring $\mathbb{Z}_m$ to a finite field of characteristic $p$ such that $p$ does not divide $m$. In this paper, we study the power of share conversions. Our main result proves that if there is a $k$-party share conversion from a ring $\mathbb{Z}_m$ to a finite field of characteristic $p$ such that $p$ does not divide $m$, then there is a $k$ sparse decoding polynomial from a ring $\mathbb{Z}_m$ to a finite field of characteristic $p$. This result implies that using share conversion in the protocol of Alon et al. can only improve the communication complexity by a constant factor. In addition, we show that if there is a $k$-party share conversion from a ring $\mathbb{Z}_m$ to a finite field, where $m$ is a product of $r$ distinct primes, then $k\geq r+1$, i.e., the number of servers in the resulting PIR protocols using the appropriate matching vectors is at least $r+1$. A similar result was recently proved by Ghasemi and Kopparty (ITCS 26); our lower bound also applies to the case in which the characteristic of the field divides $m$.

  匹配依据：MPC: secret sharing

  </details>

- **FuseFSS: Efficient Secure LLM Inference with Function Secret Sharing**
  2026-06-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.09551)
  Yuhan Ma, Yong Li, Stefan Schmid

  <details><summary>摘要 / Abstract</summary>

  Two-server secure inference allows a client to query a hosted large language model (LLM) without revealing prompts or embeddings. Recent GPU systems based on function secret sharing (FSS) make linear layers efficient, but fixed-point nonlinearities and helper operations remain a bottleneck because each operator is typically implemented as a bespoke protocol with its own comparisons, wrap-around corrections, and preprocessing material. We present FuseFSS, a compiler that replaces per-operator protocol design with a single compilation pipeline. For each scalar fixed-point operator, a compact specification lists its interval partition, low-degree arithmetic pieces, and required predicate bits. The compiler emits two batched FSS evaluations on the public masked value: one packed comparison that returns all predicate bits, and one vector interval lookup that returns the active coefficients and constants. Compared to the current state-of-the-art FSS-based GPU secure inference, FuseFSS preserves accuracy while achieving a $1.24\times$--$1.50\times$ end-to-end speedup and reducing online communication by $9\%$--$16\%$ on BERT and GPT-style models; preprocessing is also lighter, with $14\%$--$23\%$ lower key-generation time and $20\%$--$24\%$ smaller keys.

  匹配依据：MPC: secret sharing

  </details>

- **Do You Need a Receipt? Anonymous Credential Revocation at Continental Scale via Private Record Certification**
  2026-06-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1189)
  Kasra Edalatnejad, Sebastian Faust, Jonas Hofmann, Philipp-Florens Lehwalder, Thomas Schneider

  <details><summary>摘要 / Abstract</summary>

  A key challenge in digital credential systems is revocation, that is, the ability to revoke credentials post-issuance and verify their status upon presentation. While anonymous credentials enhance privacy over classical credentials (e.g., by providing unlinkability), they complicate revocation. Existing revocation schemes for anonymous credentials often suffer from high client or verifier computation, long delays before revocation takes effect (e.g., epoch-based settings), or require updates to all users with each revocation. We present an efficient, real-time revocation system for anonymous credentials with decentralized revocation authorities based on a novel primitive called Private Record Certification (PRC). PRC enables users to obtain a certificate for a record stored in a server-managed database without the servers learning which record was requested. This primitive is of independent interest, and we construct it by combining techniques from private information retrieval and secure multi-party computation. Our revocation scheme outsources its costs to the revocation authorities and has minimal overhead for clients and verifiers, while ensuring the communication costs are sublinear in the number of credentials for the revocation authorities. We build a prototype and demonstrate that our system achieves sub-second real-time latency at a scale of over 1 billion credentials, with an online operational cost of 2.5$ per server for processing 1 million PRC queries.

  匹配依据：MPC: secure multi party computation

  </details>

- **Fast Bounded-Independence Functions and Their Duals**
  2026-06-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.07009) · [IACR ePrint](https://eprint.iacr.org/2026/1182)
  Martijn Brehm, Yuval Ishai, Nicolas Resch

  <details><summary>摘要 / Abstract</summary>

  We continue the study of fast functions, computable by linear-size circuits, that share useful properties of random functions. Motivated by cryptographic applications, we generalize and improve on previous results in this area, obtaining the following results: - For any constant $t$, we construct a fast $t$-wise independent hash function with algebraic degree $\log_2 t$ (over $\mathbb F_2$), simultaneously optimizing both asymptotic circuit size and degree. - We simplify and improve a recent construction (ITCS 2026) of a family of fast codes with fast duals, both meeting the Gilbert-Varshamov bound. Unlike the previous construction, our construction has negligible failure probability, can accommodate general fields and rates, supports a systematic encoding, and admits fast universal encoders. - We strengthen the above to support stronger random-like properties, such as optimal combinatorial list-decoding. This is achieved by constructing, for any constant $t$, a family of fast linear functions that map any $t$ linearly independent inputs to uniform and statistically independent outputs. Prior to our work, this was only known for $t=1$. We demonstrate the usefulness of the above results to cryptography. This includes the first nontrivial protocols for perfectly secure multiparty computation whose circuit complexity scales linearly with the number of parties, as well as protocols for computing encrypted matrix-vector products with optimal asymptotic circuit complexity.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Provably-Secure NIZKs From Multi-Round Oracle Proofs**
  2026-06-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1167)
  Chaya Ganesh, Mor Weiss

  <details><summary>摘要 / Abstract</summary>

  We study the security of the Fiat-Shamir transformation when applied to multi-round oracle proofs in the standard model, showing that Interactive Oracle Proofs (IOPs) can be transformed via Fiat-Shamir into Non-interactive Zero-knowledge (NIZK) arguments. We obtain our result in two steps. First, we show that instantiating Kilian&#x27;s transformation with an IOP satisfying a mild Zero-Knowledge (ZK) property called semi-Honest-Verifier ZK (semi-HVZK), and a commitment scheme that is extractable and equivocal, yields a ZK argument. We then obtain provably-secure NIZK arguments from our interactive ZK arguments by instantiating Fiat-Shamir with a Correlation-Intractable Hash (CIH) function. The second step involves carefully defining an appropriate &quot;bad relation&quot; for which CIHs are known to exist. Existence of CIH for our bad relation requires the underlying semi-HVZK IOP to have an additional &quot;doom checkability&quot; property which we introduce. Roughly, doom checkability guarantees that one can efficiently check whether a non-empty partial IOP transcript is &quot;doomed&quot; in the sense that it will lead the verifier to reject. We then show that IOPs based on the &quot;MPC in the Head&quot; paradigm are doom checkable. Our results show that the Fiat-Shamir paradigm can be applied to semi-HVZK IOPs to yield provably-secure NIZKs. This extends similar results known for single-round IOPs (i.e., Probabilistically Checkable Proofs) and interactive proofs (IPs), and establishes the soundness of this method. Along the way, we also prove composition theorems for semi-HVZK IOPs, which might be of independent interest, and use them to improve the soundness error of linear-time IOPs and interactive arguments from the literature.

  匹配依据：MPC: mpc (context)

  </details>
