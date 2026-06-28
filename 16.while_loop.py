# while loop -> execute some code While some condition remain true

# name = input('Enter your name: ')
#
# while name == '':
#     print('You did not enter your name!')
#     name = input('Enter your name: ')
#
# print(f'Your name is {name}')


# age = int(input('Enter your age: '))
#
# while age < 0:
#     print('Your age must be greater than or equal to zero.')
#     age = int(input('Enter your age: '))
#
# price = int(input(f'You are {age} years old '))

# food = input('Enter a food you like (q to quit): ) ')

# while food != 'q':
#     print(f'You like {food}')
#     food = input('Enter a food you like (q to quit): ) ')
#
# print('bye bye')

num = int(input("Enter a number between 1 and 100: "))

while num < 1 or num > 100: # how while works with or in order to while stop all 2 conditions have to false :
    # it some one stad true others fale while loop works again
    print(f'{num} is not a valid number. Enter a number between 1 and 100')
    num = int(input("Enter a number between 1 and 100: "))

print(f'You entered {num}')






