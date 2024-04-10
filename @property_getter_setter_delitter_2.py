class WindowDlg:

    def __init__(self, title = "", width = 0, height = 0):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        return print(f'{self.__title}: {self.__width}, {self.__height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if 0 <= value <= 10000:
            self.__width = value
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if 0 <= value <= 10000:
            self.__height = value
            self.show()

wnd = WindowDlg('Окно', 10, 11)
assert '_WindowDlg__title' in wnd.__dict__ and '_WindowDlg__width' in wnd.__dict__ and '_WindowDlg__height' in wnd.__dict__, \
    "Атрибуты в экземпляре класса не совпадают, так же они должны быть защищёнными"

assert wnd._WindowDlg__title == 'Окно' and type(wnd._WindowDlg__title) is str, 'Название должно быть строкой'
assert 'width' in dir(wnd) and 'height' in dir(wnd), 'В классе должны быть методы для обращения к приватным атрибутам'

assert wnd.width == 10, 'Геттер для __width работает неправильно'
wnd.width = 11
assert wnd.width == 11, 'Сеттер для __width работает неправильно'

assert wnd.height == 11, 'Геттер для __height работает неправильно'
wnd.height = 22
assert wnd.height == 22, 'Сеттер для __height работает неправильно'

import io
import sys

output = io.StringIO()
sys.stdout = output
wnd.show()
sys.stdout = sys.__stdout__

assert output.getvalue().strip() == "Окно: 11, 22", 'Неправильный формат вывода в методе show'
