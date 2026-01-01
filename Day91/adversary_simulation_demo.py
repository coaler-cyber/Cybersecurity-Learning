def adversary_simulation():
    ttp = [
        {"tactic": "Initial Access", "technique": "Phishing (T1566)", "procedure": "Gửi email giả mạo với link độc hại"},
        {"tactic": "Execution", "technique": "PowerShell (T1059)", "procedure": "Chạy script PowerShell tải malware"},
        {"tactic": "Persistence", "technique": "Registry Run Keys (T1547)", "procedure": "Thêm key khởi động trong registry"},
        {"tactic": "Exfiltration", "technique": "Data Exfiltration over HTTPS (T1041)", "procedure": "Gửi dữ liệu ra ngoài qua HTTPS"}
    ]

    print("🎭 Adversary Simulation theo MITRE ATT&CK:")
    for step in ttp:
        print(f"🎯 Tactic: {step['tactic']}")
        print(f"🔧 Technique: {step['technique']}")
        print(f"📘 Procedure: {step['procedure']}\n")

if __name__ == "__main__":
    adversary_simulation()
