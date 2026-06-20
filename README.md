# File-Integrity-Checker
A Python script that uses SHA-256 hashing to detect whether a file has been modified or tampered with.

## Security Context

File integrity monitoring is the core mechanism behind real-world Host Intrusion Detection Systems (HIDS). This tool implements the same fundamental principle: store a known-good hash, compare it against the current file state, alert on mismatch.

**Threat model:** An attacker who gains write access to a system may 
modify config files, binaries, or logs to maintain persistence or 
cover tracks. This tool detects such modifications.

## Technical implementation

- Module:hashlib  (Python standard library)
- Algorithm: SHA-256 (256-bit digest, collision resistant)
- File reading: binary mode (`rb`) to handle all file types


## What it does
- Generates a unique hash (fingerprint) of a file's contents
- Compares current file hash against a stored hash
- Alerts if the file has been changed

## How to run
1. Install Python 3
2. Run: python integrity_checker.py
3. The script demonstrates integrity checking on a sample test file







## Technical implementation

- Module: `hashlib

` (Python standard library)
- Algorithm: SHA-256 (256-bit digest, collision resistant)
- File reading: binary mode (`rb`) to handle all file types



## What I learned

- How SHA-256 hashing works at the code level
- Why integrity monitoring is the 'I' in the CIA Triad
- How HIDS systems detect post-compromise file modification
- Binary file reading for accurate hash computation
