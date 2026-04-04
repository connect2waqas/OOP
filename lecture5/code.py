# understanding class in oop
l =  [1,2,3,4,5] 
"""Class: 
here l is the object for the built-in list which will followed the rules that are built-in
l.upper()
this will give us attributes error becuase of the there is no method of list with name upper()
So class is set of Rule for following of the objects.
So class is basically comibination of the data/ properties/ attributes and functions but in oop we are called it methods okay."""
"""object:
object is the instance of the class. 
object are the actuall thing which follows the class rules.

Creating a class with its objects:
string = str()
l = list()
tup_1 , tup_2  = tuple(1,), tuple(2,3,4,)

"""

class Atm:
    def __init__(self):
        self.pin = '1234'
        self.balance = 0
        self.limit = 4000
        self.menu()

    def menu(self):
        user_input = input("""How can i help you:
                           1. Create pin
                           2. change pin
                           3. check balance
                           4. withdraw
                           5. press any button to exit
                           """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.withdraw()
        else:
            exit()
    def create_pin(self):
        user_pin = input("Enter Your pin: ")
        self.pin = user_pin
        print("Your pin is set now")
        self.menu()
    def change_pin(self):
        user_pin = input("Enter Your old pin: ")
        if user_pin == self.pin:
            new_pin = input("Enter Your new pin: ")
            self.pin = new_pin
            print("Pin changed successfully...")
            self.menu()
        else:
            print("Wrong pin")
            self.menu()
    def check_balance(self):
        user_pin = input("Enter Your pin")
        if user_pin == self.pin:
            print(f"Balance: {self.balance}")
            self.menu()
        else:
            print(f"Wrong pin: {user_pin}")
            self.menu()
    def withdraw(self):
        amount = int(input("Enter amount: "))
        user_pin = input("Enter Your Pin: ")
        if user_pin == self.pin and (amount > 0 and amount < self.limit):
            self.balance -= amount
            print(f"{amount} withdraw successfully")
            self.menu()
        else:
            print("wrong pin or amount or insufficient balance")
            self.menu()

obj_1 = Atm()
