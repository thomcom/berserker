# AbstractBuilder defines the interface for all builder classes

class AbstractBuilder:
   def SetJson(self,jsonData):
      self.jsonData = jsonData
   def Build(self):
      pass
