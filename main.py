# Personal Library Manager
# Version 0.1
# Author: Shah Faisal (faisal.islam.ceme@gmail.com)
from personal_library import PersonalLibrary
import menu

# library: list = library_io.load_library()
library: PersonalLibrary = PersonalLibrary()
choice :int = 0
while choice != menu.Menu.EXIT.value:
    choice : int = menu.display_menu()
    print(f"You have selected choice #{choice}")
    menu.perform_choice(choice,library)

print("Library saved to file. See you again soon!")