def caesar_decrypt(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

if __name__ == "__main__":
    cipher = "FUF{edvlf_gpr}"
    for s in range(26):
        print(f"Shift {s}: {caesar_decrypt(cipher, s)}")
