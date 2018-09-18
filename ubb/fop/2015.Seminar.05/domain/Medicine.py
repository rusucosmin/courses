from domain.MedicineException import MedicineException

class Medicine:
    def __init__(self, id, activeSubstance, name, quantity, price):
        """
        Constructor method for medicine.
        """
        if price < 0 or quantity < 0:
            raise MedicineException("Medicine price and quantity must be >0")
        
        self._id = id
        self._activeSubstance = activeSubstance
        self._name = name
        self._quantity = quantity
        self._price = price

    def getId(self):
        """
        Return the id of the medicine. This is a read-only property as we do not have a setter
        """
        return self._id
    
    def getActiveSubstance(self):
        """
        Getter for active substance. This is a read-only property
        """
        return self._activeSubstance
    
    def getName(self):
        """
        Getter for medicine name
        """
        return self._name
    
    def setName(self, name):
        """
        Setter for medicine name
        """
        self._name = name 
        
    def getQuantity(self):
        """
        Getter for medicine quantity
        """
        return self._quantity
    
    def setQuantity(self, quantity):
        """
        Setter for medicine name.
        Input: quantity - a natural number
        """
        if quantity < 0:
            raise MedicineException("Medicine quantity must be >0")
        
        self._quantity = quantity
        
    def getPrice(self):
        """
        Getter for medicine price
        """
        return self._price
    
    def setPrice(self, price):
        """
        Setter for medicine price.
        Input: price - a natural number
        """
        if price < 0:
            raise MedicineException("Medicine price must be >0")
        
        self._price = price
        
    def __repr__(self):
        return str(self._id) + " substance=" + self._activeSubstance + ", name=" + self._name + ", quantity=" + str(self._quantity) + ", price=" + str(self._price)
