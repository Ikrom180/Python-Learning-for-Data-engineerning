#Static Methods = A method that belong to a class rather than any object from that class (instance)
#                 Usually used for general utility functions

# Instance method = Best for operations in instance of the class (object)
# Static methods = Best for utility functions that do not accsess to class data

# First you have to create object and then you can access instance method this is instance method
# Static method you can call it without create object

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f'{self.name} = {self.position}'

    @staticmethod #Without decorator we could not call like this emp1.is_calid.... 
    def is_valid_position(position):

        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_position


print(Employee.is_valid_position("Manager"))

emp1 = Employee("Eugine", "Manager")
emp2 = Employee("Squidward", "Manager")
emp3 = Employee("Spongebob", "Manager")

print(emp1.is_valid_position(emp1.position))
