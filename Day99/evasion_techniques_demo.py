import base64
import time

def obfuscation_demo():
    payload = "print('Hello World')"
    encoded = base64.b64encode(payload.encode()).decode()
    print(f"🔒 Obfuscated payload: {encoded}")
    decoded = base64.b64decode(encoded).decode()
    print(f"🔓 Decoded payload: {decoded}")

def sandbox_evasion_demo():
    print("🧪 Checking environment...")
    start = time.time()
    time.sleep(0.5)
    elapsed = time.time() - start
    if elapsed < 1:
        print("⚠️ Possible sandbox detected → Evading execution")
    else:
        print("✅ Normal environment → Continue execution")

if __name__ == "__main__":
    print("🎭 Advanced Evasion Techniques Demo\n")
    obfuscation_demo()
    print("\n---\n")
    sandbox_evasion_demo()
