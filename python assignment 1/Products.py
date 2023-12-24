class Product:
    def __init__(self, ProductID, ProductName, Description, Price):
        self.ProductID = ProductID
        self.ProductName =ProductName
        self.Description =Description
        self.Price = Price


    def print_details(self):
        print("ProductID:", self.ProductID)
        print("ProductName:", self.ProductName)
        print("Description:", self.Description)
        print("Price:", self.Price)



Product = Product(ProductID=1, ProductName="Laptop", Description="High-performance Laptop", Price=899.99)
Product= Product.print_details()