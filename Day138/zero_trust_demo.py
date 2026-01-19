def zero_trust_access(user):
    print(f"🔐 Zero Trust Access Check for: {user['name']}")
    
    if not user.get("mfa_enabled"):
        print("🚨 Access denied → MFA required")
        return False
    
    if user.get("role") not in ["admin", "developer", "analyst"]:
        print("🚨 Access denied → Unauthorized role")
        return False
    
    if not user.get("device_compliant"):
        print("🚨 Access denied → Device not compliant")
        return False
    
    print("✅ Access granted → User verified")
    return True

if __name__ == "__main__":
    users = [
        {"name": "Alice", "mfa_enabled": True, "role": "admin", "device_compliant": True},
        {"name": "Bob", "mfa_enabled": False, "role": "developer", "device_compliant": True},
        {"name": "Charlie", "mfa_enabled": True, "role": "guest", "device_compliant": True},
    ]
    for u in users:
        zero_trust_access(u)
