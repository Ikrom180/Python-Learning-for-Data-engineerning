#list comprehession = A concise way to create lists in Python
#                     Compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]

# doubles = []

# for x in range (1,11):
#     doubles.append(x * 2)
#
# print(doubles, end=' ')



# [expression for value in iterable if condition]
# we make it easyer
# doubles = [x * 2 for x in range(1,11)]
# triple = [x * 3 for x in range(1,11)]
# squares = [z * z for z in range(1,11)]
# print(doubles)
# print(triple)
# print(squares)


# fruits = ['apple', 'orange', 'banana', 'coconut']
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

# Same result return
# fruits = ['apple', 'orange', 'banana', 'coconut']
# fruits = [fruit.upper() for fruit in ['apple', 'orange', 'banana', 'coconut']]
# print(fruits)


# get the only first character
# fruits = ['apple', 'orange', 'banana', 'coconut']
# fruits_chars = [fruit[0] for fruit in fruits]
# print(fruits)


# numbers = [1, -2, 3, -4, 5, -6, 8, -7]
# positive_numbers = [num for num in numbers if num > 0]
# negative_numbers = [num for num in numbers if num < 0]
# even_num = [num for num in numbers if num % 2 == 0]
# odd_num = [num for num in numbers if num % 2 == 1]
# print(positive_numbers)
# print(negative_numbers)
# print(even_num)
# print(odd_num)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

for grade in sorted(passing_grades):
    print(grade, end=' ')
















