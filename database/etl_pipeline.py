"""
This module holds a script that loads matchmaking data from the riot api into the database.

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""

import logging
import traceback
from development.development_functions import read_config, configure_custom_logger
from database.database import Database
from riotdata.api_controller import ApiController
from riotdata.apis import match_v5 as api


# Load matches into db
def load_matches(controller: ApiController, database: Database, summoner_name: str, server: str,
                 champion: str = None, start_time: float = 1672444800):
    """
        This function gets MatchDtos from the riot games api and saves them in the database.

        Args:
            controller (ApiController): Instance of ApiController on which to execute script.
            database (Database): Instance of Database on which to execute script.
            summoner_name (str): Summoner name of the player whose matches should be gathered.
            server (str): Server which the summoner is registered on.
            champion (str): Optional filter for champion played.
            start_time (float): Optional epoch timestamp used for filtering.
    """
    # Declare variables
    logger = configure_custom_logger(__name__)
    puuid = controller.get_puuid(summoner_name, server)
    start = 0
    done = False
    matches = []
    match_count = 0

    # Haven't fully tested the mapping yet xD
    match server:
        case 'br1':
            server = 'americas'
        case 'eun1':
            server = 'europe'
        case 'euw1':
            server = 'europe'
        case 'jp1':
            server = 'asia'
        case 'la1':
            server = 'americas'
        case 'la2':
            server = 'americas'
        case 'na1':
            server = 'americas'
        case 'oc1':
            server = 'sea'
        case 'ph2':
            server = 'asia'
        case 'ru':
            server = 'europe'
        case 'sg2':
            server = 'asia'
        case 'th2':
            server = 'asia'
        case 'tr1':
            server = 'asia'
        case 'tw2':
            server = 'asia'
        case 'vn2':
            server = 'asia'

    # Check if getting the puuid worked.
    if puuid[0] == 200:

        # Loop until the api returns an empty list.
        while not done:

            # Get match ids from the api.
            match_ids = controller.get_match_ids(
                puuid=puuid[1], start=start, server=server, start_time=start_time)

            if match_ids[0] == 200:

                # Check if the server returned any matches.
                if len(match_ids[1]) > 0:

                    # Iterate and cache existing matches.
                    for match_id in match_ids:
                        request = controller.get_match(match_id, server)
                        if request[0] == 200:
                            matches.append(request[1])
                            match_count = match_count + 1

                    # Insert matches into database.
                    database.insert_data(matches, 'matchDto')

                    # Up the count match count.
                    start = start + 100
                else:
                    logger.info(f'No more matches to load, {match_count} matches retrived')
                    done = True
            else:
                logger.error(f'Something went wrong while getting the match ids')
                done = True
    else:
        logger.error('Something went wrong while getting the puuid')
    return