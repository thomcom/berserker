# Build objects of type Armor
from advmodel.AdvBuilders import ItemBuilder
from advmodel.AdvDataObjects import Armor
from advmodel.AdvDataObjects import DieRoll
from advview.Log import Log

class ArmorBuilder(ItemBuilder):
   def Build(self):
      builder = ItemBuilder()
      builder.SetJson(self.jsonData)
      result = builder.Build()
      
      try:
         result.__class__ = Armor
         result.armor = DieRoll(self.jsonData["armor"])
      except Exception:
         return None

      return result