def incident_response(logs):
    for log in logs:
        if "malware" in log.lower():
            print(f"🚨 Detection: {log}")
            print("🔍 Analysis: Malware found on host")
            print("🛑 Containment: Isolate infected host")
            print("🧹 Eradication: Remove malware")
            print("🔄 Recovery: Restore system from backup")
            print("📘 Lessons Learned: Update malware signatures\n")
        elif "sql injection" in log.lower():
            print(f"🚨 Detection: {log}")
            print("🔍 Analysis: SQL Injection attempt")
            print("🛑 Containment: Block malicious query")
            print("🧹 Eradication: Patch vulnerable code")
            print("🔄 Recovery: Restart web service")
            print("📘 Lessons Learned: Improve input validation\n")

if __name__ == "__main__":
    sample_logs = [
        "2026-01-04 Malware detected on host 192.168.1.200",
        "2026-01-04 SQL Injection attempt on /login"
    ]
    incident_response(sample_logs)
