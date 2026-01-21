def email_security_check(email):
    print(f"📧 Email Security Report for: {email['subject']}")
    
    if "urgent" in email['subject'].lower() and "click" in email['body'].lower():
        print("🚨 Potential phishing detected")
    else:
        print("✅ No phishing indicators")
    
    if email.get("attachment") and email['attachment'].endswith(".exe"):
        print("🚨 Malicious attachment detected")
    else:
        print("✅ No malicious attachment")
    
    if not email.get("spf_pass") or not email.get("dkim_pass") or not email.get("dmarc_pass"):
        print("⚠️ Email authentication failed → Possible spoofing")
    else:
        print("✅ Email authentication passed")

if __name__ == "__main__":
    email_example = {
        "subject": "Urgent: Click here to verify",
        "body": "Please click the link to verify your account",
        "attachment": "malware.exe",
        "spf_pass": False,
        "dkim_pass": True,
        "dmarc_pass": False
    }
    email_security_check(email_example)
