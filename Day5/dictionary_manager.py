my_dict = {}

while True:
    print("\n--- Menu ---")
    print("1. Thêm cặp key-value")
    print("2. Xóa key")
    print("3. Hiển thị dictionary")
    print("4. Thoát")

    choice = input("Chọn chức năng (1-4): ")

    if choice == "1":
        key = input("Nhập key: ")
        value = input("Nhập value: ")
        my_dict[key] = value
        print(f"Đã thêm {key}: {value}")
    elif choice == "2":
        key = input("Nhập key muốn xóa: ")
        if key in my_dict:
            del my_dict[key]
            print(f"Đã xóa {key}")
        else:
            print("Key không tồn tại.")
    elif choice == "3":
        print("Dictionary hiện tại:", my_dict)
    elif choice == "4":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập 1-4.")
