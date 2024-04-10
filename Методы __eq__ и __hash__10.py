class Integer:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance, self.name, value)


class Triangle:
    a = Integer()
    b = Integer()
    c = Integer()

    def __init__(self, a: (int, float), b: (int, float), c: (int, float)):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def __is_triangle(a, b, c):
        if a and b and c:
            return a < b + c and b < a + c and c < a + b
        return True

    def __setattr__(self, key, value):
        if (key == "a" and not self.__is_triangle(value, self.b, self.c)) or \
                (key == "b" and not self.__is_triangle(self.a, value, self.c)) or \
                (key == "c" and not self.__is_triangle(self.a, self.b, value)):
            raise ValueError("с указанными длинами нельзя образовать треугольник")

        super().__setattr__(key, value)

    def __len__(self):
        return int(self.a + self.b + self.c) if self.a and self.b and self.c else None

    def __call__(self):
        if not (self.a, self.b, self.c):
            return
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"
print('GOOD')