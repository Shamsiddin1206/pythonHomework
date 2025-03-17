import json
import os.path

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.balance = balance
        self.name = name

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["account_number"], data["name"], data["balance"])


class Bank:
    FILE_NAME = "accounts.txt"

    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def save_to_file(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump({acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}, file)

    def load_from_file(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)
                self.accounts = {acc_num: Account.from_dict(acc) for acc_num, acc in data.items()}

    def create_account(self):
        name = input("Enter account holder name: ")
        while True:
            try:
                initial_deposit = float(input("Enter initial deposit amount: "))
                if initial_deposit < 0:
                    raise ValueError("Initial deposit cannot be negative.")
                break
            except ValueError as e:
                print("Invalid input:", e)

        account_number = str(1000 + len(self.accounts))
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        print(f"Account created successfully! Your account number is {account_number}.")

    def view_account(self):
        account_number = input("Enter account number: ")
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}, Name: {account.name}, Balance: {account.balance}")
        else:
            print("Account not found!")

    def deposit(self):
        account_number = input("Enter account number: ")
        account = self.accounts.get(account_number)
        if account:
            while True:
                try:
                    amount = float(input("Enter deposit amount: "))
                    if amount <= 0:
                        raise ValueError("Deposit amount must be positive.")
                    break
                except ValueError as e:
                    print("Invalid input:", e)
            account.balance += amount
            self.save_to_file()
            print("Deposit successful!")
        else:
            print("Account not found!")

    def withdraw(self):
        account_number = input("Enter account number: ")
        account = self.accounts.get(account_number)
        if account:
            while True:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    if amount <= 0:
                        raise ValueError("Withdrawal amount must be positive.")
                    if amount > account.balance:
                        raise ValueError("Insufficient funds.")
                    break
                except ValueError as e:
                    print("Invalid input:", e)
            account.balance -= amount
            self.save_to_file()
            print("Withdrawal successful!")
        else:
            print("Account not found!")

    def menu(self):
        while True:
            print("\nWelcome to the Bank Application!")
            print("1. Create Account")
            print("2. View Account")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Exit")

            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    self.create_account()
                case "2":
                    self.view_account()
                case "3":
                    self.deposit()
                case "4":
                    self.withdraw()
                case "5":
                    print("Exiting the application.")
                    break
                case _:
                    print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    bank = Bank()
    bank.menu()
