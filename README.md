# bruteforce

## Chimera II cross-language crypto research

This repository contains historical cryptocurrency cryptography experiments and a safe research boundary. It is not a wallet-cracking or address-to-private-key recovery tool.

## Complete source-code citation index

| Area | Source |
|---|---|
| Python research/reference | [python/](python/) |
| Node.js integration | [node/](node/) |
| Java integration | [java/](java/) |
| C++ native layer | [cpp/](cpp/) |
| Apple/SwiftUI | [apple/](apple/) |
| Chimera interoperability | [chimera/](chimera/) |
| Documentation | [docs/](docs/) |
| Complete tracked repository | [source tree](.) |

The links above provide README-level citations for all maintained code. Component directories are the detailed source-of-record boundaries.

### Centralized Apple Objective-C + Flutter

The Apple companion is maintained in [`general/Apple-Implementations/bruteforce`](https://github.com/amerhwitat/general/tree/master/Apple-Implementations/bruteforce). It provides Objective-C/Xcode native integration and Flutter iOS/macOS UI while preserving the safe research boundary.

### Apple build

Build/archive/export on macOS with Xcode and XcodeGen. The Apple application never adds private-key recovery, seed guessing or unauthorized wallet access.

### Safe scope

- deterministic Bitcoin/Ethereum key-to-address demonstrations using material already possessed;
- address/checksum validation;
- published cryptographic test vectors;
- synthetic cryptographic benchmarks;
- CNN/RNN/GRU and offline-RL research on public or synthetic datasets;
- educational analysis of why public-address-to-private-key inversion is infeasible.

### Prohibited direction

Do not add code that recovers, guesses, maps, brute-forces or searches for a private key corresponding to an arbitrary public address. Do not attack credentials or wallets not controlled by the operator.

## License

Original project code is released under the GNU General Public License v3 or later. Third-party components retain their applicable licenses.
