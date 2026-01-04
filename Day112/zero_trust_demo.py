def zero_trust_access(user, device, location):
    print(f"🔐 Zero Trust Access Check for {user}:")
    if not device.get("compliant"):
        print("🚨 Access Denied → Device not compliant")
        return
    if location not in ["office", "vpn"]:
        print("⚠️ Access Denied → Untrusted location")
        return
    if not user.get("mfa_enabled"):
        print("⚠️ Access Denied → MFA required")
        return
    print("✅ Access Granted → Policy checks passed")

if __name__ == "__main__":
    user = {"name": "Alice", "mfa_enabled": True}
    device = {"id": "Laptop01", "compliant": True}
    location = "office"

    zero_trust_access(user, device, location)
