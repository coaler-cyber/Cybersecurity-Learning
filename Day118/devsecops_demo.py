def security_pipeline_check(code_quality, dependencies, container_image):
    print("🔐 DevSecOps Pipeline Security Report:")
    if code_quality < 80:
        print("🚨 Code quality below threshold → Fix required before deployment")
    else:
        print("✅ Code quality acceptable")

    if "vulnerable_lib" in dependencies:
        print("🚨 Vulnerable dependency detected → Remove or patch before deployment")
    else:
        print("✅ Dependencies safe")

    if not container_image.get("scanned"):
        print("🚨 Container image not scanned → High risk")
    else:
        print("✅ Container image scanned")

if __name__ == "__main__":
    code_quality_score = 75
    project_dependencies = ["flask", "requests", "vulnerable_lib"]
    container = {"name": "web_app_image", "scanned": True}

    security_pipeline_check(code_quality_score, project_dependencies, container)
