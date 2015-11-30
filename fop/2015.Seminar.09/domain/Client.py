from domain.IDObject import IDObject

class Client(IDObject):
    def __init__(self, clientId, cnp, name):
        IDObject.__init__(self, clientId)
        self._cnp = cnp
        self._name = name

    def getCNP(self):
        return self._cnp

    def getName(self):
        return self._name

    def setName(self, value):
        self._name = value

    def __eq__(self, c):
        if isinstance(c, Client) == False:
            return False
        return self._objectId == c._objectId

    def __str__(self):
        return "Id=" + str(self.getId()) + ", Name=" + str(self._name)
    
    def __repr__(self):
        return str(self)

class ClientValidator:
    def _isCNPValid(self, cnp):
        # SAALLZZJJNNNC
        if len(cnp) != 13:
            # This is not a full CNP validation
            return False
        for a in cnp:
            if a < '0' or a > '9':
                return False
        return True

    def validate(self, client):
        """
        Validate if provided Client instance is valid
        client - Instance of Client type
        Return List of validation errors. An empty list if instance is valid.
        """
        if isinstance(client, Client) == False:
            raise TypeError("Not a Client")
        _errors = []
        if self._isCNPValid(client.getCNP()) == False:
            _errors.append("CNP not valid.;")
        if len(client.getName()) == 0:
            _errors.append("Name not valid.")
        if len(_errors) != 0:
            raise ValueError(_errors)

def testClient():
    #
    # Write a test for the Client class here
    #
    pass

def testClientValidator():
    #
    # Write a test for the ClientValidator class here
    #
    pass

