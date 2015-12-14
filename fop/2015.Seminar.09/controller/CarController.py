from domain.Car import Car
from controller.UndoableOperations import *

class CarController:
    def __init__(self, undoController, validator, repository):
        self._undoController = undoController
        self._validator = validator
        self._repository = repository
        self._operations = []
        self._index = 0
        
    def create(self, clientId, licenseNumber, make, model):
        car = Car(clientId, licenseNumber, make, model)
        self._validator.validate(car)
        self._repository.store(car)
        '''
        If the operation did not raise an Exception, then we record it for Undo/Redo
        '''
        self._operations.append(AddOperation(car))
        self._index += 1
        self._undoController.recordUpdatedControllers([self])
        
    def delete(self, carId):
        car = self._repository.delete(carId)
        self._operations.append(RemoveOperation(car))
        self._index += 1
        self._undoController.recordUpdatedControllers([self])
        
    def findByID(self, clientId):
        return self._repository.find(clientId)
        
    def filter(self, make, model):
        return self._repository.filter(make, model)
        
    def update(self, car):
        oldCar = self._repository.find(car.getId()) 
        self._repository.update(car)
        self._operations.append(UpdateOperation(oldCar, car))
        self._index += 1
        self._undoController.recordUpdatedControllers([self])
        
    def undo(self):
        """
        Undo the last client operation that changed the set of clients
        Returns True if operation was undone, False otherwise
        """
        if self._index == 0:
            return False
    
        self._index -= 1
        operation = self._operations[self._index]
    
        if isinstance(operation, AddOperation):
            self._repository.delete(operation.getObject().getId())
        elif isinstance(operation, RemoveOperation):
            self._repository.store(operation.getObject())
        else:
            self._repository.update(operation.getOldObject())
        
    def redo(self):
        """
        Similar to undoController, only in the opposite direction
        """
        pass
        
    def getCarCount(self):
        return len(self._repository)