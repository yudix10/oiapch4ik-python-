import math

class Sphere:
    # Конструктор с разным числом аргументов
    def __init__(self, *args):
        if len(args) == 0:
            # Радиус 1, центр в начале координат
            self.radius = 1.0
            self.x = 0.0
            self.y = 0.0
            self.z = 0.0
        elif len(args) == 1:
            # Передан только радиус
            self.radius = float(args[0])
            self.x = 0.0
            self.y = 0.0
            self.z = 0.0
        elif len(args) == 4:
            # Радиус и координаты центра
            self.radius = float(args[0])
            self.x = float(args[1])
            self.y = float(args[2])
            self.z = float(args[3])
        else:
            raise ValueError("Неверное количество аргументов")

    # Объем сферы
    def get_volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

    # Площадь поверхности сферы
    def get_square(self):
        return 4 * math.pi * self.radius ** 2

    # Получить радиус
    def get_radius(self):
        return self.radius

    # Получить центр
    def get_center(self):
        return (self.x, self.y, self.z)

    # Изменить радиус
    def set_radius(self, r):
        self.radius = float(r)

    # Изменить центр
    def set_center(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    # Проверка, находится ли точка внутри сферы
    def is_point_inside(self, x, y, z):
        distance_squared = (x - self.x) ** 2 + (y - self.y) ** 2 + (z - self.z) ** 2
        return distance_squared <= self.radius ** 2

s0 = Sphere(0.5)  # test sphere creation with radius and default center
print(s0.get_center())  # (0.0, 0.0, 0.0)
print(s0.get_volume())  # 0.523598775598
print(s0.is_point_inside(0, -1.5, 0))  # False

s0.set_radius(1.6)
print(s0.is_point_inside(0, -1.5, 0)) # True
print(s0.get_radius()) # 1.6
