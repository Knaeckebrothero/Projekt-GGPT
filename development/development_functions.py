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


# Retrieve a list from a yaml file.
def get_player_data(keys: list[str]) -> tuple:
    with open('./development/data.yaml', 'r') as file:
        yaml_data = yaml.safe_load(file)
        result = tuple()
        for k in keys:
            result = result + (yaml_data[k], )
    return result


# Custom logger
def configure_custom_logger(
        module_name: str = __name__,
        console_level: int = 20,
        file_level: int = 10,
        logging_format: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        logging_directory: str = './logs/') -> logging.Logger:
    """
    This function configures a custom logger for printing and saving logs in a logfile.
    https://docs.python.org/3/library/logging.html?highlight=logger#module-logging

    Args:
        module_name (str): Name for the logging module, could be __name__ or a custom name.
        console_level (int): The logging level for logging in the console.
        file_level (int): The logging level for logging in the logfile.
        logging_format (str): Format used for logging.
        logging_directory (str): Path for the directory where the log files should be saved to.

    Returns:
        Logger: The configured Logger instance.
    """
    logger = logging.getLogger(logging.getLoggerClass().root.name + "." + module_name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(logging_format)

    # File handler for writing logs to a file
    file_handler = logging.FileHandler(logging_directory + module_name + '.log')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(file_level)
    logger.addHandler(file_handler)

    # Console (stream) handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(console_level)
    logger.addHandler(console_handler)

    return logger
