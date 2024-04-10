class Book:

    def __init__(self, author=None, title=None, price=None):
        self.__title = title
        self.__author = author
        self.__price = price

    def set_title(self, title):
        if isinstance(title, Book) or type(title) is str:
            self.__title = title

    def set_author(self, author):
        if isinstance(author, Book) or type(author) is str:
            self.__author = author

    def set_price(self, price):
        if isinstance(price, Book) or type(price) is int:
            self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price


b1 = Book("Nikell", "Python 3", 100)

print(b1.get_title())