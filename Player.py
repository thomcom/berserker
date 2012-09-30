import random
import Data

#: Player class definition

Data.name_i   = 0
Data.hp_i     = 1
Data.mp_i     = 2
Data.damage_i = 3

Data.spell_name_i    = 0
Data.spell_damage_i  = 1
spell_mp_cost_i = 2

class Player:
  class_list = [
    ["Wizard",        4,  25,   4],
    ["Fighter",      12,   0,   8],
    ["Thief",         6,   0,   4],
    ["Hero",         10,  15,   6],
    ["berserker",     6,   0,  20],
    ["warlock",       5, 100,   3],
    ["knight",       20,   0,  10],
    ["paladin",      10,   0,  15],
    ]

  spell_list = [
    ["hurt",              5, 2],
    ["hurt more",        10, 6],
    ["fireball",          6, 4],
    ["frost",             6, 3],
    ["lightning",         6, 5],
    ["inferno",          50,14],
    ["blizzard",         50,13],
    ["lightning storm",  50,15]
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
  def GetSpellName(cls,index):
    return self.spell_list[index][Data.spell_name_i]
  def __init__(self,name):
     self.class_type = "Classless"
     self.name       = name
     self.max_hp     = 4
     self.max_mp     = 0
     self.damage     = 0
     self.used_mp    = 0
     self.attack_die = 2
  def create(self,class_type):
     self.class_type = class_type
     for i in range( len( self.class_list ) ):
        if( class_type == self.class_list[i][Data.name_i] ):
           self.max_hp     = self.class_list[i][Data.hp_i]
           self.max_mp     = self.class_list[i][Data.mp_i]
           self.attack_die = self.class_list[i][Data.damage_i]
  def display(self):
     print("Name:  " + self.name)
     print("Class: " + self.class_type)
     print("HP:    " + str(self.max_hp-self.damage)  + "/" + str(self.max_hp))
     print("MP:    " + str(self.max_mp-self.used_mp) + "/" + str(self.max_mp))
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
     self.used_mp = self.used_mp - amount
  def get_mp(self):
     return self.max_mp - self.used_mp
  def get_hp(self):
     return str(self.max_hp - self.damage) + "/" + str(self.max_hp)
  def get_attack_damage(self):
     return random.randint(1,self.attack_die)
