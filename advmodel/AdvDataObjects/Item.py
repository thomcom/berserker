# Parent class for all items in Adv

from DieRoll import DieRoll

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

# Code for figuring out why Armor instance has no attribute 'armor'
# class Weapon(Item):
#    def __init__(self):
#       Item.__init__(self)
#       self.damage = DieRoll("1d2")
#    def __str__(self):
#       result = Item.__str__(self)
#       return result + str(self.damage)
#    def __repr__(self):
#       return self.__str__()
# 
# class Armor(Item):
#    def __init__(self):
#       Item.__init__(self)
#       self.armor = DieRoll("1d2")
#    def __str__(self):
#       result = ""
#       return result + str(self.armor)
#    def __repr__(self):
#       return self.__str__()