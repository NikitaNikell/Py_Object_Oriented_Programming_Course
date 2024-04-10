class CentralBank:

    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None # запрет на создание копии экземпляра класса ЭК

    @classmethod
    def register(cls, money):
        money.cb = cls


class Money:
    type_money = None
    EPS = 0.1

    def __init__(self, volume=0):
        self.__volume = volume
        self.__cb = None

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, obj):
        self.__cb = obj

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, obj):
        self.__volume = obj

    def get_volumes(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")

        if self.type_money is None:
            raise ValueError("Неизвестен тип кошелька")

        result1 = self.volume / self.cb.rates[self.type_money]
        result2 = other.volume / other.cb.rates[other.type_money]
        return result1, result2

    def __eq__(self, other):
        if isinstance(other, Money):
            result1, result2 = self.get_volumes(other)

            return abs(result1 - result2) < self.EPS

    def __lt__(self, other):
        if isinstance(other, Money):
            result1, result2 = self.get_volumes(other)

            return result1 < result2

    def __le__(self, other):
        if isinstance(other, Money):
            result1, result2 = self.get_volumes(other)

            return result1 <= result2


class MoneyR(Money):
    type_money = 'rub'


class MoneyD(Money):
    type_money = 'dollar'


class MoneyE(Money):
    type_money = 'euro'


CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")
