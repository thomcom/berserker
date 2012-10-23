# AdvModel stores data for Adventure Game
from advview import Log
from AdvDataRetrieve import AdvFileJsonDataRetrieve
from AdvJsonBuild import AdvJsonBuild

class Model:
   def __init__(self):
      Log(Log.STATUS,"Initialize Model")
      # Change this to AdvHttpDataRetrieve to convert
      # game to remote data source instead of local
      self.data = AdvFileJsonDataRetrieve()
      self.builder = AdvJsonBuild()
      
      # Data stored by local model
      self.settings = []
      self.player = []
      self.items = []
      self.weapons = []
      self.classes = []
      self.monsters = []
      self.side_quests = []
      self.stories = []

###########################################################
# Data preloading
###########################################################
   def LoadSettings(self):
      Log(Log.STATUS,"Loading settings")
      settings = self.data.GetDefaults()
      self.settings = self.builder.Build(settings)
   def PreloadItems(self):
      Log(Log.STATUS,"Preloading items")
      items = self.data.GetItems()
      self.items = self.builder.Build(items)
   def PreloadWeapons(self):
      Log(Log.STATUS,"Preloading weapons")
      weapons = self.data.GetWeapons()
      self.weapons = self.builder.Build(weapons)
   def PreloadArmor(self):
      Log(Log.STATUS,"Preloading armor")
      armor = self.data.GetArmor()
      self.armor = self.builder.Build(armor)
   def PreloadClasses(self):
      Log(Log.STATUS,"Preloading classes")
      classes = self.data.GetClasses()
      self.classes = self.builder.Build(classes)
   def PreloadMonsters(self):
      Log(Log.STATUS,"Preloading monsters")
      monsters = self.data.GetMonsters()
      self.monsters = self.builder.Build(monsters)
   def PreloadSideQuests(self):
      Log(Log.STATUS,"Preloading sidequests")
      sidequests = self.data.GetSideQuests()
      self.side_quests = self.builder.Build(sidequests)
   def PreloadStories(self):
      Log(Log.STATUS,"Preloading stories")
      stories = self.data.GetStories()
      self.stories = self.builder.Build(stories)

