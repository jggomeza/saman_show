from Event import Event
from TicketSale import TicketSale
from FoodFairManagement import FoodFairManagement
from FoodFairSale import FoodFairSale
from Statistics import Statistics
from SaveSell_JSON import SaveSell_JSON
import os

event = Event()
ticketSale = TicketSale()
foodFairManagement = FoodFairManagement()
foodFairSale = FoodFairSale()
statistics = Statistics()

response = SaveSell_JSON().getDatabase()

ventas=[]
count=1

value = 1
while value != 0:
  # Menu Principal
  os.system ("clear") 
  try:
    menu1 = """
      Seleccione una opción:
        1. Gestion de Eventos
        2. Buscador de Eventos
        3. Venta de Tickets
        4. Gestion feria de Comida
        5. Venta Feria de Comidas
        6. Estadisticas
        0. Salir
    """
    value = int(input(menu1))
  except Exception as e:
    print(e)
    continue

  # 1. Gestion de Eventos
  if value==1:
    os.system ("clear")
    i=1
    menu="""Seleccione un evento:\n"""
    try:
      for attrib in response['events']:
        menu+="  "+str(i)+". "+attrib['title']+"\n"
        i+=1
      evenValue = int(input(str(menu)))
    except Exception as e:
      print(e)
      
    title=str(response['events'][evenValue-1]['title'])
    print(title)
    event.getTypeEvent(title)
    event.getCartel(title)
    print(f"\nAsientos disponibles: ")
    event.getSeatingInformation(title)
    print(f"\nPrecios: ")
    event.getPrices(title) 
    print(f"\nFecha de la funcion: ")
    event.getDate_event(title)

  # 2. Buscador de Eventos
  if value==2:
    os.system ("clear")
    i=1
    menu="""Buscar un evento por:
  1. Tipo.
  2. Fecha
  3. Actor o cantante en el cartel.
  4. Nombre del evento\n"""
    try:
      for attrib in response['events']:
        i+=1
      evenValue = int(input(str(menu)))
    except Exception as e:
      print(e)

    if evenValue==1:
      os.system ("clear")
      try:
        typ=int(input("Introduce el tipo de evento que desea buscar:\n  1. Musical\n  2. Teatro\n"))
      except Exception as e:
        print(e)
      event.getSearch_event("type",typ)
    elif evenValue==2:
      os.system ("clear")
      i=1
      menu="""Seleccione la fecha a buscar:\n"""
      try:
        for attrib in response['events']:
          menu+="  "+str(i)+". "+attrib['date']+"\n"
          i+=1
        index = int(input(str(menu)))
      except Exception as e:
        print(e)
      event.getSearch_event("date",response['events'][index-1]['date'])
    elif evenValue==3:
      os.system ("clear")
      i=1
      actores=[]
      menu="""Seleccione el actor a buscar:\n"""
      try:
        for index in range(len(response['events'])):
          for actor in response['events'][index]['cartel']:
            actores.append(actor)
            menu+="  "+str(i)+". "+actor+"\n"
            i+=1
        index = int(input(str(menu)))
      except Exception as e:
        print(e)
      event.getSearch_event("cartel",actores[index-1])
    elif evenValue==4:
      os.system ("clear")
      i=1
      title=[]
      menu="""Seleccione el nombre del evento:\n"""
      try:
        for attrib in response['events']:
          title.append(attrib['title'])
          menu+="  "+str(i)+". "+attrib['title']+"\n"
          i+=1
        index = int(input(str(menu)))
      except Exception as e:
        print(e)
      event.getSearch_event("title",title[index-1])

  # 3.  Venta de Tickets
  if value==3:
    ticketSale.client()
    # venta=ticketSale.client()
    # venta['count']=count
    # venta['id']=id(venta)
    # ventas.append(dict(venta))
    # venta.clear()
    # count+=1
    # print(ventas)
    # print(venta)
  
  # 4. Gestion feria de Comida
  if value==4:
    os.system ("clear")
    menu="""Selecciona una opción:
  1. Registrar nuevos productos.
  2. Eliminar productos.
  3. Buscar productos.\n"""
    try:
      evenValue = int(input(str(menu)))
    except Exception as e:
      print(e)

    if evenValue==1:
      foodFairManagement.safeNewProduct()
    elif evenValue==2:
      foodFairManagement.deleteProducs()
    elif evenValue==3:
      menu="""Buscar un producto por:
  1. Nombre
  2. Tipo.
  3. Rango de precio.\n"""
      try:
        filter1 = int(input(str(menu)))
      except Exception as e:
        print(e)

      if filter1==1:
        try:
          # name = str(input("Introduzca el nombre del producto:\n"))
          name="Coca Cola"
        except Exception as e:
          print(e)
        foodFairManagement.getSearch_product('name',name)
      elif filter1==2:
        try:
          type = int(input("Seleccione el tipo de producto:\n  1. De empaque.\n  2. De preparación.\n"))
        except Exception as e:
          print(e)
        foodFairManagement.getSearch_product('type',type)
      elif filter1==3:
        try:
          min = int(input("Introduzca el precio minimo:\n"))
        except Exception as e:
          print(e)
        try:
          max = int(input("Introduzca el precio maximo:\n"))
        except Exception as e:
          print(e)
        foodFairManagement.getSearch_product('range',None,min,max)

  # 5. Venta Feria de Comidas
  if value==5:
    foodFairSale.ventaFood()
  # 5. Venta Feria de Comidas
  if value==6:
    menu="""Seleccione una opcion:
  1. Promedio de gasto de un cliente en un evento (ticket + feria de comida)
  2. Porcentaje de clientes que no compran en la feria de comida
  3. Clientes (los 3 primeros) de mayor fidelidad en el saman_show
  4. Top de 3 Eventos con mas ingresos
  5. Top 5 productos mas vendidos en la feria de comida\n"""
    try:
      filter1 = int(input(str(menu)))
    except Exception as e:
      print(e)

    if filter1==1:
      Statistics().avgClients()
    elif filter1==2:
      Statistics().percentClients()
    elif filter1==3:
      Statistics().faithfulClients()
    elif filter1==4:
      Statistics().eventsIncome()
    elif filter1==5:
      Statistics().productsSell()

      
