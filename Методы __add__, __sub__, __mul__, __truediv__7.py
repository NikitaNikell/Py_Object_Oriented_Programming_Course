class Box3D:

    def __init__(self, width: (int, float), height: (int, float), depth: (int, float)):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other):
        return Box3D(self.width + other.width, self.height + other.height, self.depth + other.depth)

    def __mul__(self, other):
        return Box3D(self.width * other, self.height * other, self.depth * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        if isinstance(other, Box3D):
            return Box3D(self.width - other.width, self.height - other.height, self.depth - other.depth)

    def __floordiv__(self, other):
        return Box3D(self.width // other, self.height // other, self.depth // other)

    def __mod__(self, other):
        return Box3D(self.width % other, self.height % other, self.depth % other)


# TEST-TASK___________________________________
box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)
assert hasattr(box1, "depth") and hasattr(box1, "height") and hasattr(box1, "width"), "ошибка в атрибутах"

box = box1 + box2  # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
assert box.depth == 9 and box.height == 6 and box.width == 3, "ошибка при операции Box3D(1, 2, 3) + Box3D(2, 4, 6)"

box1 = Box3D(1, 2, 3)
box = box1 * 2  # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)

assert box.depth == 6 and box.height == 4 and box.width == 2, \
    "ошибка при операции box1 * 2 (каждая размерность умножается на 2)"

box = 3 * box2  # Box3D: width=6, height=12, depth=18
assert box.depth == 18 and box.height == 12 and box.width == 6, "ошибка при операции 3 * box2"

box = box2 - box1  # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
assert box.depth == 3 and box.height == 2 and box.width == 1, "ошибка при операции box2 - box1"

box = box1 // 2  # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
assert box.depth == 1 and box.height == 1 and box.width == 0, "ошибка при операции box1 // 2"

box = box2 % 3  # Box3D: width=2, height=1, depth=0
assert box.depth == 0 and box.height == 1 and box.width == 2, "ошибка при операции box2 % 3"

print("Правильный ответ ).")





