import mysql.connector

class Enrollment:
    def __init__(self, enrollment_id, student_id, course_id, enrollment_date):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date
        self.conn = mysql.connector.connect(user='root', password='root', host='localhost', database='sisdb')
        self.cursor = self.conn.cursor()

    def get_student(self):
        # Retrieve the student associated with the enrollment
        query = "SELECT * FROM Students WHERE student_id=%s"
        self.cursor.execute(query, (self.student_id,))
        result = self.cursor.fetchone()
        return result

    def get_course(self):
        # Retrieve the course associated with the enrollment
        query = "SELECT * FROM Courses WHERE course_id=%s"
        self.cursor.execute(query, (self.course_id,))
        result = self.cursor.fetchone()
        return result