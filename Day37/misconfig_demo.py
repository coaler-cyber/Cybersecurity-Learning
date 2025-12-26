from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Trang chủ - Debug mode đang bật ❌"

if __name__ == "__main__":

    app.run(debug=True)
