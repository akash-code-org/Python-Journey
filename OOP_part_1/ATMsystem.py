class ATM:
    def __init__(self):
        self.pin = ''
        self.balance = 0
    def menu(self):
        user_input = input("""
Choose option from below:
1. Create pin
2. Change pic
3. Check balance
4. withdraw
5. Exit
""")
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.chack_balance()
        elif user_input == '4':
            self.withdrawl()
    def create_pin(self):
        user_pin = input('Enter pin: ')
        self.pin = user_pin
        user_blance = input('Enter your balance: ')
        self.balance = user_blance
        print('Your bin successfuly created: ')
    def change_pin(self):
        user_old = input('Enter your pin: ')
        if user_old == self.pin:
            new_pin = ('Enter new pin: ')
            self.pin = new_pin
            print('Your pin successufly changed: ')
        else:
            print('Your old pin is invalid: ')
    def check_balance(self):
        user_pin = input('Enter your pin: ')
        if user_pin == self.pin:
            print('Your balance is :',self.balance)
        else:
            print('Invalid pin: ')
    def withdrawl(self):
        user_pin = input('Enter your pin: ')
        if user_pin == self.pin:
            amount = int(input('Enter withdrawl amount: '))
            if amount <= self.balance:
                self.balance = self.balance - amount
            else:
                print('You not have balance: ')
        else:
            print('')
        self.menu



obj = ATM()