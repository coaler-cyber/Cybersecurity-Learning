def incident_response(alert):
    print(f"🚨 Incident detected: {alert}")
    print("📋 Incident Response Workflow:")
    print("1️⃣ Preparation: Policies & tools ready")
    print("2️⃣ Detection: Alert received & verified")
    print("3️⃣ Containment: Isolate affected system")
    print("4️⃣ Eradication: Remove malware / patch vulnerability")
    print("5️⃣ Recovery: Restore system & monitor")
    print("6️⃣ Lessons Learned: Document & improve\n")

if __name__ == "__main__":
    alerts = [
        "Malware detected on server",
        "Unauthorized access to database",
        "Data exfiltration attempt"
    ]
    for a in alerts:
        incident_response(a)
