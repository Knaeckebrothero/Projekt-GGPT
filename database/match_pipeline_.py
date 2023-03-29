"""
This is a script to loads match data from the riot api into the database.

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""

import logging
import traceback
from development.get_credentials import read_config
from database.database import Database
from loldata.api import match_v5 as api

# Basic configuration for logging.
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# Get the necessary information from the config file and declare variables.
key = read_config('apikey')
puuid = read_config('puuid')
start = 0
done = False
list_match_ids = []
matches = []
match_count = 0
db = Database('admin', read_config('dbAdmin'))

# Gets the matches from the riot api and saves them in the database.
while not done:
    # Chunk-wise retrieves match ids from the riot api.
    try:
        for match_id in api.get_match_ids(puuid=puuid, start=start, count=100, api_key=key):
            response = api.get_match(match_id, key)
            #response = MatchDto(json.load(api.get_match(match_id, key)))
            matches.append(response)
            match_count = match_count + 1
        start = start + 100
    # Breaks the loop on api error
    except BaseException as e:
        done = True
        logging.log(20, 'Done inserting! (1/2) Last API response = ' + response)
        logging.log(20, 'Done inserting! (2/2) Exception = ' + traceback.format_exc())
    # Insert the dictionary into the MongoDB collection.
    finally:
        db.insert_loldata(matches, 'matchDto')

# Close db connection and print results
db.__del__()
print("Retrieved", match_count, "matches.")
