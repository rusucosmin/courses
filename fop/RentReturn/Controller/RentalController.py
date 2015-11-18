'''
Created on Nov 13, 2015

@author: Vlad
'''
from Domain.Rental import Rental

class RentalController:
	
	def __init__(self, client_repo, car_repo, rental_repo):
		
		self.__client_repo = client_repo
		self.__car_repo = car_repo
		self.__rental_repo = rental_repo
		
	def add(self, id_client, id_car, price):
		
		client = self.__client_repo.find_by_id(id_client)
		if client is None:
			raise ValueError("No such client exists!")
		
		car = self.__car_repo.find_by_id(id_car)
		if car is None:
			raise ValueError("No such car exists!")
		
		rental = Rental(client, car, price)
		
		# TODO: validate rental (client and car can be passed to the validator and exceptions on them raised there)
		
		self.__rental_repo.add(rental)
		
	def get_all(self):
		
		all_dto = self.__rental_repo.get_all_DTO()
		
		all_rentals = [Rental(self.__client_repo.find_by_id(dto.id_client), self.__car_repo.find_by_id(dto.id_car), dto.price) for dto in all_dto]
		
		return all_rentals

	def delete(self, id_client, id_car):
		
		self.__rental_repo.delete(id_client, id_car)
		
	def delete_by_client(self, id_client):
		
		self.__rental_repo.delete_by_client(id_client)
		
	def delete_by_car(self, id_car):
		
		self.__rental_repo.delete_by_car(id_car)