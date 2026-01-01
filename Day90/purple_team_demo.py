def red_team_attack():
    attacks = [
        "Phishing email sent",
        "Brute force login attempt",
        "SQL Injection attempt"
    ]
    print("🔴 Red Team Attacks:")
    for a in attacks:
        print(f"   - {a}")
    return attacks

def blue_team_response(attacks):
    print("\n🔵 Blue Team Responses:")
    responses = []
    for a in attacks:
        if "phishing" in a.lower():
            responses.append("Block domain, train users")
        elif "brute force" in a.lower():
            responses.append("Block IP, enforce MFA")
        elif "sql injection" in a.lower():
            responses.append("Patch code, block query")
    return responses

def purple_team_collaboration():
    attacks = red_team_attack()
    responses = blue_team_response(attacks)
    print("\n🟣 Purple Team Collaboration:")
    for a, r in zip(attacks, responses):
        print(f"   Attack: {a} → Response: {r}")

if __name__ == "__main__":
    purple_team_collaboration()
