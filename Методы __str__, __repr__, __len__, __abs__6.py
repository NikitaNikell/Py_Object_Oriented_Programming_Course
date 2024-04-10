
class RadiusVector:

    def __init__(self, arg, *args):
        if len(args) == 0:
            self.__coords = [0 for i in range(arg)]
        else:
            self.__coords = [arg] + list(args)

    def set_coords(self, *args):
        n = min(len(args), len(self.__coords))
        self.__coords[:n] = args[:n]

    def get_coords(self):
        return tuple(self.__coords)

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return sum(map(lambda x: x * x, self.__coords)) ** 0.5

# TEST-TASK___________________________________
from math import sqrt

vector3D = RadiusVector(3)

k = str(*[_ for _ in vector3D.__dict__.keys()])
assert len(vector3D.__dict__[k]) == 3, "ошибка в длине списка из значений"
assert all(True if _ == 0 else False for _ in vector3D.__dict__[k]), "ошибка, значения должны быть нулями"

vector3D.set_coords(3, -5.6, 8)
k = str(*[_ for _ in vector3D.__dict__.keys()])
assert len(vector3D.__dict__[k]) == 3 and \
       (vector3D.__dict__[k] == [3, -5.6, 8] or
        vector3D.__dict__[k] == (3, -5.6, 8)), "значения координат неправильные"

assert hasattr(vector3D, 'set_coords') and callable(vector3D.set_coords), "метод set_coords не найден"
assert hasattr(vector3D, 'get_coords') and callable(vector3D.get_coords), "метод get_coords не найден"

assert vector3D.get_coords() == (3, -5.6, 8), "не правильные значения в кортеже"
assert type(vector3D.get_coords()) == tuple, "метод get_coords должен был вернуть кортеж"

vector3D = RadiusVector(3)
vector3D.set_coords(1, 1.1, -8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
assert len(vector3D.__dict__[k]) == 3 and \
       (vector3D.__dict__[k] == [1, 1.1, -8] or
        vector3D.__dict__[k] == (1, 1.1, -8)), "метод set_coords работает не верно"

vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
assert vector3D.__dict__[k] == [1, 2, -8] or vector3D.__dict__[k] == (1, 2, -8), \
    "метод set_coords изменил не те значения"

res_len = len(vector3D)  # res_len = 3
assert len(vector3D) == 3, "неправильно работает метод len()"

assert abs(vector3D) == sqrt(sum([i * i for i in vector3D.__dict__[k]])), "метод abs() вернул неверное значение"
print("Правильное решение !")