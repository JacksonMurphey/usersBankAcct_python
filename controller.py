from user_assignment import User
from BankAccount_andUser import BankAccount

guido = User("Guido van Rossum", "guido@python.com", 40)
monty = User("Monty Python", "monty@python.com", 35)
chad = User("Chad Tadd", "chadtadd@python.com", 18)

#NOTE: Chaining Method: add (return self) to methods 
guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance().transfer_money(monty, 100)

monty.transfer_money(guido, 150)

#TODO: calling a class method. 
User.user_population()


bank1 = BankAccount() 
bank2 = BankAccount() #Since I set default values for int_rate and balance in the instance. I wouldnt need to pass them through as arguments here, unless their values were different from the default. 


#NOTE: User.Practice assignment calls below. 
# guido.make_deposit(100)
# guido.make_deposit(200)
# guido.make_deposit(426)
# guido.make_withdrawal(110)
# guido.display_user_balance()

# monty.make_deposit(500)
# monty.make_deposit(250.50)
# monty.make_withdrawal(50.75)
# monty.display_user_balance()

# chad.make_deposit(500)
# chad.make_withdrawal(300)
# chad.make_withdrawal(200)
# chad.make_withdrawal(5)
# chad.display_user_balance()

# monty.display_user_balance()
# monty.transfer_money(guido, 100)