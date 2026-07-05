import random as r

options = ("rock", "paper", "scissors")
player = None
computer = r.choice(options)
is_again = True


while is_again:

    player = None
    while player not in options:
        player = input("Enter the right your choice (rock, paper, or scissors): ").lower()



    if  player == "rock" and computer == "scissors" or \
        player == "paper" and computer == "rock" or \
        player == "scissors" and computer == "paper":
        print("You win!")
    elif player == computer:
        print("Draw!")
    else:
        print("You lose!")



    print(f"player chose {player}")
    print("Computer chose: ", computer)

    if not input("Do you want to play again? (y/n): ").lower() == "y":
        is_again = False
    # or we can write like this
    # is_again = input("Do you want to play again? (y/n): ").lower()
    # if is_again.lower() == "n":
    #     is_again = False

print("Thank you for playing!")