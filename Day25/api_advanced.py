import requests

url_user = "https://randomuser.me/api/"

url_quote = "https://api.quotable.io/random"

def fetch_api(url):
    try:
        response = requests.get(url, timeout=5)  
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.Timeout:
        print("⏰ Lỗi: Quá thời gian chờ API.")
    except requests.exceptions.HTTPError as e:
        print("❌ Lỗi HTTP:", e)
    except requests.exceptions.RequestException as e:
        print("⚠️ Lỗi khác:", e)
    return None

user_data = fetch_api(url_user)
if user_data:
    user = user_data["results"][0]
    print("👤 Người dùng ngẫu nhiên:")
    print("Tên:", user["name"]["first"], user["name"]["last"])
    print("Email:", user["email"])
    print("Quốc gia:", user["location"]["country"])

quote_data = fetch_api(url_quote)
if quote_data:
    print("\n💡 Quote ngẫu nhiên:")
    print(f"\"{quote_data['content']}\" — {quote_data['author']}")
