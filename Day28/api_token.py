import requests

TOKEN = "YOUR_GITHUB_TOKEN"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

url = "https://api.github.com/user"

try:
    response = requests.get(url, headers=headers, timeout=5)
    response.raise_for_status()
    data = response.json()

    print("✅ Kết nối API thành công!\n")
    print("👤 Thông tin GitHub của bạn:")
    print("Login:", data["login"])
    print("ID:", data["id"])
    print("Public repos:", data["public_repos"])

except requests.exceptions.HTTPError as e:
    print("❌ Lỗi HTTP:", e)
except requests.exceptions.RequestException as e:
    print("⚠️ Lỗi khác:", e)
