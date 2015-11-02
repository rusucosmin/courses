__author__ = 'cosmin'


class Loan:
    '''
    Entity to represent a loan, which is basically a pair of Client, Book. Every book can have only one Client at a given moment.
    Also, every Client can have one or more books rented.
    So the Loan has:
        - Renter (Client)
        - Rented Book
    '''
    def __init__(self, client, book):
        self._client = client
        self._book = book

    def __repr__(self):
        '''
        Function to print the Object in a nice way
        '''
        return "Client %s has the book #%d with the Title: %s" % (self._client.get_name(), self._book.get_id(), self._book.get_title())

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def getClient(self):
        '''
        Function to get the Client from a specific Loan
        :return: a Client object
        '''
        return self._client

    def getBook(self):
        '''
        Function to get the Book from a specific Loan
        :return: a book object
        '''
        return self._book