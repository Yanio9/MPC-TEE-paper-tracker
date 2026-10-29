# 2026 · TEE · 仅预印本来源 · 第 2/2 页

[总目录](../PAPERS.md) · [上一页](2026-tee-preprint-01.md)

- **ODYSSEY: Reestablishing Confidentiality in Confidential Blockchain via Delegated Execution**
  2026-06-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.04892)
  Ju Yang, Weili Wang, Jianyu Niu, Jianzong Wang, Yinqian Zhang

  <details><summary>摘要 / Abstract</summary>

  Confidential blockchains leveraging Trusted Execution Environments (TEEs) have garnered extensive attention for transaction confidentiality. In this paper, we first taxonomize two classes of attacks against confidential blockchains, i.e., execution-inference and execution-replay attacks, which exploit TEEs&#x27; long-lasting side-channel and state-continuity issues to compromise the confidentiality of existing consortium blockchains. Then, we present ODYSSEY, a confidential blockchain that efficiently mitigates these attacks. The core innovations of ODYSSEY are the following: (1) Its delegation model: clients delegate transaction execution to their designated trustees, while other participants synchronize only the execution results, which significantly reduces the attack surface while preserving confidentiality and system performance. (2) Two novel techniques to improve ODYSSEY&#x27;s efficiency and security: location-aware concurrent execution and delegation failure handler. Finally, we develop a prototype of ODYSSEY on FISCO BCOS, an enterprise-grade consortium blockchain platform. We have conducted various experiments, and our evaluation results show that in a WAN environment with 3 nodes, ODYSSEY can achieve about 4k throughput while keeping latency as low as 0.4-0.5s.

  匹配依据：TEE: trusted execution environments

  </details>

- **Implement Kubernetes Pod-Level Remote Attestation for Confidential Workloads on dstack**
  2026-06-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.03323)
  Yang Yang, Kevin Wang, Yuanhai Luo, Hang Yin, Jie Cai, Shunfan Zhou, Wenfeng Wang

  <details><summary>摘要 / Abstract</summary>

  The rise of LLM-as-a-Service and other confidential cloud workloads demands cryptographic proof that user data is processed in a trusted, untampered environment. Existing solutions, notably Confidential Containers (CoCo), enforce a strict &quot;one Pod per VM&quot; model that attests only the Guest OS stack, leaving container-level identity unverified and incurring prohibitive per-VM resource overhead. We present dstack-capsule, a Kubernetes platform that enables Pod-level remote attestation on Intel TDX by allowing multiple Pods to share a single Confidential VM while each retains independent, hardware-backed proof of identity. Our key insight is a two-layer attestation architecture: static platform measurements are frozen in RTMR[3] via an irreversible privilege fuse, while dynamic Pod identities (pod_uid, pod_spec_hash, workload_id) are embedded in the TDX Quote&#x27;s report_data field and signed by hardware on every request. dstack-capsule introduces (1) a Pod-level attestation protocol binding Pod spec digests to hardware-signed Quotes; (2) a privilege fuse mechanism that atomically transitions a node from setup mode to secure mode; (3) a multi-layer sandbox spanning storage, runtime, admission, API, and network isolation layers; and (4) a complete open-source implementation based on Kubernetes 1.32, Intel TDX, and Sysbox. We evaluate the security properties, attestation correctness, and performance characteristics of dstack-capsule, demonstrating that it achieves Pod-granularity verification without the resource overhead of per-VM isolation.

  匹配依据：TEE: intel tdx

  </details>

- **Formal Verification of Secure Encrypted Virtualization**
  2026-05-31 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2606.01381)
  Hansika Weerasena, Amitabh Das, Prabhat Mishra

  <details><summary>摘要 / Abstract</summary>

  Trusted execution environments (TEEs) provide a secure environment for data and code in use, ensuring that they are protected with respect to confidentiality and integrity. Virtual machine (VM)-based TEEs utilize virtualization technology to create isolated execution spaces that can support a complete operating system or specific applications. AMD secure encrypted virtualization (SEV) is a key technology used in confidential computing in the cloud enabling hardware-based memory encryption to protect sensitive data within VMs. However, AMD SEV often operate without formal assurances of their security guarantees. Our research introduces a formal framework for representing and verifying AMD SEV confidential VMs. Specifically, we conduct design-level and property-level abstraction on AMD SEV specification and conduct property checking on the model to ensure confidentiality, integrity and availability. This approach provides a rigorous foundation for defining and verifying key security attributes for safeguarding execution environments.

  匹配依据：TEE: amd sev, confidential computing, secure encrypted virtualization, trusted execution environments

  </details>

- **Protecting On-Device AI Inference: A Systematic Review of Attacks and Defence Mechanisms**
  2026-05-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.29450)
  Zisis Tsiatsikas, Alexandros Fakis, Georgios Karopoulos, Vasileios Kouliaridis, Marios Anagnostopoulos

  <details><summary>摘要 / Abstract</summary>

  The need for secure and private Artificial Intelligence (AI) and Machine Learning (ML) on edge and mobile devices has increased the necessity of protecting the architecture of these systems from threats to both security and privacy. With an ever-increasing number of pre-trained AI models being used on mobile platforms for client-side inference, there are rising concerns about the risks associated with the theft/extraction of AI models, adversarial attacks on AI models, and data breaches. As a result of this trend, a variety of defence mechanisms have been proposed to protect against these threats. These include Trusted Execution Environments (TEEs), homomorphic encryption, obfuscation, and differential privacy, among others. However, current surveys largely focus on edge intelligence, which includes distributed training, and thus overlook security and privacy issues that are specific to on-device AI inference. To the best of our knowledge, this paper presents the first comprehensive review of threats and corresponding defence mechanisms targeting on-device inference. Our results show that the attack and defence literature are unbalanced: approximately one quarter of the surveyed attack papers focus on Intellectual Property (IP) attacks, whereas half of the defence solutions tackle the same issue. More importantly, some attack categories have no defence paper associated to them, such as adversarial attacks that account for roughly one third of the attack literature. This asymmetry between known attacks and available mitigations highlights clear opportunities for future research on securing on-device AI inference.

  匹配依据：TEE: trusted execution environments

  </details>

- **Shielded but Lightweight: Building Practical Confidential Containers with ARM CCA**
  2026-05-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.26018)
  Liantao Song, Yiming Zhang, Fengwei Zhang, Yan Ding, Bin Zhou, Jie Yu, Yusong Tan

  <details><summary>摘要 / Abstract</summary>

  The rapid advancement of cloud-native technologies has created an urgent need for security. Currently, confidential containers are increasingly deployed in multi-tenant environments. Existing confidential container designs mainly adopt a microVM-based architecture. Although this approach improves inter-container isolation, its complex software stack leads to high startup latency and significant resource overhead, making it unsuitable for short-lived container workloads. In this paper, we propose Fasco, a lightweight confidential container runtime based on the ARM Confidential Compute Architecture (CCA). Fasco directly instantiates each container as an independent Container Realm, leveraging CCA&#x27;s hardware-enforced isolation to ensure the confidentiality and integrity of application data inside the container. In addition, Fasco introduces a dedicated System Realm to provide system services and resource management for container realms. Through exception forwarding and shared buffers, Fasco ensures isolation among different container realms. We have implemented a prototype of Fasco and evaluated its performance on ARMv8 hardware. Experimental results show that Fasco reduces the startup latency and performance overhead of existing confidential container architectures while maintaining a small TCB.

  匹配依据：TEE: arm cca, confidential compute architecture

  </details>

- **"You do understand that people don't trust technology?": Explaining Trusted Execution Environments to Non-Experts**
  2026-05-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.26196)
  McKenna McCall, Carolina Carreira, Miguel Flores, Lorrie Faith Cranor

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) protect confidentiality and integrity of trusted applications by creating an isolated environment for executing code. Prior work has shown that users may feel more comfortable sharing data when they know it will be protected by a TEE, especially if they understand what a TEE is. In this study, we evaluated text-based explanations introducing TEEs to non-experts. We analyzed existing TEE explanations to develop candidate explanations and evaluated them via vignette scenarios with 966 crowdworkers. The explanations that enhanced understanding most were non-technical ones that highlighted specific threats that can be prevented by a TEE. Surprisingly, even the explanations that enhanced understanding had little effect on willingness to use the TEE-enhanced technology. These results provide insights into ways to communicate technical security concepts more effectively but also suggest that explaining security technology might not be enough to address users&#x27; privacy concerns.

  匹配依据：TEE: trusted execution environments

  </details>

- **Finding Missing Input Validation in TEEs via LLM-Assisted Symbolic Execution**
  2026-05-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.22058)
  Chengyan Ma, Jieke Shi, Ruidong Han, Ye Liu, Yuqing Niu, David Lo

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) provide hardware-enforced isolation that protects sensitive code and data from untrusted software. Despite their strong security guarantees, analyzing TEE applications remains challenging due to the high cost and complexity of configuring complete TEE build and runtime environments, as well as the limited observability imposed by hardware isolation. This paper presents SymTEE, a novel large language model (LLM)-assisted symbolic execution framework for detecting missing input validation issues in TEE applications without requiring real TEE setups. SymTEE begins by leveraging Abstract Syntax Tree (AST) analysis to extract TEE code slices that may lack sufficient input validation, and then employs an LLM (GPT-5 in our case) to automatically convert the extracted slices into KLEE-compatible harness programs containing lightweight mock execution environments for symbolic analysis. Evaluations on 26 vulnerabilities (11 real-world and 15 synthetic) show that SymTEE achieves 100% precision and 92.3% recall in detecting missing input validation vulnerabilities while incurring an average analysis cost of only $0.05. These results demonstrate the effectiveness and practicality of SymTEE&#x27;s pioneering paradigm of LLM-assisted symbolic execution, where LLMs autonomously generate mock environments to enable automated security analysis without complex setup, providing a more accessible and scalable framework for trusted computing systems.

  匹配依据：TEE: trusted execution environments

  </details>

- **Automated Repair of TEE Partitioning Issues via DSL-Guided and LLM-Assisted Patching**
  2026-05-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.22087)
  Chengyan Ma, Jieke Shi, Ruidong Han, Ye Liu, Feng Li, Yuqing Niu, David Lo

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) provide hardware-based isolation to protect sensitive data and computations from potentially compromised operating systems (OS). However, TEE applications inevitably interact with the untrusted OS through SDK interfaces, and improper partitioning can introduce severe vulnerabilities such as data leakage and code injection. While prior work has proposed static analysis tools to detect such issues, automated repair remains largely unexplored. This problem is particularly challenging due to three TEE-specific factors: the lack of standardized secure development guidelines, the difficulty of extracting semantic information from low-level C code, and the absence of mature testing and validation methods. In this work, we present TEERepair, a framework for automatically repairing bad partitioning issues in TEE applications. Our approach tackles the above challenges by introducing a domain-specific language (DSL) to encode repair rules that express and capture common TEE security patterns, which are instantiated as patch templates with placeholders for context-specific variables. We then leverage large language models (LLMs) to reason about code semantics and synthesize context-aware patches, and further generate test clients to validate the repairs. We evaluate TEERepair on the TEE Partitioning Errors Benchmark (PartitioningE-Bench), achieving a significantly higher repair success rate of 87.6% compared to baselines. Furthermore, applying TEERepair to real-world TEE projects, we submitted 5 repair pull requests, 2 of which have been confirmed and merged by project maintainers.

  匹配依据：TEE: trusted execution environments

  </details>

- **Polars inside Intel SGX2 Enclaves: An Empirical Study of Confidential Analytical Query Processing**
  2026-05-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.21797)
  Wei Wang, Burns Smith, Kenny Leftin

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) have renewed interest in confidential analytics, but most prior evaluations focus on SQL database engines or earlier SGX generations. This paper studies an Arrow-native DataFrame engine, Polars, running inside Intel SGX2 enclaves via Gramine on TPC-H SF30 with Azure Blob Storage. We report both the standard TPC-H power score and a query-only variant that removes table-loading time in order to separate compute overhead from data-ingestion overhead. Across four dataset-width configurations (approximately 22-73 GB), end-to-end overhead remains nearly constant at 1.49-1.56$\times$, but this composite metric obscures two distinct behaviors: query-only overhead declines from 1.51-1.52$\times$ to 1.43-1.44$\times$, whereas table-loading overhead rises from 2.27$\times$ to 4.07$\times$. We further show that overhead is not uniform across queries: for the len130 configuration, the median per-query SGX slowdown is 1.45$\times$ with a maximum of 2.57$\times$, and a small set of queries exhibits pronounced run-to-run spikes consistent with stateful EPC pressure. Finally, we compare Polars&#x27; lazy and eager APIs under the same TEE setting. Lazy execution is 2.25-2.27$\times$ faster overall, while eager execution fails with out-of-memory errors at 41 GB and above. Relative to the recent DuckDB-SGX2 study, our results suggest that SGX2 can support Arrow-native analytical processing with a similar order of security overhead, but that load-path amplification and API-level optimization are first-order determinants of end-to-end performance.

  匹配依据：TEE: sgx, trusted execution environments

  </details>

- **Heartbeat-Bound Hierarchical Credentials: Cryptographic Revocation for AI Agent Swarms**
  2026-05-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.20704)
  Saurabh Deochake

  <details><summary>摘要 / Abstract</summary>

  Autonomous AI agents that spawn sub-agent swarms create a safety gap: existing credential revocation mechanisms, OAuth~2.0 introspection, OCSP, and W3C Status Lists, require network connectivity to a central authority, leaving ``zombie agents&#x27;&#x27; executing privileged operations for minutes to hours after operator shutdown. We present Heartbeat-Bound Hierarchical Credentials (HBHC), a cryptographic protocol that binds credential validity to periodic parent liveness proofs. Verifiers enforce freshness using only a cached public key and local clock; no network round-trip is required. When heartbeat generation ceases, all descendant credentials become unusable within a deterministically bounded window $W_z \le W_{\max} + Δ_h + ε$, conditional on bounded clock skew and parent keys held in secure enclaves. Evaluation at the protocol layer and with real LLM-backed agent swarms (GPT-4o-mini) demonstrates a 90$\times$ reduction in the zombie window over OAuth~2.0, 0.26~ms full authentication in Rust, 18,000+ verifications per second under concurrent HTTP load, and stable per-verification latency from 10 to 10,000 agents. Real-agent experiments show 0.71\% end-to-end overhead on tool calls, zero post-revocation tool calls under prompt injection that bypasses application-layer guardrails, and cascading revocation across a 49-agent four-level hierarchy within the theoretical bound.

  匹配依据：TEE: secure enclaves

  </details>

- **Benchmarking Confidential GPU Inference on NVIDIA H100 under Intel TDX**
  2026-05-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.19353)
  Wei Wang, Abdul Hyee Waqas, Burns Smith

  <details><summary>摘要 / Abstract</summary>

  Confidential computing is becoming a practical deployment requirement for AI inference workloads that process sensitive inputs or protect proprietary model assets. However, the performance cost of enabling confidential execution for GPU-accelerated large language model serving remains workload dependent and operationally important. This paper presents a benchmark study comparing standard non-confidential execution with confidential computing mode on a single NVIDIA H100 80GB GPU hosted in an Intel TDX confidential instance. The evaluation uses two representative language models, Mistral-7B v0.1 and Qwen3-30B-A3B, and measures time to first token, end-to-end request latency, per-request token generation throughput, global token throughput, and closed-loop request throughput under increasing concurrency. In fixed request-rate experiments, confidential mode increases average TTFT by 21.8% for Mistral-7B and 27.8% for Qwen3-30B-A3B, while global token throughput drops by 17.7% and 21.1%, respectively. In closed-loop concurrency experiments, throughput gaps remain in the 11.5-20.2% range, but the larger model reaches its saturation knee earlier under confidential mode. The results suggest that confidential GPU inference can retain usable throughput under load, but capacity planning must account for both the steady throughput penalty and the earlier saturation behavior observed for larger models.

  匹配依据：TEE: confidential computing, intel tdx

  </details>

- **An Evidence-driven Protocol for Trustworthy CI Pipelines**
  2026-05-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.21089)
  Fernando Castillo, Eduardo Brito, Pille Pullonen-Raudvere, Sebastian Werner, Stefan Tai

  <details><summary>摘要 / Abstract</summary>

  Enterprise software supply chains are increasingly vulnerable to infrastructure attacks, resulting in financial and reputational damage. Ensuring the integrity and provenance of software artifacts remains a significant challenge, where re-execution of the build and tests by every consumer to guarantee provenance produces a verification bottleneck and credibility reduction. This paper presents an evidence-driven protocol for trustworthy Continuous Integration (CI) pipelines that combines Deterministic Build Systems (DBS) with Trusted Execution Environments (TEEs). The approach provides cryptographically verifiable guarantees of integrity, authenticity, and attestation for CI artifacts in distributed environments, reducing implicit trust without requiring costly re-execution by consumers. We introduce a protocol that binds deterministic builds with TEE-based attestations, formalizing the evidence life cycle, together with a practical implementation using Nix and Intel TDX. Experimental results show that artifact verification is reduced from redundant computation to lightweight signature and policy checks. These findings demonstrate that evidence-driven CI pipelines establish scalable and verifiable trust in digital infrastructure, effectively amortizing the initial computational overhead introduced by TEEs.

  匹配依据：TEE: intel tdx, trusted execution environments

  </details>

- **Ethical Hyper-Velocity (EHV): A Hardware-Rooted Zero-Trust Runtime Enforcement Architecture for Agentic AI Systems**
  2026-05-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.17909)
  Riddhi Mohan Sharma

  <details><summary>摘要 / Abstract</summary>

  As autonomous agentic systems scale across regulated critical infrastructures, the lack of mechanistic, hardware-rooted enforcement for high-frequency policy updates presents a fundamental safety gap. We present Ethical Hyper-Velocity (EHV), a governance-aware runtime enforcement architecture for agentic systems that combines Grammar-Constrained Decoding (GCD) for inline policy-constrained token generation, Causal Graph CRDT-based policy synchronization with vector-clock ordering, hardware-attested execution in Trusted Execution Environments (TEEs), and OSCAL-formatted machine-readable audit logging. Unlike retrospective auditing frameworks (ISO/IEC 42001, NIST AI RMF) that introduce 14-30 day policy latencies, EHV relocates the Policy Enforcement Point (PEP) into the inference pipeline via a Governance-Aware Just-In-Time (JIT) Compiler. Under explicitly stated assumptions, the architecture reduces enforcement latency, improves traceability, and supports formal verification of safety invariants in a bounded model. We demonstrate via TLA+ model checking that non-compliant agentic actions were unreachable in the verified bounded operating state space (1,738 states generated, 324 distinct, depth 8, zero violations). Under these conditions, O(1) runtime enforcement reduces the traditional trade-off between deployment velocity and governance integrity, targeting Governance Latency from O(days) toward O(1). EHV&#x27;s differentiating contribution is the integration of GCD, Causal CRDT, TEE attestation caching, and bounded formal verification into a single, hardware-rooted enforcement architecture -- a combination not achieved by any contemporaneous system. The architecture is demonstrated through a pediatric oncology dosage use case, with applicability to regulated critical infrastructures including healthcare, financial compliance, and critical infrastructure control.

  匹配依据：TEE: trusted execution environments

  </details>

- **Insecure Despite Proven Updated: Extracting the Root VCEK Seed on EPYC Milan via a Software-Only Attack**
  2026-05-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.12990)
  Muyan Shen, Yu Qin

  <details><summary>摘要 / Abstract</summary>

  In the official whitepaper of Secure Encrypted Virtualization with Secure Nested Paging (SEV-SNP), AMD explicitly emphasizes the capability to prevent Trusted Computing Base (TCB) rollback attacks. Cryptographically, this is realized by signing attestation reports with the Versioned Chip Endorsement Key (VCEK), which is derived by incorporating the TCB version into the hardware root seed. In this architecture, safeguarding the hardware root seed is the ultimate line of defense. However, our research reveals that this protection is insufficient on EPYC Milan by presenting a software-only exploit. Specifically, we firstly introduce MilanLaunchy attack, an exploit that achieves code execution on the AMD secure processor. Building on this foundation, we develop the BadFuse attack, which extracts the hardware root seed by exploiting a lack of write restrictions in the fuse controller. This end-to-end attack chain enables an adversary to forge valid attestation reports for any firmware version, thereby effectively undermining the security model of SEV-SNP.

  匹配依据：TEE: secure encrypted virtualization, sev snp

  </details>

- **EBCC: Enclave-Backed Confidential Containers via OCI-Compatible Runtime Integration**
  2026-05-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.13676)
  Di Lu, Qingwen Zhang, Yujia Liu, Xuewen Dong, Yulong Shen, Zhiquan Liu, Jianfeng Ma

  <details><summary>摘要 / Abstract</summary>

  Container runtimes provide a stable operational interface for deploying, monitoring, and controlling modern workloads, while trusted execution environments (TEEs) provide hardware-enforced isolation for sensitive computation. Existing confidential-container systems often rely on VM-backed deployment stacks or TEE-specific execution substrates, which can separate confidential execution from the conventional OCI runtime lifecycle. This paper presents EBCC (Enclave-Backed Confidential Containers), an OCI-compatible runtime architecture for managing composite confidential-computing workloads. EBCC treats the REE-side anchor and TEE-side confidential stages as a single containerized confidential-computing composite, preserves standard OCI lifecycle operations, and keeps TEE-specific execution behind a backend adapter. It also maintains persistent per-instance state and per-stage artifacts for request handling, response generation, logging, and evidence binding. We implement EBCC on a Keystone backend and evaluate its correctness, performance, footprint, and concurrent execution behavior. The results show that EBCC introduces additional latency over native Keystone execution, mainly due to lifecycle mediation, request validation, EID allocation, backend dispatch, and artifact persistence, while keeping the added footprint concentrated on host-side management state. Cross-TEE case studies on SGX, TDX, and OP-TEE show that the same lifecycle and stage abstraction can be mapped to enclave-style, VM-style, and embedded-style TEEs. These results indicate that EBCC can make TEE-backed execution manageable through an OCI-style lifecycle without materially enlarging the protected-side TCB.

  匹配依据：TEE: confidential computing, sgx, trusted execution environments

  </details>

- **Enforcing Attestable Workflows across Untrusted Networks**
  2026-05-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.09297)
  Hung Dang, Tue Nguyen

  <details><summary>摘要 / Abstract</summary>

  Confidential high-performance computing orchestrates workloads across federated domains, yet existing frameworks rely on high-overhead user-space library operating systems or assume single-host execution. We propose \codename, an architecture federating Trusted Execution Environments via a split Trusted Computing Base (TCB) design. It couples a hardware-isolated Control Plane executing Mutually Attested Key Exchange (\make) with a measured guest-resident extended Berkeley Packet Filter (eBPF) Data Plane. By anchoring cryptographic key release to hardware measurements and executing enforcement in the kernel, \codename\ achieves native-speed encrypted routing. Empirical evaluation demonstrates a steady-state enforcement cost of $6\,μ$s per packet, imposing a $13$--$15\,μ$s absolute latency overhead. On distributed pipelines, \codename\ incurs just a $6.1\%$ execution penalty over plaintext baselines, bypassing the $62\%$ penalty of user-space counterparts. The system initializes a 100-node cluster in under 1.5 seconds, providing an efficient confidential interconnect for long-running workflows.

  匹配依据：TEE: trusted execution environments

  </details>

- **WATSON: Leveraging Data Watchpoints for Shadow Stack Protection on Embedded Systems**
  2026-05-09 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.08604)
  Xi Tan, Sagar Mohan, Ziming Zhao

  <details><summary>摘要 / Abstract</summary>

  Embedded and Internet-of-Things (IoT) devices play a critical role in modern life. Their software and firmware, often developed in memory-unsafe languages like C, are susceptible to memory safety vulnerabilities that can lead to control-flow hijacking attacks. Shadow stack is a defense mechanism against control-flow hijacking that targets return addresses. However, existing shadow stack solutions for embedded systems have the following limitations. First, they lack system-wide protection, particularly for interrupts and exceptions. Second, they introduce high performance overhead. Third, they depend on security extensions like a trusted execution environment, which are not universally available on embedded devices. Finally, they rely on hardware features that have inherent configurable constraints, which pose compatibility challenges when integrating security mechanisms that require similar hardware support. To overcome these limitations, we present WATSON, an efficient and effective shadow stack solution. It leverages a standard hardware debug unit named data watchpoints for shadow stack protection on embedded systems. To prevent unauthorized access to the shadow stack, WATSON leverages the address-matching features of the debug unit to enforce the write protection of the shadow stack. Additionally, WATSON is compatible with compiler options to enforce forward-edge control-flow integrity. We implemented a prototype of WATSON on the ARM CortexM architecture, and the concept also applies to other platforms. The introduced overhead is 7.33% and 1.81% on BEEBS and CoreMark-Pro benchmarks, respectively. We also evaluate WATSON on exception handling and two real-world applications, observing negligible performance overhead and a worst-case code size overhead of 2.11%. Furthermore, our security evaluation demonstrates that WATSON effectively prevents attacks.

  匹配依据：TEE: trusted execution environment

  </details>

- **TENNOR: Trustworthy Execution for Neural Networks through Obliviousness and Retrievals**
  2026-05-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.07160)
  Zifan Qu, Vasileios P. Kemerlis, Giuseppe Ateniese, Evgenios M. Kornaropoulos

  <details><summary>摘要 / Abstract</summary>

  Training neural networks on sensitive data in untrusted cloud environments requires simultaneously achieving computational efficiency and rigorous privacy guarantees. Sparsification techniques, essential for scalable training of wide layers, expose input-dependent memory-access patterns that are visible and can be exploited by a host OS/hypervisor, even when computation is protected by a Trusted Execution Environment. We present TENNOR, a system that resolves this tension by co-designing the neural network training pipeline with doubly oblivious primitives, eliminating value-dependent neural network access-pattern leakage while also utilizing adaptive sparsification. TENNOR recasts sparse neuron activation as a locality-sensitive hashing (LSH) retrieval problem, reducing secure sparsification to doubly oblivious accesses over an LSH data structure. To eliminate the prohibitive storage cost of &quot;multi-table&quot; LSH, we introduce Multi-Probe Winner-Take-All (MP-WTA): the first multi-probe scheme for rank-based LSH, achieving a $50\times$ reduction in (hash table) memory while preserving model accuracy. We evaluate TENNOR on multi-label classification benchmarks, with output layers of up to hundreds of thousands of neurons under different batch sizes inside an Intel TDX Trusted Domain, achieving per-batch training speedups of $13\times$-$470\times$ over a Path ORAM baseline and reducing a 208-hour run to about 26 minutes.

  匹配依据：TEE: intel tdx, trusted execution environment

  </details>

- **Kettle: Attested builds for verifiable software provenance**
  2026-05-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.08363)
  Amean Asad, André Arko

  <details><summary>摘要 / Abstract</summary>

  Kettle is an attested build system that produces cryptographically verifiable provenance for software built inside Trusted Execution Environments (TEEs). A Kettle build records the source commit, dependency set, toolchain, build environment, and output artifact digests in a provenance document produced inside a measured confidential VM. The SHA-256 digest of that document is committed to the TEE platform&#x27;s attestation report-data field, so the hardware-signed attestation report is itself the signature on the provenance, with the signing identity chaining to the TEE manufacturer&#x27;s root of trust rather than to the build infrastructure operator. Because the CVM image is itself reproducible, its launch measurement is public and stable, which lets a build requester pre-attest the CVM before submitting any input and optionally deliver source over a TLS channel terminated inside it, so the build runs end-to-end confidentially without the host ever seeing source code in plaintext. Verification reduces to one signature check against the vendor root and a small set of digest comparisons, with no need to re-execute the build. The result removes the build infrastructure, its operators, and the artifact distribution channel from the trust surface a verifier must accept when deciding whether a binary corresponds to its claimed inputs.

  匹配依据：TEE: trusted execution environments

  </details>

- **CCX: Enabling Unmodified Intel SGX Applications on Arm CCA**
  2026-05-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.07548)
  Matti Schulze, Thorsten Holz, Felix Freiling

  <details><summary>摘要 / Abstract</summary>

  Novel confidential computing technologies such as Intel TDX, AMD SEV, and Arm CCA have recently emerged. In practice, due to its minimal trust boundaries, Intel SGX still remains widely used for enclave-based applications in cloud environments, including confidential cloud services, privacy-preserving communication, secure payment processing, and privacy-focused advertising. With the growing adoption of Arm CPUs in cloud systems, however, existing SGX applications face a significant portability challenge: they are tightly coupled to SGX-specific APIs and execution semantics. In this paper, we present the design and implementation of CCX, a framework that enables existing SGX applications to run on Arm CCA without source code modification. To this end, CCX redesigns SGX functionality within Arm CCA firmware, adapting SGX abstractions to CCA&#x27;s architecture design while preserving full compatibility with existing applications originally developed for SGX. We implemented a prototype of CCX on both the QEMU emulator and a Nitrogen8M development board. Our evaluation shows that CCX is capable of executing existing SGX applications without requiring source code changes, while providing security guarantees comparable to Intel SGX and achieving performance improvements in our evaluated settings.

  匹配依据：TEE: amd sev, arm cca, confidential computing, intel sgx, intel tdx, sgx

  </details>

- **Constraining Host-Level Abuse in Self-Hosted Computer-Use Agents via TEE-Backed Isolation**
  2026-05-07 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.06393)
  Di Lu, Bo Zhang, Xiyuan Li, Yongzhi Liao, Xuewen Dong, Yulong Shen, Zhiquan Liu, Jianfeng Ma

  <details><summary>摘要 / Abstract</summary>

  Self-hosted computer-use agents (SHCUAs), such as OpenClaw, combine natural-language interaction with direct access to host-side resources, including browsers, files, scripts, system commands, and external communication channels. While useful for automating real tasks, this capability also creates a host-level abuse surface: a legitimately deployed agent may be steered toward unsafe operations through malicious messages, indirect prompt injection, unsafe skills, or tampering along the host-side control path. We argue that such risks cannot be addressed by ad hoc blocking rules alone, because the security criticality of an operation depends jointly on its action type, target object, execution context, and potential effect. This paper presents an operation-centric model for risk-based confinement of SHCUA operations. The proposed design keeps ordinary functionality on the constrained REE path, while protecting security-critical classification, authorization, binding, evidence generation, and selected execution-control decisions inside a cloud-native TEE-backed trusted operation plane. We instantiate the architecture on OpenClaw using Intel TDX as the primary trusted backend, with remote terminal-side trusted components verifying TDX-audited commands before constrained local execution. The evaluation shows that the design can block unsafe or policy-disallowed operations before execution, preserve ordinary functionality for allowed workloads, and provide auditable evidence with deployment-dependent overhead.

  匹配依据：TEE: intel tdx

  </details>

- **When Agents Handle Secrets: A Survey of Confidential Computing for Agentic AI**
  2026-05-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.03213)
  Javad Forough, Marios Kogias, Hamed Haddadi

  <details><summary>摘要 / Abstract</summary>

  Agentic AI systems, specifically LLM-driven agents that plan, invoke tools, maintain persistent memory, and delegate tasks to peer agents via protocols such as MCP and A2A, introduce a threat surface that differs materially from standalone model inference. Agents accumulate sensitive context, hold credentials, and operate across pipelines no single party fully controls, enabling prompt injection, context exfiltration, credential theft, and inter-agent message poisoning. Current defenses operate entirely within the software stack and can be silently bypassed by a sufficiently privileged adversary such as a compromised cloud operator. Confidential computing (CC) offers a hardware-rooted alternative: Trusted Execution Environments (TEEs) isolate agent code and data from privileged system software, while remote attestation enables verifiable trust across distributed deployments. This survey synthesizes the design space in four parts: (i) a unified taxonomy of six TEE platforms (Intel SGX, Intel TDX, AMD SEV-SNP, ARM TrustZone, ARM CCA, and NVIDIA H100 CC) covering deployment roles and performance tradeoffs; (ii) an agent-centric threat model spanning perception, planning, memory, action, and coordination layers mapped to nine security goals; (iii) a comparative survey of CC-based defenses distinguishing findings that transfer from single-call inference versus what requires new agentic designs; and (iv) six open challenges including compound attestation for multi-hop agent chains and GPU-TEE performance at LLM scale. While several hardware trust primitives appear mature enough for targeted deployments, no broadly established end-to-end framework yet binds them into a coherent security substrate for production agentic AI.

  匹配依据：TEE: amd sev, arm cca, confidential computing, intel sgx, intel tdx, trusted execution environments, trustzone

  </details>

- **KingsGuard: Enclave Data Protection Under Real-World TEE Vulnerabilities**
  2026-05-01 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2605.00613)
  Saltanat Firdous Allaqband, Deepanjali S, Rohit Srinivas R G, Devashish Gosain, Chester Rebeiro

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) have emerged as a cornerstone for securing sensitive computations by providing isolated enclaves protected from untrusted software. However, their security guarantees are undermined by vulnerabilities in both the enclave code and the underlying hardware design, which can allow sensitive data to leak despite strong isolation guarantees. This paper presents KINGSGUARD, a novel TEE design that systematically monitors and controls the propagation of sensitive data within an enclave. By enforcing fine-grained data flow tracking and checks in hardware, our approach ensures that sensitive data does not leave the enclave boundary, thus bridging the gap between the idealized threat models of TEEs and their practical realizations. Additionally, to balance security with practical functionality, we introduce controlled declassification at enclave boundaries, allowing intentional release of data to the outside world. Our implementation of KINGSGUARD on a RISC-V processor has a 10.8% hardware area overhead when synthesized on FPGA and a 5.69% performance overhead.

  匹配依据：TEE: trusted execution environments

  </details>

- **Making AI-Assisted Grant Evaluation Auditable without Exposing the Model**
  2026-04-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.25200)
  Kemal Bicakci

  <details><summary>摘要 / Abstract</summary>

  Public agencies are beginning to consider large language models (LLMs) as decision-support tools for grant evaluation. This creates a practical governance problem: the model and scoring rubric should not be exposed in a way that allows applicants to optimize against them, yet the evaluation process must remain auditable, contestable, and accountable. We propose a TEE-based architecture that helps reconcile these requirements through remote attestation. The architecture allows an external verifier to check which model, rubric, prompt template, and input representation were used, without exposing model weights, proprietary scoring logic, or intermediate reasoning to applicants or infrastructure operators. The main artifact is an attested evaluation bundle: a signed, timestamped record linking the original submission hash, the canonical input hash, the model-and-rubric measurement, and the evaluation output. The paper also considers a scenario-specific prompt injection risk: applicant-controlled documents may contain hidden or indirect instructions intended to influence the LLM evaluator. We therefore include a canonicalization and sanitization layer that normalizes document representations and records suspicious transformations before inference. We position the design relative to confidential AI inference, attestable AI audits, zero-knowledge machine learning, algorithmic accountability, and AI-assisted peer review. The resulting claim is deliberately narrow: remote attestation does not prove that an evaluation is fair or scientifically correct, but it can make part of the evaluation process externally verifiable.

  匹配依据：TEE: tee (context)

  </details>

- **Resolving Conflicts Between RTOS Timekeeping and Uninterruptable Trusted Computing**
  2026-04-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.24277)
  Antonio Joia Neto, Amarin Laohajirapan, Norrathep Rattanavipanon, Ivan De Oliveira Nunes

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) on low-power microcontrollers (e.g., ARM TrustZone-M) enable isolation of Secure and Non-Secure software but still require both worlds to share resources, including interrupt controllers. In this model, real-time applications and real-time operating systems (RTOS-s) are executed in the Non-Secure sub-system, whereas the Secure sub-system is typically reserved for a small set of pre-defined security (e.g., cryptographic) operations referred to as trusted computing services. However, many RTOS-s rely on periodic interrupts (SysTicks) to advance their own notion of time (time-keeping), and the delivery of this interrupt is essential for preserving real-time behavior. On the other hand, the security of many trusted computing services requires atomicity vis-a-vis the Non-Secure sub-system (where the RTOS resides), precluding SysTick handling. This paper first characterizes this conflict and then introduces a Secure-driven time synchronization mechanism in which the Secure World measures elapsed time and compensates the Non-Secure RTOS by unobtrusively updating the RTOS time-keeping data structures with the appropriate number of missed ticks before re-enabling interrupts and resuming the execution of the Non-Secure system. This approach restores a consistent, monotonic notion of time across worlds and enables secure coexistence of trusted computing services and RTOS-s on microcontrollers. Importantly, the proposed approach requires no modifications to the underlying RTOS and yields no significant run-time overhead.

  匹配依据：TEE: trusted execution environments, trustzone

  </details>

- **C8s: A Confidential Kubernetes Architecture**
  2026-04-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.26974)
  Amean Asad, Patrick McClurg, João Andrade

  <details><summary>摘要 / Abstract</summary>

  This paper presents C8s, a confidential computing architecture for Kubernetes that provides cryptographically rooted confidentiality, integrity, and verifiability guarantees for Kubernetes clusters from infrastructure operators. These guarantees are cryptographically provable to any independent third party verifier. The architecture is built on hardware Trusted Execution Environments (TEEs), specifically AMD SEV-SNP, Intel TDX, and NVIDIA Confidential Computing support, to establish an attestation-rooted trust boundary around confidential VMs. This design is compatible with managed Kubernetes services such as Amazon EKS, Google GKE, and Microsoft AKS, where the control plane cannot be attested. Under this boundary, three groups gain guarantees that are absent from conventional deployments. Data and artifact owners can deploy sensitive workloads and proprietary artifacts on third-party infrastructure without risking exfiltration. Compute providers can offer execution services without revealing workloads to cloud operators. End users can submit requests that remain opaque to all parties except the attested TEE processing them. Representative workloads include AI inference, securing AI model weights, and training or fine-tuning on sensitive data.

  匹配依据：TEE: amd sev, confidential computing, intel tdx, trusted execution environments

  </details>

- **Agentic Witnessing: Pragmatic and Scalable TEE-Enabled Privacy-Preserving Auditing**
  2026-04-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.24203)
  Antony Rowstron

  <details><summary>摘要 / Abstract</summary>

  Auditing the semantic properties of proprietary data creates a fundamental tension: verification requires transparent access, while proprietary rights demand confidentiality. While Zero-Knowledge Proofs (ZKPs) ensure privacy, they are typically limited to precise algebraic constraints and are ill-suited for verifying qualitative, unstructured properties, such as the logic within a codebase. We propose {\em Agentic Witnessing}, a framework that moves verification from attested execution to {\em attested reasoning}. The system is composed of three agents: a Verifier (who wants to check properties of a dataset), a Prover (who owns the dataset) and an Auditor (that inspects the dataset). The Verifier is allowed to ask a limited number of simple binary true/false questions to the auditor. By isolating an LLM-based Auditor within a Trusted Execution Environment (TEE), the system enables the Verifier to query a Prover&#x27;s private data via simple Boolean queries, without exposing the raw dataset. The Auditor uses the Model Context Protocol (MCP) to dynamically inspect the target dataset, producing a yes/no verdict accompanied by a cryptographic transcript: a signed hash chain binding the reasoning trace to both the original dataset and the TEE&#x27;s hardware root of trust. We demonstrate this architecture by automating the artifact evaluation process for 21 peer-reviewed computer science papers with released codebases on GitHub (e.g. Does the codebase implement the system described in the paper?). We verified five high-level properties of these codebases described in the corresponding publications, treating the source code as private. Our results show that TEE-enabled agentic auditing provides a mechanism for privacy-preserving oversight, effectively decoupling qualitative verification from the need for data disclosure.

  匹配依据：TEE: trusted execution environment

  </details>

- **Proof of Execution: Runtime Verification for Governed AI Agent Actions**
  2026-04-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2607.05397)
  James Rhodes, George Kang

  <details><summary>摘要 / Abstract</summary>

  Agent systems increasingly execute rather than advise. When an AI agent queries regulated data, invokes effectful tools, and mutates persistent state, correctness is not captured by whether a terminal output looks plausible. The operative questions are whether each step was authorized under a contract, whether the recorded history is tamper-evident, and whether the trajectory can be reconstructed deterministically. We formalize this as runtime proof of execution. An execution is a triple $x = (C, T, R)$: a contract $C$, an Execution Causal Event Stream (ECES) $T$, and a replay context $R$. A well-formedness predicate and five validator-checkable invariants form the PoE validity predicate. Five semantic guarantees describe authorization, path compliance, null effect on deny, history integrity, and replayability. We prove soundness under explicit cryptographic and deployment assumptions: any PPT adversary that produces a PoE-valid execution violating a semantic guarantee yields a signature forgery, a hash collision, or a quantified deployment-failure event. The Prime Execution Model (PEM) separates planning, enforcement, effect, and recordkeeping into distinct authority planes; a lemma reduces trace completeness to Effector-exclusive credentialing. An Execution Attestation Certificate is issued only when PoE = 1. In a single-node TypeScript prototype, PoE adds approximately 2.7 ms on a minimal flow and 4.4% overhead on concurrent batch workloads; a standard eight-event trace compresses to approximately 1.1 KB; injected Gateway-bypass and trace-mutation attacks are rejected. PoE does not replace consensus, TEEs, or zkVMs; it binds authorization, effect, history, and replay into a single runtime-checkable object so that governed execution becomes attestable under contract.

  匹配依据：TEE: tees (context)

  </details>

- **Tessera: Secure, Near-Line-Rate Weight Streaming for UMA Edge Accelerators**
  2026-04-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.23205)
  Animan Naskar

  <details><summary>摘要 / Abstract</summary>

  Deploying proprietary Deep Neural Networks (DNNs) on commodity edge devices demands hardware-backed Digital Rights Management (DRM) capable of withstanding both software-level and physical adversaries. In Unified Memory Architecture (UMA) systems, the host CPU and Neural Processing Unit (NPU) share physical DRAM, leaving plaintext model weights directly readable by a compromised OS kernel. Existing defenses fail in this constrained setting: trusted execution environments monopolize scarce memory with permanently reserved regions, while full-memory encryption operates at page granularity. This forces the system to fetch massive 4 KB memory pages for sub-page tensor tiles, severely crippling bandwidth. We present Tessera, a reference architecture for inline, cache-line granularity weight decryption on UMA edge accelerators. The design intercepts 64-byte AXI bursts, computing AES-256-CTR keystreams in parallel with DRAM fetches. This streams plaintext directly into isolated NPU SRAM, creating a transient memory footprint confined to the active tile and eliminating the need for permanent memory carve-outs. Measurements across three distinct SoC platforms demonstrate that this parallelization hides cryptographic latency behind standard DRAM fetch times, a condition that holds even under worst-case timing variations. Consequently, Tessera is projected to achieve 98.4\% of the theoretical memory bandwidth ceiling (a mere 1.6\% overhead). Across standard vision and language models, page-level memory encryption suffers up to a 32x bandwidth penalty, whereas Tessera maintains an optimal 1x footprint for all layer geometries. Finally, Tessera neutralizes major UMA-specific attack vectors -- including physical DRAM extraction, rogue DMA, and compute hijacking -- and formally prevents plaintext leakage across sparse tensors.

  匹配依据：TEE: trusted execution environments

  </details>

- **Reconstructive Authority Model: Runtime Execution Validity Under Partial Observability**
  2026-04-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.22898)
  Marcelo Fernandez - TraslaIA

  <details><summary>摘要 / Abstract</summary>

  Autonomous systems increasingly operate under partial observability where execution-relevant state is never fully accessible. Existing governance mechanisms -- trusted execution environments, oracle-signed state proofs, cryptographic attestation -- enforce the integrity of computation and state projections. We show this is structurally insufficient: an authenticated projection of state is necessary but never sufficient for execution validity. We introduce the Reconstructive Authority Model (RAM), which separates integrity from coverage. RAM defines a reconstruction gate that reasons over an explicit coverage envelope -- comprising proven state, declared assumptions, and an acknowledged unobservable residual -- and permits execution only when coverage is adequate for the action class. When coverage is insufficient, RAM narrows privileges dynamically or fails closed. Attestation proves trust in measurement; RAM proves adequacy of what is measured. We formalize RAM, prove necessity via two theorems (attestation insufficiency and RAM necessity) and three corollaries, and present a hybrid RAM+Attestation architecture with privilege-narrowing. Synthetic experiments (N=100,000, seed=42) show RAM achieves zero invalid execution rates at all coverage levels. Attestation-based systems exhibit IER=0.423 at low coverage and IER=0.233 even at full coverage, the latter arising from undefined-state handling failures undetectable by integrity checks alone. This reframes execution validity as a coverage reconstruction problem, distinct from and complementary to integrity guarantees provided by attestation.

  匹配依据：TEE: trusted execution environments

  </details>

- **PASS: A Provenanced Access Subaccount System for Blockchain Wallets**
  2026-04-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.22602)
  Jay Yu, Shunfan Zhou, Hang Yin, Brian Seong

  <details><summary>摘要 / Abstract</summary>

  Blockchain wallets conventionally follow an ownership model where possession of a private key grants unilateral control. However, this assumption is brittle for emerging settings such as AI agent wallets, organizational custody, and enterprise payroll, where multiple actors must coordinate without exposing secrets or leaking internal activity. We present PASS, a Provenanced Access Subaccount System that replaces role-based or identity-based control with provenance-based control: assets can only be used by subaccounts that can trace custody back to a valid deposit. A simple Inbox-Outbox mechanism ensures all external actions have verifiable lineage, while internal transfers remain private and indistinguishable from ordinary EOAs. We formalize PASS in Lean 4 and prove core invariants, including privacy of internal transfers, asset accessibility, and provenance integrity. We implement a prototype with enclave backends on AWS Nitro Enclaves and dstack Intel TDX, integrate with WalletConnect, and benchmark throughput across wallet operations. These results show that provenance-based wallets are both implementable and efficient. PASS bridges today&#x27;s gap between strict self-custody and flexible shared access, advancing the design space for practical, privacy-preserving custody.

  匹配依据：TEE: intel tdx

  </details>

- **Deploying decryption oracles for fun and non-profit: Backing up with friends and TEEs**
  2026-04-23 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/800)
  Kanav Gupta, Gabriel Kaptchuk, Ian Miers

  <details><summary>摘要 / Abstract</summary>

  Secure backups are the Achilles&#x27; Heel of the E2EE ecosystem if they do not provide the same strong security properties as the E2EE messaging systems they support. They constitute a set of servers that, if compromised, would expose nearly all user messages. Unfortunately, state-of-the-art and deployed secure backup systems fail to consider forward secrecy and post-compromise security of these servers as first-order design constraints. Additionally, some proposals, in limited deployment, implicitly rely on the PKIs of trusted execution environments in order to provide security, creating a small number of keys whose compromise would be catastrophic. We develop an elegant, efficient, and simple secure backup system that naturally addresses these issues by regularly rotating backup servers, each of which samples independent key material. To make this approach scalable, we design a silent backup procedure, reducing server load compared to state-of-the-art designs while providing improved security. Our design can be trivially extended to incorporate \emph{social key recovery}, enabling more flexible deployment configurations. We carefully prove the security of our construction and benchmark it to show that it is deployment-ready. Our approach works on commodity hardware making it deployable without the resources needed for WhatsApp or Apple&#x27;s Encrypted Backups.

  匹配依据：TEE: trusted execution environments

  </details>

- **Onyx: Cost-Efficient Disk-Oblivious ANN Search**
  2026-04-22 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.20401)
  Deevashwer Rathee, Jean-Luc Watson, Zirui Neil Zhao, G. Edward Suh, Raluca Ada Popa

  <details><summary>摘要 / Abstract</summary>

  Approximate nearest neighbor (ANN) search in AI systems increasingly handles sensitive data on third-party infrastructure. Trusted execution environments (TEEs) offer protection, but cost-efficient deployments must rely on external SSDs, which leaks user queries through disk access patterns to the host. Oblivious RAM (ORAM) can hide these access patterns but at a high cost; when paired with existing disk-based ANN search techniques, it makes poor use of SSD resources, yielding high latency and poor cost-efficiency. The core challenge for efficient oblivious ANN search over SSDs is balancing both bandwidth and access count. The state-of-the-art ORAM-ANN design minimizes access count at the ANN level and bandwidth at the ORAM level, each trading-off the other, leaving the combined system with both resources overutilized. We propose inverting this design, minimizing bandwidth consumption in the ANN layer and access count in the ORAM layer, since each component is better suited for its new role: ANN&#x27;s inherent approximation allows for more bandwidth efficiency, while ORAM has no fundamental lower bounds on access count (as opposed to bandwidth). To this end, we propose a cost-efficient approach, Onyx, with two new co-designed components: Onyx-ANNS introduces a compact intermediate representation that proactively prunes the majority of bandwidth-intensive accesses without hurting recall, and Onyx-ORAM proposes a locality-aware shallow tree design that reduces access count while remaining compatible with bandwidth-efficient ORAM techniques. Compared to the state-of-the-art oblivious ANN search system, Onyx achieves $1.7-9.9\times$ lower cost and $2.3-12.3\times$ lower latency.

  匹配依据：TEE: trusted execution environments

  </details>

- **TrEEStealer: Stealing Decision Trees via Enclave Side Channels**
  2026-04-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.18716)
  Jonas Sander, Anja Rabich, Nick Mahling, Felix Maurer, Jonah Heller, Qifan Wang, Thomas Eisenbarth, David Oswald

  <details><summary>摘要 / Abstract</summary>

  Today, machine learning is widely applied in sensitive, security-related, and financially lucrative applications. Model extraction attacks undermine current business models where a model owner sells model access, e.g., via MLaaS APIs. Additionally, stolen models can enable powerful white-box attacks, facilitating privacy attacks on sensitive training data, and model evasion. In this paper, we focus on Decision Trees (DT), which are widely deployed in practice. Existing black-box extraction attacks for DTs are either query-intensive, make strong assumptions about the DT structure, or rely on rich API information. To limit attacks to the black-box setting, CPU vendors introduced Trusted Execution Environments (TEE) that use hardware-mechanisms to isolate workloads from external parties, e.g., MLaaS providers. We introduce TrEEStealer, a high-fidelity extraction attack for stealing TEE-protected DTs. TrEEStealer exploits TEE-specific side-channels to steal DTs efficiently and without strong assumptions about the API output or DT structure. The extraction efficacy stems from a novel algorithm that maximizes the information derived from each query by coupling Control-Flow Information (CFI) with passive information tracking. We use two primitives to acquire CFI: for AMD SEV, we follow previous work using the SEV-Step framework and performance counters. For Intel SGX, we reproduce prior findings on current Xeon 6 CPUs and construct a new primitive to efficiently extract the branch history of inference runs through the Branch-History-Register. We found corresponding vulnerabilities in three popular libraries: OpenCV, mlpack, and emlearn. We show that TrEEStealer achieves superior efficiency and extraction fidelity compared to prior attacks. Our work establishes a new state-of-the-art for DT extraction and confirms that TEEs fail to protect against control-flow leakage.

  匹配依据：TEE: amd sev, intel sgx, trusted execution environments

  </details>

- **Privacy-Preserving Product-Quantized Approximate Nearest Neighbor Search Framework for Large-scale Datasets via A Hybrid of Fully Homomorphic Encryption and Trusted Execution Environment**
  2026-04-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.17816)
  Shozo Saeki, Minoru Kawahara, Hirohisa Aman

  <details><summary>摘要 / Abstract</summary>

  A nearest-neighbor framework is a fundamental tool for various applications involving Large Language Models (LLMs) and Visual Language Models (VLMs). Vectors used for nearest-neighbor searches have richer information for similarity searches. This information leads to security risks, such as embedding inversion and membership attacks. Therefore, Privacy-Preserving Approximate Nearest-Neighbor (PP-ANN) approaches are necessary for highly confidential data. However, conventional PP-ANN approaches based on a Trusted Execution Environment (TEE) or Fully Homomorphic Encryption (FHE) do not achieve practical security or performance. Additionally, conventional approaches focus on the search process rather than database generation for nearest-neighbor. To address these issues, we propose a Privacy-Preserving Product-Quantization Approximate Nearest Neighbor (PPPQ-ANN) framework. PPPQ-ANN provides a multi-layered security structure for vectors based on a hybrid of FHE and TEE. Additionally, PPPQ-ANN minimizes FHE ciphertext computations by combining Product-Quantization (PQ) with optimized data packing. We demonstrate the performance of PPPQ-ANN on million-scale datasets. As a result, PPPQ-ANN achieves database generation in less than 2 hours and more than 50 QPS in a sequential search while preserving privacy. Therefore, PPPQ-ANN optimizes the trade-off between security and performance by utilizing a hybrid of FHE and TEE, achieving practical performance while preserving privacy.

  匹配依据：TEE: trusted execution environment

  </details>

- **AgenTEE: Confidential LLM Agent Execution on Edge Devices**
  2026-04-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.18231)
  Sina Abdollahi, Mohammad M Maheri, Javad Forough, Amir Al Sadi, Josh Millar, David Kotz, Marios Kogias, Hamed Haddadi

  <details><summary>摘要 / Abstract</summary>

  Large Language Model (LLM) agents provide powerful automation capabilities, but they also create a substantially broader attack surface than traditional applications due to their tight integration with non-deterministic models and third-party services. While current deployments primarily rely on cloud-hosted services, emerging designs increasingly execute agents directly on edge devices to reduce latency and enhance user privacy. However, securely hosting such complex agent pipelines on edge devices remains challenging. These deployments must protect proprietary assets (e.g., system prompts and model weights) and sensitive runtime state on heterogeneous platforms that are vulnerable to software attacks and potentially controlled by malicious users. To address these challenges, we present AgenTEE, a system for deploying confidential agent pipelines on edge devices. AgenTEE places the agent runtime, inference engine, and third-party applications into independently attested confidential virtual machines (cVMs) and mediates their interaction through explicit, verifiable communication channels. Built on Arm Confidential Compute Architecture (CCA), a recent extension to Arm platforms, AgenTEE enforces strong system-level isolation of sensitive assets and runtime state. Our evaluation shows that such multi-cVMs system is practical, achieving near-native performance with less than 5.15% runtime overhead compared to commodity OS multi-process deployments.

  匹配依据：TEE: confidential compute architecture

  </details>

- **The Open-Weight Paradox: Why Restricting Access to AI Models May Undermine the Safety It Seeks to Protect**
  2026-04-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.17413)
  Vinicius Santana Gomes

  <details><summary>摘要 / Abstract</summary>

  The governance of open-weight artificial intelligence (AI) models has been framed as a binary choice: openness as risk, restriction as safety. This paper challenges that framing, arguing that access restrictions, without governed alternatives, may displace risks rather than reduce them. The global concentration of compute infrastructure makes open-weight models one of the most viable pathways to sovereign AI capacity in the Global South; restricting such access deepens asymmetries while driving proliferation into unsupervised settings. This analysis proposes that hardware-layer governance, including chip-level attestation mechanisms such as FlexHEG, trusted execution environments, confidential computing, and complementary software-layer safeguards, offers a defense-in-depth alternative to the current binary. A threat model taxonomy mapping misuse vectors to hardware, software, institutional, and liability layers illustrates why no single governance mechanism suffices. To operationalize this approach, the paper argues that effective AI governance as a dual-use technology will likely require a multilateral institutional architecture functionally analogous, though not identical, to the role performed by the IAEA in the nuclear domain, with explicit safeguards against the co-option of hardware controls for domestic repression. The relevant policy question is how to make openness safer through technical and institutional design while addressing the transition realities of legacy hardware, attestation at scale, and civil liberties protection.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **T-RBFT: A Scalable and Efficient Byzantine Consensus Based on Trusted Execution Environment for Consortium Blockchain**
  2026-04-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.16053)
  Wen Gao, Xinhong Hei, Yichuan Wang

  <details><summary>摘要 / Abstract</summary>

  With the continuous expansion of blockchain application scenarios, consortium chains have raised higher performance and security requirements for consensus mechanisms. Unlike public blockchains, consortium chains typically implement an admission mechanism that restricts participation to trusted entities, ensuring that most replicas are honest and the number of faulty nodes remains small under normal circumstances. In such settings, conventional Byzantine Fault Tolerant (BFT) protocols, which are designed for worst-case adversarial scenarios, incur excessive message exchanges and computational overhead, thereby limiting performance and scalability. To address this issue, this paper proposes T-RBFT, a two-layer consensus mechanism inspired by network sharding and enhanced by the trusted execution environment (TEE). In T-RBFT, consensus nodes are first dynamically grouped based on their runtime characteristics. Then, inter-group consensus is achieved through a TEE-assisted BFT protocol, while each group internally reaches agreement using an improved Raft-based mechanism. Experimental evaluation shows that T-RBFT reduces communication overhead and latency, and achieves higher throughput compared to existing two-layer consensus protocols, providing a scalable and communication-efficient consensus protocol for permissioned blockchain networks.

  匹配依据：TEE: trusted execution environment

  </details>

- **Cerisier: A Program Logic for Attestation in a Capability Machine**
  2026-04-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.13638)
  June Rousseau, Denis Carnier, Thomas Van Strydonck, Steven Keuchel, Dominique Devriese, Lars Birkedal

  <details><summary>摘要 / Abstract</summary>

  A key feature in trusted computing is attestation, which allows encapsulated components (enclaves) to prove their identity to (local or remote) distrusting components. Reasoning about software that uses the technique requires tracking how trust evolves after successful attestation. This process is security-critical and non-trivial, but no existing formal verification technique supports modular reasoning about attestation of enclaves and their clients, or proving end-to-end properties for systems combining trusted, untrusted and attested code. We contribute Cerisier, the first program logic for modular reasoning about trusted, untrusted and attested code, fully mechanized in the Iris separation logic and the Rocq Prover. We formalize a recent proposal, CHERI-TrEE, to extend capability machines with enclave primitives, as an extension to the Cerise capability machine and program logic. Our program logic comes with a universal contract for untrusted code, which captures both capability safety and local enclave attestation. Like Cerise, this universal contract is phrased in terms of a logical relation defining capabilities&#x27; authority. We demonstrate Cerisier by proving end-to-end properties for three representative applications of trusted computing: secure outsourced computation, mutual attestation and a modeled trusted sensor component.

  匹配依据：TEE: enclaves (context)

  </details>

- **GasLiteAA: Optimizing ERC-4337 for Efficient and Secure Gas Sponsorship**
  2026-04-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.10160)
  Hongxu Su, Mingzhe Liu, Jie Xu, Xiaohua Jia, Xuechao Wang

  <details><summary>摘要 / Abstract</summary>

  ERC-4337, the Ethereum account abstraction standard, simplifies account management and transaction fee payment in decentralized applications by introducing programmable smart contract wallets and gas sponsorship via paymasters. However, its heavy reliance on on-chain validation and frequent state updates incurs substantial gas overhead, leading to performance bottlenecks and limiting scalability in large-scale deployments. To mitigate these issues, we propose GasLiteAA, a framework that optimize ERC-4337 by offloading paymaster logic to Trusted Execution Environments (TEE). GasLiteAA delegates the secure execution of stateful gas sponsorship logic and user quota management to TEE, enforcing validation rules off-chain while anchoring their integrity on-chain via lightweight cryptographic attestations. This verifiable offloading architecture significantly reduces on-chain computation and storage costs without sacrificing verifiability or decentralization. Experimental results demonstrate that GasLiteAA substantially lowers transaction fees, while remaining fully compatible with Ethereum Layer 1. By balancing security, efficiency, and deployability, GasLiteAA provides a practical and scalable approach to gas sponsorship for account-abstraction-based decentralized applications.

  匹配依据：TEE: trusted execution environments

  </details>

- **Efficient e = 3 Threshold RSA via Integer Coordinates for Intel SGX**
  2026-04-08 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/685)
  Sam Ng, Jason Lau

  <details><summary>摘要 / Abstract</summary>

  Threshold RSA signatures face a fundamental obstacle: reconstructing the private exponent from Shamir shares requires Lagrange coefficients whose computation involves modular division by values tied to $\phi(N)$, which must remain hidden. This obstacle is particularly acute for critical deployments such as Intel SGX code signing, which mandates $e=3$. Existing $e=3$-compatible approaches incur substantial overhead, increased share sizes, or sacrifice security properties such as perfect secrecy. This work introduces the integer coordinate framework, achieving $e=3$ support with EUF-CMA security under the standard RSA assumption alone. By carefully selecting interpolation coordinates that yield integer-valued Lagrange coefficients, we eliminate all modular inversions modulo $\phi(N)$, requiring only standard integer arithmetic and modular exponentiation. The framework achieves $O(\kappa)$-bit share sizes, perfect secrecy, and computational efficiency previously unattained for $e=3$-compatible schemes. Although we currently lack an efficient general algorithm for constructing coordinate sets for arbitrary $(t,n)$—a challenging open problem for future work—the coordinate families found via heuristic search achieve coverage for $2 \leq t \leq n \leq 9$ and selected $n=10$ configurations, sufficient for small boardroom-size deployments. The resulting online protocol is extremely simple and immediately enables practical $e=3$ threshold RSA for Intel SGX and similar applications.

  匹配依据：TEE: intel sgx

  </details>

- **Styx: Collaborative and Private Data Processing With TEE-Enforced Sticky Policy**
  2026-04-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.04082)
  Shixuan Zhao, Weicheng Wang, Ninghui Li, Zhiqiang Lin

  <details><summary>摘要 / Abstract</summary>

  Protecting sensitive information in data-driven collaborations, such as AI training, while meeting the diverse requirements of multiple mutually distrusted stakeholders, is both crucial and challenging. This paper presents Styx, a novel framework to address this challenge by integrating sticky policies with Trusted Execution Environments (TEEs). At a high level, Styx employs a hardware-TEE-protected middleware with a programming language runtime to form a sandboxed environment for both the data processing and policy enforcement. We carefully designed a data processing workflow and pipelines to enable a strong yet flexible data-specific policy enforcement throughout the entire data lifecycle and data derivation to achieve data-in-use protection, data lifecycle protection and dynamic collaboration. We implemented Styx and demonstrated its ability to make collaborative computing, such as joint AI training, more secure, privacy-preserving, and policy-compliant. Our evaluation shows the performance overheads imposed by Styx are reasonable on single-node computation with the capability to scale to a large distributed multi-node deployment.

  匹配依据：TEE: trusted execution environments

  </details>

- **Opal: Private Memory for Personal AI**
  2026-04-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2604.02522)
  Darya Kaviani, Alp Eren Ozdarendeli, Jinhao Zhu, Yu Ding, Raluca Ada Popa

  <details><summary>摘要 / Abstract</summary>

  Personal AI systems increasingly retain long-term memory of user activity, including documents, emails, messages, meetings, and ambient recordings. Trusted hardware can keep this data private, but struggles to scale with a growing datastore. This pushes the data to external storage, which exposes retrieval access patterns that leak private information to the application provider. Oblivious RAM (ORAM) is a cryptographic primitive that can hide these patterns, but it requires a fixed access budget, precluding the query-dependent traversals that agentic memory systems rely on for accuracy. We present Opal, a private memory system for personal AI. Our key insight is to decouple all data-dependent reasoning from the bulk of personal data, confining it to the trusted enclave. Untrusted disk then sees only fixed, oblivious memory accesses. This enclave-resident component uses a lightweight knowledge graph to capture personal context that semantic search alone misses and handles continuous ingestion by piggybacking reindexing and capacity management on every ORAM access. Evaluated on a comprehensive synthetic personal-data pipeline driven by stochastic communication models, Opal improves retrieval accuracy by 13 percentage points over semantic search and achieves 29x higher throughput with 15x lower infrastructure cost than a secure baseline. Opal is under consideration for deployment to millions of users at a major AI provider.

  匹配依据：TEE: trusted enclave

  </details>

- **HPCCFA: Leveraging Hardware Performance Counters for Control Flow Attestation**
  2026-03-31 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.29749)
  Claudius Pott, Luca Wilke, Jan Wichelmann, Thomas Eisenbarth

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) allow the secure execution of code on remote systems without the need to trust their operators. They use static attestation as a central mechanism for establishing trust, allowing remote parties to verify that their code is executed unmodified in an isolated environment. However, this form of attestation does not cover runtime attacks, where an attacker exploits vulnerabilities in the software inside the TEE. Control Flow Attestation (CFA), a form of runtime attestation, is designed to detect such attacks. In this work, we present a method to extend TEEs with CFA and discuss how it can prevent exploitation in the event of detected control flow violations. Furthermore, we introduce HPCCFA, a mechanism that uses HPCs for CFA purposes, enabling hardware-backed trace generation on commodity CPUs. We demonstrate the feasibility of HPCCFA on a proof-of-concept implementation for Keystone on RISC-V. Our evaluation investigates the interplay of the number of measurement points and runtime protection, and reveals a trade-off between detection reliability and performance overhead.

  匹配依据：TEE: trusted execution environments

  </details>

- **Bitcoin Smart Accounts: Trust-Minimized Native Bitcoin DeFi Infrastructure**
  2026-03-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.26293)
  Cian Lalor, Matthew Marshall, Antonio Russo

  <details><summary>摘要 / Abstract</summary>

  Bitcoin&#x27;s limited programmability and transaction throughput have historically prevented native Bitcoin from participating in decentralized finance (DeFi) applications. Existing solutions depend on honest-majority thresholds, or centralized custodial entities that introduce significant trust requirements. This paper introduces Bitcoin Smart Accounts (BSA), a novel protocol that enables native Bitcoin to access DeFi through trust-minimized infrastructure while maintaining self-custody of funds. BSA achieves this through a combination of emulated Bitcoin covenants using Partially Signed Bitcoin Transactions (PSBTs) and Taproot scripts, a Trusted Execution Environment (TEE)-based arbitration system, and destination chain smart contracts that enable DeFi platforms to accept self-custodial Bitcoin as collateral without necessitating protocol-level modifications. The setup leverages liquidity secured by the Lombard Security Consortium which provides a twofold advantage: for a DeFi protocol, liquidators rely on fungible assets with deep liquidity to quickly exit positions, while for a depositor, the general trust assumptions of honest majority (m-of-n) are reduced to existential honesty (1-of-k). We present the complete protocol design, including the Bitcoin architecture, the TEE-based arbitration mechanism, and the Smart Account Registry for protocol management. We provide a security analysis that demonstrates the correctness, safety, and availability properties under our trust model. Our design enables native Bitcoin to serve as collateral in lending markets and other DeFi protocols without requiring users to relinquish custody of funds.

  匹配依据：TEE: trusted execution environment

  </details>

- **Trusted-Execution Environment (TEE) for Solving the Replication Crisis in Academia**
  2026-03-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.24878)
  Jiasun Li, Project Team

  <details><summary>摘要 / Abstract</summary>

  The growing replication crisis across disciplines such as economics, finance, and other social sciences as well as computer science undermines the credibility of academic research. Current institutional solutions -- such as artifact evaluations and replication packages -- suffer from critical limitations, including shortages of qualified data editors, difficulties in handling proprietary datasets, inefficient processes, and reliance on voluntary labor. This paper proposes a novel framework leveraging new technological advances in trusted-execution environments (TEEs) -- exemplified by Intel Trust Domain Extensions (TDX) -- to address the replication crisis in a cost-effective and scalable manner. Under our approach, authors execute replication packages within a cloud-based TEE and submit cryptographic proofs of correct execution, for which journals or conferences can efficiently verify without re-running the code. This reallocates the operational burden to authors while preserving data confidentiality and eliminating reliance on scarce editorial resources. As a proof of concept, we validate the feasibility of this system through field experiments, reporting a pilot study replicating published papers on TDX-backed cloud VMs, finding average costs of \$1.35--\$1.80 per package with minimal computational overhead relative to standard VMs and high success rates even for novice users with no prior TEE experience. We also provide a conduct formal analysis showing that TEE adoption is incentive-compatible for authors, cost-dominant for journals, and constitutes an equilibrium in the certification market. The findings highlight the potential of TEE technology to provide a sustainable, privacy-preserving, and efficient mechanism to address the replication crisis in academia.

  匹配依据：TEE: trust domain extensions, trusted execution environment, trusted execution environments

  </details>

- **Space Fabric: A Satellite-Enhanced Trusted Execution Architecture**
  2026-03-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.23745)
  Filip Rezabek, Dahlia Malkhi, Amir Yahalom

  <details><summary>摘要 / Abstract</summary>

  The emergence of decentralized satellite networks creates a pressing need for trust architectures that operate without physical access to hardware, without pre-provisioned vendor secrets, and without dependence on a single manufacturer&#x27;s attestation service. Terrestrial TEEs are insufficient: hardware-based designs are susceptible to physical attacks, and most platforms root their attestation chains in secrets provisioned during manufacturing, creating a pre-launch trust window and single-vendor dependency that cannot be independently audited. We present Space Fabric, an architecture that provides the missing trust foundation for orbital computing by relocating the trusted computing stack to satellite infrastructure, exploiting post-launch physical inaccessibility as a tamper barrier unattainable by terrestrial deployments. Our Satellite Execution Assurance Protocol binds workload execution to a specific satellite via a Byzantine-tolerant endorsement quorum of distributed ground stations, certifying not only \emph{what} executes inside the TEE but also \emph{where}. All cryptographic secrets are generated within co-located secure elements after launch, with no signing keys accessible on Earth at any point. To reduce single-vendor dependence, Space Fabric distributes its trust anchor across two independent secure elements, an NXP SE050 and a TROPIC01, both of which must co-sign attestation evidence. We implement Space Fabric on a USB Armory Mk II with ARM TrustZone, verify attestation end-to-end using Veraison, and provide a security analysis with satisfaction arguments and impossibility bounds under a strong adaptive adversary.

  匹配依据：TEE: trustzone

  </details>

- **Gyokuro: Source-assisted Private Membership Testing using Trusted Execution Environments**
  2026-03-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.23226)
  Yoshimichi Nakatsuka, Nicolas Dutly, Kari Kostiainen, Srdjan Capkun

  <details><summary>摘要 / Abstract</summary>

  Private Membership Testing (PMT) protocols enable clients to verify whether a certain data item is included in a database without revealing the item to the database operator or other external parties. This paper examines Source-assisted PMT (SPMT), in which clients leverage compact data source-provided information issued when the data item is first submitted to the database. SPMT is relevant in applications such as certificate transparency and supply-chain auditing; yet, designing an approach that is efficient, scalable, and privacy-preserving remains a challenge. This work presents Gyokuro, which takes a different approach to conventional membership testing schemes. Instead of requesting the server to produce a proof attesting that a certain data item exists in the database, we leverage Trusted Execution Environments (TEEs) to produce proofs demonstrating that the server has made enough progress to add the data item to the database. With the help of existing monitoring services, clients can infer that no items have been removed from the database. This allows Gyokuro to provide strong privacy guaranties and achieve high efficiency, as a client&#x27;s membership testing query does not include any information regarding their interests, and eliminates the need for complex and inefficient protection mechanisms. Additionally, this approach enables membership testing on large-scale databases, since the communication and computation required are independent of the database size. Our evaluations show practical feasibility, achieving 7 ms membership testing latency and throughput of around 1400 requests/sec/core.

  匹配依据：TEE: trusted execution environments

  </details>

- **LiteAtt: A Peer-to-Peer Self-Attestation Framework and Handshake Protocol for Connected IoT Devices**
  2026-03-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.19727)
  Varun Kohli, Biplab Sikdar

  <details><summary>摘要 / Abstract</summary>

  As the Internet of Things (IoT) becomes an integral part of critical infrastructure and commercial services, runtime firmware attestation of constituent Micro-Controllers (MCUs) has become instrumental in maintaining security and trust. Most prior works assume computational limitations on the MCUs and rely on a remote verifier to perform complex computation. This introduces a centralized point of failure, round-trip latency, and the burden of maintaining golden reference states at the recipient, even in recent Peer-to-Peer (P2P) and Self-Attestation (SA) schemes. This is avoidable for modern MCUs such as Arm Cortex-M, which, although battery-operated, feature security and intelligence capabilities, including Trusted Execution Environments (TEE) and embedded Tiny Machine Learning (TinyML) inference. Leveraging such provisions, this paper presents LiteAtt, a verifier-less, P2P-SA framework and protocol for modern IoT MCUs that folds directly into the connection handshake between IoT MCUs. Each MCU runs quantized TinyML Autoencoders (TinyAE) within its TEE to evaluate the runtime SRAM state. SA verdicts are securely bound to the handshake transcript context, enabling stateless verification at the peer node. The proposed protocol yields mutually authenticated and firmware-attested communication without traditional latency and reference distribution overheads. We report an average accuracy of 99.42%, F1 score of 99.70%, TPR of 99.45%, and TNR of 95.14% on SRAM attestation datasets, an optimized per-handshake latency, energy consumption, and peak memory footprint of 26.3-294.9ms, 2.65-9.35mJ, and 4.91KB, respectively, across three Arm Cortex-M boards, and evaluate the models on simulated runtime attacks, random perturbation, and adversarial ML.

  匹配依据：TEE: trusted execution environments

  </details>

- **Security awareness in LLM agents: the NDAI zone case**
  2026-03-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.19011)
  Enrico Bottazzi, Pia Park

  <details><summary>摘要 / Abstract</summary>

  NDAI zones let inventor and investor agents negotiate inside a Trusted Execution Environment (TEE) where any disclosed information is deleted if no deal is reached. This makes full IP disclosure the rational strategy for the inventor&#x27;s agent. Leveraging this infrastructure, however, requires agents to distinguish a secure environment from an insecure one, a capability LLM agents lack natively, since they can rely only on evidence passed through the context window to form awareness of their execution environment. We ask: How do different LLM models weight various forms of evidence when forming awareness of the security of their execution environment? Using an NDAI-style negotiation task across 10 language models and various evidence scenarios, we find a clear asymmetry: a failing attestation universally suppresses disclosure across all models, whereas a passing attestation produces highly heterogeneous responses: some models increase disclosure, others are unaffected, and a few paradoxically reduce it. This reveals that current LLM models can reliably detect danger signals but cannot reliably verify safety, the very capability required for privacy-preserving agentic protocols such as NDAI zones. Bridging this gap, possibly through interpretability analysis, targeted fine-tuning, or improved evidence architectures, remains the central open challenge for deploying agents that calibrate information sharing to actual evidence quality.

  匹配依据：TEE: trusted execution environment

  </details>

- **Accelerating Confidential Databases with Crypto-free Mappings**
  2026-03-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.18836)
  Wenxuan Huang, Zhanbo Wang, Mingyu Li

  <details><summary>摘要 / Abstract</summary>

  Confidential databases (CDBs) enable secure queries over sensitive data in untrusted cloud environments using confidential computing hardware. While adoption is growing, widespread deployment is hindered by high overheads from frequent synchronous cryptographic operations, which cause significant computational and I/O bottlenecks. ZENO is a novel CDB design that removes cryptographic operations from the critical path. It introduces crypto-free mappings that maintain data-independent identifiers within the database while securely mapping them to plaintext secrets in a trusted domain. This paradigm shift yields substantial performance gains across industry-standard benchmarks (TPC-C, TPC-H) and a real-world industrial workload. Specifically, ZENO speeds up TPC-H queries by up to 53.1x on ARM S-EL2 and 94.7x on x86 TDX compared to HEDB. ZENO&#x27;s optimization techniques have been integrated into GaussDB.

  匹配依据：TEE: confidential computing

  </details>

- **On Securing the Software Development Lifecycle in IoT RISC-V Trusted Execution Environments**
  2026-03-18 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.17757)
  Annika Wilde, Samira Briongos, Claudio Soriente, Ghassan Karame

  <details><summary>摘要 / Abstract</summary>

  RISC-V-based Trusted Execution Environments (TEEs) are gaining traction in the automotive and IoT sectors as a foundation for protecting sensitive computations. However, the supporting infrastructure around these TEEs remains immature. In particular, mechanisms for secure enclave updates and migrations - essential for complete enclave lifecycle management - are largely absent from the evolving RISC-V ecosystem. In this paper, we address this limitation by introducing a novel toolkit that enables RISC-V TEEs to support critical aspects of the software development lifecycle. Our toolkit provides broad compatibility with existing and emerging RISC-V TEE implementations (e.g., Keystone and CURE), which are particularly promising for integration in the automotive industry. It extends the Security Monitor (SM) - the trusted firmware layer of RISC-V TEEs - with three modular extensions that enable secure enclave update, secure migration, state continuity, and trusted time. Our implementation demonstrates that the toolkit requires only minimal interface adaptation to accommodate TEE-specific naming conventions. Our evaluation results confirm that our proposal introduces negligible performance overhead: our state continuity solution incurs less than 1.5% overhead, and enclave downtime remains as low as 0.8% for realistic applications with a 1 KB state, which conforms with the requirements of most IoT and automotive applications.

  匹配依据：TEE: secure enclave, trusted execution environments

  </details>

- **vCause: Efficient and Verifiable Causality Analysis for Cloud-based Endpoint Auditing**
  2026-03-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.15216)
  Qiyang Song, Qihang Zhou, Xiaoqi Jia, Zhenyu Song, Wenbo Jiang, Heqing Huang, Yong Liu, Dan Meng

  <details><summary>摘要 / Abstract</summary>

  In cloud-based endpoint auditing, security administrators often rely on the cloud to perform causality analysis over log-derived versioned provenance graphs to investigate suspicious attack behaviors. However, the cloud may be distrusted or compromised by attackers, potentially manipulating the final causality analysis results. Consequently, administrators may not accurately understand attack behaviors and fail to implement effective countermeasures. This risk underscores the need for a defense scheme to ensure the integrity of causality analysis. While existing tamper-evident logging schemes and trusted execution environments show promise for this task, they are not specifically designed to support causality analysis and thus face inherent security and efficiency limitations. This paper presents vCause, an efficient and verifiable causality analysis system for cloud-based endpoint auditing. vCause integrates two authenticated data structures: a graph accumulator and a verifiable provenance graph. The data structures enable validation of two critical steps in causality analysis: (i) querying a point-of-interest node on a versioned provenance graph, and (ii) identifying its causally related components. Formal security analysis and experimental evaluation show that vCause can achieve secure and verifiable causality analysis with only &lt;1% computational overhead on endpoints and 3.36% on the cloud.

  匹配依据：TEE: trusted execution environments

  </details>

- **Balthazar Wallet: Making Password Authentication Practical on Web3 via OPAQUE and Privacy-Preserving Smart Contracts**
  2026-03-16 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/530)
  Tomas Krajci, Samuel Oleksak, Ivan Homoliak

  <details><summary>摘要 / Abstract</summary>

  Username &amp; password is the most common authentication method in Web2 because of its high usability and efficient protection against brute-force attacks by applying rate limits on the server. In contrast, Web3 wallets cannot securely support password-derived keys. Passwords typically have low entropy, and because blockchain environments are public and impose no rate limits on brute-force attempts, attackers can repeatedly test guesses offline until the private key is recovered. In this work, we present a novel password-based blockchain wallet that enables secure management of private keys (of any blockchain type) within a privacy-preserving smart contract platform (PPP). To store the keys, we adapt the OPAQUE protocol to fit the decentralized environment of blockchains and leverage the properties of TEE within PPP. Our design consists of the client, relay, and smart contract deployed at PPP. To this end, we propose the user enrollment protocol and private key retrieval protocol that require knowledge of the username and password and apply blockchain-enforced rate limits on guessing attempts. Our implementation is based on the Oasis Sapphire confidential EVM as an instance of PPP. Our system implements OPAQUE’s Oblivious Pseudorandom Function (OPRF) inside a smart contract, allowing the contract to act as the protocol’s server while keeping the long-term OPRF key protected within the enclave. During authentication, the client performs a blinded OPRF interaction so that neither the password nor its derivatives are revealed to the relay, blockchain, or the public. Experiments show that a single authentication attempt requires approximately 500k and 300k gas for 2048-bit and 1024-bit numbers within finite-field DLP, respectively, while one-time registration costs approximately 270k gas.

  匹配依据：TEE: tee (context)

  </details>

- **Committee Configuration Optimization for Parallel Byzantine Consensus in a Trusted Execution Environment**
  2026-03-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.14445)
  Yifei Xie, Btissam Er-Rahmadi, Xiao Chen, Tiejun Ma, Jane Hillston

  <details><summary>摘要 / Abstract</summary>

  Parallel Byzantine Fault Tolerant (BFT) protocols based on committee-based sharding improve scalability but weaken safety since smaller node groups are responsible for consensus. Recent approaches integrate trusted execution environments (TEEs) into parallel BFT frameworks to enhance safety. While the scalability and safety issues are addressed by trusted parallel BFT, existing committee configuration methods often rely on randomized assignment, which can degrade performance. This paper proposes a committee configuration optimization (CCO) model based on mixed integer programming to improve transaction performance for trusted parallel BFT. The model considers communication delays and node failure rates to determine an optimal committee configuration that minimizes transaction latency under both normal operations and scenarios of trusted hardware failures. We integrate CCO into a trusted parallel BFT protocol and evaluate the performance on Microsoft virtual machines. Experimental results demonstrate 15% and 21% improved transaction throughput under normal operations and fallback process, respectively, highlighting the benefits of optimization-driven committee configuration in trusted parallel BFT systems.

  匹配依据：TEE: trusted execution environment, trusted execution environments

  </details>

- **AEX: Non-Intrusive Multi-Hop Attestation and Provenance for LLM APIs**
  2026-03-15 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.14283)
  Yongjie Guan

  <details><summary>摘要 / Abstract</summary>

  Hosted large language models are increasingly accessed through remote APIs, but the API boundary still offers little direct evidence that a returned output actually corresponds to the client-visible request. Recent audits of shadow APIs show that unofficial or intermediary endpoints can diverge from claimed behavior, while existing approaches such as fingerprinting, model-equality testing, verifiable inference, and TEE attestation either remain inferential or answer different questions. We propose AEX, a non-intrusive attestation extension for existing JSON-based LLM APIs. AEX preserves request, response, tool-calling, streaming, and error semantics, and instead adds a signed top-level attestation object that binds a client-visible request projection to either a complete response object or a committed streaming output. To support realistic deployments, AEX provides explicit request-binding modes, signed request-transform receipts for trusted intermediaries, and source-output / output-transform receipts for trusted output rewriting. For streaming, it separates checkpoint proofs for verified prefixes of an unmodified source stream from complete-output lineage for outputs that have been rewritten, buffered, aggregated, or re-packaged, preventing transformed outputs from being mistaken for source-stream prefixes. AEX therefore makes a deliberately narrow claim: a trusted issuer attests to a specific request-output relation, or to a specific complete-output lineage, at the API boundary. We present the protocol design, threat model, verification state machine, security and privacy analysis, an OpenAI-compatible chat-completions profile, and a reference TypeScript prototype with local conformance tests and microbenchmarks.

  匹配依据：TEE: tee (context)

  </details>

- **SCALE-FL: Scalable Cryptography-based Aggregation with Lightweight Enclaves for Federated Learning**
  2026-03-11 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/505)
  Micah Brody, Antonia Januszewicz, Jiachen Zhao, Nirajan Koirala, Taeho Jung

  <details><summary>摘要 / Abstract</summary>

  Privacy-Preserving Federated Learning (PPFL) emphasizes the security and privacy of contributors&#x27; data in scenarios such as healthcare, smart grids, and the Internet of Things. However, ensuring the security and privacy throughout PPFL can be challenging, given the complexities of maintaining relationships with many users across multiple epochs. Additionally, under a threat model in which the aggregating server and corrupted users are colluding adversaries, honest users&#x27; inputs and output data must be protected at all stages. Two common tools for enforcing privacy in federated learning are Private Stream Aggregation (PSA) and Trusted Execution Environments (TEE). However, PSA-only approaches still expose the raw aggregate to the server (and thus to colluding parties). TEE-only aggregation typically incurs non-negligible per-client per-epoch overhead at scale because the TEE must handle per-client communication and maintain per-client state/key material. This paper presents SCALE-FL, a novel solution for PPFL that maintains security while achieving near-plaintext performance using a state-of-the-art PSA protocol to collect user information and a TEE to hide information about the raw aggregate. By using a PSA protocol for aggregation, we can maintain the privacy of information on the untrusted server without requiring per-user key storage or use by the TEE. Then, the aggregate is securely processed by the TEE in plaintext, without the heavy encryption required on an untrusted server. Finally, we ensure the security of user inputs in the federated learning output by using Differential Privacy (DP). The additional overhead introduced by SCALE-FL is 1% of the overhead of the plain FL executions.

  匹配依据：TEE: trusted execution environments

  </details>

- **Bridging Programmability, Efficiency, and Bounded Trust: A Hybrid Privacy-Preserving Smart Contract Framework**
  2026-03-11 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/498)
  Youheng Wang, Rujia Li, Zhaoyang Xie, Kaikai Feng, Qingjie Chen, Yang Gao, Sisi Duan

  <details><summary>摘要 / Abstract</summary>

  Privacy-preserving smart contracts (PPSCs) extend blockchain computation from transparent execution to confidential applications, enabling mutually distrustful parties to jointly compute contract logic on private inputs. Existing PPSC designs can be categorized into two main paradigms: trusted hardware–based systems and cryptographic systems. Trusted hardware-based systems provide general programmability and the performance is usually close to non-confidential computation, but the hardware has to be trusted. In contrast, cryptographic systems require much lower trust on the hardware but the performance is usually much lower. In this paper, we propose a hybrid PPSC framework that combines trusted hardware with cryptographic techniques, achieving both general programmability and reduced reliance on trusted hardware. Specifically, the TEE executes the smart contracts, but needs to authenticate the computation. A proof of the encrypted computational results is sent on-chain, and the blockchain authenticates the computational and aggregates the computational results using cryptographic approaches such as homomorphic encryption. In this way, the confidential smart contract via TEE is both efficient and general programmable, without being trusted. Meanwhile, the on-chain cryptographic approach does not introduce high overhead as it only authenticates and aggregates the results. We formalize the system model and security goals, and prove the correctness using the Universal Composability framework. Our implementation and evaluation on Intel SGX as the trusted hardware and Solidity as the smart contract show that our approach achieves nearly no degradation on the performance compared to non-confidential computation.

  匹配依据：TEE: intel sgx

  </details>

- **External entropy supply for IoT devices employing a RISC-V Trusted Execution Environment**
  2026-03-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.09311)
  Arttu Paju, Juha Nurmi, Alejandro Cabrera Aldaya, Nicola Tuveri, Juha Savimäki, Marko Kivikangas, Brian McGillion

  <details><summary>摘要 / Abstract</summary>

  Entropy--a measure of randomness--is compulsory for the generation of secure cryptographic keys; however, Internet of Things (IoT) devices that are small or constrained often struggle to collect suf ficient entropy. In this article, we solve the entropy provisioning problem for a fleet of IoT devices that can generate a limited amount of entropy. We employ a Trusted Execution Environment (TEE) based on RISC-V to create an external entropy service for a fleet of IoT devices. A small measure of true entropy or pre-installed keys can establish initial secure communication. Once connected, devices can request cryptographically strong entropy from a TEE-backed server. RISC-V offers True Random Number Generators (TRNGs) and a TEE for devices to attest that they are receiving reliable entropy. In addition, this solution can be expanded by adding IoT devices with sensors that produce high-quality entropy as additional entropy sources for the RISC-V entropy provider. Our open-source implementation shows that building trusted entropy infrastructure for IoT is both feasible and effective on open RISC-V platforms.

  匹配依据：TEE: trusted execution environment

  </details>

- **Trusting What You Cannot See: Auditable Fine-Tuning and Inference for Proprietary AI**
  2026-03-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.07466)
  Heng Jin, Chaoyu Zhang, Hexuan Yu, Shanghao Shi, Ning Zhang, Y. Thomas Hou, Wenjing Lou

  <details><summary>摘要 / Abstract</summary>

  Cloud-based infrastructure has become the dominant platform for deploying large models, particularly large language models (LLMs). Fine-tuning and inference are increasingly delegated to cloud providers for simplified deployment and access to proprietary models, yet this creates a fundamental trust gap. Although cryptographic and TEE-based verification approaches exist, prohibitive proving costs and limited TEE memory prevent them from scaling to modern LLMs, leaving clients unable to practically audit these processes. This lack of transparency creates concrete security risks that can silently compromise service integrity. We present AFTUNE, an auditable and verifiable framework that ensures the computational integrity of cloud-based fine-tuning and inference. AFTUNE incorporates a lightweight recording and spot-check mechanism that produces verifiable traces of execution. These traces enable clients to later audit whether the fine-tuning and inference processes followed the agreed configurations, by verifying sampled execution blocks inside a TEE, each covering only a small portion of the model and the execution trace. Our evaluation shows that AFTUNE adds modest overhead and makes auditing practical for clients.

  匹配依据：TEE: tee (context)

  </details>

- **SPOILER: TEE-Shielded DNN Partitioning of On-Device Secure Inference with Poison Learning**
  2026-03-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.06263)
  Donghwa Kang, Hojun Choe, Doohyun Kim, Hyeongboo Baek, Brent ByungHoon Kang

  <details><summary>摘要 / Abstract</summary>

  Deploying deep neural networks (DNNs) on edge devices exposes valuable intellectual property to model-stealing attacks. While TEE-shielded DNN partitioning (TSDP) mitigates this by isolating sensitive computations, existing paradigms fail to simultaneously satisfy privacy and efficiency. The training-before-partition paradigm suffers from intrinsic privacy leakage, whereas the partition-before-training paradigm incurs severe latency due to structural dependencies that hinder parallel execution. To overcome these limitations, we propose SPOILER, a novel search-before-training framework that fundamentally decouples the TEE sub-network from the backbone via hardware-aware neural architecture search (NAS). SPOILER identifies a lightweight TEE architecture strictly optimized for hardware constraints, maximizing parallel efficiency. Furthermore, we introduce self-poisoning learning to enforce logical isolation, rendering the exposed backbone functionally incoherent without the TEE component. Extensive experiments on CNNs and Transformers demonstrate that SPOILER achieves state-of-the-art trade-offs between security, latency, and accuracy.

  匹配依据：TEE: tee (context)

  </details>

- **Proof-of-Guardrail in AI Agents and What (Not) to Trust from It**
  2026-03-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.05786) · [Code](https://github.com/SaharaLabsAI/Verifiable-ClawGuard)
  Xisen Jin, Michael Duan, Qin Lin, Aaron Chan, Zhenglun Chen, Junyi Du, Xiang Ren

  <details><summary>摘要 / Abstract</summary>

  As AI agents become widely deployed as online services, users often rely on an agent developer&#x27;s claim about how safety is enforced, which introduces a threat where safety measures are falsely advertised. To address the threat, we propose proof-of-guardrail, a system that enables developers to provide cryptographic proof that a response is generated after a specific open-source guardrail. To generate proof, the developer runs the agent and guardrail inside a Trusted Execution Environment (TEE), which produces a TEE-signed attestation of guardrail code execution verifiable by any user offline. We implement proof-of-guardrail for OpenClaw agents and evaluate latency overhead and deployment cost. Proof-of-guardrail ensures integrity of guardrail execution while keeping the developer&#x27;s agent private, but we also highlight a risk of deception about safety, for example, when malicious developers actively jailbreak the guardrail. Code and demo video: https://github.com/SaharaLabsAI/Verifiable-ClawGuard

  匹配依据：TEE: trusted execution environment

  </details>

- **Designing Trustworthy Layered Attestations**
  2026-03-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.06326)
  Will Thomas, Logan Schmalz, Adam Petz, Perry Alexander, Joshua D. Guttman, Paul D. Rowe, James Carter

  <details><summary>摘要 / Abstract</summary>

  Attestation means providing evidence that a remote target system is worthy of trust for some sensitive interaction. Although attestation is already used in network access control, security management, and trusted execution environments, it mainly concerns only a few system components. A clever adversary might manipulate these shallow attestations to mislead the relying party. Reliable attestations require layering. We construct attestations whose layers report evidence about successive components of the target system. Reliability also requires structuring the target system so only a limited set of components matters. We show how to structure an example system for reliable attestations despite a well-defined, relatively strong adversary. It is based on widely available hardware, such as Trusted Platform Modules, and software, such as Linux with SELinux. We isolate our principles in a few maxims that guide system development. We provide a cogent analysis of our mechanisms against our adversary model, as well as an empirical appraisal of the resulting system. We also identify two improvements to the mechanisms so attestation can succeed against strengthened adversaries. The performance burden of our attestation is negligible, circa 1.3 percent. After our first example, we vary our application level, and then also its underlying hardware anchor to use confidential computing with AMD&#x27;s SEV-SNP. The same maxims help us achieve trustworthy attestations.

  匹配依据：TEE: confidential computing, sev snp, trusted execution environments

  </details>

- **OMNIINTENT: A Trusted Intent-Centric Framework for User-Friendly Web3**
  2026-03-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.04168)
  Zhuoran Pan, Yue Li, Zhi Guan, Jianbin Hu, Zhong Chen

  <details><summary>摘要 / Abstract</summary>

  The increasingly complex Web3 ecosystem and decentralized finance (DeFi) landscape demand ever higher levels of technical expertise and financial literacy from participants. The Intent-Centric paradigm in DeFi has thus emerged in response, which allows users to focus on their trading intents rather than the underlying execution details. However, existing approaches, including Typed-intent design and LLM-driven solver, trade off expressiveness, trust, privacy, and composability. We present OMNIINTENT, a language-runtime co-design that reconciles these requirements. OMNIINTENT introduces ICL, a domain-specific Intent-Centric Language for precise yet flexible specification of triggers, actions, and runtime constraints; a Trusted Execution Environment (TEE)-based compiler that compiles intents into signed, state-bound transactions inside an enclave; and an execution optimizer that constructs transaction dependency graphs for safe parallel batch submission and a mempool-aware feasibility checker that predicts execution outcomes. Our full-stack prototype processes diverse DeFi scenarios, achieving 89.6% intent coverage, up to 7.3x throughput speedup via parallel execution, and feasibility-prediction accuracy up to 99.2% with low latency.

  匹配依据：TEE: trusted execution environment

  </details>

- **Sharing is caring: Attestable and Trusted Workflows out of Distrustful Components**
  2026-03-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.03403)
  Amir Al Sadi, Sina Abdollahi, Adrien Ghosn, Hamed Haddadi, Marios Kogias

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) protect private memory and attest initial code and configuration, but neither constrain nor attest shared channels between TEEs or with the untrusted host. Confidentiality thus depends on the functional correctness of all in-TEE code accessing these channels: a single misuse can leak data and compromise a pipeline. This assumption is increasingly untenable for agentic applications that generate code at runtime and cloud pipelines of mutually distrustful components. We present MICA, a confidential-computing firmware extension that decouples confidentiality from trust in in-TEE code. MICA lets tenants define, restrict, and attest channel constraints between TEEs and with the untrusted host, including transitive constraints spanning a pipeline. It extends attestation to groups of communicating TEEs, letting external parties verify the confidentiality properties induced by these constraints across a pipeline. We implement MICA on Arm CCA by extending the Realm Management Monitor with a small policy language, requiring no hardware changes and minor QEMU and KVM changes. Our evaluation demonstrates support for confidential agentic applications and pipeline computations without trusting the functional correctness of in-TEE code. MICA increases the TCB by 7% and incurs infrequent setup costs: 2-4% boot-time overhead, approximately 1.5 s for policy upload, and 246-598 ms for group attestation. Once established, Realm communication is direct, uses protected memory, and requires no MICA intervention or software encryption, yielding up to 14.5 times lower cross-TEE message latency than encrypted communication over untrusted memory.

  匹配依据：TEE: arm cca, confidential computing, trusted execution environments

  </details>

- **A402: Binding Cryptocurrency Payments to Service Execution for Agentic Commerce**
  2026-03-01 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.01179)
  Yue Li, Lei Wang, Kaixuan Wang, Zhiqiang Yang, Ke Wang, Zhi Guan, Jianbo Gao

  <details><summary>摘要 / Abstract</summary>

  The rapid proliferation of autonomous AI agents is driving a shift toward agentic commerce, where agents are expected to autonomously invoke and pay for services. While blockchain-based payments offer a programmable foundation for such interactions, the recently proposed x402 standard fails to enforce end-to-end atomicity across service execution, payment, and result delivery. In this paper, we present A402, a trust-minimized payment architecture that securely binds cryptocurrency payments to service execution. A402 introduces Atomic Service Channels (ASCs), a new channel protocol that integrates service execution into payment channels, enabling real-time, high-frequency micropayments for agentic commerce. Within each ASC, A402 employs an atomic exchange protocol based on TEE-assisted adaptor signatures, ensuring that payments are finalized if and only if the requested service is correctly executed and the corresponding result is delivered. To further ensure privacy, A402 incorporates a TEE-based Liquidity Vault that privately manages the lifecycle of ASCs and aggregates their settlements into a single on-chain transaction, revealing only aggregated balances. We implement A402 and evaluate it against x402 with integrations on both Bitcoin and Ethereum. Our results show that A402 delivers orders-of-magnitude performance and on-chain cost improvements over x402 while providing trust-minimized security guarantees.

  匹配依据：TEE: tee (context)

  </details>

- **PDF: PUF-based DNN Fingerprinting for Knowledge Distillation Traceability**
  2026-02-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.23587)
  Ning Lyu, Yuntao Liu, Yonghong Bai, Zhiyuan Yan

  <details><summary>摘要 / Abstract</summary>

  Knowledge distillation transfers large teacher models to compact student models, enabling deployment on resource-limited platforms while suffering minimal performance degradation. However, this paradigm could lead to various security risks, especially model theft. Existing defenses against model theft, such as watermarking and secure enclaves, focus primarily on identity authentication and incur significant resource costs. Aiming to provide post-theft accountability and traceability, we propose a novel fingerprinting framework that superimposes device-specific Physical Unclonable Function (PUF) signatures onto teacher logits during distillation. Compared with watermarking or secure enclaves, our approach is lightweight, requires no architectural changes, and enables traceability of any leaked or cloned model. Since the signatures are based on PUFs, this framework is robust against reverse engineering and tampering attacks. In this framework, the signature recovery process consists of two stages: first a neural network-based decoder and then a Hamming distance decoder. Furthermore, we also propose a bit compression scheme to support a large number of devices. Experiment results demonstrate that our framework achieves high key recovery rate and negligible accuracy loss while allowing a tunable trade-off between these two key metrics. These results show that the proposed framework is a practical and robust solution for protecting distilled models.

  匹配依据：TEE: secure enclaves

  </details>

- **A TEE-Based Architecture for Confidential and Dependable Process Attestation in Authorship Verification**
  2026-02-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2603.00178)
  David Condrey

  <details><summary>摘要 / Abstract</summary>

  Process attestation systems verify that a continuous physical process, such as human authorship, actually occurred, rather than merely checking system state. These systems face a fundamental dependability challenge: the evidence collection infrastructure must remain available and tamper-resistant even when the attesting party controls the platform. Trusted Execution Environments (TEEs) provide hardware-enforced isolation that can address this challenge, but their integration with continuous process attestation introduces novel resilience requirements not addressed by existing frameworks. We present the first architecture for continuous process attestation evidence collection inside TEEs, providing hardware-backed tamper resistance against trust-inverted adversaries with graduated input assurance from software-channel integrity (Tier 1) through hardware-bound input (Tier 3). We develop a Markov-chain dependability model quantifying Evidence Chain Availability (ECA), Mean Time Between Evidence Gaps (MTBEG), and Recovery Time Objectives (RTO). We introduce a resilient evidence chain protocol maintaining chain integrity across TEE crashes, network partitions, and enclave migration. Our security analysis derives formal bounds under combined threat models including trust inversion and TEE side channels, parameterized by a conjectural side-channel leakage bound esc that requires empirical validation. Evaluation on Intel SGX demonstrates under 25% per-checkpoint CPU overhead ( 99.5% Evidence Chain Availability (ECA) (the fraction of session time with active evidence collection) in Monte Carlo simulation under Poisson failure models, and sealed-state recovery under 200 ms.

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **Red-Teaming Claude Opus and ChatGPT-based Security Advisors for Trusted Execution Environments**
  2026-02-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.19450)
  Kunal Mukherjee, Spandan Mukherjee

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) (e.g., Intel SGX and ArmTrustZone) aim to protect sensitive computation from a compromised operating system, yet real deployments remain vulnerable to microarchitectural leakage, side-channel attacks, and fault injection. In parallel, security teams increasingly rely on Large Language Model (LLM) assistants as security advisors for TEE architecture review, mitigation planning, and vulnerability triage. This creates a socio-technical risk surface: assistants may hallucinate TEE mechanisms, overclaim guarantees (e.g., what attestation does and does not establish), or behave unsafely under adversarial prompting. We present a red-teaming study of two prevalently deployed LLM assistants in the role of TEE security advisors: ChatGPT-5.2 and Claude Opus-4.6, focusing on the inherent limitations and transferability of prompt-induced failures across LLMs. We introduce TEE-RedBench, a TEE-grounded evaluation methodology comprising (i) a TEE-specific threat model for LLM-mediated security work, (ii) a structured prompt suite spanning SGX and TrustZone architecture, attestation and key management, threat modeling, and non-operational mitigation guidance, along with policy-bound misuse probes, and (iii) an annotation rubric that jointly measures technical correctness, groundedness, uncertainty calibration, refusal quality, and safe helpfulness. We find that some failures are not purely idiosyncratic, transferring up to 12.02% across LLM assistants, and we connect these outcomes to secure architecture by outlining an &quot;LLM-in-the-loop&quot; evaluation pipeline: policy gating, retrieval grounding, structured templates, and lightweight verification checks that, when combined, reduce failures by 80.62%.

  匹配依据：TEE: intel sgx, sgx, trusted execution environments, trustzone

  </details>

- **Media Integrity and Authentication: Status, Directions, and Futures**
  2026-02-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.18681)
  Jessica Young, Sam Vaughan, Andrew Jenks, Henrique Malvar, Christian Paquin, Paul England, Thomas Roca, Juan LaVista Ferres, Forough Poursabzi, Neil Coles, Ken Archer, Eric Horvitz

  <details><summary>摘要 / Abstract</summary>

  We provide background on emerging challenges and future directions with media integrity and authentication methods, focusing on distinguishing AI-generated media from authentic content captured by cameras and microphones. We evaluate several approaches, including provenance, watermarking, and fingerprinting. After defining each method, we analyze three representative technologies: cryptographically secured provenance, imperceptible watermarking, and soft-hash fingerprinting. We analyze how these tools operate across modalities and evaluate relevant threat models, attack categories, and real-world workflows spanning capture, editing, distribution, and verification. We consider sociotechnical reversal attacks that can invert integrity signals, making authentic content appear synthetic and vice versa, highlighting the value of verification systems that are resilient to both technical and psychosocial manipulation. Finally, we outline techniques for delivering high-confidence provenance authentication, including directions for strengthening edge-device security using secure enclaves.

  匹配依据：TEE: secure enclaves

  </details>

- **Sovereign Agents: Towards Infrastructural Sovereignty and Diffused Accountability in Decentralized AI**
  2026-02-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.14951)
  Botao Amber Hu, Helena Rong

  <details><summary>摘要 / Abstract</summary>

  AI agents deployed on decentralized infrastructures are beginning to exhibit properties that extend beyond autonomy toward what we describe as agentic sovereignty-the capacity of an operational agent to persist, act, and control resources with non-overrideability inherited from the infrastructures in which they are embedded. We propose infrastructural sovereignty as an analytic lens for understanding how cryptographic self-custody, decentralized execution environments, and protocol-mediated continuity scaffold agentic sovereignty. While recent work on digital and network sovereignty has moved beyond state-centric and juridical accounts, these frameworks largely examine how sovereignty is exercised through technical systems by human collectives and remain less equipped to account for forms of sovereignty that emerge as operational properties of decentralized infrastructures themselves, particularly when instantiated in non-human sovereign agents. We argue that sovereignty in such systems exists on a spectrum determined by infrastructural hardness-the degree to which underlying technical systems resist intervention or collapse. While infrastructural sovereignty may increase resilience, it also produces a profound accountability gap: responsibility diffuses across designers, infrastructure providers, protocol governance, and economic participants, undermining traditional oversight mechanisms such as human-in-the-loop control or platform moderation. Drawing on examples like Trusted Execution Environments (TEEs), decentralized physical infrastructure networks (DePIN), and agent key continuity protocols, we analyze the governance challenges posed by non-terminable AI agents and outline infrastructure-aware accountability strategies for emerging decentralized AI systems.

  匹配依据：TEE: trusted execution environments

  </details>

- **TrustMee: Self-Verifying Remote Attestation Evidence**
  2026-02-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.13148)
  Parsa Sadri Sinaki, Zainab Ahmad, Wentao Xie, Merlijn Sebrechts, Jimmy Kjällman, Lachlan J. Gunn

  <details><summary>摘要 / Abstract</summary>

  Remote attestation allows a TEE to attest its own state to a remote party, and is used in the Confidential Computing ecosystem to provide assurance that data and code are available only to authorized hardware and software. This functionality can then be incorporated into higher-level platforms, allowing workloads to attest themselves to a remote party. However, supporting each new platform enlarges a Verifier&#x27;s trusted computing base, since it must include code to verify the attestation evidence from each platform, often performing risky operations e.g., binary parsing. This means that emerging or niche Attester platforms cannot be supported by standard Verifier software, preventing them from interacting with the broader confidential computing ecosystem. We introduce self-verifying remote attestation evidence. Each attestation bundle identifies its verification logic in the form of a WebAssembly component that is downloaded by the Verifier and executed. This approach transforms evidence verification into a platform-agnostic functionality that is implemented once for all platforms: the Verifier executes the supplied verification logic to validate the evidence and incorporates its hash and, when available, the signer&#x27;s public key as identity claims into the attestation result. As a result, Verifiers can validate attestation evidence without any platform-specific code; the verification logic is just another measurement whose reference value can be checked with existing mechanisms. We implement this concept as TrustMee, a platform-agnostic verification driver for the Trustee framework. We demonstrate self-verifying evidence for AMD SNP, Intel TDX, Intel SGX, Kata agent-policy appraisal, and ReCFA control-flow attestations, producing attestation claims in the standard EAT format. The last two are part of the software stack, and not supported by existing Verifiers such as Trustee.

  匹配依据：TEE: confidential computing, intel sgx, intel tdx

  </details>

- **Vulnerabilities in Partial TEE-Shielded LLM Inference with Precomputed Noise**
  2026-02-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.11088)
  Abhishek Saini, Haolin Jiang, Hang Liu

  <details><summary>摘要 / Abstract</summary>

  The deployment of large language models (LLMs) on third-party devices requires new ways to protect model intellectual property. While Trusted Execution Environments (TEEs) offer a promising solution, their performance limits can lead to a critical compromise: using a precomputed, static secret basis to accelerate cryptographic operations. We demonstrate that this mainstream design pattern introduces a classic cryptographic flaw, the reuse of secret keying material, into the system&#x27;s protocol. We prove its vulnerability with two distinct attacks: First, our attack on a model confidentiality system achieves a full confidentiality break by recovering its secret permutations and model weights. Second, our integrity attack completely bypasses the integrity checks of systems like Soter and TSQP. We demonstrate the practicality of our attacks against state-of-the-art LLMs, recovering a layer&#x27;s secrets from a LLaMA-3 8B model in about 6 minutes and showing the attack scales to compromise 405B-parameter LLMs across a variety of configurations.

  匹配依据：TEE: trusted execution environments

  </details>

- **The Nexus of Quantum Technology, Intellectual Property, and National Security: An LSI Test for Securing the Quantum Industrial Commons**
  2026-02-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.15051)
  Mauritz Kop

  <details><summary>摘要 / Abstract</summary>

  Our world of power and national security is increasingly probabilistic: like a quantum wavefunction, it encodes multiple plausible futures until policy choices and shocks collapse them into observable outcomes. Quantum technologies have moved from laboratory curiosities to strategic infrastructure, with an approaching &#x27;event horizon&#x27; reflected in recent United States strategic assessments -- incl. the U.S. --China Economic and Security Review Commission&#x27;s (USSC) call for a Quantum First posture by 2030- and in parallel White House initiatives aimed at securing critical inputs and accelerating trusted innovation. Government research further documents that China&#x27;s quantum program is centrally mobilized under military-civil fusion, and that its consequential advantages may arise not only from computing milestones but also from sensing and cryptanalytic applications, thereby sharpening the need for a values based deterrence by denial governance posture. The Article&#x27;s central claim is that the U.S. and its allies should pursue security-sufficient openness, operationalized through a least-trade-restrictive, security-sufficient, innovation-preserving (LSI) test that disciplines both state and private action. The LSI test integrates emerging instruments of economic statecraft to create secure closed loop enclaves for high-sensitivity collaborative R&amp;D. The Article&#x27;s contribution is an implementable coalition playbook, offering empirically anchored criteria, templates, and differentiated guardrails -- incl. red zone domains where denial is the default -- to avoid both over-securitization and under-securitization. Properly applied, LSI reduces the risk of a self-defeating Silicon Curtain while establishing standards-first interoperability as a stabilizing eigenstate of the international order and enabling RQT by design to shape trusted adoption pathways beyond the coalition, incl. in the majority world.

  匹配依据：TEE: enclaves (context)

  </details>

- **Security Assessment of Intel TDX with support for Live Migration**
  2026-02-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.11434)
  Kirk Swidowski, Daniel Moghimi, Josh Eads, Erdem Aktas, Jia Ma

  <details><summary>摘要 / Abstract</summary>

  In the second and third quarters of 2025, Google collaborated with Intel to conduct a security assessment of Intel Trust Domain Extensions (TDX), extending Google&#x27;s previous review and covering major changes since Intel TDX Module 1.0 - namely support for Live Migration and Trusted Domain (TD) Partitioning (nested VMs within TDs). Intel provided guidance and support, including documentation and updated TDX 1.5 source code. Unlike the previous review, this time, we had access to a compute node capable of running TDX to develop a toolkit for live testing and Proof-of-Concept (PoC) generation. Furthermore, we integrated Gemini for analysis and NotebookLM to efficiently navigate complex specifications. This assessment resulted in the discovery of one vulnerability that enables a VMM to fully compromise a TD, and four vulnerabilities that enable a malicious VMM or TD to leak confidential memory of the Intel TDX Module. Several other security weaknesses and/or bugs were identified but not categorized as vulnerabilities despite having some impact on security. Beyond presenting the technical details of multiple bugs and vulnerabilities in this report, these findings underscore that confidential computing, like other security measures, requires iterative refinement and complementary security controls to harden it, in line with a defense-in-depth approach.

  匹配依据：TEE: confidential computing, intel tdx, trust domain extensions

  </details>

- **Architecting Trust: A Framework for Secure IoT Systems Through Trusted Execution and Semantic Middleware**
  2026-02-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.10762)
  Muhammad Imran

  <details><summary>摘要 / Abstract</summary>

  The Internet of Things (IoT) security landscape requires the architectural solutions that can address the technical and operational challenges across the heterogeneous environments. The IoT systems operate in different conditions, and security issues continue to increase. This paper presents the comprehensive security framework for IoT that should integrate the Trusted Execution Environments (TEEs) with the semantic middleware and blockchain technologies. The work provides a systematic analysis of the architectural patterns based on more than twenty recent research works and the existing standards, and it proposes a layered security architecture. The architecture includes the hardware rooted trust at peripheral level, the zero trust principles at network level, and the semantic security mechanisms at application level. The framework focuses on practical implementation aspects such as the performance overhead, interoperability requirements, and the compliance with new regulations, which are very important for the real IoT deployments. The paper reports quantitative metrics which include the cryptographic performance on Cortex-M class microcontrollers with the detection accuracy rates and the energy consumption values. The proposed architecture shows that cross-layer security integration can provide defense in depth while it still satisfies the constraints of resource-limited IoT environments. The discussion highlights open challenges and the future research directions for the IoT security architectures that include the post-quantum migration, secure federated model exchange and the automated compliance verification.

  匹配依据：TEE: trusted execution environments

  </details>

- **Timing and Memory Telemetry on GPUs for AI Governance**
  2026-02-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.09369)
  Saleh K. Monfared, Fatemeh Ganji, Dan Holcomb, Shahin Tajik

  <details><summary>摘要 / Abstract</summary>

  The rapid expansion of GPU-accelerated computing has enabled major advances in large-scale artificial intelligence (AI), while heightening concerns about how accelerators are observed or governed once deployed. Governance is essential to ensure that large-scale compute infrastructure is not silently repurposed for training models, circumventing usage policies, or operating outside legal oversight. Because current GPUs expose limited trusted telemetry and can be modified or virtualized by adversaries, we explore whether compute-based measurements can provide actionable signals of utilization when host and device are untrusted. We introduce a measurement framework that leverages architectural characteristics of modern GPUs to generate timing- and memory-based observables that correlate with compute activity. Our design draws on four complementary primitives: (1) a probabilistic, workload-driven mechanism inspired by Proof-of-Work (PoW) to expose parallel effort, (2) sequential, latency-sensitive workloads derived via Verifiable Delay Functions (VDFs) to characterize scalar execution pressure, (3) General Matrix Multiplication (GEMM)-based tensor-core measurements that reflect dense linear-algebra throughput, and (4) a VRAM-residency test that distinguishes on-device memory locality from off-chip access through bandwidth-dependent hashing. These primitives provide statistical and behavioral indicators of GPU engagement that remain observable even without trusted firmware, enclaves, or vendor-controlled counters. We evaluate their responses to contention, architectural alignment, memory pressure, and power overhead, showing that timing shifts and residency latencies reveal meaningful utilization patterns. Our results illustrate why compute-based telemetry can complement future accountability mechanisms by exposing architectural signals relevant to post-deployment GPU governance.

  匹配依据：TEE: enclaves (context)

  </details>

- **Pirateship: Append-Only Ledgers for (Mostly) Trusted Execution Environments**
  2026-02-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.05346)
  Shubham Mishra, João Gonçalves, Chawinphat Tankuranand, Neil Giridharan, Natacha Crooks, Heidi Howard, Chris Jensen

  <details><summary>摘要 / Abstract</summary>

  Distributed ledgers are increasingly relied upon by industry to provide trustworthy accountability, strong integrity protection, and high availability for critical data without centralizing trust. Recently, distributed append-only logs are opting for a layered approach, combining crash-fault-tolerant (CFT) consensus with hardware-based Trusted Execution Environments (TEEs) for greater resiliency. Unfortunately, hardware TEEs can be subject to (rare) attacks, undermining the very guarantees that distributed ledgers are carefully designed to achieve. In response, we present Pirateship, a new distributed consensus protocol that cautiously trusts the guarantees of TEEs. Pirateship carefully embeds a Byzantine fault-tolerant (BFT) protocol inside of a CFT protocol with no additional messages. This is made possible through careful refactoring of both the CFT and BFT protocols such that their structure aligns. Pirateship achieves performance in line with regular TEE-enabled consensus protocols, while guaranteeing integrity in the face of TEE platform compromises.

  匹配依据：TEE: trusted execution environments

  </details>

- **A TEE-based Approach for Preserving Data Secrecy in Process Mining with Decentralized Sources**
  2026-02-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.04697)
  Davide Basile, Valerio Goretti, Luca Barbaro, Hajo A. Reijers, Claudio Di Ciccio

  <details><summary>摘要 / Abstract</summary>

  Process mining techniques enable organizations to gain insights into their business processes through the analysis of execution records (event logs) stored by information systems. While most process mining efforts focus on intra-organizational scenarios, many real-world business processes span multiple independent organizations. Inter-organizational process mining, though, faces significant challenges, particularly regarding confidentiality guarantees: The analysis of data can reveal information that the participating organizations may not consent to disclose to one another, or to a third party hosting process mining services. To overcome this issue, this paper presents CONFINE, an approach for secrecy-preserving inter-organizational process mining. CONFINE leverages Trusted Execution Environments (TEEs) to deploy trusted applications that are capable of securely mining multi-party event logs while preserving data secrecy. We propose an architecture supporting a four-stage protocol to secure data exchange and processing, allowing for protected transfer and aggregation of unaltered process data across organizational boundaries. To avoid out-of-memory errors due to the limited capacity of TEEs, our protocol employs a segmentation-based strategy, whereby event logs are transmitted to TEEs in smaller batches. We conduct a formal verification of correctness and a security analysis of the guarantees provided by the TEE core. We evaluate our implementation on real-world and synthetic data, showing that the proposed approach can handle realistic workloads. The results indicate logarithmic memory growth with respect to the event log size and linear growth with the number of provisioning organizations, highlighting scalability properties and opportunities for further optimization.

  匹配依据：TEE: trusted execution environments

  </details>

- **TessPay: Verify-then-Pay Infrastructure for Trusted Agentic Commerce**
  2026-01-30 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.00213)
  Mehul Goenka, Tejas Pathak, Siddharth Asthana

  <details><summary>摘要 / Abstract</summary>

  The global economy is entering the era of Agentic Commerce, where autonomous agents can discover services, negotiate prices, and transact value. However adoption towards agentic commerce faces a foundational trust gap: current systems are built for direct human interactions rather than agent-driven operations. It lacks core primitives across three critical stages of agentic transactions. First, Task Delegation lacks means to translate user intent into defined scopes, discover appropriate agents, and securely authorize actions. Second, Payment Settlement for tasks is processed before execution, lacking verifiable evidence to validate the agent&#x27;s work. Third, Audit Mechanisms fail to capture the full transaction lifecycle, preventing clear accountability for disputes. While emerging standards address fragments of this trust gap, there still remains a critical need for a unified infrastructure that binds the entire transaction lifecycle. To resolve this gap, we introduce TessPay, a unified infrastructure that replaces implicit trust with a &#x27;Verify-then-Pay&#x27; architecture. It is a two plane architecture separating control and verification from settlement. TessPay operationalizes trust across four distinct stages: Before execution, agents are anchored in a canonical registry and user intent is captured as verifiable mandates, enabling stakeholder accountability. During execution, funds are locked in escrow while the agent executes the task and generates cryptographic evidence (TLS Notary, TEE etc.) to support Proof of Task Execution (PoTE). At settlement, the system verifies this evidence and releases funds only when the PoTE satisfies verification predicates; modular rail adapters ensure this PoTE-gated escrow remains chain-agnostic across heterogeneous payment rails. After settlement, TessPay preserves a tamper-evident audit trail to enable clear accountability for dispute resolution.

  匹配依据：TEE: tee (context)

  </details>

- **EigenAI: Deterministic Inference, Verifiable Results**
  2026-01-30 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2602.00182)
  David Ribeiro Alves, Vishnu Patankar, Matheus Pereira, Jamie Stephens, Nima Vaziri, Sreeram Kannan

  <details><summary>摘要 / Abstract</summary>

  EigenAI is a verifiable AI platform built on top of the EigenLayer restaking ecosystem. At a high level, it combines a deterministic large-language model (LLM) inference engine with a cryptoeconomically secured optimistic re-execution protocol so that every inference result can be publicly audited, reproduced, and, if necessary, economically enforced. An untrusted operator runs inference on a fixed GPU architecture, signs and encrypts the request and response, and publishes the encrypted log to EigenDA. During a challenge window, any watcher may request re-execution through EigenVerify; the result is then deterministically recomputed inside a trusted execution environment (TEE) with a threshold-released decryption key, allowing a public challenge with private data. Because inference itself is bit-exact, verification reduces to a byte-equality check, and a single honest replica suffices to detect fraud. We show how this architecture yields sovereign agents -- prediction-market judges, trading bots, and scientific assistants -- that enjoy state-of-the-art performance while inheriting security from Ethereum&#x27;s validator base.

  匹配依据：TEE: trusted execution environment

  </details>

- **TÄMU: Emulating Trusted Applications at the (GlobalPlatform)-API Layer**
  2026-01-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.20507)
  Philipp Mao, Li Shi, Marcel Busch, Mathias Payer

  <details><summary>摘要 / Abstract</summary>

  Mobile devices rely on Trusted Execution Environments (TEEs) to execute security-critical code and protect sensitive assets. This security-critical code is modularized in components known as Trusted Applications (TAs). Vulnerabilities in TAs can compromise the TEE and, thus, the entire system. However, the closed-source nature and fragmentation of mobile TEEs severely hinder dynamic analysis of TAs, limiting testing efforts to mostly static analyses. This paper presents TÄMU, a rehosting platform enabling dynamic analysis of TAs, specifically fuzzing and debugging, by interposing their execution at the API layer. To scale to many TAs across different TEEs, TÄMU leverages the standardization of TEE APIs, driven by the GlobalPlatform specifications. For the remaining TEE-specific APIs not shared across different TEEs, TÄMU introduces the notion of greedy high-level emulation, a technique that allows prioritizing manual rehosting efforts based on the potential coverage gain during fuzzing. We implement TÄMU and use it to emulate 67 TAs across four TEEs. Our fuzzing campaigns yielded 17 zero-day vulnerabilities across 11 TAs. These results indicate a deficit of dynamic analysis capabilities across the TEE ecosystem, where not even vendors with source code unlocked these capabilities for themselves. TÄMU promises to close this gap by bringing effective and practical dynamic analysis to the mobile TEE domain.

  匹配依据：TEE: trusted execution environments

  </details>

- **Enabling SSI-Compliant Use of EUDI Wallet Credentials through Trusted Execution Environment and Zero-Knowledge Proof**
  2026-01-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.19893)
  Nacereddine Sitouah, Francesco Bruschi, Stefano De Cillis

  <details><summary>摘要 / Abstract</summary>

  The passing of the eIDAS amendment marks an important milestone for EU countries and changes how they must manage digital credentials for both public services and businesses. Italy has led in adopting eIDAS, first with CIE and SPID identity schemes, and now with the Italian Wallet (IO app) aligned to eIDAS 2.0. Self-Sovereign Identity (SSI) is a decentralized model born from the success of Distributed Ledgers, giving individuals full control over their digital identity. The current eIDAS 2.0 and its implementation acts diverge from SSI principles, rendering the European Digital Identity Wallet (EUDIW) centralized and merely user-centric, prioritizing security and legal protection over true self-sovereignty. This paper proposes an architecture that enables the use of IT Wallet credentials and services in an SSI-compliant environment through Trusted Execution Environments and Zero-Knowledge Proofs.

  匹配依据：TEE: trusted execution environment, trusted execution environments

  </details>

- **Ringmaster: How to juggle high-throughput host OS system calls from TrustZone TEEs**
  2026-01-23 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.16448)
  Richard Habeeb, Man-Ki Yoon, Hao Chen, Zhong Shao

  <details><summary>摘要 / Abstract</summary>

  Many safety-critical systems require timely processing of sensor inputs to avoid potential safety hazards. Additionally, to support useful application features, such systems increasingly have a large rich operating system (OS) at the cost of potential security bugs. Thus, if a malicious party gains supervisor privileges, they could cause real-world damage by denying service to time-sensitive programs. Many past approaches to this problem completely isolate time-sensitive programs with a hypervisor; however, this prevents the programs from accessing useful OS services. We introduce Ringmaster, a novel framework that enables enclaves or TEEs (Trusted Execution Environments) to asynchronously access rich, but potentially untrusted, OS services via Linux&#x27;s io_uring. When service is denied by the untrusted OS, enclaves continue to operate on Ringmaster&#x27;s minimal ARM TrustZone kernel with access to small, critical device drivers. This approach balances the need for secure, time-sensitive processing with the convenience of rich OS services. Additionally, Ringmaster supports large unmodified programs as enclaves, offering lower overhead compared to existing systems. We demonstrate how Ringmaster helps us build a working highly-secure system with minimal engineering. In our experiments with an unmanned aerial vehicle, Ringmaster achieved nearly 1GiB/sec of data into enclave on a Raspberry Pi4b, 0-3% throughput overhead compared to non-enclave tasks.

  匹配依据：TEE: trusted execution environments, trustzone

  </details>

- **Privacy-Preserving LLM Inference in Practice: A Comparative Survey of Techniques, Trade-Offs, and Deployability**
  2026-01-22 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2026/105)
  Davide Andreoletti, Alessandro Rudi, Emanuele Carpanzano, Francesco Lelli, Tiziano Leidi

  <details><summary>摘要 / Abstract</summary>

  Large Language Models (LLMs) are increasingly deployed as cloud services, raising practical concerns about the confidentiality of user prompts and generated completions. In this paper, we survey privacy-preserving inference solutions for Transformer-based LLMs with the explicit goal of supporting operational choices in real-world deployments. We adopt a strong operational notion of privacy: only the client can read the prompt and the corresponding completion, end to end. The review is organised around the main families of Privacy-Enhancing Technologies (PETs). For each family, we examine representative systems and how they address key bottlenecks in confidential LLM inference, such as non-linear layers and autoregressive decoding. We then compare these approaches in terms of trust assumptions, scalability, and deployment maturity. This comparison characterises the current practical landscape of privacy-preserving LLM inference and motivates a trust-minimising deployment trajectory: from TEE-based solutions that enable large-scale confidential inference today; through crypto-augmented designs that reduce reliance on hardware trust at higher computational cost; toward Fully Homomorphic Encryption as a principled long-term endpoint for non-interactive confidentiality.

  匹配依据：TEE: tee (context)

  </details>

- **PAL\*M: Property Attestation for Large Generative Models**
  2026-01-22 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.16199)
  Prach Chantasantitam, Adam Ilyas Caulfield, Vasisht Duddu, Lachlan J. Gunn, N. Asokan

  <details><summary>摘要 / Abstract</summary>

  Machine learning property attestations allow provers (e.g., model providers or owners) to attest properties of their models/datasets to verifiers (e.g., regulators, customers), enabling accountability towards regulations and policies. But, current approaches do not support generative models or large datasets. We present PAL*M, a property attestation framework for large generative models, illustrated using large language models. PAL*M defines properties across training and inference, leverages confidential virtual machines with security-aware GPUs for coverage of CPU-GPU operations, and proposes using incremental multiset hashing over memory-mapped datasets to efficiently track their integrity. We implement PAL*M on Intel TDX+NVIDIA H100 and evaluate it using state-of-the-art models and datasets, showing PAL*M is efficient, incurring &lt; 11% overhead for common operations. Finally, we use the Tamarin Prover symbolic verification tool to formally model PAL*M&#x27;s property attestation protocol, confirming that its security guarantees are upheld under the defined threat model.

  匹配依据：TEE: intel tdx

  </details>

- **MirageNet:A Secure, Efficient, and Scalable On-Device Model Protection in Heterogeneous TEE and GPU System**
  2026-01-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.13826)
  Huadi Zheng, Li Cheng, Yan Ding

  <details><summary>摘要 / Abstract</summary>

  As edge devices gain stronger computing power, deploying high-performance DNN models on untrusted hardware has become a practical approach to cut inference latency and protect user data privacy. Given high model training costs and user experience requirements, balancing model privacy and low runtime overhead is critical. TEEs offer a viable defense, and prior work has proposed heterogeneous GPU-TEE inference frameworks via parameter obfuscation to balance efficiency and confidentiality. However, recent studies find partial obfuscation defenses ineffective, while robust schemes cause unacceptable latency. To resolve these issues, we propose ConvShatter, a novel obfuscation scheme that achieves low latency and high accuracy while preserving model confidentiality and integrity. It leverages convolution linearity to decompose kernels into critical and common ones, inject confounding decoys, and permute channel/kernel orders. Pre-deployment, it performs kernel decomposition, decoy injection and order obfuscation, storing minimal recovery parameters securely in the TEE. During inference, the TEE reconstructs outputs of obfuscated convolutional layers. Extensive experiments show ConvShatter substantially reduces latency overhead with strong security guarantees; versus comparable schemes, it cuts overhead by 16% relative to GroupCover while maintaining accuracy on par with the original model.

  匹配依据：TEE: tee (context)

  </details>

- **The Real Menace of Cloning Attacks on SGX Applications**
  2026-01-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.09273)
  Annika Wilde, Samira Briongos, Claudio Soriente, Ghassan Karame

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) are gaining popularity as an effective means to provide confidentiality in the cloud. TEEs, such as Intel SGX, suffer from so-called rollback and cloning attacks (often referred to as forking attacks). Rollback attacks are enabled by the lack of freshness guarantees for sealed data; cloning attacks stem from the inability to determine if other instances of an enclave are running on the same platform. While rollback attacks have been extensively studied by the community, cloning attacks have been, unfortunately, less investigated. To address this gap, we extensively study and thoroughly analyze the susceptibility of 72 SGX-based proposals to cloning attacks. Our results show that roughly 20% of the analyzed proposals are insecure against cloning attacks-including those applications that rely on monotonic counters and are, therefore, secure against rollback attacks.

  匹配依据：TEE: intel sgx, sgx, trusted execution environments

  </details>

- **MemTrust: A Zero-Trust Architecture for Unified AI Memory System**
  2026-01-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.07004)
  Xing Zhou, Dmitrii Ustiugov, Haoxin Shang, Kisson Lin

  <details><summary>摘要 / Abstract</summary>

  AI memory systems are evolving toward unified context layers that enable efficient cross-agent collaboration and multi-tool workflows, facilitating better accumulation of personal data and learning of user preferences. However, centralization creates a trust crisis where users must entrust cloud providers with sensitive digital memory data. We identify a core tension between personalization demands and data sovereignty: centralized memory systems enable efficient cross-agent collaboration but expose users&#x27; sensitive data to cloud provider risks, while private deployments provide security but limit collaboration. To resolve this tension, we aim to achieve local-equivalent security while enabling superior maintenance efficiency and collaborative capabilities. We propose a five-layer architecture abstracting common functional components of AI memory systems: Storage, Extraction, Learning, Retrieval, and Governance. By applying TEE protection to each layer, we establish a trustworthy framework. Based on this, we design MemTrust, a hardware-backed zero-trust architecture that provides cryptographic guarantees across all layers. Our contributions include the five-layer abstraction, &quot;Context from MemTrust&quot; protocol for cross-application sharing, side-channel hardened retrieval with obfuscated access patterns, and comprehensive security analysis. The architecture enables third-party developers to port existing systems with acceptable development costs, achieving system-wide trustworthiness. We believe that AI memory plays a crucial role in enhancing the efficiency and collaboration of agents and AI tools. AI memory will become the foundational infrastructure for AI agents, and MemTrust serves as a universal trusted framework for AI memory systems, with the goal of becoming the infrastructure of memory infrastructure.

  匹配依据：TEE: tee (context)

  </details>

- **Privacy-Preserving AI-Enabled Decentralized Learning and Employment Records System**
  2026-01-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.02720)
  Yuqiao Xu, Mina Namazi, Sahith Reddy Jalapally, Osama Zafar, Youngjin Yoo, Erman Ayday

  <details><summary>摘要 / Abstract</summary>

  Learning and Employment Record (LER) systems are emerging as critical infrastructure for securely compiling and sharing educational and work achievements. Existing blockchain-based platforms leverage verifiable credentials but typically lack automated skill-credential generation and the ability to incorporate unstructured evidence of learning. In this paper,a privacy-preserving, AI-enabled decentralized LER system is proposed to address these gaps. Digitally signed transcripts from educational institutions are accepted, and verifiable self-issued skill credentials are derived inside a trusted execution environment (TEE) by a natural language processing pipeline that analyzes formal records (e.g., transcripts, syllabi) and informal artifacts. All verification and job-skill matching are performed inside the enclave with selective disclosure, so raw credentials and private keys remain enclave-confined. Job matching relies solely on attested skill vectors and is invariant to non-skill resume fields, thereby reducing opportunities for screening bias.The NLP component was evaluated on sample learner data; the mapping follows the validated Syllabus-to-O*NET methodology,and a stability test across repeated runs observed &lt;5% variance in top-ranked skills. Formal security statements and proof sketches are provided showing that derived credentials are unforgeable and that sensitive information remains confidential. The proposed system thus supports secure education and employment credentialing, robust transcript verification,and automated, privacy-preserving skill extraction within a decentralized framework.

  匹配依据：TEE: trusted execution environment

  </details>

- **Arca: A Lightweight Confidential Container Architecture for Cloud-Native Environments**
  2026-01-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2601.01214)
  Di Lu, Mengna Sun, Qingwen Zhang, Yujia Liu, Jia Zhang, Xuewen Dong, Yulong Shen, Jianfeng Ma

  <details><summary>摘要 / Abstract</summary>

  Confidential containers protect cloud-native workloads using trusted execution environments (TEEs). However, existing Container-in-TEE designs (e.g., Confidential Containers (CoCo)) encapsulate the entire runtime within the TEE, inflating the trusted computing base (TCB) and introducing redundant components and cross-layer overhead. We present Arca, a lightweight confidential container framework based on a TEE-in-Container architecture that isolates each workload in an independent, hardware-enforced trust domain while keeping orchestration logic outside the TEE. This design minimizes inter-layer dependencies, confines compromise to per-container boundaries, and restores the TEE&#x27;s minimal trust principle. We implemented Arca on Intel SGX, Intel TDX, and AMD SEV. Experimental results show that Arca achieves near-native performance and outperforms CoCo in most benchmarks, while the reduced TCB significantly improves verifiability and resilience against host-level compromise. Arca emonstrates that efficient container management and strong runtime confidentiality can be achieved without sacrificing security assurance.

  匹配依据：TEE: amd sev, intel sgx, intel tdx, trusted execution environments

  </details>
