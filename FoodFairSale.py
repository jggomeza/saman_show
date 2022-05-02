from Event import Event
from SaveSell_JSON import SaveSell_JSON
from TicketSale import TicketSale
import os

class FoodFairSale(TicketSale, SaveSell_JSON):
  def __init__(self):
      self.ventaF={}
      self.database = SaveSell_JSON().getDatabase()['food_fair_inventory']
      self.ventas=TicketSale().getFairSale()

  def ventaFood(self):
    ticketSale = TicketSale()
    try:
      dni=int(input("Introduzca la cedula del cliente:\n"))
      # dni=1260
    except Exception as e:
      print(e)

    for venta in ticketSale.ventas:
      client=False
      if venta['dni']==dni:
        clientName=venta['name']
        client=True
        break

    if client:
      self.ventaF['dni']=dni
      menu=f"Indique el producto que desea comprar:\n"
      i=1
      for product in self.database:
        menu+=f"  {i}. {product['name']}\n"
        i+=1

      try:
        p=int(input(menu))
        # p=1
      except Exception as e:
        print(e)

      self.ventaF['name']=self.database[p-1]['name']
      # print(self.database[p-1])
      menu=f"Seleccione el precio:\n"
      i=1
      if isinstance(self.database[p-1]['price'], list):
        for price in self.database[p-1]['price']:
          menu+=f"  {i}. {price}\n"
          i+=1

        try:
          price=int(input(menu))
        except Exception as e:
          print(e)

        self.ventaF['price']=self.database[p-1]['price'][price-1]
      else:
        menu+=f"  {i}. {self.database[p-1]['price']}\n"
        try:
          price=int(input(menu))
        except Exception as e:
          print(e)
        
        self.ventaF['price']=self.database[p-1]['price']

      try:
        menu=f"Seleccione la cantidad que desea comprar:\n"
        cant=int(input(menu))
      except Exception as e:
        print(e)


      dni=str(dni)
      sum=0
      for i in dni:
        sum+=pow(int(i),len(dni))

      if sum==int(dni):
        menu=f"Felicidades {clientName} has obtenido un descuento del 15% por el costo de tu {self.ventaF['name']}!\n"
        menu+=f"Selecciono {cant} {self.ventaF['name']}\nCosto: {self.ventaF['price']}$\nCon el 15% de descuento: {(self.ventaF['price']*15)/100}$\nSubtotal a pagar: {self.ventaF['price']*cant-((self.ventaF['price']*cant*15)/100)}$\n"
        menu+="¿Desea proceder a pagar?:\n  1. Si\n  2. No\n"
        self.ventaF['descuento']=(self.ventaF['price']*cant*15)/100
        self.ventaF['subtotal']=self.ventaF['price']*cant
      else:
        menu+=f"Selecciono {cant} {self.ventaF['name']}\nCosto: {self.ventaF['price']}$\nSubtotal a pagar: {self.ventaF['price']*cant}$\n"
        menu+="¿Desea proceder a pagar?:\n  1. Si\n  2. No\n"
        self.ventaF['descuento']=0
        self.ventaF['subtotal']=self.ventaF['price']*cant

      
      try:
        pagar=int(input(menu))
      except Exception as e:
        print(e)

      if pagar==1:
        self.ventas.append(dict(self.ventaF))
        TicketSale().saveFairSale(self.ventas)
        # print(self.ventas)
        # print(self.database[p-1])
        self.database[p-1]['amount']-=cant
        # print(self.database[p-1])
        print("El pago se realizo de forma exitosa!")
      else:
        print("Gracias por su visita!")
    else:
      print("Debe comprar una entrada primero para poder comprar en la feria de comida!")

# os.system ("cls")
sell = FoodFairSale()
# sell.ventaFood()