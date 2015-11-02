from model.book import Book
from model.client import Client
from model.loan import Loan

__author__ = 'cosmin'


class LibraryRepository:
    '''
    Represents an actual state of a library at a given moment in time.
        properties:
            _books - list of all the books
            _clients - list of all the clients
            -loans - list of all the loans
    '''
    def __init__(self):
        self._books = []
        self._clients = []
        self._loans = []

    def addBook(self, book):
        '''
        Function to add a new Book
        :param book: the book we want to add
        '''
        self._books.append(book)

    def removeBook(self, bookId):
        '''
        Function to remove a Book
        Raises exception if no book was found.
        :param bookId:
        :raise: TypeError if the given Book was not found in the Library
        '''
        for i in range(len(self._books)):
            book = self._books[i]
            if book.getId() == bookId:
                del self._books[i]
                return
        raise TypeError("Book not found!")

    def updateTitle(self, bookId, newBookTitle):
        '''
        Function to update the Title of a book
        :param bookPack: a tuple where the first element is the id of the book and the second element is the new Title of the book
        '''
        for book in self.getBooks():
            if book.getId() == bookId:
                book.setTitle(newBookTitle)
                return
        raise TypeError("Book not found!")

    def updateDescription(self, bookId, newBookDescription):
        '''
        Function to update the Description of a given book
        :param bookPack: a tuple where the first element is the id of the book and the second element is the new Description of the book
        '''
        for book in self.getBooks():
            if book.getId() == bookId:
                book.setDescription(newBookDescription)
                return
        raise TypeError("Book not found!")

    def updateAuthor(self, bookId, newBookAuthor):
        '''
        Function to update the Author of a given book
        :param bookPack: a tuple where the first element is the id of the book and the second element is the new Author of the book
        '''
        for book in self.getBooks():
            if book.getId() == bookId:
                book.setAuthor(newBookAuthor)
                return
        raise TypeError("Book not found!")

    def searchBook(self, bookId):
        '''
        Function to search for a book in the list
        :param bookId: the id of the book we want to search for
        :return: the unique given book (since the id is unique)
        :raise TypeError Exception if the book was not found in the array
        '''
        for i in range(len(self._books)):
            book = self._books[i];
            if book.getId() == bookId:
                return book
        raise TypeError("Book not found!")

    def getBooks(self):
        '''
        Getter for the _books list of the LibraryRepository Class
        :return: the list _books
        '''
        return self._books

    def getBooksSize(self):
        '''
        Getter for the size of the _books list
        :return: an integer representing the list of the _books list
        '''
        return len(self._books)

    def addClient(self, client):
        '''
        Function to add a new Client
        :param client: the new client we want to add
        :return:
        '''
        try:
            self.searchClient(client.getCnp())
            raise ValueError("Client CNP already exists!")
        except TypeError:
            self._clients.append(client)

    def updateClientName(self, clientCnp, clientNewName):
        '''
        Function to update the Name of a client.
        :param clientPack: a tuple where the first element is the clientCnp and the second one is the new name of the client
        :raise TypeError if there is no client with the given CNP
        '''
        for client in self.getClients():
            if client.getCnp() == clientCnp:
                client.setName(clientNewName)
                return
        raise TypeError("Client not found!")

    def updateClientCnp(self, clientCnp, clientNewCnp):
        '''
        Function to update the CNP of a client.
        :param clientPack: a tuple where the first element is the clientCnp and the second one is the new cnp of the client
        :raise TypeError if there is no client with the given CNP, or the newCNP already exist
        '''
        try:
            self.searchClient(clientNewCnp)
            raise ValueError("Client CNP already exists!")
        except TypeError:
            for client in self.getClients():
                if client.getCnp() == clientCnp:
                    client.setCnp(clientNewCnp)
                    return
        raise TypeError("Client not found!")

    def removeClient(self, clientCNP):
        '''
        Function to remove a Client
        :param clientCNP: the new client we want to remove
        :return:
        '''
        for i in range(len(self._clients)):
            client = self._clients[i]
            if client.getCnp() == clientCNP:
                del self._clients[i]
                return
        raise TypeError("Client not found!")

    def searchClient(self, clientCNP):
        '''
        Function to search for a client by his CNP
        :param clientCNP: an integer representing the CNP of the client we want to search for
        :return: the unique Client (since the CNP is unique)
        :raise TypeError if there is no client with the given CNP.
        '''
        for i in range(len(self._clients)):
            client = self._clients[i]
            if client.getCnp() == clientCNP:
                return client
        raise TypeError("Client not found!")

    def getClients(self):
        '''
        Getter for the _clients list
        :return: the _clients list from the main class
        '''
        return self._clients

    def getLoans(self):
        '''
        Getter for the _loans list
        :return: the _loans list from the main class
        '''
        return self._loans

    def deepCopy(self, other):
        '''
        Function to deepCopy another LibraryRepository to this (self) one
        It copies all the data from another Repository to this one with no references of the objects (so that the states do not
            depend at all)
        :param other: another LibraryRepository
        '''
        self._books = [Book(book.getId(), book.getTitle(), book.getDescription(), book.getAuthor()) for book in other.getBooks()]
        self._clients = [Client(client.getCnp(), client.getName()) for client in other.getClients()]
        self._loans = [Loan(loan.getBook(), loan.getClient()) for loan in other.getLoans()]
