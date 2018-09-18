from controller.UndoController import UndoController
from repository.Repository import Repository
from domain.Client import ClientValidator
from controller.ClientController import ClientController
from controller.CarController import CarController
from domain.Car import CarValidator
from domain.Rental import RentalValidator
from controller.RentalController import RentalController
from _datetime import datetime

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
    clientRepo = Repository()
    clientValidator = ClientValidator()
    clientController = ClientController(undoController, clientValidator, clientRepo)
    
    clientController.create(100, "1820203556699", "Aaron")
    clientController.create(101, "2750102885566", "Bob")
    clientController.create(102, "1820604536579", "Carol")

    # We name the instances so it's easier to create some test values later
    aaron = clientRepo.find(100)
    bob = clientRepo.find(101)
    carol = clientRepo.find(102)

    '''
    Start car Controller
    '''
    carRepo = Repository()
    carValidator = CarValidator()
    carController = CarController(undoController, carValidator, carRepo)

    carController.create(200, "CJ 01 AAA", "Audi", "A3")
    carController.create(201, "CJ 01 BBB", "Audi", "A4")
    carController.create(202, "CJ 01 CCC", "Audi", "A5")
    carController.create(203, "CJ 01 DDD", "Audi", "A6")

    audiA3 = carRepo.find(200)
    audiA4 = carRepo.find(201)
    audiA5 = carRepo.find(202)
    audiA6 = carRepo.find(203)

    '''
    Start rental Controller
    '''
    rentRepo = Repository()
    rentValidator = RentalValidator()
    rentController = RentalController(undoController, rentValidator, rentRepo, carRepo, clientRepo)

    rentController.createRental(300, aaron, audiA3, datetime.strptime("2015-11-20", "%Y-%m-%d"), datetime.strptime("2015-11-22", "%Y-%m-%d"))
    rentController.createRental(301, carol, audiA5, datetime.strptime("2015-11-24", "%Y-%m-%d"), datetime.strptime("2015-11-25", "%Y-%m-%d"))
    rentController.createRental(302, carol, audiA6, datetime.strptime("2015-12-10", "%Y-%m-%d"), datetime.strptime("2015-12-12", "%Y-%m-%d"))
    rentController.createRental(303, aaron, audiA4, datetime.strptime("2015-11-21", "%Y-%m-%d"), datetime.strptime("2015-11-25", "%Y-%m-%d"))
    rentController.createRental(304, aaron, audiA3, datetime.strptime("2015-11-24", "%Y-%m-%d"), datetime.strptime("2015-11-27", "%Y-%m-%d"))
    rentController.createRental(305, bob, audiA5, datetime.strptime("2015-11-26", "%Y-%m-%d"), datetime.strptime("2015-11-27", "%Y-%m-%d"))
    rentController.createRental(306, carol, audiA6, datetime.strptime("2015-12-15", "%Y-%m-%d"), datetime.strptime("2015-12-20", "%Y-%m-%d"))
    rentController.createRental(307, bob, audiA4, datetime.strptime("2015-12-01", "%Y-%m-%d"), datetime.strptime("2015-12-10", "%Y-%m-%d"))
    rentController.createRental(308, carol, audiA4, datetime.strptime("2015-12-11", "%Y-%m-%d"), datetime.strptime("2015-12-15", "%Y-%m-%d"))
    rentController.createRental(309, aaron, audiA5, datetime.strptime("2015-11-28", "%Y-%m-%d"), datetime.strptime("2015-12-02", "%Y-%m-%d"))

    for cr in rentController.mostRentedCars(): 
        print (cr)
        
statisticsExample()
