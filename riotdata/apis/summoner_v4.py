"""
This module handles the communication with the riotgames apis.
https://developer.riotgames.com/apis#summoner-v4

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""

import requests


# Get a summoner by summoner name.
def get_summoner_by_name(name: str, api_key: str):
    return requests.get("https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}"
                        .format(name), headers={"X-Riot-Token": api_key})
