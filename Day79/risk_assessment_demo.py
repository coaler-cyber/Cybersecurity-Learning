def calculate_risk(asset, likelihood, impact):
    score = likelihood * impact
    print(f"🔍 Asset: {asset}")
    print(f"   Likelihood: {likelihood}, Impact: {impact}")
    print(f"   👉 Risk Score: {score}")
    if score >= 15:
        print("   🚨 High Risk – Ưu tiên xử lý ngay!\n")
    elif score >= 8:
        print("   ⚠️ Medium Risk – Cần theo dõi và giảm thiểu.\n")
    else:
        print("   ✅ Low Risk – Rủi ro chấp nhận được.\n")

if __name__ == "__main__":
    assets = [
        ("Web Server", 5, 5),
        ("Database", 4, 3),
        ("Employee Laptop", 2, 2)
    ]
    for asset, likelihood, impact in assets:
        calculate_risk(asset, likelihood, impact)
