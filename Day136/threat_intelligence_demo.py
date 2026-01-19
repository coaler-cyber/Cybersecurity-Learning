def analyze_ioc(ioc_list):
    print("🧠 Threat Intelligence Report:")
    for ioc in ioc_list:
        if ioc.endswith(".exe"):
            print(f"🚨 Malicious file detected: {ioc}")
        elif ioc.startswith("http://") or ioc.startswith("https://"):
            print(f"⚠️ Suspicious URL: {ioc}")
        elif ioc.count(".") == 3:
            print(f"⚠️ Suspicious IP: {ioc}")
        else:
            print(f"ℹ️ Unknown IOC type: {ioc}")

if __name__ == "__main__":
    iocs = [
        "malware_payload.exe",
        "http://malicious-domain.com",
        "192.168.1.100",
        "random_string"
    ]
    analyze_ioc(iocs)
