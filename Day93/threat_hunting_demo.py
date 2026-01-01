def threat_hunt(logs):
    print("🔍 Threat Hunting Report:")
    for log in logs:
        if "powershell" in log.lower():
            print(f"⚠️ Suspicious activity: {log} → Possible ATT&CK T1059 (PowerShell Execution)")
        elif "mimikatz" in log.lower():
            print(f"🚨 Suspicious activity: {log} → Possible ATT&CK T1003 (Credential Dumping)")
        elif "external ip" in log.lower():
            print(f"⚠️ Suspicious activity: {log} → Possible Data Exfiltration")
        else:
            print(f"ℹ️ Normal log: {log}")

if __name__ == "__main__":
    sample_logs = [
        "2026-01-07 PowerShell script executed on host",
        "2026-01-07 Mimikatz process detected",
        "2026-01-07 Large data transfer to external IP",
        "2026-01-07 User login successful"
    ]
    threat_hunt(sample_logs)
