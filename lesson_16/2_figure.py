from abc import ABC, abstractmethod
import math

class Figure(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Square(Figure): # в класі Square наслідування від класу Figure

    def __init__(self, side_length):
        self.__side_length = side_length

    def get_area(self):
        return self.__side_length ** 2

    def get_perimeter(self):
        return 4 * self.__side_length


class Rectangle(Figure):  # клас Rectangle наслідувається від класу Figure

    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def get_area(self):
        return self.__side_a * self.__side_b

    def get_perimeter(self):
        return self.__side_a * 2 + self.__side_b * 2


class Circle(Figure):  # Клас Коло наслідується від Shape

    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.__radius


# Екземпляри класів і вивід результатів
square = Square(3)
print("Square:", "area:", square.get_area(), "perimeter:", square.get_perimeter())

rectangle = Rectangle(2, 4)
print("Rectangle:", "area:", rectangle.get_area(), "perimeter:", rectangle.get_perimeter())

circle = Circle(5)
print("Circle:", "area:", round(circle.get_area(), 2), "perimeter:", round(circle.get_perimeter(), 2))

