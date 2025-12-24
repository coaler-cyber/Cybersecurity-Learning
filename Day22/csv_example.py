import csv

filename = "Day22/students.csv"

with open(filename, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Score"])
    writer.writerow(["Giang", 25, 90])
    writer.writerow(["Lan", 22, 85])
    writer.writerow(["Minh", 23, 88])

print("✅ Đã ghi dữ liệu vào students.csv")

with open(filename, mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print("\n📊 Nội dung file CSV:")
    for row in reader:
        print(row)
