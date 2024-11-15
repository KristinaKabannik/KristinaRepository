import math


class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a  # Довжина сторони а
        self.angle_a = angle_a  # Кут а між сторонами a i b

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Довжина сторони a має бути більше 0")
            super().__setattr__(name, value)

        elif name == "angle_a":
            if value <= 0 or value >= 180:
                raise ValueError("Кут повинен бути не менше 0 і не більше 180 градусів")
            super().__setattr__(name, value)

            super().__setattr__("angle_b", 180 - value)  # Знаходимо кут b

        else:
            super().__setattr__(name, value)

    def rhombus_info(self):
        return f"Сторона a: {self.side_a}, Кут a: {self.angle_a}°, Кут b: {self.angle_b}°"


rhombus = Rhombus(15, 75)    # екземпляр класу
print(rhombus.rhombus_info())
