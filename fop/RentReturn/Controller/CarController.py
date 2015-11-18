'''
Created on Nov 13, 2015

@author: Vlad
'''
from Domain.Car import Car

class CarController:
	
	def __init__(self, car_repo):
		
		self.__car_repo = car_repo
		
	def add(self, id_client, name):
		
		car = Car(id_client, name)
		
		# TODO: validate
		
		self.__car_repo.add(car)
		
	def update(self, id_car, new_name):
		
		new_car = Car(id_car, new_name)
		
		self.__car_repo.update(new_car)
		
	def delete(self, id_car):
		
		self.__car_repo.delete(id_car)
		
	def get_all(self):
		
		return self.__car_repo.get_all()
		
		