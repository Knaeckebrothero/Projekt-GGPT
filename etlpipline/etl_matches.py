"""
This module holds scripts that load matchmaking data from the riot api into the database.

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""

from development.development_functions import read_config, configure_custom_logger
from database.database import Database
from riotapi.api_controller import ApiController


# Load matches into db
def load_player_matches(
        controller: ApiController,
        database: Database,
        puuid: str,
        server: str,
        champion: str = None,
        start_time: float = 1672444800):
    """
    This function gets MatchDtos from the riot games api and saves them in the database.

    Args:
        controller (ApiController): Instance of ApiController on which to execute script.
        database (Database): Instance of Database on which to execute script.
        puuid (str): Of the player whose matches should be loaded.
        server (str): Server which the summoner is registered on.
        champion (str): Optional filter for champion played.
        start_time (float): Optional epoch timestamp used for filtering.
    """
    # Declare variables
    logger = configure_custom_logger(module_name=__name__,
                                     console_level=int(read_config('loggingLevel')),
                                     logging_directory=read_config('loggingDirectory'))
    start = 0
    done = False
    matches = []
    match_count = 0

    # Info log
    if champion:
        logger.info(f"Running etl for {puuid}, {server}, {champion}")
    else:
        logger.info(f"Running etl for {puuid}, {server}")

    # Check if getting the puuid worked.
    if puuid is not None:
        logger.debug('Got puuid, looking for match ids...')

        # Loop until the api returns an empty list.
        while not done:

            # Get match ids from the api.
            match_ids = controller.get_match_ids(
                puuid=puuid, start=start, server=server, start_time=start_time)

            if match_ids is not None:
                # Check if the server returned any matches.
                if len(match_ids) > 0:
                    logger.debug('Got match ids, loading matches...')

                    # Iterate and cache existing matches.
                    for match_id in match_ids:
                        request = controller.get_match(match_id, server)
                        if request is not None:
                            logger.debug('Caching match...')
                            matches.append(request)
                            match_count = match_count + 1

                    # Insert matches into database.
                    logger.debug('Inserting matches into db...')
                    if database.insert_data(matches, 'matchDto'):
                        logger.debug("Matches have been inserted")
                        # Up the count match count and reset matches
                        start = start + 100
                        matches = []
                    else:
                        logger.error("Something went wrong while inserting the matches into the db")
                        return
                else:
                    logger.info(f'No more matches to load, {match_count} matches loaded')
                    done = True
            else:
                logger.error(f'Something went wrong while getting the match ids')
                done = True
    else:
        logger.error(f'Something went wrong while getting puuid')
