import random

# Player class definition

name_i   = 0
hp_i     = 1
mp_i     = 2
damage_i = 3

spell_name_i    = 0
spell_damage_i  = 1
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
    ["blizzard",         50 13],
    ["lightning storm",  50 15]
    ]

  @classmethod
  def NumClasses(cls):
    return len(cls.class_list)
  @classmethod
  def NumSpells(cls):
    return len(cls.spell_list)
  @classmethod
  def GetClassName(cls,index)
    return self.class_list[index][name_i]
  def GetSpellName(cls,index)
    return self.spell_list[index][spell_name_i]
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
     for i in range( len( class_list ) ):
        if( class_type == class_list[i][name_i] ):
           self.max_hp     = class_list[i][hp_i]
           self.max_mp     = class_list[i][mp_i]
           self.attack_die = class_list[i][damage_i]
  def display(self):
     print("Name:  " + self.name)
     print("Class: " + self.class_type)
     print("HP:    " + str(self.max_hp-self.damage)  + "/" + str(self.max_hp))
     print("MP:    " + strself.max_mp-self.used_mp) + "/" + str(self.max_mp))
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
