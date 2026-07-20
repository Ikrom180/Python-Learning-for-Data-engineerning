#Class variables =  shared among all instance of a class ## instance variable inside constructor variable ##
#                   Defined outside the constructors
#                   Allow you share data among all objects created from that class


class Student:

    graduation_year = 2025
    num_of_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_of_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 32)
student4 = Student("Sandy", 34)
student5 = Student("Ikrom", 35)

# print(student1.name)
# print(student1.age)
# print(Student.graduation_year) # graduation year belogs to Student class
# print(Student.num_of_students)


print(f"My graduation year is {Student.graduation_year} and there are {Student.num_of_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
print(student5.name)