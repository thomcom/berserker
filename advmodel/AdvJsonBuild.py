# AdvJsonBuild receives a json object and returns 0 or more objects described
# by the custom json data.

import json

class JsonBuildTypes:
   TYPE = "object-type"
   
   # object types supported by AdvJsonBuild
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

class AdvJsonBuild:
   def __init__(self):
      pass
   def Build(self,jsonDict):
      # jsonDict better be a dictionary, and contain a self identifying type key
      try:
         self.currentType = jsonDict[JsonBuildTypes.TYPE]
      except keyError:
         Log(Log.DATAERROR,"AdvJsonBuild unable to parse json object: " + jsonDict + " for " + JsonBuildTypes.TYPE)
      except TypeError:
         Log(Log.DATAERROR,"AdvJsonBuild unable to parse object: " + jsonDict + " not a dictionary.")
         
      # identify type of json data
      # with large conditional block
      builder = {
         JsonBuildTypes.CLASS: ClassBuilder()
         JsonBuildTypes.CLASSES: ClassesBuilder()
         JsonBuildTypes.ITEM: ItemBuilder()
         JsonBuildTypes.ITEMS: ItemsBuilder()
         JsonBuildTypes.MONSTER: MonsterBuilder()
         JsonBuildTypes.MONSTERS: MonstersBuilder()
         JsonBuildTypes.SETTINGS: SettingsBuilder()
         JsonBuildTypes.SIDEQUEST: SideQuestBuilder()
         JsonBuildTypes.SIDEQUESTS: SideQuestsBuilder()
         JsonBuildTypes.STORIES: StoriesBuilder()
         JsonBuildTypes.STORY: StoryBuilder()
      }         
      
      # in each condition, create
      # a builder of the appropriate type
      # and call Build with that type