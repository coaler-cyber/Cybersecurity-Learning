def security_pipeline_check(pipeline):
    print("🔐 DevSecOps Security Pipeline Report:")
    
    if not pipeline.get("sast_enabled"):
        print("🚨 SAST not enabled → High risk")
    else:
        print("✅ SAST enabled (Static Application Security Testing)")
    
    if not pipeline.get("dast_enabled"):
        print("⚠️ DAST not enabled → Medium risk")
    else:
        print("✅ DAST enabled (Dynamic Application Security Testing)")
    
    if not pipeline.get("dependency_scan"):
        print("🚨 Dependency scan missing → High risk")
    else:
        print("✅ Dependency scan enabled")
    
    if not pipeline.get("compliance_check"):
        print("⚠️ Compliance check missing → Medium risk")
    else:
        print("✅ Compliance check passed")

if __name__ == "__main__":
    pipeline_config = {
        "sast_enabled": True,
        "dast_enabled": False,
        "dependency_scan": True,
        "compliance_check": False
    }
    security_pipeline_check(pipeline_config)
