filename = "data.txt"

while True:
    print("\n--- Menu ---")
    print("1. Ghi dữ liệu vào file")
    print("2. Đọc dữ liệu từ file")
    print("3. Thoát")

    choice = input("Chọn chức năng (1-3): ")

    if choice == "1":
        text = input("Nhập dữ liệu muốn ghi: ")
        with open(filename, "a") as f:   # "a" = append, ghi thêm vào cuối file
            f.write(text + "\n")
        print("Đã ghi dữ liệu vào file.")
    elif choice == "2":
        try:
            with open(filename, "r") as f:
                content = f.read()
            print("Nội dung file:\n", content)
        except FileNotFoundError:
            print("File chưa tồn tại. Hãy ghi dữ liệu trước.")
    elif choice == "3":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập 1-3.")
