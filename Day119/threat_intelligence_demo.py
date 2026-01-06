def analyze_iocs(iocs):
    print("🕵️ Threat Intelligence Report:")
    for ioc in iocs:
        if ioc.startswith("192.168"):
            print(f"ℹ️ IOC: {ioc} → Internal IP, low risk")
        elif ioc.endswith(".ru"):
            print(f"🚨 IOC: {ioc} → Suspicious domain (possible C2)")
        elif len(ioc) == 64:
            print(f"⚠️ IOC: {ioc} → File hash, check against malware DB")
        else:
            print(f"ℹ️ IOC: {ioc} → Unknown type, needs further analysis")

if __name__ == "__main__":
    sample_iocs = [
        "192.168.1.10",
        "malicious-domain.ru",
        "d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2",
        "example.com"
    ]
    analyze_iocs(sample_iocs)
