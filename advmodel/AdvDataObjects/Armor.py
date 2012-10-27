# Class for Armor items

from Item import Item

class Armor(Item):
   def __init__(self):
      super().__init__()
      self.armorDice = 1
      self.armorDie = 2
      self.armorMod = 0
   def __init__(self,item):
      self = item
      self.__init__()
   def __str__(self):
      returnString = "Armor: %dd%d" % (self.armorDice,self.armorDie)
      try:
         if self.armorMod > 0:
            returnString.append("+%d" % self.armorMod)
         else:
            returnString.append("-%d" % self.armorMod)
      except Exception, err:
         pass
      return Item().__str__() + """
         """ + returnString
   def __repr__(self):
      return self.__str__()