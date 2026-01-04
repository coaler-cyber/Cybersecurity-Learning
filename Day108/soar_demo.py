def soar_playbook(event):
    print(f"📂 SOAR Playbook triggered for event: {event}")
    if "malware" in event.lower():
        print("   Action: Isolate endpoint → Notify SOC → Create case")
    elif "phishing" in event.lower():
        print("   Action: Block domain → Alert users → Create case")
    elif "brute force" in event.lower():
        print("   Action: Lock account → Enforce MFA → Create case")
    else:
        print("   Action: Log event → Monitor → No case created")

if __name__ == "__main__":
    events = [
        "Malware detected on server",
        "Phishing email reported",
        "Brute force login attempts",
        "Normal system update"
    ]
    for e in events:
        soar_playbook(e)
