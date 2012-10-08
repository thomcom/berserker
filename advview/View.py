# curses based view for python gameplay
from advview import Log
from advmodel import Types

class View:
   def __init__(self):
      Log(Log.STATUS,"Initialize View")
   def initialize(self,platform_type):
      Log(Log.STATUS,"View.initialize(" + platform_type + ")")

