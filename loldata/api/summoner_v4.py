"""
This module handles the communication with the riotgames api.

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""

import requests as rq


# Get puuid
def get_puuid(name: str, api_key: str):
    """
        This gets the puuid by summoner name

        Args:
            name (str): The summoner name as a string.
            api_key (str): The api key as a string.

        Returns:
            Status 200: Returns the summeners puuid as a string.
            Status other: Returns the statuscode as an integer.
    """
    response = rq.get(
        "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(name),
        headers={"X-Riot-Token": api_key})
    if response.status_code == 200:
        return response.json()["puuid"]
    else:
        return {'status': response.status_code, 'body': response.json()["puuid"]}
