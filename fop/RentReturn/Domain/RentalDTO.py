'''
Created on Nov 13, 2015

@author: Vlad
'''

class RentalDTO:
	
	def __init__(self, id_client, id_car, price):
		'''
		Rental class for the id_s of the clients
		:param id_client:
		:param id_car:
		:param price:
		:return:
		'''
		
		self.__id_client = id_client
		self.__id_car = id_car
		self.__price = price
		
	@property
	def id_client(self):
		return self.__id_client
	
	@property
	def id_car(self):
		return self.__id_car

	@property
	def price(self):
		return self.__price
	
	def __eq__(self, other):
		
		return type(self) == type(other) and self.id_car == other.id_car and self.id_client == other.id_client
	
	def __hash__(self):
		
		# valoare unica, folosit pentru adaugare in dictionarele din repository
		
		return hash(str(self.id_client) + str(self.id_car))