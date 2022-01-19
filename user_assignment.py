from BankAccount_andUser import BankAccount


class User:
    population = 0
    

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.account_balance = 0
        self.age = age
        self.account = {"saving": BankAccount(0,.01)}
        User.population += 1
        

    def make_deposit(self, amount):
        self.account_balance += amount
        print(f"{self.name} deposited: ${amount}")
        return self

    def make_withdrawal(self, amount):
        
        if self.account_balance >= amount:
            self.account_balance -= amount   
            print(f"{self.name} withdrew: ${amount}")
        else: 
            print(f"You have Insufficient Funds to make this withdrawal! Thanks to overdraft protection, we prevent you from withdrawing more funds than you have available.")
            print(f"Your current account balance is: ${self.account_balance}")
            
        return self


    def display_user_balance(self):
        print(f"User: {self.name}'s current account balance: ${self.account_balance} ") 
        return self

    def transfer_money(self, other_user, amount):
        if self.account_balance < amount:
            print(f"You have Insufficient Funds to make this Transfer! Thanks to overdraft protection, we prevent you from withdrawing or transfering more funds than you have available.")
            print(f"Your current account balance is: ${self.account_balance}")
        else:
            self.make_withdrawal(amount)
            print("This amount is now being tranfered. Please wait for processing....")
            other_user.make_deposit(amount)
            self.display_user_balance()
            other_user.display_user_balance()
            return self

    @classmethod
    def user_population(cls):
        print(f"The bank has {cls.population} accounts in the system")

    
    @staticmethod
    def validate_age(age):
        is_valid = True
        if age < 18:
            is_valid = False
        print(is_valid)
        return is_valid







