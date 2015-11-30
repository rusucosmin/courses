from controller.CarController import CarController
from controller.ClientController import ClientController
from controller.RentalController import RentalController
from controller.UndoController import UndoController
from domain.Car import CarValidator
from domain.Client import ClientValidator
from domain.Rental import RentalValidator
from repositor.FileCarRepository import FileCarRepository
from repositor.FileClientRepository import FileClientRepository
from repositor.FileRentalRepository import FileRentalRepository

def statisticsExample():
    """
    An example for the creation of statistics.
    Several cars, clients and rentals are created and then a statistics is calculated over them.
    
    Follow the code below and figure out how it works!
    """
    undoController = UndoController()
    
    '''
    Start client Controller
    '''
    clientRepo = FileClientRepository()
    clientValidator = ClientValidator()
    clientController = ClientController(undoController, clientValidator, clientRepo)
    
    '''
    Start car Controller
    '''
    carRepo = FileCarRepository()
    carValidator = CarValidator()
    carController = CarController(undoController, carValidator, carRepo)

    '''
    Start rental Controller
    '''
    rentRepo = FileRentalRepository(clientRepo, carRepo)
    rentValidator = RentalValidator()
    rentController = RentalController(undoController, rentValidator, rentRepo, carRepo, clientRepo)

    '''
    Print each statistics item
    '''
    for cr in rentController.mostRentedCars(): 
        print (cr)
        
statisticsExample()
