def data_security_check(data):
    print(f"🗄️ Data Security Report for: {data['name']}")
    
    if not data.get("classified"):
        print("🚨 Data not classified → High risk")
    else:
        print("✅ Data classified")
    
    if not data.get("encrypted"):
        print("🚨 Data not encrypted → High risk")
    else:
        print("✅ Data encrypted")
    
    if not data.get("access_control"):
        print("🚨 No access control → High risk")
    else:
        print("✅ Access control enforced")
    
    if not data.get("dlp_enabled"):
        print("⚠️ DLP not enabled → Medium risk")
    else:
        print("✅ DLP enabled")
    
    if not data.get("backup_configured"):
        print("⚠️ No backup configured → Medium risk")
    else:
        print("✅ Backup configured")

if __name__ == "__main__":
    data_example = {
        "name": "CustomerDatabase",
        "classified": True,
        "encrypted": False,
        "access_control": True,
        "dlp_enabled": False,
        "backup_configured": True
    }
    data_security_check(data_example)
