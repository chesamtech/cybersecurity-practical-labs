# Practical 06: SQL Injection Detection and Prevention

Author: Samuel Njenga

## Objective
Understand SQL Injection and demonstrate how
parameterized SQL queries prevent login bypass.

## Environment
- Android
- Termux
- Python 3
- SQLite

## Tests Conducted

### Test 1: Normal Login
Result: Successful

### Test 2: SQL Injection
Result: Vulnerability demonstrated.
The simulated input bypassed authentication
in the vulnerable login function.

### Test 3: Secure Login
Result: Injection blocked.
The parameterized query treated the input
as data rather than executable SQL.

## Security Lessons
- Never concatenate untrusted input into SQL.
- Use parameterized queries.
- Validate user input.
- Store passwords using secure password hashing.
- Avoid exposing database errors to users.

## Conclusion
The experiment demonstrated SQL Injection
and the importance of secure database queries.
