def pam_access(user, resource):
    print(f"🔐 PAM Access Check for {user['name']} → {resource}")
    if not user.get("authenticated"):
        print("🚨 Access Denied → User not authenticated")
        return
    if not user.get("just_in_time"):
        print("⚠️ Access Denied → Privileged access requires JIT approval")
        return
    if resource == "critical_server" and "admin" not in user.get("roles", []):
        print("🚨 Access Denied → Admin role required")
        return
    print("✅ Access Granted → Privileged session started (audited)")

if __name__ == "__main__":
    user1 = {"name": "Alice", "authenticated": True, "just_in_time": False, "roles": ["admin"]}
    user2 = {"name": "Bob", "authenticated": True, "just_in_time": True, "roles": ["user"]}
    user3 = {"name": "Charlie", "authenticated": True, "just_in_time": True, "roles": ["admin"]}

    pam_access(user1, "critical_server")
    pam_access(user2, "critical_server")
    pam_access(user3, "critical_server")
