# 2022 · MPC · 仅预印本来源 · 第 1/4 页

[总目录](../PAPERS.md) · [下一页](2022-mpc-preprint-02.md)

- **Asynchronous Delegated Private Set Intersection with Hiding of Intersection Size**
  2022-12-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1778)
  Wyatt Howe, Andrei Lapets, Frederick Jansen, Tanner Braun, Ben Getchell

  <details><summary>摘要 / Abstract</summary>

  Integrating private set intersection (PSI) protocols within real-world data workflows, software applications, or web services can be challenging. This can occur because data contributors and result recipients do not have the technical expertise, information technology infrastructure, or other resources to participate throughout the execution of a protocol and/or to incur all the communication costs associated with participation. Furthermore, contemporary workflows, applications, and services are often designed around RESTful APIs that might not require contributors or recipients to remain online or to maintain state. Asynchronous delegated PSI protocol variants can better match the expectations of software engineers by (1) allowing data contributors to contribute their inputs and then to depart permanently, and (2) allowing result recipients to request their result only once they are ready to do so. However, such protocols usually accomplish this by introducing an additional party that learns some information about the size of the intersection. This work presents an asynchronous delegated PSI protocol variant that does not reveal the intersection size to the additional party. It is shown that such a protocol can have, on average, linear time and space complexity.

  匹配依据：MPC: private set intersection

  </details>

- **$π$QLB: A Privacy-preserving with Integrity-assuring Query Language for Blockchain**
  2022-12-29 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2212.14141)
  Nasrin Sohrabi, Norrathep Rattanavipanon, Zahir Tari

  <details><summary>摘要 / Abstract</summary>

  The increase in the adoption of blockchain technology in different application domains e.g., healthcare systems, supplychain management, has raised the demand for a data query mechanism on blockchain. Since current blockchain systems lack the support for querying data with embedded security and privacy guarantees, there exists inherent security and privacy concerns on those systems. In particular, existing systems require users to submit queries to blockchain operators (e.g., a node validator) in plaintext. This directly jeopardizes users&#x27; privacy as the submitted queries may contain sensitive information, e.g., location or gender preferences, that the users may not be comfortable sharing. On the other hand, currently, the only way for users to ensure integrity of the query result is to maintain the entire blockchain database and perform the queries locally. Doing so incurs high storage and computational costs on the users, precluding this approach to be practically deployable on common light-weight devices (e.g., smartphones). To this end, this paper proposes $π$QLB, a query language for blockchain systems that ensures both confidentiality of query inputs and integrity of query results. Additionally, $π$QLB enables SQL-like queries over the blockchain data by introducing relational data semantics into the existing blockchain database. $π$QLB has applied the recent cryptography primitive, i.e., function secret sharing (FSS), to achieve confidentiality. To support integrity, we extend the traditional FSS setting in such a way that integrity of FSS results can be efficiently verified. Successful verification indicates absence of malicious behaviors on the servers, allowing the user to establish trust from the result. To the best of our knowledge, $π$QLB is the first query model designed for blockchain databases with support for confidentiality, integrity, and SQL-like queries.

  匹配依据：MPC: secret sharing

  </details>

- **PECO: methods to enhance the privacy of DECO protocol**
  2022-12-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1774)
  Manuel B. Santos

  <details><summary>摘要 / Abstract</summary>

  The DECentralized Oracle (DECO) protocol enables the verifiable provenance of data from Transport Layer Security (TLS) connections through secure two-party computation and zero-knowledge proofs. In this paper, we present PECO, an extension of DECO that enhances privacy features through the integration of two new private three-party handshake protocols (P3P-HS). PECO allows any web user to prove to a verifier the properties of data from TLS connections without disclosing the identity of the servers. Like DECO&#x27;s three-party handshake protocol, PECO&#x27;s P3P-HS methods do not require any changes on the server side. PECO offers two options: one that provides $k-$anonymity for the server&#x27;s identity, and another that completely masks the server&#x27;s identity from the verifier. PECO is based on three main protocols: (a) commit-and-proof zero-knowledge proofs (CP-ZKP) that enable the proof of relations under committed values in zero-knowledge, (b) verification of Elliptic Curve Digital Signature Algorithm (ECDSA) signatures under a committed public key without revealing the key (zkAttest), and (c) a proof of membership to verify that a committed key belongs to a set of keys. We estimate the performance of both P3P-HS protocols and compare it to TLS timeout using state-of-the-art implementations.

  匹配依据：MPC: secure two party computation

  </details>

- **Do Not Trust in Numbers: Practical Distributed Cryptography With General Trust**
  2022-12-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1767)
  Orestis Alpos, Christian Cachin

  <details><summary>摘要 / Abstract</summary>

  In distributed cryptography independent parties jointly perform some cryptographic task. In the last decade distributed cryptography has been receiving more attention than ever. Distributed systems power almost all applications, blockchains are becoming prominent, and, consequently, numerous practical and efﬁcient distributed cryptographic primitives are being deployed. The failure models of current distributed cryptographic systems, however, lack expressibility. Assumptions are only stated through numbers of parties, thus reducing this to threshold cryptography, where all parties are treated as identical and correlations cannot be described. Distributed cryptography does not have to be threshold-based. With general distributed cryptography the authorized sets, the sets of parties that are sufﬁcient to perform some task, can be arbitrary, and are usually modeled by the abstract notion of a general access structure. Although the necessity for general distributed cryptography has been recognized long ago and many schemes have been explored in theory, relevant practical aspects remain opaque. It is unclear how the user speciﬁes a trust structure efﬁciently or how this is encoded within a scheme, for example. More importantly, implementations and benchmarks do not exist, hence the efﬁciency of the schemes is not known. Our work ﬁlls this gap. We show how an administrator can intuitively describe the access structure as a Boolean formula. This is then converted into encodings suitable for cryptographic primitives, speciﬁcally, into a tree data structure and a monotone span program. We focus on three general distributed cryptographic schemes: veriﬁable secret sharing, common coin, and distributed signatures. For each one we give the appropriate formalization and security deﬁnition in the general-trust setting. We implement the schemes and assess their efﬁciency against their threshold counterparts. Our results suggest that the general distributed schemes can offer richer expressibility at no or insigniﬁcant extra cost. Thus, they are appropriate and ready for practical deployment.

  匹配依据：MPC: secret sharing

  </details>

- **Quantum Federated Learning for Distributed Quantum Networks**
  2022-12-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2212.12913)
  Kai Yu, Fei Gao, Song Lin

  <details><summary>摘要 / Abstract</summary>

  Federated learning is a framework that can learn from distributed networks. It attempts to build a global model based on virtual fusion data without sharing the actual data. Nevertheless, the traditional federated learning process encounters two main challenges: high computational cost and message transmission security. To address these challenges, we propose a quantum federated learning for distributed quantum networks by utilizing interesting characteristics of quantum mechanics. First, we give two methods to extract the data information to the quantum state. It can cope with different acquisition frequencies of data information. Next, a quantum gradient descent algorithm is provided to help clients in the distributed quantum networks to train local models. In other words, the algorithm gives the clients a mechanism to estimate the gradient of the local model in parallel. Compared with the classical counterpart, the proposed algorithm achieves exponential acceleration in dataset scale and quadratic speedup in data dimensionality. And, a quantum secure multi-party computation protocol is designed, which utilizes the Chinese residual theorem. It could avoid errors and overflow problems that may occur in the process of large number operation. Security analysis shows that this quantum protocol can resist common external and internal attacks. Finally, to demonstrate the effectiveness of the proposed framework, we use it to the train federated linear regression model and execute essential computation steps on the Qiskit quantum computing framework.

  匹配依据：MPC: secure multi party computation

  </details>

- **On the Impossibility of Surviving (Iterated) Deletion of Weakly Dominated Strategies in Rational MPC**
  2022-12-23 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1762)
  Johannes Blömer, Jan Bobolz, Henrik Bröcher

  <details><summary>摘要 / Abstract</summary>

  Rational multiparty computation (rational MPC) provides a framework for analyzing MPC protocols through the lens of game theory. One way to judge whether an MPC protocol is rational is through weak domination: Rational players would not adhere to an MPC protocol if deviating never decreases their utility, but sometimes increases it. Secret reconstruction protocols are of particular importance in this setting because they represent the last phase of most (rational) MPC protocols. We show that most secret reconstruction protocols from the literature are not, in fact, stable with respect to weak domination. Furthermore, we formally prove that (under certain assumptions) it is impossible to design a secret reconstruction protocol which is a Nash equlibrium but not weakly dominated if (1) shares are authenticated or (2) half of all players may form a coalition.

  匹配依据：MPC: multiparty computation

  </details>

- **Towards Secure Evaluation of Online Functionalities (Corrected and Extended Version)**
  2022-12-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1755)
  Andreas Klinger, Ulrike Meyer

  <details><summary>摘要 / Abstract</summary>

  To date, ideal functionalities securely realized with secure multi-party computation (SMPC) mainly considers functions of the private inputs of a fixed number of a priori known parties. In this paper, we generalize these definitions such that protocols implementing online algorithms in a distributed fashion can be proven to be privacy-preserving. Online algorithms compute online functionalities that allow parties to arrive and leave over time, to provide multiple inputs and to obtain multiple outputs. In particular, the set of parties participating changes over time, i.e., at different points in time different sets of parties evaluate a function over their private inputs. To this end, we propose the notion of an online trusted third party that allows to prove the security of SMPC protocols implementing online functionalities or online algorithms, respectively. We show that any online functionality can be implemented perfectly secure in the presence of a semi-honest adversary, if strictly less than 1/2 of the parties participating are corrupted. We show that the same result holds in the presence of a malicious adversary if it corrupts strictly less than 1/3 of the parties and always allows the corrupted parties to arrive and provide input. Note, this is the corrected and extended version of the work presented in [24].

  匹配依据：MPC: secure evaluation, secure multi party computation

  </details>

- **Skefl: Single-Key Homomorphic Encryption for Secure Federated Learning**
  2022-12-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2212.11394)
  Dongfang Zhao

  <details><summary>摘要 / Abstract</summary>

  Homomorphic encryption (HE) is widely adopted in untrusted environments such as federated learning. A notable limitation of conventional single-key HE schemes is the stringent security assumption regarding collusion between the parameter server and participating clients: Adversary clients are assumed not to collude with the server, as otherwise, the parameter could transmit the ciphertext of one client \(C_0\) to another client \(C_1\), who shares the same private key and could recover the local model of \(C_0\). One plausible solution to alleviate this strong assumption is multi-key HE schemes, which, unfortunately, prove impractically slow in production systems. In this work, we propose a new protocol that achieves the balance between security and performance: We extend single-key HE schemes with efficient secret sharing, ensuring that collusion between the parameter server and any compromised clients cannot reveal any local model. We term this protocol Skefl: Single-key homomorphic encryption for secure federated learning. The key idea behind Skefl is the secret-sharing of homomorphic \textit{ciphertexts} generated by multiple clients using the same pair of secret and public keys. We will substantiate the security claims of the proposed protocol using the well-known simulation framework in cryptography. Additionally, we will report on the practical performance of the Skefl protocol.

  匹配依据：MPC: secret sharing

  </details>

- **RMC-PVC: A Multi-Client Reusable Verifiable Computation Protocol (Long version)**
  2022-12-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1748)
  Pascal Lafourcade, Gael Marcadet, Léo Robert

  <details><summary>摘要 / Abstract</summary>

  The verification of computations performed by an untrusted server is a cornerstone for delegated computations, especially in multi- clients setting where inputs are provided by different parties. As- suming a common secret between clients, a garbled circuit offers the attractive property to ensure the correctness of a result computed by the untrusted server while keeping the input and the function private. Yet, this verification can be guaranteed only once. Based on the notion of multi-key homomorphic encryption (MKHE), we propose RMC-PVC a multi-client verifiable computation proto- col, able to verify the correctness of computations performed by an untrusted server for inputs (encoded for a garbled circuit) provided by multiple clients. Thanks to MKHE, the garbled circuit is reusable an arbitrary number of times. In addition, each client can verify the computation by its own. Compared to a single-key FHE scheme, the MKHE usage in RMC-PVC allows to reduce the workload of the server and thus the response delay for the client. It also enforce the privacy of inputs, which are provided by different clients.

  匹配依据：MPC: garbled circuit

  </details>

- **Duoram: A Bandwidth-Efficient Distributed ORAM for 2- and 3-Party Computation**
  2022-12-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1747)
  Adithya Vadapalli, Ryan Henry, Ian Goldberg

  <details><summary>摘要 / Abstract</summary>

  We design, analyze, and implement Duoram, a fast and bandwidth-efficient distributed ORAM protocol suitable for secure 2- and 3-party computation settings. Following Doerner and shelat&#x27;s Floram construction (CCS 2017), Duoram leverages (2,2)-distributed point functions (DPFs) to represent PIR and PIR-writing queries compactly—but with a host of innovations that yield massive asymptotic reductions in communication cost and notable speedups in practice, even for modestly sized instances. Specifically, Duoram introduces a novel method for evaluating dot products of certain secret-shared vectors using communication that is only logarithmic in the vector length. As a result, for memories with $n$ addressable locations, Duoram can perform a sequence of $m$ arbitrarily interleaved reads and writes using just $O(m\lg n)$ words of communication, compared with Floram&#x27;s $O(m \sqrt{n})$ words. Moreover, most of this work can occur during a data-independent preprocessing phase, leaving just $O(m)$ words of online communication cost for the sequence—i.e., a constant online communication cost per memory access.

  匹配依据：MPC: 3 party computation

  </details>

- **Removing the Field Size Loss from Duc et al.'s Conjectured Bound for Masked Encodings**
  2022-12-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1738)
  Julien Béguinot, Wei Cheng, Sylvain Guilley, Yi Liu, Loïc Masure, Olivier Rioul, François-Xavier Standaert

  <details><summary>摘要 / Abstract</summary>

  At Eurocrypt 2015, Duc et al. conjectured that the success rate of a side-channel attack targeting an intermediate computation encoded in a linear secret-sharing, a.k.a masking with \(d+1\) shares, could be inferred by measuring the mutual information between the leakage and each share separately. This way, security bounds can be derived without having to mount the complete attack. So far, the best proven bounds for masked encodings were nearly tight with the conjecture, up to a constant factor overhead equal to the field size, which may still give loose security guarantees compared to actual attacks. In this paper, we improve upon the state-of-the-art bounds by removing the field size loss, in the cases of Boolean masking and arithmetic masking modulo a power of two. As an example, when masking in the AES field, our new bound outperforms the former ones by a factor \(256\). Moreover, we provide theoretical hints that similar results could hold for masking in other fields as well.

  匹配依据：MPC: secret sharing

  </details>

- **Quantum Amnesia Leaves Cryptographic Mementos: A Note On Quantum Skepticism**
  2022-12-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2212.08750)
  Or Sattath, Uriel Shinar

  <details><summary>摘要 / Abstract</summary>

  Leonard Shelby, the protagonist of Memento, uses mementos in the form of tattoos and pictures to handle his amnesia. Similar to Leonard, contemporary quantum computers suffer from &quot;quantum amnesia&quot;: the inability to store quantum registers for a long duration. Quantum computers can only retain classical &quot;mementos&quot; of quantum registers by measuring them before those vanish. Some quantum skeptics argue that this quantum amnesia is inherent. We point out that this variant of a skeptic world is roughly described by the quantum bounded storage model, and although it is a computational obstacle that annuls potential quantum computational advantage, the seemingly undesired properties provide a cryptographic advantage. Namely, providing exotic primitives promised by the quantum bounded storage model, such as unconditionally secure commitment and oblivious transfer schemes, with constructions involving nothing but transmission and measurement of BB84 states.

  匹配依据：MPC: oblivious transfer

  </details>

- **New and Improved Constructions for Partially Equivocable Public Key Encryption**
  2022-12-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1733)
  Benoît Libert, Alain Passelègue, Mahshid Riahinia

  <details><summary>摘要 / Abstract</summary>

  Non-committing encryption (NCE) is an advanced form of public-key encryption which guarantees the security of a Multi-Party Computation (MPC) protocol in the presence of an adaptive adversary. Brakerski et al. (TCC 2020) recently proposed an intermediate notion, termed Packed Encryption with Partial Equivocality (PEPE), which implies NCE and preserves the ciphertext rate (up to a constant factor). In this work, we propose three new constructions of rate-1 PEPE based on standard assumptions. In particular, we obtain the first constant ciphertext-rate NCE construction from the LWE assumption with polynomial modulus, and from the Subgroup Decision assumption. We also propose an alternative DDH-based construction with guaranteed polynomial running time.

  匹配依据：MPC: multi party computation

  </details>

- **Find Thy Neighbourhood: Privacy-Preserving Local Clustering**
  2022-12-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1727)
  Pranav Shriram A, Nishat Koti, Varsha Bhat Kukkala, Arpita Patra, Bhavish Raj Gopal

  <details><summary>摘要 / Abstract</summary>

  Identifying a cluster around a seed node in a graph, termed local clustering, finds use in several applications, including fraud detection, targeted advertising, community detection, etc. However, performing local clustering is challenging when the graph is distributed among multiple data owners, which is further aggravated by the privacy concerns that arise in disclosing their view of the graph. This necessitates designing solutions for privacy-preserving local clustering and is addressed for the first time in the literature. We propose using the technique of secure multiparty computation (MPC) to achieve the same. Our local clustering algorithm is based on the heat kernel PageRank (HKPR) metric, which produces the best-known cluster quality. En route to our final solution, we have two important steps: (i) designing data-oblivious equivalent of the state-of-the-art algorithms for computing local clustering and HKPR values, and (ii) compiling the data-oblivious algorithms into its secure realisation via an MPC framework that supports operations over fixed-point arithmetic representation such as multiplication and division. Keeping efficiency in mind for large graphs, we choose the best-known honest-majority 3-party framework of SWIFT (Koti et al., USENIX&#x27;21) and enhance it with some of the necessary yet missing primitives, before using it for our purpose. We benchmark the performance of our secure protocols, and the reported run time showcases the practicality of the same. Further, we perform extensive experiments to evaluate the accuracy loss of our protocols. Compared to their cleartext counterparts, we observe that the results are comparable and thus showcase the practicality of the designed protocols.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Two-Round Concurrent 2PC from Sub-Exponential LWE**
  2022-12-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1719)
  Behzad Abdolmaleki, Saikrishna Badrinarayanan, Rex Fernando, Giulio Malavolta, Ahmadreza Rahimi, Amit Sahai

  <details><summary>摘要 / Abstract</summary>

  Secure computation is a cornerstone of modern cryptography and a rich body of research is devoted to understanding its round complexity. In this work, we consider two-party computation (2PC) protocols (where both parties receive output) that remain secure in the realistic setting where many instances of the protocol are executed in parallel (concurrent security). We obtain a two-round concurrent-secure 2PC protocol based on a single, standard, post-quantum assumption: The subexponential hardness of the learning-with-errors (LWE) problem. Our protocol is in the plain model, i.e., it has no trusted setup, and it is secure in the super-polynomial simulation framework of Pass (EUROCRYPT 2003). Since two rounds are minimal for (concurrent) 2PC, this work resolves the round complexity of concurrent 2PC from standard assumptions. As immediate applications, our work establishes feasibility results for interesting cryptographic primitives, such as the first two-round password authentication key exchange (PAKE) protocol in the plain model and the first two-round concurrent secure computation protocol for quantum circuits (2PQC).

  匹配依据：MPC: secure computation, two party computation

  </details>

- **Breaking Rate-Distance Limitation of Measurement-Device-Independent Quantum Secret Sharing**
  2022-12-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2212.06148)
  Chen-Long Li, Yao Fu, Wen-Bo Liu, Yuan-Mei Xie, Bing-Hong Li, Min-Gang Zhou, Hua-Lei Yin, Zeng-Bing Chen

  <details><summary>摘要 / Abstract</summary>

  Currently most progresses on quantum secret sharing suffer from rate-distance bound, and thus the key rates are limited. In addition to the limited key rate, the technical difficulty and the corresponding cost together prevent large-scale deployment. Furthermore, the performance of most existing protocols is analyzed in the asymptotic regime without considering participant attacks. Here we report a measurement-device-independent quantum secret sharing protocol with improved key rate and transmission distance. Based on spatial multiplexing, our protocol shows it can break rate-distance bounds over network under at least ten communication parties. Compared with other protocols, our work improves the secret key rate by more than two orders of magnitude and has a longer transmission distance. We analyze the security of our protocol in the composable framework considering participant attacks and evaluate its performance in the finite-size regime. In addition, we investigate applying our protocol to digital signatures where the signature rate is improved more than $10^7$ times compared with existing protocols. We anticipate that our quantum secret sharing protocol will provide a solid future for multiparty applications on the quantum network.

  匹配依据：MPC: secret sharing

  </details>

- **All-Photonic Quantum Repeater for Multipartite Entanglement Generation**
  2022-12-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2212.05224)
  Chen-Long Li, Yao Fu, Wen-Bo Liu, Yuan-Mei Xie, Bing-Hong Li, Min-Gang Zhou, Hua-Lei Yin, Zeng-Bing Chen

  <details><summary>摘要 / Abstract</summary>

  Quantum network applications like distributed quantum computing and quantum secret sharing present a promising future network equipped with quantum resources. Entanglement generation and distribution over long distances is critical and unavoidable to utilize quantum technology in a fully-connected network. The distribution of bipartite entanglement over long distances has seen some progresses, while the distribution of multipartite entanglement over long distances remains unsolved. Here we report a two-dimensional quantum repeater protocol for the generation of multipartite entanglement over long distances with all-photonic framework to fill this gap. The yield of the proposed protocol shows long transmission distance under various numbers of network users. With the improved efficiency and flexibility of extending the number of users, we anticipate that our protocol can work as a significant building block for quantum networks in the future.

  匹配依据：MPC: secret sharing

  </details>

- **Skellam Mixture Mechanism: a Novel Approach to Federated Learning with Differential Privacy**
  2022-12-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2212.04371)
  Ergute Bao, Yizheng Zhu, Xiaokui Xiao, Yin Yang, Beng Chin Ooi, Benjamin Hong Meng Tan, Khin Mi Mi Aung

  <details><summary>摘要 / Abstract</summary>

  Deep neural networks have strong capabilities of memorizing the underlying training data, which can be a serious privacy concern. An effective solution to this problem is to train models with differential privacy, which provides rigorous privacy guarantees by injecting random noise to the gradients. This paper focuses on the scenario where sensitive data are distributed among multiple participants, who jointly train a model through federated learning (FL), using both secure multiparty computation (MPC) to ensure the confidentiality of each gradient update, and differential privacy to avoid data leakage in the resulting model. A major challenge in this setting is that common mechanisms for enforcing DP in deep learning, which inject real-valued noise, are fundamentally incompatible with MPC, which exchanges finite-field integers among the participants. Consequently, most existing DP mechanisms require rather high noise levels, leading to poor model utility. Motivated by this, we propose Skellam mixture mechanism (SMM), an approach to enforce DP on models built via FL. Compared to existing methods, SMM eliminates the assumption that the input gradients must be integer-valued, and, thus, reduces the amount of noise injected to preserve DP. Further, SMM allows tight privacy accounting due to the nice composition and sub-sampling properties of the Skellam distribution, which are key to accurate deep learning with DP. The theoretical analysis of SMM is highly non-trivial, especially considering (i) the complicated math of differentially private deep learning in general and (ii) the fact that the mixture of two Skellam distributions is rather complex, and to our knowledge, has not been studied in the DP literature. Extensive experiments on various practical settings demonstrate that SMM consistently and significantly outperforms existing solutions in terms of the utility of the resulting model.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Encrypted machine learning of molecular quantum properties**
  2022-12-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2212.04322)
  Jan Weinreich, Guido Falk von Rudorff, O. Anatole von Lilienfeld

  <details><summary>摘要 / Abstract</summary>

  Large machine learning models with improved predictions have become widely available in the chemical sciences. Unfortunately, these models do not protect the privacy necessary within commercial settings, prohibiting the use of potentially extremely valuable data by others. Encrypting the prediction process can solve this problem by double-blind model evaluation and prohibits the extraction of training or query data. However, contemporary ML models based on fully homomorphic encryption or federated learning are either too expensive for practical use or have to trade higher speed for weaker security. We have implemented secure and computationally feasible encrypted machine learning models using oblivious transfer enabling and secure predictions of molecular quantum properties across chemical compound space. However, we find that encrypted predictions using kernel ridge regression models are a million times more expensive than without encryption. This demonstrates a dire need for a compact machine learning model architecture, including molecular representation and kernel matrix size, that minimizes model evaluation costs.

  匹配依据：MPC: oblivious transfer

  </details>

- **Automaton-Based Representations of Task Knowledge from Generative Language Models**
  2022-12-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2212.01944)
  Yunhao Yang, Jean-Raphaël Gaglione, Cyrus Neary, Ufuk Topcu

  <details><summary>摘要 / Abstract</summary>

  Automaton-based representations of task knowledge play an important role in control and planning for sequential decision-making problems. However, obtaining the high-level task knowledge required to build such automata is often difficult. Meanwhile, large-scale generative language models (GLMs) can automatically generate relevant task knowledge. However, the textual outputs from GLMs cannot be formally verified or used for sequential decision-making. We propose a novel algorithm named GLM2FSA, which constructs a finite state automaton (FSA) encoding high-level task knowledge from a brief natural-language description of the task goal. GLM2FSA first sends queries to a GLM to extract task knowledge in textual form, and then it builds an FSA to represent this text-based knowledge. The proposed algorithm thus fills the gap between natural-language task descriptions and automaton-based representations, and the constructed FSA can be formally verified against user-defined specifications. We accordingly propose a method to iteratively refine the queries to the GLM based on the outcomes, e.g., counter-examples, from verification. We demonstrate GLM2FSA&#x27;s ability to build and refine automaton-based representations of everyday tasks (e.g., crossing a road), and also of tasks that require highly-specialized knowledge (e.g., executing secure multi-party computation).

  匹配依据：MPC: secure multi party computation

  </details>

- **Powers of Tau in Asynchrony**
  2022-12-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1683)
  Sourav Das, Zhuolun Xiang, Ling Ren

  <details><summary>摘要 / Abstract</summary>

  The $q$-Strong Diffie-Hellman ($q$-SDH) parameters are foundational to efficient constructions of many cryptographic primitives such as zero-knowledge succinct non-interactive arguments of knowledge, polynomial/vector commitments, verifiable secret sharing, and randomness beacon. The only existing method to generate these parameters securely is highly sequential, requires synchrony assumptions, and has very high communication and computation costs. For example, to generate parameters for any given $q$, each party incurs a communication cost of $\Omega(nq)$ and requires $\Omega(n)$ rounds. Here $n$ is the number of parties in the secure multiparty computation protocol. Since $q$ is typically large, i.e., on the order of billions, the cost is highly prohibitive. In this paper, we present a distributed protocol to generate $q$-SDH parameters in an asynchronous network. In a network of $n$ parties, our protocol tolerates up to one-third of malicious parties. Each party incurs a communication cost of $O(q + n^2\log q)$ and the protocol finishes in $O(\log q + \log n)$ expected rounds. We provide a rigorous security analysis of our protocol. We implement our protocol and evaluate it with up to 128 geographically distributed parties. Our evaluation illustrates that our protocol is highly scalable and results in a 2-6$\times$ better runtime and 4-13$\times$ better per-party bandwidth usage compared to the state-of-the-art synchronous protocol for generating $q$-SDH parameters.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Practical Asynchronous Distributed Key Generation: Improved Efficiency, Weaker Assumption, and Standard Model**
  2022-12-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1678)
  Haibin Zhang, Sisi Duan, Chao Liu, Boxin Zhao, Xuanji Meng, Shengli Liu, Yong Yu, Fangguo Zhang, Liehuang Zhu

  <details><summary>摘要 / Abstract</summary>

  Distributed key generation (DKG) allows bootstrapping threshold cryptosystems without relying on a trusted party, nowadays enabling fully decentralized applications in blockchains and multiparty computation (MPC). While we have recently seen new advancements for asynchronous DKG (ADKG) protocols, their performance remains the bottleneck for many applications, with only one protocol being implemented (DYX+ ADKG, IEEE S&amp;P 2022). DYX+ ADKG relies on the Decisional Composite Residuosity assumption (being expensive to instantiate) and the Decisional Diffie-Hellman assumption, incurring a high latency (more than 100s with a failure threshold of 16). Moreover, the security of DYX+ ADKG is based on the random oracle model (ROM) which takes hash function as an ideal function; assuming the existence of random oracle is a strong assumption, and up to now, we cannot ﬁnd any theoretically-sound implementation. Furthermore, the ADKG protocol needs public key infrastructure (PKI) to support the trustworthiness of public keys. The strong models (ROM and PKI) further limit the applicability of DYX+ ADKG, as they would add extra and strong assumptions to underlying threshold cryptosystems. For instance, if the original threshold cryptosystem works in the standard model, then the system using DYX+ ADKG would need to use ROM and PKI. In this paper, we design and implement a modular ADKG protocol that offers improved efficiency and stronger security guarantees. We explore a novel and much more direct reduction from ADKG to the underlying blocks, reducing the computational overhead and communication rounds of ADKG in the normal case. Our protocol works for both the low-threshold and high-threshold scenarios, being secure under the standard assumption (the well-established discrete logarithm assumption only) in the standard model (no trusted setup, ROM, or PKI).

  匹配依据：MPC: multiparty computation

  </details>

- **Practical Multi-Key Homomorphic Encryption for More Flexible and Efficient Secure Federated Aggregation (preliminary work)**
  2022-12-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1674)
  Alberto Pedrouzo-Ulloa, Aymen Boudguiga, Olive Chakraborty, Renaud Sirdey, Oana Stan, Martin Zuber

  <details><summary>摘要 / Abstract</summary>

  In this work, we introduce a lightweight communication-efficient multi-key approach suitable for the Federated Averaging rule. By combining secret-key RLWE-based HE, additive secret sharing and PRFs, we reduce approximately by a half the communication cost per party when compared to the usual public-key instantiations, while keeping practical homomorphic aggregation performances. Additionally, for LWE-based instantiations, our approach reduces the communication cost per party from quadratic to linear in terms of the lattice dimension.

  匹配依据：MPC: secret sharing

  </details>

- **HashVFL: Defending Against Data Reconstruction Attacks in Vertical Federated Learning**
  2022-12-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2212.00325)
  Pengyu Qiu, Xuhong Zhang, Shouling Ji, Chong Fu, Xing Yang, Ting Wang

  <details><summary>摘要 / Abstract</summary>

  Vertical Federated Learning (VFL) is a trending collaborative machine learning model training solution. Existing industrial frameworks employ secure multi-party computation techniques such as homomorphic encryption to ensure data security and privacy. Despite these efforts, studies have revealed that data leakage remains a risk in VFL due to the correlations between intermediate representations and raw data. Neural networks can accurately capture these correlations, allowing an adversary to reconstruct the data. This emphasizes the need for continued research into securing VFL systems. Our work shows that hashing is a promising solution to counter data reconstruction attacks. The one-way nature of hashing makes it difficult for an adversary to recover data from hash codes. However, implementing hashing in VFL presents new challenges, including vanishing gradients and information loss. To address these issues, we propose HashVFL, which integrates hashing and simultaneously achieves learnability, bit balance, and consistency. Experimental results indicate that HashVFL effectively maintains task performance while defending against data reconstruction attacks. It also brings additional benefits in reducing the degree of label leakage, mitigating adversarial attacks, and detecting abnormal inputs. We hope our work will inspire further research into the potential applications of HashVFL.

  匹配依据：MPC: secure multi party computation

  </details>

- **DeV-IP: A k-out-n Decentralized and verifiable BFV for Inner Product evaluation**
  2022-12-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1673)
  Jose Contreras, Hardik Gajera

  <details><summary>摘要 / Abstract</summary>

  The biometric system has become the desired alternative to a knowledge-based authentication system. An authentication system does not provide uniqueness, as a single user can create multiple registrations with different identities for authentication. Biometric authentication identifies users based on physical traits (fingerprint, iris, face, voice), which allows the system to detect multiple authentications from the same user. The biometric templates must be encrypted or hidden to preserve users&#x27; privacy. Moreover, we need a system to perform the matching process over encrypted data without decrypting templates to preserve the users&#x27; privacy. For the euclidean distance-based matching process, centralized server-based authentication leads to possible privacy violations of biometric templates since the power of computing inner product value over any two encrypted templates allows the server to retrieve the plain biometric template by computing a few inner products. To prevent this, we considered a decentralized system called collective authority, which is a part of a public network. The collective authority computes the collective public key with contributions from all nodes in the collective authority. It also performs a matching process over encrypted biometric templates in a decentralized manner where each node performs partial matching. Then the leader of the collective authority combines it to get the final value. We further provide a lattice-based verification system for each operation. Every time a node performs some computations, it needs to provide proof of the correctness of the computation, which is publicly verifiable. We finally make the system dynamics using Shamir&#x27;s secret sharing scheme. In dynamic collective authority, only $k$ nodes out of the total $n$ nodes are required to perform the matching process. We further show that the security of the proposed system relies on the security of the underlying encryption scheme and the secret sharing scheme.

  匹配依据：MPC: secret sharing

  </details>

- **High-fidelity generation of four-photon GHZ states on-chip**
  2022-11-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.15626)
  Mathias Pont, Giacomo Corrielli, Andreas Fyrillas, Iris Agresti, Gonzalo Carvacho, Nicolas Maring, Pierre-Emmanuel Emeriau, Francesco Ceccarelli, Ricardo Albiero, Paulo H. D. Ferreira, Niccolo Somaschi, Jean Senellart, Isabelle Sagnes, Martina Morassi, Aristide Lemaitre, Pascale Senellart, Fabio Sciarrino, Marco Liscidini, Nadia Belabas, Roberto Osellame

  <details><summary>摘要 / Abstract</summary>

  Mutually entangled multi-photon states are at the heart of all-optical quantum technologies. While impressive progresses have been reported in the generation of such quantum light states using free space apparatus, high-fidelity high-rate on-chip entanglement generation is crucial for future scalability. In this work, we use a bright quantum-dot based single-photon source to demonstrate the high fidelity generation of 4-photon Greenberg-Horne-Zeilinger (GHZ) states with a low-loss reconfigurable glass photonic circuit. We reconstruct the density matrix of the generated states using full quantum-state tomography reaching an experimental fidelity to the target $|{\text{GHZ}_4}\rangle$ of $\mathcal{F}_{\text{GHZ}_4} (86.0\pm0.4)\,\%$, and a purity of $\mathcal{P}_{\text{GHZ}_4}=(76.3\pm0.6)\,\%$. The entanglement of the generated states is certified with a semi device-independent approach through the violation of a Bell-like inequality by more than 39 standard deviations. Finally, we carry out a four-partite quantum secret sharing protocol on-chip where a regulator shares with three interlocutors a sifted key with up to 1978 bits, achieving a qubit-error rate of $10.87\,\%$. These results establish that the quantum-dot technology combined with glass photonic circuitry for entanglement generation on chip offers a viable path for intermediate scale quantum computation and communication.

  匹配依据：MPC: secret sharing

  </details>

- **Breaking the Size Barrier: Universal Circuits meet Lookup Tables**
  2022-11-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1652)
  Yann Disser, Daniel Günther, Thomas Schneider, Maximilian Stillger, Arthur Wigandt, Hossein Yalame

  <details><summary>摘要 / Abstract</summary>

  A Universal Circuit (UC) is a Boolean circuit of size $\Theta(n \log n)$ that can simulate any Boolean function up to a certain size $n$. Valiant (STOC&#x27;76) provided the first two UC constructions of asymptotic sizes $\sim5 n\log n$ and $\sim4.75 n\log n$, and today&#x27;s most efficient construction of Liu et al. (CRYPTO&#x27;21) has size $\sim3n\log n$. Evaluating a public UC with a secure Multi-Party Computation (MPC) protocol allows efficient Private Function Evaluation (PFE), where a private function is evaluated on private data. Previously, most UC constructions have only been developed for circuits consisting of 2-input gates. In this work, we generalize UCs to simulate circuits consisting of ($\rho\rightarrow\omega$)-Lookup Tables (LUTs) that map $\rho$ input bits to $\omega$ output bits. Our LUT-based UC (LUC) construction has an asymptotic size of $1.5\rho\omega n \log \omega n$ and improves the size of the UC over the best previous UC construction of Liu et al. (CRYPTO&#x27;21) by factors 1.12$\times$ - $2.18\times$ for common functions. Our results show that the greatest size improvement is achieved for $\rho=3$ inputs, and it decreases for $\rho&gt;3$. Furthermore, we introduce Varying Universal Circuits (VUCs), which reduce circuit size at the expense of leaking the number of inputs $\rho$ and outputs $\omega$ of each LUT. Our benchmarks demonstrate that VUCs can improve over the size of the LUC construction by a factor of up to $1.45\times$.

  匹配依据：MPC: secure multi party computation

  </details>

- **The Return of the SDitH**
  2022-11-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1645)
  Carlos Aguilar-Melchor, Nicolas Gama, James Howe, Andreas Hülsing, David Joseph, Dongze Yue

  <details><summary>摘要 / Abstract</summary>

  This paper presents a code-based signature scheme based on the well-known syndrome decoding (SD) problem. The scheme builds upon a recent line of research which uses the Multi-Party-Computation-in-the-Head (MPCitH) approach to construct efficient zero-knowledge proofs, such as Syndrome Decoding in the Head (SDitH), and builds signature schemes from them using the Fiat-Shamir transform. At the heart of our proposal is a new approach, Hypercube-MPCitH, to amplify the soundness of any MPC protocol that uses additive secret sharing. An MPCitH protocol with $N$ parties can be repeated $D$ times using parallel composition to reach the same soundness as a protocol run with $N^D$ parties. However, the former comes with $D$ times higher communication costs, often mainly contributed by the usage of $D$ `auxiliary&#x27; states (which in general have a significantly bigger impact on size than random states). Instead of that, we begin by generating $N^D$ shares, arranged into a $D$-dimensional hypercube of side $N$ containing only one `auxiliary&#x27; state. We derive from this hypercube $D$ sharings of size $N$ which are used to run $D$ instances of an $N$ party MPC protocol. Hypercube-MPCitH leads to a protocol with $1/N^D$ soundness error, requiring $N^D$ offline computation, but with only $N\cdot D$ online computation, and only $1$ `auxiliary&#x27;. As the (potentially offline) share generation phase is generally inexpensive, this leads to trade-offs that are superior to just using parallel composition. Our novel method of share generation and aggregation not only improves certain MPCitH protocols in general but also shows in concrete improvements of signature schemes. Specifically, we apply it to the work of Feneuil, Joux, and Rivain (CRYPTO&#x27;22) on code-based signatures, and obtain a new signature scheme that achieves a 8.1x improvement in global runtime and a 30x improvement in online runtime for their shortest signatures size (8,481 Bytes). It is also possible to leverage the fact that most computations are offline to define parameter sets leading to smaller signatures: 6,784 Bytes for 26 ms offline and 5,689 Bytes for 320 ms offline. For NIST security level 1, online signature cost is around 3 million cycles ($&lt;$1 ms on commodity processors), regardless of signature size.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **MPCViT: Searching for Accurate and Efficient MPC-Friendly Vision Transformer with Heterogeneous Attention**
  2022-11-25 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.13955) · [Code](https://github.com/PKU-SEC-Lab/mpcvit)
  Wenxuan Zeng, Meng Li, Wenjie Xiong, Tong Tong, Wen-jie Lu, Jin Tan, Runsheng Wang, Ru Huang

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation (MPC) enables computation directly on encrypted data and protects both data and model privacy in deep learning inference. However, existing neural network architectures, including Vision Transformers (ViTs), are not designed or optimized for MPC and incur significant latency overhead. We observe Softmax accounts for the major latency bottleneck due to a high communication complexity, but can be selectively replaced or linearized without compromising the model accuracy. Hence, in this paper, we propose an MPC-friendly ViT, dubbed MPCViT, to enable accurate yet efficient ViT inference in MPC. Based on a systematic latency and accuracy evaluation of the Softmax attention and other attention variants, we propose a heterogeneous attention optimization space. We also develop a simple yet effective MPC-aware neural architecture search algorithm for fast Pareto optimization. To further boost the inference efficiency, we propose MPCViT+, to jointly optimize the Softmax attention and other network components, including GeLU, matrix multiplication, etc. With extensive experiments, we demonstrate that MPCViT achieves 1.9%, 1.3% and 3.6% higher accuracy with 6.2x, 2.9x and 1.9x latency reduction compared with baseline ViT, MPCFormer and THE-X on the Tiny-ImageNet dataset, respectively. MPCViT+ further achieves a better Pareto front compared with MPCViT. The code and models for evaluation are available at https://github.com/PKU-SEC-Lab/mpcvit.

  匹配依据：MPC: secure multi party computation

  </details>

- **Efficient Threshold FHE for Privacy-Preserving Applications**
  2022-11-22 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1625)
  Siddhartha Chowdhury, Sayani Sinha, Animesh Singh, Shubham Mishra, Chandan Chaudhary, Sikhar Patranabis, Pratyay Mukherjee, Ayantika Chatterjee, Debdeep Mukhopadhyay

  <details><summary>摘要 / Abstract</summary>

  Threshold Fully Homomorphic Encryption (ThFHE) enables arbitrary computation over encrypted data while keeping the decryption key distributed across multiple parties at all times. ThFHE is a key enabler for threshold cryptography and, more generally, secure distributed computing. Existing ThFHE schemes relying on standard hardness assumptions, inherently require highly inefficient parameters and are unsuitable for practical deployment. In this paper, we take a novel approach towards making ThFHE practically usable by (i) proposing an efficient ThFHE scheme with a new analysis resulting in significantly improved parameters; (ii) and providing the first practical ThFHE implementation benchmark based on Torus FHE. • We propose the first practical ThFHE scheme with a polynomial modulus-to-noise ratio that supports practically efficient parameters while retaining provable security based on standard quantum-safe assumptions. We achieve this via R ́enyi divergence-based security analysis of our proposed threshold decryption mechanism. • We present a prototype software implementation of our proposed ThFHE scheme that builds upon the existing Torus-FHE library and supports (distributed) decryption on highly resource-constrained ARM-based handheld devices. Along the way, we implement several extensions to the Torus FHE library, including a Torus-based linear integer secret sharing subroutine to support ThFHE key sharing and distributed decryption for any threshold access structure. We illustrate the efficacy of our proposal via an end-to-end use case involving encrypted computations over a real medical database and distributed decryptions of the computed result on resource-constrained ARM-based handheld devices.

  匹配依据：MPC: secret sharing

  </details>

- **Secret Sharing for Generic Access Structures**
  2022-11-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1616)
  James Smith

  <details><summary>摘要 / Abstract</summary>

  Sharing a secret efficiently amongst a group of participants is not easy since there is always an adversary / eavesdropper trying to retrieve the secret. In secret sharing schemes, every participant is given a unique share. When the desired group of participants come together and provide their shares, the secret is obtained. For other combinations of shares, a garbage value is returned. A threshold secret sharing scheme was proposed by Shamir and Blakeley independently. In this (n,t) threshold secret sharing scheme, the secret can be obtained when at least $t$ out of $n$ participants contribute their shares. This paper proposes a novel algorithm to reveal the secret only to the subsets of participants belonging to the access structure. This scheme implements totally generalized ideal secret sharing. Unlike threshold secret sharing schemes, this scheme reveals the secret only to the authorized sets of participants, not any arbitrary set of users with cardinality more than or equal to $t$. Since any access structure can be realized with this scheme, this scheme can be exploited to implement various access priorities and access control mechanisms. A major advantage of this scheme over the existing ones is that the shares being distributed to the participants is totally independent of the secret being shared. Hence, no restrictions are imposed on the scheme and it finds a wider use in real world applications.

  匹配依据：MPC: secret sharing

  </details>

- **Efficient Methods for Implementation of Generalized Access Structures**
  2022-11-20 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1615)
  James Smith

  <details><summary>摘要 / Abstract</summary>

  The recent advent of cloud computing and IoT has made it imperative to store huge amount of data in the cloud servers. Enormous amount of data is also stored in the servers of big organizations. In organizations, it is not desirable for every member to have equal privileges to access the stored data. Threshold secret sharing schemes are widely used for implementing such access control mechanisms. The access privileges of the members also vary from one data packet to another. While implementing such dynamic access structures using threshold secret sharing schemes, the key management becomes too complex to be implemented in real time. Furthermore, the storage of the users’ access privileges requires exponential space (O($2^n$)) and its implementation requires exponential time. In this paper, the algorithms proposed to tackle the problems of priority based access control and authentication require a space complexity of O($n^2$) and a time complexity of O($n$), where n is the number of users. In the practical scenario, such space can easily be provided on the servers and the algorithms can run smoothly in real time.

  匹配依据：MPC: secret sharing

  </details>

- **Ligero: Lightweight Sublinear Arguments Without a Trusted Setup**
  2022-11-18 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1608)
  Scott Ames, Carmit Hazay, Yuval Ishai, Muthuramakrishnan Venkitasubramaniam

  <details><summary>摘要 / Abstract</summary>

  We design and implement a simple zero-knowledge argument protocol for $\mathsf{NP}$ whose communication complexity is proportional to the square-root of the verification circuit size. The protocol can be based on any collision-resistant hash function. Alternatively, it can be made non-interactive in the random oracle model, yielding concretely efficient zk-SNARKs that do not require a trusted setup or public-key cryptography. Our protocol is obtained by applying an optimized version of the general transformation of Ishai et al. (STOC 2007) to a variant of the protocol for secure multiparty computation of Damg$\mathring{a}$rd and Ishai (CRYPTO 2006). It can be viewed as a simple zero-knowledge interactive PCP based on ``interleaved&#x27;&#x27; Reed-Solomon codes. This paper is an extended version of the paper published in CCS 2017 and features a tighter analysis, better implementation along with formal proofs. For large verification circuits, the Ligero prover remains competitive against subsequent works with respect to the prover’s running time, where our efficiency advantages become even bigger in an amortized setting, where several instances need to be proven simultaneously. Our protocol is attractive not only for very large verification circuits but also for moderately large circuits that arise in applications. For instance, for verifying a SHA-256 preimage with $2^{-40}$ soundness error, the communication complexity is roughly 35KB. The communication complexity of our protocol is independent of the circuit structure and depends only on the number of gates. For $2^{-40}$ soundness error, the communication becomes smaller than the circuit size for circuits containing roughly 3 million gates or more. With our refined analysis the Ligero system&#x27;s proof lengths and prover&#x27;s running times are better than subsequent post-quantum ZK-SNARKs for small to moderately large circuits.

  匹配依据：MPC: secure multiparty computation

  </details>

- **SFPDML: Securer and Faster Privacy-Preserving Distributed Machine Learning based on MKTFHE**
  2022-11-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.09353)
  Hongxiao Wang, Zoe L. Jiang, Yanmin Zhao, Siu-Ming Yiu, Peng Yang, Man Chen, Zejiu Tan, Bohan Jin

  <details><summary>摘要 / Abstract</summary>

  In recent years, distributed machine learning has garnered significant attention. However, privacy continues to be an unresolved issue within this field. Multi-key homomorphic encryption over torus (MKTFHE) is one of the promising candidates for addressing this concern. Nevertheless, there may be security risks in the decryption of MKTFHE. Moreover, to our best known, the latest works about MKTFHE only support Boolean operation and linear operation which cannot directly compute the non-linear function like Sigmoid. Therefore, it is still hard to perform common machine learning such as logistic regression and neural networks in high performance. In this paper, we first discover a possible attack on the existing distributed decryption protocol for MKTFHE and subsequently introduce secret sharing to propose a securer one. Next, we design a new MKTFHE-friendly activation function via \emph{homogenizer} and \emph{compare quads}. Finally, we utilize them to implement logistic regression and neural network training in MKTFHE. Comparing the efficiency and accuracy between using Taylor polynomials of Sigmoid and our proposed function as an activation function, the experiments show that the efficiency of our function is 10 times higher than using 7-order Taylor polynomials straightly and the accuracy of the training model is similar to using a high-order polynomial as an activation function scheme.

  匹配依据：MPC: secret sharing

  </details>

- **AUC: Accountable Universal Composability**
  2022-11-17 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1606)
  Mike Graf, Ralf Küsters, Daniel Rausch

  <details><summary>摘要 / Abstract</summary>

  Accountability is a well-established and widely used security concept that allows for obtaining undeniable cryptographic proof of misbehavior, thereby incentivizing honest behavior. There already exist several general purpose accountability frameworks for formal game-based security analyses. Unfortunately, such game-based frameworks do not support modular security analyses, which is an important tool to handle the complexity of modern protocols. Universal composability (UC) models provide native support for modular analyses, including re-use and composition of security results. So far, accountability has mainly been modeled and analyzed in UC models for the special case of MPC protocols, with a general purpose accountability framework for UC still missing. That is, a framework that among others supports arbitrary protocols, a wide range of accountability properties, handling and mixing of accountable and non-accountable security properties, and modular analysis of accountable protocols. To close this gap, we propose AUC, the first general purpose accountability framework for UC models, which supports all of the above, based on several new concepts. We exemplify AUC in three case studies not covered by existing works. In particular, AUC unifies existing UC accountability approaches within a single framework.

  匹配依据：MPC: mpc (context)

  </details>

- **Secret-Shared Joins with Multiplicity from Aggregation Trees**
  2022-11-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1600)
  Saikrishna Badrinarayanan, Sourav Das, Gayathri Garimella, Srinivasan Raghuraman, Peter Rindal

  <details><summary>摘要 / Abstract</summary>

  We present novel protocols to compute SQL-like join operations on secret shared database tables with non-unique join keys. Previous approaches to the problem had the restriction that the join keys of both the input tables must be unique or had quadratic overhead. Our work lifts this restriction, allowing one or both of the secret shared input tables to have an unknown and unbounded number of repeating join keys while achieving efficient $O(n\log n)$ asymptotic communication/computation and $O(\log n)$ rounds of interaction, independent of the multiplicity of the keys. We present two join protocols, \ProtoUni and \ProtoDup. The first, \ProtoUni is optimized for the case where one table has a unique primary key while the second, \ProtoDup is for the more general setting where both tables contain duplicate keys. Both protocols require $O(n \log n)$ time and $O(\log n)$ rounds to join two tables of size $n$. Our framework for computing joins requires an efficient sorting protocol and generic secure computation for circuits. We concretely instantiate our protocols in the honest majority three-party setting. Our join protocols are built around an efficient method to compute structured aggregations over a secret shared input vector $\V\in \mathbb{D}^n$. If the parties have another secret-shared vector of control bits $\B \in \{0, 1\}^n$ to partition $\V$ into sub-vectors (that semantically relates to the join operations). A structured aggregation computes a secret shared vector $\V&#x27;\in \mathbb{D}^n$ where every sub-vector $(\V_b,...,\V_e)$ (defined by the control bits) is aggregated as $\V_i&#x27;=\V_b\op...\op \V_i$ for $i\in \{b,...,e\}$ according to some user-defined operator $\op$. Critically, the $b,e$ indices that partition the vector are secret. It&#x27;s trivial to compute aggregations by sequentially processing the input vector and control bits. This would require $O(n)$ rounds and would be very slow due to network latency. We introduce Aggregation Trees as a general technique to compute aggregations in $O(\log n)$ rounds. For our purpose of computing joins, we instantiate $\op \in$ \textsf{\{copy previous value, add\}}, but we believe that this technique is quite powerful and can find applications in other useful settings.

  匹配依据：MPC: secure computation

  </details>

- **Efficient Secure Three-Party Sorting with Applications to Data Analysis and Heavy Hitters**
  2022-11-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1595)
  Gilad Asharov, Koki Hamada, Dai Ikarashi, Ryo Kikuchi, Ariel Nof, Benny Pinkas, Katsumi Takahashi, Junichi Tomida

  <details><summary>摘要 / Abstract</summary>

  We present a three-party sorting protocol secure against passive and active adversaries in the honest majority setting. The protocol can be easily combined with other secure protocols which work on shared data, and thus enable different data analysis tasks, such as private set intersection of shared data, deduplication, and the identification of heavy hitters. The new protocol computes a stable sort. It is based on radix sort and is asymptotically better than previous secure sorting protocols. It improves on previous radix sort protocols by not having to shuffle the entire length of the items after each comparison step. We implemented our sorting protocol with different optimizations and achieved concretely fast performance. For example, sorting one million items with 32-bit keys and 32-bit values takes less than 2 seconds with semi-honest security and about 3.5 seconds with malicious security. Finding the heavy hitters among hundreds of thousands of 256-bit values takes only a few seconds, compared to close to an hour in previous work.

  匹配依据：MPC: private set intersection

  </details>

- **Practical Asynchronous Proactive Secret Sharing and Key Refresh**
  2022-11-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1586)
  Christoph U. Günther, Sourav Das, Lefteris Kokoris-Kogias

  <details><summary>摘要 / Abstract</summary>

  With the emergence of decentralized systems, spearheaded by blockchains, threshold cryptography has seen unprecedented adoption. Just recently, the trustless distribution of threshold keys over an unreliable network has started to become practical. The next logical step is ensuring the security of these keys against persistent adversaries attacking the system over long periods of time. In this work, we tackle this problem and give two practical constructions for Asynchronous Proactive Secret Sharing. Our first construction uses recent advances in asynchronous protocols and achieves a communication complexity of $O(n^3)$ where $n$ is the total number of nodes in the network. The second protocol builds upon the first and uses sortition to drive down the communication complexity to $O(c n^2)$. Here, $c$ is a tunable parameter that controls the expected size of the sharing committee chosen using the existing random coin. Additionally, we identify security flaws in prior work and ensure that our protocols are secure by giving rigorous proofs. Moreover, we introduce a related notion which we term Asynchronous Refreshable Secret Sharing — a functionality that also re-randomizes the secret itself. Finally, we demonstrate the practicability of our constructions by implementing them in Rust and running large-scale, geo-distributed benchmarks.

  匹配依据：MPC: secret sharing

  </details>

- **Attribute-based Anonymous Credential: Optimization for Single-Use and Multi-Use**
  2022-11-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1585)
  Kwan Yin Chan, Tsz Hon Yuen

  <details><summary>摘要 / Abstract</summary>

  User attributes can be authenticated by an attribute-based anonymous credential while keeping the anonymity of the user. Most attribute-based anonymous credential schemes are designed specifically for either multi-use or single-use. In this paper, we propose a unified attribute-based anonymous credential system, in which users always obtain the same format of credential from the issuer. The user can choose to use it for an efficient multi-use or single-use show proof. It is a more user-centric approach than the existing schemes. Technically, we propose an interactive approach to the credential issuance protocol using a two-party computation with an additive homomorphic encryption. At the same time, it keeps the security property of impersonation resilience, anonymity, and unlinkability. Apart from the interactive protocol, we further design the show proofs for efficient single-use credentials which maintain the user anonymity.

  匹配依据：MPC: two party computation

  </details>

- **Weighted Secret Sharing from Wiretap Channels**
  2022-11-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1578)
  Fabrice Benhamouda, Shai Halevi, Lev Stambler

  <details><summary>摘要 / Abstract</summary>

  Secret-sharing allows splitting a piece of secret information among a group of shareholders, so that it takes a large enough subset of them to recover it. In \emph{weighted} secret-sharing, each shareholder has an integer weight, and it takes a subset of large-enough weight to recover the secret. Schemes in the literature for weighted threshold secret sharing either have share sizes that grow linearly with the total weight, or ones that depend on huge public information (essentially a garbled circuit) of size (quasi)polynomial in the number of parties. To do better, we investigate a relaxation, $(\alpha, \beta)$-ramp weighted secret sharing, where subsets of weight $\beta W$ can recover the secret (with $W$ the total weight), but subsets of weight $\alpha W$ or less cannot learn anything about it. These can be constructed from standard secret-sharing schemes, but known constructions require long shares even for short secrets, achieving share sizes of $\max\big(W,\frac{|\mathrm{secret}|}{\epsilon}\big)$, where $\epsilon=\beta-\alpha$. In this note we first observe that simple rounding let us replace the total weight $W$ by $N/\epsilon$, where $N$ is the number of parties. Combined with known constructions, this yields share sizes of $O\big(\max(N,|\mathrm{secret}|)/{\epsilon}\big)$. Our main contribution is a novel connection between weighted secret sharing and wiretap channels, that improves or even eliminates the dependence on~$N$, at a price of increased dependence on $1/\epsilon$. We observe that for certain additive-noise $(R,A)$ wiretap channels, any semantically secure scheme can be naturally transformed into an $(\alpha,\beta)$-ramp weighted secret-sharing, where $\alpha,\beta$ are essentially the respective capacities of the channels $A,R$. We present two instantiations of this type of construction, one using Binary Symmetric wiretap Channels, and the other using additive Gaussian Wiretap Channels. Depending on the parameters of the underlying wiretap channels, this gives rise to $(\alpha, \beta)$-ramp schemes with share sizes $|\mathrm{secret}|/\mathrm{poly}(\epsilon\log N)$ or even just $|\mathrm{secret}|/\mathrm{poly}(\epsilon)$.

  匹配依据：MPC: garbled circuit, secret sharing

  </details>

- **Asynchronous Multi-Party Quantum Computation**
  2022-11-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1583)
  Vipul Goyal, Chen-Da Liu-Zhang, Justin Raizes, João Ribeiro

  <details><summary>摘要 / Abstract</summary>

  Multi-party quantum computation (MPQC) allows a set of parties to securely compute a quantum circuit over private quantum data. Current MPQC protocols rely on the fact that the network is synchronous, i.e., messages sent are guaranteed to be delivered within a known fixed delay upper bound, and unfortunately completely break down even when only a single message arrives late. Motivated by real-world networks, the seminal work of Ben-Or, Canetti and Goldreich (STOC&#x27;93) initiated the study of multi-party computation for classical circuits over asynchronous networks, where the network delay can be arbitrary. In this work, we begin the study of asynchronous multi-party quantum computation (AMPQC) protocols, where the circuit to compute is quantum. Our results completely characterize the optimal achievable corruption threshold: we present an $n$-party AMPQC protocol secure up to $t&lt;n/4$ corruptions, and an impossibility result when $t\geq n/4$ parties are corrupted. Remarkably, this characterization differs from the analogous classical setting, where the optimal corruption threshold is $t&lt;n/3$.

  匹配依据：MPC: multi party computation

  </details>

- **Concatenating Extended CSS Codes for Communication Efficient Quantum Secret Sharing**
  2022-11-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.06910)
  Kaushik Senthoor, Pradeep Kiran Sarvepalli

  <details><summary>摘要 / Abstract</summary>

  Recently, a class of quantum secret sharing schemes called communication efficient quantum threshold secret sharing schemes (CE-QTS) was introduced. These schemes reduced the communication cost during secret recovery. In this paper, we introduce a general class of communication efficient quantum secret sharing schemes (CE-QSS) which include both threshold and non-threshold schemes. We propose a framework for constructing CE-QSS schemes to generalize the earlier construction of CE-QTS schemes which was based on the staircase codes. The main component in this framework is a class of quantum codes which we call the extended Calderbank-Shor-Steane codes. These extended CSS codes could have other applications. We derive a bound on communication cost for CE-QSS schemes. Finally, we provide a construction of CE-QSS schemes meeting this bound using the proposed framework.

  匹配依据：MPC: secret sharing

  </details>

- **Comprehension from Chaos: Towards Informed Consent for Private Computation**
  2022-11-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.07026)
  Bailey Kacsmar, Vasisht Duddu, Kyle Tilbury, Blase Ur, Florian Kerschbaum

  <details><summary>摘要 / Abstract</summary>

  Private computation, which includes techniques like multi-party computation and private query execution, holds great promise for enabling organizations to analyze data they and their partners hold while maintaining data subjects&#x27; privacy. Despite recent interest in communicating about differential privacy, end users&#x27; perspectives on private computation have not previously been studied. To fill this gap, we conducted 22 semi-structured interviews investigating users&#x27; understanding of, and expectations for, private computation over data about them. Interviews centered on four concrete data-analysis scenarios (e.g., ad conversion analysis), each with a variant that did not use private computation and another that did (private set intersection, multi-party computation, and privacy preserving query procedures). While participants struggled with abstract definitions of private computation, they found the concrete scenarios enlightening and plausible even though we did not explain the complex cryptographic underpinnings. Private computation increased participants&#x27; acceptance of data sharing, but not unconditionally; the purpose of data sharing and analysis was the primary driver of their attitudes. Through collective activities, participants emphasized the importance of detailing the purpose of a computation and clarifying that inputs to private computation are not shared across organizations when describing private computation to end users.

  匹配依据：MPC: multi party computation, private set intersection

  </details>

- **Distributed and secure linear algebra -- Master Thesis**
  2022-11-12 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.06732)
  Hugo Mirault

  <details><summary>摘要 / Abstract</summary>

  Cryptography is the discipline that allows securing of the exchange of information. In this internship, we will focus on a certain branch of this discipline, secure computation in a network. The main goal of this internship, illustrated in this report, is to adapt a roster of protocols intended to do linear algebra. We want to adapt them to do algebra for matrices with polynomial coefficients. We then wish to make a complete analysis of the different complexities of these protocols.

  匹配依据：MPC: secure computation

  </details>

- **Black-Hole Radiation Decoding is Quantum Cryptography**
  2022-11-10 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.05491)
  Zvika Brakerski

  <details><summary>摘要 / Abstract</summary>

  We propose to study equivalence relations between phenomena in high-energy physics and the existence of standard cryptographic primitives, and show the first example where such an equivalence holds. A small number of prior works showed that high-energy phenomena can be explained by cryptographic hardness. Examples include using the existence of one-way functions to explain the hardness of decoding black-hole Hawking radiation (Harlow and Hayden 2013, Aaronson 2016), and using pseudorandom quantum states to explain the hardness of computing AdS/CFT dictionary (Bouland, Fefferman and Vazirani, 2020). In this work we show, for the former example of black-hole radiation decoding, that it also implies the existence of secure quantum cryptography. In fact, we show an existential equivalence between the hardness of black-hole radiation decoding and a variety of cryptographic primitives, including bit-commitment schemes and oblivious transfer protocols (using quantum communication). This can be viewed (with proper disclaimers, as we discuss) as providing a physical justification for the existence of secure cryptography. We conjecture that such connections may be found in other high-energy physics phenomena.

  匹配依据：MPC: oblivious transfer

  </details>

- **Several classes of projective few-weight linear codes and their applications**
  2022-11-08 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.04519)
  Canze Zhu, Qunying Liao

  <details><summary>摘要 / Abstract</summary>

  It is well-known that few-weight linear codes have better applications in secret sharing schemes \cite{JY2006,CC2005}.In particular, projective two-weight codes are very precious as they are closely related to finite projective spaces, strongly regular graphs and combinatorial designs \cite{RC1986,CD2018,P1972}. Here, we present the following two applications.

  匹配依据：MPC: secret sharing

  </details>

- **Extensible Decentralized Secret Sharing and Application to Schnorr Signatures**
  2022-11-08 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1551)
  Michele Battagliola, Riccardo Longo, Alessio Meneghetti

  <details><summary>摘要 / Abstract</summary>

  Starting from links between coding theory and secret sharing we develop an extensible and decentralized version of Shamir Secret Sharing, that allows the addition of new users after the initial share distribution. On top of it we design a totally decentralized $(t,n)$-threshold Schnorr signature scheme that needs only $t$ users online during the key generation phase, while the others join later. Under standard assumptions we prove our scheme secure against adaptive malicious adversaries. Furthermore, we show how our security notion can be strengthen when considering a rushing adversary. Using a classical game-based argument, we prove that if there is an adversary capable of forging the scheme with non-negligible probability, then we can build a forger for the centralized Schnorr scheme with non-negligible probability.

  匹配依据：MPC: secret sharing

  </details>

- **Two-Server Oblivious Transfer for Quantum Messages**
  2022-11-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.03308)
  Masahito Hayashi, Seunghoan Song

  <details><summary>摘要 / Abstract</summary>

  Oblivious transfer is considered as a cryptographic primitive task for quantum information processing over quantum network. Although it is possible with two servers, any existing protocol works only with classical messages. We propose two-server oblivious transfer protocols for quantum messages.

  匹配依据：MPC: oblivious transfer

  </details>

- **Secure Auctions in the Presence of Rational Adversaries**
  2022-11-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1541)
  Chaya Ganesh, Bhavana Kanukurthi, Girisha Shankar

  <details><summary>摘要 / Abstract</summary>

  Sealed bid auctions are used to allocate a resource among a set of interested parties. Traditionally, auctions need the presence of a trusted auctioneer to whom the bidders provide their private bid values. Existence of such a trusted party is not an assumption easily realized in practice. Generic secure computation protocols can be used to remove a trusted party. However, generic techniques result in inefficient protocols, and typically do not provide fairness - that is, a corrupt party can learn the output and abort the protocol thereby preventing other parties from learning the output. At CRYPTO 2009, Miltersen, Nielsen and Triandopoulos [MNT09], introduced the problem of building auctions that are secure against rational bidders. Such parties are modeled as self-interested agents who care more about maximizing their utility than about learning information about bids of other agents. To realize this, they put forth a novel notion of information utility and introduce a game-theoretic framework that helps analyse protocols while taking into account both information utility as well as monetary utility. Unfortunately, their construction makes use a of generic MPC protocol and, consequently, the authors do not analyze the concrete efficiency of their protocol. In this work, we construct the first concretely efficient and provably secure protocol for First Price Auctions in the rational setting. Our protocol guarantees privacy and fairness. Inspired by [MNT09], we put forth a solution concept that we call Privacy Enhanced Computational Weakly Dominant Strategy Equilibrium that captures parties&#x27; privacy and monetary concerns in the game theoretic context, and show that our protocol realizes this. We believe this notion to be of independent interest. Our protocol is crafted specifically for the use case of auctions, is simple, using off-the-shelf cryptographic components. Executing our auction protocol on commodity hardware with 10 bidders, with bids of length 10, our protocol runs to completion in 0.141s and has total communication of 30KB.

  匹配依据：MPC: secure computation

  </details>

- **Four-Round Black-Box Non-Malleable Commitments from One-Way Permutations**
  2022-11-07 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1543)
  Michele Ciampi, Emmanuela Orsini, Luisa Siniscalchi

  <details><summary>摘要 / Abstract</summary>

  We construct the first four-round non-malleable commitment scheme based solely on the black-box use of one-to-one one-way functions. Prior to our work, all non-malleable commitment schemes based on black-box use of polynomial-time cryptographic primitives require more than $16$ rounds of interaction. A key tool for our construction is a proof system that satisfies a new definition of security that we call non-malleable zero-knowledge with respect to commitments. In a nutshell, such a proof system can be safely run in parallel with a (potentially interactive) commitment scheme. We provide an instantiation of this tool using the MPC-in-the-Head approach in combination with BMR.

  匹配依据：MPC: mpc (context)

  </details>

- **Privacy-Preserving Blueprints**
  2022-11-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1536)
  Markulf Kohlweiss, Anna Lysyanskaya, An Nguyen

  <details><summary>摘要 / Abstract</summary>

  In a world where everyone uses anonymous credentials for all access control needs, it is impossible to trace wrongdoers, by design. This makes legitimate controls, such as tracing illicit trade and terror suspects, impossible to carry out. Here, we propose a privacy-preserving blueprint capability that allows an auditor to publish an encoding $pk_A$ of the function $f(x,\cdot)$ for a publicly known function $f$ and a secret input $x$. For example, $x$ may be a secret watchlist, and $f(x,y)$ may return $y$ if $y\in x$. On input her data $y$ and the auditor&#x27;s $pk_A$, a user can compute an escrow $Z$ such that anyone can verify that $Z$ was computed correctly from the user&#x27;s credential attributes, and moreover, the auditor can recover $f(x,y)$ from $Z$. Our contributions are: * We define secure $f$-blueprint systems; our definition is designed to provide a modular extension to anonymous credential systems. * We show that secure $f$-blueprint systems can be constructed for all functions $f$ from fully homomorphic encryption and NIZK proof systems, or from non-interactive secure computation and NIZK. These results are of theoretical interest but is not efficient enough for practical use. * We realize an optimal blueprint system under the DDH assumption in the random-oracle model for the watchlist function.

  匹配依据：MPC: secure computation

  </details>

- **Threshold-Optimal MPC With Friends and Foes**
  2022-11-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1526)
  Nikolas Melissaris, Divya Ravi, Sophia Yakoubov

  <details><summary>摘要 / Abstract</summary>

  Alon et. al (Crypto 2020) initiated the study of MPC with Friends and Foes (FaF) security, which captures the desirable property that even up to $h^{*}$ honest parties should learn nothing additional about other honest parties’ inputs, even if the $t$ corrupt parties send them extra information. Alon et. al describe two flavors of FaF security: weak FaF, where the simulated view of up to $h^{*}$ honest parties should be indistinguishable from their real view, and strong FaF, where the simulated view of the honest parties should be indistinguishable from their real view even in conjunction with the simulated / real view of the corrupt parties. They give several initial FaF constructions with guaranteed output delivery (GOD); however, they leave some open problems. Their only construction which supports the optimal corruption bounds of $2t+h^{*} &lt; n$ (where $n$ denotes the number of parties) only offers weak FaF security and takes much more than the optimal three rounds of communication. In this paper, we describe two new constructions with GOD, both of which support $2t+h^{*} &lt; n$. Our first construction, based on threshold FHE, is the first three-round construction that matches this optimal corruption bound (though it only offers weak FaF security). Our second construction, based on a variant of BGW, is the first such construction that offers strong FaF security (though it requires more than three rounds, as well as correlated randomness). Our final contribution is further exploration of the relationship between FaF security and similar security notions. In particular, we show that FaF security does not imply mixed adversary security (where the adversary can make $t$ active and $h^{*}$ passive corruptions), and that Best of Both Worlds security (where the adversary can make $t$ active or $t+h^{*}$ passive corruptions, but not both) is orthogonal to both FaF and mixed adversary security.

  匹配依据：MPC: mpc (context)

  </details>

- **Your Reputation's Safe with Me: Framing-Free Distributed Zero-Knowledge Proofs**
  2022-11-03 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1523)
  Carmit Hazay, Muthuramakrishnan Venkitasubramaniam, Mor Weiss

  <details><summary>摘要 / Abstract</summary>

  Distributed Zero-Knowledge (dZK) proofs, recently introduced by Boneh et al. (CYPTO`19), allow a prover $P$ to prove NP statements on an input $x$ which is distributed between $k$ verifiers $V_1,\ldots,V_k$, where each $V_i$ holds only a piece of $x$. As in standard ZK proofs, dZK proofs guarantee Completeness when all parties are honest; Soundness against a malicious prover colluding with $t$ verifiers; and Zero Knowledge against a subset of $t$ malicious verifiers, in the sense that they learn nothing about the NP witness and the input pieces of the honest verifiers. Unfortunately, dZK proofs provide no correctness guarantee for an honest prover against a subset of maliciously corrupted verifiers. In particular, such verifiers might be able to ``frame&#x27;&#x27; the prover, causing honest verifiers to reject a true claim. This is a significant limitation, since such scenarios arise naturally in dZK applications, e.g., for proving honest behavior, and such attacks are indeed possible in existing dZKs. We put forth and study the notion of strong completeness for dZKs, guaranteeing that true claims are accepted even when $t$ verifiers are maliciously corrupted. We then design strongly-complete dZK proofs using the ``MPC-in-the-head&#x27;&#x27; paradigm of Ishai et al. (STOC`07), providing a novel analysis that exploits the unique properties of the distributed setting. To demonstrate the usefulness of strong completeness, we present several applications in which it is instrumental in obtaining security. First, we construct a certifiable version of Verifiable Secret Sharing (VSS), which is a VSS in which the dealer additionally proves that the shared secret satisfies a given NP relation. Our construction withstands a constant fraction of corruptions, whereas a previous construction of Ishai et al. (TCC`14) could only handle $k^{\varepsilon}$ corruptions for a small $\varepsilon&lt;1$. We also design a reusable version of certifiable VSS that we introduce, in which the dealer can prove an unlimited number of predicates on the same shared secret. Finally, we extend a compiler of Boneh et al. (CRYPTO`19), who used dZKs to transform a class of ``natural&#x27;&#x27; semi-honest protocols in the honest-majority setting into maliciously secure ones with abort. Our compiler uses strongly-complete dZKs to obtain identifiable abort.

  匹配依据：MPC: secret sharing

  </details>

- **Towards federated multivariate statistical process control (FedMSPC)**
  2022-11-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.01645)
  Du Nguyen Duy, David Gabauer, Ramin Nikzad-Langerodi

  <details><summary>摘要 / Abstract</summary>

  The ongoing transition from a linear (produce-use-dispose) to a circular economy poses significant challenges to current state-of-the-art information and communication technologies. In particular, the derivation of integrated, high-level views on material, process, and product streams from (real-time) data produced along value chains is challenging for several reasons. Most importantly, sufficiently rich data is often available yet not shared across company borders because of privacy concerns which make it impossible to build integrated process models that capture the interrelations between input materials, process parameters, and key performance indicators along value chains. In the current contribution, we propose a privacy-preserving, federated multivariate statistical process control (FedMSPC) framework based on Federated Principal Component Analysis (PCA) and Secure Multiparty Computation to foster the incentive for closer collaboration of stakeholders along value chains. We tested our approach on two industrial benchmark data sets - SECOM and ST-AWFD. Our empirical results demonstrate the superior fault detection capability of the proposed approach compared to standard, single-party (multiway) PCA. Furthermore, we showcase the possibility of our framework to provide privacy-preserving fault diagnosis to each data holder in the value chain to underpin the benefits of secure data sharing and federated process modeling.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Secret Sharing for Generic Theoretic Cryptography**
  2022-11-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.01658)
  James Smith

  <details><summary>摘要 / Abstract</summary>

  Sharing a secret efficiently amongst a group of participants is not easy since there is always an adversary / eavesdropper trying to retrieve the secret. In secret sharing schemes, every participant is given a unique share. When the desired group of participants come together and provide their shares, the secret is obtained. For other combinations of shares, a garbage value is returned. A threshold secret sharing scheme was proposed by Shamir and Blakley independently. In this (n,t) threshold secret sharing scheme, the secret can be obtained when at least t out of n participants contribute their shares. This paper proposes a novel algorithm to reveal the secret only to the subsets of participants belonging to the access structure. This scheme implements totally generalized ideal secret sharing. Unlike threshold secret sharing schemes, this scheme reveals the secret only to the authorized sets of participants, not any arbitrary set of users with cardinality more than or equal to t. Since any access structure can be realized with this scheme, this scheme can be exploited to implement various access priorities and access control mechanisms. A major advantage of this scheme over the existing ones is that the shares being distributed to the participants is totally independent of the secret being shared. Hence, no restrictions are imposed on the scheme and it finds a wider use in real world applications.

  匹配依据：MPC: secret sharing

  </details>

- **Best-of-Both-Worlds Multiparty Quantum Computation with Publicly Verifiable Identifiable Abort**
  2022-11-03 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.01665) · [IACR ePrint](https://eprint.iacr.org/2022/1517)
  Kai-Min Chung, Mi-Ying Huang, Er-Cheng Tang, Jiapeng Zhang, Mi-Ying (Miryam) Huang

  <details><summary>摘要 / Abstract</summary>

  Alon et al. (CRYPTO 2021) introduced a multiparty quantum computation protocol that is secure with identifiable abort (MPQC-SWIA). However, their protocol allows only inside MPQC parties to know the identity of malicious players. This becomes problematic when two groups of people disagree and need a third party, like a jury, to verify who the malicious party is. This issue takes on heightened significance in the quantum setting, given that quantum states may exist in only a single copy. Thus, we emphasize the necessity of a protocol with publicly verifiable identifiable abort (PVIA), enabling outside observers with only classical computational power to agree on the identity of the malicious party in case of an abort. However, achieving MPQC with PVIA poses significant challenges due to the no-cloning theorem, and previous works proposed by Mahadev (STOC 2018) and Chung et al. (Eurocrypt 2022) for classical verification of quantum computation fall short. In this paper, we obtain the first MPQC-PVIA protocol assuming post-quantum oblivious transfer and a classical broadcast channel. The core component of our construction is a new authentication primitive called auditable quantum authentication (AQA) that identifies the malicious sender with overwhelming probability. Additionally, we provide the first MPQC protocol with best-of-both-worlds (BoBW) security, which guarantees output delivery with an honest majority and remains secure with abort even if the majority is dishonest. Our best-of-both-worlds MPQC protocol also satisfies PVIA upon abort.

  匹配依据：MPC: oblivious transfer

  </details>

- **Witness Encryption for Succinct Functional Commitments and Applications**
  2022-11-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1510)
  Matteo Campanelli, Dario Fiore, Hamidreza Khoshakhlagh

  <details><summary>摘要 / Abstract</summary>

  Witness encryption (WE), introduced by Garg, Gentry, Sahai, and Waters (STOC 2013) allows one to encrypt a message to a statement $\mathsf{x}$ for some NP language $\mathcal{L}$, such that any user holding a witness for $\mathsf{x} \in \mathcal{L}$ can decrypt the ciphertext. The extreme power of this primitive comes at the cost of its elusiveness: a practical construction from established cryptographic assumptions is currently out of reach. In this work, we investigate a new notion of encryption that has a flavor of WE and that we can build only based on bilinear pairings, for interesting classes of computation. We do this by connecting witness encryption to functional commitments (FC). FCs are an advanced notion of commitments that allows fine-grained openings, that is non-interactive proofs to show that a commitment $\mathsf{cm}$ opens to $v$ such that $y=G(v)$, with the crucial feature that both commitments and openings are succinct. Our new WE notion, witness encryption for (succinct) functional commitment (WE-FC), allows one to encrypt a message with respect to a triple $(\mathsf{cm}, G, y)$, and decryption is unlocked using an FC opening that $\mathsf{cm}$ opens to $v$ such that $y=G(v)$. This mechanism is similar to the notion of witness encryption for NIZK of commitments [Benhamouda and Lin, TCC&#x27;20], with the crucial difference that ours supports commitments and decryption time whose size and complexity do not depend on the length of the committed data $v$. Our main contributions are therefore the formal definition of WE-FC, a generic methodology to compile an FC in bilinear groups into an associated WE-FC scheme (semantically secure in the generic group model), and a new FC construction for NC1 circuits that yields a WE-FC for the same class of functions. Similarly to [Benhamouda and Lin, TCC&#x27;20], we show how to apply WE-FC to construct multiparty reusable non-interactive secure computation (mrNISC) protocols. Crucially, the efficiency profile of WE-FC yields mrNISC protocols whose offline stage has shorter communication (only a succinct commitment from each party). As an additional contribution, we discuss further applications of WE-FC and show how to extend this primitive to better suit these settings.

  匹配依据：MPC: secure computation

  </details>

- **Oblivious Quantum Computation and Delegated Multiparty Quantum Computation**
  2022-11-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.00962)
  Masahito Hayashi

  <details><summary>摘要 / Abstract</summary>

  We propose a new concept, oblivious quantum computation, which requires performing oblivious transfer with respect to the computation outcome of the quantum computation, where the secrecy of the input qubits and the program to identify the quantum gates are required. Exploiting quantum teleportation, we propose a two-server protocol for this task, which realizes an exponential improvement for the communication complexity over the simple application of two-server (quantum) oblivious transfer to the sending of the computation result. Also, we discuss delegated multiparty quantum computation, in which, several users ask multiparty quantum computation to server(s) only using classical communications. We propose a two-server protocol for the latter task as well.

  匹配依据：MPC: oblivious transfer

  </details>

- **MPCFormer: fast, performant and private Transformer inference with MPC**
  2022-11-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2211.01452) · [Code](https://github.com/MccRee177/MPCFormer)
  Dacheng Li, Rulin Shao, Hongyi Wang, Han Guo, Eric P. Xing, Hao Zhang

  <details><summary>摘要 / Abstract</summary>

  Enabling private inference is crucial for many cloud inference services that are based on Transformer models. However, existing private inference solutions can increase the inference latency by more than 60x or significantly compromise the inference quality. In this paper, we design the framework MPCFORMER as a practical solution, using Secure Multi-Party Computation (MPC) and Knowledge Distillation (KD). Through extensive evaluations, we show that MPCFORMER significantly speeds up Transformer inference in MPC settings while achieving similar ML performance to the input model. On the IMDb dataset, it achieves similar performance to BERTBASE, while being 5.3x faster. On the GLUE benchmark, it achieves 97% performance of BERTBASE with a 2.2x speedup. MPCFORMER remains effective with different trained Transformer weights such as ROBERTABASE and larger models including BERTLarge. Code is available at https://github.com/MccRee177/MPCFormer.

  匹配依据：MPC: secure multi party computation

  </details>

- **MinRank in the Head: Short Signatures from Zero-Knowledge Proofs**
  2022-11-01 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1501)
  Gora Adj, Luis Rivera-Zamarripa, Javier Verbel

  <details><summary>摘要 / Abstract</summary>

  In recent years, many digital signature scheme proposals have been built from the so-called MPC-in-the-head paradigm. This has shown to be an outstanding way to design efficient signatures with security based on hard problems. MinRank is an NP-complete problem extensively studied due to its applications to cryptanalysis since its introduction in 1999. However, only a few schemes base their security on its intractability, and their signature size is large compared with other proposals based on NP problems. This paper introduces the first MinRank-based digital signature scheme that uses the MPC-in-the-head, enabling it to achieve small signature sizes and running times. For NIST&#x27;s category I parameter set, we obtain signatures of 6.5KB, which is competitive with the shortest proposals in the literature that are based on non-structured problems.

  匹配依据：MPC: mpc (context)

  </details>

- **Simple, Fast, Efficient, and Tightly-Secure Non-Malleable Non-Interactive Timed Commitments**
  2022-10-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1498)
  Peter Chvojka, Tibor Jager

  <details><summary>摘要 / Abstract</summary>

  Timed commitment schemes, introduced by Boneh and Naor (CRYPTO 2000), can be used to achieve fairness in secure computation protocols in a simple and elegant way. The only known non-malleable construction in the standard model is due to Katz, Loss, and Xu (TCC 2020). This construction requires general-purpose zero knowledge proofs with specific properties, and it suffers from an inefficient commitment protocol, which requires the committing party to solve a computationally expensive puzzle. We propose new constructions of non-malleable non-interactive timed commitments, which combine (an extension of) the Naor-Yung paradigm used to construct IND-CCA secure encryption with a non-interactive ZK proofs for a simple algebraic language. This yields much simpler and more efficient non-malleable timed commitments in the standard model. Furthermore, our constructions also compare favourably to known constructions of timed commitments in the random oracle model, as they achieve several further interesting properties that make the schemes very practical. This includes the possibility of using a homomorphism for the forced opening of multiple commitments in the sense of Malavolta and Thyagarajan (CRYPTO 2019), and they are the first constructions to achieve public verifiability, which seems particularly useful to apply the homomorphism in practical applications.

  匹配依据：MPC: secure computation

  </details>

- **Registered Attribute-Based Encryption**
  2022-10-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1500)
  Susan Hohenberger, George Lu, Brent Waters, David J. Wu

  <details><summary>摘要 / Abstract</summary>

  Attribute-based encryption (ABE) generalizes public-key encryption and enables fine-grained control to encrypted data. However, ABE upends the traditional trust model of public-key encryption by requiring a single trusted authority to issue decryption keys. If an adversary compromises the central authority and exfiltrates its secret key, then the adversary can decrypt every ciphertext in the system. This work introduces registered ABE, a primitive that allows users to generate secret keys on their own and then register the associated public key with a &quot;key curator&quot; along with their attributes. The key curator aggregates the public keys from the different users into a single compact master public key. To decrypt, users occasionally need to obtain helper decryption keys from the key curator which they combine with their own secret keys. We require that the size of the aggregated public key, the helper decryption keys, the ciphertexts, as well as the encryption/decryption times to be polylogarithmic in the number of registered users. Moreover, the key curator is entirely transparent and maintains no secrets. Registered ABE generalizes the notion of registration-based encryption (RBE) introduced by Garg et al. (TCC 2018), who focused on the simpler setting of identity-based encryption. We construct a registered ABE scheme that supports an a priori bounded number of users and policies that can be described by a linear secret sharing scheme (e.g., monotone Boolean formulas) from assumptions on composite-order pairing groups. Our approach deviates sharply from previous techniques for constructing RBE and only makes black-box use of cryptography. All existing RBE constructions (a weaker notion than registered ABE) rely on heavy non-black-box techniques. The encryption and decryption costs of our construction are comparable to those of vanilla pairing-based ABE. Two limitations of our scheme are that it requires a structured reference string whose size scales quadratically with the number of users (and linearly with the size of the attribute universe) and the running time of registration scales linearly with the number of users. Finally, as a feasibility result, we construct a registered ABE scheme that supports general policies and an arbitrary number of users from indistinguishability obfuscation and somewhere statistically binding hash functions.

  匹配依据：MPC: secret sharing

  </details>

- **Multiplicative Partially Homomorphic CRT Secret Sharing**
  2022-10-31 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1496)
  Shlomi Dolev, Yaniv Kleinman

  <details><summary>摘要 / Abstract</summary>

  A new CRT-based positive (non-zero) secret-sharing scheme with perfect information-theoretic (PIT) security and multiplicative homomorphism is presented. The scheme is designed to support the evaluation of multiplications of non-zero secrets of multiplicative groups. Our CRT-based scheme is partially homomorphic, supporting homomorphic multiplications. Nevertheless, our scheme has the potential to be regarded as fully homomorphic for practical scenarios, such as bounded-sized multi-cloud databases.

  匹配依据：MPC: secret sharing

  </details>

- **Mahiru: a federated, policy-driven data processing and exchange system**
  2022-10-31 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.17155)
  Lourens E. Veen, Sara Shakeri, Paola Grosso

  <details><summary>摘要 / Abstract</summary>

  Secure, privacy-preserving sharing of scientific or business data is currently a popular topic for research and development, both in academia and outside of it. Systems have been proposed for sharing individual facts about individuals and sharing entire data sets, for sharing data through trusted third parties, for obfuscating sensitive data by anonymisation and homomorphic encryption, for distributed processing as in federated machine learning and secure multiparty computation, and for trading data access or ownership. However, these systems typically support only one of these solutions, while organisations often have a variety of data and use cases for which different solutions are appropriate. If a single system could be built that is flexible enough to support a variety of solutions, then administration would be greatly simplified and attack surfaces reduced. In this paper we present Mahiru, a design for a data exchange and processing system in which owners of data and software fully control their assets, users may submit a wide variety of processing requests including most of the above applications, and all parties collaborate to execute those requests in a distributed fashion, while ensuring that the policies are adhered to at all times. This is achieved through a federated, mostly decentralised architecture and a powerful policy mechanism designed to be easy to understand and simple to implement. We have created a proof-of-concept implementation of the system which is openly available and in continuous development, and which we aim to continue to extend with new functionality.

  匹配依据：MPC: secure multiparty computation

  </details>

- **PHY-Fed: An Information-Theoretic Secure Aggregation in Federated Learning in Wireless Communications**
  2022-10-30 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.16917)
  Mitra Hassani, Reza Gholizadeh

  <details><summary>摘要 / Abstract</summary>

  Federated learning (FL) is a type of distributed machine learning at the wireless edge that preserves the privacy of clients&#x27; data from adversaries and even the central server. Existing federated learning approaches either use (i) secure multiparty computation (SMC) which is vulnerable to inference or (ii) differential privacy which may decrease the test accuracy given a large number of parties with relatively small amounts of data each. To tackle the problem with the existing methods in the literature, In this paper, we introduce PHY-Fed, a new framework that secures federated algorithms from an information-theoretic point of view.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Towards Practical Secure Neural Network Inference: The Journey So Far and the Road Ahead**
  2022-10-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1483)
  Zoltán Ádám Mann, Christian Weinert, Daphnee Chabal, Joppe W. Bos

  <details><summary>摘要 / Abstract</summary>

  Neural networks (NNs) have become one of the most important tools for artificial intelligence (AI). Well-designed and trained NNs can perform inference (e.g., make decisions or predictions) on unseen inputs with high accuracy. Using NNs often involves sensitive data: depending on the specific use case, the input to the NN and/or the internals of the NN (e.g., the weights and biases) may be sensitive. Thus, there is a need for techniques for performing NN inference securely, ensuring that sensitive data remains secret. In the past few years, several approaches have been proposed for secure neural network inference. These approaches achieve better and better results in terms of efficiency, security, accuracy, and applicability, thus making big progress towards practical secure neural network inference. The proposed approaches make use of many different techniques, such as homomorphic encryption and secure multi-party computation. The aim of this survey paper is to give an overview of the main approaches proposed so far, their different properties, and the techniques used. In addition, remaining challenges towards large-scale deployments are identified.

  匹配依据：MPC: secure multi party computation

  </details>

- **Multi-Point HashDH OPRF using Multiplicative Blinding with Application to Private Set Intersection**
  2022-10-28 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1482)
  Minglang Dong

  <details><summary>摘要 / Abstract</summary>

  The privacy set intersection (PSI) protocol with the oblivious pseudorandom function (OPRF) as the core component is a crucial member of PSI family, and the most efficient PSI protocol at present also belongs to this category. Based on DDH assumption, Hash Diffie-Hellman (HashDH) PSI is one of the most classical PSI protocols. Benefiting by its low communication overhead, it still has tremendous research value today. The OPRF subprotocol at the bottom of classical DH-PSI protocol falls into the abstract blind-query-de-blinding OPRF paradigm, while employs the exponential blinding (Exp-HashDH) method. An alternative method called multiplication blinding (Mult-HashDH) offers the improvement which the exponential blinding can&#x27;t give in performance. This method substitutes multiple variable-base exponentiations with fixed-base exponentiations, and by taking full advantage of this outstanding feature and pre-computation, the computational efficiency of the client can be at least doubled. However, neither Mult-HashDH OPRF nor Mult-HashDH PSI can give a strict security proof under the semi-honest model, which makes the security of the scheme is now reeling from a crisis of confidence. In this paper, the security proof of a modified Mult-HashDH OPRF is formally given under the semi-honest model, and then the HashDH PSI protocol is constructed based on it, which not only ensures the security of the scheme but also have no influence on damaging the efficiency of the protocol. the experimental comparison shows that our protocol achieves 2.65−13.20× speedup in running time.

  匹配依据：MPC: private set intersection

  </details>

- **Machine Unlearning of Federated Clusters**
  2022-10-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.16424) · [Code](https://github.com/thupchnsky/mufc)
  Chao Pan, Jin Sima, Saurav Prakash, Vishal Rana, Olgica Milenkovic

  <details><summary>摘要 / Abstract</summary>

  Federated clustering (FC) is an unsupervised learning problem that arises in a number of practical applications, including personalized recommender and healthcare systems. With the adoption of recent laws ensuring the &quot;right to be forgotten&quot;, the problem of machine unlearning for FC methods has become of significant importance. We introduce, for the first time, the problem of machine unlearning for FC, and propose an efficient unlearning mechanism for a customized secure FC framework. Our FC framework utilizes special initialization procedures that we show are well-suited for unlearning. To protect client data privacy, we develop the secure compressed multiset aggregation (SCMA) framework that addresses sparse secure federated learning (FL) problems encountered during clustering as well as more general problems. To simultaneously facilitate low communication complexity and secret sharing protocols, we integrate Reed-Solomon encoding with special evaluation points into our SCMA pipeline, and prove that the client communication cost is logarithmic in the vector dimension. Additionally, to demonstrate the benefits of our unlearning mechanism over complete retraining, we provide a theoretical analysis for the unlearning performance of our approach. Simulation results show that the new FC framework exhibits superior clustering performance compared to previously reported FC baselines when the cluster sizes are highly imbalanced. Compared to completely retraining K-means++ locally and globally for each removal request, our unlearning procedure offers an average speed-up of roughly 84x across seven datasets. Our implementation for the proposed method is available at https://github.com/thupchnsky/mufc.

  匹配依据：MPC: secret sharing

  </details>

- **Partially Oblivious Neural Network Inference**
  2022-10-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.15189)
  Panagiotis Rizomiliotis, Christos Diou, Aikaterini Triakosia, Ilias Kyrannas, Konstantinos Tserpes

  <details><summary>摘要 / Abstract</summary>

  Oblivious inference is the task of outsourcing a ML model, like neural-networks, without disclosing critical and sensitive information, like the model&#x27;s parameters. One of the most prominent solutions for secure oblivious inference is based on a powerful cryptographic tools, like Homomorphic Encryption (HE) and/or multi-party computation (MPC). Even though the implementation of oblivious inference systems schemes has impressively improved the last decade, there are still significant limitations on the ML models that they can practically implement. Especially when both the ML model and the input data&#x27;s confidentiality must be protected. In this paper, we introduce the notion of partially oblivious inference. We empirically show that for neural network models, like CNNs, some information leakage can be acceptable. We therefore propose a novel trade-off between security and efficiency. In our research, we investigate the impact on security and inference runtime performance from the CNN model&#x27;s weights partial leakage. We experimentally demonstrate that in a CIFAR-10 network we can leak up to $80\%$ of the model&#x27;s weights with practically no security impact, while the necessary HE-mutliplications are performed four times faster.

  匹配依据：MPC: multi party computation

  </details>

- **Private Collaborative Data Cleaning via Non-Equi PSI**
  2022-10-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1465)
  Erik-Oliver Blass, Florian Kerschbaum

  <details><summary>摘要 / Abstract</summary>

  We introduce and investigate the privacy-preserving version of collaborative data cleaning. With collaborative data cleaning, two parties want to reconcile their data sets to filter out badly classified, misclassified data items. In the privacy-preserving (private) version of data cleaning, the additional security goal is that parties should only learn their misclassified data items, but nothing else about the other party&#x27;s data set. The problem of private data cleaning is essentially a variation of private set intersection (PSI), and one could employ recent circuit-PSI techniques to compute misclassifications with privacy. However, we design, analyze, and implement three new protocols tailored to the specifics of private data cleaning that significantly outperform a circuit-PSI-based approach. With the first protocol, we exploit the idea that a small additional leakage (the size of the intersection of data items) allows for runtime and communication improvements of more than one order of magnitude over circuit-PSI. The other two protocols convert the problem of finding a mismatch in data classifications into finding a match, and then follow the standard technique of using oblivious pseudo-random functions (OPRF) for computing PSI. Depending on the number of data classes, this leads to either total runtime or communication improvements of up to two orders of magnitude over circuit-PSI.

  匹配依据：MPC: private set intersection

  </details>

- **Privacy-preserving Automatic Speaker Diarization**
  2022-10-26 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.14995)
  Francisco Teixeira, Alberto Abad, Bhiksha Raj, Isabel Trancoso

  <details><summary>摘要 / Abstract</summary>

  Automatic Speaker Diarization (ASD) is an enabling technology with numerous applications, which deals with recordings of multiple speakers, raising special concerns in terms of privacy. In fact, in remote settings, where recordings are shared with a server, clients relinquish not only the privacy of their conversation, but also of all the information that can be inferred from their voices. However, to the best of our knowledge, the development of privacy-preserving ASD systems has been overlooked thus far. In this work, we tackle this problem using a combination of two cryptographic techniques, Secure Multiparty Computation (SMC) and Secure Modular Hashing, and apply them to the two main steps of a cascaded ASD system: speaker embedding extraction and agglomerative hierarchical clustering. Our system is able to achieve a reasonable trade-off between performance and efficiency, presenting real-time factors of 1.1 and 1.6, for two different SMC security settings.

  匹配依据：MPC: secure multiparty computation

  </details>

- **I want to ride my BICYCL: BICYCL Implements CryptographY in CLass groups**
  2022-10-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1466)
  Cyril Bouvier, Guilhem Castagnos, Laurent Imbert, Fabien Laguillaumie

  <details><summary>摘要 / Abstract</summary>

  We introduce BICYCL an Open Source C++ library that implements arithmetic in the ideal class groups of imaginary quadratic fields, together with a set of cryptographic primitives based on class groups. It is available at https://gite.lirmm.fr/crypto/bicycl under GNU General Public License version 3 or any later version. BICYCL provides significant speed-ups on the implementation of the arithmetic of class groups. Concerning cryptographic applications, BICYCL is orders of magnitude faster than any previous pilot implementation of the CL linearly encryption scheme, making it faster than Paillier’s encryption scheme at any security level. Linearly homomorphic encryption is the core of many multi-party computation protocols, sometimes involving a huge number of encryptions and homomorphic evaluations: class group-based protocols become the best solution in terms of bandwidth and computational efficiency to rely upon.

  匹配依据：MPC: multi party computation

  </details>

- **How to Obfuscate MPC Inputs**
  2022-10-26 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1463)
  Ian McQuoid, Mike Rosulek, Jiayu Xu

  <details><summary>摘要 / Abstract</summary>

  We introduce the idea of input obfuscation for secure two-party computation ($\textsf{io2PC}$). Suppose Alice holds a private value $x$ and wants to allow clients to learn $f(x,y_i)$, for their choice of $y_i$, via a secure computation protocol. The goal of $\textsf{io2PC}$ is for Alice to encode $x$ so that an adversary who compromises her storage gets only oracle access to the function $f(x,\cdot)$. At the same time, there must be a 2PC protocol for computing $f(x,y)$ that takes only this encoding (and not the plaintext $x$) as input. We show how to achieve $\textsf{io2PC}$ for functions that have virtual black-box (VBB) obfuscation in either the random oracle model or generic group model. For functions that can be VBB-obfuscated in the random oracle model, we provide an $\textsf{io2PC}$ protocol by replacing the random oracle with an oblivious PRF. For functions that can be VBB-obfuscated in the generic group model, we show how Alice can instantiate a &quot;personalized&quot; generic group. A personalized generic group is one where only Alice can perform the algebraic operations of the group, but where she can let others perform operations in that group via an oblivious interactive protocol.

  匹配依据：MPC: secure computation, secure two party computation

  </details>

- **Circuit Privacy for FHEW/TFHE-Style Fully Homomorphic Encryption in Practice**
  2022-10-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1459)
  Kamil Kluczniak

  <details><summary>摘要 / Abstract</summary>

  A fully homomorphic encryption (FHE) scheme allows a client to encrypt and delegate its data to a server that performs computation on the encrypted data that the client can then decrypt. While FHE gives confidentiality to clients&#x27; data, it does not protect the server&#x27;s input and computation. Nevertheless, FHE schemes are still helpful in building delegation protocols that reduce communication complexity, as the ciphertext&#x27;s size is independent of the size of the computation performed on them. We can further extend FHE by a property called circuit privacy, which guarantees that the result of computing on ciphertexts reveals no information on the computed function and the inputs of the server. Thereby, circuit private FHE gives rise to round optimal and communication efficient secure two-party computation protocols. Unfortunately, despite significant efforts and much work put into the efficiency and practical implementations of FHE schemes, very little has been done to provide useful and practical FHE supporting circuit privacy. In this work, we address this gap and design the first randomized bootstrapping algorithm whose single invocation sanitizes a ciphertext and, consequently, serves as a tool to provide circuit privacy. We give an extensive analysis, propose parameters, and provide a C++ implementation of our scheme. Our bootstrapping can sanitize a ciphertext to achieve circuit privacy at an 80-bit statistical security level in between 1.3 and 0.9 seconds, depending which Gaussian sampling algorithm is used, and whether the parameter set targets a fast Fourier or a number theoretic transform-based implementation. In addition, we can perform non-sanitized bootstrapping in around 0.27 or 0.14 seconds. Crucially, we do not need to increase the parameters to perform computation before or after sanitization takes place. For comparison&#x27;s sake, we revisit the Ducas-Stehl\&#x27;e washing machine method. In particular, we give a tight analysis, estimate efficiency, review old, and provide new parameters.

  匹配依据：MPC: secure two party computation

  </details>

- **Unconditional Proofs-of-Work and Other Possibilities of Thermodynamic Cryptography**
  2022-10-24 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.13278)
  Xavier Coiteux-Roy, Stefan Wolf

  <details><summary>摘要 / Abstract</summary>

  In line with advances in recent years about realizing cryptographic functionalities in an information-theoretically secure way from physical phenomena and laws, we propose here to obtain useful tasks from the sole assumption of limited free energy. Specifically, based on that assumption -- resulting in a setting loosely related to Maurer&#x27;s bounded-storage model -- we derive protocols for unconditional proofs-of-thermodynamical-work, secret sharing of free energy, unforgeable money, and proofs-of-position. While our schemes can be considered classical and not quantum per se, they are resistant against both classes of adversaries.

  匹配依据：MPC: secret sharing

  </details>

- **ParaDiSE: Efficient Threshold Authenticated Encryption in Fully Malicious Model**
  2022-10-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1449)
  Shashank Agrawal, Wei Dai, Atul Luykx, Pratyay Mukherjee, Peter Rindal

  <details><summary>摘要 / Abstract</summary>

  Threshold cryptographic algorithms achieve robustness against key and access compromise by distributing secret keys among multiple entities. Most prior work focuses on threshold public-key primitives, despite extensive use of authenticated encryption in practice. Though the latter can be deployed in a threshold manner using multi-party computation (MPC), doing so incurs a high communication cost. In contrast, dedicated constructions of threshold authenticated encryption algorithms can achieve high performance. However to date, few such algorithms are known, most notably DiSE (distributed symmetric encryption) by Agrawal et al. (ACM CCS 2018). To achieve threshold authenticated encryption} (TAE), prior work does not suffice, due to shortcomings in definitions, analysis, and design, allowing for potentially insecure schemes, an undesirable similarity between encryption and decryption, and insufficient understanding of the impact of parameters due to lack of concrete analysis. In response, we revisit the problem of designing secure and efficient TAE schemes. (1) We give new TAE security definitions in the fully malicious setting addressing the aforementioned concerns. (2) We construct efficient schemes satisfying our definitions and perform concrete and more modular security analyses. (3) We conduct an extensive performance evaluation of our constructions, against prior ones.

  匹配依据：MPC: multi party computation

  </details>

- **Assisted MPC**
  2022-10-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1453)
  Philipp Muth, Stefan Katzenbeisser

  <details><summary>摘要 / Abstract</summary>

  Since their introduction in the 1970s, multi-party computation protocols have become the prevalent method for two or more parties to jointly compute an agreed upon function on private inputs without revealing them to other parties. While some efficiency gains in the offline phase of MPC protocols have been achieved, most works in the past have focused on optimising the online phase. Improvements to the online phase typically shifted significant workload to the offline phase. In this work we explore a novel approach to streamline the offline phase of secret sharing based MPC protocols by introducing a helper party that executes the preprocessing for the parties engaged in the online phase. We prove, that the security guarantees provided by the MPC protocols stay unchanged and demonstrate the efficiency of our approach in two sets of benchmarks. We furthermore give three examples of real world instantiations of the helper party to demonstrate that our approach is not only of a theoretical nature.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Half-Tree: Halving the Cost of Tree Expansion in COT and DPF**
  2022-10-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1431)
  Xiaojie Guo, Kang Yang, Xiao Wang, Wenhao Zhang, Xiang Xie, Jiang Zhang, Zheli Liu

  <details><summary>摘要 / Abstract</summary>

  GGM tree is widely used in the design of correlated oblivious transfer (COT), subfield vector oblivious linear evaluation (sVOLE), distributed point function (DPF), and distributed comparison function (DCF). Often, the cost associated with GGM tree dominates the computation and communication of these protocols. In this paper, we propose a suite of optimizations that can reduce this cost by half. • Halving the cost of COT and sVOLE. Our COT protocol introduces extra correlation to each level of a GGM tree used by the state-of-the-art COT protocol. As a result, it reduces both the number of AES calls and the communication by half. Extending this idea to sVOLE, we are able to achieve similar improvement with either halved computation or halved communication. • Halving the cost of DPF and DCF. We propose improved two-party protocols for the distributed generation of DPF/DCF keys. Our tree structures behind these protocols lead to more efficient full-domain evaluation and halve the communication and the round complexity of the state-of-the-art DPF/DCF protocols. All protocols are provably secure in the random-permutation model and can be accelerated based on fixed-key AES-NI. We also improve the state-of-the-art schemes of puncturable pseudorandom function (PPRF), DPF, and DCF, which are of independent interest in dealer-available scenarios.

  匹配依据：MPC: oblivious transfer

  </details>

- **Eagle: Efficient Privacy Preserving Smart Contracts**
  2022-10-21 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1435)
  Carsten Baum, James Hsin-yu Chiang, Bernardo David, Tore Kasper Frederiksen

  <details><summary>摘要 / Abstract</summary>

  The proliferation of Decentralised Finance (DeFi) and Decentralised Autonomous Organisations (DAO), which in current form are exposed to front-running of token transactions and proposal voting, demonstrate the need to shield user inputs and internal state from the parties executing smart contracts. In this work we present “Eagle”, an efficient UC-secure protocol which efficiently realises a notion of privacy preserving smart contracts where both the amounts of tokens and the auxiliary data given as input to a contract are kept private from all parties but the one providing the input. Prior proposals realizing privacy preserving smart contracts on public, permissionless blockchains generally offer a limited contract functionality or require a trusted third party to manage private inputs and state. We achieve our results through a combination of secure multi-party computation (MPC) and zero-knowledge proofs on Pedersen commitments. Although other approaches leverage MPC in this setting, these incur impractical computational overheads by requiring the computation of cryptographic primitives within MPC. Our solution achieves security without the need of any cryptographic primitives to be computed inside the MPC instance and only require a constant amount of exponentiations per client input.

  匹配依据：MPC: secure multi party computation

  </details>

- **NFGen: Automatic Non-linear Function Evaluation Code Generator for General-purpose MPC Platforms**
  2022-10-18 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.09802)
  Xiaoyu Fan, Kun Chen, Guosai Wang, Mingchun Zhuang, Yi Li, Wei Xu

  <details><summary>摘要 / Abstract</summary>

  Due to the absence of a library for non-linear function evaluation, so-called general-purpose secure multi-party computation (MPC) are not as &#x27;&#x27;general&#x27;&#x27; as MPC programmers expect. Prior arts either naively reuse plaintext methods, resulting in suboptimal performance and even incorrect results, or handcraft ad hoc approximations for specific functions or platforms. We propose a general technique, NFGen, that utilizes pre-computed discrete piecewise polynomials to accurately approximate generic functions using fixed-point numbers. We implement it using a performance-prediction-based code generator to support different platforms. Conducting extensive evaluations of 23 non-linear functions against six MPC protocols on two platforms, we demonstrate significant performance, accuracy, and generality improvements over existing methods.

  匹配依据：MPC: secure multi party computation

  </details>

- **Private Data Valuation and Fair Payment in Data Marketplaces**
  2022-10-17 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.08723)
  Zhihua Tian, Jian Liu, Jingyu Li, Xinle Cao, Ruoxi Jia, Jun Kong, Mengdi Liu, Kui Ren

  <details><summary>摘要 / Abstract</summary>

  Data valuation is an essential task in a data marketplace. It aims at fairly compensating data owners for their contribution. There is increasing recognition in the machine learning community that the Shapley value -- a foundational profit-sharing scheme in cooperative game theory -- has major potential to value data, because it uniquely satisfies basic properties for fair credit allocation and has been shown to be able to identify data sources that are useful or harmful to model performance. However, calculating the Shapley value requires accessing original data sources. It still remains an open question how to design a real-world data marketplace that takes advantage of the Shapley value-based data pricing while protecting privacy and allowing fair payments. In this paper, we propose the {\em first} prototype of a data marketplace that values data sources based on the Shapley value in a privacy-preserving manner and at the same time ensures fair payments. Our approach is enabled by a suite of innovations on both algorithm and system design. We firstly propose a Shapley value calculation algorithm that can be efficiently implemented via multiparty computation (MPC) circuits. The key idea is to learn a performance predictor that can directly predict model performance corresponding to an input dataset without performing actual training. We further optimize the MPC circuit design based on the structure of the performance predictor. We further incorporate fair payment into the MPC circuit to guarantee that the data that the buyer pays for is exactly the same as the one that has been valuated. Our experimental results show that the proposed new data valuation algorithm is as effective as the original expensive one. Furthermore, the customized MPC protocol is efficient and scalable.

  匹配依据：MPC: multiparty computation

  </details>

- **VerifyML: Obliviously Checking Model Fairness Resilient to Malicious Model Holder**
  2022-10-16 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.08418)
  Guowen Xu, Xingshuo Han, Gelei Deng, Tianwei Zhang, Shengmin Xu, Jianting Ning, Anjia Yang, Hongwei Li

  <details><summary>摘要 / Abstract</summary>

  In this paper, we present VerifyML, the first secure inference framework to check the fairness degree of a given Machine learning (ML) model. VerifyML is generic and is immune to any obstruction by the malicious model holder during the verification process. We rely on secure two-party computation (2PC) technology to implement VerifyML, and carefully customize a series of optimization methods to boost its performance for both linear and nonlinear layer execution. Specifically, (1) VerifyML allows the vast majority of the overhead to be performed offline, thus meeting the low latency requirements for online inference. (2) To speed up offline preparation, we first design novel homomorphic parallel computing techniques to accelerate the authenticated Beaver&#x27;s triple (including matrix-vector and convolution triples) generation procedure. It achieves up to $1.7\times$ computation speedup and gains at least $10.7\times$ less communication overhead compared to state-of-the-art work. (3) We also present a new cryptographic protocol to evaluate the activation functions of non-linear layers, which is $4\times$--$42\times$ faster and has $&gt;48\times$ lesser communication than existing 2PC protocol against malicious parties. In fact, VerifyML even beats the state-of-the-art semi-honest ML secure inference system! We provide formal theoretical analysis for VerifyML security and demonstrate its performance superiority on mainstream ML models including ResNet-18 and LeNet.

  匹配依据：MPC: secure two party computation

  </details>

- **PIRANA: Faster Multi-query PIR via Constant-weight Codes**
  2022-10-16 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1401)
  Jian Liu, Jingyu Li, Di Wu, Kui Ren

  <details><summary>摘要 / Abstract</summary>

  Private information retrieval (PIR) is a cryptographic protocol that enables a wide range of privacy-preserving applications. Despite being extensively studied for decades, it is still not efficient enough to be used in practice. In this paper, we propose a novel PIR protocol named PIRANA, based on the recent advances in constant-weight codes. It is up to 188.6× faster than the original constant-weight PIR (presented in Usenix SEC &#x27;22). Most importantly, PIRANA naturally supports multi-query. It allows a client to retrieve a batch of elements from the server with a very small extra-cost compared to retrieving a single element, which results in up to an 14.4× speedup over the state-of-the-art multi-query PIR (presented in Oakland &#x27;23). We also discuss a way to extend PIRANA to labeled private set intersection (LPSI). Compared with existing LPSI protocols, PIRANA is more friendly to the scenarios where the database updates frequently.

  匹配依据：MPC: private set intersection

  </details>

- **Synchronous Perfectly Secure Message Transmission with Optimal Asynchronous Fallback Guarantees**
  2022-10-15 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1397)
  Giovanni Deligios, Chen-Da Liu-Zhang

  <details><summary>摘要 / Abstract</summary>

  Secure message transmission (SMT) constitutes a fundamental network-layer building block for distributed protocols over incomplete networks. More specifically, a sender $\mathbf{S}$ and a receiver $\mathbf{R}$ are connected via $\ell$ disjoint paths, of which at most $t$ paths are controlled by the adversary. Perfectly-secure SMT protocols in synchronous and asynchronous networks are resilient up to $\ell/2$ and $\ell/3$ corruptions respectively. In this work, we ask whether it is possible to achieve a perfect SMT protocol that simultaneously tolerates $t_s &lt; \ell/2$ corruptions when the network is synchronous, and $t_a &lt; \ell/3$ when the network is asynchronous. We completely resolve this question by showing that perfect SMT is possible if and only if $2t_a + t_s &lt; \ell$. In addition, we provide a concretely round-efficient solution for the (slightly worse) trade-off $t_a + 2t_s &lt; \ell$. As a direct application of our results, following the recent work by Appan, Chandramouli, and Choudhury [PODC&#x27;22], we obtain an $n$-party perfectly-secure synchronous multi-party computation protocol with asynchronous fallback over any network with connectivity $\ell$, as long as $t_a + 3t_s &lt;n$ and $2t_a + t_s &lt; \ell$.

  匹配依据：MPC: multi party computation

  </details>

- **A Secure Multiparty Quantum Least Common Multiple Computation Protocol**
  2022-10-15 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.08165)
  Zixian Li, Wenjie Liu

  <details><summary>摘要 / Abstract</summary>

  In this paper, we present a secure multiparty computation (SMC) protocol for least common multiple (LCM) based on Shor&#x27;s quantum period-finding algorithm (QPA). Our protocol is based on the following principle: the connection of multiple periodic functions is also a periodic function whose period is exactly the least common multiple of all small periods. Since QPA is a probabilistic algorithm, we also propose a one-vote-down vote protocol based on the existing secure multi-party quantum summation protocol, which is used to verify the results of the proposed LCM protocol. Security analysis shows that under the semi-honest model, the proposed protocol is secure with high probability, while the computational consumption remains at polynomial complexity. The protocol proposed in this paper solves the problem of efficient and secure multiparty computation of LCM, demonstrating quantum computation potential.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Reflections on trusting distributed trust**
  2022-10-14 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.08127)
  Emma Dauterman, Vivian Fang, Natacha Crooks, Raluca Ada Popa

  <details><summary>摘要 / Abstract</summary>

  Many systems today distribute trust across multiple parties such that the system provides certain security properties if a subset of the parties are honest. In the past few years, we have seen an explosion of academic and industrial cryptographic systems built on distributed trust, including secure multi-party computation applications (e.g., private analytics, secure learning, and private key recovery) and blockchains. These systems have great potential for improving security and privacy, but face a significant hurdle on the path to deployment. We initiate study of the following problem: a single organization is, by definition, a single party, and so how can a single organization build a distributed-trust system where corruptions are independent? We instead consider an alternative formulation of the problem: rather than ensuring that a distributed-trust system is set up correctly by design, what if instead, users can audit a distributed-trust deployment? We propose a framework that enables a developer to efficiently and cheaply set up any distributed-trust system in a publicly auditable way. To do this, we identify two application-independent building blocks that we can use to bootstrap arbitrary distributed-trust applications: secure hardware and an append-only log. We show how to leverage existing implementations of these building blocks to deploy distributed-trust systems, and we give recommendations for infrastructure changes that would make it easier to deploy distributed-trust systems in the future.

  匹配依据：MPC: secure multi party computation

  </details>

- **Practical Asynchronous High-threshold Distributed Key Generation and Distributed Polynomial Sampling**
  2022-10-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1389)
  Sourav Das, Zhuolun Xiang, Lefteris Kokoris-Kogias, Ling Ren

  <details><summary>摘要 / Abstract</summary>

  Distributed Key Generation (DKG) is a technique to bootstrap threshold cryptosystems without a trusted party. DKG is an essential building block to many decentralized protocols such as randomness beacons, threshold signatures, Byzantine consensus, and multiparty computation. While significant progress has been made recently, existing asynchronous DKG constructions are inefficient when the reconstruction threshold is larger than one-third of the total nodes. In this paper, we present a simple and concretely efficient asynchronous DKG (ADKG) protocol among $n=3t+1$ nodes that can tolerate up to $t$ malicious nodes and support any reconstruction threshold $\ell\ge t$. Our protocol has an expected $O(\kappa n^3)$ communication cost, where $\kappa$ is a security parameter, and only assumes the hardness of Discrete Logarithm. The core ingredient of our ADKG protocol is an asynchronous protocol to secret share a random polynomial of degree $\ell\ge t$, which has other applications such as asynchronous proactive secret sharing and asynchronous multiparty computation. We implement our high-threshold ADKG protocol and evaluate it using a network of up to 128 geographically distributed nodes. Our evaluation shows that our high-threshold ADKG protocol reduces the running time by $90\%$ and reduces the bandwidth usage by $80\%$ over state-of-the-art.

  匹配依据：MPC: multiparty computation, secret sharing

  </details>

- **Multiplicative and Verifiably Multiplicative Secret Sharing for Multipartite Adversary Structures**
  2022-10-14 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1390)
  Reo Eriguchi, Noboru Kunihiro, Koji Nuida

  <details><summary>摘要 / Abstract</summary>

  $d$-Multiplicative secret sharing enables $n$ players to locally compute additive shares of the product of $d$ secrets from their shares. Barkol et al. (Journal of Cryptology, 2010) show that it is possible to construct a $d$-multiplicative scheme for any adversary structure satisfying the $Q_d$ property, in which no $d$ sets cover the whole set of players. In this paper, we focus on multipartite adversary structures and propose efficient multiplicative and verifiably multiplicative secret sharing schemes tailored to them. First, our multiplicative scheme is applicable to any multipartite $Q_d$-adversary structure. If the number of parts is constant, our scheme achieves a share size polynomial in the number $n$ of players while the general construction by Barkol et al. results in exponentially large share size in the worst case. We also propose its variant defined over smaller fields. As a result, for a special class of bipartite adversary structures with two maximal points, it achieves a constant share size for arbitrary $n$ while the share size of the first scheme necessarily incurs a logarithmic factor of $n$. Secondly, we devise a more efficient scheme for a special class of multipartite ones such that players in each part have the same weight and a set of players belongs to the adversary structure if and only if the sum of their weights is at most a threshold. Thirdly, if the adversary structure is $Q_{d+1}$, our first scheme is shown to be a verifiably multiplicative scheme that detects incorrect outputs with probability $1$. For multipartite adversary structures with a constant number of parts, it improves the worst-case share and proof sizes of the only known general construction by Yoshida and Obana (IEEE Transactions on Information Theory, 2019). Finally, we propose a more efficient verifiably multiplicative scheme by allowing small error probability $\delta$ and focusing on a more restricted class of multipartite adversary structures. Our scheme verifies computation of polynomials and can achieve a share size independent of $\delta$ while the previous construction only works for monomials and results in a share size involving a factor of $\log\delta^{-1}$.

  匹配依据：MPC: secret sharing

  </details>

- **Sublinear-Round Broadcast without Trusted Setup against Dishonest Majority**
  2022-10-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1383)
  Andreea B. Alexandru, Julian Loss, Charalampos Papamanthou, Giorgos Tsimos

  <details><summary>摘要 / Abstract</summary>

  Byzantine broadcast is one of the fundamental problems in distributed computing. Many practical applications from secure multiparty computation to consensus mechanisms for blockchains require increasingly weaker trust assumptions, as well as scalability for an ever-growing number of users, which rules out existing solutions with linear number of rounds or trusted setup requirements. In this paper, we propose the first sublinear-round and trustless Byzantine broadcast protocol. Unlike previous sublinear-round protocols, our protocol does not assume the existence of a trusted dealer who honestly issues keys and common random strings to the parties. Our protocol is based on a new cryptographic protocol called verifiable graded consensus, designed to act as an untrusted online setup, enabling $n$ parties to almost agree on shared random strings. We propose an implementation of the verifiable graded consensus protocol using transparent setup verifiable delay functions and random oracles, which is then used to run a committee-based Byzantine protocol, similar to Chan et al. (PKC 2020), in an unbiased fashion. Finally, we obtain a polylog-round trustless Byzantine broadcast with amortized communication complexity of $\tilde O(n^2)$, which can be further improved to $\tilde O(n)$ per instance for multiple instances of parallel broadcast.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Secure Multiparty Computation for Synthetic Data Generation from Distributed Data**
  2022-10-13 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.07332)
  Mayana Pereira, Sikha Pentyala, Anderson Nascimento, Rafael T. de Sousa, Martine De Cock

  <details><summary>摘要 / Abstract</summary>

  Legal and ethical restrictions on accessing relevant data inhibit data science research in critical domains such as health, finance, and education. Synthetic data generation algorithms with privacy guarantees are emerging as a paradigm to break this data logjam. Existing approaches, however, assume that the data holders supply their raw data to a trusted curator, who uses it as fuel for synthetic data generation. This severely limits the applicability, as much of the valuable data in the world is locked up in silos, controlled by entities who cannot show their data to each other or a central aggregator without raising privacy concerns. To overcome this roadblock, we propose the first solution in which data holders only share encrypted data for differentially private synthetic data generation. Data holders send shares to servers who perform Secure Multiparty Computation (MPC) computations while the original data stays encrypted. We instantiate this idea in an MPC protocol for the Multiplicative Weights with Exponential Mechanism (MWEM) algorithm to generate synthetic data based on real data originating from many data holders without reliance on a single point of failure.

  匹配依据：MPC: secure multiparty computation

  </details>

- **AIM: Symmetric Primitive for Shorter Signatures with Stronger Security (Full Version)**
  2022-10-13 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1387)
  Seongkwang Kim, Jincheol Ha, Mincheol Son, Byeonghak Lee, Dukjae Moon, Joohee Lee, Sangyub Lee, Jihoon Kwon, Jihoon Cho, Hyojin Yoon, Jooyoung Lee

  <details><summary>摘要 / Abstract</summary>

  Post-quantum signature schemes based on the MPC-in-the-Head (MPCitH) paradigm are recently attracting significant attention as their security solely depends on the one-wayness of the underlying primitive, providing diversity for the hardness assumption in post-quantum cryptography. Recent MPCitH-friendly ciphers have been designed using simple algebraic S-boxes operating on a large field in order to improve the performance of the resulting signature schemes. Due to their simple algebraic structures, their security against algebraic attacks should be comprehensively studied. In this paper, we refine algebraic cryptanalysis of power mapping based S-boxes over binary extension fields, and cryptographic primitives based on such S-boxes. In particular, for the Gröbner basis attack over $\mathbb{F}_2$, we experimentally show that the exact number of Boolean quadratic equations obtained from the underlying S-boxes is critical to correctly estimate the theoretic complexity based on the degree of regularity. Similarly, it turns out that the XL attack might be faster when all possible quadratic equations are found and used from the S-boxes. This refined cryptanalysis leads to more precise algebraic analysis of cryptographic primitives based on algebraic S-boxes. Considering the refined algebraic cryptanalysis, we propose a new one-way function, dubbed $\mathsf{AIM}$, as an MPCitH-friendly symmetric primitive with high resistance to algebraic attacks. The security of $\mathsf{AIM}$ is comprehensively analyzed with respect to algebraic, statistical, quantum, and generic attacks. $\mathsf{AIM}$ is combined with the BN++ proof system, yielding a new signature scheme, dubbed $\mathsf{AIMer}$. Our implementation shows that $\mathsf{AIMer}$ outperforms existing signature schemes based on symmetric primitives in terms of signature size and signing time.

  匹配依据：MPC: mpc (context)

  </details>

- **On the Security of KOS**
  2022-10-12 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1371)
  Benjamin E. Diamond

  <details><summary>摘要 / Abstract</summary>

  We study the security of the random oblivious transfer extension protocol of Keller, Orsini, and Scholl (CRYPTO &#x27;15), whose security proof was recently invalidated by Roy (CRYPTO &#x27;22). We show that KOS is asymptotically secure. Our proof involves a subtle analysis of the protocol&#x27;s &quot;correlation check&quot;, and introduces several new techniques. We also study the protocol&#x27;s concrete security. We establish concrete security for security parameter values on the order of 5,000. We present evidence that a stronger result than ours—if possible—is likely to require radically new ideas.

  匹配依据：MPC: oblivious transfer

  </details>

- **Constructions of cyclic codes and extended primitive cyclic codes with their applications**
  2022-10-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.05170)
  Ziling Heng, Xinran Wang, Xiaoru Li

  <details><summary>摘要 / Abstract</summary>

  Linear codes with a few weights have many nice applications including combinatorial design, distributed storage system, secret sharing schemes and so on. In this paper, we construct two families of linear codes with a few weights based on special polynomials over finite fields. The first family of linear codes are extended primitive cyclic codes which are affine-invariant. The second family of linear codes are reducible cyclic codes. The parameters of these codes and their duals are determined. As the first application, we prove that these two families of linear codes hold $t$-designs, where $t=2,3$. As the second application, the minimum localities of the codes are also determined and optimal locally recoverable codes are derived.

  匹配依据：MPC: secret sharing

  </details>

- **Comparison of encrypted control approaches and tutorial on dynamic systems using LWE-based homomorphic encryption**
  2022-10-11 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.05560)
  Junsoo Kim, Dongwoo Kim, Yongsoo Song, Hyungbo Shim, Henrik Sandberg, Karl H. Johansson

  <details><summary>摘要 / Abstract</summary>

  Encrypted control has been introduced to protect controller data by encryption at the stage of computation and communication, by performing the computation directly on encrypted data. In this article, we first review and categorize recent relevant studies on encrypted control. Approaches based on homomorphic encryption, multi-party computation, and secret sharing are introduced, compared, and then discussed with respect to computational complexity, communication load, enabled operations, security, and research directions. We proceed to discuss a current challenge in the application of homomorphic encryption to dynamic systems, where arithmetic operations other than integer addition and multiplication are limited. We also introduce a homomorphic cryptosystem called ``GSW-LWE&#x27;&#x27; and discuss its benefits that allow for recursive multiplication of encrypted dynamic systems, without use of computationally expensive bootstrapping techniques.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **ALLOSAUR: Accumulator with Low-Latency Oblivious Sublinear Anonymous credential Updates with Revocations**
  2022-10-11 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1362)
  Samuel Jaques, Michael Lodder, Hart Montgomery

  <details><summary>摘要 / Abstract</summary>

  A cryptographic accumulator is a space- and time-efficient data structure with associated algorithms used for secure membership testing. In the growing space of digital credentials, accumulators found in managing a set of valid credentials, giving efficient and anonymous methods for credential holders to prove their validity. Unlike traditional credentials like digital signatures, one can easily revoke credentials with an accumulator; however, each revocation forces existing credential holders to engage in an expensive update process. Previous works make this faster and easier by sacrificing anonymity. To improve performance without compromising privacy, we present ALLOSAUR, a multi-party accumulator based on pairings. In ALLOSAUR, we eliminate the cost of accumulating new credentials, let &quot;credential managers&quot; manage the accumulator values with secure multiparty computation, and allow anonymous credential updates with a square-root reduction in communication costs as compared to existing work. A deployed digital credential system is a vast and complicated system, and existing formalisms do not fully address the scope or power of a real-world adversary. We develop a thorough UC-style formalism that allows arbitrary malicious behaviour from an adversary controlling a minority of credential managers and arbitrary numbers of users, credentials, and verifiers. In our new formalism we present a novel definition of privacy that captures as much anonymity as possible while accounting for inevitable losses from interaction with the system. The detail in our formalism reveals real-world issues in existing accumulator constructions, all of which ALLOSAUR avoids. Our proof-of-concept implementation can update over 1000 revocations with less than half a second of total computation and 16 kB communication, at least a 5x improvement over the previous state-of-the-art in both metrics.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Anonymous Permutation Routing**
  2022-10-10 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1353)
  Paul Bunn, Eyal Kushilevitz, Rafail Ostrovsky

  <details><summary>摘要 / Abstract</summary>

  The Non-Interactive Anonymous Router (NIAR) model was introduced by Shi and Wu [SW21] as an alternative to conventional solutions to the anonymous routing problem, in which a set of senders wish to send messages to a set of receivers. In contrast to most known approaches to support anonymous routing (e.g. mix-nets, DC-nets, etc.) which rely on a network of routers communicating with users via interactive protocols, the NIAR model assumes a $single$ router and is inherently $non$-$interactive$ (after an initial setup phase). In addition to being non-interactive, the NIAR model is compelling due to the security it provides: instead of relying on the honesty of some subset of the routers, the NIAR model requires anonymity even if the router (as well as an arbitrary subset of senders/receivers) is corrupted. In this paper, we present a protocol for the NIAR model that improves upon the results from [SW21] in two ways: - Improved computational efficiency (quadratic to near linear): Our protocol matches the communication complexity of [SW21] for each sender/receiver, while reducing the computational overhead for the router to polylog overhead instead of linear overhead. - Relaxation of assumptions: Security of the protocol in [SW21] relies on the Decisional Linear assumption in bilinear groups; while security for our protocol follows from the existence of any rate-1 oblivious transfer (OT) protocol (instantiations of this primitive are known to exist under DDH, QR and LWE [DGI19,GHO20]).

  匹配依据：MPC: oblivious transfer

  </details>

- **One-Wayness in Quantum Cryptography**
  2022-10-07 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.03394) · [IACR ePrint](https://eprint.iacr.org/2022/1336)
  Tomoyuki Morimae, Takashi Yamakawa

  <details><summary>摘要 / Abstract</summary>

  The existence of one-way functions is one of the most fundamental assumptions in classical cryptography. In the quantum world, on the other hand, there are evidences that some cryptographic primitives can exist even if one-way functions do not exist. We therefore have the following important open problem in quantum cryptography: What is the most fundamental element in quantum cryptography? In this direction, Brakerski, Canetti, and Qian recently defined a notion called EFI pairs, which are pairs of efficiently generatable states that are statistically distinguishable but computationally indistinguishable, and showed its equivalence with some cryptographic primitives including commitments, oblivious transfer, and general multi-party computations. However, their work focuses on decision-type primitives and does not cover search-type primitives like quantum money and digital signatures. In this paper, we study properties of one-way state generators (OWSGs), which are a quantum analogue of one-way functions. We first revisit the definition of OWSGs and generalize it by allowing mixed output states. Then we show the following results. (1) We define a weaker version of OWSGs, weak OWSGs, and show that they are equivalent to OWSGs. (2) Quantum digital signatures are equivalent to OWSGs. (3) Private-key quantum money schemes (with pure money states) imply OWSGs. (4) Quantum pseudo one-time pad schemes imply both OWSGs and EFI pairs. (5) We introduce an incomparable variant of OWSGs, which we call secretly-verifiable and statistically-invertible OWSGs, and show that they are equivalent to EFI pairs.

  匹配依据：MPC: oblivious transfer

  </details>

- **On the Classic Protocol for MPC Schnorr Signatures**
  2022-10-06 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1332)
  Nikolaos Makriyannis

  <details><summary>摘要 / Abstract</summary>

  In this paper, we prove that the classic three-round protocol for MPC Schnorr Signatures is fully-adaptive UC-secure. Furthermore, we show that a simple variant of the Classic protocol achieves tight security, i.e.~the security of the resulting, modified, protocol tightly reduces to the security of the underlying non-MPC scheme.

  匹配依据：MPC: mpc (context)

  </details>

- **Federated Boosted Decision Trees with Differential Privacy**
  2022-10-06 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.02910)
  Samuel Maddock, Graham Cormode, Tianhao Wang, Carsten Maple, Somesh Jha

  <details><summary>摘要 / Abstract</summary>

  There is great demand for scalable, secure, and efficient privacy-preserving machine learning models that can be trained over distributed data. While deep learning models typically achieve the best results in a centralized non-secure setting, different models can excel when privacy and communication constraints are imposed. Instead, tree-based approaches such as XGBoost have attracted much attention for their high performance and ease of use; in particular, they often achieve state-of-the-art results on tabular data. Consequently, several recent works have focused on translating Gradient Boosted Decision Tree (GBDT) models like XGBoost into federated settings, via cryptographic mechanisms such as Homomorphic Encryption (HE) and Secure Multi-Party Computation (MPC). However, these do not always provide formal privacy guarantees, or consider the full range of hyperparameters and implementation settings. In this work, we implement the GBDT model under Differential Privacy (DP). We propose a general framework that captures and extends existing approaches for differentially private decision trees. Our framework of methods is tailored to the federated setting, and we show that with a careful choice of techniques it is possible to achieve very high utility while maintaining strong levels of privacy.

  匹配依据：MPC: secure multi party computation

  </details>

- **Bicoptor: Two-round Secure Three-party Non-linear Computation without Preprocessing for Privacy-preserving Machine Learning**
  2022-10-05 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.01988)
  Lijing Zhou, Ziyu Wang, Hongrui Cui, Qingrui Song, Yu Yu

  <details><summary>摘要 / Abstract</summary>

  The overhead of non-linear functions dominates the performance of the secure multiparty computation (MPC) based privacy-preserving machine learning (PPML). This work introduces a family of novel secure three-party computation (3PC) protocols, Bicoptor, which improve the efficiency of evaluating non-linear functions. The basis of Bicoptor is a new sign determination protocol, which relies on a clever use of the truncation protocol proposed in SecureML (S\&amp;P 2017). Our 3PC sign determination protocol only requires two communication rounds, and does not involve any preprocessing. Such sign determination protocol is well-suited for computing non-linear functions in PPML, e.g. the activation function ReLU, Maxpool, and their variants. We develop suitable protocols for these non-linear functions, which form a family of GPU-friendly protocols, Bicoptor. All Bicoptor protocols only require two communication rounds without preprocessing. We evaluate Bicoptor under a 3-party LAN network over a public cloud, and achieve more than 370,000 DReLU/ReLU or 41,000 Maxpool (find the maximum value of nine inputs) operations per second. Under the same settings and environment, our ReLU protocol has a one or even two orders of magnitude improvement to the state-of-the-art works, Falcon (PETS 2021) or Edabits (CRYPTO 2020), respectively without batch processing.

  匹配依据：MPC: secure multiparty computation, secure three party computation

  </details>

- **SecureFedYJ: a safe feature Gaussianization protocol for Federated Learning**
  2022-10-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.01639)
  Tanguy Marchand, Boris Muzellec, Constance Beguier, Jean Ogier du Terrail, Mathieu Andreux

  <details><summary>摘要 / Abstract</summary>

  The Yeo-Johnson (YJ) transformation is a standard parametrized per-feature unidimensional transformation often used to Gaussianize features in machine learning. In this paper, we investigate the problem of applying the YJ transformation in a cross-silo Federated Learning setting under privacy constraints. For the first time, we prove that the YJ negative log-likelihood is in fact convex, which allows us to optimize it with exponential search. We numerically show that the resulting algorithm is more stable than the state-of-the-art approach based on the Brent minimization method. Building on this simple algorithm and Secure Multiparty Computation routines, we propose SecureFedYJ, a federated algorithm that performs a pooled-equivalent YJ transformation without leaking more information than the final fitted parameters do. Quantitative experiments on real data demonstrate that, in addition to being secure, our approach reliably normalizes features across silos as well as if data were pooled, making it a viable approach for safe federated feature Gaussianization.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Privacy-Preserving Link Prediction**
  2022-10-04 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.01297)
  Didem Demirag, Mina Namazi, Erman Ayday, Jeremy Clark

  <details><summary>摘要 / Abstract</summary>

  Consider two data holders, ABC and XYZ, with graph data (e.g., social networks, e-commerce, telecommunication, and bio-informatics). ABC can see that node A is linked to node B, and XYZ can see node B is linked to node C. Node B is the common neighbour of A and C but neither network can discover this fact on their own. In this paper, we provide a two party computation that ABC and XYZ can run to discover the common neighbours in the union of their graph data, however neither party has to reveal their plaintext graph to the other. Based on private set intersection, we implement our solution, provide measurements, and quantify partial leaks of privacy. We also propose a heavyweight solution that leaks zero information based on additively homomorphic encryption.

  匹配依据：MPC: private set intersection, two party computation

  </details>

- **General Partially Fair Multi-Party Computation with VDFs**
  2022-10-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1318)
  Bolton Bailey, Andrew Miller, Or Sattath

  <details><summary>摘要 / Abstract</summary>

  Gordon and Katz, in &quot;Partial Fairness in Secure Two-Party Computation&quot;, present a protocol for two-party computation with partial fairness which depends on presumptions on the size of the input or output of the functionality. They also show that for some other functionalities, this notion of partial fairness is impossible to achieve. In this work, we get around this impossibility result using verifiable delay functions, a primitive which brings in an assumption on the inability of an adversary to compute a certain function in a specified time. We present a gadget using VDFs which allows for any MPC to be carried out with ≈ 1/R partial fairness, where R is the number of communication rounds.

  匹配依据：MPC: multi party computation, secure two party computation, two party computation

  </details>

- **Bounded Surjective Quadratic Functions over $\\mathbb F\_p^n$ for MPC-/ZK-/FHE-Friendly Symmetric Primitives**
  2022-10-04 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1313)
  Lorenzo Grassi

  <details><summary>摘要 / Abstract</summary>

  Motivated by new applications such as secure Multi-Party Computation (MPC), Fully Homomorphic Encryption (FHE), and Zero-Knowledge proofs (ZK), many MPC-, FHE- and ZK-friendly symmetric-key primitives that minimize the number of multiplications over $\mathbb F_p$ for a large prime $p$ have been recently proposed in the literature. These symmetric primitives are usually defined via invertible functions, including (i) Feistel and Lai-Massey schemes and (ii) SPN constructions instantiated with invertible non-linear S-Boxes. However, the ``invertibility&#x27;&#x27; property is actually never required in any of the mentioned applications. In this paper, we discuss the possibility to set up MPC-/FHE-/ZK-friendly symmetric primitives instantiated with non-invertible bounded surjective functions. With respect to one-to-one functions, any output of a $l$-bounded surjective function admits at most $l$ pre-images. The simplest example is the square map $x\mapsto x^2$ over $\mathbb F_p$ for a prime $p\ge 3$, which is (obviously) $2$-bounded surjective. When working over $\mathbb F_p^n$ for $n\ge 2$, we set up bounded surjective functions by re-considering the recent results proposed by Grassi, Onofri, Pedicini and Sozzi at FSE/ToSC 2022 as starting points. Given a quadratic local map $F:\mathbb F_p^m \rightarrow \mathbb F_p$ for $m\in\{1,2,3\}$, they proved that the shift-invariant non-linear function over $\mathbb F_p^n$ defined as $\mathcal S_F(x_0, x_1, \ldots, x_{n-1}) = y_0\| y_1\| \ldots \| y_{n-1}$ where $y_i := F(x_i, x_{i+1})$ is never invertible for any $n\ge 2\cdot m-1$. Here, we prove that - the quadratic function $F:\mathbb F_p^m \rightarrow \mathbb F_p$ for $m\in\{1,2\}$ that minimizes the probability of having a collision for $\mathcal S_F$ over $\mathbb F_p^n$ is of the form $F(x_0, x_1) = x_0^2 + x_1$ (or equivalent); - the function $\mathcal S_F$ over $\mathbb F_p^n$ defined as before via $F(x_0, x_1) = x_0^2 + x_1$ (or equivalent) is $2^n$-bounded surjective. As concrete applications, we propose modified versions of the MPC-friendly schemes MiMC, HadesMiMC, and (partially of) Hydra, and of the FHE-friendly schemes Masta, Pasta, and Rubato. By instantiating them with the bounded surjective quadratic functions proposed in this paper, we are able to improve the security and/or the performances in the target applications/protocols.

  匹配依据：MPC: secure multi party computation

  </details>

- **pMPL: A Robust Multi-Party Learning Framework with a Privileged Party**
  2022-10-02 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.00486)
  Lushan Song, Jiaxuan Wang, Zhexuan Wang, Xinyu Tu, Guopeng Lin, Wenqiang Ruan, Haoqi Wu, Weili Han

  <details><summary>摘要 / Abstract</summary>

  In order to perform machine learning among multiple parties while protecting the privacy of raw data, privacy-preserving machine learning based on secure multi-party computation (MPL for short) has been a hot spot in recent. The configuration of MPL usually follows the peer-to-peer architecture, where each party has the same chance to reveal the output result. However, typical business scenarios often follow a hierarchical architecture where a powerful, usually privileged party, leads the tasks of machine learning. Only the privileged party can reveal the final model even if other assistant parties collude with each other. It is even required to avoid the abort of machine learning to ensure the scheduled deadlines and/or save used computing resources when part of assistant parties drop out. Motivated by the above scenarios, we propose pMPL, a robust MPL framework with a privileged part}. pMPL supports three-party training in the semi-honest setting. By setting alternate shares for the privileged party, pMPL is robust to tolerate one of the rest two parties dropping out during the training. With the above settings, we design a series of efficient protocols based on vector space secret sharing for pMPL to bridge the gap between vector space secret sharing and machine learning. Finally, the experimental results show that the performance of pMPL is promising when we compare it with the state-of-the-art MPL frameworks. Especially, in the LAN setting, pMPL is around $16\times$ and $5\times$ faster than TF-encrypted (with ABY3 as the back-end framework) for the linear regression, and logistic regression, respectively. Besides, the accuracy of trained models of linear regression, logistic regression, and BP neural networks can reach around 97%, 99%, and 96% on MNIST dataset respectively.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **MPC as a service using Ethereum Registry Smart Contracts - dCommon CIP**
  2022-10-02 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1309)
  Matt Shams(Anis), Bingsheng Zhang, Justinas Zaliaduonis

  <details><summary>摘要 / Abstract</summary>

  In this paper we introduce dCommon - auditable and programmable MPC as a service for solving multichain governance coordination problems throughout DeFi and Web3; Along with its on-chain part Common Interest Protocol (CIP) - an autonomous and immutable registry smart contract suite. CIP enables arbitrary business logic for off-chain computations using dCommon’s network/subnetworks with Ethereum smart contracts. In Stakehouse, CIP facilitates a trustless recovery of signing keys and key management for Ethereum validators on demand. The paper elucidates a formal overview of the MPC system cryptography mechanics and its smart contract business logic for the Stakehouse CIP (SH-CIP) application implementation.

  匹配依据：MPC: mpc (context)

  </details>

- **Privacy-preserving Decentralized Federated Learning over Time-varying Communication Graph**
  2022-10-01 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2210.00325)
  Yang Lu, Zhengxin Yu, Neeraj Suri

  <details><summary>摘要 / Abstract</summary>

  Establishing how a set of learners can provide privacy-preserving federated learning in a fully decentralized (peer-to-peer, no coordinator) manner is an open problem. We propose the first privacy-preserving consensus-based algorithm for the distributed learners to achieve decentralized global model aggregation in an environment of high mobility, where the communication graph between the learners may vary between successive rounds of model aggregation. In particular, in each round of global model aggregation, the Metropolis-Hastings method is applied to update the weighted adjacency matrix based on the current communication topology. In addition, the Shamir&#x27;s secret sharing scheme is integrated to facilitate privacy in reaching consensus of the global model. The paper establishes the correctness and privacy properties of the proposed algorithm. The computational efficiency is evaluated by a simulation built on a federated learning framework with a real-word dataset.

  匹配依据：MPC: secret sharing

  </details>

- **Private Certifier Intersection**
  2022-09-30 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1302)
  Bishakh Chandra Ghosh, Sikhar Patranabis, Dhinakaran Vinayagamurthy, Venkatraman Ramakrishna, Krishnasuri Narayanam, Sandip Chakraborty

  <details><summary>摘要 / Abstract</summary>

  We initiate the study of Private Certifier Intersection (PCI), which allows mutually distrusting parties to establish a trust basis for cross-validation of claims if they have one or more trust authorities (certifiers) in common. This is one of the essential requirements for verifiable presentations in Web 3.0, since it provides additional privacy without compromising on decentralization. A PCI protocol allows two or more parties holding certificates to identify a common set of certifiers while additionally validating the certificates issued by such certifiers, without leaking any information about the certifiers not in the output intersection. In this paper, we formally define the notion of multi-party PCI in the Simplified-UC framework for two different settings depending on whether certificates are required for any of the claims (called PCI-Any) or all of the claims (called PCI-All). We then design and implement two provably secure and practically efficient PCI protocols supporting validation of digital signature-based certificates: a PCI-Any protocol for ECDSA-based certificates and a PCI-All protocol for BLS-based certificates. The technical centerpiece of our proposals is the first secretsharing-based MPC framework supporting efficient computation of elliptic curve-based arithmetic operations, including elliptic curve pairings, in a black-box way. We implement this framework by building on top of the well-known MP-SPDZ library using OpenSSL and RELIC for elliptic curve operations, and use this implementation to benchmark our proposed PCI protocols in the LAN and WAN settings. In an intercontinental WAN setup with parties located in different continents, our protocols execute in less than a minute on input sets of size 40, which demonstrates the practicality of our proposed solutions.

  匹配依据：MPC: mpc (context)

  </details>

- **What Can Cryptography Do For Decentralized Mechanism Design?**
  2022-09-28 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2209.14462) · [IACR ePrint](https://eprint.iacr.org/2022/1294)
  Elaine Shi, Hao Chung, Ke Wu

  <details><summary>摘要 / Abstract</summary>

  Recent works of Roughgarden (EC&#x27;21) and Chung and Shi (SODA&#x27;23) initiate the study of a new decentralized mechanism design problem called transaction fee mechanism design (TFM). Unlike the classical mechanism design literature, in the decentralized environment, even the auctioneer (i.e., the miner) can be a strategic player, and it can even collude with a subset of the users facilitated by binding side contracts. Chung and Shi showed two main impossibility results that rule out the existence of a {\it dream} TFM. First, any TFM that provides incentive compatibility for individual users and miner-user coalitions must always have zero miner revenue, no matter whether the block size is finite or infinite. Second, assuming finite block size, no non-trivial TFM can simultaenously provide incentive compatibility for any individual user, and for any miner-user coalition. In this work, we explore what new models and meaningful relaxations can allow us to circumvent the impossibility results of Chung and Shi. Besides today&#x27;s model that does not employ cryptography, we introduce a new MPC-assisted model where the TFM is implemented by a joint multi-party computation (MPC) protocol among the miners. We prove several feasibility and infeasibility results for achieving {\it strict} and {\it approximate} incentive compatibility, respectively, in the plain model as well as the MPC-assisted model. We show that while cryptography is not a panacea, it indeed allows us to overcome some impossibility results pertaining to the plain model, leading to non-trivial mechanisms with useful guarantees that are otherwise impossible in the plain model. Our work is also the first to characterize the mathematical landscape of transaction fee mechanism design under approximate incentive compatibility, as well as in a cryptography-assisted model.

  匹配依据：MPC: multi party computation

  </details>

- **MPC-Pipe: an Efficient Pipeline Scheme for Secure Multi-party Machine Learning Inference**
  2022-09-27 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2209.13643)
  Yongqin Wang, Rachit Rajat, Murali Annavaram

  <details><summary>摘要 / Abstract</summary>

  Multi-party computing (MPC) has been gaining popularity as a secure computing model over the past few years. However, prior works have demonstrated that MPC protocols still pay substantial performance penalties compared to plaintext, particularly when applied to ML algorithms. The overhead is due to added computation and communication costs. Prior studies, as well as our own analysis, found that most MPC protocols today sequentially perform communication and computation. The participating parties must compute on their shares first and then perform data communication to allow the distribution of new secret shares before proceeding to the next computation step. In this work, we show that serialization is unnecessary, particularly in the context of ML computations (both in Convolutional neural networks and in Transformer-based models). We demonstrate that it is possible to carefully orchestrate the computation and communication steps to overlap. We propose MPC-Pipe, an efficient MPC system for both training and inference of ML workloads, which pipelines computations and communications in an MPC protocol during the online phase. MPC-Pipe proposes three pipeline schemes to optimize the online phase of ML in the semi-honest majority adversary setting. We implement MPC-Pipe by augmenting a modified version of CrypTen, which separates online and offline phases. We evaluate the end-to-end system performance benefits of the online phase of MPC using deep neural networks (VGG16, ResNet50) and Transformers using different network settings. We show that MPC-Pipe can improve the throughput and latency of ML workloads.

  匹配依据：MPC: multi party computing, secure computing

  </details>

- **Collusion-Resistant Functional Encryption for RAMs**
  2022-09-25 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1269)
  Prabhanjan Ananth, Kai-Min Chung, Xiong Fan, Luowen Qian

  <details><summary>摘要 / Abstract</summary>

  In recent years, functional encryption (FE) has established itself as one of the fundamental primitives in cryptography. The choice of model of computation to represent the functions associated with the functional keys plays a critical role in the complexity of the algorithms of an FE scheme. Historically, the functions are represented as circuits. However, this results in the decryption time of the FE scheme growing proportional to not only the worst case running time of the function but also the size of the input, which in many applications can be quite large. In this work, we present the first construction of a public-key collusion-resistant FE scheme, where the functions, associated with the keys, are represented as random access machines (RAMs). We base the security of our construction on the existence of: (i) public-key collusion- resistant FE for circuits and, (ii) public-key doubly-efficient private-information retrieval [Boyle et al., Canetti et al., TCC 2017]. Our scheme enjoys many nice efficiency properties, including input-specific decryption time. We also show how to achieve FE for RAMs in the bounded-key setting with weaker efficiency guarantees from laconic oblivious transfer, which can be based on standard cryptographic assumptions. En route to achieving our result, we present conceptually simpler constructions of succinct garbling for RAMs [Canetti et al., Chen et al., ITCS 2016] from weaker assumptions.

  匹配依据：MPC: oblivious transfer

  </details>

- **Asymptotically Free Broadcast in Constant Expected Time via Packed VSS**
  2022-09-24 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1266)
  Ittai Abraham, Gilad Asharov, Shravani Patil, Arpita Patra

  <details><summary>摘要 / Abstract</summary>

  Broadcast is an essential primitive for secure computation. We focus in this paper on optimal resilience (i.e., when the number of corrupted parties $t$ is less than a third of the computing parties $n$), and with no setup or cryptographic assumptions. While broadcast with worst case $t$ rounds is impossible, it has been shown [Feldman and Micali STOC&#x27;88, Katz and Koo CRYPTO&#x27;06] how to construct protocols with expected constant number of rounds in the private channel model. However, those constructions have large communication complexity, specifically $\mathcal{O}(n^2L+n^6\log n)$ expected number of bits transmitted for broadcasting a message of length $L$. This leads to a significant communication blowup in secure computation protocols in this setting. In this paper, we substantially improve the communication complexity of broadcast in constant expected time. Specifically, the expected communication complexity of our protocol is $\mathcal{O}(nL+n^4\log n)$. For messages of length $L=\Omega(n^3 \log n)$, our broadcast has no asymptotic overhead (up to expectation), as each party has to send or receive $\mathcal{O}(n^3 \log n)$ bits. We also consider parallel broadcast, where $n$ parties wish to broadcast $L$ bit messages in parallel. Our protocol has no asymptotic overhead for $L=\Omega(n^2\log n)$, which is a common communication pattern in perfectly secure MPC protocols. For instance, it is common that all parties share their inputs simultaneously at the same round, and verifiable secret sharing protocols require the dealer to broadcast a total of $\mathcal{O}(n^2\log n)$ bits. As an independent interest, our broadcast is achieved by a packed verifiable secret sharing, a new notion that we introduce. We show a protocol that verifies $\mathcal{O}(n)$ secrets simultaneously with the same cost of verifying just a single secret. This improves by a factor of $n$ the state-of-the-art.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Single-state multiparty semiquantum secret sharing with d-dimensional Bell states**
  2022-09-23 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2209.11391)
  Ying Chen, Zhi-Gang Gan, Tian-Yu Ye

  <details><summary>摘要 / Abstract</summary>

  A single-state multiparty semiquantum secret sharing (MSQSS) scheme with d-dimensional Bell states is proposed, which can accomplish the goal that only when all receivers work together can they restore the sender&#x27;s secret key. This protocol is validated to be secure against both the outside attack and the participant attack. This protocol is adaptive for the d-dimensional system, only employs one kind of d-dimensional Bell states as initial quantum resource and needs neither quantum entanglement swapping nor unitary operations.

  匹配依据：MPC: secret sharing

  </details>

- **Non-interactive XOR quantum oblivious transfer: optimal protocols and their experimental implementations**
  2022-09-22 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2209.11300)
  Lara Stroh, Nikola Horová, Robert Stárek, Ittoop V. Puthoor, Michal Mičuda, Miloslav Dušek, Erika Andersson

  <details><summary>摘要 / Abstract</summary>

  Oblivious transfer (OT) is an important cryptographic primitive. Any multi-party computation can be realised with OT as building block. XOR oblivious transfer (XOT) is a variant where the sender Alice has two bits, and a receiver Bob obtains either the first bit, the second bit, or their XOR. Bob should not learn anything more than this, and Alice should not learn what Bob has learnt. Perfect quantum OT with information-theoretic security is known to be impossible. We determine the smallest possible cheating probabilities for unrestricted dishonest parties in non-interactive quantum XOT protocols using symmetric pure states, and present an optimal protocol, which outperforms classical protocols. We also &quot;reverse&quot; this protocol, so that Bob becomes sender of a quantum state and Alice the receiver who measures it, while still implementing oblivious transfer from Alice to Bob. Cheating probabilities for both parties stay the same as for the unreversed protocol. We optically implemented both the unreversed and the reversed protocols, and cheating strategies, noting that the reversed protocol is easier to implement.

  匹配依据：MPC: multi party computation, oblivious transfer

  </details>

- **Understanding Information Disclosure from Secure Computation Output: A Study of Average Salary Computation**
  2022-09-21 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2209.10457)
  Alessandro Baccarini, Marina Blanton, Shaofeng Zou

  <details><summary>摘要 / Abstract</summary>

  Secure multi-party computation has seen substantial performance improvements in recent years and is being increasingly used in commercial products. While a significant amount of work was dedicated to improving its efficiency under standard security models, the threat models do not account for information leakage from the output of secure function evaluation. Quantifying information disclosure about private inputs from observing the function outcome is the subject of this work. Motivated by the City of Boston gender pay gap studies, in this work we focus on the computation of the average of salaries and quantify information disclosure about private inputs of one or more participants (the target) to an adversary via information-theoretic techniques. We study a number of distributions including log-normal, which is typically used for modeling salaries. We consequently evaluate information disclosure after repeated evaluation of the average function on overlapping inputs, as was done in the Boston gender pay study that ran multiple times, and provide recommendations for using the sum and average functions in secure computation applications. Our goal is to develop mechanisms that lower information disclosure about participants&#x27; inputs to a desired level and provide guidelines for setting up real-world secure evaluation of this function.

  匹配依据：MPC: secure computation, secure evaluation, secure function evaluation, secure multi party computation

  </details>

- **PolyMPCNet: Towards ReLU-free Neural Architecture Search in Two-party Computation Based Private Inference**
  2022-09-20 · MPC · 仅预印本来源 · [arXiv](https://arxiv.org/abs/2209.09424)
  Hongwu Peng, Shanglin Zhou, Yukui Luo, Shijin Duan, Nuo Xu, Ran Ran, Shaoyi Huang, Chenghong Wang, Tong Geng, Ang Li, Wujie Wen, Xiaolin Xu, Caiwen Ding

  <details><summary>摘要 / Abstract</summary>

  The rapid growth and deployment of deep learning (DL) has witnessed emerging privacy and security concerns. To mitigate these issues, secure multi-party computation (MPC) has been discussed, to enable the privacy-preserving DL computation. In practice, they often come at very high computation and communication overhead, and potentially prohibit their popularity in large scale systems. Two orthogonal research trends have attracted enormous interests in addressing the energy efficiency in secure deep learning, i.e., overhead reduction of MPC comparison protocol, and hardware acceleration. However, they either achieve a low reduction ratio and suffer from high latency due to limited computation and communication saving, or are power-hungry as existing works mainly focus on general computing platforms such as CPUs and GPUs. In this work, as the first attempt, we develop a systematic framework, PolyMPCNet, of joint overhead reduction of MPC comparison protocol and hardware acceleration, by integrating hardware latency of the cryptographic building block into the DNN loss function to achieve high energy efficiency, accuracy, and security guarantee. Instead of heuristically checking the model sensitivity after a DNN is well-trained (through deleting or dropping some non-polynomial operators), our key design principle is to em enforce exactly what is assumed in the DNN design -- training a DNN that is both hardware efficient and secure, while escaping the local minima and saddle points and maintaining high accuracy. More specifically, we propose a straight through polynomial activation initialization method for cryptographic hardware friendly trainable polynomial activation function to replace the expensive 2P-ReLU operator. We develop a cryptographic hardware scheduler and the corresponding performance model for Field Programmable Gate Arrays (FPGA) platform.

  匹配依据：MPC: secure multi party computation, two party computation

  </details>

- **Secure Quantum Bit Commitment**
  2022-09-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1238)
  Ping Wang, Yiting Su, Fangguo Zhang

  <details><summary>摘要 / Abstract</summary>

  Bit commitment (BC) is one of the most important fundamental protocols in secure multi-party computation. However, it is generally believed that unconditionally secure bit commitment is impossible even with quantum resources. In this paper, we design a secure non-interactive bit commitment protocol by exploiting the no-communication theorem of the quantum entangled states, whose security relies on the indistinguishability of whether the Bell states are measured or not. The proposed quantum bit commitment (QBC) is secure against classical adversaries with unlimited computing power, and the probability of a successful attack by quantum adversaries decreases exponentially as $n$ (the number of qubits in a group) increases.

  匹配依据：MPC: secure multi party computation

  </details>

- **On generalizations of the Lai-Massey scheme**
  2022-09-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1245)
  Lorenzo Grassi

  <details><summary>摘要 / Abstract</summary>

  In this paper, we re-investigate the Lai-Massey scheme, originally proposed in the cipher IDEA. Due to the similarity with the Feistel networks, and due to the existence of invariant subspace attacks as originally pointed out by Vaudenay at FSE 1999, the Lai-Massey scheme has received only little attention by the community. As first contribution, we propose two new generalizations of such scheme that are not (extended) affine equivalent to any generalized Feistel network proposed in the literature so far. Then, inspired by the recent Horst construction, we propose the Amaryllises structure as a generalization of the Lai-Massey scheme, in which the linear combination in the Lai-Massey scheme can be replaced by a non-linear one. Besides proposing concrete examples of the Amaryllises construction, we analyze its cryptographic properties in the context of MPC-/HE-/ZK-friendly symmetric primitives.

  匹配依据：MPC: mpc (context)

  </details>

- **Data Protection Law and Multi-Party Computation: Applications to Information Exchange between Law Enforcement Agencies**
  2022-09-19 · MPC · 仅预印本来源 · [IACR ePrint](https://eprint.iacr.org/2022/1242)
  Amos Treiber, Dirk Müllmann, Thomas Schneider, Indra Spiecker genannt Döhmann

  <details><summary>摘要 / Abstract</summary>

  Pushes for increased power of Law Enforcement (LE) for data retention and centralized storage result in legal challenges with data protection law and courts - and possible violations of the right to privacy. This is motivated by a desire for better cooperation and exchange between LE Agencies (LEAs), which is difficult due to data protection regulations, was identified as a main factor of major public security failures, and is a frequent criticism of LE. Secure Multi-Party Computation (MPC) is often seen as a technological means to solve privacy conflicts where actors want to exchange and analyze data that needs to be protected due to data protection laws. In this interdisciplinary work, we investigate the problem of private information exchange between LEAs from both a legal and technical angle. We give a legal analysis of secret-sharing based MPC techniques in general and, as a particular application scenario, consider the case of matching LE databases for lawful information exchange between LEAs. We propose a system for lawful information exchange between LEAs using MPC and private set intersection and show its feasibility by giving a legal analysis for data protection and a technical analysis for workload complexity. Towards practicality, we present insights from qualitative feedback gathered within exchanges with a major European LEA.

  匹配依据：MPC: multi party computation, private set intersection, secret sharing, secure multi party computation

  </details>
