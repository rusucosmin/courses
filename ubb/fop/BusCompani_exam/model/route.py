class Route:
    '''
    Class to encapsulate our data and to make it easy for us to maintain it
    '''
    def __init__(self, id, route, usage, buses):
        self.id = id
        self.routeCode = route
        self.usage = usage
        self.buses = buses

    def __str__(self):
        x = "Bus id = " + str(self.id)
        x = x + "\nRoute Code = " + str(self.routeCode)
        x = x + "\nUsage percent = " + str(self.usage)
        x = x + "\nNumber of Buses = " + str(self.buses)
        return x

    def __repr__(self):
        return str(self)

    '''
    Getter and setters
    '''
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setRouteCode(self, route):
        self.routeCode = route

    def getRouteCode(self):
        return self.routeCode

    def setUsage(self, usage):
        self.usage = usage

    def getUsage(self):
        return self.usage

    def setBuses(self, buses):
        self.buses = buses

    def getBuses(self):
        return self.buses

    def __eq__(self, other):
        if not isinstance(other, Route):
            return False
        return self.getId() == other.getId()

    def checkUnique(self, other):
        '''
        function to check if two routes have the same id or the save code (which, by definition should be unique)
        :param other: the comparision is made between self and other using the == operator
        :return:    True if they share at least one duplicate property
                    False otherwise
        '''
        if not isinstance(other, Route):
            return True
        if self.getId() == other.getId() or self.getRouteCode() == other.getRouteCode():
            return False
        return True

    def isValid(self):
        '''
        Function to check if a route is valid, by the definition
        :return: True if it is valid,
                 False otherwise
        '''
        if len(self.getRouteCode()) > 3:
            return False
        if self.getUsage() < 0 or self.getUsage() > 100:
            return False
        return True

    def setAttr(self, other):
        '''
        Funciton to set the attr of another route to self
        :param other:
        :return:
        '''
        self.id = other.getId()
        self.buses = other.getBuses()
        self.routeCode = other.getRouteCode()
        self.usage = other.getUsage()