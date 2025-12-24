import requests

API_KEY = "YOUR_API_KEY"
city = "Hanoi"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()

    print("✅ Kết nối API thành công!\n")
    print(f"🌤 Thời tiết tại {city}:")
    print("Nhiệt độ:", data["main"]["temp"], "°C")
    print("Độ ẩm:", data["main"]["humidity"], "%")
    print("Mô tả:", data["weather"][0]["description"])

except requests.exceptions.HTTPError as e:
    print("❌ Lỗi HTTP:", e)
except requests.exceptions.RequestException as e:
    print("⚠️ Lỗi khác:", e)
