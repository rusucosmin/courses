from domain.ValidatorException import ValidatorException
from domain.IDObject import IDObject

class Car(IDObject):
    def __init__(self, objectId, licenseNumber, make, model):
        IDObject.__init__(self, objectId)
        self._license = licenseNumber
        self._make = make
        self._model = model

    def getLicenseNumber(self):
        return self._license

    def setLicenseNumber(self, licenseNumber):
        self._license = licenseNumber

    def getMake(self):
        return self._make

    def setMake(self, make):
        self._make = make

    def getModel(self):
        return self._model
    
    def setModel(self, model):
        self._model = model

    def __eq__(self, c):
        if isinstance(c, Car) == False:
            return False
        return self.getId() == c.getId()

    def __str__(self):
        return "Id: " + str(self.getId()) + ", License: " + self._license + ", Car type: " + self._make + ", " + self._model

    # def __str__(self):
    #    return "Id: " + str(self.getId()) + "," + self._make + ", "+self._model

    def __repr__(self):
        return str(self)

class CarValidator:
    
    def __init__(self):
        # and so on...
        self.__counties = ["AB", "B", "CJ"]
        self._errors = ""

    def _licensePlateValid(self, plate):
        token = str(plate).split(' ')
        if len(token) != 3:
            return False
        if token[0] not in self.__counties:
            return False
        try:
            n = int(token[1])
            if len(token[1]) < 2 or len(token[1]) > 3:
                return False
            if n < 1 or n > 999:
                return False
            if n > 99 and token[0] != "B":
                return False
        except TypeError:
            return False
        if len(token[2]) != 3:
            return False
        tu = str(token[2]).upper()
        if tu[0] in ['I', 'O']:
            return False
        for a in tu:
            if a < 'A' or a > 'Z':
                return False
            if a == 'Q':
                return False
        return True

    def validate(self, car):
        """
        Validate if provided Car instance is valid
        car - Instance of Car type
        Return List of validation errors. An empty list if instance is valid.
        """
        if isinstance(car, Car) == False:
            raise TypeError("Can only validate Car objects!")
        _errors = []
        if len(car.getMake()) == 0:
            _errors.append("Car must have a make")
        if len(car.getModel()) == 0:
            _errors.append("Car must have a model;")
        if self._licensePlateValid(car.getLicenseNumber()) == False:
            _errors.append("Bad license plate number;")
        if len(_errors) > 0:
            raise ValidatorException(_errors)
        return True

def testCar():
    #
    # Create a test for the Car class here
    #
    pass
    
def testCarValidator():
    #
    # Create a test for CarValidator here
    #
    pass
