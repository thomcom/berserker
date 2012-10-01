
class Event:
   
   @classmethod
   def EventArray(cls,array):
      events = []
      for event in array:
         events.append(Event(event))
      return events
      
   def __init__(self,event):
      self.message = event['message']
      self.success = event['success']
      self.fail = event['fail']