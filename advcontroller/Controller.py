# AdvController runs Berserker!
from advview import Log

class Controller:
   def __init__(self):
      Log(Log.STATUS,"Controller constructor")
      self.model = 0
      self.view  = 0
   def initialize(self,platform_type):
      Log(Log.STATUS,"Controller initialize (" + platform_type + ")")
   def setModel(self,model):
      Log(Log.STATUS,"Controller setModel")
      self.model = model
   def setView(self,view):
      Log(Log.STATUS,"Controller setView")
      self.view = view

   def runGame(self):
      Log(Log.STATUS,"Controller runGame")
