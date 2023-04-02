"""
This module contains the db class which handles the communication with the application database.

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""
import logging
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
        self._logger = configure_custom_logger(__name__)
        self._client = pymongo.MongoClient(
            read_config('dbConnectionString').format(role, password, server_api=ServerApi('1')))
        self._database = self._client[read_config('database')]

    # Insert dataclasses
    def insert_data(self, data_objects: list[object], collection: str) -> bool:
        """
        This function inserts a list of dataclasses into the database.

        Args:
            data_objects (list[object]): A list containing dataclass objects to be inserted.
            collection (str): Name of the database collection in which to insert the data objects.

        Returns:
            successful (bool): Returns True if the operation was successful and False if not.
        """
        # Check if database collection exists
        if collection not in self._database.list_collection_names():
            self._logger.log(30, f'Collection {collection} does not exist on selected database')
            return False

        # Variables
        col = self._database[collection]
        dataclass_type = type(data_objects[0])
        list_dicts = []

        # Converts the dataclasses to dictionaries before inserting them into the database.
        self._logger.log(10, 'Converting objects into dictionarys...')
        for data_object in data_objects:
            # Checks if all objects are of the same type
            if not type(data_object) == dataclass_type:
                self._logger.log(30, 'List contains objects of different types')
                return False
            # Convert and append object
            list_dicts.append(asdict(data_object))

        # Checks if list needs to be chunked
        if len(list_dicts) > 25:
            for chunk in divide_chunks(list_dicts, 25):
                self._logger.log(10, 'Inserting 25 objects...')
                col.insert_many(chunk)
        else:
            self._logger.log(10, 'Inserting objects...')
            col.insert_many(list_dicts)
        return True

    # Retrieve dataclasses
    def retrieve_data(self, collection: str, number_samples: int) -> list[object]:
        pass

    # Retrieve match ids
    def retrieve_match_ids(self, collection: str) -> list[str]:
        pass
