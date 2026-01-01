def soar_workflow(alert):
    print(f"🚨 Alert received: {alert}")
    print("🔗 Orchestration: Kết nối SIEM, TIP, Firewall")
    if "malware" in alert.lower():
        print("🤖 Automation: Quét host, cô lập, gỡ bỏ malware")
    elif "phishing" in alert.lower():
        print("🤖 Automation: Block domain, cảnh báo người dùng")
    elif "sql injection" in alert.lower():
        print("🤖 Automation: Block query, patch code")
    else:
        print("🤖 Automation: Log sự kiện để phân tích thêm")
    print("✅ Response: Báo cáo SOC analyst, cập nhật IOC\n")

if __name__ == "__main__":
    alerts = [
        "Malware detected on host 192.168.1.200",
        "Phishing email campaign detected",
        "SQL Injection attempt on /login"
    ]
    for a in alerts:
        soar_workflow(a)
