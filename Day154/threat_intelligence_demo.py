def threat_feed_parser(feed):
    print("🧠 Threat Intelligence Feed Report:")
    for item in feed:
        if item['type'] == "IP":
            print(f"🔍 Malicious IP detected: {item['value']}")
        elif item['type'] == "Domain":
            print(f"🌐 Malicious Domain detected: {item['value']}")
        elif item['type'] == "Hash":
            print(f"💾 Malicious File Hash detected: {item['value']}")
        else:
            print(f"ℹ️ Unknown IOC type: {item['value']}")

if __name__ == "__main__":
    threat_feed = [
        {"type": "IP", "value": "192.168.1.100"},
        {"type": "Domain", "value": "malicious-site.com"},
        {"type": "Hash", "value": "abcd1234efgh5678"}
    ]
    threat_feed_parser(threat_feed)
