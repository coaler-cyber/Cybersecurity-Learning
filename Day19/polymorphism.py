class Animal:
    def speak(self):
        print("Động vật phát ra âm thanh.")

class Dog(Animal):
    def speak(self):
        print("Chó sủa: Gâu gâu!")

class Cat(Animal):
    def speak(self):
        print("Mèo kêu: Meo meo!")

class Bird(Animal):
    def speak(self):
        print("Chim hót: líu lo líu lo!")

def make_animal_speak(animal):
    animal.speak()

animals = [Dog(), Cat(), Bird()]

for a in animals:
    make_animal_speak(a)
