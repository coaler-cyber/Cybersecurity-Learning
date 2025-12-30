import base64

def solve_ctf():
    encoded_flag = base64.b64encode(b"CTF{basic_demo_flag}").decode()
    print("🔒 Encoded flag:", encoded_flag)

    decoded_flag = base64.b64decode(encoded_flag).decode()
    print("✅ Decoded flag:", decoded_flag)

if __name__ == "__main__":
    solve_ctf()
