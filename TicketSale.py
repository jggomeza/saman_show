from Event import Event
from Vampire import Vampire
from SaveSell_JSON import SaveSell_JSON
import os
import json

class TicketSale(Vampire,Event,SaveSell_JSON):
  def __init__(self):
      # super(Event, self).__init__()
      self.event=SaveSell_JSON().getDatabase()
      # self.ventas=[]
      self.ventas=SaveSell_JSON().getTicketSale()
      self.venta={}

  def client(self):
    i=1
    try:
      name=str(input("Introduzca el nombre del cliente:\n"))
      # name="José Gómez"
    except Exception as e:
      print(e)

    try:
      dni=int(input("Introduzca la cedula del cliente:\n"))
      # dni=25792596
    except Exception as e:
      print(e)
    
    try:
      age=int(input("Introduzca la edad del cliente:\n"))
      # age=26
    except Exception as e:
      print(e)
    

    menu="Selecione el evento al que desea asistir:\n"
    for event in self.event['events']:
      menu+=f"{i}. {event['title']}\n"
      if event['type']==1:
        menu+=f"   Musical\n"
        menu+=f"   En el musical {event['title']} se presentaran {event['bands']} bandas:\n"
        
        for iten in event['cartel']:
          menu+=f"      - {iten}\n"
      if event['type']==2:
        menu+=f"   Teatro\n"
        menu+=f"   {event['synopsis']}.\n"
        menu+="   Con la participacion de los siguientes actores:\n"
        for iten in event['cartel']:
          menu+=f"      - {iten}\n"
      i+=1
    
    try:
      evento=int(input(menu))
      # evento=1
    except Exception as e:
      print(e)

    try:
      cantTickets=int(input("Cantidad de tickets que desea comprar:\n"))
      # cantTickets=1
    except Exception as e:
      print(e)

    menu="Seleccione una zona para sentarse:\n"
    i=1
    for zone in self.event['events'][evento-1]['layout']:
      menu+=f"   {zone.capitalize()}\n"
      for seat in self.event['events'][evento-1]['layout'][zone]:
        menu+=f"      {   zone.capitalize()[0]}{seat}. asiento {seat}\n"

    try:
      seat=str(input(menu))
      # seat="B10"
    except Exception as e:
      print(e)

    menu=f"Seleccione el precio de su entrada:\n  1. General: {self.event['events'][evento-1]['prices'][0]}\n  2. VIP: {self.event['events'][evento-1]['prices'][1]}\n"
    price=int(input(menu))
    price=self.event['events'][evento-1]['prices'][price-1]*cantTickets
    # price=30

    if self.is_vampire(dni):
      price50=price-((price*50)/100)
      iva=(price*16)/100
      price16=price50+((price*16)/100)
      menu=f"Felicidades {name} has obtenido un descuento del 50% por el costo de tu entrada!\n"
      menu+=f"Selecciono el asiento {seat}\nCosto: {price}$\nCon el 50% de descuento: {price50}$\nIVA: {iva}\nSubtotal a pagar: {price16}\n"
      menu+="¿Desea proceder a pagar?:\n  1. Si\n  2. No\n"
      try:
        pagar=int(input(menu))
        # pagar=1
      except Exception as e:
        print(e)
      if pagar==1:
        self.venta['name']=name
        self.venta['dni']=dni
        self.venta['age']=age
        self.venta['event']=self.event['events'][evento-1]['title']
        self.venta['cantTickets']=cantTickets
        self.venta['seat']=seat
        self.venta['price']=price
        self.venta['descuento']=price50
        self.venta['iva']=iva
        self.venta['subtotal']=price16
        print("El pago se realizo de forma exitosa!")
        self.ventas.append(dict(self.venta))
        SaveSell_JSON().saveTicketSale(self.ventas)
        
        # return self.ventas
      else:
        print("Gracias por su visita!")
    else:
      iva=(price*16)/100
      price16=price+((price*16)/100)
      menu=f"Selecciono el asiento {seat}\nCosto: {price}$\nIVA: {iva}\nSubtotal a pagar: {price16}\n"
      menu+="¿Desea proceder a pagar?:\n  1. Si\n  2. No\n"
      try:
        pagar=int(input(menu))
        # pagar=1
      except Exception as e:
        print(e)
      if pagar==1:
        self.venta['name']=name
        self.venta['dni']=dni
        self.venta['age']=age
        self.venta['event']=self.event['events'][evento-1]['title']
        self.venta['cantTickets']=cantTickets
        self.venta['seat']=seat
        self.venta['price']=price
        self.venta['descuento']=0
        self.venta['iva']=iva
        self.venta['subtotal']=price16
        print("El pago se realizo de forma exitosa!")
        self.ventas.append(dict(self.venta))
        SaveSell_JSON().saveTicketSale(self.ventas)
        
        # return self.ventas
      else:
        print("Gracias por su visita!")

# os.system ("cls")
sell = TicketSale()
# sell.client()