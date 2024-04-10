class Ellipse:

    def __init__(self, *args):
        if args:
            self.x1, self.y1, self.x2, self.y2 = args

    def __bool__(self):
        return True if len(self.__dict__) == 4 else False

    def get_coords(self):
        if self.__bool__():
            return self.x1, self.y1, self.x2, self.y2
        else:
            raise AttributeError('нет координат для извлечения')


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]


#[print(i.get_coords()) for i in lst_geom if i.__bool__()]
[(i.get_coords()) for i in lst_geom if i.__bool__()]