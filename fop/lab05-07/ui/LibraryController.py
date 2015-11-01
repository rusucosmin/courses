import pickle
from repository.LibraryRepository import LibraryRepository

__author__ = 'cosmin'


class LibraryController:
    '''
    Class LibraryController which is a bridge between the ui and the backend code
    It has all the old and new states of the Library Repository
        Properties:
            _history - a dictionary where
                _history["states"] = a list of all LibraryRepository objects, representing all the states
                                        the application has gone through
                _history["now"] = the index in the above list where we are now.
                    - this way we can easily make a undo/redo operation
    '''
    def __init__(self):
        '''
        Constructor: initialises the Controller with the saved one (if exists) or starts a fresh (empty) Library
        '''
        self._history = self.restoreHistory()

    def getNowIndex(self):
        '''
        Function to return the now index, described above
        :return: an integer representing the pointer the the state of the application at a given time.
        '''
        return self._history["now"]

    def getLatestRepository(self):
        '''
        Function to return the actual state of the application
        :return: a LibraryRepository object - which is the "now" state of the application
        '''
        return self._history["states"][self.getNowIndex()]

    def getCloneRepository(self):
        '''
        Function to create a new LibraryRepository Object with the same values as the latest one.
        We basically create a new LibraryRepository and we alterate it, and add it to the states list.
        :return: newRepo - a deepCopy LibraryRepository of the latest repository
        '''
        newRepo = LibraryRepository()
        newRepo.deepCopy(self.getLatestRepository())
        return newRepo

    def addBook(self, book):
        '''
        Function to add a new Book
        :param book: the book we want to add
        '''
        newRepo = self.getCloneRepository()
        newRepo.addBook(book)
        self.createNewRepo(newRepo)

    def removeBook(self, bookId):
        '''
        Function to remove a Book
        Raises exception if no book was found.
        :param bookId:
        :raise: TypeError if the given Book was not found in the Library
        '''
        newRepo = self.getCloneRepository()
        newRepo.removeBook(bookId)
        self.createNewRepo(newRepo)

    def updateTitle(self, bookPack):
        '''
        Function to update the Title of a book
        :param bookPack: a tuple where the first element is the id of the book and the second element is the new Title of the book
        '''
        newRepo = self.getCloneRepository()
        newRepo.updateTitle(bookPack[0], bookPack[1])
        self.createNewRepo(newRepo)

    def updateDescription(self, bookPack):
        '''
        Function to update the Description of a given book
        :param bookPack: a tuple where the first element is the id of the book and the second element is the new Description of the book
        '''
        newRepo = self.getCloneRepository()
        newRepo.updateDescription(bookPack[0], bookPack[1])
        self.createNewRepo(newRepo)

    def updateAuthor(self, bookPack):
        '''
        Function to update the Author of a given book
        :param bookPack: a tuple where the first element is the id of the book and the second element is the new Author of the book
        '''
        newRepo = self.getCloneRepository()
        newRepo.updateAuthor(bookPack[0], bookPack[1])
        self.createNewRepo(newRepo)

    def addClient(self, client):
        '''
        Function to add a new Client
        :param client: the new client we want to add
        :return:
        '''
        newRepo = self.getCloneRepository()
        newRepo.addClient(client)
        self.createNewRepo(newRepo)

    def removeClient(self, clientCNP):
        '''
        Function to remove a Client
        :param clientCNP: the new client we want to remove
        :return:
        '''
        newRepo = self.getCloneRepository()
        newRepo.removeClient(clientCNP)
        self.createNewRepo(newRepo)

    def updateClientCnp(self, clientPack):
        '''
        Function to update the CNP of a client.
        :param clientPack: a tuple where the first element is the clientCnp and the second one is the new cnp of the client
        :raise TypeError if there is no client with the given CNP, or the newCNP already exist
        '''
        newRepo = self.getCloneRepository()
        newRepo.updateClientCnp(clientPack[0], clientPack[1])
        self.createNewRepo(newRepo)

    def updateClientName(self, clientPack):
        '''
        Function to update the Name of a client.
        :param clientPack: a tuple where the first element is the clientCnp and the second one is the new name of the client
        :raise TypeError if there is no client with the given CNP
        '''
        newRepo = self.getCloneRepository()
        newRepo.updateClientName(clientPack[0], clientPack[1])
        self.createNewRepo(newRepo)

    def listLibrary(self):
        '''
        Function to list all the books and the clients at this moment in the Library
        '''
        self.listBooks()
        self.listClients()

    def listBooks(self):
        '''
        Function to list all the books at this moment in the Library
        '''
        print('\n\n'.join(repr(book) for book in self.getLatestRepository().getBooks()))

    def listClients(self):
        '''
        Function to list all the clients at this moment in the Library
        '''
        print('\n\n'.join(repr(client) for client in self.getLatestRepository().getClients()))

    def listLoans(self):
        '''
        Function to list all the loans  at this moment in the Library
        '''
        print('\n\n'.join(repr(loan) for loan in self.getLatestRepository().getLoans()))

    def createNewRepo(self, newRepo):
        '''
        Function to create a new Repository based on the altered one.
        :param newRepo: the altered repository (the one with the latest command made
        '''
        self.forgetFuture()
        self.createFuture(newRepo)

    def forgetFuture(self):
        '''
        Function to erase all the states that are irrelevant from now on. :)
        '''
        self._history["states"] = self._history["states"][:self._history["now"] + 1]

    def createFuture(self, newRepo):
        '''
        Function to append the newRpo to the states list and to update the "now" pointer
        '''
        self._history["states"].append(newRepo)
        self._history["now"] += 1

    def undo(self):
        '''
        Function to handle the undo command
        '''
        if self._history["now"] == 0:
            print("Already at earliest state!")
        else:
            self._history["now"] -= 1

    def redo(self):

        '''
        Function to handle the redo command
        '''
        if self._history["now"] == len(self._history["states"]) - 1:
            print("Already at newest state!")
        else:
            self._history["now"] += 1

    def restoreHistory(self):
        '''
        Function to restore the latest known history (pickled in the history.bin file)
        :return the _history dictionary pickled from the the history.bin file.
                    or a new empty dictionary if there is no such file.
        '''
        try:
            with open("repository/history.bin", "rb") as f:
                lastState = pickle.load(f)
            return lastState
        except IOError:
            return {"states": [LibraryRepository()], "now": 0}

    def saveHistory(self):
        '''
        Function to save the whole application information in the history.bin file
        '''
        try:
            with open("repository/history.bin", "wb") as f:
                pickle.dump(self._history, f)
            print("Successfully saved current state!")
        except IOError:
            print("Could not save the current state!")

    def createFreshLibrary(self):
        '''
        Function to create a fresh new Library
        '''
        self._history = {"states": [LibraryRepository()], "now": 0}
        self.saveHistory()
