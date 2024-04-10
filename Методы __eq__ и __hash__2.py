class PathLine:
    def __init__(self, dist, angle):
        self.dist = dist
        self.angle = angle

    def __eq__(self, other):
        return abs(self.dist) == abs(other.dist)


p1 = PathLine(10, 1.57)
p2 = PathLine(-10, 0.49)

h1, h2 = hash(p1), hash(p2) # будет ошибка, что объекты p1 и p2 не хешируемые, для корректной работы нужно определить def __hash__