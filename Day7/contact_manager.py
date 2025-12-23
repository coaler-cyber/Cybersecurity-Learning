filename = "contacts.txt"

def load_contacts():
    contacts = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                name, phone = line.strip().split(":")
                contacts[name] = phone
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts):
    with open(filename, "w") as f:
        for name, phone in contacts.items():
            f.write(f"{name}:{phone}\n")

contacts = load_contacts()

while True:
    print("\n--- Quản lý danh bạ ---")
    print("1. Thêm liên hệ")
    print("2. Xóa liên hệ")
    print("3. Hiển thị danh bạ")
    print("4. Thoát")

    choice = input("Chọn chức năng (1-4): ")

    if choice == "1":
        name = input("Nhập tên: ")
        phone = input("Nhập số điện thoại: ")
        contacts[name] = phone
        save_contacts(contacts)
        print(f"Đã thêm {name} - {phone}")
    elif choice == "2":
        name = input("Nhập tên muốn xóa: ")
        if name in contacts:
            del contacts[name]
            save_contacts(contacts)
            print(f"Đã xóa {name}")
        else:
            print("Tên không tồn tại trong danh bạ.")
    elif choice == "3":
        print("Danh bạ hiện tại:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif choice == "4":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập 1-4.")
