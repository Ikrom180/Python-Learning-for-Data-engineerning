#Abstract class: A class cannot be instantiated on its own; Meant to be subclasses
#                They can contain abstraction methods, which are declared but have no implementations\.
#                Abstract classes benefits:
#                1. Prevents instantiation of the class itself
#                2. Requires children to use inherited abstract methods


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# If @abstract annotation stnad child class have to open like this method
# Otherwise it will give an error

class Car(Vehicle):
    def go(self):
        print('Car is going')

    def stop(self):
        print('Car is stopping')