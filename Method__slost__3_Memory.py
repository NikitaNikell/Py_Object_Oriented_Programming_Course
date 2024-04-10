class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


s = Point(3, 4)
print('No slots:', s.__sizeof__(), s.__dict__.__sizeof__()) # No slots: 32 88
d = PointSlots(3, 4)
print('Slots', d.__sizeof__()) # Slots 32

