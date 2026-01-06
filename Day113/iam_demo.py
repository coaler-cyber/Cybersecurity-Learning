def iam_access(user, resource):
    print(f"🔐 IAM Access Check for {user['name']} → {resource}")
    if not user.get("authenticated"):
        print("🚨 Access Denied → User not authenticated")
        return
    if not user.get("mfa_enabled"):
        print("⚠️ Access Denied → MFA required")
        return
    if resource == "admin_panel" and "admin" not in user.get("roles", []):
        print("🚨 Access Denied → Admin role required")
        return
    print("✅ Access Granted → Policy checks passed")

if __name__ == "__main__":
    user1 = {"name": "Alice", "authenticated": True, "mfa_enabled": True, "roles": ["user"]}
    user2 = {"name": "Bob", "authenticated": True, "mfa_enabled": False, "roles": ["admin"]}
    user3 = {"name": "Charlie", "authenticated": True, "mfa_enabled": True, "roles": ["admin"]}

    iam_access(user1, "dashboard")
    iam_access(user2, "admin_panel")
    iam_access(user3, "admin_panel")
