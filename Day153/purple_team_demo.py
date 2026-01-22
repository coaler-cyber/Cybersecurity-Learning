def purple_team_exercise(event):
    print(f"🟣 Purple Team Exercise: {event['scenario']}")
    
    if event.get("red_team_attack"):
        print("🔴 Red Team: Attack executed")
    else:
        print("🔴 Red Team: No attack")
    
    if event.get("blue_team_response"):
        print("🔵 Blue Team: Response successful")
    else:
        print("🔵 Blue Team: Response failed")
    
    if event.get("knowledge_shared"):
        print("🟣 Purple Team: Knowledge shared → Security improved")
    else:
        print("🟣 Purple Team: No knowledge sharing → Missed opportunity")

if __name__ == "__main__":
    scenario_example = {
        "scenario": "Phishing + Malware Injection",
        "red_team_attack": True,
        "blue_team_response": True,
        "knowledge_shared": True
    }
    purple_team_exercise(scenario_example)
