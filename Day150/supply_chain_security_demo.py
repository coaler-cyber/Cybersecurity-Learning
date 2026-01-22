def supply_chain_check(dependencies):
    print("🔗 Supply Chain Security Report:")
    for dep in dependencies:
        if dep.get("verified") and not dep.get("malicious"):
            print(f"✅ {dep['name']} is safe")
        elif not dep.get("verified"):
            print(f"⚠️ {dep['name']} not verified → Medium risk")
        elif dep.get("malicious"):
            print(f"🚨 {dep['name']} flagged as malicious → High risk")

if __name__ == "__main__":
    deps = [
        {"name": "requests", "verified": True, "malicious": False},
        {"name": "unknown-lib", "verified": False, "malicious": False},
        {"name": "fake-package", "verified": True, "malicious": True}
    ]
    supply_chain_check(deps)
