# Instance of abstract class that reads and writes games to a local file in plain text

class SaveGameProvider:
   def __init__(self):
      self.saveCount = 0
   def getSaveCount(self):\
      return self.saveCount

