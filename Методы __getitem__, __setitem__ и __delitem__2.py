class Track:

    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.points = []

    def add_point(self, x, y, speed):
        self.points.append([(x, y), speed])

    def __checker(self, inx):
        if type(inx) != int or inx > len(self.points):
            raise IndexError('некорректный индекс')

    def __getitem__(self, item):
        self.__checker(item)
        return self.points[item]


    def __setitem__(self, key, value):
        self.__checker(key)
        self.points[key][1] = value


tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2


tr[2] = 60
c, s = tr[2]
print(c, s)