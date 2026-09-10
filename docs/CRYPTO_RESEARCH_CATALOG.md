# Cryptocurrency and Cryptography Research Catalog

The repository's historical scripts are classified as research material. The maintained Python layer focuses on safe, reproducible cryptographic experiments.

## Coin/protocol coverage

- Bitcoin — UTXO, SHA-256 proof-of-work, secp256k1 signatures, Base58Check/Bech32 address families.
- Ethereum — account model, Keccak-256, secp256k1 signatures, EIP-55 checksum addresses.
- Litecoin and Dogecoin — Bitcoin-derived UTXO families with different network/mining parameters.
- Monero — privacy-oriented protocol with distinct cryptographic constructions and address formats.
- Solana — account/program architecture using Ed25519 signatures.

## Safe implementation boundary

Allowed: address syntax/checksum validation, deterministic key-to-address tests using keys already possessed by the operator, public test vectors, hashing, benchmarking, and protocol documentation.

Excluded: private-key recovery, seed-phrase guessing, address-targeted key search, credential harvesting, or wallet access without authorization.

The boundary is intentional: public cryptography research should remain reproducible without turning the repository into a wallet-compromise tool.
