# usersBankAcct_python
Practicing OOP: Creating user class and bank acct class, along with a controller

# Objectives:
Practice creating a class and making instances from it
Practice accessing the methods and attributes of different instances
Practice writing classes
Practice writing classes with associations

- make_withdrawal(self, amount) 
have this method decrease the user's balance by the amount specified

- display_user_balance(self)
have this method print the user's name and account balance to the terminal
eg. "User: Guido van Rossum, Balance: $150

- deposit(self, amount)
increases the account balance by the given amount

- withdraw(self, amount)
decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5

- display_account_info(self)
print to the console: eg. "Balance: $100"

- yield_interest(self)
increases the account balance by the current balance * the interest rate (as long as the balance is positive)


- BONUS: transfer_money(self, other_user, amount)
have this method decrease the user's balance by the amount and add that amount to other other_user's balance
