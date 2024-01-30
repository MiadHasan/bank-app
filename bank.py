from banking_applicaition import Banking_Application

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

    # taking user input to perform the operations
    choice = input("Enter your choice (1-8): ")
    print("")
    if choice == "1":
        name = input("Enter account holder's name: ")
        print("There are three types of accounts: ")
        print("1. Saving account")
        print("2. Current Account")
        print("3. Salary account")
        account_type_option = input("Enter account type (1-3): ")
        if account_type_option not in ["1", "2", "3"]:
            print("Invalid option.\n")
            continue
        # get details of different account types
        account_type, min_balance, opening_balance = bank.get_constrains_and_type(
            account_type_option)
        print(
            f"Opening deposit for this account is {opening_balance} and minimum balance is {min_balance}"
        )
        balance = float(
            input("Enter initial balance more than opening deposit: "))
        if balance < min_balance:
            print("Insufficient opening balance.\n")
            continue
        acc_num = bank.create_new_account(name, account_type, balance)
        print(
            f"Account created successfully. Your account number is: {acc_num}.\n")

    elif choice == "2":
        bank.display_accounts()

    elif choice == "3":
        account_number = int(input("Enter account number to update: "))
        new_name = input("Enter new account holder name: ")
        bank.update_account(account_number, new_name)

    elif choice == "4":
        account_number = int(input("Enter account number to delete: "))
        bank.delete_account(account_number)

    elif choice == "5":
        account_number = int(input("Enter account number to deposit: "))
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print(
                "Invalid amount. Please enter a positive amount to deposit.\n")
            continue
        bank.deposit_amount(account_number, amount)

    elif choice == "6":
        account_number = int(input("Enter account number to withdraw: "))
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print(
                "Invalid amount. Please enter a positive amount to withdraw.\n")
            continue
        bank.withdraw_amount(account_number, amount)

    elif choice == "7":
        account_number = int(input("Enter account number to search: "))
        bank.get_account_details(account_number)

    elif choice == "8":
        print("Exiting the banking application.\n")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 8.\n")
