import requests
import json

url = "https://randomuser.me/api/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  
    user = data["results"][0]
    print("✅ Kết nối API thành công!\n")
    print("👤 Thông tin người dùng ngẫu nhiên:")
    print("Tên:", user["name"]["first"], user["name"]["last"])
    print("Giới tính:", user["gender"])
    print("Email:", user["email"])
    print("Quốc gia:", user["location"]["country"])
else:
    print("❌ Lỗi khi gọi API:", response.status_code)
