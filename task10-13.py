import re

class InsufficientFundException(Exception):
    pass


class InvalidAccountException(Exception):
    pass


class OverDraftLimitExceeded(Exception):
    pass


class Customer:

    # Customer class representing a bank customer.

    def __init__(self, customer_id, first_name, last_name, email, phone_number, address):
        # Constructor for Customer class.

        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.set_email(email)
        self.set_phone_number(phone_number)
        self.address = address

    def set_email(self, email):
        # Simple email validation using regex
        email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if email_pattern.match(email):
            self.email = email
        else:
            raise ValueError("Invalid email address.")

    def set_phone_number(self, phone_number):

        # Simple phone number validation for 10 digits
        if re.match(r"^\d{10}$", phone_number):
            self.phone_number = phone_number
        else:
            raise ValueError("Invalid phone number.")


class Account:
    # Account class representing a bank account.

    account_number_generator = 1000  # Starting account number

    def __init__(self, customer, account_type, balance=0.0):
        self.account_number = Account.account_number_generator + 1
        Account.account_number_generator += 1
        self.customer = customer
        self.account_type = account_type
        self.balance = balance


class Bank:
    # Bank class representing the banking system.

    accounts = []  # List to store created accounts

    def create_account(self, customer, acc_type, balance):

        account = Account(customer, acc_type, balance)
        Bank.accounts.append(account)
        return account

    def get_account_balance(self, account_number):

        for account in Bank.accounts:
            if account.account_number == account_number:
                return account.balance
        raise InvalidAccountException("Account not found.")

    def deposit(self, account_number, amount):

        for account in Bank.accounts:
            if account.account_number == account_number:
                account.balance += amount
                return account.balance
        raise InvalidAccountException("Account not found.")

    def withdraw(self, account_number, amount):

        for account in Bank.accounts:
            if account.account_number == account_number:
                if account.balance >= amount:
                    account.balance -= amount
                    return account.balance
                else:
                    raise InsufficientFundException("Insufficient funds.")
        raise InvalidAccountException("Account not found.")

    def transfer(self, from_account_number, to_account_number, amount):
        # Transfer money from one account to another.

        from_account = None
        to_account = None

        for account in Bank.accounts:
            if account.account_number == from_account_number:
                from_account = account
            elif account.account_number == to_account_number:
                to_account = account

        if from_account and to_account:
            if from_account.balance >= amount:
                from_account.balance -= amount
                to_account.balance += amount
                return from_account.balance, to_account.balance
            else:
                raise InsufficientFundException("Insufficient funds.")
        else:
            raise InvalidAccountException("One or both accounts not found.")

    def get_account_details(self, account_number):

        # Retrieve account and customer details for a given account number.
        for account in Bank.accounts:
            if account.account_number == account_number:
                return account, account.customer
        raise InvalidAccountException("Account not found.")


class BankApp:

    # BankApp class to simulate the banking system.

    def main(self):
        bank = Bank()
        while True:
            try:
                print("\nBanking System Menu:")
                print("1. Create Account")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transfer")
                print("5. Get Account Balance")
                print("6. Get Account Details")
                print("7. Exit")

                choice = input("Enter your choice (1-7): ")

                if choice == '1':
                    customer_id = int(input("Enter Customer ID: "))
                    first_name = input("Enter First Name: ")
                    last_name = input("Enter Last Name: ")
                    email = input("Enter Email Address: ")
                    phone_number = input("Enter Phone Number: ")
                    address = input("Enter Address: ")

                    try:
                        customer = Customer(customer_id, first_name, last_name, email, phone_number, address)
                        acc_type = input("Choose Account Type (Savings/Current): ").capitalize()
                        balance = float(input("Enter Initial Balance: "))
                        bank.create_account(customer, acc_type, balance)
                        print("Account created successfully.")
                    except ValueError as e:
                        print(f"Error: {e}")

                elif choice == '2':
                    account_number = int(input("Enter Account Number: "))
                    amount = float(input("Enter Deposit Amount: "))
                    try:
                        balance = bank.deposit(account_number, amount)
                        print(f"Deposit successful. Current balance: {balance}")
                    except ValueError as e:
                        print(f"Error: {e}")

                elif choice == '3':
                    account_number = int(input("Enter Account Number: "))
                    amount = float(input("Enter Withdrawal Amount: "))
                    try:
                        balance = bank.withdraw(account_number, amount)
                        print(f"Withdrawal successful. Current balance: {balance}")
                    except ValueError as e:
                        print(f"Error: {e}")

                elif choice == '4':
                    from_account_number = int(input("Enter Source Account Number: "))
                    to_account_number = int(input("Enter Destination Account Number: "))
                    amount = float(input("Enter Transfer Amount: "))
                    try:
                        from_balance, to_balance = bank.transfer(from_account_number, to_account_number, amount)
                        print(f"Transfer successful. Source balance: {from_balance}, Destination balance: {to_balance}")
                    except ValueError as e:
                        print(f"Error: {e}")

                elif choice == '5':
                    account_number = int(input("Enter Account Number: "))
                    try:
                        balance = bank.get_account_balance(account_number)
                        print(f"Current balance: {balance}")
                    except ValueError as e:
                        print(f"Error: {e}")

                elif choice == '6':
                    account_number = int(input("Enter Account Number: "))
                    try:
                        account, customer = bank.get_account_details(account_number)
                        print(f"Account Details:\n{account.__dict__}\nCustomer Details:\n{customer.__dict__}")
                    except ValueError as e:
                        print(f"Error: {e}")

                elif choice == '7':
                    print("Exiting the Banking System.")
                    break

                else:
                    print("Invalid choice. Please enter a valid option.")

            except (InsufficientFundException, InvalidAccountException, OverDraftLimitExceeded) as e:
                print(f"Error: {e}")

            except Exception as e:
                print(f"An unexpected error occurred: {e}")


bank_app = BankApp()
bank_app.main()
