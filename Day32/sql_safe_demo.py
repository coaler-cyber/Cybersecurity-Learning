import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("CREATE TABLE users (id INTEGER, name TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'Giang', '123456')")

user_input = "Giang' OR '1'='1"

unsafe_query = f"SELECT * FROM users WHERE name = '{user_input}'"
print("❌ Query không an toàn:", unsafe_query)
cursor.execute(unsafe_query)
print("👉 Kết quả:", cursor.fetchall())

safe_query = "SELECT * FROM users WHERE name = ?"
cursor.execute(safe_query, (user_input,))
print("\n✅ Query an toàn:", safe_query)
print("👉 Kết quả:", cursor.fetchall())
