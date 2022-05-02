import pandas as pd
import matplotlib.pyplot as plt
import json
import os
from io import open


class Statistics():
	"""Muestra todas las estadisticas del programa"""
	def __init__(self):
		with open("TicketSale.json", "r") as openfile:
			self.ventasTickets = json.load(openfile)
		openfile.close()
		del(openfile)

		with open("FoodFairSale.json", "r") as openfile:
			self.ventasFood = json.load(openfile)
		openfile.close()
		del(openfile)
		
	def avgClients(self):
		# 1.	¿Cuál es el promedio de gasto de un cliente en un evento (ticket + feria de comida)?
		ticketTotal={}
		nameClients={}
		for tiket in self.ventasTickets:
			if tiket['dni'] in ticketTotal.keys():
				ticketTotal[tiket['dni']]+=tiket['subtotal']
			else:
				ticketTotal[tiket['dni']]=tiket['subtotal']

		foodTotal={}
		for food in self.ventasFood:
			if food['dni'] in foodTotal.keys():
				foodTotal[food['dni']]+=food['subtotal']
			else:
				foodTotal[food['dni']]=food['subtotal']


		for i in foodTotal:
			for j in ticketTotal:
				if i==j:
					ticketTotal[i]+=foodTotal[i]

		# print(ticketTotal)
		ticketTotal={k: v for k, v in sorted(ticketTotal.items(), key=lambda item: item[1], reverse=True)}
		# print(ticketTotal)
		# print(nameClients)

		# for v in list(ticketTotal.keys()):
		# 	for dni in nameClients:
		# 		if v==nameClients[dni]:
		# 			# print( nameClients[dni] )
		# 			print( dni )

		data1 = {
			'Clientes': list(ticketTotal.keys())[0:3],
			'Price': list(ticketTotal.values())[0:3]
		}
		df1 = pd.DataFrame(data1,columns=['Clientes','Price'])
		df1.plot(kind='bar', legend=True, x='Clientes', y='Price')
		avg=0
		for i in ticketTotal:
			avg+=ticketTotal[i]
		plt.title(f"El promedio de gasto de un cliente en un evento es de {round(avg/len(ticketTotal))}$ (ticket + feria de comida)")
		plt.show()

		# print(foodTotal)
		# avg=0
		# for i in ticketTotal:
		# 	avg+=ticketTotal[i]
		# print(f"El promedio de gasto de un cliente en un evento es de {round(avg/len(ticketTotal))}$")

	def percentClients(self):
		# 2.	¿Cuál es el porcentaje de clientes que no compran en la feria de comida?
		client={}
		suma=0
		for ticketV in self.ventasTickets:
			for foodV in self.ventasFood:
				if ticketV['dni']==foodV['dni']:
					suma+=1
			client[str(ticketV['dni'])]=suma
			suma=0

		count=0
		for c in client:
			if client[c]!=0:
				count+=1

		clientCompraron={}
		clientCompraron['Compraron']=count
		nocompraron=len(client)-count
		clientCompraron['No compraron']=nocompraron

		# print(clientCompraron)
		values = list(clientCompraron.values())
		labels = ['Compraron', 'No Compraron']
		# print(values)
		plt.pie(values, labels = labels, autopct='%.0f%%')
		  
		# displaying the title
		plt.title(label=f"El {round((nocompraron*100)/len(client))}% de los clientes no compraron en la feria de comida",
			loc="left",
			fontstyle='italic'
		)
		plt.show()

	def faithfulClients(self):
		# 3.	¿Quiénes son los clientes (los 3 primeros) de mayor fidelidad en el saman_show?
		fieles={}
		suma=0
		for ticketV in self.ventasTickets:
			for ticketV2 in self.ventasTickets:
				if ticketV['dni']==ticketV2['dni']:
					suma+=1
			fieles[str(ticketV['name'])]=suma
			suma=0

		# print(fieles)
		fieles={k: v for k, v in sorted(fieles.items(), key=lambda item: item[1], reverse=True)}
		# print(fieles)

		data1 = {
			'Clientes': list(fieles.keys())[0:3],
			'Cantidad de productos comprados': list(fieles.values())[0:3]
		}
		df1 = pd.DataFrame(data1,columns=['Clientes','Cantidad de productos comprados'])
		df1.plot(kind='bar', legend=True, x='Clientes', y='Cantidad de productos comprados')
		plt.title(f"Los clientes mas fieles de Saman Show")
		plt.show()
	def eventsIncome(self):
		# 4.	Top de 3 Eventos con más ingresos.
		events={}
		for ticketV in self.ventasTickets:
			# print(ticketV['event'])
			if ticketV['event'] in events.keys():
				events[ticketV['event']]+=ticketV['subtotal']
			else:
				events[ticketV['event']]=ticketV['subtotal']
		# print(events)
		events={k: v for k, v in sorted(events.items(), key=lambda item: item[1], reverse=True)}
		# print(events)

		values = list(events.values())[0:3]
		labels = list(events.keys())[0:3]
		# print(values)
		plt.pie(values, labels = labels, autopct='%.0f%%')
		  
		# displaying the title
		plt.title(label=f"Top de 3 Eventos con más ingresos",
			loc="left",
			fontstyle='italic'
		)
		plt.show()

	def productsSell(self):
		# 5.	Top 5 productos más vendidos en la feria de comida.
		product={}
		for ticketV in self.ventasFood:
			if ticketV['name'] in product.keys():
				product[ticketV['name']]+=1
			else:
				product[ticketV['name']]=1

		# print(product)
		product={k: v for k, v in sorted(product.items(), key=lambda item: item[1], reverse=True)}
		# print(product)

		values = list(product.values())[0:5]
		labels = list(product.keys())[0:5]
		plt.pie(values, labels = labels, autopct='%.0f%%')
		  
		# displaying the title
		plt.title(label=f"Top de 5 de productos más vendidos",
			loc="left",
			fontstyle='italic'
		)
		plt.show()

# Statistics().avgClients()
# Statistics().percentClients()
# Statistics().faithfulClients()
# Statistics().eventsIncome()
# Statistics().productsSell()