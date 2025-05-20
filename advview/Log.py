# Logging

import datetime
from os import mkdir

class Log:
   STATUS = "Log.STATUS"
   DUMP = "Log.DUMP"
   DATAERROR = "Log.DATAERROR"
   FILEERROR = "Log.FILEERROR"
   BUILDERROR = "Log.BUILDERROR"
   
   @classmethod
   def GetTimestamp(cls):
      time = datetime.datetime.now()
      return "%s%s%s-%s:%s:%s" % tuple([str(x).zfill(2) for x in time.timetuple()[0:6]])
   
   prefix = ""
   @classmethod
   def SetSessionTimestamp(cls):
      Log.prefix = "logs/AdvLog" + Log.GetTimestamp()
      
   def __init__(self,log_type,string):
      try:
         mkdir('logs')
      except:
         pass

      outfile = {
         Log.DUMP : open(Log.prefix + "Adv_model.dump","a"),
         Log.STATUS : open(Log.prefix + "Adv_status_log.txt","a"),
         Log.DATAERROR : open(Log.prefix + "Adv_error_log.txt","a"),
         Log.FILEERROR : open(Log.prefix + "Adv_error_log.txt","a"),
         Log.BUILDERROR : open(Log.prefix + "Adv_error_log.txt","a")
      } [log_type]

      output = Log.GetTimestamp() + " " + log_type + " " + str(string) + "\n"
      
      debug = False
      if debug:
         print(output)
      else:
         outfile.write(output)
      
      outfile.close()
