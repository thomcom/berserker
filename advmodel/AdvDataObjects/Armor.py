# Class for Armor items

from Item import Item
from DieRoll import DieRoll

class Armor(Item):
   def __init__(self):
      Item.__init__(self)
      self.armor = DieRoll("1d2")
   def __str__(self):
      result = Item.__str__(self)
      return result + """
         Armor: """ + str(self.armor)
   def __repr__(self):
      return self.__str__()