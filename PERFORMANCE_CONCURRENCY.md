# Performance & Concurrency Policy

General repository engineering follows bounded, measurable concurrency: parallelize independent work, avoid shared mutable state, cap workers, and preserve deterministic test modes.

Security-sensitive brute-force, credential-search, private-key-search, or recovery workflows are intentionally excluded from performance acceleration. Do not add worker pools or parallel search that increases key-guessing throughput.

For benign parsing, reporting, and I/O helpers, use bounded concurrency only when benchmarks demonstrate a benefit and correctness remains unchanged.
