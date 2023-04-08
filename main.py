"""
This project is a machine learning based analysis tool for the online video game League of Legends.

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""
from dataprocessing.map_server import map_server_region
from development.development_functions import read_config, configure_custom_logger, get_player_data
from database.database import Database
from riotapi.api_controller import ApiController
from database import etl_pipeline as etl

# Main function
if __name__ == '__main__':
    # Instantiate api controller and database tunnel, confire logger.
    controller = ApiController(read_config('apikey'))
    database = Database('admin', read_config('dbAdmin'))
    logger = configure_custom_logger(module_name=__name__,
                                     console_level=int(read_config('loggingLevel')),
                                     logging_directory=read_config('loggingDirectory'))

    # Load data processing keys
    puuid, servers = get_player_data(['puuids', 'servers'])

    for i in range(len(puuid)):
        etl.load_player_matches(
            controller=controller, database=database, puuid=puuid[i], server=map_server_region(servers[i]))
        logger.info(f"Player {i} has been completed")
        print('\n\n')
