from flask import Flask, request, session
import secrets

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/form")
def form():
    token = secrets.token_hex(16)
    session["csrf_token"] = token
    return f'''
        <form method="POST" action="/transfer">
            <input type="hidden" name="csrf_token" value="{token}">
            <input type="text" name="amount" placeholder="Số tiền">
            <button type="submit">Chuyển tiền</button>
        </form>
    '''

@app.route("/transfer", methods=["POST"])
def transfer():
    token = request.form.get("csrf_token")
    if not token or token != session.get("csrf_token"):
        return "❌ CSRF token không hợp lệ!"
    amount = request.form.get("amount")
    return f"✅ Đã chuyển {amount} VNĐ an toàn!"

if __name__ == "__main__":
    app.run(debug=True)
