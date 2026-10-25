from dataclasses import dataclass

@dataclass
class Car:
    brand : str
    model : str
    year  : int


car1 = Car("Audi", "S7", 2025)
car2 = Car("Audi", "S7", 2025)


print(car1)
print(car1 == car2)