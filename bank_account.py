class Bank_Account:

    def __init__(self, name, balance, account_number) -> None:
        self.name = name
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount
        print(
            f"Deposited {amount} to {self.name}'s account. New balance is {self.balance}\n")

    def withdraw(self, amount, minimum_balance):
        if self.balance - amount < minimum_balance:
            print(
                f"Insufficient balance. Minimum balance is {minimum_balance}\n")
        else:
            self.balance -= amount
            print(
                f"Withdrew {amount} from {self.name}'s account. New balance is {self.balance}\n")
