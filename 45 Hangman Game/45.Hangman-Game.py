#Hangman in Python
import random
from words import word
# word = ("apple", "orange", "banana", "coconut", "pineapple")

# word = ("apple", "orange", "banana", "coconut", "pineapple")

# print(hint)

#dictionary of the key:()

hangman_art = {
               0: ("   ",
                   "   ",
                   "   ",),

               1: (" * ",
                   "   ",
                   "   ",),

               2: (" * ",
                   " | ",
                   "   ",),

               3: (" * ",
                   "/| ",
                   "   ",),

               4: (" * ",
                   "/|\\",
                   "   ",),

               5: (" * ",
                   "/|\\",
                   "/  ",),

               6: (" *  ",
                   "/|\\",
                   "/ \\  ",)}


def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)




def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(word)
    hint = ['_'] * len(answer)
    wrong_guesses = 0
    guesses_letter = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        # display_answer(answer)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("invalid option")
            continue



        guesses_letter.add(guess)
        # if guess in guesses_letter:
        #     print("You already guessed this letter")

        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i] and hint[i] == '_':
                    hint[i] = guess
                    break
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) -1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

if __name__ == "__main__":

    main()

# for i in range(len(hangman_art)):
#     for j in hangman_art[i]:
#         print(j)


# for stage, lines in hangman_art.items():
#     print(f"Stage {stage}:")
#     for line in lines:
#         print(line)
#     print()



















# def display_hint(hint):
#     print(f"Hint: {" ".join(hint)} ",)
#
#
# answer = random.choice(word)
# print(answer)
# hint = ['_'] * len(answer)
# guesses = {}
# is_running = True
#
# while is_running:
#
#     display_hint(hint)
#     guess = input("Guess a letter: ")
#
#     if guess in answer:
#         for i in range(len(answer)):
#             if guess == answer[i] and hint[i] == "_":
#                 hint[i] = guess
#                 break


# letter da nechta bir xil harf bor tekshirsinde agar usha xarf 1 marttadan kop qaytariolsa chapdan onga oqisini i imenna usha  xarf uchun logikani yasash kere






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















































