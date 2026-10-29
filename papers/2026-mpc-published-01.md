# 2026 · MPC · 含会议/期刊记录 · 第 1/1 页

[总目录](../PAPERS.md)

- **Non-interactive Secure Computation with Constant Communication Overhead.**
  2026-07-29 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_5) · [IACR ePrint](https://eprint.iacr.org/2026/1555)
  Naty Peter, Yuval Ishai, Akshayaram Srinivasan, Ziyang Jin

  <details><summary>摘要 / Abstract</summary>

  We study the communication complexity of non-interactive secure computation (NISC) protocols with security against malicious adversaries. We give a general NISC protocol for any two-party function computed by a Boolean circuit $C$ using only $O(|C|\lambda)$ bits of communication, where $\lambda$ is a computational security parameter. This protocol is unconditionally secure in the random oracle model, assuming a standard random bit OT correlations setup. Compared to Yao&#x27;s semi-honest protocol, our protocol incurs only a constant communication overhead and achieves security against malicious parties with no additional interaction. Prior works achieved such constant overhead by either using a larger number of rounds or more structured correlations.

  匹配依据：MPC: secure computation

  </details>

- **Just-in-Time-OPRFs and a Modular Framework for Fast Private Set Intersection.**
  2026-07-26 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-032-35418-1_12) · [IACR ePrint](https://eprint.iacr.org/2026/1532)
  Rishabh Ranjan, Doreen Riepel, Mihir Bellare

  <details><summary>摘要 / Abstract</summary>

  This paper gives a modular and unified framework within which to derive fast protocols for Private Set Intersection (PSI). At the core of this is a new primitive, that we define, and that we call a Just-In-Time OPRF (JIT-OPRF). We show how to obtain PSI generically from any JIT-OPRF, and then how to obtain JIT-OPRFs from Oblivious Transfer (OT) and Vector Oblivious Linear Evaluation (VOLE). We recover as special cases PSI protocols in the literature based on these two assumptions. Our results and proofs throughout are concrete rather than asymptotic, with explicit bounds that allow one to determine security parameters to achieve a desired level (e.g.~128 bits) of proven security in practice. Our results show interesting differences in the concrete security of OT and VOLE based PSI. Beyond the practical contribution of concrete-security, our work adds conceptual simplicity to this area, and opens the door to new PSI protocols via the construction of new JIT-OPRFs.

  匹配依据：MPC: oblivious transfer, private set intersection

  </details>

- **PrivDNN: A Secure Multi-Party Computation Framework for Deep Learning using Partial DNN Encryption.**
  2026-07-24 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2607.21895) · [PoPETs](https://doi.org/10.56553/POPETS-2024-0089) · [Code](https://github.com/LiangqinRen/PrivDNN)
  Kaitai Liang, Zhu Li, Liangqin Ren, Zeyan Liu, Fengjun Li, Bo Luo

  <details><summary>摘要 / Abstract</summary>

  In the past decade, we have witnessed an exponential growth of deep learning models, platforms, and applications. While existing DL applications and Machine Learning as a service (MLaaS) frameworks assume fully trusted models, the need for privacy-preserving DNN evaluation arises. In a secure multi-party computation scenario, both the model and the data are considered proprietary, i.e., the model owner does not want to reveal the highly valuable DL model to the user, while the user does not wish to disclose their private data samples either. Conventional privacy-preserving deep learning solutions ask the users to send encrypted samples to the model owners, who must handle the heavy lifting of ciphertext-domain computation with homomorphic encryption. In this paper, we present a novel solution, namely, PrivDNN, which (1) offloads the computation to the user side by sharing an encrypted deep learning model with them, (2) significantly improves the efficiency of DNN evaluation using partial DNN encryption, (3) ensures model accuracy and model privacy using a core neuron selection and encryption scheme. Experimental results show that PrivDNN reduces privacy-preserving DNN inference time and memory requirement by up to 97% while maintaining model performance and privacy. Codes can be found at https://github.com/LiangqinRen/PrivDNN

  匹配依据：MPC: secure multi party computation

  </details>

- **Simultaneous-Message and Succinct Secure Computation: Reusable and Multiparty Protocols.**
  2026-07-12 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_4) · [IACR ePrint](https://eprint.iacr.org/2026/1425)
  Akshayaram Srinivasan, Abhishek Jain, David J. Wu, Siddharth Agarwal

  <details><summary>摘要 / Abstract</summary>

  Recently, Boyle, Jain, Servan-Schreiber, and Srinivasan (EUROCRYPT 2025) introduced the notion of simultaneous-message and succinct (SMS) secure computation. In an SMS protocol, after an initial sampling of a common reference string (CRS), two parties—Alice (with a large input) and Bob (with a small input)—can simultaneously exchange encodings of their private inputs and obtain additive shares of the output of a function evaluated over their inputs. The key requirement is succinctness: namely, the sizes of the CRS and each input encoding grow only polylogarithmically in the size of Alice&#x27;s input and the function output. Boyle et al., and independently Abram, Malavolta, and Roy (STOC 2025), constructed SMS for all bounded-depth Boolean circuits from the plain learning with errors (LWE) assumption. In this work, we extend the study of SMS along two new dimensions: Reusable SMS: In this setting, the same input encodings can be reused to compute multiple functions. Multiparty SMS: In the multiparty setting, we consider computations over one large input and multiple small inputs. Succinctness in this case means the size of the CRS and input encodings can grow with the total length of the small inputs (but polylogarithmically with the length of the long input and the size of the function output). Assuming polynomial hardness of LWE (with a sub-exponential modulus-to-noise ratio), we construct reusable two-party SMS for all bounded-depth Boolean circuits with polylogarithmic communication. By additionally assuming indistinguishability obfuscation, we present a generic compiler from reusable two-party SMS to reusable multiparty SMS. Our construction of reusable two-party SMS from LWE relies on a new &quot;dual-use&quot; technique where we reuse an LWE secret key between a lattice-based algebraic homomorphic MAC and a lattice-based homomorphic encryption scheme. This dual-use technique allows us to bootstrap a reusable SMS protocol for quadratic functions into one that supports arbitrary (bounded-depth) Boolean circuits. Along the way, we also show how to adapt a previous lattice-based algebraic homomorphic MAC based on ring LWE to obtain one based on the plain LWE assumption.

  匹配依据：MPC: secure computation

  </details>

- **Actively Secure MPC with O(\|C\|) Computation and Communication via CRT.**
  2026-06-17 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-032-35418-1_7) · [IACR ePrint](https://eprint.iacr.org/2026/1270)
  Daniel Escudero, Alexander Bienstock, Antigoni Polychroniadou

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) allows $n$ parties to compute a function of their private inputs, so that nothing beyond the output of the function is revealed. In the sub-optimal honest majority setting in which the number of corrupted parties $t&lt;(1/2-\varepsilon)n$, the works of Goyal et al. (CRYPTO&#x27;21 and CRYPTO&#x27;22), achieved $O(|C|)$ communication even against active adversaries, but with $\Omega(n\cdot|C|)$ computation, where $C$ is the arithmetic circuit computed by the MPC. Recent work by Garg et al. (CRYPTO&#x27;24) showed that both $O(|C|)$ communication and computation can be achieved in this regime, however, only against passive adversaries. In this work, we achieve the best-of-both-worlds by obtaining MPC with $O(|C|)$ communication and computation against active corruption of $t&lt;(1/2-\varepsilon)n$ parties. To do this, we introduce novel techniques for actively-secure MPC constructed from Chinese Remainder Theorem based secret sharing.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Unconditionally Secure MPC for Boolean Circuits with Constant Communication.**
  2026-06-07 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-032-35418-1_1) · [IACR ePrint](https://eprint.iacr.org/2026/1194)
  Yubo Zeng, Kang Yang, Min Zhang, Dengguo Feng

  <details><summary>摘要 / Abstract</summary>

  The communication complexity of unconditionally Secure Multi-Party Computation (MPC) protocols has been studied by a series of works in the honest-majority setting. For evaluating an arbitrary Boolean circuit, the state-of-the-art MPC protocol by Goyal et al. (Crypto 2021 and Crypto 2022) achieves the total communication cost of $O(\log n)$ bits per gate, where $n$ is the number of parties. In this work, we present the first unconditional MPC protocol for any Boolean circuit with communication of $O(1)$ bits per gate. We first construct an unconditionally secure protocol in the presence of semi-honest adversaries, and then strengthen it to guarantee security against malicious adversaries with the same communication efficiency.

  匹配依据：MPC: secure multi party computation

  </details>

- **On Succinct Non-interactive Secure Computation with Malicious Security.**
  2026-05-08 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_20) · [IACR ePrint](https://eprint.iacr.org/2026/909)
  Arka Rai Choudhuri, Omer Paneth, Abhishek Jain, Maya Farber Brodsky

  <details><summary>摘要 / Abstract</summary>

  A non-interactive secure computation (NISC) protocol allows a client with input $x$ and a server with input $y$ to compute $f(x,y)$ using a single message from the client and a single response from the server. The protocol is called succinct if the size of the server’s message depends only on the output length and is independent of the size of $y$ and the complexity of $f$. In the semi-honest setting, succinct NISC is known from fully homomorphic encryption (FHE). In contrast, malicious security is currently known only from non-standard assumptions, such as SNARKs for NP. In this work, we construct maliciously secure succinct NISC protocols for natural and widely studied functionalities from standard assumptions, namely, FHE and batch arguments (BARGs). Our first result is a protocol for private set membership (PSM): the client holds an element $x$, the server holds a large set $S$, and the function outputs $1$ if and only if $x \in S$. We then give several generalizations: - Dictionary lookup: The server holds a dictionary $D$ of key–value pairs, the client’s input is a key $k$, and the output is $D[k]$. - Verifiable dictionary lookup: The server’s dictionary must additionally satisfy a predicate $P$, computable by a read-once machine with small state. - UP search: The client input is an instance $x$, and the output is $D[w]$, where $w$ is the unique witness for $x$ under some UP relation. Our protocols achieve split-simulation security against a malicious server and standard security against a malicious client. Split-simulation is a relaxation of the standard real-ideal paradigm, where correctness of the client’s output and indistinguishability of the server’s view are guaranteed separately. At the heart of our results lies a new simulation technique in which the server’s large input is extracted piece by piece and reconstructed into a coherent input. This reconstruction is enabled by a new monotone coupling argument based on Strassen’s theorem.

  匹配依据：MPC: secure computation

  </details>

- **Maintaining Sublinear Locality Over Time: Adaptively Secure MPC on a Reusable Hidden Graph.**
  2026-05-08 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_19) · [IACR ePrint](https://eprint.iacr.org/2026/905)
  Elette Boyle, Ran Cohen, Pierre Meyer

  <details><summary>摘要 / Abstract</summary>

  Communication locality of an $n$-party protocol measures the maximum degree of the communication graph induced by the protocol execution. While secure multi-party computation (MPC) with small, sublinear locality exists in the static-corruption setting, this goal seems nearly paradoxical in the adaptive-corruption setting: Even against fail-stop adversaries, small neighbour sets of honest parties lie vulnerable to identification and corruption. Surprisingly, Chandran et al. [ITCS &#x27;15] showed that for a single MPC execution, sublinear locality and adaptive security can be simultaneously achieved, assuming honest-to-honest channels are hidden from the adversary. Their solution works in the ``hidden-graph model,&#x27;&#x27; where a fresh, initially hidden, low-degree graph is being used in each round. In turn, the combined degree grows with every round---inherently limiting the approach to a single-shot MPC execution, and sublinear total rounds. This raises the following question, which is the focus of our work: Is it possible to maintain sublinear locality over an unbounded number of executions facing adaptive adversaries? In this work, we provide an affirmative answer in two settings: First, we consider semi-honest adversaries and information-theoretic security, and construct reusable MPC with polylog($n$) locality. Second, we consider fail-stop adversaries and computational security, and construct reusable MPC with $\tilde O(n^{2/3})$ locality. Our results are obtained by devising low-locality protocols while hiding important information about the graph topology, enabling the parties to reuse a single hidden graph. As an independent contribution, this serves as new results for adaptively secure topology-hiding computation (Moran, Orlov, Richelson [TCC &#x27;15]).

  匹配依据：MPC: secure multi party computation

  </details>

- **Efficient Fuzzy Private Set Intersection from Secret-Shared OPRF.**
  2026-04-16 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2604.14909) · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00172)
  Meng Hao, Yonggang Wen, Xinpeng Yang, Chenkai Weng, Robert H. Deng, Tianwei Zhang

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) enables a sender holding a set $Q$ of size $m$ and a receiver holding a set $W$ of size $n$ to securely compute the intersection $Q \cap W$. Fuzzy PSI (FPSI) is a PSI variant where the receiver learns the items $q \in Q$ for which there exists some $w \in W$ satisfying $\mathsf{dist}(q, w) \le δ$ under a given distance metric. Although several FPSI works are proposed for $L_{p}$ distance metrics with $p \in [1, \infty]$, they either heavily rely on expensive homomorphic encryptions, or incur undesirable complexity, e.g., exponential to the element dimension, both of which lead to poor practical efficiency. In this work, we propose efficient FPSI protocols for $L_{p \in [1, \infty]}$ distance metrics, primarily leveraging significantly cheaper symmetric-key operations. Our protocols achieve linear communication and computation complexity in the set sizes $m,n$, the dimension $d$, and the distance threshold $δ$. Our core building block is an oblivious programmable PRF with secret-shared outputs, which may be of independent interest. Furthermore, we incorporate a prefix technique that reduces the dependence on the distance threshold $δ$ to logarithmic, which is particularly suitable for large $δ$. We implement our FPSI protocols and compare them with state-of-the-art constructions. Experimental results demonstrate that our protocols consistently and significantly outperform existing works across all settings. Specifically, our protocols achieve a speedup of $12{\sim}145\times$ in running time and a reduction of $3{\sim}8\times$ in communication cost compared to Gao et al.~(ASIACRYPT&#x27;24) and a speedup of $9{\sim}80\times$ in running time and a reduction of $5{\sim}19\times$ in communication cost compared to Dang et al.~(CCS&#x27;25).

  匹配依据：MPC: private set intersection

  </details>

- **Fast and Efficient Perfectly Secure Network-Agnostic Secure Computation.**
  2026-04-04 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_7) · [IACR ePrint](https://eprint.iacr.org/2026/655)
  Gilad Stern, Gilad Asharov, Fatima Elsheimy

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) enables mutually distrustful parties to jointly compute over private data without revealing their inputs. While protocols in both synchronous and asynchronous settings have achieved impressive efficiency in either communication or round complexity, combining the two has remained challenging. Only recently, Abraham, Asharov, Patil, and Patra (Eurocrypt’23, Eurocrypt’24) achieved protocols that combine low communication complexity ($O((Cn + Dn^2 + n^4)\log n)$) with fast execution ($O(D)$ rounds) in both synchronous and asynchronous models, for circuits of size $C$ and depth $D$, in the perfect setting with optimal resilience. However, both protocols crucially assume advanced knowledge of the network type and are fragile under mismatched or varying network conditions. The fragility of protocols under mismatched network assumptions highlights the need for network-agnostic MPC, where security and correctness are preserved in both synchronous and asynchronous settings. Yet, all known perfect network-agnostic protocols incur $\Omega(D+n)$ rounds and communication complexity in the order of $n^3$ or higher, far worse than their network-specific counterparts. In this work, we present the first network-agnostic MPC protocol in the perfect security setting, achieving expected round complexity $O(D)$. Our protocol has expected communication complexity $O((Cn^2 + Dn^2 + n^4)\log n)$, improving on the state of the art by a factor of $n^3$ for small circuits and $n^2$ for large circuits in communication, in addition to an additive $O(n)$ improvement in round complexity. Our design departs from the structure of prior network-agnostic protocols and introduces several new technical ideas that enable both round and communication efficiency.

  匹配依据：MPC: secure computation, secure multiparty computation

  </details>

- **Oblivis: A Framework for Delegated and Efficient Oblivious Transfer.**
  2026-03-15 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2603.14492) · [PoPETs](https://doi.org/10.56553/POPETS-2026-0104)
  Aydin Abadi, Yvo Desmedt

  <details><summary>摘要 / Abstract</summary>

  As database deployments shift toward cloud platforms and edge devices, thin clients need to securely retrieve sensitive records without leaking their query intent or metadata to the proxies that mediate access. Oblivious Transfer (OT) is a core tool for private retrieval, yet existing OTs assume direct client-database interaction and lack support for delegated querying or lightweight clients. We present Oblivis, a modular framework of new OT protocols that enable delegated, privacy-preserving query execution. Oblivis allows clients to retrieve database records without direct access, protects against leakage to both databases and proxies, and is designed with practical efficiency in mind. Its components include: (1) Delegated-Query OT, which permits secure outsourcing of query generation; (2) Multi-Receiver OT for merged, cloud-hosted databases; (3) a compiler producing constant-size responses suitable for thin clients; and (4) Supersonic OT, a proxy-based, informationtheoretic, and highly efficient 1-out-of-2 OT. The protocols are formally defined and proven secure in the simulation-based paradigm, under non-colluding assumption. We implement and empirically evaluate Supersonic OT. It achieves at least a 92x speedup over a highly efficient 1-out-of-2 OT, and a 2.6x-106x speedup over a standard OT extension across 200-100,000 invocations. Our implementation further shows that Supersonic OT remains efficient even on constrained hardware, e.g., it completes an end-to-end transfer in 1.36 ms on a Raspberry Pi 4.

  匹配依据：MPC: oblivious transfer

  </details>

- **PUFF: Maximally Proactive Security for Free in Perfectly Secure MPC with Guaranteed Output Delivery.**
  2026-03-12 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_18) · [IACR ePrint](https://eprint.iacr.org/2026/509)
  Jiarui Li, Mengzhen Zou, Guoyan Zhang, Guidong Li, Chen Qian

  <details><summary>摘要 / Abstract</summary>

  Achieving proactive security in perfectly-secure Multi-Party Computation (MPC) with guaranteed output delivery is a significant challenge, primarily because traditional protocols require all participants to be continuously online, rendering them impractical for many applications. The recently proposed layered MPC model~\cite{C:DDGIKK23} addresses this by allowing parties to be offline for extended periods. However, existing protocols for this model incur substantial overhead compared to their counterparts in the standard static setting. This work introduces a unified framework and essential building blocks for constructing protocols in the layered model, instantiable with both Shamir and CNF secret sharing. Using this framework, we develop highly efficient protocols for Verifiable Secret Sharing (VSS) and secure multiplication for proactive security. Applying our framework, we construct layered MPC protocols that drastically reduce the communication complexity and the number of layers required to evaluate an arithmetic circuit of depth $D$. Specifically, our Shamir-based MPC achieves $O(n^6)$ per-gate communication with a total layer depth of $D+13$, representing a significant improvement over the $O(n^9)$ complexity and $10D+8$ depth of~\cite{C:DDGIKK23}.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Scaling Fully Secure MPC via Robust Recursive Search and Gap Amplification.**
  2026-03-07 · MPC · 含会议/期刊记录 · [PKC](https://doi.org/10.1007/978-3-032-26734-4_10) · [IACR ePrint](https://eprint.iacr.org/2026/475)
  Matan Hamilis, Ariel Nof

  <details><summary>摘要 / Abstract</summary>

  We present a new framework for secure computation of arithmetic circuits with two-thirds honest majority that lifts semi-honest protocols to full malicious security. Our framework works with any linear secret sharing over any finite ring and maintains the type of security of the underlying semi-honest protocol (i.e., computational or information-theoretic). The framework has the following overhead complexity with respect to size \(|C|\) of the computed circuit \(C\): it incurs only logarithmic communication overhead in \(|C|\) over the cost of the semi-honest protocol, the number of additional rounds is independent of the circuit&#x27;s size, and the computational work per party is \(O(|C|)\) arithmetic operations. Even when limiting the scope to static adversaries, previous works could only achieve two of these three measures: Either the communication is logarithmic and the computational overhead per party is \(O(|C|)\), but the number of additional rounds grows with the circuit&#x27;s size, or communication is logarithmic and the number of rounds is \(O(n)\), but the computational overhead is \(O(n\cdot |C|)\). To the best of our knowledge, we are the first to achieve the desired complexity in all three fronts, making the cost of achieving full security in MPC lower than ever. Our result is achieved via a new verification technique based on a robust recursive search that finds and removes cheaters from the computation. We further improve our result by reducing costs associated with the number of parties~\(n\). While the initial result incurs cubic communication overhead with respect to \(n\) and \(O(n)\) additional rounds in the worst case, we show how to reduce it to \(\sqrt{n^5}\) communication overhead and \(O(\sqrt{n\log\log n})\) additional rounds, without sacrificing the computational overhead, which remains \(O(|C|)\). This is achieved via a novel technique we call gap amplification that accelerates the player elimination process, enabling us to reduce the number of calls to the verification subprotocol. This technique is of independent interest as it is general and can be directly applied to any protocol that relies on player elimination.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Updatable Private Set Intersection from Symmetric-Key Techniques.**
  2026-03-04 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25317-0_13) · [IACR ePrint](https://eprint.iacr.org/2026/438)
  Junxin Liu, Xinyi Shi, Peihan Miao, Jifeng Wang, Mike Rosulek

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) has become extremely practical, in large part due to the fact that modern protocols rely almost exclusively on cheap, symmetric-key cryptography. The same cannot be said for the variant of PSI called updatable PSI (UPSI; Badrinarayanan et al., PoPETS 2022), where parties’ input sets evolve over time, and the cost of re-computing the intersection depends only on the changes to their sets. In existing UPSI protocols, the number of public-key operations scales with the number of items. In this work, we introduce the first UPSI protocol that largely avoids public-key operations. In fact, our protocol uses mostly the same protocol tools/techniques that have been so successful in making (plain) PSI truly practical. By leveraging symmetric-key primitives, our implementation achieves orders-of-magnitude improvements over prior work. Additionally, we observe that existing UPSI security proofs do not consider an adversary who can choose protocol inputs adaptively (i.e., choose which items to add to the set the current epoch based on the adversary’s view in previous epochs). We observe that several existing UPSI protocols are trivially broken by such adaptive input selection (even with semi-honest corruption). Several variants of our protocol are secure in the presence of adaptively chosen inputs. Along the way, we also introduce a new and cleaner abstraction for a common idiom of using an oblivious key-value store (OKVS; Garimella et al., Crypto 2021) to represent a set of items. Our new abstraction, called affine set encoding, may be of independent interest.

  匹配依据：MPC: private set intersection

  </details>

- **Perfectly Secure Network-Agnostic MPC Comes for Free.**
  2026-02-24 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_12) · [IACR ePrint](https://eprint.iacr.org/2026/377)
  Xiaoyu Ji, Chen-Da Liu-Zhang, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) allows a set of parties to jointly compute a function while keeping their inputs private. Classical MPC protocols assume either a synchronous or an asynchronous network. Synchronous protocols tolerate more corrupted parties but rely on a timing bound, while asynchronous protocols make no timing assumptions but handle fewer corruptions. The network-agnostic model aims to combine the advantages of both. It requires security without knowing in advance whether the network is synchronous or asynchronous, guaranteeing resilience against up to $t_s$ corruptions in the synchronous case and $t_a$ corruptions in the asynchronous case. The optimal corruption threshold for perfect security has been established as $n = 2\max(t_s, t_a) + \max(2t_a, t_s) + 1$, but prior work either falls short of this threshold or requires exponential local computation. In this work, we present the first perfectly secure network-agnostic MPC protocol with polynomial communication and computation complexity under the optimal threshold. Our protocol achieves expected communication complexity $\mathcal{O}((|C|n + (D+C_I)n^2 + n^6)\log n)$ bits for a circuit of size $|C|$ over a finite field $\mathbb{F}$ of size $\mathcal{O}(n)$, depth $D$, and input size $C_I$. Our main technical contribution is a compiler that generates Beaver triples in the network-agnostic setting using synchronous and asynchronous triple-generation protocols in a black-box way. Beyond the cost of the underlying protocols, it only requires $\mathcal{O}(n^2)$ instances of network-agnostic Byzantine agreement.

  匹配依据：MPC: secure multiparty computation

  </details>

- **Dishonest-Majority Secure Computation via PIR-Authenticated Multiplication Triples.**
  2026-02-13 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-032-35418-1_15) · [IACR ePrint](https://eprint.iacr.org/2026/257)
  Matan Hamilis, Yuval Ishai, Ariel Nof, Elette Boyle, Niv Gilboa

  <details><summary>摘要 / Abstract</summary>

  We revisit the question of minimizing the overhead of security against malicious parties in dishonest-majority secure computation. A leading approach, pioneered by the SPDZ line of protocols, uses homomorphic MACs to authenticate computation: Parties effectively compute a MAC on the computation output using authenticated multiplication triples (AMT). However, securely generating these AMTs presently sits as the cost bottleneck. In this work, we introduce a new technique for enabling SPDZ-style verification via homomorphic MACs, while bypassing the need for AMT. We instead rely on the specific structure of state-of-the-art fast pseudorandom correlation generators (PCG) for generating standard (unauthenticated) multiplication triples (MT). Parties authenticate the computation result via an authenticated variant of private information retrieval (PIR), relying on the sparse representation of MT produced by these PCGs. This opens the door to a wide range of PIR optimizations and tradeoffs from the literature, resulting in asymptotic and concrete improvements over the traditional AMT-based approach. For example, in the Boolean 2-party case with \(\sigma=40\), we get a \(3\times\) to \(8\times\) computation improvement (and comparable communication) over best approaches using PCG to generate AMT, where the latter exploits variants of the Stationary Syndrome Decoding assumption of Kolesnikov et al. (Crypto 2025). With \(m\ge 3\) parties we obtain even larger improvements while reducing the asymptotic dependence on \(m\) from cubic to quadratic.

  匹配依据：MPC: secure computation

  </details>

- **Malicious Private Set Union with Two-Sided Output.**
  2026-02-09 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25317-0_14) · [IACR ePrint](https://eprint.iacr.org/2026/204)
  Ni Trieu, Sihang Pu, Jiahui Gao

  <details><summary>摘要 / Abstract</summary>

  Private Set Union (PSU) allows two parties to compute the union of their private sets without revealing any additional information---in particular, it hides their common elements (the intersection). Although recent years have seen significant progress under the semi-honest model, resulting in several efficient two-party PSU protocols, notable gaps remain: (1) some prior works model the semi-honest PSU functionality inaccurately, and (2) practical and scalable maliciously secure protocols are still lacking, except when relying on heavy generic techniques (e.g., FHE, GMW, or general purpose NIZK). In this paper, we address these issues directly and summarize our contributions as follows: 1. We revisit the formal definition of PSU, covering both the standard one-sided functionality (where only one party receives the output) and the two-sided variant (where both parties receive the output), refuting several flawed claims from prior work, and show that the notion of ``during-execution leakage&#x27;&#x27; was not well-defined in the literature, since the ``enhanced&#x27;&#x27; functionality is actually equivalent to the standard one. 2. We show how one of the fastest semi-honest protocols can be strengthened against malicious senders with a simple ad-hoc modification, while preserving its efficiency and simplicity. 3. As our main result, we present the first practical, concretely efficient, and maliciously secure two-sided PSU protocol, achieving at least a quadratic improvement over prior work. Along the way, we also resolve the challenge of assuring honest behavior for the hash-to-curve function in the PSU context---a task generally regarded as impractical due to the non-algebraic nature of the hash function. 4. We implement both protocols and compare them with existing schemes. Our experiments demonstrate that our maliciously secure protocols are only ${1.1\!-\!2.4}\times$ slower than the most efficient semi-honest protocols in the literature.

  匹配依据：MPC: private set union

  </details>

- **cwPSU: Efficient Unbalanced Private Set Union via Constant-weight Codes.**
  2026 · MPC · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/cwpsu-efficient-unbalanced-private-set-union-via-constant-weight-codes/)
  Song Bian, Hui Li, Qingwen Li

- **Updatable Multi-Party Private Set Intersection for Real-Time Collaborative Threat Intelligence.**
  2026 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2026.3707440)
  Zhongming Wang, Biwen Chen, Xiaoguo Li, Ze Jiang, Di Zhang, Xiaofeng Liao, Tao Xiang

- **Universally Composable Almost-Everywhere Secure Computation.**
  2026 · MPC · 含会议/期刊记录 · [Journal of Cryptology](https://doi.org/10.1007/S00145-025-09565-2) · [IACR ePrint](https://eprint.iacr.org/2021/1398)
  Juan A. Garay, Rutvik Patel, Pouyan Forghani, Nishanth Chandran, Rafail Ostrovsky, Vassilis Zikas, Juan Garay

  <details><summary>摘要 / Abstract</summary>

  Most existing work on secure multi-party computation (MPC) ignores a key idiosyncrasy of modern communication networks, that there are a limited number of communication paths between any two nodes, many of which might even be corrupted. The problem becomes particularly acute in the information-theoretic setting, where the lack of trusted setups (and the cryptographic primitives they enable) makes communication over sparse networks more challenging. The work by Garay and Ostrovsky [EUROCRYPT&#x27;08] on almost-everywhere MPC (AE-MPC), introduced ``best-possible security&#x27;&#x27; properties for MPC over such incomplete networks, where necessarily some of the honest parties may be excluded from the computation. In this work, we provide a universally composable definition of almost-everywhere security, which allows us to automatically and accurately capture the guarantees of AE-MPC (as well as AE-communication, the analogous ``best-possible security&#x27;&#x27; version of secure communication) in the Universal Composability (UC) framework of Canetti. Our results offer the first simulation-based treatment of this important but under-investigated problem, along with the first simulation-based proof of AE-MPC. To achieve that goal, we state and prove a general composition theorem, which makes precise the level or ``quality&#x27;&#x27; of AE-security that is obtained when a protocol&#x27;s hybrids are replaced with almost-everywhere components.

  匹配依据：MPC: secure computation, secure multi party computation

  </details>

- **UFOs: An Ultra-Fast Toolkit for Multiparty Computation on Small Elements.**
  2026 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2026.3734714)
  Yuan Zhang, Moyang Xie, Sheng Zhong, Jiacheng Gao

- **Traceable Secret Sharing Schemes for General Access Structures.**
  2026 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_1) · [IACR ePrint](https://eprint.iacr.org/2025/1120)
  Miquel Guiot, Oriol Farràs

  <details><summary>摘要 / Abstract</summary>

  Traceable secret sharing complements traditional schemes by enabling the identification of parties who sell their shares. In the model introduced by Boneh, Partap, and Rotem [CRYPTO’24], a group of corrupted parties generates a reconstruction box $R$ that, given enough valid shares as input, reconstructs the secret. The goal is to trace $R$ back to at least one of the corrupted parties using only black-box access to it. While their work provides efficient constructions for threshold access structures, it does not apply to the general case. In this work, we extend their framework to general access structures and present an information-theoretic traceable scheme supporting them. In the course of our construction, we also contribute to the study of anonymous secret sharing, a notion recently introduced by Bishop et al. [CRYPTO’25], which strengthens classical secret sharing by requiring that shares do not reveal the identities of the parties holding them. We further advance this area by proposing new and stronger definitions, and presenting an anonymous scheme for general access structures that satisfies them.

  匹配依据：MPC: secret sharing

  </details>

- **Traceable Secret Sharing Revisited.**
  2026 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_2) · [IACR ePrint](https://eprint.iacr.org/2025/1980)
  Abhishek Jain, Vipul Goyal, Aditi Partap

  <details><summary>摘要 / Abstract</summary>

  In a secret sharing scheme for a monotone access structure $\mathcal{A}$, one can share a secret among a set of parties such that all subsets of parties authorized by $\mathcal{A}$ can reconstruct the secret while all other subsets learn nothing. However, what if an unauthorized subset of parties collude and offer their shares for sale? Specifically, suppose that the parties pool their shares to create a reconstruction box that reveals the secret upon receiving enough additional shares as input. To deter this behavior, Goyal et al. (CRYPTO&#x27;21) introduced the notion of traceable secret sharing (TSS), where it is possible to provably trace reconstruction boxes containing leaked secret shares back to their respective parties. Goyal et al. and subsequent work presented definitions and constructions of TSS for the threshold access structure. In this work, we revisit the notion of TSS. - We identify shortcomings in previous formulations of TSS and present new, strengthened definitions that are not achieved by known constructions. We show that it is easy to build reconstruction boxes for which the tracing guarantees of all previous works fail. - We extend the study of TSS beyond threshold to general access structures. Our new definitions are, in fact, necessary for this setting as natural adaptations of existing definitions become vacuous for general access structures. - We present new constructions of TSS that satisfy our definitions for all access structures captured by monotone circuits. One of our constructions relies solely on one-way functions while the other additionally relies on indistinguishability obfuscation.

  匹配依据：MPC: secret sharing

  </details>

- **Towards Scalable YOSO MPC via Packed Secret-Sharing.**
  2026 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-981-95-5116-3_3) · [IACR ePrint](https://eprint.iacr.org/2025/635)
  Daniel Escudero, Elisaweta Masserova, Antigoni Polychroniadou

  <details><summary>摘要 / Abstract</summary>

  The YOSO (You Only Speak Once) model, introduced by Gentry et al. (CRYPTO 2021), helps to achieve strong security guarantees in cryptographic protocols for distributed settings, like blockchains, with large number of parties. YOSO protocols typically employ smaller anonymous committees to execute individual rounds of the protocol instead of having all parties execute the entire protocol. After completing their tasks, parties encrypt protocol messages for the next anonymous committee and erase their internal state before publishing ciphertexts, thereby enhancing security in dynamically changing environments. In this work, we consider the problem of secure multi-party computation (MPC), a fundamental problem in cryptography and distributed computing. We assume honest majority among the committee members, and work in the online-offline, i.e., preprocessing, setting. In this context, we present the first YOSO MPC protocol where efficiency---measured as communication complexity---improves as the number of parties increases. Specifically, for $0 0$, the sizes of the committees are only marginally increased, while online communication is significantly reduced. Furthermore, we explicitly consider fail-stop adversaries, i.e., honest participants who may inadvertently fail due to reasons such as denial of service or software/hardware errors. In prior YOSO work, these adversaries were grouped with fully malicious parties. Adding explicit support for them allows us to achieve even better scalability.

  匹配依据：MPC: secret sharing, secure multi party computation

  </details>

- **Threshold Homomorphic Secret Sharing: Definitions and Constructions.**
  2026 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-981-95-5119-4_18)
  Junqing Gong, Rupeng Yang, Shifeng Sun, Xinzhou Wang, Yuan Luo, Dawu Gu

- **Taming Adaptive Security and New Access Structures in Evolving Secret Sharing.**
  2026 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-981-95-5125-5_3)
  Sara Giammusso, Danilo Francati, Daniele Venturi

- **Succinct Line-Point Zero-Knowledge Arguments from Homomorphic Secret Sharing.**
  2026 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-981-95-5116-3_19) · [IACR ePrint](https://eprint.iacr.org/2025/1866)
  Zhe Li, Mengmeng Zhou, Yizhou Yao, Chaoping Xing, Chen Yuan

  <details><summary>摘要 / Abstract</summary>

  Dittmer, Ishai and Ostrovsky (ITC&#x27;21) proposed {\em line-point zero-knowledge proof} (LPZK), a simple ``commit-and-prove&#x27;&#x27; system, motivated by practical protocols for compressing correlated pseudorandomness used in secure multiparty computation (MPC). Typically, LPZK admits concretely efficient ZK protocols with a streaming, linear time prover, {\em but a linear size proof}. A natural question raised in the context is how far can we go in minimizing the proof size, while maintaining the prover efficiency. Though a recent work by Lin, Xing and Yao (ASIACRYPT&#x27;24) gives an interactive LPZK with a sublinear proof size $O(n+d^2\log{|\mathcal{C}|})$, it is still far from being {\em succinct}, where $n,d,|\mathcal{C}|$ are referred to as input size, circuit depth, and circuit size, respectively. In this work, we beat the proof size barrier and propose {\em succinct LPZK arguments}, by distilling techniques from orthogonal studies on homomorphic secret sharing and succinct garbling. Specifically, under variants of group/lattice-based assumptions, we show the followings: i) There exist succinct LPZK arguments with common reference string (CRS) size $O(n^{2/3})$, proof size $O(n^{2/3})$, prover time $O(n^{4/3}+|\mathcal{C}|)$, verification time $O(n+|\mathcal{C}|)$, and negligible soundness error, where both the prover and the verifier executions and be run in a streaming fashion. ii) The above proof size can be further optimized to $O(1)$, at the cost of a larger CRS size $O(n)$, and prover time increased to $O(n^{2}+|\mathcal{C}|)$. In general, our succinct LPZK arguments pave a new way for building designated-verifier zero-knowledge succinct non-interactive arguments of knowledge (dv-zkSNARKs), and new interesting features (e.g., streaming, constant sized proof with CRS size not proportional to the circuit size) are obtained for the first time along the way.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Succinct Garbled Circuits with Low-Depth Garbling Algorithms.**
  2026 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_9) · [IACR ePrint](https://eprint.iacr.org/2025/2308)
  Huijia Lin, Hanjun Li, George Lu

  <details><summary>摘要 / Abstract</summary>

  We study the problem of constructing Boolean garbling schemes that are both succinct$-$with garbled circuit size significantly smaller than the original circuit$-$and have low-depth garbling algorithms, where the garbling process runs in parallel time logarithmic in the circuit size. Prior schemes achieve one but not the other, unless relying on indistinguishability obfuscation ($\mathsf{iO}$), which is prohibitively inefficient, relies on a combination of multiple assumptions, and achieves only polynomial garbling depth $\mathsf{poly}(\lambda,\log |C|)$. We resolve this tension by presenting the first garbling schemes that are both succinct and admit garbling algorithms in $\mathsf{NC}^1$, based only on standard group and lattice assumptions. Our main results include: • $\textbf{One-bit-per-gate garbling}$ with logarithmic garbling depth based on DDH or RLWE and the existence of a local PRG. • $\textbf{Succinct privacy-free garbling}$ of size linear in the circuit depth $D$ (and sublinear in the circuit size $|C|$), based on DDH or RLWE. • $\textbf{Reusable, fully succinct garbling}$ with logarithmic garbling depth, based on decomposable LWE. The DDH-based one-bit-per-gate scheme has tunably small inverse polynomial correctness and privacy errors, which can be made negligible at the cost of increasing garbling depth to $\mathsf{poly}(\lambda)$. As further extension, we also obtain the first attribute-based encryption schemes with succinct keys and low-depth key generation. At a conceptual level, our constructions are derived from a unified framework that subsumes all prior approaches to succinct garbling. It identifies the common source of high-depth garbling, and provides a general methodology for reducing garbling depth without sacrificing succinctness, applicable across different techniques and assumptions.

  匹配依据：MPC: garbled circuit, garbled circuits, garbling schemes

  </details>

- **Succinct Computational Secret Sharing for Monotone Circuits.**
  2026 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-981-95-5125-5_4) · [IACR ePrint](https://eprint.iacr.org/2025/850)
  Shafik Nassar, George Lu, Brent Waters

  <details><summary>摘要 / Abstract</summary>

  Secret sharing is a cornerstone of modern cryptography, underpinning the secure distribution and reconstruction of secrets among authorized participants. In these schemes, succinctness—measured by the size of the distributed shares—has long been an area of both great theoretical and practical interest, with large gaps between constructions and best known lower bounds. In this paper, we present a novel computational secret sharing scheme for monotone Boolean circuits that achieves substantially shorter share sizes than previously known constructions in the standard model. Our scheme attains a public share size of $n + \mathsf{poly}(\lambda, \log |C|)$ and a user share size of $\lambda$, where n denotes the number of users, $C$ is the monotone circuit and $\lambda$ is the security parameter, thus effectively eliminating the dependence on the circuit size. This marks a significant improvement over earlier approaches, which exhibited share sizes that grew with the number of gates in the circuit. Our construction makes use of indistinguishability obfuscation and injective one-way functions.

  匹配依据：MPC: secret sharing

  </details>

- **Statistically Secure Asynchronous MPC with Linear Communication and 풪(n5) Additive Overhead.**
  2026 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-032-35418-1_2)
  Yifan Song, Xiaoyu Ji

- **Simplified PIR and CDS Protocols and Improved Linear Secret-Sharing Schemes.**
  2026 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-032-12293-3_12) · [IACR ePrint](https://eprint.iacr.org/2024/1599)
  Bar Alon, Or Lasri, Amos Beimel

  <details><summary>摘要 / Abstract</summary>

  We consider 3 related cryptographic primitives, private information retrieval (PIR) protocols, conditional disclosure of secrets (CDS) protocols, and secret-sharing schemes; these primitives have many applications in cryptography. We study these primitives requiring information-theoretic security. The complexity of the three primitives has been dramatically improved in the last few years and they are closely related, i.e., the 2-server PIR protocol of Dvir and Gopi (J. ACM 2016) was transformed to construct the CDS protocols of Liu, Vaikuntanathan, and Wee (CRYPTO 2017, Eurocrypt 2018) and these CDS protocols are the main ingredient in the construction of the best-known secret-sharing schemes. To date, the message size required in PIR and CDS protocols and the share size required in secret-sharing schemes are not understood and there are big gaps between their upper bounds and lower bounds. The goal of this paper is to try to better understand the upper bounds by simplifying current constructions and supplying tools for improving their complexity. We obtain the following results: - We simplify, abstract, and generalize the 2-server PIR protocol of Dvir and Gopi (J. ACM 2016), the recent multi-server PIR protocol of Ghasemi, Kopparty, and Sudan (STOC 2025), and the 2-server and multi-server CDS protocols of Liu et al.\ (CRYPTO 2017, Eurocrypt 2018) and Beimel, Farr\`as, and Lasri (TCC 2023). In particular, we present one PIR protocol generalizing both the 2-server and multi-server PIR protocols using general share conversions. For $k\geq 3$ servers, our main contribution is a simpler proof the correctness of the protocol, avoiding the partial derivatives and interpolation polynomials used by Ghasemi et al. - In addition to simplifying previous protocols, our 2-server protocols can use a relaxed variant of matching vectors over any $m$ that is the product of two distinct primes. Our constructions do not improve the communication complexity of PIR and CDS protocols; however, construction of better relaxed matching vectors over \emph{any} $m$ that is the product of two distinct primes will improve the communication complexity of $2$-server PIR and $2$-server CDS protocols. - In many applications of secret-sharing schemes it is important that the scheme is linear, e.g., by using the fact that parties can locally add shares of two secrets and obtain shares of the sum of the secrets. In an independent result, we provide a construction of linear secret-sharing schemes for $n$-party access structures with improved share size of $2^{0.7563n}$. Previously, the best share size for linear secret-sharing schemes was $2^{0.7576n}$ and it is known that for most $n$-party access structures the shares&#x27; size is at least $2^{0.5n}$. This result is achieved by a reduction to unbalanced CDS protocols (compared to balanced CDS protocols in previous constructions).

  匹配依据：MPC: secret sharing

  </details>

- **Secure Computation Over Gaussian Multiple-Access Wiretap Channels With Feedback.**
  2026 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2026.3715114)
  Han Deng, Bin Dai, Yuhan Yang, Fan Cheng, Haoheng Yuan, Chao Qi

- **Secure Computation Against NC1 Leakage Without Secure Hardware.**
  2026 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-032-35415-0_10)
  Yuyu Wang

- **Secret Sharing Schemes From Correlated Random Variables and Rate-Limited Public Communication.**
  2026 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2505.04076) · [TIFS](https://doi.org/10.1109/TIFS.2026.3657030)
  Rumia Sultana, Remi A. Chou

  <details><summary>摘要 / Abstract</summary>

  A dealer aims to share a secret with participants so that only predefined subsets can reconstruct it, while others learn nothing. The dealer and participants access correlated randomness and communicate over a one-way, public, rate-limited channel. For this problem, we propose the first explicit coding scheme able to handle arbitrary access structures and achieve the best known achievable rates, previously obtained non-constructively. Our construction relies on lossy source coding coupled with distribution approximation to handle the reliability constraints, followed by universal hashing to handle the security constraints. We stress that our coding scheme does not require symmetry or degradation assumptions on the correlated random variables, and does not need a pre-shared secret among the participants and dealer. As a by-product, our construction also yields explicit coding schemes for secret-key generation under one-way, rate-limited public communication that, unlike prior work, achieves the capacity for arbitrary source correlations and do not require a pre-shared secret to ensure strong secrecy.

  匹配依据：MPC: secret sharing

  </details>

- **SecP-Tuning: Efficient Privacy-Preserving Prompt Tuning for Large Language Models via MPC.**
  2026 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2506.15307) · [ICLR](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7f2e5d16c2c5ac161ce7aa44af35c0fe-Abstract-Conference.html)
  Zhuo Zhang, Xun Zhou, Yehong Zhang, Shiyu Liu, Jinglong Luo, Ye Dong, Hui Wang, Zenglin Xu, Yue Yu

  <details><summary>摘要 / Abstract</summary>

  Large Language Models (LLMs) have revolutionized numerous fields, yet their adaptation to specialized tasks in privacy-sensitive domains such as healthcare and finance remains constrained due to the scarcity of accessible training data caused by stringent privacy requirements. Secure Multi-party Computation (MPC)-based privacy-preserving machine learning provides theoretical guarantees for the privacy of model parameters and data. However, its application to LLMs has been predominantly limited to inference, as fine-tuning introduces significant efficiency challenges, particularly in backward propagation, optimizer, and self-attention operations. To address these challenges, we propose SecP-Tuning, the first MPC-based framework designed for efficient, privacy-preserving prompt tuning of LLMs. SecP-Tuning innovatively integrates Forward-only Tuning (FoT) through the ``data owner-server interaction&quot; paradigm, effectively removing the need for privacy-preserving computations in backward propagation and optimization processes. Furthermore, it devises an efficient privacy-preserving Random Feature Attention (RFA), effectively mitigating the computational complexity of softmax-based self-attention and circumventing MPC-incompatible nonlinear operations. Experimental results demonstrate that, compared to full-Parameter Supervised Fine-Tuning (SFT) and gradient-based prompt tuning, SecP-Tuning achieves approximately 12x and 16x end-to-end acceleration, as well as 17x and 20x reductions in communication overhead, respectively. Moreover, it delivers performance comparable to gradient-based methods across multiple few-shot tasks.

  匹配依据：MPC: secure multi party computation

  </details>

- **SecOIR: Enhancing Privacy and Accuracy in Outsourced Image Retrieval via Function Secret Sharing and Deep Hashing.**
  2026 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2025.3628356)
  Zhi Li, Hao Wang, Xiaochao Wei, Ye Su, Lei Wu, Wenying Zhang

- **Scalable Privacy-Preserving Shortest Path Distance Computation via 2-Hop Labeling in MPC.**
  2026 · MPC · 含会议/期刊记录 · [PACMMOD / SIGMOD](https://doi.org/10.1145/3786695)
  Huizhong Wang, Kun Chen, Chenhao Ma, Yuanyuan Zeng, Wei Dong

- **RoundRole: Unlocking the Efficiency of Multi-party Computation with Bandwidth-aware Execution.**
  2026 · MPC · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/roundrole-unlocking-the-efficiency-of-multi-party-computation-with-bandwidth-aware-execution/)
  Kun Chen, Wei Xu, Jiping Yu, Yunyi Chen, Xiaoyu Fan, Xin Liu

- **Randomized Agreement, Verifiable Secret Sharing and Multi-party Computation in Granular Synchrony.**
  2026 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-981-95-5116-3_1) · [IACR ePrint](https://eprint.iacr.org/2025/1327)
  David Heath, Ananya Appan, Ling Ren

  <details><summary>摘要 / Abstract</summary>

  Granular Synchrony (Giridharan et al. DISC 2024) is a new network model that unifies the classic timing models of synchrony and asynchrony. The network is viewed as a graph consisting of a mixture of synchronous, eventually synchronous, and asynchronous communication links. It has been shown that Granular Synchrony allows deterministic Byzantine agreement protocols to achieve a corruption threshold in between complete synchrony and complete asynchrony if and only if the network graph satisfies the right condition, namely, that no two groups of honest parties of size $n-2t$ can be partitioned from each other. In this work, we show that the same network condition is also tight for Agreement on a Common Subset (ACS), Verifiable Secret Sharing (VSS), and secure Multi-Party Computation (MPC) with guaranteed output delivery, when the corruption threshold is between one-third and one-half. Our protocols are randomized and assume that all links are either synchronous or asynchronous. %(no partially synchronous links are needed). Our ACS protocol incurs an amortized communication cost of $O(n^3\lambda)$ bits per input, and our VSS and MPC protocols incur amortized communication costs of $O(n^3)$ and $O(n^4)$ field elements per secret and per multiplication gate, respectively. To design our protocols, we also construct protocols for Reliable Broadcast and Externally Valid Byzantine Agreement (EVBA), which are of independent interest.

  匹配依据：MPC: multi party computation, secret sharing, secure multi party computation

  </details>

- **Pseudorandom Correlation Functions for Garbled Circuits.**
  2026 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-032-12293-3_15) · [IACR ePrint](https://eprint.iacr.org/2025/2325)
  Srini Devadas, Geoffroy Couteau, Sacha Servan-Schreiber, Alexander Koch, Srinivas Devadas

  <details><summary>摘要 / Abstract</summary>

  In this paper, we define the notion of pseudorandom correlation generators (PCGs) and functions (PCFs) for garbled circuit correlations. With a Garbling PCG or PCF, two parties can non-interactively generate a virtually unbounded number of secret-shared garbled circuits and corresponding secret-shared garbled inputs. With the shares of the garbled circuit and garbled input, anyone can recover the garbled circuit and evaluate it to obtain the result of the computation in the clear. In the process of constructing Garbling PCFs, we introduce a new primitive that we call a Topology-Adaptive PCF (TAPCF), which we construct from two different variants of the learning parity with noise (LPN) assumption. Informally, a TAPCF is a PCF that additionally allows the target correlation to be specified on-demand (i.e., at evaluation time). As a contribution of independent interest, we show that TAPCFs enable the first silent secure computation protocol with function-dependent silent preprocessing. Using our TAPCF construction as a building block, we construct a Garbling PCF that allows the parties to specify the circuit they wish to garble on the fly. Under realistic parameter settings, we estimate that, with our construction, two parties can generate one garbled circuit per second, for circuits with 10,000 AND gates. Garbling PCFs have several applications: We provide constructions for (1) an efficient homomorphic secret-sharing scheme for specific high-depth circuits, (2) a zero-knowledge proof system over secret shares that supports checking unstructured languages, and (3) a semi-honest reusable two-round, two-party computation protocol supporting non-interactive public outputs.

  匹配依据：MPC: garbled circuit, garbled circuits, secret sharing, secure computation, two party computation

  </details>

- **Privacy-Preserving Continuous Authentication of Smartphone Users via Secret Sharing.**
  2026 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2026.3680150)
  Mingming Hu, Ding Wang, Daojun Han, Bibo Tu, Jingtao Guo

- **PriFFT: Privacy-Preserving Federated Fine-Tuning of Large Language Models via Hybrid Secret Sharing.**
  2026 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2503.03146) · [TDSC](https://doi.org/10.1109/TDSC.2026.3661572)
  Ke Cheng, Qiang Qu, Zhichao You, Jiaxuan Fu, Xutong Mu, Shiyang Ma, Yulong Shen, Xuewen Dong

  <details><summary>摘要 / Abstract</summary>

  Fine-tuning large language models (LLMs) raises privacy concerns due to the risk of exposing sensitive training data. Federated learning (FL) mitigates this risk by keeping training samples on local devices, while facing the following problems in privacy-preserving federated fine-tuning. (i) Recent studies show that adversaries can still infer private information in FL. (ii) LLM parameters are shared publicly during federated fine-tuning, while developers are often reluctant to disclose these parameters, posing further security challenges. (iii) Existing works focus on secure inference of LLMs but do not consider privacy-preserving fine-tuning. Inspired by the above problems, we propose PriFFT, a privacy-preserving federated fine-tuning mechanism, to protect both the model parameters and users&#x27; privacy. Due to considerable LLM parameters, we present hybrid secret sharing combining arithmetic secret sharing (ASS) and function secret sharing (FSS) to build secure operations and implement secure layers and activation for privacy-preserving fine-tuning. To improve the efficiency of privacy-preserving federated fine-tuning of LLMs, we optimize several secure computation protocols based on FSS, including reciprocal calculation, tensor products, natural exponentiation, softmax, sigmoid, hyperbolic tangent, and dropout. The hybrid secret sharing enables PriFFT to apply our optimized FSS protocols while combining ASS protocols to support complex computation without extra communication. The optimized protocols reduce execution time up to 62.5% and communication overhead up to 70.7% compared to existing protocols. Besides, PriFFT reduces execution time and communication overhead in privacy-preserving fine-tuning up to 59.1%$ and 77.0%$ without accuracy drop compared to the existing secret sharing methods.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Practical Traceable Over-Threshold Multi-Party Private Set Intersection.**
  2026 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2512.24652) · [NDSS](https://www.ndss-symposium.org/ndss-paper/practical-traceable-over-threshold-multi-party-private-set-intersection/)
  Kailiang Ji, Weijing You, Huiyang He, Le Yang, Jingqiang Lin

  <details><summary>摘要 / Abstract</summary>

  Multi-Party Private Set Intersection (MP-PSI) with threshold enhances the flexibility of MP-PSI by disclosing elements present in at least $t$ participants&#x27; sets, rather than requiring elements to appear in all $n$ sets. In scenarios where each participant is responsible for its dataset, e.g., digital forensics, MP-PSI with threshold should disclose both intersection elements and corresponding holders such that elements are traceable and the reliability of intersection is guaranteed. We refer to MP-PSI with threshold supporting traceability as Traceable Over-Threshold MP-PSI (T-OT-MP-PSI). However, research on such protocols remains limited, and existing work tolerates at most $t-2$ semi-honest participants at considerable computational cost. We propose two novel Traceable OT-MP-PSI protocols. The first, Efficient Traceable OT-MP-PSI (ET-OT-MP-PSI), combines Shamir&#x27;s secret sharing with an oblivious programmable pseudorandom function, achieving significantly improved efficiency with resistance to at most $t-2$ semi-honest participants. The second, Security-enhanced Traceable OT-MP-PSI (ST-OT-MP-PSI), achieves security against up to $n-1$ semi-honest participants by further leveraging the oblivious linear evaluation protocol. Compared to Mahdavi et al.&#x27;s protocol, ours eliminate the assumption that certain special parties do not collude. Experimental results demonstrate significant improvements: for $n=5$, $t=3$, and sets of size $2^{14}$, ET-OT-MP-PSI achieves $15056\times$ speedup and ST-OT-MP-PSI achieves $505\times$ speedup over Mahdavi et al.&#x27;s protocol.

  匹配依据：MPC: private set intersection, secret sharing

  </details>

- **Practical Private Set Operation via Secret Sharing for Lightweight Clients.**
  2026 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2026.3684841)
  Ziyu Niu, Yumei Li, Yudi Zhang, Willy Susilo, Hao Wang, Ye Su

- **Practical Multi-Party Private Set Intersection with Reducible Zero-Sharing.**
  2026 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00006) · [IACR ePrint](https://eprint.iacr.org/2025/2019)
  Jin Tan, Zhenyu Guan, Hua Guo, Yewei Guan, Jiarong Huo, Man Ho Au

  <details><summary>摘要 / Abstract</summary>

  Multi-party Private Set Intersection (mPSI) enables $n(n\geq3)$ parties, each holding a set of size $m$, to jointly compute their intersection while preserving the confidentiality of each set, which is essential for privacy-preserving data analysis and secure database queries. Existing mPSI protocols have limitations in achieving both sufficient security and practical efficiency. This paper presents a novel and efficient mPSI construction in the semi-honest model while resisting arbitrary collusion attacks. Our construction works in the offline/online paradigm. Given the corruption threshold $t$, the online phase achieves linear total computational and communication complexity, that is $O((n+t)m)$, and solely uses symmetric operations. This makes our construction theoretically outperform the existing works. The technical core of the construction is our newly extracted primitive called reducible zero-sharing, which allows $t(t&lt;n)$ parties to obtain shares of zero for items in the intersection of $n$ parties&#x27; input set, while resisting up to $t-1$ colluding parties. We present a practical construction of reducible zero-sharing in the offline/online paradigm by leveraging the homomorphic property of oblivious key-value store (OKVS). With extensive experiments, we demonstrate that our construction outperforms state-of-the-art works in terms of online running time and communication cost. Specifically, compared to works with sufficient security, the online running time of our mPSI construction is $9.57-114.46\times$ faster in the LAN setting, $2.69-28.41\times$ faster in the WAN setting, while the communication cost is $0.29-28.70\times$ lower. Notably, the total performance (offline+online) still obtains up to $18.73\times$ improvement. Compared with works with practical efficiency, our mPSI construction achieves similar performance while providing stronger security.

  匹配依据：MPC: private set intersection

  </details>

- **Polynomial Secret Sharing Schemes and Algebraic Matroids.**
  2026 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-032-12293-3_14) · [IACR ePrint](https://eprint.iacr.org/2025/368)
  Oriol Farràs, Amos Beimel, Adriana Moya

  <details><summary>摘要 / Abstract</summary>

  Polynomial secret sharing schemes generalize the linear ones by adding more expressivity and giving room for efficiency improvements. In these schemes, the secret is an element of a finite field, and the shares are obtained by evaluating polynomials on the secret and some random field elements, i.e., for every party there is a set of polynomials that computes the share of the party. Notably, for general access structures, the best known polynomial schemes have better share size than the best known linear ones. This work investigates the properties of the polynomials and the fields that allow these efficiency gains and aims to characterize the access structures that benefit from them. We focus first on ideal schemes, which are optimal in the sense that the size of each share is the size of the secret. We prove that, under some restrictions, if the degrees of the sharing polynomials are not too big compared to the size of the field, then its access structure is a port of an algebraic matroid. This result establishes a new connection between ideal schemes and matroids, extending the known connection between ideal linear schemes and linearly representable matroids. For general polynomial schemes, we extend these results and analyze their privacy and correctness. Additionally, we show that given a set of polynomials over a field of large characteristic, one can construct linear schemes that realize the access structure determined by these polynomials; as a consequence, polynomial secret sharing schemes over these fields are not stronger than linear schemes. While there exist ports of algebraic matroids that do not admit ideal schemes, we demonstrate that they always admit schemes with statistical security and information ratio tending to one. This is achieved by considering schemes where the sharings are points in algebraic varieties.

  匹配依据：MPC: secret sharing

  </details>

- **Over-Threshold Multiparty Private Set Intersection for Collaborative Network Intrusion Detection.**
  2026 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2510.12045) · [NSDI](https://www.usenix.org/conference/nsdi26/presentation/arpaci)
  Florian Kerschbaum, Raouf Boutaba, Onur Eren Arpaci

  <details><summary>摘要 / Abstract</summary>

  An important function of collaborative network intrusion detection is to analyze the network logs of the collaborators for joint IP addresses. However, sharing IP addresses in plain is sensitive and may be even subject to privacy legislation as it is personally identifiable information. In this paper, we present the privacy-preserving collection of IP addresses. We propose a single collector, over-threshold private set intersection protocol. In this protocol $N$ participants identify the IP addresses that appear in at least $t$ participant&#x27;s sets without revealing any information about other IP addresses. Using a novel hashing scheme, we reduce the computational complexity of the previous state-of-the-art solution from $O(M(N \log{M}/t)^{2t})$ to $O(t^2M\binom{N}{t})$, where $M$ denotes the dataset size. This reduction makes it practically feasible to apply our protocol to real network logs. We test our protocol using joint networks logs of multiple institutions. Additionally, we present two deployment options: a collusion-safe deployment, which provides stronger security guarantees at the cost of increased communication overhead, and a non-interactive deployment, which assumes a non-colluding collector but offers significantly lower communication costs and applicable to many use cases of collaborative network intrusion detection similar to ours.

  匹配依据：MPC: private set intersection

  </details>

- **Optimistic Asynchronous Dynamic-Committee Proactive Secret Sharing.**
  2026 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00243) · [IACR ePrint](https://eprint.iacr.org/2025/880)
  Zhuolun Xiang, Qiang Tang, Bin Hu, Zhenliang Lu, Zongyang Zhang, Jianwei Liu

  <details><summary>摘要 / Abstract</summary>

  Dynamic-committee Proactive Secret Sharing (DPSS) has gained increased attention for its ability to dynamically update the shareholder committees and refresh secret shares, even against adversaries that gradually corrupt all nodes. However, existing state-of-the-art asynchronous DPSS protocols suffer from significant $\mathcal{O}(n^3)$ message complexity and $\mathcal{O}(\lambda n^3)$ communication complexity, where $\lambda$ denotes the security parameter and $n$ is the committee size. In this paper, we distinguish optimistic-case and worst-case scenarios based on node behaviors and network conditions, thus reducing the redundant communication overhead of asynchronous DPSS. Under the trusted setup assumption, we achieved an $\mathcal{O}(n^2)$ message complexity in all scenarios. Additionally, our protocol has an $\mathcal{O}(\lambda n^2)$ communication complexity in the optimistic case, where all nodes are honest and the network is synchronous, and $\mathcal{O}(\lambda n^3)$ communication complexity in the worst case. We also propose two strategies to eliminate the strong trusted setup assumptions, and the asymptotic performance still surpasses the state-of-the-art protocols. For committee sizes of 4 to 400, the estimated concrete communication cost of our DPSS is 19--100x (resp., 8--14x) smaller in the optimistic case (resp., worst case) compared to LongLive (USENIX Security &#x27;23). Experiments in AWS show that our DPSS achieves a latency of 1.9--8 seconds for committee sizes from 4 to 64. Single-machine benchmarks reveal a (computational) runtime reduction of up to 44\%.

  匹配依据：MPC: secret sharing

  </details>

- **Optimal Access Structure Partition Methods for Image Secret Sharing.**
  2026 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2025.3645631)
  Li Tang, Ching-Nung Yang, Wei Qi Yan, Zhihua Xia, Xiaotian Wu

- **On the Security of Linear Secret Sharing with General Noisy Side-Channel Leakage.**
  2026 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25336-1_17) · [IACR ePrint](https://eprint.iacr.org/2025/1809)
  Hessam Mahdavifar, Utkarsh Gupta

  <details><summary>摘要 / Abstract</summary>

  Secret sharing is a foundational cryptographic primitive for sharing keys in distributed systems. In a classical $(n,t)$-threshold setting, it involves a dealer who has a secret, a set of $n$ users to whom shares of the secret are sent, and a threshold $t$ which is the minimum number of shares required to recover the secret. These schemes offer an all-or-nothing security approach where less than $t$ shares reveal no information about the secret. But these guarantees are threatened by side-channel attacks which can leak partial information from each share. Initiated by Benhamouda et al. (Crypto&#x27;18), the security of linear secret sharing schemes has been studied for bounded leakage attack models, which assume that the adversary can leak bounded functions of each share. However, this model does not translate into real-world attacks, as physical side-channels are inherently noisy. The $\delta$-noisy channel model, proposed by Prouff and Rivain (Eurocrypt’13), is a general leakage framework which captures the noisy behavior of side-channels. In this work, we study the security of linear secret sharing schemes with $\delta$-noisy leakage, and show bounds on the mutual information (MI) and statistical bias ($\Delta^{\mathrm{TV}}$) security metrics. Our results are based on the Fourier analytical framework, first used by Benhamouda et al. (Crypto&#x27;18), adapted to the $\delta$-noisy leakage model. To give security bounds, we introduce a security parameter $\eta\le \min{\{1,2\delta\}}$, determined by the Fourier linear biases of the posterior distributions of the leaked secret shares. Then, the Poisson summation formula enables us to bound the ratio between the observed leakage for some given secret, and leakage under independence as $(1\pm \eta^t)$. This is then used to show a) $(n,t \ge \tau (n+1))$-threshold schemes over $\mathbb{F}_q$ have at most $\mathcal{O}(q^{-t(\gamma+1-1/\tau)})$ leakage, given $\eta \le q^{-\gamma}$; and consequently b) for $(n,n)$-threshold schemes the guessing advantage is at most $(q-1) \cdot \eta^n \le (q-1)\cdot (2 \delta)^n$. This work can be viewed as a next step towards closing the gap between theory and practice in leakage resilient cryptography.

  匹配依据：MPC: secret sharing

  </details>

- **On the Power of Sumcheck in Secure Multiparty Computation.**
  2026 · MPC · 含会议/期刊记录 · [PKC](https://doi.org/10.1007/978-3-032-26734-4_9) · [IACR ePrint](https://eprint.iacr.org/2025/177)
  Zhe Li, Yizhou Yao, Chen Yuan, Chaoping Xing

  <details><summary>摘要 / Abstract</summary>

  Lund et al. (JACM 1992) invented the powerful Sumcheck protocol that has been extensively used in complexity theory and in designing concretely efficient (zero-knowledge) arguments. In this work, we systematically study Sumcheck in the context of secure multi-party computation (MPC). Our main result is a new unified framework for lifting semi-honest MPC protocols to maliciously secure ones, with a small {\em constant} multiplicative overhead in {\em both} computation and communication. In general, our approach applies to any semi-honest, linear secret-sharing based dishonest majority MPC secure up to additive attacks, where linear secret-sharing can be enhanced with an authentication mechanism. At a high-level, our approach has a highly distributive flavor, where the parties jointly emulate a Sumcheck prover to prove the correctness of MPC semi-honest evaluations in zero-knowledge, while simultaneously emulating a Sumcheck verifier to verify the proof themselves. Equipped with our new techniques, we design a SPDZ-style MPC protocol with $5N+O(\log{N})$ online communication per party and sublinear preprocessing based on efficient pseudorandom correlation generators (PCGs), where $N$ is the circuit size. This substantially improves the $6N$ communication achieved in Le Mans (CRYPTO 2022), the state-of-the-art in the SPDZ line of works. Technically, the savings are obtained by using a Sumcheck-based mechanism to check $N$ \emph{unverified} authenticated multiplication triple relations, which requires only $N+1$ {\em standard Beaver triples} and $O(\log{N})$ random authenticated shares, rather than $N$ additional unverified authenticated triples needed by a ``sacrifice&#x27;&#x27; strategy. We also show concrete benefits for honest majority MPC protocols based on Shamir secret sharing. Compared to the best known approach in this scenario (Goyal et al. CRYPTO 2020) based on {\em fully linear interactive oracle proofs} (FLIOPs), asymptotically we achieve the same $O(N)$ additive overhead in computation and $O(\log{N})$ additive overhead in communication. However, we replace the $O(\log{N})$ double sharings used there with $O(\log{N})$ random sharings, and reduce the soundness error from $O(\frac{N}{|\mathbb{F}|})$ to $O(\frac{\log{N}}{|\mathbb{F}|})$, where $\mathbb{F}$ is the underlying field.

  匹配依据：MPC: secret sharing, secure multi party computation, secure multiparty computation

  </details>

- **On the Attribute Hiding Security of Privacy Preserving Secret-Sharing-Based Outsourced Decision Tree Classification.**
  2026 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2026.3714143)
  Yu-Chi Chen, Chang-Ching Hung, Tsung-Chen Hsieh, Srinivas Shekar

- **New Upper and Lower Bounds for Perfectly Secure MPC.**
  2026 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_13) · [IACR ePrint](https://eprint.iacr.org/2025/1206)
  Lawrence Roy, Shravani Patil, Arpita Patra, Ivan Damgård

  <details><summary>摘要 / Abstract</summary>

  We consider perfectly secure MPC for $n$ players and $t$ malicious corruptions. We ask whether requiring only security with abort (rather than guaranteed output delivery, GOD) can help to achieve protocols with better resilience, communication complexity or round complexity. We show that for resilience and communication complexity, abort security does not help, one still needs $3t&lt; n$ for a synchronous network and $4t&lt; n$ in the asynchronous case. And, in both cases, a communication overhead of $O(n)$ bits per gate is necessary. When $O(n)$ overhead is inevitable, one can explore if this overhead can be pushed to the preprocessing phase and the online phase can be achieved with $O(1)$ overhead. This result was recently achieved in the synchronous setting, in fact, with GOD guarantee. We show this same result in the asynchronous setting. This was previously open since the main standard approach to getting constant overhead in a synchronous on-line phase fails in the asynchronous setting. In particular, this shows that we do not need to settle for abort security to get an asynchronous perfectly secure protocol with overheads $O(n)$ and $O(1)$. Lastly, in the synchronous setting, we show that perfect secure MPC with abort requires only 2 rounds, in contrast to protocols with GOD that require 4 rounds.

  匹配依据：MPC: mpc (context)

  </details>

- **New Framework for Structure-Aware PSI From Distributed Function Secret Sharing.**
  2026 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-981-95-5116-3_10) · [IACR ePrint](https://eprint.iacr.org/2025/907)
  Peihan Miao, Dung Bui, Gayathri Garimella, Phuoc Pham Van Long, Phuoc Van Long Pham

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) allows two parties to jointly compute the intersection of their private sets without revealing any additional information. Structure-aware PSI (sa-PSI), introduced by Garimella et al. (Crypto&#x27;22), is a variant where Alice&#x27;s input set has a publicly known structure and Bob&#x27;s input set remains unstructured, enabling new applications like fuzzy PSI. Their construction relies solely on lightweight cryptographic primitives such as symmetric-key primitives and oblivious transfer (OT) extension. Since then, there has been active research on sa-PSI based on lightweight cryptography. Notably, recent work by Garimella et al. (Crypto&#x27;24) achieves sa-PSI with both communication and computation costs only scaling with the description size of Alice&#x27;s set, rather than its potentially large cardinality. However, this line of work remains largely theoretical, lacking efficient concrete implementations. In this work, we close this gap by presenting a new framework for sa-PSI that achieves practical efficiency. We identify and eliminate a hidden multiplicative overhead proportional to the security parameter (e.g., 128) in prior symmetric-key-based sa-PSI constructions. A key building block of our new framework is a distributed Function Secret Sharing (dFSS) key generation protocol tailored to the structure of Alice&#x27;s set, which may be of independent interest. To demonstrate the practicality of our framework, we extend our dFSS protocol to support incremental evaluation, introduce new techniques for spatial hashing, and develop several new optimization techniques, including reducing the exponential dependence on dimension and enabling load balancing between the two parties. We instantiate our framework for structured sets defined by unions of $d$-dimensional $\ell_\infty$ balls, and implement our protocols using only lightweight symmetric-key primitives and OT extension. Our experiments show concrete performance improvements of up to $27\times$ speedup in computation and $7.7\times$ reduction in communication in low-dimensional, large-radius settings compared to existing public-key-based fuzzy PSI protocols by van Baarsen &amp; Pu (Eurocrypt&#x27;24) and Gao et al. (Asiacrypt&#x27;24).

  匹配依据：MPC: oblivious transfer, private set intersection, secret sharing

  </details>

- **Multiparty Homomorphic Secret Sharing and More from LPN and MQ.**
  2026 · MPC · 含会议/期刊记录 · [TCC](https://doi.org/10.1007/978-3-032-12293-3_16) · [IACR ePrint](https://eprint.iacr.org/2025/966)
  Geoffroy Couteau, Naman Kumar, Xiaxi Ye

  <details><summary>摘要 / Abstract</summary>

  We give the first constructions of multiparty pseudorandom correlation generators, distributed point functions, and (negligible-error) homomorphic secret sharing for constant-degree polynomials for any number of parties without using LWE or iO. Our constructions are proven secure under the combination of LPN with dimension $n$, $2n$ samples, and noise rate $n^{\varepsilon-1}$ for a small constant $\varepsilon$, and MQ with $n$ variables and $n^{1+\delta}$ equations. As applications of our results, we obtain from the same assumptions secure multiparty computation protocols with sublinear communication and silent preprocessing, as well as private information retrieval for $M$ servers and size-$\lambda^d$ databases with optimal download rate and client-to-server communication $M^d\cdot \lambda^3$.

  匹配依据：MPC: secret sharing, secure multiparty computation

  </details>

- **Multiparty Computation with Minimal Overhead Without Circuit Transformation.**
  2026 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-032-35418-1_5)
  Aditya Hegde, Mingyuan Wang, Phuoc Pham Van Long

- **MinBucket MPSI: Breaking the Max-Size Bottleneck in Multi-Party Private Set Intersection.**
  2026 · MPC · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/minbucket-mpsi-breaking-the-max-size-bottleneck-in-multi-party-private-set-intersection/)
  Yang Cao, Binbin Tu, Yu Chen, Boyudong Zhu

- **Malicious Homomorphic Secret Sharing with Applications to DV-NIZK and More.**
  2026 · MPC · 含会议/期刊记录 · [PKC](https://doi.org/10.1007/978-3-032-26740-5_7) · [IACR ePrint](https://eprint.iacr.org/2025/2077)
  Lisa Kohl, Zhe Li, Pedro Capitão, Hila Dahari-Garbian

  <details><summary>摘要 / Abstract</summary>

  Homomorphic Secret Sharing (CRYPTO 2016) allows a secret to be shared among two or more parties in such a way that the parties can locally evaluate a class of functions on their shares. Homomorphic secret sharing (HSS) schemes and their underlying techniques have facilitated a wide range of applications. To account for the fact that parties generating or evaluating the shares might act maliciously, variants of HSS schemes that allow detection of such malicious behavior have been introduced. However, all prior approaches of malicious HSS that capture the class of $\mathsf{NC}1$ circuits either crucially rely on a random oracle or require an non-reusable setup. In this work, we initiate the study of malicious public-key $2$-party HSS in the standard model with reusable setup, where any malicious behavior during share generation and share evaluation can be detected. Towards constructing malicious HSS, we introduce the notion of homomorphic secret sharing with robust linear reconstruction (RLR-HSS) and show that this notion readily implies malicious HSS. We outline challenges in instantiating RLR-HSS due to the error present in all current HSS constructions not relying on SHE/FHE, and show how to overcome these using derandomization techniques by Dwork et al. (EUROCRYPT 2004). Finally, we show applications of malicious HSS to compact designated verifier non-interactive zero knowledge arguments and maliciously secure $2$-party computation in the standard model (supporting the same function class as the underlying malicious HSS).

  匹配依据：MPC: secret sharing, secure 2 party computation

  </details>

- **Honest Majority Constant-Round MPC with Linear Communication from One-Way Functions.**
  2026 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-032-12287-2_1) · [IACR ePrint](https://eprint.iacr.org/2025/1676)
  Junru Li, Yifan Song

  <details><summary>摘要 / Abstract</summary>

  Secure multiparty computation (MPC) faces a fundamental efficiency trade-off between round complexity and communication complexity: without fully homomorphic encryption, protocols with constant round complexity (e.g., protocols based on garbled circuits) incur high communication cost, while communication-efficient approaches (e.g., protocols based on secret sharing) have round complexity linear in the depth of the circuit. In this work, we focus on reducing the communication complexity of constant-round MPC protocols in the honest majority setting. Existing results either rely on strong assumptions (e.g., random oracles, DDH, LPN) or incur high communication of $\Omega(|C|n^2\kappa)$ bits under one-way functions (OWFs). However, non-constant-round MPC protocols can achieve linear communication in the number of parties even with information-theoretic security. We resolve this gap by presenting the first constant-round honest majority MPC protocol with linear communication complexity of $O(|C|n\kappa + n^2\kappa^2+n^4\kappa)$ only from OWFs. We introduce novel techniques for computing garbled circuits via party virtualization and efficient local computation of virtual parties, which optimize the existing protocols on multiparty garbling. These allow us to overcome the $O(n^2\kappa)$ bit of communication per-gate bottleneck of prior protocols, matching the scalability of the best non-constant-round protocols in the same setting.

  匹配依据：MPC: garbled circuits, secret sharing, secure multiparty computation

  </details>

- **GoSSamer: Lightweight and Linear-Communication Asynchronous (Dynamic Proactive) Secret Sharing and the Applications.**
  2026 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00185) · [IACR ePrint](https://eprint.iacr.org/2025/1516)
  Bin Hu, Yuan Lu, Xinxin Xing, Yizhong Liu, Boyang Liao, Jianwei Liu, Xun Lin, Tianwei Zhang

  <details><summary>摘要 / Abstract</summary>

  Asynchronous complete secret sharing (ACSS) and asynchronous dynamic proactive secret sharing (ADPSS) are fundamental primitives for secret sharing and resharing in modern threshold systems, such as multi-party computation, distributed key management, and blockchain. However, existing ACSS constructions that employ homomorphic commitments incur notable computational overhead, while the lightweight-computation constructions require quadratic per-secret communication, limiting scalability as the number of parties grows. ADPSS constructions inevitably inherit these inefficiencies due to their tight coupling to the commitment-based ACSS and requiring at least quadratic cross-committee communication. To break these bottlenecks, we design GoSSamer, a concretely and asymptotically efficient protocol suite, where both our ACSS and ADPSS achieve (1) lightweight computation with only hash function and symmetric encryption; (2) asymptotically optimal, linear per-secret communication; (3) optimal resilience in asynchronous networks; and (4) post-quantum security. In GoSSamer-ACSS, we propose an original-evaluation propagation paradigm for linear communication without commitment‑requiring interpolation, which further unlocks our lightweight bivariate-polynomial-based degree checking for share verification. Building on this foundation, GoSSamer‑ADPSS contributes two further techniques: a consistency verification technique that decouples the ADPSS framework from the commitment-based ACSS, and a dual-committee reconstruction technique that yields linear per-secret communication. When deployed in distributed AWS instances, GoSSamer-ACSS reduces the runtime by 95.6% compared to the linear-communication scheme hbACSS (NDSS&#x27;22) and 45.8% compared to lightweight SS24 (JoC&#x27;24). GoSSamer-ADPSS reduces the runtime by at least 67.7% compared to LongLive (Usenix Security&#x27;23). Moreover, when applied to practical distributed key management systems, the GoSSamer-ACSS-based distributed key generation is 7-11x faster than DXK+23 (Usenix Security&#x27;23), and GoSSamer-ADPSS-based key resharing reaches a throughput of 1994 keys/s across 10-node committees, compared to 85 keys/s in LongLive.

  匹配依据：MPC: multi party computation, secret sharing

  </details>

- **Fuzzy Private Set Intersection from VOLE.**
  2026 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-981-95-5116-3_11) · [IACR ePrint](https://eprint.iacr.org/2025/911)
  Sihang Pu, Aron van Baarsen

  <details><summary>摘要 / Abstract</summary>

  Private set intersection (PSI) is a well-researched cryptographic primitive that allows two parties to compute the intersection of their input sets without revealing any information about items outside of the intersection. Fuzzy private set intersection is a relatively new variant of PSI, where items are not matched exactly but ``fuzzily&#x27;&#x27;. Most commonly, items are points $\mathbf{q},\mathbf{w}$ in $d$-dimensional integer space $\mathbb{Z}^d$ and a point is a fuzzy match to another if it lies within a ball of radius $\delta$ centered at this point, with respect to some distance metric. Previous works either only support infinity $(L_{\infty}$) distance metric and standard PSI functionality, or support general Minkowski ($L_{\mathsf{p}}$, $\mathsf{p}\in[1,\infty]$) distance metrics and realize richer functionalities but rely on expensive homomorphic encryptions. Our work aims to bridge this gap by giving the first construction of a fuzzy PSI protocol for general Minkowski distance metrics relying on significantly cheaper operations during the online phase. Our main building block is a novel fuzzy matching protocol based on an oblivious pseudorandom function (OPRF), which can be realized very efficiently from vector oblivious linear evaluation (VOLE). Our protocol is able to preserve the asymptotic complexity as well as the simplicity of the fuzzy matching protocol from van Baarsen and Pu (Eurocrypt &#x27;24), while being much more concretely efficient. Additionally, we achieve several asymptotic improvements by representing intervals succinctly. Finally, we present the first fuzzy PSI protocol for infinity distance that places no assumptions on the sets of points, while maintaining asymptotic complexities comparable to the state-of-the-art fuzzy PSI protocol.

  匹配依据：MPC: private set intersection

  </details>

- **Faster Than Ever: A New Lightweight Private Set Intersection and Its Variants.**
  2026 · MPC · 含会议/期刊记录 · [NDSS](https://www.ndss-symposium.org/ndss-paper/faster-than-ever-a-new-lightweight-private-set-intersection-and-its-variants/)
  Liyao Xiang, Jinyong Shan, Weidong Qiu, Guowei Ling, Peng Tang

- **FESCAT: Function Secret Sharing Based Efficient Secure Collaborative Analysis of Time Series Data.**
  2026 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2025.3632891)
  David S. L. Wei, Jingcheng Zhao, Qibin Sun, Bin Zhu, Kaiping Xue, Jun Lu

- **Efficient Privacy-Preserving User Tracking From Threshold Multi-Party Private Set Intersection.**
  2026 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2026.3705319)
  Jianting Ning, Haining Yang, Jing Qin, Bo Zhao, Jixin Ma

- **Efficient Malicious Multiparty Private Set Intersection Supporting Cardinality, Sharing, and Batching.**
  2026 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2026.3671114)
  Kim-Kwang Raymond Choo, Zhenfu Cao, Xiyuan Han, Jun Zhou, Xiaolei Dong

- **Deniable Secret Sharing.**
  2026 · MPC · 含会议/期刊记录 · [series/lncs](https://doi.org/10.1007/978-3-032-12293-3_13) · [IACR ePrint](https://eprint.iacr.org/2025/525)
  Sophia Yakoubov, Sebastian Kolby, Divya Ravi, Ran Canetti, Ivan Damgård

  <details><summary>摘要 / Abstract</summary>

  We introduce deniable secret sharing (DSS), which, analogously to deniable encryption, enables shareholders to produce fake shares that are consistent with a target “fake message”, regardless of the original secret. In contrast to deniable encryption, in a DSS scheme an adversary sees multiple shares, some of which might be real, and some fake. This makes DSS a more difficult task, especially in situations where the fake shares need to be generated by individual shareholders, without coordination with other shareholders. We define several desirable properties for DSS, and show both positive and negative results for each. The strongest property is fake hiding, which is a natural analogy of deniability for encryption: given a complete set of shares, an adversary cannot determine whether any shares are fake. We show a construction based on Shamir secret sharing that achieves fake hiding as long as (1) the fakers are qualified (number $t$ or more), and (2) the set of real shares which the adversary sees is unqualified. Next we show a construction based on indistinguishability obfuscation that relaxes condition (1) and achieves fake hiding even when the fakers are unqualified (as long as they comprise more than half of the shareholders). We also extend the first construction to provide the weaker property of faker anonymity for all thresholds. (Faker anonymity requires that given some real shares and some fake shares, an adversary should not be able to tell which are fake, even if it can tell that some fake shares are present.) All of these constructions require the fakers to coordinate in order to produce fake shares. On the negative side, we first show that fake hiding is unachievable when the fakers are a minority, even if the fakers coordinate. Further, if the fakers do not coordinate, then even faker anonymity is unachievable as soon as $t &lt; n$ (namely the reconstruction threshold is smaller than the number of parties).

  匹配依据：MPC: secret sharing

  </details>

- **Decor: Delegated Computation on Randomness for Secure Evaluation of Nonlinear Functions.**
  2026 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00256)
  Hyunghoon Cho, Haris Smajlovic, Ruzica Piskac, Kyle Sheng, Timos Antonopoulos

- **DMPF-PSI: Enabling High-Frequency Updatable Private Set Intersection on Dynamic Data.**
  2026 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2026.3705330)
  Zhi Li, Debiao He, Hao Wang, Jiadi Zhang, Ye Su

- **Cryptanalysis of "Multi-Party Private Set Intersection With One-Round Online Interaction".**
  2026 · MPC · 含会议/期刊记录 · [TIFS](https://doi.org/10.1109/TIFS.2026.3666890)
  Yewei Guan, Jiarong Huo, Ye Yuan, Hua Guo, Jin Tan

- **Concretely-Efficient Multi-Key Homomorphic Secret Sharing and Applications.**
  2026 · MPC · 含会议/期刊记录 · [IEEE S&amp;P](https://doi.org/10.1109/SP63933.2026.00004) · [IACR ePrint](https://eprint.iacr.org/2025/1803)
  Srini Devadas, Geoffroy Couteau, Kaiwen He, Sacha Servan-Schreiber, Srinivas Devadas

  <details><summary>摘要 / Abstract</summary>

  Homomorphic secret sharing (HSS) is a powerful cryptographic primitive that enables efficient, low-communication secure computation without the use of fully homomorphic encryption. Public-key HSS is a well-known variant that supports inputs from multiple parties, but all parties must agree on a joint public key before any party can encode their inputs, requiring extra rounds of communication in applications. Recently, Couteau et al. (EUROCRYPT 2025) constructed multi-key HSS (MKHSS)—a new primitive which allows parties to encode their inputs under independent keys—under the DCR assumption. MKHSS assumes only a reusable common reference string, without the need for prior interactions between parties or a public-key infrastructure. In this paper, we construct and implement the first concretely-efficient MKHSS scheme under the same assumptions used by Couteau et al. Using an algorithmic insight that reduces the largest modulus in Couteau et al. from $N^4$ to $N^2$, our optimized implementation can homomorphically multiply inputs in 5.0 milliseconds—while an implementation of Couteau et al. requires 224.6 milliseconds—thereby achieving a $45\times$ speedup. A powerful application of MKHSS is to realize attribute-based non-interactive key exchange (ANIKE), which generalizes password-authenticated key exchange (PAKE) to arbitrary attribute policies. ANIKE is currently only known from MKHSS and in this paper we show the first practical instantiation of ANIKE for two concrete predicate types with applications to geolocation-based key exchange and fuzzy PAKE. We use our implementation to evaluate the first concretely-efficient ANIKE schemes for a range of practically useful policies. Using our implementation, two parties can perform a geolocation-based key exchange in under one second and a fuzzy PAKE on an 8-word passphrase in a few seconds for realistic parameters, on a single core, achieving a roughly $30 \times$ speedup over Couteau et al. for both applications.

  匹配依据：MPC: secret sharing, secure computation

  </details>

- **Client-Server Homomorphic Secret Sharing in the CRS Model.**
  2026 · MPC · 含会议/期刊记录 · [EUROCRYPT](https://doi.org/10.1007/978-3-032-25324-8_3)
  Geoffroy Couteau, Aditya Hegde, Lawrence Roy, Lalita Devadas, Abhishek Jain, Damiano Abram, Sacha Servan-Schreiber

- **Broadcast-Optimal Secure Computation from Black-Box Oblivious Transfer.**
  2026 · MPC · 含会议/期刊记录 · [ASIACRYPT](https://doi.org/10.1007/978-981-95-5116-3_5) · [IACR ePrint](https://eprint.iacr.org/2025/1614)
  Luisa Siniscalchi, Michele Ciampi, Divya Ravi, Yu Xia

  <details><summary>摘要 / Abstract</summary>

  When investigating the round-complexity of multi-party computation protocols (MPC) protocols, it is common to assume that in each round parties can communicate over broadcast channels. However, broadcast is an expensive resource, and as such its use should be minimized. For this reason, Cohen, Garay, and Zikas (Eurocrypt 2020) investigated the tradeoffs between the use of broadcast in two-round protocols assuming setup and the achievable security guarantees. Despite the prolific line of research that followed the results of Cohen, Garay, and Zikas, none of the existing results considered the problem of minimizing the use of broadcast while relying in a 𝑏𝑙𝑎𝑐𝑘-𝑏𝑜𝑥 way on the underlying cryptographic primitives. In this work, we fully characterize the necessary and sufficient requirements in terms of broadcast usage in the 𝑑𝑖𝑠ℎ𝑜𝑛𝑒𝑠𝑡 𝑚𝑎𝑗𝑜𝑟𝑖𝑡𝑦 setting for round-optimal MPC with black-box use of minimal cryptographic assumptions. Our main result shows that to securely realize any functionality with 𝑢𝑛𝑎𝑛𝑖𝑚𝑜𝑢𝑠 𝑎𝑏𝑜𝑟𝑡 in the common reference string model with black-box use of two-round oblivious transfer it is necessary and sufficient for the parties to adhere to the following pattern: in the first two rounds the parties exchange messages over peer-to-peer channels, and in the last round the messages are sent over a broadcast channel. We also extend our results to the correlated randomness setting where we prove that one round of peer-to-peer interaction and one round of broadcast is optimal to evaluate any functionality with unanimous abort.

  匹配依据：MPC: multi party computation, oblivious transfer, secure computation

  </details>

- **Breaking the $\\varOmega (\|C\|\\kappa )$ Barrier on Garbled Circuit Size in the Random Oracle Model.**
  2026 · MPC · 含会议/期刊记录 · [CRYPTO](https://doi.org/10.1007/978-3-032-35418-1_18)
  Junru Li, Yifan Song

- **Beyond the Output: Inference Attacks on Private Set Union and Multi-Key Private Matching.**
  2026 · MPC · 含会议/期刊记录 · [PoPETs](https://doi.org/10.56553/POPETS-2026-0155)
  Francesca Falzon, Tianxin Tang, Kenneth G. Paterson, Andrea Raguso

- **Approx-PSI: Efficient Differentially Private Set Intersection-Based Analysis.**
  2026 · MPC · 含会议/期刊记录 · [TDSC](https://doi.org/10.1109/TDSC.2025.3629820)
  Jian Long, Ziyuan Liang, Zhan Qin, Chao Li, Fan Zhang

- **A Construction of Evolving k-Threshold Secret Sharing Scheme over A Polynomial Ring.**
  2026 · MPC · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2402.01144) · [ASIACRYPT](https://doi.org/10.1007/978-981-95-5125-5_1) · [IACR ePrint](https://eprint.iacr.org/2025/1499)
  Sian-Jheng Lin, Xianhong Xie, Hongru Cao, Qi Cheng, Nenghai Yu, Yunghsiang Sam Han, Yunghsiang S. Han

  <details><summary>摘要 / Abstract</summary>

  The threshold secret sharing scheme enables a dealer to distribute the share to every participant such that the secret is correctly recovered from a certain amount of shares. The traditional $(k, n)$ threshold secret sharing scheme requires that the number of participants $n$ is known in advance. In contrast, the evolving secret sharing scheme allows that $n$ can be uncertain and even ever-growing. In this paper, we consider the evolving secret sharing scenario. Based on the prefix codes, we propose a brand-new construction of evolving $k$-threshold secret sharing scheme for an $\ell$-bit secret over a polynomial ring, with correctness and perfect security. The proposed scheme is the first evolving $k$-threshold secret sharing scheme by generalizing Shamir&#x27;s scheme onto a polynomial ring. Besides, the proposed scheme also establishes the connection between prefix codes and the evolving schemes for $k\geq2$. The analysis shows that the size of the $t$-th share is $(k-1)(\ell_t-1)+\ell$ bits, where $\ell_t$ denotes the length of a binary prefix code of encoding integer $t$. In particular, when $\delta$ code is chosen as the prefix code, the share size is $(k-1)\lfloor\lg t\rfloor+2(k-1)\lfloor\lg ({\lfloor\lg t\rfloor+1}) \rfloor+\ell$, which improves the prior best result $(k-1)\lg t+6k^4\ell\lg{\lg t}\cdot\lg{\lg {\lg t}}+ 7k^4\ell\lg k$, where $\lg$ denotes the binary logarithm. Specifically, when $k=2$, the proposal also provides a unified mathematical decryption for prior evolving $2$-threshold secret sharing schemes and also achieves the minimal share size for a single-bit secret, which is the same as the best-known scheme.

  匹配依据：MPC: secret sharing

  </details>
