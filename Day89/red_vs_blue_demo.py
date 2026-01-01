def red_team_attack():
    attacks = [
        "Phishing email sent to employee",
        "Brute force login attempt on web portal",
        "SQL Injection attempt on /login"
    ]
    print("🔴 Red Team Attacks:")
    for a in attacks:
        print(f"   - {a}")
    return attacks

def blue_team_defense(attacks):
    print("\n🔵 Blue Team Responses:")
    for a in attacks:
        if "phishing" in a.lower():
            print("   - Detected phishing → Block domain, alert users")
        elif "brute force" in a.lower():
            print("   - Detected brute force → Block IP, enforce MFA")
        elif "sql injection" in a.lower():
            print("   - Detected SQLi → Patch code, block query")
        else:
            print("   - Log event for further analysis")

if __name__ == "__main__":
    attacks = red_team_attack()
    blue_team_defense(attacks)
