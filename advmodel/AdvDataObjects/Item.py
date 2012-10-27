# Parent class for all items in Adv

class Item:
   def __init__(self):
      self.name = "Item"
      self.text = "Empty item text"
      self.value = 0
      self.usability = None
      self.salable = True
   def __str__(self):
      print("Item---")
      print("Name: " + self.name)
      print("Value: " + self.value)
      print("Usability: " + self.usability)
      print("Salable: " + self.salable)