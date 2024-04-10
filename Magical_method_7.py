class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        """ отвечает за сравнение на равенство с помощью оператора ==
        можно инвертировать и использовать вместо метода __ne__(self, other) !=
        """
        print('__eq__ call')
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        """ отвечает за сравнение на меньше с помощью оператора <
        можно инвертировать и использовать вместо метода __gt__(self, other) >
        """
        print('__lt__ call')
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        """ отвечает за сравнение на меньше или равно с помощью оператора <=
        можно инвертировать и использовать вместо метода __ge__(self, other) >=
        """
        return self == other or self < other


r = Rectangle(4, 5)
d = Rectangle(2, 4)
w = Rectangle(4, 5)
print(r <= d)
print(r >= w)
print(r == w)
print(r != w)



class MyClass:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return isinstance(other, MyClass) and self.x == other.x

a = MyClass(1)
b = MyClass(1)

print(a == b) # True, потому что a и b являются экземплярами одного и того же класса и совпадают значения атрибута х