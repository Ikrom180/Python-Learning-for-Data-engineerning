import random
from curses.ascii import isdigit

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)
print(answer)
guesses = 0
is_running = True

print("Welcome to the Number Guessing Game!")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Guess the number: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100")
        elif guess < answer:
            print("Answer is too low")
        elif guess > answer:
            print("Answer is too long")
        else :
            print("The true answer is", answer)
            print("You guessed the number", guess)
            is_running = False


    else:
        print("invalid guess")
        print(f'please select a number between {lowest_num} and {highest_num}')

print(f'You guessed the number', guesses)


