import Player
import Monster
from Game import Game

the_game = Game()

while(True):
   the_player = the_game.Run()
   if( the_player.is_alive() ):
      print(the_player.get_name() + " is alive!")
      break;
   else:
      print(the_player.get_name() + " was killed in the attack.")
      print("Your hero selection was too weak to survive.  Try again.")

print("You won the game!")

