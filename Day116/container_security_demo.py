def container_security_check(container):
    print(f"📦 Security Check for container: {container['name']}")
    if not container.get("image_scanned"):
        print("🚨 Image not scanned → High risk")
    else:
        print("✅ Image scanned")

    if container.get("runs_as_root"):
        print("🚨 Container runs as root → High risk")
    else:
        print("✅ Container runs as non-root")

    if not container.get("network_isolated"):
        print("⚠️ Network not isolated → Medium risk")
    else:
        print("✅ Network isolated")

    if not container.get("secrets_encrypted"):
        print("🚨 Secrets not encrypted → High risk")
    else:
        print("✅ Secrets encrypted")

if __name__ == "__main__":
    container_config = {
        "name": "web_app",
        "image_scanned": True,
        "runs_as_root": False,
        "network_isolated": False,
        "secrets_encrypted": True
    }
    container_security_check(container_config)
