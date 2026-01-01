def threat_hunting(logs):
    suspicious_ips = {}
    for log in logs:
        if "ssh failed login" in log.lower():
            ip = log.split()[-1]
            suspicious_ips[ip] = suspicious_ips.get(ip, 0) + 1

    for ip, count in suspicious_ips.items():
        if count > 3:
            print(f"⚠️ Threat Hunting: Phát hiện brute force SSH từ {ip} ({count} lần)")
            print("👉 Action: Block IP, alert SOC")

if __name__ == "__main__":
    sample_logs = [
        "2026-01-03 SSH failed login from 192.168.1.50",
        "2026-01-03 SSH failed login from 192.168.1.50",
        "2026-01-03 SSH failed login from 192.168.1.50",
        "2026-01-03 SSH failed login from 192.168.1.50",
        "2026-01-03 SSH failed login from 203.0.113.10"
    ]
    threat_hunting(sample_logs)
