from main import Account


# task 8-2 subclass inherited from accountclass
class SavingsAccount(Account):

    # Subclass representing a Savings Account.

    def __init__(self, account_number, interest_rate, account_balance=0.0):
        super().__init__(account_number, "Savings", account_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        # Calculate and add interest to the savings account balance.

        interest = self.interest_rate * self.account_balance
        self.account_balance += interest
        print(f"Interest calculated and added. New balance: {self.account_balance}")


class CurrentAccount(Account):
    # Subclass representing a Current Account.

    OVERDRAFT_LIMIT = 1000.0  # Example overdraft limit

    def __init__(self, account_number, overdraft_limit, account_balance=0.0):
        super().__init__(account_number, "Current", account_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):

        # Withdraw the specified amount from the current account with overdraft limit.
        available_balance = self.account_balance + self.overdraft_limit
        if amount <= available_balance:
            self.account_balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.account_balance}")
        else:
            print("Insufficient funds. Withdrawal failed.")


'''
# Example usage:

# Create a savings account
savings_account = SavingsAccount(account_number=2001, interest_rate=0.05)
savings_account.deposit(1000.0)
savings_account.calculate_interest()

# Create a current account
current_account = CurrentAccount(account_number=3001, overdraft_limit=500.0)
current_account.deposit(200.0)
current_account.withdraw(300.0)
'''


class Bank:
    """
    Bank class representing the banking system.
    """

    def main(self):
        while True:
            print("\nBanking System Menu:")
            print("1. Create Savings Account")
            print("2. Create Current Account")
            print("3. Exit")

            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                # Create Savings Account
                account_number = int(input("Enter account number: "))
                interest_rate = float(input("Enter interest rate for the savings account: "))
                savings_account = SavingsAccount(account_number, interest_rate)
                self.perform_operations(savings_account)

            elif choice == '2':
                # Create Current Account
                account_number = int(input("Enter account number: "))
                overdraft_limit = float(input("Enter overdraft limit for the current account: "))
                current_account = CurrentAccount(account_number, overdraft_limit)
                self.perform_operations(current_account)

            elif choice == '3':
                print("Exiting the Banking System.")
                break

            else:
                print("Invalid choice. Please enter a valid option.")

    def perform_operations(self, account):

        while True:
            print("\nAccount Operations Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Calculate Interest (for Savings Account)")
            print("4. Exit")

            operation_choice = input("Enter your choice (1-4): ")

            if operation_choice == '1':
                amount = float(input("Enter the deposit amount: "))
                account.deposit(amount)

            elif operation_choice == '2':
                amount = float(input("Enter the withdrawal amount: "))
                account.withdraw(amount)

            elif operation_choice == '3' and isinstance(account, SavingsAccount):
                account.calculate_interest()

            elif operation_choice == '4':
                print("Exiting Account Operations.")
                break

            else:
                print("Invalid choice. Please enter a valid option.")


bank = Bank()
bank.main()