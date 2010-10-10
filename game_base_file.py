import random

class_list = [
      ["Wizard",        4, 25, 4],
      ["Fighter",       12,0,  8],
      ["Thief",         6, 0,  4],
      ["Hero",          10,15, 6],
      ["berserker",     6, 0,  20],
      ["warlock",       2, 100,3]
      ]

spell_list = [
      ["hurt",              5, 2],
      ["hurt more",         10,6],
      ["fireball",          6, 4],
      ["frost",             6, 3],
      ["lightning",         6, 5],
      ["inferno",           50,14],
      ["blizzard",          50,13],
      ["lightning storm",   50,15]
      ]

monster_list = [
      ["Goblin",        4, 0, 6],
      ["Ogre",          10,0, 10],
      ["Wolf",          8, 0, 8],
      ["Ogre Mage",     8, 6, 12],
      ["Dragon",        20,10,12]
      ]

name_i   = 0
hp_i     = 1
mp_i     = 2
damage_i = 3

spell_name_i    = 0
spell_damage_i  = 1
spell_mp_cost_i = 2

class Player:
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
     print("MP:    " + str(self.max_mp-self.used_mp) + "/" + str(self.max_mp))
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

class Monster(Player):
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

game_introduction = """Hello! Welcome to ComerGame!  ComerGame! is the awesomest text adventure roleplaying game you have ever played.

Please enter your name: """

def run_game():

   # create game introduction, query user for player name
   player_name = raw_input( game_introduction )
   print( "Welcome to ComerGame!, " + player_name )
   print( "Choose your class, " + player_name )
  
   # ask the user what class to play
   for i in range(len(class_list)):
      print( str(i+1) + " " + class_list[i][name_i] )
   chosen_class = raw_input( "Enter the number of the class you want to play: " )
   chosen_class = int(chosen_class) - 1

   # create a new player using the chosen class
   the_player = Player(player_name)
   the_player.create( class_list[chosen_class][name_i] )

   # show the newly created
   the_player.display()

   # now the player is created, we need to have an encounter with a monster
   # 1. create a random new monster type
   # 2. display the new monster to the player
   # 3. ask the player what they want to do: fight, spell, item, or run
   # 4. resolve battle - monster attacks player, player does whatever they selected
  
   # create monster and display it
   the_enemy = Monster(monster_list[random.randint( 0,len( monster_list )-1 )][name_i])
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
            for i in range( len( spell_list ) ):
               print(str(i+1) + " " + spell_list[i][0] )
            spell_choice = int(raw_input("choose a spell"))-1
            # we have the spell choice
            # now we need to compute mana used, and damage, and apply the same way
            # as an attack
            # TODO: player can cast spell if they have ANY mana, doesn't matter if
            # they have enough to cast it
            player_damage  = random.randint(1,spell_list[spell_choice][spell_damage_i])
            player.use_mp( spell_list[spell_choice][spell_mp_cost_i] )
            monster_damage = monster.get_attack_damage()
            print("You cast " + spell_list[spell_choice][spell_name_i] + " for " + \
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

