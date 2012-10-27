# Logging

class Log:
   STATUS = "Log.STATUS"
   DATAERROR = "Log.DATAERROR"
   FILERROR = "Log.FILEERROR"
   BUILDERROR = "Log.BUILDERROR"
   
   status_filename = "advstatus.log"
   def __init__(self,log_type,string):
      #if log_type == Log.STATUS:
         # TODO: append to file with time etc
      #   print(string)
      print(log_type,string)