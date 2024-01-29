class Bank_Account:

    def __init__(self, name, balance, account_number) -> None:
        self.name = name
        self.balance = balance
        self.account_number = account_number


class Saving_Account(Bank_Account):

    def __init__(self, name="", balance=0, account_number=0) -> None:
        self.type = "saving"
        self.min_balance = 500
        self.opening_balance = 1000
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

    def display_accounts(self):
        for account in self.accounts:
            print(
                f"Account Number: {account.account_number} | Name: {account.name} | Account Type: {account.type} | Balance: {account.balance}"
            )

    def update_account(self, account_number, new_name):
        for account in self.accounts:
            if account.account_number == account_number:
                account.name = new_name
                print("Account updated successfully.")
                return
        print("Account not found.")


bank = Banking_Application()

while True:
    print("1. Create a new account")
    print("2. Display all accounts")
    print("3. Update an account")
    print("4. Delete an account")
    print("5. Deposit an amount into your account")
    print("6. Withdraw an amount from your account")
    print("7. Search for account")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        name = input("Enter account holder's name: ")
        print("There are three types of accounts: ")
        print("1. Saving account")
        print("2. Current Account")
        print("3. Salary account")
        account_type_option = input("Enter account type (1-3): ")
        if account_type_option not in ["1", "2", "3"]:
            print("Invalid option.")
            continue
        account_type, min_balance, opening_balance = bank.get_constrains_and_type(
            account_type_option)
        print(
            f"Opening deposit for this account is {opening_balance} and minimum balance is {min_balance}"
        )
        balance = int(
            input("Enter initial balance more than opening deposit: "))
        if balance < min_balance:
            print("Insufficient opening balance.")
            continue
        acc_num = bank.create_new_account(name, account_type, balance)
        print(f"Account created successfully. Account number is {acc_num}")

    elif choice == "2":
        bank.display_accounts()

    elif choice == "3":
        account_number = int(input("Enter account number to update: "))
        new_name = input("Enter new account holder name: ")
        bank.update_account(account_number, new_name)

    elif choice == "4":
        print(choice)

    elif choice == "5":
        print(choice)

    elif choice == "6":
        print(choice)

    elif choice == "7":
        print(choice)

    elif choice == "8":
        print(choice)
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
