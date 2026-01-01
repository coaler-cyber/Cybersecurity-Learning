def monitor_system(logs):
    for log in logs:
        if "failed login" in log.lower():
            print(f"⚠️ Alert: {log} → Possible brute force attack")
        elif "large data transfer" in log.lower():
            print(f"🚨 Alert: {log} → Possible data exfiltration")
        elif "unauthorized access" in log.lower():
            print(f"❌ Alert: {log} → Unauthorized access detected")
        else:
            print(f"ℹ️ Normal log: {log}")

if __name__ == "__main__":
    sample_logs = [
        "2026-01-06 Failed login attempt from 192.168.1.50",
        "2026-01-06 Large data transfer to external IP",
        "2026-01-06 Unauthorized access to database",
        "2026-01-06 User login successful"
    ]
    monitor_system(sample_logs)
