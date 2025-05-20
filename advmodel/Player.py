import random
from .Data import Data
from advview.ETio import Output

class Player:
  class_list = [
#name
#starting hp
#starting mp
#starting damage
#starting initiative
    ["Wizard",        4,  25,   4, 2],
    ["Fighter",      12,   0,   8, 3],
    ["Thief",         6,   0,   4, 4],
    ["Hero",         10,  15,   6, 3],
    ["Berserker",     6,   0,  20, 1],
    ["Warlock",       5, 100,   3, 2],
    ["Knight",       20,   0,  10, 2],
    ["Paladin",      10,   0,  15, 2],
    ]

#name
#damage 1-n
#mp cost
  spell_list = [
    ["Hurt",              5, 2],
    ["Hurt more",        10, 6],
    ["Fireball",          6, 4],
    ["Frost",             6, 3],
    ["Lightning",         6, 5],
    ["Inferno",          50,14],
    ["Blizzard",         50,13],
    ["Lightning storm",  50,15]
    ]

  @classmethod
  def NumClasses(cls):
    return len(cls.class_list)
  @classmethod
  def NumSpells(cls):
    return len(cls.spell_list)
  @classmethod
  def GetClassName(cls,index):
    return cls.class_list[index][Data.name_i]
  @classmethod
  def GetSpellName(cls,index):
    return cls.spell_list[index][Data.spell_name_i]
  @classmethod
  def GetSpellDamage(cls,index):
     return cls.spell_list[index][Data.spell_damage_i]
  @classmethod
  def GetSpellManaCost(cls,index):
     return cls.spell_list[index][Data.spell_mp_cost_i]
  def __init__(self,name):
     self.class_type = "Classless"
     self.name       = name
     self.level      = 1
     self.xp         = 0 
     self.max_hp     = 4
     self.max_mp     = 0
     self.damage     = 0
     self.used_mp    = 0
     self.attack_die = 2
     self.initiative = 1
     self.story_progress = 0
  def create(self,class_type):
     self.class_type = class_type
     for i in range( len( self.class_list ) ):
        if( class_type == self.class_list[i][Data.name_i] ):
           self.max_hp     = self.class_list[i][Data.hp_i]
           self.max_mp     = self.class_list[i][Data.mp_i]
           self.attack_die = self.class_list[i][Data.damage_i]
  def display(self):
     Output.Main("Name:  " + self.name)
     Output.Main("Class: " + self.class_type)
     Output.Main("Level: " + str(self.level) + " Exp: " + str(self.xp))
     Output.Main("HP:    " + str(self.max_hp-self.damage)  + "/" + str(self.max_hp))
     Output.Main("MP:    " + str(self.max_mp-self.used_mp) + "/" + str(self.max_mp))
  def damaged(self,amount):
     self.damage = self.damage + amount
  def healed(self,amount):
     self.damage = self.damage - amount
     if( self.damage < 0 ):
        self.damage = 0
  def get_name(self):
     return self.name
  def is_alive(self):
     if( self.max_hp-self.damage > 0 ):
        return True
     else:
        return False
  def use_mp(self,amount):
     self.used_mp += amount
  def get_mp(self):
     return self.max_mp - self.used_mp
  def get_hp(self):
     return str(self.max_hp - self.damage) + "/" + str(self.max_hp)
  def get_attack_damage(self):
     return random.randint(1,self.attack_die)
