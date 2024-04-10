class Square:
    def __new__(cls, w, h):
        cls.area = lambda self: self.width * self.height

        setattr(cls, 'perimeter', lambda self: 2 * (self.width + self.height))
        instance = super().__new__(cls)
        instance.width = w
        instance.height = h
        return instance


s = Square(3, 4)
print(s.area())
print(s.perimeter())