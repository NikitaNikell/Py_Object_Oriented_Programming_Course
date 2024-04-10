class Book:
    def __init__(self, a, b, desc):
        self.a = a
        self.b = b
        self.desc = desc

    def __bool__(self):
        print("Вызван __bool__ для ", self.desc)
        return self.a == self.b


book1 = Book(1, 2, 'res = bool(book)')
book2 = Book(1, 2, 'if book:')
book3 = Book(1, 2, 'while book:')
book4 = Book(1, 2, 'print(book)')
book5 = Book(1, 2, 'len(book):')
book6 = Book(1, 2, 'for b in book:')

""" Тest: res = bool(book) """
res = bool(book1)

""" Test: if book: """
if book2:
    pass

""" Тest: while book: """
while book3:
    pass

""" Тest: print(book) """
print("Не вызывается для print(book)", book4)

""" Тest: len(book): """
try:
    len(book5)
except TypeError:
    print("Ошибка для len(book5) TypeError: object of type 'Book' has no len()")

""" Test: for b in book: """
try:
    for b in book6:
        pass
except TypeError:
    print("Ошибка для for b in book6 TypeError: 'Book' object is not iterable")