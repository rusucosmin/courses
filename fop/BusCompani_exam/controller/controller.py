from model.route import Route
from model.exceptions import BusException

class Controller:
    '''
    Controller Class to control
    self.repo = the repository for our application
    '''
    def __init__(self, repository, f):
        self.repo = repository
        self.loadData(f)

    def loadData(self, f):
        '''
        function to load the data from file f into the repository
        :param f: the file
        '''
        corruptFile = False
        for line in f:
            args = line.split(',')
            cur = Route(int(args[0]), args[1], int(args[2]), int(args[3]))
            if cur.isValid() and self.checkUnique(cur):
                self.addRoute(cur)
            else:
                corruptFile = True
        return corruptFile

    def addRoute(self, route):
        self.repo.add(route)

    def checkUnique(self, cur):
        '''
        function to check is there is another bus route with the same id or the same route code (which should be unique)
        :param cur: the new route to check for 'duplicate'
        :return: True if there is such a route
                False if there isn't
        '''
        for x in self.repo.getRoutes():
            if not cur.checkUnique(x):
                return False
        return True

    def increaseWhere(self, lowerBound, delta):
        '''
        function to increase with delta buses all the routes with usage >= lowerBound
        :param lowerBound: an integer representing the lowerBound for upgrading
        :param delta: the amount of new buses for each route
        '''
        for x in self.repo.getRoutes():
            if x.getUsage() >= lowerBound:
                x.setBuses(x.getBuses() + 1)

    def removeBelow(self, upperBound):
        '''
        function to remove all the buses with usage <= upperBound
        :param upperBound:
        :return:
        '''
        for x in self.repo.getRoutes():
            if x.getUsage() <= upperBound:
                self.repo.remove(x)

    def getRoutes(self):
        '''
        Function to return all the routes
        :return:
        '''
        return self.repo.getRoutes()

    def saveState(self):
        self.repo.saveToFile()

    def update(self, curr):
        for x in self.getRoutes():
            if x == curr:
                x.setAttr(curr)