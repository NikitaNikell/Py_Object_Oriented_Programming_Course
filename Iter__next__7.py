from random import randint


class Dice:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Dice={self.value}"


class Game:
    def __iter__(self):
        return self

    def __next__(self):
        return Dice(randint(1, 6)), Dice(randint(1, 6))   #почти бесконечный итератор


for d1, d2 in Game():
    print(d1, d2)
    if d1.value == 6 and d2.value == 6:
        print('GameOver')
        break