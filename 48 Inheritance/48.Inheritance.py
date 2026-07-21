#Inheritance  = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f'{self.name} eating')

    def sleep(self):
        print(f'{self.name} is a sleep ')

class Dog(Animal):
    def speak(self):
        print(f'{self.name} say woof')

class Cat(Animal):
    def speak(self):
        print(f'{self.name} say meow')

class Mouse(Animal):
    def speak(self):
        print(f'{self.name} say cicici')

dog = Dog('Scooby')
cat = Cat('Garfield')
mouse = Mouse('Mickey')


print(dog.name)
print(dog.is_alive)

cat.speak()
dog.speak()