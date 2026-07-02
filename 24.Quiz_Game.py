questions = ("what color is son?: ", "Dark room has black color?: ", "What color is bear?: ", "What mission NSLOOKUP can do?: ", "Python is slow?: ")
options = (("A. red","B. green","C. yellow","D. black"),("A. Yes", "B. No", "C.Blue", "D.Red"),("A. Black", "B. yellow", "C. Red", "D.Blue"),
           ("A. It will find Dns Name", "B. Internet finder ","C.Blue ", "D.Red", "C.Yellow"),("A. No", "B. Yes", "C.Blue", "D.Red"))

answers = ("C", "A", "B", "A", "B")
guesses = []
score = 0
question_num = 0

for collection in questions:
    print("-------------------------------")
    print(collection)
    for option in options[question_num]:
        print(option)

    guess = input("enter your guess: ")
    if guess.upper() not in ("A","B","C","D"):
        print("You entered an invalid input")
        break
    else:

        if guess.upper() == answers[question_num]:
            print("Correct!")
            guesses.append(guess.upper())
            score += 1
        else:
            guesses.append(guess.upper())
            print("Incorrect!")

        question_num += 1

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")

print()

print("guesses: ", end="")

for guess in guesses:
    print(guess , end=" ")

print()

print(f"You find {score} guesses")

print()
score = (score / len(questions)) * 100
print(score)