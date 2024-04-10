#Напишите определение класса PowerTwo
class PowerTwo:

    def __init__(self, num):
        self.num = num
        self.it = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.it >= self.num:
            raise StopIteration
        else:
            self.it += 1
            return 2**self.it



numbers = PowerTwo(2)

assert hasattr(numbers, '__next__') is True
assert hasattr(numbers, '__iter__') is True

iterator = iter(numbers)
print('Элементы итератора PowerTwo(2)')
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
    raise ValueError('Не реализовали StopIteration')
except StopIteration:
    pass

print('-' * 15)
print('Элементы итератора PowerTwo(20)')
for i in PowerTwo(20):
    print(i)