from timeit import timeit

# make data
# from random import choice, seed
# seed(12)
#
# keys = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg']
# prices = ["10 20", "20 30", "30 40", "50 60", "70 80", "90 10", "20 50"]
# data = "\n".join([": ".join(choice([*zip(keys, prices)])) for _ in range(100)])


data = "ddd: 50 60\nccc: 30 40\nfff: 90 10\neee: 70 80\nfff: 90 10\nccc: 30 40\nbbb: 20 30\nddd: 50 60\n" \
       "aaa: 10 20\nccc: 30 40\nddd: 50 60\nccc: 30 40\nfff: 90 10\nggg: 20 50\nddd: 50 60\nfff: 90 10\n" \
       "ggg: 20 50\neee: 70 80\nbbb: 20 30\neee: 70 80\naaa: 10 20\nfff: 90 10\neee: 70 80\nbbb: 20 30\n" \
       "ddd: 50 60\nccc: 30 40\nbbb: 20 30\nccc: 30 40\nbbb: 20 30\naaa: 10 20\neee: 70 80\nggg: 20 50\n" \
       "bbb: 20 30\naaa: 10 20\neee: 70 80\nfff: 90 10\nggg: 20 50\nccc: 30 40\nfff: 90 10\nddd: 50 60\n" \
       "ggg: 20 50\nggg: 20 50\naaa: 10 20\naaa: 10 20\naaa: 10 20\nggg: 20 50\nfff: 90 10\neee: 70 80\n" \
       "bbb: 20 30\naaa: 10 20\nddd: 50 60\nddd: 50 60\naaa: 10 20\nfff: 90 10\nddd: 50 60\nbbb: 20 30\n" \
       "eee: 70 80\nccc: 30 40\neee: 70 80\neee: 70 80\nbbb: 20 30\nfff: 90 10\naaa: 10 20\neee: 70 80\n" \
       "bbb: 20 30\neee: 70 80\nggg: 20 50\naaa: 10 20\nddd: 50 60\neee: 70 80\nddd: 50 60\nfff: 90 10\n" \
       "eee: 70 80\nddd: 50 60\nddd: 50 60\neee: 70 80\nddd: 50 60\neee: 70 80\naaa: 10 20\nfff: 90 10\n" \
       "fff: 90 10\naaa: 10 20\nbbb: 20 30\nggg: 20 50\nfff: 90 10\nccc: 30 40\nccc: 30 40\nccc: 30 40\n" \
       "ggg: 20 50\nfff: 90 10\nddd: 50 60\nfff: 90 10\nccc: 30 40\naaa: 10 20\nccc: 30 40\nbbb: 20 30\n" \
       "ccc: 30 40\nccc: 30 40\nccc: 30 40\neee: 70 80"

lst_in = list(map(str.strip, data.splitlines())) # Ctrl + D

vic = """
class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f'{self.name} - {self.weight} - {self.price}'

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)

from collections import Counter
items = []
for line in lst_in:
    name, data = line.split(':')
    weight, price = map(float, data.split())
    items.append(ShopItem(name, weight, price))

shop_items = {k: [k, v] for k, v in Counter(items).items()}
"""

alex = """
class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)

def box(x):
    y, z = [], x.find(':')
    y.append(x[:z])
    y += x[z + 2:].split()
    return y

shop_items = {}
for i in lst_in:
    shop_items.setdefault(ShopItem(*box(i)), [ShopItem(*box(i)), 0])[1] += 1
"""

count = 100
print("vic:".rjust(5), timeit(stmt=vic, number=count, setup="from __main__ import lst_in"))
print("alex:".rjust(5), timeit(stmt=alex, number=count, setup="from __main__ import lst_in"))


