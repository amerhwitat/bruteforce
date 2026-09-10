# Crypto AI Research Boundary

The repository may use CNN/RNN models, offline reinforcement learning and public blockchain datasets for educational research, anomaly detection, protocol analysis and synthetic benchmarking.

Allowed workloads include:
- public address and transaction datasets;
- balance-history analysis;
- hash/signature test vectors;
- CNN/RNN/LSTM sequence classification;
- offline PPO-style environments;
- cryptographic performance benchmarks;
- owner-authorized restore-and-verify workflows using recovery material already possessed by the operator.

## Wallet recovery boundary

Legitimate wallet recovery is implemented as **restore-and-verify**, not as cracking. A recovery workflow may validate existing wallet backups or already-held recovery material, derive deterministic public addresses, compare them with an owner-supplied address inventory, and pass signing to a secure wallet or external signer.

The repository must not become an address-to-private-key recovery engine. Do not add seed guessing, arbitrary private-key enumeration against target addresses, credential harvesting, password attacks against third-party wallets, or unauthorized wallet access. Keys already possessed by the operator may be represented by non-secret fingerprints or handled through an external secure vault.

A public balance, transaction history, or a user's claim of ownership is not treated by the software as proof that a guessed secret is authorized or correct.

This boundary is compatible with the repository's existing educational cryptography scope.
