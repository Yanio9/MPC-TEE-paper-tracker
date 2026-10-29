# 2021 · TEE · 含会议/期刊记录 · 第 1/1 页

[总目录](../PAPERS.md)

- **SmashEx: Smashing SGX Enclaves Using Exceptions.**
  2021-10-13 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2110.06657) · [ACM CCS](https://doi.org/10.1145/3460120.3484821)
  Shweta Shinde, Jinhua Cui, Zhijingcheng Yu, Zhiping Cai, Prateek Saxena, Jason Zhijingcheng Yu

  <details><summary>摘要 / Abstract</summary>

  Exceptions are a commodity hardware functionality which is central to multi-tasking OSes as well as event-driven user applications. Normally, the OS assists the user application by lifting the semantics of exceptions received from hardware to program-friendly user signals and exception handling interfaces. However, can exception handlers work securely in user enclaves, such as those enabled by Intel SGX, where the OS is not trusted by the enclave code? In this paper, we introduce a new attack called SmashEx which exploits the OS-enclave interface for asynchronous exceptions in SGX. It demonstrates the importance of a fundamental property of safe atomic execution that is required on this interface. In the absence of atomicity, we show that asynchronous exception handling in SGX enclaves is complicated and prone to re-entrancy vulnerabilities. Our attacks do not assume any memory errors in the enclave code, side channels, or application-specific logic flaws. We concretely demonstrate exploits that cause arbitrary disclosure of enclave private memory and code-reuse (ROP) attacks in the enclave. We show reliable exploits on two widely-used SGX runtimes, Intel SGX SDK and Microsoft Open Enclave, running OpenSSL and cURL libraries respectively. We tested a total of 14 frameworks, including Intel SGX SDK and Microsoft Open Enclave, 10 of which are vulnerable. We discuss how the vulnerability manifests on both SGX1-based and SGX2-based platforms. We present potential mitigation and long-term defenses for SmashEx.

  匹配依据：TEE: intel sgx, sgx, sgx enclaves

  </details>

- **IceClave: A Trusted Execution Environment for In-Storage Computing.**
  2021-09-08 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2109.03373) · [MICRO](https://doi.org/10.1145/3466752.3480109)
  Hyung Jin Lim, Changhwan Youn, Jongryool Kim, Myeong Joon Kang, Yuqi Xue, Luyi Kang, Weiwei Jia, Bruce L. Jacob, Jian Huang, Xiaohao Wang, Bruce Jacob

  <details><summary>摘要 / Abstract</summary>

  In-storage computing with modern solid-state drives (SSDs) enables developers to offload programs from the host to the SSD. It has been proven to be an effective approach to alleviate the I/O bottleneck. To facilitate in-storage computing, many frameworks have been proposed. However, few of them treat the in-storage security as the first citizen. Specifically, since modern SSD controllers do not have a trusted execution environment, an offloaded (malicious) program could steal, modify, and even destroy the data stored in the SSD. In this paper, we first investigate the attacks that could be conducted by offloaded in-storage programs. To defend against these attacks, we build a lightweight trusted execution environment, named IceClave for in-storage computing. IceClave enables security isolation between in-storage programs and flash management functions that include flash address translation, data access control, and garbage collection, with TrustZone extensions. IceClave also achieves security isolation between in-storage programs by enforcing memory integrity verification of in-storage DRAM with low overhead. To protect data loaded from flash chips, IceClave develops a lightweight data encryption/decryption mechanism in flash controllers. We develop IceClave with a full system simulator. We evaluate IceClave with a variety of data-intensive applications such as databases. Compared to state-of-the-art in-storage computing approaches, IceClave introduces only 7.6% performance overhead, while enforcing security isolation in the SSD controller with minimal hardware cost. IceClave still keeps the performance benefit of in-storage computing by delivering up to 2.31$\times$ better performance than the conventional host-based trusted computing approach.

  匹配依据：TEE: trusted execution environment, trustzone

  </details>

- **One Glitch to Rule Them All: Fault Injection Attacks Against AMD's Secure Encrypted Virtualization.**
  2021-08-10 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2108.04575) · [ACM CCS](https://doi.org/10.1145/3460120.3484779)
  Thilo Krachenfels, Robert Buhren, Hans Niklas Jacob, Jean-Pierre Seifert

  <details><summary>摘要 / Abstract</summary>

  AMD Secure Encrypted Virtualization (SEV) offers protection mechanisms for virtual machines in untrusted environments through memory and register encryption. To separate security-sensitive operations from software executing on the main x86 cores, SEV leverages the AMD Secure Processor (AMD-SP). This paper introduces a new approach to attack SEV-protected virtual machines (VMs) by targeting the AMD-SP. We present a voltage glitching attack that allows an attacker to execute custom payloads on the AMD-SPs of all microarchitectures that support SEV currently on the market (Zen 1, Zen 2, and Zen 3). The presented methods allow us to deploy a custom SEV firmware on the AMD-SP, which enables an adversary to decrypt a VM&#x27;s memory. Furthermore, using our approach, we can extract endorsement keys of SEV-enabled CPUs, which allows us to fake attestation reports or to pose as a valid target for VM migration without requiring physical access to the target host. Moreover, we reverse-engineered the Versioned Chip Endorsement Key (VCEK) mechanism introduced with SEV Secure Nested Paging (SEV-SNP). The VCEK binds the endorsement keys to the firmware version of TCB components relevant for SEV. Building on the ability to extract the endorsement keys, we show how to derive valid VCEKs for arbitrary firmware versions. With our findings, we prove that SEV cannot adequately protect confidential data in cloud environments from insider attackers, such as rogue administrators, on currently available CPUs.

  匹配依据：TEE: secure encrypted virtualization, sev snp

  </details>

- **What Is the Price for Joining Securely? Benchmarking Equi-Joins in Trusted Execution Environments.**
  2021 · TEE · 含会议/期刊记录 · [PVLDB](https://doi.org/10.14778/3494124.3494146)
  Jorge-Arnulfo Quiané-Ruiz, Jonas Traub, Kajetan Jeremi Maliszewski, Volker Markl

- **VoltPillager: Hardware-based fault injection attacks against Intel SGX Enclaves using the SVID voltage scaling interface.**
  2021 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity21/presentation/chen-zitai)
  David F. Oswald, Edward Dean, Georgios Vasilakis, Kit Murdock, Zitai Chen, Flavio D. Garcia

- **VeriDB: An SGX-based Verifiable Database.**
  2021 · TEE · 含会议/期刊记录 · [SIGMOD](https://doi.org/10.1145/3448016.3457308)
  Yanqing Peng, Sheng Wang, Yifan Cai, Feifei Li, Ke Ma, Wenchao Zhou

- **Utilizing and Extending Trusted Execution Environment in Heterogeneous SoCs for a Pay-Per-Device IP Licensing Scheme.**
  2021 · TEE · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2021.3058777)
  Sven Nitzsche, Nadir Khan, Asier Garciandia López, Jürgen Becker

- **SGX-MR: Regulating Dataflows for Protecting Access Patterns of Data-Intensive SGX Applications.**
  2021 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2009.03518) · [PoPETs](https://doi.org/10.2478/POPETS-2021-0002)
  Sagar Sharma, A. K. M. Mubashwir Alam, Keke Chen, A K M Mubashwir Alam

  <details><summary>摘要 / Abstract</summary>

  Intel SGX has been a popular trusted execution environment (TEE) for protecting the integrity and confidentiality of applications running on untrusted platforms such as cloud. However, the access patterns of SGX-based programs can still be observed by adversaries, which may leak important information for successful attacks. Researchers have been experimenting with Oblivious RAM (ORAM) to address the privacy of access patterns. ORAM is a powerful low-level primitive that provides application-agnostic protection for any I/O operations, however, at a high cost. We find that some application-specific access patterns, such as sequential block I/O, do not provide additional information to adversaries. Others, such as sorting, can be replaced with specific oblivious algorithms that are more efficient than ORAM. The challenge is that developers may need to look into all the details of application-specific access patterns to design suitable solutions, which is time-consuming and error-prone. In this paper, we present the lightweight SGX based MapReduce (SGX-MR) approach that regulates the dataflow of data-intensive SGX applications for easier application-level access-pattern analysis and protection. It uses the MapReduce framework to cover a large class of data-intensive applications, and the entire framework can be implemented with a small memory footprint. With this framework, we have examined the stages of data processing, identified the access patterns that need protection, and designed corresponding efficient protection methods. Our experiments show that SGX-MR based applications are much more efficient than ORAM-based implementations.

  匹配依据：TEE: intel sgx, sgx, trusted execution environment

  </details>

- **QShield: Protecting Outsourced Cloud Data Queries With Multi-User Access Control Based on SGX.**
  2021 · TEE · 含会议/期刊记录 · [TPDS](https://doi.org/10.1109/TPDS.2020.3024880)
  Dan Liu, Zheng Yan, Yaxing Chen, Qinghua Zheng

- **High-Performance Smart Contracts Concurrent Execution for Permissioned Blockchain Using SGX.**
  2021 · TEE · 含会议/期刊记录 · [ICDE](https://doi.org/10.1109/ICDE51399.2021.00175)
  Zhao Zhang, Aoying Zhou, Min Fang, Cheqing Jin

- **Frontal Attack: Leaking Control-Flow in SGX via the CPU Frontend.**
  2021 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2005.11516) · [USENIX Security](https://www.usenix.org/conference/usenixsecurity21/presentation/puddu)
  Moritz Schneider, Ivan Puddu, Miro Haller, Srdjan Capkun, Srdjan Čapkun

  <details><summary>摘要 / Abstract</summary>

  We introduce a new timing side-channel attack on Intel CPU processors. Our Frontal attack exploits timing differences that arise from how the CPU frontend fetches and processes instructions while being interrupted. In particular, we observe that in modern Intel CPUs, some instructions&#x27; execution times will depend on which operations precede and succeed them, and on their virtual addresses. Unlike previous attacks that could only profile branches if they contained different code or had known branch targets, the Frontal attack allows the adversary to distinguish between instruction-wise identical branches. As the attack requires OS capabilities to set the interrupts, we use it to exploit SGX enclaves. Our attack further demonstrates that secret-dependent branches should not be used even alongside defenses to current controlled-channel attacks. We show that the adversary can use the Frontal attack to extract a secret from an SGX enclave if that secret was used as a branching condition for two instruction-wise identical branches. We successfully tested the attack on all the available Intel CPUs with SGX (until 10th gen) and used it to leak information from two commonly used cryptographic libraries.

  匹配依据：TEE: sgx, sgx enclave, sgx enclaves

  </details>

- **CrossLine: Breaking "Security-by-Crash" based Memory Isolation in AMD SEV.**
  2021 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2008.00146) · [ACM CCS](https://doi.org/10.1145/3460120.3485253)
  Mengyuan Li, Zhiqiang Lin, Yinqian Zhang

  <details><summary>摘要 / Abstract</summary>

  AMD&#x27;s Secure Encrypted Virtualization (SEV) is an emerging security feature on AMD processors that allows virtual machines to run on encrypted memory and perform confidential computing even with an untrusted hypervisor. This paper first demystifies SEV&#x27;s improper use of address space identifier (ASID) for controlling accesses of a VM to encrypted memory pages, cache lines, and TLB entries. We then present the CROSSLINE attacks, a novel class of attacks against SEV that allow the adversary to launch an attacker VM and change its ASID to that of the victim VM to impersonate the victim. We present two variants of CROSSLINE attacks: CROSSLINE V1 decrypts victim&#x27;s page tables or memory blocks following the format of a page table entry; CROSSLINE V2 constructs encryption and decryption oracles by executing instructions of the victim VM. We have successfully performed CROSSLINE attacks on SEV and SEV-ES processors.

  匹配依据：TEE: amd sev, confidential computing, secure encrypted virtualization

  </details>

- **Confidential computing for OpenPOWER.**
  2021 · TEE · 含会议/期刊记录 · [EuroSys](https://doi.org/10.1145/3447786.3456243)
  Brad Frey, Lawrence Roy, Jeffrey Stuecheli, Enriquillo Valdez, Laurent Dufour, Mohit Kapur, Janani Janakirman, Wendel Voigt, Michael V. Le, William A. Starke, Ryan Grimm, Bharata Bhasker Rao, John M. Ludden, Kenneth A. Goldman, Ramachandra Pai, Sukadev Bhattiprolu, Cathy May, Guerney D. H. Hunt, Hani Jamjoom, Paul Mackerras, Rick Boivie, Elaine R. Palmer

- **Confidential Serverless Made Efficient with Plug-In Enclaves.**
  2021 · TEE · 含会议/期刊记录 · [ISCA](https://doi.org/10.1109/ISCA52012.2021.00032)
  Yubin Xia, Haibo Chen, Mingyu Li

- **CURE: A Security Architecture with CUstomizable and Resilient Enclaves.**
  2021 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2010.15866) · [USENIX Security](https://www.usenix.org/conference/usenixsecurity21/presentation/bahmani)
  Ferdinand Brasser, Ghada Dessouky, Raad Bahmani, Patrick Jauernig, Matthias Klimmek, Emmanuel Stapf, Ahmad-Reza Sadeghi

  <details><summary>摘要 / Abstract</summary>

  Security architectures providing Trusted Execution Environments (TEEs) have been an appealing research subject for a wide range of computer systems, from low-end embedded devices to powerful cloud servers. The goal of these architectures is to protect sensitive services in isolated execution contexts, called enclaves. Unfortunately, existing TEE solutions suffer from significant design shortcomings. First, they follow a one-size-fits-all approach offering only a single enclave type, however, different services need flexible enclaves that can adjust to their demands. Second, they cannot efficiently support emerging applications (e.g., Machine Learning as a Service), which require secure channels to peripherals (e.g., accelerators), or the computational power of multiple cores. Third, their protection against cache side-channel attacks is either an afterthought or impractical, i.e., no fine-grained mapping between cache resources and individual enclaves is provided. In this work, we propose CURE, the first security architecture, which tackles these design challenges by providing different types of enclaves: (i) sub-space enclaves provide vertical isolation at all execution privilege levels, (ii) user-space enclaves provide isolated execution to unprivileged applications, and (iii) self-contained enclaves allow isolated execution environments that span multiple privilege levels. Moreover, CURE enables the exclusive assignment of system resources, e.g., peripherals, CPU cores, or cache resources to single enclaves. CURE requires minimal hardware changes while significantly improving the state of the art of hardware-assisted security architectures. We implemented CURE on a RISC-V-based SoC and thoroughly evaluated our prototype in terms of hardware and performance overhead. CURE imposes a geometric mean performance overhead of 15.33% on standard benchmarks.

  匹配依据：TEE: trusted execution environments

  </details>

- **CIPHERLEAKS: Breaking Constant-time Cryptography on AMD SEV via the Ciphertext Side Channel.**
  2021 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity21/presentation/li-mengyuan)
  Mengyuan Li, Huibo Wang, Yueqiang Cheng, Kang Li, Yinqian Zhang
