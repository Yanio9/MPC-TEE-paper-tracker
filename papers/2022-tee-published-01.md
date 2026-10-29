# 2022 · TEE · 含会议/期刊记录 · 第 1/1 页

[总目录](../PAPERS.md)

- **Cerberus: A Formal Approach to Secure and Efficient Enclave Memory Sharing**
  2022-09-30 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2209.15253) · [ACM CCS](https://doi.org/10.1145/3548606.3560595)
  Anjo Vahldiek-Oberwagner, Dayeol Lee, Pranav Gaddamadugu, Alexander Thomas, Catherine Lu, Kevin Cheang, Dawn Song, Sanjit A. Seshia, Mona Vij, Krste Asanovic, Krste Asanović

  <details><summary>摘要 / Abstract</summary>

  Hardware enclaves rely on a disjoint memory model, which maps each physical address to an enclave to achieve strong memory isolation. However, this severely limits the performance and programmability of enclave programs. While some prior work proposes enclave memory sharing, it does not provide a formal model or verification of their designs. This paper presents Cerberus, a formal approach to secure and efficient enclave memory sharing. To reduce the burden of formal verification, we compare different sharing models and choose a simple yet powerful sharing model. Based on the sharing model, Cerberus extends an enclave platform such that enclave memory can be made immutable and shareable across multiple enclaves via additional operations. We use incremental verification starting with an existing formal model called the Trusted Abstract Platform (TAP). Using our extended TAP model, we formally verify that Cerberus does not break or weaken the security guarantees of the enclaves despite allowing memory sharing. More specifically, we prove the Secure Remote Execution (SRE) property on our formal model. Finally, the paper shows the feasibility of Cerberus by implementing it in an existing enclave platform, RISC-V Keystone.

  匹配依据：TEE: hardware enclaves

  </details>

- **SoK: TEE-assisted Confidential Smart Contract**
  2022-03-16 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2203.08548) · [PoPETs](https://doi.org/10.56553/POPETS-2022-0093)
  Qi Wang, David Galindo, Qin Wang, Rujia Li, Mark Ryan

  <details><summary>摘要 / Abstract</summary>

  The blockchain-based smart contract lacks privacy since the contract state and instruction code are exposed to the public. Combining smart-contract execution with Trusted Execution Environments (TEEs) provides an efficient solution, called TEE-assisted smart contracts, for protecting the confidentiality of contract states. However, the combination approaches are varied, and a systematic study is absent. Newly released systems may fail to draw upon the experience learned from existing protocols, such as repeating known design mistakes or applying TEE technology in insecure ways. In this paper, we first investigate and categorize the existing systems into two types: the layer-one solution and layer-two solution. Then, we establish an analysis framework to capture their common lights, covering the desired properties (for contract services), threat models, and security considerations (for underlying systems). Based on our taxonomy, we identify their ideal functionalities and uncover the fundamental flaws and reasons for the challenges in each specification design. We believe that this work would provide a guide for the development of TEE-assisted smart contracts, as well as a framework to evaluate future TEE-assisted confidential contract systems.

  匹配依据：TEE: trusted execution environments

  </details>

- **ReZone: Disarming TrustZone with TEE Privilege Reduction**
  2022-03-02 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2203.01025) · [USENIX Security](https://www.usenix.org/conference/usenixsecurity22/presentation/cerdeira)
  Nuno Santos, Sandro Pinto, David Cerdeira, José Martins

  <details><summary>摘要 / Abstract</summary>

  In TrustZone-assisted TEEs, the trusted OS has unrestricted access to both secure and normal world memory. Unfortunately, this architectural limitation has opened an aisle of exploration for attackers, which have demonstrated how to leverage a chain of exploits to hijack the trusted OS and gain full control of the system, targeting (i) the rich execution environment (REE), (ii) all trusted applications (TAs), and (iii) the secure monitor. In this paper, we propose ReZone. The main novelty behind ReZone design relies on leveraging TrustZone-agnostic hardware primitives available on commercially off-the-shelf (COTS) platforms to restrict the privileges of the trusted OS. With ReZone, a monolithic TEE is restructured and partitioned into multiple sandboxed domains named zones, which have only access to private resources. We have fully implemented ReZone for the i.MX 8MQuad EVK and integrated it with Android OS and OP-TEE. We extensively evaluated ReZone using microbenchmarks and real-world applications. ReZone can sustain popular applications like DRM-protected video encoding with acceptable performance overheads. We have surveyed 80 CVE vulnerability reports and estimate that ReZone could mitigate 86.84% of them.

  匹配依据：TEE: trustzone

  </details>

- **Trust Dies in Darkness: Shedding Light on Samsung's TrustZone Keymaster Design**
  2022-02-21 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity22/presentation/shakevsky) · [IACR ePrint](https://eprint.iacr.org/2022/208)
  Eyal Ronen, Alon Shakevsky, Avishai Wool

  <details><summary>摘要 / Abstract</summary>

  ARM-based Android smartphones rely on the TrustZone hardware support for a Trusted Execution Environment (TEE) to implement security-sensitive functions. The TEE runs a separate, isolated, TrustZone Operating System (TZOS), in parallel to Android. The implementation of the cryptographic functions within the TZOS is left to the device vendors, who create proprietary undocumented designs. In this work, we expose the cryptographic design and implementation of Android&#x27;s Hardware-Backed Keystore in Samsung&#x27;s Galaxy S8, S9, S10, S20, and S21 flagship devices. We reversed-engineered and provide a detailed description of the cryptographic design and code structure, and we unveil severe design flaws. We present an IV reuse attack on AES-GCM that allows an attacker to extract hardware-protected key material, and a downgrade attack that makes even the latest Samsung devices vulnerable to the IV reuse attack. We demonstrate working key extraction attacks on the latest devices. We also show the implications of our attacks on two higher-level cryptographic protocols between the TrustZone and a remote server: we demonstrate a working FIDO2 WebAuthn login bypass and a compromise of Google’s Secure Key Import. We discuss multiple flaws in the design flow of TrustZone based protocols. Although our specific attacks only apply to the $\approx$100 million devices made by Samsung, it raises the much more general requirement for open and proven standards for critical cryptographic and security designs.

  匹配依据：TEE: trusted execution environment, trustzone

  </details>

- **vSGX: Virtualizing SGX Enclaves on AMD SEV.**
  2022 · TEE · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP46214.2022.9833694)
  Mengyuan Li, Shixuan Zhao, Yinqian Zhang, Zhiqiang Lin

- **Smile: Secure Memory Introspection for Live Enclave.**
  2022 · TEE · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP46214.2022.9833714)
  Fengwei Zhang, Xuhua Ding, Lei Zhou

- **SGXTuner: Performance Enhancement of Intel SGX Applications Via Stochastic Optimization.**
  2022 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2021.3064391)
  Giovanni Mazzeo, Sergei Arnautov, Luigi Romano, Christof Fetzer

- **SGXLock: Towards Efficiently Establishing Mutual Distrust Between Host Application and Enclave for SGX.**
  2022 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity22/presentation/chen-yuan)
  Guorui Xu, Jiaqi Li, Cong Wang, Yajin Zhou, Kui Ren, Zhi Wang, Yuan Chen

- **SGXFuzz: Efficiently Synthesizing Nested Structures for SGX Enclave Fuzzing.**
  2022 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity22/presentation/cloosters)
  Johannes Willbold, Tobias Cloosters, Lucas Davi, Thorsten Holz

- **SEFrame: An SGX-enhanced Smart Contract Execution Framework for Permissioned Blockchain.**
  2022 · TEE · 含会议/期刊记录 · [ICDE](https://doi.org/10.1109/ICDE53745.2022.00289)
  Xinna Zhou, Zhao Zhang, Aoying Zhou, Min Fang, Cheqing Jin

- **Rphx: Result Pattern Hiding Conjunctive Query Over Private Compressed Index Using Intel SGX.**
  2022 · TEE · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2022.3144877)
  Yong Qi, Saiyu Qi, Jianfeng Wang, Ee-Chien Chang, Qin Jiang, Pengfei Wu

- **Repurposing Segmentation as a Practical LVI-NULL Mitigation in SGX.**
  2022 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity22/presentation/giner)
  Michael Schwarz, Daniel Gruss, Claudio Canella, Andreas Kogler, Lukas Giner

- **RT-TEE: Real-time System Availability for Cyber-physical Systems using ARM TrustZone.**
  2022 · TEE · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP46214.2022.9833604)
  Ning Zhang, Jinwen Wang, Ao Li, Haoran Li, Chenyang Lu

- **Pistis: Issuing Trusted and Authorized Certificates With Distributed Ledger and TEE.**
  2022 · TEE · 含会议/期刊记录 · [TPDS](https://doi.org/10.1109/TPDS.2021.3121562)
  Zecheng Li, Haotian Wu, Yuanyuan Yang, Bin Xiao, Laphou Lao, Songtao Guo

- **Minimum Viable Device Drivers for ARM TrustZone**
  2022 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2110.08303) · [EuroSys](https://doi.org/10.1145/3492321.3519565)
  Felix Xiaozhu Lin, Liwei Guo

  <details><summary>摘要 / Abstract</summary>

  While TrustZone can isolate IO hardware, it lacks drivers for modern IO devices. Rather than porting drivers, we propose a novel approach to deriving minimum viable drivers: developers exercise a full driver and record the driver/device interactions; the processed recordings, dubbed driverlets, are replayed in the TEE at run time to access IO devices. Driverlets address two key challenges: correctness and expressiveness, for which they build on a key construct called interaction template. The interaction template ensures faithful reproduction of recorded IO jobs (albeit on new IO data); it accepts dynamic input values; it tolerates nondeterministic device behaviors. We demonstrate driverlets on a series of sophisticated devices, making them accessible to TrustZone for the first time to our knowledge. Our experiments show that driverlets are secure, easy to build, and incur acceptable overhead (1.4x -2.7x compared to native drivers). Driverlets fill a critical gap in the TrustZone TEE, realizing its long-promised vision of secure IO.

  匹配依据：TEE: trustzone

  </details>

- **Minefield: A Software-only Protection for SGX Enclaves against DVFS Attacks.**
  2022 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity22/presentation/kogler-minefield)
  Michael Schwarz, Daniel Gruss, Andreas Kogler

- **Malware in the SGX Supply Chain: Be Careful When Signing Enclaves!**
  2022 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2020.3024562)
  Rafael Pires, Emanuel Onica, Andrei Mogage, Vlad Constantin Craciun, Pascal Felber

- **MAGE: Mutual Attestation for a Group of Enclaves without Trusted Third Parties**
  2022 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2008.09501) · [USENIX Security](https://www.usenix.org/conference/usenixsecurity22/presentation/chen-guoxing)
  Guoxing Chen, Yinqian Zhang

  <details><summary>摘要 / Abstract</summary>

  Intel Software Guard Extensions (SGX) local and remote attestation mechanisms enable an enclave to attest its identity (i.e., the enclave measurement, which is the cryptographic hash of its initial code and data) to an enclave. To verify that the attested identity is trusted, one enclave usually includes the measurement of the enclave it trusts into its initial data in advance assuming no trusted third parties are available during runtime to provide this piece of information. However, when mutual trust between these two enclaves is required, it is infeasible to simultaneously include into their own initial data the other&#x27;s measurements respectively as any change to the initial data will change their measurements, making the previously included measurements invalid. In this paper, we propose MAGE, a framework enabling a group of enclaves to mutually attest each other without trusted third parties. Particularly, we introduce a technique to instrument these enclaves so that each of them could derive the others&#x27; measurements using information solely from its own initial data. We also provide a prototype implementation based on Intel SGX SDK, to facilitate enclave developers to adopt this technique.

  匹配依据：TEE: intel sgx, sgx

  </details>

- **Differentially Oblivious Data Analysis With Intel SGX: Design, Optimization, and Evaluation.**
  2022 · TEE · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2021.3106317)
  Jianting Ning, Qi Li, Wei Wu, Xinyi Huang, Pengfei Wu

- **Design and Verification of the Arm Confidential Compute Architecture.**
  2022 · TEE · 含会议/期刊记录 · [OSDI](https://www.usenix.org/conference/osdi22/presentation/li)
  Ronghui Gu, Christoffer Dall, Yousuf Sait, Gareth Stockwell, Xuheng Li, Xupeng Li, Jason Nieh

- **Composite Enclaves: Towards Disaggregated Trusted Execution**
  2022 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2010.10416) · [TCHES](https://doi.org/10.46586/TCHES.V2022.I1.630-656)
  Aritra Dhar, Moritz Schneider, Ivan Puddu, Kari Kostiainen, Srdjan Capkun

  <details><summary>摘要 / Abstract</summary>

  The ever-rising computation demand is forcing the move from the CPU to heterogeneous specialized hardware, which is readily available across modern datacenters through disaggregated infrastructure. On the other hand, trusted execution environments (TEEs), one of the most promising recent developments in hardware security, can only protect code confined in the CPU, limiting TEEs&#x27; potential and applicability to a handful of applications. We observe that the TEEs&#x27; hardware trusted computing base (TCB) is fixed at design time, which in practice leads to using untrusted software to employ peripherals in TEEs. Based on this observation, we propose \emph{composite enclaves} with a configurable hardware and software TCB, allowing enclaves access to multiple computing and IO resources. Finally, we present two case studies of composite enclaves: i) an FPGA platform based on RISC-V Keystone connected to emulated peripherals and sensors, and ii) a large-scale accelerator. These case studies showcase a flexible but small TCB (2.5 KLoC for IO peripherals and drivers), with a low-performance overhead (only around 220 additional cycles for a context switch), thus demonstrating the feasibility of our approach and showing that it can work with a wide range of specialized hardware.

  匹配依据：TEE: trusted execution environments

  </details>

- **Composable Cachelets: Protecting Enclaves from Cache Side-Channel Attacks.**
  2022 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity22/presentation/townley)
  Yu David Liu, Kerem Arikan, Daniel Townley, Dmitry V. Ponomarev, Oguz Ergin

- **CRONUS: Fault-isolated, Secure and High-performance Heterogeneous Computing for Trusted Execution Environment.**
  2022 · TEE · 含会议/期刊记录 · [MICRO](https://doi.org/10.1109/MICRO56248.2022.00019)
  Shixiong Zhao, Tianxiang Shen, Jianyu Jiang, Sen Wang, Heming Cui, Xiapu Luo, Ji Qi, Xusheng Chen, Li Chen, Gong Zhang

- **Abusing Trust: Mobile Kernel Subversion via TrustZone Rootkits.**
  2022 · TEE · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SPW54247.2022.9833891)
  Thomas Grechenig, Christian Schanes, Daniel Marth, Clemens Hlauschek

- **A Systematic Look at Ciphertext Side Channels on AMD SEV-SNP.**
  2022 · TEE · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP46214.2022.9833768)
  Radu Teodorescu, Mengyuan Li, Jan Wichelmann, Luca Wilke, Thomas Eisenbarth, Yinqian Zhang

- **A Hardware-Software Co-design for Efficient Intra-Enclave Isolation.**
  2022 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity22/presentation/gu-jinyu)
  Jinyu Gu, Yubin Xia, Bojun Zhu, Wentai Li, Haibo Chen, Mingyu Li
