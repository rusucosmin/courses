from domain.MedicineException import MedicineException

class MedicineController:
    def __init__(self, repo):
        self._repo = repo
    
    def addMedicine(self, medicine):
        """
        Add a new medicine
        Input: medicine - the medicine that will be added
        Raises MedicineException in case of duplicate medicine id.
        """
        self._repo.add(medicine)
    
    def removeMedicine(self, id):
        """
        Remove the medicine with the given id
        Input: id - the id of the medicine to remove
        Raises MedicineException in case medicine having the given id does not exist
        """
        self._repo.remove(id)
    
    def getAll(self):
        return self._repo.getAll()
    
    def findMedicineByName(self, name):
        """
        Find all medicines having the given name
        Input: name - the name of the medicine being searched for
        Output: List of medicines having the given name.
        """
        result = []
        for m in self._repo.getAll():
            if name == m.getName():
                result.append(m)
        return result

    def findMedicineById(self, id):
        for m in self._repo.getAll():
            if id == m.getId():
                return m
        raise MedicineException("No medicine with the given id found")
    
    def getMedicinesByActiveSubstance(self, activeSubstance):
        """
        Returns a sorted list of medicines having the given active substance. The list is sorted ascending by price.
        Input: activeSubstance - the active substance searched for
        Output: a list of medicines, sorted ascending by price, having the same active substance 
        """
        result = []
        for m in self._repo.getAll():
            if activeSubstance == m.getActiveSubstance():
                result.append(m)
        
        sortFlag = False
        while not sortFlag:
            sortFlag = True
            for i in range(0, len(result) - 1):
                if result[i].getPrice() > result[i + 1].getPrice():
                    result[i], result[i + 1] = result[i + 1], result[i]
                    sortFlag = False
        return result

    def buyMedicine(self, medId, medAm):
        m = self.findMedicineById(medId)
        if m.getQuantity() <= medAm:
            raise MedicineException("Medicine not available in quantity!")
        else:
            m.setQuantity(m.getQuantity() - medAm)
            print("Medicine bought, remaining ", m.getQuantity())
