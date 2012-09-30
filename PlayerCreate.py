from Player import Player
from Data import Data

class PlayerCreate:
   create_first_message = "This if your first time playing " + Data.game_name + """".
You must create your first character.  We have simplified this process for you.

Enter your name: """
   create_later_message = """Attempt to delve the dungeons again.  Create a new character.
   
Enter your name: """
   
   @classmethod
   def CreateFirst(cls):
      # create game introduction, query user for player name
      player_name = raw_input( cls.create_first_message )
      print( "Choose your class, " + player_name )

      # ask the user what class to play
      for i in range(Player.NumClasses()):
         print( str(i+1) + " " + Player.GetClassName(i) )
      chosen_class = raw_input( "Enter the number of the class you want to play: " )
      chosen_class = int(chosen_class) - 1

      # create a new player using the chosen class
      the_player = Player(player_name)
      the_player.create( Player.GetClassName(chosen_class) )
      return the_player