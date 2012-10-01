from Player import Player
import json
from StringIO import StringIO

class MainStory:
   @classmethod
   def LoadAllStories(cls):
      json_data=open("./Stories/Berserker.json").read()
      self.all_stories = json.loads(json_data)
      print(self.all_stories)  
         
   def __init__(self,the_player):
      self.loadStory("Berserker")
   
   def loadStory(self,story_name):
      print("loading...")