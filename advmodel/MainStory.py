import json
import io
from StringIO import StringIO

from Event import Event
from Player import Player
from Monster import Monster
from Monster import MonsterBuilder
from advview import ETio

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
      # TODO: Use AdvDataRetrieve
      berserker_file = io.open("./json/StoryDefault.json")
      parsedJson = json.loads(berserker_file.read())
      print(parsedJson)
      cls.all_stories = [parsedJson]

   def __init__(self,the_player):
      # Use players class to weight story loading decision
      self.story = MainStory.all_stories[0]['storyline']
      self.monsters = MainStory.all_stories[0]['monsters']
      self.items = MainStory.all_stories[0]['items']
      self.name = self.story['name']
      self.end = End(self.story['End']['message'],self.story['End']['reward'])
      self.menu = Menu(self.story['Menu']['choices'],self.story['Menu']['text'])
      self.events = Event.EventArray(self.story['Events'])

   def loadStory(self,story_name):
      Output.Main(story_name)
      Output.Main(MainStory.all_stories.viewvalues())
      Output.Main(MainStory.all_stories['mainstory']['name'])

   def shopping(self):
      Output.Main(self.story)
