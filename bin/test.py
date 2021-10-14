import yaml
import os

with open(r'./conf.yaml') as file:
    conf_yaml = yaml.safe_load(file)

    conf_dir_name        = conf_yaml['dir_name']

os.mkdir(f'./{conf_dir_name}')