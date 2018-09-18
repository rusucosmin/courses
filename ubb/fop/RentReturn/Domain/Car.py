'''
Created on Nov 13, 2015

@author: Vlad
'''

class Car:
	
	def __init__(self, id_car, name):
		'''
		Car class representing the object type car, which has an id and a name
		:param id_car:
		:param name:
		:return:
		'''
		self.__id_car = id_car
		self.__name = name
		
	@property
	def id_car(self):
		'''
		Getter for the id_car
		:return: an integer representing the id of the car
		'''
		return self.__id_car
	
	@property
	def name(self):
		'''
		Getter for the name of the car
		:return: a string containing the name of the car
		'''
		return self.__name
	
	def __str__(self):
		'''
		Function to return a human readable string for our car.
		:return: a string
		'''
		return "{0}. {1}".format(self.id_car, self.name)
	
	def __repr__(self):
		'''
		Function to return a human readable string for our car
		:return: a string
		'''
		return str(self)
	
	def __eq__(self, other):
		'''
		Equal operator
		:param other: other car
		:return: true if they are equal, and false if the aren't
		'''
		return type(self) == type(other) and self.id_car == other.id_car
	
	def __hash__(self):
		'''
		Function to get the hash value of the object
		:return: a unique id
		'''
		# valoare unica, folosit pentru adaugare in dictionarele din repository
		
		return hash(self.id_car)