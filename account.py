class Account:
    def __init__(self, name:str) -> None:
        """
        Constructor to create initial stae of a person object
        :param name: person's name
        :param balance: person's balance
        """
        self.__account_name = name
        self.__account_balance = 0


    def deposit(self, amount: float) -> bool:
        """
        Compute balance after deposit
        :param amount: deposit amount
        :return: false when transaction is unsuccessful, true when transaction is successful
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True


    def withdraw(self, amount: float) -> bool:
        """
        Compute balance after withdraw
        :param amount: withdraw amount
        :return: false when transaction is unsuccessful, true when transaction is successful
        """
        if amount > self.__account_balance or amount <= 0:
            return False
        else:
            self.__account_balance -= amount
            return True


    def get_balance(self) -> float:
        """
        Method to access a person's balance
        :return: person's balance
        """
        return self.__account_balance


    def get_name(self) -> str:
        """
        Method to access a person's name
        :return: person's name
        """
        return self.__account_name