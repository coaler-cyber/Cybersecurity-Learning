from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Trang chủ - Debug mode đã tắt ✅"

if __name__ == "__main__":
    app.run(debug=False)
