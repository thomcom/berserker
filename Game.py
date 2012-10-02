from Player import Player
from Battle import Battle
from SaveGameProvider import SaveGameProvider
from PlayerCreate import PlayerCreate
from Data import Data
from MainStory import MainStory
from ETio import Output
from ETio import Input
from MainStory import Menu

class Game:

   game_introduction = "Hello! Welcome to " + Data.game_name + "! " + Data.game_name + " is the awesomest text adventure roleplaying game you have ever played.  You will not play the same game twice."""

   def __init__(self):
      self.default_menu = Menu(["i","a","q"],"i)nspect self a)bandon quest q)uit")

   def Run(self):
      MainStory.LoadAllStories()
      
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

      self.runStoryMain(the_story,the_player)
      
      Output.Main(the_player.get_name() + " was killed in the action.")
      Output.Main("Your hero selection was too weak to survive.  Try again.")
      return the_player
         
   def runStoryMain(self,the_story,the_player):
      storynum = 0;
      while( the_player.is_alive() ):
         response = Input.GetKeyPressWithMenu( the_story.menu, self.default_menu )
         if( response == 0 or response == 1 ):
            Output.Main(the_story.events[storynum].message)
            battle = Battle.GetRandomBattle(the_player)
            while(battle.is_active()):
               battle.execute()
            if( the_player.is_alive() ):
               Output.Main( the_story.events[storynum].success )
            else:
               Output.Main( the_story.events[storynum].fail )
               return the_player
            storynum = storynum + 1   
         elif( response == 2 ):
            Output.Main("There are no stores in the wasteland.")
         elif( response == 3 ):
            Output.Main("You sleep fitfully (Hp + 1).")
            the_player.healed(1)
         elif( response == 4 ):
            the_player.display()
         elif( response == 5 ):
            return the_player
         elif( response == 6 ):
            return the_player
         else:
            Output.Main("Invalid Selection")
         
      