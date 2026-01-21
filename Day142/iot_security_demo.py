def iot_security_check(device):
    print(f"📡 IoT Security Report for: {device['name']}")
    
    if device.get("default_password"):
        print("🚨 Weak authentication → Default password in use")
    else:
        print("✅ Strong authentication configured")
    
    if not device.get("firmware_updated"):
        print("🚨 Insecure firmware → Update required")
    else:
        print("✅ Firmware up-to-date")
    
    if device.get("exposed_to_internet"):
        print("⚠️ Device exposed to internet → Medium risk")
    else:
        print("✅ Device behind firewall")
    
    if not device.get("data_encrypted"):
        print("🚨 Data not encrypted → High risk")
    else:
        print("✅ Data encryption enabled")

if __name__ == "__main__":
    device_example = {
        "name": "SmartCamera",
        "default_password": True,
        "firmware_updated": False,
        "exposed_to_internet": True,
        "data_encrypted": False
    }
    iot_security_check(device_example)
