from Player import Player
from Monster import Monster
import random

class Battle:
   @classmethod
   def GetRandomBattle(cls,player):
      the_player = player;
      the_enemy = Monster.GetRandomMonster()
      the_battle = Battle(player,the_enemy)
      return the_battle
        
   def __init__(self,player,enemy):
      self.player = player;
      self.enemy = enemy;
      print("You've been attacked by a " + self.enemy.get_name() + "!")
   def is_active(self):
      return self.player.is_alive() and self.enemy.is_alive()
   def execute(self):
      self.do_battle(self.player,self.enemy)
   def do_battle(self,player,monster):
      # do battle loop
      while(True):
         # display a status
         print( player.get_name() + " " + player.get_hp())
         print( monster.get_name() + " " + monster.get_hp())
         # ask the player what to do
         decision_string = """1. Attack!
2. Cast a spell
3. Use an item
4. Run away
Choose an action: """
         choice = raw_input( decision_string )

         if( choice == "4" ):
            print("The " + monster.get_name() + " pursues you relentlessly!")
            return player
         if( choice == "3" ):
            print("You don't have any items! Make another choice.")
         if( choice == "2" ):
            if( player.get_mp() > 0 ):
               for i in range( Player.NumSpells() ):
                  print(str(i+1) + " " + Player.GetSpellName(i) )
               spell_choice = int(raw_input("Choose a spell: "))-1
               # we have the spell choice
               # now we need to compute mana used, and damage, and apply the same way
               # as an attack
               # TODO: player can cast spell if they have ANY mana, doesn't matter if
               # they have enough to cast it
               player_damage  = random.randint(1,Player.GetSpellDamage(spell_choice))
               player.use_mp( Player.GetSpellManaCost(spell_choice) ) 
               monster_damage = monster.get_attack_damage()
               print("You cast " + Player.GetSpellName(spell_choice) + " for " + \
                     str(player_damage) + " damage!")
               return self.apply_damages(player,player_damage,monster,monster_damage)
            else:
               print("You don't have enough magic power!")
         if( choice == "1" ):
            player_damage  = player.get_attack_damage()
            monster_damage = monster.get_attack_damage() 
            print("You attack for " + str(player_damage) + " damage!")
            return self.apply_damages(player,player_damage,monster,monster_damage)
      return player


   def apply_damages(self,player,player_damage,monster,monster_damage):
      monster.damaged( player_damage )      
      if( not monster.is_alive() ):
         print( "=== " + monster.get_name() + " is killed! ===")
         monster.reward(player)
         return player
      player.damaged( monster_damage )
      print( monster.get_name() + " hits you for " + str(monster_damage) + "!" )
      if( not player.is_alive() ):
         print("You are killed!")
         return player
      return player