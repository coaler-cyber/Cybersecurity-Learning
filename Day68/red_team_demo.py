import socket

def reconnaissance(target):
    print(f"🔍 Reconnaissance: quét cổng trên {target}")
    for port in [22, 80, 443]:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"✅ Port {port} mở")
            s.close()
        except:
            print(f"❌ Port {port} đóng")

def exploitation():
    print("🚀 Exploitation: mô phỏng khai thác lỗ hổng web (SQLi)")
    query = "SELECT * FROM users WHERE username='admin' AND password='' OR '1'='1'"
    print("🔓 Query injection:", query)
    print("✅ Đăng nhập thành công (mô phỏng)")

if __name__ == "__main__":
    reconnaissance("127.0.0.1")
    exploitation()
