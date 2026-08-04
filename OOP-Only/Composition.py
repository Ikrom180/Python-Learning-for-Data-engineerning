# Aggregation = A relationship where one object contains references to other Independent objects
#               "has-a" relationship

# Composition = The composed object directly owns its components, which cannot exist independently
#               "owns-a" relationship




class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:

    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheel_size = [Wheel(wheel_size) for wheel in range(4)]


    def display(self):
        return f'{self.make} {self.model} {self.engine.horse_power}hp {self.wheel_size[0].size}in'


car = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)

print(car.display())