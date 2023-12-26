from datetime import datetime
from Student import Student
from course import Course
from Teacher import Teacher
from Enrollment import Enrollment
from Payment import Payment
from SIS import SIS


def main():
    try:
        # Create instances of SIS, Student, Course, and Teacher
        sis = SIS()
        student = Student(1, 'sharath', 'Doe', datetime(2000, 1, 1), 'john.doe@example.com', '123-456-7890')
        course = Course(101, 'Computer Science', 'CS101', None)
        teacher = Teacher(1, 'Professor', 'Smith', 'new.email@example.com')

        # Test methods related to the Student class
        # student.enroll_in_course(course.course_id)  # Method belongs to the Student class
        student.update_student_info('John', 'Doe', datetime(2000, 1, 1), 'john.doe@example.com',
                                    '987-654-3210')  # Method belongs to the Student class
        student.make_payment(100)  # Method belongs to the Student class
        student.display_student_info()  # Method belongs to the Student class
        enrollments = student.get_enrolled_courses()  # Method belongs to the Student class
        payments = student.get_payment_history()  # Method belongs to the Student class

        # Test methods related to the Course class
        course.assign_teacher(teacher.teacher_id)  # Method belongs to the Course class
        course.update_course_info('Introduction to Computer Science', 4)  # Method belongs to the Course class
        course.display_course_info()  # Method belongs to the Course class
        course_enrollments = course.get_enrollments()  # Method belongs to the Course class
        assigned_teacher = course.get_teacher()  # Method belongs to the Course class

        # Test methods related to the SIS class
        sis.enroll_student_in_course(student.student_id, course.course_id)  # Method belongs to the SIS class
        sis.assign_teacher_to_course(teacher.teacher_id, course.course_id)  # Method belongs to the SIS class
        sis.record_payment(student.student_id, 150)  # Method belongs to the SIS class
        enrollment_report = sis.generate_enrollment_report(course.course_id)  # Method belongs to the SIS class
        payment_report = sis.generate_payment_report(student.student_id)  # Method belongs to the SIS class
        course_statistics = sis.calculate_course_statistics(course.course_id)  # Method belongs to the SIS class

        # Display results
        print("\nTest Results:")
        student.display_student_info()
        course.display_course_info()
        teacher.display_teacher_info()
        print("\nEnrollments:")
        for enrollment in enrollments:
            print(enrollment)
        print("\nPayments:")
        for payment in payments:
            print(payment)
        print("\nCourse Enrollments:")
        for course_enrollment in course_enrollments:
            print(course_enrollment)
        print("\nAssigned Teacher:")
        print(assigned_teacher)
        print("\nEnrollment Report:")
        print(enrollment_report)
        print("\nPayment Report:")
        print(payment_report)
        print("\nCourse Statistics:")
        print(course_statistics)

    except Exception as e:
        print(f"Error: {str(e)}")

    finally:
        # Close database connection
        sis.conn.close()


if __name__ == "__main__":
    main()
