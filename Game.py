from Player import Player
from Battle import Battle

class Game:

    game_introduction = """Hello! Welcome to Berserkers and Warlocks!  Bererkers and Warlocks! is the awesomest text adventure roleplaying game you have ever played.

    Please enter your name: """

    def Run(self):
        # Main game loop
        return self.run_game()
    

    def run_game(self):
       # create game introduction, query user for player name
       player_name = raw_input( self.game_introduction )
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

       battle = Battle.GetRandomBattle(the_player)
       battle.execute()

       return the_player