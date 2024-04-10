class Iterator:
    def __init__(self, text):
        self.text = text.upper()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.text[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result


phrase = Iterator('Qwerty')
it_1 = iter(phrase)
it_2 = iter(phrase)
for i in it_1:
    print(i)
for i in it_1:
    print(i)
for i in it_2:
    print(i)