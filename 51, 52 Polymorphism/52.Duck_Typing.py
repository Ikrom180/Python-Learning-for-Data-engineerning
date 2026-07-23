# 'Duck Typing' = Another Way to achieve polymorphism based Inheritance
#                 Object must have the minimum necessary attributes/methods
#                 "If it looks like a duck and quaks like a duck, it must be a duck"


class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof !")

class Cat(Animal):
    def speak(self):
        print("Meow !")



class Car:

    alive = False

    def speak(self):
        print("Honk !")

animal = [Dog(), Cat(), Car()]

for animal in animal:
    animal.speak()
    print(animal.alive)