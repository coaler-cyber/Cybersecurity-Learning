def siem_rules(logs):
    alerts = []
    failed_login_count = 0
    for log in logs:
        if "failed login" in log.lower():
            failed_login_count += 1
        if "malware" in log.lower():
            alerts.append(("🚨 Malware detected", log))
        if "sql injection" in log.lower():
            alerts.append(("❌ SQL Injection attempt", log))

    if failed_login_count > 3:
        alerts.append(("⚠️ Brute force suspected", f"{failed_login_count} failed logins detected"))

    return alerts

if __name__ == "__main__":
    sample_logs = [
        "2026-01-02 Failed login attempt from 192.168.1.50",
        "2026-01-02 Failed login attempt from 192.168.1.50",
        "2026-01-02 Failed login attempt from 192.168.1.50",
        "2026-01-02 Failed login attempt from 192.168.1.50",
        "2026-01-02 Malware detected on host 192.168.1.100",
        "2026-01-02 SQL Injection attempt on /login"
    ]
    alerts = siem_rules(sample_logs)
    for alert, log in alerts:
        print(alert, "→", log)
