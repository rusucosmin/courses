from _datetime import datetime
from datetime import date

from controller.CarController import CarController
from controller.ClientController import ClientController
from controller.RentalController import RentalController
from controller.UndoController import UndoController
from domain.Car import CarValidator, Car
from domain.Client import ClientValidator, Client
from domain.Rental import RentalValidator, Rental
from repository.Repository import Repository


def undoExample():
    """
    An example for doing multiple undo operations. 
    This is a bit more difficult than in Lab2-4 due to the fact that there are now several controllers, 
    and each of them can perform operations that require undo support.
     
    Follow the code below and figure out how it works!
    """
    
    undoController = UndoController()
    
    '''
    Start client Controller
    '''
    clientRepo = Repository()
    clientValidator = ClientValidator()
    clientController = ClientController(undoController, clientValidator, clientRepo)
    
    '''
    Start car Controller
    '''
    carRepo = Repository()
    carValidator = CarValidator()
    carController = CarController(undoController, carValidator, carRepo)
    
    '''
    Start rental Controller
    '''
    rentRepo = Repository()
    rentValidator = RentalValidator()
    rentController = RentalController(undoController, rentValidator, rentRepo, carRepo, clientRepo)
    
    print("---> Initial state of repositories")
    print(clientRepo)
    print(carRepo)
    print(rentRepo)
    
    '''
    We add a client, a new car as well as a rental
    '''
    clientController.create(103, "1900102035588", "Dale")
    carController.create(201, "CJ 02 ZZZ", "Dacia", "Sandero")
    
    rentStart = datetime.strptime("2015-11-26", "%Y-%m-%d")
    rentEnd = datetime.strptime("2015-11-30", "%Y-%m-%d")
    rentController.createRental(301, clientRepo.find(103), carRepo.find(201), rentStart, rentEnd)
    
    print("---> We added a client, a new car and a rental")
    print(clientRepo)
    print(carRepo)
    print(rentRepo)
    
    '''
    Now undo the performed operations, one by one
    '''
    undoController.undo()
    print("---> After 1 undo")
    print(clientRepo)
    print(carRepo)
    print(rentRepo)
    
    
    undoController.undo()
    print("---> After 2 undos")
    print(clientRepo)
    print(carRepo)
    print(rentRepo)
    
    undoController.undo()
    print("---> After 3 undos")
    print(clientRepo)
    print(carRepo)
    print(rentRepo)

undoExample()