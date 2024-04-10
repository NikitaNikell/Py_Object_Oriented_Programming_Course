class Rectangle:
    __slots__ = '__width', 'height'

    def __init__(self, a, b):
        self.width = a
        self.height = b

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        print('setter called')
        self.__width = value


class Square(Rectangle):
    __slots__ = 'color',

    def __init__(self, a, color):
        super().__init__(a, a)
        self.color = color


s = Square(4, 'black')
print(s.height, s.width, s.color)
s.width = 5
s.color = 'white'
print(s.height, s.width, s.color)