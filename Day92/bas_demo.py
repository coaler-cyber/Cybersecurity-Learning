def bas_simulation():
    scenarios = [
        {"attack": "Phishing Email", "expected_detection": True, "expected_response": "Block domain, alert users"},
        {"attack": "Brute Force Login", "expected_detection": True, "expected_response": "Block IP, enforce MFA"},
        {"attack": "SQL Injection", "expected_detection": True, "expected_response": "Patch code, block query"},
        {"attack": "Data Exfiltration", "expected_detection": False, "expected_response": "Investigate anomaly"}
    ]

    print("🧪 Breach & Attack Simulation Report:")
    for s in scenarios:
        print(f"\n🔴 Attack: {s['attack']}")
        print(f"   ✅ Expected Detection: {s['expected_detection']}")
        print(f"   🛡️ Expected Response: {s['expected_response']}")

if __name__ == "__main__":
    bas_simulation()
