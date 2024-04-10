class SequenceIterator:
    def __init__(self, sp):
        self.sp = sp[::2] + sp[1::2]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.sp[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result


container = SequenceIterator([1, 5, 4, 6, 43, True, 'hello'])
for i in container:
    print(i)
