from add_student import session
from create_bd import Student


def update_student(student_id, first_name=None, last_name=None, email=None): # Оновлюємо дані студента
    student = session.query(Student).filter_by(student_id=student_id).first()
    if student:
        if first_name:
            student.first_name = first_name
        if last_name:
            student.last_name = last_name
        if email:
            student.email = email
        session.commit()
        print(f"Дані студента {student_id} оновлені.")
    else:
        print("Такого студента не існує.")
