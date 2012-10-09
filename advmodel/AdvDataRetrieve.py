##########################################################
# Thomson Comer 10/8/2012 AdvDataRetrieve.py
#
##########################################################
import json
import io

# loads local file game data
class AdvFileDataRetrieve:
   def __init__(self):
      print(__file__)
      self.defaultsPath = "./json/English.json"
      self.itemPath = "./json/Items.json"
      self.weaponPath = "./json/Weapons.json"
      self.classPath = "./json/Classes.json"
      self.monsterPath = "./json/Monsters.json"
      self.sideQuestPath = "./json/Sidequests.json"
      self.storyJson = "./json/StoryDefault.json"
   def __getJson(self,path):
      try:
         if not isinstance(path,basestring):
            raise TypeError("json path not a string")
         classFile = io.open(path)
         classJson = json.loads(classFile.read())
         return classJson
      except TypeError, err:
         Output.Log(str(err))
      except Exception, err:
         Output.Log("Error getting json " + str(err))
   def getdefaultsJson(self):
      return self.__getJson(self.modelDefaultsPath)
   def getItemJson(self):
      return self.__getJson(self.itemPath)
   def getWeaponJson(self):
      return self.__getJson(self.weaponPath)
   def getClassJson(self):
      return self.__getJson(self.classPath)
   def getMonsterJson(self):
      return self.__getJson(self.monsterPath)
   def getSideQuestJson(self):
      return self.__getJson(self.sideQuestPath)
   def getStoryJson(self):
      return self.__getJson(self.storyJson)

# Will eventually asynchronously retrieve data from http server
class AdvHttpDataRetrieve:
   def __init__(self): pass
   def getdefaultsJson(self): pass
   def getItemJson(self): pass
   def getWeaponJson(self): pass
   def getClassJson(self): pass
   def getMonsterJson(self): pass 
   def getSideQuestJson(self): pass
   def getStoryJson(self): pass

