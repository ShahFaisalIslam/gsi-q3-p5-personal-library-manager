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
    input_index = 0
    # Display the actions
    for item in menu_items:
        print(f"{index}. {item}")
        index += 1

    # Take choice from user as number
    while True:
        try:
            input_index : int = int(input("Enter your choice (number):"))
            if input_index not in Menu:
                raise ValueError()
        except:
            print("Invalid input, enter a choice from 1 to 6")
            continue
        break
    return input_index

# Perform action based on given choice
def perform_choice(choice : int):
    if choice == Menu.ADD.value:
        pass
    elif choice == Menu.REMOVE.value:
        pass
    elif choice == Menu.SEARCH.value:
        pass
    elif choice == Menu.DISPLAY_BOOKS.value:
        pass
    elif choice == Menu.DISPLAY_STATS.value:
        pass
    elif choice == Menu.EXIT.value:
        pass
    else:
        print(f"Choice {choice} not present in menu")