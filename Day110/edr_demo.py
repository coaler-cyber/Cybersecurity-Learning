def edr_response(events):
    print("🖥️ EDR Response Report:")
    for e in events:
        if "malware" in e.lower():
            print(f"🚨 Event: {e} → Action: Kill process, quarantine file, isolate endpoint")
        elif "ransomware" in e.lower():
            print(f"🚨 Event: {e} → Action: Stop encryption, disconnect network, alert SOC")
        elif "unauthorized access" in e.lower():
            print(f"⚠️ Event: {e} → Action: Lock account, investigate logs")
        else:
            print(f"ℹ️ Event: {e} → Action: Monitor only")

if __name__ == "__main__":
    sample_events = [
        "Malware detected in temp folder",
        "Ransomware activity detected",
        "Unauthorized access to admin account",
        "Normal system update"
    ]
    edr_response(sample_events)
