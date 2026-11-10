# Security Incident Investigation Report

Author: Samuel Njenga

## Project
Practical 05: SOC Security Log Analyzer

## Objective
Analyse authentication logs to identify repeated
failed login attempts and generate security alerts.

## Summary
- Total events analysed: 8
- Failed login events: 6
- Successful login events: 2
- Suspicious IP alerts: 2

## Findings

### IP: 192.0.2.10
- Failed attempts: 3
- Alert generated: Yes

### IP: 192.0.2.20
- Successful logins: 1
- Failed attempts: 0

### IP: 192.0.2.30
- Failed attempts: 3
- Successful logins: 1
- Alert generated: Yes
- Recommendation: Investigate the sequence of
  failed and successful authentication events.

## Detection Rule
Generate an alert when an IP address records
three or more failed login attempts.

## Limitations
The logs are simulated training data using
documentation-only IP addresses.
The alert threshold is educational and does
not prove malicious activity.

## Conclusion
The Python analyzer successfully processed
the sample logs and identified two IP addresses
requiring further investigation.
