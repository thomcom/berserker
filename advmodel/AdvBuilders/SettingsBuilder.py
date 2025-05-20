from advmodel.AdvBuilders import AbstractBuilder
from .AdvEventsBuilder import *
from advmodel.Settings import Settings

class SettingsBuilder(AbstractBuilder):
   def Build(self):
      result = Settings()
      result.gamename = self.jsonData["game-name"]
      result.anykey = self.jsonData["any-key"]
      result.none = self.jsonData["none"]
      result.basics = self.jsonData["basics"]
      result.globalmenu = self.jsonData["global-menu"]
      
      builder = WelcomeEvBuilder()
      builder.SetJson(self.jsonData["WelcomeEv"])
      result.WelcomeEv = builder.Build()
     
      builder = StandingsEvBuilder()
      builder.SetJson(self.jsonData["StandingsEv"])
      result.StandingsEv = builder.Build()

      builder = ShopEvBuilder()
      builder.SetJson(self.jsonData["ShopEv"])
      result.ShopEv = builder.Build()

      builder = SellItemEvBuilder()
      builder.SetJson(self.jsonData["SellItemEv"])
      result.SellItemEv = builder.Build()

      builder = RewardEvBuilder()
      builder.SetJson(self.jsonData["RewardEv"])
      result.RewardEv = builder.Build()

      builder = QuitEvBuilder()
      builder.SetJson(self.jsonData["QuitEv"])
      result.QuitEv = builder.Build()

      builder = PlayerMakeEvBuilder()
      builder.SetJson(self.jsonData["PlayerMakeEv"])
      result.PlayerMakeEv = builder.Build()

      builder = PlayerInfoEvBuilder()
      builder.SetJson(self.jsonData["PlayerInfoEv"])
      result.PlayerInfoEv = builder.Build()

      builder = DecideEvBuilder()
      builder.SetJson(self.jsonData["DecideEv"])
      result.DecideEv = builder.Build()

      builder = BuyItemEvBuilder()
      builder.SetJson(self.jsonData["BuyItemEv"])
      result.BuyItemEv = builder.Build()

      builder = AchievementsEvBuilder()
      builder.SetJson(self.jsonData["AchievementsEv"])
      result.AchievementsEv = builder.Build()

      return result;
