class OrderDetails:
    def __init__(self, OrderDetailID, Order, Product, Quantity):
        self.OrderDetailID = OrderDetailID
        self.Order = Order
        self.Product = Product
        self.Quantity = Quantity

    def print_details(self):
        print("OrderDetailID:", self.OrderDetailID)
        print("Order:", self.Order)
        print("Product:", self.Product)
        print("Quantity:",self.Quantity)


OrderDetails= OrderDetails(OrderDetailID=1, Order="1", Product="1", Quantity=1)
OrderDetails= OrderDetails.print_details()