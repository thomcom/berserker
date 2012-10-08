from Player import Player
from advview.ETio import *
import random
import math
from Data import Data

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
      Output.Log("Type: " + self.name)
      Output.Log("HP:    " + str(self.max_hp-self.damage)  + "/" + str(self.max_hp))
      Output.Log("Attack: " + str(self.attack_die))
      Output.Log("XP:    " + str(self.xp_value))
      Output.Log("Battle: " + str(self.battle))
      try:
         Output.Log("Loot: " + str(self.loot))
      except:
         Output.Log("No loot")
   def reward(self,player):
      Output.Main("=== You earn " + str(self.get_xp_value()) + "xp! ===")
      player.xp = player.xp + self.get_xp_value()

class MonsterBuilder:
   def __init__(self):
      self.monster = Monster()
   def setJson(self,json):
      self.jsonSource = json
   def build(self):
      try:
         json = self.jsonSource
         monster = Monster()
         monster.name = json['name']
         monster.level = json['level']
         monster.max_hp = math.pow(monster.level,2) + 4
         monster.attack_die = math.pow(monster.level,2)/1.8 + 4
         monster.xp_value = math.pow(monster.level,4) + 4
         monster.battle = json['battle']
         if 'loot' in json:
            monster.loot = json['loot']
         return monster
      except Exception as err:
         Output.Log("Tried to load bad Monster : " + str(self.jsonSource))
         Output.Log(str(err))
         raise
         return 0
      
      
      
      
