from model.route import Route

class Repository:
    '''
    Repository class:
        self.routes: an array of Routes to store all the data
    '''
    def __init__(self):
        self.routes = []

    def add(self, routeToAdd):
        '''
        Function to add a new route to the list
        :param routeToAdd:
        :return:
        '''
        self.routes.append(routeToAdd)

    def find(self, routeToFind):
        '''
        Function to find a route in the list(by id)
        :param routeToFind:
        :return:
        '''
        for route in self.routes:
            if route == routeToFind:
                return route
        return None

    def remove(self, routeToRemove):
        '''
        Function to remove a specific route from the list (by id)
        :param routeToRemove:
        :return:
        '''
        for i in range(len(self.routes)):
            if self.routes[i] == routeToRemove:
                del self.routes[i]
                return True
        return False

    def getRoutes(self):
        '''
        function to return the list of routes
        :return:
        '''
        return self.routes

    def saveToFile(self):
        '''
        function for persistency, to save the data from the memory into an external data base (.txt file)
        :return:
        '''
        with open("database.txt", "w") as f:
            for x in self.getRoutes():
                f.write(",".join(str(y) for y in [x.getId(), x.getRouteCode(), x.getUsage(), x.getBuses()]))
                f.write("\n")