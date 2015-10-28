__author__ = 'cosmin'


class Loan:
    def __init__(self, book, client):
        self._book = book
        self._client = client

    def getBook(self): return self._book

    def getClient(self): return self._client

