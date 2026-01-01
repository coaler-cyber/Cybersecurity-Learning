def forensic_analysis(logs):
    print("🕵️ Digital Forensics Report:")
    for log in logs:
        if "deleted file" in log.lower():
            print(f"⚠️ Evidence: {log} → Possible data tampering")
        elif "usb device" in log.lower():
            print(f"⚠️ Evidence: {log} → Possible data exfiltration via USB")
        elif "unauthorized access" in log.lower():
            print(f"🚨 Evidence: {log} → Unauthorized access detected")
        else:
            print(f"ℹ️ Normal log: {log}")

    print("\n📑 Documentation: All findings recorded for legal review")

if __name__ == "__main__":
    sample_logs = [
        "2026-01-08 Deleted file detected in system",
        "2026-01-08 USB device connected to workstation",
        "2026-01-08 Unauthorized access to HR database",
        "2026-01-08 User login successful"
    ]
    forensic_analysis(sample_logs)
