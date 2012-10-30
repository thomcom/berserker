# Class for Weapon items

from Item import Item
from DieRoll import DieRoll

class Weapon(Item):
   def __init__(self):
      Item.__init__(self)
      self.damage = DieRoll("1d2")
   def __str__(self):
      result = Item.__str__(self)
      return result + str(self.damage)
   def __repr__(self):
      return self.__str__()