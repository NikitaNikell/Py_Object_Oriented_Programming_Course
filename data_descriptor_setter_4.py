class FloatValue:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")
        setattr(instance, self.name, value)


class Cell:

    value = FloatValue()

    def __init__(self, value = 0.0):
        self.value = value


class TableSheet:

    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.cells = [[Cell(float(0.0)) for i in range(M)] for j in range(N)]


table = TableSheet(5, 3)

n = 1.0
for i in range(5):
    for j in range(3):
        table.cells[i][j].value = n
        n += 1.0

assert isinstance(table, TableSheet)
assert len(table.cells) == 5 and len(table.cells[0]) == 3

assert type(table.cells) == list

res = [int(x.value) for row in table.cells for x in row]
assert res == list(range(1, 16))

table.cells[0][0].value = 1.0
x = table.cells[1][0].value

try:

    table.cells[0][0].value = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"


