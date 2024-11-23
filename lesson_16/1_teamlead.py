class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


def test_teamlead_check_attributes():
    teamlead = TeamLead("Alex", 130, "IT", "Python", 10)

    assert hasattr(teamlead, 'name'), "Помилка. Клас TeamLead має успадковувати атрибут 'name' від класу Employee"  # Перевірка, чи має об'єкт lead атрибут з назвою 'name'
    assert hasattr(teamlead, 'salary'), "Помилка. Клас TeamLead має успадковувати атрибут 'salary' від класу Employee"     # якщо ж немає такого атрибуту, то виведеться ерор
    assert hasattr(teamlead, 'department'), "Помилка. Клас TeamLead має успадковувати атрибут 'department' від класу Manager"
    assert hasattr(teamlead, 'programming_language'), "Помилка. Клас TeamLead має успадковувати атрибут 'programming_language' від класу Developer"
    assert hasattr(teamlead, 'team_size'), "Помилка. Клас TeamLead повинен мати атрибут 'team_size'"

    return "Атрибути з класу Manager та Developer наявні у класі TeamLead"

test_teamlead_check_attributes()
