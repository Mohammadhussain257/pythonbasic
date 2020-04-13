import sys


class Bank:
    bankname = 'My Bank'

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print('After deposit your balance is : ', self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient fund cannot perform operation')
            sys.exit()
        self.balance = self.balance - amount
        print('After withdraw your balance is ', self.balance)


print('Welcome to ', Bank.bankname)
name = input('Enter your name : ')
b = Bank(name)
while True:
    print('d-Deposit\nw-Withdraw\ne-Exit')
    option = input('Choose Your Option : ')
    if option.lower() == 'd':
        amount = float(input('Enter the amount to deposit : '))
        b.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input('Enter the amount to withdraw : '))
        b.withdraw(amount)
    elif option.lower() == 'e':
        print('Thank you visit again')
        sys.exit()
    else:
        print('Please chose a valid option')
