# Bitcoin public-key range search

A Python experiment that samples private-key candidates within a specified bit range and compares their secp256k1 public points to a supplied public key.

> [!WARNING]
> This is **not a general public-key-to-private-key converter**. It performs random candidate search, with replacement: candidates may be repeated and the search may never finish. Recovering a normally generated Bitcoin private key from its public key is computationally infeasible in practice. The repository name is historical.

## How it works

For each sampled integer `k` in the range `2^(bit-1)` through `2^bit - 1`, the script computes `P - kG`, where `P` is the supplied point and `G` is the secp256k1 generator. If the result is the point at infinity, the candidate corresponds to the supplied point. The sampling is random, not exhaustive; there is no guaranteed completion time.

A match is printed in decimal and appended to `found.txt` in plaintext. That file contains sensitive key material if real keys are used. Use only toy keys and public keys you are authorized to test; do not use this experiment for wallet security or key storage.

## Installation

Prerequisites: Python 3 and the `ecdsa` package.

```bash
git clone https://github.com/ufodia/bitcoin-public-key-to-private-key
cd bitcoin-public-key-to-private-key
pip install ecdsa
```

## Usage

```bash
python pubtoprivate.py -b 15 -pb 04fea58ffcf49566f6e9e9350cf5bca2861312f422966e8db16094beb14dc3df2cc71136e9f21ec86870c3a999f045d712f848c6fd6ed9582521c3f7444c8f182e
```

- `-pb` / `--pubkey`: public key as hexadecimal.
- `-b` / `--bit`: bit length defining the candidate range.

This historical example is included to demonstrate the command syntax; its outcome and runtime are not guaranteed.

## Disclaimer

For educational and research use. Use only on material you own or are explicitly authorized to test.

## Support this project

**BTC**: `1GZdNtQYa2DN4b3hLekrYErv9c8WLqbBTm`

<p align="center">
  <a href="https://buymeacoffee.com/ufodia">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" height="60">
  </a>
</p>
