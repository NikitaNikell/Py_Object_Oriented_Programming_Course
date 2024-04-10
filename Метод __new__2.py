class Square:
    def __new__(cls, w, h):
        cls.area = lambda self: self.width * self.height # cоздание метода
        cls.perimeter = lambda self: 2 * (self.width + self.height) # cоздание метода

       #setattr(cls, 'perimeter', lambda self: 2 * (self.width + self.height)) аналог создания метода
        instance = super().__new__(cls)
        return instance

    def __init__(self, w, h):
        self.width = w
        self.height = h


s = Square(3, 4)
print(s)
print(s.area())
print(s.perimeter())