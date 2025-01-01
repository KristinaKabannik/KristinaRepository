from create_bd import Student
from add_student import session, new_student


def delete_student(student_id: object) -> object:  # Видаляємо студента з бази даних
    student = session.query(Student).filter_by(student_id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Студента {student.first_name} {student.last_name} видалено.")
    else:
        print("Студента не знайдено.")
        
delete_student(new_student.student_id)
