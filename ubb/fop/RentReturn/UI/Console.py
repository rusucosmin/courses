'''
Created on Nov 13, 2015

@author: Vlad
'''

class Console:
	
	def __init__(self, ctrl_car, ctrl_client, ctrl_rental):
		'''
		Class responsible for the ui exceprience
		:param ctrl_car: the CarController
		:param ctrl_client: the ClientController
		:param ctrl_rental: the RentalController
		'''
		
		self.__ctrl_car = ctrl_car
		self.__ctrl_client = ctrl_client
		self.__ctrl_rental = ctrl_rental
		
	def show(self):
		
		while True:
			print("1. Add car")
			print("2. Update car")
			print("3. Delete car")
			print("4. Add client")
			print("5. Update client")
			print("6. Delete client")
			print("7. Show clients")
			print("8. Show cars")
			print("9. Add rental")
			print("10. Delete rental")
			print("11. Show rentals")

			print("0. Exit")
			
			option = input("Option: ")
			
			if option == "1":
				self.__add_car()
			elif option == "2":
				self.__update_cars()
			elif option == "3":
				self.__delete_cars()
			elif option == "4":
				self.__add_client()
			elif option == "5":
				self.__update_clients()
			elif option == "6":
				self.__delete_clients()
			elif option == "7":
				self.__show_clients()
			elif option == "8":
				self.__show_cars()
			elif option == "9":
				self.__add_rental()
			elif option == "10":
				self.__delete_rental()
			elif option == "11":
				self.__show_rentals()
			elif option == "0":
				break
			else:
				print("Invalid option, please try again!")
				
	def __add_car(self):
		
		while True:
			
			try:
				id = input("ID: ")
				name = input("name: ")
				
				self.__ctrl_car.add(id, name)
			
				break
			except KeyError as ke:
				print(ke)
				
	def __add_client(self):
		
		while True:
		
			try:
				id = input("ID: ")
				name = input("name: ")
				
				self.__ctrl_client.add(id, name)
				
				break
			except KeyError as ke:
				print(ke)
				
	def __show_cars(self):
		
		print(self.__ctrl_car.get_all())
		
	def __show_clients(self):
		
		print(self.__ctrl_client.get_all())
		
	def __update_cars(self):
		
		while True:
			
			try:
				id = input("ID: ")
				name = input("name: ")
				
				self.__ctrl_car.update(id, name)
			
				break
			except KeyError as ke:
				print(ke)
				
	def __delete_cars(self):
		
		while True:
			
			try:
				id = input("ID to delete: ")
				
				self.__ctrl_rental.delete_by_car(id)
				self.__ctrl_car.delete(id)
				
				break
			except KeyError as ke:
				print(ke)
		
	def __update_clients(self):
		
		while True:
		
			try:
				id = input("ID: ")
				name = input("name: ")
				
				self.__ctrl_client.update(id, name)
				
				break
			except KeyError as ke:
				print(ke)
				
	def __delete_clients(self):
		
		while True:
			
			try:
				id = input("ID to delete: ")
				
				self.__ctrl_rental.delete_by_client(id)
				self.__ctrl_client.delete(id)
				
				break
			except KeyError as ke:
				print(ke)
		
	def __add_rental(self):
		
		while True:
			
			#try:
				id_client = input("ID Client: ")
				id_car = input("ID Car: ")
				price = input("Price: ")
				
				self.__ctrl_rental.add(id_client, id_car, price)
				
				break
			#except KeyError as ke:
			#	print(ke)
			#except ValueError as ve:
			#	print(ve)
				
	def __delete_rental(self):
		
		while True:
			
			try:
				id_client = input("ID of the client: ")
				id_car = input("ID of the car: ")
				
				self.__ctrl_rental.delete(id_client, id_car)
				
				break
			except KeyError as ke:
				print(ke)
	
	def __show_rentals(self):
		
		print(self.__ctrl_rental.get_all())