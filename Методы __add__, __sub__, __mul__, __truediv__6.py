class Item:

    def __init__(self, name: str, money: (int, float)):
        self.name = name
        self.money = money

    def __add__(self, other):
        if not isinstance(other, Item) and isinstance(other, (int, float)):
            raise AttributeError("Неправильный тип данных")
        self.money += other.money
        return self.money

    def __radd__(self, other):
        return other + self.money


class Budget:

    def __init__(self):
        self.items = []

    def add_item(self, it):
        if isinstance(it, Item):
            self.items.append(it)

    def remove_item(self, indx):
        if 0 <= indx < len(self.items):
            del self.items[indx]

    def get_items(self):
        return self.items


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))
assert len(my_budget.get_items()) == 4
my_budget.remove_item(1)
assert len(my_budget.get_items()) == 3
s = 0
for x in my_budget.get_items():
    s = s + x
assert s == 3500.1
# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
assert Item('a', 150) + Item('b', 111.11)  == 261.11