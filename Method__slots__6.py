class Good:
    __slots__ = ['_price']

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value * 2


obj = Good(5)
print(obj.price)
obj.price = 10
print(obj.price)