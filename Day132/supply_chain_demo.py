def check_package(package):
    print(f"📦 Checking package: {package['name']}")
    if package.get("source") != "trusted_repo":
        print("🚨 Suspicious source → Possible supply chain attack")
    if "malicious_code" in package.get("content", "").lower():
        print("🚨 Malicious code detected in package")
    else:
        print("✅ Package seems clean")

if __name__ == "__main__":
    packages = [
        {"name": "requests", "source": "trusted_repo", "content": "standard http library"},
        {"name": "internal_lib", "source": "untrusted_repo", "content": "malicious_code injected"}
    ]
    for pkg in packages:
        check_package(pkg)
