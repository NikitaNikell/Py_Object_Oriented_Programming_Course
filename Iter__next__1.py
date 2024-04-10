class Student:
    def __init__(self, name):
        self.name = name
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.name):
            #self.index = 0 # сброс счётчика для повторного итерирования
            raise StopIteration
        self.index += 1
        return self.name[self.index - 1]


ivan = Student('Ivan')
it = iter(ivan)

for i in it:
    print(i)

print('----')

for i in it:
    print(i)