# AdvModel stores data for Adventure Game
from advview import Log

class Model:
   def __init__(self):
      Log(Log.STATUS,"Initialize Model")
   def preloadClasses(self):
      Log(Log.STATUS,"Preloading classes")
   def preloadMonsters(self):
      Log(Log.STATUS,"Preloading monsters")
   def preloadSideQuests(self):
      Log(Log.STATUS,"Preloading sidequests")
   def preloadItems(self):
      Log(Log.STATUS,"Preloading items")

