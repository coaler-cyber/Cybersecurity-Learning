def xdr_response(events):
    print("🌐 XDR Response Report:")
    for e in events:
        if "endpoint malware" in e.lower():
            print(f"🚨 Event: {e} → Action: Quarantine file, isolate endpoint")
        elif "network attack" in e.lower():
            print(f"🚨 Event: {e} → Action: Block IP, update firewall rules")
        elif "email phishing" in e.lower():
            print(f"⚠️ Event: {e} → Action: Remove email, alert users")
        elif "cloud misconfig" in e.lower():
            print(f"⚠️ Event: {e} → Action: Fix config, enforce policy")
        else:
            print(f"ℹ️ Event: {e} → Action: Monitor only")

if __name__ == "__main__":
    sample_events = [
        "Endpoint malware detected",
        "Network attack from 203.0.113.5",
        "Email phishing attempt",
        "Cloud misconfig detected",
        "Normal system update"
    ]
    xdr_response(sample_events)
