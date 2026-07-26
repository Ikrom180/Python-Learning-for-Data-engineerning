# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself


#  Instance methods = Best for operations on instances of the class (objects)
#  Static methods = Best for utility functions that do not need access to class data
#  Class methods = Best for class-level data or require access to the class itself

class Student:

    count = 0
    totalGpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.totalGpa += gpa

    #Instance method
    def get_info(self):
        return f'{self.name}, {self.gpa}'

    @classmethod
    def get_count(cls):
        return f'Total # number of student {Student.count}'

    @classmethod
    def get_avg(cls):
        if Student.count == 0:
            return 0
        else:
            return f'Average Students Gpa is : {Student.totalGpa/Student.count:.2f} '




student1 = Student("John", 3.2)
student2 = Student("John", 2.0)
student3 = Student("John", 4.0)

print(Student.get_count())
print(Student.get_avg())