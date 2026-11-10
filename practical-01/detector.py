from collections import Counter

failed_ips = Counter()

with open("auth.log", "r") as file:
    for line in file:
        if "status=FAILED" in line:
            for part in line.split():
                if part.startswith("ip="):
                    ip = part.split("=")[1]
                    failed_ips[ip] += 1

print("\nCYBERSECURITY LOG ANALYZER")
print("==========================")

for ip, count in sorted(failed_ips.items()):
    print(f"{ip}: {count} failed attempts")

    if count >= 3:
        print("ALERT: Suspicious login activity!")
    else:
        print("Status: Below alert threshold")

print("\nInvestigation complete.")
