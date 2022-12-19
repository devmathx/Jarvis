import yaml

data = yaml.safe_load(open('nlu\\train.yaml', 'r', encoding='utf-8').read())

for command in data["commands"]:
    print(command)