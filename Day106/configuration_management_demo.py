def check_configuration(configs, baseline):
    print("⚙️ Configuration Management Report:")
    for key, value in configs.items():
        if key in baseline:
            if configs[key] == baseline[key]:
                print(f"✅ {key}: {value} (matches baseline)")
            else:
                print(f"🚨 {key}: {value} (baseline = {baseline[key]}) → Needs remediation")
        else:
            print(f"ℹ️ {key}: {value} (not in baseline)")

if __name__ == "__main__":
    baseline_config = {
        "password_policy": "strong",
        "firewall_enabled": True,
        "ssh_root_login": False
    }

    current_config = {
        "password_policy": "weak",
        "firewall_enabled": True,
        "ssh_root_login": True,
        "logging_enabled": True
    }

    check_configuration(current_config, baseline_config)
