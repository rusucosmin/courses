from repository.RepositoryException import RepositoryException

class Repository:
    """
    Repository for storing IDObject instances
    """
    def __init__(self):
        self._objects = []

    def store(self, obj):
        if self.find(obj.getId()) != None:
            raise RepositoryException("Element having id=" + str(obj.getId()) + " already stored!")
        self._objects.append(obj)

    def update(self, object):
        """
        Update the instance given as parameter. The provided instance replaces the one having the same ID
        object - The object that will be updated
        Raises RepositoryException in case the object is not contained within the repository
        """
        el = self.find(object.getId())
        if el == None:
            raise RepositoryException("Element not found!")
        idx = self._objects.index(el)
        self._objects.remove(el)
        self._objects.insert(idx, object)

    def find(self, objectId):
        for e in self._objects:
            if objectId == e.getId():
                return e
        return None

    def delete(self, objectId):
        """
        Remove the object with given objectId from repository
        objectId - The objectId that will be removed
        Returns the object that was removed
        Raises RepositoryException if object with given objectId is not contained in the repository
        """
        object = self.find(objectId)
        if object == None:
            raise RepositoryException("Element not in repository!")
        self._objects.remove(object)
        return object

    def getAll(self):
        return self._objects;

    def __len__(self):
        return len(self._objects)

    def __str__(self):
        r = "Repository:\n"
        for e in self._objects:
            r += str(e)
            r += "\n"
        return r
