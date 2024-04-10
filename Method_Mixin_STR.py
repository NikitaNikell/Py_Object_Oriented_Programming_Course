class ToStringMixin:
    """ Миксин для преобразования к строке """
    def __str__(self):
        return f"{self.__class__.__name__}({str(self.__dict__)})"

class MyClass(ToStringMixin):
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = MyClass(1, 2)
print(obj) # Output: MyClass({'x': 1, 'y': 2})
