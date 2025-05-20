##########################################################
# Thomson Comer 10/8/2012 AdvDataRetrieve.py
#
##########################################################
import json
import io

from advview import Log

# loads local file game data
class AdvFileJsonDataRetrieve:
   def __init__(self):
      self.armorPath = "./json/Armor.json"
      self.defaultsPath = "./json/English.json"
      self.itemPath = "./json/Items.json"
      self.weaponPath = "./json/Weapons.json"
      self.classPath = "./json/Classes.json"
      self.monsterPath = "./json/Monsters.json"
      self.sideQuestPath = "./json/Sidequests.json"
      self.storyJson = "./json/StoryDefault.json"
   def __getJson(self,path):
      try:
         if not isinstance(path,str):
            raise TypeError("json path not a string")
         classFile = io.open(path)
         classJson = json.loads(classFile.read())
         return classJson
      except TypeError as err:
         Log(Log.FILEERROR,str(err))
      except Exception as err:
         Log(Log.DATAERROR,"Error getting json " + str(err))
   def GetArmor(self):
      return self.__getJson(self.armorPath)
   def GetDefaults(self):
      return self.__getJson(self.defaultsPath)
   def GetItems(self):
      return self.__getJson(self.itemPath)
   def GetWeapons(self):
      return self.__getJson(self.weaponPath)
   def GetClasses(self):
      return self.__getJson(self.classPath)
   def GetMonsters(self):
      return self.__getJson(self.monsterPath)
   def GetSideQuests(self):
      return self.__getJson(self.sideQuestPath)
   def GetStories(self):
      return self.__getJson(self.storyJson)

# Will eventually asynchronously retrieve data from http server
class AdvHttpJsonDataRetrieve:
   def __init__(self): pass
   def GetDefaults(self): pass
   def GetItem(self): pass
   def GetWeapon(self): pass
   def GetClass(self): pass
   def GetMonster(self): pass 
   def GetSideQuest(self): pass
   def GetStory(self): pass

