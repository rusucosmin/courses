'''
Created on Nov 13, 2015

@author: Vlad
'''
from Repositories.Repository import GenericRepository
from Repositories.RentalRepository import RentalRepository
from Controller.ClientController import ClientController
from Controller.CarController import CarController
from Controller.RentalController import RentalController
from UI.Console import Console
from Domain.Client import Client
from Domain.Car import Car
from Repositories.ClientRepository import ClientRepository
from Repositories.CarRepository import CarRepository


repo_clients = ClientRepository()
repo_clients.add(Client("1", "client1"))
repo_clients.add(Client("2", "client2"))
repo_clients.add(Client("3", "client3"))

repo_cars = CarRepository()
repo_cars.add(Car("1", "car1"))
repo_cars.add(Car("2", "car2"))
repo_cars.add(Car("3", "car3"))

repo_rentals = RentalRepository()

ctrl_clients = ClientController(repo_clients)
ctrl_cars = CarController(repo_cars)
ctrl_rentals = RentalController(repo_clients, repo_cars, repo_rentals)

ui = Console(ctrl_cars, ctrl_clients, ctrl_rentals)

ui.show()