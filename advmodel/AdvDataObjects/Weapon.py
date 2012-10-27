# Class for Weapon items

from AdvDataObjects import Item

class Weapon(Item):
   def __init__(self):
      self.attackDice = 1
      self.attackDie = 4
      self.attackMod = 0