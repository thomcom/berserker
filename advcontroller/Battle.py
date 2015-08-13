from advmodel import Player
from advmodel.Monster import *
import random
from advview.ETio import *

class Battle:
   @classmethod
   def GetRandomBattle(cls,player):
      the_player = player;
      the_enemy = Monster.GetRandomMonster()
      the_battle = Battle(player,the_enemy)
      return the_battle
   @classmethod
   def GetBattleWithEnemy(cls,player,enemy):
      return Battle(player, enemy)
   def __init__(self,player,enemy):
      self.player = player;
      self.enemy = enemy;
      Output.Main("You've been attacked by a " + self.enemy.get_name() + "!")
   def is_active(self):
      return self.player.is_alive() and self.enemy.is_alive()
   def execute(self):
      self.do_battle(self.player,self.enemy)
   def do_battle(self,player,monster):
      # do battle loop
      while(True):
         # display a status
         Output.Main( player.get_name() + " " + player.get_hp())
         Output.Main( monster.get_name() + " " + monster.get_hp())
         # ask the player what to do
         decision_string = """1. Attack!
2. Cast a spell
3. Use an item
4. Run away
Choose an action: """
         choice = Input.GetKeyPressWithPrompt( decision_string )

         if( choice == "4" ):
            Output.Main("The " + monster.get_name() + " pursues you relentlessly!")
            return player
         if( choice == "3" ):
            Output.Main("You don't have any items! Make another choice.")
         if( choice == "2" ):
            if( player.get_mp() > 0 ):
               for i in range( Player.NumSpells() ):
                  Output.Main(str(i+1) + " " + Player.GetSpellName(i) )
               spell_choice = int(Input.GetKeyPressWithPrompt("Choose a spell: "))-1
               # we have the spell choice
               # now we need to compute mana used, and damage, and apply the same way
               # as an attack
               # TODO: player can cast spell if they have ANY mana, doesn't matter if
               # they have enough to cast it
               player_damage  = random.randint(1,Player.GetSpellDamage(spell_choice))
               player.use_mp( Player.GetSpellManaCost(spell_choice) )
               monster_damage = monster.get_attack_damage()
               Output.Main("You cast " + Player.GetSpellName(spell_choice) + " for " + \
                     str(player_damage) + " damage!")
               return self.apply_damages(player,player_damage,monster,monster_damage)
            else:
               Output.Main("You don't have enough magic power!")
         if( choice == "1" ):
            player_damage  = player.get_attack_damage()
            monster_damage = monster.get_attack_damage()
            Output.Main("You attack for " + str(player_damage) + " damage!")
            return self.apply_damages(player,player_damage,monster,monster_damage)
      return player

   def apply_damages(self,player,player_damage,monster,monster_damage):
      monster.damaged( player_damage )
      if( not monster.is_alive() ):
         Output.Main( "=== " + monster.get_name() + " is killed! ===")
         monster.reward(player)
         return player
      player.damaged( monster_damage )
      Output.Main( monster.get_name() + " hits you for " + str(monster_damage) + "!" )
      if( not player.is_alive() ):
         if monster.is_lethal:
            Output.Main("You are killed!")
         else:
            player.damage = player.max_hp - 1

      return player
