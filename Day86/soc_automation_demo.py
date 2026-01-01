def soc_playbook(alert):
    print(f"🚨 Alert received: {alert}")
    if "malware" in alert.lower():
        print("🔍 Action: Scan affected host")
        print("🛑 Action: Isolate host from network")
        print("🧹 Action: Remove malware")
        print("✅ Action: Restore system\n")
    elif "failed login" in alert.lower():
        print("🔍 Action: Check login source IP")
        print("🛑 Action: Block IP if brute force suspected")
        print("✅ Action: Notify SOC analyst\n")
    elif "sql injection" in alert.lower():
        print("🔍 Action: Block malicious query")
        print("🧹 Action: Patch vulnerable code")
        print("✅ Action: Restart web service\n")
    else:
        print("ℹ️ Action: Log event for further analysis\n")

if __name__ == "__main__":
    alerts = [
        "Malware detected on host 192.168.1.200",
        "Multiple failed login attempts from 203.0.113.50",
        "SQL Injection attempt on /login"
    ]
    for a in alerts:
        soc_playbook(a)
