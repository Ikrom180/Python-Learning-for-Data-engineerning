#Function = A block of reusable code
        #   place() after the function name to invoke it

# def happy_birthday(name, age):
#     print(f"Happy Birthday to {name} !")
#     print(f"You are {age} old !")
#     print(f"Happy Birthday to {name} !")
#     print()
#
#
# happy_birthday("ikrom", 25)  # inside function values called attribute  and you have to give it them order by order
# happy_birthday("ikrom", 25)
# happy_birthday("ikrom", 25)


#
# def display_invoice(username, amount, due_date):
#     print(f'Hello {username}')
#     print(f'You have of ${amount:.2f} is due {due_date} ')
#
# display_invoice("Jamshid", 25, "01/02")

#return = statement used to end a function
# and send a resutlt back to the caller

# def add(x, y):
#     z = x + y
#     return z
#
# def subtract(x, y):
#     z = x - y
#     return z
#
# def multiply(x, y):
#     z = x * y
#     return z
#
# def divide(x, y):
#     z = x / y
#     return f"{z:.2f}"
#
# print(add(2,3))
# print(subtract(2,3))
# print(multiply(2,3))
# print(divide(2,3))


name = input("Enter your name: ")
last_name = input("Enter your last name: ")

def capitalize_name(name, lastname):
    first = name.title()
    last = lastname.title()
    return first + " " + last


full_name = capitalize_name(name,last_name)
print(full_name)