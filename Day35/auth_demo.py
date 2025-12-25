users = {"Giang": "123456"}

def login(username, password):
    if username in users and users[username] == password:
        return "✅ Đăng nhập thành công!"
    return "❌ Sai tài khoản hoặc mật khẩu!"

print(login("Giang", "123456"))
print(login("Giang", "abcdef"))
