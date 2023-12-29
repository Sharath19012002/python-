import mysql.connector
from mysql.connector import Error


class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
            try:
                DBConnection.connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='root',
                    database='couriermanagementsystem'
                )
                if DBConnection.connection.is_connected():
                    print("Connected to the database")

            except mysql.connector.Error as e:
                print(f"Error: {e}")

        return DBConnection.connection


class CourierServiceDb:
    connection = DBConnection.getConnection()

    def insertOrder(courierId, senderName, senderAddress, receiverName, receiverAddress, weight, status, trackingNumber,
                    deliveryDate):
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "INSERT INTO Couriers (courierID,SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate) " \
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (courierId, senderName, senderAddress, receiverName, receiverAddress,
                    weight, status, trackingNumber, deliveryDate)

            cursor.execute(query, data)
            CourierServiceDb.connection.commit()
            print("Order inserted successfully.")

        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def updateCourierStatus(trackingNumber, newStatus):
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "UPDATE Couriers SET Status = %s WHERE TrackingNumber = %s"
            data = (newStatus, trackingNumber)

            cursor.execute(query, data)
            CourierServiceDb.connection.commit()
            print("Courier status updated successfully.")

        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def getDeliveryHistory(trackingNumber):
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "SELECT * FROM Couriers WHERE TrackingNumber = %s"
            data = (trackingNumber,)

            cursor.execute(query, data)
            result = cursor.fetchall()
            return result

        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()


# Insert Order
CourierServiceDb.insertOrder(10, 'sharath', 'green park colony', 'tejas', 'hyderabad', 5, 'delivered', 'TS987656', '2023-04-05')
print('\ninserted')

# Update Courier Status
CourierServiceDb.updateCourierStatus('TS789002', newStatus="In transit")
print('\n\nupdated')

# Get Delivery History
delivery_history = CourierServiceDb.getDeliveryHistory('TN789002')
print("\n\nDelivery History:", delivery_history)