def stride_analysis(system_component):
    threats = {
        "Spoofing": f"⚠️ {system_component} có thể bị giả mạo danh tính",
        "Tampering": f"⚠️ {system_component} có thể bị thay đổi dữ liệu",
        "Repudiation": f"⚠️ {system_component} có thể không thể truy vết hành động",
        "Information Disclosure": f"⚠️ {system_component} có thể rò rỉ dữ liệu",
        "Denial of Service": f"⚠️ {system_component} có thể bị tấn công từ chối dịch vụ",
        "Elevation of Privilege": f"⚠️ {system_component} có thể bị leo thang đặc quyền"
    }
    return threats

if __name__ == "__main__":
    component = "Web Login Module"
    analysis = stride_analysis(component)
    print(f"🔍 STRIDE Threat Modeling cho {component}:")
    for category, desc in analysis.items():
        print(f"{category}: {desc}")
