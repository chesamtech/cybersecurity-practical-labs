import re

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add a number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add a special character.")

    print("\nPASSWORD SECURITY REPORT")
    print("------------------------")

    if score <= 2:
        print("Strength: WEAK")
    elif score <= 4:
        print("Strength: MODERATE")
    else:
        print("Strength: STRONG")

    print("Score:", score, "/ 5")

    if feedback:
        print("\nRecommendations:")
        for item in feedback:
            print("-", item)

password = input("Enter a TEST password: ")
check_password(password)
