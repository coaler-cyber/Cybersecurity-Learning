from flask import Flask, request, session, escape
import hashlib, secrets, logging

app = Flask(__name__)
app.secret_key = "supersecret"

logging.basicConfig(filename="final.log", level=logging.INFO,
                    format="%(asctime)s - %(message)s")

users = {"Giang": hashlib.sha256("123456".encode()).hexdigest()}

@app.route("/")
def home():
    return "Trang chủ an toàn ✅"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = escape(request.form.get("username"))
        password = request.form.get("password")
        hashed_pw = hashlib.sha256(password.encode()).hexdigest()

        if username in users and users[username] == hashed_pw:
            
            token = secrets.token_hex(16)
            session["csrf_token"] = token
            logging.info(f"Đăng nhập thành công: {username}")
            return f"✅ Xin chào {username}! CSRF token: {token}"
        else:
            logging.warning(f"Đăng nhập thất bại: {username}")
            return "❌ Sai tài khoản hoặc mật khẩu!"
    return '''
        <form method="POST">
            <input type="text" name="username" placeholder="Tên đăng nhập">
            <input type="password" name="password" placeholder="Mật khẩu">
            <button type="submit">Đăng nhập</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=False)
