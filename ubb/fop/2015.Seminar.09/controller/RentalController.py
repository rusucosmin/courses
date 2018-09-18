from controller.UndoableOperations import *
from domain.CarRentalException import CarRentalException
from domain.Rental import *

class RentalController:
    """
    Controller for rental operations
    """
    def __init__(self, undoController, validator, rentalRepo, carRepo, clientRepo):
        self._undoController = undoController 
        self._validator = validator
        self._repository = rentalRepo
        self._carRepo = carRepo
        self._cliRepo = clientRepo
        self._operations = []
        self._index = 0

    def createRental(self, rentalId, client, car, start, end):
        """
        Create a rental using the provided data
        rentalId - id of the new rental
        client - The client that will rent the car
        car - The car to be rented
        start, end - The endpoints of the rental
        """
        rental = Rental(rentalId, start, end, client, car)
        self._validator.validate(rental)
        
        '''
        Check the car's availability for the given period 
        '''
        if self.isCarAvailable(car, start, end) == False:
            raise CarRentalException("Car is not available during that time!")

        self._repository.store(rental)
        '''
        If the operation did not raise an Exception, then we record it for Undo/Redo
        '''
        self._operations.append(AddOperation(rental))
        self._index += 1
        self._undoController.recordUpdatedControllers([self])

    def isCarAvailable(self, car, start, end):
        """
        Check the availability of the given car to be rented in the provided time period
        car - The availability of this car is verified
        start, end - The time span. The car is available if it is not rented in this time span
        Return True if the car is available, False otherwise
        """
        rentals = self.filterRentals(None, car)
        for rent in rentals:
            if start > rent.getEnd() or end < rent.getStart():
                continue
            return False
        return True

    def filterRentals(self, client, car):
        """
        Return a list of rentals performed by the provided client for the provided car
        client - The client performing the rental. None means all clients
        cars - The rented car. None means all cars 
        """
        result = []
        for rental in self._repository.getAll():
            if client != None and rental.getClient() != client:
                continue
            if car != None and rental.getCar() != car:
                continue
            result.append(rental)
        return result
        
    def mostRentedCars(self):
        """
        Returns an ordered list of the cars in their 'most rented' order, by total number of rental days 
        """
        result = []

        '''
        1. Build the data transfer object
        '''
        for car in self._carRepo.getAll():
            rentals = self.filterRentals(None, car)
            result.append(CarRentals(car, rentals))
            
        '''
        2. Sort it
        '''
        result.sort()
        return result

    def undo(self):
        """
        Undo the last client operation that changed the set of clients
        Returns True if operation was undone, False otherwise
        """
        if self._index == 0:
            return False
    
        self._index -= 1
        operation = self._operations[self._index]

        '''
        Rentals can only be created, so the only type of supported operation is the AddOperation
        '''
        self._repository.delete(operation.getObject().getId())

        
    def redo(self):
        """
        Similar to undoController, only in the opposite direction
        """
        pass

class CarRentals:
    def __init__(self, car, rentals):
        """
        Constructor for this data transfer object
        car - The car for this object
        rentals - The list of rentals where the given car was rented  
        """
        self._car = car
        self._rentals = rentals

    def getCar(self):
        return self._car
    
    def getRentals(self):
        return self._rentals
    
    def __lt__(self, carRental):
        """
        < operator required for the sort
        """
        return self.getRentalDays() < carRental.getRentalDays()
    
    def __str__(self):
        return str(self.getRentalDays()) + " for car " + str(self._car)
    
    def __repr__(self):
        return str(self)    
    
    def getRentalDays(self):
        """
        Returns the number of days the car was rented
        """
        d = 0
        for rental in self._rentals:
            d += len(rental)
        return d

def testRentalController():
    """
    I do not have to be specified :)
    """
    pass
    
