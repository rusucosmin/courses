from repository.Repository import Repository
from domain.Client import Client

class FileClientRepository(Repository):
    _fName = "clients.txt"

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
        client = Repository.delete(self, objectId)
        self._storeToFile()
        return client

    def _storeToFile(self):
        f = open(self._fName, "w")
        cars = Repository.getAll(self)
        for c in cars:
            cf = str(c.getId()) + ";" + c.getCNP() + ";" + c.getName() + "\n"
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
            c = Client(int(t[0]), t[1], t[2])
            Repository.store(self, c)
            line = f.readline().strip()
        f.close()
