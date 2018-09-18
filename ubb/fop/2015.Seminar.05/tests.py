from domain.Medicine import *
from domain.MedicineException import *
from repository.MedicineRepository import MedicineRepository

def testMedicine():
    '''
    First we test getters & setters
    '''
    med = Medicine(1, "Aspirin", "BX Aspirin", 100, 10)
    assert med.getId() == 1
    assert med.getName() == "BX Aspirin"
    assert med.getActiveSubstance() == "Aspirin"
    assert med.getQuantity() == 100
    assert med.getPrice() == 10
    
    med.setPrice(9)
    med.setQuatity(200)
    med.setName("New Aspirin")
    
    assert med.getPrice() == 9
    assert med.getQuantity() == 200
    assert med.getName() == "New Aspirin"

    '''
    Test that we cannot set <0 price and quantity
    '''
    try:
        med.setQuatity(-2)
        assert False
    except MedicineException:
        pass
    
    try:
        med.setPrice(-2)
        assert False
    except MedicineException:
        pass    
    
    '''
    Test that a new Medicine cannot be buit using <0 price OR quantity
    '''
    try:
        m = Medicine(1, "Aspirin", "BX Aspirin", -1, 10)
        assert False
    except MedicineException:
        pass

    '''
    We need separate tests here, as we have to check that both situations generate exception
    '''
    try:
        m = Medicine(1, "Aspirin", "BX Aspirin", 90, -2)
        assert False
    except MedicineException:
        pass

def testRepository():
    repo = MedicineRepository()
    
    m1 = Medicine(1, "Aspirin", "BX Aspirin", 100, 10)
    m2 = Medicine(1, "Paracetamol", "MM Para", 80, 25)

    assert len(repo) == 0
    
    '''
    Test adding and retrieving medicines to/from repository
    '''
    repo.add(m1)
    assert len(repo) == 1
    assert repo.findById(1) == m1
    
    try:
        repo.add(m1)
        assert False
    except MedicineException:
        pass
    
    try:
        repo.add(m2)
        assert False
    except MedicineException:
        pass

    m2 = Medicine(2, "Paracetamol", "MM Para", 80, 25)
    repo.add(m2)
    
    assert len(repo) == 2
    assert repo.findById(1) == m1
    assert repo.findById(2) == m2
    
    '''
    Test removing medicines from repository
    '''
    assert len(repo) == 2
    repo.remove(1)
    assert len(repo) == 1
    
    assert repo.findById(2) == m2
    assert repo.findById(1) == None
    
    try:
        repo.remove(1)
        assert False
    except MedicineException:
        pass
    
    assert repo.remove(2) == m2
    assert len(repo) == 0  

def testController():
    """
    Please write a comprehensive test for the MedicineController here, using the examples provided above
    """

testMedicine()
testRepository()
testController()
