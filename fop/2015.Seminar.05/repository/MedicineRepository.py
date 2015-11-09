from domain.Medicine import MedicineException

class MedicineRepository:

    def __init__(self):
        """
        Constructor for MedicineRepository class
        """
        self._data = []

    def add(self, medicine):
        """
        Add a medicine to the repository
        Input: medicine - Medicine to be added
        Raises MedicineException in case of duplicate id
        """
        if self._find(medicine.getId()) != -1:
            raise MedicineException("Medicine with id - " + str(id) + " already exists")

        self._data.append(medicine)

    def _find(self, id):
        """
        Return the index of the medicine having the given id
        Input: id - the id of the medicine we search for
        Output: Index of the medicine in the repository's list if found, -1 otherwise
        """
        for i in range(0, len(self._data)):
            if self._data[i].getId() == id:
                return i
        return -1

    def findById(self, id):
        """
        Return the medicine having the given id
        Input: id - The id that we search for
        Output: The medicine if found, None otherwise
        """
        index = self._find(id)
        if index == -1:
            return None
        return self._data[index]

    def __len__(self):
        """
        Overriding the len() built-in function
        """
        return len(self._data)
    
    def remove(self, id):
        """
        Remove the medicine having the given id
        Input: index - A natural number between 0 and the repo size
        Output: The medicine that was removed
        MedicineException is raised if a medicine having the given id does not exist
        """
        index = self._find(id)
        if index == -1:
            raise MedicineException("Medicine having id - " + str(id) + " is not in repository")
        return self._data.pop(index)
        
    def removeAll(self):
        """
        Remove all data from repository
        """
        self._data.clear()

    def getAll(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return self._data
