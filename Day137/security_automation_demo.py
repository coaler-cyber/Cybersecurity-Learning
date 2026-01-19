def security_automation(event):
    print(f"🤖 Security Automation triggered for: {event}")
    if "malware" in event.lower():
        print("   Action: Isolate endpoint → Notify SOC → Remediate")
    elif "phishing" in event.lower():
        print("   Action: Block domain → Alert users → Update SIEM")
    elif "brute force" in event.lower():
        print("   Action: Lock account → Enforce MFA → Notify admin")
    else:
        print("   Action: Monitor event → No immediate action")

if __name__ == "__main__":
    events = [
        "Malware detected on workstation",
        "Phishing email campaign",
        "Brute force login attempts",
        "Normal system update"
    ]
    for e in events:
        security_automation(e)
