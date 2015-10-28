import pickle
from repository.LibraryRepository import LibraryRepository

__author__ = 'cosmin'


class LibraryController:

    def __init__(self):
        self._history = self.restoreHistory()

    def getNowIndex(self):
        return self._history["now"]

    def getLatestRepository(self):
        return self._history["states"][self.getNowIndex()]

    def addBook(self, book):
        self.getLatestRepository().addBook(book)
        #self.forgetFuture()

    def addClient(self, client):
        self.getLatestRepository().addClient(client)

    def forgetFuture(self):
        self._history["states"] = self._history["states"][:self._history["now"] + 1]

    def listBooks(self):
        print('\n\n'.join(repr(book) for book in self.getLatestRepository().getBooks()))

    def listClients(self):
        print('\n\n'.join(repr(client) for client in self.getLatestRepository().getClients()))

    def restoreHistory(self):
        try:
            with open("repository/history.bin", "rb") as f:
                lastState = pickle.load(f)
            return lastState
        except IOError:
            return {"states": [LibraryRepository()], "now": 0}

    def saveHistory(self):
        try:
            with open("repository/history.bin", "wb") as f:
                pickle.dump(self._history, f)
            print("Succesfully saved current state!")
        except IOError:
            print("Could not save the current state!")