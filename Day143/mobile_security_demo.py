def mobile_app_security_check(app):
    print(f"📱 Mobile Security Report for: {app['name']}")
    
    if not app.get("data_encrypted"):
        print("🚨 Insecure data storage → High risk")
    else:
        print("✅ Data encrypted")
    
    if not app.get("mfa_enabled"):
        print("🚨 Weak authentication → MFA missing")
    else:
        print("✅ MFA enabled")
    
    if not app.get("https_api"):
        print("🚨 Insecure communication → API not using HTTPS")
    else:
        print("✅ Secure API communication")
    
    if app.get("reverse_engineering_protection"):
        print("✅ Reverse engineering protection enabled")
    else:
        print("⚠️ No reverse engineering protection → Medium risk")

if __name__ == "__main__":
    app_example = {
        "name": "BankingApp",
        "data_encrypted": False,
        "mfa_enabled": True,
        "https_api": True,
        "reverse_engineering_protection": False
    }
    mobile_app_security_check(app_example)
