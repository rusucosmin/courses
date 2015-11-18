'''
Created on Nov 13, 2015

@author: Vlad
'''

from Domain.Client import Client

class ClientController:
	
	def __init__(self, client_repo):
		
		self.__client_repo = client_repo
		
	def add(self, id_client, name):
		
		client = Client(id_client, name)
		
		# TODO: validate
		
		self.__client_repo.add(client)
		
	def update(self, id_client, new_name):
		
		new_client = Client(id_client, new_name)
		
		self.__client_repo.update(new_client)
		
	def delete(self, id_client):
		
		self.__client_repo.delete(id_client)
		
	def get_all(self):
		
		return self.__client_repo.get_all()
		
		