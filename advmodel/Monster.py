from .Player import Player
from advview.ETio import *
import random
import math
from .Data import Data

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
      # Loot is processed after battle; don't log it here
  def reward(self,player):
     Output.Main("=== You earn " + str(self.get_xp_value()) + "xp! ===")
     player.xp = player.xp + self.get_xp_value()
     found = []
     if self.loot:
        loot_entries = self.loot if isinstance(self.loot, list) else [self.loot]
        for entry in loot_entries:
           if isinstance(entry, dict):
              item = entry.get('item')
              if item:
                 if isinstance(item, dict):
                    chance = int(item.get('chance', 100))
                    if random.randint(1, 100) <= chance:
                       player.add_item(item.get('name'))
                       found.append(item.get('name'))
                 else:
                    player.add_item(item)
                    found.append(item)
              gold = entry.get('gold')
              if gold:
                 minimum = int(gold.get('minimum', 0))
                 rand = int(gold.get('random', 0))
                 amount = minimum + random.randint(0, rand)
                 player.add_gold(amount)
                 found.append(f"{amount}g")
           elif isinstance(entry, str):
              player.add_item(entry)
              found.append(entry)
     if found:
        msg = getattr(self, 'corpse_message', "You found %s on its smoldering corpse!")
        Output.Main(msg % (" and ".join(found)))

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
         monster.max_hp = int(math.pow(monster.level,2) + 4)
         monster.attack_die = int(math.pow(monster.level,2)/1.8 + 4)
         monster.xp_value = int(math.pow(monster.level,4) + 4)
         monster.battle = json['battle']
         monster.loot = json.get('loot')
         monster.corpse_message = json.get('corpse_message')
         monster.is_lethal = True
         if 'lethal' in json:
            monster.is_lethal = json['lethal']
         return monster
      except Exception as err:
         Output.Log("Tried to load bad Monster : " + str(self.jsonSource))
         Output.Log(str(err))
         raise
         return 0
