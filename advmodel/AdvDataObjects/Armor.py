# Class for Armor items

from AdvDataObjects import Item

class Armor(Item):
   def __init__(self):
      self.armorDice = 1
      self.armorDie = 2
      self.armorMod = 0