import dis

def suspicious_function(x, y):
    result = (x * y) ^ 0xDEADBEEF
    return result

def reverse_engineering(func):
    print(f"🔍 Reverse Engineering {func.__name__}")
    print("➡️ Disassembly:")
    dis.dis(func)

if __name__ == "__main__":
    print("🧩 Reverse Engineering Demo")
    reverse_engineering(suspicious_function)
    print(f"Result of suspicious_function(5, 10): {suspicious_function(5, 10)}")
