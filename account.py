class Account:
    def __init__(self, name: str):
        self.__account_name = Account(name)
        self.__account_balance = 0

    def deposit(self, amount: float):
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float):
        if amount <= 0:
            return False
        elif amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_balance


