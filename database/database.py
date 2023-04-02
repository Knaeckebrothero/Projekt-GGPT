"""
This module contains the db class which handles the communication with the application database.

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""

import pymongo
from pymongo.server_api import ServerApi
from dataclasses import asdict
from development.development_functions import read_config, configure_custom_logger


# Splits a list into smaller lists.
def divide_chunks(mylist: list, chunk_size: int):
    for i in range(0, len(mylist), chunk_size):
        yield mylist[i:i + chunk_size]


# Primary database class
class Database:
    """
    Class containing all the attributes and methods used to communicate with the database.
    """

    def __init__(self, role: str, password: str):
        """
        Args:
            role (str): Login credentials, Admin for example
            password (str): Login credentials
        """
        self._logger = configure_custom_logger(module_name=__name__,
                                               console_level=int(read_config('loggingLevel')),
                                               logging_directory=read_config('loggingDirectory'))
        self._client = pymongo.MongoClient(
            read_config('dbConnectionString').format(role, password, server_api=ServerApi('1')))
        self._database = self._client[read_config('database')]
        self._logger.debug("Class initialized")

    # Insert dictionary
    def insert_data(self, data_dicts: list[dict], collection: str) -> bool:
        """
        This function inserts a list of dataclasses into the database.

        Args:
            data_dicts (list[object]): A list containing dataclass objects to be inserted.
            collection (str): Name of the database collection in which to insert the dataprocessing objects.

        Returns:
            successful (bool): Returns True if the operation was successful and False if not.
        """
        # Info log
        self._logger.info(f"Received {len(data_dicts)} objects to be inserted into {collection}")

        # Check if database collection exists
        if collection not in self._database.list_collection_names():
            self._logger.error(f'Collection {collection} does not exist on selected database')
            return False
        else:
            col = self._database[collection]

        # Checks if list needs to be chunked and inserts dataprocessing.
        if len(data_dicts) > 25:
            for chunk in divide_chunks(data_dicts, 25):
                self._logger.debug('Inserting 25 objects...')
                try:
                    col.insert_many(chunk)
                except BaseException as e:
                    self._logger.error(f'Error inserting dataprocessing into db, exception{e}')
                    return False
        else:
            self._logger.debug('Inserting objects...')
            try:
                col.insert_many(data_dicts)
            except BaseException as e:
                self._logger.error(f'Error inserting dataprocessing into db, exception{e}')
                return False

        # If no errors occurred function returns true.
        self._logger.info("All dataprocessing objects inserted successfully")
        return True

    # Retrieve dataclasses
    def retrieve_data(self, collection: str, number_samples: int) -> list[object]:
        pass

    # Retrieve match ids
    def retrieve_match_ids(self, collection: str) -> list[str]:
        pass
