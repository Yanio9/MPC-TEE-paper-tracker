# 2024 · MPC + TEE · 仅预印本来源 · 第 1/1 页

[总目录](../PAPERS.md)

- **TRUST: A Toolkit for TEE-Assisted Secure Outsourced Computation over Integers**
  2024-12-02 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2412.01073)
  Bowen Zhao, Jiuhui Li, Peiming Xu, Xiaoguo Li, Qingqi Pei, Yulong Shen

  <details><summary>摘要 / Abstract</summary>

  Secure outsourced computation (SOC) provides secure computing services by taking advantage of the computation power of cloud computing and the technology of privacy computing (e.g., homomorphic encryption). Expanding computational operations on encrypted data (e.g., enabling complex calculations directly over ciphertexts) and broadening the applicability of SOC across diverse use cases remain critical yet challenging research topics in the field. Nevertheless, previous SOC solutions frequently lack the computational efficiency and adaptability required to fully meet evolving demands. To this end, in this paper, we propose a toolkit for TEE-assisted (Trusted Execution Environment) SOC over integers, named TRUST. In terms of system architecture, TRUST falls in a single TEE-equipped cloud server only through seamlessly integrating the computation of REE (Rich Execution Environment) and TEE. In consideration of TEE being difficult to permanently store data and being vulnerable to attacks, we introduce a (2, 2)-threshold homomorphic cryptosystem to fit the hybrid computation between REE and TEE. Additionally, we carefully design a suite of SOC protocols supporting unary, binary and ternary operations. To achieve applications, we present \texttt{SEAT}, secure data trading based on TRUST. Security analysis demonstrates that TRUST enables SOC, avoids collusion attacks among multiple cloud servers, and mitigates potential secret leakage risks within TEE (e.g., from side-channel attacks). Experimental evaluations indicate that TRUST outperforms the state-of-the-art and requires no alignment of data as well as any network communications. Furthermore, \texttt{SEAT} is as effective as the \texttt{Baseline} without any data protection.

  匹配依据：MPC: secure computing; TEE: trusted execution environment

  </details>

- **Physical and Software Based Fault Injection Attacks Against TEEs in Mobile Devices: A Systemisation of Knowledge**
  2024-11-22 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2411.14878)
  Aaron Joy, Ben Soh, Zhi Zhang, Sri Parameswaran, Darshana Jayasinghe

  <details><summary>摘要 / Abstract</summary>

  Trusted Execution Environments (TEEs) are critical components of modern secure computing, providing isolated zones in processors to safeguard sensitive data and execute secure operations. Despite their importance, TEEs are increasingly vulnerable to fault injection (FI) attacks, including both physical methods, such as Electromagnetic Fault Injection (EMFI), and software-based techniques. This survey examines these FI methodologies, exploring their ability to disrupt TEE operations and expose vulnerabilities in devices ranging from smartphones and IoT systems to cloud platforms. The study highlights the evolution and effectiveness of non-invasive techniques, such as EMFI, which induce faults through electromagnetic disturbances without physical modifications to hardware, making them harder to detect and mitigate. Real-world case studies illustrate the significant risks posed by these attacks, including unauthorised access, privilege escalation, and data corruption. In addition, the survey identifies gaps in existing TEE security architectures and emphasises the need for enhanced countermeasures, such as dynamic anomaly detection and updated threat models. The findings underline the importance of interdisciplinary collaboration to address these vulnerabilities, involving researchers, manufacturers, and policymakers. This survey provides actionable insights and recommendations to guide the development of more robust TEE architectures in mobile devices, fortify FI resilience, and shape global security standards. By advancing TEE security, this research aims to protect critical digital infrastructure and maintain trust in secure computing systems worldwide.

  匹配依据：MPC: secure computing; TEE: trusted execution environments

  </details>

- **Research Directions for Verifiable Crypto-Physically Secure TEEs**
  2024-10-04 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2410.03183)
  Sylvain Bellemare

  <details><summary>摘要 / Abstract</summary>

  A niche corner of the Web3 world is increasingly making use of hardware-based Trusted Execution Environments (TEEs) to build decentralized infrastructure. One of the motivations to use TEEs is to go beyond the current performance limitations of cryptography-based alternatives such as zero-knowledge proofs (ZKP), fully homomorphic encryption (FHE), and multi-party computation (MPC). Despite their appealing advantages, current TEEs suffer from serious limitations as they are not secure against physical attacks, and their attestation mechanism is rooted in the chip manufacturer&#x27;s trust. As a result, Web3 applications have to rely on cloud infrastruture to act as trusted guardians of hardware-based TEEs and have to accept to trust chip manufacturers. This work aims at exploring how we could potentially architect and implement chips that would be secure against physical attacks and would not require putting trust in chip manufacturers. One goal of this work is to motivate the Web3 movement to acknowledge and leverage the substantial amount of relevant hardware research that already exists. In brief, a combination of: (1) physical unclonable functions (PUFs) to secure the root-of-trust; (2) masking and redundancy techniques to secure computations; (3) open source hardware and imaging techniques to verify that a chip matches its expected design; can help move towards attesting that a given TEE can be trusted without the need to trust a cloud provider and a chip manufacturer.

  匹配依据：MPC: multi party computation; TEE: trusted execution environments

  </details>

- **Honest Computing: Achieving demonstrable data lineage and provenance for driving data and process-sensitive policies**
  2024-07-19 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2407.14390)
  Florian Guitton, Axel Oehmichen, Étienne Bossé, Yike Guo

  <details><summary>摘要 / Abstract</summary>

  Data is the foundation of any scientific, industrial or commercial process. Its journey typically flows from collection to transport, storage, management and processing. While best practices and regulations guide data management and protection, recent events have underscored its vulnerability. Academic research and commercial data handling have been marred by scandals, revealing the brittleness of data management. Data, despite its importance, is susceptible to undue disclosures, leaks, losses, manipulation, or fabrication. These incidents often occur without visibility or accountability, necessitating a systematic structure for safe, honest, and auditable data management. In this paper, we introduce the concept of Honest Computing as the practice and approach that emphasizes transparency, integrity, and ethical behaviour within the realm of computing and technology. It ensures that computer systems and software operate honestly and reliably without hidden agendas, biases, or unethical practices. It enables privacy and confidentiality of data and code by design and by default. We also introduce a reference framework to achieve demonstrable data lineage and provenance, contrasting it with Secure Computing, a related but differently-orientated form of computing. At its core, Honest Computing leverages Trustless Computing, Confidential Computing, Distributed Computing, Cryptography and AAA security concepts. Honest Computing opens new ways of creating technology-based processes and workflows which permit the migration of regulatory frameworks for data protection from principle-based approaches to rule-based ones. Addressing use cases in many fields, from AI model protection and ethical layering to digital currency formation for finance and banking, trading, and healthcare, this foundational layer approach can help define new standards for appropriate data custody and processing.

  匹配依据：MPC: secure computing; TEE: confidential computing

  </details>

- **Locking Machine Learning Models into Hardware**
  2024-05-31 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2405.20990)
  Eleanor Clifford, Adhithya Saravanan, Harry Langford, Cheng Zhang, Yiren Zhao, Robert Mullins, Ilia Shumailov, Jamie Hayes

  <details><summary>摘要 / Abstract</summary>

  Modern machine learning (ML) models are expensive IP and business competitiveness often depends on keeping this IP confidential. This in turn restricts how these models are deployed; for example, it is unclear how to deploy a model on-device without inevitably leaking the underlying model. At the same time, confidential computing technologies such as multi-party computation or homomorphic encryption remain impractical for wide adoption. In this paper, we take a different approach and investigate the feasibility of ML-specific mechanisms that deter unauthorized model use by restricting the model to only be usable on specific hardware, making adoption on unauthorized hardware inconvenient. That way, even if IP is compromised, it cannot be trivially used without specialised hardware or major model adjustment. In a sense, we seek to enable cheap \emph{locking of machine learning models into specific hardware}. We demonstrate that \emph{locking} mechanisms are feasible by either targeting efficiency of model representations, making such models incompatible with quantization, or tying the model&#x27;s operation to specific characteristics of hardware, such as the number of clock cycles for arithmetic operations. We demonstrate that locking comes with negligible overheads, while significantly restricting usability of the resultant model on unauthorized hardware.

  匹配依据：MPC: multi party computation; TEE: confidential computing

  </details>

- **Detecting Rogue Decryption in (Threshold) Encryption via Self-Incriminating Proofs**
  2024-05-22 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/794)
  James Hsin-yu Chiang, Bernardo David, Tore Kasper Frederiksen, Arup Mondal, Esra Yeniaras

  <details><summary>摘要 / Abstract</summary>

  Keeping decrypting parties accountable in public key encryption is notoriously hard since the secret key owner can decrypt any arbitrary ciphertext. Threshold encryption aims to solve this issue by distributing the power to decrypt among a set of parties, who must interact via a decryption protocol. However, such parties can employ cryptographic tools such as Multiparty Computation (MPC) to decrypt arbitrary ciphertexts without being detected. We introduce the notion of (threshold) encryption with Self-Incriminating Proofs, where parties must produce a self-incriminating proof of decryption when decrypting every ciphertext. In the standard public key encryption case, the adversary could destroy these proofs, so we strengthen our notion to guarantee that the proofs are published when decryption succeeds. This creates a decryption audit trail, which is useful in scenarios where decryption power is held by a single trusted party (e.g., a Trusted Execution Environment) who must be kept accountable. In the threshold case, we ensure that at least one of the parties who execute the decryption protocol will learn a self-incriminating proof, even if they employ advanced tools such as MPC. The fact that a party learns the proof and may leak it at any moment functions as a deterrent for parties who do not wish to be identified as malicious decryptors (e.g., a commercial operator of a service based on threshold encryption). We investigate the (im)possibility and applications of our notions while providing matching constructions under appropriate assumptions. In the threshold case, we build on recent results on Individual Cryptography (CRYPTO 2023).

  匹配依据：MPC: multiparty computation; TEE: trusted execution environment

  </details>

- **Hidden $\\Delta$-fairness: A Novel Notion for Fair Secure Two-Party Computation**
  2024-04-16 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/587)
  Saskia Bayreuther, Robin Berger, Felix Dörre, Jeremias Mechler, Jörn Müller-Quade

  <details><summary>摘要 / Abstract</summary>

  Secure two-party computation allows two mutually distrusting parties to compute a joint function over their inputs, guaranteeing properties such as input privacy or correctness. For many tasks, such as joint computation of statistics, it is important that when one party receives the result of the computation, the other party also receives the result. Unfortunately, this property, which is called fairness, is unattainable in the two-party setting for arbitrary functions. So weaker variants have been proposed. One such notion, proposed by Pass et al. (EUROCRYPT 2017) is called $\Delta$-fairness. Informally, it guarantees that if a corrupt party receives the output in round $r$ and stops participating in the protocol, then the honest party receives the output by round $\Delta(r)$. This notion is achieved by using so-called secure enclaves. In many settings, $\Delta$-fairness is not sufficient, because a corrupt party is guaranteed to receive its output before the honest party, giving the corrupt party an advantage in further interaction. Worse, as $\Delta$ is known to the corrupt party, it can abort the protocol when it is most advantageous. We extend the concept of $\Delta$-fairness by introducing a new fairness notion, which we call hidden $\Delta$-fairness, which addresses these problems. First of all, under our new notion, a corrupt party may not benefit from aborting, because it may not, with probability $\frac{1}{2}$, learn the result first. Moreover, $\Delta$ and other parameters are sampled according to a given distribution and remain unknown to the participants in the computation. We propose a 2PC protocol that achieves hidden $\Delta$-fairness, also using secure enclaves, and prove its security in the Generalized Universal Composability (GUC) framework.

  匹配依据：MPC: secure two party computation; TEE: secure enclaves

  </details>

- **Confidential Federated Computations**
  2024-04-16 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2404.10764)
  Hubert Eichner, Daniel Ramage, Kallista Bonawitz, Dzmitry Huba, Tiziano Santoro, Brett McLarnon, Timon Van Overveldt, Nova Fallen, Peter Kairouz, Albert Cheu, Katharine Daly, Adria Gascon, Marco Gruteser, Brendan McMahan

  <details><summary>摘要 / Abstract</summary>

  Federated Learning and Analytics (FLA) have seen widespread adoption by technology platforms for processing sensitive on-device data. However, basic FLA systems have privacy limitations: they do not necessarily require anonymization mechanisms like differential privacy (DP), and provide limited protections against a potentially malicious service provider. Adding DP to a basic FLA system currently requires either adding excessive noise to each device&#x27;s updates, or assuming an honest service provider that correctly implements the mechanism and only uses the privatized outputs. Secure multiparty computation (SMPC) -based oblivious aggregations can limit the service provider&#x27;s access to individual user updates and improve DP tradeoffs, but the tradeoffs are still suboptimal, and they suffer from scalability challenges and susceptibility to Sybil attacks. This paper introduces a novel system architecture that leverages trusted execution environments (TEEs) and open-sourcing to both ensure confidentiality of server-side computations and provide externally verifiable privacy properties, bolstering the robustness and trustworthiness of private federated computations.

  匹配依据：MPC: secure multiparty computation; TEE: trusted execution environments

  </details>

- **Two-Party Decision Tree Training from Updatable Order-Revealing Encryption**
  2024-04-11 · MPC / TEE · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2024/560)
  Robin Berger, Felix Dörre, Alexander Koch

  <details><summary>摘要 / Abstract</summary>

  Running machine learning algorithms on encrypted data is a way forward to marry functionality needs common in industry with the important concerns for privacy when working with potentially sensitive data. While there is already a growing field on this topic and a variety of protocols, mostly employing fully homomorphic encryption or performing secure multiparty computation (MPC), we are the first to propose a protocol that makes use of a specialized encryption scheme that allows to do secure comparisons on ciphertexts and update these ciphertexts to be encryptions of the same plaintexts but under a new key. We call this notion Updatable Order-Revealing Encryption (uORE) and provide a secure construction using a key-homomorphic pseudorandom function. In a second step, we use this scheme to construct an efficient three-round protocol between two parties to compute a decision tree (or forest) on labeled data provided by both parties. The protocol is in the passively-secure setting and has some leakage on the data that arises from the comparison function on the ciphertexts. We motivate how our protocol can be compiled into an actively-secure protocol with less leakage using secure enclaves, in a graceful degradation manner, e.g. falling back to the uORE leakage, if the enclave becomes fully transparent. We also analyze the leakage of this approach, giving an upper bound on the leaked information. Analyzing the performance of our protocol shows that this approach allows us to be much more efficient (especially w.r.t. the number of rounds) than current MPC-based approaches, hence allowing for an interesting trade-off between security and performance.

  匹配依据：MPC: secure multiparty computation; TEE: secure enclaves

  </details>

- **vSPACE: Voting in a Scalable, Privacy-Aware and Confidential Election**
  2024-03-08 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2403.05275)
  Se Elnour, William J Buchanan, Paul Keating, Mwrwan Abubakar, Sirag Elnour

  <details><summary>摘要 / Abstract</summary>

  The vSPACE experimental proof-of-concept (PoC) on the TrueElect[Anon][Creds] protocol presents a novel approach to secure, private, and scalable elections, extending the TrueElect and ElectAnon protocols with the integration of AnonCreds SSI (Self-Sovereign Identity). Such a protocol PoC is situated within a Zero-Trust Architecture (ZTA) and leverages confidential computing, continuous authentication, multi-party computation (MPC), and well-architected framework (WAF) principles to address the challenges of cybersecurity, privacy, and trust over IP (ToIP) protection. Employing a Kubernetes confidential cluster within an Enterprise-Scale Landing Zone (ESLZ), vSPACE integrates Distributed Ledger Technology (DLT) for immutable and certifiable audit trails. The Infrastructure as Code (IaC) model ensures rapid deployment, consistent management, and adherence to security standards, making vSPACE a future-proof solution for digital voting systems.

  匹配依据：MPC: multi party computation; TEE: confidential computing

  </details>

- **Secure Scattered Memory: Rethinking Secure Enclave Memory with Secret Sharing**
  2024-02-24 · MPC / TEE · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2402.15824)
  Haoran Geng, Yuezhi Che, Dazhao Chen, Michael Niemier, Xiaobo Sharon Hu

  <details><summary>摘要 / Abstract</summary>

  The rise of cloud computing demands secure memory systems that ensure data confidentiality, integrity, and freshness against replay attacks. Existing schemes such as AES-XTS, AES-GCM, and AES-CTR each trade performance for security, with only AES-CTR plus Message Authentication Codes (MAC) and Merkle Trees (MT) providing full protection - at the cost of substantial counter and MT overhead. This paper introduces Secure Scattered Memory (SSM), a novel scheme that replaces counter-based encryption with polynomial-based secret sharing. Each data block is encoded into multiple cryptographically independent shares distributed across memory, inherently preventing information leakage while ensuring integrity and freshness through mathematical reconstruction properties. Implemented and synthesized in a 28 nm commercial PDK, SSM occupies 0.27 mm^2 and consumes 284.53 mW. Experiments show only 10% and 8% performance overhead over AES-XTS and AES-GCM, respectively, while outperforming Morphable Counter (MICRO 2018) by up to 40%, achieving 12% better performance than EMCC/RMCC (MICRO 2022), and exceeding COSMOS (MICRO 2025) by 3%.

  匹配依据：MPC: secret sharing; TEE: secure enclave

  </details>
