# Bank App

This Python program implements a simple banking application using object-oriented programming (OOP) concepts. The application allows users to perform various operations related to different types of accounts such as savings, current, and salary accounts.

## Classes

### `Bank_Account`

The `Bank_Account` class serves as the base class for different types of bank accounts. It includes common attributes such as balance, account number, holder's name and methods shared among all account types, such as initializing an account, depositing, and withdrawing funds.

### Account Types
There are three account types:

1. **`Saving_Account`**
2. **`Current_Account`**
3. **`Salary_Account`**\
All the three types of account have the common attributes and methods that is:
   - Attributes: `min_balance`: Minimum balance an account should have, `opening_balance`: Initial deposit to open the account.
   - Methods: `get_min_balance()`: returns the minimun balance, `get_opening_balance()`: returns the opening balance



### `Banking_Application`

The `Banking_Application` class manages the overall functionality of the banking application. It includes methods for creating new accounts, displaying account details, updating accounts, deleting accounts, depositing and withdrawing amounts and searching for accounts.

## Usage

1. Run the bank.py file to start the banking application.
2. Choose from the available options (1-8) to perform various banking operations.

## Operations

1. **Create a new account**: Enter account holder's name, choose the account type, and provide the initial balance. The program enforces minimum balance constraints based on the account type.

2. **Display all accounts**: View details of all existing accounts.

3. **Update an account**: Modify the account holder's name for a specified account.

4. **Delete an account**: Remove an existing account from the system.

5. **Deposit an amount into your account**: Add funds to a specific account.

6. **Withdraw an amount from your account**: Remove funds from a specific account, ensuring minimum balance constraints.

7. **Search for account**: Find and display details of a specific account.

8. **Exit**: Terminate the banking application.

## Constraints

- Each account type has a minimum balance requirement to open the account.
- Each account type may require maintaining a minimum balance before withdrawing an amount.
- No database is used; account data is stored in memory.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/MiadHasan/bank-app.git
    cd bank-app
    ```

2. Run the program:

    ```bash
    python bank.py
    ```

3. Follow the on-screen prompts to interact with the banking application.