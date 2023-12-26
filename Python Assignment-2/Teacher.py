import mysql.connector
from exceptions import InvalidTeacherDataException
class Teacher:
    def __init__(self, teacher_id, first_name, last_name, email):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.conn = mysql.connector.connect(user='root', password='root', host='localhost', database='sisdb')
        self.cursor = self.conn.cursor()

    def update_teacher_info(self, first_name, last_name, email):
        if not first_name or not last_name or not email:
            raise InvalidTeacherDataException("Invalid teacher data")

        # Update teacher information
        query = "UPDATE Teacher SET first_name=%s, last_name=%s, email=%s WHERE teacher_id=%s"
        values = (first_name, last_name, email, self.teacher_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def display_teacher_info(self):
        # Display detailed information about the teacher
        query = "SELECT * FROM Teacher WHERE teacher_id=%s"
        self.cursor.execute(query, (self.teacher_id,))
        result = self.cursor.fetchone()
        print("Teacher Information:")
        print("Teacher ID:", result[0])
        print("First Name:", result[1])
        print("Last Name:", result[2])
        print("Email:", result[3])

    def get_assigned_courses(self):
        # Retrieve a list of courses assigned to the teacher
        query = "SELECT Courses.course_id, course_name FROM Courses WHERE teacher_id=%s"
        self.cursor.execute(query, (self.teacher_id,))
        courses = self.cursor.fetchall()
        return courses