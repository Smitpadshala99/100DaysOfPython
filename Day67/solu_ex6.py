class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []
    
    def addBooks(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def show(self):
        print(f"The library has {self.no_of_books} books")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBooks("Book 1")
l1.addBooks("Book 2")
l1.addBooks("Book 3")
l1.show()