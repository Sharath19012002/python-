import mysql.connector
from exceptions import StudentNotFoundException,PaymentValidationException
class Payment:
    def __init__(self, payment_id, student_id, amount, payment_date):
        self.payment_id = payment_id
        self.student_id = student_id
        self.amount = amount
        self.payment_date = payment_date
        self.conn = mysql.connector.connect(user='root', password='root', host='localhost', database='sisdb')
        self.cursor = self.conn.cursor()

    def get_student(self):
        # Check if the student exists
        query = "SELECT * FROM Students WHERE student_id=%s"
        self.cursor.execute(query, (self.student_id,))
        if not self.cursor.fetchone():
            raise StudentNotFoundException(self.student_id)

        # Retrieve the student associated with the payment
        query = "SELECT * FROM Students WHERE student_id=%s"
        self.cursor.execute(query, (self.student_id,))
        result = self.cursor.fetchone()
        return result

    def get_payment_amount(self):
        # Validate payment amount
        if self.amount <= 0:
            raise PaymentValidationException("Invalid payment amount")

        # Retrieve the payment amount
        return self.amount

    def get_payment_date(self):
        # Retrieve the payment date
        return self.payment_date
