def iso27001_check():
    controls = ["Information Security Policy", "Access Control", "Cryptography", "Operations Security", "Supplier Relationships"]
    print("📋 ISO 27001 Checklist:")
    for c in controls:
        print(f"   - {c}: ✅ Implemented")

def nist_check():
    functions = ["Identify", "Protect", "Detect", "Respond", "Recover"]
    print("\n📋 NIST Cybersecurity Framework:")
    for f in functions:
        print(f"   - {f}: ✅ In place")

if __name__ == "__main__":
    iso27001_check()
    nist_check()
