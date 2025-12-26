import hashlib

passwords = ["123456", "password", "admin123"]
hashes = []

for pw in passwords:
    h = hashlib.md5(pw.encode()).hexdigest()
    hashes.append(h)
    print(f"🔑 Mật khẩu: {pw} -> Hash: {h}")

with open("hash.txt", "w") as f:
    for h in hashes:
        f.write(h + "\n")
