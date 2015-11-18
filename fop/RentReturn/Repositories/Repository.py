'''
Created on Nov 13, 2015

@author: Vlad
'''

class GenericRepository:
	'''
	GenericRepository, which is a base class for all other repositories
	'''
	def __init__(self):
		
		self._storage = []
		
	def add(self, obj):
		'''
		Function to handle the add for every repository
		:param obj:
		:return:
		'''
		if obj in self._storage:
			raise KeyError("Duplicate object!")
		
		self._storage.append(obj)
		
	def update(self, obj):
		'''
		Function to update the object
		:param obj:
		:return:
		'''
		if obj not in self._storage:
			raise KeyError("Object does not exist!")
		
		for i in range(len(self._storage)):
			if self._storage[i] == obj:
				self._storage[i] = obj
		
	def get_all(self):
		'''
		Function to get the content of all the repositories
		:return: a list of objects
		'''
		return self._storage