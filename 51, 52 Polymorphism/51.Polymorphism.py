#Polymorphism = Greek word that means to "have many forms or faces"
#               Poly = Many
#               Morphe = Form

#               Two Ways to achieve Polymorphism
#               1.  Inheritance = An object could be treated of the same type as a parent class
#               2. 'Duck Typing' = Object must have necessary attributes/methods


# Each classes have 2 forms which 1 form is their own class second one is Shape parent class form
# for example Circle => Shape # But not Squeare not= circle like this ...

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):  #-> if we do not extend from shape it won't iterate in same shapes group
#Pizza considered -> Circle ->Circele considered Shape -> so pizza can be **Pizza->Circle->Shape**
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping



# circle = Circle()

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza('Peperoni', 15)]

for shape in shapes:
    print(f'{shape.area()} cm2')
