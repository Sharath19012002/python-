import mysql.connector
from mysql.connector import Error
import datetime
def initialize_database():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root'
        )

        cursor = connection.cursor()

        # Create the SIS database
        cursor.execute("CREATE DATABASE IF NOT EXISTS sisdb")
        cursor.execute("USE sisdb")

        # Create Students table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Students (
                student_id INT PRIMARY KEY,
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                date_of_birth DATE,
                email VARCHAR(255),
                phone_number VARCHAR(15)
            )
        """)

        # Create Courses table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Courses (
                course_id INT PRIMARY KEY,
                course_name VARCHAR(255),
                credits INT,
                teacher_id INT,
                FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
            )
        """)

        # Create Enrollments table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Enrollments (
                enrollment_id INT PRIMARY KEY,
                student_id INT,
                course_id INT,
                enrollment_date DATE,
                FOREIGN KEY (student_id) REFERENCES Students(student_id),
                FOREIGN KEY (course_id) REFERENCES Courses(course_id)
            )
        """)

        # Create Teacher table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Teacher (
                teacher_id INT PRIMARY KEY,
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                email VARCHAR(255)
            )
        """)

        # Create Payments table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Payments (
                payment_id INT PRIMARY KEY,
                student_id INT,
                amount DECIMAL(10, 2),
                payment_date DATE,
                FOREIGN KEY (student_id) REFERENCES Students(student_id)
            )
        """)

        # Commit changes and close cursor
        connection.commit()
        cursor.close()

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close database connection
        if connection.is_connected():
            connection.close()

def retrieve_data(table_name):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='SISDB'
        )

        cursor = connection.cursor()

        # Example: Retrieve all data from a specific table
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()

        return data

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def insert_data(query, values):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='SISDB'
        )

        cursor = connection.cursor()

        # Example: Insert data into a table
        cursor.execute(query, values)
        connection.commit()

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def update_data(query, values):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='SISDB'
        )

        cursor = connection.cursor()

        # Example: Update data in a table
        cursor.execute(query, values)
        connection.commit()

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def manage_transaction(queries, values):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='SISDB'
        )

        cursor = connection.cursor()

        # Example: Transaction management
        connection.start_transaction()

        for i in range(len(queries)):
            cursor.execute(queries[i], values[i])

        connection.commit()

    except Error as e:
        print(f"Error: {e}")
        connection.rollback()

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def dynamic_query_builder(table_name, columns, conditions, sorting):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='SISDB'
        )

        cursor = connection.cursor()

        # Example: Dynamic query builder
        query = f"SELECT {', '.join(columns)} FROM {table_name}"

        if conditions:
            query += f" WHERE {' AND '.join(conditions)}"

        if sorting:
            query += f" ORDER BY {', '.join(sorting)}"

        cursor.execute(query)
        data = cursor.fetchall()

        return data

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


initialize_database()

# Retrieve data from Students table
students_data = retrieve_data("Students")
print("Students Data:")
print(students_data)

# Insert data into Students table
insert_query = "INSERT INTO Students (student_id, first_name, last_name, date_of_birth, email, phone_number) VALUES (%s, %s, %s, %s, %s, %s)"
insert_values = (1, 'John', 'Doe', datetime.datetime(2000, 1, 1), 'john.doe@example.com', '123-456-7890')
insert_data(insert_query, insert_values)

# Update data in Students table
update_query = "UPDATE Students SET phone_number = %s WHERE student_id = %s"
update_values = ('987-654-3210', 1)
update_data(update_query, update_values)

# Manage a transaction
transaction_queries = [
    "INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES (%s, %s, %s, %s)",
    "INSERT INTO Payments (payment_id, student_id, amount, payment_date) VALUES (%s, %s, %s, %s)"
]

transaction_values = [
    (1, 1, 1, datetime.date.today()),
    (1, 1, 50.00, datetime.date.today())
]
manage_transaction(transaction_queries, transaction_values)

# Dynamic query builder example
dynamic_query = dynamic_query_builder("Students", ["student_id", "first_name", "last_name"], ["first_name = 'John'"], ["last_name DESC"])
print("Dynamic Query Result:")
print(dynamic_query)
