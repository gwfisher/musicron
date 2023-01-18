from main import PluginRegistry

class Plugin:
    name = "general"

    def __init__(self):
        pass

    def setup(self):
        print("You found me!")
