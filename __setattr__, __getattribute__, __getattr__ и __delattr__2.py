class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, name, value):
        match name:
            case "title" | "author" if not isinstance(value, str):
                raise TypeError("Неверный тип присваиваемых данных.")
            case "pages" | "year" if not type(value) is int:
                raise TypeError("Неверный тип присваиваемых данных.")
            case _:
                # Если атрибут не совпадает с 'title', 'author', 'pages' или 'year'
                super().__setattr__(name, value)

# Пример использования
book = Book(title="Example Book", author="John Doe", pages=200, year=2023)

print(book.__dict__)

# Попытка присвоить неверный тип данных
# try:
#     book.pages = "invalid_value"
# except TypeError as e:
#     print(e)