class Account:
    def __init__(self, account_number=None, account_type=None, account_balance=None):
        self._account_number = account_number
        self._account_type = account_type
        self._account_balance = account_balance

    # Getter methods
    def get_account_number(self):
        return self._account_number

    def get_account_type(self):
        return self._account_type

    def get_account_balance(self):
        return self._account_balance

    # Setter methods
    def set_account_number(self, account_number):
        self._account_number = account_number

    def set_account_type(self, account_type):
        self._account_type = account_type

    def set_account_balance(self, account_balance):
        self._account_balance = account_balance

    def display_account_info(self):
        print(f"Account Number: {self._account_number}")
        print(f"Account Type: {self._account_type}")
        print(f"Account Balance: ${self._account_balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited ${amount:.2f} into the account.")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._account_balance:
                self._account_balance -= amount
                print(f"Withdrew ${amount:.2f} from the account.")
            else:
                print("Insufficient balance. Withdrawal not allowed.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def calculate_interest(self):
        interest_rate = 0.045  # 4.5%
        interest_amount = self._account_balance * interest_rate
        print(f"Interest calculated: ${interest_amount:.2f}")