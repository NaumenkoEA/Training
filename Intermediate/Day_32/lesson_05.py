class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f"{self.name}, {self.age} years old"



class Car :
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand}, {self.model} , ({self.year})"
    
    def __repr__(self):
        return f"Car('{self.brand}', '{self.model}', {self.year})"

car1 = Car("Audi", "S7", 2025)
car2 = Car("BMW", "M5", 2024)
cars = [car1, car2]

print(cars)