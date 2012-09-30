import Player
from Player import Player
from Data import Data
import random

class Monster(Player):
   monster_list = [
      ["Goblin",        4, 0, 6],
      ["Ogre",          10,0, 10],
      ["Wolf",          8, 0, 8],
      ["Ogre mage",     8, 6, 12],
      ["Dragon",        20,10,12]
      ]
   @classmethod
   def GetRandomMonster(cls):
      return Monster(cls.monster_list[random.randint( 0,len(cls.monster_list)-1 )][Data.name_i])
   def __init__(self,name="Monster"):
      self.name = name
      Player.__init__(self,self.name)
      for i in range( len( self.monster_list ) ):
         if( self.name == self.monster_list[i][Data.name_i] ):
            self.max_hp     = self.monster_list[i][Data.hp_i]
            self.max_mp     = self.monster_list[i][Data.mp_i]
            self.attack_die = self.monster_list[i][Data.damage_i]
   def display(self):
      print("Type: " + self.name)
      print("HP:    " + str(self.max_hp-self.damage)  + "/" + str(self.max_hp))
      print("MP:    " + str(self.max_mp-self.used_mp) + "/" + str(self.max_mp))
   
