from SaveSell_JSON import SaveSell_JSON

class Event(SaveSell_JSON):
  def __init__(self): # Constructor de la clase, es el que da el estado inicial
    self.response = SaveSell_JSON().getDatabase()
  def printJson(self):
    print(self.response['events'])
  def getName_events(self):
    i = 1
    for attrib in self.response['events']:
      print(str(i)+". "+attrib['title'])
      i+=1
  def getName_event(self,nameEvent):
    for attrib in self.response['events']:
      if attrib['title']==nameEvent:
        print(attrib['title'])
  def getTypeEvent(self,nameEvent):
    for attrib in self.response['events']:
      if attrib['title']==nameEvent:
        if attrib['type']==1:
          print("Musical:")
          print(f"  En el musical {nameEvent} se presentaran {attrib['bands']} bandas: ")
        if attrib['type']==2:
          print("Teatro:")
          print(f"  {nameEvent}:\n  {attrib['synopsis']}")
  def getCartel(self,nameEvent):
    i = 1
    for attrib in self.response['events']:
      if attrib['title']==nameEvent:
        for iten in attrib['cartel']:
          print(f"  {i}. {iten}")
          i+=1
  def getSeatingInformation(self,nameEvent):
    for attrib in self.response['events']:
      if attrib['title']==nameEvent:
        for zone in attrib['layout']:
          print(f"{zone.capitalize()}")
          for seat in attrib['layout'][zone]:
              print(f" -> {seat}")
  def getPrices(self, nameEvent):
      for attrib in self.response['events']:
          if attrib['title']==nameEvent:
              print(f"  General -> {attrib['prices'][0]}$")
              print(f"  Vip -> {attrib['prices'][1]}$")
  def getDate_event(self, nameEvent):
    for attrib in self.response['events']:
        if attrib['title']==nameEvent:
            print(f"    {attrib['date']}")
  def getSearch_event(self, filter, searching):
    for attrib in self.response['events']:
      if filter == 'type':
        if attrib['type']==searching:
          print(f"Titulo: {attrib['title']}")
          self.getTypeEvent(attrib['title'])
          self.getCartel(attrib['title'])
          print(f"\nAsientos disponibles: ")
          self.getSeatingInformation(attrib['title'])
          print(f"\nPrecios: ")
          self.getPrices(attrib['title']) 
          print(f"\nFecha de la funcion: ")
          self.getDate_event(attrib['title'])
          print("-------------------------------------------------------")
      elif filter == 'date':
        if attrib['date']==searching:
          print(f"Titulo: {attrib['title']}")
          self.getTypeEvent(attrib['title'])
          self.getCartel(attrib['title'])
          print(f"\nAsientos disponibles: ")
          self.getSeatingInformation(attrib['title'])
          print(f"\nPrecios: ")
          self.getPrices(attrib['title']) 
          print(f"\nFecha de la funcion: ")
          self.getDate_event(attrib['title'])
          print("-------------------------------------------------------")
      elif filter == 'cartel':
        for actor in attrib['cartel']:
          if actor == searching:
            print(f"Titulo: {attrib['title']}")
            self.getTypeEvent(attrib['title'])
            self.getCartel(attrib['title'])
            print(f"\nAsientos disponibles: ")
            self.getSeatingInformation(attrib['title'])
            print(f"\nPrecios: ")
            self.getPrices(attrib['title']) 
            print(f"\nFecha de la funcion: ")
            self.getDate_event(attrib['title'])
            print("-------------------------------------------------------")
      elif filter == 'title':
        if attrib['title']==searching:
          print(f"Titulo: {attrib['title']}")
          self.getTypeEvent(attrib['title'])
          self.getCartel(attrib['title'])
          print(f"\nAsientos disponibles: ")
          self.getSeatingInformation(attrib['title'])
          print(f"\nPrecios: ")
          self.getPrices(attrib['title']) 
          print(f"\nFecha de la funcion: ")
          self.getDate_event(attrib['title'])
          print("-------------------------------------------------------")

        
# event = Event()
# event.printJson()
# event.getName_events()
# event.getName_event("Saman Fest")
# event.getTypeEvent("Saman Fest")
# event.getTypeEvent("El famtasma del paraninfo")
# event.getCartel("Saman Fest") 
# event.getSeatingInformation("Saman Fest")
# event.getPrices("Saman Fest") 
# event.getDate_event("Saman Fest")
# event.getSearch_event("type",2)
# event.getSearch_event("cartel",'Ramayana')
# event.getSearch_event("date",'2022-04-01')
# event.getSearch_event("title","Saman Fest")