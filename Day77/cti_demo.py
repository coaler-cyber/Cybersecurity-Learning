def analyze_ttp(logs):
    for log in logs:
        if "phishing" in log.lower():
            print("🎯 Tactic: Initial Access")
            print("🔧 Technique: Phishing (MITRE ATT&CK T1566)")
            print("📘 Procedure: Email giả mạo với link độc hại\n")
        elif "credential dumping" in log.lower():
            print("🎯 Tactic: Credential Access")
            print("🔧 Technique: Credential Dumping (MITRE ATT&CK T1003)")
            print("📘 Procedure: Dùng mimikatz để lấy mật khẩu\n")
        elif "persistence" in log.lower():
            print("🎯 Tactic: Persistence")
            print("🔧 Technique: Registry Run Keys (MITRE ATT&CK T1547)")
            print("📘 Procedure: Thêm key khởi động trong registry\n")

if __name__ == "__main__":
    sample_logs = [
        "2026-01-05 Phishing email detected",
        "2026-01-05 Credential Dumping attempt",
        "2026-01-05 Persistence via registry key"
    ]
    analyze_ttp(sample_logs)
