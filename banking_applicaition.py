from account_types import Saving_Account, Current_Account, Salary_Account


class Banking_Application:

    def __init__(self) -> None:
        self.accounts = []
        self.total_accounts_created = 0

    def create_new_account(self, name, type, balance):
        if type == "saving":
            account = Saving_Account(
                name, balance, self.total_accounts_created+1)
        elif type == "current":
            account = Current_Account(
                name, balance, self.total_accounts_created+1)
        else:
            account = Salary_Account(
                name, balance, self.total_accounts_created+1)
        self.accounts.append(account)
        self.total_accounts_created += 1
        return self.total_accounts_created

    def get_constrains_and_type(self, choice):
        if choice == "1":
            return ("saving", Saving_Account().min_balance,
                    Saving_Account().opening_balance)
        elif choice == "2":
            return ("current", Current_Account().min_balance,
                    Current_Account().opening_balance)
        else:
            return ("salary", Salary_Account().min_balance,
                    Salary_Account().opening_balance)

    def display(self, account_number, name, account_type, balance):
        print(
            f"Account Number: {account_number} | Name: {name} | Account Type: {account_type} | Balance: {balance}\n"
        )

    def display_accounts(self):
        if len(self.accounts) == 0:
            print("No accounts to display.\n")
            return
        for account in self.accounts:
            self.display(account.account_number, account.name,
                         account.type, account.balance)
        print("")

    def update_account(self, account_number, new_name):
        for account in self.accounts:
            if account.account_number == account_number:
                account.name = new_name
                print("Account updated successfully.\n")
                return
        print("Account not found.\n")

    def delete_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print("Account deleted successfully.\n")
                return
        print("Account not found.\n")

    def deposit_amount(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                account.deposit(amount)
                return
        print("Account not found.\n")

    def withdraw_amount(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                account.withdraw(amount, account.get_min_balance())
                return
        print("Account not found.\n")

    def get_account_details(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.display(account.account_number, account.name,
                             account.type, account.balance)
                return
        print("Account not found.\n")
