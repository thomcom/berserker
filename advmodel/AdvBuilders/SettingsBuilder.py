from advmodel.AdvBuilders import AbstractBuilder
from advmodel.Settings import Settings
class SettingsBuilder(AbstractBuilder):
   def Build(self):
      result = Settings()
      result.gamename = self.jsonData["game-name"]
      result.anykey = self.jsonData["any-key"]
      result.none = self.jsonData["none"]
      result.basics = self.jsonData["basics"]
      result.globalmenu = self.jsonData["global-menu"]
      result.WelcomeEv = self.jsonData["WelcomeEv"]
      result.StandingsEv = self.jsonData["StandingsEv"]
      result.ShopEv = self.jsonData["ShopEv"]
      result.SellItemEv = self.jsonData["SellItemEv"]
      result.RewardEv = self.jsonData["RewardEv"]
      result.QuitEv = self.jsonData["QuitEv"]
      result.PlayerMakeEv = self.jsonData["PlayerMakeEv"]
      result.PlayerInfoEv = self.jsonData["PlayerInfoEv"]
      result.DecideEv = self.jsonData["DecideEv"]
      result.BuyItemEv = self.jsonData["BuyItemEv"]
      result.AchievementsEv = self.jsonData["AchievementsEv"]
      return result;