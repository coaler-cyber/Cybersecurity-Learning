import re

def sanitize_input(user_input):
    print(f"🔍 Checking input: {user_input}")
    
    sql_keywords = ["SELECT", "DROP", "INSERT", "DELETE", "--", ";"]
    if any(keyword.lower() in user_input.lower() for keyword in sql_keywords):
        print("🚨 Potential SQL Injection detected")
    else:
        print("✅ No SQL Injection risk")
    
    if re.search(r"<script.*?>", user_input, re.IGNORECASE):
        print("🚨 Potential XSS detected")
    else:
        print("✅ No XSS risk")

if __name__ == "__main__":
    inputs = [
        "SELECT * FROM users WHERE id=1",
        "<script>alert('XSS')</script>",
        "normalUserInput"
    ]
    for inp in inputs:
        sanitize_input(inp)
