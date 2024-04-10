# Исходник:
# class Circle:
#     PI = 3.14
#
#     def __init__(self, radius):
#         self._radius = radius
#         self._diameter = 2 * radius
#
#     def get_radius(self):
#         return self._radius
#
#     def get_diameter(self):
#         return self._diameter
#
#     def get_area(self):
#         return self.PI * self._radius ** 2
#
#     def get_perimeter(self):
#         return 2 * self.PI * self._radius
#
# """ Ваша задача переписать класс Circle таким образом, чтобы все атрибуты и методы определялись только в методе __new__ """

class Circle:
    PI = 3.14

    def __new__(cls, radius):
        instance = super().__new__(cls)
        instance._radius = radius
        instance._diameter = 2 * radius
        cls.get_radius = lambda x: instance._radius
        cls.get_diameter = lambda x: instance._diameter
        cls.get_area = lambda x: cls.PI * instance._radius ** 2
        cls.get_perimeter = lambda x: 2 * cls.PI * instance._radius
        return instance


circle_instance = Circle(3.5)

print(f"Radius: {circle_instance.get_radius()}")
print(f"Diameter: {circle_instance.get_diameter()}")
print(f"Area: {circle_instance.get_area()}")
print(f"Perimeter: {circle_instance.get_perimeter()}")
