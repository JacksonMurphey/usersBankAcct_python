
class BankAccount:
    bank_name = "Don't Go Broke Banking"
    all_accounts = []
    


    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        

    def deposit(self, amount):
        self.balance += amount
        print(f"{self} deposited: ${amount}")
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self} withdrew: ${amount}")
        else: 
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5.00
            if self.balance <= 0:
                print("Your account balance is now in the RED(negative). You owe us money, so get out there and make some money")
            else:
                print("Thank you for the $5, please come again.")
        return self

    def display_account_info(self):
        print(f"Your Account Balance is: ${self.balance}")
        return self


    def yield_interest(self):

        if self.balance >= .01:
            
            self.balance = (self.balance * self.int_rate) + self.balance
            

            
        


        else:
            print("No funds available to add interest to!")
        return self 

    @classmethod
    def all_accts(cls):
        print(f"Welcome to " + str(BankAccount.bank_name) +":\n Acount info to follow...")
        # for acct in cls.all_accounts:
        #     print(acct)
            
            # print(f"Account Placeholder name: " + str(acct))
            # print(f"Interest Rate: " + str(cls.int_rate))
            # print(f"Starting Balance: $" + str(cls.balance))
        # print(f"Welcome to " + str(BankAccount.bank_name) +":\n Acount info to follow...")
        # guido, monty, chad in User.all_accounts
        # bank1, bank2 in BankAccount.all_accounts
        # print("bank1", "\nbank2", "\nGuido van Rossum", "\nMonty Python", "\nChad Tadd")
        
        
        
        # BankAccount.all_accounts = bank1.display_account_info(), bank2.display_account_info()
        # print(BankAccount.all_accounts)


    



class User:
    population = 0
    all_accounts = []

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        #two creat two accounts I would create an dictionary above, such 
        #{"saving": BankAccount(int_rate=0.02, balance=100), "checking": BankAccount(int_rate=0.05, balance=0)}
        self.age = age
        User.all_accounts.append(self)
        
        User.population += 1

    def make_deposit(self, amount):
        
        print(f"{self.name} deposited: ${amount}")
        self.account.balance += amount
        return self

    # def test_test(self):
    #     self.account.deposit(100)
    #     print(self.account.balance)


    def make_withdrawal(self, amount):
        #
        if self.account.balance >= amount:
            self.account.balance -= amount   
            print(f"{self.name} withdrew: ${amount}")
        else: 
            print(f"You have Insufficient Funds to make this withdrawal! Thanks to overdraft protection, we prevent you from withdrawing more funds than you have available.")
            print(f"Your current account balance is: ${self.account}")
            
        return self


    def display_user_balance(self):
        print(f"User: {self.name}'s current account balance: ${self.account.balance} ") 
        return self

    def transfer_money(self, other_user, amount):
        if self.account.balance < amount:
            print(f"You have Insufficient Funds to make this Transfer! Thanks to overdraft protection, we prevent you from withdrawing or transfering more funds than you have available.")
            print(f"Your current account balance is: ${self.account}")
        else:
            self.make_withdrawal(amount)
            print("This amount is now being tranfered. Please wait for processing....")
            other_user.make_deposit(amount)
            self.display_user_balance()
            # other_user.display_user_balance()
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

guido = User("Guido van Rossum", "guido@python.com", 40)
monty = User("Monty Python", "monty@python.com", 35)
chad = User("Chad Tadd", "chadtadd@python.com", 18)


    






bank1.deposit(100).deposit(125.25).deposit(35).withdraw(65.15).yield_interest().display_account_info()

bank2.deposit(100).deposit(300).withdraw(100).withdraw(200).withdraw(100).withdraw(.25).yield_interest().display_account_info()
print("_____________________")





monty.make_deposit(100).make_deposit(200).display_user_balance()
monty.make_withdrawal(175).display_user_balance()

monty.transfer_money(guido, 100)
User.user_population()
monty.transfer_money(chad, 10)
print(f"chad has ${chad.account.balance} in his account now")
# monty.test_test()
# monty.account.withdraw(75)
# print(bank1.display_account_info())

print(BankAccount.all_accounts)
