#Hangman in Python
import random
# word = ("apple", "orange", "banana", "coconut", "pineapple")

word = ("apple", "orange", "banana", "coconut", "pineapple")

answer = random.choice(word)


def display_hint(hint):
    print("Hint:", " ".join(hint))

hint = ["_"] * len(answer)


# MY version
is_running = True

while is_running:




    print(answer)

    display_hint(hint)  # You need to define this function

    guess = input("Enter your guess: ").lower()

    if guess in answer:
        for i in range(len(answer)):
            if answer[i] == guess:
                hint[i] = guess















































#
# # MY version
# word = ("apple", "orange", "banana", "coconut", "pineapple")
#
# choice = random.choice(word)
# length = len(choice)
# middle_name = length // 2
#
# result = ""
# # print(choice)
#
#
#
# for i in range(length):
#     if i == middle_name:
#         result += choice[middle_name]
#     else:
#         result += "_"
#
# print(result)















































