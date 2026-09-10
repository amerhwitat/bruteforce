# bruteforce

## Chimera II Crypto Safety Update

This repository contains historical experimentation around cryptocurrency address/key generation. It is **not** a wallet-recovery tool.

### Safe scope

Use this repository only for:

- deterministic Bitcoin/Ethereum key-to-address demonstrations;
- address and checksum validation;
- published cryptographic test vectors;
- benchmarking cryptographic primitives on synthetic data;
- educational analysis of why public-address-to-private-key inversion is infeasible.

### Prohibited implementation direction

Do not add code that attempts to recover, infer, map, brute-force, or search for a private key corresponding to an arbitrary public Bitcoin or Ethereum address. Do not use address datasets to identify wallets whose keys are not already possessed by the operator.

### Chimera II integration

The repository may serve as a research/reference component for Chimera II OS, including its CISC/RISC cryptographic instruction experiments, provided wallet-key recovery functionality is not introduced.

### Dependencies

Historical scripts may reference `hdwallet`, `colorama`, `requests`, and `web3`. New code should document dependencies explicitly and use sanitized test vectors.
