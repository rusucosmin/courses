from datetime import *
from repository.Repository import Repository
from domain.Rental import Rental

class FileRentalRepository(Repository):
    _fName = "rentals.txt"

    def __init__(self, clientRepo, carRepo):
        Repository.__init__(self)
        self._carRepo = carRepo
        self._clientRepo = clientRepo
        self._loadFromFile()

    def store(self, e):
        Repository.store(self, e)
        self._storeToFile()

    def update(self, e):
        Repository.update(self, e)
        self._storeToFile()

    def delete(self, objectId):
        Repository.delete(self, objectId)
        self._storeToFile()

    def _storeToFile(self):
        f = open(self._fName, "w")
        rentals = Repository.getAll(self)
        for r in rentals:
            rl = str(r.getId()) + ";" + str(r.getClient().getId()) + ";" + str(r.getCar().getId()) + ";" + r.getStart().strftime("%Y-%m-%d") + ";" + r.getEnd().strftime("%Y-%m-%d") + "\n"
            f.write(rl)
        f.close()

    def _loadFromFile(self):
        try:
            f = open(self._fName, "r")
        except IOError:
            return
        line = f.readline().strip()
        while line != "":
            t = line.split(";")
            
            car = self._carRepo.find(int(t[1]))
            client = self._clientRepo.find(int(t[2]))
            
            c = Rental(t[0], datetime.strptime(t[3], "%Y-%m-%d"), datetime.strptime(t[4], "%Y-%m-%d"), client, car)
            Repository.store(self, c)
            line = f.readline().strip()
        f.close()
