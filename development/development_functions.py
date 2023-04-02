"""
This is a function to load your credentials from the config file.

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""
import logging
import yaml


# Retrieve credentials from a yaml file.
def read_config(key: str) -> str:
    with open('./development/config.yaml', 'r') as cfg:
        return yaml.safe_load(cfg)[key]
        cfg_file.close()


# Defines a custom logger.
def configure_custom_logger(module_name: str) -> logging.Logger:
    logger = logging.getLogger(logging.getLoggerClass().root.name + "." + module_name)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler = logging.FileHandler(read_config('loggingDirectory') + module_name + '.log')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(read_config('loggingLevel'))
    return logger
