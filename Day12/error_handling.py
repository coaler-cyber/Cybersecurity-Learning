try:
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    result = a / b
    print("Kết quả chia:", result)

except ZeroDivisionError:
    print("❌ Lỗi: Không thể chia cho 0!")

except ValueError:
    print("❌ Lỗi: Vui lòng nhập số nguyên hợp lệ!")

except Exception as e:
    print("❌ Lỗi khác xảy ra:", e)

finally:
    print("👉 Chương trình kết thúc.")
