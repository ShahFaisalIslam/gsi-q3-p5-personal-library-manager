# Personal Library module

from library_io import load_library,save_library
from enum import Enum

# Book class, to ensure that any book added has at least the required variables
# title : Book title
# author: Book author
# pub_year: Publication Year
# genre: Genre
# status: Where book is read (True) or not read (False) 
class Book(dict):
    def __init__(self,title: str, author: str,pub_year: int,genre: str,status: bool):
        self.title = title
        self.author = author
        self.pub_year = pub_year
        self.genre = genre
        self.status = status

# Enum for search mode
class SearchMode(Enum):
    TITLE = 1
    AUTHOR = 2

# Member: List of books
# Methods:
#   * Add a book
#   * Remove a book
#   * Search for a book
#   * Display all books
#   * Display aggregated statistics
class PersonalLibrary:
    def __init__(self):
        self.books = load_library()

    # Add a book
    def add_book(self):
        title : str = input("Title:")
        author : str = input("Author:")
        # Publication year may not be given as a number
        pub_year = None
        while True:
            try:
                pub_year : int = int(input("Publication Year:"))
                break
            except:
                print("Invalid year, please try again, something like 1234")
 
        genre : str = input("Genre:")

        # Response may not be a yes or no or anything that starts with y or n
        status = None
        while True:
            try:
                status: str = input("Is book read? (yes/no):")
                if status[0].lower() == 'y':
                    status = True
                elif status[0].lower() == 'n':
                    status = False
                else:
                    raise ValueError()
                break
            except:
                print("Invalid input, provide yes or no")
        pass
        self.books.append(Book(title,author,pub_year,genre,status).__dict__)

    # Remove a book
    def remove_book(self):
        title : str = input("Title:")
        index = 0
        removed_book = None
        for book in self.books:
            if book["title"] == title:
                removed_book = self.books.pop(index)
            index += 1
        
        if removed_book:
            print(f"Removed book '{removed_book["title"]}' by '{removed_book["author"]}")
        else:
            print(f"No book found with title '{title}'")
    
    # Helper to display a book
    def _display_book(self,index : int,book : dict) -> None:
        print(f"{index}. {book["title"]} by {book["author"]} ({book["pub_year"]}) - {book["genre"]} - {'Read' if book["status"] else 'Not Read'}")

    # Search for a book by title or author
    def search_book(self):
        choice : int = None
        found_books : list[Book] = []

        # Obtain search choice
        while True:
            try:
                choice = int(input("Type 1 for title, or 2 for author:"))
                if choice != SearchMode.AUTHOR.value and choice != SearchMode.TITLE.value:
                    raise ValueError()
                break
            except:
                print("Invalid choice, type 1 or 2")
        
        match choice:
            case SearchMode.AUTHOR.value:
                author = input("Author:")
                for book in self.books:
                    if author == book["author"]:
                        found_books.append(book)
            case SearchMode.TITLE.value:
                title = input("Title:")
                for book in self.books:
                    if title == book["title"]:
                        found_books.append(book)

        if not len(found_books):
            print("No books found")
        else:
            index = 1
            print("Found books:")
            for book in found_books:
                self._display_book(index,book)
                index += 1

    # Display all books
    def display_books(self):
        index = 1
        for book in self.books:
            self._display_book(index,book)
            index += 1

    # Display aggregate statistics
    def display_aggr_stats(self):
        print(f"Total books: {len(self.books)}")
        n_books_read : int = 0
        for book in self.books:
            if book["status"]:
                n_books_read += 1
        print(f"Read: {round(n_books_read * 100/len(self.books))} %")

    # Called upon destruction of the object. Our code keeps the object 
    # throughout runtime, so it automatically runs at the end of the program
    def __del__(self):
        save_library(self.books)