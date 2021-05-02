#module for client-authentication, to prevent api-abuse

from datetime import datetime

#main class
class Authentication():
	def __init__(self):
		#saving client's ip + date of the latest key-authentication in a dictionary; format: "ip": "date"
		self.clients= {}


	#method to get the day as int from a datetime.datetime object
	def extract_day(self,time_object):
		elementS = str(time_object)
		#ignore time
		date= elementS.split(" ")[0]
		#extract day
		day= int(date.split("-")[2])
		return day


	#delete all self.clients pairs which are older than 24hours
	def clear_dic(self):

		#saves the keys of the elements in self.clients which are older than 24hours
		keys_of_older_clients= []

		#search for older clients
		for client in self.clients.keys():
			element= self.clients[client]

			if self.extract_day(datetime.now()) != self.extract_day(element):
				keys_of_older_clients.append(client)

        #delete them
		for oldie in keys_of_older_clients:
			del self.clients[oldie]


	#checks if the client have to send the API-key, return True -> no API-key needed, return False -> API-key needed
	def check_client(self, client_ip):
		#delete all self.clients pairs which are older than 24hours
		self.clear_dic()

		#checking if client_ip is in self.clients
		for ip in self.clients.keys():
			if client_ip == ip:
				self.clients[client_ip]= datetime.now()
				return True

		return False

	def add_client(self, client_ip):
		self.clients[client_ip]= datetime.now()



