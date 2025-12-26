import hashlib
from cryptography.fernet import Fernet

password = "123456"
hashed_pw = hashlib.sha256(password.encode()).hexdigest()

key = Fernet.generate_key()
cipher = Fernet(key)

credit_card = "4111111111111111"
encrypted_card = cipher.encrypt(credit_card.encode())

print("✅ Mật khẩu hash:", hashed_pw)
print("✅ Thẻ tín dụng mã hóa:", encrypted_card)

decrypted_card = cipher.decrypt(encrypted_card).decode()
print("👉 Giải mã thẻ:", decrypted_card)
