import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("CREATE TABLE users (id INTEGER, name TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'Giang', '123456')")

user_input = "Giang' OR '1'='1"
query = f"SELECT * FROM users WHERE name = '{user_input}'"

print("❌ Query không an toàn:", query)
cursor.execute(query)
print("👉 Kết quả:", cursor.fetchall())
