import mysql.connector
class TechShop:
    def __init__(self,host,user, password, database):
        try:
            # Connect to the MySQL server
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='TechShop',
                port=3306
            )
            print("Database Connection Succesfull")
            # Create a cursor to execute SQL queries
            self.cursor = self.connection.cursor()

        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error: Access denied. Check your username and password.")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Error: Database does not exist.")
            else:
                print("Error:", err)

TechShop = TechShop( host='localhost',user='root', password='root', database='TechShop')