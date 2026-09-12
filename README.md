# bruteforce

## Chimera II cross-language crypto research

This repository contains historical cryptocurrency cryptography experiments and a safe research boundary. It is not a wallet-cracking or address-to-private-key recovery tool.

### Implementation tracks

- `python/` — Python research/reference layer.
- `node/` — Node.js ESM integration layer.
- `java/` — Java interoperability/application layer.
- `cpp/` — C++ interoperability/native layer.
- `apple/` — SwiftUI/Xcode iOS/iPadOS and macOS research shell.
- `docs/` — cross-language contracts, provenance and security boundaries.
- `chimera/` — shared 128D/P2P interoperability contract.

### Apple build

`apple/project.yml` is generated with XcodeGen into native iOS/macOS application targets. Build/archive/export on macOS with Xcode. The Apple application preserves the repository's safe research boundary and never adds private-key recovery, seed guessing or unauthorized wallet access.

### Chimera 128D + P2P

The application may exchange research metadata through the common Chimera 128D state model, separating geometry from observer/perspective and supporting temporal, event, object, interaction and extensible vector state. `chimera/p2p_protocol.json` defines authenticated peer identity, capabilities, sequencing, replay protection and content-addressed synchronization. Security research remains local/public/synthetic; P2P does not distribute cracking jobs or private keys.

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

See `docs/CRYPTO_AI_BOUNDARY.md`.

## License

Original project code is released under the GNU General Public License v3 or later. Third-party components retain their applicable licenses.
