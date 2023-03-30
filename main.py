"""
This module contains the main function.
The project is a machine learning based analysis tool for the video game League of Legends.

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""
from database.database import Database
from development.get_credentials import read_config
from riotdata.api_controller import ApiController

# Main function
if __name__ == '__main__':
    # Instantiate api controller and database tunnel
    api = ApiController(read_config('apikey'))
    db = Database('admin', read_config('dbAdmin'))

    i = 0
    while i < 215:
        response_code, response = api.get_puuid(name="0x67686f7374")
        print(i, " - ", response_code)
        i = i +1
