from model.book import Book
from model.client import Client
from model.exception import LibraryException

__author__ = 'cosmin'


class Command:
    '''
    Represents a data type. A command is a list of arguments given by the user, which defines what
        operation the application should execute
    It has only one property:
        -a list of string containing the command arguments
    '''
    ARGS = {
        "addbook":4,
        "addclient":3,
        "removebook":2,
        "removeclient":2,
        "updatecnp":3,
        "updatename":3,
        "updatetitle":3,
        "updateauthor":3,
        "updatedescription":3,
        "rentbook": 3,
        "returnbook": 3,
        "list": 1,
        "save": 1,
        "exit": 1,
        "delete": 1,
        "listbooks": 1,
        "listclients": 1,
        "undo": 1,
        "redo": 1,
        "help": 1
    }
    def __init__(self, stringInput):
        self._args = stringInput.split('|')
        self._args[0] = self._args[0].lower()
        if not self._args[0] in Command.ARGS.keys():
            raise LibraryException("CommandError - Unknown command!")
        if len(self._args) != Command.ARGS[self._args[0]]:
            raise LibraryException("CommandError - Argument size do not match!")
        for arg in self._args:
            if arg == "":
                raise LibraryException("CommandError - Empty parameters!")

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def getArgs(self):
        return self._args

    def getArgsSize(self):
        return len(self._args)

    def getArg(self, pos):
        if pos >= self.getArgsSize():
            raise LibraryException("Command error - Not enough parameters.")
        return self._args[pos]

    def toAddBook(self, id):
        return Book(id, self.getArg(1), self.getArg(2), self.getArg(3))

    def toAddClient(self):
        try:
            return Client(int(self.getArg(1)), self.getArg(2))
        except ValueError as ve:
            raise LibraryException("Client CNP should be an integer.")

    def toRemoveClient(self):
        try:
            return int(self.getArg(1))
        except ValueError as ve:
            raise LibraryException("Client CNP should be an integer.")

    def toRemoveBook(self):
        try:
            return int(self.getArg(1))
        except ValueError as ve:
            raise LibraryException("Book number should be an integer.")

    def toUpdateCnp(self):
        try:
            return (int(self.getArg(1)), int(self.getArg(2)))
        except ValueError:
            raise LibraryException("Client CNP should be an integer.")

    def toUpdateName(self):
        try:
            return (int(self.getArg(1)), self.getArg(2))
        except ValueError:
            raise LibraryException("Client CNP should be an integer.")

    def toUpdateTitle(self):
        try:
            return (int(self.getArg(1)), self.getArg(2))
        except ValueError:
            raise LibraryException("Book ID should be an integer.")

    def toUpdateDescription(self):
        try:
            return (int(self.getArg(1)), self.getArg(2))
        except ValueError:
            raise LibraryException("Book ID should be an integer.")

    def toUpdateAuthor(self):
        try:
            return (int(self.getArg(1)), self.getArg(2))
        except ValueError:
            raise LibraryException("Book ID should be an integer.")