# Build objects of type Armor

from AdvDataObjects import Armor

class ArmorBuilder:
   def Build(self):
      result = Armor()
      
      armorVal = self.jsonData["armor"]
      
      try:
         armorSplit = armorVal.split("d")
         if len(armorSplit) < 2 : raise Exception
      except Exception, err:
         Log(Log.BUILDERROR," Armor value ("+armorVal+") invalid\n" + self)
         return None
         
      try:
         result.armorDice = int(armorSplit[0])
      except Exception, err:
         Log(Log.BUILDERROR," Armor dice ("+armorVal+") invalid\n" + self)
         return None
      
      isNegative = False
      isPositive = False
      try:
         negative = armorSplit[1].index("-")
         isNegative = True
         armorDieMod = armorSplit[1].split("-")
         result.armorMod = -int(armorDieMod[1])
      except ValueError, err:
         pass
      except Exception, err:
         Log(Log.BUILDERROR," Armor modifier ("+armorSplit[1]+") invalid\n" + self)
         return None
                  
      try:
         positive = armorSplit[1].index("+")
         isPositive = True
         armorDieMod = armorSplit[1].split("+")
         result.armorMod = int(armorDieMod[1])
      except ValueError, err:
         pass
      except Exception, err:
         Log(Log.BUILDERROR," Armor modifier ("+armorSplit[1]+") invalid\n" + self)
         return None
                  
      try:
         result.armorDie = int(armorDieMod[0])
      except Exception, err:
         Log(Log.BUILDERROR," Armor die ("+armorDieMod+") invalid\n" + self)      
         return None
         
      return result