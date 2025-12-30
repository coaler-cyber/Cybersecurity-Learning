def hunt_threats(logs):
    for log in logs:
        if "ssh" in log.lower() and "failed" in log.lower():
            print(f"⚠️ Phát hiện brute force SSH: {log}")
        elif "suspicious" in log.lower():
            print(f"❌ Phát hiện hoạt động đáng ngờ: {log}")
        elif "admin login" in log.lower() and "remote" in log.lower():
            print(f"🔍 Kiểm tra đăng nhập admin từ xa: {log}")

if __name__ == "__main__":
    sample_logs = [
        "2025-12-30 SSH failed login from 192.168.1.50",
        "2025-12-30 Suspicious process started on host 192.168.1.60",
        "2025-12-30 Admin login remote from 203.0.113.10"
    ]
    hunt_threats(sample_logs)
