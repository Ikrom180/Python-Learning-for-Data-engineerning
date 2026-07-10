#Iterables = An object/collection that can return its elements one at a time,
#            allowing it to be iterated over in a loop

# numbers = [1, 2, 3, 4, 5] ->list
# numbers = (1, 2, 3, 4, 5) # -> tuple
# numbers = {1, 2, 3, 4, 5} # -> sets are not reverseable




# for number in reversed(numbers):
#     print(number, end= ' ')


# fruits = {"apple", "orange", "banana", "coconut"}
#
# for fruit in (fruits):
#     print(fruit, end = ' ')


# name = 'Bro Code'
#
# for letter in name:
#     print(letter, end=' ')


my_dictionary = {"A":1, "B":2, "C":3}

for key, value in my_dictionary.items():
    print(f"{key}: {value}")