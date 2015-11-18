class AddOperation:
    """
    Class that models an add operation 
    """
    def __init__(self, object):
        """
        Constructor for AddOperation class
        object - The object that was added
        """
        self._object = object
        
    def getObject(self):
        return self._object
    
class RemoveOperation:
    """
    Class that models a remove operation 
    """
    def __init__(self, object):
        """
        Constructor for RemoveOperation class
        object - The object that was removed
        """
        self._object = object
        
    def getObject(self):
        return self._object
        
class UpdateOperation:
    """
    Class that models an update operation 
    """
    def __init__(self, oldObject, updatedObject):
        """
        Constructor for UpdateOperation class
        oldObject - The instance before updating
        updatedObject - The instance after the update
        """
        self._oldObject = oldObject
        self._updatedObject = updatedObject
        
    def getOldObject(self):
        return self._oldObject

    def getUpdatedObject(self):
        return self._updatedObject