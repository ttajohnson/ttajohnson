"""
Represent an ATM with a class containing two attributes: a balance and an interest rate.
A newly created account will default to a balance of 0 and an interest rate of 0.1%.
"""

class ATM():
    
    def __init__(self):
        self.balance = 0
        self.interest_rate = 0.001

    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def check_withdrawal(self, amount):
        return amount < self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def calc_interest(self):
        return self.balance * self.interest_rate
    

atm = ATM()

print("Welcome to the ATM")

while True:
    command = input('Enter a command: ')

    match command:
        case 'balance':
            balance = atm.check_balance()
            print(f'Your balance is ${balance}')
        case 'deposit':
            amount = float(input('How much would you like to deposit? '))
            atm.deposit(amount)
            print(f'Deposited ${amount}')
        case 'withdraw':
            amount = float(input('How much would you like to withdraw? '))
            if atm.check_withdrawal(amount):
                atm.withdraw(amount)
                print(f'Withdrew ${amount}')
            else:
                print("Insufficient funds...")
        case 'interest':
            amount = atm.calc_interest()
            atm.deposit(amount)
            print(f'Accumulated ${amount} in interest.')
        case 'help':
            print('Available Commands:\nbalance - get current balance\ndeposit - deposit money\nwithdraw - withdraw money\ninterest - accumulate interest\nexit - exit program')
        case 'exit':
            break
        case _:
            print('Unkown command, try again or enter help.')