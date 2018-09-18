import unittest
from repository.Repository import Repository
from domain.Client import Client
from repository.RepositoryException import RepositoryException

class RepositoryTest(unittest.TestCase):
    '''
    Unit test case example for Repository
    '''
    def setUp(self):
        self._repo = Repository()
    
    def testRepo(self):
        self.assertEqual(len(self._repo), 0)
        c = Client("1", "1840101223366", "Anna")
        self._repo.store(c)
        self.assertEqual(len(self._repo), 1)
        self.assertRaises(RepositoryException , self._repo.store, c)
        
        c = Client("2", "1840101223366", "Anna")
        self._repo.store(c)
        self.assertEqual(len(self._repo), 2)
        '''
        And so on for the other Repository operations
        '''