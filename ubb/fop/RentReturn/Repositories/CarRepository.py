'''
Created on Nov 13, 2015

@author: Vlad
'''

from Repositories.Repository import GenericRepository

class CarRepository(GenericRepository):
	def __init__(self):
		'''
		Repository for the cars
		'''
		
		super().__init__()
	
	def find_by_id(self, id_car):

		for obj in self._storage:
			if obj.id_car == id_car:
				return obj
			
		return None
	
	def delete(self, id_car):
		
		for obj in self._storage:
			if obj.id_car == id_car:
				self._storage.remove(obj)
				return
		
		raise KeyError("Object does not exist!")
		