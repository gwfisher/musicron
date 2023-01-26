
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(script_dir, 'plugins'))

class PluginRegistry:
    def __init__(self):
        self._registry = {}
    
    def register(self,name):
        def decorator(func):
            self._registry[name] = func
            return func
        return decorator

    def setup_plugins(self):
        for name,func in self._registry.items():
            func()