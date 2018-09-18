import unittest
from domain.Car import CarValidator, Car
from domain.ValidatorException import ValidatorException

class CarValidatorTestCase(unittest.TestCase):
    '''
    A unit test example
    '''
    def setUp(self):
        self.v = CarValidator()
        self.c = Car("1", "AB 01 RTY", "Dacia", "Duster")
    
    def testCarValidator(self):
        self.assertTrue(self.v.validate, self.c)
        self.c.setMake("")
        self.assertRaises(ValidatorException, self.v.validate, self.c)
        self.c.setMake("Dacia")
        self.c.setModel("")
        self.assertRaises(ValidatorException, self.v.validate, self.c)        

    def testCarLicenseValidatorBlackBox(self):
        self.c.setLicenseNumber("AB 01 ABC")
        self.assertTrue(self.v.validate, self.c)
        
        self.c.setLicenseNumber("B 101 ABC")
        self.assertTrue(self.v.validate, self.c)
        
        self.c.setLicenseNumber("TY 01 ABC")
        self.assertTrue(self.v.validate, self.c)
                
        self.c.setLicenseNumber("CJ 121 AABC")
        self.assertTrue(self.v.validate, self.c)
        '''
        and so on...
        '''

    def testCarLicenseValidatorWhiteBox(self):
        '''
        Testing for license plate tokens
        '''
        self.c.setLicenseNumber("")
        self.assertRaises(ValidatorException, self.v.validate, self.c)
        self.c.setLicenseNumber("CJ 01")
        self.assertRaises(ValidatorException, self.v.validate, self.c)        
        self.c.setLicenseNumber("CJ 02 AAB S")
        self.assertRaises(ValidatorException, self.v.validate, self.c)
        self.c.setLicenseNumber("AB 02 MMS")
        self.assertTrue(self.v.validate, self.c)
        '''
        Testing for counties
        '''
        self.c.setLicenseNumber("X 02 MMS")
        self.assertRaises(ValidatorException, self.v.validate, self.c)
        self.c.setLicenseNumber("XMAS 02 MMS")
        self.assertRaises(ValidatorException, self.v.validate, self.c)                
        '''
        Testing for number part
        '''
        self.c.setLicenseNumber("AB 223 MKJ")
        self.assertRaises(ValidatorException, self.v.validate, self.c)
        self.c.setLicenseNumber("B 1 MKJ")
        self.assertRaises(ValidatorException, self.v.validate, self.c)        
        '''
        Testing for special Bucharest case
        '''
        self.c.setLicenseNumber("AB 223 MKJ")
        self.assertRaises(ValidatorException, self.v.validate, self.c)
        self.c.setLicenseNumber("B 223 MKJ")
        self.assertTrue(self.v.validate, self.c)
        '''
        Test for letter combination length & validity
        '''
        self.c.setLicenseNumber("AB 22 AA")
        self.assertRaises(ValidatorException, self.v.validate, self.c)
        self.c.setLicenseNumber("CJ 23 AAAB")
        self.assertRaises(ValidatorException, self.v.validate, self.c)
        self.c.setLicenseNumber("AB 22 AAQ")
        self.assertRaises(ValidatorException, self.v.validate, self.c)
        self.c.setLicenseNumber("CJ 23 IOP")
        self.assertRaises(ValidatorException, self.v.validate, self.c)
        self.c.setLicenseNumber("CJ 23 OIP")
        self.assertRaises(ValidatorException, self.v.validate, self.c)
