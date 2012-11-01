
from advmodel import Model
from advmodel import Types
from advcontroller import Controller
from advview import View
from advview import Log

class Game:
   def Launch(self):
      Log.SetSessionTimestamp()
      m = Model()
      m.LoadSettings()
      m.PreloadItems()
      m.PreloadWeapons()
      m.PreloadArmor()
      m.PreloadClasses()
      m.PreloadMonsters()
      m.PreloadSideQuests()
      m.PreloadStories()

      v = View()
      v.initialize(Types.OSX)
      
      c = Controller()
      c.initialize(Types.OSX)
      c.setModel(m)
      c.setView(v)

      c.runGame()

