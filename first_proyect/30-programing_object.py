class Car:
    def __init__(self, make, model, year):
        self.make = make,
        self.model = model,
        self.year = year
    def display_info(self):
        return f'{self.year} {self.make} {self.model}'

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        return f'{self.year} {self.make} {self.model} with {self.battery_capacity} kWh battery'

car1 = Car("Toyota", "Camriy", 2022)
car2 = Car("Tesla", "Model S", 2023)
electric_car = ElectricCar("Nissan", "Leaf", 2023, 40)

print(electric_car.display_info())

print(car1.display_info())
print(car2.display_info())