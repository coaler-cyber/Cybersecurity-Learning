def share_ioc():
    iocs = {
        "malicious_ips": ["192.168.1.100", "203.0.113.50"],
        "malware_hashes": ["abcd1234efgh5678", "deadbeefcafebabe"],
        "phishing_domains": ["evil-login.com", "fake-bank.net"]
    }

    print("📡 Threat Intelligence Sharing:")
    for category, values in iocs.items():
        print(f"🔍 {category}:")
        for v in values:
            print(f"   - {v}")

if __name__ == "__main__":
    share_ioc()
