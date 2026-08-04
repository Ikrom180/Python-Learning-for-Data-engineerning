# Aggregation = Represents a relationship where one object (the whole)
#               contains references to one or more INDEPENDENT objects (the parts)


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
            self.books.append(book)

    def list_books(self):
        # print(self.books)
            for book in self.books:
                print(f"{book.title} by {book.author}")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library('New York Public Library')

book1 = Book('Harry Potter', 'J.K. Rowling')
book2 = Book('The Hobbit', 'J.R.R. Tolkein')
book3 = Book('The Colour of Magic', 'Terry Pratchet')

library.books.append(book1)
library.books.append(book2)
library.books.append(book3)

library.list_books()