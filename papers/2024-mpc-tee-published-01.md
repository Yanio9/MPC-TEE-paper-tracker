# 2024 · MPC + TEE · 含会议/期刊记录 · 第 1/1 页

[总目录](../PAPERS.md)

- **DECLOAK: Enable Secure and Cheap Multi-Party Transactions on Legacy Blockchains by a Minimally Trusted TEE Network**
  2024 · MPC / TEE · 含会议/期刊记录 · [arXiv](https://arxiv.org/abs/2202.10206) · [TIFS](https://doi.org/10.1109/TIFS.2023.3318935)
  Yuchen Wu, Lei Wang, Hong Lei, Bangdao Chen, Yue Li, Qian Ren, Yingjun Wu

  <details><summary>摘要 / Abstract</summary>

  As the confidentiality and scalability of smart contracts have become a crucial demand of blockchains, off-chain contract execution frameworks have been promising. Some have recently expanded off-chain contracts to Multi-Party Computation (MPC), which seek to transition the on-chain states by off-chain MPC. The most general problem among these solutions is MPT, since its off-chain MPC takes on- and off-chain inputs, delivers on- and off-chain outputs, and can be publicly verified by the blockchain, thus capable of covering more scenarios. However, existing Multi-Party Transaction (MPT) solutions lack at least one of data availability, financial fairness, delivery fairness, and delivery atomicity. These properties are crucially valued by communities, e.g., the Ethereum community, or users. Even worse, these solutions require high-cost interactions between the blockchain and off-chain systems. This paper proposes a novel MPT-enabled off-chain contract execution framework, DECLOAK. DECLOAK is the first to achieve data availability of MPT, and our method can apply to other fields that seek to persist user data on-chain. Moreover, DECLOAK solves all mentioned shortcomings with even lower gas costs and weaker assumptions. Specifically, DECLOAK tolerates all but one Byzantine party and TEE executors. Evaluating on 10 MPTs, DECLOAK reduces the gas cost of the SOTA, Cloak, by 65.6%. Consequently, we are the first to not only achieve such level secure MPT in practical assumption, but also demonstrate that evaluating MPT in the comparable gas cost to normal Ethereum transaction is possible. And the cost superiority of DECLOAK increases as the number of MPT parties grows.

  匹配依据：MPC: multi party computation; TEE: tee (context)

  </details>
