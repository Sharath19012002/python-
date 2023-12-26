from account import Account

class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_type, initial_balance):
        account = Account(account_number, account_type, initial_balance)
        self.accounts.append(account)
        print(f"Account created: {account_number}, Type: {account_type}, Initial Balance: ${initial_balance:.2f}")

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print(f"Account {account_number} not found.")

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print(f"Account {account_number} not found.")

    def calculate_interest(self, account_number):
        account = self.find_account(account_number)
        if account and account.get_account_type() == "Savings":
            account.calculate_interest()
        elif account:
            print("Interest calculation is applicable only for Savings accounts.")
        else:
            print(f"Account {account_number} not found.")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None