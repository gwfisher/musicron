#!/usr/bin/env python

from datetime import datetime
from dateutil import tz
from pathlib import Path
from core.config import ConfigFile,LoadYaml
from core.timedate import TimeDate
from core.thread import PluginThread
from core.plugin import PluginRegistry

import importlib2
import sys
import functools
import os
import time

class MusiCron:
    def __init__(self, plugins:list=[]):

        self.player_thread = None

        self.plugins = PluginRegistry()
        for plugin in plugins:
            imported_module = importlib2.import_module('plugins.' + plugin)
            imported_instance = imported_module.Plugin()
            self.plugins.register(imported_module.Plugin.name)(imported_instance.setup())

    def play(self,provider,URL):
        self.player_thread = PluginThread(self.plugins,provider,URL)
        self.player_thread.start()

    def stop(self,provider,URL):
        self.player_thread.stop()
        
    def run(self):
        configPath = os.path.expanduser('~/.musicron.conf')  
        try:
            if os.path.isfile(configPath):
                configPath = os.path.expanduser('~/.musicron.conf')

                config_file = ConfigFile(configPath) #start reading the config YAML file
                configs = config_file.get_configs()
            else:
                configPath = 'musicron.conf.sample'
        except FileNotFoundError:
            print("Config File Not Found")

        while(True):
            timeDate = TimeDate()
            
            currentTime = timeDate.getTime("local")
            currentDay = timeDate.getDay("local")
            currentNow = currentTime + " " + currentDay
            
            currentTimeUTC = timeDate.getTime("UTC")
            currentDayUTC = timeDate.getDay("UTC")

            currentNowUTC = "U" + currentTimeUTC + " " + currentDayUTC

            for config in configs:
                name = config.name
                playTime = config.time
                provider = config.service.provider
                plugin = config.service.plugin
                URL = config.service.url

                if playTime.find("-") != -1:
                    runTime = playTime.split("-")
                    startTime = runTime[0]
                    endTime = runTime[1]
                    print(startTime)
                    print(endTime)
                else:
                    startTime = playTime

                if startTime == currentTime or startTime == currentNow or startTime == currentTimeUTC or startTime == currentNowUTC:
                    print("Playing " + name + "at" + startTime)
                    self.play(provider,URL)
                elif endTime == currentTime or endTime == currentNow or endTime == currentTimeUTC or endTime == currentNowUTC:
                    print("Playing " + name + "at" + startTime)
                    self.stop(provider,URL)
                else:
                    pass

            time.sleep(60)

if __name__ == "__main__":
    path = os.path.join(os.path.dirname(__file__), 'plugins')
    if os.path.isdir(path):
        dir_list = os.listdir(path)
        app = MusiCron(dir_list)
        app.run()
    else:
        print("Plugins directory not found.")
