def incident_response(event):
    print(f"🚨 Incident Response Workflow for: {event}")
    print("➡️ Preparation: Ensure playbooks & tools ready")
    print("➡️ Detection & Analysis: Identify incident via SIEM/EDR")
    print("➡️ Containment: Isolate affected systems")
    print("➡️ Eradication: Remove malware / patch vulnerability")
    print("➡️ Recovery: Restore systems & validate integrity")
    print("➡️ Lessons Learned: Document findings & improve process")

if __name__ == "__main__":
    events = [
        "Malware outbreak in network",
        "Phishing campaign detected",
        "Unauthorized access to admin account"
    ]
    for e in events:
        incident_response(e)
