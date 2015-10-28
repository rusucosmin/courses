#from model.client import Client
#from model.book import Book
#from model.loan import  Loan
import pickle

__author__ = 'cosmin'


class LibraryRepository:
    def __init__(self):
        self._books = []
        self._clients = []
        self._loans = []

    def addBook(self, book):
        self._books.append(book)

    def addClient(self, client):
        self._clients.append(client)

    def addLoan(self, loan):
        self._loans.append(loan)

    def getBooks(self):
        return self._books

    def getClients(self):
        return self._clients

    def getLoans(self):
        return self._loans

'''
    def getBooks(self):
        try:
            with open("books.bin") as f:
                self._books = pickle.load(f)
        except IOError:
            self._books = []

    def getClients(self):
        try:
            with open("clients.bin") as f:
                self._clients = pickle.load(f)
        except IOError:
            self._books = []

    def getLoans(self):
        try:
            with open("loans.bin") as f:
                self._clients = pickle.load(f);
        except IOError:
            self._clients = []
'''
