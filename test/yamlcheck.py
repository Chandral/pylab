import yaml

dict_file = {"apples": 22220}
with open(r'config.yaml', 'a') as file:
    documents = yaml.dump(dict_file, file)