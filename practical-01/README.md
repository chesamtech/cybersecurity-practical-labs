# Practical 01: Security Log Monitoring

## Project Overview
A beginner cybersecurity project that uses Python
to analyse simulated authentication logs and detect
repeated failed login attempts.

## Objectives
- Understand authentication logs.
- Identify failed login attempts.
- Count failed attempts by IP address.
- Generate alerts for suspicious activity.

## Tools Used
- Android
- Termux
- Python 3
- Git

## Detection Rule
An IP address generating 3 or more failed
login attempts triggers a security alert.

## Execution
Run:

python detector.py

## Expected Findings
- 192.0.2.10: 3 failed attempts
- 192.0.2.30: 3 failed attempts

Both trigger security alerts.

## Disclaimer
All log entries are simulated for educational
purposes. No real systems were attacked.

## Author
Samuel Njenga
