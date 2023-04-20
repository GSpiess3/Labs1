class account:
    """
    A class designed to get info on a persons account
    """

    def __init__(self, name: str, balance=0) -> None:
        """
        This gets the account info.
        :param name: accounts name notice name must be a string
        :param balance: accounts balance default is set to 0
        """
        self.__name = name
        self.__balance = balance

    def deposite(self, amount):
        '''
        This allows users to deposit money.
        :return: The function will return True or False, True if it wokred and False if it failed
        '''
        if amount <= 0:
            return False
        else:
            self.__balance = amount + self.__balance
            return True

    def withdraw(self, amount):
        '''
        This allows users to withdrawl money
        :return: The function will return True or False, True if it worked and False is it failed
        '''
        if amount <= 0 or amount > self.__balance:
            return False
        else:
            self.__balance = self.__balance - amount
            return True

    def get_name(self) -> str:
        """
        Get the accounts name
        :return: accounts name and name is a string
        """
        return self.__name

    def get_balance(self) -> float:
        """
        Get the account balance
        :return: accounts balance we change whatever the number was to a float
        """
        return self.__balance


