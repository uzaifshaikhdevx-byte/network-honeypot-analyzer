# Network Decoy Honeypot & Threat Log Analyzer

A lightweight Python-based network decoy designed to detect unauthorized access attempts, capture brute-force credential stuffing, and generate threat audit logs.

## Features
- **TCP Decoy Listener:** Listens on port `2222` emulating a basic server authentication prompt using socket programming.
- **Forensic Audit Logging:** Records timestamps, remote client IP addresses, attempted usernames, and passwords to `attacks.log`.
- **Threat Log Analysis:** Parses raw logs using Python's `Counter` module to identify high-frequency targets and brute-force patterns.

## Tech Stack
- **Language:** Python 3
- **Libraries:** `socket`, `collections`, `datetime`
- **Protocol:** TCP/IP

## How to Run

1. **Start the Decoy Listener:**
   ```bash
   python honeypot.py
