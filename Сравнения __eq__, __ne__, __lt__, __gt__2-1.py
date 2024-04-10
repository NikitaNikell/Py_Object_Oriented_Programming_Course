class DimensionsDescriptors: # дескриптор / дескрипторы

    def __set_name__(self, owner, name):
        self.name = '_' + owner.__name__ + '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__validate(instance, value):
            setattr(instance, self.name, value)

    @staticmethod
    def __validate(instance, value):
        return instance.MIN_DIMENSION <= value <= instance.MAX_DIMENSION


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000
    a = DimensionsDescriptors()
    b = DimensionsDescriptors()
    c = DimensionsDescriptors()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def volume(self):
        return self.a * self.b * self.c

    def __gt__(self, other):
        return self.volume > other.volume

    def __ge__(self, other):
        return self.volume >= other.volume

    def __repr__(self):
        return f"{self.volume}"


class ShopItem:

    def __init__(self, name: str, price: (int, float), dim: Dimensions):
        self.name = name
        self.price = price
        self.dim = dim
        self.dim_volume = self.dim.volume

    def __repr__(self):
        fields = [f'{f}={v}' for f, v in self.__dict__.items()]
        return f"{type(self).__name__}" + str(tuple(fields)).replace("\'", '')


lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
            ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
            ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
            ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))]

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim_volume)

print(lst_shop_sorted)