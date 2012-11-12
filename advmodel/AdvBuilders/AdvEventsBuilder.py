from advmodel.AdvBuilders import AbstractBuilder
from advmodel.AdvEvents import *
from advview.Log import Log

class WelcomeEvBuilder(AbstractBuilder):
   def Build(self):
      result = WelcomeEv()
      try:
         result.welcome = str(self.jsonData)["welcome"]
         result.select = str(self.jsonData)["select"]
         result.opts = str(self.jsonData)["opts"]
         result.deletewarning = str(self.jsonData)["delete-warning"]
         result.toomanytocreate = str(self.jsonData)["too-many-tocreate"]
      except Exception, err:
         Log(Log.BUILDERROR,"Problem reading WelcomeEv from " + str(self.jsonData))
         Log(Log.BUILDERROR,str(str(err.__class__))+str(err))
      return result

class StandingsEvBuilder(AbstractBuilder):
   def Build(self):
      result = StandingsEv()
      try:
         result.title = str(self.jsonData)["title"]
         result.select = str(self.jsonData)["select"]
         result.opts = str(self.jsonData)["opts"]
      except Exception, err:
         Log(Log.BUILDERROR,"Problem reading StandingsEv from " + str(self.jsonData))
         Log(Log.BUILDERROR,str(err.__class__)+str(err))
      return result

class ShopEvBuilder(AbstractBuilder):
   def Build(self):
      result = ShopEv()
      try:
         result.title = str(self.jsonData)["title"]
         result.select = str(self.jsonData)["select"]
         result.opts = str(self.jsonData)["opts"] 
      except Exception, err:
         Log(Log.BUILDERROR,"Problem reading ShopEv from " + str(self.jsonData))
         Log(Log.BUILDERROR,str(err.__class__)+str(err))
      return result

class SellItemEvBuilder(AbstractBuilder):
   def Build(self):
      result = SellItemEv()
      try:
         result.title = str(self.jsonData)["title"]
         result.select = str(self.jsonData)["select"]
         result.confirm = str(self.jsonData)["confirm"] 
         result.done = str(self.jsonData)["done"] 
      except Exception, err:
         Log(Log.BUILDERROR,"Problem reading SellItemEv from " + str(self.jsonData))
         Log(Log.BUILDERROR,str(err.__class__)+str(err))
      return result

class RewardEvBuilder(AbstractBuilder):
   def Build(self):
      result = RewardEv()
      try:
         result.title = str(self.jsonData)["title"] 
      except Exception, err:
         Log(Log.BUILDERROR,"Problem reading RewardEv from " + str(self.jsonData))
         Log(Log.BUILDERROR,str(err.__class__)+str(err))
      return result

class QuitEvBuilder(AbstractBuilder):
   def Build(self):
      result = QuitEv()
      try:
         result.title = str(self.jsonData)["title"] 
      except Exception, err:
         Log(Log.BUILDERROR,"Problem reading QuitEv from " + str(self.jsonData))
         Log(Log.BUILDERROR,str(err.__class__)+str(err))
      return result

class PlayerMakeEvBuilder(AbstractBuilder):
   def Build(self):
      result = PlayerMakeEv()
      try:
         result.entername = str(self.jsonData)["enter-name"] 
         result.chooseclass = str(self.jsonData)["choose-class"] 
      except Exception, err:
         Log(Log.BUILDERROR,"Problem reading PlayerMakeEv from " + str(self.jsonData))
         Log(Log.BUILDERROR,str(err.__class__)+str(err))
      return result
      
class PlayerInfoEvBuilder(AbstractBuilder):
   def Build(self):
      result = PlayerInfoEv()
      try:
         result.select = str(self.jsonData)["select"] 
         result.inventory = str(self.jsonData)["inventory"] 
         result.achievements = str(self.jsonData)["achievements"] 
         result.standings = str(self.jsonData)["standings"] 
         result.opts = str(self.jsonData)["opts"] 
      except Exception, err:
         Log(Log.BUILDERROR,"Problem reading PlayerInfoEv from " + str(self.jsonData))
         Log(Log.BUILDERROR,str(err.__class__)+str(err))
      return result
      
class DecideEvBuilder(AbstractBuilder):
   def Build(self):
      result = DecideEv()
      try:
         result.title = str(self.jsonData)["title"] 
      except Exception, err:
         Log(Log.BUILDERROR,"Problem reading DecideEv from " + str(self.jsonData))
         Log(Log.BUILDERROR,str(err.__class__)+str(err))
      return result
      
class BuyItemEvBuilder(AbstractBuilder):
   def Build(self):
      result = BuyItemEv()
      try:
         result.title = str(self.jsonData)["title"] 
         result.equipreminder = str(self.jsonData)["equip-reminder"] 
         result.usereminder = str(self.jsonData)["use-reminder"] 
         result.noncombat = str(self.jsonData)["non-combat"] 
      except Exception, err:
         Log(Log.BUILDERROR,"Problem reading BuyItemEv from " + str(self.jsonData))
         Log(Log.BUILDERROR,str(err.__class__)+str(err))
      return result

class AchievementsEvBuilder(AbstractBuilder):
   def Build(self):
      result = AchievementsEv()
      try:
         result.title = str(self.jsonData)["title"] 
         result.subtitle = str(self.jsonData)["subtitle"] 
         result.total = str(self.jsonData)["total"] 
         result.select = str(self.jsonData)["select"] 
         result.opts = str(self.jsonData)["opts"] 
      except Exception, err:
         Log(Log.BUILDERROR,"Problem reading AchievementsEv from " + str(self.jsonData))
         Log(Log.BUILDERROR,str(err.__class__)+str(err))
      return result
