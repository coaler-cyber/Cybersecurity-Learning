def audit_system(system):
    checklist = {
        "Firewall Enabled": True,
        "Antivirus Updated": True,
        "Password Policy Enforced": False,
        "Encryption Enabled": True,
        "Logging Enabled": False
    }

    print(f"📋 Security Audit Report for {system}:")
    for item, status in checklist.items():
        if status:
            print(f"   ✅ {item}")
        else:
            print(f"   ❌ {item} - Needs remediation")

if __name__ == "__main__":
    audit_system("Corporate Network")
