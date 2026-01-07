def threat_hunting(logs):
    print("🕵️ Threat Hunting Report:")
    for log in logs:
        if "failed login" in log.lower():
            print(f"⚠️ Suspicious: {log} → Possible brute force attack")
        elif "powershell" in log.lower():
            print(f"🚨 Suspicious: {log} → Possible malicious script execution")
        elif "data exfiltration" in log.lower():
            print(f"🚨 Critical: {log} → Possible data theft")
        else:
            print(f"ℹ️ Normal log: {log}")

if __name__ == "__main__":
    sample_logs = [
        "User failed login attempt from 203.0.113.5",
        "Powershell command executed on endpoint",
        "Data exfiltration detected to external server",
        "System update completed successfully"
    ]
    threat_hunting(sample_logs)
