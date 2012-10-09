
from advmodel import Model
from advmodel import Types
from advcontroller import Controller
from advview import View

class Game:
   def Launch(self):
      m = Model()
      m.preloadItems()
      m.preloadClasses()
      m.preloadMonsters()
      m.preloadSideQuests()
      m.preloadStories()

      v = View()
      v.initialize(Types.OSX)
      
      c = Controller()
      c.initialize(Types.OSX)
      c.setModel(m)
      c.setView(v)

      c.runGame()

