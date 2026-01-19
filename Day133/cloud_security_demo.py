def cloud_security_check(config):
    print("☁️ Cloud Security Report:")
    if not config.get("iam_least_privilege"):
        print("🚨 IAM misconfigured → High risk")
    else:
        print("✅ IAM least privilege enforced")

    if not config.get("data_encrypted"):
        print("🚨 Data not encrypted → High risk")
    else:
        print("✅ Data encryption enabled")

    if not config.get("network_segmentation"):
        print("⚠️ No network segmentation → Medium risk")
    else:
        print("✅ Network segmentation configured")

    if not config.get("logging_enabled"):
        print("⚠️ Logging disabled → Medium risk")
    else:
        print("✅ Logging enabled")

    if not config.get("compliance_certified"):
        print("⚠️ Compliance not certified → Medium risk")
    else:
        print("✅ Compliance certified")

if __name__ == "__main__":
    cloud_config = {
        "iam_least_privilege": True,
        "data_encrypted": True,
        "network_segmentation": False,
        "logging_enabled": True,
        "compliance_certified": False
    }
    cloud_security_check(cloud_config)
