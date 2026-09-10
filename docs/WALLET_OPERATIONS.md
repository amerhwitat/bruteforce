# Wallet operations and fund-state model

This repository supports legitimate wallet-security research and owner-authorized transaction workflows. It does not implement address-to-private-key recovery, seed guessing against target wallets, credential harvesting, or arbitrary private-key enumeration.

## Send / receive

Wallet integrations may:

- request a fresh receiving address from a wallet the operator controls;
- construct or validate transactions;
- delegate signing to an authenticated wallet or external signer;
- broadcast an already-signed transaction;
- record transaction IDs and confirmation state.

Ethereum integrations should use `eth_sendRawTransaction` for externally signed transactions. Bitcoin integrations may delegate spending to authenticated Bitcoin Core wallet RPCs.

## Address state

Normalize observed addresses into:

- `OWNED` — ownership has been established by the operator;
- `WATCH_ONLY` — public observation only;
- `BURN` — known/provably unspendable destination;
- `UNKNOWN` — observed but ownership is not established.

Only `OWNED` addresses may be offered as spend sources. `BURN` outputs are never presented as recoverable funds.

## Burn addresses

The scanner may identify and report coins sent to burn addresses. It must not claim that those funds can be collected. A deliberate/provably unspendable output remains unspendable unless the underlying protocol explicitly provides a recovery mechanism.

## Security

Private signing material remains outside this research code whenever possible. Test vectors must use synthetic keys, regtest/testnet assets, or externally supplied signed transactions.
