# The Settings class contains all of the defaults required
# for prompting the user.

from AdvEvents import *

class Settings:
   def __init__(self):
      self.gamename = "default"
      self.anykey = "anykey"
      self.none = "none"
      self.basics = None
      self.globalmenu = None
      self.WelcomeEv = WelcomeEv()
      self.StandingsEv = StandingsEv()
      self.ShopEv = ShopEv()
      self.SellItemEv = SellItemEv()
      self.RewardEv = RewardEv()
      self.QuitEv = QuitEv()
      self.PlayerMakeEv = PlayerMakeEv()
      self.PlayerInfoEv = PlayerInfoEv()
      self.DecideEv = DecideEv()
      self.BuyItemEv = BuyItemEv()
      self.AchievementsEv = AchievementsEv()
   def __str__(self):
      return """
   Adv Localized Settings Loaded:
      Game-Name: %s
      AnyKey Prompt: %s
      None: %s
      Basics Menu: %s
      Global Menu: %s
      
      WelcomeEv: %s
      StandingsEv: %s 
      ShopEv: %s
      SellItemEv: %s
      RewardEv: %s
      QuitEv: %s
      PlayerMakeEv: %s
      PlayerInfoEv: %s
      DecideEv: %s
      BuyItemEv: %s
      AchievementsEv: %s""" % (self.gamename,self.anykey,self.none,self.basics,self.globalmenu, \
                        self.WelcomeEv,self.StandingsEv,self.ShopEv,self.SellItemEv, \
                        self.RewardEv,self.QuitEv,self.PlayerMakeEv,self.PlayerInfoEv, \
                        self.DecideEv,self.BuyItemEv,self.AchievementsEv)
   def __repr__(self):
      return self.__str__()