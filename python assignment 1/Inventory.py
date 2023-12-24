class Inventory:
    def __init__(self, InventoryID, Product, QuantityInStock,LastStockUpdate):
        self.InventoryID = InventoryID
        self.Product = Product
        self.QuantityInStock =QuantityInStock
        self.LastStockUpdate = LastStockUpdate

    def print_details(self):
        print("InventoryID:", self.InventoryID)
        print("Product:", self.Product)
        print("QuantityInStock:", self.QuantityInStock)
        print("LastStockUpdate:",self.LastStockUpdate)

Inventory=  Inventory(InventoryID=1,Product="1", QuantityInStock=10,LastStockUpdate="2023-01-01")
Inventory= Inventory.print_details()
