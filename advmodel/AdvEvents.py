# Adv models a stack of events which lead into one another
# This module contains all of the event classes and their defaults

class Event:
   def __init__():
      self.next = None
      self.prev = None

class WelcomeEv(Event):
   def __init__():
      self.welcome = "Welcome to %s!  You have previously braved upon adventure!"
      self.select = "S)elect, C)reate, or D)elete a character"
      self.opts = ["s","c","d"]
      self.deletewarning = "Deleting your character is not reversible!  Are you sure?"
      self.toomanytocreate = "You have enough characters.  Finish the game with one or delete it!"

class StandingsEv(Event):
   def __init__():
      self.title = "%s Standings"
      self.select = "T)op 10    M)y rank    C)lasses"
      self.opts = ["t","m","c"]

class ShopEv(Event):
   def __init__():
      self.title = "Welcome to %s's store!  What would you like to buy?"
      self.select = "W)eapon, A)rmor, or I)tem: "
      self.opts = ["w","a","i"]

class SellItemEv(Event):
   def __init__():
      self.title = "Lighten Your LoadI"
      self.select = "Select an item to sell (n): "
      self.confirm = "Are you sure you want to sell %s for %dg?"
      self.done = "%s sold!"

class RewardEv(Event):
   def __init__():
      self.title = "You received:"

class QuitEv(Event):
   def __init__():
      self.title = "%s is shutting down.  Thanks for playing and come back soon!"

class PlayerMakeEv(Event):
   def __init__():
      self.entername = "Enter your name: "
      self.chooseclass = "Choose your class: "

class PlayerInfoEv(Event):
   def __init__():
      self.select = "D)one"
      self.inventory = "C)haracter inventory"
      self.achievements = "P)layer achievements"
      self.standings = "S)tandings",     
      self.opts = ["d","c","p","s"]

class DecideEv(Event):
   def __init__():
      self.title = "You must decide."

class BuyItemEv(Event):
   def __init__():
      self.title = "You bought %s!"
      self.equipreminder = "Don't forget to equip it!"
      self.usereminder = "You can use it in battle for an edge."
      self.noncombat = "This item can only be used outside of combat."

class AchievementsEv(Event):
   def __init__():
      self.title = "You are a well seasoned berserker!"
      self.subtitle = "Achievements received: "
      self.total = "%d/%d achievements unlocked!"
      self.select = "D)one"
      self.opts = ["d"]

