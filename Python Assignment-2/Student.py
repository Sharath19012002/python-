import mysql.connector
from datetime import datetime
from exceptions import DuplicateEnrollmentException,PaymentValidationException

class Student:
    def __init__(self, student_id, first_name, last_name, date_of_birth, email, phone_number):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        self.conn = mysql.connector.connect(user='root', password='root', host='localhost', database='sisdb')
        self.cursor = self.conn.cursor()

    def enroll_in_course(self, course_id):
        # Check if the student is already enrolled in the course
        query = "SELECT * FROM Enrollments WHERE student_id=%s AND course_id=%s"
        self.cursor.execute(query, (self.student_id, course_id))
        if self.cursor.fetchone():
            raise DuplicateEnrollmentException(self.student_id, course_id)

        # Enroll the student in a course
        enrollment_date = datetime.now().date()
        query = "INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES (%s, %s, %s)"
        values = (self.student_id, course_id, enrollment_date)
        self.cursor.execute(query, values)
        self.conn.commit()

    def update_student_info(self, first_name, last_name, date_of_birth, email, phone_number):
        # Update student information

        query = "UPDATE Students SET first_name=%s, last_name=%s, date_of_birth=%s, email=%s, phone_number=%s WHERE student_id=%s"
        values = (first_name, last_name, date_of_birth, email, phone_number, self.student_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def make_payment(self, amount):
        # Record a payment made by the student
        if amount <= 0:
            raise PaymentValidationException("Invalid payment amount")

        # Record a payment made by the student
        payment_date = datetime.now().date()
        query = "INSERT INTO Payments (student_id, amount, payment_date) VALUES (%s, %s, %s)"
        values = (self.student_id, amount, payment_date)
        self.cursor.execute(query, values)
        self.conn.commit()

    def display_student_info(self):
        # Display detailed information about the student
        query = "SELECT * FROM Students WHERE student_id=%s"
        self.cursor.execute(query, (self.student_id,))
        result = self.cursor.fetchone()
        print("Student Information:")
        print("Student ID:", result[0])
        print("First Name:", result[1])
        print("Last Name:", result[2])
        print("Date of Birth:", result[3])
        print("Email:", result[4])
        print("Phone Number:", result[5])

    def get_enrolled_courses(self):
        # Retrieve a list of courses in which the student is enrolled
        query = "SELECT Courses.course_id, course_name FROM Courses JOIN Enrollments ON Courses.course_id = Enrollments.course_id WHERE student_id=%s"
        self.cursor.execute(query, (self.student_id,))
        courses = self.cursor.fetchall()
        return courses

    def get_payment_history(self):
        # Retrieve a list of payment records for the student
        query = "SELECT * FROM Payments WHERE student_id=%s"
        self.cursor.execute(query, (self.student_id,))
        payments = self.cursor.fetchall()
        return payments

#sis = Student(1,"John","Doe",datetime(1995, 8, 15),"john.doe@example.com", "123-456-7890")

#sis.enroll_in_course()

# Enroll John in the specified courses
courses_to_enroll = ["Introduction to Programming", "Mathematics 101"]

# Perform student enrollment





