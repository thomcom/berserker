from Player import Player
from Battle import Battle
from SaveGameProvider import SaveGameProvider
from PlayerCreate import PlayerCreate
from Data import Data
from MainStory import MainStory

class Game:

   game_introduction = "Hello! Welcome to " + Data.game_name + "! " + Data.game_name + " is the awesomest text adventure roleplaying game you have ever played.  You will not play the same game twice."""

   def Run(self):
      # Main game loop
      return self.run_game()

   def run_game(self):
      saveGames = SaveGameProvider()
      if( saveGames.getSaveCount() == 0 ):
         the_player = PlayerCreate.CreateFirst()
      else:
         the_player = GameLoader.LoadGameDialog()         
        
      # display player
      the_player.display()
      
      # now the player is created, we need to load a random-ish main storyline
      the_story = MainStory(the_player)

      # now the player is created, we need to have an encounter with a monster
      # 1. create a random new monster type
      # 2. display the new monster to the player
      # 3. ask the player what they want to do: fight, spell, item, or run
      # 4. resolve battle - monster attacks player, player does whatever they selected

      the_player = self.run_battles_till_death(the_player)
      
      print(the_player.get_name() + " was killed in the attack.")
      print("Your hero selection was too weak to survive.  Try again.")
      return the_player
      
   def run_battles_till_death(self,the_player):
      while( the_player.is_alive() ):
         battle = Battle.GetRandomBattle(the_player)
         while(battle.is_active()):
            battle.execute()
      return the_player
         
         