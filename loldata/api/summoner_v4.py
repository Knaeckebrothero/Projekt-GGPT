"""
This module handles the communication with the riotgames api.
https://developer.riotgames.com/apis#summoner-v4

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""

import requests as rq


# Get puuid
def get_puuid(name: str, api_key: str):
    """
        This gets the puuid by summoner name.

        Args:
            name (str): The summoner name.
            api_key (str): The api key.

        Returns:
            response (dict): Returns a dictionary with the statuscode (int)
            and puuid (str).
    """
    response = rq.get(
        "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(name),
        headers={"X-Riot-Token": api_key})
    return {'status': response.status_code, 'body': response.json()["puuid"]}
