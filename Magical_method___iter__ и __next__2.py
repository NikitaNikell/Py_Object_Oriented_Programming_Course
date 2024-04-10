class InfinityIterator:

    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        number = self.counter
        self.counter += 10
        return number

a = iter(InfinityIterator())

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))