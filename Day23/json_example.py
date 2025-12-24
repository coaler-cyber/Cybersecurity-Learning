import json

filename = "Day23/students.json"

students = {
    "students": [
        {"name": "Giang", "age": 25, "score": 90},
        {"name": "Lan", "age": 22, "score": 85},
        {"name": "Minh", "age": 23, "score": 88}
    ]
}

with open(filename, "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=4)

print("✅ Đã ghi dữ liệu vào students.json")

with open(filename, "r", encoding="utf-8") as f:
    data = json.load(f)
    print("\n📊 Nội dung file JSON:")
    for s in data["students"]:
        print(f"{s['name']} - {s['age']} tuổi - điểm {s['score']}")
