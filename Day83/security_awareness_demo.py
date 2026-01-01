def awareness_quiz():
    questions = [
        {
            "q": "Bạn nhận được email yêu cầu nhập mật khẩu, bạn nên làm gì?",
            "a": "Không click link, báo cho IT"
        },
        {
            "q": "Mật khẩu an toàn nên có đặc điểm gì?",
            "a": "Ít nhất 8 ký tự, gồm chữ hoa, số, ký tự đặc biệt"
        },
        {
            "q": "Nếu ai đó gọi điện xin thông tin cá nhân, bạn nên?",
            "a": "Từ chối và báo cáo cho quản lý"
        }
    ]

    print("📚 Security Awareness Quiz:")
    for q in questions:
        print(f"❓ {q['q']}")
        print(f"✅ Đáp án đúng: {q['a']}\n")

if __name__ == "__main__":
    awareness_quiz()
