class Quadrilateral:

    def __init__(self, width = None, height = None):
        if not height:
            self.width = width
            self.height = width
        else:
            self.width = width
            self.height = height

    def __str__(self):
        if self.__bool__():
            return f"Квадрат размером {self.width}х{self.height}"

        return f"Прямоугольник размером {self.width}х{self.height}"

    def __bool__(self):
        return self.height == self.width


q1 = Quadrilateral(10)
print(q1)
assert q1.height == 10
assert q1.width == 10
assert bool(q1) is True
assert q1.__str__() == "Квадрат размером 10х10"
assert isinstance(q1, Quadrilateral)

q2 = Quadrilateral(3, 5)
print(q2)
assert q2.__str__() == "Прямоугольник размером 3х5"
assert bool(q2) is not True
assert isinstance(q2, Quadrilateral)

q3 = Quadrilateral(4, 7)
print(q3)
assert bool(q3) is False
assert q3.__str__() == "Прямоугольник размером 4х7"
assert isinstance(q3, Quadrilateral)