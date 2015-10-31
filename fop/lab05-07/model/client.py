__author__ = 'cosmin'


class Client:
    """
    Represents an entity for the clients who can rent books, which has the following properties:
        -cnp - an uniquely determined id
        -name - the name of the person (client)
    """
    def __init__(self, cnp, name):
        self._cnp = cnp
        self._name = name

    def __repr__(self):
        '''
        Function to print the Object in a nice way
        '''
        return "Client Name: %s\nCNP: %s" % (self._name, self._cnp)

    def getCnp(self):
        '''
        Getter for the cnp property
        :return: the cnp of the client
        '''
        return self._cnp

    def setCnp(self, cnp):
        '''
        Setter for the cnp property
        '''
        self._cnp = cnp

    def getName(self):
        '''
        Getter for the name property
        :return: the name of the client (string)
        '''
        return self._name

    def setName(self, name):
        '''
        Setter for the name of a client
        '''
        self._name = name
