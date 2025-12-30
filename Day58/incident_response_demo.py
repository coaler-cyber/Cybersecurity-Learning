def incident_response(logs):
    for log in logs:
        if "malware" in log.lower():
            print(f"⚠️ Phát hiện malware: {log}")
            print("👉 Action: Isolate infected system")
        elif "failed login" in log.lower():
            print(f"⚠️ Phát hiện brute force: {log}")
            print("👉 Action: Lock account, enable MFA")
        elif "data exfiltration" in log.lower():
            print(f"❌ Phát hiện rò rỉ dữ liệu: {log}")
            print("👉 Action: Block traffic, investigate source")

if __name__ == "__main__":
    sample_logs = [
        "2025-12-30 Malware detected on host 192.168.1.10",
        "2025-12-30 Failed login attempt from 192.168.1.20",
        "2025-12-30 Data exfiltration detected via port 443"
    ]
    incident_response(sample_logs)
