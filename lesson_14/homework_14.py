class Student:
    def __init__(self, first_name, last_name, age, average_score):    # конструктор, magic method
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_score = average_score

    def modify_average_score(self, new_score):      #метод класу
        self.average_score = new_score

    def student_info(self):                         #метод класу
        return f"Ім'я: {self.first_name}, Прізвище: {self.last_name}, Вік: {self.age}, Середній бал: {self.average_score}"


student = Student("John", "Doe", 18, 70)    #екземпляр класу
print(student.student_info())

student.modify_average_score(75)  # Змінюємо середній бал
print(student.student_info())
