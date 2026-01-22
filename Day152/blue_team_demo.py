def blue_team_defense(event):
    print(f"🛡️ Blue Team Defense triggered for: {event}")
    
    if "malware" in event.lower():
        print("   Action: Isolate endpoint → Run AV scan → Notify SOC")
    elif "phishing" in event.lower():
        print("   Action: Block sender → Alert users → Update email filters")
    elif "brute force" in event.lower():
        print("   Action: Lock account → Enforce MFA → Monitor login attempts")
    elif "data exfiltration" in event.lower():
        print("   Action: Block traffic → Investigate → Report incident")
    else:
        print("   Action: Monitor event → No immediate action")

if __name__ == "__main__":
    events = [
        "Malware detected on workstation",
        "Phishing email attempt",
        "Brute force login detected",
        "Data exfiltration attempt",
        "Normal system update"
    ]
    for e in events:
        blue_team_defense(e)
