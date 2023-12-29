
#1
def check_order_status(order_status):
    if order_status == "Delivered":
        return "The order has been delivered."
    elif order_status == "Processing":
        return "The order is still being processed."
    elif order_status == "Cancelled":
        return "The order has been cancelled."
    else:
        return "Invalid order status."

# Example usage
order_status_input = input("Enter the order status: ")
result = check_order_status(order_status_input)
print(result)


#2
def categorize_parcel(weight):
    if weight < 5:
        return "Light"
    elif 5 <= weight <= 15:
        return "Medium"
    else:
        return "Heavy"

# Example usage
parcel_weight_input = float(input("Enter the parcel weight: "))
category = categorize_parcel(parcel_weight_input)
print(f"The parcel is categorized as {category}.")



#3
# Sample employee data (replace with database queries in a real system)
employees = {
    "employee1": "employee1pass",
    "employee2": "employee2pass",
    # Add more employees as needed
}

def authenticate_user(username, password):
    if username in employees and employees[username] == password:
        return f"Authentication successful. Welcome, {username} (employee)."
    else:
        return "Authentication failed. Invalid username or password."

# Example usage
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")
authentication_result = authenticate_user(username_input, password_input)
print(authentication_result)


#4
couriers = [
    {"CourierID": 1, "Capacity": 10, "Location": "A"},
    {"CourierID": 2, "Capacity": 15, "Location": "B"},
]

shipments = [
    {"ShipmentID": 101, "Weight": 8, "Destination": "A"},
    {"ShipmentID": 102, "Weight": 12, "Destination": "B"},
]

def assign_courier(shipment):
    for courier in couriers:
        if courier["Capacity"] >= shipment["Weight"] and courier["Location"] == shipment["Destination"]:
            return f"Assigned CourierID {courier['CourierID']} to ShipmentID {shipment['ShipmentID']}."
    return "No suitable courier found for the shipment."

# Example usage
for shipment in shipments:
    assignment_result = assign_courier(shipment)
    print(assignment_result)



#5
orders = [
    {"OrderID": 1, "CustomerName": "customer1", "Status": "Delivered"},
    {"OrderID": 2, "CustomerName": "customer1", "Status": "Processing"},
    {"OrderID": 3, "CustomerName": "customer2", "Status": "Delivered"},
]

def display_customer_orders(customer_name):
    print(f"Orders for {customer_name}:")
    for order in orders:
        if order["CustomerName"] == customer_name:
            print(f"OrderID: {order['OrderID']}, Status: {order['Status']}")

# Example usage
customer_name_input = input("Enter customer name: ")
display_customer_orders(customer_name_input)



#6
courier = {"CourierID": 1, "CurrentLocation": "A", "Destination": "B"}

def track_courier_location(courier):
    print(f"Courier {courier['CourierID']} is currently at {courier['CurrentLocation']}.")
    while courier['CurrentLocation'] != courier['Destination']:
        new_location = input("Enter the new location of the courier: ")
        courier['CurrentLocation'] = new_location
        print(f"Courier {courier['CourierID']} is now at {courier['CurrentLocation']}.")

    print(f"Courier {courier['CourierID']} has reached its destination {courier['Destination']}.")

# Example usage
track_courier_location(courier)



#7
parcel_tracking_history = []

def update_parcel_location(location):
    parcel_tracking_history.append(location)
    print(f"Parcel tracking history updated. Current location: {location}")

# Example usage
update_parcel_location("Warehouse A")
update_parcel_location("In Transit")
update_parcel_location("Destination B")






#8
couriers = [
    {"CourierID": 1, "CurrentLocation": "Warehouse A"},
    {"CourierID": 2, "CurrentLocation": "Warehouse B"},
    {"CourierID": 3, "CurrentLocation": "Warehouse C"},
]

def find_nearest_courier(destination):
    nearest_courier = None
    min_distance = float('inf')

    for courier in couriers:
        distance = abs(ord(courier['CurrentLocation'][0]) - ord(destination[0]))

        if distance < min_distance:
            min_distance = distance
            nearest_courier = courier

    return nearest_courier

# Example usage
order_destination_input = input("Enter the destination for the new order: ")
nearest_courier = find_nearest_courier(order_destination_input)
print(f"The nearest available courier is CourierID {nearest_courier['CourierID']} at {nearest_courier['CurrentLocation']}.")




#9
parcel_tracking_data = [
    ["123456", "In Transit"],
    ["789012", "Out for Delivery"],
    ["345678", "Delivered"],
]

def track_parcel(parcel_number):
    for entry in parcel_tracking_data:
        if entry[0] == parcel_number:
            status = entry[1]
            if status == "In Transit":
                print("Parcel in transit.")
            elif status == "Out for Delivery":
                print("Parcel out for delivery.")
            elif status == "Delivered":
                print("Parcel delivered.")
            else:
                print("Invalid status.")
            return
    print("Parcel not found.")

# Example usage
parcel_number_input = input("Enter the parcel tracking number: ")
track_parcel(parcel_number_input)





#11
def format_address(street, city, state, zip_code):
    formatted_address = f"{street.title()}, {city.title()}, {state.upper()} {zip_code}"
    return formatted_address

# Example usage
street_input = input("Enter street: ")
city_input = input("Enter city: ")
state_input = input("Enter state: ")
zip_code_input = input("Enter zip code: ")
formatted_address = format_address(street_input, city_input, state_input, zip_code_input)
print("Formatted Address:", formatted_address)



#12
def generate_order_confirmation_email(customer_name, order_number, delivery_address, delivery_date):
    email_content = (
        "Dear %s,\n\n"
        "Order Confirmation:\n"
        "Order Number: %s\n"
        "Delivery Address: %s\n"
        "Expected Delivery Date: %s\n\n"
        "Thank you for choosing our courier service!"
        % (customer_name, order_number, delivery_address, delivery_date)
    )
    return email_content

# Example usage
customer_name_input = input("Enter customer name: ")
order_number_input = input("Enter order number: ")
delivery_address_input = input("Enter delivery address: ")
delivery_date_input = input("Enter expected delivery date: ")
confirmation_email = generate_order_confirmation_email(customer_name_input, order_number_input, delivery_address_input, delivery_date_input)
print(confirmation_email)



#13
def calculate_shipping_cost(source_address, destination_address, parcel_weight):
    # Replace with your actual distance and cost calculation logic
    distance = abs(ord(source_address[0]) - ord(destination_address[0]))
    shipping_cost = distance * parcel_weight * 0.1
    return shipping_cost

# Example usage
source_address_input = input("Enter source address: ")
destination_address_input = input("Enter destination address: ")
parcel_weight_input = float(input("Enter parcel weight: "))
shipping_cost = calculate_shipping_cost(source_address_input, destination_address_input, parcel_weight_input)
print("Shipping Cost:", shipping_cost)


# 14
import random
import string


def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(12))
    return password


# Example usage
generated_password = generate_password()
print("Generated Password:", generated_password)



#15
def find_similar_addresses(address, addresses_list):
    similar_addresses = [addr for addr in addresses_list if addr==address]
    return similar_addresses

# Example usage
addresses_list = ["123 Main St, City1", "456 First Ave, City2", "123 Main St, City3", "789 Second St, City4"]
address_input = input("Enter an address: ")
similar_addresses = find_similar_addresses(address_input, addresses_list)
print("Similar Addresses:", similar_addresses)