import requests

domain = "example.com"
subdomains = ["www", "mail", "ftp", "test", "dev"]

for sub in subdomains:
    url = f"http://{sub}.{domain}"
    try:
        r = requests.get(url, timeout=2)
        print(f"✅ Tìm thấy subdomain: {url} - Status {r.status_code}")
    except requests.ConnectionError:
        print(f"❌ Không tồn tại: {url}")
