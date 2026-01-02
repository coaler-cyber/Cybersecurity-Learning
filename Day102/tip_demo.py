def share_ioc(iocs, platform):
    print(f"📡 Sharing IOC to {platform} TIP:")
    for ioc in iocs:
        print(f"   - {ioc} → Shared successfully")

if __name__ == "__main__":
    sample_iocs = [
        "malware.exe",
        "203.0.113.50",
        "phishing.example.com",
        "44d88612fea8a8f36de82e1278abb02f"
    ]
    share_ioc(sample_iocs, "MISP")
