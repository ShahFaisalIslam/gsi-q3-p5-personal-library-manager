# Personal Library module
# It will contain a class PersonalLibrary as follows:
# Private member: List of books
# Methods:
#   * Add a book
#   * Remove a book
#   * Search for a book
#   * Display all books
#   * Display aggregated statistics
from library_io import load_library,save_library

class PersonalLibrary:
    def __init__(self):
        self.books = load_library()

    # Add a book
    def add_book(self):
        pass

    # Remove a book
    def remove_book(self):
        pass

    # Called upon destruction of the object. Our code keeps the object 
    # throughout runtime, so it automatically runs at the end of the program
    def __del__(self):
        save_library(self.books)