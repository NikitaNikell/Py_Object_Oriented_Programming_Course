class Book:

    def __init__(self, title="", author="", pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key == "title" or key == "author":
            if not isinstance(value, str):
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                return object.__setattr__(self, key, value)

        elif key == "pages" or key == "year":
            if type(value) != int:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                return object.__setattr__(self, key, value)

book = Book("Python ООП", "Сергей Балакирев", 123, 2022)

print(book.__dict__)
assert book.title == "Python ООП" and book.author == "Сергей Балакирев" and book.pages == 123 and book.year == 2022, "в объекте book имеются неверные данные в значениях атрибутов"
