def purple_team_workflow(event):
    print(f"🟣 Purple Team Exercise for event: {event}")
    if "phishing" in event.lower():
        print("   🔴 Red Team: Simulate phishing attack")
        print("   🔵 Blue Team: Detect via SIEM → Block domain → Notify users")
    elif "malware" in event.lower():
        print("   🔴 Red Team: Deploy malware payload")
        print("   🔵 Blue Team: Detect via EDR → Isolate endpoint → Remediate")
    elif "brute force" in event.lower():
        print("   🔴 Red Team: Attempt brute force login")
        print("   🔵 Blue Team: Detect via logs → Lock account → Enforce MFA")
    else:
        print("   🔴 Red Team: Simulate generic attack")
        print("   🔵 Blue Team: Monitor & improve detection rules")

if __name__ == "__main__":
    events = [
        "Phishing email campaign",
        "Malware detected on endpoint",
        "Brute force login attempts",
        "Normal system update"
    ]
    for e in events:
        purple_team_workflow(e)
