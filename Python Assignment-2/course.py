import mysql.connector
from datetime import datetime
from exceptions import TeacherNotFoundException,InvalidCourseDataException

class Course:
    def __init__(self, course_id, course_name, credits, teacher_id):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.teacher_id = teacher_id
        self.conn = mysql.connector.connect(user='root', password='root', host='localhost', database='sisdb')
        self.cursor = self.conn.cursor()

    def assign_teacher(self, teacher_id):
        # Check if the teacher exists
        query = "SELECT * FROM Teacher WHERE teacher_id=%s"
        self.cursor.execute(query, (teacher_id,))
        if not self.cursor.fetchone():
            raise TeacherNotFoundException(teacher_id)

        # Assign a teacher to the course
        query = "UPDATE Courses SET teacher_id=%s WHERE course_id=%s"
        values = (teacher_id, self.course_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def update_course_info(self, course_name, credits):
        if not course_name or not credits:
            raise InvalidCourseDataException("Invalid course data")

        # Update course information
        query = "UPDATE Courses SET course_name=%s, credits=%s WHERE course_id=%s"
        values = (course_name, credits, self.course_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def display_course_info(self):
        # Display detailed information about the course
        query = "SELECT * FROM Courses WHERE course_id=%s"
        self.cursor.execute(query, (self.course_id,))
        result = self.cursor.fetchone()
        print("Course Information:")
        print("Course ID:", result[0])
        print("Course Name:", result[1])
        print("Credits:", result[2])
        print("Teacher ID:", result[3])

    def get_enrollments(self):
        # Retrieve a list of student enrollments for the course
        query = "SELECT Students.student_id, first_name, last_name FROM Students JOIN Enrollments ON Students.student_id = Enrollments.student_id WHERE course_id=%s"
        self.cursor.execute(query, (self.course_id,))
        enrollments = self.cursor.fetchall()
        return enrollments

    def get_teacher(self):
        # Retrieve the assigned teacher for the course
        query = "SELECT * FROM Teacher WHERE teacher_id=%s"
        self.cursor.execute(query, (self.teacher_id,))
        result = self.cursor.fetchone()
        return result