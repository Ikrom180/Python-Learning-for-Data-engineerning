# Abstract Classes provide partial implementation and can have concrete methods,
# while Interfaces (via ABC with @abstractmethod) define only method signatures with no implementation.
# Python doesn't have a formal interface keyword like Java—we use Abstract Base Classes (ABCs) for both purposes.

from abc import ABC, abstractmethod


class Drawable(ABC):
    """Interface for drawable objects"""

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    # No concrete methods allowed in a pure interface


class Circle(Drawable):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        return "Drawing a circle"

    def get_area(self):
        return 3.14 * self.radius ** 2


class Square(Drawable):
    def __init__(self, side):
        self.side = side

    def draw(self):
        return "Drawing a square"

    def get_area(self):
        return self.side ** 2