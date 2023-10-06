# python script showing battery details
import psutil
import os
import threading
import datetime

#Save datas in that txt file that is in that path
FILE_PATH =r""

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

def printit():
  e = datetime.datetime.now()
  battery = psutil.sensors_battery()
  threading.Timer(60.0, printit).start()
  with open(FILE_PATH,"a") as f:
    f.write(f"battery--> {battery.percent} // powerPlugged--> {battery.power_plugged} // date--> {e.day, e.month, e.year} // time--> {e.hour}:{e.minute}:{e.second}\n")
  print("Worked")
  
printit()


# os.system("shutdown /s /t 1")     shut down computer

