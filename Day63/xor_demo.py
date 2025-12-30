def xor_decrypt(ciphertext, key):
    return "".join(chr(ord(c) ^ key) for c in ciphertext)

if __name__ == "__main__":
    cipher = "".join(chr(ord(c) ^ 42) for c in "CTF{crypto_flag}")
    print("🔒 Cipher:", cipher)
    print("✅ Decrypted:", xor_decrypt(cipher, 42))
