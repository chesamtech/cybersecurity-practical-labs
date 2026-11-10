# Practical 05: SOC Security Log Analyzer

Author: Samuel Njenga

## Objective
Build a Python tool that analyses authentication
logs and detects repeated failed login attempts.

## Technologies
- Python 3
- Termux
- Collections Counter

## Features
- Counts failed login attempts by IP.
- Counts successful logins by IP.
- Detects repeated failures.
- Generates security alerts.
- Produces an investigation summary.

## Detection Threshold
Three or more failed attempts per IP.

## Test Results
- Events analysed: 8
- Failed attempts: 6
- Successful logins: 2
- Alerts generated: 2

## Files
- analyzer.py: Python detection program.
- security.log: Simulated authentication events.
- incident-report.md: Investigation report.

## Conclusion
This project demonstrates basic SOC monitoring
and Python security automation.
