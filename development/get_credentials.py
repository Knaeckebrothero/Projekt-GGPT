"""
This is a function to load your credentials from the config file.
"""
import yaml


# Retrieve credentials from a yaml file
def read_config(key: str):
    with open('../development/config.yaml', 'r') as cfg:
        return yaml.safe_load(cfg)[key]
        cfg_file.close()
