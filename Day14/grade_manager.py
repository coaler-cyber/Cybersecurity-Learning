filename = "grades.txt"

def load_grades():
    grades = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                name, score = line.strip().split(":")
                grades[name] = float(score)
    except FileNotFoundError:
        pass
    return grades

def save_grades(grades):
    with open(filename, "w") as f:
        for name, score in grades.items():
            f.write(f"{name}:{score}\n")

def average_score(grades):
    if len(grades) == 0:
        return 0
    return sum(grades.values()) / len(grades)

grades = load_grades()

while True:
    print("\n--- Quản lý điểm số ---")
    print("1. Thêm học sinh và điểm")
    print("2. Hiển thị danh sách điểm")
    print("3. Tính điểm trung bình")
    print("4. Thoát")

    choice = input("Chọn chức năng (1-4): ")

    if choice == "1":
        name = input("Nhập tên học sinh: ")
        try:
            score = float(input("Nhập điểm: "))
            grades[name] = score
            save_grades(grades)
            print(f"Đã thêm {name} - {score}")
        except ValueError:
            print("❌ Lỗi: Điểm phải là số!")
    elif choice == "2":
        print("Danh sách điểm:")
        for name, score in grades.items():
            print(f"{name}: {score}")
    elif choice == "3":
        print("Điểm trung bình:", average_score(grades))
    elif choice == "4":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập 1-4.")
