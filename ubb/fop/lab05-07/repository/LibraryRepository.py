import pickle

from model.exception import LibraryException
from model.library import Library

__author__ = 'cosmin'


class LibraryRepository:
    '''
    Class LibraryRepository which is a bridge between the ui and the backend code
    It has all the old and new states of the Library Repository
        Properties:
            _states = a list of all LibraryRepository objects, representing all the states
                                        the application has gone through
            _now = the index in the above list where we are now.
                    - this way we can easily make a undo/redo operation
    '''
    def __init__(self, restore = True):
        '''
        Constructor: initialises the Repository with the saved one (if exists) or starts a fresh (empty) Library
        '''
        if restore:
            self.restoreHistory()
        else:
            self.createFreshLibrary()

    def getNowIndex(self):
        '''
        Function to return the now index, described above
        :return: an integer representing the pointer the the state of the application at a given time.
        '''
        return self._now

    def getLibrary(self):
        '''
        Function to return the actual state of the application
        :return: a LibraryRepository object - which is the "now" state of the application
        '''
        return self._states[self.getNowIndex()]

    def getStateClone(self):
        '''
        Function to create a new LibraryRepository Object with the same values as the latest one.
        We basically create a new LibraryRepository and we alter it, and add it to the states list.
        :return: newState - a deepCopy LibraryRepository of the latest repository
        '''
        newState = Library()
        newState.deepCopy(self.getLibrary())
        return newState

    def addBook(self, book):
        '''
        Function to add a new Book
        :param book: the book we want to add
        '''
        newState = self.getStateClone()
        newState.addBook(book)
        self.createNewRepo(newState)

    def getBooksSize(self):
        '''
        Function to return the size of the actual book repository
        :return: an integer representing the number of books in the library
        '''
        return self.getLibrary().getBooksSize()

    def removeBook(self, bookId):
        '''
        Function to remove a Book
        Raises exception if no book was found.
        :param bookId:
        :raise: TypeError if the given Book was not found in the Library
        '''
        newState = self.getStateClone()
        newState.removeBook(bookId)
        self.createNewRepo(newState)

    def updateTitle(self, bookId, newTitle):
        '''
        Function to update the Title of a book
        :param bookPack: a tuple where the first element is the id of the book and the second element is the new Title of the book
        '''
        newState = self.getStateClone()
        newState.updateTitle(bookId, newTitle)
        self.createNewRepo(newState)

    def updateDescription(self, bookId, newDescr):
        '''
        Function to update the Description of a given book
        :param bookPack: a tuple where the first element is the id of the book and the second element is the new Description of the book
        '''
        newState = self.getStateClone()
        newState.updateDescription(bookId, newDescr)
        self.createNewRepo(newState)

    def updateAuthor(self, bookId, newAuthor):
        '''
        Function to update the Author of a given book
        :param bookPack: a tuple where the first element is the id of the book and the second element is the new Author of the book
        '''
        newState = self.getStateClone()
        newState.updateAuthor(bookId, newAuthor)
        self.createNewRepo(newState)

    def addClient(self, client):
        '''
        Function to add a new Client
        :param client: the new client we want to add
        :return:
        '''
        newState = self.getStateClone()
        newState.addClient(client)
        self.createNewRepo(newState)

    def removeClient(self, clientCNP):
        '''
        Function to remove a Client
        :param clientCNP: the new client we want to remove
        '''
        newState = self.getStateClone()
        newState.removeClient(clientCNP)
        self.createNewRepo(newState)

    def updateClientCnp(self, clientCNP, newCNP):
        '''
        Function to update the CNP of a client.
        :param clientPack: a tuple where the first element is the clientCnp and the second one is the new cnp of the client
        :raise TypeError if there is no client with the given CNP, or the newCNP already exist
        '''
        newState = self.getStateClone()
        newState.updateClientCnp(clientCNP, newCNP)
        self.createNewRepo(newState)

    def updateClientName(self, clientCNP, newName):
        '''
        Function to update the Name of a client.
        :param clientPack: a tuple where the first element is the clientCnp and the second one is the new name of the client
        :raise TypeError if there is no client with the given CNP
        '''
        newState = self.getStateClone()
        newState.updateClientName(clientCNP, newName)
        self.createNewRepo(newState)

    def rentBook(self, clientCNP, bookID):
        newState = self.getStateClone()
        newState.rentBook(clientCNP, bookID)
        self.createNewRepo(newState)

    def returnBook(self, clientCNP, bookID):
        newState = self.getStateClone()
        newState.returnBook(clientCNP, bookID)
        self.createNewRepo(newState)

    def getBooks(self):
        '''
        Function to list all the books at this moment in the Library
        '''
        return self.getLibrary().getBooks()

    def getClients(self):
        '''
        Function to list all the clients at this moment in the Library
        '''
        return self.getLibrary().getClients()

    def getLoans(self):
        '''
        Function to list all the loans  at this moment in the Library
        '''
        return self.getLibrary().getLoans()

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
        self._states = self._states[:self.getNowIndex() + 1]

    def createFuture(self, newRepo):
        '''
        Function to append the newRpo to the states list and to update the "now" pointer
        '''
        self._states.append(newRepo)
        self._now += 1

    def undo(self):
        '''
        Function to handle the undo command
        '''
        if self._now == 0:
            raise LibraryException("Already at earliest state!")
        else:
            self._now -= 1

    def redo(self):

        '''
        Function to handle the redo command
        '''
        if self._now == len(self._states) - 1:
            raise LibraryException("Already at newest state!")
        else:
            self._now += 1

    def restoreHistory(self):
        '''
        Function to restore the latest known history (pickled in the history.bin file)
        :return the _history dictionary pickled from the the history.bin file.
                    or a new empty dictionary if there is no such file.
        '''
        try:
            with open("repository/history.bin", "rb") as f:
                lastState = pickle.load(f)
                self._states = lastState._states
                self._now = lastState._now
        except IOError:
            self.createFreshLibrary()

    def saveHistory(self):
        '''
        Function to save the whole application information in the history.bin file
        '''
        try:
            with open("repository/history.bin", "wb") as f:
                pickle.dump(self, f)
            return "Successfully saved current state!"
        except IOError:
            raise LibraryException("Could not save the current state!")

    def createFreshLibrary(self):
        '''
        Function to create a fresh new Library
        '''
        self._states =  [Library()]
        self._now = 0
