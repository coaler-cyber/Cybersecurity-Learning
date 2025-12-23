class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022)

car1.info()
car2.info()
