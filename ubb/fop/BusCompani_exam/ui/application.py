from model.route import Route
from model.exceptions import BusException

from controller.controller import Controller
from repository.repository import Repository

class Application:
    Menu = [-1, 1, 2, 3, 4]
    def __init__(self, controller, repository):
        self.controller = controller
        self.repository = repository

    def showMenu(self):
        print("Hi, here are the available commands:\n")
        print("     1. Update data about a bus route, given its ID")
        print("     2. Update all bus routes whose usage percentages are above 85 by ")
        print("         increasing the number of buses on those routes by 1.")
        print("     3. Remove all bus routes whose usage percentages are below 20.")
        print("     4. List all buses")
        print("     -1. Exit")

    def getRouteFromInput(self):
        id = input("Insert id: ")
        rc = input("Insert Route Code: ")
        usage = input("Insert usage percent: ")
        buses = input("Insert the number of buses: ")
        return Route(int(id), rc, int(usage), int(buses))

    def run(self):
        while True:
            try:
                self.showMenu()
                op = int(input("Please insert the type of operation you want to do: "))
                while not op in Application.Menu:
                    op = int(input("Please insert the type of operation you want to do: "))
                if op == 1:
                    cur = self.getRouteFromInput()
                    self.controller.update(cur)
                elif op == 2:
                    self.controller.increaseWhere(85, 1)
                elif op == 3:
                    self.controller.removeBelow(20)
                elif op == 4:
                    print('\n\n'.join(str(x) for x in self.controller.getRoutes()))
                elif op == -1:
                    self.controller.saveState()
                    print("Thank you for using this software.\nCosmin Rusu")
                else:
                    print("Not implemented yet! :)")
            except ValueError as ve:
                print("Value should be integer!")
            except BusException as be:
                print(be)
            except Exception as e:
                print("There was a problem...")