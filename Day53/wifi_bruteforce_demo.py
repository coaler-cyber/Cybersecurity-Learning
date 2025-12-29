import hashlib

target_hash = hashlib.sha1("mypassword".encode()).hexdigest()

wordlist = ["123456", "password", "mypassword", "admin123"]

for pw in wordlist:
    h = hashlib.sha1(pw.encode()).hexdigest()
    if h == target_hash:
        print(f"✅ Tìm thấy mật khẩu Wi-Fi: {pw}")
        break
    else:
        print(f"❌ Thử mật khẩu thất bại: {pw}")
