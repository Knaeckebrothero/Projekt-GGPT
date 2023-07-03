"""
This module holds scripts that load player data from the riot api into the database.

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""

from development.development_functions import read_config, configure_custom_logger
from database.database import Database
from riotapi.api_controller import ApiController


# Load matches into db
def load_player_data(controller: ApiController, database: Database, collection_name: str):
    """
    This function gathers additional information about plays from the database.

    Args:
        controller (ApiController): Instance of ApiController on which to execute script.
        database (Database): Instance of Database on which to execute script.
        collection_name (str): Name of the collection to load the players from.
    """

    # Declare variables
    logger = configure_custom_logger(module_name=__name__,
                                     console_level=int(read_config('loggingLevel')),
                                     logging_directory=read_config('loggingDirectory'))

    # Info log
    logger.info(f"Running etl for players from {collection_name}")

    # Get all new players from the database.
    players = database.retrieve_data(collection_name)

    # Loop through all players.
    for player in players:

        # Get puuid from player.
        puuid = controller.get_puuid(player['Player_Name'], player['Server'])

        # Check if getting the puuid worked
        if puuid is not None:

            # Get player data from the api.
            player_data = controller.get_player_data(puuid, player['Server'])

            # Check if the player data is not empty.
            if player_data is not None:

                # Add player data to player.
                player.update(player_data)

                # Update player in database.
                database.update_data(collection_name, player)

                # Info log
                logger.info(f"Updated player {player['Player_Name']}")

            else:

                # Info log
                logger.info(f"Could not get player data for {player['Player_Name']}")
