def red_team_attack(passwords, target_pw):
    print("🔴 Red Team: Thử brute force...")
    for pw in passwords:
        if pw == target_pw:
            print(f"✅ Tìm thấy mật khẩu: {pw}")
            return True
        else:
            print(f"❌ Thử mật khẩu thất bại: {pw}")
    return False

def blue_team_defense(attempts, threshold=3):
    print("🔵 Blue Team: Giám sát đăng nhập...")
    if attempts > threshold:
        print("⚠️ Phát hiện brute force! Khóa tài khoản ngay.")
    else:
        print("✅ Không phát hiện bất thường.")

if __name__ == "__main__":
    wordlist = ["123456", "password", "admin123", "letmein"]
    target_pw = "admin123"

    success = red_team_attack(wordlist, target_pw)
    blue_team_defense(len(wordlist))
