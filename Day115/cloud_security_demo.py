def cloud_security_check(config):
    print("☁️ Cloud Security Report:")
    if not config.get("iam_mfa_enabled"):
        print("🚨 IAM: MFA not enabled → High risk")
    else:
        print("✅ IAM: MFA enabled")

    if not config.get("data_encryption"):
        print("🚨 Data: Encryption not enabled → High risk")
    else:
        print("✅ Data: Encryption enabled")

    if not config.get("network_firewall"):
        print("🚨 Network: Firewall not configured → High risk")
    else:
        print("✅ Network: Firewall configured")

    if not config.get("monitoring_enabled"):
        print("⚠️ Monitoring: Disabled → Medium risk")
    else:
        print("✅ Monitoring: Enabled")

if __name__ == "__main__":
    cloud_config = {
        "iam_mfa_enabled": True,
        "data_encryption": False,
        "network_firewall": True,
        "monitoring_enabled": False
    }
    cloud_security_check(cloud_config)
