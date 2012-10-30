# Logging

import datetime

class Log:
   STATUS = "Log.STATUS"
   DATAERROR = "Log.DATAERROR"
   FILERROR = "Log.FILEERROR"
   BUILDERROR = "Log.BUILDERROR"
   
   status_filename = "advstatus.log"
   def __init__(self,log_type,string):
      #if log_type == Log.STATUS:
         # TODO: append to file with time etc
      time = datetime.datetime.now()
      tstamp = "%s%s%s-%s:%s:%s" % tuple(time.timetuple())[0:6]
      print(tstamp + " " + log_type + " " + string)