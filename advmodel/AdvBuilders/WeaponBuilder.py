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
      result.__class__ = Weapon
      
      try:
         result.damage = DieRoll(self.jsonData["damage"])
      except Exception, err:
         # TODO: Handle various DieRollInitExceptions
         Log(Log.BUILDERROR,"DieRoll throws an exception!!!")
         result.damage = DieRoll("1d2")

      return result