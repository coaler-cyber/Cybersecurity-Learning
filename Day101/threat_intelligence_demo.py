def analyze_ioc(iocs):
    print("🧠 Threat Intelligence Report:")
    for ioc in iocs:
        if ioc.endswith(".exe"):
            print(f"🚨 IOC: {ioc} → Suspicious file (possible malware)")
        elif ioc.startswith("192.168"):
            print(f"⚠️ IOC: {ioc} → Internal IP, check for lateral movement")
        elif "example.com" in ioc:
            print(f"⚠️ IOC: {ioc} → Malicious domain detected")
        elif len(ioc) == 32:
            print(f"🔑 IOC: {ioc} → Possible MD5 hash of malware")
        else:
            print(f"ℹ️ IOC: {ioc} → No threat detected")

if __name__ == "__main__":
    sample_iocs = [
        "malware.exe",
        "192.168.1.50",
        "bad.example.com",
        "44d88612fea8a8f36de82e1278abb02f",
        "normal.docx"
    ]
    analyze_ioc(sample_iocs)
