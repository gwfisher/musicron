import dbus
import psutil
import os
import subprocess
import time
from musicron.core.plugin import PluginRegistry

class Plugin:
     name = "VLC"

     def __init__(self):
          pass

     def __getProcess(self):
          processName = "vlc"
          for proc in psutil.process_iter():
               if processName.lower() in proc.name().lower():
                    return True
          return False

     def setup(self):
          if not self.__getProcess():
               try:
                    subprocess.Popen(["vlc"])
                    time.sleep(5)
               except FileNotFoundError:
                    print("VLC Not installed")
               
          bus = dbus.SessionBus()
          proxy = bus.get_object('org.mpris.MediaPlayer2.vlc','/org/mpris/MediaPlayer2')
          self.vlc = dbus.Interface(proxy, dbus_interface='org.mpris.MediaPlayer2.Player')
          print("Loaded VLC")
          return self
     
     def Play(self,uri):
          print(uri)
          self.vlc.OpenUri(uri)
          self.vlc.Play()
     
     def Stop(self):
          self.vlc.Stop()


