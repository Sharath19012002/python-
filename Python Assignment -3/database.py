import mysql.connector
from mysql.connector import Error
from datetime import datetime
class InvalidAccountException(Exception):
    pass

class InsufficientFundException(Exception):
    pass

class OverDraftLimitExceeded(Exception):
    pass


class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address


class Account:
    last_account_number = 0

    def __init__(self, customer, account_type, balance=0.0):
        Account.last_account_number += 1
        self.account_number = Account.last_account_number
        self.customer = customer
        self.account_type = account_type
        self.balance = balance


class Transaction:
    def __init__(self, account, description, transaction_type, transaction_amount):
        self.account = account
        self.description = description
        self.date_time = datetime.now()
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount


class SavingsAccount(Account):
    def __init__(self, customer, interest_rate):
        super().__init__(customer, "Savings")
        self.interest_rate = interest_rate


class CurrentAccount(Account):
    def __init__(self, customer, overdraft_limit):
        super().__init__(customer, "Current")
        self.overdraft_limit = overdraft_limit


class ZeroBalanceAccount(Account):
    def __init__(self, customer):
        super().__init__(customer, "ZeroBalance")

class DBUtil:
    @staticmethod
    def get_db_conn():
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="hmbank"
            )
            return connection

        except Exception as e:
            print(f"Error: {e}")
            return None

class BankRepositoryImpl():
    def create_account(self, customer, acc_type, balance):
        try:
            conn = DBUtil.get_db_conn()
            cursor = conn.cursor()

            # Insert customer details
            cursor.execute("INSERT INTO customers (customer_id, first_name, last_name, email, phone_number, address) "
                           "VALUES (%s, %s, %s, %s, %s, %s)",
                           (customer.customer_id, customer.first_name, customer.last_name, customer.email,
                            customer.phone_number, customer.address))
            conn.commit()

            # Insert account details
            cursor.execute("INSERT INTO accounts (account_type, balance, customer_id) "
                           "VALUES (%s, %s, %s)",
                           (acc_type, balance, customer.customer_id))
            conn.commit()

            return Account.last_account_number

        except Error as e:
            print(f"Error: {e}")
            return None

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def list_accounts(self):
        try:
            conn = DBUtil.get_db_conn()
            cursor = conn.cursor()

            # Retrieve all accounts
            cursor.execute("SELECT * FROM accounts")
            accounts = cursor.fetchall()

            return [self.map_account(row) for row in accounts]

        except Error as e:
            print(f"Error: {e}")
            return None

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def calculate_interest(self):
        try:
            conn = DBUtil.get_db_conn()
            cursor = conn.cursor()

            # Calculate interest for savings accounts
            cursor.execute("UPDATE accounts SET balance = balance * (1 + interest_rate / 100) "
                           "WHERE account_type = 'Savings'")
            conn.commit()

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_account_balance(self, account_number):
        try:
            conn = DBUtil.get_db_conn()
            cursor = conn.cursor()

            # Retrieve account balance
            cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
            balance = cursor.fetchone()

            if balance:
                return balance[0]
            else:
                return 'Account number is not present'

        except Error as e:
            print(f"Error: {e}")
            return None

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def deposit(self, account_number, amount):
        try:
            conn = DBUtil.get_db_conn()
            cursor = conn.cursor()

            # Update account balance for deposit
            cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_number = %s", (amount, account_number))
            conn.commit()

            # Record the transaction
            self.record_transaction(account_number, "Deposit", "Deposit", amount)

            return self.get_account_balance(account_number)

        except Error as e:
            print(f"Error: {e}")
            return None

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def withdraw(self, account_number, amount):
        try:
            conn = DBUtil.get_db_conn()
            cursor = conn.cursor()

            # Retrieve current account balance
            cursor.execute("SELECT balance, account_type FROM accounts WHERE account_number = %s", (account_number,))
            result = cursor.fetchone()

            if result:
                balance, account_type = result
                if account_type == "Savings" and (balance - amount) < 500:
                    raise InsufficientFundException("Withdrawal violates minimum balance rule.")

                if account_type == "Current" and (balance - amount) < 0:
                    raise OverDraftLimitExceeded("Withdrawal exceeds available balance and overdraft limit.")

                # Update account balance for withdrawal
                cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_number = %s",
                               (amount, account_number))
                conn.commit()

                # Record the transaction
                self.record_transaction(account_number, "Withdrawal", "Withdrawal", amount)

                return self.get_account_balance(account_number)

            else:
                raise InvalidAccountException("Account not found.")

        except (InsufficientFundException, OverDraftLimitExceeded) as e:
            raise e

        except Error as e:
            print(f"Error: {e}")
            return None

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def transfer(self, from_account_number, to_account_number, amount):
        try:
            conn = DBUtil.get_db_conn()
            cursor = conn.cursor()

            # Check if both accounts exist
            if not self.account_exists(from_account_number) or not self.account_exists(to_account_number):
                raise InvalidAccountException("One or both accounts not found.")

            # Check if the source account has sufficient funds
            from_balance = self.get_account_balance(from_account_number)
            if from_balance < amount:
                raise InsufficientFundException("Insufficient funds for the transfer.")

            # Update source account balance for withdrawal
            cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_number = %s",
                           (amount, from_account_number))
            conn.commit()

            # Update destination account balance for deposit
            cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_number = %s",
                           (amount, to_account_number))
            conn.commit()

            # Record the transactions
            self.record_transaction(from_account_number, "Transfer", "Transfer to " + str(to_account_number), amount)
            self.record_transaction(to_account_number, "Transfer", "Transfer from " + str(from_account_number), amount)

            return self.get_account_balance(from_account_number), self.get_account_balance(to_account_number)

        except (InsufficientFundException, InvalidAccountException) as e:
            raise e

        except Error as e:
            print(f"Error: {e}")
            return None

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_account_details(self, account_number):
        try:
            conn = DBUtil.get_db_conn()
            cursor = conn.cursor()

            # Retrieve account details
            cursor.execute("SELECT * FROM accounts INNER JOIN customers "
                           "ON accounts.customer_id = customers.customer_id "
                           "WHERE account_number = %s", (account_number,))
            result = cursor.fetchone()

            if result:
                account_details = {
                    "account_number": result[0],
                    "account_type": result[1],
                    "balance": result[2],
                    "customer_id": result[3],
                    "first_name": result[5],
                    "last_name": result[6],
                    "email": result[7],
                    "phone_number": result[8],
                    "address": result[9]
                }
                return account_details

            else:
                raise InvalidAccountException("Account not found.")

        except InvalidAccountException as e:
            raise e

        except Error as e:
            print(f"Error: {e}")
            return None

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_transactions(self, account_number, from_date, to_date):
        try:
            conn = DBUtil.get_db_conn()
            cursor = conn.cursor()

            # Retrieve transactions within the date range
            cursor.execute("SELECT * FROM transactions WHERE account_number = %s "
                           "AND date_time BETWEEN %s AND %s",
                           (account_number, from_date, to_date))
            transactions = cursor.fetchall()

            return [self.map_transaction(row) for row in transactions]

        except Error as e:
            print(f"Error: {e}")
            return None

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def record_transaction(self, account_number, description, transaction_type, transaction_amount):
        try:
            conn = DBUtil.get_db_conn()
            cursor = conn.cursor()

            # Record the transaction
            cursor.execute("INSERT INTO transactions (account_number, description, date_time, transaction_type, transaction_amount) "
                           "VALUES (%s, %s, %s, %s, %s)",
                           (account_number, description, datetime.now(), transaction_type, transaction_amount))
            conn.commit()

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    @staticmethod
    def map_account(row):
        return {
            "account_number": row[0],
            "account_type": row[1],
            "balance": row[2],
            "customer_id": row[3]
        }

    @staticmethod
    def map_transaction(row):
        return {
            "account_number": row[0],
            "description": row[1],
            "date_time": row[2],
            "transaction_type": row[3],
            "transaction_amount": row[4]
        }

    def account_exists(self, account_number):
        try:
            conn = DBUtil.get_db_conn()
            cursor = conn.cursor()

            # Check if the account exists
            cursor.execute("SELECT * FROM accounts WHERE account_number = %s", (account_number,))
            return cursor.fetchone() is not None

        except Error as e:
            print(f"Error: {e}")
            return False

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()


# Example usage:

# Create an instance of BankRepositoryImpl and test the methods
bank_repository = BankRepositoryImpl()

# Create a customer
customer = Customer(1, "Rohan", "Chaudhari", "Rohan@example.com", "1234567890", "123 jalagon")
customer1 = Customer(2, "Rohit", "Rajput", "Rohit@example.com", "1234567098", "12345 jalgaon")

# Create a SavingsAccount
savings_account_number = bank_repository.create_account(customer, "Savings", 1000.0)
print("Savings Account Number:", savings_account_number)

# Create a CurrentAccount
current_account_number = bank_repository.create_account(customer1, "Current", 2000.0)
print("Current Account Number:", current_account_number)

# Perform transactions
bank_repository.deposit(1, 500)
bank_repository.withdraw(1, 100)
#bank_repository.transfer(savings_account_number, current_account_number, 100.0)

# Get account details
savings_account_details = bank_repository.get_account_details(1)
current_account_details = bank_repository.get_account_details(1)

print("Savings Account Details:", savings_account_details)
print("Current Account Details:", current_account_details)

# Get account balance
savings_balance = bank_repository.get_account_balance(1)
current_balance = bank_repository.get_account_balance(1)

print("Savings Account Balance:", savings_balance)
#print("Current Account Balance:", current_balance)

# List all accounts
accounts_list = bank_repository.list_accounts()
print("All Accounts:", accounts_list)

# Calculate interest for savings accounts
bank_repository.calculate_interest()

# Get transactions
transactions = bank_repository.get_transactions(1, datetime(2023, 1, 1), datetime.now())
print("Savings Account Transactions:", transactions)
