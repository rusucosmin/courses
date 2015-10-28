__author__ = 'cosmin'

from model.book import Book
from model.client import Client
from model.loan import Loan

class LibraryApplication:
    def __init__(self, controller):
        self._controller = controller

    def run(self):
        while True:
            self.showMenu()
            goodOpt = False
            while not goodOpt:
                try:
                    opt = int(input("Type a command number: "))
                    if opt not in [1, 2, 3, 4, 10]:
                        print("Please choose one of the number from the command list.")
                    else:
                        goodOpt = True
                except Exception:
                    print("The number should be an integer!")
            if opt == 1:
                self._controller.addBook(self.getBookFromInput())
            elif opt == 2:
                self._controller.addClient(self.getClientFromInput())
            elif opt == 3:
                self._controller.listBooks()
            elif opt == 4:
                self._controller.listClients()
            elif opt == 10:
                self._controller.saveHistory()
                break


    def getBookFromInput(self):
        return Book("ito", "Introduction to algorithms", "The Bible", "T.H.Cormen")

    def getClientFromInput(self):
        return Client("1960715060015", "Rusu Cosmin")

    def showMenu(self):
        print("Here are the commands:")
        print("     1. add Book")
        print("     2. add Client")
        print("     3. list Books")
        print("     4. list Clients")