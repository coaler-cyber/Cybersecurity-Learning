def red_team_attack():
    print("🔴 Red Team: Thử SQL Injection...")
    attack = "SELECT * FROM users WHERE username='admin' AND password='' OR '1'='1'"
    return attack

def blue_team_defense(query):
    print("🔵 Blue Team: Giám sát query...")
    if "' OR '1'='1" in query:
        print("⚠️ Phát hiện SQL Injection!")
        print("👉 Action: Block query, alert SOC")
    else:
        print("✅ Query an toàn.")

if __name__ == "__main__":
    attack_query = red_team_attack()
    print("Red Team query:", attack_query)
    blue_team_defense(attack_query)
