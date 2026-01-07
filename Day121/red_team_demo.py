def red_team_workflow(target):
    print(f"🎯 Red Team Engagement on target: {target}")
    steps = [
        "Reconnaissance → Collect domain, IP, employee info",
        "Exploitation → Exploit vulnerable service",
        "Lateral Movement → Pivot to internal network",
        "Persistence → Create backdoor account",
        "Exfiltration → Extract sensitive data",
        "Reporting → Document findings & recommendations"
    ]
    for s in steps:
        print(f"➡️ {s}")

if __name__ == "__main__":
    target = "example-corp.com"
    red_team_workflow(target)
