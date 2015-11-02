__author__ = 'cosmin'


class Book:
    '''
    Represents an entity Book, with the properties:
        -id - a uniquely determined id, random using uuid4() function
        -title - the title of the book
        -description - the description of the book
        -author - the name of the book's author
    '''
    def __init__(self, id, title, description, author):
        self._id = id
        self._title = title
        self._description = description
        self._author = author

    def __repr__(self):
        '''
        Function to print the Book in a nice way
        '''
        return "Book #%d:\nTitle: %s\nDescription: %s\nAuthor: %s\n" % (self._id, self._title, self._description, self._author)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def getId(self):
        '''
        Getter for the id of the book
        :return: an integer representing the id of the book
        '''
        return self._id

    def setId(self, id):
        '''
        Setter for the id of the book
        :param id: the new id of the book
        '''
        self._id = id

    def getTitle(self):
        '''
        Getter for the title of the book
        :return: a string: the title of the book
        '''
        return self._title

    def setTitle(self, title):
        '''
        Setter for the title of the book
        :return: a string: the title of the book
        '''
        self._title = title

    def getDescription(self):
        '''
        Getter for the description of the book
        :return: a string: the description of the book
        '''
        return self._description

    def setDescription(self, description):
        '''
        Setter for the description of the book
        :param description: the new description of the book
        '''
        self._description = description

    def getAuthor(self):
        '''
        Getter for the author of the book
        :return: a string representing the author of the book
        '''
        return self._author

    def setAuthor(self, author):
        '''
        Setter for the author of the book
        :param description: the new author of the book
        '''
        self._author = author
