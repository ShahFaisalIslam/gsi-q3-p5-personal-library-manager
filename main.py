# Personal Library Manager
# Version 0.1
# Author: Shah Faisal (faisal.islam.ceme@gmail.com)

import library_io
import menu

library: list = library_io.load_library()

choice : int = menu.display_menu()
print(f"You have selected choice #{choice}")
menu.perform_choice(choice)
library_io.save_library(library)