def container_security_check(container):
    print(f"🐳 Container Security Report for: {container['name']}")
    
    if not container.get("image_scanned"):
        print("🚨 Image not scanned → High risk")
    else:
        print("✅ Image scanned for vulnerabilities")

    if container.get("runs_as_root"):
        print("🚨 Container runs as root → High risk")
    else:
        print("✅ Container runs as non-root user")

    if not container.get("network_policy"):
        print("⚠️ No network policy → Medium risk")
    else:
        print("✅ Network policy enforced")

    if not container.get("logging_enabled"):
        print("⚠️ Logging disabled → Medium risk")
    else:
        print("✅ Logging enabled")

if __name__ == "__main__":
    container_config = {
        "name": "web_app_container",
        "image_scanned": True,
        "runs_as_root": False,
        "network_policy": False,
        "logging_enabled": True
    }
    container_security_check(container_config)
