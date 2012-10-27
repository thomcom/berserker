# Build objects of type Item
from advmodel.AdvBuilders import AbstractBuilder
from advmodel.AdvDataObjects import Item
from advview.Log import Log

class ItemBuilder(AbstractBuilder):
   def Build(self):
      result = Item()
      try:
         result.name = self.jsonData["name"]
      except Exception, err:
         Log(Log.BUILDERROR," Item name\n" + str(result))
         
      try:
         result.text = self.jsonData["text"]
      except Exception, err:
         Log(Log.BUILDERROR," Item text\n" + str(result))
      
      try:
         result.value = self.jsonData["value"]
      except Exception, err:
         Log(Log.BUILDERROR," Item value\n" + str(result))

      try:
         result.usability = self.jsonData["usability"]
      except Exception, err:
         Log(Log.BUILDERROR," Item usability\n" + str(result))

      try:
         result.salable = self.jsonData["salable"]
      except Exception, err:
         # default is salable, if no entry then the object should be salable
         pass

      return result;