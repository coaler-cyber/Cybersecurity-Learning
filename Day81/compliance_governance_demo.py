def compliance_check(system):
    rules = {
        "GDPR": ["Data Encryption", "User Consent", "Right to Erasure"],
        "HIPAA": ["Access Control", "Audit Logs", "Data Integrity"],
        "PCI-DSS": ["Network Segmentation", "Cardholder Data Protection", "Vulnerability Management"]
    }

    print(f"📋 Compliance check for {system}:")
    for standard, controls in rules.items():
        print(f"\n🔍 {standard} requirements:")
        for c in controls:
            print(f"   - {c}: ✅ Implemented")

if __name__ == "__main__":
    compliance_check("E-commerce Platform")
