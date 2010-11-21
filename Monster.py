import Player
from Player import Player

#Monster class definition

monster_list = [
      ["Goblin",        4, 0, 6],
      ["Ogre",          10,0, 10],
      ["Wolf",          8, 0, 8],
      ["Ogre Mage",     8, 6, 12],
      ["Dragon",        20,10,12]
      ]

class Monster(Player):
   @classmethod
   def GetRandomMonster(cls):
      return Monster(monster_list[random.randint( 0,len(monster_list)-1 )][name_i]
   def __init__(self,name="Monster"):
      self.name = name
      Player.__init__(self,self.name)
      for i in range( len( monster_list ) ):
         if( self.name == monster_list[i][name_i] ):
            self.max_hp     = monster_list[i][hp_i]
            self.max_mp     = monster_list[i][mp_i]
            self.attack_die = monster_list[i][damage_i]
   def display(self):
      print("Type: " + self.name)
      print("HP:    " + str(self.max_hp-self.damage)  + "/" + str(self.max_hp))
      print("MP:    " + str(self.max_mp-self.used_mp) + "/" + str(self.max_mp))
   
