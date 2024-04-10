class Vector:

    def __init__(self, *args):
        self.coords = list(args)

    def __checker(self, v1, v2):
        if len(v1) != len(v2):
            raise ArithmeticError('размерности векторов не совпадают')

    def __add__(self, other):
        self.__checker(self.coords, other.coords)
        new_coordinates = [x + y for x, y in zip(self.coords, other.coords)]
        return Vector(*new_coordinates)

    def __sub__(self, other):
        self.__checker(self.coords, other.coords)
        new_coordinates = [x - y for x, y in zip(self.coords, other.coords)]
        return Vector(*new_coordinates)

    def __mul__(self, other):
        self.__checker(self.coords, other.coords)
        new_coordinates = [x * y for x, y in zip(self.coords, other.coords)]
        return Vector(*new_coordinates)

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.coords = list(a + b for a, b in zip(self.coords, other.coords))
            return self
        self.coords = list(a + other for a in self.coords)
        return self

    def __isub__(self, other):
        if isinstance(other, Vector):
            self.coords = list(a - b for a, b in zip(self.coords, other.coords))
            return self
        self.coords = list(a - other for a in self.coords)
        return self

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return self.coords != other.coords


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True


