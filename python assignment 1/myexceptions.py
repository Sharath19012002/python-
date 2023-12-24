import mysql.connector
class DetailsNotFoundException(Exception):
    pass

class InvalidDataException(Exception):
    pass

class InsufficientStockException(Exception):
    pass

class IncompleteOrderException(Exception):
    pass

class PaymentFailedException(Exception):
    pass

class FileIOException(Exception):
    pass

class DatabaseAccessException(Exception):
    pass

class ConcurrencyException(Exception):
    pass

class AuthenticationException(Exception):
    pass

class AuthorizationException(Exception):
    pass

# Example Usage

class DataValidation:
    def register_user(self, Email):
        try:
            user_id = self.save_user_to_database(Email)
            print("User with email 'john.doe@email.com' successfully registered with ID {user_id}")
            if not self.is_valid_email(Email):
                raise InvalidDataException("Invalid email address.")
        except InvalidDataException as e:
            print("Error during registration: {str(e)}")
            # Inform the user about the invalid data

    def is_valid_email(self, email):
        email='john.doe@email.com'
        if (email):
            return True
        else:
            return False

class InventoryManagement:
    def process_order(self, order):
        try:
            self.check_inventory(order)
            self.process_order_details(order)
            order.status = "Processed"
            print("Order {order.order_id} processed successfully.")
        except InsufficientStockException:
            print("Insufficient stock. Unable to process the order.")
            order.update_order_status("Pending - Insufficient Stock")

    def check_inventory(self, order):
        for order_detail in order.order_details:
            if order_detail.product.quantity_in_stock < order_detail.quantity:
                raise InsufficientStockException()

class OrderProcessing:
    def process_order_details(self, OrderDetails):
        try:
            self.check_order_details(OrderDetails)
            self.process_order_details_logic(OrderDetails)
        except IncompleteOrderException as e:
            print("Error processing order details : {str(e)}")
    def check_order_details(self, order_details):
        for order_detail in order_details:
            if order_detail.product is None:
                raise IncompleteOrderException("Order detail is missing a product reference.")

class PaymentProcessing:
    def process_payment(self, order, payment_info):
        try:
            order.update_order_status("Payment Successful")
        except PaymentFailedException:
            print("Payment failed. Please try again or use a different payment method.")
            order.update_order_status("Payment Failed")

class FileIO:
    def write_to_file(self, data, filename):
        try:
            with open(filename, 'w') as file:
                file.write(data)
                print(f"Data successfully written to {filename}")
        except FileIOException as e:
            print(f"Error writing to file: {str(e)}")

class DatabaseAccess:
    def execute_query(self, query):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='TechShop',
                port=3306
            )
            print("Database Connection Succesfull")
            self.cursor = self.connection.cursor()

        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error: Access denied. Check your username and password.")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Error: Database does not exist.")
            else:
                print("Error:", err)
            print("Query executed successfully")
        except DatabaseAccessException as e:
            print(f"Error accessing the database: {str(e)}")

class ConcurrencyControl:
    def update_order(self, order):
        try:
            self.simulate_concurrent_update(order)
            print(f"Order {order.order_id} updated successfully.")
        except ConcurrencyException:
            print("Another user has modified the order. Please retry.")


class SecurityAndAuthentication:
    def authenticate_user(self, username, password):
        try:
            authenticated = self.check_credentials(username, password)
            if authenticated:
                print(f"User '{username}' successfully authenticated.")
            else:
                raise AuthenticationException("Invalid username or password.")
        except AuthenticationException:
            print("Authentication failed. Please provide valid credentials.")

    def authorize_access(self, user, resource):
        try:
            if self.has_permission(user, resource):
                print(f"User '{user}' authorized to access resource '{resource}'.")
            else:
                raise AuthorizationException("Unauthorized access. You do not have permission to access this resource.")
        except AuthorizationException:
            print("Unauthorized access. You do not have permission to access this resource.")
