import random


class Account(object):
    def __init__(self, user_id, currency="USD"):
        self.user_id = user_id
        self.currency = currency
        self.current_balance = self.__read_balance_from_database()

        print(f"Current balance is : {self.current_balance}.")

    def withdraw(self, amount):
        self.current_balance = self.current_balance - float(amount)
        print(f"New balance after withdraw is: {self.current_balance}.")

    def deposit(self, amount):
        self.current_balance = self.current_balance + float(amount)
        print(f"New balance after deposit is: {self.current_balance}.")

    def generate_statement(self, start_date, end_date):
        pass

    def __read_balance_from_database(self):  # Private method, only called inside the class
        print(f"Getting balance from database for user: {self.user_id}")
        return random.randint(100, 1000)


account_1 = Account(9781)
print(dir(account_1))

print("")
print(f"Current balance: {account_1.current_balance}.")
account_1.deposit(100)
account_1.withdraw(10)

# account_1.__read_balance_from_database  #  object has no attribute [Private method]