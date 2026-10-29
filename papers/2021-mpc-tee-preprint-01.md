# 2021 · MPC + TEE · 仅预印本来源 · 第 1/1 页

[总目录](../PAPERS.md)

- **CHEX-MIX: Combining Homomorphic Encryption with Trusted Execution Environments for Two-party Oblivious Inference in the Cloud**
  2021-12-09 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1603)
  Deepika Natarajan, Andrew Loveless, Wei Dai, Ronald Dreslinski

  <details><summary>摘要 / Abstract</summary>

  Data, when coupled with state-of-the-art machine learning models, can enable remarkable applications. But, there exists an underlying tension: users wish to keep their data private, and model providers wish to protect their intellectual property. Homomorphic encryption (HE) and multi-party computation (MPC) techniques have been proposed as solutions to this problem; however, both techniques require model providers to fully trust the server performing the machine learning computation. This limits the scale of inference applications, since it prevents model providers from leveraging shared public cloud infrastructures. In this work, we present CHEX-MIX, a solution to the problem of privacy-preserving machine learning between two mutually distrustful parties in an untrusted cloud setting. CHEX-MIX relies on a combination of HE and trusted execution environments (TEEs), using HE to provide clients with confidentiality guarantees, and TEEs to provide model providers with confidentiality guarantees and protect the integrity of computation from malicious cloud adversaries. Unlike prior solutions to this problem, such as multi-key HE, single-key HE, MPC, or TEE-only techniques, our solution assumes that both the client and the cloud can be malicious, makes no collusion assumptions, and frees model providers from needing to maintain private online infrastructures. Our results show that CHEX-MIX can execute at high efficiency, with low communication cost, while providing security guarantees unaddressed by prior work. Compared to a recent multi-key HE work that allows partial cloud offload, for example, CHEX-MIX achieves a 3× lower communication cost and a 3× faster computation time.

  匹配依据：MPC: multi party computation; TEE: trusted execution environments

  </details>

- **Flatee: Federated Learning Across Trusted Execution Environments**
  2021-11-12 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2111.06867)
  Arup Mondal, Yash More, Ruthu Hulikal Rooparaghunath, Debayan Gupta

  <details><summary>摘要 / Abstract</summary>

  Federated learning allows us to distributively train a machine learning model where multiple parties share local model parameters without sharing private data. However, parameter exchange may still leak information. Several approaches have been proposed to overcome this, based on multi-party computation, fully homomorphic encryption, etc.; many of these protocols are slow and impractical for real-world use as they involve a large number of cryptographic operations. In this paper, we propose the use of Trusted Execution Environments (TEE), which provide a platform for isolated execution of code and handling of data, for this purpose. We describe Flatee, an efficient privacy-preserving federated learning framework across TEEs, which considerably reduces training and communication time. Our framework can handle malicious parties (we do not natively solve adversarial data poisoning, though we describe a preliminary approach to handle this).

  匹配依据：MPC: multi party computation; TEE: trusted execution environments

  </details>

- **PIM-Enclave: Bringing Confidential Computation Inside Memory**
  2021-11-05 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2111.03307)
  Kha Dinh Duy, Hojoon Lee

  <details><summary>摘要 / Abstract</summary>

  Demand for data-intensive workloads and confidential computing are the prominent research directions shaping the future of cloud computing. Computer architectures are evolving to accommodate the computing of large data better. Protecting the computation of sensitive data is also an imperative yet challenging objective; processor-supported secure enclaves serve as the key element in confidential computing in the cloud. However, side-channel attacks are threatening their security boundaries. The current processor architectures consume a considerable portion of its cycles in moving data. Near data computation is a promising approach that minimizes redundant data movement by placing computation inside storage. In this paper, we present a novel design for Processing-In-Memory (PIM) as a data-intensive workload accelerator for confidential computing. Based on our observation that moving computation closer to memory can achieve efficiency of computation and confidentiality of the processed information simultaneously, we study the advantages of confidential computing \emph{inside} memory. We then explain our security model and programming model developed for PIM-based computation offloading. We construct our findings into a software-hardware co-design, which we call PIM-Enclave. Our design illustrates the advantages of PIM-based confidential computing acceleration. Our evaluation shows PIM-Enclave can provide a side-channel resistant secure computation offloading and run data-intensive applications with negligible performance overhead compared to baseline PIM model.

  匹配依据：MPC: secure computation; TEE: confidential computing, secure enclaves

  </details>

- **GPS: Integration of Graphene, PALISADE, and SGX for Large-scale Aggregations of Distributed Data**
  2021-09-14 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/1155)
  Jonathan Takeshita, Colin McKechney, Justin Pajak, Antonis Papadimitriou, Ryan Karl, Taeho Jung

  <details><summary>摘要 / Abstract</summary>

  Secure computing methods such as fully homomorphic encryption and hardware solutions such as Intel Software Guard Extension (SGX) have been applied to provide security for user input in privacy-oriented computation outsourcing. Fully homomorphic encryption is amenable to parallelization and hardware acceleration to improve its scalability and latency, but is limited in the complexity of functions it can efficiently evaluate. SGX is capable of arbitrarily complex calculations, but due to expensive memory paging and context switches, computations in SGX are bound by practical limits. These limitations make either of fully homomorphic encryption or SGX alone unsuitable for large-scale multi-user computations with complex intermediate calculations. In this paper, we present GPS, a novel framework integrating the Graphene, PALISADE, and SGX technologies. GPS combines the scalability of homomorphic encryption with the arbitrary computational abilities of SGX, forming a more functional and efficient system for outsourced secure computations with large numbers of users. We implement GPS using linear regression training as an instantiation, and our experimental results indicate a base speedup of 1.03x to 8.69x (depending on computation parameters) over an SGX-only linear regression training without multithreading or hardware acceleration. Experiments and projections show improvements over the SGX-only training of 3.28x to 10.43x using multithreading and 4.99x to 12.67 with GPU acceleration.

  匹配依据：MPC: secure computing; TEE: sgx

  </details>

- **undeSErVed trust: Exploiting Permutation-Agnostic Remote Attestation**
  2021-06-29 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.15387)
  Luca Wilke, Jan Wichelmann, Florian Sieck, Thomas Eisenbarth

  <details><summary>摘要 / Abstract</summary>

  The ongoing trend of moving data and computation to the cloud is met with concerns regarding privacy and protection of intellectual property. Cloud Service Providers (CSP) must be fully trusted to not tamper with or disclose processed data, hampering adoption of cloud services for many sensitive or critical applications. As a result, CSPs and CPU manufacturers are rushing to find solutions for secure outsourced computation in the Cloud. While enclaves, like Intel SGX, are strongly limited in terms of throughput and size, AMD&#x27;s Secure Encrypted Virtualization (SEV) offers hardware support for transparently protecting code and data of entire VMs, thus removing the performance, memory and software adaption barriers of enclaves. Through attestation of boot code integrity and means for securely transferring secrets into an encrypted VM, CSPs are effectively removed from the list of trusted entities. There have been several attacks on the security of SEV, by abusing I/O channels to encrypt and decrypt data, or by moving encrypted code blocks at runtime. Yet, none of these attacks have targeted the attestation protocol, the core of the secure computing environment created by SEV. We show that the current attestation mechanism of Zen 1 and Zen 2 architectures has a significant flaw, allowing us to manipulate the loaded code without affecting the attestation outcome. An attacker may abuse this weakness to inject arbitrary code at startup -- and thus take control over the entire VM execution, without any indication to the VM&#x27;s owner. Our attack primitives allow the attacker to do extensive modifications to the bootloader and the operating system, like injecting spy code or extracting secret data. We present a full end-to-end attack, from the initial exploit to leaking the key of the encrypted disk image during boot, giving the attacker unthrottled access to all of the VM&#x27;s persistent data.

  匹配依据：MPC: secure computing; TEE: intel sgx, secure encrypted virtualization

  </details>

- **Cloak: Transitioning States on Legacy Blockchains Using Secure and Publicly Verifiable Off-Chain Multi-Party Computation**
  2021-06-26 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.13926)
  Qian Ren, Yingjun Wu, Han Liu, Yue Li, Anne Victor, Hong Lei, Lei Wang, Bangdao Chen

  <details><summary>摘要 / Abstract</summary>

  In recent years, the confidentiality of smart contracts has become a fundamental requirement for practical applications. While many efforts have been made to develop architectural capabilities for enforcing confidential smart contracts, a few works arise to extend confidential smart contracts to Multi-Party Computation (MPC), i.e., multiple parties jointly evaluate a transaction off-chain and commit the outputs on-chain without revealing their secret inputs/outputs to each other. However, existing solutions lack public verifiability and require O(n) transactions to enable negotiation or resist adversaries, thus suffering from inefficiency and compromised security. In this paper, we propose Cloak, a framework for enabling Multi-Party Transaction (MPT) on existing blockchains. An MPT refers to transitioning blockchain states by an publicly verifiable off-chain MPC. We identify and handle the challenges of securing MPT by harmonizing TEE and blockchain. Consequently, Cloak secures the off-chain nondeterministic negotiation process (a party joins an MPT without knowing identities or the total number of parties until the MPT proposal settles), achieves public verifiability (the public can validate that the MPT correctly handles the secret inputs/outputs from multiple parties and reads/writes states on-chain), and resists Byzantine adversaries. According to our proof, Cloak achieves better security with only 2 transactions, superior to previous works that achieve compromised security at O(n) transactions cost. By evaluating examples and real-world MPTs, the gas cost of Cloak reduces by 32.4% on average.

  匹配依据：MPC: multi party computation; TEE: tee (context)

  </details>

- **Private Signaling**
  2021-06-24 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/853)
  Varun Madathil, Alessandra Scafuro, István András Seres, Omer Shlomovits, Denis Varlakov

  <details><summary>摘要 / Abstract</summary>

  We introduce the problem of private signaling. In this problem, a sender posts a message to a certain location of a public bulletin board, and then computes a signal that allows only the intended recipient (and no one else) to learn that it is the recipient of the posted message. Besides privacy, this problem has the following crucial efficiency requirements. First, the sender and recipient do not participate in any out-of-band communication, and second, the overhead of the recipient should be asymptotically better than scanning the entire board. Existing techniques, such as the server-aided fuzzy message detection (Beck et al., CCS’21), could be employed to solve the private signaling problem. However, this solution requires that the computational effort of the recipient grows with the amount of privacy desired, providing no saving over scanning the entire board if the maximum privacy is required. In this work, we present a server-aided solution to the private signaling problem that guar- antees full privacy for all recipients, while requiring only constant amount of work for both the recipient and the sender. We provide the following contributions. First, we provide a formal definition of private signaling in the Universal Composability (UC) framework and show that it generalizes several real-world settings where recipient anonymity is desired. Second, we present two protocols that UC-realize our definition: one using a single server equipped with a trusted execution environment, and one based on two servers that employs garbled circuits. Third, we provide an open-source implementation of both of our protocols and evaluate their performance and show that they are practical.

  匹配依据：MPC: garbled circuits; TEE: trusted execution environment

  </details>

- **SSS-PRNU: Privacy-Preserving PRNU Based Camera Attribution using Shamir Secret Sharing**
  2021-06-13 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2106.07029)
  Riyanka Jena, Priyanka Singh, Manoranjan Mohanty

  <details><summary>摘要 / Abstract</summary>

  Photo Response Non-Uniformity(PRNU) noise has proven to be very effective tool in camera based forensics. It helps to match a photo to the device that clicked it. In today&#x27;s scenario, where millions and millions of images are uploaded every hour, it is very easy to compute this unique PRNU pattern from a couple of shared images on social profiles. This endangers the privacy of the camera owner and becomes a cause of major concern for the privacy-aware society. We propose SSS-PRNU scheme that facilitates the forensic investigators to carry out their crime investigation without breaching the privacy of the people. Thus, maintaining a balance between the two. To preserve privacy, extraction of camera fingerprint and PRNU noise for a suspicious image is computed in a trusted execution environment such as ARM TrustZone. After extraction, the sensitive information of camera fingerprint and PRNU noise is distributed into multiple obfuscated shares using Shamir secret sharing(SSS) scheme. These shares are information-theoretically secure and leak no information of underlying content. The encrypted information is distributed to multiple third-part servers where correlation is computed on a share basis between the camera fingerprint and the PRNU noise. These partial correlation values are combined together to obtain the final correlation value that becomes the basis for a match decision. Transforming the computation of the correlation value in the encrypted domain and making it well suited for a distributed environment is the main contribution of the paper. Experiment results validate the feasibility of the proposed scheme that provides a secure framework for PRNU based source camera attribution. The security analysis and evaluation of computational and storage overheads are performed to analysis the practical feasibility of the scheme.

  匹配依据：MPC: secret sharing; TEE: trusted execution environment, trustzone

  </details>

- **SoK: Opportunities for Software-Hardware-Security Codesign for Next Generation Secure Computing**
  2021-05-02 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2105.00378)
  Deeksha Dangwal, Meghan Cowan, Armin Alaghi, Vincent T. Lee, Brandon Reagen, Caroline Trippel

  <details><summary>摘要 / Abstract</summary>

  Users are demanding increased data security. As a result, security is rapidly becoming a first-order design constraint in next generation computing systems. Researchers and practitioners are exploring various security technologies to meet user demand such as trusted execution environments (e.g., Intel SGX, ARM TrustZone), homomorphic encryption, and differential privacy. Each technique provides some degree of security, but differs with respect to threat coverage, performance overheads, as well as implementation and deployment challenges. In this paper, we present a systemization of knowledge (SoK) on these design considerations and trade-offs using several prominent security technologies. Our study exposes the need for \textit{software-hardware-security} codesign to realize efficient and effective solutions of securing user data. In particular, we explore how design considerations across applications, hardware, and security mechanisms must be combined to overcome fundamental limitations in current technologies so that we can minimize performance overhead while achieving sufficient threat model coverage. Finally, we propose a set of guidelines to facilitate putting these secure computing technologies into practice.

  匹配依据：MPC: secure computing; TEE: intel sgx, trusted execution environments, trustzone

  </details>

- **Cryptonomial: A Framework for Private Time-Series Polynomial Calculations**
  2021-04-15 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/473)
  Ryan Karl, Jonathan Takeshita, Alamin Mohammed, Aaron Striegel, Taeho Jung

  <details><summary>摘要 / Abstract</summary>

  In modern times, data collected from multi-user distributed applications must be analyzed on a massive scale to support critical business objectives. While analytics often requires the use of personal data, it may compromise user privacy expectations if this analysis is conducted over plaintext data. Private Stream Aggregation (PSA) allows for the aggregation of time-series data, while still providing strong privacy guarantees, and is significantly more efficient over a network than related techniques (e.g. homomorphic encryption, secure multiparty computation, etc.) due to its asynchronous and efficient protocols. However, PSA protocols face limitations and can only compute basic functions, such as sum, average, etc.. We present Cryptonomial, a framework for converting any PSA scheme amenable to a complex canonical embedding into a secure computation protocol that can compute any function over time-series data that can be written as a multivariate polynomial, by combining PSA and a Trusted Execution Environment. This design allows us to compute the parallelizable sections of our protocol outside the TEE using advanced hardware, that can take better advantage of parallelism. We show that Cryptonomial inherits the security requirements of PSA, and supports fully malicious security. We simulate our scheme, and show that our techniques enable performance that is orders of magnitude faster than similar work supporting polynomial calculations.

  匹配依据：MPC: secure computation, secure multiparty computation; TEE: trusted execution environment

  </details>

- **Secure Fast Evaluation of Iterative Methods: With an Application to Secure PageRank**
  2021-03-01 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2021/207)
  Daniele Cozzo, Nigel P. Smart, Younes Talibi Alaoui

  <details><summary>摘要 / Abstract</summary>

  Iterative methods are a standard technique in many areas of scientific computing. The key idea is that a function is applied repeatedly until the resulting sequence converges to the correct answer. When applying such methods in a secure computation methodology (for example using MPC, FHE, or SGX) one either needs to perform enough steps to ensure convergence irrespective of the input data, or one needs to perform a convergence test within the algorithm, and this itself leads to a leakage of data. Using the Banach Fixed Point theorem, and its extensions, we show that this data-leakage can be quantified. We then apply this to a secure (via MPC) implementation of the PageRank methodology. For PageRank we show that allowing this small amount of data-leakage produces a much more efficient secure implementation, and that for many underlying graphs this `leakage&#x27; is already known to any attacker.

  匹配依据：MPC: secure computation; TEE: sgx

  </details>
