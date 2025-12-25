import hashlib

users = {"Giang": hashlib.sha256("123456".encode()).hexdigest()}
login_attempts = {}

def login(username, password):
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    
    if login_attempts.get(username, 0) >= 3:
        return "⛔ Tài khoản bị khóa tạm thời do quá nhiều lần thử!"
    
    if username in users and users[username] == hashed_pw:
        login_attempts[username] = 0
        return "✅ Đăng nhập thành công!"
    else:
        login_attempts[username] = login_attempts.get(username, 0) + 1
        return "❌ Sai tài khoản hoặc mật khẩu!"

print(login("Giang", "123456"))
print(login("Giang", "abcdef"))
print(login("Giang", "abcdef"))
print(login("Giang", "abcdef"))
