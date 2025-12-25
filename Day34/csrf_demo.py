from flask import Flask, request

app = Flask(__name__)

@app.route("/transfer", methods=["POST"])
def transfer():
    amount = request.form.get("amount")
    return f"💸 Đã chuyển {amount} VNĐ!"

if __name__ == "__main__":
    app.run(debug=True)
