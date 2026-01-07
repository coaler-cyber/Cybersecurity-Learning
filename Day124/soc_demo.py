def soc_workflow(event):
    print(f"🏢 SOC Handling Event: {event}")
    if "malware" in event.lower():
        print("   Step 1: Detect via SIEM/EDR")
        print("   Step 2: Isolate endpoint")
        print("   Step 3: Remediate & report")
    elif "phishing" in event.lower():
        print("   Step 1: Detect via SIEM")
        print("   Step 2: Block domain & alert users")
        print("   Step 3: Report incident")
    elif "brute force" in event.lower():
        print("   Step 1: Detect via logs")
        print("   Step 2: Lock account & enforce MFA")
        print("   Step 3: Report incident")
    else:
        print("   Step 1: Monitor event")
        print("   Step 2: No immediate action")

if __name__ == "__main__":
    events = [
        "Malware detected on server",
        "Phishing email campaign",
        "Brute force login attempts",
        "Normal system update"
    ]
    for e in events:
        soc_workflow(e)
