class Order:
    def __init__(self, OrderID, CustomerID, OrderDate,TotalAmount):
        self.OrderID = OrderID
        self.CustomerID = CustomerID
        self.OrderDate =OrderDate
        self.TotalAmount = TotalAmount

    def print_details(self):
        print("OrderID:", self.OrderID)
        print("CustomerID:", self.CustomerID)
        print("OrderDate:", self.OrderDate)
        print("TotalAmount:",self.TotalAmount)


Order= Order(OrderID=1, CustomerID="1", OrderDate="2023-01-15", TotalAmount=899.99)
Order= Order.print_details()