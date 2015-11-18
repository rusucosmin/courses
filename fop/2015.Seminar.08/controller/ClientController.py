from domain.Client import Client
from controller.UndoableOperations import *

class ClientController:
    def __init__(self, undoController, validator, repository):
        self._undoController = undoController
        self._validator = validator
        self._repository = repository
        self._operations = []
        self._index = 0

    def create(self, clientId, cnp, name):
        client = Client(clientId, cnp, name)
        self._validator.validate(client)
        self._repository.store(client)
        '''
        If the operation did not raise an Exception, then we record it for Undo/Redo
        '''
        self._operations.append(AddOperation(client))
        self._index += 1
        self._undoController.recordUpdatedControllers([self])

    def delete(self, carId):
        client = self._repository.delete(carId)
        self._operations.append(RemoveOperation(client))
        self._index += 1
        self._undoController.recordUpdatedControllers([self])
        
    def update(self, car):
        oldClient = self._repository.find(car.getId())
        self._repository.update(car)
        self._operations.append(UpdateOperation(oldClient, car))
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
        
    def getClientCount(self):
        return len(self._repository)
        
    
        
            
        
