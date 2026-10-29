# 2020 · TEE · 含会议/期刊记录 · 第 1/1 页

[总目录](../PAPERS.md)

- **TeeRex: Discovery and Exploitation of Memory Corruption Vulnerabilities in SGX Enclaves**
  2020-07-15 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2007.07586) · [USENIX Security](https://www.usenix.org/conference/usenixsecurity20/presentation/cloosters)
  Michael Rodler, Tobias Cloosters, Lucas Davi

  <details><summary>摘要 / Abstract</summary>

  Intel&#x27;s Software Guard Extensions (SGX) introduced new instructions to switch the processor to enclave mode which protects it from introspection. While the enclave mode strongly protects the memory and the state of the processor, it cannot withstand memory corruption errors inside the enclave code. In this paper, we show that the attack surface of SGX enclaves provides new challenges for enclave developers as exploitable memory corruption vulnerabilities are easily introduced into enclave code. We develop TeeRex to automatically analyze enclave binary code for vulnerabilities introduced at the host-to-enclave boundary by means of symbolic execution. Our evaluation on public enclave binaries reveal that many of them suffer from memory corruption errors allowing an attacker to corrupt function pointers or perform arbitrary memory writes. As we will show, TeeRex features a specifically tailored framework for SGX enclaves that allows simple proof-of-concept exploit construction to assess the discovered vulnerabilities. Our findings reveal vulnerabilities in multiple enclaves, including enclaves developed by Intel, Baidu, and WolfSSL, as well as biometric fingerprint software deployed on popular laptop brands.

  匹配依据：TEE: sgx, sgx enclaves

  </details>

- **Occlum: Secure and Efficient Multitasking Inside a Single Enclave of Intel SGX**
  2020-01-21 · TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2001.07450) · [ASPLOS](https://doi.org/10.1145/3373376.3378469)
  Yi Xu, Yubin Xia, Shoumeng Yan, Youren Shen, Runji Wang, Hongliang Tian, Kang Chen, Yu Chen

  <details><summary>摘要 / Abstract</summary>

  Intel Software Guard Extensions (SGX) enables user-level code to create private memory regions called enclaves, whose code and data are protected by the CPU from software and hardware attacks outside the enclaves. Recent work introduces library operating systems (LibOSes) to SGX so that legacy applications can run inside enclaves with few or even no modifications. As virtually any non-trivial application demands multiple processes, it is essential for LibOSes to support multitasking. However, none of the existing SGX LibOSes support multitasking both securely and efficiently. This paper presents Occlum, a system that enables secure and efficient multitasking on SGX. We implement the LibOS processes as SFI-Isolated Processes (SIPs). SFI is a software instrumentation technique for sandboxing untrusted modules (called domains). We design a novel SFI scheme named MPX-based, Multi-Domain SFI (MMDSFI) and leverage MMDSFI to enforce the isolation of SIPs. We also design an independent verifier to ensure the security guarantees of MMDSFI. With SIPs safely sharing the single address space of an enclave, the LibOS can implement multitasking efficiently. The Occlum LibOS outperforms the state-of-the-art SGX LibOS on multitasking-heavy workloads by up to 6,600X on micro-benchmarks and up to 500X on application benchmarks.

  匹配依据：TEE: intel sgx, sgx

  </details>

- **Unearthing the TrustedCore: A Critical Review on Huawei's Trusted Execution Environment.**
  2020 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/woot20/presentation/busch)
  Tilo Müller, Marcel Busch, Johannes Westphal

- **TRUSTORE: Side-Channel Resistant Storage for SGX using Intel Hybrid CPU-FPGA.**
  2020 · TEE · 含会议/期刊记录 · [ACM CCS](https://doi.org/10.1145/3372297.3417265)
  Seonghyun Park, Adil Ahmad, Hyunyoung Oh, Yunheung Paek, Byoungyoung Lee

- **SoK: Understanding the Prevailing Security Vulnerabilities in TrustZone-assisted TEE Systems.**
  2020 · TEE · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP40000.2020.00061)
  Nuno Santos, Pedro Fonseca, Sandro Pinto, David Cerdeira

- **SecGrid: A Secure and Efficient SGX-Enabled Smart Grid System With Rich Functionalities.**
  2020 · TEE · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2019.2938875)
  Peilin Hong, Hao Yue, Nenghai Yu, Shaohua Li, David S. L. Wei, Kaiping Xue

- **SENG, the SGX-Enforcing Network Gateway: Authorizing Communication from Shielded Clients.**
  2020 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity20/presentation/schwarz)
  Christian Rossow, Fabian Schwarz

- **Plundervolt: Software-based Fault Injection Attacks against Intel SGX.**
  2020 · TEE · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP40000.2020.00057)
  David F. Oswald, Daniel Gruss, Jo Van Bulck, Kit Murdock, Flavio D. Garcia, Frank Piessens

- **PARTEMU: Enabling Dynamic Analysis of Real-World TrustZone Software Using Emulation.**
  2020 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity20/presentation/harrison)
  Rohan Padhye, Michael Grace, Koushik Sen, Hayawardh Vijayakumar, Lee Harrison

- **Oblivious coopetitive analytics using hardware enclaves.**
  2020 · TEE · 含会议/期刊记录 · [EuroSys](https://doi.org/10.1145/3342195.3387552)
  Chester Leung, Raluca A. Popa, Ankur Dave, Joseph Gonzalez, Ion Stoica

- **Nested Enclave: Supporting Fine-grained Hierarchical Isolation with SGX.**
  2020 · TEE · 含会议/期刊记录 · [ISCA](https://doi.org/10.1109/ISCA45697.2020.00069)
  Joongun Park, Naegyeong Kang, Taehoon Kim, Jaehyuk Huh, Youngjin Kwon

- **MPTEE: bringing flexible and efficient memory protection to Intel SGX.**
  2020 · TEE · 含会议/期刊记录 · [EuroSys](https://doi.org/10.1145/3342195.3387536)
  Yong Qi, Saiyu Qi, Wenjia Zhao, Kangjie Lu

- **Keystone: an open framework for architecting trusted execution environments.**
  2020 · TEE · 含会议/期刊记录 · [EuroSys](https://doi.org/10.1145/3342195.3387532)
  David Kohlbrenner, Shweta Shinde, Dayeol Lee, Krste Asanovic, Dawn Song

- **HybCache: Hybrid Side-Channel-Resilient Caches for Trusted Execution Environments.**
  2020 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity20/presentation/dessouky)
  Ghada Dessouky, Tommaso Frassetto, Ahmad-Reza Sadeghi

- **Establishing Trusted I/O Paths for SGX Client Systems With Aurora.**
  2020 · TEE · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2019.2945621)
  Lin Jiang, Yixiu Chen, Zhuosi Xie, Tianqi Yang, Mingyu Li, Hongliang Liang

- **Enabling Rack-scale Confidential Computing using Heterogeneous Trusted Execution Environment.**
  2020 · TEE · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP40000.2020.00054)
  XiaoFeng Wang, Dan Meng, Boyan Zhao, Jiameng Ying, Jiangfeng Cao, Zhongpu Wang, Rui Hou, Yuhui Zhang, Lixin Zhang, Jianping Zhu, Wenhao Wang

- **Civet: An Efficient Java Partitioning Framework for Hardware Enclaves.**
  2020 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity20/presentation/tsai)
  Jeongseok Son, Bhushan Jain, Donald E. Porter, John McAvey, Chia-Che Tsai, Raluca A. Popa

- **COIN Attacks: On Insecurity of Enclave Untrusted Interfaces in SGX.**
  2020 · TEE · 含会议/期刊记录 · [ASPLOS](https://doi.org/10.1145/3373376.3378486)
  Mustakimur Khandaker, Yueqiang Cheng, Zhi Wang, Tao Wei

- **Bluethunder: A 2-level Directional Predictor Based Side-Channel Attack against SGX.**
  2020 · TEE · 含会议/期刊记录 · [CHES](https://doi.org/10.13154/TCHES.V2020.I1.321-347)
  Pei Zhao, Chunliang Hao, Tianlin Huo, Xiaoni Meng, Wenhao Wang, Mingshu Li, Jian Zhai

- **An Off-Chip Attack on Hardware Enclaves via the Memory Bus.**
  2020 · TEE · 含会议/期刊记录 · [USENIX Security](https://www.usenix.org/conference/usenixsecurity20/presentation/lee-dayeol)
  Chia-Che Tsai, Ian T. Fang, Dongha Jung, Dayeol Lee, Raluca A. Popa
