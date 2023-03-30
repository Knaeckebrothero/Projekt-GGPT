"""
This is a function to load your credentials from the config file.

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""
import yaml


# Retrieve credentials from a yaml file
def read_config(key: str):
    with open('./development/config.yaml', 'r') as cfg:
        return yaml.safe_load(cfg)[key]
        cfg_file.close()
