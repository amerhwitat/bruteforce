# Crypto Interoperability, Research References, and Provenance

The historical name of this repository is retained for continuity. Current functionality is restricted to benign cryptographic research, deterministic key-to-address demonstrations, validation, test vectors and synthetic benchmarks.

## Public standards

- BIP-32: https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki
- ERC-55 / EIP-55: https://eips.ethereum.org/EIPS/eip-55
- ERC-1191: https://eips.ethereum.org/EIPS/eip-1191

## Comparable open-source implementations reviewed

- https://github.com/bitcoinjs/bip32 — MIT; BIP-32 TypeScript implementation.
- https://github.com/bitcoinjs/bitcoinjs-lib — MIT; Bitcoin/BIP39/BIP44 ecosystem.
- https://github.com/paulmillr/scure-bip32 — MIT; audited/minimal BIP-32 implementation.
- https://github.com/paulmillr/scure-bip39 — MIT; audited/minimal BIP-39 implementation.
- https://github.com/bitcoin-core/secp256k1 — MIT; high-assurance secp256k1 C library.
- https://github.com/dan-da/hd-wallet-derive — HD wallet derivation interoperability reference.

## What is incorporated

This document incorporates **research findings and compatibility requirements**, not third-party source code. A third-party implementation may be added later only after an explicit license/provenance review and preservation of required notices.

## Safe implementation boundary

The project must not implement public-address-to-private-key search, guessing, inference, wallet targeting, or brute-force recovery. Safe experiments include known-key derivation, address/checksum validation, deterministic published vectors, cryptographic benchmarks and analysis of computational infeasibility.

## Chimera II

The repository may supply synthetic cryptographic workloads and conformance vectors to Chimera II's C8192/R8192 emulator and wide-integer research, without introducing wallet-recovery functionality.
