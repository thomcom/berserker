from Event import Event
from Player import Player
import json
from StringIO import StringIO
import io
from ETio import Output

class Menu:
   def __init__(self,choices,text):
      self.choices = choices;
      self.text = text;
      
class End:
   def __init__(self,message,reward):
      self.message = message;
      self.reward = reward;

class MainStory:
   all_stories = []
   
   @classmethod
   def LoadAllStories(cls):
      berserker_file = io.open("./Stories/Berserker.json")
      parsedJson = json.loads(berserker_file.read())
      cls.all_stories = parsedJson
         
   def __init__(self,the_player):
      # Use players class to weight story loading decision
      my_story = MainStory.all_stories['mainstory']
      self.name = my_story['name']
      self.end = End(my_story['end']['message'],my_story['end']['reward'])
      self.menu = Menu(my_story['menu']['choices'],my_story['menu']['text'])
      self.events = Event.EventArray(my_story['events'])
      
   
   def loadStory(self,story_name):
      Output.Main(story_name)
      Output.Main(MainStory.all_stories.viewvalues())
      Output.Main(MainStory.all_stories['mainstory']['name'])