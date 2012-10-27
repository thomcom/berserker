# Parent class for all items in Adv

class Item:
   def __init__(self):
      self.name = "Item"
      self.text = "Empty item text"
      self.value = 0
      self.usability = None
      self.salable = True
   def __str__(self):
      return """
         Name: %s
         Value: %d
         Usability: %s
         Salable: %s """ % (self.name,self.value,self.usability,self.salable)
   def __repr__(self):
      return self.__str__()
      

      
