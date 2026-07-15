#Banking Program

def showBalance(balance):
    return balance

def deposit():
    amount = int(input('Enter your amount: '))


    if amount < 0:
        print('Please enter a positive amount')
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input('Enter your withdraw amount: '))


    if amount < 0:
        print('Please enter a positive amount')
        return 0
    elif amount > balance:
        print('withdraw have to be more than balance')
        return 0
    else:
        return amount



def main():
    balance = 0
    is_running = True

    while is_running:
        print('**************************')
        print("Welcome to Banking Program")
        print('**************************')
        print('1.Show Balance')
        print('2.Deposit')
        print('3.Withdraw')
        print('4.Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            print(f'Your Balance is ${showBalance(balance):.2f}')
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        elif not choice.isdigit():
            print('Please enter a number')
        else:
            print('Please enter a valid choice')

print('Thank you for using Banking Program')

if __name__ == '__main__':
    main()