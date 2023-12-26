class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None, email=None, phone_number=None, address=None):
        self._customer_id = customer_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone_number = phone_number
        self._address = address

    # Getter methods
    def get_customer_id(self):
        return self._customer_id

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_email(self):
        return self._email

    def get_phone_number(self):
        return self._phone_number

    def get_address(self):
        return self._address

    # Setter methods
    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_email(self, email):
        self._email = email

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def set_address(self, address):
        self._address = address

    def print_all_information(self):
        print(f"Customer ID: {self._customer_id}")
        print(f"First Name: {self._first_name}")
        print(f"Last Name: {self._last_name}")
        print(f"Email Address: {self._email}")
        print(f"Phone Number: {self._phone_number}")
        print(f"Address: {self._address}")
