class InfinityIterator:
    """ Создайте класс InfinityIterator, который реализует бесконечный итератор. """

    def __init__(self, num=0):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        result = self.num
        self.num += 10
        return result


for i in InfinityIterator(0):
    print(i)