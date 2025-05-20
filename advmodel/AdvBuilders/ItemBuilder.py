# Build objects of type Item
from advmodel.AdvBuilders import AbstractBuilder
from advmodel.AdvDataObjects import Item
from advview.Log import Log

class ItemBuilder(AbstractBuilder):
   def Build(self):
      result = Item()

      # Item must have name, text, and value
      # Other attributes are optional
      try:
         result.name = self.jsonData["name"]
      except Exception as err:
         Log(Log.BUILDERROR," Item name" + str(self.jsonData))
         return None

      try:
         result.text = self.jsonData["text"]
      except Exception as err:
         Log(Log.BUILDERROR," Item text" + str(self.jsonData))
         return None

      try:
         result.value = self.jsonData["value"]
      except Exception as err:
         Log(Log.BUILDERROR," Item value" + str(self.jsonData))
         return None

      try:
         result.usability = self.jsonData["usability"]
      except Exception as err:
         Log(Log.BUILDERROR," Item usability" + str(self.jsonData))

      try:
         result.salable = self.jsonData["salable"]
      except Exception as err:
         # default is salable, if no entry then the object should be salable
         pass

      return result;
