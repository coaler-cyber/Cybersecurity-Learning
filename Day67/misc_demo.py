import base64
import codecs

def misc_challenge():
    step1 = base64.b64encode(b"CTF{misc_demo_flag}").decode()
    step2 = codecs.encode(step1, "rot_13")

    print("🔒 Encoded (ROT13 + Base64):", step2)

    decoded_rot13 = codecs.decode(step2, "rot_13")
    decoded_flag = base64.b64decode(decoded_rot13).decode()
    print("✅ Decoded flag:", decoded_flag)

if __name__ == "__main__":
    misc_challenge()
