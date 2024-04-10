import sys


class ShopItem:

    def __init__(self, name: str, weight: (int, float), price: (int, float)):
        self.name = name
        self.weight = weight
        self.price = price

    def __eq__(self, other):
        if isinstance(other, ShopItem):
            return self.name == other.name and self.weight == other.weight and self.price == other.price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))


lst_in = list(map(str.strip, sys.stdin.readlines())) # END == Ctrl+D

shop_items = {}
for elem in lst_in:
    name, weight, price = elem.rsplit(maxsplit=2)
    obj = ShopItem(name, weight, price)
    shop_items.setdefault(obj, [obj, 0])[1] += 1

it1 = ShopItem('name', 10, 11)
it2 = ShopItem('name', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

it2 = ShopItem('name', 10, 12)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('name', 11, 11)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('NAME', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

name = lst_in[0].split(':')
for sp in shop_items.values():
    assert isinstance(sp[0], ShopItem) and type(sp[1]) == int, "в значениях словаря shop_items первый элемент должен быть объектом класса ShopItem, а второй - целым числом"

v = list(shop_items.values())
if v[0][0].name.strip() == "Системный блок":
    assert v[0][1] == 1 and v[1][1] == 2 and v[2][1] == 1 and len(v) == 3, "неверные значения в словаре shop_items"

if v[0][0].name.strip() == "X-box":
    assert v[0][1] == 2 and v[1][1] == 1 and v[2][1] == 2 and len(v) == 3, "неверные значения в словаре shop_items"


print("GOOD")