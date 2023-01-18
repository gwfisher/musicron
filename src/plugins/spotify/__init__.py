import dbus
from main import PluginRegistry

class Plugin:
     name = "Spotify"

     def __init__(self):
        pass

     def setup(self):
          bus = dbus.SessionBus()
          proxy = bus.get_object('org.mpris.MediaPlayer2.spotify','/org/mpris/MediaPlayer2')
          self.spotify = dbus.Interface(proxy, dbus_interface='org.mpris.MediaPlayer2.Player')
        
          print("Loaded Spotify")

          return self
     

     def Play(self,uri):
          self.spotify.OpenUri(uri)
          self.spotify.Play()
     
     def Stop(self):
          self.spotify.Stop()





      

   

      


