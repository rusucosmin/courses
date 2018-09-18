from domain.Medicine import Medicine
from domain.MedicineException import MedicineException

class UI:
    def __init__(self, controller):
        self._controller = controller

    def _printMenu(self):
        str = '\nAvailable commands:\n'
        str += '\t 1 - Add medicine\n'
        str += '\t 2 - Remove medicine\n'
        str += '\t 3 - Find medicine by name\n'
        str += '\t 4 - Display medicines with the given active substance\n'
        str += '\t 5 - Buy medicine\n'
        str += '\t 0 - Exit\n'
        print(str)

    def _addMedicineMenu(self):
        id = UI._readPositiveInteger("Medicine id =")
        substance = input("Active substance =")
        name = input("Medicine name =")
        quantity = UI._readPositiveInteger("Medicine quantity =")
        price = UI._readPositiveInteger("Medicine price =")

        med = Medicine(id, substance, name, quantity, price)
        self._controller.addMedicine(med)
    
    def _removeMedicineMenu(self):
        self._printMedicineList(self._controller.getAll())
        id = self._readPositiveInteger("Medicine id=")
        self._controller.removeMedicine(id)
    
    def _findMedicineMenu(self):
        name = input("Medicine name =")
        print("Found medicine(s):")
        print(self._controller.findMedicineByName(name))
    
    def _showMedicinesByActiveSubstanceMenu(self):
        activeSubstance = input("Medicine active substance =")
        self._printMedicineList(self._controller.getMedicinesByActiveSubstance(activeSubstance))
        
    def _buyMedicineMenu(self):
        medId = self._readPositiveInteger("Please input the id of the medicine!")
        amonut = self._readPositiveInteger("Please input the amount of the medicine!")
        self._controller.buyMedicine(medId, amount)

    def _printMedicineList(self, list):
        print("Medicines:")
        for m in list:    
            print(m)
    
    def mainMenu(self):
        keepAlive = True
        while keepAlive:
            self._printMedicineList(self._controller.getAll())
            self._printMenu()
            command = input("Enter command: ").strip()
            try: 
                if command == '0':
                    print("exit...")
                    keepAlive = False
                elif command == '1':
                    self._addMedicineMenu()
                elif command == '2':
                    self._removeMedicineMenu()
                elif command == '3':
                    self._findMedicineMenu()
                elif command == '4':
                    self._showMedicinesByActiveSubstanceMenu()
                elif command == '5':
                    self._buyMedicineMenu()
                else:
                    print("Invalid commnad!")
            except MedicineException as e:
                print(e)
                
    @staticmethod
    def _readPositiveInteger(msg):
        """
        Reads a positive integer
        Input: -
        Output: A positive integer
        """
        result = None
        while result == None:
            try:
                result = int(input(msg))
                if result < 0:
                    raise ValueError
            except ValueError:
                print("Please input a positive integer!")
        return result
