def red_team_attack(target):
    print(f"🎯 Red Team Attack Simulation on: {target['name']}")
    
    if target.get("phishing_success"):
        print("🚨 Phishing attack successful → Credentials compromised")
    else:
        print("✅ Phishing attack failed")
    
    if target.get("vulnerability_exploited"):
        print("🚨 Vulnerability exploited → System access gained")
    else:
        print("✅ No vulnerability exploited")
    
    if target.get("physical_breach"):
        print("🚨 Physical breach successful → Unauthorized entry")
    else:
        print("✅ Physical security intact")
    
    if target.get("lateral_movement"):
        print("🚨 Lateral movement detected → Multiple systems compromised")
    else:
        print("✅ No lateral movement")

if __name__ == "__main__":
    target_example = {
        "name": "CorporateNetwork",
        "phishing_success": True,
        "vulnerability_exploited": True,
        "physical_breach": False,
        "lateral_movement": True
    }
    red_team_attack(target_example)
