# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meals = ["chicken", "fish", "turkey"]
#
#
#
# groceries = [fruits, vegetables, meals]
#
# groceries[0][2] = "tasty"
#
# print(groceries[0][1])



# groceries = (["apple", "orange", "banana", "coconut"],
#              ["celery", "carrots", "potatoes"],
#              ["chicken", "fish", "turkey"])
#
#
# for collection in groceries:
#     for food in collection:
#         print(food, end=' ')
#     print()

num_pad = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ('*', 0, '#'))

for collection in num_pad:
    for number in collection:
        print(number, end=' ')
    print()
