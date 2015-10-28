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

    def __repr__(self): return "Client Name: %s\nCNP: %s" % (self._name, self._cnp)

    def get_cnp(self): return self._cnp

    def set_cnp(self, cnp): self._cnp = cnp

    def get_name(self): return self._name

    def set_name(self, name): self._name = name
