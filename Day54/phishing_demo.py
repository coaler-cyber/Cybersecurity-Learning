def fake_email():
    subject = "🔒 Security Alert: Verify Your Account"
    body = """
    Dear User,

    We detected unusual login attempts on your account.
    Please verify your credentials immediately at:
    http://fake-login.example.com

    Thank you,
    Security Team
    """
    print("📧 Fake Email Sent")
    print("Subject:", subject)
    print("Body:\n", body)

if __name__ == "__main__":
    fake_email()
