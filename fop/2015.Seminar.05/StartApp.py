from repository.MedicineRepository import MedicineRepository
from controller.MedicineController import MedicineController
from ui.UI import *


repository = MedicineRepository()

repository.add(Medicine(1, "aspirin", "AX Aspirin", 100, 5))
repository.add(Medicine(5, "aspirin", "Final Aspirin", 100, 4))
repository.add(Medicine(6, "aspirin", "Easy Aspirin", 100, 8))
repository.add(Medicine(2, "vitamin C", "C Plus (Plus?)", 200, 4))
repository.add(Medicine(3, "vitamin B", "Micro B Vitamins", 154, 6))
repository.add(Medicine(4, "magnesium", "Magnesium +", 70, 60))

controller = MedicineController(repository)
ui = UI(controller)

ui.mainMenu()
