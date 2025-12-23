my_list = []

while True:
    print("\n--- Menu ---")
    print("1. Thêm phần tử")
    print("2. Xóa phần tử")
    print("3. Hiển thị danh sách")
    print("4. Thoát")

    choice = input("Chọn chức năng (1-4): ")

    if choice == "1":
        item = input("Nhập phần tử muốn thêm: ")
        my_list.append(item)
        print(f"Đã thêm {item} vào danh sách.")
    elif choice == "2":
        item = input("Nhập phần tử muốn xóa: ")
        if item in my_list:
            my_list.remove(item)
            print(f"Đã xóa {item} khỏi danh sách.")
        else:
            print("Phần tử không tồn tại trong danh sách.")
    elif choice == "3":
        print("Danh sách hiện tại:", my_list)
    elif choice == "4":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập 1-4.")
