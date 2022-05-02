from Event import Event
from SaveSell_JSON import SaveSell_JSON

class FoodFairManagement(SaveSell_JSON):
  def __init__(self): # Constructor de la clase, es el que da el estado inicial
    self.database = SaveSell_JSON().getDatabase()['food_fair_inventory']
  
  def printJson(self):
    print(self.database)
  def safeNewProduct(self):
    product={}

    try:
      nameProduct = str(input("Introduzca el nombre del Producto:\n"))
    except Exception as e:
      print(e)
    product['name']=nameProduct

    try:
      price = float(input("Indique el precio del alimento:\n"))
      price+=(price*16)/100
    except Exception as e:
      print(e)
    product['price']=price

    try:
      amount = float(input("Indique la cantidad del alimento:\n"))
    except Exception as e:
      print(e)
    product['amount']=amount

    try:
      typ = int(input("Introduzca el tipo de Producto:\n1. Bebida\n2. Alimento\n"))
    except Exception as e:
      print(e)

    if typ==1:
      try:
        size = int(input("Indique el tamaño:\n1. Pequeño\n2. Mediano\n3. Grande\n"))
      except Exception as e:
        print(e)

      product['presentation']=size
      if size==1:
        size="Pequeño"
      elif size==2:
        size="Mediano"
      elif size==3:
        size="Grande"

    if typ==2:
      try:
        typeProduct = int(input("Indique el tipo de alimento:\n1. De empaque\n2. De preparacíon\n"))
      except Exception as e:
        print(e)
      product['type']=typeProduct
      if typeProduct==1:
        typeProduct="De empaque"
      elif typeProduct==2:
        typeProduct="De preparacíon"

    self.database.append(product)

  def deleteProducs(self):
    i=1
    menu="""Seleccione un producto para eliminar:\n"""
    try:
      for product in self.database:
        menu+="  "+str(i)+". "+product['name']+"\n"
        i+=1
      product = int(input(str(menu)))
    except Exception as e:
      print(e)

    if len(self.database)>=1:
      self.database.pop(product-1)

  def getSearch_product(self, filter, searching, min=0, max=0):
    for dic in self.database:
      if filter=='name':
        if searching == str(dic['name']):
          print(f"Nombre: {dic['name']}")
          if isinstance(dic['price'], list):
            i=1
            for p in dic['price']:
              print(f"Precio {i}: {p} $")
              i+=1
          if type(dic['price'])==float:
            print(f"Precio: {dic['price']} $")  
          print(f"Cantidad: {dic['amount']}")
          if 'presentation' in dic:
            print(f"Presentación: {dic['presentation']}")
          if 'type' in dic:
            print(f"Tipo: {dic['type']}")
          print("-------------------------------------------------------")

      if filter=='type':
        if searching == int(dic['type']):
          print(f"Nombre: {dic['name']}")
          if isinstance(dic['price'], list):
            i=1
            for p in dic['price']:
              print(f"Precio {i}: {p} $")
              i+=1
          if type(dic['price'])==float:
            print(f"Precio: {dic['price']} $")  
          print(f"Cantidad: {dic['amount']}")
          if 'presentation' in dic:
            print(f"Presentación: {dic['presentation']}")
          if 'type' in dic:
            print(f"Tipo: {dic['type']}")
          print("-------------------------------------------------------")

      if filter=='range':
        if isinstance(dic['price'], list):
          mayor=sorted(dic['price'],reverse=True)[0]
          if min < mayor and mayor < max:
            print(f"Nombre: {dic['name']}")
            if isinstance(dic['price'], list):
              i=1
              for p in dic['price']:
                print(f"Precio {i}: {p} $")
                i+=1
            if type(dic['price'])==float:
              print(f"Precio: {dic['price']} $")  
            print(f"Cantidad: {dic['amount']}")
            if 'presentation' in dic:
              print(f"Presentación: {dic['presentation']}")
            if 'type' in dic:
              print(f"Tipo: {dic['type']}")
            print("-------------------------------------------------------")
        else:
          mayor=dic['price']
          if min < mayor and mayor < max:
            print(f"Nombre: {dic['name']}")
            if isinstance(dic['price'], list):
              i=1
              for p in dic['price']:
                print(f"Precio {i}: {p} $")
                i+=1
            if type(dic['price'])==float:
              print(f"Precio: {dic['price']} $")  
            print(f"Cantidad: {dic['amount']}")
            if 'presentation' in dic:
              print(f"Presentación: {dic['presentation']}")
            if 'type' in dic:
              print(f"Tipo: {dic['type']}")
            print("-------------------------------------------------------")
            
# os.system ("cls")
# food = FoodFairManagement()
# food.printJson()
# food.safeNewProduct()
# food.deleteProducs()
# food.getSearch_product("name","Jugo")
# food.getSearch_product("name","Doritos")