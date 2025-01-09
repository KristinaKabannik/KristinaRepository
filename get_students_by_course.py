from add_student import session
from create_bd import Student, Course, Rel

def get_students_by_course(course_id): # Отримуємо список студентів, зареєстрованих на певному курсі
    course = session.query(Course).filter_by(course_id=course_id).first()
    if course:
        print(f"Студенти, зареєстровані на курс {course.course_name}:")
        for student in course.students:
            print(f"{student.first_name} {student.last_name} - {student.email}")
    else:
        print("Курс не знайдено.")


get_students_by_course(2)
