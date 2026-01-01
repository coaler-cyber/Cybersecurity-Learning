class ThreatIntelPlatform:
    def __init__(self):
        self.iocs = {"ips": [], "hashes": [], "domains": []}

    def collect(self, category, value):
        self.iocs[category].append(value)
        print(f"📥 Collected {category}: {value}")

    def normalize(self):
        print("⚙️ Normalizing data to STIX format (mô phỏng)...")
        for category, values in self.iocs.items():
            for v in values:
                print(f"   {category.upper()} → {v}")

    def share(self):
        print("📡 Sharing threat intelligence with community...")
        for category, values in self.iocs.items():
            for v in values:
                print(f"   Shared {category}: {v}")

if __name__ == "__main__":
    tip = ThreatIntelPlatform()
    tip.collect("ips", "203.0.113.50")
    tip.collect("hashes", "deadbeefcafebabe")
    tip.collect("domains", "phishing-login.net")
    tip.normalize()
    tip.share()
