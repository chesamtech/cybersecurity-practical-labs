import sqlite3

# Create a local training database
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE users (
    username TEXT,
    password TEXT
)
""")

cursor.execute(
    "INSERT INTO users VALUES (?, ?)",
    ("admin", "TrainingPass123")
)

cursor.execute(
    "INSERT INTO users VALUES (?, ?)",
    ("student", "StudentPass123")
)

connection.commit()


def vulnerable_login(username, password):
    print("\n--- VULNERABLE LOGIN ---")

    query = (
        "SELECT * FROM users WHERE username = '"
        + username
        + "' AND password = '"
        + password
        + "'"
    )

    print("SQL query:", query)

    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        print("LOGIN SUCCESSFUL:", result[0])
    else:
        print("LOGIN FAILED")


def secure_login(username, password):
    print("\n--- SECURE LOGIN ---")

    query = "SELECT * FROM users WHERE username = ? AND password = ?"

    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        print("LOGIN SUCCESSFUL:", result[0])
    else:
        print("LOGIN FAILED")


print("SQL INJECTION TRAINING LAB")
print("===========================")

print("\nTEST 1: Normal login")
vulnerable_login("student", "StudentPass123")

print("\nTEST 2: Simulated SQL injection")
attack_username = "' OR '1'='1' -- "
vulnerable_login(attack_username, "anything")

print("\nTEST 3: Same input against secure login")
secure_login(attack_username, "anything")

connection.close()
