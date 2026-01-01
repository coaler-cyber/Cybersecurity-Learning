def reverse_engineering(binary_data):
    print("🔍 Reverse Engineering Report:")
    for data in binary_data:
        if "password" in data.lower():
            print(f"⚠️ Found hardcoded credential: {data}")
        elif "api_key" in data.lower():
            print(f"🚨 Found API key: {data}")
        elif "http" in data.lower():
            print(f"⚠️ Found suspicious URL: {data}")
        else:
            print(f"ℹ️ String: {data}")

if __name__ == "__main__":
    binary_data = [
        "Password=123456",
        "API_KEY=ABCD-1234-EFGH",
        "http://malicious.example.com",
        "NormalString"
    ]
    reverse_engineering(binary_data)
