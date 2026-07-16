#Python Slot Machine
import random
from unittest import result


def spin_row():
    symbols = ['@','#','%','&','$']

    return [random.choice(symbols) for _ in range(3)] # result = [random.choice(symbols) for symbol in range(3)] we can write like that but we can't use symbol so use choose 1 option
    #instead we can use list comprehation
    # for symbol in range(3):
    #     result.append(random.choice(symbols))

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == '@' and row[1] =='@' and row[2] =='@':
        return bet *2
    elif row[0] == '#' and row[1] == '#' and row[2] == '#':
        return bet * 3
    elif row[0] == '%' and row[1] == '%' and row[2] == '%':
        return bet * 4
    elif row[0] == '&' and row[1] == '&' and row[2] == '&':
        return bet * 5
    elif row[0] == '$' and row[1] == '$' and row[2] == '$':
        return bet * 10
    else:
        return 0


def main():
    balance = 100

    print("***************************")
    print("Welcome to the SlotMachine")
    print("Symbols: @, #, %, &, $")
    print("***************************")

    while balance > 0:
        print(f'Current Balance: ${balance}')

        bet = input("Enter your bet: ")



        if not bet.isdigit():
            print("Please enter a true value")
            continue

        bet  = int(bet)

        if bet > balance:
            print("Insufficient Balance")
            continue

        if bet <= 0:
            print("Number must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning....\n")
        print_row(row)

        result = get_payout(row, bet)

        if result > 0:
            print(f"You won ${result} amount of money")
        else:
            print("You lost!")

        balance += result

        play_again = input("Do you want to play again? (Y/N): ").upper()

        if balance == 0:
            print("You lost all of money!")
            break
        if not play_again == 'Y':
            break

if __name__ == '__main__':
    main()