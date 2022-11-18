class Account:
    def __init__(self, name: str) -> None:
        """
        Initialize the variable for account name and account balance.
        :param name: Account name is equal to what is put in for account. Account balance is set to 0.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        This function increases by the amount given.
        :param amount: Amount added to the account.
        :return: True if the amount is not negative or zero then will be false.
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        This function decreases the amount given.
        :param amount: Amount subtracted to the account.
        :return: True if amount is not negative, zero or more than the account balance. Then will return false.
        """
        if amount <= 0:
            return False
        elif amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Get the account balance.
        :return: Account balance.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Get the account name.
        :return: Account name.
        """
        return self.__account_name


