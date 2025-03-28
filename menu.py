# Menu module

from enum import Enum

class Menu(Enum):
    ADD = 1
    REMOVE = 2
    SEARCH = 3
    DISPLAY_BOOKS = 4
    DISPLAY_STATS = 5
    EXIT = 6

menu_items : tuple = "Add a book", "Remove a book", "Search for a book", "Display all books", "Display Statistics", "Exit"

# Displays all actions, and prompts user to provide item number
def display_menu() -> int:
    index = 1
    for item in menu_items:
        print(f"{index}. {item}")
        index += 1

    # Take choice from user as number
    input_index : int = int(input("Enter your choice (number):"))
    return input_index

# Perform action based on given choice
def perform_choice(choice : int):
    if choice not in Menu:
        print(f"{choice} is not valid")