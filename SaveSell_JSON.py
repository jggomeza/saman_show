import requests
import json


class SaveSell_JSON(object):
	"""Almacena un JSON de las ventas para preservar los datos"""
	def getDatabase(self):
		with open("api.json", "r") as openfile:
			try:
				json_object = json.load(openfile)
			except Exception as e:
				response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json')
				with open("api.json", "w") as outfile:
					json.dump(response.json(), outfile, indent=4, separators=(", ", ": "))
				outfile.close()
				del(outfile)
				json_object = json.load(openfile)
		openfile.close()
		del(openfile)
		return json_object
	def getTicketSale(self):
		with open("TicketSale.json", "r") as openfile:
			try:
				json_object = json.load(openfile)
			except Exception as e:
				with open("TicketSale.json", "w") as outfile:
					json.dump([], outfile, indent=4, separators=(", ", ": "))
				outfile.close()
				del(outfile)
				json_object = json.load(openfile)
		openfile.close()
		del(openfile)
		return json_object
	def saveTicketSale(self,sell):
		with open("TicketSale.json", "w") as outfile:
		  json.dump(sell, outfile, indent=4, separators=(", ", ": "))
		outfile.close()
		del(outfile)
		
	def getFairSale(self):
		with open("FoodFairSale.json", "r") as openfile:
			try:
				json_object = json.load(openfile)
			except Exception as e:
				with open("FoodFairSale.json", "w") as outfile:
					json.dump([], outfile, indent=4, separators=(", ", ": "))
				outfile.close()
				del(outfile)
				json_object = json.load(openfile)
		openfile.close()
		del(openfile)
		return json_object
	def saveFairSale(self,sell):
		with open("FoodFairSale.json", "w") as outfile:
		  json.dump(sell, outfile, indent=4, separators=(", ", ": "))
		outfile.close()
		del(outfile)


















	# def printJSON(self):
	# 	with open("sample.json", "r") as openfile:
	# 		json_object = json.load(openfile)
	# 	print(json_object)
	# 	print(type(json_object))
	# 	openfile.close()
	# 	del(openfile)

	# def saveDict(self,name,dni,age):
	# 	empty=False
	# 	with open("sample.json", "r+") as openfile:
	# 		try:
	# 			list=json.load(openfile)
	# 		except Exception as e:
	# 			with open("sample.json", "w") as outfile:
	# 				json.dump([{"name":name,"dni":dni,"age":age}], outfile, indent=4, separators=(", ", ": "))#, sort_keys=True)
	# 			empty=True
	# 		finally:
	# 			if not empty:
	# 				with open("sample.json", "r+") as openfile:
	# 					list=json.load(openfile)
	# 					list.append({"name":name,"dni":dni,"age":age})
						
	# 					print(list)

	# 					with open("sample.json", "w") as outfile:
	# 						json.dump(list, outfile, indent=4, separators=(", ", ": "))#, sort_keys=True)
	# 					outfile.close()
	# 					del(outfile)
	# 					empty=False

# create = SaveSell_JSON()
# # create.printJSON()
# for x in range(1,2):
# 	create.saveDict(f"Jose{x}",f"dni{x}",f"age{x}")
