"""
This module handles the communication with the riotgames api.
https://developer.riotgames.com/apis#match-v5

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""

import requests as rq
from dacite import from_dict
from loldata import MatchDto
from loldata import MatchTimelineDto


# Get match ids
def get_match_ids(puuid: str, start: int, count: int, api_key: str):
    """
            This gets match ids by puuid.

            Args:
                puuid (str): The puuid of the player.
                start (int): The index where to start.
                count (int): Number of matches to retrieve, up to 100.
                api_key (str): The api key.

            Returns:
                response (dict): Returns a dictionary with the statuscode (int)
                and match ids (list).
    """
    response = rq.get("https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{}/"
                      "ids?start={}&count={}".format(puuid, start, count), headers={"X-Riot-Token": api_key})
    return {'status': response.status_code, 'body': response.json()}


# Get match
def get_match(match_id: str, api_key: str):
    """
            This gets a match by match id.

            Args:
                match_id (str): The match id.
                api_key (str): The api key.

            Returns:
                response (dict): Returns a dictionary with the statuscode (int)
                and a match (MatchDto).
    """
    response = rq.get("https://europe.api.riotgames.com/lol/match/v5/matches/{}".format(match_id),
                      headers={"X-Riot-Token": api_key})
    return {'status': response.status_code,
            'match': from_dict(data_class=MatchDto, data=response.json())}


# Get match timeline
def get_match_timeline(match_id: str, api_key: str):
    """
            This gets a matchs timeline by match id.

            Args:
                match_id (str): The match id.
                api_key (str): The api key.

            Returns:
                response (dict): Returns a dictionary with the statuscode (int)
                and a timeline (MatchTimelineDto).
    """
    response = rq.get("https://europe.api.riotgames.com/lol/match/v5/matches/{}/timeline"
                      .format(match_id), headers={"X-Riot-Token": api_key})
    return {'status': response.status_code,
            'timeline': from_dict(data_class=MatchTimelineDto, data=response.json())}
