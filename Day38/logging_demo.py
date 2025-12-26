from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(filename="access.log", level=logging.INFO,
                    format="%(asctime)s - %(message)s")

@app.route("/")
def home():
    ip = request.remote_addr
    logging.info(f"Truy cập từ IP: {ip}")
    return "Trang chủ - đã ghi log ✅"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    logging.info(f"Đăng nhập thử với username: {username}")
    return "Đã ghi log đăng nhập!"
    
if __name__ == "__main__":
    app.run(debug=False)
