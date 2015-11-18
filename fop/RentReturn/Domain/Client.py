'''
Created on Nov 13, 2015

@author: Vlad
'''

class Client:
	
	def __init__(self, id_client, name):
		'''
		Client object
		:param id_client:  inte
		:param name:
		:return:
		'''
		
		self.__id_client = id_client
		self.__name = name
		
	@property
	def id_client(self):
		'''
		Getter for the id of the client
		:return: an integer representing the id of a client
		'''
		return self.__id_client
	
	@property
	def name(self):
		'''
		Getter for the name of the client
		:return: a stirng representing the name of a client
		'''
		return self.__name
	
	def __str__(self):
		'''
		Return a human-readable string of the client
		:return: a string
		'''
		return "{0}. {1}".format(self.id_client, self.name)

	def __repr__(self):
		'''
		Return a human=readable string of the client
		:return:
		'''
		return str(self)
	
	def __eq__(self, other):
		'''
		Equal operator for the client object
		:param other: another client
		:return: true if the current object equals other or false otherwise
		'''
		return type(self) == type(other) and self.id_client == other.id_client
	
	def __hash__(self):

		'''
		Return the hash value for the current object
		:return: an integer
		'''
		# valoare unica, folosit pentru adaugare in dictionarele din repository
		
		return hash(self.id_client)