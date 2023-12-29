
class User:
    def __init__(self, userID, userName, email, password, contactNumber, address):
        self.__userID = userID
        self.__userName = userName
        self.__email = email
        self.__password = password
        self.__contactNumber = contactNumber
        self.__address = address

class Courier:
    def __init__(self, courierID, senderName, senderAddress, receiverName, receiverAddress, weight, status, trackingNumber, deliveryDate, userId):
        self.__courierID = courierID
        self.__senderName = senderName
        self.__senderAddress = senderAddress
        self.__receiverName = receiverName
        self.__receiverAddress = receiverAddress
        self.__weight = weight
        self.__status = status
        self.__trackingNumber = trackingNumber
        self.__deliveryDate = deliveryDate
        self.__userId = userId

class Employee:
    def __init__(self, employeeID, employeeName, email, contactNumber, role, salary):
        self.__employeeID = employeeID
        self.__employeeName = employeeName
        self.__email = email
        self.__contactNumber = contactNumber
        self.__role = role
        self.__salary = salary

class Location:
    def __init__(self, locationID, locationName, address):
        self.__locationID = locationID
        self.__locationName = locationName
        self.__address = address

class CourierCompany:
    def __init__(self, companyName):
        self.__companyName = companyName
        self.__courierDetails = []  # Collection of Courier objects
        self.__employeeDetails = []  # Collection of Employee objects
        self.__locationDetails = []  # Collection of Location objects

class Payment:
    def __init__(self, paymentID, courierID, amount, paymentDate):
        self.__paymentID = paymentID
        self.__courierID = courierID
        self.__amount = amount
        self.__paymentDate = paymentDate
'''
'''
from abc import ABC, abstractmethod
import random

class ICourierUserService(ABC):

    @abstractmethod
    def placeOrder(self, courierObj):
        pass

    @abstractmethod
    def getOrderStatus(self, trackingNumber):

        pass

    @abstractmethod
    def cancelOrder(self, trackingNumber):

        pass

    @abstractmethod
    def getAssignedOrder(self, courierStaffId):
        pass


class Courier:
    unique_tracking_number = random.randint(1000, 9999)

    def __init__(self, senderName, senderAddress, receiverName, receiverAddress, weight, userId):
        self.trackingNumber = Courier.unique_tracking_number
        Courier.unique_tracking_number += 1


# Example of usage
class CourierUserService(ICourierUserService):

    def placeOrder(self, courierObj):
        return courierObj.trackingNumber

    def getOrderStatus(self, trackingNumber):
        return "In Transit" 

    def cancelOrder(self, trackingNumber):
        return True  

    def getAssignedOrder(self, courierStaffId):
        return [1234, 5678, 91011]  

# Example of usage
courierObj = Courier("John Doe", "123 Main St", "Jane Doe", "456 Second St", 2.5, 1)
courierUserService = CourierUserService()
tracking_number = courierUserService.placeOrder(courierObj)
print(f"Tracking Number: {tracking_number}")
status = courierUserService.getOrderStatus(tracking_number)
print(f"Order Status: {status}")
canceled = courierUserService.cancelOrder(tracking_number)
print(f"Order Canceled: {canceled}")
assigned_orders = courierUserService.getAssignedOrder(1)
print(f"Assigned Orders: {assigned_orders}")

###
from abc import ABC, abstractmethod
from datetime import datetime
import random


class Employee:
    def __init__(self, employeeID, employeeName, contactNumber):
        self.employeeID = employeeID
        self.employeeName = employeeName
        self.contactNumber = contactNumber


class Courier:
    tracking_number_counter = random.randint(1000, 9999)

    def __init__(self, senderName, senderAddress, receiverName, receiverAddress, weight, userId):
        self.trackingNumber = Courier.tracking_number_counter
        Courier.tracking_number_counter += 1
        self.senderName = senderName
        self.senderAddress = senderAddress
        self.receiverName = receiverName
        self.receiverAddress = receiverAddress
        self.weight = weight
        self.status = "yetToTransit"
        self.userId = userId


class ICourierUserService(ABC):
    @abstractmethod
    def placeOrder(self, courierObj):
        pass

    @abstractmethod
    def getOrderStatus(self, trackingNumber):
        pass

    @abstractmethod
    def cancelOrder(self, trackingNumber):
        pass

    @abstractmethod
    def getAssignedOrder(self, courierStaffId):
        pass


class ICourierAdminService(ABC):
    @abstractmethod
    def addCourierStaff(self, name, contactNumber):
        pass


# Custom Exceptions
class TrackingNumberNotFoundException(Exception):
    pass


class InvalidEmployeeIdException(Exception):
    pass


class Courier:
    tracking_number_counter = random.randint(1000, 9999)

    def __init__(self, senderName, senderAddress, receiverName, receiverAddress, weight, userId):
        self.trackingNumber = Courier.tracking_number_counter
        Courier.tracking_number_counter += 1
        self.senderName = senderName
        self.senderAddress = senderAddress
        self.receiverName = receiverName
        self.receiverAddress = receiverAddress
        self.weight = weight
        self.status = "yetToTransit"
        self.userId = userId


class CourierService(ICourierUserService, ICourierAdminService):
    courier_orders = []
    courier_staff = []

    def placeOrder(self, courierObj):
        CourierService.courier_orders.append(courierObj)
        return courierObj.trackingNumber

    def getOrderStatus(self, trackingNumber):
        for order in CourierService.courier_orders:
            if order.trackingNumber == trackingNumber:
                return order.status
        raise TrackingNumberNotFoundException("Tracking Number not found.")

    def cancelOrder(self, trackingNumber):
        for order in CourierService.courier_orders:
            if order.trackingNumber == trackingNumber:
                if order.status == "yetToTransit":
                    CourierService.courier_orders.remove(order)
                    return True
                else:
                    raise TrackingNumberNotFoundException(
                        "Cannot cancel an order that is already in transit or delivered.")
        raise TrackingNumberNotFoundException("Tracking Number not found.")

    def getAssignedOrder(self, courierStaffId):
        try:
            staff_orders = [order for order in CourierService.courier_orders if order.userId == courierStaffId]
            if not staff_orders:
                raise TrackingNumberNotFoundException("No orders assigned to the specified courier staff.")
            return staff_orders
        except TrackingNumberNotFoundException as e:
            print(f"Exception: {e}")

    def addCourierStaff(self, name, contactNumber):
        new_staff = Employee(employeeID=len(CourierService.courier_staff) + 1, employeeName=name,
                             contactNumber=contactNumber)
        CourierService.courier_staff.append(new_staff)
        return new_staff.employeeID

    def getEmployeeNameById(self, employeeID):
        for employee in CourierService.courier_staff:
            if employee.employeeID == employeeID:
                return employee.employeeName
        raise InvalidEmployeeIdException("Invalid Employee ID.")


courier_service = CourierService()

try:
    # Place Order
    order1 = Courier("Sharath", "123 green park colony", "tejas", "456 hyderabad", 11, userId=2)
    tracking_number = courier_service.placeOrder(order1)
    print(f"Order placed. Tracking Number: {tracking_number}")

    # Get Order Status
    status = courier_service.getOrderStatus(tracking_number)
    print(f"Order Status: {status}")

    # Cancel Order
    cancellation_result = courier_service.cancelOrder(tracking_number)
    print(f"Order Cancellation Result: {cancellation_result}")

    # Get Assigned Orders
    assigned_orders = courier_service.getAssignedOrder(courierStaffId=1)
    print(f"Assigned Orders: {assigned_orders}")

    # Add Courier Staff
    staff_id = courier_service.addCourierStaff(name="Courier Staff 2", contactNumber="9876542310")
    print(f"New Courier Staff added. Staff ID: {staff_id}")

    # Get Employee Name by ID
    employee_name = courier_service.getEmployeeNameById(employeeID=2)
    print(f"Employee Name: {employee_name}")

except (TrackingNumberNotFoundException, InvalidEmployeeIdException) as e:
    print(f"Exception: {e}")
except Exception as e:
    print(f"Unexpected Exception: {e}")
finally:
    print("Execution completed.")

# 10
import re


def validate_customer_info(data, detail):
    if detail == "name":
        return data.isalpha() and data.istitle()
    elif detail == "address":
        return data.isalnum() and not any(char.isdigit() for char in data)
    elif detail == "phone number":
        return re.match(r'^\d{3}-\d{3}-\d{4}$', data) is not None

    else:
        return False


# Example usage
name_input = input("Enter customer name: ")
print(validate_customer_info(name_input, "name"))

address_input = input("Enter customer address: ")
print(validate_customer_info(address_input, "address"))

phone_number_input = input("Enter customer phone number (format: ###-###-####): ")
print(validate_customer_info(phone_number_input, "phone number"))