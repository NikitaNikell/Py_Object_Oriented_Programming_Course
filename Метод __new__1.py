# Магический метод __new__ — это метод, который вызывается для фактического создания нового объекта как экземпляра желаемого класса.

class Point:
    def __new__(cls, *args, **kwargs):
        print('Point: Создание экземпляра')
        instance = object.__new__(cls)
        return instance

    def __init__(self, x, y):
        print('Point: Инициализация экземпляра')
        self.x = x
        self.y = y


class Point3D(Point):
    def __new__(cls, *args, **kwargs):
        print('Point3D: Создание экземпляра')
        instance = object.__new__(cls)
        return instance

    def __init__(self, x, y, z):
        print('Point3D: Инициализация экземпляра')
        super().__init__(x, y)
        self.z = z


p = Point3D(10, 20, 30)
print(p.__dict__)