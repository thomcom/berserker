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
      result.__class__ = Armor

      result.armor = DieRoll(self.jsonData["armor"])      
      # try:
      # 
      # except Exception, err:
      #    # TODO: Handle various DieRollInitExceptions
      #    Log(Log.BUILDERROR,"DieRoll throws an exception!!!")
      #    result.armor = DieRoll("1d2")

      return result