class IDObject():
    """
    Base class for all objects having unique id within the application
    """
    def __init__(self, objectId):
        """
        Constructor method for building IDObject
        objectId - the unique objectId of the object in the application
        """
        self._objectId = objectId
        
    def getId(self):
        """
        Return the object's unique id
        """
        return self._objectId

def testIDObject():
    obj = IDObject(133)
    assert obj.getId() == 133