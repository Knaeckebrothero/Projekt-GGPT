"""
This module handles the communication with the riotgames api.

Product -- GGPT
https://github.com/Knaeckebrothero/Projekt-GGPT
App ID -- 616160
https://developer.riotgames.com/
"""

import requests as rq
from dacite import from_dict
from loldata import MatchDto


# Gets a list of match ids, by puuid
def get_match_ids(puuid: str, start: int, count: int, api_key: str):
    response = rq.get("https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{}/"
                      "ids?start={}&count={}".format(puuid, start, count), headers={"X-Riot-Token": api_key})
    return response.json()


# Gets a match by match id
def get_match(match_id: str, api_key: str):
    response = rq.get("https://europe.api.riotgames.com/lol/match/v5/matches/{}".format(match_id),
                      headers={"X-Riot-Token": api_key})
    return from_dict(data_class=MatchDto, data=response.json())


# Gets the timeline of a match by match id
def get_match_timeline(match_id: str, api_key: str):
    response = rq.get("https://europe.api.riotgames.com/lol/match/v5/matches/{}/timeline"
                      .format(match_id), headers={"X-Riot-Token": api_key})
    return response.json()
