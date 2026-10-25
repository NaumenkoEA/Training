class Car :
    def __init__(self,brand ,model ,year,mileage):
        self.brand =brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def show_info(self):
        print(self.brand,self.model,self.year ,self.mileage,self.age_car(),self.needs_service())

    def age_car(self):
        return 2026 - self.year

    def drive(self,km):
        if(km > 0):
            self.mileage +=km
        else:
            print("The number of kilometers must be greater than 0")

    def needs_service(self):
        return self.mileage >= 10000

class ElectricCar(Car):
    def __init__(self, brand, model, year, mileage, battery):
        super().__init__(brand, model, year, mileage)
        self.battery = battery

    def show_info(self):
        super().show_info()
        print("Battery:", self.battery)

class SportCar(Car):
    def __init__(self, brand, model, year, mileage,max_speed):
        super().__init__(brand, model, year, mileage)
        self.max_speed = max_speed

    def show_info(self):
        super().show_info()
        print("Max speed: ",self.max_speed)

car1 = Car("audi", "s7", 2025, 10000)
car2 = Car("geely", "monjaro", 2026, 1000)
car = ElectricCar("tesla" , "model 3" , 2025 , 5000 ,80)
sport_car = SportCar("bmw", "m4", 2024, 3000, 290)


car1.show_info()
car2.show_info()
car.show_info()
sport_car.show_info()