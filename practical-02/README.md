# Practical 02: Network Security Assessment

Author: Samuel Njenga

## Objective
Use Nmap to inspect the local Android device for
open TCP ports and identify available services.

## Tool
Nmap 7.993 running on Termux (Android).

## Target
127.0.0.1 (localhost)

## Command
nmap -sT -sV 127.0.0.1

## Findings
- Host status: Up
- TCP ports scanned: 1,000
- Open TCP ports: 0
- Closed TCP ports: 1,000
- Scan duration: Approximately 4.92 seconds

## Analysis
No open TCP ports were identified among the
1,000 default ports scanned.

This is a baseline assessment of the local
device, not a complete security audit.

## Conclusion
The scan completed successfully. Further
authorised testing can examine additional
network configurations and services.
