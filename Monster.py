import Player
from Player import Player
from Data import Data
import random

class Monster(Player):
   monster_list = [
# name
# hp
# mana
# damage
# xp
      ["Goblin",        4, 0, 6,   15],
      ["Ogre",          10,0, 10,  30],
      ["Wolf",          8, 0, 8,   20],
      ["Ogre mage",     8, 6, 12,  40],
      ["Dragon",        20,10,12, 100]
      ]
   @classmethod
   def GetRandomMonster(cls):
      return Monster(cls.monster_list[random.randint( 0,len(cls.monster_list)-1 )][Data.name_i])
   def __init__(self,name="Goblin"):
      self.name = name
      Player.__init__(self,self.name)
      for i in range( len( self.monster_list ) ):
         if( self.name == self.monster_list[i][Data.name_i] ):
            self.max_hp     = self.monster_list[i][Data.hp_i]
            self.max_mp     = self.monster_list[i][Data.mp_i]
            self.attack_die = self.monster_list[i][Data.damage_i]
            self.xp_value   = self.monster_list[i][Data.xp_reward_i]
   def get_xp_value(self):
      return self.xp_value
   def display(self):
      print("Type: " + self.name)
      print("HP:    " + str(self.max_hp-self.damage)  + "/" + str(self.max_hp))
      print("MP:    " + str(self.max_mp-self.used_mp) + "/" + str(self.max_mp))
      print("XP:    " + str(self.xp_value))
   def reward(self,player):
      print("=== You earn " + str(self.get_xp_value()) + "xp! ===")
      player.xp = player.xp + self.get_xp_value()