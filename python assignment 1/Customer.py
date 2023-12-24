class Customer:
    def __init__(self, CustomerID, FirstName, LastName, Email, Phone, Address):
        self.CustomerID = CustomerID
        self.FirstName =FirstName
        self.LastName = LastName
        self.Email = Email
        self.Phone = Phone
        self.Address = Address

#sample data
    def print_details(self):
        print("CustomerID:", self.CustomerID)
        print("FirstName:", self.FirstName)
        print("LastName:", self.LastName)
        print("Email:", self.Email)
        print("Phone:", self.Phone)
        print("Address:", self.Address)

Customer=Customer(CustomerID=2, FirstName="John", LastName="Doe", Email="john.doe@example.com", Phone="123-456-7890",Address="123 Main St")
Customer= Customer.print_details()