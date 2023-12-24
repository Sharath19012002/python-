from Customer import Customer
from Inventory import Inventory
from Products import Product
from OrderDetails import OrderDetails
from Orders import Order




def add_product(self, product):
    # Check for duplicate products
    if any(p.product_id == product.product_id or p.name == product.name for p in self.products):
        raise ValueError("Duplicate product found.")
    self.products.append(product)
    self.inventory.add(Inventory(product.product_id, 0))  # Add inventory entry with quantity 0


def update_product(self, product_id, new_name, new_category, new_price):
    product_index = next((i for i, p in enumerate(self.products) if p.product_id == product_id), None)
    if product_index is not None:
        self.products[product_index].name = new_name
        self.products[product_index].category = new_category
        self.products[product_index].price = new_price
    else:
        raise ValueError("Product not found.")


def remove_product(self, product_id):
    product_index = next((i for i, p in enumerate(self.products) if p.product_id == product_id), None)
    if product_index is not None:
        del self.products[product_index]
        self.inventory.discard(product_id)  # Remove inventory entry
    else:
        raise ValueError("Product not found.")


def add_order(self, order):
    # Update inventory when adding a new order
    for detail in order.order_details:
        inventory_item = next((i for i, inv in enumerate(self.inventory) if inv.product_id == detail.product_id), None)
        if inventory_item is not None:
            if self.inventory[inventory_item].quantity < detail.quantity:
                raise ValueError("Insufficient stock.")
            self.inventory[inventory_item].quantity -= detail.quantity
        else:
            raise ValueError("Product not found in inventory.")
    self.orders.append(order)


def update_order_status(self, order_id, new_status):
    order_index = next((i for i, o in enumerate(self.orders) if o.order_id == order_id), None)
    if order_index is not None:
        self.orders[order_index].status = new_status
    else:
        raise ValueError("Order not found.")


def remove_canceled_order(self, order_id):
    order_index = next((i for i, o in enumerate(self.orders) if o.order_id == order_id), None)
    if order_index is not None:
        canceled_order = self.orders.pop(order_index)
        # Restore inventory when removing a canceled order
        for detail in canceled_order.order_details:
            inventory_item = next((i for i, inv in enumerate(self.inventory) if inv.product_id == detail.product_id),
                                  None)
            if inventory_item is not None:
                self.inventory[inventory_item].quantity += detail.quantity
    else:
        raise ValueError("Order not found.")


def sort_orders_by_date(self, ascending=True):
    return sorted(self.orders, key=lambda x: x.order_date, reverse=not ascending)


def search_products(self, keyword):
    return [p for p in self.products if keyword.lower() in p.name.lower() or keyword.lower() in p.category.lower()]


def record_payment(self, order_id, amount):
    order_index = next((i for i, o in enumerate(self.orders) if o.order_id == order_id), None)
    if order_index is not None:
        self.payment_records.append(Order(order_id, amount, status="Paid"))
    else:
        raise ValueError("Order not found.")


def update_payment_status(self, order_id, new_status):
    payment_index = next((i for i, p in enumerate(self.payment_records) if p.order_id == order_id), None)
    if payment_index is not None:
        self.payment_records[payment_index].status = new_status
    else:
        raise ValueError("Payment record not found.")
