from bank_account import Bank_Account


class Saving_Account(Bank_Account):

    def __init__(self, name="", balance=0, account_number=0) -> None:
        # constructors for the account
        self.type = "saving"
        self.min_balance = 500
        self.opening_balance = 1000
        # initializing parent class attribute through child class
        Bank_Account.__init__(self, name, balance, account_number)

    def get_min_balance(self):
        return self.min_balance

    def get_opening_balance(self):
        return self.opening_balance


class Current_Account(Bank_Account):

    def __init__(self, name="", balance=0, account_number=0) -> None:
        self.type = "current"
        self.min_balance = 1000
        self.opening_balance = 1000
        Bank_Account.__init__(self, name, balance, account_number)

    def get_min_balance(self):
        return self.min_balance

    def get_opening_balance(self):
        return self.opening_balance


class Salary_Account(Bank_Account):

    def __init__(self, name="", balance=0, account_number=0) -> None:
        self.type = "salary"
        self.min_balance = 100
        self.opening_balance = 500
        Bank_Account.__init__(self, name, balance, account_number)

    def get_min_balance(self):
        return self.min_balance

    def get_opening_balance(self):
        return self.opening_balance
