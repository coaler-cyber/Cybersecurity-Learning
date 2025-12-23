class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} phát ra âm thanh.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} sủa: Gâu gâu!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} kêu: Meo meo!")

dog = Dog("Chó")
cat = Cat("Mèo")

dog.speak()
cat.speak()
