def blue_team_workflow(event):
    print(f"🛡️ Blue Team Response for event: {event}")
    if "malware" in event.lower():
        print("   Action: Detect via EDR → Isolate endpoint → Remediate")
    elif "phishing" in event.lower():
        print("   Action: Detect via SIEM → Block domain → Notify users")
    elif "brute force" in event.lower():
        print("   Action: Detect via logs → Lock account → Enforce MFA")
    else:
        print("   Action: Monitor event → No immediate action")

if __name__ == "__main__":
    events = [
        "Malware detected on workstation",
        "Phishing email reported",
        "Brute force login attempts",
        "Normal system update"
    ]
    for e in events:
        blue_team_workflow(e)
