import yaml

dict_file = {"apples": 22220}

with open("config.yaml") as file:
    list_doc = yaml.load(file, Loader=yaml.FullLoader)

for i in list_doc:
    if i == "mangoes":
        list_doc[i] = 1111222
    print(i, "~", list_doc[i], '~', type(list_doc[i]))

with open("config.yaml", "w") as f:
    yaml.dump(list_doc, f)
