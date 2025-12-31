def blue_team_monitor(logs):
    for log in logs:
        if "port scan" in log.lower():
            print(f"⚠️ Phát hiện port scan: {log}")
            print("👉 Action: Block source IP")
        elif "sql injection" in log.lower():
            print(f"❌ Phát hiện SQL Injection: {log}")
            print("👉 Action: Enable WAF rules")
        elif "malware" in log.lower():
            print(f"🚨 Phát hiện malware: {log}")
            print("👉 Action: Isolate infected host")

if __name__ == "__main__":
    sample_logs = [
        "2025-12-31 Port scan detected from 192.168.1.100",
        "2025-12-31 SQL Injection attempt on /login",
        "2025-12-31 Malware detected on host 192.168.1.200"
    ]
    blue_team_monitor(sample_logs)
