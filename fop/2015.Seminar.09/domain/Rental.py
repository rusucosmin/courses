from datetime import *
from domain.IDObject import IDObject
from domain.ValidatorException import ValidatorException

class Rental(IDObject):
    def __init__(self, rentalId, start, end, client, car):
        IDObject.__init__(self, rentalId)
        self._client = client
        self._car = car
        self._start = start
        self._end = end

    def getClient(self):
        return self._client
    
    def getCar(self):
        return self._car
    
    def getStart(self):
        return self._start
    
    def setStart(self, start):
        self._start = start

    def setClient(self, client):
        self._client = client
    
    def setCar(self, car):
        self._car = car
    
    def getEnd(self):
        return self._end
    
    def setEnd(self, end):
        self._end = end

    def __len__(self):
        return (self._end - self._start).days + 1

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "Rental:\nCar: " + str(self._car) + "\nClient: " + str(self._client) + "\nPeriod: " + self._start.strftime("%Y-%m-%d") + " to " + self._end.strftime("%Y-%m-%d")

class RentalValidator:
    
    def validate(self, rental):
        if isinstance(rental, Rental) == False:
            raise TypeError("Not a Rental")
        _errorList = []
        now = datetime.now()
        if rental.getStart() < now:
            _errorList.append("Rental starts in past;")
        if len(rental) < 1:
            _errorList.append("Rental must be at least 1 day;")
        if len(_errorList) > 0:
            raise ValidatorException(_errorList)

def testRental():
    pass

def testRentalValidator():
    #
    # Test for RentalValidator
    #
    pass

