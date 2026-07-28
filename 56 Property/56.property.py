# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic  when read, or delete attributes
#             Gives you getter , setter, and deleter method


# if we make before variable '_' -> protected if we do like it '__' -> private and you cannot call outside of the class
# protected variable can be use in child class but private you cannot use it
# if we do not write without @property it will return method memory addr

class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property # -> Getter -> read
    def width(self):
        return f'{self._width:.1f}cm'
    @property # -> Getter -> read
    def height(self):
        return f'{self._height:.1f}cm'

    @width.setter # Setter -> write
    def width(self, new_width):
        if new_width > 0 :
            self._width = new_width
        else:
            print('width must be greater than 0')

    @height.setter # Setter -> write
    def height(self, new_height):
        if new_height > 0 :
            self._height = new_height
        else:
            print('height must be greater than 0')




rectangle = Rectangle(3, 4)

# print(rectangle._width) -> this will be 3
# print(rectangle._height) -> this will be 3

rectangle.width = 5
rectangle.height = 6

print(rectangle.width)
print(rectangle.height)