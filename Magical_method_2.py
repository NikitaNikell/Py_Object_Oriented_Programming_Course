class Vector:

    def __init__(self, *args):
        self.values = sorted([i for i in args if isinstance(i, int) and not isinstance(i, bool)])


    def __str__(self):
        if len(self.values) == 0:
            return "Пустой вектор"
        else:
            return f"Вектор{tuple(self.values)}"

v1 = Vector(1, 2, 3)
assert isinstance(v1, Vector)
assert str(v1) == 'Вектор(1, 2, 3)'

v2 = Vector()
assert isinstance(v2, Vector)
assert str(v2) == 'Пустой вектор'

v3 = Vector([4, 5], 'hello', 3, -1.5, 1, 2)
assert isinstance(v3, Vector)
assert sorted(v3.values) == [1, 2, 3]
assert str(v3) == 'Вектор(1, 2, 3)'

v4 = Vector([4, 5], 'hello')
assert str(v2) == 'Пустой вектор'
assert v2.values == []

v5 = Vector(1, 2, True)
assert isinstance(v5, Vector)
assert str(v5) == 'Вектор(1, 2)'

print(v1)
print(v2)
print(v3)
print(v4)
