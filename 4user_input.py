# input() = A Function that prompts the user to enter data
#           Returns the entered data as a string

# name =input("What is your name?: ")
# age = int(input("What is your age?: "))
#
# age = age + 1 # is wrong so we have to to like this
#
#
# print(f'My name is {name}')
# print(f'My age is {age}')


# Excercise 1 Rectangle  Area Calculator

# w = float(input("Width : "))
# l = float(input("Length : "))
#
# a =  w * l
# print(f'The area is : {a} cm')

#Exercise 2 Shopping Cart Program
item = input("What is your favorite item?: ")
price = float(input("What is your favorite price?: "))
quantity = int(input("What is your favorite quantity?: "))

total = price  * quantity

print(f"You ordered {item}")
print(f'You have bought {quantity} x {item}/s')
print(f'Total: {total}')