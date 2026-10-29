# 2024 · TEE · 含会议/期刊记录 · 第 1/1 页

[总目录](../PAPERS.md)

- **TensorTEE: Unifying Heterogeneous TEE Granularity for Efficient Secure Collaborative Tensor Computing**
  2024-07-12 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2407.08903) · [ASPLOS](https://doi.org/10.1145/3622781.3674168)
  Yifan Hao, Xiaqing Li, Yuanbo Wen, Erhu Feng, Jianan Mu, Pengwei Jin, Tianyun Ma, Xinkai Song, Husheng Han, Zidong Du, Ling Liang, Xinyao Zheng, Qi Guo, Xing Hu

  <details><summary>摘要 / Abstract</summary>

  Heterogeneous collaborative computing with NPU and CPU has received widespread attention due to its substantial performance benefits. To ensure data confidentiality and integrity during computing, Trusted Execution Environments (TEE) is considered a promising solution because of its comparatively lower overhead. However, existing heterogeneous TEE designs are inefficient for collaborative computing due to fine and different memory granularities between CPU and NPU. 1) The cacheline granularity of CPU TEE intensifies memory pressure due to its extra memory access, and 2) the cacheline granularity MAC of NPU escalates the pressure on the limited memory storage. 3) Data transfer across heterogeneous enclaves relies on the transit of non-secure regions, resulting in cumbersome re-encryption and scheduling. To address these issues, we propose TensorTEE, a unified tensor-granularity heterogeneous TEE for efficient secure collaborative tensor computing. First, we virtually support tensor granularity in CPU TEE to eliminate the off-chip metadata access by detecting and maintaining tensor structures on-chip. Second, we propose tensor-granularity MAC management with predictive execution to avoid computational stalls while eliminating off-chip MAC storage and access. Moreover, based on the unified granularity, we enable direct data transfer without re-encryption and scheduling dilemmas. Our evaluation is built on enhanced Gem5 and a cycle-accurate NPU simulator. The results show that TensorTEE improves the performance of Large Language Model (LLM) training workloads by 4.0x compared to existing work and incurs only 2.1% overhead compared to non-secure training, offering a practical security assurance for LLM training.

  匹配依据：TEE: trusted execution environments

  </details>

- **WeSee: Using Malicious \#VC Interrupts to Break AMD SEV-SNP**
  2024-04-04 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2404.03526) · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00262)
  Shweta Shinde, Benedict Schlüter, Supraja Sridhara, Andrin Bertschi

  <details><summary>摘要 / Abstract</summary>

  AMD SEV-SNP offers VM-level trusted execution environments (TEEs) to protect the confidentiality and integrity for sensitive cloud workloads from untrusted hypervisor controlled by the cloud provider. AMD introduced a new exception, #VC, to facilitate the communication between the VM and the untrusted hypervisor. We present WeSee attack, where the hypervisor injects malicious #VC into a victim VM&#x27;s CPU to compromise the security guarantees of AMD SEV-SNP. Specifically, WeSee injects interrupt number 29, which delivers a #VC exception to the VM who then executes the corresponding handler that performs data and register copies between the VM and the hypervisor. WeSee shows that using well-crafted #VC injections, the attacker can induce arbitrary behavior in the VM. Our case-studies demonstrate that WeSee can leak sensitive VM information (kTLS keys for NGINX), corrupt kernel data (firewall rules), and inject arbitrary code (launch a root shell from the kernel space).

  匹配依据：TEE: amd sev, trusted execution environments

  </details>

- **sNPU: Trusted Execution Environments on Integrated NPUs.**
  2024 · TEE · 含会议/期刊记录 · [ISCA](https://doi.org/10.1109/ISCA59077.2024.00057)
  Yubin Xia, Erhu Feng, Haibo Chen, Dahu Feng, Dong Du

- **Trusted Execution Environments for Quantum Computers.**
  2024 · TEE · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3658644.3690855)
  Theodoros Trochatos

- **TDXdown: Single-Stepping and Instruction Counting Attacks against Intel TDX.**
  2024 · TEE · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3658644.3690230)
  Luca Wilke, Florian Sieck, Thomas Eisenbarth

- **Specification and Verification of Strong Timing Isolation of Hardware Enclaves.**
  2024 · TEE · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3658644.3690203)
  Clément Pit-Claudel, Thomas Bourgeat, Stella Lau, Adam Chlipala

- **SoK: SGX.Fail: How Stuff Gets eXposed.**
  2024 · TEE · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00260)
  Christina Garman, Stephan van Schaik, Eyal Ronen, Alexander Seto, Thomas Yurek, Bader AlBassam, Daniel Genkin, Yuval Yarom, Andrew Miller, Adam Batori

- **Secure Similarity Queries Over Vertically Distributed Data via TEE-Enhanced Cloud Computing.**
  2024 · TEE · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2024.3413630)
  Hui Zhu, Jun Shao, Yunguo Guan, Rongxing Lu, Fengwei Wang, Songnian Zhang, Hui Li, Yandong Zheng

- **Salus: A Practical Trusted Execution Environment for CPU-FPGA Heterogeneous Cloud Platforms.**
  2024 · TEE · 含会议/期刊记录 · [ASPLOS](https://doi.org/10.1145/3622781.3674169)
  Zhen Gu, Yiran Li, Le Su, Yijin Guan, Yanheng Lu, Dimin Niu, Sheng Wang, Yu Zou, Mingyu Gao, Feifei Li, Yuan Xie

- **SGXFault: An Efficient Page Fault Handling Mechanism for SGX Enclaves.**
  2024 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2023.3268169)
  Omais Shafi Pandith

- **SEV-Step: A Single-Stepping Framework for AMD-SEV**
  2024 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2307.14757) · [TCHES](https://doi.org/10.46586/TCHES.V2024.I1.180-206)
  Anja Rabich, Luca Wilke, Jan Wichelmann, Thomas Eisenbarth

  <details><summary>摘要 / Abstract</summary>

  The ever increasing popularity and availability of Trusted Execution Environments (TEEs) had a stark influence on microarchitectural attack research in academia, as their strong attacker model both boosts existing attack vectors and introduces several new ones. While many works have focused on Intel SGX, other TEEs like AMD SEV have recently also started to receive more attention. A common technique when attacking SGX enclaves is single-stepping, where the system&#x27;s APIC timer is used to interrupt the enclave after every instruction. Single-stepping increases the temporal resolution of subsequent microarchitectural attacks to a maximum. A key driver in the proliferation of this complex attack technique was the SGX-Step framework, which offered a stable reference implementation for single-stepping and a relatively easy setup. In this paper, we demonstrate that SEV VMs can also be reliably single-stepped. To lay the foundation for further microarchitectural attack research against SEV, we introduce the reusable SEV-Step framework. Besides reliable single-stepping, SEV-Step provides easy access to common attack primitives like page fault tracking and cache attacks against SEV. All features can be used interactively from user space. We demonstrate SEV-Step&#x27;s capabilities by carrying out an end-to-end cache attack against SEV that leaks the volume key of a LUKS2-encrypted disk. Finally, we show for the first time that SEV is vulnerable to Nemesis-style attacks, which allow to extract information about the type and operands of single-stepped instructions from SEV-protected VMs.

  匹配依据：TEE: amd sev, intel sgx, sgx, sgx enclaves, trusted execution environments

  </details>

- **Pandora: Principled Symbolic Validation of Intel SGX Enclave Runtimes.**
  2024 · TEE · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00090)
  David F. Oswald, Jo Van Bulck, Lesly-Ann Daniel, Fritz Alder, Frank Piessens

- **On (the Lack of) Code Confidentiality in Trusted Execution Environments**
  2024 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2212.07899) · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00259)
  Daniele Lain, Ivan Puddu, Moritz Schneider, Stefano Boschetto, Srdjan Capkun, Srdjan Čapkun

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) have been proposed as a solution to protect code confidentiality in scenarios where computation is outsourced to an untrusted operator. We study the resilience of such solutions to side-channel attacks in two commonly deployed scenarios: when a confidential code is a native binary that is shipped and executed within a TEE and when the confidential code is an intermediate representation (IR) executed on top of a runtime within a TEE. We show that executing IR code such as WASM bytecode on a runtime executing in a TEE leaks most IR instructions with high accuracy and therefore reveals the confidential code. Contrary to IR execution, native execution is much less susceptible to leakage and largely resists even the most powerful side-channel attacks. We evaluate native execution leakage in Intel SGX and AMD SEV and experimentally demonstrate end-to-end instruction extraction on Intel SGX, with WASM bytecode as IR executed within WAMR, a hybrid between a JIT compiler and interpreter developed by Intel. Our experiments show that IR code leakage from such systems is practical and therefore question the security claims of several commercial solutions which rely on TEEs+WASM for code confidentiality.

  匹配依据：TEE: amd sev, intel sgx, trusted execution environments

  </details>

- **No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML**
  2024 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2310.07152) · [IEEE S&amp;P](https://doi.org/10.1109/SP54263.2024.00052)
  Yao Guo, Bingyan Liu, Yifeng Cai, Chen Gong, Yuanyuan Yuan, Xiangqun Chen, Ding Li, Ziqi Zhang

  <details><summary>摘要 / Abstract</summary>

  On-device ML introduces new security challenges: DNN models become white-box accessible to device users. Based on white-box information, adversaries can conduct effective model stealing (MS) and membership inference attack (MIA). Using Trusted Execution Environments (TEEs) to shield on-device DNN models aims to downgrade (easy) white-box attacks to (harder) black-box attacks. However, one major shortcoming is the sharply increased latency (up to 50X). To accelerate TEE-shield DNN computation with GPUs, researchers proposed several model partition techniques. These solutions, referred to as TEE-Shielded DNN Partition (TSDP), partition a DNN model into two parts, offloading the privacy-insensitive part to the GPU while shielding the privacy-sensitive part within the TEE. This paper benchmarks existing TSDP solutions using both MS and MIA across a variety of DNN models, datasets, and metrics. We show important findings that existing TSDP solutions are vulnerable to privacy-stealing attacks and are not as safe as commonly believed. We also unveil the inherent difficulty in deciding optimal DNN partition configurations (i.e., the highest security with minimal utility cost) for present TSDP solutions. The experiments show that such ``sweet spot&#x27;&#x27; configurations vary across datasets and models. Based on lessons harvested from the experiments, we present TEESlice, a novel TSDP method that defends against MS and MIA during DNN inference. TEESlice follows a partition-before-training strategy, which allows for accurate separation between privacy-related weights from public weights. TEESlice delivers the same security protection as shielding the entire DNN model inside TEE (the ``upper-bound&#x27;&#x27; security guarantees) with over 10X less overhead (in both experimental and real-world environments) than prior TSDP solutions and no accuracy loss.

  匹配依据：TEE: trusted execution environments

  </details>

- **LDR: Secure and Efficient Linux Driver Runtime for Embedded TEE Systems.**
  2024 · TEE · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/ldr-secure-and-efficient-linux-driver-runtime-for-embedded-tee-systems/)
  Haobo Li, Lan Luo, Xinhui Shao, Huaiyu Yan, Ping Jiang, Ming Yang, Kai Dong, Xinwen Fu, Junzhou Luo, Zhen Ling

- **HyperTEE: A Decoupled TEE Architecture with Secure Enclave Management.**
  2024 · TEE · 含会议/期刊记录 · [MICRO](https://doi.org/10.1109/MICRO61859.2024.00018)
  Shijun Zhao, Dan Meng, Fengwei Zhang, Peinan Li, Yubiao Huang, Lutan Zhao, Yunkai Bai, Rui Hou, Michael C. Huang

- **GroupCover: A Secure, Efficient and Scalable Inference Framework for On-device Model Protection based on TEEs.**
  2024 · TEE · 含会议/期刊记录 · [ICML](https://proceedings.mlr.press/v235/zhang24bn.html)
  Tianyi Zhang, Zheng Zhang, Jianwei Liu, Yao Zhang, Ye Wu, Na Wang, Ziqi Zhang

- **Gramine-TDX: A Lightweight OS Kernel for Confidential VMs.**
  2024 · TEE · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3658644.3690323)
  Dmitrii Kuvaiskii, Dimitrios Stavrakakis, Cedric Xing, Kailun Qin, Pramod Bhatotia, Mona Vij

- **GlobalConfusion: TrustZone Trusted Application 0-Days by Design.**
  2024 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity24/presentation/busch-globalconfusion)
  Marcel Busch, Philipp Mao, Mathias Payer

- **Faults in Our Bus: Novel Bus Fault Attack to Break ARM TrustZone.**
  2024 · TEE · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/faults-in-our-bus-novel-bus-fault-attack-to-break-arm-trustzone/)
  Nimish Mishra, Debdeep Mukhopadhyay, Anirban Chakraborty

- **Ensuring State Continuity for Confidential Computing: A Blockchain-Based Approach.**
  2024 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2024.3381973)
  Yinqian Zhang, Jianyu Niu, Xiang Li, Wei Peng, Xiaokuan Zhang

- **EnclaveFuzz: Finding Vulnerabilities in SGX Applications.**
  2024 · TEE · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/enclavefuzz-finding-vulnerabilities-in-sgx-applications/)
  Liheng Chen, Baojian Chen, Zheyu Ma, Chao Zhang, Yuan Li, Zheming Li

- **Data Enclave: A Data-Centric Trusted Execution Environment.**
  2024 · TEE · 含会议/期刊记录 · [HPCA](https://doi.org/10.1109/HPCA57654.2024.00026)
  Yan Solihin, James Pangia, Xipeng Shen, Yuanchao Xu, Chencheng Ye

- **CAGE: Complementing Arm CCA with GPU Extensions.**
  2024 · TEE · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/cage-complementing-arm-cca-with-gpu-extensions/)
  Kevin Leach, Chenxu Wang, Shoumeng Yan, Fengwei Zhang, Yunjie Deng, Jiannong Cao, Zhenyu Ning, Zhengyu He

- **Building a Lightweight Trusted Execution Environment for Arm GPUs.**
  2024 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2023.3334277)
  Kevin Leach, Shoumeng Yan, Fengwei Zhang, Zhengyu He, Chenxu Wang, Zhenyu Ning, Jin Li, Yunjie Deng, Jiannong Cao

- **ACAI: Protecting Accelerator Execution with Arm Confidential Computing Architecture**
  2024 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2305.15986) · [USENIX Security](https://www.usenix.org/conference/usenixsecurity24/presentation/sridhara)
  Shweta Shinde, Supraja Sridhara, Mark Kuhne, Benedict Schlüter, Andrin Bertschi, Fabio Aliberti

  <details><summary>摘要 / Abstract</summary>

  Trusted execution environments in several existing and upcoming CPUs demonstrate the success of confidential computing, with the caveat that tenants cannot securely use accelerators such as GPUs and FPGAs. In this paper, we reconsider the Arm Confidential Computing Architecture (CCA) design, an upcoming TEE feature in Armv9-A, to address this gap. We observe that CCA offers the right abstraction and mechanisms to allow confidential VMs to use accelerators as a first-class abstraction. We build ACAI, a CCA-based solution, with a principled approach of extending CCA security invariants to device-side access to address several critical security gaps. Our experimental results on GPU and FPGA demonstrate the feasibility of ACAI while maintaining security guarantees.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **A Quantum Computer Trusted Execution Environment.**
  2024 · TEE · 含会议/期刊记录 · [HPCA](https://doi.org/10.1109/HPCA57654.2024.00051)
  Sanjay Deshpande, Chuanqi Xu, Yao Lu, Theodoros Trochatos, Yongshan Ding, Jakub Szefer

- **A Comprehensive Trusted Runtime for WebAssembly with Intel SGX**
  2024 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2312.09087) · [TDSC](https://doi.org/10.1109/TDSC.2023.3334516)
  Marcelo Pasin, Giovanni Mazzeo, Darshan Vaydia, Valerio Schiavoni, Arne Hollum, Jämes Ménétrey, Pascal Felber

  <details><summary>摘要 / Abstract</summary>

  In real-world scenarios, trusted execution environments (TEEs) frequently host applications that lack the trust of the infrastructure provider, as well as data owners who have specifically outsourced their data for remote processing. We present Twine, a trusted runtime for running WebAssembly-compiled applications within TEEs, establishing a two-way sandbox. Twine leverages memory safety guarantees of WebAssembly (Wasm) and abstracts the complexity of TEEs, empowering the execution of legacy and language-agnostic applications. It extends the standard WebAssembly system interface (WASI), providing controlled OS services, focusing on I/O. Additionally, through built-in TEE mechanisms, Twine delivers attestation capabilities to ensure the integrity of the runtime and the OS services supplied to the application. We evaluate its performance using general-purpose benchmarks and real-world applications, showing it compares on par with state-of-the-art solutions. A case study involving fintech company Credora reveals that Twine can be deployed in production with reasonable performance trade-offs, ranging from a 0.7x slowdown to a 1.17x speedup compared to native run time. Finally, we identify performance improvement through library optimisation, showcasing one such adjustment that leads up to 4.1x speedup. Twine is open-source and has been upstreamed into the original Wasm runtime, WAMR.

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>
