"""
Write a Library class with no_of_books and books as two instance variables.
Write a program to create a library from this Library class and show how 
you can print all books, add a book and get the number of books using 
different methods. Show that your program doesnt persist the books 
after the program is stopped!
"""

class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books += 1

    def print_all_books(self):
        print("Books in the library:")
        for book in self.books:
            print("- " + book)

    def get_no_of_books(self):
        return self.no_of_books

# Create a library instance
library = Library()

# Add books to the library
library.add_book("Book 1")
library.add_book("Book 2")
library.add_book("Book 3")

# Print all books
library.print_all_books()

# Get the number of books
num_books = library.get_no_of_books()
print(f"Total number of books in the library: {num_books}")
