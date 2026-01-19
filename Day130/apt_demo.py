def apt_workflow(target):
    print(f"🎯 APT Simulation on target: {target}")
    steps = [
        "Initial Access → Phishing email with malicious attachment",
        "Establish Foothold → Install backdoor malware",
        "Escalation → Gain admin privileges",
        "Lateral Movement → Pivot to internal servers",
        "Persistence → Create hidden scheduled tasks",
        "Exfiltration → Steal sensitive documents"
    ]
    for s in steps:
        print(f"➡️ {s}")

if __name__ == "__main__":
    target = "corporate-network.local"
    apt_workflow(target)
