# Build objects of type Weapon
from advmodel.AdvBuilders import ItemBuilder
from advmodel.AdvDataObjects import Weapon
from advmodel.AdvDataObjects import DieRoll
from advview.Log import Log

class WeaponBuilder(ItemBuilder):
   def Build(self):
      builder = ItemBuilder()
      builder.SetJson(self.jsonData)
      result = builder.Build()
      
      try:
         result.__class__ = Weapon
         result.damage = DieRoll(self.jsonData["damage"])
      except Exception:
         return None

      return result