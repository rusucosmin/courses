from model.book import Book
from model.client import Client

__author__ = 'cosmin'


class Command:
    '''
    Represents a data type. A command is a list of arguments given by the user, which defines what
        operation the application should execute
    It has only one property:
        -a list of string containing the command arguments
    '''
    ADD_BOOK_ARGS = 3 + 1                   # +1 for the command type
    ADD_CLIENT_ARGS = 2 + 1
    REMOVE_BOOK_ARGS = 1 + 1
    REMOVE_CLIENT_ARGS = 1 + 1
    UPDATE_CLIENT_CNP = 2 + 1
    UPDATE_CLIENT_NAME = 2 + 1
    UPDATE_BOOK_TITLE = 2 + 1
    UPDATE_BOOK_AUTHOR = 2 + 1
    UPDATE_BOOK_DESCRIPTION = 2 + 1
    def __init__(self, stringInput):
        self._args = stringInput.split('|')
        self._args[0] = self._args[0].lower()
        for arg in self._args:
            if arg == "":
                raise SyntaxError("CommandError - Empty parameters!")

    def getArgs(self):
        return self._args

    def getArgsSize(self):
        return len(self._args)

    def getArg(self, pos):
        if pos >= self.getArgsSize():
            raise SyntaxError("Command error - Not enough parameters.")
        return self._args[pos]

    def testArgsSize(self, actualSize, wantedSize):
        if actualSize != wantedSize:
            raise SyntaxError("Command error - Wrong parameters.")

    def toAddBook(self, id):
        self.testArgsSize(self.getArgsSize(), Command.ADD_BOOK_ARGS)
        return Book(id, self.getArg(1), self.getArg(2), self.getArg(3))

    def toAddClient(self):
        self.testArgsSize(self.getArgsSize(), Command.ADD_CLIENT_ARGS)
        try:
            return Client(int(self.getArg(1)), self.getArg(2))
        except ValueError as ve:
            raise ValueError("Client CNP should be an integer.")

    def toRemoveClient(self):
        self.testArgsSize(self.getArgsSize(), Command.REMOVE_CLIENT_ARGS)
        try:
            return int(self.getArg(1))
        except ValueError as ve:
            raise ValueError("Client CNP should be an integer.")

    def toRemoveBook(self):
        self.testArgsSize(self.getArgsSize(), Command.REMOVE_BOOK_ARGS)
        try:
            return int(self.getArg(1))
        except ValueError as ve:
            raise ValueError("Book number should be an integer.")

    def toUpdateCnp(self):
        self.testArgsSize(self.getArgsSize(), Command.UPDATE_CLIENT_CNP)
        try:
            return (int(self.getArg(1)), int(self.getArg(2)))
        except ValueError:
            raise ValueError("Client CNP should be an integer.")
    def toUpdateName(self):
        self.testArgsSize(self.getArgsSize(), Command.UPDATE_CLIENT_NAME)
        try:
            return (int(self.getArg(1)), self.getArg(2))
        except ValueError:
            raise ValueError("Client CNP should be an integer.")

    def toUpdateTitle(self):
        self.testArgsSize(self.getArgsSize(), Command.UPDATE_BOOK_TITLE)
        try:
            return (int(self.getArg(1)), self.getArg(2))
        except ValueError:
            raise ValueError("Book ID should be an integer.")

    def toUpdateDescription(self):
        self.testArgsSize(self.getArgsSize(), Command.UPDATE_BOOK_TITLE)
        try:
            return (int(self.getArg(1)), self.getArg(2))
        except ValueError:
            raise ValueError("Book ID should be an integer.")

    def toUpdateAuthor(self):
        self.testArgsSize(self.getArgsSize(), Command.UPDATE_BOOK_TITLE)
        try:
            return (int(self.getArg(1)), self.getArg(2))
        except ValueError:
            raise ValueError("Book ID should be an integer.")