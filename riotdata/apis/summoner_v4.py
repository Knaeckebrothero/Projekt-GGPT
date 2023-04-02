"""
This module holds riot games apis belonging to the summoner category.
https://developer.riotgames.com/apis#summoner-v4

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""

import requests


# Get a summoner by summoner name.
def get_summoner_by_name(
        api_key: str, summoner_name: str, server: str = 'euw1') -> requests.models.Response:
    return requests.get(
        "https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}"
        .format(server, summoner_name), headers={"X-Riot-Token": api_key})
