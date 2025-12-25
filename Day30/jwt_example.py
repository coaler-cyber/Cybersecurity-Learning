import time
import jwt  

SECRET_KEY = "mysecret"

def create_access_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": time.time() + 10  
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def create_refresh_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": time.time() + 86400  
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

user_id = 123
access_token = create_access_token(user_id)
refresh_token = create_refresh_token(user_id)

print("✅ Access Token:", access_token)
print("🔄 Refresh Token:", refresh_token)

try:
    decoded = jwt.decode(access_token, SECRET_KEY, algorithms=["HS256"])
    print("\n👤 Token hợp lệ, user_id:", decoded["user_id"])
except jwt.ExpiredSignatureError:
    print("\n❌ Access Token hết hạn, dùng Refresh Token để lấy mới!")
