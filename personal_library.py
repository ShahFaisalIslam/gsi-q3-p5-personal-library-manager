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
        pass

    # Called upon destruction of the object. Our code keeps the object 
    # throughout runtime, so it automatically runs at the end of the program
    def __del__(self):
        save_library(self.books)