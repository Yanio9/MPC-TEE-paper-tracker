# 2026 · MPC + TEE · 仅预印本来源 · 第 1/1 页

[总目录](../PAPERS.md)

- **Trusted Model Environment for Private Semantic Computations**
  2026-09-24 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2609.30032)
  Vasisht Duddu, Xi He

  <details><summary>摘要 / Abstract</summary>

  A private semantic computation primitive enables parties to privately compute over structured and unstructured data that requires understanding its semantics, context, and relationships. Standard cryptographic primitives (e.g., multiparty computation) do not readily support such computation. Generative models are well suited for such tasks but typically process data in plaintext, while cryptographic private inference remains inefficient and difficult to scale. Thus, we need a new primitive for private semantic computation. We introduce trusted model environments (TME), the first such primitive that executes generative models inside trusted execution environments (TEEs) while controlling output leakage. TME is designed to be (i) effective (correctly performs the semantic task); (ii) confidential (protects computation and sensitive inputs); (iii) utility-preserving (retains utility on other tasks); (iv) verifiable (provides tamper-resistant evidence of the computations); (v) efficient (incurs low overhead compared to baseline model computations); and (vi) scalable (supports multiple participating parties). Effectiveness follows from the generative models, while TEEs provide confidential computation. For confidentiality of sensitive inputs, we combine adversarial training to resist verbatim leakage with an information flow control module to suppress semantic leakage. For verifiability, we introduce novel attestations that let parties verify TME operations on their data and queries, along with optimizations (e.g., batching) for efficiency and scalability. We design and evaluate the proof-of-concept for TME across three applications, showing that it meets all the requirements.

  匹配依据：MPC: multiparty computation; TEE: trusted execution environments

  </details>

- **TEE-Assisted Authenticated MPC for Resource Constrained Edge\_Intelligence**
  2026-08-19 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1733)
  Puyu Wang, Ruidan Su, Zhenshen Liu, Ruiqi Yang, Kai Fan, Hui Li

  <details><summary>摘要 / Abstract</summary>

  Supporting privacy-preserving analytics across large Internet of Things (IoT) populations remains difficult. Resource-constrained devices may be unable to execute expensive multi-party computation (MPC) preprocessing or remain in a sustained many-party online protocol. We present a remotely attested, trusted execution environment (TEE)-assisted authenticated MPC multiplication scheme for large-scale edge intelligence. The TEE is deliberately restricted to the offline phase: before task-time compute committees are selected according to current edge availability and resource conditions, an Intel Software Guard Extensions (SGX) enclave provisions fine-grained authenticated material to authorized edge devices and then leaves the computation path. When a task arrives, a smaller set of $m&lt;n$ compute committees aggregates the delegated device shares, the input owners inject their private data and model parameters through preprocessed masks, and the committees perform authenticated online multiplication without re-entering the TEE. We establish the correctness and authentication invariants of the committee-level computation and analyze the remotely attested deployment under an explicit TEE trust assumption. A hardware-SGX prototype implements the integrated scheme. The prototype generates batches of 10 million triples; at $l=1$ million in the evaluated three-recipient configuration, it achieves a $12.17\times$ preprocessing speedup over the evaluated MP-SPDZ MASCOT baseline. A separate stress test packages one preprocessing row for 100,000 recipients, and integrated tests reject ciphertext and online message-authentication-code (MAC) tampering. These results show that our scheme substantially improves preprocessing performance over the evaluated software-only protocol and is well suited to resource-constrained edge-intelligence deployments, underscoring its strong practical utility.

  匹配依据：MPC: multi party computation; TEE: sgx, sgx enclave, trusted execution environment

  </details>

- **Verifiable SelfMix**
  2026-08-05 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1617)
  Doron Zarchy

  <details><summary>摘要 / Abstract</summary>

  Anonymous communication systems aim to hide which user sent which message, but existing designs sit at two extremes: efficient, centralized mixnets that rely on at least one honest mix server, and fully decentralized protocols such as DC-nets and MPC-based shuffles that avoid trusted mixers at the cost of high communication and fragility under disruption. This paper introduces \emph{verifiable self-mix} (VSM), a new anonymity architecture for privately shuffling messages posted on a public bulletin board. In VSM, users \emph{self-mix} their encrypted messages by writing them to secret locations in a public table. A preprocessing protocol, \emph{Unique Number Selection} (UNS), assigns every user a distinct hidden mix location; an anonymization protocol, \emph{Secure Mapping of Private Permutation} (SMPP), ensures that each such location contains exactly that user&#x27;s ciphertext, without revealing the mapping from users to locations. Because each user learns their own final location, VSM provides \emph{unconditional individual verifiability}: after an optional decryption step, users can check that their message appears at the correct slot without running any cryptographic checks. We formally define VSM and prove anonymity, integrity, and self-verifiability in the malicious model. We then present several concrete instantiations. Our UNS protocols rely on either trusted hardware or multiple servers running plaintext-equivalence tests and require only constant private memory, making them suitable for constrained trusted execution environments. Our SMPP constructions allow trade-offs between trust and bandwidth, achieving $O(n)$ ciphertext uploads per user (or $O(\log n)$ in theory under FHE, at substantial setup cost), while avoiding the pairwise shared-pad state and interactive disruption-resolution typical of classic DC-net designs.

  匹配依据：MPC: mpc (context); TEE: trusted execution environments

  </details>

- **Multi-tenant Kubernetes Use Cases for AI, Secure Computing and Data Services, and More**
  2026-08-01 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2608.00742)
  Jake Watson, Sadaf R Alam, Christopher Woods, Abdelwahab Kawafi, Thomas Green, Ian Johnson, Ellis Pires, Jessica R. Jones, Utz-Uwe Haus

  <details><summary>摘要 / Abstract</summary>

  Kubernetes, as a container orchestration engine, has been widely used in cloud-native ecosystems for several years. In supercomputing ecosystems, especially where bare-metal performance for compute and network devices are considered, the adoption is somewhat limited. However, with the increasing diversity of use cases such as AI, secure and confidential computing for sensitive data, and mixed workload orchestration, a traditional, single-tenant batch computing system does not offer the flexibility and reproducibility to which public cloud users are accustomed. Note that Kubernetes is not considered a replacement for batch scheduling systems, which have powerful features for large-scale MPI jobs with thousands of network end points. Rather, it is a complementary service provided as part of a national AI Research Resource. We evaluate Kubernetes deployment on a Hewlett Packard Enterprise (HPE) Cray EX supercomputerwith HPE Slingshot interconnect, called Isambard-AI, with co-design use cases. One is a Trusted Research Environment used for medical and health sciences. The other combines KubeRay, Ray, and vLLM to provide a distributed, sandboxed, persistent AI model hosting service targeting multi-tenant confidential computing. We discuss challenges and lessons learned, and where further development is needed to offer a production Kubernetes-as-a-Service on HPE Cray EX (and later) platforms.

  匹配依据：MPC: secure computing; TEE: confidential computing

  </details>

- **SoK: Confidential Transformer Inference and Retrieval-Augmented Generation**
  2026-07-28 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1544)
  Timofey Yaluhin

  <details><summary>摘要 / Abstract</summary>

  Running Transformer inference and retrieval-augmented generation (RAG) over confidential data forces a choice: either expose prompts and documents to a cloud operator, or keep the data on-premises, which confines the deployment to weaker self-hosted models. Existing defenses span five mechanism families: secure computation (MPC and FHE), trusted execution environments (TEEs), static obfuscation, differential privacy, and hybrid TEE-and-obfuscation splits. No prior systematization compares them on a common footing of mechanism, threat model, and deployment cost, and none covers the RAG retrieval layer. We organize the field by deployment readiness: the likelihood a scheme is adopted in practice, scored on performance, utility, and threat-model fit. The scoring spans inference and RAG retrieval, both dense and graph. We find that no family dominates: each attains at most two of the three criteria, and which one it sacrifices is fixed by its security basis, so the deployable choice is set by the constraint an application can least afford to relax. Even trusted hardware is no exception, since every surveyed scheme ignores the side channels to which it is most exposed. We further surface hidden deployment costs, such as client reliance and a custom serving path, identify private graph-RAG as the least-served setting, and find that no design yet keeps a pipeline confidential from query to answer.

  匹配依据：MPC: secure computation; TEE: trusted execution environments

  </details>

- **Encifher: A Trusted-Execution Coprocessor for Confidential Computation on Solana**
  2026-07-23 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1504)
  Nitanshu Lokhande, Rishabh Gupta, Rachit Chahar, Arun Jangra, Aniket Prajapati, Muskan Kumari

  <details><summary>摘要 / Abstract</summary>

  Public blockchains expose all state and computation by default, which is incompatible with financial applications that require confidentiality. Solana achieves high throughput and sub-second confirmation, making it an attractive settlement layer, yet it oﬀers no general mechanism for computing over encrypted state: fully homomorphic encryption (FHE) remains orders of magnitude too slow for interactive use, secure multi-party computation (MPC) incurs heavy communication, and Solana’s native confidential-transfer extension hides only token amounts and supports no programmable logic. We present Encifher, a confidentiality coprocessor for Solana that brings general, programmable computation over encrypted state to a high-throughput chain. Encifher adopts the ciphertext-handle and symbolic-execution interface of confidential-computing coprocessors (e.g., Zama’s fhEVM), but resolves it inside a Trusted Execution Environment (TEE) rather than with a fully homomorphic evaluator: on-chain Solana programs manipulate only 128-bit handles to ciphertexts, while an oﬀ-chain coprocessor running inside a hardware enclave fetches the corresponding ciphertexts from a public data availability layer, decrypts and computes on plaintext within the enclave, re-encrypts, and commits attested, Merkle-anchored results back on chain. A key observation is that Solana’s account model and parallel (Sealevel) scheduler turn the transaction’s declared read/write set into the dependency graph of the confidential computation, yielding parallel, correctly-ordered execution of encrypted operations without a bespoke scheduler. To avoid the single-point-of-failure of an enclave holding a master decryption key, Encifher distributes trust across a threshold-decryption committee and verifies enclave attestation on chain. Encifher is deployed in production, powering confidential payments, swaps, and a cross-chain bridge. In production, a confidential swap settles in a single Solana transaction costing 157,000 compute units; the AES-256-GCM symmetric-encryption layer runs at over a million operations per second and threshold decryption completes in single-digit to tens of milliseconds (near-plaintext speed, against the many-orders-of-magnitude overhead of FHE), and Encifher has served over 5,000 users and 50,000 confidential operations. We are explicit about the cost of this design point: Encifher reduces the trust base to TEE integrity, honest threshold key management, and the cloud attestation root, rather than to cryptographic hardness alone.

  匹配依据：MPC: secure multi party computation; TEE: confidential computing, hardware enclave, trusted execution environment

  </details>

- **SENTRA:Privacy-Preserving Training in Outsourced Cloud Environments**
  2026-07-15 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1443)
  Maryam Zarezadeh, Jana Eisoldt, Bhavish Mohee, Stefan Köpsell, Behzad Abdolmaleki

  <details><summary>摘要 / Abstract</summary>

  Training machine learning models in untrusted clouds requires strong guarantees of confidentiality, integrity, and correctness, while remaining scalable and resilient to node churn. These challenges are further amplified in emerging agentic AI systems, where autonomous and distributed learning components require trustworthy coordination and secure state management across heterogeneous cloud environments. Existing Trusted Execution Environments (TEEs) lack scalability and remain vulnerable to side-channel attacks for large workloads, while pure secure multi-party computation (MPC) approaches incur prohibitive overhead in practice. SENTRA (Secure ENclave-based TRaining Architecture) addresses these challenges through a hybrid architecture that combines TEEs, secret sharing, and communication-efficient MPC with system level mechanisms that secure the entire training lifecycle. SENTRA introduces a scalable collective attestation protocol that verifies all participating enclaves and enforces hardware exclusivity before any node may store or process secret shares. Training data and model parameters are stored as secret shares in a versioned enclave-backed key–value store (KVS), providing rollback protection and consistent state under adversarial conditions. SENTRA further supports dynamic, fault tolerant membership through Dynamic Proactive Secret Sharing (DPSS)-based resharing, safe packed-MPC computation under degree bounds, and adaptive handling of node failures. Evaluation of a prototype implementation shows that SENTRA achieves up to 8.89 samples/s throughput and 1.29× faster training than the CrypTen baseline in software-only mode. In hardware-enclave mode, SENTRA incurs only an 8.3% performance overhead while providing memory-isolated confidentiality, fault-tolerant membership management, rollback protection, and recovery from node failures in approximately 8 seconds.

  匹配依据：MPC: secret sharing, secure multi party computation; TEE: hardware enclave, secure enclave, trusted execution environments

  </details>

- **Key-Recovery Attacks on TALUS: A Cryptanalytic Note**
  2026-07-07 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1386)
  Guilhem Niot

  <details><summary>摘要 / Abstract</summary>

  We present key-recovery attacks on the constructions of TALUS (Kao and Chang), a threshold ML-DSA (FIPS 204) construction available on arXiv and scheduled for presentation at the NIST Threshold Call Preview Talks Round 2 (TCPT-2, https://csrc.nist.gov/events/2026/tcpt). For TALUS-MPC, which is claimed EUF-CMA secure against an adversary corrupting up to $T − 1$ parties, we show the claim is false via two independent attacks, both exploiting the same root cause. TALUS-MPC uses Feldman commitments that apply the public matrix A to secret values: key shares of $s_1$ during key generation, and contributions to the nonce $y$ during signing. Since A is left-invertible in every ML-DSA parameter set, these images are invertible by Gaussian elimination, with no lattice problem to solve. A passive observer recovers all key shares of $s_1$ directly from the key-generation broadcast, and independently recovers the aggregate nonce y from the signing broadcast, which then yields $s_1 = c^{−1} \cdot (z − y)$ from a single signature. For TALUS-TEE and TALUS-MPC, we identify a persisting flaw: the rejection-sampling check that protects the error term $s_2$ in standard ML-DSA has been removed. Each signature leaks a noisy linear equation in $s_2$; applying least-squares recovery over the cyclotomic ring - an instance of LWE without modular reduction - recovers the full secret from a few hundred million signatures. The sample counts we derive are not optimized and we believe exploiting the bounded noise structure and lattice-reduction techniques would reduce them significantly, but we focus on establishing the structural flaw.

  匹配依据：MPC: mpc (context); TEE: tee (context)

  </details>

- **Two-Way Confidential VMs (2cVM): Collaborative Confidential Computing for Mutually Distrustful Parties**
  2026-06-09 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.10615)
  Jordi Thijsman, Merlijn Sebrechts, Stefan Lefever, Filip De Turck, Bruno Volckaert

  <details><summary>摘要 / Abstract</summary>

  Collaborative computation across organizations is often constrained by the need to process sensitive data and proprietary code without exposing them to untrusted infrastructure or participants. Cryptographic approaches such as fully homomorphic encryption and secure multi-party computation provide strong confidentiality but remain impractical for general workloads due to their extreme computational cost. We present the Two-Way Confidential Virtual Machine (2cVM), a two-layer architecture that pairs a hardware trusted execution environment with an intra-workload isolation layer. Unlike regular Confidential Virtual Machines, 2cVM enforces mutual isolation between co-resident workloads, ensuring that participants retain control over their data and code. All computation in 2cVM is governed by a Commitment Manifest that enumerates participants, component composition, permitted data channels, and authorized outputs; the manifest is locked to the VM and incorporated into attestation evidence, making the policy immutable and independently verifiable throughout the VM&#x27;s lifetime. A proof-of-concept realization combines AMD SEV-SNP for hardware protection with the WebAssembly Component Model for fine-grained sandboxing of participant code. Evaluation on commodity hardware across four benchmark classes shows that the two isolation layers do not accumulate linearly: once a workload executes inside the WebAssembly sandbox, the marginal cost of enabling hardware memory protection is small. Overhead is workload-dependent, governed primarily by memory access pattern, ranging from negligible for sequential workloads to approximately 2x for irregular, pointer-chasing access patterns. These results indicate that 2cVM provides a practical and verifiable foundation for privacy-preserving collaborative computation.

  匹配依据：MPC: secure multi party computation; TEE: amd sev, confidential computing, trusted execution environment

  </details>

- **TeeDAO: A Decentralized Autonomous Organization for Heterogeneous TEEs**
  2026-06-03 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.04912)
  Pinshen Xu, Wentao Dong, Guoxing Chen, Jianyu Niu, Cong Wang, Yinqian Zhang

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) have emerged as a critical technology for safeguarding sensitive data and ensuring code integrity in modern computing systems. However, relying on a single TEE implementation makes systems vulnerable to a central point of attack. Building distributed-trust systems leveraging heterogeneous TEEs helps disperse trust but still faces threats from centralized management and adaptive mobile adversaries. To address these challenges, this paper introduces TeeDAO, a novel three-layer framework that automatically organizes multiple heterogeneous TEE instances and provides unified interfaces to support diverse applications, while ensuring long-term guarantees of availability, integrity, and confidentiality. TeeDAO couples BFT-ordered governance with heterogeneity-aware Distributed Proactive Secret Sharing (DPSS) and Secure Multi-Party Computation (MPC) so that attestation-driven committee changes are consistently reflected in secret recovery, resharing, and computation across a dynamic committee of heterogeneous TEEs. We implement a prototype of TeeDAO, integrating COBRA&#x27;s DPSS scheme with the HotStuff BFT consensus protocol, and adapt it for Intel SGX, TDX, and Hygon CSV. Evaluations demonstrate that TeeDAO achieves up to 1.8x higher key-value store throughput in a large cluster with 61 nodes compared to state-of-the-art systems, efficient autonomous management, and minimal computation overhead (&lt;18%) for multi-party computation tasks.

  匹配依据：MPC: multi party computation, secret sharing, secure multi party computation; TEE: intel sgx, trusted execution environments

  </details>

- **More from Less: Composable General Multi-Party Computation with Global Public Verifiability from a Single Enclave Only**
  2026-05-20 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/1005)
  Saskia Bayreuther, Robin Berger, Felix Dörre, Eva Hetzel, Yufan Jiang, Christian Martin, Jeremias Mechler, Jörn Müller-Quade

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs), also known as secure enclaves, such as Intel SGX, Intel TDX or AMD SEV are seeing widespread use to perform computations on highly sensitive data. To analyze the security of cryptographic protocols using TEEs, several formal models exist, notably the one by Pass et al. (EUROCRYPT 2017) for attested computations in the Generalized UC framework. Using this model and the proposed global ideal functionality $\mathcal{G}_{\mathrm{att}}^{\mathrm{PST}}$, provably secure multi-party computations with practical efficiency are possible. Attested computations are achieved by having enclave outputs signed with a key pair held by $\mathcal{G}_{\mathrm{att}}^{\mathrm{PST}}$, together with the enclave&#x27;s code. Being a global functionality, the verification key can be obtained by any party. Perhaps surprisingly, this model does not give rise to a meaningful notion of public verifiability, i. e. the ability of external parties to plausibly verify results, even though some commercially available enclaves allow exactly that. We formalize this intuition in the form of an impossibility result and propose a novel simulation technique where equivocation is not handled by the simulator resp. adversary anymore, but in a coordinated effort between our new functionality $\mathcal{G}_{\mathrm{att}}$ and a (local) ideal functionality $\mathcal{F}$ that is realized with public verifiability. To this end, several technical problems need to be solved, in particular to ensure that this new mechanism cannot be abused. While unconventional, this approach is, to the best of our knowledge, the first to achieve a general variant of public verifiability a) even when all protocol parties are corrupted and $\mathcal{F}$ is probabilistic and b) where guarantees of honest (external) verifiers are not affected by simulation at all. We call the latter property global public verifiability. We also address a second impossibility result of Pass et al., namely the requirement that every protocol party needs a TEE (even in a setting without public verifiability), unless an additional (global) setup is used. We address this impossibility result by introducing designated-verifier attestations that are only valid for a single party in a single protocol execution, akin to what is possible with real-world enclaves. Using our improved model, we propose protocols for (globally publicly verifiable) composable general MPC and prove their security under the notion of Universal Composition with Global Subroutines (Badertscher et al., TCC 2020) and static malicious corruptions.

  匹配依据：MPC: multi party computation; TEE: amd sev, intel sgx, intel tdx, secure enclaves, trusted execution environments

  </details>

- **CHRONOS: A Hardware-Assisted Phase-Decoupled Framework for Secure Federated Learning in IoT**
  2026-04-21 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.19053)
  Hung Dang

  <details><summary>摘要 / Abstract</summary>

  Federated learning enables collaborative training on IoT gateways without sharing raw data, yet gradients remain susceptible to inversion attacks. Existing Secure Multiparty Computation defenses impose prohibitive communication overhead, exceeding strict IoT latency and energy budgets. We propose CHRONOS, a hardware-assisted framework that decouples cryptographic setup from active training. During idle windows, CHRONOS executes a once-per-epoch server-relayed Diffie-Hellman exchange within an ARM TrustZone enclave, sealing shared secrets and distributing Shamir shares to peers. During training, clients mask gradients via a single stream-cipher evaluation and transmit in one round; a hardware-backed counter enforces mask freshness. If clients drop mid-round, the server reconstructs masks from peer-held shares (k x 32 bytes/client), preserving aggregation without round repetition. Evaluation on a 32-node heterogeneous testbed (Rock Pi 4 and Orange Pi 5) shows that CHRONOS reduces active-phase latency by up to 74\% over synchronous secure aggregation. It mitigates gradient inversion while maintaining a persistent Secure World footprint under 1.1 KB, independent of model dimension and training horizon.

  匹配依据：MPC: secure multiparty computation; TEE: trustzone

  </details>

- **SPoCK: Sequential Proofs of Complete Knowledge**
  2026-04-15 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/738)
  Antonio Giulio D'Antona, Charlotte Hoffmann, Krzysztof Pietrzak

  <details><summary>摘要 / Abstract</summary>

  A proof of knowledge certifies that the prover “knows” a secret. This property is established by the existence of an extractor that, given access to the prover, can extract the secret. Unfortunately, this does not imply that a single entity has access to the secret in the clear, as it may be secret-shared among several parties and the proof computed using multiparty computation (MPC), or the secret may be embedded in a trusted execution environment (TEE) that only allows limited access to it. Often, the ability to encumber a secret in this way breaks the security of a system; vote selling in e-voting schemes is one example. To address this, two recent papers introduced the notions of “Proofs of Complete Knowledge” (PoCK) [Kelkar et al., CCS’24] and “Individual Cryptography” [Dziembowski et al., CRYPTO’23]. While the goals and constructions in those works differ, both rely on the same key idea to prevent encumbrance. To compute a proof, the prover must evaluate a hash function on a huge number of inputs. One then assumes that only a fraction of those can be encumbered, while for the rest the prover must know the inputs in the clear, and these clear inputs are sufficient to extract the secret. Computing a huge number of hashes is a challenge even for an honest prover (who has the secret in the clear), so those works suggest using outdated Bitcoin mining hardware to make the scheme practical. By forcing the prover to evaluate the hashes in a sequential manner, we could get meaningful security against encumbrance with far fewer hashes, especially against MPC, where round complexity is a major bottleneck. As a concrete instantiation of this idea, we define and construct Sequential Proofs of Complete Knowledge (SPoCK). Our construction uses the PoCK of Kelkar et al. (which are based on Fischlin’s straight-line extractable proofs of knowledge). The computation of this PoCK is then embedded into the computation of the Proof of Sequential Work from [Cohen&amp;Pietrzak, EUROCRYPT’18]. SPoCK thus have the potential to enable complete-knowledge or individual-cryptography primitives where honest parties can use standard hardware. We also propose a variant of this scheme that requires a large amount of memory throughout the evaluation, providing better security also against TEEs.

  匹配依据：MPC: multiparty computation; TEE: trusted execution environment

  </details>

- **LLM-Redactor: An Empirical Evaluation of Eight Techniques for Privacy-Preserving LLM Requests**
  2026-04-13 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.12064) · [Code](https://github.com/jayluxferro/llm-redactor)
  Justice Owusu Agyemang, Jerry John Kponyo, Elliot Amponsah, Godfred Manu Addo Boakye, Kwame Opuni-Boachie Obour Agyekum

  <details><summary>摘要 / Abstract</summary>

  Coding agents and LLM-powered applications routinely send potentially sensitive content to cloud LLM APIs where it may be logged, retained, used for training, or subpoenaed. Existing privacy tooling focuses on network-level encryption and organization-level DLP, neither of which addresses the content of prompts themselves. We present a systematic empirical evaluation of eight techniques for privacy-preserving LLM requests: (A) local-only inference, (B) redaction with placeholder restoration, (C) semantic rephrasing, (D) Trusted Execution Environment hosted inference, (E) split inference, (F) fully homomorphic encryption, (G) secret sharing via multi-party computation, and (H) differential-privacy noise. We implement all eight (or a tractable research-stage subset where deployment is not yet feasible) in an open-source shim compatible with MCP and any OpenAI-compatible API. We evaluate the four practical options (A, B, C, H) and their combinations across four workload classes using a ground-truth-labelled leak benchmark of 1,300 samples with 4,014 annotations. Our headline finding is that no single technique dominates: the combination A+B+C (route locally when possible, redact and rephrase the rest) achieves 0.6% combined leak on PII and 31.3% on proprietary code, with zero exact leaks on PII across 500 samples. We present a decision rule that selects the appropriate option(s) from a threat-model budget and workload characterisation. Code, benchmarks, and evaluation harness are released at https://github.com/jayluxferro/llm-redactor.

  匹配依据：MPC: multi party computation, secret sharing; TEE: trusted execution environment

  </details>

- **TAMI-MPC:Trusted Acceleration of Minimal-Interaction MPC for Efficient Nonlinear Inference**
  2026-03-25 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.24861)
  Zhuoran Li, Hanieh Totonchi Asl, Yifei Cai, Ebrahim Nouri, Danella Zhao

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) offers a practical foundation for privacy-preserving machine learning at the edge. However, current MPC systems rely heavily on communication and computation-intensive primitives-such as secure comparison for nonlinear inference, which are often impractical on resource-constrained platforms. To enable real-time inference under a resource-constrained platform, we introduce a Trusted Acceleration of Minimal-Interaction MPC framework, TAMI-MPC, for nonlinear evaluation. Specifically, we reduce communication cost by redesigning the core primitives, leaf comparison, and tree merge, reducing the interactive round from log(n) to just 1 per operation. Furthermore, unlike prior work that heavily relies on oblivious transfer (OT), a well-known computational bottleneck, we leverage synchronized seeds inside the TEE to eliminate OT for the vast majority of our designs, along with a correlated-randomness reuse technique that keeps new designs computationally lightweight. To fully realize the potential, we design a specialized accelerator that restructures the dataflow across stages to enable continuous, fine-grained streaming and high parallelism, reducing memory overhead. Our design achieves up to 4.86x speedup on ResNet-50 inference, compared with state-of-the-art CNN frameworks, and achieves up to 7.44x speedup on BERT-base inference, compared with state-of-the-art LLM frameworks.

  匹配依据：MPC: oblivious transfer, secure multi party computation; TEE: tee (context)

  </details>

- **Human-Extractable ZK Proofs of Knowledge: A Solution to Dark DAOs**
  2026-03-13 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/511)
  Zeyuan Yin, Leiyuan Tian, Bingsheng Zhang, Kui Ren

  <details><summary>摘要 / Abstract</summary>

  A Decentralized Autonomous Organization (DAO) is a pioneering evolution to realize a decentralized democratic governance over a blockchain. In a DAO, stakeholders usually make collective decisions through secure on-chain voting. Recently, Dark DAO (Austgen et al., arXiv:2311.03530) was proposed as a decentralized cartel that enables automated vote-buying. It attacks the inalienable authentication of a remote e-voting system by leveraging key encumbrance via MPC or TEEs, enabling a voter to pass the authentication without knowing the actual key. To defend against this new type of attack, the notions of individual knowledge (Dziembowski et al., CRYPTO &#x27;23) and complete knowledge (Kelkar et al., CCS &#x27;24) were proposed, ensuring that the prover has unencumbered knowledge of a secret. However, their solutions rely on TEEs or ASICs, which are difficult to deploy on blockchain. Inspired by the human-extractable CAPTCHA puzzles proposed by Kumarasubramanian et al. (PKC &#x27;13), we propose a new primitive called human-extractable zero-knowledge proofs of knowledge (HE-ZKPoK) as an alternative solution to Dark DAOs. Our HE-ZKPoK protocol forces the prover to solve human-extractable CAPTCHA puzzles along with completing a standard zero-knowledge proof of knowledge, avoiding the need for specialized hardware. As a result, any human entity can extract the witness merely by looking at the prover&#x27;s CAPTCHA queries and the associated puzzles. With this property, we conclude that if a voter sells his vote, his secret key will be fully exposed, thus deterring voters from engaging in vote-buying.

  匹配依据：MPC: mpc (context); TEE: tees (context)

  </details>

- **UC-Secure Star DKG for Non-Exportable Key Shares with VSS-Free Enforcement**
  2026-02-25 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.22187)
  Vipin Singh Sehrawat

  <details><summary>摘要 / Abstract</summary>

  Distributed Key Generation (DKG) lets parties derive a common public key while keeping the signing key secret-shared. UC-secure DKG requires a verifiable-sharing enforcement layer -- classically satisfied via Verifiable Secret Sharing (VSS) and/or commitment-and-proof mechanisms -- for secrecy, uniqueness, and affine consistency. We target the Non-eXportable Key (NXK) setting enforced by hardware-backed key-isolation modules (e.g., TEEs, HSM-like APIs), formalized via an ideal KeyBox (keystore) functionality $\mathcal{F}_{KeyBox}$ that keeps shares non-exportable and permits only attested KeyBox-to-KeyBox sealing. With confidentiality delegated to the NXK boundary, the remaining challenge is enforcing transcript-defined affine consistency without exporting or resharing shares. State continuity rules out rewinding-based extraction, mandating straight-line techniques. We combine (i) KeyBox confidentiality; (ii) Unique Structure Verification (USV), a publicly verifiable certificate whose certified scalar never leaves the KeyBox yet whose public group element is transcript-derivable; and (iii) Fischlin-based UC-extractable NIZK arguments of knowledge in a gRO-CRP (global Random Oracle with Context-Restricted Programmability) model. We construct Star DKG (SDKG), a UC-secure scheme for multi-device threshold wallets where a designated service must co-sign but cannot sign alone, realizing a 1+1-out-of-$n$ star access structure (center plus any leaf) over roles (primary vs. recovery) with role-based device registration. In the $\mathcal{F}_{KeyBox}$-hybrid and gRO-CRP models, under DL and DDH assumptions with adaptive corruptions and secure erasures, SDKG UC-realizes a transcript-driven refinement of the standard UC-DKG functionality. Over a prime-order group of size $p$, SDKG incurs $\widetilde{O}(n\log p)$ communication overhead and $\widetilde{O}(n\log^{2.585}p)$ bit-operation cost.

  匹配依据：MPC: secret sharing; TEE: tees (context)

  </details>

- **TeeMAF: A TEE-Based Mutual Attestation Framework for On-Chain and Off-Chain Functions in Blockchain DApps**
  2026-01-12 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.07726)
  Xiangyu Liu, Brian Lee, Yuansong Qiao

  <details><summary>摘要 / Abstract</summary>

  The rapid development of Internet of Things (IoT) technology has led to growing concerns about data security and user privacy in the interactions within distributed systems. Decentralized Applications (DApps) in distributed systems consist of on-chain and off-chain functions, where on-chain functions are smart contracts running in the blockchain network, while off-chain functions operate outside the blockchain. Since smart contracts cannot access off-chain information, they cannot verify whether the off-chain functions, i.e. the software components, they interact with have been tampered or not. As a result, establishing mutual trust between the on-chain smart contracts and the off-chain functions remains a significant challenge. To address the challenge, this paper introduces TeeMAF, a generic framework for mutual attestation between on-chain and off-chain functions, leveraging Trusted Execution Environments (TEE), specifically Intel Software Guard Extensions (SGX), SCONE (a TEE container on top of Intel SGX), and remote attestation technologies. This ensures that the deployed off-chain functions of a DApp execute in a provably secure computing environment and achieve mutual attestation with the interacting on-chain functions. Through a security analysis of TeeMAF, the reliability of deployed DApps can be verified, ensuring their correct execution. Furthermore, based on this framework, this paper proposes a decentralized resource orchestration platform (a specific DApp) for deploying applications over untrusted environments. The system is implemented on Ethereum and benchmarked using Hyperledger Caliper. Performance evaluation focusing on throughput and latency demonstrates that, compared to platforms without a mutual attestation scheme, the performance overhead remains within an acceptable range.

  匹配依据：MPC: secure computing; TEE: intel sgx, sgx, trusted execution environments

  </details>
