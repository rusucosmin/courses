'''
Created on Nov 13, 2015

@author: Vlad
'''

class Rental:
	
	def __init__(self, client, car, price):
		'''
		Rental class object
		:param client: client object
		:param car:  car object
		:param price: the prince for renting the car to this client
		'''

		self.__client = client
		self.__car = car
		self.__price = price
		
	@property
	def car(self):
		'''
		Getter for the car
		:return: a Car object
		'''
		return self.__car
	
	@property
	def client(self):
		'''
		Getter for the client
		:return: a Client object
		'''
		return self.__client
	
	@property
	def price(self):
		'''
		Getter for the price
		:return: an integer
		'''
		return self.__price
	
	def __str__(self):
		'''
		:return:
		'''
		return "Car {0} rented to client {1}".format(self.car, self.client)

	
	def __repr__(self):
	
		return str(self)
	
	def __eq__(self, other):
		return type(self) == type(other) and self.client.id_client == other.client.id_client \
										 and self.car.id_car == other.car.id_car
	
