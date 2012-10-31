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

   # dynamic model data loader
   def AddObjects(self,objects):
      # put objects into list
      try:
         testList = objects[0]
      except Exception, err:
         objects = [objects]

      for obj in objects:
         pass
         

###########################################################
# Data preloading
###########################################################
   def LoadSettings(self):
      Log(Log.STATUS,"Loading settings")
      settings = self.data.GetDefaults()
      self.settings = self.builder.Build(settings)
      Log(Log.DUMP,"Dumping settings:\n"+str(self.settings))
   def PreloadItems(self):
      Log(Log.STATUS,"Preloading items")
      items = self.data.GetItems()
      self.items = self.builder.Build(items)
      Log(Log.DUMP,"Dumping items:\n"+str(self.items))
   def PreloadWeapons(self):
      Log(Log.STATUS,"Preloading weapons")
      weapons = self.data.GetWeapons()
      self.weapons = self.builder.Build(weapons)
      Log(Log.DUMP,"Dumping weapons:\n"+str(self.weapons))
   def PreloadArmor(self):
      Log(Log.STATUS,"Preloading armor")
      armor = self.data.GetArmor()
      self.armor = self.builder.Build(armor)
      Log(Log.DUMP,"Dumping armor:\n"+str(self.armor))
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

