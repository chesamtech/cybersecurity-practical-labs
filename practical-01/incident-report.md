# Security Incident Investigation Report

## 1. Incident Type
Repeated failed authentication attempts.

## 2. Investigation Environment
Android Termux and Python.

## 3. Evidence
The simulated authentication log contained
seven records.

## 4. Findings
IP 192.0.2.10 generated 3 failed attempts.

IP 192.0.2.30 generated 3 failed attempts.

IP 192.0.2.20 recorded one successful login
and no failed attempts.

## 5. Detection
The Python script flagged both IP addresses
because they reached the threshold of 3 failures.

## 6. Recommendations
- Monitor repeated failed login attempts.
- Apply account lockout policies where appropriate.
- Investigate unusual authentication patterns.
- Enable multi-factor authentication.
- Review security logs regularly.

## 7. Conclusion
The Python detection tool successfully identified
both simulated suspicious sources.

## 8. Limitations
The dataset is simulated. The findings do not
represent a confirmed real-world attack.
