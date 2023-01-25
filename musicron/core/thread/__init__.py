import threading

class PluginThread(threading.Thread):

    def __init__(self,plugins,provider,URL):
        super().__init__()
        self.provider = provider
        self.URL = URL
        self.plugins = plugins

    def run(self):
        self.active_plugin = self.plugins._registry.get(self.provider)
        self.active_plugin.Play(self.URL)
    
    def stop(self):
        self.active_plugin.Stop()