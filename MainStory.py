import json
import io
from StringIO import StringIO

from Event import Event
from Player import Player
from Monster import Monster
from Monster import MonsterBuilder
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
      cls.all_stories = [parsedJson]
         
   def __init__(self,the_player):
      # Use players class to weight story loading decision
      my_story = MainStory.all_stories[0]['mainstory']
      self.name = my_story['name']
      self.end = End(my_story['End']['message'],my_story['End']['reward'])
      self.menu = Menu(my_story['Menu']['choices'],my_story['Menu']['text'])
      self.events = Event.EventArray(my_story['Events'])
      if 'Monsters' in my_story:
         self.monsters = []
         for monsterJson in my_story['Monsters']:
            monsterBuilder = MonsterBuilder()
            monsterBuilder.setJson(monsterJson)
            self.monsters.append(monsterBuilder.build())
   
   def loadStory(self,story_name):
      Output.Main(story_name)
      Output.Main(MainStory.all_stories.viewvalues())
      Output.Main(MainStory.all_stories['mainstory']['name'])