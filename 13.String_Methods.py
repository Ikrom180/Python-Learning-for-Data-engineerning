# name = input("Enter your name: ")
# result = len(name) =>  len method shows length string
# result = name.find(" ") => find from indexation index begin from 0 : Bro Code => show result -> 3
# result = name.rfind("o") #=> find values reverse order
# name = name.capitalize() #=>  it will return string and make first letter with upper case
# name = name.upper()
# name = name.lower()
# name = name.title() #=> like capitalize
# name = name.isdigit() # this method find the number only is number comes with string it will return false -> this method return bool
# name.isalpha => isalpha return bool it only contain string
# result = name.count('ikrom') #=> it will count what ever me need
# replaced = name.replace('i','a') #=> replace method return str .
# print(help(int)) => 'help' it will help to identify which attribute to do what


# print(name)
# print(result)
# print(replaced)


# validate user input excersise

# 1.username is no more than 12 characters
# 2.username must not contain spaces
# 3.username must not contain digits

username = input("Enter your username: ")

if len(username) > 12 :
    print("Username no more than 12 characters")
elif not username.find(" ") == -1:
    print("Your name contains spaces.")
if username.isalpha() == False:
    print("Your have to write only alphanumeric characters.")
else:
    print(f"Welcome {username} ")




















