class LibraryIterator:
    def __init__(self, books):
        self.books = books
        self.current_book_index = 0
        self.current_page_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_book_index < len(self.books):
            book = self.books[self.current_book_index]
            if self.current_page_index < len(book.pages):
                page = book.pages[self.current_page_index]
                self.current_page_index += 1
                return page
            else:
                self.current_book_index += 1
                self.current_page_index = 0
                return next(self)
        else:
            raise StopIteration

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        return LibraryIterator(self.books) # тут определите, что будете передавать итератору


# Пример использования
book1 = Book("Book 1", ["Page 1", "Page 2", "Page 3", "Page 4"])
book2 = Book("Book 2", ["Page A", "Page B", "Page C"])
book3 = Book("Book 3", ["Chapter 1", "Chapter 2"])

library = Library()
library.add_book(book1)

library.add_book(book2)
library.add_book(book3)

# Используем вложенный итератор для обхода страниц в библиотеке
for page in library:
    print(page)