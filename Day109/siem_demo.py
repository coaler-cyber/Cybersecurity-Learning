def siem_analysis(logs):
    print("📊 SIEM Analysis Report:")
    for log in logs:
        if "failed login" in log.lower():
            print(f"⚠️ Alert: {log} → Possible brute force attack")
        elif "malware" in log.lower():
            print(f"🚨 Alert: {log} → Malware detected")
        elif "phishing" in log.lower():
            print(f"⚠️ Alert: {log} → Phishing attempt")
        else:
            print(f"ℹ️ Normal log: {log}")

if __name__ == "__main__":
    sample_logs = [
        "User failed login attempt from 203.0.113.5",
        "Malware detected on endpoint",
        "Phishing email reported by user",
        "System update completed successfully"
    ]
    siem_analysis(sample_logs)
