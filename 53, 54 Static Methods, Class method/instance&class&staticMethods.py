from typing import Self
from datetime import date

# @classmethod works with class variable and we will use with method(cls)
class Person:

    def __init__(self, name:str, age: int):
        self.name = name
        self.age = age

    def description(self) -> str:
        return f"Name: {self.name}, Age: {self.age} years old"

    @classmethod
    def age_from_year(cls, name:str, birth_year:int) -> Self :
        current_year: int = date.today().year
        age: int = current_year - birth_year
        return cls(name, age)


federico = Person.age_from_year('federico', 1989)
print(federico.description())


# ****************************
# class Person:
#     def __init__(self, name, age):
#         """CONSTRUCTOR - creates and initializes instances"""
#         self.name = name
#         self.age = age
#         print(f"Constructor called: Creating {name}")
#
#     @classmethod
#     def from_birth_year(cls, name, birth_year):
#         """Class method - uses cls to call the constructor"""
#         # cls is the Person class (not a constructor!)
#         # But we USE cls to call the constructor
#         age = 2024 - birth_year
#         return cls(name, age)  # ← cls calls __init__ here
#
#
# # Usage
# person1 = Person("Alice", 30)
# # Output: Constructor called: Creating Alice
# # This directly calls __init__
#
# person2 = Person.from_birth_year("Bob", 1990)
# # Output: Constructor called: Creating Bob
# # Class method uses cls() which calls __init__
# ****************************





# instance & staticmethod

# class Calculator:
#     def __init__(self, version: int):
#         self.version = version
#
#     #instance method when we use self it will inctance method bc it will create when object created
#     def description(self):
#         print(f'Currently running Calculator on version: {self.version}')
#
#
#     #Static methods is the method where we can use anywhere on the class and we do not use self
#     @staticmethod
#     def add_numbers(*numbers: float) -> float:
#         return sum(numbers)
#
#
#
#
# calc1 = Calculator(10)
# calc2 = Calculator(100)
#
# calc1.description()
# calc2.description()
#
# print(Calculator.add_numbers(calc1.version, calc2.version))