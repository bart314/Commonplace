import yaml

with open('website.yaml', 'r') as file:
    loaded_data = yaml.safe_load(file)