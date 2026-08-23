class ATM:

    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
Choose option from below:
1. Create pin
2. Change pin
3. Check Balance
4. Withdraw
5. Exit
""")
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input('Create a pin: ')
        self.pin = user_pin
        user_balance = int(input('Enter your balance:'))
        self.balance = user_balance
        print('Balance is:',self.balance)
        self.menu()

    def change_pin(self):
        old_pin = input('Enter old pin: ')
        if old_pin == self.pin:
            new_pin = input('Enter new pin: ')
            self.pin = new_pin
        else:
            print('Invalid old pin: ')
        self.menu()

    def check_balance(self):
        user_pin = input('Enter pin: ')
        if user_pin == self.pin:
            print('Balance is: ',self.balance)
        else:
            print('Invaild pin: ')
        self.menu()

    def withdraw(self):
        user_pin = input('Enter pin :')
        if user_pin == self.pin:
            amount = int(input('Enter amount :'))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print('Balance is: ',self.balance)
            else:
                print('Infulance balance: ')
        else:
            print('Invalid pin :')
        self.menu()


obj = ATM()
print(obj)