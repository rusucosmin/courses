import pickle
from repository.LibraryRepository import LibraryRepository
from model.exception import LibraryException
from model.sort import gnomeSort, myFilter
from model.book import Book

import operator

__author__ = 'cosmin'


class LibraryController:
    '''
    Class LibraryController which is a bridge between the ui and the database
        Properties:
            _repo: the repository where everything is saved
    '''
    def __init__(self, repo):
        '''
        Constructor: initialises the Controller with the repositories
        '''
        self._repo = repo

    def addBook(self, book):
        '''
        Function to add a new Book
        :param book: the book we want to add
        '''
        self._repo.addBook(book)

    def removeBook(self, bookId):
        '''
        Function to remove a Book
        Raises exception if no book was found.
        :param bookId:
        :raise: TypeError if the given Book was not found in the Library
        '''
        for book in [loan.getBook() for loan in self._repo.getLoans()]:
            if book.getId() == bookId:
                raise LibraryException("Book rented...")
        self._repo.removeBook(bookId)

    def updateTitle(self, bookId, newTitle):
        '''
        Function to update the Title of a book
        :param bookPack: a tuple where the first element is the id of the book and the second element is the new Title of the book
        '''
        self._repo.updateTitle(bookId, newTitle)

    def updateDescription(self, bookId, newDescription):
        '''
        Function to update the Description of a given book
        :param bookPack: a tuple where the first element is the id of the book and the second element is the new Description of the book
        '''
        self._repo.updateDescription(bookId, newDescription)

    def updateAuthor(self, bookId, newAuthor):
        '''
        Function to update the Author of a given book
        :param bookPack: a tuple where the first element is the id of the book and the second element is the new Author of the book
        '''
        self._repo.updateAuthor(bookId, newAuthor)


    def addClient(self, client):
        '''
        Function to add a new Client
        :param client: the new client we want to add
        :return:
        '''
        self._repo.addClient(client)

    def removeClient(self, clientCNP):
        '''
        Function to remove a Client
        :param clientCNP: the new client we want to remove
        :return:
        '''
        for client in [loan.getClient() for loan in self._repo.getLoans()]:
            if client.getCnp() == clientCNP:
                raise LibraryException("Client has rented book, please return them and then remove him.")
        self._repo.removeClient(clientCNP)

    def updateClientCnp(self, clientCNP, newCNP):
        '''
        Function to update the CNP of a client.
        :param clientPack: a tuple where the first element is the clientCnp and the second one is the new cnp of the client
        :raise TypeError if there is no client with the given CNP, or the newCNP already exist
        '''
        self._repo.updateClientCnp(clientCNP, newCNP)

    def updateClientName(self, clientCNP, nwName):
        '''
        Function to update the Name of a client.
        :param clientPack: a tuple where the first element is the clientCnp and the second one is the new name of the client
        :raise TypeError if there is no client with the given CNP
        '''
        self._repo.updateClientName(clientCNP, nwName)

    def getLibrary(self):
        '''
        Function to list all the books and the clients at this moment in the Library
        '''
        return self._repo.getLibrary()

    def getBooks(self):
        '''
        Function to list all the books at this moment in the Library
        '''
        return self._repo.getBooks()

    def getClients(self):
        '''
        Function to list all the clients at this moment in the Library
        '''
        return self._repo.getClients()

    def getLoans(self):
        '''
        Function to list all the loans  at this moment in the Library
        '''
        return self._repo.getLoans()

    def rentBook(self, clientCNP, bookID):
        '''
        function to implement the rent a book function
        '''
        return self._repo.rentBook(clientCNP, bookID)

    def returnBook(self, clientCNP, bookID):
        '''
        function to implement the return a book function
        '''
        return self._repo.returnBook(clientCNP, bookID)

    def undo(self):
        '''
        Function to handle the undo command
        '''
        self._repo.undo()

    def redo(self):
        '''
        Function to handle the redo command
        '''
        self._repo.redo()

    def save(self):
        '''
        Function to save the whole application information in the history.bin file
        '''
        self._repo.saveHistory()

    def recreate(self):
        '''
        Function to create a fresh new Library
        '''
        self._repo.createFreshLibrary()

    def getRentedBooksSorted(self):
        '''
        Function to return the books sorted by title
        :return:
        '''
        loans = self._repo.getLoans()
        rentedbooks = []
        for loan in loans:
            rentedbooks.append(loan.getBook())
        return gnomeSort(rentedbooks, Book.cmpByTitle, False)

    @staticmethod
    def cmpActive(x, y):
        '''
        Static method to compare two tuples (Client, nr_of_books_rented)
        It compares first by the number of rented books, then by name.
        :return:
        '''
        if x[1] < y[1]:
            return -1
        elif x[1] > y[1]:
            return 1
        else:
            if x[0].getName() > y[0].getName():
                return 1
            elif x[0].getName() < y[0].getName():
                return -1
            else:
                return 0

    def getMostActiveUsers(self):
        loans = self._repo.getLoans()
        users = []
        for loan in loans:
            if loan.getClient() in [x[0] for x in users]:
                for i in range(len(users)):
                    if users[i][0] == loan.getClient():
                        users[i] = (users[i][0], users[i][1] + 1)
            else:
                users.append((loan.getClient(), 1))
        return gnomeSort(users, LibraryController.cmpActive, True)
       # return sorted(many.items(), key=operator.itemgetter(1), reverse=True)

    @staticmethod
    def filterFct(book):
        return book.getId() < 3

    def filterBooks(self, iterable):
        return myFilter(iterable, LibraryController.filterFct)