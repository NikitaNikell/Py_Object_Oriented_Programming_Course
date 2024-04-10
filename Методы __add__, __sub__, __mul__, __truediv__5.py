class Book:
    def __init__(self, title: str, author:str, year:int):
        self.title = title if type(title) == str else None
        self.author = author if type(author) == str else None
        self.year = year if type(year) == int else None


class Lib:
    def __init__(self):
        self.book_list = []

    @staticmethod
    def __verify_value(value):
        if not isinstance(value, Book):
            raise ArithmeticError('Неверныо переданны данные')

    def __add__(self, other):
        self.__verify_value(other)
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            self.book_list.pop(other)
        elif isinstance(other, Book):
            self.book_list.remove(other)
        return self

    def __isub__(self, other):
        return self.__sub__(other)

    def __len__(self):
        return len(self.book_list)


book = Book("Book_1", "Nickel", 2023)



