'''
Created on Nov 13, 2015

@author: Vlad
'''
from Repositories.Repository import GenericRepository

class ClientRepository(GenericRepository):
	'''
	Repository for the clients
	'''
	def __init__(self):
		
		super().__init__()
	
	def find_by_id(self, id_client):

		for obj in self.get_all():
			if obj.id_client == id_client:
				return obj
		
		return None
	
	def delete(self, id_client):
		
		for obj in self._storage:
			if obj.id_client == id_client:
				self._storage.remove(obj)
				return
		
		raise KeyError("Object does not exist!")
		