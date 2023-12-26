class Customer:
    #Customer class representing a bank customer.
    def __init__(self, customer_id, first_name, last_name, email, phone_number, address):
        #Constructor for Customer class.
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address


class Account:
    #Account class representing a bank account.
    def __init__(self, account_number, account_type, account_balance=0.0):
        self.account_number = account_number
        self.account_type = account_type
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited {amount} into account {self.account_number} . New balance: {self.account_balance}")

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.account_balance}")
        else:
            print("Insufficient balance. Withdrawal failed.")

    def calculate_interest(self):
        if self.account_type == "Savings":
            interest = 0.045 * self.account_balance
            self.account_balance += interest
            print(f"Interest calculated and added. New balance: {self.account_balance}")



class Bank:
    def main(self):
        # Create a customer
        customer = Customer(customer_id=1, first_name="John", last_name="Doe",
                            email="john.doe@example.com", phone_number="1234567890", address="123 Main Street")


        # Create an account for the customer
        account = Account(account_number=1001, account_type="Savings")

        # Deposit and withdraw operations
        account.deposit(1000.0)
        account.withdraw(500.0)

        # Calculate and add interest for savings account
        account.calculate_interest()


# Create an instance of the Bank class and execute the main method
bank = Bank()
bank.main()


#example for task 8-1
# Example usage:

# Create an account for the customer
account = Account(account_number=1001, account_type="Savings")

# Deposit and withdraw operations with different data types
account.deposit(1000.0)   # float
account.withdraw(500.0)    # float

account.deposit(200)       # int
account.withdraw(100)      # int

account.deposit(300.5)     # double
account.withdraw(150.25)   # double