#DieRoll stores three values in the format of a D&D die roll:
#Number of dice to be rolled,
#Number of faces on the rolled die,
#Modifier to add or subtract from die roll(s)
from random import randint

from advview.Log import Log

class DieRoll:
   def __init__(self):
      self.dice = 1
      self.die = 2
      self.modifier = 0
   def __init__(self,str):
      self.dice = 1
      self.die = 2
      self.modifier = 0
      self.SetArmorString(str)
   def __str__(self):
      returnString = "%dd%d" % (self.dice,self.die)
      if self.modifier > 0:
         returnString += "+%d" % self.modifier
      else:
         returnString += "%d" % self.modifier
      return returnString
   def __repr__(self):
      return self.__str__()
   def SetArmorString(self,armorString):
      val = armorString
      
      try:
         dieSplit = val.split("d")
         if len(dieSplit) < 2 : raise Exception
      except Exception, err:
         Log(Log.BUILDERROR," DieRoll value ("+armorString+") invalid\n" + str(self))
         return self
         
      try:
         self.dice = int(dieSplit[0])
      except Exception, err:
         Log(Log.BUILDERROR," DieRoll dice ("+armorString+") invalid\n" + str(self))
         return self
      
      if dieSplit[1].count("-"):
         dieMod = dieSplit[1].split("-")
         self.die = int(dieMod[0])
         if( len(dieMod) > 1):
            self.modifier = -int(dieMod[1])
                  
      if dieSplit[1].count("+"):
         dieMod = dieSplit[1].split("+")
         self.die = int(dieMod[0])
         if( len(dieMod) > 1):
            self.modifier = int(dieMod[1])

      return self
   def GetRoll(self):
      return sum(randint(1,self.die) for k in range(self.dice))+self.modifier