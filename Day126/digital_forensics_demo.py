def forensic_analysis(logs):
    print("🔍 Digital Forensics Report:")
    for log in logs:
        if "deleted file" in log.lower():
            print(f"🚨 Evidence: {log} → Possible data tampering")
        elif "usb device" in log.lower():
            print(f"⚠️ Evidence: {log} → Possible unauthorized data transfer")
        elif "admin login" in log.lower():
            print(f"ℹ️ Evidence: {log} → Privileged access detected")
        else:
            print(f"ℹ️ Normal log: {log}")

if __name__ == "__main__":
    sample_logs = [
        "Deleted file: confidential.docx",
        "USB device connected to workstation",
        "Admin login from 203.0.113.5",
        "System update completed"
    ]
    forensic_analysis(sample_logs)
