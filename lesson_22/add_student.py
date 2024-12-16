from sqlalchemy.orm import sessionmaker
from create_bd import Student, Course, Rel, engine

Session = sessionmaker(bind=engine)  # Створення сесії для взаємодії з базою даних
session = Session()

def add_student(first_name, last_name, email):  # Додаємо нового студента
    new_student = Student(first_name=first_name, last_name=last_name, email=email)
    session.add(new_student)
    session.commit()
    return new_student

def enroll_student_in_course(student_id, course_id):  # Додавання студента до курсу
    student = session.query(Student).filter_by(student_id=student_id).first()
    course = session.query(Course).filter_by(course_id=course_id).first()
    if student and course:
        student.courses.append(course)
        session.commit()
        print(f"Студент {student.first_name} доданий до курсу {course.course_name}.")
    else:
        print("Немає такого студента або курсу.")


new_student = add_student('Alex', 'LL', 'alex.ll@test.com') # Приклад додавання студента
enroll_student_in_course(new_student.student_id, 2)  # на курс з id 2
