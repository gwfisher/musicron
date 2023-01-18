import yaml

class LoadYaml:
    def __init__(self,confFile):

        self.confFile = confFile

        with open(confFile,'r') as file:
            self.loadedConf = yaml.safe_load(file)

class Config:
    def __init__(self, name: str, time: str, service: dict):
        self.name = name
        self.time = time
        self.service = service

class Service:
    def __init__(self, provider: str, url: str, plugin: str):
        self.provider = provider
        self.url = url
        self.plugin = plugin

class ConfigFile:
    def __init__(self, configFile):
        self.configs = []
        with open (configFile,"r") as file:
            data = yaml.safe_load(file)
            for item in data:
                if 'name' in item and 'time' in item and 'service' in item:
                    service_data = item['service']
                    service = Service(provider=service_data['provider'],url=service_data['url'],plugin=service_data['plugin'])
                    config = Config(name=item['name'], time=item['time'], service=service)
                    self.configs.append(config)
                    
    def get_configs(self):
        return self.configs
