import yaml

class Settings:
    loaded_data = {}

    def get_settings(cls):
        if len(Settings.loaded_data)==0:
            with open('website.yaml', 'r') as file:
                Settings.loaded_data = yaml.safe_load(file)
        
        return Settings.loaded_data

