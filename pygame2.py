
import os
import random
import string

# Define the base class for Accounts
class Account:
    def __init__(self, account_number, password, account_type, balance=0):
        self.account_number = account_number
        self.password = password
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")

    def get_balance(self):
        return self.balance

# Define the PersonalAccount class inheriting from Account
class PersonalAccount(Account):
    def __init__(self, account_number, password, balance=0):
        super().__init__(account_number, password, 'Personal', balance)

# Define the BusinessAccount class inheriting from Account
class BusinessAccount(Account):
    def __init__(self, account_number, password, balance=0):
        super().__init__(account_number, password, 'Business', balance)

# Function to generate a random account number
def generate_account_number():
    return ''.join(random.choices(string.digits, k=10))

# Function to generate a random password
def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

# Function to save account information to file
def save_account_to_file(account):
    with open("accounts.txt", "a") as file:
        file.write(f"{account.account_number},{account.password},{account.account_type},{account.balance}\n")

# Function to read account information from file
def read_accounts_from_file():
    accounts = {}
    if os.path.exists("accounts.txt"):
        with open("accounts.txt", "r") as file:
            for line in file:
                account_number, password, account_type, balance = line.strip().split(",")
                balance = float(balance)
                if account_type == "Personal":
                    account = PersonalAccount(account_number, password, balance)
                else:
                    account = BusinessAccount(account_number, password, balance)
                accounts[account_number] = account
    return accounts

# Function to create a new account
def create_account(account_type):
    account_number = generate_account_number()
    password = generate_password()
    if account_type == "Personal":
        account = PersonalAccount(account_number, password)
    else:
        account = BusinessAccount(account_number, password)
    save_account_to_file(account)
    print(f"Account created successfully! Account Number: {account_number}, Password: {password}")

# Function to login to an account
def login(account_number, password, accounts):
    if account_number in accounts and accounts[account_number].password == password:
        return accounts[account_number]
    else:
        print("Invalid account number or password!")
        return None

# Function to transfer money between accounts
def transfer_money(sender, receiver_account_number, amount, accounts):
    if receiver_account_number not in accounts:
        print("Receiving account does not exist!")
    elif sender.balance < amount:
        print("Insufficient funds!")
    else:
        sender.withdraw(amount)
        accounts[receiver_account_number].deposit(amount)
        print(f"${amount} transferred to account {receiver_account_number}.")

def main():
    accounts = read_accounts_from_file()
    while True:
        print("\n1. Open Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_type = input("Enter account type (Personal/Business): ")
            create_account(account_type)
        elif choice == "2":
            account_number = input("Enter account number: ")
            password = input("Enter password: ")
            account = login(account_number, password, accounts)
            if account:
                while True:
                    print("\n1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transfer Money")
                    print("5. Delete Account")
                    print("6. Logout")
                    action = input("Enter your choice: ")

                    if action == "1":
                        print(f"Current balance: ${account.get_balance()}")
                    elif action == "2":
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                        accounts[account.account_number] = account  # Update the account in the dictionary
                        save_account_to_file(account)  # Update the account in the file
                    elif action == "3":
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                        accounts[account.account_number] = account  # Update the account in the dictionary
                        save_account_to_file(account)  # Update the account in the file
                    elif action == "4":
                        receiver_account_number = input("Enter receiver account number: ")
                        amount = float(input("Enter amount to transfer: "))
                        transfer_money(account, receiver_account_number, amount, accounts)
                        save_account_to_file(accounts[account.account_number])  # Update sender account in the file
                        save_account_to_file(accounts[receiver_account_number])  # Update receiver account in the file
                    elif action == "5":
                        confirm = input("Are you sure you want to delete this account? (yes/no): ")
                        if confirm.lower() == "yes":
                            del accounts[account_number]
                            with open("accounts.txt", "w") as file:
                                for acc in accounts.values():
                                    save_account_to_file(acc)
                            print("Account deleted successfully.")
                            break
                    elif action == "6":
                        break
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
