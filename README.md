# bruteforce

## Chimera II cross-language crypto research

This repository contains historical cryptocurrency cryptography experiments and a safe research boundary. It is not a wallet-cracking or address-to-private-key recovery tool.

### Implementation tracks

- `python/` — Python research/reference layer.
- `node/` — Node.js ESM integration layer.
- `java/` — Java interoperability/application layer.
- `cpp/` — C++ interoperability/native layer.
- `docs/` — cross-language contracts, provenance and security boundaries.

### Safe scope

- deterministic Bitcoin/Ethereum key-to-address demonstrations using material already possessed;
- address/checksum validation;
- published cryptographic test vectors;
- synthetic cryptographic benchmarks;
- CNN/RNN/GRU and offline-RL research on public or synthetic datasets;
- educational analysis of why public-address-to-private-key inversion is infeasible.

### Prohibited direction

Do not add code that recovers, guesses, maps, brute-forces or searches for a private key corresponding to an arbitrary public address. Do not attack credentials or wallets not controlled by the operator.

### Interoperability

The cross-language implementation uses deterministic JSON/JSONL contracts so Python, Node.js, Java and C++ can consume the same public/synthetic vectors. The Chimera II C8192/R8192 layer consumes the same reproducibility metadata.

See `docs/CRYPTO_AI_BOUNDARY.md` for the security boundary.