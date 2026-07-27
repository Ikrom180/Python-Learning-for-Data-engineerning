#Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                They are automatically called bby many of Python's built-in operations.
#                They allow developers to define or customize the behavior of objects


class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    #Instead of returning  memory addr it will return given data
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    #This will return bool what condition we will give
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    #Less than
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    #Greater Than
    def __gt__(self, other):
        return self.num_pages > other.num_pages

    #Addition
    def __add__(self, other):
        return f'{self.num_pages + other.num_pages} pages'

    #Make object iterable
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    #get item if we will give object like a list option it will return whatever we want
    def __getitem__(self,keyword):
        if keyword == 'title':
            return self.title
        elif keyword == 'author':
            return self.author
        elif keyword == 'num_pages':
            return self.num_pages
        else:
            return f'There is no {keyword} in the book'

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

# print(book1)

#What ever we compare objects it will return false till we use __eq__ bc memory always will be different
# print(book1 == book2)
# print(book1 < book2)
# print(book1 > book2)
# print(book2 + book3)

# print('THE' in book1)

print(book1['num_pages'])
print(book2['num_pages'])
print(book3['num_pages'])
