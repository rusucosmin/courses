__author__ = 'cosmin'

from repository.LibraryRepository import *

class Book:
    """
    Represents an entity Book, with the properties:
        -id - a uniquely determined id, random using uuid4() function
        -title - the title of the book
        -description - the description of the book
        -author - the name of the book's author
    """
    def __init__(self, id, title, description, author):
        self._id = id
        self._title = title;
        self._description = description
        self._author = author

    def __repr__(self): return "Book Title: %s\nDescription: %s\nAuthor: %s\n" % (self._title, self._description, self._author)

    def get_id(self): return self._id

    def set_id(self, id): self._id = id

    def get_title(self): return self._title

    def set_title(self, title): self._title = title

    def get_description(self): return self._description

    def set_description(self, description): self._description = description

    def get_author(self): return self._author

    def set_author(self, author): self._author = author
