# AdvJsonBuild receives a json object and returns 0 or more objects described
# by the custom json data.

import json
from advview import Log
from AdvBuilders import *

class JsonBuildTypes:
   TYPE = "object-type"
   
   # object types supported by AdvJsonBuild
   ARMOR = "armor"
   ARMORS = "armors"
   CLASS = "class"
   CLASSES = "classes"
   ITEM = "item"   
   ITEMS = "items"
   MONSTER = "monster"
   MONSTERS = "monsters"
   SETTINGS = "settings"
   SIDEQUEST = "sidequest"
   SIDEQUESTS = "sidequests"
   STORY = "story"
   STORIES = "stories"
   WEAPON = "weapon"
   WEAPONS = "weapons"

class AdvJsonBuild:
   def __init__(self):
      pass
   def __getBuilder(self,type):
      try:
         result = {
            JsonBuildTypes.ARMOR: ArmorBuilder(),
            JsonBuildTypes.ARMORS: ArmorsBuilder(),
            JsonBuildTypes.CLASS: ClassBuilder(),
            JsonBuildTypes.CLASSES: ClassesBuilder(),
            JsonBuildTypes.ITEM: ItemBuilder(),
            JsonBuildTypes.ITEMS: ItemsBuilder(),
            JsonBuildTypes.MONSTER: MonsterBuilder(),
            JsonBuildTypes.MONSTERS: MonstersBuilder(),
            JsonBuildTypes.SETTINGS: SettingsBuilder(),
            JsonBuildTypes.SIDEQUEST: SideQuestBuilder(),
            JsonBuildTypes.SIDEQUESTS: SideQuestsBuilder(),         
            JsonBuildTypes.STORY: StoryBuilder(),
            JsonBuildTypes.STORIES: StoriesBuilder(),
            JsonBuildTypes.WEAPON: WeaponBuilder(),
            JsonBuildTypes.WEAPONS: WeaponsBuilder()
         } [type]
         return result
      except KeyError, err:
         Log(Log.BUILDERROR,"Object key " + type + " not a valid AdvJson object")
         return None
      
   def Build(self,jsonData):
      try:
         # jsonDict may be a list of dictionaries
         listTest = jsonData[0]
      except KeyError, err:
         # or it is a dictionary, so insert it into a list for simplicity
         jsonData = [jsonData]
      except Exception, err:
         # or there was an error
         Log(Log.BUILDERROR,"AdvJsonBuild unable to build an object " + str(jsonData))
         return None
         
      # iterate over list, making appropriate builders each time
      resultList = []
      for jsonDict in jsonData:
         try:
            builder = self.__getBuilder(jsonDict[JsonBuildTypes.TYPE])
         except Exception, err:
            builder = None
         if None != builder:
            builder.SetJson(jsonDict)
            resultList.append(builder.Build())
         
      return resultList
      