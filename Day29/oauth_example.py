from requests_oauthlib import OAuth2Session

client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
authorization_base_url = "https://github.com/login/oauth/authorize"
token_url = "https://github.com/login/oauth/access_token"

github = OAuth2Session(client_id)
authorization_url, state = github.authorization_url(authorization_base_url)
print("👉 Truy cập link sau để đăng nhập GitHub:")
print(authorization_url)

redirect_response = input("\nDán toàn bộ URL sau khi đăng nhập: ")

token = github.fetch_token(token_url,
                           client_secret=client_secret,
                           authorization_response=redirect_response)

print("\n✅ Access Token nhận được:")
print(token)

r = github.get("https://api.github.com/user")
print("\n👤 Thông tin GitHub của bạn:")
print(r.json())
