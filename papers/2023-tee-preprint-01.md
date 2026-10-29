# 2023 · TEE · 仅预印本来源 · 第 1/1 页

[总目录](../PAPERS.md)

- **Trusted Execution Environment for Decentralized Process Mining**
  2023-12-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2312.12105)
  Valerio Goretti, Davide Basile, Luca Barbaro, Claudio Di Ciccio

  <details><summary>摘要 / Abstract</summary>

  Inter-organizational business processes involve multiple independent organizations collaborating to achieve mutual interests. Process mining techniques have the potential to allow these organizations to enhance operational efficiency, improve performance, and deepen the understanding of their business based on the recorded process event data. However, inter-organizational process mining faces substantial challenges, including topical secrecy concerns: The involved organizations may not be willing to expose their own data to run mining algorithms jointly with their counterparts or third parties. In this paper, we introduce CONFINE, a novel approach that unlocks process mining on multiple actors&#x27; process event data while safeguarding the secrecy and integrity of the original records in an inter-organizational business setting. To ensure that the phases of the presented interaction protocol are secure and that the processed information is hidden from involved and external actors alike, our approach resorts to a decentralized architecture comprised of trusted applications running in Trusted Execution Environments (TEEs). We show the feasibility of our solution by showcasing its application to a healthcare scenario and evaluating our implementation in terms of memory usage and scalability on real-world event logs.

  匹配依据：TEE: trusted execution environment, trusted execution environments

  </details>

- **QuanShield: Protecting against Side-Channels Attacks using Self-Destructing Enclaves**
  2023-12-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2312.11796)
  Shujie Cui, Haohua Li, Yuanhong Li, Zhi Zhang, Lluís Vilanova, Peter Pietzuch

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) allow user processes to create enclaves that protect security-sensitive computation against access from the OS kernel and the hypervisor. Recent work has shown that TEEs are vulnerable to side-channel attacks that allow an adversary to learn secrets shielded in enclaves. The majority of such attacks trigger exceptions or interrupts to trace the control or data flow of enclave execution. We propose QuanShield, a system that protects enclaves from side-channel attacks that interrupt enclave execution. The main idea behind QuanShield is to strengthen resource isolation by creating an interrupt-free environment on a dedicated CPU core for running enclaves in which enclaves terminate when interrupts occur. QuanShield avoids interrupts by exploiting the tickless scheduling mode supported by recent OS kernels. QuanShield then uses the save area (SA) of the enclave, which is used by the hardware to support interrupt handling, as a second stack. Through an LLVM-based compiler pass, QuanShield modifies enclave instructions to store/load memory references, such as function frame base addresses, to/from the SA. When an interrupt occurs, the hardware overwrites the data in the SA with CPU state, thus ensuring that enclave execution fails. Our evaluation shows that QuanShield significantly raises the bar for interrupt-based attacks with practical overhead.

  匹配依据：TEE: trusted execution environments

  </details>

- **Fortress: Securing IoT Peripherals with Trusted Execution Environments**
  2023-12-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2312.02542)
  Peterson Yuhala, Jämes Ménétrey, Pascal Felber, Marcelo Pasin, Valerio Schiavoni

  <details><summary>摘要 / Abstract</summary>

  With the increasing popularity of Internet of Things (IoT) devices, securing sensitive user data has emerged as a major challenge. These devices often collect confidential information, such as audio and visual data, through peripheral inputs like microphones and cameras. Such sensitive information is then exposed to potential threats, either from malicious software with high-level access rights or transmitted (sometimes inadvertently) to untrusted cloud services. In this paper, we propose a generic design to enhance the privacy in IoT-based systems by isolating peripheral I/O memory regions in a secure kernel space of a trusted execution environment (TEE). Only a minimal set of peripheral driver code, resident within the secure kernel, can access this protected memory area. This design effectively restricts any unauthorised access by system software, including the operating system and hypervisor. The sensitive peripheral data is then securely transferred to a user-space TEE, where obfuscation mechanisms can be applied before it is relayed to third parties, e.g., the cloud. To validate our architectural approach, we provide a proof-of-concept implementation of our design by securing an audio peripheral based on inter-IC sound (I2S), a serial bus to interconnect audio devices. The experimental results show that our design offers a robust security solution with an acceptable computational overhead.

  匹配依据：TEE: trusted execution environment, trusted execution environments

  </details>

- **Cache Side-Channel Attacks Through Electromagnetic Emanations of DRAM Accesses**
  2023-12-05 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1864)
  Julien Maillard, Thomas Hiscock, Maxime Lecomte, Christophe Clavier

  <details><summary>摘要 / Abstract</summary>

  Remote side-channel attacks on processors exploit hardware and micro-architectural effects observable from software measurements. So far, the analysis of micro-architectural leakages over physical side-channels (power consumption, electromagnetic field) received little treatment. In this paper, we argue that those attacks are a serious threat, especially against systems such as smartphones and Internet-of-Things (IoT) devices which are physically exposed to the end-user. Namely, we show that the observation of Dynamic Random Access Memory (DRAM) accesses with an electromagnetic (EM) probe constitutes a reliable alternative to time measurements in cache side-channel attacks. We describe the EVICT+EM attack, that allows recovering a full AES key on a T-Tables implementation with similar number of encryptions than state-of-the-art EVICT+RELOAD attacks on the studied ARM platforms. This new attack paradigm removes the need for shared memory and exploits EM radiations instead of high precision timers. Then, we introduce PRIME+EM, which goal is to reverse-engineer cache usage patterns. This attack allows to recover the layout of lookup tables within the cache. Finally, we present COLLISION+EM, a collision-based attack on a System-on-chip (SoC) that does not require malicious code execution, and show its practical efficiency in recovering key material on an ARM TrustZone application. Those results show that physical observation of the micro-architecture can lead to improved attacks.

  匹配依据：TEE: trustzone

  </details>

- **All Rivers Run to the Sea: Private Learning with Asymmetric Flows**
  2023-12-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2312.05264)
  Yue Niu, Ramy E. Ali, Saurav Prakash, Salman Avestimehr

  <details><summary>摘要 / Abstract</summary>

  Data privacy is of great concern in cloud machine-learning service platforms, when sensitive data are exposed to service providers. While private computing environments (e.g., secure enclaves), and cryptographic approaches (e.g., homomorphic encryption) provide strong privacy protection, their computing performance still falls short compared to cloud GPUs. To achieve privacy protection with high computing performance, we propose Delta, a new private training and inference framework, with comparable model performance as non-private centralized training. Delta features two asymmetric data flows: the main information-sensitive flow and the residual flow. The main part flows into a small model while the residuals are offloaded to a large model. Specifically, Delta embeds the information-sensitive representations into a low-dimensional space while pushing the information-insensitive part into high-dimension residuals. To ensure privacy protection, the low-dimensional information-sensitive part is secured and fed to a small model in a private environment. On the other hand, the residual part is sent to fast cloud GPUs, and processed by a large model. To further enhance privacy and reduce the communication cost, Delta applies a random binary quantization technique along with a DP-based technique to the residuals before sharing them with the public platform. We theoretically show that Delta guarantees differential privacy in the public environment and greatly reduces the complexity in the private environment. We conduct empirical analyses on CIFAR-10, CIFAR-100 and ImageNet datasets and ResNet-18 and ResNet-34, showing that Delta achieves strong privacy protection, fast training, and inference without significantly compromising the model utility.

  匹配依据：TEE: secure enclaves

  </details>

- **A Holistic Approach for Trustworthy Distributed Systems with WebAssembly and TEEs**
  2023-12-01 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2312.00702)
  Jämes Ménétrey, Aeneas Grüter, Peterson Yuhala, Julius Oeftiger, Pascal Felber, Marcelo Pasin, Valerio Schiavoni

  <details><summary>摘要 / Abstract</summary>

  Publish/subscribe systems play a key role in enabling communication between numerous devices in distributed and large-scale architectures. While widely adopted, securing such systems often trades portability for additional integrity and attestation guarantees. Trusted Execution Environments (TEEs) offer a potential solution with enclaves to enhance security and trust. However, application development for TEEs is complex, and many existing solutions are tied to specific TEE architectures, limiting adaptability. Current communication protocols also inadequately manage attestation proofs or expose essential attestation information. This paper introduces a novel approach using WebAssembly to address these issues, a key enabling technology nowadays capturing academia and industry attention. We present the design of a portable and fully attested publish/subscribe middleware system as a holistic approach for trustworthy and distributed communication between various systems. Based on this proposal, we have implemented and evaluated in-depth a fully-fledged publish/subscribe broker running within Intel SGX, compiled in WebAssembly, and built on top of industry-battled frameworks and standards, i.e., MQTT and TLS protocols. Our extended TLS protocol preserves the privacy of attestation information, among other benefits. Our experimental results showcase most overheads, revealing a 1.55x decrease in message throughput when using a trusted broker. We open-source the contributions of this work to the research community to facilitate experimental reproducibility.

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **Ontologising Trustworthy in the Telecommunications Domain**
  2023-11-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2311.15839)
  Ian Oliver, Pekka Kuure, Wiktor Sedkowski, Thore Sommer

  <details><summary>摘要 / Abstract</summary>

  Based upon trusted and confidential computing platforms, telecommunications systems must provide guaranteed security for the processes and data running atop them. This in turn requires us to provide trustworthy systems. The term trustworthy is poorly defined with corresponding misunderstanding and misapplication. We present a definition of this term, as well as others, demonstrate its application against certain telecommunications use cases and address how the learnings from ontologising these structures contribute to standardisation and the necessity for FAIR ontologies across telecommunications standards and hosting organisations.

  匹配依据：TEE: confidential computing

  </details>

- **D-GATE: Decentralized Geolocation and Time Enforcement for Usage Control**
  2023-11-21 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2311.12647)
  Hendrik Meyer zum Felde, Jean-Luc Reding, Michael Lux

  <details><summary>摘要 / Abstract</summary>

  In the context of cloud environments, data providers entrust their data to data consumers in order to allow further computing on their own IT infrastructure. Usage control measures allow the data provider to restrict the usage of its data even on the data consumer&#x27;s system. Two of these restrictions can be the geographic location and time limitations. Current solutions that could be used to enforce such constraints can be easily manipulated. These include solutions based on the system time, organizational agreements, GPS-based techniques or simple delay measurements to derive the distance to known reference servers. With D-GATE, we propose a reliable solution that uses trusted execution environments and relies on a decentralized mesh of reference nodes, so-called GeoClients. Here, participants periodically measure the lowest network delay to each other to geolocate themselves. For data providers, it is thus possible to technically attest usage control with time and geolocation constraints without depending on centralized reference systems.

  匹配依据：TEE: trusted execution environments

  </details>

- **A Large-Scale Study on the Prevalence and Usage of TEE-based Features on Android**
  2023-11-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2311.10511)
  Davide Bove

  <details><summary>摘要 / Abstract</summary>

  In the realm of mobile security, where OS-based protections have proven insufficient against robust attackers, Trusted Execution Environments (TEEs) have emerged as a hardware-based security technology. Despite the industry&#x27;s persistence in advancing TEE technology, the impact on end users and developers remains largely unexplored. This study addresses this gap by conducting a large-scale analysis of TEE utilization in Android applications, focusing on the key areas of cryptography, digital rights management, biometric authentication, and secure dialogs. To facilitate our extensive analysis, we introduce Mobsec Analytika, a framework tailored for large-scale app examinations, which we make available to the research community. Through the analysis of 170,550 popular Android apps, our analysis illuminates the implementation of TEE-related features and their contextual usage. Our findings reveal that TEE features are predominantly utilized indirectly through third-party libraries, with only 6.7% of apps directly invoking the APIs. Moreover, the study reveals the underutilization of the recent TEE-based UI feature Protected Confirmation.

  匹配依据：TEE: trusted execution environments

  </details>

- **MirrorNet: A TEE-Friendly Framework for Secure On-device DNN Inference**
  2023-11-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2311.09489)
  Ziyu Liu, Yukui Luo, Shijin Duan, Tong Zhou, Xiaolin Xu

  <details><summary>摘要 / Abstract</summary>

  Deep neural network (DNN) models have become prevalent in edge devices for real-time inference. However, they are vulnerable to model extraction attacks and require protection. Existing defense approaches either fail to fully safeguard model confidentiality or result in significant latency issues. To overcome these challenges, this paper presents MirrorNet, which leverages Trusted Execution Environment (TEE) to enable secure on-device DNN inference. It generates a TEE-friendly implementation for any given DNN model to protect the model confidentiality, while meeting the stringent computation and storage constraints of TEE. The framework consists of two key components: the backbone model (BackboneNet), which is stored in the normal world but achieves lower inference accuracy, and the Companion Partial Monitor (CPM), a lightweight mirrored branch stored in the secure world, preserving model confidentiality. During inference, the CPM monitors the intermediate results from the BackboneNet and rectifies the classification output to achieve higher accuracy. To enhance flexibility, MirrorNet incorporates two modules: the CPM Strategy Generator, which generates various protection strategies, and the Performance Emulator, which estimates the performance of each strategy and selects the most optimal one. Extensive experiments demonstrate the effectiveness of MirrorNet in providing security guarantees while maintaining low computation latency, making MirrorNet a practical and promising solution for secure on-device DNN inference. For the evaluation, MirrorNet can achieve a 18.6% accuracy gap between authenticated and illegal use, while only introducing 0.99% hardware overhead.

  匹配依据：TEE: trusted execution environment

  </details>

- **LightEMU: Hardware Assisted Fuzzing of Trusted Applications**
  2023-11-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2311.09532)
  Haoqi Shan, Sravani Nissankararao, Yujia Liu, Moyao Huang, Shuo Wang, Yier Jin, Dean Sullivan

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) are deployed in many CPU designs because of the confidentiality and integrity guarantees they provide. ARM TrustZone is a TEE extensively deployed on smart phones, IoT devices, and notebooks. Specifically, TrustZone is used to separate code execution and data into two worlds, normal world and secure world. However, this separation inherently prevents traditional fuzzing approaches which rely upon coverage-guided feedback and existing fuzzing research is, therefore, extremely limited. In this paper, we present a native and generic method to perform efficient and scalable feedback-driven fuzzing on Trusted Applications (TAs) using ARM CoreSight. We propose LightEMU, a novel fuzzing framework that allows us to fuzz TAs by decoupling them from relied TEE. We argue that LightEMU is a promising first-stage approach for rapidly discovering TA vulnerabilities prior to investing effort in whole system TEE evaluation precisely because the majority of publicly disclosed TrustZone bugs reside in the TA code itself. We implement LightEMU and adapt it to Teegris, Trusty, OP-TEE and QSEE and evaluate 8 real-world TAs while triggering 3 unique crashes and achieving x10 time speedup when fuzzing TAs using the state-of-the-art TrustZone fuzzing framework.

  匹配依据：TEE: trusted execution environments, trustzone

  </details>

- **ConstMig: Enabling Secure Live Migration of Large Intel SGX-based applications**
  2023-11-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2311.06991)
  Sandeep Kumar, Abhisek Panda, Smruti R. Sarangi

  <details><summary>摘要 / Abstract</summary>

  Cloud service providers are adopting Trusted Execution Environments (TEEs) to provide hardware-guaranteed security to applications running on remote, untrusted data centers. However, migrating such applications still relies on the decade-old stop-and-copy method, which introduces large downtimes. Modern live-migration approaches such as pre-copy and post-copy do not work for TEE-based applications due to hardware-enforced restrictions. We propose ConstMig, a near-zero-downtime live-migration mechanism for large memory-footprint TEE-based applications. ConstMig is fully compatible with containers, virtual machines (VMs), and microVMs. Our prototype, built on Intel SGX, achieves near-zero downtime irrespective of enclave size and requires no additional hardware support. ConstMig reduces total downtime by 77 - 96% for a suite of SGX applications with multi-gigabyte memory footprints compared to state-of-the-art TEE-based migration solutions such as MigSGX.

  匹配依据：TEE: intel sgx, sgx, trusted execution environments

  </details>

- **Triad: Trusted Timestamps in Untrusted Environments**
  2023-11-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2311.06156)
  Gabriel P. Fernandez, Andrey Brito, Christof Fetzer

  <details><summary>摘要 / Abstract</summary>

  We aim to provide trusted time measurement mechanisms to applications and cloud infrastructure deployed in environments that could harbor potential adversaries, including the hardware infrastructure provider. Despite Trusted Execution Environments (TEEs) providing multiple security functionalities, timestamps from the Operating System are not covered. Nevertheless, some services require time for validating permissions or ordering events. To address that need, we introduce Triad, a trusted timestamp dispatcher of time readings. The solution provides trusted timestamps enforced by mutually supportive enclave-based clock servers that create a continuous trusted timeline. We leverage enclave properties such as forced exits and CPU-based counters to mitigate attacks on the server&#x27;s timestamp counters. Triad produces trusted, confidential, monotonically-increasing timestamps with bounded error and desirable, non-trivial properties. Our implementation relies on Intel SGX and SCONE, allowing transparent usage. We evaluate Triad&#x27;s error and behavior in multiple dimensions.

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **A Last-Level Defense for Application Integrity and Confidentiality**
  2023-11-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2311.06154)
  Gabriel P. Fernandez, Andrey Brito, Ardhi Putra Pratama Hartono, Muhammad Usama Sardar, Christof Fetzer

  <details><summary>摘要 / Abstract</summary>

  Our objective is to protect the integrity and confidentiality of applications operating in untrusted environments. Trusted Execution Environments (TEEs) are not a panacea. Hardware TEEs fail to protect applications against Sybil, Fork and Rollback Attacks and, consequently, fail to preserve the consistency and integrity of applications. We introduce a novel system, LLD, that enforces the integrity and consistency of applications in a transparent and scalable fashion. Our solution augments TEEs with instantiation control and rollback protection. Instantiation control, enforced with TEE-supported leases, mitigates Sybil/Fork Attacks without incurring the high costs of solving crypto-puzzles. Our rollback detection mechanism does not need excessive replication, nor does it sacrifice durability. We show that implementing these functionalities in the LLD runtime automatically protects applications and services such as a popular DBMS.

  匹配依据：TEE: trusted execution environments

  </details>

- **DAO Decentralization: Voting-Bloc Entropy, Bribery, and Dark DAOs**
  2023-11-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2311.03530)
  James Austgen, Andrés Fábrega, Sarah Allen, Kushal Babel, Mahimna Kelkar, Ari Juels

  <details><summary>摘要 / Abstract</summary>

  Decentralized Autonomous Organizations (DAOs) use smart contracts to foster communities working toward common goals. Existing definitions of decentralization, however-the &#x27;D&#x27; in DAO-fall short of capturing key properties characteristic of diverse and equitable participation. We propose a new metric called Voting-Bloc Entropy (VBE, pronounced &#x27;&#x27;vibe&#x27;&#x27;) that formalizes a broad notion of decentralization in voting on DAO proposals. VBE measures the similarity of participants&#x27; utility functions across a set of proposals. We use VBE to prove a number of results about the decentralizing effects of vote delegation, proposal bundling, bribery, and quadratic voting. Our results lead to practical suggestions for enhancing DAO decentralization. One of our results highlights the risk of systemic bribery with increasing DAO decentralization. To show that this threat is realistic, we present the first practical realization of a Dark DAO, a proposed mechanism for privacy-preserving corruption of identity systems, including those used in DAO voting. Our Dark-DAO prototype uses trusted execution environments (TEEs) in the Oasis Sapphire blockchain for attacks on Ethereum DAOs. It demonstrates that Dark DAOs constitute a realistic future concern for DAO governance.

  匹配依据：TEE: trusted execution environments

  </details>

- **SinClave: Hardware-assisted Singletons for TEEs**
  2023-11-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2311.02697)
  Franz Gregor, Robert Krahn, Do Le Quoc, Christof Fetzer

  <details><summary>摘要 / Abstract</summary>

  For trusted execution environments (TEEs), remote attestation permits establishing trust in software executed on a remote host. It requires that the measurement of a remote TEE is both complete and fresh: We need to measure all aspects that might determine the behavior of an application, and this measurement has to be reasonably fresh. Performing measurements only at the start of a TEE simplifies the attestation but enables &quot;reuse&quot; attacks of enclaves. We demonstrate how to perform such reuse attacks for different TEE frameworks. We also show how to address this issue by enforcing freshness - through the concept of a singleton enclave - and completeness of the measurements. Completeness of measurements is not trivial since the secrets provisioned to an enclave and the content of the filesystem can both affect the behavior of the software, i.e., can be used to mount reuse attacks. We present mechanisms to include measurements of these two components in the remote attestation. Our evaluation based on real-world applications shows that our approach incurs only negligible overhead ranging from 1.03% to 13.2%.

  匹配依据：TEE: trusted execution environments

  </details>

- **Plug Your Volt: Protecting Intel Processors against Dynamic Voltage Frequency Scaling based Fault Attacks**
  2023-10-30 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1679)
  Nimish Mishra, Rahul Arvind Mool, Anirban Chakraborty, Debdeep Mukhopadhyay

  <details><summary>摘要 / Abstract</summary>

  The need for energy optimizations in modern systems forces CPU vendors to provide Dynamic Voltage Frequency Scaling (DVFS) interfaces that allow software to control the voltage and frequency of CPU cores. In recent years, the accessibility of such DVFS interfaces to adversaries has amounted to a plethora of fault attack vectors. In response, the current countermeasures involve either restricting access to DVFS interfaces or including additional compiler-based checks that let the DVFS fault occur but prevent an adversary from weaponizing it. However, such countermeasures are overly restrictive because (1) they prevent benign, non-SGX processes from utilizing DVFS, and (2) rely upon a less practical threat model than what is acceptable for Intel SGX. In this work, we hence put forth a new countermeasure perspective. We reason that all DVFS fault attacks are helped by system design decisions that allow an adversary to search through the entire space of frequency/voltage pairs which lead to DVFS faults on the victim system. Using this observation, we classify such frequency/voltage pairs causing DVFS faults as unsafe system states. We then develop a kernel module level countermeasure (in non-SGX execution context) that polls core frequency/voltage pairs to detect when the system is in an unsafe state, and force it back into a safe state. Our countermeasure completely prevents DVFS faults on three Intel generation CPUs: Sky Lake, Kaby Lake R, and Comet Lake, while allowing accessibility of DVFS features to benign non-SGX executions (something which prior works fail to achieve). Additionally, we also put forth the notion of maximal safe state, allowing our countermeasure to be implemented both as microcode (on the micro-architecture level) and as model-specific register (on the hardware level), as opposed to prior countermeasures which can not be implemented at the hardware level. Finally, we evaluate the overhead of our kernel module&#x27;s execution on SPEC2017, observing an minuscule overhead of 0.28%.

  匹配依据：TEE: intel sgx, sgx

  </details>

- **RIPencapsulation: Defeating IP Encapsulation on TI MSP Devices**
  2023-10-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2310.16433)
  Prakhar Sah, Matthew Hicks

  <details><summary>摘要 / Abstract</summary>

  Internet of Things (IoT) devices sit at the intersection of unwieldy software complexity and unprecedented attacker access. This unique position comes with a daunting security challenge: how can I protect both proprietary code and confidential data on a device that the attacker has unfettered access to? Trusted Execution Environments (TEEs) promise to solve this challenge through hardware-based separation of trusted and untrusted computation and data. While TEEs do an adequate job of protecting secrets on desktop-class devices, we reveal that trade-offs made in one of the most widely-used commercial IoT devices undermine their TEE&#x27;s security. This paper uncovers two fundamental weaknesses in IP Encapsulation (IPE), the TEE deployed by Texas Instruments for MSP430 and MSP432 devices. We observe that lack of call site enforcement and residual state after unexpected TEE exits enable an attacker to reveal all proprietary code and secret data within the IPE. We design and implement an attack called RIPencapsulation, which systematically executes portions of code within the IPE and uses the partial state revealed through the register file to exfiltrate secret data and to identify gadget instructions. The attack then uses gadget instructions to reveal all proprietary code within the IPE. Our evaluation with commodity devices and a production compiler and settings shows that -- even after following all manufacturer-recommended secure coding practices -- RIPencapsultaion reveals, within minutes, both the code and keys from third-party cryptographic implementations protected by the IPE.

  匹配依据：TEE: trusted execution environments

  </details>

- **SecV: Secure Code Partitioning via Multi-Language Secure Values**
  2023-10-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2310.15582)
  Peterson Yuhala, Pascal Felber, Hugo Guiroux, Jean-Pierre Lozi, Alain Tchana, Valerio Schiavoni, Gaël Thomas

  <details><summary>摘要 / Abstract</summary>

  Trusted execution environments like Intel SGX provide \emph{enclaves}, which offer strong security guarantees for applications. Running entire applications inside enclaves is possible, but this approach leads to a large trusted computing base (TCB). As such, various tools have been developed to partition programs written in languages such as C or Java into \emph{trusted} and \emph{untrusted} parts, which are run in and out of enclaves respectively. However, those tools depend on language-specific taint-analysis and partitioning techniques. They cannot be reused for other languages and there is thus a need for tools that transcend this language barrier. We address this challenge by proposing a multi-language technique to specify sensitive code or data, as well as a multi-language tool to analyse and partition the resulting programs for trusted execution environments like Intel SGX. We leverage GraalVM&#x27;s Truffle framework, which provides a language-agnostic abstract syntax tree (AST) representation for programs, to provide special AST nodes called \emph{secure nodes} that encapsulate sensitive program information. Secure nodes can easily be embedded into the ASTs of a wide range of languages via Truffle&#x27;s \emph{polyglot API}. Our technique includes a multi-language dynamic taint tracking tool to analyse and partition applications based on our generic secure nodes. Our extensive evaluation with micro- and macro-benchmarks shows that we can use our technique for two languages (Javascript and \python), and that partitioned programs can obtain up to $14.5\%$ performance improvement as compared to unpartitioned versions.

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **Multilayer Environment and Toolchain for Holistic NetwOrk Design and Analysis**
  2023-10-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2310.16190)
  Filip Rezabek, Kilian Glas, Richard von Seck, Achraf Aroua, Tizian Leonhardt, Georg Carle

  <details><summary>摘要 / Abstract</summary>

  The recent developments and research in distributed ledger technologies and blockchain have contributed to the increasing adoption of distributed systems. To collect relevant insights into systems&#x27; behavior, we observe many evaluation frameworks focusing mainly on the system under test throughput. However, these frameworks often need more comprehensiveness and generality, particularly in adopting a distributed applications&#x27; cross-layer approach. This work analyses in detail the requirements for distributed systems assessment. We summarize these findings into a structured methodology and experimentation framework called METHODA. Our approach emphasizes setting up and assessing a broader spectrum of distributed systems and addresses a notable research gap. We showcase the effectiveness of the framework by evaluating four distinct systems and their interaction, leveraging a diverse set of eight carefully selected metrics and 12 essential parameters. Through experimentation and analysis we demonstrate the framework&#x27;s capabilities to provide valuable insights across various use cases. For instance, we identify that a combination of Trusted Execution Environments with threshold signature scheme FROST introduces minimal overhead on the performance with average latency around \SI{40}{\ms}. We showcase an emulation of realistic systems behavior, e.g., Maximal Extractable Value is possible and could be used to further model such dynamics. The METHODA framework enables a deeper understanding of distributed systems and is a powerful tool for researchers and practitioners navigating the complex landscape of modern computing infrastructures.

  匹配依据：TEE: trusted execution environments

  </details>

- **Crystalor: Recoverable Memory Encryption Mechanism with Optimized Metadata Structure**
  2023-10-20 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1630)
  Rei Ueno, Hiromichi Haneda, Naofumi Homma, Akiko Inoue, Kazuhiko Minematsu

  <details><summary>摘要 / Abstract</summary>

  This study presents an efficient recoverable memory encryption mechanism, named Crystalor. Existing memory encryption mechanisms, such as Intel SGX integrity tree, offer neither crash consistency nor recoverability, which results in attack surfaces and causes a non-trivial limitation of practical availability. Although the crash consistency of encrypted memory has been studied in the research field of microarchitecture, existing mechanisms lack formal security analysis and cannot incorporate with metadata optimization mechanisms, which are essential to achieve a practical performance. Crystalor efficiently realizes provably-secure recoverable memory encryption with metadata optimization. To establish Crystalor with provable security and practical performance, we develop a dedicated universal hash function PXOR-Hash and a microarchitecture equipped with PXOR-Hash. Crystalor incurs almost no latency overhead under the nominal operations for the recoverability, while it has a simple construction in such a way as to be compatible with existing microarchitectures. We evaluate its practical performance through both algorithmic analyses and system-level simulation in comparison with the state-of-the-art ones, such as SCUE. Crystalor requires 29–62% fewer clock cycles per memory read/write operation than SCUE for protecting a 4 TB memory. In addition, Crystalor and SCUE require 312 GB and 554 GB memory overheads for metadata, respectively, which indicates that Crystalor achieves a memory overhead reduction of 44%. The results of the system-level simulation using the gem5 simulator indicate that Crystalor achieves a reduction of up to 11.5% in the workload execution time compared to SCUE. Moreover, Crystalor achieves a higher availability and memory recovery several thousand times faster than SCUE, as Crystalor offers lazy recovery.

  匹配依据：TEE: intel sgx

  </details>

- **Confidential Consortium Framework: Secure Multiparty Applications with Confidentiality, Integrity, and High Availability**
  2023-10-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2310.11559) · [Code](https://github.com/microsoft/CCF)
  Heidi Howard, Fritz Alder, Edward Ashton, Amaury Chamayou, Sylvan Clebsch, Manuel Costa, Antoine Delignat-Lavaud, Cedric Fournet, Andrew Jeffery, Matthew Kerner, Fotios Kounelis, Markus A. Kuppe, Julien Maffre, Mark Russinovich, Christoph M. Wintersteiger

  <details><summary>摘要 / Abstract</summary>

  Confidentiality, integrity protection, and high availability, abbreviated to CIA, are essential properties for trustworthy data systems. The rise of cloud computing and the growing demand for multiparty applications however means that building modern CIA systems is more challenging than ever. In response, we present the Confidential Consortium Framework (CCF), a general-purpose foundation for developing secure stateful CIA applications. CCF combines centralized compute with decentralized trust, supporting deployment on untrusted cloud infrastructure and transparent governance by mutually untrusted parties. CCF leverages hardware-based trusted execution environments for remotely verifiable confidentiality and code integrity. This is coupled with state machine replication backed by an auditable immutable ledger for data integrity and high availability. CCF enables each service to bring its own application logic, custom multiparty governance model, and deployment scenario, decoupling the operators of nodes from the consortium that governs them. CCF is open-source and available now at https://github.com/microsoft/CCF.

  匹配依据：TEE: trusted execution environments

  </details>

- **TRANSOM: An Efficient Fault-Tolerant System for Training LLMs**
  2023-10-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2310.10046)
  Baodong Wu, Lei Xia, Qingping Li, Kangyu Li, Xu Chen, Yongqiang Guo, Tieyao Xiang, Yuheng Chen, Shigang Li

  <details><summary>摘要 / Abstract</summary>

  Large language models (LLMs) with hundreds of billions or trillions of parameters, represented by chatGPT, have achieved profound impact on various fields. However, training LLMs with super-large-scale parameters requires large high-performance GPU clusters and long training periods lasting for months. Due to the inevitable hardware and software failures in large-scale clusters, maintaining uninterrupted and long-duration training is extremely challenging. As a result, A substantial amount of training time is devoted to task checkpoint saving and loading, task rescheduling and restart, and task manual anomaly checks, which greatly harms the overall training efficiency. To address these issues, we propose TRANSOM, a novel fault-tolerant LLM training system. In this work, we design three key subsystems: the training pipeline automatic fault tolerance and recovery mechanism named Transom Operator and Launcher (TOL), the training task multi-dimensional metric automatic anomaly detection system named Transom Eagle Eye (TEE), and the training checkpoint asynchronous access automatic fault tolerance and recovery technology named Transom Checkpoint Engine (TCE). Here, TOL manages the lifecycle of training tasks, while TEE is responsible for task monitoring and anomaly reporting. TEE detects training anomalies and reports them to TOL, who automatically enters the fault tolerance strategy to eliminate abnormal nodes and restart the training task. And the asynchronous checkpoint saving and loading functionality provided by TCE greatly shorten the fault tolerance overhead. The experimental results indicate that TRANSOM significantly enhances the efficiency of large-scale LLM training on clusters. Specifically, the pre-training time for GPT3-175B has been reduced by 28%, while checkpoint saving and loading performance have improved by a factor of 20.

  匹配依据：TEE: tee (context)

  </details>

- **VBFT: Veloce Byzantine Fault Tolerant Consensus for Blockchains**
  2023-10-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2310.09663)
  Mohammad M. Jalalzai, Chen Feng, Victoria Lemieux

  <details><summary>摘要 / Abstract</summary>

  Low latency is one of the most desirable features of partially synchronous Byzantine consensus protocols. Existing low-latency protocols have achieved consensus with just two communication steps by reducing the maximum number of faults the protocol can tolerate (from $f = \frac{n-1}{3}$ to $f = \frac{n+1}{5}$), \textcolor{black}{by relaxing protocol safety guarantees}, or by using trusted hardware like Trusted Execution Environment. Furthermore, these two-step protocols don&#x27;t support rotating leaders and low-cost view change (leader replacement), which are important features of many blockchain use cases. In this paper, we propose a protocol called VBFT which achieves consensus in just two communication steps without sacrificing desirable features. In particular, VBFT tolerates $f = \frac{n-1}{3}$ faults (which is the best possible), guarantees strong safety for honest leaders, and requires no trusted hardware. Moreover, VBFT supports leader rotation and low-cost view change, thereby improving prior art on multiple axes.

  匹配依据：TEE: trusted execution environment

  </details>

- **DASICS White Paper: Enhancing Memory Protection with Dynamic Compartmentalization**
  2023-10-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2310.06435)
  Yue Jin, Yibin Xu, Chengyuan Yang, Han Wang, Tianyi Huang, Tianyue Lu, Mingyu Chen

  <details><summary>摘要 / Abstract</summary>

  In the existing software development ecosystem, security issues introduced by third-party code cannot be overlooked. Among these security concerns, memory access vulnerabilities stand out prominently, leading to risks such as the theft or tampering of sensitive data. To address this issue, software-based defense mechanisms have been established at the programming language, compiler, and operating system levels. However, as a trade-off, these mechanisms significantly reduce software execution efficiency. Hardware-software co-design approaches have sought to either construct entirely isolated trusted execution environments or attempt to partition security domains within the same address space. While such approaches enhance efficiency compared to pure software methods, they also encounter challenges related to granularity of protection, performance overhead, and portability. In response to these challenges, we present the DASICS (Dynamic in-Address-Space Isolation by Code Segments) secure processor design, which offers dynamic and flexible security protection across multiple privilege levels, addressing data flow protection, control flow protection, and secure system calls. We have implemented hardware FPGA prototypes and software QEMU simulator prototypes based on DASICS, along with necessary modifications to system software for adaptability. We illustrate the protective mechanisms and effectiveness of DASICS with two practical examples and provide potential real-world use cases where DASICS could be applied.

  匹配依据：TEE: trusted execution environments

  </details>

- **A Blockchain-driven Architecture for Usage Control in Solid**
  2023-10-09 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2310.05731)
  Davide Basile, Claudio Di Ciccio, Valerio Goretti, Sabrina Kirrane

  <details><summary>摘要 / Abstract</summary>

  Decentralization initiatives like Solid enable data owners to control who has access to their data and to stimulate innovation by creating both application and data markets. Once data owners share their data with others, though, it is no longer possible for them to control how their data are used. To address this issue, we propose a usage control architecture to monitor compliance with usage control policies. To this end, our solution relies on blockchain and trusted execution environments. We demonstrate the potential of the architecture by describing the various workflows needed to realize a motivating use case scenario for data markets. Additionally, we discuss the merits of the approach from privacy, security, integrateability, and affordability perspectives.

  匹配依据：TEE: trusted execution environments

  </details>

- **Accountable Decryption made Formal and Practical**
  2023-10-05 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1519)
  Rujia Li, Yuanzhao Li, Qin Wang, Sisi Duan, Qi Wang, Mark Ryan

  <details><summary>摘要 / Abstract</summary>

  With the increasing scale and complexity of online activities, accountability, as an after-the-fact mechanism, has become an effective complementary approach to ensure system security. Decades of research have delved into the connotation of accountability. They fail, however, to achieve practical accountability of decryption. This paper seeks to address this gap. We consider the scenario where a client (called encryptor, her) encrypts her data and then chooses a delegate (a.k.a. decryptor, him) that stores data for her. If the decryptor initiates an illegitimate decryption on the encrypted data, there is a non-negligible probability that this behavior will be detected, thereby holding the decryptor accountable for his decryption. We make three contributions. First, we review key definitions of accountability known so far. Based on extensive investigations, we formalize new definitions of accountability specifically targeting the decryption process, denoted as accountable decryption, and discuss the (im)possibilities when capturing this concept. We also define the security goals in correspondence. Secondly, we present a novel Trusted Execution Environment(TEE)-assisted solution aligning with definitions. Instead of fully trusting TEE, we take a further step, making TEE work in the &quot;trust, but verify&quot; model where we trust TEE and use its service, but empower users (i.e., decryptors) to detect the potentially compromised state of TEEs. Thirdly, we implement a full-fledged system and conduct a series of evaluations. The results demonstrate that our solution is efficient. Even in a scenario involving $300,000$ log entries, the decryption process concludes in approximately $5.5$ms, and malicious decryptors can be identified within $69$ms.

  匹配依据：TEE: trusted execution environment

  </details>

- **No Forking Way: Detecting Cloning Attacks on Intel SGX Applications**
  2023-10-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2310.03002)
  Samira Briongos, Ghassan Karame, Claudio Soriente, Annika Wilde

  <details><summary>摘要 / Abstract</summary>

  Forking attacks against TEEs like Intel SGX can be carried out either by rolling back the application to a previous state, or by cloning the application and by partitioning its inputs across the cloned instances. Current solutions to forking attacks require Trusted Third Parties (TTP) that are hard to find in real-world deployments. In the absence of a TTP, many TEE applications rely on monotonic counters to mitigate forking attacks based on rollbacks; however, they have no protection mechanism against forking attack based on cloning. In this paper, we analyze 72 SGX applications and show that approximately 20% of those are vulnerable to forking attacks based on cloning - including those that rely on monotonic counters. To address this problem, we present CloneBuster, the first practical clone-detection mechanism for Intel SGX that does not rely on a TTP and, as such, can be used directly to protect existing applications. CloneBuster allows enclaves to (self-) detect whether another enclave with the same binary is running on the same platform. To do so, CloneBuster relies on a cache-based covert channel for enclaves to signal their presence to (and detect the presence of) clones on the same machine. We show that CloneBuster is robust despite a malicious OS, only incurs a marginal impact on the application performance, and adds approximately 800 LoC to the TCB. When used in conjunction with monotonic counters, CloneBuster allows applications to benefit from a comprehensive protection against forking attacks.

  匹配依据：TEE: intel sgx, sgx

  </details>

- **Runtime Verification for Trustworthy Computing**
  2023-10-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2310.02341)
  Robert Abela, Christian Colombo, Axel Curmi, Mattea Fenech, Mark Vella, Angelo Ferrando

  <details><summary>摘要 / Abstract</summary>

  Autonomous and robotic systems are increasingly being trusted with sensitive activities with potentially serious consequences if that trust is broken. Runtime verification techniques present a natural source of inspiration for monitoring and enforcing the desirable properties of the communication protocols in place, providing a formal basis and ways to limit intrusiveness. A recently proposed approach, RV-TEE, shows how runtime verification can enhance the level of trust to the Rich Execution Environment (REE), consequently adding a further layer of protection around the Trusted Execution Environment (TEE). By reflecting on the implication of deploying RV in the context of trustworthy computing, we propose practical solutions to two threat models for the RV-TEE monitoring process: one where the adversary has gained access to the system without elevated privileges, and another where the adversary gains all privileges to the host system but fails to steal secrets from the TEE.

  匹配依据：TEE: trusted execution environment

  </details>

- **A Distributed Efficient Blockchain Oracle Scheme for Internet of Things**
  2023-09-30 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2310.00254)
  Youquan Xian, Lianghaojie Zhou, Jianyong Jiang, Boyi Wang, Hao Huo, Peng Liu

  <details><summary>摘要 / Abstract</summary>

  In recent years, blockchain has been widely applied in the Internet of Things (IoT). Blockchain oracle, as a bridge for data communication between blockchain and off-chain, has also received significant attention. However, the numerous and heterogeneous devices in the IoT pose great challenges to the efficiency and security of data acquisition for oracles. We find that the matching relationship between data sources and oracle nodes greatly affects the efficiency and service quality of the entire oracle system. To address these issues, this paper proposes a distributed and efficient oracle solution tailored for the IoT, enabling fast acquisition of real-time off-chain data. Specifically, we first design a distributed oracle architecture that combines both Trusted Execution Environment (TEE) devices and ordinary devices to improve system scalability, considering the heterogeneity of IoT devices. Secondly, based on the trusted node information provided by TEE, we determine the matching relationship between nodes and data sources, assigning appropriate nodes for tasks to enhance system efficiency. Through simulation experiments, our proposed solution has been shown to effectively improve the efficiency and service quality of the system, reducing the average response time by approximately 9.92\% compared to conventional approaches.

  匹配依据：TEE: trusted execution environment

  </details>

- **SyzTrust: State-aware Fuzzing on Trusted OS Designed for IoT Devices**
  2023-09-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.14742)
  Qinying Wang, Boyu Chang, Shouling Ji, Yuan Tian, Xuhong Zhang, Binbin Zhao, Gaoning Pan, Chenyang Lyu, Mathias Payer, Wenhai Wang, Raheem Beyah

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) embedded in IoT devices provide a deployable solution to secure IoT applications at the hardware level. By design, in TEEs, the Trusted Operating System (Trusted OS) is the primary component. It enables the TEE to use security-based design techniques, such as data encryption and identity authentication. Once a Trusted OS has been exploited, the TEE can no longer ensure security. However, Trusted OSes for IoT devices have received little security analysis, which is challenging from several perspectives: (1) Trusted OSes are closed-source and have an unfavorable environment for sending test cases and collecting feedback. (2) Trusted OSes have complex data structures and require a stateful workflow, which limits existing vulnerability detection tools. To address the challenges, we present SyzTrust, the first state-aware fuzzing framework for vetting the security of resource-limited Trusted OSes. SyzTrust adopts a hardware-assisted framework to enable fuzzing Trusted OSes directly on IoT devices as well as tracking state and code coverage non-invasively. SyzTrust utilizes composite feedback to guide the fuzzer to effectively explore more states as well as to increase the code coverage. We evaluate SyzTrust on Trusted OSes from three major vendors: Samsung, Tsinglink Cloud, and Ali Cloud. These systems run on Cortex M23/33 MCUs, which provide the necessary abstraction for embedded TEEs. We discovered 70 previously unknown vulnerabilities in their Trusted OSes, receiving 10 new CVEs so far. Furthermore, compared to the baseline, SyzTrust has demonstrated significant improvements, including 66% higher code coverage, 651% higher state coverage, and 31% improved vulnerability-finding capability. We report all discovered new vulnerabilities to vendors and open source SyzTrust.

  匹配依据：TEE: trusted execution environments

  </details>

- **Private Web Search with Tiptoe**
  2023-09-21 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1438)
  Alexandra Henzinger, Emma Dauterman, Henry Corrigan-Gibbs, Nickolai Zeldovich

  <details><summary>摘要 / Abstract</summary>

  Tiptoe is a private web search engine that allows clients to search over hundreds of millions of documents, while revealing no information about their search query to the search engine’s servers. Tiptoe’s privacy guarantee is based on cryptography alone; it does not require hardware enclaves or non-colluding servers. Tiptoe uses semantic embeddings to reduce the problem of private full-text search to private nearest-neighbor search. Then, Tiptoe implements private nearest-neighbor search with a new, high-throughput protocol based on linearly homomorphic encryption. Running on a 45-server cluster, Tiptoe can privately search over 360 million web pages with 145 core-seconds of server compute, 56.9 MiB of client-server communication (74% of which occurs before the client enters its search query), and 2.7 seconds of end-to-end latency. Tiptoe’s search works best on conceptual queries (“knee pain”) and less well on exact string matches (“123 Main Street, New York”). On the MS MARCO search-quality benchmark, Tiptoe ranks the best-matching result in position 7.7 on average. This is worse than a state-of-the-art, non-private neural search algorithm (average rank: 2.3), but is close to the classical tf-idf algorithm (average rank: 6.7). Finally, Tiptoe is extensible: it also supports private text-to-image search and, with minor modifications, it can search over audio, code, and more.

  匹配依据：TEE: hardware enclaves

  </details>

- **PRIVATON - Privacy Preserving Automaton for Proof of Computations**
  2023-09-20 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1424)
  Bala Subramanyan

  <details><summary>摘要 / Abstract</summary>

  Amid the landscape of confidential computing, where security and privacy reign supreme, PRIVATON emerges as a pioneering and practical solution to safeguard sensitive data and computations. A verifiable proof of computation model, with one of its variant built upon the dual sandbox strategy, PRIVATON combines Trusted Execution Environment (TEE) technologies with WebAssembly (WASM) runtime environments to establish an ecosystem for privacy-preserving computations. This approach involves fine grained modeling of computations as finite state automatons, guided by verifiable proofs that attest to their unerring execution. PRIVATON is guided by the profound principles of &quot;least privilege&quot; and &quot;intentional use.&quot; Through the former, each computation module&#x27;s privileges are meticulously constrained, reducing vulnerability vectors. The latter ensures that privileges are allocated explicitly, fostering comprehension and security. This rigorous adherence minimizes privilege misuse and information leakage, bolstering the overall security posture. At its core, PRIVATON&#x27;s innovation lies in its comprehensive assurance of data privacy and security. State machine proofs not only attest to the absence of data leakage but also prevent unauthorized data transmission. By providing unassailable proof of computation integrity, PRIVATON shields against code misuse within the system. This proactive stance fortifies its mission to safeguard the sanctity of data, computations, and the privacy of all stakeholders. Evidenced by its real-world application, PRIVATON has been validated within the cryptocurrency trading ecosystem, where it acts as a distributed and privacy-preserving credit oracle. Its implementation within Credora’s landscape underlines its potential to transform data-centric paradigms, empowering stakeholders with an unshakeable confidence in data security. In a world where data privacy is paramount, PRIVATON stands as a guardian, epitomizing the convergence of technology, security, and trust.

  匹配依据：TEE: confidential computing, trusted execution environment

  </details>

- **Mitigating Adversarial Attacks in Federated Learning with Trusted Execution Environments**
  2023-09-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.07197) · [Code](https://github.com/queyrusi/Pelta)
  Simon Queyrut, Valerio Schiavoni, Pascal Felber

  <details><summary>摘要 / Abstract</summary>

  The main premise of federated learning (FL) is that machine learning model updates are computed locally to preserve user data privacy. This approach avoids by design user data to ever leave the perimeter of their device. Once the updates aggregated, the model is broadcast to all nodes in the federation. However, without proper defenses, compromised nodes can probe the model inside their local memory in search for adversarial examples, which can lead to dangerous real-world scenarios. For instance, in image-based applications, adversarial examples consist of images slightly perturbed to the human eye getting misclassified by the local model. These adversarial images are then later presented to a victim node&#x27;s counterpart model to replay the attack. Typical examples harness dissemination strategies such as altered traffic signs (patch attacks) no longer recognized by autonomous vehicles or seemingly unaltered samples that poison the local dataset of the FL scheme to undermine its robustness. Pelta is a novel shielding mechanism leveraging Trusted Execution Environments (TEEs) that reduce the ability of attackers to craft adversarial samples. Pelta masks inside the TEE the first part of the back-propagation chain rule, typically exploited by attackers to craft the malicious samples. We evaluate Pelta on state-of-the-art accurate models using three well-established datasets: CIFAR-10, CIFAR-100 and ImageNet. We show the effectiveness of Pelta in mitigating six white-box state-of-the-art adversarial attacks, such as Projected Gradient Descent, Momentum Iterative Method, Auto Projected Gradient Descent, the Carlini &amp; Wagner attack. In particular, Pelta constitutes the first attempt at defending an ensemble model against the Self-Attention Gradient attack to the best of our knowledge. Our code is available to the research community at https://github.com/queyrusi/Pelta.

  匹配依据：TEE: trusted execution environments

  </details>

- **Caveat (IoT) Emptor: Towards Transparency of IoT Device Presence (Full Version)**
  2023-09-07 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.03574)
  Sashidhar Jakkamsetti, Youngil Kim, Gene Tsudik

  <details><summary>摘要 / Abstract</summary>

  As many types of IoT devices worm their way into numerous settings and many aspects of our daily lives, awareness of their presence and functionality becomes a source of major concern. Hidden IoT devices can snoop (via sensing) on nearby unsuspecting users, and impact the environment where unaware users are present, via actuation. This prompts, respectively, privacy and security/safety issues. The dangers of hidden IoT devices have been recognized and prior research suggested some means of mitigation, mostly based on traffic analysis or using specialized hardware to uncover devices. While such approaches are partially effective, there is currently no comprehensive approach to IoT device transparency. Prompted in part by recent privacy regulations (GDPR and CCPA), this paper motivates and constructs a privacy-agile Root-of-Trust architecture for IoT devices, called PAISA: Privacy-Agile IoT Sensing and Actuation. It guarantees timely and secure announcements about IoT devices&#x27; presence and their capabilities. PAISA has two components: one on the IoT device that guarantees periodic announcements of its presence even if all device software is compromised, and the other that runs on the user device, which captures and processes announcements. Notably, PAISA requires no hardware modifications; it uses a popular off-the-shelf Trusted Execution Environment (TEE) -- ARM TrustZone. This work also comprises a fully functional (open-sourced) prototype implementation of PAISA, which includes: an IoT device that makes announcements via IEEE 802.11 WiFi beacons and an Android smartphone-based app that captures and processes announcements. Both security and performance of PAISA design and prototype are discussed.

  匹配依据：TEE: trusted execution environment, trustzone

  </details>

- **Security Verification of Low-Trust Architectures**
  2023-09-01 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2309.00181)
  Qinhan Tan, Yonathan Fisseha, Shibo Chen, Lauren Biernacki, Jean-Baptiste Jeannin, Sharad Malik, Todd Austin

  <details><summary>摘要 / Abstract</summary>

  Low-trust architectures work on, from the viewpoint of software, always-encrypted data, and significantly reduce the amount of hardware trust to a small software-free enclave component. In this paper, we perform a complete formal verification of a specific low-trust architecture, the Sequestered Encryption (SE) architecture, to show that the design is secure against direct data disclosures and digital side channels for all possible programs. We first define the security requirements of the ISA of SE low-trust architecture. Looking upwards, this ISA serves as an abstraction of the hardware for the software, and is used to show how any program comprising these instructions cannot leak information, including through digital side channels. Looking downwards this ISA is a specification for the hardware, and is used to define the proof obligations for any RTL implementation arising from the ISA-level security requirements. These cover both functional and digital side-channel leakage. Next, we show how these proof obligations can be successfully discharged using commercial formal verification tools. We demonstrate the efficacy of our RTL security verification technique for seven different correct and buggy implementations of the SE architecture.

  匹配依据：TEE: enclave (context)

  </details>

- **Towards a Formally Verified Security Monitor for VM-based Confidential Computing**
  2023-08-20 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.10249)
  Wojciech Ozga, Guerney D. H. Hunt, Michael V. Le, Elaine R. Palmer, Avraham Shinnar

  <details><summary>摘要 / Abstract</summary>

  Confidential computing is a key technology for isolating high-assurance applications from the large amounts of untrusted code typical in modern systems. Existing confidential computing systems cannot be certified for use in critical applications, like systems controlling critical infrastructure, hardware security modules, or aircraft, as they lack formal verification. This paper presents an approach to formally modeling and proving a security monitor. It introduces a canonical architecture for virtual machine (VM)-based confidential computing systems. It abstracts processor-specific components and identifies a minimal set of hardware primitives required by a trusted security monitor to enforce security guarantees. We demonstrate our methodology and proposed approach with an example from our Rust implementation of the security monitor for RISC-V.

  匹配依据：TEE: confidential computing

  </details>

- **Flexway O-Sort: Enclave-Friendly and Optimal Oblivious Sorting**
  2023-08-20 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1258)
  Tianyao Gu, Yilei Wang, Afonso Tinoco, Bingnan Chen, Ke Yi, Elaine Shi

  <details><summary>摘要 / Abstract</summary>

  Oblivious algorithms are being deployed at large scale in real world to enable privacy-preserving applications such as Signal&#x27;s private contact discovery. Oblivious sorting is a fundamental building block in the design of oblivious algorithms for numerous computation tasks. Unfortunately, there is still a theory-practice gap for oblivious sort. The commonly implemented bitonic sorting algorithm is not asymptotically optimal, whereas known asymptotically optimal algorithms suffer from large constants. In this paper, we construct a new oblivious sorting algorithm called flexway o-sort, which is asymptotically optimal, concretely efficient, and suitable for implementation in hardware enclaves such as Intel SGX. For moderately large inputs of $12$ GB, our flexway o-sort algorithm outperforms known oblivious sorting algorithms by $1.32\times$ to $28.8\times$ when the data fits within the hardware enclave, and by $4.1\times$ to $208\times$ when the data does not fit within the hardware enclave. We also implemented various applications of oblivious sorting, including histogram, database join, and initialization of an ORAM data structure. For these applications and data sets from 8GB to 32GB, we achieve $1.44 \sim 2.3\times$ speedup over bitonic sort when the data fits within the enclave, and $4.9 \sim 5.5\times$ speedup when the data does not fit within the enclave.

  匹配依据：TEE: hardware enclave, hardware enclaves, intel sgx

  </details>

- **Waks-On/Waks-Off: Fast Oblivious Offline/Online Shuffling and Sorting with Waksman Networks**
  2023-08-15 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1236)
  Sajin Sasy, Aaron Johnson, Ian Goldberg

  <details><summary>摘要 / Abstract</summary>

  As more privacy-preserving solutions leverage trusted execution environments (TEEs) like Intel SGX, it becomes pertinent that these solutions can by design thwart TEE side-channel attacks that research has brought to light. In particular, such solutions need to be fully oblivious to circumvent leaking private information through memory or timing side channels. In this work, we present fast fully oblivious algorithms for shuffling and sorting data. Oblivious shuffling and sorting are two fundamental primitives that are frequently used for permuting data in privacy-preserving solutions. We present novel oblivious shuffling and sorting algorithms in the offline/online model such that the bulk of the computation can be done in an offline phase that is independent of the data to be permuted. The resulting online phase provides performance improvements over state-of-the-art oblivious shuffling and sorting algorithms both asymptotically ($O(\beta n\log n)$ vs. $O(\beta n \log^2n)$) and concretely ($&gt;5\times$ and $&gt;3\times$ speedups), when permuting $n$ items each of size $\beta$. Our work revisits Waksman networks, and it uses the key observation that setting the control bits of a Waksman network for a uniformly random shuffle is independent of the data to be shuffled. However, setting the control bits of a Waksman network efficiently and fully obliviously poses a challenge, and we provide a novel algorithm to this end. The total costs (inclusive of offline computation) of our WaksShuffle shuffling algorithm and our WaksSort sorting algorithm are lower than all other fully oblivious shuffling and sorting algorithms when the items are at least moderately sized (i.e., $\beta$ &gt; 1400 B), and the performance gap only widens as the item sizes increase. Furthermore, WaksShuffle improves the online cost of oblivious shuffling by $&gt;5\times$ for shuffling $2^{20}$ items of any size; similarly WaksShuffle+QS, our other sorting algorithm, provides $&gt;2.7\times$ speedups in the online cost of oblivious sorting.

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **SoK: Privacy-Preserving Smart Contract**
  2023-08-13 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1226)
  Huayi Qi, Minghui Xu, Dongxiao Yu, Xiuzhen Cheng

  <details><summary>摘要 / Abstract</summary>

  The privacy concern in smart contract applications continues to grow, leading to the proposal of various schemes aimed at developing comprehensive and universally applicable privacy-preserving smart contract (PPSC) schemes. However, the existing research in this area is fragmented and lacks a comprehensive system overview. This paper aims to bridge the existing research gap on PPSC schemes by systematizing previous studies in this field. The primary focus is on two categories: PPSC schemes based on cryptographic tools like zero-knowledge proofs, as well as schemes based on trusted execution environments. In doing so, we aim to provide a condensed summary of the different approaches taken in constructing PPSC schemes. Additionally, we also offer a comparative analysis of these approaches, highlighting the similarities and differences between them. Furthermore, we shed light on the challenges that developers face when designing and implementing PPSC schemes. Finally, we delve into potential future directions for improving and advancing these schemes, discussing possible avenues for further research and development.

  匹配依据：TEE: trusted execution environments

  </details>

- **SGX-MR-Prot: Efficient and Developer-Friendly Access-Pattern Protection in Trusted Execution Environments**
  2023-08-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.06445)
  AKM Mubashwir Alam, Justin Boyce, Keke Chen

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments, such as Intel SGX, use hardware supports to ensure the confidentiality and integrity of applications against a compromised cloud system. However, side channels like access patterns remain for adversaries to exploit and obtain sensitive information. Common approaches use oblivious programs or primitives, such as ORAM, to make access patterns oblivious to input data, which are challenging to develop. This demonstration shows a prototype SGX-MR-Prot for efficiently protecting access patterns of SGX-based data-intensive applications and minimizing developers&#x27; efforts. SGX-MR-Prot uses the MapReduce framework to regulate application dataflows to reduce the cost of access-pattern protection and hide the data oblivious details from SGX developers. This demonstration will allow users to intuitively understand the unique contributions of the framework-based protection approach via interactive exploration and visualization.

  匹配依据：TEE: intel sgx, sgx, trusted execution environments

  </details>

- **Making Your Program Oblivious: a Comparative Study for Side-channel-safe Confidential Computing**
  2023-08-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.06442)
  AKM Mubashwir Alam, Keke Chen

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) are gradually adopted by major cloud providers, offering a practical option of \emph{confidential computing} for users who don&#x27;t fully trust public clouds. TEEs use CPU-enabled hardware features to eliminate direct breaches from compromised operating systems or hypervisors. However, recent studies have shown that side-channel attacks are still effective on TEEs. An appealing solution is to convert applications to be \emph{data oblivious} to deter many side-channel attacks. While a few research prototypes on TEEs have adopted specific data oblivious operations, the general conversion approaches have never been thoroughly compared against and tested on benchmark TEE applications. These limitations make it difficult for researchers and practitioners to choose and adopt a suitable data oblivious approach for their applications. To address these issues, we conduct a comprehensive analysis of several representative conversion approaches and implement benchmark TEE applications with them. We also perform an extensive empirical study to provide insights into their performance and ease of use.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **Pelta: Shielding Transformers to Mitigate Evasion Attacks in Federated Learning**
  2023-08-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.04373)
  Simon Queyrut, Yérom-David Bromberg, Valerio Schiavoni

  <details><summary>摘要 / Abstract</summary>

  The main premise of federated learning is that machine learning model updates are computed locally, in particular to preserve user data privacy, as those never leave the perimeter of their device. This mechanism supposes the general model, once aggregated, to be broadcast to collaborating and non malicious nodes. However, without proper defenses, compromised clients can easily probe the model inside their local memory in search of adversarial examples. For instance, considering image-based applications, adversarial examples consist of imperceptibly perturbed images (to the human eye) misclassified by the local model, which can be later presented to a victim node&#x27;s counterpart model to replicate the attack. To mitigate such malicious probing, we introduce Pelta, a novel shielding mechanism leveraging trusted hardware. By harnessing the capabilities of Trusted Execution Environments (TEEs), Pelta masks part of the back-propagation chain rule, otherwise typically exploited by attackers for the design of malicious samples. We evaluate Pelta on a state of the art ensemble model and demonstrate its effectiveness against the Self Attention Gradient adversarial Attack.

  匹配依据：TEE: trusted execution environments

  </details>

- **Hardware Architecture for a Quantum Computer Trusted Execution Environment**
  2023-08-07 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.03897)
  Theodoros Trochatos, Chuanqi Xu, Sanjay Deshpande, Yao Lu, Yongshan Ding, Jakub Szefer

  <details><summary>摘要 / Abstract</summary>

  The cloud-based environments in which today&#x27;s and future quantum computers will operate, raise concerns about the security and privacy of user&#x27;s intellectual property. Quantum circuits submitted to cloud-based quantum computer providers represent sensitive or proprietary algorithms developed by users that need protection. Further, input data is hard-coded into the circuits, and leakage of the circuits can expose users&#x27; data. To help protect users&#x27; circuits and data from possibly malicious quantum computer cloud providers, this work presented the first hardware architecture for a trusted execution environment for quantum computers. To protect the user&#x27;s circuits and data, the quantum computer control pulses are obfuscated with decoy control pulses. While digital data can be encrypted, analog control pulses cannot and this paper proposed the novel decoy pulse approach to obfuscate the analog control pulses. The proposed decoy pulses can easily be added to the software by users. Meanwhile, the hardware components of the architecture proposed in this paper take care of eliminating, i.e. attenuating, the decoy pulses inside the superconducting quantum computer&#x27;s dilution refrigerator before they reach the qubits. The hardware architecture also contains tamper-resistant features to protect the trusted hardware and users&#x27; information. The work leverages a new metric of variational distance to analyze the impact and scalability of hardware protection. The variational distance of the circuits protected with our scheme, compared to unprotected circuits, is in the range of only $0.16$ to $0.26$. This work demonstrates that protection from possibly malicious cloud providers is feasible and all the hardware components needed for the proposed architecture are available today.

  匹配依据：TEE: trusted execution environment

  </details>

- **FLIPS: Federated Learning using Intelligent Participant Selection**
  2023-08-07 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.03901)
  Rahul Atul Bhope, K. R. Jayaram, Nalini Venkatasubramanian, Ashish Verma, Gegi Thomas

  <details><summary>摘要 / Abstract</summary>

  This paper presents the design and implementation of FLIPS, a middleware system to manage data and participant heterogeneity in federated learning (FL) training workloads. In particular, we examine the benefits of label distribution clustering on participant selection in federated learning. FLIPS clusters parties involved in an FL training job based on the label distribution of their data apriori, and during FL training, ensures that each cluster is equitably represented in the participants selected. FLIPS can support the most common FL algorithms, including FedAvg, FedProx, FedDyn, FedOpt and FedYogi. To manage platform heterogeneity and dynamic resource availability, FLIPS incorporates a straggler management mechanism to handle changing capacities in distributed, smart community applications. Privacy of label distributions, clustering and participant selection is ensured through a trusted execution environment (TEE). Our comprehensive empirical evaluation compares FLIPS with random participant selection, as well as three other &quot;smart&quot; selection mechanisms - Oort, TiFL and gradient clustering using two real-world datasets, two benchmark datasets, two different non-IID distributions and three common FL algorithms (FedYogi, FedProx and FedAvg). We demonstrate that FLIPS significantly improves convergence, achieving higher accuracy by 17 - 20 % with 20 - 60 % lower communication costs, and these benefits endure in the presence of straggler participants.

  匹配依据：TEE: trusted execution environment

  </details>

- **Integrating Homomorphic Encryption and Trusted Execution Technology for Autonomous and Confidential Model Refining in Cloud**
  2023-08-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.00963)
  Pinglan Liu, Wensheng Zhang

  <details><summary>摘要 / Abstract</summary>

  With the popularity of cloud computing and machine learning, it has been a trend to outsource machine learning processes (including model training and model-based inference) to cloud. By the outsourcing, other than utilizing the extensive and scalable resource offered by the cloud service provider, it will also be attractive to users if the cloud servers can manage the machine learning processes autonomously on behalf of the users. Such a feature will be especially salient when the machine learning is expected to be a long-term continuous process and the users are not always available to participate. Due to security and privacy concerns, it is also desired that the autonomous learning preserves the confidentiality of users&#x27; data and models involved. Hence, in this paper, we aim to design a scheme that enables autonomous and confidential model refining in cloud. Homomorphic encryption and trusted execution environment technology can protect confidentiality for autonomous computation, but each of them has their limitations respectively and they are complementary to each other. Therefore, we further propose to integrate these two techniques in the design of the model refining scheme. Through implementation and experiments, we evaluate the feasibility of our proposed scheme. The results indicate that, with our proposed scheme the cloud server can autonomously refine an encrypted model with newly provided encrypted training data to continuously improve its accuracy. Though the efficiency is still significantly lower than the baseline scheme that refines plaintext-model with plaintext-data, we expect that it can be improved by fully utilizing the higher level of parallelism and the computational power of GPU at the cloud server.

  匹配依据：TEE: trusted execution environment

  </details>

- **Decentralized Translator of Trust: Supporting Heterogeneous TEE for Critical Infrastructure Protection**
  2023-08-02 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.01474)
  Rabimba Karanjai, Rowan Collier, Zhimin Gao, Lin Chen, Xinxin Fan, Taeweon Suh, Weidong Shi, Lei Xu

  <details><summary>摘要 / Abstract</summary>

  Trusted execution environment (TEE) technology has found many applications in mitigating various security risks in an efficient manner, which is attractive for critical infrastructure protection. First, the natural of critical infrastructure requires it to be well protected from various cyber attacks. Second, performance is usually important for critical infrastructure and it cannot afford an expensive protection mechanism. While a large number of TEE-based critical infrastructure protection systems have been proposed to address various security challenges (e.g., secure sensing and reliable control), most existing works ignore one important feature, i.e., devices comprised the critical infrastructure may be equipped with multiple incompatible TEE technologies and belongs to different owners. This feature makes it hard for these devices to establish mutual trust and form a unified TEE environment. To address these challenges and fully unleash the potential of TEE technology for critical infrastructure protection, we propose DHTee, a decentralized coordination mechanism. DHTee uses blockchain technology to support key TEE functions in a heterogeneous TEE environment, especially the attestation service. A Device equipped with one TEE can interact securely with the blockchain to verify whether another potential collaborating device claiming to have a different TEE meets the security requirements. DHTee is also flexible and can support new TEE schemes without affecting devices using existing TEEs that have been supported by the system.

  匹配依据：TEE: trusted execution environment

  </details>

- **FLAIRS: FPGA-Accelerated Inference-Resistant &amp; Secure Federated Learning**
  2023-08-01 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2308.00553)
  Huimin Li, Phillip Rieger, Shaza Zeitouni, Stjepan Picek, Ahmad-Reza Sadeghi

  <details><summary>摘要 / Abstract</summary>

  Federated Learning (FL) has become very popular since it enables clients to train a joint model collaboratively without sharing their private data. However, FL has been shown to be susceptible to backdoor and inference attacks. While in the former, the adversary injects manipulated updates into the aggregation process; the latter leverages clients&#x27; local models to deduce their private data. Contemporary solutions to address the security concerns of FL are either impractical for real-world deployment due to high-performance overheads or are tailored towards addressing specific threats, for instance, privacy-preserving aggregation or backdoor defenses. Given these limitations, our research delves into the advantages of harnessing the FPGA-based computing paradigm to overcome performance bottlenecks of software-only solutions while mitigating backdoor and inference attacks. We utilize FPGA-based enclaves to address inference attacks during the aggregation process of FL. We adopt an advanced backdoor-aware aggregation algorithm on the FPGA to counter backdoor attacks. We implemented and evaluated our method on Xilinx VMK-180, yielding a significant speed-up of around 300 times on the IoT-Traffic dataset and more than 506 times on the CIFAR-10 dataset.

  匹配依据：TEE: enclaves (context)

  </details>

- **Confidential Computing across Edge-to-Cloud for Machine Learning: A Survey Study**
  2023-07-31 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2307.16447)
  SM Zobaed, Mohsen Amini Salehi

  <details><summary>摘要 / Abstract</summary>

  Confidential computing has gained prominence due to the escalating volume of data-driven applications (e.g., machine learning and big data) and the acute desire for secure processing of sensitive data, particularly, across distributed environments, such as edge-to-cloud continuum. Provided that the works accomplished in this emerging area are scattered across various research fields, this paper aims at surveying the fundamental concepts, and cutting-edge software and hardware solutions developed for confidential computing using trusted execution environments, homomorphic encryption, and secure enclaves. We underscore the significance of building trust in both hardware and software levels and delve into their applications particularly for machine learning (ML) applications. While substantial progress has been made, there are some barely-explored areas that need extra attention from the researchers and practitioners in the community to improve confidentiality aspects, develop more robust attestation mechanisms, and to address vulnerabilities of the existing trusted execution environments. Providing a comprehensive taxonomy of the confidential computing landscape, this survey enables researchers to advance this field to ultimately ensure the secure processing of users&#x27; sensitive data across a multitude of applications and computing tiers.

  匹配依据：TEE: confidential computing, secure enclaves, trusted execution environments

  </details>

- **HasTEE: Programming Trusted Execution Environments with Haskell**
  2023-07-24 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2307.13172)
  Abhiroop Sarkar, Robert Krook, Alejandro Russo, Koen Claessen

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) are hardware-enforced memory isolation units, emerging as a pivotal security solution for security-critical applications. TEEs, like Intel SGX and ARM TrustZone, allow the isolation of confidential code and data within an untrusted host environment, such as the cloud and IoT. Despite strong security guarantees, TEE adoption has been hindered by an awkward programming model. This model requires manual application partitioning and the use of error-prone, memory-unsafe, and potentially information-leaking low-level C/C++ libraries. We address the above with \textit{HasTEE}, a domain-specific language (DSL) embedded in Haskell for programming TEE applications. HasTEE includes a port of the GHC runtime for the Intel-SGX TEE. HasTEE uses Haskell&#x27;s type system to automatically partition an application and to enforce \textit{Information Flow Control} on confidential data. The DSL, being embedded in Haskell, allows for the usage of higher-order functions, monads, and a restricted set of I/O operations to write any standard Haskell application. Contrary to previous work, HasTEE is lightweight, simple, and is provided as a \emph{simple security library}; thus avoiding any GHC modifications. We show the applicability of HasTEE by implementing case studies on federated learning, an encrypted password wallet, and a differentially-private data clean room.

  匹配依据：TEE: intel sgx, trusted execution environments, trustzone

  </details>

- **Towards Runtime Customizable Trusted Execution Environment on FPGA-SoC**
  2023-07-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2307.04375)
  Yanling Wang, Xiaolin Chang, Haoran Zhu, Jianhua Wang, Yanwei Gong, Lin Li

  <details><summary>摘要 / Abstract</summary>

  Processing sensitive data and deploying well-designed Intellectual Property (IP) cores on remote Field Programmable Gate Array (FPGA) are prone to private data leakage and IP theft. One effective solution is constructing Trusted Execution Environment (TEE) on FPGA-SoCs (FPGA System on Chips). Researchers have integrated this type TEE with Trusted Platform Module (TPM)-based trusted boot, denoted as FPGA-SoC tbTEE. But there is no effort on secure and trusted runtime customization of FPGA-SoC TEE. This paper extends FPGA-SoC tbTEE to build Runtime Customizable TEE (RCTEE) on FPGA-SoC by additive three major components (our work): 1) CrloadIP, which can load an IP core at runtime such that RCTEE can be adjusted dynamically and securely; 2) CexecIP, which can not only execute an IP core without modifying the operating system of FPGA-SoC TEE, but also prevent insider attacks from executing IPs deployed in RCTEE; 3) CremoAT, which can provide the newly measured RCTEE state and establish a secure and trusted communication path between remote verifiers and RCTEE. We conduct a security analysis of RCTEE and its performance evaluation on Xilinx Zynq UltraScale+ XCZU15EG 2FFVB1156 MPSoC.

  匹配依据：TEE: trusted execution environment

  </details>

- **Accelerating Secure and Verifiable Data Deletion in Cloud Storage via SGX and Blockchain**
  2023-07-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2307.04316)
  Xiangman Li, Jianbing Ni

  <details><summary>摘要 / Abstract</summary>

  Secure data deletion enables data owners to fully control the erasure of their data stored on local or cloud data centers and is essential for preventing data leakage, especially for cloud storage. However, traditional data deletion based on unlinking, overwriting, and cryptographic key management either ineffectiveness in cloud storage or rely on unpractical assumption. In this paper, we present SevDel, a secure and verifiable data deletion scheme, which leverages the zero-knowledge proof to achieve the verification of the encryption of the outsourced data without retrieving the ciphertexts, while the deletion of the encryption keys are guaranteed based on Intel SGX. SevDel implements secure interfaces to perform data encryption and decryption for secure cloud storage. It also utilizes smart contract to enforce the operations of the cloud service provider to follow service level agreements with data owners and the penalty over the service provider, who discloses the cloud data on its servers. Evaluation on real-world workload demonstrates that SevDel achieves efficient data deletion verification and maintain high bandwidth savings.

  匹配依据：TEE: intel sgx, sgx

  </details>

- **SoK: Privacy-Preserving Signatures**
  2023-07-04 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/1039)
  Alishah Chator, Matthew Green, Pratyush Ranjan Tiwari

  <details><summary>摘要 / Abstract</summary>

  Modern security systems depend fundamentally on the ability of users to authenticate their communications to other parties in a network. Unfortunately, cryptographic authentication can substantially undermine the privacy of users. One possible solution to this problem is to use privacy-preserving cryptographic authentication. These protocols allow users to authenticate their communications without revealing their identity to the verifier. In the non-interactive setting, the most common protocols include blind, ring, and group signatures, each of which has been the subject of enormous research in the security and cryptography literature. These primitives are now being deployed at scale in major applications, including Intel&#x27;s SGX software attestation framework. The depth of the research literature and the prospect of large-scale deployment motivate us to systematize our understanding of the research in this area. This work provides an overview of these techniques, focusing on applications and efficiency.

  匹配依据：TEE: sgx

  </details>

- **SoK: A Systematic Review of TEE Usage for Developing Trusted Applications**
  2023-06-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.15025)
  Arttu Paju, Muhammad Owais Javed, Juha Nurmi, Juha Savimäki, Brian McGillion, Billy Bob Brumley

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) are a feature of modern central processing units (CPUs) that aim to provide a high assurance, isolated environment in which to run workloads that demand both confidentiality and integrity. Hardware and software components in the CPU isolate workloads, commonly referred to as Trusted Applications (TAs), from the main operating system (OS). This article aims to analyse the TEE ecosystem, determine its usability, and suggest improvements where necessary to make adoption easier. To better understand TEE usage, we gathered academic and practical examples from a total of 223 references. We summarise the literature and provide a publication timeline, along with insights into the evolution of TEE research and deployment. We categorise TAs into major groups and analyse the tools available to developers. Lastly, we evaluate trusted container projects, test performance, and identify the requirements for migrating applications inside them.

  匹配依据：TEE: trusted execution environments

  </details>

- **Private Federated Learning in Gboard**
  2023-06-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.14793)
  Yuanbo Zhang, Daniel Ramage, Zheng Xu, Yanxiang Zhang, Shumin Zhai, Peter Kairouz

  <details><summary>摘要 / Abstract</summary>

  This white paper describes recent advances in Gboard(Google Keyboard)&#x27;s use of federated learning, DP-Follow-the-Regularized-Leader (DP-FTRL) algorithm, and secure aggregation techniques to train machine learning (ML) models for suggestion, prediction and correction intelligence from many users&#x27; typing data. Gboard&#x27;s investment in those privacy technologies allows users&#x27; typing data to be processed locally on device, to be aggregated as early as possible, and to have strong anonymization and differential privacy where possible. Technical strategies and practices have been established to allow ML models to be trained and deployed with meaningfully formal DP guarantees and high utility. The paper also looks ahead to how technologies such as trusted execution environments may be used to further improve the privacy and security of Gboard&#x27;s ML models.

  匹配依据：TEE: trusted execution environments

  </details>

- **Citadel: Simple Spectre-Safe Isolation For Real-World Programs That Share Memory**
  2023-06-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.14882)
  Jules Drean, Miguel Gomez-Garcia, Fisher Jepsen, Thomas Bourgeat, Srinivas Devadas

  <details><summary>摘要 / Abstract</summary>

  Transient execution side-channel attacks, such as Spectre, have been shown to break almost all isolation primitives. We introduce a new security property we call relaxed microarchitectural isolation (RMI) that allows sensitive programs that are not-constant-time to share memory with an attacker while restricting the information leakage to that of non-speculative execution. Although this type of speculative security property is typically challenging to enforce, we show that we can leverage the enclave setup to achieve it. In particular, we use microarchitectural isolation to restrict attacker&#x27;s observations in conjunction with straightforward hardware mechanisms to limit speculation. This new design point presents a compelling trade-off between security, usability, and performance, making it possible to efficiently enforce RMI for any program. We demonstrate our approach by implementing and evaluating two simple defense mechanisms that satisfy RMI: (1) Safe mode, which disables speculative accesses to shared memory, and (2) Burst mode, a localized performance optimization that requires simple program analysis on small code snippets. Our end-to-end prototype, Citadel, consists of an FPGA-based multicore processor that boots Linux and runs secure applications, including cryptographic libraries and private inference, with less than 5% performance overhead.

  匹配依据：TEE: enclave (context)

  </details>

- **virtCCA: Virtualized Arm Confidential Compute Architecture with TrustZone**
  2023-06-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.11011)
  Xiangyi Xu, Wenhao Wang, Yongzheng Wu, Chenyu Wang, Huifeng Zhu, Haocheng Ma, Zhennan Min, Zixuan Pang, Rui Hou, Yier Jin

  <details><summary>摘要 / Abstract</summary>

  Arm introduced the Confidential Compute Architecture (CCA) in the upcoming Armv9-A architecture, enabling the support of confidential virtual machines (CVMs) in a separate world called the Realm world, providing protection from untrusted normal world. While CCA offers a promising future for confidential computing, the widespread commercial CCA hardware is not available in the near future. To fill this gap, we present virtCCA, an architecture that facilitates virtualized CCA using TrustZone, a mature hardware feature on existing Arm platforms. Notably, virtCCA can be implemented on platforms equipped with the Secure EL2 (S-EL2) extension from ARMv8.4 onwards, as well as on earlier platforms that lack S-EL2 support. virtCCA provides strong compatibility with the CCA specifications at the API level. We developed the entire CCA software and firmware stack on top of virtCCA, including the enhancements to the normal world&#x27;s KVM to support CVMs, and the TrustZone Management Monitor (TMM) that enforces isolation among CVMs and provides CVM lifecycle management. We have implemented virtCCA on real Arm servers, both with and without S-EL2 support. Our evaluation on micro-benchmarks and macrobenchmarks demonstrates that the overhead of running CVMs is acceptable compared to running normal-world VMs. Specifically, in a set of real-world workloads, the overhead of virtCCA-SEL2 is less than 29.7% for I/O intensive workloads, while virtCCA-EL3 outperforms the baseline in most cases.

  匹配依据：TEE: confidential compute architecture, confidential computing, trustzone

  </details>

- **Confidential Computing in Edge-Cloud Hierarchy**
  2023-06-19 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.10834)
  Yeghisabet Alaverdyan, Suren Poghosyan, Vahagn Poghosyan

  <details><summary>摘要 / Abstract</summary>

  The paper introduces confidential computing approaches focused on protecting hierarchical data within edge-cloud network. Edge-cloud network suggests splitting and sharing data between the main cloud and the range of networks near the endpoint devices. The proposed solutions allow data in this two-level hierarchy to be protected via embedding traditional encryption at rest and in transit while leaving the remaining security issues, such as sensitive data and operations in use, in the scope of trusted execution environment. Hierarchical data for each network device are linked and identified through distinct paths between edge and main cloud using individual blockchain. Methods for data and cryptographic key splitting between the edge and the main cloud are based on strong authentication techniques ensuring the shared data confidentiality, integrity and availability.

  匹配依据：TEE: confidential computing, trusted execution environment

  </details>

- **TALUS: Reinforcing TEE Confidentiality with Cryptographic Coprocessors (Technical Report)**
  2023-06-06 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.03643)
  Dhiman Chakraborty, Michael Schwarz, Sven Bugiel

  <details><summary>摘要 / Abstract</summary>

  Platforms are nowadays typically equipped with tristed execution environments (TEES), such as Intel SGX and ARM TrustZone. However, recent microarchitectural attacks on TEEs repeatedly broke their confidentiality guarantees, including the leakage of long-term cryptographic secrets. These systems are typically also equipped with a cryptographic coprocessor, such as a TPM or Google Titan. These coprocessors offer a unique set of security features focused on safeguarding cryptographic secrets. Still, despite their simultaneous availability, the integration between these technologies is practically nonexistent, which prevents them from benefitting from each other&#x27;s strengths. In this paper, we propose TALUS, a general design and a set of three main requirements for a secure symbiosis between TEEs and cryptographic coprocessors. We implement a proof-of-concept of TALUS based on Intel SGX and a hardware TPM. We show that with TALUS, the long-term secrets used in the SGX life cycle can be moved to the TPM. We demonstrate that our design is robust even in the presence of transient execution attacks, preventing an entire class of attacks due to the reduced attack surface on the shared hardware.

  匹配依据：TEE: intel sgx, sgx, trustzone

  </details>

- **Optimized Vectorization Implementation of CRYSTALS-Dilithium**
  2023-06-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2306.01989)
  Jieyu Zheng, Haoliang Zhu, Zhenyu Song, Zheng Wang, Yunlei Zhao

  <details><summary>摘要 / Abstract</summary>

  CRYSTALS-Dilithium is a lattice-based signature scheme to be standardized by NIST as the primary post-quantum signature algorithm. In this work, we make a thorough study of optimizing the implementations of Dilithium by utilizing the Advanced Vector Extension (AVX) instructions, specifically AVX2 and the latest AVX-512. We first present an improved parallel small polynomial multiplication with tailored early evaluation (PSPM-TEE) to further speed up the signing procedure. Our PSPM algorithm outperform the NTT by 47%-66% in AVX2 and AVX-512 implementation. We then present a tailored reduction method that is simpler and faster than Montgomery reduction. We minimize the CPU cycles of tailored reduction AVX-512 implementation by using AVX-512IFMA. Finally, we propose a fully and highly vectorized implementation of Dilithium using AVX-512. This is achieved by carefully vectorizing most of Dilithium functions with the AVX-512 instructions in order to improve efficiency both for time and for space simultaneously. With all the optimization efforts, our AVX-512 implementation improves the performance by 43.2%/39.3%/45.6% in key generation, 36.6%/41.6%/43.7% in signing, and 45.3%/46.5%/47.4% in verification for the parameter sets of Dilithium2/3/5 respectively. To the best of our knowledge, our AVX-512 implementation has the best performance for Dilithium on the Intel x86-64 CPU platform to date.

  匹配依据：TEE: tee (context)

  </details>

- **Securing Cloud File Systems with Trusted Execution**
  2023-05-29 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.18639)
  Quinn Burke, Yohan Beugin, Blaine Hoak, Rachel King, Eric Pauley, Ryan Sheatsley, Mingli Yu, Ting He, Thomas La Porta, Patrick McDaniel

  <details><summary>摘要 / Abstract</summary>

  Cloud file systems offer organizations a scalable and reliable file storage solution. However, cloud file systems have become prime targets for adversaries, and traditional designs are not equipped to protect organizations against the myriad of attacks that may be initiated by a malicious cloud provider, co-tenant, or end-client. Recently proposed designs leveraging cryptographic techniques and trusted execution environments (TEEs) still force organizations to make undesirable trade-offs, consequently leading to either security, functional, or performance limitations. In this paper, we introduce BFS, a cloud file system that leverages the security capabilities provided by TEEs to bootstrap new security protocols that deliver strong security guarantees, high-performance, and a transparent POSIX-like interface to clients. BFS delivers stronger security guarantees and up to a 2.5X speedup over a state-of-the-art secure file system. Moreover, compared to the industry standard NFS, BFS achieves up to 2.2X speedups across micro-benchmarks and incurs &lt;1X overhead for most macro-benchmark workloads. BFS demonstrates a holistic cloud file system design that does not sacrifice an organizations&#x27; security yet can embrace all of the functional and performance advantages of outsourcing.

  匹配依据：TEE: trusted execution environments

  </details>

- **Towards Confidential Computing: A Secure Cloud Architecture for Big Data Analytics and AI**
  2023-05-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.17761)
  Naweiluo Zhou, Florent Dufour, Vinzent Bode, Peter Zinterhof, Nicolay J Hammer, Dieter Kranzlmüller

  <details><summary>摘要 / Abstract</summary>

  Cloud computing provisions computer resources at a cost-effective way based on demand. Therefore it has become a viable solution for big data analytics and artificial intelligence which have been widely adopted in various domain science. Data security in certain fields such as biomedical research remains a major concern when moving their workflows to cloud, because cloud environments are generally outsourced which are more exposed to risks. We present a secure cloud architecture and describes how it enables workflow packaging and scheduling while keeping its data, logic and computation secure in transit, in use and at rest.

  匹配依据：TEE: confidential computing

  </details>

- **CBDC-AquaSphere: Interoperable Central Bank Digital Currency Built on Trusted Computing and Blockchain**
  2023-05-26 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.16893)
  Ivan Homoliak, Martin Perešíni, Patrik Holop, Jakub Handzuš, Fran Casino

  <details><summary>摘要 / Abstract</summary>

  The adoption of decentralized, tamper-proof ledger systems is paving the way for new applications and opportunities in different contexts. While most research aims to improve their scalability, privacy, and governance issues, interoperability has received less attention. Executing transactions across various blockchains is notably instrumental in unlocking the potential of novel applications, particularly in the financial sector, where their potential would otherwise be significantly diminished. Therefore, interoperable ledgers are crucial to ensure the expansion and further adoption of such a technology in various contexts. In this paper, we present a protocol that uses a combination of trusted execution environment (TEE) and blockchains to enable interoperability over independent semi-centralized CBDC ledgers, guaranteeing the atomicity of inter-bank transfers. Our interoperability protocol uses a custom adaptation of atomic swap protocol and is executed by any pair of CBDC instances to realize a one-way transfer. It ensures features such as atomicity, verifiability, correctness, censorship resistance, and privacy while offering high scalability in terms of the number of CBDC instances. Our approach enables to possible deployment scenarios that can be combined: (1) CBDC instances represent central banks of multiple countries, and (2) CBDC instances represent the set of retail banks and a paramount central bank of a single country. We provide a detailed description of our protocol as well as an extensive analysis of its benefits, features, and security. In this WIP paper, we made a proof-of-concept implementation and made a partial evaluation, while the more extensive evaluation will be made in our future work.

  匹配依据：TEE: trusted execution environment

  </details>

- **Nimble: Rollback Protection for Confidential Cloud Services (extended version)**
  2023-05-25 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/761)
  Sebastian Angel, Aditya Basu, Weidong Cui, Trent Jaeger, Stella Lau, Srinath Setty, Sudheesh Singanamalla

  <details><summary>摘要 / Abstract</summary>

  This paper introduces Nimble, a cloud service that helps applications running in trusted execution environments (TEEs) to detect rollback attacks (i.e., detect whether a data item retrieved from persistent storage is the latest version). To achieve this, Nimble realizes an append-only ledger service by employing a simple state machine running in a TEE in conjunction with a crash fault-tolerant storage service. Nimble then replicates this trusted state machine to ensure the system is available even if a minority of state machines crash. A salient aspect of Nimble is a new reconfiguration protocol that allows a cloud provider to replace the set of nodes running the trusted state machine whenever it wishes—without affecting safety. We have formally verified Nimble’s core protocol in Dafny, and have implemented Nimble such that its trusted state machine runs in multiple TEE platforms (Intel SGX and AMD SNP-SEV). Our results show that a deployment of Nimble on machines running in different availability zones can achieve from tens of thousands of requests/sec with an end-to-end latency of under 3.2 ms (based on an in-memory key-value store) to several thousands of requests/sec with a latency of 30ms (based on Azure Table).

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **A Survey of Security Concerns and Countermeasures in Modern Micro-architectures with Transient Execution**
  2023-05-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.16251)
  Nikhilesh Singh, Vinod Ganesan, Chester Rebeiro

  <details><summary>摘要 / Abstract</summary>

  In the last two decades, the evolving cyber-threat landscape has brought to center stage the contentious tradeoffs between the security and performance of modern microprocessors. The guarantees provided by the hardware to ensure no violation of process boundaries have been shown to be breached in several real-world scenarios. While modern CPU features such as superscalar, out-of-order, simultaneous multi-threading, and speculative execution play a critical role in boosting system performance, they are central for a potent class of security attacks termed transient micro-architectural attacks. These attacks leverage shared hardware resources in the CPU that are used during speculative and out-of-order execution to steal sensitive information. Researchers have used these attacks to read data from the Operating Systems (OS) and Trusted Execution Environments (TEE) and to even break hardware-enforced isolation. Over the years, several variants of transient micro-architectural attacks have been developed. While each variant differs in the shared hardware resource used, the underlying attack follows a similar strategy. This paper presents a panoramic view of security concerns in modern CPUs, focusing on the mechanisms of these attacks and providing a classification of the variants. Further, we discuss state-of-the-art defense mechanisms towards mitigating these attacks.

  匹配依据：TEE: trusted execution environments

  </details>

- **Flexible remote attestation of pre-SNP SEV VMs using SGX enclaves**
  2023-05-16 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.09351)
  Pedro Antonino, Ante Derek, Wojciech Aleksander Wołoszyn

  <details><summary>摘要 / Abstract</summary>

  We propose a protocol that explores a synergy between two TEE implementations: it brings SGX-like remote attestation to SEV VMs. We use the notion of a \emph{trusted guest owner}, implemented as an SGX enclave, to deploy, attest, and provision a SEV VM. This machine can, in turn, rely on the trusted owner to generate SGX-like attestation proofs on its behalf. Our protocol combines the application portability of SEV with the flexible remote attestation of SGX. We formalise our protocol and prove that it achieves the intended guarantees using the Tamarin prover. Moreover, we develop an implementation for our trusted guest owner together with example SEV machines, and put those together to demonstrate how our protocol can be used in practice; we use this implementation to evaluate our protocol in the context of creating \emph{accountable machine-learning models}. We also discuss how our protocol can be extended to provide a simple remote attestation mechanism for a heterogeneous infrastructure of trusted components.

  匹配依据：TEE: sgx, sgx enclave, sgx enclaves

  </details>

- **MISO: Legacy-compatible Privacy-preserving Single Sign-on using Trusted Execution Environments**
  2023-05-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.06833)
  Rongwu Xu, Sen Yang, Fan Zhang, Zhixuan Fang

  <details><summary>摘要 / Abstract</summary>

  Single sign-on (SSO) allows users to authenticate to third-party applications through a central identity provider. Despite their wide adoption, deployed SSO systems suffer from privacy problems such as user tracking by the identity provider. While numerous solutions have been proposed by academic papers, none were adopted because they require modifying identity providers, a significant adoption barrier in practice. Solutions do get deployed, however, fail to eliminate major privacy issues. Leveraging Trusted Execution Environments (TEEs), we propose MISO, the first privacy-preserving SSO system that is completely compatible with existing identity providers (such as Google and Facebook). This means MISO can be easily integrated into existing SSO ecosystem today and benefit end users. MISO also enables new functionality that standard SSO cannot offer: MISO allows users to leverage multiple identity providers in a single SSO workflow, potentially in a threshold fashion, to better protect user accounts. We fully implemented MISO based on Intel SGX. Our evaluation shows that MISO can handle high user concurrency with practical performance.

  匹配依据：TEE: intel sgx, trusted execution environments

  </details>

- **Let It TEE: Asynchronous Byzantine Atomic Broadcast with $n \\geq 2f+1$**
  2023-05-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.06123)
  Marc Leinweber, Hannes Hartenstein

  <details><summary>摘要 / Abstract</summary>

  Asynchronous Byzantine Atomic Broadcast (ABAB) promises simplicity in implementation as well as increased performance and robustness in comparison to partially synchronous approaches. We adapt the recently proposed DAG-Rider approach to achieve ABAB with $n\geq 2f+1$ processes, of which $f$ are faulty, with only a constant increase in message size. We leverage a small Trusted Execution Environment (TEE) that provides a unique sequential identifier generator (USIG) to implement Reliable Broadcast with $n&gt;f$ processes and show that the quorum-critical proofs still hold when adapting the quorum size to $\lfloor \frac{n}{2} \rfloor + 1$. This first USIG-based ABAB preserves the simplicity of DAG-Rider and serves as starting point for further research on TEE-based ABAB.

  匹配依据：TEE: trusted execution environment

  </details>

- **Data Station: Delegated, Trustworthy, and Auditable Computation to Enable Data-Sharing Consortia with a Data Escrow**
  2023-05-05 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.03842)
  Siyuan Xia, Zhiru Zhu, Chris Zhu, Jinjin Zhao, Kyle Chard, Aaron J. Elmore, Ian Foster, Michael Franklin, Sanjay Krishnan, Raul Castro Fernandez

  <details><summary>摘要 / Abstract</summary>

  Pooling and sharing data increases and distributes its value. But since data cannot be revoked once shared, scenarios that require controlled release of data for regulatory, privacy, and legal reasons default to not sharing. Because selectively controlling what data to release is difficult, the few data-sharing consortia that exist are often built around data-sharing agreements resulting from long and tedious one-off negotiations. We introduce Data Station, a data escrow designed to enable the formation of data-sharing consortia. Data owners share data with the escrow knowing it will not be released without their consent. Data users delegate their computation to the escrow. The data escrow relies on delegated computation to execute queries without releasing the data first. Data Station leverages hardware enclaves to generate trust among participants, and exploits the centralization of data and computation to generate an audit log. We evaluate Data Station on machine learning and data-sharing applications while running on an untrusted intermediary. In addition to important qualitative advantages, we show that Data Station: i) outperforms federated learning baselines in accuracy and runtime for the machine learning application; ii) is orders of magnitude faster than alternative secure data-sharing frameworks; and iii) introduces small overhead on the critical path.

  匹配依据：TEE: hardware enclaves

  </details>

- **Enhancing IoT Security and Privacy with Trusted Execution Environments and Machine Learning**
  2023-05-04 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.02584)
  Peterson Yuhala

  <details><summary>摘要 / Abstract</summary>

  With the increasing popularity of Internet of Things (IoT) devices, security concerns have become a major challenge: confidential information is constantly being transmitted (sometimes inadvertently) from user devices to untrusted cloud services. This work proposes a design to enhance security and privacy in IoT based systems by isolating hardware peripheral drivers in a trusted execution environment (TEE), and leveraging secure machine learning classification techniques to filter out sensitive data, e.g., speech, images, etc. from the associated peripheral devices before it makes its way to an untrusted party in the cloud.

  匹配依据：TEE: trusted execution environment, trusted execution environments

  </details>

- **SGX Switchless Calls Made Configless**
  2023-05-01 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.00763)
  Peterson Yuhala, Michael Paper, Timothée Zerbib, Pascal Felber, Valerio Schiavoni, Alain Tchana

  <details><summary>摘要 / Abstract</summary>

  Intel&#x27;s software guard extensions (SGX) provide hardware enclaves to guarantee confidentiality and integrity for sensitive code and data. However, systems leveraging such security mechanisms must often pay high performance overheads. A major source of this overhead is SGX enclave transitions which induce expensive cross-enclave context switches. The Intel SGX SDK mitigates this with a switchless call mechanism for transitionless cross-enclave calls using worker threads. Intel&#x27;s SGX switchless call implementation improves performance but provides limited flexibility: developers need to statically fix the system configuration at build time, which is error-prone and misconfigurations lead to performance degradations and waste of CPU resources. ZC-SWITCHLESS is a configless and efficient technique to drive the execution of SGX switchless calls. Its dynamic approach optimises the total switchless worker threads at runtime to minimise CPU waste. The experimental evaluation shows that ZC-SWITCHLESS obviates the performance penalty of misconfigured switchless systems while minimising CPU waste.

  匹配依据：TEE: hardware enclaves, intel sgx, sgx, sgx enclave

  </details>

- **Montsalvat: Partitioning Java Applications to Minimize the TCB in Intel SGX**
  2023-05-01 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.00766)
  Peterson Yuhala, Jämes Ménétrey, Pascal Felber, Valerio Schiavoni, Alain Tchana, Gaël Thomas, Hugo Guiroux, Jean-Pierre Lozi

  <details><summary>摘要 / Abstract</summary>

  The popularity of the Java programming language has led to its wide adoption in cloud computing infrastructures. However, Java applications running in untrusted clouds are vulnerable to various forms of privileged attacks. The emergence of trusted execution environments (TEEs) such as Intel SGX mitigates this problem. TEEs protect code and data in secure enclaves inaccessible to untrusted software, including the kernel and hypervisors. To efficiently use TEEs, developers must manually partition their applications into trusted and untrusted parts, in order to reduce the size of the trusted computing base (TCB) and minimise the risks of security vulnerabilities. However, partitioning applications poses two important challenges: (i) ensuring efficient object communication between the partitioned components, and (ii) ensuring the consistency of garbage collection between the parts, especially with memory-managed languages such as Java. We present Montsalvat, a tool which provides a practical and intuitive annotation-based partitioning approach for Java applications destined for secure enclaves. Montsalvat provides an RMI-like mechanism to ensure inter-object communication, as well as consistent garbage collection across the partitioned components. We implement Montsalvat with GraalVM native-image, a tool for compiling Java applications ahead-of-time into standalone native executables that do not require a JVM at runtime. Our extensive evaluation with micro- and macro-benchmarks shows our partitioning approach to boost performance in real-world applications

  匹配依据：TEE: intel sgx, secure enclaves, trusted execution environments

  </details>

- **faulTPM: Exposing AMD fTPMs' Deepest Secrets**
  2023-04-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.14717)
  Hans Niklas Jacob, Christian Werling, Robert Buhren, Jean-Pierre Seifert

  <details><summary>摘要 / Abstract</summary>

  Trusted Platform Modules constitute an integral building block of modern security features. Moreover, as Windows 11 made a TPM 2.0 mandatory, they are subject to an ever-increasing academic challenge. While discrete TPMs - as found in higher-end systems - have been susceptible to attacks on their exposed communication interface, more common firmware TPMs (fTPMs) are immune to this attack vector as they do not communicate with the CPU via an exposed bus. In this paper, we analyze a new class of attacks against fTPMs: Attacking their Trusted Execution Environment can lead to a full TPM state compromise. We experimentally verify this attack by compromising the AMD Secure Processor, which constitutes the TEE for AMD&#x27;s fTPMs. In contrast to previous dTPM sniffing attacks, this vulnerability exposes the complete internal TPM state of the fTPM. It allows us to extract any cryptographic material stored or sealed by the fTPM regardless of authentication mechanisms such as Platform Configuration Register validation or passphrases with anti-hammering protection. First, we demonstrate the impact of our findings by - to the best of our knowledge - enabling the first attack against Full Disk Encryption solutions backed by an fTPM. Furthermore, we lay out how any application relying solely on the security properties of the TPM - like Bitlocker&#x27;s TPM- only protector - can be defeated by an attacker with 2-3 hours of physical access to the target device. Lastly, we analyze the impact of our attack on FDE solutions protected by a TPM and PIN strategy. While a naive implementation also leaves the disk completely unprotected, we find that BitLocker&#x27;s FDE implementation withholds some protection depending on the complexity of the used PIN. Our results show that when an fTPM&#x27;s internal state is compromised, a TPM and PIN strategy for FDE is less secure than TPM-less protection with a reasonable passphrase.

  匹配依据：TEE: trusted execution environment

  </details>

- **NNSplitter: An Active Defense Solution for DNN Model via Automated Weight Obfuscation**
  2023-04-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2305.00097) · [Code](https://github.com/Tongzhou0101/NNSplitter)
  Tong Zhou, Yukui Luo, Shaolei Ren, Xiaolin Xu

  <details><summary>摘要 / Abstract</summary>

  As a type of valuable intellectual property (IP), deep neural network (DNN) models have been protected by techniques like watermarking. However, such passive model protection cannot fully prevent model abuse. In this work, we propose an active model IP protection scheme, namely NNSplitter, which actively protects the model by splitting it into two parts: the obfuscated model that performs poorly due to weight obfuscation, and the model secrets consisting of the indexes and original values of the obfuscated weights, which can only be accessed by authorized users with the support of the trusted execution environment. Experimental results demonstrate the effectiveness of NNSplitter, e.g., by only modifying 275 out of over 11 million (i.e., 0.002%) weights, the accuracy of the obfuscated ResNet-18 model on CIFAR-10 can drop to 10%. Moreover, NNSplitter is stealthy and resilient against norm clipping and fine-tuning attacks, making it an appealing solution for DNN model protection. The code is available at: https://github.com/Tongzhou0101/NNSplitter.

  匹配依据：TEE: trusted execution environment

  </details>

- **You Can't Always Check What You Wanted: Selective Checking and Trusted Execution to Prevent False Actuations in Cyber-Physical Systems**
  2023-04-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.13956)
  Monowar Hasan, Sibin Mohan

  <details><summary>摘要 / Abstract</summary>

  Cyber-physical systems (CPS) are vulnerable to attacks targeting outgoing actuation commands that modify their physical behaviors. The limited resources in such systems, coupled with their stringent timing constraints, often prevents the checking of every outgoing command. We present a &quot;selective checking&quot; mechanism that uses game-theoretic modeling to identify the right subset of commands to be checked in order to deter an adversary. This mechanism is coupled with a &quot;delay-aware&quot; trusted execution environment (TEE) to ensure that only verified actuation commands are ever sent to the physical system, thus maintaining their safety and integrity. The selective checking and trusted execution (SCATE) framework is implemented on an off-the-shelf ARM platform running standard embedded Linux. We demonstrate the effectiveness of SCATE using four realistic cyber-physical systems (a ground rover, a flight controller, a robotic arm and an automated syringe pump) and study design trade-offs. Not only does SCATE provide a high level of security and high performance, it also suffers from significantly lower overheads (30.48%-47.32% less) in the process. In fact, SCATE can work with more systems without negatively affecting the safety of the system. Considering that most CPS do not have any such checking mechanisms, and SCATE is guaranteed to meet all the timing requirements (i.e., ensure the safety/integrity of the system), our methods can significantly improve the security (and, hence, safety) of the system.

  匹配依据：TEE: trusted execution environment

  </details>

- **Blockchain-based Federated Learning with Secure Aggregation in Trusted Execution Environment for Internet-of-Things**
  2023-04-25 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.12889)
  Aditya Pribadi Kalapaaking, Ibrahim Khalil, Mohammad Saidur Rahman, Mohammed Atiquzzaman, Xun Yi, Mahathir Almashor

  <details><summary>摘要 / Abstract</summary>

  This paper proposes a blockchain-based Federated Learning (FL) framework with Intel Software Guard Extension (SGX)-based Trusted Execution Environment (TEE) to securely aggregate local models in Industrial Internet-of-Things (IIoTs). In FL, local models can be tampered with by attackers. Hence, a global model generated from the tampered local models can be erroneous. Therefore, the proposed framework leverages a blockchain network for secure model aggregation. Each blockchain node hosts an SGX-enabled processor that securely performs the FL-based aggregation tasks to generate a global model. Blockchain nodes can verify the authenticity of the aggregated model, run a blockchain consensus mechanism to ensure the integrity of the model, and add it to the distributed ledger for tamper-proof storage. Each cluster can obtain the aggregated model from the blockchain and verify its integrity before using it. We conducted several experiments with different CNN models and datasets to evaluate the performance of the proposed framework.

  匹配依据：TEE: sgx, trusted execution environment

  </details>

- **Scalable Private Signaling**
  2023-04-23 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/572)
  Sashidhar Jakkamsetti, Zeyu Liu, Varun Madathil

  <details><summary>摘要 / Abstract</summary>

  Private messaging systems that use a bulletin board, like privacy-preserving blockchains, have been a popular topic during the last couple of years. In these systems, typically a private message is posted on the board for a recipient and the privacy requirement is that no one can determine the sender and the recipient of the message. Until recently, the efficiency of these recipients was not considered, and the party had to perform a naive scan of the board to retrieve their messages. More recently, works like Fuzzy Message Detection (FMD), Private Signaling (PS), and Oblivious Message Retrieval (OMR) have studied the problem of protecting recipient privacy by outsourcing the message retrieval process to an untrusted server. However, FMD only provides limited privacy guarantees, and PS and OMR greatly lack scalability. In this work, we present a new construction for private signaling which is both asymptotically superior and concretely orders of magnitude faster than all prior works while providing full privacy. Our constructions make use of a trusted execution environment (TEE) and an Oblivious RAM to improve the computation complexity of the server. We also improve the privacy guarantees by keeping the recipient hidden even during the retrieval of signals from the server. Our proof-of-concept open-source implementation shows that for a server serving a million recipients and ten million messages, it only takes $&lt; 60$ milliseconds to process a sent message, and $&lt; 6$ seconds to process a retrieval (of 100 signals) request from a recipient.

  匹配依据：TEE: trusted execution environment

  </details>

- **AVX Timing Side-Channel Attacks against Address Space Layout Randomization**
  2023-04-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.07940)
  Hyunwoo Choi, Suryeon Kim, Seungwon Shin

  <details><summary>摘要 / Abstract</summary>

  Modern x86 processors support an AVX instruction set to boost performance. However, this extension may cause security issues. We discovered that there are vulnerable properties in implementing masked load/store instructions. Based on this, we present a novel AVX timing side-channel attack that can defeat address space layout randomization. We demonstrate the significance of our attack by showing User and Kernel ASLR breaks on the recent Intel and AMD processors in various environments, including cloud computing systems, an SGX enclave (a fine-grained ASLR break), and major operating systems. We further demonstrate that our attack can be used to infer user behavior, such as Bluetooth events and mouse movements. We highlight that stronger isolation or more fine-grained randomization should be adopted to successfully mitigate our presented attacks.

  匹配依据：TEE: sgx, sgx enclave

  </details>

- **CoVE: Towards Confidential Computing on RISC-V Platforms**
  2023-04-12 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.06167)
  Ravi Sahita, Atish Patra, Vedvyas Shanbhogue, Samuel Ortiz, Andrew Bresticker, Dylan Reid, Atul Khare, Rajnesh Kanwal

  <details><summary>摘要 / Abstract</summary>

  Multi-tenant computing platforms are typically comprised of several software and hardware components including platform firmware, host operating system kernel, virtualization monitor, and the actual tenant payloads that run on them (typically in a virtual machine, container, or application). This model is well established in large scale commercial deployment, but the downside is that all platform components and operators are in the Trusted Computing Base (TCB) of the tenant. This aspect is ill-suited for privacy-oriented workloads that aim to minimize the TCB footprint. Confidential computing presents a good stepping-stone towards providing a quantifiable TCB for computing. Confidential computing [1] requires the use of a HW-attested Trusted Execution Environments for data-in-use protection. The RISC-V architecture presents a strong foundation for meeting the requirements for Confidential Computing and other security paradigms in a clean slate manner. This paper describes a reference architecture and discusses ISA, non-ISA and system-on-chip (SoC) requirements for confidential computing on RISC-V Platforms. It discusses proposed ISA and non-ISA Extension for Confidential Virtual Machine for RISC-V platforms, referred to as CoVE.

  匹配依据：TEE: confidential computing, trusted execution environments

  </details>

- **A visão da BBChain sobre o contexto tecnológico subjacente à adoção do Real Digital**
  2023-04-10 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2304.04833)
  Marcio G B de Avellar, Alexandre A S Junior, André H G Lopes, André L S Carneiro, João A Pereira, Davi C B D da Cunha

  <details><summary>摘要 / Abstract</summary>

  We explore confidential computing in the context of CBDCs using Microsoft&#x27;s CCF framework as an example. By developing an experiment and comparing different approaches and performance and security metrics, we seek to evaluate the effectiveness of confidential computing to improve the privacy, security, and performance of CBDCs. Preliminary results suggest that confidential computing could be a promising solution to the technological challenges faced by CBDCs. Furthermore, by implementing confidential computing in DLTs such as Hyperledger Besu and utilizing frameworks such as CCF, we increase transaction confidentiality and privacy while maintaining the scalability and interoperability required for a global digital financial system. In conclusion, confidential computing can significantly bolster CBDC development, fostering a secure, private, and efficient financial future. -- Exploramos o uso da computação confidencial no contexto das CBDCs utilizando o framework CCF da Microsoft como exemplo. Via desenvolvimento de experimentos e comparação de diferentes abordagens e métricas de desempenho e segurança, buscamos avaliar a eficácia da computação confidencial para melhorar a privacidade, segurança e desempenho das CBDCs. Resultados preliminares sugerem que a computação confidencial pode ser uma solução promissora para os desafios tecnológicos enfrentados pelas CBDCs. Ao implementar a computação confidencial em DLTs, como o Hyperledger Besu, e utilizar frameworks como o CCF, aumentamos a confidencialidade e a privacidade das transações, mantendo a escalabilidade e a interoperabilidade necessárias para um sistema financeiro global e digital. Em conclusão, a computação confidencial pode reforçar significativamente o desenvolvimento do CBDC, promovendo um futuro financeiro seguro, privado e eficiente.

  匹配依据：TEE: confidential computing

  </details>

- **Remote attestation of SEV-SNP confidential VMs using e-vTPMs**
  2023-03-29 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.16463)
  Vikram Narayanan, Claudio Carvalho, Angelo Ruocco, Gheorghe Almási, James Bottomley, Mengmei Ye, Tobin Feldman-Fitzthum, Daniele Buono, Hubertus Franke, Anton Burtsev

  <details><summary>摘要 / Abstract</summary>

  Trying to address the security challenges of a cloud-centric software deployment paradigm, silicon and cloud vendors are introducing confidential computing - an umbrella term aimed at providing hardware and software mechanisms for protecting cloud workloads from the cloud provider and its software stack. Today, Intel SGX, AMD SEV, Intel TDX, etc., provide a way to shield cloud applications from the cloud provider through encryption of the application&#x27;s memory below the hardware boundary of the CPU, hence requiring trust only in the CPU vendor. Unfortunately, existing hardware mechanisms do not automatically enable the guarantee that a protected system was not tampered with during configuration and boot time. Such a guarantee relies on a hardware RoT, i.e., an integrity-protected location that can store measurements in a trustworthy manner, extend them, and authenticate the measurement logs to the user. In this work, we design and implement a virtual TPM that virtualizes the hardware RoT without requiring trust in the cloud provider. To ensure the security of a vTPM in a provider-controlled environment, we leverage unique isolation properties of the SEV-SNP hardware that allows us to execute secure services as part of the enclave environment protected from the cloud provider. We further develop a novel approach to vTPM state management where the vTPM state is not preserved across reboots. Specifically, we develop a stateless ephemeral vTPM that supports remote attestation without any persistent state on the host. This allows us to pair each confidential VM with a private instance of a vTPM completely isolated from the provider-controlled environment and other VMs. We built our prototype entirely on open-source components. Though our work is AMD-specific, a similar approach could be used to build remote attestation protocols on other trusted execution environments.

  匹配依据：TEE: amd sev, confidential computing, intel sgx, intel tdx, sev snp, trusted execution environments

  </details>

- **Cyber Security aboard Micro Aerial Vehicles: An OpenTitan-based Visual Communication Use Case**
  2023-03-29 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.16554)
  Maicol Ciani, Stefano Bonato, Rafail Psiakis, Angelo Garofalo, Luca Valente, Suresh Sugumar, Alessandro Giusti, Davide Rossi, Daniele Palossi

  <details><summary>摘要 / Abstract</summary>

  Autonomous Micro Aerial Vehicles (MAVs), with a form factor of 10cm in diameter, are an emerging technology thanks to the broad applicability enabled by their onboard intelligence. However, these platforms are strongly limited in the onboard power envelope for processing, i.e., less than a few hundred mW, which confines the onboard processors to the class of simple microcontroller units (MCUs). These MCUs lack advanced security features opening the way to a wide range of cyber security vulnerabilities, from the communication between agents of the same fleet to the onboard execution of malicious code. This work presents an open source System on Chip (SoC) design that integrates a 64 bit Linux capable host processor accelerated by an 8 core 32 bit parallel programmable accelerator. The heterogeneous system architecture is coupled with a security enclave based on an open source OpenTitan root of trust. To demonstrate our design, we propose a use case where OpenTitan detects a security breach on the SoC aboard the MAV and drives its exclusive GPIOs to start a LED blinking routine. This procedure embodies an unconventional visual communication between two palm sized MAVs: the receiver MAV classifies the LED state of the sender (on or off) with an onboard convolutional neural network running on the parallel accelerator. Then, it reconstructs a high-level message in 1.3s, 2.3 times faster than current commercial solutions.

  匹配依据：TEE: enclave (context)

  </details>

- **Intel TDX Demystified: A Top-Down Approach**
  2023-03-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.15540)
  Pau-Chen Cheng, Wojciech Ozga, Enriquillo Valdez, Salman Ahmed, Zhongshu Gu, Hani Jamjoom, Hubertus Franke, James Bottomley

  <details><summary>摘要 / Abstract</summary>

  Intel Trust Domain Extensions (TDX) is a new architectural extension in the 4th Generation Intel Xeon Scalable Processor that supports confidential computing. TDX allows the deployment of virtual machines in the Secure-Arbitration Mode (SEAM) with encrypted CPU state and memory, integrity protection, and remote attestation. TDX aims to enforce hardware-assisted isolation for virtual machines and minimize the attack surface exposed to host platforms, which are considered to be untrustworthy or adversarial in the confidential computing&#x27;s new threat model. TDX can be leveraged by regulated industries or sensitive data holders to outsource their computations and data with end-to-end protection in public cloud infrastructure. This paper aims to provide a comprehensive understanding of TDX to potential adopters, domain experts, and security researchers looking to leverage the technology for their own purposes. We adopt a top-down approach, starting with high-level security principles and moving to low-level technical details of TDX. Our analysis is based on publicly available documentation and source code, offering insights from security researchers outside of Intel.

  匹配依据：TEE: confidential computing, intel tdx, trust domain extensions

  </details>

- **Software-based security approach for networked embedded devices**
  2023-03-14 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.07975)
  José Ferreira, Alan Oliveira, André Souto, José Cecílio

  <details><summary>摘要 / Abstract</summary>

  As the Internet of Things (IoT) continues to expand, data security has become increasingly important for ensuring privacy and safety, especially given the sensitive and, sometimes, critical nature of the data handled by IoT devices. There exist hardware-based trusted execution environments used to protect data, but they are not compatible with low-cost devices that lack hardware-assisted security features. The research in this paper presents software-based protection and encryption mechanisms explicitly designed for embedded devices. The proposed architecture is designed to work with low-cost, low-end devices without requiring the usual changes on the underlying hardware. It protects against hardware attacks and supports runtime updates, enabling devices to write data in protected memory. The proposed solution is an alternative data security approach for low-cost IoT devices without compromising performance or functionality. Our work underscores the importance of developing secure and cost-effective solutions for protecting data in the context of IoT.

  匹配依据：TEE: trusted execution environments

  </details>

- **ISC-FLAT: On the Conflict Between Control Flow Attestation and Real-Time Operations**
  2023-03-07 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2303.03561)
  Antonio Joia Neto, Ivan de Oliveira Nunes

  <details><summary>摘要 / Abstract</summary>

  The wide adoption of IoT gadgets and Cyber-Physical Systems (CPS) makes embedded devices increasingly important. While some of these devices perform mission-critical tasks, they are usually implemented using Micro-Controller Units (MCUs) that lack security mechanisms on par with those available to general-purpose computers, making them more susceptible to remote exploits that could corrupt their software integrity. Motivated by this problem, prior work has proposed techniques to remotely assess the trustworthiness of embedded MCU software. Among them, Control Flow Attestation (CFA) enables remote detection of runtime abuses that illegally modify the program&#x27;s control flow during execution. Despite these advances, current CFA methods share a fundamental limitation: they preclude interrupts during the execution of the software operation being attested. Simply put, existing CFA techniques are insecure unless interrupts are disabled on the MCU. On the other hand, we argue that the lack of interruptability can obscure CFA usefulness, as most embedded applications depend on interrupts to process asynchronous events in real-time. To address this limitation, we propose Interrupt-Safe Control Flow Attestation (ISC-FLAT): a CFA technique that is compatible with existing MCUs and enables interrupt handling without compromising the authenticity of CFA reports. Similar to other CFA techniques that do not require customized hardware modifications, ISC-FLAT leverages a Trusted Execution Environment (TEE) (in particular, our prototype is built on ARM TrustZone-M) to securely generate unforgeable CFA reports without precluding applications from processing interrupts. We implement a fully functional ISC-FLAT prototype on the ARM Cortex-M33 MCU and demonstrate that it incurs minimal runtime overhead when compared to existing TEE-based CFA methods that do not support interrupts.

  匹配依据：TEE: trusted execution environment, trustzone

  </details>

- **Capstone: A Capability-based Foundation for Trustless Secure Memory Access (Extended Version)**
  2023-02-27 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.13863)
  Jason Zhijingcheng Yu, Conrad Watt, Aditya Badole, Trevor E. Carlson, Prateek Saxena

  <details><summary>摘要 / Abstract</summary>

  Capability-based memory isolation is a promising new architectural primitive. Software can access low-level memory only via capability handles rather than raw pointers, which provides a natural interface to enforce security restrictions. Existing architectural capability designs such as CHERI provide spatial safety, but fail to extend to other memory models that security-sensitive software designs may desire. In this paper, we propose Capstone, a more expressive architectural capability design that supports multiple existing memory isolation models in a trustless setup, i.e., without relying on trusted software components. We show how Capstone is well-suited for environments where privilege boundaries are fluid (dynamically extensible), memory sharing/delegation are desired both temporally and spatially, and where such needs are to be balanced with availability concerns. Capstone can also be implemented efficiently. We present an implementation sketch and through evaluation show that its overhead is below 50% in common use cases. We also prototype a functional emulator for Capstone and use it to demonstrate the runnable implementations of six real-world memory models without trusted software components: three types of enclave-based TEEs, a thread scheduler, a memory allocator, and Rust-style memory safety -- all within the interface of Capstone.

  匹配依据：TEE: enclave (context)

  </details>

- **Parma: Confidential Containers via Attested Execution Policies**
  2023-02-08 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2302.03976)
  Matthew A. Johnson, Stavros Volos, Ken Gordon, Sean T. Allen, Christoph M. Wintersteiger, Sylvan Clebsch, John Starks, Manuel Costa

  <details><summary>摘要 / Abstract</summary>

  Container-based technologies empower cloud tenants to develop highly portable software and deploy services in the cloud at a rapid pace. Cloud privacy, meanwhile, is important as a large number of container deployments operate on privacy-sensitive data, but challenging due to the increasing frequency and sophistication of attacks. State-of-the-art confidential container-based designs leverage process-based trusted execution environments (TEEs), but face security and compatibility issues that limits their practical deployment. We propose Parma, an architecture that provides lift-and-shift deployment of unmodified containers while providing strong security protection against a powerful attacker who controls the untrusted host and hypervisor. Parma leverages VM-level isolation to execute a container group within a unique VM-based TEE. Besides container integrity and user data confidentiality and integrity, Parma also offers container attestation and execution integrity based on an attested execution policy. Parma execution policies provide an inductive proof over all future states of the container group. This proof, which is established during initialization, forms a root of trust that can be used for secure operations within the container group without requiring any modifications of the containerized workflow itself (aside from the inclusion of the execution policy.) We evaluate Parma on AMD SEV-SNP processors by running a diverse set of workloads demonstrating that workflows exhibit 0-26% additional overhead in performance over running outside the enclave, with a mean 13% overhead on SPEC2017, while requiring no modifications to their program code. Adding execution policies introduces less than 1% additional overhead. Furthermore, we have deployed Parma as the underlying technology driving Confidential Containers on Azure Container Instances.

  匹配依据：TEE: amd sev, trusted execution environments

  </details>

- **BAFFLE: A Baseline of Backpropagation-Free Federated Learning**
  2023-01-28 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2301.12195) · [Code](https://github.com/FengHZ/BAFFLE)
  Haozhe Feng, Tianyu Pang, Chao Du, Wei Chen, Shuicheng Yan, Min Lin

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) is a general principle for decentralized clients to train a server model collectively without sharing local data. FL is a promising framework with practical applications, but its standard training paradigm requires the clients to backpropagate through the model to compute gradients. Since these clients are typically edge devices and not fully trusted, executing backpropagation on them incurs computational and storage overhead as well as white-box vulnerability. In light of this, we develop backpropagation-free federated learning, dubbed BAFFLE, in which backpropagation is replaced by multiple forward processes to estimate gradients. BAFFLE is 1) memory-efficient and easily fits uploading bandwidth; 2) compatible with inference-only hardware optimization and model quantization or pruning; and 3) well-suited to trusted execution environments, because the clients in BAFFLE only execute forward propagation and return a set of scalars to the server. Empirically we use BAFFLE to train deep models from scratch or to finetune pretrained models, achieving acceptable results. Code is available in https://github.com/FengHZ/BAFFLE.

  匹配依据：TEE: trusted execution environments

  </details>

- **Cache-timing attack against HQC**
  2023-01-27 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/102)
  Senyang Huang, Rui Qi Sim, Chitchanok Chuengsatiansup, Qian Guo, Thomas Johansson

  <details><summary>摘要 / Abstract</summary>

  In this paper, we present the first chosen-ciphertext (CC) cache-timing attacks on the reference implementation of HQC. We build a cache-timing based distinguisher for implementing a plaintext-checking (PC) oracle. The PC oracle uses side-channel information to check if a given ciphertext decrypts to a given message. This is done by identifying a vulnerability during the generating process of two vectors in the reference implementation of HQC. We also propose a new method of using PC oracles for chosen-ciphertext side-channel attacks against HQC, which may have independent interest. We show a general proof-of-concept attack, where we use the Flush&amp;Reload technique and also derive, in more detail, a practical attack on an HQC execution on Intel SGX, where the Prime&amp;Probe technique is used. We show the exact path to do key recovery by explaining the detailed steps, using the PC oracle. In both scenarios, the new attack requires $53,857$ traces on average with much fewer PC oracle calls than the timing attack of Guo et al. CHES 2022 on an HQC implementation.

  匹配依据：TEE: intel sgx

  </details>

- **Blockchain based Resource Governance for Decentralized Web Environments**
  2023-01-17 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2301.06919)
  Davide Basile, Claudio Di Ciccio, Valerio Goretti, Sabrina Kirrane

  <details><summary>摘要 / Abstract</summary>

  Decentralization initiatives such as Solid and ActivityPub aim to give data owners more control over their data and to level the playing field by enabling small companies and individuals to gain access to data, thus stimulating innovation. However, these initiatives typically employ access control mechanisms that cannot verify compliance with usage conditions after access has been granted to others. In this paper, we extend the state of the art by proposing a resource governance conceptual framework, entitled ReGov, that facilitates usage control in decentralized web environments. We subsequently demonstrate how our framework can be instantiated by combining blockchain and trusted execution environments. Through blockchain technologies, we record policies expressing the usage conditions associated with resources and monitor their compliance. Our instantiation employs trusted execution environments to enforce said policies, inside data consumers&#x27; devices.} We evaluate the framework instantiation through a detailed analysis of requirements derived from a data market motivating scenario, as well as an assessment of the security, privacy, and affordability aspects of our proposal.

  匹配依据：TEE: trusted execution environments

  </details>

- **PMFault: Faulting and Bricking Server CPUs through Management Interfaces**
  2023-01-13 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2301.05538)
  Zitai Chen, David Oswald

  <details><summary>摘要 / Abstract</summary>

  Apart from the actual CPU, modern server motherboards contain other auxiliary components, for example voltage regulators for power management. Those are connected to the CPU and the separate Baseboard Management Controller (BMC) via the I2C-based PMBus. In this paper, using the case study of the widely used Supermicro X11SSL motherboard, we show how remotely exploitable software weaknesses in the BMC (or other processors with PMBus access) can be used to access the PMBus and then perform hardware-based fault injection attacks on the main CPU. The underlying weaknesses include insecure firmware encryption and signing mechanisms, a lack of authentication for the firmware upgrade process and the IPMI KCS control interface, as well as the motherboard design (with the PMBus connected to the BMC and SMBus by default). First, we show that undervolting through the PMBus allows breaking the integrity guarantees of SGX enclaves, bypassing Intel&#x27;s countermeasures against previous undervolting attacks like Plundervolt/V0ltPwn. Second, we experimentally show that overvolting outside the specified range has the potential of permanently damaging Intel Xeon CPUs, rendering the server inoperable. We assess the impact of our findings on other server motherboards made by Supermicro and ASRock. Our attacks, dubbed PMFault, can be carried out by a privileged software adversary and do not require physical access to the server motherboard or knowledge of the BMC login credentials. We responsibly disclosed the issues reported in this paper to Supermicro and discuss possible countermeasures at different levels. To the best of our knowledge, the 12th generation of Supermicro motherboards, which was designed before we reported PMFault to Supermicro, is not vulnerable.

  匹配依据：TEE: sgx, sgx enclaves

  </details>

- **MVAM: Multi-variant Attacks on Memory for IoT Trust Computing**
  2023-01-11 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2301.04591)
  Arup Kumar Sarker, Md Khairul Islam, Yuan Tian

  <details><summary>摘要 / Abstract</summary>

  With the significant development of the Internet of Things and low-cost cloud services, the sensory and data processing requirements of IoT systems are continually going up. TrustZone is a hardware-protected Trusted Execution Environment (TEE) for ARM processors specifically designed for IoT handheld systems. It provides memory isolation techniques to protect trusted application data from being exploited by malicious entities. In this work, we focus on identifying different vulnerabilities of the TrustZone extension of ARM Cortex-M processors. Then design and implement a threat model to execute those attacks. We have found that TrustZone is vulnerable to buffer overflow-based attacks. We have used this to create an attack called MOFlow and successfully leaked the data of another trusted app. This is done by intentionally overflowing the memory of one app to access the encrypted memory of other apps inside the secure world. We have also found that, by not validating the input parameters in the entry function, TrustZone has exposed a security weakness. We call this Achilles heel and present an attack model showing how to exploit this weakness too. Our proposed novel attacks are implemented and successfully tested on two recent ARM Cortex-M processors available on the market (M23 and M33).

  匹配依据：TEE: trusted execution environment, trustzone

  </details>

- **It Runs and it Hides: A Function-Hiding Construction for Private-Key Multi-Input Functional Encryption**
  2023-01-07 · TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2023/024)
  Alexandros Bakas, Antonis Michalas

  <details><summary>摘要 / Abstract</summary>

  Functional Encryption (FE) is a modern cryptographic technique that allows users to learn only a specific function of the encrypted data and nothing else about its actual content. While the first notions of security in FE revolved around the privacy of the encrypted data, more recent approaches also consider the privacy of the computed function. While in the public key setting, only a limited level of function-privacy can be achieved, in the private-key setting privacy potential is significantly larger. However, this potential is still limited by the lack of rich function families. For this work, we started by identifying the limitations of the current state-of-the-art approaches which, in its turn, allowed us to consider a new threat model for FE schemes. To the best of our knowledge, we here present the first attempt to quantify the leakage during the execution of an FE scheme. By leveraging the functionality offered by Trusted Execution Environments, we propose a construction that given any message-private functional encryption scheme yields a function-private one. Finally, we argue in favour of our construction&#x27;s applicability on constrained devices by showing that it has low storage and computation costs.

  匹配依据：TEE: trusted execution environments

  </details>

- **AI-Driven Confidential Computing across Edge-to-Cloud Continuum**
  2023-01-03 · TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2301.00928)
  SM Zobaed

  <details><summary>摘要 / Abstract</summary>

  With the meteoric growth of technology, individuals and organizations are widely adopting cloud services to mitigate the burdens of maintenance. Despite its scalability and ease of use, many users who own sensitive data refrain from fully utilizing cloud services due to confidentiality concerns. Maintaining data confidentiality for data at rest and in transit has been widely explored but data remains vulnerable in the cloud while it is in use. This vulnerability is further elevated once the scope of computing spans across the edge-to-cloud continuum. Accordingly, the goal of this dissertation is to enable data confidentiality by adopting confidential computing across the continuum. Towards this goal, one approach we explore is to separate the intelligence aspect of data processing from the pattern-matching aspect. We present our approach to make confidential data clustering on the cloud, and then develop confidential search service across edge-to-cloud for unstructured text data. Our proposed clustering solution named ClusPr, performs topic-based clustering for static and dynamic datasets that improves cluster coherency up to 30%-to-60% when compared with other encryption-based clustering techniques. Our trusted enterprise search service named SAED, provides context-aware and personalized semantic search over confidential data across the continuum. We realized that enabling confidential computing across edge-to-cloud requires major contribution from the edge tiers particularly to run multiple Deep Learning (DL) services concurrently. This raises memory contention on the edge tier. To resolve this, we develop Edge-MultiAI framework to manage Neural Network (NN) models of DL applications such that it can meet the latency constraints of the DL applications without compromising inference accuracy.

  匹配依据：TEE: confidential computing

  </details>
