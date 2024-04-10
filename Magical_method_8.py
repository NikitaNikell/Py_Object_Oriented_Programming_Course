from functools import total_ordering

@total_ordering
class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Fruit):
            return self.price == other.price
        if isinstance(other, float):
            return self.price == other

    def __lt__(self, other):
        if isinstance(other, Fruit):
            return self.price < other.price
        if isinstance(other, float):
            return self.price < other

apple = Fruit("Apple", 0.5)
orange = Fruit("Orange", 1)
banana = Fruit("Banana", 1.6)
lime = Fruit("Lime", 1.0)

assert (banana > 1.2) is True
assert (banana >= 1.2) is True
assert (banana == 1.2) is False
assert (banana != 1.2) is True
assert (banana < 1.2) is False
assert (banana <= 1.2) is False

assert (apple > orange) is False
assert (apple >= orange) is False
assert (apple == orange) is False
assert (apple != orange) is True
assert (apple < orange) is True
assert (apple <= orange) is True

assert (orange == lime) is True
assert (orange != lime) is False
assert (orange > lime) is False
assert (orange < lime) is False
assert (orange <= lime) is True
assert (orange >= lime) is True
print('Good')