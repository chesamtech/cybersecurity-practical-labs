# SQL Injection Security Assessment Report

Author: Samuel Njenga

## Vulnerability
SQL Injection (SQLi)

## Target
A locally hosted SQLite training database.

## Finding
The vulnerable login function constructed SQL
queries by directly concatenating user input.

## Evidence
The simulated input:

' OR '1'='1' -- 

caused the vulnerable login to return the
admin record without valid credentials.

## Impact
In a real application, similar weaknesses
could allow unauthorised database access.

## Remediation
Use parameterized SQL queries.

The secure implementation used placeholders
and passed user input separately to SQLite.

## Retest
The same simulated input failed against
the secure login function.

## Conclusion
The vulnerability was demonstrated locally
and successfully mitigated using parameterized
queries.

This was a controlled educational exercise,
not an assessment of a production website.
