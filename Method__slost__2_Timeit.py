from timeit import timeit

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def test_time_point():
    p1 = Point(3, 4)
    p1.x = 100
    p1.x
    del p1.x


def test_time_pointslots():
    p1 = PointSlots(3, 4)
    p1.x = 100
    p1.x
    del p1.x


print('No __slots__ stopped:', timeit(test_time_point))
print('__slots__ stopped:', timeit(test_time_pointslots))
