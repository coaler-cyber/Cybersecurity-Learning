class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Xin chào, mình là {self.name}, {self.age} tuổi.")

    def is_adult(self):
        return self.age >= 18

student1 = Student("Giang", 25)
student2 = Student("Lan", 16)

student1.introduce()
print("Giang là người lớn?", student1.is_adult())

student2.introduce()
print("Lan là người lớn?", student2.is_adult())
