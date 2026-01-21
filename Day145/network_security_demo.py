def network_security_check(config):
    print("🌐 Network Security Report:")
    
    if not config.get("firewall_enabled"):
        print("🚨 Firewall disabled → High risk")
    else:
        print("✅ Firewall enabled")
    
    if not config.get("ids_ips_enabled"):
        print("⚠️ IDS/IPS not enabled → Medium risk")
    else:
        print("✅ IDS/IPS enabled")
    
    if not config.get("vpn_required"):
        print("🚨 VPN not required → High risk for remote access")
    else:
        print("✅ VPN required for remote access")
    
    if not config.get("network_segmentation"):
        print("⚠️ No network segmentation → Medium risk")
    else:
        print("✅ Network segmentation configured")
    
    if not config.get("secure_protocols"):
        print("🚨 Insecure protocols in use → High risk")
    else:
        print("✅ Secure protocols enforced")

if __name__ == "__main__":
    network_config = {
        "firewall_enabled": True,
        "ids_ips_enabled": False,
        "vpn_required": True,
        "network_segmentation": False,
        "secure_protocols": True
    }
    network_security_check(network_config)
