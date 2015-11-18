'''
Created on Nov 13, 2015

@author: Vlad
'''

from Repositories.Repository import GenericRepository
from Domain.RentalDTO import RentalDTO

class RentalRepository(GenericRepository):
	'''
	Repository for the rentals
	'''
	def __init__(self):

		super().__init__()
		
	def find_by_id(self, id_client, id_car):
		'''
		Funtion to return the object rental object of a specific id_client, and id_car
		:param id_client:
		:param id_car:
		:return:
		'''
		for obj in self.get_all():
			if obj.id_client == id_client and obj.id_car == id_car:
				return obj
		
		return None
		
	def find_by_client(self, id_client):
		return [RentalDTO(obj.id_client, obj.id_car, obj.price) for obj in self.get_all() if obj.id_client == id_client]

	def find_by_car(self, id_car):
		return [RentalDTO(obj.id_client, obj.id_car, obj.price) for obj in self.get_all() if obj.id_car == id_car]
	
	def add(self, rental):
		
		if self.find_by_id(rental.client.id_client, rental.car.id_car) is not None:
			raise KeyError("Rental already exists!")
	
		dto = RentalDTO(rental.client.id_client, rental.car.id_car, rental.price)
		self._storage.append(dto)
		
	def __del(self, condition):
	
		len_before = len(self._storage)
		self._storage = [rental for rental in self._storage if not condition(rental)]
		
		return len_before != len(self._storage)
	
	def delete(self, id_client, id_car):
		
		if not self.__del(lambda x: x.id_client == id_client and x.id_car == id_car):
			raise KeyError("There are no rentals for that client and car!")
	
	def delete_by_client(self, id_client):
	
		if not self.__del(lambda x: x.id_client == id_client):
			raise KeyError("There are no rentals for that client!")
	
	def delete_by_car(self, id_car):
	
		if not self.__del(lambda x: x.id_car == id_car):
			raise KeyError("There are no rentals for that car!")
		
	
		
	
	def get_all_DTO(self):
		
		return [RentalDTO(obj.id_client, obj.id_car, obj.price) for obj in self.get_all()]