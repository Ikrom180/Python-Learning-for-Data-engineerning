#Membership operators =  used tom test weather a value or variable is found in a sequence
#                        (string, list, tuple, set or dictionary)
#                        1. in
#                        2. not in


# word = "Apple"
# letter = input("Guess a letter in the secret word: ").capitalize()

# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print("You guessed incorrectly")
#
# print(letter)

# if letter not in word:
#     print(f"There is not a {letter}")
# else:
#     print("You guessed correctly")
#


# students = {"Spongebob", "Patrick", "Sandy"}
#
# student = input("Enter the name of student: ").capitalize()
#
#
# if student in students:
#     print(f'{student} is a valid student')
# else:
#     print(f'{student} is not a valid student')

# grades = { "Sandy": "A",
#            "Ikrom": "B",
#            "Ben": "C",
#            "Izzat": "D"}
#
#
# def grade_finder(name):
#
#     if name in grades:
#         return f"{name} is grade {grades[name]}"
#     else:
#         return f"{name} is not found"
#
# student = input("Enter student name: ").capitalize()
#
# print(grade_finder(student))



email = "Ikrom.Bakhtiyarov@PoytaxtBank.uz"

if '@' in email and '.' in email:
    print("valid email")
else:
    print("invalid email")








