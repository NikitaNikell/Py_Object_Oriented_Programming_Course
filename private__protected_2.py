class Money:

    def __init__(self, money):
        if type(money) is int:
            self.__money = money

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        if self.__check_money(mn):
            self.__money += mn.__money

    def __check_money(self, money):
        if type(money) is int and money >= 0 or isinstance(money, Money):
            return True
        else:
            return False




mn_1 = Money(10)
mn_2 = Money(20)
assert mn_1._Money__money == 10 and mn_2._Money__money == 20, "неверные значения в локальном приватном атрибуте __money"

mn_1.set_money(100)
mn_2.add_money(mn_1)

assert mn_1.get_money() == 100 and mn_2.get_money() == 120, "неверное количество средств: возможно некорректая работа методов set_money и/или add_money"

mn_1.set_money(-1)
print(mn_1.get_money())

assert mn_1.get_money() == 100, "неверное количество средств: некорректная работа метода set_money"
m2 = mn_2.get_money()    # 120

print(mn_1)
print(mn_2)
