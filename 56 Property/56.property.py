# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic  when read, or delete attributes
#             Gives you getter , setter, and deleter method


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
