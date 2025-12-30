def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print("🔍 Query chạy:", query)

    if password == "' OR '1'='1":
        print("✅ Đăng nhập thành công (SQL Injection)!")
    else:
        print("❌ Sai mật khẩu!")

if __name__ == "__main__":
    login("admin", "wrongpass")

    login("admin", "' OR '1'='1")
