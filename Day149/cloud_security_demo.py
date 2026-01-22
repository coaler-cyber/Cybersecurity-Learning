def cloud_security_check(config):
    print("☁️ Cloud Security Report:")
    
    if not config.get("iam_configured"):
        print("🚨 IAM not configured → High risk")
    else:
        print("✅ IAM configured")
    
    if not config.get("data_encrypted"):
        print("🚨 Data not encrypted → High risk")
    else:
        print("✅ Data encrypted")
    
    if not config.get("network_security"):
        print("⚠️ No network security → Medium risk")
    else:
        print("✅ Network security enforced")
    
    if not config.get("compliance"):
        print("⚠️ Compliance not checked → Medium risk")
    else:
        print("✅ Compliance verified")
    
    if not config.get("monitoring_enabled"):
        print("⚠️ Monitoring disabled → Medium risk")
    else:
        print("✅ Monitoring enabled")

if __name__ == "__main__":
    cloud_config = {
        "iam_configured": True,
        "data_encrypted": False,
        "network_security": True,
        "compliance": False,
        "monitoring_enabled": True
    }
    cloud_security_check(cloud_config)
