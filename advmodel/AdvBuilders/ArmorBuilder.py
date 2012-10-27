# Build objects of type Armor
from advmodel.AdvBuilders import ItemBuilder
from advmodel.AdvDataObjects import Armor
from advview.Log import Log

class ArmorBuilder(ItemBuilder):
   def Build(self):
      result = ItemBuilder.Build(self)
      result.__class__ = Armor
      
      armorVal = self.jsonData["armor"]
      
      try:
         armorSplit = armorVal.split("d")
         if len(armorSplit) < 2 : raise Exception
      except Exception, err:
         Log(Log.BUILDERROR," Armor value ("+armorVal+") invalid\n" + str(result))
         return None
         
      try:
         result.armorDice = int(armorSplit[0])
      except Exception, err:
         Log(Log.BUILDERROR," Armor dice ("+armorVal+") invalid\n" + str(result))
         return None
      
      try:
         armorDieMod = armorSplit[1].split("-")
         result.armorDie = int(armorDieMod[0])
         result.armorMod = -int(armorDieMod[1])
      except ValueError, err:
         pass
      except IndexError, err:
         pass
      except Exception, err:
         Log(Log.BUILDERROR," Armor modifier ("+str(armorVal)+") invalid\n" + str(result))
         return None
                  
      try:
         armorDieMod = armorSplit[1].split("+")
         result.armorDie = int(armorDieMod[0])
         result.armorMod = int(armorDieMod[1])
      except ValueError, err:
         pass
      except IndexError, err:
         pass
      except Exception, err:
         Log(Log.BUILDERROR," Armor modifier ("+str(armorVal)+") invalid\n" + str(result))
         return None
         
      return result