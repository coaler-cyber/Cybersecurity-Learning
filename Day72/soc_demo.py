def soc_monitor(logs):
    alerts = []
    for log in logs:
        if "failed login" in log.lower():
            alerts.append(("⚠️ Failed login detected", log))
        elif "malware" in log.lower():
            alerts.append(("🚨 Malware detected", log))
        elif "sql injection" in log.lower():
            alerts.append(("❌ SQL Injection attempt", log))
    return alerts

if __name__ == "__main__":
    sample_logs = [
        "2026-01-01 Failed login attempt from 192.168.1.50",
        "2026-01-01 Malware detected on host 192.168.1.100",
        "2026-01-01 SQL Injection attempt on /login"
    ]
    alerts = soc_monitor(sample_logs)
    for alert, log in alerts:
        print(alert, "→", log)
