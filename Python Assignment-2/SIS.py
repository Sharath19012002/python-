import mysql.connector
from datetime import datetime
from exceptions import CourseNotFoundException, StudentNotFoundException, DuplicateEnrollmentException, \
    TeacherNotFoundException, PaymentValidationException, InsufficientFundsException


class SIS:
    def __init__(self):
        self.conn = mysql.connector.connect(user='root', password='root', host='localhost', database='sisdb')
        self.cursor = self.conn.cursor()

    def enroll_student_in_course(self, student_id, course_id):
        # Check if the course exists
        query = "SELECT * FROM Courses WHERE course_id=%s"
        self.cursor.execute(query, (course_id,))
        if not self.cursor.fetchone():
            raise CourseNotFoundException(course_id)

        # Check if the student exists
        query = "SELECT * FROM Students WHERE student_id=%s"
        self.cursor.execute(query, (student_id,))
        if not self.cursor.fetchone():
            raise StudentNotFoundException(student_id)

    def assign_teacher_to_course(self, teacher_id, course_id):
        # Assign a teacher to a course
        query = "UPDATE Courses SET teacher_id=%s WHERE course_id=%s"
        values = (teacher_id, course_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def record_payment(self, student_id, amount):
        # Record a payment made by a student
        payment_date = datetime.now().date()
        query = "INSERT INTO Payments (student_id, amount, payment_date) VALUES (%s, %s, %s)"
        values = (student_id, amount, payment_date)
        self.cursor.execute(query, values)
        self.conn.commit()

    def generate_enrollment_report(self, course_id):
        # Generate a report of students enrolled in a specific course
        query = "SELECT * FROM Students JOIN Enrollments ON Students.student_id = Enrollments.student_id WHERE course_id=%s"
        self.cursor.execute(query, (course_id,))
        report = self.cursor.fetchall()
        return report

    def generate_payment_report(self, student_id):
        # Generate a report of payments made by a specific student
        query = "SELECT * FROM Payments WHERE student_id=%s"
        self.cursor.execute(query, (student_id,))
        report = self.cursor.fetchall()
        return report

    def calculate_course_statistics(self, course_id):
        # Calculate statistics for a specific course
        query_enrollments = "SELECT COUNT(*) FROM Enrollments WHERE course_id=%s"
        query_payments = "SELECT SUM(amount) FROM Payments JOIN Enrollments ON Payments.student_id = Enrollments.student_id WHERE course_id=%s"
        self.cursor.execute(query_enrollments, (course_id,))
        num_enrollments = self.cursor.fetchone()[0]
        self.cursor.execute(query_payments, (course_id,))
        total_payments = self.cursor.fetchone()[0]
        return num_enrollments, total_payments

    # Method to add an enrollment to both the Student's and Course's enrollment lists
    def add_enrollment(self, student, course, enrollment_date):
        # Check if the student and course exist
        query_student = "SELECT * FROM Students WHERE student_id=%s"
        query_course = "SELECT * FROM Courses WHERE course_id=%s"
        self.cursor.execute(query_student, (student.student_id,))
        student_data = self.cursor.fetchone()
        self.cursor.execute(query_course, (course.course_id,))
        course_data = self.cursor.fetchone()

        if not student_data:
            raise StudentNotFoundException(student.student_id)
        if not course_data:
            raise CourseNotFoundException(course.course_id)

        # Check if the student is already enrolled in the course
        query_duplicate_enrollment = "SELECT * FROM Enrollments WHERE student_id=%s AND course_id=%s"
        self.cursor.execute(query_duplicate_enrollment, (student.student_id, course.course_id))
        if self.cursor.fetchone():
            raise DuplicateEnrollmentException(student.student_id, course.course_id)

        # Add enrollment to both the Student's and Course's enrollment lists
        query_add_enrollment = "INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES (%s, %s, %s)"
        values = (student.student_id, course.course_id, enrollment_date)
        self.cursor.execute(query_add_enrollment, values)
        self.conn.commit()

    def assign_course_to_teacher(self, course, teacher):
        # Check if the course and teacher exist
        query_course = "SELECT * FROM Courses WHERE course_id=%s"
        query_teacher = "SELECT * FROM Teacher WHERE teacher_id=%s"
        self.cursor.execute(query_course, (course.course_id,))
        course_data = self.cursor.fetchone()
        self.cursor.execute(query_teacher, (teacher.teacher_id,))
        teacher_data = self.cursor.fetchone()

        if not course_data:
            raise CourseNotFoundException(course.course_id)
        if not teacher_data:
            raise TeacherNotFoundException(teacher.teacher_id)

        # Assign the course to the teacher
        query_assign_course = "UPDATE Courses SET teacher_id=%s WHERE course_id=%s"
        values = (teacher.teacher_id, course.course_id)
        self.cursor.execute(query_assign_course, values)
        self.conn.commit()

    def add_payment(self, student, amount, payment_date):
        # Check if the student exists
        query_student = "SELECT * FROM Students WHERE student_id=%s"
        self.cursor.execute(query_student, (student.student_id,))
        student_data = self.cursor.fetchone()

        if not student_data:
            raise StudentNotFoundException(student.student_id)

        # Validate payment amount
        if amount <= 0:
            raise PaymentValidationException("Invalid payment amount")

        # Check if the student has enough funds
        query_enrollments = "SELECT COUNT(*) FROM Enrollments WHERE student_id=%s"
        self.cursor.execute(query_enrollments, (student.student_id,))
        num_enrollments = self.cursor.fetchone()[0]

        if amount > num_enrollments * 100:  # Assuming each enrollment costs 100 units
            raise InsufficientFundsException(student.student_id, "Unable to make payment. Insufficient funds.")

        # Add payment to the Student's payment history
        query_add_payment = "INSERT INTO Payments (student_id, amount, payment_date) VALUES (%s, %s, %s)"
        values = (student.student_id, amount, payment_date)
        self.cursor.execute(query_add_payment, values)
        self.conn.commit()

    # Method to retrieve all enrollments for a specific student
    def get_enrollments_for_student(self, student):
        # Check if the student exists
        query_student = "SELECT * FROM Students WHERE student_id=%s"
        self.cursor.execute(query_student, (student.student_id,))
        student_data = self.cursor.fetchone()

        if not student_data:
            raise StudentNotFoundException(student.student_id)

        # Retrieve all enrollments for the student
        query_enrollments = "SELECT * FROM Enrollments WHERE student_id=%s"
        self.cursor.execute(query_enrollments, (student.student_id,))
        enrollments = self.cursor.fetchall()
        return enrollments

    # Method to retrieve all courses assigned to a specific teacher
    def get_courses_for_teacher(self, teacher):
        # Check if the teacher exists
        query_teacher = "SELECT * FROM Teacher WHERE teacher_id=%s"
        self.cursor.execute(query_teacher, (teacher.teacher_id,))
        teacher_data = self.cursor.fetchone()

        if not teacher_data:
            raise TeacherNotFoundException(teacher.teacher_id)

        # Retrieve all courses assigned to the teacher
        query_courses = "SELECT * FROM Courses WHERE teacher_id=%s"
        self.cursor.execute(query_courses, (teacher.teacher_id,))
        courses = self.cursor.fetchall()
        return courses