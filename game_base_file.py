import random
import Player
from Monster import Monster
from Player import Player
game_introduction = """Hello! Welcome to Berserkers and Warlocks!  Bererkers and Warlocks! is the awesomest text adventure roleplaying game you have ever played.

Please enter your name: """

def run_game():

   # create game introduction, query user for player name
   player_name = raw_input( game_introduction )
   print( "Welcome to Berserkers and Warlocks!, " + player_name )
   print( "Choose your class, " + player_name )
  
   # ask the user what class to play
   for i in range(Player.NumClasses()):
      print( str(i+1) + " " + Player.GetClassName(i) )
   chosen_class = raw_input( "Enter the number of the class you want to play: " )
   chosen_class = int(chosen_class) - 1

   # create a new player using the chosen class
   the_player = Player(player_name)
   the_player.create( Player.GetClassName(chosen_class) )

   # show the newly created
   the_player.display()

   # now the player is created, we need to have an encounter with a monster
   # 1. create a random new monster type
   # 2. display the new monster to the player
   # 3. ask the player what they want to do: fight, spell, item, or run
   # 4. resolve battle - monster attacks player, player does whatever they selected
  
   # create monster and display it
   the_enemy = Monster.GetRandomMonster()
   print("You've been attacked by a " + the_enemy.get_name() + "!")
  
   the_player = do_battle(the_player,the_enemy)

   return the_player

def do_battle(player,monster):
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
         print("You escaped!")
         return player
      if( choice == "3" ):
         print("You don't have any items! Make another choice.")
      if( choice == "2" ):
         if( player.get_mp() > 0 ):
            for i in range( Player.NumSpells() ):
               print(str(i+1) + " " + Player.GetSpellName(i) )
            spell_choice = int(raw_input("choose a spell"))-1
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
            return apply_damages(player,player_damage,monster,monster_damage)
         else:
            print("You don't have enough magic power!")
      if( choice == "1" ):
         player_damage  = player.get_attack_damage()
         monster_damage = monster.get_attack_damage() 
         monster.damaged( player_damage )
         print("You attack for " + str(player_damage) + " damage!")
         return apply_damages(player,player_damage,monster,monster_damage)
   return player


def apply_damages(player,player_damage,monster,monster_damage):
   if( not monster.is_alive() ):
      print( monster.get_name() + " is killed!")
      return player
   player.damaged( monster_damage )
   print( monster.get_name() + " hits you for " + str(monster_damage) + "!" )
   if( not player.is_alive() ):
      print("You are killed!")
      return player
   return player

while(True):
   the_player = run_game()
   if( the_player.is_alive() ):
      print(the_player.get_name() + " is alive!")
      break;
   else:
      print(the_player.get_name() + " was killed in the attack.")
   print("Your hero selection was too weak to survive.  Try again.")

print("You won the game!")

