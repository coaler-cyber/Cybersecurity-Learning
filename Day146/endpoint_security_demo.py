def endpoint_security_check(endpoint):
    print(f"💻 Endpoint Security Report for: {endpoint['name']}")
    
    if not endpoint.get("antivirus_enabled"):
        print("🚨 Antivirus/EDR disabled → High risk")
    else:
        print("✅ Antivirus/EDR enabled")
    
    if not endpoint.get("patched"):
        print("🚨 System not patched → Vulnerable to exploits")
    else:
        print("✅ System patched")
    
    if endpoint.get("usb_access"):
        print("⚠️ USB access allowed → Medium risk")
    else:
        print("✅ USB access restricted")
    
    if not endpoint.get("app_whitelisting"):
        print("⚠️ No application whitelisting → Medium risk")
    else:
        print("✅ Application whitelisting enforced")
    
    if not endpoint.get("behavior_monitoring"):
        print("⚠️ No behavioral monitoring → Medium risk")
    else:
        print("✅ Behavioral monitoring active")

if __name__ == "__main__":
    endpoint_example = {
        "name": "Workstation-01",
        "antivirus_enabled": True,
        "patched": False,
        "usb_access": True,
        "app_whitelisting": False,
        "behavior_monitoring": True
    }
    endpoint_security_check(endpoint_example)
