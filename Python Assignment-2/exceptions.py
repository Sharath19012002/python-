class DuplicateEnrollmentException(Exception):
    def __init__(self, student_id, course_id):
        super().__init__(f"Student {student_id} is already enrolled in Course {course_id}")

class CourseNotFoundException(Exception):
    def __init__(self, course_id):
        super().__init__(f"Course {course_id} not found in the system")

class StudentNotFoundException(Exception):
    def __init__(self, student_id):
        super().__init__(f"Student {student_id} not found in the system")

class TeacherNotFoundException(Exception):
    def __init__(self, teacher_id):
        super().__init__(f"Teacher {teacher_id} not found in the system")

class PaymentValidationException(Exception):
    def __init__(self, message="Payment validation failed"):
        super().__init__(message)

class InvalidStudentDataException(Exception):
    def __init__(self, message="Invalid student data"):
        super().__init__(message)

class InvalidCourseDataException(Exception):
    def __init__(self, message="Invalid course data"):
        super().__init__(message)

class InvalidEnrollmentDataException(Exception):
    def __init__(self, message="Invalid enrollment data"):
        super().__init__(message)

class InvalidTeacherDataException(Exception):
    def __init__(self, message="Invalid teacher data"):
        super().__init__(message)

class InsufficientFundsException(Exception):
    def __init__(self, student_id, course_id):
        super().__init__(f"Student {student_id} does not have sufficient funds to enroll in Course {course_id}")