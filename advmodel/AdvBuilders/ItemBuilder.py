# Build objects of type Item

from AdvDataObjects import Item

class ItemBuilder:
   def Build(self):
      result = Item()
      try:
         result.name = self.jsonData["name"]
      except Exception, err:
         Log(Log.BUILDERROR," Item name\n" + self)
         
      try:
         result.text = self.jsonData["text"]
      except Exception, err:
         Log(Log.BUILDERROR," Item text\n" + self)
      
      try:
         result.value = self.jsonData["value"]
      except Exception, err:
         Log(Log.BUILDERROR," Item value\n" + self)

      try:
         result.usability = self.jsonData["usability"]
      except Exception, err:
         Log(Log.BUILDERROR," Item usability\n" + self)

      try:
         result.salable = self.jsonData["salable"]
      except Exception, err:
         Log(Log.BUILDERROR," Item salable\n" + self)

      return result;