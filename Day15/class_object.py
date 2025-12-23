class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Giang", 25)
student2 = Student("Lan", 22)

print("Tên:", student1.name, "- Tuổi:", student1.age)
print("Tên:", student2.name, "- Tuổi:", student2.age)
