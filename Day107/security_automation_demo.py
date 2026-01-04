def automate_security(events):
    print("🤖 Security Automation Report:")
    for e in events:
        if "malware" in e.lower():
            print(f"🚨 Event: {e} → Action: Isolate endpoint, alert SOC")
        elif "phishing" in e.lower():
            print(f"⚠️ Event: {e} → Action: Block domain, notify users")
        elif "failed login" in e.lower():
            print(f"⚠️ Event: {e} → Action: Lock account, enforce MFA")
        else:
            print(f"ℹ️ Event: {e} → Action: Log & monitor")

if __name__ == "__main__":
    sample_events = [
        "Malware detected on workstation",
        "Phishing email received by user",
        "Multiple failed login attempts",
        "Normal system update"
    ]
    automate_security(sample_events)
