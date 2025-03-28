# Library I/O
# This module provides two functions:
# * load_library(), for loading library from library file
# * save_library(), for saving library to library file

import json

library_filename : tuple = ("library.json",) # Tuples are immutable

def load_library() -> list:
    library : list = []

    with open(library_filename[0]) as library_file:
        library = json.loads(library_file.read())

    return library

def save_library(library: list):
    with open(library_filename[0],'w') as library_file:
        json.dump(library,library_file)