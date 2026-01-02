def patch_management(patches):
    print("🔧 Patch Management Report:")
    for p in patches:
        if p["critical"]:
            print(f"🚨 Critical Patch: {p['name']} → Deploy immediately")
        elif p["risk"] >= 7:
            print(f"⚠️ High Risk Patch: {p['name']} → Test & deploy within 7 days")
        elif p["risk"] >= 4:
            print(f"ℹ️ Medium Risk Patch: {p['name']} → Deploy within 30 days")
        else:
            print(f"✅ Low Risk Patch: {p['name']} → Schedule for next update cycle")

if __name__ == "__main__":
    patches = [
        {"name": "Windows Security Update KB500123", "critical": True, "risk": 9.8},
        {"name": "OpenSSL Patch 1.1.1k", "critical": False, "risk": 7.5},
        {"name": "Apache Config Update", "critical": False, "risk": 5.0},
        {"name": "Minor UI Fix", "critical": False, "risk": 2.0}
    ]
    patch_management(patches)
