from repository.Repository import Repository
from domain.Car import Car

class FileCarRepository(Repository):
    _fName = "cars.txt"

    def __init__(self):
        Repository.__init__(self)
        self._loadFromFile()

    def store(self, e):
        Repository.store(self, e)
        self._storeToFile()

    def update(self, e):
        Repository.update(self, e)
        self._storeToFile()

    def delete(self, objectId):
        car = Repository.delete(self, objectId)
        self._storeToFile()
        return car

    def _storeToFile(self):
        f = open(self._fName, "w")
        cars = Repository.getAll(self)
        for c in cars:
            cf = str(c.getId()) + ";" + c.getLicenseNumber() + ";" + c.getMake() + ";" + c.getModel() + "\n"
            f.write(cf)
        f.close()

    def _loadFromFile(self):
        try:
            f = open(self._fName, "r")
        except IOError:
            return
        line = f.readline().strip()
        while line != "":
            t = line.split(";")
            c = Car(int(t[0]), t[1], t[2], t[3])
            Repository.store(self, c)
            line = f.readline().strip()
        f.close()
