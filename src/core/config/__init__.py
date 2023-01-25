import yaml

class LoadYaml:
    def __init__(self,confFile):

        self.confFile = confFile

        with open(confFile,'r') as file:
            loadedConf = yaml.safe_load(file)
            self.validate(loadedConf)
    
    def validate(self,confFile):

        self.config = []

        for conf in confFile:
            configBuf = { }
            if not conf['name']:
                print("Item requires a name in configuration file")
            else:
                configBuf['name'] = conf['name']
            if not conf['time']:
                print("Item Requires a time")
            else:
                configBuf['time'] = conf['time']
            if not conf['service']:
                print("Item Requires Service")
            else:
                configBuf['service'] = conf['service']

            self.config.append(configBuf)

        return self.config
        
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

        try:
            loadedConfig = LoadYaml(configFile) # Load YAML and begin validation
        except FileNotFoundError:
            print("Configuration file not found")

        for item in loadedConfig.config:
            service_data = item['service']
            service = Service(provider=service_data['provider'],url=service_data['url'],plugin=service_data['plugin'])
            config = Config(name=item['name'], time=item['time'], service=service)
            self.configs.append(config)
                    
    def get_configs(self):
        return self.configs