"""
This project is a machine learning based analysis tool for the online video game League of Legends.

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""
from development.development_functions import read_config, configure_custom_logger
from database.database import Database
from riotdata.api_controller import ApiController
from database import etl_pipeline as etl

# Main function
if __name__ == '__main__':
    # Instantiate api controller and database tunnel
    controller = ApiController(read_config('apikey'))
    database = Database('admin', read_config('dbAdmin'))
    logger = configure_custom_logger(__name__)

    players = ['TTV King Fidd', 'ShadowaIk', '9년의 공백', 'Kouwae']
    servers = ['na1', 'na1', 'kr', 'br1']

    for i in range(4):
        etl.load_matches(
            controller=controller, database=database, summoner_name=players[i], server=servers[i])
        logger.info(f"Player {i} has been completed!")
