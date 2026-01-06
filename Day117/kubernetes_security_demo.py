def kubernetes_security_check(cluster):
    print("☸️ Kubernetes Security Report:")
    if not cluster.get("rbac_enabled"):
        print("🚨 RBAC not enabled → High risk")
    else:
        print("✅ RBAC enabled")

    if cluster.get("pods_run_as_root"):
        print("🚨 Pods running as root → High risk")
    else:
        print("✅ Pods run as non-root")

    if not cluster.get("network_policies"):
        print("⚠️ Network policies not configured → Medium risk")
    else:
        print("✅ Network policies configured")

    if not cluster.get("secrets_encrypted"):
        print("🚨 Secrets not encrypted → High risk")
    else:
        print("✅ Secrets encrypted")

    if not cluster.get("audit_logging"):
        print("⚠️ Audit logging disabled → Medium risk")
    else:
        print("✅ Audit logging enabled")

if __name__ == "__main__":
    cluster_config = {
        "rbac_enabled": True,
        "pods_run_as_root": False,
        "network_policies": False,
        "secrets_encrypted": True,
        "audit_logging": True
    }
    kubernetes_security_check(cluster_config)
