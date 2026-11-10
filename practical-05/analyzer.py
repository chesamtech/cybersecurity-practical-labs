from collections import Counter

LOG_FILE = "security.log"
THRESHOLD = 3

failed_by_ip = Counter()
successful_by_ip = Counter()
total_events = 0

with open(LOG_FILE, "r") as file:
    for line in file:
        total_events += 1

        parts = line.strip().split()

        if len(parts) < 5:
            continue

        username = parts[2].split("=")[1]
        ip_address = parts[3].split("=")[1]
        status = parts[4].split("=")[1]

        if status == "FAILED":
            failed_by_ip[ip_address] += 1

        elif status == "SUCCESS":
            successful_by_ip[ip_address] += 1

print("\nSOC SECURITY LOG ANALYZER")
print("=========================")

print("Total events:", total_events)

print("\nFAILED LOGIN ATTEMPTS")
for ip, count in failed_by_ip.items():
    print(f"{ip}: {count}")

print("\nSUCCESSFUL LOGINS")
for ip, count in successful_by_ip.items():
    print(f"{ip}: {count}")

print("\nSECURITY ALERTS")
for ip, count in failed_by_ip.items():
    if count >= THRESHOLD:
        print(f"ALERT: {ip} has {count} failed login attempts!")

print("\nINVESTIGATION COMPLETE")
